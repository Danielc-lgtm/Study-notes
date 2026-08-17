---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Thm - Selberg Zeta Identity (Killing Case)"
  - "Def - Critical Exponent and the Prime Geodesic Theorem"
tags: [paper, spectral-geometry, determinants, renormalisation]
---

# Notation

- $X=\Gamma\backslash\mathbb{H}^2$ — a **closed** hyperbolic surface of genus $g$; $\mathcal{G}(X)$ all oriented closed geodesics, so $\mathcal{G}(X)\setminus\mathcal{P}_X$ are the non-primitive ones
- $\det_\zeta\Delta$ — the [[Def - Zeta-Regularised Determinant of the Laplacian|zeta-regularised determinant]] with $\lambda_0=0$ excluded
- $E=\big(4\zeta'_{\mathbb{R}}(-1)-\tfrac12+\log(2\pi)\big)/(4\pi)\approx0.0538$; $\gamma_{\mathrm{EM}}\approx0.5772$ the Euler–Mascheroni constant; $C$, $C_1$ universal constants
- $S_X(t)$ — the geometric term of the Selberg trace formula; $S^{\mathrm{p}}_X(t)$ its primitive part ($m=1$ only)
- $\mathrm{Li}(x)=\int_2^x\mathrm{d}t/\log t$; $\widetilde{\mathrm{Li}}(x)=\mathrm{Li}(x)$ for $x\geq2$ and $0$ for $x<2$
- $E_1(\kappa)=\int_1^\infty e^{-\kappa t}/t\,\mathrm{d}t$ — the exponential integral, $=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ as $\kappa\to0^+$
- $M_\kappa$, $R_\kappa$ — the total killing mass and the correction term in the proof of (ii)

---

# Type card

> [!abstract] Type card — Theorem 5.1 (determinant via loop measure, compact case)
> **Given.** A closed hyperbolic surface $X=\Gamma\backslash\mathbb{H}^2$ of genus $g$; the Selberg trace formula for the heat semigroup; the refined [[Def - Critical Exponent and the Prime Geodesic Theorem|prime geodesic theorem]] (43); Naud's formula (45); and any of the paper's Bernstein functions. $\det_\zeta\Delta$ excludes $\lambda_0=0$.
>
> **Produces.** Three expressions for $-\log\det_\zeta\Delta$, all real numbers, in terms of loop masses: a length-spectrum-truncated one for Brownian motion, a $\kappa\to0^+$ limit for killing yielding $\log\det_\zeta\Delta=\mathrm{Area}(X)E+\log Z'_X(1)$, and an $\alpha/2$-rescaled one for the stable case.
>
> **Lets you.** Renormalise the divergent Brownian total mass on a finite-area surface in a way that is **forced** rather than chosen — the divergence is exactly the pole of the spectral zeta function — and, in the killing form, obtain the classical determinant formula as a $\kappa\to0^+$ limit with no cutoff anywhere.

---

# Statement

> **Theorem 5.1 (zeta-regularised determinant of the Laplacian in terms of subordinate Brownian loop measure, compact case).** Let $X=\Gamma\backslash\mathbb{H}^2$ be a closed hyperbolic surface of genus $g$, and $\mathcal{G}(X)$ the set of all oriented closed geodesics on $X$. Write $\det_\zeta\Delta$ for the zeta-regularised determinant of $\Delta_X$ with $\lambda_0=0$ excluded. Let $\phi$ be any of the Bernstein functions treated in this paper.
>
> **(i) Brownian ($\phi(\lambda)=\lambda$):**
> $$-\log\det{}_\zeta\Delta = -\mathrm{Area}(X)E + C + \sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X\big(\mathcal{C}_X(\gamma)\big) + \int_{R=0}^\infty\frac{1}{e^R-1}\,\mathrm{d}\Big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\Big).\tag{46}$$
>
> **(ii) Brownian with killing ($\phi(\lambda)=\lambda+\kappa$, $\kappa>0$).** For each $\kappa>0$,
> $$-\log\det{}_\zeta\Delta = -\mathrm{Area}(X)E + \log\kappa + \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) + O(\kappa)\tag{47}$$
> $$= -\mathrm{Area}(X)E + \log\kappa - \log Z_X\Big(\tfrac12+\sqrt{\tfrac14+\kappa}\Big) + O(\kappa),\tag{48}$$
> and letting $\kappa\to0^+$, where $s=\tfrac12+\sqrt{\tfrac14+\kappa}\to1$ and the simple zero of $Z_X$ at $s=1$ (from $\lambda_0=0$) gives $-\log Z_X(s)\sim-\log Z'_X(1)-\log\kappa$, the $\log\kappa$ terms cancel and the $O(\kappa)$ vanishes, leaving
> $$\log\det{}_\zeta\Delta = \mathrm{Area}(X)E + \log Z'_X(1).\tag{49}$$
>
> **(iii) $\alpha$-stable ($\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$):**
> $$-\log\det{}_\zeta\Delta^{\alpha/2} = \frac{\alpha}{2}\Big(-\mathrm{Area}(X)E+C\Big) + \sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu^\alpha_X\big(\mathcal{C}_X(\gamma)\big) + \frac{\alpha}{2}\int_{R=0}^\infty\frac{1}{e^R-1}\,\mathrm{d}\Big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\Big).\tag{50}$$
>
> In (iii), $\det_\zeta\Delta^{\alpha/2}$ is the zeta-regularised determinant of the spectral fractional Laplacian, defined as in (45) with $\lambda_j$ replaced by $\lambda_j^{\alpha/2}$. In (i) and (iii) the summation and integral converge.

