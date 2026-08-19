---
type: remark
subject: probability-geometry
prereqs:
  - "Lemma - Wang-Xue Strip Integral"
  - "Thm - Mass of a Subordinate Brownian Loop Class"
  - "Thm - Mass of a Free Homotopy Class"
  - "Def - Subordinate Brownian Loop Measure"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
tags: [paper, brownian-loops, spectral-geometry, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §5.1 — Naud's geodesic heat-trace integrand is the loop-mass integrand of §3"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a **closed** hyperbolic surface (genus $g \ge 2$, no boundary, no cusps).
- $\mathcal P_X$ — the primitive oriented closed geodesics of $X$; $\ell_\gamma > 0$ the length of $\gamma \in \mathcal P_X$.
- $L := m\ell_\gamma$ — the translation length of $\gamma^m$ (for $m \ge 1$).
- $\tau \in \Gamma$ — a primitive hyperbolic representative of $\gamma$, standardised so $\tau : z \mapsto e^{\ell_\gamma} z$.
- $\mathcal F_\tau = \{z \in \mathbb H^2 : 1 \le \operatorname{Im} z < e^{\ell_\gamma}\}$ — the fundamental strip of $\langle \tau\rangle$.
- $p_{\mathbb H^2}(s, z, w)$ — the Brownian heat kernel on $\mathbb H^2$; depends only on the hyperbolic distance $d_{\mathbb H^2}(z, w)$.
- $C_X(\gamma^m)$ — the free homotopy class of loops on $X$ that wind $m$ times around $\gamma$.
- $\mu_X$ — the Brownian loop measure on $X$; $\mu^\kappa_X$ its killing-$\kappa$ variant, with heat kernel $e^{-\kappa t}p_X(t, z, w)$.
- $S_X(t)$ — **Naud's geodesic heat-trace term**, the length-spectrum part of the Selberg trace formula:
  $$S_X(t) \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\frac{e^{-t/4}}{(4\pi t)^{1/2}}\,\frac{\ell_\gamma\,e^{-(m\ell_\gamma)^2/(4t)}}{2\sinh(m\ell_\gamma/2)}.$$
- $V_\phi(ds)$ — the weighted potential measure of a Bernstein function $\phi$; for $\phi(\lambda) = \lambda$, $V_\phi = ds/s$; for $\phi(\lambda) = \lambda + \kappa$, $V_\phi = e^{-\kappa s}\,ds/s$.

> [!recall]- Brownian heat kernel on $\mathbb H^2$
> **Formally:** the transition density $p_{\mathbb H^2}(s, z, w)$ of Brownian motion on $\mathbb H^2$ (semigroup $e^{-s\Delta_{\mathbb H^2}}$, positive Laplacian) is a function of $s > 0$ and $r = d_{\mathbb H^2}(z, w)$ only:
> $$p_{\mathbb H^2}(s, r) \;=\; \frac{\sqrt 2\,e^{-s/4}}{(4\pi s)^{3/2}}\int_r^\infty\frac{u\,e^{-u^2/(4s)}}{\sqrt{\cosh u - \cosh r}}\,du.$$
> **In words:** the return-probability density of hyperbolic Brownian motion. Depends only on distance because $\mathbb H^2$ is homogeneous and isotropic. The factor $e^{-s/4}$ is the spectral-bottom correction from negative curvature: the bottom of $\operatorname{spec}\Delta_{\mathbb H^2}$ on $L^2$ is $1/4 = (1/2)^2$.
> **Concretely:** at short $s$ and small $r$, $p_{\mathbb H^2}(s, r) \sim (4\pi s)^{-1}e^{-r^2/(4s)}$ — the flat-plane Gaussian, since $\mathbb H^2$ and $\mathbb R^2$ agree infinitesimally. Full detail: [[Def - Heat Kernel and Heat Semigroup]].

> [!recall]- Wang–Xue strip integral (Lemma 3.4)
> **Formally:** for $\tau : z \mapsto e^{\ell_\gamma} z$, $m \ge 1$, $L = m\ell_\gamma$, and every $s > 0$:
> $$\int_{\mathcal F_\tau} p_{\mathbb H^2}(s, z, \tau^m z)\,d\rho_{\mathbb H^2}(z) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}.$$
> **In words:** the strip integral of the $\mathbb H^2$ heat kernel from $z$ to its $\tau^m$-translate factors into a *geometric* width $\ell_\gamma/[2\sinh(L/2)]$ and a *1-D-Gaussian-in-$L$* piece $e^{-s/4}e^{-L^2/(4s)}/(2\sqrt{\pi s})$ (the on-axis Brownian bridge cost of translating by hyperbolic distance $L$, times the spectral-bottom correction).
> **Concretely:** at $L = \log 2$, $s = 1$: strip integral $\approx (\log 2)/(2\sinh(\log 2/2))\cdot e^{-1/4}e^{-(\log 2)^2/4}/(2\sqrt\pi) \approx 0.187$. Full detail: [[Lemma - Wang-Xue Strip Integral]].

