---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Vector Bundle"
  - "Def - Differential k-Form on a Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, algebraic-topology, characteristic-classes, gauge-theory]
---

# Notation

$E \to M$ is a complex vector bundle of rank $n$ with structure group $U(n)$ (equivalently, a rank-$n$ complex bundle with Hermitian metric). $\omega = \omega_U$ is a local **connection 1-form** in a frame $e_U$ over an open patch $U \subseteq M$; it is an $n \times n$ matrix of 1-forms with values in $\mathfrak{u}(n)$ (anti-Hermitian matrices). $\theta = \theta_U = d\omega + \omega \wedge \omega$ is the local **curvature 2-form**; it is an $n \times n$ matrix of 2-forms with values in $\mathfrak{u}(n)$. The wedge product $\omega \wedge \omega$ is matrix multiplication composed with wedge of forms: $(\omega \wedge \omega)^a_b = \omega^a_c \wedge \omega^c_b$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

> [!warning] Convention: $i/(2\pi)$ normalisation
> The factor $i/(2\pi)$ in $\det(I + i\theta/(2\pi))$ is chosen so that the **periods** of Chern forms — their integrals over integer cycles — are integers. Different conventions absorb the factors $i$, $2\pi$, or even both into the curvature; the resulting forms differ by overall scalars and one is sometimes the negative of the other. The de Rham class is the same up to normalisation. Frankel uses the mathematician's anti-Hermitian $\mathfrak{u}(n)$ and the factor $i/(2\pi)$; we follow this.

---

# Axiom Motivation

The motivating question is: *what closed differential forms can we extract from the curvature of a connection, and what do they tell us about the bundle?* For a Riemannian surface, the **Gaussian curvature** $K$ gives the closed 2-form $(K/2\pi) \, dA$ whose integral over the surface equals the Euler characteristic — the Gauss–Bonnet theorem. This is one of the great theorems of geometry, but it is a single instance, applying only to the tangent bundle of a 2-manifold. Chern's question was: *is this a special case of a general construction?* The answer is yes, and the general construction is the **Chern–Weil homomorphism**: invariant polynomials of curvature give characteristic forms.

Why should *polynomials* of curvature give closed forms? Curvature itself is a 2-form $\theta$ valued in $\mathfrak{u}(n)$ — a matrix of 2-forms. A polynomial $P$ in matrix entries of $\theta$, with constant coefficients, gives a higher-degree differential form. For this form to be:
- **Closed** ($dP(\theta) = 0$): requires $P$ to be **invariant** under the adjoint action of $U(n)$ on $\mathfrak{u}(n)$, i.e., $P(g \theta g^{-1}) = P(\theta)$ for $g \in U(n)$. This is because the Bianchi identity $\nabla \theta = 0$ (where $\nabla$ is the covariant exterior derivative) implies $dP(\theta) = 0$ if and only if $P$ is invariant.
- **Globally defined** on $M$: requires $P$ to be invariant in the same sense, because under change of frame $\theta \to g\theta g^{-1}$, and invariance ensures $P(\theta)$ does not depend on the frame.

The natural candidates for invariant polynomials on $\mathfrak{u}(n)$ are the **coefficients of the characteristic polynomial** $\det(\lambda I - A)$:

$$\det(\lambda I - A) = \lambda^n - \mathrm{Tr}(A) \lambda^{n-1} + \cdots + (-1)^n \det(A).$$

These are the **elementary symmetric polynomials** of the eigenvalues of $A$. They are obviously invariant under conjugation $A \to gAg^{-1}$ (since the eigenvalues are invariants of the conjugacy class). Equivalently, expanding $\det(I + A)$ gives

$$\det(I + A) = 1 + \mathrm{Tr}(A) + \tfrac{1}{2}[(\mathrm{Tr}\, A)^2 - \mathrm{Tr}(A^2)] + \cdots + \det(A),$$

a sum of degree-$r$ invariant polynomials $\mathrm{Tr}(\wedge^r A)$ for $r = 0, 1, \ldots, n$.

