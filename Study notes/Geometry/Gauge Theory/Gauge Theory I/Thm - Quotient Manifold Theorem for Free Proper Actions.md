---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Thm - Regular Value Theorem on Manifolds"
  - "Thm - The Rank Theorem"
  - "Thm - The Inverse Function Theorem"
  - "Def - Equivariant Map"
  - "Thm - Universal Property of the Quotient"
tags: [geometry, gauge-theory, lie-groups]
---

# Notation

Throughout, $G$ is a Lie group with identity $e$ and $\dim G = k$, and $M$ is a smooth manifold with $\dim M = m$; "smooth" means $C^\infty$, and manifolds are Hausdorff and second countable. We follow the series convention that Lie groups act on the objects of gauge theory on the **right**, so we state and prove the theorem for a smooth right action

$$\mu : M \times G \longrightarrow M, \qquad \mu(x, g) = x \cdot g, \qquad x \cdot (gh) = (x \cdot g) \cdot h, \quad x \cdot e = x,$$

and record the left-action version at the end, obtained from the [[Def - Free, Transitive, Effective, and Proper Group Actions|left–right dictionary]] $x * g := g^{-1} \cdot x$. For each $g \in G$ the map $R_g : M \to M$, $R_g(x) = x \cdot g$, is a diffeomorphism with inverse $R_{g^{-1}}$. The **orbit** of $x$ is $x \cdot G := \{x \cdot g : g \in G\}$, the **orbit space** is $M/G := \{x \cdot G : x \in M\}$ carrying the quotient topology, and the **quotient map** (or **projection**) is

$$\pi : M \longrightarrow M/G, \qquad \pi(x) = x \cdot G.$$

The action is [[Def - Free, Transitive, Effective, and Proper Group Actions|**free**]] if $x \cdot g = x$ for some $x$ forces $g = e$; it is [[Def - Free, Transitive, Effective, and Proper Group Actions|**proper**]] if the map

$$\Theta : G \times M \longrightarrow M \times M, \qquad \Theta(g, x) = (x \cdot g, \, x),$$

is a **proper map**, meaning $\Theta^{-1}(K)$ is compact for every compact $K \subseteq M \times M$. For $p \in M$ the **orbit map** is $\theta^{(p)} : G \to M$, $\theta^{(p)}(g) = p \cdot g$; it is the restriction of $\mu$ and hence smooth. The [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] of $\xi \in \mathfrak{g} = T_eG$ is $\xi_M(x) = \tfrac{d}{dt}\big|_{0}\, x \cdot \exp(t\xi) = d_e\theta^{(x)}(\xi)$, so the image of $d_e\theta^{(p)}$ is the space of fundamental vectors at $p$. The words [[Def - Immersion, Submersion, and Embedding|immersion, submersion, and embedding]] are used in the standard sense, and $\operatorname{pr}_1, \operatorname{pr}_2$ denote the two projections of a product. A **local section** of $\pi$ over an open set $W \subseteq M/G$ is a smooth map $\sigma : W \to M$ with $\pi \circ \sigma = \operatorname{id}_W$.

> [!warning] Convention: "properly discontinuous" versus "proper"
> Haydys (in the construction of the associated bundle $P \times_\varrho V$, and in the insight items I2.2.2–I2.2.3) calls the free $G$-action on $P \times V$ by $(p, v) \cdot g = (p \cdot g, \varrho(g^{-1}) v)$ "**properly discontinuous**." For a **positive-dimensional** Lie group this is a misnomer: "properly discontinuous" is reserved for **discrete** groups (see [[Def - Discrete Group and Properly Discontinuous Action]]), where it is a genuinely different, combinatorial condition. The correct hypothesis making $(P \times V)/G$ a manifold when $G$ is a general Lie group is that the action be **free and proper**, which is exactly what this theorem requires. The two notions coincide only in the discrete case, where properly discontinuous $\iff$ free and proper (proved on the discrete-group definition page). Wherever a later chapter quotes Haydys's phrase for a non-discrete group, read it as "free and proper" and apply the present theorem.

---

# Statement

> **Theorem (Quotient Manifold Theorem for free proper actions).** Let $G$ be a Lie group of dimension $k$ acting smoothly, **freely**, and **properly** on a smooth manifold $M$ of dimension $m$ (on either side). Then:
>
> 1. **(Manifold structure.)** The orbit space $M/G$ admits a unique smooth manifold structure of dimension $m - k$ for which the quotient map $\pi : M \to M/G$ is a smooth **submersion**.
> 2. **(Topology.)** With this structure $M/G$ is Hausdorff and second countable.
> 3. **(Local sections.)** Every point of $M/G$ has a neighbourhood $W$ over which $\pi$ admits a smooth local section $\sigma : W \to M$, $\pi \circ \sigma = \operatorname{id}_W$.
> 4. **(Universal property.)** For every smooth manifold $N$ and every smooth map $f : M \to N$ that is constant on the orbits of $G$, there is a **unique** smooth map $\tilde f : M/G \to N$ with $\tilde f \circ \pi = f$.

> **Corollary (compact group, free action).** If $G$ is **compact** and acts smoothly and freely on $M$, then the action is automatically proper, so all four conclusions hold. In particular $\dim(M/G) = \dim M - \dim G$ and $\pi$ is a smooth submersion.

The corollary is the form in which Bär states the result (Theorem 1.5.11): a compact Lie group acting freely produces a smooth orbit space with the maximal-rank projection and the universal property. The theorem is the sharpening — noticed already by Bär's "idea of proof," which invokes compactness only to guarantee Hausdorffness and the one-to-one correspondence of nearby points with orbits — in which compactness is replaced by the exact topological hypothesis it was standing in for, namely properness.

---

# Motivation

Every construction in gauge theory that "divides out a symmetry" is an instance of this theorem. The projective space $\mathbb{CP}^{n-1}$ is $S^{2n-1}/U(1)$; a homogeneous space $G/H$ is the quotient of $G$ by the free right action of a closed subgroup $H$; the base of a principal bundle is recovered from the total space as $P/G$; an associated bundle $P \times_\varrho V$ is a quotient of $P \times V$ by a free proper action; a manifold covered by another is a quotient by a discrete group. In each case one begins with a manifold on which a group acts and wishes to know that the set of orbits is again a manifold, of the expected dimension, with the projection as smooth as possible. This theorem is the single statement that licenses all of them at once, and it isolates exactly which hypotheses on the action are needed.

The question it answers is delicate because the orbit space, taken naively, can be badly behaved. Consider the irrational line: let $\mathbb{R}$ act on the torus $T^2 = \mathbb{R}^2 / \mathbb{Z}^2$ by $t \cdot (x, y) = (x + t, y + \alpha t)$ with $\alpha$ irrational. This action is smooth and free, yet every orbit is dense, so the only open set saturated by orbits is the whole torus, and the orbit space carries the indiscrete topology: it is not Hausdorff, not a manifold, not even a decent topological space. What has gone wrong is that orbits accumulate on one another; distinct orbits cannot be separated. Properness is precisely the hypothesis that rules this out. It says, in the contrapositive, that a sequence of group elements moving a bounded set to a bounded set cannot escape to infinity in $G$, and this is what prevents orbits from spiralling arbitrarily close to each other. Freeness, meanwhile, guarantees that each orbit is a faithful copy of $G$ — an embedded submanifold diffeomorphic to $G$, of dimension exactly $k$ — so that "collapsing an orbit to a point" removes exactly $k$ dimensions, giving the dimension count $\dim(M/G) = m - k$. The theorem says these two hypotheses, free and proper, are together sufficient: nothing more is needed.

