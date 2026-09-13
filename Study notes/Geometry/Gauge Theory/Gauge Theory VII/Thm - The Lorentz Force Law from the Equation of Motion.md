---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Worldline, Equation of Motion of a Charged Particle, and Relativistic Mass"
  - "Thm - Solutions of the Lorentz Force Equation Have Constant Speed and Exist Uniquely"
  - "Def - Hodge Star in Arbitrary Signature"
  - "Def - Musical Isomorphism (Flat and Sharp)"
  - "Def - Levi-Civita Connection"
  - "Def - Covariant Derivative along a Curve"
tags: [geometry, gauge-theory, electromagnetism]
---

# Notation

We work on **Minkowski space** $M = \mathbb{R}^{1,3}$: the manifold $\mathbb{R}^4$ with standard coordinates $(t, x, y, z) = (x^0, x^1, x^2, x^3)$ and the constant Lorentzian inner product $\langle\cdot,\cdot\rangle$ of signature $(-,+,+,+)$, so that $\langle\partial_t, \partial_t\rangle = -1$, $\langle\partial_{x^i}, \partial_{x^j}\rangle = \delta_{ij}$ for $i, j \in \{1,2,3\}$, and all mixed products vanish. This is the signature and unit convention ($c = 1$) fixed for the whole electrodynamics section; see the standing-convention note below. The volume form is $\mathrm{vol} = dt \wedge dx \wedge dy \wedge dz$ and the index (number of negative directions) is $p = 1$.

A **worldline** is a smooth curve $c : I \to M$ on an interval $I \subseteq \mathbb{R}$, written in coordinates $c(\tau) = \big(t(\tau), \vec c(\tau)\big)$ with $\vec c = (x, y, z)$ the spatial part. A prime always denotes the derivative with respect to the worldline parameter $\tau$, so $c' = dc/d\tau = \big(t', \vec c\,'\big)$ and $\vec c\,'' = d^2\vec c/d\tau^2$. The curve is **timelike** if $\langle c', c'\rangle < 0$; it is parametrised by **eigentime** (proper time) if $\langle c', c'\rangle = -1$, and we take the future orientation $t' > 0$. The **observed velocity** relative to the coordinate frame is $\vec v := d\vec c/dt = \vec c\,'/t'$, a vector in $\mathbb{R}^3$; timelikeness forces $|\vec v| < 1$, established on [[Def - Worldline, Equation of Motion of a Charged Particle, and Relativistic Mass|the worldline page]].

The **electromagnetic field strength** is the real $2$-form $F \in \Omega^2(M; \mathbb{R})$ whose electric and magnetic coefficients relative to the coordinates $(t, x, y, z)$ are, as fixed on [[Def - U(1) Gauge Field and Electromagnetic Connection|the electromagnetic-connection page]],
$$F = E_x\, dx \wedge dt + E_y\, dy \wedge dt + E_z\, dz \wedge dt + B_x\, dy \wedge dz + B_y\, dz \wedge dx + B_z\, dx \wedge dy,$$
with $\vec E = (E_x, E_y, E_z)$ and $\vec B = (B_x, B_y, B_z)$ smooth $\mathbb{R}^3$-valued functions of the spacetime point. The symbol $\langle\cdot,\cdot\rangle$ applied to two spatial vectors, as in $\langle\vec c\,', \vec E\rangle$, means the Euclidean dot product on $\mathbb{R}^3$; $\times$ is the Euclidean cross product on $\mathbb{R}^3$, with $(\vec B \times \vec c\,')_x = B_y z' - B_z y'$ and cyclically. The **sharp** $\eta^\sharp \in T_qM$ of a covector $\eta \in T_q^*M$ is the vector dual to $\eta$ under the metric, defined by $\eta(Y) = \langle\eta^\sharp, Y\rangle$ for all $Y \in T_qM$; this is the [[Def - Musical Isomorphism (Flat and Sharp)|musical isomorphism]] for the Lorentzian metric. The symbol $F(c', \cdot)$ denotes the $1$-form $Y \mapsto F(c', Y)$, that is, the interior product $\iota_{c'}F$.

Along the worldline, $\frac{\nabla}{d\tau}$ is the [[Def - Covariant Derivative along a Curve|covariant derivative along $c$]] for the [[Def - Levi-Civita Connection|Levi-Civita connection]] of $\langle\cdot,\cdot\rangle$. The test particle carries **rest mass** $m_0 = 1$ and **charge** $1$, and its **relativistic mass** is $m := m_0/\sqrt{1 - |\vec v|^2}$; under eigentime parametrisation this equals $m_0 t' = t'$, a fact proved on [[Def - Worldline, Equation of Motion of a Charged Particle, and Relativistic Mass|the worldline page]] and recalled in Lemma 5.

> [!warning] Convention: signature and units versus the special-relativity notes
> This page uses Bär's conventions: signature $(-,+,+,+)$, natural units $c = 1$, and unit rest mass and charge. The vault's special-relativity pages, in particular [[Def - The Lorentz Four-Force|the Lorentz four-force page]], use the opposite metric convention $(+,-,-,-)$, keep $c$ and the charge $q$ explicit, and work in SI units. The dictionary is: the metrics are related by $g_B = -g_{\mathrm{SR}}$, the field strength $F$ is the **same** $2$-form and the fields $\vec E, \vec B$ are the **same** functions in both, and on Minkowski space the Hodge stars satisfy $\star_B = -\star_V$. Because $g_B = -g_{\mathrm{SR}}$, timelike vectors satisfy $\langle c', c'\rangle < 0$ here but $\langle U, U\rangle > 0$ there, and the sharp differs by an overall sign on covectors; these two sign reversals cancel in the equation of motion, which is why both conventions produce the identical physical law $\frac{d}{dt}(m\vec v) = \vec E + \vec v \times \vec B$.

---

# Statement

> **Theorem (the Lorentz force law from the equation of motion).** Let $F$ be an electromagnetic field strength on Minkowski space $M = \mathbb{R}^{1,3}$, and let $c(\tau) = \big(t(\tau), \vec c(\tau)\big)$ be a timelike worldline parametrised by eigentime, $\langle c', c'\rangle = -1$ and $t' > 0$. Then the equation of motion of the test particle,
> $$\frac{\nabla}{d\tau} c' + F(c', \cdot)^\sharp = 0, \tag{3.12}$$
> is equivalent, in the standard coordinates, to the pair of vector equations
> $$t'' - \langle\vec c\,', \vec E\rangle = 0, \qquad\qquad \vec c\,'' - t'\,\vec E + \vec B \times \vec c\,' = 0.$$
> Moreover the first (temporal) equation is a consequence of the second (spatial) equation together with the eigentime constraint $\langle c', c'\rangle = -1$, so the content of $(3.12)$ is carried entirely by the spatial equation. Dividing the spatial equation by $t' > 0$ and using $m = m_0 t' = t'$ and $\vec v = \vec c\,'/t'$ yields the **Lorentz force law**
> $$\frac{d}{dt}\big(m\,\vec v\big) = \vec E + \vec v \times \vec B. \tag{3.13}$$

