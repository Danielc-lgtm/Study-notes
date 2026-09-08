---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Holonomy Group of a Connection"
  - "Def - Path-Ordered Exponential"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
  - "Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Transformation of Local Connection and Curvature Forms"
  - "Thm - The Maurer-Cartan Equation"
  - "Def - The Maurer-Cartan Form"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is an **abelian** matrix Lie group, $G \subset GL(n; \mathbb{K})$ with $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$; the guiding example is the circle group $G = U(1) = \{z \in \mathbb{C} : |z| = 1\}$. Its Lie algebra is $\mathfrak{g} = T_e G$, and because $G$ is abelian the bracket on $\mathfrak{g}$ vanishes identically, $[\xi, \eta] = 0$ for all $\xi, \eta \in \mathfrak{g}$; for $U(1)$ we have $\mathfrak{g} = i\mathbb{R}$. We write $\exp : \mathfrak{g} \to G$ for the Lie-group exponential map; for a matrix group this is the matrix exponential $\exp(X) = \sum_{k \ge 0} X^k / k!$, and for an abelian group it is a homomorphism, $\exp(\xi + \eta) = \exp(\xi)\exp(\eta)$.

We work with a principal $G$-bundle $\pi : P \to M$ over a smooth manifold $M$, carrying a [[Def - Connection on a Principal Bundle|principal connection]] $\omega \in \Omega^1(P; \mathfrak{g})$. A **trivialising open set** is an open $U_\alpha \subset M$ on which a smooth [[Thm - Sections of a Principal Bundle and Triviality|local section]] $s_\alpha : U_\alpha \to P$ exists. The associated [[Def - Local Connection Form and Gauge Potential|local connection form]] (gauge potential) is
$$A_\alpha := s_\alpha^{*}\omega \in \Omega^1(U_\alpha; \mathfrak{g}),$$
and the **local curvature form** is $F_\alpha := s_\alpha^{*}\Omega = dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]$, where $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ is the [[Def - Curvature of a Principal Connection|curvature of the connection]]. Because $[\,\cdot\,,\,\cdot\,]$ vanishes on $\mathfrak{g}$, the second term drops out and
$$F_\alpha = dA_\alpha .$$
We shall see in Step 0 of the proof that for abelian $G$ these local forms agree on overlaps and glue to a single **global curvature** $F \in \Omega^2(M; \mathfrak{g})$; we write $F = dA_\alpha$ for its restriction to any chart.

A **loop** at $m \in M$ is a piecewise smooth curve $c : [0,1] \to M$ with $c(0) = c(1) = m$; we say $c$ **bounds** a compact oriented surface $S \subset M$ (a smooth $2$-manifold with boundary, given an orientation) when $\partial S = c$ as oriented manifolds. For a point $p \in P_m := \pi^{-1}(m)$, the [[Def - Holonomy Group of a Connection|holonomy]] $\operatorname{hol}_p(c) \in G$ is the unique group element with
$$\Gamma(c)(p) = p \cdot \operatorname{hol}_p(c),$$
where $\Gamma(c) : P_m \to P_m$ is [[Def - Parallel Transport in a Principal Bundle|parallel transport]] around $c$. We show below that for abelian $G$ this element is independent of $p$, and write it $\operatorname{hol}(c)$.

We write $\theta \in \Omega^1(G; \mathfrak{g})$ for the [[Def - The Maurer-Cartan Form|left Maurer–Cartan form]]; for a matrix group $\theta = g^{-1}\,dg$, and for a smooth map $g : U_\alpha \to G$ the pull-back $g^{*}\theta \in \Omega^1(U_\alpha; \mathfrak{g})$ is $g^{-1}\,dg$ read on $U_\alpha$. Finally, $\mathcal{P}\exp\big({-}\int_0^{t} A\big)$ denotes the [[Def - Path-Ordered Exponential|path-ordered exponential]] of a continuous matrix-valued curve $A : [0,L] \to \operatorname{Mat}(n \times n; \mathbb{K})$, the solution operator of $\dot v = -A(t)\,v$.

> [!warning] Convention: local connection form and parallel-transport sign
> Bär (*Gauge Theory*, Remark 2.6.9) writes $\omega_\alpha$ for the local connection form $s_\alpha^{*}\omega$ and $\Gamma(c)$ for parallel transport, and states the abelian holonomy formula as $\Gamma(c) = \exp\big({-}\int_c \omega_\alpha\big) = \exp\big({-}\int_S \Omega_\alpha\big)$. The series writes $A_\alpha := s_\alpha^{*}\omega$ for the potential and $F = dA_\alpha$ for the abelian curvature, and records holonomy as the group element $\operatorname{hol}(c)$ with $\Gamma(c)(p) = p \cdot \operatorname{hol}(c)$. The two agree: for abelian $G$, $\Gamma(c)$ is right multiplication by $\operatorname{hol}(c)$, so the displayed scalar $\exp(-\int_c A_\alpha)$ *is* $\operatorname{hol}(c)$. The minus sign in $\exp(-\int)$ is inherited from the parallel-transport ODE $\dot v = -A(t) v$ (series convention $\nabla = d + A$, horizontal-lift equation $\dot h = -A_\alpha(\dot c)\,h$); the other common sign convention $\nabla = d - A$ flips it to $\exp(+\int)$.

---

# Statement

> **Theorem (holonomy of an abelian connection).** Let $\pi : P \to M$ be a principal $G$-bundle with connection $\omega$, where $G \subset GL(n; \mathbb{K})$ is an **abelian** matrix Lie group, and let $A_\alpha = s_\alpha^{*}\omega$ be the local connection form on a trivialising set $U_\alpha$ with global curvature $F = dA_\alpha$. Then the following hold.
>
> **(a) The general loop formula.** For every piecewise smooth loop $c$ contained in $U_\alpha$,
> $$\operatorname{hol}(c) = \exp\!\Big({-}\int_c A_\alpha\Big) \in G,$$
> and this element is independent of the base point $p \in P_{c(0)}$ and of the choice of trivialising section $s_\alpha$ on $U_\alpha$.
>
> **(b) The curvature-flux formula.** If, in addition, $c$ bounds a compact oriented surface $S \subset U_\alpha$ with $\partial S = c$, then
> $$\operatorname{hol}(c) = \exp\!\Big({-}\int_c A_\alpha\Big) = \exp\!\Big({-}\int_S F\Big).$$
>
> **(c) Curvature detects holonomy.** If the curvature does not vanish, $F \ne 0$, then there is a loop with nontrivial holonomy: some piecewise smooth loop $c$ has $\operatorname{hol}(c) \ne e$.

