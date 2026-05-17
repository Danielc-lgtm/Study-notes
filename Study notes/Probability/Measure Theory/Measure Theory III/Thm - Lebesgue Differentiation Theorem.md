---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Hardy-Littlewood Maximal Function"
  - "Def - Lebesgue Measure"
  - "Thm - Dominated Convergence Theorem"
tags: [analysis, measure-theory]
---

# Notation

$f\in L^1_{loc}(\mathbb{R}^n)$; $B(x,r)$ the ball of radius $r$; $\fint_{B}=\frac1{\lambda(B)}\int_B$. $f^*$ — the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal function]].

---

# Motivation

The fundamental theorem of calculus says $\frac{d}{dx}\int_a^x f=f(x)$ for *continuous* $f$. Does it survive when $f$ is merely integrable — when $f$ may be discontinuous everywhere? The Lebesgue differentiation theorem answers *yes, almost everywhere*: the local averages $\fint_{B(x,r)}f$ converge to $f(x)$ for almost every $x$, for *every* locally integrable $f$. It is the measure-theoretic fundamental theorem of calculus, and the statement that "$f(x)$ is recoverable from $f$'s averages near $x$" — a function is, a.e., the limit of its own local means.

---

# Sources and Targets

**Sources.** Hypothesis: $f\in L^1_{loc}(\mathbb{R}^n)$. The proof's broadening: it suffices to treat $f\in L^1$ (localise by $f\mathbf{1}_{B(x,1)}$); the balls $B(x,r)$ may be replaced by cubes or any "nicely shrinking" family.

**Targets.** The conclusion gives: **Lebesgue points** (a.e. $x$ satisfies even $\fint_{B(x,r)}|f-f(x)|\to0$); the **density theorem** — for measurable $E$, a.e. point of $E$ has density $1$ in $E$; and the a.e. differentiability of the indefinite integral, the FTC for Lebesgue integrals.

---

# Formal Statement

For every $f\in L^1_{loc}(\mathbb{R}^n)$,
$$\lim_{r\downarrow0}\ \frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f(y)\,dy\ =\ f(x)\qquad\text{for }\lambda\text{-a.e. }x\in\mathbb{R}^n.$$
More strongly, $\lim_{r\downarrow0}\fint_{B(x,r)}|f(y)-f(x)|\,dy=0$ for a.e. $x$ (such $x$ are **Lebesgue points** of $f$). Balls may be replaced by cubes.

---

# Why Is It True

The proof is the canonical **"dense class + maximal inequality" argument** for an a.e. limit.

*Step 1 — the easy class.* For **continuous** $g$, $\fint_{B(x,r)}g\to g(x)$ at *every* $x$ — an $\varepsilon$–$\delta$ triviality, since $g$ is nearly constant on a small ball. So the theorem holds on the dense subclass $C_c(\mathbb{R}^n)\subseteq L^1$.

*Step 2 — control the error for general $f$.* Write $f=g+(f-g)$ with $g$ continuous, $\|f-g\|_1<\varepsilon$ (density of $C_c$ in [[Def - Lp Spaces|$L^1$]]). The averaging error of $f$ is bounded by: the error of $g$ (which is $0$, Step 1) $+$ the contribution of $f-g$. The latter is controlled by *two* quantities — the [[Def - Hardy-Littlewood Maximal Function|maximal function]] $(f-g)^*$ and the pointwise value $|f-g|$:
$$\limsup_{r\to0}\Big|\fint_{B(x,r)}f-f(x)\Big|\le(f-g)^*(x)+|f(x)-g(x)|.$$

