---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Covering Space"
  - "Def - Universal Cover"
  - "Def - Deck Transformation Group"
  - "Def - Simply Connected Space"
  - "Thm - Path Lifting and Homotopy Lifting"
  - "Thm - Lifting Criterion for Continuous Maps"
  - "Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map"
  - "Def - Discrete Group and Properly Discontinuous Action"
  - "Def - Principal G-Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold — smooth, Hausdorff, and second countable, as always in this series — and we assume in addition that $M$ is **connected**. Since a connected manifold is locally path-connected, connectedness and path-connectedness coincide for it, and we use "connected" freely. We fix once and for all a base point $m \in M$.

By a **path** in $M$ we mean a continuous map $\gamma \colon [0,1] \to M$; it runs *from* $\gamma(0)$ *to* $\gamma(1)$. For a path $\gamma$ we write $\bar\gamma$ for its reverse, $\bar\gamma(t) = \gamma(1-t)$, and $c_x$ for the constant path at a point $x$, $c_x(t) = x$. Given paths $\gamma, \eta$ with $\gamma(1) = \eta(0)$ their [[Def - Path-Product and the Fundamental Group|concatenation]] is
$$\gamma \cdot \eta \,(t) = \begin{cases} \gamma(2t), & 0 \le t \le \tfrac12,\\ \eta(2t-1), & \tfrac12 \le t \le 1.\end{cases}$$
Two paths with the same endpoints are [[Def - Homotopy of Paths|path-homotopic]], written $\gamma \simeq \eta$, if there is a continuous $H \colon [0,1]^2 \to M$ with $H(s,0) = \gamma(s)$, $H(s,1) = \eta(s)$, $H(0,t) = \gamma(0)$, and $H(1,t) = \gamma(1)$ for all $s,t$; we write $[\gamma]$ for the path-homotopy class of $\gamma$. The [[Def - Path-Product and the Fundamental Group|fundamental group]] $\pi_1(M,m)$ is the set of path-homotopy classes of loops at $m$ (paths with $\gamma(0) = \gamma(1) = m$) under $[\gamma][\eta] = [\gamma \cdot \eta]$; that this is a group is [[Thm - The Fundamental Group is a Group|proved separately]]. We write $\mathbb{1} = [c_m]$ for its identity. A space is [[Def - Simply Connected Space|simply connected]] if it is path-connected and its fundamental group is trivial.

A [[Def - Covering Space|covering map]] is a continuous surjection $q \colon \tilde M \to M$ such that every point of $M$ has an open **evenly covered** neighbourhood $U$: $q^{-1}(U) = \bigsqcup_\alpha \tilde U_\alpha$ is a disjoint union of open sets ("sheets"), each mapped by $q$ homeomorphically onto $U$. When $\tilde M$ and $M$ are smooth manifolds and $q$ is smooth with each restriction $q|_{\tilde U_\alpha}$ a diffeomorphism, $q$ is a **smooth covering map**; a smooth covering map is a **local diffeomorphism**. A [[Def - Deck Transformation Group|deck transformation]] of $q$ is a homeomorphism $\varphi \colon \tilde M \to \tilde M$ with $q \circ \varphi = q$; the deck transformations form a group $\operatorname{Deck}(\tilde M / M)$ under composition. A [[Def - Universal Cover|universal cover]] of $M$ is a covering $q \colon \tilde M \to M$ whose total space $\tilde M$ is simply connected.

For a discrete group $\Gamma$ acting on the left of a manifold $N$ by diffeomorphisms, the action is [[Def - Discrete Group and Properly Discontinuous Action|properly discontinuous]] if every $x \in N$ has a neighbourhood $U$ with $gU \cap U = \varnothing$ for every $g \in \Gamma \setminus \{e\}$; it is **free** if no non-identity element has a fixed point. A [[Def - Principal G-Bundle|principal G-bundle]] is a fibre bundle $\pi \colon P \to M$ with a smooth free right $G$-action preserving fibres and transitive on each of them, admitting $G$-equivariant local trivialisations. For a *discrete* structure group this reduces to a smooth covering map together with a free fibrewise-transitive right action, as we verify below. (In wikilink display text below we render symbols in Unicode, as the vault requires.)

> [!warning] Convention: deck transformations act on the left; the structure group of a principal bundle acts on the right.
> A deck transformation $\varphi$ is a self-map of $\tilde M$, and composition $(\varphi \circ \psi)$ makes $\operatorname{Deck}(\tilde M/M)$ act *on the left*. The series convention is that the structure group of a [[Def - Principal G-Bundle|principal bundle]] acts on the *right* (Gauge Theory series conventions: $R_g(p) = p \cdot g$). We therefore turn the isomorphism $\Phi \colon \pi_1(M,m) \xrightarrow{\ \cong\ } \operatorname{Deck}(\tilde M/M)$ of part (c) into a right action of $\pi_1(M,m)$ on $\tilde M$ by the standard inversion recipe
> $$\tilde x \cdot [\gamma] := \Phi([\gamma])^{-1}(\tilde x),$$
> which is a genuine right action precisely because $\Phi$ is a group homomorphism. Haydys (§3.3) writes only "$\tilde M$ viewed as a principal $\pi_1(M)$-bundle, $\pi_1(M)$ acting by deck transformations" and does not distinguish left from right; the recipe above is the one-line reconciliation with the series' right-action convention. Haydys also leaves the standing hypotheses on $M$ (local path-connectedness, semi-local simple connectivity) implicit; for a manifold they hold automatically, and we prove this as Lemma 1.

---

# Statement

> **Theorem (Existence of the universal cover and the deck action of $\pi_1$).** Let $M$ be a connected smooth manifold with base point $m \in M$.
>
> **(a) Existence, smoothness, uniqueness.** There is a simply connected smooth covering map $q \colon \tilde M \to M$ — the *universal cover*. The total space $\tilde M$ carries a unique smooth structure making $q$ a local diffeomorphism, and with it $\tilde M$ is Hausdorff and second countable, hence a smooth manifold. The universal cover is unique up to isomorphism of coverings over $M$: if $q_i \colon \tilde M_i \to M$ ($i = 1,2$) are two simply connected coverings, there is a diffeomorphism $h \colon \tilde M_1 \to \tilde M_2$ with $q_2 \circ h = q_1$.
>
> **(b) The deck action.** The deck group $\operatorname{Deck}(\tilde M / M)$ acts on $\tilde M$ smoothly, freely, and properly discontinuously, and transitively on each fibre $q^{-1}(x)$. The projection $q$ induces a diffeomorphism
> $$\tilde M / \operatorname{Deck}(\tilde M/M) \;\xrightarrow{\ \cong\ }\; M.$$
>
> **(c) The fundamental group is the deck group, and $q$ is a principal bundle.** Choosing $\tilde m \in q^{-1}(m)$, there is a canonical group isomorphism
> $$\Phi \colon \pi_1(M,m) \;\xrightarrow{\ \cong\ }\; \operatorname{Deck}(\tilde M / M).$$
> Transporting it to a right action $\tilde x \cdot [\gamma] = \Phi([\gamma])^{-1}(\tilde x)$ of the discrete group $\pi_1(M,m)$, the map $q \colon \tilde M \to M$ becomes a principal $\pi_1(M,m)$-bundle.
>
> **(d) Countability.** The group $\pi_1(M,m)$ is countable.

The four parts are logically intertwined: part (d) is used inside part (a) to establish second countability of $\tilde M$, and part (c) uses the free proper action of part (b) together with the quotient theorem to promote $q$ to a principal bundle. The proof below sequences the lemmas so that each is available where it is needed.

---

# Motivation

The whole of §5.4 rests on a single translation: a *flat connection is the same thing as a representation of the fundamental group*. That translation, proved on [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy-correspondence page]], needs a space on which to build the flat bundle attached to a representation $\rho \colon \pi_1(M,m) \to G$. That space is the universal cover $\tilde M$, and the bundle is the associated bundle $\tilde M \times_\rho G$ of the principal $\pi_1(M,m)$-bundle $q \colon \tilde M \to M$. So before we can say "flat bundles are representations", we must first know three concrete things, and this page supplies all three: that the universal cover *exists* as a smooth manifold, that the fundamental group *acts* on it as the deck group (making $q$ a principal bundle with discrete structure group $\pi_1$), and that $\pi_1$ is *countable* (which is what makes the moduli space of flat connections with compact structure group compact, on [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|the compactness page]]).

There is a second, more elementary reason the universal cover matters here. The [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy-invariance of flat holonomy]] tells us that parallel transport of a flat connection only sees the *homotopy class* of a loop, so the transport data is a map on $\pi_1(M,m)$. The universal cover is, quite literally, the space whose points are homotopy classes of paths starting at $m$: it is the geometric object that "remembers homotopy classes of paths and nothing more". Making that intuition into a theorem — with a smooth structure, a group action, and a principal-bundle statement — is exactly what turns the informal "transport depends only on homotopy" into the rigorous correspondence with representations.

