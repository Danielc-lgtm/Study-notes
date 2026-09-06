---
type: topic
subject: gauge-theory
chapter: "Gauge Theory II"
title: "Gauge Theory II — Principal Bundles, Representations, and Bundle Classification"
tags: [geometry, gauge-theory, fibre-bundles, principal-bundles, representations]
---

# Notation Registry

$B$ is a smooth paracompact manifold, $G$ a Lie group with Lie algebra $\mathfrak g$, and $P\xrightarrow{\pi}B$ a right principal $G$-bundle. A left representation is $\rho:G\to\mathrm{GL}(V)$. We use the associated-bundle convention
$$
P\times_\rho V=(P\times V)/((p,v)\cdot g=(pg,\rho(g)^{-1}v)).
$$
A local section $s_\alpha:U_\alpha\to P$ determines transition functions by $s_\beta=s_\alpha g_{\alpha\beta}$; hence $g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}$.

# Motivation

Gauge Theory I began with vector bundles, whose fibres already carry linear coordinates. A gauge group such as $U(1)$ or $SU(2)$ is more primitive: it describes how admissible frames differ, independently of any particular representation on matter. A principal bundle packages those frames. Once $P$ is known, every representation of $G$ produces a vector bundle, and every equivariant map produces a section. One topological object can therefore support many kinds of fields.

The central problem in this chapter is global gluing. Locally, $P$ is merely $U\times G$. Globally, transition functions can wind in a way no change of local section removes. A reduction of structure group records extra geometry; a classifying map records the bundle's isomorphism class. The Hopf fibration is the running example because all three descriptions—free group action, transition cocycle, and characteristic integer—can be computed explicitly.

# Concept Map

## §2.1 Lie groups, actions, and representations

The needed Lie theory is recalled rather than duplicated:

- [[Def - Lie Group]], [[Def - Lie Algebra]], and [[Def - The Lie Algebra of a Lie Group]];
- [[Def - Exponential Map of a Lie Group]] and [[Thm - Naturality of the Exponential Map]];
- [[Def - Smooth Action of a Lie Group]], [[Thm - Orbit-Stabilizer for Lie Group Actions]], and [[Thm - Homogeneous Space is a Smooth Manifold]];
- [[Thm - The Closed Subgroup Theorem]].

The new bridge is **[[Def - Representation of a Lie Group]]**. Direct sums, tensor products, duals, exterior and symmetric powers, complexification, and differentiation to a Lie-algebra representation are the operations that later generate matter bundles. [[Ex - Weight Representations of U(1)]] records the integer weights, and [[Thm - Irreducible Representations of U(1) and SU(2)]] proves the rank-one compact classification used by the sources.

Two quotient criteria from the source will be used repeatedly. A free action of a
compact Lie group is proper, and its orbit space is a smooth manifold for which
the quotient map is a principal bundle. A free action of a discrete group has
the same conclusion when it is properly discontinuous; without that hypothesis
the quotient can fail to be Hausdorff, as for the translation action of
$\mathbb Q$ on $\mathbb R$. The source's calculations of $SO(2)\cong U(1)$,
$SU(2)\cong S^3$, the classical matrix Lie algebras, and the exponential map
are covered by the linked Differential Geometry XI pages and their examples.

## §2.2 Fibre bundles and principal bundles

- **[[Def - Fibre Bundle]]** — a locally trivial family with typical fibre $F$; pullback is the universal way to change the base.
- **[[Def - Principal G-Bundle]]** — a fibre bundle whose fibres are free transitive right $G$-spaces.
- **[[Thm - Principal Bundles are Locally Trivial via G-Action]]** — local sections and local trivializations are equivalent; a global section exists exactly when the principal bundle is trivial.
- **[[Def - The Hopf Bundle]]** — $S^{2n+1}\to\mathbb{CP}^n$ is the quotient by scalar $U(1)$ action; $S^7\to S^4$ is its quaternionic $SU(2)$ analogue.

> [!note] Exercises
> [[Exercise Index - §2.1 Fibre Bundles and Principal Bundles]]

## §2.3 Frames, representations, and associated bundles

- **[[Def - Frame Bundle of a Vector Bundle]]** and **[[Def - Orthonormal Frame Bundle]]** — linear or metric frames form principal bundles.
- **[[Def - Associated Bundle]]** and **[[Thm - Associated-Bundle Construction Yields a Bundle]]** — a representation turns principal frames into vector fibres.
- **[[Def - Homogeneous Bundle]]** — $G\to G/H$ is a principal $H$-bundle and $G\times_HV\to G/H$ is homogeneous.
- **[[Def - Extension and Reduction of Structure Group]]** — a homomorphism $G\to H$ extends a $G$-bundle; a reduction reverses this operation and records additional structure.

