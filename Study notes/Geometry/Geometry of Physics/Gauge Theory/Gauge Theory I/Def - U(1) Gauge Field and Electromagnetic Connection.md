---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Complex Line Bundle"
  - "Def - Connection on a Vector Bundle"
tags: [gauge-theory, electromagnetism, u1, connection]
---

# Notation

Let $L\to M$ be a Hermitian line bundle and fix a real charge $q$. A local unitary frame $e$ identifies a section with $s=e\psi$. We use the convention
$$\nabla(e\psi)=e(d\psi+iqA\psi),$$
where $A$ is real. If physical units are retained, replace $q$ by $q/\hbar$ (and by $q/(\hbar c)$ in Gaussian spatial minimal coupling).

# Axiom Motivation

A charged field has a phase which can be described only relative to a chosen local unitary frame. Ordinary differentiation detects changes of that frame as if they were changes of the field. The connection term cancels this spurious derivative. Its curvature is independent of the frame and is therefore the electromagnetic field strength.

# The Definition

> [!definition] Electromagnetic connection
> A **$U(1)$ gauge field** on $L$ is a unitary connection $\nabla$. In a unitary frame it has the unique form
> $$\nabla=d+iqA,qquad A\in\Omega^1(U;\mathbb R).$$
> The real $1$-form $A$ is the **local gauge potential**. The real electromagnetic field strength is
> $$F=dA,$$
> so the curvature of $\nabla$ is $F_\nabla=iqF$.

If $e'=e^{iq\chi}e$, then $A'=A+d\chi$. Hence $F'=dA'=F$. A local potential is not itself a global observable; the connection and its curvature are.

On an oriented Lorentzian four-manifold, the source-free Bianchi equation is $dF=0$. Once a metric and Hodge star are fixed, the inhomogeneous Maxwell equation is $d{\star}F=J$ in the normalization where the current $3$-form is $J$. Gauge Theory V derives these equations and records signature-dependent signs.

# Relate to Other Fields / Compression

On a trivial line bundle a connection can be represented by one global $A$. On a nontrivial line bundle only local potentials $A_\alpha$ exist, with $A_\beta=A_\alpha+d\chi_{\alpha\beta}$ on overlaps. Their derivatives agree and define one global closed $2$-form $F$ whose normalized periods encode the first Chern class.

# Examples / Corollaries

- If $A=d\chi$ on a contractible region, changing frame removes $A$ and $F=0$.
- A flat connection can still have nontrivial loop holonomy on a nonsimply-connected region; this is the Aharonov–Bohm mechanism.
- A monopole field has nonzero flux through $S^2$, so no single global potential exists on $S^2$.

# Unlocked by This

[[Ex - Gauge-Invariant Coupling of Schrödinger to EM Field]] derives minimal coupling, while [[Def - Wilson Line and Holonomy of a Connection]] identifies the gauge-invariant phase associated to transport.
