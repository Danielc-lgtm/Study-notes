---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Chern-Simons Functional"
  - "Thm - Transgression Formula and the Chern-Simons Form"
  - "Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree"
  - "Thm - Gauge Variation of the Chern-Simons Functional"
  - "Thm - Generic Sections are Transverse to the Zero Section"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Manifold with Boundary and Induced Orientation"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a closed oriented three-manifold and $P\to M$ a principal $SU(2)$-bundle; every such bundle is trivial, so after choosing a trivialisation a connection on $P$ is recorded by its gauge potential $A\in\Omega^1(M;\mathfrak{su}(2))$, an $\mathfrak{su}(2)$-valued one-form on $M$, where $\mathfrak{su}(2)=\{\xi\in\mathfrak{gl}_2(\mathbb C):\xi^*=-\xi,\ \operatorname{tr}\xi=0\}$ is the Lie algebra of $SU(2)$. We write $\operatorname{tr}$ for the trace of $2\times 2$ complex matrices in the defining representation, and for $\mathfrak{su}(2)$-valued forms $\alpha,\beta$ the symbol $\operatorname{tr}(\alpha\wedge\beta)$ means the ordinary scalar-valued form obtained by wedging the form parts and tracing the matrix product. The **Chern–Simons three-form** of $A$ is
$$\operatorname{cs}(A):=\operatorname{tr}\!\Big(A\wedge dA+\tfrac23\,A\wedge A\wedge A\Big)\in\Omega^3(M),$$
and the **Chern–Simons functional** is $\vartheta(A):=\tfrac1{8\pi^2}\int_M\operatorname{cs}(A)\in\mathbb R/\mathbb Z$; both are defined and motivated on [[Def - Chern-Simons Functional]]. The curvature of a gauge potential is $F_A=dA+A\wedge A$ (matrix-group convention, in which $\tfrac12[A\wedge A]=A\wedge A$).

On the four-dimensional side, $X$ denotes a compact oriented four-manifold with boundary $\partial X=M$; $P_X\to X$ is a principal $SU(2)$-bundle and $A_X$ a connection on it, with curvature $F_{A_X}\in\Omega^2(X;\operatorname{ad}P_X)$. The phrase "$A_X$ restricts to $A$" means that under the given isomorphism $P_X|_M\cong P$ the pulled-back connection along the inclusion $\iota\colon M\hookrightarrow X$ is $A$. For a chart-disc $D\cong D^4$ in the interior of $X$ we write $S^3\cong\partial D$ for its bounding three-sphere, $D^\circ$ for its interior, and $E:=P_X\times_{SU(2)}\mathbb C^2$ for the rank-two complex (rank-four real) vector bundle associated to $P_X$ through the defining representation of $SU(2)$ on $\mathbb C^2$; it carries the Hermitian structure induced by the standard one on $\mathbb C^2$, which is $SU(2)$-invariant.

The orientation conventions are those of the series. The Hodge star plays no role here. Orientations of boundaries and of products are the induced (outward-normal-first) orientations of [[Def - Manifold with Boundary and Induced Orientation]]; when two bounded pieces are glued along $M$ the second is given the reversed orientation, so that its boundary is $-M$ and the glued manifold is oriented. The normalisation $\operatorname{tr}(\xi^2)=-2\det\xi$ on $\mathfrak{su}(2)$ fixes the constant $\tfrac1{8\pi^2}$; it is the same constant appearing in the second-Chern-number theorem.

> [!warning] Convention: the theorem is conditional on a given extension
> The statement below **assumes** that an extension $(X,P_X,A_X)$ of $(M,P,A)$ is given; it does not assert that one exists. That every closed oriented three-manifold bounds a compact oriented four-manifold (Thom–Rokhlin), and that the bundle and connection then extend, are the facts Haydys records as I3.2.1–I3.2.2. **These bounding and extension facts are neither proved nor used in this series**; wherever we need a four-dimensional formula we are handed the four-manifold. The content of the theorem is that *whenever* such an extension is supplied, its second-Chern-form integral computes $\vartheta(A)$.

This page is sign-insensitive: parts (a) and (b) assert only membership in $\mathbb Z$ or equality modulo $\mathbb Z$, and part (c) is a pure Stokes computation with no gauge transformation, so none of the orientation-dependent signs recorded on [[Def - The Hopf Bundle#Sign ledger]] enter. We flag one source correction. **Haydys's Exercise 96(a), second display, omits the normalising factor $\tfrac1{8\pi^2}$** in the cylinder formula (item 6 of the source typo list); the corrected identity, with the factor restored, is part (c) below.

---

# Statement

> **Theorem (the four-dimensional formula for the Chern–Simons functional).** Let $M$ be a closed oriented three-manifold, $P\to M$ a principal $SU(2)$-bundle, and $A\in\Omega^1(M;\mathfrak{su}(2))$ a gauge potential, with $\vartheta(A)\in\mathbb R/\mathbb Z$ its Chern–Simons functional.
>
> **(a) The bounding formula.** Let $X$ be a compact oriented four-manifold with $\partial X=M$, let $P_X\to X$ be a principal $SU(2)$-bundle with $P_X|_M\cong P$, and let $A_X$ be a connection on $P_X$ restricting to $A$. Then
> $$\vartheta(A)\equiv\frac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})\pmod{\mathbb Z}.$$
>
> **(b) Independence of the extension.** If $(X,P_X,A_X)$ and $(X',P'_X,A'_X)$ are two such extensions of $(M,P,A)$, then
> $$\frac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})-\frac1{8\pi^2}\int_{X'}\operatorname{tr}(F_{A'_X}\wedge F_{A'_X})\in\mathbb Z.$$
>
> **(c) The cylinder formula (equality in $\mathbb R$).** Let $X=M\times[t_0,t_1]$ with the product orientation, let $A\in\Omega^1(X;\mathfrak{su}(2))$ be a gauge potential on the (trivial) bundle $P_X=P\times[t_0,t_1]$, and for $t\in[t_0,t_1]$ let $A_t:=\iota_t^*A\in\Omega^1(M;\mathfrak{su}(2))$ be its restriction to the slice $\iota_t\colon M\to M\times\{t\}$. Then, in $\mathbb R$,
> $$\vartheta(A_{t_1})-\vartheta(A_{t_0})=\frac1{8\pi^2}\int_{M\times[t_0,t_1]}\operatorname{tr}(F_A\wedge F_A).$$

The three parts are progressively sharper. Part (a) identifies the three-dimensional functional with a four-dimensional density but only modulo $\mathbb Z$, because that is the best possible: different extensions genuinely give different real numbers. Part (b) says the ambiguity is exactly an integer, which is what makes the four-dimensional definition of $\vartheta$ well posed in $\mathbb R/\mathbb Z$ and is the well-definedness clause of [[Def - Chern-Simons Functional]]. Part (c) is the special case in which the four-manifold is a cylinder over $M$: there the two boundary components are copies of $M$ in the *same* trivialisation, the integer ambiguity disappears, and the identity holds on the nose in $\mathbb R$ — this is the form used to read $\vartheta$ as an action along a path of connections.

---

# Motivation

The Chern–Simons functional is defined on [[Def - Chern-Simons Functional]] by the three-dimensional formula $\vartheta(A)=\tfrac1{8\pi^2}\int_M\operatorname{cs}(A)$, a quantity one can compute from the gauge potential $A$ alone, with no reference to any four-manifold. Haydys, following Chern and Simons, introduces the same functional the other way round: he writes down the four-dimensional integral $\tfrac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})$ over a bounding four-manifold and calls *that* the definition. The present theorem is the bridge between the two viewpoints. It answers the question a reader of both definitions must ask: are they the same functional, and if so, in what precise sense?

