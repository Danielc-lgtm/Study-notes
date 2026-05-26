---
type: theorem
subject: measure-theory
prereqs:
  - "Thm - Product Measure"
  - "Thm - Monotone Convergence Theorem"
  - "Thm - Approximation by Simple Functions"
  - "Def - The Integral"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X_i,\mathcal{A}_i,\mu_i)$, $i=1,2$, $\sigma$-finite; $\mu_1\otimes\mu_2$ the [[Thm - Product Measure|product measure]] on $X_1\times X_2$. $f:X_1\times X_2\to[-\infty,\infty]$ measurable for $\mathcal{A}_1\otimes\mathcal{A}_2$.

---

# Motivation

A double integral $\int_{X_1\times X_2}f\,d(\mu_1\otimes\mu_2)$ is, in principle, an integral over the whole product space — hard to evaluate directly. Fubini–Tonelli reduces it to an **iterated integral**: integrate out $x_2$ first (a one-variable integral, for each fixed $x_1$), then integrate the result over $x_1$ — or in the other order. It is the theorem that makes multiple integrals *computable*, and that licenses interchanging the order of integration. **Tonelli** is the non-negative version (no integrability hypothesis needed); **Fubini** is the signed version (needs absolute integrability). Together they are among the most-used theorems in all of analysis and probability.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is "$\mu_1,\mu_2$ are $\sigma$-finite and either $f\ge0$ or $f\in L^1(\mu_1\otimes\mu_2)$." Most working applications never present themselves in this packaged form — the input arrives as something else, and one has to recognise the Fubini-Tonelli setup underneath.

The first disguised source is any product of $\sigma$-finite measures, even when one factor is not Lebesgue. The combination "Lebesgue measure $\lambda$ on $\mathbb{R}$ times counting measure $\#$ on $\mathbb{N}$" is the bridge that turns a sum-of-integrals into a single integral against $\lambda\otimes\#$: $\sum_{n=1}^\infty\int_\mathbb{R} f_n(x)\,dx=\int_{\mathbb{R}\times\mathbb{N}}f(x,n)\,d(\lambda\otimes\#)$, with the discrete measure $\#$ trivially $\sigma$-finite. A concrete example: in proving the convergence of a Fourier series $\sum_n a_n e^{inx}$ in $L^1$, one wishes to interchange $\sum_n$ and $\int_{\mathbb{T}}$. Recognising the sum as an integral against counting measure recasts the problem as a Tonelli interchange on $\mathbb{T}\times\mathbb{N}$ — and the integrability hypothesis $\sum_n\int|a_n e^{inx}|\,dx<\infty$ becomes the obvious finiteness condition for Tonelli on $|f|$. Once one sees sums as integrals, Fubini-Tonelli is the universal swap.

The second disguised source is an integral over a set defined by inequalities. To evaluate $\int_A g(x)\,d\mu(x)$ where $A=\{x:h(x)>t\}$ depends on a parameter $t$, write the indicator $\mathbf{1}_A(x)=\mathbf{1}_{h(x)>t}$ as a function on the product space $X\times\mathbb{R}$ and integrate against $\mu\otimes\lambda$. The bridge: any integral over a measurably-defined region is a double integral via the indicator of the defining set in the product, and Tonelli makes the two iterated orders accessible. A concrete example: the layer-cake formula $\int_X g\,d\mu=\int_0^\infty\mu(g>t)\,dt$ is exactly the Fubini interchange applied to $\mathbf{1}_{\{(x,t):0<t<g(x)\}}$ on $X\times[0,\infty)$. The slicing-by-level-sets trick that runs through Marcinkiewicz interpolation, the proof of the Hardy-Littlewood maximal inequality, and every $L^p$-rearrangement argument is Tonelli on a region defined by inequalities.

The third disguised source is a convolution integral, presented as a single integral over $\mathbb{R}^n$. The expression $(f*g)(x)=\int f(x-y)g(y)\,dy$ looks like a one-dimensional input but is best understood as a double integral $\int\int f(x-y)g(y)\,dy\,dx$ on $\mathbb{R}^n\times\mathbb{R}^n$. The bridge: convolution is integration of a function on the product space, and almost every convolution identity is Fubini's interchange in disguise. A concrete example: the convolution Young's inequality $\|f*g\|_1\le\|f\|_1\|g\|_1$ for $f,g\in L^1$ is Tonelli applied to $|f(x-y)g(y)|$ on $\mathbb{R}^n\times\mathbb{R}^n$ (the iterated integral factors as $\|f\|_1\|g\|_1$ by translation invariance of $\lambda$), promoting integrability of $|fg|$ on the product to integrability of $f*g$ on $\mathbb{R}^n$.