Now substitute $A = (i/2\pi) \theta$, with the factor $i$ to make the result *real* (since $\theta$ is anti-Hermitian, $i\theta$ is Hermitian) and the factor $1/(2\pi)$ to make the periods *integers*. The result is the **total Chern form**:

$$c(E) := \det\!\left(I + \frac{i}{2\pi}\theta\right) = 1 + c_1(E) + c_2(E) + \cdots + c_n(E),$$

a sum of forms of even degree, where $c_r$ is a $2r$-form. Each $c_r$ is the local statement of an invariant polynomial applied to curvature.

Why the factor $i$? Because $\theta$ is anti-Hermitian ($\theta^* = -\theta$), and $i\theta$ is Hermitian. The trace of a Hermitian matrix is real, the determinant of $I + (\text{Hermitian})$ is real, so the resulting Chern forms are *real* forms on $M$ — not complex-valued. If we omitted $i$, the Chern forms would be imaginary, and we would have to track imaginary signs throughout. The $i$ is the right cleanup factor.

Why the factor $1/(2\pi)$? Because we want the integrality $\int_z c_r \in \mathbb{Z}$ for integer cycles $z$, and this requires a specific normalisation. The simplest example is the case of $U(1)$ and a circle: a loop of holonomy $e^{i\alpha}$ around a singularity contributes $\alpha/(2\pi)$ to the integral $\int c_1$. For this to be an integer when the loop is a generator, we need $\alpha \in 2\pi\mathbb{Z}$ — i.e., the holonomy is the identity. The $1/(2\pi)$ matches the period of the exponential map.

The three properties of Chern forms — globally defined, closed, integer periods — are not three independent miracles. They are three consequences of three pieces of structure: invariance under conjugation (global definedness), the Bianchi identity (closedness), and the relationship between curvature and the holonomy of the connection (integer periods). The Chern–Weil theorem packages them into a single statement.

The fourth and most important property — **independence of the connection** — is the punchline. Two connections on the same bundle give curvature forms differing by a *covariant* expression, and the corresponding Chern forms differ by an *exact* form. So the de Rham cohomology class is the same — it is an invariant of the bundle itself, not of the connection. This is what makes the Chern class a *topological* invariant.

---

# The Definition

Let $E \to M$ be a complex rank-$n$ vector bundle with structure group $U(n)$ (or more generally, a complex vector bundle with a Hermitian metric and a metric-compatible connection). Let $\omega$ be a local connection 1-form in a frame $e_U$ over an open subset $U \subseteq M$, and let $\theta = d\omega + \omega \wedge \omega$ be the local curvature 2-form — an $n \times n$ matrix of 2-forms with values in $\mathfrak{u}(n)$.

The **$r$-th Chern form** of $E$, denoted $c_r(E)$, is the $2r$-form on $M$ defined locally by

$$c_r(E) = \text{coefficient of } \lambda^{n-r} \text{ in } \det\!\left(\lambda I + \frac{i}{2\pi}\theta\right) = \text{(elementary symmetric polynomial of degree } r \text{ in } \frac{i\theta}{2\pi}\text{)}.$$

Equivalently, the **total Chern form** is

$$c(E) := \det\!\left(I + \frac{i}{2\pi}\theta\right) = 1 + c_1(E) + c_2(E) + \cdots + c_n(E),$$

and $c_r(E)$ is the degree-$2r$ component (a form of degree $2r$ on $M$).

The first two Chern forms are:

$$c_1(E) = \frac{i}{2\pi} \mathrm{Tr}(\theta),$$

$$c_2(E) = \frac{1}{8\pi^2}\big[\mathrm{Tr}(\theta) \wedge \mathrm{Tr}(\theta) - \mathrm{Tr}(\theta \wedge \theta)\big].$$

For an $SU(n)$ bundle ($\mathrm{Tr}(\theta) = 0$), these simplify:

$$c_1(E) = 0, \qquad c_2(E) = -\frac{1}{8\pi^2} \mathrm{Tr}(\theta \wedge \theta).$$

The Chern forms have the following fundamental properties (see [[Thm - Chern Forms are Closed and Their Cohomology Class is Independent of Connection]]):

