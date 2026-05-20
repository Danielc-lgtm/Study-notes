---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is open; $f : U \to \mathbb{C}$ is a complex-valued function of a complex variable. The complex derivative at $w \in U$, when it exists, is denoted $f'(w) \in \mathbb{C}$. We write $f = u + iv$ with $u, v : U \to \mathbb{R}$ the real and imaginary parts (viewing $U \subseteq \mathbb{R}^2$). Full registry on [[Complex Analysis I — Basic Notions]].

---

# Axiom Motivation

The starting move of complex analysis is to copy the definition of differentiability from real analysis, *verbatim*, but apply it to a function of a complex variable. The real definition reads: $f$ is differentiable at $w$ if $\lim_{z \to w}(f(z) - f(w))/(z - w)$ exists. Replace $\mathbb{R}$ by $\mathbb{C}$ and the *same formula* defines complex differentiability. What changes is the limit.

In real variables, $z \to w$ means $z$ approaches $w$ from the left or the right — two directions, and existence of the limit means both one-sided limits agree. In complex variables, $z \to w$ means $z$ approaches $w$ from *every direction in the plane* — uncountably many directions. The ratio $(f(z) - f(w))/(z - w)$ is now a *complex* number, with a magnitude and a phase, and the limit must exist as a complex number, *independent of direction*. This is a vastly stronger condition than its real counterpart. Two real partial derivatives — one in the $x$-direction, one in the $y$-direction — must agree in a precise way (the Cauchy–Riemann equations), and *all other directions* must also agree, which is automatic once the two axial directions do (granted real differentiability).

Why insist that the limit exists at *every* direction of approach, rather than just along, say, the coordinate axes? Because the whole subject of complex analysis exists in the strength of this condition. The single direction "along the $x$-axis" gives only a partial derivative $f_x$; the single direction "along the $y$-axis" gives only $f_y$. The condition that they are *the same complex number* — which is what "limit exists in $\mathbb{C}$" forces — is the Cauchy–Riemann condition $f_x = -if_y$, which is the source of all rigidity. Weakening to "limit exists along some chosen family of directions" would lose the rigidity and the subject would collapse.

We then define "holomorphic at $w$" as a *neighbourhood* property: $f$ is differentiable on some disc $D(w, r)$. The disc-neighbourhood requirement, rather than just differentiability at the single point $w$, is what makes the local theory work: theorems about power series expansions, integration around small contours, and continuity of $f'$ all need a disc on which differentiability holds, not just a single point. Without it, $f$ could be differentiable only at isolated points (which happens: $f(z) = |z|^2$ is differentiable only at $0$), and the local theory would not even begin.

"Holomorphic on $U$" is then just "differentiable at every point of $U$" — since differentiability at every point of an open set automatically gives differentiability on a disc around every point.

Finally, "entire" means "holomorphic on all of $\mathbb{C}$". The smallness of $\mathbb{C}$ as a *complex* space (one complex dimension) combined with the rigidity of holomorphicity makes the class of entire functions surprisingly constrained — bounded entire functions are constant (Liouville), entire functions of bounded growth are polynomials (Cauchy estimates). This is in stark contrast to the real $C^\infty$ functions on $\mathbb{R}$, which can be wildly oscillatory and bounded simultaneously ($\sin x$).

---

# The Definition

Let $U \subseteq \mathbb{C}$ be open and $f : U \to \mathbb{C}$ a function.

**Complex differentiable at $w \in U$.** $f$ is **complex differentiable at $w$** if the limit
$$f'(w) := \lim_{z \to w}\frac{f(z) - f(w)}{z - w}$$
exists in $\mathbb{C}$. The limit is taken over all sequences $z_n \in U \setminus \{w\}$ with $z_n \to w$; equivalently, the existence requires the same limit value along every direction of approach.

**Holomorphic at $w$.** $f$ is **holomorphic at $w$** if there exists $r > 0$ such that $f$ is complex differentiable at every point of $D(w, r) \subseteq U$.

**Holomorphic on $U$.** $f$ is **holomorphic on $U$** if it is holomorphic at every $w \in U$. (Equivalently: $f$ is complex differentiable at every point of $U$.)

**Entire.** $f$ is **entire** if it is holomorphic on all of $\mathbb{C}$.

The same formal rules of differentiation hold as in real analysis: sum, product, quotient, chain rule. The proofs are *identical* to the real-variable proofs, since they use only the algebra of limits.

---

# Relate to Other Fields / Compression

