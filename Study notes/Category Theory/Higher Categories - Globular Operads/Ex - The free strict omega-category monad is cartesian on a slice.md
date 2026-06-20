---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - The Free Strict ω-Category Monad"
  - "Def - Pullback and Pushout"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

The truncation of the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] $T$ to $1$-globular sets (directed graphs) is the **free-category monad** $fc$, sending a directed graph $G$ to the graph $fcG$ whose edges are the finite *paths* in $G$. Show that $fc$ is a **cartesian monad** by verifying:

(a) $fc$ preserves pullbacks of directed graphs;

(b) the unit $\eta : 1 \Rightarrow fc$ is a cartesian natural transformation;

(c) the multiplication $\mu : fc^2 \Rightarrow fc$ is a cartesian natural transformation.

Then explain in one sentence why the same argument, applied dimension by dimension, shows the full $T$ is cartesian.

**Recall:**

A directed graph $G$ has a set $G_0$ of vertices and a set $G_1$ of edges with source/target maps $G_1 \rightrightarrows G_0$; it is a $1$-globular set. The **free-category monad** $fc$ has $(fcG)_0 = G_0$ and $(fcG)_1 =$ the set of finite paths (including length-$0$ identity paths at each vertex). The unit $\eta_G : G \to fcG$ sends an edge to the length-$1$ path; the multiplication $\mu_G : fc^2 G \to fcG$ concatenates a path-of-paths into a single path.

A monad $(S, \eta, \mu)$ on a category $\mathcal{C}$ with [[Def - Pullback and Pushout|pullbacks]] is **cartesian** if $S$ preserves pullbacks and $\eta, \mu$ are **cartesian natural transformations** — meaning every naturality square
$$
\begin{array}{ccc}
SA & \xrightarrow{\,Sf\,} & SB\\
\downarrow & & \downarrow\\
\cdots & & \cdots
\end{array}
$$
is a [[Def - Pullback and Pushout|pullback]]. A square is a pullback when its top-left corner is, up to canonical iso, the set of compatible pairs from the other three corners.

---

# Convergent Strategy

**Problem class:** This is a *cartesianness* problem in the sense of the topic page's problem-solving strategy — the foundational kind, justifying that the operad framework applies. The route is always the same: reduce the abstract pullback-preservation and cartesian-naturality conditions to elementary statements about paths, then verify them combinatorially. The slice (here, the $1$-dimensional truncation) is chosen because it isolates the free-monoid combinatorics that drive the general case.

**Assumption pattern:** The key assumption is the *explicit path description* of $fc$: edges of $fcG$ are finite paths in $G$. This combinatorial handle is what makes the pullback conditions checkable — "a path in a pullback graph is a compatible pair of paths" is the whole content of (a), and it is recognizable the moment you write paths as sequences of edges. The free-monoid structure ("$fcG$'s edges are sequences of $G$'s edges over a vertex") is the signal that cartesianness will hold, because the free-monoid monad on sets is cartesian.

**Theorem routing:** No external theorem is needed; the route is "unwind the definitions of [[Def - Pullback and Pushout|pullback]] and of $fc$, then match". For (a), route through "a path in $G \times_H K$ is a pair of paths, one in $G$ and one in $K$, with matching image-path in $H$". For (b) and (c), route through "the naturality square is a pullback iff the corner set is exactly the compatible pairs", verified by the length/concatenation bookkeeping of paths.

**Key decision point:** The non-obvious choice is to verify cartesianness *at the level of individual paths* (a path in the pullback is a compatible pair of paths) rather than abstractly. The tempting alternative — invoking a general theorem that "polynomial monads are cartesian" — is correct but hides the mechanism; doing it by hand on paths is what reveals *why* it works (paths are free, so they pull back) and what makes the dimension-by-dimension generalization to $T$ transparent.

---

# Legal Operations Used

1. **Operation 2 from the topic page (use cartesianness to form fibres/substitution), here proving the prerequisite for it.** This exercise establishes the very cartesianness that operation 2 later takes for granted; it is the bottom of the stack.

2. **Operation 7 from the topic page (transport through truncation/embedding).** We work in the $1$-dimensional truncation, where $T$ becomes $fc$, precisely because the truncated case is manageable and the argument transports upward dimension by dimension.

---

# Hints

