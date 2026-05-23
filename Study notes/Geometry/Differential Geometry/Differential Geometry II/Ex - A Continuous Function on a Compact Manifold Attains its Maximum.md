---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Continuous Map"
  - "Def - Compact Space"
  - "Thm - Smooth Maps are Continuous"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $M$ be a compact smooth manifold and let $f : M \to \mathbb{R}$ be a continuous function. Show that $f$ attains its maximum and minimum on $M$ — that is, there exist points $p_{\max}, p_{\min} \in M$ such that
$$f(p_{\max}) = \sup_{p \in M} f(p), \quad f(p_{\min}) = \inf_{p \in M} f(p).$$

In particular, every smooth function on a compact smooth manifold attains its extremum (since smooth maps are continuous by [[Thm - Smooth Maps are Continuous]]).

**Recall:**

The relevant topological notions:

A topological space $X$ is **compact** if every open cover has a finite subcover. (See [[Def - Compact Space]].)

The extreme value theorem in $\mathbb{R}$: a continuous function on a compact subset of $\mathbb{R}^n$ attains its supremum and infimum.

A key result: the continuous image of a compact space is compact. (See [[Thm - Continuous Image of a Compact Space]].)

A continuous map between manifolds:

![[Thm - Smooth Maps are Continuous#Statement]]

— this is the bridge from "smooth $f$" to "continuous $f$" needed to apply continuity-based arguments.

---

# Convergent Strategy

**Problem class:** Application of compactness + continuity to derive an extremal property. This is the canonical "extreme value theorem" pattern, generalized from $\mathbb{R}^n$ to manifolds. The routing is: continuous image of compact is compact $\Rightarrow$ $f(M)$ is a compact subset of $\mathbb{R}$ $\Rightarrow$ closed and bounded $\Rightarrow$ supremum and infimum are attained.

**Assumption pattern:** $M$ is compact (a topological property), $f$ is continuous (also topological — smoothness is not needed for this exercise, although smoothness implies continuity). The compactness of $M$ and continuity of $f$ together control the topology of the image $f(M) \subseteq \mathbb{R}$, and the extremum existence on compact subsets of $\mathbb{R}$ is a one-variable fact (Heine–Borel + extreme value).

**Theorem routing:** From continuity of $f$ ($f^{-1}$ of open is open in $M$) and compactness of $M$, conclude $f(M)$ is compact in $\mathbb{R}$ (via the theorem that continuous images of compact sets are compact). Then $f(M) \subseteq \mathbb{R}$ is closed and bounded (by Heine–Borel). Bounded $\Rightarrow$ $\sup f(M) < \infty$ and $\inf f(M) > -\infty$. Closed $\Rightarrow$ $\sup f(M) \in f(M)$ and $\inf f(M) \in f(M)$ (the supremum and infimum of a closed set in $\mathbb{R}$ are attained). So there exist $p_{\max}, p_{\min} \in M$ with $f(p_{\max}) = \sup f(M)$ and $f(p_{\min}) = \inf f(M)$.

**Key decision point:** The non-obvious move is recognizing that the manifold-theoretic content is *almost zero* — this is a pure topology exercise. The manifold structure on $M$ is irrelevant beyond the compactness; any compact topological space would do. The only "manifold-related" input is the bridge from "smooth $f$" to "continuous $f$" (if the function is given as smooth), which is [[Thm - Smooth Maps are Continuous]]. The reaction pattern to recognize this: any extremal-value question on a compact space reduces to applying continuity of the function to derive compactness of the image, then applying extremum-existence on $\mathbb{R}$.

---

# Legal Operations Used

This exercise sits at the intersection of smooth manifold theory and basic topology, and primarily uses topological operations:

1. **Recognize $C^\infty(M)$ structure to lift algebraic facts (operation 10 from the topic page).** $C^\infty(M)$ is a subset of $C(M)$, and any topological property of continuous functions transfers to smooth functions on the same domain.

2. **Topological operation: continuous image of compact is compact.** This is from [[Thm - Continuous Image of a Compact Space]], and it is the workhorse step.

3. **Real-analysis operation: closed bounded subsets of $\mathbb{R}$ attain sup and inf.** This is the extreme-value theorem in [[Def - Dimension|dimension]] $1$ (or its set-theoretic version: closed sets attain their bounds).

---

# Hints

> [!note]- Hint 1
> The result is a manifold-theoretic restatement of the extreme value theorem from one-variable calculus. The bridge is: a smooth function is continuous, the continuous image of a compact space is compact, compact subsets of $\mathbb{R}$ are closed and bounded, and a closed bounded subset of $\mathbb{R}$ attains its sup and inf.

> [!note]- Hint 2
> Use [[Thm - Smooth Maps are Continuous]] to get continuity of $f$ (if you start from "smooth"). Then use a topological theorem: continuous image of compact is compact (see [[Thm - Continuous Image of a Compact Space]]).

> [!note]- Hint 3
> Once $f(M) \subseteq \mathbb{R}$ is shown to be compact, use Heine–Borel: compact subsets of $\mathbb{R}^n$ are closed and bounded. Bounded $\Rightarrow$ $\sup f(M), \inf f(M)$ are finite. Closed $\Rightarrow$ $\sup f(M), \inf f(M) \in f(M)$.

---

# Solution

The proof is the manifold-theoretic application of the extreme value theorem from one-variable calculus. The routing is: continuity of $f$ (given) + compactness of $M$ (given) $\Rightarrow$ $f(M) \subseteq \mathbb{R}$ is compact $\Rightarrow$ $f(M)$ is closed and bounded $\Rightarrow$ $\sup f(M)$ and $\inf f(M)$ are attained.

**Step 1: $f(M)$ is compact in $\mathbb{R}$.**

$f : M \to \mathbb{R}$ is continuous, and $M$ is compact. By [[Thm - Continuous Image of a Compact Space]], $f(M)$ is a compact subset of $\mathbb{R}$.

> [!note]- Derivation
> The theorem "continuous image of compact is compact" is a direct consequence of the definition of compactness. Let $\{V_\alpha\}$ be an open cover of $f(M)$. Then $\{f^{-1}(V_\alpha)\}$ is an open cover of $M$ (each preimage is open by continuity, the union covers $M$ since the $V_\alpha$ cover $f(M)$). By compactness of $M$, there is a finite subcover $f^{-1}(V_{\alpha_1}), \ldots, f^{-1}(V_{\alpha_k})$ of $M$. Then $V_{\alpha_1}, \ldots, V_{\alpha_k}$ cover $f(M)$: for any $y \in f(M)$, $y = f(p)$ for some $p \in M$, and $p \in f^{-1}(V_{\alpha_j})$ for some $j$, so $y = f(p) \in V_{\alpha_j}$. So $\{V_{\alpha_1}, \ldots, V_{\alpha_k}\}$ is a finite subcover of $f(M)$, hence $f(M)$ is compact.

**Step 2: $f(M)$ is closed and bounded in $\mathbb{R}$.**

By the Heine–Borel theorem ([[Thm - Heine–Borel Theorem]]), compact subsets of $\mathbb{R}^n$ are exactly the closed and bounded subsets. In particular, $f(M) \subseteq \mathbb{R}$ is closed and bounded.

> [!note]- Derivation
> Heine–Borel for $\mathbb{R}$: a subset of $\mathbb{R}$ is compact iff it is closed and bounded.
>
> "Bounded": $f(M) \subseteq [-R, R]$ for some $R > 0$. (Compact in $\mathbb{R}$ implies bounded, since the open cover $\{(-n, n)\}_{n \in \mathbb{N}}$ has a finite subcover when restricted to $f(M)$, the largest of whose $(-n, n)$'s contains $f(M)$.)
>
> "Closed": $f(M)$ is the complement of an open set in $\mathbb{R}$.

**Step 3: the sup and inf of $f(M)$ are attained.**

Set $s = \sup f(M)$ and $i = \inf f(M)$. Since $f(M)$ is bounded, $s, i \in \mathbb{R}$ (not $\pm \infty$). Since $f(M)$ is closed, $s \in f(M)$ and $i \in f(M)$ (the supremum and infimum of a closed subset of $\mathbb{R}$ are attained, because they are limits of sequences in $f(M)$ and closed sets contain their limits).

So there exist $p_{\max}, p_{\min} \in M$ with $f(p_{\max}) = s$ and $f(p_{\min}) = i$.

> [!note]- Derivation
> Closed sets contain their boundary: more specifically, the sup of a non-empty bounded set $S \subseteq \mathbb{R}$ is the limit of a sequence in $S$ (one can take any sequence $s_n \in S$ with $s_n \to \sup S$; such a sequence exists by the definition of supremum). If $S$ is closed, the limit $\sup S$ is in $S$. So $\sup f(M) \in f(M)$, i.e. there exists $p_{\max} \in M$ with $f(p_{\max}) = \sup f(M)$. Symmetric argument for the infimum.

> [!note]- Complete formal solution
> **Theorem.** Let $M$ be a compact topological space and let $f : M \to \mathbb{R}$ be a continuous function. Then $f$ attains its maximum and minimum on $M$.
>
> *Proof.*
>
> *Step 1.* By [[Thm - Continuous Image of a Compact Space]], $f(M) \subseteq \mathbb{R}$ is compact.
>
> *Step 2.* By the Heine–Borel theorem ([[Thm - Heine–Borel Theorem]]), $f(M)$ is closed and bounded in $\mathbb{R}$.
>
> *Step 3.* Set $s = \sup f(M)$ and $i = \inf f(M)$. Boundedness gives $s, i \in \mathbb{R}$.
>
> Since $f(M)$ is closed: any sequence in $f(M)$ that converges in $\mathbb{R}$ has limit in $f(M)$. By the definition of supremum, there exists a sequence $\{y_n\} \subseteq f(M)$ with $y_n \to s$. Hence $s \in f(M)$. Symmetrically, $i \in f(M)$.
>
> So there exist $p_{\max}, p_{\min} \in M$ with $f(p_{\max}) = s$ and $f(p_{\min}) = i$. $\quad\blacksquare$
>
> Applied to a smooth $f$ on a compact smooth manifold: smooth $\Rightarrow$ continuous by [[Thm - Smooth Maps are Continuous]], so the theorem applies. The smooth function attains its maximum and minimum.

---

# Key Takeaways

**Extremum results on manifolds are pure topology with continuity as input.** The manifold structure of $M$ is not used beyond compactness — any compact topological space would give the same theorem. The manifold structure enters only through the implicit "smooth $\Rightarrow$ continuous" bridge if the function is given as smooth rather than directly continuous. The reaction pattern: any extremum question on a manifold reduces to "is the relevant function continuous?" + "is the relevant space compact?", and the answer follows from real-analysis facts about $\mathbb{R}$.

**Continuous image of compact is compact is one of the highest-leverage topological facts.** This single theorem, applied to a continuous $f : X \to Y$ from compact $X$ to any $Y$, immediately gives compactness of $f(X)$ — and compactness of the image is the gateway to many further conclusions (closed image, bounded image when $Y = \mathbb{R}$, attained extremum). The recognition trigger is "compact source + continuous map"; the reaction is "image is compact, with all the structural consequences thereof". This pattern repeats in differential geometry whenever a compact manifold is mapped continuously somewhere: integration becomes finite, supremum norms become attained, sequences have convergent subsequences in the image.

**Compactness + continuity = boundedness on manifolds.** A continuous function on a compact manifold is bounded (its image is bounded). This is one of the most-used facts in analysis on manifolds: it lets you treat smooth functions on compact manifolds as having uniform bounds, which is what powers many global estimates (Sobolev inequalities, elliptic regularity on compact manifolds, the spectral theory of self-adjoint operators on compact Riemannian manifolds). The trigger is any "compact $M$" hypothesis; the reaction is "every continuous function is bounded, and every smooth function attains its extremum".

This exercise is the simplest application of compactness in the smooth-manifold setting. Companion exercises include checking that [[Def - Diffeomorphism|diffeomorphisms]] preserve compactness (a simple consequence of continuity), and that the [[Def - Homeomorphism|homeomorphism]] class of a compact smooth manifold determines its compactness (trivially). The application to existence theorems for critical points of smooth functions (Morse theory) is more elaborate and belongs to [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]. The companion exercise [[Ex - The Inclusion of an Open Submanifold is Smooth]] demonstrates the dual: an open submanifold of a compact manifold need not be compact, so compactness is not inherited by open submanifolds (e.g., $\mathbb{R}^n \subseteq S^n$ via stereographic projection is open in $S^n$ but is itself non-compact).
