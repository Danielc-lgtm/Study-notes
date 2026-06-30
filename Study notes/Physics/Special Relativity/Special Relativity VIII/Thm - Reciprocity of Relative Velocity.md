---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - Velocity Relative to an Observer"
  - "Def - Lorentz Factor and Relative Velocity"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature, so a four-velocity has $u \cdot u = +1$. Two observers $\mathcal{O}, \mathcal{O}'$ have future-directed unit four-velocities $u, u'$ and [[Def - Observer and Local Rest Space|local rest spaces]] $E_u = \{X : u\cdot X = 0\}$, $E_{u'} = \{X : u'\cdot X = 0\}$. The [[Def - Lorentz Factor and Relative Velocity|Lorentz factor between them]] is $\Gamma_0 = u \cdot u'$. The velocity of $\mathcal{O}'$ relative to $\mathcal{O}$ is $U \in E_u$; the velocity of $\mathcal{O}$ relative to $\mathcal{O}'$ is $U' \in E_{u'}$. The [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] onto $E_{u'}$ is $\perp_{u'}X = X - (u'\cdot X)\,u'$, and $\lVert X\rVert_g = \sqrt{-X\cdot X}$ denotes the magnitude of a spacelike vector. We assume the two worldlines cross at a common event $O$, so that $u, u'$ and the relative velocities are all defined at one point. Full registry on [[Special Relativity VIII — Kinematics II, Change of Observer]].

---

# Statement

