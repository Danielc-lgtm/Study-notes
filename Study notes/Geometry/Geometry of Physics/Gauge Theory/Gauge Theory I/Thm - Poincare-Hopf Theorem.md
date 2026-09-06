---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Index of a Vector Field at a Zero"
  - "Thm - Gauss-Bonnet Theorem for Surfaces"
tags: [geometry, topology, Euler-characteristic]
---

# Notation

Let $M$ be a closed oriented smooth surface, $v$ a smooth tangent vector field with isolated zeros $p_1,\ldots,p_N$, and $\operatorname{ind}_{p_j}(v)$ their local indices.

# Statement

> [!theorem] Poincaré–Hopf for closed oriented surfaces
> $$
> \sum_{j=1}^N\operatorname{ind}_{p_j}(v)=\chi(M).
> $$

# Motivation

The vector field supplies a preferred frame wherever it is nonzero. The obstruction to extending that frame through each missing point is its winding number. Curvature measures the obstruction to having one frame globally, so integrating curvature adds precisely those local windings.

# Rederivation Scaffold

Normalize $v$ on the punctured surface, complete it to an oriented orthonormal frame, apply Stokes to its scalar $SO(2)$ connection form, identify each boundary integral with a local index, and finish with Gauss–Bonnet.

# Formal Proof

> [!proof]- Formal Proof
> Choose a Riemannian metric and disjoint positively oriented coordinate discs $D_j(\varepsilon)$ about the zeros, small enough to contain no other zeros. Put
> $$M_\varepsilon=M\setminus\bigcup_j\operatorname{int}D_j(\varepsilon).$$
> On $M_\varepsilon$, let $e_1=v/\lVert v\rVert$ and let $e_2$ be its positive quarter-turn. This is a global oriented orthonormal frame. Write its Levi–Civita connection matrix as
> $$\omega=\begin{pmatrix}0&\alpha\\-\alpha&0\end{pmatrix}.$$
> Since $SO(2)$ is abelian, the curvature component is $\Omega^1{}_2=d\alpha$. Stokes gives
> $$
> \int_{M_\varepsilon}\Omega^1{}_2
> =\int_{\partial M_\varepsilon}\alpha
> =-\sum_j\int_{\partial D_j(\varepsilon)}\alpha,
> $$
> because the boundary orientation inherited from the punctured surface is opposite to the positive boundary orientation of each deleted disc.
>
> Fix a smooth oriented orthonormal reference frame $(f_1,f_2)$ on $D_j$. Along $\partial D_j(\varepsilon)$ write
> $$e_1=\cos\theta,f_1+\sin\theta,f_2,qquad
> e_2=-\sin\theta,f_1+\cos\theta,f_2.$$
> If $\beta$ is the connection component in the reference frame, the passive rotation formula is $\alpha=\beta-d\theta$. Therefore
> $$
> -\frac1{2\pi}\int_{\partial D_j(\varepsilon)}\alpha
> =\frac1{2\pi}\int_{\partial D_j(\varepsilon)}d\theta
> -\frac1{2\pi}\int_{\partial D_j(\varepsilon)}\beta.
> $$
> The first term is $\operatorname{ind}_{p_j}(v)$. The second tends to zero with $\varepsilon$, because $\beta$ is smooth and the boundary length tends to zero. Also $\int_{M_\varepsilon}\Omega^1{}_2\to\int_M\Omega^1{}_2$ by smoothness. Passing to the limit yields
> $$
> \frac1{2\pi}\int_M\Omega^1{}_2
> =\sum_j\operatorname{ind}_{p_j}(v).
> $$
> Gauss–Bonnet identifies the left side with $\chi(M)$, completing the proof.

# What Makes This Hard

The frame defined by $v/|v|$ exists only on the punctured surface. The boundary orientations and the sign in the frame-rotation law are therefore essential; ignoring either loses the index sign.

# Bridges

The general $n$-dimensional theorem identifies the zero-section intersection number with the Euler class $e(TM)[M]=\chi(M)$. The surface proof above is its moving-frame realization.
