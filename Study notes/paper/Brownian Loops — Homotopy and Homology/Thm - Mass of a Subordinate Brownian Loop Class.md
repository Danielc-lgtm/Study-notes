---
type: theorem
subject: probability-geometry
prereqs:
  - "Thm - Mass of a Free Homotopy Class"
  - "Lemma - Wang-Xue Strip Integral"
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Subordinate Brownian Loop Measure"
  - "Def - Weighted Potential Measure"
  - "Def - The Loop-Length Integral"
  - "Lemma - Collapsing the Time Integral of the Subordinate Kernel"
tags: [paper, brownian-loops, hyperbolic-geometry, subordinate-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 3.5"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ — a geometrically finite hyperbolic surface.
- $\gamma \in \mathcal{P}_X$ — a primitive closed geodesic of length $\ell_\gamma > 0$; $\tau \in \Gamma$ its primitive hyperbolic representative, standardised so $\tau : z\mapsto e^{\ell_\gamma}z$; $\mathcal{F}_\tau = \{1\le\mathrm{Im}\,z < e^{\ell_\gamma}\}$ the fundamental strip; $C_X(\gamma^m)$ the free homotopy class of the $m$-fold winding.
- $L := m\ell_\gamma$ — the total translation length used everywhere in this subpage.
- $\phi : (0,\infty)\to (0,\infty)$ — a **Bernstein function** (Assumption 2.3 of the paper): concave, non-decreasing, with $\phi(0^+) = 0$. Its subordinator has Laplace exponent $\phi$: $\mathbb{E}[e^{-\lambda S_t}] = e^{-t\phi(\lambda)}$.
- $\psi^\phi_t(ds)$ — the law of $S_t$, so $p^\phi_{\mathbb{H}^2}(t,z,w) = \int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,w)\,\psi^\phi_t(ds)$.
- $V_\phi(ds) := \int_0^\infty\psi^\phi_t(ds)\,dt/t$ — the **weighted potential measure** on $(0,\infty)$; the $dt/t$-average of the subordinator laws (Definition 2.9).
- $I_\phi(L) := \int_0^\infty \frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds)$ — the **loop-length integral** (Definition 3.6).
- $\mu^\phi_X$ — the subordinate loop measure on $X$; for jump processes, defined as in Remark 3.1.