> **Reciprocity of relative velocity.** Let $\mathcal{O}, \mathcal{O}'$ be two observers whose worldlines cross at an event $O$, with four-velocities $u, u'$ and Lorentz factor $\Gamma_0 = u\cdot u'$. Let $U \in E_u$ be the velocity of $\mathcal{O}'$ relative to $\mathcal{O}$, defined by $u' = \Gamma_0(u + U)$, and $U' \in E_{u'}$ the velocity of $\mathcal{O}$ relative to $\mathcal{O}'$, defined by $u = \Gamma_0(u' + U')$. Then:
> $$U' = -\frac{1}{\Gamma_0}\,\perp_{u'}U,$$
> and consequently the two relative velocities have equal magnitude,
> $$\lVert U' \rVert_g = \lVert U \rVert_g.$$
> In general $U' \ne -U$: the vectors $U$ and $U'$ belong to the distinct subspaces $E_u$ and $E_{u'}$, and the Galilean identity $U' = -U$ holds only in the limit $\lVert U\rVert_g \to 0$.

---

# Motivation

In Newtonian mechanics, the relation between the velocity of $B$ relative to $A$ and the velocity of $A$ relative to $B$ is so obvious it is never stated: they are negatives, $\mathbf{u}_{A/B} = -\mathbf{u}_{B/A}$. Both are vectors in the one universal space of Newtonian simultaneity, and reversing the roles of the two bodies reverses the velocity. This identity is the bedrock of every relative-motion calculation: it is why "you moving toward me" and "me moving toward you" are interchangeable descriptions.

This theorem asks what survives of that identity in relativity, and the answer is the first genuine surprise of the change-of-observer story. The two relative velocities are *not* negatives, and they cannot be, because they do not even live in the same vector space: $U$ is a vector in $\mathcal{O}$'s rest space $E_u$, and $U'$ is a vector in $\mathcal{O}'$'s rest space $E_{u'}$, and these are two different three-dimensional subspaces of spacetime, tilted relative to one another by the relative motion. There is no observer-independent way to say a vector in one is minus a vector in the other.

What the theorem rescues is a weaker but still robust statement: the two relative *speeds* are equal, $\lVert U'\rVert_g = \lVert U\rVert_g$. This is the relativistic residue of the Galilean identity — the magnitudes survive even though the vector relation does not. The result is the template for the whole chapter: a Galilean equation between vectors degrades into an equation between their invariant magnitudes, and the precise vector relation ($U' = -\Gamma_0^{-1}\perp_{u'}U$) records *which vector in which rest space*, which is where all the new physics lives. It matters in practice because it is what licenses talking about "the relative speed of two observers" as a single well-defined number — the thing that enters the Lorentz factor $\Gamma_0$ symmetrically — even though "the relative velocity" is two different vectors.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "two observers with four-velocities $u, u'$, related by $u' = \Gamma_0(u + U)$". Recognising its disguises:

The first disguised source is **"two inertial frames in standard configuration"**. A frame $S'$ moving at coordinate velocity $\mathbf{v}$ along the $x$-axis of $S$ is exactly the case $u = (1,\mathbf{0})$, $u' = \Gamma(1, \mathbf{v})$ in $S$-coordinates, so $U = \mathbf{v}$ and the theorem applies. The bridge is that any pair of inertial observers *is* a pair of four-velocities crossing (after translation) at a common event. *Example problem:* show that if $S'$ measures $S$ to recede at speed $w$, then $S$ measures $S'$ to recede at the same speed $w$ — even though the velocity *vectors* point in genuinely different directions in the two frames' rest spaces. This is the standard textbook "reciprocity of velocity" of [[Ex - Reciprocity and the evenness of the Lorentz factor|§1]], here given its frame-free form.

The second disguised source is **"a particle and an observer, viewed from the particle's rest frame"**. Taking the particle's own four-velocity as $u'$ and the observer's as $u$, the velocity of the observer *as seen by the particle* is $U'$, and the velocity of the particle *as seen by the observer* is $U$. The theorem says these have equal magnitude. The bridge is that "the particle's rest frame" is just a second observer. *Example problem:* a muon sees the Earth's atmosphere rushing up at speed $V$; show the laboratory sees the muon descend at the same speed $V$ (the symmetric input to the atmospheric-muon length-contraction argument).

The third disguised source is **"a symmetric scalar product"**. Whenever a quantity is built as $u \cdot u'$ for two four-velocities, its symmetry $u\cdot u' = u'\cdot u$ is the algebraic seed of reciprocity: the Lorentz factor $\Gamma_0$ is automatically the same in both directions, and the magnitude equality follows from extracting $\lVert U\rVert^2 = 1 - 1/\Gamma_0^2$ from it. The bridge is that the symmetry of the metric *is* the reciprocity of the factor. *Example problem:* prove the Lorentz factor relating two observers is the same regardless of which is called "moving", as a one-line consequence of $u\cdot u' = u'\cdot u$.

**Targets (Output Amplification)**

The conclusion is "$\lVert U'\rVert_g = \lVert U\rVert_g$, with $U' = -\Gamma_0^{-1}\perp_{u'}U$".

Combine the conclusion with **the definition of the Lorentz factor**. Since $\Gamma_0 = (1 - \lVert U\rVert^2)^{-1/2}$ depends only on the relative *speed*, and the speeds are equal, $\Gamma_0$ is the same computed from either observer's viewpoint. The further result is that $\Gamma_0$ is a genuine symmetric function of the pair $(\mathcal{O}, \mathcal{O}')$, which is what makes the time-dilation and length-contraction factors well-defined without specifying "which one is moving". The combination is useful because it removes an apparent ambiguity that confuses every beginner: both observers see the other's clock slow by the *same* $\Gamma_0$, and this is consistent precisely because the relation is reciprocal.

Combine the conclusion with **length contraction**. The contraction factor is $\Gamma_0$, the same number both ways by reciprocity, so each observer measures the *other's* rulers contracted by the same factor — there is no contradiction, because they are measuring different rulers using different simultaneity slices. The further result, exploited in [[Thm - Length Contraction (General)]], is the symmetric mutual contraction that resolves the ladder-and-barn paradox. The combination is nonobvious because naive logic says "if I see your ruler short, you should see mine long", and reciprocity is exactly what refutes that.

Combine the conclusion with **the projector identity** $U' = -\Gamma_0^{-1}\perp_{u'}U$. This explicit formula, beyond the magnitude equality, tells you the *direction* of the reciprocal velocity in $E_{u'}$: it is minus the shadow of $U$ cast on $\mathcal{O}'$'s rest space. The further result is that one can carry $U$ from $E_u$ to $E_{u'}$ concretely, which is the building block of the [[Thm - Law of Velocity Composition|velocity-composition law]] (where the same projection appears). The combination is useful whenever a calculation must produce the reciprocal velocity as an actual vector, not merely its length.

---

# Why Is It True

The heart of the matter is that "the velocity of $X$ relative to $Y$" is *not* a property of the pair $\{X, Y\}$ but a property of the pair *together with a choice of whose rest space to use*. Once you accept that the answer must live in a chosen rest space, the asymmetry is forced: $U$ has to be in $E_u$ and $U'$ has to be in $E_{u'}$, and there is simply no room for them to be negatives unless those two spaces coincide.