The importance of the four-dimensional description is that it makes the relationship to [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree|Chern–Weil theory]] transparent. The integrand $\operatorname{tr}(F_{A_X}\wedge F_{A_X})$ is, up to the constant $8\pi^2$, the second Chern form of $P_X$; its integral over a *closed* four-manifold is $8\pi^2$ times an integer. The Chern–Simons functional is what is left over when the four-manifold has a boundary: it is the "fractional part" of a second Chern number, a secondary invariant living on the three-dimensional boundary where the primary integer invariant of the four-dimensional bulk is not yet forced to be a whole number. This is exactly why the natural codomain is the circle $\mathbb R/\mathbb Z$: the integer part is the content of the bulk, and only the fractional part is intrinsic to the boundary.

The theorem also carries the well-definedness that the four-dimensional definition needs to make sense at all. A definition that says "choose a bounding four-manifold and integrate" is only legitimate if the answer does not depend on the choice. Part (b) supplies precisely that guarantee, and it is the reason $\vartheta$ takes values in $\mathbb R/\mathbb Z$ rather than $\mathbb R$: two choices differ by an integer, so their classes modulo $\mathbb Z$ agree. Finally, the cylinder formula of part (c) is the version that makes $\vartheta$ behave like an action functional: for a path of connections $t\mapsto A_t$, the change in $\vartheta$ along the path equals the integral of the second Chern form over the trace of the path, which is the geometric content behind the gradient-flow picture in which the flat connections appear as critical points and the instantons as flow lines.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of part (a) is that a bounding datum $(X,P_X,A_X)$ is handed to us. The skill is to recognise when a problem secretly supplies one.

The first disguised source is **a mapping cylinder or a family of connections parametrised by an interval**. Whenever one is given a smooth one-parameter family $A_t$ of connections on $P\to M$ for $t\in[t_0,t_1]$, one has, without further work, a connection on the cylinder $M\times[t_0,t_1]$ whose slices are the $A_t$; the family *is* the four-dimensional datum. The bridge $B\Rightarrow A$ is that a path of three-dimensional connections is a single four-dimensional connection on a bounding manifold with two boundary copies of $M$. The non-obvious part is that the four-manifold need not be exotic — a cylinder does the job — so that part (c) applies and the difference of the endpoint values is computed by a bulk integral. *Example problem:* given a homotopy from the trivial connection to a flat connection $A_1$, compute $\vartheta(A_1)$ by integrating the second Chern form over the cylinder of the homotopy.

The second disguised source is **an instanton on an asymptotically cylindrical or capped four-manifold**. A finite-energy anti-self-dual connection on a four-manifold with a cylindrical end modelled on $M\times[0,\infty)$ restricts, near the end, to a path of connections on $M$ converging to a flat limit; truncating at a large but finite $t$ produces exactly a bounding datum $(X,P_X,A_X)$ with $\partial X=M$. The bridge is that finite Yang–Mills energy forces the connection to limit onto a flat connection on the boundary slice, so the truncation is a legitimate extension. The non-obviousness is that the boundary connection is not chosen by hand but produced by the analysis of the instanton at infinity. *Example problem:* express the difference of Chern–Simons values of the two flat limits of an instanton on a cylinder as its total instanton energy.

The third disguised source is **any statement that a three-manifold bounds, together with an obstruction argument that the bundle extends**. For an $SU(2)$-bundle over a three-manifold the bundle is automatically trivial and hence extends over any bounding four-manifold; the connection then extends by convex interpolation with a product connection near the boundary. The bridge $B\Rightarrow A$ is: triviality of $P$ over $M$ removes the bundle-extension obstruction, so the mere existence of a bounding $X$ produces a full datum $(X,P_X,A_X)$. The non-obvious step is that the *bundle* obstruction, which in general lives in a cohomology group of $X$ relative to $M$, vanishes here because $SU(2)$ is two-connected enough for three-dimensional bases. *Example problem:* show that for $M=S^3$ one may take $X=D^4$ with the trivial bundle, so that $\vartheta$ of a connection on $S^3$ equals a single bulk integral over the four-ball modulo $\mathbb Z$.

**Targets (Output Amplification)**

The bare conclusions gain force in combination.

Combine part (a) with **the second-Chern-number integrality theorem on a closed manifold**. Capping $M$ off by two different bounding manifolds and gluing gives a closed four-manifold whose bulk integral is a genuine second Chern number; the extra ingredient is [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree|the integrality theorem]], and the payoff is part (b): the two boundary computations of $\vartheta$ agree modulo $\mathbb Z$. This is the mechanism by which a boundary invariant inherits well-definedness from a bulk integrality statement.

Combine part (c) with **the first-variation formula for $\vartheta$**. Differentiating the cylinder identity in $t_1$ and using that the differential of $\vartheta$ at $A$ is $a\mapsto\tfrac1{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a)$ (proved on [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|the critical-point theorem]]) recovers the pointwise identity $\tfrac{d}{dt}\vartheta(A_t)=\tfrac1{4\pi^2}\int_M\operatorname{tr}(F_{A_t}\wedge\dot A_t)$; the extra ingredient is the first-variation computation, and the payoff is that the gradient of $\vartheta$ is the curvature. The critical points are therefore the flat connections, and the downward flow lines are the anti-self-dual connections on the cylinder.

Combine part (a) with **a choice of two connections on the same $(X,P_X)$**. Since the bulk integral is, by Lemma 4 below, independent of the interior extension connection once the boundary value is fixed, part (a) shows $\vartheta(A)$ depends only on $A$ and not on how it is extended; the extra ingredient is the transgression formula on $X$, and the payoff is a proof that the four-dimensional definition is insensitive to the extension of the connection, which is the half of well-definedness not covered by the choice of four-manifold.

---

# Why Is It True

