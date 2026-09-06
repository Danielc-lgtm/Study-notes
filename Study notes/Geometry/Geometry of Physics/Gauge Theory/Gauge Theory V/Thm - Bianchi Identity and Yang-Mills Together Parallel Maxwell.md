---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Yang-Mills Equation"
  - "Def - The Yang-Mills Field Strength"
  - "Thm - Yang-Mills Equation from the Action Principle"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

$(M, g)$ is an oriented 4-manifold (typically Minkowski $\mathbb{R}^{1,3}$ or Euclidean $\mathbb{R}^4$); $G$ a compact Lie group; $A$ a connection on a principal $G$-bundle with field strength $F$; $J$ a current source. For $G = U(1)$, the standard EM identifications are $F_{0i} = -E_i$ (electric field components), $F_{ij} = \epsilon_{ijk}B_k$ (magnetic field components), $A^\mu = (\phi, \vec A)$ (scalar and vector potentials), $J^\mu = (\rho, \vec j)$ (charge density and current density).

Maxwell's equations in their classical vector form are:
- Gauss: $\nabla\cdot\vec E = \rho$
- No magnetic monopoles: $\nabla\cdot\vec B = 0$
- Faraday: $\nabla\times\vec E + \partial_t\vec B = 0$
- Ampère–Maxwell: $\nabla\times\vec B - \partial_t\vec E = \vec j$

Wider conventions are in [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons]].

---

# Statement

> **Theorem (YM + Bianchi $\implies$ Maxwell for $G = U(1)$, generalised Maxwell for non-abelian $G$).** Let $A$ be a connection on a principal $G$-bundle over a 4-manifold $(M, g)$, with field strength $F$ and a current source $J \in \Omega^1(M; \operatorname{ad} P)$. The pair of equations
> $$d_A F = 0 \quad\text{(Bianchi identity)} \qquad\text{and}\qquad d_A\star F = \star J \quad\text{(Yang-Mills)}$$
> reduces, for $G = U(1)$ on Minkowski $\mathbb{R}^{1,3}$, to the four Maxwell equations:
> - Bianchi $dF = 0$ gives $\nabla\cdot\vec B = 0$ and $\nabla\times\vec E + \partial_t\vec B = 0$.
> - Yang-Mills $d\star F = \star J$ gives $\nabla\cdot\vec E = \rho$ and $\nabla\times\vec B - \partial_t\vec E = \vec j$.
>
> For non-abelian $G$ the same equations retain their differential-form structure but acquire commutator terms $-iq[A, \cdot]$ in the covariant derivatives, yielding the non-abelian generalisations
> - $\partial_\mu F^{\mu\nu} - iq[A_\mu, F^{\mu\nu}] = J^\nu$ (Yang-Mills with source),
> - $\partial_{[\mu}F_{\nu\rho]} - iq[A_{[\mu}, F_{\nu\rho]}] = 0$ (Bianchi).

> **Corollary (charge conservation).** Applying $d_A$ to the sourced YM equation and using $d_A^2 = [F, \cdot]$ plus Bianchi, one gets $d_A\star J = 0$. For $G = U(1)$ this is the classical charge conservation $\partial_\mu J^\mu = \partial_t\rho + \nabla\cdot\vec j = 0$.

---

# Motivation

This theorem says that **Yang–Mills theory is literally non-abelian Maxwell theory** — the differential-form equations are the same, only the gauge group changes. This is the technical justification for treating YM as "generalised electromagnetism", and the bridge that allows physicists to develop intuition about non-abelian gauge theory from familiarity with Maxwell's equations.

Three observations make the theorem non-trivial. First, the *structural unity* of the Maxwell equations as a single pair $(dF = 0, d\star F = \star J)$ is itself a substantive result — in the classical vector formulation, the four Maxwell equations look like four unrelated facts, but in the differential-form formulation they collapse to two equations of the same character (covariant exterior derivative of a 2-form). This unification was achieved by Hermann Weyl in the 1920s and is one of the most elegant simplifications in mathematical physics.

