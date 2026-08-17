---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Eisenstein Series and the Continuous Spectrum"
  - "Def - Zeta-Regularised Determinant of the Laplacian"
tags: [paper, spectral-geometry, determinants, renormalisation]
---

# Notation

- $\bar X$ — the compactification of $X$ obtained by capping each end with a circle at infinity
- $x$ — a **boundary defining function**: a smooth function on $\bar X$ vanishing to first order at the ends; $\mu$ a smooth density
- $\mathrm{FP}_{z=0}$ — the finite part at $z=0$ of a meromorphic continuation
- ${}^0\!\!\int_X f\mu$ — the renormalised integral; ${}^0\mathrm{Area}(g)$ the renormalised area
- ${}^0\mathrm{Tr}$ — the renormalised trace, or $0$-trace; $\zeta^0_X$ the associated zeta function; $\det_0\Delta_X$ the renormalised determinant
- $P$ — the projection onto the $L^2$ null space of $\Delta_X$
- $\chi(X)$ — the Euler characteristic

---

# In plain language

On a cusped surface the heat semigroup is not trace class, so $\int_X p_X(t,z,z)\,\mathrm{d}\mathrm{vol}_g(z)$ diverges — the diagonal does not decay fast enough in the cusps. The fix is not to avoid the divergent integral but to **assign it a finite value in a canonical way**.

The device is standard regularisation, applied to an integral rather than to a series. Compactify $X$ by capping each end with a circle at infinity, giving $\bar X$ with a boundary defining function $x$ vanishing to first order at the ends. For a function $f$ with a controlled expansion at the ends, the integral $\int_X x^z f\mu$ converges when $\operatorname{Re}(z)$ is large — the factor $x^z$ kills the divergence — and continues meromorphically in $z$. Its **finite part at $z=0$** is the renormalised integral. **The extra power $x^z$ plays exactly the role that $t^s$ plays in the Mellin definition of $\zeta_X$**; §5.2 is §5.1's regularisation applied one level lower down, to the integral rather than to the sum.

Applying this to the heat-kernel diagonal gives the $0$-trace, and then everything of §5.1 runs: Mellin transform, spectral zeta, derivative at $0$, determinant. On a closed surface the $0$-trace is the ordinary trace and $\det_0$ reduces to $\det_\zeta$, so nothing is lost.

Two sanity checks that the renormalisation is the right one. Applied to the volume form it gives the **renormalised area** ${}^0\mathrm{Area}(g)$, which for a hyperbolic metric equals $-2\pi\chi(X)$ — the Gauss–Bonnet answer, exactly what an area *should* be. And the Riesz version defined above agrees with the Hadamard version, which cuts the ends off at $x\geq\epsilon$ and takes the finite part as $\epsilon\to0$; the two agreeing means the value does not depend on how the cutoff is organised.

**There was a choice, and the paper names the alternative.** One could instead define a **relative** determinant, comparing $\Delta_X$ to a model operator along the ends so that the divergent parts cancel. The paper follows Melrose's microlocal route instead, keeping $\Delta_X$ itself and regularising the trace. The main insight there is that a hyperbolic surface has a natural compactification on which the heat kernel has a *controlled asymptotic expansion at the ends*, so the divergent part is identifiable and removable.

---

# The definition

> **The renormalised integral.** Fix the compactification $\bar X$ with a boundary defining function $x$ — a smooth function vanishing to first order at the ends — and a smooth density $\mu$. For $f$ with a controlled expansion at the ends, the integral $\int_X x^zf\mu$ converges when $\operatorname{Re}(z)$ is large and continues meromorphically in $z$; its finite part at $z=0$ is the **renormalised integral**
> $$^0\!\!\int_X f\mu := \mathop{\mathrm{FP}}_{z=0}\int_X x^z f\mu.\tag{59}$$
> This is the **Riesz** renormalisation; the **Hadamard** version cuts the ends off at $x\geq\epsilon$ and takes the finite part as $\epsilon\to0$, and the two agree for the functions used here.
>
> Applied to the volume form it gives the **renormalised area** ${}^0\mathrm{Area}(g):={}^0\!\!\int_X\mathrm{d}\mathrm{vol}_g$, which for a hyperbolic metric equals $-2\pi\chi(X)$ by the Gauss–Bonnet theorem for such metrics.

> **The renormalised trace ($0$-trace).** For a trace-class operator with continuous kernel, Lidskii's theorem computes the trace as the integral of the diagonal. On a cusped surface the heat kernel is not trace class, but its diagonal $p_X(t,z,z)$ still has a controlled expansion at the ends, so the divergent integral of the diagonal is replaced by its renormalised value:
> $$^0\mathrm{Tr}\big(e^{-t\Delta_X}\big) := {}^0\!\!\int_X p_X(t,z,z)\,\mathrm{d}\mathrm{vol}_g(z),\tag{60}$$
> defined for each $t>0$. As $t\to\infty$ it converges exponentially to the rank of the $L^2$ null space; as $t\to0$ it has an asymptotic expansion in powers of $t$ and $t\log t$, **the logarithmic terms coming from the cusps**.

