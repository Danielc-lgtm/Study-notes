---
type: definition
subject: gauge-theory
prereqs: ["Def - Orientation Fundamental Class and Poincare Duality"]
tags: [four-manifolds, intersection-form]
---
# The Definition
For a closed connected oriented four-manifold $X$, the intersection form on the free lattice $H^2(X;\mathbb Z)/\mathrm{Tor}$ is
$$Q_X(a,b)=\langle a\smile b,[X]\rangle.$$
Poincaré duality makes $Q_X$ unimodular, and degree-two graded commutativity makes it symmetric. Transverse oriented surfaces representing the dual homology classes compute it by signed intersection points.

The form is **even** if $Q(x,x)$ is even for every $x$, otherwise **odd**. Over $\mathbb R$ it diagonalizes with $b_2^+$ positive and $b_2^-$ negative eigenvalues; $\sigma(X)=b_2^+-b_2^-$.

# Operations and examples
Orientation reversal negates $Q_X$. Connected sum gives $Q_{X\#Y}\cong Q_X\oplus Q_Y$. For $S^2\times S^2$, the factor spheres give the hyperbolic matrix $H=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$. For $\mathbb{CP}^2$ with complex orientation, $Q=(1)$. The even positive-definite $E_8$ lattice has rank and signature eight.

# Gauge-theory dictionary
For a metric, harmonic two-forms split as $\mathcal H^2_+\oplus\mathcal H^2_-$, and
$$Q_X([\alpha],[\alpha])=\|\alpha^+\|_2^2-\|\alpha^-\|_2^2.$$
Thus the metric-dependent Hodge splitting realizes the metric-independent signature.