> [!recall]- Bernstein function $\phi$ and its subordinator
> **Formally:** $\phi : (0,\infty)\to(0,\infty)$ is a **Bernstein function** if it is $C^\infty$, non-decreasing, and its first derivative $\phi'$ is completely monotone (all higher derivatives alternate in sign). Equivalently, $\phi$ has the Lévy–Khintchine representation $\phi(\lambda) = a + b\lambda + \int_0^\infty(1-e^{-\lambda s})\,\nu(ds)$ for some $a, b\ge 0$ and Lévy measure $\nu$ with $\int(s\wedge 1)\,\nu(ds) < \infty$. A subordinator $S = (S_t)_{t\ge 0}$ is an $[0,\infty)$-valued Lévy process (non-decreasing paths); its Laplace exponent is $\mathbb{E}[e^{-\lambda S_t}] = e^{-t\phi(\lambda)}$ for some Bernstein $\phi$.
> **In words:** a Bernstein function is a smooth non-decreasing function with all derivatives sign-alternating — a shape restrictive enough to characterise exactly which functions of an operator produce a probability-preserving process (Bochner subordination). The corresponding subordinator is a random clock that only ever moves forward.
> **Concretely:** $\phi(\lambda) = \lambda$ gives the identity subordinator $S_t = t$ (no jumps, no subordination). $\phi(\lambda) = \lambda + \kappa$ gives Brownian motion with killing at rate $\kappa$. $\phi(\lambda) = \lambda^{\alpha/2}$, $\alpha\in(0,2)$, gives the $\alpha/2$-stable subordinator (heavy-tailed jumps, no drift). $\phi(\lambda) = (\lambda + \kappa)^{\alpha/2}$ is the shifted stable. Full detail: [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- Weighted potential measure $V_\phi$
> **Formally:** for a Bernstein $\phi$ with subordinator law $\psi^\phi_t(ds)$, the *weighted potential measure* on $(0,\infty)$ is $V_\phi(ds) := \int_0^\infty \psi^\phi_t(ds)\,\frac{dt}{t}$: the Haar-$dt/t$-average of subordinator distributions. Equivalently, $V_\phi$ can be read off from $\phi$'s Bernstein triple.
> **In words:** collapse the two-parameter family of subordinator distributions $(\psi^\phi_t)_{t>0}$ against the loop-measure weight $dt/t$ into a single measure on the "internal-clock" variable $s$. This is the object that carries all of $\phi$'s dependence in the class-mass identity.
> **Concretely:** for $\phi = \lambda$ (Brownian), $V_\phi(ds) = ds/s$; for $\phi = \lambda + \kappa$ (killing $\kappa$), $V_\phi(ds) = e^{-\kappa s}\,ds/s$; for $\phi = \lambda^{\alpha/2}$ ($\alpha$-stable), $V_\phi(ds) = (\alpha/2)\,ds/s$; for $\phi = (\lambda+\kappa)^{\alpha/2}$ (shifted stable), $V_\phi(ds) = (\alpha/2)\,e^{-\kappa s}\,ds/s$. Full detail: [[Def - Weighted Potential Measure]] and Example 2.10 of the paper.

> [!recall]- Subordinate loop measure $\mu^\phi_X$
> **Formally:** the subordinate loop measure on $X$ is $\mu^\phi_X = \int_0^\infty\frac{dt}{t}\int_X\mathbb{W}^{t,\phi}_{z\to z, X}\,d\rho_X(z)$ where $\mathbb{W}^{t,\phi}$ is the bridge measure of the $\phi$-subordinate Brownian motion. Its kernel is $p^\phi_{\mathbb{H}^2}(t,z,w) = \int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,w)\,\psi^\phi_t(ds)$; the periodisation to $X$ is $p^\phi_X(t,z,w) = \sum_{h\in\Gamma}p^\phi_{\mathbb{H}^2}(t,\tilde z, h\tilde w)$.
> **In words:** the loop measure of the process $Y = B\circ S$ — Brownian motion clocked by a $\phi$-subordinator. When $\phi = \lambda$, this is the ordinary Brownian loop measure; other $\phi$'s produce jump-process variants ($\alpha$-stable, killed Brownian, etc.).
> **Concretely:** for $\phi(\lambda) = \lambda + \kappa$, $\mu^\phi_X = \mu^\kappa_X$ is the Brownian loop measure weighted by the survival factor $e^{-\kappa t}$ at time $t$ — the Schrödinger loop measure with constant potential $\kappa$. For $\phi(\lambda) = \lambda^{\alpha/2}$, $\mu^\phi_X$ is the loop measure of the $\alpha$-stable process (an infinite-jump-rate càdlàg process on $\mathbb{H}^2$). Full detail: [[Def - Subordinate Brownian Loop Measure]].

> [!recall]- Loop-length integral $I_\phi(L)$
> **Formally:** $I_\phi(L) := \int_{(0,\infty)}\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds)$, a positive real-valued function of $L>0$.
> **In words:** a purely one-dimensional integral in the internal-clock variable $s$; it packages all of $\phi$'s dependence in one place. The geometry (surface, class) enters $I_\phi$ only through the total translation length $L = m\ell_\gamma$.
> **Concretely:** for $\phi(\lambda) = \lambda$, $I_\phi(L) = e^{-L/2}/L$; for $\phi(\lambda) = \lambda + \kappa$, $I_\phi(L) = e^{-L\sqrt{1/4+\kappa}}/L$; both by the Gaussian-type integral identity below. Full detail: [[Def - The Loop-Length Integral]].

> [!recall]- Wang–Xue strip integral (Lemma 3.4)
> **Formally:** for $\tau : z\mapsto e^{\ell_\gamma}z$, $m\ge 1$, $L = m\ell_\gamma$, and every $s > 0$: $\int_{\mathcal{F}_\tau}p_{\mathbb{H}^2}(s,z,\tau^m z)\,d\rho_{\mathbb{H}^2}(z) = \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}$.
> **In words:** the fundamental-strip integral of the $\mathbb{H}^2$ heat kernel from $z$ to its $\tau^m$-translate has a closed form: geometric factor $\ell_\gamma/[2\sinh(L/2)]$ times a 1-D Gaussian in $L$ with a curvature correction $e^{-s/4}$.
> **Concretely:** at $L = \log 2$, $s = 1$: the strip integral equals $(\log 2)/(2\sinh(\log 2/2))\cdot e^{-1/4}e^{-(\log 2)^2/4}/(2\sqrt\pi) \approx 0.693/0.720\cdot 0.779\cdot 0.883/3.545 \approx 0.187$ — a moderate positive number, small because the exponential factor is $\approx 0.688$ and the Gaussian weight is $\approx 0.282$. Full detail: [[Lemma - Wang-Xue Strip Integral]].

