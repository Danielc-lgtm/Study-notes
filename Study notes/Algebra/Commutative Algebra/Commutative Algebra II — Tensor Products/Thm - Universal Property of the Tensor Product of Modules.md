---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Free Module"
  - "Def - Module Homomorphism"
  - "Def - Bilinear and Multilinear Maps"
  - "Def - Tensor Product of Modules"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; all modules unital. Let $R$ be a ring and $M, N, L$ be [[Def - Module|$R$-modules]]. We write $M\otimes_R N$ for the [[Def - Tensor Product of Modules|tensor product]], $m\otimes n$ for a pure tensor, $i = i_{M\otimes N} : M\times N\to M\otimes N$, $(m,n)\mapsto m\otimes n$, for the canonical [[Def - Bilinear and Multilinear Maps|bilinear map]], $\operatorname{Bil}_R(M\times N, L)$ for the bilinear maps $M\times N\to L$, and $\operatorname{Hom}_R(-,-)$ for $R$-linear maps. The full registry is on [[Commutative Algebra II — Tensor Products]].

---

# Statement

> **Theorem (Universal property of the tensor product).** Let $M, N$ be $R$-modules. For every $R$-module $L$ and every $R$-bilinear map $f : M\times N\to L$, there is a *unique* $R$-linear map $h : M\otimes_R N\to L$ such that $f = h\circ i$, i.e.
> $$h(m\otimes n) = f(m,n)\qquad\text{for all }(m,n)\in M\times N.$$
> Equivalently, post-composition with $i$ is a bijection, natural in $L$,
> $$\operatorname{Hom}_R(M\otimes_R N,\ L)\ \xrightarrow{\ \cong\ }\ \operatorname{Bil}_R(M\times N,\ L),\qquad h\mapsto h\circ i.$$

> **Corollary (Uniqueness of the tensor product).** If $(T, j)$ is any pair with $T$ an $R$-module and $j : M\times N\to T$ bilinear satisfying the same universal property, then there is a *unique* $R$-module isomorphism $\varphi : M\otimes_R N\to T$ with $\varphi\circ i = j$ (so $m\otimes n\mapsto j(m,n)$). Hence the tensor product is determined up to unique isomorphism.

> **Corollary (Vanishing criterion).** $\sum_{i=1}^\ell m_i\otimes n_i = 0$ in $M\otimes_R N$ if and only if $\sum_{i=1}^\ell f(m_i, n_i) = 0$ for *every* $R$-module $L$ and every $R$-bilinear map $f : M\times N\to L$.

The universal property — not the fraction model — is the working definition of the tensor product.

---

# Motivation

The construction of $M\otimes_R N$ as $F/K$ is a means to an end; on its own it is opaque, because deciding what holds in a quotient of an enormous free module is hard. This theorem is the payoff that makes the construction usable: it says the tensor product is exactly characterised by a single clean property, "every bilinear map factors through it uniquely as a linear map". Once you have this, you never touch the free-module presentation again. You build maps out of $M\otimes N$ by writing down bilinear maps; you identify $M\otimes N$ with known objects by matching the property; you prove tensors nonzero by exhibiting surviving bilinear maps. The theorem is what turns a definition into a tool.

The role it plays is to *convert* a hard kind of object — a map out of a quotient module, which would normally require checking well-definedness on representatives — into an easy kind — a bilinear map, checkable slot by slot. Becker phrases it as challenge-and-solution: you *challenge* $M\otimes N$ with a bilinear map $f$, and you are guaranteed a *unique solution* $h$, the linear map answering the challenge. The uniqueness half is as important as the existence half: it is what makes the tensor product *canonical*, so that any two constructions of it (the fraction model, a clever explicit model, an abstract one) are forced to be the same object up to unique isomorphism. This is why we may speak of "*the*" tensor product even though the construction looks arbitrary.

The deepest content is the reframing as a natural bijection $\operatorname{Hom}_R(M\otimes N, L)\cong\operatorname{Bil}_R(M\times N, L)$. This says $M\otimes N$ **represents** the bilinear-maps functor: it is the universal object whose linear maps *are* bilinear maps. Representability is the modern reason tensor products exist and are unique, and it is the entry point to the tensor–hom adjunction and the homological theory of the next chapter.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is "I have a bilinear map (or want to produce a linear map out of $M\otimes N$)". The skill is recognising bilinearity in disguise.

