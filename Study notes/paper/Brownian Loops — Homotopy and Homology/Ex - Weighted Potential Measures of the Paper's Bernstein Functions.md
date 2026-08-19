---
type: example
subject: probability
prereqs:
  - "Def - Weighted Potential Measure"
  - "Def - Bernstein Function, Subordinator, and Subordination"
tags: [paper, brownian-loops, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Example 2.10"
---

# Notation

$\phi:(0,\infty)\to[0,\infty)$ a Bernstein function with subordinator law $\psi^\phi_t$ on $[0,\infty)$; $V_\phi$ its weighted potential measure of Definition 2.9. $\alpha\in(0,2)$, $\kappa\ge 0$. $g_{\alpha/2}$ the standard $\alpha/2$-stable density on $(0,\infty)$ (probability density: $\int_0^\infty g_{\alpha/2}(u)\,du=1$); $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})$ the $\alpha/2$-stable subordinator density at time $t$. $h:(0,\infty)\to[0,\infty)$ a non-negative measurable test function.

> [!recall]- Weighted potential measure $V_\phi$
> **Formally:** the $\sigma$-finite measure on $(0,\infty)$ characterised by $\int h(s)\,V_\phi(ds)=\int_0^\infty\frac{dt}{t}\int h(s)\,\psi^\phi_t(ds)$ for every non-negative measurable $h$ making the right-hand side finite.
> **In words:** the compressed record of "average the subordinator's law $\psi^\phi_t$ over duration $t$ using the scale-invariant weight $\frac{dt}{t}$ (the weight for which multiplication $t \to \lambda t$ preserves total mass on $(0,\infty)$)". A measure on the subordination variable $s$ packaging the outer $t$-integral for [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]].
> **Concretely:** for Brownian ($\psi^\phi_t=\delta_t$), the identity localises at $s=t$ so $\int h(s)\,V_\phi(ds)=\int h(t)\,\frac{dt}{t}$, i.e. $V_\phi(ds)=\frac{ds}{s}$. See [[Def - Weighted Potential Measure]].

> [!recall]- Bernstein functions and subordinator laws of the paper's four cases
> **Formally:** the four Bernstein functions are (1) $\phi(\lambda)=\lambda$, $\psi^\phi_t=\delta_t$; (2) $\phi(\lambda)=\lambda+\kappa$, $\psi^\phi_t=e^{-\kappa t}\delta_t$; (3) $\phi(\lambda)=\lambda^{\alpha/2}$, $\psi^\phi_t(ds)=\eta^\alpha_t(s)\,ds$; (4) $\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$, $\psi^\phi_t(ds)=e^{-\kappa s}\eta^\alpha_t(s)\,ds$.
> **In words:** trivial clock; deterministic-clock-with-killing; $\alpha/2$-stable clock; $\alpha/2$-stable clock exponentially tilted.
> **Concretely:** case 1's clock is $S_t=t$; case 3's clock is heavy-tailed with density $\eta^\alpha_t(s)$; case 4 is case 3 with density weighted by $e^{-\kappa s}$ (a killing-by-subordination-time factor). See [[Ex - The Four Bernstein Functions of the Paper]].

> [!recall]- The multiplicative Haar measure $\frac{dt}{t}$ on $(0,\infty)$
> **Formally:** $\sigma$-finite scale-invariant measure with $\int_{\lambda a}^{\lambda b}\frac{dt}{t}=\int_a^b\frac{dt}{t}$; infinite total mass, finite on compacts of $(0,\infty)$.
> **In words:** the unique duration-blind weight on positive reals; each factor of $e$ carries one unit of mass.
> **Concretely:** the change $u=\log t$ turns $\int_a^b f(t)\,\frac{dt}{t}$ into $\int_{\log a}^{\log b} f(e^u)\,du$, ordinary Lebesgue integration. See [[Def - Signed and Infinite Measures for Loop Measures]].

---

# Statement

