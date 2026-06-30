---
type: definition
subject: special-relativity
prereqs:
  - "Thm - Polar Decomposition of the Lorentz Group"
  - "Def - Boosts as Hyperbolic Rotations"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\Lambda_1, \Lambda_2$ are [[Def - Boosts as Hyperbolic Rotations|Lorentz boosts]] with velocity vectors $\mathbf{V}_1, \mathbf{V}_2$ (in the rest space of an intermediate observer $e_0'$), Lorentz factors $\Gamma_1, \Gamma_2$, rapidities $\psi_1, \psi_2$. The angle between $\mathbf{V}_1$ and $\mathbf{V}_2$ is $\chi \in [0,\pi]$. We write $\oplus$ for relativistic velocity addition and $R[\mathbf{V}_1,\mathbf{V}_2]$ for the Thomas rotation, with angle $\varphi_T$. Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Axiom Motivation

The [[Thm - Polar Decomposition of the Lorentz Group|polar decomposition]] guarantees that, relative to a chosen observer, every restricted Lorentz transformation splits uniquely into a boost and a rotation. The Thomas rotation is what you get when you apply this split to the *composition of two boosts* — and the motivation for naming it is the discovery that the rotation factor is, surprisingly, not trivial.

Here is the surprise in full. Collinear boosts behave perfectly: two boosts along the same line compose to a boost along that line, with rapidities adding, and no rotation appears. One naturally expects this to persist for non-collinear boosts — that the composition of two boosts is always a boost, just along a tilted direction. It is *not*. Compose a boost along $x$ with a boost along $y$, and the result moves the observer to a new velocity (as expected) *but also rotates the spatial frame* about the $z$-axis. The composition is a boost times a leftover rotation, and that leftover rotation is the Thomas rotation. The motivation for the concept is precisely to name and quantify this unexpected residue.

Why must it exist? The polar decomposition gives the answer at the level of structure. The product $\Lambda_2\circ\Lambda_1$ of two boosts is restricted, so it factors uniquely as $S\circ R$ relative to the initial observer $e_0$. The boost $S$ is forced — it is the boost carrying $e_0$ to the final velocity $\Lambda_2\Lambda_1(e_0)$, which is the relativistic sum of the two velocities. The rotation $R$ is whatever is left, $R = S^{-1}\Lambda_2\Lambda_1$. The question is whether $R = \mathrm{Id}$. It would be, if $\Lambda_2\Lambda_1$ were itself a boost; but a boost in a semi-adapted basis is *symmetric*, and the product of two boosts in non-coplanar planes is *not* symmetric (the product of two symmetric matrices is symmetric only if they commute, and non-coplanar boosts do not commute). So $R \ne \mathrm{Id}$: the asymmetry of the product *is* the Thomas rotation. The concept is motivated by the need to extract and measure this asymmetry.

What controls the rotation? The single geometric parameter is the angle $\chi$ between the two boost velocities. At $\chi = 0$ or $\pi$ the boosts are collinear, the product is a boost, and $R = \mathrm{Id}$. As $\chi$ moves toward $\pi/2$ the rotation grows, reaching its maximum for perpendicular boosts. So the Thomas rotation is a function of the two speeds and the angle between them, vanishing in the collinear limit. This is why the definition must be stated for *non-collinear* boosts: the collinear case is the degenerate one where the rotation disappears.

The deeper motivation is physical. A particle moving on a curved worldline — an electron in an atom, a gyroscope in orbit — is continuously boosted in changing directions, and each pair of successive infinitesimal boosts leaves an infinitesimal Thomas rotation. Integrated around the orbit, these accumulate into a net rotation of the particle's spin: the **Thomas precession**. So the Thomas rotation is not a curiosity of composing two finite boosts; it is the kinematic seed of a measurable precession that appears in the fine structure of atomic spectra. The definition exists to make this seed precise.

---

# The Definition

Let $\Lambda_1, \Lambda_2$ be two Lorentz boosts whose planes share a timelike direction (the case of a change of observer), with velocity vectors $\mathbf{V}_1, \mathbf{V}_2$ relative to an intermediate observer $e_0'$, not collinear. By the [[Thm - Polar Decomposition of the Lorentz Group|polar decomposition]], the composition factors uniquely as
$$
\Lambda_2 \circ \Lambda_1 = S \circ R,
$$
where $S$ is a boost and $R$ is a spatial rotation fixing the appropriate timelike direction. The rotation $R$ is the **Thomas rotation** (also the **Wigner rotation**) of the pair $(\Lambda_1, \Lambda_2)$, written $R[\mathbf{V}_1, \mathbf{V}_2]$.

Its plane is the plane spanned by the two boost velocities, $\Pi_R = \mathrm{Span}(\mathbf{V}_1, \mathbf{V}_2)$ (equivalently $\mathrm{Span}(e_1, e_2)$ in the adapted frame), and its angle $\varphi_T$, the **Thomas rotation angle** (or **Wigner angle**), satisfies
$$
\cos\varphi_T = 1 - \frac{(\Gamma_1 - 1)(\Gamma_2 - 1)}{1 + \Gamma}\sin^2\chi, \qquad -\pi \le \varphi_T \le 0,
$$
where $\chi$ is the angle between $\mathbf{V}_1, \mathbf{V}_2$ and $\Gamma = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi)$ is the Lorentz factor of the composite boost $S$. The rotation is **clockwise** in $\Pi_R$ (oriented so that $\mathbf{V}_1\times\mathbf{V}_2$ is the positive normal), hence the sign $\varphi_T \le 0$. For collinear boosts ($\chi = 0$ or $\pi$), $R = \mathrm{Id}$ and $\varphi_T = 0$.

