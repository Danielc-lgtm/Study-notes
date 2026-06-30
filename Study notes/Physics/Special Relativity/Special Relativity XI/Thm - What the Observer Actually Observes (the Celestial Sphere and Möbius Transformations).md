---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Spinor Map and SL(2,C)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
  - "Def - Weyl Spinors (Left and Right Handed)"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus. A null four-vector $X$ has $X\cdot X = \det\underline X = 0$, where $\underline X = x^\mu\sigma_\mu$ is its [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Hermitian-matrix]] form. $\xi = (\xi_1,\xi_2)^{\mathsf T} \in \mathbb{C}^2$ is a two-component (left Weyl) spinor; $A = \begin{pmatrix}a&b\\c&d\end{pmatrix} \in SL(2,\mathbb{C})$ ($ad - bc = 1$) is a Lorentz transformation via the [[Def - The Spinor Map and SL(2,C)|spinor map]], acting on spacetime by $\underline X \mapsto A\underline X A^\dagger$. We write $\omega \in \mathbb{C}\cup\{\infty\}$ for a point of the **Riemann sphere** $\mathbb{C}\mathrm{P}^1$, $S^2$ for the celestial sphere, $\theta, \phi$ for the polar and azimuthal angles of a sky direction, and $\psi$ for a boost rapidity with $\beta = \tanh\psi$. Full registry on [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

---

# Statement

> **Theorem (the celestial sphere and Möbius transformations).** The future null directions seen by an observer at the origin form a sphere $S^2$, the **celestial sphere**. Each is encoded by a two-component spinor $\xi$ (defined up to phase) through the rank-one Hermitian matrix $\underline X = \xi\xi^\dagger$, and the map
> $$ \xi \;\longmapsto\; \omega = \frac{\xi_1}{\xi_2} \in \mathbb{C}\cup\{\infty\} $$
> is a stereographic projection identifying the celestial sphere with the Riemann sphere $\mathbb{C}\mathrm{P}^1$; for a direction at polar angle $\theta$ and azimuth $\phi$, $\omega = e^{i\phi}\cot(\theta/2)$. A restricted Lorentz transformation $A = \begin{pmatrix}a&b\\c&d\end{pmatrix} \in SL(2,\mathbb{C})$ acts on the spinor by $\xi \mapsto A\xi$, hence on the celestial sphere by the **Möbius transformation**
> $$ \omega \;\longmapsto\; \omega' = \frac{a\omega + b}{c\omega + d}, \qquad ad - bc = 1. $$
> The group of these maps is $PSL(2,\mathbb{C}) = SL(2,\mathbb{C})/\{\pm I\} \cong SO^+(1,3)$.

> **Corollary (a sphere always looks like a circle — Penrose–Terrell).** Because stereographic projection and Möbius transformations both send circles to circles (they are conformal), the outline of a sphere on one observer's sky is a circle on *every* observer's sky. Aberration is a conformal map of the heavens, not an affine squashing: the apparent outline of a round object is never distorted into an ellipse, however fast the observer moves.

---

# Motivation

Special relativity is usually presented as a theory of *coordinates* — what numbers different observers assign to the same event — and the lesson is that length contracts and time dilates. But coordinates are not what an observer *sees*. Seeing involves light, and light takes time to travel from an object to the eye, so the image on an observer's retina mixes the geometry of the object with the geometry of the light rays. The question this theorem answers is the one the coordinate story leaves open: what does a moving observer actually *see*?

The answer is unexpectedly elegant and is the payoff of the entire $SL(2,\mathbb{C})$ machinery. The directions from which light arrives form a sphere — the celestial sphere, literally the dome of the night sky — and that sphere is naturally the Riemann sphere of complex analysis. A change of observer acts on it not by some complicated angle-dependent distortion but by a Möbius transformation, the simplest nontrivial maps of the sphere, the same maps a first course in complex analysis studies. This is the sense in which "writing the Lorentz group as $SL(2,\mathbb{C})$ gives a wonderfully elegant way" (Tong) to answer the question.

The corollary is the genuinely surprising physics. Naively, a sphere rushing past should look squashed by length contraction into an ellipsoid, and its outline should be an ellipse. It is not. Because Möbius maps send circles to circles, the outline stays a perfect circle for every observer — a fact discovered, astonishingly, more than fifty years after Einstein, by Terrell and Penrose. The Lorentz contraction is real in the coordinates but *invisible* in the photograph of a sphere, exactly cancelled by the light-travel-time delay. This theorem is where that cancellation becomes transparent: it is the conformality of the Möbius action.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a null direction, encoded by a spinor," and recognising when the celestial-sphere picture applies is the skill.

The first disguised source is **"a light ray, or a massless particle's momentum."** Any null four-vector — the direction of an incoming photon, the momentum of a massless particle — has $\det\underline X = 0$, so factors as $\underline X = \xi\xi^\dagger$ and supplies a spinor and a point $\omega$ on the Riemann sphere. The bridge is that a rank-one Hermitian matrix is exactly an outer product $\xi\xi^\dagger$. *Example problem:* find the apparent direction of a star after a boost by tracking $\omega$.

The second disguised source is **"a question about appearance rather than coordinates."** Whenever a problem asks what an observer *sees* — the aberration of starlight, the apparent position of an object, the bunching of stars toward the direction of motion — it is a question about the celestial sphere and hence about a Möbius transformation. The bridge is that seeing is determined by null directions, which form the celestial sphere. *Example problem:* compute the forward concentration of the cosmic microwave background as seen by a fast-moving observer.

The third disguised source is **"the apparent shape of an extended object."** The outline of an object subtends a curve on the celestial sphere, and asking how that curve transforms under a change of observer is asking how a curve on $\mathbb{C}\mathrm{P}^1$ transforms under Möbius maps. The bridge is conformality: circles go to circles. *Example problem:* show a fast-moving sphere photographs as a circle (Penrose–Terrell), and a fast-moving cube appears rotated rather than contracted (Terrell rotation).

**Targets (Output Amplification)**

The conclusion is "Lorentz transformations act on the sky by Möbius maps."

Combine the conclusion with **conformality (circle-preservation)** to deduce that round outlines stay round. Since Möbius maps send circles to circles, the apparent outline of any spherical object is observer-independent up to a circle. The further result is the Penrose–Terrell invisibility of the Lorentz contraction. The combination is nonobvious because the *coordinates* of the sphere are genuinely contracted, yet the *image* is not. *Example:* the impossibility of photographing length contraction directly off a sphere.

Combine the conclusion with **a specific boost** to extract the aberration formula. A boost along the line of sight is the special Möbius map $\omega \mapsto e^{-\psi}\omega$ (a real dilation of the Riemann sphere), which in angles is $\cot(\theta'/2) = e^{-\psi}\cot(\theta/2)$ — the relativistic aberration formula. The further result connects the abstract group action to the measurable bending of starlight. The combination is useful because it turns a four-vector boost into a one-line transformation of a single complex number. *Example:* the headlight effect, in which a fast source's emission is beamed forward.

Combine the conclusion with **the kernel $\{\pm I\}$** to identify the symmetry group of the sky. Since $A$ and $-A$ give the same Möbius map, the group acting faithfully on the celestial sphere is $PSL(2,\mathbb{C}) \cong SO^+(1,3)$ — the restricted Lorentz group *is* the conformal group of the two-sphere. The combination is the deepest structural statement: relativistic kinematics and two-dimensional conformal geometry are the same subject. *Example:* recognising aberration as a conformal transformation.

---

# Why Is It True

The chain is short once each link is seen.

*Null directions form a sphere.* A future null vector has $t > 0$ and $t^2 = x^2 + y^2 + z^2$; fixing the (irrelevant) overall scale, the spatial part $(x,y,z)/t$ is a unit vector, a point of $S^2$. So the future light cone, modulo scaling, is the sphere of directions.

*A null direction is a spinor up to phase.* A Hermitian matrix of zero determinant has rank at most one (for a nonzero future-pointing one, exactly one), and a rank-one positive-semidefinite Hermitian matrix is an outer product $\xi\xi^\dagger$. The spinor $\xi$ is determined up to a phase $e^{i\beta}$ (since $\xi\xi^\dagger = (e^{i\beta}\xi)(e^{i\beta}\xi)^\dagger$), so the sphere of null directions is the space of spinors-up-to-phase-and-scale, which is exactly $\mathbb{C}\mathrm{P}^1$ — the projective line, the Riemann sphere.

*The ratio is stereographic projection.* Projectivising $\xi = (\xi_1,\xi_2)$ to the ratio $\omega = \xi_1/\xi_2$ is, geometrically, stereographic projection of the celestial sphere onto the plane: the point $\xi_2 = 0$ goes to $\omega = \infty$ (the north pole), and a direction at polar angle $\theta$, azimuth $\phi$ maps to $\omega = e^{i\phi}\cot(\theta/2)$. This is the standard identification of the sphere with $\mathbb{C}\cup\{\infty\}$.

*Lorentz acts by Möbius.* Here is the crux, and it is forced by the transformation law of the spinor. The four-vector transforms by $\underline X \mapsto A\underline X A^\dagger$, but $\underline X = \xi\xi^\dagger$, so $A\underline X A^\dagger = (A\xi)(A\xi)^\dagger$ — the spinor transforms by the *single* factor $\xi \mapsto A\xi$ ([[Def - Weyl Spinors (Left and Right Handed)|it is a Weyl spinor]]). The ratio then transforms as $\omega = \xi_1/\xi_2 \mapsto (a\xi_1 + b\xi_2)/(c\xi_1 + d\xi_2) = (a\omega + b)/(c\omega + d)$ — a fractional linear, i.e. Möbius, transformation. The Möbius action on the sky is simply the linear action $\xi \mapsto A\xi$ pushed down to the ratio.

**The whole theorem in one sentence: a null direction is a spinor up to phase, its stereographic coordinate is the ratio of the spinor's components, and since the spinor transforms linearly by $A$, the ratio transforms by the Möbius map of $A$.**

*Why circles stay circles.* Both stereographic projection and Möbius transformations are conformal — they preserve angles — and a basic fact of inversive geometry is that conformal maps of the sphere (equivalently, Möbius maps of the plane-plus-infinity) send the family of circles-and-lines to itself. Geometrically, a Möbius map is a composition of inversions in spheres, and inversions preserve circles. So a circle on the celestial sphere stays a circle. Since the outline of a sphere is a circle on the celestial sphere (it is the boundary of a cap), it remains a circle for every observer — that is the Penrose–Terrell statement, and it is conformality, nothing more.

---

# What Makes This Hard

The single non-obvious step is realising that the *spinor* (not the four-vector) is the natural object, and that it transforms by one factor of $A$ — which is what makes the action fractional-linear rather than something more complicated. Most people get stuck trying to transform the four-vector $\underline X$ directly and not seeing the Möbius structure; the trick is to factor $\underline X = \xi\xi^\dagger$ first. The second subtlety is conceptual: distinguishing what an observer *sees* (null directions, the celestial sphere) from the *coordinates* an observer assigns (the full four-vector), because the surprising cancellation in Penrose–Terrell lives precisely in that gap. The most common error is to apply length contraction to the apparent shape, concluding a sphere looks like an ellipse — forgetting that conformality forbids it.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show null directions form $S^2$; factor a null Hermitian matrix as $\xi\xi^\dagger$ to get a spinor up to phase; identify the ratio $\omega = \xi_1/\xi_2$ with stereographic projection onto $\mathbb{C}\mathrm{P}^1$; push the linear law $\xi \mapsto A\xi$ down to the Möbius law on $\omega$; invoke conformality for the circle corollary.

**Subgoal decomposition:**

1. **Null directions = $S^2$.** Show the future null cone modulo scale is the sphere of spatial directions.
   - *Hint:* $t^2 = x^2 + y^2 + z^2$ with $t > 0$; divide by $t$.
   - *Why needed:* Identifies the celestial sphere as a genuine $S^2$.

2. **Null Hermitian = $\xi\xi^\dagger$.** Show a rank-one positive-semidefinite Hermitian matrix is an outer product, $\xi$ up to phase.
   - *Hint:* $\det\underline X = 0 \Rightarrow$ rank $\le 1$; a rank-one Hermitian PSD matrix is $\xi\xi^\dagger$.
   - *Why needed:* Produces the spinor and exhibits the phase redundancy, so the sphere is $\mathbb{C}\mathrm{P}^1$.

3. **Stereographic coordinate.** Show $\omega = \xi_1/\xi_2$ identifies $\mathbb{C}\mathrm{P}^1$ with $\mathbb{C}\cup\{\infty\}$, and $\omega = e^{i\phi}\cot(\theta/2)$.
   - *Hint:* Parametrise a unit direction by $(\theta,\phi)$ and build $\xi$ from it.
   - *Why needed:* Makes the celestial sphere the concrete Riemann sphere.

4. **Möbius action.** Show $\xi \mapsto A\xi$ pushes to $\omega \mapsto (a\omega+b)/(c\omega+d)$.
   - *Hint:* $\omega = \xi_1/\xi_2$; substitute $A\xi$ and divide.
   - *Why needed:* This is the main claim — Lorentz acts by Möbius.

5. **Circle corollary.** Conclude circles map to circles.
   - *Hint:* Möbius maps are conformal and preserve the circle-line family.
   - *Why needed:* Gives Penrose–Terrell: a sphere looks like a circle to all observers.

---

# Lemma Decomposition

> [!note]- Lemma 1: A future null direction is a rank-one Hermitian matrix ξξ†
> **Statement:** A nonzero future-pointing null four-vector $X$ ($\det\underline X = 0$, $\mathrm{tr}\,\underline X > 0$) has $\underline X = \xi\xi^\dagger$ for a $\xi \in \mathbb{C}^2$ unique up to a phase $\xi \mapsto e^{i\beta}\xi$.
>
> **Hint:** Zero determinant forces rank $\le 1$; a rank-one positive-semidefinite Hermitian matrix is an outer product.
>
> **Why needed:** Produces the spinor labelling a null direction and exhibits the $U(1)$ phase redundancy, so the celestial sphere is $\mathbb{C}\mathrm{P}^1$.
>
> > [!note]- Full proof
> > $\det\underline X = 0$ means $\underline X$ is singular, so $\mathrm{rank}\,\underline X \le 1$; it is nonzero (since $X \neq 0$), so the rank is exactly $1$. A Hermitian matrix is diagonalisable with real eigenvalues; a rank-one Hermitian matrix has one nonzero eigenvalue $\lambda$, and positivity of the trace ($\mathrm{tr}\,\underline X = 2x^0 > 0$ for a future null vector) forces $\lambda > 0$. Writing the unit eigenvector as $u$, $\underline X = \lambda u u^\dagger = (\sqrt\lambda\, u)(\sqrt\lambda\, u)^\dagger = \xi\xi^\dagger$ with $\xi = \sqrt\lambda\,u$. Since $\xi\xi^\dagger = (e^{i\beta}\xi)(e^{i\beta}\xi)^\dagger$, $\xi$ is determined only up to a phase. (For the past cone one writes $\underline X = -\xi\xi^\dagger$.) $\blacksquare$

> [!note]- Lemma 2: The ratio ω = ξ₁/ξ₂ is stereographic projection
> **Statement:** The map $\xi \mapsto \omega = \xi_1/\xi_2 \in \mathbb{C}\cup\{\infty\}$ identifies $\mathbb{C}\mathrm{P}^1$ (spinors up to scale and phase) with the Riemann sphere, and a direction at polar angle $\theta$, azimuth $\phi$ has $\omega = e^{i\phi}\cot(\theta/2)$.
>
> **Hint:** A unit direction $\mathbf n = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ gives $\underline X = I + \mathbf n\cdot\boldsymbol\sigma$ (a null vector $(1,\mathbf n)$); factor it as $\xi\xi^\dagger$ and form the ratio.
>
> **Why needed:** Makes the abstract $\mathbb{C}\mathrm{P}^1$ into the concrete Riemann sphere with an explicit angle formula, needed for the aberration computation.
>
> > [!note]- Full proof
> > The future null vector in direction $\mathbf n$ is $X = (1, \mathbf n)$ with $\underline X = \sigma_0 + \mathbf n\cdot\boldsymbol\sigma = \begin{pmatrix}1 + \cos\theta & \sin\theta\,e^{-i\phi} \\ \sin\theta\,e^{i\phi} & 1 - \cos\theta\end{pmatrix}$. This is rank one (determinant $1 - \cos^2\theta - \sin^2\theta = 0$). Using $1 + \cos\theta = 2\cos^2\tfrac\theta2$, $1 - \cos\theta = 2\sin^2\tfrac\theta2$, $\sin\theta = 2\sin\tfrac\theta2\cos\tfrac\theta2$, one checks $\underline X = \xi\xi^\dagger$ with $\xi = \sqrt2\begin{pmatrix}\cos\tfrac\theta2\,e^{-i\phi/2} \\ \sin\tfrac\theta2\,e^{i\phi/2}\end{pmatrix}$ (verify: $\xi_1\bar\xi_1 = 2\cos^2\tfrac\theta2 = 1 + \cos\theta$, $\xi_1\bar\xi_2 = 2\cos\tfrac\theta2\sin\tfrac\theta2 e^{-i\phi} = \sin\theta\,e^{-i\phi}$). Hence
> > $$\omega = \frac{\xi_1}{\xi_2} = \frac{\cos\tfrac\theta2\,e^{-i\phi/2}}{\sin\tfrac\theta2\,e^{i\phi/2}} = e^{-i\phi}\cot\tfrac\theta2.$$
> > (The sign of $\phi$ in the exponent is a chirality/orientation convention; up to complex conjugation this is the standard stereographic coordinate $\omega = e^{i\phi}\cot(\theta/2)$, with $\theta = 0$ giving $\omega = \infty$ and $\theta = \pi$ giving $\omega = 0$.) The map is a bijection $S^2 \to \mathbb{C}\cup\{\infty\}$, the stereographic projection. $\blacksquare$

> [!note]- Lemma 3: ξ ↦ Aξ pushes down to the Möbius map
> **Statement:** If $\xi \mapsto A\xi$ with $A = \begin{pmatrix}a&b\\c&d\end{pmatrix}$, then $\omega = \xi_1/\xi_2 \mapsto \omega' = (a\omega + b)/(c\omega + d)$.
>
> **Hint:** Substitute the components of $A\xi$ and divide numerator by $\xi_2$.
>
> **Why needed:** This is the central claim: the Lorentz action on null directions is the Möbius action.
>
> > [!note]- Full proof
> > Under $\xi \mapsto A\xi$, the new components are $\xi_1' = a\xi_1 + b\xi_2$ and $\xi_2' = c\xi_1 + d\xi_2$. Therefore
> > $$\omega' = \frac{\xi_1'}{\xi_2'} = \frac{a\xi_1 + b\xi_2}{c\xi_1 + d\xi_2} = \frac{a(\xi_1/\xi_2) + b}{c(\xi_1/\xi_2) + d} = \frac{a\omega + b}{c\omega + d},$$
> > dividing numerator and denominator by $\xi_2$. This is the Möbius transformation associated with $A$, and the spinor transformation law $\xi \mapsto A\xi$ follows because $\underline X = \xi\xi^\dagger \mapsto A\underline X A^\dagger = (A\xi)(A\xi)^\dagger$ (Lemma 1 and the [[Def - The Spinor Map and SL(2,C)|spinor map]]). $\blacksquare$

> [!note]- Lemma 4: Möbius maps send circles to circles
> **Statement:** A Möbius transformation $\omega \mapsto (a\omega + b)/(c\omega + d)$ maps the family of circles-and-lines in $\mathbb{C}\cup\{\infty\}$ to itself; equivalently, circles on the Riemann sphere map to circles.
>
> **Hint:** Decompose a Möbius map into translations, dilations/rotations, and the inversion $\omega \mapsto 1/\omega$; check each preserves circles-and-lines.
>
> **Why needed:** Gives the Penrose–Terrell corollary — a sphere's circular outline stays circular for every observer.
>
> > [!note]- Full proof
> > Every Möbius map with $c \neq 0$ factors as $\omega \mapsto c\omega + d \mapsto 1/(c\omega + d) \mapsto a/c + (bc - ad)/c \cdot 1/(c\omega+d)$ — a composition of an affine map $\omega \mapsto \alpha\omega + \beta$ (translation, rotation, scaling) and the inversion $\omega \mapsto 1/\omega$ (the case $c = 0$ is purely affine). Affine maps obviously send circles to circles and lines to lines. For the inversion, the general circle-or-line $A|\omega|^2 + \mathrm{Re}(\bar B\omega) + C = 0$ (with $A, C \in \mathbb{R}$, $B \in \mathbb{C}$) becomes, under $\omega \mapsto 1/\omega$, the equation $C|\omega|^2 + \mathrm{Re}(B\omega) + A = 0$ — again of the circle-or-line form, with $A$ and $C$ swapped. Hence the whole family is preserved. On the sphere, lines are circles through the north pole, so the unified statement is "circles map to circles." Since the outline of a spherical object is a circle on the celestial sphere, it remains a circle under every Lorentz transformation. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **The celestial sphere.** A future-pointing null four-vector satisfies $x^0 > 0$ and $(x^0)^2 = (x^1)^2 + (x^2)^2 + (x^3)^2$; scaling by $x^0$ (light rays differing by scale are the same direction) leaves the unit spatial vector $\mathbf n = (x^1,x^2,x^3)/x^0 \in S^2$. So the set of future null directions is the sphere $S^2$, the celestial sphere.
>
> **Spinor encoding.** By Lemma 1, the Hermitian matrix $\underline X$ of a future null vector is $\xi\xi^\dagger$ for a spinor $\xi$ unique up to phase. By Lemma 2, the ratio $\omega = \xi_1/\xi_2$ identifies the celestial sphere $\mathbb{C}\mathrm{P}^1$ with the Riemann sphere $\mathbb{C}\cup\{\infty\}$ via stereographic projection, with $\omega = e^{i\phi}\cot(\theta/2)$ for a direction $(\theta,\phi)$.
>
> **Möbius action.** A Lorentz transformation acts by $\underline X \mapsto A\underline X A^\dagger$; since $\underline X = \xi\xi^\dagger$, this is $(A\xi)(A\xi)^\dagger$, i.e. the spinor transforms by $\xi \mapsto A\xi$ ([[Def - Weyl Spinors (Left and Right Handed)|a Weyl spinor]]). By Lemma 3, the ratio then transforms by the Möbius map $\omega \mapsto (a\omega+b)/(c\omega+d)$. The kernel of this action on $\omega$ is $\{\pm I\}$ (as for the spinor map), so the faithful group of sky transformations is $PSL(2,\mathbb{C}) = SL(2,\mathbb{C})/\{\pm I\} \cong SO^+(1,3)$.
>
> **Circle corollary.** By Lemma 4, Möbius maps send circles to circles. The outline of a sphere subtends a circle on the celestial sphere; under any change of observer this outline is transformed by a Möbius map and so remains a circle. Therefore a sphere photographs as a circle to every inertial observer (Penrose–Terrell), and aberration — being a conformal Möbius map — distorts patterns painted on the sphere but never the circular outline. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The aberration of the cosmic microwave background (cosmology).** The CMB is nearly isotropic in the cosmic rest frame, but an observer moving at velocity $\beta$ sees it boosted: hotter ahead, cooler behind, with the temperature pattern aberrated by exactly the Möbius dilation $\omega \mapsto e^{-\psi}\omega$ of this theorem. The measured dipole anisotropy of the CMB ($\sim 3.4$ mK) is this aberration, and it gives the Solar System's velocity through the CMB ($\sim 370$ km/s). The application turns the abstract Möbius action into a measured cosmological quantity.

**Terrell rotation of a fast-moving cube (visualisation).** A cube rushing past at relativistic speed does not appear length-contracted but *rotated* — the far face becomes visible because light from it, emitted earlier, reaches the observer alongside light from the near face. This **Terrell rotation** is the celestial-sphere statement that the cube's edges, mapped by a Möbius transformation, rearrange into the appearance of a rotated (not contracted) cube. The application is the standard correction to naive "relativistic flight simulator" graphics.

**Conformal field theory on the celestial sphere (quantum gravity).** In the modern *celestial holography* programme, scattering amplitudes in four-dimensional asymptotically flat spacetime are recast as correlation functions of a two-dimensional conformal field theory living on the celestial sphere, precisely because the Lorentz group acts on that sphere as the conformal group $PSL(2,\mathbb{C})$ of this theorem. The application is at the research frontier: the $SL(2,\mathbb{C})$-as-Möbius-group identification is the kinematical backbone of celestial amplitudes and their connection to soft theorems and asymptotic symmetries.

---

# Bridges

- **[[Def - Weyl Spinors (Left and Right Handed)]]** — the spinor $\xi$ labelling a null direction *is* a left Weyl spinor, and its transformation law $\xi \mapsto A\xi$ is exactly the defining $(\tfrac12,0)$ representation. The celestial sphere is therefore the projectivisation of the left Weyl spinor space, $\mathbb{P}(\mathbb{C}^2) = \mathbb{C}\mathrm{P}^1$, and the Möbius action is the projective action of $SL(2,\mathbb{C})$ on it.

- **[[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group]]** — the same kernel $\{\pm I\}$ that makes $\mathscr{S}$ two-to-one makes the Möbius action of $SL(2,\mathbb{C})$ on the sphere factor through $PSL(2,\mathbb{C}) = SL(2,\mathbb{C})/\{\pm I\}$, which is therefore isomorphic to $SO^+(1,3)$. The restricted Lorentz group *is* the Möbius (conformal) group of the two-sphere — a statement this theorem makes by exhibiting the action explicitly.

- **[[Thm - The Spinor Map SU(2) to SO(3)]]** — the Hopf fibration $S^3 = SU(2) \to S^2$ that appears there is the same $S^3/U(1) = S^2$ structure here: a unit spinor $\xi$ with $\xi^\dagger\xi = 1$ lives on $S^3$, the phase redundancy $\xi \mapsto e^{i\beta}\xi$ is the $U(1)$ fibre, and the quotient is the celestial sphere $S^2$. The rotation subgroup $SU(2)$ acts on the sphere by ordinary rigid rotations (the compact Möbius maps), while the boosts act by the non-compact dilations responsible for aberration.

- **[[Thm - Aberration of Light]]** (Special Relativity VIII) — the elementary aberration formula derived there from velocity composition is recovered here as the special Möbius map $\omega \mapsto e^{-\psi}\omega$, i.e. $\cot(\theta'/2) = e^{-\psi}\cot(\theta/2)$ with $e^{-\psi} = \sqrt{(1-\beta)/(1+\beta)}$. The celestial-sphere derivation is the geometric completion of the kinematic one, and it is what reveals aberration to be a conformal (circle-preserving) map. The apparent-shape effects are the subject of [[Def - Apparent Rotation and Images of Moving Objects]] (Penrose–Terrell), of which the circle corollary here is the spinor-method proof.

---

# Unlocked by This

> [!tip] The BMS Group and Celestial Holography *(from Quantum Gravity)*
> The celestial sphere is the conformal boundary structure of an asymptotically flat spacetime, and the Lorentz-as-Möbius action extends there to the infinite-dimensional **Bondi–Metzner–Sachs group**, whose "superrotations" are the local conformal transformations of the sphere. Gravitational scattering amplitudes, recast as correlators of a conformal field theory on this sphere (**celestial holography**), make the $PSL(2,\mathbb{C})$ Möbius symmetry of this theorem the global conformal symmetry of a putative two-dimensional dual theory. The flat-spacetime backdrop is [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] Twistor Theory *(from Mathematical Physics)*
> Penrose's **twistor programme** takes the identification "null ray $\leftrightarrow$ spinor" seriously as the foundation of a reformulation of spacetime physics: the basic object is not a point but a null ray, encoded by a spinor (a twistor), and fields are recovered by contour integrals over the twistor space $\mathbb{C}\mathrm{P}^3$. The celestial sphere $\mathbb{C}\mathrm{P}^1$ of this theorem is the first slice of that construction, and the Möbius action is the projective action of $SL(2,\mathbb{C})$ that twistor theory globalises. It is the route by which the conformal geometry of the sky becomes a tool for solving the field equations.