> [!recall]- Mass of a free homotopy class $C_X(\gamma^m)$ under a subordinate loop measure (Theorem 3.5)
> **Formally:** for a Bernstein function $\phi$ with weighted potential measure $V_\phi$, and $L = m\ell_\gamma$,
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty \frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds).$$
> **In words:** the mass of one homotopy class is a single 1-D integral in the internal-clock variable $s$; the geometry enters only via $L$, and $\phi$ enters only via $V_\phi$.
> **Concretely:** for $\phi = \lambda$ (Brownian), $V_\phi = ds/s$, so $\mu_X(C_X(\gamma^m)) = \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}\cdot\frac{ds}{s} = \frac{1}{m}\cdot\frac{1}{e^L - 1}$; for $\phi = \lambda + \kappa$ (killed), $V_\phi = e^{-\kappa s}\,ds/s$ inserts a factor $e^{-\kappa s}$ inside the integral. Full detail: [[Thm - Mass of a Subordinate Brownian Loop Class]].

> [!recall]- Selberg trace formula, geodesic part
> **Formally:** on a closed hyperbolic $X$, the heat trace splits as
> $$\sum_{j \ge 0}e^{-t\lambda_j} \;=\; \operatorname{Area}(X)\,\frac{e^{-t/4}}{(4\pi t)^{3/2}}\int_0^\infty\frac{r\,e^{-r^2/4t}}{\sinh(r/2)}\,dr \;+\; S_X(t),$$
> the first summand being the *identity* (area-density) contribution and the second the geodesic contribution over primitive geodesics and their windings.
> **In words:** the heat trace on $X$ decomposes into a "smooth" area piece (comes from the identity element of $\Gamma$) and a "length-spectrum" piece $S_X(t)$ that sums a Gaussian-weighted contribution over every closed geodesic.
> **Concretely:** at large $t$, $S_X(t) \to 1$ (the $\lambda_0 = 0$ eigenvalue dominates the LHS, and the identity term decays); at small $t$, $S_X(t)$ is exponentially small (every $(\gamma, m)$ term carries $e^{-L^2/4t}$ with $L > 0$). Full detail: cited as external input in [[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]]'s proof.

---

# Claim / Identity

