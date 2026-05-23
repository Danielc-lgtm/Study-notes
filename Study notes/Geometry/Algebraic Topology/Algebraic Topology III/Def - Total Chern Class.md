---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Chern Forms of a U(n) Bundle"
  - "Def - de Rham Cohomology"
tags: [geometry, algebraic-topology, characteristic-classes]
---

# Notation

$E \to M$ is a complex rank-$n$ vector bundle with $U(n)$ structure group. $\theta$ is the curvature 2-form of a $U(n)$ connection on $E$. $c_r(E)$ is the [[Def - Chern Forms of a U(n) Bundle|$r$-th Chern form]], a real $2r$-form on $M$. $H^*_{\mathrm{dR}}(M; \mathbb{R}) = \bigoplus_k H^k_{\mathrm{dR}}(M; \mathbb{R})$ is the de Rham cohomology ring of $M$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

Once we have individual Chern forms $c_1, c_2, \ldots, c_n$, the natural question is: *what algebraic structure do they assemble into?* The answer is the **total Chern class**, a single object $c(E) \in H^{\mathrm{even}}(M; \mathbb{R})$ that packages all the individual classes. The reason to bundle them is twofold: they satisfy a multiplicative law under Whitney sum, and the total class has a clean formal expression as a determinant.

The Whitney sum formula

$$c(E \oplus F) = c(E) \cdot c(F)$$

is the central reason for assembling Chern forms into a total class. For individual classes, this reads

$$c_r(E \oplus F) = \sum_{i + j = r} c_i(E) \cdot c_j(F),$$

an awkward convolution. As a product of total classes, it is one line. The convolution arises because direct sum of bundles corresponds to block-diagonal connections, and the determinant of a block-diagonal matrix factors:

$$\det\!\left(I + \frac{i}{2\pi}\begin{pmatrix} \theta_E & 0 \\ 0 & \theta_F \end{pmatrix}\right) = \det\!\left(I + \frac{i}{2\pi}\theta_E\right) \cdot \det\!\left(I + \frac{i}{2\pi}\theta_F\right).$$

This is the Whitney sum formula, in one identity.

The formal expression

$$c(E) = \det\!\left(I + \frac{i}{2\pi}\theta\right) = 1 + c_1(E) + c_2(E) + \cdots + c_n(E)$$

is the most economical way to write down all Chern forms at once. Reading it as a single determinant rather than as a sum makes the connection to invariant theory transparent: the determinant is *the* characteristic invariant polynomial of a matrix, and the total Chern class is its translation to the curvature setting.

A second motivation is the **splitting principle**. Heuristically, every complex vector bundle "splits" (after suitable cohomological manipulation) into a direct sum of line bundles $E = L_1 \oplus L_2 \oplus \cdots \oplus L_n$, and then by Whitney sum

$$c(E) = c(L_1) \cdot c(L_2) \cdots c(L_n) = (1 + x_1)(1 + x_2)\cdots(1 + x_n)$$

where $x_i = c_1(L_i)$ are the **Chern roots**. The individual $c_r(E)$ are then the elementary symmetric polynomials of $x_1, \ldots, x_n$:

$$c_r(E) = \sigma_r(x_1, \ldots, x_n).$$

This factorisation is "fake" in general — most bundles do not literally split as direct sums — but the *computation* of Chern classes proceeds as if they do, via the splitting principle: any identity in symmetric functions of the $x_i$ is also true for the corresponding Chern classes. This is the framework in which Chern computations are actually performed.

The third motivation is **classification**: the total Chern class lives in the **even cohomology** $H^{\mathrm{even}}(M; \mathbb{R}) = \bigoplus_{k \geq 0} H^{2k}(M; \mathbb{R})$, and via the integer lift in $H^{\mathrm{even}}(M; \mathbb{Z})$, it provides the strongest computable invariant of the bundle. For line bundles ($n = 1$), $c(L) = 1 + c_1(L)$ contains the same information as $c_1(L)$ alone, and this is a *complete* invariant — line bundles on a CW complex are completely classified by $c_1 \in H^2(X; \mathbb{Z})$ (see [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]]). For higher-rank bundles, the total Chern class is necessary but not always sufficient; there can be inequivalent bundles with the same Chern classes (distinguished by torsion invariants or higher characteristic classes).

