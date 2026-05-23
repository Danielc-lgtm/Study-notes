---
type: theorem
subject: advanced-probability
prereqs:
  - "Thm - Lévy's Continuity Theorem"
  - "Def - Characteristic Function"
  - "Def - Weak Convergence"
tags: [probability, advanced-probability]
---

# Notation

$(X_n)$ i.i.d. with $\mathbb{E}[X_1]=\mu$, $\mathrm{Var}(X_1)=\sigma^2\in(0,\infty)$; $S_n=X_1+\cdots+X_n$; $N(0,1)$ the standard Gaussian, characteristic function $e^{-t^2/2}$.

---

# Motivation

The [[Thm - Strong Law of Large Numbers|law of large numbers]] says $S_n/n\to\mu$ — the average has *no fluctuation* in the limit. The central limit theorem describes the fluctuation that the law of large numbers discards: $S_n-n\mu$ is of order $\sqrt n$, and once rescaled by $\sqrt n$ it converges to a **Gaussian** — *regardless of the distribution of $X_1$*. This universality is the most important fact in probability and statistics: it is why the bell curve is everywhere, why measurement errors are Gaussian, why confidence intervals have their form. The CLT says the Gaussian is the universal *attractor* for normalised sums of independent pieces, each individually negligible.

---

# Sources and Targets

**Sources.** Hypotheses: $(X_n)$ **i.i.d.** with **finite, non-zero variance**. Finite variance is essential — heavy-tailed $X_1$ (infinite variance) converge instead to *stable* laws. Independence can be weakened (martingale, mixing CLTs); the i.i.d. case is the prototype.

**Targets.** $\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$ gives: **confidence intervals** and hypothesis tests in statistics; the $\sqrt n$ scaling of Monte Carlo error; the **Gaussian approximation** $\mathbb{P}(S_n\le a)\approx\Phi(\frac{a-n\mu}{\sigma\sqrt n})$; and, in the functional form (Donsker), the construction of Brownian motion as a scaling limit.

---

# Statement

Let $(X_n)_{n\ge1}$ be **independent and identically distributed** with $\mathbb{E}[X_1]=\mu$ and $0<\sigma^2=\mathrm{Var}(X_1)<\infty$. Then
$$\frac{S_n-n\mu}{\sigma\sqrt n}\ \xrightarrow{\ d\ }\ N(0,1)\qquad\text{as }n\to\infty,$$
i.e. for every $a\in\mathbb{R}$, $\ \mathbb{P}\big(\tfrac{S_n-n\mu}{\sigma\sqrt n}\le a\big)\to\Phi(a)=\int_{-\infty}^a\frac{e^{-x^2/2}}{\sqrt{2\pi}}\,dx$.

---

# Why Is It True

The proof is a *characteristic-function computation*, made legitimate by [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]]: it suffices to show the characteristic function of the normalised sum converges, pointwise, to $e^{-t^2/2}$ — the Gaussian's.

Centre and rescale: assume $\mu=0$, $\sigma^2=1$ (replace $X_k$ by $(X_k-\mu)/\sigma$), and set $Z_n=S_n/\sqrt n$. The two structural facts:

*Independence linearises the sum.* Because the $X_k$ are independent, the [[Def - Characteristic Function|characteristic function of a sum is a product]]:
$$\varphi_{Z_n}(t)=\mathbb{E}\big[e^{it S_n/\sqrt n}\big]=\prod_{k=1}^n\mathbb{E}\big[e^{i(t/\sqrt n)X_k}\big]=\varphi_X\!\left(\frac{t}{\sqrt n}\right)^{\!n}.$$
The whole problem is now to understand one characteristic function, $\varphi_X$, near $0$, raised to a high power.

