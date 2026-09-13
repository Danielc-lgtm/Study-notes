---
type: definition
subject: gauge-theory
prereqs:
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
  - "Def - Charge-Current 3-Form"
  - "Def - Hodge Star in Arbitrary Signature"
  - "Thm - Bianchi Identity for a Principal Connection"
tags: [geometry, gauge-theory, electrodynamics, physics]
---

# Notation

Throughout this page $M$ is an oriented Lorentzian four-manifold, the mathematical model of spacetime. In agreement with the whole of chapter VII we work in Bär's signature $(-,+,+,+)$, that is, in local coordinates $(t,x,y,z)$ adapted to the metric we have $\langle\partial_t,\partial_t\rangle<0$ and $\langle\partial_x,\partial_x\rangle,\langle\partial_y,\partial_y\rangle,\langle\partial_z,\partial_z\rangle>0$, and we set the speed of light $c=1$. The index of the tangent space, meaning the number of negative signs in a generalised orthonormal basis, is $p=1$. The volume form is $\mathrm{vol}$, and on Minkowski space in the standard coordinates $\mathrm{vol}=dt\wedge dx\wedge dy\wedge dz$.

The objects that enter the equations are all fixed on their own pages, which we recall here so that this page can be read cold.

- $P\to M$ is a principal $U(1)$-bundle and $\omega\in\mathcal C(P)$ is a connection on it; the **[[Def - U(1) Gauge Field and Electromagnetic Connection|electromagnetic field strength]]** is the real $2$-form $F\in\Omega^2(M;\mathbb R)$ determined by the descended curvature through $\bar\Omega=iF$. Because $U(1)$ is abelian and its adjoint representation is trivial, the local curvature form $s^*\Omega$ is independent of the local section $s$ and defines the global $\bar\Omega\in\Omega^2(M;i\mathbb R)$; this is exactly the content of [[Def - U(1) Gauge Field and Electromagnetic Connection]]. In coordinates $(t,x,y,z)$ we write, with time-dependent vector fields $\vec E=(E_x,E_y,E_z)$ and $\vec B=(B_x,B_y,B_z)$,
$$F = E_x\,dx\wedge dt + E_y\,dy\wedge dt + E_z\,dz\wedge dt + B_x\,dy\wedge dz + B_y\,dz\wedge dx + B_z\,dx\wedge dy,$$
so that $F_{i0}=E_i$; $\vec E$ is the electric field and $\vec B$ the magnetic field of the observer whose worldlines are the $t$-coordinate lines. Both are coordinate-dependent.
- $J\in\Omega^3(M;\mathbb R)$ is the **[[Def - Charge-Current 3-Form|charge–current $3$-form]]**, written in coordinates as
$$J = \varrho\,dx\wedge dy\wedge dz - j_x\,dt\wedge dy\wedge dz - j_y\,dt\wedge dz\wedge dx - j_z\,dt\wedge dx\wedge dy,$$
with charge density $\varrho\in C^\infty(M)$ and current density $\vec j=(j_x,j_y,j_z)$; this is [[Def - Charge-Current 3-Form]].
- $\star\colon\Omega^k(M;\mathbb R)\to\Omega^{n-k}(M;\mathbb R)$ is the **[[Def - Hodge Star in Arbitrary Signature|Hodge star]]** attached to the metric and orientation, defined pointwise by the requirement $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$ for all $\omega\in\Lambda^k$, $\eta\in\Lambda^{n-k}$; this is [[Def - Hodge Star in Arbitrary Signature]]. On Minkowski space its action on the coordinate $2$-forms is the six-line table
$$\star(dt\wedge dx)=dy\wedge dz,\quad \star(dt\wedge dy)=dz\wedge dx,\quad \star(dt\wedge dz)=dx\wedge dy,$$
$$\star(dy\wedge dz)=-dt\wedge dx,\quad \star(dz\wedge dx)=-dt\wedge dy,\quad \star(dx\wedge dy)=-dt\wedge dz,$$
from which $\star\star=-1$ on $2$-forms in this signature and dimension.
- $d\colon\Omega^k(M)\to\Omega^{k+1}(M)$ is the exterior derivative ([[Def - Exterior Derivative on a Manifold]]), and $\operatorname{div}$, $\operatorname{rot}$ denote the ordinary spatial divergence and curl of a time-dependent vector field on the $\{t=\text{const}\}$ slices.

