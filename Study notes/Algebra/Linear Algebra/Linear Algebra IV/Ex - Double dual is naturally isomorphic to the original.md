---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Dual Space"
  - "Def - Dual Map"
  - "Def - Linear Map"
  - "Thm - Dimension of Dual Space"
  - "Thm - Fundamental Theorem of Linear Maps"
tags: [algebra, linear-algebra]
---

# Problem Statement

The **double dual** of $V$ is the dual of $V'$, denoted $V'' = (V')' = \mathcal{L}(V', \mathbb{F})$. Define the **evaluation map** $\Lambda : V \to V''$ by
$$(\Lambda v)(\varphi) = \varphi(v) \qquad \text{for } v \in V, \varphi \in V'.$$
That is, $\Lambda v$ is the functional on $V'$ that evaluates each $\varphi$ at the fixed vector $v$.

Prove the following.

1. $\Lambda$ is a linear map from $V$ to $V''$.
2. $\Lambda$ is **injective**.
3. If $V$ is finite-dimensional, $\Lambda$ is an isomorphism — so $V \cong V''$ canonically (no choice of basis required).
4. The isomorphism $\Lambda$ is *natural* in the sense that for any $T \in \mathcal{L}(V)$, the dual-of-dual $T'' = (T')' : V'' \to V''$ satisfies
$$T'' \circ \Lambda = \Lambda \circ T.$$
Contrast this with the non-canonical isomorphism $V \cong V'$ in finite dimensions, which requires choosing a basis.

**Recall:**

![[Def - Dual Space#The Definition]]

The [[Def - Dual Map|dual map]] of $T \in \mathcal{L}(V, W)$ is $T' \in \mathcal{L}(W', V')$ defined by $T'(\varphi) = \varphi \circ T$.

![[Thm - Dimension of Dual Space#Statement]]

A linear map between finite-dimensional spaces of the same dimension is an isomorphism iff it is injective.

---

# Convergent Strategy

**Problem class.** This is the central *natural-vs-unnatural isomorphism* exercise of the chapter (problem class 4 from the [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Problem-Solving Strategy|topic page]]). The goal is to establish the canonical isomorphism $V \cong V''$ in finite dimensions and contrast it with the basis-dependent isomorphism $V \cong V'$. The result is the cleanest instance of *naturality* in linear algebra.

**Assumption pattern.** The recognisable signal is "$V''$" or "double dual" in the problem statement. The constructive part is writing down the evaluation map $\Lambda$ explicitly. The verification has three parts: linearity, injectivity, and surjectivity (or equivalently, the dimension argument).

**Theorem routing.** The route has four parts:
- *Linearity of $\Lambda$* uses pointwise linearity of the operations on $V''$.
- *Injectivity of $\Lambda$* uses the existence of "enough" functionals: for any nonzero $v$, there is a $\varphi$ with $\varphi(v) \neq 0$.
- *Surjectivity* (in finite dimensions) follows from dimension counting: $\dim V'' = \dim V' = \dim V$, and an injective linear map between same-dimensional spaces is automatically surjective.
- *Naturality* is verified by direct computation, using the definition of $T''$.

**Key decision point.** The non-obvious move is *recognising the existence of separating functionals*. For injectivity, we need: $v \neq 0$ implies some $\varphi$ separates $v$ from $0$ (i.e. $\varphi(v) \neq 0$). In finite dimensions this is easy via the dual basis (one of the dual-basis functionals must give nonzero on $v$ since $v$ has a nonzero coordinate). In infinite dimensions this is the [[Def - Dual Space|Hahn-Banach theorem]], a deep theorem of functional analysis. The exercise teaches the structural pattern: *naturality lives at the level of existence of separating functionals*.

---

# Legal Operations Used

From [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Legal Operations|the topic page]]:

1. **Build a linear functional to expose structure** (operation 4). The whole exercise is about the natural evaluation functional $\operatorname{ev}_v(\varphi) = \varphi(v)$, which builds an element of $V''$ from each $v \in V$.

2. **Apply the evaluation map $\Lambda$** (operation 8). The exercise is the proof that $\Lambda$ is well-defined, linear, injective, and an isomorphism in finite dimensions.

3. **Dualize a map to reverse direction** (operation 6). The naturality statement uses the double-dual map $T''$, applied twice to reverse direction back to the original.

---

# Hints

> [!note]- Hint 1
> The evaluation map $\Lambda$ is "swap the roles of vector and functional": instead of $\varphi(v)$ as "$\varphi$ evaluated at $v$", view it as "$v$ evaluated at $\varphi$", giving a functional $\Lambda v$ on the space of functionals.

> [!note]- Hint 2
> Linearity of $\Lambda$ means: $\Lambda(v_1 + v_2) = \Lambda v_1 + \Lambda v_2$ as functionals on $V'$. Check at each $\varphi$: $(\Lambda(v_1 + v_2))(\varphi) = ?$.

> [!note]- Hint 3
> For injectivity, suppose $\Lambda v = 0$. This means $(\Lambda v)(\varphi) = \varphi(v) = 0$ for every $\varphi \in V'$. Why must $v = 0$? Use the dual basis: if $v$ had a nonzero coordinate, the corresponding dual-basis functional would give a nonzero value.

> [!note]- Hint 4
> In finite dimensions, $\dim V'' = \dim V$. An injective linear map between equidimensional spaces is automatically surjective. So once injectivity is established, the isomorphism follows.

> [!note]- Hint 5
> For naturality: compute $(T''(\Lambda v))(\varphi)$ using the definition of $T''$ (= dual of $T'$) twice, and compute $(\Lambda(Tv))(\varphi)$ using the definition of $\Lambda$. Both should equal $\varphi(Tv)$.

---

# Solution

The solution has four steps. Step 1 verifies $\Lambda$ is linear by checking at each $\varphi$. Step 2 verifies injectivity by using the dual basis. Step 3 invokes dimension counting to conclude surjectivity in finite dimensions. Step 4 verifies naturality by direct computation. The non-obvious move is in Step 2, where injectivity uses the existence of *separating functionals* — every nonzero vector has some functional that detects it.

**Step 1: $\Lambda$ is linear.**

For $v, w \in V$ and $\lambda \in \mathbb{F}$:
$$\Lambda(v + w) = \Lambda v + \Lambda w, \qquad \Lambda(\lambda v) = \lambda \Lambda v.$$

> [!note]- Derivation
> Two elements of $V''$ are equal iff they agree at every $\varphi \in V'$. For $\varphi \in V'$:
> $$(\Lambda(v + w))(\varphi) = \varphi(v + w) = \varphi(v) + \varphi(w) = (\Lambda v)(\varphi) + (\Lambda w)(\varphi) = (\Lambda v + \Lambda w)(\varphi),$$
> using the definition of $\Lambda$ (twice), linearity of $\varphi$, and the pointwise definition of addition in $V''$. So $\Lambda(v + w) = \Lambda v + \Lambda w$ in $V''$.
>
> Similarly:
> $$(\Lambda(\lambda v))(\varphi) = \varphi(\lambda v) = \lambda \varphi(v) = \lambda (\Lambda v)(\varphi) = (\lambda \Lambda v)(\varphi),$$
> using linearity of $\varphi$ and the pointwise definition of scalar multiplication. So $\Lambda(\lambda v) = \lambda \Lambda v$.
>
> Hence $\Lambda$ is linear.

**Step 2: $\Lambda$ is injective.**

If $\Lambda v = 0$ in $V''$, then $v = 0$ in $V$.

> [!note]- Derivation
> Suppose $\Lambda v = 0$, i.e. $(\Lambda v)(\varphi) = 0$ for every $\varphi \in V'$. By the definition of $\Lambda$, this is $\varphi(v) = 0$ for every $\varphi \in V'$.
>
> *Claim: this forces $v = 0$.*
>
> Suppose for contradiction $v \neq 0$. Then $v$ extends to a basis of $V$: by the [[Thm - Every Linearly Independent List Extends to a Basis|extension lemma]], there is a basis $v_1 = v, v_2, \dots, v_n$ of $V$ (or, in finite dimensions, choose any basis containing $v$ — for instance, complete $\{v\}$ to a basis). Let $\varphi_1, \dots, \varphi_n$ be the dual basis. Then $\varphi_1(v) = \varphi_1(v_1) = \delta_{11} = 1 \neq 0$, contradicting $\varphi(v) = 0$ for every $\varphi$.
>
> Hence $v = 0$. So $\operatorname{null} \Lambda = \{0\}$, and $\Lambda$ is injective.
>
> *(Remark on infinite dimensions: the construction above uses the existence of a basis of $V$ that includes $v$. In infinite dimensions this requires the axiom of choice via the Hamel-basis theorem, or alternatively the **Hahn-Banach theorem**, which directly produces a separating functional.)*

**Step 3: In finite dimensions, $\Lambda$ is an isomorphism.**

By Step 2, $\Lambda$ is injective. We need surjectivity.

> [!note]- Derivation
> By [[Thm - Dimension of Dual Space|the dual dimension theorem]], $\dim V' = \dim V$, hence $\dim V'' = \dim V' = \dim V$. So $\Lambda : V \to V''$ is a linear map between two vector spaces of the *same finite dimension*.
>
> By the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]]:
> $$\dim V = \dim \operatorname{null} \Lambda + \dim \operatorname{range} \Lambda = 0 + \dim \operatorname{range} \Lambda = \dim \operatorname{range} \Lambda,$$
> using injectivity ($\operatorname{null} \Lambda = \{0\}$). So $\dim \operatorname{range} \Lambda = \dim V = \dim V''$, hence $\operatorname{range} \Lambda = V''$. Therefore $\Lambda$ is surjective, and being both injective and surjective, it is an isomorphism.

**Step 4: $\Lambda$ is natural.**

For every $T \in \mathcal{L}(V)$, $T'' \circ \Lambda = \Lambda \circ T$ as maps $V \to V''$.

> [!note]- Derivation
> Let $T \in \mathcal{L}(V)$. The double dual map $T'' = (T')'$ is the dual of $T'$, so $T'' \in \mathcal{L}(V'')$. By the definition of the dual:
> $$T''(\Phi) = \Phi \circ T' \quad \text{for } \Phi \in V''.$$
>
> Take $v \in V$ and $\varphi \in V'$. Compute both sides at $v$ and evaluate at $\varphi$:
>
> *Left side*, $T'' \circ \Lambda$:
> $$(T''(\Lambda v))(\varphi) = (\Lambda v \circ T')(\varphi) = (\Lambda v)(T'(\varphi)) = T'(\varphi)(v) = (\varphi \circ T)(v) = \varphi(Tv).$$
> The first equality is the definition of $T''$. The second is composition. The third is the definition of $\Lambda$. The fourth is the definition of $T'$. The fifth is composition.
>
> *Right side*, $\Lambda \circ T$:
> $$(\Lambda(Tv))(\varphi) = \varphi(Tv).$$
> Direct from the definition of $\Lambda$.
>
> Both sides give $\varphi(Tv)$. Since this equality holds for every $\varphi \in V'$, the functionals $T''(\Lambda v)$ and $\Lambda(Tv)$ agree on every element of $V'$, hence are equal in $V''$. Since this equality holds for every $v$, $T'' \circ \Lambda = \Lambda \circ T$.

**Conclusion.** $\Lambda : V \to V''$ is a natural linear injection, which is an isomorphism in finite dimensions. The isomorphism does not require choosing a basis — the definition $(\Lambda v)(\varphi) = \varphi(v)$ uses only the canonical pairing $V \times V' \to \mathbb{F}$. $\blacksquare$

> [!note]- Complete formal solution
> Define $\Lambda : V \to V''$ by $(\Lambda v)(\varphi) = \varphi(v)$.
>
> *Linearity.* For $\varphi \in V'$:
> $$(\Lambda(v + w))(\varphi) = \varphi(v + w) = \varphi(v) + \varphi(w) = (\Lambda v + \Lambda w)(\varphi),$$
> $$(\Lambda(\lambda v))(\varphi) = \varphi(\lambda v) = \lambda \varphi(v) = (\lambda \Lambda v)(\varphi).$$
> Since this holds for all $\varphi$, $\Lambda$ is linear.
>
> *Injectivity.* Suppose $\Lambda v = 0$. Then $\varphi(v) = 0$ for every $\varphi \in V'$. If $v \neq 0$, extend $\{v\}$ to a basis $v = v_1, v_2, \dots, v_n$ of $V$; the first dual-basis functional $\varphi_1$ satisfies $\varphi_1(v) = 1 \neq 0$, contradicting $\varphi(v) = 0$ for all $\varphi$. So $v = 0$.
>
> *Isomorphism in finite dimensions.* $\dim V'' = \dim V' = \dim V$. By rank-nullity, an injective linear map between equidimensional spaces is surjective. Hence $\Lambda$ is an isomorphism.
>
> *Naturality.* For $T \in \mathcal{L}(V)$, $v \in V$, $\varphi \in V'$:
> $$(T''(\Lambda v))(\varphi) = (\Lambda v)(T'(\varphi)) = T'(\varphi)(v) = \varphi(Tv) = (\Lambda(Tv))(\varphi).$$
> So $T'' \circ \Lambda = \Lambda \circ T$. $\blacksquare$

---

## The Natural-vs-Unnatural Contrast

This contrast deserves its own subsection because it is the conceptual payload of the exercise.

**The "unnatural" isomorphism $V \cong V'$.** In finite dimensions, $\dim V = \dim V'$, so there is *some* linear isomorphism $V \to V'$. But constructing one requires picking a basis $v_1, \dots, v_n$ of $V$ and sending $v_k \mapsto \varphi_k$ (the dual basis). The isomorphism depends on the choice of basis: choosing a different basis $w_1, \dots, w_n$ of $V$ gives a different isomorphism. There is no canonical way to choose a particular isomorphism; the choice is *external data*, not intrinsic.

**The "natural" isomorphism $V \cong V''$.** The evaluation map $\Lambda$ uses *no choice*. The recipe $(\Lambda v)(\varphi) = \varphi(v)$ uses only the canonical pairing $V \times V' \to \mathbb{F}$, which exists for any $V$ without further data. So $\Lambda$ is determined by $V$ alone, and the isomorphism $V \cong V''$ holds *canonically* in finite dimensions.

**The technical content of "naturality":** the identity $T'' \circ \Lambda = \Lambda \circ T$ in Step 4 is what mathematicians call **naturality** in the categorical sense. It says that the system of maps $\{\Lambda_V : V \to V''\}_V$ is *compatible* with all linear maps $T$: applying $T$ first and then $\Lambda$ is the same as applying $\Lambda$ first and then $T''$. This compatibility is what makes $\Lambda$ a *natural transformation* (from the identity functor to the double-dual functor), and it is the formal definition of "canonical isomorphism".

**Why this matters beyond linear algebra:** the natural-vs-unnatural distinction is the gateway to category theory. *Theorems are often natural; constructions are often not.* Naturality is the technical condition that makes a construction "independent of choices", and it is what survives change of basis, change of coordinates, change of representation. In differential geometry, *natural* tensors transform predictably under coordinate change; *unnatural* objects (like a chosen basis) do not. In representation theory, *natural* maps respect group actions. In algebraic topology, the *naturality* of homology under continuous maps is what makes it a functor. The present exercise is the basic case of all of these.

---

# Key Takeaways

**The double dual is canonically isomorphic to the original; the dual is not.** This is the cleanest example of *naturality* in linear algebra and the gateway to categorical thinking. The recipe $\Lambda v = \operatorname{ev}_v$ (the evaluation map "swap the roles of vector and functional") uses no choice, while any isomorphism $V \to V'$ requires picking a basis. The distinction matters because *theorems* hold for natural isomorphisms — for instance, "every linear map $T$ on $V$ extends to a linear map $T''$ on $V''$ that respects $\Lambda$" — but the analogous statement for the basis-dependent $V \to V'$ fails. When you find yourself building an isomorphism, ask "does this use a choice?" — if yes, it is unnatural; if no, it is natural.

**Naturality is the categorical content of "no choice required"**. The identity $T'' \circ \Lambda = \Lambda \circ T$ is a commutative diagram saying that "$\Lambda$ commutes with every linear map". This is the technical definition of *natural transformation*, and it generalises far beyond linear algebra. In category theory, a natural transformation between two functors is a system of morphisms that commute with all maps. The present exercise gives you the simplest non-trivial example. Once you internalize this pattern, you start recognising it everywhere: every "this construction doesn't depend on choices" statement is a naturality statement, with a precise commutative diagram backing it up.

**The existence of "enough" functionals is the structural foundation of duality**. The injectivity of $\Lambda$ depends crucially on the existence of separating functionals: for every nonzero $v$, there is a $\varphi$ with $\varphi(v) \neq 0$. In finite dimensions this is automatic from the dual basis. In infinite dimensions it is the *Hahn-Banach theorem*, a substantive analytic theorem. So the present exercise is the *easy* case of a deep theorem: "the dual is big enough to separate points". Whenever you see a theorem that "uses the dual non-trivially" in infinite dimensions, Hahn-Banach is usually in the background.

**Use $\Lambda$ to identify $V$ with a subset of $V''$ in proofs.** Once you have $\Lambda : V \to V''$, you can identify vectors $v \in V$ with their images $\Lambda v \in V''$. This is useful in proofs: a statement about "every $v \in V$" can be rephrased as a statement about "every $\Lambda v \in \operatorname{range} \Lambda \subseteq V''$", and dualisation arguments become natural. For instance, the identity $U = \{v : \varphi(v) = 0 \text{ for all } \varphi \in U^0\}$ (Exercise 20 of LADR §3F) becomes more natural with the identification: under $\Lambda$, $U$ corresponds to $(U^0)^0$ in $V''$, which is the annihilator-annihilator identity. The *double dual identification* is the right way to think about "subspaces of $V$ as annihilators in $V''$".

**Cross-link to companion exercises.** This exercise interacts closely with [[Ex - Annihilator of a subspace has complementary dimension]] (the annihilator-annihilator identity $(U^0)^0 = U$ uses the canonical $V \cong V''$). The infinite-dimensional generalisation appears in functional analysis as the **Banach-Alaoglu theorem** and the **reflexive Banach space** condition. The naturality observation in Step 4 is the first non-trivial instance of *natural transformation* that students typically meet.
