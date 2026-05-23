---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Jacobi Field"
  - "Def - Conjugate Point"
  - "Def - The Riemannian Exponential Map"
tags: [geometry, riemannian-geometry, jacobi-fields, conjugate-points, curvature]
---

# Notation

$(M, g)$ a Riemannian manifold, $\gamma_v : I \to M$ the unique geodesic with $\gamma_v(0) = p$ and $\dot\gamma_v(0) = v$. $T = \dot\gamma_v$. The Riemann curvature operator on $T^\perp$ is $w \mapsto R(w, T)T$, a self-adjoint linear map on $T^\perp$ depending on $t$. Its eigenvalues are $\lambda_1(t) \leq \cdots \leq \lambda_{n-1}(t)$. $J$ denotes a [[Def - Jacobi Field|Jacobi field]] along $\gamma_v$, satisfying $J'' + R(J, T)T = 0$. Full registry on [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Statement

> **Theorem (Jacobi Equation and Conjugate Points).** Let $(M, g)$ be a Riemannian manifold and $\gamma_v : I \to M$ a geodesic with $\gamma_v(0) = p$ and $\dot\gamma_v(0) = v$. For each $w \in T_pM$, the [[Def - Jacobi Field|Jacobi field]] $J_w$ along $\gamma_v$ with $J_w(0) = 0$ and $J_w'(0) = w$ is given by
> $$J_w(t) = d(\exp_p)_{tv}(tw).$$
> Consequently:
>
> (i) The differential $d(\exp_p)_{tv}$ at $tv \in T_pM$ is invertible iff there is no nonzero $w \in T_pM$ with $J_w(t) = 0$, i.e., iff $\gamma_v(t)$ is *not* [[Def - Conjugate Point|conjugate]] to $p$ along $\gamma_v$.
>
> (ii) The multiplicity of the conjugate pair $(p, \gamma_v(t))$ along $\gamma_v$ equals $\dim \ker d(\exp_p)_{tv}$.

> **Corollary (curvature-eigenvalue / conjugate-point dictionary).** Along a unit-speed geodesic $\gamma$, parallel-transport an orthonormal frame $(e_1(t), \ldots, e_{n-1}(t))$ along $T^\perp$. The Jacobi equation on a normal field $J(t) = \sum_i f_i(t) e_i(t)$ becomes the linear ODE system
> $$f''(t) + A(t)\, f(t) = 0,$$
> where $A(t)_{ij} := g(R(e_j, T)T, e_i)$ is the matrix of the curvature operator in the parallel frame. **Conjugate points appear at parameter values $t_0$ where the matrix-valued solution $\Phi(t)$ of $\Phi'' + A \Phi = 0$ with $\Phi(0) = 0, \Phi'(0) = I$ becomes singular**, and the eigenvalues of $A(t)$ are the precise rates at which conjugate points appear.

> **Corollary (Sturm comparison ⟹ conjugate-point distance bounds).** If the sectional curvature on $M$ along $\gamma$ satisfies $K \geq K_0 > 0$ for every 2-plane containing $T$, then there is a conjugate point along $\gamma$ at parameter at most $\pi/\sqrt{K_0}$. If $K \leq 0$ along $\gamma$, then there are no conjugate points anywhere along $\gamma$.

---

# Motivation

This theorem is the cleanest possible statement of the **link between three different layers** of Riemannian geometry: the linear-algebraic data (the curvature operator, its eigenvalues), the ODE-theoretic data (the Jacobi equation, its zeros), and the geometric data (the exponential map, its singular values). The dictionary it establishes is:

| Curvature eigenvalues | Jacobi equation zeros | Singular values of $\exp_p$ |
|---|---|---|
| $\lambda > 0$ | $f'' + \lambda f = 0$ with zero at $\pi/\sqrt\lambda$ | Conjugate point at distance $\pi/\sqrt\lambda$ |
| $\lambda = 0$ | $f'' = 0$, no zero | No conjugate point |
| $\lambda < 0$ | $f'' + \lambda f = 0$, hyperbolic, no zero | No conjugate point |

This is the entire engine of comparison geometry. Curvature bounds — whether on sectional curvature, Ricci curvature, or scalar curvature — translate into bounds on conjugate-point distance, which translate into bounds on the injectivity radius, which translate into bounds on the diameter (via the second variation of length), which translate into compactness and topology results (Bonnet–Myers, Synge, Cartan–Hadamard).

The Jacobi-field formula $J_w(t) = d(\exp_p)_{tv}(tw)$ is also the technical heart of the theorem. It says that **Jacobi fields with $J(0) = 0$ are the radial derivatives of the exponential map**. This converts the abstract "Jacobi field" (defined as the variation of geodesics through nearby geodesics) into the concrete "differential of $\exp_p$ along radial directions", which is computable in any specific example. And it makes the equivalence between conjugate points (Jacobi field $J_w(t) = 0$) and singular values of $d(\exp_p)$ ($\ker d(\exp_p)_{tv} \ni w$) into a tautology.

The variational/Morse-theoretic content is the [[Thm - Second Variation of Arc Length|second variation of arc length]]: at a conjugate point, the index form has a non-trivial kernel, signalling the loss of length-minimisation. The **Morse Index Theorem** packages this into a count: the index of the index form equals the number of interior conjugate points, with multiplicity.

The **eigenvalue link** is the new insight worth dwelling on. The Jacobi operator $\mathcal J(V) := V'' + R(V, T)T$ is a self-adjoint second-order ODE operator with the curvature operator $R(\cdot, T)T$ as its zeroth-order coefficient. Its spectrum is determined by the eigenvalues $\lambda_i(t)$ of this coefficient. Positive eigenvalues force the corresponding scalar Jacobi equations $f_i'' + \lambda_i f_i = 0$ to oscillate, producing conjugate points; large positive eigenvalues force conjugate points to appear quickly (Sturm comparison: bigger $\lambda$ ⟹ earlier zero of $f$). Negative eigenvalues forbid conjugate points entirely along the corresponding directions. So **the spectrum of the curvature operator along $\gamma$ is the spectrum of the conjugate-point geometry along $\gamma$**.

This is the precise sense in which positive Ricci curvature forces conjugate points (and hence diameter bounds, via Bonnet–Myers): the trace of the curvature operator $\sum_i \lambda_i(t) = \mathrm{Ric}(T, T)$, so a lower bound on Ricci forces an average lower bound on the eigenvalues, forces a conjugate point within $\pi/\sqrt{\mathrm{Ric}/(n-1)}$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a geodesic and a tangent vector. Sources are problems where the link between Jacobi fields and the exponential map's differential is implicit.

The most common source is **a problem about $\exp_p$ failing to be a local diffeomorphism**. The map $\exp_p$ is a local diffeo at $v$ iff $d(\exp_p)_v$ is invertible. So any problem about caustics, focal points, or breakdown of normal coordinates is, by the theorem, a problem about conjugate points and Jacobi fields. Bridge: any "where does the exponential map develop singularities?" question routes through the Jacobi equation.

A subtler source is **a problem about geodesic flow stability**. The Poincaré linearisation of geodesic flow at a periodic orbit (closed geodesic) is governed by Jacobi fields along the orbit. Eigenvalues of the linearised return map encode stability: eigenvalues on the unit circle ⟺ marginally stable; eigenvalues with $|\lambda| \neq 1$ ⟺ hyperbolic. Bridge: dynamical-systems questions about closed geodesics route through the Jacobi-field formulation.

A third source is **a problem with sectional curvature bounds**. Any "sectional curvature is $\geq K_0$" or "$\leq K_0$" hypothesis routes through the eigenvalue link of the theorem to a conclusion about conjugate-point distance — and hence to a conclusion about the injectivity radius, the diameter, the fundamental group, or other global structures. Bridge: curvature bounds ⟹ conjugate-point bounds via Sturm comparison.

**Targets (Output Amplification)**

The conclusion is the dictionary between Jacobi fields, conjugate points, and $\exp_p$ singular values. Targets are the structural results that use this dictionary.

The most important combination is **theorem + a positive-curvature lower bound ⟹ Bonnet–Myers**. If $\mathrm{Ric} \geq (n-1) K_0 g$ with $K_0 > 0$, then the trace of $R(\cdot, T)T$ is at least $(n-1)K_0$ on $T^\perp$, so the average eigenvalue is at least $K_0$. By Sturm comparison applied to each scalar Jacobi equation, the corresponding $f_i$ has a zero within $\pi/\sqrt{K_0}$. So a conjugate point appears within $\pi/\sqrt{K_0}$ along any unit-speed geodesic. By the [[Thm - Second Variation of Arc Length|second variation]] and [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]], the diameter is at most $\pi/\sqrt{K_0}$. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

