---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
tags: [paper, brownian-loops, zeta-functions, statistical-mechanics]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 4.4"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a geometrically finite hyperbolic surface with critical exponent $\delta$.
- $\mathcal P_X$ — the primitive oriented closed geodesics of $X$, lengths $\ell_\gamma$.
- $Z_X(s) = \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ — the Selberg zeta function.
- For each $\gamma \in \mathcal P_X$ and $s > \delta$, set the **per-geodesic bosonic partition function**
  $$Z_\gamma(s) := \prod_{k \ge 0}\big(1 - e^{-(s + k)\ell_\gamma}\big)^{-1}.$$
- $\mathcal Z(s) := \prod_{\gamma \in \mathcal P_X} Z_\gamma(s)$ — the **grand partition function** (a product of the per-geodesic ones); by construction $\mathcal Z(s) = Z_X(s)^{-1}$.
- $\mu^\kappa_X$ — the killing-$\kappa$ Brownian loop measure ($\kappa \ge -\frac14$); with spectral parameter $s(\kappa) = \frac12 + \sqrt{\frac14 + \kappa}$.

> [!recall]- Selberg zeta $Z_X(s)$ and its log-expansion
> **Formally:** $Z_X(s) = \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s + k)\ell_\gamma})$ for $\operatorname{Re} s > \delta$; $-\log Z_X(s) = \sum_\gamma\sum_{m \ge 1}\frac{1}{m}\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$.
> **In words:** a product with one factor per closed geodesic and per non-negative integer $k$; each factor has the exponential shape $1 - e^{-(s+k)\ell_\gamma}$. This is the generating function of the length spectrum of $X$.
> **Concretely:** for a single-geodesic toy $\Gamma = \langle \tau_0 : z \mapsto e^\ell z\rangle$, $Z_X(s) = \prod_{k \ge 0}(1 - e^{-(s+k)\ell})$; at $s = 1$, $\ell = 1$: $Z_X(1) \approx 0.521$. Full detail: [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Selberg zeta identity for the total loop mass
> **Formally:** for $\kappa \ge -\frac14$ with $s(\kappa) = \frac12 + \sqrt{\frac14 + \kappa} > \delta$, $\sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m)) = -\log Z_X(s(\kappa))$; in particular at $\kappa = 0$ (plain Brownian, $s = 1$), the total mass equals $-\log Z_X(1)$.
> **In words:** the sum of the killed Brownian loop masses over all non-trivial-non-peripheral topological types on the surface is a specific value of the Selberg zeta function.
> **Concretely:** on an infinite-area surface with $\delta = 1/2$, at $\kappa = 0$, $-\log Z_X(1)$ is a finite positive number equal to the total Brownian loop mass over non-trivial classes. Full detail: [[Thm - Selberg Zeta Identity for the Total Loop Mass]].