We assume the reader knows the [[Def - Covering Space|covering space]], [[Def - Universal Cover|universal cover]], and [[Def - Deck Transformation Group|deck group]] definitions, the [[Thm - Path Lifting and Homotopy Lifting|path- and homotopy-lifting theorems]], and the [[Thm - Lifting Criterion for Continuous Maps|lifting criterion]] — all from the algebraic-topology chapter, where those results are proved for general topological spaces. This page adds the smooth-manifold content that the gauge-theory chapters need and cannot import from later chapters, and it proves the properties (existence, freeness, proper discontinuity, transitivity, the isomorphism with $\pi_1$, countability) that the definition pages only state.

---

# Sources and Targets

**Sources (Input Broadening).** The hypothesis "$M$ is a connected manifold" is mild, so the useful question is: which problems secretly hand you such an $M$, so that this theorem then hands you a universal cover, a $\pi_1$-action, and countability for free?

The first disguised source is **a connected Lie group $G$**. A Lie group is in particular a connected manifold, so the theorem produces its universal cover $\tilde G \to G$. The non-obvious bridge is that $\tilde G$ inherits a Lie group structure for which $\tilde G \to G$ is a homomorphism with kernel the discrete central subgroup $\pi_1(G)$: one lifts the multiplication $\tilde G \times \tilde G \to G$ through the covering using the lifting criterion (the domain $\tilde G \times \tilde G$ is simply connected). *Example problem:* recover that $\operatorname{SU}(2) \to \operatorname{SO}(3)$ is the universal cover with deck group $\mathbb{Z}/2$, so that $\pi_1(\operatorname{SO}(3)) = \mathbb{Z}/2$, from the fact that $\operatorname{SU}(2) \cong S^3$ is simply connected — see [[Ex - SU(2) is the Universal Cover of SO(3)|the SU(2)–SO(3) page]].

The second disguised source is **a manifold presented as a quotient $N / \Gamma$ by a free properly discontinuous action of a discrete group $\Gamma$**. By the [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|quotient-covering theorem]], the projection $N \to N/\Gamma$ is a covering with $\Gamma$ as a group of deck transformations; if moreover $N$ is simply connected, then $N \to N/\Gamma$ *is* the universal cover and $\pi_1(N/\Gamma) \cong \Gamma$ by part (c) of this theorem. The bridge is that a group action can manufacture both the cover and the fundamental group at once. *Example problem:* read off $\pi_1(T^n) = \mathbb{Z}^n$ from $T^n = \mathbb{R}^n / \mathbb{Z}^n$, since $\mathbb{R}^n$ is simply connected and $\mathbb{Z}^n$ acts freely and properly discontinuously by translation — this is [[Ex - The Universal Cover of the Circle and of the Torus|the torus exercise]].

The third disguised source is **a manifold known to be locally contractible but of unclear global shape**, for instance a configuration space or a manifold built by gluing charts. Every manifold is locally Euclidean, hence locally contractible, hence semi-locally simply connected, so the classical existence obstruction never appears and the theorem applies unconditionally. The bridge — that local contractibility upgrades to the semi-local-simple-connectivity hypothesis of the general existence theorem — is Lemma 1 below, and it is what lets us drop all point-set caveats when the base is a manifold. *Example problem:* certify that any smooth surface, however wildly embedded, has a universal cover and a well-defined countable $\pi_1$ without checking any point-set condition by hand.

**Targets (Output Amplification).** The bare conclusion — a simply connected principal $\pi_1(M,m)$-bundle $\tilde M \to M$ — becomes a machine when combined with extra data.

Combine the conclusion with **a homomorphism $\rho \colon \pi_1(M,m) \to G$ into a Lie group**. The [[Def - Associated Bundle|associated bundle]] $\tilde M \times_\rho G$ is then a principal $G$-bundle over $M$ carrying a canonical flat connection whose monodromy is $\rho$. The extra ingredient is the representation, and the payoff is the entire construction direction of the monodromy correspondence, [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|proved on the next page]]: *every* flat bundle arises this way. This is the reason the present page is a prerequisite of that one.

Combine the conclusion with **a specific free properly discontinuous action realising $M$ as a quotient**. If $M = \tilde M_0 / \Gamma$ with $\tilde M_0$ simply connected, uniqueness in part (a) identifies $\tilde M_0$ with the abstract universal cover and part (c) identifies $\Gamma$ with $\pi_1(M,m)$. The extra ingredient is the explicit quotient presentation; the payoff is a *computation* of the fundamental group and its representation variety. For $M = T^n$ this gives $\mathcal{R}(T^n; U(1)) = \operatorname{Hom}(\mathbb{Z}^n, U(1)) = U(1)^n$, the worked example on [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|the compactness page]].

Combine the conclusion with **an orientation double cover or a sign representation**. The countability of $\pi_1$ (part d) together with the deck action lets one build the **orientation double cover** of a non-orientable manifold as the associated bundle of the sign representation $\pi_1(M) \to \mathbb{Z}/2 \to O(1)$, and more generally the [[Ex - A Flat Connection on the Möbius Line Bundle with Holonomy Minus One|Möbius line bundle with holonomy −1]]. The extra ingredient is a homomorphism to $\{\pm 1\}$; the payoff is a genuinely non-trivial flat real line bundle, the simplest example distinguishing flat bundles by their monodromy.

For a *purely technical* role, note that part (d) — countability — is invoked once more, on [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|the compactness page]], to see that $\operatorname{Hom}(\pi_1(M,m), G)$ is a *countable* product of copies of the compact group $G$, so that a diagonal-subsequence argument gives compactness without appeal to the full Tychonoff theorem.

---

# Why Is It True

Forget the point-set machinery and picture what the universal cover *is*. Fix the base point $m$. A point of $M$ near $m$ is easy to name — you just point at it — but if $M$ is not simply connected, naming a point *together with a way of getting there from $m$* carries strictly more information: two routes from $m$ to the same endpoint can be genuinely different, non-homotopic, paths. The universal cover is the space you get by refusing to forget the route: its points are exactly the homotopy classes $[\gamma]$ of paths $\gamma$ starting at $m$, and the projection $q([\gamma]) = \gamma(1)$ throws the route away and remembers only the endpoint.

Why is this a *covering*? Over a small contractible neighbourhood $U$ of a point $x$, any two routes into $U$ that end at the same point of $U$ and arrive "the same way" are homotopic, because $U$ has no holes to wind around; so the classes $[\gamma]$ ending in $U$ organise into disjoint copies of $U$, one copy for each homotopy class of route from $m$ to the *edge* of $U$. Those copies are the sheets. Why is $\tilde M$ *simply connected*? A loop upstairs is a family of routes varying continuously and returning to its start; projecting it down and using that a lift is determined by its start, the loop must have been constant on homotopy classes all along — there is nothing left to wind around once the routes themselves are the points.

Now the deck group and $\pi_1$. A loop $\gamma$ at $m$ gives a self-map of $\tilde M$ by *prepending*: $[\alpha] \mapsto [\gamma \cdot \alpha]$. This shuffles the routes without changing their endpoints, so it commutes with $q$ — it is a deck transformation. Prepending $\gamma$ then $\delta$ is prepending $\delta \cdot \gamma$; matching this to composition of maps is exactly the statement that $\pi_1$ *is* the deck group. And the fibre over $m$ — the routes that come back to $m$, i.e. the loops — is precisely $\pi_1(M,m)$, on which the deck group acts simply transitively. That simple transitivity is what makes $q$ a *principal* bundle: the fibre is a torsor under $\pi_1$, a copy of the group with no preferred identity.

> **The mechanism in one sentence:** the universal cover is the space of homotopy classes of paths out of the base point, the fundamental group acts on it by prepending loops, and because prepending is free and simply transitive on the loops-that-return, the projection is a principal bundle whose structure group is $\pi_1$.

Countability, finally, is a separate and humbler fact: a manifold is covered by countably many coordinate balls, each simply connected, and any loop can be chopped into finitely many arcs each living in one ball; up to homotopy an arc in a simply connected ball is pinned down by its endpoints, and there are only countably many "junction" endpoints to choose from, so only countably many homotopy classes of loops can be assembled.

---

# What Makes This Hard