For the circle group $G = U(1)$ these read, with $A_\alpha = i a$ for a real $1$-form $a$ and $F = i\, da$,
$$\operatorname{hol}(c) = \exp\!\Big({-}i\int_c a\Big) = \exp\!\Big({-}i\int_S da\Big) \in U(1),$$
so the holonomy of a $U(1)$-connection around a loop is the phase $e^{-i \Phi}$, where $\Phi = \int_S da$ is the *magnetic flux* of the curvature through any surface the loop bounds.

---

# Motivation

Parallel transport around a loop, encoded in the [[Def - Holonomy Group of a Connection|holonomy]] element $\operatorname{hol}(c)$, is in general an intractable object: it is the endpoint of an ordinary differential equation with a time-dependent, non-commuting coefficient, and it depends on the whole loop $c$, not merely on the region the loop encloses. The [[Def - Path-Ordered Exponential|path-ordered exponential]] exists precisely because one cannot in general write the solution as $\exp$ of an integral — the values $A_\alpha(\dot c(t))$ at different times do not commute, and there is an *ordering problem*. The present theorem says that for an abelian structure group the ordering problem evaporates, and holonomy becomes something one can actually compute: a single exponential of an integral, and — through Stokes' theorem — an exponential of the total curvature caught inside the loop.

This is the first place in the series where curvature acquires an *operational* meaning rather than a definitional one. Curvature was defined as the obstruction $F_\nabla = d^\nabla \circ d^\nabla$ to the covariant derivative squaring to zero, or as $d\omega + \tfrac12[\omega \wedge \omega]$ on the total space; those are formulas. Here curvature is measured: it is exactly what a loop of parallel transport detects. A flat connection ($F = 0$) transports a fibre around any small loop back to itself; a curved connection ($F \ne 0$) rotates it by an amount equal to the flux of $F$. Part (c) turns this into a converse — nonzero curvature is not merely a local invariant but is *seen* by holonomy — which is the seed of the entire correspondence between curvature integrals and topological invariants developed from chapter VI onward.

The abelian case is not a toy. It is the mathematics of electromagnetism. A connection on a principal $U(1)$-bundle is an electromagnetic potential $A_\alpha = i(\phi\,dt - \mathbf{A}\cdot d\mathbf{x})$; its curvature $F$ is the electromagnetic field strength; and the holonomy $\exp(-i\int_S F)$ around a spatial loop is the Aharonov–Bohm phase acquired by a charged particle encircling a magnetic flux. That the phase depends only on the enclosed flux, and can be nonzero even where the field itself is zero along the particle's path (part (b) needs $F$ only on the spanning surface $S$, not on $c$), is precisely the physical content of the Aharonov–Bohm effect and, run in reverse, of Dirac's quantisation of magnetic charge in chapter VII.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is "$G$ abelian and $c$ a loop in one chart". The skill is recognising when a problem hands you this input in disguise.

The first disguised source is **a structure group that is abelian only after restriction or reduction**. A connection whose holonomy group $\operatorname{Hol}(\omega)$ happens to lie in an abelian subgroup $T \subset G$ (for instance a maximal torus) behaves, on the sub-bundle it preserves, exactly like an abelian connection: all the transport operators commute, so the ordering problem disappears on that reduced bundle and the theorem applies verbatim. The bridge $B \Rightarrow A$ is that a connection with abelian holonomy reduces its structure group to the closure of $\operatorname{Hol}(\omega)$, which is an abelian, hence (for compact $G$) toral, subgroup; on the reduction the hypothesis holds. *Example problem:* a diagonal $U(1)^n \subset U(n)$ connection on a Hermitian bundle splits into line bundles, and its holonomy is computed line by line by the theorem, giving $n$ independent Aharonov–Bohm phases.

The second disguised source is **a connection whose local form is closed, $dA_\alpha = 0$, on a non-simply-connected chart**. Flatness ($F = 0$) is the degenerate case of the theorem: part (a) still gives $\operatorname{hol}(c) = \exp(-\int_c A_\alpha)$, but now $A_\alpha$ is closed, so the integral $\int_c A_\alpha$ depends only on the de Rham class $[c] \in H_1(U_\alpha; \mathbb{R})$ and the periods of $A_\alpha$. The bridge is that "closed potential on a chart with topology" is the input under which holonomy becomes a homomorphism on $H_1$ — the monodromy of a flat connection, developed in §5.4. *Example problem:* the flat connection $A = i\,a\,d\theta$ on the trivial bundle over the annulus (or the circle) has holonomy $e^{-2\pi i a}$ around the generating loop, computed as a period even though no surface $S$ is available inside the chart.

The third disguised source is **any problem that supplies a two-dimensional region and a field to integrate over it**, phrased without any bundle at all. Whenever one is asked for the total flux of a closed or exact $2$-form through a surface and told to compare it around the boundary, the abelian holonomy theorem is the statement that the boundary integral and the surface integral agree up to $\exp$; recognising the potential $A_\alpha$ as a connection turns a Stokes computation into a transport computation. The bridge is that Stokes' theorem for the exact form $F = dA_\alpha$ *is* the equality in part (b). *Example problem:* the [[Ex - Holonomy around a Spherical Cap is the Solid Angle|solid-angle holonomy of a spherical cap]] — the transport phase around a latitude circle equals the enclosed solid angle — is exactly this theorem applied to the Hopf connection, with $S$ the cap.

**Targets (Output Amplification)**

Combine part (b) with **a surface whose boundary loop is contractible to a point**, and shrink $S$ to a point: the flux $\int_S F$ tends to zero, so $\operatorname{hol}(c) \to e$, and the leading correction is $\operatorname{hol}(c) = e - \int_S F + \cdots$. The extra ingredient is a Taylor expansion of $\exp$; the payoff is the **infinitesimal reading of curvature**, that $F$ is the density of holonomy per unit area, which is proved in full and to higher order (including the non-abelian $A \wedge A$ correction) in [[Thm - Curvature is the Infinitesimal Holonomy|Curvature is the Infinitesimal Holonomy]].

Combine part (b) with **the integrality of the first Chern class**. Over a closed surface $\Sigma$ decomposed into two caps meeting along a loop $c$, the two holonomy computations $\exp(-\int_{S_+} F)$ and $\exp(-\int_{S_-} F)$ (with opposite orientations) must give inverse group elements because they compute the same transport in the two trivialisations; their consistency forces $\int_\Sigma F \in 2\pi i\,\mathbb{Z}$ for $U(1)$. The extra ingredient is the transition-function comparison on the overlap; the payoff is **Dirac's quantisation condition** and the integrality theorem $c_1(L) \in H^2(M; \mathbb{Z})$, taken up in chapter VII.