> [!warning] Convention: the Hodge star ($\star_B$ versus $\star_V$)
> The series uses **Bär's Hodge star** $\star=\star_B$, fixed by $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$, which satisfies $\star\star=(-1)^{k(n-k)+p}$ on $k$-forms. The vault's Riemannian operator [[Def - The Hodge Star Operator|$\star_V$]] (Hodge Theory I) is fixed by the other common relation $\alpha\wedge\star_V\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}$; the two differ by $\star_B=(-1)^{k(n-k)}\star_V$, and on a definite ($p=0$) space they also differ from a third normalisation by the sign $(-1)^p$. The comparison relevant here is that in dimension four on $2$-forms the shuffle sign $(-1)^{k(n-k)}=(-1)^{2\cdot2}=+1$, so the two conventions agree there; the full sign bookkeeping is carried out once on [[Def - Hodge Star in Arbitrary Signature]] and is not repeated. In Lorentzian signature ($p=1$) on Minkowski $2$-forms one has $\star_B=-\star_V$.

> [!warning] Convention: the special-relativity pages ($(+,-,-,-)$, SI units)
> The Special Relativity chapter states the same physics in the opposite signature and in SI units. There [[Thm - Maxwell Equations]] (SR XXII) reads $d\star_V F=\mu_0\star_V j$, in signature $(+,-,-,-)$ with the constant $\mu_0$ present, and the current is packaged as the four-current $1$-form $j$ of [[Def - The Electric Four-Current]]. The dictionary to the present page is: the metrics are related by $g_B=-g_{\mathrm{SR}}$; the field strength $F$ is the *same* $2$-form and $\vec E$, $\vec B$ are the *same* fields; on Minkowski $2$-forms $\star_B=-\star_V$; the source $3$-form and the four-current $1$-form are related by $J=\star_B\,j^\flat$ up to the sign computed on [[Def - Charge-Current 3-Form]]. Setting $\mu_0=1$ (unit charge) and carrying the two sign flips through turns $d\star_V F=\mu_0\star_V j$ into the equation $d\star_B F+J=0$ used below; the two statements are the same law.

---

# Axiom Motivation

The task of this chapter is to recognise classical electrodynamics as the theory of a connection on a principal $U(1)$-bundle. Once the [[Def - U(1) Gauge Field and Electromagnetic Connection|electromagnetic field strength]] $F$ has been identified with the curvature and the [[Def - Charge-Current 3-Form|charge–current]] $J$ with a $3$-form, the physical content of Maxwell's four vector-calculus equations must be repackaged as equations between differential forms. This page fixes that repackaging: it names, as the two defining laws of the theory, the equations that a pair $(\omega,J)$ must satisfy for the connection to describe a physically admissible electromagnetic field with the given sources. The derivations that show these two form-equations reproduce the four classical laws are theorems on the next pages; here we state the laws and justify why *these* are the right laws to write down.

The first desideratum is that the equations be **coordinate-free and gauge-invariant**. The classical Maxwell equations are written in a chosen inertial frame in terms of $\vec E$, $\vec B$, $\varrho$, $\vec j$, all of which depend on that frame; a fundamental law should not. The exterior derivative $d$ and the Hodge star $\star$ are the only two natural first-order operators on forms — $d$ is built from the smooth structure alone and $\star$ from the metric and orientation alone — so any law built from $d$, $\star$, $F$, and $J$ is automatically independent of coordinates. Gauge invariance is likewise forced: since $U(1)$ is abelian, the curvature and hence $F$ do not change under a gauge transformation ($\bar\Omega'=\bar\Omega$, so $F'=F$, from [[Thm - Gauge Transformations Act on Connections and Curvature|the transformation law]] with $\operatorname{Ad}_{g^{-1}}=\mathrm{id}$), and $J$ is a fixed geometric object; so any equation among $dF$, $d\star F$, and $J$ is gauge-invariant on the nose. A law written in terms of the potential $A$ alone would fail both tests.

