---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Product Measure"
  - "Thm - Fubini-Tonelli Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $D=\{(x,x):x\in[0,1]\}$ be the diagonal of the unit square.

**(a)** Show $D\in\mathcal{B}([0,1])\otimes\mathcal{B}([0,1])$.

**(b)** Compute $(\lambda\otimes\lambda)(D)$ via [[Thm - Fubini-Tonelli Theorem|Tonelli]] and show it is $0$ — the diagonal is a planar null set.

**(c)** Now let $\mu$ be **counting measure** on $[0,1]$. Compute the two iterated integrals of $\mathbf{1}_D$ for $\mu\otimes\lambda$ and show they *differ*. Reconcile with Tonelli.

**Recall:**

[[Thm - Fubini-Tonelli Theorem|Tonelli]] requires both measures **$\sigma$-finite**; then $\int\mathbf{1}_D=\iint\mathbf{1}_D$ in either order.

---

# Convergent Strategy

**Problem class:** computing a product measure of a thin set; probing the $\sigma$-finiteness hypothesis of Tonelli.

**Assumption pattern:** $D$ has measurable (length-$0$) slices for $\lambda$ — vertical slice $D_x=\{x\}$. For $\lambda\otimes\lambda$, Tonelli applies and gives $0$. For $\mu\otimes\lambda$ with $\mu$ counting measure on the *uncountable* $[0,1]$, $\mu$ is **not $\sigma$-finite** — Tonelli's hypothesis fails, and the iterated integrals diverge.

---

# Legal Operations Used

1. **Tonelli** on $\mathbf{1}_D$ (when both measures $\sigma$-finite).
2. **Compute slices** and their measures.
3. **Negate $\sigma$-finiteness** of counting measure on an uncountable set.

---

# Hints

> [!note]- Hint 1
> $D$ is closed in $[0,1]^2$, hence Borel, hence in the product $\sigma$-algebra ($\mathcal{B}\otimes\mathcal{B}=\mathcal{B}(\mathbb{R}^2)$ restricted).

> [!note]- Hint 2
> Vertical slice $D_x=\{x\}$, with $\lambda(\{x\})=0$. Integrate over $x$.

> [!note]- Hint 3
> For (c): $\int_x\big(\int_y\mathbf{1}_D\,d\lambda\big)d\mu$ vs $\int_y\big(\int_x\mathbf{1}_D\,d\mu\big)d\lambda$ — one is $0$, the other $1$.

---

# Solution

**Step 1 — (a).** $D$ is the zero set of the continuous $(x,y)\mapsto x-y$, hence closed in $[0,1]^2$, hence Borel; and $\mathcal{B}([0,1])\otimes\mathcal{B}([0,1])=\mathcal{B}([0,1]^2)$, so $D$ is product-measurable.

**Step 2 — (b).** Both factors are $\lambda$, finite on $[0,1]$, hence $\sigma$-finite. By [[Thm - Fubini-Tonelli Theorem|Tonelli]] on $\mathbf{1}_D\ge0$,
$$(\lambda\otimes\lambda)(D)=\int_0^1\Big(\int_0^1\mathbf{1}_D(x,y)\,d\lambda(y)\Big)d\lambda(x)=\int_0^1\lambda(\{x\})\,d\lambda(x)=\int_0^1 0\,d\lambda=0.$$
The diagonal is a planar null set — consistent with it being a one-dimensional curve in two-dimensional space.

**Step 3 — (c).** Let $\mu$ = counting measure on $[0,1]$.

> [!note]- Derivation
> *Integrate $y$ ($d\lambda$) first, then $x$ ($d\mu$):* $\int_y\mathbf{1}_D(x,y)\,d\lambda=\lambda(\{x\})=0$, so $\int_x 0\,d\mu=0$.
> *Integrate $x$ ($d\mu$) first, then $y$ ($d\lambda$):* $\int_x\mathbf{1}_D(x,y)\,d\mu=\mu(\{y\})=1$, so $\int_y 1\,d\lambda=\lambda([0,1])=1$.
> The two iterated integrals are $0\neq1$. This does **not** contradict [[Thm - Fubini-Tonelli Theorem|Tonelli]]: Tonelli requires both measures $\sigma$-finite, but counting measure on the *uncountable* set $[0,1]$ is **not $\sigma$-finite** — any countable union of finite-measure (finite) sets is countable, never all of $[0,1]$. With the hypothesis violated, the iterated integrals are free to disagree.

> [!note]- Complete formal solution
> (a) $D$ closed $\Rightarrow$ Borel $\Rightarrow$ product-measurable. (b) Tonelli on $\mathbf{1}_D$ ($\lambda,\lambda$ $\sigma$-finite): $\int_x\lambda(\{x\})\,d\lambda=0$. (c) For $\mu\otimes\lambda$: $\lambda$-first gives $0$, $\mu$-first gives $\int_y\mu(\{y\})\,d\lambda=\int_y 1\,d\lambda=1$; no contradiction, since counting measure on uncountable $[0,1]$ is not $\sigma$-finite, violating Tonelli's hypothesis. $\blacksquare$

---

# Key Takeaways

**A "thin" set — a curve, a lower-dimensional submanifold — has product measure zero, because almost every slice has measure zero.** Tonelli converts "$(\lambda\otimes\lambda)(D)=0$" into "$\int\lambda(\text{slice})\,d\lambda=0$," and each slice $\{x\}$ is a single point. This is the rigorous form of "a one-dimensional curve occupies no two-dimensional area," and it generalises: graphs of measurable functions, hyperplanes, and smooth submanifolds of positive codimension are all Lebesgue-null.

**$\sigma$-finiteness is a genuine hypothesis of Tonelli, not a technicality — counting measure on an uncountable space breaks it, and the iterated integrals then legitimately disagree.** This is the exact analogue, *for non-negative* integrands, of how [[Ex - Fubini fails without integrability|Fubini fails without integrability]] for signed ones: in both cases a hypothesis of the Fubini–Tonelli theorem is amputated and the order of integration stops mattering. The diagnostic before any iterated-integral computation: *are both measures $\sigma$-finite, and (for signed $f$) is $f$ absolutely integrable?*
