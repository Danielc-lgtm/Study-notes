---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Discrete Group and Properly Discontinuous Action"
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $(\mathbb{Q}, +)$ carry the **discrete topology** — so that it is a $0$-dimensional Lie group, a discrete group — and let it act on the real line $\mathbb{R}$ by translation,
$$\mathbb{Q} \times \mathbb{R} \longrightarrow \mathbb{R}, \qquad (q, t) \longmapsto q \cdot t := q + t.$$

Prove the following.

- **(A)** The action is **not** properly discontinuous. Concretely, condition (i) of proper discontinuity fails at *every* point: for each $p \in \mathbb{R}$ and each neighbourhood $U$ of $p$ there is a nonzero $q \in \mathbb{Q}$ with $q \cdot U \cap U \neq \emptyset$. Condition (ii) fails as well: for any two points $s \neq t$ in different orbits and any neighbourhoods $U \ni s$, $V \ni t$, there is a $q \in \mathbb{Q}$ with $q \cdot U \cap V \neq \emptyset$. Both failures are consequences of the fact that every orbit $q \mapsto q + t$ is **dense** in $\mathbb{R}$.

- **(B)** The orbit space $\mathbb{Q}\backslash\mathbb{R}$, with the quotient topology, carries the **indiscrete topology** (the only open sets are $\emptyset$ and the whole space). Since it has more than one point, it is **not Hausdorff** — and so, in particular, cannot be a manifold.

This is Bär's Example 1.5.25. The source disposes of it in two sentences ("any two different orbits are arbitrarily close" and "the quotient $\mathbb{Q}\backslash\mathbb{R}$ is not Hausdorff"); the task is to write out the density argument, deduce the failure of both conditions, and prove the sharp topological statement that the quotient is indiscrete.

**Recall:**

The relevant notion is proper discontinuity for a discrete group action.

