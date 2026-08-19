---
type: theorem
subject: spectral-geometry
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
  - "Thm - Prime Geodesic Theorem"
  - "Thm - Mass of a Subordinate Brownian Loop Class"
tags: [paper, brownian-loops, zeta-functions, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 5.1"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a **closed** (compact, no boundary, no cusps) hyperbolic surface of genus $g \ge 2$; $\operatorname{Area}(X) = 4\pi(g - 1)$ by Gauss–Bonnet.
- $\Delta_X$ — the positive Laplace–Beltrami operator; discrete spectrum $0 = \lambda_0 < \lambda_1 \le \lambda_2 \le \cdots \to \infty$; $\det_\zeta\Delta_X$ excludes the zero mode.
- $\mathcal P_X$ — the primitive oriented closed geodesics of $X$; $\mathcal G(X) = \{\gamma^m : \gamma \in \mathcal P_X, m \ge 1\}$ all oriented closed geodesics, primitive or not.
- $\ell_\gamma > 0$ — the length of primitive geodesic $\gamma$; $L := m\ell_\gamma$ the length of $\gamma^m$.
- $C_X(\gamma^m)$ — the free homotopy class winding $m$ times around $\gamma$.
- $\phi$ — a Bernstein function; the four paper cases are $\phi = \lambda$ (Brownian, case (i)), $\phi = \lambda + \kappa$ ($\kappa > 0$, killed, case (ii)), $\phi = \lambda^{\alpha/2}$ ($\alpha \in (0, 2)$, $\alpha$-stable, case (iii)).
- $\mu^\phi_X$ — the $\phi$-subordinate loop measure on $X$; $\mu_X = \mu^\lambda_X$ the plain Brownian loop measure; $\mu^\kappa_X = \mu^{\lambda + \kappa}_X$ the killed version.
- $\kappa \ge 0$ — a killing rate; $s := \frac12 + \sqrt{\frac14 + \kappa}$ the associated spectral parameter, with $s = 1 \Leftrightarrow \kappa = 0$.
- $Z_X(s)$ — the Selberg zeta function; on a closed surface, $Z_X(s) = Z_X'(1)(s - 1) + O((s-1)^2)$ near $s = 1$.
- $N_X(R) := \#\{\gamma \in \mathcal P_X : \ell_\gamma \le R\}$ — the primitive geodesic counting function.
- $E := \frac{1}{4\pi}\!\left(4\zeta_R'(-1) - \frac12 + \log 2\pi\right) \approx 0.0538$ — the universal Naud constant (the "area density" of $\log\det_\zeta\Delta$).
- $C$ — a universal constant appearing only in case (i); explicitly $C = -\gamma_{\mathrm{EM}} + C_1$ with $\gamma_{\mathrm{EM}} \approx 0.5772$ the Euler–Mascheroni constant and $C_1$ the universal integration constant of case (i)'s Step 3.
- $\widetilde{\mathrm{Li}}(x) := \int_2^x \frac{du}{\log u}$ — the **cutoff logarithmic integral**; the standard $\operatorname{Li}(x)$ with the singular lower endpoint replaced by $2$ so the integral is convergent as written; $\widetilde{\mathrm{Li}}(x) \sim x/\log x$ as $x \to \infty$.
- $S_X(t) := \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell_\gamma\,e^{-(m\ell_\gamma)^2/4t}}{2\sinh(m\ell_\gamma/2)}$ — Naud's **geodesic heat-trace term** (the length-spectrum part of the trace formula); exponentially small as $t \to 0$, tends to $1$ as $t \to \infty$.
- $S^p_X(t) := \sum_{\gamma \in \mathcal P_X}\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell_\gamma\,e^{-\ell_\gamma^2/4t}}{2\sinh(\ell_\gamma/2)}$ — the **primitive part** of Naud's term (only $m = 1$).
- $E_1(\kappa) := \int_1^\infty t^{-1} e^{-\kappa t}\,dt$ — the exponential integral function; $E_1(\kappa) = -\gamma_{\mathrm{EM}} - \log\kappa + O(\kappa)$ as $\kappa \to 0^+$.

> [!recall]- Zeta-regularised determinant of the Laplacian
> **Formally:** for a closed surface with Laplace eigenvalues $0=\lambda_0<\lambda_1\le\lambda_2\le\cdots\to\infty$, the spectral zeta function is $\zeta_X(s):=\sum_{j\ge1}\lambda_j^{-s}$ (convergent for $\operatorname{Re}s>1$). It equals the Mellin transform $\Gamma(s)^{-1}\int_0^\infty t^{s-1}(\operatorname{Tr}e^{-t\Delta_X}-1)\,dt$, continues meromorphically to $\mathbb C$, is regular at $s=0$, and $\log\det_\zeta\Delta_X:=-\zeta_X'(0)$.
> **In words:** you want $\prod_{j\ge1}\lambda_j$, but this product is infinite. The zeta-regularised determinant is a finite, canonical stand-in: use $\log\prod_j\lambda_j = \sum_j\log\lambda_j = -\zeta'(0)$ formally, and take the analytic continuation of $-\zeta'(0)$ as the definition. Reduces to the ordinary product when there are finitely many eigenvalues.
> **Concretely:** for three eigenvalues $1, 2, 3$: $\zeta(s) = 1 + 2^{-s} + 3^{-s}$; $-\zeta'(0) = \log 6$; $\det_\zeta = 6 = 1\cdot 2\cdot 3$. On the flat torus $T^2 = \mathbb R^2/(2\pi\mathbb Z)^2$, $\det_\zeta\Delta$ is a finite Jacobi-theta-product number. See [[Def - Zeta-Regularised Determinant of the Laplacian]].

