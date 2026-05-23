---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Vector Bundle"
  - "Def - de Rham Cohomology"
  - "Def - Chern Forms of a U(n) Bundle"
tags: [geometry, algebraic-topology, characteristic-classes]
---

# Notation

$E \to M$ is a vector bundle (real or complex) over a topological space or manifold $M$. $f : N \to M$ is a continuous map; $f^* E \to N$ is the **pullback bundle**. $H^*(M; R)$ is cohomology with coefficients in a ring $R$ (typically $\mathbb{Z}$, $\mathbb{R}$, $\mathbb{Z}/2$, $\mathbb{Q}$). A **characteristic class** is denoted $c$, $w$, $p$, $e$ depending on type (Chern, Stiefel–Whitney, Pontryagin, Euler). See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

The motivating question is: *what is the right abstract notion of "characteristic invariant of a vector bundle"?* We have seen [[Def - Chern Forms of a U(n) Bundle|Chern forms]] $c_r$ for complex vector bundles, which produce real cohomology classes from curvature. We want to know: in what sense are these *the* invariants, and what other invariants exist for other types of bundles (real, oriented, spin)?

The answer is the formal notion of a **characteristic class**: an assignment to every vector bundle of a cohomology class on its base, *naturally* with respect to pullback. The naturality condition is the central axiom: it is what makes characteristic classes a topological invariant in the strict sense (they depend only on the isomorphism class of the bundle, not on auxiliary data like a connection), and it is what allows them to be computed by pulling back from a universal classifying space.

The naturality axiom $c(f^* E) = f^* c(E)$ for every continuous map $f : N \to M$ implies several things at once:

1. **Topological invariance:** the class $c(E) \in H^*(M; R)$ depends only on the isomorphism class of $E$ as a bundle, not on any auxiliary structure.
2. **Functoriality:** the assignment $E \mapsto c(E)$ is a natural transformation between two functors (isomorphism classes of bundles, and cohomology).
3. **Universal characterisation:** every characteristic class is determined by its values on a universal bundle $\xi$ over a classifying space $BG$. Specifically, $c$ is determined by $c(\xi) \in H^*(BG; R)$, since for any bundle $E$ with classifying map $f_E : M \to BG$, we have $c(E) = f_E^* c(\xi)$.

The universal characterisation reduces the *classification* of characteristic classes to the computation of $H^*(BG; R)$. For the principal classes:

- $G = U(n)$: $H^*(BU(n); \mathbb{Z}) = \mathbb{Z}[c_1, c_2, \ldots, c_n]$ — Chern classes are *all* the characteristic classes of complex vector bundles in integer cohomology.
- $G = O(n)$: $H^*(BO(n); \mathbb{Z}/2) = \mathbb{Z}/2[w_1, w_2, \ldots, w_n]$ — Stiefel–Whitney classes.
- $G = SO(n)$: $H^*(BSO(n); \mathbb{Z}/2) = \mathbb{Z}/2[w_2, w_3, \ldots, w_n]$ — Stiefel–Whitney except $w_1$ (which is the orientability obstruction, vanishing for $SO$).
- $G = SO(2n)$: includes additionally the **Euler class** $e \in H^{2n}(BSO(2n); \mathbb{Z})$ with $e^2 = p_n$ (top Pontryagin).
- $G = SO(n)$, integer cohomology: $H^*(BSO(n); \mathbb{Z})[\tfrac{1}{2}] = \mathbb{Z}[\tfrac{1}{2}][p_1, p_2, \ldots]$ — **Pontryagin classes** (mod 2-torsion).

The structure of $H^*(BG; R)$ is the *content* of the theory: it tells you exactly which characteristic classes exist and what relations they satisfy.

Why is this the right axiomatisation? Three reasons:

**(a) Naturality is the minimal condition for any meaningful invariant.** Any invariant of a bundle that does not respect pullback would be unstable under deformation of the base — it could change discontinuously with the base manifold, even when the bundle is "the same" via pullback. Naturality forces the invariant to be a *cohomology-valued function* of bundle isomorphism class.

**(b) The universal classifying space is rich enough.** For every Lie group $G$ there is a classifying space $BG$ with a universal principal $G$-bundle $EG \to BG$, such that every principal $G$-bundle is a pullback of this universal one (uniquely up to homotopy). So characteristic classes are exactly elements of $H^*(BG; R)$, and the classification is *complete* once $H^*(BG; R)$ is computed.

**(c) The cohomology of $BG$ is computable.** For compact connected Lie groups $G$, $H^*(BG; \mathbb{Q})$ is a polynomial ring on generators corresponding to the **Chern–Weil construction** — invariant polynomials on the Lie algebra $\mathfrak{g}$. The integer cohomology adds torsion that has to be tracked separately, but the rational structure is fully captured by Chern–Weil.

