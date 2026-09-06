---
type: topic
subject: gauge-theory
chapter: "Gauge Theory V"
title: "Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons"
tags: [gauge-theory, hodge-theory, maxwell, yang-mills, instantons]
---

# Notation Registry

$(M^n,g)$ is oriented and has signature $(p,q)$, with $q$ negative directions. $P\to M$ is a principal compact $G$-bundle, $\mathfrak g$ carries an $\operatorname{Ad}$-invariant positive inner product, $A$ is a connection, and
$$F_A=dA+A\wedge A,\qquad d_A=d+[A,\cdot].$$
The Hodge star satisfies $*^2=(-1)^{k(n-k)+q}$ on $k$-forms. On a Riemannian four-manifold, write $F_A=F_A^++F_A^-$ with $*F_A^\pm=\pm F_A^\pm$.

# Motivation

Gauge geometry supplies identities but not dynamics. Bianchi says $d_AF_A=0$ for every connection; it cannot select the fields realized in nature. A metric adds the Hodge star, allowing curvature to be paired with itself. The simplest local, gauge-invariant quadratic functional is the Yang–Mills action. Its Euler–Lagrange equation says curvature is covariantly co-closed.

The abelian specialization is Maxwell theory. Nonabelian curvature contains $A\wedge A$, so the field carries the charge to which it responds and the equation is nonlinear. In Euclidean dimension four, a second structure appears: the star acts as an involution on two-forms. Completing the action square separates a topological term from a nonnegative norm. Self-dual or anti-self-dual connections saturate the resulting bound and automatically solve Yang–Mills.

# Concept Map

## §5.1 Hodge star and Maxwell theory

- [[Def - Hodge Star in Arbitrary Signature]] fixes the Euclidean/Lorentzian sign and conformal behavior.
- [[Def - Maxwell Field, Action, and Equations]] derives $dF=0$ and $d*F=*j$ and distinguishes local potentials from global curvature.
- [[Thm - Bianchi Identity and Yang-Mills Together Parallel Maxwell]] places Maxwell inside the nonabelian system.
- [[Thm - Stress-Energy Tensor of a Gauge Field]] derives energy-momentum and its divergence.

![[Exercise Index - §5.1 Hodge Theory, Maxwell, and Noether Symmetry]]

## §5.2 Yang–Mills dynamics