> [!recall]- Hyperbolic surface $X = \Gamma\backslash\mathbb H^2$ (closed case)
> **Formally:** $\mathbb H^2 = \{x + iy : y > 0\}$ with metric $ds^2 = (dx^2 + dy^2)/y^2$; $\Gamma \subset \mathrm{PSL}(2, \mathbb R)$ a discrete torsion-free subgroup with **compact quotient** (a *cocompact* Fuchsian group); $X = \Gamma\backslash\mathbb H^2$ is a closed hyperbolic surface of genus $g \ge 2$ with $K \equiv -1$ and $\operatorname{Area}(X) = 4\pi(g - 1)$.
> **In words:** the upper half-plane with a curved ruler, quotiented by a discrete group whose fundamental region is a compact hyperbolic polygon (with sides identified). The result is a compact surface of constant negative curvature, like a "many-holed pretzel" made hyperbolic.
> **Concretely:** a genus-$2$ closed hyperbolic surface has area $4\pi$, systole (shortest closed geodesic) bounded below by a positive constant; every free homotopy class contains a unique closed geodesic of definite positive length. See [[Def - Fuchsian Group and the Hyperbolic Quotient Surface]].

> [!recall]- Brownian loop measure with killing $\mu^\kappa_X$
> **Formally:** for $\kappa \ge 0$, the killing-$\kappa$ Brownian loop measure on $X$ is the loop measure of the semigroup $e^{-t(\Delta_X + \kappa)} = e^{-\kappa t}\,e^{-t\Delta_X}$; equivalently its heat kernel is $p^\kappa_X(t, z, w) = e^{-\kappa t}\,p_X(t, z, w)$, weighting Brownian bridges by the survival factor $e^{-\kappa t}$. Extended to $\kappa \ge -\frac14$ analytically.
> **In words:** ordinary Brownian loop measure tilted by a time-decay $e^{-\kappa t}$: longer loops are penalised more. Corresponds to the Schrödinger operator $\Delta_X + \kappa$ (constant potential $\kappa$).
> **Concretely:** at $\kappa = 0$, no killing — plain Brownian; at $\kappa = 1$, loops of duration $\sim 1$ are damped by $e^{-1} \approx 0.37$. See [[Def - Subordinate Brownian Loop Measure]] and [[Ex - The Subordinate Form of Brownian Motion with Killing]].

> [!recall]- Selberg zeta $Z_X(s)$: simple zero at $s = 1$ on a closed surface
> **Formally:** $Z_X(s) := \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ for $\operatorname{Re}s > 1$; log-expansion $-\log Z_X(s) = \sum_\gamma \sum_{m \ge 1}\frac{1}{m}\frac{e^{-sm\ell_\gamma}}{1 - e^{-m\ell_\gamma}}$. Continues meromorphically to $\mathbb C$; on a closed surface, $\lambda_0 = 0$ forces a **simple zero at $s = 1$**: $Z_X(s) = Z_X'(1)(s - 1) + O((s - 1)^2)$, with $Z_X'(1) > 0$ finite.
> **In words:** a "prime-power" product over closed geodesics, generating the length spectrum. Its zeros encode the discrete Laplace spectrum; the zero eigenvalue produces the simple zero at $s = 1$.
> **Concretely:** near $s = 1$, $-\log Z_X(s) = -\log Z_X'(1) - \log(s - 1) + O(s - 1)$; the $-\log(s - 1) \to +\infty$ as $s \to 1$ is the source of the total loop mass divergence on a closed surface. See [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Spectral parameter $s(\kappa) = \frac12 + \sqrt{\frac14 + \kappa}$
> **Formally:** the map $\kappa \mapsto s$ solving $s(s - 1) = \kappa$ (with the branch $s \ge \frac12$) is $s(\kappa) = \frac12 + \sqrt{\frac14 + \kappa}$. Real for $\kappa \ge -\frac14$; $s(0) = 1$, $s(\kappa) \to \infty$ as $\kappa \to \infty$; and near $\kappa = 0$, $s - 1 = \kappa / (\sqrt{1/4 + \kappa} + 1/2) \sim \kappa$.
> **In words:** the killing rate $\kappa$ and the zeta variable $s$ are two coordinates on the same parameter; the map converts $\sqrt{1/4 + \kappa}$ to $s - 1/2$, aligning the killed loop-mass exponent with the Selberg zeta variable.
> **Concretely:** $\kappa = 0 \Leftrightarrow s = 1$ (the critical point); $\kappa = 2 \Leftrightarrow s = 2$. The equivalence $s - 1 \sim \kappa$ as $\kappa \to 0^+$ is the elementary limit used repeatedly in the killed proof. See [[Remark - The Range of the Killing Parameter]].