Combine part (a) with **the fundamental group of the base**, in the flat case $F = 0$: the assignment $[c] \mapsto \operatorname{hol}(c)$ becomes a homomorphism $\pi_1(M, m) \to G$. The extra ingredient is homotopy invariance of holonomy for flat connections; the payoff is the **monodromy correspondence** between flat abelian connections and characters of $\pi_1$, i.e. the identification $\mathcal{M}^\flat_{U(1)}(M) \cong \operatorname{Hom}(\pi_1(M), U(1))$ established in [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy theorem]].

---

# Why Is It True

Picture the circle group. A $U(1)$-connection assigns to each infinitesimal step of a loop a small phase rotation $\exp(-A_\alpha(\dot c)\,dt)$; parallel transport composes these rotations along the loop. For a *non-abelian* group the order of composition matters — rotating first about one axis and then another is not the same as reversing the order — and this is the entire reason the path-ordered exponential cannot collapse to $\exp$ of the summed generator. For an abelian group all these infinitesimal rotations commute, so their ordered product is just the exponential of their sum, and the sum of $A_\alpha(\dot c(t))\,dt$ along the loop is the line integral $\int_c A_\alpha$. That is part (a): abelianness dissolves the ordering, and holonomy becomes $\exp$ of an integral.

Now Stokes. The line integral $\int_c A_\alpha$ around the boundary of a surface equals the surface integral $\int_S dA_\alpha$ of its exterior derivative — this is Stokes' theorem, and $dA_\alpha$ is exactly the abelian curvature $F$. So the phase around the loop is the exponential of the total curvature flux threading any surface the loop bounds. That is part (b), and it explains why the phase is insensitive to how the loop wiggles: only the enclosed flux counts.

> **The mechanism in one sentence: for an abelian structure group the ordered transport product collapses to $\exp$ of the integrated connection because all infinitesimal transports commute, and Stokes' theorem then rewrites the loop integral of the connection as the surface flux of its curvature.**

Part (c) is the converse read of the same fact. If $F$ is nonzero somewhere, choose a tiny disc $S$ where its flux is a small nonzero element of $\mathfrak{g}$. Since $\exp$ is a local diffeomorphism near $0 \in \mathfrak{g}$, a small nonzero flux exponentiates to a group element different from the identity. So the loop bounding that disc has nontrivial holonomy — curvature that exists is curvature that transport can feel.

---

# What Makes This Hard

The single subtle point is that holonomy is an *intrinsic* object — defined by $\Gamma(c)(p) = p \cdot \operatorname{hol}_p(c)$ without reference to any trivialisation — while the formula $\exp(-\int_c A_\alpha)$ is written in a chosen local section $s_\alpha$, and $A_\alpha$ changes when the section changes. One must check that the answer does not: two sections differ by a gauge $g$, the potentials differ by the pure-gauge term $g^{*}\theta$, and the extra contribution $\int_c g^{*}\theta$ is a period of the Maurer–Cartan form, which for a loop lies in the kernel of $\exp$ (it is $2\pi i\,\mathbb{Z}$ for $U(1)$) and therefore leaves $\exp(-\int_c A_\alpha)$ unchanged. Skipping this check leaves the formula ill-defined. The second, easier-to-miss point is that "abelian" is used *twice*: once to collapse the path-ordered exponential (part (a)), and once, silently, to know that the local curvature forms agree on overlaps so that $F = dA_\alpha$ is a single global $2$-form (the surface $S$ in part (b) can cross chart boundaries only because $F$ is globally defined). The common error is to prove part (b) inside one chart and forget that the statement quantifies over surfaces, which for the standard applications (the sphere, the torus) are not contained in any single trivialising set.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce holonomy to the path-ordered exponential of the local connection form via the horizontal-lift ODE; collapse the path-ordered exponential to an ordinary exponential using abelianness; rewrite the resulting loop integral as a surface flux by Stokes; and clean up by checking independence of the base point and the trivialisation, then read off the nonvanishing consequence.

**Subgoal decomposition:**

1. **Holonomy is the path-ordered exponential of $A_\alpha(\dot c)$.** Show that in the trivialisation $s_\alpha$, with $p = s_\alpha(m)$, one has $\operatorname{hol}_p(c) = \mathcal{P}\exp\big({-}\int_0^1 A_\alpha(\dot c(t))\,dt\big)$.
   - *Hint:* The horizontal lift of $c$ through $p$ is $\tilde c(t) = s_\alpha(c(t)) \cdot h(t)$ with $h(0) = e$; horizontality reduces to $\dot h = -A_\alpha(\dot c)\,h$, whose solution operator is the path-ordered exponential.
   - *Why needed:* It turns the geometric holonomy into an ODE quantity we can manipulate algebraically.

2. **The ordered exponential collapses for commuting coefficients.** Show that if all $A(t)$ take values in an abelian subalgebra, then $\mathcal{P}\exp\big({-}\int_0^t A\big) = \exp\big({-}\int_0^t A(\tau)\,d\tau\big)$.
   - *Hint:* Differentiate the ordinary exponential of the integral termwise and use commutativity to pull $A(t)$ to the front; it solves the same ODE with the same initial value, so uniqueness identifies the two.
   - *Why needed:* This is where "abelian" is spent to remove the ordering; it produces $\exp(-\int_c A_\alpha)$.

3. **Stokes rewrites the loop integral as a surface flux.** Show $\int_c A_\alpha = \int_S dA_\alpha = \int_S F$ when $\partial S = c$ and $S \subset U_\alpha$.
   - *Hint:* Apply Stokes' theorem to the $\mathfrak{g}$-valued $1$-form $A_\alpha$ componentwise; $dA_\alpha = F$ because the bracket term in the curvature vanishes.
   - *Why needed:* It converts part (a) into the flux formula of part (b).

3'. **The answer is independent of base point and trivialisation.** Show $\operatorname{hol}_{pg}(c) = \operatorname{hol}_p(c)$ for abelian $G$, and that changing $s_\alpha$ to $s_\alpha \cdot g$ changes $\int_c A_\alpha$ by $\int_c g^{*}\theta \in \ker \exp$.
   - *Hint:* Base point: $\operatorname{hol}_{pg} = g^{-1}\operatorname{hol}_p\,g = \operatorname{hol}_p$ by abelianness. Trivialisation: $\int_c g^{*}\theta$ is a period of the Maurer–Cartan form; exhibit it as the logarithm of a loop in $G$ and conclude $\exp(-\int_c g^{*}\theta) = e$.
   - *Why needed:* Without it the formula is not well-defined and part (a)'s claim of intrinsic value is unproved.