1. Each $c_r(E)$ is a **globally defined real** $2r$-form on $M$ (independent of frame).
2. Each $c_r(E)$ is **closed**: $dc_r(E) = 0$.
3. The de Rham class $[c_r(E)] \in H^{2r}_{\mathrm{dR}}(M; \mathbb{R})$ is **independent of the connection** $\omega$.
4. The periods $\int_z c_r(E) \in \mathbb{Z}$ for every integer $2r$-cycle $z$ on $M$.

The de Rham class $[c_r(E)]$ is the **$r$-th Chern class** of $E$, and the collection of all $c_r$ for $r = 1, \ldots, n$ assembles into the [[Def - Total Chern Class|total Chern class]] $c(E)$.

---

# Categorical / Structural Definition

The Chern forms arise from the **Chern–Weil homomorphism**:

$$\mathrm{CW} : \mathbb{C}[\mathfrak{g}]^G \to H^*_{\mathrm{dR}}(M; \mathbb{R})$$

where $G = U(n)$ and $\mathbb{C}[\mathfrak{g}]^G$ is the algebra of $G$-invariant polynomials on the Lie algebra $\mathfrak{g} = \mathfrak{u}(n)$. The map sends an invariant polynomial $P$ of degree $r$ to the cohomology class $[P(\theta)] \in H^{2r}_{\mathrm{dR}}(M)$ obtained by applying $P$ to the curvature 2-form. The image is independent of the connection (by [[Thm - Chern-Weil Theorem (Statement)|Chern–Weil]]).

For $G = U(n)$, the ring of invariant polynomials is

$$\mathbb{C}[\mathfrak{u}(n)]^{U(n)} = \mathbb{C}[\sigma_1, \sigma_2, \ldots, \sigma_n]$$

where $\sigma_r$ is the $r$-th elementary symmetric polynomial of the eigenvalues. The Chern forms $c_r$ correspond to $\sigma_r(i\theta/2\pi)$. This identifies the ring of Chern classes with the **cohomology of the classifying space** $BU(n)$:

$$H^*(BU(n); \mathbb{Z}) = \mathbb{Z}[c_1, c_2, \ldots, c_n].$$

Every complex vector bundle $E \to M$ has a classifying map $f : M \to BU(n)$, and $c_r(E) = f^* c_r$ where $c_r \in H^{2r}(BU(n); \mathbb{Z})$ is the universal Chern class. This is the most categorical way to state the construction: Chern classes are pullbacks of universal classes from the classifying space.

---

# Relate to Other Fields / Compression

**True name:** the $r$-th Chern form is **the $r$-th elementary symmetric polynomial of curvature eigenvalues, normalised to have integer periods**. The operational picture is: at each point of $M$, the curvature is a 2-form-valued matrix in $\mathfrak{u}(n)$, and we extract the symmetric-polynomial invariants of this matrix (which are conjugation-invariant) and assemble them into a global differential form. The remarkable fact, due to Chern–Weil, is that this construction is *topological* — the resulting cohomology class is connection-independent.

In **gauge theory**, the Chern forms are the basic gauge-invariant local densities built from the curvature ("field strength") $F$ of a Yang–Mills connection. $c_1 = (i/2\pi) \mathrm{Tr}(F)$ vanishes for $SU(n)$ bundles (because $\mathfrak{su}(n)$ matrices are traceless); $c_2 = -(1/8\pi^2) \mathrm{Tr}(F \wedge F)$ is the **topological charge density** whose integral gives the instanton number. The Yang–Mills action $\int \mathrm{Tr}(F \wedge \star F)$ is *not* a topological invariant (it depends on the metric via $\star$), but the *difference* $\int \mathrm{Tr}(F \wedge F) = -8\pi^2 \int c_2$ is topological, leading to the Bogomolnyi bound and self-duality.

In **algebraic geometry**, Chern classes of holomorphic vector bundles on complex manifolds can be computed by the **Chern–Weil formula** using the unique unitary connection compatible with the holomorphic structure (the **Chern connection**), or by purely algebraic methods (sheaf-cohomology, Atiyah classes). On projective varieties, Chern classes are intersection numbers with hyperplane classes.