Second, the *correspondence between differential-form objects and vector-calculus objects* is non-obvious: the 2-form $F$ on $\mathbb{R}^{1,3}$ has 6 independent components, which split as 3 "electric" ($F_{0i}$) and 3 "magnetic" ($F_{ij}$); the Hodge dual $\star F$ on Minkowski $\mathbb{R}^{1,3}$ exchanges electric and magnetic (with appropriate signs), so the YM equation $d\star F = \star J$ involves the *magnetic* components on the LHS contributing to the *electric* charge equation. Working out these correspondences explicitly is the substantive content of the proof.

Third, the *commutator generalisation* to non-abelian $G$ adds physically essential self-interaction terms: $\partial_\mu F^{\mu\nu} - iq[A_\mu, F^{\mu\nu}] = J^\nu$, where the $-iq[A, F]$ term is *the field acting as its own source*. In QED, photons do not carry electric charge and there is no self-interaction; in QCD, gluons carry colour charge and interact directly with each other via this commutator term. The non-linear nature of QCD — confinement, asymptotic freedom, mass gap — is essentially due to this single term in the equations.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a connection $A$ on a $U(1)$- or general compact-$G$-bundle on a 4-manifold". Each of the following is a source from which this hypothesis can be extracted in a less obvious problem.

A first source is **a Lagrangian $\mathcal{L} = -\tfrac14 F^{\mu\nu}F_{\mu\nu} + (\text{matter terms})$ for a fundamental field theory**. Property $B$ is "the field theory has gauge invariance and a $U(1)$ or non-abelian gauge group". The bridge is that by the Euler–Lagrange theorem applied to the $A_\mu$ variations, the resulting field equation is exactly $\partial_\mu F^{\mu\nu} = J^\nu$ (with the Noether current of matter as source). So any Lagrangian field theory containing a Maxwell-like kinetic term for a gauge field produces Maxwell (or non-abelian Maxwell) as its EOM. This is the source behind every gauge theory in physics.

A second source is **a vector bundle with a flat connection** ($F = 0$). Property $B$ is "the connection has zero curvature". The bridge is that $F = 0$ trivially satisfies the YM equation $d\star F = 0$ and is *also* trivially Bianchi-satisfying. So flat connections are always in the kernel of both equations — the "vacuum" sector. The space of flat $G$-connections modulo gauge equivalence is the **character variety** $\operatorname{Hom}(\pi_1(M), G)/G$, a finite-dimensional algebraic variety. This is the source behind the entire theory of *flat-bundle invariants* (Chern–Simons theory at level 0, Reidemeister torsion, Wilson lines).

A third source is **a static configuration with rotational symmetry**. Property $B$ is "the field configuration depends only on the radial coordinate $r$ and time $t$, with rotational symmetry in the angular variables". The bridge is that the Maxwell equations in spherical coordinates reduce to ODEs on $r$ and $t$ — much easier than the full PDE — and the resulting solutions include the **Coulomb potential** $A_0 = q/(4\pi r)$ and the **magnetic monopole** $A_\theta = (g/4\pi)(1 - \cos\theta)$ (Dirac monopole, which has a string singularity). For non-abelian $G$, the same ansatz produces **'t Hooft–Polyakov monopoles** (regular solutions when the gauge group is spontaneously broken). The reduction to ODEs is the dominant technique for finding explicit solutions of Maxwell/YM with source.

**Targets (Output Amplification)**

The conclusion is "the pair (Bianchi, YM) gives Maxwell-like first-order equations on $F$". Each of the following combines this with one more property $D$ to give a non-trivial result $E$.

A first combination is **Maxwell pair + Lorenz gauge $\partial_\mu A^\mu = 0$ = wave equation on $A$**. Add the property $D$ of the Lorenz gauge condition (which can always be imposed by a gauge transformation). The Maxwell equations $\partial_\mu F^{\mu\nu} = J^\nu$ become $\partial^2 A^\nu - \partial^\nu(\partial_\mu A^\mu) = J^\nu$, which in Lorenz gauge reduces to $\partial^2 A^\nu = J^\nu$, the wave equation on each component of $A^\nu$. The result $E$ is that electromagnetic waves propagate at the speed of light $c$, and the Maxwell equations admit plane-wave solutions $A^\nu = \epsilon^\nu e^{ik\cdot x}$ with $k^2 = 0$ — the electromagnetic radiation that constitutes light.