Strip away the four-manifold topology and the mechanism is a single application of Stokes' theorem. The four-form $\operatorname{tr}(F\wedge F)$ is not exact on a general four-manifold, but *in any trivialisation of the bundle* it is the exterior derivative of the Chern–Simons three-form: $\operatorname{tr}(F_A\wedge F_A)=d\operatorname{cs}(A)$, the transgression identity. So wherever $P_X$ is trivial, integrating the bulk four-form is the same as integrating the boundary three-form, by Stokes. Over the boundary $M$ this boundary three-form is exactly $\operatorname{cs}(A)$, whose integral is $8\pi^2\vartheta(A)$.

> **The bulk integral of the second Chern form equals the boundary integral of the Chern–Simons form, because the second Chern form is the exterior derivative of the Chern–Simons form in any trivialisation, and Stokes' theorem turns a bulk exact form into a boundary integral.**

The only obstruction to running this argument globally is that $P_X$ need not be trivial over all of $X$, so there is no single trivialisation in which $\operatorname{tr}(F\wedge F)=d\operatorname{cs}(A_X)$ holds everywhere. This is where the topology enters, and it enters in a controlled way. An $SU(2)$-bundle over a four-manifold is trivial once a single point is removed, because the associated $\mathbb C^2$-bundle then has a nowhere-vanishing section and $SU(2)$ acts simply transitively on the unit sphere of $\mathbb C^2$. Removing small balls around the finitely many zeros of a generic section leaves a region on which $P_X$ *is* trivialised, so the Stokes argument runs there; each removed ball is contractible, hence carries its own trivialisation, and the two trivialisations on the little three-sphere around a zero differ by a gauge transformation. The gauge-variation theorem says that a change of trivialisation shifts $\tfrac1{8\pi^2}\int\operatorname{cs}$ by an integer. So each removed ball contributes an integer, and modulo $\mathbb Z$ the global answer is the same as the naive boundary answer. That is part (a).

Part (b) is the same idea run on a closed manifold. Two bounding data glue along $M$ into a closed four-manifold, on which the bulk integral is a genuine second Chern number, hence an integer. The difference of the two original bulk integrals is that integer. Part (c) is the cleanest case: the cylinder is a product, its bundle is globally trivial, no balls need be removed, and the two boundary contributions are computed in one and the same trivialisation, so the answer is exact in $\mathbb R$ with no modular ambiguity at all.

---

# What Makes This Hard

The subtle point is that $P_X$ can be non-trivial, so one cannot simply apply Stokes to $\operatorname{tr}(F\wedge F)=d\operatorname{cs}(A_X)$ over all of $X$: the three-form $\operatorname{cs}(A_X)$ is trivialisation-dependent and does not exist globally. The correct move is to trivialise $P_X$ away from the finite zero set of a generic section, run Stokes on the punctured manifold, and account for each puncture by a change-of-trivialisation integer; the common error is to forget that the little spheres bounding the removed balls carry the *opposite* induced orientation to their role as boundaries of the balls, which flips a sign and, if unnoticed, appears to change the answer by twice each puncture's contribution rather than leaving it an integer. A second trap in part (b) is the smooth gluing: the two connections agree on $M$ but need not agree on a collar, so one must first homotope them to a product form near the boundary — and one must know that this homotopy does not change the bulk integral, which is the separate content of Lemma 4.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** In every part, use the transgression identity $\operatorname{tr}(F\wedge F)=d\operatorname{cs}(A)$ (valid in any trivialisation) to convert a bulk integral of the second Chern form into a boundary integral of the Chern–Simons form, then apply Stokes. The bundle is trivialised globally on a cylinder (part c) or on the complement of finitely many points (parts a, b); the punctures and the gluing account for the integer ambiguity.

**Subgoal decomposition:**

1. **A nowhere-zero section trivialises $P_X$.** Show that a unit-length section of $E=P_X\times_{SU(2)}\mathbb C^2$ is the same as a section of $P_X$, hence trivialises it.
   - *Hint:* $SU(2)$ acts simply transitively on the unit sphere $S^3\subset\mathbb C^2$; identify $P_X$ with the unit-sphere bundle of $E$ through the first basis vector.
   - *Why needed:* it is the only way non-triviality of $P_X$ is tamed; it turns a section into a trivialisation.

2. **A generic section is nonvanishing near $M$ with finitely many interior zeros.** Produce a section of $E$ transverse to the zero section, nonzero on a neighbourhood of $\partial X$.
   - *Hint:* apply the generic-sections theorem; the rank ($4$) exceeds $\dim M=3$ on the boundary and equals $\dim X=4$ in the interior; use the relative clause to keep the collar section fixed.
   - *Why needed:* it yields a global trivialisation of $P_X$ off finitely many interior points, on which Stokes runs.

3. **Each puncture contributes an integer.** Show that removing a ball $D$ around a zero and comparing the trivialisation from step 2 with a trivialisation of $P_X|_D$ changes $\tfrac1{8\pi^2}\int_{S^3}\operatorname{cs}$ by an integer.
   - *Hint:* the two trivialisations differ by $g\colon S^3\to SU(2)$; apply the gauge-variation theorem; then apply Stokes on the ball.
   - *Why needed:* it is what makes the punctured Stokes computation agree with the boundary integral modulo $\mathbb Z$.

4. **The bulk integral does not depend on the interior extension of the connection.** For two connections on $(X,P_X)$ with the same boundary value $A$, show the bulk integrals are equal in $\mathbb R$.
   - *Hint:* their difference is $\int_X d(\text{transgression})=\int_M(\text{transgression})$, and the transgression form restricts to zero on $M$ because the two connections agree there.
   - *Why needed:* it licenses homotoping the connections to a product form near the collar in part (b) without changing the answer.

5. **Assemble.** Part (a): Stokes on the punctured $X$ plus steps 1–3. Part (b): glue two data into a closed manifold (using step 4 to make them product near the collar) and apply integrality. Part (c): Stokes on the product cylinder with two boundary slices.

---

# Lemma Decomposition

