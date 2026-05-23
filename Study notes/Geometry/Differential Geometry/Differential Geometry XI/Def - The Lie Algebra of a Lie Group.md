---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Lie Algebra"
  - "Def - Left-Invariant Vector Field"
  - "Def - The Tangent Space"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group with identity $e$. The Lie algebra of $G$ is denoted $\mathfrak{g}$ or $\mathrm{Lie}(G)$. The canonical identification $\mathfrak{g} \cong T_e G$ as vector spaces is used freely; the bracket on $T_e G$ is the one transported from left-invariant vector fields via the evaluation isomorphism $X \mapsto X_e$. For matrix Lie groups, $\mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$ as vector spaces, with the matrix commutator as bracket. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Axiom Motivation

We have two prior notions to combine. From the [[Def - Lie Group|Lie group]] side we have $G$, a smooth manifold with smooth group operations; we want to extract its "infinitesimal structure" at the identity. From the [[Def - Lie Algebra|Lie algebra]] side we have an abstract notion of vector space with a bracket; we want to produce an instance of this structure from $G$.

The natural candidate for the underlying vector space is $T_e G$ — it is finite-dimensional, of dimension $\dim G$, and it is intrinsically attached to $G$ at the identity (the only group-theoretically distinguished point). The question is: what bracket should we put on $T_e G$?

Three answers present themselves; one is correct.

**Answer 1 (wrong, in general):** define the bracket via the commutator in $G$, $[g, h] = ghg^{-1}h^{-1}$, and try to linearize. The issue is that $[g, h] = e$ when $g$ or $h$ is the identity, so the differential of the commutator map at $(e, e)$ is zero — we get no first-order information. The commutator's *second* derivative is what carries the bracket information, and extracting it correctly requires care.

**Answer 2 (correct, indirect):** define the bracket via the [[Thm - Naturality of the Exponential Map|Baker–Campbell–Hausdorff formula]]. For small enough $X, Y \in T_e G$, $\log(\exp X \exp Y) = X + Y + \tfrac{1}{2}[X, Y] + \cdots$, where $\log$ is the local inverse of $\exp$. The $\tfrac{1}{2}[X, Y]$ term, doubled, defines a bracket on $T_e G$. This works but is circular if one tries to use it as a definition (we need to define $\exp$ first), and it is technically delicate.

**Answer 3 (correct, direct, used by Lee):** identify $T_e G$ with the space of left-invariant vector fields on $G$ (via $X \mapsto X^L$, the evaluation-inverse isomorphism). Left-invariant vector fields are closed under the Lie bracket of vector fields ([[Thm - Left-Invariant Vector Fields Form a Lie Algebra|theorem]]), so the bracket of vector fields restricts to a bracket on this finite-dimensional space, which transports to $T_e G$ via the isomorphism. This gives a clean definition of the bracket without needing $\exp$ first; in fact $\exp$ will later be defined in terms of integral curves of left-invariant vector fields, which presupposes the bracket on $\mathfrak{g}$.

The chosen construction routes through left-invariant vector fields not because they are physically intrinsic to the situation but because they bridge two pieces of machinery already in hand: tangent vectors at a point (linear algebra) and Lie brackets of vector fields (manifold theory). The bridge is constructed in [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]].

**Why is this the "right" bracket?** Because it agrees with the matrix commutator on matrix Lie [[Def - Group|groups]] (see [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]), and because it reproduces the BCH leading-order formula for $\exp(X) \exp(Y)$ in terms of $X + Y + \tfrac{1}{2}[X, Y]$. These two checks pin down the bracket uniquely, and the left-invariant-vector-field construction is the one that achieves them.

**The dimension count.** The evaluation map $\mathrm{Lie}(G) \to T_e G$, $X \mapsto X_e$, is a vector space isomorphism (Lee Thm 8.37). The injectivity is the rigidity statement: a left-invariant vector field is determined by its value at $e$. Surjectivity is via the construction $v \mapsto v^L$ where $v^L|_g = d(L_g)_e(v)$. Hence $\dim \mathfrak{g} = \dim T_e G = \dim G$.

---

# The Definition

Let $G$ be a [[Def - Lie Group|Lie group]] with identity $e$. The **Lie algebra of $G$**, denoted $\mathfrak{g}$ or $\mathrm{Lie}(G)$, is defined equivalently in two ways:

1. **As left-invariant vector fields.** $\mathrm{Lie}(G) = \{X \in \mathfrak{X}(G) : X \text{ is left-invariant}\}$, the space of smooth [[Def - Left-Invariant Vector Field|left-invariant vector fields]] on $G$, with the [[Def - The Lie Bracket of Vector Fields|Lie bracket of vector fields]] $[X, Y] f = X(Yf) - Y(Xf)$.