A second combination is **theorem + non-positive sectional curvature ⟹ Cartan–Hadamard**. If $K \leq 0$ everywhere, the curvature eigenvalues are non-positive, and no conjugate points appear along any geodesic. Hence $d(\exp_p)$ is everywhere invertible, $\exp_p$ is a local diffeomorphism, and on a complete simply connected manifold it is a *global* diffeomorphism $T_pM \to M$. So $M$ is diffeomorphic to $\mathbb{R}^n$.

A third combination is **theorem + explicit symmetric-space metric ⟹ explicit Jacobi-field and conjugate-point structure**. On the round sphere, $R(\cdot, T)T = T^\perp$ (i.e., the curvature operator is the identity on $T^\perp$), so all eigenvalues are $1$, and the scalar Jacobi equation is $f'' + f = 0$ — conjugate points at $\pi$ (the antipode). On hyperbolic space, all eigenvalues are $-1$, scalar Jacobi is $f'' - f = 0$ — no conjugate points. On a Lie group with bi-invariant metric, the eigenvalues are $|\mathrm{ad}_X|^2 / 4$, giving conjugate points at specific distances determined by the Lie algebra structure.

A fourth combination is **theorem + the Morse Index Theorem ⟹ count of conjugate points = index of $I$**. The index form $I$ has, as its kernel on $\mathcal V_0^\perp$, the Jacobi fields vanishing at both endpoints — i.e., conjugate-point fields. The number of conjugate points strictly inside $\gamma$ equals the index of $I$ (a finite count, since $I$ is a Hessian on a separable space). This is the **Morse Index Theorem**, and it makes the conjugate-point count a variational invariant of $\gamma$.

