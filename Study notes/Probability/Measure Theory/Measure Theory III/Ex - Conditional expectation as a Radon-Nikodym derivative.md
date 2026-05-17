---
type: exercise
subject: measure-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Radon-Nikodym Theorem"
  - "Def - Absolute Continuity and Density"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space, $\mathcal{G}\subseteq\mathcal{F}$ a sub-$\sigma$-algebra, and $X\ge0$ an integrable random variable.

**(a)** Show $\nu(A)=\int_A X\,d\mathbb{P}$, restricted to $A\in\mathcal{G}$, defines a finite measure on $(\Omega,\mathcal{G})$ with $\nu\ll\mathbb{P}|_\mathcal{G}$.

**(b)** Apply [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] (on $(\Omega,\mathcal{G})$) to obtain a $\mathcal{G}$-measurable $Y\ge0$ with $\int_A Y\,d\mathbb{P}=\int_A X\,d\mathbb{P}$ for all $A\in\mathcal{G}$.

**(c)** Conclude that $Y$ is *the* [[Def - Conditional Expectation|conditional expectation]] $\mathbb{E}[X\mid\mathcal{G}]$ — it exists and is a.s. unique. Extend to integrable $X$ of either sign.

**Recall:**

[[Thm - Radon-Nikodym Theorem|Radon–Nikodym]]: $\nu\ll\mu$ ($\sigma$-finite) $\Rightarrow\nu=f\mu$ for a $\mu$-a.e.-unique density $f\ge0$.

---

# Convergent Strategy

**Problem class:** *constructing* an object (conditional expectation) by recognising it as a Radon–Nikodym derivative.

**Assumption pattern:** the defining property of $\mathbb{E}[X\mid\mathcal{G}]$ — "$\mathcal{G}$-measurable, and $\int_A Y\,d\mathbb{P}=\int_A X\,d\mathbb{P}$ for $A\in\mathcal{G}$" — is *exactly* the statement "$Y$ is the density of $\nu(\cdot)=\int_\cdot X\,d\mathbb{P}$ with respect to $\mathbb{P}$, on the $\sigma$-algebra $\mathcal{G}$."

**Theorem routing:** verify $\nu\ll\mathbb{P}|_\mathcal{G}$; Radon–Nikodym yields the density $Y$; uniqueness of the density is a.s.-uniqueness of $\mathbb{E}[X\mid\mathcal{G}]$.

**Key decision point:** working on the *sub*-$\sigma$-algebra $\mathcal{G}$ — that is what forces $Y$ to be $\mathcal{G}$-measurable.

---

# Legal Operations Used

1. **Restrict a measure to a sub-$\sigma$-algebra.**
2. **Verify absolute continuity** via "$\mathbb{P}(A)=0\Rightarrow\nu(A)=0$."
3. **Radon–Nikodym** to produce the density; **uniqueness** of the density.

---

# Hints

> [!note]- Hint 1
> $\nu(A)=\int_A X\,d\mathbb{P}$ is a measure ($\sigma$-additivity is [[Thm - Monotone Convergence Theorem|MCT]]); finite since $\nu(\Omega)=\mathbb{E}[X]<\infty$.

> [!note]- Hint 2
> If $A\in\mathcal{G}$ has $\mathbb{P}(A)=0$, then $X\mathbf{1}_A=0$ a.s., so $\nu(A)=0$. Hence $\nu\ll\mathbb{P}|_\mathcal{G}$.

> [!note]- Hint 3
> Radon–Nikodym on $(\Omega,\mathcal{G},\mathbb{P}|_\mathcal{G})$ gives a $\mathcal{G}$-measurable density $Y$. Its defining equation $\int_A Y\,d\mathbb{P}=\nu(A)=\int_A X\,d\mathbb{P}$ is the characterisation of $\mathbb{E}[X\mid\mathcal{G}]$.

---

# Solution

**Step 1 — (a).** Define $\nu:\mathcal{G}\to[0,\infty)$ by $\nu(A)=\int_A X\,d\mathbb{P}$. It is a measure: $\nu(\emptyset)=0$, and for disjoint $A_n\in\mathcal{G}$, $\nu(\bigsqcup A_n)=\int X\mathbf{1}_{\bigsqcup A_n}\,d\mathbb{P}=\sum_n\int X\mathbf{1}_{A_n}\,d\mathbb{P}$ by [[Thm - Monotone Convergence Theorem|MCT]] applied to partial sums. It is finite: $\nu(\Omega)=\mathbb{E}[X]<\infty$. Absolute continuity: if $A\in\mathcal{G}$ with $\mathbb{P}(A)=0$, then $X\mathbf{1}_A=0$ $\mathbb{P}$-a.s., so $\nu(A)=\int X\mathbf{1}_A\,d\mathbb{P}=0$. Hence $\nu\ll\mathbb{P}|_\mathcal{G}$.