> [!warning] Convention: a sign typo in the source and in the page inventory
> Bär prints the temporal equation with a plus sign, "$t'' + \langle\vec c\,', \vec E\rangle = 0$" (p. 89), and the manifest inventory for this page reproduces that plus sign. This is a transcription slip: Bär's own componentwise computation gives $F(c', \cdot)^\sharp = -\langle\vec c\,', \vec E\rangle\,\partial_t + (\ldots)$, whose $\partial_t$-coefficient is $-\langle\vec c\,', \vec E\rangle$, so the equation of motion forces $t'' - \langle\vec c\,', \vec E\rangle = 0$. The minus sign is also exactly what the announced reduction "the first equation follows from the second by scalar multiplication with $\vec v$" produces (Lemma 4). We therefore state and prove the temporal equation with the corrected minus sign. Two further slips in the same paragraph are corrected below: Bär prints "$\vec v\,''$" for $\vec c\,''$ in the spatial equation, and "$\tfrac{d}{dt}\langle c', c'\rangle$" for the $\tau$-derivative $\tfrac{d}{d\tau}\langle c', c'\rangle$ in the reduction, and "$t' = \langle\vec v, \vec c\,''\rangle$" for $t'' = \langle\vec v, \vec c\,''\rangle$.

---

# Motivation

The equation of motion $(3.12)$ is a single, manifestly coordinate-free statement: it says that the covariant acceleration $\frac{\nabla}{d\tau}c'$ of the worldline is minus the sharp of the force one-form $F(c', \cdot)$. Its virtue is exactly its invariance — it holds in every chart of every Lorentzian $4$-manifold, and on [[Thm - Solutions of the Lorentz Force Equation Have Constant Speed and Exist Uniquely|the previous page]] it is what makes constancy of speed and existence-uniqueness of trajectories immediate. Its defect, for someone who wants to *use* it, is that it hides the physics inside the geometric machinery of connections, sharps, and interior products. Nobody predicts the path of an electron in a magnetic field by writing $\frac{\nabla}{d\tau}c' + F(c', \cdot)^\sharp = 0$; they write "mass times acceleration equals $\vec E + \vec v \times \vec B$" and integrate.

This theorem is the bridge between the two descriptions. It answers the question: *when we unpack the invariant equation of motion in an inertial frame, what do we get?* The answer is the nineteenth-century Lorentz force law, exactly as measured in the laboratory, with the relativistic mass $m = m_0 t'$ appearing in the right place. That the covariant equation reproduces the elementary law is not automatic — it requires that the electric field sit in the $dx^i \wedge dt$ block of $F$ and the magnetic field in the purely spatial block, that the sharp on Minkowski flip the sign of the time component, and that the eigentime constraint make the temporal equation redundant. Verifying all of this is the point.

There is a second reason the theorem matters, internal to the gauge-theoretic development. The whole of §7.2 recasts electrodynamics as the theory of a connection on a principal $U(1)$-bundle: the field $F$ is a curvature, the Maxwell equations are $dF = 0$ and $d \star F + J = 0$, and the source-free dynamics come from a variational principle. The equation of motion $(3.12)$ is the one place where the *matter* — a charged test particle — couples to the connection. Showing that this coupling reduces to the familiar force law confirms that the abstract picture has not silently changed the physics; it is the sanity check that ties the bundle language back to what a charged particle actually does.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is "a timelike eigentime worldline solving $(3.12)$ on Minkowski space". The disguised inputs are the situations that hand you such a worldline without naming one.

The first disguised source is **any timelike solution of $(3.12)$ under an arbitrary admissible parametrisation**. A problem rarely presents a curve already normalised to $\langle c', c'\rangle = -1$; it presents a solution of the equation of motion with some initial data. The bridge $B \Rightarrow A$ is the constant-speed theorem: [[Thm - Solutions of the Lorentz Force Equation Have Constant Speed and Exist Uniquely|any solution of $(3.12)$ that is timelike at one instant has $\langle c', c'\rangle$ constant and is timelike throughout]], so after an affine reparametrisation $\tau \mapsto a\tau + b$ and, if necessary, a reversal $\tau \mapsto -\tau$, it satisfies $\langle c', c'\rangle = -1$ and $t' > 0$ — the hypothesis of this theorem — without any loss. The non-obvious point is that one may impose eigentime *freely*, precisely because the force is skew and does no work. *Example problem:* given the trajectory of a charge released from rest in a uniform field, reparametrise to eigentime and read off the lab-frame acceleration from $(3.13)$.