2. **As tangent space at the identity with transported bracket.** $\mathfrak{g} = T_e G$, equipped with the bracket $[X_e, Y_e] := [X^L, Y^L]_e$ where $X^L$ and $Y^L$ are the left-invariant vector fields with values $X_e, Y_e$ at $e$.

These two definitions are equivalent via the **evaluation isomorphism** $\varepsilon : \mathrm{Lie}(G) \to T_e G$, $\varepsilon(X) = X_e$, which is a vector space isomorphism (Lee Thm 8.37) and, by construction, a Lie algebra isomorphism with respect to the transported bracket.

The Lie algebra $\mathfrak{g}$ is a real Lie algebra of dimension $\dim G$. It is finite-dimensional, satisfying bilinearity, antisymmetry, and the Jacobi identity (inherited from the Lie bracket of vector fields).

For matrix Lie [[Def - Group|groups]] $G \leq \mathrm{GL}(n, \mathbb{R})$: $\mathfrak{g} = T_I G \subseteq T_I \mathrm{GL}(n) \cong M(n, \mathbb{R}) = \mathfrak{gl}(n, \mathbb{R})$, with bracket the matrix commutator $[A, B] = AB - BA$ — see [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]].

---

# Relate to Other Fields / Compression

The Lie algebra of $G$ is the **linearization of $G$ at the identity**: the tangent space carrying the algebraic shadow of the group multiplication, captured in a single bracket. It is the simultaneous instance of two structures already introduced — the [[Def - The Tangent Space|tangent space]] at a point of a smooth manifold, and an abstract [[Def - Lie Algebra|Lie algebra]] — and the construction is what bridges them.

From the [[Def - Lie Group|Lie-group-theoretic side]], it is the canonical finite-dimensional Lie algebra associated to a Lie group, a complete invariant up to coverings on the simply-connected side. From the manifold-theoretic side, it is the space of left-invariant vector fields, providing a global trivialization of $TG$.

**True name:** $\mathfrak{g}$ is **the algebraic shadow of $G$'s multiplication, captured to first order at $e$**. The Lie correspondence (Lee Thm 20.21) says this is a precise statement: for connected simply connected Lie groups, $\mathfrak{g}$ captures everything. Equivalently, $\mathfrak{g}$ is **the algebra of infinitesimal generators of one-parameter subgroups**: each $X \in \mathfrak{g}$ generates a unique one-parameter subgroup $t \mapsto \exp(tX)$, and the bracket measures the non-commutativity of these one-parameter subgroups via the BCH formula.

---

# Examples / Corollaries

**Is an instance: $\mathrm{Lie}(\mathbb{R}^n) \cong \mathbb{R}^n$ (abelian).** $T_0 \mathbb{R}^n = \mathbb{R}^n$ as vector spaces; left-invariant vector fields are constant; the bracket of constant vector fields is zero; so $\mathfrak{g}$ is an abelian Lie algebra of dimension $n$.

**Is an instance: $\mathrm{Lie}(\mathrm{GL}(n, \mathbb{R})) = \mathfrak{gl}(n, \mathbb{R})$.** $T_I \mathrm{GL}(n, \mathbb{R}) = M(n, \mathbb{R})$ since $\mathrm{GL}(n)$ is open in $M(n) \cong \mathbb{R}^{n^2}$. The bracket on $T_I = M(n)$ inherited from left-invariant vector fields is the matrix commutator $[A, B] = AB - BA$. So $\mathfrak{gl}(n, \mathbb{R}) = (M(n, \mathbb{R}), [\cdot, \cdot]_{\mathrm{comm}})$. See [[Ex - The Lie Algebra of GL(n,R) is the Space of n by n Matrices]].

**Is an instance: $\mathrm{Lie}(\mathrm{SL}(n, \mathbb{R})) = \mathfrak{sl}(n, \mathbb{R})$.** $\mathfrak{sl}(n) = \{A \in \mathfrak{gl}(n) : \mathrm{tr} A = 0\}$, the traceless matrices, dimension $n^2 - 1$. Computed by differentiating $\det A = 1$ at $A = I$: $\det(I + tX) = 1 + t \mathrm{tr} X + O(t^2)$, so the constraint is $\mathrm{tr} X = 0$.

**Is an instance: $\mathrm{Lie}(\mathrm{O}(n)) = \mathrm{Lie}(\mathrm{SO}(n)) = \mathfrak{so}(n)$.** $\mathfrak{so}(n) = \{A \in \mathfrak{gl}(n) : A^T = -A\}$, antisymmetric matrices, dimension $\binom{n}{2}$. Note that $\mathrm{O}(n)$ and $\mathrm{SO}(n)$ have the **same** Lie algebra because they share an identity component — and the Lie algebra only sees infinitesimal data at $e$.

