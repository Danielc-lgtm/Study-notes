---
type: remark
subject: spectral-geometry
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
  - "Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure"
  - "Def - Heat Kernel and Heat Semigroup"
tags: [paper, brownian-loops, spectral-geometry, cusps]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §5.2 — why the compact determinant construction breaks on cusped surfaces, and the Melrose fix"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a **finite-area but non-compact** hyperbolic surface: geometrically finite, $\operatorname{Area}(X) < \infty$, with $n_C \ge 1$ **cusps** (finitely many puncture-shaped ends of infinite Euclidean but finite hyperbolic diameter).
- $\Delta_X$ — the positive Laplace–Beltrami operator on $L^2(X)$; on a cusped surface it is essentially self-adjoint but does **not** have purely discrete spectrum.
- $\lambda_j$ — discrete $L^2$-eigenvalues of $\Delta_X$ (finitely many, or countable with $\lambda_j \to \infty$); $\lambda_0 = 0$ is present since $\operatorname{Area}(X) < \infty$ makes the constants $L^2$.
- $E_j(z, s)$ — Eisenstein series (one per cusp), the *generalised* eigenfunctions of $\Delta_X$; solve $\Delta_X E_j = s(1 - s) E_j$ but are not in $L^2(X)$.
- $p_X(t, z, w)$ — the heat kernel of $\Delta_X$; on a cusped surface, its diagonal $p_X(t, z, z)$ is a *bounded* function of $z$ for each fixed $t > 0$, but $\int_X p_X(t, z, z)\,d\!\operatorname{vol}$ diverges (see Step 3 below).
- $\bar X$ — the Melrose compactification: $X$ with a smooth boundary circle added at each cusp (the "circle at infinity").
- $x : \bar X \to [0, \infty)$ — a smooth **boundary defining function**: $x \equiv 0$ on the added boundary, $x > 0$ on the interior, and $dx \ne 0$ on the boundary (first-order vanishing).
- ${}^0\!\!\int_X f\,d\!\operatorname{vol} := \operatorname{FP}_{z = 0}\int_X x^z f\,d\!\operatorname{vol}$ — the **Melrose renormalised integral** (Riesz form): for $f$ with a controlled expansion at the cusps, $\int_X x^z f\,d\!\operatorname{vol}$ converges for $\operatorname{Re} z$ large, continues meromorphically in $z$, and we take the finite part at $z = 0$.
- ${}^0\!\operatorname{Tr}(e^{-t\Delta_X}) := {}^0\!\!\int_X p_X(t, z, z)\,d\!\operatorname{vol}(z)$ — the **renormalised (0-)trace**.
- $P$ — the orthogonal projection onto the finite-dimensional $L^2$-null space of $\Delta_X$ (which contains at least the constant functions).
- $\zeta^0_X(s) := \Gamma(s)^{-1}\int_0^\infty t^{s - 1}\big({}^0\!\operatorname{Tr}(e^{-t\Delta_X}) - P\big)\,dt$ — the renormalised spectral zeta.
- $\det_0\Delta_X := e^{-(\zeta^0_X)'(0)}$ — the **0-determinant**.

> [!recall]- Hyperbolic surface with cusps (finite-area, non-compact)
> **Formally:** $X = \Gamma\backslash\mathbb H^2$ where $\Gamma \subset \mathrm{PSL}(2, \mathbb R)$ is a geometrically finite, torsion-free Fuchsian group with $\operatorname{covol}(\Gamma) < \infty$ but no compact fundamental domain. Each *cusp* is a $\Gamma$-conjugacy class of parabolic fixed points on the ideal boundary $\partial\mathbb H^2 \cup \{\infty\}$; each admits a coordinate neighbourhood of the form $\{z \in \mathbb H^2 : \operatorname{Im} z > c\}/\langle z \mapsto z + 1\rangle$, a hyperbolic "cusp region" (parabolic quotient) of finite hyperbolic area $1/c$ but infinite Euclidean shape.
> **In words:** a hyperbolic surface with finitely many "puncture-shaped ends" — each end is topologically a punctured disc, geometrically a shrinking horn narrowing to a point at infinity but with only finite total volume. The most famous example is the **modular surface** $\mathrm{PSL}(2, \mathbb Z)\backslash\mathbb H^2$: one cusp, area $\pi/3$, non-compact.
> **Concretely:** the modular surface is a "triangle with two ideal vertices identified", area $\pi/3 \approx 1.047$; the geodesic $\{iy : y \ge 1\}$ heads off into the single cusp and never comes back within finite hyperbolic distance, even though its "height" grows without bound. Full detail: [[Def - Fuchsian Group and the Hyperbolic Quotient Surface]].

> [!recall]- Trace-class operator and Lidskii's theorem
> **Formally:** a bounded operator $T$ on a separable Hilbert space $\mathcal H$ is **trace class** if $\sum_j \langle |T| e_j, e_j\rangle < \infty$ for some (equivalently every) orthonormal basis $(e_j)$; equivalently, its singular values are summable. For $T$ trace class, its *trace* is $\operatorname{Tr} T := \sum_j \langle T e_j, e_j\rangle$; Lidskii's theorem asserts $\operatorname{Tr} T = \sum_k \lambda_k(T)$ (counted with algebraic multiplicity). If $T$ has a continuous integral kernel $K(x, y)$ on a compact manifold, $\operatorname{Tr} T = \int K(x, x)\,d\!\operatorname{vol}(x)$.
> **In words:** trace class is the class of operators for which the "sum of eigenvalues" makes sense. On a closed manifold, the heat semigroup $e^{-t\Delta}$ is trace class for every $t > 0$ (rapid decay of Weyl-count eigenvalues), and $\operatorname{Tr}(e^{-t\Delta}) = \sum_j e^{-t\lambda_j} = \int p(t, z, z)\,d\!\operatorname{vol}$.
> **Concretely:** on the flat torus $T^2 = \mathbb R^2/(2\pi\mathbb Z)^2$, the Laplacian's eigenvalues are $\{n_1^2 + n_2^2 : (n_1, n_2) \in \mathbb Z^2\}$, so $\operatorname{Tr}(e^{-t\Delta}) = \sum_{(n_1, n_2)}e^{-t(n_1^2 + n_2^2)} = \theta(t)^2$ (a Jacobi theta), summable for every $t > 0$; in particular trace class.

> [!recall]- Zeta-regularised determinant (closed / discrete-spectrum case)
> **Formally:** for a positive self-adjoint operator $A$ on $L^2$ with purely discrete spectrum $0 < \lambda_1 \le \lambda_2 \le \cdots \to \infty$ and $e^{-tA}$ trace class for every $t > 0$: define $\zeta_A(s) := \sum_j \lambda_j^{-s} = \Gamma(s)^{-1}\int_0^\infty t^{s - 1}(\operatorname{Tr}\, e^{-tA} - 0\text{-mode})\,dt$; this continues meromorphically to $\mathbb C$, is regular at $s = 0$, and $\det_\zeta A := e^{-\zeta_A'(0)}$.
> **In words:** the "product of all eigenvalues" $\prod \lambda_j$ is formally infinite; the zeta-regularised determinant is the finite canonical stand-in defined by analytic continuation of the log-derivative of the spectral zeta at $s = 0$.
> **Concretely:** for $A$ with three eigenvalues $1, 2, 3$: $\zeta_A(s) = 1 + 2^{-s} + 3^{-s}$, $-\zeta_A'(0) = \log 6$, $\det_\zeta A = 6 = 1\cdot 2\cdot 3$ — the ordinary product. Full detail: [[Def - Zeta-Regularised Determinant of the Laplacian]].

> [!recall]- Continuous spectrum and generalised eigenfunctions
> **Formally:** the spectrum $\sigma(A) \subset \mathbb R$ of a self-adjoint $A$ decomposes as $\sigma_{\mathrm{disc}} \cup \sigma_{\mathrm{ess}}$: $\lambda \in \sigma_{\mathrm{disc}}$ iff there is an $L^2$-eigenfunction $f$ with $Af = \lambda f$; $\lambda \in \sigma_{\mathrm{ess}}$ (the essential/continuous part) iff no $L^2$-eigenfunction exists but $\lambda$ is a limit of approximate eigenvalues (Weyl criterion). A *generalised eigenfunction* at $\lambda \in \sigma_{\mathrm{ess}}$ is a *tempered* (polynomially-bounded, not $L^2$) solution of $Af = \lambda f$.
> **In words:** discrete spectrum: bound states, $L^2$-eigenfunctions, isolated $\lambda$'s. Continuous spectrum: scattering states, non-$L^2$ but bounded eigenfunctions, $\lambda$'s form a continuum.
> **Concretely:** for $A = -d^2/dx^2$ on $L^2(\mathbb R)$: no discrete spectrum (a plane wave $e^{ikx}$ is bounded but not $L^2$); the whole $[0, \infty)$ is continuous spectrum, and the plane waves $e^{ikx}$ are the generalised eigenfunctions at $\lambda = k^2$. On $L^2([0, 1])$ with Dirichlet BCs, only discrete spectrum $\{n^2\pi^2\}$.

---

# Claim / Identity

> **Claim (compact determinant construction breaks in the cusped case).**
>
> **(1) Break.** Let $X$ be a finite-area, non-compact hyperbolic surface with $n_C \ge 1$ cusps. Then:
> - $\Delta_X$ has continuous spectrum $[1/4, \infty)$ with multiplicity $n_C$, whose generalised eigenfunctions are the Eisenstein series $E_j(z, s)$ (one per cusp).
> - The heat semigroup $e^{-t\Delta_X}$ is **not** trace class for any $t > 0$, and $\int_X p_X(t, z, z)\,d\!\operatorname{vol}(z) = +\infty$.
> - Consequently the compact-case spectral zeta $\sum_j \lambda_j^{-s}$ has no discrete series to sum over, and the compact-case identity $\zeta_A(s) = \Gamma(s)^{-1}\int t^{s-1}(\operatorname{Tr} e^{-tA} - 1)\,dt$ is meaningless.
>
> **(2) Fix.** Let $\bar X$ be the Melrose compactification (adding one boundary circle at each cusp) and $x$ a boundary defining function. The **renormalised integral** ${}^0\!\!\int_X f := \operatorname{FP}_{z = 0}\int_X x^z f\,d\!\operatorname{vol}$ turns the divergent trace $\int_X p_X(t, z, z)\,d\!\operatorname{vol}$ into the finite **0-trace** ${}^0\!\operatorname{Tr}(e^{-t\Delta_X}) := {}^0\!\!\int_X p_X(t, z, z)\,d\!\operatorname{vol}$. Its Mellin transform (with the null-space projection $P$ subtracted for large-$t$ convergence) gives $\zeta^0_X(s) := \Gamma(s)^{-1}\int_0^\infty t^{s-1}({}^0\!\operatorname{Tr}(e^{-t\Delta_X}) - P)\,dt$; this continues meromorphically to $\mathbb C$, is regular at $s = 0$, and the **0-determinant** is $\det_0\Delta_X := e^{-(\zeta^0_X)'(0)}$.
>
> **(3) Reduction.** On a closed surface (no cusps, $x \equiv 1$, no boundary to renormalise against), ${}^0\!\!\int_X = \int_X$, ${}^0\!\operatorname{Tr} = \operatorname{Tr}$, $\zeta^0_X = \zeta_X$, and $\det_0\Delta_X = \det_\zeta\Delta_X$: the 0-determinant reduces to the ordinary zeta-regularised determinant of §5.1.

---

# In One Line

Cusps put Eisenstein series into the spectrum, making $\Delta_X$'s spectrum continuous $[1/4, \infty)$ (in addition to any discrete $L^2$-eigenvalues); no discrete list of eigenvalues means no compact-case spectral zeta, no trace-class heat semigroup, and no compact-case determinant. Melrose's fix — compactify to $\bar X$, multiply the integrand by $x^z$ (with $x$ vanishing at the cusp boundary), analytically continue in $z$, take the finite part at $z = 0$ — extracts a finite renormalised trace that plugs into the same $\zeta'(0)$ machine, defining $\det_0\Delta_X$; on a closed surface it collapses back to $\det_\zeta\Delta_X$.

---

# Why It's True

**Mechanism (one sentence).** *Cusps supply parabolic-fixed-point Eisenstein series (a continuous family of eigenfunctions, non-$L^2$) that populate $[1/4, \infty)$ as continuous spectrum; a continuous spectrum has no eigenvalue list, so $\operatorname{Tr}(e^{-t\Delta_X})$ diverges — Melrose's renormalised integral against a boundary defining function $x^z$ subtracts off the divergent contribution and keeps only the finite spectral content, exactly what the compact-case machine needs to produce a determinant.*

The compact-case story of §5.1 relies on two ingredients: (a) a discrete list of eigenvalues to feed into $\sum_j \lambda_j^{-s}$; (b) a trace-class heat semigroup so that $\operatorname{Tr}(e^{-t\Delta_X}) = \sum_j e^{-t\lambda_j}$. Both ingredients disappear when cusps are present. What survives is the *pointwise* heat kernel $p_X(t, z, z)$ — a bounded function of $z \in X$ for each fixed $t > 0$ — but its integral over $X$ diverges because the cusp neck lets the Eisenstein-series contribution to the diagonal make the integrand non-integrable at the cusp (see the Derivation for the explicit picture).

Melrose's fix is a *renormalisation of the divergent integral*, not a modification of the operator $\Delta_X$. Compactify $X$ to $\bar X$ by adding a circle at infinity at each cusp, take a smooth function $x$ that vanishes to first order on the added boundary, and multiply the integrand by $x^z$: for large enough $\operatorname{Re} z$ this kills the cusp divergence and the integral converges; analytic continuation in $z$ picks up the "finite part" at $z = 0$, in effect *subtracting off* the divergent piece and keeping only the regular remainder. What remains — the 0-trace — is a finite function of $t$ with a controlled short-time expansion; it plays the role of $\operatorname{Tr}(e^{-t\Delta_X})$ in the compact-case recipe, producing a well-defined 0-determinant $\det_0\Delta_X$. On a closed surface, $x \equiv 1$, no analytic continuation is needed, and the whole construction collapses back to the compact-case one — that is the "reduction" claim.

---

# Derivation

> [!note]- Gap-free derivation
>
> **Step 1 — how cusps put Eisenstein series into the spectrum.** Near each cusp of $X$ there is a coordinate $(u, y)$ with $u \in \mathbb R/\mathbb Z$ and $y > c > 0$ (a chart on the parabolic quotient $\{\operatorname{Im} z > c\}/\langle z \mapsto z + 1\rangle$), in which the hyperbolic metric is $ds^2 = (du^2 + dy^2)/y^2$ and the Laplacian is $\Delta_X = -y^2(\partial_u^2 + \partial_y^2)$. Separation of variables in the cusp with $u$-periodic boundary gives *tempered* (bounded, polynomially growing) solutions $y^s$ and $y^{1-s}$ of $\Delta_X f = s(1-s)f$ in the constant-$u$ mode; these are not in $L^2(X)$ (they neither decay at $y \to \infty$ nor blow up), but they are bounded and satisfy the eigenequation. Symmetrising each cusp gives, for every $s \in \frac12 + i\mathbb R$, one *Eisenstein series* $E_j(z, s)$ per cusp (obtained by averaging the cusp-adapted $y^s$ over cosets of the parabolic subgroup): a generalised eigenfunction with $\Delta_X E_j = s(1-s)E_j$ and eigenvalue $\lambda = s(1-s) \in [1/4, \infty)$ when $s = 1/2 + it$, $t \in \mathbb R$. Standard scattering-theory arguments (Selberg's spectral resolution) then show that $[1/4, \infty)$ is the continuous spectrum of $\Delta_X$, with multiplicity equal to $n_C$ (one band per cusp).
>
> **Step 2 — heat semigroup is not trace class.** The spectral resolution of $\Delta_X$ on $L^2(X)$ has two pieces: a discrete part (finitely many, or $\lambda_j \to \infty$, with $L^2$-eigenfunctions $\phi_j$) and a continuous part on $[1/4, \infty)$ (parametrised by $s = 1/2 + it$, $t \in \mathbb R$, with Eisenstein series $E_j(z, 1/2 + it)$ as generalised eigenfunctions). Correspondingly the heat kernel on the diagonal decomposes as
> $$p_X(t, z, z) \;=\; \underbrace{\sum_j e^{-t\lambda_j}|\phi_j(z)|^2}_{\text{discrete}} \;+\; \underbrace{\frac{1}{4\pi}\sum_{j = 1}^{n_C}\int_{-\infty}^\infty e^{-t(1/4 + r^2)}|E_j(z, 1/2 + ir)|^2\,dr}_{\text{Eisenstein continuum}}.$$
> Integrating over $z \in X$: the discrete piece integrates against $\int |\phi_j|^2\,d\!\operatorname{vol} = 1$ to give $\sum_j e^{-t\lambda_j}$ (finite for each $t > 0$ by Weyl's law on the discrete part). The continuous piece involves $|E_j(z, 1/2 + ir)|^2$, which is *not* integrable in $z$: as $z$ heads out the $j$-th cusp along $y \to \infty$, $|E_j(z, s)|^2 \sim y^{2\operatorname{Re}s}$ up to a bounded oscillating term, and $\int_c^\infty y^{2\operatorname{Re}s}\cdot dy/y^2$ diverges at $\operatorname{Re}s = 1/2$ (the value $2\operatorname{Re}s - 2 = -1$ makes $\int^\infty dy/y = +\infty$). So the Eisenstein-continuum contribution to $\int_X p_X(t, z, z)\,d\!\operatorname{vol}$ diverges. Since $p_X(t, z, z) > 0$ everywhere, $\int_X p_X(t, z, z)\,d\!\operatorname{vol} = +\infty$ for every $t > 0$, and $e^{-t\Delta_X}$ is not trace class.
>
> *Note.* The divergence is not due to $X$ having infinite volume — a cusp has finite volume $1/c$. It is a purely *spectral* divergence: the Eisenstein modes carry non-integrable mass to the cusp.
>
> **Step 3 — compact-case zeta recipe is meaningless.** The compact-case definition $\zeta_A(s) := \sum_j \lambda_j^{-s}$ has no continuous-spectrum analogue with a finite sum: one would want to include the continuous $[1/4, \infty)$ modes, but each $\lambda \in [1/4, \infty)$ has an $n_C$-fold multiplicity in the generalised sense, and there is no discrete measure to sum against. Equivalently, the Mellin-transform version $\zeta_A(s) = \Gamma(s)^{-1}\int_0^\infty t^{s-1}(\operatorname{Tr} e^{-tA} - 1)\,dt$ fails because $\operatorname{Tr} e^{-tA}$ is undefined (Step 2). The compact-case construction of $\det_\zeta\Delta_X$ therefore has no starting point on a cusped surface.
>
> **Step 4 — the Melrose renormalised integral.** Compactify $X$ to $\bar X$ by adding one boundary circle at each cusp; $\bar X$ is a smooth compact manifold-with-boundary. Choose a smooth $x : \bar X \to [0, \infty)$ with $x^{-1}(0)$ exactly the added boundary and $dx \ne 0$ there — a *boundary defining function*. Near a cusp, $x = 1/y$ (or any smooth first-order-vanishing multiple) is the standard choice; then $x^z = y^{-z}$ near the cusp, so $y^{2\operatorname{Re}s}\cdot y^{-z}\cdot dy/y^2 = y^{2\operatorname{Re}s - z - 2}\,dy$ integrates on $y \in [c, \infty)$ precisely when $\operatorname{Re}z > 2\operatorname{Re}s - 1$. So for a function $f$ with a *controlled* expansion at each cusp (finite-order polyhomogeneous), the integral $\int_X x^z f\,d\!\operatorname{vol}$ converges for $\operatorname{Re}z$ large, is a meromorphic function of $z$ (poles determined by the expansion coefficients), and its **finite part** at $z = 0$ — the constant term of the Laurent expansion — is by definition the **renormalised integral**:
> $${}^0\!\!\int_X f\,d\!\operatorname{vol} \;:=\; \operatorname{FP}_{z = 0}\int_X x^z f\,d\!\operatorname{vol}. \tag{Riesz form}$$
> An equivalent Hadamard form takes $\lim_{\epsilon \to 0^+}[\int_{x \ge \epsilon} f\,d\!\operatorname{vol} - (\text{divergent-in-}\epsilon\text{-part})]$; the two agree for the polyhomogeneous $f$'s arising here.
>
> **Step 5 — the renormalised trace and zeta.** The heat-kernel diagonal $p_X(t, z, z)$ has a controlled asymptotic expansion in the cusp coordinates as $y \to \infty$, so ${}^0\!\!\int_X p_X(t, z, z)\,d\!\operatorname{vol}$ is well-defined and finite for every $t > 0$. Call it the **0-trace**:
> $${}^0\!\operatorname{Tr}(e^{-t\Delta_X}) \;:=\; {}^0\!\!\int_X p_X(t, z, z)\,d\!\operatorname{vol}(z).$$
> The 0-trace has: (a) exponential decay as $t \to \infty$ down to the rank of the $L^2$-null space (constants, plus any other discrete zero modes); (b) a short-time asymptotic ${}^0\!\operatorname{Tr}(e^{-t\Delta_X}) \sim a_{-1}/t + a_0 + a_{0, \log}\log t + \cdots$ (the $\log t$ terms come from the cusps). Subtract the projection $P$ onto the $L^2$-null space so the large-$t$ integrand decays exponentially, and take the Mellin transform:
> $$\zeta^0_X(s) \;:=\; \frac{1}{\Gamma(s)}\int_0^\infty t^{s - 1}\big({}^0\!\operatorname{Tr}(e^{-t\Delta_X}) - P\big)\,dt.$$
> The short-time expansion continues $\zeta^0_X$ meromorphically to $\mathbb C$; the $1/\Gamma(s)$ prefactor kills the potential pole at $s = 0$, so $\zeta^0_X$ is regular at $s = 0$ and its derivative $(\zeta^0_X)'(0)$ is a finite number. The **0-determinant** is
> $$\det_0\Delta_X \;:=\; e^{-(\zeta^0_X)'(0)}. \tag{62 of the paper}$$
>
> **Step 6 — reduction to the compact case.** On a closed surface there is no boundary to compactify against: $\bar X = X$, $x \equiv 1$, and $x^z \equiv 1$ regardless of $z$. Therefore ${}^0\!\!\int_X f = \int_X f$, ${}^0\!\operatorname{Tr}(e^{-t\Delta_X}) = \operatorname{Tr}(e^{-t\Delta_X}) = \sum_j e^{-t\lambda_j}$, and $\zeta^0_X = \zeta_X$; consequently $\det_0\Delta_X = \det_\zeta\Delta_X$. So (2) is a strict extension of the compact-case construction of §5.1: same recipe, with the divergent trace replaced by its Melrose renormalisation whenever a cusp requires it. $\blacksquare$

---

# Where the paper uses this

Motivates the entire §5.2 construction: the [[Thm - Borthwick-Judge-Perry Determinant Formula|Borthwick–Judge–Perry formula (Theorem 5.5)]] takes $\det_0\Delta_X$ as its object of study, and [[Thm - Determinant via Loop Measure, Finite-Area Case|Theorem 5.7]] plugs the [[Thm - Selberg Zeta Identity for the Total Loop Mass|Selberg zeta identity]] into it to recover the finite-area analogue of the compact-case identity — but *only* the 0-determinant $\det_0\Delta_X$ makes sense on cusped $X$, so the whole finite-area statement depends on this remark's construction. Also underlies [[Remark - The Infinite-Area Determinant Case|Remark 5.8]] (infinite-area case), where $\det_0\Delta_X$ is again the correct object because the naive $\det_\zeta$ still fails. Read in context: [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.2]].
