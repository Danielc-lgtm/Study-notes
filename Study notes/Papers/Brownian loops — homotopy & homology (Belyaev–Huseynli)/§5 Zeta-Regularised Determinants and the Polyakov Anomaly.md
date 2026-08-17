---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "5"
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)"
  - "Thm - Polyakov's Conformal Anomaly Formula"
  - "Def - Renormalised Integral and the 0-Trace"
  - "Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)"
tags: [paper, spectral-geometry, determinants, renormalisation]
---

# Notation

- $0=\lambda_0<\lambda_1\leq\lambda_2\leq\cdots$ — the eigenvalues of $\Delta_X$ on a **closed** hyperbolic surface, with multiplicity; $\lambda_0$ simple, with constant eigenfunctions; $\lambda_j\sim4\pi j/\mathrm{Area}(X)$ by Weyl's law
- $\zeta_X(s)=\sum_{j\geq1}\lambda_j^{-s}$ — the spectral zeta function, convergent for $\operatorname{Re}(s)>1$, meromorphically continued; regular at $0$ with $\zeta_X(0)=\chi(X)/6-1$
- $\log\det{}_\zeta\Delta_X := -\zeta'_X(0)$ — the [[Def - Zeta-Regularised Determinant of the Laplacian|zeta-regularised determinant]], zero eigenvalue excluded
- $E = \big(4\zeta'_{\mathbb{R}}(-1)-\tfrac12+\log(2\pi)\big)/(4\pi)\approx0.0538$ — the universal constant of Naud's formula; $\gamma_{\mathrm{EM}}\approx0.5772$ the Euler–Mascheroni constant; $C$, $C_1$ universal constants
- $\mathcal{G}(X)$ — the set of **all** oriented closed geodesics on $X$, so $\mathcal{G}(X)\setminus\mathcal{P}_X$ are the non-primitive ones
- $S_X(t)$ — the geometric term of the Selberg trace formula; $S^{\mathrm{p}}_X(t)$ its primitive part ($m=1$ only)
- $\mathrm{Li}(x)=\int_2^x\mathrm{d}t/\log t$; $\widetilde{\mathrm{Li}}(x)$ its cutoff, equal to $\mathrm{Li}(x)$ for $x\geq2$ and $0$ for $x<2$
- $E_1(\kappa)=\int_1^\infty e^{-\kappa t}/t\,\mathrm{d}t$ — the exponential integral, with $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ as $\kappa\to0^+$
- $g=e^{2\sigma}g_0$ — a conformal rescaling; $K_0$ the Gauss curvature of $g_0$; $P_X(\sigma)$ the Polyakov correction relative to $g_{\mathrm{hyp}}$
- $x$, $\mu$ — a boundary defining function on the compactification $\bar X$, and a smooth density; ${}^0\!\!\int_X$, ${}^0\mathrm{Tr}$, $\det_0$ — the [[Def - Renormalised Integral and the 0-Trace|renormalised integral, trace and determinant]]
- $n_C$, $n_F$ — the numbers of cusps and funnels; $\chi=\chi(X)$ the Euler characteristic; $P$ the projection onto the $L^2$ null space
- $M=\chi(X)\big(\tfrac12\log2\pi-2\zeta'_{\mathbb{R}}(-1)+\tfrac14\big)$, $F=-\chi(X)$, $G_\infty(s)=(2\pi)^{-s}\Gamma(s)G(s)^2$ with $G$ the Barnes $G$-function; $D_X(s)$ as in (66)

---

# What this section is for

[[Thm - Finiteness of the Total Mass|Corollary 4.7]] left a problem. On a finite-area surface $\delta=1$, so the Brownian total mass diverges, and there is nothing to normalise in §6. This section supplies the renormalisation — and its point is that the renormalisation is **not arbitrary**: the divergence is exactly the pole structure of the spectral zeta function, and subtracting it is the same operation as defining $\det_\zeta\Delta$.

The identification was already visible formally in [[§3.2 Euclidean Quantum Mechanics and the Path Integral|§3.2]]: the Schwinger proper-time representation writes $-\log\det(\Delta_X+\kappa)$ as $\int_0^\infty\frac{\mathrm{d}t}{t}e^{-\kappa t}\operatorname{Tr}(e^{-t\Delta_X})$, which is term for term the killing loop measure summed over *all* loops. What §5 does is make that rigorous, by choosing a regularisation and then computing what the divergent part actually is.

**The choice of regularisation matters and the paper makes a specific one.** Ray and Singer defined $\log\det_\zeta\Delta:=-\zeta'_X(0)$, and the observation that this can be read as a total loop mass is older than this paper (Le Jan; and for Riemann surfaces there is a renormalisation truncating by *quadratic variation*). The paper instead truncates **by the length spectrum**, following Wang–Xue. The advantage is that the truncation is then made of the same material as everything else in the paper — geodesic lengths and the counting function $N_X$ — so the answer comes out in terms the previous sections already produced.

There are two regimes and they are genuinely different problems.

**§5.1, closed surfaces.** Here $\Delta_X$ has purely discrete spectrum, $e^{-t\Delta_X}$ is trace class, and everything works. The input is the Selberg trace formula for the heat semigroup, which splits $\sum_j e^{-t\lambda_j}$ into an identity contribution and a geometric contribution $S_X(t)$ summed over hyperbolic conjugacy classes. Naud's formula turns $-\log\det_\zeta\Delta$ into an integral of $S_X(t)/t$. Theorem 5.1 then reorganises that integral into loop masses. The **killing** version, part (ii), is the cleanest: for $\kappa>0$ the total mass is already finite by Corollary 4.7, so no cutoff is needed at all, and the whole content is a $\kappa\to0^+$ limit in which a $\log\kappa$ divergence in $E_1(\kappa)$ cancels against the simple zero of $Z_X$ at $s=1$. What survives is
$$\log\det{}_\zeta\Delta = \mathrm{Area}(X)\,E + \log Z'_X(1),$$
the classical D'Hoker–Phong determinant formula. **The killing rate is a regulator, and sending it to zero is the renormalisation.** That is the cleanest single idea in §5.

**§5.2, finite-area non-compact surfaces.** Here the construction breaks: alongside the $L^2$ eigenvalues there is continuous spectrum filling $[\tfrac14,\infty)$ with multiplicity the number of cusps, whose generalised eigenfunctions are the [[Def - Eisenstein Series and the Continuous Spectrum|Eisenstein series]] and which do not lie in $L^2$. There is no discrete sequence to feed into $\sum_j\lambda_j^{-s}$ and $e^{-t\Delta_X}$ is not trace class. The paper's route — one of several, the other being a *relative* determinant comparing $\Delta_X$ to a model operator along the ends — is Melrose's microlocal method: compactify $X$ by capping each end with a circle at infinity, use the controlled asymptotic expansion of the heat kernel at the ends, and integrate the diagonal in a **renormalised** sense that removes the divergent part of that expansion. Then Borthwick–Judge–Perry relate the resulting $\det_0\Delta_X$ to $Z_X$, and Corollary 4.3 substitutes the loop mass for $-\log Z_X(s)$.

---

# §5.1 The compact case

## Theorem 5.1 — determinant via loop measure

> [!abstract] Type card — Theorem 5.1 (zeta-regularised determinant via loop measure, compact case)
> **Given.** A closed hyperbolic surface $X=\Gamma\backslash\mathbb{H}^2$ of genus $g$; the refined [[Def - Critical Exponent and the Prime Geodesic Theorem|prime geodesic theorem]] (43); the Selberg trace formula for the heat semigroup; and any of the paper's Bernstein functions. $\det_\zeta\Delta$ excludes $\lambda_0=0$.
>
> **Produces.** Three formulas for $-\log\det_\zeta\Delta$, all real numbers:
> **(i) Brownian.** $-\log\det_\zeta\Delta = -\mathrm{Area}(X)E + C + \sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X(\mathcal{C}_X(\gamma)) + \int_0^\infty\frac{1}{e^R-1}\,\mathrm{d}\big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\big)$, with both the sum and the integral convergent.
> **(ii) Killing, $\kappa>0$.** $-\log\det_\zeta\Delta = -\mathrm{Area}(X)E+\log\kappa+\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))+O(\kappa) = -\mathrm{Area}(X)E+\log\kappa-\log Z_X(s)+O(\kappa)$, and in the limit $\kappa\to0^+$, $\;\log\det_\zeta\Delta = \mathrm{Area}(X)E+\log Z'_X(1)$.
> **(iii) $\alpha$-stable.** The part-(i) formula multiplied by $\alpha/2$, giving $\det_\zeta\Delta^{\alpha/2}$, defined with $\lambda_j$ replaced by $\lambda_j^{\alpha/2}$.
>
> **Lets you.** Renormalise the divergent Brownian total mass on a finite-area surface in a way that is forced rather than chosen — the divergence is exactly the pole of the spectral zeta function — and, in the killing form, obtain the classical determinant formula as a $\kappa\to0^+$ limit with no cutoff anywhere.

