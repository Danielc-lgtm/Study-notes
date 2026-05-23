---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Thm - Cartan's First Structural Equation"
  - "Thm - Cartan's Second Structural Equation"
  - "Def - Connection 1-Forms (Cartan)"
  - "Def - Curvature 2-Forms (Cartan)"
tags: [geometry, riemannian-geometry, connections, cartan-formalism]
---

# Problem Statement

Using the **orthonormal coframe** $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\,d\varphi$ on the round 2-sphere $S^2$:

(a) Compute $d\sigma^1$ and $d\sigma^2$.

(b) Apply Cartan's first structural equation $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ (torsion-free) together with the antisymmetry condition $\omega^a{}_b + \omega^b{}_a = 0$ (metric-compatibility for an orthonormal frame) to determine the connection 1-form $\omega^1{}_2$.

(c) Apply Cartan's second structural equation $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$ to compute the curvature 2-form $\Omega^1{}_2$.

(d) Read off the Gaussian curvature $K$ of the round 2-sphere and confirm $K = 1$.

**Recall:**

![[Thm - Cartan's First Structural Equation#Statement]]

![[Thm - Cartan's Second Structural Equation#Statement]]

For an orthonormal frame on a 2-dimensional Riemannian manifold, there is only one independent connection 1-form $\omega^1{}_2$ (with $\omega^2{}_1 = -\omega^1{}_2$, $\omega^1{}_1 = \omega^2{}_2 = 0$), and only one curvature 2-form $\Omega^1{}_2 = K\sigma^1 \wedge \sigma^2$ where $K$ is the **Gaussian curvature**.

---

# Convergent Strategy

**Problem class:** The textbook application of Cartan's structural equations to compute connection and curvature on a 2-surface in an orthonormal frame. This is dramatically faster than the coordinate Christoffel-based approach (see [[Ex - Christoffel Symbols of the Round Metric on the Sphere]] for the coordinate version), illustrating the operational power of the moving-frame method.

**Assumption pattern:** A 2-dimensional Riemannian manifold with metric given diagonally in spherical coordinates. The orthonormal coframe $(d\theta, \sin\theta\,d\varphi)$ is the natural choice — the coframe whose squares sum to give the metric. Computing $d$ of each is a one-step calculation.

**Theorem routing:** Apply Cartan's first structural equation [[Thm - Cartan's First Structural Equation]] to extract $\omega^1{}_2$ from the $d\sigma^a$'s. The antisymmetry of $\omega$ (metric-compatibility in orthonormal frame) reduces the problem to a single unknown. Then apply Cartan's second structural equation [[Thm - Cartan's Second Structural Equation]] to compute $\Omega^1{}_2$ from $\omega^1{}_2$, and read off $K$ from $\Omega^1{}_2 = K\sigma^1 \wedge \sigma^2$.

**Key decision point:** The non-obvious move is recognising that the first structural equation, in conjunction with antisymmetry, uniquely determines $\omega^1{}_2$ from $d\sigma^a$ — no Christoffel-formula computation needed. The system $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ with antisymmetric $\omega$ has a unique solution, and the solution is the connection 1-form of the unique Levi-Civita connection (existence-uniqueness from [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)]]). This is the computational miracle of the Cartan method.

---

# Legal Operations Used

1. **Operation 2 from the topic page (Set up an orthonormal coframe and use Cartan's first structural equation).** The orthonormal coframe is $(\sigma^1, \sigma^2) = (d\theta, \sin\theta\,d\varphi)$, and the first structural equation extracts $\omega^1{}_2$ in two algebraic moves.

2. **Operation 3 from the topic page (Apply Cartan's second structural equation to compute curvature).** Once $\omega^1{}_2$ is known, $\Omega^1{}_2$ is a one-line calculation. In 2D the $\omega \wedge \omega$ piece vanishes (because the connection matrix is $\begin{pmatrix}0 & \omega^1{}_2 \\ -\omega^1{}_2 & 0\end{pmatrix}$ and $\omega^1{}_c \wedge \omega^c{}_2$ involves $c = 1, 2$ but with $\omega^1{}_1 = 0$ and $\omega^2{}_2 = 0$, only $\omega^1{}_2 \wedge \omega^2{}_2$ and $\omega^1{}_1 \wedge \omega^1{}_2$ contribute, both zero).

---

# Hints

> [!note]- Hint 1
> Verify the coframe is orthonormal: $g = (\sigma^1)^2 + (\sigma^2)^2 = (d\theta)^2 + \sin^2\theta(d\varphi)^2$ — matches the round metric.

> [!note]- Hint 2
> Compute $d\sigma^1 = d(d\theta) = 0$ (since $d^2 = 0$). Compute $d\sigma^2 = d(\sin\theta\,d\varphi) = \cos\theta\,d\theta \wedge d\varphi$. Rewrite in the orthonormal basis: $\cos\theta\,d\theta \wedge d\varphi = \cot\theta\,d\theta \wedge (\sin\theta\,d\varphi) = \cot\theta\,\sigma^1 \wedge \sigma^2$.

> [!note]- Hint 3
> Cartan's first equation with torsion-free and antisymmetry gives: $d\sigma^1 + \omega^1{}_2 \wedge \sigma^2 = 0$ (since $\omega^1{}_1 = 0$), and $d\sigma^2 - \omega^1{}_2 \wedge \sigma^1 = 0$ (since $\omega^2{}_1 = -\omega^1{}_2$ and $\omega^2{}_2 = 0$). The first equation is $0 + \omega^1{}_2 \wedge \sigma^2 = 0$, automatically satisfied for any $\omega^1{}_2 = $ multiple of $\sigma^2$. The second gives $\cot\theta\,\sigma^1 \wedge \sigma^2 = \omega^1{}_2 \wedge \sigma^1$. Hence $\omega^1{}_2 = -\cos\theta\,d\varphi$ (note the sign: $\omega^1{}_2 \wedge \sigma^1 = -\sigma^1 \wedge \omega^1{}_2$).

> [!note]- Hint 4
> Compute $d\omega^1{}_2 = d(-\cos\theta\,d\varphi) = \sin\theta\,d\theta \wedge d\varphi = \sigma^1 \wedge \sigma^2$ (using $d\varphi = \sigma^2/\sin\theta$, so $d\theta \wedge d\varphi = \sigma^1 \wedge \sigma^2/\sin\theta$, hence $\sin\theta\,d\theta \wedge d\varphi = \sigma^1 \wedge \sigma^2$). The $\omega \wedge \omega$ piece in 2D vanishes. So $\Omega^1{}_2 = \sigma^1 \wedge \sigma^2$, giving $K = 1$.

---

# Solution

**Plan paragraph.** The solution is three steps: compute $d\sigma^1, d\sigma^2$ (trivially); solve the first structural equation for $\omega^1{}_2$ (a brief algebraic deduction using antisymmetry); compute $d\omega^1{}_2$ and apply the second structural equation to find $\Omega^1{}_2$ (one-line, since the $\omega \wedge \omega$ piece vanishes in 2D). The result $K = 1$ falls out at the end.

**Step 1: Compute $d\sigma^1$ and $d\sigma^2$.**

$\sigma^1 = d\theta$, so $d\sigma^1 = d(d\theta) = 0$ by $d^2 = 0$.

$\sigma^2 = \sin\theta\,d\varphi$, so $d\sigma^2 = d(\sin\theta) \wedge d\varphi + \sin\theta\,d(d\varphi) = \cos\theta\,d\theta \wedge d\varphi + 0 = \cos\theta\,d\theta \wedge d\varphi$.

Express in the orthonormal basis: $d\varphi = (1/\sin\theta)\sigma^2$, so $d\theta \wedge d\varphi = (1/\sin\theta)\sigma^1 \wedge \sigma^2$. Therefore $d\sigma^2 = \cos\theta \cdot (1/\sin\theta)\sigma^1 \wedge \sigma^2 = \cot\theta\,\sigma^1 \wedge \sigma^2$.

> [!note]- Derivation
> $d\sigma^1 = d(d\theta) = 0$: trivially. $d\sigma^2 = d(\sin\theta\,d\varphi)$: by the Leibniz rule for $d$, $d(f\alpha) = df \wedge \alpha + f\,d\alpha$. Here $f = \sin\theta$ and $\alpha = d\varphi$, so $df = \cos\theta\,d\theta$ and $d\alpha = 0$. Result: $d\sigma^2 = \cos\theta\,d\theta \wedge d\varphi$. To express in orthonormal basis: $\sigma^1 = d\theta, \sigma^2 = \sin\theta\,d\varphi$, so $d\theta \wedge d\varphi = \sigma^1 \wedge (\sigma^2/\sin\theta) = \sigma^1 \wedge \sigma^2/\sin\theta$. Thus $d\sigma^2 = \cos\theta \cdot \sigma^1 \wedge \sigma^2/\sin\theta = \cot\theta\,\sigma^1 \wedge \sigma^2$.

**Step 2: Apply Cartan's first structural equation.**

The connection 1-forms in an orthonormal frame are antisymmetric: $\omega^1{}_1 = \omega^2{}_2 = 0$ and $\omega^2{}_1 = -\omega^1{}_2$. So the only unknown is $\omega^1{}_2$.

First structural equations (torsion-free):
- $d\sigma^1 + \omega^1{}_b \wedge \sigma^b = 0$, i.e., $0 + \omega^1{}_1 \wedge \sigma^1 + \omega^1{}_2 \wedge \sigma^2 = \omega^1{}_2 \wedge \sigma^2 = 0$.
- $d\sigma^2 + \omega^2{}_b \wedge \sigma^b = 0$, i.e., $\cot\theta\,\sigma^1 \wedge \sigma^2 + \omega^2{}_1 \wedge \sigma^1 + 0 = \cot\theta\,\sigma^1 \wedge \sigma^2 - \omega^1{}_2 \wedge \sigma^1 = 0$.

From the first equation, $\omega^1{}_2 \wedge \sigma^2 = 0$, which is automatically satisfied if $\omega^1{}_2$ has no $\sigma^1$ component — i.e., $\omega^1{}_2$ is a multiple of $\sigma^2$. Write $\omega^1{}_2 = a\,\sigma^2 + b\,\sigma^1$, then the first equation gives $a\sigma^2 \wedge \sigma^2 + b\sigma^1 \wedge \sigma^2 = b\sigma^1 \wedge \sigma^2 = 0$, so $b = 0$. Hence $\omega^1{}_2 = a\,\sigma^2$.

From the second equation, $\cot\theta\,\sigma^1 \wedge \sigma^2 = \omega^1{}_2 \wedge \sigma^1 = a\,\sigma^2 \wedge \sigma^1 = -a\,\sigma^1 \wedge \sigma^2$. So $-a = \cot\theta$, i.e., $a = -\cot\theta$. Therefore $\omega^1{}_2 = -\cot\theta\,\sigma^2 = -\cot\theta\cdot\sin\theta\,d\varphi = -\cos\theta\,d\varphi$.

> [!note]- Derivation
> Set up the system using the antisymmetry. There is only one independent connection 1-form $\omega^1{}_2$ in 2D. The two first-structural-equation conditions (one for $a = 1$, one for $a = 2$) constrain it. The first ($a = 1$) gives a "form" constraint: $\omega^1{}_2 \wedge \sigma^2 = 0$, forcing $\omega^1{}_2 = $ a multiple of $\sigma^2$ (no $\sigma^1$ component). The second ($a = 2$) determines the multiple: $\omega^1{}_2 = -\cot\theta\,\sigma^2 = -\cos\theta\,d\varphi$. Both equations are satisfied; the solution is unique.

**Step 3: Apply Cartan's second structural equation.**

$\Omega^1{}_2 = d\omega^1{}_2 + \omega^1{}_c \wedge \omega^c{}_2$. The $\omega \wedge \omega$ piece: sum over $c = 1, 2$. $\omega^1{}_1 \wedge \omega^1{}_2 = 0$ (since $\omega^1{}_1 = 0$); $\omega^1{}_2 \wedge \omega^2{}_2 = 0$ (since $\omega^2{}_2 = 0$). So the entire $\omega \wedge \omega$ contribution vanishes.

$d\omega^1{}_2 = d(-\cos\theta\,d\varphi) = \sin\theta\,d\theta \wedge d\varphi + 0 = \sin\theta\,d\theta \wedge d\varphi$.

Express in orthonormal basis: $\sin\theta\,d\theta \wedge d\varphi = d\theta \wedge (\sin\theta\,d\varphi) = \sigma^1 \wedge \sigma^2$. So $\Omega^1{}_2 = \sigma^1 \wedge \sigma^2$.

> [!note]- Derivation
> $\omega^1{}_2 = -\cos\theta\,d\varphi$. By Leibniz, $d\omega^1{}_2 = d(-\cos\theta) \wedge d\varphi + (-\cos\theta) \wedge d(d\varphi) = \sin\theta\,d\theta \wedge d\varphi + 0 = \sin\theta\,d\theta \wedge d\varphi$. Rewriting in orthonormal basis ($\sigma^1 = d\theta, \sigma^2 = \sin\theta\,d\varphi$): $\sin\theta\,d\theta \wedge d\varphi = d\theta \wedge \sin\theta\,d\varphi = \sigma^1 \wedge \sigma^2$.
>
> For the $\omega \wedge \omega$ term: the connection matrix is $\omega = \begin{pmatrix}0 & \omega^1{}_2 \\ -\omega^1{}_2 & 0\end{pmatrix}$. Matrix product $\omega \wedge \omega$: $(1, 1)$ entry is $\omega^1{}_1 \wedge \omega^1{}_1 + \omega^1{}_2 \wedge \omega^2{}_1 = 0 + \omega^1{}_2 \wedge (-\omega^1{}_2) = -\omega^1{}_2 \wedge \omega^1{}_2 = 0$ (1-form wedged with itself is zero). $(1, 2)$ entry is $\omega^1{}_1 \wedge \omega^1{}_2 + \omega^1{}_2 \wedge \omega^2{}_2 = 0 + 0 = 0$. So $(\omega \wedge \omega)^1{}_2 = 0$. Hence $\Omega^1{}_2 = d\omega^1{}_2 = \sigma^1 \wedge \sigma^2$.

**Step 4: Read off the Gaussian curvature.**

In 2D, the curvature 2-form in an orthonormal frame has the form $\Omega^1{}_2 = K\sigma^1 \wedge \sigma^2$ where $K$ is the **Gaussian curvature**. From Step 3, $\Omega^1{}_2 = \sigma^1 \wedge \sigma^2$, so $K = 1$. ✓ (The unit 2-sphere has constant Gaussian curvature $1$ — as expected.)

> [!note]- Complete formal solution
> **Orthonormal coframe.** $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\,d\varphi$. Verify: $(\sigma^1)^2 + (\sigma^2)^2 = (d\theta)^2 + \sin^2\theta(d\varphi)^2 = g$ ✓.
>
> **Exterior derivatives.** $d\sigma^1 = 0$, $d\sigma^2 = \cos\theta\,d\theta \wedge d\varphi = \cot\theta\,\sigma^1 \wedge \sigma^2$.
>
> **Connection 1-form via first structural equation + antisymmetry.** In 2D the orthonormal-frame connection has one independent component $\omega^1{}_2$ (with $\omega^2{}_1 = -\omega^1{}_2$). The first structural equation $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ gives $\omega^1{}_2 \wedge \sigma^2 = 0$ (from $a = 1$) and $\omega^1{}_2 \wedge \sigma^1 = \cot\theta\,\sigma^1 \wedge \sigma^2$ (from $a = 2$, after antisymmetry). Solving: $\omega^1{}_2 = -\cot\theta\,\sigma^2 = -\cos\theta\,d\varphi$.
>
> **Curvature 2-form via second structural equation.** $\Omega^1{}_2 = d\omega^1{}_2 + \omega^1{}_c \wedge \omega^c{}_2 = d(-\cos\theta\,d\varphi) + 0 = \sin\theta\,d\theta \wedge d\varphi = \sigma^1 \wedge \sigma^2$ (the $\omega \wedge \omega$ term vanishes in 2D since $\omega^1{}_1 = \omega^2{}_2 = 0$).
>
> **Gaussian curvature.** $\Omega^1{}_2 = K\sigma^1 \wedge \sigma^2$ gives $K = 1$. The unit 2-sphere has constant Gaussian curvature $1$. $\blacksquare$

---

# Key Takeaways

**The Cartan structural equations are dramatically faster than the coordinate Christoffel approach.** Compare this computation (about 3 lines for the connection, 1 line for the curvature) with the coordinate computation in [[Ex - Christoffel Symbols of the Round Metric on the Sphere]] (about a page). The savings come from skipping the inverse-metric step, avoiding the cumbersome triple-sum in the Christoffel formula, and exploiting the antisymmetry of the orthonormal-frame connection 1-forms (which has only 1 independent entry in 2D instead of 6 Christoffel symbols). For higher-dimensional examples (e.g., Schwarzschild in 4D), the savings are even larger — the Cartan method has $n(n-1)/2 = 6$ independent connection 1-forms vs. $n^2(n+1)/2 = 40$ Christoffel symbols, and the curvature computation similarly compresses.

**Solve for $\omega$ from the structural equation + antisymmetry — this is a determinate system.** The combination of $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ (torsion-free) and $\omega^a{}_b + \omega^b{}_a = 0$ (metric-compatible in orthonormal frame) is exactly enough constraint to determine $\omega^a{}_b$ uniquely from $d\sigma^a$. The argument: $n^2$ unknowns ($\omega^a{}_b$ for each $a, b$, each a 1-form), with $n$ equations from torsion-free and $n(n+1)/2$ "diagonal/symmetric" antisymmetry conditions, leaving $n(n-1)/2$ independent unknowns — and $n$ structural-equation constraints determining them. The system is square (the residual $n$ constraints from torsion-free are exactly $n$ conditions on $n(n-1)/2$ unknowns, which is enough by a counting argument when one tracks degrees of freedom carefully). This determinate-system property is the operational content of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem]] in the moving-frame language.

**In 2D, $\omega \wedge \omega = 0$ automatically.** The orthonormal-frame connection matrix in 2D has the form $\omega = \begin{pmatrix}0 & \omega^1{}_2 \\ -\omega^1{}_2 & 0\end{pmatrix}$. Computing $\omega \wedge \omega$: the diagonal entries are $\pm\omega^1{}_2 \wedge \omega^1{}_2 = 0$ (any 1-form wedged with itself is zero); the off-diagonal entries involve $\omega^1{}_1$ or $\omega^2{}_2$, both zero. So in 2D the second structural equation reduces to $\Omega = d\omega$ — the "abelian" form. This is special to 2D; in higher [[Def - Dimension|dimensions]] the $\omega \wedge \omega$ piece is essential and is the source of the non-linearity of Yang-Mills theory. The 2D simplification reflects the fact that the structure [[Def - Group|group]] $\mathrm{SO}(2)$ is abelian.

**The Gaussian curvature is the entire local geometric content of a 2D Riemannian manifold.** In 2D, the Riemann curvature tensor has $\tfrac{n^2(n^2-1)}{12} = \tfrac{4 \cdot 3}{12} = 1$ independent component, which is exactly the Gaussian curvature $K$. There is no "sectional curvature" distinction or "Ricci-tensor versus Riemann-tensor" distinction in 2D — everything collapses to one scalar function $K$. This is why 2D Riemannian geometry is governed by a single scalar field, and why the Gauss-Bonnet theorem $\int_M K\,dA = 2\pi\chi(M)$ takes the simple "integrate the scalar curvature" form. In higher dimensions the curvature tensor has many more components, and one needs sectional curvatures, Ricci, and scalar to capture different aspects.

**This is the standard method for general relativity computations.** The orthonormal-frame Cartan approach is the standard technique in every general relativity textbook for computing the Christoffel symbols and Riemann tensor of nontrivial metrics — Schwarzschild, Kerr, FRW, de Sitter. See [[Ex - Computing Curvature 2-Forms in an Orthonormal Frame]] for the Schwarzschild calculation, which follows the same recipe and gives the spacetime curvatures needed to evaluate the Einstein field equations.
