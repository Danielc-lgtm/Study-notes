---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Lebesgue Differentiation Theorem"
  - "Def - Lebesgue Measure"
tags: [analysis, measure-theory]
---

# Problem Statement

For a Lebesgue-measurable $E\subseteq\mathbb{R}^n$ and $x\in\mathbb{R}^n$, define the **density of $E$ at $x$**:
$$d_E(x)=\lim_{r\downarrow0}\frac{\lambda(E\cap B(x,r))}{\lambda(B(x,r))},$$
when the limit exists.

**(a)** Prove the **Lebesgue density theorem**: $d_E(x)=1$ for a.e. $x\in E$ and $d_E(x)=0$ for a.e. $x\notin E$.

**(b)** Conclude there is no measurable set $E\subseteq\mathbb{R}$ with $0<\lambda(E\cap I)<\lambda(I)$ for *every* interval $I$ — no set is "uniformly half-dense."

**Recall:**

![[Thm - Lebesgue Differentiation Theorem#Formal Statement]]

---

# Convergent Strategy

**Problem class:** an a.e.-statement about local averages — a direct corollary of the [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]] applied to an indicator.

**Assumption pattern:** $d_E(x)$ is precisely the average of $f=\mathbf{1}_E$ over $B(x,r)$; the differentiation theorem says this average $\to f(x)=\mathbf{1}_E(x)$ a.e.

**Theorem routing:** $\mathbf{1}_E\in L^1_{loc}$; differentiation theorem $\Rightarrow\fint_{B(x,r)}\mathbf{1}_E\to\mathbf{1}_E(x)$ a.e., which is $1$ on $E$, $0$ off $E$.

---

# Legal Operations Used

1. **Apply the differentiation theorem to $\mathbf{1}_E$.**
2. **Contradiction via density** for (b).

---

# Hints

> [!note]- Hint 1
> $\dfrac{\lambda(E\cap B(x,r))}{\lambda(B(x,r))}=\fint_{B(x,r)}\mathbf{1}_E$. What does the differentiation theorem say about this average?

> [!note]- Hint 2
> The theorem gives $\fint_{B(x,r)}\mathbf{1}_E\to\mathbf{1}_E(x)$ a.e. — and $\mathbf{1}_E(x)$ is $1$ on $E$, $0$ off $E$.

> [!note]- Hint 3
> For (b): a "half-dense" $E$ would have $d_E(x)\le1/2$ everywhere — but a.e. point of $E$ has density $1$.

---

# Solution

**Step 1 — (a).** $\mathbf{1}_E$ is locally integrable ($|\mathbf{1}_E|\le1$). The [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation theorem]] gives, for a.e. $x$,
$$d_E(x)=\lim_{r\downarrow0}\fint_{B(x,r)}\mathbf{1}_E\,d\lambda=\mathbf{1}_E(x).$$
And $\mathbf{1}_E(x)=1$ for $x\in E$, $=0$ for $x\notin E$. So $d_E=1$ a.e. on $E$ and $d_E=0$ a.e. off $E$ — almost every point of a measurable set is a point of *full density*, and almost every point outside is of *zero density*.

**Step 2 — (b).** Suppose $E$ is measurable with $0<\lambda(E\cap I)<\lambda(I)$ for every interval $I$. Then for every $x$ and every $r$, $0<\fint_{B(x,r)}\mathbf{1}_E<1$, so whenever $d_E(x)$ exists it lies in $[0,1]$ and — by the strict inequalities, taking $r\to0$ — one might hope to force $d_E(x)\notin\{0,1\}$. By (a), however, $d_E(x)\in\{0,1\}$ for a.e. $x$. So a.e. $x$ has $d_E(x)\in\{0,1\}$, and $E$ has positive measure, so a.e. point of $E$ has density exactly $1$. Pick such an $x\in E$: then $\fint_{B(x,r)}\mathbf{1}_E\to1$, contradicting $\fint_{B(x,r)}\mathbf{1}_E<1$ being bounded away from $1$? — more carefully: $d_E(x)=1$ means the averages *approach* $1$, which is compatible with each being $<1$; the genuine contradiction is with a *uniform* gap. If $\lambda(E\cap I)\le(1-\delta)\lambda(I)$ for all $I$ and a fixed $\delta>0$, then $d_E(x)\le1-\delta<1$ everywhere, contradicting (a). So no set is *uniformly bounded away from full density* on all intervals — a measurable set is, near a.e. of its points, *almost all* of every small ball.

> [!note]- Complete formal solution
> (a) $d_E(x)=\lim_r\fint_{B(x,r)}\mathbf{1}_E$; the differentiation theorem gives this limit $=\mathbf{1}_E(x)$ a.e., i.e. $1$ on $E$, $0$ off $E$. (b) If $\lambda(E\cap I)\le(1-\delta)\lambda(I)$ for all intervals $I$, then every average $\fint_{B(x,r)}\mathbf{1}_E\le1-\delta$, so $d_E\le1-\delta<1$ everywhere — contradicting that a.e. point of the positive-measure set $E$ has density $1$. $\blacksquare$

---

# Key Takeaways

**A measurable set has no "fuzzy" points: almost every point is either of full density ($1$) or zero density ($0$).** This is the Lebesgue differentiation theorem read for an indicator function — and it is a striking rigidity statement. Intuitively a measurable set might be "$50\%$ dense everywhere" (like a thickened rational lattice), but the density theorem forbids it: density is a.e. *binary*. The boundary, where $0<d_E<1$, is a null set.

**The differentiation theorem applied to $\mathbf{1}_E$ is the prototype "apply a function-level theorem to an indicator to get a set-level theorem."** This is the reverse of the [[Thm - Monotone Convergence Theorem|standard machine]] (which builds *up* from indicators); here one *specialises down*. The density theorem is the tool behind the regularity of measurable sets, the structure of sets of positive measure (every such set contains a near-interval — Steinhaus's theorem), and the a.e. behaviour of [[Thm - Radon-Nikodym Theorem|Radon–Nikodym derivatives]] as limits of measure ratios.
