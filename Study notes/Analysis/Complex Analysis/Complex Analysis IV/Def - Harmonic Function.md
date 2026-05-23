---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Thm - Cauchy–Riemann Equations"
tags: [analysis, complex-analysis, pde]
---

# Notation

$U \subseteq \mathbb{R}^2 \cong \mathbb{C}$ is an open set, $u : U \to \mathbb{R}$ is a real-valued function of two variables (or equivalently of one complex variable). The Laplacian is $\Delta u = u_{xx} + u_{yy} = \partial^2 u/\partial x^2 + \partial^2 u/\partial y^2$. The full registry lives on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Axiom Motivation

A function is **harmonic** if it satisfies Laplace's equation $\Delta u = 0$. Why is this specific second-order PDE singled out for a name?

Several reasons converge:

**Physically, harmonic functions describe equilibrium states.** A harmonic function is one whose value at any point equals the *average* of its values on any surrounding circle (the **mean value property**). Equivalently, the function has no "local sources" or "local sinks" — it's perfectly balanced. This matches the physical situation of:
- Electrostatic potential in a charge-free region;
- Steady-state temperature in a region with no heat sources;
- Steady incompressible inviscid flow's velocity potential and stream function;
- The shape of a stretched membrane with no transverse forces.

**Mathematically, harmonic functions are the "imaginary half" of holomorphic functions.** If $f = u + iv$ is holomorphic, then $u$ and $v$ are both harmonic (by Cauchy-Riemann: $u_{xx} = v_{yx} = v_{xy} = -u_{yy}$, so $u_{xx} + u_{yy} = 0$; similarly for $v$). Conversely, on a simply connected domain, every harmonic $u$ is the real part of some holomorphic $f$ — the **harmonic conjugate** $v$ exists, unique up to additive constants.

This $u \leftrightarrow$ holomorphic connection means harmonic functions inherit all the rigidity of holomorphic ones. They are real-analytic, satisfy maximum/minimum principles, have unique continuation, and are determined by boundary values on any closed curve (the Dirichlet problem). All of these are facts about holomorphic functions translated to real-variable language.

**The Laplacian $\Delta = \partial_x^2 + \partial_y^2$ is the unique (up to scaling) rotation-invariant second-order linear differential operator.** Any other second-order linear operator like $a u_{xx} + 2b u_{xy} + c u_{yy}$ with $b \neq 0$ would not be rotation-invariant, and would have eigenstructure that depends on direction. Asking for "function whose averaging over rotations matches its centre value" forces $\Delta = 0$.

What would break with a different definition?

- Defining "harmonic" as $u_{xx} = 0$ alone: would give "linear in $x$", not the right notion.
- Defining as $u_{xx} - u_{yy} = 0$: would give the *wave equation* in 2D space-time, a different theory (hyperbolic, not elliptic).
- Defining as $\Delta u =$ a nonzero source: gives the Poisson equation, useful but not "harmonic".

The Laplace equation $\Delta u = 0$ is the unique condition that simultaneously characterizes equilibrium, encodes the real part of holomorphic functions, and gives the right rigidity properties for the theory.

---

# The Definition

Let $U \subseteq \mathbb{R}^2 \cong \mathbb{C}$ be open.

A function $u : U \to \mathbb{R}$ is **harmonic** on $U$ if:
1. $u \in C^2(U)$ (twice continuously differentiable);
2. $\Delta u = u_{xx} + u_{yy} = 0$ on $U$.

**Complex notation.** Writing $z = x + iy, \bar z = x - iy$, the operator $\Delta$ factors as $\Delta = 4 \partial^2/(\partial z \partial\bar z)$. So $u$ is harmonic iff $\partial^2 u/(\partial z \partial \bar z) = 0$ — equivalently, $\partial u/\partial \bar z$ is holomorphic in $z$ (or $\partial u/\partial z$ is anti-holomorphic).

**Harmonic conjugate.** A function $v : U \to \mathbb{R}$ is a **harmonic conjugate** of $u$ if $f = u + iv$ is holomorphic on $U$. By Cauchy-Riemann: $u_x = v_y, u_y = -v_x$. On a simply connected $U$, every harmonic $u$ has a harmonic conjugate $v$, unique up to additive constants.

---

# Relate to Other Fields / Compression

A harmonic function is the **time-independent (steady-state) solution** of the heat equation $\partial_t u = \Delta u$. Setting $\partial_t u = 0$ gives $\Delta u = 0$. So harmonic functions describe heat distributions that are not changing in time — equilibrium states.

A harmonic function on a 2D domain is the **velocity potential of a 2D incompressible, irrotational flow**. The velocity field $v = \nabla\phi$ derives from the potential; incompressibility ($\nabla \cdot v = 0$) gives $\Delta\phi = 0$. The **stream function** is the harmonic conjugate.

In **probability**, a harmonic function on $U$ has the property that for a Brownian motion $B_t$ started at $z \in U$ and stopped at the first exit time $\tau$ from $U$: $u(z) = \mathbb{E}_z[u(B_\tau)]$. This is the **probabilistic representation of the Dirichlet problem**: $u$ is the expected value at exit, given that it solves Laplace's equation with boundary values prescribed on $\partial U$.

In **PDE**, harmonic functions are the prototype of **elliptic PDE solutions**: smooth, satisfying maximum principles, with unique continuation. The theory of elliptic operators is a generalization of the Laplacian's theory.

