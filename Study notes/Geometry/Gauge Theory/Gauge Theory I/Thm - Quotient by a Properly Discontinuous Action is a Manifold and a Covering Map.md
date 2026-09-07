---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Discrete Group and Properly Discontinuous Action"
  - "Thm - Quotient Manifold Theorem for Free Proper Actions"
  - "Def - Covering Space"
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold (smooth, Hausdorff, second countable, as in every page of this series), and $\Gamma$ is a **discrete group**, that is, a zero-dimensional Lie group; being a zero-dimensional second-countable space, $\Gamma$ is countable, and it carries the discrete topology, so "smooth" for a map out of $\Gamma$ imposes no condition beyond the set-theoretic one. We write the group operation multiplicatively with identity $e \in \Gamma$.

We work with a fixed **smooth left action** of $\Gamma$ on $M$, a smooth map
$$\theta \colon \Gamma \times M \longrightarrow M, \qquad \theta(g, p) = g \cdot p,$$
satisfying $e \cdot p = p$ and $g \cdot (h \cdot p) = (gh) \cdot p$ for all $g, h \in \Gamma$ and $p \in M$. For each fixed $g \in \Gamma$ we write $\theta_g \colon M \to M$, $\theta_g(p) = g \cdot p$, for the map "act by $g$"; it is a [[Def - Diffeomorphism|diffeomorphism]] of $M$ with inverse $\theta_{g^{-1}}$, because $\theta_g$ and $\theta_{g^{-1}}$ are smooth (restrictions of the smooth $\theta$ to the slices $\{g\} \times M$, $\{g^{-1}\} \times M$) and mutually inverse. The **orbit** of $p$ is $\Gamma \cdot p = \{g \cdot p : g \in \Gamma\}$; the **orbit space** $\Gamma \backslash M$ is the set of orbits, carrying the quotient topology, and
$$\pi \colon M \longrightarrow \Gamma \backslash M, \qquad \pi(p) = \Gamma \cdot p,$$
is the quotient map. Everything below is written for a left action; the right-action version is identical after replacing $g \cdot p$ by $p \cdot g$ and $\Gamma \backslash M$ by $M / \Gamma$.

The action is **[[Def - Free, Transitive, Effective, and Proper Group Actions|free]]** if $g \cdot p = p$ for some $p$ forces $g = e$; **[[Def - Free, Transitive, Effective, and Proper Group Actions|proper]]** if the map $\Gamma \times M \to M \times M$, $(g, p) \mapsto (g \cdot p, p)$, is a proper map (preimages of compact sets are compact). The action is **[[Def - Discrete Group and Properly Discontinuous Action|properly discontinuous]]** if it satisfies Bär's two conditions, restated in full in the Statement below.

> [!warning] Convention: notation for the discrete group and the orbit space
> Bär (Definition 1.5.22, Theorem 1.5.23) writes the discrete group as $G$ and the orbit space of a left action as $G \backslash M$. This series reserves $G$ for a general Lie group and writes $\Gamma$ for a discrete group, matching the standard usage in which $\Gamma$ is the deck group of a covering. For the right actions that appear on principal bundles the series writes $M / \Gamma$; here, with a left action, the orbit space is $\Gamma \backslash M$. The two conventions are related by $p \cdot g := g^{-1} \cdot p$, which turns a left action into a right action with the same orbits.

The full symbol registry for the chapter is on the parent page [[Gauge Theory I — Lie Groups, Representations, and Group Actions]].

---

# Statement

> **Theorem (quotient by a properly discontinuous action; Bär, Theorem 1.5.23; Lee, *Introduction to Smooth Manifolds* 2e, Theorem 21.13).** Let $\Gamma$ be a discrete group acting smoothly and **properly discontinuously** on a smooth manifold $M$, that is, the smooth left action $\theta \colon \Gamma \times M \to M$ satisfies
> $$
> \textbf{(i)} \quad \forall\, p \in M \ \ \exists\ \text{an open neighbourhood } U \ni p \ \text{ with } \ \big(g \cdot U \cap U \neq \varnothing \ \Longrightarrow\ g = e\big),
> $$
> $$
> \textbf{(ii)} \quad \forall\, p, q \in M \ \text{ with } \ \Gamma \cdot p \neq \Gamma \cdot q, \ \ \exists\ \text{open } U \ni p, \ V \ni q \ \text{ with } \ g \cdot U \cap V = \varnothing \ \ \forall\, g \in \Gamma,
> $$
> where $g \cdot U := \theta_g(U) = \{g \cdot u : u \in U\}$. Then:
> 1. The orbit space $\Gamma \backslash M$ carries a **unique** smooth manifold structure such that the quotient map $\pi \colon M \to \Gamma \backslash M$, $p \mapsto \Gamma \cdot p$, is smooth and a **[[Def - Covering Space|smooth covering map]]**; in particular $\pi$ is a **local diffeomorphism**, $\dim(\Gamma \backslash M) = \dim M$, and $\Gamma \backslash M$ is Hausdorff and second countable.
> 2. Every neighbourhood $U$ of the form in (i) is **evenly covered**: writing $\widehat U := \pi(U)$, which is open, one has
> $$\pi^{-1}(\widehat U) \;=\; \bigsqcup_{g \in \Gamma} g \cdot U \qquad\text{(a disjoint union),}$$
> and for each $g \in \Gamma$ the restriction $\pi|_{g \cdot U} \colon g \cdot U \to \widehat U$ is a diffeomorphism. The sheets of the cover over $\widehat U$ are exactly the translates $g \cdot U$, indexed by $\Gamma$, so the fibre $\pi^{-1}(\pi(p))$ is in bijection with $\Gamma$.
> 3. **Universal property.** For every smooth manifold $N$ and every smooth map $f \colon M \to N$ that is constant on the orbits of $\Gamma$ (that is, $f(g \cdot p) = f(p)$ for all $g \in \Gamma$, $p \in M$), there is a **unique** smooth map $\widetilde f \colon \Gamma \backslash M \to N$ with $\widetilde f \circ \pi = f$.