---

# Statement

> **Theorem (determinant as a renormalised loop mass, compact case; Belyaev–Huseynli Theorem 5.1).** Let $X = \Gamma\backslash\mathbb H^2$ be a closed hyperbolic surface of genus $g \ge 2$. With $\det_\zeta\Delta_X$ (zero mode excluded), $E$ the Naud constant, $C$ a universal constant, and $\widetilde{\mathrm{Li}}$ the cutoff logarithmic integral as above:
>
> **(i) Brownian case ($\phi = \lambda$):**
> $$-\log\det_\zeta\Delta_X \;=\; -\operatorname{Area}(X)\,E + C + \!\!\!\sum_{\gamma \in \mathcal G(X) \setminus \mathcal P_X}\!\!\!\mu_X\big(C_X(\gamma)\big) + \int_0^\infty\frac{1}{e^R - 1}\,d\!\big(N_X(R) - \widetilde{\mathrm{Li}}(e^R)\big).$$
>
> **(ii) Killing case ($\phi = \lambda + \kappa$, $\kappa > 0$):**
> $$-\log\det_\zeta\Delta_X \;=\; -\operatorname{Area}(X)\,E + \log\kappa + \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu^\kappa_X\big(C_X(\gamma^m)\big) + O(\kappa)$$
> $$\;=\; -\operatorname{Area}(X)\,E + \log\kappa - \log Z_X\!\big(\frac12 + \sqrt{\frac14 + \kappa}\big) + O(\kappa),$$
> and, letting $\kappa \to 0^+$,
> $$\log\det_\zeta\Delta_X \;=\; \operatorname{Area}(X)\,E + \log Z_X'(1).$$
>
> **(iii) $\alpha$-stable case ($\phi = \lambda^{\alpha/2}$, $\alpha \in (0, 2)$):** the analogue of (i) for the *spectral fractional Laplacian* $\Delta_X^{\alpha/2}$, obtained by scaling the geometric terms by $\alpha/2$:
> $$-\log\det_\zeta\Delta_X^{\alpha/2} \;=\; \frac{\alpha}{2}\Big[-\operatorname{Area}(X)\,E + C + \!\!\!\sum_{\gamma \in \mathcal G(X) \setminus \mathcal P_X}\!\!\!\mu_X\big(C_X(\gamma)\big) + \int_0^\infty\!\!\frac{1}{e^R - 1}\,d\!\big(N_X - \widetilde{\mathrm{Li}}(e^R)\big)\Big].$$

---

# In One Line

The **infinite** total Brownian loop mass on a closed hyperbolic surface is renormalised into the **finite** classical spectral invariant $\det_\zeta\Delta_X$: express $-\log\det_\zeta\Delta_X$ via Naud's determinant formula (a length-spectrum sum), reorganise the length-spectrum sum into homotopy-class loop masses (§3), and the killing-rate $\log\kappa$ divergence cancels exactly against the simple zero of the Selberg zeta at $s = 1$.

---

# Why It's True

**Mechanism (one sentence).** *Naud's determinant formula writes $-\log\det_\zeta\Delta_X$ as (a universal $\operatorname{Area}(X)\,E$ term) $+$ (an integral of the length-spectrum heat trace $S_X(t)/t$); the integrand $S_X(t)/t$ is precisely the loop-mass integrand of §3, so the integral **is** a total homotopy-class mass; that total is infinite in the Brownian case, but a $\log\kappa$ counterterm introduced by the killing rate cancels the divergence against the Selberg zeta's simple zero at $s = 1$, leaving the finite $\log\det_\zeta\Delta_X = \operatorname{Area}(X)\,E + \log Z_X'(1)$.*

The three cases are three ways of taming the small-$t$ divergence of $\int S_X(t)/t\,dt$ (equivalently, the divergence of the total loop mass in the contractible/short-loop regime):

- **Case (ii), killed:** insert the survival factor $e^{-\kappa t}$; this shifts $E_1(\kappa) = -\gamma_{\mathrm{EM}} - \log\kappa + O(\kappa)$ into the identity, producing a $\log\kappa$ term that, on the $\kappa \to 0$ limit, is cancelled exactly by the $-\log(s - 1) \sim -\log\kappa$ coming from the Selberg zeta's simple zero at $s = 1$. This is the cleanest case: two logarithms with matching coefficients cancel.

