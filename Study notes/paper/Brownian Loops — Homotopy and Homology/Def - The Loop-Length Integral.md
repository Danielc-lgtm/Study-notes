---
type: definition
subject: probability-geometry
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Weighted Potential Measure"
  - "Def - Heat Kernel and Heat Semigroup"
tags: [paper, brownian-loops, subordinate-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 3.6"
---

# Notation

- $\phi : (0,\infty)\to(0,\infty)$ — a Bernstein function (Assumption 2.3): $C^\infty$, non-decreasing, $\phi'$ completely monotone, $\phi(0^+)=0$.
- $V_\phi$ — the weighted potential measure on $(0,\infty)$: $V_\phi(ds) = \int_0^\infty \psi^\phi_t(ds)\,dt/t$, where $\psi^\phi_t$ is the law of the $\phi$-subordinator $S_t$ (Definition 2.9).
- $L > 0$ — a positive real parameter (thought of as a total translation length; when applied to a class $C_X(\gamma^m)$, $L = m\ell_\gamma$).
- $s$ — the "internal-clock" or subordination variable, ranging over $(0,\infty)$.

> [!recall]- Bernstein function $\phi$ and its weighted potential measure $V_\phi$
> **Formally:** a Bernstein function $\phi:(0,\infty)\to(0,\infty)$ has the Lévy–Khintchine form $\phi(\lambda) = a + b\lambda + \int_0^\infty(1-e^{-\lambda s})\,\nu(ds)$; its subordinator has Laplace exponent $\phi$. The **weighted potential measure** on $(0,\infty)$ is $V_\phi(ds) := \int_0^\infty \psi^\phi_t(ds)\,\frac{dt}{t}$ where $\psi^\phi_t$ is the law of $S_t$ (Definition 2.9); this is finite on compact subsets of $(0,\infty)$ under Assumption 2.3.
> **In words:** $V_\phi$ is what the subordinator's family of laws collapses to when averaged against the loop-measure weight $dt/t$. It carries all of $\phi$'s information in one measure on the subordination variable $s$.
> **Concretely:** $\phi(\lambda) = \lambda$: $V_\phi(ds) = ds/s$; $\phi(\lambda) = \lambda + \kappa$: $V_\phi(ds) = e^{-\kappa s}ds/s$; $\phi(\lambda) = \lambda^{\alpha/2}$: $V_\phi(ds) = (\alpha/2)\,ds/s$; $\phi(\lambda) = (\lambda + \kappa)^{\alpha/2}$: $V_\phi(ds) = (\alpha/2)e^{-\kappa s}ds/s$. Full detail: [[Def - Weighted Potential Measure]] and [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- Where the integrand $e^{-s/4}e^{-L^2/(4s)}/(2\sqrt{\pi s})$ comes from
> **Formally:** the factor $e^{-L^2/(4s)}/(2\sqrt{\pi s})$ is the 1-D Euclidean heat kernel at time $s$ from $0$ to $L$ (evaluated with the paper's normalisation of Brownian variance); $e^{-s/4}$ is the spectral-bottom correction of the $\mathbb{H}^2$ heat kernel ($1/4 = (\frac12)^2$ is the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$). Together, $e^{-s/4}e^{-L^2/(4s)}/(2\sqrt{\pi s})$ is exactly the *spatial* strip integral of the $\mathbb{H}^2$ heat kernel with the geometric prefactor $\ell_\gamma/[2\sinh(L/2)]$ stripped off (Wang–Xue Lemma 3.4).
> **In words:** the integrand of $I_\phi(L)$ is precisely the axis-plus-curvature part of the strip integral — the piece that depends on the subordination variable $s$. The purely geometric parts of the class-mass ($\ell_\gamma$, $\sinh(L/2)$, the winding $m$) have already been pulled outside.
> **Concretely:** at $L = \log 2 \approx 0.693$, $s = 1$: integrand equals $e^{-1/4}e^{-(\log 2)^2/4}/(2\sqrt\pi) \approx 0.779\cdot 0.883/3.545 \approx 0.194$; as $s\to 0^+$, the $e^{-L^2/(4s)}$ crushes to zero (short paths cannot travel distance $L$); as $s\to\infty$, the $e^{-s/4}/\sqrt s$ decays exponentially. So the integrand is concentrated near $s \sim L$ (the diffusive time-scale to cover distance $L$). Full detail: [[Lemma - Wang-Xue Strip Integral]].

---

# Statement

> **Definition (loop-length integral; Belyaev–Huseynli 3.6).** For a Bernstein function $\phi$ with weighted potential measure $V_\phi$ (Definition 2.9) and $L > 0$, the **loop-length integral** is
> $$I_\phi(L) \;:=\; \int_{(0,\infty)} \frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds).$$
> With this abbreviation, [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] reads $\mu^\phi_X\big(C_X(\gamma^m)\big) = \dfrac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)$ with $L = m\ell_\gamma$.

---

# In One Line

The purely one-dimensional integral (over the subordination variable $s$) that carries all the $\phi$-dependence of a class-mass; the geometry enters only through $L = m\ell_\gamma$ and the prefactor $\ell_\gamma/[2\sinh(L/2)]$.

---

# Motivation and Unpacking

**Why isolate this integral?** [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] shows that every subordinate-loop class-mass factors into (a purely geometric prefactor) $\times$ (a $\phi$-and-$L$-only integral). The prefactor depends only on $(\ell_\gamma, m)$; the $\phi$-and-$L$-only integral depends only on the Bernstein function $\phi$ and the total translation length $L = m\ell_\gamma$. Isolating the second factor as $I_\phi(L)$ separates the two roles: **geometry** (which packages via the geodesic length $\ell_\gamma$ and its integer multiples $L$) versus **process** (which packages via the weighted potential measure $V_\phi$).

The paper then treats $I_\phi$ as the *fundamental analytic object* of the section. §4 and §5 study its behaviour as $L$ ranges over the length spectrum $\{m\ell_\gamma\}$; the sum $\sum_{\gamma,m} \frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)$ over primitive geodesics and windings is the total mass of the loop measure (minus contractible + peripheral contributions), and its closed form is the Selberg zeta function.

