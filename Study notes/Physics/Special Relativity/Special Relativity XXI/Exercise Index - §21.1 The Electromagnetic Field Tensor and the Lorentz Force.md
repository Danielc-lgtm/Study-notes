---
type: exercise-index
subject: special-relativity
section: "21.1"
tags: [physics, special-relativity, electromagnetism]
---

## §21.1 The Electromagnetic Field Tensor and the Lorentz Force — Exercises

The exercises of §21.1 build fluency with the central object of the chapter — the electromagnetic field as an antisymmetric 2-form $F$ — and with the Lorentz four-force it exerts. The first drills the structural logic: that the purity of the Lorentz force (orthogonality to four-velocity, conservation of rest mass) is *equivalent* to the antisymmetry of $F$, and that projecting onto an observer recovers the elementary $\mathbf{f} = q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$ and the power $q\mathbf{E}\cdot\mathbf{V}$ — whence the magnetic field does no work. The second is a hands-on construction-and-verification of the field tensor: assembling its component matrix from $\mathbf{E}$ and $\mathbf{B}$, raising indices (with the mostly-minus sign bookkeeping), and computing the Hodge dual, which exchanges electric and magnetic. The third interprets the observer decomposition $F = \underline{U_0}\wedge\mathbf{E} + \star(\underline{U_0}\wedge c\mathbf{B})$, distinguishing the metric dual from the Hodge dual and making precise the sense in which $\mathbf{E}$ and $\mathbf{B}$ are observer-dependent slices of the absolute tensor $F$. The unifying theme: $F$ is the objective object, and the familiar fields and forces are its projections onto an observer's rest space.

- [[Ex - The Lorentz force is a pure four-force]] (⭐⭐) — derive the antisymmetry of $F$ from the purity $f\cdot U = 0$ (rest-mass conservation), show the converse, and project the four-force to recover $\boldsymbol{\mathfrak{F}} = q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$ and the power $q\mathbf{E}\cdot\mathbf{V}$, concluding that a magnetic field does no work ([[Def - The Lorentz Four-Force]], [[Def - The Electromagnetic Field Tensor]], [[Def - Four-Force]]).

- [[Ex - Building the field tensor from E and B]] (⭐) — assemble the component matrix $F_{\alpha\beta}$ with $\mathbf{E}$ in the time-space block and $c\mathbf{B}$ in the space-space block, raise indices (time-space block flips sign in mostly-minus, space-space does not), compute the Hodge dual $\star F$ and verify it exchanges $\mathbf{E}\to-c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$, and recover the fields by contraction with $U_0$ ([[Def - The Electromagnetic Field Tensor]], [[Def - The Hodge Star]], [[Def - The Levi-Civita Tensor]]).

- [[Ex - The metric dual and the field decomposition]] (⭐⭐) — verify $\mathbf{E} = F(\cdot,U_0)$ and $c\mathbf{B} = \star F(U_0,\cdot)$ lie in the rest space (antisymmetry), distinguish the metric dual $F^\sharp$ (index-raising) from the Hodge dual $\star F$ (electric–magnetic exchange), recover the elementary Lorentz force from the decomposition, and explain why the $\mathbf{E}/\mathbf{B}$ split is observer-dependent while $F$ is not ([[Def - The Electromagnetic Field Tensor]], [[Def - The Hodge Star]], [[Def - Observer and Local Rest Space]]).