The three conclusions are of three different kinds and it is worth keeping them apart: (1) is the *existence and rigidity of the smooth structure*, (2) is the *concrete local model* that makes $\pi$ a covering and names its sheets, and (3) is the *functorial* statement that lets smooth objects on $M$ that ignore the $\Gamma$-symmetry descend to $\Gamma \backslash M$.

---

# Motivation

There are two ways a manifold acquires a genuinely new manifold below it, and this theorem governs the discrete one. The [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]] handles a *positive-dimensional* group $G$ acting freely and properly: it collapses each orbit, a copy of $G$, to a point, and the quotient has dimension $\dim M - \dim G$, strictly smaller. The present theorem handles a *zero-dimensional* group $\Gamma$. Now the orbits are discrete point-clusters, nothing is collapsed dimensionally, and the quotient has the **same** dimension as $M$. What changes is not the dimension but the *global identifications*: points of $M$ that lie in a common $\Gamma$-orbit are glued together, and the result is a manifold that $M$ sits above as a stack of sheets. This is exactly the geometry of a covering, and the theorem is the precise statement that a well-behaved discrete symmetry of $M$ produces a covering $M \to \Gamma \backslash M$ downstairs.

The problem the hypotheses solve is that not every action of a discrete group yields a manifold quotient, and one must see exactly what can go wrong. Two failures are possible, and conditions (i) and (ii) are tailored one to each. First, an orbit could accumulate onto itself — a point $p$ could have translates $g \cdot p$ arbitrarily close to $p$ for infinitely many $g \neq e$ — and then no small neighbourhood of $\pi(p)$ can look like a single clean copy of a neighbourhood of $p$; there is no local chart. Condition (i) rules this out by demanding a neighbourhood $U$ so small that the *only* translate meeting it is the trivial one. Second, even when each orbit is locally tidy, two *distinct* orbits could be inseparable — every neighbourhood of one orbit could meet every neighbourhood of the other — and then $\Gamma \backslash M$, though locally Euclidean, would fail to be Hausdorff and would not be a manifold at all. Condition (ii) rules this out by separating distinct orbits. The archetype of the second failure is the action of $(\mathbb{Q}, +)$ on $\mathbb{R}$ by translation: every orbit is dense, so no two orbits can be separated, and $\mathbb{Q} \backslash \mathbb{R}$ carries the indiscrete topology (proved on [[Def - Discrete Group and Properly Discontinuous Action|the definition page]] and in [[Ex - The Rationals Acting on R are Not Properly Discontinuous|the accompanying exercise]]). The word "discontinuous" in "properly discontinuous" is historical and slightly misleading: the action is perfectly continuous — indeed smooth; what is discontinuous, in the sense of "discrete", is the way the orbit sits inside $M$.

The reward for the two hypotheses is large. Every concrete quotient that presents a familiar space as $M$ divided by a symmetry passes through this theorem: the circle $S^1 = \mathbb{Z} \backslash \mathbb{R}$, the torus $T^n = \mathbb{R}^n / \mathbb{Z}^n$, real projective space $\mathbb{RP}^n = S^n / (\mathbb{Z}/2)$, the mapping torus of a diffeomorphism, and — most importantly for gauge theory — the universal cover $\widetilde X \to X$ realised as $\pi_1(X)$ acting on $\widetilde X$, which is the first and simplest example of a principal bundle with a discrete structure group. The theorem is what certifies that all of these are smooth manifolds and that the quotient maps are honest coverings, so that lifting theory, deck transformations, and the identification of $\Gamma$ with the fundamental group all become available.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is "discrete group, smooth action, conditions (i) and (ii)". The skill is to recognise the many situations that secretly supply a properly discontinuous action even though the words never appear.

The first disguised source is **a free action of a finite group on a manifold**. If a finite group $\Gamma$ acts smoothly and freely on a Hausdorff manifold $M$, the action is automatically properly discontinuous. The bridge is a compactness argument: finiteness makes $\Gamma$ compact, and a free action of a compact group on a Hausdorff manifold is proper (the orbit map is a homeomorphism onto a compact, hence closed, orbit), and for a discrete group "free and proper" is equivalent to "properly discontinuous" — the equivalence proved on [[Def - Discrete Group and Properly Discontinuous Action|the definition page]]. Concretely, for a *finite* group one produces the neighbourhood in (i) by hand: the finitely many points $g \cdot p$ ($g \neq e$) are distinct from $p$ by freeness, Hausdorffness separates $p$ from each of them, and one intersects the finitely many separating neighbourhoods. *Example problem:* the antipodal action of $\mathbb{Z}/2 = \{\pm 1\}$ on $S^n$ is free (no point equals its antipode), hence properly discontinuous, so $\mathbb{RP}^n = S^n / (\mathbb{Z}/2)$ is a smooth manifold double-covered by $S^n$.

