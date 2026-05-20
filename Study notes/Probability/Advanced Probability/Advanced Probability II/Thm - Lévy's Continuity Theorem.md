---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Characteristic Function"
  - "Def - Weak Convergence"
  - "Thm - Prokhorov's Theorem"
tags: [probability, advanced-probability]
---

# Notation

$X_n,X$ random variables; $\varphi_n=\varphi_{X_n}$, $\varphi=\varphi_X$ their [[Def - Characteristic Function|characteristic functions]]; $\Rightarrow$ — [[Def - Weak Convergence|weak convergence]].

---

# Motivation

[[Def - Weak Convergence|Weak convergence]] of laws — $\int f\,d\mu_n\to\int f\,d\mu$ for *all* bounded continuous $f$ — is an unwieldy thing to verify directly. Lévy's continuity theorem replaces it by a far simpler condition: **pointwise convergence of the [[Def - Characteristic Function|characteristic functions]]**. Since the characteristic function turns the convolution of independent sums into a *product*, this is precisely what makes the [[Thm - Central Limit Theorem|central limit theorem]] provable — one need only show $\varphi_{S_n/\sqrt n}(t)\to e^{-t^2/2}$, a computation, instead of testing against every continuous function. Lévy's theorem is the bridge from the analytic object $\varphi$ back to the probabilistic conclusion.

---

# Sources and Targets

**Sources.** Hypothesis: $\varphi_n(t)\to\psi(t)$ pointwise for every $t$. The *strong form* needs only that the limit $\psi$ is **continuous at $0$** (then $\psi$ is automatically a characteristic function); the *weak form* assumes from the start that $\psi=\varphi_X$ for a known $X$.

**Targets.** $X_n\xrightarrow{d}X$. Combined with the [[Def - Characteristic Function|convolution-to-product]] property $\varphi_{X+Y}=\varphi_X\varphi_Y$, this is the engine of the [[Thm - Central Limit Theorem|CLT]] and of the Lévy–Khinchin classification of limit laws; it also proves that characteristic functions *determine* laws.

---

# Statement

Let $(X_n)$ be random variables with characteristic functions $\varphi_n$.

**(Easy direction.)** If $X_n\xrightarrow{d}X$, then $\varphi_n(t)\to\varphi_X(t)$ for every $t$ (indeed uniformly on compacts).

**(Lévy's continuity theorem.)** If $\varphi_n(t)\to\psi(t)$ for every $t$, and $\psi$ is **continuous at $0$**, then $\psi=\varphi_X$ is the characteristic function of some random variable $X$, and $X_n\xrightarrow{d}X$.

In particular, $X_n\xrightarrow{d}X$ **if and only if** $\varphi_n\to\varphi_X$ pointwise.

---

# Why Is It True

**Easy direction.** $x\mapsto e^{itx}$ is bounded and continuous, so $\varphi_n(t)=\mathbb{E}[e^{itX_n}]\to\mathbb{E}[e^{itX}]=\varphi(t)$ is just [[Def - Weak Convergence|weak convergence]] tested against this particular function.

**Hard direction** — two steps, *tightness* then *identification*.

*Tightness.* Why does pointwise convergence of $\varphi_n$, with $\psi$ continuous at $0$, prevent mass escaping to infinity? Because the characteristic function near $0$ *controls the tails*. The key estimate: for any law, $\mu(|x|\ge\lambda)\le C\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\varphi(t))\,dt$ — the tail probability is bounded by an average of $1-\operatorname{Re}\varphi$ over a small interval near $0$. (Intuitively, $1-\operatorname{Re}\varphi(t)=\mathbb{E}[1-\cos(tX)]$ is large near $0$ exactly when $X$ has heavy tails.) Now: $\psi$ continuous at $0$ with $\psi(0)=\lim\varphi_n(0)=1$ means $1-\operatorname{Re}\psi$ is small near $0$; $\varphi_n\to\psi$ plus dominated convergence makes $\int_0^{1/\lambda}(1-\operatorname{Re}\varphi_n)$ uniformly small. The estimate then gives a *uniform* tail bound — $(X_n)$ is **tight**.