![[Def - Discrete Group and Properly Discontinuous Action#The Definition]]

For the action of a discrete group $G$ on a manifold $M$, written $(g, p) \mapsto g \cdot p$, proper discontinuity is the conjunction of two conditions from [[Def - Discrete Group and Properly Discontinuous Action|Bär]]:

- **(i)** for every $p \in M$ there is a neighbourhood $U$ of $p$ with $g \cdot U \cap U \neq \emptyset \Rightarrow g = e$;
- **(ii)** for every pair $p, q \in M$ in different orbits there are neighbourhoods $U \ni p$, $V \ni q$ with $g \cdot U \cap V = \emptyset$ for all $g \in G$.

To *disprove* proper discontinuity it is enough to negate either condition; we negate both, since both fail and the two failures illuminate different features of the dense action.

We also use two elementary facts about the real line, both standard and used without further comment: the rationals are **dense** in $\mathbb{R}$ (every nonempty open interval contains a rational number), and the quotient topology on an orbit space is defined so that a set is open in $\mathbb{Q}\backslash\mathbb{R}$ if and only if its preimage under the projection $\pi : \mathbb{R} \to \mathbb{Q}\backslash\mathbb{R}$ is open in $\mathbb{R}$; equivalently, the open sets of $\mathbb{Q}\backslash\mathbb{R}$ correspond to the $\mathbb{Q}$-**invariant** (saturated) open subsets of $\mathbb{R}$.

---

# Convergent Strategy

**Problem class.** This is a *disprove-a-property* problem paired with a *sharp topological identification*. Part (A) is a negation: to defeat proper discontinuity one need only produce, for the appropriate quantifier structure, a single offending group element. Part (B) goes further than "not Hausdorff" — it pins down the quotient topology exactly, and the non-Hausdorff conclusion falls out as a corollary. Recognising that the quotient is not merely non-Hausdorff but *indiscrete* is what makes the failure vivid: there are no nonconstant continuous functions on it at all.

**Assumption pattern.** Everything is driven by *density of the orbits*. The orbit of any $t$ is $t + \mathbb{Q}$, a translate of $\mathbb{Q}$, hence dense in $\mathbb{R}$. Density is the exact opposite of the "positive separation" that proper discontinuity demands: where the $\mathbb{Z}$-action of the companion exercise had a smallest nonzero displacement and a positive orbit-to-orbit distance, the $\mathbb{Q}$-action has neither — arbitrarily small nonzero rationals exist, and every orbit comes arbitrarily close to every point.

**Theorem routing.** No heavy theorem is needed; the route is elementary. For (A)(i), pick a small enough nonzero rational to translate an interval onto itself. For (A)(ii), use density of the orbit of $s$ to land a translate inside $V$. For (B), characterise the saturated open sets: show that a nonempty $\mathbb{Q}$-invariant open subset of $\mathbb{R}$ must be all of $\mathbb{R}$, because a translate of any open interval by all of $\mathbb{Q}$ already covers $\mathbb{R}$. That leaves only $\emptyset$ and $\mathbb{R}$ as saturated open sets, which is precisely the statement that the quotient is indiscrete.

**Key decision point.** The one step that requires a small idea is proving that a nonempty $\mathbb{Q}$-invariant open set is everything. The move is to note that such a set contains some open interval $(a, b)$ with $a < b$, and that the union of all rational translates $(a, b) + \mathbb{Q} = \bigcup_{q \in \mathbb{Q}} (a + q, b + q)$ is *all* of $\mathbb{R}$: for any real $x$, the interval $(x - b, x - a)$ has positive length $b - a$ and therefore contains a rational $q$, which places $x$ in $(a + q, b + q)$. This "translates of a fixed-length interval by a dense set cover everything" is the crux, and it is exactly the density fact wearing a different hat.

---

# Legal Operations Used

This solution deploys the following legal operations from the topic page's Legal Operations (referred to descriptively here; the orchestrator will reconcile numbering once the topic page is assembled).

1. **Defeat a universal property by exhibiting one offending group element.** Proper discontinuity asserts the existence of *good* neighbourhoods; to negate it, produce, for a given point and any neighbourhood, a specific nonzero $q \in \mathbb{Q}$ that violates the required disjointness.

2. **Use density of an orbit to intersect a prescribed target set.** Because $t + \mathbb{Q}$ is dense, some rational translate of any neighbourhood of $s$ meets any prescribed neighbourhood $V$ of a point $t$; this kills condition (ii).

3. **Compute the quotient topology through saturated open sets.** Identify the open sets of $\mathbb{Q}\backslash\mathbb{R}$ with the $\mathbb{Q}$-invariant open subsets of $\mathbb{R}$, then determine those directly.

4. **Show a nonempty invariant open set is everything by covering with translates.** From an interval inside a nonempty $\mathbb{Q}$-invariant open set, cover $\mathbb{R}$ by rational translates of that interval to force the set to be all of $\mathbb{R}$.

5. **Read non-Hausdorffness off the indiscrete topology.** A space with the indiscrete topology and at least two points cannot separate them by disjoint open sets, hence is not Hausdorff (and not even $T_1$).

---

# Hints

> [!note]- Hint 1
> To show the action is *not* properly discontinuous you only have to break one of the two conditions — but break them by producing an explicit bad rational. For condition (i) at a point $p$, take a neighbourhood $U$ and ask: is there a *small* nonzero rational $q$ such that $q + U$ still overlaps $U$? Small nonzero rationals exist in every neighbourhood of $0$.

> [!note]- Hint 2
> The single fact behind everything is that the orbit $t + \mathbb{Q}$ is *dense* in $\mathbb{R}$: it meets every nonempty open interval. For condition (ii), if $U \ni s$ and $V \ni t$, density of $s + \mathbb{Q}$ inside the interval $V$ gives a rational $q$ with $s + q \in V$; since $s + q \in q \cdot U$ (as $s \in U$), the translate $q \cdot U$ meets $V$.

> [!note]- Hint 3
> For part (B), recall that a subset of $\mathbb{Q}\backslash\mathbb{R}$ is open exactly when its preimage in $\mathbb{R}$ is open — equivalently, the open sets of the quotient are the $\mathbb{Q}$-*invariant* open subsets of $\mathbb{R}$ (open sets $W$ with $W + q = W$ for all $q \in \mathbb{Q}$). So the whole problem is: which $\mathbb{Q}$-invariant open subsets of $\mathbb{R}$ are there?

> [!note]- Hint 4
> Suppose $W \subseteq \mathbb{R}$ is open, nonempty, and $\mathbb{Q}$-invariant. It contains an interval $(a, b)$, $a < b$. Because $W$ is invariant it contains $(a, b) + q$ for every rational $q$. Show $\bigcup_{q \in \mathbb{Q}} (a + q, b + q) = \mathbb{R}$: given any $x$, find a rational in $(x - b, x - a)$. Conclude $W = \mathbb{R}$, so the only saturated open sets are $\emptyset$ and $\mathbb{R}$ — the quotient is indiscrete.

---

# Solution

The plan is to run everything off one fact — the density of each orbit $t + \mathbb{Q}$ — and to draw three conclusions from it. First we break condition (i) at every point by translating a neighbourhood onto itself with a small nonzero rational; then we break condition (ii) by using density to slide a translate of one neighbourhood into another; finally we compute the quotient topology exactly, showing the only saturated open sets are $\emptyset$ and $\mathbb{R}$, so the quotient is indiscrete and therefore not Hausdorff.

**Step 0: The map is a smooth action of the discrete group $\mathbb{Q}$, with dense orbits.**

> [!note]- Derivation
> Write $\theta(q, t) = q + t$. The action axioms hold: $\theta(0, t) = t$, and for $q, r \in \mathbb{Q}$,
> $$\theta\big(q, \theta(r, t)\big) = q + (r + t) = (q + r) + t = \theta(q + r, t) \qquad \text{(associativity of addition).}$$
> Endowed with the discrete topology, $\mathbb{Q}$ is a $0$-dimensional Lie group (a discrete group in the sense of [[Def - Discrete Group and Properly Discontinuous Action|Bär]]), and each translation $t \mapsto q + t$ is smooth, so $\theta$ is a smooth action; its identity element is $e = 0$.
>
> The orbit of $t \in \mathbb{R}$ is
> $$\mathbb{Q} \cdot t = \{q + t : q \in \mathbb{Q}\} = t + \mathbb{Q}.$$
> This set is **dense** in $\mathbb{R}$: for any nonempty open interval $(\alpha, \beta)$, the interval $(\alpha - t, \beta - t)$ has positive length and hence contains a rational $q$ (rationals are dense in $\mathbb{R}$); then $t + q \in (\alpha, \beta)$, so the orbit meets $(\alpha, \beta)$. Two points $s, t$ lie in the same orbit if and only if $t - s \in \mathbb{Q}$.

**Step 1 (Part A, condition (i) fails at every point): A small nonzero rational translates a neighbourhood onto itself.**

For every $p \in \mathbb{R}$ and every neighbourhood $U$ of $p$ there is a nonzero $q \in \mathbb{Q}$ with $q \cdot U \cap U \neq \emptyset$; hence no neighbourhood witnesses condition (i), and (i) fails at $p$.

> [!note]- Derivation
> Fix $p \in \mathbb{R}$ and any neighbourhood $U$ of $p$. Since $U$ is a neighbourhood, it contains an open interval $(p - \delta, p + \delta)$ for some $\delta > 0$. By density of the rationals there is a rational $q$ with
> $$0 < q < 2\delta \qquad \text{(the interval } (0, 2\delta) \text{ contains a rational).}$$
> This $q$ is nonzero. Consider the point $p - \delta + \tfrac{q}{2}$. Because $0 < q < 2\delta$ we have $0 < \tfrac{q}{2} < \delta$, so
> $$p - \delta < p - \delta + \tfrac{q}{2} < p + \delta, \qquad\text{hence}\qquad p - \delta + \tfrac{q}{2} \in (p - \delta, p + \delta) \subseteq U.$$
> Its image under $q$ is $q \cdot \left(p - \delta + \tfrac{q}{2}\right) = p - \delta + \tfrac{q}{2} + q = p - \delta + \tfrac{3q}{2}$; since $0 < \tfrac{3q}{2} < 3\delta$ we cannot immediately place it, so instead we exhibit a common point of $q\cdot U$ and $U$ directly. The overlap of the interval $(p - \delta, p + \delta)$ and its translate $(p - \delta + q, p + \delta + q)$ is nonempty precisely when $q < 2\delta$, which holds; explicitly the point
> $$x := p + \delta - \tfrac{q}{2}$$
> satisfies $x \in (p - \delta, p + \delta) \subseteq U$ (as $0 < \tfrac{q}{2} < \delta$ gives $p - \delta < x < p + \delta$) and also $x \in (p - \delta + q, p + \delta + q)$ (since $x - q = p + \delta - \tfrac{3q}{2} > p - \delta$ because $\tfrac{3q}{2} < 3\delta$ is not yet enough — instead note $x > p - \delta + q \iff \delta - \tfrac{q}{2} > -\delta + q \iff 2\delta > \tfrac{3q}{2}$, i.e. $q < \tfrac{4\delta}{3}$). To avoid the borderline, simply choose $q$ at the outset with $0 < q < \delta$; then $x = p + \delta - \tfrac{q}{2}$ lies in $(p - \delta, p + \delta)$ and in $(p - \delta + q, p + \delta + q)$ because $x - q = p + \delta - \tfrac{3q}{2} > p + \delta - \tfrac{3\delta}{2} = p - \tfrac{\delta}{2} > p - \delta$. Hence
> $$x \in U \cap (U + q) \subseteq U \cap (q \cdot U), \qquad\text{so}\qquad q \cdot U \cap U \neq \emptyset \text{ with } q \neq 0.$$
> As $U$ was an arbitrary neighbourhood of $p$, no neighbourhood of $p$ satisfies "$q \cdot U \cap U \neq \emptyset \Rightarrow q = 0$". Therefore condition (i) fails at $p$, and $p$ was arbitrary.

**Step 2 (Part A, condition (ii) fails): Density slides a translate of one neighbourhood into the other.**

For any $s, t$ in different orbits and any neighbourhoods $U \ni s$, $V \ni t$, there is $q \in \mathbb{Q}$ with $q \cdot U \cap V \neq \emptyset$; hence no separating neighbourhoods exist, and (ii) fails.

> [!note]- Derivation
> Let $s, t$ lie in different orbits, so $t - s \notin \mathbb{Q}$ (Step 0), and let $U \ni s$, $V \ni t$ be arbitrary neighbourhoods. Since $V$ is a neighbourhood of $t$ it contains an open interval $(t - \eta, t + \eta)$ for some $\eta > 0$. By density of the orbit $s + \mathbb{Q}$ (Step 0), this orbit meets $(t - \eta, t + \eta)$: there is $q \in \mathbb{Q}$ with
> $$s + q \in (t - \eta, t + \eta) \subseteq V.$$
> Now $s \in U$, so $s + q = q \cdot s \in q \cdot U$. Thus the point $s + q$ lies in both $q \cdot U$ and $V$:
> $$s + q \in q \cdot U \cap V, \qquad\text{so}\qquad q \cdot U \cap V \neq \emptyset.$$
> Since $U \ni s$ and $V \ni t$ were arbitrary neighbourhoods, there is no pair of neighbourhoods with $q \cdot U \cap V = \emptyset$ for all $q$. Therefore condition (ii) fails. Either failure already shows the action is not properly discontinuous.

**Step 3 (Part B): The saturated open sets are only $\emptyset$ and $\mathbb{R}$.**

A subset of $\mathbb{Q}\backslash\mathbb{R}$ is open if and only if it is $\pi(W)$ for a $\mathbb{Q}$-invariant open $W \subseteq \mathbb{R}$; the only such $W$ are $\emptyset$ and $\mathbb{R}$.

> [!note]- Derivation
> By definition of the quotient topology, $O \subseteq \mathbb{Q}\backslash\mathbb{R}$ is open if and only if $\pi^{-1}(O)$ is open in $\mathbb{R}$. The preimage $\pi^{-1}(O)$ is always a union of orbits, that is a $\mathbb{Q}$-**invariant** set: $W + q = W$ for every $q \in \mathbb{Q}$ (a point lies in $\pi^{-1}(O)$ if and only if its whole orbit does). Conversely every $\mathbb{Q}$-invariant open $W$ is $\pi^{-1}(\pi(W))$ with $\pi(W)$ open. So the open sets of $\mathbb{Q}\backslash\mathbb{R}$ correspond bijectively, via $W \mapsto \pi(W)$, to the $\mathbb{Q}$-invariant open subsets $W$ of $\mathbb{R}$.
>
> **Claim: the only $\mathbb{Q}$-invariant open subsets of $\mathbb{R}$ are $\emptyset$ and $\mathbb{R}$.** Let $W$ be $\mathbb{Q}$-invariant and open with $W \neq \emptyset$; we show $W = \mathbb{R}$. Being open and nonempty, $W$ contains an open interval $(a, b)$ with $a < b$. By $\mathbb{Q}$-invariance, $W \supseteq (a, b) + q = (a + q, b + q)$ for every $q \in \mathbb{Q}$, hence
> $$W \supseteq \bigcup_{q \in \mathbb{Q}} (a + q, \, b + q).$$
> This union is all of $\mathbb{R}$: given any $x \in \mathbb{R}$, the interval $(x - b, x - a)$ has positive length $b - a > 0$, so it contains a rational $q$ (density of $\mathbb{Q}$); then $x - b < q < x - a$, which rearranges to $a + q < x < b + q$, i.e. $x \in (a + q, b + q)$. Since $x$ was arbitrary,
> $$\bigcup_{q \in \mathbb{Q}} (a + q, \, b + q) = \mathbb{R}, \qquad\text{whence}\qquad W = \mathbb{R}.$$
> Therefore the only $\mathbb{Q}$-invariant open subsets of $\mathbb{R}$ are $\emptyset$ and $\mathbb{R}$, and correspondingly the only open subsets of $\mathbb{Q}\backslash\mathbb{R}$ are $\emptyset$ and the whole space: the quotient topology is **indiscrete**.

**Step 4 (Part B): The quotient is not Hausdorff.**

> [!note]- Derivation
> The orbit space $\mathbb{Q}\backslash\mathbb{R}$ has more than one point: two reals $s, t$ give the same point if and only if $t - s \in \mathbb{Q}$, and there exist reals in different cosets — for instance $0$ and $\sqrt{2}$, since $\sqrt{2} - 0 = \sqrt{2} \notin \mathbb{Q}$. (In fact there are uncountably many cosets, since $\mathbb{Q}$ is countable and $\mathbb{R}$ is not.)
>
> Take two distinct points $\pi(s) \neq \pi(t)$. Any open set containing $\pi(s)$ is nonempty, hence by Step 3 equals the whole space $\mathbb{Q}\backslash\mathbb{R}$, and likewise for any open set containing $\pi(t)$. Two open sets each equal to the whole space cannot be disjoint (their intersection is the whole space, which is nonempty). So $\pi(s)$ and $\pi(t)$ cannot be separated by disjoint open neighbourhoods. Therefore $\mathbb{Q}\backslash\mathbb{R}$ is **not Hausdorff**. In particular it is not a topological manifold, since manifolds are Hausdorff by definition — which is the structural reason proper discontinuity, the hypothesis that would have made the quotient a manifold via [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem]], had to fail.

> [!note]- Complete formal solution
> **Claim.** The translation action of $(\mathbb{Q}, +)$ (discrete topology) on $\mathbb{R}$ is not properly discontinuous, and $\mathbb{Q}\backslash\mathbb{R}$ is indiscrete, hence not Hausdorff.
>
> Translation is a smooth action of the discrete group $\mathbb{Q}$ with orbits $t + \mathbb{Q}$, each dense in $\mathbb{R}$ (every open interval contains a point of $t + \mathbb{Q}$, by density of $\mathbb{Q}$); $s, t$ share an orbit iff $t - s \in \mathbb{Q}$.
>
> **(A) Not properly discontinuous.** *Condition (i) fails at every $p$.* Given a neighbourhood $U \supseteq (p - \delta, p + \delta)$, pick a rational $q$ with $0 < q < \delta$. Then $x := p + \delta - \tfrac{q}{2}$ lies in $(p - \delta, p + \delta) \subseteq U$ and satisfies $x - q = p + \delta - \tfrac{3q}{2} > p - \delta$, so $x \in (p - \delta + q, p + \delta + q) = U' + q$ where $U' = (p-\delta,p+\delta)$; thus $x \in U \cap (q \cdot U)$ with $q \neq 0$. *Condition (ii) fails.* For $s, t$ in different orbits and neighbourhoods $U \ni s$, $V \supseteq (t - \eta, t + \eta)$, density of $s + \mathbb{Q}$ gives $q \in \mathbb{Q}$ with $s + q \in V$; as $s \in U$, $s + q \in q \cdot U \cap V$. Either failure shows the action is not properly discontinuous.
>
> **(B) The quotient is indiscrete.** Open sets of $\mathbb{Q}\backslash\mathbb{R}$ correspond to $\mathbb{Q}$-invariant open $W \subseteq \mathbb{R}$. If such a $W$ is nonempty it contains an interval $(a, b)$, $a < b$, and by invariance $W \supseteq \bigcup_{q \in \mathbb{Q}}(a + q, b + q) = \mathbb{R}$ (for any $x$, the interval $(x - b, x - a)$ of length $b - a > 0$ contains a rational $q$, so $x \in (a + q, b + q)$); hence $W = \mathbb{R}$. So the only open subsets of $\mathbb{Q}\backslash\mathbb{R}$ are $\emptyset$ and the whole space. The quotient has $\geq 2$ points (e.g. $\pi(0) \neq \pi(\sqrt{2})$), and two distinct points cannot be separated because every nonempty open set is everything; therefore $\mathbb{Q}\backslash\mathbb{R}$ is not Hausdorff, and not a manifold. $\blacksquare$

---

# Key Takeaways

**To disprove a property whose statement is "there exist good neighbourhoods", exhibit a single bad group element against arbitrary neighbourhoods.** Proper discontinuity is an existential-over-neighbourhoods claim; its negation is universal-over-neighbourhoods and existential-over-group-elements. So the disproof has a fixed shape: take an *arbitrary* candidate neighbourhood and, using the structure of the action, produce one nonzero $q \in \mathbb{Q}$ that spoils the required disjointness. Recognising this quantifier flip is the whole strategic content — one does not need to understand the quotient at all to see the action fails to be properly discontinuous. The same logic disproves free-and-proper-ness, even covering, and evenly-covered conditions throughout the theory: identify the offending element, do not attempt to survey all neighbourhoods. The contrast with the companion exercise [[Ex - The Circle as the Quotient of R by the Integers]] is exact — there the group $\mathbb{Z}$ had a *smallest* nonzero displacement, which supplied a positive radius and made the good neighbourhoods exist; here $\mathbb{Q}$ has arbitrarily small nonzero elements, and that single difference is what collapses the argument.

**Density of the orbits is the precise obstruction to proper discontinuity, and it is worth naming as the diagnostic.** A discrete group acts properly discontinuously only when its orbits are, locally, spread out with a positive gap — that gap is what feeds the separating radius. When orbits are dense the gap is zero everywhere, and both conditions of proper discontinuity fail for the same reason: no neighbourhood can be isolated from its translates, and no two orbits can be separated. So when confronted with a discrete action, the first question to ask is whether the orbits are discrete (positive local separation) or dense; the answer decides properly-discontinuous-or-not before any neighbourhoods are chosen. This dichotomy recurs whenever a countable group acts by translations on a group: $\mathbb{Z} \subseteq \mathbb{R}$ acts properly discontinuously and gives the circle, an irrational-rotation subgroup of the circle acts with dense orbits and gives a non-manifold, and the boundary case between them is exactly the boundary between "closed discrete subgroup" and "dense subgroup".

**Computing a quotient topology exactly — not just its separation properties — is done through the saturated open sets, and often yields more than expected.** The quotient topology is defined by pullback, so the open sets of $\mathbb{Q}\backslash\mathbb{R}$ are in bijection with the invariant (saturated) open subsets of $\mathbb{R}$. Determining those directly here produced a sharp result: the only invariant open sets are $\emptyset$ and $\mathbb{R}$, so the quotient is not merely non-Hausdorff but *indiscrete*, meaning it carries no topological information at all and admits no nonconstant continuous function to any Hausdorff space. The technique — covering the whole space by translates of one interval to force a nonempty invariant open set to be everything — is the reusable core; it works whenever a dense subgroup acts, and it is the same computation that shows the leaf space of an irrational foliation, or the quotient of a group by a dense subgroup, is indiscrete. The transferable diagnostic: to find a quotient's topology, list its saturated open sets; when a dense group acts, expect that list to contain only the two trivial members, and read off both non-Hausdorffness and the total loss of separation from that.