**Step 2 — (b).** Both $\nu$ and $\mathbb{P}|_\mathcal{G}$ are finite measures on $(\Omega,\mathcal{G})$, hence $\sigma$-finite, and $\nu\ll\mathbb{P}|_\mathcal{G}$. By the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]] *on the measurable space $(\Omega,\mathcal{G})$*, there is a $\mathcal{G}$-measurable $Y\ge0$, unique up to $\mathbb{P}$-a.s. equality, with
$$\int_A Y\,d\mathbb{P}=\nu(A)=\int_A X\,d\mathbb{P}\qquad\text{for every }A\in\mathcal{G}.$$
Crucially $Y$ is **$\mathcal{G}$-measurable** — because Radon–Nikodym was applied on $\mathcal{G}$, the density it produces is $\mathcal{G}$-measurable.

**Step 3 — (c).** The two properties of $Y$ — *(i) $\mathcal{G}$-measurable*, *(ii) $\int_A Y\,d\mathbb{P}=\int_A X\,d\mathbb{P}$ for all $A\in\mathcal{G}$* — are *exactly* the defining characterisation of the [[Def - Conditional Expectation|conditional expectation]] $\mathbb{E}[X\mid\mathcal{G}]$. So $Y=\mathbb{E}[X\mid\mathcal{G}]$ exists, and the a.s.-uniqueness of the Radon–Nikodym density *is* the a.s.-uniqueness of conditional expectation. For integrable $X$ of either sign, apply the construction to $X^+$ and $X^-$ separately and set $\mathbb{E}[X\mid\mathcal{G}]=\mathbb{E}[X^+\mid\mathcal{G}]-\mathbb{E}[X^-\mid\mathcal{G}]$.

> [!note]- Complete formal solution
> (a) $\nu(A)=\int_A X\,d\mathbb{P}$ is a finite measure on $\mathcal{G}$ ($\sigma$-additivity by MCT, $\nu(\Omega)=\mathbb{E}X<\infty$); $\mathbb{P}(A)=0\Rightarrow X\mathbf{1}_A=0$ a.s. $\Rightarrow\nu(A)=0$, so $\nu\ll\mathbb{P}|_\mathcal{G}$. (b) Radon–Nikodym on $(\Omega,\mathcal{G})$ yields a $\mathcal{G}$-measurable density $Y\ge0$ with $\int_A Y\,d\mathbb{P}=\int_A X\,d\mathbb{P}$, $A\in\mathcal{G}$, unique a.s. (c) $(i)$–$(ii)$ are the definition of $\mathbb{E}[X\mid\mathcal{G}]$; density-uniqueness is a.s.-uniqueness; split $X=X^+-X^-$ for the general case. $\blacksquare$

---

# Key Takeaways

**Conditional expectation *is* a Radon–Nikodym derivative — its existence and a.s.-uniqueness are not separate facts but a direct reading of the Radon–Nikodym theorem applied on the sub-$\sigma$-algebra.** The defining property of $\mathbb{E}[X\mid\mathcal{G}]$ ("$\mathcal{G}$-measurable, same integral as $X$ over every $\mathcal{G}$-set") *is* the statement "density of $\int_\cdot X\,d\mathbb{P}$ with respect to $\mathbb{P}$, on $\mathcal{G}$." Applying Radon–Nikodym *on $\mathcal{G}$* — not on $\mathcal{F}$ — is the decisive move: it is what forces the output to be $\mathcal{G}$-measurable, i.e. to "depend only on the information in $\mathcal{G}$."

**This is one of the two canonical constructions of conditional expectation; the other is [[Ex - The Cauchy-Schwarz inequality and L2 geometry|$L^2$ orthogonal projection]].** Radon–Nikodym handles all integrable $X$ directly (no $L^2$ assumption) and exposes conditional expectation as a *change-of-density* object; the projection construction is geometric and works first for $X\in L^2$. The two agree where both apply. Either way, conditional expectation inherits its theory — linearity, monotonicity, the tower property — from the measure-theoretic machinery, and the abstract construction is what makes $\mathbb{E}[X\mid\mathcal{G}]$ well-defined even when the naive "condition on an event of probability zero" fails.