- **Case (i), Brownian:** no killing, no $\log\kappa$ to cancel divergence — instead **renormalise geometrically**, following Wang–Xue. Split Naud's integral into a *non-primitive part* (loops of winding number $m \ge 2$; converges by the geodesic-length lower bound) and a *primitive part* (loops of winding number $m = 1$; the divergent piece). The non-primitive part evaluates in closed form via the §3.1.1 Gaussian identity to a sum of masses of non-primitive classes. The primitive part, evaluated against the geodesic counting measure $dN_X(R)$, is decomposed as (universal constant $C_1$ coming from the smooth $d\widetilde{\mathrm{Li}}(e^R)$ integrated against an error-function kernel) $+$ (finite integral of $1/(e^R - 1)$ against the "excess" measure $d(N_X - \widetilde{\mathrm{Li}}(e^R))$, whose convergence is guaranteed by the refined prime geodesic theorem).

- **Case (iii), $\alpha$-stable:** the spectral fractional Laplacian $\Delta_X^{\alpha/2}$ has eigenvalues $\lambda_j^{\alpha/2}$, so its spectral zeta is $\zeta_{\Delta_X^{\alpha/2}}(s) = \zeta_X(\alpha s / 2)$; differentiating at $s = 0$ gives $\log\det_\zeta\Delta_X^{\alpha/2} = \frac{\alpha}{2}\log\det_\zeta\Delta_X$. Since the $\alpha$-stable loop-class masses are exactly $\frac\alpha 2$ times the Brownian ones ([[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] with $\phi = \lambda^{\alpha/2}$), the whole of case (i) rescales.

---

# Proof

The proofs of the four sub-claims are given below, each in its own collapsible block. Case (ii) finite-$\kappa$ and case (ii) $\kappa \to 0$ are the analytical heart; case (i) is Wang–Xue's geometric renormalisation and is the most involved; case (iii) is a rescaling deduction.

> [!cite]- External input — Selberg trace formula and Naud's determinant expansion
> **Statement (typed):** on a closed hyperbolic surface $X = \Gamma\backslash\mathbb H^2$, the heat trace splits into an *identity* (geometric-area) term and a *geodesic* term,
> $$\sum_{j \ge 0} e^{-t\lambda_j} \;=\; \operatorname{Area}(X)\,\frac{e^{-t/4}}{(4\pi t)^{3/2}}\!\int_0^\infty \frac{r\,e^{-r^2/4t}}{\sinh(r/2)}\,dr \;+\; S_X(t),$$
> and (Naud) $-\log\det_\zeta\Delta_X = -\operatorname{Area}(X)\,E - \gamma_{\mathrm{EM}} + \int_0^1\frac{S_X(t)}{t}\,dt + \int_1^\infty\frac{S_X(t) - 1}{t}\,dt$, with $\gamma_{\mathrm{EM}}$ the Euler–Mascheroni constant, $E$ as above, and $S_X$ as above ($S_X(t)$ exponentially small as $t \to 0$; $S_X(t) - 1$ exponentially small as $t \to \infty$).
> **Why it's true:** the trace formula equates a spectral sum with a sum over the identity and hyperbolic conjugacy classes of $\Gamma$ (i.e. the closed geodesics); feeding it through the Mellin transform / $\zeta'(0)$ machine turns $-\log\det_\zeta$ into an integral of the geodesic term. The identity-class integrand contributes the universal $\operatorname{Area}(X)\,E$ area-density term; the geodesic term contributes the length-spectrum integral.
> **Source.** Selberg, *Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces*, J. Indian Math. Soc. **20** (1956); Naud's compact expansion via [WX25] (F. Naud), used in Wang–Xue *Path integrals and the Selberg zeta function* (2025). Take on faith — the geodesic term $S_X(t)$ is exactly the $t \downarrow 0$ heat-kernel weight of Brownian loops of each length, which is why it re-expresses as a loop mass (see the §3 note [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]).

> [!cite]- External input — refined prime geodesic theorem (closed case)
> **Statement (typed):** for a closed hyperbolic surface ($\delta = 1$), as $R \to \infty$
> $$N_X(R) \;=\; \operatorname{Li}(e^R) \;+\; \!\!\sum_{0 < \lambda_j \le 1/4}\!\operatorname{Li}(e^{s_j R}) \;+\; O_X(e^{3R/4}/R),$$
> where $\operatorname{Li}(x) = \int_2^x du/\log u \sim x/\log x$ and $s_j = \frac12 + \sqrt{\frac14 - \lambda_j} \in [\frac12, 1]$. Consequently $|N_X(R) - \widetilde{\mathrm{Li}}(e^R)| = O_X(e^{(1 - \epsilon)R})$ for some $\epsilon > 0$.
> **Why it's true:** the leading $\operatorname{Li}(e^R)$ is the classical prime geodesic theorem (analogue of PNT for hyperbolic surfaces); small eigenvalues $\lambda_j < 1/4$ contribute extra $\operatorname{Li}(e^{s_j R})$ terms via the corresponding zeros of $Z_X$ off the critical line; the error is controlled by the zero-free region of $Z_X$ (Selberg's spectral theory).
> **Source.** Selberg's zeta and Hejhal's *Selberg trace formula for PSL(2, ℝ)*, vol. I–II (Springer 1976, 1983); used in Wang–Xue via [WX25]. Take on faith — the point for us is the $O(e^{(1-\epsilon)R})$ bound on $N_X - \widetilde{\mathrm{Li}}(e^R)$, which makes the renormalising integral in case (i) converge.

