---
type: topic
subject: gauge-theory
chapter: "Gauge Theory I"
title: "Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection"
tags: [geometry, gauge-theory, vector-bundles, electromagnetism]
---

# Notation Registry

Throughout, $M$ is a smooth manifold, $E\to M$ is a rank-$r$ real or complex vector bundle, $\Gamma(E)$ is its space of smooth sections, and $\Omega^k(M;E)=\Gamma(\Lambda^kT^*M\otimes E)$. A connection is written $\nabla$; in a local frame it is $d+A$, with curvature $F_A=dA+A\wedge A$.

For the electromagnetic specialization, $L\to M$ is a Hermitian line bundle, $q\in\mathbb R$ is the charge appearing in the representation $e^{i\theta}\mapsto e^{iq\theta}$, and a unitary frame writes
$$
\nabla=d+iqA,qquad A\in\Omega^1(M;\mathbb R),qquad F_\nabla=iqF,quad F=dA.
$$
A change of unitary frame $e'=e^{iq\chi}e$ gives
$$
A'=A+d\chi.
$$
Equivalently, if one actively transforms the coefficient of a fixed-frame section by $\psi'=e^{-iq\chi}\psi$, then $A'=A+d\chi$ and $(d+iqA')\psi'=e^{-iq\chi}(d+iqA)\psi$. These passive and active descriptions must not be mixed.

# Motivation

A derivative compares nearby values. For an ordinary function those values lie in one fixed vector space; for a section, $s(x)\in E_x$ and $s(y)\in E_y$ lie in different fibres. A connection is the additional rule that makes differentiation possible. Its curvature records the obstruction to making that comparison path-independent.

Gauge theory begins when the comparison rule itself is dynamical or physically observable. In electromagnetism, a charged wavefunction is locally a complex function only after choosing a unitary frame of a line bundle. Changing that frame changes the local potential $A$ but not the connection. The field strength is curvature, and a charged particle transported around a loop acquires its holonomy. Thus “gauge freedom” is not freedom to change the physical field; it is freedom to change a local representative of one global geometric object.

The chapter develops this claim in the smallest setting where every mechanism is visible. Principal bundles and non-abelian structure are deferred to [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]] and [[Gauge Theory III — Principal Connections, Curvature, Holonomy, and Gauge Symmetry]].

# Concept Map

## §1.1 Connections as differentiation between fibres

Before adding a connection, recall the bundle operations used throughout the sources. If
$E$ and $K$ are bundles over $M$, then $E\oplus K$, $E\otimes K$, $E^*$,
$\operatorname{Hom}(E,K)=E^*\otimes K$, and $\operatorname{End}E$ are formed
fibrewise and glued by the induced transition functions. A smooth map $f:N\to M$
produces the pullback bundle $f^*E\to N$. Sections form a
$C^\infty(M)$-module, not ordinarily a vector space with pointwise-independent
coefficients. These facts are developed in [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]];
here they matter because a connection must propagate through every one of these
operations by a Leibniz rule.

- **[[Def - Connection on a Vector Bundle]]**
  - A connection is a first-order operator $\nabla:\Gamma(E)\to\Omega^1(M;E)$ satisfying the Leibniz rule.
  - In a frame, $\nabla=d+A$ and $A'=g^{-1}Ag+g^{-1}dg$.
  - Connections form an affine space over $\Omega^1(M;\operatorname{End}E)$.
- **[[Thm - Existence of Connections via Partitions of Unity]]**
  - Local trivial connections glue because the coefficients of a partition of unity sum to one.
- **[[Ex - Connection on the Tangent Bundle of S^2 from the Round Metric]]**
  - The Levi–Civita connection is the basic nontrivial vector-bundle connection.

> [!note] Exercises
> [[Exercise Index - §1.2 Connections on Vector Bundles]]

## §1.2 Curvature: the failure of second derivatives to commute

- **[[Def - Curvature of a Vector-Bundle Connection]]**
  - $F_\nabla(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}$ and locally $F_A=dA+A\wedge A$.
- **[[Thm - Curvature is C-Infinity Linear in Sections]]**
  - All derivative terms cancel, so curvature is an $\operatorname{End}E$-valued $2$-form.
- **[[Thm - Bianchi Identity for a Vector-Bundle Connection]]**
  - $d_\nabla F_\nabla=0$ is the compatibility identity forced by $F_A=dA+A^2$.
- **[[Ex - Curvature of a Trivial Bundle with Trivial Connection is Zero]]**
  - Triviality of the bundle does not force zero curvature; the chosen trivial connection does.

## §1.3 Hermitian line bundles and electromagnetism

- **[[Def - Complex Line Bundle]]** and **[[Def - Hermitian Vector Bundle]]**
  - A unitary frame reduces the local connection matrix to $iqA$ with $A$ real.
- **[[Def - U(1) Gauge Field and Electromagnetic Connection]]**
  - The electromagnetic potential is the local representative $A$; the field strength $F=dA$ is its curvature after removing the factor $iq$.
