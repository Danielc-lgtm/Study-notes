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

$f\in L^1_{loc}(\mathbb{R}^n)$; $B(x,r)$ the ball of radius $r$; $\frac{1}{\lambda(B)}\int_{B}=\frac1{\lambda(B)}\int_B$. $f^*$ — the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal function]].

---

# Motivation

The fundamental theorem of calculus says $\frac{d}{dx}\int_a^x f=f(x)$ for *continuous* $f$. Does it survive when $f$ is merely integrable — when $f$ may be discontinuous everywhere? The Lebesgue differentiation theorem answers *yes, almost everywhere*: the local averages $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f$ converge to $f(x)$ for almost every $x$, for *every* locally integrable $f$. It is the measure-theoretic fundamental theorem of calculus, and the statement that "$f(x)$ is recoverable from $f$'s averages near $x$" — a function is, a.e., the limit of its own local means.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is $f\in L^1_{loc}(\mathbb{R}^n)$. This is already a strikingly weak hypothesis — no continuity, no smoothness, no global integrability — and a great deal of analysis lives inside $L^1_{loc}$ in disguise.

The first source is **any locally integrable function recognised through a finite-energy or finite-mass condition**. A function $f$ defined on $\mathbb{R}^n$ with $\int_K|f|<\infty$ on every compact $K$ qualifies, even if $f\notin L^1$ globally — polynomials, the Coulomb potential $1/|x|$ on $\mathbb{R}^3$ away from $0$, and every continuous function are in $L^1_{loc}$. The bridge: local integrability is exactly what is needed to make $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f$ well-defined and finite for every $r>0$, which is what the theorem requires. A concrete problem: in electrostatics one needs to recover a charge density from its potential averages near a point, and any reasonable charge density — even singular ones like dipoles smeared on a hypersurface, after mollification — sits in $L^1_{loc}$.

The second source is **the indicator function $\mathbf{1}_E$ of any measurable set $E\subseteq\mathbb{R}^n$**. This is trivially in $L^1_{loc}$ (it is bounded), but the substantive content is what LDT *says* about it: applying the theorem to $f=\mathbf{1}_E$ gives that $\frac{\lambda(E\cap B(x,r))}{\lambda(B(x,r))}\to\mathbf{1}_E(x)$ for a.e. $x$. The bridge is that "density of $E$ at $x$" is precisely "average of $\mathbf{1}_E$ near $x$." A concrete problem: in geometric measure theory, to show that a measurable set $E$ of positive Lebesgue measure has *measurable boundary* in any useful sense, one identifies points of density $1$ (the measure-theoretic interior) and points of density $0$ (the measure-theoretic exterior) — the Lebesgue density theorem says these account for almost every point of $\mathbb{R}^n$. This is the source for [[Thm - Steinhaus Theorem|Steinhaus]] and for the fact that a measurable set of positive measure contains "almost a ball" near a density point.

The third source is **any Sobolev or BV function**, which one might not initially see as locally integrable. A function $u\in W^{1,p}(\Omega)$ has $u\in L^p_{loc}\subseteq L^1_{loc}$ by Hölder, and a function of bounded variation has $u\in L^1_{loc}$ by definition. The bridge: once recognised as $L^1_{loc}$, the LDT supplies pointwise a.e. values that agree with the equivalence class — the *precise representative*. A concrete problem: solutions to elliptic PDEs in $W^{1,2}$ are defined only as equivalence classes, but the LDT lets one speak of pointwise a.e. values, and combined with Sobolev embedding it produces pointwise continuity of $u$ wherever $u\in W^{1,p}$ with $p>n$.

**Targets (Output Amplification)**

The conclusion is "$\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f\to f(x)$ a.e." On its own this is a one-line statement; combined with other ingredients it amplifies into three structurally distinct theorems.

The first combination is **LDT together with a density argument and the Lebesgue-point refinement**. The stronger form $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-f(x)|\to0$ at a.e. $x$ says that not just the *value* but the entire *local oscillation* of $f$ collapses to nothing near a.e. $x$. The amplified result: $f$ is recoverable pointwise a.e. from its averages, and so any operator defined by averaging — convolution with an approximate identity, mollification, smoothing kernels — converges pointwise a.e. to the original $f$ for every $f\in L^p$ with $p\ge1$. This is the foundational tool for approximation theory and the entire technology of regularisation in PDE.

