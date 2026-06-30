---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Thomas Rotation"
  - "Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation"
  - "Thm - Polar Decomposition of the Lorentz Group"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, in an orthonormal frame $(e_0, e_1, e_2, e_3)$, with rest space $E = e_0^\perp$ of the observer $e_0$. The relativistic velocity sum is written $\mathbf{V}_1 \oplus \mathbf{V}_2$ (apply $\mathbf{V}_1$ first, then $\mathbf{V}_2$, all relative to $e_0$).

1. **Boosts are not closed under composition.** Let $\Lambda_1$ be a boost along $e_1$ and $\Lambda_2$ a boost along $e_2$ (non-coplanar planes). Prove that the matrix of $\Lambda_2\circ\Lambda_1$ in the frame $(e_0, e_1, e_2, e_3)$ is *not symmetric* (when an index is lowered with $\eta$), and conclude that $\Lambda_2\circ\Lambda_1$ is not a boost. Hence the set of all boosts is not a subgroup of $SO^+(1,3)$.
2. **Identify the residual rotation.** By the polar decomposition, $\Lambda_2\circ\Lambda_1 = S\circ R$ with $S$ a boost (velocity $\mathbf{V}_1 \oplus \mathbf{V}_2$) and $R \ne \mathrm{Id}$ the **Wigner rotation** (the Thomas rotation $R[\mathbf{V}_1, \mathbf{V}_2]$). Show $R$ acts in $\mathrm{Span}(\mathbf{V}_1, \mathbf{V}_2)$.
3. **Velocity addition is not commutative — by exactly the Thomas angle.** Prove the gyrocommutativity identity
$$
\mathbf{V}_1 \oplus \mathbf{V}_2 = R[\mathbf{V}_1, \mathbf{V}_2]\,(\mathbf{V}_2 \oplus \mathbf{V}_1),
$$
so the two orders of addition have equal magnitude but differ in direction by the Thomas rotation. (Use the polar decompositions of $\Lambda_2\Lambda_1$ and $\Lambda_1\Lambda_2$ and the fact that they are conjugate.)
4. **Why no subgroup can exist.** Explain, using the simplicity of $SO^+(1,3)$ (no proper normal subgroup other than $\{\mathrm{Id}\}$), why the boosts *cannot* be assembled into any subgroup that the rotations normalise — so the Thomas rotation is not an avoidable nuisance but a structural necessity.

**Recall:**

The exercise gathers the structural facts that boosts fail to close, that the failure is the Wigner rotation, and that velocity addition fails to commute by exactly that rotation.

