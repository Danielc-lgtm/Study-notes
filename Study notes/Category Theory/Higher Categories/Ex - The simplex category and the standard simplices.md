---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Simplicial Set"
  - "Def - The Yoneda Embedding"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Work out the combinatorics of the [[Def - Simplicial Set|simplex category]] $\Delta$ and the standard simplices.

1. Verify two of the **cosimplicial identities** relating the cofaces $d^i$ and codegeneracies $s^i$: namely $d^j d^i = d^i d^{j-1}$ for $i < j$, and $s^j d^i = d^i s^{j-1}$ for $i < j$.
2. Using the [[Def - The Yoneda Embedding|Yoneda lemma]], describe the $k$-simplices of the standard $n$-simplex $\Delta^n = \Delta(-,[n])$ explicitly, and count $\Delta^2_0, \Delta^2_1, \Delta^2_2$ (the vertices, edges, and triangles of the standard $2$-simplex, degenerate ones included).
3. Describe the inner horn $\Lambda^2_1\subseteq\Delta^2$ explicitly: which simplices does it contain, and which are missing?

**Recall:**

The [[Def - Simplicial Set|simplex category]] $\Delta$ has objects $[n]=\{0<1<\dots<n\}$ and order-preserving maps. The coface $d^i:[n-1]\to[n]$ is the injection missing $i$; the codegeneracy $s^i:[n+1]\to[n]$ is the surjection hitting $i$ twice. The standard $n$-simplex is the representable [[Def - Presheaf|presheaf]] $\Delta^n=\Delta(-,[n])$, so $\Delta^n_k=\Delta([k],[n])$; by the [[Def - The Yoneda Embedding|Yoneda lemma]], $\mathbf{sSet}(\Delta^n,X)\cong X_n$. The horn $\Lambda^n_i$ is the union of all faces except the $i$th.

---

# Convergent Strategy

**Problem class:** This is a "compute the simplices via the universal property" drill, the second source pattern of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is to *never enumerate by hand* but to read simplices off the representable description $\Delta^n_k=\Delta([k],[n])$, and to verify the cosimplicial identities by tracking where each integer goes.

**Assumption pattern:** The recognisable feature is that $\Delta^n$ is *representable*; by Yoneda its $k$-simplices are exactly the order-preserving maps $[k]\to[n]$. So counting simplices becomes counting monotone maps between finite ordinals — a pure combinatorics problem with a closed-form answer.

**Theorem routing:** The route for part 2 is the [[Def - The Yoneda Embedding|Yoneda lemma]] (a $k$-simplex of $\Delta^n$ is a map $\Delta^k\to\Delta^n$ is an element of $\Delta^n_k=\Delta([k],[n])$). For part 1 the route is direct computation: evaluate both sides of each identity on an arbitrary $j\in[\,\cdot\,]$.

**Key decision point:** The non-obvious choice in part 1 is to verify the identities *as functions*, by evaluating on a general element and splitting into cases by where the element sits relative to the indices $i,j$. The temptation is to argue abstractly; the reliable method is to push a single integer through both composites and watch the index bookkeeping.

---

# Legal Operations Used

1. **Operation 2 (compute the simplices of a simplicial set via its universal property).** We read $\Delta^n_k=\Delta([k],[n])$ off representability and count monotone maps.

---

# Hints

> [!note]- Hint 1
> A monotone map $[k]\to[n]$ is determined by a weakly increasing sequence $0\le a_0\le a_1\le\dots\le a_k\le n$. How many such sequences are there? (Stars and bars: choosing $k+1$ values from $n+1$ with repetition.)

> [!note]- Hint 2
> For the cosimplicial identity $d^j d^i = d^i d^{j-1}$ ($i<j$): both sides are injections $[n-2]\to[n]$ missing two values. Compute which two values each side misses — they should be the same set $\{i,j\}$.

> [!note]- Hint 3
> $\Delta^2_0=\Delta([0],[2])$ counts vertices; $\Delta^2_1=\Delta([1],[2])$ counts edges (including degenerate constant ones); $\Delta^2_2=\Delta([2],[2])$ counts triangles. Use the stars-and-bars count $\binom{n+k+1}{k+1}$ with $n=2$.