> **Example (Belyaev–Huseynli 2.10 — Weighted potential measures).** For the four Bernstein functions of the paper:
>
> (a) **Brownian** ($\phi(\lambda)=\lambda$): $V_\phi(ds)=\dfrac{ds}{s}$.
>
> (b) **Killing** ($\phi(\lambda)=\lambda+\kappa$, $\kappa\ge 0$): $V_\phi(ds)=e^{-\kappa s}\,\dfrac{ds}{s}$.
>
> (c) **$\alpha$-stable** ($\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$): $V_\phi(ds)=\dfrac{\alpha}{2}\,\dfrac{ds}{s}$.
>
> (d) **Shifted $\alpha$-stable** ($\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$, $\alpha\in(0,2),\kappa\ge 0$): $V_\phi(ds)=\dfrac{\alpha}{2}\,e^{-\kappa s}\,\dfrac{ds}{s}$.
>
> Cases (a)–(c) are the paper's Example 2.10; case (d) is the shifted $\alpha$-stable case computed in §3.1.4.

---

# Computation

**Case (a): Brownian, $\phi(\lambda)=\lambda$, $\psi^\phi_t=\delta_t$.** The atom at $s=t$ makes the inner integral trivial: $\int_{(0,\infty)}h(s)\,\psi^\phi_t(ds)=h(t)$. So
$$\int h(s)\,V_\phi(ds) \;=\; \int_0^\infty\frac{dt}{t}\,h(t) \;=\; \int_0^\infty h(s)\,\frac{ds}{s},$$
whence $V_\phi(ds)=\frac{ds}{s}$. **The multiplicative Haar measure returns.**

**Case (b): Killing, $\phi(\lambda)=\lambda+\kappa$, $\psi^\phi_t=e^{-\kappa t}\delta_t$.** Same localisation, now with the exponential factor:
$$\int_{(0,\infty)}h(s)\,\psi^\phi_t(ds)=e^{-\kappa t}h(t),$$
so
$$\int h(s)\,V_\phi(ds) \;=\; \int_0^\infty\frac{dt}{t}\,e^{-\kappa t}h(t) \;=\; \int_0^\infty h(s)\,e^{-\kappa s}\,\frac{ds}{s},$$
whence $V_\phi(ds)=e^{-\kappa s}\frac{ds}{s}$. **The Haar measure, exponentially tilted.**

**Case (c): $\alpha$-stable, $\phi(\lambda)=\lambda^{\alpha/2}$, $\psi^\phi_t(ds)=\eta^\alpha_t(s)\,ds$.** Now the inner integral is a genuine integral, not a point evaluation. By definition,
$$\int h(s)\,V_\phi(ds) \;=\; \int_0^\infty\frac{dt}{t}\int_0^\infty h(s)\,t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})\,ds.$$
Swap the order of integration (Tonelli, since everything is non-negative and the measures are $\sigma$-finite):
$$\int h(s)\,V_\phi(ds) \;=\; \int_0^\infty h(s)\Bigg[\int_0^\infty \frac{1}{t}\,t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})\,dt\Bigg]\,ds.$$
The task is to evaluate the bracketed inner integral in $t$ for fixed $s>0$. Substitute $u=s\,t^{-2/\alpha}$, so $t=(s/u)^{\alpha/2}$. Then $\log t=\frac{\alpha}{2}(\log s-\log u)$, so $\frac{dt}{t}=-\frac{\alpha}{2}\frac{du}{u}$; equivalently $\frac{1}{t}\,t^{-2/\alpha}\,dt=t^{-2/\alpha}\frac{dt}{t}=\frac{u}{s}\cdot(-\frac{\alpha}{2}\frac{du}{u})=-\frac{\alpha}{2s}\,du$. As $t$ ranges over $(0,\infty)$, $u$ ranges over $(\infty,0)$ (since $t\to 0^+$ makes $u\to\infty$ and $t\to\infty$ makes $u\to 0^+$); reversing to $(0,\infty)$ cancels the minus sign. So
$$\int_0^\infty\frac{1}{t}\,t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})\,dt \;=\; \frac{\alpha}{2s}\int_0^\infty g_{\alpha/2}(u)\,du \;=\; \frac{\alpha}{2s},$$
using that $g_{\alpha/2}$ is a probability density ($\int_0^\infty g_{\alpha/2}=1$). Substituting back,
$$\int h(s)\,V_\phi(ds) \;=\; \int_0^\infty h(s)\cdot\frac{\alpha}{2s}\,ds \;=\; \frac{\alpha}{2}\int_0^\infty h(s)\,\frac{ds}{s},$$
whence $V_\phi(ds)=\frac{\alpha}{2}\frac{ds}{s}$. **The multiplicative Haar measure again, up to the constant $\alpha/2$.**