The first disguised source is **a formula on pure tensors that you want to be a well-defined linear map**. The property $B$ is "I have written $h(m\otimes n) = (\text{something in }m, n)$ and need it to extend to all tensors". The bridge: check the *something* is bilinear in $(m,n)$; then the theorem hands you a unique well-defined $h$, no representative-checking. The non-obvious part is that you *never* verify well-definedness directly — bilinearity is the entire obligation. *Example problem:* to define $\operatorname{tr} : V^*\otimes V\to k$, write $(\varphi\otimes v)\mapsto\varphi(v)$; since $(\varphi, v)\mapsto\varphi(v)$ is bilinear, $\operatorname{tr}$ exists and is unique.

The second disguised source is **a multiplication or pairing**. The property $B$ is "there is a product $M\times N\to L$ linear in each factor". Ring multiplication, scalar action, inner products, evaluation pairings, matrix multiplication are all bilinear, so each *is* a linear map out of a tensor product. The non-obviousness: multiplication, which is visibly nonlinear on the product, becomes a genuine linear map once you tensor. *Example problem:* the algebra structure of $A$ is the linear map $A\otimes_R A\to A$ induced by $(a,b)\mapsto ab$.

The third disguised source is **a candidate isomorphism you want to certify**. The property $B$ is "I conjecture $M\otimes N\cong T$ and have a bilinear map $j : M\times N\to T$". The bridge: if $(T, j)$ satisfies the universal property, the uniqueness corollary gives a *canonical* isomorphism for free; or build maps both ways via the property and check composites on pure tensors. The non-obviousness: matching a universal property proves isomorphism without exhibiting an explicit inverse. *Example problem:* prove $R\otimes_R M\cong M$ by checking $(r,m)\mapsto rm$ is universal.

The fourth disguised source is **a suspicion that a tensor is nonzero**. The property $B$ is "I cannot collapse $\sum m_i\otimes n_i$ to $0$". The bridge is the vanishing corollary: produce *one* bilinear $f$ with $\sum f(m_i,n_i)\neq 0$ and non-vanishing is certified. The non-obviousness: a *single well-chosen map* settles a question the relations cannot. *Example problem:* $2\otimes\bar1\neq 0$ in $2\mathbb{Z}\otimes\mathbb{Z}/2$ via $b(2x,\bar y) = \overline{xy}$.

**Targets (Output Amplification)**

The conclusion $C$ is "there is a unique linear $h$ with $h(m\otimes n) = f(m,n)$".

Combine $C$ with **a second bilinear map in the other direction**. Producing $h : M\otimes N\to T$ and $h' : T\to M\otimes N$ and checking $h'h$, $hh'$ are the identity *on generators* (pure tensors, which generate) yields $E$ = an isomorphism $M\otimes N\cong T$. The combination is nonobvious because checking on pure tensors suffices — generators determine a linear map — so you never verify equality of maps on all tensors. This is the standard route to every standard isomorphism.

Combine $C$ with **the functoriality of $\otimes$**. Given linear $f : M\to M'$, $g : N\to N'$, the bilinear map $(m,n)\mapsto f(m)\otimes g(n)$ induces (by $C$) the unique $f\otimes g : M\otimes N\to M'\otimes N'$. The result $E$ is the [[Thm - Functoriality of the Tensor Product|action of $\otimes$ on morphisms]] — the universal property is *what defines* $f\otimes g$. Nonobvious because functoriality is not assumed; it is manufactured from the universal property one map at a time.

Combine $C$ with **currying**. Reading $\operatorname{Bil}_R(M\times N, L)\cong\operatorname{Hom}_R(M, \operatorname{Hom}_R(N, L))$ together with $C$ gives the **tensor–hom adjunction** $\operatorname{Hom}_R(M\otimes N, L)\cong\operatorname{Hom}_R(M, \operatorname{Hom}_R(N, L))$. The result $E$ is that $-\otimes N$ is left adjoint to $\operatorname{Hom}_R(N, -)$, the structural fact behind right-exactness and $\operatorname{Tor}$. Nonobvious because it links tensor and hom, which look unrelated.

---