---

# Why Is It True

**Mechanism summary:** **the variation $\gamma_s(t) := \exp_p(t(v + sw))$ has $\gamma_0 = \gamma_v$ and is geodesic for each $s$ (since it has initial velocity $v + sw$), so its variation field $J_w(t) = \partial_s|_{s=0}\exp_p(t(v + sw))$ is by definition a Jacobi field; differentiating produces $J_w(t) = d(\exp_p)_{tv}(tw)$, and conjugate points along $\gamma_v$ are precisely the values of $t$ at which this Jacobi field vanishes — equivalently, the singular values of $d(\exp_p)_{tv}$.**

The proof is the same identification we used in the [[Thm - The Gauss Lemma|Gauss lemma]], applied carefully. Setup the variation $\gamma_s(t) := \exp_p(t(v + sw))$. For each $s$, $\gamma_s$ is a geodesic — it starts at $p$ with initial velocity $v + sw$. So the variation $\gamma_s$ is a *variation through geodesics*, and by [[Def - Jacobi Field|the definition of Jacobi field as variation through geodesics]], the variation field $J(t) := \partial_s|_{s=0}\gamma_s(t)$ is a Jacobi field along $\gamma_0 = \gamma_v$.

Compute $J$:
$$J(t) = \partial_s|_{s=0}\exp_p(t(v + sw)) = d(\exp_p)_{tv}(tw).$$
This is the formula in the statement.