> [!note]- Gap-free proof of case (ii), finite $\kappa$ (the first line of the theorem)
> **Step 0 — set up the killed loop mass as a Mellin integral of the killed heat trace.** The killed heat trace on $X$ is $\operatorname{Tr}(e^{-t(\Delta_X + \kappa)}) = e^{-\kappa t}\sum_{j \ge 0} e^{-t\lambda_j}$; subtracting the $\lambda_0 = 0$ contribution (which is $e^{-\kappa t}$) and applying Naud's decomposition, the geodesic part is $e^{-\kappa t}S_X(t)$. The total killed non-trivial-class mass is therefore
> $$M_\kappa \;:=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; \int_0^\infty e^{-\kappa t}\,\frac{S_X(t)}{t}\,dt$$
> (finite for $\kappa > 0$ because $e^{-\kappa t}$ tames the large-$t$ growth of $S_X$, and $S_X(t)$ is exponentially small as $t \to 0$; no cutoff needed).
>
> **Step 1 — split at $t = 1$ and rearrange to Naud's form.** Split the integral at $t = 1$ and, in the tail $t > 1$, subtract and add back $1$:
> $$M_\kappa \;=\; \int_0^1 e^{-\kappa t}\,\frac{S_X(t)}{t}\,dt \;+\; \int_1^\infty e^{-\kappa t}\,\frac{S_X(t) - 1}{t}\,dt \;+\; E_1(\kappa),$$
> with $E_1(\kappa) := \int_1^\infty e^{-\kappa t}/t\,dt$ the exponential integral. Compare with Naud's identity $\int_0^1 S_X/t\,dt + \int_1^\infty (S_X - 1)/t\,dt$ (i.e. Naud's formula without the killing weight): the difference is exactly the *correction* introduced by the extra factor $e^{-\kappa t}$ in each integrand,
> $$M_\kappa - E_1(\kappa) \;=\; \int_0^1\frac{S_X}{t}\,dt + \int_1^\infty\frac{S_X - 1}{t}\,dt \;-\; R_\kappa,$$
> where $R_\kappa$ is the *correction integral*
> $$R_\kappa \;:=\; \int_0^1 (1 - e^{-\kappa t})\,\frac{S_X(t)}{t}\,dt \;+\; \int_1^\infty (1 - e^{-\kappa t})\,\frac{S_X(t) - 1}{t}\,dt.$$
>
> **Step 2 — bound $|R_\kappa| = O(\kappa)$.** Use the elementary inequality $1 - e^{-\kappa t} \le \kappa t$ (valid for all $t, \kappa \ge 0$): substituting into each integrand,
> $$|R_\kappa| \;\le\; \kappa\int_0^1 S_X(t)\,dt \;+\; \kappa\int_1^\infty |S_X(t) - 1|\,dt \;=\; O(\kappa),$$
> both integrals finite because $S_X(t)$ is exponentially small as $t \to 0^+$ (each geodesic term carries $e^{-\ell_\gamma^2/4t}$ with $\ell_\gamma > 0$) and $|S_X(t) - 1|$ is exponentially small as $t \to \infty$ (dominated by the smallest-eigenvalue heat-trace correction).
>
> **Step 3 — expand $E_1(\kappa)$ near $\kappa = 0$.** The standard asymptotic (from the series $E_1(\kappa) = -\gamma_{\mathrm{EM}} - \log\kappa - \sum_{n \ge 1}(-\kappa)^n/(n\cdot n!)$; see Abramowitz–Stegun §5.1.11) gives $E_1(\kappa) = -\gamma_{\mathrm{EM}} - \log\kappa + O(\kappa)$ as $\kappa \to 0^+$.
>
> **Step 4 — substitute into Naud.** Rearranging Step 1:
> $$\int_0^1\frac{S_X}{t}\,dt + \int_1^\infty\frac{S_X - 1}{t}\,dt \;=\; M_\kappa - E_1(\kappa) + R_\kappa \;=\; M_\kappa + \gamma_{\mathrm{EM}} + \log\kappa + O(\kappa).$$
> Substituting into Naud's identity $-\log\det_\zeta\Delta_X = -\operatorname{Area}(X)\,E - \gamma_{\mathrm{EM}} + \int_0^1 S_X/t\,dt + \int_1^\infty(S_X - 1)/t\,dt$,
> $$-\log\det_\zeta\Delta_X \;=\; -\operatorname{Area}(X)\,E - \gamma_{\mathrm{EM}} + M_\kappa + \gamma_{\mathrm{EM}} + \log\kappa + O(\kappa) \;=\; -\operatorname{Area}(X)\,E + \log\kappa + M_\kappa + O(\kappa).$$
> The two $\gamma_{\mathrm{EM}}$'s cancel exactly — that is the point of the $\gamma_{\mathrm{EM}}$ counterterm in Naud's formula. This is the first line of (ii). $\blacksquare$