# Why Is It True

The construction was *built* to make this true, so the proof is really a verification that the four bilinearity relations are exactly the right ones. Start from the free module $F = R^{\oplus(M\times N)}$ on the set $M\times N$. A linear map *out of a free module* is the freest thing in module theory: it is determined by, and may be prescribed arbitrarily on, the basis. So an $R$-linear map $F\to L$ is the *same* as an arbitrary function $\{e_{m,n}\}\to L$, i.e. an arbitrary function $\hat f : M\times N\to L$ — no constraints at all.

Now $M\otimes N = F/K$, and a linear map $F/K\to L$ is the same as a linear map $F\to L$ that *vanishes on $K$*. What does "vanishes on $K$" demand of the corresponding function $\hat f : M\times N\to L$? Exactly that $\hat f$ respects the four generating relations of $K$: additivity in each slot and scalar-pulling from each slot. But "respects those four relations" is *verbatim* the definition of $R$-[[Def - Bilinear and Multilinear Maps|bilinear]]. So

$$\{\text{linear }h : M\otimes N\to L\} = \{\text{linear }F\to L\text{ vanishing on }K\} = \{\text{bilinear }f : M\times N\to L\},$$

and the bijection is precisely $h\mapsto h\circ i$. The existence half is "a bilinear $f$ gives a linear $F\to L$ vanishing on $K$, hence descends to $h$"; the uniqueness half is "two such $h$ agree on the generators $m\otimes n$, hence everywhere, since pure tensors generate".

**The whole theorem is the single observation that quotienting $F$ by exactly the bilinearity relations makes "linear out of the quotient" coincide with "bilinear out of $M\times N$" — no relation too many (or some bilinear maps would not descend), none too few (or $h$ would not be well-defined).**

The uniqueness *of the tensor product itself* (first corollary) is the standard universal-object argument: challenge $M\otimes N$ with $j$ to get $\varphi : M\otimes N\to T$; challenge $T$ with $i$ to get $\psi : T\to M\otimes N$; then $\psi\varphi$ solves the challenge "$M\otimes N$ with $i$", but so does the identity, and uniqueness of solutions forces $\psi\varphi = \operatorname{id}$; symmetrically $\varphi\psi = \operatorname{id}$. Universal objects are always unique up to unique isomorphism, for exactly this reason.

---

# What Makes This Hard

The conceptual hurdle is *trusting* that you may stop checking well-definedness: the instinct, trained on quotient constructions, is to verify that a formula on pure tensors does not depend on the representation, but the theorem says bilinearity *is* that verification, done once and for all. The non-obvious step in the proof is the translation "linear map vanishing on $K$ $\leftrightarrow$ function respecting the four relations $\leftrightarrow$ bilinear map" — recognising that the *generators* of $K$ are in bijection with the *clauses* of bilinearity. The most common error is to prove uniqueness of $h$ by some computation other than "pure tensors generate, so a linear map is determined by its values on them".

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use that maps out of a free module are unconstrained, then that maps out of a quotient are maps out of the free module killing the relation submodule, then that "killing the bilinearity relations" means "being bilinear". Get uniqueness from "pure tensors generate". For the second corollary, run the standard universal-object back-and-forth.

**Subgoal decomposition:**

1. **Maps out of $F$ are functions on $M\times N$.** Show $\operatorname{Hom}_R(F, L)\cong\{\text{functions }M\times N\to L\}$.
   - *Hint:* $F$ is free on the set $M\times N$; a linear map out of a free module is prescribed arbitrarily on the basis $\{e_{m,n}\}$.
   - *Why needed:* It is the unconstrained starting point against which the relations cut.

2. **Maps out of $F/K$ are maps out of $F$ vanishing on $K$.** Show $\operatorname{Hom}_R(F/K, L)\cong\{h\in\operatorname{Hom}_R(F,L) : h|_K = 0\}$.
   - *Hint:* Universal property of the quotient module: maps from $F/K$ are maps from $F$ killing $K$.
   - *Why needed:* It moves the question from $M\otimes N$ to $F$, where step 1 applies.

3. **Vanishing on $K$ equals bilinearity.** Show a function $M\times N\to L$ lifts to a map $F\to L$ killing $K$ iff it is bilinear.
   - *Hint:* The four generating families of $K$ are exactly the four clauses of the bilinearity definition; killing them = respecting them.
   - *Why needed:* It is the heart — it identifies the descended maps with bilinear maps.

