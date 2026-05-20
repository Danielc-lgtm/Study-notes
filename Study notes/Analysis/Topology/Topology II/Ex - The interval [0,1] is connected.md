---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Connected Space"
  - "Def - Topological Space"
  - "Def - Continuous Map"
tags: [analysis, topology, connectedness]
---

# Problem Statement

Show that the closed unit interval $[0, 1] \subseteq \mathbb{R}$ with its standard subspace topology is connected.

The classical hint, due to Bredon, is the right one: suppose by contradiction that $[0, 1] = U \sqcup V$ where $U, V$ are nonempty open subsets of $[0, 1]$ with $U \cap V = \emptyset$, and (without loss of generality) $1 \in V$. Consider the supremum
$$s = \sup(U).$$
Derive a contradiction from each of the cases $s \in U$ and $s \in V$.

**Recall:**

The relevant objects are the connectedness definition and the standard topology on $[0,1]$.

![[Def - Connected Space#The Definition]]

A subset $U \subseteq [0, 1]$ is **open** in the subspace topology if and only if $U = [0, 1] \cap W$ for some open $W \subseteq \mathbb{R}$, where openness in $\mathbb{R}$ is the usual notion: every point has an $\varepsilon$-interval around it inside the set. Concretely, $U$ is open in $[0, 1]$ exactly when for every $x \in U$ there is $\varepsilon > 0$ with $[0, 1] \cap (x - \varepsilon, x + \varepsilon) \subseteq U$.

The supremum $s = \sup(U)$ exists because $U \subseteq [0, 1]$ is nonempty and bounded above by $1$. We have $s \in [0, 1]$, and there are points of $U$ arbitrarily close to $s$ from below (the defining property of the supremum).

---

# Convergent Strategy

**Problem class.** Direct verification of connectedness from the definition. The route is the standard one for *negative* statements: assume the negation (a separation exists) and derive a contradiction. The single tool available is the order completeness of $\mathbb{R}$ — the existence of the supremum is what converts an abstract decomposition into a *specific* point one can argue about.

**Assumption pattern.** A separation $[0,1] = U \sqcup V$ is given with $U, V$ open and nonempty and (by convention) $1 \in V$. The interval $[0, 1]$ inherits two structural features: it is bounded and complete in the order, so every nonempty bounded subset has a supremum.

**Theorem routing.** No prior theorems beyond the order completeness of $\mathbb{R}$. The key step is the dichotomy "$s \in U$ or $s \in V$" — exhaustive by the assumed partition — combined with the openness of whichever set contains $s$. Each branch leads to a contradiction with $s = \sup(U)$ (in one case $s$ should not be the largest, in the other case there should be points of $U$ close to $s$ from below).

**Key decision point.** The non-obvious step is forming $\sup(U)$. The intuition: if $U$ and $V$ partition $[0,1]$ with $U$ "on the left" and $V$ "on the right" (which is what $1 \in V$ suggests), the *boundary* between them ought to be a single point — but neither $U$ nor $V$ can claim it, because both are open, and the boundary cannot lie in an open set arbitrarily close to its complement.

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Direct subcover/separation extraction from the open-set definition.** To prove a connectedness statement directly, assume the negation (a separation exists), name the two open pieces $U, V$, and pick a specific point of contention using order completeness.

2. **Use order completeness of $\mathbb{R}$ to extract a critical point.** The supremum $s = \sup(U)$ is the only well-defined point one can name without further information about $U$ or $V$. It serves as the place where the two cases of the dichotomy bite.

3. **Exploit openness to find an $\varepsilon$-interval inside a set.** When $s$ lies in an open set, an interval $(s - \varepsilon, s + \varepsilon) \cap [0, 1]$ lies inside it. This is the "breathing room" of openness, and it is the contradiction-engine: $s$ being a supremum says nothing on either side of it should be safe.

---

# Hints

> [!note]- Hint 1
> Suppose $[0, 1] = U \sqcup V$ with $U, V$ nonempty, open, disjoint, and $1 \in V$. The single named point you can produce is $s = \sup(U)$. Since $0 \in [0, 1] = U \cup V$ and $1 \in V$, the point $0$ might be in either set; what is important is that $U$ is nonempty so $\sup(U)$ exists and lies in $[0, 1]$.

> [!note]- Hint 2
> Where is $s$? It lies in $U$ or $V$. Treat each case separately. In each, use the *openness* of whichever set contains $s$ to find an interval around $s$ inside that set, and show this contradicts $s = \sup(U)$.

> [!note]- Hint 3
> Case $s \in U$: openness of $U$ gives an interval $(s - \varepsilon, s + \varepsilon) \cap [0, 1] \subseteq U$. But this means there is a point larger than $s$ in $U$ (provided $s < 1$), contradicting that $s$ is an upper bound. Also note $s \neq 1$ — because $1 \in V$.
>
> Case $s \in V$: openness of $V$ gives an interval $(s - \varepsilon, s + \varepsilon) \cap [0, 1] \subseteq V$. But points of $U$ are arbitrarily close to $s$ from below (since $s = \sup U$), so some point of $U$ lies in this interval, hence in $V$ — contradicting $U \cap V = \emptyset$.

---

# Solution

The argument is one of the cleanest applications of order completeness in mathematics: a hypothesised separation $[0, 1] = U \sqcup V$ forces us to look at the boundary between $U$ and $V$, and the boundary cannot lie in either open set without contradicting either the supremum or the openness.

**Step 1: Set up the supremum.**

Assume for contradiction that $[0, 1] = U \sqcup V$ with $U, V$ open in $[0, 1]$, both nonempty, disjoint, and $1 \in V$. Let $s = \sup(U) \in [0, 1]$. Since $[0, 1] = U \cup V$, $s \in U$ or $s \in V$. We rule out both.

> [!note]- Derivation
> The set $U$ is nonempty and bounded above by $1$, so $\sup(U)$ exists in $\mathbb{R}$ by order completeness. Since every element of $U$ lies in $[0, 1]$, we have $0 \leq \sup(U) \leq 1$, so $s \in [0, 1]$. The interval $[0, 1] = U \sqcup V$ partitions $[0, 1]$, so the point $s$ — which belongs to $[0, 1]$ — must belong to exactly one of $U$ or $V$.

**Step 2: Rule out $s \in U$.**

If $s \in U$, then openness of $U$ gives an interval $[0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq U$ for some $\varepsilon > 0$. Since $1 \in V$ and $U \cap V = \emptyset$, $s \neq 1$, so $s < 1$ and we can take $\varepsilon$ small enough that $s + \varepsilon/2 \in [0, 1]$. Then $s + \varepsilon/2 \in U$, contradicting that $s$ is an upper bound for $U$.

> [!note]- Derivation
> Suppose $s \in U$. By definition of the subspace topology, $U$ open in $[0, 1]$ means: there is an open $W \subseteq \mathbb{R}$ with $U = [0, 1] \cap W$. Since $s \in W$ open in $\mathbb{R}$, there is $\varepsilon > 0$ with $(s - \varepsilon, s + \varepsilon) \subseteq W$, hence
> $$[0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq U.$$
> Now $1 \in V$ and $V$ is disjoint from $U$, so $1 \notin U$, hence $s \neq 1$, hence $s < 1$. Choose $\varepsilon$ also small enough that $s + \varepsilon/2 < 1$, which is possible since $s < 1$. Then $s + \varepsilon/2 \in [0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq U$, but $s + \varepsilon/2 > s$, contradicting $s$ being an upper bound for $U$.

**Step 3: Rule out $s \in V$.**

If $s \in V$, then openness of $V$ gives $[0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq V$ for some $\varepsilon > 0$. By definition of the supremum, there is a point $u \in U$ with $s - \varepsilon < u \leq s$. Then $u \in U \cap V$, contradicting $U \cap V = \emptyset$.

> [!note]- Derivation
> Suppose $s \in V$. By the same openness argument as in Step 2, there is $\varepsilon > 0$ with $[0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq V$.
>
> If $s = 0$, then $U \subseteq [0, s] = \{0\} \subseteq V$ (since $s$ is an upper bound for $U$ and $s = 0$, so $U \subseteq \{0\}$, but $0 = s \in V$). But $U$ is nonempty, so $0 \in U$, contradicting $0 \in V$. So $s > 0$.
>
> Now $s = \sup(U)$ and $s > 0$, and $U$ is nonempty. By the definition of supremum, for every $\delta > 0$ there is $u \in U$ with $s - \delta < u \leq s$. Take $\delta = \varepsilon$ (and $\delta = \min(s, \varepsilon)$ to ensure $u \geq 0$): some $u \in U$ satisfies $u > s - \varepsilon$ and $u \leq s$. Hence $u \in [0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq V$. But also $u \in U$, so $u \in U \cap V = \emptyset$ — contradiction.

> [!note]- Complete formal solution
> Assume for contradiction that $[0, 1] = U \sqcup V$ where $U$ and $V$ are disjoint nonempty open subsets of $[0, 1]$ and (relabel if needed) $1 \in V$. Set $s = \sup(U)$; this exists because $U \neq \emptyset$ is bounded above by $1$, and $s \in [0, 1]$.
>
> By the partition, exactly one of $s \in U$ or $s \in V$ holds.
>
> *Case $s \in U$.* By openness of $U$ in $[0, 1]$, there is $\varepsilon > 0$ with $[0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq U$. Since $1 \in V$ and $V \cap U = \emptyset$, we have $1 \notin U$, so $s < 1$. Shrinking $\varepsilon$ if necessary so $s + \varepsilon/2 < 1$, the point $s + \varepsilon/2$ lies in $[0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq U$ and is strictly greater than $s$, contradicting that $s$ is an upper bound for $U$.
>
> *Case $s \in V$.* By openness of $V$, there is $\varepsilon > 0$ with $[0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq V$. By definition of supremum, there exists $u \in U$ with $\max(s - \varepsilon, 0) < u \leq s$. Then $u \in [0, 1] \cap (s - \varepsilon, s + \varepsilon) \subseteq V$, but $u \in U$, contradicting $U \cap V = \emptyset$. (If $U = \{0\}$, then $s = 0 \in V$ gives $0 \in V$ and $0 \in U$, an immediate contradiction.)
>
> Both cases are absurd, so no such separation $U \sqcup V$ exists, and $[0, 1]$ is connected. $\blacksquare$

---

# Key Takeaways

**The supremum is the canonical "boundary point" between a hypothesised pair of open sets in $\mathbb{R}$, and it is the only named point one can extract from a separation.** Whenever you are asked to prove an order-related connectedness or continuity statement in $\mathbb{R}$ — connectedness of intervals, the intermediate value theorem, the existence of a fixed point of an increasing self-map of $[0, 1]$ — the move is the same: assume the negation, take a supremum of one of the sets involved, and use the dichotomy "$s$ is in one set or the other" to extract a contradiction from the openness or order property of each. This *supremum-of-a-set* technique is the order-theoretic substitute for compactness, and it predates the abstract topological definition by a century. It works specifically because $\mathbb{R}$ is order-complete; on $\mathbb{Q}$ the supremum may fail to exist, and indeed $\mathbb{Q}$ is disconnected.

**Openness gives you breathing room around any of its points; supremum says there is no breathing room from below.** The contradiction in this proof has a single underlying shape, applied twice with sides swapped. If $s$ lies in the open set, *both* sides of $s$ have breathing room — but the supremum has elements arbitrarily close on the left and is itself an upper bound, so "arbitrarily close on the right" is forbidden. If $s$ lies in the *other* open set, breathing room on the left is what is forbidden — but the supremum forces points of $U$ to be arbitrarily close on the left, intruding into the other open set. The deeper version of this pattern is the *boundary lemma*: in any topological space, $\partial U \cap U = \emptyset$ (the boundary of an open set does not meet the open set), but $\partial U \subseteq \overline{U}$. A supremum is a candidate boundary point, and a separation forces the boundary into one of two pieces neither of which can house it.

**Connectedness of $[0, 1]$ propagates everywhere via continuous images and overlapping unions, so this single proof unlocks a large fraction of topology.** From $[0, 1]$ connected, $[a, b]$ is connected by the linear homeomorphism $t \mapsto a + (b-a)t$. From there, $\mathbb{R} = \bigcup_n [-n, n]$ is connected as a union of overlapping connected sets sharing $0$ (by [[Thm - Union of Overlapping Connected Sets is Connected]]). From $\mathbb{R}$ connected, $\mathbb{R}^n$ is connected by induction on dimension (using product-of-connected-is-connected). From $\mathbb{R}^n$ connected, any path-connected space is connected (the image of $[0, 1]$ under a path is connected, and paths joining all points to a basepoint exhibit a union of overlapping connected sets). Without this lemma, the whole apparatus collapses: there would be no source of connectedness in classical mathematics.

**The two-set-separation argument is the prototype for every "no nontrivial decomposition" proof in topology and algebra.** The same shape — assume $X = A \sqcup B$ nontrivial, derive a contradiction from a specific element of $A$ — appears in proving simplicity of groups (no nontrivial normal subgroups), connectedness of $\operatorname{Spec} R$ for an indecomposable ring, irreducibility of a topological space, and primality of an ideal. The general lesson: a "no decomposition" property is best proved by assuming a decomposition and extracting a specific witness (a generator, a boundary point, an idempotent) whose existence is contradictory. Mastering this pattern in the simplest case — $[0, 1]$ — is preparation for every harder instance.