The second disguised source is **a lattice of isometries, or more generally a group acting by isometries with discrete orbits without fixed points**. If $\Gamma$ acts on a Riemannian manifold $(M, \mathfrak g)$ by isometries, freely, and so that each orbit is a closed discrete subset with a positive infimum of pairwise distances (a *uniformly discrete* orbit), then the metric balls of half that radius furnish the neighbourhoods in (i) and (ii) simultaneously, and the action is properly discontinuous. The bridge is metric: isometries preserve distances, so a ball of radius $r/2$ about $p$ can meet its translate only if two orbit points are within $r$, which the uniform-discreteness rules out unless the translate is trivial. *Example problem:* the translation action of the lattice $\mathbb{Z}^n \leq \mathbb{R}^n$ has every orbit a translate of $\mathbb{Z}^n$, pairwise distances at least $1$; hence it is properly discontinuous and $T^n = \mathbb{R}^n / \mathbb{Z}^n$ is a smooth manifold, with $\mathbb{R}^n \to T^n$ a covering.

The third disguised source is **a diffeomorphism of a manifold, promoted to a $\mathbb{Z}$-action along an auxiliary line**. Given any diffeomorphism $\phi \colon F \to F$, let $\mathbb{Z}$ act on $\mathbb{R} \times F$ by $k \cdot (t, f) = (t + k, \phi^k(f))$. This action is properly discontinuous *no matter how badly $\phi$ behaves*, because the translation in the $\mathbb{R}$-coordinate already forces $U = (t - \tfrac12, t + \tfrac12) \times F$ to meet only its trivial translate, and distinct $\mathbb{Z}$-orbits differ in their $\mathbb{R}$-coordinate modulo $1$. The bridge is that a single free proper $\mathbb{Z}$-factor (translation of $\mathbb{R}$) dominates: adjoining any diffeomorphism in the fibre cannot destroy proper discontinuity. *Example problem:* the quotient $\mathbb{Z} \backslash (\mathbb{R} \times F)$ is the **mapping torus** of $\phi$, a smooth manifold fibring over $S^1 = \mathbb{Z} \backslash \mathbb{R}$ with fibre $F$, obtained from $[0, 1] \times F$ by gluing $\{0\} \times F$ to $\{1\} \times F$ through $\phi$.

**Targets (Output Amplification)**

The bare output is "a smooth covering $\pi \colon M \to \Gamma \backslash M$". Combined with one further ingredient it does much more.

Combine the conclusion with **the covering-space dictionary between $\Gamma$ and the fundamental group**. If in addition $M$ is connected and simply connected, then $\pi \colon M \to \Gamma \backslash M$ is a universal covering (see [[Def - Universal Cover]]), and the deck group of a universal covering is the fundamental group of the base; since $\Gamma$ acts by deck transformations, one gets a group isomorphism $\Gamma \cong \pi_1(\Gamma \backslash M)$. The extra ingredient is the theory of the universal cover; the payoff is a *computation of a fundamental group by hand*: $\pi_1(T^n) \cong \mathbb{Z}^n$ from $\mathbb{R}^n / \mathbb{Z}^n$, and $\pi_1(\mathbb{RP}^n) \cong \mathbb{Z}/2$ from $S^n / (\mathbb{Z}/2)$ for $n \geq 2$. This is exactly the mechanism by which the universal cover becomes a **principal $\pi_1$-bundle**, the entry point to gauge theory with a discrete structure group.

Combine the conclusion with **a $\Gamma$-invariant tensor field on $M$**. Because $\pi$ is a local diffeomorphism, any smooth tensor field on $M$ that is invariant under every $\theta_g$ descends to a well-defined smooth tensor field on $\Gamma \backslash M$; one transports it through the local inverses of $\pi$, and invariance is exactly what makes the local pieces agree on overlaps. The extra ingredient is a $\Gamma$-invariant object; the payoff is *geometry downstairs from geometry upstairs*: the flat Euclidean metric on $\mathbb{R}^n$ is $\mathbb{Z}^n$-invariant and descends to a flat metric on $T^n$, and a $\Gamma$-invariant complex structure descends, so quotients of $\mathbb{C}^n$ by lattices are complex tori. This is the abstract reason "the torus is flat".

Combine the conclusion with **multiplicativity of the Euler characteristic under a finite cover**. For a finite group $\Gamma$ of order $|\Gamma|$ acting properly discontinuously (equivalently, freely) on a compact manifold $M$, the covering $\pi$ has $|\Gamma|$ sheets, so $\chi(M) = |\Gamma| \cdot \chi(\Gamma \backslash M)$. The extra ingredient is the counting law for the Euler characteristic; the payoff is a *rigidity obstruction*: if $\chi(M)$ is odd — as for $M = S^{2n}$, where $\chi(S^{2n}) = 2$ constrains the sheet number to divide $2$ — then only very small groups can act freely, and one recovers, for instance, that no group of order greater than $2$ acts freely on an even sphere.

---

# Why Is It True

Set the formal machinery aside and watch what condition (i) does. It hands every point $p$ a neighbourhood $U$ so tight that among all the translates $g \cdot U$, only $g = e$ produces one that overlaps $U$. Two consequences follow at once, and together they are the entire theorem. First, the translates $\{g \cdot U : g \in \Gamma\}$ are **pairwise disjoint**: if $g \cdot U$ met $g' \cdot U$, then applying the diffeomorphism $\theta_{g^{-1}}$ would make $U$ meet $(g^{-1}g) \cdot U$, forcing $g^{-1}g' = e$, that is $g = g'$. So above the little patch $\widehat U = \pi(U)$ downstairs, the preimage in $M$ is a genuinely disjoint stack of copies of $U$, one for each element of $\Gamma$. Second, $\pi$ **does not identify any two points of $U$ with each other**: if $\pi(x) = \pi(y)$ with $x, y \in U$, then $y = g \cdot x$ for some $g$, so $y \in U \cap (g \cdot U)$, forcing $g = e$ and $y = x$. So $\pi$ restricted to $U$ is injective — it carries $U$ bijectively onto $\widehat U$.