4. **Existence and uniqueness of $h$.** Conclude $h$ exists, and is unique because pure tensors generate $M\otimes N$.
   - *Hint:* Compose steps 1–3 for existence; for uniqueness, two linear maps agreeing on the generating set $\{m\otimes n\}$ are equal.
   - *Why needed:* It is the statement.

5. **Uniqueness of the tensor product.** From the universal property, derive that any $(T, j)$ with it is uniquely isomorphic to $(M\otimes N, i)$.
   - *Hint:* Challenge each with the other's map; the two composites are solutions to identity-challenges, hence identities.
   - *Why needed:* It is the first corollary — canonicity of $\otimes$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Maps out of a free module are functions on the basis
> **Statement:** For the free module $F = R^{\oplus(M\times N)}$ with basis $\{e_{m,n}\}$, restriction to the basis gives a bijection $\operatorname{Hom}_R(F, L)\cong\{\text{functions }M\times N\to L\}$; any function extends uniquely to a linear map.
>
> **Hint:** The defining [[Def - Free Module|universal property of a free module]]: a linear map out of $R^{(X)}$ is the same as an arbitrary set map out of $X$.
>
> **Why needed:** It is the unconstrained baseline; the relations of $K$ will carve the bilinear maps out of all functions.
>
> > [!note]- Full proof
> > By the universal property of the [[Def - Free Module|free module]] $F = R^{\oplus(M\times N)}$, for any $R$-module $L$ and any function $\hat f : M\times N\to L$ (equivalently, any assignment $e_{m,n}\mapsto\hat f(m,n)$) there is a unique $R$-linear map $\tilde f : F\to L$ with $\tilde f(e_{m,n}) = \hat f(m,n)$, given on a general element $\sum_k r_k e_{m_k,n_k}$ by $\sum_k r_k\hat f(m_k, n_k)$. Restriction $h\mapsto((m,n)\mapsto h(e_{m,n}))$ is the inverse bijection. No relations are imposed, so *every* function arises.

> [!note]- Lemma 2: A function descends to $F/K$ iff it is bilinear
> **Statement:** A function $\hat f : M\times N\to L$ extends to a linear $\tilde f : F\to L$ with $\tilde f|_K = 0$ if and only if $\hat f$ is $R$-bilinear.
>
> **Hint:** Apply $\tilde f$ to each of the four generators of $K$ and read off the four clauses of [[Def - Bilinear and Multilinear Maps|bilinearity]].
>
> **Why needed:** It is the exact match between the relation submodule $K$ and the bilinearity definition — the crux of the theorem.
>
> > [!note]- Full proof
> > $K$ is generated by $e_{m,n_1}+e_{m,n_2}-e_{m,n_1+n_2}$, $e_{m_1,n}+e_{m_2,n}-e_{m_1+m_2,n}$, $re_{m,n}-e_{rm,n}$, $re_{m,n}-e_{m,rn}$. Since $\tilde f$ is linear, $\tilde f$ vanishes on $K$ iff it vanishes on each generator. Vanishing on the first family says $\hat f(m,n_1)+\hat f(m,n_2) = \hat f(m,n_1+n_2)$ (additivity in slot 2); on the second, additivity in slot 1; on the third, $r\hat f(m,n) = \hat f(rm,n)$; on the fourth, $r\hat f(m,n) = \hat f(m,rn)$. Together these are exactly the conditions for $\hat f$ to be $R$-bilinear. Conversely, if $\hat f$ is bilinear, $\tilde f$ vanishes on every listed generator, hence on $K$.

