---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Weak and Lax Monoidal Functor"
  - "Def - Monoidal Category"
  - "Def - Monoid in a Monoidal Category"
  - "Def - Vector Space"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $k$ be a field and let $k[-] : (\mathbf{Set},\times,1)\to(\mathbf{Vect}_k,\otimes_k,k)$ be the **free vector space** functor: $k[X]$ is the [[Def - Vector Space|vector space]] with basis $X$ (formal finite $k$-linear combinations of elements of $X$), and on a function $f:X\to Y$, $k[f]$ extends $f$ linearly.

(a) Construct natural comparison maps $\varphi_{X,Y}:k[X]\otimes_k k[Y]\to k[X\times Y]$ and $\varphi_0:k\to k[1]$, and show they are **isomorphisms**, so $k[-]$ is a **weak (strong)** [[Def - Weak and Lax Monoidal Functor|monoidal functor]].

(b) Deduce that $k[-]$ sends [[Def - Monoid in a Monoidal Category|monoids]] to monoids: an ordinary monoid $M$ (a monoid in $(\mathbf{Set},\times)$) is carried to the **monoid algebra** $k[M]$ (a monoid in $(\mathbf{Vect}_k,\otimes_k)$, i.e. a $k$-algebra).

(c) Contrast with the forgetful functor $U:(\mathbf{Vect}_k,\otimes_k)\to(\mathbf{Set},\times)$: explain why $U$ is *not* (strong) monoidal for these tensor products.

**Recall:**

A [[Def - Weak and Lax Monoidal Functor|strong (weak) monoidal functor]] is a functor with *invertible* tensor and unit comparisons $\varphi_{A,B}:FA\boxtimes FB\to F(A\otimes B)$, $\varphi_0:J\to FI$, satisfying the coherence axioms:

![[Def - Weak and Lax Monoidal Functor#The Definition]]

A [[Def - Monoid in a Monoidal Category|monoid]] in $(\mathbf{Set},\times)$ is an ordinary monoid; a monoid in $(\mathbf{Vect}_k,\otimes_k)$ is a unital associative $k$-algebra. The free vector space $k[X]$ has the universal property that linear maps $k[X]\to V$ correspond to functions $X\to V$.

---

# Convergent Strategy

**Problem class:** This is a *structure-transport* problem from the topic page's catalogue: showing a functor preserves an algebraic structure ([[Def - Monoid in a Monoidal Category|monoids]]) by exhibiting a monoidal structure on it. It is the routine, foundational case ($\star$) that calibrates the harder lax examples.

**Assumption pattern:** The unlock is the universal property of $k[X]$: a basis of $k[X]\otimes_k k[Y]$ is pairs $(x,y)$, which is exactly a basis of $k[X\times Y]$, so the comparison is a bijection on bases and hence an isomorphism of vector spaces. Recognising that "free on $X$" interacts perfectly with $\otimes$ because tensor of free modules is free on the product basis is the key.

**Theorem routing:** Part (a) routes through the universal property of the free vector space (and of $\otimes_k$): define $\varphi$ on basis elements and check it is a basis bijection. Part (b) routes through the general principle (proved on [[Def - Weak and Lax Monoidal Functor]]) that a *lax* — hence in particular a strong — monoidal functor sends monoids to monoids; here it sends the set-monoid $M$ to the $k$-algebra $k[M]$. Part (c) is a non-existence argument: there is no natural comparison $U(V)\times U(W)\to U(V\otimes W)$.

**Key decision point:** The non-obvious choice in (c) is to see *why* the forgetful functor fails: the underlying set of $V\otimes_k W$ is not the product of the underlying sets — a general tensor is a *sum* of pure tensors $\sum_i v_i\otimes w_i$, not a single pair $(v,w)$. So there is no natural way to turn a pair $(v,w)$ into the full set $U(V\otimes W)$ surjectively, and the forgetful functor carries no monoidal comparison for $(\otimes,\times)$. The trap is to assume every functor between monoidal categories is monoidal; the comparison map must actually exist and be natural.

---

# Legal Operations Used

1. **The lax-transports-algebra principle (from [[Def - Weak and Lax Monoidal Functor]]).** Part (b) uses that any lax (hence strong) monoidal functor sends [[Def - Monoid in a Monoidal Category|monoids]] to monoids, since the comparison $\varphi$ lets the image of a multiplication compose.

2. **Operation 4 / universal-property recognition (topic page).** Part (a) uses the universal property of the free construction and of $\otimes_k$ to build and verify the comparison isomorphisms without choosing coordinates beyond the bases.

---

# Hints

> [!note]- Hint 1
> A basis of $k[X]\otimes_k k[Y]$ is $\{x\otimes y : x\in X, y\in Y\}$, and a basis of $k[X\times Y]$ is $\{(x,y):x\in X,y\in Y\}$. Define $\varphi$ on basis elements by $x\otimes y\mapsto (x,y)$.

> [!note]- Hint 2
> A linear map that sends a basis bijectively to a basis is an isomorphism. Check $\varphi$ does this; naturality in $X,Y$ follows because it is defined on basis elements compatibly with functions.

> [!note]- Hint 3
> For (b), recall a monoid in $(\mathbf{Set},\times)$ is an ordinary monoid $M$ with $\mu:M\times M\to M$ and $\eta:1\to M$. Apply $k[-]$ and post-compose with $\varphi$: $k[M]\otimes k[M]\xrightarrow{\varphi}k[M\times M]\xrightarrow{k[\mu]}k[M]$ is the algebra multiplication. The result is the monoid algebra (group algebra when $M$ is a group).

> [!note]- Hint 4
> For (c), ask: what is the underlying set of $V\otimes_k W$? An element is a *sum* $\sum_i v_i\otimes w_i$, not a single pair. So there is no natural surjection $U(V)\times U(W)\to U(V\otimes W)$ — pairs are not enough to name a general tensor. Hence no natural $\varphi$ exists for $U$ with $(\otimes,\times)$.

---

# Solution

The plan: (a) build $\varphi$ as the basis bijection $x\otimes y\mapsto(x,y)$ and $\varphi_0:k\to k[1]$ the unit, both isomorphisms; (b) transport monoids via the general lax-to-monoid principle, identifying the image as the monoid algebra; (c) argue no comparison exists for the forgetful functor because the underlying set of a tensor is not a product. The whole exercise rests on the fact that the tensor of free modules is free on the product basis.

**Step 1: The comparison maps are isomorphisms.**

Define $\varphi_{X,Y}:k[X]\otimes_k k[Y]\to k[X\times Y]$ by $x\otimes y\mapsto(x,y)$ on bases and $\varphi_0:k\to k[1]$ by $1\mapsto\ast$ (the single basis element). Both are isomorphisms, so $k[-]$ is strong monoidal.

> [!note]- Derivation
> The space $k[X]$ has basis $X$; by the universal property of the [[Def - Vector Space|tensor product]], $k[X]\otimes_k k[Y]$ has basis $\{x\otimes y:x\in X,y\in Y\}$. The space $k[X\times Y]$ has basis $X\times Y = \{(x,y)\}$. Define $\varphi_{X,Y}$ as the unique linear map with $\varphi(x\otimes y)=(x,y)$. It sends a basis bijectively onto a basis, hence is a linear isomorphism with inverse $(x,y)\mapsto x\otimes y$.
>
> Naturality: for functions $f:X\to X'$, $g:Y\to Y'$, both routes around the naturality square send $x\otimes y\mapsto (f(x),g(y))$, so $\varphi$ is natural.
>
> The unit comparison: $J=k$ is the unit of $(\mathbf{Vect}_k,\otimes_k)$ and $I=1$ (the one-point set) is the unit of $(\mathbf{Set},\times)$. Then $k[1]\cong k$ (basis $\{\ast\}$), and $\varphi_0:k\to k[1]$, $1\mapsto\ast$, is an isomorphism.
>
> The associativity and unit coherence axioms hold because both sides, on basis elements, send iterated tensors of basis vectors to the corresponding tuples, and the [[Def - Monoidal Category|associators/unitors]] of $\mathbf{Vect}_k$ and $\mathbf{Set}$ act by reassociating tuples; one checks the diagrams commute on bases, hence everywhere. Since $\varphi,\varphi_0$ are isomorphisms, $k[-]$ is a **strong (weak) [[Def - Weak and Lax Monoidal Functor|monoidal functor]]**.

**Step 2: Monoids go to monoid algebras.**

> [!note]- Derivation
> By the general principle (any lax monoidal functor sends [[Def - Monoid in a Monoidal Category|monoids]] to monoids — and strong is in particular lax), the strong monoidal functor $k[-]$ carries a monoid in $(\mathbf{Set},\times)$ to a monoid in $(\mathbf{Vect}_k,\otimes_k)$.
>
> Concretely, let $M$ be an ordinary monoid: $\mu:M\times M\to M$, $\eta:1\to M$ picking out the identity $e$. The image monoid has:
> - underlying object $k[M]$;
> - multiplication $\;k[M]\otimes_k k[M]\xrightarrow{\ \varphi\ }k[M\times M]\xrightarrow{\ k[\mu]\ }k[M]$, which on basis elements is $m\otimes m'\mapsto (m,m')\mapsto mm'$ and extends bilinearly: $(\sum a_m m)(\sum b_{m'} m')=\sum_{m,m'}a_m b_{m'}(mm')$;
> - unit $\;k\xrightarrow{\varphi_0}k[1]\xrightarrow{k[\eta]}k[M]$, sending $1\mapsto e$.
>
> This is exactly the **monoid algebra** $k[M]$ — the $k$-algebra whose multiplication extends the monoid law linearly. When $M=G$ is a group it is the **group algebra** $k[G]$. The associativity and unit of $k[M]$ as an algebra are guaranteed *automatically* by the monoidal-functor axioms, with no separate verification, which is the whole convenience of the transport principle.

