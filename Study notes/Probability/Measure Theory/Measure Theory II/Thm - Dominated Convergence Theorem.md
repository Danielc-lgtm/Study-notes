---
type: theorem
subject: measure-theory
prereqs:
  - "Def - The Integral"
  - "Thm - Fatou's Lemma"
  - "Thm - Properties of the Integral"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $f,f_n:X\to[-\infty,\infty]$ measurable; $g\in L^1(\mu)$ a non-negative **dominating function**.

---

# Motivation

The central practical question of integration: *when may one interchange a limit and an integral*, $\lim\int f_n=\int\lim f_n$? [[Thm - Monotone Convergence Theorem|MCT]] answers it for monotone non-negative sequences; the dominated convergence theorem (DCT) answers it for *general* sequences, signed and non-monotone, under one clean hypothesis — a single integrable function $g$ dominating every $|f_n|$. DCT is the workhorse: it is what one reaches for to differentiate under the integral sign, to compute limits of integrals, to prove continuity of integral transforms. The dominating function is the device that *forbids mass from escaping*; with escape ruled out, limit and integral commute.

---

# Sources and Targets

**Sources.** Hypotheses: $f_n\to f$ [[Def - Almost Everywhere|a.e.]] and $|f_n|\le g$ a.e. with $g\in L^1$. The art is *recognising or building the dominating $g$*: (i) a *uniform bound* $|f_n|\le M$ on a finite-measure space — take $g\equiv M\in L^1$ (this is *bounded convergence*); (ii) for a Cauchy sequence in $L^1$, the dominating function $g=\sum_k|f_{n_{k+1}}-f_{n_k}|$ built from a rapidly-convergent subsequence (the key trick in proving [[Thm - Completeness of Lp Spaces|completeness of Lᵖ]]); (iii) in probability, $|X_n|\le Y$ for an integrable $Y$, or $L^p$-boundedness for $p>1$. Building the dominator is the input-broadening skill.