> [!note] Remark 5.2 — this is D'Hoker–Phong
> Equation (49) is the classical determinant formula
> $$\det{}_\zeta\Delta = Z'_X(1)\,e^{(2g-2)\left(2\zeta'_{\mathbb{R}}(-1)-\frac14+\frac12\log2\pi\right)},$$
> using $\mathrm{Area}(X)=4\pi(g-1)$ by Gauss–Bonnet. The loop-measure route does not produce a new formula; it produces a *derivation* in which every term has a probabilistic meaning, and in which the regulator is a killing rate rather than an analytic continuation.

---

# Why it is true

Part (ii) is the conceptually clean one and should be read first; parts (i) and (iii) are then bookkeeping.

**Part (ii): a killing rate is a regulator.** By [[Thm - Finiteness of the Total Mass|Corollary 4.7]], for $\kappa>0$ the total mass over non-trivial classes is already finite — so no cutoff is needed at all, and the entire content is a limit. Naud's formula expresses $-\log\det_\zeta\Delta$ as an integral of $S_X(t)/t$ split at $t=1$, and the killing total mass $M_\kappa=\int_0^\infty e^{-\kappa t}S_X(t)/t\,\mathrm{d}t$ is the same integral with the killing weight inserted. The difference between them is $O(\kappa)$ — because $1-e^{-\kappa t}\leq\kappa t$ and both $\int_0^1 S_X(t)\,\mathrm{d}t$ and $\int_1^\infty|S_X(t)-1|\,\mathrm{d}t$ are finite, $S_X$ being exponentially small as $t\to0$ and $|S_X-1|$ exponentially small as $t\to\infty$ — plus an exponential integral $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$.

So $-\log\det_\zeta\Delta = -\mathrm{Area}(X)E+\log\kappa+M_\kappa+O(\kappa)$, with the two Euler–Mascheroni constants cancelling. Now let $\kappa\to0^+$: $M_\kappa=-\log Z_X(s)$ by [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]], and $M_\kappa\to+\infty$ because $s\to1=\delta$. **But the divergence is exactly $-\log\kappa$**, because $\lambda_0=0$ gives $Z_X$ a simple zero at $s=1$, so $-\log Z_X(s)\sim-\log Z'_X(1)-\log(s-1)$ and $s-1\sim\kappa$. The two $\log\kappa$ cancel, and (49) drops out.

**The mechanism in one line: the killing rate $\kappa$ regularises the divergent total mass, its divergence as $\kappa\to0^+$ is a single $\log\kappa$, and that $\log\kappa$ is cancelled by the simple zero of $Z_X$ at $s=1$ that the eigenvalue $\lambda_0=0$ creates.**

**Part (i): the same renormalisation, done by truncation instead.** With $\kappa=0$ there is no regulator, so the divergence must be subtracted by hand — and the subtraction is chosen by the *refined* prime geodesic theorem (43), which says $N_X(R)=\widetilde{\mathrm{Li}}(e^R)+O_X(e^{(1-\epsilon)R})$. So subtracting $\widetilde{\mathrm{Li}}(e^R)$ from the counting measure removes exactly the divergent part and leaves a convergent integral. Note what this means: **the truncation is not arbitrary; it is the main term of the geodesic counting asymptotic, and what remains is the fluctuation.** The non-primitive geodesics need no truncation at all, since their masses ($m\geq2$) already sum absolutely, and they come out as the explicit sum $\sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X(\mathcal{C}_X(\gamma))$.