**The one-line mechanism: $U$ and $U'$ are the two different orthogonal projections of the same relative motion onto the two different rest spaces, so they agree in length (the length is set by the boost angle, which is symmetric) but disagree in direction (each points within its own space).**

Here is the picture without algebra. Draw the two worldlines crossing at $O$, with four-velocities $u$ and $u'$ making a hyperbolic "angle" between them (a rapidity $\varphi$, with $\Gamma_0 = \cosh\varphi$). The rest space $E_u$ is the spatial slice orthogonal to $u$; the rest space $E_{u'}$ is the slice orthogonal to $u'$; they are tilted by the same hyperbolic angle. The velocity $U$ is obtained by projecting the *direction of $u'$* into $E_u$ and normalising appropriately — geometrically, it is "how much of $\mathcal{O}'$'s motion lies in $\mathcal{O}$'s space". By the perfect symmetry of the configuration under swapping $u \leftrightarrow u'$ (the hyperbolic angle between two lines does not care which line you start from), the velocity $U'$ — "how much of $\mathcal{O}$'s motion lies in $\mathcal{O}'$'s space" — has the *same magnitude*. But it is computed in a *different* slice, so it points in a different direction in spacetime. The magnitude is symmetric because it is a function of the angle alone; the direction is asymmetric because each velocity is confined to its own observer's slice.

Why, then, do they *seem* like negatives in the Newtonian world? Because in the limit of small relative speed the hyperbolic angle is tiny, the two rest spaces are nearly the same slice, and the projection becomes the identity. In that limit $\perp_{u'}U \to U$ and $\Gamma_0 \to 1$, so $U' \to -U$. The Galilean identity is the small-angle shadow of the true statement; the minus sign is real (the reciprocal velocity does point "backward"), but the equality of the two *vectors* is an artefact of pretending the two slices coincide.

---

# What Makes This Hard

The conceptual obstacle is accepting that $U$ and $U'$ are not comparable as vectors at all — most people instinctively want to write $U' = -U$ and then "correct it", when the correct statement is that the equation is type-incorrect from the start because the two vectors live in different spaces. The non-obvious technical step is the projector identity $U' = -\Gamma_0^{-1}\perp_{u'}U$: deriving it requires substituting the decomposition of $u$ in terms of $u'$ and $U'$ into the decomposition of $u'$ in terms of $u$ and $U$, and recognising the orthogonal projection that emerges. The most common error is to compute $\lVert U'\rVert$ by naively taking $-U$ and getting the right magnitude *for the wrong reason*, masking the fact that the directions genuinely differ — a slip that becomes a real error the moment the *direction* of $U'$ is needed (as in non-collinear velocity composition).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Start from the two defining decompositions $u' = \Gamma_0(u + U)$ and $u = \Gamma_0(u' + U')$. Substitute the first into the second to get one equation relating $U'$ to $U$ and the four-velocities; then project onto $E_{u'}$ to isolate $U'$, and take the squared norm to get the magnitude equality. The key invariants are $u\cdot u = u'\cdot u' = 1$, $u\cdot U = u'\cdot U' = 0$, and $\Gamma_0^2(1 - \lVert U\rVert^2) = 1$.

**Subgoal decomposition:**

1. **Extract the magnitude of $U$ from the Lorentz factor.** Show $\lVert U\rVert_g^2 = 1 - 1/\Gamma_0^2$, equivalently $\Gamma_0 = (1 - \lVert U\rVert^2)^{-1/2}$.
   - *Hint:* Take the squared norm of $u' = \Gamma_0(u + U)$ using $u'\cdot u' = 1$, $u\cdot u = 1$, $u\cdot U = 0$, and $U\cdot U = -\lVert U\rVert^2$.
   - *Why needed:* This expresses the relative speed purely through $\Gamma_0$, which is symmetric, so it will give the magnitude equality immediately once the same is done for $U'$.

2. **Derive the explicit relation $U' = -\Gamma_0^{-1}\perp_{u'}U$.** Substitute the first decomposition into the second and solve.
   - *Hint:* From $u = \Gamma_0(u' + U')$ get $U' = u/\Gamma_0 - u'$; substitute $u' = \Gamma_0(u+U)$ for the $u'$ on the right, or instead apply the projector $\perp_{u'}$ to $u = \Gamma_0(u' + U')$ noting $\perp_{u'}u' = 0$ and $\perp_{u'}U' = U'$.
   - *Why needed:* This is the explicit reciprocal-velocity formula; the magnitude equality follows by taking its norm.