> **The renormalised determinant.** Via the Mellin transform,
> $$\zeta^0_X(s) := \frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}\,{}^0\mathrm{Tr}\big(e^{-t\Delta_X}-P\big)\,\mathrm{d}t,\tag{61}$$
> where $P$ is the projection onto the $L^2$ null space, subtracted so that the $t\to\infty$ end converges. The short-time expansion gives $\zeta^0_X$ a meromorphic continuation to $\mathbb{C}$ that is regular at the origin, and the **renormalised determinant** is
> $$\det{}_0\Delta_X := e^{-(\zeta^0_X)'(0)}.\tag{62}$$
> On a closed surface the $0$-trace is the ordinary trace and $\det_0$ reduces to the zeta-regularised determinant of the compact case.

---

# Types and signatures

- $x : \bar X\to[0,\infty)$ — smooth, vanishing to first order exactly at the ends; **not canonical**, but the finite part is independent of the choice for the functions used
- ${}^0\!\!\int_X : \{f\text{ with controlled expansion}\}\to\mathbb{R}$ — a linear functional; **not** a positive functional, and not an integral against any measure
- ${}^0\mathrm{Tr}(e^{-t\Delta_X}) : (0,\infty)\to\mathbb{R}$ — finite for each $t>0$, exponentially convergent to $\operatorname{rank}(P)$ as $t\to\infty$
- $\zeta^0_X$ — meromorphic on $\mathbb{C}$, **regular at $0$**
- $\det_0\Delta_X\in(0,\infty)$ — a number; equals $\det_\zeta\Delta_X$ when $X$ is closed

**The $t\log t$ terms are the new feature.** On a closed surface the short-time heat-trace expansion has only powers of $t$; the logarithms here come from the cusps, and they are what make the renormalisation necessary rather than cosmetic.

---

# Example

The renormalised area, as a check. For a hyperbolic metric on a geometrically finite surface, ${}^0\mathrm{Area}(g)=-2\pi\chi(X)$. On a closed surface of genus $g$ this is $-2\pi(2-2g)=4\pi(g-1)$, the honest area — the renormalisation does nothing when nothing needs renormalising. On a cusped or funnelled surface the actual area may be infinite (funnels) or finite but with the renormalised value differing (cusps), and in both cases the answer is the topological one. **A renormalisation that returns Gauss–Bonnet on the volume form is a renormalisation one can trust.**

**Near-miss non-example — the naive trace.** $\int_X p_X(t,z,z)\,\mathrm{d}\mathrm{vol}_g(z)$ diverges outright on a cusped surface, because $p_X(t,z,z)$ does not decay in the cusps. There is no value to take; the renormalisation supplies one. Similarly $\sum_j\lambda_j^{-s}$ has no meaning since the spectrum is not discrete — see [[Def - Eisenstein Series and the Continuous Spectrum]].

**Second near-miss — the relative determinant.** The alternative route compares $\Delta_X$ to a model operator along the ends, so that the divergent parts cancel in the difference. That produces a determinant *of a pair*, not of $\Delta_X$ alone, and it is a genuinely different object with a different normalisation. The paper chooses Melrose's route precisely to keep $\Delta_X$ itself.

---

# Used in this paper at

- [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]] — $\det_0(\Delta_X-s(1-s))$ is the object factorised
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] — $-\log\det_0(\Delta_X+\kappa)$ is expressed through the loop mass
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.2 — where the construction is set out
- [[Def - Zeta-Regularised Determinant of the Laplacian]] — the compact-case object this generalises, and reduces to

---

# Where this sits in my DAG

The functional analysis — trace-class operators, Lidskii's theorem, the Mellin transform, meromorphic continuation and finite parts — is *Functional Analysis* (🟢) and classical analysis. The Gauss–Bonnet check is [[Thm - Gauss-Bonnet Theorem for Surfaces]] and [[Def - Euler Characteristic]].

**Quoted, not derived:** that the heat-kernel diagonal has a controlled asymptotic expansion at the ends of the compactification, and the precise form of the short-time expansion of ${}^0\mathrm{Tr}$ in powers of $t$ and $t\log t$. These are Melrose's microlocal analysis, and the paper points to the literature for the explicit coordinates near cusps and funnels. Their home node in the DAG is *Microlocal Analysis / Semiclassical Analysis / Sheaf Quantization* (🔵).

Nothing in the paper computes with these expansions directly — the machinery is invoked so that $\det_0$ exists, after which [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]] takes over with an explicit closed form. So the practical dependency is on the *existence* of $\det_0$ and on that theorem, not on the microlocal details.