The role the theorem plays downstream is that of a **manifold factory**. One hands it a manifold with a free proper action and receives a manifold together with a submersion, a pairing that is the local model of a fibre bundle. Indeed the local sections in part (3) are the germ of local triviality: a smooth section over $W$ trivialises $\pi$ over $W$ once the group is used to spread the section across the orbit, which is how the theorem becomes, in chapter III, the statement that a principal bundle is exactly the quotient map of a free proper action. The universal property in part (4) is what makes the smooth structure *usable*: it says that to define a smooth map out of the quotient it suffices to define a smooth $G$-invariant map out of $M$, so one never has to touch the abstract orbit space directly.

We assume the reader is comfortable with smooth manifolds, the [[Def - Immersion, Submersion, and Embedding|immersion/submersion/embedding]] vocabulary, the [[Thm - The Rank Theorem|rank theorem]] and its regular-value corollary, and the basic theory of [[Def - Smooth Action of a Lie Group|smooth Lie group actions]]; the topological input (proper maps, local compactness) is recalled where it is used.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypotheses are "smooth, free, proper," but each arrives in problems disguised.

The first disguised source is **a compact group acting freely**. Compactness is a far more common and easily checked condition than properness, and it *implies* properness for any smooth action: if $K \subseteq M \times M$ is compact then $\Theta^{-1}(K)$ is a closed subset (continuity of $\Theta$) of the compact set $G \times \operatorname{pr}_2(K)$, hence compact. The bridge $B \Rightarrow A$ is "compact $\Rightarrow$ proper," and it is non-obvious only in that one must recognise that the *action* map $\Theta$, not the group multiplication, is what has to be proper. *Example problem:* the diagonal action of $U(1)$ on the odd sphere $S^{2n-1} \subseteq \mathbb{C}^n$ is free (a unit scalar fixing a nonzero vector is $1$); since $U(1)$ is compact the action is proper, so [[Ex - The Scalar Action of U(1) on Odd Spheres is Free|$S^{2n-1}/U(1)$]] is a manifold, namely $\mathbb{CP}^{n-1}$.

The second disguised source is **a closed subgroup $H$ of a Lie group $G$ acting on $G$ by right translation**. Here $M = G$ and the action is $x \cdot h = xh$. It is free (right translation has no fixed points unless $h = e$), and it is proper because $H$ is closed: if $K \subseteq G \times G$ is compact then $\Theta^{-1}(K) = \{(h, x) : (xh, x) \in K\}$ sits inside $\{(h,x) : x \in \operatorname{pr}_2 K,\ xh \in \operatorname{pr}_1 K\}$, and $h = x^{-1}(xh)$ ranges over the compact set $(\operatorname{pr}_2 K)^{-1}\cdot \operatorname{pr}_1 K$ intersected with the closed set $H$, hence over a compact set. The bridge is "$H$ closed in $G$ $\Rightarrow$ right translation of $H$ on $G$ is proper," and the theorem then yields the homogeneous space $G/H$ as a manifold — the present theorem *generalises* [[Thm - Homogeneous Space is a Smooth Manifold|the homogeneous-space theorem]], recovering it when $M = G$. *Example problem:* obtain $S^2 = SO(3)/SO(2)$ and $\mathbb{CP}^{n-1} = U(n)/(U(n-1)\times U(1))$ as smooth manifolds.

The third disguised source is **a free action whose properness is verified by a "no runaway" estimate on group elements**. Many actions are neither by compact groups nor by translation, and properness is verified directly: whenever $x_i \to x$ and $x_i \cdot g_i \to y$, the elements $g_i$ subconverge in $G$. This sequential form of properness (equivalent to it when $G$ and $M$ are metrisable, which they are here, being second countable manifolds) is often the practical route. The bridge is "sequential properness $\Rightarrow$ properness," and its subtlety is that one must produce a *limit inside $G$*, not merely a bounded sequence. *Example problem:* the deck action of the fundamental group $\pi_1(B)$ on a universal cover, or the $\mathbb{Z}^n$-action on $\mathbb{R}^n$ by translation, verified this way, gives the covering-space quotients of chapter V.

**Targets (Output Amplification).** The bare output is "a submersion onto a manifold of dimension $m - k$." Combined with further ingredients it produces the central objects of the subject.

Combine the conclusion with **a representation $\varrho : G \to GL(V)$** to build **associated bundles**. Given a free proper (principal) action of $G$ on $P$, the diagonal action on $P \times V$, $(p, v) \cdot g = (p \cdot g, \varrho(g^{-1}) v)$, is again free (it is free already in the $P$-factor) and proper (the projection $P \times V \to P$ is equivariant and proper-detecting), so the theorem makes $P \times_\varrho V := (P \times V)/G$ a smooth manifold and a vector bundle over $P/G$. The extra ingredient is the representation; the payoff is that every tensor bundle of gauge theory is manufactured this way. This is exactly the construction whose manifold structure Haydys asserts without proof (I2.2.2, I2.2.3) and which the present theorem supplies.

Combine the conclusion with **the identification of local sections as local trivialisations** to obtain **principal bundles from free proper actions**. Part (3) gives, near each orbit, a smooth section $\sigma$; the map $(w, g) \mapsto \sigma(w) \cdot g$ is then a diffeomorphism from $W \times G$ onto the saturated open set $\pi^{-1}(W)$, i.e. a local trivialisation. The extra ingredient is the group action spreading the section across the orbit; the payoff is the theorem of chapter III that a free proper action is the same data as a principal $G$-bundle.

Combine the conclusion with **the discreteness of $G$** to obtain **covering maps**. When $G$ is a discrete group acting freely and properly (equivalently, [[Def - Discrete Group and Properly Discontinuous Action|properly discontinuously]]), the submersion $\pi$ has zero-dimensional fibres and is a local diffeomorphism, and the theorem specialises to [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the covering-space quotient theorem]]. The extra ingredient is $\dim G = 0$; the payoff is $T^n = \mathbb{R}^n/\mathbb{Z}^n$, mapping tori, and the universal cover as a principal $\pi_1$-bundle.

---

# Why Is It True

Set the abstract quotient aside and picture the manifold near one orbit. The orbit $\mathcal{O} = p \cdot G$ is a $k$-dimensional copy of $G$ sitting inside $M$. Freeness is what makes it a *faithful* copy: the orbit map $g \mapsto p \cdot g$ is injective, and — being of constant rank, which any orbit map is — an injective constant-rank map is an immersion, so the orbit is an immersed $k$-manifold. Properness upgrades the immersion to an embedding, because a proper injective immersion is a closed embedding. So the orbit is a genuine embedded submanifold, and it is exactly $k$-dimensional.

