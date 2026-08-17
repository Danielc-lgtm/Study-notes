---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Subordinator and Subordination of a Semigroup"
  - "Constr - Assumption 2.3 (Strictly Increasing Subordinator)"
tags: [paper, probability, subordination]
---

# Notation

- $\phi$ — a [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; $\psi^\phi_t$ the law of its subordinator at time $t$, a measure on $[0,\infty)$
- $V_\phi$ — the weighted potential measure, a $\sigma$-finite measure on $(0,\infty)$; written $V_\phi(\mathrm{d}s)=V_\phi(s)\,\mathrm{d}s$ when absolutely continuous, which it is in every case the paper treats
- $h$ — a non-negative measurable test function on $(0,\infty)$
- $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(st^{-2/\alpha})$ — the $\alpha/2$-stable subordinator density, $g_{\alpha/2}$ being the standard $\alpha/2$-stable density on $(0,\infty)$
- $\kappa\geq0$ a killing rate, $\alpha\in(0,2)$ a stability index

---

# In plain language

$V_\phi$ is what is left of the subordination after the loop-duration integral has been carried out.

Here is the situation it resolves. A subordinate loop measure carries two integrals: one over the loop duration $t$ with the weight $\mathrm{d}t/t$, and one over the subordination variable $s$ against the law $\psi^\phi_t(\mathrm{d}s)$. The variable $t$ appears nowhere except inside $\psi^\phi_t$ — the geometry of the surface knows nothing about it. So integrate it out first. The result is a single measure on $(0,\infty)$, in the variable $s$, which contains all the information about $\phi$ that the loop measure can see.

The consequence is the architecture of the whole paper. After [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]], the choice of process appears in exactly one place: as the measure being integrated against. Brownian motion, killing, $\alpha$-stable and shifted $\alpha$-stable differ only in $V_\phi$, and each of the paper's special cases is a one-line substitution from the four-line table below.

The name is Schilling–Song–Vondraček's; the *potential measure* of a subordinator is $\int_0^\infty\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}t$, and this is the same thing with the Haar weight $\mathrm{d}t/t$ in place of $\mathrm{d}t$ — hence "weighted".

---

# The construction

> **Definition 2.9 (weighted potential measure).** The **weighted potential measure** $V_\phi$ is the $\sigma$-finite measure on $(0,\infty)$ defined by
> $$\int_{(0,\infty)}h(s)\,V_\phi(\mathrm{d}s) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{(0,\infty)}h(s)\,\psi^\phi_t(\mathrm{d}s)\tag{7}$$
> for every non-negative measurable $h$ for which the right-hand side is finite. When $V_\phi$ is absolutely continuous one writes $V_\phi(\mathrm{d}s)=V_\phi(s)\,\mathrm{d}s$; this holds for all the Bernstein functions of this paper.

Two remarks on the definition as stated. It is a definition *by its action on test functions*, which is what one wants, since every use of $V_\phi$ downstream is against a specific $h$. And the integral on the right runs over $(0,\infty)$ rather than $[0,\infty)$ — legitimate precisely because Assumption 2.3 gives $\psi^\phi_t(\{0\})=0$, so no mass is discarded.

---

# Type card

> [!abstract] Type card — Definition 2.9 (weighted potential measure)
> **Given.** A Bernstein function $\phi$ satisfying Assumption 2.3, with subordinator laws $\{\psi^\phi_t\}_{t>0}$ on $[0,\infty)$.
>
> **Produces.** A $\sigma$-finite measure $V_\phi$ on $(0,\infty)$ — **not finite**: in every case in the table below it has a $\mathrm{d}s/s$ singularity at the origin. Absolutely continuous in every case treated.
>
> **Lets you.** Replace the double integral $\int_0^\infty\frac{\mathrm{d}t}{t}\int_{[0,\infty)}(\cdots)\,\psi^\phi_t(\mathrm{d}s)$ by the single integral $\int_{(0,\infty)}(\cdots)\,V_\phi(\mathrm{d}s)$ — the collapse performed by [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] and used in every mass computation of §3 and §7.

---

# Properties relied on later

**The four cases (Example 2.10).** These are the substitutions every special case in the paper runs on.

| $\phi(\lambda)$ | process | $\psi^\phi_t$ | $V_\phi(\mathrm{d}s)$ |
|---|---|---|---|
| $\lambda$ | Brownian motion | $\delta_t$ | $\mathrm{d}s/s$ |
| $\lambda+\kappa$ | Brownian with killing | $e^{-\kappa t}\delta_t$ | $e^{-\kappa s}\,\mathrm{d}s/s$ |
| $\lambda^{\alpha/2}$ | $\alpha$-stable | $\eta^\alpha_t(s)\,\mathrm{d}s$ | $\tfrac{\alpha}{2}\,\mathrm{d}s/s$ |
| $(\lambda+\kappa)^{\alpha/2}$ | shifted $\alpha$-stable | $e^{-\kappa s}\eta^\alpha_t(s)\,\mathrm{d}s$ | $\tfrac{\alpha}{2}e^{-\kappa s}\,\mathrm{d}s/s$ |

