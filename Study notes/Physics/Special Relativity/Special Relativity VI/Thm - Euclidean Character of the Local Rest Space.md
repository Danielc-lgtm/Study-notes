---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - Classification of Four-Vectors"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a spacelike vector has $X\cdot X < 0$. The [[Def - Observer and Local Rest Space|local rest space]] of an observer is $E_{U_0} = U_0^\perp$, with $U_0\cdot U_0 = +1$. The **spatial metric** on the rest space is $h(X,Y) = -\,g(X,Y) = -X\cdot Y$; the spatial norm is $\|X\| = \sqrt{h(X,X)} = \sqrt{-X\cdot X}$. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

> [!warning] Convention
> Gourgoulhon (mostly-plus, $\vec u\cdot\vec u = -1$) finds the metric *already* positive definite on the rest space, $g(\vec v,\vec v)\geq 0$, because his spacelike vectors have $g > 0$. In our mostly-minus convention spacelike vectors have $X\cdot X < 0$, so the metric restricted to the rest space is *negative* definite, and one flips its sign to obtain the positive-definite spatial metric $h = -g|_{E_{U_0}}$. The numerical distances and angles are identical in both conventions.

---

# Statement

> **Euclidean character of the local rest space.** Let $\mathcal{O}$ be an observer with four-velocity $U_0$ and local rest space $E_{U_0} = U_0^\perp$. Every nonzero vector of $E_{U_0}$ is spacelike, so the metric restricted to $E_{U_0}$ is negative definite (in mostly-minus signature), and its negative
> $$h \;:=\; -\,g\big|_{E_{U_0}}, \qquad h(X,Y) = -X\cdot Y,$$
> is a **positive-definite** inner product. Thus $(E_{U_0},\, h)$ is a genuine three-dimensional **Euclidean space**: the spatial norm $\|X\| = \sqrt{-X\cdot X}$ is a norm in the strict sense, it induces a distance $d(M,N) = \|\overrightarrow{MN}\|$ making $\mathscr{E}_{U_0}$ a metric space obeying Pythagoras' theorem, and angles are defined by
> $$\cos\theta = \frac{h(X,Y)}{\|X\|\,\|Y\|} = \frac{-X\cdot Y}{\sqrt{(-X\cdot X)(-Y\cdot Y)}}.$$
> In short, in the local rest space all of vector calculus is identical to ordinary three-dimensional Euclidean calculus.

---

# Motivation

An observer's rest space was defined as the orthogonal complement $U_0^\perp$ of the four-velocity — an abstract three-dimensional slice of spacetime. But an observer does not experience their space as an abstract slice; they experience it as ordinary Euclidean three-space, where the Pythagorean theorem holds, lengths add in quadrature, and angles behave normally. This theorem is the guarantee that the abstract definition delivers the familiar experience: the rest space, with the right sign on the metric, *is* Euclidean $\mathbb{R}^3$.

The result is what licenses every spatial computation in the rest of the chapter. Once you know $(E_{U_0}, h)$ is Euclidean, you may compute distances, project onto subspaces, build orthonormal triads, take cross products, and apply Pythagoras inside the rest space with no relativistic caveats at all — the strangeness of Minkowski geometry (null vectors, the reversed triangle inequality, the light cone) lives entirely in the time direction $U_0$, and projecting it out leaves the residue you grew up with. The radar distance of Synge's formula, the orthonormal local frame, the cross product defining the spatial rotation $\vec\omega$ — all of these presuppose that the rest space is honestly Euclidean.

There is also a conceptual surprise to digest: an *indefinite* metric on spacetime produces a *definite* metric on the rest space. The resolution, made precise by the theorem, is that the one positive-norm direction of spacetime is used up by the four-velocity, leaving the orthogonal complement with three negative-norm directions, which a sign flip turns into three positive-norm Euclidean directions. The signature $(1,3)$ is, read this way, exactly "one timelike direction whose orthogonal complement is Euclidean three-space".

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ lies in $U_0^\perp$ for a timelike $U_0$". The point is to recognise this in disguise.

