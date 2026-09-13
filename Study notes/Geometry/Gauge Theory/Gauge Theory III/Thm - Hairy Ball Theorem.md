---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - The Brouwer Degree is an Integer and a Homotopy Invariant"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Thm - Regular Value Theorem on Manifolds"
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
  - "Thm - Fundamental Theorem on Flows"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $S^m = \{x \in \mathbb{R}^{m+1} : \lvert x \rvert = 1\}$ denotes the unit sphere in Euclidean space $\mathbb{R}^{m+1}$, where $\lvert x \rvert = \langle x, x\rangle^{1/2}$ and $\langle\cdot,\cdot\rangle$ is the standard inner product $\langle x, y\rangle = \sum_{i=0}^{m} x_i y_i$. It is a smooth, closed (compact without boundary) $m$-dimensional manifold, and it is connected for $m \geq 1$ (the case $m = 0$, where $S^0 = \{-1, +1\}$ is two points, is dispatched separately in the proof; the Brouwer degree used below requires a connected target and is therefore applied only for $m \geq 1$). We orient $S^m$ by the **outward-normal-first convention**: an ordered basis $(e_1, \dots, e_m)$ of the tangent space $T_x S^m$ is declared positively oriented if and only if $(x, e_1, \dots, e_m)$ is a positively oriented basis of $\mathbb{R}^{m+1}$ with its standard orientation, where $x$ is the outward unit normal at $x$. This is the [[Def - Orientation of a Smooth Manifold|orientation]] induced on the boundary $S^m = \partial \overline{B^{m+1}}$ of the closed unit ball, and it is the same convention under which $SU(2) \cong S^3$ is oriented in this series.

A **tangent vector field** on $S^m$ is a smooth section $v \in \Gamma(TS^m)$; concretely, identifying $T_x S^m$ with the linear subspace $x^\perp = \{w \in \mathbb{R}^{m+1} : \langle x, w\rangle = 0\}$ of $\mathbb{R}^{m+1}$ (justified in Lemma 1 below), it is a smooth map $v : S^m \to \mathbb{R}^{m+1}$ with $\langle x, v(x)\rangle = 0$ for all $x$. The field is **nowhere-vanishing** if $v(x) \neq 0$ for all $x \in S^m$. The **antipodal map** is $a : S^m \to S^m$, $a(x) = -x$, the restriction of $-\operatorname{id}_{\mathbb{R}^{m+1}}$.

We write $\deg f \in \mathbb{Z}$ for the [[Def - Brouwer Degree of a Map|Brouwer degree]] of a smooth map $f$ between closed oriented $m$-manifolds with connected target, and $O(m+1) = \{A \in GL(m+1; \mathbb{R}) : A^{\mathsf T} A = I\}$ for the orthogonal group, acting on $\mathbb{R}^{m+1}$ by matrix multiplication. For a Lie group $G$ with Lie algebra $\mathfrak{g} = T_e G$ acting smoothly on a manifold $M$ on the left (the series convention for group actions on manifolds), the [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] of $X \in \mathfrak{g}$ is the smooth section $\bar X \in \Gamma(TM)$, $\bar X(p) = d_e \ell_p(X)$, where $\ell_p : G \to M$, $\ell_p(g) = g \cdot p$ is the orbit map through $p$; $\exp : \mathfrak{g} \to G$ is the [[Def - Exponential Map of a Lie Group|Lie-group exponential]].

> [!warning] Convention: what this page proves, and what it does not
> Bär records the obstruction in the reverse-implication form (Remark 1.5.19): "if $M$ carries a nowhere-vanishing vector field then $\chi(M) = 0$, so $M \not\cong S^{2n}$", invoking the general Poincaré–Hopf theorem without proof. We prove instead the *direct* statement below — that $S^{2n}$ carries no nowhere-vanishing field — which is precisely the case the sources use (Haydys's hint I2.1.1 to Exercise X2.1.2, and Bär's obstruction to free actions). The general Poincaré–Hopf equality $\sum_x \operatorname{ind}_x v = \chi(M)$ for an arbitrary closed manifold $M$ is **not** claimed here; it is a separate result reached by another route (see Bridges, [[Thm - Poincare-Hopf Theorem for Surfaces]] for the surface case).

---

# Statement

> **Theorem (Hairy Ball Theorem).** For every $n \geq 0$, the even-dimensional sphere $S^{2n}$ admits no nowhere-vanishing tangent vector field. Equivalently, every smooth tangent vector field $v \in \Gamma(TS^{2n})$ has a zero: there exists $x \in S^{2n}$ with $v(x) = 0$.

Three consequences are recorded as corollaries; each is proved in full in the Formal Proof section.

> **Corollary 1 (homotopy rigidity of the antipodal map).** The antipodal map $a : S^{2n} \to S^{2n}$, $a(x) = -x$, is not smoothly homotopic to the identity $\operatorname{id}_{S^{2n}}$.

