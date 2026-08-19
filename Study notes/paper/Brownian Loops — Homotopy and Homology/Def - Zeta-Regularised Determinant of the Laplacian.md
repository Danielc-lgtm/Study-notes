---
type: definition
subject: analysis
prereqs:
  - "Def - Heat Kernel and Heat Semigroup"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
tags: [analysis, spectral-geometry, zeta-functions, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$X$ a closed hyperbolic surface; $\Delta_X$ its positive [[Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure|Laplace–Beltrami operator]] with discrete spectrum $0=\lambda_0<\lambda_1\le\lambda_2\le\cdots$; $\operatorname{Tr}(e^{-t\Delta_X})=\sum_{j\ge0}e^{-t\lambda_j}$ the heat trace; $\Gamma(s)$ the Gamma function; $\zeta_R$ the Riemann zeta function; $\chi(X)=2-2g$ the Euler characteristic. $s\in\mathbb{C}$.

---

# Axiom Motivation

The "determinant of the Laplacian" $\det\Delta_X$ ought to be the product of its eigenvalues $\prod_{j\ge1}\lambda_j$ (dropping the zero mode) — a natural quantity in physics (one-loop partition functions) and geometry (analytic torsion). But that product diverges: by Weyl's law $\lambda_j\sim 4\pi j/\operatorname{Area}(X)$, so $\log\det=\sum_j\log\lambda_j$ has terms growing like $\log j$ and diverges. The eigenvalues are too many and too large. **Zeta regularisation** is the standard cure: instead of summing $\log\lambda_j$ directly, encode the eigenvalues in a **spectral zeta function** $\zeta_X(s)=\sum_j\lambda_j^{-s}$, which converges for $\operatorname{Re}s$ large, continue it analytically to $s=0$, and *define* $\log\det$ by the value of its derivative there. This is finite and canonical.

The trick that makes the continuation work — and the reason this belongs in a paper about heat/loops — is the **Mellin transform**: $\lambda^{-s}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}e^{-t\lambda}\,dt$, so $\zeta_X(s)$ is a Mellin transform of the heat trace. The heat trace's *small-$t$ asymptotics* (which are local geometry — area, Euler characteristic) control the poles of $\zeta_X$, and the $1/\Gamma(s)$ factor's zero at $s=0$ makes $\zeta_X$ regular there. So $\det_\zeta\Delta$ is read off from heat-kernel data — and the heat trace $\operatorname{Tr}(e^{-t\Delta_X})=\int_X p(t,x,x)\,d\operatorname{vol}_g$ is built from Brownian loops (paths returning to their start). That is the door through which the loop measure enters: $-\log\det_\zeta\Delta$ is a regularised total loop mass.

> [!recall]- Mellin transform and meromorphic continuation
> **Formally:** for a function $f:(0,\infty)\to\mathbb{C}$ with polynomial-growth control, the *Mellin transform* is $(\mathcal{M}f)(s) := \int_0^\infty t^{s-1}f(t)\,dt$; it converges in a vertical strip $\operatorname{Re}s\in(a,b)$ determined by the small-$t$ and large-$t$ asymptotics of $f$; analytic continuation extends $\mathcal{M}f$ to a *meromorphic* function on $\mathbb{C}$ whose poles record the coefficients of the $t$-asymptotic expansions.
> **In words:** an integral transform that turns a function of positive real $t$ into a function of a complex variable $s$; it converges in a strip in the complex plane; the trick is that even though the integral only makes sense in the strip, the resulting function of $s$ extends naturally to a well-defined complex-analytic function on ALL of $\mathbb{C}$ (except a few isolated poles), simply by requiring analyticity. This "extension to a bigger domain" is called *meromorphic continuation*.
> **Concretely:** the Gamma function $\Gamma(s)$ is $\mathcal{M}f$ for $f(t) = e^{-t}$, and while $\int_0^\infty t^{s-1}e^{-t}\,dt$ only converges for $\operatorname{Re}s > 0$, $\Gamma(s)$ extends meromorphically to $\mathbb{C}$ with simple poles at $s = 0, -1, -2, \ldots$. Analogously, the Riemann zeta $\zeta_R(s)$ is defined initially as $\sum n^{-s}$ for $\operatorname{Re}s > 1$, but extends meromorphically to $\mathbb{C}$ with a single simple pole at $s = 1$.