The first disguised source is **"$X$ is a displacement between two simultaneous events"**. By [[Def - Einstein-Poincaré Simultaneity|the simultaneity criterion]], such a displacement is orthogonal to $U_0$, hence in the rest space, hence spacelike — so the theorem makes it have a well-defined positive spatial length. The bridge is "simultaneous $\Rightarrow$ orthogonal to $U_0$ $\Rightarrow$ in $E_{U_0}$". *Example problem:* show that the spatial separation an observer measures between two simultaneous events has a frame-independent (for that observer) Euclidean length.

The second disguised source is **"$X$ is the relative velocity of a particle for $\mathcal{O}$"**. The relative velocity $V$, built by projecting a particle's four-velocity, lies in the rest space by construction; the theorem makes $\|V\|$ a genuine speed and guarantees $\|V\| < 1$ (a separate fact, but the Euclidean norm is what "speed" means). *Example problem:* show that the magnitude of an observed three-velocity is a Euclidean norm in the rest space.

The third disguised source is **"$X$ is the projection $\Pi(Y)$ of any vector"**. Whatever $Y$ is, its [[Def - The Orthogonal Projector onto the Local Rest Space|spatial part]] $\Pi(Y) = Y - (Y\cdot U_0)U_0$ lies in the rest space and is therefore spacelike, with a Euclidean length. The bridge is that the projector lands in $E_{U_0}$ by idempotence. *Example problem:* compute the "spatial magnitude" of the electric field an observer measures, $\|\Pi(\text{something})\|$.

**Targets (Output Amplification)**

The conclusion is "$(E_{U_0}, h)$ is Euclidean three-space".

Combine the conclusion with **the Gram–Schmidt process**. Since $(E_{U_0}, h)$ is a positive-definite three-dimensional inner-product space, one can always build an $h$-orthonormal basis $(e_1, e_2, e_3)$ of it. The further result is the spatial triad of the [[Def - Local Frame and Four-Rotation|local frame]]: together with $e_0 = U_0$ it forms a pseudo-orthonormal tetrad of spacetime. The combination is useful because it manufactures the observer's coordinate axes out of nothing but the Euclidean structure.

Combine the conclusion with **the cross product**. A three-dimensional oriented Euclidean space carries a cross product; in the rest space it is $\vec v\times_{U_0}\vec w = \epsilon(U_0, \vec v, \vec w, \cdot)^\sharp$, built from the spacetime [[Def - Spacetime Orientation|Levi-Civita tensor]] restricted to the rest space. The further result is the apparatus for the spatial rotation $\vec\omega$ of the four-rotation and, later, the magnetic field. The combination is nonobvious because it shows the three-dimensional vector calculus of $\nabla\times$, $\vec v\times\vec w$, and the scalar triple product all live, unchanged, inside the rest space.

Combine the conclusion with **Pythagoras and the triangle inequality**. Because $h$ is positive definite, the ordinary (un-reversed) triangle inequality $\|X + Y\|\leq\|X\| + \|Y\|$ holds in the rest space — in stark contrast to the *reversed* triangle inequality for timelike vectors. The further result is that spatial geometry is genuinely Euclidean and not Minkowskian: the strangeness is confined to the time direction. The combination is useful as a sanity check — any spatial computation may be cross-checked against ordinary $\mathbb{R}^3$ intuition.

---

# Why Is It True

The whole theorem turns on one prior fact: **any nonzero vector orthogonal to a timelike vector is spacelike.** Grant that, and the rest is bookkeeping.

Here is why orthogonality to timelike forces spacelike. Work in an orthonormal frame where $U_0 = (1, 0, 0, 0)$. A vector $X$ orthogonal to $U_0$ satisfies $X\cdot U_0 = X^0 = 0$, so $X = (0, X^1, X^2, X^3)$ is purely spatial in this frame, and $X\cdot X = -(X^1)^2 - (X^2)^2 - (X^3)^2 \leq 0$, with equality only if $X = 0$. So every nonzero $X\in U_0^\perp$ has $X\cdot X < 0$: spacelike. (Frame-independently: the metric has signature $(1,3)$, the single $+$ is carried by $U_0$, and Sylvester's law forces the orthogonal complement to carry the three $-$'s.)

