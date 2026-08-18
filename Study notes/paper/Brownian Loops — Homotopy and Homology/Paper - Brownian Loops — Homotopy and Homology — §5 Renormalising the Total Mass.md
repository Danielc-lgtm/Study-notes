---
type: paper-section
paper: "Belyaev–Huseynli, A probability measure on homotopy & homology classes via Brownian loops"
section: "5 — Renormalising the total mass"
tags: [paper, brownian-loops, spectral-geometry, zeta-functions]
---

# §5 — Renormalising the total mass of Brownian loops

Back to the [[Paper - Brownian Loops — Homotopy and Homology|hub]]. §4 showed the total loop mass is $-\log Z_X(1)$ — **finite for infinite-area surfaces but infinite for finite-area ones** (where $\delta=1$ and the trivial class diverges). To get an honest probability measure on homotopy classes (§6) one must renormalise this infinite total. The right renormalised value turns out to be a classical spectral invariant, the **zeta-regularised determinant of the Laplacian** $\det_\zeta\Delta_X$. This section expresses $-\log\det_\zeta\Delta_X$ as a (renormalised) total loop mass, in the compact case (§5.1), under conformal change (§5.1.1, Polyakov), and in the finite-area cusped case (§5.2). Much of the machinery — the Selberg trace formula, Naud's determinant formula, the D'Hoker–Phong and Borthwick–Judge–Perry identities — is external; the paper's own content is the *reorganisation into loop masses* and a clean $\kappa\to0$ limit in which a $\log\kappa$ divergence cancels against the Selberg zeta's zero. Those we prove in full; the inputs are stated as external callouts.

**Symbols.** $\{\lambda_j\}$ the Laplace eigenvalues; $\zeta_X(s)=\sum_{j\ge1}\lambda_j^{-s}$; $\det_\zeta\Delta$ the [[Def - Zeta-Regularised Determinant of the Laplacian|zeta-regularised determinant]]; $\chi(X)=2-2g$; $\kappa\ge0$ killing rate, $s=\frac12+\sqrt{\frac14+\kappa}$; $E=\frac{1}{4\pi}(4\zeta_R'(-1)-\frac12+\log2\pi)\approx0.0538$; $N_X(R)$ the geodesic counting function; $\widetilde{\mathrm{Li}}$ the cutoff logarithmic integral.

---

## §5.1 — The compact case

> [!recall]- Zeta-regularised determinant of the Laplacian
> **Formally:** for a closed surface with eigenvalues $0=\lambda_0<\lambda_1\le\cdots$, $\zeta_X(s)=\sum_{j\ge1}\lambda_j^{-s}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}(\operatorname{Tr}e^{-t\Delta_X}-1)\,dt$ continues meromorphically, is regular at $0$, and $\log\det_\zeta\Delta_X:=-\zeta_X'(0)$. See [[Def - Zeta-Regularised Determinant of the Laplacian]].
> **In words:** the finite, canonical stand-in for the divergent product $\prod_{j\ge1}\lambda_j$; read off from heat-trace (hence loop) data.

The bridge from the determinant to loops is a length-spectrum expansion of $-\log\det_\zeta\Delta$, which the paper takes from the Selberg trace formula.

> [!cite]- External input — Selberg trace formula and Naud's determinant expansion
> **Statement (typed):** on a closed hyperbolic surface, the heat trace splits into an *identity* (geometric-area) term and a *geodesic* term,
> $$\sum_{j\ge0}e^{-t\lambda_j}=\operatorname{Area}(X)\frac{e^{-t/4}}{(4\pi t)^{3/2}}\!\int_0^\infty\frac{r\,e^{-r^2/4t}}{\sinh(r/2)}\,dr+\underbrace{\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell_\gamma\,e^{-(m\ell_\gamma)^2/4t}}{2\sinh(m\ell_\gamma/2)}}_{=:S_X(t)},$$
> and (Naud) $-\log\det_\zeta\Delta_X=-\operatorname{Area}(X)\,E-\gamma_{\mathrm{EM}}+\int_0^1\frac{S_X(t)}{t}\,dt+\int_1^\infty\frac{S_X(t)-1}{t}\,dt$, where $\gamma_{\mathrm{EM}}\approx0.5772$ is Euler–Mascheroni and $S_X$ is the geodesic term above (exponentially small as $t\to0$; $S_X(t)-1$ exponentially small as $t\to\infty$).
> **Why it's true:** the trace formula equates a spectral sum with a sum over the identity and hyperbolic conjugacy classes of $\Gamma$ (the geodesics); feeding it through the Mellin/$\zeta'(0)$ machine turns $-\log\det_\zeta$ into an integral of the geodesic term. **Source:** Selberg; Naud (via [WX25]). Take on faith; the geodesic term $S_X(t)$ is exactly the $t\downarrow0$ heat-kernel weight of Brownian loops of each length, which is why it re-expresses as a loop mass.