> [!recall]- Collapsing $\int(dt/t)\int h(s)\psi^\phi_t(ds) = \int h(s)V_\phi(ds)$ (Lemma 2.11)
> **Formally:** for a non-negative measurable $h : (0,\infty)\to[0,\infty)$, $\int_0^\infty\frac{dt}{t}\int_{[0,\infty)}h(s)\,\psi^\phi_t(ds) = \int_{(0,\infty)}h(s)\,V_\phi(ds)$, where $V_\phi(ds) = \int_0^\infty\psi^\phi_t(ds)\,dt/t$. This is Tonelli/Fubini for non-negative integrands (the swap of the $t$-integral and the expectation defining the potential measure).
> **In words:** the two-parameter integral of a function of $s$ against the $t$-family of subordinator laws, weighted by $dt/t$, collapses to a single integral of the function against the weighted potential measure.
> **Concretely:** for $\phi = \lambda$, $\psi^\phi_t = \delta_t$ (identity subordinator), so $\int_0^\infty h(s)\,\delta_t(ds)\,dt/t = h(t)/t\,dt$; integrating over $t$ gives $\int h(s)\,ds/s$ — matching $V_\phi(ds) = ds/s$. Full detail: [[Lemma - Collapsing the Time Integral of the Subordinate Kernel]].

> [!recall]- Gaussian-type integral $\int_0^\infty s^{-3/2}e^{-as-b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{ab}}$
> **Formally:** for constants $a, b > 0$, $\int_0^\infty s^{-3/2}\,e^{-as - b/s}\,ds = \sqrt{\pi/b}\;e^{-2\sqrt{ab}}$.
> **In words:** an elementary calculus identity — the integrand is a positive function of a positive variable, and the closed form on the right is what it evaluates to. Any $\phi$-mass in the paper that has a closed form comes from this identity applied to specific $(a, b)$.
> **Concretely:** at $a = 1/4$, $b = L^2/4$: $\int_0^\infty s^{-3/2}e^{-s/4 - L^2/4s}\,ds = \sqrt{4\pi/L^2}\,e^{-L/2} = (2\sqrt\pi/L)\,e^{-L/2}$; so $\frac{1}{2\sqrt\pi}\int_0^\infty s^{-3/2}e^{-s/4-L^2/4s}\,ds = e^{-L/2}/L$ — the Brownian $I_{\mathrm{BM}}(L)$. **Short proof:** substitute $s = \sqrt{b/a}\,u$; the integral becomes $\int_0^\infty u^{-3/2}e^{-\sqrt{ab}(u+1/u)}\,du$; then $u\mapsto 1/u$ symmetrises to $\int_0^\infty u^{-1/2}e^{-c(u+1/u)}du$ ($c := \sqrt{ab}$), and taking the average of the two integrals with $w := \sqrt u - 1/\sqrt u$ (so $dw = \frac12(u^{-1/2} + u^{-3/2})\,du$ and $u + 1/u = w^2 + 2$) collapses to $\int_{-\infty}^\infty e^{-c(w^2+2)}\,dw = \sqrt{\pi/c}\,e^{-2c}$. Standard evaluation; see Gradshteyn–Ryzhik 3.471.

---

# Statement

> **Theorem (mass of a subordinate loop class; Belyaev–Huseynli 3.5).** Let $X = \Gamma\backslash\mathbb{H}^2$ be a geometrically finite hyperbolic surface, $\phi$ a Bernstein function (Assumption 2.3), $\gamma\in\mathcal{P}_X$ a primitive closed geodesic, and $m\ge 1$. With $L := m\ell_\gamma$,
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty \frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L),$$
> where $V_\phi$ is the weighted potential measure of $\phi$ and $I_\phi$ the loop-length integral.

---

# In One Line

Theorem 3.2 specialised to a $\phi$-subordinate process, with the duration-integral collapsed by Lemma 2.11 and the strip integral evaluated by Wang–Xue's Lemma 3.4: every class-mass reduces to a single 1-D integral in the subordination variable $s$, packaged as $I_\phi(L)$ multiplied by the geometric prefactor $\ell_\gamma/[2\sinh(L/2)]$.

