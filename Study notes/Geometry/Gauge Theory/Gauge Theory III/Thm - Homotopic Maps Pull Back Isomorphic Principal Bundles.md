---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Thm - Existence of Smooth Partitions of Unity"
  - "Def - Smooth Homotopy of Maps"
  - "Thm - Fundamental Theorem on Flows"
  - "Def - Associated Bundle"
  - "Thm - Vector Bundles are Associated to Their Frame Bundles"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group, and all manifolds are smooth, Hausdorff, and second countable; "smooth" means $C^\infty$. We write $I = [0,1]$ for the closed unit interval and $t$ for its coordinate, so that $M \times I$ is a smooth manifold with boundary $\partial(M \times I) = (M \times \{0\}) \cup (M \times \{1\})$, and $\partial_t = \frac{\partial}{\partial t}$ is the globally defined vector field on $M \times I$ tangent to every segment $\{m\} \times I$.

A **[[Def - Principal G-Bundle|principal $G$-bundle]]** $\pi \colon P \to N$ is a [[Def - Fibre Bundle|fibre bundle]] carrying a smooth **right** action $P \times G \to P$, $(p,g) \mapsto p \cdot g = R_g(p)$, that is free, preserves the fibres, is transitive on each fibre, and admits $G$-equivariant local trivialisations: for a suitable open cover $\{V_\alpha\}$ of $N$ there are diffeomorphisms $\Psi_\alpha \colon \pi^{-1}(V_\alpha) \to V_\alpha \times G$ with $\operatorname{pr}_{V_\alpha} \circ \Psi_\alpha = \pi$ and $\Psi_\alpha(p \cdot g) = \Psi_\alpha(p) \cdot g$, where $G$ acts on $V_\alpha \times G$ by $(x,h) \cdot g = (x, hg)$. We write $P_x = \pi^{-1}(x)$ for the fibre over $x \in N$.