> **Corollary 2 (non-triviality of the tangent bundle).** The tangent bundle $TS^{2n}$ is not trivial, and the [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(TS^{2n})$ admits no global smooth section.

> **Corollary 3 (no free positive-dimensional actions).** No Lie group $G$ with $\dim G \geq 1$ acts smoothly and freely on $S^{2n}$.

The three corollaries are tied together by one mechanism: each of a global trivialisation of $TS^{2n}$, a global frame, and the fundamental vector field of a nonzero Lie-algebra element of a freely acting group would *produce* a nowhere-vanishing tangent field, which the theorem forbids. Corollary 1 is not a consequence but a by-product: it is the exact statement about degrees that the proof of the theorem establishes.

---

# Motivation

The question the theorem answers is elementary to pose and its answer is the prototype of every obstruction argument in bundle theory: *can one comb a sphere flat?* A tangent vector field on $S^m$ assigns to each point a tangent direction, varying smoothly; a nowhere-vanishing one is a way of "combing the hair" so that no cowlick or bald spot ever appears. On the circle $S^1$ one can: the field $v(\cos\theta, \sin\theta) = (-\sin\theta, \cos\theta)$ points always counterclockwise and never vanishes. On the ordinary two-sphere $S^2$ one cannot, and the reason is not a failure of ingenuity but a topological law.

The importance of this fact for gauge theory is that it is the first instance, and the cleanest, of the central theme of Chapter III: *a bundle can fail to admit a section, and the failure is detected by an integer that is invariant under deformation*. Here the bundle is $TS^{2n}$, the section sought is a nowhere-vanishing field, and the deforming integer is the Brouwer degree. Exactly the same shape of argument — build a map to a sphere or a group, compute its degree or winding number, and observe that the arithmetic is inconsistent with the section existing — reappears when we show the Hopf bundle is nontrivial (§3.5, via the winding number of $z/\lvert z\rvert$), when we classify $U(1)$- and $SU(2)$-bundles (§3.6), and when the second Chern number obstructs triviality of an instanton bundle (Chapter VI). The hairy ball theorem is where this reasoning is stripped to its bones.

There is a second reason the theorem sits in this chapter rather than in a topology course. Bär uses it to close off a natural question about symmetry: *which manifolds can be homogeneous under a continuous group in a fixed-point-free way?* If a Lie group of positive dimension acts freely on $M$, then differentiating a one-parameter subgroup produces a nowhere-vanishing vector field on $M$ (the orbits are one-dimensional and never degenerate, because the action is free). So a free action is a *source* of nowhere-vanishing fields, and the hairy ball theorem, read contrapositively, says that even-dimensional spheres are too rigid to admit one. This is why $S^2$, unlike $S^1$ and $S^3$, is not a Lie group and carries no free circle action, whereas $S^3 = SU(2)$ is a group and $S^1 = U(1)$ acts on itself.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's own hypothesis is minimal — one only needs the manifold to be an even sphere — so the "source" question is which problems secretly ask whether $S^{2n}$ has a nowhere-vanishing field without naming one.

The first disguised source is **a claim that a rank-$k$ real bundle over $S^{2n}$ is trivial, or admits $k$ independent sections**. Triviality of a rank-$k$ bundle $E \to S^{2n}$ means an isomorphism $E \cong S^{2n} \times \mathbb{R}^k$, and the constant section $x \mapsto (x, e_1)$ then transports to a nowhere-vanishing section of $E$. When $E = TS^{2n}$ this is a nowhere-vanishing field, and the theorem forbids it; so "is $TS^{2n}$ trivial?" is the hairy ball theorem in disguise. The bridge is: *a trivial bundle has a nowhere-vanishing section, indeed a full frame.* *Example problem:* prove that $S^2$ is not parallelisable, i.e. $TS^2 \not\cong S^2 \times \mathbb{R}^2$ (this is Haydys's Exercise X2.1.2, worked as [[Ex - The Tangent Bundle of S^2 is Nontrivial]]).

The second disguised source is **a smooth free action of a positive-dimensional Lie group on a compact manifold suspected to be $S^{2n}$**. As explained in the Motivation, freeness plus $\dim G \geq 1$ manufactures a nowhere-vanishing field. The non-obvious step is recognising that the *infinitesimal generator* of a one-parameter subgroup, the fundamental vector field $\bar X$, is nowhere-vanishing precisely because the action is free: a zero of $\bar X$ would be a point fixed by the whole subgroup $\{\exp(tX)\}$. *Example problem:* show that $U(1)$ cannot act freely on $S^2$, so that $S^2$ is not the total space of a circle bundle in the way $S^3$ is (the Hopf bundle).

The third disguised source is **a claim that two self-maps of $S^{2n}$ related by a rotation-through-a-field are homotopic**, or more generally any assertion that the antipodal map has even degree. The homotopy $x \mapsto \cos(\pi t)x + \sin(\pi t)w(x)$ built from a unit field $w$ is exactly the "rotate each point a half-turn along its tangent direction" motion; its existence would make $\operatorname{id}$ and $a$ homotopic. The bridge is: *a nowhere-vanishing field is the same data as a homotopy from the identity to the antipodal map.* *Example problem:* decide whether the map $x \mapsto -x$ on $S^4$ can be deformed to the identity (it cannot, because its degree is $-1$).

**Targets (Output Amplification)**

The bare conclusion — no nowhere-vanishing field — becomes much more when combined with structural facts about bundles.

Combine the theorem with the **section–triviality dictionary for principal bundles** ([[Thm - Sections of a Principal Bundle and Triviality]]: a principal bundle is trivial if and only if it has a global section; a vector bundle $E$ is trivial if and only if $\operatorname{Fr}(E)$ has a global section). The further result is Corollary 2: $\operatorname{Fr}(TS^{2n})$ has no section and $TS^{2n}$ is nontrivial. This is non-obvious because it converts a statement about *one* section (a single nowhere-vanishing field) into a statement about the *entire* frame bundle, an object of dimension $2n + (2n)^2 = 2n(2n+1)$ (the base dimension $2n$ plus the fibre dimension $\dim GL(2n; \mathbb{R}) = (2n)^2$).

Combine the theorem with the **Euler class and Chern–Weil theory** (Chapter VI). The obstruction to a nowhere-vanishing section of an oriented rank-$m$ bundle over an $m$-manifold is its Euler number, and for $TS^{2n}$ this number is $\chi(S^{2n}) = 2$. The further result is that the hairy ball theorem is the vanishing statement $\chi(S^{2n}) \neq 0$ made concrete; running the same degree computation with signs counts the zeros of a generic field and recovers $2$. The extra ingredient is the theory of characteristic numbers as integrals of curvature.

Combine the theorem with **classification of homogeneous spaces**. Knowing that $S^{2n}$ admits no free positive-dimensional action (Corollary 3), together with the fact that a transitive action of a compact group realises $M$ as $G/H$, restricts which spheres can be Lie groups: only $S^0, S^1, S^3$ are (and $S^7$ is a parallelisable non-group). The payoff is the identification of $S^1 = U(1)$ and $S^3 = SU(2)$ as the only spheres appearing as structure groups in this series, with $S^2 = \mathbb{CP}^1$ appearing instead as a base.

---

# Why Is It True

Set aside the formal machinery and picture the two-sphere. Suppose there *were* a nowhere-vanishing tangent field; normalise it to unit length, so at each point $x$ we have a unit tangent vector $w(x)$ perpendicular to $x$. Now rotate: in the plane spanned by $x$ and $w(x)$, turn $x$ toward $w(x)$ by an angle $\pi t$. At time $t = 0$ the point sits still; as $t$ runs to $1$ the point swings through a half-circle and lands exactly at $-x$. Because $x$ and $w(x)$ are orthogonal unit vectors, the swinging point $\cos(\pi t)x + \sin(\pi t)w(x)$ never leaves the sphere. So the field would give us a continuous, indeed smooth, motion carrying the identity map of the sphere onto the antipodal map.

The contradiction is now a matter of counting. The Brouwer degree assigns to every self-map of the sphere an integer that does not change under smooth deformation and equals the signed number of preimages of a generic point. The identity map has degree $+1$: a generic point has exactly one preimage, itself, counted with $+$. The antipodal map $x \mapsto -x$ is an orthogonal transformation with determinant $(-1)^{2n+1} = -1$; an orthogonal transformation acts on the sphere with degree equal to its determinant, because it either preserves or reverses the outward-normal orientation according to that sign. So the antipodal map has degree $-1$. If the identity could be deformed into the antipodal map, their degrees would have to agree, and we would have $1 = -1$.

> **The mechanism in one sentence:** a nowhere-vanishing field would let us rotate the sphere half a turn everywhere at once, deforming the identity into the antipodal map, but the identity has degree $+1$ and the antipodal map of an even sphere has degree $-1$, and degree is deformation-invariant.

The parity of the dimension is doing all the work, and it enters at exactly one point: the sign of $\det(-I) = (-1)^{m+1}$. For $m$ even this is $-1$ and the argument bites; for $m$ odd, as on $S^1$ and $S^3$, it is $+1$, the antipodal map is homotopic to the identity, and indeed a nowhere-vanishing field exists (on $S^{2k-1} \subset \mathbb{C}^k$ take $w(x) = ix$). The theorem is a statement about the parity of the ambient dimension, disguised as a statement about hair.

---

# What Makes This Hard

The single non-obvious construction is the homotopy: seeing that a nowhere-vanishing field is *equivalent data* to a deformation of the identity into the antipodal map, and checking that the rotated point stays on the sphere (this uses orthogonality $\langle x, w(x)\rangle = 0$ and unit length in an exact cancellation, not an approximation). The common error is to attempt the theorem by a local or intuitive argument — "the hair must part somewhere" — which is genuinely false in odd dimensions and therefore cannot be a proof in even dimensions; any correct argument must use the parity, and the only place parity can enter honestly is the determinant sign of the antipodal map. A second subtlety is that the degree computation for the antipodal map must fix an orientation convention and track how the orthogonal map moves it; skipping this and asserting "$\deg a = \pm 1$, say $-1$" hides precisely the parity that is the content of the theorem.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Assume a nowhere-vanishing field exists and derive a contradiction from the Brouwer degree. Normalise the field to unit length, use it to build an explicit smooth homotopy from the identity to the antipodal map, then compute the two degrees ($+1$ and $-1$) and observe they must be equal but are not.

**Subgoal decomposition:**

1. **Identify tangent vectors with the orthogonal complement.** Show $T_x S^m = x^\perp$, so that a tangent field is an $\mathbb{R}^{m+1}$-valued map $v$ with $\langle x, v(x)\rangle = 0$, and a nowhere-vanishing one normalises to a unit tangent field $w = v/\lvert v\rvert$.
   - *Hint:* $S^m$ is the regular level set $f^{-1}(1)$ of $f(x) = \langle x, x\rangle$; compute $df_x$.
   - *Why needed:* Without the concrete description of tangent vectors, the homotopy formula cannot be written or its values checked to lie on the sphere.

2. **Compute the degree of an orthogonal map on the sphere.** Show that for $A \in O(m+1)$ the restriction $A|_{S^m}$ has degree $\det A$; deduce $\deg \operatorname{id} = 1$ and $\deg a = (-1)^{m+1}$.
   - *Hint:* $A|_{S^m}$ is a diffeomorphism, so every point is a regular value with a single preimage; the sign of the determinant of $dA_x$ is $\det A$ once tangent spaces are oriented by the outward normal.
   - *Why needed:* This is the arithmetic that the two ends of the homotopy must satisfy; the parity of the dimension lives here.

3. **Build the homotopy from a unit field.** Given a unit tangent field $w$ on $S^{2n}$, show $F(x, t) = \cos(\pi t)x + \sin(\pi t)w(x)$ is a smooth homotopy $S^{2n} \times [0,1] \to S^{2n}$ from $\operatorname{id}$ to $a$.
   - *Hint:* Compute $\lvert F(x, t)\rvert^2$ using $\langle x, w(x)\rangle = 0$; evaluate at $t = 0, 1$.
   - *Why needed:* It is the bridge that turns the hypothetical field into a statement about degrees.

4. **Assemble the contradiction.** Combine subgoals 2 and 3 with the homotopy-invariance of degree to get $1 = -1$.
   - *Hint:* Homotopic maps have equal degree.
   - *Why needed:* This is the theorem.

5. **Discharge the corollaries.** From the theorem deduce (1) $a \not\simeq \operatorname{id}$, (2) $TS^{2n}$ nontrivial and $\operatorname{Fr}(TS^{2n})$ sectionless, (3) no free positive-dimensional action.
   - *Hint:* Each corollary produces a nowhere-vanishing field, contradicting the theorem; for (3) use that a zero of a fundamental vector field is a fixed point of a one-parameter subgroup.
   - *Why needed:* These are the uses the sources make of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The tangent space of the sphere is the orthogonal complement of the position vector
> **Statement:** For $x \in S^m$, the tangent space is $T_x S^m = x^\perp = \{w \in \mathbb{R}^{m+1} : \langle x, w\rangle = 0\}$. Consequently a smooth map $v : S^m \to \mathbb{R}^{m+1}$ is a tangent vector field if and only if $\langle x, v(x)\rangle = 0$ for all $x$; and if $v$ is nowhere-vanishing then $w := v/\lvert v\rvert$ is a smooth unit tangent field.
>
> **Hint:** Realise $S^m$ as a regular level set of $f(x) = \langle x, x\rangle$ and apply the regular value theorem.
>
> **Why needed:** It converts the abstract notion "tangent field" into an explicit $\mathbb{R}^{m+1}$-valued condition, which is what lets us write the homotopy $F$ and verify $\lvert F\rvert = 1$; the normalisation reduces the general theorem to the unit-field case.
>
> > [!note]- Full proof
> > **Realise the sphere as a regular level set.** Define $f : \mathbb{R}^{m+1} \to \mathbb{R}$ by $f(x) = \langle x, x\rangle = \sum_{i=0}^m x_i^2$, a smooth function, so that $S^m = f^{-1}(1)$. Its differential at $x$ is the linear map
> > $$d f_x(w) = 2\langle x, w\rangle \qquad \text{(directional derivative: } \tfrac{d}{ds}\big|_0 \langle x + sw, x + sw\rangle = 2\langle x, w\rangle\text{)}.$$
> > For $x \in S^m$ we have $x \neq 0$, so $d f_x$ is surjective onto $\mathbb{R}$ (it sends $w = x$ to $2\lvert x\rvert^2 = 2 \neq 0$); hence $1$ is a regular value of $f$.
> >
> > **Apply the regular value theorem.** By the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] — if $y$ is a regular value of a smooth map $f : N \to P$ then $f^{-1}(y)$ is an embedded submanifold with $T_x f^{-1}(y) = \ker d f_x$ at each of its points — the level set $S^m = f^{-1}(1)$ is a smooth embedded $m$-dimensional submanifold of $\mathbb{R}^{m+1}$ and
> > $$T_x S^m = \ker d f_x = \{w \in \mathbb{R}^{m+1} : 2\langle x, w\rangle = 0\} = x^\perp \qquad \text{(by the formula for } d f_x\text{)}.$$
> > This is an $m$-dimensional subspace, matching $\dim S^m = m$.
> >
> > **The field criterion.** Under the standard inclusion $T_x S^m \subset T_x \mathbb{R}^{m+1} = \mathbb{R}^{m+1}$, a smooth section $v$ of $TS^m$ is exactly a smooth map $v : S^m \to \mathbb{R}^{m+1}$ whose value at each $x$ lies in $T_x S^m = x^\perp$, that is, satisfies $\langle x, v(x)\rangle = 0$; conversely any such smooth map is a tangent field. This is the stated equivalence.
> >
> > **Normalisation.** Suppose $v$ is nowhere-vanishing, so $\lvert v(x)\rvert > 0$ for all $x$. Then $x \mapsto \lvert v(x)\rvert = \langle v(x), v(x)\rangle^{1/2}$ is smooth (composition of the smooth $v$, the smooth inner product, and the square root, which is smooth on $(0, \infty)$), and $w := v/\lvert v\rvert$ is a smooth map $S^m \to \mathbb{R}^{m+1}$ with $\lvert w(x)\rvert = 1$ and $\langle x, w(x)\rangle = \lvert v(x)\rvert^{-1}\langle x, v(x)\rangle = 0$. So $w$ is a smooth unit tangent field. $\blacksquare$

> [!note]- Lemma 2: The Brouwer degree of an orthogonal map on the sphere is its determinant
> **Statement:** Let $A \in O(m+1)$. Then $A$ restricts to a diffeomorphism $A|_{S^m}$ of $S^m$, and $\deg(A|_{S^m}) = \det A \in \{+1, -1\}$. In particular $\deg(\operatorname{id}_{S^m}) = 1$, and the antipodal map $a = (-I)|_{S^m}$ has $\deg a = (-1)^{m+1}$.
>
> **Hint:** A diffeomorphism makes every point a regular value with one preimage; compute the sign of $\det d(A|_{S^m})_x$ by tracking how $A$ moves the outward-normal orientation.
>
> **Why needed:** It supplies the two numbers $\deg \operatorname{id} = 1$ and $\deg a = -1$ (for $m = 2n$) whose forced equality is the contradiction; this is where even-dimensionality enters, through $\det(-I) = (-1)^{m+1}$.
>
> > [!note]- Full proof
> > **$A|_{S^m}$ is a diffeomorphism of $S^m$.** Since $A$ is orthogonal, $\lvert Ax\rvert = \lvert x\rvert$, so $A(S^m) \subseteq S^m$; as $A^{-1} = A^{\mathsf T}$ is also orthogonal, $A^{-1}(S^m) \subseteq S^m$ too, and $A|_{S^m}$ is a smooth bijection of $S^m$ with smooth inverse $A^{-1}|_{S^m}$. Thus $A|_{S^m}$ is a diffeomorphism of the closed, connected, oriented $m$-manifold $S^m$, so its degree is defined.
> >
> > **Every point is a regular value with a single preimage.** Fix $y \in S^m$ and let $x_0 = A^{-1}y \in S^m$, the unique preimage. Because $A|_{S^m}$ is a diffeomorphism, its differential $d(A|_{S^m})_{x_0} : T_{x_0}S^m \to T_y S^m$ is a linear isomorphism, so $y$ is a regular value. We now invoke the regular-value formula for the degree.
> >
> > > **Restatement of the tool.** By [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]], clause (b): for closed oriented $m$-manifolds $M, N$ with $N$ connected, a smooth map $f : M \to N$, and any regular value $y \in N$, the preimage $f^{-1}(y)$ is finite and $\deg f = \sum_{x \in f^{-1}(y)} \operatorname{sign}\det d f_x$, where the sign of the determinant is computed with respect to the chosen orientations of $T_x M$ and $T_y N$.
> >
> > Applying this to $f = A|_{S^m}$ at the regular value $y$, whose only preimage is $x_0$,
> > $$\deg(A|_{S^m}) = \operatorname{sign}\det\!\big(d(A|_{S^m})_{x_0}\big) \qquad \text{(regular-value formula, single preimage } x_0\text{)}.$$
> >
> > **Identify the differential.** Because $A$ is linear, its restriction to the submanifold $S^m$ has differential equal to $A$ itself restricted to tangent spaces:
> > $$d(A|_{S^m})_{x_0} = A|_{T_{x_0}S^m} : T_{x_0}S^m \to T_y S^m \qquad \text{(differential of a linear map is the map)},$$
> > and this is well-defined as a map into $T_y S^m$ because $A(x_0^\perp) = (A x_0)^\perp = y^\perp$ (orthogonal maps preserve orthogonality: $\langle Ax_0, Aw\rangle = \langle x_0, w\rangle$), i.e. $A(T_{x_0}S^m) = T_y S^m$ by Lemma 1.
> >
> > **Compute the orientation sign.** Choose a positively oriented basis $(e_1, \dots, e_m)$ of $T_{x_0}S^m$; by the outward-normal-first convention this means $(x_0, e_1, \dots, e_m)$ is a positively oriented basis of $\mathbb{R}^{m+1}$. Apply $A$: the image basis of $T_y S^m$ is $(A e_1, \dots, A e_m)$, and we ask its orientation sign. By the same convention, $(A e_1, \dots, A e_m)$ is positively oriented in $T_y S^m$ if and only if $(y, A e_1, \dots, A e_m) = (A x_0, A e_1, \dots, A e_m)$ is positively oriented in $\mathbb{R}^{m+1}$ (using $y = A x_0$). But
> > $$(A x_0, A e_1, \dots, A e_m) = A \cdot (x_0, e_1, \dots, e_m) \qquad \text{(} A \text{ applied columnwise to the ordered basis)},$$
> > so the two ordered bases of $\mathbb{R}^{m+1}$ differ by the linear map $A$, and their orientations therefore differ by $\operatorname{sign}\det A = \det A$ (as $\det A = \pm 1$ for $A \in O(m+1)$). Since $(x_0, e_1, \dots, e_m)$ is positive, $(A x_0, A e_1, \dots, A e_m)$ has orientation sign $\det A$; hence $(A e_1, \dots, A e_m)$ has orientation sign $\det A$ in $T_y S^m$. Therefore the differential $d(A|_{S^m})_{x_0}$ carries the positive basis $(e_1, \dots, e_m)$ to the $\det A$-oriented basis $(A e_1, \dots, A e_m)$, which means
> > $$\operatorname{sign}\det\!\big(d(A|_{S^m})_{x_0}\big) = \det A.$$
> >
> > **Conclude.** Combining the last two displays, $\deg(A|_{S^m}) = \det A$. For $A = I$ this gives $\deg \operatorname{id}_{S^m} = \det I = 1$. For $A = -I$, which is orthogonal with $\det(-I) = (-1)^{m+1}$, it gives $\deg a = (-1)^{m+1}$. (Equivalently, $-I$ is the product of the $m+1$ reflections in the coordinate hyperplanes, each of determinant $-1$ hence degree $-1$ by the first part of this lemma; by multiplicativity of the degree — clause (e) of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]], $\deg(g \circ f) = \deg g \cdot \deg f$ — the composite has degree $(-1)^{m+1}$, so $\deg a = (-1)^{m+1}$.) $\blacksquare$

