---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $F$ (almost always $\mathbb{R}$ or $\mathbb{C}$), and $T \in \mathcal{L}(V)$ is an operator on $V$ — a linear map $V \to V$. The notation $U \leq V$ means $U$ is a subspace of $V$. The image of $U$ under $T$ is $T(U) = \{Tv : v \in U\}$. The restriction of $T$ to an invariant subspace $U$ is $T|_U : U \to U$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Axiom Motivation

An operator $T$ on a vector space $V$ is potentially very complicated. The strategy of the entire chapter — and indeed of every chapter on operators that follows — is to **break $V$ apart** into pieces that $T$ respects, and to study $T$ separately on each piece. The pieces are the **invariant subspaces** of $T$, and the central question of §5 is: what invariant subspaces does $T$ have?

What is the right axiomatic content? We want a subspace $U \leq V$ such that "the restriction of $T$ to $U$" is a well-defined operator on $U$. For the restriction to land in $U$, we need $Tv \in U$ for every $v \in U$. That is the single requirement. So a $T$-invariant subspace is a subspace $U$ closed under the action of $T$ — exactly the same condition as "closed under multiplication by a scalar" for a subspace of a vector space, with the operator $T$ playing the role of a scalar.

The condition is *necessary* because otherwise $T|_U$ has no codomain to land in; it is *sufficient* because closure under $T$ makes $T|_U$ a linear map $U \to U$, which by definition is an operator on $U$. The minimality of the requirement is the point: nothing more is asked of $U$ than this single closure property, and the rest of the structure (subspace structure, linearity of $T$) is inherited.

Two trivial invariant subspaces always exist: the zero subspace $\{0\}$, and $V$ itself. The interesting question is whether *non-trivial* invariant subspaces exist, where non-trivial means "neither $\{0\}$ nor $V$". This is the central question of operator theory.

Three classes of invariant subspace arise mechanically from $T$ itself, and they should be in the reader's reflexes:

1. **The null space $\ker T = \{v : Tv = 0\}$.** It is invariant because if $v \in \ker T$ then $Tv = 0 \in \ker T$.
2. **The range $\operatorname{im} T = \{Tv : v \in V\}$.** It is invariant because $T(Tv) = Tv'$ for $v' = Tv \in \operatorname{im} T$.
3. **For any polynomial $p \in F[x]$, the null space $\ker p(T)$ and range $\operatorname{im} p(T)$ of $p(T)$.** Because $T$ and $p(T)$ commute (as a power of $T$ commutes with $T$, and linear combinations of commuting operators commute), $T$ leaves both invariant.

These constructions are the source of most invariant subspaces one encounters. The third one in particular — invariant subspaces from kernels and ranges of polynomials in $T$ — is the foundation of the existence-of-eigenvalues argument: factor an annihilating polynomial of $T$, look at the kernels of the factors, find one that is non-trivial.

The *simplest* possible non-trivial invariant subspace is **one-dimensional**: a line through the origin invariant under $T$. On such a line, $T$ must act as a scalar — there is nowhere else for it to map a vector. That scalar is an [[Def - Eigenvalue and Eigenvector|eigenvalue]] and the vector spans an eigenvector. Whether such a line exists at all is the question answered by [[Thm - Existence of Eigenvalues on Complex Vector Spaces|the existence-of-eigenvalues theorem]], and the answer is "yes over $\mathbb{C}$, not always over $\mathbb{R}$".

Why does the axiom have only one half — closure under $T$ — and not also "closure under $T^{-1}$" (when $T$ is invertible)? Because requiring both would be a much stronger condition: it would say $U$ is invariant under both $T$ and $T^{-1}$, hence under all powers $T^k$ for $k \in \mathbb{Z}$. This is the condition for **$T$-stability**, and it is more rigid than mere invariance. The looser, one-sided condition is the right one because it makes "find an invariant subspace and induct" a useful strategy: it imposes the minimum needed for the induction step to go through.

A final point about the philosophy. The existence question "does $T$ have a non-trivial invariant subspace?" has a famous infinite-dimensional analogue: the **invariant subspace problem** for bounded operators on a Hilbert space. The question whether every such operator has a non-trivial closed invariant subspace has been open for decades for separable Hilbert spaces; counterexamples are known for general Banach spaces. So even the most basic question of operator theory becomes hard in infinite dimensions, and the finite-dimensional answer — "yes, over $\mathbb{C}$, by the existence of eigenvalues" — is to be appreciated.

---

# The Definition

Let $V$ be a vector space over a field $F$ and let $T \in \mathcal{L}(V)$. A subspace $U \leq V$ is **invariant under $T$** (or simply **$T$-invariant**) if $T(U) \subseteq U$, that is,
$$v \in U \;\implies\; Tv \in U.$$

When $U$ is invariant under $T$, the **restriction** $T|_U : U \to U$, defined by $T|_U(v) = Tv$ for $v \in U$, is a well-defined operator on $U$.

The **trivial invariant subspaces** are $\{0\}$ and $V$ itself; both are always invariant. A non-trivial invariant subspace is one different from both.

---

# Categorical / Structural Definition