Now assemble. Each translate $g \cdot U$ is carried by $\pi$ onto the *same* patch $\widehat U$ (because $\pi$ is constant on orbits, and $g \cdot U$ is the orbit-image of $U$), and it is carried there bijectively (because $\theta_g$ is a diffeomorphism $U \to g \cdot U$ and $\pi$ is injective on $U$). Since $\pi$ is an open map and a local diffeomorphism — which is where the dimension count $\dim(\Gamma \backslash M) = \dim M$ enters, making a submersion the same as a local diffeomorphism — each of these bijections is in fact a diffeomorphism. That is the definition of "$\widehat U$ is evenly covered", and it holds around every point. The map $\pi$ is therefore a covering.

> **The mechanism in one sentence:** condition (i) shrinks each point's neighbourhood until its $\Gamma$-translates are pairwise disjoint and $\pi$ is injective on it, so that neighbourhood becomes an evenly covered patch and $\pi$ is a covering; condition (ii) is the separate guarantee that the quotient is Hausdorff, and hence a manifold rather than a mere locally Euclidean space.

The only piece not visible from condition (i) alone is that $\Gamma \backslash M$ is a *smooth manifold* to begin with — that it is Hausdorff and second countable and carries a compatible atlas. That is what one imports from the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]]: a properly discontinuous action is free and proper, and the quotient manifold theorem then produces the smooth structure, the submersion, and the universal property. Everything specific to the discrete case — the even covering — is the local analysis above, laid on top of that.

---

# What Makes This Hard

The subtle point is that "conditions (i) and (ii)" is *not* obviously the same as "free and proper", and one must not silently assume it. Condition (i) alone gives freeness and the even-covering picture but permits a non-Hausdorff quotient; condition (ii) is a genuinely separate demand that does the Hausdorff work, and it is exactly the hypothesis that fails for the rationals acting on the line. Reducing the theorem to the quotient manifold theorem therefore rests on the equivalence "properly discontinuous $\iff$ free and proper" for a discrete group, which is proved on the definition page and must be cited, not waved at. The second common error is to forget the dimension count: one must observe $\dim \Gamma = 0$ to know that the submersion $\pi$ produced by the quotient manifold theorem is between manifolds of *equal* dimension, for only then is a submersion automatically a local diffeomorphism and each sheet an honest diffeomorphism rather than merely a smooth bijection. The third is to prove the sheets are bijections and stop: a continuous or smooth bijection need not have smooth inverse, so one must invoke openness and local-diffeomorphism status to upgrade each $\pi|_{g \cdot U}$ to a diffeomorphism.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** First reduce to the quotient manifold theorem by observing that a properly discontinuous action of a discrete group is free and proper, which delivers the smooth structure, the submersion $\pi$, second countability, Hausdorffness, and the universal property in one stroke. Then note $\dim \Gamma = 0$, so $\pi$ is a submersion between equidimensional manifolds and hence a local diffeomorphism and an open map. Finally, use condition (i) to show each such neighbourhood $U$ is evenly covered, which is precisely "$\pi$ is a covering map"; uniqueness of the structure is inherited from the quotient manifold theorem.

**Subgoal decomposition:**

1. **Reduce to free-and-proper.** Show the action is free and proper.
   - *Hint:* Freeness is immediate from (i); for properness invoke the equivalence proved on the definition page.
   - *Why needed:* It is the exact hypothesis of the quotient manifold theorem.

2. **Import the smooth structure.** Apply the quotient manifold theorem to get a unique smooth structure on $\Gamma \backslash M$ making $\pi$ a submersion, with $\Gamma \backslash M$ Hausdorff and second countable and the universal property in force.
   - *Hint:* Read the dimension formula $\dim(\Gamma \backslash M) = \dim M - \dim \Gamma$ with $\dim \Gamma = 0$.
   - *Why needed:* It supplies conclusions (1)'s manifold structure and (3)'s universal property directly.

3. **Upgrade the submersion to a local diffeomorphism.** Show $\pi$ is a local diffeomorphism and an open map.
   - *Hint:* A submersion has surjective differential; between equal-dimensional spaces surjective forces bijective, and the inverse function theorem finishes it. Openness is the standing property of submersions.
   - *Why needed:* Each sheet of the cover must be a diffeomorphism, not just a bijection.

4. **Translates are disjoint and $\pi$ is injective on $U$.** For a neighbourhood $U$ as in (i), show $\{g \cdot U\}_{g \in \Gamma}$ are pairwise disjoint and $\pi|_U$ is injective.
   - *Hint:* Overlap of $g \cdot U$ and $g' \cdot U$, pushed by $\theta_{g^{-1}}$, contradicts (i); likewise $\pi(x) = \pi(y)$ inside $U$.
   - *Why needed:* Disjointness is the "disjoint union" in even covering; injectivity makes $\pi|_U$ a bijection onto its image.

5. **Even covering.** Prove $\pi^{-1}(\pi(U)) = \bigsqcup_g g \cdot U$ and each $\pi|_{g \cdot U} \colon g \cdot U \to \pi(U)$ is a diffeomorphism, then conclude $\pi$ is a smooth covering map.
   - *Hint:* $\pi^{-1}(\pi(U)) = \bigcup_g g \cdot U$ holds for any group action; disjointness is Subgoal 4; $\pi|_{g \cdot U} = (\pi|_U) \circ \theta_{g^{-1}}$ is a composite of diffeomorphisms.
   - *Why needed:* This is conclusion (2), and it is the definition of covering map, giving conclusion (1)'s covering statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: The translates of an (i)-neighbourhood are pairwise disjoint, and $\pi$ is injective on it
