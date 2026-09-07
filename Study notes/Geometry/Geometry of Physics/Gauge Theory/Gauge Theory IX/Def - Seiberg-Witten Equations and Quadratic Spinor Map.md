---
type: definition
subject: gauge-theory
prereqs: ["Def - Spinor Bundle, Chirality, and Twisted Dirac Operator", "Def - Self-Dual and Anti-Self-Dual Connection"]
tags: [gauge-theory, seiberg-witten, spin-c]
---

# Prerequisite Concepts

- [[Def - Spinor Bundle, Chirality, and Twisted Dirac Operator]]
- [[Def - Self-Dual and Anti-Self-Dual Connection]]

# Convention and Motivation

Fix a spin-c structure on a closed oriented Riemannian four-manifold, with bundles $S^\pm$ and determinant line $L$. Clifford multiplication identifies $i\Lambda^2_+$ with trace-free Hermitian endomorphisms of $S^+$. The equations couple a linear Dirac equation to a curvature equation whose source is the unique natural quadratic expression in the spinor.

# The Definition

> [!definition] Seiberg–Witten equations
> Define
> $$q(\psi)=\psi\psi^*-\frac12|\psi|^2\operatorname{id}_{S^+}\in i\mathfrak{su}(S^+)\cong i\Lambda^2_+.$$
> For a positive spinor $\psi$ and unitary determinant-line connection $A$, the equations are
> $$D_A^+\psi=0,\qquad F_A^+=q(\psi)+\eta,$$
> where $\eta\in\Omega^2_+(i\mathbb R)$ is a fixed perturbation.

The unperturbed Seiberg–Witten map is
$$\operatorname{SW}(\psi,A)=(D_A^+\psi,F_A^+-q(\psi)).$$
Our normalization matches Haydys: changing the determinant connection by $a$ changes $D_A$ by $\frac12c(a)$.

# Algebraic Identities

The polarization $q(\psi,\phi)$ is determined by $q(\psi+\phi)-q(\psi)-q(\phi)=2q(\psi,\phi)$. In rank two,
$$\langle q(\psi)\psi,\psi\rangle=\frac12|\psi|^4.$$
This positive quartic term is the engine of compactness.

