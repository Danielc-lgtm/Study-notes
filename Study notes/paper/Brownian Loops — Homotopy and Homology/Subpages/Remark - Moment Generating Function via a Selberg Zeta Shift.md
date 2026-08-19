---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Probability Measure on Homotopy Classes"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
tags: [paper, brownian-loops, spectral-geometry, moment-generating-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §6.1 — MGF and all moments of $L$ via a shift of the spectral parameter"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface; $\Gamma \subset \mathrm{PSL}(2, \mathbb{R})$ discrete torsion-free.
- $\mathcal P_X$ the set of oriented primitive closed geodesics; $\ell_\gamma > 0$ the length of $\gamma \in \mathcal P_X$.
- $C_X(\gamma^m)$ the free homotopy class winding $m \ge 1$ times around $\gamma$.
- $\kappa > 0$ the killing rate, $s = \frac12 + \sqrt{\frac14 + \kappa} \in (1, \infty)$ the spectral parameter (assumed $> \delta$, the critical exponent of $\Gamma$).
- $\mu^\kappa_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$ the killed loop mass of the class (§3.1.2).
- $Z_X(s) = \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ the Selberg zeta function; $F(s) := -\log Z_X(s)$ the total killed loop mass, a positive real number for $s > \delta$.
- $\mathbb{P}_s(C_X(\gamma^m)) := \mu^\kappa_X(C_X(\gamma^m))/F(s)$ the probability measure on free homotopy classes; $\mathbb{E}_s, \operatorname{Var}_s$ expectation and variance under $\mathbb{P}_s$.
- $L := m\ell_\gamma$ the geodesic length of the class $C_X(\gamma^m)$, viewed as a random variable on the probability space of classes.

> [!recall]- Killed loop-measure mass $\mu^\kappa_X(C_X(\gamma^m))$
> **Formally:** for the Brownian loop measure on $X$ with killing at rate $\kappa \ge 0$, the mass of the free homotopy class $C_X(\gamma^m)$ is
> $$\mu^\kappa_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1},\qquad s = \frac12 + \sqrt{\frac14 + \kappa},$$
> a positive real number depending only on the geodesic length $\ell_\gamma$, the winding $m$, and the spectral parameter $s$.
> **In words:** a single number attached to each topological class, telling you how much loop-measure weight the class carries. Longer classes ($L = m\ell_\gamma$ large) get exponentially suppressed weight $\propto e^{-sL}$; the parameter $s$ controls how heavily the suppression penalises length. The $s$-dependence is packaged entirely inside the *single* factor $e^{(1-s)m\ell_\gamma} = e^{(1-s)L}$ — the denominator $e^{m\ell_\gamma} - 1$ and the prefactor $1/m$ are $s$-free — which is what makes the shift trick below possible.
> **Concretely:** on an infinite-area surface with one primitive geodesic of length $\ell = \log 2$ and $s = 2$, $\mu^\kappa(C_X(\gamma)) = \frac11\cdot\frac{e^{-\log 2}}{e^{\log 2} - 1} = \frac{1/2}{1} = \frac12$; $\mu^\kappa(C_X(\gamma^2)) = \frac12\cdot\frac{e^{-2\log 2}}{e^{2\log 2} - 1} = \frac12\cdot\frac{1/4}{3} = \frac{1}{24}$. Full derivation: [[Thm - Mass of a Subordinate Brownian Loop Class]].

> [!recall]- Total killed loop mass $F(s) = -\log Z_X(s)$
> **Formally:** the Selberg zeta $Z_X(s) := \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ is absolutely convergent for $\operatorname{Re}s > \delta$; its logarithm expands term-by-term (Corollary 4.3) as
> $$F(s) := -\log Z_X(s) = \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu^\kappa_X(C_X(\gamma^m)) = \sum_{\gamma, m}\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1},$$
> the sum of positive killed loop masses over all free homotopy classes.
> **In words:** the total loop-measure weight on $X$ under killing at rate $\kappa = s(s-1)$, packaged as a single positive analytic function of $s$. Its *value* at $s = \frac12 + \sqrt{\frac14 + \kappa}$ is the normalising constant of the probability measure $\mathbb{P}_s$; its *derivatives* in $s$ generate all moments of the length random variable $L$, which is what this remark exploits.
> **Concretely:** for a toy surface with one primitive geodesic of length $\ell = 1$, $F(2) = \sum_m \frac{1}{m}\cdot\frac{e^{-m}}{e^m - 1} \approx 0.214 + 0.009 + 0.0007 + \cdots \approx 0.224$. Full detail: [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]] and [[Thm - Selberg Zeta Identity for the Total Loop Mass]].

---

# Claim / Identity

