---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Group"
  - "Def - Minkowski Space and the Metric"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so timelike vectors have $X\cdot X > 0$. A [[Def - The Lorentz Group|Lorentz transformation]] $\Lambda$ is a real $4\times 4$ matrix satisfying $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$; its components in a right-handed orthonormal basis $(e_0,e_1,e_2,e_3)$ (with $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$) are written $\Lambda^\alpha{}_\beta$, with $\alpha$ labelling rows and $\beta$ columns. The entry $\Lambda^0{}_0$ is the time–time component. Greek indices run $0$–$3$, Latin $i,j$ run $1$–$3$. Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

This is a compound page: it defines four interlocking notions — the **proper Lorentz group** $SO(1,3)$, the **orthochronous Lorentz group** $O^+(1,3)$, the **restricted Lorentz group** $SO^+(1,3)$, and the discrete-reflection **reduction** of $O(1,3)$ to its identity component — because they are introduced together as the connected-component structure of $O(1,3)$ and none is fully usable without the others.

---

# Axiom Motivation

[[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group|Special Relativity IV]] established that $O(1,3)$ is a single group, the isometries of the interval. But it is not a single *connected* group, and the physics lives in only one of its pieces. The motivation for carving $O(1,3)$ into subgroups is the demand to isolate the transformations a real physical process can produce — and that is exactly the component of the identity, because any process unfolding in time traces a continuous path through the group starting at $\mathrm{Id}$.

What invariants could distinguish the pieces? We need functions on $O(1,3)$ that are *locally constant* — constant on each connected component, jumping only between components. Two such functions are forced on us by the defining equation. Taking the determinant of $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ and using $\det\eta = -1 \ne 0$ gives $(\det\Lambda)^2 = 1$, so $\det\Lambda \in \{+1, -1\}$ — a function that cannot vary continuously, hence is constant on components. This is the **proper/improper** split, and it is the relativistic version of the orientation invariant that splits $O(n)$ into $SO(n)$ and its reflection coset. Setting $\mu = \nu = 0$ in the index form $\eta_{\alpha\beta}\Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu = \eta_{\mu\nu}$ gives $(\Lambda^0{}_0)^2 - \sum_i(\Lambda^i{}_0)^2 = 1$, hence $(\Lambda^0{}_0)^2 \ge 1$, so $\Lambda^0{}_0 \ge 1$ or $\Lambda^0{}_0 \le -1$ — the value can never pass through the forbidden interval $(-1, 1)$, so its sign is locally constant. This is the **orthochronous/antichronous** split, the genuinely new invariant of *Lorentzian* signature, recording whether the direction of time is preserved.

Why these two and no others? Because they exhaust the locally-constant functions: $O(1,3)$ has exactly four connected components, one for each sign pair, and a deeper analysis (the polar decomposition, or the surjectivity of the exponential map onto each component) shows each sign pair gives a *single* connected piece. So the two signs are a complete set of component invariants. Were we to drop the determinant invariant, we would lump together orientation-preserving and orientation-reversing transformations and lose the distinction between a rotation and a rotation-plus-mirror. Were we to drop the orthochronous invariant — the temptation of someone carrying over Euclidean intuition, where there is no "time" to reverse — we would lump together transformations that preserve the arrow of time with those that reverse it, and call a time-reversal a symmetry of a process that is manifestly irreversible.