> [!note]- Lemma 3: A unit tangent field produces a smooth homotopy from the identity to the antipodal map
> **Statement:** Let $w$ be a smooth unit tangent field on $S^m$ (so $\lvert w(x)\rvert = 1$ and $\langle x, w(x)\rangle = 0$ for all $x$). Then $F : S^m \times [0,1] \to S^m$, $F(x, t) = \cos(\pi t)\,x + \sin(\pi t)\,w(x)$, is a well-defined smooth homotopy with $F(\cdot, 0) = \operatorname{id}_{S^m}$ and $F(\cdot, 1) = a$, the antipodal map.
>
> **Hint:** The orthogonality of $x$ and $w(x)$ makes $\lvert F(x,t)\rvert^2$ collapse to $\cos^2 + \sin^2 = 1$.
>
> **Why needed:** It is the bridge turning the hypothetical nowhere-vanishing field into the statement $\operatorname{id} \simeq a$, which the degree computation of Lemma 2 then refutes.
>
> > [!note]- Full proof
> > **$F$ lands in $S^m$.** For $(x, t) \in S^m \times [0,1]$,
> > $$\lvert F(x,t)\rvert^2 = \big\langle \cos(\pi t)x + \sin(\pi t)w(x),\; \cos(\pi t)x + \sin(\pi t)w(x)\big\rangle$$
> > $$= \cos^2(\pi t)\,\lvert x\rvert^2 + 2\cos(\pi t)\sin(\pi t)\,\langle x, w(x)\rangle + \sin^2(\pi t)\,\lvert w(x)\rvert^2 \qquad \text{(bilinearity of } \langle\cdot,\cdot\rangle\text{)}$$
> > $$= \cos^2(\pi t)\cdot 1 + 2\cos(\pi t)\sin(\pi t)\cdot 0 + \sin^2(\pi t)\cdot 1 = 1 \qquad \text{(since } \lvert x\rvert = \lvert w(x)\rvert = 1 \text{ and } \langle x, w(x)\rangle = 0\text{)}.$$
> > So $F(x, t) \in S^m$ for every $(x, t)$; the cross term vanishes exactly because $w(x)$ is tangent, i.e. orthogonal to $x$ (Lemma 1).
> >
> > **$F$ is smooth.** The maps $(x, t) \mapsto \cos(\pi t)$, $(x, t) \mapsto \sin(\pi t)$, $x \mapsto x$, and $x \mapsto w(x)$ are smooth on $S^m \times [0,1]$, and $F$ is built from them by scalar multiplication and addition in $\mathbb{R}^{m+1}$; as its image lies in the embedded submanifold $S^m$, $F$ is smooth as a map into $S^m$.
> >
> > **Endpoints.** At $t = 0$: $F(x, 0) = \cos(0)x + \sin(0)w(x) = x$, so $F(\cdot, 0) = \operatorname{id}_{S^m}$. At $t = 1$: $F(x, 1) = \cos(\pi)x + \sin(\pi)w(x) = -x = a(x)$, so $F(\cdot, 1) = a$. Hence $F$ is a smooth homotopy from the identity to the antipodal map. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the theorem, then each corollary.
>
> **Goal.** Show that $S^{2n}$ admits no nowhere-vanishing tangent vector field. We argue by contradiction, using the Brouwer degree.
>
> **Step 0 — the degree machinery is available.** The sphere $S^{2n}$ is a closed, connected, oriented $2n$-manifold (oriented by the outward-normal-first convention of the Notation section), so the [[Def - Brouwer Degree of a Map|Brouwer degree]] of any smooth self-map is defined and, by [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]], is an integer satisfying: (b) $\deg f = \sum_{x \in f^{-1}(y)}\operatorname{sign}\det d f_x$ for every regular value $y$; and (c) smoothly homotopic maps have equal degree. Both clauses are proved in full on that page.
>
> **Step 1 — assume a field and normalise it.** Suppose, for contradiction, that there is a smooth nowhere-vanishing tangent vector field $v$ on $S^{2n}$. By **Lemma 1**, $w := v/\lvert v\rvert$ is a smooth *unit* tangent field: $\lvert w(x)\rvert = 1$ and $\langle x, w(x)\rangle = 0$ for all $x \in S^{2n}$.
>
> **Step 2 — build the homotopy.** By **Lemma 3** applied to $w$, the map
> $$F : S^{2n} \times [0,1] \to S^{2n}, \qquad F(x, t) = \cos(\pi t)\,x + \sin(\pi t)\,w(x),$$
> is a smooth homotopy with $F(\cdot, 0) = \operatorname{id}_{S^{2n}}$ and $F(\cdot, 1) = a$, the antipodal map. Thus $\operatorname{id}_{S^{2n}}$ is smoothly homotopic to $a$.
>
> **Step 3 — the two degrees disagree.** By the homotopy invariance of degree (Step 0, clause (c)) and Step 2,
> $$\deg(\operatorname{id}_{S^{2n}}) = \deg(a).$$
> By **Lemma 2** (degree of an orthogonal map equals its determinant), applied with $m = 2n$,
> $$\deg(\operatorname{id}_{S^{2n}}) = \det(I) = 1, \qquad \deg(a) = \det(-I) = (-1)^{2n+1} = -1 \qquad \text{(since } 2n+1 \text{ is odd)}.$$
> Combining the last two displays gives $1 = -1$.
>
> **Step 4 — the contradiction.** The equality $1 = -1$ is false in $\mathbb{Z}$. This contradicts the assumption of Step 1 that a nowhere-vanishing tangent field exists. Therefore $S^{2n}$ admits no nowhere-vanishing tangent vector field; equivalently, every smooth tangent field on $S^{2n}$ has a zero. This proves the theorem. $\blacksquare$
>
> ---
>
> **Corollary 1 — the antipodal map is not homotopic to the identity.**
> The antipodal map $a$ of $S^{2n}$ has $\deg a = (-1)^{2n+1} = -1$ and $\deg \operatorname{id}_{S^{2n}} = 1$ (both by **Lemma 2**). If $a$ were smoothly homotopic to $\operatorname{id}_{S^{2n}}$, then by homotopy invariance of degree (Step 0, clause (c)) we would have $\deg a = \deg \operatorname{id}_{S^{2n}}$, i.e. $-1 = 1$, which is false. Hence $a \not\simeq \operatorname{id}_{S^{2n}}$. $\blacksquare$
>
> *(This corollary needs neither Lemma 1 nor Lemma 3; it is the pure degree statement extracted from Step 3. Conversely, the theorem is the assertion that this rigidity obstructs the homotopy $F$ of Step 2 from existing, which is what forbids the field.)*
>
> **Corollary 2 — $TS^{2n}$ is nontrivial and $\operatorname{Fr}(TS^{2n})$ has no section.**
> *Non-triviality of $TS^{2n}$.* Suppose $TS^{2n} \cong S^{2n} \times \mathbb{R}^{2n}$ were trivial, with a bundle isomorphism $\Phi : S^{2n} \times \mathbb{R}^{2n} \to TS^{2n}$ covering the identity of $S^{2n}$. Then $x \mapsto \Phi(x, e_1)$, with $e_1$ the first standard basis vector of $\mathbb{R}^{2n}$, is a smooth section of $TS^{2n}$, and it is nowhere-vanishing because $\Phi$ restricts to a linear isomorphism $\{x\} \times \mathbb{R}^{2n} \to T_x S^{2n}$ on each fibre, so $\Phi(x, e_1) \neq 0$ (as $e_1 \neq 0$). This is a nowhere-vanishing tangent field, contradicting the theorem. Hence $TS^{2n}$ is not trivial.
>
> *No global frame.* By [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality dictionary]] — restated: for a real vector bundle $E$ of rank $k$, the frame bundle $\operatorname{Fr}(E)$ (the principal $GL(k;\mathbb{R})$-bundle of ordered bases of the fibres) admits a global smooth section if and only if $E$ is trivial — the non-triviality of $TS^{2n}$ just proved gives that $\operatorname{Fr}(TS^{2n})$ has no global section. Directly: a global section of $\operatorname{Fr}(TS^{2n})$ is a smooth global frame $(e_1, \dots, e_{2n})$ of $TS^{2n}$, and its first component $x \mapsto e_1(x)$ is a nowhere-vanishing tangent field (a frame is pointwise linearly independent, so each $e_i(x) \neq 0$), again contradicting the theorem. $\blacksquare$
>
> **Corollary 3 — no positive-dimensional Lie group acts freely on $S^{2n}$.**
> Suppose a Lie group $G$ with $\dim G \geq 1$ acts smoothly and [[Def - Free, Transitive, Effective, and Proper Group Actions|freely]] on $S^{2n}$ on the left (the series convention for a group action on a manifold; the right case is identical after replacing every $g \cdot p$ below by $p \cdot g$ and the left-action axiom $(gh)\cdot p = g \cdot (h \cdot p)$ by $p \cdot (gh) = (p \cdot g)\cdot h$). Since $\dim G \geq 1$, the Lie algebra $\mathfrak{g} = T_e G$ is nonzero; fix $X \in \mathfrak{g}$ with $X \neq 0$. Consider the [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] $\bar X \in \Gamma(TS^{2n})$, which is smooth by that definition, given by $\bar X(p) = d_e \ell_p(X)$ where $\ell_p(g) = g \cdot p$.
>
> > **Claim.** $\bar X$ is nowhere-vanishing on $S^{2n}$.
>
> **Proof of Claim.** Fix $p \in S^{2n}$ and consider the smooth curve $\gamma_p : \mathbb{R} \to S^{2n}$, $\gamma_p(t) = \exp(tX) \cdot p$.
>
> *The curve is an integral curve of $\bar X$.* For any $t_0 \in \mathbb{R}$, using that $t \mapsto \exp(tX)$ is a one-parameter subgroup — $\exp((t_0 + s)X) = \exp(sX)\exp(t_0 X)$ — and the left-action axiom $(gh)\cdot p = g \cdot (h \cdot p)$,
> $$\gamma_p(t_0 + s) = \exp((t_0 + s)X) \cdot p = \exp(sX)\cdot\big(\exp(t_0 X)\cdot p\big) = \ell_{q}(\exp(sX)), \qquad q := \gamma_p(t_0).$$
> Differentiating at $s = 0$ and using $\tfrac{d}{ds}\big|_0 \exp(sX) = X$ (defining property of the exponential map) together with the chain rule,
> $$\gamma_p'(t_0) = \tfrac{d}{ds}\big|_0 \ell_q(\exp(sX)) = d_e \ell_q(X) = \bar X(q) = \bar X(\gamma_p(t_0)) \qquad \text{(definition of } \bar X\text{)}.$$
> Thus $\gamma_p$ solves $\gamma_p'(t) = \bar X(\gamma_p(t))$ with $\gamma_p(0) = p$; it is the integral curve of $\bar X$ through $p$.
>
> *A zero forces a fixed one-parameter subgroup.* Suppose, toward a contradiction with freeness, that $\bar X(p) = 0$ for some $p$. Then the constant curve $\eta(t) \equiv p$ also satisfies $\eta'(t) = 0 = \bar X(p) = \bar X(\eta(t))$ with $\eta(0) = p$. By the uniqueness of integral curves ([[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]]: through each point there is a unique maximal integral curve of a smooth vector field), $\gamma_p = \eta$, that is,
> $$\exp(tX) \cdot p = p \qquad \text{for all } t \in \mathbb{R}.$$
> Now $X \neq 0$ and $\exp$ is a local diffeomorphism at $0 \in \mathfrak{g}$ (its differential at $0$ is the identity of $\mathfrak{g}$, by [[Def - Exponential Map of a Lie Group|the exponential map]]), so for all sufficiently small $t \neq 0$ we have $\exp(tX) \neq e = \exp(0)$ because $tX \neq 0$. For such a $t$, $\exp(tX) \cdot p = p = e \cdot p$ exhibits a nonidentity element $\exp(tX)$ fixing $p$, contradicting freeness of the action (a free action has $g \cdot p = p \Rightarrow g = e$). Therefore no zero exists: $\bar X(p) \neq 0$ for all $p$, proving the Claim.
>
> **Conclude.** The Claim produces a nowhere-vanishing tangent vector field $\bar X$ on $S^{2n}$, contradicting the theorem. Hence no Lie group of positive dimension acts smoothly and freely on $S^{2n}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Vector fields on odd spheres, for contrast.** On $S^{2k-1} \subset \mathbb{C}^k$ define $w(z) = iz$ (multiplication by the imaginary unit in each complex coordinate). Verify that $w$ is a nowhere-vanishing unit tangent field: $\lvert iz\rvert = \lvert z\rvert = 1$ and the real inner product $\langle z, iz\rangle = \operatorname{Re}\sum \bar z_j (i z_j) = \operatorname{Re}(i\lvert z\rvert^2) = 0$. This is a good exercise because it shows the theorem is *sharp in the parity*: the identical construction fails only at the sign $\det(-I)$, and the reader sees exactly why odd spheres escape. The vector field $w$ is also the fundamental vector field of the free $U(1)$-action $z \mapsto e^{i\theta}z$, tying the exercise back to Corollary 3 and to the Hopf bundle.