**Strategy (i).** Split Naud's integral into the non-primitive part, which converges without renormalisation and equals $\sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X(\mathcal{C}_X(\gamma))$ outright; and the primitive part, written as an integral against the prime geodesic counting measure, in which decomposing $N_X = \widetilde{\mathrm{Li}}(e^R)+(N_X-\widetilde{\mathrm{Li}}(e^R))$ sends the $X$-independent piece to a universal constant and collapses the remainder's error-function expression to $1/(e^R-1)$.

**Strategy (ii).** For $\kappa>0$ no cutoff is needed; split Naud's integral at $t=1$, compare with $M_\kappa=\int_0^\infty e^{-\kappa t}S_X(t)/t\,\mathrm{d}t$, bound the correction by $|1-e^{-\kappa t}|\leq\kappa t$ to get $O(\kappa)$, and use $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ so that the two Euler–Mascheroni terms cancel. Then let $\kappa\to0^+$ and cancel $\log\kappa$ against the simple zero of $Z_X$ at $s=1$.

**Strategy (iii).** One line: $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$, so $\log\det_\zeta\Delta^{\alpha/2}=(\alpha/2)\log\det_\zeta\Delta$; multiply (i) by $\alpha/2$ and use $\mu^\alpha_X=(\alpha/2)\mu_X$ on each homotopy-class term.

