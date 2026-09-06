---
type: definition
subject: gauge-theory
prereqs: ["Def - Spin and Spin-c Structures", "Def - Dirac Bundle and Dirac Operator"]
tags: [gauge-theory, spinor-bundle, chirality, twisted-dirac]
---

# The Definition

> [!definition] Spinor bundle
> Given a spin or spin-c structure and the complex spin representation $\Delta_n$, the spinor bundle is
> $$S=P\times_{\operatorname{Spin}^{(c)}(n)}\Delta_n.$$
> Its compatible connection defines the spin or spin-c Dirac operator $D:\Gamma(S)\to\Gamma(S)$.

In even dimension, the complex volume element squares to one and splits
$$S=S^+\oplus S^-.$$
Clifford multiplication by a one-form reverses chirality, so
$$D=\begin{pmatrix}0&D^-\\D^+&0\end{pmatrix},\qquad D^+:\Gamma(S^+)\to\Gamma(S^-).$$

# Twisting

If $E$ is a Hermitian bundle with unitary connection $A$, the product connection on $S\otimes E$ is Clifford-compatible and defines $D_A$. If $A$ changes by $a\in\Omega^1(\operatorname{End}E)$, then
$$D_{A+a}=D_A+c(a).$$
For a spin-c Dirac operator parametrized by a determinant-line connection, the corresponding formula contains $\frac12c(a)$ because the spinor $U(1)$ weight is one while the determinant weight is two.

# Dimension Four

$\operatorname{Spin}(4)=SU(2)_+\times SU(2)_-$ and $S^\pm$ are the two fundamental complex rank-two representations. This algebraic splitting is the spinorial counterpart of $\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-$.