Now the Euclidean character. The restriction $g|_{E_{U_0}}$ is a symmetric bilinear form on the three-dimensional $E_{U_0}$, and we have just shown its quadratic form is $\leq 0$, vanishing only at $0$ — it is negative definite. Flip the sign: $h = -g|_{E_{U_0}}$ is positive definite. A positive-definite symmetric bilinear form on a finite-dimensional real space is, by definition, a Euclidean inner product, and a three-dimensional Euclidean inner-product space is isometric to $\mathbb{R}^3$ with the dot product. Everything Euclidean — norm, distance, Pythagoras, angles, orthonormal bases, cross products — follows from positive-definiteness alone.

The one-line summary: **the timelike $U_0$ soaks up the single plus sign of the signature, so its orthogonal complement is left with three minus signs, and flipping them gives Euclidean $\mathbb{R}^3$.** The indefiniteness of spacetime and the definiteness of space are two sides of the same signature.

---

# What Makes This Hard

The only genuinely substantive step is the lemma "orthogonal to timelike $\Rightarrow$ spacelike", and the place people stumble is trying to prove it without choosing an adapted frame — the cleanest argument picks the frame where $U_0$ is the time axis, reducing it to a one-line sign computation. The common confusion is the sign: in mostly-minus the rest-space metric is *negative* definite, and one must remember to flip it to get the Euclidean $h$; forgetting the flip leads to "negative lengths" and apparent nonsense. A subtler trap is to expect the *reversed* triangle inequality (which holds for timelike vectors) inside the rest space — but spacelike vectors in a definite subspace obey the *ordinary* triangle inequality, because $h$ is a genuine positive-definite norm.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove that vectors orthogonal to the timelike $U_0$ are spacelike (work in the frame where $U_0$ is the time axis), deduce the restricted metric is negative definite, flip its sign to get a positive-definite $h$, and invoke that a positive-definite three-dimensional form is Euclidean.

**Subgoal decomposition:**

1. **Orthogonal to timelike is spacelike.** Show $X\in U_0^\perp$, $X\neq 0\Rightarrow X\cdot X < 0$.
   - *Hint:* In the frame $U_0 = (1,\mathbf 0)$, orthogonality kills $X^0$, leaving $X\cdot X = -|\mathbf X|^2$.
   - *Why needed:* It is the one nontrivial input; everything else is definitional.

2. **The restricted metric is negative definite; its negative is positive definite.** Set $h = -g|_{E_{U_0}}$.
   - *Hint:* Negative definite means $g(X,X) < 0$ for $X\neq 0$, which subgoal 1 gives; negate.
   - *Why needed:* It produces a bona fide Euclidean inner product.

3. **A positive-definite three-dimensional form is Euclidean.** Conclude $(E_{U_0}, h)\cong\mathbb{R}^3$.
   - *Hint:* Definition of Euclidean space; Gram–Schmidt gives an $h$-orthonormal basis.
   - *Why needed:* It delivers Pythagoras, angles, distances, cross products.

---

# Lemma Decomposition

> [!note]- Lemma 1: A nonzero vector orthogonal to a timelike vector is spacelike
> **Statement:** If $U_0$ is timelike and $X\neq 0$ satisfies $X\cdot U_0 = 0$, then $X\cdot X < 0$.
>
> **Hint:** Choose an orthonormal frame in which $U_0$ is the time axis.
>
> **Why needed:** It is the sole nontrivial input; the Euclidean character is then automatic.
>
> > [!note]- Full proof
> > Since $U_0$ is timelike, there is an orthonormal basis with $U_0 = U_0^0\,e_0$ and $U_0^0\neq 0$ (boost so that $U_0$ has no spatial part; concretely the rest frame of $U_0$). Then $X\cdot U_0 = U_0^0\,X^0$ (using $\eta = \mathrm{diag}(1,-1,-1,-1)$ and $X\cdot U_0 = X^0 U_0^0$ since $U_0$ is purely temporal), so $X\cdot U_0 = 0$ forces $X^0 = 0$. Hence $X = (0, X^1, X^2, X^3)$ and
> > $$X\cdot X = (X^0)^2 - (X^1)^2 - (X^2)^2 - (X^3)^2 = -\big[(X^1)^2 + (X^2)^2 + (X^3)^2\big] \leq 0,$$
> > with equality iff $X^1 = X^2 = X^3 = 0$, i.e. iff $X = 0$. Since $X\neq 0$, $X\cdot X < 0$: $X$ is spacelike. (This is frame-independent: $X\cdot X$ is a Lorentz invariant.) $\blacksquare$