> [!note] Exercises
> [[Exercise Index - §2.2 Frame and Associated Bundles]]

## §2.4 Classification

- **[[Def - Universal Bundle and Classifying Space]]** — a universal principal bundle $EG\to BG$ turns pullback into a classification mechanism.
- **[[Thm - Classification of Principal Bundles by Maps to BG]]** — over a paracompact base, isomorphism classes of principal $G$-bundles correspond to homotopy classes $[B,BG]$.
- [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]] specializes this to $U(1)$ because $BU(1)\simeq\mathbb{CP}^\infty\simeq K(\mathbb Z,2)$.
- [[Ex - Quaternionic Hopf Bundle and SU(2) Classification]] explains why $BSU(2)\simeq\mathbb{HP}^\infty$ and why $SU(2)$-bundles over a closed four-manifold are measured by $c_2$.

## §2.5 Preview: characteristic geometry and Berry phase (developed in Gauge Theory IV)

The existing Pfaffian, Euler, Gauss–Bonnet, and Berry pages are preserved as previews. Their systematic derivation belongs to Gauge Theory IV, after curvature on principal bundles has been developed:

- [[Def - Pfaffian]], [[Def - The Euler Class of a Real Oriented Vector Bundle]], and [[Thm - Gauss-Bonnet-Chern Theorem]];
- [[Thm - Gauss-Bonnet for Closed Surfaces (Chern's Proof)]];
- [[Def - Berry Connection]] and [[Thm - Berry Phase Equals Holonomy of the Berry Connection]].

# Sources and Targets

Given local data, the usual target is a global bundle. Transition functions must satisfy a cocycle identity; changing local sections modifies them by a coboundary. Given a principal bundle and a field type, the target is an associated bundle determined by a representation. Given an $H$-bundle carrying suspected $G$-geometry, the target is a reduction of structure group. Given only the topology of $B$, the target is an isomorphism class, obtained from a homotopy class of maps $B\to BG$.

# Legal Operations

1. **Pull back:** $f:N\to B$ sends $P$ to $f^*P$ and preserves structure group.
2. **Form an associated bundle:** quotient $P\times V$ by the diagonal action, checking the inverse in the $V$ factor.
3. **Recover equivariant maps:** sections of $P\times_\rho V$ correspond to maps $\phi:P\to V$ satisfying $\phi(pg)=\rho(g)^{-1}\phi(p)$.
4. **Change local sections:** if $s'_\alpha=s_\alpha h_\alpha$, then $g'_{\alpha\beta}=h_\alpha^{-1}g_{\alpha\beta}h_\beta$.
5. **Extend structure group:** use $P\times_\varphi H$ for a homomorphism $\varphi:G\to H$.
6. **Test a reduction:** an $H$-bundle reduces to $G\subset H$ exactly when the associated $H/G$-bundle has a global section.
7. **Classify by pullback:** choose $f:B\to BG$ and form $f^*EG$; homotopic maps yield isomorphic bundles.

# Problem-Solving Strategy

Start by fixing left/right conventions. To prove a quotient construction is a bundle, first prove the action is free and proper, then build local trivializations; freeness alone is insufficient. To decide triviality, search for a global section or show a characteristic obstruction prevents one. To compare two cocycles, search for local functions $h_\alpha$ implementing a coboundary. To translate between geometry and representation theory, identify the principal frame bundle first and apply the relevant representation only afterward.

# Most Reusable Properties

- A principal fibre is a $G$-torsor: it resembles $G$ but has no preferred identity.
- Local sections are gauges; a global gauge exists exactly for a trivial principal bundle.
- One principal bundle produces many associated bundles.
- Reduction of structure group is equivalent to a section of a quotient-fibre bundle.
- Universal bundles convert bundle classification into homotopy theory.

# Bridges

Gauge Theory III adds connections, horizontal lifts, curvature, holonomy, and gauge transformations to this topological skeleton. Gauge Theory IV applies invariant polynomials to that curvature. Gauge Theory VI uses the reductions $SO(n)\leftarrow Spin(n)$ and $SO(n)\times U(1)\leftarrow Spin^c(n)$ to define spinor bundles.

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §§2.2.1–2.2.2 and §2.4.
- Konstantin Wernli, *Mathematical Gauge Theory*, Chapter 1 and §§2.1–2.2.