In **algebraic geometry**, harmonic functions are real parts of holomorphic functions, which on a Riemann surface correspond to **half** of a (holomorphic) cohomology class. The Hodge theory of compact Riemann surfaces decomposes the cohomology into holomorphic and anti-holomorphic parts.

---

# Examples / Corollaries

**Is an instance — $u(x, y) = x$.** Linear in $x$; $u_{xx} = 0, u_{yy} = 0$, sum zero. Harmonic. The harmonic conjugate is $v(x, y) = y$: $u + iv = x + iy = z$, holomorphic.

**Is an instance — $u(x, y) = x^2 - y^2$.** $u_{xx} = 2, u_{yy} = -2$, sum zero. Harmonic. Harmonic conjugate: $v(x, y) = 2xy$. Check: $u + iv = x^2 - y^2 + 2ixy = (x + iy)^2 = z^2$, holomorphic.

**Is an instance — $u(x, y) = e^x \cos y$.** $u_{xx} = e^x \cos y, u_{yy} = -e^x \cos y$, sum zero. Harmonic. Harmonic conjugate: $v(x, y) = e^x \sin y$. Check: $u + iv = e^x(\cos y + i\sin y) = e^z$, holomorphic.

**Is an instance — $u(x, y) = \log\sqrt{x^2 + y^2} = \log|z|$.** Harmonic on $\mathbb{C}\setminus\{0\}$. Check: $u_x = x/(x^2 + y^2), u_{xx} = (y^2 - x^2)/(x^2 + y^2)^2$, similarly $u_{yy} = (x^2 - y^2)/(x^2 + y^2)^2$, sum is zero.

The harmonic conjugate of $\log|z|$ on the simply connected domain $\mathbb{C}\setminus(-\infty, 0]$ is $\arg z$. On the full $\mathbb{C}\setminus\{0\}$, the conjugate $\arg z$ is multi-valued — *no global harmonic conjugate exists*, because $\mathbb{C}\setminus\{0\}$ is not simply connected.

**Is NOT an instance — $u(x, y) = x^2 + y^2$.** $u_{xx} + u_{yy} = 2 + 2 = 4 \neq 0$. Not harmonic. (This is $|z|^2$, which solves $\Delta u = 4$.)

**Is NOT an instance — $u(x, y) = \operatorname{Re}(z\bar z) = |z|^2$.** Same as above, not harmonic.

**Is NOT an instance — $u(x, y) = |x|$.** Not $C^2$ at $x = 0$. (Fails regularity, even if formally $u_{xx} = 0$ where defined.)

**Corollary — sum of harmonic is harmonic.** $\Delta$ is linear, so if $u, v$ are harmonic, so is $au + bv$ for any $a, b \in \mathbb{R}$.

**Corollary — composition with conformal maps preserves harmonicity.** If $u$ is harmonic on $V$ and $f : U \to V$ is conformal (holomorphic with $f' \neq 0$), then $u \circ f$ is harmonic on $U$. This is the key fact behind conformal-map techniques for Laplace's equation.

**Corollary — mean value property.** A harmonic function $u$ on $D(a, R)$ satisfies $u(a) = (1/(2\pi))\int_0^{2\pi} u(a + re^{i\theta})\,d\theta$ for any $0 < r < R$ — value at the centre equals the average on a surrounding circle.

**Calibration check.** Verify that $u(x, y) = x^2 - y^2$ is harmonic by computing $u_{xx} = 2$ and $u_{yy} = -2$, then identify it as $\operatorname{Re}(z^2)$ to find the harmonic conjugate $v = 2xy$. Verify that $u = x^2 + y^2 = |z|^2$ is *not* harmonic ($\Delta u = 4$), and that the failure traces to $|z|^2 = z \bar z$ having both holomorphic and antiholomorphic parts. And verify that $\log|z|$ is harmonic on $\mathbb{C} \setminus \{0\}$ but has no *global* harmonic conjugate, because $\arg z$ is multi-valued — the obstruction is exactly the non-simply-connectedness of the punctured plane.

---

# Unlocked by This

> [!tip] Real-Part of Holomorphic on Simply Connected *(from §3.6+)*
> The fundamental equivalence: harmonic on simply connected $U$ ⟺ real part of holomorphic. See [[Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)]].

> [!tip] Mean Value and Maximum Principle *(from §3.6+)*
> Harmonic functions satisfy [[Thm - Mean Value Property of Harmonic Functions|mean value]] and [[Thm - Maximum Principle for Harmonic Functions|maximum principle]] — direct consequences of being the real part of holomorphic functions.

> [!tip] Dirichlet Problem and Poisson Kernel *(from §3.6+)*
> Given boundary values on $\partial \mathbb{D}$, the [[Thm - Poisson Integral Formula|Poisson integral formula]] reconstructs the unique harmonic extension to the interior. This solves the Dirichlet problem on the disc.

> [!tip] Subharmonic Functions and Plurisubharmonic *(from PDE)*
> Generalizing harmonic to **subharmonic** ($\Delta u \geq 0$) gives a vast theory with applications to potential theory, complex analysis in several variables, and PDE.

> [!tip] Heat Equation and Stochastic Calculus *(from Probability)*
> Harmonic functions are the steady states of the heat equation, and have a probabilistic interpretation via Brownian motion exit-value formulas.
