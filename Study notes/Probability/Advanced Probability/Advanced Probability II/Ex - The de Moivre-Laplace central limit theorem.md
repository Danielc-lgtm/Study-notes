---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Central Limit Theorem"
  - "Def - Characteristic Function"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $S_n$ be the number of heads in $n$ independent fair coin tosses — a Binomial$(n,\tfrac12)$ random variable.

**(a)** Identify the mean and variance of $S_n$, and write down what the [[Thm - Central Limit Theorem|central limit theorem]] gives for $S_n$.

**(b)** State the **de Moivre–Laplace theorem**: $\mathbb{P}\!\left(a\le\frac{S_n-n/2}{\sqrt{n}/2}\le b\right)\to\Phi(b)-\Phi(a)$, and derive it from the CLT.

**(c)** Verify the characteristic-function computation directly: $\varphi_{(S_n-n/2)/(\sqrt n/2)}(t)\to e^{-t^2/2}$.

**Recall:**

[[Thm - Central Limit Theorem|CLT]]: for i.i.d. $X_k$ with mean $\mu$, variance $\sigma^2$, $\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$.

---

# Convergent Strategy

**Problem class:** instantiating the CLT on the foundational example — coin tossing — and seeing the characteristic-function machinery concretely.

**Assumption pattern:** $S_n=\sum_{k=1}^n X_k$ with $X_k$ i.i.d. Bernoulli$(\tfrac12)$ — the CLT's hypothesis exactly. Mean $\tfrac12$, variance $\tfrac14$ per toss.

---

# Legal Operations Used

1. **Recognise $S_n$ as an i.i.d. sum**, apply the CLT.
2. **Bernoulli characteristic function**, take the $n$-th power, Taylor-expand.

---

# Hints

> [!note]- Hint 1
> $X_k\in\{0,1\}$, $\mathbb{P}(X_k=1)=\tfrac12$: $\mathbb{E}X_k=\tfrac12$, $\mathrm{Var}(X_k)=\tfrac14$. So $\mathbb{E}S_n=n/2$, $\mathrm{Var}(S_n)=n/4$.

> [!note]- Hint 2
> The CLT normaliser is $\sigma\sqrt n=\tfrac12\sqrt n$. So $\frac{S_n-n/2}{\sqrt n/2}\xrightarrow{d}N(0,1)$.

> [!note]- Hint 3
> $\varphi_{X_k}(t)=\tfrac12+\tfrac12 e^{it}$. Centre, rescale by $\sqrt n/2$, take the $n$-th power, expand.

---

# Solution

**Step 1 — (a).** Write $S_n=\sum_{k=1}^n X_k$ with $X_k$ i.i.d. Bernoulli$(\tfrac12)$: $\mathbb{E}[X_k]=\tfrac12$, $\mathrm{Var}(X_k)=\tfrac12\cdot\tfrac12=\tfrac14$. So $\mathbb{E}[S_n]=n/2$ and $\mathrm{Var}(S_n)=n/4$, $\sigma=\tfrac12$. The [[Thm - Central Limit Theorem|CLT]] applies directly:
$$\frac{S_n-n/2}{\tfrac12\sqrt n}\ \xrightarrow{\ d\ }\ N(0,1).$$

**Step 2 — (b).** Convergence in distribution to $N(0,1)$ means $F_{Z_n}(x)\to\Phi(x)$ at every $x$ (the limit $\Phi$ is continuous), where $Z_n=\frac{S_n-n/2}{\sqrt n/2}$. Hence for any $a<b$,
$$\mathbb{P}\!\left(a\le\frac{S_n-n/2}{\sqrt n/2}\le b\right)=F_{Z_n}(b)-F_{Z_n}(a^-)\ \longrightarrow\ \Phi(b)-\Phi(a),$$
the **de Moivre–Laplace theorem** — historically the *first* central limit theorem (1733/1812), the Gaussian approximation to the binomial.

**Step 3 — (c) Direct characteristic-function check.** $\varphi_{X_k}(t)=\mathbb{E}[e^{itX_k}]=\tfrac12 e^{i\cdot0}+\tfrac12 e^{it}=\tfrac12(1+e^{it})$. Centre: $X_k-\tfrac12$ has characteristic function $e^{-it/2}\varphi_{X_k}(t)=\tfrac12(e^{-it/2}+e^{it/2})=\cos(t/2)$. The normalised sum $Z_n=\frac{1}{\sqrt n/2}\sum_k(X_k-\tfrac12)$ has, by independence,
$$\varphi_{Z_n}(t)=\Big[\cos\!\Big(\frac{t}{\sqrt n}\Big)\Big]^n.$$
Taylor: $\cos(s)=1-s^2/2+o(s^2)$, so $\cos(t/\sqrt n)=1-\frac{t^2}{2n}+o(1/n)$, and $\varphi_{Z_n}(t)=(1-\frac{t^2}{2n}+o(1/n))^n\to e^{-t^2/2}$. By [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]], $Z_n\xrightarrow{d}N(0,1)$ — the CLT, verified by hand on the coin-tossing case.

> [!note]- Complete formal solution
> (a) $X_k$ Bernoulli$(\tfrac12)$: $\mathbb{E}S_n=n/2$, $\mathrm{Var}(S_n)=n/4$; CLT gives $\frac{S_n-n/2}{\sqrt n/2}\xrightarrow{d}N(0,1)$. (b) Convergence in distribution to the continuous $\Phi$ gives $\mathbb{P}(a\le Z_n\le b)\to\Phi(b)-\Phi(a)$. (c) $\varphi_{X_k-1/2}(t)=\cos(t/2)$, so $\varphi_{Z_n}(t)=\cos(t/\sqrt n)^n=(1-\frac{t^2}{2n}+o(1/n))^n\to e^{-t^2/2}$. $\blacksquare$

---

# Key Takeaways

**The de Moivre–Laplace theorem — the Gaussian approximation to the binomial — is the [[Thm - Central Limit Theorem|CLT]] for the simplest possible summands, fair coin tosses, and historically the theorem from which the whole subject grew.** Recognising $S_n$ as an i.i.d. sum of Bernoulli variables is the entire modelling step; the CLT then delivers $\frac{S_n-n/2}{\sqrt n/2}\xrightarrow{d}N(0,1)$, and convergence in distribution to the *continuous* $\Phi$ converts to convergence of the interval probabilities. This is the prototype of every "count of successes is approximately Gaussian" statement in statistics.

**The hand computation $\varphi_{Z_n}(t)=\cos(t/\sqrt n)^n\to e^{-t^2/2}$ is the CLT proof in miniature, with no machinery hidden.** Independence turns the characteristic function into an $n$-th power; the second-order Taylor expansion of $\cos$ — which exists because Bernoulli variables trivially have all moments — produces $1-\frac{t^2}{2n}$; and $(1-\frac{t^2}{2n})^n\to e^{-t^2/2}$. Every step of the [[Thm - Central Limit Theorem|general CLT]] is visible here: factor by independence, expand to second order using finite variance, recognise the exponential limit, invoke [[Thm - Lévy's Continuity Theorem|Lévy]]. The coin-tossing case is the right place to first *see* why the Gaussian is universal.
