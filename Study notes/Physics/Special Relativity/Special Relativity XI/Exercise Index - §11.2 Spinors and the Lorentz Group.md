---
type: exercise-index
subject: special-relativity
section: "11.2"
tags: [physics, special-relativity]
---

## §11.2 Spinors and the Lorentz Group — Exercises

The exercises of §11.2 turn the abstract double cover into concrete computations and connect it to spin and representation theory. The first runs the $SU(2)\to SO(3)$ map on a rotation about the $z$-axis, making the half-angle, the $4\pi$ periodicity, and the quaternion conjugation formula tangible. The second does the boost counterpart, showing that the Hermitian (non-unitary) elements of $SL(2,\mathbb{C})$ are exactly the boosts and that their eigenvalues are the Doppler factors. The third establishes the Lie-algebra isomorphism $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(1,3)$ by matching generators — $\mathscr{S}'(\sigma_i) = 2K_i$, $\mathscr{S}'(i\sigma_i) = -2J_i$ — and reads off the two-Weyl-spinor structure from the complexified splitting $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$. Across all three, the recurring diagnostic is "imaginary exponent of a Pauli matrix = unitary = rotation; real exponent = Hermitian = boost," and the recurring factor of two — half-angle, two preimages, the doubled generator — is always the same fact: the two factors of $A$ in the congruence.

- [[Ex - SU(2) double-covers SO(3) — a rotation about the z-axis]] (⭐⭐) — compute $A(\theta) = \exp(-\tfrac{i\theta}{2}\sigma_3) = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$, show its congruence rotates $(x^1, x^2)$ by $\theta$ via the off-diagonal phase $e^{-i\theta}$, exhibit $A(\theta+2\pi) = -A(\theta)$ giving the same rotation ($2\pi$ for the rotation, $4\pi$ for $A$), and recover the quaternion conjugation $\mathbf v \mapsto q\mathbf v q^{-1}$ ([[Thm - The Spinor Map SU(2) to SO(3)]], [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence]], [[Def - Quaternions]]).

- [[Ex - A Lorentz boost as an SL(2,C) element]] (⭐⭐) — compute the Hermitian $A(\psi) = \exp(\tfrac\psi2\sigma_3) = \mathrm{diag}(e^{\psi/2}, e^{-\psi/2})$, show its congruence scales the light-cone coordinates $t \pm z$ by $e^{\pm\psi}$ to give the rapidity boost, explain why a Hermitian (not unitary) matrix is needed (unitary fixes time), and relate its eigenvalues $e^{\pm\psi/2}$ to the Doppler factors ([[Def - Lie Algebra sl(2,C) and the Exponential Map]], [[Def - The Spinor Map and SL(2,C)]], [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence]]).

- [[Ex - The Lie algebra isomorphism sl(2,C) to so(1,3)]] (⭐⭐⭐) — compute the differential $\mathscr{S}'(B) = B\underline X + \underline X B^\dagger$ on the Pauli basis, find $\mathscr{S}'(\sigma_i) = 2K_i$ (Hermitian $\to$ boost, via the anticommutator) and $\mathscr{S}'(i\sigma_i) = -2J_i$ (anti-Hermitian $\to$ rotation, via the commutator), verify the bracket $[\sigma_1,\sigma_2]\mapsto[K_1,K_2]=-J_3$, and connect to $\mathfrak{so}(1,3)_{\mathbb C}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ and the two Weyl spinors ([[Def - Lie Algebra sl(2,C) and the Exponential Map]], [[Def - Lie Algebra of the Lorentz Group]], [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence]]).