**Targets.** "$\int f_n\to\int f$" combines with: (i) the *mean value theorem* to give **differentiation under the integral sign** — $\frac{d}{dt}\int f(t,x)\,d\mu=\int\partial_t f(t,x)\,d\mu$ when $|\partial_t f|\le g\in L^1$; (ii) [[Thm - Markov's Inequality|Markov]] to control [[Def - Convergence in Measure|convergence in measure]]; (iii) continuity of [[Def - Characteristic Function|characteristic functions]] and other integral transforms.

---

# Formal Statement

Let $g\in L^1(\mu)$, $g\ge0$, and let $f,f_n:X\to[-\infty,\infty]$ be measurable with
$$|f_n|\le g\ \ \mu\text{-a.e. (all }n),\qquad f_n\to f\ \ \mu\text{-a.e.}$$
Then $f_n,f\in L^1(\mu)$ and
$$\int_X|f_n-f|\,d\mu\xrightarrow[n\to\infty]{}0,\qquad\text{hence}\qquad \int_X f_n\,d\mu\xrightarrow[n\to\infty]{}\int_X f\,d\mu.$$

---

# Why Is It True

First, integrability: $|f_n|\le g$ and $f_n\to f$ a.e. give $|f|\le g$ a.e., so $f,f_n\in L^1$ (dominated by an integrable function) and $|f_n-f|\le 2g\in L^1$. All integrals in sight are finite.

The conclusion is **Fatou applied to a cleverly chosen non-negative sequence**. The functions $2g-|f_n-f|$ are $\ge0$ (since $|f_n-f|\le2g$), so [[Thm - Fatou's Lemma|Fatou]] applies to them:
$$\int\liminf_n\big(2g-|f_n-f|\big)\,d\mu\ \le\ \liminf_n\int\big(2g-|f_n-f|\big)\,d\mu.$$
Now evaluate both sides. On the left, $f_n\to f$ a.e. forces $|f_n-f|\to0$ a.e., so $\liminf(2g-|f_n-f|)=2g$ a.e., and the left side is $\int 2g$. On the right, [[Thm - Properties of the Integral|linearity]] splits the integral: $\int 2g-\limsup_n\int|f_n-f|$ (the $\liminf$ of $-(\cdots)$ is $-\limsup$). So
$$\int 2g\ \le\ \int 2g-\limsup_n\int|f_n-f|.$$
Since $\int 2g<\infty$ it cancels, leaving $\limsup_n\int|f_n-f|\le0$. As the integrand is non-negative, $\int|f_n-f|\to0$. Finally $|\int f_n-\int f|=|\int(f_n-f)|\le\int|f_n-f|\to0$ by the [[Thm - Properties of the Integral|triangle inequality]].

The mechanism in one line: **the dominator $g$ does two jobs — it makes $2g\pm(f_n-f)\ge0$ so Fatou is legal, and it is integrable so $\int 2g$ can be cancelled.** The dominator is precisely what *pins the mass down*: it forbids the escape-to-infinity that makes [[Thm - Fatou's Lemma|Fatou]] strict and breaks naive limit-swapping.

---

# What Makes This Hard

The proof has exactly one non-obvious move and it is everything: **apply Fatou not to $f_n$ but to the auxiliary non-negative sequence $2g-|f_n-f|$.** Manufacturing a non-negative quantity out of a signed problem, so that the hypothesis-light Fatou becomes applicable, is the trick. The second subtlety is *why $g$ must be integrable*: it is so that $\int 2g$ is finite and can be subtracted off — exactly the same "no $\infty-\infty$" discipline as everywhere. The classic error is forgetting domination entirely: the moving bump $f_n=\tfrac1n\mathbf{1}_{[0,n]}$ has $f_n\to0$ but $\int f_n=1\not\to0$, because *no* integrable $g$ dominates the whole sequence.

---

# Rederivation Scaffold

**High-level strategy.** Domination $\Rightarrow$ all functions in $L^1$. Apply [[Thm - Fatou's Lemma|Fatou]] to $2g-|f_n-f|\ge0$; evaluate both sides; cancel the finite $\int 2g$ to get $\int|f_n-f|\to0$; triangle inequality finishes.

**Subgoal decomposition.**

1. **Integrability.** $|f_n|\le g$, $f_n\to f$ a.e. $\Rightarrow|f|\le g$ a.e. $\Rightarrow f,f_n\in L^1$ and $|f_n-f|\le2g\in L^1$.
2. **Apply Fatou to $2g-|f_n-f|\ge0$.**
3. **Evaluate.** Left: $\liminf=2g$ a.e. Right: linearity gives $\int 2g-\limsup\int|f_n-f|$.
4. **Cancel and conclude.** $\int 2g<\infty$ cancels $\Rightarrow\limsup\int|f_n-f|\le0\Rightarrow\int|f_n-f|\to0$; triangle inequality gives $\int f_n\to\int f$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Domination forces integrability
> **Statement:** Under the hypotheses, $f,f_n\in L^1$ and $|f_n-f|\le2g$ a.e.
>
> > [!note]- Full proof
> > $|f_n|\le g$ a.e. and $f_n\to f$ a.e. give $|f|=\lim|f_n|\le g$ a.e. By [[Thm - Properties of the Integral|monotonicity]], $\int|f|\le\int g<\infty$ and $\int|f_n|\le\int g<\infty$, so $f,f_n\in L^1$. Then $|f_n-f|\le|f_n|+|f|\le2g$ a.e. $\square$

> [!note]- Lemma 2: Fatou on the auxiliary sequence
> **Statement:** $\limsup_n\int|f_n-f|\,d\mu\le0$.
>
> **Hint:** Apply Fatou to $2g-|f_n-f|\ge0$.
>
> > [!note]- Full proof
> > By Lemma 1, $h_n:=2g-|f_n-f|\ge0$ a.e. and is measurable. [[Thm - Fatou's Lemma|Fatou]]: $\int\liminf h_n\le\liminf\int h_n$. Since $f_n\to f$ a.e., $|f_n-f|\to0$ a.e., so $\liminf h_n=2g$ a.e., and the left side is $\int 2g$. By [[Thm - Properties of the Integral|linearity]], $\int h_n=\int 2g-\int|f_n-f|$, so $\liminf\int h_n=\int 2g-\limsup\int|f_n-f|$. Thus $\int 2g\le\int 2g-\limsup\int|f_n-f|$; since $\int 2g<\infty$, cancel to get $\limsup\int|f_n-f|\le0$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 puts $f,f_n$ in $L^1$. Lemma 2 gives $\limsup_n\int|f_n-f|\le0$; as $\int|f_n-f|\ge0$, $\lim_n\int|f_n-f|=0$. Finally, by the [[Thm - Properties of the Integral|triangle inequality]], $\big|\int f_n-\int f\big|=\big|\int(f_n-f)\big|\le\int|f_n-f|\to0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

DCT + the mean value theorem yields **differentiation under the integral**: if $|\partial_t f(t,x)|\le g(x)\in L^1$, then $\frac{d}{dt}\int f(t,x)\,d\mu=\int\partial_t f(t,x)\,d\mu$ — proved by applying DCT to the difference quotients. This computes derivatives of [[Def - Characteristic Function|characteristic functions]], proves smoothness of the heat kernel, and is the engine of countless analytic estimates. In probability, DCT with a uniform bound is *bounded convergence*, and DCT is what upgrades a.s. convergence to $L^1$ convergence when a dominating variable exists — the dominated case of the [[Thm - Vitali Convergence Theorem|Vitali theorem]].

---

# Bridges

- **[[Thm - Fatou's Lemma]]** — DCT is Fatou applied to $2g\pm(f_n-f)$; the dominator $g$ converts Fatou's one-sided inequality into a two-sided equality.
- **[[Thm - Vitali Convergence Theorem]]** — generalises DCT: the rigid hypothesis "$\exists$ dominating $g$" is replaced by the optimal "[[Def - Uniform Integrability|uniformly integrable]]."
- **[[Thm - Completeness of Lp Spaces]]** — its proof builds a dominating function $\sum|f_{n_{k+1}}-f_{n_k}|$ and invokes DCT.
