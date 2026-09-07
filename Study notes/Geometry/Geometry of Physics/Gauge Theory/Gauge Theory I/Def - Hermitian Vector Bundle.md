---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Bundle"
  - "Def - Complex Line Bundle"
tags: [geometry, gauge-theory, hermitian, unitary]
---

# Prerequisite Concepts

- [[Def - Vector Bundle]]
- [[Def - Complex Line Bundle]]

# Notation

Let $E\to M$ be a rank-$r$ complex vector bundle. We take Hermitian inner products to be conjugate-linear in the first variable and linear in the second.

# The Definition

> [!definition] Hermitian vector bundle
> A **Hermitian metric** on $E$ is a smoothly varying family of positive-definite Hermitian forms
> $$h_x:E_x\times E_x\to\mathbb C.$$
> Equivalently, $h(s,t)$ is smooth for all local smooth sections $s,t$, and fibrewise
> $$h(au,bv)=\overline a,b,h(u,v),\qquad
> h(v,u)=\overline{h(u,v)},\qquad h(v,v)>0\ (v\ne0).$$
> A complex vector bundle equipped with $h$ is a **Hermitian vector bundle**.

A local frame $(e_1,\ldots,e_r)$ is **unitary** if $h(e_a,e_b)=\delta_{ab}$. Such frames exist by smooth Gram–Schmidt. Their transition maps take values in $U(r)$, so choosing $h$ is equivalent to reducing the frame bundle's structure group from $\mathrm{GL}_r(\mathbb C)$ to $U(r)$.

# Compatible Connections

> [!definition] Unitary connection
> A connection $\nabla$ is **unitary** (or Hermitian-compatible) when
> $$
> d\,h(s,t)=h(\nabla s,t)+h(s,\nabla t).
> $$

In a unitary frame, $\nabla=d+A$ is compatible exactly when $A^*=-A$. To see necessity, apply compatibility to the constant frame pair $e_a,e_b$:
$$0=d\delta_{ab}=h(\nabla e_a,e_b)+h(e_a,\nabla e_b)=(A^*)_{ab}+A_{ab}.$$
The same computation in reverse proves sufficiency. Thus $A\in\Omega^1(U;\mathfrak u(r))$ and $F_A\in\Omega^2(U;\mathfrak u(r))$.

# Existence

Every complex vector bundle over a paracompact manifold admits a Hermitian metric. Choose standard metrics $h_\alpha$ in local trivializations and a subordinate partition of unity $(\rho_\alpha)$. Then $h=\sum_\alpha\rho_\alpha h_\alpha$ is smooth and positive definite: for $v\ne0$, every $h_\alpha(v,v)>0$ wherever defined and at least one coefficient at the base point is positive.

A unitary connection also exists. Start with any connection $\nabla^0$ and define $\nabla$ by adding the unique endomorphism-valued $1$-form which removes the Hermitian-symmetric part of $\nabla^0h$; equivalently, glue locally trivial unitary connections by a partition of unity.

# Examples / Corollaries

For a Hermitian line bundle, $\mathfrak u(1)=i\mathbb R$, hence a unitary connection is locally $d+i\alpha$ for a real $1$-form $\alpha$. This is the setting of [[Def - U(1) Gauge Field and Electromagnetic Connection]]. Parallel transport of a unitary connection preserves $h$, because along a curve
$$\frac d{dt}h(s,t)=h(\nabla_{\dot\gamma}s,t)+h(s,\nabla_{\dot\gamma}t).$$

# Unlocked by This

Invariant inner products allow gauge-invariant norms such as $|F_A|^2$ and hence the Yang–Mills action. Spinor bundles in Seiberg–Witten theory are Hermitian bundles with compatible Clifford connections.