A second combination is **Maxwell pair + duality $F \to \star F$ = electromagnetic duality**. Add the property $D$ that the source-free Maxwell equations $dF = 0$, $d\star F = 0$ are *symmetric* under $F \leftrightarrow \star F$. The result $E$ is **electromagnetic duality**: a transformation $(\vec E, \vec B) \to (\vec B, -\vec E)$ that preserves the Maxwell equations and exchanges electric and magnetic sectors. This duality is broken by the presence of electric sources (no magnetic monopoles in standard EM); restoring it would require magnetic-monopole sources, leading to the **Dirac quantisation condition** $eg = 2\pi n\hbar$ on magnetic-electric charge product. In non-abelian theories, the analogous duality is **Montonen–Olive duality** between $SU(N)$ and its dual group, central to modern string theory and $\mathcal{N} = 4$ super-Yang–Mills.

A third combination is **Maxwell pair + axisymmetric ansatz = magnetic monopole**. Add the property $D$ of spherical symmetry. The Maxwell equations on $\mathbb{R}^3$ with magnetic charge $g$ at the origin produce the **Dirac monopole** $\vec B = (g/4\pi r^2)\hat r$, derivable from the singular potential $\vec A = (g/4\pi)(1 - \cos\theta)/(r\sin\theta)\hat\phi$ which has a string singularity along the negative $z$-axis. The result $E$ is the existence of magnetic-monopole solutions to Maxwell (when one allows singular potentials), the **Dirac quantisation condition** required for the string to be invisible to electron wavefunctions, and ultimately the topology of $U(1)$-bundles on $S^2$. See [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]] for the magnetic monopole's natural setting.

---

# Why Is It True

The intuition is direct: **the differential-form equation $dF = 0$ on a 4-manifold contains $4 = \binom{4}{3}$ independent component equations, two each from the "time-like" $(F_{0[ij]})$ and "space-like" $(F_{[ijk]})$ pieces — which are precisely the no-monopole and Faraday equations of vector calculus**. Similarly, the equation $d\star F = \star J$ contains 4 component equations splitting as Gauss + Ampère–Maxwell.

The mechanism in one bolded sentence: **the 6 components of the antisymmetric tensor $F_{\mu\nu}$ split into 3 electric and 3 magnetic components, the Hodge star exchanges them with signs determined by the metric, and the two differential operations $d$ and $d\star$ on a 2-form in 4D each produce 4 component equations — exactly the count of Maxwell's equations**.

The verification is computational. For $G = U(1)$ on Minkowski $\mathbb{R}^{1,3}$ with $F_{\mu\nu}$ given by the EM identifications:
- $dF = 0$ in components reads $\partial_{[\mu}F_{\nu\rho]} = 0$, four equations indexed by the triple $(\mu, \nu, \rho)$ from $\{0, 1, 2, 3\}$. Three of these (with $\mu = 0$) give $\partial_t F_{ij} - \partial_i F_{0j} + \partial_j F_{0i} = 0$, i.e., the three components of $\partial_t\vec B + \nabla\times\vec E = 0$ (Faraday). One (with all spatial indices) gives $\partial_i F_{jk} + (\text{cyclic}) = 0$, i.e., $\nabla\cdot\vec B = 0$ (no monopoles).
- $d\star F = \star J$ in components reads $\partial_\mu F^{\mu\nu} = J^\nu$, four equations indexed by $\nu \in \{0, 1, 2, 3\}$. The $\nu = 0$ equation gives $\partial_i E^i = \rho$, i.e., $\nabla\cdot\vec E = \rho$ (Gauss). The three spatial $\nu = i$ equations give $\partial_0 F^{0i} + \partial_j F^{ji} = J^i$, which after using $F^{0i} = -E^i$ and $F^{ij} = \epsilon^{ijk}B_k$ unpacks to $-\partial_t E^i + \epsilon^{ijk}\partial_j B_k = J^i$, i.e., $\nabla\times\vec B - \partial_t\vec E = \vec j$ (Ampère–Maxwell).

