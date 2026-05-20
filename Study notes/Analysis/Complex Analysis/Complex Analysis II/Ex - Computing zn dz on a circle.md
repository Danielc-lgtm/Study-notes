---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Def - Contour Integral"
  - "Thm - Fundamental Theorem of Contour Integration"
tags: [analysis, complex-analysis]
---

# Problem Statement

For each integer $n \in \mathbb{Z}$, compute the contour integral
$$\int_{|z| = 1} z^n\,dz$$
where the unit circle is traversed counterclockwise once.

**Recall:**

The [[Def - Contour Integral|contour integral]] is $\int_\gamma f\,dz = \int_a^b f(\gamma(t))\gamma'(t)\,dt$ for $\gamma : [a, b] \to \mathbb{C}$ piecewise $C^1$. If $f$ has a primitive $F$ on a domain containing $\gamma$, [[Thm - Fundamental Theorem of Contour Integration]] gives $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$, which is $0$ for closed $\gamma$.

---

# Convergent Strategy

**Problem class:** Direct computation of a contour integral, with case-split by whether a primitive exists globally.

**Assumption pattern:** Integer powers $z^n$ — easy primitives for $n \neq -1$.

**Theorem routing:** For $n \neq -1$: $z^{n+1}/(n+1)$ is a primitive on $\mathbb{C}^\times$ (or $\mathbb{C}$ for $n \geq 0$); FT gives $0$. For $n = -1$: no global primitive on a domain containing the circle; parametrize and compute directly.

**Key decision point:** Recognizing that the case $n = -1$ is the *single* nonzero integral, and that it is the seed of all winding-number and residue phenomena.

---

# Legal Operations Used

1. **Identify a primitive** for $n \neq -1$: $z^{n+1}/(n+1)$, valid on $\mathbb{C}^\times$ (where $n < -1$) or $\mathbb{C}$ (where $n \geq 0$). Closed loop ⇒ integral $= 0$.
2. **Direct parametrization** of the unit circle: $\gamma(t) = e^{it}, t \in [0, 2\pi]$, $\gamma'(t) = ie^{it}$.
3. **Reduce** the integral $\int_{|z|=1} z^n\,dz = \int_0^{2\pi} e^{int} \cdot ie^{it}\,dt = i\int_0^{2\pi} e^{i(n+1)t}\,dt$.

---

# Hints

> [!note]- Hint 1
> Recall: $z^{n+1}/(n+1)$ is the primitive of $z^n$ for $n \neq -1$. Where does this primitive exist on the domain containing the circle?

> [!note]- Hint 2
> For $n = -1$, no global primitive: parametrize $\gamma(t) = e^{it}$ and compute the integral by hand.

---

# Solution

**Case 1: $n \neq -1$.**

The function $z^n$ has primitive $F(z) = z^{n+1}/(n+1)$:
- For $n \geq 0$: $F$ is entire (a polynomial), so $z^n$ has a primitive on all of $\mathbb{C}$.
- For $n \leq -2$: $F$ is holomorphic on $\mathbb{C}^\times$ (the singularity at $0$ in the original function is shifted to $0$ in $F$, but $F$ is still well-defined for $z \neq 0$).

In either case, $F$ is a primitive of $z^n$ on a domain containing the unit circle. By [[Thm - Fundamental Theorem of Contour Integration]]:
$$\int_{|z|=1} z^n\,dz = F(\text{endpoint}) - F(\text{startpoint}) = 0$$
since the curve is closed.

**Case 2: $n = -1$.**

Parametrize $\gamma(t) = e^{it}, t \in [0, 2\pi]$. Then $\gamma'(t) = ie^{it}$, and $z^{-1} = e^{-it}$ on the circle. So
$$\int_{|z|=1}\frac{dz}{z} = \int_0^{2\pi} e^{-it} \cdot ie^{it}\,dt = i\int_0^{2\pi} 1\,dt = 2\pi i.$$

So the integral is $2\pi i$, nonzero.

> [!note]- Complete formal solution
> $\int_{|z|=1} z^n\,dz = \begin{cases} 0 & n \neq -1 \\ 2\pi i & n = -1\end{cases}$.
>
> For $n \neq -1$: primitive $z^{n+1}/(n+1)$ on a domain containing the unit circle (in $\mathbb{C}$ for $n \geq 0$, in $\mathbb{C}^\times$ for $n \leq -2$). FT of contour integration: integral around closed curve is $0$.
>
> For $n = -1$: parametrize, compute $i \int_0^{2\pi} e^{i(n+1)t}\,dt = i \int_0^{2\pi} 1\,dt = 2\pi i$. $\blacksquare$

---

# Key Takeaways

**The single nonzero integral.**

Among the integer powers $z^n$, only $n = -1$ gives a nonzero contour integral around the unit circle. This single integral is the *seed* of all winding-number and residue theory: $\frac{1}{2\pi i}\int dz/z = 1$ is the winding number of the unit circle around $0$. The general statement: for $f(z) = (z - a)^{-1}$ and a closed curve $\gamma$ not passing through $a$, $\frac{1}{2\pi i}\int_\gamma dz/(z - a)$ is the winding number of $\gamma$ around $a$.

**Why is $n = -1$ special?**

Because $1/z$ has no global primitive on any domain containing a loop around $0$ (e.g., the unit circle). The primitives of $1/z$ are branches of $\log z$, defined only on simply connected subsets of $\mathbb{C}^\times$. The unit circle goes around $0$, breaking simple-connectedness — and so the FT does not apply.

**Trigger-reaction pattern.**

When you see $\int_\gamma f\,dz$ for $f = 1/z$, the answer involves *winding number*, not direct integration. The general principle: contour integrals around closed curves equal $2\pi i$ times the sum of residues inside (the residue theorem of [[Complex Analysis III — Winding, Laurent, Residues|CA III]]). The integer $n = -1$ case here is the prototype.
