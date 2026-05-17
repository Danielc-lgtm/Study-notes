---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Hardy-Littlewood Maximal Function"
  - "Def - The Integral"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $f^*$ be the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal function]] of $f\in L^1(\mathbb{R}^n)$.

**(a)** For $f=\mathbf{1}_{B(0,1)}$ show $f^*(x)\ge c\,|x|^{-n}$ for $|x|>1$, and conclude $f^*\notin L^1(\mathbb{R}^n)$ unless $f=0$.

**(b)** Explain why this forces the [[Def - Hardy-Littlewood Maximal Function|maximal inequality]] to be a *weak-type* bound $\lambda(f^*>a)\le\frac{C}{a}\|f\|_1$ rather than a strong $L^1\to L^1$ bound.

**(c)** Verify the maximal inequality is nonetheless *sharp enough* for the [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]] — a weak bound on $(f-g)^*$ is all that the exceptional-set argument needs.

**Recall:**

$f^*(x)=\sup_{r>0}\fint_{B(x,r)}|f|$; the maximal inequality $\lambda(\{f^*>a\})\le\frac{5^n}{a}\|f\|_1$.

---

# Convergent Strategy

**Problem class:** showing an operator is *not* bounded on $L^1$, and why the weaker bound suffices anyway.

**Assumption pattern:** $f^*$ averages $|f|$ over balls; for $|x|$ large, the ball $B(x,|x|+1)$ still catches all the mass of $f$, but its volume grows like $|x|^n$ — so $f^*(x)$ decays only like $|x|^{-n}$, the borderline non-integrable rate.

**Theorem routing:** lower-bound $f^*(x)$ by the average over one well-chosen large ball; integrate the lower bound.

---

# Legal Operations Used

1. **Lower-bound a supremum** by one term.
2. **Compare to the non-integrable $|x|^{-n}$.**

---

# Hints

> [!note]- Hint 1
> For $|x|>1$, the ball $B(x,|x|+1)$ contains $B(0,1)$, so $\int_{B(x,|x|+1)}|f|=\int_{B(0,1)}|f|=:c_1>0$.

> [!note]- Hint 2
> $f^*(x)\ge\fint_{B(x,|x|+1)}|f|=\frac{c_1}{\lambda(B(x,|x|+1))}\ge\frac{c_1}{C(|x|+1)^n}\ge c\,|x|^{-n}$.

> [!note]- Hint 3
> $\int_{|x|>1}|x|^{-n}\,dx=\infty$ (in polar coordinates, $\int_1^\infty r^{-n}r^{n-1}\,dr=\int_1^\infty r^{-1}\,dr$).

---

# Solution

**Step 1 — (a).** Let $f\in L^1$, $f\neq0$, and pick $r_0$ with $c_1:=\int_{B(0,r_0)}|f|>0$. For $|x|>r_0$, the ball $B(x,|x|+r_0)$ contains $B(0,r_0)$ (any $y$ with $|y|<r_0$ has $|y-x|\le|y|+|x|<|x|+r_0$). Hence
$$f^*(x)\ge\fint_{B(x,|x|+r_0)}|f|=\frac{1}{\lambda(B(x,|x|+r_0))}\int_{B(x,|x|+r_0)}|f|\ge\frac{c_1}{\omega_n(|x|+r_0)^n}\ge c\,|x|^{-n}$$
for $|x|$ large, with $c>0$ and $\omega_n=\lambda(B(0,1))$. Now $\int_{|x|>r_0}|x|^{-n}\,dx=\omega_n'\int_{r_0}^\infty r^{-n}\cdot r^{n-1}\,dr=\omega_n'\int_{r_0}^\infty\frac{dr}{r}=\infty$. So $\int f^*\ge c\int_{|x|>r_0}|x|^{-n}\,dx=\infty$ — $f^*\notin L^1$.

**Step 2 — (b).** A *strong* $L^1\to L^1$ bound would assert $\|f^*\|_1\le C\|f\|_1$. Part (a) shows $\|f^*\|_1=\infty$ for every $f\neq0$ — so no strong bound can hold. The best possible is the **weak-type $(1,1)$** bound $\lambda(\{f^*>a\})\le\frac{C}{a}\|f\|_1$, which controls the *level sets* of $f^*$ without controlling its integral. The decay $f^*\sim|x|^{-n}$ is *exactly borderline*: $|x|^{-n}$ just fails to be integrable, and correspondingly $\lambda(\{|x|^{-n}>a\})\sim a^{-1}$ — the level sets shrink at precisely the rate the weak bound permits.

**Step 3 — (c).** The [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]]'s exceptional-set argument needs only to make $\lambda(\{(f-g)^*>\varepsilon\})$ small for a good approximation $g$. The weak bound delivers exactly that: $\lambda(\{(f-g)^*>\varepsilon\})\le\frac{5^n}{\varepsilon}\|f-g\|_1$, and choosing $\|f-g\|_1$ small (density of continuous functions) makes the right side small. A *strong* bound is never needed — and, by (a), never available. The weak bound is the sharp tool, sufficient and necessary.

> [!note]- Complete formal solution
> (a) For $|x|>r_0$, $B(x,|x|+r_0)\supseteq B(0,r_0)$, so $f^*(x)\ge c_1/\lambda(B(x,|x|+r_0))\ge c|x|^{-n}$; $\int_{|x|>r_0}|x|^{-n}dx=\infty$ (polar), so $f^*\notin L^1$. (b) Hence no $\|f^*\|_1\le C\|f\|_1$; the best is the weak bound on $\lambda(\{f^*>a\})$, matching the borderline $|x|^{-n}$ decay. (c) The differentiation theorem only needs $\lambda(\{(f-g)^*>\varepsilon\})$ small, which the weak bound supplies via $\|f-g\|_1$ small. $\blacksquare$

---

# Key Takeaways

**The maximal function is *not* bounded on $L^1$ — it decays only like $|x|^{-n}$, the exact borderline of non-integrability — so the maximal inequality is necessarily a *weak-type* bound, on level sets, not on the norm.** This is a structural feature of harmonic analysis: the natural operators (maximal functions, the Hilbert transform) fail strong $L^1$ bounds and one settles for weak-type $(1,1)$. The weak bound is not a defect; it is the truth, and recognising "this operator can only be weakly bounded at $p=1$" is the start of the Calderón–Zygmund/interpolation machinery (weak $(1,1)$ + bounded on $L^\infty$ interpolates to strong $L^p$ for $1<p<\infty$).

**A weak bound is exactly what an a.e.-convergence proof consumes — it bounds the *exceptional set*, never needing to bound a norm.** The [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]] (and the [[Thm - Almost Sure Martingale Convergence|martingale]] and ergodic theorems) all run the same template: dense class + maximal inequality, where the maximal inequality squeezes the bad set. None needs the strong bound, which is fortunate, since none is available. The lesson: match the tool to the task — a.e. statements want weak (level-set) bounds, norm statements want strong ones.