> **Statement:** Let $U \subseteq M$ be open with the property in condition (i): $g \cdot U \cap U \neq \varnothing \Rightarrow g = e$. Then (a) $g \cdot U \cap g' \cdot U = \varnothing$ whenever $g \neq g'$, and (b) if $x, y \in U$ satisfy $\pi(x) = \pi(y)$ then $x = y$.
>
> **Hint:** Apply the diffeomorphism $\theta_{g^{-1}}$ to an overlap to bring it back to a self-overlap of $U$, then use (i).
>
> **Why needed:** Part (a) is the "disjoint union" in the even-covering statement; part (b) makes $\pi|_U$ injective, hence a bijection onto $\pi(U)$.
>
> > [!note]- Full proof
> > **(a) Disjointness of translates.** Suppose $g \neq g'$ and, for contradiction, that there is a point $z \in g \cdot U \cap g' \cdot U$. Then $z = g \cdot u = g' \cdot u'$ for some $u, u' \in U$. Applying the diffeomorphism $\theta_{g^{-1}}$ to both descriptions of $z$,
> > $$u = \theta_{g^{-1}}(z) = \theta_{g^{-1}}(g' \cdot u') = (g^{-1} g') \cdot u' \qquad \text{(since } \theta_{g^{-1}} \circ \theta_{g'} = \theta_{g^{-1} g'} \text{ by the action axiom).}$$
> > Thus $u = (g^{-1} g') \cdot u' \in (g^{-1} g') \cdot U$, while also $u \in U$, so $(g^{-1} g') \cdot U \cap U \neq \varnothing$. By condition (i) this forces $g^{-1} g' = e$, that is $g = g'$, contradicting $g \neq g'$. Hence no such $z$ exists and $g \cdot U \cap g' \cdot U = \varnothing$.
> >
> > **(b) Injectivity of $\pi$ on $U$.** Suppose $x, y \in U$ with $\pi(x) = \pi(y)$; by definition of $\pi$ this says $x$ and $y$ lie in the same orbit, so $y = g \cdot x$ for some $g \in \Gamma$. Then $y \in U$ and $y = g \cdot x \in g \cdot U$, so $U \cap g \cdot U \neq \varnothing$, whence $g = e$ by condition (i), and therefore $y = e \cdot x = x$. So $\pi|_U$ is injective. $\blacksquare$

> [!note]- Lemma 2: A properly discontinuous action of a discrete group is free and proper
> **Statement:** If the discrete group $\Gamma$ acts smoothly and properly discontinuously on $M$ (conditions (i) and (ii)), then the action is free and proper.
>
> **Hint:** Freeness reads straight off (i); properness is the substantive half, established on the definition page and invoked here with its statement restated.
>
> **Why needed:** It is precisely the hypothesis "free and proper" required to apply the quotient manifold theorem in Step 1 of the formal proof.
>
> > [!note]- Full proof
> > **Freeness.** Let $g \in \Gamma$ and $p \in M$ satisfy $g \cdot p = p$. Choose an open neighbourhood $U \ni p$ as in condition (i). Then $p \in U$ and $p = g \cdot p \in g \cdot U$, so $g \cdot U \cap U \ni p$ is non-empty; condition (i) forces $g = e$. Since this holds for every fixed point of every element, the only element with a fixed point is $e$, which is the definition of a free action.
> >
> > **Properness.** For a discrete group, the equivalence
> > $$\text{properly discontinuous} \iff \text{free and proper}$$
> > is proved in full, both directions, on [[Def - Discrete Group and Properly Discontinuous Action|the definition page]] (corollary to the definition): the forward direction shows that condition (i) gives freeness and that conditions (i)–(ii) together give properness of the map $(g, p) \mapsto (g \cdot p, p)$ — the key step being that (i) makes $\{g \in \Gamma : g \cdot K \cap K \neq \varnothing\}$ finite for every compact $K$, and (ii) makes the orbit relation closed so that the quotient is Hausdorff — while the converse recovers (i) from a slice neighbourhood and (ii) from the closedness of the orbit relation. Invoking that corollary with the present hypotheses (which are exactly its left-hand side), the action is proper. $\blacksquare$

> [!note]- Lemma 3: A submersion between manifolds of equal dimension is a local diffeomorphism and an open map
> **Statement:** Let $\pi \colon M \to Q$ be a smooth submersion of smooth manifolds with $\dim M = \dim Q$. Then $\pi$ is a local diffeomorphism (each point of $M$ has a neighbourhood mapped diffeomorphically onto an open set) and an open map.
>
> **Hint:** A surjective linear map between vector spaces of equal finite dimension is an isomorphism; the inverse function theorem turns an isomorphism of differentials into a local diffeomorphism.
>
> **Why needed:** The quotient manifold theorem yields $\pi$ only as a submersion; this lemma, together with $\dim \Gamma = 0$, upgrades it so that the sheets $\pi|_{g \cdot U}$ are diffeomorphisms.
>
> > [!note]- Full proof
> > **Differential is an isomorphism.** Fix $p \in M$ and set $q = \pi(p)$. Because $\pi$ is a [[Def - Immersion, Submersion, and Embedding|submersion]], its differential $d\pi_p \colon T_p M \to T_q Q$ is surjective. Both tangent spaces are real vector spaces of dimension $\dim M = \dim Q =: n$. A surjective linear map $L \colon V \to W$ between finite-dimensional spaces satisfies $\dim W = \dim V - \dim \ker L$ (the rank–nullity theorem), so with $\dim V = \dim W = n$ we get $\dim \ker L = 0$, that is $L$ is injective; a surjective injective linear map is an isomorphism. Hence $d\pi_p$ is a linear isomorphism.
> >
> > **Local diffeomorphism.** By the [[Thm - The Inverse Function Theorem|inverse function theorem]] — if a smooth map has invertible differential at a point, it restricts to a diffeomorphism between open neighbourhoods of that point and its image — there are open sets $W \ni p$ and $W' \ni q$ with $\pi|_W \colon W \to W'$ a diffeomorphism. As $p$ was arbitrary, $\pi$ is a local diffeomorphism.
> >
> > **Open map.** A local diffeomorphism is open: for open $A \subseteq M$ and $a \in A$, pick $W \ni a$ with $\pi|_W$ a diffeomorphism onto the open set $\pi(W)$; then $\pi(A \cap W)$ is open (diffeomorphisms are open) and contains $\pi(a)$, so $\pi(A) = \bigcup_{a \in A} \pi(A \cap W_a)$ is a union of open sets, hence open. (Equivalently this is the standing fact that [[Thm - Submersions are Open Maps|smooth submersions are open maps]], restated: a smooth submersion carries open sets to open sets.) $\blacksquare$

> [!note]- Lemma 4: For any group action, $\pi^{-1}(\pi(A)) = \bigcup_{g} g \cdot A$
> **Statement:** For a left action of $\Gamma$ on $M$ with quotient map $\pi$, and any subset $A \subseteq M$, one has $\pi^{-1}(\pi(A)) = \bigcup_{g \in \Gamma} g \cdot A$. In particular, if $A$ is open then $\pi(A)$ is open in the quotient topology.
>
> **Hint:** "Same orbit as some point of $A$" is exactly "a translate of some point of $A$".
>
> **Why needed:** It identifies the full preimage of the patch $\pi(U)$ as the union of translates, which Lemma 1 then splits into a disjoint union; the openness clause makes $\pi(U)$ an open patch.
>
> > [!note]- Full proof
> > **Set equality.** A point $x \in M$ lies in $\pi^{-1}(\pi(A))$ if and only if $\pi(x) \in \pi(A)$, i.e. if and only if there is $a \in A$ with $\pi(x) = \pi(a)$, i.e. (by definition of $\pi$) if and only if $x$ and $a$ lie in a common orbit for some $a \in A$, i.e. if and only if $x = g \cdot a$ for some $g \in \Gamma$ and $a \in A$. That last condition says exactly $x \in \bigcup_{g \in \Gamma} g \cdot A$. Hence $\pi^{-1}(\pi(A)) = \bigcup_{g \in \Gamma} g \cdot A$.
> >
> > **Openness.** If $A$ is open, then each $g \cdot A = \theta_g(A)$ is open because $\theta_g$ is a diffeomorphism, so $\pi^{-1}(\pi(A)) = \bigcup_g g \cdot A$ is open in $M$. By the definition of the quotient topology, a set $S \subseteq \Gamma \backslash M$ is open exactly when $\pi^{-1}(S)$ is open; taking $S = \pi(A)$, whose preimage we have just shown is open, $\pi(A)$ is open. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Gamma$ be a discrete group acting smoothly and properly discontinuously on the smooth manifold $M$, with quotient map $\pi \colon M \to \Gamma \backslash M$.
>
> **Step 0 — the hypotheses of the quotient manifold theorem hold.** By Lemma 2, the action is free and proper. This is the precondition we must have in place before any smooth structure on $\Gamma \backslash M$ is available.
>
> **Step 1 — import the smooth structure, submersion, second countability, Hausdorffness, and universal property.** By the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]] — restated: *if a Lie group $G$ acts smoothly, freely and properly on a smooth manifold $M$, then $G \backslash M$ carries a unique smooth manifold structure of dimension $\dim M - \dim G$ for which $\pi \colon M \to G \backslash M$ is a smooth submersion; moreover $G \backslash M$ is Hausdorff and second countable, $\pi$ admits smooth local sections, and for every smooth $f \colon M \to N$ constant on orbits there is a unique smooth $\widetilde f$ with $\widetilde f \circ \pi = f$* — applied with $G = \Gamma$ (a discrete group is a zero-dimensional Lie group), there is a **unique** smooth structure on $\Gamma \backslash M$ making $\pi$ a smooth submersion, and with it $\Gamma \backslash M$ is Hausdorff and second countable and the universal property of conclusion (3) holds verbatim. Because $\dim \Gamma = 0$, the dimension formula reads
> $$\dim(\Gamma \backslash M) = \dim M - \dim \Gamma = \dim M \qquad \text{(quotient manifold theorem, } \dim \Gamma = 0\text{).}$$
> This already establishes conclusion (3), and all of conclusion (1) except the covering statement; the uniqueness in conclusion (1) is inherited here, once we note in Step 4 that a covering map is in particular a submersion, so the unique submersion-compatible structure is the unique covering-compatible one.
>
> **Step 2 — $\pi$ is a local diffeomorphism and an open map.** By Step 1, $\pi$ is a smooth submersion between manifolds of equal dimension $\dim M = \dim(\Gamma \backslash M)$. By Lemma 3, such a map is a local diffeomorphism and an open map. In particular $\pi$ carries open sets to open sets, and near each point it has a smooth local inverse.
>
> **Step 3 — every (i)-neighbourhood is evenly covered.** Fix $q \in \Gamma \backslash M$ and a point $p \in M$ with $\pi(p) = q$. By condition (i) choose an open neighbourhood $U \ni p$ with $g \cdot U \cap U \neq \varnothing \Rightarrow g = e$. Put $\widehat U := \pi(U)$; by Lemma 4 (openness clause) $\widehat U$ is open, and it contains $q = \pi(p)$.
>
> **Preimage splits as the union of translates.** By Lemma 4 (set equality),
> $$\pi^{-1}(\widehat U) = \pi^{-1}(\pi(U)) = \bigcup_{g \in \Gamma} g \cdot U \qquad \text{(Lemma 4).}$$
>
> **The union is disjoint.** By Lemma 1(a), the sets $\{g \cdot U : g \in \Gamma\}$ are pairwise disjoint, so the union above is a disjoint union:
> $$\pi^{-1}(\widehat U) = \bigsqcup_{g \in \Gamma} g \cdot U \qquad \text{(Lemma 1(a)).}$$
>
> **Each translate maps diffeomorphically onto $\widehat U$.** Consider first $g = e$. The map $\pi|_U \colon U \to \widehat U$ is: surjective by definition of $\widehat U = \pi(U)$; injective by Lemma 1(b); smooth as a restriction of $\pi$; open as a restriction of the open map $\pi$ (Step 2) to the open set $U$, so its inverse is continuous; and a local diffeomorphism as a restriction of the local diffeomorphism $\pi$ (Step 2). A bijective local diffeomorphism has a smooth inverse (locally it agrees with the smooth local inverses of $\pi$), hence $\pi|_U \colon U \to \widehat U$ is a diffeomorphism. Now take an arbitrary $g \in \Gamma$. Since $\pi$ is constant on orbits, $\pi \circ \theta_g = \pi$, and $\theta_{g^{-1}} \colon g \cdot U \to U$ is a diffeomorphism (restriction of the diffeomorphism $\theta_{g^{-1}}$, which maps $g \cdot U$ onto $U$); therefore
> $$\pi|_{g \cdot U} = \pi \circ \big(\theta_{g^{-1}}\big) \big|_{g \cdot U} = \big(\pi|_U\big) \circ \big(\theta_{g^{-1}}|_{g \cdot U}\big) \qquad \text{(since } \pi \circ \theta_{g^{-1}} = \pi \text{ and } \theta_{g^{-1}}(g \cdot U) = U\text{),}$$
> a composite of the diffeomorphism $\theta_{g^{-1}}|_{g \cdot U} \colon g \cdot U \to U$ with the diffeomorphism $\pi|_U \colon U \to \widehat U$. A composite of diffeomorphisms is a diffeomorphism, so $\pi|_{g \cdot U} \colon g \cdot U \to \widehat U$ is a diffeomorphism for every $g \in \Gamma$. This is exactly the statement that $\widehat U$ is evenly covered by $\pi$, with sheets the translates $g \cdot U$; it is conclusion (2), and the fibre $\pi^{-1}(q) = \{g \cdot p : g \in \Gamma\}$ is in bijection with $\Gamma$ by freeness (Lemma 2).
>
> **Step 4 — $\pi$ is a smooth covering map, and the structure is the unique one.** Every point $q \in \Gamma \backslash M$ was shown in Step 3 to possess an evenly covered open neighbourhood $\widehat U$, with each sheet mapped diffeomorphically onto $\widehat U$ by $\pi$. By the definition of a [[Def - Covering Space|smooth covering map]] — restated: *a smooth surjection $\pi \colon M \to Q$ between smooth manifolds is a smooth covering map if every point of $Q$ has an open neighbourhood $\widehat U$ whose preimage is a disjoint union of open sets each mapped diffeomorphically onto $\widehat U$ by $\pi$* — the map $\pi$ is a smooth covering map. (It is surjective because every orbit is $\pi(p)$ for some $p$.) A smooth covering map is in particular a local diffeomorphism, and a local diffeomorphism is a submersion; hence the smooth structure making $\pi$ a covering map is a smooth structure making $\pi$ a submersion, and by the uniqueness clause of Step 1 it is the unique such structure. This establishes the uniqueness in conclusion (1) and completes conclusion (1).
>
> **Conclusion.** The orbit space $\Gamma \backslash M$ carries a unique smooth structure making $\pi$ a smooth covering map; it is Hausdorff, second countable, of dimension $\dim M$; every (i)-neighbourhood is evenly covered with sheets the $\Gamma$-translates; and the universal property holds. Therefore all three conclusions are proved. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The circle and the exponential covering (analysis / topology).** The action of $\mathbb{Z}$ on $\mathbb{R}$ by $k \cdot t = t + k$ is properly discontinuous, with $U = (t - \tfrac12, t + \tfrac12)$ realising condition (i) and $\varepsilon = \min_k |t - (s + k)|$ realising condition (ii) for orbit-distinct $s, t$. The theorem makes $\mathbb{Z} \backslash \mathbb{R}$ a smooth manifold and $\mathbb{R} \to \mathbb{Z} \backslash \mathbb{R}$ a covering; the map $f(t) = (\cos 2\pi t, \sin 2\pi t)$ is $\mathbb{Z}$-invariant, so the universal property descends it to a diffeomorphism $\mathbb{Z} \backslash \mathbb{R} \cong S^1$ (worked in [[Ex - The Circle as the Quotient of R by the Integers|the accompanying exercise]]). The theorem applies because a single free translation is properly discontinuous, which is non-obvious only in that one must produce the two neighbourhoods explicitly.