**Closed forms in the concrete cases.** Applying the Gaussian-type integral $\int_0^\infty s^{-3/2}e^{-as - b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ (see the recall in [[Thm - Mass of a Subordinate Brownian Loop Class]]) to each of the four cases §3.1.1–3.1.4:
- **Brownian** ($V_\phi(ds) = ds/s$): $I_{\mathrm{BM}}(L) = e^{-L/2}/L$.
- **Killing** ($V_\phi(ds) = e^{-\kappa s}ds/s$, $\kappa\ge 0$): $I_\kappa(L) = e^{-L\sqrt{1/4+\kappa}}/L$.
- **$\alpha$-stable** ($V_\phi(ds) = (\alpha/2)ds/s$): $I_\alpha(L) = (\alpha/2)\cdot e^{-L/2}/L$.
- **Shifted $\alpha$-stable** ($V_\phi(ds) = (\alpha/2)e^{-\kappa s}ds/s$): $I_\phi(L) = (\alpha/2)\cdot e^{-L\sqrt{1/4+\kappa}}/L$.

Each is a single elementary function of $L$; the whole class-mass is then $\ell_\gamma/[2\sinh(L/2)]$ times this.

**Small concrete instance.** Take the Brownian case ($V_\phi = ds/s$) with $L = 1$:
$$I_{\mathrm{BM}}(1) = \int_0^\infty\frac{e^{-s/4}e^{-1/(4s)}}{2\sqrt{\pi}\,s^{3/2}}\,ds \;=\; \frac{e^{-1/2}}{1} \;=\; e^{-1/2} \approx 0.607.$$
Multiplied by $\ell_\gamma/[2\sinh(1/2)]$ (which at $L = \ell_\gamma = 1$ is $1/(2\sinh(1/2)) \approx 0.958$), this gives $\mu_X(C_X(\gamma)) \approx 0.582 \approx 1/(e - 1)$ — matching the Wang–Xue formula $1/(e^L - 1)$ at $L = 1$.

**Standard names.** The paper uses the term "loop-length integral" for $I_\phi$. It is not universally standardised; alternate presentations (Buser, Sarnak) work directly with the class-mass or with the trace-formula spectral function, without naming this specific 1-D integral. When citing outside this paper, describe it as "the potential-measure integral $\int e^{-s/4}e^{-L^2/(4s)}/(2\sqrt{\pi s})\,V_\phi(ds)$".

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.1]] to abbreviate [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]]. Studied in detail in [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4]] to sum the masses into a Selberg zeta function, and in [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]] to relate $|\mu^\kappa_X|_{\mathrm{reg}}$ to the zeta-regularised determinant.