> **Claim (Naud's geodesic term is the total loop-mass integrand).** With notation as above:
>
> **(1) Term-by-term.** For every $\gamma \in \mathcal P_X$, every $m \ge 1$, and every $\kappa \ge 0$,
> $$\int_0^\infty e^{-\kappa t}\cdot\left[\frac{e^{-t/4}}{(4\pi t)^{1/2}}\,\frac{\ell_\gamma\,e^{-L^2/(4t)}}{2\sinh(L/2)}\right]\frac{dt}{t} \;=\; \mu^\kappa_X\big(C_X(\gamma^m)\big),\qquad L := m\ell_\gamma.$$
> The bracketed factor is exactly the $(\gamma, m)$-term of Naud's $S_X(t)$; the $e^{-\kappa t}$ prefactor is the killing survival factor.
>
> **(2) Summed.** For every $\kappa > 0$, by Fubini (all summands non-negative),
> $$\int_0^\infty e^{-\kappa t}\,\frac{S_X(t)}{t}\,dt \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=:\; M_\kappa.$$
>
> **(3) Brownian ($\kappa = 0$).** Term-by-term the identification still holds; the *non-primitive part* sums absolutely to
> $$\int_0^\infty\frac{S_X(t) - S^p_X(t)}{t}\,dt \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 2}\frac{1}{m}\cdot\frac{1}{e^{m\ell_\gamma} - 1} \;=\; \sum_{\gamma \in \mathcal G(X)\setminus\mathcal P_X}\mu_X\big(C_X(\gamma)\big),$$
> and the *primitive part* $\int_0^\infty S^p_X(t)/t\,dt$ (with $S^p_X$ the $m = 1$ subsum) is the divergent piece that must be renormalised by the prime geodesic theorem.

---

# In One Line

Naud's length-spectrum integrand $S_X(t)/t$ is not merely *reminiscent* of a loop-mass integrand — it *is* one, term for term: the $(\gamma, m)$-term of $S_X(t)/t$ integrated over $t \in (0, \infty)$ against $e^{-\kappa t}$ is exactly the killed Brownian loop mass of the class $C_X(\gamma^m)$. This is the load-bearing identification that turns Naud's determinant expansion into a total loop-mass identity, and it is the whole reason §5 exists as a chapter on renormalising Brownian loops.

---

# Why It's True

**Mechanism (one sentence).** *The $(\gamma, m)$-term of $S_X(t)$, divided by $t$, is (algebraically) the Wang–Xue strip integral of the $\mathbb H^2$ heat kernel across $\tau^m$ with subordination variable $s := t$; feeding this into Theorem 3.5 with $\phi = \lambda + \kappa$ (weighted potential measure $V_\phi = e^{-\kappa s}\,ds/s$) recovers $\mu^\kappa_X(C_X(\gamma^m))$ directly.*

The Selberg trace formula splits the spectral heat trace into an "area" (identity) piece and a "geodesic" piece $S_X$. Wang–Xue's Lemma 3.4 evaluates the strip integral of the $\mathbb H^2$ Brownian kernel across $\tau^m$ in closed form, producing exactly the same shape:
$$\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}.$$
Both are 1-D-Gaussian-in-$L$ objects weighted by a curvature correction $e^{-s/4}$ and a strip width $\ell_\gamma/[2\sinh(L/2)]$. Once the identity is recognised, the $t$-integral of $S_X(t)/t$ *is* the Bernstein-subordinated loop-length integral $I_\phi(L)$ of §3, and summing over $(\gamma, m)$ recovers the total non-trivial loop mass. The whole spectral-to-probabilistic translation in §5 is this one algebraic coincidence, packaged as a load-bearing identity.

---

# Derivation