The genuinely non-trivial step is proving that the set of homotopy classes of paths, with the "prepend a small path in $U$" topology, is actually a covering space — that the candidate sheets are open, disjoint, and mapped homeomorphically — and this requires the base to be locally path-connected and semi-locally simply connected. For a general topological space these conditions must be hypothesised; the point that is easy to overlook is that for a *manifold* they are free, because a manifold is locally Euclidean, hence locally contractible (Lemma 1). The most common error in the smooth version is to build $\tilde M$ as a topological cover and then simply assert it is a manifold: one must actually produce charts (by pulling back charts of $M$ through the local homeomorphism $q$) and, separately, verify **second countability**, which does *not* follow from that of $M$ alone but needs the fibre — hence $\pi_1$ — to be countable. The other subtle point is the direction of the isomorphism $\pi_1 \cong \operatorname{Deck}$: with deck transformations composing on the left and loops concatenating in a fixed order, the map is a genuine homomorphism only for one of the two natural conventions, and turning it into the right action a principal bundle wants requires the inversion in the Convention callout.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build $\tilde M$ as the set of homotopy classes of paths from $m$, topologise it by the "extend inside a good neighbourhood" basis, and prove it is a covering of $M$ with simply connected total space (this needs only that a manifold is locally contractible). Pull charts of $M$ back through the local homeomorphism $q$ to make $\tilde M$ a smooth manifold; get second countability from countability of $\pi_1$, which you prove by a coordinate-ball chopping argument. Then read off the deck group: freeness and proper discontinuity come from uniqueness of lifts, transitivity on fibres from the lifting criterion applied to the simply connected $\tilde M$, and the isomorphism with $\pi_1$ from the prepending action. Finally, a free properly discontinuous action with quotient $M$ is a principal bundle for the discrete structure group.

**Subgoal decomposition:**

1. **Manifolds are semi-locally simply connected.** Show every manifold is locally contractible, hence locally path-connected and semi-locally simply connected.
   - *Hint:* Euclidean coordinate balls are contractible.
   - *Why needed:* it removes every point-set hypothesis from the general existence theorem, so the construction applies to any manifold.

2. **The construction is a covering.** Define $\tilde M$, the topology, and $q([\gamma]) = \gamma(1)$; prove $q$ is a covering map.
   - *Hint:* over a good neighbourhood $U$ (path-connected with $\pi_1(U) \to \pi_1(M)$ trivial), the sets $U_{[\gamma]}$ are the sheets.
   - *Why needed:* it is the existence statement of part (a) at the topological level.

3. **The total space is simply connected.** Show $\tilde M$ is path-connected and $\pi_1(\tilde M) = 1$.
   - *Hint:* connect $[\gamma]$ to $\tilde m$ along the "shrinking $\gamma$" path; kill $\pi_1(\tilde M)$ using that a loop upstairs projects to a nullhomotopic loop.
   - *Why needed:* it is the defining property of a *universal* cover and the engine of transitivity and uniqueness.

4. **Smooth structure and second countability.** Pull back charts of $M$ through $q$; prove Hausdorffness; prove second countability from countability of the fibre.
   - *Hint:* a countable basis of evenly covered sets downstairs has countably many sheets over it upstairs once the fibre is countable.
   - *Why needed:* it makes $\tilde M$ a smooth manifold and $q$ a local diffeomorphism.

5. **$\pi_1$ is countable.** Chop a loop into finitely many arcs in coordinate balls; count.
   - *Hint:* countably many balls, countably many junction points, one homotopy class per pair of endpoints in a simply connected ball.
   - *Why needed:* it supplies second countability in subgoal 4 and countability in part (d).

6. **The deck action.** Prove free, properly discontinuous, transitive on fibres, with quotient $M$.
   - *Hint:* free and properly discontinuous from unique lifting; transitive from the lifting criterion; quotient from the chapter-I quotient theorem.
   - *Why needed:* part (b).

7. **$\pi_1 \cong \operatorname{Deck}$ and the principal-bundle structure.** Prepending loops realises $\pi_1$ as the deck group; the induced right action makes $q$ a principal $\pi_1$-bundle.
   - *Hint:* $\Phi([\gamma])[\alpha] = [\gamma \cdot \alpha]$; equivariant trivialisations come from evenly covered sets.
   - *Why needed:* part (c).

---

# Lemma Decomposition

> [!note]- Lemma 1: A smooth manifold is locally contractible, hence locally path-connected and semi-locally simply connected
> **Statement:** Every point of a smooth manifold $M$ has arbitrarily small open neighbourhoods that are contractible. Consequently $M$ is locally path-connected and semi-locally simply connected: every $x \in M$ has a neighbourhood $U$ for which the inclusion-induced map $\pi_1(U,x) \to \pi_1(M,x)$ is trivial.
>
> **Hint:** Use a chart carrying $x$ to $0$ and a round ball; a ball is star-shaped, hence contractible.
>
> **Why needed:** It certifies that the classical existence hypotheses hold for *every* manifold, so the construction of Lemma 2 applies unconditionally.
>
> > [!note]- Full proof
> > **Goal.** We must produce, around each point, contractible neighbourhoods, and deduce the two point-set properties.
> >
> > **Existence of contractible neighbourhoods.** Let $x \in M$. By definition of a smooth manifold there is a chart $(V,\phi)$ with $x \in V$ and $\phi \colon V \to \phi(V) \subseteq \mathbb{R}^n$ a homeomorphism onto an open set. Choose $r > 0$ with the round ball $B = B_r(\phi(x)) \subseteq \phi(V)$ (possible since $\phi(V)$ is open), and set $U = \phi^{-1}(B)$, an open neighbourhood of $x$. The ball $B$ is convex, hence star-shaped about $\phi(x)$, so the straight-line homotopy $F(y,t) = (1-t)y + t\,\phi(x)$ contracts $B$ to $\phi(x)$; transporting it through $\phi$, the map $H(z,t) = \phi^{-1}\big((1-t)\phi(z) + t\,\phi(x)\big)$ is a continuous homotopy $U \times [0,1] \to U$ from $\operatorname{id}_U$ to the constant map $x$ (it lands in $U$ because $B$ is convex and $\phi^{-1}$ is defined on $B$). Hence $U$ is contractible. Shrinking $r$ gives arbitrarily small such $U$.
> >
> > **Local path-connectedness.** A contractible space is path-connected (the contraction gives, for any two points $z, z'$, the concatenation of the tracks $t \mapsto H(z,t)$ and $t \mapsto H(z',1-t)$, a path from $z$ to $z'$). Since arbitrarily small neighbourhoods $U$ are contractible, hence path-connected, $M$ is locally path-connected.
> >
> > **Semi-local simple connectivity.** For the contractible neighbourhood $U$ of $x$ and any loop $\eta$ in $U$ at $x$, the homotopy $s \mapsto H(\eta(s),\,\cdot\,)$ contracts $\eta$ to the constant loop $c_x$ *within $U$*; a fortiori $\eta$ is nullhomotopic in $M$. Thus every element of the image of $\pi_1(U,x) \to \pi_1(M,x)$ is trivial, i.e. the map is the trivial homomorphism. This is exactly semi-local simple connectivity. $\blacksquare$