> [!note]- Hint 1
> Write everything in terms of paths. An edge of $fcG$ is a finite path $v_0 \to v_1 \to \cdots \to v_k$ in $G$. A pullback $G \times_H K$ has, as edges, pairs of edges $(e, e')$ with the same image in $H$. Combine these two descriptions.

> [!note]- Hint 2
> For (a): a path in $G \times_H K$ is a sequence of edge-pairs $(e_i, e'_i)$, each pair having matching image in $H$. Show this is the same data as a pair of paths — one in $G$, one in $K$ — that map to the *same* path in $H$. That equality of two descriptions *is* the pullback condition.

> [!note]- Hint 3
> For (b), the unit naturality square for $f : G \to G'$ has corners $G, G', fcG, fcG'$. A square is a pullback iff $G \cong G' \times_{fcG'} fcG$. Unwind: an element of the right side is a vertex/edge of $G'$ together with a *length-$1$* path of $fcG$ over it — show the length-$1$ constraint forces it to come from a single edge of $G$.

> [!note]- Hint 4
> For (c), the multiplication square's pullback condition says: a path-of-paths in $fc^2 G'$ together with a compatible single path in $fcG$ is the same as a path-of-paths in $fc^2 G$. The content is that concatenation $\mu$ does not lose information about *how* the path was subdivided once you also know the underlying graph map — which is exactly the freeness of paths.

---

# Solution

The proof verifies the three cartesian conditions by translating each into a statement about paths and checking the two sides describe the same data. Step 1 handles pullback preservation (a path in a pullback is a compatible pair of paths). Step 2 handles the unit (length-$1$ paths come from single edges). Step 3 handles the multiplication (subdivided paths are determined by their concatenation plus the graph structure). The unifying move is "paths are free sequences, and free sequences pull back".

**Step 1: $fc$ preserves pullbacks.**

> [!note]- Derivation
> Let $G \to H \leftarrow K$ be graph maps with pullback $G \times_H K$: its vertices are pairs $(v, w)$ of vertices with equal image in $H$, and its edges are pairs $(e, e')$ of edges with equal image in $H$ (and matching endpoints). Apply $fc$. An edge of $fc(G \times_H K)$ is a finite path in $G \times_H K$, i.e. a sequence
> $$
> \big((e_1, e'_1), (e_2, e'_2), \dots, (e_k, e'_k)\big), \qquad e_i \in G_1,\ e'_i \in K_1,\ \text{image}(e_i) = \text{image}(e'_i) \text{ in } H,
> $$
> with consecutive endpoints matching in both coordinates. This is exactly the data of a path $(e_1, \dots, e_k)$ in $G$ and a path $(e'_1, \dots, e'_k)$ in $K$ of the *same length* whose images in $H$ coincide path-by-path — that is, a pair of paths in $G$ and $K$ mapping to the same path in $H$. But that is precisely an edge of the pullback $fcG \times_{fcH} fcK$. Hence
> $$
> fc(G \times_H K) \cong fcG \times_{fcH} fcK,
> $$
> naturally, so $fc$ preserves pullbacks. (The length matching is automatic because two paths can only have equal image in $H$ if they have equal length.)

**Step 2: the unit $\eta$ is cartesian.**

> [!note]- Derivation
> Fix $f : G \to G'$. The unit naturality square is
> $$
> \begin{array}{ccc}
> G & \xrightarrow{\;f\;} & G'\\
> {\scriptstyle\eta_G}\big\downarrow & & \big\downarrow{\scriptstyle\eta_{G'}}\\
> fcG & \xrightarrow{\;fcf\;} & fcG'.
> \end{array}
> $$
> We must show $G \cong G' \times_{fcG'} fcG$. An element of the pullback is a cell $x'$ of $G'$ together with a path $p$ of $fcG$ such that $\eta_{G'}(x') = (fcf)(p)$, i.e. the length-$1$ path on $x'$ equals the image path $f \circ p$. Since $\eta_{G'}(x')$ has length $1$, the path $f \circ p$ has length $1$, forcing $p$ itself to have length $1$ (a graph map preserves path length), say $p = \eta_G(x)$ for a unique cell $x$ of $G$; and then $f(x) = x'$. So the pullback consists of cells $x$ of $G$ (with $x'= f(x)$ determined), i.e. it is $G$. Hence the square is a pullback and $\eta$ is cartesian.

**Step 3: the multiplication $\mu$ is cartesian.**

> [!note]- Derivation
> Fix $f : G \to G'$. The multiplication square is
> $$
> \begin{array}{ccc}
> fc^2 G & \xrightarrow{\;fc^2 f\;} & fc^2 G'\\
> {\scriptstyle\mu_G}\big\downarrow & & \big\downarrow{\scriptstyle\mu_{G'}}\\
> fcG & \xrightarrow{\;fcf\;} & fcG'.
> \end{array}
> $$
> We show $fc^2 G \cong fcG \times_{fcG'} fc^2 G'$. An edge of $fc^2 G$ is a *path of paths* in $G$: a sequence $(p_1, \dots, p_r)$ of paths $p_j$ in $G$ with matching endpoints. An element of the pullback is a single path $q$ in $fcG$ (that is, a path in $G$) together with a path-of-paths $P' = (p'_1, \dots, p'_r)$ in $G'$ such that $\mu_{G'}(P') = (fcf)(q)$ — i.e. the concatenation $p'_1 \cdots p'_r$ equals the image path $f \circ q$. Now $f \circ q$ is a single path in $G'$ of definite length, and $P'$ specifies a *subdivision* of it into $r$ pieces of lengths $\ell_1, \dots, \ell_r$. Given $q$ (a path in $G$) and this subdivision pattern $(\ell_1, \dots, \ell_r)$ — which is exactly the extra data $P'$ carries beyond its concatenation — we recover a unique path-of-paths in $G$: cut $q$ into consecutive pieces of lengths $\ell_1, \dots, \ell_r$. Conversely a path-of-paths in $G$ determines its concatenation $q = \mu_G(\cdot)$ and (by applying $f$) the subdivided image $P'$. These assignments are mutually inverse, so $fc^2 G \cong fcG \times_{fcG'} fc^2 G'$ and $\mu$ is cartesian. The key point is freeness: a path remembers nothing but its sequence of edges, so a concatenation plus a length-pattern reconstructs the subdivision uniquely.

> [!note]- Complete formal solution
> Use the path description of $fc$ throughout.
>
> *(a) Pullback preservation.* For $G \to H \leftarrow K$, an edge of $fc(G\times_H K)$ is a sequence of edge-pairs $((e_i, e'_i))_{i\le k}$ with $\mathrm{im}(e_i)=\mathrm{im}(e'_i)$ in $H$ and matching endpoints; this is a pair of equal-length paths in $G$ and $K$ with equal image-path in $H$, i.e. an edge of $fcG\times_{fcH} fcK$. So $fc(G\times_H K)\cong fcG\times_{fcH} fcK$ naturally, and $fc$ preserves pullbacks.
>
> *(b) Unit cartesian.* For $f:G\to G'$, an element of $G'\times_{fcG'} fcG$ is $(x', p)$ with $\eta_{G'}(x') = (fcf)(p)$; the left side has length $1$, forcing $p$ to have length $1$, say $p=\eta_G(x)$ with $f(x)=x'$. So the pullback is $G$, and $\eta$ is cartesian.
>
> *(c) Multiplication cartesian.* For $f:G\to G'$, an element of $fcG\times_{fcG'} fc^2 G'$ is $(q, P')$ with $\mu_{G'}(P') = (fcf)(q)$; $P'$ subdivides the image path $f\circ q$ into pieces of lengths $\ell_1,\dots,\ell_r$, and cutting $q$ into consecutive pieces of those lengths gives a unique path-of-paths in $G$, inverse to $(\mu_G, fc^2 f)$. So $fc^2 G\cong fcG\times_{fcG'} fc^2 G'$ and $\mu$ is cartesian.
>
> Hence $fc$ is a cartesian monad.
>
> *Generalization to $T$.* The full free-strict-$\omega$-category monad is built by the recursion $\mathrm{pd}(m+1)=\mathrm{pd}(m)^\ast$, i.e. by applying the free-monoid (path/list) construction in each dimension; since each free-monoid layer is cartesian by exactly the path arguments above and pullbacks are computed dimension-wise in globular sets, $T$ is cartesian. $\blacksquare$

---

# Key Takeaways

**Cartesianness of a free-algebra monad is "freeness made into a pullback".** The deepest lesson here is *why* $fc$ (and hence $T$) is cartesian: a free path remembers nothing but its sequence of edges, so it can be reconstructed from partial data by pulling back — a path in a pullback graph is exactly a compatible pair of paths, a length-$1$ path comes from a single edge, a concatenation plus a subdivision pattern recovers the path-of-paths. Each cartesian condition is one face of "the data is free, hence determined by its pieces". This is the trigger for recognizing cartesianness in the wild: whenever a monad's free algebras are built from *ordered, non-collapsing* data (lists, paths, trees, pasting diagrams), expect cartesianness; whenever they involve *forgetting order or duplicating* (multisets, symmetric powers), expect failure. The free-commutative-monoid monad fails cartesianness for exactly the opposite reason — forgetting order destroys the reconstruction a pullback needs.

**Verify abstract conditions on the smallest faithful slice.** Rather than attack the cartesianness of the full $\omega$-dimensional $T$, this exercise drops to the $1$-dimensional truncation $fc$, where the combinatorics are visible (paths) and the pullback conditions become elementary. The general result then follows because $T$ is assembled out of free-monoid layers and pullbacks are computed dimension-wise. This "prove it on the truncation, then lift dimension by dimension" pattern is the standard route through the technical results of the chapter (it is also how Leinster's Appendix F proceeds), and the transferable diagnostic is: when a higher-categorical claim about all dimensions looks intractable, find the lowest dimension where the phenomenon already appears and settle it there first.

**Cartesianness is the license, not a luxury.** It is easy to treat "the monad is cartesian" as a technical footnote, but this exercise shows it is the single hypothesis on which the entire globular-operad edifice rests: without it, the substitution product on collections is not associative, fibres $P(\pi)$ are not well-defined, and "globular operad" cannot be stated (see the topic page's first illegal-but-tempting operation). Having proved it here for the simplest case, you have earned the right to invoke "since $T$ is cartesian" freely in every later construction — exactly as the topic page's legal operation 2 does. The companion exercise [[Ex - The substitution product and why cartesianness is needed]] shows the converse failure, exhibiting where the substitution product breaks without cartesianness.
