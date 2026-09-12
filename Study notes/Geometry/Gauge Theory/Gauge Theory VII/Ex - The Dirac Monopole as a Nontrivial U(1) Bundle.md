---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
  - "Def - The Hopf Bundle"
  - "Thm - First Chern Class of a Line Bundle from Curvature"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, gauge-theory]
---

# Problem Statement

Work on the punctured space $M = \mathbb{R}^3 \setminus \{0\}$, thought of as the region outside a magnetic point source sitting at the origin. Fix a real constant $g \in \mathbb{R}$, the *magnetic charge*, and consider the static electromagnetic field with vanishing electric field and radial magnetic field
$$\vec{E} = 0, \qquad \vec{B}(\vec{x}) = g\,\frac{\vec{x}}{|\vec{x}|^{3}}, \qquad \vec{x} \in \mathbb{R}^3 \setminus \{0\}.$$
Following the standing conventions of [[Def - U(1) Gauge Field and Electromagnetic Connection|the U(1) gauge field]], encode this magnetic field as a real $2$-form on $M$,
$$F \;=\; B_x\, dy \wedge dz + B_y\, dz \wedge dx + B_z\, dx \wedge dy \;=\; \frac{g}{|\vec{x}|^{3}}\big( x\, dy \wedge dz + y\, dz \wedge dx + z\, dx \wedge dy \big).$$

Prove the following four assertions, which together are the geometric content of **Dirac's monopole**.

1. **The field is closed but not exact.** Show $dF = 0$ on all of $M$, yet $F$ is not the exterior derivative of any smooth $1$-form on $M$. The obstruction is the flux
$$\int_{S^2} F = 4\pi g \neq 0 \qquad (\text{when } g \neq 0),$$
computed over any sphere $S^2 = \{|\vec{x}| = R\}$ centred at the origin, and the impossibility follows from [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] applied to the closed surface $S^2$.

2. **Local potentials exist on each hemisphere.** Construct smooth $1$-forms $A_N$ on the region $U_N = S^2 \setminus \{\text{south pole}\}$ and $A_S$ on $U_S = S^2 \setminus \{\text{north pole}\}$ with $dA_N = dA_S = F$. There is no single potential valid on the whole of $M$ (that is assertion 1); the price of retaining a potential is that it must be given patch by patch.

3. **The transition function is $e^{2ig\varphi}$.** On the overlap $U_N \cap U_S$ (the sphere minus its two poles, coordinatised by the azimuthal angle $\varphi$), show that the two local potentials differ by $A_N - A_S = 2g\, d\varphi$, and deduce that the two local trivialisations of the underlying principal $U(1)$-bundle are glued by the transition function $e^{2ig\varphi}$.

4. **Dirac quantisation.** Show that the requirement that $e^{2ig\varphi}$ be a single-valued $U(1)$-valued function on the overlap — the [[Def - Transition Functions and the Cocycle Condition|cocycle condition]] — forces
$$2g \in \mathbb{Z}.$$
Conclude that the bundle carrying this monopole is the $2g$-th tensor power of [[Def - The Hopf Bundle|the Hopf bundle]] over $S^2$, and that its first Chern number equals the integer $-2g$, in agreement with the integrality supplied by [[Thm - First Chern Class of a Line Bundle from Curvature|the first Chern class from curvature]].

**Recall:**

The objects in play are a $U(1)$ gauge field, its curvature as a global $2$-form, the Hopf bundle as the generator of the isomorphism classes of $U(1)$-bundles over $S^2$, the first Chern class computed from curvature, and Stokes's theorem on a closed surface.