---

# Solution

The plan: Step 1 verifies the two cosimplicial identities by evaluating on a general integer. Step 2 reads off $\Delta^n_k$ via Yoneda and counts the low-dimensional simplices of $\Delta^2$. Step 3 describes the inner horn $\Lambda^2_1$.

**Step 1: Two cosimplicial identities.** For $i<j$: $d^j d^i = d^i d^{j-1}$ (both miss exactly $\{i,j\}$), and $s^j d^i = d^i s^{j-1}$.

> [!note]- Derivation
> *Identity $d^j d^i = d^i d^{j-1}$ ($i<j$), both maps $[n-2]\to[n]$.* Recall $d^i$ is "skip $i$": $d^i(\ell)=\ell$ if $\ell<i$, $\ell+1$ if $\ell\ge i$. The composite $d^j d^i$ first skips $i$ (in $[n-1]$) then skips $j$ (in $[n]$). The composite $d^i d^{j-1}$ first skips $j-1$ then skips $i$. Both are injections $[n-2]\hookrightarrow[n]$, and an injection of ordinals is determined by its image, equivalently by the two values it omits. The left side omits $i$ and $j$ (skipping $i$ first, then $j$, where because $i<j$ the second skip lands at the original $j$). The right side omits $i$ and $j$ likewise. Same omitted set $\{i,j\}$, so the maps are equal.
>
> *Identity $s^j d^i = d^i s^{j-1}$ ($i<j$), both maps $[n]\to[n-1]$.* Recall $s^j$ is "repeat $j$": $s^j(\ell)=\ell$ if $\ell\le j$, $\ell-1$ if $\ell>j$. Evaluate on $\ell\in[n]$. Since $i<j$, the coface $d^i$ (skip $i$) and the codegeneracy $s^j$ (merge at $j$) act on disjoint indices, so they commute up to the index shift recorded by $j-1$ versus $j$: a case check on $\ell<i$, $\ell=i,\dots$, $\ell$ large confirms $s^j(d^i(\ell)) = d^i(s^{j-1}(\ell))$ in every case. (The shift from $j$ to $j-1$ on the right compensates for the insertion done by $d^i$ on the left.)

**Step 2: Simplices of $\Delta^n$ via Yoneda; counts for $\Delta^2$.** By Yoneda, $\Delta^n_k=\Delta([k],[n])$ = monotone maps $[k]\to[n]$ = weakly increasing sequences $0\le a_0\le\dots\le a_k\le n$, counted by $\binom{n+k+1}{k+1}$. For $n=2$: $\Delta^2_0=3$, $\Delta^2_1=6$, $\Delta^2_2=10$.

> [!note]- Derivation
> A $k$-simplex of $\Delta^n$ is, by [[Def - The Yoneda Embedding|Yoneda]], an element of $\Delta^n_k = \Delta([k],[n])$: an order-preserving map $[k]\to[n]$, equivalently a weakly increasing tuple $(a_0\le\dots\le a_k)$ with $a_\ell\in\{0,\dots,n\}$. The number of such tuples is the number of multisets of size $k+1$ from $n+1$ symbols, $\binom{(n+1)+(k+1)-1}{k+1}=\binom{n+k+1}{k+1}$.
> - $\Delta^2_0=\Delta([0],[2])$: maps $[0]\to[2]$, i.e. choices of one vertex — $\binom{3}{1}=3$ (the three vertices $0,1,2$).
> - $\Delta^2_1=\Delta([1],[2])$: pairs $a_0\le a_1$ in $\{0,1,2\}$ — $\binom{4}{2}=6$. These are the three non-degenerate edges $01,02,12$ together with three degenerate edges $00,11,22$ (the constant maps).
> - $\Delta^2_2=\Delta([2],[2])$: triples $a_0\le a_1\le a_2$ — $\binom{5}{3}=10$. The unique *non-degenerate* one is the identity $012$ (the solid triangle); the other nine are degenerate.