Notice $S_X(t)$'s summand is precisely the strip heat-kernel integrand of §3 (the Wang–Xue Lemma 3.4 integrand with $s=t$): so $\int\frac{S_X(t)}{t}\,dt$ is a total Brownian loop mass. The paper renormalises the divergent finite-area case by subtracting the *long-geodesic* tail predicted by the refined prime geodesic theorem.

> [!cite]- External input — refined prime geodesic theorem (closed case)
> **Statement (typed):** for a closed hyperbolic surface ($\delta=1$), $N_X(R)=\operatorname{Li}(e^{R})+\sum_{0<\lambda_j\le1/4}\operatorname{Li}(e^{s_jR})+O_X(e^{3R/4}/R)$ as $R\to\infty$, where $\operatorname{Li}(x)=\int_2^x\frac{dt}{\log t}\sim x/\log x$ and $s_j=\frac12+\sqrt{\frac14-\lambda_j}$.
> **Why it's true:** the small eigenvalues $\lambda_j<\frac14$ contribute extra $\operatorname{Li}(e^{s_jR})$ terms beyond the main $\operatorname{Li}(e^R)$; the error is controlled by the zero-free region of $Z_X$. **Source:** Selberg/Hejhal; via [WX25]. This gives $|N_X(R)-\widetilde{\mathrm{Li}}(e^R)|=O_X(e^{(1-\epsilon)R})$, making the renormalising integral converge.

> **Theorem 5.1 (determinant as a renormalised loop mass; compact case).** Let $X=\Gamma\backslash\mathbb{H}^2$ be closed of genus $g$, $\mathcal G(X)$ all oriented closed geodesics, $\det_\zeta\Delta$ with $\lambda_0=0$ excluded, $\phi$ any Bernstein function of the paper. Then, with $E$, $C$ (a universal constant), and $\widetilde{\mathrm{Li}}$ (the logarithmic integral cut off at $x=2$) as above:
> **(i) Brownian ($\phi=\lambda$):** $\displaystyle -\log\det_\zeta\Delta=-\operatorname{Area}(X)E+C+\!\!\sum_{\gamma\in\mathcal G(X)\setminus\mathcal P_X}\!\!\mu_X(C_X(\gamma))+\int_0^\infty\frac{1}{e^R-1}\,d\big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\big).$
> **(ii) Killing ($\phi=\lambda+\kappa$, $\kappa>0$):** $\displaystyle -\log\det_\zeta\Delta=-\operatorname{Area}(X)E+\log\kappa+\sum_{\gamma,m}\mu^\kappa_X(C_X(\gamma^m))+O(\kappa)=-\operatorname{Area}(X)E+\log\kappa-\log Z_X\!\big(\frac12+\sqrt{\frac14+\kappa}\big)+O(\kappa)$, and letting $\kappa\to0^+$ gives $\log\det_\zeta\Delta=\operatorname{Area}(X)E+\log Z_X'(1)$.
> **(iii) $\alpha$-stable:** as (i), scaled by $\frac\alpha2$ on the geometric terms (determinant of the spectral fractional Laplacian).

Stub: [[Thm - Determinant as Renormalised Loop Mass]]. Write $S^p_X(t):=\sum_{\gamma\in\mathcal P_X}\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell_\gamma}{2\sinh(\ell_\gamma/2)}e^{-\ell_\gamma^2/4t}$ for the **primitive part** ($m=1$ only) of Naud's geodesic term $S_X(t)$. All three cases start from Naud's formula and differ only in how the small-$t$ divergence of $\int S_X/t$ is tamed.

