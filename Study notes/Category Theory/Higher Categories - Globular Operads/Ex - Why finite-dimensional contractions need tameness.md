---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Contraction on a Globular Operad"
  - "Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)"
  - "Def - Globular Operad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

In the finite-dimensional ($n$-category) theory, a [[Def - Contraction on a Globular Operad|contraction]] is a *precontraction on a tame map*, where a map of $n$-globular sets is **tame** if any two parallel $n$-cells with the same image are equal. Investigate why this extra condition is needed:

(a) Show that for an $n$-globular operad, precontractibility makes the top-dimensional source-target pairing $(s, t) : P(\pi) \to \mathrm{Par}_P(\pi)$ *surjective*, and tameness makes it *injective*, so a contraction makes it a *bijection* — hence $P(\pi)$ in the top dimension is determined as $\mathrm{Par}_P(\pi)$.

(b) Exhibit a precontractible $n$-operad that is **not** contractible (the top pairing is surjective but not injective), and explain why no dimension $n+1$ is available to remedy it.

(c) Explain why the infinite-dimensional ($\omega$) theory needs **no** tameness condition.

**Recall:**

For an $n$-globular operad $P$, a [[Def - Contraction on a Globular Operad|precontraction]] supplies lifts of parallel pairs in dimensions $1 \le m \le n$ (the source/target/shape conditions). A map $q$ is **tame** if any two parallel top-dimensional cells $\alpha^-, \alpha^+$ with $q(\alpha^-) = q(\alpha^+)$ satisfy $\alpha^- = \alpha^+$; a **contraction** is a precontraction on a tame map. The source-target pairing is $(s,t) : P(\pi) \to \mathrm{Par}_P(\pi)$, $\theta \mapsto (s\theta, t\theta)$. In the $\omega$-theory there is no top dimension. A [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)|weak n-category]] is an $L_n$-algebra for the initial tame $n$-operad-with-contraction.

---

# Convergent Strategy

**Problem class:** This is a *subtlety-analysis* problem feeding the topic page's truncation discussion. The goal is to understand exactly why the finite-dimensional definition differs from the infinite one by a single condition (tameness), by analyzing the source-target pairing in the top dimension. The route is "precontraction $=$ surjectivity, tameness $=$ injectivity, contraction $=$ bijectivity; the top dimension cannot defer".

**Assumption pattern:** The decisive structural fact is that a precontraction is a *section* of the source-target pairing, hence makes it surjective; tameness is *injectivity* of that pairing. The presence of a "top dimension with nothing above" is the signal that the relation between parallel cells must be an equality (handled in dimension $n$) rather than a higher cell (deferred to $n+1$). Recognizing "surjective $+$ injective $=$ bijective $=$ determined by the pairs below" is the unlock.

**Theorem routing:** Route through the source-target pairing analysis (Leinster 9.3): a precontraction is a one-sided inverse to $(s,t)$, so $(s,t)$ is surjective; tameness is injectivity of $(s,t)$ in dimension $n$; together they force $(s,t)$ bijective, so $P(\pi) \cong \mathrm{Par}_P(\pi)$ in dimension $n$, determining $P$ from its $(n-1)$-part. For (b), route through an explicit failure of injectivity. For (c), route through "the $\omega$-theory always has a dimension $n+1$ to receive the lift, so surjectivity (precontraction) suffices and uniqueness is deferred forever".

**Key decision point:** The non-obvious choice is to analyze contractibility through the *bijectivity* of the source-target pairing rather than through the lifts directly. The tempting alternative — defining a contraction only as "lifts exist" — misses that in the top dimension lifts existing (surjective) is not enough; one also needs them essentially unique (injective), because there is no higher dimension to relate two different lifts. Seeing the pairing as the right object reveals tameness as the missing injectivity.

---

# Legal Operations Used

1. **Operation 8 from the topic page (enforce tameness to strictify the top dimension).** This is the exercise's central content: tameness is the top-dimensional injectivity that the finite theory needs.

2. **Operation 3 from the topic page (contraction lifts), analyzed via the pairing.** A precontraction is recast as a section of $(s,t)$, the cleaner object for the analysis.

---

# Hints

> [!note]- Hint 1
> A precontraction $\chi_\pi$ assigns to each parallel pair a lift with that source and target. In terms of the pairing $(s,t) : P(\pi) \to \mathrm{Par}_P(\pi)$, this says $(s,t) \circ \chi_\pi = \mathrm{id}$ — so $\chi_\pi$ is a *section* and $(s,t)$ is *surjective*.