3. **Conclude equality of magnitudes.** Show $\lVert U'\rVert_g = \lVert U\rVert_g$.
   - *Hint:* Either repeat Subgoal 1 with primes (getting $\lVert U'\rVert^2 = 1 - 1/\Gamma_0^2$, the same right-hand side because $\Gamma_0$ is symmetric), or take the squared norm of the formula from Subgoal 2 and simplify $\lVert\perp_{u'}U\rVert^2$.
   - *Why needed:* This is the surviving Galilean residue, the headline conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: The relative speed is fixed by the Lorentz factor
> **Statement:** From $u' = \Gamma_0(u + U)$ with $u\cdot u = u'\cdot u' = 1$, $u\cdot U = 0$, one has $\lVert U\rVert_g^2 = 1 - 1/\Gamma_0^2$, i.e. $\Gamma_0 = (1 - \lVert U\rVert^2)^{-1/2}$.
>
> **Hint:** Square the decomposition and use orthogonality.
>
> **Why needed:** It writes the relative speed through the symmetric quantity $\Gamma_0$, which is the engine of the magnitude equality.
>
> > [!note]- Full proof
> > Take the Minkowski square of $u' = \Gamma_0(u + U)$:
> > $$u'\cdot u' = \Gamma_0^2\,(u + U)\cdot(u + U) = \Gamma_0^2\big(u\cdot u + 2\,u\cdot U + U\cdot U\big).$$
> > Now $u'\cdot u' = 1$, $u\cdot u = 1$, $u\cdot U = 0$ (since $U \in E_u$), and $U\cdot U = -\lVert U\rVert_g^2$ (spacelike, mostly-minus). Hence
> > $$1 = \Gamma_0^2\big(1 - \lVert U\rVert_g^2\big),$$
> > so $\lVert U\rVert_g^2 = 1 - 1/\Gamma_0^2$ and $\Gamma_0 = (1 - \lVert U\rVert_g^2)^{-1/2}$. $\blacksquare$

> [!note]- Lemma 2: The reciprocal velocity is the negative projection
> **Statement:** $U' = -\dfrac{1}{\Gamma_0}\perp_{u'}U$, where $\perp_{u'}X = X - (u'\cdot X)u'$.
>
> **Hint:** Apply the projector $\perp_{u'}$ to the decomposition $u = \Gamma_0(u' + U')$.
>
> **Why needed:** It is the explicit direction-and-magnitude formula for the reciprocal velocity, the precise replacement for the Galilean $U' = -U$.
>
> > [!note]- Full proof
> > Apply $\perp_{u'}$ to $u = \Gamma_0(u' + U')$. Since $\perp_{u'}u' = u' - (u'\cdot u')u' = u' - u' = 0$ and $\perp_{u'}U' = U' - (u'\cdot U')u' = U'$ (because $U' \in E_{u'}$ so $u'\cdot U' = 0$), the right-hand side projects to $\Gamma_0 U'$. The left-hand side projects to $\perp_{u'}u = u - (u'\cdot u)u' = u - \Gamma_0 u'$. Therefore
> > $$\Gamma_0 U' = u - \Gamma_0 u'.$$
> > Now substitute $u' = \Gamma_0(u + U)$ to eliminate $u'$ on the right is one route; more directly, compute $\perp_{u'}U$ and compare. We have $\perp_{u'}U = U - (u'\cdot U)u'$. From $u' = \Gamma_0(u+U)$, $u'\cdot U = \Gamma_0(u\cdot U + U\cdot U) = \Gamma_0(0 - \lVert U\rVert^2) = -\Gamma_0\lVert U\rVert^2$. Meanwhile, from $\Gamma_0 U' = u - \Gamma_0 u'$ and $u = \Gamma_0 u' + \Gamma_0 U'$... instead, solve cleanly: write $u = \Gamma_0 u' + \Gamma_0 U'$, so $u - \Gamma_0 u' = \Gamma_0 U'$ gives $U' = (u - \Gamma_0 u')/\Gamma_0 = u/\Gamma_0 - u'$. Substitute $u' = \Gamma_0(u + U)$:
> > $$U' = \frac{u}{\Gamma_0} - \Gamma_0(u + U) = \Big(\frac{1}{\Gamma_0} - \Gamma_0\Big)u - \Gamma_0 U.$$
> > Using $1/\Gamma_0 - \Gamma_0 = (1 - \Gamma_0^2)/\Gamma_0$ and $\Gamma_0^2 - 1 = \Gamma_0^2\lVert U\rVert^2$ (Lemma 1), this is $U' = -\Gamma_0\lVert U\rVert^2\,u - \Gamma_0 U$. Finally check this equals $-\Gamma_0^{-1}\perp_{u'}U$: compute $-\Gamma_0^{-1}\perp_{u'}U = -\Gamma_0^{-1}(U - (-\Gamma_0\lVert U\rVert^2)u') = -\Gamma_0^{-1}U - \lVert U\rVert^2 u'$. Substituting $u' = \Gamma_0(u+U)$ gives $-\Gamma_0^{-1}U - \lVert U\rVert^2\Gamma_0(u + U) = -\Gamma_0\lVert U\rVert^2 u - (\Gamma_0^{-1} + \Gamma_0\lVert U\rVert^2)U$, and $\Gamma_0^{-1} + \Gamma_0\lVert U\rVert^2 = \Gamma_0^{-1}(1 + \Gamma_0^2\lVert U\rVert^2) = \Gamma_0^{-1}\Gamma_0^2 = \Gamma_0$, so this is $-\Gamma_0\lVert U\rVert^2 u - \Gamma_0 U$, matching. Hence $U' = -\Gamma_0^{-1}\perp_{u'}U$. $\blacksquare$

