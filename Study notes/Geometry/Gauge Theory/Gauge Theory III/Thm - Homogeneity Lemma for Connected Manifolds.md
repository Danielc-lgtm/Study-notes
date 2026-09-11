---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Fundamental Theorem on Flows"
  - "Ex - Compactly Supported Vector Fields are Complete"
  - "Thm - Existence of Smooth Bump Functions"
  - "Def - Diffeomorphism"
  - "Def - Smooth Vector Field"
  - "Def - Flow of a Vector Field"
  - "Def - Connected Space"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, manifolds are smooth, Hausdorff, and second countable, and "smooth" means $C^\infty$, as agreed for the whole series; $M$ denotes a connected such manifold, of dimension $n = \dim M$. We write $B = \{x \in \mathbb{R}^n : |x| < 1\}$ for the open unit ball, $\bar B_\rho = \{x \in \mathbb{R}^n : |x| \le \rho\}$ for the closed ball of radius $\rho$, and $[p, q] = \{(1-s)p + sq : s \in [0, 1]\}$ for the closed straight segment joining $p, q \in \mathbb{R}^n$. A [[Def - Diffeomorphism|diffeomorphism]] is a smooth bijection with smooth inverse; $\operatorname{Diff}(M)$ is the group of diffeomorphisms of $M$ under composition. For a [[Def - Smooth Vector Field|smooth vector field]] $X$ on a manifold, $\operatorname{supp} X = \overline{\{x : X_x \neq 0\}}$ is its support, and $\Phi \colon \mathcal{D} \to M$ is its maximal [[Def - Flow of a Vector Field|flow]], with $\Phi_t(x) = \Phi(t, x)$.

A **smooth isotopy of $M$** is a smooth map $H \colon M \times [0, 1] \to M$ such that each $H_t := H(\cdot, t)$ is a diffeomorphism of $M$ and $H_0 = \operatorname{id}_M$; it is an isotopy **from the identity to $h$** when $H_1 = h$, and it **fixes a subset $K \subseteq M$ pointwise** when $H_t(x) = x$ for all $x \in K$ and all $t \in [0, 1]$. A diffeomorphism $h$ is **smoothly isotopic to the identity** when such an $H$ with $H_1 = h$ exists; the notion is the diffeomorphism-valued refinement of a [[Def - Smooth Homotopy of Maps|smooth homotopy]]. We say $H$ is **supported in** a set $C \subseteq M$ when $H_t(x) = x$ for every $x \in M \setminus C$ and every $t$; a supported isotopy fixes pointwise everything outside its support.