**Case (d): Shifted $\alpha$-stable, $\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$, $\psi^\phi_t(ds)=e^{-\kappa s}\eta^\alpha_t(s)\,ds$.** Apply the case-(c) computation to the *test function* $h(s)e^{-\kappa s}$ in place of $h(s)$ (both are non-negative):
$$\int h(s)\,V_\phi(ds) \;=\; \int_0^\infty\frac{dt}{t}\int_0^\infty h(s)e^{-\kappa s}\eta^\alpha_t(s)\,ds \;\overset{(\text{c})}{=}\; \frac{\alpha}{2}\int_0^\infty h(s)e^{-\kappa s}\,\frac{ds}{s},$$
whence $V_\phi(ds)=\frac{\alpha}{2}e^{-\kappa s}\frac{ds}{s}$. **The killing tilt of case (c).**

---

# Calibration

**Read the pattern.** The four $V_\phi$'s all take the form $c\cdot e^{-\kappa s}\frac{ds}{s}$ for some $(c,\kappa)$: $(1,0)$, $(1,\kappa)$, $(\alpha/2,0)$, $(\alpha/2,\kappa)$. Three of the four are proportional to the scale-invariant Haar $\frac{ds}{s}$; the exceptions are the killed ones, where $e^{-\kappa s}$ breaks scale-invariance. The paper's Remark in §3.1.3 explains this cleanly: the $\alpha/2$-stable subordinator laws are self-similar under $s\mapsto\lambda^{2/\alpha}s$, and $\frac{dt}{t}$ is itself scale-invariant; combining a self-similar law with a scale-invariant weight produces a scale-invariant measure — necessarily a constant multiple of $\frac{ds}{s}$ on $(0,\infty)$. Killing (the shift by $\kappa$) is what breaks self-similarity and lets $V_\phi$ carry non-trivial geometry.

**Sanity check: additivity in $\kappa$.** Case (b) with $\kappa=0$ reduces to case (a): $V_\phi(ds)=\frac{ds}{s}$. Case (d) with $\kappa=0$ reduces to case (c): $V_\phi(ds)=\frac{\alpha}{2}\frac{ds}{s}$. Case (d) with $\alpha=2$ (formally) reduces to case (b): $V_\phi(ds)=e^{-\kappa s}\frac{ds}{s}$ — with the constant $\alpha/2=1$, this matches. All limits are consistent.

**Sanity check: dimensions.** Every $V_\phi$ has the form (dimensionless constant) $\times$ ($e^{-\kappa s}$) $\times$ ($\frac{ds}{s}$). Since $\frac{ds}{s}$ is dimensionally $[\text{time}]^0$ (it is $d(\log s)$), and $e^{-\kappa s}$ requires $\kappa\cdot s$ dimensionless, $\kappa$ has units of $[\text{time}]^{-1}$ — consistent with $\kappa$ being a killing *rate*.

**Sanity check: the Tonelli step in case (c) is legal.** The integrand $(t,s)\mapsto h(s)\,t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})$ is non-negative and jointly measurable; the measures $\frac{dt}{t}$ on $(0,\infty)$ and Lebesgue $ds$ on $(0,\infty)$ are both $\sigma$-finite; so Tonelli applies without integrability hypothesis. The reversal of limits under $u=s\,t^{-2/\alpha}$ is a change of variables in a single integral, whose sign is absorbed by the reversal of orientation — no extra care needed.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.4]] to compute $V_\phi$ concretely for the three Bernstein functions of Example 2.5 (cases (a)–(c)); case (d) is added in §3.1.4 alongside the shifted $\alpha$-stable's mass formula. Together the four $V_\phi$'s populate every free-homotopy-class mass computation of §3.1: [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] rewrites the outer $t$-integral in $\mu^\phi_X(C_X(\gamma^m))$ as an $s$-integral against $V_\phi$, at which point the four densities above are what one substitutes to get the closed-form answers of §3.1.2 (killing), §3.1.3 ($\alpha$-stable), §3.1.4 (shifted $\alpha$-stable), and the trivial §3.1.1 (Brownian).