- **[[Def - Gauge Transformation]]**
  - Passive frame change and active transformation are two descriptions of the same covariance equation.
- **[[Ex - Gauge-Invariant Coupling of Schrödinger to EM Field]]**
  - Minimal coupling replaces $d$ by $d+iqA$ because ordinary differentiation does not preserve local phase covariance.

> [!note] Exercises
> [[Exercise Index - §1.3 Electromagnetic Connection]]

## §1.4 Global effects: flux and holonomy

- **[[Def - Wilson Line and Holonomy of a Connection]]**
  - Parallel transport along a path is the path-ordered exponential; for $U(1)$ path ordering disappears.
- **[[Def - The Dirac Monopole Bundle]]**, **[[Ex - Dirac Monopole as a Non-Trivial Bundle over S^2]]**, and **[[Thm - Dirac Quantization Condition]]**
  - Local potentials patch to a global connection precisely when the normalized flux is integral.
- **[[Ex - The Aharonov-Bohm Phase from the Magnetic Solenoid]]**
  - A flat connection may have nontrivial holonomy when the base is not simply connected.

> [!note] Exercises
> [[Exercise Index - §1.4 Monopoles, Aharonov-Bohm, and Topological Effects]]

## §1.5 Topological enrichment: zeros of vector fields

The existing vector-field material is preserved as an enrichment linking local indices to global topology. It is not needed for the connection–electromagnetism development.

- [[Def - Index of a Vector Field at a Zero]]
- [[Thm - Poincare-Hopf Theorem]] and [[Thm - Hairy Ball Theorem]]
- [[Ex - Index of the Source-Sink Vector Field on the Sphere]]
- [[Ex - Stiefel Vector Field on the Odd Sphere is Nowhere-Zero]]
- [[Exercise Index - §1.1 Vector Fields and Euler Characteristic]]

# Sources and Targets

A typical input is a bundle whose local coefficients must be differentiated covariantly. The immediate targets are a connection, its curvature, and gauge-covariant observables. Local frames turn the problem into matrix-valued differential forms; frame-change laws decide which expressions are global. In the abelian case, the hierarchy compresses to
$$
\text{unitary connection }\nabla
\longrightarrow \text{local potential }A
\longrightarrow \text{curvature }F=dA
\longrightarrow \text{flux and holonomy}.
$$
Local questions are answered by choosing a frame. Global questions are answered by checking overlap data, periods, or holonomy.

# Legal Operations

1. **Choose a local frame.** Write $s=eu$ and $\nabla=d+A$; never treat $A$ as a global tensor.
2. **Change frame covariantly.** Use $A'=g^{-1}Ag+g^{-1}dg$ and $F'=g^{-1}Fg$.
3. **Take differences of connections.** The inhomogeneous terms cancel, so $\nabla'-\nabla\in\Omega^1(M;\operatorname{End}E)$.
4. **Square the covariant derivative.** On sections, $d_\nabla^2=F_\nabla\wedge(-)$.
5. **Specialize to rank one.** Commutators vanish, hence $F=dA$ and $dF=0$.
6. **Integrate curvature over a closed surface.** With the convention
   $c_1(L)=[iF_\nabla/(2\pi)]$, a Hermitian line bundle has integral normalized
   curvature periods. Reversing this convention reverses every displayed Chern
   number but changes no integrality statement.
7. **Integrate the connection along a path.** In $U(1)$, transport is $\exp(-iq\int_\gamma A)$ for the convention $\nabla=d+iqA$.

# Problem-Solving Strategy

First type every object: global connection, local potential, global curvature, local coefficient of a section. Next choose whether the transformation is passive or active and keep that choice fixed. Compute locally, then prove the answer glues using its transformation law. For a local differential question, calculate $F=dA+A^2$. For a global question, inspect transition functions and periods. For an observable attached to a loop, compute holonomy; Stokes' theorem may replace it by curvature flux only when a suitable spanning surface and trivialization exist.

# Most Reusable Properties

- Connections exist but are not canonical; their differences are tensors.
- Curvature is global although the connection matrix is not.
- Flat means locally pure gauge, not necessarily globally trivial.
- In an abelian theory $A\wedge A=0$, but topology may still obstruct a global potential.
- Gauge covariance is a bookkeeping identity forced by changing local frames.

# Bridges

- [[Riemannian Geometry I — Connections and Covariant Differentiation]] develops affine connections, parallel transport, and Levi–Civita geometry.
- [[Gauge Theory III — Principal Connections, Curvature, Holonomy, and Gauge Symmetry]] replaces frame matrices by a global principal connection.
- Gauge Theory IV will turn invariant polynomials in curvature into characteristic classes.
- Gauge Theory V will derive Maxwell and Yang–Mills equations from the Hodge star and action principles.

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §2.1 and §2.3.
- Konstantin Wernli, *Mathematical Gauge Theory*, §§3.1–3.2 for the electromagnetic specialization and Hodge-sign conventions developed later in Gauge Theory V.