---

# Why It's True

**Mechanism (one sentence).** *Substitute the subordination integral for $p^\phi_{\mathbb{H}^2}$ into Theorem 3.2, do the spatial integral first (Wang–Xue's Lemma 3.4 evaluates it in closed form independent of $z$), then collapse the remaining $(t,s)$-integral against $dt/t$ into the single $V_\phi$-integral by Lemma 2.11.*

There are three composable ingredients:

- [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] writes the class-mass as a triple integral over $(t, z, s')$ (with $s'$ implicit in the choice of Dirichlet-form kernel $p^E$).
- [[Def - Subordinate Brownian Loop Measure|Subordination]] $p^\phi_{\mathbb{H}^2}(t,z,w) = \int p_{\mathbb{H}^2}(s,z,w)\,\psi^\phi_t(ds)$ makes the $s$-integral explicit.
- The **spatial** integral $\int_{\mathcal{F}_\tau}p_{\mathbb{H}^2}(s,z,\tau^m z)\,d\rho_{\mathbb{H}^2}(z)$ is *independent of $t$* and equal to the Wang–Xue closed form — so the double integral in $(t, s)$ factors as (subordinator) × (heat-kernel evaluation), and Lemma 2.11 collapses the $t$-integral into $V_\phi$.

The upshot is that the *entire dependence of the class-mass on $\phi$* is packaged in the single 1-D integral $I_\phi(L)$; the entire geometric dependence is in the prefactor $\ell_\gamma/[2\sinh(L/2)]$ and the parameter $L = m\ell_\gamma$. That is why every concrete process the paper considers has a closed form: one Gaussian-type integral is enough.

---

# Proof

> [!note]- Gap-free proof
> **Step 1 — substitute Theorem 3.2 with the subordinate kernel.** By [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] with $p^E := p^\phi$,
> $$\mu^\phi_X(C_X(\gamma^m)) \;=\; \int_0^\infty\frac{dt}{t}\int_{\mathcal{F}_\tau} p^\phi_{\mathbb{H}^2}(t, z, \tau^m z)\,d\rho_{\mathbb{H}^2}(z).$$
> Insert the subordination formula $p^\phi_{\mathbb{H}^2}(t, z, w) = \int_{[0,\infty)} p_{\mathbb{H}^2}(s, z, w)\,\psi^\phi_t(ds)$:
> $$\mu^\phi_X(C_X(\gamma^m)) \;=\; \int_0^\infty\frac{dt}{t}\int_{\mathcal{F}_\tau}\int_{[0,\infty)} p_{\mathbb{H}^2}(s, z, \tau^m z)\,\psi^\phi_t(ds)\,d\rho_{\mathbb{H}^2}(z).$$
>
> **Step 2 — do the spatial integral first (Tonelli on non-negative integrand).** All three integrands are non-negative measurable, so Tonelli lets us swap freely:
> $$\mu^\phi_X(C_X(\gamma^m)) \;=\; \int_0^\infty\frac{dt}{t}\int_{[0,\infty)}\Big(\int_{\mathcal{F}_\tau} p_{\mathbb{H}^2}(s, z, \tau^m z)\,d\rho_{\mathbb{H}^2}(z)\Big)\psi^\phi_t(ds).$$
> By the [[Lemma - Wang-Xue Strip Integral|Wang–Xue strip integral (Lemma 3.4)]], the inner spatial integral evaluates to $\frac{\ell_\gamma}{2\sinh(L/2)}\cdot h(s)$ with
> $$h(s) := \frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}},$$
> independent of $z$ (and of the coset labelling of the class — the geometry of the strip has already been folded in). Substituting,
> $$\mu^\phi_X(C_X(\gamma^m)) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{dt}{t}\int_{[0,\infty)}h(s)\,\psi^\phi_t(ds).$$
>
> **Step 3 — collapse the $t$-integral into $V_\phi$.** Apply [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] with the non-negative measurable $h(s) = e^{-s/4}e^{-L^2/(4s)}/(2\sqrt{\pi s})$: $\int_0^\infty\frac{dt}{t}\int_{[0,\infty)}h(s)\,\psi^\phi_t(ds) = \int_{(0,\infty)}h(s)\,V_\phi(ds)$. Therefore
> $$\mu^\phi_X(C_X(\gamma^m)) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty h(s)\,V_\phi(ds) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L). \qquad\blacksquare$$

---