4. **Nonzero curvature yields nontrivial holonomy.** Show that if $F \ne 0$ there is a loop $c$ with $\operatorname{hol}(c) \ne e$.
   - *Hint:* Localise where $F \ne 0$, take a small coordinate square $S$; then $\int_S F$ is small and nonzero, and $\exp$ is injective near $0$.
   - *Why needed:* It is the converse content of the theorem, part (c).

---

# Lemma Decomposition

> [!note]- Lemma 1: For a matrix group, holonomy in a trivialisation is the path-ordered exponential of the local connection form
> **Statement:** Let $G \subset GL(n; \mathbb{K})$ be a matrix Lie group (not necessarily abelian), $\omega$ a connection on $P \to M$, $U_\alpha$ a trivialising set with section $s_\alpha$, and $c : [0,1] \to U_\alpha$ a piecewise smooth loop at $m = c(0) = c(1)$. Put $p := s_\alpha(m)$. Then
> $$\operatorname{hol}_p(c) = \mathcal{P}\exp\!\Big({-}\int_0^1 A_\alpha(\dot c(t))\,dt\Big),$$
> the path-ordered exponential of the continuous matrix curve $t \mapsto A_\alpha(\dot c(t)) \in \mathfrak{g} \subset \operatorname{Mat}(n \times n; \mathbb{K})$.
>
> **Hint:** Write the horizontal lift in the trivialisation as $\tilde c = (s_\alpha \circ c)\cdot h$; horizontality is a linear ODE for $h$; identify its solution operator.
>
> **Why needed:** It is the bridge from the intrinsic definition of holonomy to a computable ODE quantity, and it is the object that Lemma 2 collapses.
>
> > [!note]- Full proof
> > **Set-up.** By the [[Thm - Existence and Uniqueness of Horizontal Lifts|existence and uniqueness of horizontal lifts]] — for a connection $\omega$, a piecewise smooth curve $c$, and a point $p \in P_{c(0)}$ there is a unique piecewise smooth horizontal lift $\tilde c : [0,1] \to P$ with $\pi \circ \tilde c = c$, $\dot{\tilde c}(t) \in H_{\tilde c(t)} = \ker \omega_{\tilde c(t)}$, and $\tilde c(0) = p$ — the lift $\tilde c$ through $p = s_\alpha(m)$ exists and is unique. Since $c([0,1]) \subset U_\alpha$ and $s_\alpha$ trivialises $P|_{U_\alpha}$ by $(u, g) \mapsto s_\alpha(u)\cdot g$, we may write
> > $$\tilde c(t) = s_\alpha(c(t)) \cdot h(t), \qquad h : [0,1] \to G, \quad h(0) = e,$$
> > for a unique piecewise smooth curve $h$ in $G$, the fibre coordinate; the initial value is $h(0) = e$ because $\tilde c(0) = s_\alpha(m) = p$.
> >
> > **Reduce horizontality to a linear ODE.** By the horizontal-lift theorem, in the trivialisation $s_\alpha$ the condition $\dot{\tilde c}(t) \in H_{\tilde c(t)}$ is equivalent to the fibre ODE
> > $$\dot h(t) = -\,dR_{h(t)}\big(A_\alpha(\dot c(t))\big),$$
> > where $R_g$ is right translation and $A_\alpha = s_\alpha^{*}\omega$; this is the reduction proved on the horizontal-lift page (the local connection form drives the fibre coordinate). For a matrix group $G \subset GL(n; \mathbb{K})$, right translation $R_h(g) = g\,h$ is the restriction of a linear map, so its differential is $dR_h(X) = X\,h$, and the ODE becomes the **linear** equation
> > $$\dot h(t) = -A_\alpha(\dot c(t))\,h(t), \qquad h(0) = e. \tag{$\ast$}$$
> > The coefficient $t \mapsto A_\alpha(\dot c(t))$ is continuous on $[0,1]$ (piecewise smooth, with one-sided limits at the finitely many corners of $c$), so $(\ast)$ is a linear first-order matrix ODE with continuous coefficient.
> >
> > **Identify the solution operator.** By [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation|the path-ordered exponential theorem]] — for continuous $A : [0,L] \to \operatorname{Mat}(n\times n; \mathbb{K})$ the unique solution of $\dot v = -A(t)v$, $v(0) = v_0$, is $v(t) = \mathcal{P}\exp\big({-}\int_0^t A\big)\,v_0$ — applied with $A(t) = A_\alpha(\dot c(t))$, $L = 1$, and $v_0 = e = 1_n$, the unique solution of $(\ast)$ is
> > $$h(t) = \mathcal{P}\exp\!\Big({-}\int_0^t A_\alpha(\dot c)\Big)\cdot 1_n = \mathcal{P}\exp\!\Big({-}\int_0^t A_\alpha(\dot c)\Big).$$
> >
> > **Read off holonomy.** At $t = 1$ the lift closes over the fibre $P_m$: $\tilde c(1) = s_\alpha(m)\cdot h(1) = p \cdot h(1)$. By the [[Def - Holonomy Group of a Connection|definition of holonomy]], $\Gamma(c)(p) = \tilde c(1) = p \cdot \operatorname{hol}_p(c)$, and since the $G$-action on the fibre is free, comparing $p \cdot h(1) = p\cdot \operatorname{hol}_p(c)$ gives $\operatorname{hol}_p(c) = h(1)$. Therefore
> > $$\operatorname{hol}_p(c) = \mathcal{P}\exp\!\Big({-}\int_0^1 A_\alpha(\dot c(t))\,dt\Big),$$
> > as claimed. $\blacksquare$

