---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Spinor Map and SL(2,C)"
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - Exponential Map of a Lie Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus. $SL(2,\mathbb{C})$ is the group of unit-determinant $2\times 2$ complex matrices; $\mathfrak{so}(1,3)$ is the [[Def - Lie Algebra of the Lorentz Group|Lie algebra of the Lorentz group]], with rotation generators $J_i$ and boost generators $K_i$ ($i = 1,2,3$) satisfying $[J_i,J_j] = \varepsilon_{ijk}J_k$, $[J_i,K_j] = \varepsilon_{ijk}K_k$, $[K_i,K_j] = -\varepsilon_{ijk}J_k$. We write $\mathrm{tr}$ for trace, $[B_1,B_2] = B_1B_2 - B_2B_1$ for the commutator, $\boldsymbol\sigma = (\sigma_1,\sigma_2,\sigma_3)$ for the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Pauli matrices]], and $\exp$ for the matrix exponential. $\mathscr{S}$ is the [[Def - The Spinor Map and SL(2,C)|spinor map]] and $\mathscr{S}'$ its differential at the identity. Full registry on [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

This is a compound page: it defines two interlocking notions — the **Lie algebra** $\mathfrak{sl}(2,\mathbb{C})$ (with the differential $\mathscr{S}'$ realising $\mathfrak{sl}(2,\mathbb{C})\cong\mathfrak{so}(1,3)$) and the **exponential map** $\exp : \mathfrak{sl}(2,\mathbb{C})\to SL(2,\mathbb{C})$ — because the exponential is how the algebra generates the group and the two are studied together.

---

# Axiom Motivation

The previous chapter built the Lie algebra of the Lorentz group by differentiating the defining condition $\Lambda^{\mathsf T}\eta\Lambda = \eta$. This page does the same for $SL(2,\mathbb{C})$, and then uses the spinor map to show the two algebras are *the same algebra in different clothes*. The motivation is to make the abstract isomorphism $\mathfrak{so}(1,3)_{\mathbb C}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ from [[Special Relativity X — The Lorentz Group as a Lie Group|the last chapter]] into a concrete identification of generators, and to understand why the group exponential carries half-angles.

The Lie algebra of a [[Def - Lie Group|matrix Lie group]] $G$ is the tangent space at the identity: the matrices $B$ such that $I + \varepsilon B$ lies in $G$ to first order in $\varepsilon$, equivalently $\exp(\varepsilon B) \in G$. For $SL(2,\mathbb{C})$ the defining condition is $\det A = 1$, so we ask which $B$ have $\det(I + \varepsilon B) = 1 + O(\varepsilon^2)$. The general variation-of-determinant formula $\det(I + \varepsilon B) = 1 + \varepsilon\,\mathrm{tr}\,B + O(\varepsilon^2)$ — itself a consequence of $\delta\ln\det A = \mathrm{tr}(A^{-1}\delta A)$ at $A = I$ — shows the condition is $\mathrm{tr}\,B = 0$. So the algebra is the **traceless** $2\times 2$ complex matrices. Why traceless rather than some other condition? Because the determinant constraint is *one complex equation*, and its linearisation is *one complex linear functional* on matrices, namely the trace; vanishing of the trace is exactly the kernel of that functional.

The dimension count is the consistency check the whole identification rests on. A traceless $2\times 2$ complex matrix has $8 - 2 = 6$ real parameters (eight from a complex matrix, minus two from the one complex trace constraint). This is the same as $\dim_{\mathbb R}\mathfrak{so}(1,3) = 6$. If the dimensions disagreed, no isomorphism could exist; their agreement is the first sign that $\mathscr{S}$ is a local isomorphism, which it must be if it is a covering map.

What is the bracket? The Lie bracket of any matrix Lie algebra is the [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator|commutator]] $[B_1,B_2] = B_1B_2 - B_2B_1$, and the only thing to check is that the commutator of two traceless matrices is traceless — which it is, since $\mathrm{tr}(B_1B_2) = \mathrm{tr}(B_2B_1)$ always, so $\mathrm{tr}[B_1,B_2] = 0$. This closure is what makes $\mathfrak{sl}(2,\mathbb{C})$ a Lie algebra and not merely a vector space.

