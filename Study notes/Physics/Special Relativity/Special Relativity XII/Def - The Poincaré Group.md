---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Group"
  - "Def - Minkowski Space and the Metric"
  - "Def - The Lorentz Transformation"
  - "Def - Inertial Observer"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. Minkowski spacetime $\mathscr{E}$ is the four-dimensional real affine space with displacement vector space $E$; its points are events, written $M, N, O$. A [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$ is a linear map of $E$ preserving the metric, with matrix $\Lambda^\alpha{}_\beta$ in an orthonormal basis; the [[Def - The Lorentz Group|Lorentz group]] is $\mathrm{O}(1,3)$ and its restricted (proper orthochronous) subgroup is $\mathrm{SO}^+(1,3)$. We write $\overrightarrow{MN}$ for the displacement from $M$ to $N$. A Poincaré transformation is written $f = (\boldsymbol{v}, \Lambda)$ with translation vector $\boldsymbol{v} \in E$ and Lorentz part $\Lambda$. The symbol $\rtimes$ denotes semidirect product. Gourgoulhon writes the group $\mathrm{IO}(3,1)$ (opposite signature) and the restricted version $\mathrm{ISO}_o(3,1)$. Full registry on [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

---

# Axiom Motivation

The Lorentz group $\mathrm{O}(1,3)$ relates the *directions* of spacetime: it tells you how two inertial observers' axes are rotated and boosted relative to one another. But it has a built-in blind spot — it acts on the displacement vector space $E$, fixing the origin. Two inertial observers do not in general share an origin: their worldlines cross spacetime at different events, and their coordinate systems are centred on different points. The relation between their coordinates is therefore not just $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta$ but $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$, with a constant shift $x_0'$ accounting for the offset of origins. The desideratum is to enlarge the Lorentz group to include these shifts — to find the full symmetry group of Minkowski space *as an affine space*, the group of all transformations that preserve the interval between every pair of events. That group is the Poincaré group, and the design question is what structure it must have.

The first decision is what objects the group consists of. A transformation preserving all intervals must preserve the flat metric, and the metric-preserving maps of an affine space are exactly the **affine maps** whose linear part is an isometry — this is a standard fact: an isometry of a flat metric is determined by where it sends one point and by its (metric-preserving) linear part. So each Poincaré transformation $f$ has the form "apply a Lorentz transformation $\Lambda$ to displacements, then translate", and is captured by the pair $(\boldsymbol{v}, \Lambda)$: the translation vector $\boldsymbol{v} = \overrightarrow{Of(O)}$ (the image of a chosen origin) and the Lorentz part $\Lambda$. Why both pieces? Drop the translation and you are back to the Lorentz group, blind to origin offsets — too small to relate two inertial observers in general position. Drop the Lorentz part and you have only translations, which cannot rotate or boost — too small to relate observers in relative motion. Both are needed, and the count of parameters is forced: four for the translation, six for the Lorentz part, ten in all.

The second and deeper decision is the *composition law*, and this is where the definition earns its subtlety. One is strongly tempted to compose the pairs componentwise — translations add, Lorentz parts multiply — giving $(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) \overset{?}{=} (\boldsymbol{v}_1 + \boldsymbol{v}_2, \Lambda_1\Lambda_2)$, which would make the group the direct product $\mathbb{R}^4 \times \mathrm{O}(1,3)$. This is *wrong*, and seeing why is the whole motivation. Apply $f_2 = (\boldsymbol{v}_2, \Lambda_2)$ first: it translates an event by $\boldsymbol{v}_2$ (after the Lorentz part). Now apply $f_1 = (\boldsymbol{v}_1, \Lambda_1)$: its Lorentz part $\Lambda_1$ acts on *everything that came before*, including the translation $\boldsymbol{v}_2$ that $f_2$ produced. So the translation $\boldsymbol{v}_2$ gets *rotated by* $\Lambda_1$ before $\boldsymbol{v}_1$ is added. The correct composition is
$$(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2,\; \Lambda_1\Lambda_2),$$
with the lone factor $\Lambda_1$ in front of $\boldsymbol{v}_2$. That factor is not a blemish to be removed; it is the entire structure of the group. It says the Lorentz group *acts* on the translation group, and a product with such an action is by definition a **semidirect product**, written $\rtimes$. The physical necessity of the twist is that boosting-then-translating must differ from translating-then-boosting — a boost changes what "translate by $\boldsymbol{v}$" means, because it changes the axes $\boldsymbol{v}$ is measured against — and the only composition law that records this is the semidirect one.

What would go wrong with the direct-product law? It would make translations and Lorentz transformations commute, which is false: conjugating a translation by a boost yields a *different* translation (the boosted one), not the same one. The direct-product structure would also make the Lorentz subgroup normal, which it is not. The semidirect law, by contrast, makes the *translations* normal — conjugating a translation by any Poincaré element gives the Lorentz-rotated translation, still a translation — and this normality is the structural fact from which everything in §12.2 flows, including the non-simplicity of the group. So the single design decision, forced by the geometry of "Lorentz acts on translations", is to compose with the twist $\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2$. One more requirement pins down the choice of which factor's Lorentz part acts: it must be $\Lambda_1$ (the *outer*, later-applied transformation) acting on $\boldsymbol{v}_2$ (the *inner*, earlier translation), because the later transformation sees and re-expresses everything the earlier one did. Reversing this — $\boldsymbol{v}_2 + \Lambda_2\boldsymbol{v}_1$ — would correspond to composing in the opposite order and gives the opposite-handed semidirect product; the convention here matches "apply right factor first".

---

# The Definition

The **Poincaré group** $\mathrm{ISO}(1,3)$ (also $\mathrm{IO}(1,3)$, the *inhomogeneous Lorentz group*) is the group of all affine transformations $f : \mathscr{E} \to \mathscr{E}$ of Minkowski spacetime whose linear part is a [[Def - The Lorentz Group|Lorentz transformation]]:
$$
\forall (M, N) \in \mathscr{E}^2, \qquad \overrightarrow{f(M)\,f(N)} = \Lambda\big(\overrightarrow{MN}\big)
\quad\text{for some } \Lambda \in \mathrm{O}(1,3).
$$
The Lorentz part $\Lambda$ is uniquely determined by $f$. Fixing an origin $O \in \mathscr{E}$, every Poincaré transformation acts as
$$
\overrightarrow{O\,f(M)} = \Lambda\big(\overrightarrow{OM}\big) + \boldsymbol{v},
\qquad \boldsymbol{v} = \overrightarrow{O\,f(O)},
$$
and so decomposes uniquely as a **Lorentz transformation pointed at $O$** (the map $\Lambda_O$ fixing $O$ with $\overrightarrow{O\Lambda_O(M)} = \Lambda(\overrightarrow{OM})$) followed by a **translation** $T$ of vector $\boldsymbol{v}$:
$$
f = T \circ \Lambda_O, \qquad \text{written } f = (\boldsymbol{v}, \Lambda).
$$

The **group law** is
$$
(\boldsymbol{v}_1, \Lambda_1)\,(\boldsymbol{v}_2, \Lambda_2) = \big(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2,\; \Lambda_1\Lambda_2\big),
$$
the identity is $(\boldsymbol{0}, \mathrm{Id})$, and the inverse is
$$
(\boldsymbol{v}, \Lambda)^{-1} = \big(-\Lambda^{-1}\boldsymbol{v},\; \Lambda^{-1}\big).
$$
This law exhibits the Poincaré group as the **semidirect product** of the translation group $(\mathbb{R}^4, +)$ by the Lorentz group:
$$
\mathrm{ISO}(1,3) \;\simeq\; \mathbb{R}^4 \rtimes \mathrm{O}(1,3),
$$
in which the translations $(\boldsymbol{v}, \mathrm{Id})$ form a **normal abelian subgroup** isomorphic to $(\mathbb{R}^4, +)$, and the Lorentz transformations $(\boldsymbol{0}, \Lambda)$ form a subgroup isomorphic to $\mathrm{O}(1,3)$ that acts on the translations by $\boldsymbol{v} \mapsto \Lambda\boldsymbol{v}$. The group is ten-dimensional. The **restricted Poincaré group** $\mathrm{ISO}^+(1,3) \simeq \mathbb{R}^4 \rtimes \mathrm{SO}^+(1,3)$, whose Lorentz part is proper orthochronous, is the subgroup that governs changes of inertial observer.

A **passive** Poincaré transformation is the associated change of inertial coordinates $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$ relating one event's coordinates in two inertial frames; an **active** Poincaré transformation is the map $f$ itself, sending one event to another within a single frame. The two have identical algebraic form and opposite meaning (see [[Ex - Active versus passive Poincaré transformations]]).

---

# Categorical / Structural Definition

Structurally, the Poincaré group is the **isometry group** $\mathrm{Isom}(\mathscr{E}, \eta)$ of Minkowski space as a flat pseudo-Riemannian (here, Lorentzian) affine space: the group of all bijections of $\mathscr{E}$ preserving the interval between every pair of events. By the general theory of isometries of flat metrics, every such map is affine, so this isometry group is precisely the affine extension of the linear isometry group, which is the Lorentz group. This places the Poincaré group in a uniform hierarchy of "inhomogeneous orthogonal groups": the rigid motions of Euclidean $n$-space form $\mathrm{ISO}(n) = \mathbb{R}^n \rtimes \mathrm{O}(n)$, and the rigid motions of the Minkowski signature-$(1,3)$ space form $\mathrm{ISO}(1,3) = \mathbb{R}^4 \rtimes \mathrm{O}(1,3)$ by the identical construction, only the signature of the preserved form changing.

The semidirect-product structure has a clean categorical description. Given a [[Def - Group|group]] $H$ acting on an abelian group $N$ by a homomorphism $\varphi : H \to \mathrm{Aut}(N)$, the **semidirect product** $N \rtimes_\varphi H$ is the set $N \times H$ with multiplication $(n_1, h_1)(n_2, h_2) = (n_1 + \varphi(h_1)(n_2),\, h_1 h_2)$. It is characterised by a *split short exact sequence*
$$
1 \longrightarrow N \longrightarrow N \rtimes_\varphi H \longrightarrow H \longrightarrow 1,
$$
where the first map embeds $N$ as the normal subgroup $\{(n, e)\}$, the second projects onto $H$, and the sequence *splits* because $H$ embeds back as the subgroup $\{(e, h)\}$, a section of the projection. The semidirect product is exactly a split extension of $H$ by $N$ with the conjugation action $\varphi$; the direct product is the special case $\varphi = \mathrm{trivial}$, where the extension is split *and central*. For the Poincaré group, $N = (\mathbb{R}^4, +)$, $H = \mathrm{O}(1,3)$, and $\varphi$ is the tautological action of Lorentz matrices on four-vectors — the action that is "non-trivial enough" to force the semidirect, rather than direct, structure. The non-triviality of $\varphi$ is precisely the statement that boosts do not commute with translations, and it is what makes the translations a *proper* normal subgroup, hence the Poincaré group **non-simple** (unlike the simple restricted Lorentz group $\mathrm{SO}^+(1,3)$).

As a [[Def - Lie Group|Lie group]] the Poincaré group is the automorphism object of the Minkowski-space structure in the category of flat Lorentzian affine spaces with isometric morphisms; its identity component is $\mathrm{ISO}^+(1,3)$, and its Lie algebra is the semidirect-sum $\mathfrak{iso}(1,3) = \mathbb{R}^4 \rtimes \mathfrak{so}(1,3)$ (see [[Thm - The Poincaré Group as a Lie Group]]).

---

# Relate to Other Fields / Compression

The Poincaré group is the relativistic analogue of two classical groups, and locating it between them is the fastest way to understand it. It is the spacetime analogue of the **Euclidean group** $\mathrm{ISO}(3) = \mathbb{R}^3 \rtimes \mathrm{O}(3)$ of rigid motions of ordinary three-dimensional space: rotations and reflections (the $\mathrm{O}(3)$ part) together with translations (the $\mathbb{R}^3$ part), composed by exactly the same semidirect law. Replace Euclidean three-space by Minkowski four-space and orthogonal rotations by Lorentz transformations and you have the Poincaré group. It is also the relativistic completion of the **Galilean group** of Newtonian mechanics; the Galilean group is the $c \to \infty$ contraction of the Poincaré group, in which the boost–translation bracket $[K_i, P_j] = \delta_{ij}P_0$ is suppressed and time becomes absolute.

**True name:** the Poincaré group is *the group of rigid motions of spacetime* — every way of sliding and rotating the whole of Minkowski space while keeping all intervals between events fixed. This isometry-group characterisation is the operational one: it tells you immediately that the group is affine (rigid motions of a flat space are affine), that it splits into a translation and a rotation part, that the translations are normal (sliding the whole space commutes with itself and is preserved under any rigid motion), and that the invariants of the group are the interval-built quantities. When you need to decide whether some transformation belongs to the Poincaré group, ask only: does it preserve the interval between every pair of events? If so it is a rigid motion of spacetime, hence Poincaré.

The compression that matters most for what follows is that the Poincaré group is the *full* symmetry group of special relativity — the group with respect to which every physical law must be invariant. Lorentz invariance (invariance under $\mathrm{O}(1,3)$) plus translation invariance (invariance under $\mathbb{R}^4$) together *are* Poincaré invariance, and a relativistic theory is exactly one whose Lagrangian is a Poincaré scalar. By Noether's theorem the ten generators correspond to ten conserved quantities: the four translations give energy and momentum, the three rotations give angular momentum, and the three boosts give the centre-of-energy theorem. The Poincaré group is thus the source of every spacetime conservation law of relativistic physics.

---

# Examples / Corollaries

**Is an instance — a pure translation.** The map $f(M) = M + \boldsymbol{v}$, written $(\boldsymbol{v}, \mathrm{Id})$, shifts every event by the fixed vector $\boldsymbol{v}$ and leaves all directions unchanged. It is a Poincaré transformation with Lorentz part the identity. Two translations compose by ordinary addition, $(\boldsymbol{v}_1, \mathrm{Id})(\boldsymbol{v}_2, \mathrm{Id}) = (\boldsymbol{v}_1 + \boldsymbol{v}_2, \mathrm{Id})$ (the semidirect twist is trivial when $\Lambda_1 = \mathrm{Id}$), so the translations form an abelian subgroup isomorphic to $(\mathbb{R}^4, +)$.

**Is an instance — a Lorentz transformation pointed at an event.** The map $\Lambda_O$ fixing a chosen event $O$ and acting as $\overrightarrow{O\Lambda_O(M)} = \Lambda(\overrightarrow{OM})$, written $(\boldsymbol{0}, \Lambda)$, is a Poincaré transformation that boosts or rotates spacetime about $O$. The set of all Lorentz transformations pointed at a *fixed* $O$ is a subgroup isomorphic to the [[Def - The Lorentz Group|Lorentz group]] $\mathrm{O}(1,3)$. Changing the base point $O$ conjugates this subgroup by a translation, which is why it is *not* normal.

**Is an instance — the boost relating two inertial observers.** The change of inertial coordinates $ct' = \gamma(ct - vx)$, $x' = \gamma(x - vt)$, $y' = y$, $z' = z$ (Gourgoulhon's eq. 8.14) is the passive Poincaré transformation with $\Lambda$ a boost and $x_0' = 0$ (origins coinciding at $t = t' = 0$). With a nonzero $x_0'$ it accounts for observers whose origins do not coincide.

**Is NOT an instance — a dilation.** The map $f(M) = O + 2\,\overrightarrow{OM}$, which doubles every displacement from $O$, is affine but its linear part $2\,\mathrm{Id}$ is not a Lorentz transformation (it does not preserve the metric: $\eta(2X, 2X) = 4\,\eta(X,X) \neq \eta(X,X)$). It is a *conformal* transformation, not a Poincaré one. The interval between events is scaled, not preserved, so $f$ is excluded. This non-example marks the boundary: enlarging the Poincaré group by dilations and special conformal transformations gives the conformal group, the symmetry of massless theories, but that is a strictly larger group.

**Is NOT an instance — a generic diffeomorphism.** A smooth bijection of $\mathscr{E}$ that is not affine — say one that curves straight lines — is not a Poincaré transformation, because Poincaré transformations are affine. Such maps appear in general relativity as the diffeomorphism gauge group, but in flat-spacetime special relativity only the affine, interval-preserving maps are symmetries.

**Corollary — the inverse formula.** From the group law, $(\boldsymbol{v}, \Lambda)(\boldsymbol{w}, \Lambda^{-1}) = (\boldsymbol{v} + \Lambda\boldsymbol{w}, \mathrm{Id})$, which is the identity exactly when $\boldsymbol{w} = -\Lambda^{-1}\boldsymbol{v}$; hence $(\boldsymbol{v}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})$. Note the inverse translation is *not* $-\boldsymbol{v}$ but $-\Lambda^{-1}\boldsymbol{v}$ — the semidirect twist again.

**Corollary — conjugating a translation gives a translation.** $(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id})(\boldsymbol{w}, \Lambda)^{-1} = (\Lambda\boldsymbol{v}, \mathrm{Id})$, a translation by the Lorentz-rotated vector. This is the calculation that proves the translations normal and is worked in [[Ex - Translations form a normal abelian subgroup]].

**Calibration check.** If you have understood the definition you should be able to (i) compute the product $(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2)$ and explain why the factor $\Lambda_1$ appears in front of $\boldsymbol{v}_2$; (ii) verify $(\boldsymbol{v}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})$ by multiplying it out; and (iii) decide whether a dilation or a generic diffeomorphism is a Poincaré transformation, and answer "no, because the linear part is not a Lorentz transformation / the map is not affine".

---

# Unlocked by This

> [!tip] The Poincaré Group as a Lie Group *(from §12.2)*
> The Poincaré group is a ten-dimensional Lie group, and its Lie algebra $\mathfrak{iso}(1,3)$ — with generators $P_\alpha, K_i, J_i$ and the structure constants of the chapter — is the kinematic algebra of relativistic physics. See [[Thm - The Poincaré Group as a Lie Group]].

> [!tip] The Casimir Invariants and the Wigner Classification *(from §12.3)*
> The Poincaré group has exactly two [[Def - Casimir Invariants of the Poincaré Group|Casimir invariants]], $P^2$ and $W^2$, whose values are the mass and spin; Wigner's classification of the irreducible unitary representations by these two labels is the definition of what an elementary particle is.

> [!tip] Spacetime Conservation Laws via Noether *(from the Principle of Least Action)*
> Because the laws of physics are invariant under the Poincaré group, **Noether's theorem** assigns a conserved quantity to each of the ten generators: energy and momentum to the four translations, angular momentum to the three rotations, and the centre-of-energy theorem to the three boosts. The Poincaré group is thus the origin of every spacetime conservation law; see the principle of least action and [[Def - Angular Momentum Four-Tensor]].

> [!tip] Local Poincaré Symmetry and Gauge Gravity *(from General Relativity)*
> In general relativity the *global* Poincaré symmetry of flat spacetime is replaced by a *local* one: a separate copy of the Poincaré (or Lorentz) group acts in the tangent space at each event, and gauging this local symmetry — making the group element a function of position — is one route to the gravitational field, the Poincaré gauge theory of gravity. The translations gauge to the vierbein and the Lorentz part to the spin connection. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
