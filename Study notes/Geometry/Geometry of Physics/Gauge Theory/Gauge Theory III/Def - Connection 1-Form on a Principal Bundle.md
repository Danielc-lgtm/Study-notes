---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Fundamental Vector Field of a Principal Bundle"
  - "Def - Lie-Algebra-Valued Differential Form"
tags: [gauge-theory, principal-connection, connection-form]
---

# Prerequisite Concepts

- [[Def - Fundamental Vector Field of a Principal Bundle]]
- [[Def - Lie-Algebra-Valued Differential Form]]

# Notation

Throughout, $P\xrightarrow{\pi}M$ is a right principal $G$-bundle,
$R_g(p)=pg$, and $\xi_P(p)=\left.\frac d{dt}\right|_0p\exp(t\xi)$.

# Axiom Motivation

A fibre of $P$ is a torsor: its points are choices of gauge, not vectors that
can be subtracted. To compare choices over nearby base points, one must first
separate genuine displacement in $M$ from motion caused only by the right
$G$-action. A connection form performs this separation by returning the
Lie-algebra element responsible for the vertical part of a tangent vector.

The reproduction axiom is forced by this interpretation. If it were dropped,
the zero form would qualify, although it cannot distinguish any vertical
motion and its kernel contains the entire fibre direction. Requiring
$\omega(\xi_P)=\xi$ makes $\omega|_{V_pP}$ the inverse of the canonical map
$\mathfrak g\to V_pP$.

Reproduction alone is not enough. One could choose unrelated complements at
$p$ and $pg$, so translating a horizontal lift along a fibre might cease to be
horizontal. Equivariance excludes this defect. Its adjoint factor is not an
optional convention: for a right action,
$(R_g)_*\xi_P=(\operatorname{Ad}_{g^{-1}}\xi)_P$, so reproduction at both
$p$ and $pg$ forces precisely $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$.

Together the axioms ensure that $\ker\omega$ is a smooth, right-invariant
horizontal complement. Thus the algebraic definition is designed so that it
can be integrated into [[Def - Parallel Transport of a Principal Connection|parallel transport]] and pulled down to local gauge potentials.

# The Definition

> [!definition] Principal connection form
> A **principal connection** on a right principal $G$-bundle $P\to M$ is a form $\omega\in\Omega^1(P;\mathfrak g)$ such that
> $$
> \omega_p(\xi_P(p))=\xi,\qquad
> R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega.
> $$

The first axiom says that $\omega$ reads the infinitesimal group generator of a vertical vector. The second says that changing the point in the torsor changes this generator by the adjoint representation.

# Horizontal Projection

The horizontal space is $H_p=\ker\omega_p$. Every $X\in T_pP$ decomposes uniquely as
$$X=X^H+(\omega_pX)_P(p).$$
Consequently the vertical projection is $X\mapsto(\omega X)_P$ and the horizontal projection is $X\mapsto X-(\omega X)_P$.

# Trivial Bundle

On $P=M\times G$ let $\theta=g^{-1}dg$ be the left Maurer–Cartan form. Every principal connection is uniquely
$$
\omega_{(x,g)}=\operatorname{Ad}_{g^{-1}}A_x+\theta_g
$$
for some $A\in\Omega^1(M;\mathfrak g)$. Pullback by the canonical section $s(x)=(x,e)$ gives $s^*\omega=A$. The connection is the product flat connection exactly when $A=0$.

# Affine Structure

If $\omega'$ and $\omega$ are connections, their difference is horizontal and $\operatorname{Ad}$-equivariant, so it descends to an element of $\Omega^1(M;\operatorname{Ad}P)$. Conversely every such form added upstairs produces another connection. Therefore the space of principal connections is affine over $\Omega^1(M;\operatorname{Ad}P)$.


# Examples and Non-Examples

The product connection on $M\times G$ is $g^{-1}dg$; its horizontal vectors
are exactly those tangent to $M\times\{g\}$. More generally, inserting any
$A\in\Omega^1(M;\mathfrak g)$ in the trivial-bundle formula above produces a
connection and shows concretely why a local potential is not itself invariant.

The Levi–Civita connection becomes a principal $O(n)$-connection on the
orthonormal frame bundle: a moving frame is horizontal precisely when every
frame vector is parallel. This is the same construction as gauge theory, with
orthonormal frames playing the role of gauges.

The form $\pi^*\alpha$ for $\alpha\in\Omega^1(M;\mathfrak g)$ is generally a
non-example because it vanishes on every vertical vector and therefore fails
reproduction. The Maurer–Cartan form alone is a global formula only after a
product trivialization; writing it on a nontrivial bundle presupposes the
missing global gauge.

**True name:** a principal connection form is the equivariant vertical
projection $TP\to P\times\mathfrak g$, written after identifying each vertical
tangent space with $\mathfrak g$.

**Calibration check.** On a fundamental vector it returns its generator; on a
horizontal vector it returns zero; after right translation its value changes
by $\operatorname{Ad}_{g^{-1}}$.

# Unlocked by This

The kernel gives [[Def - Horizontal Subspace|horizontal spaces]], integration
gives [[Thm - Horizontal Lift Existence and Uniqueness|horizontal lifts]], and
the failure of the horizontal distribution to be integrable is measured by
[[Def - Curvature 2-Form on a Principal Bundle|curvature]].