The second combination is **LDT together with the [[Thm - Vitali Covering Theorem|Vitali covering lemma]] (in its full form, for sets rather than functions)**. The amplified result is the **differentiation of measures**: for any Borel measure $\nu$ on $\mathbb{R}^n$, the limit $D\nu(x)=\lim_r\nu(B(x,r))/\lambda(B(x,r))$ exists a.e., and if $\nu\ll\lambda$ then $D\nu=d\nu/d\lambda$ is the [[Thm - Radon-Nikodym Theorem|Radon-Nikodym derivative]]. The combination is non-obvious because it computes the Radon-Nikodym derivative — defined abstractly via $\sigma$-additivity and absolute continuity — as a concrete geometric limit of ratios. This is the path through which Radon-Nikodym becomes computable rather than merely existential.

The third combination is **LDT together with [[Thm - Sobolev Embedding Theorem|Sobolev embedding]]**. For $u\in W^{1,p}(\Omega)$ with $p>n$, Sobolev embedding gives $u\in C^{0,\alpha}$ for $\alpha=1-n/p$; LDT then identifies the precise representative of $u$ as the pointwise-everywhere Hölder-continuous function. The amplified result: Sobolev functions above the embedding threshold have *genuine pointwise values everywhere*, not just a.e., and these values inherit Hölder regularity. The combination is what makes regularity theory in PDE function: weak solutions in $W^{1,p}$ for $p>n$ are classical solutions in $C^{0,\alpha}$ at every point, and the bridge is LDT supplying the pointwise representative.

---

# Statement

For every $f\in L^1_{loc}(\mathbb{R}^n)$,
$$\lim_{r\downarrow0}\ \frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f(y)\,dy\ =\ f(x)\qquad\text{for }\lambda\text{-a.e. }x\in\mathbb{R}^n.$$
More strongly, $\lim_{r\downarrow0}\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f(y)-f(x)|\,dy=0$ for a.e. $x$ (such $x$ are **Lebesgue points** of $f$). Balls may be replaced by cubes.

---

# Why Is It True

The proof is the canonical **"dense class + maximal inequality" argument** for an a.e. limit.

*Step 1 — the easy class.* For **continuous** $g$, $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}g\to g(x)$ at *every* $x$ — an $\varepsilon$–$\delta$ triviality, since $g$ is nearly constant on a small ball. So the theorem holds on the dense subclass $C_c(\mathbb{R}^n)\subseteq L^1$.

*Step 2 — control the error for general $f$.* Write $f=g+(f-g)$ with $g$ continuous, $\|f-g\|_1<\varepsilon$ (density of $C_c$ in [[Def - Lp Spaces|L¹]]). The averaging error of $f$ is bounded by: the error of $g$ (which is $0$, Step 1) $+$ the contribution of $f-g$. The latter is controlled by *two* quantities — the [[Def - Hardy-Littlewood Maximal Function|maximal function]] $(f-g)^*$ and the pointwise value $|f-g|$:
$$\limsup_{r\to0}\Big|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f-f(x)\Big|\le(f-g)^*(x)+|f(x)-g(x)|.$$