Full proofs of all three parts: [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]].

> [!note] Remark 5.2 — this is D'Hoker–Phong
> Equation (49) is the classical determinant formula
> $$\det{}_\zeta\Delta = Z'_X(1)\,e^{(2g-2)\left(2\zeta'_{\mathbb{R}}(-1)-\frac14+\frac12\log2\pi\right)},$$
> using $\mathrm{Area}(X)=4\pi(g-1)$ by Gauss–Bonnet. So the loop-measure route is not producing a new formula; it is producing a *derivation* of a known formula in which every term has a probabilistic meaning, and in which the regulator is a killing rate rather than an analytic continuation.

## §5.1.1 Polyakov's conformal anomaly

Theorem 5.1 computes $\log\det_\zeta\Delta$ on the hyperbolic representative of each conformal class. Polyakov's formula supplies the transformation law within a fixed conformal class, so the two together cover every metric.

> [!abstract] Type card — Theorem 5.3 (Polyakov's conformal anomaly formula)
> **Given.** Conformally equivalent smooth metrics $g_0$ and $g=e^{2\sigma}g_0$ on a closed surface $X$, with $K_0$ the Gauss curvature of $g_0$.
>
> **Produces.** The transformation law
> $$\log\det{}_\zeta\Delta_X = -\frac{1}{12\pi}\int_X|\nabla_{g_0}\sigma|^2\,\mathrm{d}\mathrm{vol}_{g_0} - \frac{1}{6\pi}\int_X K_0\,\sigma\,\mathrm{d}\mathrm{vol}_{g_0} + \log\frac{\mathrm{vol}_g(X)}{\mathrm{vol}_{g_0}(X)} + \log\det{}_\zeta\Delta_{g_0}.$$
>
> **Lets you.** Move between any two metrics in a conformal class without recomputing a determinant — the difference is an explicit local functional of $\sigma$ plus a volume ratio.

Specialising $g_0=g_{\mathrm{hyp}}$, the unique hyperbolic representative (so $K_0\equiv-1$ and $\mathrm{vol}_{g_0}(X)=\mathrm{Area}(X)=4\pi(g-1)$ by Gauss–Bonnet), the curvature coupling reduces to $+\frac{1}{6\pi}\int_X\sigma\,\mathrm{d}A_{\mathrm{hyp}}$ and one writes
$$P_X(\sigma) := -\frac{1}{12\pi}\int_X|\nabla\sigma|^2\,\mathrm{d}A_{\mathrm{hyp}} + \frac{1}{6\pi}\int_X\sigma\,\mathrm{d}A_{\mathrm{hyp}} + \log\frac{\mathrm{vol}_g(X)}{4\pi(g-1)}$$
for the Polyakov correction, so that $\log\det_\zeta\Delta_g = P_X(\sigma)+\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$.

> [!abstract] Type card — Corollary 5.4 (Polyakov's formula via Brownian loop measure)
> **Given.** A closed hyperbolic surface $X$ of genus $g$, and any smooth metric $g=e^{2\sigma}g_{\mathrm{hyp}}$ in its conformal class.
>
> **Produces.** $\log\det_\zeta\Delta_X = P_X(\sigma)+\mathrm{Area}(X)E-C-\sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X(\mathcal{C}_X(\gamma))-\int_0^\infty\frac{1}{e^R-1}\mathrm{d}(N_X(R)-\widetilde{\mathrm{Li}}(e^R))$; equivalently, via the $\kappa\to0^+$ limit, $\log\det_\zeta\Delta_X = P_X(\sigma)+\mathrm{Area}(X)E+\log Z'_X(1)$.
>
> **Lets you.** Extend the loop-measure determinant formula from the hyperbolic representative to every metric in the conformal class, with the loop-measure content untouched and all the metric dependence isolated in $P_X(\sigma)$.

Pages: [[Thm - Polyakov's Conformal Anomaly Formula]], [[Thm - Polyakov's Formula via Brownian Loop Measure]]. Note that this is the second and last place [[Constr - The Brownian Loop Measure|conformal invariance]] is cashed in — the loop-measure terms are conformally invariant, which is *why* they are unchanged by the rescaling and all the $\sigma$-dependence collects into a single explicit functional.

---

# §5.2 The non-compact finite-area case

## What breaks, and the repair

On a non-compact finite-area surface the $L^2$ spectrum starting at $\lambda_0=0$ is joined by continuous spectrum filling $[\tfrac14,\infty)$ with multiplicity $n_C$, whose generalised eigenfunctions are the [[Def - Eisenstein Series and the Continuous Spectrum|Eisenstein series]] $E_j(z,s)$ solving $\Delta_X E_j = s(1-s)E_j$ but not lying in $L^2$. So $\sum_j\lambda_j^{-s}$ has no meaning and $e^{-t\Delta_X}$ is not trace class.

The repair, following Melrose, is to renormalise rather than to compare. Fix the compactification $\bar X$ obtained by capping each end with a circle at infinity, with boundary defining function $x$ and smooth density $\mu$. For $f$ with a controlled expansion at the ends, $\int_X x^z f\mu$ converges for $\operatorname{Re}(z)$ large and continues meromorphically, and its finite part at $z=0$ is the **renormalised integral** ${}^0\!\!\int_X f\mu := \mathrm{FP}_{z=0}\int_X x^z f\mu$. Applied to the volume form this gives the renormalised area, which for a hyperbolic metric equals $-2\pi\chi(X)$ by the Gauss–Bonnet theorem for such metrics. Applied to the heat-kernel diagonal it gives the **$0$-trace** ${}^0\mathrm{Tr}(e^{-t\Delta_X}) := {}^0\!\!\int_X p_X(t,z,z)\,\mathrm{d}\mathrm{vol}_g(z)$, and the Mellin transform of ${}^0\mathrm{Tr}(e^{-t\Delta_X}-P)$ defines $\zeta^0_X$ and hence $\det_0\Delta_X := e^{-(\zeta^0_X)'(0)}$. On a closed surface the $0$-trace is the ordinary trace and $\det_0$ reduces to $\det_\zeta$. Details: [[Def - Renormalised Integral and the 0-Trace]].

> [!abstract] Type card — Theorem 5.5 (Borthwick–Judge–Perry)
> **Given.** A geometrically finite hyperbolic surface $X$ with $n_C$ cusps and Euler characteristic $\chi$; the resolvent $R_X(s)=(\Delta_X-s(1-s))^{-1}$ and its renormalised trace.
>
> **Produces.** The explicit factorisation
> $$\det{}_0\big(\Delta_X-s(1-s)\big) = Z_X(s)\,e^{M+Fs(1-s)}\,G_\infty(s)^\chi\Big(\tfrac{2s}{\sqrt\pi}\big(s-\tfrac12\big)\Gamma\big(s-\tfrac12\big)\Big)^{-n_C},$$
> with $M$, $F$, $G_\infty$ as in the notation registry; and consequently $\det_0\Delta_X = C_XZ'_X(1)$ when $\mathrm{Area}(X)<\infty$, $\;=C_XZ_X(1)$ when $\mathrm{Area}(X)=\infty$.
>
> **Lets you.** Convert every $\det_0$ statement into a $Z_X$ statement, which Corollary 4.3 then converts into a loop-mass statement.

This is quoted, not proved; see [[Thm - Borthwick–Judge–Perry Determinant Formula]] and the gaps section of [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes]]. The derivative $Z'_X(1)$ appears in the finite-area case for a reason worth remembering: $0$ lies in the spectrum of $\Delta_X$ when $\mathrm{Area}(X)<\infty$, giving $Z_X$ a simple zero at $s=1$, which must be divided out. In infinite area $0$ is not an $L^2$ eigenvalue, $Z_X(1)\neq0$, and no derivative is needed.

## Theorem 5.7 — the finite-area formula

> [!abstract] Type card — Theorem 5.7 (determinant via loop measure, finite-area case)
> **Given.** A geometrically finite hyperbolic surface $X$ of finite area with $n_C$ cusps and Euler characteristic $\chi$; the constants $M$, $F$ and the function $D_X(s)$ of Theorem 5.5; and $\kappa\geq0$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$, so that $s(s-1)=\kappa$ and $\Delta_X-s(1-s)=\Delta_X+\kappa$.
>
> **Produces.** The identity
> $$-\log\det{}_0(\Delta_X+\kappa) = F\kappa - M + \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) - D_X(s),$$
> and, dividing out the simple zero and letting $\kappa\to0^+$, $\;\log\det_0\Delta_X = M+D_X(1)+\log Z'_X(1)=\log C_X+\log Z'_X(1)$, where $D_X(1)=-\chi\log(2\pi)-n_C\log\sqrt{2\pi}$.
>
> **Lets you.** Run the entire §5 programme when the Laplacian has continuous spectrum and the heat semigroup is not trace class — so that a cusped surface, which by [[Thm - Finiteness of the Total Mass|Corollary 4.7]] has divergent Brownian total mass, still yields a well-defined determinant and hence a normalisable measure in §6.

**Strategy.** Substitute the Corollary 4.3 identity $-\log Z_X(s)=\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ into the logarithm of the Borthwick–Judge–Perry factorisation, using $s(1-s)=-\kappa$; then take the limit by expanding $Z_X(s)=Z'_X(1)(s-1)+O((s-1)^2)$ and observing that dividing by $s(s-1)=\kappa$ subtracts a $\log(s-1)$ that cancels the divergence, since $s-1\sim\kappa$ as $\kappa\to0^+$.

Full proof: [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)]].

