---
type: exercise-index
subject: special-relativity
section: "10.3"
tags: [physics, special-relativity, lie-groups, representation-theory]
---

## §10.3 The Exponential Map and Structure Constants — Exercises

The exercises of §10.3 carry the Lie algebra back up to the group and into representation theory. Two of them exponentiate generators: a boost generator $K_1$, whose positive square $K_1^2 = \mathrm{diag}(1,1,0,0)$ resums the series into the hyperbolic boost $\cosh\psi, \sinh\psi$, and a rotation generator $J_3$, whose negative square $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ resums into the circular rotation $\cos\varphi, \sin\varphi$ — the sign of $G^2$ deciding hyperbolic-versus-circular and, equivalently, non-compact-versus-compact. The third carries out the chapter's deepest computation, the complex change of basis $A_i = \tfrac12(J_i + iK_i)$ that decouples the algebra into two commuting copies of $\mathfrak{su}(2)$ and labels all relativistic fields by a pair $(j_A, j_B)$. The fourth applies Baker–Campbell–Hausdorff to two non-collinear boosts and extracts the Thomas rotation from the single commutator $[K_1, K_2] = -J_3$. The unifying observation: the structure constants determine everything — the closed-form exponentials, the complex split into spin algebras, and the composition law with its Thomas rotation — so the finite group and its representation theory are entirely encoded in the brackets of the generators.

- [[Ex - Exponentiating a boost generator gives a hyperbolic boost]] (⭐⭐) — compute $K_1^2$ and $K_1^3$, resum $\exp(\psi K_1)$ into the hyperbolic boost matrix, identify $v = \tanh\psi$, and trace the hyperbolic functions to the *positive* sign of $K_1^2$ (versus the circular rotation case) ([[Thm - The Exponential Map Generates the Restricted Lorentz Group]], [[Def - Lie Algebra of the Lorentz Group]], [[Def - Boosts as Hyperbolic Rotations]]).

- [[Ex - Exponentiating a rotation generator gives a rotation]] (⭐) — compute $J_3^2$ and $J_3^3$, resum $\exp(\varphi J_3)$ into the Rodrigues rotation matrix, verify $2\pi$-periodicity, and contrast the compact rotation circle with the non-compact boost line via the *negative* sign of $J_3^2$ ([[Thm - The Exponential Map Generates the Restricted Lorentz Group]], [[Def - Lie Algebra of the Lorentz Group]]).

- [[Ex - The complexification splits so(1,3) into two copies of su(2)]] (⭐⭐⭐) — form $A_i = \tfrac12(J_i + iK_i)$, $B_i = \tfrac12(J_i - iK_i)$, compute $[A_i, A_j] = \epsilon_{ijk}A_k$ and $[A_i, B_j] = 0$, conclude $\mathfrak{so}(1,3)_{\mathbb{C}} = \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ (explaining why complexification is essential), and read off the $(j_A, j_B)$ field dictionary ([[Thm - The Complexification of so(1,3) and the (A,B) Decomposition]], [[Def - Lie Algebra of the Lorentz Group]], [[Def - Generators and Structure Constants]]).

- [[Ex - The Thomas rotation from the boost-boost commutator]] (⭐⭐⭐) — apply Baker–Campbell–Hausdorff to two perpendicular boosts, show the leading correction $\tfrac12[K_1, K_2] = -\tfrac12 J_3$ is a rotation generator, obtain the Thomas–Wigner angle $\approx \tfrac12\psi_1\psi_2$, and connect to Thomas precession and the absence of rotation for collinear boosts ([[Thm - The Exponential Map Generates the Restricted Lorentz Group]], [[Def - Generators and Structure Constants]], [[Def - Thomas Rotation]]).
