---
type: definition
subject: measure-theory
prereqs:
  - "Def - The Integral"
  - "Def - Lebesgue Measure"
tags: [analysis, measure-theory]
---

# Notation

$f\in L^1_{loc}(\mathbb{R}^n)$ — locally integrable. $B(x,r)$ — the open ball of radius $r$ about $x$; $\lambda$ Lebesgue measure; $\frac{1}{\lambda(B)}\int_{B}=\frac1{\lambda(B)}\int_B$ the average. $f^*$ — the maximal function.

---

# Axiom Motivation

The [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation theorem]] asserts that the local averages $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f$ recover $f(x)$ as $r\to0$, for almost every $x$. To prove an *almost-everywhere* limit statement, the standard route is: prove it on a dense class where it is easy (continuous functions), then control the *exceptional set* for general $f$ by a quantitative bound. The object that delivers the quantitative bound is the **Hardy–Littlewood maximal function**.

The idea: instead of tracking the limit of averages, track their *supremum* over all radii — the worst-case average. $f^*(x)=\sup_{r>0}\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f|$ dominates every average, so controlling $f^*$ controls all of them at once. The decisive fact is the **maximal inequality**: $f^*$ is *weakly* bounded, $\lambda(\{f^*>a\})\le\frac{C}{a}\|f\|_1$ — the set where the worst-case average is large has small measure. This weak bound is exactly the tool that squeezes the exceptional set in the differentiation theorem to measure zero.

Why the *supremum* and not the limit? Because the supremum is *monotone and measurable* and amenable to a covering argument, whereas the limit is the very thing in question. And why only a *weak* ($L^1\to L^{1,\infty}$) bound, not a strong $L^1\to L^1$ one? Because $f^*$ is genuinely *not* in $L^1$ (it decays like $|x|^{-n}$ at infinity, borderline non-integrable) — the weak bound is the best possible, and it is enough. The maximal function is the prototype of a vast family of operators in harmonic analysis; its weak bound, proved via the [[Thm - Lebesgue Differentiation Theorem|Vitali covering lemma]], is the template for the whole subject.

---

# The Definition

For $f\in L^1_{loc}(\mathbb{R}^n)$, the **Hardy–Littlewood maximal function** is
$$f^*(x)=\sup_{r>0}\ \frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f(y)|\,dy\ \in[0,\infty].$$
It is the supremum, over all radii, of the average of $|f|$ on the ball $B(x,r)$.

$f^*$ is measurable (each average $x\mapsto\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f|$ is continuous, and $f^*$ is a supremum of them). It satisfies the **maximal inequality**: for $f\in L^1(\mathbb{R}^n)$ and every $a>0$,
$$\lambda\big(\{x:f^*(x)>a\}\big)\ \le\ \frac{5^n}{a}\,\|f\|_{L^1(\mathbb{R}^n)}.$$
In general $f^*\notin L^1(\mathbb{R}^n)$ unless $f=0$: it decays only like $|x|^{-n}$, just failing integrability.

---

# Relate to Other Fields / Compression

The maximal function is the cornerstone of **harmonic analysis**: it controls singular integrals, the Hilbert transform, and Calderón–Zygmund operators, and the *maximal inequality* is the prototype "weak-type $(1,1)$" bound from which $L^p$-boundedness for $1<p\le\infty$ follows by interpolation. The same construction — sup of averages over a family of sets — gives the *martingale maximal function* of [[Thm - Doob's Maximal Inequality|Doob's inequality]] and the *ergodic maximal function* behind the pointwise ergodic theorem. All three maximal inequalities are proved by the same covering idea, and all three serve the same purpose: bounding the exceptional set in an a.e.-convergence theorem.

---

# Examples / Corollaries

For $f=\mathbf{1}_{B(0,1)}$, $f^*(x)$ is comparable to $\min(1,|x|^{-n})$ — it equals $1$ inside and decays like $|x|^{-n}$ outside, confirming $f^*\notin L^1$.

For $f$ **continuous** at $x$, $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f|\to|f(x)|$ as $r\to0$, so the *small-radius* averages behave well; $f^*$ captures instead the *worst* radius.

Corollary (the point of it all): the maximal inequality bounds $\lambda(\{(f-g)^*>a\})$ by $\frac{5^n}{a}\|f-g\|_1$; taking $g$ a continuous approximation of $f$ makes the right side small, which forces the exceptional set of the [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]] to be null.

Calibration: (i) Is $f^*\ge|f|$ a.e.? Yes — at a [[Thm - Lebesgue Differentiation Theorem|Lebesgue point]] the averages tend to $|f|$, and $f^*$ is their sup. (ii) Is $f^*\in L^1$? No, unless $f=0$. (iii) Is the maximal inequality a *strong* or *weak* bound? Weak — it bounds a level set, not a norm; that is the best possible at $p=1$.

---

# Unlocked by This

> [!tip] Lebesgue differentiation theorem
> The maximal inequality is the engine of the [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation theorem]]: $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f\to f(x)$ for a.e. $x$, for every locally integrable $f$.

> [!tip] Doob's maximal inequality *(from Martingale Theory)*
> The martingale analogue — $\lambda\,\mathbb{P}(\sup_n|X_n|\ge\lambda)\le\mathbb{E}|X_N|$ — is the same maximal-inequality idea for [[Def - Martingale|martingales]]; see [[Thm - Doob's Maximal Inequality]].