> [!note]- Lemma 2: The restricted metric is negative definite and $h$ is positive definite
> **Statement:** $g|_{E_{U_0}}$ is negative definite, and $h = -g|_{E_{U_0}}$ is positive definite.
>
> **Hint:** Lemma 1 says $g(X,X) < 0$ for nonzero $X\in E_{U_0}$; negate.
>
> **Why needed:** It packages the spacelike property as a genuine Euclidean inner product.
>
> > [!note]- Full proof
> > $g|_{E_{U_0}}$ is symmetric and bilinear (restriction of a symmetric bilinear form). By Lemma 1, $g(X,X) = X\cdot X < 0$ for every nonzero $X\in E_{U_0}$, and $g(0,0) = 0$; so $g|_{E_{U_0}}$ is negative definite. Therefore $h(X,Y) := -g(X,Y)$ is symmetric, bilinear, with $h(X,X) = -X\cdot X > 0$ for $X\neq 0$ and $h(0,0) = 0$: positive definite. $\blacksquare$

> [!note]- Lemma 3: A positive-definite three-dimensional inner-product space is Euclidean $\mathbb{R}^3$
> **Statement:** $(E_{U_0}, h)$ is isometric to $(\mathbb{R}^3, \cdot)$; it admits an $h$-orthonormal basis, obeys Pythagoras, and supports angles and a cross product.
>
> **Hint:** Apply Gram–Schmidt to any basis of the three-dimensional $E_{U_0}$ using $h$.
>
> **Why needed:** It is the conclusion: full Euclidean vector calculus in the rest space.
>
> > [!note]- Full proof
> > $E_{U_0}$ is three-dimensional (orthogonal complement of a line in a four-dimensional non-degenerate space). On a finite-dimensional real vector space, a positive-definite symmetric bilinear form is by definition a Euclidean inner product; Gram–Schmidt applied to any basis (legal because $h$ is positive definite, so no nonzero vector has zero norm and no division by zero occurs) yields an $h$-orthonormal basis $(e_1, e_2, e_3)$ with $h(e_i, e_j) = \delta_{ij}$. In this basis $h$ is the standard dot product, so $(E_{U_0}, h)\cong(\mathbb{R}^3, \cdot)$. The norm $\|X\| = \sqrt{h(X,X)}$ satisfies the triangle inequality and the parallelogram law; the distance $d(M,N) = \|\overrightarrow{MN}\|$ makes $\mathscr{E}_{U_0}$ a metric space; Pythagoras holds for $h$-orthogonal vectors; angles are defined by $\cos\theta = h(X,Y)/(\|X\|\|Y\|)$ (well-defined by Cauchy–Schwarz for the positive-definite $h$); and the orientation from the spacetime Levi-Civita tensor gives a cross product. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{O}$ have timelike four-velocity $U_0$ and rest space $E_{U_0} = U_0^\perp$.
>
> By Lemma 1, every nonzero $X\in E_{U_0}$ is spacelike, $X\cdot X < 0$: in the rest frame of $U_0$, orthogonality forces $X^0 = 0$ and then $X\cdot X = -|\mathbf X|^2 < 0$.
>
> By Lemma 2, the restriction $g|_{E_{U_0}}$ is therefore negative definite, and $h := -g|_{E_{U_0}}$ is a positive-definite symmetric bilinear form.
>
> By Lemma 3, the three-dimensional positive-definite inner-product space $(E_{U_0}, h)$ is isometric to Euclidean $\mathbb{R}^3$: it has an $h$-orthonormal basis, the norm $\|X\| = \sqrt{-X\cdot X}$ is a genuine norm, the induced distance makes $\mathscr{E}_{U_0}$ a metric space obeying Pythagoras, angles are defined by $\cos\theta = -X\cdot Y/(\|X\|\|Y\|)$, and the rest space carries a cross product.
>
> Hence in the local rest space all of vector calculus is identical to ordinary three-dimensional Euclidean calculus. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The $3+1$ split and the spatial metric (general relativity).** In the Hamiltonian formulation of general relativity, the metric induced on a spacelike slice by the projector is exactly this $h$, and its positive-definiteness is what makes the slice a Riemannian three-manifold carrying genuine spatial geometry. Recognising that the Lorentzian signature of spacetime is precisely what makes the spatial slices Riemannian is the deep application; the entire ADM formalism rests on it.