For non-abelian $G$ the same calculation produces the same component equations *plus* commutator terms $-iq[A, F]$ everywhere a covariant derivative appears. The non-abelian Maxwell equations are then $\partial_\mu F^{\mu\nu} - iq[A_\mu, F^{\mu\nu}] = J^\nu$, with the new term being the self-interaction of the gauge field.

The corollary on charge conservation follows by applying $d_A$ to the sourced YM equation: $d_A^2\star F = d_A\star J$. The LHS is $d_A^2\star F = [F, \star F]$ (using the curvature definition $d_A^2 = [F, \cdot]$ on adjoint-valued forms). For $G = U(1)$, $[F, \star F] = 0$ because the algebra is abelian, so $d\star J = 0$, i.e., $\partial_\mu J^\mu = 0$ — charge conservation. For non-abelian $G$, $[F, \star F]$ is generally non-zero, but it vanishes *on shell* (when $d_A\star F = J$), and one obtains the covariant conservation $d_A\star J = 0$.

---

# What Makes This Hard

The principal difficulty is *getting the component equations right* — the indices, signs, and signature conventions interact in delicate ways, and a single misplaced sign produces wrong equations. The most common errors: (a) forgetting the factor of $\sqrt{|g|}$ in the components of the Hodge star, leading to wrong dependence on the metric determinant; (b) misidentifying $F^{0i} = E^i$ versus $F^{0i} = -E^i$ depending on the signature convention; (c) confusing the *graded* commutator on $\mathfrak{g}$-valued forms with the *matrix* commutator on coefficients — they involve different signs in different degrees. A careful component-by-component verification is the only reliable way to dispel doubt, and is done at least once in any serious treatment.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
For $G = U(1)$, expand $F = F_{\mu\nu}\tfrac12 dx^\mu\wedge dx^\nu$ with the EM identifications, compute $dF$ and $d\star F$ in coordinates, and match each component to one of the four Maxwell equations. For non-abelian $G$, repeat with the commutator terms restored.

**Subgoal decomposition:**

1. **Identify the components of $F$ for $G = U(1)$ on Minkowski space.** $F_{0i} = -E_i$, $F_{ij} = \epsilon_{ijk}B_k$.
   - *Hint:* The conventions are partially convention-dependent; the choice here matches Frankel and most modern texts.
   - *Why needed:* Sets up the identification of differential-form components with vector-calculus components.

2. **Compute the four independent components of $dF = 0$.** For $\mu\nu\rho$ chosen from $\{0, 1, 2, 3\}$, the equation $\partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu} + \partial_\rho F_{\mu\nu} = 0$ has 4 distinct triples (mod permutations). Three involve $\mu = 0$ (Faraday components), one involves all spatial indices (no-monopole).
   - *Hint:* The 4 triples correspond to $\binom{4}{3} = 4$.
   - *Why needed:* Connects $dF = 0$ to the two "homogeneous" Maxwell equations.

3. **Compute the four independent components of $d\star F = \star J$.** For $\nu \in \{0, 1, 2, 3\}$, the equation $\partial_\mu F^{\mu\nu} = J^\nu$ has 4 components. $\nu = 0$ gives Gauss; $\nu = i$ gives Ampère–Maxwell.
   - *Hint:* The Hodge dual on Minkowski signature: $(\star F)_{\rho\sigma} = \tfrac12\sqrt{|g|}\,\epsilon_{\rho\sigma\mu\nu}F^{\mu\nu}$.
   - *Why needed:* Connects $d\star F = \star J$ to the two "inhomogeneous" Maxwell equations.