**Continuous wind patterns on the earth.** Model the wind as a continuous tangent field on $S^2$; the theorem (in its continuous form, obtained by smoothing) guarantees a point of zero horizontal wind — a cyclone's eye. The exercise is to make the meteorological statement precise and to see that it is genuinely the hairy ball theorem, not a metaphor: the "at least one calm point" conclusion is exactly "every tangent field vanishes somewhere". It is non-obvious because the physical intuition ("wind can circulate everywhere") is the false odd-dimensional picture transplanted to the even-dimensional sphere.

**Fixed points of maps close to the antipodal map.** Show that any smooth self-map $f$ of $S^{2n}$ with no fixed point and no antipodal point (never $f(x) = x$ and never $f(x) = -x$) is impossible to combine — more precisely, a map with no fixed point is homotopic to the antipodal map, and a map with no antipodal point is homotopic to the identity, so a map with neither would force $\operatorname{id} \simeq a$, contradicting Corollary 1. The exercise applies the same homotopy-through-the-shorter-arc idea as Lemma 3 and is a clean use of degree; it is the standard route to the Brouwer fixed-point theorem's cousins on spheres.

---

# Bridges

- **[[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|Brouwer degree]]** — the engine. The whole theorem is the observation that the integer $\deg$ separates $\operatorname{id}$ from $a$ on an even sphere; Lemma 2's computation $\deg(A|_{S^m}) = \det A$ is the regular-value formula (clause (b)) specialised to a single-preimage diffeomorphism, and Step 3 is homotopy invariance (clause (c)). Every appearance of "degree" here is restated from that page.