> [!note]- Gap-free proof of case (ii) as $\kappa \to 0^+$ (the limit line of the theorem)
> **Step 1 — insert the Selberg zeta identity.** By [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] applied to the killing rate $\kappa$, with $s = s(\kappa) = \frac12 + \sqrt{\frac14 + \kappa}$,
> $$M_\kappa \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; -\log Z_X(s).$$
> Substituting into the first line of (ii),
> $$-\log\det_\zeta\Delta_X \;=\; -\operatorname{Area}(X)\,E + \log\kappa - \log Z_X(s) + O(\kappa),$$
> which is the second line of (ii). All that remains is the $\kappa \to 0$ limit.
>
> **Step 2 — expand $-\log Z_X(s)$ near $s = 1$.** On a closed surface, $\lambda_0 = 0$ is an $L^2$-eigenvalue (constants are integrable on a compact surface), forcing $Z_X$ a **simple zero at $s = 1$**. So $Z_X(s) = Z_X'(1)(s - 1) + O((s - 1)^2)$ with $Z_X'(1) > 0$, giving
> $$-\log Z_X(s) \;=\; -\log Z_X'(1) \;-\; \log(s - 1) \;+\; O(s - 1).$$
>
> **Step 3 — relate $\log(s - 1)$ to $\log\kappa$.** By definition $s = \frac12 + \sqrt{\frac14 + \kappa}$, so
> $$s - 1 \;=\; \sqrt{\frac14 + \kappa} - \frac12 \;=\; \frac{(1/4 + \kappa) - 1/4}{\sqrt{1/4 + \kappa} + 1/2} \;=\; \frac{\kappa}{\sqrt{1/4 + \kappa} + 1/2}.$$
> As $\kappa \to 0^+$, the denominator tends to $1$, so $s - 1 = \kappa\,(1 + O(\kappa)) \sim \kappa$; taking logarithms,
> $$\log(s - 1) \;=\; \log\kappa \;+\; \log(1 + O(\kappa)) \;=\; \log\kappa \;+\; o(1).$$
>
> **Step 4 — cancel and take the limit.** Substituting Step 2 and Step 3 into Step 1's expression,
> $$-\log\det_\zeta\Delta_X \;=\; -\operatorname{Area}(X)\,E + \log\kappa - \log Z_X'(1) - \log(s - 1) + o(1)$$
> $$\;=\; -\operatorname{Area}(X)\,E + \log\kappa - \log Z_X'(1) - \log\kappa + o(1) \;=\; -\operatorname{Area}(X)\,E - \log Z_X'(1) + o(1).$$
> The $\log\kappa$ from the killing counterterm cancels **exactly** the $-\log\kappa$ from the Selberg zeta's simple zero. Taking $\kappa \to 0^+$, the $o(1)$ vanishes and, negating,
> $$\log\det_\zeta\Delta_X \;=\; \operatorname{Area}(X)\,E + \log Z_X'(1). \qquad \blacksquare$$
>
> *This is precisely the classical D'Hoker–Phong determinant formula; see [[Remark - D'Hoker-Phong Determinant Formula|Remark 5.2]] for the identification $\det_\zeta\Delta_X = Z_X'(1)\,e^{(2g - 2)(2\zeta_R'(-1) - 1/4 + \frac12\log 2\pi)}$ and the ⚠️ factor-of-2 flag.*