In **real multivariable analysis**, viewing $\mathbb{C} \cong \mathbb{R}^2$ and $f = u + iv$ as a map $\mathbb{R}^2 \to \mathbb{R}^2$, the function has a [[Def - Critical Point, Hessian, and Definiteness|total derivative]] $Df_w : \mathbb{R}^2 \to \mathbb{R}^2$ at $w$ whenever $u, v$ are real-differentiable. Complex differentiability at $w$ is then *precisely* the condition that $Df_w$ is not merely $\mathbb{R}$-linear but $\mathbb{C}$-linear — i.e., commutes with multiplication by $i$. The Cauchy–Riemann equations $u_x = v_y, u_y = -v_x$ are this condition spelled out in coordinates: they assert that the Jacobian matrix has the form $\begin{pmatrix} a & -b \\ b & a\end{pmatrix}$, which is multiplication by $a + ib$.

In **differential geometry**, $\mathbb{C}$ is a complex manifold of complex dimension $1$; the tangent space at any point carries a *complex structure* $J$ (multiplication by $i$). A holomorphic map is a smooth map whose differential commutes with $J$. The same definition extends to arbitrary complex manifolds and gives the global notion of holomorphic map.

In **algebraic geometry**, the algebraic analogue is a *morphism of schemes* over $\mathbb{C}$: a map that pulls polynomial functions to polynomial functions. The complex-analytic and algebraic-geometric categories are related by GAGA (Serre's theorem), which says they coincide for compact complex manifolds that are algebraic.

---

# Examples / Corollaries

**Is an instance — polynomials.** Any polynomial $p(z) = \sum_{k=0}^n a_k z^k$ is entire. By induction on degree using the product rule, $p'(z) = \sum_{k=1}^n k a_k z^{k-1}$ at every $z$.

**Is an instance — rational functions.** $f(z) = p(z)/q(z)$ for $p, q$ polynomials is holomorphic on $\mathbb{C} \setminus q^{-1}(0)$ by the quotient rule.

**Is an instance — the complex exponential.** $\exp(z) = \sum_{n=0}^\infty z^n/n!$ is entire with $\exp'(z) = \exp(z)$, proved via termwise differentiation of the power series (see [[Def - Complex Exponential and Trigonometric Functions]]).

**Is NOT an instance — $f(z) = \bar z$.** Complex conjugation is real-differentiable everywhere (it is just the linear map $(x, y) \mapsto (x, -y)$) but complex-differentiable nowhere. The Cauchy–Riemann equations $u = x, v = -y$ give $u_x = 1, v_y = -1$, which violates $u_x = v_y$. Concretely, the limit $(\bar z - \bar w)/(z - w)$ takes value $1$ along $z = w + t$ (real) and $-1$ along $z = w + it$. See [[Ex - The function f(z) = bar z is not differentiable]].

**Is NOT an instance — $f(z) = |z|^2$.** Real-differentiable everywhere ($f(x, y) = x^2 + y^2$ with $f_x = 2x, f_y = 2y$). Complex-differentiable only at $z = 0$: at any other $w \neq 0$, the CR equations fail ($u = x^2 + y^2$ has $u_y = 2y \neq 0 = -v_x$ since $v = 0$). At $z = 0$ it is differentiable with $f'(0) = 0$, but holomorphicity fails — there is no disc around $0$ on which $f$ is differentiable.

**Corollary — holomorphicity is closed under sum, product, quotient (where defined), and composition.** Direct consequence of the limit rules. The class of holomorphic functions on $U$ forms a $\mathbb{C}$-algebra under pointwise operations.

**Corollary — a constant function is entire with derivative $0$.** Trivial from the definition.

**Calibration check.** Verify that $f(z) = z$ is entire with $f'(z) = 1$ (trivially); that $f(z) = z^2$ is entire with $f'(z) = 2z$ (product rule); that $f(z) = 1/z$ is holomorphic on $\mathbb{C}^\times$ with $f'(z) = -1/z^2$ (quotient rule). If you can also explain why $f(z) = \operatorname{Re}(z)$ is *not* holomorphic anywhere (CR fails: $u = x, v = 0$, so $u_x = 1, v_y = 0$), you have the basic intuition.

---

# Unlocked by This

> [!tip] Cauchy–Riemann Equations *(from this topic)*
> The translation of holomorphicity into a pair of real PDEs is the [[Thm - Cauchy–Riemann Equations|Cauchy–Riemann theorem]], the source of every concrete check of holomorphicity.

> [!tip] Analytic Equivalence *(from CA II)*
> A holomorphic function on an open set is automatically *analytic*: locally equal to a convergent power series. This equivalence is the central structural theorem of complex analysis and is the content of [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]].

> [!tip] Complex Manifolds *(from Complex Geometry)*
> A **complex manifold** is a topological space locally biholomorphic to a domain in $\mathbb{C}^n$; the holomorphic-function machinery defined here is the local model. Riemann surfaces are the one-dimensional case.