In **K-theory**, the Chern character $\mathrm{ch}(E) = \mathrm{Tr}(\exp(i\theta/2\pi)) = n + c_1 + \tfrac{1}{2}(c_1^2 - 2c_2) + \cdots$ is a ring homomorphism from $K^0(M) \otimes \mathbb{Q}$ to $H^{\mathrm{even}}(M; \mathbb{Q})$, providing the comparison between K-theory and rational cohomology.

In **physics**, every integer-valued topological invariant in gauge theory and condensed matter is a Chern number: TKNN integers in the integer quantum Hall effect, instanton numbers in QCD, Chern–Simons levels, and the topological invariants of topological insulators.

---

# Examples / Corollaries

**Example: trivial bundle.** For the trivial bundle $E = M \times \mathbb{C}^n$ with the flat connection $\omega = 0$, the curvature is $\theta = 0$, so all Chern forms vanish: $c_r = 0$ for $r \geq 1$. The Chern *classes* $[c_r] \in H^{2r}_{\mathrm{dR}}(M)$ also vanish. This is consistent with the fact that trivial bundles have no topological obstructions.

**Example: tautological line bundle on $\mathbb{CP}^1$.** Let $L = \mathcal{O}(-1)$ be the tautological line bundle on $\mathbb{CP}^1 = S^2$ — fibre over $[z_0 : z_1]$ is the line $\{(\lambda z_0, \lambda z_1)\} \subset \mathbb{C}^2$. The **Fubini–Study connection** has curvature 2-form $\theta = -i \omega_{\mathrm{FS}}$ where $\omega_{\mathrm{FS}}$ is the Fubini–Study Kähler form. Then $c_1(L) = (i/2\pi)\mathrm{Tr}(\theta) = (1/2\pi) \omega_{\mathrm{FS}}$, and $\int_{\mathbb{CP}^1} c_1(L) = -1$. See [[Ex - The Chern Number of the Hopf Line Bundle over CP^1]].

**Example: SU(2) instanton on $\mathbb{R}^4$.** For the BPST instanton with curvature 2-form $F$ (an $\mathfrak{su}(2)$-valued 2-form), the second Chern form is $c_2 = -(1/8\pi^2) \mathrm{Tr}(F \wedge F)$. The integral $\int_{\mathbb{R}^4} c_2 = -1$ (or $+1$ depending on orientation), counting the instanton number. See [[Ex - Winding Number of the BPST Instanton is 1]].

**Example: tangent bundle of $\mathbb{CP}^n$.** For the holomorphic tangent bundle $T\mathbb{CP}^n$, the **Euler sequence** $0 \to \mathcal{O} \to \mathcal{O}(1)^{\oplus(n+1)} \to T\mathbb{CP}^n \to 0$ gives, via the Whitney sum formula and the multiplicativity of total Chern class,

$$c(T\mathbb{CP}^n) = (1 + h)^{n+1}/1 = (1 + h)^{n+1}$$

where $h = c_1(\mathcal{O}(1)) \in H^2(\mathbb{CP}^n; \mathbb{Z})$ is the hyperplane class. So $c_r(T\mathbb{CP}^n) = \binom{n+1}{r} h^r$. In particular $c_n(T\mathbb{CP}^n) = (n+1) h^n$ and $\int_{\mathbb{CP}^n} c_n = n + 1$, which is the Euler characteristic of $\mathbb{CP}^n$ (one for each cell in dimensions $0, 2, 4, \ldots, 2n$).

**Example: complex line bundle, $c_1$ formula.** For a complex line bundle $L \to M$ with $U(1)$ connection $\omega = -iA$ (so $A$ is a real-valued 1-form, the "vector potential"), the curvature is $\theta = -iF$ with $F = dA$, and $c_1(L) = (i/2\pi)\mathrm{Tr}(\theta) = (1/2\pi) F$. So **$c_1 = F/(2\pi)$** for a line bundle — the formula universally used in gauge theory.

