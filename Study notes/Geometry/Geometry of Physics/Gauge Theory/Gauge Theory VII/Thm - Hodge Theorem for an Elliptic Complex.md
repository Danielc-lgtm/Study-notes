---
type: theorem
subject: gauge-theory
prereqs: ["Def - Elliptic Complex and Associated Laplacian", "Thm - Elliptic Operators are Fredholm and the Fredholm Alternative"]
tags: [gauge-theory, hodge-theorem, elliptic-complex]
---

# Prerequisite Concepts

- [[Def - Elliptic Complex and Associated Laplacian]]
- [[Thm - Elliptic Operators are Fredholm and the Fredholm Alternative]]

# Statement

> [!theorem] Hodge theorem for elliptic complexes
> On a closed manifold, each cohomology class of an elliptic complex has a unique harmonic representative. More precisely,
> $$\mathcal H^j=\ker\Delta_j=\ker L_j\cap\ker L_{j-1}^*,$$
> $$\Gamma(E_j)=\operatorname{im}L_{j-1}\oplus\mathcal H^j\oplus\operatorname{im}L_j^*,$$
> and $\mathcal H^j\cong H^j$ is finite dimensional.

# Formal Proof

> [!proof]- Formal Proof
> Pairing $\Delta_js$ with $s$ gives
> $$\langle\Delta_js,s\rangle=\|L_js\|^2+\|L_{j-1}^*s\|^2,$$
> proving the kernel identity. Ellipticity of $\Delta_j$ makes $\mathcal H^j$ finite dimensional.
>
> The Fredholm alternative gives $L^2$-orthogonal decomposition
> $\Gamma(E_j)=\ker\Delta_j\oplus\operatorname{im}\Delta_j$. Since
> $\operatorname{im}\Delta_j\subseteq\operatorname{im}L_{j-1}+\operatorname{im}L_j^*$ and the reverse inclusion follows by solving with the Green operator on $(\ker\Delta_j)^\perp$, the displayed decomposition follows; the two image summands are orthogonal because $L_jL_{j-1}=0$.
>
> If $s\in\ker L_j$, decompose $s=L_{j-1}u+h+L_j^*v$. Applying $L_j$ and pairing with $v$ gives $\|L_j^*v\|^2=0$, so $s$ is cohomologous to $h$. If harmonic $h$ is exact, $h=L_{j-1}u$, then $\|h\|^2=\langle h,L_{j-1}u\rangle=\langle L_{j-1}^*h,u\rangle=0$. Thus the representative exists uniquely.

# Consequence

For the de Rham complex, this recovers ordinary Hodge theory. For gauge deformation complexes, it gives a finite-dimensional linear model for the moduli space.