Now slice across it. Choose a small piece of manifold $S$ through $p$, of the complementary dimension $m - k$, meeting the orbit transversally — so that at $p$ the tangent space splits as $T_pM = T_p\mathcal{O} \oplus T_pS$. Sweep this slice around by the group: form $\psi(g, s) = s \cdot g$. At $(e, p)$ the derivative of $\psi$ sends the $G$-directions onto $T_p\mathcal{O}$ (that is the orbit map's derivative) and the $S$-directions onto $T_pS$ (that is the identity on the slice), so it hits all of $T_pM$ and, the dimensions matching, is an isomorphism. By the inverse function theorem $\psi$ is a local diffeomorphism, and equivariance spreads this to a local diffeomorphism along the whole orbit. The one genuinely global point is **injectivity**: could two different pairs $(g, s), (g', s')$ land on the same point? If the slice is small enough, no — and this is precisely where properness and freeness are both consumed. A collision $s \cdot g = s' \cdot g'$ with $s, s'$ near $p$ forces the group element $g'g^{-1}$ carrying $s$ to $s'$ to stay bounded (properness), hence to subconverge to some $h$ with $p \cdot h = p$, hence $h = e$ (freeness); but then the collision happens where $\psi$ is already injective, a contradiction. So a small enough slice $S$ gives a "tube" $G \times S \cong \pi^{-1}(\pi(S))$ in which **each orbit meets $S$ exactly once**.

That single fact is the whole theorem.

> **The slice $S$ is a chart for the orbit space:** because each orbit crosses $S$ once, the composite $\pi|_S : S \to M/G$ is a bijection onto an open set, and it carries the smooth structure of $S$ down to $M/G$; in these charts $\pi$ becomes the projection $G \times S \to S$, manifestly a submersion, and the section $s \mapsto s$ becomes the local section of part (3).

Different slices give different charts, and their transition map sends a point of one slice to the unique point of the other in the same orbit — a smooth operation because it is read off from the tube diffeomorphisms $\psi$. The dimension is $\dim S = m - k$. Hausdorffness comes from properness in the guise of the orbit relation being *closed*: a proper map into a locally compact Hausdorff space has closed image, and closed orbit relation plus open projection is exactly the criterion for the quotient to be Hausdorff. Second countability is inherited because $\pi$ is an open map. The universal property and the uniqueness of the structure are then formal consequences of the submersion having local sections.

---

# What Makes This Hard

The one deep step is the injectivity of the tube map $\psi$ after shrinking the slice; every other step is bookkeeping. The difficulty is that injectivity is not a pointwise or infinitesimal condition — $\psi$ is already a local diffeomorphism, so *locally* injective, for free — but a global one, and it is the only place where freeness and properness are used together and essentially. The common error is to prove $\psi$ is a local diffeomorphism and stop, concluding the tube is embedded; without the properness-plus-freeness argument the "tube" can wrap around and self-intersect (exactly what happens for the dense irrational-line action, where $\psi$ is a local diffeomorphism but never injective on any $G \times S$). The second trap is to forget that properness is needed for Hausdorffness independently of the slice argument: even granting embedded orbits and local charts, two orbits can fail to be separated in the quotient unless the orbit relation is closed, and closedness is again exactly properness.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** First settle the topology of $M/G$ (open projection $\Rightarrow$ second countable; proper action $\Rightarrow$ closed orbit relation $\Rightarrow$ Hausdorff). Then, near each point $p$, build a slice $S$ transverse to the orbit and prove the tube map $\psi : G \times S \to M$, $(g,s) \mapsto s \cdot g$, is a diffeomorphism onto a saturated open set after shrinking $S$; freeness and properness enter only in the shrinking step. Read charts of $M/G$ off the slices, check the transitions and the submersion property, and derive uniqueness and the universal property from local sections.

**Subgoal decomposition.**
1. **$\pi$ is open and $M/G$ is second countable.** *Hint:* $\pi^{-1}(\pi(U)) = \bigcup_g R_g(U)$. *Why needed:* openness gives second countability directly and is used in the Hausdorff and chart arguments.
2. **The orbit relation $\mathcal{R} = \Theta(G \times M)$ is closed, hence $M/G$ is Hausdorff.** *Hint:* a proper continuous map into a locally compact Hausdorff space is closed; then separate off-diagonal pairs. *Why needed:* Hausdorffness of the quotient, part (2).
3. **Each orbit is an embedded $k$-submanifold; the orbit map is a proper injective immersion.** *Hint:* equivariance forces constant rank; freeness forces injectivity, hence (constant rank + injective) immersion; properness forces embedding. *Why needed:* fixes $\dim \mathcal{O} = k$ and supplies $T_p\mathcal{O}$ for the slice.
4. **The tube $\psi : G \times S \to M$ is a diffeomorphism onto a saturated open set, with $S$ meeting each orbit once.** *Hint:* $d\psi_{(e,p)}$ is an isomorphism (inverse function theorem, equivariance); injectivity after shrinking from properness + freeness. *Why needed:* the heart; produces charts, the submersion, and local sections.
5. **Charts, submersion, transition smoothness, local sections.** *Hint:* $\pi|_S$ is a homeomorphism onto an open set; in tube coordinates $\pi$ is the projection $G \times S \to S$. *Why needed:* the smooth structure of parts (1),(3).
6. **Uniqueness of the structure and the universal property.** *Hint:* a surjective smooth map with local sections satisfies "$F$ smooth $\iff F \circ \pi$ smooth"; apply to $\operatorname{id}$ and to $f$. *Why needed:* parts (1) uniqueness and (4).

---

# Lemma Decomposition

> [!note]- Lemma 1: A continuous proper map into a locally compact Hausdorff space is closed.
> **Statement:** Let $f : X \to Y$ be continuous with $Y$ [[Def - Locally Compact Space|locally compact]] Hausdorff, and suppose $f$ is proper ($f^{-1}(K)$ compact for every compact $K \subseteq Y$). Then $f$ is a closed map: $f(C)$ is closed in $Y$ for every closed $C \subseteq X$.
>
> **Hint:** Test closedness of $f(C)$ against a compact neighbourhood of a would-be limit point.
>
> **Why needed:** It converts properness of the action ($\Theta$ proper) into closedness of the orbit relation $\mathcal{R} = \Theta(G \times M)$ (Lemma 3), and properness of the orbit map into its being an embedding (Lemma 4).
>
> > [!note]- Full proof
> > **Goal.** Fix a closed set $C \subseteq X$; we must show $\overline{f(C)} \subseteq f(C)$.
> >
> > **Reduce to a compact neighbourhood.** Let $y \in \overline{f(C)}$. Since $Y$ is locally compact Hausdorff, choose a compact set $K \subseteq Y$ that is a neighbourhood of $y$, so $y \in \operatorname{int} K$ (this is the defining property of local compactness in the Hausdorff setting). We claim $y$ is a limit point of the smaller set $f(C) \cap K$. Let $V$ be any neighbourhood of $y$. Then $V \cap \operatorname{int} K$ is again a neighbourhood of $y$, so it meets $f(C)$ (because $y \in \overline{f(C)}$); a common point lies in $V$ and in $f(C) \cap \operatorname{int} K \subseteq f(C) \cap K$. Hence every neighbourhood of $y$ meets $f(C) \cap K$, that is, $y \in \overline{f(C) \cap K}$.
> >
> > **The set $f(C) \cap K$ is closed.** We have $f(C) \cap K = f\big(C \cap f^{-1}(K)\big)$: indeed $z \in f(C)\cap K$ iff $z \in K$ and $z = f(c)$ for some $c \in C$, and then $c \in C \cap f^{-1}(K)$; conversely the image of any $c \in C \cap f^{-1}(K)$ lies in $f(C) \cap K$. Now $f^{-1}(K)$ is compact (properness of $f$, with $K$ compact), so $C \cap f^{-1}(K)$ is a closed subset of a compact set, hence compact; its continuous image $f\big(C \cap f^{-1}(K)\big)$ is compact (continuity of $f$), and a compact subset of the Hausdorff space $Y$ is closed.
> >
> > **Conclude.** Combining the two displayed facts, $y \in \overline{f(C) \cap K} = f(C) \cap K \subseteq f(C)$ (the middle equality since $f(C)\cap K$ is closed). As $y \in \overline{f(C)}$ was arbitrary, $f(C)$ is closed. Therefore $f$ is a closed map. $\blacksquare$

> [!note]- Lemma 2: The projection $\pi$ is open, and $M/G$ is second countable.
> **Statement:** For any smooth right action, the quotient map $\pi : M \to M/G$ is an open map, and if $M$ is second countable then $M/G$ (with the quotient topology) is second countable.
>
> **Hint:** The saturation of an open set is a union of the diffeomorphic copies $R_g(U)$.
>
> **Why needed:** Openness of $\pi$ drives second countability, the Hausdorff separation (Lemma 3), and the fact that $\pi|_S$ is a homeomorphism onto an open set (Formal Proof, Step 3).
>
> > [!note]- Full proof
> > **Goal.** Show $\pi(U)$ is open for open $U \subseteq M$, then exhibit a countable basis of $M/G$.
> >
> > **$\pi$ is open.** Let $U \subseteq M$ be open. By definition of the quotient topology, $\pi(U)$ is open in $M/G$ if and only if its saturation $\pi^{-1}(\pi(U))$ is open in $M$. Now $x \in \pi^{-1}(\pi(U))$ means $x \cdot G$ meets $U$, i.e. $x \cdot g \in U$ for some $g$, i.e. $x \in U \cdot g^{-1} = R_{g^{-1}}(U)$ for some $g$; hence
> > $$\pi^{-1}(\pi(U)) = \bigcup_{g \in G} R_{g}(U) \qquad \text{(each } x \text{ lies in some } R_g(U)\text{, and conversely each } R_g(U) \subseteq \pi^{-1}(\pi(U))\text{).}$$
> > Each $R_g : M \to M$ is a diffeomorphism (with inverse $R_{g^{-1}}$), so $R_g(U)$ is open; a union of open sets is open. Thus $\pi^{-1}(\pi(U))$ is open and $\pi(U)$ is open.
> >
> > **Second countability.** Let $\mathcal{B} = \{B_i\}_{i \in \mathbb{N}}$ be a countable basis for $M$. Set $\mathcal{B}' = \{\pi(B_i)\}_{i \in \mathbb{N}}$; each $\pi(B_i)$ is open (by openness of $\pi$ just proved), and $\mathcal{B}'$ is countable. We check it is a basis. Let $W \subseteq M/G$ be open and $\pi(x) \in W$. Then $x \in \pi^{-1}(W)$, which is open in $M$, so there is $B_i$ with $x \in B_i \subseteq \pi^{-1}(W)$. Applying $\pi$ and using $\pi(\pi^{-1}(W)) = W$ (surjectivity of $\pi$), we get $\pi(x) \in \pi(B_i) \subseteq W$. Hence every open set is a union of members of $\mathcal{B}'$, so $\mathcal{B}'$ is a countable basis and $M/G$ is second countable. $\blacksquare$

> [!note]- Lemma 3: For a proper action the orbit relation is closed, and $M/G$ is Hausdorff.
> **Statement:** If the action is proper, the orbit relation $\mathcal{R} := \Theta(G \times M) = \{(x \cdot g, x) : g \in G,\ x \in M\} \subseteq M \times M$ is closed, and $M/G$ is Hausdorff.
>
> **Hint:** $\mathcal{R}$ is the image of the proper map $\Theta$; then separate a non-related pair by a rectangle and push it down.
>
> **Why needed:** This is part (2), Hausdorffness, and the only proof of it uses properness rather than the slice.
>
> > [!note]- Full proof
> > **Goal.** Show $\mathcal{R}$ is closed, then separate distinct orbits in the quotient.
> >
> > **The orbit relation equals $\Theta(G \times M)$ and is closed.** By definition $\Theta(g, x) = (x \cdot g, x)$, so $\Theta(G \times M) = \{(x \cdot g, x)\}$ consists of all pairs whose two entries lie in a common orbit; this is the full same-orbit relation $\mathcal{R}$ (given any $a, b$ in one orbit, write $a = b \cdot g$, then $(a,b) = \Theta(g, b)$). The target $M \times M$ is a smooth manifold, hence locally compact and Hausdorff. The action is proper, meaning $\Theta$ is a proper map; by **Lemma 1** (proper continuous map into a locally compact Hausdorff space is closed), $\Theta$ is a closed map, so its image $\mathcal{R} = \Theta(G \times M)$ of the closed set $G \times M$ is closed in $M \times M$.
> >
> > **Separate distinct orbits.** Let $\pi(x) \neq \pi(y)$, so $x$ and $y$ lie in different orbits and $(x, y) \notin \mathcal{R}$. Since $\mathcal{R}$ is closed, its complement is open and contains $(x, y)$, so there are open sets $U \ni x$ and $V \ni y$ with $(U \times V) \cap \mathcal{R} = \varnothing$. The images $\pi(U)$ and $\pi(V)$ are open (by **Lemma 2**, $\pi$ is open) and contain $\pi(x), \pi(y)$ respectively. They are disjoint: if some $z \in \pi(U) \cap \pi(V)$, then $z = \pi(u) = \pi(v)$ for $u \in U$, $v \in V$, whence $u, v$ share an orbit and $(u, v) \in \mathcal{R} \cap (U \times V)$, contradicting the choice of $U, V$. Thus $\pi(x)$ and $\pi(y)$ have disjoint open neighbourhoods, so $M/G$ is Hausdorff. $\blacksquare$

> [!note]- Lemma 4: Each orbit is an embedded $k$-submanifold; the orbit map is a proper injective immersion.
> **Statement:** Let the action be free and proper and let $p \in M$. The orbit map $\theta^{(p)} : G \to M$, $\theta^{(p)}(g) = p \cdot g$, has **constant rank**, is **injective**, and is a **proper** map; consequently it is a smooth embedding, and the orbit $\mathcal{O}_p = p \cdot G$ is a properly embedded submanifold of $M$ of dimension $k = \dim G$, with $T_p\mathcal{O}_p = \operatorname{im}\big(d_e\theta^{(p)}\big)$.
>
> **Hint:** Differentiate the equivariance $\theta^{(p)} \circ R_a = R_a \circ \theta^{(p)}$ for constant rank; free $\Rightarrow$ injective; injective + constant rank $\Rightarrow$ immersion; proper injective immersion $\Rightarrow$ embedding.
>
> **Why needed:** It fixes the orbit dimension at $k$ (hence $\dim M/G = m-k$) and provides the tangent line $T_p\mathcal{O}_p$ transverse to which the slice is built (Lemma 5).
>
> > [!note]- Full proof
> > **Goal.** Establish constant rank, injectivity, and properness of $\theta^{(p)}$, then assemble the embedding.
> >
> > **Constant rank (equivariant rank theorem).** Let $G$ act on itself by right translation $R_a^G : g \mapsto ga$; this action is transitive. The orbit map is equivariant for this action on the source and the given action on the target: $\theta^{(p)}(R_a^G g) = p \cdot (ga) = (p \cdot g)\cdot a = R_a\big(\theta^{(p)}(g)\big)$, i.e. $\theta^{(p)} \circ R_a^G = R_a \circ \theta^{(p)}$. Differentiating at $g$ and using that $R_a^G$ and $R_a$ are diffeomorphisms (so their differentials are isomorphisms),
> > $$d\theta^{(p)}_{ga} \circ d(R_a^G)_g = d(R_a)_{p\cdot g} \circ d\theta^{(p)}_g \qquad \text{(chain rule on } \theta^{(p)} \circ R_a^G = R_a \circ \theta^{(p)}\text{)},$$
> > whence $\operatorname{rank} d\theta^{(p)}_{ga} = \operatorname{rank} d\theta^{(p)}_g$ for all $g$ (composing with isomorphisms preserves rank). Since right translation is transitive on $G$, every point $g$ is $R_a^G(e)$ for a suitable $a$, so the rank is the constant $r := \operatorname{rank} d\theta^{(p)}_e$. This is the [[Def - Equivariant Map|equivariant rank theorem]] specialised to the orbit map.
> >
> > **Injectivity (freeness).** Suppose $\theta^{(p)}(g) = \theta^{(p)}(g')$, i.e. $p \cdot g = p \cdot g'$. Apply $R_{(g')^{-1}}$: $(p\cdot g)\cdot (g')^{-1} = p \cdot (g (g')^{-1})$ and $(p \cdot g')\cdot (g')^{-1} = p$, so $p \cdot (g (g')^{-1}) = p$. By **freeness**, $g(g')^{-1} = e$, hence $g = g'$. Thus $\theta^{(p)}$ is injective.
> >
> > **Injective + constant rank $\Rightarrow$ immersion.** By the [[Thm - The Rank Theorem|rank theorem]] — a map of constant rank $r$ near a point admits charts in which it reads $(x^1,\dots,x^k) \mapsto (x^1,\dots,x^r,0,\dots,0)$ — if $r < k$ then in such a chart $\theta^{(p)}$ is independent of the coordinates $x^{r+1},\dots,x^k$ and therefore not injective on any neighbourhood, contradicting injectivity. Hence $r = k$: $d\theta^{(p)}_g$ is injective for every $g$, so $\theta^{(p)}$ is an immersion, and $\operatorname{im}\big(d_e\theta^{(p)}\big)$ is $k$-dimensional.
> >
> > **Properness of the orbit map (properness of the action).** Let $K \subseteq M$ be compact. Then
> > $$\big(\theta^{(p)}\big)^{-1}(K) \times \{p\} = \Theta^{-1}\big(K \times \{p\}\big) \cap \big(G \times \{p\}\big) \qquad \text{(since } \Theta(g,p) = (p\cdot g, p) \in K \times \{p\} \iff p\cdot g \in K\text{)}.$$
> > Here $K \times \{p\}$ is compact, so $\Theta^{-1}(K \times \{p\})$ is compact (**properness** of $\Theta$); intersecting with the closed set $G \times \{p\}$ keeps it compact; projecting to the first factor (a continuous map) shows $\big(\theta^{(p)}\big)^{-1}(K)$ is compact. Thus $\theta^{(p)}$ is proper.
> >
> > **Proper injective immersion $\Rightarrow$ embedding.** As a proper continuous map into the locally compact Hausdorff space $M$, $\theta^{(p)}$ is closed (**Lemma 1**); a closed injective continuous map is a homeomorphism onto its image (it is a continuous bijection onto $\operatorname{im}\theta^{(p)}$ that carries closed sets to closed sets, hence has continuous inverse). A topological embedding that is also an immersion is a smooth embedding. Therefore $\mathcal{O}_p = \theta^{(p)}(G)$ is an embedded submanifold, diffeomorphic to $G$, of dimension $k$, and its tangent space at $p = \theta^{(p)}(e)$ is $T_p\mathcal{O}_p = \operatorname{im}\big(d_e\theta^{(p)}\big)$. Properness of $\theta^{(p)}$ makes the embedding proper (closed). $\blacksquare$

> [!note]- Lemma 5: The tube map is a diffeomorphism onto a saturated open set.
> **Statement:** Let the action be free and proper, $p \in M$, and let $\mathcal{O}_p$ be the orbit through $p$ (Lemma 4). There is an embedded submanifold $S \ni p$ of dimension $m - k$ with $T_pM = T_p\mathcal{O}_p \oplus T_pS$ such that the **tube map**
> $$\psi : G \times S \longrightarrow M, \qquad \psi(g, s) = s \cdot g,$$
> is a diffeomorphism onto the open $G$-saturated set $U := \psi(G \times S) = S \cdot G = \pi^{-1}(\pi(S))$, and $S$ meets each orbit contained in $U$ in exactly one point.
>
> **Hint:** Build $S$ as a regular level set transverse to $\mathcal{O}_p$; $d\psi_{(e,p)}$ is an isomorphism, so $\psi$ is a local diffeomorphism along $G \times \{p\}$; shrink $S$ to force global injectivity using properness and freeness.
>
> **Why needed:** This is the crux; it produces the charts, the submersion property, and the local sections all at once.
>
> > [!note]- Full proof
> > **Goal.** Construct $S$; show $\psi$ is a local diffeomorphism near $G \times \{p\}$; shrink $S$ so $\psi$ is injective; conclude it is a diffeomorphism onto an open saturated set meeting each orbit once.
> >
> > **Step A — a transverse slice as a regular level set.** By Lemma 4, $T_p\mathcal{O}_p \subseteq T_pM$ is a $k$-dimensional subspace. Choose a smooth chart $(V, \varphi)$ centred at $p$, $\varphi : V \to \mathbb{R}^m$, $\varphi(p) = 0$; precomposing $\varphi$ with a linear isomorphism of $\mathbb{R}^m$ we may arrange $d\varphi_p(T_p\mathcal{O}_p) = \mathbb{R}^k \times \{0\}$. Let $\rho := \operatorname{pr}_{\mathbb{R}^k} \circ \varphi : V \to \mathbb{R}^k$, a submersion (its differential $\operatorname{pr}_{\mathbb{R}^k}\circ d\varphi$ is surjective everywhere), so $0$ is a regular value. By the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] — the preimage of a regular value of a smooth map is an embedded submanifold whose tangent space is the kernel of the differential — the set
> > $$S_0 := \rho^{-1}(0) = \varphi^{-1}\big(\{0\} \times \mathbb{R}^{m-k}\big) \cap V$$
> > is an embedded submanifold through $p$ of dimension $m - k$, with $T_pS_0 = \ker d\rho_p = d\varphi_p^{-1}\big(\{0\}\times \mathbb{R}^{m-k}\big)$. Since $d\varphi_p(T_p\mathcal{O}_p) = \mathbb{R}^k \times \{0\}$ and $d\varphi_p(T_pS_0) = \{0\}\times\mathbb{R}^{m-k}$ are complementary in $\mathbb{R}^m$ and $d\varphi_p$ is an isomorphism, $T_pM = T_p\mathcal{O}_p \oplus T_pS_0$.
> >
> > **Step B — $\psi$ is a local diffeomorphism along $G \times \{p\}$.** Consider $\psi_0 : G \times S_0 \to M$, $\psi_0(g,s) = s \cdot g$; it is smooth (restriction of $\mu$). Compute $d(\psi_0)_{(e,p)}$ on the splitting $T_{(e,p)}(G\times S_0) = T_eG \oplus T_pS_0$. Restricting to $T_eG$ (with $s = p$ fixed), $\psi_0(g, p) = p \cdot g = \theta^{(p)}(g)$, so $d(\psi_0)_{(e,p)}(\xi, 0) = d_e\theta^{(p)}(\xi) \in T_p\mathcal{O}_p$; and restricting to $T_pS_0$ (with $g = e$ fixed), $\psi_0(e, s) = s$, so $d(\psi_0)_{(e,p)}(0, w) = w \in T_pS_0$. Hence the image of $d(\psi_0)_{(e,p)}$ is $T_p\mathcal{O}_p + T_pS_0 = T_pM$ (Step A), and since $\dim(T_eG \oplus T_pS_0) = k + (m-k) = m = \dim M$, the differential $d(\psi_0)_{(e,p)}$ is an isomorphism. By the [[Thm - The Inverse Function Theorem|inverse function theorem]] — a smooth map whose differential at a point is invertible restricts to a diffeomorphism of a neighbourhood — $\psi_0$ is a diffeomorphism from a neighbourhood of $(e, p)$ onto a neighbourhood of $p$. For arbitrary $g_0 \in G$, right translation gives $\psi_0(g g_0, s) = s \cdot (g g_0) = (s \cdot g)\cdot g_0 = R_{g_0}\big(\psi_0(g, s)\big)$, i.e. $\psi_0 \circ (m_{g_0} \times \operatorname{id}) = R_{g_0} \circ \psi_0$ where $m_{g_0}(g) = g g_0$; as $m_{g_0}\times\operatorname{id}$ and $R_{g_0}$ are diffeomorphisms and $\psi_0$ is a local diffeomorphism at $(e,p)$, it is a local diffeomorphism at $(g_0, p)$ for every $g_0$. Thus $\psi_0$ is a local diffeomorphism at every point of $G \times \{p\}$.
> >
> > **Step C — injectivity after shrinking (freeness and properness).** We claim there is an open neighbourhood $S \subseteq S_0$ of $p$ such that $\psi := \psi_0|_{G \times S}$ is injective. Suppose not. Then for every member of a countable neighbourhood basis $S_0 \supseteq W_1 \supseteq W_2 \supseteq \cdots \downarrow \{p\}$ the restriction $\psi_0|_{G \times W_i}$ fails to be injective, giving distinct pairs $(g_i, s_i) \neq (g_i', s_i')$ in $G \times W_i$ with $s_i \cdot g_i = s_i' \cdot g_i'$; note $s_i, s_i' \to p$. Put $h_i := g_i (g_i')^{-1}$, so that applying $R_{(g_i')^{-1}}$ to $s_i \cdot g_i = s_i' \cdot g_i'$ gives $s_i \cdot h_i = s_i'$, equivalently $s_i = s_i' \cdot h_i^{-1}$. Now
> > $$\Theta(h_i, s_i) = (s_i \cdot h_i,\ s_i) = (s_i',\ s_i) \longrightarrow (p, p) \qquad \text{(since } s_i, s_i' \to p\text{),}$$
> > so, choosing a compact neighbourhood $L$ of $(p,p)$ in $M \times M$ (available since $M \times M$ is locally compact), the tail of $\{(h_i, s_i)\}$ lies in $\Theta^{-1}(L)$; by **properness** $\Theta^{-1}(L)$ is compact, and a compact subset of the second-countable, hence metrisable, manifold $G \times M$ is sequentially compact, so after passing to a subsequence $h_i \to h \in G$ and $s_i \to s_\ast \in M$, where $s_\ast = p$ since $s_i \to p$ already. Then $s_i' = s_i \cdot h_i \to p \cdot h$, while also $s_i' \to p$, so $p \cdot h = p$; by **freeness** $h = e$, hence $h_i \to e$. Consider the two pairs $(e, s_i)$ and $(h_i^{-1}, s_i')$ in $G \times S_0$: from $s_i = s_i' \cdot h_i^{-1}$ we get $\psi_0(e, s_i) = s_i = \psi_0(h_i^{-1}, s_i')$. Both pairs converge to $(e, p)$ (because $h_i \to e$ and $s_i, s_i' \to p$), where $\psi_0$ is injective on a neighbourhood (Step B). For $i$ large both pairs lie in that neighbourhood, forcing $(e, s_i) = (h_i^{-1}, s_i')$, i.e. $h_i = e$ and $s_i = s_i'$. Then $s_i \cdot g_i = s_i' \cdot g_i' = s_i \cdot g_i'$, and applying $R_{(g_i')^{-1}}$ with **freeness** gives $g_i = g_i'$. Hence $(g_i, s_i) = (g_i', s_i')$, contradicting their distinctness. Therefore some $S := W_i$ works: $\psi = \psi_0|_{G\times S}$ is injective.
> >
> > **Step D — diffeomorphism onto an open saturated set.** The map $\psi : G \times S \to M$ is a local diffeomorphism (Step B restricts to the open set $G \times S$) and injective (Step C), hence a diffeomorphism onto its image $U := \psi(G \times S)$, which is open because a local diffeomorphism is an open map. Moreover $U = \{s \cdot g : s \in S,\ g \in G\} = S \cdot G$ is a union of orbits, so it is $G$-saturated: $U = \pi^{-1}(\pi(S))$. Finally $S$ meets each orbit in $U$ exactly once: if $s, s' \in S$ lie in one orbit, say $s' = s \cdot g$, then $\psi(g, s) = s \cdot g = s' = \psi(e, s')$, and injectivity forces $(g, s) = (e, s')$, so $g = e$ and $s = s'$. $\blacksquare$

> [!note]- Lemma 6: A surjective smooth map with local sections satisfies the smooth characteristic property.
> **Statement:** Let $\pi : M \to Q$ be a surjective smooth map between manifolds such that every point of $Q$ lies in the image of a smooth local section (a smooth $\sigma : W \to M$ with $\pi \circ \sigma = \operatorname{id}_W$, $W$ open). Then for any smooth manifold $N$ and any map $F : Q \to N$, $F$ is smooth if and only if $F \circ \pi$ is smooth.
>
> **Hint:** For "if," write $F = (F\circ\pi)\circ\sigma$ locally.
>
> **Why needed:** It yields the uniqueness of the smooth structure and the smoothness of the induced map in the universal property.
>
> > [!note]- Full proof
> > **Goal.** Prove both implications.
> >
> > **($\Rightarrow$).** If $F$ is smooth then $F \circ \pi$ is a composition of smooth maps, hence smooth.
> >
> > **($\Leftarrow$).** Assume $F \circ \pi$ is smooth. Fix $q \in Q$ and choose a smooth local section $\sigma : W \to M$ with $q \in W$ and $\pi \circ \sigma = \operatorname{id}_W$. Then on $W$,
> > $$F|_W = F \circ \operatorname{id}_W = F \circ (\pi \circ \sigma) = (F \circ \pi) \circ \sigma \qquad \text{(associativity; } \pi\circ\sigma = \operatorname{id}_W\text{),}$$
> > a composition of the smooth maps $\sigma$ and $F \circ \pi$, hence smooth on $W$. As $q$ was arbitrary and smoothness is local, $F$ is smooth on $Q$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the theorem for a right action; the left-action case is handled at the end. Write $k = \dim G$, $m = \dim M$.
>
> **Step 0 — the orbit space is a second-countable Hausdorff space.** By **Lemma 2**, $\pi : M \to M/G$ is an open map and $M/G$ is second countable. By **Lemma 3** (which uses properness through **Lemma 1**), the orbit relation $\mathcal{R} = \Theta(G\times M)$ is closed in $M \times M$ and $M/G$ is Hausdorff. These are the point-set preconditions a manifold structure requires, and they establish part (2) of the statement independently of the charts constructed below.
>
> **Step 1 — orbits are embedded $k$-submanifolds.** Fix $p \in M$. By **Lemma 4** (freeness and properness), the orbit map $\theta^{(p)}$ is a proper injective immersion, so the orbit $\mathcal{O}_p = p\cdot G$ is a properly embedded submanifold of dimension $k$ with $T_p\mathcal{O}_p = \operatorname{im}(d_e\theta^{(p)})$. This fixes the codimension of orbits at $m - k$, the eventual dimension of the quotient.
>
> **Step 2 — the tube.** By **Lemma 5**, there is an embedded slice $S \ni p$ of dimension $m - k$ with $T_pM = T_p\mathcal{O}_p \oplus T_pS$, for which the tube map $\psi_S : G \times S \to M$, $(g,s)\mapsto s\cdot g$, is a diffeomorphism onto an open $G$-saturated set $U_S = \pi^{-1}(\pi(S))$, and $S$ meets each orbit in $U_S$ exactly once.
>
> **Step 3 — charts, the submersion property, and local sections.** For the slice $S$ of Step 2, consider the restricted projection $\pi|_S : S \to M/G$.
>
> *It is a homeomorphism onto the open set $\pi(S) = \pi(U_S)$.* It is injective because $S$ meets each orbit in $U_S$ at most once (Lemma 5). It is surjective onto $\pi(U_S)$ because every orbit in $U_S$ meets $S$. It is continuous (restriction of the continuous $\pi$). It is open as a map $S \to \pi(S)$: for open $V \subseteq S$, the saturation $\pi^{-1}(\pi(V)) = V \cdot G = \psi_S(G \times V)$ is open (image of an open set under the diffeomorphism $\psi_S$), so $\pi(V)$ is open in $M/G$ by the quotient topology, and $\pi(S) = \pi(U_S)$ is open by **Lemma 2**. A continuous open bijection is a homeomorphism.
>
> *Charts.* Let $\phi_S : S \to \mathbb{R}^{m-k}$ be a smooth chart of the $(m-k)$-manifold $S$. Define
> $$\eta_S := \phi_S \circ (\pi|_S)^{-1} : \pi(U_S) \longrightarrow \mathbb{R}^{m-k},$$
> a homeomorphism onto an open subset of $\mathbb{R}^{m-k}$ (composition of the homeomorphism $(\pi|_S)^{-1}$ and the chart $\phi_S$). As $p$ ranges over $M$ the sets $\pi(U_S)$ cover $M/G$, so $\{(\pi(U_S), \eta_S)\}$ is an atlas of charts of dimension $m - k$.
>
> *Smooth transitions.* Let $S = S_\alpha$ and $S' = S_\beta$ be two slices with $\pi(U_{S_\alpha}) \cap \pi(U_{S_\beta}) \neq \varnothing$, and abbreviate $\psi_\alpha = \psi_{S_\alpha}$, $\psi_\beta = \psi_{S_\beta}$. On the overlap, the transition of the underlying slice maps is $\tau := (\pi|_{S_\beta})^{-1} \circ (\pi|_{S_\alpha})$, defined on the open set $\pi|_{S_\alpha}^{-1}(\pi(U_{S_\alpha})\cap\pi(U_{S_\beta})) \subseteq S_\alpha$. For such $s \in S_\alpha$, $\tau(s)$ is the unique point of $S_\beta$ in the orbit of $s$; here $s \in U_{S_\beta}$, because $\pi(s) \in \pi(U_{S_\beta})$ forces the whole orbit of $s$ into the $G$-saturated set $U_{S_\beta}$ (Lemma 5) and in particular $s$ itself, so we may write $s = \psi_\beta(g, s_\beta)$ with $(g, s_\beta) = \psi_\beta^{-1}(s)$, and then $s_\beta = s \cdot g^{-1}$ lies in $S_\beta$ and in the orbit of $s$, so $\tau(s) = s_\beta = \operatorname{pr}_2\big(\psi_\beta^{-1}(s)\big)$. Thus $\tau = \operatorname{pr}_2 \circ \psi_\beta^{-1} \circ \iota_{S_\alpha}$ is a composition of the smooth maps $\iota_{S_\alpha}$ (inclusion $S_\alpha \hookrightarrow M$), $\psi_\beta^{-1}$ (a diffeomorphism), and $\operatorname{pr}_2$, hence smooth. The inverse map $\tau^{-1} = (\pi|_{S_\alpha})^{-1} \circ (\pi|_{S_\beta})$ is the same construction with the two slices exchanged, that is $\tau^{-1} = \operatorname{pr}_2 \circ \psi_\alpha^{-1} \circ \iota_{S_\beta}$, and every step of the previous sentence survives the exchange $\alpha \leftrightarrow \beta$ (the roles of $S_\alpha$ and $S_\beta$ are symmetric), so $\tau^{-1}$ is smooth as well and $\tau$ is a diffeomorphism. Therefore the chart transition $\eta_{S_\beta} \circ \eta_{S_\alpha}^{-1} = \phi_{S_\beta} \circ \tau \circ \phi_{S_\alpha}^{-1}$ and its inverse $\eta_{S_\alpha} \circ \eta_{S_\beta}^{-1} = \phi_{S_\alpha} \circ \tau^{-1} \circ \phi_{S_\beta}^{-1}$ are both smooth. The atlas is smooth, and it induces the quotient topology (its charts are homeomorphisms onto opens of the quotient topology, by the previous paragraph). Together with Step 0, $M/G$ is a smooth manifold of dimension $m - k$ that is Hausdorff and second countable.
>
> *$\pi$ is a submersion.* Fix $x \in M$, let $S$ be a slice with $x \in U_S$, and use $\psi_S^{-1} : U_S \to G \times S$ followed by product charts of $G$ and of $S$ as a chart of $M$ near $x$; use $\eta_S$ as the chart of $M/G$ near $\pi(x)$. For $y = \psi_S(g, s) \in U_S$ we have $\pi(y) = \pi(s \cdot g) = \pi(s) = (\pi|_S)(s)$, so in these coordinates $\pi$ reads as the projection $(g\text{-coordinates}, s\text{-coordinates}) \mapsto s\text{-coordinates}$, i.e. $\phi_S(s)$. This projection has surjective differential everywhere, so $\pi$ is a smooth submersion; in particular $\pi$ is smooth and of maximal rank $m - k$ at every point, which is part (1)'s regularity claim and Bär's condition (i).
>
> *Local sections (part 3).* For each slice $S$ define $\sigma_S := \iota_S \circ (\pi|_S)^{-1} : \pi(U_S) \to M$, the composition of the smooth inclusion $\iota_S : S \hookrightarrow M$ with the smooth (chart-smooth) inverse $(\pi|_S)^{-1}$. Then $\pi \circ \sigma_S = \pi \circ \iota_S \circ (\pi|_S)^{-1} = (\pi|_S) \circ (\pi|_S)^{-1} = \operatorname{id}$ on $\pi(U_S)$. Since the sets $\pi(U_S)$ cover $M/G$, every point has a neighbourhood over which $\pi$ has a smooth local section.
>
> **Step 4 — uniqueness of the structure and the universal property.**
>
> *Uniqueness (part 1).* Suppose $Q_1$ and $Q_2$ denote the topological space $M/G$ equipped with two smooth structures, each making $\pi$ a smooth submersion. A submersion admits smooth local sections through every point of its image (this is exactly what Step 3 constructed, and it holds for any submersion by the submersion form of the [[Thm - The Rank Theorem|rank theorem]]); so $\pi : M \to Q_1$ meets the hypothesis of **Lemma 6**. The identity map $\operatorname{id} : Q_1 \to Q_2$ satisfies $\operatorname{id} \circ \pi = \pi : M \to Q_2$, which is smooth; by **Lemma 6** (with $F = \operatorname{id}$, $N = Q_2$), $\operatorname{id} : Q_1 \to Q_2$ is smooth. By symmetry $\operatorname{id} : Q_2 \to Q_1$ is smooth. Hence $\operatorname{id}$ is a diffeomorphism $Q_1 \cong Q_2$, so the two smooth structures coincide: the structure making $\pi$ a smooth submersion is unique.
>
> *Universal property (part 4).* Let $N$ be a smooth manifold and $f : M \to N$ a smooth map constant on the orbits of $G$, i.e. $f(x \cdot g) = f(x)$ for all $x, g$. By the topological [[Thm - Universal Property of the Quotient|universal property of the quotient]] — for a quotient map $\pi : M \to M/G$ and a continuous $f$ that is constant on the fibres of $\pi$ there is a unique continuous $\tilde f : M/G \to N$ with $\tilde f \circ \pi = f$ — such a unique continuous $\tilde f$ exists (the fibres of $\pi$ are exactly the orbits). It remains to see $\tilde f$ is smooth. But $\tilde f \circ \pi = f$ is smooth, and $\pi$ is a surjective submersion with local sections (Step 3), so by **Lemma 6** (with $F = \tilde f$) $\tilde f$ is smooth. Uniqueness among *smooth* maps is inherited from uniqueness among continuous maps. This is part (4).
>
> **The compact corollary.** Suppose $G$ is compact and the smooth action is free; we show it is proper, so the theorem applies. Let $K \subseteq M \times M$ be compact. Then $\Theta^{-1}(K)$ is closed in $G \times M$ (continuity of $\Theta$) and contained in $G \times \operatorname{pr}_2(K)$: indeed $(g, x) \in \Theta^{-1}(K)$ gives $(x\cdot g, x) \in K$, so $x \in \operatorname{pr}_2(K)$. The set $G \times \operatorname{pr}_2(K)$ is compact (a product of the compact $G$ and the compact continuous image $\operatorname{pr}_2(K)$), and a closed subset of a compact set is compact, so $\Theta^{-1}(K)$ is compact. Hence $\Theta$ is proper, the action is proper, and all four conclusions hold; this is Bär's Theorem 1.5.11.
>
> **The left-action case.** Suppose instead $G$ acts on the left, $g \cdot x$, freely and properly (properness now meaning $(g,x) \mapsto (g\cdot x, x)$ is proper), with orbit space $G\backslash M$. The map $\Phi : G \times M \to G \times M$, $(g, x)\mapsto (g^{-1}, x)$, is a diffeomorphism, and under the [[Def - Free, Transitive, Effective, and Proper Group Actions|left–right dictionary]] $x * g := g^{-1} \cdot x$ the left action becomes a right action with the same orbits ($x * G = G \cdot x$), hence the same orbit space $G\backslash M = M / {*}$ as a set and topological space. Freeness is preserved ($x * g = x \iff g^{-1}\cdot x = x \iff g = e$). Properness is preserved as well: writing $\Theta_L(g,x) = (g\cdot x,\, x)$ for the left action's properness map (assumed proper by hypothesis) and $\Theta_*(g,x) = (x * g,\, x) = (g^{-1}\cdot x,\, x)$ for the right action's, the two are related by $\Theta_* = \Theta_L \circ \Phi$ (since $\Theta_L(\Phi(g,x)) = \Theta_L(g^{-1}, x) = (g^{-1}\cdot x,\, x) = \Theta_*(g,x)$), so for compact $K \subseteq M \times M$ we have $\Theta_*^{-1}(K) = \Phi^{-1}\big(\Theta_L^{-1}(K)\big)$, which is compact because $\Theta_L^{-1}(K)$ is compact (properness of $\Theta_L$) and $\Phi$ is a diffeomorphism. Hence $\Theta_*$ is proper, so the right action $*$ is free and proper. Every step above therefore applies verbatim to the right action $*$, and the resulting smooth structure, submersion, sections, and universal property are those of $G\backslash M$. Thus the theorem holds for actions on either side. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Complex projective space (application B-E1.5.7).** The diagonal action of $U(1)$ on $S^{2n-1} \subseteq \mathbb{C}^n$ by $z \cdot \lambda = \lambda z$ is free (a unit scalar fixing a nonzero vector is $1$) and, $U(1)$ being compact, proper by the corollary. The theorem makes $\mathbb{CP}^{n-1} = S^{2n-1}/U(1)$ a smooth manifold of real dimension $(2n-1) - 1 = 2(n-1)$ with the Hopf projection a submersion. The exercise is non-obvious because the manifold structure of projective space is usually *postulated* via homogeneous coordinate charts; here it is *derived*, and the two structures must then be checked to agree — a good test of the universal property, since the coordinate charts define smooth maps constant on orbits. See [[Def - Complex Projective Space as a Quotient]] and [[Ex - The Scalar Action of U(1) on Odd Spheres is Free]].

**Homogeneous spaces of Lie groups.** Let $H$ be a closed subgroup of a Lie group $G$, acting on $G$ by right translation $x \cdot h = xh$. This action is free and proper (properness from $H$ closed, as in the second disguised source), so $G/H$ is a smooth manifold of dimension $\dim G - \dim H$ and $G \to G/H$ a submersion. The theorem applies with $M = G$, and the exercise is to recover the classical examples $S^n = SO(n+1)/SO(n)$, $\mathbb{CP}^{n-1} = U(n)/(U(n-1)\times U(1))$, and the Grassmannians. It is non-obvious that the general slice construction reproduces the concrete coset charts one writes by hand; the present theorem *is* the general form of [[Thm - Homogeneous Space is a Smooth Manifold|the homogeneous-space theorem]].

**Statistical manifolds and quotients by scaling.** In information geometry the space of strictly positive measures on a finite set is acted on freely and properly by the scaling group $\mathbb{R}_{>0}$, and the quotient is the probability simplex; more generally a free proper $\mathbb{R}_{>0}$- or $\mathbb{R}^k$-action removes a scale or gauge redundancy. The theorem applies because the acting group, though noncompact, acts properly (a scaling estimate). The exercise is to identify when a redundancy in a parametrised statistical model is a free proper group action, so that the reduced model is again a smooth manifold — a recurring move in the geometry of exponential families, where the non-obviousness is precisely the verification of properness for a noncompact group.

---

# Bridges

**From free proper actions to principal bundles.** A principal $G$-bundle is, by the definition used in chapter III, a smooth free action of $G$ on a manifold $P$ that is *locally trivial*: near each base point $P$ looks like $W \times G$ with $G$ acting on the second factor. The present theorem builds the bridge in one direction: a **free and proper** action produces the base $B = P/G$, the submersion $\pi : P \to B$, and — via the local sections of part (3) — the local trivialisations $W \times G \to \pi^{-1}(W)$, $(w, g) \mapsto \sigma(w)\cdot g$, which are diffeomorphisms because $\psi$ is. Thus a free proper action is already a principal bundle, and the properness hypothesis is exactly the input that turns "free action" into "bundle." Chapter III completes the bridge, showing conversely that a principal bundle's total space carries a free proper action.

**From principal bundles to associated bundles.** Given a principal $G$-bundle $P$ (a free proper action) and a representation $\varrho : G \to GL(V)$, the diagonal action on $P \times V$, $(p,v)\cdot g = (p\cdot g,\ \varrho(g^{-1})v)$, is free (its $P$-component is free) and proper: if $K \subseteq (P\times V)^2$ is compact then a colliding sequence projects to a colliding sequence in $P$, where properness of the $P$-action bounds the group elements. The theorem then makes $P \times_\varrho V = (P\times V)/G$ a smooth manifold and, fibrewise, a vector bundle over $B = P/G$. This is the construction Haydys performs (D2.2.8) and whose smoothness he asserts as "properly discontinuous"; the correct justification is the present theorem with the hypothesis "free and proper," recorded in the convention callout above. The insight items B-I2.2.2 ("quotients $(P\times H)/G$ are manifolds also for noncompact $G$") and B-I2.2.3 ("smoothness by the general theory of group actions"), together with A-I2.2.2, are all instances of this bridge.

**From positive-dimensional groups to discrete groups.** Specialising to $\dim G = 0$ — a [[Def - Discrete Group and Properly Discontinuous Action|discrete group]] $\Gamma$ acting freely and properly — the orbits are $0$-dimensional, the submersion $\pi$ is a local diffeomorphism, and the tube $\Gamma \times S \cong \pi^{-1}(\pi(S))$ becomes a disjoint union of copies of $S$, i.e. an evenly-covered neighbourhood. The theorem thereby specialises to [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the covering-space quotient theorem]], the bridge being that "properly discontinuous" for discrete groups is exactly "free and proper." This connects the present chapter to covering-space theory (chapter V) and gives $T^n = \mathbb{R}^n/\mathbb{Z}^n$ and mapping tori as immediate corollaries.

---

# Unlocked by This

> [!tip] Concept: The base of a principal bundle *(from fibre-bundle theory)*
> With the quotient manifold theorem in hand, chapter III can define a principal $G$-bundle as a free proper action and *recover* its base as $P/G$, rather than positing the base and the projection separately. The local sections proved here are the local trivialisations there.

> [!tip] Concept: Symplectic and other quotients *(from geometric mechanics)*
> The Marsden–Weinstein symplectic quotient $\mu^{-1}(0)/G$, the reduction of a phase space by a symmetry group, is a two-step application: first the regular value theorem makes $\mu^{-1}(0)$ a submanifold, then the present theorem — freeness and properness of the induced $G$-action on the level set — makes the reduced space a manifold. The pattern "cut down to a level set, then quotient by a free proper action" is the standard route to reduced spaces throughout gauge theory, where the moduli spaces of chapters X–XI are built exactly this way.

> [!tip] Concept: Moduli spaces as quotients by the gauge group *(from gauge theory)*
> The configuration spaces of connections modulo gauge, $\mathcal{A}/\mathcal{G}$, are infinite-dimensional analogues; the finite-dimensional prototype is this theorem, and the recurring technical labour in later chapters — establishing that the gauge action on irreducible connections is free and proper — is precisely the hypothesis-checking this theorem demands.