**Is NOT an instance: a polynomial that is not invariant.** The polynomial $P(A) = A_{11}$ (the upper-left entry of the matrix) is *not* invariant under conjugation, so the form $P(\theta)$ is not globally defined: it depends on the frame. Different frames give different "upper-left entries", differing by gauge transformations. Only invariant polynomials give globally defined forms.

**Corollary: $c(E \oplus F) = c(E) \cdot c(F)$ (Whitney sum formula).** For two complex vector bundles $E, F$ over $M$, the total Chern class of their direct sum equals the product of total Chern classes. Equivalently, $c_r(E \oplus F) = \sum_{i + j = r} c_i(E) \cdot c_j(F)$. The proof uses block-diagonal connections: $\omega_{E \oplus F} = \mathrm{diag}(\omega_E, \omega_F)$, and the determinant of a block-diagonal matrix is the product of block determinants.

**Corollary: $c_r(\bar E) = (-1)^r c_r(E)$ (complex conjugate bundle).** The complex conjugate bundle $\bar E$ has the conjugate connection $\bar\omega = -\omega^T$ (transpose); its curvature is $\bar\theta = -\theta^T$. Plugging into $\det(I + (i/2\pi)\bar\theta) = \det(I - (i/2\pi)\theta^T) = \det(I - (i/2\pi)\theta)$, we get the polynomial in $-\theta$, which differs from $c(E)$ by signs: $c_r(\bar E) = (-1)^r c_r(E)$.

**Corollary: $c_r(E^*) = (-1)^r c_r(E)$ (dual bundle).** Same calculation as for the conjugate, since the dual of a complex vector bundle has connection $-\omega^T$ in the dual frame.

**Calibration check.** If you understand the definition you should be able to: (i) verify that $c_1 = (i/2\pi)\mathrm{Tr}(\theta)$ from the determinant expansion; (ii) compute $c_2$ for a 2x2 matrix of 2-forms; (iii) confirm that for $SU(n)$ bundles, $c_1 = 0$ and $c_2 = -(1/8\pi^2)\mathrm{Tr}(\theta \wedge \theta)$; (iv) verify $c(E) = c(\bar E)$ if $E = \bar E$ (real structure).

---

# Unlocked by This

> [!tip] Chern Character *(from K-theory)*
> The **Chern character** of a complex vector bundle $E$ is $\mathrm{ch}(E) = \mathrm{Tr}(\exp(i\theta/2\pi)) = n + c_1 + \tfrac{1}{2}(c_1^2 - 2c_2) + \tfrac{1}{6}(c_1^3 - 3c_1 c_2 + 3c_3) + \cdots$, a sum of forms of even degree expressed as polynomials in Chern forms. Unlike the total Chern class (which multiplies under direct sum), the Chern character is *additive*: $\mathrm{ch}(E \oplus F) = \mathrm{ch}(E) + \mathrm{ch}(F)$ and *multiplicative under tensor product*: $\mathrm{ch}(E \otimes F) = \mathrm{ch}(E) \cdot \mathrm{ch}(F)$. This makes $\mathrm{ch}$ a ring homomorphism from **K-theory** $K^0(M) \otimes \mathbb{Q}$ to rational cohomology $H^{\mathrm{even}}(M; \mathbb{Q})$ — the bridge between K-theory and cohomology that underlies the **Atiyah–Singer index theorem**.

> [!tip] Hirzebruch–Riemann–Roch *(from Algebraic Geometry)*
> For a holomorphic vector bundle $E$ on a compact complex manifold $X$ of complex dimension $n$, the **Hirzebruch–Riemann–Roch theorem** states
> $$\chi(X, E) = \int_X \mathrm{ch}(E) \cdot \mathrm{Td}(X),$$
> where $\chi(X, E) = \sum_k (-1)^k \dim H^k(X, E)$ is the holomorphic Euler characteristic and $\mathrm{Td}(X)$ is the **Todd class** of $X$, a specific polynomial in the Chern classes of $TX$. This generalises the classical Riemann–Roch theorem for curves and is the foundational result of intersection theory on complex varieties.