4. **Repeat with commutator terms for non-abelian $G$.** All four component equations acquire an extra $-iq[A_\mu, F^{\mu\nu}]$ or similar commutator term.
   - *Hint:* The covariant exterior derivative is $d_A = d + [\omega, \cdot]$ with $\omega = -iqA$.
   - *Why needed:* Extends the result to the non-abelian case, with self-interaction terms.

---

# Lemma Decomposition

> [!note]- Lemma 1: $dF = 0$ in components for the $U(1)$ field on Minkowski space
> **Statement:** With $F_{0i} = -E_i$, $F_{ij} = \epsilon_{ijk}B_k$ on Minkowski $\mathbb{R}^{1,3}$ with signature $(-,+,+,+)$, the four component equations of $dF = 0$ are: $\nabla\cdot\vec B = 0$ (one equation) and $\partial_t\vec B + \nabla\times\vec E = 0$ (three equations).
>
> **Hint:** $dF$ is a 3-form, with components $(dF)_{\mu\nu\rho} = \partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu} + \partial_\rho F_{\mu\nu}$.
>
> **Why needed:** This is the Maxwell side of the Bianchi identity, identified as the no-monopole and Faraday equations.
>
> > [!note]- Full proof
> > For the triple $(\mu, \nu, \rho) = (1, 2, 3)$: $(dF)_{123} = \partial_1 F_{23} + \partial_2 F_{31} + \partial_3 F_{12} = \partial_1(\epsilon_{231}B_1) + \partial_2(\epsilon_{312}B_2) + \partial_3(\epsilon_{123}B_3) = \partial_1 B_1 + \partial_2 B_2 + \partial_3 B_3 = \nabla\cdot\vec B$. Setting this to zero: $\nabla\cdot\vec B = 0$.
> >
> > For the triple $(\mu, \nu, \rho) = (0, 2, 3)$: $(dF)_{023} = \partial_0 F_{23} + \partial_2 F_{30} + \partial_3 F_{02} = \partial_t B_1 + \partial_2 E_3 - \partial_3 E_2 = \partial_t B_1 + (\nabla\times\vec E)_1$. Setting to zero: $\partial_t B_1 + (\nabla\times\vec E)_1 = 0$. Similarly for the triples $(0,3,1)$ and $(0,1,2)$, giving the other two components. Combined: $\partial_t\vec B + \nabla\times\vec E = 0$, Faraday's law.

> [!note]- Lemma 2: $d\star F = \star J$ in components for the $U(1)$ field on Minkowski space
> **Statement:** With $F_{0i} = -E_i$, $F_{ij} = \epsilon_{ijk}B_k$, $J^\mu = (\rho, \vec j)$, the four component equations of $d\star F = \star J$ are: $\nabla\cdot\vec E = \rho$ (Gauss, one equation) and $\nabla\times\vec B - \partial_t\vec E = \vec j$ (Ampère–Maxwell, three equations).
>
> **Hint:** Equivalently $\partial_\mu F^{\mu\nu} = J^\nu$ in components, raised indices using $\eta^{\mu\nu} = \operatorname{diag}(-1, +1, +1, +1)$.
>
> **Why needed:** This is the Maxwell side of the YM equation, identified as the Gauss and Ampère–Maxwell equations.
>
> > [!note]- Full proof
> > For $\nu = 0$: $\partial_\mu F^{\mu 0} = \partial_i F^{i0} = \partial_i (-\eta^{ii}\eta^{00}E_i) = \partial_i E_i = \nabla\cdot\vec E$ (using $\eta^{00} = -1$, $\eta^{ii} = +1$). Setting this equal to $J^0 = \rho$: $\nabla\cdot\vec E = \rho$, Gauss's law.
> >
> > For $\nu = 1$: $\partial_\mu F^{\mu 1} = \partial_0 F^{01} + \partial_2 F^{21} + \partial_3 F^{31}$. Computing: $F^{01} = \eta^{00}\eta^{11}F_{01} = -F_{01} = E_1$ (using the signature). $F^{21} = \eta^{22}\eta^{11}F_{21} = F_{21} = -\epsilon_{21k}B_k = -\epsilon_{213}B_3 = B_3$. Similarly $F^{31} = -B_2$. So $\partial_0 F^{01} + \partial_2 F^{21} + \partial_3 F^{31} = -\partial_t E_1 + \partial_2 B_3 - \partial_3 B_2 = -\partial_t E_1 + (\nabla\times\vec B)_1$. Setting equal to $J^1 = j_1$: $(\nabla\times\vec B)_1 - \partial_t E_1 = j_1$. Similarly for $\nu = 2, 3$, giving $\nabla\times\vec B - \partial_t\vec E = \vec j$, Ampère–Maxwell.