The fourth motivation is **functorial**: the assignment $E \mapsto c(E)$ is natural under pullback ($c(f^* E) = f^* c(E)$) and multiplicative under direct sum and tensor product (with appropriate formulae). These make $c$ a *characteristic class* in the formal sense — see [[Def - Characteristic Class]] — and identify $c(E)$ as the pullback of universal classes from the classifying space $BU(n)$.

---

# The Definition

Let $E \to M$ be a complex rank-$n$ vector bundle with $U(n)$ structure group and a chosen connection. The **total Chern form** of $E$ is

$$c(E) := \det\!\left(I + \frac{i}{2\pi}\theta\right) = 1 + c_1(E) + c_2(E) + \cdots + c_n(E),$$

a closed differential form on $M$ of mixed (even) degree, where $c_r(E)$ is the [[Def - Chern Forms of a U(n) Bundle|$r$-th Chern form]] of degree $2r$.

The **total Chern class** of $E$, also denoted $c(E)$, is the de Rham cohomology class:

$$c(E) = [c_1(E)] + [c_2(E)] + \cdots + [c_n(E)] \in H^{\mathrm{even}}_{\mathrm{dR}}(M; \mathbb{R}) = \bigoplus_{k \geq 0} H^{2k}_{\mathrm{dR}}(M; \mathbb{R}).$$

This class is independent of the connection (by [[Thm - Chern-Weil Theorem (Statement)|Chern–Weil]]) and lifts canonically to integer cohomology $H^{\mathrm{even}}(M; \mathbb{Z})$ via the universal Chern classes in $H^*(BU(n); \mathbb{Z})$.

**Fundamental properties:**

1. **Whitney sum formula:** $c(E \oplus F) = c(E) \cdot c(F)$, where the product is the cup product in cohomology. Equivalently, $c_r(E \oplus F) = \sum_{i+j=r} c_i(E) \cdot c_j(F)$.

2. **Naturality:** for any continuous (or smooth) map $f : N \to M$, $c(f^* E) = f^* c(E)$, i.e., the pullback bundle has pullback total Chern class.

3. **Normalisation:** for the tautological line bundle $\mathcal{O}(-1) \to \mathbb{CP}^1$, $c_1 = -h$ where $h$ is the positive generator of $H^2(\mathbb{CP}^1; \mathbb{Z}) = \mathbb{Z}$. Equivalently, $\int_{\mathbb{CP}^1} c_1(\mathcal{O}(-1)) = -1$.

These three properties uniquely characterise the total Chern class — they are the **Hirzebruch axioms** for Chern classes.

---

# Categorical / Structural Definition

The total Chern class is the image of $E$ under the **classifying map** composed with the universal Chern class. Specifically:

1. Every complex rank-$n$ vector bundle $E \to M$ has a **classifying map** $f_E : M \to BU(n)$, unique up to homotopy, such that $E = f_E^* \xi_n$ where $\xi_n \to BU(n)$ is the universal rank-$n$ bundle.

2. The integer cohomology of $BU(n)$ is a polynomial ring:
$$H^*(BU(n); \mathbb{Z}) = \mathbb{Z}[c_1, c_2, \ldots, c_n], \qquad \deg c_r = 2r.$$
The classes $c_r$ are the **universal Chern classes** of the universal bundle $\xi_n$.

3. The total Chern class of $E$ is the pullback:
$$c(E) = f_E^*(1 + c_1 + c_2 + \cdots + c_n) \in H^{\mathrm{even}}(M; \mathbb{Z}).$$

This is the most categorical description: Chern classes are pullbacks of universal classes from the classifying space, and the de Rham forms produced by Chern–Weil are just one specific representative cocycle in the appropriate cohomology class.

In **K-theory**, the total Chern class extends to a homomorphism

$$c : K^0(M) \to H^{\mathrm{even}}(M; \mathbb{Z}), \qquad [E] - [F] \mapsto c(E) / c(F)$$