**Targets (Output Amplification)**

The conclusion is "the double integral equals either iterated integral." Combined with other standard tools, this interchange unlocks identities and computations far beyond elementary multi-variable calculus.

The first amplification is Fubini combined with a careful choice of integration order to evaluate otherwise-intractable integrals. The technique: write the integrand as $f(x,y)=\int_{X_2}g(x,y,z)\,d\mu_2(z)$ for some auxiliary integrand, then swap to integrate over $z$ first. A classic example: $\int_0^\infty\frac{\sin x}{x}\,dx=\frac{\pi}{2}$, computed by writing $\frac{1}{x}=\int_0^\infty e^{-xy}\,dy$ for $x>0$ and applying Tonelli on $|e^{-xy}\sin x|$ over $(0,\infty)\times(0,\infty)$ — the swap converts the slowly-convergent oscillatory $\sin x/x$ integral into the easy double integral $\int_0^\infty\frac{1}{1+y^2}\,dy=\pi/2$. The amplification is non-obvious because the original integrand looks one-dimensional; introducing the parameter $y$ and recognising a product-space integral is the whole trick, and Fubini licenses the swap.

The second amplification is Fubini combined with Cavalieri's principle for computing measures by slicing. The product-measure identity $(\mu_1\otimes\mu_2)(E)=\int_{X_1}\mu_2(E_{x_1})\,d\mu_1$ — itself the indicator case of Tonelli — generalises to: for measurable $g\ge0$ on $X_1\times X_2$, $\int g\,d(\mu_1\otimes\mu_2)=\int_{X_1}\left(\int_{X_2}g(x_1,x_2)\,d\mu_2\right)d\mu_1$. The amplified result is Cavalieri's slicing formula for higher-dimensional volumes: $\lambda^n(E)=\int_\mathbb{R}\lambda^{n-1}(E_{x_n})\,dx_n$ for any measurable $E\subseteq\mathbb{R}^n$. This is how one computes the volume of the $n$-ball $|B^n|=\pi^{n/2}/\Gamma(n/2+1)$ inductively, and how one derives the surface-area formula for spheres by differentiating $\lambda^n(B^n_r)$ with respect to $r$ via the polar Fubini decomposition $dx=r^{n-1}\,dr\,d\sigma$.

The third amplification is Fubini in convolution theory, producing the foundational structural results of harmonic analysis. The associativity of convolution, $(f*g)*h=f*(g*h)$, is a Fubini interchange on $\mathbb{R}^n\times\mathbb{R}^n\times\mathbb{R}^n$. The Fourier-transform identity $\widehat{f*g}=\hat f\cdot\hat g$ requires Fubini to swap the integrals defining $\widehat{f*g}$. Young's convolution inequality $\|f*g\|_r\le\|f\|_p\|g\|_q$ for $1/p+1/q=1+1/r$ uses a Fubini-plus-Hölder argument on the product space. The amplified result: the entire algebra structure of $L^1(\mathbb{R}^n)$ as a Banach algebra under convolution is downstream of Fubini-Tonelli, and the corresponding result for groups other than $\mathbb{R}^n$ — via Haar measure on locally compact groups — requires precisely the $\sigma$-finiteness condition that Fubini-Tonelli demands.

---

# Statement

Let $(X_i,\mathcal{A}_i,\mu_i)$ be $\sigma$-finite and $f:X_1\times X_2\to[-\infty,\infty]$ be $\mathcal{A}_1\otimes\mathcal{A}_2$-measurable.

**(Tonelli)** If $f\ge0$, then the slice functions $x_2\mapsto f(x_1,x_2)$ and $x_1\mapsto f(x_1,x_2)$ are measurable, the iterated integrals $x_1\mapsto\int f(x_1,x_2)\,d\mu_2$ and $x_2\mapsto\int f(x_1,x_2)\,d\mu_1$ are measurable, and
$$\int_{X_1\times X_2}f\,d(\mu_1\otimes\mu_2)=\int_{X_1}\!\Big(\int_{X_2}f\,d\mu_2\Big)d\mu_1=\int_{X_2}\!\Big(\int_{X_1}f\,d\mu_1\Big)d\mu_2,$$
all three values equal in $[0,\infty]$.