The reduction to the identity component is then the natural endgame. We want, for each $\Lambda$, to peel off a discrete reflection and land in $SO^+(1,3)$, where the continuous theory applies. The reflections must be the simplest representatives of the non-identity sign pairs: **parity** $P = \mathrm{diag}(1,-1,-1,-1)$ (improper, orthochronous — flips space, keeps time's arrow), **time reversal** $T = \mathrm{diag}(-1,1,1,1)$ (improper, antichronous — reverses time, keeps orientation of space up to the reflection), and **total inversion** $I = -\mathrm{Id} = PT$ (proper, antichronous). These three plus the identity are forced to be a group — and the only four-element group containing three commuting involutions is the Klein four-group $\mathbb{Z}/2\times\mathbb{Z}/2$. If instead we had tried to use a single reflection, as in the Euclidean case, we could not reach all four components; the two independent reflections, in time and in space, are exactly what the two independent sign invariants demand.

---

# The Definition

Let $O(1,3)$ be the [[Def - The Lorentz Group|Lorentz group]], the group of real $4\times 4$ matrices $\Lambda$ with $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$.

The **proper Lorentz group** is
$$
SO(1,3) \;=\; \{\Lambda \in O(1,3) : \det\Lambda = +1\}.
$$
It is a subgroup of index two: the determinant $O(1,3) \to \{\pm 1\}$ is a homomorphism with kernel $SO(1,3)$.

The **orthochronous Lorentz group** is
$$
O^+(1,3) \;=\; \{\Lambda \in O(1,3) : \Lambda^0{}_0 \ge 1\}.
$$
Equivalently, $\Lambda$ is orthochronous iff it maps every future-pointing timelike vector to a future-pointing timelike vector. It is a subgroup of index two.

The **restricted Lorentz group** (proper orthochronous) is their intersection,
$$
SO^+(1,3) \;=\; \{\Lambda \in O(1,3) : \det\Lambda = +1 \ \text{and}\ \Lambda^0{}_0 \ge 1\},
$$
a subgroup of index four, and the connected component of the identity. Its elements are the **restricted Lorentz transformations**; they are exactly the transformations relating the local frames of two observers (right-handed, future-pointing).

The **discrete reflections** are the involutions
$$
I = -\mathrm{Id} = \mathrm{diag}(-1,-1,-1,-1), \qquad
P = \mathrm{diag}(1,-1,-1,-1), \qquad
T = \mathrm{diag}(-1,1,1,1),
$$
called total (spacetime) inversion, parity (space inversion), and time reversal. They satisfy $I = PT = TP$ and $P^2 = T^2 = I^2 = \mathrm{Id}$. Their component memberships are $I \in SO_{\text{anti}}(1,3)$ (proper, antichronous), $P \in O^-_{\text{improper}}(1,3)$ (improper, orthochronous), $T \in O^-_{\text{anti}}(1,3)$ (improper, antichronous).

The **reduction** statement is that $O(1,3)$ is the disjoint union of four connected components,
$$
O(1,3) \;=\; SO^+(1,3) \ \sqcup\ I\cdot SO^+(1,3) \ \sqcup\ P\cdot SO^+(1,3) \ \sqcup\ T\cdot SO^+(1,3),
$$
so every $\Lambda \in O(1,3)$ equals exactly one of $\Lambda_0$, $I\Lambda_0$, $P\Lambda_0$, $T\Lambda_0$ with $\Lambda_0 \in SO^+(1,3)$, according to its two signs. Among the four components, only $SO^+(1,3)$ is a group (the others lack the identity).

---

# Categorical / Structural Definition

The component structure is an exact sequence of groups. The two sign maps assemble into a single homomorphism
$$
\sigma : O(1,3) \longrightarrow \mathbb{Z}/2 \times \mathbb{Z}/2, \qquad
\Lambda \longmapsto \big(\tfrac{1-\det\Lambda}{2},\ \tfrac{1 - \mathrm{sgn}\,\Lambda^0{}_0}{2}\big),
$$
sending a proper orthochronous transformation to $(0,0)$, an improper one to $(1,0)$, an antichronous one to $(0,1)$, and an improper-antichronous one to $(1,1)$. This $\sigma$ is surjective (the reflections $I, P, T$ hit the three nonzero classes) with kernel exactly $SO^+(1,3)$, giving the short exact sequence
$$
1 \longrightarrow SO^+(1,3) \longrightarrow O(1,3) \xrightarrow{\ \sigma\ } \mathbb{Z}/2 \times \mathbb{Z}/2 \longrightarrow 1.
$$
The first isomorphism theorem then reads $O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2 \times \mathbb{Z}/2$, the group of connected components $\pi_0(O(1,3))$. The sequence is *split* — the subgroup $\{\mathrm{Id}, I, P, T\}$ is a section of $\sigma$ — so $O(1,3)$ is a semidirect product $SO^+(1,3) \rtimes (\mathbb{Z}/2\times\mathbb{Z}/2)$; the action is by conjugation, and because $SO^+(1,3)$ is normal ([[Thm - The Restricted Lorentz Group is a Normal Subgroup]]) the product is well-defined. This is the same structure as $O(n) = SO(n) \rtimes \mathbb{Z}/2$, with the single orientation reflection replaced by the Klein four-group of space-and-time reflections.

---

# Relate to Other Fields / Compression

The component structure is the Lorentzian analogue of the orthogonal-group story. For the Euclidean group $O(n)$, the determinant is the only locally-constant invariant, $O(n)/SO(n) \cong \mathbb{Z}/2$, and the single reflection is a mirror. Passing to indefinite signature $O(p,q)$ with $p, q \ge 1$ doubles the component count to four, because the timelike and spacelike parts can each be reflected independently: $O(p,q)$ has $\pi_0 \cong \mathbb{Z}/2 \times \mathbb{Z}/2$, with the two factors recording orientation of the timelike and spacelike subspaces separately. Special relativity is the case $(p,q) = (1,3)$, where "orientation of the timelike part" is the arrow of time and the new invariant is $\mathrm{sgn}\,\Lambda^0{}_0$.

**True name:** the restricted Lorentz group $SO^+(1,3)$ is "the identity component of $O(1,3)$" — the transformations reachable from the identity by a continuous path, equivalently by a physical process, equivalently (it turns out) by the exponential of the Lie algebra. The two defining inequalities $\det = +1$, $\Lambda^0{}_0 \ge 1$ are the operational test, but the conceptual content is connectedness to $\mathrm{Id}$, which is why only this piece carries the continuous symmetry the rest of relativity uses.

---

# Examples / Corollaries

**Is an instance — a boost.** A boost along $x$ with rapidity $\psi$, matrix $\mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{smallmatrix}, 1, 1\big)$, has $\det = \cosh^2\psi - \sinh^2\psi = 1$ and $\Lambda^0{}_0 = \cosh\psi \ge 1$, so it lies in $SO^+(1,3)$. Every [[Def - Boosts as Hyperbolic Rotations|boost]] is restricted.