> [!note]- Lemma 3: The magnitudes are equal
> **Statement:** $\lVert U'\rVert_g = \lVert U\rVert_g$.
>
> **Hint:** Apply Lemma 1 with the roles of the two observers swapped.
>
> **Why needed:** It is the surviving Galilean identity, the conclusion of the theorem.
>
> > [!note]- Full proof
> > The decomposition $u = \Gamma_0(u' + U')$ has exactly the same form as $u' = \Gamma_0(u + U)$ with $(u, U) \leftrightarrow (u', U')$, and the Lorentz factor $\Gamma_0 = u\cdot u' = u'\cdot u$ is symmetric. So Lemma 1, applied to this decomposition, gives $\lVert U'\rVert_g^2 = 1 - 1/\Gamma_0^2$. Comparing with $\lVert U\rVert_g^2 = 1 - 1/\Gamma_0^2$ from Lemma 1 itself, $\lVert U'\rVert_g^2 = \lVert U\rVert_g^2$, hence $\lVert U'\rVert_g = \lVert U\rVert_g$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $u, u'$ be the four-velocities, $\Gamma_0 = u\cdot u'$, with the defining decompositions
> $$u' = \Gamma_0(u + U),\quad u\cdot U = 0; \qquad u = \Gamma_0(u' + U'),\quad u'\cdot U' = 0,$$
> and $u\cdot u = u'\cdot u' = 1$.
>
> *Step 1 (relative speed).* Squaring the first decomposition, $1 = u'\cdot u' = \Gamma_0^2(1 + 0 - \lVert U\rVert_g^2)$, so
> $$\lVert U\rVert_g^2 = 1 - \Gamma_0^{-2}. \tag{$\ast$}$$
>
> *Step 2 (explicit reciprocal velocity).* From $u = \Gamma_0(u' + U')$, solve $U' = u/\Gamma_0 - u'$ and substitute $u' = \Gamma_0(u + U)$:
> $$U' = \frac{u}{\Gamma_0} - \Gamma_0(u + U) = \Big(\frac{1}{\Gamma_0} - \Gamma_0\Big)u - \Gamma_0 U = -\Gamma_0\lVert U\rVert_g^2\,u - \Gamma_0 U,$$
> using $\Gamma_0 - \Gamma_0^{-1} = \Gamma_0(1 - \Gamma_0^{-2}) = \Gamma_0\lVert U\rVert_g^2$ from $(\ast)$. A direct computation (Lemma 2) shows this equals $-\Gamma_0^{-1}\perp_{u'}U$.
>
> *Step 3 (magnitude equality).* The second decomposition $u = \Gamma_0(u' + U')$ is the first with $(u,U)\leftrightarrow(u',U')$ and the *same* symmetric $\Gamma_0$; squaring it gives $\lVert U'\rVert_g^2 = 1 - \Gamma_0^{-2}$, identical to $(\ast)$. Hence
> $$\lVert U'\rVert_g = \lVert U\rVert_g.$$
>
> Finally, $U' = -U$ would require $U \in E_{u'}$, i.e. $u'\cdot U = 0$; but $u'\cdot U = \Gamma_0(u\cdot U + U\cdot U) = -\Gamma_0\lVert U\rVert_g^2$, which vanishes only when $\lVert U\rVert_g = 0$. So $U' \ne -U$ unless the relative speed is zero, in which limit $\Gamma_0 \to 1$, $\perp_{u'} \to \mathrm{Id}$, and $U' \to -U$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Hyperbolic geometry of the velocity space.** The set of relative velocities of magnitude less than $c$ is a model of three-dimensional hyperbolic space, and reciprocity is the statement that the hyperbolic *distance* from the origin to $U$ equals that to $U'$ — the rapidity $\varphi = \tanh^{-1}\lVert U\rVert$ is the same. The "non-negativeness" $U' \ne -U$ is the curvature of this space showing up: in flat (Euclidean) velocity space the reciprocal would be exactly $-U$, and the deviation measures the hyperbolic curvature. The application is nonobvious because reciprocity, an apparently elementary symmetry, is secretly a statement about the isometries of hyperbolic 3-space acting on itself.