> [!note]- Lemma 1: A unit section of the associated $\mathbb C^2$-bundle trivialises the $SU(2)$-bundle
> **Statement:** Let $P_X\to Y$ be a principal $SU(2)$-bundle over a manifold $Y$, and $E=P_X\times_{SU(2)}\mathbb C^2$ its associated bundle for the defining representation, with the induced Hermitian structure. If $u\in\Gamma(E)$ is a section with $|u(y)|=1$ for all $y$, then $P_X$ admits a global section, hence is trivial.
>
> **Hint:** $SU(2)$ acts simply transitively on the unit sphere $S^3=\{v\in\mathbb C^2:|v|=1\}$; identify the unit-sphere bundle $S(E)$ with $P_X$.
>
> **Why needed:** it converts the analytic object produced by genericity — a nowhere-zero section — into the geometric object needed for Stokes, a trivialisation.
>
> > [!note]- Full proof
> > **Step 0 — the action on the unit sphere is simply transitive.** Write $e_1=(1,0)^{\mathsf T}\in\mathbb C^2$. An element $g\in SU(2)$ has the form $g=\begin{pmatrix}a&-\bar b\\ b&\bar a\end{pmatrix}$ with $|a|^2+|b|^2=1$, and $g\,e_1=(a,b)^{\mathsf T}$. Thus $g\,e_1=e_1$ forces $a=1,b=0$, that is $g=I$: the stabiliser of $e_1$ is trivial (the action is free at $e_1$, and by equivariance everywhere on the orbit). The orbit map $SU(2)\to S^3$, $g\mapsto g\,e_1$, is a smooth injection between compact connected three-manifolds; its differential at the identity is injective (freeness), hence an isomorphism by equal dimensions, so the map is a local diffeomorphism, and being an injective local diffeomorphism from a compact manifold it is a diffeomorphism onto the open-and-closed image $S^3$. Therefore $SU(2)$ acts simply transitively on $S^3$.
> >
> > **Step 1 — the unit-sphere bundle is a copy of $P_X$.** The unit-sphere bundle $S(E)=P_X\times_{SU(2)}S^3$ has fibre $S^3$ on which $SU(2)$ acts simply transitively; by Step 0 the map
> > $$\Phi\colon P_X\longrightarrow S(E),\qquad \Phi(p)=[p,e_1],$$
> > is well defined and $SU(2)$-equivariant, where $[p,v]$ denotes the class of $(p,v)\in P_X\times S^3$ under $(p,v)\sim(p\cdot g,\ g^{-1}v)$. It is fibrewise bijective: on the fibre over $y$, fixing a point $p_0\in(P_X)_y$ every element of $P_X{}_y$ is $p_0\cdot g$ and every element of $S(E)_y$ is $[p_0,v]$ with $v\in S^3$, and $\Phi(p_0\cdot g)=[p_0\cdot g,e_1]=[p_0,g\,e_1]$; simple transitivity makes $g\mapsto g\,e_1$ a bijection $SU(2)\to S^3$, so $\Phi$ is a fibrewise bijection, and it is smooth with smooth inverse (both built from the diffeomorphism of Step 0 in local trivialisations). Hence $\Phi$ is a bundle isomorphism.
> >
> > **Step 2 — a unit section is a section of $P_X$.** A section $u\in\Gamma(E)$ with $|u|\equiv1$ is exactly a section of $S(E)$. Composing with $\Phi^{-1}$ gives a section $s:=\Phi^{-1}\circ u\in\Gamma(P_X)$. By [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]] — *a principal bundle is trivial if and only if it admits a global section, a section $s$ inducing the trivialisation $Y\times SU(2)\to P_X$, $(y,g)\mapsto s(y)\cdot g$* — the bundle $P_X$ is trivial. Therefore a unit section of $E$ trivialises $P_X$. $\blacksquare$