**Is an instance — a spatial rotation.** A rotation $\mathrm{diag}(1, H)$ with $H \in SO(3)$ has $\det = \det H = 1$ and $\Lambda^0{}_0 = 1$, so it too is restricted. The restricted group contains the full rotation group $SO(3)$ as the subgroup fixing $e_0$.

**Is NOT an instance — parity.** $P = \mathrm{diag}(1,-1,-1,-1)$ has $\det P = -1$ (improper) and $\Lambda^0{}_0 = 1 \ge 1$ (orthochronous), so $P \in O^+(1,3)$ but $P \notin SO(1,3)$ and $P \notin SO^+(1,3)$. It preserves the arrow of time but reverses spatial orientation — a genuine symmetry of classical mechanics and electromagnetism, but *not* of the weak interaction, whose parity violation is a statement that $P$ is not a symmetry of nature.

**Is NOT an instance — the antichronous set.** The set of antichronous transformations ($\Lambda^0{}_0 \le -1$) is not a subgroup: it does not contain the identity ($\Lambda^0{}_0 = 1$ for $\mathrm{Id}$), and the product of two antichronous transformations is orthochronous (two sign flips of the time direction cancel). Likewise the improper set is not a subgroup. Only the four sign-pair classes that *include* $(+,+)$ — i.e. only $SO^+(1,3)$ among the four — form a group.

**Corollary — the index-four lattice of subgroups.** $SO^+(1,3)$ sits at the bottom of a lattice: it is contained in $SO(1,3)$ (add the antichronous-proper coset $I\cdot SO^+$), in $O^+(1,3)$ (add the improper-orthochronous coset $P\cdot SO^+$), and in the orthochronous-and-proper-preserving subgroup $SO^+ \cup I\cdot SO^+$... — three index-two subgroups of $O(1,3)$ contain it, corresponding to the three index-two subgroups of $\mathbb{Z}/2\times\mathbb{Z}/2$, and $SO^+$ is their common intersection.

**Calibration check.** The reader who has understood the definition should be able to: (i) given any of $I, P, T, \mathrm{Id}$, state its determinant and the sign of its time-component and hence its component; (ii) verify that the product of an antichronous and an orthochronous transformation is antichronous, and of two antichronous ones is orthochronous; (iii) explain why $SO(1,3)$ is connected but has *two* components when intersected with the data "orthochronous or not," and why the connected piece is $SO^+(1,3)$.

---

# Unlocked by This

> [!tip] The Lie Group $SO^+(1,3)$ and Its Topology *(from Special Relativity X)*
> The restricted Lorentz group is a six-dimensional Lie group, and as a manifold it is $\mathbb{R}^3 \times SO(3)$ (three boost parameters times the rotation group), which is connected but *not simply connected*: its fundamental group is $\mathbb{Z}/2$, inherited from $\pi_1(SO(3)) = \mathbb{Z}/2$. This non-trivial $\pi_1$ is what forces the existence of spinors and the double cover **SL(2,ℂ)**, and it is invisible at the level of the discrete component structure of this page — $\pi_0$ counts components, $\pi_1$ counts loops, and the deep topology is in $\pi_1$.

> [!tip] Parity and Time-Reversal Symmetry in Physics *(from quantum field theory)*
> The discrete reflections $P$ and $T$ are not merely group elements; they are candidate *symmetries of physical law*, and whether a given interaction respects them is a deep empirical question. Electromagnetism and gravity respect $P$, $T$, and $C$ (charge conjugation) separately; the weak interaction violates $P$ maximally and violates $CP$ slightly; and the **CPT theorem** of quantum field theory guarantees that the combined operation $CPT$ is always a symmetry of any local, Lorentz-invariant theory. The four-component structure of the Lorentz group is the classical skeleton on which these discrete symmetries hang.
