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

**Strategy.** Rescale $s$ so the exponent becomes $-c(v+1/v)$ with $c=\sqrt{ab}$; then the substitution $w=\sqrt v-1/\sqrt v$ turns the symmetrised integrand into a bare Gaussian.

> [!note]- Proof of (GI) (skippable)
> Put $s=\sqrt{b/a}\,v$. Then $s^{-3/2}\,\mathrm{d}s=(b/a)^{-1/4}v^{-3/2}\,\mathrm{d}v$ and $as+b/s=c\,(v+1/v)$ with $c:=\sqrt{ab}$, so
> $$I:=\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\Big(\tfrac ab\Big)^{1/4}K(c),\qquad K(c):=\int_0^\infty v^{-3/2}e^{-c(v+1/v)}\,\mathrm{d}v.$$
> The substitution $v\mapsto1/v$ leaves $v+1/v$ fixed and carries $v^{-3/2}\,\mathrm{d}v$ to $v^{-1/2}\,\mathrm{d}v$, so $K(c)=\int_0^\infty v^{-1/2}e^{-c(v+1/v)}\,\mathrm{d}v$ as well. Adding the two expressions and substituting $w=\sqrt v-1/\sqrt v$, for which $\mathrm{d}w=\tfrac12(v^{-1/2}+v^{-3/2})\,\mathrm{d}v$ and $v+1/v=w^2+2$,
> $$2K(c)=\int_0^\infty\big(v^{-1/2}+v^{-3/2}\big)e^{-c(v+1/v)}\,\mathrm{d}v=2\int_{-\infty}^{\infty}e^{-c(w^2+2)}\,\mathrm{d}w=2e^{-2c}\sqrt{\pi/c}.$$
> Hence $K(c)=e^{-2c}\sqrt{\pi/c}$ and
> $$I=\Big(\tfrac ab\Big)^{1/4}e^{-2\sqrt{ab}}\sqrt{\pi}\,(ab)^{-1/4}=\sqrt{\frac\pi b}\;e^{-2\sqrt{ab}}.\;\square$$

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