(formal quotient, well-defined in the multiplicative group of even cohomology). This is *not* a ring homomorphism — that role is played by the **Chern character** $\mathrm{ch}$, which is additive on direct sums and multiplicative on tensor products.

---

# Relate to Other Fields / Compression

**True name:** the total Chern class is **the determinant $\det(I + i\theta/2\pi)$ of the matrix of curvature 2-forms, interpreted as a cohomology class**. The operational picture is: take the curvature, scale by $i/2\pi$, add the identity, compute the determinant in the exterior algebra of differential forms; what you get is a mixed-degree closed form whose cohomology class is connection-independent. The factorisation $(1 + x_1)(1 + x_2)\cdots(1 + x_n)$ in the splitting-principle picture reveals the structure as a product over Chern roots.

In **algebraic topology**, $c(E)$ generates the cohomology of the classifying space $BU(n)$ as a polynomial ring. Universal characteristic classes for any structure group $G$ are characterised by the cohomology of $BG$; for compact connected $G$, the cohomology is a polynomial ring with one generator per generator of $\mathbb{R}[\mathfrak{g}]^G$. Chern classes are the case $G = U(n)$.

In **algebraic geometry**, $c(E)$ corresponds to the **Atiyah class** in $H^1(M, \Omega^1 \otimes \mathrm{End}\, E)$, the obstruction to a holomorphic splitting of the bundle. The Chern classes are recoverable by tracing powers of the Atiyah class.

In **gauge theory**, $c(E)$ provides the topological labels of gauge field configurations. For $U(n)$ bundles, the $n - 1$ classes $c_1, \ldots, c_n$ (well, all $n$ but $c_n$ is the Euler class for the underlying real bundle) label different topological sectors. The Yang–Mills equations have distinct moduli spaces in each sector, labelled by the second Chern number $\int c_2$ for $SU(n)$ instantons.

---

# Examples / Corollaries

**Example: trivial bundle.** $c(E_{\mathrm{trivial}}) = 1$, since the curvature of the flat connection vanishes.

**Example: line bundle.** $c(L) = 1 + c_1(L)$ for any complex line bundle $L$. All higher $c_r$ vanish because rank is 1.

**Example: $T\mathbb{CP}^n$.** From the Euler sequence $0 \to \mathcal{O} \to \mathcal{O}(1)^{\oplus(n+1)} \to T\mathbb{CP}^n \to 0$ and the Whitney sum formula applied to the corresponding cohomological factorisation,

$$c(T\mathbb{CP}^n) = \frac{c(\mathcal{O}(1)^{\oplus(n+1)})}{c(\mathcal{O})} = \frac{(1 + h)^{n+1}}{1} = (1 + h)^{n+1},$$

where $h = c_1(\mathcal{O}(1)) \in H^2(\mathbb{CP}^n; \mathbb{Z})$. Reading off coefficients:

$$c_r(T\mathbb{CP}^n) = \binom{n+1}{r} h^r.$$

In particular, $c_n(T\mathbb{CP}^n) = (n+1) h^n$, and $\int_{\mathbb{CP}^n} c_n = n + 1 = \chi(\mathbb{CP}^n)$.

**Example: tangent bundle of $S^{2n}$.** The complexified tangent bundle $TS^{2n} \otimes \mathbb{C}$ has $c(TS^{2n} \otimes \mathbb{C}) = 1$, because $S^{2n}$ has trivial real cohomology in odd degrees. But the **Euler class** $e(TS^{2n}) \in H^{2n}(S^{2n}; \mathbb{Z}) = \mathbb{Z}$ is $2$ (when $S^{2n}$ has standard orientation), recovering the Euler characteristic $\chi(S^{2n}) = 2$. This shows that the Euler class is not always the top Chern class of the complexification.