> [!note]- Gap-free proof of case (i), Brownian ($\kappa = 0$)
> With no killing there is no $\log\kappa$ to absorb the divergence, so the paper renormalises **geometrically**, following Wang–Xue [WX25].
>
> **Step 1 — split Naud's integral into primitive and non-primitive pieces.** Recall the primitive part $S^p_X(t) = \sum_{\gamma \in \mathcal P_X}\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell_\gamma\,e^{-\ell_\gamma^2/4t}}{2\sinh(\ell_\gamma/2)}$ (only the $m = 1$ terms of $S_X$). The non-primitive part is $S_X - S^p_X$. Split Naud's identity as
> $$\int_0^1\frac{S_X}{t}\,dt + \int_1^\infty\frac{S_X - 1}{t}\,dt \;=\; \int_0^\infty\frac{S_X - S^p_X}{t}\,dt \;+\; \int_0^1\frac{S^p_X}{t}\,dt + \int_1^\infty\frac{S^p_X - 1}{t}\,dt.$$
> (The rearrangement is legal because the LHS and RHS are equal Lebesgue integrands rearranged: cancel $\int_0^1 S^p_X/t$ from both sides, note $\int_1^\infty (S_X - S^p_X)/t = \int_1^\infty (S_X - 1)/t - \int_1^\infty (S^p_X - 1)/t$, and the $-1$'s match because the same "1" appears on both sides.) The point is that $\int_0^\infty (S_X - S^p_X)/t\,dt$ converges as a full integral over $(0, \infty)$ (all $m \ge 2$ terms carry $e^{-(m\ell_\gamma)^2/4t}$ with $m\ell_\gamma \ge 2\ell_{\mathrm{sys}}$, killing the small-$t$ singularity uniformly), so we have isolated the divergent piece into the primitive integrals.
>
> **Step 2 — the non-primitive part in closed form.** For each $\gamma \in \mathcal P_X$ and $m \ge 2$, the inner $t$-integral of the $(\gamma, m)$ term of $S_X - S^p_X$ is
> $$\int_0^\infty\frac{1}{t}\cdot\frac{e^{-t/4}}{(4\pi t)^{1/2}}\cdot\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}\cdot e^{-(m\ell_\gamma)^2/4t}\,dt.$$
> Pulling constants out and applying the Gaussian-type identity $\int_0^\infty s^{-3/2}e^{-as - b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ (with $a = 1/4$, $b = (m\ell_\gamma)^2/4$, so $2\sqrt{ab} = m\ell_\gamma/2$ and $\sqrt{\pi/b} = 2\sqrt\pi/(m\ell_\gamma)$; the same identity underpins the §3.1.1 loop-length integral),
> $$= \;\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}\cdot\frac{1}{(4\pi)^{1/2}}\cdot\frac{2\sqrt\pi}{m\ell_\gamma}\cdot e^{-m\ell_\gamma/2} \;=\; \frac{1}{m\cdot 2\sinh(m\ell_\gamma/2)}\cdot e^{-m\ell_\gamma/2}.$$
> Expanding $2\sinh(m\ell_\gamma/2) = e^{m\ell_\gamma/2} - e^{-m\ell_\gamma/2}$ and factoring $e^{m\ell_\gamma/2}$ out of the denominator gives $\frac{e^{-m\ell_\gamma/2}}{e^{m\ell_\gamma/2} - e^{-m\ell_\gamma/2}} = \frac{1}{e^{m\ell_\gamma} - 1}$; so the $(\gamma, m)$ term equals $\frac{1}{m}\cdot\frac{1}{e^{m\ell_\gamma} - 1}$. Summing over $m \ge 2$ and $\gamma$,
> $$\int_0^\infty\frac{S_X - S^p_X}{t}\,dt \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 2}\frac{1}{m}\cdot\frac{1}{e^{m\ell_\gamma} - 1} \;=\;\!\!\! \sum_{\gamma \in \mathcal G(X)\setminus\mathcal P_X}\!\!\!\mu_X\big(C_X(\gamma)\big),$$
> the sum of Brownian loop masses over *non-primitive* closed geodesics (using [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] at $\kappa = 0$: $\mu_X(C_X(\gamma^m)) = 1/(m(e^{m\ell_\gamma} - 1))$; the $m \ge 2$ terms are exactly the non-primitive classes).
>
> **Step 3 — the primitive part, renormalised.** Rewrite $S^p_X(t)$ as an integral against the primitive-geodesic counting measure $dN_X(R)$ (so a geodesic of length $\ell_\gamma$ contributes a Dirac spike at $R = \ell_\gamma$):
> $$S^p_X(t) \;=\; \int_0^\infty\frac{e^{-t/4}}{(4\pi t)^{1/2}}\,\frac{R\,e^{-R^2/4t}}{2\sinh(R/2)}\,dN_X(R).$$
> Substitute into $\int_0^1 S^p_X/t\,dt + \int_1^\infty (S^p_X - 1)/t\,dt$, exchange the order of integration (legal by Tonelli after checking positivity + absolute convergence), and evaluate the *inner* $t$-integrals in error-function form.
>
> > [!cite]- External input — the inner $t$-integral evaluation (Wang–Xue [WX25], eqs. (4.13)–(4.16))
> > After the change of order, the inner $t$-integrals against $\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{R e^{-R^2/4t}}{2\sinh(R/2)}$ evaluate to expressions in $\operatorname{erf}(\cdot)$ / $\operatorname{erfc}(\cdot)$ (the standard Gaussian error and complementary error functions). Decomposing the outer measure $dN_X(R)$ as $dN_X(R) = d\widetilde{\mathrm{Li}}(e^R) + d(N_X(R) - \widetilde{\mathrm{Li}}(e^R))$:
> > - The **$d\widetilde{\mathrm{Li}}(e^R)$ part** is $X$-independent (it depends only on the smooth model function $\widetilde{\mathrm{Li}}(e^R)$, not on which surface $X$) and, after the $t$-integral is evaluated, contributes a **universal constant** $C_1$.
> > - The **$d(N_X(R) - \widetilde{\mathrm{Li}}(e^R))$ part**'s error-function-expression $t$-integral, on integration against $R$, **collapses to** $\frac{1}{e^R - 1}$, giving $\int_0^\infty \frac{1}{e^R - 1}\,d(N_X(R) - \widetilde{\mathrm{Li}}(e^R))$; this integral converges by the refined prime geodesic theorem's bound $|N_X - \widetilde{\mathrm{Li}}(e^R)| = O_X(e^{(1-\epsilon)R})$, which after integration by parts controls the tail against the $e^{-R}$ decay of $1/(e^R - 1)$.
> > **Source.** Wang–Xue [WX25], Eqs. (4.13)–(4.16); the calculation is a definite-integral evaluation (change of variables + integration by parts on the error-function primitive), **taken on faith** here.
>
> Combining, $\int_0^1 S^p_X/t\,dt + \int_1^\infty (S^p_X - 1)/t\,dt = C_1 + \int_0^\infty\frac{1}{e^R - 1}\,d(N_X(R) - \widetilde{\mathrm{Li}}(e^R))$.
>
> **Step 4 — assemble.** Substituting Steps 2 and 3 into the split of Step 1,
> $$\int_0^1\frac{S_X}{t}\,dt + \int_1^\infty\frac{S_X - 1}{t}\,dt \;=\; \sum_{\gamma \in \mathcal G(X)\setminus\mathcal P_X}\!\!\mu_X(C_X(\gamma)) \;+\; C_1 \;+\; \int_0^\infty\frac{1}{e^R - 1}\,d(N_X - \widetilde{\mathrm{Li}}(e^R)).$$
> Plugging into Naud's identity $-\log\det_\zeta\Delta_X = -\operatorname{Area}(X)\,E - \gamma_{\mathrm{EM}} + \int_0^1 S_X/t + \int_1^\infty (S_X - 1)/t$ and setting $C := -\gamma_{\mathrm{EM}} + C_1$,
> $$-\log\det_\zeta\Delta_X \;=\; -\operatorname{Area}(X)\,E + C + \!\!\sum_{\gamma \in \mathcal G(X)\setminus\mathcal P_X}\!\!\mu_X(C_X(\gamma)) + \int_0^\infty\frac{1}{e^R - 1}\,d(N_X - \widetilde{\mathrm{Li}}(e^R)). \quad \blacksquare$$

