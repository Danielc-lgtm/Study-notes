---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Lp Spaces"
  - "Def - The Integral"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $1\le p,q\le\infty$ **conjugate exponents**, $\tfrac1p+\tfrac1q=1$; $\|f\|_p$ the [[Def - Lp Spaces|Lᵖ norm]].

---

# Motivation

For $L^p$ to be a *normed* vector space, $\|\cdot\|_p$ must satisfy the triangle inequality $\|f+g\|_p\le\|f\|_p+\|g\|_p$ — **Minkowski's inequality**. For $p=1$ and $p=\infty$ this is easy; for $1<p<\infty$ it is not obvious at all (the function $t\mapsto t^p$ is nonlinear). The route to it runs through **Hölder's inequality** $\int|fg|\le\|f\|_p\|g\|_q$, which is itself the fundamental pairing between $L^p$ and its dual $L^q$ — the inequality that says "an $L^p$ function tested against an $L^q$ function gives an $L^1$ number." Hölder generalises Cauchy–Schwarz ($p=q=2$); together the two inequalities are the structural backbone of all $L^p$ theory.

---

# Sources and Targets

**Sources.** Both rest on the *convexity* of $t\mapsto t^p$, packaged as **Young's inequality** $ab\le\tfrac{a^p}{p}+\tfrac{b^q}{q}$. Recognising a product to be split, or a sum to be bounded, as an instance of conjugate-exponent structure is the source skill.

**Targets.** Hölder gives: the **inclusion $L^{p'}\subseteq L^p$** on a finite-measure space ($p\le p'$); **interpolation** $\|f\|_r\le\|f\|_p^\theta\|f\|_q^{1-\theta}$; the pairing realising $L^q=(L^p)^*$. Minkowski gives the triangle inequality, hence makes $L^p$ a normed space and underwrites [[Thm - Completeness of Lp Spaces|its completeness]].

---

# Statement

Let $1\le p,q\le\infty$ with $\tfrac1p+\tfrac1q=1$, and $f,g$ measurable.

**(Young's inequality)** For $a,b\ge0$ and $1<p,q<\infty$ conjugate: $\displaystyle ab\le\frac{a^p}{p}+\frac{b^q}{q}$, with equality iff $a^p=b^q$.

**(Hölder)** $\displaystyle\int_X|fg|\,d\mu\ \le\ \|f\|_p\,\|g\|_q$. In particular $f\in L^p,g\in L^q\Rightarrow fg\in L^1$. The case $p=q=2$ is the **Cauchy–Schwarz inequality**.

**(Minkowski)** For $f,g\in L^p$, $1\le p\le\infty$: $\displaystyle\|f+g\|_p\le\|f\|_p+\|g\|_p$, so $L^p$ is closed under addition and $\|\cdot\|_p$ is a norm.

---

# Why Is It True

**Young** is convexity of $-\log$. Since $-\log$ is strictly convex, $-\log\!\big(\tfrac{a^p}{p}+\tfrac{b^q}{q}\big)\le\tfrac1p(-\log a^p)+\tfrac1q(-\log b^q)=-\log(ab)$ (the weights $\tfrac1p,\tfrac1q$ sum to $1$). Exponentiating reverses the inequality: $ab\le\tfrac{a^p}{p}+\tfrac{b^q}{q}$. Young *is* the convexity of the logarithm, nothing more.

**Hölder** is Young, integrated. Normalise: assume $\|f\|_p=\|g\|_q=1$ (divide through; the degenerate cases $\|f\|_p\in\{0,\infty\}$ are trivial). Apply Young pointwise to $a=|f(x)|,b=|g(x)|$: $|f(x)g(x)|\le\tfrac{|f(x)|^p}{p}+\tfrac{|g(x)|^q}{q}$. Integrate, using [[Thm - Properties of the Integral|linearity]]: $\int|fg|\le\tfrac1p\|f\|_p^p+\tfrac1q\|g\|_q^q=\tfrac1p+\tfrac1q=1=\|f\|_p\|g\|_q$. The normalisation is what makes the right side collapse to $1$.

**Minkowski** is Hölder, applied cleverly. For $p=1,\infty$ it is the triangle inequality of $\mathbb{R}$ integrated/ess-sup'd. For $1<p<\infty$: write $|f+g|^p=|f+g|\,|f+g|^{p-1}\le(|f|+|g|)|f+g|^{p-1}$, integrate, and apply Hölder to each term, pairing $|f|\in L^p$ with $|f+g|^{p-1}\in L^q$ (note $(p-1)q=p$). This produces $\|f+g\|_p^p\le(\|f\|_p+\|g\|_p)\,\|f+g\|_p^{p-1}$; divide by $\|f+g\|_p^{p-1}$. Alternatively, and most cleanly, Minkowski *is the convexity of $t\mapsto t^p$ directly*: writing $h=\tfrac{f}{\|f\|_p}$, $k=\tfrac{g}{\|g\|_p}$, $t=\tfrac{\|f\|_p}{\|f\|_p+\|g\|_p}$, the claim $\|th+(1-t)k\|_p\le1$ follows from $|th+(1-t)k|^p\le t|h|^p+(1-t)|k|^p$ integrated — and that pointwise inequality is exactly convexity of $s\mapsto s^p$.

The unifying frame: **convexity is the single source.** Young is convexity of $-\log$; Hölder is Young integrated; Minkowski is convexity of $t^p$ integrated. Every $L^p$ inequality is a convexity statement run through the integral.

---

# What Makes This Hard

The genuine ideas: (i) the **conjugate-exponent bookkeeping** $\tfrac1p+\tfrac1q=1$, which is what makes $\tfrac1p+\tfrac1q$ collapse to $1$ after normalisation, and what makes $(p-1)q=p$ in the Minkowski step; (ii) the **normalisation** to unit norm, without which Hölder's right side does not simplify; (iii) for Minkowski, the splitting $|f+g|^p=|f+g|\cdot|f+g|^{p-1}$ that creates an $L^q$ factor to feed Hölder. The common error is forgetting to handle $p=1,\infty$ separately (Young/Hölder's conjugate structure degenerates there) and mismatching the exponents.

