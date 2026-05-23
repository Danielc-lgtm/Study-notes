---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - The Tangent Space"
tags: [geometry, differential-geometry, lie-groups]
---

# Problem Statement

Show that the Lie algebra of $\mathrm{GL}(n, \mathbb{R})$ is the space $\mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$ of all $n \times n$ real matrices, identified as the tangent space to $\mathrm{GL}(n, \mathbb{R})$ at the identity. (The bracket on $\mathfrak{gl}(n, \mathbb{R})$ as the matrix commutator is established in [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]].)

**Recall:**

A [[Def - Lie Group|Lie group]] is a smooth manifold with smooth multiplication and inversion. The **Lie algebra** of a Lie [[Def - Group|group]] $G$ is the tangent space $T_e G$ with bracket inherited from left-invariant vector fields (see [[Def - The Lie Algebra of a Lie Group]]). The **general linear group** $\mathrm{GL}(n, \mathbb{R})$ is the set of invertible $n \times n$ real matrices under matrix multiplication, an open subset of $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$.

---

# Convergent Strategy

**Problem class:** This is a Lie algebra computation for a matrix Lie group — the prototype of a basic computation in this chapter. The Lie algebra is by definition the tangent space at the identity, so the computation reduces to identifying the tangent space concretely.

**Assumption pattern:** $\mathrm{GL}(n, \mathbb{R})$ is an **open subset** of the vector space $M(n, \mathbb{R})$. Open subsets of vector spaces have a canonical identification of tangent spaces with the ambient vector space at every point. This is the key structural fact that makes the calculation trivial.

**Theorem routing:** The route uses one fact: for any open subset $U$ of a finite-dimensional vector space $V$, and any $p \in U$, $T_p U \cong V$ canonically (Lee Lemma 3.7 / standard tangent-space identification for vector spaces). Applied to $U = \mathrm{GL}(n, \mathbb{R})$, $V = M(n, \mathbb{R})$, $p = I$: $T_I \mathrm{GL}(n, \mathbb{R}) = M(n, \mathbb{R})$. Then by definition $\mathfrak{gl}(n, \mathbb{R}) = T_I \mathrm{GL}(n, \mathbb{R}) = M(n, \mathbb{R})$.

**Key decision point:** The non-obvious move is recognizing that $\mathrm{GL}(n, \mathbb{R})$ is an *open* submanifold of $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$ (not a closed submanifold or a level set), so its tangent spaces are identified with all of $M(n, \mathbb{R})$ — there is no constraint to differentiate. This is what makes the Lie algebra "all of $M(n, \mathbb{R})$" rather than a proper [[Def - Subspace|subspace]].

---

# Legal Operations Used

1. **Compute the Lie algebra as the tangent space at the identity (operation 1 from the topic page).** Here applied trivially: since $\mathrm{GL}(n)$ is an open submanifold of $M(n)$, the tangent space at $I$ is the entire ambient vector space. No defining equation needs to be differentiated; the constraint is empty.

---

# Hints

> [!note]- Hint 1
> What is the manifold structure of $\mathrm{GL}(n, \mathbb{R})$? Is it a submanifold defined by some equation, or is it something simpler?

> [!note]- Hint 2
> $\mathrm{GL}(n, \mathbb{R}) = \{A \in M(n, \mathbb{R}) : \det A \neq 0\}$. The determinant is continuous, so its preimage of $\mathbb{R} \setminus \{0\}$ is **open**. So $\mathrm{GL}(n, \mathbb{R})$ is an open subset of $M(n, \mathbb{R})$.

> [!note]- Hint 3
> For any open subset $U$ of a finite-dimensional vector space $V$, the tangent space at any point $p \in U$ is canonically $V$ itself — there is no "constraint" to differentiate.

---

# Solution

The result follows from one structural fact about open submanifolds of vector spaces, applied to the identity element of $\mathrm{GL}(n, \mathbb{R})$.

**Step 1: $\mathrm{GL}(n, \mathbb{R})$ is an open submanifold of $M(n, \mathbb{R})$.**