**(Fubini)** If $f\in L^1(\mu_1\otimes\mu_2)$, then for $\mu_1$-a.e. $x_1$ the slice $f(x_1,\cdot)\in L^1(\mu_2)$, the (a.e.-defined) iterated integral is in $L^1(\mu_1)$, and the same chain of equalities holds.

---

# Why Is It True

Tonelli is the [[Thm - Approximation by Simple Functions|standard machine]] turned once.

*Indicators.* For $f=\mathbf{1}_E$, $\int_{X_2}\mathbf{1}_E(x_1,x_2)\,d\mu_2=\mu_2(E_{x_1})$, and the [[Thm - Product Measure|product measure theorem]] *is exactly* the statement $\int_{X_1}\mu_2(E_{x_1})\,d\mu_1=(\mu_1\otimes\mu_2)(E)$. So Tonelli holds for indicators *by the definition of the product measure*.

*Simple functions.* By [[Thm - Properties of the Integral|linearity]] of all three integrals, Tonelli extends to non-negative simple functions.

*General $f\ge0$.* Take simple $s_n\uparrow f$ ([[Thm - Approximation by Simple Functions]]). Each slice $s_n(x_1,\cdot)\uparrow f(x_1,\cdot)$, so by [[Thm - Monotone Convergence Theorem|MCT]] (in $x_2$) $\int s_n(x_1,\cdot)\,d\mu_2\uparrow\int f(x_1,\cdot)\,d\mu_2$; this limit is measurable in $x_1$. Apply MCT *again* (in $x_1$, and in the product space): all three integrals of $s_n$ converge to the corresponding integrals of $f$, and equality is preserved through the limit. **Tonelli is the product-measure identity for indicators, propagated to all $f\ge0$ by the standard machine, with MCT doing every limit interchange** — which is why Tonelli needs *no integrability hypothesis*: MCT never does.

*Fubini.* Split $f=f^+-f^-$. Apply Tonelli to $f^+$ and $f^-$ separately. The hypothesis $f\in L^1(\mu_1\otimes\mu_2)$ — equivalently, by Tonelli applied to $|f|$, the finiteness of the iterated integral of $|f|$ — guarantees $\int f^\pm\,d(\mu_1\otimes\mu_2)<\infty$, so the subtraction $\iint f^+-\iint f^-$ involves no "$\infty-\infty$" and the iterated integrals of $f^\pm$ are finite for $\mu_1$-a.e. $x_1$. Subtract.

---

# What Makes This Hard

Tonelli itself is routine *once* one accepts that "Tonelli for indicators $=$ the product measure theorem" — that recognition is the keystone, and it is why the [[Thm - Product Measure|product measure]] had to be built via the slice formula first. The genuine pitfall is **Fubini without integrability**: the iterated integrals can both exist and *disagree* if $f$ is not absolutely integrable (the classic $\sum_n\sum_m(\mathbf{1}_{n=m}-\mathbf{1}_{n=m+1})$ on $\mathbb{N}\times\mathbb{N}$ gives $0\neq1$). The discipline: **always run Tonelli on $|f|$ first**; only if that iterated integral is finite may one apply Fubini to $f$.

---

# Rederivation Scaffold

**High-level strategy.** Tonelli: standard machine — indicators (= product measure theorem), simple (linearity), $f\ge0$ (MCT twice). Fubini: split $f=f^+-f^-$, Tonelli on each, subtract using $L^1$.

**Subgoal decomposition.**

1. **Tonelli for indicators.** $\iint\mathbf{1}_E$ in any order $=(\mu_1\otimes\mu_2)(E)$ — restate the [[Thm - Product Measure|product measure theorem]].
2. **Tonelli for simple $f\ge0$.** Linearity of the three integrals.
3. **Tonelli for $f\ge0$.** $s_n\uparrow f$; MCT in $x_2$, then in $x_1$ and in the product — equality survives.
4. **Fubini.** $f=f^+-f^-$; Tonelli on $f^\pm$; $f\in L^1\Rightarrow\iint f^\pm<\infty$; subtract; slices in $L^1$ a.e.