*Step 3 — squeeze the exceptional set.* Let $A_\varepsilon=\{x:\limsup_r|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f-f(x)|>2\varepsilon\}$. By Step 2, $A_\varepsilon\subseteq\{(f-g)^*>\varepsilon\}\cup\{|f-g|>\varepsilon\}$. Now bound both: the **maximal inequality** gives $\lambda((f-g)^*>\varepsilon)\le\frac{5^n}{\varepsilon}\|f-g\|_1<\frac{5^n\varepsilon}{\varepsilon}=5^n$... — sharpen by choosing $\|f-g\|_1<\varepsilon^2$: then $\lambda((f-g)^*>\varepsilon)\le5^n\varepsilon$, and [[Ex - Markov's inequality|Markov]] gives $\lambda(|f-g|>\varepsilon)\le\varepsilon$. So $\lambda(A_\varepsilon)\le(5^n+1)\varepsilon$. Since $g$ (hence $\varepsilon$) was arbitrary, $\lambda(A_\varepsilon)=0$; and $A=\bigcup_k A_{1/k}$ is null. Off $A$, the limit is $f(x)$.

The mechanism: **the maximal inequality is precisely the device that bounds the exceptional set.** On the dense class the limit is exact; the error for general $f$ is the error of an $L^1$-small perturbation; and the maximal function converts "$L^1$-small perturbation" into "small exceptional set" — because $f^*$ controls *all* averages simultaneously. The maximal inequality itself is proved by the **[[Thm - Lebesgue Differentiation Theorem#Lemma 1|Vitali covering lemma]]** — from any family of balls covering the level set, extract a *disjoint* subfamily whose $5\times$ dilates still cover, so the level set's measure is controlled by $5^n\times$ a disjoint sum of integrals, i.e. by $\|f\|_1$.

---

# What Makes This Hard

The architecture — dense class, then maximal inequality to kill the exceptional set — is the non-obvious idea, and it is *the* template for proving a.e.-convergence theorems (the same shape recurs for the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]] and the pointwise ergodic theorem). The technical heart is the **Vitali covering lemma** and the geometric factor $5^n$: one must see that disjointifying a cover, at the cost of dilating by $5$, is what makes the maximal inequality [[Def - Dimension|dimension]]-uniform. The common error is to expect a *strong* ($L^1$) bound on $f^*$ — there is none; only the *weak* bound, and it is exactly enough.

---

# Rederivation Scaffold

**High-level strategy.** Prove the limit on continuous functions (trivial). For general $f$, split $f=g+(f-g)$ with $g$ continuous and $\|f-g\|_1$ tiny; bound the exceptional set by $\{(f-g)^*>\varepsilon\}\cup\{|f-g|>\varepsilon\}$; kill it with the maximal inequality and Markov.

**Subgoal decomposition.**

1. **Vitali covering lemma.** From balls covering a set, extract disjoint balls whose $5\times$ dilates cover.
2. **Maximal inequality.** $\lambda(f^*>a)\le\frac{5^n}{a}\|f\|_1$, from the covering lemma.
3. **Continuous case.** $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}g\to g(x)$ everywhere, by uniform continuity locally.
4. **Squeeze.** $f=g+(f-g)$, $\|f-g\|_1<\varepsilon^2$; bound $\lambda(A_\varepsilon)\le(5^n+1)\varepsilon$ via the maximal inequality and Markov; let $\varepsilon\to0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Vitali covering lemma
> **Statement:** Let $\mathcal{F}$ be a family of balls in $\mathbb{R}^n$ with $\sup_{B\in\mathcal{F}}\operatorname{diam}B<\infty$. There is a countable *disjoint* subfamily $\mathcal{G}\subseteq\mathcal{F}$ with $\bigcup_{B\in\mathcal{F}}B\subseteq\bigcup_{B\in\mathcal{G}}\widehat B$, where $\widehat B$ is $B$ concentrically dilated by $5$.
>
> **Hint:** Greedy selection: at each step pick a ball of (nearly) maximal radius among those disjoint from all previously chosen; the factor $5$ exists so the triangle inequality forces any unchosen ball into a chosen dilate.
>
> **Why needed:** It is the combinatorial heart of the maximal inequality — converting an arbitrary cover by balls into a disjoint subcover whose dilates still cover, so volumes can be added without double-counting, at the price of a controllable dimensional constant $5^n$.
>
> > [!note]- Full proof
> > Greedily select disjoint balls, at each stage taking one of (nearly) maximal radius among those disjoint from all chosen so far. Any $B_0\in\mathcal{F}$ meets some chosen $B$ of radius $\ge\frac12\operatorname{rad}B_0$ (else $B_0$ would have been selectable); then $B_0\subseteq\widehat B$ by the triangle inequality. $\square$

> [!note]- Lemma 2: The maximal inequality
> **Statement:** For $f\in L^1(\mathbb{R}^n)$, $a>0$: $\lambda(\{f^*>a\})\le\frac{5^n}{a}\|f\|_1$.
>
> **Hint:** For each $x$ in the bad set pick a witness ball with average exceeding $a$, then apply Lemma 1 to thin the cover to a disjoint subfamily whose $5$-dilates still cover.
>
> **Why needed:** This weak-$(1,1)$ bound on the Hardy-Littlewood maximal function is the substitute for an honest pointwise bound on averages, and it is what makes the density-of-$C_c$ approximation work: small $L^1$-error implies small bad-set measure for the averages, so the discrepancy $|\text{avg}-f|$ vanishes a.e. in the limit.
>
> > [!note]- Full proof
> > For each $x$ with $f^*(x)>a$ pick a ball $B_x$ with $\frac{1}{\lambda(B_x)}\int_{B_x}|f|>a$, so $\lambda(B_x)<\frac1a\int_{B_x}|f|$. These balls cover $\{f^*>a\}$; by Lemma 1 extract disjoint $B_1,B_2,\dots$ with $5\times$-dilates covering. Then $\lambda(f^*>a)\le\sum_j\lambda(\widehat B_j)=5^n\sum_j\lambda(B_j)\le\frac{5^n}{a}\sum_j\int_{B_j}|f|\le\frac{5^n}{a}\|f\|_1$, the last step by disjointness. $\square$

> [!note]- Lemma 3: The continuous case
> **Statement:** For $g$ continuous, $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}g\to g(x)$ at every $x$.
>
> **Hint:** Direct from continuity: $|g(y)-g(x)|<\varepsilon$ for $y$ close to $x$ forces the average over $B(x,r)$ to lie within $\varepsilon$ of $g(x)$ once $r$ is small.
>
> **Why needed:** This handles the dense subclass $C_c\subseteq L^1$. The Lebesgue Differentiation Theorem for general $f\in L^1$ then follows by the density strategy: approximate $f$ by continuous $g$ in $L^1$, use Lemma 3 to control the average of $g$, and use Lemma 2 to control the remainder $f-g$.
>
> > [!note]- Full proof
> > Given $\varepsilon$, continuity gives $\delta$ with $|g(y)-g(x)|<\varepsilon$ for $|y-x|<\delta$; then for $r<\delta$, $|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}g-g(x)|\le\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|g-g(x)|<\varepsilon$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> WLOG $f\in L^1(\mathbb{R}^n)$. Given $\varepsilon>0$, density of $C_c$ in $L^1$ gives continuous $g$ with $\|f-g\|_1<\varepsilon^2$. For any $x$, $\limsup_r|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f-f(x)|\le\limsup_r\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-g|+\limsup_r|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}g-g(x)|+|g(x)-f(x)|\le(f-g)^*(x)+0+|f-g|(x)$ (Lemma 3 kills the middle term). So $A_\varepsilon:=\{\limsup_r|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f-f(x)|>2\varepsilon\}\subseteq\{(f-g)^*>\varepsilon\}\cup\{|f-g|>\varepsilon\}$, and by Lemma 2 and [[Ex - Markov's inequality|Markov]], $\lambda(A_\varepsilon)\le\frac{5^n}{\varepsilon}\|f-g\|_1+\frac1\varepsilon\|f-g\|_1<(5^n+1)\varepsilon$. As $\varepsilon$ is arbitrary, $\lambda(A_\varepsilon)=0$; $A=\bigcup_k A_{1/k}$ is null, and off $A$ the limit equals $f(x)$. The Lebesgue-point statement follows by applying this to $|f-c|$ over a countable dense set of constants $c$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The Lebesgue **density theorem** is the special case $f=\mathbf{1}_E$: a.e. point of a measurable set $E$ has *density $1$* ($\lambda(E\cap B(x,r))/\lambda(B(x,r))\to1$) — measurable sets have no "fuzzy" points, almost. The same dense-class-plus-maximal-inequality architecture proves the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]] (with [[Thm - Doob's Maximal Inequality|Doob's]] maximal inequality) and the pointwise ergodic theorem (with the ergodic maximal inequality).

---

# Bridges

- **[[Def - Hardy-Littlewood Maximal Function]]** — the maximal function and its weak inequality are the engine.
- **[[Thm - Doob's Maximal Inequality]]** *(Martingale Theory)* — the martingale twin of the maximal inequality, proving a.s. martingale convergence by the same template.
- **[[Thm - Radon-Nikodym Theorem]]** — for $\nu\ll\lambda$, the differentiation theorem shows $\mathrm{d}\nu/\mathrm{d}\lambda(x)=\lim_r\nu(B(x,r))/\lambda(B(x,r))$.