The second desideratum is that the equations **split into an identity and a law**, matching the fact that two of Maxwell's classical equations (Gauss for magnetism and Faraday) contain no sources while the other two (Coulomb and Ampère) do. The source-free pair must be automatic, true for *every* connection, because they express the mere fact that $F$ is a curvature; the pair with sources must be a genuine constraint, singling out the physical connections among all connections with the prescribed current. This is exactly the shape produced by the two operators. The equation $dF=0$ is automatic: $F$ is (a real multiple of) the descended curvature of a principal connection, and the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] forces its exterior derivative to vanish. The equation $d\star F+J=0$ is not automatic — it is the Euler–Lagrange equation of the electromagnetic action, and it is the place where the sources $J$ enter. So the split into "homogeneous identity" and "inhomogeneous law" is not an accident of notation; it reflects the difference between a property of curvatures and a dynamical constraint.

The third desideratum concerns **the exact form of the inhomogeneous equation, and in particular its sign**. One could imagine writing $d\star F=J$, $d\star F+J=0$, or $d\star F=\mu J$ for various constants $\mu$. The constant is a matter of units and disappears once charge is measured in the units in which $\mu_0=1$. The sign, however, is fixed by the variational principle: the electromagnetic action pairs the field-energy term $\tfrac12 F\wedge\star F$ against the coupling term $A\wedge J$, and demanding that the connection be a critical point produces the combination $d\star F+J$ set to zero, not $d\star F-J$ (see [[Thm - Euler-Lagrange Equation of the Electromagnetic Action]], derived on its own page). If one dropped the sign discipline and wrote $d\star F=J$ instead, then the continuity equation would still read $dJ=0$ (because $d\,d\star F=0$ regardless of sign), so the conservation of charge would survive — but Poynting's theorem, the local energy balance $\tfrac12\partial_t(|\vec E|^2+|\vec B|^2)+\operatorname{div}(\vec E\times\vec B)=-\langle\vec E,\vec j\rangle$, would come out with the wrong sign on the work term $\langle\vec E,\vec j\rangle$, predicting that currents *gain* energy from the field where they should lose it. The sign is therefore not cosmetic, and the series fixes it once and for all as $d\star F+J=0$.

> [!warning] Convention: Bär's internal sign typo
> Bär's text is inconsistent about this sign. On p. 86, deriving the Euler–Lagrange equation, he obtains $d\star F+J=0$; on p. 95, restating it before Poynting's theorem, he writes $d\star F=J$ (Wernli typo appendix, item 21). These two differ by the sign of $J$. **The series adopts $d\star F+J=0$ throughout**, consistent with the variational derivation on [[Thm - Euler-Lagrange Equation of the Electromagnetic Action]], and re-derives Poynting's theorem with this sign on [[Thm - Poynting's Theorem]]. Every page of the series that needs the inhomogeneous law uses the corrected form.

Could a reader invent these two equations from the desiderata alone? Yes: the demand for a gauge-invariant, coordinate-free, first-order theory in which two equations are automatic curvature-identities and two are source constraints leaves essentially no freedom. The only natural closed condition on a curvature is $dF=0$; the only natural first-order source equation built from $\star$ is $d\star F=\pm J$ (up to units); and the variational principle fixes the sign. What remains is to *verify* that these abstract equations, written out in a frame, are the Maxwell equations of the textbooks, which is the business of the coordinate theorem below.

---

# The Definition

Let $M$ be an oriented Lorentzian four-manifold, $P\to M$ a principal $U(1)$-bundle, $\omega\in\mathcal C(P)$ a connection with descended curvature $\bar\Omega=iF$, $F\in\Omega^2(M;\mathbb R)$, and let $J\in\Omega^3(M;\mathbb R)$ be a charge–current $3$-form. We say that the pair $(\omega,J)$ — equivalently, the field strength $F$ together with the source $J$ — **satisfies Maxwell's equations** if the following two equations hold on all of $M$:

$$\boxed{\;dF = 0\;}\qquad\text{(homogeneous Maxwell equation)},$$

$$\boxed{\;d\star F + J = 0\;}\qquad\text{(inhomogeneous Maxwell equation)}.$$

The first equation, $dF=0$, is the **homogeneous** (source-free) Maxwell equation. It is an **identity**, satisfied by every field strength that arises as the curvature of a $U(1)$-connection, and requires nothing of the source $J$. Its status as an identity is the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]]:

> **Theorem (Bianchi identity, abelian case, restated).** Let $\omega$ be a connection on a principal $G$-bundle with curvature $\Omega$; then the exterior covariant derivative of the curvature vanishes, $d^\omega\Omega=0$, and locally $dF_A+[A\wedge F_A]=0$. When $G=U(1)$ is abelian the bracket term vanishes, the local curvature forms $s^*\Omega$ patch to a global $\bar\Omega=iF$ (as on [[Def - U(1) Gauge Field and Electromagnetic Connection]]), and the identity reduces to $d\bar\Omega=0$, that is, $dF=0$.