> [!note]- Lemma 3: Charge conservation $\partial_\mu J^\mu = 0$ from the Maxwell pair
> **Statement:** For $G = U(1)$, the Maxwell equations $\partial_\mu F^{\mu\nu} = J^\nu$ imply $\partial_\nu J^\nu = 0$.
>
> **Hint:** Apply $\partial_\nu$ to both sides; the LHS gives $\partial_\nu\partial_\mu F^{\mu\nu}$, which vanishes by the antisymmetry of $F^{\mu\nu}$.
>
> **Why needed:** This is the famous charge conservation following from Maxwell's equations alone — the same content as the abelian Noether current $J^\mu = -e\bar\psi\gamma^\mu\psi$ being conserved.
>
> > [!note]- Full proof
> > Compute $\partial_\nu\partial_\mu F^{\mu\nu}$. Since partial derivatives commute, $\partial_\nu\partial_\mu = \partial_\mu\partial_\nu$. Since $F^{\mu\nu} = -F^{\nu\mu}$ is antisymmetric, the sum over $\mu, \nu$ gives $\partial_\nu\partial_\mu F^{\mu\nu} = -\partial_\nu\partial_\mu F^{\nu\mu} = -\partial_\mu\partial_\nu F^{\nu\mu} = -\partial_\nu\partial_\mu F^{\mu\nu}$ (renaming dummies). Hence $\partial_\nu\partial_\mu F^{\mu\nu} = -\partial_\nu\partial_\mu F^{\mu\nu}$, forcing $\partial_\nu\partial_\mu F^{\mu\nu} = 0$. So $\partial_\nu J^\nu = \partial_\nu\partial_\mu F^{\mu\nu} = 0$, charge conservation. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Take $G = U(1)$ on Minkowski $\mathbb{R}^{1,3}$ with the signature convention $(-,+,+,+)$, and the EM identifications $F_{0i} = -E_i$, $F_{ij} = \epsilon_{ijk}B_k$, $A^\mu = (\phi, \vec A)$, $J^\mu = (\rho, \vec j)$.
>
> *Step 1 — Bianchi identity gives Faraday + no-monopole.* By Lemma 1, the four component equations of $dF = 0$ are: $\nabla\cdot\vec B = 0$ (one equation) and $\partial_t\vec B + \nabla\times\vec E = 0$ (three equations). These are the two "homogeneous" Maxwell equations.
>
> *Step 2 — Yang–Mills equation gives Gauss + Ampère–Maxwell.* By Lemma 2, the four component equations of $d\star F = \star J$ (equivalently $\partial_\mu F^{\mu\nu} = J^\nu$) are: $\nabla\cdot\vec E = \rho$ (one equation) and $\nabla\times\vec B - \partial_t\vec E = \vec j$ (three equations). These are the two "inhomogeneous" Maxwell equations.
>
> *Step 3 — Combining gives all four Maxwell equations.* Together, the pair (Bianchi, YM) for $G = U(1)$ on Minkowski space reproduces the complete set of Maxwell's equations, expressed in differential-form language as a first-order system on $F$.
>
> *Step 4 — Non-abelian generalisation.* For arbitrary compact $G$, $F = dA - iqA\wedge A$ has the extra commutator term, and the covariant derivative $d_A = d + [\omega, \cdot]$ replaces $d$. The four component equations of $d_A F = 0$ are: $\partial_{[\mu}F_{\nu\rho]} - iq[A_{[\mu}, F_{\nu\rho]}] = 0$ (Bianchi). The four component equations of $d_A\star F = \star J$ are: $\partial_\mu F^{\mu\nu} - iq[A_\mu, F^{\mu\nu}] = J^\nu$ (Yang–Mills with source). For $G = U(1)$ the commutator term vanishes and these reduce to Maxwell. For non-abelian $G$, the commutator term is the new feature, encoding gauge-field self-interaction.
>
> *Step 5 — Charge conservation.* By Lemma 3 (abelian case) or its non-abelian generalisation (apply $d_A$ to $d_A\star F = \star J$ and use the on-shell vanishing of $d_A^2\star F = [F, \star F]$ via Bianchi), the source satisfies $d_A\star J = 0$, equivalently $\partial_\mu J^\mu = 0$ for $G = U(1)$ or $\nabla_\mu J^\mu - iq[A_\mu, J^\mu] = 0$ for non-abelian $G$. This is charge conservation.
>
> The non-abelian charge conservation is *covariant* rather than ordinary — the current is conserved up to gauge rotation. For confined gauge theories like QCD, this distinction has physical consequences: there is no gauge-invariant local "colour current density", only gauge-invariant integrated colour charges. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Application 1 — Wave equation for electromagnetic radiation.** Imposing the Lorenz gauge $\partial_\mu A^\mu = 0$ on the Maxwell equations and combining with the YM equation $\partial_\mu F^{\mu\nu} = J^\nu$ produces $\partial^2 A^\nu = J^\nu$, the wave equation. Source-free solutions ($J = 0$) are plane waves $A^\nu = \epsilon^\nu e^{ik\cdot x}$ with $k^2 = 0$ (null wave vector), giving electromagnetic radiation propagating at the speed of light. The polarisation vector $\epsilon^\nu$ has two physical components (the gauge condition removes one and the equation of motion removes another), corresponding to the two photon helicities $\pm 1$.

