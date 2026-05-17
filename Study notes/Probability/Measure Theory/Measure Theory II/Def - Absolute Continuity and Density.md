---
type: definition
subject: measure-theory
prereqs:
  - "Def - The Integral"
  - "Def - Measure and Measure Space"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A})$ measurable; $\mu,\nu$ measures on it; $f\ge0$ measurable. $\nu\ll\mu$ — $\nu$ absolutely continuous w.r.t. $\mu$.

---

# Axiom Motivation

Once we can integrate, every non-negative measurable function $f$ generates a *new* measure: $\nu(A)=\int_A f\,d\mu$. The function $f$ is a **density** — it re-weights $\mu$, making some regions count more, others less. (That $\nu$ is genuinely a measure — $\sigma$-additive — is the [[Thm - Monotone Convergence Theorem|monotone convergence theorem]].) This is how the Gaussian, the exponential, and every continuous law arise: a density against Lebesgue measure.

Which measures $\nu$ arise this way? A necessary condition is visible immediately: if $\mu(A)=0$ then $f\mathbf{1}_A=0$ a.e., so $\nu(A)=0$. A density-measure **cannot put mass where $\mu$ has none**. This necessary condition is named **absolute continuity**, $\nu\ll\mu$. The deep theorem — [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] — is that for $\sigma$-finite measures it is also *sufficient*: $\nu\ll\mu$ forces $\nu=f\mu$ for some density $f=\mathrm{d}\nu/\mathrm{d}\mu$.

The "$\varepsilon$–$\delta$" reformulation explains the name. For a *finite* $\nu\ll\mu$: small $\mu$-measure forces small $\nu$-measure, $\mu(A)<\delta\Rightarrow\nu(A)<\varepsilon$. This is genuine continuity of $\nu$ with respect to $\mu$, and applied to $\nu(A)=\int_A|g|\,d\mu$ it says **the integral of an $L^1$ function over a small set is small** — a uniform-smallness property. Strengthening it to a *family* of functions gives **uniform absolute continuity of integrals**, the precise extra hypothesis (beyond [[Def - Convergence in Measure|convergence in measure]]) that the [[Thm - Vitali Convergence Theorem|Vitali theorem]] needs for $L^1$-convergence.

---

# The Definition

Let $\mu,\nu$ be measures on $(X,\mathcal{A})$.

**Density.** For measurable $f:X\to[0,\infty]$, the set function $\nu(A)=\int_A f\,d\mu$ is a measure on $(X,\mathcal{A})$; one says $\nu$ **has density $f$** with respect to $\mu$ and writes $\nu=f\mu$.

**Absolute continuity.** $\nu$ is **absolutely continuous** with respect to $\mu$, written $\nu\ll\mu$, if
$$\mu(A)=0\ \Longrightarrow\ \nu(A)=0\qquad\text{for all }A\in\mathcal{A}.$$

**$\varepsilon$–$\delta$ form.** If $\nu$ is finite and $\nu\ll\mu$, then: for every $\varepsilon>0$ there is $\delta>0$ with $\mu(A)<\delta\Rightarrow\nu(A)<\varepsilon$. In particular, for a single $g\in L^1(\mu)$,
$$\forall\varepsilon>0\ \exists\delta>0\ \forall A:\ \mu(A)<\delta\implies\int_A|g|\,d\mu<\varepsilon.$$

**Uniform absolute continuity.** A family $\mathcal{F}\subseteq L^1(\mu)$ has **uniformly absolutely continuous integrals** if
$$\forall\varepsilon>0\ \exists\delta>0\ \forall f\in\mathcal{F}\ \forall A:\ \mu(A)<\delta\implies\int_A|f|\,d\mu<\varepsilon.$$
Every *finite* family has this property; the content is whether an *infinite* family does.

---

# Relate to Other Fields / Compression

A density is the measure-theoretic version of a *change of weights* or a *mass distribution*; $\mathrm{d}\nu/\mathrm{d}\mu$ generalises the Jacobian and the probability density function in one stroke. In probability, $\nu\ll\mathbb{P}$ with density $f$ is exactly a random variable having **probability density function** $f$; the Radon–Nikodym derivative of one law w.r.t. another is the **likelihood ratio** of statistics and the change-of-measure factor (Girsanov) of stochastic analysis. "Uniformly absolutely continuous integrals" is one of the two equivalent faces of [[Def - Uniform Integrability|uniform integrability]] — the compactness notion that controls $L^1$-convergence.

---

# Examples / Corollaries

The **standard Gaussian** $\nu=f\lambda$ with $f(x)=(2\pi)^{-1/2}e^{-x^2/2}$ is a probability measure, $\nu\ll\lambda$. The **exponential** $f(x)=\lambda e^{-\lambda x}\mathbf{1}_{x\ge0}$ likewise. The **Dirac measure** $\delta_0$ is *not* $\ll\lambda$: $\lambda(\{0\})=0$ but $\delta_0(\{0\})=1$ — point masses are the obstruction to having a density (they are the *singular* part).

A single $g\in L^1(\mu)$ always has absolutely continuous integral ($\varepsilon$–$\delta$ form); hence so does any finite family. An infinite family may fail it — and that failure is exactly non-uniform-integrability.

Calibration: (i) Is $\lambda\ll\#$ (counting measure)? Yes vacuously where $\#$ has no null sets — but $\lambda$ has no density w.r.t. $\#$ because $\#$ is not $\sigma$-finite. (ii) Is $\delta_0\ll\lambda$? No. (iii) Does $\nu\ll\mu$ give an $\varepsilon$–$\delta$ statement for *infinite* $\nu$? Not necessarily — the $\varepsilon$–$\delta$ form needs $\nu$ finite.

---

# Unlocked by This

> [!tip] Radon–Nikodym theorem and conditional expectation
> [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] proves the converse: $\nu\ll\mu$ ($\sigma$-finite) $\Rightarrow\nu=f\mu$. Applied to a measure restricted to a sub-$\sigma$-algebra, the resulting density *is* the [[Def - Conditional Expectation|conditional expectation]].

> [!tip] Uniform integrability *(from [[Advanced Probability II — Convergence and Limit Theorems|Advanced Probability]])*
> Uniformly absolutely continuous integrals (plus an $L^1$-bound) is [[Def - Uniform Integrability|uniform integrability]] — the hypothesis upgrading convergence in probability to $L^1$ and a.s.-martingale convergence to $L^1$.