> [!note]- Lemma 2: A generic section is nonvanishing near the boundary with finitely many nondegenerate interior zeros
> **Statement:** Let $X$ be a compact oriented four-manifold with boundary $\partial X=M$, and $E\to X$ a rank-two complex (rank-four real) vector bundle whose restriction to a collar of $M$ is trivial. Then there is a section $s\in\Gamma(E)$ that is transverse to the zero section, nowhere zero on a neighbourhood of $M$, and has finitely many zeros $p_1,\dots,p_N$ in the interior, each nondegenerate.
>
> **Hint:** start from the constant unit section on the (trivial) collar bundle, which is nowhere zero hence vacuously transverse there, and extend to a global transverse section by the relative clause of the generic-sections theorem; count dimensions.
>
> **Why needed:** it produces a global trivialisation of $P_X$ off finitely many interior points and confines the topological defect to those points.
>
> > [!note]- Full proof
> > **Step 0 — a nonvanishing collar section.** Since $E$ is trivial over an open collar $U\supset M$, the constant section $u_0$ equal to the first basis vector of the trivialisation is a nowhere-zero section of $E|_U$. A nowhere-zero section is transverse to the zero section, vacuously, since its image never meets the zero section. Extend $u_0$ to a global (not necessarily transverse) section $s_0\in\Gamma(E)$ by multiplying by a smooth cutoff equal to $1$ on a smaller collar $U'\Subset U$ and supported in $U$; then $s_0$ is nowhere zero on $U'$ and transverse there.
> >
> > **Step 1 — perturb rel the collar.** Apply [[Thm - Generic Sections are Transverse to the Zero Section|the generic-sections theorem]], relative version: *for a vector bundle $E\to X$ over a compact manifold, a section already transverse to the zero section on a neighbourhood of a closed set $K$ can be perturbed, keeping it fixed near $K$, to a section transverse to the zero section on all of $X$; the perturbation is $s=s_0+\sum_i a_i\phi_i s_i$ with $\{s_i\}$ a spanning family, $\{\phi_i\}$ a partition of unity supported away from $K$, and almost every coefficient vector $a$ admissible.* Take $K=\overline{U'}$, a closed neighbourhood of $M$ on which $s_0$ is transverse. The resulting section $s$ equals $s_0$ near $M$, so it is nowhere zero on a neighbourhood of $M$, and it is transverse to the zero section on all of $X$.
> >
> > **Step 2 — the zero set is finite and interior.** By transversality, the zero set $s^{-1}(0)$ is a smooth submanifold of $X$ of dimension $\dim X-\operatorname{rank}_{\mathbb R}E=4-4=0$, that is, a discrete set; since $X$ is compact it is finite, say $\{p_1,\dots,p_N\}$. By Step 1 all $p_i$ lie in the interior (none in the neighbourhood of $M$ where $s\ne0$). Transversality at a zero $p_i$ means the vertical derivative $D_{p_i}s\colon T_{p_i}X\to E_{p_i}$ is an isomorphism (surjective between equal dimensions), that is, the zero is nondegenerate. This is exactly clauses (c)–(d) of the generic-sections theorem in the case $\operatorname{rank}_{\mathbb R}E=\dim X$ over the interior and $\operatorname{rank}_{\mathbb R}E>\dim M$ over the boundary. $\blacksquare$

> [!note]- Lemma 3: Each puncture contributes an integer
> **Statement:** Let $D\cong D^4$ be a closed chart-ball in the interior of $X$ with $S^3=\partial D$, on which $P_X$ is trivial (as it is, $D$ being contractible). Suppose $P_X$ is also trivialised on a neighbourhood of $S^3$ by a trivialisation $\tau$ (coming from a nowhere-zero section there), with connection matrix $A_X^\tau$, and let $A_X^\sigma$ be the connection matrix in a trivialisation $\sigma$ of $P_X|_D$. Then
> $$\frac1{8\pi^2}\int_{S^3}\operatorname{cs}(A_X^\tau)-\frac1{8\pi^2}\int_D\operatorname{tr}(F_{A_X}\wedge F_{A_X})\in\mathbb Z,$$
> where $S^3$ carries the boundary orientation of $D$.
>
> **Hint:** on $D$ use Stokes with $\sigma$; on $S^3$ compare $\tau$ and $\sigma$ by the gauge-variation theorem.
>
> **Why needed:** it is the accounting that makes the punctured Stokes computation of part (a) correct modulo $\mathbb Z$.
>
> > [!note]- Full proof
> > **Step 0 — the transgression identity in a trivialisation.** In any trivialisation with connection matrix $B\in\Omega^1(\cdot;\mathfrak{su}(2))$, [[Thm - Transgression Formula and the Chern-Simons Form|the transgression corollary]] gives $\operatorname{tr}(F_B\wedge F_B)=d\operatorname{cs}(B)$, where $\operatorname{cs}(B)=\operatorname{tr}(B\wedge dB+\tfrac23B\wedge B\wedge B)$ and $F_B=dB+B\wedge B$. This holds on the open sets where $\tau$ and $\sigma$ are defined.
> >
> > **Step 1 — Stokes on the ball.** The bundle $P_X|_D$ is trivial ($D$ contractible), with connection matrix $A_X^\sigma$; the four-form $\operatorname{tr}(F_{A_X}\wedge F_{A_X})$ is globally $d\operatorname{cs}(A_X^\sigma)$ on $D$. By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — *for a compact oriented manifold with boundary and a form $\omega$ of one degree below the top, $\int_D d\omega=\int_{\partial D}\iota^*\omega$ with $\partial D$ the induced boundary orientation* —
> > $$\int_D\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\int_D d\operatorname{cs}(A_X^\sigma)=\int_{S^3}\operatorname{cs}(A_X^\sigma)\qquad(\text{Step 0; Stokes; }\partial D=S^3).$$
> >
> > **Step 2 — compare the two trivialisations on $S^3$.** On the three-sphere $S^3$ both $\tau$ and $\sigma$ are defined, and they differ by a gauge transformation $g\colon S^3\to SU(2)$ with $A_X^\tau=(A_X^\sigma)^g=g^{-1}A_X^\sigma g+g^{-1}dg$ (the change-of-trivialisation law for connection matrices). The sphere $S^3$ is a closed oriented three-manifold, so [[Thm - Gauge Variation of the Chern-Simons Functional|the gauge-variation theorem]] applies — *for $A\in\Omega^1(M;\mathfrak{su}(2))$ on a closed oriented three-manifold and $g\colon M\to SU(2)$, $\tfrac1{8\pi^2}\int_M\operatorname{cs}(A^g)=\tfrac1{8\pi^2}\int_M\operatorname{cs}(A)+\deg g$ with $\deg g\in\mathbb Z$* — giving
> > $$\frac1{8\pi^2}\int_{S^3}\operatorname{cs}(A_X^\tau)=\frac1{8\pi^2}\int_{S^3}\operatorname{cs}(A_X^\sigma)+\deg g\qquad(\text{gauge-variation theorem, with }\deg g\in\mathbb Z).$$
> >
> > **Step 3 — combine.** Substituting the Step 1 identity $\tfrac1{8\pi^2}\int_{S^3}\operatorname{cs}(A_X^\sigma)=\tfrac1{8\pi^2}\int_D\operatorname{tr}(F_{A_X}\wedge F_{A_X})$ into the Step 2 equation,
> > $$\frac1{8\pi^2}\int_{S^3}\operatorname{cs}(A_X^\tau)=\frac1{8\pi^2}\int_D\operatorname{tr}(F_{A_X}\wedge F_{A_X})+\deg g.$$
> > Since $\deg g\in\mathbb Z$, the difference of the two terms on the left- and right-hand sides is the integer $\deg g$. Therefore the displayed difference in the statement is an integer. $\blacksquare$

> [!note]- Lemma 4: The bulk integral is independent of the interior extension connection
> **Statement:** Let $X$ be a compact oriented four-manifold with $\partial X=M$, $P_X\to X$ a principal $SU(2)$-bundle, and $A_X,\widetilde A_X$ two connections on $P_X$ that restrict to the *same* connection on $M$ (i.e. $\iota^*A_X=\iota^*\widetilde A_X$ as connections on $P_X|_M$). Then
> $$\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\int_X\operatorname{tr}(F_{\widetilde A_X}\wedge F_{\widetilde A_X})\quad\text{in }\mathbb R.$$
>
> **Hint:** the difference of the two second Chern forms is exact, with the transgression form as primitive; the primitive restricts to zero on $M$ because the two connections agree there.
>
> **Why needed:** it lets us homotope the two connections to a product form near the collar in part (b) without changing the integrals.
>
> > [!note]- Full proof
> > **Step 0 — the difference of connections is a global tensorial one-form.** The difference $b:=A_X-\widetilde A_X$ is a connection minus a connection, hence a global section of $T^*X\otimes\operatorname{ad}P_X$, i.e. a basic $\operatorname{ad}$-valued one-form; over $M$ it restricts to $\iota^*b=\iota^*A_X-\iota^*\widetilde A_X=0$ by hypothesis.
> >
> > **Step 1 — the transgression primitive.** Set $\omega_0=\widetilde A_X$, $\omega_1=A_X$, $\omega_t=\omega_0+tb$, $F_t=F_{\omega_t}$, and take the invariant polynomial $p(\xi)=\operatorname{tr}(\xi^2)$ of degree $d=2$ with polarisation $p(\xi,\eta)=\operatorname{tr}(\xi\eta)$. By [[Thm - Transgression Formula and the Chern-Simons Form|the transgression formula]] — *for connections $\omega_0,\omega_1$ on $P_X$ and $p\in I(SU(2))$ of degree $d$, $p(F_1)-p(F_0)=d\,Tp(\omega_0,\omega_1)$ with primitive $Tp=d\int_0^1 p(b,F_t,\dots,F_t)\,dt$ descended to a global form on $X$* — we obtain, with $d=2$,
> > $$\operatorname{tr}(F_{A_X}\wedge F_{A_X})-\operatorname{tr}(F_{\widetilde A_X}\wedge F_{\widetilde A_X})=d\,T,\qquad T:=2\int_0^1\operatorname{tr}(b\wedge F_t)\,dt\in\Omega^3(X),$$
> > a globally defined three-form on $X$ (well defined because $b$ and each $F_t$ are global forms on $X$).
> >
> > **Step 2 — the primitive vanishes on the boundary.** Pulling back by $\iota\colon M\hookrightarrow X$ and using that pullback commutes with wedge and with the fibre integral in $t$,
> > $$\iota^*T=2\int_0^1\operatorname{tr}(\iota^*b\wedge\iota^*F_t)\,dt=0\qquad(\text{since }\iota^*b=0\text{ by Step 0}).$$
> >
> > **Step 3 — Stokes.** By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] on the compact oriented $X$ with $\partial X=M$,
> > $$\int_X\big[\operatorname{tr}(F_{A_X}\wedge F_{A_X})-\operatorname{tr}(F_{\widetilde A_X}\wedge F_{\widetilde A_X})\big]=\int_X dT=\int_M\iota^*T=0\qquad(\text{Step 1; Stokes; Step 2}).$$
> > Therefore the two bulk integrals are equal in $\mathbb R$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout write $\operatorname{cs}(B)=\operatorname{tr}(B\wedge dB+\tfrac23B\wedge B\wedge B)$ for a gauge potential $B$, and recall the transgression corollary $\operatorname{tr}(F_B\wedge F_B)=d\operatorname{cs}(B)$ valid in any trivialisation ([[Thm - Transgression Formula and the Chern-Simons Form|transgression corollary]]). Recall also that $\vartheta(A)=\tfrac1{8\pi^2}\int_M\operatorname{cs}(A)\bmod\mathbb Z$ is independent of the trivialisation of $P$ modulo $\mathbb Z$, by the [[Thm - Gauge Variation of the Chern-Simons Functional|gauge-variation theorem]] (two trivialisations differ by $g\colon M\to SU(2)$ and $\tfrac1{8\pi^2}\int_M\operatorname{cs}$ changes by $\deg g\in\mathbb Z$).
>
> ---
> ### Part (a): the bounding formula
>
> **Step 0 — reduce to a global trivialisation off finitely many points.** The associated bundle $E=P_X\times_{SU(2)}\mathbb C^2$ is a rank-four real bundle over $X$; over a collar of $M$ it is trivial, because $P_X|_M\cong P$ is trivial ([[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|every SU(2)-bundle over a manifold of dimension ≤ 3 is trivial]]) and the collar retracts to $M$. By **Lemma 2** choose a section $s\in\Gamma(E)$ transverse to the zero section, nowhere zero on a neighbourhood of $M$, with finitely many interior zeros $p_1,\dots,p_N$. Choose disjoint closed chart-balls $D_1,\dots,D_N$ with $p_i\in D_i^\circ$, all in the interior of $X$ and disjoint from the neighbourhood of $M$ where $s\ne0$; write $S_i=\partial D_i\cong S^3$ and $X'=X\setminus\bigcup_i D_i^\circ$. On $X'$ the section $s$ is nowhere zero, so $u:=s/|s|$ is a unit section of $E|_{X'}$; by **Lemma 1** it induces a trivialisation $\tau$ of $P_X|_{X'}$, with global connection matrix $A_X^\tau\in\Omega^1(X';\mathfrak{su}(2))$. Because $u$ is defined on a neighbourhood of $M$, the restriction $\tau|_M$ is a genuine trivialisation of $P$, and in it the connection matrix of $A$ is $\iota^*A_X^\tau$.
>
> **Step 1 — Stokes on the punctured manifold.** On $X'$ the transgression corollary gives $\operatorname{tr}(F_{A_X}\wedge F_{A_X})=d\operatorname{cs}(A_X^\tau)$ globally. The manifold $X'$ is compact and oriented with boundary $\partial X'=M\sqcup\bigsqcup_i(-S_i)$, where each $S_i$ carries its orientation as $\partial D_i$ and appears in $\partial X'$ with the opposite sign, because the outward normal of $X'$ along $S_i$ points into $D_i$, which is the inward normal of $D_i$ ([[Def - Manifold with Boundary and Induced Orientation|induced-orientation convention]]). By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]],
> $$\int_{X'}\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\int_{\partial X'}\operatorname{cs}(A_X^\tau)=\int_M\operatorname{cs}(A_X^\tau)-\sum_{i=1}^N\int_{S_i}\operatorname{cs}(A_X^\tau)\qquad(\text{transgression; Stokes; orientation of }\partial X').$$
> On $M$ we have $\int_M\operatorname{cs}(A_X^\tau)=\int_M\operatorname{cs}(\iota^*A_X^\tau)$, the integral of the Chern–Simons form of $A$ in the trivialisation $\tau|_M$.
>
> **Step 2 — restore the punctures.** By additivity of the integral over $X=X'\cup\bigcup_i D_i$ (the pieces overlap only in the measure-zero spheres $S_i$),
> $$\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\int_{X'}\operatorname{tr}(F_{A_X}\wedge F_{A_X})+\sum_{i=1}^N\int_{D_i}\operatorname{tr}(F_{A_X}\wedge F_{A_X}).$$
> By **Lemma 3** applied to each ball $D_i$ (with $\tau$ the Step 0 trivialisation on $S_i$ and $\sigma_i$ a trivialisation of $P_X|_{D_i}$),
> $$\frac1{8\pi^2}\int_{S_i}\operatorname{cs}(A_X^\tau)=\frac1{8\pi^2}\int_{D_i}\operatorname{tr}(F_{A_X}\wedge F_{A_X})+m_i,\qquad m_i\in\mathbb Z.$$
>
> **Step 3 — combine.** Multiply the Step 1 identity by $\tfrac1{8\pi^2}$ and substitute the Lemma 3 relation for each $\tfrac1{8\pi^2}\int_{S_i}\operatorname{cs}(A_X^\tau)$:
> $$\frac1{8\pi^2}\int_{X'}\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\frac1{8\pi^2}\int_M\operatorname{cs}(A_X^\tau)-\sum_{i=1}^N\Big[\frac1{8\pi^2}\int_{D_i}\operatorname{tr}(F_{A_X}\wedge F_{A_X})+m_i\Big].$$
> Move the ball integrals to the left and use the Step 2 additivity to recognise the whole of $X$:
> $$\frac1{8\pi^2}\int_{X'}\operatorname{tr}(F_{A_X}\wedge F_{A_X})+\sum_{i=1}^N\frac1{8\pi^2}\int_{D_i}\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\frac1{8\pi^2}\int_M\operatorname{cs}(A_X^\tau)-\sum_{i=1}^N m_i,$$
> that is,
> $$\frac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\frac1{8\pi^2}\int_M\operatorname{cs}(\iota^*A_X^\tau)-\sum_{i=1}^N m_i\qquad(\text{Step 2 additivity}).$$
>
> **Step 4 — conclude modulo $\mathbb Z$.** The first term on the right, $\tfrac1{8\pi^2}\int_M\operatorname{cs}(\iota^*A_X^\tau)$, is a representative in $\mathbb R$ of $\vartheta(A)$, computed in the trivialisation $\tau|_M$; since $\vartheta(A)$ is trivialisation-independent modulo $\mathbb Z$, its class in $\mathbb R/\mathbb Z$ is $\vartheta(A)$. The remaining term $\sum_i m_i$ is an integer. Therefore
> $$\frac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})\equiv\vartheta(A)\pmod{\mathbb Z},$$
> which is part (a).
>
> *(Smallest concrete case.)* If $P_X$ is already trivial over all of $X$ — for instance $X=D^4$, $M=S^3$, $P_X$ the product bundle — the section $s$ can be taken nowhere zero, $N=0$, no balls are removed, and Steps 2–3 collapse to the single line $\tfrac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\tfrac1{8\pi^2}\int_M\operatorname{cs}(\iota^*A_X^\tau)$, which is $\vartheta(A)$ exactly in the induced trivialisation and modulo $\mathbb Z$ in any other.
>
> ---
> ### Part (b): independence of the extension
>
> **Step 0 — the quick route.** By part (a), each bulk integral is congruent to $\vartheta(A)$ modulo $\mathbb Z$:
> $$\frac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}^2)\equiv\vartheta(A)\equiv\frac1{8\pi^2}\int_{X'}\operatorname{tr}(F_{A'_X}^2)\pmod{\mathbb Z},$$
> so their difference lies in $\mathbb Z$. This already proves (b); we now give the direct gluing argument, which does not presuppose part (a) and exhibits the integer as a genuine second Chern number.
>
> **Step 1 — normalise the connections near the collar.** Fix collars $M\times[0,1)\hookrightarrow X$ and $M\times(-1,0]\hookrightarrow\overline{X'}$, where $\overline{X'}$ is $X'$ with the reversed orientation, so that $\partial\overline{X'}=-M$. Over $M\times[0,1)$ the product connection $\pi^*A$ (pullback of $A$ under the projection $\pi\colon M\times[0,1)\to M$) is a connection on $P_X$ restricting to $A$ on $M$. Choosing a smooth interpolation supported in the collar, replace $A_X$ by a connection $\widehat A_X$ that equals $\pi^*A$ on a smaller collar $M\times[0,\tfrac12]$ and equals $A_X$ outside the collar; likewise replace $A'_X$ by $\widehat A'_X$ equal to $\pi^*A$ near the collar. By **Lemma 4** (both $\widehat A_X$ and $A_X$ restrict to $A$ on $M$),
> $$\int_X\operatorname{tr}(F_{\widehat A_X}^2)=\int_X\operatorname{tr}(F_{A_X}^2),\qquad\int_{X'}\operatorname{tr}(F_{\widehat A'_X}^2)=\int_{X'}\operatorname{tr}(F_{A'_X}^2),$$
> so replacing the connections changes nothing.
>
> **Step 2 — glue.** Since $P|_M$ is trivial, the bundles $P_X$ and $P'_X$, both restricting to $P$ over $M$, glue along the collar (matching the trivialisations of $P$ over $M$) into a principal $SU(2)$-bundle $P_Z\to Z$ over the closed oriented four-manifold $Z=X\cup_M\overline{X'}$. Because $\widehat A_X$ and $\widehat A'_X$ both equal the *same* product connection $\pi^*A$ on the overlapping collar, they glue into a smooth connection $A_Z$ on $P_Z$. The curvature $\operatorname{tr}(F_{A_Z}\wedge F_{A_Z})$ is a smooth four-form on all of $Z$, agreeing with the respective pieces on $X$ and $\overline{X'}$.
>
> **Step 3 — integrate and apply integrality.** By additivity of the integral over $Z=X\cup\overline{X'}$ and $\int_{\overline{X'}}=-\int_{X'}$ (reversed orientation),
> $$\frac1{8\pi^2}\int_Z\operatorname{tr}(F_{A_Z}^2)=\frac1{8\pi^2}\int_X\operatorname{tr}(F_{\widehat A_X}^2)-\frac1{8\pi^2}\int_{X'}\operatorname{tr}(F_{\widehat A'_X}^2)\qquad(\text{additivity; orientation reversal}).$$
> The left-hand side is a Chern–Weil integral over the closed oriented four-manifold $Z$; by [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree|the second-Chern-number theorem]] — *for a principal $SU(2)$-bundle $P_Z$ with connection $A_Z$ over a closed connected oriented four-manifold, $\tfrac1{8\pi^2}\int_Z\operatorname{tr}(F_{A_Z}\wedge F_{A_Z})=k(P_Z)\in\mathbb Z$* — it equals $k(P_Z)\in\mathbb Z$. Combined with the Step 1 equalities,
> $$\frac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}^2)-\frac1{8\pi^2}\int_{X'}\operatorname{tr}(F_{A'_X}^2)=k(P_Z)\in\mathbb Z.$$
> (If $Z$ is disconnected, apply the theorem to each component and sum the integers.) This is part (b), and it exhibits the integer explicitly as the second Chern number of the glued bundle.
>
> ---
> ### Part (c): the cylinder formula
>
> **Step 0 — the cylinder bundle is trivial.** For $X=M\times[t_0,t_1]$ the bundle $P_X=P\times[t_0,t_1]$ is trivial ($M$ is a three-manifold, so $P$ is trivial, and $[t_0,t_1]$ is contractible). Fix the product trivialisation; then $A\in\Omega^1(X;\mathfrak{su}(2))$ is a global gauge potential and $A_t=\iota_t^*A$ is its restriction to the slice $\iota_t\colon M\to M\times\{t\}$.
>
> **Step 1 — transgression and Stokes with two boundary components.** By the transgression corollary $\operatorname{tr}(F_A\wedge F_A)=d\operatorname{cs}(A)$ globally on $X$. The product $M\times[t_0,t_1]$ has boundary, with its induced orientation, $\partial X=M\times\{t_1\}\ \sqcup\ (-M)\times\{t_0\}$: the top slice ($t=t_1$, outward normal $+\partial_t$) is positively oriented and the bottom slice ($t=t_0$, outward normal $-\partial_t$) negatively, by [[Def - Manifold with Boundary and Induced Orientation|the outward-normal-first convention]] (consistent with the fundamental theorem of calculus $\partial[t_0,t_1]=\{t_1\}-\{t_0\}$). Hence, by [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]],
> $$\int_{M\times[t_0,t_1]}\operatorname{tr}(F_A\wedge F_A)=\int_{M\times[t_0,t_1]}d\operatorname{cs}(A)=\int_{M\times\{t_1\}}\operatorname{cs}(A)-\int_{M\times\{t_0\}}\operatorname{cs}(A).$$
>
> **Step 2 — identify the slice integrals.** Pulling back the Chern–Simons form to the slice, and using that pullback commutes with the exterior derivative on one-forms ([[Thm - Pullback Commutes with d for 1-Forms|pullback commutes with d]]), so that $\iota_t^*(dA)=d(\iota_t^*A)=dA_t$,
> $$\iota_t^*\operatorname{cs}(A)=\operatorname{tr}\!\big(\iota_t^*A\wedge\iota_t^*(dA)+\tfrac23(\iota_t^*A)^{\wedge3}\big)=\operatorname{tr}\!\big(A_t\wedge dA_t+\tfrac23A_t\wedge A_t\wedge A_t\big)=\operatorname{cs}(A_t).$$
> Therefore $\int_{M\times\{t\}}\operatorname{cs}(A)=\int_M\operatorname{cs}(A_t)$ for $t\in\{t_0,t_1\}$ (the slice $M\times\{t\}$ is identified with $M$ by $\iota_t$, an orientation-preserving diffeomorphism, and integration is invariant under such by [[Thm - Change of Variables for Integration on Manifolds|the change-of-variables theorem]]).
>
> **Step 3 — divide and conclude.** Substituting into Step 1 and dividing by $8\pi^2$,
> $$\frac1{8\pi^2}\int_{M\times[t_0,t_1]}\operatorname{tr}(F_A\wedge F_A)=\frac1{8\pi^2}\int_M\operatorname{cs}(A_{t_1})-\frac1{8\pi^2}\int_M\operatorname{cs}(A_{t_0})=\vartheta(A_{t_1})-\vartheta(A_{t_0}).$$
> The last equality is an equality in $\mathbb R$, not merely modulo $\mathbb Z$, because both slice integrals are computed in the *same* product trivialisation, so no change-of-trivialisation integer intervenes. This is part (c). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Secondary characteristic classes and Chern–Simons in odd dimensions.** The same transgression-and-Stokes mechanism defines a Chern–Simons invariant for any $\operatorname{Ad}$-invariant polynomial $p$ of degree $d$ on any structure group, living on a $(2d-1)$-manifold and taking values in $\mathbb R/\Lambda$ for a period lattice $\Lambda$. The theorem applies because the only two facts used are the transgression identity $p(F)=d\,Tp$ and the integrality of $\int p(F)$ over a closed $2d$-manifold. It is non-obvious that the fractional ambiguity is a *lattice* and not all of $\mathbb R$: this is exactly the integrality of the primary Chern–Weil number, and it fails for polynomials that are not integral characteristic classes.