*Finite variance gives a Taylor expansion.* Since $\mathbb{E}X=0$, $\mathbb{E}X^2=1$, the [[Def - Characteristic Function|moment property]] ($\varphi_X^{(k)}(0)=i^k\mathbb{E}X^k$) gives the second-order expansion
$$\varphi_X(s)=1+is\,\mathbb{E}X-\tfrac{s^2}{2}\mathbb{E}X^2+o(s^2)=1-\tfrac{s^2}{2}+o(s^2)\quad(s\to0).$$
Substitute $s=t/\sqrt n$ — which $\to0$ as $n\to\infty$:
$$\varphi_{Z_n}(t)=\left(1-\frac{t^2}{2n}+o\!\left(\frac1n\right)\right)^{\!n}\ \xrightarrow[n\to\infty]{}\ e^{-t^2/2},$$
by the standard limit $(1+c/n+o(1/n))^n\to e^c$. The limit $e^{-t^2/2}$ is the characteristic function of $N(0,1)$, and it is continuous at $0$ — so [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]] converts pointwise convergence of characteristic functions into [[Def - Weak Convergence|weak convergence]] of laws: $Z_n\xrightarrow{d}N(0,1)$.

The slogan: **independence turns $\varphi_{S_n/\sqrt n}$ into $\varphi_X(t/\sqrt n)^n$; finite variance gives $\varphi_X(s)\approx1-s^2/2$; and $(1-\frac{t^2}{2n})^n\to e^{-t^2/2}$ — the Gaussian appears because it is the function whose log is exactly quadratic.** Universality is built in: only $\mathbb{E}X=0$ and $\mathbb{E}X^2=1$ enter — the mean and variance — so *every* distribution with those two normalised moments has the same limit. The third and higher moments wash out under the $1/\sqrt n$ scaling.

---

# What Makes This Hard

The proof, *given* [[Thm - Lévy's Continuity Theorem|Lévy's theorem]] and the [[Def - Characteristic Function|moment expansion]], is short — but each ingredient is substantial. The genuine subtleties: (i) one must know that finite *second* moment licenses the *second-order* Taylor expansion of $\varphi_X$ with an $o(s^2)$ remainder — this is exactly the regularity the hypothesis $\sigma^2<\infty$ buys, and no more; (ii) the rescaling $s=t/\sqrt n$ is what makes the linear term vanish (mean $0$) and the quadratic term survive at the right rate — *why $\sqrt n$* is the content; (iii) the heavy lifting is hidden in Lévy's theorem (tightness, Prokhorov). The common error is to forget that finite variance is *essential* — infinite variance gives a different ($\sqrt n$ becomes $n^{1/\alpha}$) scaling and a stable, non-Gaussian limit.

---

# Rederivation Scaffold

**High-level strategy.** Reduce to $\mu=0,\sigma^2=1$. Factor $\varphi_{S_n/\sqrt n}=\varphi_X(t/\sqrt n)^n$ by independence. Taylor-expand $\varphi_X(s)=1-s^2/2+o(s^2)$ using finite variance. Take the $n$-th power, get $e^{-t^2/2}$. Apply Lévy's continuity theorem.

**Subgoal decomposition.**