> [!note]- Gap-free proof of Theorem 5.1(ii), finite κ (the first line)
> **Step 0 — Naud's integral with killing.** The killed heat trace is $e^{-\kappa t}S_X(t)$, so the total killed mass is $M_\kappa:=\sum_{\gamma,m}\mu^\kappa_X(C_X(\gamma^m))=\int_0^\infty e^{-\kappa t}\frac{S_X(t)}{t}\,dt$ (finite for $\kappa>0$, so no cutoff is needed). Split at $t=1$ and subtract $1$ in the tail:
> $$M_\kappa=\int_0^1 e^{-\kappa t}\frac{S_X(t)}{t}\,dt+\int_1^\infty e^{-\kappa t}\frac{S_X(t)-1}{t}\,dt+E_1(\kappa),\qquad E_1(\kappa):=\int_1^\infty\frac{e^{-\kappa t}}{t}\,dt$$
> ($E_1$ the exponential integral). Comparing with the integral in [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|Naud's formula]] $\int_0^1\frac{S_X}{t}+\int_1^\infty\frac{S_X-1}{t}=M_\kappa-E_1(\kappa)+R_\kappa$, where $R_\kappa:=\int_0^1(1-e^{-\kappa t})\frac{S_X}{t}\,dt+\int_1^\infty(1-e^{-\kappa t})\frac{S_X-1}{t}\,dt$.
> **Step 1 — bound the correction.** Using $1-e^{-\kappa t}\le\kappa t$, $|R_\kappa|\le\kappa\int_0^1 S_X(t)\,dt+\kappa\int_1^\infty|S_X(t)-1|\,dt=O(\kappa)$, both integrals finite because $S_X(t)$ is exponentially small as $t\to0^+$ and $|S_X(t)-1|$ is exponentially small as $t\to\infty$. The standard expansion is $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ as $\kappa\to0^+$.
> **Step 2 — substitute into Naud.** $-\log\det_\zeta\Delta=-\operatorname{Area}(X)E-\gamma_{\mathrm{EM}}+M_\kappa-E_1(\kappa)+R_\kappa=-\operatorname{Area}(X)E+\log\kappa+M_\kappa+O(\kappa)$ — the two $\gamma_{\mathrm{EM}}$ cancel. This is the first line of (ii). $\blacksquare$

> [!note]- Gap-free proof of Theorem 5.1(ii) as κ→0 (the limit)
> **Step 1 — insert the Selberg identity.** By [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]], $M_\kappa=\sum_{\gamma,m}\mu^\kappa_X(C_X(\gamma^m))=-\log Z_X(s)$ with $s=\frac12+\sqrt{\frac14+\kappa}$, giving the second line $-\log\det_\zeta\Delta=-\operatorname{Area}(X)E+\log\kappa-\log Z_X(s)+O(\kappa)$.
> **Step 2 — expand $Z_X$ near its zero at $s=1$.** On a *closed* surface $\lambda_0=0$ is a genuine eigenvalue, forcing $Z_X$ a **simple zero at $s=1$**: $Z_X(s)=Z_X'(1)(s-1)+O((s-1)^2)$, so $-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1)$.
> **Step 3 — relate $\log(s-1)$ to $\log\kappa$.** $s-1=\sqrt{\frac14+\kappa}-\frac12=\frac{\kappa}{\sqrt{1/4+\kappa}+\frac12}\to\kappa$ as $\kappa\to0^+$, so $\log(s-1)=\log\kappa+o(1)$.
> **Step 4 — cancel.** The $\log\kappa$ and $-\log(s-1)=-\log\kappa-o(1)$ cancel, leaving $\log\det_\zeta\Delta=\operatorname{Area}(X)E+\log Z_X'(1)$. $\blacksquare$
> *(This is the classical D'Hoker–Phong determinant formula $\det_\zeta\Delta=Z_X'(1)\,e^{(2g-2)(2\zeta_R'(-1)-1/4+\frac12\log2\pi)}$ — see Remark 5.2. ⚠️ The factor-of-2 bookkeeping between the constant $E$ and D'Hoker–Phong's exponent is a convention I did not fully reconcile; flagged.)*

> [!note]- Gap-free proof of Theorem 5.1(i), Brownian ($\kappa=0$)
> With no killing there is no $\log\kappa$ to absorb the divergence, so the paper renormalises *geometrically*, following [WX25].
> **Step 1 — split Naud's integral (eq. 51).** $\int_0^1\frac{S_X}{t}+\int_1^\infty\frac{S_X-1}{t}=\int_0^\infty\frac{S_X-S^p_X}{t}\,dt+\int_0^1\frac{S^p_X}{t}\,dt+\int_1^\infty\frac{S^p_X-1}{t}\,dt$, isolating the primitive part $S^p_X$.
> **Step 2 — the non-primitive part (eq. 52), computed in closed form.** $\int_0^\infty\frac{S_X-S^p_X}{t}\,dt=\sum_{\gamma\in\mathcal P_X}\sum_{m\ge2}\int_0^\infty\frac1t\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}e^{-(m\ell_\gamma)^2/4t}\,dt$. Each inner integral is exactly the §3.1.1 computation: $\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}(4\pi)^{-1/2}\int_0^\infty t^{-3/2}e^{-t/4-(m\ell_\gamma)^2/4t}\,dt=\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}\cdot\frac{e^{-m\ell_\gamma/2}}{m\ell_\gamma}=\frac1m\frac{1}{e^{m\ell_\gamma}-1}$ (Gaussian-type identity, $(4\pi)^{-1/2}\cdot\frac{2\sqrt\pi}{m\ell_\gamma}=\frac1{m\ell_\gamma}$). So the non-primitive part $=\sum_{\gamma\in\mathcal P_X}\sum_{m\ge2}\frac1m\frac1{e^{m\ell_\gamma}-1}=\sum_{\gamma\in\mathcal G(X)\setminus\mathcal P_X}\mu_X(C_X(\gamma))$, the masses of the *non-primitive* closed geodesics $\gamma^m$ ($m\ge2$).
> **Step 3 — the primitive part (eq. 53), renormalised.** Write $S^p_X(t)=\int_0^\infty\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{R}{2\sinh(R/2)}e^{-R^2/4t}\,dN_X(R)$ against the prime-geodesic counting measure, exchange the order of integration in $\int_0^1 S^p_X/t$ and $\int_1^\infty(S^p_X-1)/t$, and evaluate the inner $t$-integrals via the error function.
> > [!cite]- External input — the inner $t$-integral evaluation [WX25, (4.13)–(4.16)]
> > The exchanged inner integrals evaluate to error-function expressions; decomposing $N_X(R)=\widetilde{\mathrm{Li}}(e^R)+(N_X(R)-\widetilde{\mathrm{Li}}(e^R))$, the $d\widetilde{\mathrm{Li}}(e^R)$ part is $X$-independent and contributes a **universal constant** $C_1$, while in the $d(N_X-\widetilde{\mathrm{Li}}(e^R))$ part the error-function expression **collapses to** $\frac{1}{e^R-1}$, with convergence guaranteed by the refined prime geodesic theorem. **Source:** Wang–Xue [WX25, Eqs. (4.13)–(4.16)]; the calculation is a definite-integral evaluation, taken on faith here.
> Hence $\int_0^1\frac{S^p_X}{t}+\int_1^\infty\frac{S^p_X-1}{t}=C_1+\int_0^\infty\frac{1}{e^R-1}\,d\big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\big)$, the last integral convergent because $|N_X(R)-\widetilde{\mathrm{Li}}(e^R)|=O_X(e^{(1-\epsilon)R})$ (refined prime geodesic theorem), so integration by parts closes it.
> **Step 4 — combine.** Substituting Steps 2–3 into the split of Step 1 and into Naud's formula gives case (i), with the constant $C=-\gamma_{\mathrm{EM}}+C_1$. $\blacksquare$

