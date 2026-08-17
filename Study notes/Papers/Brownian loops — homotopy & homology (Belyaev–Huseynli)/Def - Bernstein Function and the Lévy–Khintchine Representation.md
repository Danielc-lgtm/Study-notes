---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs: []
tags: [paper, probability, subordination, levy-processes]
---

# Notation

- $\phi : (0,\infty)\to[0,\infty)$ — the Bernstein function
- $\phi^{(n)}$ — the $n$-th derivative
- $(a,b,\nu)$ — the Lévy–Khintchine triple: $a\geq0$ the **killing rate**, $b\geq0$ the **drift**, $\nu$ the **Lévy measure** on $(0,\infty)$
- $\alpha\in(0,2)$ — the stability index; $\kappa\geq0$ a constant killing rate
- $g_{\alpha/2}$ — the density of the standard $\alpha/2$-stable distribution on $(0,\infty)$
- $\eta^\alpha_t(s) = t^{-2/\alpha}g_{\alpha/2}(st^{-2/\alpha})$ — the density of the $\alpha/2$-stable subordinator law at time $t$

---

# In plain language

A Bernstein function is the Laplace exponent of an increasing Lévy process. Equivalently, and this is the definition the paper uses, it is a smooth non-negative function on $(0,\infty)$ whose derivative is completely monotone: $\phi'\geq0$, $\phi''\leq0$, $\phi'''\geq0$, and so on with alternating signs.

The alternating-sign condition looks arbitrary until you see the representation theorem, which says every such $\phi$ is
$$\phi(\lambda) = a + b\lambda + \int_0^\infty(1-e^{-\lambda s})\,\nu(\mathrm{d}s),$$
and the three pieces have meanings. The constant $a$ is a killing rate — the clock stops at rate $a$. The linear term $b\lambda$ is a deterministic drift — the clock runs at speed $b$. And the integral is a superposition of jumps of size $s$ arriving at rate $\nu(\mathrm{d}s)$. So reading a Bernstein function is reading a recipe for a random clock, and the sign-alternation condition is just what "increasing process built out of these three ingredients" looks like from the Laplace side.

For the paper, $\phi$ is the whole parametrisation of the family of processes it works with. Everything in §3 onwards is a statement holding for every $\phi$, with the special cases obtained by substitution. The four that matter are collected below, and it is worth noticing what the triple does in each: the shift $\kappa$ turns on $a$; the stable exponent turns off $b$ and turns on an infinite $\nu$; and turning on $\nu$ is exactly what makes the resulting process jump.

---

# The definition

> **Definition (Bernstein function).** A function $\phi : (0,\infty)\to[0,\infty)$ is a **Bernstein function** if it is $C^\infty$ and
> $$(-1)^{n-1}\phi^{(n)}(\lambda)\geq0\qquad\text{for all }n\geq1\text{ and all }\lambda>0.$$

> **Theorem (Lévy–Khintchine representation).** Every Bernstein function admits a **unique** representation
> $$\phi(\lambda) = a + b\lambda + \int_0^\infty\big(1-e^{-\lambda s}\big)\,\nu(\mathrm{d}s),\qquad\lambda>0,\tag{1}$$
> where $a\geq0$ is the killing rate, $b\geq0$ the drift, and $\nu$ is a measure on $(0,\infty)$ satisfying $\int_0^\infty(1\wedge s)\,\nu(\mathrm{d}s)<\infty$.

The integrability condition $\int(1\wedge s)\,\nu(\mathrm{d}s)<\infty$ is what makes the integral converge: near $s=0$ one has $1-e^{-\lambda s}\approx\lambda s$, so small jumps must be integrable against $s$; near $s=\infty$ one has $1-e^{-\lambda s}\approx1$, so large jumps must be finite in number. Note that $\nu$ itself need **not** be finite — and when $\nu(0,\infty)=\infty$ the process makes infinitely many jumps in any time interval, which is precisely one half of [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]].

---

# Types and signatures

- $\phi : (0,\infty)\to[0,\infty)$ — smooth, non-negative, non-decreasing, concave
- $a\in[0,\infty)$ — a number; $\phi(0^+)=a$
- $b\in[0,\infty)$ — a number; $b=\lim_{\lambda\to\infty}\phi(\lambda)/\lambda$
- $\nu$ — a measure on $(0,\infty)$, **not** in general finite, with $\int_0^\infty(1\wedge s)\,\nu(\mathrm{d}s)<\infty$
- $\eta^\alpha_t : (0,\infty)\to(0,\infty)$ — a probability density in $s$ for each fixed $t>0$

