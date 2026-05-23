---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Symmetric Tensor Field"
  - "Def - Tensor Field on a Manifold"
  - "Def - Mixed Tensor"
tags: [geometry, differential-geometry, continuum-mechanics, stress-tensor]
---

# Problem Statement

In continuum mechanics, the **Cauchy stress tensor** $\sigma$ at a point $p$ in a deformable body is defined by the requirement that, for any oriented unit area element with normal $\hat n$, the force per unit area (the *traction*) exerted across the surface by the material on one side on the material on the other side is

$$t(\hat n) = \sigma(\hat n, \cdot),$$

where $\sigma$ is a multilinear gadget. Specifically:

**(a)** Argue that $\sigma$ is a $(1, 1)$-tensor on $T_pM$ (the tangent space at the point in the body), i.e., a linear map $T_pM \to T_pM$ that sends a normal vector $\hat n$ to the traction vector $t(\hat n)$.

**(b)** Using the conservation of angular momentum (Cauchy's second law), show that $\sigma_{ij} = \sigma_{ji}$ — the stress tensor is *symmetric* when written as a $(0, 2)$-tensor after lowering the contravariant index with the spatial metric.

**(c)** The principal stresses are the eigenvalues of $\sigma$ (as a self-adjoint operator on $T_pM$, using the metric to identify $(1, 1)$ and $(0, 2)$ types), and the principal axes are the corresponding eigenvectors. Show that the principal stresses are always real, and the principal axes can be chosen orthogonal — and explain why this matters physically.

**Recall:**

A [[Def - Symmetric Tensor Field|symmetric covariant 2-tensor]] on $V$ is a bilinear form $\sigma$ with $\sigma(v, w) = \sigma(w, v)$ for all $v, w \in V$.

A [[Def - Mixed Tensor|mixed (1, 1)-tensor]] on $V$ is a multilinear function $W : V^* \times V \to \mathbb{R}$, equivalently a linear map $T : V \to V$ via $W(\omega, v) = \omega(Tv)$. The matrix of $T$ in a basis is the matrix of components $W^i_j = T^i_j$.

In Riemannian geometry, a metric $g$ provides an isomorphism between $(1, 1)$- and $(0, 2)$-tensors: a $(1, 1)$-tensor $T^i_j$ has a "lowered" form $T_{ij} = g_{ik}T^k_j$, a $(0, 2)$-tensor.

**Cauchy's second law:** The conservation of angular momentum for a deformable body implies that the stress tensor $\sigma$ (as a $(0, 2)$-tensor) is symmetric. The argument is local: consider an infinitesimal cube around a point, compute the net torque from stresses on all six faces, and the requirement that the torque per unit volume be finite forces $\sigma_{ij} = \sigma_{ji}$.

---

# Convergent Strategy

**Problem class.** This is a *recognize the tensor structure of a physical quantity* problem. The stress tensor is presented physically (as the force per unit area on a surface); the task is to identify its tensorial nature and use the consequences. The chapter's [[Differential Geometry VII — Tensors and Tensor Fields#Problem-Solving Strategy|problem-solving strategy]] says: when a physical quantity is multilinear in its inputs and outputs, it is a tensor; the type $(k, \ell)$ is read off from the variances of the slots.

**Assumption pattern.** Three hypotheses: (i) the traction $t(\hat n)$ depends linearly on $\hat n$ (this is Cauchy's stress principle, a postulate of continuum mechanics not derived here); (ii) angular momentum is conserved in the body (Cauchy's second law); (iii) the body has a spatial metric structure (the Euclidean metric in 3D, or a Riemannian metric in general).

**Theorem routing.** For (a), the linearity of $t$ in $\hat n$ identifies $\sigma$ as a $(1, 1)$-tensor (input one vector, output one vector). For (b), the conservation of angular momentum applied to an infinitesimal volume gives the symmetry $\sigma_{ij} = \sigma_{ji}$ (after lowering an index with the metric). For (c), the symmetry implies $\sigma$ is self-adjoint with respect to the metric, and the spectral theorem then gives real eigenvalues and an orthogonal eigenbasis.

**Key decision point.** The non-obvious step is converting $\sigma$ from a $(1, 1)$-tensor (the natural type given the input/output structure of traction-from-normal) to a $(0, 2)$-tensor (the symmetric bilinear form). This conversion requires a metric — without one, "$\sigma_{ij} = \sigma_{ji}$" makes no sense, since the slots are of different types. The metric is what enables index gymnastics, and it is what makes the symmetric/asymmetric question well-posed for $\sigma$.

---

# Legal Operations Used

From [[Differential Geometry VII — Tensors and Tensor Fields#Legal Operations|the topic page's Legal Operations]]:

1. **Check tensoriality via $C^\infty(M)$-multilinearity** (operation 2). The linear dependence of traction on the normal vector identifies $\sigma$ as a tensor.

2. **Compute components in a chart** (operation 3). Components $\sigma^i_j$ or $\sigma_{ij}$ in a basis of $T_pM$.

3. **Symmetrize or alternate a covariant tensor** (operation 7). Angular momentum conservation forces $\sigma_{ij}$ to be in the *symmetric* part of $T^2(V^*)$.

4. **Multiply a tensor field by a smooth function** (operation 9, used implicitly): the stress tensor is a tensor *field* whose components vary smoothly with position in the body.

---

# Hints

> [!note]- Hint 1
> For part (a), the key fact is *Cauchy's stress principle*: the traction $t$ across an infinitesimal area element depends **linearly** on the normal vector $\hat n$ of that element (and on no other geometric data of the element). This is a postulate of continuum mechanics — it is what makes "stress" a well-defined point-level concept rather than a surface-level one.

> [!note]- Hint 2
> For part (b), consider a small cube around a point with edges aligned with coordinate axes. Each face has an outward normal $\pm e_i$ and a traction $\pm \sigma(e_i)$. Compute the torque on the cube from these tractions about each axis. As the cube shrinks (volume → 0 but surface area → boundary), the torque per unit volume must remain finite, which forces the off-diagonal $\sigma_{ij} - \sigma_{ji} = 0$.

> [!note]- Hint 3
> For part (c), the symmetric $(0, 2)$-tensor $\sigma_{ij}$ is a symmetric bilinear form on $T_pM$. The associated linear map $\sigma^i_j$ (after raising one index with the metric) is then self-adjoint: $g(\sigma v, w) = g(v, \sigma w)$. The spectral theorem for self-adjoint operators on a real inner-product space says: real eigenvalues and an orthonormal eigenbasis exist.

---

# Solution

The proof breaks into three parts. (a) Establish $\sigma$ as a $(1, 1)$-tensor. (b) Derive symmetry from angular momentum conservation. (c) Apply the spectral theorem for principal stresses and axes.

**Step (a): $\sigma$ is a $(1, 1)$-tensor.**

The traction $t$ depends linearly on the normal $\hat n$ and is a vector in $T_pM$. So $\sigma : T_pM \to T_pM$ is a linear map — equivalently, a $(1, 1)$-tensor.

> [!note]- Derivation
> *Cauchy's stress principle* says that the traction $t$ across an oriented surface element through a point $p$ depends only on the unit normal $\hat n$ to that element, and the dependence is linear: $t(a\hat n_1 + b\hat n_2) = at(\hat n_1) + bt(\hat n_2)$ for any unit vectors $\hat n_1, \hat n_2$ and scalars $a, b$.
>
> This linearity, extended by scaling to all vectors (not just unit vectors), defines a linear map $\sigma : T_pM \to T_pM$, $\hat n \mapsto t(\hat n)$. Under the isomorphism $\mathcal{L}(V, V) \cong V \otimes V^* \cong T^{(1,1)}(V)$ from [[Def - Mixed Tensor|the mixed-tensor characterization]], this linear map corresponds to a $(1, 1)$-tensor $\sigma \in T^{(1,1)}(T_pM)$ with components $\sigma^i_j$ in any basis.
>
> Geometrically: $\sigma$ converts an "input" direction (the surface normal) into an "output" direction (the traction). The $(1, 1)$ type encodes "one input, one output" — exactly matching the physical interpretation.

**Step (b): Symmetry from angular momentum conservation.**

Conservation of angular momentum applied to an infinitesimal element forces $\sigma_{ij} = \sigma_{ji}$ (after lowering an index with the spatial metric).

> [!note]- Derivation
> Consider a small cubic element of size $\epsilon$ around a point $p$, with edges along the coordinate axes $e_1, e_2, e_3$. The six faces have outward normals $\pm e_1, \pm e_2, \pm e_3$, and the traction on each face is $\pm \sigma(e_i)$, with components $\pm \sigma^j_i$ (the $j$-th component of the traction across the face with normal $\pm e_i$).
>
> *Compute the torque about the $e_3$-axis.* The face with normal $+e_1$ has area $\epsilon^2$ and traction-component $\sigma^2_1$ (the $e_2$-component of the force per unit area), giving force $\sigma^2_1 \epsilon^2$ in the $e_2$ direction. This force acts at $(\epsilon/2)e_1$, so its torque about the $e_3$-axis is $(\epsilon/2) \cdot \sigma^2_1 \epsilon^2 = (\sigma^2_1/2) \epsilon^3$ in the $+e_3$ direction.
>
> The face $-e_1$ (normal $-e_1$, opposite side) gives a force in the $-e_2$ direction at $(-\epsilon/2)e_1$. Torque: $(-\epsilon/2) \cdot (-\sigma^2_1 \epsilon^2) = (\sigma^2_1 / 2)\epsilon^3$ — *same direction*. Total from the $\pm e_1$ faces: $\sigma^2_1 \epsilon^3$.
>
> Similarly, the face $\pm e_2$ contributes net torque $-\sigma^1_2 \epsilon^3$ (with opposite sign because the moment arm $(\pm\epsilon/2)e_2$ is in $e_2$ while the force component is in $e_1$, and the cross product $e_2 \times e_1 = -e_3$).
>
> The total torque about the $e_3$-axis from all six faces is $(\sigma^2_1 - \sigma^1_2)\epsilon^3$, which scales as the volume.
>
> *The body force contribution* scales as the volume $\epsilon^3$ times $\text{arm length} \sim \epsilon$, so as $\epsilon^4$. As $\epsilon \to 0$, the volume torque from $\sigma$ (scaling as $\epsilon^3$) dominates body-force torque (scaling as $\epsilon^4$). For the **angular acceleration** of the element to remain finite (since the moment of inertia of the cube scales as $\epsilon^5$), the angular momentum equation forces the leading-order torque to vanish:
> $$\sigma^2_1 - \sigma^1_2 = 0.$$
>
> By symmetry (interchanging axes), $\sigma^i_j - \sigma^j_i = 0$ for all $i, j$. In components with metric-lowered indices, $\sigma_{ij} = g_{ik}\sigma^k_j$, and the symmetry $\sigma^i_j = \sigma^j_i$ in Cartesian coordinates (where $g_{ij} = \delta_{ij}$) directly gives $\sigma_{ij} = \sigma_{ji}$.
>
> So $\sigma$ as a $(0, 2)$-tensor is **symmetric**. $\blacksquare$

**Step (c): Principal stresses and principal axes via the spectral theorem.**

Since $\sigma$ (with one index raised by the metric) is a self-adjoint operator on $T_pM$ with the Euclidean inner product, the spectral theorem applies: its eigenvalues (principal stresses) are real, and its eigenvectors (principal axes) can be chosen orthonormal.

> [!note]- Derivation
> The $(0, 2)$-tensor $\sigma_{ij}$ is symmetric (Step (b)), and the corresponding linear map $\sigma^i_j = g^{ik}\sigma_{kj}$ is self-adjoint with respect to the metric:
> $$g(\sigma v, w) = g_{ij}(\sigma v)^i w^j = g_{ij} \sigma^i_k v^k w^j = \sigma_{jk} v^k w^j = \sigma_{kj} v^k w^j = g(v, \sigma w),$$
> using $\sigma_{jk} = \sigma_{kj}$ (symmetry) and the metric to lower/raise indices.
>
> By the **spectral theorem** for self-adjoint operators on a finite-dimensional real inner-product space ($T_pM$ with the spatial metric):
> 1. All eigenvalues of $\sigma$ are real.
> 2. Eigenvectors corresponding to distinct eigenvalues are orthogonal.
> 3. There exists an orthonormal basis of eigenvectors (i.e., $\sigma$ is diagonalizable).
>
> *Physical interpretation.* The **principal stresses** are the eigenvalues $\lambda_1, \lambda_2, \lambda_3$ of $\sigma$ — they are the values of $t \cdot \hat n$ on each principal axis (the stresses normal to a surface aligned with that axis). The **principal axes** are the eigenvectors $e_1^*, e_2^*, e_3^*$ — orthogonal directions in which the stress is purely normal (no shear). In the principal-axis frame, the stress tensor is diagonal: $\sigma = \mathrm{diag}(\lambda_1, \lambda_2, \lambda_3)$.
>
> This matters physically because in the principal-axis frame, the material experiences pure compression or pure tension in each axis direction, with no shear stress. The principal stresses characterize the local stress state completely up to rotation, and they determine whether the material yields (via von Mises or Tresca criteria), fractures, or remains elastic.

> [!note]- Complete formal solution
> *Step (a).* The traction $t$ depends linearly on the normal $\hat n$ (Cauchy's stress principle), defining a linear map $\sigma : T_pM \to T_pM$, equivalently a $(1, 1)$-tensor with components $\sigma^i_j$.
>
> *Step (b).* Conservation of angular momentum on an infinitesimal cubic element: the surface tractions contribute a torque scaling as the volume $\epsilon^3$, while the body forces contribute $\epsilon^4$. The leading torque must vanish, giving $\sigma^i_j = \sigma^j_i$ in Cartesian coordinates, hence $\sigma_{ij} = \sigma_{ji}$ as a $(0, 2)$-tensor after metric-lowering of one index.
>
> *Step (c).* The symmetric $(0, 2)$-tensor $\sigma$ corresponds to a self-adjoint operator on $T_pM$. By the spectral theorem, it has real eigenvalues (principal stresses) and an orthonormal eigenbasis (principal axes), and is diagonal in this basis. $\blacksquare$

---

# Key Takeaways

**The variance of a physical tensor is determined by its slot types.** Whenever you encounter a multilinear physical quantity, the first task is to identify *what kind of input each slot accepts* and *what kind of output each slot produces*. For the stress tensor, the input is a normal vector (a contravariant vector) and the output is a traction force (a contravariant vector). So the natural type is $(1, 1)$: one slot for the contravariant input, one slot to "deliver" the contravariant output. A bilinear pairing of two contravariant inputs would be a $(0, 2)$-type, like the metric. Different slot types correspond to different functorial behavior and different operations. Most physics texts present stress as a $(0, 2)$-tensor (after lowering an index with the spatial metric) because the symmetry $\sigma_{ij} = \sigma_{ji}$ is cleaner in that form. But the *natural* type, before any metric is invoked, is $(1, 1)$.

**Conservation laws force tensor symmetries.** The symmetry $\sigma_{ij} = \sigma_{ji}$ is *not* a postulate or a definition — it is a *consequence* of angular momentum conservation applied to an infinitesimal element. The same pattern recurs across physics: the symmetry of the Einstein tensor in GR comes from the contracted Bianchi identity; the symmetry of the metric is the basic axiom of inner-product geometry; the antisymmetry of the electromagnetic field tensor $F_{\mu\nu}$ comes from gauge invariance and the no-magnetic-monopole equation. Whenever you see a tensor with a definite symmetry property, ask: what physical conservation law forces it?

**The spectral theorem applies to symmetric $(0, 2)$-tensors via the metric.** The principal-axis decomposition of the stress tensor is a special case of the spectral theorem for self-adjoint operators. The key step is using the spatial metric to convert a symmetric $(0, 2)$-tensor into a self-adjoint $(1, 1)$-tensor (a self-adjoint operator), at which point real eigenvalues and orthogonal eigenvectors are automatic. The same machinery applies to: the **Ricci tensor** (the eigenvalues are the Ricci curvatures), the **second fundamental form** of a hypersurface (eigenvalues are the principal curvatures), the **strain tensor** (eigenvalues are the principal strains), and many more. Every "principal" decomposition in geometry and continuum mechanics is the spectral theorem applied to a symmetric tensor.

**Index gymnastics requires a metric.** The conversion between $(1, 1)$ and $(0, 2)$ formulations of $\sigma$ — and the meaningfulness of the symmetry $\sigma_{ij} = \sigma_{ji}$ — requires a metric (the spatial Euclidean metric in 3D, or a general Riemannian metric). Without a metric, there is no canonical way to compare an upper index to a lower index, and the "symmetry" question is type-incoherent. The fact that we can freely raise and lower indices in continuum mechanics is a consequence of working in a fixed flat space with the Euclidean metric. In curved spaces (like the spacetime manifolds of general relativity), the spatial metric is replaced by the Lorentzian metric $g_{\mu\nu}$, but the principle is the same: a metric is needed to convert between covariant and contravariant variance.