---

# Lemma Decomposition

> [!note]- Lemma 1: Tonelli for non-negative functions
> **Statement:** For $f\ge0$ measurable, the three integrals coincide in $[0,\infty]$.
>
> **Hint:** Standard machine: verify it for indicators (this is the product measure identity), extend by linearity to non-negative simple functions, then climb to general $f\ge0$ by MCT applied separately in each variable.
>
> **Why needed:** Tonelli is the unconditional version — it always holds for $f\ge0$, even when the integrals are $+\infty$. Fubini for signed integrable $f$ then follows by splitting $f=f^+-f^-$ and applying Tonelli to each piece, with no $\infty-\infty$ obstruction.
>
> > [!note]- Full proof
> > For $f=\mathbf{1}_E$ this is the [[Thm - Product Measure|product measure]] identity $(\mu_1\otimes\mu_2)(E)=\int\mu_2(E_{x_1})\,d\mu_1=\int\mu_1(E_{x_2})\,d\mu_2$. Linearity extends it to non-negative simple functions. For general $f\ge0$, take simple $s_n\uparrow f$; the slices $s_n(x_1,\cdot)\uparrow f(x_1,\cdot)$, so [[Thm - Monotone Convergence Theorem|MCT]] gives $\int s_n(x_1,\cdot)d\mu_2\uparrow\int f(x_1,\cdot)d\mu_2$ (measurable in $x_1$ as a limit of measurables); MCT again in $d\mu_1$ and in $d(\mu_1\otimes\mu_2)$ carries the three-way equality to the limit. $\square$

> [!note]- Lemma 2: Fubini from Tonelli
> **Statement:** $f\in L^1(\mu_1\otimes\mu_2)\Rightarrow$ the iterated integrals exist a.e., are finite, and equal $\int f\,d(\mu_1\otimes\mu_2)$.
>
> **Hint:** First Tonelli on $|f|$ certifies that the slice $f(x_1,\cdot)\in L^1(\mu_2)$ for a.e. $x_1$; then split $f=f^+-f^-$ and apply Tonelli to each non-negative piece — since both have finite integral, subtraction is legal.
>
> **Why needed:** This is the signed-and-integrable version that practitioners actually use — swapping the order of integration for a real- or complex-valued $L^1$ function, justified once Tonelli has provided the $\sigma$-finite-style finiteness control.
>
> > [!note]- Full proof
> > By Lemma 1 applied to $|f|\ge0$, $\iint|f|=\int|f|\,d(\mu_1\otimes\mu_2)<\infty$, so the iterated integral of $|f|$ is finite — hence $\int|f(x_1,\cdot)|\,d\mu_2<\infty$ for $\mu_1$-a.e. $x_1$, i.e. $f(x_1,\cdot)\in L^1(\mu_2)$ a.e. Apply Lemma 1 to $f^+$ and $f^-$ (both $\ge0$, both with finite integral $\le\int|f|$). Subtracting the two finite iterated integrals (no $\infty-\infty$) gives $\iint f=\int f\,d(\mu_1\otimes\mu_2)$, in either order. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 is Tonelli; Lemma 2 is Fubini. Measurability of the slice and iterated-integral functions is part of Lemma 1's induction (limits of measurable functions). $\blacksquare$

---

# Cross-Field Exercise Suggestions

Fubini–Tonelli proves the **layer-cake formula** $\int g\,d\mu=\int_0^\infty\mu(g>t)\,dt$ (apply Tonelli to $\mathbf{1}_{\{(x,t):t<g(x)\}}$ on $X\times[0,\infty)$) — the bridge between integrating a function and integrating its tail. In probability it gives $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$ for independent $X,Y$ (the joint law is a product, integrate the product against it), and the [[Thm - Doob's Maximal Inequality|Lᵖ maximal inequality]] uses Fubini to integrate $\int_0^\infty pt^{p-1}\mathbb{P}(X^*>t)\,dt$.

---

# Bridges

- **[[Thm - Product Measure]]** — supplies the measure; Tonelli-for-indicators *is* the product-measure theorem.
- **[[Thm - Monotone Convergence Theorem]]** — every limit interchange in Tonelli is an MCT; this is why Tonelli is hypothesis-free.
- **[[Def - Independence]]** *(Advanced Probability)* — Fubini against a product law is the computational engine for independent random variables.