> [!recall]- Grand canonical partition function of an ideal Bose gas
> **Formally:** for a system of non-interacting bosons with single-particle energy levels $\{\varepsilon_j\}_{j \ge 0}$, at inverse temperature $\beta$ and chemical potential $\mu$, the grand canonical partition function is $\mathcal Z_{\mathrm{gc}}(\beta, \mu) = \prod_j \sum_{n_j = 0}^\infty e^{-\beta(\varepsilon_j - \mu) n_j} = \prod_j (1 - e^{-\beta(\varepsilon_j - \mu)})^{-1}$, valid when $\mu < \min_j \varepsilon_j$ (so every factor's ratio $e^{-\beta(\varepsilon_j - \mu)} < 1$ and the geometric series converges).
> **In words:** each single-particle energy level $\varepsilon_j$ can be occupied by any non-negative integer number of bosons; the partition function factors over levels, and each factor is a geometric series in the occupation number. The infinite product $(1 - e^{-\beta(\varepsilon_j - \mu)})^{-1}$ is the trademark shape of a "sum over indistinguishable-particle occupations."
> **Concretely:** a $2$-level system with $\varepsilon_0 = 0$, $\varepsilon_1 = 1$, $\beta = 1$, $\mu = -\infty$ (no particles allowed): $\mathcal Z_{\mathrm{gc}} = \prod_{j=0,1}(1 - 0)^{-1} = 1$ (vacuum). At $\mu = -0.5$: $\mathcal Z_{\mathrm{gc}} = (1 - e^{-0.5})^{-1}(1 - e^{-1.5})^{-1} \approx (1 - 0.607)^{-1}(1 - 0.223)^{-1} \approx 2.542 \times 1.287 \approx 3.272$. The average occupation of level $j$ is $\bar n_j = 1/(e^{\beta(\varepsilon_j - \mu)} - 1)$ — the Bose–Einstein distribution.

---

# Statement

> **Remark (bosonic partition function interpretation; Belyaev–Huseynli 4.4).** For each primitive geodesic $\gamma \in \mathcal P_X$ define the **per-geodesic bosonic partition function**
> $$Z_\gamma(s) \;:=\; \prod_{k \ge 0}\big(1 - e^{-(s + k)\ell_\gamma}\big)^{-1},$$
> and the total (grand) partition function $\mathcal Z(s) := \prod_{\gamma \in \mathcal P_X} Z_\gamma(s)$. Then $\mathcal Z(s) = Z_X(s)^{-1}$, and the Selberg zeta identity of [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] reads
> $$\sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; \log \mathcal Z(s(\kappa)).$$
> Each $Z_\gamma(s)$ is the partition function of a **free bosonic system** with occupation modes indexed by $k \ge 0$ and single-mode energies $\varepsilon_k^{(\gamma)} := (s + k)\ell_\gamma$; $\mathcal Z(s)$ is the grand-canonical partition function of a free Bose gas at zero chemical potential, and the total loop mass is its log.

⚠️ *(This is a physical interpretation. The mathematical content is the zeta identity of [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]; the reading below rewrites that identity in the vocabulary of statistical mechanics but adds no new mathematical statement.)*

---

# In One Line

The Selberg zeta identity — total killed-Brownian loop mass equals $-\log Z_X(s)$ — reads, in physicists' language, as: the total loop mass is the log of the grand canonical partition function of an ideal Bose gas whose single-particle spectrum is indexed by $(\gamma, k)$ with energies $(s + k)\ell_\gamma$.

---

# Unpacking

**Why "bosonic".** A free non-interacting bosonic mode with energy $\varepsilon$ contributes a factor $(1 - e^{-\beta\varepsilon})^{-1}$ to the grand canonical partition function (with $\beta$ the inverse temperature and chemical potential $\mu = 0$): each occupation number $n \in \{0, 1, 2, \ldots\}$ contributes $e^{-\beta\varepsilon n}$, summing to the geometric series. Compare with $Z_\gamma(s) = \prod_{k \ge 0}(1 - e^{-(s + k)\ell_\gamma})^{-1}$: each factor $(1 - e^{-(s + k)\ell_\gamma})^{-1}$ has exactly the free-boson shape, with $\beta \varepsilon = (s + k)\ell_\gamma$. Reading $s$ as a chemical-potential shift and $\ell_\gamma$ as an inverse-temperature-times-a-length unit, the mode $(\gamma, k)$ carries "energy $\varepsilon^{(\gamma)}_k = (s + k)\ell_\gamma$" (in the same units). The mode label $k \ge 0$ is a Kaluza-like tower — the tower comes from *quantising loop winding along a single geodesic*.

**The whole surface.** Multiplying $Z_\gamma(s)$ over all primitive geodesics $\gamma$ gives $\mathcal Z(s) = \prod_\gamma Z_\gamma(s)$: the partition function of a free Bose gas with an independent boson tower per geodesic. Because $Z_\gamma(s) = \prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})^{-1}$ is the reciprocal of the Selberg factor for $\gamma$, taking the product over $\gamma$ inverts the whole Selberg zeta: $\mathcal Z(s) = Z_X(s)^{-1}$. Taking $\log$ turns the reciprocal into a sign flip:
$$\log \mathcal Z(s) \;=\; -\log Z_X(s).$$
Combining with the Selberg zeta identity ([[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]), which asserts $\sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m)) = -\log Z_X(s(\kappa))$, the total loop mass equals $\log \mathcal Z(s(\kappa))$.

**"Zero chemical potential".** The single-particle energies $(s + k)\ell_\gamma$ are all strictly positive for $s > 0$ and $k \ge 0$, so the physical constraint $\mu < \min_k \varepsilon_k^{(\gamma)} = s\ell_\gamma$ is satisfied automatically at $\mu = 0$; convergence of every geometric factor holds for $s > 0$. The interpretation reads $s$ itself as the "gap" between the (zero) chemical potential and the lowest single-particle level $s\ell_\gamma$; increasing $s$ opens the gap, suppresses occupation, and makes the partition function smaller (equivalently $Z_X(s)$ larger, total loop mass smaller).

**What the analogy adds and does not add.** The physical picture is a *re-reading* — it gives the reader a familiar mental object (a Bose gas) whose partition function the paper's random-loop total mass computes. It does *not* imply that the Brownian loop measure literally *is* the trace of a bosonic thermal density matrix; the identification is at the level of generating-function shapes, not at the level of a Hilbert-space construction. Making the analogy precise (identifying the modes $(\gamma, k)$ with occupation-number states of a Bose field on the trivial line bundle over the shift space of geodesics, say) is beyond the paper's scope; the remark serves as an *interpretation hint*, not a claim.

**Convergence caveat.** The equality $\mathcal Z(s) = Z_X(s)^{-1}$ requires $s > \delta$ so that both products converge; at the critical exponent, $Z_X(\delta) = 0$ and $\mathcal Z(\delta) = +\infty$ (the "partition function blows up" at the critical inverse temperature — a Bose-condensation-flavoured phenomenon).

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.1.1]] immediately after [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]. Purely interpretive — the paper does not use this reading in a later proof. It offers a bridge to the physics literature (Polyakov's bosonic string sum, string partition functions on hyperbolic Riemann surfaces) where the same product structure appears; the closest formal cousin is the one-loop bosonic string free energy on a Riemann surface, whose modular integrand is built from the same Selberg factors.
