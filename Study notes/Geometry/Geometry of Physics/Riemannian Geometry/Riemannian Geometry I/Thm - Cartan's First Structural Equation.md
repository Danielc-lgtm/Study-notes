---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Connection 1-Forms (Cartan)"
  - "Def - Torsion Tensor"
  - "Def - Local Frame"
  - "Def - Exterior Derivative on a Manifold"
tags: [geometry, riemannian-geometry, connections, cartan-formalism]
---

# Notation

$(M, \nabla)$ — smooth manifold with affine connection on $TM$. $e = (e_a)$ — local frame; $\sigma^a$ — dual coframe with $\sigma^a(e_b) = \delta^a_b$. $\omega^a{}_b$ — [[Def - Connection 1-Forms (Cartan)|connection 1-forms]] in the frame, $\nabla e_b = e_a \otimes \omega^a{}_b$. $\tau^a$ — torsion 2-forms, $\tau^a = \tfrac{1}{2}T^a_{bc}\sigma^b \wedge \sigma^c$ with $T(e_b, e_c) = T^a_{bc}e_a$. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Statement

> **Theorem (Cartan's First Structural Equation).** Let $(M, \nabla)$ be a smooth manifold with affine connection on $TM$. In any local frame $(e_a)$ with dual coframe $(\sigma^a)$ and connection 1-forms $\omega^a{}_b$, the exterior derivative of $\sigma^a$ satisfies
> $$
> d\sigma^a + \omega^a{}_b \wedge \sigma^b = \tau^a,
> $$
> where $\tau^a = \tfrac{1}{2}T^a_{bc}\sigma^b \wedge \sigma^c$ are the **torsion 2-forms** of $\nabla$ in the frame.
>
> In particular, the connection is **torsion-free** if and only if
> $$
> d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0
> $$
> in every frame.

---

# Motivation

Cartan's first structural equation packages the data of the connection 1-forms and the torsion into a single identity involving the exterior derivative of the coframe. This is the **moving-frame** language for connections, in which the basic objects are differential forms (which transform predictably under change of frame and have the full power of the exterior calculus) rather than coordinate-frame Christoffel symbols.

The motivation is twofold. First, the equation provides a **calculation engine**: given the coframe $\sigma^a$ of an orthonormal (or other natural) frame, the exterior derivatives $d\sigma^a$ are usually short to compute. The first structural equation then *determines* the connection 1-forms $\omega^a{}_b$ from $d\sigma^a$ alone, in conjunction with metric-compatibility ($\omega^a{}_b + \omega^b{}_a = 0$ in an orthonormal frame). This is dramatically faster than the coordinate Christoffel formula for most concrete metrics — see [[Ex - Cartan Structural Equations on S^2]] and [[Ex - Computing Curvature 2-Forms in an Orthonormal Frame]].

Second, the equation has a clean **geometric content**: it says that the failure of $d\sigma^a$ to vanish in the "connection-corrected" form $d\sigma^a + \omega^a{}_b \wedge \sigma^b$ is exactly the torsion. For torsion-free connections, $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ is a strong constraint linking the connection to the coframe — and on a coordinate frame where $\sigma^a = dx^a$, $d\sigma^a = 0$ automatically and the equation $\omega^a{}_b \wedge \sigma^b = 0$ gives the symmetry of the Christoffel symbols.

The equation generalises: for a connection on an arbitrary vector bundle, there is no "soldering form" identifying the bundle with $TM$, so there is no torsion. The first structural equation is therefore *specific* to the tangent bundle. The second structural equation [[Thm - Cartan's Second Structural Equation]] for curvature generalises to any vector bundle.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: any connection on $TM$ presented in a local frame.* The first structural equation always holds — it is a *definition-equivalent* identity, not a conditional theorem. The bridge: whenever you have a connection and a frame, the equation $d\sigma^a + \omega^a{}_b \wedge \sigma^b = \tau^a$ relates the three objects.

*Source 2: an orthonormal coframe on a Riemannian manifold + metric-compatibility.* In an orthonormal frame, metric-compatibility forces antisymmetry $\omega^a{}_b + \omega^b{}_a = 0$. Combined with torsion-freeness (giving $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$), the first structural equation becomes a *determining* equation for $\omega^a{}_b$ from $d\sigma^a$ alone. The bridge: "Riemannian metric + orthonormal coframe + torsion-free + metric-compatible" → first structural equation determines $\omega$.

*Source 3: a coframe on a Lie group of left-invariant 1-forms.* On a Lie group $G$, the Maurer-Cartan structural equations $d\sigma^a + \tfrac{1}{2}c^a_{bc}\sigma^b \wedge \sigma^c = 0$ (with $c^a_{bc}$ the structure constants of $\mathfrak{g}$) are a special case of the first structural equation for the connection $\nabla \equiv 0$ on left-invariant frames — with torsion $\tau^a = -\tfrac{1}{2}c^a_{bc}\sigma^b \wedge \sigma^c$. This is the connection-theoretic content of the Maurer-Cartan equation, and it is the input to the [[Ex - The Tangent Bundle of a Lie Group has a Canonical Flat Connection|Weitzenböck connection example]].

**Targets (Output Amplification)**

*Target combination 1: First structural equation + antisymmetry (metric-compatibility) ⟹ explicit formula for $\omega^a{}_b$.* In an orthonormal frame with torsion-free connection, the system $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ together with $\omega^a{}_b + \omega^b{}_a = 0$ has a unique solution for $\omega^a{}_b$, found by direct algebraic manipulation. This is the fast method for computing the Levi-Civita connection in practice.

*Target combination 2: First structural equation + integration ⟹ holonomy around a loop.* The first structural equation can be integrated around a loop $\gamma$: $\oint_\gamma \sigma^a = \int_{\partial D} \sigma^a = \int_D d\sigma^a = -\int_D \omega^a{}_b \wedge \sigma^b + \int_D \tau^a$. For a torsion-free connection on a flat manifold, this reduces to a relation between the loop's "displacement" and the integrated connection 1-forms.

*Target combination 3: First structural equation + Bianchi identity ⟹ constraints on torsion.* Exterior-differentiating Cartan's first structural equation gives $d\tau^a - d\omega^a{}_b \wedge \sigma^b + \omega^a{}_b \wedge d\sigma^b = 0$. Substituting $d\omega = \Omega - \omega \wedge \omega$ (from Cartan's second structural equation) and $d\sigma^b = \tau^b - \omega^b{}_c \wedge \sigma^c$, after simplification one gets the **first Bianchi identity** $d\tau^a + \omega^a{}_b \wedge \tau^b = \Omega^a{}_b \wedge \sigma^b$. For torsion-free connections, $\tau^a = 0$ and this becomes $\Omega^a{}_b \wedge \sigma^b = 0$, the algebraic Bianchi identity $R^a{}_{[bcd]} = 0$.

---

# Why Is It True

**Mechanism summary:** **the first structural equation is the dual statement of the connection: $\sigma^a$ measures coordinates in the frame $e$; $d\sigma^a$ measures how those coordinates change; $\omega^a{}_b \wedge \sigma^b$ measures the change due to the rotation of the frame itself; the remainder is the torsion.**

The intuition. The 1-forms $\sigma^a$ are dual to the frame: $\sigma^a(X) = X^a$ is the $a$-th component of $X$ in the frame. The exterior derivative $d\sigma^a$ measures the rate of change of this "componentisation" as you move. There are two reasons the components might change: (i) the vector field $X$ itself changes; (ii) the frame $e_a$ in which we measure the components rotates. The first effect contributes via $d X^a = d\sigma^a(X) +$ derivative terms; the second effect is the connection. Combining: $d\sigma^a + \omega^a{}_b \wedge \sigma^b$ subtracts off the rotation of the frame, leaving only the "intrinsic" change of the dual coframe, which is exactly the torsion 2-form $\tau^a$.

Equivalently, in the coordinate-free formulation: $\tau(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$ is the torsion vector field, and $\sigma^a(\tau(X, Y)) = T^a_{bc}X^b Y^c$. On the other hand, by the formula for the exterior derivative of a 1-form, $d\sigma^a(X, Y) = X\sigma^a(Y) - Y\sigma^a(X) - \sigma^a([X, Y]) = X(Y^a) - Y(X^a) - \sigma^a([X, Y])$. Adding $\omega^a{}_b \wedge \sigma^b(X, Y) = \omega^a{}_b(X)Y^b - \omega^a{}_b(Y)X^b = \sigma^a(\nabla_X(Y^b e_b) - Y^b\nabla_X e_b \text{ correction}) ...$ the calculation works out: the LHS $d\sigma^a + \omega \wedge \sigma$ evaluated on $(X, Y)$ equals $\sigma^a(\nabla_X Y - \nabla_Y X - [X, Y]) = T^a_{bc}X^b Y^c$, which is $\tau^a(X, Y)$. So the equation is the dual statement of the torsion definition, packaged in form language.

---

# What Makes This Hard

The conceptual difficulty is **seeing why $d\sigma^a + \omega^a{}_b \wedge \sigma^b$ has the right sign and structure to equal the torsion**. The intuition "exterior derivative of the coframe minus the connection-induced change" is right, but the *sign* of the $\omega$ term is the conventional one that comes from how one defines the connection on the dual frame (covectors transform with a minus sign relative to vectors). Different sign conventions in different textbooks (especially Frankel vs. Lee vs. do Carmo) can confuse: the convention used here is the standard one (positive sign in $\nabla e_b = \omega^a{}_b\,e_a$).

The mechanical hard part is **verifying the equation in coordinates and in non-coordinate frames**. In a coordinate frame the equation is essentially trivial ($d(dx^a) = 0$, so $\omega^a{}_b \wedge dx^b = -\tau^a$, equivalently $\Gamma^a_{jb}dx^j \wedge dx^b = -\tfrac{1}{2}T^a_{jb}dx^j \wedge dx^b$, giving $\Gamma^a_{[jb]} = -\tfrac{1}{2}T^a_{jb}$, equivalently $T^a_{jb} = \Gamma^a_{jb} - \Gamma^a_{bj}$ — the standard formula). In a general frame, $d\sigma^a$ is nontrivial (it picks up structure-function corrections $-\tfrac{1}{2}c^a_{bc}\sigma^b \wedge \sigma^c$), and the calculation must track all the corrections carefully.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute $d\sigma^a(X, Y)$ using the coordinate-free formula for $d$, evaluate $\omega^a{}_b \wedge \sigma^b$ on $(X, Y)$ using the connection axioms, and show the sum equals $\tau^a(X, Y)$.

**Subgoal decomposition:**

1. **Expand $d\sigma^a(X, Y)$.** Use the formula $d\eta(X, Y) = X(\eta(Y)) - Y(\eta(X)) - \eta([X, Y])$ for a 1-form $\eta$, applied to $\eta = \sigma^a$. Get $d\sigma^a(X, Y) = X\sigma^a(Y) - Y\sigma^a(X) - \sigma^a([X, Y])$.
   - *Hint:* Standard coordinate-free identity for $d$ on 1-forms.
   - *Why needed:* This is the LHS contribution.

2. **Expand $(\omega^a{}_b \wedge \sigma^b)(X, Y)$.** Use $(\alpha \wedge \beta)(X, Y) = \alpha(X)\beta(Y) - \alpha(Y)\beta(X)$ to get $\omega^a{}_b(X)\sigma^b(Y) - \omega^a{}_b(Y)\sigma^b(X)$. Recognize $\omega^a{}_b(X)\sigma^b(Y) = \sigma^a(\omega^c{}_b(X)Y^b e_c) = \sigma^a(\nabla_X Y - X\text{-componentwise derivative})$... actually use that $\nabla_X Y = X(Y^a)e_a + Y^b \omega^a{}_b(X)e_a$, so $\omega^a{}_b(X)Y^b = \sigma^a(\nabla_X Y) - X(Y^a)$, equivalently $\sigma^a(\nabla_X Y) = X(Y^a) + \omega^a{}_b(X)Y^b$.
   - *Hint:* Use the formula for $\nabla_X Y$ in terms of $\omega$.
   - *Why needed:* This is the second LHS contribution.

3. **Combine and identify the torsion.** Putting (1) and (2) together: $(d\sigma^a + \omega^a{}_b \wedge \sigma^b)(X, Y) = X\sigma^a(Y) - Y\sigma^a(X) - \sigma^a([X, Y]) + \omega^a{}_b(X)\sigma^b(Y) - \omega^a{}_b(Y)\sigma^b(X) = [X(Y^a) + \omega^a{}_b(X)Y^b] - [Y(X^a) + \omega^a{}_b(Y)X^b] - \sigma^a([X, Y]) = \sigma^a(\nabla_X Y) - \sigma^a(\nabla_Y X) - \sigma^a([X, Y]) = \sigma^a(\nabla_X Y - \nabla_Y X - [X, Y]) = \sigma^a(\tau(X, Y)) = \tau^a(X, Y)$.
   - *Hint:* The $\sigma^a$ "extracts the $a$-th component" and converts torsion vector to torsion 2-form value.
   - *Why needed:* Concludes the equation.

---

# Lemma Decomposition

> [!note]- Lemma 1: The coordinate-free formula for $d$ on a 1-form
> **Statement:** For any 1-form $\eta \in \Omega^1(M)$ and vector fields $X, Y \in \mathfrak{X}(M)$, $d\eta(X, Y) = X(\eta(Y)) - Y(\eta(X)) - \eta([X, Y])$.
>
> **Hint:** This is a standard identity, derivable by writing $\eta = \eta_i\,dx^i$ in coordinates and computing both sides.
>
> **Why needed:** This is the formula that expands $d\sigma^a(X, Y)$ in step 1 of the proof.
>
> > [!note]- Full proof
> > Standard. See [[Differential Geometry VIII — Differential Forms]] or any differential-geometry text. The formula is exterior-derivative's invariant characterisation on 1-forms.

> [!note]- Lemma 2: $\sigma^a(\nabla_X Y) = X(Y^a) + \omega^a{}_b(X)Y^b$
> **Statement:** For any frame $e$, dual coframe $\sigma$, vector field $Y = Y^b e_b$, and vector field $X$, the $a$-th component of $\nabla_X Y$ in the frame $e$ is $\sigma^a(\nabla_X Y) = X(Y^a) + \omega^a{}_b(X)Y^b$.
>
> **Hint:** Apply $\nabla_X$ to $Y = Y^b e_b$ using Leibniz and the definition $\nabla_X e_b = \omega^a{}_b(X)e_a$.
>
> **Why needed:** This is the formula that converts $\omega^a{}_b(X)Y^b$ into a component of $\nabla_X Y$, used in step 2 of the proof.
>
> > [!note]- Full proof
> > $\nabla_X Y = \nabla_X(Y^b e_b) = X(Y^b)e_b + Y^b \nabla_X e_b = X(Y^b)e_b + Y^b \omega^c{}_b(X)e_c$. Relabel the second sum's dummy index $c \to a$: $\nabla_X Y = (X(Y^a) + \omega^a{}_b(X)Y^b)e_a$. Hence $\sigma^a(\nabla_X Y) = X(Y^a) + \omega^a{}_b(X)Y^b$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X, Y \in \mathfrak{X}(M)$. Compute both sides of $d\sigma^a + \omega^a{}_b \wedge \sigma^b = \tau^a$ evaluated on $(X, Y)$.
>
> **LHS, first term.** By Lemma 1, $d\sigma^a(X, Y) = X(\sigma^a(Y)) - Y(\sigma^a(X)) - \sigma^a([X, Y]) = X(Y^a) - Y(X^a) - \sigma^a([X, Y])$, where $X^a = \sigma^a(X)$, $Y^a = \sigma^a(Y)$.
>
> **LHS, second term.** $(\omega^a{}_b \wedge \sigma^b)(X, Y) = \omega^a{}_b(X)\sigma^b(Y) - \omega^a{}_b(Y)\sigma^b(X) = \omega^a{}_b(X)Y^b - \omega^a{}_b(Y)X^b$.
>
> **Sum.** $d\sigma^a(X, Y) + (\omega^a{}_b \wedge \sigma^b)(X, Y) = [X(Y^a) + \omega^a{}_b(X)Y^b] - [Y(X^a) + \omega^a{}_b(Y)X^b] - \sigma^a([X, Y])$.
>
> By Lemma 2, the first bracket is $\sigma^a(\nabla_X Y)$ and the second bracket is $\sigma^a(\nabla_Y X)$. So
> $$
> (d\sigma^a + \omega^a{}_b \wedge \sigma^b)(X, Y) = \sigma^a(\nabla_X Y) - \sigma^a(\nabla_Y X) - \sigma^a([X, Y]) = \sigma^a(\nabla_X Y - \nabla_Y X - [X, Y]) = \sigma^a(T(X, Y)) = \tau^a(X, Y),
> $$
> where the last equality is the definition of the torsion 2-form $\tau^a$ as the $\sigma^a$-component of the torsion tensor $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$. $\blacksquare$
>
> **Corollary (torsion-free case).** When $\nabla$ is torsion-free, $\tau^a \equiv 0$ and the equation becomes $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$, which can be used to *solve* for the connection 1-forms from the coframe.

---

# Cross-Field Exercise Suggestions

**1. Compute the connection 1-forms of the round 2-sphere.** Using the orthonormal coframe $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\,d\varphi$, compute $d\sigma^1 = 0$ and $d\sigma^2 = \cos\theta\,d\theta \wedge d\varphi = \cot\theta\,\sigma^1 \wedge \sigma^2$. Applying the first structural equation (torsion-free) with antisymmetry $\omega^1{}_2 = -\omega^2{}_1$, solve for $\omega^1{}_2 = -\cos\theta\,d\varphi$. See [[Ex - Cartan Structural Equations on S^2]].

**2. Compute the connection 1-forms of the Schwarzschild metric.** Using the orthonormal coframe $\sigma^0 = f^{1/2}dt$, $\sigma^1 = f^{-1/2}dr$, $\sigma^2 = r\,d\theta$, $\sigma^3 = r\sin\theta\,d\varphi$ for $f = 1 - 2M/r$, compute the $d\sigma^a$ and solve the first structural equation with antisymmetry for the $\omega^a{}_b$. This is the standard computation in general relativity. See [[Ex - Computing Curvature 2-Forms in an Orthonormal Frame]].

**3. The Maurer-Cartan equation as a special case.** On a Lie [[Def - Group|group]] $G$ with left-invariant frame $(e_a)$ and dual coframe $(\sigma^a)$, the Maurer-Cartan equation is $d\sigma^a + \tfrac{1}{2}c^a_{bc}\sigma^b \wedge \sigma^c = 0$, where $c^a_{bc}$ are the structure constants of $\mathfrak{g}$. Show that this is exactly the first structural equation for the Weitzenböck connection $\nabla \equiv 0$ on left-invariant frames, with torsion $\tau^a = -\tfrac{1}{2}c^a_{bc}\sigma^b \wedge \sigma^c$. (Frankel exercise.)

**4. Pseudo-Riemannian first structural equation.** Verify the first structural equation holds verbatim for connections on $TM$ with pseudo-Riemannian (e.g., Lorentzian) metric. The proof uses only the connection axioms and the definition of torsion — not positive-definiteness — so the same identity holds in Lorentzian signature, with the same solution method via antisymmetry under $\eta_{ab}$ instead of $\delta_{ab}$.

---

# Bridges

- **[[Thm - Cartan's Second Structural Equation]]** — The two structural equations together encode the entire content of a connection in the moving-frame language. The first encodes torsion (and, for torsion-free connections, allows computation of $\omega$ from $\sigma$); the second encodes curvature ($\Omega = d\omega + \omega \wedge \omega$). Exterior-differentiating each gives the Bianchi identities.

- **[[Thm - Koszul Formula]]** — Both Koszul and Cartan's first structural equation determine the Levi-Civita connection from the metric, by different routes. The Koszul formula is invariant (frame-independent); the first structural equation is in a chosen frame. They are equivalent characterisations and one can convert between them in either direction.

- **The Maurer-Cartan equation on a Lie group** — On a Lie group, the left-invariant coframe satisfies $d\sigma^a + \tfrac{1}{2}c^a_{bc}\sigma^b \wedge \sigma^c = 0$ (the Maurer-Cartan equation). Reading this as the first structural equation for the Weitzenböck connection identifies the Maurer-Cartan structure constants as the torsion of that connection. This is the bridge from Lie-group theory to the moving-frame formalism.

- **The soldering form on the frame bundle** — On the principal $\mathrm{GL}(n)$-bundle of frames $\mathrm{Fr}(M)$, there is a canonical $\mathbb{R}^n$-valued 1-form $\theta$ (the soldering form) that identifies tangent vectors to $M$ with their components in any frame. Cartan's first structural equation in the principal-bundle formulation is $d\theta + \omega \wedge \theta = \tau$ on the total space, with $\omega$ the principal connection 1-form and $\tau$ the torsion 2-form. This is the bridge to [[Gauge Theory IV — Connections and Curvature on Principal Bundles|principal-bundle connections]] and gauge theory.

---

# Unlocked by This

> [!tip] The Practical Algorithm for Computing the Levi-Civita Connection *(from Riemannian Geometry)*
> Combined with metric-compatibility (antisymmetry of $\omega$ in an orthonormal frame), the first structural equation provides the fastest practical algorithm for computing the Levi-Civita connection of any concrete Riemannian or Lorentzian metric:
> 1. Set up an orthonormal coframe $\sigma^a$ for the metric.
> 2. Compute $d\sigma^a$ — usually short due to the structure of the chosen coframe.
> 3. Solve $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ for $\omega^a{}_b$ subject to $\omega^a{}_b = -\omega^b{}_a$.
> 4. Use Cartan's second structural equation $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$ to compute the curvature 2-forms.
>
> This is the route used in every general-relativity textbook for computing the Riemann tensor of any nontrivial metric (Schwarzschild, Kerr, FRW, de Sitter, Reissner-Nordström). It is dramatically faster than the coordinate Christoffel-symbol approach for any metric beyond the trivial.

> [!tip] The First Bianchi Identity *(from Riemannian Geometry)*
> Exterior-differentiating Cartan's first structural equation and using the second structural equation gives the **first Bianchi identity** in differential-form language: $d\tau^a + \omega^a{}_b \wedge \tau^b = \Omega^a{}_b \wedge \sigma^b$. For torsion-free connections this reduces to $\Omega^a{}_b \wedge \sigma^b = 0$, which in components is the algebraic Bianchi identity $R^a{}_{[bcd]} = 0$. This is one of the key algebraic symmetries of the Riemann tensor.