The deepest content is that **every characteristic class is a polynomial in the basic Chern, Pontryagin, Stiefel–Whitney, or Euler classes** (depending on the structure group). There are no exotic characteristic classes outside this framework — the polynomial-ring structure of $H^*(BG)$ exhausts everything.

---

# The Definition

A **characteristic class** of complex rank-$n$ vector bundles, valued in cohomology with coefficients in a ring $R$, is an assignment

$$c : \{\text{isomorphism classes of complex rank-}n\text{ bundles on }M\} \to H^*(M; R)$$

defined for every topological space (or CW complex, or manifold) $M$, satisfying the **naturality** axiom: for every continuous map $f : N \to M$ and every bundle $E \to M$,

$$c(f^* E) = f^* c(E).$$

The analogous definition holds for **real vector bundles** (structure group $O(n)$), **oriented real bundles** (structure group $SO(n)$), **spin bundles** (structure group $\mathrm{Spin}(n)$), and any other structure group $G$ via principal $G$-bundles.

**Examples of characteristic classes:**

- **Chern classes** $c_1, c_2, \ldots, c_n$ for complex rank-$n$ bundles, in $H^{2r}(M; \mathbb{Z})$. See [[Def - Chern Forms of a U(n) Bundle]], [[Def - First Chern Class]], [[Def - Second Chern Class]].
- **Stiefel–Whitney classes** $w_1, w_2, \ldots, w_n$ for real rank-$n$ bundles, in $H^r(M; \mathbb{Z}/2)$.
- **Pontryagin classes** $p_1, p_2, \ldots$ for real oriented bundles, in $H^{4r}(M; \mathbb{Z})$, defined by $p_r(E_{\mathbb{R}}) = (-1)^r c_{2r}(E_{\mathbb{R}} \otimes \mathbb{C})$.
- **Euler class** $e(E)$ for oriented real rank-$n$ bundles, in $H^n(M; \mathbb{Z})$.
- **Total Chern class** $c(E) = 1 + c_1 + c_2 + \cdots \in H^{\mathrm{even}}(M; \mathbb{Z})$.
- **Chern character** $\mathrm{ch}(E) \in H^{\mathrm{even}}(M; \mathbb{Q})$.
- **Todd class** $\mathrm{Td}(E) \in H^{\mathrm{even}}(M; \mathbb{Q})$.

**The fundamental theorem of characteristic classes** (Brown representability + classifying space theory):

Characteristic classes for principal $G$-bundles, valued in $H^*(\cdot; R)$, are in bijection with elements of $H^*(BG; R)$, where $BG$ is the classifying space of $G$. The bijection sends $\alpha \in H^*(BG; R)$ to the characteristic class $E \mapsto f_E^* \alpha$, where $f_E : M \to BG$ is the classifying map of $E$.

For compact connected Lie groups $G$, $H^*(BG; \mathbb{Q})$ is a polynomial ring whose generators correspond to the invariant polynomials on $\mathfrak{g}$ via the **Chern–Weil construction**.

---

# Categorical / Structural Definition

A characteristic class is a **natural transformation** between two functors $\mathrm{Top}^{\mathrm{op}} \to \mathrm{Set}$:

- $\mathrm{Bun}_G(\cdot)$: isomorphism classes of principal $G$-bundles on a space.
- $H^*(\cdot; R)$: cohomology with coefficients in $R$.

The natural transformation $c : \mathrm{Bun}_G \to H^*(\cdot; R)$ assigns to each bundle a cohomology class, naturally with respect to pullback.

Equivalently, by **Brown representability**, both functors are representable: $\mathrm{Bun}_G(X) = [X, BG]$ and $H^n(X; R) = [X, K(R, n)]$. A natural transformation is then a morphism between the representing spaces, i.e., a homotopy class of maps $BG \to K(R, n)$ — which is exactly an element of $H^n(BG; R)$. The total natural transformation is an element of $H^*(BG; R) = \prod_n H^n(BG; R)$.

This is the *categorical* characterisation: **characteristic classes are elements of $H^*(BG; R)$**. The Chern–Weil construction is the differential-geometric realisation, computing the de Rham cohomology of $BG$ in terms of invariant polynomials on $\mathfrak{g}$.

In **stable homotopy theory**, characteristic classes generalise further to **cohomology operations** in **extraordinary cohomology theories** like K-theory or cobordism. The **Adams operations** $\psi^k$ in K-theory are characteristic classes that are *not* polynomial in Chern classes — they are independent invariants of K-theory.

---

# Relate to Other Fields / Compression

**True name:** a characteristic class is **an obstruction to a structure being globally trivial**, packaged as a cohomology class natural in the base. Each characteristic class has an "obstruction" interpretation:

- $w_1$ obstructs orientability (vanishes iff the bundle is orientable).
- $w_2$ obstructs spin structure (vanishes iff a $\mathrm{Spin}$-lift exists).
- $c_1$ obstructs a global non-vanishing section (for line bundles).
- $c_n =$ Euler class obstructs a global non-vanishing section (for top-rank).
- Higher $c_r$ obstruct $r$-fold-linearly-independent global sections.
- $p_1$ relates to signature and curvature integrals.

Each obstruction lives in the appropriate cohomology group determined by the obstruction theory: an obstruction to extending a section across a $k$-cell lives in $H^k(M; \pi_{k-1}(\text{fibre}))$, and the *first nonzero* obstruction is captured by the corresponding characteristic class.

In **algebraic geometry**, characteristic classes are computed via the **Chow ring** of intersection theory rather than singular cohomology, but the formal structure is the same. The Chow ring of a Grassmannian is generated by Schubert cycles, which are precisely the universal Chern classes.

In **K-theory**, characteristic classes correspond to **stable operations**: natural transformations $K^0(\cdot) \to K^0(\cdot)$. The Adams operations $\psi^k$ are the key examples, with $\psi^k$ acting as multiplication by $k^n$ on the line-bundle part $K^0(BU(1))^n$. Adams operations are *not* polynomial in Chern classes — they reveal K-theory information invisible to ordinary cohomology.

In **physics**, characteristic classes are the topological labels of field configurations:
- Magnetic monopole charge = $\int c_1$ (Maxwell).
- Instanton number = $\int c_2$ (Yang–Mills).
- Soliton winding = degree of a map = top Chern number.
- Witten anomaly coefficient = Pontryagin number.
- TKNN integer (quantum Hall) = $\int c_1$.

---

# Examples / Corollaries

**Example: Chern classes of complex bundles.** For a complex vector bundle $E$, the Chern classes $c_r(E) \in H^{2r}(M; \mathbb{Z})$ are the fundamental characteristic classes. They satisfy naturality, multiplicativity under Whitney sum, and the normalisation $c_1(\mathcal{O}(-1)) = -h$ on $\mathbb{CP}^1$.

**Example: Stiefel–Whitney classes.** For a real rank-$n$ bundle $E_{\mathbb{R}}$, the Stiefel–Whitney classes $w_r(E_{\mathbb{R}}) \in H^r(M; \mathbb{Z}/2)$ satisfy:

- $w_1(E)$ vanishes iff $E$ is orientable.
- $w_2(E)$ vanishes iff $E$ admits a spin structure (a lift of the structure group from $SO(n)$ to $\mathrm{Spin}(n)$).
- The total Stiefel–Whitney class $w(E) = 1 + w_1 + w_2 + \cdots$ satisfies $w(E \oplus F) = w(E) w(F)$.

For $\mathbb{RP}^2$ (real projective plane), $w_1 \neq 0$ (it is non-orientable), so it has no Stiefel–Whitney lift to $\mathbb{Z}$.

**Example: Pontryagin classes.** For a real oriented bundle $E_{\mathbb{R}}$, $p_r(E_{\mathbb{R}}) = (-1)^r c_{2r}(E_{\mathbb{R}} \otimes \mathbb{C}) \in H^{4r}(M; \mathbb{Z})$. Pontryagin classes live in degrees divisible by 4 and are "real" characteristic classes that survive in integer cohomology (modulo torsion). For a 4-manifold $M^4$, $\int_M p_1 = 3 \sigma(M)$ — the **signature theorem** of Hirzebruch.

**Example: Euler class.** For an oriented real rank-$n$ bundle $E_{\mathbb{R}}$, the Euler class $e(E_{\mathbb{R}}) \in H^n(M; \mathbb{Z})$ is the *top* characteristic class. For the tangent bundle $TM$ of a closed oriented manifold, $\int_M e(TM) = \chi(M)$, the Euler characteristic. For a complex rank-$n$ bundle viewed as a real rank-$2n$ bundle, $e(E_{\mathbb{R}}) = c_n(E)$, the top Chern class.

**Example: Chern character.** $\mathrm{ch}(E) = \mathrm{Tr}(\exp(i\theta/2\pi)) = n + c_1 + \tfrac{1}{2}(c_1^2 - 2c_2) + \cdots \in H^{\mathrm{even}}(M; \mathbb{Q})$. The Chern character is *additive* on direct sums ($\mathrm{ch}(E \oplus F) = \mathrm{ch}(E) + \mathrm{ch}(F)$) and *multiplicative* on tensor products ($\mathrm{ch}(E \otimes F) = \mathrm{ch}(E) \cdot \mathrm{ch}(F)$). This is the natural ring homomorphism $K^0(M) \otimes \mathbb{Q} \to H^{\mathrm{even}}(M; \mathbb{Q})$.