A **coordinate ball** at a point $q$ is the preimage $\psi^{-1}(B')$ of an open Euclidean ball $B'$ under a [[Def - Smooth Map between Manifolds|smooth]] chart $\psi \colon V \to \mathbb{R}^n$ defined on an open set $V$, chosen so that $q \in \psi^{-1}(B')$; a **coordinate disc** is an open subset $D \subseteq M$ diffeomorphic to $\mathbb{R}^n$ (equivalently to an open ball). The full symbol registry for the chapter is on the parent page [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]].

> [!warning] Convention: sources
> This page belongs to §3.5, the chapter's kit of smooth-topological tools. It is drawn not from Haydys or Bär but from Milnor, *Topology from the Differentiable Viewpoint*, §4 (the "Homogeneity Lemma"); the section exists because the clutching and generic-section arguments the classification of §3.6 needs rely on being able to slide points around a manifold by an ambient isotopy, and the sources use this freely without proof. All conventions are the standing series conventions above.

---

# Statement

> **Homogeneity Lemma (Milnor, TDV §4).** Let $M$ be a connected manifold, let $x, y \in M$, and let $K \subseteq M \setminus \{x, y\}$ be a closed subset such that $M \setminus K$ is connected. Then there is a diffeomorphism $h \colon M \to M$, smoothly isotopic to the identity through diffeomorphisms fixing $K$ pointwise, with $h(x) = y$.

> **Corollary (gathering finitely many points).** Let $M$ be a connected manifold of dimension $n \ge 2$, let $\{p_1, \dots, p_m\} \subseteq M$ be a finite set of distinct points, and let $D \subseteq M$ be a nonempty coordinate disc. Then there is a diffeomorphism $h \colon M \to M$, smoothly isotopic to the identity, with $h(p_i) \in D$ for every $i$.

The corollary is what the rest of the chapter uses: it lets one assume, after an isotopy, that all the zeros of a generic section, or all the points where a bundle fails to be trivial, sit inside a single coordinate disc, so that the bundle is trivial off that disc and the clutching description applies.

---

# Motivation

A connected manifold has no distinguished points: geometrically, one point is the same as any other. The homogeneity lemma is the statement that makes this slogan precise and, more importantly, *effective* — not merely "there is an abstract symmetry exchanging $x$ and $y$", but "there is a concrete diffeomorphism, deformable to the identity, that carries $x$ to $y$ while leaving a prescribed closed set untouched". The deformability to the identity is the operative clause: it means the diffeomorphism changes nothing that an isotopy invariant can see. Pulling a bundle, a cohomology class, or a section back along $h$ therefore changes it by an isomorphism, and one may freely move the interesting points of a problem to wherever they are most convenient.

The problem the lemma solves in this chapter is the following. When one perturbs a section of a vector bundle to be transverse to the zero section — see [[Thm - Generic Sections are Transverse to the Zero Section|Generic Sections are Transverse to the Zero Section]] — the section acquires a finite set of isolated, nondegenerate zeros, scattered across the base. To read off a bundle invariant from these zeros, or to exhibit the bundle as built by a single clutching function, one wants them all in one coordinate disc, so that the bundle is trivial on the complement of that disc and everything of interest is localized. There is no reason a generic section should oblige by putting its zeros in one place. The homogeneity lemma supplies the missing move: slide the zeros together by an ambient isotopy, which — being isotopic to the identity — does not change the isomorphism class of the bundle. The lemma is the hinge between "the zeros exist and are finite" and "the zeros can be assumed to sit in one disc".

The closed set $K$ that must be fixed is not decoration. When the points are moved one at a time, the ones already parked in the disc must be held in place while the next is brought over; they constitute the $K$ of the next step. This is exactly why the statement is proved in the relative form "fixing $K$" rather than the bare form "there exists $h$ with $h(x) = y$", and why the hypothesis is connectedness of $M \setminus K$ rather than of $M$: the isotopy must be able to travel from $x$ to $y$ without ever crossing $K$.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is mild — a connected manifold and two points with a connected complement of the forbidden set — so the skill is recognizing when a problem is secretly asking for the homogeneity lemma.

The first disguised source is **a demand that two configurations of points be identified up to a diffeomorphism deformable to the identity**. Whenever a construction depends a priori on *where* a finite set of marked points sits, and one wants to prove the construction is independent of that placement, the bridge is: any two ordered tuples of distinct points in a connected manifold of dimension at least two are carried one to the other by a diffeomorphism isotopic to the identity (the corollary, applied to bring both tuples to a standard position inside a chart). The non-obvious step is realizing that "independent of the placement of the points" is a homogeneity statement rather than a computation. *Example problem:* show that the local index of an isolated, nondegenerate zero of a section does not depend on which chart is used to compute it, by first isotoping the zero to the chart's origin.

The second disguised source is **a construction that can only be performed inside a single chart but must be made to work at a global point**. Many local models — a bump, a plateau, a standard clutching function on a boundary sphere — are written down in Euclidean coordinates and then need to be installed near an arbitrary point of $M$. The bridge is that the homogeneity lemma lets you assume, after an isotopy that changes nothing isotopy-invariant, that the point in question is the centre of your favourite coordinate ball. The non-obviousness is that the isotopy is doing genuine work: it is what licenses "without loss of generality the point is at the origin". *Example problem:* prove that every principal $G$-bundle over a sphere $S^n$ with $G$ connected is trivial over the complement of a single point, by isotoping the finitely many points of non-triviality together — the mechanism behind [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]].

The third disguised source is **a claim of transitivity for the identity component of the diffeomorphism group**. The statement "$\operatorname{Diff}_0(M)$ acts transitively on $M$", and its relative and multi-point refinements, are exactly the homogeneity lemma and its corollary. Whenever a proof wants to reduce to a single orbit of this action — for instance to define an invariant by its value at one point and argue it is the same everywhere — the bridge is the lemma. The non-obviousness is that transitivity of an infinite-dimensional group is not obvious from group theory and must be supplied by a construction; the construction is the flow of a bump-modulated field. *Example problem:* show that a smooth measure of total mass one on a connected manifold is carried to any other such measure by a diffeomorphism (Moser's theorem), whose first step is the homogeneity that lets one work locally.

**Targets (Output Amplification)**

The bare conclusion is one diffeomorphism carrying $x$ to $y$. Combined with other results it becomes a workhorse.

Combine the corollary with **the generic-section theorem**. The extra ingredient $C$ is the existence of a section transverse to the zero section with finitely many zeros ([[Thm - Generic Sections are Transverse to the Zero Section|Generic Sections are Transverse to the Zero Section]]). The payoff $E$ is that, after an ambient isotopy, all the zeros lie in one coordinate disc $D$, so the section is nowhere zero on $M \setminus D$; hence the bundle is trivial over $M \setminus D$ (a nowhere-zero section of a line bundle trivializes it, and for higher rank one completes the section to a frame off the disc after a further perturbation). This is the statement "an $SU(2)$-bundle over a four-manifold is trivial off a point" that §3.6 turns into a clutching classification.

Combine the corollary with **the clutching construction**. The extra ingredient $C$ is that a bundle trivial over $M \setminus D$ and over $D$ is determined by a clutching map on the boundary sphere of $D$ ([[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching theorem]]). The payoff $E$ is a bijection between isomorphism classes of such bundles and homotopy classes of clutching maps, which is the engine of the classification of $U(1)$- and $SU(2)$-bundles. Homogeneity is what guarantees the hypothesis of the clutching theorem — that the non-triviality is confined to one disc — can always be met.

Combine the lemma with **the homotopy invariance of bundles**. The extra ingredient $C$ is that a diffeomorphism isotopic to the identity pulls a bundle back to an isomorphic bundle ([[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|homotopic maps pull back isomorphic bundles]], part (d)). The payoff $E$ is that all the sliding the lemma performs is free of charge at the level of isomorphism classes: any invariant of bundles that is constant under isomorphism is unchanged by the homogeneity isotopies, so one may localize freely without corrupting the invariant one is trying to compute.

---

# Why Is It True

**The mechanism in one sentence: a point can be pushed to any nearby point by flowing along a constant vector field cut off to a coordinate ball, "reachability by such a push" is an open condition, and on a connected manifold an open-and-closed nonempty condition is everything.**

Unpack this in three movements.

*Local sliding.* Inside a chart, identify a neighbourhood with the unit ball $B \subseteq \mathbb{R}^n$. To move a point $p$ to a point $q$ of the ball, take the constant vector field pointing from $p$ to $q$, namely $x \mapsto (q - p)$, and multiply it by a bump function $\varphi$ that equals $1$ on the segment $[p, q]$ and vanishes outside the ball. The resulting field $X = \varphi \cdot (q - p)$ is compactly supported, hence complete, and its flow is defined for all time and is the identity outside the ball. The integral curve starting at $p$ moves at unit speed straight along the segment (because $\varphi = 1$ there), so at time one it has arrived exactly at $q$. The time-one flow is a diffeomorphism carrying $p$ to $q$, equal to the identity outside the ball, and the flow itself for times in $[0, 1]$ is the isotopy to the identity. The bump function is doing two jobs at once: it stops the field at the edge of the ball, which makes the diffeomorphism extend by the identity to the whole manifold; and it makes the field constant on the segment, which makes the point travel in a straight line and arrive on time.

*Openness.* Say $x$ can **reach** $z$ if some ambient isotopy fixing $K$ and supported off $K$ carries $x$ to $z$. The local sliding shows: if $x$ can reach $z$, then $x$ can reach every point of a whole coordinate ball around $z$ (compose the isotopy reaching $z$ with a local slide from $z$ to the nearby target). So the set of points reachable from $x$ is open. It is also, by the same reasoning applied to its complement, closed — for if a point were on the boundary of the reachable set, a local slide from it would reach into the reachable set, and reachability is symmetric and transitive, so the boundary point would itself be reachable. Reachability is an equivalence relation, so the manifold (with $K$ deleted, so that the slides never touch $K$) is partitioned into open reachability classes.

*Connectedness closes the argument.* A partition of a connected space into nonempty open sets has only one block. Since $x$ and $y$ both lie in $M \setminus K$, which is connected by hypothesis, they lie in the same block: $x$ reaches $y$. The whole content of the lemma is that a purely local ability — to nudge a point a little way in a chart — propagates to a global ability along any connected path, and the propagation costs nothing at the level of isotopy because each nudge is itself isotopic to the identity.

The dimension hypothesis $n \ge 2$ enters only in the corollary, and only through one fact: removing finitely many points from a connected manifold of dimension at least two leaves it connected, because a punctured Euclidean ball $\mathbb{R}^n \setminus \{0\}$ is connected when $n \ge 2$. In dimension one this fails — the line minus a point falls apart — and indeed one cannot slide a point past another on a curve.

---

# What Makes This Hard

The conceptual skeleton is short, but three points require care. First, the relative clause: the isotopy must fix $K$ pointwise, which is arranged by working in $M \setminus K$ and only ever using coordinate balls disjoint from $K$; the correct hypothesis is therefore connectedness of $M \setminus K$, not of $M$, and forgetting the difference produces a false statement (one cannot cross a wall of forbidden points). Second, the concatenation of isotopies used for transitivity is not literally smooth at the join unless each isotopy is first reparametrized to be constant in time near its endpoints; this is a standard technical adjustment but must be stated, not assumed. Third, in the corollary the bookkeeping of which points are held fixed at each step is essential: the points already moved into the disc become part of $K$ for the next step, and one must verify that the point currently being moved and its target both avoid that $K$, and that $M \setminus K$ is still connected — the last of which is exactly where dimension at least two is spent.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Build one local move — a diffeomorphism of a ball, identity near the boundary and isotopic to the identity, carrying one interior point to another — as the time-one flow of a bump-cut constant field. Promote it to a global statement by defining "reachable by a $K$-fixing isotopy" on $M \setminus K$, showing this relation is an equivalence relation with open classes, and invoking connectedness of $M \setminus K$. For the corollary, move the points one at a time into the disc, freezing the ones already placed, using that a connected manifold of dimension at least two stays connected after deleting a finite set.

**Subgoal decomposition:**

1. **Local isotopy in a ball.** For $p, q$ in the open unit ball, produce a diffeomorphism of $\mathbb{R}^n$, equal to the identity outside the ball and isotopic to the identity rel the complement of the ball, carrying $p$ to $q$.
   - *Hint:* Flow the field $\varphi(x)\,(q - p)$ with $\varphi$ a bump equal to $1$ on $[p, q]$ and supported in the ball; the integral curve from $p$ is the straight segment traversed at unit speed.
   - *Why needed:* It is the only place analysis enters; everything global is assembled from it.

2. **Reachability is an equivalence relation with open classes.** On $M \setminus K$, declare $p \approx q$ when a smooth isotopy of $M$ supported in a compact subset of $M \setminus K$ carries $p$ to $q$; show reflexivity, symmetry, transitivity, and that each class is open.
   - *Hint:* Openness is subgoal 1 transported through a chart; transitivity needs the constant-near-endpoints reparametrization.
   - *Why needed:* An equivalence relation with open classes on a connected space has one class.

3. **Main statement.** Apply subgoal 2 with the connected space $M \setminus K$ to conclude $x \approx y$, and read off $h$ and the isotopy.
   - *Hint:* Support in $M \setminus K$ forces the isotopy to fix $K$.
   - *Why needed:* This is the theorem.

4. **Punctured connectivity.** Show that a connected manifold of dimension $n \ge 2$ minus a finite set is connected.
   - *Hint:* One point at a time; a coordinate ball's puncture $\mathbb{R}^n \setminus \{0\}$ is connected for $n \ge 2$, and it glues the two hypothetical halves together.
   - *Why needed:* It is the hypothesis of the main statement at each step of the corollary.

5. **Corollary.** Move the points into the disc one at a time, adding each parked point to the fixed set.
   - *Hint:* At step $i$ freeze $\{q_1, \dots, q_{i-1}\} \cup \{p_{i+1}, \dots, p_m\}$ and apply the main statement.
   - *Why needed:* This is the form the chapter uses.

---

# Lemma Decomposition

> [!note]- Lemma 1: Local isotopy inside a ball
> **Statement:** Let $B = \{x \in \mathbb{R}^n : |x| < 1\}$ and let $p, q \in B$. There is a smooth isotopy $\Phi \colon \mathbb{R}^n \times [0, 1] \to \mathbb{R}^n$ with $\Phi_0 = \operatorname{id}$, each $\Phi_t$ a diffeomorphism, $\Phi_1(p) = q$, and $\Phi_t(x) = x$ for every $x \notin B$ and every $t \in [0, 1]$. In particular $\Phi_1$ is a diffeomorphism of $\mathbb{R}^n$ equal to the identity outside $B$, isotopic to the identity through diffeomorphisms equal to the identity outside $B$, and carrying $p$ to $q$.
>
> **Hint:** Flow the compactly supported field $X(x) = \varphi(x)\,(q - p)$, where $\varphi$ is a bump equal to $1$ on $[p, q]$ and supported in $B$; the curve from $p$ runs straight along $[p, q]$ at unit speed.
>
> **Why needed:** It is the atomic move; the global statement is these moves chained along a connected path.
>
> > [!note]- Full proof
> > **Choose the bump function.** The closed segment $[p, q] = \{(1-s)p + sq : s \in [0, 1]\}$ is a compact subset of the open ball $B$, so there is $\rho < 1$ with $[p, q] \subseteq \bar B_\rho = \{x : |x| \le \rho\}$ (take $\rho = \max_{s \in [0,1]} |(1-s)p + sq| < 1$, the maximum of a continuous function on the compact segment, which is strictly less than $1$ because the segment lies in the open ball). The set $\bar B_\rho$ is closed and the open ball $B$ satisfies $\bar B_\rho \subseteq B$, so by the existence of smooth bump functions —
> > > [!note]- Restatement: [[Thm - Existence of Smooth Bump Functions|Existence of Smooth Bump Functions]]
> > > For any closed subset $A$ of a smooth manifold and any open set $U \supseteq A$, there is a smooth function $\psi \colon M \to [0, 1]$ with $\psi \equiv 1$ on $A$ and $\operatorname{supp} \psi \subseteq U$.
> >
> > applied with $A = \bar B_\rho$ and $U = B$ on the manifold $\mathbb{R}^n$, there is a smooth $\varphi \colon \mathbb{R}^n \to [0, 1]$ with $\varphi \equiv 1$ on $\bar B_\rho$ and $\operatorname{supp} \varphi \subseteq B$. Since $[p, q] \subseteq \bar B_\rho$ we have $\varphi \equiv 1$ on $[p, q]$, and since $\operatorname{supp} \varphi \subseteq B$ we have $\varphi(x) = 0$ for every $x \notin B$ (such an $x$ lies outside the support).
> >
> > **Define and flow the field.** Set $c := q - p \in \mathbb{R}^n$ and define the smooth vector field $X(x) := \varphi(x)\, c$ on $\mathbb{R}^n$. Its support satisfies $\operatorname{supp} X \subseteq \operatorname{supp} \varphi \subseteq B$ (where $\varphi = 0$, the field vanishes), and $\operatorname{supp} \varphi$ is closed and contained in the bounded set $B$, hence compact. Therefore $X$ has compact support, and by the completeness of compactly supported fields —
> > > [!note]- Restatement: [[Ex - Compactly Supported Vector Fields are Complete|Compactly Supported Vector Fields are Complete]]
> > > A smooth vector field with compact support on a smooth manifold is complete: its maximal flow domain is all of $\mathbb{R} \times M$, so every maximal integral curve is defined for all $t \in \mathbb{R}$.
> >
> > the maximal flow of $X$ is defined on all of $\mathbb{R} \times \mathbb{R}^n$. By the fundamental theorem on flows —
> > > [!note]- Restatement: [[Thm - Fundamental Theorem on Flows|Fundamental Theorem on Flows]]
> > > A smooth vector field $X$ on $M$ has a unique smooth maximal flow $\Phi \colon \mathcal{D} \to M$ with $\Phi_0 = \operatorname{id}$, whose infinitesimal generator is $X$; for each $t$, the time-$t$ map $\Phi_t \colon M_t \to M_{-t}$ is a diffeomorphism with inverse $\Phi_{-t}$, where $M_t = \{x : (t, x) \in \mathcal{D}\}$.
> >
> > this flow $\Phi$ is smooth on $\mathbb{R} \times \mathbb{R}^n$, and each $\Phi_t \colon \mathbb{R}^n \to \mathbb{R}^n$ is a diffeomorphism (with $M_t = M_{-t} = \mathbb{R}^n$ by completeness), with $\Phi_0 = \operatorname{id}$.
> >
> > **The field vanishes outside $B$, so the flow fixes the exterior.** For $x \notin B$ we have $X(x) = \varphi(x) c = 0$, so the constant curve $t \mapsto x$ is an integral curve of $X$ through $x$; by the uniqueness clause of the fundamental theorem on flows it is *the* maximal integral curve, whence $\Phi_t(x) = x$ for all $t$. Thus $\Phi_t(x) = x$ for every $x \notin B$ and every $t$.
> >
> > **The point $p$ arrives at $q$ at time one.** Let $\gamma(t) := \Phi_t(p)$, the integral curve of $X$ with $\gamma(0) = p$, so $\gamma'(t) = X(\gamma(t)) = \varphi(\gamma(t))\, c$ (definition of an integral curve and of $X$). Because $\gamma'(t)$ is always a scalar multiple of the fixed vector $c$, the curve stays on the ray $p + \mathbb{R}_{\ge 0}\, c$; write $\gamma(t) = p + s(t)\, c$ with $s(0) = 0$, where $s(t) \ge 0$ is smooth (it is the $c$-coordinate of $\gamma(t) - p$ divided by $|c|^2$, hence smooth in $t$; if $c = 0$ then $p = q$ and $\Phi_t \equiv \operatorname{id}$ already works, so assume $c \neq 0$). Substituting into the differential equation, $s'(t)\, c = \varphi\big(p + s(t) c\big)\, c$, so $s'(t) = \varphi\big(p + s(t) c\big)$ (cancelling the nonzero $c$). For $s \in [0, 1]$ the point $p + s c = (1 - s)p + s q$ lies on the segment $[p, q]$, where $\varphi \equiv 1$; hence as long as $s(t) \in [0, 1]$ we have $s'(t) = 1$. Since $s(0) = 0$ and $s' \equiv 1$ while $s \in [0,1]$, the unique solution is $s(t) = t$ on $[0, 1]$, so $\gamma(1) = p + 1 \cdot c = p + (q - p) = q$. Therefore $\Phi_1(p) = q$.
> >
> > **Assemble the isotopy.** Restrict $\Phi$ to $\mathbb{R}^n \times [0, 1]$. It is smooth, $\Phi_0 = \operatorname{id}$, each $\Phi_t$ is a diffeomorphism, $\Phi_t(x) = x$ for $x \notin B$, and $\Phi_1(p) = q$. This is the required isotopy, and $\Phi_1$ is the required diffeomorphism. $\blacksquare$

> [!note]- Lemma 2: Reachability is an equivalence relation with open classes
> **Statement:** Let $N$ be a smooth manifold and $M \supseteq N$ a manifold containing $N$ as an open subset. For $p, q \in N$, write $p \approx q$ when there exists a smooth isotopy $H \colon M \times [0, 1] \to M$ with $H_0 = \operatorname{id}_M$, each $H_t$ a diffeomorphism of $M$, $H_1(p) = q$, and a compact set $C \subseteq N$ with $H_t(x) = x$ for all $x \in M \setminus C$ and all $t$ ("$H$ is supported in $C$"). Then $\approx$ is an equivalence relation on $N$, and each equivalence class is open in $N$.
>
> **Hint:** Reflexivity is the constant isotopy; symmetry uses $G_t = H_{1-t} \circ H_1^{-1}$; transitivity concatenates two isotopies after reparametrizing them to be constant near their endpoints; openness is Lemma 1 transported through a chart.
>
> **Why needed:** An equivalence relation with open classes on a connected space has a single class; that is how connectedness of $N$ yields transitivity of the sliding action.
>
> > [!note]- Full proof
> > Throughout, "supported in $C$" for $C \subseteq N$ compact means $H_t = \operatorname{id}$ off $C$; note that any $H$ supported in $C \subseteq N$ fixes $M \setminus N$ pointwise, and in particular fixes any set disjoint from $N$.
> >
> > **Fix a reparametrization tool.** Choose once and for all a smooth nondecreasing function $\tau \colon [0, 1] \to [0, 1]$ with $\tau \equiv 0$ on $[0, \tfrac14]$ and $\tau \equiv 1$ on $[\tfrac34, 1]$ (for instance $\tau = \beta / (\beta + \tilde\beta)$ built from bump functions; its existence is a one-variable case of [[Thm - Existence of Smooth Bump Functions|the bump function theorem]]). For any isotopy $H$, the reparametrized isotopy $\hat H_t := H_{\tau(t)}$ is smooth, has the same endpoints ($\hat H_0 = H_0$, $\hat H_1 = H_1$), the same support, and is *constant in $t$* near $t = 0$ and near $t = 1$. Replacing every isotopy below by its reparametrization, we may and do assume all isotopies are constant in time near their endpoints; this makes every concatenation smooth at the join.
> >
> > **Reflexivity.** The constant isotopy $H_t = \operatorname{id}_M$ is supported in the empty set (or any point of $N$) and gives $p \approx p$.
> >
> > **Symmetry.** Suppose $p \approx q$ via $H$ supported in $C \subseteq N$, with $H_1(p) = q$. Define $G_t := H_{1-t} \circ H_1^{-1}$. Then $G$ is smooth (composition of the smooth flow-family with the fixed diffeomorphism $H_1^{-1}$), $G_0 = H_1 \circ H_1^{-1} = \operatorname{id}_M$, each $G_t$ is a diffeomorphism, and $G_1 = H_0 \circ H_1^{-1} = H_1^{-1}$, so $G_1(q) = H_1^{-1}(q) = p$ (since $H_1(p) = q$). For support: each $H_s$ is the identity off $C$, hence so is $H_1^{-1}$ (a bijection equal to the identity off $C$ has inverse equal to the identity off $C$), and a composition of two maps each equal to the identity off $C$ is equal to the identity off $C$; thus $G$ is supported in $C \subseteq N$. Hence $q \approx p$.
> >
> > **Transitivity.** Suppose $p \approx q$ via $H$ supported in $C_1 \subseteq N$ and $q \approx r$ via $H'$ supported in $C_2 \subseteq N$, both constant near their endpoints, with $H_1(p) = q$ and $H'_1(q) = r$. Define
> > $$K_t := \begin{cases} H_{2t}, & t \in [0, \tfrac12], \\ H'_{2t - 1} \circ H_1, & t \in [\tfrac12, 1]. \end{cases}$$
> > At $t = \tfrac12$ the two formulas agree: the first gives $H_1$, the second gives $H'_0 \circ H_1 = \operatorname{id} \circ H_1 = H_1$. Because $H$ is constant near $t = 1$ and $H'$ is constant near $t = 0$, both pieces are constant in $t$ near $t = \tfrac12$, so $K$ is smooth across the join; it is smooth on each half by construction. Each $K_t$ is a diffeomorphism, $K_0 = H_0 = \operatorname{id}_M$, and $K_1 = H'_1 \circ H_1$, so $K_1(p) = H'_1(H_1(p)) = H'_1(q) = r$. For support: on $[0, \tfrac12]$, $K_t$ is the identity off $C_1$; on $[\tfrac12, 1]$, $K_t = H'_{2t-1} \circ H_1$ is the identity off $C_1 \cup C_2$ (a point outside $C_1 \cup C_2$ is fixed by $H_1$, landing outside $C_2$ — indeed it is not moved, so it stays outside $C_2$ — and then fixed by $H'_{2t-1}$). Thus $K$ is supported in the compact set $C_1 \cup C_2 \subseteq N$, and $p \approx r$.
> >
> > **Openness of classes.** Let $p \in N$ and let $[p] = \{q \in N : p \approx q\}$ be its class. Fix $q \in [p]$; we produce an open neighbourhood of $q$ inside $[p]$. Since $N$ is a manifold and open in $M$, there is a chart $\psi \colon V \to \mathbb{R}^n$ with $q \in V \subseteq N$, $\psi(V) = \mathbb{R}^n$, and $\psi(q) = 0$ (translate a chart so its centre maps to the origin). Let $W := \psi^{-1}(B)$, an open neighbourhood of $q$ with $W \subseteq V \subseteq N$; we claim $W \subseteq [p]$. Take any $q' \in W$ and set $q'' := \psi(q') \in B$. By Lemma 1 (with $p := 0$ and $q := q''$, both in $B$) there is a smooth isotopy $\Phi \colon \mathbb{R}^n \times [0,1] \to \mathbb{R}^n$, each $\Phi_t$ a diffeomorphism, $\Phi_0 = \operatorname{id}$, $\Phi_t = \operatorname{id}$ outside $B$, and $\Phi_1(0) = q''$. Transport it to $M$ by
> > $$L_t(x) := \begin{cases} \psi^{-1}\big(\Phi_t(\psi(x))\big), & x \in V, \\ x, & x \in M \setminus \psi^{-1}(\bar B_{1/2}), \end{cases}$$
> > where the two definitions agree on the overlap $V \setminus \psi^{-1}(\bar B_{1/2})$ because $\Phi_t$ is the identity outside $B \supseteq \bar B_{1/2}$, so $\psi^{-1}(\Phi_t(\psi(x))) = \psi^{-1}(\psi(x)) = x$ there. The two open sets $V$ and $M \setminus \psi^{-1}(\bar B_{1/2})$ cover $M$ (a point not in $V$ is certainly not in $\psi^{-1}(\bar B_{1/2}) \subseteq V$), and $L_t$ is smooth on each and agrees on the overlap, so $L_t$ is a well-defined smooth map, a diffeomorphism (with inverse defined the same way from $\Phi_t^{-1}$), and $L$ is smooth in $(x, t)$. We have $L_0 = \operatorname{id}_M$ and $L_1(q) = \psi^{-1}(\Phi_1(\psi(q))) = \psi^{-1}(\Phi_1(0)) = \psi^{-1}(q'') = q'$. Finally $L$ is supported in the compact set $\psi^{-1}(\bar B_\rho)$ for the $\rho < 1$ of Lemma 1's construction, which lies in $V \subseteq N$; hence $q \approx q'$ (via $L$), so by symmetry and transitivity applied to $p \approx q \approx q'$ we get $p \approx q'$, i.e. $q' \in [p]$. Thus $W \subseteq [p]$, and $[p]$ is open. $\blacksquare$

> [!note]- Lemma 3: A connected manifold of dimension at least two minus a finite set is connected
> **Statement:** Let $N$ be a connected manifold with $\dim N = n \ge 2$, and let $F \subseteq N$ be a finite subset. Then $N \setminus F$ is connected.
>
> **Hint:** Delete one point at a time; a punctured coordinate ball $\mathbb{R}^n \setminus \{0\}$ is connected for $n \ge 2$ and glues any hypothetical decomposition of $N \setminus \{a\}$ back together.
>
> **Why needed:** It is the hypothesis "$M \setminus K$ connected" of the main statement at each step of the corollary, where $K$ is the growing finite set of frozen points.
>
> > [!note]- Full proof
> > **Reduce to one point.** We induct on the number of points $k = |F|$. For $k = 0$ there is nothing to prove. Assume $N \setminus F'$ is connected for every $(k-1)$-point subset $F'$, and let $F = \{a_1, \dots, a_k\}$. Then $N' := N \setminus \{a_1, \dots, a_{k-1}\}$ is connected by the inductive hypothesis, it is an open subset of $N$ hence a manifold of the same dimension $n \ge 2$, and $N \setminus F = N' \setminus \{a_k\}$. So it suffices to prove: *deleting a single point from a connected manifold of dimension $n \ge 2$ leaves it connected.*
> >
> > **The punctured ball is connected.** First, $\mathbb{R}^n \setminus \{0\}$ is path connected for $n \ge 2$, hence connected. Given $u, v \in \mathbb{R}^n \setminus \{0\}$: if $0$ does not lie on the segment $[u, v]$, the straight path $t \mapsto (1-t)u + tv$ joins them in $\mathbb{R}^n \setminus \{0\}$; if $0 \in [u, v]$, then $u$ and $v$ are negative multiples of each other (the origin is an interior point of the segment only when the endpoints point in opposite directions), so choose a vector $w \neq 0$ not proportional to $u$ — possible because $n \ge 2$ gives a second independent direction — and note that neither $[u, w]$ nor $[w, v]$ contains $0$ (the origin lies on a segment only between antipodal directions, and $w$ is proportional to neither $u$ nor $v$), so concatenating the two straight paths joins $u$ to $v$ off the origin. Hence $\mathbb{R}^n \setminus \{0\}$ is connected.
> >
> > **Glue.** Let $L$ be a connected manifold of dimension $n \ge 2$ and $a \in L$. Suppose, for contradiction, that $L \setminus \{a\}$ is disconnected: $L \setminus \{a\} = U \sqcup V$ with $U, V$ nonempty, disjoint, and open in $L \setminus \{a\}$. Because $L \setminus \{a\}$ is open in $L$, both $U$ and $V$ are open in $L$. Choose a coordinate ball at $a$: a chart $\psi \colon V_0 \to \mathbb{R}^n$ with $a \in V_0$, $\psi(V_0) = \mathbb{R}^n$, $\psi(a) = 0$, and set $B_0 := \psi^{-1}(B)$, an open neighbourhood of $a$. Then $B_0 \setminus \{a\} = \psi^{-1}(B \setminus \{0\})$ is the diffeomorphic image of the connected set $B \setminus \{0\}$ (the unit ball minus its centre is connected by the same argument as the punctured space), hence connected, and it is contained in $L \setminus \{a\} = U \sqcup V$. A connected subset of a disjoint union of two open sets lies entirely in one of them; say $B_0 \setminus \{a\} \subseteq U$. Then $V \cap B_0 = \emptyset$, since $V$ meets neither $B_0 \setminus \{a\}$ (disjoint from $U \supseteq B_0 \setminus \{a\}$) nor $\{a\}$ (as $a \notin V$). Now $U \cup \{a\} = U \cup B_0$ is open in $L$ (it is a union of the open set $U$ with the open set $B_0$; the equality holds because $B_0 = (B_0 \setminus \{a\}) \cup \{a\} \subseteq U \cup \{a\}$, while $\{a\} \subseteq B_0$). We have exhibited $L = (U \cup \{a\}) \sqcup V$ as a disjoint union of two open sets, both nonempty ($V \neq \emptyset$; $a \in U \cup \{a\}$), contradicting the connectedness of $L$. Therefore $L \setminus \{a\}$ is connected, completing the induction. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Part I — the main statement.** Let $M$ be connected, $x, y \in M$, and $K \subseteq M \setminus \{x, y\}$ closed with $M \setminus K$ connected. We must produce a diffeomorphism $h \colon M \to M$, smoothly isotopic to the identity through diffeomorphisms fixing $K$ pointwise, with $h(x) = y$.
>
> **Step 0 — the working manifold.** Set $N := M \setminus K$. Since $K$ is closed, $N$ is open in $M$, hence a smooth manifold of dimension $n$, and it is connected by hypothesis. Because $K \subseteq M \setminus \{x, y\}$, both $x$ and $y$ lie in $N$.
>
> **Step 1 — apply the reachability relation.** By Lemma 2, applied to the open submanifold $N \subseteq M$, the relation $\approx$ on $N$ (there exists a smooth isotopy of $M$ from the identity, supported in a compact subset of $N$, whose time-one map sends one point to the other) is an equivalence relation whose classes are open in $N$.
>
> **Step 2 — connectedness forces one class.** The equivalence classes of $\approx$ partition $N$ into pairwise disjoint nonempty sets, each open in $N$ by Step 1. If there were two distinct classes, then one class and the union of all the others would be two disjoint nonempty open sets covering $N$, contradicting the connectedness of $N$ (Step 0). Hence there is exactly one class, and in particular $x \approx y$.
>
> **Step 3 — read off $h$ and verify the fixing of $K$.** By $x \approx y$ there is a smooth isotopy $H \colon M \times [0, 1] \to M$ with $H_0 = \operatorname{id}_M$, each $H_t$ a diffeomorphism, $H_1(x) = y$, and $H$ supported in a compact set $C \subseteq N = M \setminus K$. Set $h := H_1$. Since $K \subseteq M \setminus C$ and $H$ is supported in $C$, we have $H_t(z) = z$ for every $z \in K$ and every $t$; that is, $H$ fixes $K$ pointwise. Thus $h$ is a diffeomorphism of $M$, smoothly isotopic to the identity through the diffeomorphisms $H_t$, each fixing $K$ pointwise, with $h(x) = y$. This proves the main statement.
>
> **Part II — the corollary.** Let $M$ be connected with $\dim M = n \ge 2$, let $p_1, \dots, p_m$ be distinct points of $M$, and let $D \subseteq M$ be a nonempty coordinate disc. We must produce a diffeomorphism $h$, isotopic to the identity, with $h(p_i) \in D$ for all $i$.
>
> **Step 0 — choose targets.** A coordinate disc $D$ is diffeomorphic to $\mathbb{R}^n$, hence infinite, so we may choose distinct points $q_1, \dots, q_m \in D$ such that every $q_j$ is different from every $p_i$ (the $q_j$ are picked one at a time from $D$ minus the finite set of the $p_i$ and the previously chosen $q$'s, which is nonempty). Thus the $2m$ points $p_1, \dots, p_m, q_1, \dots, q_m$ are all distinct except that the lists $\{p_i\}$ and $\{q_j\}$ are internally distinct and mutually disjoint.
>
> **Step 1 — move the points one at a time.** For $i = 1, \dots, m$ define the finite, hence closed, set
> $$K_i := \{q_1, \dots, q_{i-1}\} \cup \{p_{i+1}, \dots, p_m\} \subseteq M.$$
> We check the hypotheses of the main statement (Part I) with $x := p_i$, $y := q_i$, $K := K_i$. First, $p_i \notin K_i$: it is not among $q_1, \dots, q_{i-1}$ (the $q$'s avoid all $p$'s, Step 0) and not among $p_{i+1}, \dots, p_m$ (the $p$'s are distinct). Second, $q_i \notin K_i$: it is not among $q_1, \dots, q_{i-1}$ (the $q$'s are distinct) and not among $p_{i+1}, \dots, p_m$ (the $q$'s avoid all $p$'s). So $K_i \subseteq M \setminus \{p_i, q_i\}$. Third, $M \setminus K_i$ is connected: $K_i$ is finite and $M$ is connected of dimension $n \ge 2$, so this is Lemma 3. By the main statement there is a diffeomorphism $h_i \colon M \to M$, smoothly isotopic to the identity through diffeomorphisms fixing $K_i$ pointwise, with $h_i(p_i) = q_i$.
>
> **Step 2 — the composite carries every point into $D$.** Set $h := h_m \circ h_{m-1} \circ \cdots \circ h_1$. Fix $i$ and track $p_i$ under the successive maps. For $j < i$, the point $p_i$ belongs to $\{p_{j+1}, \dots, p_m\} \subseteq K_j$, so $h_j$ fixes it: $h_j(p_i) = p_i$. Hence $(h_{i-1} \circ \cdots \circ h_1)(p_i) = p_i$. Applying $h_i$ gives $q_i$. For $j > i$, the point $q_i$ belongs to $\{q_1, \dots, q_{j-1}\} \subseteq K_j$, so $h_j$ fixes it: $h_j(q_i) = q_i$. Hence $(h_m \circ \cdots \circ h_{i+1})(q_i) = q_i$. Combining, $h(p_i) = q_i \in D$. As $i$ was arbitrary, $h(p_i) \in D$ for every $i$.
>
> **Step 3 — the composite is isotopic to the identity.** Each $h_i$ is smoothly isotopic to $\operatorname{id}_M$; let $H^{(i)}$ be an isotopy with $H^{(i)}_0 = \operatorname{id}$, $H^{(i)}_1 = h_i$. Composition of diffeomorphisms isotopic to the identity is isotopic to the identity: reparametrizing each $H^{(i)}$ to be constant near its endpoints (using the smooth $\tau$ of Lemma 2) and concatenating exactly as in the transitivity argument of Lemma 2, one obtains a single smooth isotopy from $\operatorname{id}_M$ to $h_m \circ \cdots \circ h_1 = h$ (at each stage compose the running isotopy with the fixed diffeomorphism accumulated so far, precisely as $K_t = H'_{2t-1} \circ H_1$ was formed there). Therefore $h$ is smoothly isotopic to the identity, with $h(p_i) \in D$ for all $i$. $\qquad \blacksquare$

---

# Cross-Field Exercise Suggestions

**Isotopy uniqueness of the connected sum.** In differential topology the connected sum $M_1 \# M_2$ of two connected $n$-manifolds is formed by deleting a small disc from each and gluing along the resulting boundary spheres. The construction appears to depend on where the discs are cut and on the gluing diffeomorphism. The homogeneity lemma shows the choice of disc does not matter up to diffeomorphism: any two coordinate discs in a connected manifold are carried one to the other by a diffeomorphism isotopic to the identity (isotope the centre by the lemma, then rescale in a chart). The application is non-obvious because "the sum is well defined" sounds like it needs a global uniqueness theorem, when in fact a local homogeneity plus an isotopy suffices for the disc-placement half of it.

**Transitivity of the identity component of the diffeomorphism group.** In the theory of transformation groups one wants to know that $\operatorname{Diff}_0(M)$, the identity component of the diffeomorphism group of a connected manifold, acts transitively on $M$, and more strongly $k$-transitively on ordered $k$-tuples of distinct points when $\dim M \ge 2$. This is precisely the homogeneity lemma and its corollary read as a statement about the group action. It is the starting point for showing that many natural bundles and geometric structures are homogeneous, and that the group $\operatorname{Diff}_0(M)$ is, for $M$ connected, a perfect and even simple group (Thurston's theorem), whose proof begins with exactly this local-to-global sliding.

**Moser's theorem on volume forms.** Given two smooth volume forms of equal total volume on a compact connected oriented manifold, Moser's theorem produces a diffeomorphism, isotopic to the identity, pulling one to the other. The first reduction in Moser's argument is local: one uses homogeneity to move any finite discrepancy into a single chart and to arrange normalizations at a point. The homogeneity lemma is the tool that turns "the forms agree somewhere" into "the forms agree at a point I have placed conveniently", which is how the pointwise normal form feeds the global flow argument.

---

# Bridges

- **[[Thm - Generic Sections are Transverse to the Zero Section|Generic Sections are Transverse to the Zero Section]]** — the supplier of the points to be moved. That theorem perturbs a section of a vector bundle to be transverse to the zero section, producing a finite set of isolated nondegenerate zeros. The homogeneity corollary then gathers those zeros into one coordinate disc by an ambient isotopy; because the isotopy is isotopic to the identity, the bundle's isomorphism class is unchanged, and the section is nowhere zero off the disc. Together they realize the slogan "a bundle with a generic section is trivial off a disc."

- **[[Thm - Clutching Construction for Bundles over a Closed Manifold|Clutching Construction for Bundles over a Closed Manifold]]** — the consumer of the gathered configuration. Clutching describes a bundle that is trivial over the disc and over its complement by a single transition function on the boundary sphere. The homogeneity corollary guarantees the hypothesis of that description can always be arranged: whatever the original bundle, an isotopy places all of its non-triviality inside one disc. The two results are the two halves of "every bundle over a sphere is a clutched bundle."

- **[[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|Homotopic Maps Pull Back Isomorphic Principal Bundles]]** — the reason the sliding is free. A diffeomorphism isotopic to the identity is, in particular, homotopic to the identity, so pulling a bundle back along it yields an isomorphic bundle. This is what makes the homogeneity isotopies harmless: every bundle-theoretic quantity that is an isomorphism invariant survives them. The homogeneity lemma provides the diffeomorphisms; this theorem certifies that using them changes nothing one cares about.

- **[[Ex - Compactly Supported Vector Fields are Complete|Compactly Supported Vector Fields are Complete]]** and **[[Thm - Fundamental Theorem on Flows|the Fundamental Theorem on Flows]]** — the analytic engine, one level down. The single local move of Lemma 1 is the time-one flow of a compactly supported field; completeness makes the flow defined for all time and the fundamental theorem makes each time-slice a diffeomorphism smooth in the point. All of the lemma's global content is bootstrapped from this one flow through the topology of a connected space.

- **[[Ex - Moving Finitely Many Points into a Disc by an Isotopy|Moving Finitely Many Points into a Disc by an Isotopy]]** — the concrete drill. It carries out the corollary explicitly on the torus, writing down the vector fields whose flows move three prescribed points into a small disc, and so makes visible the one-point-at-a-time bookkeeping of Part II of the proof.

---

# Unlocked by This

> [!tip] Bundles are trivial off a point *(from Gauge Theory)*
> For a connected structure group $G$ and a closed manifold $X$, every principal $G$-bundle whose non-triviality is concentrated at finitely many points can be isotoped to be trivial on the complement of a single coordinate disc, hence exhibited by one clutching function. This is the geometric input for the classification of $U(1)$- and $SU(2)$-bundles in **§3.6**, where the clutching function's homotopy class becomes the bundle's characteristic number.

> [!tip] Homogeneity of configuration spaces *(from Differential Topology)*
> The corollary says the identity component $\operatorname{Diff}_0(M)$ acts transitively on the ordered configuration space of $k$ distinct points of a connected manifold of dimension at least two. This underlies the well-definedness of connected sums, the mapping-class-group description of surfaces, and the reduction of many gluing constructions to a standard local model.
