---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Basis and Subbasis for a Topology"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space and $x$ a point of $X$. A **neighbourhood** of $x$ — typically written $N$ or $M$ — is a subset of $X$ containing an open set that contains $x$. The collection of all neighbourhoods of $x$ is denoted $\mathcal{N}(x)$; a **neighbourhood basis** at $x$ is denoted $\mathcal{B}_x$. Open balls in a metric space are $B_\varepsilon(x) = \{y : d(x,y) < \varepsilon\}$. The full notation registry sits on the parent page [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

The definition of a neighbourhood is curious at first sight: a neighbourhood of $x$ need not itself be an open set. One could simplify the language by *defining* a neighbourhood to mean "an open set containing $x$", and many books in fact do. So we should ask why the more permissive definition exists, and what it buys.

The answer is that "around $x$ there is room to move" is a more flexible and primitive notion than "an open set containing $x$". The intuition we want to capture is that of a *region with $x$ in its interior* — a piece of the space that surrounds $x$ with at least a little wiggle room in every direction. An open set containing $x$ certainly is such a region, but so is, for example, the closed interval $[-1, 1]$ as a neighbourhood of $0$ in $\mathbb{R}$: it contains $(-1, 1)$, which is open and contains $0$, so there is room around $0$ inside $[-1, 1]$ — even though $[-1, 1]$ has boundary points where the room runs out. Declaring such a set a neighbourhood of $0$ is what lets us say things like "$f$ is bounded in a neighbourhood of $0$" using a closed interval, which is often the most natural form of the statement.

There is a precise structural reason too. We frequently want to talk about the local behaviour of a function or sequence *near* $x$ without committing to any particular open set. The neighbourhood language gives us a *filter* of sets at $x$: closed under enlargement (any superset of a neighbourhood is a neighbourhood) and closed under finite intersection (two neighbourhoods of $x$ together leave room around $x$, since open sets are closed under finite intersection). The filter is the right algebraic object for "local around $x$", and dropping the openness requirement is what makes it a filter rather than merely a base.

A second question is why we then add the auxiliary notion of a **neighbourhood basis**. The neighbourhood filter $\mathcal{N}(x)$ is often unwieldy — every set containing $(-\delta, \delta)$ is a neighbourhood of $0$ in $\mathbb{R}$, an enormous collection. But a much smaller family is *generating* for it: the open intervals $(-\delta, \delta)$ themselves, or even the rational-radius intervals $(-1/n, 1/n)$, suffice — every neighbourhood of $0$ contains one of these. The smaller family is the **basis**, and it lets us check local conditions by examining only a tractable family rather than the entire filter. The metric balls $B_{1/n}(x)$ are the prototype, and the very existence of such a *countable* basis is what makes metric spaces behave like analysis: this is the content of [[Def - First and Second Countable|first countability]].

The split between neighbourhood and neighbourhood basis mirrors the split between "topology" and "basis for a topology". In each pair, the larger object is the closed-under-something collection that we actually reason about, and the smaller object is a generating family we can specify in practice. The reason for both notions is the same: working with the full filter would be operationally hopeless; working only with a basis would lose the algebraic closure properties we want. We keep both, and the price is one extra definition.

---

# The Definition

Let $X$ be a topological space and $x \in X$.

**Neighbourhood.** A subset $N \subseteq X$ is a **neighbourhood** of $x$ if there exists an open set $U \in \tau_X$ with
$$x \in U \subseteq N.$$
Equivalently, $x$ lies in the interior of $N$. A neighbourhood need not itself be open; an **open neighbourhood** of $x$ is a neighbourhood that *is* open. The collection of all neighbourhoods of $x$ is written $\mathcal{N}(x)$.

**Neighbourhood basis.** A collection $\mathcal{B}_x \subseteq \mathcal{N}(x)$ is a **neighbourhood basis** (or **local base**) at $x$ if for every neighbourhood $N \in \mathcal{N}(x)$ there is some $B \in \mathcal{B}_x$ with $B \subseteq N$. Equivalently, $\mathcal{N}(x) = \{N \subseteq X : \exists B \in \mathcal{B}_x,\ B \subseteq N\}$.

Two elementary consequences of the definition: $\mathcal{N}(x)$ is closed under finite intersections (the intersection of two open sets containing $x$ is open and contains $x$) and under arbitrary supersets (containing a witness is closed under enlargement). A neighbourhood basis $\mathcal{B}_x$ need not be closed under either operation — it is just a *generating* family.

**Continuity at a point.** A function $f : X \to Y$ between topological spaces is **continuous at $x$** if for every neighbourhood $N$ of $f(x)$ in $Y$, the preimage $f^{-1}(N)$ is a neighbourhood of $x$ in $X$. Equivalently, it suffices to check this for $N$ in some neighbourhood basis at $f(x)$.

---

# Relate to Other Fields / Compression

The neighbourhood filter $\mathcal{N}(x)$ is, formally, a **filter** on $X$ in the sense of order theory: a collection closed under finite intersections and supersets, not containing the empty set. The neighbourhood basis is a **filter base**. So the topological apparatus at a point is an instance of the order-theoretic apparatus of filters and bases — and conversely, *generalized topology* via filters is one route to spaces too pathological for sequences to capture, used in the theory of [[Def - Net Convergence|nets and filter convergence]].

The data of "for every point a filter base of neighbourhoods" is in fact *another way* to specify a topology, alternative to the one starting from open sets. The two specifications are equivalent: given a topology, the neighbourhood filters at every point are determined; given a coherent assignment of neighbourhood filters to every point (satisfying a short list of axioms — see Bredon §2 Problem 5), one recovers a unique topology with those neighbourhood filters. This local-data formulation is what makes the neighbourhood basis the natural tool for *local* questions in topology — continuity at a point, limit at a point, the local structure at a singularity.