An **isomorphism** of principal $G$-bundles $Q \to N$ and $Q' \to N$ over the same base is a $G$-equivariant diffeomorphism $F \colon Q \to Q'$ covering the identity of $N$, that is, with $\pi' \circ F = \pi$; we write $Q \cong Q'$. Following [[Def - Fibre Bundle|Bär's convention]], a principal bundle is **trivial** when it is isomorphic to the product bundle $N \times G \to N$; equivalently it admits a global equivariant trivialisation, and equivalently — by the theorem recalled below — it admits a global smooth section.

For a smooth map $\lambda \colon N' \to N$ and a principal $G$-bundle $P \to N$, the **[[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|pull-back]]** is
$$\lambda^* P = \{(x', p) \in N' \times P : \lambda(x') = \pi(p)\}, \qquad \operatorname{pr}_1 \colon \lambda^* P \to N', \quad (x',p) \cdot g = (x', p \cdot g),$$
a principal $G$-bundle over $N'$ whose fibre over $x'$ is identified with $P_{\lambda(x')}$ through $\operatorname{pr}_2$.

We use two projections and the slice inclusions:
$$\operatorname{pr} \colon M \times I \to M, \quad \operatorname{pr}(m,t) = m; \qquad \iota_t \colon M \to M \times I, \quad \iota_t(m) = (m,t) \quad (t \in I \text{ fixed}).$$
For a bundle $P \to M \times I$ we write $P|_{M \times \{t\}} := \iota_t^* P$ for its restriction to the slice at height $t$, a principal $G$-bundle over $M$ (identifying $M \times \{t\} \cong M$ through $\iota_t$); the abbreviation $P_0 := P|_{M \times \{0\}}$ is used repeatedly.

Two maps $f_0, f_1 \colon M' \to M$ are **[[Def - Smooth Homotopy of Maps|smoothly homotopic]]**, written $f_0 \simeq f_1$, when there is a smooth $H \colon M' \times I \to M$ with $H(\cdot, 0) = f_0$ and $H(\cdot, 1) = f_1$. A diffeomorphism $h \colon M \to M$ is **isotopic to the identity** when there is a smooth $H \colon M \times I \to M$ with $H(\cdot, 0) = \operatorname{id}_M$, $H(\cdot, 1) = h$, and each $H(\cdot, t)$ a diffeomorphism. A manifold $M$ is **smoothly contractible** when $\operatorname{id}_M$ is smoothly homotopic to a constant map; the [[Def - Homotopy Equivalence and Contractible Space|closed disc]] $D^n$, the interval $I$, and every convex subset of $\mathbb{R}^n$ are smoothly contractible through the straight-line homotopy $H(x,t) = (1-t)(x - x_0) + x_0$ to an interior basepoint $x_0$.

> [!warning] Convention: right actions and the meaning of "trivial"
> The structure group acts on the right throughout the series, so equivariant trivialisations intertwine the right action with right multiplication on $G$; this is the sign that makes the transition of two trivialisations a **left** multiplication by a $G$-valued map (used in Lemma 1). Haydys ($A$) states without proof, at his equation for parallel transport (p. 32), that "any bundle over an interval is trivial"; part (c) of this theorem is exactly that statement, now proved, so nothing downstream imports it.

---

# Statement

> **Theorem (homotopy invariance of principal bundles).** Let $G$ be a Lie group.
>
> **(a)** Let $P \to M \times I$ be a principal $G$-bundle over $M \times I$, where $M$ is any manifold. Then
> $$P \;\cong\; \operatorname{pr}^*\big(P|_{M \times \{0\}}\big)$$
> as principal $G$-bundles over $M \times I$. In particular the two boundary restrictions are isomorphic over $M$:
> $$P|_{M \times \{0\}} \;\cong\; P|_{M \times \{1\}}.$$
>
> **(b)** If $f_0, f_1 \colon M' \to M$ are smoothly homotopic, then $f_0^* P \cong f_1^* P$ for every principal $G$-bundle $P \to M$.
>
> **(c)** Every principal $G$-bundle over a smoothly contractible manifold is trivial. In particular every principal $G$-bundle over a closed disc $D^n$, over the interval $I$, and over $\mathbb{R}^n$ is trivial.
>
> **(d)** If $h \colon M \to M$ is a diffeomorphism isotopic to the identity, then $h^* P \cong P$ for every principal $G$-bundle $P \to M$.
>
> **(e)** The same four statements hold, with the same proofs, for real and complex vector bundles and, more generally, for fibre bundles with structure group $G$ and typical fibre $F$.

The heart of the theorem is (a); parts (b)–(e) are deduced from it.

---

# Motivation

A principal bundle over a base $M$ is a geometric object one would like to classify: to say when two bundles are "the same" and to attach to a bundle numbers or cohomology classes that see only its isomorphism type. Every such programme rests on one structural fact, and this theorem is that fact. It says that the isomorphism type of a bundle cannot detect a *deformation* of its base data: if a family of bundles is assembled into a single bundle over the cylinder $M \times I$, the two ends of the cylinder carry isomorphic bundles, however the family twists in between.

The question the theorem answers is therefore the following. Suppose two smooth maps $f_0, f_1 \colon M' \to M$ can be deformed into one another — they are smoothly homotopic. A bundle $P \to M$ can be transported to $M'$ along either map, giving $f_0^* P$ and $f_1^* P$. Are these the same bundle? If the answer were "no in general", then the operation "pull back a bundle along a map" would depend on the map in an unusable, infinitely fine way, and there would be no hope of a classification by homotopy classes of maps. The theorem says the answer is "yes always": pulling back is a *homotopy* invariant of the map. This single fact turns the study of bundles over $M$ into the study of homotopy classes of maps out of $M$, which is the entire content of §3.6 and the reason a classifying space exists at all.

The mechanism deserves to be named before it is proved, because it is completely concrete. A bundle over the cylinder $M \times I$ looks, over small patches of $M$, like a product $\text{patch} \times I \times G$. Along the interval direction of such a product there is an obvious way to move a point of the fibre over $(m,0)$ up to the fibre over $(m,t)$: keep the $G$-coordinate fixed and raise $t$. The only obstruction to doing this globally is that the patches disagree about what "keep the $G$-coordinate fixed" means. We remove the obstruction not by forcing the patches to agree — which fails, and is the source of a notorious smoothness trap discussed below — but by *averaging* the several local prescriptions with a partition of unity into one honest rule for moving up the cylinder. That rule is a vector field on the total space; its flow slides every fibre down onto the bottom fibre, and the slide is the isomorphism $P \cong \operatorname{pr}^*(P_0)$. The alternatives one might try first — gluing local trivialisations across level sets, or invoking a connection — either break smoothness or import machinery that the notes have not yet built; the averaged-lift construction needs nothing beyond a partition of unity and the existence and uniqueness of integral curves.

The reader is assumed to know principal bundles, their equivariant trivialisations and sections, the pull-back construction, smooth partitions of unity, and the existence, uniqueness, and smooth dependence of solutions of ordinary differential equations on manifolds. Nothing about connections on principal bundles (chapter IV) is used, and this is deliberate: the classification results of §3.6 and the topological invariance of the characteristic classes in chapter VI must not depend circularly on the connection theory they are used to interpret.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of part (a) is only "a principal bundle over a cylinder $M \times I$". The skill is to recognise, in a problem that never mentions a cylinder, that one is secretly present.

The first disguised source is **a smoothly varying one-parameter family of geometric structures on a fixed bundle or base**. Whenever one has, for each $t \in I$, a structure $\sigma_t$ (a Hermitian metric, a Euclidean metric, a reduction of the structure group, a choice of trivialising data) depending smoothly on $t$, the total collection assembles into a single bundle or a single reduction over $M \times I$ whose slices at $t = 0$ and $t = 1$ are the two structures one wishes to compare. The bridge $B \Rightarrow A$ is: "a smooth path of structures is a structure over $M \times I$." The non-obvious step is that one must check the family is jointly smooth in $(m,t)$, not merely smooth in $m$ for each fixed $t$. *Example problem:* two Hermitian structures $h_0, h_1$ on a complex line bundle $L \to M$ are joined by the convex path $h_t = (1-t) h_0 + t h_1$, which is again Hermitian for every $t$; the associated $U(1)$-reductions form a principal $U(1)$-bundle over $M \times I$, so by part (a) the two reductions are isomorphic, and hence the first Chern class does not depend on the choice of Hermitian structure.

The second disguised source is **a null-homotopic map**, that is, a map $f \colon M' \to M$ that can be smoothly deformed to a constant. Recognising that a given map is null-homotopic — because its target is smoothly contractible, or because it factors through a contractible piece — immediately supplies the cylinder $M' \times I$ carrying the homotopy, and part (b) then shows $f^* P \cong \text{constant}^* P$, which is trivial. The bridge is "null-homotopic $\Rightarrow$ every pull-back is trivial." *Example problem:* the inclusion of a coordinate disc $D \hookrightarrow X$ into any manifold is null-homotopic (contract $D$ to its centre), so every bundle restricted to a coordinate disc is trivial; this is the fact that makes the clutching construction of §3.5 possible.

The third disguised source is **a diffeomorphism presented as the time-one map of an isotopy** — most often, a "small" diffeomorphism such as one supported in a disc, or a flow of a compactly supported vector field. Whenever a diffeomorphism $h$ arises as $h = H(\cdot, 1)$ for a smooth path $H(\cdot, t)$ of diffeomorphisms starting at the identity, part (d) gives $h^* P \cong P$ for free. The bridge is "isotopic to the identity $\Rightarrow$ pulling back changes nothing." *Example problem:* the homogeneity lemma moves any finite set of points of a connected manifold into a single coordinate disc by a diffeomorphism isotopic to the identity; part (d) then guarantees that gathering the zeros of a generic section into one disc does not change the isomorphism type of the bundle, which is what lets the clutching invariant of §3.6 be well defined.

**Targets (Output Amplification)**

The bare output of part (a) is an isomorphism of two bundles over a cylinder. Combined with other ingredients it produces the classification theory of the whole subject.

Combine part (b) with **a universal bundle**. If $E \to B$ is a bundle with the property that every bundle over a reasonable base is pulled back from it, then part (b) shows the assignment "bundle $\mapsto$ homotopy class of its classifying map" is well defined, and the classification of bundles over $M$ becomes the computation of the homotopy set $[M; B]$. The extra ingredient is the existence of the universal bundle (the direct-limit spaces $\mathbb{CP}^\infty$ for $U(1)$ and $\mathbb{HP}^\infty$ for $Sp(1)$ built in §3.6); the payoff is the entire classification programme of §3.6.

Combine part (b) with **Chern–Weil theory**. A characteristic class is defined by a de Rham class on the base of a universal bundle, pulled back along a classifying map. Part (b) is exactly the statement that this pull-back is independent of the classifying map up to homotopy, so characteristic classes depend only on the isomorphism type of the bundle. The extra ingredient is the homotopy invariance of de Rham cohomology (chapter X); the payoff is that the Chern and Pontryagin numbers of chapter VI are genuine invariants and not artefacts of a choice.

Combine part (a) with **the clutching construction**. A bundle over a base decomposed into two pieces glued along a collar is determined by a transition map on the collar, and a homotopy of the transition map is a bundle over collar $\times I$; part (a) applied there shows that homotopic clutching maps give isomorphic bundles. The extra ingredient is the collar neighbourhood of the gluing sphere; the payoff is the degree invariant of §3.6, and in particular the "only if" half of the mapping-torus triviality criterion, that the mapping torus of a diffeomorphism $\phi$ is trivial only when $\phi$ is isotopic to the identity.

---

# Why Is It True

Set the formal proof aside and picture the cylinder $M \times I$ with the bundle $P$ sitting over it. Over a small patch $V \subseteq M \times I$ the bundle is a product $V \times G$, and inside such a product there is a canonical way to travel straight up the interval direction: move from $(m, t_0, g)$ to $(m, t_1, g)$ keeping $g$ fixed. If a single such product structure covered the whole cylinder, we could slide every fibre straight down to height $0$ and read off the isomorphism $P \cong \operatorname{pr}^*(P_0)$ instantly. The bundle is only *locally* a product, so different patches prescribe different "straight up" directions, and where two patches overlap their prescriptions differ.

The essential idea is that this disagreement is harmless because the prescriptions can be **averaged**. Each local product structure gives a vector field on the total space that points "straight up the interval, fibre coordinate held fixed"; this field is $G$-invariant, because holding the $G$-coordinate fixed is a right-equivariant instruction, and it projects down to $\partial_t$ on the base. A partition of unity subordinate to the patches lets us take a convex combination of these local fields. A convex combination of $G$-invariant fields projecting to $\partial_t$ is again a $G$-invariant field projecting to $\partial_t$ — the weights sum to one, so the projection is still exactly $\partial_t$. We have manufactured one global rule for going up the cylinder out of the many inconsistent local ones, and it is invariant under the group.

Now integrate. The flow of this field pushes points along, covering the translation $(m,t) \mapsto (m, t+s)$ downstairs; because the field is $G$-invariant, the flow commutes with the right action, so the time-shift from height $t$ to height $0$ is a $G$-equivariant diffeomorphism of the fibre over $(m,t)$ onto the fibre over $(m,0)$. Doing this at every point at once is a bundle isomorphism $P \cong \operatorname{pr}^*(P_0)$. The interval has been contracted to its bottom endpoint, and the bundle rode along.

> **Mechanism in one sentence.** A principal bundle over $M \times I$ can be slid down the interval onto its bottom face because a partition of unity averages the local "hold the fibre coordinate fixed and raise $t$" prescriptions into one $G$-invariant vector field whose flow carries each fibre equivariantly onto the fibre below it.

Part (b) is then a formality: a homotopy $H \colon M' \times I \to M$ turns two maps into the two ends of a single bundle $H^* P$ over the cylinder $M' \times I$, and part (a) says the two ends agree. The interval is not special to $I$; it is only the shape of a deformation, and the theorem says a deformation of the base data is invisible to the isomorphism type.

---

# What Makes This Hard

The tempting first proof is to glue: trivialise $P$ over $M \times [0, c]$ and over $M \times [c, 1]$, adjust the upper trivialisation by the transition function on the level set $M \times \{c\}$ so the two agree there, and declare the concatenation a global trivialisation. This is exactly right in the topological category and exactly wrong in the smooth one. Two trivialisations that agree on a level set need not agree in their derivative transverse to the level set, so the concatenated map is generally only continuous, with a corner along $M \times \{c\}$; nothing forces the $\partial_t$-derivatives to match, and no choice of the level transition function repairs it. The non-obvious move is to abandon gluing entirely and build the isomorphism as the flow of an averaged invariant vector field, where smoothness is automatic because a smooth partition of unity produces a smooth field and its flow is smooth by the theory of ordinary differential equations.

The second subtlety is completeness. The flow must be defined all the way from height $t$ to height $0$, but the fibre $G$ may be non-compact, so an integral curve could in principle escape to infinity in finite time and fail to reach the bottom. The resolution uses the group invariance a second time: because the field is $G$-invariant, the length of time an integral curve exists depends only on its base point, not on which point of the fibre it starts at; that existence time is then a positive function on the compact segment $\{m\} \times I$, hence bounded below, so the flow reaches the bottom in finitely many uniform steps. It is the invariance, not any compactness of the base, that makes the flow complete, which is why part (a) holds for an arbitrary base manifold $M$ and not only a compact one.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build a single $G$-invariant vector field on $P$ that projects to $\partial_t$ on the cylinder $M \times I$, by taking each local trivialisation's "raise $t$, hold the fibre fixed" field and averaging them with a partition of unity. Show its flow is defined across the whole interval and is $G$-equivariant fibre to fibre. Assemble the fibre-to-fibre flow maps down to height $0$ into the isomorphism $P \cong \operatorname{pr}^*(P_0)$. Deduce the rest.

**Subgoal decomposition:**

1. **Construct the invariant lift.** Produce a $G$-invariant vector field $\xi$ on $P$ with $d\pi(\xi_p) = \partial_t|_{\pi(p)}$ for all $p$.
   - *Hint:* Over a trivialising open $V_\alpha$, take the field $(\partial_t, 0)$ on $V_\alpha \times G$ and pull it back; this is invariant and projects to $\partial_t$. Average with a partition of unity $\{\rho_\alpha\}$ pulled back from the base.
   - *Why needed:* This one field replaces all the inconsistent local product structures with a single global rule for moving up the cylinder, and its smoothness is guaranteed by the smoothness of the partition of unity.

2. **Flow it across the interval, equivariantly and completely.** Show the integral curves of $\xi$ starting over $(m, t_0)$ reach every height $t_1 \in I$, and that the resulting time-shift maps $\Phi_{t_1 \leftarrow t_0} \colon P_{(m,t_0)} \to P_{(m,t_1)}$ are $G$-equivariant diffeomorphisms satisfying the flow relations.
   - *Hint:* Uniqueness gives $R_g \circ \gamma_p = \gamma_{p \cdot g}$, so existence time depends only on the base point; minimise it over the compact segment $\{m\} \times I$.
   - *Why needed:* Without completeness the slide to the bottom is not defined; without equivariance it is not a bundle map.

3. **Assemble the isomorphism.** Define $F(p) = (\pi(p), \Phi_{0 \leftarrow t}(p))$ for $p \in P_{(m,t)}$ and verify it is a principal-bundle isomorphism $P \to \operatorname{pr}^*(P_0)$.
   - *Hint:* The inverse is $((m,t), q) \mapsto \Phi_{t \leftarrow 0}(q)$; smoothness is joint smoothness of the flow, equivariance is subgoal 2.
   - *Why needed:* This is part (a); everything else is a corollary.

4. **Deduce (b)–(e).** Apply (a) to $H^* P$ for a homotopy $H$ to get (b); apply (b) to a contraction and to an isotopy to get (c) and (d); pass through the frame bundle and the associated-bundle construction to get (e).
   - *Hint:* For (b) use functoriality of pull-back, $(H \circ \iota_i)^* P \cong \iota_i^* H^* P$; for (c) note the pull-back along a constant map has a global section.
   - *Why needed:* These are the statements actually used downstream.

---

# Lemma Decomposition

> [!note]- Lemma 1: A principal bundle admits a $G$-invariant lift of any base vector field
> **Statement:** Let $\pi \colon Q \to N$ be a principal $G$-bundle and $X$ a smooth vector field on $N$. Then there is a smooth $G$-invariant vector field $\xi$ on $Q$ — meaning $(R_g)_* \xi = \xi$, that is $d R_g(\xi_q) = \xi_{q \cdot g}$ for all $g \in G$, $q \in Q$ — such that $d\pi(\xi_q) = X_{\pi(q)}$ for every $q \in Q$.
>
> **Hint:** Over each trivialising open $V_\alpha$ the field $(X|_{V_\alpha}, 0)$ on $V_\alpha \times G$ pulls back to an invariant lift; average these with a partition of unity subordinate to $\{V_\alpha\}$, pulled back to $Q$.
>
> **Why needed:** With $N = M \times I$ and $X = \partial_t$, the field $\xi$ is the single global "move up the cylinder" rule whose flow produces the isomorphism; the averaging is what makes it smooth and defined everywhere.
>
> > [!note]- Full proof
> > **Goal.** Construct a smooth $G$-invariant vector field $\xi$ on $Q$ projecting under $d\pi$ to $X$.
> >
> > **Step 1 — the local lifts.** Choose a cover $\{V_\alpha\}_{\alpha \in A}$ of $N$ by open sets over which $Q$ is trivial, with $G$-equivariant trivialisations $\Psi_\alpha \colon \pi^{-1}(V_\alpha) \to V_\alpha \times G$ satisfying $\operatorname{pr}_{V_\alpha} \circ \Psi_\alpha = \pi$ and $\Psi_\alpha(q \cdot g) = \Psi_\alpha(q) \cdot g$ (such a cover exists by the definition of a principal bundle). On the product $V_\alpha \times G$ consider the vector field whose value at $(x, h)$ is
> > $$Y_\alpha(x,h) = \big(X_x,\, 0_h\big) \in T_x V_\alpha \oplus T_h G = T_{(x,h)}(V_\alpha \times G),$$
> > that is, the horizontal-in-the-base field lifting $X$ with zero component along $G$. Pull it back to $\pi^{-1}(V_\alpha)$ by setting $\xi_\alpha := (\Psi_\alpha^{-1})_* Y_\alpha$, a smooth vector field on $\pi^{-1}(V_\alpha)$.
> >
> > **Step 2 — each local lift is invariant and projects to $X$.** The right action on $V_\alpha \times G$ is $(x,h) \cdot g = (x, hg)$, and its differential sends $(X_x, 0_h) \mapsto (X_x, 0_{hg})$ (right translation on $G$ carries the zero vector to the zero vector), so $(R_g)_* Y_\alpha = Y_\alpha$. Because $\Psi_\alpha$ is $G$-equivariant, conjugating by it preserves invariance: $(R_g)_* \xi_\alpha = \xi_\alpha$ on $\pi^{-1}(V_\alpha)$ (since $\Psi_\alpha \circ R_g = R_g \circ \Psi_\alpha$). Moreover $\operatorname{pr}_{V_\alpha} \circ \Psi_\alpha = \pi$ gives $d\pi = d\operatorname{pr}_{V_\alpha} \circ d\Psi_\alpha$, and $d\operatorname{pr}_{V_\alpha}(Y_\alpha) = X$, so
> > $$d\pi(\xi_\alpha) = d\operatorname{pr}_{V_\alpha}\big(d\Psi_\alpha (\Psi_\alpha^{-1})_* Y_\alpha\big) = d\operatorname{pr}_{V_\alpha}(Y_\alpha) = X \qquad \text{(chain rule; definition of } \xi_\alpha \text{)}.$$
> >
> > **Step 3 — average with a partition of unity.** By the [[Thm - Existence of Smooth Partitions of Unity|existence of smooth partitions of unity]] on the second-countable manifold $N$ (the argument applies verbatim to a manifold with boundary, which is the case $N = M \times I$ we need), choose a smooth partition of unity $\{\rho_\alpha\}_{\alpha \in A}$ subordinate to $\{V_\alpha\}$: each $\rho_\alpha \colon N \to [0,1]$ is smooth with $\operatorname{supp}\rho_\alpha \subseteq V_\alpha$, the family $\{\operatorname{supp}\rho_\alpha\}$ is locally finite, and $\sum_\alpha \rho_\alpha \equiv 1$. Define
> > $$\xi := \sum_{\alpha \in A} (\rho_\alpha \circ \pi)\, \xi_\alpha,$$
> > where each summand $(\rho_\alpha \circ \pi)\,\xi_\alpha$, a priori defined on $\pi^{-1}(V_\alpha)$, is extended by the zero field over $Q \setminus \pi^{-1}(\operatorname{supp}\rho_\alpha)$. This extension is smooth because $\rho_\alpha \circ \pi$ vanishes with all derivatives on a neighbourhood of the boundary of $\pi^{-1}(\operatorname{supp}\rho_\alpha)$ inside $\pi^{-1}(V_\alpha)$; local finiteness of $\{\pi^{-1}(\operatorname{supp}\rho_\alpha)\}$ (the preimage of a locally finite family under the continuous $\pi$) makes the sum locally finite, hence a smooth vector field on $Q$.
> >
> > **Step 4 — the average is invariant and projects to $X$.** Each coefficient $\rho_\alpha \circ \pi$ is constant on the fibres of $\pi$, hence $G$-invariant as a function, and each $\xi_\alpha$ is $G$-invariant by Step 2, so each summand is $G$-invariant and therefore so is $\xi$. For the projection, $d\pi$ is fibrewise linear and $\rho_\alpha \circ \pi$ is a scalar constant along each fibre, so at $q$ with $\pi(q) = x$,
> > $$d\pi(\xi_q) = \sum_{\alpha} \rho_\alpha(x)\, d\pi(\xi_{\alpha, q}) = \sum_{\alpha} \rho_\alpha(x)\, X_x = \Big(\sum_\alpha \rho_\alpha(x)\Big) X_x = X_x \qquad \text{(Step 2; } \textstyle\sum_\alpha \rho_\alpha \equiv 1 \text{)}.$$
> >
> > **Conclusion.** The field $\xi$ is smooth, $G$-invariant, and projects to $X$. $\blacksquare$

> [!note]- Lemma 2: The flow of an invariant lift of $\partial_t$ is complete across $I$ and equivariant fibre to fibre
> **Statement:** Let $\xi$ be a $G$-invariant vector field on the principal $G$-bundle $\pi \colon P \to M \times I$ with $d\pi(\xi) = \partial_t$. Then for every $m \in M$, every $t_0 \in I$, and every $p \in P_{(m, t_0)}$, the maximal integral curve $\gamma_p$ of $\xi$ with $\gamma_p(0) = p$ is defined for all $s$ with $t_0 + s \in I$, and $\pi(\gamma_p(s)) = (m, t_0 + s)$. Consequently, for $t_0, t_1 \in I$ the **transport maps**
> $$\Phi_{t_1 \leftarrow t_0} \colon P_{(m,t_0)} \to P_{(m,t_1)}, \qquad \Phi_{t_1 \leftarrow t_0}(p) := \gamma_p(t_1 - t_0),$$
> are $G$-equivariant diffeomorphisms, jointly smooth in $(m, p)$, with $\Phi_{t_0 \leftarrow t_0} = \operatorname{id}$ and $\Phi_{t_2 \leftarrow t_1} \circ \Phi_{t_1 \leftarrow t_0} = \Phi_{t_2 \leftarrow t_0}$.
>
> **Hint:** Uniqueness of integral curves gives $R_g \circ \gamma_p = \gamma_{p \cdot g}$, so the existence time is a function of the base point alone; minimise this positive function over the compact segment $\{m\} \times I$ to reach either endpoint in finitely many steps.
>
> **Why needed:** The transport maps are the fibre-to-fibre isomorphisms out of which the global isomorphism of part (a) is built; completeness guarantees they reach the bottom face, equivariance makes them bundle maps.
>
> > [!note]- Full proof
> > **Goal.** Show the integral curves reach across $I$ and that the transport maps are equivariant diffeomorphisms with the flow relations.
> >
> > **Step 1 — integral curves exist locally and project to translations.** By the [[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]] — for a smooth vector field on a manifold, through each point there is a unique maximal integral curve, the flow domain is open in $\mathbb{R} \times P$, and the flow is smooth on it — each $p$ has a unique maximal integral curve $\gamma_p$ of $\xi$ with $\gamma_p(0) = p$, defined on an open interval $J_p \ni 0$. Since $d\pi(\xi) = \partial_t$, the composite $\pi \circ \gamma_p$ is an integral curve of $\partial_t$ on $M \times I$, and integral curves of $\partial_t$ are $s \mapsto (m, t_0 + s)$; hence $\pi(\gamma_p(s)) = (m, t_0 + s)$ wherever $\gamma_p$ is defined, and in particular the projected curve stays in the segment $\{m\} \times I$ exactly while $t_0 + s \in I$. (Here $\partial_t$ points strictly into $M \times I$ along $M \times \{0\}$ and out along $M \times \{1\}$; the curves we use travel between heights $0$ and $t_0 \le 1$ and so remain in $M \times I$ throughout, meeting the boundary only at their endpoints, where the fundamental theorem applies in a boundary chart.)
> >
> > **Step 2 — equivariance of integral curves.** Fix $g \in G$. Because $\xi$ is $G$-invariant, $d R_g(\xi_q) = \xi_{q \cdot g}$, so
> > $$\frac{d}{ds}\big(R_g(\gamma_p(s))\big) = d R_g\big(\dot\gamma_p(s)\big) = d R_g\big(\xi_{\gamma_p(s)}\big) = \xi_{R_g(\gamma_p(s))} \qquad \text{(chain rule; } \dot\gamma_p = \xi \text{ along } \gamma_p \text{; invariance of } \xi \text{)}.$$
> > Thus $s \mapsto R_g(\gamma_p(s))$ is an integral curve of $\xi$ starting at $p \cdot g$; by uniqueness it equals $\gamma_{p \cdot g}$. In particular $J_{p \cdot g} = J_p$: the existence interval is unchanged by the right action.
> >
> > **Step 3 — completeness across $I$.** By Step 2 the maximal existence interval $J_p$ depends only on $\pi(p) = (m, t_0)$; write its forward endpoint as $s^+(m, t_0) \in (0, +\infty]$. The flow domain is open (Step 1), so $s^+$ is lower semicontinuous, and it is strictly positive at every base point by local existence. On the compact segment $\{m\} \times I$ a strictly positive lower semicontinuous function attains a positive minimum $\delta > 0$. Now suppose, for contradiction, that some $\gamma_p$ with $\pi(p) = (m, t_0)$ failed to reach a height $t_1 > t_0$ in $I$: let $s^* = \sup\{s : t_0 + s \le t_1,\ \gamma_p \text{ defined on } [0,s]\}$, so $t_0 + s^* \le t_1 \le 1$ and $\gamma_p$ is not defined on $[0, s^* + \varepsilon]$ for any $\varepsilon > 0$. But the point $q := \gamma_p(s^* - \delta/2)$ lies over $(m, t_0 + s^* - \delta/2) \in \{m\} \times I$, whose forward existence time is at least $\delta$, so $\gamma_q$ — which equals $s \mapsto \gamma_p(s^* - \delta/2 + s)$ by uniqueness — is defined on $[0, \delta]$, extending $\gamma_p$ past $s^*$, a contradiction. Hence every height in $I$ is reached going forward; the same argument with $\partial_t$ replaced by $-\partial_t$ handles going backward. Therefore $\gamma_p$ is defined for all $s$ with $t_0 + s \in I$.
> >
> > **Step 4 — the transport maps are equivariant diffeomorphisms with the flow relations.** For $t_0, t_1 \in I$ the map $\Phi_{t_1 \leftarrow t_0}(p) = \gamma_p(t_1 - t_0)$ is defined on all of $P_{(m,t_0)}$ by Step 3 and lands in $P_{(m, t_1)}$ by Step 1. It is smooth in $p$ (indeed jointly in $(m,p)$) because the flow is smooth (Step 1). Uniqueness of integral curves gives the cocycle relations $\Phi_{t_0 \leftarrow t_0} = \operatorname{id}$ and $\Phi_{t_2 \leftarrow t_1} \circ \Phi_{t_1 \leftarrow t_0} = \Phi_{t_2 \leftarrow t_0}$, whence $\Phi_{t_1 \leftarrow t_0}$ is a diffeomorphism with inverse $\Phi_{t_0 \leftarrow t_1}$. Finally, equivariance is Step 2 evaluated at parameter $t_1 - t_0$:
> > $$\Phi_{t_1 \leftarrow t_0}(p \cdot g) = \gamma_{p \cdot g}(t_1 - t_0) = R_g\big(\gamma_p(t_1 - t_0)\big) = \Phi_{t_1 \leftarrow t_0}(p) \cdot g.$$
> >
> > **Conclusion.** The transport maps are $G$-equivariant diffeomorphisms between fibres, jointly smooth, satisfying the flow relations. $\blacksquare$

> [!note]- Lemma 3: The transport maps assemble into the isomorphism $P \cong \operatorname{pr}^*(P_0)$
> **Statement:** With $\xi$, $\Phi$ as in Lemmas 1–2 for $P \to M \times I$, the map
> $$F \colon P \to \operatorname{pr}^*(P_0), \qquad F(p) = \big(\pi(p),\, \Phi_{0 \leftarrow t}(p)\big) \quad \text{for } p \in P_{(m,t)},$$
> is an isomorphism of principal $G$-bundles over $M \times I$, where $P_0 = P|_{M \times \{0\}}$.
>
> **Hint:** Check in turn that $F$ covers the identity, is $G$-equivariant, is smooth with smooth inverse $((m,t), q) \mapsto \Phi_{t \leftarrow 0}(q)$.
>
> **Why needed:** This is precisely part (a); the boundary case $t = 1$ gives $P_0 \cong P_1$.
>
> > [!note]- Full proof
> > **Goal.** Show $F$ is a $G$-equivariant diffeomorphism covering $\operatorname{id}_{M \times I}$.
> >
> > **Step 0 — $F$ lands in $\operatorname{pr}^*(P_0)$.** Recall $\operatorname{pr}^*(P_0) = \{((m,t), q) : q \in (P_0)_m = P_{(m,0)}\}$ with projection $((m,t),q) \mapsto (m,t)$ and right action $((m,t),q) \cdot g = ((m,t), q \cdot g)$ (the pull-back structure of the [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|pull-back bundle]] along $\operatorname{pr}$). For $p \in P_{(m,t)}$ we have $\pi(p) = (m,t)$ and $\Phi_{0 \leftarrow t}(p) \in P_{(m,0)} = (P_0)_m$ by Lemma 2, so $F(p) = ((m,t), \Phi_{0\leftarrow t}(p))$ is a legitimate element of $\operatorname{pr}^*(P_0)$.
> >
> > **Step 1 — $F$ covers the identity.** The projection of $F(p)$ is its first coordinate $\pi(p) = (m,t)$, so $\operatorname{pr}_1 \circ F = \pi$, that is $F$ covers $\operatorname{id}_{M \times I}$.
> >
> > **Step 2 — $F$ is $G$-equivariant.** For $p \in P_{(m,t)}$ and $g \in G$, using the equivariance of the transport maps (Lemma 2) and the right action on the pull-back,
> > $$F(p \cdot g) = \big((m,t),\, \Phi_{0 \leftarrow t}(p \cdot g)\big) = \big((m,t),\, \Phi_{0 \leftarrow t}(p) \cdot g\big) = F(p) \cdot g.$$
> >
> > **Step 3 — $F$ is smooth with a smooth inverse.** The height $t$ is the smooth function $\operatorname{pr}_I \circ \pi$ of $p$, and the transport $\Phi_{0 \leftarrow t}(p)$ is jointly smooth in $(p, t)$ by Lemma 2, so $F$ is smooth. Define
> > $$F^{-1} \colon \operatorname{pr}^*(P_0) \to P, \qquad F^{-1}\big((m,t), q\big) = \Phi_{t \leftarrow 0}(q).$$
> > This is smooth by the same joint smoothness, and it is a two-sided inverse: $F^{-1}(F(p)) = \Phi_{t \leftarrow 0}(\Phi_{0 \leftarrow t}(p)) = p$ and $F(F^{-1}((m,t),q)) = ((m,t), \Phi_{0 \leftarrow t}(\Phi_{t \leftarrow 0}(q))) = ((m,t), q)$, using $\Phi_{0 \leftarrow t} \circ \Phi_{t \leftarrow 0} = \operatorname{id}$ and $\Phi_{t \leftarrow 0} \circ \Phi_{0 \leftarrow t} = \operatorname{id}$ from the flow relations (Lemma 2).
> >
> > **Conclusion.** $F$ is a $G$-equivariant diffeomorphism covering the identity, hence an isomorphism $P \cong \operatorname{pr}^*(P_0)$ of principal $G$-bundles. Restricting $F$ to the slice $t = 1$ gives a $G$-equivariant diffeomorphism $P_{(m,1)} \to P_{(m,0)}$ over $M$, that is $P|_{M \times \{1\}} \cong P|_{M \times \{0\}}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a Lie group.
>
> **Part (a).** Let $P \to M \times I$ be a principal $G$-bundle over an arbitrary manifold $M$. By **Lemma 1**, applied with $N = M \times I$ and $X = \partial_t$, there is a $G$-invariant vector field $\xi$ on $P$ with $d\pi(\xi) = \partial_t$. By **Lemma 2**, the flow of $\xi$ provides, for each $m$ and each pair of heights, the $G$-equivariant transport diffeomorphisms $\Phi_{t_1 \leftarrow t_0} \colon P_{(m,t_0)} \to P_{(m,t_1)}$, defined for all heights in $I$ and satisfying the flow relations. By **Lemma 3**, the map $F(p) = (\pi(p), \Phi_{0 \leftarrow t}(p))$ is an isomorphism of principal $G$-bundles $P \cong \operatorname{pr}^*(P_0)$, and its restriction to the top face gives $P|_{M \times \{1\}} \cong P|_{M \times \{0\}}$. This is part (a). Note that only the compactness of each individual segment $\{m\} \times I$ was used (in Lemma 2, Step 3); no compactness of $M$ is required, so (a) holds for every manifold $M$.
>
> **Part (b).** Let $f_0, f_1 \colon M' \to M$ be smoothly homotopic, with smooth homotopy $H \colon M' \times I \to M$, $H(\cdot, 0) = f_0$, $H(\cdot, 1) = f_1$, and let $P \to M$ be a principal $G$-bundle. By the [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|pull-back theorem]] — the pull-back of a principal $G$-bundle along a smooth map is again a principal $G$-bundle — $H^* P$ is a principal $G$-bundle over $M' \times I$.
>
> **Functoriality of pull-back.** For $i \in \{0,1\}$, write $\iota_i \colon M' \to M' \times I$, $\iota_i(m') = (m', i)$, so that $H \circ \iota_i = f_i$. We claim the canonical identification
> $$\iota_i^*(H^* P) \;\cong\; (H \circ \iota_i)^* P = f_i^* P$$
> is an isomorphism of principal $G$-bundles over $M'$. Indeed, by the fibre description of the pull-back, the fibre of $\iota_i^*(H^*P)$ over $m'$ is $(H^*P)_{(m', i)} = P_{H(m', i)} = P_{f_i(m')}$, which is exactly the fibre of $f_i^* P$ over $m'$; the map $(m', (( m',i), p)) \mapsto (m', p)$ realises this identification as a $G$-equivariant diffeomorphism over $\operatorname{id}_{M'}$ (it intertwines the right actions, which act on the $P$-coordinate in both bundles, and covers the identity). Hence $\iota_i^*(H^* P) \cong f_i^* P$.
>
> Now apply part (a) to the bundle $Q := H^* P$ over $M' \times I$: its two boundary restrictions are isomorphic, $Q|_{M' \times \{0\}} \cong Q|_{M' \times \{1\}}$, that is $\iota_0^*(H^* P) \cong \iota_1^*(H^* P)$. Combining with the functoriality isomorphism at $i = 0$ and $i = 1$,
> $$f_0^* P \cong \iota_0^*(H^* P) \cong \iota_1^*(H^* P) \cong f_1^* P,$$
> which is part (b).
>
> **Part (c).** Let $M$ be smoothly contractible: there is a smooth homotopy from $\operatorname{id}_M$ to a constant map $c_{x_0} \colon M \to M$, $c_{x_0}(m) = x_0$. Let $P \to M$ be a principal $G$-bundle. By part (b) applied to $f_0 = \operatorname{id}_M$ and $f_1 = c_{x_0}$,
> $$P = \operatorname{id}_M^* P \;\cong\; c_{x_0}^* P.$$
> The pull-back $c_{x_0}^* P$ has fibre $P_{x_0}$ over every point of $M$, and it admits a global smooth section: fixing any $p_0 \in P_{x_0}$, the map $s \colon M \to c_{x_0}^* P$, $s(m) = (m, p_0)$, satisfies $\operatorname{pr}_1(s(m)) = m$ and is smooth. By the [[Thm - Sections of a Principal Bundle and Triviality|section–triviality theorem]] — a principal $G$-bundle is trivial if and only if it admits a global smooth section — $c_{x_0}^* P$ is trivial, and therefore so is $P$. The closed disc $D^n$, the interval $I = [0,1]$, and every convex $C \subseteq \mathbb{R}^n$ are smoothly contractible through the straight-line homotopy $H(x, t) = (1-t)(x - x_0) + x_0$ to an interior point $x_0$, which is smooth and, at each $t$, valued in the (convex) set; hence every principal $G$-bundle over any of these bases is trivial. In particular every principal $G$-bundle over $I$ is trivial, which is the fact used without proof at Haydys's parallel-transport construction.
>
> **Part (d).** Let $h \colon M \to M$ be a diffeomorphism isotopic to the identity, so there is a smooth $H \colon M \times I \to M$ with $H(\cdot, 0) = \operatorname{id}_M$ and $H(\cdot, 1) = h$ (isotopy through diffeomorphisms is in particular a smooth homotopy of maps). By part (b) with $f_0 = \operatorname{id}_M$ and $f_1 = h$,
> $$h^* P \cong \operatorname{id}_M^* P = P,$$
> which is part (d).
>
> **Part (e).** We reduce the vector-bundle and fibre-bundle cases to the principal case just proved.
>
> *Vector bundles.* Let $E \to M \times I$ be a real (or complex) vector bundle of rank $r$. Its [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E) \to M \times I$ is a principal $\mathrm{GL}_r$-bundle. By part (a) applied to $\operatorname{Fr}(E)$,
> $$\operatorname{Fr}(E) \;\cong\; \operatorname{pr}^*\big(\operatorname{Fr}(E)|_{M \times \{0\}}\big) = \operatorname{pr}^*\big(\operatorname{Fr}(E|_{M \times \{0\}})\big),$$
> the last equality because forming the frame bundle commutes with restriction (a frame of $E$ at $(m,0)$ is a frame of $E|_{M \times \{0\}}$ at $m$). By the [[Thm - Vector Bundles are Associated to Their Frame Bundles|associated-frame-bundle theorem]] a vector bundle is recovered from its frame bundle as the associated bundle $E \cong \operatorname{Fr}(E) \times_{\mathrm{GL}_r} \mathbb{K}^r$, and the [[Def - Associated Bundle|associated-bundle construction]] $Q \mapsto Q \times_{\mathrm{GL}_r} \mathbb{K}^r$ sends isomorphic principal bundles to isomorphic vector bundles and commutes with pull-back (both facts are immediate from the fibre description: $(\lambda^* Q) \times_{\mathrm{GL}_r} \mathbb{K}^r \cong \lambda^*(Q \times_{\mathrm{GL}_r} \mathbb{K}^r)$ fibrewise). Applying this functor to the displayed isomorphism gives $E \cong \operatorname{pr}^*(E|_{M \times \{0\}})$, the vector-bundle form of (a); parts (b)–(d) then follow for vector bundles by the identical deductions.
>
> *Fibre bundles with structure group $G$.* Let $E \to M \times I$ be a fibre bundle with typical fibre $F$ and structure group $G$ acting effectively on $F$, so $E$ is given by a cocycle $\{g_{\alpha\beta}\}$ with values in $G$. The [[Thm - Principal Bundles are Classified by Cocycles|cocycle construction]] produces a principal $G$-bundle $P \to M \times I$ with the same cocycle, and $E \cong P \times_G F$ is the associated fibre bundle. By part (a), $P \cong \operatorname{pr}^*(P|_{M \times \{0\}})$; since $\cdot \times_G F$ carries isomorphic principal bundles to isomorphic fibre bundles and commutes with pull-back (again from the fibre description), $E \cong \operatorname{pr}^*(E|_{M \times \{0\}})$, and parts (b)–(d) follow as before.
>
> This completes the proof of all five parts. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Independence of a construction from an auxiliary metric or reduction.** Many objects in geometry are built after choosing an auxiliary structure — a Riemannian metric to define an orthonormal frame bundle, a Hermitian structure to define a $U(1)$-reduction, a connection to define horizontal lifts. To show the resulting bundle does not depend on the choice, join two choices by a smooth convex path and assemble the family into a bundle over $M \times I$; the theorem's part (a) then forces the two ends to be isomorphic. The theorem applies because the space of such structures is convex, so any two lie on a smooth segment, and it is non-obvious because "the same construction with different input" is not visibly a cylinder until the convex path is drawn.

**Triviality of bundles over building blocks in a decomposition.** When a manifold is cut into contractible pieces — a coordinate disc and its complement thickened by a collar, or the cells of a handle decomposition — one wants each piece to carry only trivial bundles so that the global bundle is determined by gluing data. Part (c) supplies exactly this: every bundle over a contractible piece is trivial. The theorem applies because coordinate discs and cells are smoothly contractible, and it is non-obvious that no local invariant survives, since a priori a bundle over a disc could be knotted in a way a single chart does not reveal.

**Invariance under symmetries of the base.** If a Lie group or a discrete group acts on $M$ through diffeomorphisms isotopic to the identity — for instance the identity component of the diffeomorphism group, or the flow of a complete vector field — then part (d) shows each such symmetry fixes the isomorphism type of every bundle. The theorem applies because time-one maps of flows are isotopic to the identity through the flow itself, and it is non-obvious because the symmetry may move the base substantially while leaving every bundle unmoved up to isomorphism; this is the mechanism behind the invariance of the clutching degree under the homogeneity lemma.

---

# Bridges

- **Classification by homotopy classes of maps (§3.6).** Part (b) is the well-definedness statement without which the classification cannot be phrased: it says the map "principal bundle $\mapsto$ homotopy class of its classifying map" is well defined and injective on homotopy classes. Concretely, once §3.6 exhibits a bundle $E \to B$ from which every bundle over $M$ is a pull-back, two classifying maps $f, f' \colon M \to B$ with $f \simeq f'$ give $f^* E \cong f'^* E$ by part (b), so the assignment descends to the homotopy set $[M; B]$; the converse, that isomorphic bundles have homotopic classifying maps, is the harder half proved there. The construction is the pull-back square of the universal bundle, and part (b) is the only ingredient that makes the vertical arrow depend only on the homotopy class of the horizontal one.

- **Topological invariance of characteristic classes (chapter VI).** A characteristic class of $P \to M$ is defined as $f_P^* c$, the pull-back of a fixed de Rham class $c$ on the base of the universal bundle along a classifying map $f_P$ of $P$. Part (b) shows $f_P$ is determined up to smooth homotopy by the isomorphism type of $P$, and the homotopy invariance of de Rham cohomology (chapter X) shows homotopic maps induce equal maps on cohomology, so $f_P^* c$ depends only on the isomorphism class of $P$. The bridge is the composition of two independent homotopy-invariance statements — one for bundles (this theorem), one for cohomology — meeting at the classifying map.

- **The mapping-torus triviality criterion (its converse).** The mapping torus $E_\phi \to S^1$ of a diffeomorphism $\phi \colon F \to F$ is trivial when $\phi$ is isotopic to the identity, by an explicit untwisting; the converse, that triviality forces $\phi \simeq \operatorname{id}$, runs through this theorem. Cutting $S^1$ at a point exhibits $E_\phi$ over the two arcs with clutching data recording $\phi$; a triviality of $E_\phi$ is a homotopy of the clutching data to the constant, and applying part (a) over the collar $S^0 \times I$ of the cut translates that homotopy into an isotopy of $\phi$ to the identity. The construction is the clutching description of §3.6 combined with part (a) on the collar; this is the route by which the "only if" half of the mapping-torus theorem (Bär's Theorem 2.1.1) is completed.

- **Independence of the first Chern class from the Hermitian structure.** Two Hermitian structures $h_0, h_1$ on a complex line bundle are joined by the convex path $h_t = (1-t)h_0 + t h_1$; the unit-circle subbundles of $(L, h_t)$ form a principal $U(1)$-bundle over $M \times I$ whose ends are the two $U(1)$-reductions. By part (a) the ends are isomorphic, so the reductions are isomorphic principal $U(1)$-bundles and carry the same first Chern class. The construction is the convex combination of Hermitian forms, which stays Hermitian, turning a choice into a cylinder.

---

# Unlocked by This

> [!tip] Classifying spaces and the set $[M; B]$ *(from Algebraic Topology)*
> Part (b) is the technical core that lets isomorphism classes of principal $G$-bundles over $M$ be identified with homotopy classes of maps $M \to B$ into a classifying space. The direct-limit models $\mathbb{CP}^\infty$ for $U(1)$ and $\mathbb{HP}^\infty$ for $Sp(1)$, and the classification theorems built on them, are developed on the pages [[Def - Classifying Bundle and Classifying Map]] and [[Thm - Line Bundles over Compact Manifolds are Pulled Back from Projective Space]].

> [!tip] The clutching construction *(from Bundle Theory)*
> Part (c), that bundles over contractible pieces are trivial, and part (d), that isotopies of the base do not change bundles, are the two facts that make clutching well defined: a bundle over a closed manifold that is trivial off a disc is described by a transition map on the boundary sphere, and homotopic transition maps give isomorphic bundles. This is carried out on [[Thm - Clutching Construction for Bundles over a Closed Manifold]].