> [!note]- Lemma 2: The space of homotopy classes of paths is a covering of $M$
> **Statement:** Let $\tilde M = \{[\gamma] : \gamma \text{ a path in } M \text{ with } \gamma(0) = m\}$ and $q \colon \tilde M \to M$, $q([\gamma]) = \gamma(1)$. For an open $U \subseteq M$ that is path-connected with $\pi_1(U,u) \to \pi_1(M,u)$ trivial for one (hence every) $u \in U$ — call such $U$ *good* — and a class $[\gamma]$ with $\gamma(1) \in U$, put
> $$U_{[\gamma]} = \{[\gamma \cdot \eta] : \eta \text{ a path in } U \text{ with } \eta(0) = \gamma(1)\}.$$
> The sets $U_{[\gamma]}$ form the basis of a topology on $\tilde M$, and with it $q$ is a covering map. Every point of $M$ has a good neighbourhood.
>
> **Hint:** Good neighbourhoods exist by Lemma 1. Show $q$ maps each $U_{[\gamma]}$ bijectively onto $U$, that the $U_{[\gamma]}$ over a fixed good $U$ are equal or disjoint, and that $q$ restricts to a homeomorphism on each.
>
> **Why needed:** It is the existence statement of part (a) at the level of topological spaces.
>
> > [!note]- Full proof
> > **Goal.** Construct the topology, verify it is a topology, and verify the covering axioms.
> >
> > **Good neighbourhoods exist and form a basis of $M$.** By Lemma 1 every $x \in M$ has contractible — in particular path-connected and, by the semi-local condition, good — neighbourhoods, arbitrarily small; so good open sets cover $M$ and form a basis for the topology of $M$. We use repeatedly that if $U$ is good and $u, u' \in U$, then any two paths in $U$ from $u$ to $u'$ are homotopic *in $M$* (rel endpoints): their concatenation-with-reverse is a loop in $U$, nullhomotopic in $M$ by goodness, and a nullhomotopic difference means the two paths are $M$-homotopic.
> >
> > **$q$ maps $U_{[\gamma]}$ onto $U$.** Fix good $U$ and $[\gamma]$ with $\gamma(1) \in U$. For $[\gamma \cdot \eta] \in U_{[\gamma]}$ we have $q([\gamma \cdot \eta]) = (\gamma \cdot \eta)(1) = \eta(1) \in U$, so $q(U_{[\gamma]}) \subseteq U$. Conversely, since $U$ is path-connected, any $u \in U$ is $\eta(1)$ for some path $\eta$ in $U$ from $\gamma(1)$, so $u = q([\gamma \cdot \eta])$; thus $q(U_{[\gamma]}) = U$.
> >
> > **$q|_{U_{[\gamma]}}$ is injective.** Suppose $[\gamma \cdot \eta] , [\gamma \cdot \eta'] \in U_{[\gamma]}$ with $q([\gamma \cdot \eta]) = q([\gamma \cdot \eta'])$, i.e. $\eta(1) = \eta'(1)$. Both $\eta, \eta'$ are paths in $U$ from $\gamma(1)$ to the same point, so $\eta \simeq \eta'$ rel endpoints in $M$ by goodness (previous paragraph); hence $\gamma \cdot \eta \simeq \gamma \cdot \eta'$ and $[\gamma \cdot \eta] = [\gamma \cdot \eta']$. So $q|_{U_{[\gamma]}}$ is a bijection $U_{[\gamma]} \to U$.
> >
> > **The $U_{[\gamma]}$ are the basis of a topology.** We check the basis axiom: if $[\delta] \in U_{[\gamma]} \cap V_{[\gamma']}$ with $U, V$ good, there is a good $W \ni q([\delta])$ with $W_{[\delta]} \subseteq U_{[\gamma]} \cap V_{[\gamma']}$. First note that $[\delta] \in U_{[\gamma]}$ implies $U_{[\delta]} = U_{[\gamma]}$: writing $\delta \simeq \gamma \cdot \eta$ with $\eta$ in $U$, any $[\delta \cdot \mu]$ with $\mu$ in $U$ equals $[\gamma \cdot (\eta \cdot \mu)] \in U_{[\gamma]}$ and conversely, so the two basic sets coincide. Now take $W \subseteq U \cap V$ good with $q([\delta]) \in W$ (exists since good sets form a basis of $M$). For $\mu$ a path in $W$ from $q([\delta])$, $[\delta \cdot \mu] \in U_{[\delta]} = U_{[\gamma]}$ and $\in V_{[\delta]} = V_{[\gamma']}$ (as $\mu$ lies in $W \subseteq U$ and $\subseteq V$); hence $W_{[\delta]} \subseteq U_{[\gamma]} \cap V_{[\gamma']}$, and $[\delta] \in W_{[\delta]}$ (take $\mu = c_{q([\delta])}$). This is the basis axiom, so the $U_{[\gamma]}$ generate a topology.
> >
> > **$q$ is continuous and open.** For good $U$ and any basic $U_{[\gamma]}$, $q(U_{[\gamma]}) = U$ is open, so $q$ is open. For continuity, let $V \subseteq M$ be open and $[\delta] \in q^{-1}(V)$; pick good $W \subseteq V$ with $q([\delta]) \in W$; then $W_{[\delta]}$ is a basic neighbourhood of $[\delta]$ with $q(W_{[\delta]}) = W \subseteq V$, so $q^{-1}(V)$ is open. As $q|_{U_{[\gamma]}}$ is a continuous open bijection onto $U$, it is a homeomorphism.
> >
> > **Even covering.** Fix good $U$ and $x \in U$; we show $q^{-1}(U) = \bigsqcup_{[\gamma] \in q^{-1}(x)} U_{[\gamma]}$ with the $U_{[\gamma]}$ pairwise equal or disjoint. Every class in $q^{-1}(U)$ ends in $U$, so lies in $U_{[\delta]}$ for $[\delta]$ its own class, and $U_{[\delta]} = U_{[\gamma]}$ for the class $[\gamma]$ obtained by dragging the endpoint back to $x$ inside $U$; hence $q^{-1}(U) = \bigcup_{[\gamma] \in q^{-1}(x)} U_{[\gamma]}$. Two such sets $U_{[\gamma]}, U_{[\gamma']}$ ($[\gamma],[\gamma'] \in q^{-1}(x)$) are equal if $U_{[\gamma]} \cap U_{[\gamma']} \neq \varnothing$ (by the coincidence shown in the basis step) and otherwise disjoint; and $U_{[\gamma]} = U_{[\gamma']}$ forces $[\gamma] = [\gamma']$ since restricting $q$ to $U_{[\gamma]}$ is injective and both classes map to $x$. So the union is disjoint, indexed by $q^{-1}(x)$, and each piece maps homeomorphically onto $U$. Thus $U$ is evenly covered and $q$ is a covering map. $\blacksquare$

> [!note]- Lemma 3: The total space $\tilde M$ is simply connected
> **Statement:** With $\tilde M$, $q$ as in Lemma 2 and $\tilde m = [c_m] \in q^{-1}(m)$, the space $\tilde M$ is path-connected and $\pi_1(\tilde M, \tilde m) = \{1\}$. Hence $q \colon \tilde M \to M$ is a universal cover.
>
> **Hint:** For path-connectedness use the "restriction paths" $\gamma_s(t) = \gamma(st)$; for triviality of $\pi_1(\tilde M)$ use that $q_* \pi_1(\tilde M, \tilde m)$ consists of classes of loops that lift to loops, and identify this with the classes fixing the endpoint.
>
> **Why needed:** Being simply connected is what makes $q$ the *universal* cover; it drives transitivity of the deck action (Lemma 6) and uniqueness (Formal Proof).
>
> > [!note]- Full proof
> > **Goal.** Show any point connects to $\tilde m$ by a path, and any loop at $\tilde m$ is nullhomotopic.
> >
> > **Path-connectedness.** Let $[\gamma] \in \tilde M$, with $\gamma$ a path from $m$. Define, for $s \in [0,1]$, the truncated path $\gamma_s(t) = \gamma(st)$, running from $m$ to $\gamma(s)$; then $\Gamma(s) = [\gamma_s]$ is a map $[0,1] \to \tilde M$ with $\Gamma(0) = [c_m] = \tilde m$ and $\Gamma(1) = [\gamma]$. It is continuous: given a basic neighbourhood $U_{[\gamma_{s_0}]}$ of $\Gamma(s_0)$, choose $\varepsilon$ so that $\gamma([s_0 - \varepsilon, s_0 + \varepsilon]) \subseteq U$ (continuity of $\gamma$, $U$ good); for $s$ in this range $\gamma_s \simeq \gamma_{s_0} \cdot (\text{restriction of } \gamma \text{ to } [s_0, s])$ up to reparametrisation, so $\Gamma(s) \in U_{[\gamma_{s_0}]}$. Hence $\Gamma$ is a path from $\tilde m$ to $[\gamma]$, and $\tilde M$ is path-connected.
> >
> > **Trivial fundamental group.** By the [[Thm - Lifting Criterion for Continuous Maps|lifting-criterion]] machinery, $q_*$ is injective on $\pi_1(\tilde M, \tilde m)$ (a covering induces an injection on $\pi_1$, since a nullhomotopy downstairs lifts, by the [[Thm - Path Lifting and Homotopy Lifting|homotopy-lifting property]], to a nullhomotopy upstairs with fixed endpoints). So it suffices to show $q_* \pi_1(\tilde M, \tilde m) = \{1\}$ in $\pi_1(M,m)$. A class in $q_* \pi_1(\tilde M, \tilde m)$ is $[q \circ \tilde\ell]$ for a loop $\tilde\ell$ at $\tilde m$; write $\gamma = q \circ \tilde\ell$, a loop at $m$. The path $s \mapsto \Gamma(s) = [\gamma_s]$ of the previous paragraph is *the* lift of $\gamma$ starting at $\tilde m$ (it satisfies $q(\Gamma(s)) = \gamma_s(1) = \gamma(s)$ and $\Gamma(0) = \tilde m$), so by uniqueness of lifts $\tilde\ell = \Gamma$. Since $\tilde\ell$ is a loop, $\Gamma(1) = \Gamma(0)$, that is $[\gamma_1] = [c_m]$; but $\gamma_1 = \gamma$, so $[\gamma] = [c_m] = \mathbb{1}$. Thus $q_* \pi_1(\tilde M, \tilde m) = \{1\}$, and by injectivity $\pi_1(\tilde M, \tilde m) = \{1\}$. Together with path-connectedness, $\tilde M$ is simply connected. $\blacksquare$

> [!note]- Lemma 4: The fibre over $m$ is in canonical bijection with $\pi_1(M,m)$
> **Statement:** The map $\pi_1(M,m) \to q^{-1}(m)$, $[\gamma] \mapsto [\gamma]$ (a loop at $m$ is a path from $m$ ending at $m$), is a well-defined bijection.
>
> **Hint:** A class in $q^{-1}(m)$ is exactly a homotopy class of path from $m$ that *ends* at $m$, i.e. a loop.
>
> **Why needed:** It identifies the fibre — hence the number of sheets — with $\pi_1$, giving countability of the fibre from countability of $\pi_1$ (used in Lemma 5) and the torsor structure in Lemma 7.
>
> > [!note]- Full proof
> > **Goal.** Match loop classes with fibre points.
> >
> > A point of $q^{-1}(m)$ is a class $[\gamma]$ with $q([\gamma]) = \gamma(1) = m$ and $\gamma(0) = m$ by definition of $\tilde M$; that is, $\gamma$ is a loop at $m$ and $[\gamma]$ its path-homotopy class. Conversely every loop class $[\gamma] \in \pi_1(M,m)$ is such a point. The two descriptions are literally the same set of homotopy classes, so the identity assignment $[\gamma] \mapsto [\gamma]$ is a well-defined bijection $\pi_1(M,m) \to q^{-1}(m)$. $\blacksquare$

> [!note]- Lemma 5: $\pi_1(M,m)$ is countable
> **Statement:** The fundamental group of a connected smooth manifold $M$ is countable.
>
> **Hint:** Cover $M$ by countably many coordinate balls; chop a loop into finitely many arcs each inside one ball; count the possible arcs up to homotopy through countably many junction points.
>
> **Why needed:** It is part (d), and it supplies the countable fibre used to prove second countability of $\tilde M$ in Lemma 6' (Formal Proof, Step 4).
>
> > [!note]- Full proof
> > **Goal.** Exhibit a countable generating set for $\pi_1(M,m)$; a group with a countable generating set is countable.
> >
> > **Step 1 — a countable cover by simply connected balls.** Since $M$ is a manifold it is second countable, so from the basis of contractible coordinate balls of Lemma 1 we may extract a *countable* subfamily $\mathcal{B} = \{B_i\}_{i \in I}$, $I \subseteq \mathbb{N}$, still covering $M$ (every open cover of a second-countable space has a countable subcover, by choosing for each basic set of a fixed countable basis one member of the cover containing it). Each $B_i$ is contractible, hence path-connected and simply connected.
> >
> > **Step 2 — countably many junction points.** For each ordered pair $(i,j) \in I \times I$ with $B_i \cap B_j \neq \varnothing$, the intersection $B_i \cap B_j$ is a nonempty open subset of the manifold $M$, hence itself a manifold, hence second countable, hence has at most countably many path-components. Choose one point in each such component; over all pairs this selects a countable set $\mathcal{P} = \{p_k\}_{k \in K}$, $K \subseteq \mathbb{N}$, of *junction points*, and we include $m$ among them by fixing the index of a ball containing $m$. For each $p_k$ fix once and for all a path $g_k$ in $M$ from $m$ to $p_k$ (possible since $M$ is path-connected), with $g$ at $m$ taken to be the constant path $c_m$.
> >
> > **Step 3 — the countable generating set.** For any two junction points $p_k, p_l$ lying in a common ball $B_i$, the ball is simply connected, so *any* path in $B_i$ from $p_k$ to $p_l$ is homotopic rel endpoints to any other such path; call the resulting well-defined homotopy class $h_{i,k,l}$ (defined only when $p_k, p_l \in B_i$). Set
> > $$\mathcal{G} = \big\{\, [\,g_k \cdot h_{i,k,l} \cdot \bar g_l\,] \in \pi_1(M,m) : p_k, p_l \in B_i \,\big\}.$$
> > The index set — triples $(i,k,l)$ — is a subset of $I \times K \times K$, hence countable, so $\mathcal{G}$ is countable.
> >
> > **Step 4 — $\mathcal{G}$ generates.** Let $f$ be any loop at $m$. The sets $\{f^{-1}(B_i)\}_{i \in I}$ form an open cover of the compact interval $[0,1]$; by the Lebesgue number lemma there is a subdivision $0 = t_0 < t_1 < \dots < t_N = 1$ with each $f([t_{r-1}, t_r])$ contained in some ball $B_{i_r}$. For each interior division point $t_r$ ($1 \le r \le N-1$), the point $f(t_r)$ lies in $B_{i_r} \cap B_{i_{r+1}}$, so it lies in the path-component of that intersection whose chosen junction point we call $p_{k_r}$; let $\sigma_r$ be a path *inside* $B_{i_r} \cap B_{i_{r+1}}$ from $f(t_r)$ to $p_{k_r}$. Set $k_0$ so that $p_{k_0} = m = f(t_0) = f(t_N)$ and $\sigma_0 = \sigma_N = c_m$. Writing $f_r = f|_{[t_{r-1},t_r]}$ (reparametrised to $[0,1]$), a standard telescoping — inserting $\bar\sigma_{r-1} \cdot \sigma_{r-1} \simeq \text{const}$ between consecutive arcs — gives
> > $$f \simeq (f_1 \cdot \sigma_1)\cdot(\bar\sigma_1 \cdot f_2 \cdot \sigma_2)\cdots(\bar\sigma_{N-1}\cdot f_N),$$
> > rel endpoints. Each factor $\bar\sigma_{r-1}\cdot f_r \cdot \sigma_r$ is a path from $p_{k_{r-1}}$ to $p_{k_r}$ lying entirely in the simply connected ball $B_{i_r}$ (both $\sigma$'s live in intersections contained in $B_{i_r}$, and $f_r$ lives in $B_{i_r}$), so its class rel endpoints is $h_{i_r, k_{r-1}, k_r}$. Therefore
> > $$[f] = \prod_{r=1}^{N} \big[g_{k_{r-1}} \cdot h_{i_r, k_{r-1}, k_r} \cdot \bar g_{k_r}\big],$$
> > where we have again inserted cancelling pairs $\bar g_{k_r} \cdot g_{k_r} \simeq \text{const}$ between the factors and used $g_{k_0} = g_{k_N} = c_m$. Each bracket is an element of $\mathcal{G}$ (or its inverse, which is also generated). Hence $[f]$ is a finite product of elements of $\mathcal{G}$.
> >
> > **Conclusion.** Every element of $\pi_1(M,m)$ is a finite product of elements of the countable set $\mathcal{G}$, so $\pi_1(M,m)$ is countable (the set of finite words in a countable alphabet is countable, and $\pi_1$ is a quotient of it). $\blacksquare$

> [!note]- Lemma 6: The deck group acts freely, properly discontinuously, and transitively on fibres
> **Statement:** Let $q \colon \tilde M \to M$ be the universal cover of Lemmas 2–3. The group $\operatorname{Deck}(\tilde M/M)$ acts on $\tilde M$ (i) *freely* — a deck transformation with a fixed point is the identity; (ii) *properly discontinuously* — every $\tilde x$ has a neighbourhood $W$ with $\varphi(W) \cap W = \varnothing$ for all $\varphi \neq \operatorname{id}$; (iii) *transitively on each fibre* — for $\tilde x, \tilde y \in q^{-1}(x)$ there is $\varphi \in \operatorname{Deck}(\tilde M/M)$ with $\varphi(\tilde x) = \tilde y$; and the action is by diffeomorphisms once the smooth structure of Step 2 of the Formal Proof is in place.
>
> **Hint:** (i) and (ii) from uniqueness of lifts; (iii) from the [[Thm - Lifting Criterion for Continuous Maps|lifting criterion]] using that $\tilde M$ is simply connected.
>
> **Why needed:** It is the content of part (b) apart from the quotient identification, and it feeds the principal-bundle structure of part (c).
>
> > [!note]- Full proof
> > **Goal.** Establish freeness, proper discontinuity, and fibrewise transitivity.
> >
> > **Uniqueness of lifts (recalled).** We use the following consequence of the [[Thm - Path Lifting and Homotopy Lifting|path-lifting theorem]]: *if $\tilde M$ is connected and $f, f' \colon \tilde M \to \tilde M$ are continuous with $q \circ f = q \circ f' = q$ and $f(\tilde x) = f'(\tilde x)$ for one point $\tilde x$, then $f = f'$.* Indeed, the set $\{\tilde y : f(\tilde y) = f'(\tilde y)\}$ is open (on an evenly covered neighbourhood two lifts landing in the same sheet at a point agree there) and closed (if they landed in different sheets at a limit point they would differ on a neighbourhood), nonempty, hence all of the connected $\tilde M$.
> >
> > **(i) Freeness.** Let $\varphi \in \operatorname{Deck}(\tilde M/M)$ fix a point $\tilde x$. Then $\varphi$ and $\operatorname{id}_{\tilde M}$ are both self-maps covering $q$ (indeed $q \circ \varphi = q = q \circ \operatorname{id}$) and agree at $\tilde x$; by uniqueness of lifts $\varphi = \operatorname{id}_{\tilde M}$. So only the identity has a fixed point: the action is free. ($\tilde M$ is connected by Lemma 3.)
> >
> > **(ii) Proper discontinuity.** Let $\tilde x \in \tilde M$ and let $U$ be an evenly covered neighbourhood of $q(\tilde x)$, with $\tilde x$ in the sheet $W$ (so $q|_W \colon W \to U$ is a homeomorphism). Take any $\varphi \neq \operatorname{id}$ and suppose $\varphi(W) \cap W \neq \varnothing$. Since $q \circ \varphi = q$, the set $\varphi(W)$ is again a sheet over $U$; two sheets over an evenly covered $U$ are equal or disjoint, so $\varphi(W) = W$. Then $q|_W \circ \varphi|_W = q|_W$ as maps $W \to U$, and since $q|_W$ is injective, $\varphi|_W = \operatorname{id}_W$; thus $\varphi$ has a fixed point, forcing $\varphi = \operatorname{id}$ by (i) — a contradiction. Hence $\varphi(W) \cap W = \varnothing$ for every $\varphi \neq \operatorname{id}$, and the action is properly discontinuous.
> >
> > **(iii) Fibrewise transitivity.** Let $\tilde x, \tilde y \in q^{-1}(x)$. We seek a deck transformation carrying $\tilde x$ to $\tilde y$. Apply the [[Thm - Lifting Criterion for Continuous Maps|lifting criterion]] — *for a covering $q \colon \tilde M \to M$ and a connected, locally path-connected space $Y$ with a map $g \colon Y \to M$ and basepoints, a lift $\tilde g$ with prescribed value at the basepoint exists iff $g_* \pi_1(Y) \subseteq q_* \pi_1(\tilde M)$, and is then unique* — to $Y = \tilde M$ and $g = q$: the required inclusion $q_* \pi_1(\tilde M, \tilde x) \subseteq q_* \pi_1(\tilde M, \tilde y)$ holds because $\pi_1(\tilde M, \tilde x) = \{1\}$ by Lemma 3, and $\tilde M$ is connected and locally path-connected (being locally homeomorphic to $M$, which is so by Lemma 1). So there is a unique continuous $\varphi \colon \tilde M \to \tilde M$ with $q \circ \varphi = q$ and $\varphi(\tilde x) = \tilde y$. Symmetrically there is $\psi$ with $q \circ \psi = q$ and $\psi(\tilde y) = \tilde x$. Now $\psi \circ \varphi$ covers $q$ and fixes $\tilde x$, so $\psi \circ \varphi = \operatorname{id}$ by uniqueness of lifts; likewise $\varphi \circ \psi = \operatorname{id}$. Hence $\varphi$ is a homeomorphism with $q \circ \varphi = q$, i.e. a deck transformation, and $\varphi(\tilde x) = \tilde y$. The action is transitive on the fibre.
> >
> > **Smoothness of the action.** Once $\tilde M$ carries the smooth structure making $q$ a local diffeomorphism (Formal Proof, Step 2), a deck transformation $\varphi$ is locally $\varphi = (q|_{\text{sheet}})^{-1} \circ q$, a composition of local diffeomorphisms, hence smooth; its inverse is a deck transformation too, so $\varphi$ is a diffeomorphism. $\blacksquare$

> [!note]- Lemma 7: Prepending loops identifies $\pi_1(M,m)$ with the deck group, and $q$ is a principal $\pi_1$-bundle
> **Statement:** With $\tilde m = [c_m]$, define, for $[\gamma] \in \pi_1(M,m)$, the map $\Phi([\gamma]) \colon \tilde M \to \tilde M$, $\Phi([\gamma])([\alpha]) = [\gamma \cdot \alpha]$. Then each $\Phi([\gamma])$ is a deck transformation, and $\Phi \colon \pi_1(M,m) \to \operatorname{Deck}(\tilde M/M)$ is a group isomorphism. Defining the right action $\tilde x \cdot [\gamma] := \Phi([\gamma])^{-1}(\tilde x)$, the map $q \colon \tilde M \to M$ is a principal $\pi_1(M,m)$-bundle for the discrete structure group $\pi_1(M,m)$.
>
> **Hint:** Prepending a fixed loop preserves endpoints, so commutes with $q$; it maps basic sets to basic sets; the homomorphism law is $\gamma \cdot (\delta \cdot \alpha) = (\gamma \cdot \delta) \cdot \alpha$; equivariant local trivialisations come from evenly covered sets.
>
> **Why needed:** It is part (c): both the isomorphism $\pi_1 \cong \operatorname{Deck}$ and the promotion of $q$ to a principal bundle.
>
> > [!note]- Full proof
> > **Goal.** Show $\Phi$ is well defined into $\operatorname{Deck}$, an isomorphism, and that the induced right action makes $q$ principal.
> >
> > **$\Phi([\gamma])$ is a well-defined deck transformation.** For a loop $\gamma$ at $m$ and a path $\alpha$ from $m$, the concatenation $\gamma \cdot \alpha$ is again a path from $m$, so $[\gamma \cdot \alpha] \in \tilde M$; and if $\alpha \simeq \alpha'$ rel endpoints then $\gamma \cdot \alpha \simeq \gamma \cdot \alpha'$, and if $\gamma \simeq \gamma'$ rel endpoints then $\gamma\cdot\alpha \simeq \gamma'\cdot\alpha$, so the value depends only on $[\gamma]$ and $[\alpha]$: $\Phi([\gamma])$ is well defined. It covers $q$ because $q(\Phi([\gamma])[\alpha]) = (\gamma\cdot\alpha)(1) = \alpha(1) = q([\alpha])$. It maps the basic set $U_{[\alpha]}$ onto $U_{[\gamma\cdot\alpha]}$ (prepending $\gamma$ commutes with appending a path $\eta$ in $U$: $\gamma\cdot(\alpha\cdot\eta) \simeq (\gamma\cdot\alpha)\cdot\eta$), so it is continuous and open, hence a homeomorphism with inverse $\Phi([\bar\gamma])$ (since $[\gamma\cdot(\bar\gamma\cdot\alpha)] = [\alpha]$). Thus $\Phi([\gamma]) \in \operatorname{Deck}(\tilde M/M)$.
> >
> > **$\Phi$ is a homomorphism.** For $[\gamma],[\delta] \in \pi_1(M,m)$ and any $[\alpha]$,
> > $$\Phi([\gamma])\big(\Phi([\delta])[\alpha]\big) = \Phi([\gamma])[\delta\cdot\alpha] = [\gamma\cdot(\delta\cdot\alpha)] = [(\gamma\cdot\delta)\cdot\alpha] = \Phi([\gamma][\delta])[\alpha] \quad(\text{associativity of concatenation up to homotopy}),$$
> > so $\Phi([\gamma])\circ\Phi([\delta]) = \Phi([\gamma][\delta])$: $\Phi$ is a group homomorphism.
> >
> > **$\Phi$ is injective.** If $\Phi([\gamma]) = \operatorname{id}$, then evaluating at $\tilde m = [c_m]$ gives $[\gamma] = [\gamma\cdot c_m] = \Phi([\gamma])(\tilde m) = \tilde m = [c_m] = \mathbb{1}$. So $\ker\Phi$ is trivial.
> >
> > **$\Phi$ is surjective.** Let $\varphi \in \operatorname{Deck}(\tilde M/M)$. Then $\varphi(\tilde m) \in q^{-1}(m)$, which by Lemma 4 is a loop class $[\gamma] \in \pi_1(M,m)$. The deck transformation $\Phi([\gamma])$ also sends $\tilde m$ to $[\gamma\cdot c_m] = [\gamma] = \varphi(\tilde m)$. Two deck transformations agreeing at $\tilde m$ are equal by uniqueness of lifts (Lemma 6, freeness argument: $\varphi^{-1}\circ\Phi([\gamma])$ fixes $\tilde m$, hence is the identity), so $\varphi = \Phi([\gamma])$. Thus $\Phi$ is onto, and altogether a group isomorphism $\pi_1(M,m) \xrightarrow{\cong} \operatorname{Deck}(\tilde M/M)$.
> >
> > **The right action.** Put $\tilde x \cdot [\gamma] := \Phi([\gamma])^{-1}(\tilde x)$. This is a right action: $\tilde x\cdot \mathbb{1} = \Phi(\mathbb{1})^{-1}(\tilde x) = \tilde x$, and since $\Phi$ is a homomorphism,
> > $$(\tilde x\cdot[\gamma])\cdot[\delta] = \Phi([\delta])^{-1}\Phi([\gamma])^{-1}(\tilde x) = \big(\Phi([\gamma])\Phi([\delta])\big)^{-1}(\tilde x) = \Phi([\gamma][\delta])^{-1}(\tilde x) = \tilde x\cdot([\gamma][\delta]).$$
> > The action is smooth (each $\Phi([\gamma])$ is a diffeomorphism, Lemma 6), free (the $\Phi([\gamma])$ act freely, Lemma 6(i)), and preserves fibres and is transitive on each of them (Lemma 6(iii)); it is properly discontinuous (Lemma 6(ii)).
> >
> > **Equivariant local trivialisations.** Let $U \subseteq M$ be evenly covered and connected, with $q^{-1}(U) = \bigsqcup_{[\gamma]\in\pi_1} W_{[\gamma]}$ where $W_{[\gamma]} := \Phi([\gamma])(W_{\mathbb 1})$ and $W_{\mathbb 1}$ is a chosen sheet (the deck group permutes the sheets simply transitively, since it is transitive on the fibre by Lemma 6(iii) and free, so the sheets over $U$ are indexed bijectively by $\pi_1$ via $[\gamma] \mapsto \Phi([\gamma])(W_{\mathbb 1})$). Define
> > $$\Psi_U \colon q^{-1}(U) \to U \times \pi_1(M,m), \qquad \Psi_U(\tilde x) = \big(q(\tilde x),\, [\gamma]\big) \text{ where } \tilde x \in W_{[\gamma]}.$$
> > This is a diffeomorphism onto $U \times \pi_1$ (a local diffeomorphism on each sheet, and the discrete second factor separates the sheets). We verify it is equivariant, where $\pi_1(M,m)$ acts on the right of $U \times \pi_1(M,m)$ by $(u, [\gamma]) \cdot [\delta] := (u,\, [\delta]^{-1}[\gamma])$ — the standard right action of the group on itself, transported through the inversion built into $\Phi$. Take $\tilde x \in W_{[\gamma]}$, so $\Psi_U(\tilde x) = (q(\tilde x), [\gamma])$. Its image under the right action is
> > $$\tilde x \cdot [\delta] = \Phi([\delta])^{-1}(\tilde x) \in \Phi([\delta])^{-1}\big(W_{[\gamma]}\big) = \Phi([\delta])^{-1}\Phi([\gamma])\big(W_{\mathbb 1}\big) = \Phi\big([\delta]^{-1}[\gamma]\big)\big(W_{\mathbb 1}\big) = W_{[\delta]^{-1}[\gamma]} \qquad (\Phi \text{ a homomorphism}),$$
> > so its label is $[\delta]^{-1}[\gamma]$ and $\Psi_U(\tilde x \cdot [\delta]) = (q(\tilde x),\, [\delta]^{-1}[\gamma]) = \Psi_U(\tilde x) \cdot [\delta]$ (using $q(\tilde x \cdot [\delta]) = q(\tilde x)$ since $\Phi([\delta])^{-1}$ is a deck transformation). Thus $\Psi_U$ is a $\pi_1$-equivariant local trivialisation.
> >
> > **Conclusion.** The smooth covering $q$ carries a smooth, free, fibrewise-transitive right action of the discrete group $\pi_1(M,m)$ with equivariant local trivialisations, which is precisely the data of a [[Def - Principal G-Bundle|principal π₁(M,m)-bundle]]. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a connected smooth manifold with base point $m$.
>
> **Step 0 — preconditions.** By **Lemma 1**, $M$ is locally path-connected and semi-locally simply connected; these are the hypotheses under which the construction of the universal cover is legitimate, and they hold for every manifold.
>
> **Step 1 — existence as a topological universal cover.** By **Lemma 2**, the set $\tilde M$ of path-homotopy classes of paths from $m$, with the basic sets $U_{[\gamma]}$ over good neighbourhoods $U$, is a topological space and $q([\gamma]) = \gamma(1)$ is a covering map. By **Lemma 3**, $\tilde M$ is path-connected and $\pi_1(\tilde M, \tilde m) = \{1\}$, so $q \colon \tilde M \to M$ is a universal cover in the sense of [[Def - Universal Cover|the definition]]. This proves the existence clause of part (a).
>
> **Step 2 — smooth structure, Hausdorffness, local diffeomorphism, uniqueness.** We give $\tilde M$ charts by pulling back charts of $M$. Let $\mathcal A$ be a smooth atlas of $M$ each of whose chart domains $V$ is a *connected evenly covered* open set (refine any atlas by intersecting with the evenly covered sets of Step 1, using that they form a basis by Lemma 1). For a chart $(V, \phi)$ of $\mathcal A$ and each sheet $\tilde V$ over $V$, declare $(\tilde V,\; \phi \circ q|_{\tilde V})$ a chart of $\tilde M$; here $q|_{\tilde V} \colon \tilde V \to V$ is a homeomorphism by the covering property. These cover $\tilde M$. Two such charts $(\tilde V, \phi\circ q|_{\tilde V})$ and $(\tilde V', \psi\circ q|_{\tilde V'})$ have transition map, on the overlap,
> $$(\psi\circ q|_{\tilde V'})\circ(\phi\circ q|_{\tilde V})^{-1} = \psi\circ q \circ (q|_{\tilde V})^{-1}\circ\phi^{-1} = \psi\circ\phi^{-1} \quad (\text{since } q\circ(q|_{\tilde V})^{-1} = \operatorname{id} \text{ on } V\cap V'),$$
> a transition map of $M$, hence smooth. So the charts form a smooth atlas, and in it $q$ reads locally as $\phi^{-1}\circ(\phi\circ q|_{\tilde V}) = q|_{\tilde V}$ followed by identity in coordinates — explicitly $\phi\circ q|_{\tilde V}\circ (\phi\circ q|_{\tilde V})^{-1} = \operatorname{id}$ — so $q$ is a local diffeomorphism. *Hausdorffness:* given $\tilde x \neq \tilde y$, if $q(\tilde x)\neq q(\tilde y)$ separate them downstairs (M Hausdorff) and pull back through $q$; if $q(\tilde x) = q(\tilde y) = x$, then $\tilde x, \tilde y$ lie in different sheets of an evenly covered neighbourhood of $x$ (Lemma 2), which are disjoint open sets separating them. *Uniqueness of the smooth structure:* any smooth structure making $q$ a local diffeomorphism must have each $q|_{\tilde V}$ a diffeomorphism onto $(V,\phi)$, hence must contain the charts $\phi\circ q|_{\tilde V}$ up to smooth compatibility; so the structure is unique.
>
> **Step 3 — countability of $\pi_1$ and second countability of $\tilde M$.** By **Lemma 5**, $\pi_1(M,m)$ is countable; this is part (d). By **Lemma 4**, the fibre $q^{-1}(m) \cong \pi_1(M,m)$ is therefore countable, and since $M$ is connected all fibres have the same cardinality, so every fibre is countable. Now take a countable basis $\mathcal C$ of $M$ consisting of connected evenly covered open sets (possible: intersect a countable basis of $M$ with the evenly covered sets, which form a basis). For each $C \in \mathcal C$, $q^{-1}(C)$ is a disjoint union of countably many sheets (one per point of the countable fibre). The collection of all these sheets, over all $C \in \mathcal C$, is a countable family of open subsets of $\tilde M$, and it is a basis for $\tilde M$: given an open $O \subseteq \tilde M$ and $\tilde x \in O$, choose a sheet $\tilde V$ containing $\tilde x$ over some evenly covered $V$; $q(\tilde V \cap O)$ is open in $V$, pick $C \in \mathcal C$ with $q(\tilde x) \in C \subseteq q(\tilde V\cap O)$, and the sheet of $q^{-1}(C)$ through $\tilde x$ lies in $\tilde V\cap O \subseteq O$. Hence $\tilde M$ is second countable. Together with Step 2, $\tilde M$ is a smooth manifold. This completes part (a) except uniqueness.
>
> **Step 4 — uniqueness of the universal cover.** Let $q_i \colon \tilde M_i \to M$ ($i=1,2$) be simply connected coverings; fix $\tilde m_i \in q_i^{-1}(m)$. By the [[Thm - Lifting Criterion for Continuous Maps|lifting criterion]] (recalled in Lemma 6), applied with $Y = \tilde M_1$, $g = q_1$, target cover $q_2$, and the trivial inclusion $ (q_1)_*\pi_1(\tilde M_1,\tilde m_1) = \{1\} \subseteq (q_2)_*\pi_1(\tilde M_2,\tilde m_2)$, there is a unique continuous $h \colon \tilde M_1 \to \tilde M_2$ with $q_2\circ h = q_1$ and $h(\tilde m_1) = \tilde m_2$; symmetrically a unique $k \colon \tilde M_2 \to \tilde M_1$ with $q_1\circ k = q_2$ and $k(\tilde m_2) = \tilde m_1$. Then $k\circ h$ covers $q_1$ and fixes $\tilde m_1$, so $k\circ h = \operatorname{id}_{\tilde M_1}$ by uniqueness of lifts; likewise $h\circ k = \operatorname{id}_{\tilde M_2}$. Thus $h$ is a homeomorphism of coverings. When both $\tilde M_i$ carry the smooth structure of Step 2, $h$ is locally $h = (q_2|_{\text{sheet}})^{-1}\circ q_1$, a composition of local diffeomorphisms, hence a diffeomorphism. This proves the uniqueness clause of part (a).
>
> **Step 5 — the deck action (part b).** By **Lemma 6**, $\operatorname{Deck}(\tilde M/M)$ acts on $\tilde M$ freely, properly discontinuously, and transitively on each fibre, and by diffeomorphisms (Step 2 supplies the smooth structure invoked at the end of Lemma 6). It remains to identify the quotient. The deck group is a discrete group acting smoothly, freely, and properly discontinuously; by the [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|quotient-covering theorem]] — *if a discrete group $\Gamma$ acts smoothly and properly discontinuously on a manifold $N$, then $\Gamma\backslash N$ has a unique smooth structure making $N \to \Gamma\backslash N$ a smooth covering map* — the orbit space $\tilde M/\operatorname{Deck}(\tilde M/M)$ is a smooth manifold and the quotient projection $\pi \colon \tilde M \to \tilde M/\operatorname{Deck}$ is a smooth covering. Because $q$ is constant on deck orbits ($q\circ\varphi = q$) and, by fibrewise transitivity (Lemma 6(iii)), separates distinct orbits — two points with $q(\tilde x) = q(\tilde y)$ lie in one orbit — the map $q$ descends to a continuous bijection $\bar q \colon \tilde M/\operatorname{Deck} \to M$ with $\bar q\circ\pi = q$. Both $\pi$ and $q$ are local diffeomorphisms, so $\bar q$ is a local diffeomorphism; a bijective local diffeomorphism is a diffeomorphism. Hence $\tilde M/\operatorname{Deck}(\tilde M/M) \cong M$, completing part (b).
>
> **Step 6 — the fundamental group is the deck group and $q$ is a principal bundle (part c).** By **Lemma 7**, the prepending map $\Phi([\gamma])[\alpha] = [\gamma\cdot\alpha]$ is a group isomorphism $\Phi \colon \pi_1(M,m) \xrightarrow{\cong} \operatorname{Deck}(\tilde M/M)$, and the induced right action $\tilde x\cdot[\gamma] = \Phi([\gamma])^{-1}(\tilde x)$ makes $q \colon \tilde M \to M$ a principal $\pi_1(M,m)$-bundle for the discrete structure group $\pi_1(M,m)$. This is part (c). (The choice of $\tilde m = [c_m]$ is the base point $\tilde m \in q^{-1}(m)$; a different choice conjugates $\Phi$ by the corresponding deck transformation, which is the usual ambiguity of the isomorphism.)
>
> **Conclusion.** Parts (a)–(d) are established: (a) by Steps 1–4, (b) by Step 5, (c) by Step 6, (d) by Lemma 5 (used already in Step 3). Therefore every connected smooth manifold has a universal cover, the fundamental group acts on it as the deck group making the projection a principal $\pi_1$-bundle, and $\pi_1$ is countable. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Lie theory: the universal cover of a Lie group is a Lie group.** Let $G$ be a connected Lie group with universal cover $q \colon \tilde G \to G$. The theorem gives $\tilde G$ as a simply connected manifold with a deck action of $\pi_1(G)$. The exercise is to lift the multiplication $\mu \colon G\times G \to G$ to $\tilde\mu \colon \tilde G\times\tilde G \to \tilde G$ using the lifting criterion (the domain is simply connected), check the group axioms by uniqueness of lifts, and conclude $\pi_1(G)$ is a discrete central subgroup of $\tilde G$ with $\tilde G/\pi_1(G) \cong G$. This is non-obvious because it upgrades a purely topological construction to an algebraic one, and it is the mechanism behind $\operatorname{SU}(2) \to \operatorname{SO}(3)$ ([[Ex - SU(2) is the Universal Cover of SO(3)|the spin double cover]]) and $\mathbb{R}\to U(1)$.

**Riemannian geometry: developing map of a flat manifold.** Let $(M,g)$ be a connected flat Riemannian manifold, so the [[Thm - Local Triviality of Flat Connections|Levi-Civita connection is locally trivialisable]]. Pull the metric back to $\tilde M$ through the local diffeomorphism $q$; the deck group then acts by isometries, and the parallel transport of $\tilde M$ integrates to a *developing map* $\tilde M \to \mathbb{R}^n$ that intertwines the deck action with a representation $\pi_1(M) \to \operatorname{Isom}(\mathbb{R}^n)$. The exercise is to build this map and read off that flat compact manifolds are quotients of $\mathbb{R}^n$ by discrete groups of isometries. The theorem applies because it supplies exactly the principal $\pi_1$-bundle on which the developing map is $\pi_1$-equivariant; the non-obvious point is that flatness alone forces the global quotient structure.

**Complex geometry / number theory: modular curves.** The upper half-plane $\mathbb{H}$ is simply connected, and a torsion-free discrete subgroup $\Gamma \subseteq \operatorname{PSL}_2(\mathbb{R})$ acting freely and properly discontinuously makes $\mathbb{H} \to \Gamma\backslash\mathbb{H}$ the universal cover of the quotient Riemann surface, with $\pi_1(\Gamma\backslash\mathbb{H}) \cong \Gamma$ by part (c). The exercise is to identify the fundamental group of a modular or Shimura curve with its uniformising group and to deduce countability of that group directly from part (d). The theorem applies because the quotient is a manifold (surface) and the source group action is free properly discontinuous; the non-obvious content is that the abstract $\pi_1$ of the quotient equals the concrete matrix group $\Gamma$.

---

# Bridges

- **[[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|Flat connections and monodromy representations]].** This is the direct sequel: given the principal $\pi_1(M,m)$-bundle $q \colon \tilde M \to M$ of part (c) and a homomorphism $\rho \colon \pi_1(M,m) \to G$, the [[Def - Associated Bundle|associated bundle]] $\tilde M \times_\rho G$ is a principal $G$-bundle over $M$ with a canonical flat connection of monodromy $\rho$. Every flat bundle arises so, and the resulting bijection $\{\text{flat bundles}\}/\!\cong \;\leftrightarrow\; \operatorname{Hom}(\pi_1, G)/\text{conj}$ is the central theorem of §5.4. The present page is the geometric substrate on which that construction is carried out.

- **[[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|The quotient-covering theorem]] (chapter I).** That theorem runs the construction in the *opposite* direction: from a free properly discontinuous action it produces a covering. This page produces, from an arbitrary connected manifold, a free properly discontinuous action (of $\operatorname{Deck}$) whose quotient is the manifold, and Step 5 invokes the quotient theorem to identify $\tilde M/\operatorname{Deck}$ with $M$ as a smooth manifold. The two together say: connected manifolds and free properly discontinuous actions of $\pi_1$ on simply connected manifolds are two views of the same data.

- **The torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$.** The translation action of $\mathbb{Z}^n$ on the simply connected $\mathbb{R}^n$ is free and properly discontinuous, so by uniqueness (part a) $\mathbb{R}^n \to T^n$ *is* the universal cover and $\pi_1(T^n) \cong \mathbb{Z}^n$ (part c). This is the running example of the chapter and the basis of [[Ex - The Universal Cover of the Circle and of the Torus|the torus exercise]] and of the flat-$U(1)$-connection computation $\mathcal{R}(T^n; U(1)) = U(1)^n$.

- **The orientation double cover.** For a connected manifold $M$ the first Stiefel–Whitney class defines a homomorphism $w_1 \colon \pi_1(M,m) \to \mathbb{Z}/2$, and the associated bundle of the sign representation $\mathbb{Z}/2 \hookrightarrow O(1)$ produces the **orientation double cover** $M^{\mathrm{or}} \to M$, a two-sheeted covering that is connected precisely when $M$ is non-orientable. This is the simplest non-trivial flat real line bundle and the simplest place where the deck action of part (b) is visibly the group $\mathbb{Z}/2$ acting by the antipode on fibres.

---

# Unlocked by This

> [!tip] Flat bundles as bundles with discrete structure group *(from Gauge Theory)*
> Because $q \colon \tilde M \to M$ is a principal bundle with the *discrete* group $\pi_1(M,m)$, every associated bundle $\tilde M \times_\rho V$ inherits transition functions that are locally *constant*. A flat bundle is exactly a bundle whose structure group has been reduced to a discrete group, and this is the precise sense in which "flat = locally the product connection" of [[Thm - Local Triviality of Flat Connections|the local-triviality page]] meets "flat = a representation of $\pi_1$".

> [!tip] Countable fundamental groups and moduli compactness *(from Gauge Theory)*
> Part (d) — countability of $\pi_1$ — is what makes $\operatorname{Hom}(\pi_1(M,m), G)$ a *countable* product of copies of the compact group $G$, so that a diagonal-subsequence argument gives sequential compactness of the representation variety without the general Tychonoff theorem, on [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|the compactness page]].