Thus $dF=0$ is not a law imposed on the field but a theorem about curvatures; it is written as one of Maxwell's equations because, decomposed in coordinates, it *is* two of the four classical laws.

The second equation, $d\star F+J=0$, is the **inhomogeneous** Maxwell equation. It is a genuine **law**: among all connections whose curvature has the prescribed relation to the source, it selects the physical ones. It is precisely the Euler–Lagrange equation of the electromagnetic action functional, and this is what fixes both its form and its sign:

> **Theorem (Euler–Lagrange criterion, restated).** With the action built from the Lagrangian $L(\omega)=\tfrac12 F\wedge\star F+A\wedge J$, a connection $\omega$ is a critical point of $\int_{\bar U}L$ under all compactly supported variations if and only if $d\star F+J=0$. This is proved in full on [[Thm - Euler-Lagrange Equation of the Electromagnetic Action]].

The pair of boxed equations is the definition. The unpacking into the four classical vector-calculus equations, the passage that makes the physical content visible, is carried out on [[Thm - Maxwell Equations in Coordinates]]; we restate its conclusions here because they are the meaning of the two boxed equations:

- $dF=0$ is equivalent, in a frame on Minkowski space, to $\operatorname{div}\vec B=0$ (Gauss's law for magnetism, equation (3.7)) together with $\partial_t\vec B+\operatorname{rot}\vec E=0$ (Faraday's law of induction, equation (3.8));
- $d\star F+J=0$ is equivalent, in the same frame, to $\operatorname{div}\vec E=\varrho$ (Coulomb's / Gauss's law, equation (3.9)) together with $\operatorname{rot}\vec B-\partial_t\vec E=\vec j$ (Ampère's law with Maxwell's correction, equation (3.10)).

The numbering $(3.7)$–$(3.10)$ is Bär's. The two boxed equations are the source of all four; the homogeneous one carries no charge or current, and the inhomogeneous one is where $\varrho$ and $\vec j$ appear.

**The smallest concrete case.** Take $M=\mathbb R^{1,3}$, Minkowski space, and $P=M\times U(1)$ the trivial bundle with the flat background connection, so that $F=dA$ for a globally defined potential $1$-form $A$. In this case $dF=d\,dA=0$ is immediate from $d^2=0$ ([[Thm - d-Squared-is-Zero]]), which is the concrete face of the Bianchi identity; and $d\star F+J=0$ is a single third-order-in-$A$ but first-order-in-$F$ equation whose four component-equations are the four Maxwell laws. Even in this simplest setting the two equations are not symmetric: the first holds for structural reasons, the second is the equation of motion.

---

# Relate to Other Fields / Compression

**True name.** Operationally, the definition says: *a field strength is a closed $2$-form, and the physical ones are those whose Hodge dual is closed up to the source.* The homogeneous equation is the statement that $F$ lives in a de Rham cohomology class (it is closed, [[Def - de Rham Cohomology]]), and the inhomogeneous equation is the statement that $\star F$ is closed away from sources. Everything else — the electric and magnetic fields, the potentials, the four classical laws — is a coordinate presentation of these two closedness conditions. In one sentence: **electromagnetism is the theory of a closed $2$-form whose Hodge dual is closed off the sources.**

This compresses a great deal. The homogeneous equation $dF=0$ tells us that $F$ defines a class $[F]\in H^2_{\mathrm{dR}}(M;\mathbb R)$; when the bundle is nontrivial this class is (a real multiple of) the first Chern class of the associated line bundle ([[Thm - First Chern Class of a Line Bundle from Curvature]]), so the integral $\int_S F$ over a closed surface $S$ is quantised and topological, independent of the physical details of the field. This is the reason magnetic charge, were it to exist, would be quantised: a magnetic monopole is exactly a $U(1)$-bundle with nonzero Chern class, and the flux $\int_{S^2}F$ then measures the degree of the bundle (the subject of the Dirac-monopole exercise in this section). The inhomogeneous equation, by contrast, is metric-dependent through $\star$, and this dependence is the entry point for coupling electromagnetism to gravity and for the conformal-invariance phenomena of §7.3.