A $T$-invariant subspace is a **subobject** in the category whose objects are pairs $(V, T)$ — a vector space together with a chosen operator — and whose morphisms $\phi : (V, T) \to (W, S)$ are linear maps $\phi : V \to W$ satisfying $\phi \circ T = S \circ \phi$ (the "intertwining" condition). In this category, a subobject of $(V, T)$ is a pair $(U, T|_U)$ where $U \leq V$ is a subspace satisfying $T(U) \subseteq U$, with the morphism being the inclusion.

This is the same as saying: a $T$-invariant subspace is a **submodule** of $V$ viewed as an $F[x]$-module with $x$ acting as $T$. The dictionary
$$(V, T) \;\longleftrightarrow\; F[x]\text{-module structure on } V$$
sends $T$-invariant subspaces to $F[x]$-submodules. This is the bridge to [[Def - The Module of a Linear Operator]] and to the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] for $F[x]$-modules: the indecomposable submodules of $V$ are exactly the cyclic submodules $F[x]/(p)$ for $p$ an irreducible power, and these correspond geometrically to the [[Thm - Jordan Normal Form|Jordan blocks]] of $T$.

The quotient construction also works: when $U \leq V$ is $T$-invariant, $T$ descends to an operator $T/U \in \mathcal{L}(V/U)$ on the quotient space, defined by $(T/U)(v + U) = Tv + U$. This is the quotient $F[x]$-module $V/U$, and the construction commutes with restriction in the natural sense. Together, restriction and quotient are the two ways to make an invariant subspace into a strategic ingredient: study $T$ on $U$ and $T/U$ on $V/U$ separately.

---

# Relate to Other Fields / Compression

**True name.** A $T$-invariant subspace is a "$T$-stable region of $V$" — a piece you can isolate and study on its own because $T$ never carries vectors out of it. Operationally, an invariant subspace is **a chunk on which the operator is well-defined as a self-map**, equivalently the data $V = U \oplus W$ (when a complementary invariant subspace exists) decomposes $T$ into a block-diagonal form $T = T|_U \oplus T|_W$. This block-diagonal decomposition is what makes invariant subspaces a strategic ingredient: they let you compute on smaller pieces.

In **dynamical systems**, a $T$-invariant subspace is exactly a $T$-stable region of the phase space — once a trajectory enters $U$, it stays in $U$ forever. This is the precise meaning of "invariant" in the dynamical sense. Eigenvalues of $T|_U$ govern the local behaviour on $U$; the absence of non-trivial invariant subspaces (irreducibility) means the system mixes between all parts of $V$.

