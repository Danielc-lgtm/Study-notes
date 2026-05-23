---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - Riemannian Metric"
  - "Thm - Poincare-Hopf Theorem"
tags: [geometry, gauge-theory, curvature, sphere, Gauss-Bonnet]
---

# Problem Statement

Equip the unit sphere $S^2 \subset \mathbb{R}^3$ with the round metric $g = d\theta^2 + \sin^2\theta\,d\phi^2$ in spherical coordinates $(\theta, \phi)$ on (most of) $S^2$. Let $\nabla$ be the **Levi-Civita connection** on $TS^2$ — the unique torsion-free, metric-compatible connection.

**(a)** In the orthonormal frame $(e_\theta = \partial_\theta, e_\phi = \frac{1}{\sin\theta}\partial_\phi)$, compute the connection 1-form matrix $\omega = (\omega^\alpha{}_\beta)$.

**(b)** Compute the curvature 2-form matrix $F = (F^\alpha{}_\beta) = d\omega + \omega \wedge \omega$. Express it in terms of the area 2-form on $S^2$.

**(c)** Integrate the curvature over $S^2$ and verify the Gauss-Bonnet theorem: $\frac{1}{2\pi}\int_{S^2}F^\theta{}_\phi = \chi(S^2) = 2$ (with appropriate sign conventions).

**Recall:**

The **Levi-Civita connection** $\nabla$ on a Riemannian manifold $(M, g)$ is the unique connection on $TM$ satisfying (i) metric compatibility $\nabla g = 0$ and (ii) zero torsion $\nabla_X Y - \nabla_Y X = [X, Y]$. In an orthonormal frame $(e_a)$ with dual frame $(\theta^a)$, the **first structure equation** $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ determines $\omega$ uniquely, given the antisymmetry $\omega^a{}_b = -\omega^b{}_a$ (which follows from metric compatibility).