**The eta invariant and the Atiyah–Patodi–Singer boundary term.** In index theory on a four-manifold with boundary, the index of a Dirac operator equals a bulk integral of a characteristic form plus a boundary correction; the Chern–Simons functional is the connection-dependent piece of that correction. The theorem applies because the bulk integrand is again $\operatorname{tr}(F\wedge F)$ up to normalisation, so its non-integer boundary part is $\vartheta$. The non-obvious point is that a spectral invariant of the boundary operator (the eta invariant) and the geometric $\vartheta$ enter the same formula, tying an analytic quantity to a topological one.

**Instanton Floer homology and the gradient of $\vartheta$.** Part (c) says the change in $\vartheta$ along a path of connections is the second-Chern-form integral over the trace of the path; combined with the first-variation formula, $\vartheta$ is a functional on the space of connections on $M$ whose critical points are the flat connections and whose gradient flow lines are the anti-self-dual connections on the cylinder $M\times\mathbb R$. The theorem applies because the cylinder is the bounding four-manifold of the two ends. It is non-obvious that a functional defined only modulo $\mathbb Z$ nevertheless has a well-defined real-valued *difference* along any path — which is precisely the content of part (c) — and this is what allows the Morse-theoretic construction to assign integer gradings by the spectral flow.

---

# Bridges

