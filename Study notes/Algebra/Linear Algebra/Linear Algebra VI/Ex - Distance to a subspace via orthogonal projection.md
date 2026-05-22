---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthogonal Projection"
  - "Thm - Best Approximation by Orthogonal Projection"
  - "Thm - Gram-Schmidt Procedure"
tags: [algebra, linear-algebra]
---

# Problem Statement

In $\mathbb{R}^4$ with the standard Euclidean inner product, let
$$
U = \operatorname{span}\bigl((1, 1, 0, 0),\ (1, 1, 1, 2)\bigr).
$$

Find the vector $u \in U$ that minimises $\|u - (1, 2, 3, 4)\|$, and compute this minimum distance.

**Recall:**

The setting: $V = \mathbb{R}^4$ with $\langle x, y\rangle = x_1 y_1 + x_2 y_2 + x_3 y_3 + x_4 y_4$.

![[Thm - Best Approximation by Orthogonal Projection#Statement]]

The orthogonal projection has the explicit formula
$$
P_U v = \langle v, e_1\rangle e_1 + \langle v, e_2\rangle e_2
$$
once we have an orthonormal basis $e_1, e_2$ of $U$. Gram-Schmidt converts the given spanning set $(1, 1, 0, 0), (1, 1, 1, 2)$ to such an orthonormal basis.

---

# Convergent Strategy

**Problem class.** This is a *distance-to-subspace* problem, the simplest application of the [[Thm - Best Approximation by Orthogonal Projection|best-approximation theorem]]. The route is mechanical: Gram-Schmidt the spanning set to get an orthonormal basis, project the target vector, compute the distance.

**Assumption pattern.** The hypothesis is an explicit $2$-dimensional subspace of $\mathbb{R}^4$ given by two spanning vectors, and a target vector. The spanning vectors are *not* orthogonal: $\langle (1, 1, 0, 0), (1, 1, 1, 2)\rangle = 1 + 1 + 0 + 0 = 2 \neq 0$. So Gram-Schmidt is required to convert them to an orthonormal basis.

**Theorem routing.** The route is:
1. By the [[Thm - Best Approximation by Orthogonal Projection|best-approximation theorem]], the minimiser is $P_U v$, the orthogonal projection of $v = (1, 2, 3, 4)$ onto $U$.
2. By [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]], an orthonormal basis $e_1, e_2$ of $U$ is constructed from the given spanning set.
3. By the orthonormal-basis formula, $P_U v = \langle v, e_1\rangle e_1 + \langle v, e_2\rangle e_2$.
4. The minimum distance is $\|v - P_U v\|$, computable directly or via Pythagoras as $\sqrt{\|v\|^2 - \|P_U v\|^2}$.

**Key decision point.** Whether to use the orthonormal-basis formula or solve the projection problem via normal equations $A^T A x = A^T v$ where $A$ is the matrix with columns $v_1, v_2$. Both approaches are correct; the orthonormal-basis approach is cleaner and is the canonical route in the chapter, while normal equations is the matrix-oriented alternative more familiar from least-squares.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VI — §6 Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Project orthogonally to find the closest point** (operation 3). The minimiser of $\|v - u\|$ over $u \in U$ is $P_U v$.

2. **Orthogonalize via Gram-Schmidt** (operation 2). The spanning vectors $(1, 1, 0, 0), (1, 1, 1, 2)$ are not orthogonal in $\mathbb{R}^4$; Gram-Schmidt produces the orthonormal basis.

3. **Use Pythagoras to break a norm into orthogonal pieces** (operation 4). Computing the distance via $\|v - P_U v\|^2 = \|v\|^2 - \|P_U v\|^2$ uses $v = P_U v + (v - P_U v)$ and the orthogonality of the summands.

---

# Hints

> [!note]- Hint 1
> The minimiser is $u^* = P_U v$, the orthogonal projection. To compute it, you need an orthonormal basis of $U$. The given spanning vectors are not orthonormal, so use Gram-Schmidt.

> [!note]- Hint 2
> Set $v_1 = (1, 1, 0, 0)$. Then $e_1 = v_1 / \|v_1\| = v_1/\sqrt{2}$. For $e_2$, subtract from $v_2 = (1, 1, 1, 2)$ its projection onto $e_1$, then normalize.

> [!note]- Hint 3
> Compute $\langle v_2, e_1\rangle = \langle (1, 1, 1, 2), (1, 1, 0, 0)/\sqrt{2}\rangle = 2/\sqrt{2} = \sqrt{2}$. So $v_2 - \langle v_2, e_1\rangle e_1 = (1, 1, 1, 2) - \sqrt{2} \cdot (1, 1, 0, 0)/\sqrt{2} = (1, 1, 1, 2) - (1, 1, 0, 0) = (0, 0, 1, 2)$. The norm is $\sqrt{0 + 0 + 1 + 4} = \sqrt{5}$, so $e_2 = (0, 0, 1, 2)/\sqrt{5}$.

> [!note]- Hint 4
> Now compute the projection coefficients: $\langle v, e_1\rangle = \langle (1, 2, 3, 4), (1, 1, 0, 0)/\sqrt{2}\rangle = 3/\sqrt{2}$ and $\langle v, e_2\rangle = \langle (1, 2, 3, 4), (0, 0, 1, 2)/\sqrt{5}\rangle = (3 + 8)/\sqrt{5} = 11/\sqrt{5}$.

> [!note]- Hint 5
> The projection is $P_U v = \frac{3}{\sqrt{2}}\cdot \frac{(1, 1, 0, 0)}{\sqrt{2}} + \frac{11}{\sqrt{5}}\cdot \frac{(0, 0, 1, 2)}{\sqrt{5}} = \frac{3}{2}(1, 1, 0, 0) + \frac{11}{5}(0, 0, 1, 2) = (3/2, 3/2, 11/5, 22/5)$. The residual is $v - P_U v = (-1/2, 1/2, 4/5, -2/5)$, with norm $\sqrt{1/4 + 1/4 + 16/25 + 4/25} = \sqrt{1/2 + 20/25} = \sqrt{1/2 + 4/5}$.

---

# Solution

The strategy is the standard projection route: Gram-Schmidt the spanning set, compute projection coefficients, sum.

**Plan:** Step 1 sets up the projection problem. Step 2 builds the orthonormal basis $e_1, e_2$ via Gram-Schmidt. Step 3 computes the projection $P_U v$ and the closest vector $u^* = P_U v$. Step 4 computes the minimum distance $\|v - u^*\|$.

**Step 1: Identify the projection problem.**

We seek $u^* = P_U v$, where $U = \operatorname{span}((1, 1, 0, 0), (1, 1, 1, 2))$ and $v = (1, 2, 3, 4)$.

> [!note]- Derivation
> By the [[Thm - Best Approximation by Orthogonal Projection|best-approximation theorem]], the minimiser of $\|u - v\|$ over $u \in U$ is the orthogonal projection $P_U v$. We compute it explicitly using an orthonormal basis of $U$.

**Step 2: Gram-Schmidt to build an orthonormal basis of $U$.**

Apply Gram-Schmidt to $v_1 = (1, 1, 0, 0)$ and $v_2 = (1, 1, 1, 2)$ to get an orthonormal pair $e_1, e_2$.

> [!note]- Derivation
> First, $\|v_1\|^2 = 1 + 1 + 0 + 0 = 2$, so $\|v_1\| = \sqrt{2}$ and $e_1 = v_1/\sqrt{2} = (1, 1, 0, 0)/\sqrt{2}$.
>
> Next, subtract from $v_2$ its projection onto $e_1$:
> $$\langle v_2, e_1\rangle = \langle (1, 1, 1, 2), (1, 1, 0, 0)\rangle/\sqrt{2} = (1 + 1 + 0 + 0)/\sqrt{2} = 2/\sqrt{2} = \sqrt{2}.$$
> Then
> $$f_2 = v_2 - \langle v_2, e_1\rangle e_1 = (1, 1, 1, 2) - \sqrt{2} \cdot (1, 1, 0, 0)/\sqrt{2} = (1, 1, 1, 2) - (1, 1, 0, 0) = (0, 0, 1, 2).$$
> So $\|f_2\|^2 = 0 + 0 + 1 + 4 = 5$, $\|f_2\| = \sqrt{5}$, and $e_2 = (0, 0, 1, 2)/\sqrt{5}$.
>
> Verify orthonormality: $\|e_1\|^2 = (1 + 1)/2 = 1$, $\|e_2\|^2 = (1 + 4)/5 = 1$, and $\langle e_1, e_2\rangle = (1 \cdot 0 + 1 \cdot 0 + 0 \cdot 1 + 0 \cdot 2)/\sqrt{10} = 0$. So $e_1, e_2$ is orthonormal.

**Step 3: Compute the orthogonal projection $P_U v$.**

By the orthonormal-basis formula, $P_U v = \langle v, e_1\rangle e_1 + \langle v, e_2\rangle e_2$.

> [!note]- Derivation
> Compute:
> $$\langle v, e_1\rangle = \langle (1, 2, 3, 4), (1, 1, 0, 0)\rangle/\sqrt{2} = (1 + 2 + 0 + 0)/\sqrt{2} = 3/\sqrt{2}.$$
> $$\langle v, e_2\rangle = \langle (1, 2, 3, 4), (0, 0, 1, 2)\rangle/\sqrt{5} = (0 + 0 + 3 + 8)/\sqrt{5} = 11/\sqrt{5}.$$
>
> Hence
> $$P_U v = \frac{3}{\sqrt{2}}\cdot \frac{(1, 1, 0, 0)}{\sqrt{2}} + \frac{11}{\sqrt{5}}\cdot\frac{(0, 0, 1, 2)}{\sqrt{5}} = \frac{3}{2}(1, 1, 0, 0) + \frac{11}{5}(0, 0, 1, 2).$$
> Computing:
> $$P_U v = \left(\frac{3}{2},\ \frac{3}{2},\ \frac{11}{5},\ \frac{22}{5}\right).$$

**Step 4: Compute the minimum distance $\|v - P_U v\|$.**

The residual is $v - P_U v$, and the minimum distance is its norm.

> [!note]- Derivation
> The residual is
> $$v - P_U v = (1, 2, 3, 4) - (3/2, 3/2, 11/5, 22/5) = (1 - 3/2,\ 2 - 3/2,\ 3 - 11/5,\ 4 - 22/5) = (-1/2,\ 1/2,\ 4/5,\ -2/5).$$
>
> Its squared norm:
> $$\|v - P_U v\|^2 = \left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 + \left(\frac{4}{5}\right)^2 + \left(\frac{2}{5}\right)^2 = \frac{1}{4} + \frac{1}{4} + \frac{16}{25} + \frac{4}{25} = \frac{1}{2} + \frac{20}{25} = \frac{1}{2} + \frac{4}{5}.$$
>
> Common denominator $10$: $\frac{5}{10} + \frac{8}{10} = \frac{13}{10}$.
>
> So $\|v - P_U v\| = \sqrt{13/10} = \sqrt{1.3} \approx 1.140$.

> [!note]- Sanity check via Pythagoras
> An alternative check: $\|v\|^2 = 1 + 4 + 9 + 16 = 30$. By Pythagoras applied to $v = P_U v + (v - P_U v)$, $\|v\|^2 = \|P_U v\|^2 + \|v - P_U v\|^2$.
>
> Compute $\|P_U v\|^2 = (3/2)^2 + (3/2)^2 + (11/5)^2 + (22/5)^2 = 9/4 + 9/4 + 121/25 + 484/25 = 9/2 + 605/25 = 9/2 + 121/5$. Common denominator $10$: $45/10 + 242/10 = 287/10 = 28.7$.
>
> So $\|v - P_U v\|^2 = \|v\|^2 - \|P_U v\|^2 = 30 - 28.7 = 1.3 = 13/10$. ✓ Confirms the direct computation.

> [!note]- Complete formal solution
> Apply [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] to $v_1 = (1, 1, 0, 0), v_2 = (1, 1, 1, 2)$:
> $$e_1 = \frac{(1, 1, 0, 0)}{\sqrt{2}}, \quad e_2 = \frac{(0, 0, 1, 2)}{\sqrt{5}}.$$
>
> Project $v = (1, 2, 3, 4)$:
> $$\langle v, e_1\rangle = \frac{3}{\sqrt{2}}, \quad \langle v, e_2\rangle = \frac{11}{\sqrt{5}}.$$
> $$u^* = P_U v = \frac{3}{2}(1, 1, 0, 0) + \frac{11}{5}(0, 0, 1, 2) = \left(\frac{3}{2}, \frac{3}{2}, \frac{11}{5}, \frac{22}{5}\right).$$
>
> Minimum distance:
> $$\|v - u^*\| = \sqrt{\frac{13}{10}} \approx 1.140.$$
>
> Equivalently $\|v - u^*\| = \sqrt{30 - 28.7}$, verifiable via Pythagoras. $\blacksquare$

---

# Key Takeaways

**The orthogonal-projection algorithm is a three-step recipe.** Whenever you have a finite-dimensional subspace and a target vector, the algorithm for finding the closest point in the subspace is: (1) Gram-Schmidt the spanning set to get an orthonormal basis $e_1, \dots, e_m$; (2) compute the projection coefficients $\langle v, e_k\rangle$ for each $k$; (3) the closest point is $\sum_k \langle v, e_k\rangle e_k$, and the minimum distance is the norm of the residual. This recipe is the operational core of the chapter. Every "best fit" computation — least squares, polynomial approximation, conditional expectation in $L^2$ — follows the same three steps. The only thing that changes is the specific inner product and subspace. The transferable lesson: distance-to-a-subspace problems always reduce to Gram-Schmidt + orthonormal projection.

**Pythagoras gives a sanity check via norms.** The identity $\|v\|^2 = \|P_U v\|^2 + \|v - P_U v\|^2$ (from the orthogonal decomposition $v = P_U v + (v - P_U v)$) provides a sanity check on any projection computation: the squared norms of the projection and the residual should sum to the squared norm of the target. If they do not, there is a computational error somewhere — most likely in the Gram-Schmidt orthonormalization or in the projection-coefficient extraction. The Pythagoras check is also useful when only the *distance* is needed, not the projection itself: $\|v - P_U v\|^2 = \|v\|^2 - \|P_U v\|^2$, so you can compute distances without explicitly forming residual vectors.

**Choice of orthonormal basis is canonical for the answer but arbitrary in the basis itself.** The projection $P_U v$ does not depend on which orthonormal basis you Gram-Schmidt to; the final vector is the same regardless of basis choice. But the *route* through the calculation depends on the basis. In this exercise, Gram-Schmidt of $(v_1, v_2)$ in the order given produces specific $e_1, e_2$; reordering the input as $(v_2, v_1)$ would produce different intermediate vectors but the same final projection. The robustness of the answer to basis-choice is a feature: it means you do not need to worry about choosing the "right" basis, only about Gram-Schmidting *some* basis correctly.

**This algorithm is what makes least-squares and regression computable.** The exact same recipe — Gram-Schmidt + projection — underlies least-squares regression. For a regression problem $\min_x \|Ax - b\|$ with $A \in \mathbb{R}^{m \times n}$ having linearly independent columns, you can solve it by: (i) Gram-Schmidt the columns of $A$ to get an orthonormal basis $q_1, \dots, q_n$ of $\operatorname{col} A$; (ii) compute $A\hat x = \sum_k \langle b, q_k\rangle q_k$, the orthogonal projection of $b$ onto $\operatorname{col} A$. The Gram-Schmidt-based algorithm for least squares is one of the standard numerical methods (typically implemented as **QR factorization** $A = QR$). This exercise is the toy version, in $\mathbb{R}^4$ with a $2$-dimensional subspace, of an algorithm used millions of times daily in statistical computing.
