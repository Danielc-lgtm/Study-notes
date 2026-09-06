---
type: theorem
subject: gauge-theory
prereqs: ["Def - Seiberg-Witten Equations and Quadratic Spinor Map", "Def - Elliptic Complex and Associated Laplacian"]
tags: [gauge-theory, seiberg-witten, elliptic-complex]
---

# Statement

> [!theorem] Seiberg–Witten deformation complex
> At a solution $(\psi,A)$,
> $$0\to\Omega^0(i\mathbb R)\xrightarrow{R}\Gamma(S^+)\oplus\Omega^1(i\mathbb R)\xrightarrow{D\operatorname{SW}}\Gamma(S^-)\oplus\Omega^2_+(i\mathbb R)\to0$$
> is elliptic, where
> $$R(\xi)=(-\xi\psi,2d\xi),$$
> $$D\operatorname{SW}(\phi,a)=\left(D_A^+\phi+\frac12c(a)\psi, d^+a-2q(\psi,\phi)\right).$$

# Formal Proof

> [!proof]- Formal Proof
> Equivariance and the fact that the base point is a zero imply $D\operatorname{SW}\circ R=0$. Zeroth-order terms do not enter principal symbols. The symbol complex is therefore the direct sum of the chiral Dirac symbol and
> $$0\to\Lambda^0\xrightarrow{\xi\wedge}\Lambda^1\xrightarrow{\pi_+(\xi\wedge)}\Lambda^2_+\to0.$$
> The Dirac symbol is invertible for $\xi\ne0$. For the second sequence choose an oriented orthonormal basis with $\xi=e^1$. Its first image is $\mathbb Re^1$; the kernel of $\pi_+(e^1\wedge-)$ is also $\mathbb Re^1$, since the three images of $e^2,e^3,e^4$ form a basis of $\Lambda^2_+$. The last symbol is surjective for the same reason. Thus the full symbol sequence is exact.

# Consequence

Adding the slice operator $R^*$ gives a single elliptic Fredholm operator. Its kernel is the tangent space of a regular irreducible moduli space and its cokernel is the obstruction space.