- **From the boundary term of the Yang–Mills action (chapter VII).** On a four-manifold with boundary the Yang–Mills action $\tfrac12\int_X|F_{A_X}|^2$ and the topological term $\tfrac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})$ are related by the pointwise inequality $|F|^2\ge\pm\langle F,\star F\rangle$, with equality for (anti-)self-dual connections. Part (a) identifies the topological term with $\vartheta(A)$ on the boundary modulo $\mathbb Z$, so the Chern–Simons functional is literally the boundary contribution to the instanton action; the self-dual Yang–Mills equations on $X$ become, on the cylindrical end, the downward gradient flow of $\vartheta$. This is the construction that makes the Chern–Simons functional the action of three-dimensional gauge theory.

- **From Chern–Weil theory to secondary invariants.** The primary invariant of a bundle is the integer $\tfrac1{8\pi^2}\int_Z\operatorname{tr}(F\wedge F)$ over a closed manifold; when the closed manifold is cut along a three-manifold $M$, the primary invariant splits as a sum of two boundary quantities that are individually only real numbers, well defined modulo $\mathbb Z$. The construction is: choose bounding data, integrate the second Chern form, read the fractional part. Part (b) is what guarantees the fractional part is intrinsic to $(M,P,A)$; the whole edifice of secondary (Chern–Simons) invariants rests on this single integrality-plus-gluing step.