Initial conditions:
- $J(0) = \partial_s|_{s=0}\exp_p(0) = 0$, since $\exp_p(0) = p$ for all $s$.
- $J'(0) = \nabla_T J|_{t=0}$. By the swap $\nabla_{\partial_t}\partial_s = \nabla_{\partial_s}\partial_t$ (using torsion-freeness and $[\partial_s, \partial_t] = 0$), $\nabla_{\partial_t}\partial_s \Gamma|_{t=0} = \nabla_{\partial_s}\partial_t \Gamma|_{t=0} = \partial_s|_{s=0}(v + sw) = w$.

So $J$ is the unique Jacobi field with $J(0) = 0, J'(0) = w$ — the one we denoted $J_w$ in the statement.

For the conjugate-point characterisation: $\gamma_v(t_0)$ is conjugate to $p$ along $\gamma_v$ iff there is a non-zero $w \in T_pM$ with $J_w(t_0) = 0$ — which by the formula $J_w(t_0) = d(\exp_p)_{t_0 v}(t_0 w)$ is equivalent to $w \in \ker d(\exp_p)_{t_0 v}/(t_0)$ (modulo the factor $t_0 \neq 0$, which doesn't affect the kernel). The kernel of $d(\exp_p)_{t_0 v}$ is exactly the multiplicity of the conjugate pair.

The **eigenvalue link** comes from parallel-transporting a frame along $\gamma$ and reducing the Jacobi equation to a constant-coefficient system in the frame. The frame turns $\nabla_T$ into $d/dt$, and the curvature operator becomes the matrix $A(t)$ of components. The eigenvalues of $A(t)$ are the sectional curvatures of the 2-planes spanned by $T$ and the frame vectors — by definition of sectional curvature. Sturm comparison applied to each scalar equation $f_i'' + \lambda_i(t) f_i = 0$ then gives the conjugate-point bounds.

---

# What Makes This Hard

The conceptual difficulty is **the identification of $d(\exp_p)$ with a Jacobi field**. The differential of the exponential map and the Jacobi equation are *a priori* different objects, and the equality $J_w = d(\exp_p)_{tv}(tw)$ requires the swap-of-covariant-derivatives argument plus the careful identification of initial conditions. It is the key identity that makes the entire theorem possible.

The technical difficulty is the **parallel-transport reduction**. The Jacobi equation along $\gamma$ is naturally written using $\nabla_T$, which is hard to manipulate directly. Parallel-transporting an orthonormal frame converts it to a constant-coefficient ODE in the frame (but with the curvature operator becoming the time-dependent matrix $A(t)$), which is the form needed for Sturm-comparison arguments.

The most common error is to **conflate the parameter on $\gamma$ (called $t$) with the radial coordinate in $T_pM$ (called $r$ in polar coordinates)**. They are the same on a unit-speed geodesic — the geodesic with unit initial velocity is parametrised by arc length — but on a general-speed geodesic they differ by the constant $|v|$. The formula $J_w(t) = d(\exp_p)_{tv}(tw)$ has $t$ as the geodesic parameter, *not* the radial coordinate.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Construct the variation $\gamma_s(t) := \exp_p(t(v + sw))$, observe it is a variation through geodesics. Compute the variation field and identify it as a Jacobi field with explicit initial conditions. The formula $J_w(t) = d(\exp_p)_{tv}(tw)$ comes from differentiating; the conjugate-point characterisation is then immediate.

**Subgoal decomposition:**

1. **Construct the variation $\gamma_s(t) = \exp_p(t(v + sw))$.** Verify each $\gamma_s$ is a geodesic.
   - *Hint:* by homogeneity of geodesics, $\exp_p(t \cdot u) = \gamma_u(t)$, so $\gamma_s(t) = \gamma_{v + sw}(t)$.
   - *Why needed:* gives a variation *through geodesics*, the setup for a Jacobi field.

2. **Compute the variation field $J(t) := \partial_s|_{s=0}\gamma_s(t)$.** Express it as $d(\exp_p)_{tv}(tw)$.
   - *Hint:* by chain rule, $\partial_s|_{s=0}\exp_p(t(v + sw)) = d(\exp_p)_{tv}\cdot t w$.
   - *Why needed:* gives the explicit formula.

3. **Verify $J$ is a Jacobi field.** It is a variation through geodesics — that *is* a Jacobi field by definition.
   - *Hint:* either invoke the definition directly, or differentiate $\nabla_T \dot\gamma_s = 0$ in $s$ and use the curvature swap.
   - *Why needed:* connects the formula to the Jacobi equation.

4. **Verify initial conditions.** $J(0) = 0$ (since $\exp_p(0) = p$ for all $s$). $J'(0) = w$ (by torsion-free covariant derivative swap).
   - *Hint:* substitute and compute.
   - *Why needed:* pin down which Jacobi field this is.

5. **Derive the conjugate-point characterisation.** $\gamma_v(t_0)$ conjugate to $p$ ⟺ exists $w \neq 0$ with $J_w(t_0) = 0$ ⟺ $d(\exp_p)_{t_0 v}$ has non-trivial kernel ⟺ singular.
   - *Hint:* unwind definitions.
   - *Why needed:* states the explicit conjugate-point dictionary.

6. **Apply parallel-transport reduction and Sturm comparison.** Parallel-transport an orthonormal frame; the Jacobi equation becomes $f'' + A(t)f = 0$ with $A(t)$ the matrix of the curvature operator. Eigenvalues of $A(t)$ give conjugate-point distance bounds via Sturm comparison with constant-coefficient equations.
   - *Hint:* this is the standard Sturm-Liouville argument.
   - *Why needed:* gives the eigenvalue/conjugate-point dictionary.

---

# Lemma Decomposition

> [!note]- Lemma 1: The variation $\gamma_s(t) = \exp_p(t(v + sw))$ is a variation through geodesics
> **Statement:** For any $v, w \in T_pM$ and any $s$ such that $v + sw$ is in the domain of $\exp_p$ near $0$, the curve $\gamma_s : t \mapsto \exp_p(t(v + sw))$ is a geodesic with $\gamma_s(0) = p$ and $\dot\gamma_s(0) = v + sw$.
>
> **Hint:** This is the definition of the exponential map: $\exp_p(t u)$ is the geodesic with initial velocity $u$, evaluated at time $t$.
>
> **Why needed:** Establishes that the variation field is a Jacobi field (because it is a variation through geodesics).
>
> > [!note]- Full proof
> > By the homogeneity property of the exponential map (see [[Def - The Riemannian Exponential Map]]), $\exp_p(tu) = \gamma_u(t)$ where $\gamma_u$ is the geodesic with $\gamma_u(0) = p, \dot\gamma_u(0) = u$. Setting $u = v + sw$ gives $\gamma_s(t) = \exp_p(t(v + sw)) = \gamma_{v + sw}(t)$. This is by construction a geodesic with $\gamma_s(0) = p$ and $\dot\gamma_s(0) = v + sw$.

> [!note]- Lemma 2: Variation field is $d(\exp_p)_{tv}(tw)$
> **Statement:** $J(t) := \partial_s|_{s=0}\gamma_s(t) = d(\exp_p)_{tv}(tw)$.
>
> **Hint:** Apply the chain rule to $\exp_p(t(v + sw))$ in $s$.
>
> **Why needed:** Gives the explicit formula for the Jacobi field with $J(0) = 0$.
>
> > [!note]- Full proof
> > By the chain rule (applied to $\exp_p$ as a function $T_pM \to M$),
> > $$J(t) = \partial_s|_{s=0}\exp_p(t(v + sw)) = d(\exp_p)_{tv}\cdot \partial_s|_{s=0}(t(v + sw)) = d(\exp_p)_{tv}(tw),$$
> > using the linearity of $d(\exp_p)_{tv}$ in the second argument.

> [!note]- Lemma 3: $J$ satisfies the Jacobi equation with $J(0) = 0, J'(0) = w$
> **Statement:** The variation field $J$ from Lemma 2 is the Jacobi field along $\gamma_v$ with $J(0) = 0$ and $J'(0) = w$.
>
> **Hint:** $J$ is a variation through geodesics, hence a Jacobi field by definition. The initial conditions follow by direct computation.
>
> **Why needed:** Identifies which Jacobi field the formula $d(\exp_p)_{tv}(tw)$ gives.
>
> > [!note]- Full proof
> > $J$ is the variation field of a variation through geodesics (Lemma 1), so by [[Def - Jacobi Field|the definition]], $J$ is a Jacobi field.
> >
> > Initial conditions:
> > - $J(0) = d(\exp_p)_{0}(0) = 0$ (since $0 \cdot w = 0$ and $d(\exp_p)_0(0) = 0$).
> > - $J'(0)$: by the swap $\nabla_{\partial_t}\partial_s \Gamma = \nabla_{\partial_s}\partial_t \Gamma$ (Lemma 2 of [[Thm - First Variation of Arc Length]]),
> > $$J'(0) = \nabla_{\partial_t}\partial_s \Gamma|_{(t,s) = (0,0)} = \nabla_{\partial_s}\partial_t \Gamma|_{(0,0)} = \partial_s|_{s=0}(v + sw) = w.$$
> > So $J = J_w$, the unique Jacobi field with $J(0) = 0, J'(0) = w$.

> [!note]- Lemma 4: Sturm comparison for the scalar Jacobi equation
> **Statement:** If $f$ solves $f'' + a(t) f = 0$ with $f(0) = 0$ and $a(t) \geq K_0 > 0$ on $[0, T]$, then $f$ has a zero in $(0, \pi/\sqrt{K_0}]$.
>
> **Hint:** Compare with the model solution $\tilde f$ of $\tilde f'' + K_0 \tilde f = 0$ with $\tilde f(0) = 0$, $\tilde f(t) = \sin(\sqrt{K_0}\, t)/\sqrt{K_0}$, which has zero at $\pi/\sqrt{K_0}$. By Sturm comparison, $f$ has a zero in $(0, \pi/\sqrt{K_0}]$.
>
> **Why needed:** Translates curvature bounds into conjugate-point distance bounds.
>
> > [!note]- Full proof (sketch)
> > Compute the Wronskian $W(t) = f'(t)\tilde f(t) - f(t)\tilde f'(t)$. Differentiate: $W'(t) = f''\tilde f - f \tilde f'' = (-a f)\tilde f - f(-K_0 \tilde f) = (K_0 - a) f \tilde f$. If $a \geq K_0$ and $f, \tilde f > 0$ on an interval, then $W' \leq 0$.
> >
> > Initially (at $t = 0$): $f(0) = \tilde f(0) = 0$, and $W(0) = f'(0) \cdot 0 - 0 \cdot \tilde f'(0) = 0$. So $W(0) = 0$.
> >
> > Suppose for contradiction $f > 0$ on $(0, \pi/\sqrt{K_0}]$. On this interval $\tilde f > 0$ (until $\pi/\sqrt{K_0}$, where it vanishes). So $W' \leq 0$, hence $W$ is non-increasing from $W(0) = 0$, hence $W \leq 0$ on the interval. At $t = \pi/\sqrt{K_0}$, $\tilde f(t) = 0$ and $\tilde f'(t) < 0$ (the model is decreasing past its maximum), so $W(\pi/\sqrt{K_0}) = f'(t) \cdot 0 - f(t)\tilde f'(t) = -f(t)\tilde f'(t) > 0$ (since $f > 0$ and $\tilde f' < 0$). Contradiction. So $f$ has a zero in $(0, \pi/\sqrt{K_0}]$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** $J_w(t) = d(\exp_p)_{tv}(tw)$, where $J_w$ is the Jacobi field along $\gamma_v$ with $J_w(0) = 0, J_w'(0) = w$. Furthermore, $d(\exp_p)_{tv}$ is invertible iff $\gamma_v(t)$ is not conjugate to $p$ along $\gamma_v$, with multiplicity equal to $\dim \ker d(\exp_p)_{tv}$.
>
> *Proof.* Define $\gamma_s(t) := \exp_p(t(v + sw))$. By Lemma 1, each $\gamma_s$ is a geodesic with $\gamma_s(0) = p, \dot\gamma_s(0) = v + sw$. So $\gamma_s$ is a smooth variation through geodesics of $\gamma_0 = \gamma_v$.
>
> By Lemma 2, the variation field $J(t) := \partial_s|_{s=0}\gamma_s(t) = d(\exp_p)_{tv}(tw)$.
>
> By Lemma 3, $J$ is the unique Jacobi field along $\gamma_v$ with $J(0) = 0, J'(0) = w$. So $J = J_w$, and the formula $J_w(t) = d(\exp_p)_{tv}(tw)$ is established.
>
> For the conjugate-point characterisation: $\gamma_v(t)$ is conjugate to $p$ along $\gamma_v$ iff there exists a non-zero $w \in T_pM$ with $J_w(t) = 0$ iff there exists $w$ such that $d(\exp_p)_{tv}(tw) = 0$ iff $\ker d(\exp_p)_{tv}$ contains some $tw \neq 0$ iff $d(\exp_p)_{tv}$ is singular. The multiplicity is the dimension of this kernel.
>
> The Sturm-comparison corollary follows from Lemma 4 applied to each scalar equation $f_i'' + \lambda_i(t) f_i = 0$ obtained by diagonalising the matrix $A(t)$ of the curvature operator in a parallel-transported frame. Bounds on the eigenvalues $\lambda_i(t)$ translate via Sturm into conjugate-point distance bounds. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**ODE theory: the Sturm oscillation theorem.** The scalar Jacobi equation $f'' + a(t) f = 0$ is the prototype of a Sturm–Liouville problem. The Sturm oscillation theorem, the comparison theorem, and the interlacing of zeros of eigenfunctions are all classical results of Sturm–Liouville theory that translate directly into Riemannian-geometric statements about conjugate points and the geometry of Jacobi fields. The conjugate-point analysis in Riemannian geometry is, in disguise, the study of the spectrum and zeros of these operators.