> [!note]- Lemma 3: Pure tensors generate, so $h$ is unique
> **Statement:** If $h_1, h_2 : M\otimes_R N\to L$ are $R$-linear and $h_1(m\otimes n) = h_2(m\otimes n)$ for all $(m,n)$, then $h_1 = h_2$.
>
> **Hint:** Pure tensors generate $M\otimes_R N$ as an $R$-module; a linear map is determined by its values on a generating set.
>
> **Why needed:** It supplies the uniqueness half of the theorem and is the reason "check on pure tensors" suffices everywhere.
>
> > [!note]- Full proof
> > Every element of $M\otimes_R N$ is a finite sum $\sum_k m_k\otimes n_k$ (pure tensors generate, by construction). If $h_1, h_2$ agree on each $m_k\otimes n_k$, then by linearity $h_1(\sum_k m_k\otimes n_k) = \sum_k h_1(m_k\otimes n_k) = \sum_k h_2(m_k\otimes n_k) = h_2(\sum_k m_k\otimes n_k)$. Hence $h_1 = h_2$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M, N, L$ be $R$-modules and $f : M\times N\to L$ an $R$-bilinear map. Recall $M\otimes_R N = F/K$ with $F = R^{\oplus(M\times N)}$, basis $\{e_{m,n}\}$, $K$ the bilinearity-relation submodule, and $i(m,n) = m\otimes n = e_{m,n} + K$.
>
> **Existence.** By **Lemma 1**, the assignment $e_{m,n}\mapsto f(m,n)$ extends to a unique $R$-linear $\tilde f : F\to L$. By **Lemma 2**, since $f$ is bilinear, $\tilde f$ vanishes on $K$. By the universal property of the quotient module, $\tilde f$ factors through $F/K = M\otimes_R N$: there is an $R$-linear $h : M\otimes_R N\to L$ with $h(x + K) = \tilde f(x)$. In particular $h(m\otimes n) = h(e_{m,n}+K) = \tilde f(e_{m,n}) = f(m,n)$, i.e. $f = h\circ i$.
>
> **Uniqueness.** If $h'$ also satisfies $h'(m\otimes n) = f(m,n)$ for all $(m,n)$, then $h$ and $h'$ agree on all pure tensors, so by **Lemma 3** $h = h'$.
>
> Thus $h\mapsto h\circ i$ is a bijection $\operatorname{Hom}_R(M\otimes_R N, L)\to\operatorname{Bil}_R(M\times N, L)$; naturality in $L$ is immediate from $h\mapsto h\circ i$ commuting with post-composition by linear maps $L\to L'$.
>
> ---
> **Corollary (uniqueness of the tensor product).** Let $(T, j)$ satisfy the same universal property. Challenge $M\otimes N$ with $j$: there is a unique linear $\varphi : M\otimes N\to T$ with $\varphi\circ i = j$. Challenge $T$ with $i$: there is a unique linear $\psi : T\to M\otimes N$ with $\psi\circ j = i$. Then $(\psi\circ\varphi)\circ i = \psi\circ j = i$, so $\psi\circ\varphi : M\otimes N\to M\otimes N$ is a solution to the challenge "$M\otimes N$ with $i$"; but $\operatorname{id}_{M\otimes N}$ is also a solution, so by uniqueness $\psi\circ\varphi = \operatorname{id}$. Symmetrically $\varphi\circ\psi = \operatorname{id}_T$. Hence $\varphi$ is an isomorphism with $\varphi(m\otimes n) = j(m,n)$, unique with $\varphi\circ i = j$.
>
> ---
> **Corollary (vanishing criterion).** If $\sum_i m_i\otimes n_i = 0$ and $f$ is any bilinear map, then $\sum_i f(m_i,n_i) = \sum_i h(m_i\otimes n_i) = h(\sum_i m_i\otimes n_i) = h(0) = 0$. Conversely, if $\sum_i m_i\otimes n_i\neq 0$, take $L = M\otimes N$ and $f = i$ itself: then $\sum_i f(m_i,n_i) = \sum_i m_i\otimes n_i\neq 0$. So vanishing of the tensor is equivalent to $\sum_i f(m_i,n_i) = 0$ for all bilinear $f$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The trace without a basis (linear algebra).** Define the trace of an operator $T\in\operatorname{End}(V)$, $V$ finite-dimensional, as the image of $T$ under $\operatorname{End}(V)\cong V^*\otimes V\xrightarrow{\operatorname{ev}}k$, where $\operatorname{ev}(\varphi\otimes v) = \varphi(v)$. The universal property makes $\operatorname{ev}$ well-defined from the bilinear pairing, and basis-independence is automatic — proving $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ and change-of-basis invariance for free. Nonobvious because it replaces the "sum of diagonal entries" definition by a canonical map, exactly the universal-property reflex. See [[Ex - The Kronecker product of matrices]].

