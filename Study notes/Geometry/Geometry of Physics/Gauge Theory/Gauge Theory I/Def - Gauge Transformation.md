---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
tags: [gauge-theory, gauge-transformation, bundle-automorphism]
---

# Prerequisite Concepts

- [[Def - Connection on a Vector Bundle]]

# Notation

Let $E\to M$ be a rank-$r$ vector bundle with connection $\nabla$. A gauge transformation is written $u:E\to E$. In a local frame it is a map $g:U\to\mathrm{GL}_r(\mathbb K)$. For a Hermitian bundle, $g$ takes values in $U(r)$.

# The Definition

> [!definition] Gauge transformation
> A **gauge transformation** is a smooth vector-bundle automorphism $u:E\to E$ covering $\operatorname{id}_M$. It acts on sections by $s\mapsto us$ and on connections by
> $$
> (u\cdot\nabla)_Xs=u\bigl(\nabla_X(u^{-1}s)\bigr).
> $$
> This action is characterized by covariance:
> $$(u\cdot\nabla)(us)=u(\nabla s).$$

If $\nabla=d+A$ and $u$ is represented by $g$, then
$$
A^g=gAg^{-1}-dg\,g^{-1},\qquad F_{A^g}=gF_Ag^{-1}.
$$
This is the **active** convention. A passive frame change $e'=eg$ instead gives
$$
A'=g^{-1}Ag+g^{-1}dg,\qquad F'=g^{-1}F_Ag.
$$
The formulas look different because the same matrix $g$ is being used for inverse operations. Either convention is valid; mixing them in one calculation is not.

# Axiom Motivation

Gauge-equivalent pairs encode the same comparison rule in different fibre coordinates. Curvature transforms homogeneously because it is a tensor. The connection matrix transforms inhomogeneously because differentiating the changing frame produces an additional $dg$ term.

# Examples / Corollaries

For $\nabla=d+iqA$ on a line bundle, take the active transformation $u=e^{-iq\chi}$. Then
$$
\psi^u=e^{-iq\chi}\psi,\qquad A^u=A+d\chi,\qquad
(d+iqA^u)\psi^u=e^{-iq\chi}(d+iqA)\psi.
$$
Thus $F=dA$ and the norm $|\psi|$ are invariant, while $A$ and $\psi$ separately depend on gauge.

# Legal Operations

Gauge-invariant quantities descend to the quotient $\mathcal A(E)/\mathcal G(E)$. Gauge-covariant quantities transform in a representation and may be combined by invariant pairings. A bare local connection matrix is neither invariant nor tensorial.

# Unlocked by This

The stabilizer of a connection and the singularities of the gauge quotient become central in moduli-space theory. Gauge Theory III develops the intrinsic principal-bundle version.