**Step 3: The inner horn $\Lambda^2_1$.** $\Lambda^2_1\subseteq\Delta^2$ is the union of the faces $d^0$ and $d^2$ (omitting the $1$st face), i.e. the two edges $0\to 1$ and $1\to 2$; it is missing the long edge $0\to 2$ (the $1$st face $d^1$) and the solid triangle $012$.

> [!note]- Derivation
> By definition $\Lambda^2_1$ is the union of all faces of $\Delta^2$ except the $i=1$ face. The faces of $\Delta^2$ are the three edges: $d^0$ omits vertex $0$, giving the edge $12$; $d^1$ omits vertex $1$, giving the long edge $02$; $d^2$ omits vertex $2$, giving the edge $01$. The inner horn $\Lambda^2_1$ keeps $d^0$ ($12$) and $d^2$ ($01$) and discards $d^1$ ($02$). So $\Lambda^2_1$ is exactly the two edges $0\to 1\to 2$ glued at vertex $1$ — a "composable pair of arrows" — missing the long edge $02$ and the filling triangle. This is why a filler of $\Lambda^2_1$ is a *composite* of the two edges.

> [!note]- Complete formal solution
> *Cosimplicial identities.* For $i<j$, $d^j d^i$ and $d^i d^{j-1}$ are injections $[n-2]\to[n]$ both omitting exactly $\{i,j\}$, hence equal; $s^j d^i$ and $d^i s^{j-1}$ agree on every $\ell\in[n]$ by a case check, the $j\!-\!1$ shift compensating the $d^i$ insertion.
>
> *Standard simplices.* By [[Def - The Yoneda Embedding|Yoneda]], $\Delta^n_k=\Delta([k],[n])=\{$monotone $[k]\to[n]\}$, counted by $\binom{n+k+1}{k+1}$. For $n=2$: $|\Delta^2_0|=3$, $|\Delta^2_1|=6$ (three non-degenerate edges, three degenerate), $|\Delta^2_2|=10$ (one non-degenerate triangle $012$).
>
> *Inner horn.* $\Lambda^2_1$ = edges $01$ and $12$ (faces $d^2,d^0$), missing the long edge $02$ (face $d^1$) and the triangle: a composable pair awaiting a composite. $\quad\blacksquare$

---

# Key Takeaways

**Never enumerate simplices by hand — read them off the representable description.** The whole convenience of $\Delta^n=\Delta(-,[n])$ is that, by [[Def - The Yoneda Embedding|Yoneda]], its $k$-simplices are *defined* to be the monotone maps $[k]\to[n]$. Counting simplices, identifying degeneracies, and describing faces all reduce to combinatorics of order-preserving maps between ordinals. This is the reusable move whenever a simplicial set is given by a universal property (representable, nerve, singular complex): the simplices come for free from the defining mapping property, and trying to build them by gluing is both slower and error-prone.

**Degenerate simplices outnumber non-degenerate ones, and keeping track of which is which is essential.** Of the six $1$-simplices of $\Delta^2$, only three are non-degenerate edges; of the ten $2$-simplices, only one is the non-degenerate triangle. The degenerate simplices (constant maps, repeated vertices) are the images of degeneracy maps and are exactly the bookkeeping that distinguishes simplicial sets from semi-simplicial sets. When describing or drawing a simplicial set, specify its *non-degenerate* simplices; the rest are forced. This distinction becomes load-bearing in geometric realisation, where each non-degenerate $n$-simplex contributes one $n$-cell and degenerate simplices contribute nothing new.

**The inner horn $\Lambda^2_1$ is literally "two composable arrows", and this picture is the seed of the whole $\infty$-category story.** Working out that $\Lambda^2_1$ consists of the edges $01$ and $12$ glued at $1$, missing the long edge $02$, makes concrete the central translation of the chapter: a map $\Lambda^2_1\to X$ is a composable pair, and a [[Def - Quasi-Category|filler]] is a composite. Carrying this geometric picture — horn = partial diagram awaiting completion, filler = the completion — into the higher dimensions is exactly how composition, associativity, and their coherences get encoded. The trigger to remember: whenever "inner horn" appears, picture the missing-long-edge triangle and read "a composite is being requested".