> [!note] Remark 5.8 — the infinite-area case
> When $\mathrm{Area}(X)=\infty$ one has $\delta<1$, so by Corollary 4.7 the total mass is already finite and no renormalisation is required at all: the determinant identity holds directly at $s=1$, because $0$ is not an $L^2$ eigenvalue and $Z_X(1)\neq0$. The corresponding expression for $-\log\det_0\Delta_X$ via the loop mass and the resonance divisor of $Z_X$ is Lemonde–Wang's, and follows from Theorem 5.5. The Polyakov anomaly formula for non-compact surfaces exists in the literature too.

---

# What to carry forward

**The regulator idea.** A killing rate is a regulator; $\kappa\to0^+$ is the renormalisation; the $\log\kappa$ divergence cancels against the simple zero of $Z_X$ at $s=1$ that $\lambda_0=0$ creates. This is the cleanest single mechanism in the section and it is what makes part (ii) of Theorem 5.1 shorter than part (i).

**$\log\det_\zeta\Delta = \mathrm{Area}(X)E+\log Z'_X(1)$** for a closed hyperbolic surface — D'Hoker–Phong, re-derived probabilistically — and its cusped analogue $\log\det_0\Delta_X = \log C_X+\log Z'_X(1)$.

**Where the conformal invariance of $\mu_X$ is spent.** Twice in the whole paper: §3.4's length-spectrum identity, and Corollary 5.4. Both times the mechanism is the same — the loop-measure terms do not move under a conformal change, so all the metric dependence isolates into an explicit local functional.

**That the finite-area and infinite-area cases are genuinely different**, and that the divergence in the finite-area case is the presence of $\lambda_0=0$, hence the zero of $Z_X$ at $s=1$, hence the need for a derivative.

Next: [[§6 Probability Measures on Homotopy and Homology Classes]], which is what all the finiteness work was for.