# Computed cases (§3.1.1–§3.1.4)

Every closed form the paper gives in §3.1 follows from the theorem by substituting a specific $V_\phi$ (from Example 2.10 of the paper) and applying the Gaussian-type identity. The four cases are the paper's own §3.1.1 (Brownian), §3.1.2 (killing), §3.1.3 ($\alpha$-stable), §3.1.4 (shifted $\alpha$-stable).

> [!note]- §3.1.1 — Brownian ($\phi(\lambda) = \lambda$)
> Here $V_\phi(ds) = ds/s$, so
> $$I_{\mathrm{BM}}(L) \;=\; \int_0^\infty\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi}\,s^{3/2}}\,ds \;=\; \frac{1}{2\sqrt\pi}\int_0^\infty s^{-3/2}e^{-s/4 - L^2/4s}\,ds.$$
> Apply the Gaussian-type identity with $a = 1/4$, $b = L^2/4$: $\int_0^\infty s^{-3/2}e^{-as-b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{ab}}$; here $2\sqrt{ab} = 2\cdot\sqrt{L^2/16} = L/2$, $\sqrt{\pi/b} = \sqrt{4\pi/L^2} = 2\sqrt\pi/L$; so
> $$I_{\mathrm{BM}}(L) = \frac{1}{2\sqrt\pi}\cdot\frac{2\sqrt\pi}{L}\,e^{-L/2} = \frac{e^{-L/2}}{L}.$$
> Substituting,
> $$\mu_X(C_X(\gamma^m)) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-L/2}}{L} \;=\; \frac{\ell_\gamma}{L}\cdot\frac{e^{-L/2}}{2\sinh(L/2)} \;=\; \frac{1}{m}\cdot\frac{1}{e^L - 1},$$
> using $\ell_\gamma/L = 1/m$ (recall $L = m\ell_\gamma$) and $e^{-L/2}/(2\sinh(L/2)) = e^{-L/2}/(e^{L/2} - e^{-L/2}) = 1/(e^L - 1)$. This recovers Wang–Xue [WX25, Lemma 3.2].

> [!note]- §3.1.2 — Brownian with killing ($\phi(\lambda) = \lambda + \kappa$, $\kappa\ge 0$)
> Here $V_\phi(ds) = e^{-\kappa s}\,ds/s$, so the killed loop-length integral is
> $$I_\kappa(L) = \int_0^\infty\frac{e^{-(1/4+\kappa)s}e^{-L^2/4s}}{2\sqrt\pi\,s^{3/2}}\,ds = \frac{1}{2\sqrt\pi}\int_0^\infty s^{-3/2}e^{-(1/4+\kappa)s - L^2/4s}\,ds.$$
> Same identity with $a = 1/4 + \kappa$, $b = L^2/4$: $2\sqrt{ab} = 2\sqrt{(1/4+\kappa)(L^2/4)} = L\sqrt{1/4+\kappa}$, $\sqrt{\pi/b} = 2\sqrt\pi/L$; so
> $$I_\kappa(L) = \frac{e^{-L\sqrt{1/4+\kappa}}}{L}.$$
> Then
> $$\mu^\kappa_X(C_X(\gamma^m)) = \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-L\sqrt{1/4+\kappa}}}{L} = \frac{1}{m}\cdot\frac{e^{(\frac12 - \sqrt{1/4+\kappa})L}}{e^L - 1},$$
> where the algebraic manipulation $\ell_\gamma/L = 1/m$ and $e^{-L\sqrt{1/4+\kappa}}/(2\sinh(L/2)) = e^{-L\sqrt{1/4+\kappa}}/(e^{L/2}(1 - e^{-L})) = e^{-L\sqrt{1/4+\kappa} - L/2}/(1 - e^{-L})$; simplifying and pulling out an $e^{L/2}$ gives the boxed form. This is exactly Lemonde–Wang [LW26, Lemma 3.1]; $\kappa = 0$ recovers §3.1.1. In this case the underlying operator is the Schrödinger operator $\Delta_{\mathbb{H}^2} + \kappa$ (constant potential $\kappa$), no longer the Laplacian.