1. **Normalise.** Replace $X_k$ by $(X_k-\mu)/\sigma$; reduce to $Z_n=S_n/\sqrt n$, $\mathbb{E}X=0$, $\mathbb{E}X^2=1$.
2. **Factor.** Independence $\Rightarrow\varphi_{Z_n}(t)=\varphi_X(t/\sqrt n)^n$.
3. **Expand.** Finite variance $\Rightarrow\varphi_X(s)=1-s^2/2+o(s^2)$ ([[Def - Characteristic Function|moment property]]).
4. **Limit.** $(1-\frac{t^2}{2n}+o(1/n))^n\to e^{-t^2/2}$.
5. **Convert.** $e^{-t^2/2}$ is continuous at $0$ and is $\varphi_{N(0,1)}$; [[Thm - Lévy's Continuity Theorem|Lévy]] $\Rightarrow Z_n\xrightarrow{d}N(0,1)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The characteristic function factors and expands
> **Statement:** For i.i.d. $X_k$ with $\mathbb{E}X=0$, $\mathbb{E}X^2=1$: $\varphi_{S_n/\sqrt n}(t)=\varphi_X(t/\sqrt n)^n$ and $\varphi_X(s)=1-s^2/2+o(s^2)$.
>
> **Hint:** Two independent observations: independence turns the characteristic function of a sum into a product, and finite second moment lets you Taylor-expand $\varphi_X$ around $0$ with the derivatives read off from the moments.
>
> **Why needed:** The product form is what allows the Fourier transform to "see" the central limit phenomenon — [[Def - Convolution|convolutions]] of densities (sums of independent variables) become powers of characteristic functions, and second-order Taylor data is exactly what survives the $1/\sqrt n$ rescaling.
>
> > [!note]- Full proof
> > Independence and the [[Ex - Independence and the factorisation of expectation|convolution-to-product]] property give $\varphi_{S_n/\sqrt n}(t)=\mathbb{E}[\prod_k e^{i(t/\sqrt n)X_k}]=\prod_k\varphi_X(t/\sqrt n)=\varphi_X(t/\sqrt n)^n$. Since $\mathbb{E}X^2<\infty$, $\varphi_X\in C^2$ with $\varphi_X(0)=1$, $\varphi_X'(0)=i\mathbb{E}X=0$, $\varphi_X''(0)=-\mathbb{E}X^2=-1$; Taylor's theorem gives $\varphi_X(s)=1-s^2/2+o(s^2)$. $\square$

> [!note]- Lemma 2: The $n$-th power converges to the Gaussian
> **Statement:** $\varphi_X(t/\sqrt n)^n\to e^{-t^2/2}$ for every $t$.
>
> **Hint:** Take logarithms (legal for large $n$ since the argument is near $1$) and use $\log(1+u)=u+o(u)$: the leading term $-t^2/(2n)$ multiplied by $n$ converges to $-t^2/2$ while the remainder $o(1/n)\cdot n\to 0$.
>
> **Why needed:** This is the explicit Gaussian limit at the characteristic-function level. Combined with Lévy's continuity theorem, pointwise convergence of characteristic functions to $e^{-t^2/2}$ (continuous at $0$) upgrades to weak convergence of distributions to $N(0,1)$ — which is the CLT.
>
> > [!note]- Full proof
> > By Lemma 1, $\varphi_X(t/\sqrt n)=1-\frac{t^2}{2n}+o(1/n)$. Taking logarithms (defined for large $n$, since the argument $\to1$), $n\log\varphi_X(t/\sqrt n)=n(-\frac{t^2}{2n}+o(1/n))=-\frac{t^2}{2}+o(1)\to-\frac{t^2}{2}$. Exponentiate: $\varphi_X(t/\sqrt n)^n\to e^{-t^2/2}$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Reduce to $\mu=0$, $\sigma^2=1$. By Lemmas 1–2, $\varphi_{S_n/\sqrt n}(t)\to e^{-t^2/2}$ for every $t$. The limit $e^{-t^2/2}$ is continuous (everywhere, in particular at $0$) and equals $\varphi_{N(0,1)}$. By [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]], $S_n/\sqrt n\xrightarrow{d}N(0,1)$; undoing the normalisation, $\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The CLT underlies **all of inferential statistics** — confidence intervals, $z$- and $t$-tests, the $\sqrt n$ rate of estimator error. Its functional version, **Donsker's invariance principle**, says the rescaled random walk converges weakly (in path space) to Brownian motion — the CLT "for the whole trajectory," and a construction of Brownian motion. The Lindeberg–Feller and [[Def - Martingale|martingale]] CLTs extend it beyond i.i.d.; Stein's method gives quantitative (Berry–Esseen) rates.

---

# Bridges

- **[[Thm - Lévy's Continuity Theorem]]** — the bridge converting "$\varphi_n\to e^{-t^2/2}$" into "$\xrightarrow{d}N(0,1)$"; without it the CLT computation is inconclusive.
- **[[Thm - Strong Law of Large Numbers]]** — the CLT refines the SLLN: it describes the $\sqrt n$-scale fluctuations the law of large numbers shows merely vanish.
- **[[Def - Characteristic Function]]** — the self-duality of the Gaussian ($\varphi=e^{-t^2/2}$, log exactly quadratic) is *why* the Gaussian is the universal limit.