**Construction of the cup product (algebraic topology).** The cup product on cohomology $H^p\times H^q\to H^{p+q}$ is bilinear, hence factors through $H^p\otimes H^q\to H^{p+q}$; the universal property is what lets one *define* the product as a single linear map and check its properties (associativity, graded-commutativity) on tensors. Nonobvious because a "multiplication on cohomology" is naturally a tensor-induced map, not a formula on cocycles.

**Multiplication of a quantum composite system (quantum information).** An observable on $\mathcal{H}_A\otimes\mathcal{H}_B$ built from local observables $X\otimes Y$ is the linear map induced by the bilinear $(X, Y)\mapsto X\otimes Y$; the universal property is what guarantees $X\otimes Y$ extends consistently to entangled (non-pure) states. Nonobvious because local data on product states must determine an operator on *all* states, which is precisely what the universal property certifies.

---

# Bridges

- **[[Def - Tensor Product of Modules|Tensor Product of Modules]]** — this theorem is the *meaning* of that construction. The free-module presentation $F/K$ is one model; the universal property is the characterisation that survives forgetting the model, and the uniqueness corollary is what licenses calling it "*the*" tensor product. Every later proof in the chapter cites this rather than the $F/K$ definition.

- **[[Thm - Functoriality of the Tensor Product|Functoriality of the Tensor Product]]** — the map $f\otimes g$ is *defined* by this theorem: the bilinear $(m,n)\mapsto f(m)\otimes g(n)$ induces the unique linear $f\otimes g$. So functoriality is not an extra axiom but a one-map-at-a-time application of the universal property, and composition $(f\otimes g)(h\otimes i) = (fh)\otimes(gi)$ follows by uniqueness.

- **[[Thm - Standard Isomorphisms of Tensor Products|Standard Isomorphisms]]** — every standard isomorphism (commutativity, associativity, distributivity, $R\otimes M\cong M$, the quotient rule) is proved by this theorem: build bilinear maps both ways, get linear maps by the property, check composites on pure tensors (where [[Thm - Universal Property of the Tensor Product of Modules#Lemma Decomposition|Lemma 3]] says agreement on generators suffices).

- **The tensor–hom adjunction** — currying a bilinear map gives $\operatorname{Bil}_R(M\times N, L)\cong\operatorname{Hom}_R(M, \operatorname{Hom}_R(N, L))$, which combined with this theorem yields $\operatorname{Hom}_R(M\otimes N, L)\cong\operatorname{Hom}_R(M, \operatorname{Hom}_R(N, L))$: $-\otimes N$ is left adjoint to $\operatorname{Hom}_R(N, -)$. This adjunction is the structural source of the right-exactness of $\otimes$ developed in [[Commutative Algebra III — Flatness and Exactness]].

- **[[Thm - Universal Property of the Tensor Product|Universal Property of the Tensor Product (vector spaces)]]** — this is the field-case special form, $V\otimes_k W$ for $k$ a field; the present theorem is the generalisation to an arbitrary commutative ring $R$, with the same proof. Over a field every module is free, so the vanishing subtleties disappear.

---

# Unlocked by This

> [!tip] Representable functors and Yoneda *(from Category Theory)*
> The statement "$M\otimes N$ represents $\operatorname{Bil}_R(M\times N, -)$" is the prototype of a **representable functor**, and the uniqueness corollary is the Yoneda-lemma fact that a representing object is unique up to unique isomorphism. Tensor products, free modules, localizations, and products are all "the object representing a functor of maps"; recognising this unifies every universal construction in the vault.

> [!tip] Adjoint functors and the tensor–hom adjunction *(from Homological Algebra)*
> The bijection $\operatorname{Hom}_R(M\otimes N, L)\cong\operatorname{Hom}_R(M, \operatorname{Hom}_R(N, L))$ exhibits $-\otimes N \dashv \operatorname{Hom}_R(N, -)$ as an **adjoint pair**. Left adjoints preserve colimits (hence $\otimes$ is right exact and preserves direct sums), and the failure of right-exactness to be exactness is measured by $\operatorname{Tor}$ — the gateway to [[Commutative Algebra III — Flatness and Exactness]].