**Optics: focal points and caustics.** A wavefront in geometric optics is propagated along geodesics of the optical metric, and the points where the wavefront becomes singular — **caustics** — are precisely where the linearised geodesic flow (i.e., the Jacobi-field equation) develops vanishing solutions. So caustics in optics are conjugate points in disguise, and the geometric-optics theory of caustics (cusp catastrophes, swallowtails, butterfly catastrophes — the classification of low-codimension caustic singularities) is the geometric-optics version of the Riemannian theory.

**Symplectic geometry: the Maslov index.** A Lagrangian submanifold of a symplectic manifold has, along any path, a *Maslov index* counting how many times it becomes tangent to the vertical foliation. For the case of Lagrangian flows generated by Hamiltonians, the Maslov index along a Hamiltonian trajectory equals the **conjugate-point count of the projection** — i.e., the Morse index of the corresponding variational problem. The Riemannian Morse Index Theorem is the special case for geodesic Hamiltonians; the general symplectic Maslov-index theory is the deep generalisation.

**General relativity: the Raychaudhuri equation.** The Lorentzian analogue of the Jacobi equation, applied to a *congruence* of geodesics (rather than a single geodesic), is the **Raychaudhuri equation**. It governs the **expansion** $\theta$, **shear** $\sigma$, and **rotation** $\omega$ of the congruence. Focusing of the expansion ($\theta \to -\infty$) signals a focal point analogous to a Riemannian conjugate point — and in Lorentzian signature, with the energy conditions of general relativity, the Raychaudhuri equation forces focal points along causal geodesics in finite affine parameter, leading to the **Penrose singularity theorem**.