In analysis, the neighbourhood basis $\{B_{1/n}(x)\}_{n \geq 1}$ is what powers the sequence-based criterion for closure and continuity: a countable, shrinking family of "test sets" around $x$, which is exactly the data a sequence consumes. The failure of this picture in general topological spaces — which forces nets or filters — is precisely the failure of a countable neighbourhood basis to exist, i.e. the failure of [[Def - First and Second Countable|first countability]].

---

# Examples / Corollaries

**Is an instance — metric balls.** In a metric space $(X, d)$, the closed balls $\overline{B_{1/n}(x)} = \{y : d(x,y) \leq 1/n\}$ form a neighbourhood basis at $x$. So do the open balls $B_{1/n}(x)$. Each closed ball is a neighbourhood (it contains the open ball $B_{1/(n+1)}(x)$, which is open and contains $x$); each open ball is a neighbourhood for the trivial reason of being open. This double presentation — open ball basis and closed ball basis — is one reason the open/closed distinction matters less for neighbourhoods than for opens.

**Is an instance — the whole space.** $X$ itself is a neighbourhood of every point, since $X$ is open and contains every $x$. It is rarely a useful neighbourhood — the point of neighbourhoods is to *localize* — but it is always available, and it is the maximal neighbourhood. The basis $\{X\}$ is a neighbourhood basis at $x$ if and only if $\{X\}$ is the indiscrete topology (no other open sets containing $x$).

**Is NOT an instance — the open interval $(0, 1)$ at $x = 0$ in $\mathbb{R}$.** $(0,1)$ does not contain $0$, hence is not a neighbourhood of $0$. More subtly, even the set $\{0\} \cup (1, 2)$ is not a neighbourhood of $0$ in $\mathbb{R}$ despite containing $0$: there is no open set $U$ with $0 \in U \subseteq \{0\} \cup (1, 2)$, because any open interval around $0$ extends into $(- \delta, 0)$ and is not contained in the right-hand piece. Containment of the *point* is not enough — the neighbourhood must surround the point with open room.

**Is an instance — closed intervals as neighbourhoods.** $[-1, 1]$ is a neighbourhood of $0$ in $\mathbb{R}$, since the open interval $(-1, 1)$ lies inside it and contains $0$. This is the most useful "$N$ is not open" example, and it is the standard one for stating boundedness lemmas. A function $f$ is *locally bounded* at $0$ if there is a neighbourhood of $0$ on which $f$ is bounded — and one can often take that neighbourhood to be a closed interval, which has compactness in $\mathbb{R}^n$ ready to deploy.

**Is NOT an instance — at an isolated point.** If $x \in X$ is an isolated point (the singleton $\{x\}$ is open), then $\{x\}$ is itself an open neighbourhood of $x$, and $\{\{x\}\}$ is a one-element neighbourhood basis. The discrete topology produces this for every point. Note this is the smallest possible neighbourhood basis, and a function $f$ is automatically continuous at every isolated point of its domain — there is nothing to check.

**Corollary — finite intersections of neighbourhood basis elements need not be in the basis.** A neighbourhood basis is *not* generally closed under finite intersections. In $\mathbb{R}$ at $0$, the basis $\{(-1/n, 1/n)\}$ is closed under intersections (intersecting $(-1/n, 1/n)$ and $(-1/m, 1/m)$ gives the smaller one), but the basis $\{(- 1, 1/n) \cup (-1/n, 1)\}$ would not be. The defining property is only that every neighbourhood contains *some* basis element, not that the basis itself is closed under any operations.

**Corollary — characterization of continuity at $x$ via neighbourhood basis.** If $\mathcal{B}_{f(x)}$ is a neighbourhood basis at $f(x)$ in $Y$, then $f$ is continuous at $x$ if and only if $f^{-1}(B)$ is a neighbourhood of $x$ for every $B \in \mathcal{B}_{f(x)}$. The proof is that the neighbourhood filter at $f(x)$ is exactly the family of supersets of elements of $\mathcal{B}_{f(x)}$, and $f^{-1}$ commutes with $\supseteq$. This is what makes the basis the practical tool: one verifies continuity on a small, named family.

**Calibration check.** Verify directly that the rational-radius open balls $B_{1/n}(x)$ form a countable neighbourhood basis at every point of $\mathbb{R}$; that in the [[Def - First and Second Countable|cofinite topology]] on an infinite set $X$, no point has a countable neighbourhood basis (the cofinite open sets are uncountable in number and no countable subfamily generates the filter); and that in any topological space, the open neighbourhoods of $x$ form a neighbourhood basis at $x$ (the trivial basis: every neighbourhood contains an open neighbourhood by definition).

---

# Unlocked by This

> [!tip] First Countability and Sequential Closure *(from this topic)*
> The whole point of demanding a *countable* neighbourhood basis at every point is to make sequences sufficient for topological reasoning. With a countable basis $\{B_n\}$ shrinking to $x$, a sequence $x_n \in B_n$ converges to $x$, and conversely every accumulation point of a sequence is reached by such a basis. The link is made precise by [[Def - First and Second Countable]] and used in [[Thm - Characterizations of the Closure]].

> [!tip] Filters and Convergence *(from General Topology)*
> Once one realizes a neighbourhood basis is a filter base, the natural generalization is to ask about *arbitrary* filter bases on a space — not just those localized at a point. This gives **filter convergence**, an alternative to sequence convergence that captures topology completely even in non-first-countable spaces. Nets are the equivalent intermediate object, defined in §6 of [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].