> **Claim (moment generating function of $L$ under $\mathbb{P}_s$ via a Selberg zeta shift).** Let $\kappa > 0$ and $s = \frac12 + \sqrt{\frac14 + \kappa} > \delta$. For every real $r$ with $s + r > \delta$ (equivalently $r > \delta - s$; in particular $r > 1 - s$ suffices when $\delta \le 1$),
> $$\mathbb{E}_s\!\big[e^{-rL}\big] = \frac{-\log Z_X(s + r)}{-\log Z_X(s)} = \frac{\log Z_X(s + r)}{\log Z_X(s)}.\qquad (\star)$$
> Consequently, writing $F(s) := -\log Z_X(s)$, every moment of $L$ is a derivative of $F$:
> $$\mathbb{E}_s[L^n] = \frac{(-1)^n F^{(n)}(s)}{F(s)},\qquad n \ge 1,\qquad (\star\star)$$
> and the first two cumulants are derivatives of $\log F$:
> $$\mathbb{E}_s[L] = -\frac{d}{ds}\log F(s) = -\frac{F'(s)}{F(s)},\qquad \operatorname{Var}_s(L) = \frac{d^2}{ds^2}\log F(s).\qquad (\star{\star}\star)$$
> Since $\operatorname{Var}_s(L) > 0$, $\log F$ is strictly convex on $(\delta, \infty) \cap (1, \infty)$; hence $s \mapsto \mathbb{E}_s[L]$ is strictly decreasing — *more killing shortens the typical class.*

---

# In One Line

Shifting the spectral parameter $s \mapsto s + r$ is exactly the same as tilting the length distribution by $e^{-rL}$, because the killed-mass formula depends on $s$ only through the single factor $e^{(1-s)L}$; so the MGF of $L$ under $\mathbb{P}_s$ is the *ratio* $\log Z_X(s+r)/\log Z_X(s)$ of Selberg zeta values, and every moment falls out of derivatives of $-\log Z_X$ evaluated at $s$.

---

# Why It's True

**Mechanism.** *The mass of every class $C_X(\gamma^m)$ carries $s$ only through the exponent $(1-s)L$ with $L = m\ell_\gamma$; multiplying the mass by $e^{-rL}$ therefore replaces $(1-s)L$ by $(1-s-r)L = (1-(s+r))L$, which is exactly the same mass formula evaluated at parameter $s + r$. Summing over all classes, $\sum_{\gamma, m}e^{-rL}\mu^\kappa_X(C_X(\gamma^m)) = -\log Z_X(s+r)$; dividing by the normaliser $-\log Z_X(s)$ gives the MGF as a ratio of Selberg zeta values. Differentiating $F(s)$ in $s$ pulls a factor $-L$ out of every summand; differentiating $n$ times pulls $(-L)^n$; hence $n$-th moments equal $F^{(n)}(s)/F(s)$ (up to sign).*

The Selberg zeta function *is* the moment generating function of $L$ in disguise: it packages both the normalisation ($F(s)$) and the tilted normalisations ($F(s+r)$) in one analytic object. Everything the reader might want to know about the length distribution of a random class is a derivative of $F$ at the chosen $s$.

---

# Derivation

> [!note]- Gap-free derivation
> **Step 1 — the shift identity at the summand level.** For any $(\gamma, m)$ and any $r$ with $s + r > \delta$,
> $$e^{-r\,m\ell_\gamma}\cdot\mu^\kappa_X(C_X(\gamma^m)) = e^{-rm\ell_\gamma}\cdot\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1} = \frac{1}{m}\cdot\frac{e^{(1-(s+r))m\ell_\gamma}}{e^{m\ell_\gamma} - 1} = \mu^{\kappa(r)}_X\!\big(C_X(\gamma^m)\big),$$
> where $\kappa(r) := (s+r)(s+r-1)$ is the killing rate whose spectral parameter is $s+r$. The denominator $e^{m\ell_\gamma} - 1$ and the prefactor $1/m$ are $s$-free, so the multiplication by $e^{-rL}$ passes through untouched into the exponent.
>
> **Step 2 — the shift identity at the level of totals (proof of $(\star)$).** Since $\sum_{\gamma, m}\mu^{\kappa(r)}_X(C_X(\gamma^m)) = -\log Z_X(s + r)$ (Corollary 4.3 at the shifted parameter), summing Step 1 over all $(\gamma, m)$,
> $$\sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}e^{-r m\ell_\gamma}\,\mu^\kappa_X(C_X(\gamma^m)) = -\log Z_X(s + r).$$
> The absolute-convergence hypothesis $s + r > \delta$ justifies term-by-term rearrangement (Fubini on a positive double sum). Dividing by the normaliser $-\log Z_X(s) = F(s)$,
> $$\mathbb{E}_s\!\big[e^{-rL}\big] = \frac{1}{F(s)}\sum_{\gamma, m}e^{-rm\ell_\gamma}\mu^\kappa_X(C_X(\gamma^m)) = \frac{-\log Z_X(s + r)}{-\log Z_X(s)} = \frac{\log Z_X(s+r)}{\log Z_X(s)},$$
> which is $(\star)$. The last equality just cancels a minus sign in numerator and denominator.
>
> **Step 3 — differentiating $F$ pulls $-L$ (proof of $(\star\star)$).** From the log-expansion $F(s) = \sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m))$ and the fact that each summand depends on $s$ only through the factor $e^{(1-s)m\ell_\gamma}$,
> $$\frac{d}{ds}\mu^\kappa_X(C_X(\gamma^m)) = -m\ell_\gamma\cdot\mu^\kappa_X(C_X(\gamma^m)) = -L\cdot\mu^\kappa_X(C_X(\gamma^m)).$$
> Term-by-term differentiation is legal because the double sum converges absolutely and uniformly on compact subsets of $\{s : \operatorname{Re}s > \delta\}$ (Selberg-zeta convergence estimates). Iterating $n$ times,
> $$F^{(n)}(s) = \sum_{\gamma, m}(-L)^n\,\mu^\kappa_X(C_X(\gamma^m)) = (-1)^n\sum_{\gamma, m}L^n\,\mu^\kappa_X(C_X(\gamma^m)).$$
> Dividing by $F(s)$ recognises the right side as $F(s)\cdot\mathbb{E}_s[L^n]$; solving,
> $$\mathbb{E}_s[L^n] = \frac{(-1)^n F^{(n)}(s)}{F(s)},\qquad n \ge 1,$$
> which is $(\star\star)$.
>
> **Step 4 — mean and variance as derivatives of $\log F$ (proof of $(\star{\star}\star)$).** By the chain rule,
> $$\frac{d}{ds}\log F(s) = \frac{F'(s)}{F(s)} = \frac{-1}{F(s)}\sum_{\gamma, m}L\,\mu^\kappa_X(C_X(\gamma^m)) = -\mathbb{E}_s[L],$$
> so $\mathbb{E}_s[L] = -(d/ds)\log F(s)$. Differentiating once more,
> $$\frac{d^2}{ds^2}\log F(s) = \frac{F''(s)F(s) - F'(s)^2}{F(s)^2} = \frac{F''(s)}{F(s)} - \Big(\frac{F'(s)}{F(s)}\Big)^2 = \mathbb{E}_s[L^2] - \mathbb{E}_s[L]^2 = \operatorname{Var}_s(L),$$
> using $(\star\star)$ at $n = 2$ ($\mathbb{E}_s[L^2] = F''/F$) and the previous line ($\mathbb{E}_s[L] = -F'/F$).
>
> **Step 5 — convexity of $\log F$ and monotonicity of $\mathbb{E}_s[L]$.** Because $L$ is a non-constant random variable (there are at least two free homotopy classes of different lengths on any $X$ with more than one primitive geodesic — otherwise the spectrum is a single arithmetic progression, ruled out on generic hyperbolic surfaces), $\operatorname{Var}_s(L) > 0$; by Step 4, $(d^2/ds^2)\log F(s) > 0$, so $\log F$ is strictly convex on the parameter range $s > \max(\delta, 1)$. Its derivative $-\mathbb{E}_s[L] = (d/ds)\log F(s)$ is therefore strictly increasing in $s$, i.e. $\mathbb{E}_s[L]$ is strictly decreasing in $s$: increasing $\kappa$ (equivalently $s$) shortens the typical class. $\blacksquare$
>
> **Sanity check: $r = 0$.** $(\star)$ at $r = 0$ gives $\mathbb{E}_s[e^0] = 1 = \log Z_X(s)/\log Z_X(s)$. Trivial. **Sanity check: $s + r \to \delta^+$.** As $r \downarrow \delta - s$, $-\log Z_X(s+r) \to +\infty$ (the total mass diverges at the critical exponent), so the MGF $\mathbb{E}_s[e^{-rL}]$ diverges — consistent with the length distribution having a right tail that only sums against exponentials $e^{-rL}$ with $r > \delta - s$.

---

# Where the paper uses this

Introduced (implicitly, as the reasoning at the top of [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.1]]) immediately after the definition of $\mathbb{P}_s$ ([[Def - Probability Measure on Homotopy Classes]]). The moment formulas $(\star\star)$ and $(\star{\star}\star)$ feed the [[Remark - Systole Limit of the Homotopy Probability Measure|systole-limit computation]] (the leading large-$s$ behaviour of $F$ is what gives $\mathbb{E}_s[L] \to \ell_{\mathrm{sys}}$) and are the reason "every distributional statement about $L$ is a statement about the Selberg zeta and its derivatives" — the paper's own summary of §6.1.