> [!note]- Hint 2
> Tameness says distinct parallel top-cells with the same image are equal — i.e. $(s,t)$ is *injective* in dimension $n$ (two top-operations with the same source-target pair are equal). Surjective plus injective is bijective.

> [!note]- Hint 3
> Bijectivity of $(s,t)$ in dimension $n$ means $P(\pi) \cong \mathrm{Par}_P(\pi)$ for top-dimensional $\pi$ — the top fibre is *exactly* the parallel pairs from below. So a contractible $n$-operad is completely determined by its $(n-1)$-dimensional part.

> [!note]- Hint 4
> For (b), build an $n$-operad where two distinct top-operations have the same source and target (so $(s,t)$ is not injective) but every parallel pair still lifts (so it is surjective). For (c), note that in the $\omega$-theory two competing top-lifts would be parallel cells in the *next* dimension, which exists — so they can be related by a lift there, and uniqueness is never required.

---

# Solution

The solution recasts precontractibility and tameness as surjectivity and injectivity of the source-target pairing (Step 1), exhibits a precontractible-not-contractible operad (Step 2), and explains the absence of tameness in the $\omega$-theory (Step 3). The pivot is "the top dimension cannot defer, so the relation between competing lifts must be an equality".

**Step 1: precontraction $=$ surjective, tameness $=$ injective, contraction $=$ bijective.**

> [!note]- Derivation
> A precontraction $\chi$ on an $n$-operad $P$ supplies, for each $\pi$ and each parallel pair $(\alpha^-, \alpha^+) \in \mathrm{Par}_P(\pi)$, an operation $\chi_\pi(\alpha^-, \alpha^+) \in P(\pi)$ with $s = \alpha^-$, $t = \alpha^+$. In terms of the source-target pairing
> $$
> (s, t) : P(\pi) \longrightarrow \mathrm{Par}_P(\pi), \qquad \theta \mapsto (s\theta, t\theta),
> $$
> this says precisely $(s,t) \circ \chi_\pi = \mathrm{id}_{\mathrm{Par}_P(\pi)}$: the precontraction is a *section*, so $(s,t)$ is **surjective**. Now tameness of the map $d$ underlying $P$ says: any two parallel top-dimensional ($n$-)operations with the same image are equal — equivalently, two $n$-operations with the same source-target pair are equal, which is exactly that $(s,t)$ is **injective** in dimension $n$. A *contraction* is a precontraction on a tame map, so in the top dimension $(s,t)$ is both surjective and injective, hence a **bijection**:
> $$
> (s, t) : P(\pi) \xrightarrow{\ \cong\ } \mathrm{Par}_P(\pi) \qquad (\pi \text{ top-dimensional}).
> $$
> Consequently the top fibre $P(\pi)$ is *exactly* the set of parallel pairs $\mathrm{Par}_P(\pi)$ from the dimension below: a contractible $n$-operad is entirely determined by its $(n-1)$-dimensional part. This is the precise structural meaning of "coherence in the top dimension becomes equality".

**Step 2: a precontractible non-contractible operad.**

> [!note]- Derivation
> We want an $n$-operad whose top pairing is surjective but not injective. Take $n = 2$ for concreteness. Build a $2$-operad $P$ that, in dimension $1$, has the trees (so it has genuine parallel pairs of $1$-operations, e.g. the two bracketings of three arrows), and in dimension $2$ has, for each parallel pair $(\alpha^-, \alpha^+)$, *two distinct* operations $\theta_1, \theta_2 \in P(\pi)$ both with source $\alpha^-$ and target $\alpha^+$. Then:
> - $(s,t) : P(\pi) \to \mathrm{Par}_P(\pi)$ is **surjective** — every parallel pair is hit (by $\theta_1$, say), so $P$ admits a precontraction (choose $\chi_\pi(\alpha^-,\alpha^+) = \theta_1$);
> - but $(s,t)$ is **not injective** — $\theta_1 \neq \theta_2$ yet they have the same source-target pair, so $P$ is **not tame**, hence **not contractible**.
>
> Why can this not be repaired? In a *weak $2$-category*, the two competing top-operations $\theta_1, \theta_2$ would need to be related by a cell that witnesses them as equivalent — but such a cell would be a $3$-cell, and there is **no dimension $3$** in a $2$-operad. With nowhere to put the witnessing cell, the only way to make $\theta_1$ and $\theta_2$ cohere is to *identify* them, $\theta_1 = \theta_2$ — which is exactly the tameness condition. So a precontractible-but-not-tame $2$-operad carries spurious distinct parallel top cells that ought to be equal but cannot be related; tameness forbids exactly this.

**Step 3: the $\omega$-theory needs no tameness.**