**Mutual time dilation in GPS and particle storage rings.** Two clocks in relative motion each measure the *other* to run slow by the same $\Gamma_0$, a direct corollary of reciprocity (since $\Gamma_0$ is symmetric). In a particle storage ring, the laboratory sees the circulating particles' clocks (their decay clocks) dilated, and reciprocity guarantees the particles would see the laboratory's clocks dilated by the same factor — both correct, because they slice spacetime differently. The application is out-of-distribution because it looks paradoxical (each slower than the other) until reciprocity plus the relativity of simultaneity resolves it.

**The composition of group elements and conjugation.** In the [[Def - The Lorentz Group|Lorentz group]], reciprocity is the statement that the boost taking $u$ to $u'$ and the boost taking $u'$ to $u$ are *inverses*, hence have the same rapidity magnitude — but the boost from $u'$ to $u$ is the *conjugate* of the naive inverse by the rotation between the rest spaces, which is why $U'$ is a rotated version of $-U$ rather than $-U$ itself. The application connects the elementary kinematic reciprocity to the group-theoretic fact that $g^{-1}$ and $g$ share a conjugacy-invariant (the rapidity), explored in [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Bridges

- **[[Thm - Law of Velocity Composition]]** — reciprocity is the special case of velocity composition where the "particle" $\mathcal{P}$ is taken to be one of the observers: setting $V = U$ (the particle is $\mathcal{O}'$ itself) in the composition law reproduces $U' = -\Gamma_0^{-1}\perp_{u'}U$. The projector $\perp_{u'}$ that appears in reciprocity is the very same one that appears in the general composition formula; reciprocity is the simplest instance of "carry a velocity from $E_u$ to $E_{u'}$".

- **[[Thm - Length Contraction (General)]]** — the symmetric factor $\Gamma_0$ that reciprocity certifies is what makes mutual length contraction consistent: each observer contracts the other's ruler by the same $\Gamma_0$, and the resolution of the ladder-and-barn paradox rests on this symmetry combined with the relativity of simultaneity.

- **[[Def - Lorentz Factor and Relative Velocity]]** — reciprocity is, at bottom, the symmetry of the scalar product $u\cdot u' = u'\cdot u$. That single symmetry of the Minkowski metric is what guarantees the Lorentz factor between two observers is direction-independent, and the magnitude equality of relative velocities is its immediate corollary.

- **The hyperbolic-angle picture of rapidity** — writing $\Gamma_0 = \cosh\varphi$ with $\varphi$ the rapidity between the worldlines, reciprocity is the statement that the hyperbolic angle between two lines does not depend on which line is taken first, exactly as the Euclidean angle between two lines is symmetric. This is the cleanest way to see why the magnitudes must agree.

---

# Unlocked by This

> [!tip] The Symmetry of the Thomas Rotation *(from the Lorentz Group)*
> Reciprocity says the boost from $\mathcal{O}$ to $\mathcal{O}'$ and back are inverse boosts of equal rapidity — but their composition with a *third* observer's boost fails to close, and the failure is the **Thomas–Wigner rotation**. The fact that $U' \ne -U$ (the reciprocal velocity is *rotated*, not merely reversed) is the kinematic first sign that boosts do not commute and do not form a subgroup; the systematic development is [[Special Relativity IX — The Lorentz Group, Structure and Classification]].