---

# Bridges

- **[[Def - Jacobi Field|Jacobi Field]]** — the kinematic object. The theorem says: Jacobi fields with $J(0) = 0$ are *exactly* the radial differentials of $\exp_p$. The Jacobi field is the variational version of the differential, and the Jacobi equation is the equation of variations of the geodesic flow.

- **[[Def - Conjugate Point|Conjugate Point]]** — the obstruction. A conjugate point is where a Jacobi field with $J(0) = 0$ returns to zero, equivalently where $d(\exp_p)$ becomes singular. The theorem provides the precise dictionary.

- **[[Def - The Riemannian Exponential Map|The Exponential Map]]** — the geometric face. $\exp_p$ is a local diffeomorphism iff its differential is invertible iff there are no conjugate points. So the *injectivity radius* — the largest $r$ for which $\exp_p|_{B(0,r)}$ is a diffeomorphism — is at most the first conjugate distance.

- **[[Thm - Second Variation of Arc Length|Second Variation of Arc Length]]** — the variational face. The kernel of the index form is the space of Jacobi fields vanishing at the endpoints, which is non-trivial exactly at conjugate-point parameter pairs. The conjugate-point count = index of $I$ via the Morse Index Theorem.

- **The Bonnet–Myers diameter bound** — the direct application. A positive lower bound on Ricci curvature forces a positive lower bound on the average eigenvalue of the curvature operator $R(\cdot, T)T$, which by Sturm comparison forces conjugate points within bounded distance, which (via second variation and Hopf–Rinow) forces bounded diameter. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

