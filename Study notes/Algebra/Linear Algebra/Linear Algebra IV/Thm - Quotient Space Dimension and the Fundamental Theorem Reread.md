---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Quotient Space"
  - "Def - Quotient Map of Linear Map"
  - "Thm - Fundamental Theorem of Linear Maps"
  - "Def - Null Space and Range"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $\mathbb{F}$ and $U \leq V$ is a subspace. The [[Def - Quotient Space|quotient space]] is $V/U$ with [[Def - Quotient Map of Linear Map|quotient map]] $\pi : V \to V/U$. For a linear map $T \in \mathcal{L}(V, W)$ the induced map is $\tilde T : V/\operatorname{null} T \to W$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

---

# Statement

> **Theorem (Dimension of a Quotient).** Let $V$ be a finite-dimensional vector space and $U \leq V$ a [[Def - Subspace|subspace]]. Then
> $$\dim(V/U) = \dim V - \dim U.$$

> **Companion ([[Thm - First Isomorphism Theorem|First Isomorphism Theorem]] for [[Def - Vector Space|Vector Spaces]]).** Let $T \in \mathcal{L}(V, W)$. The induced map $\tilde T : V/\operatorname{null} T \to W$ defined by $\tilde T(v + \operatorname{null} T) = Tv$ is a well-defined, injective linear map with $\operatorname{range} \tilde T = \operatorname{range} T$. Hence $\tilde T$ restricts to an isomorphism
> $$V / \operatorname{null} T \;\xrightarrow{\;\cong\;}\; \operatorname{range} T.$$
> Taking [[Def - Dimension|dimensions]] yields $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$, the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]].

The two statements form a structural-and-counting pair. The dimension formula is the consequence; the isomorphism is the structural content.

---

# Motivation

The fundamental theorem of linear maps gives a counting identity:
$$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T.$$
This identity is correct but unsatisfying — it gives equality of numbers without explaining *why*. The "why" turns out to be that the quotient $V/\operatorname{null} T$ is *literally isomorphic* to $\operatorname{range} T$, so the two numbers being equal is the dimension shadow of an underlying isomorphism. The counting identity is thus rederived as a triviality (both sides count the dimension of the *same* vector space) once you accept the isomorphism.

This is one of those structural rereadings that, once seen, makes the original theorem look obvious — and the reread becomes the version you actually carry around for problem-solving. It is much easier to *use* "$V/\operatorname{null} T \cong \operatorname{range} T$" than to use "rank plus nullity equals dimension", because the isomorphism gives you a *map*, not just a number.

The historical context: this theorem is the **first isomorphism theorem for vector spaces**, and it is the linear-algebraic specialisation of [[Thm - First Isomorphism Theorem|the first isomorphism theorem for groups]]. The construction $V/\operatorname{null} T \cong \operatorname{range} T$ for linear maps is identical to $G/\ker\varphi \cong \operatorname{im}\varphi$ for [[Def - Group|group]] [[Def - Homomorphism|homomorphisms]], with [[Def - Subspace|subspaces]] playing the role of normal [[Def - Subgroup|subgroups]] (every subspace is automatically normal in the abelian sense, so there is nothing to check). Once internalised, the theorem can be invoked verbatim from [[Def - Group|group]] theory.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal preconditions are: $V$ finite-dimensional, $U$ a subspace (for the dimension formula); $T$ a linear map (for the isomorphism). The disguised sources are the typical setups that contain a quotient or an induced map.

The first disguised source is **a linear map with non-trivial null space, asking what makes it injective**. Whenever the question "make this map injective" appears, the answer is "quotient by the null space". $T : V \to W$ may fail to be injective because $\operatorname{null} T \neq \{0\}$; the induced $\tilde T : V/\operatorname{null} T \to W$ *is* injective by construction. *Example problem:* given a linear map $T$ that is not injective, find a vector space on which $T$ becomes injective — answer is $V/\operatorname{null} T$.

