---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Eisenstein Series and the Continuous Spectrum"
  - "Def - Zeta-Regularised Determinant of the Laplacian"
tags: [paper, spectral-theory, microlocal-analysis]
---

# Signature

| symbol | type |
|---|---|
| $\bar X$ | the compactification of $X$: each end capped with a circle at infinity |
| $x$ | $\bar X\to[0,\infty)$ — a **boundary defining function**: smooth, vanishing to first order at the ends |
| $\mu$ | a smooth density on $\bar X$ |
| $f$ | a function with a controlled asymptotic expansion at the ends |
| ${}^0\!\int_X$ | the **renormalised integral**, $(f,\mu)\mapsto\mathbb{R}$ |
| ${}^0\mathrm{Tr}$ | the **0-trace**; ${}^0\mathrm{Tr}(e^{-t\Delta_X})\in\mathbb{R}$ for each $t>0$ |
| $\zeta^0_X$ | the renormalised spectral zeta; $\det_0\Delta_X:=e^{-(\zeta^0_X)'(0)}$ |
| $P$ | orthogonal projection onto $\ker_{L^2}\Delta_X$ |

---

# Definition

> **(D1) Renormalised integral (Riesz).** $\displaystyle\int_Xx^zf\mu$ converges for $\mathrm{Re}(z)$ large and continues meromorphically in $z$; set
> $$^0\!\!\int_Xf\mu:=\underset{z=0}{\mathrm{FP}}\int_Xx^zf\mu.\tag{59}$$
> The **Hadamard** version cuts the ends at $x\geq\epsilon$ and takes the finite part as $\epsilon\to0$; the two agree for the functions used here.
>
> **(D2) 0-trace.**
> $$^0\mathrm{Tr}\big(e^{-t\Delta_X}\big):=\ ^0\!\!\int_Xp_X(t,z,z)\,\mathrm{d}\mathrm{vol}_g(z),\qquad t>0.\tag{60}$$
> Legitimate because the diagonal $p_X(t,z,z)$ has a controlled expansion at the ends, even though its ordinary integral diverges.
>
> **(D3) Renormalised zeta and determinant.**
> $$\zeta^0_X(s):=\frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}\ ^0\mathrm{Tr}\big(e^{-t\Delta_X}-P\big)\,\mathrm{d}t,\qquad {\det}_0\Delta_X:=e^{-(\zeta^0_X)'(0)}.\tag{61},(62)$$
> Subtracting $P$ makes the $t\to\infty$ end converge.

> **(F1) Why $\zeta^0_X$ is regular at $0$.** As $t\to\infty$, ${}^0\mathrm{Tr}(e^{-t\Delta_X})\to\mathrm{rank}\,P$ exponentially. As $t\downarrow0$ it has an asymptotic expansion in powers of $t$ **and $t\log t$** — the logarithms coming from the cusps. This expansion gives $\zeta^0_X$ a meromorphic continuation regular at the origin.
>
> **(F2) Consistency.** On a closed surface the 0-trace **is** the ordinary trace and $\det_0$ reduces to ${\det}_\zeta$ of §5.1.
>
> **(F3) Renormalised area.** Applying (59) to the volume form gives $^0\mathrm{Area}(g):=\ ^0\!\int_X\mathrm{d}\mathrm{vol}_g=-2\pi\chi(X)$, the Gauss–Bonnet theorem for these metrics.

> [!warning] "Renormalised" here means *finite part of a meromorphic continuation*, not a limit
> $\int_Xp_X(t,z,z)\,\mathrm{d}\mathrm{vol}_g=\infty$ outright. (59) does not tame that integral; it defines a **different** number, the constant term of an analytic family. The choice of boundary defining function $x$ affects the answer in general — it is fixed once with the compactification, and the paper takes the standard cusp/funnel coordinates.

---

# Type card

> [!abstract] Type card — ${}^0\mathrm{Tr}$, $\det_0$
> **Given.** **(H1)** $X$ geometrically finite hyperbolic; $\bar X$ its compactification with a fixed boundary defining function $x$. **(H2)** the heat-kernel diagonal has a controlled expansion at the ends — [[Ext - Melrose Renormalised Trace Expansion|(M)]].
>
> **Produces.** For each $t>0$ a number ${}^0\mathrm{Tr}(e^{-t\Delta_X})$; hence a function $\zeta^0_X$ regular at $0$; hence a number $\det_0\Delta_X\in(0,\infty)$.
>
> **Lets you.** Define a determinant when $e^{-t\Delta_X}$ is not trace class, agreeing with ${\det}_\zeta$ when it is. This is the object [[Ext - Borthwick–Judge–Perry Determinant Formula|(BJP)]] relates to $Z_X$, and hence to loop masses.

---

# Depends on

- [[Def - Eisenstein Series and the Continuous Spectrum]] — why $\mathrm{Tr}$ fails
- [[Ext - Melrose Renormalised Trace Expansion]] — (H2), (F1)
- [[Def - Zeta-Regularised Determinant of the Laplacian]] — the template being generalised, and (F2)
- 🟢 meromorphic continuation, finite parts, Mellin transform — *Complex Analysis*, *Functional Analysis* (8,10)
- 🟢 Lidskii's theorem (trace $=$ integral of the diagonal, for trace-class operators with continuous kernel) — the fact being *replaced*

---

# Checks

**Instance.** $X$ closed: $x\equiv1$, no ends, the finite part is the integral itself, and (60) is Lidskii's theorem. $\det_0=\det_\zeta$ — this is (F2).

**Instance.** $X$ finite area with $n_C$ cusps: $^0\mathrm{Area}(g)=-2\pi\chi(X)=\mathrm{Area}(X)$, since the hyperbolic area is already finite. The renormalisation does nothing to the area but is essential for the heat diagonal.

**Non-instance (fails without a controlled expansion).** A function $f$ on $X$ whose behaviour at the ends is not of the form $\sum_kc_kx^{a_k}(\log x)^{b_k}$: then $\int_Xx^zf\mu$ need not continue meromorphically, and (59) is undefined. **Consequence:** (M) is not decoration — it is the hypothesis that makes the definition well posed.

**Non-instance (fails the $t\to\infty$ convergence).** Omitting $-P$ in (61): ${}^0\mathrm{Tr}(e^{-t\Delta_X})\to\mathrm{rank}\,P=1$, so the $t$-integral diverges at infinity for every $s$. The subtraction is exactly the finite-area analogue of dropping $\lambda_0=0$ in §5.1.

---

# Used at

- [[Ext - Borthwick–Judge–Perry Determinant Formula]] — $\det_0$ is its subject; (63) is an identity for ${}^0\mathrm{Tr}(R_X(s)^2)$
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)]] — the object computed
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.2

---

# Commentary

> [!note]- Commentary (skippable)
> The construction is Melrose's, and the idea is geometric before it is analytic: a hyperbolic surface with cusps or funnels has a natural compactification $\bar X$ obtained by gluing a circle at infinity onto each end, and on $\bar X$ the heat kernel is not merely bounded but has a **known** asymptotic form near the boundary. Once the divergence is known explicitly, one can subtract it in a canonical way, and the finite part of $\int x^zf\mu$ at $z=0$ is that subtraction packaged as an analytic continuation.
>
> The $t\log t$ terms in (F1) are the fingerprint of the cusps and are the one genuinely new feature relative to §5.1. On a closed surface the short-time expansion has only powers of $t$; the logarithms here are why $\zeta^0_X$ needs its own argument for regularity at $0$ rather than inheriting §5.1's.
>
> What the reader should carry forward is narrow: $\det_0$ exists, it agrees with $\det_\zeta$ when both are defined, and (BJP) computes it in terms of $Z_X$. Nothing in §5.2's use of loop measures reopens the construction.
