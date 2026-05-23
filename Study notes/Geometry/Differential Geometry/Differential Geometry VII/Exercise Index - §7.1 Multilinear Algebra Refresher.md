---
type: exercise-index
subject: differential-geometry
section: "7.1"
tags: [geometry, differential-geometry, multilinear-algebra]
---

## §7.1 Multilinear Algebra Refresher — Exercises

This section drills the multilinear algebra of a single finite-dimensional vector space $V$, as the fibre-level ingredient for tensor fields on a manifold. The exercises focus on **recognizing tensoriality** (verifying multilinearity), **computing components** (in a chosen basis), and the **distinction between $(1, 1)$-tensors and linear maps** (which are the same object viewed in two ways). The Kronecker delta exercise is the most basic non-trivial drill — it isolates the unique tensor with chart-independent components and so functions as the prototype for "what makes a tensor a tensor". The decomposition exercise drills the standard splitting of $T^2$ into its symmetric and antisymmetric parts and exhibits its failure at higher rank.

- [[Ex - The Kronecker Delta as a Mixed Tensor]] (⭐) — verify that the evaluation pairing is a $(1, 1)$-tensor; compute its components; show they are basis-invariant; identify the corresponding linear map as the identity ([[Def - Mixed Tensor]], [[Thm - Transformation Rule for Tensor Components]]).

- [[Ex - Decomposing a 2-Tensor into Symmetric and Antisymmetric Parts]] (⭐) — drill the $k = 2$ decomposition into symmetric + alternating parts; verify the projector identities; exhibit a counterexample showing failure for $k = 3$ ([[Def - Symmetric Tensor Field]], [[Def - Alternating Tensor Field]], [[Thm - Symmetrization and Alternation Projectors]]).

- [[Ex - The Stress Tensor as a Symmetric 2-Tensor]] (⭐⭐) — recognize the stress tensor as a $(1, 1)$-tensor, derive its symmetry from angular momentum conservation, apply the spectral theorem for principal stresses and axes ([[Def - Mixed Tensor]], [[Def - Symmetric Tensor Field]]).