**Gram–Schmidt with an indefinite metric (linear algebra).** Building the local frame requires an $h$-orthonormal triad of the rest space, obtained by Gram–Schmidt — but one must use the *positive-definite* $h$, not the indefinite $g$, or the process can divide by a zero "norm". Comparing Gram–Schmidt in the definite rest space with the indefinite Gram–Schmidt of [[Special Relativity III — Minkowski Spacetime and the Metric|the full spacetime]] is an instructive drill: the rest space is where the process is unproblematic.

**The hyperboloid of four-velocities as hyperbolic space (geometry).** The future unit timelike vectors form a hyperboloid, a model of hyperbolic three-space, and its Riemannian metric at the point $U_0$ is exactly the spatial metric $h$ on the tangent space $U_0^\perp$. Thus the Euclidean character of the rest space is the statement that the velocity hyperboloid is a Riemannian (indeed hyperbolic) manifold. The application is surprising because it ties the observer's flat rest space to the curved geometry of velocity space, with rapidity as hyperbolic distance.

---

# Bridges

- **[[Def - Classification of Four-Vectors]]** — the engine of the theorem is the classification fact "orthogonal to timelike is spacelike". The Euclidean character of the rest space is that fact applied to all three dimensions of the orthogonal complement at once.

- **[[Def - The Orthogonal Projector onto the Local Rest Space]]** — the projector lands every vector in this Euclidean rest space, so $\|\Pi(X)\|$ is always a well-defined positive spatial length. The projector and the Euclidean structure are the two halves of "extract the spatial part and measure it".

- **[[Def - Semi-Riemannian Metric and Signature]]** — the theorem is the local, flat instance of the general fact that a Lorentzian (signature $(1, n)$) metric induces a Riemannian (positive-definite) metric on any spacelike hypersurface. The signature bookkeeping — one timelike direction, Riemannian complement — is the same.

- **The reversed triangle inequality** — the contrast is instructive: timelike vectors obey the *reversed* triangle inequality (straight worldline is longest), but spacelike vectors in the definite rest space obey the *ordinary* triangle inequality (straight path is shortest). The sign of the norm is what flips the inequality, and the rest space is where the ordinary one is restored. (See [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group]].)

---

# Unlocked by This

> [!tip] The Orthonormal Local Frame and Observer Coordinates *(from §6.2)*
> Because the rest space is Euclidean, Gram–Schmidt produces an orthonormal spatial triad $(e_1, e_2, e_3)$; together with $e_0 = U_0$ this is the pseudo-orthonormal [[Def - Local Frame and Four-Rotation|local frame]], the observer's coordinate axes, and the reference space $R_{\mathcal{O}}$ is the abstract Euclidean $\mathbb{R}^3$ it maps onto.

> [!tip] The Cross Product and the Spatial Rotation *(from §6.3)*
> The orientation inherited from the spacetime Levi-Civita tensor equips the Euclidean rest space with a cross product $\times_{U_0}$, which is exactly the operation appearing in the spatial-rotation part $\vec\omega\times_{U_0}e_\alpha$ of the [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|four-rotation]], and later in the magnetic field.

> [!tip] Riemannian Spatial Slices in the 3+1 Formalism *(from General Relativity)*
> The positive-definiteness of $h$ is what makes the spatial slices of a $3+1$ decomposition genuine **Riemannian three-manifolds**, carrying the dynamical spatial metric of the Hamiltonian (ADM) formulation of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]]; the Lorentzian signature of spacetime is precisely the condition that an observer's space be Riemannian.