---

# Unlocked by This

> [!tip] Bonnet–Myers Diameter Bound *(from Riemannian Geometry)*
> The theorem's eigenvalue/conjugate-point dictionary, combined with the Sturm comparison lemma, gives the Bonnet–Myers theorem: $\mathrm{Ric} \geq (n-1) K_0 g$ with $K_0 > 0$ ⟹ $\mathrm{diam}(M) \leq \pi/\sqrt{K_0}$. The trace inequality on the curvature operator gives an average eigenvalue lower bound; Sturm comparison applied to the average gives a conjugate-point distance bound. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] Cartan–Hadamard Theorem *(from Riemannian Geometry)*
> Non-positive sectional curvature ⟹ non-positive eigenvalues of $R(\cdot, T)T$ ⟹ no conjugate points (the scalar Jacobi equation $f'' + \lambda f = 0$ with $\lambda \leq 0$ has no zero between $0$ and $\infty$ from a $f(0) = 0$ start) ⟹ $d(\exp_p)$ never singular ⟹ $\exp_p$ is a local diffeomorphism. With completeness and simple connectedness, this upgrades to global diffeomorphism. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] **Morse Theory of the Energy Functional** *(from Morse Theory)*
> The Morse Index Theorem says the index of $I$ on $\gamma$ equals the number of interior conjugate points. Combined with the *Bott iteration formula* for closed geodesics, this gives the full Morse theory of the energy functional on the loop space $\Omega(M)$ — and from it, theorems about the existence and multiplicity of closed geodesics (Gromoll–Meyer's theorem, the Lusternik–Fet existence theorem, the Bangert–Hingston theorem on infinitely many closed geodesics on simply connected manifolds).