---

# Rederivation Scaffold

**High-level strategy.** Young from convexity of $-\log$. Hölder: normalise, apply Young pointwise, integrate. Minkowski: split $|f+g|^p$, apply Hölder twice (or invoke convexity of $t^p$ directly).

**Subgoal decomposition.**

1. **Young.** $-\log$ convex $\Rightarrow ab\le a^p/p+b^q/q$.
2. **Hölder.** Reduce to $\|f\|_p=\|g\|_q=1$; Young pointwise; integrate to get $\int|fg|\le1$.
3. **Minkowski, $p\in(1,\infty)$.** $|f+g|^p\le(|f|+|g|)|f+g|^{p-1}$; integrate; Hölder on each term with $(p-1)q=p$; divide by $\|f+g\|_p^{p-1}$.
4. **Minkowski, $p\in\{1,\infty\}$.** Triangle inequality of $\mathbb{R}$, integrated or ess-sup'd.

---

# Lemma Decomposition

> [!note]- Lemma 1: Young's inequality
> **Statement:** $ab\le a^p/p+b^q/q$ for $a,b\ge0$, $1<p,q<\infty$, $\tfrac1p+\tfrac1q=1$.
>
> > [!note]- Full proof
> > If $a=0$ or $b=0$ trivial. Else, by convexity of $-\log$ on $(0,\infty)$ with weights $\tfrac1p+\tfrac1q=1$: $-\log\big(\tfrac1p a^p+\tfrac1q b^q\big)\le\tfrac1p(-\log a^p)+\tfrac1q(-\log b^q)=-\log a-\log b=-\log(ab)$. Since $-\log$ is decreasing, $\tfrac1p a^p+\tfrac1q b^q\ge ab$. Equality in convexity iff $a^p=b^q$. $\square$

> [!note]- Lemma 2: Hölder's inequality
> **Statement:** $\int|fg|\,d\mu\le\|f\|_p\|g\|_q$.
>
> > [!note]- Full proof
> > If $p=1,q=\infty$: $|fg|\le|f|\,\|g\|_\infty$ a.e., integrate. For $1<p,q<\infty$: if $\|f\|_p$ or $\|g\|_q$ is $0$ or $\infty$ the inequality is trivial; otherwise set $\tilde f=f/\|f\|_p$, $\tilde g=g/\|g\|_q$. By Lemma 1 pointwise, $|\tilde f\tilde g|\le\tfrac1p|\tilde f|^p+\tfrac1q|\tilde g|^q$; integrate: $\int|\tilde f\tilde g|\le\tfrac1p\|\tilde f\|_p^p+\tfrac1q\|\tilde g\|_q^q=\tfrac1p+\tfrac1q=1$. Multiply by $\|f\|_p\|g\|_q$. $\square$

> [!note]- Lemma 3: Minkowski's inequality
> **Statement:** $\|f+g\|_p\le\|f\|_p+\|g\|_p$.
>
> > [!note]- Full proof
> > $p\in\{1,\infty\}$: from $|f+g|\le|f|+|g|$, integrate or take ess-sup. $1<p<\infty$: $\|f+g\|_p^p=\int|f+g|^p\le\int(|f|+|g|)|f+g|^{p-1}=\int|f|\,|f+g|^{p-1}+\int|g|\,|f+g|^{p-1}$. Apply Lemma 2 to each term with exponents $p,q$: $|f+g|^{p-1}\in L^q$ since $(p-1)q=p$ and $\big\||f+g|^{p-1}\big\|_q=\|f+g\|_p^{p/q}=\|f+g\|_p^{p-1}$. So $\|f+g\|_p^p\le(\|f\|_p+\|g\|_p)\|f+g\|_p^{p-1}$. If $\|f+g\|_p\in(0,\infty)$ divide; the cases $0,\infty$ are direct. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemmas 1–3. Lemma 1 (Young) feeds Lemma 2 (Hölder), which feeds Lemma 3 (Minkowski). Minkowski makes $\|\cdot\|_p$ subadditive; with $\|\alpha f\|_p=|\alpha|\|f\|_p$ and positive-definiteness on $L^p$ (modulo a.e.), $\|\cdot\|_p$ is a norm. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Hölder on a *probability* space gives the **moment inequality** $\|X\|_r\le\|X\|_p$ for $r\le p$ — higher moments dominate lower (a special case: $\mathrm{Var}\ge0$). Cauchy–Schwarz ($p=q=2$) gives $|\mathbb{E}[XY]|\le\|X\|_2\|Y\|_2$, the bound behind correlation coefficients and the [[Def - Conditional Expectation|L² projection]] picture of conditional expectation. Hölder also yields the **Lyapunov / log-convexity** of $p\mapsto\log\|X\|_p$, used in interpolation and large-deviation estimates.

---

# Bridges

- **[[Thm - Completeness of Lp Spaces]]** — Minkowski makes $L^p$ a normed space; completeness then makes it Banach.
- **[[Def - Lp Spaces]]** — these inequalities are what make $\|\cdot\|_p$ a genuine norm and $L^p$ a vector space.
- **Jensen's inequality** — Young, Hölder, Minkowski are all convexity statements; Jensen is the general convexity-and-integration principle behind them.