- **[[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]]** — the general obstruction. Poincaré–Hopf says that for a vector field with isolated zeros on a closed manifold $M$, the sum of the indices equals the Euler characteristic $\chi(M)$; since $\chi(S^{2n}) = 2 \neq 0$, no zero-free field exists. That is the $\chi(M) = 0$ criterion Bär invokes (Remark 1.5.19). This page proves the special case $S^{2n}$ directly, by degree, without developing index theory; the surface version and its consequence for $S^2$ are on the linked page.

- **[[Ex - Hairy Ball Theorem from Poincare-Hopf|the S² case via Poincaré–Hopf]]** — the alternative route. The two-sphere case admits a short proof by exhibiting one field (say the gradient of the height function) with two zeros of index $+1$ each, summing to $\chi(S^2) = 2$, and invoking Poincaré–Hopf. Comparing the two proofs isolates what is field-independent (the Euler number) from what is field-specific (the explicit homotopy here).

- **[[Ex - The Tangent Bundle of S^2 is Nontrivial|non-parallelisability of S²]]** and **[[Ex - The Frame Bundle of TS^2 Admits No Global Section|the sectionless frame bundle]]** — the immediate applications recorded in the source (Haydys X2.1.2, and the last clause of A-X2.2.1). They are Corollary 2 for $n = 1$, and they open the chapter's larger theme that a bundle's sections are constrained by topology.