**Part (iii): one line.** $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$, so $\log\det_\zeta\Delta^{\alpha/2}=(\alpha/2)\log\det_\zeta\Delta$; and $\mu^\alpha_X=(\alpha/2)\mu_X$ on each homotopy-class term by §3.1.3. Multiply (46) by $\alpha/2$.

---

# Strategy

**Strategy (i).** Split Naud's integral into the non-primitive part, which converges without renormalisation and equals $\sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X(\mathcal{C}_X(\gamma))$ outright; and the primitive part, written as an integral against the prime geodesic counting measure, in which decomposing $N_X=\widetilde{\mathrm{Li}}(e^R)+(N_X-\widetilde{\mathrm{Li}}(e^R))$ sends the $X$-independent piece to a universal constant and collapses the remainder's error-function expression to $1/(e^R-1)$.

**Strategy (ii).** For $\kappa>0$ no cutoff is needed; split Naud's integral at $t=1$, compare with $M_\kappa$, bound the correction by $1-e^{-\kappa t}\leq\kappa t$ to get $O(\kappa)$, and use $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ so the two Euler–Mascheroni terms cancel. Then let $\kappa\to0^+$ and cancel $\log\kappa$ against the simple zero of $Z_X$ at $s=1$.

**Strategy (iii).** $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$ and $\mu^\alpha_X=(\alpha/2)\mu_X$; multiply (i) by $\alpha/2$.

> [!note]- The inputs: the trace formula and Naud's formula
> The Selberg trace formula for the heat semigroup on a closed hyperbolic surface gives
> $$\sum_{j\geq0}e^{-t\lambda_j} = \mathrm{Area}(X)\frac{e^{-t/4}}{(4\pi t)^{3/2}}\int_0^\infty\frac{re^{-r^2/(4t)}}{\sinh(r/2)}\,\mathrm{d}r \;+\; \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell(\gamma)}{2\sinh(m\ell(\gamma)/2)}e^{-(m\ell(\gamma))^2/(4t)},\tag{44}$$
> the first term being the **identity contribution** and the second the **geometric contribution** from hyperbolic conjugacy classes. Notice that the geometric term's summand is exactly the analytic factor of [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]] times the geometric prefactor — the trace formula's geometric side is a sum of the objects §3 computes one at a time.
>
> Naud uses this to write
> $$-\log\det{}_\zeta\Delta_X = -\mathrm{Area}(X)E-\gamma_{\mathrm{EM}} + \int_0^1\frac{S_X(t)}{t}\,\mathrm{d}t + \int_1^\infty\frac{S_X(t)-1}{t}\,\mathrm{d}t,\tag{45}$$
> where $S_X(t)$ is the geometric term of (44). Note $S_X(t)$ is exponentially small as $t\to0$ and $|S_X(t)-1|$ is exponentially small as $t\to\infty$, which is what makes both integrals converge.