- **From the transgression form to the WZW term.** For a pure-gauge connection $A=g^{-1}dg$ the Chern–Simons form reduces to $-\tfrac13\operatorname{tr}((g^{-1}dg)^{\wedge3})$, the bi-invariant three-form of $SU(2)$ whose integral is $\pm24\pi^2$ times a degree. The cylinder formula of part (c), applied to a path of pure-gauge connections, expresses the change of $\vartheta$ as the integral of this three-form over the trace of the path, which is the Wess–Zumino–Witten term of two-dimensional conformal field theory. The construction runs entirely through the transgression identity and Stokes; the appearance of a degree is the same $\deg g$ that produces the integer ambiguity in part (a).

---

# Unlocked by This

> [!tip] The Chern–Simons action of three-dimensional gauge theory *(from Mathematical Physics)*
> With part (a) identifying $\vartheta$ as the boundary fractional part of the instanton number, the functional $A\mapsto\vartheta(A)$ becomes the action of three-dimensional topological gauge theory. Its critical points are the flat connections (**[[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections]]**), and its quantisation produces topological invariants of three-manifolds and knots.

> [!tip] Instanton Floer homology *(from Low-Dimensional Topology)*
> The gradient flow of $\vartheta$ on the space of connections over $M$, whose flow lines are the anti-self-dual connections on the cylinder $M\times\mathbb R$ supplied by part (c), is the setting of **instanton Floer homology**: a homology theory generated by the flat connections and with differential counting instantons, whose Euler characteristic recovers the Casson invariant of $M$.