![[Def - U(1) Gauge Field and Electromagnetic Connection#The Definition]]

The single feature we use is that for the abelian group $U(1)$ the adjoint representation is trivial, so the local curvature form $s^*\Omega$ does not depend on the local section $s$ and assembles into a global curvature $\bar{\Omega} \in \Omega^2(M; i\mathbb{R})$; writing $\bar{\Omega} = iF$ defines the real field strength $F \in \Omega^2(M; \mathbb{R})$, and the Bianchi identity gives $dF = 0$. In a local trivialisation with section $s$ the connection is $s^*\omega = iA_{\mathrm{loc}}$ for a real $1$-form $A_{\mathrm{loc}}$, the *gauge potential*, and there $F = dA_{\mathrm{loc}}$. Under a change of local section $s' = s \cdot h$ with $h : U \to U(1)$, and because $\operatorname{Ad}$ is trivial for $U(1)$, the local connection forms are related by $s'^{*}\omega = s^{*}\omega + h^{-1}\, dh$; writing $h = e^{i\lambda}$ gives $h^{-1} dh = i\, d\lambda$, so $A'_{\mathrm{loc}} = A_{\mathrm{loc}} + d\lambda$.

![[Def - The Hopf Bundle#The Definition]]

The face of the Hopf bundle this problem uses is that it is a principal $U(1)$-bundle over $S^2$ whose class **generates** the group of isomorphism classes of principal $U(1)$-bundles over $S^2$: relative to the standard two-set cover of $S^2$ by the complements of the two poles, the Hopf bundle is glued across the equatorial overlap by a transition function of winding number one, namely $e^{i\varphi}$ (up to the orientation convention fixed on that page's sign ledger). Tensor powers of line bundles add winding numbers, so the $n$-th tensor power of the Hopf bundle is glued by $e^{in\varphi}$.

![[Thm - First Chern Class of a Line Bundle from Curvature#Statement]]

![[Thm - Stokes' Theorem on Manifolds#Statement]]

The face of Stokes we use is the closed-manifold corollary: on a compact oriented boundaryless manifold $M$ (here the sphere $S^2$, whose boundary is empty), $\int_M d\alpha = 0$ for every smooth form $\alpha$ of the top degree minus one. A form whose integral over $S^2$ is non-zero therefore cannot be exact on any neighbourhood of $S^2$.

> [!warning] Convention: signs of the transition function and the Chern number
> The magnitude of the winding number of the transition function, and hence the quantisation $2g \in \mathbb{Z}$, is convention-independent. Its **sign**, and equivalently whether the monopole bundle is the $+2g$-th or the $-2g$-th power of the Hopf bundle, depends on two choices fixed elsewhere in the series: which local section is called $s_N$ versus $s_S$ (this flips $g_{NS} \leftrightarrow g_{NS}^{-1}$), and which winding number is assigned to the Hopf generator on the sign ledger of [[Def - The Hopf Bundle]]. Throughout we label the sections so that the northern-to-southern transition function reads $e^{2ig\varphi}$, as in the problem statement, and we defer the overall sign of the Chern number to that ledger. We use the Chern normalisation $c_1(L) = \big[\tfrac{i}{2\pi}\bar{\Omega}\big]$ of the series conventions.

---

# Convergent Strategy

**Problem class.** This is a *detect and quantise a topological obstruction* problem: we are handed a locally consistent field (a closed $2$-form) and must decide whether it comes from a globally defined potential, and if not, extract the integer that measures the failure. The diagnostic is always the same — a closed form is exact on a region if and only if all its periods, the integrals over the closed submanifolds generating the homology of the region, vanish. Here $M = \mathbb{R}^3 \setminus \{0\}$ deformation-retracts onto the sphere $S^2$, whose second de Rham cohomology is one-dimensional and detected by integration over $S^2$ itself, so the single period $\int_{S^2} F$ decides everything. The problem then upgrades this de Rham statement into a statement about a principal $U(1)$-bundle: the non-vanishing period is exactly the obstruction to trivialising the bundle, and its integrality is Dirac's charge quantisation.

**Assumption pattern.** The hypotheses are a punctured domain and a specific radial field. The punctured domain is what makes the problem non-trivial: on a contractible region [[Thm - The Poincaré Lemma on a Star-Shaped Region|the Poincaré lemma]] would give a global potential immediately, and there would be no monopole. The radial inverse-square form of $\vec{B}$ is what makes the field closed away from the origin (its divergence vanishes there) while depositing all of its flux — the entire source — at the excised point. The assumption pattern to recognise is *"closed form on a region with a hole, source hidden in the hole"*: the hole carries a period, and the period is the physics.

**Theorem routing.** The route runs through four results. First, [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] on the closed surface $S^2$ converts "$F$ is exact" into "$\int_{S^2} F = 0$", so computing the flux both proves non-exactness and produces the number $4\pi g$. Second, [[Def - U(1) Gauge Field and Electromagnetic Connection|the U(1) gauge field]] supplies the transformation law $A'_{\mathrm{loc}} = A_{\mathrm{loc}} + d\lambda$ that turns the difference of two local potentials into a transition function. Third, [[Def - Transition Functions and the Cocycle Condition|the cocycle condition]] and [[Thm - Principal Bundles are Classified by Cocycles|the classification of bundles by cocycles]] make single-valuedness of the transition function the exact requirement, giving $2g \in \mathbb{Z}$; and [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the classification of U(1)-bundles]] reads the winding number $2g$ as the isomorphism class, identifying the bundle as a power of [[Def - The Hopf Bundle|the Hopf bundle]]. Fourth, [[Thm - First Chern Class of a Line Bundle from Curvature|the first Chern class from curvature]] recovers the same integer as $\tfrac{i}{2\pi}$ times the integral of the curvature, a second, independent derivation of quantisation.

**Key decision point.** The one move that unlocks the whole exercise is to *stop looking for a global potential and build two local ones on overlapping patches*. Once one accepts that no single $A$ exists (assertion 1), the natural object is a pair $(A_N, A_S)$ agreeing up to a gauge transformation on the overlap. Their difference $A_N - A_S = 2g\, d\varphi$ is not itself exact on the overlap — $\varphi$ is not a single-valued function on the punctured sphere — and it is precisely this failure of $\varphi$ to be single-valued that, exponentiated, produces a non-trivial transition function and forces $2g$ to be an integer. Recognising that "the gauge transformation relating two patches is the transition function of a bundle" is the conceptual pivot from differential forms to bundle topology.

---

# Legal Operations Used

The topic page for §7.2 collects the legal operations of $U(1)$ gauge theory; this solution deploys the following, named descriptively here and to be reconciled with the topic page's numbering once it is written.

1. **Encode a magnetic field as a $2$-form via the Frankel dictionary.** A vector field $\vec{B} = (B_x, B_y, B_z)$ on a region of $\mathbb{R}^3$ is turned into the $2$-form $F = B_x\, dy \wedge dz + B_y\, dz \wedge dx + B_z\, dx \wedge dy$, so that $dF = (\operatorname{div}\vec{B})\, dx \wedge dy \wedge dz$ and the flux $\int_\Sigma F$ of the form over a surface equals the flux $\int_\Sigma \vec{B} \cdot d\vec{S}$ of the field. The trigger is any static magnetic configuration; the pattern is to move to forms so that divergence becomes $d$ and flux becomes integration.

2. **Test exactness by integrating over a generating cycle (the period test).** To decide whether a closed form $F$ is exact on a region, integrate it over the closed submanifolds that generate the region's homology; a single non-zero period certifies non-exactness. The trigger is a closed form on a non-contractible region; the pattern is to identify the generating cycle (here $S^2$) and compute one integral, using [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] to know that exact forms have vanishing periods.

3. **The two-patch (Wu–Yang) construction of a connection.** When no global potential exists, cover the base by patches on each of which a potential does exist, and record the gauge transformations relating them on the overlaps. The trigger is a non-exact but locally exact curvature; the pattern is to solve $dA = F$ separately on contractible patches and glue.

4. **Extract a transition function from two local gauge potentials.** Given local potentials $A_N, A_S$ with $A_N - A_S = d\lambda$ on the overlap, the transition function of the bundle is $e^{i\lambda}$, using the abelian transformation law $A'_{\mathrm{loc}} = A_{\mathrm{loc}} + d\lambda$ from [[Def - U(1) Gauge Field and Electromagnetic Connection|the U(1) gauge field]]. The trigger is a pair of patchwise potentials; the pattern is to write their difference as $d\lambda$ and exponentiate.

5. **Impose the cocycle condition to quantise.** A candidate transition function must be a genuine single-valued map into $U(1)$ on each overlap; imposing this on $e^{2ig\varphi}$, where $\varphi$ increases by $2\pi$ around the equator, forces $2g \in \mathbb{Z}$. The trigger is a transition function built from a multivalued angle; the pattern is to demand periodicity under $\varphi \mapsto \varphi + 2\pi$.

---

# Hints

> [!note]- Hint 1
> Do not try to build the potential first. Ask instead whether a global potential can exist at all. A closed $2$-form on a surface without boundary integrates to zero if it is exact — this is the closed-manifold corollary of Stokes's theorem. So compute one number, the flux of $F$ through a sphere about the origin, and see whether it is zero. Spherical coordinates make the field $2$-form very simple.

> [!note]- Hint 2
> To turn the Cartesian expression for $F$ into spherical coordinates, recognise it as an interior product: $x\, dy \wedge dz + y\, dz \wedge dx + z\, dx \wedge dy = i_{\vec{r}}(dx \wedge dy \wedge dz)$, where $\vec{r} = x\partial_x + y\partial_y + z\partial_z = r\partial_r$ is the radial vector field, and $dx \wedge dy \wedge dz = r^2 \sin\theta\, dr \wedge d\theta \wedge d\varphi$. Contracting gives $F = g\sin\theta\, d\theta \wedge d\varphi$, from which both $dF = 0$ and the flux are one-line computations.

> [!note]- Hint 3
> For the potentials, guess $A = c(\theta)\, d\varphi$ and solve $dA = F$; you need $c'(\theta) = g\sin\theta$, so $c(\theta) = -g\cos\theta + \text{const}$. The constant is not cosmetic: choose it so the form is *smooth at a pole*. Near the north pole $d\varphi$ blows up, and only the combination $(1 - \cos\theta)\, d\varphi$ (which vanishes to second order there) stays smooth; near the south pole it is $(1 + \cos\theta)\, d\varphi$. This fixes $A_N = g(1-\cos\theta)\, d\varphi$ and $A_S = -g(1+\cos\theta)\, d\varphi$.

> [!note]- Hint 4
> Subtract the two potentials on the overlap: $A_N - A_S = 2g\, d\varphi$. By the abelian transformation law $A_N = A_S + d\lambda$ with $\lambda = 2g\varphi$, so the transition function is $e^{i\lambda} = e^{2ig\varphi}$. Now $\varphi$ and $\varphi + 2\pi$ label the same point of the sphere; for $e^{2ig\varphi}$ to be a well-defined function there, its value must not jump as $\varphi$ advances by $2\pi$. Write that condition out.

---

# Solution

The plan is to first prove non-exactness by a flux computation, so that the necessity of two patches is forced rather than assumed; then to write down the two hemispheric potentials and verify each yields $F$; then to compute their overlap difference and exponentiate it into a transition function; and finally to impose single-valuedness of that transition function, which quantises $2g$ and identifies the bundle. Throughout we use spherical coordinates $(r, \theta, \varphi)$ with $x = r\sin\theta\cos\varphi$, $y = r\sin\theta\sin\varphi$, $z = r\cos\theta$, where $r > 0$, $\theta \in [0, \pi]$ is the polar angle measured from the positive $z$-axis, and $\varphi \in \mathbb{R}/2\pi\mathbb{Z}$ is the azimuthal angle; the poles are $\theta = 0$ (north) and $\theta = \pi$ (south).

**Step 1: The field strength is $F = g\sin\theta\, d\theta \wedge d\varphi$, so $dF = 0$.**

We rewrite the Cartesian $2$-form in spherical coordinates using the [[Def - Interior Product (Contraction with a Vector Field)|interior product]], and then differentiate.

> [!note]- Derivation
> Let $\vec{r} = x\partial_x + y\partial_y + z\partial_z$ be the radial (Euler) vector field; in spherical coordinates $\vec{r} = r\partial_r$, because the flow of $r\partial_r$ is the radial scaling that generates $\vec{r}$. The Cartesian numerator of $F$ is the contraction of the Euclidean volume form along $\vec{r}$:
> $$i_{\vec{r}}(dx \wedge dy \wedge dz) = x\, i_{\partial_x}(dx \wedge dy \wedge dz) + y\, i_{\partial_y}(dx \wedge dy \wedge dz) + z\, i_{\partial_z}(dx \wedge dy \wedge dz) \qquad (\text{linearity of the interior product in the vector slot})$$
> $$= x\, dy \wedge dz + y\, dz \wedge dx + z\, dx \wedge dy \qquad (i_{\partial_x}(dx \wedge dy \wedge dz) = dy \wedge dz,\ i_{\partial_y}(\cdots) = -dx \wedge dz = dz \wedge dx,\ i_{\partial_z}(\cdots) = dx \wedge dy).$$
> Therefore, with $F = \dfrac{g}{r^3}\, i_{\vec{r}}(dx \wedge dy \wedge dz)$ and the standard volume form $dx \wedge dy \wedge dz = r^2 \sin\theta\, dr \wedge d\theta \wedge d\varphi$,
> $$F = \frac{g}{r^3}\, i_{r\partial_r}\big(r^2 \sin\theta\, dr \wedge d\theta \wedge d\varphi\big) = \frac{g}{r^3}\cdot r \cdot r^2 \sin\theta\; i_{\partial_r}\big(dr \wedge d\theta \wedge d\varphi\big) \qquad (\vec{r} = r\partial_r;\ \text{scalars pull out of the contraction})$$
> $$= g\sin\theta\; d\theta \wedge d\varphi \qquad (i_{\partial_r}\, dr = 1,\ i_{\partial_r}\, d\theta = i_{\partial_r}\, d\varphi = 0,\ \text{so } i_{\partial_r}(dr \wedge d\theta \wedge d\varphi) = d\theta \wedge d\varphi).$$
> This is $g$ times the standard solid-angle form; in particular it is independent of $r$. Differentiating,
> $$dF = g\, d(\sin\theta\, d\theta \wedge d\varphi) = g\Big( d(\sin\theta) \wedge d\theta \wedge d\varphi + \sin\theta\, d(d\theta \wedge d\varphi) \Big) \qquad (\text{Leibniz rule for the exterior derivative on a wedge product})$$
> $$= g\Big( \cos\theta\, d\theta \wedge d\theta \wedge d\varphi + 0 \Big) = 0 \qquad (d(\sin\theta) = \cos\theta\, d\theta;\ d\theta \wedge d\theta = 0;\ d(d\theta \wedge d\varphi) = 0 \text{ since } d^2 = 0).$$
> The same conclusion reads, in the vector-calculus dictionary, $dF = (\operatorname{div}\vec{B})\, dx \wedge dy \wedge dz = 0$ because $\operatorname{div}(g\vec{x}/|\vec{x}|^3) = 0$ for $\vec{x} \neq 0$. Thus $F$ is closed on all of $M = \mathbb{R}^3 \setminus \{0\}$.

**Step 2: The flux is $\int_{S^2} F = 4\pi g$, so $F$ is not exact.**

We integrate the field $2$-form over a sphere about the origin and invoke the closed-manifold corollary of Stokes's theorem to rule out any global potential.

> [!note]- Derivation
> Let $S^2 = \{|\vec{x}| = R\}$ for any $R > 0$, oriented as the boundary of the ball (outward normal), so that $(\theta, \varphi)$ with $d\theta \wedge d\varphi$ is a positively oriented chart away from the poles. Restricting $F = g\sin\theta\, d\theta \wedge d\varphi$ to $S^2$ (the $r$-dependence has already dropped out) and integrating,
> $$\int_{S^2} F = \int_{0}^{2\pi}\!\!\int_{0}^{\pi} g\sin\theta \; d\theta\, d\varphi = g\left(\int_0^{2\pi} d\varphi\right)\left(\int_0^\pi \sin\theta\, d\theta\right) \qquad (\text{Fubini; the integrand is a product})$$
> $$= g \cdot 2\pi \cdot \big[-\cos\theta\big]_{0}^{\pi} = g \cdot 2\pi \cdot \big((-\cos\pi) - (-\cos 0)\big) = g \cdot 2\pi \cdot (1 + 1) = 4\pi g \qquad (\text{fundamental theorem of calculus}).$$
> Suppose, for contradiction, that $F = d\alpha$ for some $\alpha \in \Omega^1(M)$. The sphere $S^2 \subset M$ is a compact oriented smooth surface **without boundary**. By the closed-manifold corollary of [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] — for a compact oriented boundaryless $n$-manifold, $\int_M d\omega = 0$ for every smooth $(n-1)$-form $\omega$ — we would have
> $$\int_{S^2} F = \int_{S^2} d\alpha = \int_{S^2} d\big(\alpha|_{S^2}\big) = 0 \qquad (\text{Stokes on the closed surface } S^2;\ \text{pullback commutes with } d).$$
> This contradicts $\int_{S^2} F = 4\pi g \neq 0$ (using $g \neq 0$). Therefore **no global potential $\alpha$ exists on $M$**; equivalently $[F] \neq 0$ in $H^2_{\mathrm{dR}}(M)$, consistent with $M = \mathbb{R}^3 \setminus \{0\}$ retracting onto $S^2$ and $H^2_{\mathrm{dR}}(S^2) \cong \mathbb{R}$.

**Step 3: Hemispheric potentials $A_N = g(1-\cos\theta)\, d\varphi$ and $A_S = -g(1+\cos\theta)\, d\varphi$ satisfy $dA_N = dA_S = F$.**

Although no global potential exists, each hemisphere is contractible, so a potential exists there; we exhibit explicit ones and check smoothness at the pole each patch contains.

> [!note]- Derivation
> Put $U_N = S^2 \setminus \{\theta = \pi\}$ (the sphere minus the south pole) and $U_S = S^2 \setminus \{\theta = 0\}$ (minus the north pole), and correspondingly the punctured cones over them in $M$. Define
> $$A_N := g(1 - \cos\theta)\, d\varphi \quad \text{on } U_N, \qquad A_S := -g(1 + \cos\theta)\, d\varphi \quad \text{on } U_S.$$
> *Each is a potential for $F$.* Using $d(1 \mp \cos\theta) = \pm\sin\theta\, d\theta$ and $d(d\varphi) = 0$,
> $$dA_N = g\, d\big((1-\cos\theta)\, d\varphi\big) = g\, d(1-\cos\theta) \wedge d\varphi = g\sin\theta\, d\theta \wedge d\varphi = F \qquad (\text{Leibniz rule; } d(1-\cos\theta) = \sin\theta\, d\theta;\ \text{Step 1}),$$
> $$dA_S = -g\, d\big((1+\cos\theta)\, d\varphi\big) = -g\, d(1+\cos\theta) \wedge d\varphi = -g(-\sin\theta)\, d\theta \wedge d\varphi = g\sin\theta\, d\theta \wedge d\varphi = F \qquad (\text{same, with } d(1+\cos\theta) = -\sin\theta\, d\theta).$$
> *Smoothness at the enclosed pole.* The coordinate $1$-form $d\varphi$ is singular along the whole polar axis (where $\varphi$ is undefined), so we must check that the coefficients kill this singularity at the pole each patch keeps. Near the north pole introduce the Cartesian chart $(u, v)$ on the sphere with $u = \sin\theta\cos\varphi$, $v = \sin\theta\sin\varphi$, so that $\rho := \sqrt{u^2 + v^2} = \sin\theta$ is the distance from the axis and
> $$d\varphi = \frac{u\, dv - v\, du}{u^2 + v^2} = \frac{u\, dv - v\, du}{\rho^2} \qquad (\varphi = \operatorname{atan2}(v,u);\ \text{differentiate}).$$
> As $\theta \to 0$ we have $1 - \cos\theta = \tfrac{1}{2}\theta^2 + O(\theta^4)$ and $\rho = \sin\theta = \theta + O(\theta^3)$, so $1 - \cos\theta = \tfrac{1}{2}\rho^2 + O(\rho^4)$, and therefore
> $$A_N = g(1-\cos\theta)\, d\varphi = g\Big(\tfrac{1}{2}\rho^2 + O(\rho^4)\Big)\frac{u\, dv - v\, du}{\rho^2} = \tfrac{g}{2}(u\, dv - v\, du) + O(\rho^2)\,(u\,dv - v\,du) \qquad (\text{substitute both expansions}),$$
> which is a smooth $1$-form in the coordinates $(u,v)$ across $\rho = 0$ (the pole), since $u\, dv - v\, du$ and every $O(\rho^2)$ correction are smooth there. Hence $A_N$ is smooth on all of $U_N$, including the north pole, and singular only along the south-pole axis, which $U_N$ excludes. The identical computation at $\theta = \pi$, with $1 + \cos\theta = \tfrac{1}{2}(\pi-\theta)^2 + O((\pi-\theta)^4)$, shows $A_S$ is smooth on all of $U_S$, including the south pole, and singular only along the north-pole axis, which $U_S$ excludes. This is the Wu–Yang two-patch potential: the unavoidable singular "Dirac string" of each patch is pushed onto the pole the other patch covers.

**Step 4: On the overlap the potentials differ by $2g\, d\varphi$, giving transition function $e^{2ig\varphi}$.**

Subtracting the two local potentials on the overlap produces an exact-looking difference $d(2g\varphi)$, and the abelian transformation law turns this into the bundle's transition function.

> [!note]- Derivation
> The overlap is $U_N \cap U_S = S^2 \setminus \{\text{both poles}\}$, the open band on which both $A_N$ and $A_S$ are defined; it is parametrised by $\theta \in (0, \pi)$ and $\varphi \in \mathbb{R}/2\pi\mathbb{Z}$, and it deformation-retracts onto the equatorial circle $\{\theta = \pi/2\}$. There,
> $$A_N - A_S = g(1 - \cos\theta)\, d\varphi - \big(-g(1 + \cos\theta)\, d\varphi\big) = g\big[(1 - \cos\theta) + (1 + \cos\theta)\big]\, d\varphi = 2g\, d\varphi \qquad (\text{the } \pm\cos\theta \text{ terms cancel}).$$
> Now let $s_N, s_S$ be the local sections of the underlying principal $U(1)$-bundle whose pulled-back connection forms are $s_N^*\omega = iA_N$ and $s_S^*\omega = iA_S$, and let $g_{NS} : U_N \cap U_S \to U(1)$ be the transition function defined by $s_S = s_N \cdot g_{NS}$. By the abelian transformation law recalled above (valid because $\operatorname{Ad}$ is trivial for $U(1)$),
> $$iA_S = s_S^*\omega = s_N^*\omega + g_{NS}^{-1}\, dg_{NS} = iA_N + g_{NS}^{-1}\, dg_{NS} \qquad (\text{abelian transformation law of the U(1) gauge field},\ \operatorname{Ad}_{h^{-1}} = \mathrm{id}),$$
> so that
> $$g_{NS}^{-1}\, dg_{NS} = i(A_S - A_N) = -2ig\, d\varphi \qquad (\text{Step 4, first display}).$$
> Writing $g_{NS} = e^{i\lambda}$ with $\lambda$ a locally defined real function on the overlap gives $g_{NS}^{-1}\, dg_{NS} = i\, d\lambda$, hence $d\lambda = -2g\, d\varphi$ and $\lambda = -2g\varphi$ up to an additive constant, which we absorb, so
> $$g_{NS} = e^{-2ig\varphi}.$$
> The transition function relating the northern trivialisation to the southern one is the inverse $g_{SN} = g_{NS}^{-1} = e^{2ig\varphi}$, matching the form stated in the problem. In either direction the winding number of the transition function around the equatorial circle has magnitude $|2g|$; its sign is the convention fixed in the callout above.

**Step 5: Single-valuedness forces $2g \in \mathbb{Z}$; the bundle is the $2g$-th power of the Hopf bundle.**

The transition function is built from the multivalued angle $\varphi$; demanding that it nonetheless be a genuine function on the overlap is the cocycle condition, and it quantises $g$.

> [!note]- Derivation
> The overlap $U_N \cap U_S$ is a subset of the sphere, on which $\varphi$ and $\varphi + 2\pi$ denote the *same point*. For $g_{NS} = e^{-2ig\varphi}$ to be a well-defined map $U_N \cap U_S \to U(1)$ — a requirement of the [[Def - Transition Functions and the Cocycle Condition|cocycle condition]], which demands each transition function be a continuous $U(1)$-valued function on its overlap — its value must be unchanged when $\varphi$ is advanced by $2\pi$:
> $$e^{-2ig(\varphi + 2\pi)} = e^{-2ig\varphi} \quad\Longleftrightarrow\quad e^{-2ig\varphi}\, e^{-4\pi i g} = e^{-2ig\varphi} \quad\Longleftrightarrow\quad e^{-4\pi i g} = 1 \qquad (\text{cancel the nowhere-zero factor } e^{-2ig\varphi}).$$
> Now $e^{-4\pi i g} = 1$ if and only if $-4\pi g \in 2\pi\mathbb{Z}$, that is,
> $$4\pi g = 2\pi n \ \text{ for some } n \in \mathbb{Z} \quad\Longleftrightarrow\quad 2g = n \in \mathbb{Z}.$$
> This is **Dirac's quantisation condition** $2g \in \mathbb{Z}$: in units where the elementary electric charge is one, the magnetic charge $g$ is a half-integer. With $2g = n$, the transition function is $g_{SN} = e^{in\varphi}$, of winding number $n$. Since the Hopf bundle over $S^2$ is glued across the equator by the winding-one function $e^{i\varphi}$ and generates the isomorphism classes of principal $U(1)$-bundles over $S^2$, and since [[Thm - Principal Bundles are Classified by Cocycles|bundles over a two-set cover are classified by their single transition function up to the cocycle-preserving equivalence]], the monopole bundle is the $n = 2g$-th tensor power of [[Def - The Hopf Bundle|the Hopf bundle]]. By [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the classification of principal U(1)-bundles by the first Chern class]] this integer is a complete invariant of the bundle: the monopole of charge $g$ lives on the bundle of class $2g \in \mathbb{Z} \cong \operatorname{Pic}(S^2)$, and distinct half-integer charges give non-isomorphic bundles.

**Step 6 (independent check): the first Chern number equals $-2g$, re-deriving integrality.**

The curvature route to the same integer confirms the cocycle computation and ties the topological charge to Chern–Weil theory.

> [!note]- Derivation
> The curvature of the $U(1)$-connection is $\bar{\Omega} = iF$, an $i\mathbb{R}$-valued global $2$-form (Recall). By [[Thm - First Chern Class of a Line Bundle from Curvature|the first Chern class from curvature]] — for a Hermitian line bundle $L \to X$ with a unitary connection of curvature $\bar{\Omega}$, the first Chern class is $c_1(L) = \big[\tfrac{i}{2\pi}\bar{\Omega}\big] \in H^2_{\mathrm{dR}}(X)$, an integral class whose integral over any closed oriented surface is an integer — the first Chern number over $S^2$ is
> $$\int_{S^2} c_1(L) = \int_{S^2} \frac{i}{2\pi}\bar{\Omega} = \int_{S^2}\frac{i}{2\pi}(iF) = -\frac{1}{2\pi}\int_{S^2} F = -\frac{1}{2\pi}\cdot 4\pi g = -2g \qquad (\bar{\Omega} = iF,\ i \cdot i = -1;\ \text{Step 2}).$$
> The theorem asserts this number is an integer; hence $-2g \in \mathbb{Z}$, i.e. $2g \in \mathbb{Z}$, exactly the quantisation of Step 5, now obtained without ever writing a transition function. The two derivations agree: the winding number $n = 2g$ of the transition function is (up to the ledger sign) the first Chern number $-2g$ of the bundle, as it must be, since both compute the same isomorphism class in $\operatorname{Pic}(S^2) \cong \mathbb{Z}$.

> [!note]- Complete formal solution
> Let $M = \mathbb{R}^3 \setminus \{0\}$, let $g \in \mathbb{R}$, and let $F = \tfrac{g}{|\vec{x}|^3}(x\, dy \wedge dz + y\, dz \wedge dx + z\, dx \wedge dy)$ be the magnetic field $2$-form. Use spherical coordinates $(r, \theta, \varphi)$.
>
> **(1) $F$ is closed.** With $\vec{r} = x\partial_x + y\partial_y + z\partial_z = r\partial_r$ and $dx \wedge dy \wedge dz = r^2\sin\theta\, dr \wedge d\theta \wedge d\varphi$, the interior-product identity $x\, dy \wedge dz + y\, dz \wedge dx + z\, dx \wedge dy = i_{\vec{r}}(dx \wedge dy \wedge dz)$ gives $F = \tfrac{g}{r^3}\, i_{r\partial_r}(r^2\sin\theta\, dr \wedge d\theta \wedge d\varphi) = g\sin\theta\, d\theta \wedge d\varphi$. Then $dF = g\, d(\sin\theta) \wedge d\theta \wedge d\varphi = g\cos\theta\, d\theta \wedge d\theta \wedge d\varphi = 0$.
>
> **(2) $F$ is not exact.** Over $S^2 = \{|\vec{x}| = R\}$, $\int_{S^2} F = \int_0^{2\pi}\!\!\int_0^\pi g\sin\theta\, d\theta\, d\varphi = 2\pi g\,[-\cos\theta]_0^\pi = 4\pi g$. If $F = d\alpha$ globally, then by the closed-manifold corollary of Stokes's theorem $\int_{S^2} F = \int_{S^2} d(\alpha|_{S^2}) = 0$, contradicting $4\pi g \neq 0$. Hence no global potential exists and $[F] \neq 0$ in $H^2_{\mathrm{dR}}(M)$.
>
> **(3) Local potentials.** On $U_N = S^2 \setminus \{\text{S pole}\}$ set $A_N = g(1-\cos\theta)\, d\varphi$; on $U_S = S^2 \setminus \{\text{N pole}\}$ set $A_S = -g(1+\cos\theta)\, d\varphi$. Both satisfy $dA_N = dA_S = g\sin\theta\, d\theta \wedge d\varphi = F$, since $d(\mp\cos\theta) = \pm\sin\theta\, d\theta$. In the Cartesian pole chart $(u,v)$ with $\rho = \sin\theta$ and $d\varphi = (u\, dv - v\, du)/\rho^2$, the expansion $1 - \cos\theta = \tfrac12\rho^2 + O(\rho^4)$ shows $A_N = \tfrac{g}{2}(u\, dv - v\, du) + O(\rho^2)$ is smooth across the north pole; symmetrically $A_S$ is smooth across the south pole. Each is singular only on the axis the other patch covers.
>
> **(4) Transition function.** On $U_N \cap U_S$, $A_N - A_S = 2g\, d\varphi$. With local sections $s_N, s_S$ having $s_N^*\omega = iA_N$, $s_S^*\omega = iA_S$, and $s_S = s_N \cdot g_{NS}$, the abelian transformation law $s_S^*\omega = s_N^*\omega + g_{NS}^{-1}dg_{NS}$ gives $g_{NS}^{-1}dg_{NS} = i(A_S - A_N) = -2ig\, d\varphi$, hence $g_{NS} = e^{-2ig\varphi}$ and $g_{SN} = e^{2ig\varphi}$.
>
> **(5) Quantisation.** Single-valuedness of $g_{NS}$ on the overlap requires $e^{-2ig(\varphi + 2\pi)} = e^{-2ig\varphi}$, i.e. $e^{-4\pi i g} = 1$, i.e. $2g = n \in \mathbb{Z}$. The transition function $e^{in\varphi}$ has winding number $n$; the Hopf bundle is the winding-one generator of the $U(1)$-bundles over $S^2$, so the monopole bundle is its $n = 2g$-th tensor power, of first Chern number $-2g$ by $\int_{S^2} c_1(L) = \int_{S^2}\tfrac{i}{2\pi}(iF) = -\tfrac{1}{2\pi}\cdot 4\pi g = -2g$. Both routes give $2g \in \mathbb{Z}$. $\blacksquare$

> [!warning] Illegal but tempting: "$\mathbb{R}^3 \setminus \{0\}$ is simply connected, so $dF = 0$ implies $F = dA$."
> Simple connectedness is the vanishing of the *first* homotopy or de Rham group; it says every closed $1$-form is exact. The Poincaré lemma that upgrades "closed" to "exact" in *all* degrees requires the region to be contractible (star-shaped suffices), as in [[Thm - The Poincaré Lemma on a Star-Shaped Region]]. But $M = \mathbb{R}^3 \setminus \{0\}$ retracts onto $S^2$, which is simply connected yet has $H^2_{\mathrm{dR}}(S^2) \cong \mathbb{R} \neq 0$: closed $2$-forms need not be exact. The very computation $\int_{S^2} F = 4\pi g \neq 0$ exhibits a closed $2$-form that is not exact, so the tempting inference is false, and the obstruction it overlooks is precisely the monopole. The extra condition that would make the inference legal is *contractibility* of the domain, which the puncture destroys in degree two.

> [!note]- Independent sanity check (dimensional and limiting)
> Two independent checks. First, the trivial case $g = 0$: then $F = 0 = d(0)$ is exact, the transition function is the constant $1$, the bundle is trivial, and the Chern number is $0$ — all four assertions degenerate correctly. Second, the smallest non-trivial charge $2g = 1$, i.e. $g = 1/2$: the transition function is $e^{i\varphi}$, exactly the Hopf generator, and the bundle is the Hopf bundle itself with Chern number $-1$; this is the minimal Dirac monopole, and it should sit on the generating bundle, which it does. The flux $\int_{S^2} F = 4\pi g = 2\pi$ then equals $2\pi$ times the (magnitude of the) Chern number, as the normalisation $c_1 = [\tfrac{i}{2\pi}\bar\Omega]$ demands.

---

# Key Takeaways

**A closed form fails to be exact exactly when it has a non-zero period, and the period is computed by one integral over a generating cycle.** The engine of this whole problem is the pairing between closed forms and closed submanifolds furnished by Stokes's theorem: an exact form integrates to zero over any boundaryless submanifold, so a single non-zero integral certifies non-exactness with no further work. The reusable discipline is, when handed a closed field on a region with topology, to *find the generating cycles of the region and compute the periods* rather than hunting fruitlessly for a potential. Here the region $\mathbb{R}^3 \setminus \{0\}$ retracts onto $S^2$, whose second homology is generated by $[S^2]$ itself, so there is exactly one period to compute, $\int_{S^2} F = 4\pi g$, and it decides everything. The trigger condition is the phrase "closed but possibly not exact on a non-contractible region"; the transferable diagnostic is that the number of independent periods equals the rank of the relevant cohomology, and each non-zero period is an obstruction one can often read as a physical charge. The same reasoning recurs for the winding number of a phase around a vortex ($\oint d\varphi$ over $S^1$), for the circulation of an irrotational-but-not-conservative flow, and for the residue of a meromorphic differential.

**Topological charges become integers because they are winding numbers of gluing data, and quantisation is the demand that the gluing be consistent.** The pivot of the argument is that a globally obstructed potential can always be traded for a family of local potentials plus the gauge transformations relating them, and those gauge transformations are the transition functions of a bundle. The moment a transition function is built from a multivalued angle — here $e^{2ig\varphi}$ — its very existence as a single-valued map into $U(1)$ imposes an integrality condition, because $U(1)$ is a circle and a map from a circle to a circle has an integer winding number. This is why charge quantisation is unavoidable rather than imposed: it is the cocycle condition in disguise. The trigger to reach for this pattern is any situation where a locally-defined quantity (a phase, a potential, a frame) cannot be globalised; the move is to record the transition data and read off its winding, degree, or period. The identical mechanism quantises the vorticity of superfluid circulation, the flux through a superconducting ring, the degree of a map used in a clutching construction, and — one dimension up — the instanton number of an $SU(2)$-bundle, where the winding of the clutching function around $S^3$ replaces the winding around the equatorial $S^1$.

**Two derivations of the same integer, one combinatorial and one analytic, are a structural feature and a powerful check, not a coincidence.** The quantisation $2g \in \mathbb{Z}$ appeared first as the winding number of a transition function (Step 5) and again as the first Chern number $-2g$ computed by integrating the curvature (Step 6). That these agree is the content of Chern–Weil theory specialised to line bundles: the first Chern class computed analytically from any connection's curvature equals the topological class computed combinatorially from transition functions, so the flux $\tfrac{i}{2\pi}\int \bar\Omega$ is forced to be an integer even though the curvature is a smooth, continuously varying object. The reusable lesson is to *always seek the second computation*: when a topological invariant admits both a gluing description and a curvature-integral description, matching them checks arithmetic and sign conventions and often reveals the normalisation constant (here the $\tfrac{i}{2\pi}$). The transferable diagnostic is that any integrality theorem — the degree of a map equals a Chern number equals a winding number equals an intersection number — is really one integer wearing several disguises, and the disguises are chosen to fit the tool at hand: Stokes and periods for de Rham, transition functions for classification, curvature integrals for Chern–Weil. This exercise is the abelian, two-dimensional prototype of that principle, and its non-abelian, four-dimensional sequel is the instanton-number computation that opens the study of Yang–Mills fields.