*Step 3 — squeeze the exceptional set.* Let $A_\varepsilon=\{x:\limsup_r|\fint f-f(x)|>2\varepsilon\}$. By Step 2, $A_\varepsilon\subseteq\{(f-g)^*>\varepsilon\}\cup\{|f-g|>\varepsilon\}$. Now bound both: the **maximal inequality** gives $\lambda((f-g)^*>\varepsilon)\le\frac{5^n}{\varepsilon}\|f-g\|_1<\frac{5^n\varepsilon}{\varepsilon}=5^n$... — sharpen by choosing $\|f-g\|_1<\varepsilon^2$: then $\lambda((f-g)^*>\varepsilon)\le5^n\varepsilon$, and [[Ex - Markov's inequality|Markov]] gives $\lambda(|f-g|>\varepsilon)\le\varepsilon$. So $\lambda(A_\varepsilon)\le(5^n+1)\varepsilon$. Since $g$ (hence $\varepsilon$) was arbitrary, $\lambda(A_\varepsilon)=0$; and $A=\bigcup_k A_{1/k}$ is null. Off $A$, the limit is $f(x)$.

The mechanism: **the maximal inequality is precisely the device that bounds the exceptional set.** On the dense class the limit is exact; the error for general $f$ is the error of an $L^1$-small perturbation; and the maximal function converts "$L^1$-small perturbation" into "small exceptional set" — because $f^*$ controls *all* averages simultaneously. The maximal inequality itself is proved by the **[[Thm - Lebesgue Differentiation Theorem#Lemma 1|Vitali covering lemma]]** — from any family of balls covering the level set, extract a *disjoint* subfamily whose $5\times$ dilates still cover, so the level set's measure is controlled by $5^n\times$ a disjoint sum of integrals, i.e. by $\|f\|_1$.

---

# What Makes This Hard

The architecture — dense class, then maximal inequality to kill the exceptional set — is the non-obvious idea, and it is *the* template for proving a.e.-convergence theorems (the same shape recurs for the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]] and the pointwise ergodic theorem). The technical heart is the **Vitali covering lemma** and the geometric factor $5^n$: one must see that disjointifying a cover, at the cost of dilating by $5$, is what makes the maximal inequality dimension-uniform. The common error is to expect a *strong* ($L^1$) bound on $f^*$ — there is none; only the *weak* bound, and it is exactly enough.

---

# Rederivation Scaffold

**High-level strategy.** Prove the limit on continuous functions (trivial). For general $f$, split $f=g+(f-g)$ with $g$ continuous and $\|f-g\|_1$ tiny; bound the exceptional set by $\{(f-g)^*>\varepsilon\}\cup\{|f-g|>\varepsilon\}$; kill it with the maximal inequality and Markov.

**Subgoal decomposition.**

1. **Vitali covering lemma.** From balls covering a set, extract disjoint balls whose $5\times$ dilates cover.
2. **Maximal inequality.** $\lambda(f^*>a)\le\frac{5^n}{a}\|f\|_1$, from the covering lemma.
3. **Continuous case.** $\fint_{B(x,r)}g\to g(x)$ everywhere, by uniform continuity locally.
4. **Squeeze.** $f=g+(f-g)$, $\|f-g\|_1<\varepsilon^2$; bound $\lambda(A_\varepsilon)\le(5^n+1)\varepsilon$ via the maximal inequality and Markov; let $\varepsilon\to0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Vitali covering lemma
> **Statement:** Let $\mathcal{F}$ be a family of balls in $\mathbb{R}^n$ with $\sup_{B\in\mathcal{F}}\operatorname{diam}B<\infty$. There is a countable *disjoint* subfamily $\mathcal{G}\subseteq\mathcal{F}$ with $\bigcup_{B\in\mathcal{F}}B\subseteq\bigcup_{B\in\mathcal{G}}\widehat B$, where $\widehat B$ is $B$ concentrically dilated by $5$.
>
> > [!note]- Full proof
> > Greedily select disjoint balls, at each stage taking one of (nearly) maximal radius among those disjoint from all chosen so far. Any $B_0\in\mathcal{F}$ meets some chosen $B$ of radius $\ge\frac12\operatorname{rad}B_0$ (else $B_0$ would have been selectable); then $B_0\subseteq\widehat B$ by the triangle inequality. $\square$

> [!note]- Lemma 2: The maximal inequality
> **Statement:** For $f\in L^1(\mathbb{R}^n)$, $a>0$: $\lambda(\{f^*>a\})\le\frac{5^n}{a}\|f\|_1$.
>
> > [!note]- Full proof
> > For each $x$ with $f^*(x)>a$ pick a ball $B_x$ with $\fint_{B_x}|f|>a$, so $\lambda(B_x)<\frac1a\int_{B_x}|f|$. These balls cover $\{f^*>a\}$; by Lemma 1 extract disjoint $B_1,B_2,\dots$ with $5\times$-dilates covering. Then $\lambda(f^*>a)\le\sum_j\lambda(\widehat B_j)=5^n\sum_j\lambda(B_j)\le\frac{5^n}{a}\sum_j\int_{B_j}|f|\le\frac{5^n}{a}\|f\|_1$, the last step by disjointness. $\square$

> [!note]- Lemma 3: The continuous case
> **Statement:** For $g$ continuous, $\fint_{B(x,r)}g\to g(x)$ at every $x$.
>
> > [!note]- Full proof
> > Given $\varepsilon$, continuity gives $\delta$ with $|g(y)-g(x)|<\varepsilon$ for $|y-x|<\delta$; then for $r<\delta$, $|\fint_{B(x,r)}g-g(x)|\le\fint_{B(x,r)}|g-g(x)|<\varepsilon$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> WLOG $f\in L^1(\mathbb{R}^n)$. Given $\varepsilon>0$, density of $C_c$ in $L^1$ gives continuous $g$ with $\|f-g\|_1<\varepsilon^2$. For any $x$, $\limsup_r|\fint_{B(x,r)}f-f(x)|\le\limsup_r\fint|f-g|+\limsup_r|\fint g-g(x)|+|g(x)-f(x)|\le(f-g)^*(x)+0+|f-g|(x)$ (Lemma 3 kills the middle term). So $A_\varepsilon:=\{\limsup_r|\fint f-f(x)|>2\varepsilon\}\subseteq\{(f-g)^*>\varepsilon\}\cup\{|f-g|>\varepsilon\}$, and by Lemma 2 and [[Ex - Markov's inequality|Markov]], $\lambda(A_\varepsilon)\le\frac{5^n}{\varepsilon}\|f-g\|_1+\frac1\varepsilon\|f-g\|_1<(5^n+1)\varepsilon$. As $\varepsilon$ is arbitrary, $\lambda(A_\varepsilon)=0$; $A=\bigcup_k A_{1/k}$ is null, and off $A$ the limit equals $f(x)$. The Lebesgue-point statement follows by applying this to $|f-c|$ over a countable dense set of constants $c$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The Lebesgue **density theorem** is the special case $f=\mathbf{1}_E$: a.e. point of a measurable set $E$ has *density $1$* ($\lambda(E\cap B(x,r))/\lambda(B(x,r))\to1$) — measurable sets have no "fuzzy" points, almost. The same dense-class-plus-maximal-inequality architecture proves the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]] (with [[Thm - Doob's Maximal Inequality|Doob's]] maximal inequality) and the pointwise ergodic theorem (with the ergodic maximal inequality).

---

# Bridges

- **[[Def - Hardy-Littlewood Maximal Function]]** — the maximal function and its weak inequality are the engine.
- **[[Thm - Doob's Maximal Inequality]]** *(Martingale Theory)* — the martingale twin of the maximal inequality, proving a.s. martingale convergence by the same template.
- **[[Thm - Radon-Nikodym Theorem]]** — for $\nu\ll\lambda$, the differentiation theorem shows $\mathrm{d}\nu/\mathrm{d}\lambda(x)=\lim_r\nu(B(x,r))/\lambda(B(x,r))$.