**Connection to Hodge theory and wave equations.** On a compact Riemannian manifold the operator $\delta=\pm\star d\star$ is the codifferential ([[Def - The Codifferential]], [[Thm - Codifferential is the Adjoint of d]] in the vault's Riemannian convention), and a form is harmonic when it is both closed and co-closed. In the source-free Lorentzian case ($J=0$) the two Maxwell equations say precisely that $F$ is both $d$-closed and $\star d\star$-closed, i.e. that $F$ is a "harmonic" $2$-form for the Lorentzian d'Alembertian rather than the Riemannian Laplacian; writing $F=dA$ in a gauge with $d\star A=0$ (the Lorenz gauge, [[Def - Gauge Choice and the Lorenz Gauge]]) turns $d\star F=0$ into the wave equation $\Box A=0$, which is why electromagnetic waves travel at the speed of light. The Riemannian Hodge decomposition and the Lorentzian wave picture are two specialisations of the same pair of equations.

**Connection to general relativity.** The stress content of the field, the energy-momentum tensor $T$ built from $F$, is divergence-free precisely when the inhomogeneous equation holds in vacuum; this is the electromagnetic half of the source of Einstein's equations and is developed on the [[Def - Einstein Tensor|Einstein]]–Maxwell pages. The homogeneous equation has no gravitational analogue — there is no "Bianchi identity for the source" — which is one way to see that electromagnetism, unlike gravity, has a genuine external source term.

---

# Examples / Corollaries

**Is an instance — the vacuum on Minkowski space.** Take $M=\mathbb R^{1,3}$ and set the source to zero, $J=0$. Then Maxwell's equations become
$$dF=0,\qquad d\star F=0,$$
the source-free system. This is the arena of light: any $F$ with $\vec E=E_0\cos(kz-t)\,\hat x$, $\vec B=E_0\cos(kz-t)\,\hat y$ (a plane wave travelling in the $z$-direction) satisfies both, as one checks by the coordinate computation on [[Thm - Maxwell Equations in Coordinates]] and drills on [[Ex - Maxwell's Equations on Minkowski Space from the Two Form Equations]]. The verification here is only that the *statement of the laws* degenerates correctly: with $J=0$ the second boxed equation loses its inhomogeneity and the pair is the closed/co-closed system, so a source-free electromagnetic field is exactly a $2$-form that is both $d$-closed and $\star d\star$-closed.

**Is an instance — the Coulomb field, off the origin, satisfies $d\star F=0$.** Consider on $M=\mathbb R\times(\mathbb R^3\setminus\{0\})$ the static electric field of a point charge $q$ at the origin,
$$\vec E(\vec x)=q\,\frac{\vec x}{|\vec x|^3},\qquad \vec B=0,\qquad \partial_t\vec E=0,$$
where $\vec x=(x,y,z)$ and $|\vec x|=r=\sqrt{x^2+y^2+z^2}$. We verify, clause by clause, that both Maxwell equations hold with $J=0$ on the region $r>0$.

*Homogeneous equation.* The field strength $2$-form is
$$F = E_x\,dx\wedge dt + E_y\,dy\wedge dt + E_z\,dz\wedge dt \qquad(\text{since }\vec B=0).$$
Its exterior derivative is
$$dF = \sum_{i}\Big(\partial_{x^i}E_x\,dx^i\wedge dx\wedge dt + \partial_{x^i}E_y\,dx^i\wedge dy\wedge dt + \partial_{x^i}E_z\,dx^i\wedge dz\wedge dt\Big)\qquad(\text{the }\partial_t E_i\text{ terms vanish, } \vec E \text{ static}).$$
Collecting the purely spatial $3$-form part gives the coefficient $\partial_y E_z-\partial_z E_y$ on $dt\wedge dy\wedge dz$ and its cyclic partners — that is, $\operatorname{rot}\vec E$ — while the $dx\wedge dy\wedge dz$ coefficient is absent because $\vec B=0$ makes $\operatorname{div}\vec B=0$ automatically. Now $\vec E=q\,\vec x/r^3=-\nabla\phi$ with $\phi=q/r$, and the curl of a gradient vanishes ($\operatorname{rot}\nabla\phi=0$, since mixed partials commute), so $\operatorname{rot}\vec E=0$. Hence $dF=0$: Gauss's law for magnetism and Faraday's law both hold, the latter because a static curl-free field induces nothing. (This also follows with no computation from the Bianchi identity, since $F$ is a curvature; the point of the computation is to see it explicitly.)

*Inhomogeneous equation.* Apply the Hodge star using the Minkowski table of the Notation section. With $\vec B=0$,
$$\star F = -E_x\,dy\wedge dz - E_y\,dz\wedge dx - E_z\,dx\wedge dy\qquad(\text{star table: }\star(dx\wedge dt)=-\star(dt\wedge dx)=-dy\wedge dz,\text{ etc.}).$$
Differentiating, and again dropping the $\partial_t$ terms because the field is static,
$$d\star F = -\big(\partial_x E_x\big)\,dx\wedge dy\wedge dz - \big(\partial_y E_y\big)\,dy\wedge dz\wedge dx - \big(\partial_z E_z\big)\,dz\wedge dx\wedge dy\qquad(\text{only the derivative along the missing coordinate survives each term}),$$
$$= -\big(\partial_x E_x+\partial_y E_y+\partial_z E_z\big)\,dx\wedge dy\wedge dz \qquad(\text{since } dy\wedge dz\wedge dx = dz\wedge dx\wedge dy = dx\wedge dy\wedge dz)$$
$$= -\operatorname{div}\vec E\;\,dx\wedge dy\wedge dz.$$
It remains to compute $\operatorname{div}\vec E$ for $r>0$. Writing $E_i=q\,x_i/r^3$,
$$\partial_{x_i}\!\left(\frac{x_i}{r^3}\right) = \frac{1}{r^3} - \frac{3x_i^2}{r^5}\qquad(\text{quotient rule, } \partial_{x_i}r = x_i/r),$$
$$\operatorname{div}\vec E = q\sum_{i=1}^3\left(\frac{1}{r^3}-\frac{3x_i^2}{r^5}\right) = q\left(\frac{3}{r^3}-\frac{3(x^2+y^2+z^2)}{r^5}\right) = q\left(\frac{3}{r^3}-\frac{3r^2}{r^5}\right) = 0\qquad(\text{since } x^2+y^2+z^2=r^2).$$
Therefore $d\star F=0$ on $r>0$, and Maxwell's inhomogeneous equation $d\star F+J=0$ holds there with $J=0$: away from the point charge the Coulomb field is source-free. The charge itself sits at the origin, which has been removed from $M$; in the distributional sense one recovers $\operatorname{div}\vec E=4\pi q\,\delta_0$, so that $J=4\pi q\,\delta_0\,dx\wedge dy\wedge dz$ is a point source, consistent with Coulomb's law $\operatorname{div}\vec E=\varrho$. On the smooth manifold $r>0$, however, every clause of both equations is satisfied with vanishing source, as required.

**Is NOT an instance — a field with $\operatorname{div}\vec B\ne0$.** No field strength arising from a $U(1)$-connection can have $\operatorname{div}\vec B\ne0$ at any point, so a putative "field" with a magnetic monopole density is not the curvature of any connection and hence cannot satisfy the homogeneous Maxwell equation. We verify the obstruction directly. Suppose $F$ came from a connection $\omega$; then $F=\bar\Omega/i$ with $\bar\Omega$ the descended curvature, and the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] forces $dF=0$ (restated above: for abelian $G$ the bracket term drops and $d\bar\Omega=0$). Decomposing $dF$ in coordinates, the coefficient of $dx\wedge dy\wedge dz$ is exactly $\partial_x B_x+\partial_y B_y+\partial_z B_z=\operatorname{div}\vec B$ (this is the $3$-form part computed on [[Thm - Maxwell Equations in Coordinates]]). Since $dF=0$, this coefficient vanishes identically, so $\operatorname{div}\vec B=0$ everywhere. A prescribed field with $\operatorname{div}\vec B\ne0$ at some point therefore has $dF\ne0$ there, contradicts the Bianchi identity, and is not a curvature. This is the differential-geometric statement of the experimental absence of magnetic monopoles: the homogeneous Maxwell equation is not a contingent law but a consequence of $F$ being a curvature, and it forbids point sources of magnetic flux on any single trivialised patch. (The subtle case — a genuinely nontrivial bundle, where $F$ is closed but not exact and $\int_{S^2}F\ne0$ — is a *quantised* flux through a surface, not a nonzero $\operatorname{div}\vec B$ at a point, and is exactly the Dirac monopole of [[Ex - The Dirac Monopole as a Nontrivial U(1) Bundle]]; there $\operatorname{div}\vec B=0$ still holds pointwise on every patch.)

**Corollary — conservation of charge.** From the definition alone one reads off that the source $3$-form must be closed. Applying $d$ to the inhomogeneous equation and using $d^2=0$ ([[Thm - d-Squared-is-Zero]]),
$$0 = d\big(d\star F + J\big) = d\,d\star F + dJ = dJ\qquad(\text{since } d\,d\star F = d^2(\star F)=0).$$
Thus $dJ=0$: any electromagnetic field with a source obeying Maxwell's equations has a *conserved* source. In coordinates $dJ=(\partial_t\varrho+\operatorname{div}\vec j)\,dt\wedge dx\wedge dy\wedge dz$, so this is the continuity equation $\partial_t\varrho+\operatorname{div}\vec j=0$; the full statement, with the integral form of charge conservation, is proved on [[Thm - Continuity Equation and Conservation of Charge]]. The mechanism is that $J$ is exact up to sign ($J=-d\star F$ on shell), and an exact form is closed.

**Calibration check.** Three quick verifications the reader can carry out from this page. First, confirm that $dF=0$ really is automatic for the vacuum plane wave: since that $F$ is closed it defines a de Rham class, and on contractible Minkowski space every closed form is exact, so $F=dA$ and $dF=d^2A=0$; no computation with $\vec E$, $\vec B$ is needed for the homogeneous half. Second, check the sign of the double star used above: from the Minkowski table, $\star\star(dt\wedge dx)=\star(dy\wedge dz)=-dt\wedge dx$, so $\star\star=-1$ on $2$-forms, in agreement with $\star\star=(-1)^{k(n-k)+p}=(-1)^{4+1}=-1$ for $k=2$, $n=4$, $p=1$. Third, verify that the non-example is genuinely about $\operatorname{div}\vec B$ and not $\operatorname{div}\vec E$: the coefficient of $dx\wedge dy\wedge dz$ in $dF$ is $\operatorname{div}\vec B$ (from the $\vec B$-part of $F$, whose exterior derivative produces the spatial $3$-form), whereas $\operatorname{div}\vec E$ appears only after applying $\star$, in $d\star F$; so it is exactly the *homogeneous* equation, the one that is an identity, that forbids magnetic monopoles.

---

# Unlocked by This

> [!tip] Maxwell's equations in coordinates *(from this topic, §7.2)*
> The two boxed equations become the four classical laws once written in a frame; the computation, coefficient by coefficient, is [[Thm - Maxwell Equations in Coordinates]]. That page also fixes the star of $F$ (correcting Bär's $-B_z\,dz\wedge dt$ sign typo to $+B_z\,dz\wedge dt$).

> [!tip] The variational origin of the inhomogeneous law *(from this topic, §7.2)*
> The equation $d\star F+J=0$ is not postulated but derived: it is the Euler–Lagrange equation of the action $\tfrac12\int F\wedge\star F+\int A\wedge J$, proved on [[Thm - Euler-Lagrange Equation of the Electromagnetic Action]]. This is the entry point to the whole variational treatment of gauge fields.

> [!tip] Conservation of charge *(from this topic, §7.2)*
> The closedness $dJ=0$ extracted above becomes the continuity equation and, integrated, the conservation of total charge on [[Thm - Continuity Equation and Conservation of Charge]].

> [!tip] Yang–Mills equations *(from §7.4)*
> Replacing the abelian $U(1)$ by a nonabelian structure group and $d$ by the exterior covariant derivative $d^A$ turns the inhomogeneous Maxwell equation into the **Yang–Mills equation** $d^A\star F_A=0$, whose self-dual solutions are instantons. Maxwell's inhomogeneous law is the abelian, source-free shadow of Yang–Mills; the homogeneous law becomes the Bianchi identity $d^A F_A=0$.

> [!tip] Magnetic charge quantisation and the Dirac monopole *(from §7.2, Chern–Weil)*
> Because $F$ is closed, $\int_{S}F$ over a closed surface is a topological invariant of the underlying $U(1)$-bundle, a multiple of $2\pi$; a nonzero value is a **magnetic monopole**, realised as a nontrivial bundle. This is developed in [[Ex - The Dirac Monopole as a Nontrivial U(1) Bundle]] using [[Thm - First Chern Class of a Line Bundle from Curvature]].
