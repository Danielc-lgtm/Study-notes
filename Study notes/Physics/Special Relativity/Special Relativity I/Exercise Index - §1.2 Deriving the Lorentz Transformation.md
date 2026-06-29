---
type: exercise-index
subject: special-relativity
section: "1.2"
tags: [physics, special-relativity]
---

## §1.2 Deriving the Lorentz Transformation — Exercises

The exercises of §1.2 are about the derivation itself and its immediate structural payoff. The first is the load-bearing one: carry out the full postulate-to-formula derivation, applying inertia (linearity), the moving origin (spatial form), isotropy (evenness of $\gamma$), and the constancy of light (the value of $\gamma$) in sequence, then recover the clock equation by substitution. The second redoes the whole thing by Bondi's $k$-calculus — a logically *weaker* set of assumptions (light signals only, no linearity postulate) — reaching the same boost and exposing $\gamma = \tfrac12(k + k^{-1})$, $k = e^\varphi$ as the Doppler factor and boost eigenvalue. The third composes two boosts to *derive* the velocity-addition law and the one-parameter group structure, with [[Def - Rapidity|rapidity]] as the additive coordinate. Together they show the Lorentz transformation is forced, reachable from several directions, and group-structured.

- [[Ex - Deriving the Lorentz transformation from the postulates]] (⭐⭐) — the full first-principles derivation: linearity from inertia, $x' = \gamma(x-vt)$ from the moving origin, $\gamma_v = \gamma_{-v}$ from isotropy, $\gamma = (1-v^2/c^2)^{-1/2}$ from multiplying the forward and backward light conditions, and $t' = \gamma(t - vx/c^2)$ by substitution; checks via the light ray and the Galilean limit ([[Def - Inertial Frame and the Postulates of Special Relativity]], [[Def - The Lorentz Transformation]], [[Thm - Uniqueness of the Lorentz Transformation from the Postulates]], [[Def - Galilean Spacetime and Its Failure]]).

- [[Ex - The k-calculus (Bondi) derivation]] (⭐⭐⭐) — a second, independent derivation from light signals alone: define the $k$-factor, apply it twice for a round trip, radar-coordinatise to get $k = \sqrt{(c+v)/(c-v)}$, recover the boost with $\gamma = \tfrac12(k + k^{-1})$, and identify $k = e^\varphi$ as the relativistic Doppler factor (multiplicative under composition, hence additive rapidity) and the eigenvalue of the boost along the light cone ([[Def - Inertial Frame and the Postulates of Special Relativity]], [[Def - The Lorentz Transformation]], [[Def - Spacetime Diagram]], [[Def - Rapidity]], [[Thm - Relativistic Velocity Addition]]).

- [[Ex - Composing two collinear boosts]] (⭐⭐) — multiply two boost matrices to derive $v_{12} = (v_1+v_2)/(1+v_1v_2)$, confirm the composite is a genuine boost via $A^2 - B^2 = 1$, redo it in rapidity to get $\varphi_1 + \varphi_2$ trivially, and conclude the boosts form a one-parameter group with $|v_{12}| < 1$ automatic since $\tanh: \mathbb{R} \to (-1,1)$ ([[Def - The Lorentz Transformation]], [[Def - Rapidity]], [[Thm - Relativistic Velocity Addition]]).