![[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation#Statement]]

![[Def - Thomas Rotation#The Definition]]

A boost in a semi-adapted basis has a symmetric matrix ($\Lambda_{\alpha\beta} = \Lambda_{\beta\alpha}$ with indices lowered by $\eta$); a product of symmetric matrices is symmetric iff they commute. The [[Thm - Polar Decomposition of the Lorentz Group|polar decomposition]] writes any restricted $\Lambda = S\circ R$ uniquely. The relativistic velocity sum is the velocity of the composite boost ([[Thm - Relativistic Velocity Addition]], general form).

---

# Convergent Strategy

**Problem class.** A *subgroup-question* and *extract-the-Thomas-rotation* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: the closure check on "is a boost" *fails*, and the obstruction is identified as the Wigner/Thomas rotation, which is then tied to the non-commutativity of velocity addition and to the group's simplicity.

**Assumption pattern.** The signpost is "are the boosts a subgroup?" — and the most informative answer is *no*. The instrument is the symmetry criterion: a boost has a symmetric matrix, so a product of boosts is a boost only if the factors commute, and non-coplanar boosts do not commute. The residual asymmetry is the Wigner rotation, the same object as the Thomas rotation seen from the representation-theory side (Wigner's little-group construction).

**Theorem routing.** Part 1 uses the symmetry criterion ([[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|composition theorem]], general case). Part 2 instantiates [[Thm - Polar Decomposition of the Lorentz Group|the polar decomposition]] and [[Def - Thomas Rotation|the Thomas rotation]]. Part 3 is the gyrocommutativity identity, proved by comparing the polar decompositions of $\Lambda_2\Lambda_1$ and its conjugate $\Lambda_1\Lambda_2$. Part 4 invokes the simplicity of $SO^+(1,3)$, the chapter's deepest structural fact.

**Key decision point.** The hardest step is part 3: the cleanest proof is *not* to compute both velocity sums by brute force, but to observe that $\Lambda_1\Lambda_2 = P(\Lambda_2\Lambda_1)P^{-1}$ for the reflection $P$ swapping the two boost directions, so their boost factors have the same magnitude and their rotation factors are related — yielding the identity without grinding out the addition formula twice. The natural-but-laborious move is the brute-force double computation.

---

# Legal Operations Used

1. **The boost is symmetric, the rotation is orthogonal** (most-reusable property): the closure check is "is the product symmetric?" — and it fails for non-coplanar boosts.

2. **Compose boosts by velocity addition plus a Thomas rotation** (operation 8): the product is a boost (velocity $\mathbf{V}_1\oplus\mathbf{V}_2$) times the Wigner rotation.

3. **Polar-decompose relative to a chosen 4-velocity** (operation 7): extract $S$ and the residual rotation $R$.

4. **Invoke simplicity to forbid a factorisation** (insight/illegal-operation 1): $SO^+(1,3)$ being simple, no proper normal subgroup hosts the boosts.

---

# Hints

> [!note]- Hint 1
> A matrix $\Lambda$ is "symmetric" in the relevant sense iff $\eta\Lambda$ is a symmetric matrix, i.e. $\Lambda_{\alpha\beta} := \eta_{\alpha\gamma}\Lambda^\gamma{}_\beta$ equals $\Lambda_{\beta\alpha}$. Each boost $\Lambda_i$ separately passes this test. For the product, compute the $(0,2)$ and $(2,0)$ lowered entries of $\Lambda_2\Lambda_1$: you will find $\Lambda_{02} = \Gamma_1\Gamma_2 V_2$ while $\Lambda_{20} = -\Gamma_2 V_2$ (signs and the extra $\Gamma_1$ from the first boost). They are unequal, so the product is asymmetric. Algebraically: the product of two symmetric matrices $A, B$ satisfies $(AB)^{\mathsf T} = B^{\mathsf T}A^{\mathsf T} = BA$, which equals $AB$ only if $A, B$ commute; non-coplanar boosts do not commute.

> [!note]- Hint 2
> The polar decomposition $\Lambda_2\Lambda_1 = S\circ R$ has $S$ the boost carrying $e_0$ to $\Lambda_2\Lambda_1(e_0)$, whose spatial part is the relativistic sum $\mathbf{V}_1\oplus\mathbf{V}_2$ (times $\Gamma$). The rotation $R = S^{-1}\Lambda_2\Lambda_1$ fixes $e_0$ and also fixes the direction $\mathbf{V}_1\times\mathbf{V}_2$ (perpendicular to both velocities), so it rotates the plane $\mathrm{Span}(\mathbf{V}_1, \mathbf{V}_2)$ about that axis. This $R$ is the Wigner rotation; it is *the same operator* as the Thomas rotation, the name "Wigner" emphasising its role in the little-group / representation-theory construction.

> [!note]- Hint 3
> Let $P$ be the spatial reflection (an improper Lorentz transformation, but its conjugation action is fine) that swaps the roles of the two boost directions — concretely the reflection exchanging $e_1 \leftrightarrow e_2$, or more invariantly the reflection across the bisecting plane of $\mathbf{V}_1, \mathbf{V}_2$. Then $\Lambda_1\Lambda_2 = P(\Lambda_2\Lambda_1)P^{-1}$ relates the two orders. Their boost factors have the same Lorentz factor (so $|\mathbf{V}_1\oplus\mathbf{V}_2| = |\mathbf{V}_2\oplus\mathbf{V}_1|$), and chasing the polar decompositions through the conjugation shows the velocities differ by the rotation $R[\mathbf{V}_1,\mathbf{V}_2]$. Alternatively, prove it directly: both sums are the spatial part of a boost factor, and $S(\Lambda_2\Lambda_1) = R\cdot S(\Lambda_1\Lambda_2)\cdot R^{-1}$ as boosts forces the velocities to be $R$-related.

> [!note]- Hint 4
> Suppose the boosts generated a subgroup $B$ normalised by the rotations $K = SO(3)$. Then $BK$ would be a subgroup, and $B$ a normal subgroup of it; but more sharply, any nontrivial subgroup of $SO^+(1,3)$ that the whole group normalises must be normal in $SO^+(1,3)$, and $SO^+(1,3)$ is *simple* — its only normal subgroups are $\{\mathrm{Id}\}$ and the whole group. The boosts (a $3$-dimensional set) are neither, so they cannot form a normal subgroup, and in fact cannot close into any subgroup compatible with the rotation action. The Thomas rotation is the obstruction that simplicity *guarantees* must appear.

---

# Solution

We show boosts fail to close (Step 1), identify the residual Wigner rotation (Step 2), prove velocity addition fails to commute by exactly that rotation (Step 3), and explain why simplicity makes this unavoidable (Step 4).

**Step 1: Boosts are not closed.**

> [!note]- Derivation
> Take $\Lambda_1$ along $e_1$, $\Lambda_2$ along $e_2$, and form $\Lambda = \Lambda_2\Lambda_1$. The relevant entries: from Step 1 of the perpendicular-boost computation, $\Lambda(e_0) = \Gamma_1\Gamma_2 e_0 + \Gamma_1 V_1 e_1 + \Gamma_1\Gamma_2 V_2 e_2$, so the column gives $\Lambda^0{}_0 = \Gamma_1\Gamma_2$, $\Lambda^1{}_0 = \Gamma_1 V_1$, $\Lambda^2{}_0 = \Gamma_1\Gamma_2 V_2$. The $e_0$-row (action on the spatial basis) gives $\Lambda^0{}_1 = \Gamma_1 V_1$ (from $\Lambda_1$) and $\Lambda^0{}_2 = \Gamma_2 V_2$ (from $\Lambda_2$, which acts after but couples $e_2$ to $e_0$ with factor $\Gamma_2 V_2$). Lower indices with $\eta = \mathrm{diag}(1,-1,-1,-1)$:
> $$\Lambda_{20} = \eta_{22}\Lambda^2{}_0 = -\Gamma_1\Gamma_2 V_2, \qquad \Lambda_{02} = \eta_{00}\Lambda^0{}_2 = +\Gamma_2 V_2.$$
> These are unequal (for $\Gamma_1 > 1$), so $\eta\Lambda$ is **not** symmetric. The general principle: each boost has $\eta\Lambda_i$ symmetric, and $(\eta\Lambda_2\Lambda_1)^{\mathsf T} = \Lambda_1^{\mathsf T}\Lambda_2^{\mathsf T}\eta$; using $\Lambda_i^{\mathsf T}\eta = \eta\Lambda_i$ (the defining relation rearranged with $\eta^2 = I$ and $\Lambda_i$ symmetric) this equals $\eta\Lambda_1\Lambda_2$, which equals $\eta\Lambda_2\Lambda_1$ only if $\Lambda_1\Lambda_2 = \Lambda_2\Lambda_1$ — i.e. only if the boosts commute. Non-coplanar boosts do not commute, so the product is asymmetric, hence **not a boost**. The set of all boosts is therefore not closed under composition, and is not a subgroup of $SO^+(1,3)$. $\square$

**Step 2: The residual Wigner rotation.**

> [!note]- Derivation
> By [[Thm - Polar Decomposition of the Lorentz Group|the polar decomposition]] relative to $e_0$, $\Lambda_2\Lambda_1 = S\circ R$. The boost $S$ carries $e_0$ to $\Lambda_2\Lambda_1(e_0)$; writing $\Lambda_2\Lambda_1(e_0) = \Gamma(e_0 + \mathbf{W})$ with $\Gamma = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi)$, the velocity of $S$ is $\mathbf{W} = \mathbf{V}_1\oplus\mathbf{V}_2$, the relativistic sum ([[Thm - Relativistic Velocity Addition|velocity addition]], general form). The rotation $R = S^{-1}\Lambda_2\Lambda_1$ fixes $e_0$ (so lies in $SO(3)$ on the rest space) and fixes the common perpendicular $\mathbf{V}_1\times\mathbf{V}_2$ to both velocities — because both boosts and $S$ act trivially on that direction. Hence $R$ rotates the plane $\mathrm{Span}(\mathbf{V}_1, \mathbf{V}_2)$ about the axis $\mathbf{V}_1\times\mathbf{V}_2$, by the Thomas angle $\varphi_T$. This $R = R[\mathbf{V}_1,\mathbf{V}_2]$ is the **Wigner rotation**; it is identical to the Thomas rotation, the two names marking the same operator in the kinematic (Thomas) and representation-theoretic (Wigner little-group) literatures.

**Step 3: Velocity addition fails to commute by the Thomas rotation.**

> [!note]- Derivation
> Consider the two orders $\Lambda_2\Lambda_1$ and $\Lambda_1\Lambda_2$. Let $\sigma$ be the spatial reflection across the plane bisecting $\mathbf{V}_1$ and $\mathbf{V}_2$ (so $\sigma\mathbf{V}_1 = \mathbf{V}_2$, $\sigma\mathbf{V}_2 = \mathbf{V}_1$); it conjugates one boost into the other, $\sigma\Lambda_1\sigma^{-1} = \Lambda_2'$ and so on. More directly, polar-decompose both:
> $$\Lambda_2\Lambda_1 = S_{12}\circ R_{12}, \qquad \Lambda_1\Lambda_2 = S_{21}\circ R_{21},$$
> with $S_{12}$ the boost of velocity $\mathbf{V}_1\oplus\mathbf{V}_2$ and $S_{21}$ the boost of velocity $\mathbf{V}_2\oplus\mathbf{V}_1$. Taking the time–time component, both composites have the *same* Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi)$ (symmetric in $1\leftrightarrow 2$), so
> $$|\mathbf{V}_1\oplus\mathbf{V}_2| = |\mathbf{V}_2\oplus\mathbf{V}_1| = V \quad\text{(equal magnitudes).}$$
> Now relate the two products. From $\Lambda_2\Lambda_1 = S_{12}R_{12}$ and applying the rotation $R_{12}^{-1}$ on the left and using that conjugating a boost by a rotation rotates its velocity, one finds $S_{21} = R_{12}^{-1} S_{12} R_{12}$ — the two composite boosts are conjugate by the Thomas rotation. A boost $S_{21} = R^{-1}S_{12}R$ has velocity $R^{-1}(\mathbf{V}_1\oplus\mathbf{V}_2)$. Therefore
> $$\mathbf{V}_2\oplus\mathbf{V}_1 = R[\mathbf{V}_1,\mathbf{V}_2]^{-1}(\mathbf{V}_1\oplus\mathbf{V}_2) \;\Longleftrightarrow\; \mathbf{V}_1\oplus\mathbf{V}_2 = R[\mathbf{V}_1,\mathbf{V}_2]\,(\mathbf{V}_2\oplus\mathbf{V}_1).$$
> This is **gyrocommutativity**: the two orders of addition have equal magnitude but their directions differ by exactly the Thomas rotation $R[\mathbf{V}_1,\mathbf{V}_2]$. Velocity addition is non-commutative, and the Thomas rotation is the *precise* measure of the failure — not an inequality of magnitudes (those agree) but a rotation of directions. $\square$

**Step 4: Simplicity makes it unavoidable.**

> [!note]- Derivation
> Suppose, for contradiction, that the boosts could be organised into a subgroup $B \le SO^+(1,3)$ normalised by the rotations $K = SO(3)$ (which is the minimal compatibility one would want for a "boost part" of a clean factorisation $SO^+(1,3) = B\rtimes K$). Conjugating a boost along $\mathbf{n}$ by a rotation gives the boost along $H\mathbf{n}$, so $K$ acts transitively on the boost directions; if $B$ contained one nontrivial boost it would contain all of them (by $K$-conjugation), so $B = \{\text{all boosts}\}\cup\cdots$. For $B$ to be a subgroup it must be closed, but Step 1 shows the product of two non-coplanar boosts leaves $B$ (it is a four-screw). To repair this, $B$ would have to contain those four-screws too, and iterating, $B$ would grow to contain rotations — collapsing to all of $SO^+(1,3)$.
>
> The clean statement is the structural one: a subgroup normalised by all of $SO^+(1,3)$ is a **normal subgroup**, and $SO^+(1,3)$ is **simple** — its only normal subgroups are $\{\mathrm{Id}\}$ and itself. A putative boost-subgroup normalised by the rotations (hence, since rotations and boosts generate the whole group, normalised by everything) would have to be normal, so either trivial or everything. The boosts form a $3$-dimensional set, neither trivial nor the whole $6$-dimensional group, so **no such subgroup exists**. The Thomas rotation is therefore not an artefact of clumsy bookkeeping that a better choice of "boost" could remove; it is forced by the simplicity of the Lorentz group. The polar decomposition splits each *element* relative to a chosen observer, but no splitting of the *group* into boost and rotation factors can exist, and the leftover rotation when you compose two boosts is the visible shadow of that impossibility. $\blacksquare$

> [!note]- Complete formal solution
> For $\Lambda_2$ along $e_2$ and $\Lambda_1$ along $e_1$, the product has lowered entries $\Lambda_{02} = \Gamma_2 V_2 \ne -\Gamma_1\Gamma_2 V_2 = \Lambda_{20}$, so $\eta\Lambda_2\Lambda_1$ is not symmetric; since $(\eta\Lambda_2\Lambda_1)^{\mathsf T} = \eta\Lambda_1\Lambda_2 \ne \eta\Lambda_2\Lambda_1$ unless the boosts commute, and non-coplanar boosts do not commute, the product is not a boost — boosts are not closed, not a subgroup. Polar-decomposing $\Lambda_2\Lambda_1 = S\circ R$, the boost $S$ has velocity $\mathbf{V}_1\oplus\mathbf{V}_2$ and Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$, while $R = R[\mathbf{V}_1,\mathbf{V}_2]$ (the Wigner rotation) fixes $e_0$ and $\mathbf{V}_1\times\mathbf{V}_2$, rotating $\mathrm{Span}(\mathbf{V}_1,\mathbf{V}_2)$ by $\varphi_T$. The two orders share the Lorentz factor $\Gamma$ (symmetric in $1\leftrightarrow2$), so $|\mathbf{V}_1\oplus\mathbf{V}_2| = |\mathbf{V}_2\oplus\mathbf{V}_1|$; their boost factors are conjugate, $S_{21} = R^{-1}S_{12}R$, giving the gyrocommutativity identity $\mathbf{V}_1\oplus\mathbf{V}_2 = R[\mathbf{V}_1,\mathbf{V}_2](\mathbf{V}_2\oplus\mathbf{V}_1)$. Finally, a boost-subgroup normalised by the rotations would be normal in the simple group $SO^+(1,3)$, hence trivial or everything; the $3$-dimensional boost set is neither, so no such subgroup exists and the Thomas rotation is structurally forced. $\blacksquare$

---

# Key Takeaways

**The symmetry criterion turns "are boosts a subgroup?" into a one-line computation that answers no.** A boost has a symmetric matrix (index lowered with $\eta$); a product of symmetric matrices is symmetric only when they commute; non-coplanar boosts do not commute; therefore their product is asymmetric and not a boost. This is the entire argument, and it is the cleanest possible proof that the boosts fail to close. The reusable instrument is the equivalence "is a boost $\iff$ symmetric matrix," which converts a group-theoretic closure question into a matrix-symmetry check. The same criterion, run in reverse, shows that the *failure* of symmetry is exactly the rotation content extracted by polar decomposition — so the computation does not merely answer "no," it hands you the Wigner rotation as the asymmetric part.

**The Wigner rotation and the Thomas rotation are the same operator, and they measure non-commutativity of velocity addition exactly — as a rotation of direction, not a change of magnitude.** The residual rotation in the composition of two boosts has two names: "Thomas," from the kinematic precession it generates, and "Wigner," from its role in the little-group construction of relativistic particle states. They are one object, $R[\mathbf{V}_1,\mathbf{V}_2]$. The gyrocommutativity identity $\mathbf{V}_1\oplus\mathbf{V}_2 = R(\mathbf{V}_2\oplus\mathbf{V}_1)$ pins down the precise nature of the non-commutativity: the two orders of velocity addition yield velocities of *equal magnitude* (same composite Lorentz factor, symmetric in the two boosts) but *different direction*, related by the Thomas rotation. So velocity addition is non-commutative in a very specific way — a pure rotation of the result — and this is the foundational fact of the gyrogroup structure of velocity space. Whenever a composition law fails to commute by a rotation rather than by a magnitude, suspect a gyrogroup and a holonomy.

**Simplicity of the Lorentz group is the deep reason the Thomas rotation cannot be removed.** The most important conceptual takeaway is that the Thomas rotation is not a removable inconvenience but a structural necessity. $SO^+(1,3)$ is a simple group: it has no proper nontrivial normal subgroup. Any clean factorisation of the group into "boost part times rotation part" would exhibit the boosts as a normal subgroup, which simplicity forbids. So the boosts cannot form a subgroup, the composition of two boosts must leave a rotation, and that rotation is the Thomas rotation. This reframes a whole cluster of facts — boosts not closing, velocity addition not commuting, three boosts leaving a residual rotation, the gyrogroup defect, the precession measured in atomic spectra — as a single phenomenon: the simplicity of the Lorentz group forbids the boost/rotation splitting you instinctively want, and the Thomas rotation is what appears in its place. The trigger to internalise: the moment you are tempted to factor $SO^+(1,3)$ into smaller groups, recall it is simple and stop — the obstruction will be a Thomas-type rotation every time.
