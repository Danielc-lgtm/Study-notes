---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Lebesgue Differentiation Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

A point $x$ is a **Lebesgue point** of $f\in L^1_{loc}(\mathbb{R}^n)$ if $\displaystyle\lim_{r\downarrow0}\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f(y)-f(x)|\,dy=0$.

**(a)** Show almost every $x$ is a Lebesgue point of $f$.

**(b)** Show that at a Lebesgue point, $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f\to f(x)$ — so the Lebesgue-point property is *stronger* than mere convergence of averages.

**(c)** Exhibit a point where the averages converge but which is *not* a Lebesgue point, showing (b) is a strict implication.

**Recall:**

![[Thm - Lebesgue Differentiation Theorem#Formal Statement]]

---

# Convergent Strategy

**Problem class:** strengthening "averages converge" to "averages of the *deviation* converge" — and locating the gap.

**Assumption pattern:** the [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]] applies to $|f-c|$ for any constant $c$; running it over a *countable dense set* of constants $c$ and discarding the (countably many) null exceptional sets yields the Lebesgue-point property for a.e. $x$.

**Theorem routing:** apply the theorem to $g_c=|f-c|$ for $c\in\mathbb{Q}$; intersect the full-measure sets; approximate $f(x)$ by a nearby rational.

---

# Legal Operations Used

1. **Apply the differentiation theorem to a countable family** $|f-c|$, $c\in\mathbb{Q}$.
2. **Countable intersection of full-measure sets** is full-measure.
3. **Triangle inequality** to swap the constant $c$ for $f(x)$.

---

# Hints

> [!note]- Hint 1
> For each rational $c$, $|f-c|\in L^1_{loc}$, so by the differentiation theorem $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-c|\to|f(x)-c|$ for a.e. $x$.

> [!note]- Hint 2
> Intersect over $c\in\mathbb{Q}$ — countably many null exceptional sets union to a null set.

> [!note]- Hint 3
> At a good $x$, given $\varepsilon$ pick rational $c$ with $|f(x)-c|<\varepsilon$; then $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-f(x)|\le\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-c|+|c-f(x)|$.

---

# Solution

**Step 1 — (a).** For each $c\in\mathbb{Q}$, the function $|f-c|$ is locally integrable, so by the [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation theorem]],
$$\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f(y)-c|\,dy\xrightarrow[r\downarrow0]{}|f(x)-c|\quad\text{for }x\notin N_c,\ \lambda(N_c)=0.$$
Let $N=\bigcup_{c\in\mathbb{Q}}N_c$ — a countable union of null sets, hence null. Fix $x\notin N$ and $\varepsilon>0$; choose $c\in\mathbb{Q}$ with $|f(x)-c|<\varepsilon$. Then
$$\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f(y)-f(x)|\,dy\le\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f(y)-c|\,dy+|c-f(x)|.$$
The first term $\to|f(x)-c|<\varepsilon$ as $r\to0$ (since $x\notin N_c$), so $\limsup_r\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-f(x)|\le|f(x)-c|+\varepsilon<2\varepsilon$. As $\varepsilon$ is arbitrary, the limit is $0$: $x$ is a Lebesgue point. So a.e. $x$ is a Lebesgue point.

**Step 2 — (b).** At a Lebesgue point, by the triangle inequality for integrals,
$$\Big|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f-f(x)\Big|=\Big|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}(f-f(x))\Big|\le\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-f(x)|\to0.$$
So the averages of $f$ converge to $f(x)$. The Lebesgue-point property is strictly stronger: it controls the average of the *absolute deviation*, ruling out cancellation, whereas mere convergence of $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f$ allows large positive and negative excursions to cancel.

**Step 3 — (c).** Take $n=1$, $f=\mathbf{1}_{(0,\infty)}-\mathbf{1}_{(-\infty,0)}$ (the sign function), $x=0$. By symmetry $\frac{1}{\lambda(B(0,r))}\int_{B(0,r)}f=\frac{1}{\lambda((-r,r))}\int_{(-r,r)}f=0\to0$ — the averages converge (to $0$). But $f(0)$ aside, $\frac{1}{\lambda((-r,r))}\int_{(-r,r)}|f(y)-f(0)|$: with $f(0)=0$ say, $\frac{1}{\lambda((-r,r))}\int_{(-r,r)}|f|=\frac{1}{\lambda((-r,r))}\int_{(-r,r)}1=1\not\to0$. So $0$ is *not* a Lebesgue point, yet the averages converge — the positive and negative halves cancel in $\frac{1}{\lambda(B(0,r))}\int_{B(0,r)}f$ but not in $\frac{1}{\lambda(B(0,r))}\int_{B(0,r)}|f|$.

> [!note]- Complete formal solution
> (a) Differentiation theorem on $|f-c|$ for each $c\in\mathbb{Q}$ gives full-measure $N_c^c$; off $N=\bigcup_c N_c$ (null), approximate $f(x)$ by rational $c$ and use the triangle inequality to get $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-f(x)|\to0$. (b) $\big|\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f-f(x)\big|\le\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-f(x)|\to0$. (c) The sign function at $0$: $\frac{1}{\lambda((-r,r))}\int_{(-r,r)}f=0\to0$ but $\frac{1}{\lambda((-r,r))}\int_{(-r,r)}|f-f(0)|=1\not\to0$ — averages converge, not a Lebesgue point. $\blacksquare$

---

# Key Takeaways

**The Lebesgue differentiation theorem upgrades, for free, to the *Lebesgue-point* statement — controlling the average *deviation* $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-f(x)|$, not just the average $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f$ — by running it over a countable dense family of constants.** The technique "apply an a.e.-theorem to a countable family and intersect the full-measure sets" is a standard amplifier: countably many null exceptional sets cost nothing. The Lebesgue-point property is the genuinely useful form — it says $f$ is, near a.e. point, *approximately constant in mean*, with no cancellation hiding oscillation.

**"Averages converge" is strictly weaker than "Lebesgue point," and the gap is *cancellation*.** $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}f$ can converge because positive and negative deviations cancel — as for the sign function at the origin — while $\frac{1}{\lambda(B(x,r))}\int_{B(x,r)}|f-f(x)|$ stays large. The Lebesgue-point property forbids this. This distinction matters wherever one needs $f$ to be genuinely well-approximated by its value (convergence of [[Def - Conditional Expectation|conditional expectations]], pointwise convergence of Fourier series, mollifier approximation): the relevant hypothesis is always "Lebesgue point," not "averages converge."