> [!note]- Gap-free derivation
>
> **Step 1 — write down the $(\gamma, m)$-term of $S_X(t)/t$ with $L = m\ell_\gamma$.** From the definition of $S_X(t)$, the summand for the pair $(\gamma, m)$ is
> $$\left[\frac{S_X(t)}{t}\right]_{(\gamma, m)} \;=\; \frac{1}{t}\cdot\frac{e^{-t/4}}{(4\pi t)^{1/2}}\cdot\frac{\ell_\gamma\,e^{-L^2/(4t)}}{2\sinh(L/2)}.$$
> Regrouping (and using $(4\pi t)^{1/2} = 2\sqrt{\pi t}$),
> $$\left[\frac{S_X(t)}{t}\right]_{(\gamma, m)} \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-t/4}\,e^{-L^2/(4t)}}{2\sqrt{\pi t}}\cdot\frac{1}{t}.$$
>
> **Step 2 — recognise Wang–Xue's strip integral with $s = t$.** By [[Lemma - Wang-Xue Strip Integral|Lemma 3.4]] with subordination variable $s := t$,
> $$\int_{\mathcal F_\tau} p_{\mathbb H^2}(t, z, \tau^m z)\,d\rho_{\mathbb H^2}(z) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-t/4}\,e^{-L^2/(4t)}}{2\sqrt{\pi t}}.$$
> The right-hand side is *exactly* the factor after the last $\frac{1}{t}$ in Step 1. Therefore
> $$\left[\frac{S_X(t)}{t}\right]_{(\gamma, m)} \;=\; \left[\int_{\mathcal F_\tau} p_{\mathbb H^2}(t, z, \tau^m z)\,d\rho_{\mathbb H^2}(z)\right]\cdot\frac{1}{t}.$$
> The $(\gamma, m)$-term of Naud's integrand, divided by $t$, is a **fundamental-strip integral of the $\mathbb H^2$ Brownian kernel across $\tau^m$**, weighted by the loop-measure $1/t$ factor.
>
> **Step 3 — multiply by the killing survival factor $e^{-\kappa t}$ and integrate.** For any $\kappa \ge 0$, multiply the identity of Step 2 by $e^{-\kappa t}$ and integrate over $t \in (0, \infty)$:
> $$\int_0^\infty e^{-\kappa t}\,\left[\frac{S_X(t)}{t}\right]_{(\gamma, m)}\!\!dt \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty \frac{e^{-t/4}\,e^{-L^2/(4t)}}{2\sqrt{\pi t}}\,\frac{e^{-\kappa t}\,dt}{t}.$$
> The right-hand side is the loop-length integral $I_\phi(L)$ for the Bernstein function $\phi(\lambda) = \lambda + \kappa$, whose weighted potential measure is $V_\phi(ds) = e^{-\kappa s}\,ds/s$ (Example 2.10 of the paper; also the third bullet of the third recall above).
>
> **Step 4 — identify the right-hand side as $\mu^\kappa_X(C_X(\gamma^m))$.** By [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] applied with $\phi(\lambda) = \lambda + \kappa$,
> $$\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty \frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,e^{-\kappa s}\,\frac{ds}{s}.$$
> Comparing (renaming $s \leftrightarrow t$), this is exactly Step 3's right-hand side. Hence
> $$\int_0^\infty e^{-\kappa t}\,\left[\frac{S_X(t)}{t}\right]_{(\gamma, m)}\!\!dt \;=\; \mu^\kappa_X\big(C_X(\gamma^m)\big). \tag{$\star$}$$
> This proves **(1)**.
>
> **Step 5 — sum over $(\gamma, m)$ by Fubini.** All summands in $S_X$ and all class masses are non-negative. For $\kappa > 0$, the double sum $M_\kappa := \sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m))$ is finite (this is the total killed loop mass; see [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]: $M_\kappa = -\log Z_X(s)$ with $s = \frac12 + \sqrt{\frac14 + \kappa} > 1$). By the Tonelli theorem (non-negative integrands, interchange of a countable sum with a Lebesgue integral),
> $$\int_0^\infty e^{-\kappa t}\,\frac{S_X(t)}{t}\,dt \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\int_0^\infty e^{-\kappa t}\,\left[\frac{S_X(t)}{t}\right]_{(\gamma, m)}\!\!dt \;\stackrel{(\star)}{=}\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; M_\kappa.$$
> This proves **(2)**.
>
> **Step 6 — Brownian case $\kappa = 0$, term-by-term identity survives.** Setting $\kappa = 0$ in ($\star$), the term-by-term identity still holds:
> $$\int_0^\infty \left[\frac{S_X(t)}{t}\right]_{(\gamma, m)}dt \;=\; \mu_X\big(C_X(\gamma^m)\big) \;=\; \frac{1}{m}\cdot\frac{1}{e^{m\ell_\gamma} - 1},$$
> the last equality by [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] specialised to $\phi = \lambda$ (see the third recall above). What *fails* at $\kappa = 0$ is the summability: the primitive $(m = 1)$ subsum $S^p_X(t) := \sum_\gamma\left[\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{\ell_\gamma e^{-\ell_\gamma^2/(4t)}}{2\sinh(\ell_\gamma/2)}\right]$ satisfies $S^p_X(t) \to 1$ as $t \to \infty$ (the $\lambda_0 = 0$ eigenvalue's contribution to the trace), making $\int^\infty S^p_X/t\,dt = +\infty$; correspondingly, $\sum_\gamma \mu_X(C_X(\gamma)) = \sum_\gamma \frac{1}{e^{\ell_\gamma} - 1} = +\infty$ on a closed surface (the primitive-class total mass diverges).
>
> **Step 7 — non-primitive part sums absolutely to a finite total.** For $m \ge 2$, the identity of Step 6 gives $\int_0^\infty [S_X/t]_{(\gamma, m)}\,dt = \frac{1}{m(e^{m\ell_\gamma} - 1)}$, and the double sum
> $$\sum_{\gamma \in \mathcal P_X}\sum_{m \ge 2}\frac{1}{m(e^{m\ell_\gamma} - 1)}$$
> converges absolutely (the systole bound $\ell_\gamma \ge \ell_{\mathrm{sys}} > 0$ gives $e^{m\ell_\gamma} - 1 \ge e^{2\ell_{\mathrm{sys}}} - 1$ for $m \ge 2$, and the geodesic count grows like $e^R/R$ — beat by the exponential $e^{-m\ell_\gamma}$). By Tonelli again,
> $$\int_0^\infty \frac{S_X(t) - S^p_X(t)}{t}\,dt \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 2}\frac{1}{m(e^{m\ell_\gamma} - 1)} \;=\; \!\!\!\!\sum_{\gamma \in \mathcal G(X)\setminus\mathcal P_X}\!\!\!\mu_X\big(C_X(\gamma)\big),$$
> the last equality using that non-primitive closed geodesics on $X$ are exactly $\{\gamma^m : \gamma \in \mathcal P_X, m \ge 2\}$. This proves **(3)**: the identity of $S_X/t$ with the total loop-mass integrand survives at $\kappa = 0$ in a *split* form — the non-primitive half converges to a finite loop-mass total, while the primitive half is the divergent piece that requires PGT renormalisation. $\blacksquare$

The identity ($\star$) is the paper's whole reason for writing $-\log\det_\zeta\Delta_X$ as a sum over loop masses: without it, Naud's expansion (a spectral-geometric object) and the total Brownian loop mass (a probabilistic object) would live in disjoint languages. With it, the two are the same integral.

---

# Where the paper uses this

Used implicitly at the very first step of *every* proof branch of [[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]] (compact case): Step 0 of the finite-$\kappa$ proof invokes $M_\kappa = \int_0^\infty e^{-\kappa t}S_X(t)/t\,dt$ (which is **(2)** here); Step 2 of the Brownian proof invokes the non-primitive closed form (which is **(3)** here); the $\alpha$-stable case rescales the Brownian identity. Also used in [[Thm - Determinant via Loop Measure, Finite-Area Case|Theorem 5.7]] (cusped case): the [[Thm - Selberg Zeta Identity for the Total Loop Mass|Selberg zeta identity]] $-\log Z_X(s) = M_\kappa$ that is fed into Borthwick–Judge–Perry is *this* identification, unfolded onto Selberg zeta content via [[Lemma - Selberg Zeta Criterion|Lemma 4.2]]. Read in context: [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]].