---

# Example

The four Bernstein functions that carry the paper, and what each does to the process.

| $\phi(\lambda)$ | resulting process | triple $(a,b,\nu)$ | law $\psi^\phi_t$ |
|---|---|---|---|
| $\lambda$ | Brownian motion (no subordination) | $(0,1,0)$ | $\delta_t$ |
| $\lambda+\kappa$, $\kappa>0$ | Brownian with killing | $(\kappa,1,0)$ | $e^{-\kappa t}\delta_t$ |
| $\lambda^{\alpha/2}$, $\alpha\in(0,2)$ | $\alpha$-stable (pure jump) | $(0,0,\nu_\alpha)$ | density $\eta^\alpha_t(s)$ |
| $(\lambda+\kappa)^{\alpha/2}$ | shifted $\alpha$-stable | composition of the two above | $e^{-\kappa s}\eta^\alpha_t(s)\,\mathrm{d}s$ |

with $\nu_\alpha(\mathrm{d}s)=\frac{\alpha/2}{\Gamma(1-\alpha/2)}s^{-1-\alpha/2}\,\mathrm{d}s$. The framework also covers gamma, inverse Gaussian and relativistic stable subordinators, which the paper mentions but does not compute.

Check the reading of the triple against the table. For $\phi(\lambda)=\lambda$: no killing, unit drift, no jumps — the clock is the identity and nothing happens, which is why $\psi^\phi_t=\delta_t$. For $\phi(\lambda)=\lambda+\kappa$: same clock, but killed at rate $\kappa$, so $|\psi^\phi_t|=e^{-\kappa t}<1$. For $\phi(\lambda)=\lambda^{\alpha/2}$: no drift at all, so the clock advances *only* by jumps, and $\nu_\alpha(0,\infty)=\infty$ so there are infinitely many of them in any interval — hence a pure-jump process even though the underlying $B$ is a diffusion. The boundary case $\alpha=2$ gives $\phi(\lambda)=\lambda$ and recovers Brownian motion.

**Near-miss non-example.** $\phi(\lambda)=\lambda+\kappa$ with $\kappa<0$ is **not** a Bernstein function: its killing rate is negative, so the representation (1) fails at $n=0$, so to speak — $\phi$ takes negative values near $\lambda=0$ and there is no increasing Lévy process with this exponent. The paper nevertheless uses the range $\kappa\in[-\tfrac14,0)$ (Remark 3.7), on the grounds that the *formula* (26) continues to make sense analytically and the defining integral still converges. The cutoff at $\kappa=-\tfrac14$ is not arbitrary: it is where $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ stops being real, and $\kappa=-\tfrac14$ gives $s=\tfrac12$, the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$. So the extended range is the whole real-$s$ range, cut off by the spectrum rather than by the Bernstein condition.

A second near-miss worth naming: a **compound Poisson** subordinator has finite $\nu$ and zero drift, so $\phi(\lambda)=\int(1-e^{-\lambda s})\nu(\mathrm{d}s)$ with $\nu(0,\infty)<\infty$ — a perfectly good Bernstein function whose law $\psi^\phi_t$ has an atom at $s=0$ (the clock has not moved yet). Its semigroup therefore has no transition density, and this is exactly what Assumption 2.3 excludes.

---

# Used in this paper at

- [[Def - Subordinator and Subordination of a Semigroup]] — $\phi$ is the Laplace exponent of the subordinator and, by functional calculus, the map $A\mapsto\phi(A)$ on generators
- [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]] — the standing hypothesis is a condition on $(b,\nu)$
- [[Constr - The Weighted Potential Measure Vϕ]] — $V_\phi$ is built from the laws $\psi^\phi_t$, hence from $\phi$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]], [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — hypothesised as "a Bernstein function satisfying Assumption 2.3"
- [[Thm - Selberg Zeta Criterion|Lemma 4.2]], [[Thm - Finiteness of the Total Mass|Corollary 4.7]] — quantified over the paper's Bernstein functions, with $s(\phi)$ the attached spectral parameter

---

# Where this sits in my DAG

Anchors. Completely monotone functions, Laplace transforms and their inversion, and Lévy processes with their Laplace exponents all come from *Advanced Probability / Measure-Theoretic* (🟢) and *SDEs* (🟢). The Lévy–Khintchine representation for subordinators is a specialisation of the Lévy–Khintchine formula for Lévy processes, and the reference for the systematic theory is Schilling–Song–Vondraček, *Bernstein functions*. Nothing here needs a further page.
