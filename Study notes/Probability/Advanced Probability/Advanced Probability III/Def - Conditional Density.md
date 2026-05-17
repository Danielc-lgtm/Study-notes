---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Conditional Expectation"
  - "Def - Absolute Continuity and Density"
tags: [probability, advanced-probability]
---

# Notation

$(U,V)$ a pair of random variables with joint density $f_{U,V}(u,v)$ with respect to Lebesgue measure on $\mathbb{R}^2$; $f_U$ the marginal density of $U$; $f_{V\mid U}$ the conditional density.

---

# Axiom Motivation

[[Def - Conditional Expectation|Conditional expectation]] $\mathbb{E}[h(V)\mid U]$ is defined abstractly, by a characterising property — but in the concrete case where $(U,V)$ has a *joint density*, one wants a *formula*. The obstacle: conditioning on $\{U=u\}$ conditions on a probability-zero event, so the elementary recipe $\mathbb{E}[\cdot\mid U=u]=\mathbb{E}[\cdot\mathbf{1}_{U=u}]/\mathbb{P}(U=u)$ is "$0/0$".

The **conditional density** resolves this by taking the obvious formula and *justifying it as a limit*. Conditioning on $U\in[u,u+\mathrm{d}u]$ — a positive-probability event — the conditional law of $V$ has density proportional to $f_{U,V}(u,v)$; normalising,
$$f_{V\mid U}(v\mid u)=\frac{f_{U,V}(u,v)}{f_U(u)},\qquad f_U(u)=\int_\mathbb{R}f_{U,V}(u,v)\,\mathrm{d}v.$$
This is the "ratio of joint to marginal" — the density analogue of $\mathbb{P}(A\mid B)=\mathbb{P}(A\cap B)/\mathbb{P}(B)$, with $\mathrm{d}u$ cancelling. The point of *defining* it is that $g(u)=\int h(v)f_{V\mid U}(v\mid u)\,\mathrm{d}v$ then *provably satisfies the two characterising properties of $\mathbb{E}[h(V)\mid U]$* — it is $\sigma(U)$-measurable, and it integrates correctly over $\{U\in B\}$ (a [[Thm - Fubini-Tonelli Theorem|Fubini]] check). So the conditional density turns the abstract conditional expectation into a concrete integral, and "guess the formula, verify the two properties" becomes the standard computational method.

---

# The Definition

Let $(U,V)$ have joint density $f_{U,V}$ on $\mathbb{R}^2$, with marginal $f_U(u)=\int_\mathbb{R}f_{U,V}(u,v)\,\mathrm{d}v$. The **conditional density of $V$ given $U=u$** is, for $u$ with $f_U(u)>0$,
$$f_{V\mid U}(v\mid u)=\frac{f_{U,V}(u,v)}{f_U(u)}\qquad(v\in\mathbb{R}),$$
a genuine probability density in $v$ ($\ge0$, integrates to $1$). The **conditional expectation** is then computed by
$$\mathbb{E}[h(V)\mid U]=g(U),\qquad g(u)=\int_\mathbb{R}h(v)\,f_{V\mid U}(v\mid u)\,\mathrm{d}v,$$
and one writes $\mathbb{E}[h(V)\mid U=u]=g(u)$. This $g(U)$ satisfies the [[Def - Conditional Expectation|two defining properties]] of $\mathbb{E}[h(V)\mid U]$, so the formula is correct.

The **conditional probability** is $\mathbb{P}(V\in B\mid U=u)=\int_B f_{V\mid U}(v\mid u)\,\mathrm{d}v$.

---

# Relate to Other Fields / Compression

The conditional density is the *density* version of the elementary $\mathbb{P}(A\mid B)=\mathbb{P}(A\cap B)/\mathbb{P}(B)$ — joint over marginal — made rigorous by interpreting "$U=u$" as a limit of "$U\approx u$." In statistics it is the basis of **Bayesian inference**: $f_{V\mid U}$ with $V$ the parameter and $U$ the data is the *posterior density*, and the identity $f_{V\mid U}f_U=f_{U,V}=f_{U\mid V}f_V$ is **Bayes' theorem**. In information theory the conditional density carries the conditional entropy $H(V\mid U)$.

---

# Examples / Corollaries

**Independence.** If $U,V$ are independent, $f_{U,V}=f_Uf_V$, so $f_{V\mid U}(v\mid u)=f_V(v)$ — the conditional density is the marginal, and $\mathbb{E}[h(V)\mid U]=\mathbb{E}[h(V)]$.

**Bivariate Gaussian.** For $(U,V)$ jointly Gaussian, $f_{V\mid U}(\cdot\mid u)$ is again Gaussian, with mean *linear* in $u$ and variance *not depending on $u$*: $\mathbb{E}[V\mid U]=\mathbb{E}V+\frac{\mathrm{Cov}(U,V)}{\mathrm{Var}(U)}(U-\mathbb{E}U)$. The conditional expectation of a Gaussian is the *linear regression*.

Calibration: (i) Is $f_{V\mid U}(\cdot\mid u)$ a probability density? Yes, in $v$, for each fixed $u$ with $f_U(u)>0$. (ii) Does the conditional density need $\mathbb{P}(U=u)>0$? No — that is the whole point; it is defined where the *marginal density* is positive. (iii) For independent $U,V$, what is $\mathbb{E}[V\mid U]$? The constant $\mathbb{E}[V]$.

---

# Unlocked by This

> [!tip] Bayesian inference and the Gaussian conditional
> With $V$ a parameter and $U$ data, $f_{V\mid U}$ is the **posterior** — the engine of Bayesian statistics. The Gaussian case gives linear regression / the Kalman filter.