**Example: Todd class.** $\mathrm{Td}(E) = \prod_i \frac{x_i}{1 - e^{-x_i}}$ where $x_i$ are Chern roots. It appears in the Hirzebruch–Riemann–Roch formula: $\chi(X, E) = \int_X \mathrm{ch}(E) \mathrm{Td}(X)$.

**Is NOT an instance: bundle metric.** A choice of Hermitian metric on a complex bundle is *not* a characteristic class — it is auxiliary data, not a topological invariant. Different metrics on the same bundle give the same characteristic classes (since they are isomorphic bundles), but the metric itself is not a cohomology class.

**Is NOT an instance: connection.** A connection on a bundle is also not a characteristic class — it is *additional structure*. Different connections give the same Chern classes (independence of connection, Chern–Weil), but the connection 1-form itself is not natural under pullback in the right way.

**Corollary: Whitney sum formulae.**

- Chern: $c(E \oplus F) = c(E) c(F)$.
- Stiefel–Whitney: $w(E \oplus F) = w(E) w(F)$.
- Pontryagin (mod 2-torsion): $p(E \oplus F) = p(E) p(F)$.
- Euler: $e(E \oplus F) = e(E) e(F)$.

**Corollary: vanishing on trivial bundles.** All characteristic classes (other than the leading $1$) vanish on trivial bundles. This is because the trivial bundle has classifying map a constant, and constants pull back any cohomology class to zero (in positive degree).

**Corollary: cohomology of classifying spaces.** $H^*(BU(n); \mathbb{Z}) = \mathbb{Z}[c_1, \ldots, c_n]$, $H^*(BO(n); \mathbb{Z}/2) = \mathbb{Z}/2[w_1, \ldots, w_n]$, $H^*(BSO(n); \mathbb{Q}) = \mathbb{Q}[p_1, p_2, \ldots]$ (with Euler class adjoined in even rank). These polynomial structures are the universal classifications of characteristic classes.

**Calibration check.** If you understand the definition you should be able to: (i) explain why $w_1$ is an orientability obstruction; (ii) verify naturality $c(f^* E) = f^* c(E)$ from the construction of Chern classes; (iii) compute Pontryagin classes from Chern classes via $p_r = (-1)^r c_{2r}(\cdot \otimes \mathbb{C})$; (iv) state the Whitney sum formula for Stiefel–Whitney and verify on simple cases.

---

# Unlocked by This

> [!tip] Atiyah–Singer Index Theorem *(from Analysis on Manifolds)*
> For an elliptic differential operator $D$ on a compact manifold $M$, the **analytic index** $\mathrm{ind}(D) = \dim\ker D - \dim\mathrm{coker}\, D$ equals an integral of characteristic classes:
> $$\mathrm{ind}(D) = \int_M \mathrm{ch}(\sigma(D)) \cdot \mathrm{Td}(TM \otimes \mathbb{C}),$$
> where $\sigma(D)$ is the principal symbol of $D$, a K-theory class on $M$. This is the **Atiyah–Singer index theorem**, one of the deepest results in mathematics: it computes a *spectral* quantity (the dimension of the kernel of an elliptic operator) as a *topological* integral. Special cases include the Gauss–Bonnet theorem (Euler characteristic from curvature), Hirzebruch–Riemann–Roch (holomorphic Euler characteristic), and the signature theorem.

> [!tip] Cobordism *(from Differential Topology)*
> Two closed oriented $n$-manifolds $M, N$ are **cobordant** if there is a compact oriented $(n+1)$-manifold $W$ with $\partial W = M \sqcup \bar N$. The set of cobordism classes forms the **cobordism ring** $\Omega^{\mathrm{SO}}_n$. **Pontryagin numbers** $\int_M p_{i_1} \cdots p_{i_k}$ are cobordism invariants, and Thom's theorem identifies $\Omega^{\mathrm{SO}}_* \otimes \mathbb{Q}$ as a polynomial ring on classes detected by Pontryagin numbers. This makes characteristic classes the *complete invariant* for rational cobordism.

> [!tip] String Theory Anomaly Cancellation *(from Theoretical Physics)*
> In Type I superstring theory, the **Green–Schwarz mechanism** cancels gauge anomalies via a counterterm involving the *eight*-form combination of Pontryagin and Chern classes of the spacetime tangent bundle and the gauge bundle. Specifically, for $E_8 \times E_8$ heterotic strings, the anomaly is proportional to $\mathrm{Tr}\, R^4 + \mathrm{Tr}\, F^4 -$ (cross terms), and cancellation requires these polynomials to *split* as products of lower-degree characteristic classes — a stringent topological condition that selected $E_8 \times E_8$ as one of two consistent gauge groups for 10D heterotic strings.