The second disguised source is **a charged particle coupled to a connection on an associated bundle**. In the gauge-theoretic setting the force one-form $F(c', \cdot)$ is the contraction of the curvature of a $U(1)$-connection with the velocity; a problem may hand you the connection and the bundle rather than the field $F$. The bridge is that for a $U(1)$-bundle the curvature descends to a global real $2$-form $F$ on the base (the adjoint action being trivial), so the abstract coupling *is* an electromagnetic field strength in the sense used here, and $(3.12)$ applies verbatim once a trivialisation supplies coordinates. *Example problem:* a monopole background presented as a nontrivial line bundle over $\mathbb{R}^3 \setminus \{0\}$ still governs test charges by $(3.13)$ on any contractible chart.

The third disguised source is **the geodesic equation with a first-order perturbation**. Any second-order ODE of the shape $\ddot c^k + \Gamma^k_{ij}\dot c^i \dot c^j = -\text{(linear in }\dot c)$ is the equation of motion of *some* skew force. The bridge is that a velocity-linear right-hand side that is skew in the appropriate sense (metrically, $\langle \text{force}, c'\rangle = 0$) is realised by a $2$-form $F$ via $F(c', \cdot)^\sharp$, so the trajectory is a Lorentz-force trajectory for that $F$; on flat Minkowski the Christoffel term drops and the equation is exactly $(3.12)$. The non-obviousness is recognising a metric-skew velocity-linear force as an electromagnetic one. *Example problem:* a rotating-frame Coriolis-type term can, on the flat model, be absorbed into an effective magnetic field.

**Targets (Output Amplification).** The bare conclusion is the pair of vector equations and the force law $(3.13)$.

Combine $(3.13)$ with **a specific field configuration** and you get an explicit ODE system that can be integrated. With $\vec E = 0$ and $\vec B$ constant, the force law is $\frac{d}{dt}(t'\vec v) = \vec v \times \vec B$; because $m = t'$ is then constant (the magnetic field does no work, so the energy $t'$ is conserved), this reduces to uniform circular motion at the cyclotron frequency, the payoff being the quantitative prediction $|\vec v| = \text{const}$ and radius $|\vec v|/|\vec B|$. The extra ingredient is the conservation of $t'$, itself the temporal equation of this theorem with $\vec E = 0$.

Combine the theorem with **the covariant form of the four-force** and you recover the special-relativistic statement. Contracting $(3.12)$ with $c'$ gives the pure-force identity $\langle F(c', \cdot)^\sharp, c'\rangle = F(c', c') = 0$, so the electromagnetic force never changes the rest mass; combined with the temporal equation this is the statement that only $\vec E$ does work, at rate $\langle\vec c\,', \vec E\rangle$. The payoff is the energy balance $\frac{dm}{dt} = \langle\vec v, \vec E\rangle$, whose extra ingredient is the antisymmetry of $F$, and which is the bridge to [[Def - The Lorentz Four-Force|the four-force description]].

Combine the theorem with **the non-relativistic limit** $|\vec v| \ll 1$ and you recover Newtonian electrodynamics. In that limit $t' = 1/\sqrt{1 - |\vec v|^2} \to 1$, so $m \to m_0$ is constant and eigentime $\tau$ agrees with coordinate time $t$; the force law $(3.13)$ becomes $m_0\,\ddot{\vec c} = \vec E + \vec v \times \vec B$, the textbook equation. The extra ingredient is the expansion of $t'$, and the payoff is the identification of the classical Lorentz force as the slow-particle shadow of the covariant law.

---

# Why Is It True

Set aside the computation and picture the equation of motion as one four-vector equation with a time slot and three space slots. The left-hand side $\frac{\nabla}{d\tau}c'$ is, on flat Minkowski, just the ordinary acceleration $(t'', \vec c\,'')$, because the standard coordinates are affine for the flat metric and the Christoffel symbols vanish. The right-hand side is the sharp of the force one-form $F(c', \cdot)$. Everything hinges on which components of $F$ feed which slot of that one-form, and on the sign the Lorentzian sharp attaches to the time slot.

The magnetic and electric fields occupy structurally different blocks of $F$. The electric field lives in the "mixed" $dx^i \wedge dt$ block: contracting $F$ with the time part $t'\partial_t$ of the velocity pulls a $dx^i$ out of that block, producing the spatial term $-t'\vec E$; contracting with the space part $\vec c\,'$ pulls a $dt$ out, producing the temporal term $+\langle\vec c\,', \vec E\rangle\,dt$. The magnetic field lives in the purely spatial block $dy \wedge dz$, and so on; contracting it with the space part of the velocity produces the cross product $\vec B \times \vec c\,'$, and it contributes nothing to the time slot because it has no $dt$. This is the geometric content of the statement that the spatial block of $F$ is the Hodge dual of $\vec B$: duality in three space dimensions is exactly the cross product, so contraction with a velocity yields $\vec B \times \vec c\,'$.

Now apply the sharp. On the spatial covectors $dx^i$ the sharp is the identity, so the spatial force one-form passes to $-t'\vec E + \vec B \times \vec c\,'$ unchanged. On $dt$ the Lorentzian sharp gives $dt^\sharp = -\partial_t$, the single sign that distinguishes Minkowski from Euclidean space; this flips the temporal coefficient from $+\langle\vec c\,', \vec E\rangle$ to $-\langle\vec c\,', \vec E\rangle\,\partial_t$. Matching components of $(t'', \vec c\,'') + F(c', \cdot)^\sharp = 0$ then gives the temporal equation $t'' - \langle\vec c\,', \vec E\rangle = 0$ and the spatial equation $\vec c\,'' - t'\vec E + \vec B \times \vec c\,' = 0$.

Finally, why is the temporal equation redundant? Because eigentime pins the speed: $\langle c', c'\rangle = -1$ is a constraint, and differentiating it relates $t''$ to the spatial data, exactly reproducing the temporal equation from the spatial one. Physically, the temporal equation is the energy-balance equation $\frac{dm}{dt} = \langle\vec v, \vec E\rangle$, and energy balance is not independent dynamics once you have fixed the speed and know the spatial force.

**In one sentence: the equation of motion is one covariant four-vector equation, and unpacking it in a lab frame — electric field in the mixed block, magnetic field in the spatial block as the dual of $\vec B$, the Lorentzian sharp flipping the time slot — turns it into the classical Lorentz force law together with a redundant energy-balance equation.**

---

# What Makes This Hard

The one genuinely non-obvious step is the sign that the Lorentzian sharp attaches to the time component: on $(-,+,+,+)$ one has $dt^\sharp = -\partial_t$ while $dx^\sharp = \partial_x$, and forgetting this reverses the temporal equation and breaks the redundancy argument — this is precisely the slip in the printed source. The second trap is bookkeeping in the interior product $\iota_{c'}F$: with six terms in $F$ and four in $c'$, the temptation is to lose or mis-sign a magnetic term, and the check that the three spatial coefficients assemble into $-t'\vec E + \vec B \times \vec c\,'$ must be done component by component against the cross-product convention. The third subtlety is that "the temporal equation follows from the spatial one" is a statement about *solutions constrained to eigentime*, not an algebraic identity between the four component equations; it uses the constraint $\langle c', c'\rangle = -1$ and the skewness $\langle \vec B \times \vec c\,', \vec c\,'\rangle = 0$, and omitting either makes the deduction fail.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** On flat Minkowski the covariant acceleration is the coordinate second derivative, so the left-hand side of $(3.12)$ is $(t'', \vec c\,'')$. Compute the right-hand side by taking the interior product of $F$ with $c'$ and then applying the sharp, keeping careful track of the sign $dt^\sharp = -\partial_t$. Match components to obtain the two vector equations, show the temporal one follows from the spatial one via the eigentime constraint, and rescale the spatial one by $t'$ to reach $(3.13)$.

**Subgoal decomposition:**

1. **Reduce the left-hand side.**
   - *Hint:* The standard coordinates are affine for the flat metric; all Christoffel symbols vanish, so $\frac{\nabla}{d\tau}c'$ has components $\ddot c^k$.
   - *Why needed:* It turns the geometric acceleration into the elementary $(t'', \vec c\,'')$, which is what the physical law is stated in.

2. **Find the sharp of the coframe.**
   - *Hint:* Solve $\langle (dx^\mu)^\sharp, \partial_\nu\rangle = \delta^\mu_\nu$; the diagonal metric gives $dt^\sharp = -\partial_t$ and $(dx^i)^\sharp = \partial_{x^i}$.
   - *Why needed:* Every term of the force one-form must be pushed through the sharp, and the time sign is the crux.

3. **Contract $F$ with $c'$.**
   - *Hint:* Use $\iota_{c'}(\alpha \wedge \beta) = \alpha(c')\beta - \beta(c')\alpha$ on each of the six terms; collect coefficients of $dt, dx, dy, dz$.
   - *Why needed:* It produces the force one-form $F(c', \cdot)$ before sharping.

4. **Assemble $F(c', \cdot)^\sharp$ and match components.**
   - *Hint:* Apply Subgoal 2's sharps; recognise the spatial coefficients as $-t'\vec E + \vec B \times \vec c\,'$ and the temporal coefficient as $-\langle\vec c\,', \vec E\rangle$.
   - *Why needed:* Setting $(t'', \vec c\,'') + F(c', \cdot)^\sharp = 0$ componentwise is exactly the pair of vector equations.

5. **Show the temporal equation is redundant.**
   - *Hint:* Differentiate $\langle c', c'\rangle = -1$ to get $t't'' = \langle\vec c\,', \vec c\,''\rangle$; substitute the spatial equation and use $\langle\vec B \times \vec c\,', \vec c\,'\rangle = 0$.
   - *Why needed:* It isolates the spatial equation as the whole content of $(3.12)$.

6. **Rescale to the force law.**
   - *Hint:* Recall $m = m_0 t' = t'$ and $\vec v = \vec c\,'/t'$; then $\frac{d}{dt}(m\vec v) = \vec c\,''/t'$, and dividing the spatial equation by $t'$ gives $(3.13)$.
   - *Why needed:* It converts the eigentime-parametrised equation into the lab-frame law in coordinate time $t$.

---

# Lemma Decomposition

> [!note]- Lemma 1: On Minkowski space the covariant derivative along a curve is the coordinate second derivative
> **Statement:** For the Levi-Civita connection of the flat metric $\langle\cdot,\cdot\rangle$ on $M = \mathbb{R}^{1,3}$ in standard coordinates, and any smooth curve $c(\tau) = (c^0, c^1, c^2, c^3)(\tau)$, the covariant derivative of the velocity along the curve is $\frac{\nabla}{d\tau}c' = \sum_{k=0}^3 (c^k)''\,\partial_{x^k}\big|_{c(\tau)}$.
>
> **Hint:** The metric coefficients are constant, so the Christoffel symbols vanish; the general coordinate formula for $\frac{\nabla}{d\tau}c'$ then loses its connection term.
>
> **Why needed:** It converts the left-hand side of $(3.12)$ from a covariant acceleration into the ordinary second derivative $(t'', \vec c\,'')$ that appears in the physical law.
>
> > [!note]- Full proof
> > **The Christoffel symbols vanish.** By the [[Def - Levi-Civita Connection|Levi-Civita connection]] the Christoffel symbols in a coordinate chart are
> > $$\Gamma^k_{ij} = \tfrac12 \sum_l g^{kl}\big(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\big) \qquad \text{(Koszul formula in coordinates)},$$
> > where $g_{ij} = \langle\partial_{x^i}, \partial_{x^j}\rangle$ and $(g^{kl})$ is the inverse matrix. On Minkowski space in standard coordinates $g_{ij} = \operatorname{diag}(-1, 1, 1, 1)_{ij}$ is a **constant** matrix, so $\partial_i g_{jl} = 0$ for all $i, j, l$ (every partial derivative of a constant is zero). Hence $\Gamma^k_{ij} = 0$ for all $i, j, k$.
> >
> > **The connection term drops.** By [[Def - Covariant Derivative along a Curve|the definition of the covariant derivative along a curve]], writing $c' = \sum_i (c^i)'\,\partial_{x^i}$, its components are
> > $$\Big(\tfrac{\nabla}{d\tau}c'\Big)^k = (c^k)'' + \sum_{i,j} \Gamma^k_{ij}\,(c^i)'\,(c^j)' \qquad \text{(coordinate formula for the covariant derivative along $c$)}.$$
> > Substituting $\Gamma^k_{ij} = 0$ (just shown) leaves $\big(\tfrac{\nabla}{d\tau}c'\big)^k = (c^k)''$ for each $k$. Therefore $\frac{\nabla}{d\tau}c' = \sum_k (c^k)''\,\partial_{x^k}$, i.e. it has coordinate components $(t'', x'', y'', z'') = (t'', \vec c\,'')$. $\blacksquare$

> [!note]- Lemma 2: The sharp of the coframe on Minkowski space
> **Statement:** On $M = \mathbb{R}^{1,3}$ with signature $(-,+,+,+)$, the [[Def - Musical Isomorphism (Flat and Sharp)|sharp]] acts on the coordinate coframe by $dt^\sharp = -\partial_t$ and $(dx^i)^\sharp = \partial_{x^i}$ for $i \in \{1,2,3\}$. Consequently, for a one-form $\eta = \eta_0\, dt + \sum_i \eta_i\, dx^i$, one has $\eta^\sharp = -\eta_0\,\partial_t + \sum_i \eta_i\,\partial_{x^i}$.
>
> **Hint:** By definition $\eta^\sharp$ is the unique vector with $\langle\eta^\sharp, Y\rangle = \eta(Y)$ for all $Y$; test against each coordinate basis vector using the diagonal metric.
>
> **Why needed:** It is the single place the Lorentzian signature enters the reduction; the sign $dt^\sharp = -\partial_t$ is what fixes the temporal equation's sign.
>
> > [!note]- Full proof
> > **The defining equation.** By [[Def - Musical Isomorphism (Flat and Sharp)|the definition of the sharp]], $\eta^\sharp$ is the unique vector satisfying $\langle\eta^\sharp, Y\rangle = \eta(Y)$ for all $Y \in T_qM$; uniqueness holds because $\langle\cdot,\cdot\rangle$ is non-degenerate. It suffices to check the claimed values against the basis $\{\partial_t, \partial_x, \partial_y, \partial_z\}$, since a vector is determined by its inner products with a basis when the form is non-degenerate.
> >
> > **The time covector.** Put $V = -\partial_t$. For every basis vector $Y$,
> > $$\langle V, \partial_t\rangle = \langle -\partial_t, \partial_t\rangle = -(-1) = 1 = dt(\partial_t), \qquad \langle V, \partial_{x^i}\rangle = \langle -\partial_t, \partial_{x^i}\rangle = 0 = dt(\partial_{x^i}) \quad (i = 1,2,3),$$
> > using $\langle\partial_t, \partial_t\rangle = -1$ and $\langle\partial_t, \partial_{x^i}\rangle = 0$ (orthogonality of the coordinate frame). Thus $V$ represents $dt$, so $dt^\sharp = -\partial_t$.
> >
> > **The space covectors.** Fix $i \in \{1,2,3\}$ and put $W = \partial_{x^i}$. For every basis vector $Y$,
> > $$\langle W, \partial_{x^j}\rangle = \langle\partial_{x^i}, \partial_{x^j}\rangle = \delta_{ij} = dx^i(\partial_{x^j}), \qquad \langle W, \partial_t\rangle = \langle\partial_{x^i}, \partial_t\rangle = 0 = dx^i(\partial_t),$$
> > using $\langle\partial_{x^i}, \partial_{x^j}\rangle = \delta_{ij}$. Thus $W$ represents $dx^i$, so $(dx^i)^\sharp = \partial_{x^i}$.
> >
> > **The general covector.** The sharp is linear (it is the inverse of the linear flat map, [[Def - Musical Isomorphism (Flat and Sharp)|musical isomorphism]]), so for $\eta = \eta_0\, dt + \sum_i \eta_i\, dx^i$,
> > $$\eta^\sharp = \eta_0\,dt^\sharp + \sum_i \eta_i\,(dx^i)^\sharp = -\eta_0\,\partial_t + \sum_i \eta_i\,\partial_{x^i}. \qquad \blacksquare$$

> [!note]- Lemma 3: The contraction $F(c', \cdot)^\sharp$
> **Statement:** For $F = E_x\, dx \wedge dt + E_y\, dy \wedge dt + E_z\, dz \wedge dt + B_x\, dy \wedge dz + B_y\, dz \wedge dx + B_z\, dx \wedge dy$ and $c' = t'\partial_t + x'\partial_x + y'\partial_y + z'\partial_z$,
> $$F(c', \cdot) = \langle\vec c\,', \vec E\rangle\, dt + \sum_{i=1}^3 \big(-t' E_i + (\vec B \times \vec c\,')_i\big)\, dx^i, \qquad F(c', \cdot)^\sharp = -\langle\vec c\,', \vec E\rangle\,\partial_t + \big(-t'\vec E + \vec B \times \vec c\,'\big),$$
> where the last term is the vector $\sum_i (-t' E_i + (\vec B \times \vec c\,')_i)\,\partial_{x^i}$.
>
> **Hint:** Use $\iota_{c'}(\alpha \wedge \beta) = \alpha(c')\,\beta - \beta(c')\,\alpha$ on each of the six wedge terms, collect coefficients of $dt$ and each $dx^i$, then apply Lemma 2.
>
> **Why needed:** It is the entire right-hand side of $(3.12)$ written in coordinates; matching it against Lemma 1 produces the two vector equations.
>
> > [!note]- Full proof
> > **The interior product of a wedge.** For one-forms $\alpha, \beta$ and a vector $v$, $\iota_v(\alpha \wedge \beta) = \alpha(v)\,\beta - \beta(v)\,\alpha$ (contraction is an antiderivation of degree $-1$; on a two-fold wedge this is the stated identity). We apply it to each term of $F$ with $v = c'$, noting $dt(c') = t'$, $dx(c') = x'$, $dy(c') = y'$, $dz(c') = z'$.
> >
> > **The electric terms.** For the three mixed terms,
> > $$\iota_{c'}(E_x\, dx \wedge dt) = E_x\big(x'\, dt - t'\, dx\big), \quad \iota_{c'}(E_y\, dy \wedge dt) = E_y\big(y'\, dt - t'\, dy\big), \quad \iota_{c'}(E_z\, dz \wedge dt) = E_z\big(z'\, dt - t'\, dz\big),$$
> > each by the wedge identity. Their $dt$-parts sum to $(E_x x' + E_y y' + E_z z')\,dt = \langle\vec c\,', \vec E\rangle\,dt$, and their $dx^i$-parts contribute $-t'E_i$ to the coefficient of $dx^i$.
> >
> > **The magnetic terms.** For the three spatial terms,
> > $$\iota_{c'}(B_x\, dy \wedge dz) = B_x\big(y'\, dz - z'\, dy\big), \quad \iota_{c'}(B_y\, dz \wedge dx) = B_y\big(z'\, dx - x'\, dz\big), \quad \iota_{c'}(B_z\, dx \wedge dy) = B_z\big(x'\, dy - y'\, dx\big),$$
> > again by the wedge identity; these have no $dt$-part. Collecting the coefficient of each spatial covector:
> > $$dx : \quad B_y z' - B_z y' = (\vec B \times \vec c\,')_x, \qquad dy : \quad B_z x' - B_x z' = (\vec B \times \vec c\,')_y, \qquad dz : \quad B_x y' - B_y x' = (\vec B \times \vec c\,')_z,$$
> > by the definition of the cross product $(\vec B \times \vec c\,')_x = B_y z' - B_z y'$ and its cyclic images.
> >
> > **Assemble the one-form.** Adding the electric and magnetic contributions,
> > $$F(c', \cdot) = \langle\vec c\,', \vec E\rangle\, dt + \sum_{i=1}^3 \big(-t' E_i + (\vec B \times \vec c\,')_i\big)\, dx^i,$$
> > the coefficient of $dt$ coming only from the electric terms and the coefficient of each $dx^i$ combining the electric $-t'E_i$ with the magnetic $(\vec B \times \vec c\,')_i$.
> >
> > **Apply the sharp.** By Lemma 2, $dt^\sharp = -\partial_t$ and $(dx^i)^\sharp = \partial_{x^i}$, so
> > $$F(c', \cdot)^\sharp = \langle\vec c\,', \vec E\rangle\,(-\partial_t) + \sum_{i=1}^3 \big(-t' E_i + (\vec B \times \vec c\,')_i\big)\,\partial_{x^i} = -\langle\vec c\,', \vec E\rangle\,\partial_t + \big(-t'\vec E + \vec B \times \vec c\,'\big). \qquad \blacksquare$$

> [!note]- Lemma 4: The temporal equation follows from the spatial equation and the eigentime constraint
> **Statement:** Suppose $c$ is parametrised by eigentime, $\langle c', c'\rangle = -1$ with $t' > 0$, and satisfies the spatial equation $\vec c\,'' - t'\vec E + \vec B \times \vec c\,' = 0$. Then $t'' - \langle\vec c\,', \vec E\rangle = 0$.
>
> **Hint:** Differentiate the constraint $-t'^2 + |\vec c\,'|^2 = -1$ with respect to $\tau$ to relate $t''$ to $\langle\vec c\,', \vec c\,''\rangle$; then substitute the spatial equation and use $\langle\vec B \times \vec c\,', \vec c\,'\rangle = 0$.
>
> **Why needed:** It shows the four component equations of $(3.12)$ are not independent under eigentime: the temporal one is implied, so the spatial equation carries the full content.
>
> > [!note]- Full proof
> > **Differentiate the constraint.** In coordinates the eigentime condition reads $\langle c', c'\rangle = -(t')^2 + |\vec c\,'|^2 = -1$, a constant. Differentiating with respect to $\tau$,
> > $$0 = \frac{d}{d\tau}\big(-(t')^2 + |\vec c\,'|^2\big) = -2t't'' + 2\langle\vec c\,', \vec c\,''\rangle \qquad \text{(chain rule; } |\vec c\,'|^2 = \langle\vec c\,', \vec c\,'\rangle \text{ on } \mathbb{R}^3\text{)},$$
> > so, dividing by $2$,
> > $$t't'' = \langle\vec c\,', \vec c\,''\rangle. \tag{$\ast$}$$
> >
> > **Substitute the spatial equation.** The spatial equation gives $\vec c\,'' = t'\vec E - \vec B \times \vec c\,'$. Taking the Euclidean inner product with $\vec c\,'$,
> > $$\langle\vec c\,', \vec c\,''\rangle = t'\,\langle\vec c\,', \vec E\rangle - \langle\vec c\,', \vec B \times \vec c\,'\rangle = t'\,\langle\vec c\,', \vec E\rangle \qquad \text{(since } \langle\vec c\,', \vec B \times \vec c\,'\rangle = 0\text{)},$$
> > the cross product $\vec B \times \vec c\,'$ being orthogonal to $\vec c\,'$ (a vector is orthogonal to any cross product in which it appears).
> >
> > **Combine and cancel.** Substituting this into $(\ast)$ gives $t't'' = t'\,\langle\vec c\,', \vec E\rangle$. Since $t' > 0$ we may divide by $t'$, obtaining
> > $$t'' = \langle\vec c\,', \vec E\rangle, \qquad \text{i.e.} \qquad t'' - \langle\vec c\,', \vec E\rangle = 0. \qquad \blacksquare$$

> [!note]- Lemma 5: The kinematic rewriting of the momentum derivative
> **Statement:** Under eigentime parametrisation with $t' > 0$, rest mass $m_0 = 1$, relativistic mass $m = m_0 t' = t'$, and observed velocity $\vec v = \vec c\,'/t'$, one has $\frac{d}{dt}\big(m\vec v\big) = \frac{\vec c\,''}{t'}$, where $\frac{d}{dt} = \frac{1}{t'}\frac{d}{d\tau}$ is the derivative with respect to coordinate time.
>
> **Hint:** Simplify $m\vec v$ first — the factors of $t'$ cancel — and then convert the coordinate-time derivative to a $\tau$-derivative by the chain rule $dt/d\tau = t'$.
>
> **Why needed:** It turns the eigentime-parametrised spatial equation into the lab-frame force law $(3.13)$ expressed in coordinate time $t$.
>
> > [!note]- Full proof
> > **Simplify the momentum.** Using $m = m_0 t' = t'$ (the relativistic-mass identity under eigentime, proved on [[Def - Worldline, Equation of Motion of a Charged Particle, and Relativistic Mass|the worldline page]]: $1/\sqrt{1 - |\vec v|^2} = t'$) and $\vec v = \vec c\,'/t'$,
> > $$m\vec v = t' \cdot \frac{\vec c\,'}{t'} = \vec c\,' \qquad \text{(the two factors of } t' \text{ cancel; here } m_0 = 1\text{)}.$$
> >
> > **Convert the time derivative.** The relation $t = t(\tau)$ has $dt/d\tau = t' > 0$, so the coordinate-time derivative of a quantity $q(\tau)$ is $\frac{dq}{dt} = \frac{dq}{d\tau}\cdot\frac{d\tau}{dt} = \frac{1}{t'}\,q'$ (chain rule, with $d\tau/dt = 1/t'$). Applying this to $m\vec v = \vec c\,'$,
> > $$\frac{d}{dt}\big(m\vec v\big) = \frac{d}{dt}\vec c\,' = \frac{1}{t'}\,\frac{d}{d\tau}\vec c\,' = \frac{\vec c\,''}{t'}. \qquad \blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $c(\tau) = (t(\tau), \vec c(\tau))$ be a timelike worldline on Minkowski space, parametrised by eigentime so that $\langle c', c'\rangle = -1$ and $t' > 0$, and let $F$ be an electromagnetic field strength. We show that the equation of motion $\frac{\nabla}{d\tau}c' + F(c', \cdot)^\sharp = 0$ is equivalent to the two vector equations, that the temporal one is redundant, and that the spatial one is the Lorentz force law $(3.13)$.
>
> **Step 0 — the setup is well-posed.** The worldline is timelike at every instant and parametrised by eigentime, hypotheses that are consistent: by [[Thm - Solutions of the Lorentz Force Equation Have Constant Speed and Exist Uniquely|the constant-speed theorem]] — *every solution of $(3.12)$ that is timelike at one instant has $\langle c', c'\rangle$ constant, so can be affinely reparametrised to $\langle c', c'\rangle = -1$ with $t' > 0$* — this normalisation entails no loss of generality. The observed velocity $\vec v = \vec c\,'/t'$ is defined because $t' > 0$, and satisfies $|\vec v| < 1$ by timelikeness. The relativistic mass $m = m_0/\sqrt{1 - |\vec v|^2}$ is therefore finite and equals $m_0 t' = t'$.
>
> **Step 1 — reduce the left-hand side.** By Lemma 1, the standard coordinates are affine for the flat Minkowski metric, so all Christoffel symbols vanish and
> $$\frac{\nabla}{d\tau}c' = t''\,\partial_t + \vec c\,'' = (t'', \vec c\,''),$$
> where $\vec c\,'' = (x'', y'', z'')$ denotes the spatial part.
>
> **Step 2 — reduce the right-hand side.** By Lemma 3, contracting $F$ with $c'$ and applying the sharp (with $dt^\sharp = -\partial_t$, $(dx^i)^\sharp = \partial_{x^i}$ from Lemma 2) gives
> $$F(c', \cdot)^\sharp = -\langle\vec c\,', \vec E\rangle\,\partial_t + \big(-t'\vec E + \vec B \times \vec c\,'\big),$$
> the second summand being the spatial vector $\sum_i(-t'E_i + (\vec B \times \vec c\,')_i)\,\partial_{x^i}$.
>
> **Step 3 — match components.** Adding Steps 1 and 2 and setting the result to zero, the equation of motion $(3.12)$ becomes
> $$\big(t'' - \langle\vec c\,', \vec E\rangle\big)\,\partial_t + \big(\vec c\,'' - t'\vec E + \vec B \times \vec c\,'\big) = 0.$$
> Since $\{\partial_t, \partial_x, \partial_y, \partial_z\}$ is a basis, a vector vanishes if and only if each of its components vanishes. Hence $(3.12)$ holds if and only if both
> $$t'' - \langle\vec c\,', \vec E\rangle = 0 \qquad \text{(temporal)} \qquad\text{and}\qquad \vec c\,'' - t'\vec E + \vec B \times \vec c\,' = 0 \qquad \text{(spatial)}$$
> hold. This is the claimed pair of vector equations. (Bär prints the temporal equation with a plus sign; the componentwise computation of Step 2 gives the coefficient $-\langle\vec c\,', \vec E\rangle$ of $\partial_t$, so the correct sign is minus, as recorded in the Statement's convention callout.)
>
> **Step 4 — the temporal equation is redundant.** Assume the spatial equation and the eigentime constraint. By Lemma 4, differentiating $\langle c', c'\rangle = -1$ yields $t't'' = \langle\vec c\,', \vec c\,''\rangle$, and substituting $\vec c\,'' = t'\vec E - \vec B \times \vec c\,'$ together with the orthogonality $\langle\vec c\,', \vec B \times \vec c\,'\rangle = 0$ gives $t't'' = t'\langle\vec c\,', \vec E\rangle$; dividing by $t' > 0$ recovers exactly $t'' - \langle\vec c\,', \vec E\rangle = 0$, the temporal equation. Therefore, for an eigentime-parametrised worldline, the spatial equation already implies the temporal one, and $(3.12)$ is equivalent to the spatial equation alone.
>
> **Step 5 — obtain the Lorentz force law.** Start from the spatial equation $\vec c\,'' - t'\vec E + \vec B \times \vec c\,' = 0$ and divide by $t' > 0$:
> $$\frac{\vec c\,''}{t'} - \vec E + \frac{\vec B \times \vec c\,'}{t'} = 0 \qquad \text{(divide each term by } t'\text{)}.$$
> Now $\frac{\vec B \times \vec c\,'}{t'} = \vec B \times \frac{\vec c\,'}{t'} = \vec B \times \vec v$ (bilinearity of the cross product, definition $\vec v = \vec c\,'/t'$), and by Lemma 5, $\frac{\vec c\,''}{t'} = \frac{d}{dt}(m\vec v)$. Substituting,
> $$\frac{d}{dt}\big(m\vec v\big) - \vec E + \vec B \times \vec v = 0 \qquad \Longleftrightarrow \qquad \frac{d}{dt}\big(m\vec v\big) = \vec E - \vec B \times \vec v = \vec E + \vec v \times \vec B,$$
> the last equality by antisymmetry of the cross product ($\vec B \times \vec v = -\vec v \times \vec B$). This is the Lorentz force law $(3.13)$.
>
> **Conclusion.** The equation of motion $(3.12)$ is equivalent to the temporal and spatial vector equations; under eigentime the temporal equation follows from the spatial one and the constraint; and the spatial equation, rescaled by $t'$, is precisely $\frac{d}{dt}(m\vec v) = \vec E + \vec v \times \vec B$. The covariant equation of motion of a charged test particle on Minkowski space is the classical Lorentz force law. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Cyclotron motion in a uniform magnetic field (mechanics / dynamical systems).** Take $\vec E = 0$ and $\vec B = B\hat z$ constant, and integrate $(3.13)$. The theorem applies because a constant field is a legitimate electromagnetic field strength on Minkowski space, and its eigentime worldlines are exactly the solutions of the force law; the non-obvious ingredient is that with $\vec E = 0$ the temporal equation gives $t'' = 0$, so $t'$ — hence $m$ — is constant and the equation linearises to $\ddot{\vec c} = \frac{1}{t'}\vec B \times \vec c\,'$, whose spatial projection is uniform circular motion. Computing the radius and frequency in terms of $|\vec v|$ and $B$ is the payoff. This is non-obvious because the *relativistic* mass, not the rest mass, sets the frequency, and only the constancy of $t'$ from this theorem makes that visible.

**The energy balance and the work–energy theorem (electromagnetism).** Derive $\frac{dm}{dt} = \langle\vec v, \vec E\rangle$ from the temporal equation and interpret it. The theorem applies because the temporal equation $t'' = \langle\vec c\,', \vec E\rangle$ is one of the two component equations; dividing by $t'$ and using $m = t'$ turns it into a statement about the rate of change of energy. The non-obvious point is that the magnetic field is entirely absent from the energy balance — it does no work — which the exercise must trace back to the fact that $\vec B$ contributes only the cross-product term, orthogonal to $\vec v$. This connects to the four-force identity $F(c', c') = 0$.

**Recovering the geodesic limit (Riemannian and Lorentzian geometry).** Set $F = 0$ and show that $(3.12)$ becomes the geodesic equation, so a free charged particle moves on a straight timelike line of Minkowski space. The theorem applies degenerately: with $\vec E = \vec B = 0$ the force one-form vanishes and both vector equations read $c'' = 0$. The non-obvious transfer is to a *curved* Lorentzian manifold, where Lemma 1 fails and the Christoffel term survives; the exercise is to show that the same contraction-and-sharp computation still splits $(3.12)$ into a curved geodesic term plus the Lorentz force, so the force law is a frame-dependent readout even in general relativity. This links the flat computation to the equation of motion on a general spacetime.

---

# Bridges

- **[[Def - The Lorentz Four-Force|The Lorentz four-force]]** — the same physics in the special-relativity register. There the force is defined covariantly as $f = qF(\cdot, U)$ in signature $(+,-,-,-)$ with $U$ the four-velocity ($\langle U, U\rangle = 1$), and its spatial projection onto an observer's rest space is $q(\mathbf{E} + \mathbf{V} \times \mathbf{B})$, the same law $(3.13)$ with $q$ and $c$ restored. This page is the gauge-theoretic re-derivation of that projection: what the special-relativity page obtains by decomposing the four-force relative to an observer, this page obtains by contracting the curvature two-form with the velocity and applying the Lorentzian sharp. The metric sign flip $g_B = -g_{\mathrm{SR}}$ and the corresponding sign flips of the sharp and of the timelike condition cancel, so the two derivations land on the identical formula.

- **[[Ex - The Lorentz force is a pure four-force|The Lorentz force is a pure four-force]]** — the statement that the electromagnetic force conserves rest mass. Contracting $(3.12)$ with $c'$ gives $\langle\frac{\nabla}{d\tau}c', c'\rangle = -F(c', c') = 0$ by the antisymmetry of $F$; this is the invariant form of "the magnetic field does no work" and is exactly the temporal equation once $\vec v$ is contracted in. The exercise there works the identity in the four-force language; here it is the mechanism behind the redundancy of the temporal equation (Step 4).

- **[[Thm - Solutions of the Lorentz Force Equation Have Constant Speed and Exist Uniquely|Constant speed and unique solutions]]** — the prerequisite that licenses the eigentime normalisation. That theorem guarantees $\langle c', c'\rangle$ is constant along any solution, so the hypothesis "$\langle c', c'\rangle = -1$" of this page can always be arranged, and it supplies the existence-uniqueness of trajectories for given initial data. Without it, the reduction here would apply only to worldlines that happen to be eigentime-parametrised in advance.

- **The non-relativistic Newton law** — obtained by expanding $t' = 1/\sqrt{1 - |\vec v|^2}$ for $|\vec v| \ll 1$. To first order $t' \to 1$, so $m \to m_0$, coordinate time $t$ agrees with eigentime $\tau$, and $(3.13)$ collapses to $m_0\,\ddot{\vec c} = \vec E + \vec v \times \vec B$. The bridge is a Taylor expansion of the single relativistic factor $t'$; the whole relativistic content of the force law is carried by the velocity-dependence of $m$.

---

# Unlocked by This

> [!tip] Motion of a charge in a uniform field *(from Electromagnetism)*
> With $(3.13)$ in hand, the trajectories in constant $\vec E$ or constant $\vec B$ can be integrated in closed form: uniform hyperbolic (boost) motion for a pure electric field, uniform circular (cyclotron) motion at the relativistic frequency for a pure magnetic field. See **Thm - Motion of a Charge in a Uniform Field**.

> [!tip] The Yang–Mills equation of motion *(from Gauge Theory)*
> The abelian coupling $F(c', \cdot)^\sharp$ of a charge to a $U(1)$-connection is the model for the coupling of matter to a non-abelian connection, where the field strength takes values in the Lie algebra and the force acquires an internal-index structure. The reduction performed here — contract the curvature with the velocity, split into components — is the template for reading off the classical motion of a coloured particle in a Yang–Mills field.
