---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, analysis]
---

# Signature

| symbol | type |
|---|---|
| $a$ | $\in(0,\infty)$ |
| $b$ | $\in(0,\infty)$ |
| $s$ | integration variable on $(0,\infty)$ |

---

# Statement

> **(GI) Gaussian reciprocal integral identity.** *Precondition:*
> **(P1)** $a>0$;
> **(P2)** $b>0$.
>
> *Conclusion:*
> $$\int_0^\infty s^{-3/2}\,e^{-as-b/s}\,\mathrm{d}s \;=\; \sqrt{\frac{\pi}{b}}\;e^{-2\sqrt{ab}}.$$

> **Companion form**, used once in §7: for $a>0$, $c\geq0$,
> $$\int_{c}^\infty u\,e^{-u^2/4t}\,\mathrm{d}u = 2t\,e^{-c^2/4t},\qquad t>0.$$
> (Elementary: the integrand is $-2t\frac{\mathrm{d}}{\mathrm{d}u}e^{-u^2/4t}$.)

> [!note]- Proof of (GI) (skippable)
> Substitute $u=\sqrt{as}-\sqrt{b/s}$, so $u:\ (0,\infty)\to(-\infty,\infty)$ is an increasing bijection with $u^2=as+b/s-2\sqrt{ab}$ and $\mathrm{d}u=\tfrac12(\sqrt{a/s}+\sqrt{b}\,s^{-3/2})\,\mathrm{d}s$. Writing $I$ for the integral and $J:=\int_0^\infty s^{-1/2}e^{-as-b/s}\,\mathrm{d}s$, the substitution $s\mapsto b/(as)$ gives $J=\sqrt{b/a}\,I$, and
> $$\int_{-\infty}^\infty e^{-u^2}\,\mathrm{d}u = e^{2\sqrt{ab}}\cdot\tfrac12\Big(\sqrt a\,J\,b^{-1/2}\cdot\sqrt b + \sqrt b\,I\Big)\cdot\!\!\ \text{(combining the two halves)} = e^{2\sqrt{ab}}\sqrt b\,I,$$
> whence $I=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$.

---

# Type card

> [!abstract] Type card — (GI)
> **Given.** (P1) $a>0$; (P2) $b>0$.
>
> **Produces.** A positive real number in closed form: $\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$. Note the output depends on $(a,b)$ only through $\sqrt{ab}$ and $b$.
>
> **Lets you.** Discharge every heat-kernel time-integral in the paper. Six computations use it; each is fixed by naming its $(a,b)$.

---

# Status

- **Proved here:** yes, above (it is elementary, but it is invoked six times and is worth having once).
- **Source:** classical; the paper uses it without attribution as "the integral identity".
- **DAG node:** none needed — anchor material (*Analysis of PDEs* 🟢).
- **What is safe to assume:** the conclusion verbatim under $a,b>0$. Note $a=0$ is **not** permitted: the integral diverges at $s\to\infty$.

---

# Used at

| page | $a$ | $b$ | output |
|---|---|---|---|
| [[Constr - The Weighted Heat-Kernel Integral Iϕ]] — Brownian | $\tfrac14$ | $L^2/4$ | $\frac{2\sqrt\pi}{L}e^{-L/2}$ |
| [[Constr - The Weighted Heat-Kernel Integral Iϕ]] — killing $\kappa$ | $\tfrac14+\kappa$ | $L^2/4$ | $\frac{2\sqrt\pi}{L}e^{-L\sqrt{1/4+\kappa}}$ |
| [[Constr - The Weighted Heat-Kernel Integral Iϕ]] — $\alpha$-stable | $\tfrac14$ | $L^2/4$ | as Brownian, $\times\tfrac\alpha2$ |
| [[Constr - The Weighted Heat-Kernel Integral Iϕ]] — shifted $\alpha$-stable | $\tfrac14+\kappa$ | $L^2/4$ | as killing, $\times\tfrac\alpha2$ |
| [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]] | $1$ | $(m\ell_\gamma)^2/4$ | $\frac{2\sqrt\pi}{m\ell_\gamma}e^{-m\ell_\gamma}$ |
| [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]] | — | — | companion form, $c=m\ell_\gamma$ |

---

# Commentary

> [!note]- Commentary (skippable)
> The parameter $a$ is always the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^n}$, shifted by the killing rate: $(n-1)^2/4+\kappa$, so $\tfrac14+\kappa$ on $\mathbb{H}^2$ and $1$ on $\mathbb{H}^3$. The parameter $b$ is always $L^2/4$ with $L$ the real geodesic length. So the output $e^{-2\sqrt{ab}}=e^{-L\sqrt{(n-1)^2/4+\kappa}}$ is where the spectral parameter $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ enters the paper — the $\sqrt{\tfrac14+\kappa}$ in $s$ is exactly $\sqrt a$ here.
>
> Tracking that one substitution across the six rows above is the cheapest way to see why every mass formula in §3 and §7 has the shape it does.
