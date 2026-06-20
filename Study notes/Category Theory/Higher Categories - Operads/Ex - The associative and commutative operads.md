---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Operad"
  - "Def - Algebra for an Operad"
  - "Def - Monoid in a Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Define the **associative operad** $\mathrm{Assoc}$ in $\mathbf{Set}$ by $\mathrm{Assoc}(n) = S_n$ (the symmetric group, with right multiplication as the $S_n$-action) and the **commutative operad** $\mathrm{Comm}$ by $\mathrm{Comm}(n) = \{*\}$ (a one-point set, trivial $S_n$-action). 

(a) Give the operadic composition $\gamma$ for each, and verify both are operads.

(b) Prove that $\mathrm{Assoc}$-algebras in $\mathbf{Set}$ are exactly [[Def - Monoid in a Monoidal Category|monoids]], and that $\mathrm{Comm}$-algebras are exactly commutative monoids.

(c) Exhibit the unique operad morphism $\mathrm{Assoc} \to \mathrm{Comm}$, and explain in operadic terms why "every commutative monoid is a monoid" but not conversely.

**Recall:**

![[Def - Operad#The Definition]]

An [[Def - Algebra for an Operad|algebra]] over an operad $P$ in $\mathbf{Set}$ is a set $X$ with maps $\rho_n : P(n) \times X^n \to X$, $S_n$-equivariant, compatible with $\gamma$ and the unit. A [[Def - Monoid in a Monoidal Category|monoid]] is a set with an associative unital binary product.

---

# Convergent Strategy

**Problem class:** This is a *compute-the-algebras-of-a-given-operad* problem, the central recurring task of §3. The method: identify the generating operations (the small-arity pieces), see what an algebra structure assigns to them, and read off the classical structure from the operad's relations.

**Assumption pattern:** The signal is "an operad given explicitly arity by arity, with a recognisable group or point in each arity". For $\mathrm{Assoc}$, $\mathrm{Assoc}(n) = S_n$ means an $n$-ary operation is an *ordering* of the inputs — exactly what an associative non-commutative product needs. For $\mathrm{Comm}$, $\mathrm{Comm}(n) = \{*\}$ means there is *one* operation regardless of order, which is commutativity. The arity-$2$ part is where the generating product lives; the relations live in arity $3$ (associativity) and in the $S_2$-action (commutativity).

**Theorem routing:** Part (b) routes through the definition of [[Def - Algebra for an Operad|operad-algebra]]: an algebra structure is determined by where the generating binary operation goes, and the operad relations become the monoid axioms. Part (c) routes through the universal/terminal property: $\mathrm{Comm}$ is the *terminal reduced operad* (one operation per arity), so there is a unique map to it from any operad, and pulling back a $\mathrm{Comm}$-algebra structure along $\mathrm{Assoc} \to \mathrm{Comm}$ gives an $\mathrm{Assoc}$-algebra — which is the operadic content of "commutative $\Rightarrow$ associative".

**Key decision point:** The crux of (b) is recognising that $\mathrm{Assoc}(2) = S_2 = \{e, (1\,2)\}$ has *two* elements, corresponding to the products $xy$ and $yx$, while $\mathrm{Comm}(2) = \{*\}$ has *one*. This is where commutativity is forced or not: in $\mathrm{Comm}$ the unique binary operation must be invariant under the swap, so $xy = yx$; in $\mathrm{Assoc}$ the two orderings are distinct operations, so the product need not commute. The temptation is to treat the two operads as "the same up to the $S_n$-action" — they are not; the action is exactly the difference.

---

# Legal Operations Used

1. **Read an algebra structure off the generating operation (operation 4 from the topic page).** An algebra over $\mathrm{Assoc}$ or $\mathrm{Comm}$ is determined by the image of the binary operation; we extract the monoid product from it.

2. **Translate operad relations into algebra axioms (operation 2 from the topic page).** Associativity in arity $3$ and the $S_2$-action become the monoid associativity and (for $\mathrm{Comm}$) commutativity.

3. **Use terminality of $\mathrm{Comm}$ to build an operad morphism (operation 6 from the topic page).** The unique map $\mathrm{Assoc} \to \mathrm{Comm}$ collapses each $S_n$ to the point.

---

# Hints

> [!note]- Hint 1
> $\mathrm{Assoc}(2) = S_2 = \{e, \tau\}$. Think of $e$ as the product $x_1 x_2$ and $\tau$ as $x_2 x_1$. What is $\mathrm{Comm}(2)$, and what does the single element correspond to?

> [!note]- Hint 2
> An $\mathrm{Assoc}$-algebra structure on $X$ assigns to $e \in \mathrm{Assoc}(2)$ a binary map $m : X^2 \to X$. Equivariance forces the value on $\tau$ to be $m$ with arguments swapped. The arity-$3$ relation $\gamma(e; e, \mathrm{id}) = \gamma(e; \mathrm{id}, e)$ in $\mathrm{Assoc}$ (both equal the unique ordering of $3$ elements built from the binary one) becomes associativity of $m$.

> [!note]- Hint 3
> For $\mathrm{Comm}$, equivariance under the *trivial* action forces $m(x,y) = m(y,x)$ directly, because the single operation must equal itself after the swap, and the algebra's equivariance turns that into $m(x,y) = m(y,x)$.

> [!note]- Hint 4
> The map $\mathrm{Assoc} \to \mathrm{Comm}$ sends every $\sigma \in S_n$ to the unique point $* \in \mathrm{Comm}(n)$. Check this is an operad map (it trivially preserves everything). A $\mathrm{Comm}$-algebra pulled back along it is a $\mathrm{Comm}$-algebra *viewed as* an $\mathrm{Assoc}$-algebra — i.e. a commutative monoid viewed as a monoid.

---

# Solution

The plan: verify both are operads by exhibiting $\gamma$ (Step 1); compute algebras by tracking the binary generator and the arity-$3$ relation (Steps 2–3); then build the operad morphism and interpret the restriction functor on algebras (Step 4).

**Step 1: Both are operads.**

> [!note]- Derivation
> *$\mathrm{Comm}$.* With $\mathrm{Comm}(n) = \{*\}$, there is a unique candidate for every $\gamma$, unit, and action, and all axioms hold trivially because every set involved is a point. So $\mathrm{Comm}$ is an operad — indeed the terminal reduced operad.
>
> *$\mathrm{Assoc}$.* With $\mathrm{Assoc}(n) = S_n$, the unit is $e \in S_1$. The composition $\gamma : S_k \times S_{n_1} \times \dots \times S_{n_k} \to S_{n_1 + \dots + n_k}$ is the *block substitution*: given an ordering $\sigma$ of $k$ blocks and orderings $\tau_i$ within each block, produce the ordering of $n_1 + \dots + n_k$ elements that arranges the blocks by $\sigma$ and the elements inside block $i$ by $\tau_i$. Concretely $\gamma(\sigma; \tau_1, \dots, \tau_k) = \sigma\langle n_1, \dots, n_k\rangle \cdot (\tau_{\sigma^{-1}(1)} \oplus \dots)$, the block permutation composed with the within-block ones. Associativity of $\gamma$ is associativity of "arrange blocks of blocks"; the unit law is immediate; equivariance is the defining compatibility of block permutations with the $S_n$-actions. So $\mathrm{Assoc}$ is an operad.

**Step 2: $\mathrm{Assoc}$-algebras are monoids.**

> [!note]- Derivation
> Let $X$ be an $\mathrm{Assoc}$-algebra with structure maps $\rho_n : S_n \times X^n \to X$. Write $m(x,y) = \rho_2(e; x, y)$ for the value on the identity ordering $e \in S_2$. Equivariance gives $\rho_2(\tau; x, y) = \rho_2(e; y, x) = m(y, x)$. The nullary part: $\rho_0(* ; ) = \rho_0(e_{S_0}) =: 1 \in X$ is a chosen element. The unit law of the algebra says $\rho_1(e; x) = x$.
>
> *Associativity.* In $\mathrm{Assoc}(3) = S_3$, the operation $\gamma(e_{S_2}; e_{S_2}, e_{S_1})$ — multiply the first two, then with the third — and $\gamma(e_{S_2}; e_{S_1}, e_{S_2})$ — multiply the last two, then the first — are both the identity ordering of $3$ elements (they describe $((x_1 x_2) x_3)$ and $(x_1 (x_2 x_3))$, which are *the same element* $e \in S_3$ because $\mathrm{Assoc}$ has no relations beyond the group structure and both bracketings give the identity permutation). Applying $\rho_3$ and using compatibility with $\gamma$, $m(m(x,y), z) = m(x, m(y,z))$. So $m$ is associative.
>
> *Unit element.* The algebra-unit and the nullary operation $1$ give $m(1, x) = x = m(x, 1)$ via the arity-$(0,1)$ composition relations. Hence $(X, m, 1)$ is a [[Def - Monoid in a Monoidal Category|monoid]]. Conversely a monoid $(X, m, 1)$ defines an $\mathrm{Assoc}$-algebra: send $\sigma \in S_n$ to the operation "multiply the $n$ inputs in the order $\sigma$", which is well-defined and associative-compatible. The two constructions are inverse, so $\mathrm{Alg}_{\mathrm{Assoc}} \cong \mathbf{Mon}$.

**Step 3: $\mathrm{Comm}$-algebras are commutative monoids.**

> [!note]- Derivation
> Let $X$ be a $\mathrm{Comm}$-algebra, $m(x,y) = \rho_2(*; x, y)$. Equivariance under the *trivial* $S_2$-action says $\rho_2(* \cdot \tau; x, y) = \rho_2(*; y, x)$, i.e. $\rho_2(*; x, y) = \rho_2(*; y, x)$ since $* \cdot \tau = *$. Thus $m(x,y) = m(y,x)$ — commutativity. Associativity follows exactly as in Step 2 (the unique arity-$3$ operation, built from $m$ both ways, forces $m(m(x,y),z) = m(x,m(y,z))$). The nullary point gives a unit. So $X$ is a commutative monoid, and conversely; hence $\mathrm{Alg}_{\mathrm{Comm}} \cong \mathbf{CMon}$.

**Step 4: The morphism $\mathrm{Assoc} \to \mathrm{Comm}$ and the implication.**

> [!note]- Derivation
> Define $p : \mathrm{Assoc} \to \mathrm{Comm}$ by $p_n : S_n \to \{*\}$, the unique map. It preserves the unit ($e \mapsto *$), composition (everything lands in points), and the $S_n$-action (trivially), so $p$ is an operad morphism — in fact the unique one, since $\mathrm{Comm}$ is terminal among reduced operads. Restriction along $p$ is a functor $p^* : \mathrm{Alg}_{\mathrm{Comm}} \to \mathrm{Alg}_{\mathrm{Assoc}}$: a $\mathrm{Comm}$-algebra $X$ becomes an $\mathrm{Assoc}$-algebra by $\rho^{\mathrm{Assoc}}_n(\sigma; x_\bullet) = \rho^{\mathrm{Comm}}_n(p_n(\sigma); x_\bullet) = \rho^{\mathrm{Comm}}_n(*; x_\bullet)$, which ignores $\sigma$. In monoid terms, $p^*$ is the inclusion $\mathbf{CMon} \hookrightarrow \mathbf{Mon}$: a commutative monoid *is* a monoid. There is no operad map $\mathrm{Comm} \to \mathrm{Assoc}$ over the identity making the converse work, because such a map would have to choose, for each arity, a single $S_n$-invariant element of $S_n$ compatible with composition — and for $n \geq 2$ the only $S_n$-fixed point under right multiplication does not exist ($S_n$ acts freely), so the binary operation cannot be sent to a commutative one. This is the operadic reason a monoid need not be commutative.

> [!note]- Complete formal solution
> *Operads.* $\mathrm{Comm}(n) = \{*\}$ is the terminal reduced operad (all axioms trivial). $\mathrm{Assoc}(n) = S_n$ with $\gamma$ the block substitution $\gamma(\sigma; \tau_\bullet) = \sigma\langle n_\bullet\rangle \cdot (\tau_\bullet)$, unit $e \in S_1$, action by right multiplication; associativity, unit, equivariance hold by the block-permutation calculus.
>
> *Algebras.* For an $\mathrm{Assoc}$-algebra put $m(x,y) = \rho_2(e;x,y)$; equivariance gives $\rho_2(\tau;x,y) = m(y,x)$, the arity-$3$ identity gives associativity, and the nullary operation gives a unit, so $\mathrm{Alg}_{\mathrm{Assoc}} \cong \mathbf{Mon}$. For a $\mathrm{Comm}$-algebra, trivial-action equivariance gives $m(x,y) = m(y,x)$, and associativity as before, so $\mathrm{Alg}_{\mathrm{Comm}} \cong \mathbf{CMon}$.
>
> *Morphism.* The unique $p : \mathrm{Assoc} \to \mathrm{Comm}$ (collapse each $S_n$ to a point) induces $p^* : \mathbf{CMon} \hookrightarrow \mathbf{Mon}$, the statement "commutative monoid is a monoid". No section exists because $S_n$ has no fixed point under right multiplication for $n \geq 2$, so a monoid need not be commutative. $\blacksquare$

---

# Key Takeaways

**The symmetric-group action is the dial between associative and commutative.** The cleanest lesson here is that $\mathrm{Assoc}$ and $\mathrm{Comm}$ differ *only* in their $S_n$-pieces — $S_n$ versus a point — and that difference is exactly the difference between "order matters" and "order does not". This is a precise instance of a general phenomenon: the more an operad's $S_n$-action collapses operations together, the more commutative its algebras. Carrying this dial in mind lets you predict, from the size of $P(n)$ as an $S_n$-set, how much commutativity the algebras have: free $S_n$-action means fully non-commutative (each ordering a distinct operation), trivial action means fully commutative. The little-disks operads $E_n$ interpolate exactly along this dial, from $E_1 \simeq \mathrm{Assoc}$ to $E_\infty \simeq \mathrm{Comm}$.

**Relations live in arity three; the binary operation lives in arity two.** A reusable diagnostic for reading an operad's algebras: the *generators* sit in low arity (here, the binary product in arity $2$), and the *relations* sit one arity higher (associativity is an arity-$3$ statement). When you want to know what kind of algebra an operad presents, examine $P(2)$ to find the products and $P(3)$ to find the relations among them. This is why "associative" and "Lie" are arity-$3$ conditions (associativity, Jacobi) on an arity-$2$ generator (product, bracket), and it tells you where to look first when handed an unfamiliar operad.

**Terminality and the restriction functor encode implications between structures.** That there is a unique operad map $\mathrm{Assoc} \to \mathrm{Comm}$ and that restriction along it is the inclusion $\mathbf{CMon} \hookrightarrow \mathbf{Mon}$ is the operadic mechanism behind *every* "structure-with-more-axioms is a structure-with-fewer-axioms" implication. The general pattern: an operad map $P \to Q$ induces a restriction $\mathrm{Alg}_Q \to \mathrm{Alg}_P$ (note the direction reversal — a $Q$-algebra is automatically a $P$-algebra), and the *existence or non-existence* of such maps tells you which forgetful relationships hold between algebra types. When you want to know "is every $Q$-algebra a $P$-algebra?", the question becomes "is there an operad map $P \to Q$?" — a finite, checkable question about operations and relations rather than a case analysis on algebras.