> [!note]- Proof of (i) (skippable)
> The integral $\int_{R=0}^\infty\frac{1}{e^R-1}\,\mathrm{d}N_X(R)$ is the total mass $\sum_{\gamma\in\mathcal{P}_X}\mu_X(\mathcal{C}_X(\gamma))$ of Brownian loops homotopic to a primitive geodesic. Subtracting $\int_{R=0}^\infty\frac{1}{e^R-1}\,\mathrm{d}\widetilde{\mathrm{Li}}(e^R)$ renormalises the contribution of loops homotopic to a long ($R\gg1$) primitive geodesic, as suggested by (43). By the refined prime geodesic theorem, $|N_X(R)-\widetilde{\mathrm{Li}}(e^R)|=O_X(e^{(1-\epsilon)R})$ as $R\to\infty$ for some $\epsilon>0$ depending on $X$; hence the integral in (46) converges by integration by parts, and the sum converges for the same reason.
>
> Split the integrals in (45) as
> $$\int_0^1\frac{S_X(t)}{t}\,\mathrm{d}t+\int_1^\infty\frac{S_X(t)-1}{t}\,\mathrm{d}t = \int_0^\infty\frac{S_X(t)-S^{\mathrm{p}}_X(t)}{t}\,\mathrm{d}t + \int_0^1\frac{S^{\mathrm{p}}_X(t)}{t}\,\mathrm{d}t + \int_1^\infty\frac{S^{\mathrm{p}}_X(t)-1}{t}\,\mathrm{d}t,\tag{51}$$
> where $S^{\mathrm{p}}_X(t)=\sum_{\gamma\in\mathcal{P}_X}\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell(\gamma)}{2\sinh(\ell(\gamma)/2)}e^{-\ell(\gamma)^2/4t}$ is the primitive part.
>
> **The non-primitive part converges without renormalisation:**
> $$\int_0^\infty\frac{S_X(t)-S^{\mathrm{p}}_X(t)}{t}\,\mathrm{d}t = \sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq2}\int_0^\infty\frac1t\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell(\gamma)}{2\sinh(m\ell(\gamma)/2)}e^{-(m\ell(\gamma))^2/4t}\,\mathrm{d}t = \sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq2}\frac1m\frac{1}{e^{m\ell(\gamma)}-1} = \sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X\big(\mathcal{C}_X(\gamma)\big),\tag{52}$$
> the inner $t$-integral being exactly the Brownian computation of §3.1.1.
>
> **For the primitive part**, write $S^{\mathrm{p}}_X(t)$ as an integral against the prime geodesic counting measure,
> $$S^{\mathrm{p}}_X(t) = \int_{R=0}^\infty\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{R}{2\sinh(R/2)}e^{-R^2/4t}\,\mathrm{d}N_X(R),$$
> and exchange the order of integration in each of $\int_0^1 S^{\mathrm{p}}_X(t)/t\,\mathrm{d}t$ and $\int_1^\infty(S^{\mathrm{p}}_X(t)-1)/t\,\mathrm{d}t$. The inner $t$-integrals evaluate via the error function; the full calculation is in [WX25, Eqs. (4.13)–(4.16)]. Decomposing $N_X(R)=\widetilde{\mathrm{Li}}(e^R)+(N_X(R)-\widetilde{\mathrm{Li}}(e^R))$, the $\mathrm{d}\widetilde{\mathrm{Li}}(e^R)$ part has no $X$-dependence and contributes a universal constant $C_1$, and in the $\mathrm{d}(N_X(R)-\widetilde{\mathrm{Li}}(e^R))$ part the error-function expression collapses to $1/(e^R-1)$, with convergence given by (43). Hence
> $$\int_0^1\frac{S^{\mathrm{p}}_X(t)}{t}\,\mathrm{d}t+\int_1^\infty\frac{S^{\mathrm{p}}_X(t)-1}{t}\,\mathrm{d}t = C_1+\int_{R=0}^\infty\frac{1}{e^R-1}\,\mathrm{d}\Big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\Big).\tag{53}$$
> Substituting (52) and (53) into (51) and combining with (45) gives (46) with $C=-\gamma_{\mathrm{EM}}+C_1$. $\;\square$

> [!note]- Proof of (ii) (skippable)
> For $\kappa>0$ the total mass is finite by [[Thm - Finiteness of the Total Mass|Corollary 4.7]], so no cutoff is needed. Since the Brownian-with-killing heat trace is $e^{-\kappa t}S_X(t)$,
> $$M_\kappa := \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{e^{-\kappa t}S_X(t)}{t}\,\mathrm{d}t.$$
> Splitting at $t=1$ and subtracting $1$ from $S_X$ in the tail,
> $$M_\kappa = \int_0^1\frac{e^{-\kappa t}S_X(t)}{t}\,\mathrm{d}t+\int_1^\infty\frac{e^{-\kappa t}S_X(t)-1}{t}\,\mathrm{d}t+E_1(\kappa),\tag{54}$$
> where $E_1(\kappa):=\int_1^\infty e^{-\kappa t}/t\,\mathrm{d}t$. Comparing with Naud's (45),
> $$\int_0^1\frac{S_X(t)}{t}\,\mathrm{d}t+\int_1^\infty\frac{S_X(t)-1}{t}\,\mathrm{d}t = M_\kappa-E_1(\kappa)+R_\kappa,\tag{55}$$
> where
> $$R_\kappa := \int_0^1\frac{(1-e^{-\kappa t})S_X(t)}{t}\,\mathrm{d}t+\int_1^\infty\frac{(1-e^{-\kappa t})S_X(t)-1}{t}\,\mathrm{d}t.$$
> Using $1-e^{-\kappa t}\leq\kappa t$ on $(0,\infty)$,
> $$|R_\kappa|\leq\kappa\int_0^1 S_X(t)\,\mathrm{d}t+\kappa\int_1^\infty|S_X(t)-1|\,\mathrm{d}t = O(\kappa),$$
> since $S_X(t)$ is exponentially small as $t\to0^+$ and $|S_X(t)-1|$ is exponentially small as $t\to\infty$, so both integrals are finite. The standard expansion gives $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ as $\kappa\to0^+$.
>
> Substituting (55) into (45),
> $$-\log\det{}_\zeta\Delta = -\mathrm{Area}(X)E-\gamma_{\mathrm{EM}}+M_\kappa-E_1(\kappa)+R_\kappa = -\mathrm{Area}(X)E+\log\kappa+M_\kappa+O(\kappa),$$
> the two $\gamma_{\mathrm{EM}}$ terms cancelling. This is (47), and (48) follows by [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]]. Letting $\kappa\to0^+$ and using the simple zero of $Z_X$ at $s=1$ gives (49). $\;\square$