**Real projective space and the antipodal map (topology / geometry).** The antipodal action of $\mathbb{Z}/2$ on $S^n$ is free — no unit vector equals its negative — hence, being a free action of a finite group on a Hausdorff manifold, properly discontinuous. The theorem yields the smooth manifold $\mathbb{RP}^n = S^n / (\mathbb{Z}/2)$ and the two-sheeted covering $S^n \to \mathbb{RP}^n$. The application is non-obvious because "free finite action" does not visibly mention conditions (i)–(ii); the bridge is the compactness argument turning free-plus-compact into properly discontinuous. For $n \geq 2$ this covering is universal, so $\pi_1(\mathbb{RP}^n) \cong \mathbb{Z}/2$.

**The mapping torus of a diffeomorphism (dynamics / bundle theory).** Given $\phi \in \operatorname{Diff}(F)$, the action $k \cdot (t, f) = (t + k, \phi^k(f))$ of $\mathbb{Z}$ on $\mathbb{R} \times F$ is properly discontinuous because the $\mathbb{R}$-translation already forces disjointness of translates of $(t - \tfrac12, t + \tfrac12) \times F$, regardless of $\phi$. The theorem builds the mapping torus $\mathbb{Z} \backslash (\mathbb{R} \times F)$ as a smooth manifold with a covering by $\mathbb{R} \times F$; projecting to the first coordinate gives a fibre bundle over $S^1$ with fibre $F$ and monodromy $\phi$. The point that makes this non-obvious is that no hypothesis on $\phi$ is needed: a well-behaved factor dominates a badly behaved one in proper discontinuity.