> [!note]- Calculation (skippable) — the four entries
> **(a) Brownian, $\phi(\lambda)=\lambda$.** Here $\psi^\phi_t=\delta_t$, so the inner integral in (7) is $h(t)$ and the $\mathrm{d}t/t$ integral **localises at $s=t$**: $\int_0^\infty h(t)\,\mathrm{d}t/t$. Hence $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ — the Haar measure passes through untouched.
>
> **(b) Killing, $\phi(\lambda)=\lambda+\kappa$.** Now $\psi^\phi_t=e^{-\kappa t}\delta_t$, and the same localisation gives $\int_0^\infty h(t)e^{-\kappa t}\,\mathrm{d}t/t$, so $V_\phi(\mathrm{d}s)=e^{-\kappa s}\,\mathrm{d}s/s$.
>
> **(c) $\alpha$-stable, $\phi(\lambda)=\lambda^{\alpha/2}$.** The law is $\psi^\phi_t(\mathrm{d}s)=t^{-2/\alpha}g_{\alpha/2}(st^{-2/\alpha})\,\mathrm{d}s$. Substitute $u=st^{-2/\alpha}$ in (7): for fixed $s$, as $t$ ranges over $(0,\infty)$ so does $u$, with $\mathrm{d}t/t = -\tfrac{\alpha}{2}\,\mathrm{d}u/u$ up to orientation, and
> $$\int_0^\infty\frac1t\,t^{-2/\alpha}g_{\alpha/2}\big(st^{-2/\alpha}\big)\,\mathrm{d}t = \frac{\alpha}{2s}\int_0^\infty g_{\alpha/2}(u)\,\mathrm{d}u = \frac{\alpha}{2s},$$
> since $g_{\alpha/2}$ is a probability density. Hence $V_\phi(\mathrm{d}s)=\tfrac{\alpha}{2}\,\mathrm{d}s/s$.
>
> **(d) Shifted $\alpha$-stable, $\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$.** From $e^{-t(\lambda+\kappa)^{\alpha/2}}=\int_0^\infty e^{-u(\lambda+\kappa)}\eta^\alpha_t(u)\,\mathrm{d}u = \int_0^\infty e^{-\lambda s}e^{-\kappa s}\eta^\alpha_t(s)\,\mathrm{d}s$, the law is the exponential tilt $\psi^\phi_t(\mathrm{d}s)=e^{-\kappa s}\eta^\alpha_t(s)\,\mathrm{d}s$. Applying the collapse of (c) to $h(s)e^{-\kappa s}$ rather than $h(s)$ gives $V_\phi(\mathrm{d}s)=\tfrac{\alpha}{2}e^{-\kappa s}\,\mathrm{d}s/s$.

**The scale-invariance obstruction, and why it is structural.** In case (c) the Haar measure is preserved up to the constant $\alpha/2$, and this is forced rather than lucky. Self-similar subordinators are exactly the stable ones; the weight $\mathrm{d}t/t$ is itself scale-invariant; combining the two scalings in (7) leaves only measures on $(0,\infty)$ compatible with both, and those are precisely the constant multiples of $\mathrm{d}s/s$. **Consequence: any scale-invariant subordination gives $\mu^\phi_X = c\,\mu_X$ and reveals nothing about the geometry of $X$ that Brownian motion did not already reveal.** Breaking the scale invariance is exactly what case (d) does, and it is the paper's own suggested repair — see §3.1.3.

---

# Consumed by

- [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] — the identity that makes $V_\phi$ usable
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — $V_\phi$ is the measure the closed-form mass is an integral against; assumed as a hypothesis
- [[Constr - The Weighted Heat-Kernel Integral Iϕ|Definition 3.6]] — $I_\phi$ is defined as an integral against $V_\phi$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — the same role in three dimensions
- [[Thm - Selberg Zeta Criterion|Lemma 4.2]] — indirectly, through $I_\phi$: the criterion is a condition on what $V_\phi$ does to the heat-kernel factor
- [[§3 Decomposition over Homotopy Classes]] §3.1.1–3.1.4 — the four special cases are substitutions of the four table entries

---

# Where this sits in my DAG

Reduces to [[Def - Subordinator and Subordination of a Semigroup]] and [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]] on the probabilistic side, and to [[Thm - Fubini-Tonelli Theorem|Tonelli]] on the measure-theoretic side, all of which are anchors or one step from them. The stable-density computation in case (c) uses only the change of variables $u=st^{-2/\alpha}$ and the fact that $g_{\alpha/2}$ integrates to $1$; the explicit form of $g_{\alpha/2}$ is never needed, which is worth noticing — the paper cites Bogdan et al. for it but no formula in the paper depends on it.
