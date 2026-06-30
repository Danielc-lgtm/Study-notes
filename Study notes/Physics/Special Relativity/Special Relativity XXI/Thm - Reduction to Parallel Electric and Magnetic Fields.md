---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - Transformation of Electric and Magnetic Fields"
  - "Thm - The Electromagnetic Field Invariants"
  - "Def - The Electromagnetic Field Tensor"
tags: [physics, special-relativity, electromagnetism]
---

# Notation

SI units, $c$ kept. Signature $\mathrm{diag}(+1,-1,-1,-1)$. An observer $\mathcal{O}$ measures fields $\mathbf{E}$, $\mathbf{B}$ at an event $O$, with magnitudes $E = |\mathbf{E}|$, $B = |\mathbf{B}|$ and angle $\theta\in\,]0,\pi[$ between them. A second observer $\mathcal{O}'$ through $O$ moves at velocity $\mathbf{U} = U\,\mathbf{e}$ relative to $\mathcal{O}$, with $\Gamma = (1-U^2/c^2)^{-1/2}$, and measures $\mathbf{E}'$, $\mathbf{B}'$. The [[Thm - The Electromagnetic Field Invariants|field invariants]] are $I_1 = c^2B^2 - E^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$. The field is **null** when $I_1 = I_2 = 0$. The spatial cross product is $\times$. Full registry on [[Special Relativity XXI — The Electromagnetic Field]].

---

# Statement

> **Theorem (reduction to parallel fields).** If the [[Def - The Electromagnetic Field Tensor|electromagnetic field]] is *not null* at an event $O$ (that is, $I_1$ and $I_2$ are not both zero), then there exists an inertial observer through $O$ for whom the electric and magnetic fields at $O$ are **parallel** (or one of them vanishes).

> **Corollary (the $I_2 = 0$ case).** If $I_2 = 0$ (so $\mathbf{E}\perp\mathbf{B}$ for every observer) and $I_1 \ne 0$, the field can be reduced to **purely magnetic** (if $I_1 > 0$) or **purely electric** (if $I_1 < 0$), by a boost perpendicular to both fields with velocity
> $$U = \frac{E}{B}\quad (I_1 > 0,\ \text{gives } \mathbf{E}' = 0), \qquad U = c^2\frac{B}{E}\quad (I_1 < 0,\ \text{gives } \mathbf{B}' = 0).$$

The reducing observer is not unique: any further boost along the common direction of $\mathbf{E}'$ and $\mathbf{B}'$ preserves their parallelism. Only for a *null* field does the reduction fail — there is then no frame in which $\mathbf{E}$ and $\mathbf{B}$ are parallel or either vanishes.

---

# Motivation

A general electromagnetic field has $\mathbf{E}$ and $\mathbf{B}$ pointing in arbitrary, unrelated directions, and studying the motion of a charge in such a field is a genuinely three-dimensional problem. This theorem says the situation is almost always simpler than it looks: for any field that is not on the radiation-like boundary, there is an observer for whom $\mathbf{E}$ and $\mathbf{B}$ line up, reducing the problem to the highly symmetric case of *parallel* fields — where the motion separates into a hyperbolic part along the common axis and a circular part around it.

The result is the geometric payoff of the [[Thm - The Electromagnetic Field Invariants|invariants]]: the two invariants $I_1$ and $I_2$ classify fields up to Lorentz transformation, and this theorem exhibits the canonical representative of each class. A field with $I_2 \ne 0$ reduces to parallel non-zero $\mathbf{E}$ and $\mathbf{B}$; a field with $I_2 = 0$ reduces to a single field (purely electric or purely magnetic); only the null field $I_1 = I_2 = 0$ has no such simplification. This is the Lorentz-group classification of antisymmetric tensors made concrete and physical.

Its practical importance is that it licenses the standard solution strategy for charged-particle motion: *boost to the frame where the field is parallel (or pure), solve the simple motion there, and boost back.* The cyclotron and the crossed-field trajectory are both solved this way in [[Thm - Motion of a Charge in a Uniform Field]], and the velocity $U = E/B$ at which a crossed field becomes purely magnetic is exactly the pass-velocity of the [[Special Relativity XXI — The Electromagnetic Field|Wien filter]].

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a non-null electromagnetic field at an event."

The first disguised source is **"the field is given as a crossed field $\mathbf{E}\perp\mathbf{B}$ with unequal magnitudes."** Crossed fields with $E\ne cB$ have $I_2 = 0$ and $I_1\ne0$, exactly the corollary's hypothesis, so they reduce to a single pure field. The bridge is recognising $\mathbf{E}\perp\mathbf{B}$ as $I_2 = 0$. *Example problem:* a velocity selector (crossed $\mathbf{E}$ and $\mathbf{B}$) with $cB > E$ becomes purely magnetic in the frame moving at $U = E/B$.

The second disguised source is **"the field is that of a moving charge."** The [[Def - Field of a Charge in Uniform Translation|moving-charge field]] has $\mathbf{B} = \frac{1}{c^2}\mathbf{U}\times\mathbf{E}$, hence $\mathbf{E}\perp\mathbf{B}$ ($I_2=0$) and $E > cB$ ($I_1 < 0$, since $|\mathbf{B}| = U|\mathbf{E}|\sin\angle/c^2 < |\mathbf{E}|/c$). The bridge is the orthogonality and dominance of the moving-charge field. *Example problem:* show that the field of a moving charge is purely electric in the charge's rest frame — the reduction velocity $U = c^2B/E$ recovers exactly the charge's velocity.

The third disguised source is **"the invariants are computed and at least one is nonzero."** Any field for which $(I_1, I_2)\ne(0,0)$ qualifies; computing the invariants in any convenient frame settles whether the reduction is possible and to what form. The bridge is the invariant classification. *Example problem:* given fields in the lab, decide whether a frame exists in which they are antiparallel — yes, unless the field is null.

**Targets (Output Amplification)**

The conclusion is "there is a frame with $\mathbf{E}'\parallel\mathbf{B}'$ (or one of them zero)."

Combine the conclusion with **the parallel-field equation of motion.** In the reduced frame, the motion of a charge separates: hyperbolic acceleration along the common axis (driven by $\mathbf{E}'$), circular gyration around it (driven by $\mathbf{B}'$). The further result is the complete trajectory in a general non-null uniform field, obtained by solving the separated motion and boosting back. The combination is the backbone of [[Thm - Motion of a Charge in a Uniform Field]]. *Example:* a charge in arbitrary uniform $\mathbf{E}$, $\mathbf{B}$ with $I_2\ne0$ executes a "drifting helix with increasing pitch" — visible only after reducing to parallel fields.

Combine the conclusion with **the Wien-filter condition.** When $I_2 = 0$ and $I_1 > 0$, the reducing velocity $U = E/B$ is the velocity at which a charge passes *undeflected* through the crossed field (electric and magnetic forces cancel). The further result is the velocity selector: only particles with speed $E/B$ traverse the field straight. The combination is the operating principle of the Wien filter. *Example:* tuning $E/B$ selects a single velocity from a beam with a spread of speeds.

Combine the conclusion with **the drift velocity of guiding-centre motion.** The reduction velocity $\mathbf{U} = \mathbf{E}\times\mathbf{B}/B^2$ (for $I_1>0$) is precisely the $\mathbf{E}\times\mathbf{B}$ **drift velocity** of plasma physics: the average velocity at which a charged particle's gyration centre drifts in crossed fields. The further result connects the relativistic reduction to the non-relativistic guiding-centre theory. The combination is central to magnetised-plasma confinement. *Example:* particles in a tokamak's crossed fields drift at $\mathbf{E}\times\mathbf{B}/B^2$ regardless of charge or mass.

---

# Why Is It True

The reduction works because boosting *rotates* $\mathbf{E}$ and $\mathbf{B}$ toward or away from each other, and you can always boost enough to align them — unless the field is null, in which case the alignment "completes only at the speed of light", which is unreachable.

**The one-line mechanism: a boost perpendicular to the plane of $\mathbf{E}$ and $\mathbf{B}$ continuously turns the cross product $\mathbf{E}'\times\mathbf{B}'$, and the condition $\mathbf{E}'\times\mathbf{B}' = 0$ (parallel fields) is a quadratic in the boost speed whose discriminant is $(I_1^2 + 4I_2^2)/(\text{positive})$ — non-negative, hence solvable, with the solution at speed $< c$ existing precisely when the field is not null.**

To see this, choose the boost direction $\mathbf{e}$ along the normal $\mathbf{E}\times\mathbf{B}$ to the plane the two fields span. Under such a boost, $\mathbf{E}$ and $\mathbf{B}$ stay in their plane (the boost-transverse plane) and rotate within it. The transformed cross product $\mathbf{E}'\times\mathbf{B}'$, computed from the [[Thm - Transformation of Electric and Magnetic Fields|transformation law]], comes out proportional to a quadratic in $x = U/c$:
$$
x^2 - \frac{E^2 + c^2B^2}{cEB\sin\theta}\,x + 1 = 0.
$$
Its discriminant is $\Delta = \big(\frac{E^2+c^2B^2}{cEB\sin\theta}\big)^2 - 4 = \frac{I_1^2 + 4I_2^2}{(cEB\sin\theta)^2}$, which is manifestly $\ge0$ — so *real* roots always exist. The product of the roots is $1$ (constant term over leading coefficient), so the two roots are reciprocals; one lies below $1$ and one above, and the physically admissible root ($U < c$, i.e. $x < 1$) always exists *unless* the two roots coincide at $x = 1$. They coincide exactly when $\Delta = 0$, that is when $I_1 = I_2 = 0$ — the null field. So the reduction is possible for every non-null field, and impossible only at the null boundary, where the required boost would need $U = c$.

The deeper reason, in representation-theoretic terms: the field is the complex three-vector $\mathbf{E} + ic\mathbf{B}$, and the Lorentz group acts as complex rotations $SO(3,\mathbb{C})$. A complex three-vector can be rotated to have $\mathbf{E}'$ and $\mathbf{B}'$ parallel (i.e. $\mathbf{E}'+ic\mathbf{B}'$ real-proportional to a fixed direction) *unless* it is a null vector of the complex bilinear form — and the complex norm is exactly $-I_1 + 2iI_2$, which vanishes precisely for the null field. Reduction to parallel fields is the statement that a non-isotropic complex vector can be aligned; the null field is the isotropic vector that cannot.

---

# What Makes This Hard

The hard step is *choosing the boost direction*: it must be perpendicular to the plane of $\mathbf{E}$ and $\mathbf{B}$ (along $\mathbf{E}\times\mathbf{B}$), and seeing why this is the right choice — that it keeps both fields in their plane while rotating them within it — is the non-obvious geometric insight. The second difficulty is recognising that the quadratic always has a root below $1$ *except* for the null field, which requires tracking the discriminant down to $I_1^2 + 4I_2^2$ and seeing that it vanishes only when both invariants do. The common error is to forget the null case and assert reduction is *always* possible — it fails precisely on the radiation fields, and that exception is physically important (a plane wave cannot be transformed to rest).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Boost along the normal $\mathbf{E}\times\mathbf{B}$ to the field plane. Demand the transformed fields be parallel, $\mathbf{E}'\times\mathbf{B}' = 0$. Using the transformation law, this becomes a quadratic in $U/c$. Show its discriminant is $(I_1^2 + 4I_2^2)/(\text{positive}) \ge 0$, so real roots exist; show the roots are reciprocal, so one is below $1$ (admissible) unless they coincide at $1$, which happens only for the null field.

**Subgoal decomposition:**

1. **Choose the boost direction.** Take $\mathbf{e} = (EB\sin\theta)^{-1}\,\mathbf{E}\times\mathbf{B}$, the unit normal to the field plane.
   - *Hint:* A boost normal to the plane leaves both fields in the plane and only rotates them.
   - *Why needed:* It reduces the alignment to a one-parameter (speed) problem.

2. **Impose parallelism.** Compute $\mathbf{E}'\times\mathbf{B}'$ for this boost and set it to zero.
   - *Hint:* Use the transformation law; both fields are transverse to the boost, so each transforms by $\Gamma$ with a cross term.
   - *Why needed:* It encodes "fields parallel" as an equation in $U$.

3. **Reduce to a quadratic.** Show the condition is $x^2 - \frac{E^2+c^2B^2}{cEB\sin\theta}x + 1 = 0$ with $x = U/c$.
   - *Hint:* Collect terms; the constant is $1$ and the linear coefficient involves $E^2 + c^2B^2$.
   - *Why needed:* It is the equation to solve for the reducing speed.

4. **Analyse the roots.** Show $\Delta = (I_1^2 + 4I_2^2)/(cEB\sin\theta)^2 \ge 0$, the product of roots is $1$, and the admissible root $x<1$ exists unless $I_1 = I_2 = 0$.
   - *Hint:* Reciprocal roots straddle $1$; they merge at $1$ exactly when $\Delta = 0$, i.e. the null field.
   - *Why needed:* It establishes existence (and the failure for null fields), completing the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: A normal boost keeps the fields in their plane
> **Statement:** Boosting with velocity $\mathbf{U} = U\mathbf{e}$, $\mathbf{e}\parallel\mathbf{E}\times\mathbf{B}$, transforms $\mathbf{E}$ and $\mathbf{B}$ into fields $\mathbf{E}'$, $\mathbf{B}'$ that still lie in the plane spanned by the original $\mathbf{E}$, $\mathbf{B}$.
>
> **Hint:** Both $\mathbf{E}$ and $\mathbf{B}$ are perpendicular to the boost; the cross-product terms $\mathbf{U}\times\mathbf{B}$, $\mathbf{U}\times\mathbf{E}$ also lie in the plane.
>
> **Why needed:** It guarantees the alignment is a planar (one-angle) problem, reducible to one equation.
>
> > [!note]- Full proof
> > Since $\mathbf{e}\parallel\mathbf{E}\times\mathbf{B}$ is normal to the plane $P = \mathrm{span}(\mathbf{E},\mathbf{B})$, both fields are transverse to the boost: $\mathbf{E}_\parallel = \mathbf{B}_\parallel = 0$, $\mathbf{E}_\perp = \mathbf{E}$, $\mathbf{B}_\perp = \mathbf{B}$. The transformation law gives $\mathbf{E}' = \Gamma(\mathbf{E} + \mathbf{U}\times\mathbf{B})$, $\mathbf{B}' = \Gamma(\mathbf{B} - \tfrac{1}{c^2}\mathbf{U}\times\mathbf{E})$. Now $\mathbf{U}\times\mathbf{B}$ is perpendicular to $\mathbf{U}$ (hence in $P^{\perp\perp} = $ the plane through... ) — concretely, $\mathbf{U}\parallel\mathbf{E}\times\mathbf{B}$, so $\mathbf{U}\times\mathbf{B}$ lies in $P$ (it is perpendicular to $\mathbf{B}$ and to $\mathbf{U}$, and the plane perpendicular to $\mathbf{U}$ is $P$). Likewise $\mathbf{U}\times\mathbf{E}\in P$. Therefore $\mathbf{E}', \mathbf{B}'\in P$. $\blacksquare$

> [!note]- Lemma 2: Parallelism is a quadratic in U/c
> **Statement:** The condition $\mathbf{E}'\times\mathbf{B}' = 0$ is equivalent to $x^2 - \frac{E^2+c^2B^2}{cEB\sin\theta}\,x + 1 = 0$, with $x = U/c$.
>
> **Hint:** Expand $\mathbf{E}'\times\mathbf{B}'$ using Lemma 1's expressions and the double cross-product identity; the orthogonality $\mathbf{e}\cdot\mathbf{E} = \mathbf{e}\cdot\mathbf{B} = 0$ simplifies it.
>
> **Why needed:** It turns the geometric condition into a solvable algebraic equation.
>
> > [!note]- Full proof
> > Following the source (Eqs. (17.39)–(17.40)), substitute $\mathbf{E}' = \Gamma(\mathbf{E} + U\mathbf{e}\times\mathbf{B})$ and $\mathbf{B}' = \Gamma(\mathbf{B} - \tfrac{U}{c^2}\mathbf{e}\times\mathbf{E})$ into $\mathbf{E}'\times\mathbf{B}'$. Expanding the four cross products and using $\mathbf{e}\cdot\mathbf{E} = \mathbf{e}\cdot\mathbf{B} = 0$ together with $\mathbf{e} = (EB\sin\theta)^{-1}\mathbf{E}\times\mathbf{B}$, one finds
> > $$\mathbf{E}'\times\mathbf{B}' = \Gamma^2\Big[EB\sin\theta\Big(1 + \frac{U^2}{c^2}\Big) - \frac{U}{c^2}(E^2 + c^2B^2)\Big]\mathbf{e}.$$
> > Setting the bracket to zero and dividing by $cEB\sin\theta/c$ gives, with $x = U/c$,
> > $$1 + x^2 - \frac{E^2 + c^2B^2}{cEB\sin\theta}\,x = 0,$$
> > i.e. $x^2 - \frac{E^2+c^2B^2}{cEB\sin\theta}x + 1 = 0$. $\blacksquare$

> [!note]- Lemma 3: The admissible root exists iff the field is non-null
> **Statement:** The quadratic has real reciprocal roots; the root with $x<1$ exists unless $I_1 = I_2 = 0$, in which case the double root is $x = 1$.
>
> **Hint:** Compute the discriminant in terms of the invariants; use Vieta (product of roots $=1$).
>
> **Why needed:** It is the existence statement and pinpoints the unique failure (the null field).
>
> > [!note]- Full proof
> > The discriminant is
> > $$\Delta = \Big(\frac{E^2+c^2B^2}{cEB\sin\theta}\Big)^2 - 4 = \frac{(E^2+c^2B^2)^2 - 4c^2E^2B^2\sin^2\theta}{(cEB\sin\theta)^2}.$$
> > The numerator is $(E^2 - c^2B^2)^2 + 4c^2E^2B^2(1 - \sin^2\theta) = I_1^2 + 4c^2E^2B^2\cos^2\theta = I_1^2 + 4I_2^2$ (using $I_1 = c^2B^2 - E^2$ and $I_2 = cEB\cos\theta = c\mathbf{E}\cdot\mathbf{B}$). Hence $\Delta = (I_1^2 + 4I_2^2)/(cEB\sin\theta)^2 \ge 0$: real roots. By Vieta the product of the roots is $1$, so they are reciprocals $x_0, 1/x_0$; if $x_0 < 1$ it is admissible. The roots coincide ($x_0 = 1$, no admissible boost with $U<c$) iff $\Delta = 0$ iff $I_1^2 + 4I_2^2 = 0$ iff $I_1 = I_2 = 0$, the null field. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Suppose the field at $O$ is non-null, $(I_1, I_2)\ne(0,0)$, and that $\mathbf{E}$, $\mathbf{B}$ are not already parallel (else take $\mathcal{O}' = \mathcal{O}$); then $\sin\theta\ne0$ and the unit normal $\mathbf{e} = (EB\sin\theta)^{-1}\mathbf{E}\times\mathbf{B}$ is defined.
>
> Boost from $\mathcal{O}$ to an observer $\mathcal{O}'$ with velocity $\mathbf{U} = U\mathbf{e}$. By Lemma 1 the transformed fields $\mathbf{E}'$, $\mathbf{B}'$ lie in the plane $\mathrm{span}(\mathbf{E},\mathbf{B})$. By Lemma 2 the parallelism condition $\mathbf{E}'\times\mathbf{B}' = 0$ is the quadratic $x^2 - \frac{E^2+c^2B^2}{cEB\sin\theta}x + 1 = 0$ in $x = U/c$. By Lemma 3 this quadratic has real reciprocal roots with discriminant $(I_1^2+4I_2^2)/(cEB\sin\theta)^2$; since the field is non-null this is strictly positive, the roots are distinct, and the smaller one satisfies $x_0 < 1$, giving an admissible boost speed $U = cx_0 < c$. For this $\mathcal{O}'$, $\mathbf{E}'\parallel\mathbf{B}'$.
>
> **Corollary ($I_2 = 0$).** If additionally $I_2 = 0$, then $\mathbf{E}\perp\mathbf{B}$ ($\theta = \pi/2$, $\sin\theta = 1$) and the parallel fields $\mathbf{E}'\parallel\mathbf{B}'$ must also be perpendicular (parallelism is preserved by the construction, orthogonality by $I_2 = 0$); two vectors both parallel and perpendicular force one to vanish. The reducing speed solves $x^2 - \frac{E^2+c^2B^2}{cEB}x + 1 = 0$ with the admissible root giving (using $I_1 = c^2B^2 - E^2$)
> $$U = \frac{E}{B}\ (I_1>0,\ \mathbf{E}'=0,\ \text{purely magnetic}), \qquad U = c^2\frac{B}{E}\ (I_1<0,\ \mathbf{B}'=0,\ \text{purely electric}).$$
>
> **Non-uniqueness.** Any further boost of $\mathcal{O}'$ along the common direction of $\mathbf{E}'$, $\mathbf{B}'$ leaves both unchanged in direction (longitudinal components are invariant), so the parallel-field observer is not unique. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The $\mathbf{E}\times\mathbf{B}$ drift in plasma physics.** The reducing velocity for a crossed field with $I_1>0$ is $\mathbf{U} = \mathbf{E}\times\mathbf{B}/B^2$, the **drift velocity** at which the guiding centre of a charged particle moves in crossed fields, independent of charge and mass. Deriving the non-relativistic drift from the relativistic reduction connects this theorem to magnetic-confinement fusion. The application is nonobvious because the "drift" looks like a dynamical effect but is really a change of frame.

**The Wien velocity filter.** When $\mathbf{E}\perp\mathbf{B}$ and $cB > E$, the boost $U = E/B$ that makes the field purely magnetic is the velocity at which the electric and magnetic forces on a charge cancel, so only particles with speed $E/B$ pass undeflected. Designing a velocity selector for a given speed is choosing $E/B$. The application links the reduction theorem to mass spectrometry and beam optics.

**Whether a field configuration can be electrostatic.** Given measured $\mathbf{E}$ and $\mathbf{B}$, decide whether there is a frame in which the field is purely electric (hence describable by a scalar potential alone). The answer is yes iff $I_2 = 0$ and $I_1 < 0$ — a clean invariant criterion. The application shows the theorem answers a question about the *existence* of a description, not just a computation.

---

# Bridges

- **[[Thm - The Electromagnetic Field Invariants]]** — the reduction is governed entirely by the invariants: $I_2$ determines whether the reduced fields are both nonzero (parallel) or one vanishes (pure), and the null condition $I_1 = I_2 = 0$ is exactly when reduction fails. The discriminant $I_1^2 + 4I_2^2$ that controls existence *is* the squared modulus of the complex invariant $-I_1 + 2iI_2$.

- **[[Thm - Transformation of Electric and Magnetic Fields]]** — the proof is an application of the transformation law with the boost chosen normal to the field plane; the theorem is what you can *achieve* by transforming, the transformation law is the tool.

- **[[Thm - Motion of a Charge in a Uniform Field]]** — the reduction is the first step in solving charged-particle motion in a general uniform field: reduce to parallel (or pure) fields, solve the separated hyperbolic-plus-circular motion, and boost back. The reduction theorem is what makes the general case tractable.

- **The $\mathbf{E}\times\mathbf{B}$ drift and guiding-centre motion** — the reducing velocity $\mathbf{E}\times\mathbf{B}/B^2$ is the drift velocity of the non-relativistic guiding-centre approximation; the relativistic reduction is the exact statement of which the drift is the slow-field limit.

---

# Unlocked by This

> [!tip] The Lorentz-Group Classification of 2-Forms *(from Representation Theory)*
> This theorem is the physical face of the **classification of antisymmetric tensors** under the Lorentz group: every non-null 2-form is Lorentz-equivalent to a "block-diagonal" canonical form with $\mathbf{E}'\parallel\mathbf{B}'$, and the null 2-forms are the single exceptional orbit. This is the orbit structure of the $(1,0)\oplus(0,1)$ representation, classified by the complex invariant $-I_1 + 2iI_2$, with the null fields the isotropic (light-like) vectors of the complex form.

> [!tip] Magnetic Confinement and Particle Drifts *(from Plasma Physics)*
> The reducing frame for crossed fields moves at the $\mathbf{E}\times\mathbf{B}$ **drift velocity**, the foundation of guiding-centre theory: in a magnetised plasma, particles gyrate rapidly while their centres drift at $\mathbf{E}\times\mathbf{B}/B^2$ (plus curvature and gradient drifts). This single frame change explains why a perpendicular electric field drives a charge-independent flow, the basic transport mechanism in tokamaks and in the magnetosphere.