> [!note]- Gap-free proof of Theorem 5.1(iii), α-stable
> The spectral fractional Laplacian $\Delta^{\alpha/2}$ has eigenvalues $\lambda_j^{\alpha/2}$, so its spectral zeta is $\zeta_{\Delta^{\alpha/2}}(s)=\sum_j(\lambda_j^{\alpha/2})^{-s}=\sum_j\lambda_j^{-\alpha s/2}=\zeta_X(\alpha s/2)$; differentiating at $s=0$ gives $\log\det_\zeta\Delta^{\alpha/2}=-\zeta_{\Delta^{\alpha/2}}'(0)=-\frac\alpha2\zeta_X'(0)=\frac\alpha2\log\det_\zeta\Delta$. Multiplying case (i) by $\alpha/2$ and using $\mu^\alpha_X=\frac\alpha2\mu_X$ on each homotopy-class term (§3.1.3) yields case (iii). $\blacksquare$

**Remark 5.2 (the D'Hoker–Phong formula).** Equation (49) — $\log\det_\zeta\Delta=\operatorname{Area}(X)E+\log Z_X'(1)$ — is the classical determinant formula of D'Hoker–Phong, $\det_\zeta\Delta=Z_X'(1)\,e^{(2g-2)(2\zeta_R'(-1)-1/4+\frac12\log2\pi)}$.

---

## §5.1.1 — Polyakov's conformal anomaly formula

Theorem 5.1 computes $\log\det_\zeta\Delta$ for the *hyperbolic* metric in a conformal class; Polyakov's formula transports it to any conformally-equivalent metric.

> [!cite]- External input — Polyakov's conformal anomaly formula (Theorem 5.3)
> **Statement (typed):** for conformally-equivalent smooth metrics $g_0$ and $g=e^{2\sigma}g_0$ on a closed surface, with $K_0$ the Gauss curvature of $g_0$,
> $$\log\det_\zeta\Delta_g=-\frac{1}{12\pi}\!\int_X|\nabla_{g_0}\sigma|^2\,d\!\operatorname{vol}_{g_0}-\frac{1}{6\pi}\!\int_X K_0\,\sigma\,d\!\operatorname{vol}_{g_0}+\log\frac{\operatorname{vol}_g(X)}{\operatorname{vol}_{g_0}(X)}+\log\det_\zeta\Delta_{g_0}.$$
> **Why it's true:** the conformal variation of $\log\det_\zeta$ is a local curvature integral (the *conformal anomaly* of the 2-D scalar determinant); integrating it gives Polyakov's formula. **Source:** Polyakov; Osgood–Phillips–Sarnak. The $-\frac1{12\pi}$ is the central-charge normalisation of one free boson.

Specialising $g_0=g_{\mathrm{hyp}}$ ($K_0\equiv-1$, $\operatorname{Area}=4\pi(g-1)$ by Gauss–Bonnet) and writing $P_X(\sigma):=-\frac1{12\pi}\int|\nabla\sigma|^2\,dA_{\mathrm{hyp}}+\frac1{6\pi}\int\sigma\,dA_{\mathrm{hyp}}+\log\frac{\operatorname{vol}_g(X)}{4\pi(g-1)}$ for the Polyakov correction, Theorem 5.1 extends to any metric in the class:

> **Corollary 5.4 (Polyakov via loop measure).** For $g=e^{2\sigma}g_{\mathrm{hyp}}$ any smooth metric in the conformal class of a closed hyperbolic $X$,
> $$\log\det_\zeta\Delta_X=P_X(\sigma)+\operatorname{Area}(X)E-C-\!\!\sum_{\gamma\in\mathcal G(X)\setminus\mathcal P_X}\!\!\mu_X(C_X(\gamma))-\int_0^\infty\frac{1}{e^R-1}\,d\big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\big),$$
> equivalently (via the $\kappa\to0$ limit) $\log\det_\zeta\Delta_X=P_X(\sigma)+\operatorname{Area}(X)E+\log Z_X'(1)$.

Stub: [[Cor - Polyakov Formula via Brownian Loop Measure]]. So the determinant for *any* metric is the loop-measure value on the hyperbolic representative plus the explicit local Polyakov correction — a clean split of spectral information (loops/geodesics) from conformal information ($\sigma$).

---

## §5.2 — The finite-area (cusped) case

For a non-compact finite-area surface the construction breaks: $\Delta_X$ has continuous spectrum $[\frac14,\infty)$ (one band per cusp, generalised eigenfunctions the **Eisenstein series**), so $e^{-t\Delta_X}$ is not trace-class and there is no eigenvalue sum to zeta-regularise. The fix is a **renormalised determinant** ${\det}_0\Delta_X$.

> [!recall]- Renormalised trace and 0-determinant (cusped case)
> **Formally:** using Melrose's compactification $\bar X$ with boundary defining function $x$, the renormalised integral $^{0}\!\int_X f:=\operatorname{FP}_{z=0}\int_X x^z f$ (finite part) defines the **$0$-trace** $^{0}\!\operatorname{Tr}(e^{-t\Delta_X})=\,^{0}\!\int_X p(t,z,z)\,d\!\operatorname{vol}_g$; then $\zeta^0_X(s)=\Gamma(s)^{-1}\int_0^\infty t^{s-1}(^{0}\!\operatorname{Tr}(e^{-t\Delta_X})-P)\,dt$ and ${\det}_0\Delta_X:=e^{-(\zeta^0_X)'(0)}$. On a closed surface this is $\det_\zeta\Delta_X$. See [[Def - Zeta-Regularised Determinant of the Laplacian]].
> **In words:** subtract the (explicitly known) cusp divergence from the heat trace before zeta-regularising; the leftover finite part is the determinant.

> [!cite]- External input — Borthwick–Judge–Perry determinant formula (Theorem 5.5)
> **Statement (typed):** for a geometrically finite hyperbolic surface with $n_C$ cusps and $\chi=\chi(X)$,
> $${\det}_0(\Delta_X-s(1-s))=Z_X(s)\,e^{M+F s(1-s)}\,G_\infty(s)^\chi\Big(\frac{\sqrt2}{\;}\big[2s\sqrt\pi\,(s-\frac12)\big]\,\Gamma(s-\frac12)\Big)^{-n_C},$$
> with $G_\infty(s)=(2\pi)^{-s}\Gamma(s)G(s)^2$ (Barnes $G$), $M=\chi(\frac12\log2\pi-2\zeta_R'(-1)+\frac14)$, $F=-\chi$. Consequently ${\det}_0\Delta_X=C_X Z_X'(1)$ (finite area) or $C_X Z_X(1)$ (infinite area), $C_X=e^M(2\pi)^{-\chi}(\sqrt2\pi)^{-n_C}$.
> **Why it's true:** integrating the resolvent-trace identity $\big(\frac{1}{2s-1}\partial_s\big)^2\log{\det}_0(\Delta_X-s(1-s))=-\,^{0}\!\operatorname{Tr}(R_X(s)^2)$ fixes the determinant up to $e^{M+Fs(1-s)}$; the explicit cusp factors come from the continuous spectrum. **Source:** Borthwick–Judge–Perry. Take on faith; the $Z_X$ factor is the discrete-spectrum content that becomes the loop mass.

**Remark 5.6 (why the derivative $Z_X'(1)$ appears).** The finite-area answer will involve $Z_X'(1)$ rather than $Z_X(1)$ precisely because $0$ lies in the spectrum of $\Delta_X$ when $\operatorname{Area}(X)<\infty$: the eigenvalue $\lambda_0=0$ forces $Z_X$ a **simple zero at $s=1$**, and that zero is divided out when forming ${\det}_0\Delta_X$ (it is $Z_X$'s derivative that survives). In the infinite-area case $0$ is *not* an $L^2$-eigenvalue, $Z_X(1)\ne0$, and no derivative is needed — the parallel remark 5.8 below.

Writing $D_X(s):=\chi\log G_\infty(s)-\log\big[(2s)^{n_C}\pi(s-\frac12)^{n_C/2}\Gamma(s-\frac12)^{n_C}\big]$ and taking $-\log$ of the formula gives $-\log{\det}_0(\Delta_X-s(1-s))=-Fs(1-s)-M-\log Z_X(s)-D_X(s)$. The paper's contribution is again to substitute the loop-mass form of $-\log Z_X$ and take the limit:

> **Theorem 5.7 (determinant via loop measure; finite-area case).** With $M,F,D_X$ as above and $\kappa\ge0$, $s=\frac12+\sqrt{\frac14+\kappa}>1$ (so $s(s-1)=\kappa$, $\Delta_X-s(1-s)=\Delta_X+\kappa$):
> $$-\log{\det}_0(\Delta_X+\kappa)=F\kappa-M+\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X(C_X(\gamma^m))-D_X(s),$$
> and, dividing out the simple zero at $s=1$, the $\kappa\to0^+$ limit gives $\log{\det}_0\Delta_X=M+D_X(1)+\log Z_X'(1)=\log C_X+\log Z_X'(1)$.

> [!note]- Gap-free proof of Theorem 5.7
> **Step 1 — substitute the loop-mass form.** In $-\log{\det}_0(\Delta_X-s(1-s))=-Fs(1-s)-M-\log Z_X(s)-D_X(s)$, use $s(1-s)=-\kappa$ (so $-Fs(1-s)=F\kappa$) and [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] $-\log Z_X(s)=\sum_{\gamma,m}\mu^\kappa_X(C_X(\gamma^m))$. This gives the displayed identity for $-\log{\det}_0(\Delta_X+\kappa)$.
> **Step 2 — the $\kappa\to0$ limit.** Finite area forces $\lambda_0=0\in\operatorname{spec}\Delta_X$, so $Z_X$ has a **simple zero at $s=1$**: $Z_X(s)=Z_X'(1)(s-1)+O((s-1)^2)$, hence $-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1)$. To define $\det_0\Delta_X$ itself we divide out the zero: ${\det}_0\Delta_X:=\lim_{s\to1}\frac{{\det}_0(\Delta_X-s(1-s))}{s(s-1)}$, i.e. subtract $\log(s(s-1))=\log\kappa$ from $\log{\det}_0(\Delta_X-s(1-s))$. As in Theorem 5.1(ii), $s-1=\frac{\kappa}{\sqrt{1/4+\kappa}+1/2}\sim\kappa$, so $-\log(s-1)$ cancels the $-\log\kappa=-\log(s(s-1))$ coming from the division (the surviving pieces: $F\kappa\to0$, $D_X(s)\to D_X(1)$).
> **Step 3 — collect.** The cancellation leaves $\log{\det}_0\Delta_X=M+D_X(1)+\log Z_X'(1)$. With $D_X(1)=-\chi\log(2\pi)-n_C\log(\sqrt2\pi)$ one checks $M+D_X(1)=\log C_X$ (where $C_X=e^M(2\pi)^{-\chi}(\sqrt2\pi)^{-n_C}$), giving $\log{\det}_0\Delta_X=\log C_X+\log Z_X'(1)$. $\blacksquare$

Stub: [[Thm - Determinant via Loop Measure, Finite-Area Case]]. **Remark 5.8 (infinite area).** When $\operatorname{Area}(X)=\infty$, $\delta<1$ and (§4) the total loop mass is *already finite*; $0$ is not an $L^2$-eigenvalue so $Z_X(1)\ne0$ and no derivative/renormalisation is needed — the determinant identity holds directly at $s=1$ (Lemonde–Wang [LW26]). Continue to [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6]], where these finite normalisations become probability measures.

---

## Section verification log (§5)

**Verified.** All four determinant identities of §5 are reproduced with gap-free proofs in the paper's own order: Theorem 5.1(ii) finite-$\kappa$ (the $R_\kappa=O(\kappa)$ bound via $1-e^{-\kappa t}\le\kappa t$ and $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$); Theorem 5.1(ii) as $\kappa\to0$ (the $\log\kappa$/$\log(s-1)$ cancellation against the Selberg zeta's simple zero, with the elementary limit $s-1=\kappa/(\sqrt{1/4+\kappa}+\frac12)\sim\kappa$); Theorem 5.1(i) Brownian (the primitive/non-primitive split, the non-primitive part evaluated in closed form to $\sum_{m\ge2}\frac1m\frac1{e^{m\ell_\gamma}-1}$ via the §3.1.1 Gaussian identity, and the constant $C=-\gamma_{\mathrm{EM}}+C_1$); Theorem 5.1(iii) $\alpha$-stable ($\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$); and Theorem 5.7 finite-area (same $\kappa\to0$ cancellation).
**Flagged / uncertain.** ⚠️ The factor-of-2 bookkeeping between the constant $E$ and the D'Hoker–Phong exponent (Remark 5.2) was not fully reconciled — the identity is stated as the paper gives it. The one internal step taken on faith is the inner $t$-integral evaluation of the primitive part in Theorem 5.1(i) — the error-function collapse to $\frac1{e^R-1}$ — which the paper itself imports from Wang–Xue [WX25, (4.13)–(4.16)]; cited as an external input rather than re-derived.
**Intuition not yet formalised.** The heat-trace-to-loop-mass identification ($S_X(t)/t$ integrated $=$ loop mass) is stated via the Selberg trace formula (external input), not re-derived. The Selberg trace formula, Naud's formula, refined prime geodesic theorem, Polyakov's formula, and the Borthwick–Judge–Perry determinant formula are all external inputs, stated + typed + cited, not proved (they are beyond the undergraduate floor and beyond what the paper itself proves).
