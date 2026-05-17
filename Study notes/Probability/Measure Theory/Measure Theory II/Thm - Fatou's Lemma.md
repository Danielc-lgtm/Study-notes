---
type: theorem
subject: measure-theory
prereqs:
  - "Def - The Integral"
  - "Thm - Monotone Convergence Theorem"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $f_n:X\to[0,\infty]$ measurable. $\liminf_n f_n$ is the pointwise lower limit.

---

# Motivation

The [[Thm - Monotone Convergence Theorem|MCT]] handles *monotone* sequences. For a general sequence of non-negative functions, no equality $\lim\int f_n=\int\lim f_n$ can hold — mass can [[Ex - Continuity from above requires finite measure|escape to infinity]]. Fatou's lemma is what survives: a one-sided inequality, $\int\liminf f_n\le\liminf\int f_n$, valid with *no* hypothesis beyond non-negativity. It is the universal safety net — always available — and the springboard for the [[Thm - Dominated Convergence Theorem|dominated convergence theorem]]. The inequality direction encodes a real phenomenon: integration can only *lose* mass in the limit, never gain it; mass can leak away (escape to infinity, concentrate into a spike) but cannot appear from nowhere.

---

# Sources and Targets

**Sources.** The only hypothesis is "$f_n\ge0$ measurable" — Fatou is the most hypothesis-light convergence theorem, hence applicable whenever non-negativity holds, even when no limit exists. A standard *bridge*: given a sequence with $f_n\to f$ and a dominating $g$, apply Fatou to the non-negative $g\pm f_n$ or $g-|f_n-f|$ — this is the trick that derives DCT.

**Targets.** "$\int\liminf\le\liminf\int$" yields: (i) [[Thm - Dominated Convergence Theorem|DCT]], by applying Fatou twice (to $g+f_n$ and $g-f_n$); (ii) **lower semicontinuity of the integral** — if $f_n\to f$ a.e. then $\int f\le\liminf\int f_n$, so the integral cannot jump up under limits; (iii) in probability, that $\mathbb{E}[\liminf X_n]\le\liminf\mathbb{E}[X_n]$, used to bound limits of expectations from one side for free.

---

# Formal Statement

Let $f_n:X\to[0,\infty]$ be measurable, $n\in\mathbb{N}$. Then
$$\int_X\Big(\liminf_{n\to\infty}f_n\Big)\,d\mu\ \le\ \liminf_{n\to\infty}\int_X f_n\,d\mu.$$
The inequality may be strict, and *no* hypothesis beyond $f_n\ge0$ is needed.

---

# Why Is It True

Fatou is MCT applied to the right monotone sequence. The definition of $\liminf$ *is* a monotone limit: $\liminf_n f_n=\lim_n g_n$ where $g_n=\inf_{k\ge n}f_k$, and the $g_n$ **increase** ($g_n\le g_{n+1}$, since infimising over a smaller tail can only raise the value). So $g_n\uparrow\liminf f_n$, and [[Thm - Monotone Convergence Theorem|MCT]] gives $\int g_n\uparrow\int\liminf f_n$.

Now the one inequality that does the work: $g_n=\inf_{k\ge n}f_k\le f_k$ for every $k\ge n$, so by [[Thm - Properties of the Integral|monotonicity]] $\int g_n\le\int f_k$ for every $k\ge n$, hence $\int g_n\le\inf_{k\ge n}\int f_k$. Take $n\to\infty$: the left side rises to $\int\liminf f_n$ (MCT), the right side rises to $\liminf_n\int f_n$ (by definition of $\liminf$ of the number sequence $\int f_n$). The inequality is preserved in the limit.

The slogan: **$\liminf$ of functions is secretly a monotone limit ($g_n\uparrow$); feed it to MCT; the bound $g_n\le f_k$ leaks through to the integrals.** The inequality is one-sided because $g_n$ is a *lower envelope* — it underestimates each $f_k$, and that underestimate is exactly the "$\le$."

Why can it be strict? Because mass escapes. The moving bump $f_n=\mathbf{1}_{[n,n+1]}$ has $\liminf f_n=0$ so $\int\liminf f_n=0$, while $\int f_n=1$ for all $n$ so $\liminf\int f_n=1$: $0<1$. The mass is always present but slides off to infinity, invisible to the pointwise $\liminf$.