**Step 3: The forgetful functor is not monoidal for $(\otimes,\times)$.**

> [!note]- Derivation
> Let $U:\mathbf{Vect}_k\to\mathbf{Set}$ be the underlying-set functor. A (lax) monoidal structure for the pair $(\otimes_k,\times)$ would require a natural map
> $$\varphi^U_{V,W}: U(V)\times U(W)\longrightarrow U(V\otimes_k W),$$
> i.e. a natural rule turning a pair $(v,w)$ of vectors into an element of $V\otimes_k W$. There *is* such a map, $(v,w)\mapsto v\otimes w$ (the pure-tensor map) — so $U$ is *lax* monoidal. But it is **not strong**: $v\otimes w$ ranges only over *pure* tensors, while a general element of $V\otimes_k W$ is a sum $\sum_i v_i\otimes w_i$ of several pure tensors. The underlying set $U(V\otimes_k W)$ is strictly larger than the image of $U(V)\times U(W)$ (whenever $\dim V,\dim W\geq 2$), so $\varphi^U$ is not surjective, hence not an isomorphism. Therefore $U$ is lax but not strong monoidal for $(\otimes,\times)$.
>
> The conceptual upshot: the underlying set of a tensor product is *not* the product of the underlying sets — pairs cannot name sums of pure tensors. This is exactly why a $k$-algebra's multiplication is not recovered by forgetting to sets, and why the *free* functor (which is strong) is the one that transports monoids cleanly, while the forgetful functor only does so laxly. (Note the lax direction still transports *comonoids* dually and is responsible for other structure; the failure is specifically the strong/invertible level.)