The second disguised source is **a "values determine equivalence" structure**. If you have an invariant on $V$ that two vectors share exactly when their difference is in a subspace $U$, then the invariant is a function on $V/U$, and is in fact a *linear isomorphism* $V/U \to (\text{values})$ via the first isomorphism theorem. *Example problem:* show that "polynomials of degree $\leq n$ modulo polynomials vanishing at $a$" is isomorphic to $\mathbb{F}$ via $p + U \mapsto p(a)$.

The third disguised source is **a counting problem with a quotient flavor**. Whenever a problem asks for $\dim V$ and the natural setup is "$V$ is built from a subspace and the quotient", the dimension formula $\dim V = \dim U + \dim V/U$ does the work. *Example problem:* if $V = \mathbb{R}^7$ and $U$ is the subspace of vectors summing to zero, what is $\dim V/U$? Answer: $1$, since $U$ has dimension $6$.

**Targets (Output Amplification)**

Combine with **a guess of the answer**. To prove $V/U \cong Q$ for a candidate $Q$, exhibit a surjective $T : V \to Q$ with $\operatorname{null} T = U$. The theorem then converts the surjection-with-correct-null-space into the isomorphism. *Why nonobvious:* it lets you avoid coset arithmetic entirely. *Useful for:* identifying any quotient in any algebraic setting.

Combine with **an explicit complement**. If $W \leq V$ is a complement of $U$ (so $V = U \oplus W$), then $V/U \cong W$ via the natural map $w \mapsto w + U$. This gives a concrete realization of the quotient inside $V$. *Why nonobvious:* it requires choosing $W$, which is not canonical, but once chosen the quotient is "the same" as a subspace. *Useful for:* working with the quotient in coordinates.

Combine with the **annihilator / dual**. For finite-dimensional $V$ and subspace $U$, $\dim U^0 = \dim V/U$ via $(V/U)' \cong U^0$. The first isomorphism theorem applied to the dual of the inclusion $i : U \hookrightarrow V$ gives this — see [[Thm - Null Space and Range of Dual Map]]. This converts dimension formulas across the dual.

---

# Why Is It True

The induced map $\tilde T : V/\operatorname{null} T \to W$ is defined to *forget exactly what $T$ already forgets*. Two vectors $v, v'$ map to the same image under $T$ if and only if $T(v - v') = 0$, i.e. if and only if $v - v' \in \operatorname{null} T$, i.e. if and only if $v$ and $v'$ define the same coset of $\operatorname{null} T$. So:

> Two [[Def - Coset|cosets]] $v + \operatorname{null} T$ and $v' + \operatorname{null} T$ have the same image under $\tilde T$ if and only if they are equal — *which is the definition of injectivity*.

This single observation is the whole theorem. The [[Def - Coset|cosets]] of $\operatorname{null} T$ are *literally the fibres* of $T$ — the sets of vectors sharing a common image. The null space measures the redundancy in $T$, and quotienting by the null space is exactly removing that redundancy. The resulting map $\tilde T$ is forced to be injective because we have collapsed exactly the things $T$ was collapsing.

> **The whole intuition in one sentence: a linear map's fibres are cosets of its null space, so quotienting by the null space identifies the fibres with their common image — and that is the isomorphism.**

The dimension formula then follows by applying the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] to the quotient map $\pi : V \to V/U$ (whose null space is $U$ and range is $V/U$):
$$\dim V = \dim \operatorname{null} \pi + \dim \operatorname{range} \pi = \dim U + \dim V/U.$$
Solving for $\dim V/U$ gives the dimension formula. So the dimension formula is the rank-nullity theorem applied to the quotient map — a one-line proof that the quotient has the right size.

---

# What Makes This Hard