Equivalently, the Thomas rotation is the exact obstruction to commutativity of relativistic velocity addition: writing $\mathbf{V}_1 \oplus \mathbf{V}_2$ for the relativistic sum ([[Thm - Relativistic Velocity Addition]], general form),
$$
\mathbf{V}_1 \oplus \mathbf{V}_2 = R[\mathbf{V}_1, \mathbf{V}_2]\,(\mathbf{V}_2 \oplus \mathbf{V}_1),
$$
so the two orders of addition differ by the Thomas rotation.

---

# Categorical / Structural Definition

The Thomas rotation is a *cocycle* on the set of boost velocities. Relativistic velocity addition makes the open unit ball $\mathcal{B} = \{\mathbf{V} : |\mathbf{V}| < 1\}$ into a **gyrogroup** — a structure satisfying group-like axioms but with commutativity and associativity twisted by an automorphism. The twisting automorphism is exactly the Thomas rotation: defining the *gyration* $\mathrm{gyr}[\mathbf{V}_1, \mathbf{V}_2] := R[\mathbf{V}_1,\mathbf{V}_2] \in SO(3)$, the gyrogroup axioms read
$$
\mathbf{V}_1 \oplus \mathbf{V}_2 = \mathrm{gyr}[\mathbf{V}_1,\mathbf{V}_2](\mathbf{V}_2 \oplus \mathbf{V}_1) \quad\text{(gyrocommutativity)},
$$
$$
\mathbf{V}_1 \oplus (\mathbf{V}_2 \oplus \mathbf{V}_3) = (\mathbf{V}_1 \oplus \mathbf{V}_2) \oplus \mathrm{gyr}[\mathbf{V}_1, \mathbf{V}_2]\mathbf{V}_3 \quad\text{(gyroassociativity)}.
$$
The gyration $\mathrm{gyr}[\mathbf{V}_1,\mathbf{V}_2]$ measures, at the level of $SO(3)$, the failure of the boost subset to be a subgroup of $SO^+(1,3)$. In the language of group extensions, the boosts do not form a subgroup, but they form a *section* of the quotient map $SO^+(1,3) \to SO^+(1,3)/SO(3)$ (the coset space of velocities), and the Thomas rotation is the cocycle measuring the failure of this section to be a homomorphism. The category-theoretic content is that velocity space $\mathcal{B}$ is the homogeneous space $SO^+(1,3)/SO(3)$, the boosts are a (non-group) set of coset representatives, and composing two representatives and re-normalising introduces the Thomas rotation as the correction term.

---

# Relate to Other Fields / Compression

The Thomas rotation is the **holonomy of velocity space**. Geometrically, the ball of velocities with the Lorentz-invariant metric is a model of three-dimensional **hyperbolic space**, the boosts act as its hyperbolic translations, and the Thomas rotation is the holonomy of parallel transport around a closed loop. Carry a vector around a geodesic triangle in hyperbolic space and it returns rotated by an angle equal to the *area* of the triangle (the angular deficit, by Gauss–Bonnet with constant negative curvature). Composing two boosts and returning traces such a triangle, and the Thomas angle is its area deficit. This is the precise sense in which the Thomas rotation is curvature made kinematic: it is nonzero exactly because velocity space is curved.

**True name:** the Thomas rotation is "the holonomy of parallel transport around a loop in hyperbolic velocity space," equivalently "the gyration automorphism measuring the non-closure of boosts." The polar-decomposition definition (the rotation factor of a product of two boosts) is the official one, but the operational content is that it is the unavoidable rotation generated when you change velocity in a closed cycle — the same geometric phenomenon as the Foucault pendulum's precession (holonomy on the sphere) or Berry's phase (holonomy in parameter space), here on the hyperbolic manifold of velocities.

---

# Examples / Corollaries