> [!note]- Lemma 2: The path-ordered exponential of commuting coefficients is an ordinary exponential
> **Statement:** Let $A : [0,L] \to \operatorname{Mat}(n\times n; \mathbb{K})$ be continuous and suppose all values commute, $A(s)A(t) = A(t)A(s)$ for all $s, t \in [0,L]$ (for instance, $A$ takes values in an abelian subalgebra). Then
> $$\mathcal{P}\exp\!\Big({-}\int_0^t A(\tau)\,d\tau\Big) = \exp\!\Big({-}\int_0^t A(\tau)\,d\tau\Big), \qquad t \in [0,L].$$
>
> **Hint:** Differentiate the right-hand side termwise; commutativity lets you pull $A(t)$ out front, so it solves the defining ODE with the same initial value; conclude by uniqueness.
>
> **Why needed:** This is the step that spends the abelian hypothesis: it removes the ordering and turns holonomy into $\exp$ of an integral.
>
> > [!note]- Full proof
> > **Goal and strategy.** Write $B(t) := \int_0^t A(\tau)\,d\tau \in \operatorname{Mat}(n\times n; \mathbb{K})$ and $u(t) := \exp(-B(t))$. We show $u$ solves the initial value problem $\dot u = -A(t)\,u$, $u(0) = 1_n$; since the [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation|path-ordered exponential is the unique solution operator]] of that same problem, uniqueness forces $u(t) = \mathcal{P}\exp(-\int_0^t A)$, which is the claim.
> >
> > **Preliminary: the values commute with the integral.** For every $s, t$, $A(s)$ commutes with $A(t)$ by hypothesis, hence $A(t)$ commutes with the Riemann integral $B(t) = \int_0^t A(\tau)\,d\tau$ (the integral is a limit of Riemann sums $\sum_k A(\tau_k)\,\Delta\tau_k$, each term of which commutes with $A(t)$, and matrix multiplication by the fixed matrix $A(t)$ is continuous, so it passes to the limit). Consequently $A(t)$ commutes with every power $B(t)^{j}$ and with $\exp(-B(t))$.
> >
> > **Initial value.** $u(0) = \exp(-B(0)) = \exp(0) = 1_n$.
> >
> > **Differentiate the exponential series termwise.** The matrix exponential is the everywhere-absolutely-convergent power series $\exp(-B) = \sum_{j\ge 0} \frac{(-1)^j}{j!}B^{j}$. Each entry of $B(t)$ is $C^1$ in $t$ with $\dot B(t) = A(t)$ by the fundamental theorem of calculus (the integrand $A$ is continuous). On any compact $t$-interval the differentiated series $\sum_{j\ge 1}\frac{(-1)^j}{j!}\frac{d}{dt}B(t)^{j}$ is dominated in operator norm by $\sum_{j\ge 1}\frac{j}{j!}\,C^{\,j-1}\,\|A\|_{C^0}$ with $C := \sup_t \|B(t)\| < \infty$, which converges; hence the series may be differentiated term by term (uniform convergence of the differentiated series licenses termwise differentiation of a series of $C^1$ functions). Thus
> > $$\dot u(t) = \sum_{j \ge 1}\frac{(-1)^j}{j!}\,\frac{d}{dt}\big(B(t)^{j}\big).$$
> >
> > **Use commutativity to collapse the derivative of $B^{j}$.** For a matrix curve whose values commute with their own derivative — here $B(t)$ commutes with $\dot B(t) = A(t)$, established above — the product rule gives
> > $$\frac{d}{dt}\big(B^{j}\big) = \sum_{i=1}^{j} B^{\,i-1}\,\dot B\, B^{\,j-i} = \sum_{i=1}^{j} \dot B\, B^{\,j-1} = j\,A(t)\,B(t)^{\,j-1},$$
> > where the middle equality moves $\dot B = A(t)$ past the powers of $B$ (they commute), and there are $j$ equal terms. Substituting,
> > $$\dot u(t) = \sum_{j\ge 1}\frac{(-1)^j}{j!}\,j\,A(t)\,B(t)^{\,j-1} = -A(t)\sum_{j\ge 1}\frac{(-1)^{j-1}}{(j-1)!}\,B(t)^{\,j-1} = -A(t)\sum_{k\ge 0}\frac{(-1)^{k}}{k!}\,B(t)^{k},$$
> > the last step re-indexing $k = j-1$ and pulling out the sign. The remaining sum is $\exp(-B(t)) = u(t)$, so
> > $$\dot u(t) = -A(t)\,u(t).$$
> >
> > **Conclude by uniqueness.** The curve $u(t) = \exp(-B(t))$ satisfies $\dot u = -A(t)u$ and $u(0) = 1_n$, the same initial value problem whose unique solution operator is the path-ordered exponential. Therefore $\exp\big({-}\int_0^t A\big) = u(t) = \mathcal{P}\exp\big({-}\int_0^t A\big)$ for all $t$. $\blacksquare$
> >
> > *(This is the corollary recorded on [[Def - Path-Ordered Exponential|the path-ordered exponential page]]; it is proved here in full so that the present page is self-contained.)*

