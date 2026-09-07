---
type: exercise
subject: gauge-theory
prereqs: ["Def - Intersection Form of a Four-Manifold"]
tags: [four-manifolds, exercise]
---
# Exercise
Compute $Q_X$ for $S^4$, $S^2\times S^2$, $\mathbb{CP}^2$, $\overline{\mathbb{CP}}{}^2$, and $k\mathbb{CP}^2\#\ell\overline{\mathbb{CP}}{}^2$. Determine rank, signature, parity, and definiteness.

> [!solution]- Solution
> Since $H^2(S^4)=0$, its form has rank zero. For $S^2\times S^2$, the two factor classes square to zero and pair to one, giving $H=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$, of rank two, signature zero, even parity, and indefinite type. The complex line in $\mathbb{CP}^2$ has self-intersection one, so its form is $(1)$; orientation reversal gives $(-1)$. Connected sum takes orthogonal sums, hence the final form is $I_k\oplus(-I_\ell)$, with rank $k+\ell$, signature $k-\ell$, odd parity when $k+\ell>0$, and definite exactly when $k=0$ or $\ell=0$.