> [!note]- Complete formal solution
> **(a)** Define $\varphi_{X,Y}:k[X]\otimes_k k[Y]\to k[X\times Y]$ by $x\otimes y\mapsto(x,y)$ on bases; it is a bijection of bases, hence a linear isomorphism, and is natural in $X,Y$. Define $\varphi_0:k\to k[1]\cong k$, $1\mapsto\ast$, an isomorphism. The coherence axioms hold on bases (associators/unitors reassociate tuples), so $k[-]$ is a strong [[Def - Weak and Lax Monoidal Functor|monoidal functor]].
>
> **(b)** A strong monoidal functor is lax, so it sends [[Def - Monoid in a Monoidal Category|monoids]] to monoids. The monoid $M$ in $(\mathbf{Set},\times)$ maps to $k[M]$ with multiplication $k[\mu]\circ\varphi$ (i.e. $m\otimes m'\mapsto mm'$ extended bilinearly) and unit $k[\eta]\circ\varphi_0$ ($1\mapsto e$) — the monoid algebra $k[M]$, a $k$-algebra; the group algebra $k[G]$ when $M=G$.
>
> **(c)** $U:\mathbf{Vect}_k\to\mathbf{Set}$ admits the pure-tensor comparison $(v,w)\mapsto v\otimes w$, making it *lax* monoidal, but this is not surjective onto $U(V\otimes_k W)$ (general tensors are sums of pure tensors), so it is **not strong** for $(\otimes_k,\times)$. The underlying set of a tensor is not the product of the underlying sets. $\qquad\blacksquare$

---

# Key Takeaways

**Strong monoidal functors transport monoids, and the free functor is the cleanest example because tensor of free objects is free on the product basis.** The mechanism behind part (b) — a [[Def - Weak and Lax Monoidal Functor|strong (or lax) monoidal functor]] carries [[Def - Monoid in a Monoidal Category|monoids]] to monoids — is one of the most-used facts in algebra, and the free vector space functor is its calibrating instance. The reason $k[-]$ is *strong* (comparison invertible, not merely lax) is the special algebraic fact that $k[X]\otimes_k k[Y]\cong k[X\times Y]$: tensoring free modules gives the free module on the product of bases. Whenever a "free" construction is in play, expect it to be strong monoidal and hence to transport algebraic structure perfectly — free groups, free monoids, free algebras, and free modules all behave this way, which is why "the monoid algebra," "the group algebra," and "the tensor algebra" are constructed exactly by this transport.

**Whether a functor is monoidal at all — and at which level — is a real condition, not a formality.** Part (c) is the cautionary half: the forgetful functor, which one might naively expect to "obviously" respect both products, is only *lax* and not *strong* for $(\otimes,\times)$, because the underlying set of a tensor product is genuinely larger than the product of underlying sets. The lesson is to always check the comparison map: does it exist naturally, and is it invertible? The answer determines whether the functor transports monoids (lax suffices), gives a monoidal equivalence (strong needed), or fails to interact with the tensors at all. This diagnostic — exists? invertible? which direction? — is the decision tree from [[Def - Weak and Lax Monoidal Functor]], and it must be run, not assumed.

**The underlying set of a tensor product is not the product of underlying sets — pairs cannot name sums of pure tensors.** This single fact, surfaced in part (c), explains a great deal: why bilinear algebra is more than pairs of vectors, why the tensor product needs its universal property rather than a naive set-level definition, and why $\otimes$ and $\times$ are genuinely different monoidal structures. A general tensor $\sum_i v_i\otimes w_i$ has no expression as one pair $(v,w)$, so any construction that tries to recover the tensor from pairs (the forgetful functor's comparison) is non-surjective. Internalising this prevents a whole class of errors in which one treats a tensor like a Cartesian product; the trigger is the appearance of $\otimes$ where one is tempted to manipulate "elements as pairs."