> [!note]- Lemma 3: A loop's period of the Maurer–Cartan form lies in the kernel of the exponential
> **Statement:** Let $G \subset GL(n; \mathbb{K})$ be an **abelian** matrix Lie group with Maurer–Cartan form $\theta = g^{-1}dg$, let $g : U_\alpha \to G$ be smooth, and let $c : [0,1] \to U_\alpha$ be a piecewise smooth loop. Then
> $$\exp\!\Big({-}\int_c g^{*}\theta\Big) = e.$$
> For $G = U(1) \subset \mathbb{C}^{\times}$ one has $\int_c g^{*}\theta = 2\pi i \cdot w(g \circ c)$, where $w(g\circ c) \in \mathbb{Z}$ is the winding number of the loop $g \circ c$ about $0$.
>
> **Hint:** Set $\gamma := g \circ c : [0,1] \to G$, a loop. Show that $t \mapsto \exp\big(\int_0^t \gamma^{*}\theta\big)$ and $t \mapsto \gamma(t)\gamma(0)^{-1}$ solve the same ODE with the same initial value; evaluate at $t = 1$.
>
> **Why needed:** It proves the formula $\exp(-\int_c A_\alpha)$ is independent of the trivialising section, so that part (a)'s value is genuinely the intrinsic holonomy.
>
> > [!note]- Full proof
> > **Set-up.** Let $\gamma := g \circ c : [0,1] \to G$; since $c$ is a loop and $g$ is a map, $\gamma$ is a piecewise smooth loop in $G$, $\gamma(0) = \gamma(1)$. Pulling back the Maurer–Cartan form along $c$ and then $g$ is the same as pulling back along $\gamma$: $\int_c g^{*}\theta = \int_0^1 (g\circ c)^{*}\theta = \int_0^1 \gamma^{*}\theta = \int_0^1 \gamma(t)^{-1}\dot\gamma(t)\,dt$, using $\theta = g^{-1}dg$ for the matrix group. Write $\Phi(t) := \int_0^t \gamma(\tau)^{-1}\dot\gamma(\tau)\,d\tau \in \mathfrak{g}$, so that $\int_c g^{*}\theta = \Phi(1)$.
> >
> > **Two curves solving one ODE.** Define
> > $$u(t) := \exp(\Phi(t)) \in G, \qquad w(t) := \gamma(t)\,\gamma(0)^{-1} \in G.$$
> > Set $\beta(t) := \gamma(t)^{-1}\dot\gamma(t) \in \mathfrak{g}$, so $\dot\Phi(t) = \beta(t)$.
> >
> > **$u$ solves $\dot y = y\,\beta$.** Because $G$ is abelian, $\Phi(t)$ and $\dot\Phi(t) = \beta(t)$ take values in the abelian Lie algebra $\mathfrak{g}$ and hence commute; by the same termwise-differentiation-with-commuting-derivative computation as in Lemma 2,
> > $$\dot u(t) = \exp(\Phi(t))\,\dot\Phi(t) = u(t)\,\beta(t) \qquad \text{(matrix exponential differentiated, } \Phi \text{ commutes with } \dot\Phi\text{)}.$$
> >
> > **$w$ solves $\dot y = y\,\beta$.** Differentiating $w(t) = \gamma(t)\gamma(0)^{-1}$,
> > $$\dot w(t) = \dot\gamma(t)\,\gamma(0)^{-1} = \gamma(t)\gamma(0)^{-1}\,\gamma(0)\gamma(t)^{-1}\dot\gamma(t) = w(t)\,\big(\gamma(0)\gamma(t)^{-1}\dot\gamma(t)\big).$$
> > Since $G$ is abelian, $\gamma(0)\gamma(t)^{-1}\dot\gamma(t) = \gamma(t)^{-1}\dot\gamma(t)\,\gamma(0)\cdot\gamma(0)^{-1} = \gamma(t)^{-1}\dot\gamma(t) = \beta(t)$ (the fixed factor $\gamma(0)$ and its inverse commute past everything and cancel), so $\dot w(t) = w(t)\,\beta(t)$.
> >
> > **Same initial value, hence equal.** $u(0) = \exp(\Phi(0)) = \exp(0) = e$ and $w(0) = \gamma(0)\gamma(0)^{-1} = e$. The initial value problem $\dot y = y\,\beta(t)$, $y(0) = e$, is a linear ODE in the ambient matrix space ($\dot y = y\beta$ is linear in $y$ with continuous coefficient $\beta$), so its solution is unique by [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation|the uniqueness clause of the linear-ODE theorem]] (applied to $y^{t}$, which solves $\dot{(y^{t})} = -(-\beta^{t})\,y^{t}$). Therefore $u(t) = w(t)$ for all $t$.
> >
> > **Evaluate at the endpoint.** At $t = 1$,
> > $$\exp\!\Big(\int_c g^{*}\theta\Big) = \exp(\Phi(1)) = u(1) = w(1) = \gamma(1)\,\gamma(0)^{-1} = e,$$
> > because $\gamma$ is a loop, $\gamma(1) = \gamma(0)$. Taking the inverse (or replacing $\Phi$ by $-\Phi$, equally a loop period) gives $\exp\big({-}\int_c g^{*}\theta\big) = e$.
> >
> > **The $U(1)$ periods are $2\pi i\,\mathbb{Z}$.** For $G = U(1) \subset \mathbb{C}^{\times}$ the Maurer–Cartan form is $\theta = z^{-1}dz$, so $\int_c g^{*}\theta = \int_{\gamma}\frac{dz}{z}$. By [[Thm - Existence and Properties of the Winding Number|the winding-number theorem]] — for a piecewise smooth loop $\gamma$ in $\mathbb{C}\setminus\{0\}$, $\frac{1}{2\pi i}\int_\gamma \frac{dz}{z} = w(\gamma) \in \mathbb{Z}$ is the [[Def - Winding Number|winding number]] of $\gamma$ about the origin — we get $\int_c g^{*}\theta = 2\pi i\,w(\gamma)$. Since $\exp : i\mathbb{R} \to U(1)$ is $\xi \mapsto e^{\xi}$ with kernel $2\pi i\,\mathbb{Z}$, indeed $\exp(-2\pi i\,w(\gamma)) = 1$, consistent with the general statement. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi : P \to M$ be a principal $G$-bundle with connection $\omega$, $G \subset GL(n;\mathbb{K})$ abelian, and let $c : [0,1] \to U_\alpha$ be a piecewise smooth loop at $m = c(0) = c(1)$ inside a trivialising set with section $s_\alpha$ and local connection form $A_\alpha = s_\alpha^{*}\omega$.
>
> **Step 0 — the global curvature is well-defined.** We first check that $F := dA_\alpha$ does not depend on the chart, so that the surface integral in part (b) makes sense for surfaces crossing chart boundaries. Let $s_\beta = s_\alpha \cdot g_{\alpha\beta}$ be another local section on an overlap, with transition map $g_{\alpha\beta} : U_\alpha \cap U_\beta \to G$. By [[Thm - Transformation of Local Connection and Curvature Forms|the transformation law for local connection forms]] — for $s_\beta = s_\alpha g_{\alpha\beta}$ one has $A_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha + g_{\alpha\beta}^{*}\theta$ — and since $G$ is abelian the adjoint action is trivial, $\operatorname{Ad}_{g^{-1}} = \operatorname{id}$, this reads
> $$A_\beta = A_\alpha + g_{\alpha\beta}^{*}\theta \qquad \text{(transformation law, } \operatorname{Ad} = \operatorname{id} \text{ for abelian } G\text{)}.$$
> Taking exterior derivatives,
> $$dA_\beta = dA_\alpha + d\big(g_{\alpha\beta}^{*}\theta\big) = dA_\alpha \qquad \text{(since } d(g_{\alpha\beta}^{*}\theta) = 0\text{)},$$
> where the vanishing is [[Thm - The Maurer-Cartan Equation|the Maurer–Cartan equation]]: $d\theta + \tfrac12[\theta\wedge\theta] = 0$ pulls back to $d(g_{\alpha\beta}^{*}\theta) + \tfrac12[g_{\alpha\beta}^{*}\theta \wedge g_{\alpha\beta}^{*}\theta] = 0$, and the bracket term vanishes because $\mathfrak{g}$ is abelian, leaving $d(g_{\alpha\beta}^{*}\theta) = 0$. Hence the local $2$-forms $F_\alpha = dA_\alpha$ agree on all overlaps and define a single global $F \in \Omega^2(M; \mathfrak{g})$. (This is the abelian clause of the transformation theorem, $F_\beta = F_\alpha$.) Also, because $[\,\cdot\,,\,\cdot\,]$ vanishes on $\mathfrak{g}$, the local curvature $F_\alpha = dA_\alpha + \tfrac12[A_\alpha\wedge A_\alpha] = dA_\alpha$, so $F = dA_\alpha$ throughout.
>
> **Step 1 — the general loop formula (part (a)).** Put $p := s_\alpha(m)$. By **Lemma 1**, in this trivialisation
> $$\operatorname{hol}_p(c) = \mathcal{P}\exp\!\Big({-}\int_0^1 A_\alpha(\dot c(t))\,dt\Big).$$
> The integrand $t \mapsto A_\alpha(\dot c(t))$ takes values in the abelian Lie algebra $\mathfrak{g}$, so any two of its values commute. By **Lemma 2** (commuting coefficients), the path-ordered exponential collapses to an ordinary exponential:
> $$\operatorname{hol}_p(c) = \exp\!\Big({-}\int_0^1 A_\alpha(\dot c(t))\,dt\Big) \qquad \text{(Lemma 2, } \mathfrak{g} \text{ abelian)}.$$
> Finally $\int_0^1 A_\alpha(\dot c(t))\,dt = \int_c A_\alpha$ by the definition of the line integral of a $1$-form along $c$ (pull $A_\alpha$ back by $c$ and integrate over $[0,1]$). Therefore
> $$\operatorname{hol}_p(c) = \exp\!\Big({-}\int_c A_\alpha\Big).$$
>
> **Step 2 — independence of the base point.** For any other point $p' \in P_m$ we have $p' = p\cdot a$ for a unique $a \in G$. By the conjugation law for holonomy proved on [[Def - Holonomy Group of a Connection|the holonomy page]] — $\operatorname{hol}_{p\cdot a}(c) = a^{-1}\operatorname{hol}_p(c)\,a$ — and abelianness of $G$,
> $$\operatorname{hol}_{p'}(c) = a^{-1}\operatorname{hol}_p(c)\,a = \operatorname{hol}_p(c) \qquad \text{(} G \text{ abelian, so conjugation is trivial)}.$$
> Thus the holonomy is the same for every base point in the fibre, and we may write $\operatorname{hol}(c) := \operatorname{hol}_p(c)$.
>
> **Step 3 — independence of the trivialisation.** Let $s'_\alpha = s_\alpha \cdot g$ be another section on $U_\alpha$, $g : U_\alpha \to G$, with local form $A'_\alpha = A_\alpha + g^{*}\theta$ (transformation law, $\operatorname{Ad} = \operatorname{id}$, as in Step 0). Then
> $$\exp\!\Big({-}\int_c A'_\alpha\Big) = \exp\!\Big({-}\int_c A_\alpha - \int_c g^{*}\theta\Big) = \exp\!\Big({-}\int_c A_\alpha\Big)\cdot\exp\!\Big({-}\int_c g^{*}\theta\Big),$$
> where the product splits because $\exp$ is a homomorphism on the abelian group $G$ and the two integrals lie in the abelian $\mathfrak{g}$. By **Lemma 3**, $\exp\big({-}\int_c g^{*}\theta\big) = e$, so
> $$\exp\!\Big({-}\int_c A'_\alpha\Big) = \exp\!\Big({-}\int_c A_\alpha\Big).$$
> Combined with Steps 1–2, the value $\operatorname{hol}(c) = \exp(-\int_c A_\alpha)$ is independent of the section, completing **part (a)**.
>
> **Step 4 — the curvature-flux formula (part (b)).** Assume now that $c$ bounds a compact oriented surface $S \subset U_\alpha$ with $\partial S = c$. Apply [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — for a compact oriented $k$-manifold $S$ with boundary and a smooth $(k-1)$-form $\eta$, $\int_S d\eta = \int_{\partial S}\eta$ — to each of the finitely many real component $1$-forms of the $\mathfrak{g}$-valued form $A_\alpha$ (fix a basis of $\mathfrak{g}$ and apply Stokes componentwise; the boundary orientation on $\partial S = c$ is the one induced from $S$). This gives
> $$\int_c A_\alpha = \int_{\partial S} A_\alpha = \int_S dA_\alpha = \int_S F \qquad \text{(Stokes' theorem; } dA_\alpha = F \text{ by Step 0)}.$$
> Exponentiating the negative,
> $$\operatorname{hol}(c) = \exp\!\Big({-}\int_c A_\alpha\Big) = \exp\!\Big({-}\int_S F\Big),$$
> which is **part (b)**.
>
> **Step 5 — curvature detects holonomy (part (c)).** Suppose $F \ne 0$, so $F_{m_0} \ne 0$ at some point $m_0 \in M$. Choose a chart $U_\alpha \ni m_0$ with coordinates $(x^1, \dots, x^d)$ centred at $m_0$ and a basis $(\xi_1, \dots, \xi_r)$ of $\mathfrak{g}$; write $F = \sum_{a} F^{a}\,\xi_a$ with real $2$-forms $F^{a}$. Since $F_{m_0} \ne 0$, some component $F^{a}$ is nonzero at $m_0$, and after a linear change of the coordinates we may assume $F^{a}_{m_0}(\partial_1, \partial_2) = \lambda \ne 0$. For $\varepsilon > 0$ let $S_\varepsilon := \{(x^1, x^2, 0, \dots, 0) : 0 \le x^1, x^2 \le \varepsilon\}$ be the coordinate square in the $x^1x^2$-plane, oriented by $dx^1\wedge dx^2$, with boundary loop $c_\varepsilon := \partial S_\varepsilon$. By continuity of the smooth density $F^{a}(\partial_1, \partial_2)$,
> $$\int_{S_\varepsilon} F = \Big(\sum_a \int_{S_\varepsilon} F^{a}(\partial_1,\partial_2)\,dx^1dx^2\Big)\,\xi_a = \big(\lambda\,\varepsilon^2 + o(\varepsilon^2)\big)\,\xi_a + o(\varepsilon^2) \qquad (\varepsilon \to 0),$$
> so for all sufficiently small $\varepsilon$ the element $v_\varepsilon := -\int_{S_\varepsilon} F \in \mathfrak{g}$ is nonzero and satisfies $v_\varepsilon \to 0$. The exponential $\exp : \mathfrak{g} \to G$ has invertible differential $d_0\exp = \operatorname{id}$ at $0$, so by the inverse function theorem it is a diffeomorphism, in particular injective, on some neighbourhood $V \ni 0$; choose $\varepsilon$ small enough that $v_\varepsilon \in V \setminus \{0\}$. Then $\exp(v_\varepsilon) \ne \exp(0) = e$. By part (b),
> $$\operatorname{hol}(c_\varepsilon) = \exp\!\Big({-}\int_{S_\varepsilon} F\Big) = \exp(v_\varepsilon) \ne e.$$
> Hence the loop $c_\varepsilon$ has nontrivial holonomy, proving **part (c)**.
>
> **Conclusion.** For an abelian structure group the holonomy of any loop in a chart is the exponential of the loop integral of the local connection form (part (a)), equivalently the exponential of the negative flux of the global curvature through any spanning surface (part (b)); and a connection with nonzero curvature necessarily has a loop of nontrivial holonomy (part (c)). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Electromagnetism and the Aharonov–Bohm phase (physics).** Model a static magnetic field on $\mathbb{R}^3 \setminus (z\text{-axis})$ by a $U(1)$-connection with potential $A = i\,\mathbf{A}\cdot d\mathbf{x}$, where $\mathbf{A}$ is the vector potential of a thin solenoid along the $z$-axis carrying flux $\Phi$. Outside the solenoid the field $F = i\,\mathbf{B}\cdot d\mathbf{S}$ vanishes, yet the holonomy of a horizontal loop $c$ encircling the axis is $\exp(-i\Phi) \ne 1$ whenever $\Phi \notin 2\pi\mathbb{Z}$. The theorem applies because $G = U(1)$ is abelian; the exercise is non-obvious because $c$ lies where $F = 0$, so part (b) must be applied with a surface $S$ that *does* cross the solenoid, and the phase is the flux through that surface — the loop feels a field it never touches. This is the electromagnetic prototype for Dirac's quantisation argument in chapter VII.

**Geometric phases in quantum mechanics (mathematical physics).** Consider a family of Hamiltonians $H(\mathbf{R})$ depending on external parameters $\mathbf{R}$ in a parameter manifold $M$, with a nondegenerate ground state defining a Hermitian line bundle $L \to M$ (the Berry line bundle) and the Berry connection $A$. The Berry phase acquired on adiabatically transporting the state around a loop $c$ is exactly $\operatorname{hol}(c) = \exp(-\oint_c A) = \exp(-\int_S F)$, the flux of the Berry curvature. The theorem applies because the structure group is $U(1)$; it is non-obvious as an application because the physics literature derives the phase by a direct adiabatic computation, whereas the theorem shows it is *forced* to be a curvature flux by abelianness alone, independent of any adiabatic approximation.

**Complex analysis and periods (pure mathematics).** On the punctured plane $\mathbb{C}\setminus\{0\}$ take the flat $U(1)$-connection $A = i\,a\,d\theta$ (a real multiple of the angular form, $a \in \mathbb{R}$). Its curvature is $F = i\,a\,d(d\theta) = 0$ away from the origin, so no surface computation is available, but part (a) still gives $\operatorname{hol}(c) = \exp(-i\,a\oint_c d\theta) = \exp(-2\pi i\,a\,w(c))$ for a loop $c$ of winding number $w(c)$. The exercise ties the abelian holonomy formula to the residue/period viewpoint: the holonomy is a character of $\pi_1(\mathbb{C}\setminus\{0\}) = \mathbb{Z}$, and Lemma 3's winding-number identity is precisely the statement that this character is well-defined modulo the kernel of $\exp$. It is non-obvious because it shows that the "monodromy" of a multivalued function $z^{a}$ is a special case of gauge holonomy.

---

# Bridges

- **[[Thm - Curvature is the Infinitesimal Holonomy|Curvature is the infinitesimal holonomy]].** The present theorem is the *exact* (abelian) version of what that theorem does *infinitesimally* for a general matrix group: expanding $\operatorname{hol}(c_L) = \exp(-\int_{S_L} F)$ to first order in the area $L^2$ gives $\operatorname{hol}(c_L) = 1 - \int_{S_L}F + O(L^3)$, and the abelian case is precisely the one in which the higher, non-commutative $A\wedge A$ corrections vanish and the first-order relation is promoted to an equality valid for loops of any size. Reading the two together shows that curvature is the density of holonomy per unit area, with the abelian case being the one where "density" integrates cleanly.

- **[[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|Homotopy invariance of flat holonomy]].** When $F = 0$, part (a) survives but part (b) trivialises: $\int_c A_\alpha$ becomes a period of a closed form, unchanged under homotopies of $c$ that stay in the chart. Globalising this (across charts, via a subdivision argument) is exactly how the flat-connection chapter shows holonomy descends to a function of the homotopy class $[c] \in \pi_1(M)$, producing the monodromy homomorphism $\pi_1(M) \to U(1)$ and the identification $\mathcal{M}^\flat_{U(1)}(M) \cong \operatorname{Hom}(\pi_1(M), U(1))$.

- **Dirac quantisation of magnetic charge (chapter VII).** Applying part (b) to the two hemispheres of $S^2$ bounded by the equator, in the two trivialisations of a $U(1)$-bundle over $S^2$, the two holonomy computations must agree; their consistency is the statement that $\frac{1}{2\pi i}\int_{S^2}F \in \mathbb{Z}$, the integrality of the first Chern number. Physically this is the quantisation of magnetic charge in units set by the electric charge, and it is built directly on the base-point/trivialisation independence proved here (Steps 2–3) together with the winding-number kernel computation of Lemma 3.

- **[[Ex - Holonomy around a Spherical Cap is the Solid Angle|Solid-angle holonomy on the sphere]] (Riemannian Geometry IV).** The parallel transport of a tangent vector around a spherical cap rotates it by the enclosed solid angle. Reinterpreting the tangent bundle of $S^2$ as an associated $U(1) \cong SO(2)$-bundle, this rotation *is* the abelian holonomy $\exp(-\int_S F)$ of the Levi-Civita connection, with $F$ the (Gaussian) curvature $2$-form and $\int_S F$ the solid angle by the Gauss–Bonnet integrand. The present theorem is the general mechanism of which that spherical-cap exercise is a concrete instance.

---

# Unlocked by This

> [!tip] Wilson loops *(from Gauge Theory / Physics)*
> For a general (non-abelian) matrix group the gauge-invariant observable built from holonomy is the **Wilson loop** $W(c) = \operatorname{tr}\big(\rho(\operatorname{hol}(c))\big)$ in a representation $\rho$. The abelian theorem is the case where the trace is a single phase $e^{-i\int_S F}$ and the loop observable is literally the exponentiated flux; this is the base case against which the non-abelian, path-ordered Wilson loop is defined and understood.

> [!tip] The first Chern class as curvature flux *(from Chern–Weil theory, Chapter VI)*
> The identity $\operatorname{hol}(\partial S) = \exp(-\int_S F)$ is the loop-level shadow of the Chern–Weil statement that $\tfrac{i}{2\pi}F$ represents an integral cohomology class $c_1(L) \in H^2(M;\mathbb{Z})$. Curvature integrals over closed surfaces are integers because holonomies around their (contractible-on-each-piece) decomposing loops must be consistent — the abelian holonomy theorem is where that consistency first becomes visible.