**Is an instance — two perpendicular boosts.** Boost along $x$ by $\mathbf{V}_1 = V_1\hat{\mathbf{x}}$, then along $y$ by $\mathbf{V}_2 = V_2\hat{\mathbf{y}}$, so $\chi = \pi/2$. The Thomas rotation is about the $z$-axis with $\cos\varphi_T = (\Gamma_1 + \Gamma_2)/(1 + \Gamma_1\Gamma_2)$. For small speeds, $\varphi_T \approx -\tfrac12 V_1 V_2$.

**Is an instance — the non-commutativity of velocity addition.** Adding $\mathbf{V}_1$ then $\mathbf{V}_2$ gives a velocity rotated by $\varphi_T$ relative to adding $\mathbf{V}_2$ then $\mathbf{V}_1$: the magnitudes $|\mathbf{V}_1\oplus\mathbf{V}_2| = |\mathbf{V}_2\oplus\mathbf{V}_1|$ agree, but the *directions* differ by the Thomas angle, which is why velocity addition is not commutative.

**Is NOT an instance — collinear boosts.** Two boosts along the same line ($\chi = 0$) compose to a pure boost, $R = \mathrm{Id}$, $\varphi_T = 0$: there is *no* Thomas rotation. This is the degenerate case the definition excludes from the "non-collinear" hypothesis, and it is why the relativistic velocity-addition formula for collinear velocities is commutative.

**Is NOT an instance — a single boost.** A single boost has no Thomas rotation: the phenomenon requires *two* boosts in different directions. Polar-decomposing a single boost gives $S = $ that boost and $R = \mathrm{Id}$.

**Corollary — the maximal Thomas angle.** Fixing the speeds and varying $\chi$, the Thomas angle is maximal at $\cos\chi_m = -\sqrt{(\Gamma_1-1)(\Gamma_2-1)/((\Gamma_1+1)(\Gamma_2+1))}$ (so $\chi_m > \pi/2$), where $\cos\varphi_{T,\max} = 1 - 2(\Gamma_1-1)(\Gamma_2-1)/((\Gamma_1+1)(\Gamma_2+1))$. As $\Gamma_1, \Gamma_2 \to \infty$ the maximal Thomas angle approaches $\pi$: ultrarelativistic boosts can produce nearly a half-turn.

**Calibration check.** The reader who has understood the definition should be able to: (i) state why collinear boosts produce no Thomas rotation, in terms of $\sin\chi = 0$; (ii) compute the small-velocity limit $\varphi_T \approx -\tfrac12(\mathbf{V}_1\times\mathbf{V}_2)$ (magnitude $\tfrac12 V_1 V_2\sin\chi$) from the formula; (iii) explain why the Thomas rotation makes velocity addition non-commutative but keeps the magnitudes of the two orders equal.

---

# Unlocked by This

> [!tip] Thomas Precession and Atomic Fine Structure *(from Special Relativity XVI)*
> A gyroscope (or an electron's spin) carried around a closed loop in velocity space accumulates the integrated infinitesimal Thomas rotations as a net precession, the **Thomas precession**, with rate $\boldsymbol{\Omega}_T = \frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}$. For an electron orbiting a nucleus, this kinematic precession opposes the precession induced by the magnetic interaction and supplies exactly the factor of $\tfrac12$ that reconciles the naive spin–orbit coupling with the observed fine-structure splitting of hydrogen — a half that puzzled physicists until Thomas explained it in 1926 as a purely relativistic effect of the non-closure of boosts. See [[Special Relativity XVI — Accelerated Observers]], [[Def - Thomas Precession]], and [[Thm - The Thomas Equation]].

> [!tip] Gyrogroups and the Algebra of Velocity Space *(from abstract algebra)*
> The Thomas rotation is the defining structure of a **gyrogroup**, Abraham Ungar's axiomatization of relativistic velocity addition as a group-like object whose commutativity and associativity are twisted by the gyration automorphism $\mathrm{gyr}[\mathbf{u},\mathbf{v}] = R[\mathbf{u},\mathbf{v}]$. The ball of velocities with $\oplus$ is the prototype gyrogroup (the "Einstein gyrogroup"), and the same structure appears for the Möbius addition of the complex disk and for the bootstrapping of hyperbolic geometry from the velocity-addition law. This reframes "boosts do not form a subgroup" as the precise statement that velocities form a gyrogroup, not a group, with the Thomas rotation as the obstruction.

> [!tip] Berry Phase and Geometric Phases *(from quantum mechanics)*
> The Thomas rotation is a **geometric phase** — a holonomy acquired by transporting a state around a closed loop in a parameter space, here the hyperbolic space of velocities. It is the relativistic-kinematic cousin of **Berry's phase** in quantum mechanics (holonomy in the space of Hamiltonian parameters), the Aharonov–Bohm phase (holonomy around a flux), and the Foucault pendulum's precession (holonomy on the sphere). All are instances of the same principle: parallel transport around a closed loop in a curved space returns the transported object rotated or phase-shifted by an amount equal to the enclosed curvature, and the Thomas rotation is this principle applied to the curved manifold of relativistic velocities.
