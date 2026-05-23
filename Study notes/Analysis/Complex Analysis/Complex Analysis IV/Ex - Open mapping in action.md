---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Open Mapping Theorem"
  - "Def - Holomorphic Function"
  - "Thm - Cauchy–Riemann Equations"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $f$ be holomorphic on a domain $D$ with $|f|$ constant on $D$. Show that $f$ is constant on $D$.

**Recall:**

![[Thm - Open Mapping Theorem#Notation]]

A non-constant holomorphic function on a domain is an open map.

---

# Convergent Strategy

**Problem class:** Force constancy of a holomorphic function from a geometric constraint on $|f|$. Two strategies: (a) the *open mapping* argument; (b) the *Cauchy-Riemann* argument. Both work.

**Assumption pattern:** $|f| = c$ on $D$ for some constant $c \geq 0$. If $c = 0$, $f = 0$, trivially constant. Otherwise $f \neq 0$ on $D$.

**Theorem routing:** Two routes:
- *Open mapping*: $f(D)$ lies on the circle $|w| = c$, which is *not open*. By open mapping theorem (contrapositive), $f$ must be constant.
- *Cauchy-Riemann*: differentiate $|f|^2 = u^2 + v^2 = c^2$ and use CR equations.

**Key decision point:** The open mapping argument is the "smart" one — instant. The CR argument is more direct but requires algebra.

---

# Legal Operations Used

**Method 1 (Open Mapping):**
1. Assume $|f| = c$ on $D$, suppose $c > 0$ (else $f \equiv 0$, constant, done).
2. Observe $f(D) \subseteq \{|w| = c\}$, the circle of radius $c$.
3. The circle $\{|w| = c\}$ has empty interior (is *not open*) in $\mathbb{C}$.
4. By [[Thm - Open Mapping Theorem|open mapping theorem]], if $f$ is non-constant, $f(D)$ is open — contradiction.
5. Conclude $f$ is constant.

**Method 2 (Cauchy-Riemann):**
1. Write $f = u + iv$. $|f|^2 = u^2 + v^2 = c^2$, constant.
2. Differentiate: $2u u_x + 2v v_x = 0$, $2u u_y + 2v v_y = 0$.
3. Apply Cauchy-Riemann: $v_x = -u_y$, $v_y = u_x$. So: $u u_x - v u_y = 0$ and $u u_y + v u_x = 0$.
4. Solve the linear system in $u_x, u_y$: determinant is $u^2 + v^2 = c^2$.
5. If $c \neq 0$: $u_x = u_y = 0$, so $u$ constant, similarly $v$ constant.
6. If $c = 0$: $f = 0$, constant trivially.

---

# Hints

> [!note]- Hint 1 (Open Mapping)
> The image $f(D)$ lies on a circle, which has no interior. By the open mapping theorem (contrapositive), $f$ must be constant.

> [!note]- Hint 2 (Cauchy-Riemann)
> Write $f = u + iv$ with $u^2 + v^2 = c^2$ constant. Differentiate and apply Cauchy-Riemann.

> [!note]- Hint 3 (CR algebra)
> $u u_x + v v_x = 0$ and $u u_y + v v_y = 0$. Apply $v_x = -u_y, v_y = u_x$: $u u_x - v u_y = 0$ and $u u_y + v u_x = 0$. This is a linear system in $u_x, u_y$ with matrix $\begin{pmatrix}u & -v \\ v & u\end{pmatrix}$, determinant $u^2 + v^2 = c^2$. Nontrivial determinant ⟹ $u_x = u_y = 0$.

---

# Solution

**Method 1 (via Open Mapping)**

**Step 1: Reduce to the case $|f| = c > 0$**

If $|f| = c = 0$ on $D$, then $f \equiv 0$, constant. Otherwise, $c > 0$.

**Step 2: $f(D)$ lies on a circle**

> [!note]- Derivation
> The image $f(D) \subseteq \{w \in \mathbb{C} : |w| = c\}$, the circle of radius $c$ centred at $0$.
>
> The circle is a closed curve, not an open set in $\mathbb{C}$ — its interior (as a subset of $\mathbb{C}$, not as a region inside the circle) is empty. Specifically, any point on the circle has neighborhoods in $\mathbb{C}$ containing points *not* on the circle.

**Step 3: Contradiction with open mapping**

> [!note]- Derivation
> Suppose $f$ is non-constant. By the [[Thm - Open Mapping Theorem|open mapping theorem]], $f(D)$ is an open subset of $\mathbb{C}$. But $f(D) \subseteq \{|w| = c\}$, which has empty interior. The only open subset of a set with empty interior is the empty set. So $f(D) = \emptyset$, impossible since $D$ is nonempty.
>
> Hence $f$ is constant.

> [!note]- Complete formal solution (Method 1)
> Suppose $|f(z)| = c$ for all $z \in D$. If $c = 0$, $f \equiv 0$, constant.
>
> If $c > 0$: $f(D) \subseteq \{w \in \mathbb{C} : |w| = c\}$, the circle of radius $c$. This circle has empty interior in $\mathbb{C}$, so the only open subset of the circle is $\emptyset$.
>
> If $f$ is non-constant, by the [[Thm - Open Mapping Theorem|open mapping theorem]] $f(D)$ is open. But $f(D) \subseteq$ (set with empty interior), so $f(D) = \emptyset$. Contradiction with $f(D) \neq \emptyset$.
>
> So $f$ is constant. $\blacksquare$

**Method 2 (via Cauchy-Riemann)**

> [!note]- Derivation
> Write $f = u + iv$. The condition $|f|^2 = u^2 + v^2 = c^2$ holds on $D$.
>
> Differentiate with respect to $x$: $2u u_x + 2v v_x = 0$, so $u u_x + v v_x = 0$.
> Differentiate with respect to $y$: $u u_y + v v_y = 0$.
>
> Apply Cauchy-Riemann: $v_x = -u_y$ and $v_y = u_x$. Substituting:
> $$u u_x - v u_y = 0, \qquad u u_y + v u_x = 0.$$
>
> This is a linear system in $u_x, u_y$:
> $$\begin{pmatrix} u & -v \\ v & u \end{pmatrix}\begin{pmatrix}u_x \\ u_y\end{pmatrix} = \begin{pmatrix}0 \\ 0\end{pmatrix}.$$
> The determinant is $u^2 + v^2 = c^2$. If $c \neq 0$, the only solution is $u_x = u_y = 0$, so $u$ is constant. Then $v$ is also constant (by CR or by $v^2 = c^2 - u^2$ constant). Hence $f = u + iv$ is constant.
>
> If $c = 0$: $f \equiv 0$, trivially constant.

---

# Key Takeaways

**Trigger-reaction pattern — "$|f|$ constant on a domain" → "$f$ is constant".** This is a fundamental consequence of holomorphic rigidity. The image of a non-constant holomorphic function is always 2-dimensional ("thick"), so being constrained to a 1-dimensional set (a circle, a line) forces constancy.

**Compare with real analysis.** A real $C^\infty$ function with $|f| = c$ can be highly non-constant: $f(x) = c\cos(g(x))$ for any smooth $g$, for instance. The constraint $|f| = c$ on a real interval is much weaker than on a complex domain.

**The open mapping argument is geometric; the CR argument is computational.** Different problem-solving styles suit different proofs:
- Open mapping: immediate, conceptual, uses high-powered theorem.
- Cauchy-Riemann: direct calculation, can be done with bare definitions, doesn't invoke "big" theorems.

**Generalization — image in any non-open set forces constancy.** A non-constant holomorphic function has open image. So if the image is constrained to *any* set with empty interior — a line, a curve, a countable set — the function must be constant. Examples:
- $f : D \to \mathbb{R}$ holomorphic ⟹ $f$ constant.
- $f : D \to$ (countable set) holomorphic ⟹ $f$ constant.
- $f : D \to$ (a smooth curve in $\mathbb{C}$) holomorphic ⟹ $f$ constant.