---

# The Definition

> **Definition (spectral zeta function; zeta-regularised determinant).** For a closed hyperbolic surface $X$, the **spectral zeta function** is
> $$\zeta_X(s):=\sum_{j=1}^\infty\lambda_j^{-s}=\frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}\big(\operatorname{Tr}(e^{-t\Delta_X})-1\big)\,dt,\qquad\operatorname{Re}(s)>1,$$
> where the "$-1$" removes the zero eigenvalue ($\dim\ker\Delta_X=1$, the constants). Using the short-time heat-trace asymptotic $\operatorname{Tr}(e^{-t\Delta_X})-1\sim\frac{\operatorname{Area}(X)}{4\pi t}+\big(\frac{\chi(X)}{6}-1\big)+O(t)$ as $t\downarrow0$, $\zeta_X$ continues meromorphically to $\mathbb{C}$, is **analytic at $s=0$** (the $1/\Gamma(s)$ zero cancels the potential pole), with $\zeta_X(0)=\frac{\chi(X)}{6}-1$. The **zeta-regularised determinant** is
> $$\log\det_\zeta\Delta_X:=-\zeta_X'(0),$$
> the Ray–Singer definition (formally $-\zeta_X'(0)=\sum_{j\ge1}\log\lambda_j$, since $\frac{d}{ds}\lambda^{-s}\big|_{s=0}=-\log\lambda$).

> **Definition (renormalised determinant, cusped case — sketch).** On a cusped surface (finite-area but with punctures — infinite-length narrow ends), the naive heat trace $\int_X p(t,z,z)\,d\operatorname{vol}_g$ diverges — but *not* because the cusp has large volume. A model cusp $\{(x,y):0\le x<1,\,y>c\}/\langle z\mapsto z+1\rangle$ has $\operatorname{vol} = \int_c^\infty y^{-2}\,dy \cdot 1 = 1/c$, which is **finite**. What diverges is the *spectral* sum: on a compact surface, $p(t,z,z) = \sum_j e^{-t\lambda_j}|\phi_j(z)|^2$ collapses to a trace-class heat trace $\sum_j e^{-t\lambda_j} < \infty$; on a cusped surface the continuous spectrum $[1/4,\infty)$ contributes an additional $\int_{1/4}^\infty e^{-t\lambda}\,dN(\lambda)$-type term coming from the Eisenstein series (recalled below), and *that* piece diverges (the "spectral density" $dN/d\lambda$ built from the Eisenstein series does not decay fast enough to make the integral finite). Equivalently, $e^{-t\Delta_X}$ fails to be trace-class as an operator on $L^2(X)$.
>
> *Concrete check on the cusp itself.* The finite-volume computation is the sanity check above; the *pointwise* density $p(t,z,z)$ on the cusp does not decay as $y\to\infty$ (it stays $\sim 1/(4\pi t)$ locally, since the local geometry near $y=\infty$ looks Euclidean at each point), but this is compatible with finite volume — integrating a bounded function against a finite measure gives a finite answer. The divergence is invisible from the volume side and appears only in the spectral decomposition.
>
> The fix is a **renormalised ($0$-)trace** ${}^{0}\!\operatorname{Tr}(e^{-t\Delta_X}) = {}^{0}\!\int_X p(t,z,z)\,d\operatorname{vol}_g$: cut the cusps at height $Y$, subtract the divergent-in-$Y$ part of the truncated integral, and take the Hadamard/Riesz *finite part* as $Y\to\infty$. Form $\zeta^0_X(s) = \Gamma(s)^{-1}\int_0^\infty t^{s-1}({}^{0}\!\operatorname{Tr}(e^{-t\Delta_X}) - P)\,dt$ (with $P$ the $L^2$-null projection) and set ${\det}_0\Delta_X := e^{-(\zeta^0_X)'(0)}$. On a closed surface, no cusps to cut and $\ker\Delta_X = \mathbb{R}$, so ${\det}_0\Delta_X$ reduces to $\det_\zeta\Delta_X$.

> [!recall]- Continuous spectrum and Eisenstein series
> **Formally:** on a cusped surface, $\Delta_X$ has spectrum $[1/4,\infty)$ (a continuous interval), realised by *generalised eigenfunctions* called **Eisenstein series** that are not in $L^2$ but are honest eigenfunctions locally.
> **In words:** unlike a compact surface (isolated eigenvalues), a cusped surface has a whole interval of "eigenvalues" that don't correspond to genuine $L^2$ eigenfunctions — instead they come from "waves" that don't decay at infinity, so their $L^2$ norm is infinite even though they satisfy $\Delta u = \lambda u$ pointwise.
> **Concretely:** on the modular surface $\mathrm{PSL}(2,\mathbb{Z})\backslash\mathbb{H}^2$, the Eisenstein series $E(z,s) = \sum y^s$ (summed over the cusp's orbit) is a formal eigenfunction of $\Delta$ with eigenvalue $s(1-s)$, for every $s$ with $\operatorname{Re}s = 1/2$ — giving the continuous band $[1/4,\infty)$.

> [!recall]- Trace-class operator
> **Formally:** $T:H\to H$ is *trace-class* if $\sum_j \langle|T|u_j, u_j\rangle < \infty$ for one (equivalently every) orthonormal basis $\{u_j\}$; then $\operatorname{Tr}(T) := \sum_j\langle Tu_j, u_j\rangle$ is well-defined and basis-independent.
> **In words:** an operator with a well-defined finite trace, generalising $\operatorname{Tr}(A) = \sum A_{jj}$ for finite matrices.
> **Concretely:** the identity operator on infinite-dimensional $H$ is NOT trace-class (its trace is $\infty$); the heat kernel $e^{-t\Delta}$ on a compact surface IS trace-class for every $t>0$ (Weyl's law gives $\sum_j e^{-t\lambda_j} < \infty$). On a cusped surface, $e^{-t\Delta_X}$ picks up the continuous-spectrum contribution $\int_{1/4}^\infty e^{-t\lambda}\,d\lambda$-type terms whose *spatial density* fails to be integrable across the cusps — so $e^{-t\Delta_X}$ fails to be trace-class.

> [!recall]- $L^2$-null projection $P$
> **Formally:** $P:L^2(X)\to L^2(X)$ is the orthogonal projection onto the finite-dimensional kernel of $\Delta_X$, i.e. onto the $L^2$-solutions of $\Delta u = 0$.
> **In words:** the projection onto the "constant modes" of the Laplacian — the eigenfunctions with eigenvalue exactly zero.
> **Concretely:** on a connected closed surface, $\ker\Delta = \mathbb{R}$ (only the constants), so $P$ is the rank-one operator $Pf = (1/\operatorname{Area})\int f\,d\operatorname{vol}$; it appears inside $\zeta_X(s)$-style formulas as a subtraction to strip off the $\lambda_0 = 0$ contribution that would blow up the sum $\sum \lambda_j^{-s}$ (since $0^{-s}$ is undefined).

> [!recall]- Finite part (Hadamard/Riesz)
> **Formally:** for a function $I(z)$ meromorphic near $z=0$ with Laurent expansion $I(z) = c_{-k}/z^k + \cdots + c_{-1}/z + c_0 + c_1 z + \cdots$, the *finite part* is $\operatorname{FP}_{z=0} I(z) := c_0$.
> **In words:** the "constant term" left after peeling off the pole terms — the natural finite number one attaches to a divergent expression when the divergence has a specific, isolatable structure.
> **Concretely:** for $I(z) = 1/z$, $\operatorname{FP}_{z=0} I = 0$; for $I(z) = e^{-z}/z = 1/z - 1 + z/2 - \cdots$, $\operatorname{FP}_{z=0} I = -1$; for $I(z) = \int_0^1 t^{z-1}\,dt = 1/z$ (computed by direct integration for $\operatorname{Re}z > 0$), $\operatorname{FP}_{z=0} I = 0$.

**Concrete unpacking (the mechanism, in one line).** For a single positive number $\lambda$, "$\zeta(s)=\lambda^{-s}$, $-\zeta'(0)=\log\lambda$" recovers $\log\lambda$; zeta regularisation just does this for all eigenvalues at once, using analytic continuation to make the infinite product sensible. The output $\det_\zeta\Delta_X$ is a single positive real number attached to the surface.

**Standard names.** **Spectral (Minakshisundaram–Pleijel) zeta function**, **zeta-regularised / Ray–Singer determinant**, **heat trace**, **Weyl's law**; the cusped-surface version is the **relative / $0$-determinant** (Müller; Borthwick–Judge–Perry). Reference: Ray–Singer, *R-torsion and the Laplacian*; for surfaces, Sarnak, *Determinants of Laplacians*.

---

# Examples and Non-Examples

**Is an instance.** On a closed hyperbolic surface, $\det_\zeta\Delta_X$ is the D'Hoker–Phong / Sarnak quantity, equal to $Z_X'(1)\,e^{(2g-2)(2\zeta_R'(-1)-1/4+\frac12\log2\pi)}$ (a Selberg-zeta derivative times a universal constant). On the round $S^2$, $\det_\zeta\Delta$ is a known constant ($\exp(\frac12-4\zeta_R'(-1))$).

**Is NOT an instance.** The naive product $\prod_{j\ge1}\lambda_j$ is **not** the zeta-regularised determinant — it diverges. Nor is $\exp(\sum_{j\le N}\log\lambda_j)$ for a hard cutoff $N$ a canonical answer; it depends on $N$ and the geometry of the truncation, whereas zeta regularisation is cutoff-independent.

**Calibration check.** (1) Verify $\lambda^{-s}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}e^{-t\lambda}\,dt$ (definition of $\Gamma$ after $t\mapsto t/\lambda$). (2) From the $t\downarrow0$ heat-trace asymptotic, locate the pole of $\zeta_X$ at $s=1$ (from the $1/t$ term) and confirm analyticity at $s=0$. (3) Check $\frac{d}{ds}\lambda_j^{-s}\big|_{s=0}=-\log\lambda_j$, motivating $-\zeta_X'(0)=\sum\log\lambda_j$.

---

# Where the paper uses this

§5 renormalises the (infinite, for finite-area $X$) total Brownian loop mass by expressing $\log\det_\zeta\Delta_X$ through it: Theorem 5.1 (compact) and Theorem 5.7 (finite-area) write $-\log\det_\zeta\Delta_X$ (resp. $-\log{\det}_0(\Delta_X+\kappa)$) as a length-spectrum sum $=$ loop mass, cancelling the divergence against the Selberg zeta's zero at $s=1$ in the $\kappa\to0$ limit. This finite determinant is the normalising constant of §6's probability measure. **[[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]]**.

---

# Verified against

Ray–Singer, *R-torsion and the Laplacian on Riemannian manifolds* (Adv. Math. 1971) for $\log\det_\zeta=-\zeta'(0)$; Sarnak, *Determinants of Laplacians* (Comm. Math. Phys. 1987) and D'Hoker–Phong, *On determinants of Laplacians on Riemann surfaces* for the closed hyperbolic case $\det_\zeta\Delta=Z_X'(1)\,e^{\cdots}$; Borthwick–Judge–Perry, *Selberg zeta functions and relative determinants* for the cusped $0$-determinant. Heat-trace asymptotic $\operatorname{Tr}(e^{-t\Delta})\sim\frac{\operatorname{Area}}{4\pi t}+\frac{\chi}{6}+\cdots$ standard (Minakshisundaram–Pleijel; McKean–Singer). Matches the paper's §5.