The exponential map is forced on us as the way back from the algebra to the group: $\exp(B) = \sum_n B^n/n!$ converges for every matrix and lands in $SL(2,\mathbb{C})$ whenever $\mathrm{tr}\,B = 0$, because $\det\exp(B) = \exp(\mathrm{tr}\,B) = \exp(0) = 1$. The half-angles appear not by fiat but because the spinor map carries *two* factors of $A$: differentiating $A\underline X A^\dagger$ with $A = \exp(\varepsilon B)$ produces $B\underline X + \underline X B^\dagger$ (the $\varepsilon^1$ term), a *sum* of two contributions, so the algebra generator $B$ maps to a Lorentz generator that is effectively "doubled" — which is why, run backwards, a Lorentz rotation by $\theta$ comes from an $SL(2,\mathbb{C})$ generator carrying $\theta/2$.

What fails if we forgot tracelessness and exponentiated a non-traceless $B$? Then $\det\exp(B) = e^{\mathrm{tr}\,B}\neq 1$, and the result would leave $SL(2,\mathbb{C})$ — it would be a general invertible matrix, dilating the interval rather than preserving it. Tracelessness is exactly the condition that keeps the exponential inside the group, the matrix analogue of "the velocity is tangent to the constraint surface."

---

# The Definition

The **Lie algebra of $SL(2,\mathbb{C})$** is
$$
\mathfrak{sl}(2,\mathbb{C}) \;=\; \{\,B \in \mathrm{Mat}(2,\mathbb{C}) : \mathrm{tr}\,B = 0\,\},
$$
a real Lie algebra of dimension $6$, with bracket the matrix commutator $[B_1,B_2] = B_1B_2 - B_2B_1$ (which is traceless because $\mathrm{tr}(B_1B_2) = \mathrm{tr}(B_2B_1)$). A real basis is
$$
\sigma_1,\ \sigma_2,\ \sigma_3,\ i\sigma_1,\ i\sigma_2,\ i\sigma_3
$$
(the three traceless Pauli matrices and their products with $i$). The compact subalgebra $\mathfrak{su}(2) = \mathrm{span}_{\mathbb R}\{i\sigma_1,i\sigma_2,i\sigma_3\}$ of anti-Hermitian traceless matrices sits inside it.

The **differential of the spinor map** at the identity is the linear map
$$
\mathscr{S}' : \mathfrak{sl}(2,\mathbb{C}) \to \mathfrak{so}(1,3), \qquad
\mathscr{S}'(B) = \mathscr{H}^{-1}\circ\Phi_B'\circ\mathscr{H}, \quad \Phi_B'(\underline X) = B\,\underline X + \underline X\,B^\dagger,
$$
obtained by differentiating $\underline X \mapsto A\underline X A^\dagger$ along $A = \exp(\varepsilon B)$. It is a **Lie-algebra isomorphism**, $\mathscr{S}'([B_1,B_2]) = [\mathscr{S}'(B_1),\mathscr{S}'(B_2)]$, with the explicit action on the basis
$$
\boxed{\;\mathscr{S}'(\sigma_i) = 2K_i, \qquad \mathscr{S}'(i\sigma_i) = -2J_i,\;}
$$
proving
$$
\mathfrak{so}(1,3) \;\cong\; \mathfrak{sl}(2,\mathbb{C}).
$$
The Hermitian generators $\sigma_i$ map to boosts $K_i$; the anti-Hermitian generators $i\sigma_i$ map to rotations $J_i$.