> [!note]- Derivation
> In the infinite-dimensional theory there is *no* top dimension. Suppose two operations $\theta_1, \theta_2 \in L(\pi)$ have the same source-target pair. Then $\theta_1, \theta_2$ are themselves a *parallel pair* in dimension $\dim\pi$, over the boundary of a $(\dim\pi + 1)$-dimensional pasting diagram — and that dimension *exists*. The contraction, acting there, lifts $(\theta_1, \theta_2)$ to a cell witnessing them as equivalent. So in the $\omega$-theory there is never any need to *identify* competing lifts; they are related by a higher cell, deferred upward forever. Surjectivity of the pairing (precontraction) is therefore enough, and injectivity (tameness) is *not* imposed — indeed imposing it would force coherence cells to be equalities one dimension down, collapsing weakness back to strictness. The whole subtlety of the finite case is the absence of the next dimension; the infinite case, paradoxically, is *simpler* because it never runs out of room.

> [!note]- Complete formal solution
> *(a)* A precontraction $\chi_\pi$ satisfies $(s,t)\circ\chi_\pi=\mathrm{id}$, so $(s,t):P(\pi)\to\mathrm{Par}_P(\pi)$ is surjective. Tameness says two parallel top-operations with equal image (equal source-target pair) are equal, i.e. $(s,t)$ is injective in the top dimension. A contraction (precontraction on a tame map) thus makes $(s,t)$ bijective in dimension $n$, so $P(\pi)\cong\mathrm{Par}_P(\pi)$ there and $P$ is determined by its $(n-1)$-part.
>
> *(b)* Take a $2$-operad with the trees in dimension $1$ (genuine parallel pairs) and, in dimension $2$, two distinct operations $\theta_1\neq\theta_2$ with the same source-target pair for some parallel pair. Then $(s,t)$ is surjective (precontractible) but not injective (not tame), so $P$ is not contractible. It cannot be repaired because relating $\theta_1,\theta_2$ requires a $3$-cell, which a $2$-operad lacks; the only fix is to identify them — which is tameness.
>
> *(c)* In the $\omega$-theory, two competing lifts $\theta_1,\theta_2$ are a parallel pair in the *next* (existing) dimension and are related by a contraction lift there; uniqueness is deferred upward forever, so no tameness is needed, and imposing it would collapse weakness to strictness. $\blacksquare$

---

# Key Takeaways

**A contraction is a section of the source-target pairing; tameness is its injectivity.** The cleanest way to hold the entire contraction concept — and the one this exercise installs — is as conditions on the pairing $(s,t) : P(\pi) \to \mathrm{Par}_P(\pi)$. A precontraction makes it surjective (every parallel pair has a lift); tameness makes it injective (lifts with the same boundary are equal); a contraction makes it bijective in the top dimension. This recasting turns vague talk of "fillers" into a sharp statement about a function being onto, one-to-one, or both, and it immediately yields the structural payoff: in the top dimension the fibre is *exactly* the parallel pairs below, so a contractible $n$-operad is determined by its lower part. The trigger: whenever analyzing filling conditions, look at the relevant evaluation/boundary map and ask which of surjective/injective/bijective the condition imposes.

**The top dimension cannot defer, so its coherence is forced to be equality.** The conceptual heart is that weakness works by *deferral*: a relation between competing composites is witnessed by a higher cell, which is itself only related up to a yet-higher cell, indefinitely. This deferral requires a next dimension to exist. In an $n$-category the top dimension has no successor, so the deferral chain must terminate — and the only way to terminate it is to make the top relation an *equality* (tameness). This is why classical coherence theorems ("all diagrams commute") are top-dimensional phenomena: they are deferral chains forced to bottom out. The transferable insight: finite-dimensional truncations of "everything up to coherence" theories acquire strictness *at the top* precisely because there is nowhere left to defer; the same mechanism gives Mac Lane coherence in [[Thm - Weak 2-Categories are Bicategories]].

**The infinite-dimensional theory is simpler than the finite one.** Counterintuitively, the $\omega$-theory needs *no* tameness condition and is in that sense cleaner: it never runs out of room, so every competing pair of lifts is related by a cell one dimension up, and uniqueness is never demanded. The finite theory is the one with the extra subtlety, because truncation creates a top dimension that must be handled specially. This inverts the usual expectation that infinite objects are harder; here the infinite object is the natural one and the finite truncations are the awkward special cases. The lesson for working with truncated higher structures: expect the top dimension to behave differently (strictly), and expect the un-truncated version to be more uniform. See the precontraction/contraction distinction in [[Def - Contraction on a Globular Operad]] and its role in the weak-$n$-category definition in [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)]].