---

# What Makes This Hard

There is one idea and missing it leaves you stuck: **$\liminf_n f_n$ is itself the increasing limit of $g_n=\inf_{k\ge n}f_k$**. Once seen, Fatou is "apply MCT to $g_n$, and note $\int g_n\le\int f_k$." The common errors: trying to apply MCT directly to the non-monotone $f_n$; or believing the inequality should be an equality (it is genuinely one-sided — the escaping-bump example is the reason).

---

# Rederivation Scaffold

**High-level strategy.** Set $g_n=\inf_{k\ge n}f_k$; observe $g_n\uparrow\liminf f_n$; apply MCT; use $g_n\le f_k$ ($k\ge n$) to get $\int g_n\le\inf_{k\ge n}\int f_k$; pass to the limit.

**Subgoal decomposition.**

1. **$g_n=\inf_{k\ge n}f_k$ is measurable and increasing**, with $g_n\uparrow\liminf f_n$.
2. **$\int g_n\le\int f_k$ for all $k\ge n$**, by monotonicity, so $\int g_n\le\inf_{k\ge n}\int f_k$.
3. **Let $n\to\infty$:** MCT gives $\int g_n\uparrow\int\liminf f_n$; $\inf_{k\ge n}\int f_k\uparrow\liminf_n\int f_n$; the inequality survives.

---

# Lemma Decomposition

> [!note]- Lemma 1: The infimum envelopes increase to the liminf
> **Statement:** $g_n=\inf_{k\ge n}f_k$ is measurable, $g_n\le g_{n+1}$, and $g_n\uparrow\liminf_n f_n$.
>
> > [!note]- Full proof
> > Measurability: countable infimum of measurable functions ([[Thm - Operations Preserve Measurability]]). Monotone: $\{f_k:k\ge n+1\}\subseteq\{f_k:k\ge n\}$, and an infimum over a smaller set is $\ge$, so $g_{n+1}\ge g_n$. Limit: $\liminf_n f_n=\sup_n\inf_{k\ge n}f_k=\sup_n g_n=\lim_n g_n$ since $g_n$ increases. $\square$

> [!note]- Lemma 2: Integral comparison
> **Statement:** $\int g_n\,d\mu\le\inf_{k\ge n}\int f_k\,d\mu$.
>
> > [!note]- Full proof
> > For each $k\ge n$, $g_n=\inf_{j\ge n}f_j\le f_k$ pointwise, so by [[Thm - Properties of the Integral|monotonicity of the integral]] $\int g_n\le\int f_k$. As this holds for every $k\ge n$, $\int g_n\le\inf_{k\ge n}\int f_k$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $g_n\uparrow\liminf_n f_n$ with $g_n\ge0$ measurable, so [[Thm - Monotone Convergence Theorem|MCT]] gives $\int g_n\,d\mu\uparrow\int\liminf_n f_n\,d\mu$. By Lemma 2, $\int g_n\le\inf_{k\ge n}\int f_k$. Letting $n\to\infty$, the left side tends to $\int\liminf f_n$ and the right side tends to $\sup_n\inf_{k\ge n}\int f_k=\liminf_n\int f_n$. Hence $\int\liminf_n f_n\le\liminf_n\int f_n$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Fatou applied to $g\pm f_n$ (when $|f_n|\le g\in L^1$) *is* the proof of [[Thm - Dominated Convergence Theorem|DCT]]. Applied in probability: $\mathbb{E}[\liminf X_n]\le\liminf\mathbb{E}[X_n]$ for $X_n\ge0$ — this gives, for instance, that the limit of an $L^1$-bounded sequence of non-negative random variables is itself integrable, the step that makes the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]]'s limit a genuine $L^1$ random variable.

---

# Bridges

- **[[Thm - Monotone Convergence Theorem]]** — Fatou is MCT applied to $g_n=\inf_{k\ge n}f_k$; one theorem feeds the other.
- **[[Thm - Dominated Convergence Theorem]]** — DCT is "Fatou applied twice," to $g+f_n$ and $g-f_n$.
- **[[Ex - Continuity from above requires finite measure]]** — the escaping-bump that makes Fatou strict is the same escape-to-infinity mechanism.