**Is an instance: $\mathrm{Lie}(\mathrm{U}(n)) = \mathfrak{u}(n)$.** $\mathfrak{u}(n) = \{A \in \mathfrak{gl}(n, \mathbb{C}) : A^* = -A\}$, skew-Hermitian complex matrices viewed as a real Lie algebra. [[Def - Dimension|Dimension]] $n^2$ (as a real algebra).

**Is an instance: $\mathrm{Lie}(\mathrm{SU}(n)) = \mathfrak{su}(n)$.** $\mathfrak{su}(n) = \{A \in \mathfrak{u}(n) : \mathrm{tr} A = 0\}$, traceless skew-Hermitian matrices. Dimension $n^2 - 1$.

**Is an instance: $\mathrm{Lie}(S^1) \cong \mathbb{R}$ (abelian).** The circle has $1$-dimensional Lie algebra spanned by the angle vector field $\partial/\partial\theta$. Bracket is zero (only $1$-dimensional, and any $1$-dimensional Lie algebra is abelian by antisymmetry).

**Is an instance: $\mathrm{Lie}(\mathrm{Heis}(3)) = \mathfrak{h}_3$.** The Heisenberg Lie algebra, $3$-dimensional with basis $X, Y, Z$ and brackets $[X, Y] = Z$, $[X, Z] = [Y, Z] = 0$. Non-abelian, nilpotent.

**Corollary ([[Def - Dimension|dimensions]] match).** $\dim \mathfrak{g} = \dim G$.

**Corollary (functorial).** Every Lie group homomorphism $F : G \to H$ induces a Lie algebra homomorphism $F_* = dF_e : \mathfrak{g} \to \mathfrak{h}$ — see [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism]]. The assignment $G \mapsto \mathfrak{g}$, $F \mapsto F_*$ is a functor $\mathbf{LieGrp} \to \mathbf{LieAlg}$.

**Corollary (isomorphism preserved).** If $G \cong H$ as Lie groups, then $\mathfrak{g} \cong \mathfrak{h}$ as Lie algebras. The converse fails: $\mathfrak{so}(3) \cong \mathfrak{su}(2)$ as Lie algebras, but $\mathrm{SO}(3) \not\cong \mathrm{SU}(2)$ as Lie groups — they differ by a double cover. This is the canonical demonstration that the Lie functor is not injective on objects.

**Corollary (abelian iff abelian on identity component).** For a connected Lie group $G$, $G$ is abelian if and only if $\mathfrak{g}$ is abelian (Lee Problem 20-7). The proof routes through $\exp$: $G$ is generated by $\exp(\mathfrak{g})$, and elements of $\exp(\mathfrak{g})$ commute pairwise iff the brackets of their generators vanish.

**Calibration check.** If you can compute (i) $\mathrm{Lie}(\mathrm{SO}(3)) = \mathfrak{so}(3)$ as antisymmetric $3 \times 3$ matrices, of dimension $3$; (ii) the Lie bracket on $\mathfrak{gl}(n)$ as the matrix commutator; and (iii) the equivalence between left-invariant vector fields and tangent vectors at $e$ via the evaluation map — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] The Exponential Map *(from this chapter)*
> Given $\mathfrak{g}$ as the Lie algebra of $G$, the **exponential map** $\exp : \mathfrak{g} \to G$ is defined as $\exp(X) = \gamma_X(1)$ where $\gamma_X$ is the integral curve of the left-invariant vector field $X^L$ starting at $e$. See [[Def - Exponential Map of a Lie Group]].

> [!tip] The Lie Correspondence *(from Lie Groups, Advanced)*
> For connected, simply connected Lie groups, the assignment $G \mapsto \mathfrak{g}$ is an equivalence of categories with finite-dimensional Lie algebras. Every Lie algebra integrates uniquely to a simply connected Lie group, and Lie algebra homomorphisms lift uniquely to Lie group homomorphisms. This is the deep structural theorem unifying the algebra and geometry.

> [!tip] Killing Form and Semisimplicity *(from Lie Algebra Theory)*
> The Killing form $B(X, Y) = \mathrm{tr}(\mathrm{ad}_X \mathrm{ad}_Y)$ on $\mathfrak{g}$ is non-degenerate exactly when $\mathfrak{g}$ is **semisimple** (Cartan's criterion), and its signature distinguishes the compact, non-compact, and split real forms. On compact semisimple $G$, the (negative of the) Killing form is a bi-invariant Riemannian metric.

> [!tip] Adjoint Representation *(from this chapter)*
> The action of $G$ on $\mathfrak{g}$ by conjugation, $\mathrm{Ad}_g(X) = d(C_g)_e(X)$, is the **adjoint representation** $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$. Its derivative at the identity is $\mathrm{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$, $\mathrm{ad}_X(Y) = [X, Y]$ — the Lie algebra adjoint. See [[Def - Adjoint Representation]].