The **exponential map** $\exp : \mathfrak{sl}(2,\mathbb{C}) \to SL(2,\mathbb{C})$, $\exp(B) = \sum_{n\ge 0}B^n/n!$, lands in $SL(2,\mathbb{C})$ because $\det\exp(B) = e^{\mathrm{tr}\,B} = 1$, and intertwines with the Lorentz-group exponential through the **commutative square**
$$
\mathscr{S}(\exp B) \;=\; \exp\big(\mathscr{S}'(B)\big), \qquad B \in \mathfrak{sl}(2,\mathbb{C}).
$$
Using $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$ for a unit $\mathbf n$, the two physically important families are
$$
\text{rotation:}\quad \exp\!\Big(-\tfrac{\theta}{2}\,n^j i\sigma_j\Big) = \cos\tfrac\theta2\,I - i\sin\tfrac\theta2\,(\mathbf n\cdot\boldsymbol\sigma),
$$
$$
\text{boost:}\quad \exp\!\Big(\tfrac{\psi}{2}\,n^j\sigma_j\Big) = \cosh\tfrac\psi2\,I + \sinh\tfrac\psi2\,(\mathbf n\cdot\boldsymbol\sigma),
$$
mapping under $\mathscr{S}$ to the Lorentz rotation $\exp(\theta\,n^j J_j)$ and boost $\exp(\psi\,n^j K_j)$ respectively.

Unlike the exponential of $\mathfrak{so}(1,3)$, which is **surjective** onto $SO^+(1,3)$, the exponential of $\mathfrak{sl}(2,\mathbb{C})$ is **not surjective** onto $SL(2,\mathbb{C})$: matrices of the form $-I + N$ with $N \neq 0$ nilpotent ($N^2 = 0$) have no logarithm in $\mathfrak{sl}(2,\mathbb{C})$. For every $A \in SL(2,\mathbb{C})$, however, either $A$ or $-A$ is an exponential, which (via the double cover) is consistent with surjectivity downstairs.

---

# Categorical / Structural Definition

The structural content is the commutative square of Lie functors. The spinor map $\mathscr{S}: SL(2,\mathbb{C})\to SO^+(1,3)$ is a homomorphism of Lie groups; applying the Lie-functor (tangent space at the identity) gives the homomorphism of Lie algebras $\mathscr{S}' = d\mathscr{S}_e: \mathfrak{sl}(2,\mathbb{C})\to\mathfrak{so}(1,3)$; and the naturality of the exponential — the fact that $\exp$ is a natural transformation from the Lie-algebra functor to the Lie-group functor — is exactly the square $\mathscr{S}\circ\exp = \exp\circ\mathscr{S}'$. This is the general theorem that a Lie group homomorphism commutes with the exponential maps of source and target, instantiated for the spinor map.

That $\mathscr{S}'$ is an *isomorphism* of Lie algebras while $\mathscr{S}$ is only a *covering* (not an isomorphism) of Lie groups is the cleanest illustration of a foundational fact: the Lie algebra sees only the *local* structure of the group, and two groups with the same Lie algebra — here $SL(2,\mathbb{C})$ and $SO^+(1,3)$ — can differ *globally* (here by the kernel $\mathbb{Z}/2$ and the consequent failure of $SO^+(1,3)$ to be simply connected). The exponential's surjectivity downstairs but not upstairs is a further global fingerprint: the cover, being "bigger," has elements ($-I + N$) not reachable by a single one-parameter subgroup, even though their images are.

---

# Relate to Other Fields / Compression

The differential $\mathscr{S}'$ realises concretely the complexification statement $\mathfrak{so}(1,3)_{\mathbb C}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ from [[Special Relativity X — The Lorentz Group as a Lie Group|the previous chapter]]: the two commuting $\mathfrak{su}(2)$ factors are the $\pm$ eigenspaces of complex conjugation, spanned by $J_i \pm iK_i$, and under $\mathscr{S}'$ these correspond to $\tfrac12(i\sigma_i) \mp \tfrac{i}{2}\sigma_i$ combinations in $\mathfrak{sl}(2,\mathbb{C})\otimes\mathbb{C}$. The Weyl spinors $(\tfrac12,0)$ and $(0,\tfrac12)$ are the representations on which one factor acts and the other is trivial.

The bracket-as-commutator and the exponential-collapses-by-Euler are the same phenomena as in the vault's [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator|matrix Lie bracket]] and [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices|\mathfrak{so}(3) computation]]; here the matrices are $2\times 2$ complex and traceless rather than $3\times 3$ real and antisymmetric, but the structure — tangent space at the identity, commutator bracket, exponential back to the group — is identical, and the [[Def - Exponential Map of a Lie Group|exponential map]] is the general construction.

**True name:** $\mathfrak{sl}(2,\mathbb{C})$ is "*the traceless $2\times 2$ complex matrices, with commutator bracket*," and the operational fact that makes it usable is "*a Pauli exponential collapses by Euler's formula because $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$*." Every rotation and boost matrix is built this way, and the half-angle is the signature of the double cover.

---

# Examples / Corollaries

**Is an instance — a boost generator.** $B = \tfrac\psi2\sigma_3 \in \mathfrak{sl}(2,\mathbb{C})$ (traceless). Then $\exp(B) = \cosh\tfrac\psi2\,I + \sinh\tfrac\psi2\,\sigma_3 = \mathrm{diag}(e^{\psi/2}, e^{-\psi/2})$, the $z$-boost matrix, and $\mathscr{S}(\exp B)$ is the Lorentz boost of rapidity $\psi$ along $z$ (consistent with $\mathscr{S}'(\sigma_3) = 2K_3$, since $B = \tfrac\psi2\sigma_3 \mapsto \psi K_3$).

**Is an instance — a rotation generator.** $B = -\tfrac\theta2 i\sigma_3 \in \mathfrak{sl}(2,\mathbb{C})$. Then $\exp(B) = \cos\tfrac\theta2\,I - i\sin\tfrac\theta2\,\sigma_3 = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$, a unitary matrix in $SU(2)$, mapping to the rotation by $\theta$ about $z$ (consistent with $\mathscr{S}'(i\sigma_3) = -2J_3$, so $B = -\tfrac\theta2 i\sigma_3 \mapsto \theta J_3$).

**Is an instance — verifying the bracket isomorphism.** Compute $[\sigma_1,\sigma_2] = 2i\sigma_3$ in $\mathfrak{sl}(2,\mathbb{C})$. Applying $\mathscr{S}'$: $[\mathscr{S}'(\sigma_1),\mathscr{S}'(\sigma_2)] = [2K_1, 2K_2] = 4[K_1,K_2] = 4(-J_3) = -4J_3$, while $\mathscr{S}'([\sigma_1,\sigma_2]) = \mathscr{S}'(2i\sigma_3) = 2\mathscr{S}'(i\sigma_3) = 2(-2J_3) = -4J_3$. They agree — the bracket is preserved, confirming $[K_1,K_2] = -J_3$.

**Is NOT an instance — a non-traceless matrix.** $B = \sigma_3 + I = \mathrm{diag}(2,0)$ has $\mathrm{tr}\,B = 2 \neq 0$, so $B \notin \mathfrak{sl}(2,\mathbb{C})$. Its exponential $\exp(B) = \mathrm{diag}(e^2, 1)$ has determinant $e^2 \neq 1$, leaving $SL(2,\mathbb{C})$; it generates a dilation, not a Lorentz transformation.

**Is NOT an instance — a target of the exponential that is not reached.** The matrix $A = -I + N$ with $N = \begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix}$ is in $SL(2,\mathbb{C})$ ($\det A = (-1)(-1) - 0 = 1$) but is *not* of the form $\exp(B)$ for any traceless $B$: its only eigenvalue is $-1$ (with a single Jordan block), and no traceless $2\times 2$ matrix exponentiates to a non-diagonalisable matrix with a negative repeated eigenvalue. This is the concrete witness that $\exp$ is not surjective on $SL(2,\mathbb{C})$. Its negative $-A = I - N$ *is* an exponential, $-A = \exp(-N)$ since $N^2 = 0$.

**Corollary — the half-angle, finally explained.** The factor of two in $\mathscr{S}'(\sigma_i) = 2K_i$ is the algebra-level statement of the half-angle: an $SL(2,\mathbb{C})$ generator maps to *twice* the corresponding Lorentz generator, so to produce a Lorentz rotation by $\theta$ (generator $\theta J_i$) you exponentiate the $SL(2,\mathbb{C})$ generator $\tfrac\theta2(i\sigma_i)$ carrying only half the parameter.

**Calibration check.** If you have understood this page you should be able to: (1) verify $\det\exp(B) = e^{\mathrm{tr}\,B}$ for a diagonalisable $B$ and conclude tracelessness is necessary and sufficient for $\exp(B)\in SL(2,\mathbb{C})$; (2) collapse $\exp(\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma)$ to $\cosh\tfrac\psi2\,I + \sinh\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma$ using $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$; (3) explain in one sentence why $\mathfrak{sl}(2,\mathbb{C})\cong\mathfrak{so}(1,3)$ does not imply $SL(2,\mathbb{C})\cong SO^+(1,3)$.

---

# Unlocked by This

> [!tip] The Casimir Operators and Field Equations *(from Quantum Field Theory)*
> The quadratic Casimirs of $\mathfrak{sl}(2,\mathbb{C})$ — built from $J^2 - K^2$ and $\mathbf J\cdot\mathbf K$ — label the finite-dimensional representations, and combined with the **Casimirs of the Poincaré group** ([[Def - Casimir Invariants of the Poincaré Group]]) they produce the relativistic wave equations: the Klein–Gordon equation for $(0,0)$, the Dirac equation for $(\tfrac12,0)\oplus(0,\tfrac12)$, the Maxwell equations for $(1,0)\oplus(0,1)$. The algebra isomorphism on this page is what lets these equations be written in $2\times 2$ spinor form.

> [!tip] The Exponential and the Geodesics of a Lie Group *(from Differential Geometry)*
> The matrix exponential $\exp:\mathfrak{sl}(2,\mathbb{C})\to SL(2,\mathbb{C})$ is the [[Def - Exponential Map of a Lie Group|Lie-group exponential]], whose images are the one-parameter subgroups — the geodesics through the identity for the canonical bi-invariant connection. The failure of surjectivity here is a feature non-compact Lie groups generally have and compact ones (like $SU(2)$, where $\exp$ *is* surjective) do not, a distinction visible in the contrast between the boost (non-compact, hyperbolic) and rotation (compact, periodic) one-parameter subgroups.