> [!note]- §3.1.3 — $\alpha$-stable ($\phi(\lambda) = \lambda^{\alpha/2}$, $\alpha\in(0,2)$)
> Here $V_\phi(ds) = (\alpha/2)\,ds/s$, so
> $$I_\alpha(L) = \frac{\alpha}{2}\int_0^\infty\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt\pi\,s^{3/2}}\,ds = \frac{\alpha}{2}\cdot I_{\mathrm{BM}}(L) = \frac{\alpha}{2}\cdot\frac{e^{-L/2}}{L},$$
> and
> $$\mu^\alpha_X(C_X(\gamma^m)) = \frac{\alpha}{2}\cdot\mu_X(C_X(\gamma^m)) = \frac{\alpha}{2}\cdot\frac{1}{m(e^L - 1)}.$$
> The class-mass under an $\alpha$-stable process is just a *constant multiple* (namely $\alpha/2$) of the Brownian class-mass (with the reading of Remark 3.1: the class of a càdlàg $\alpha$-stable path is defined via the underlying Brownian arc, so the formula is well-defined despite the process having no continuous lift).
>
> **Why the geometry drops out.** The collapse is forced by **scale-invariance**: the self-similar subordinators are exactly the $\alpha$-stable ones, and the loop-measure weight $dt/t$ is itself scale-invariant, so the only measure on $(0,\infty)$ compatible with both scalings is a constant times $ds/s$; the constant is $\alpha/2$. Under such a scaling, no geometric detail of $X$ can survive — the surface's information channels are all Brownian. To get a class-mass whose *form* differs from the Brownian one, scale-invariance must be broken; the simplest way is to subordinate the *shifted* Laplacian $\Delta_{\mathbb{H}^2} + \kappa$, which is §3.1.4.

> [!note]- §3.1.4 — Shifted $\alpha$-stable ($\phi(\lambda) = (\lambda + \kappa)^{\alpha/2}$, $\alpha\in(0,2)$, $\kappa\ge 0$)
> Here the operator is $(\Delta_{\mathbb{H}^2} + \kappa)^{\alpha/2}$, obtained by composing $\lambda\mapsto\lambda+\kappa$ (a Bernstein function) with $u\mapsto u^{\alpha/2}$ (another Bernstein function); the composition is again Bernstein (in fact **complete Bernstein**), so the §2 framework applies. The subordinator law is an exponential tilt of the $\alpha$-stable law: from
> $$e^{-t(\lambda + \kappa)^{\alpha/2}} = \int_0^\infty e^{-u(\lambda+\kappa)}\,\eta^\alpha_t(u)\,du = \int_0^\infty e^{-\lambda s}\,e^{-\kappa s}\,\eta^\alpha_t(s)\,ds,$$
> one reads $\psi^\phi_t(ds) = e^{-\kappa s}\eta^\alpha_t(s)\,ds$ (where $\eta^\alpha_t$ is the $\alpha/2$-stable subordinator density). Collapsing against $dt/t$ by Definition 2.9, with the extra survival factor $e^{-\kappa s}$, gives $V_\phi(ds) = (\alpha/2)\,e^{-\kappa s}\,ds/s$. So
> $$I_\phi(L) = \frac{\alpha}{2}\int_0^\infty\frac{e^{-(1/4+\kappa)s}e^{-L^2/4s}}{2\sqrt\pi\,s^{3/2}}\,ds = \frac{\alpha}{2}\cdot\frac{e^{-L\sqrt{1/4+\kappa}}}{L}$$
> (Gaussian-type identity with $a = 1/4 + \kappa$, $b = L^2/4$, exactly as in §3.1.2). Substituting into Theorem 3.5,
> $$\mu^\phi_X(C_X(\gamma^m)) = \frac{\alpha}{2}\cdot\frac{1}{m}\cdot\frac{e^{(\frac12 - \sqrt{1/4+\kappa})L}}{e^L - 1}.$$
> The killing restores the geometry-sensitive exponent $\frac12 - \sqrt{1/4+\kappa}$ (which distinguishes this case in form from the pure Brownian one), with an extra multiplicative constant $\alpha/2$ from the stable exponent.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.1]]. The four computed cases feed the loop-soup means of [[Prop - Poissonian Structure of Homotopy Classes|Prop 3.8]] and the length-spectrum recovery of [[Prop - Loop Masses Determine the Length Spectrum|Prop 3.11]]. The killed formula (§3.1.2) is the input to the Selberg zeta identity of [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4]] and to the determinant identity of [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]]. The interpretation of the $\alpha$-stable case uses [[Remark - Homotopy Classes for Jump Processes|Remark 3.1]]. The complete-Bernstein composition in §3.1.4 is the concrete instance of Assumption 2.3.
