---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Transition Density and Heat Kernel"
tags: [paper, probability]
---

# Signature

| symbol | type |
|---|---|
| $\Omega_t$ | path space on $[0,t]$: $C([0,t],E)$ for a diffusion, $D([0,t],E)$ for a càdlàg process |
| $\mathrm{ev}_t$ | $\Omega_t\to E$, $\omega\mapsto\omega(t)$ — the endpoint map, Borel |
| $W^t_x$ | measure on $\Omega_t$; the path law started at $x$; $\lvert W^t_x\rvert=1$ (no killing) or $\leq1$ (with killing) |
| $W^t_{x\to y}$ | measure on $\Omega_t$; **unnormalised**; $\lvert W^t_{x\to y}\rvert=p(t,x,y)$, **not** $1$ |
| $p$ | the transition density of the process against $m$ |
| $(\mathrm{ev}_t)_*W^t_x$ | pushforward of $W^t_x$ under $\mathrm{ev}_t$; a measure on $E$ |

---

# Definition

> **Definition (unnormalised bridge measure).** The family $\{W^t_{x\to y}\}_{y\in E}$ is the **disintegration of $W^t_x$ with respect to the endpoint**, characterised by
> **(D1) Disintegration.** $\ \displaystyle W^t_x=\int_E W^t_{x\to y}\,m(\mathrm{d}y)$, i.e. $\ W^t_x(B)=\int_E W^t_{x\to y}(B)\,m(\mathrm{d}y)$ for every Borel $B\subseteq\Omega_t$.
> **(D2) Concentration.** $\ W^t_{x\to y}\big(\{\omega:\omega(t)\neq y\}\big)=0$ for $m$-a.e. $y$.
>
> The family is unique up to $m$-null sets of $y$.

> **(F1) Total mass.** $\ \lvert W^t_{x\to y}\rvert=p(t,x,y)$.
>
> **(F2) Conditional law.** On $\{p(t,x,y)>0\}$, the probability measure $W^t_{x\to y}/p(t,x,y)$ is the law of the process conditioned on $\omega(t)=y$.
>
> **(F3) Diagonal.** $\ \lvert W^t_{x\to x}\rvert=p(t,x,x)$ — the object integrated in every loop-measure definition in the paper.

**Gloss.** $W^t_{x\to y}$ is the conditional law *times* the density that the conditioning event has; it is a measure of mass $p(t,x,y)$, not a probability.

> [!warning] The normalisation is load-bearing
> Every loop-measure formula in the paper carries a factor of $p(t,x,x)$ that comes from (F1), not from any separate weighting. Reading $W^t_{x\to x}$ as a probability measure would silently divide every mass by $p(t,x,x)$ and destroy the short-time divergence that motivates §5.

**Existence.** (D1)–(D2) hold whenever $\mathrm{ev}_t$ is Borel between standard Borel spaces and $(\mathrm{ev}_t)_*W^t_x\ll m$ with density $p(t,x,\cdot)$ — which is exactly [[Def - Transition Density and Heat Kernel|(D3) of the transition-density page]]. So existence of the bridge family is a consequence of existence of $p$, not an extra assumption.

---

# Type card

> [!abstract] Type card — unnormalised bridge measure
> **Given.** **(H1)** $W^t_x$ a (sub-)probability measure on $\Omega_t$. **(H2)** $\mathrm{ev}_t$ Borel with $(\mathrm{ev}_t)_*W^t_x=p(t,x,\cdot)\,m$.
>
> **Produces.** A family $\{W^t_{x\to y}\}_{y\in E}$ of measures on $\Omega_t$ satisfying (D1),(D2); each of total mass $p(t,x,y)$; unique up to $m$-null $y$.
>
> **Lets you.** Write $\int_E W^t_{x\to y}\,m(\mathrm{d}y)$ instead of a conditional expectation, so that "integrate over all loops of duration $t$ rooted anywhere" is a single unnormalised integral $\int_E W^t_{x\to x}\,m(\mathrm{d}x)$ of total mass $\int_E p(t,x,x)\,m(\mathrm{d}x)$.

---

# Depends on

- [[Def - Transition Density and Heat Kernel]] — (D3) there gives existence here
- 🟢 disintegration of measures on standard Borel spaces; pushforward — *Advanced Probability*
- [[Thm - Radon-Nikodym Theorem]] — the density $p(t,x,\cdot)$ of $(\mathrm{ev}_t)_*W^t_x$

---

# Checks

**Instance.** $E=\mathbb{R}$, standard Brownian motion at speed $2$, $m=$ Lebesgue, $p(t,x,y)=(4\pi t)^{-1/2}e^{-(x-y)^2/4t}$. Then $W^t_{x\to y}$ has total mass $(4\pi t)^{-1/2}e^{-(x-y)^2/4t}$, and $W^t_{x\to y}/p(t,x,y)$ is the Brownian bridge, a probability measure. On the diagonal, $\lvert W^t_{x\to x}\rvert=(4\pi t)^{-1/2}\to\infty$ as $t\downarrow0$.

**Non-instance.** The normalised bridge $\widehat W^t_{x\to y}:=W^t_{x\to y}/p(t,x,y)$ satisfies (D2) but **fails (D1)**: $\int_E\widehat W^t_{x\to y}\,m(\mathrm{d}y)$ has total mass $\int_E m(\mathrm{d}y)$, which is $\infty$ on $\mathbb{H}^2$, not $1$. Consequence: substituting $\widehat W$ for $W$ in [[Constr - The Brownian Loop Measure|Definition 2.1]] changes the loop measure by a factor $p(t,x,x)^{-1}$ pointwise and produces a different, non-$\sigma$-finite object.

---

# Used at

- [[Constr - The Brownian Loop Measure]] — $\mu^*_X=\int_0^\infty\frac{\mathrm{d}t}{t}\int_XW^t_{x\to x}\,\mathrm{d}\operatorname{vol}_g(x)$, via (F3)
- [[Constr - The Dirichlet-Form Loop Measure]], [[Constr - The Subordinate Brownian Loop Measure]] — same, with $\Omega_t=D([0,t],X)$
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — Step 1 decomposes $W^{t,\mathcal{E}}_{z\to z,X}$ as a $\Gamma$-sum of pushed-forward upstairs bridges
- [[Def - Schwinger Proper-Time Representation]] — Feynman–Kac is stated against $W^t_{x\to y}$

---

# Commentary

> [!note]- Commentary (skippable)
> The paper introduces this in one sentence — "the bridge measure has total mass $\lvert W^t_{x\to y}\rvert=p(t,x,y)$ and $W^t_{x\to y}/p(t,x,y)$ is the usual conditional law given $\omega(t)=y$" — and the word doing the work is *unnormalised*. It is the single most consequential convention in §2, because the whole reason the Brownian loop measure diverges at $t\downarrow0$ is that $\lvert W^t_{x\to x}\rvert=p(t,x,x)\sim1/4\pi t$ blows up, and then $\int_X\mathrm{d}\operatorname{vol}_g$ and $\mathrm{d}t/t$ compound it to $\int_0 t^{-2}\,\mathrm{d}t$.
>
> The choice is not arbitrary. The unnormalised family is the one for which (D1) holds, i.e. the one that reassembles the path law; the normalised family does not, and there is no measure on $E$ against which it would. So "unnormalised" is not a weighting decision but the only disintegration that exists.
