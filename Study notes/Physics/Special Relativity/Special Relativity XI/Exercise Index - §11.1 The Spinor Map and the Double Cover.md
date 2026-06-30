---
type: exercise-index
subject: special-relativity
section: "11.1"
tags: [physics, special-relativity]
---

## §11.1 The Spinor Map and the Double Cover — Exercises

The exercises of §11.1 build the foundational machinery of the chapter: the Pauli matrices and their multiplication law, the realisation of a four-vector as a Hermitian matrix with the interval as a determinant, and the spinor map $\mathscr{S} : SL(2,\mathbb{C}) \to SO^+(1,3)$ that this realisation makes possible. The first exercise establishes the algebra ($\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$ and $\det\underline X = X\cdot X$) on which everything downstream rests. The second proves the spinor map's image lands in the *restricted* Lorentz group — proper and orthochronous — by computing $(\Lambda_A)^0{}_0 = \tfrac12\sum|\,\cdot\,|^2 > 0$. The third computes the kernel $\{\pm I\}$, the single calculation that upgrades "homomorphism" to "double cover" and is the algebraic source of spin. The unifying technique is the congruence $\underline X \mapsto A\underline X A^\dagger$, with its two factors of $A$ responsible for determinant-preservation, the homomorphism property, and the eventual half-angle.

- [[Ex - Pauli matrix identities and the Hermitian correspondence]] (⭐) — derive $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$ and $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$ from the explicit matrices, then verify $\det\underline X = X\cdot X$ and the trace inverse $x^\mu = \tfrac12\mathrm{tr}(\sigma_\mu\underline X)$ — the algebra that powers every later computation ([[Def - Pauli Matrices and the Hermitian-Matrix Correspondence]]).

- [[Ex - The spinor map lands in the proper orthochronous Lorentz group]] (⭐⭐) — show $\Phi_A(\underline X) = A\underline X A^\dagger$ preserves Hermiticity and determinant (so $\Lambda_A$ is Lorentz), is a homomorphism via $(AB)^\dagger = B^\dagger A^\dagger$, has $(\Lambda_A)^0{}_0 = \tfrac12(|\alpha|^2+|\beta|^2+|\gamma|^2+|\delta|^2) > 0$ (orthochronous), and $\det\Lambda_A = 1$ (proper), placing the image in $SO^+(1,3)$ ([[Def - The Spinor Map and SL(2,C)]], [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence]]).

- [[Ex - The kernel of the spinor map is plus or minus the identity]] (⭐⭐) — compute $\ker\mathscr{S} = \{\pm I\}$ by testing $A\underline X A^\dagger = \underline X$ on $I, \sigma_3, \sigma_1$ (forcing $A$ scalar, then $\pm I$ by $\det$), deduce the two-to-one structure $SO^+(1,3) \cong SL(2,\mathbb{C})/\{\pm I\}$, and exhibit $A = I$ versus $A = -I$ producing the same rotation but opposite signs on a spinor ([[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group]], [[Def - The Spinor Map and SL(2,C)]], [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence]]).