> [!note]- Proof of (iii) (skippable)
> Since $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$, one has $\log\det_\zeta\Delta^{\alpha/2}=(\alpha/2)\log\det_\zeta\Delta$ by the chain rule at $s=0$. Multiplying (46) by $\alpha/2$ and using $\mu^\alpha_X=(\alpha/2)\mu_X$ on each homotopy-class term gives (50). $\;\square$

---

# What this assumes, and where to climb

**The Selberg trace formula (44)** — quoted, and the deepest input to the paper. It is the first of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|five recorded gaps]]; home node *Automorphic Forms / Selberg Trace Formula* (🔵), references Iwaniec and Bergeron. Everything in §5.1 is arithmetic on top of it. **Worth noticing: the geometric term of (44) is a sum of exactly the quantities §3 computes one class at a time**, so [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] is what one term of the trace formula's geometric side looks like in isolation.

**Naud's formula (45)** — quoted; it is the trace formula converted into an expression for $-\log\det_\zeta\Delta$, with the constants $E$ and $\gamma_{\mathrm{EM}}$ made explicit.

**The refined prime geodesic theorem (43)** — [[Def - Critical Exponent and the Prime Geodesic Theorem]]. Two jobs in part (i): it chooses the truncation ($\widetilde{\mathrm{Li}}(e^R)$ is the main term) and it supplies the error bound $O_X(e^{(1-\epsilon)R})$ that makes the remaining integral converge.

**Corollary 4.3** — [[Thm - Selberg Zeta Identity (Killing Case)]], substituted to turn $M_\kappa$ into $-\log Z_X(s)$ in (48).

**Corollary 4.7** — [[Thm - Finiteness of the Total Mass]], for "the total mass is finite so no cutoff is needed" in part (ii).

**The simple zero of $Z_X$ at $s=1$**, from $\lambda_0=0$ — [[Def - Selberg Zeta Function]]. Without it the $\kappa\to0^+$ limit diverges and part (ii) has no conclusion.

**Closedness of $X$**, used everywhere: the trace formula (44) is the compact one, $e^{-t\Delta_X}$ is trace class, and the spectrum is discrete. §5.2 is the repair for the non-compact case.

---

# What consumes this

- [[Thm - Polyakov's Formula via Brownian Loop Measure|Corollary 5.4]] — extends (46) and (49) off the hyperbolic representative to every metric in the conformal class
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] — the section's central result
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] — the non-compact analogue, structurally parallel: substitute Corollary 4.3 into an explicit determinant factorisation and take $\kappa\to0^+$

---

# Reading it against the rest of the paper

The comparison worth drawing is between the two renormalisations. Part (i) truncates **by the length spectrum**, following Wang–Xue, subtracting the prime-geodesic main term $\widetilde{\mathrm{Li}}(e^R)$. Part (ii) uses **a killing rate as a regulator** and takes $\kappa\to0^+$. Both give the same answer, and (ii) is much shorter — because the killing rate does the work that the explicit truncation has to do by hand, and because Corollary 4.3 already computes the regularised quantity in closed form.

The paper notes that a third renormalisation exists in the literature, truncating **by quadratic variation** rather than by the length spectrum. All three agree because $\det_\zeta$ is defined independently of any of them; what differs is which terms the answer is expressed in.