**Flat and complex tori (Riemannian and complex geometry).** The lattice $\mathbb{Z}^n$ acts on $\mathbb{R}^n$ by translation, properly discontinuously (uniformly discrete orbits), so $T^n = \mathbb{R}^n / \mathbb{Z}^n$ is a smooth manifold covered by $\mathbb{R}^n$. Because $\pi$ is a local diffeomorphism, the $\mathbb{Z}^n$-invariant flat metric $\sum_i (dx^i)^2$ and, in the even-dimensional case, a $\Gamma$-invariant complex structure descend, giving flat Riemannian tori and complex tori. The theorem is what licenses the descent of these tensors; the invariance of the object under $\Gamma$ is the extra hypothesis, and recognising that a local diffeomorphism transports invariant tensors is the step.

---

# Bridges

- **[[Thm - Quotient Manifold Theorem for Free Proper Actions|Quotient manifold theorem for free proper actions]]** — the parent result. The present theorem is its zero-dimensional specialisation: a discrete group is a Lie group of dimension zero, so the quotient has the same dimension as $M$ and the submersion becomes a local diffeomorphism. The two theorems together partition the "good group quotients" of a manifold into the positive-dimensional case (dimension drops, quotient fibred by copies of $G$) and the discrete case (dimension preserved, quotient covered by $M$). One proves the discrete case by feeding "properly discontinuous $\Rightarrow$ free and proper" into the parent theorem and adding the even-covering analysis.