In **representation theory**, a $G$-invariant subspace of a representation $\rho : G \to \mathrm{GL}(V)$ is a subspace $U \leq V$ with $\rho(g)(U) \subseteq U$ for all $g \in G$ — invariance under the whole group action, not just a single operator. The same general structure theory applies: a representation is **irreducible** if its only invariant subspaces are $\{0\}$ and $V$, and complete reducibility (Maschke's theorem for finite groups in characteristic zero) decomposes any representation as a direct sum of irreducibles. The single-operator case in §5 is the simplest instance: $G = \mathbb{Z}$ acting by powers of $T$.

In **commutative algebra and algebraic geometry**, an invariant subspace is a **submodule**. The duality between geometric subobjects (subvarieties) and algebraic subobjects (ideals or modules) is the bridge: in our setting, invariant subspaces are "infinitesimal subvarieties" of the projective space $\mathbb{P}(V)$ stable under the dynamical system given by $T$.

---

# Examples / Corollaries

**Always-invariant: $\ker T$ and $\operatorname{im} T$.** For any $T \in \mathcal{L}(V)$, both $\ker T = \{v : Tv = 0\}$ and $\operatorname{im} T = \{Tv : v \in V\}$ are $T$-invariant. The null space is invariant because if $Tv = 0$, then $T(Tv) = T(0) = 0$, so $Tv \in \ker T$. The range is invariant because $T(Tv) = T(v')$ for $v' = Tv \in \operatorname{im} T$, so $T(\operatorname{im} T) \subseteq \operatorname{im} T$.

**Always-invariant: kernels and ranges of polynomials in $T$.** For any polynomial $p \in F[x]$, both $\ker p(T)$ and $\operatorname{im} p(T)$ are $T$-invariant. The argument is that $T$ and $p(T)$ commute (since polynomials in the same operator commute), so if $p(T)v = 0$, then $p(T)(Tv) = T(p(T)v) = T(0) = 0$, hence $Tv \in \ker p(T)$. This is the source of essentially every interesting invariant subspace one constructs in this chapter: by choosing the polynomial $p$ to exploit some property of $T$ (such as a factor of the [[Def - Minimal Polynomial|minimal polynomial]]), one isolates structurally meaningful pieces of $V$.

**One-dimensional invariant subspace = eigenvector.** If $U = \operatorname{span}(v)$ with $v \neq 0$ is one-dimensional and invariant under $T$, then $Tv$ must be a scalar multiple of $v$: $Tv = \lambda v$ for some $\lambda \in F$. So $\lambda$ is an [[Def - Eigenvalue and Eigenvector|eigenvalue]] and $v$ is an eigenvector. Conversely, any eigenvector $v$ spans a one-dimensional $T$-invariant subspace. The notions are equivalent.

**A specific example: rotation by $90°$ on $\mathbb{R}^2$.** Let $T \in \mathcal{L}(\mathbb{R}^2)$ be defined by $T(x, y) = (-y, x)$ — a $90°$ counterclockwise rotation. The only invariant subspaces are $\{0\}$ and $\mathbb{R}^2$ itself: there is no one-dimensional invariant subspace (any line gets rotated to a perpendicular line), so $T$ has no eigenvalues over $\mathbb{R}$. This is the standard example showing the importance of the field hypothesis: complexifying $T$ to act on $\mathbb{C}^2$ introduces eigenvalues $\pm i$ and corresponding one-dimensional complex invariant subspaces.

**Non-example: a subspace closed under $T$ and not under $T^{-1}$.** Let $T$ be the right-shift on the space of polynomials: $T(p(x)) = xp(x)$. The subspace $U = x \cdot F[x]$ (polynomials with no constant term) is $T$-invariant since multiplying by $x$ never restores a constant term, but is *not* invariant under $T^{-1}$ (if $T$ is interpreted on a domain where $T^{-1}$ makes sense, like extending to formal Laurent series). This illustrates the **one-sided** nature of the invariance condition — it does not automatically give bilateral closure.

**Non-example: an "almost invariant" subspace that fails the condition.** In $\mathbb{R}^2$ with $T(x, y) = (y, 0)$, the subspace $U = \operatorname{span}((1, 0))$ is mapped to $0 \in U$ — so it satisfies $T(U) \subseteq U$ — but its "complement" $W = \operatorname{span}((0, 1))$ is mapped to $\operatorname{span}((1, 0)) = U$, which is *not* contained in $W$. So $W$ is *not* $T$-invariant, even though it is $T$'s image. The lesson: invariance is a property of the subspace under the specific operator, not a default feature of complementary subspaces.

**Corollary: the sum of invariant subspaces is invariant.** If $U_1, U_2 \leq V$ are both $T$-invariant, so is $U_1 + U_2 = \{u_1 + u_2 : u_1 \in U_1, u_2 \in U_2\}$. (For $v = u_1 + u_2$, we have $Tv = Tu_1 + Tu_2 \in U_1 + U_2$.) Likewise, $U_1 \cap U_2$ is $T$-invariant: if $v \in U_1 \cap U_2$, then $Tv \in U_1$ (since $v \in U_1$) and $Tv \in U_2$ (since $v \in U_2$). So the set of $T$-invariant subspaces is closed under arbitrary sums and intersections — it forms a **complete sublattice** of the subspace lattice of $V$.

**Calibration check.** If you have understood the definition: (a) you can quickly verify that $\ker T^k$ is invariant for every $k \geq 0$ (by induction on $k$, using $T(T^k v) = T^k(Tv)$); (b) you recognise that on the operator $T(x, y, z) = (y, z, 0)$ on $F^3$, the subspaces $\operatorname{span}(e_1)$ and $\operatorname{span}(e_1, e_2)$ are invariant (yielding an upper-triangular matrix in this basis), while $\operatorname{span}(e_2)$ alone is not (since $Te_2 = e_1 \notin \operatorname{span}(e_2)$); (c) you can identify the eigenvalues of an operator with the scalars $\lambda$ such that $\ker(T - \lambda I)$ is non-trivial — i.e. the scalars for which the kernel is itself a non-trivial invariant subspace.

---

# Unlocked by This

> [!tip] Eigenvalue and Eigenvector *(from Linear Algebra V, §5A)*
> The simplest non-trivial invariant subspaces are one-dimensional, and these are exactly the spans of eigenvectors. See [[Def - Eigenvalue and Eigenvector]]. The whole theory of eigenvalues is the study of one-dimensional invariant subspaces.

> [!tip] The Generalized Eigenspace Decomposition *(from Linear Algebra VIII)*
> The deeper analogue of "one-dimensional invariant subspace" is a **generalized eigenspace**: $G(\lambda, T) = \ker(T - \lambda I)^{\dim V}$. These are the largest $T$-invariant subspaces on which $T$ acts as $\lambda I$ plus a nilpotent. The [[Thm - Generalized Eigenspace Decomposition]] says $V$ decomposes as a direct sum of generalized eigenspaces — the deepest direct-sum decomposition an operator admits over $\mathbb{C}$.

> [!tip] Irreducibility in Representation Theory *(from Representation Theory)*
> A representation of a group $G$ on $V$ is **irreducible** if its only $G$-invariant subspaces are $\{0\}$ and $V$. The single-operator case in §5 is the special case $G = \mathbb{Z}$ acting by $T$; irreducibility there is rare (it requires $T$ to be a scalar multiple of $I$ when $F = \mathbb{C}$). Schur's lemma — the centrepiece of representation theory — describes the intertwining maps between irreducible representations, and its proof rests on the fact that the kernel and image of any intertwiner are invariant.