The dimension formula itself is mechanical once the quotient map is in hand. The trap is the **well-definedness** of the induced map $\tilde T$: the rule $\tilde T(v + \operatorname{null} T) := Tv$ uses a representative $v$, and one must check $Tv$ is independent of the choice. The check is: if $v + \operatorname{null} T = v' + \operatorname{null} T$, then $v - v' \in \operatorname{null} T$, so $T(v - v') = 0$, so $Tv = Tv'$. Beginners often skip this check or confuse it with injectivity (which uses the *same* equation, read in the opposite direction). The other slip is forgetting to restrict the codomain to $\operatorname{range} T$ — the induced $\tilde T : V/\operatorname{null} T \to W$ is *injective but not surjective onto $W$*, only onto its range.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Apply the fundamental theorem of linear maps to the quotient map $\pi : V \to V/U$ for the dimension formula. For the companion isomorphism, define $\tilde T$ on cosets, check well-definedness, then check linearity, injectivity, and the range identification.

**Subgoal decomposition:**

1. **Dimension formula.** Apply rank-nullity to $\pi : V \to V/U$.
   - *Hint:* $\operatorname{null} \pi = U$ and $\operatorname{range} \pi = V/U$ (the quotient map is surjective).
   - *Why needed:* This is the dimension formula directly.

2. **Define $\tilde T$ on cosets.** Set $\tilde T(v + \operatorname{null} T) := Tv$.
   - *Hint:* This is the only definition consistent with $\tilde T \circ \pi = T$.
   - *Why needed:* The induced map exists by definition.

3. **Well-definedness.** Check $Tv$ is independent of the representative $v$.
   - *Hint:* $v + \operatorname{null} T = v' + \operatorname{null} T \iff v - v' \in \operatorname{null} T \iff T(v - v') = 0 \iff Tv = Tv'$.
   - *Why needed:* Until this is checked, $\tilde T$ is not a function.

4. **Linearity of $\tilde T$.** Use the quotient operations slot by slot.
   - *Hint:* $\tilde T((v + N) + (v' + N)) = \tilde T((v + v') + N) = T(v + v') = Tv + Tv' = \tilde T(v + N) + \tilde T(v' + N)$, writing $N = \operatorname{null} T$.
   - *Why needed:* An isomorphism must be linear.

5. **Injectivity of $\tilde T$.** Reuse the well-definedness equation in the reverse direction.
   - *Hint:* $\tilde T(v + N) = 0 \iff Tv = 0 \iff v \in N \iff v + N = 0 + N$.
   - *Why needed:* An isomorphism must be injective.

6. **Range identification.** $\operatorname{range} \tilde T = \operatorname{range} T$ by definition.
   - *Hint:* Every element of $\operatorname{range} T$ is $Tv = \tilde T(v + N)$, and every element of $\operatorname{range} \tilde T$ is $\tilde T(v + N) = Tv \in \operatorname{range} T$.
   - *Why needed:* The isomorphism's target is $\operatorname{range} T$, not the larger $W$.

7. **Recover the dimension equation.** Take [[Def - Dimension|dimensions]] of both sides of $V/\operatorname{null} T \cong \operatorname{range} T$, and substitute the dimension formula.
   - *Hint:* $\dim V - \dim \operatorname{null} T = \dim(V/\operatorname{null} T) = \dim \operatorname{range} T$, hence $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$.
   - *Why needed:* This is the rank-nullity theorem reread.

---

# Lemma Decomposition

> [!note]- Lemma 1: The quotient map is linear, surjective, with null space $U$
> **Statement:** Let $V$ be a vector space and $U \leq V$ a subspace. The quotient map $\pi : V \to V/U$, $\pi(v) = v + U$, is linear, surjective, with $\operatorname{null} \pi = U$.
>
> **Hint:** Linearity of $\pi$ uses the definitions of the operations on $V/U$. Surjectivity is tautological: every $v + U \in V/U$ is $\pi(v)$. The null space computation uses $v + U = 0 + U \iff v \in U$, which is the partition lemma.
>
> **Why needed:** This is the input for the dimension formula via rank-nullity, and the structural property "every subspace is a null space".
>
> > [!note]- Full proof
> > **Linearity:** $\pi(v + w) = (v + w) + U = (v + U) + (w + U) = \pi(v) + \pi(w)$, using the definition of addition on $V/U$. Similarly $\pi(\lambda v) = (\lambda v) + U = \lambda(v + U) = \lambda \pi(v)$.
> >
> > **Surjectivity:** every element of $V/U$ has the form $v + U$ for some $v \in V$, and $v + U = \pi(v)$.
> >
> > **Null space:** $\pi(v) = 0_{V/U} \iff v + U = 0 + U \iff v - 0 \in U \iff v \in U$, using the [[Def - Affine Subset#Lemma: Two Translates of a Subspace are Equal or Disjoint|partition lemma]]. Hence $\operatorname{null} \pi = U$.

> [!note]- Lemma 2: The induced map is well-defined and linear
> **Statement:** For $T \in \mathcal{L}(V, W)$, the rule $\tilde T(v + \operatorname{null} T) := Tv$ defines a linear map $\tilde T : V/\operatorname{null} T \to W$.
>
> **Hint:** Well-definedness uses the partition property of cosets. Linearity uses the definitions of operations on the quotient.
>
> **Why needed:** $\tilde T$ is the candidate isomorphism — well-definedness must be checked, and linearity is needed for $\tilde T$ to be an isomorphism (not just a bijection).
>
> > [!note]- Full proof
> > **Well-definedness:** suppose $v + \operatorname{null} T = v' + \operatorname{null} T$. Then $v - v' \in \operatorname{null} T$, so $T(v - v') = 0$, hence $Tv = Tv'$. The value $\tilde T(v + \operatorname{null} T) = Tv$ is independent of the representative.
> >
> > **Linearity:** with $N = \operatorname{null} T$,
> > $$\tilde T((v + N) + (v' + N)) = \tilde T((v + v') + N) = T(v + v') = Tv + Tv' = \tilde T(v + N) + \tilde T(v' + N),$$
> > $$\tilde T(\lambda(v + N)) = \tilde T((\lambda v) + N) = T(\lambda v) = \lambda Tv = \lambda \tilde T(v + N).$$

> [!note]- Lemma 3: The induced map is injective
> **Statement:** For $T \in \mathcal{L}(V, W)$, the induced map $\tilde T : V/\operatorname{null} T \to W$ is injective.
>
> **Hint:** $\tilde T(v + N) = 0$ in $W$ iff $Tv = 0$ iff $v \in N$ iff $v + N = 0 + N$. Trivial null space implies injectivity.
>
> **Why needed:** Injectivity is half of being an isomorphism (the other half is surjectivity onto the right codomain, automatic for $\tilde T$ landing in $\operatorname{range} T$).
>
> > [!note]- Full proof
> > Let $N = \operatorname{null} T$. Suppose $\tilde T(v + N) = 0$ in $W$. By definition $\tilde T(v + N) = Tv$, so $Tv = 0$. Hence $v \in N = \operatorname{null} T$. By the partition property, $v + N = 0 + N$, the zero of $V/N$. So $\operatorname{null} \tilde T = \{0 + N\}$, and $\tilde T$ is injective.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — the quotient exists.** $U$ is a subspace of $V$, so the quotient space $V/U$ is defined ([[Def - Quotient Space]]). Similarly, $\operatorname{null} T$ is a subspace of $V$ (it is the null space of a linear map), so $V/\operatorname{null} T$ exists.
>
> **Step 1 — dimension formula.** By Lemma 1, the quotient map $\pi : V \to V/U$ is linear, surjective, with $\operatorname{null} \pi = U$ and $\operatorname{range} \pi = V/U$. By the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]],
> $$\dim V = \dim \operatorname{null} \pi + \dim \operatorname{range} \pi = \dim U + \dim(V/U).$$
> Solving, $\dim(V/U) = \dim V - \dim U$.
>
> **Step 2 — first isomorphism theorem.** Let $T \in \mathcal{L}(V, W)$ and $N = \operatorname{null} T$. Define $\tilde T : V/N \to W$ by $\tilde T(v + N) := Tv$. By Lemma 2, $\tilde T$ is well-defined and linear; by Lemma 3, it is injective.
>
> **Step 3 — range identification.** By definition, $\operatorname{range} \tilde T = \{Tv : v \in V\} = \operatorname{range} T$. So restricting the codomain of $\tilde T$ to $\operatorname{range} T$ produces a linear map $V/N \to \operatorname{range} T$ that is injective and surjective — an isomorphism.
>
> **Step 4 — conclude.** Hence
> $$V / \operatorname{null} T \;\xrightarrow{\;\cong\;}\; \operatorname{range} T,$$
> and taking dimensions,
> $$\dim V - \dim \operatorname{null} T = \dim(V/\operatorname{null} T) = \dim \operatorname{range} T,$$
> equivalent to the original [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]] statement $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Codimension of a hyperplane.** A *hyperplane* in $V$ is a subspace of codimension $1$, i.e. with $\dim V/H = 1$. Equivalently, by the first isomorphism theorem applied to a non-zero functional $\varphi$ with $\operatorname{null} \varphi = H$, the quotient $V/H \cong \mathbb{F}$. So *every* hyperplane is the null space of a non-zero functional, and the quotient is one-dimensional. This is a foundational result for the [[Def - Dual Space|dual space]] machinery in §3F.

**Modular arithmetic from quotients.** Take $V = \mathbb{Z}$ (an abelian group, not strictly a vector space, but the same construction works) and $U = n\mathbb{Z}$. Then $V/U = \mathbb{Z}/n\mathbb{Z}$ is finite, has $n$ elements, and the *order* of $V/U$ is $\dim V / \dim U$ in some sense — but for the additive group, the "size" is the index. Modular arithmetic *is* the first isomorphism theorem applied to "reduction mod $n$": $\mathbb{Z}/n\mathbb{Z} \cong$ image of reduction. This is the group-theoretic analogue of the present linear-algebraic theorem.

**Quotients of function spaces.** Let $V = C([0,1])$ (continuous functions on $[0,1]$) and $U = \{f \in V : f(0) = 0\}$, the functions vanishing at $0$. The quotient $V/U$ identifies any two functions that agree at $0$, and is canonically isomorphic to $\mathbb{R}$ via $f + U \mapsto f(0)$. The same construction produces "boundary values" of distributions in the theory of PDE: the quotient space *is* the space of boundary values.

---

# Bridges

- **[[Thm - Fundamental Theorem of Linear Maps]]** — exact reread. The fundamental theorem says $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$; the present theorem rederives this from the isomorphism $V/\operatorname{null} T \cong \operatorname{range} T$ via the dimension formula applied to the quotient map. The two theorems are *the same theorem* in different registers — one numerical, one structural.

- **[[Thm - First Isomorphism Theorem]]** — exact specialisation. The first isomorphism theorem for groups states $G/\ker\varphi \cong \operatorname{im}\varphi$; specialising to vector spaces (which are abelian groups with extra structure) gives $V/\operatorname{null} T \cong \operatorname{range} T$. The proofs are identical except for the extra check that the scalar action is well-defined (which is automatic by linearity of $T$). So the present theorem is the group theorem with a linear-algebra adjective.

- **[[Thm - Dimension of a Sum of Subspaces]]** — companion in counting. The sum-of-subspaces formula $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$ can also be derived from the present theorem by writing $U + W$ as the image of $U \times W$ under the sum map, with null space $\{(u, -u) : u \in U \cap W\} \cong U \cap W$.

- **[[Thm - First Isomorphism Theorem|Isomorphism theorems for modules]]** — generalisation. The same statement holds for modules over a ring, with submodules in place of subspaces and module homomorphisms in place of linear maps. The proof is identical. See [[Def - Submodule]] and [[Def - Quotient Module]].

---

# Unlocked by This

> [!tip] Splitting of Short Exact Sequences *(from Linear Algebra)*
> Every short exact sequence of vector spaces $0 \to U \to V \to V/U \to 0$ *splits*: there is a subspace $W \leq V$ with $V = U \oplus W$ and $W \cong V/U$. This is *not* a feature of general modules — it relies on vector spaces having complements for every subspace, which uses the existence of a basis (i.e. the axiom of choice for general infinite dimensions). The dimension formula is the counting shadow.

> [!tip] Snake Lemma and Long Exact Sequences *(from Homological Algebra)*
> The first isomorphism theorem for vector spaces is the base case of the much larger structure of *exact sequences*. Given a chain complex with linear maps, the homology vector spaces $H_n = \operatorname{null} d_n / \operatorname{range} d_{n+1}$ measure the failure of exactness. The snake lemma assembles homology groups across short exact sequences into long exact sequences, and these are the foundation of homological algebra. The construction at every step uses quotient-by-image, which is the operation introduced here.