- **[[Def - Covering Space|Covering spaces]]** — the receiving notion. The theorem is the differential-geometric origin of covering maps: whenever a discrete group acts properly discontinuously, the orbit projection *is* a smooth covering map, and every element of $\Gamma$ names one sheet. Conversely, the deck-transformation group of a covering acts properly discontinuously on the total space, so "properly discontinuous action of a discrete group" and "regular (normal) covering with deck group $\Gamma$" are two descriptions of the same object; this is the bridge along which the theorem enters the classification of coverings by subgroups of $\pi_1$.

- **[[Def - Universal Cover|Universal cover as a principal bundle with discrete structure group]]** — the gauge-theoretic payoff. When $M$ is simply connected, the covering $\pi \colon M \to \Gamma \backslash M$ produced here is the universal cover of $\Gamma \backslash M$, and $\Gamma \cong \pi_1(\Gamma \backslash M)$ acts freely, making $M \to \Gamma \backslash M$ a **principal $\Gamma$-bundle** — the simplest instance of the principal bundles that carry connections in later chapters, here with the discrete structure group $\Gamma$ and no continuous gauge freedom. The construction of every classifying space and every flat connection with prescribed holonomy runs through this bridge.

- **[[Ex - The Torus is a Smooth Manifold via Quotient|The torus as a lattice quotient]]** — the prototype computation. Applying the theorem to $\mathbb{Z}^n \curvearrowright \mathbb{R}^n$ produces $T^n$ with its covering $\mathbb{R}^n \to T^n$, and this single example already exhibits every feature: a preserved dimension, evenly covered patches (small open cubes), the deck group $\mathbb{Z}^n \cong \pi_1(T^n)$, and the descent of the flat metric. It is the concrete anchor for the whole theorem.

---

# Unlocked by This

> [!tip] Deck transformations and the Galois correspondence *(from Algebraic Topology)*
> Once every properly discontinuous action gives a covering, the converse populates the theory: for a connected, locally path-connected, semilocally simply connected base, connected coverings correspond to conjugacy classes of subgroups of $\pi_1$, with normal subgroups giving exactly the coverings that arise as $\Gamma \backslash M$ for a properly discontinuous $\Gamma$. See [[Thm - Galois Correspondence for Covering Spaces]].

> [!tip] Mapping tori and fibre bundles over the circle *(from Bundle Theory)*
> The $\mathbb{Z}$-action $k \cdot (t, f) = (t + k, \phi^k(f))$ turns any diffeomorphism $\phi$ into a smooth fibre bundle over $S^1$ whose monodromy is $\phi$; every fibre bundle over $S^1$ arises this way. This is the first construction of a non-trivial bundle in the series and is developed in **Gauge Theory III**.

> [!tip] Space forms and locally symmetric spaces *(from Riemannian Geometry)*
> A discrete group of isometries acting properly discontinuously and freely on a simply connected model space $\mathbb{R}^n$, $S^n$, or $\mathbb{H}^n$ produces a **space form** — a complete manifold of constant curvature — with the model metric descending through the covering. Flat tori, spherical space forms, and hyperbolic surfaces $\Gamma \backslash \mathbb{H}^2$ are all instances.