> [!note]- Gap-free proof of case (iii), $\alpha$-stable
> **Step 1 — spectral zeta of $\Delta_X^{\alpha/2}$.** The spectral fractional Laplacian $\Delta_X^{\alpha/2}$ is defined by functional calculus: it has the same eigenfunctions as $\Delta_X$, with eigenvalues $\lambda_j^{\alpha/2}$. Its spectral zeta function is therefore
> $$\zeta_{\Delta_X^{\alpha/2}}(s) \;=\; \sum_{j \ge 1}(\lambda_j^{\alpha/2})^{-s} \;=\; \sum_{j \ge 1}\lambda_j^{-\alpha s / 2} \;=\; \zeta_X(\alpha s / 2).$$
>
> **Step 2 — differentiate at $s = 0$.** By the chain rule, $\frac{d}{ds}\zeta_X(\alpha s / 2)\big|_{s = 0} = \frac{\alpha}{2}\,\zeta_X'(0)$; therefore
> $$\log\det_\zeta\Delta_X^{\alpha/2} \;=\; -\zeta_{\Delta_X^{\alpha/2}}'(0) \;=\; -\frac{\alpha}{2}\,\zeta_X'(0) \;=\; \frac{\alpha}{2}\log\det_\zeta\Delta_X.$$
>
> **Step 3 — assemble case (i) and rescale.** On the loop-mass side, [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] with $\phi = \lambda^{\alpha/2}$ gives $\mu^\alpha_X(C_X(\gamma^m)) = (\alpha/2)\,\mu_X(C_X(\gamma^m))$ for every non-trivial class: the $\alpha$-stable class-mass is exactly $\alpha/2$ times the Brownian class-mass. So multiplying case (i)'s identity by $\alpha/2$,
> $$-\frac{\alpha}{2}\log\det_\zeta\Delta_X \;=\; \frac{\alpha}{2}\Big[-\operatorname{Area}(X)\,E + C + \!\!\sum_{\gamma \in \mathcal G(X)\setminus\mathcal P_X}\!\!\mu_X(C_X(\gamma)) + \int_0^\infty\!\frac{d(N_X - \widetilde{\mathrm{Li}}(e^R))}{e^R - 1}\Big],$$
> and by Step 2 the LHS equals $-\log\det_\zeta\Delta_X^{\alpha/2}$. Rearranging gives the theorem's (iii). $\blacksquare$

---

# Where the paper uses this

Central result of [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.1]] — the compact-case determinant identity that turns the paper's Brownian loops into a spectral invariant. Combined with [[Thm - Polyakov Conformal Anomaly Formula|Polyakov's formula (Theorem 5.3)]] to give [[Cor - Polyakov Formula via Brownian Loop Measure|Corollary 5.4]] (any-metric version). Reappears in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6]] as the finite normalising constant that turns the renormalised loop measure into a probability measure on homotopy classes. See also [[Remark - D'Hoker-Phong Determinant Formula|Remark 5.2]] for the identification with the classical D'Hoker–Phong formula (and its ⚠️ flag).