![[Def - Curvature of a Vector-Bundle Connection#The Definition]]

---

# Convergent Strategy

**Problem class:** This is a *concrete computation* of curvature on the simplest non-trivial closed 2-manifold. It illustrates the structure-equation method for finding the Levi-Civita connection 1-form in an orthonormal frame, then computes the curvature and integrates it to recover the Gauss-Bonnet theorem. The exercise serves as a bridge: from the abstract definition of curvature on a vector bundle to the concrete realization on the tangent bundle of a Riemannian surface, where curvature is *Gaussian curvature*.

**Assumption pattern:** The metric $g = d\theta^2 + \sin^2\theta\,d\phi^2$ is given explicitly. The orthonormal frame $(e_\theta, e_\phi)$ and its dual coframe $(\theta^1 = d\theta, \theta^2 = \sin\theta\,d\phi)$ are immediate. The first structure equation $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ together with the antisymmetry $\omega^1{}_2 = -\omega^2{}_1$ uniquely determines the connection 1-form. Computing $d\theta^a$ and matching gives $\omega^1{}_2 = -\cos\theta\,d\phi$.

**Theorem routing:** Compute $d\theta^a$ for each $a$, then solve $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ for the connection 1-form. Compute the curvature 2-form via the structure equation. For abelian holonomy (since $SO(2) = U(1)$ is abelian), $F = d\omega$ (the $\omega \wedge \omega$ term vanishes for $2 \times 2$ antisymmetric matrices wedged with themselves). Integrate the only independent component over $S^2$, matching $4\pi \cdot K$ with $K = +1$ the Gaussian curvature, hence $\int F = 4\pi = 2\pi\chi(S^2)$.

**Key decision point:** The non-obvious choice is to work in an *orthonormal* frame rather than the coordinate frame. In the coordinate frame $(\partial_\theta, \partial_\phi)$, the connection has *six* non-trivial Christoffel symbols $\Gamma^k{}_{ij}$ and the matrix $\omega^k{}_i = \Gamma^k{}_{ij}dx^j$ has off-diagonal asymmetries. In the orthonormal frame, the antisymmetry $\omega^1{}_2 = -\omega^2{}_1$ reduces the problem to a single 1-form (since the matrix has only two entries up to sign and the trace is zero), and the structure equation is much cleaner. *Always work in an orthonormal frame for surface-curvature calculations*.

---

# Legal Operations Used

1. **Choose a local trivialization (chart) and compute everything component-wise** (operation 1). Here the choice is the orthonormal frame $(e_\theta, e_\phi)$ adapted to the spherical metric. In this frame, the structure group reduces to $SO(2)$, and the matrix-valued forms have antisymmetric structure.

2. **Apply the curvature formula $F = d\omega + \omega \wedge \omega$** (operation 2). With $SO(2)$ abelian, $\omega \wedge \omega = 0$, so $F = d\omega$.

3. **Integrate the curvature over a closed surface to extract a Chern/Euler number** (operation 3). The integral $\frac{1}{2\pi}\int_{S^2}F^\theta{}_\phi$ gives an integer — here $\chi(S^2) = 2$.

---

# Hints

> [!note]- Hint 1
> Work in the orthonormal frame: $e_1 = \partial_\theta$, $e_2 = \frac{1}{\sin\theta}\partial_\phi$. The dual coframe is $\theta^1 = d\theta$, $\theta^2 = \sin\theta\,d\phi$.

> [!note]- Hint 2
> Use the **first structure equation** for the Levi-Civita connection: $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$, together with the antisymmetry $\omega^a{}_b = -\omega^b{}_a$ (consequence of metric compatibility on an orthonormal frame). Compute $d\theta^1 = 0$ and $d\theta^2 = \cos\theta\,d\theta \wedge d\phi$, then solve.

> [!note]- Hint 3
> The connection 1-form has only one independent component (the matrix is $2 \times 2$ antisymmetric): $\omega^1{}_2 = -\omega^2{}_1$. Solve for this single 1-form.

> [!note]- Hint 4
> For abelian structure groups like $SO(2)$, the term $\omega \wedge \omega = 0$ — entries are scalars and a scalar wedged with itself is zero. So $F = d\omega$.

> [!note]- Hint 5
> The area form on $S^2$ in spherical coordinates is $\mathrm{dA} = \sin\theta\,d\theta \wedge d\phi$, integrating to $\int_{S^2}\mathrm{dA} = 4\pi$. The Gaussian curvature of $S^2$ with the round metric is $K = +1$ everywhere, so $\int K\,\mathrm{dA} = 4\pi = 2\pi\chi(S^2)$, verifying Gauss-Bonnet.

---

# Solution

The proof has four steps. Step 1 sets up the orthonormal frame. Step 2 uses the first structure equation to find $\omega^1{}_2 = -\cos\theta\,d\phi$. Step 3 computes the curvature $F^1{}_2 = d\omega^1{}_2 = \sin\theta\,d\theta \wedge d\phi$. Step 4 integrates over $S^2$ to get $4\pi = 2\pi\chi(S^2)$, verifying Gauss-Bonnet.

**Step 1: Orthonormal frame and dual coframe.**

> [!note]- Derivation
> The metric is $g = d\theta^2 + \sin^2\theta\,d\phi^2$. The coordinate vectors $\partial_\theta, \partial_\phi$ have norms $|\partial_\theta| = 1$ and $|\partial_\phi| = \sin\theta$ (so $\partial_\phi$ has variable norm), and are orthogonal. To get an orthonormal frame:
> $$e_1 = e_\theta := \partial_\theta, \qquad e_2 = e_\phi := \frac{1}{\sin\theta}\partial_\phi.$$
>
> The dual coframe $(\theta^1, \theta^2)$ is determined by $\theta^a(e_b) = \delta^a_b$:
> $$\theta^1 = d\theta, \qquad \theta^2 = \sin\theta\,d\phi.$$
>
> Check: $\theta^1(e_1) = d\theta(\partial_\theta) = 1$, $\theta^2(e_2) = \sin\theta\,d\phi(\frac{1}{\sin\theta}\partial_\phi) = 1$, cross terms zero. ✓

**Step 2: Solve the first structure equation for $\omega^1{}_2$.**

> [!note]- Derivation
> The first structure equation $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ together with antisymmetry $\omega^1{}_2 = -\omega^2{}_1$ (and $\omega^1{}_1 = \omega^2{}_2 = 0$ for antisymmetric $2 \times 2$ matrices) gives:
>
> $d\theta^1 + \omega^1{}_2 \wedge \theta^2 = 0$
>
> $d\theta^2 + \omega^2{}_1 \wedge \theta^1 = 0$ (equivalently $d\theta^2 - \omega^1{}_2 \wedge \theta^1 = 0$)
>
> Compute:
> $$d\theta^1 = d(d\theta) = 0.$$
> $$d\theta^2 = d(\sin\theta\,d\phi) = \cos\theta\,d\theta \wedge d\phi.$$
>
> Plug into the equations:
> $$0 + \omega^1{}_2 \wedge \sin\theta\,d\phi = 0 \quad\Rightarrow\quad \omega^1{}_2 \wedge d\phi = 0 \text{ (modulo factor)},$$
> $$\cos\theta\,d\theta \wedge d\phi - \omega^1{}_2 \wedge d\theta = 0 \quad\Rightarrow\quad \omega^1{}_2 \wedge d\theta = \cos\theta\,d\theta \wedge d\phi.$$
>
> Write $\omega^1{}_2 = A\,d\theta + B\,d\phi$ for unknown smooth functions $A, B$. From the second equation:
> $$(A\,d\theta + B\,d\phi) \wedge d\theta = B\,d\phi \wedge d\theta = -B\,d\theta \wedge d\phi = \cos\theta\,d\theta \wedge d\phi.$$
> So $B = -\cos\theta$.
>
> From the first equation: $\omega^1{}_2 \wedge \sin\theta\,d\phi = (A\,d\theta + B\,d\phi) \wedge \sin\theta\,d\phi = A\sin\theta\,d\theta \wedge d\phi = 0$.
> So $A = 0$.
>
> Combining: $\omega^1{}_2 = -\cos\theta\,d\phi$, hence $\omega^2{}_1 = \cos\theta\,d\phi$. In matrix form:
> $$\omega = \begin{pmatrix} 0 & -\cos\theta\,d\phi \\ \cos\theta\,d\phi & 0 \end{pmatrix}.$$

**Step 3: Compute the curvature $F = d\omega + \omega \wedge \omega$.**

> [!note]- Derivation
> Since the structure group is $SO(2) \cong U(1)$ (abelian), the $\omega \wedge \omega$ term vanishes: $\omega^1{}_\gamma \wedge \omega^\gamma{}_2 = \omega^1{}_1 \wedge \omega^1{}_2 + \omega^1{}_2 \wedge \omega^2{}_2 = 0 \wedge \omega^1{}_2 + \omega^1{}_2 \wedge 0 = 0$.
>
> So $F = d\omega$. The single non-trivial component is:
> $$F^1{}_2 = d\omega^1{}_2 = d(-\cos\theta\,d\phi) = \sin\theta\,d\theta \wedge d\phi.$$
>
> In matrix form:
> $$F = \begin{pmatrix} 0 & \sin\theta\,d\theta \wedge d\phi \\ -\sin\theta\,d\theta \wedge d\phi & 0 \end{pmatrix}.$$
>
> Note: $\sin\theta\,d\theta \wedge d\phi$ is precisely the **area 2-form** of $S^2$, $\mathrm{dA}$. So $F^1{}_2 = K \cdot \mathrm{dA}$ where $K = +1$ is the Gaussian curvature.

**Step 4: Integrate and verify Gauss-Bonnet.**

> [!note]- Derivation
> Integrate $F^1{}_2$ over $S^2$:
> $$\int_{S^2}F^1{}_2 = \int_0^\pi\int_0^{2\pi}\sin\theta\,d\theta\,d\phi = 2\pi \cdot 2 = 4\pi.$$
>
> Compare with Gauss-Bonnet: $\int_M K\,\mathrm{dA} = 2\pi\chi(M)$. For $M = S^2$, $K = 1$, so $\int_{S^2}\mathrm{dA} = 4\pi = 2\pi\chi(S^2)$, giving $\chi(S^2) = 2$. ✓
>
> Equivalently, $\frac{1}{2\pi}\int_{S^2}F^1{}_2 = \frac{4\pi}{2\pi} = 2 = \chi(S^2)$. This is the **Euler number** of $TS^2$ computed from curvature, matching the topological Euler characteristic.

> [!note]- Complete formal solution
> **Setup.** On $S^2$ with the round metric $g = d\theta^2 + \sin^2\theta\,d\phi^2$, define the orthonormal frame $e_1 = \partial_\theta$, $e_2 = \frac{1}{\sin\theta}\partial_\phi$, with dual coframe $\theta^1 = d\theta$, $\theta^2 = \sin\theta\,d\phi$.
>
> **Connection 1-form.** Solve the first structure equation $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ with antisymmetry $\omega^a{}_b = -\omega^b{}_a$. Compute $d\theta^1 = 0$, $d\theta^2 = \cos\theta\,d\theta \wedge d\phi$. Writing $\omega^1{}_2 = A\,d\theta + B\,d\phi$, the equations give $A = 0$, $B = -\cos\theta$. Hence
> $$\omega^1{}_2 = -\cos\theta\,d\phi, \quad \omega^2{}_1 = +\cos\theta\,d\phi.$$
>
> **Curvature.** Since the structure group $SO(2)$ is abelian, $\omega \wedge \omega = 0$, so $F = d\omega$. The single non-trivial component:
> $$F^1{}_2 = d(-\cos\theta\,d\phi) = \sin\theta\,d\theta \wedge d\phi = K\,\mathrm{dA}$$
> with $K = +1$ the Gaussian curvature and $\mathrm{dA} = \sin\theta\,d\theta \wedge d\phi$ the area 2-form.
>
> **Gauss-Bonnet.** $\frac{1}{2\pi}\int_{S^2}F^1{}_2 = \frac{1}{2\pi}\int_{S^2}\sin\theta\,d\theta\,d\phi = \frac{4\pi}{2\pi} = 2 = \chi(S^2)$. $\blacksquare$

> [!warning] Illegal but tempting: forgetting the orthonormal-frame normalization
> If you use the coordinate frame $(\partial_\theta, \partial_\phi)$ directly, the connection 1-form has the form $\omega^k{}_i = \Gamma^k{}_{ij}dx^j$ with six non-trivial Christoffel symbols, and matters get messy. The orthonormal-frame computation is much cleaner because of the antisymmetry $\omega^a{}_b = -\omega^b{}_a$, which reduces the $2 \times 2$ matrix to a single 1-form. **Always work in an orthonormal frame for explicit Riemannian-curvature computations.**

---

# Key Takeaways

**The orthonormal-frame method is the cleanest way to compute Levi-Civita connections on surfaces.**

The trick is to introduce a frame in which the structure group reduces to $SO(2)$ (or $O(2)$ for non-orientable case), making the antisymmetry $\omega^a{}_b = -\omega^b{}_a$ explicit. The first structure equation $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ then becomes a system of equations with the antisymmetry as an algebraic constraint, easily solved for the few independent components. For a 2-surface, there is *one* independent connection 1-form (the $\omega^1{}_2$ component); for an $n$-surface, there are $\binom{n}{2}$ independent components. This method scales cleanly to higher dimensions and is the basis for Cartan's "moving-frame method".

**For abelian structure groups, $F = d\omega$ — the structure equation simplifies dramatically.**

The wedge of $\omega$ with itself vanishes for abelian groups ($SO(2)$, $U(1)$), so the curvature is *exact* in any patch where $\omega$ is well-defined. This makes the EM curvature $F = dA$ a particularly simple object — but the simplicity is *not generic*. For non-abelian gauge groups, the $\omega \wedge \omega$ term is non-zero and produces the *non-linear* nature of Yang-Mills theory. The contrast between Maxwell (linear, abelian) and Yang-Mills (non-linear, non-abelian) is precisely this term.

**Gauss-Bonnet relates local geometry to global topology, with the curvature integral as the bridge.**

The integral $\int_M K\,\mathrm{dA} = 2\pi\chi(M)$ is one of the most beautiful results in mathematics: a purely geometric quantity (integral of Gaussian curvature) equals a purely topological invariant (Euler characteristic). This exercise computes both sides directly for $S^2$ and confirms the equality. The general result for higher even-dimensional manifolds is the **Chern-Gauss-Bonnet theorem**, with the integrand being the *Pfaffian* of the curvature 2-form — a polynomial generalization of $K$. See [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] for the higher-dimensional version. The pattern "topological invariant = integral of a curvature polynomial" recurs throughout Chern-Weil theory and the Atiyah-Singer index theorem.

**Cross-link to companion exercise:** See [[Ex - Index of the Source-Sink Vector Field on the Sphere]] for the *Poincaré-Hopf* version of the same identity: $\chi(S^2) = 2$ computed via vector-field indices. Gauss-Bonnet and Poincaré-Hopf are *two* computations of the same integer, by genuinely different means (curvature integration vs. zero counting). Chern's intrinsic proof of Gauss-Bonnet provides the bridge between them — see [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]].