- **[[Def - Fundamental Vector Field of a Group Action|fundamental vector fields]] and [[Thm - Fundamental Theorem on Flows|the flow theorem]]** — the bridge into Lie theory used in Corollary 3. A free action's infinitesimal generators are nowhere-vanishing because a zero would be a fixed point of the generated one-parameter subgroup; this is the differential-geometric shadow of "free means fixed-point-free", and it is why $S^2$ is not a Lie group and admits no free circle action, in contrast to $S^1 = U(1)$ and $S^3 = SU(2)$.

---

# Unlocked by This

> [!tip] Non-triviality of principal bundles by an invariant *(from Gauge Theory III–VI)*
> The pattern "a section would force an integer to take two incompatible values" recurs throughout the classification of bundles: the [[Def - The Hopf Bundle|Hopf bundle]] is nontrivial because the winding number of its transition function $z/\lvert z\rvert$ is $1 \neq 0$, and $SU(2)$-bundles over a $4$-manifold are classified by the second Chern number. The hairy ball theorem is the rank-$m$-over-$S^m$ prototype of these obstructions.

> [!tip] The Euler class *(from Chern–Weil theory, Gauge Theory VI)*
> The obstruction to a nowhere-vanishing section of an oriented rank-$m$ real bundle over an $m$-manifold is a single cohomology class, the Euler class, whose integral is the Euler number. For $TS^{2n}$ this number is $\chi(S^{2n}) = 2$, and the hairy ball theorem is its non-vanishing made elementary. See **Euler class via the Pfaffian**.