**Example: Whitney sum on a surface.** On a surface $M^2$, $H^{\mathrm{even}}(M; \mathbb{Z}) = H^0(M) \oplus H^2(M)$. For a bundle of rank 1, $c(L) = 1 + c_1(L) \in H^0 \oplus H^2$; for rank 2, $c(E) = 1 + c_1(E) \in H^0 \oplus H^2$ (since $H^4(M^2) = 0$). The Whitney sum formula $c(L \oplus L') = c(L) c(L') = (1 + c_1(L))(1 + c_1(L')) = 1 + c_1(L) + c_1(L') + c_1(L) \cdot c_1(L')$. The product $c_1(L) \cdot c_1(L')$ vanishes for dimensional reasons ($H^4(M^2) = 0$), so $c_1(L \oplus L') = c_1(L) + c_1(L')$, recovering the additivity of $c_1$ for line bundles on a surface.

**Example: rank-2 bundle on $S^4$.** $H^*(S^4; \mathbb{Z}) = \mathbb{Z}$ in degrees 0, 4 and zero elsewhere. So for a rank-2 complex vector bundle $E \to S^4$, $c(E) = 1 + c_2(E)$ (with $c_1 = 0$ for dimensional reasons in $H^2(S^4) = 0$). The bundle is classified by $c_2 \in H^4(S^4; \mathbb{Z}) = \mathbb{Z}$ — an integer, the **second Chern number**. For $SU(2) = S^3$ bundles, this integer is the **instanton number** when $S^4$ is interpreted as the compactification of $\mathbb{R}^4$.

**Is NOT an instance: a single odd-degree form.** Chern forms are always of even degree (since curvature is a 2-form and the determinant in differential forms produces even degrees), so there is no $c_{1/2}$ or $c_{3/2}$. The total Chern class lives in even cohomology only.

**Corollary: $c(E^*) = $ conjugate.** For the dual bundle $E^*$, $c_r(E^*) = (-1)^r c_r(E)$, so

$$c(E^*) = \sum_r (-1)^r c_r(E) = c(E)|_{c_r \to (-c_r)}.$$

In total-class form, $c(E^*)(t) = c(E)(-t)$ where $t$ is the formal degree variable.

**Corollary: total Chern class commutes with sums.** If $E = E_1 \oplus E_2 \oplus \cdots \oplus E_k$, then $c(E) = c(E_1) c(E_2) \cdots c(E_k)$. Applied to line bundle decompositions (splitting principle), this gives the factorisation $c(E) = \prod_i (1 + x_i)$ with Chern roots $x_i$.

**Corollary: integrality.** $c(E) \in H^{\mathrm{even}}(M; \mathbb{Z}) \otimes \mathbb{R}$ — the de Rham class lifts to integer cohomology. For integer cycles $z$, $\int_z c_r \in \mathbb{Z}$.

**Calibration check.** If you understand the definition you should be able to: (i) write $c(L_1 \oplus L_2)$ in terms of $c_1(L_1)$ and $c_1(L_2)$; (ii) compute $c(T\mathbb{CP}^2)$ explicitly; (iii) explain why $c(E)$ has no odd-degree component.

---

# Unlocked by This

> [!tip] Splitting Principle *(from Algebraic Topology)*
> The **splitting principle** says: for any complex vector bundle $E \to M$ of rank $n$, there exists a continuous map $p : F \to M$ (where $F$ is the **flag bundle** of $E$) such that (i) $p^* : H^*(M; \mathbb{Z}) \to H^*(F; \mathbb{Z})$ is injective, and (ii) $p^* E$ splits as a direct sum of line bundles on $F$. This means: any identity in symmetric functions of "Chern roots" $x_1, \ldots, x_n$ that holds for split bundles holds for *all* bundles after pulling back, and by injectivity it holds on $M$. The splitting principle is what makes the formal-power-series manipulations of Chern classes (Chern character, Todd class, $\hat A$-genus) work uniformly for all bundles.

> [!tip] Cohomology of Grassmannians *(from Schubert Calculus)*
> The classifying space $BU(n)$ is a direct limit of complex Grassmannians $\mathrm{Gr}(n, N)$ as $N \to \infty$, and $H^*(\mathrm{Gr}(n, N); \mathbb{Z})$ is generated by Chern classes of the tautological rank-$n$ bundle, with relations coming from the **Schubert decomposition**. This is the foundation of **Schubert calculus**, the intersection theory of subvarieties of Grassmannians; it has applications throughout enumerative algebraic geometry (counting lines on cubic surfaces, conics tangent to five given conics, etc.) via Chern-class computations on Grassmannians and flag varieties.