**Application 2 — Dirac monopole and quantisation.** The Dirac magnetic monopole has $\vec B = (g/4\pi r^2)\hat r$ on $\mathbb{R}^3\setminus\{0\}$, satisfying $\nabla\cdot\vec B = g\delta^3(\vec x)$ (a magnetic *source*). The Maxwell equation $\nabla\cdot\vec B = 0$ is violated at the origin, but the field is consistent away from the origin. The vector potential $\vec A$ producing this field cannot be globally defined as a smooth 1-form on $\mathbb{R}^3\setminus\{0\}$ — it has a *string singularity* along a half-axis. The **Dirac quantisation condition** $eg = 2\pi n\hbar$ for integer $n$ is the requirement that the string be invisible to electron wavefunctions (a phase shift of integer-multiple of $2\pi$ across the string). This is the source of *all* charge quantisation in quantum mechanics. See [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

**Application 3 — Non-abelian magnetic monopole ('t Hooft–Polyakov).** When a non-abelian gauge group $G = SU(2)$ is spontaneously broken to $U(1)$ by a Higgs field $\Phi$, the resulting $U(1)$ gauge field can have magnetic charge — but unlike the abelian Dirac monopole, this 't Hooft–Polyakov monopole is *non-singular*, being a regular soliton solution of the coupled Yang–Mills–Higgs system. The magnetic charge is automatically quantised (no need for the Dirac argument) because the gauge group structure constraints it: the asymptotic Higgs field defines a map $S^2_\infty \to G/H = SU(2)/U(1) = S^2$, classified by $\pi_2(S^2) = \mathbb{Z}$.

---

# Bridges

- **Connection to [[Thm - Yang-Mills Equation from the Action Principle]]:** The YM equation $d_A\star F = \star J$ is derived from the variational principle applied to the YM action plus matter source. The Bianchi identity $d_A F = 0$ holds for *every* connection, not just YM critical points — it is an algebraic identity from $F$ being a curvature. The pair (Bianchi, YM) is therefore *automatic for any solution of the variational principle*.

- **Connection to the [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition|Hodge decomposition]]:** On a compact Riemannian 4-manifold, every 2-form $\omega$ decomposes uniquely as $\omega = d\alpha + d^*\beta + \gamma$ with $\gamma$ harmonic. For $\omega = F$ a Yang–Mills field strength (on the abelian case for simplicity), the Bianchi identity $dF = 0$ forces $F$ to be in the kernel of $d$, i.e., $F$ has no $d^*\beta$ component. The YM equation $d^*F = 0$ then forces $F$ to be in the kernel of $d^*$ as well. So a YM field strength is *harmonic*: $\Delta F = 0$. This connects Yang–Mills theory directly to Hodge theory and the topology of the underlying manifold.

- **Connection to [[Algebraic Topology III — Higher Homotopy and Chern Forms|the topology of G-bundles]]:** The Bianchi identity $dF = 0$ (abelian case) means $F$ is a closed 2-form, hence represents a class $[F] \in H^2_{\text{dR}}(M)$. For $G = U(1)$ this is the **first Chern class** $c_1(P) \in H^2(M; \mathbb{Z})$ — a topological invariant classifying the principal $U(1)$-bundle $P$. The integrality of $c_1$ (after dividing by $2\pi$) explains why magnetic flux is quantised in units of $2\pi\hbar/e$. For non-abelian $G$, $\operatorname{tr}(F\wedge F)$ is a closed 4-form representing the **second Chern class**, integer-valued and classifying the principal bundle up to topology.

- **Connection to General Relativity:** Einstein's equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ have the same broad structure: a "field equation" $G_{\mu\nu} = T_{\mu\nu}$ paired with a "Bianchi-like identity" $\nabla_\mu G^{\mu\nu} = 0$ (the contracted Bianchi identity for the Riemann tensor), which forces $\nabla_\mu T^{\mu\nu} = 0$ — covariant conservation of energy-momentum. The structural parallel: in YM the Bianchi identity for the curvature implies conservation of the source current; in GR, the Bianchi identity for the Riemann tensor implies conservation of the energy-momentum tensor. The same mechanism. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Unlocked by This

> [!tip] Magnetic Monopoles and the Topology of $U(1)$-Bundles *(from Differential Topology)*
> The Dirac monopole on $\mathbb{R}^3\setminus\{0\}$ is the **first non-trivial example of a non-trivial principal $U(1)$-bundle** in physics: there is no globally smooth vector potential producing the monopole's magnetic field, only patch-wise potentials related by a non-trivial transition function (the "Dirac string"). The bundle in question is the **Hopf bundle** $S^3 \to S^2$, with the magnetic charge being the *first Chern number* $c_1 = \pm 1$ of the line bundle associated to the Hopf bundle by the standard $U(1)$-representation. The Dirac quantisation condition $eg = 2\pi n\hbar$ is then the statement that physical line bundles have integer Chern number — a topological fact, not a quantum-mechanical one. This is one of the earliest examples in physics where *topology determines quantisation*.

> [!tip] The Wu–Yang Description of the Magnetic Monopole *(from Differential Geometry)*
> Wu and Yang (1975) gave the manifestly gauge-invariant description of the Dirac monopole: cover $S^2$ by two charts (north patch $U_N = S^2\setminus\{\text{south pole}\}$ and south patch $U_S = S^2\setminus\{\text{north pole}\}$), and define different vector potentials $\vec A_N$ and $\vec A_S$ on each patch, related on the overlap $U_N\cap U_S = S^2\setminus\{\text{poles}\}$ by a gauge transformation $\vec A_S = \vec A_N + (e/g)\nabla\Lambda$ for some $\Lambda$. The compatibility condition is that $\Lambda$ must be single-valued modulo $2\pi/eg$, giving the Dirac quantisation. This construction is the simplest example of a *principal bundle in physics described by transition functions* and is the seed of the modern *principal-bundle* formulation of gauge theory.