*Identification.* By [[Thm - Prokhorov's Theorem|Prokhorov]], tightness gives a weakly convergent subsequence $X_{n_k}\Rightarrow X$. By the easy direction, $\varphi_{n_k}\to\varphi_X$; but also $\varphi_{n_k}\to\psi$, so $\psi=\varphi_X$ — in particular $\psi$ *is* a characteristic function. Every subsequential limit has characteristic function $\psi$, hence (characteristic functions [[Def - Characteristic Function|determine]] laws) the *same* law. A sequence all of whose subsequential limits agree converges: $X_n\xrightarrow{d}X$.

The slogan: **continuity of $\psi$ at $0$ forces tightness (the characteristic function near $0$ governs the tails); Prokhorov then extracts a limit, and uniqueness of the characteristic function pins it down.** The hypothesis "continuous at $0$" is exactly the no-escape condition — drop it ($\varphi_n(t)=e^{-nt^2/2}\to\mathbf{1}_{\{t=0\}}$, discontinuous at $0$) and the mass escapes ($X_n=\sqrt n\,Z\to\infty$, no weak limit).

---

# What Makes This Hard

The whole subtlety is the **tightness step** — and it is where the hypothesis "$\psi$ continuous at $0$" is spent. One must know (or derive) the inequality bounding a tail probability by $\int_0^{1/\lambda}(1-\operatorname{Re}\varphi)$ — the precise sense in which "$\varphi$ flat near $0$ $\Leftrightarrow$ light tails." Without continuity at $0$, $\psi$ need not be a characteristic function at all and the theorem fails. The second, milder subtlety: the conclusion is reached by the *subsequence-and-uniqueness* method (Prokhorov gives subsequential limits; uniqueness of the characteristic function makes them all equal), not by a direct construction.

---

# Rederivation Scaffold

**High-level strategy.** Easy direction: $e^{itx}\in C_b$. Hard direction: tail estimate $+$ continuity of $\psi$ at $0$ $\Rightarrow$ tightness $\Rightarrow$ ([[Thm - Prokhorov's Theorem|Prokhorov]]) subsequential weak limits, all with characteristic function $\psi$, hence all equal $\Rightarrow X_n\xrightarrow{d}X$.

**Subgoal decomposition.**

1. **Easy direction.** $\varphi_n(t)=\mathbb{E}[e^{itX_n}]\to\mathbb{E}[e^{itX}]$ since $e^{itx}\in C_b$.
2. **Tail estimate.** $\mu(|x|\ge\lambda)\le C\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\varphi(t))\,dt$.
3. **Tightness.** $\psi$ continuous at $0$, $\psi(0)=1$, $\varphi_n\to\psi$ $\Rightarrow\int_0^{1/\lambda}(1-\operatorname{Re}\varphi_n)$ uniformly small $\Rightarrow$ uniform tail bound.
4. **Identify.** Prokhorov $\Rightarrow$ subsequential limit $X$; $\varphi_X=\psi$; uniqueness $\Rightarrow$ all limits equal $\Rightarrow X_n\xrightarrow{d}X$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Tails are controlled by the characteristic function near 0
> **Statement:** For any law with characteristic function $\varphi$ and $\lambda>0$, $\ \mu(|x|\ge\lambda)\le C\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\varphi(t))\,dt$ with $C=(1-\sin1)^{-1}$.
>
> > [!note]- Full proof
> > From $\int_0^M(1-\cos u)\,du=M-\sin M\ge M(1-\sin1)$ for $M\ge1$, substituting $M=|x|/\lambda$ and changing variables, $\mathbf{1}_{\{|x|\ge\lambda\}}\le C\lambda\int_0^{1/\lambda}(1-\cos(tx))\,dt$. Integrate over $\mu$ and use $\operatorname{Re}\varphi(t)=\int\cos(tx)\,d\mu$ (Fubini). $\square$

> [!note]- Lemma 2: Tightness from continuity at 0
> **Statement:** If $\varphi_n\to\psi$ pointwise and $\psi$ is continuous at $0$ with $\psi(0)=1$, then $(\mu_n)$ is tight.
>
> > [!note]- Full proof
> > Given $\varepsilon$, continuity of $\psi$ at $0$ and $\psi(0)=1$ give $\lambda$ with $C\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\psi(t))\,dt<\varepsilon/2$. Since $|\varphi_n|\le1$ and $\varphi_n\to\psi$, dominated convergence gives $C\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\varphi_n)\,dt\to C\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\psi)\,dt<\varepsilon/2$, so $<\varepsilon$ for all large $n$ (the finitely many small $n$ are individually tight). By Lemma 1, $\sup_n\mu_n(|x|\ge\lambda)<\varepsilon$ — tightness. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Easy direction: $e^{itx}\in C_b\Rightarrow\varphi_n(t)\to\varphi_X(t)$. Hard direction: by Lemma 2, $(\mu_n)$ is tight; by [[Thm - Prokhorov's Theorem|Prokhorov]], every subsequence has a weakly convergent sub-subsequence $X_{n_k}\Rightarrow Y$, and by the easy direction $\varphi_Y=\lim\varphi_{n_k}=\psi$. Since [[Def - Characteristic Function|characteristic functions determine laws]], all subsequential limits share the law with characteristic function $\psi$; a sequence whose every subsequential limit is the same law converges weakly to it. So $X_n\xrightarrow{d}X$ with $\varphi_X=\psi$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Lévy's theorem reduces the [[Thm - Central Limit Theorem|central limit theorem]] to the *analytic* computation $\varphi_X(t/\sqrt n)^n\to e^{-t^2/2}$ — a Taylor expansion. It likewise drives the Poisson limit theorem (rare events), and the Lévy–Khinchin theorem classifying all possible limits of normalised sums (infinitely divisible laws) by the structure of their characteristic functions.

---

# Bridges

- **[[Def - Characteristic Function]]** — the tool; Lévy's theorem is what makes "convergence of characteristic functions" probabilistically meaningful.
- **[[Thm - Prokhorov's Theorem]]** — supplies the compactness; Lévy supplies the uniqueness; together they give convergence.
- **[[Thm - Central Limit Theorem]]** — the headline application.