The determinant map $\det : M(n, \mathbb{R}) \to \mathbb{R}$ is continuous (in fact polynomial in the matrix entries). The preimage of the open set $\mathbb{R} \setminus \{0\}$ is therefore open in $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$. So $\mathrm{GL}(n, \mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$ is open.

> [!note]- Derivation
> The map $A \mapsto \det A$ is a sum of products of matrix entries, hence a polynomial $M(n, \mathbb{R}) \to \mathbb{R}$. Polynomials are smooth, hence continuous. The set $\mathbb{R} \setminus \{0\}$ is open in $\mathbb{R}$. So $\mathrm{GL}(n, \mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$ is open in $M(n, \mathbb{R})$. As an open subset of an $n^2$-dimensional real vector space, $\mathrm{GL}(n, \mathbb{R})$ is a smooth manifold of [[Def - Dimension|dimension]] $n^2$, with a single chart $\mathrm{id} : \mathrm{GL}(n, \mathbb{R}) \to \mathrm{GL}(n, \mathbb{R}) \subset M(n, \mathbb{R}) = \mathbb{R}^{n^2}$ (or any restriction thereof).

**Step 2: The tangent space at $I$ is all of $M(n, \mathbb{R})$.**

For any open subset $U$ of a finite-dimensional vector space $V$ and any point $p \in U$, the tangent space $T_p U$ is canonically identified with $V$ — via, for instance, the identification of a tangent vector with the velocity of a curve in $U$, where the velocity of $\gamma(t) = p + tv$ at $t = 0$ is $v \in V$.

> [!note]- Derivation
> For an open subset $U$ of $V$ and $p \in U$, a tangent vector at $p$ is an equivalence class of curves $\gamma : (-\epsilon, \epsilon) \to U$ with $\gamma(0) = p$, modulo first-order tangency. Such a curve has a velocity $\gamma'(0) \in V$ (since $\gamma$ takes values in $V$ and $V$ is a vector space). The assignment $[\gamma] \mapsto \gamma'(0)$ is a linear bijection $T_p U \to V$. Applied to $U = \mathrm{GL}(n, \mathbb{R})$, $V = M(n, \mathbb{R})$, $p = I$: $T_I \mathrm{GL}(n, \mathbb{R}) \cong M(n, \mathbb{R})$.

**Step 3: $\mathfrak{gl}(n, \mathbb{R}) = T_I \mathrm{GL}(n, \mathbb{R}) = M(n, \mathbb{R})$.**

By the definition of the Lie algebra of a Lie group, $\mathfrak{g} = T_e G$ as a vector space (with bracket from left-invariant vector fields — addressed separately in [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]). Combining Step 2 with this definition:

$$\mathfrak{gl}(n, \mathbb{R}) = T_I \mathrm{GL}(n, \mathbb{R}) = M(n, \mathbb{R}).$$

The dimension is $n^2$, agreeing with $\dim \mathrm{GL}(n, \mathbb{R}) = n^2$.

> [!note]- Complete formal solution
> $\mathrm{GL}(n, \mathbb{R})$ is the preimage under the continuous determinant function $\det : M(n, \mathbb{R}) \to \mathbb{R}$ of the open set $\mathbb{R} \setminus \{0\}$, hence is an open subset of $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$. As an open subset of a vector space, $\mathrm{GL}(n, \mathbb{R})$ is a smooth manifold of dimension $n^2$, and the tangent space at any point — in particular at $I$ — is canonically identified with the ambient vector space $M(n, \mathbb{R})$. By the definition of the Lie algebra of a Lie group, $\mathfrak{gl}(n, \mathbb{R}) := \mathrm{Lie}(\mathrm{GL}(n, \mathbb{R})) = T_I \mathrm{GL}(n, \mathbb{R}) = M(n, \mathbb{R})$. (The bracket structure on $M(n, \mathbb{R})$ — the matrix commutator — is established in [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]].)

---

# Key Takeaways

**Open [[Def - Subgroup|subgroups]] of vector spaces have trivial tangent-space computations.**

When a Lie group is realized as an open subset of a vector space — and not as a level set of equations — its Lie algebra is the entire ambient vector space, with no constraints to compute. This is the principle that makes $\mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$ a trivial calculation, distinguished from the more interesting cases like $\mathfrak{o}(n)$, $\mathfrak{sl}(n)$, $\mathfrak{u}(n)$, where the Lie algebra is a *proper* subspace of $\mathfrak{gl}(n)$ defined by differentiating equations at the identity. The trigger: a Lie group given as an open subset (rather than a level set) has Lie algebra equal to the ambient vector space.

**$\mathfrak{gl}(n, \mathbb{R})$ is the "universe" containing all matrix Lie algebras.**

Every matrix Lie group $G \leq \mathrm{GL}(n, \mathbb{R})$ has Lie algebra $\mathfrak{g} \subseteq \mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$, with the bracket inherited from the matrix commutator on $\mathfrak{gl}(n)$. So $\mathfrak{gl}(n)$ is the "biggest" matrix Lie algebra in dimension $n$, and the classical Lie algebras $\mathfrak{o}(n), \mathfrak{sl}(n), \mathfrak{u}(n), \mathfrak{su}(n), \mathfrak{sp}(2n)$ are computed as [[Def - Subspace|subspaces]] of $\mathfrak{gl}(n)$ cut out by linear conditions (antisymmetry, tracelessness, skew-Hermiticity, symplectic compatibility). The universality of $\mathfrak{gl}(n)$ as the ambient algebra is the structural fact that makes the classification of classical matrix Lie [[Def - Group|groups]] tractable.

**[[Def - Dimension|Dimension]] matching.**

$\dim \mathfrak{gl}(n, \mathbb{R}) = n^2 = \dim \mathrm{GL}(n, \mathbb{R})$. This is the general fact $\dim \mathfrak{g} = \dim G$ (Lee Thm 8.37), specialized here. The dimension check serves as a sanity verification: the calculation $\mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$ gives exactly $n^2$ free parameters in the matrix, matching the dimension of $\mathrm{GL}(n, \mathbb{R})$ as an open subset of $\mathbb{R}^{n^2}$.