- [[Def - The Yang-Mills Field Strength]] records the local component formula.
- [[Def - Gauge-Covariant Derivative]] differentiates adjoint-valued fields.
- [[Def - The Yang-Mills Action Functional]] gives the global curvature norm.
- [[Thm - Yang-Mills Equation from the Action Principle]] proves $d_A^*F_A=0$, equivalently $d_A*F_A=0$.
- [[Def - The Yang-Mills Equation]] separates vacuum and sourced equations.
- [[Def - Noether Current for an Internal Symmetry]] and [[Thm - Noether's Theorem for Internal Symmetries]] explain conserved matter currents.

![[Exercise Index - §5.2 The Yang-Mills Lagrangian and Equations]]

## §5.3 Four-dimensional self-duality

- [[Def - Self-Dual and Anti-Self-Dual Connection]] defines the first-order equations.
- [[Thm - Self-Dual Connections Solve Yang-Mills Automatically]] combines self-duality with Bianchi.
- [[Thm - BPS Bound on the Yang-Mills Action]] relates the curvature norm to the second Chern number.
- [[Ex - Conformal Invariance of Yang-Mills on R^4]] explains why dimension four is critical.

![[Exercise Index - §5.3 Self-Duality and Instantons]]

## §5.4 Instantons and BPST

- [[Def - Instanton]] imposes Euclidean Yang–Mills and finite action.
- [[Def - The BPST Instanton]] gives the charge-one $SU(2)$ ansatz.
- [[Ex - 't Hooft Symbols and Self-Duality]] packages the self-dual basis.
- [[Ex - Computing the Field Strength of the BPST Instanton]] performs the curvature calculation.
- [[Thm - Existence of the BPST Instanton]] checks smooth extension and finite action.
- [[Ex - Verifying the Second Chern Number of BPST is 1]] fixes the topological normalization.

![[Exercise Index - §5.4 The BPST Solution]]

# Sources and Targets

A metric and orientation are the input for the Hodge star. A connection then yields three principal targets: an action $\|F_A\|^2$, its Euler–Lagrange equation $d_A^*F_A=0$, and in four dimensions the topological number $\int\operatorname{tr}(F_A\wedge F_A)$. Conversely, a prescribed topological charge suggests minimizing the action within that component; the BPS identity converts the minimization problem into the first-order equation $F_A^\pm=0$.

Maxwell problems usually start with either a potential, a closed integral two-form, or electric and magnetic components. Yang–Mills problems start with a principal connection or local gauge potential. Instanton problems add Euclidean signature, four dimensions, finite action, and an asymptotic framing.

# Legal Operations

1. **Apply the Hodge star only after fixing signature and orientation.** The sign of $*^2$ controls whether a real self-dual decomposition exists.
2. **Vary within the affine space of connections.** Write $A_t=A+ta$ with $a\in\Omega^1(M;\operatorname{Ad}P)$ and use $\dot F=d_Aa$.
3. **Integrate covariantly by parts.** Compact support or boundary conditions remove the boundary term and expose $d_A^*F_A$.
4. **Use Bianchi independently of dynamics.** It holds off shell and turns self-duality into the Yang–Mills equation.
5. **Complete the square in four Euclidean dimensions.** Orthogonality of $\Omega^2_+$ and $\Omega^2_-$ separates norm and characteristic number.
6. **Exploit conformal invariance on middle-degree forms.** In dimension four, $*$ on two-forms and $\int|F|^2$ are conformally invariant.
7. **Compactify finite-action configurations only after controlling decay.** Removable-singularity and framing results justify passage from $\mathbb R^4$ to $S^4$.
8. **Quotient by gauge only after identifying stabilizers.** Reducible connections produce singular orbit spaces.
9. **Compare bulk charge with boundary winding.** Chern–Simons transgression relates $\int_{\mathbb R^4}\operatorname{tr}(F\wedge F)$ to the degree of the asymptotic map $S^3\to G$.

## Illegal but tempting

Do not impose the real equation $F=*F$ in Lorentzian four-space: there $*^2=-1$ on real two-forms; Euclidean signature or complexification is required. Do not infer that every Yang–Mills field is self-dual: self-duality is a sufficient first-order condition and characterizes saturation of the topological bound, not every critical point. Do not infer a topological charge from finite $L^2$ curvature alone without the extension/decay hypotheses that make the boundary map and integral degree well defined.

# Problem-Solving Strategy

For a field equation, decide first whether it is kinematic or variational. Curvature identities come from $d_A^2$ and Bianchi; dynamics comes from varying an action. During variation, keep $a=\delta A$ adjoint-valued, compute $\delta F=d_Aa$, and integrate by parts once. In four-dimensional minimization, avoid the second-order equation initially: split curvature into $F^+$ and $F^-$ and read the action and characteristic number as the sum and difference of their squared norms.

For an explicit instanton, fix Lie-algebra and orientation conventions before checking signs. Compute curvature, identify the self-dual basis, verify decay, and only then evaluate charge. The unifying question is: **how does the metric turn gauge-covariant curvature into dynamics while topology constrains its minima?**

# Most Reusable Properties

- [[Def - Hodge Star in Arbitrary Signature|Signature controls duality]]: $*^2=1$ on Euclidean four-dimensional two-forms but $-1$ in Lorentzian signature.
- [[Thm - Yang-Mills Equation from the Action Principle|Yang–Mills is covariant co-closedness]]: the nonlinear equation has the same formal shape as source-free Maxwell.
- [[Thm - Self-Dual Connections Solve Yang-Mills Automatically|First order implies second order]]: Bianchi is the mechanism, not a separate computation.
- [[Thm - BPS Bound on the Yang-Mills Action|Topology bounds energy]]: equality identifies absolute minima in a fixed charge sector.
- [[Thm - Stress-Energy Tensor of a Gauge Field|Stress-energy divergence]] is the local force-transfer law and vanishes in vacuum.

# Insights

Four dimensions are special for two independent but compatible reasons. The Hodge star preserves degree only on middle-dimensional forms, and the Yang–Mills action is conformally invariant only when curvature has degree two in dimension four. Consequently self-duality is both algebraically meaningful and analytically scale-invariant.

The distinction between representation and object remains essential. $A_\mu$ is a gauge-dependent local representative; $F_A$ is an adjoint-valued global object; $\langle F_A,F_A\rangle$ is a gauge-invariant scalar density; and the Chern number is a topological integer. Each passage forgets information while gaining invariance.

# Bridges

Gauge Theory IV supplies the characteristic number in the BPS bound and the Chern–Simons boundary term. Gauge Theory VII supplies Sobolev completions, elliptic estimates, and compactness tools. Gauge Theory XI explains how anti-self-dual moduli spaces constrain smooth four-manifolds.

# Sources

- Konstantin Wernli, *Mathematical Gauge Theory*, §§3.1–3.3.
- Andriy Haydys, *Introduction to Gauge Theory*, §3 for characteristic-number normalization and later analytical chapters for moduli-space structure.
