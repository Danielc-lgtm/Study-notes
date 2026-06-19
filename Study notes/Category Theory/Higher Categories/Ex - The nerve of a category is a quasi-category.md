---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Kan Complex and the Nerve"
  - "Def - Quasi-Category"
  - "Def - Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Prove that for any [[Def - Category|category]] $\mathcal{C}$, the [[Def - Kan Complex and the Nerve|nerve]] $N(\mathcal{C})$ is a [[Def - Quasi-Category|quasi-category]]: every inner horn $\Lambda^n_i\to N(\mathcal{C})$ (with $0<i<n$) has a filler. Show moreover that the filler is **unique**, so $N(\mathcal{C})$ is the special case of a quasi-category in which composition is single-valued. Treat the base case $n=2$ (composition) explicitly and indicate the inductive step for $n\ge 3$ (associativity and higher coherence).

**Recall:**

The [[Def - Kan Complex and the Nerve|nerve]] has $N(\mathcal{C})_n = \mathrm{Fun}([n],\mathcal{C})$, the strings $A_0\xrightarrow{f_1}\cdots\xrightarrow{f_n}A_n$ of $n$ composable arrows; the face map $d_i$ composes the $i$th and $(i{+}1)$st arrows (for $0<i<n$) or drops an end arrow, and degeneracies insert identities. A [[Def - Quasi-Category|quasi-category]] is a [[Def - Simplicial Set|simplicial set]] in which every *inner* horn $\Lambda^n_i$ ($0<i<n$) has a filler. The inner horn $\Lambda^n_i$ contains all faces of $\Delta^n$ except the $i$th.

---

# Convergent Strategy

**Problem class:** This is a "verify horn-filling" problem, the central "fill" target of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is to interpret an inner horn as partial data (a string with one composite missing) and show the missing data is uniquely determined by composition in $\mathcal{C}$.

**Assumption pattern:** The recognisable feature is that simplices of $N(\mathcal{C})$ are *strings of composable arrows* — a fully combinatorial description. An inner horn $\Lambda^n_i\to N(\mathcal{C})$ supplies all the edges of such a string except those crossing vertex $i$, and composition in $\mathcal{C}$ fills the gap.

**Theorem routing:** The route is the [[Def - Kan Complex and the Nerve|nerve]] description plus the [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterisation]] (which this exercise re-proves in the forward direction): unique inner fillers correspond to single-valued composition.

**Key decision point:** The non-obvious choice is identifying *exactly what data an inner horn omits and what forces the filler*. For $\Lambda^2_1$ the omitted face is the long edge, forced by composing the two given edges. For $\Lambda^n_i$ with $n\ge 3$, the omitted face is an $(n-1)$-simplex, and one must check the *remaining* faces already pin down the whole string, so the filler is both existent and unique. Mishandling which face is missing is the usual error.

---

# Legal Operations Used

1. **Operation 2 (compute simplices via the universal property).** Simplices of $N(\mathcal{C})$ are functors $[n]\to\mathcal{C}$, i.e. composable strings.

2. **Operation 3 (translate horn-filling into composites).** An inner horn is a string missing the data across vertex $i$; the filler is the composite supplied by $\mathcal{C}$.

3. **Operation 4 (apply the nerve characterisation).** Unique fillers ⟺ the simplicial set is a nerve; here we establish the existence-and-uniqueness directly.

---

# Hints

> [!note]- Hint 1
> An inner horn $\Lambda^n_i\to N(\mathcal{C})$ assigns a compatible family of simplices to all faces of $\Delta^n$ except the $i$th. For $n=2$, $i=1$, this is just two composable arrows $f:A_0\to A_1$, $g:A_1\to A_2$. What is the filler?

> [!note]- Hint 2
> For $n=2$: the missing face is the long edge $A_0\to A_2$. The unique $2$-simplex with edges $f,g$ is the string $(f,g)$ whose $d_1$ is $g\circ f$. So existence = "$g\circ f$ exists", uniqueness = "the composite is single-valued".

> [!note]- Hint 3
> For $n\ge 3$: an inner horn gives all but one $(n-1)$-face of a string of $n$ composable arrows. The remaining faces already specify *all the individual arrows* $f_1,\dots,f_n$ (the edges along the spine), and a string is determined by its arrows. So the filler — the full string — exists and is unique; the missing face is then forced by composition/associativity.

---

# Solution

The plan: Step 1 sets up an inner horn as partial string data. Step 2 fills $\Lambda^2_1$ explicitly (composition) and shows uniqueness. Step 3 handles $n\ge 3$ by observing the spine of arrows is determined, forcing the unique filler (associativity at $n=3$). Step 4 concludes $N(\mathcal{C})$ is a quasi-category with unique inner fillers.

**Step 1: An inner horn is partial string data.** A map $\Lambda^n_i\to N(\mathcal{C})$ is a compatible assignment of composable-string data to every face of $\Delta^n$ except the $i$th.

> [!note]- Derivation
> By [[Def - Kan Complex and the Nerve|definition]], an $m$-simplex of $N(\mathcal{C})$ is a functor $[m]\to\mathcal{C}$, i.e. a string of $m$ composable arrows; a map $\Lambda^n_i\to N(\mathcal{C})$ is a family of such, one per face $d^j$ ($j\ne i$), agreeing on overlaps. The faces $d^j$ for $j\ne i$ together contain every *edge* (1-face) of $\Delta^n$ — in particular all $n$ "spine" edges $A_0\to A_1\to\dots\to A_n$ — because an edge is omitted from $\Lambda^n_i$ only if both its endpoints are the single omitted vertex, which cannot happen. So the horn already specifies all the individual arrows $f_1,\dots,f_n$ of the string.

**Step 2: Fill $\Lambda^2_1$ (composition), uniquely.** For $n=2$, $i=1$, the horn is a composable pair $f:A_0\to A_1$, $g:A_1\to A_2$; the unique filler is the $2$-simplex $(f,g)$ with long edge $g\circ f$.

> [!note]- Derivation
> $\Lambda^2_1$ consists of the two edges $d^2 = f$ ($A_0\to A_1$) and $d^0 = g$ ($A_1\to A_2$), omitting the long edge $d^1$ ($A_0\to A_2$). A $2$-simplex of $N(\mathcal{C})$ is a functor $[2]\to\mathcal{C}$, i.e. a string $A_0\xrightarrow{f}A_1\xrightarrow{g}A_2$ — *determined by its two spine edges $f,g$*. There is exactly one such string extending the horn, namely $(f,g)$ itself, and its omitted face $d^1$ is the composite $g\circ f$ (the value of the functor on the arrow $0\to 2$). Existence: $g\circ f$ exists because $\mathcal{C}$ is a category. Uniqueness: the string $(f,g)$ is the only functor $[2]\to\mathcal{C}$ with these spine edges. So $\Lambda^2_1$ has a unique filler, and the filler *is* composition.

**Step 3: Fill $\Lambda^n_i$ for $n\ge 3$, uniquely.** The horn determines all spine arrows $f_1,\dots,f_n$; the unique functor $[n]\to\mathcal{C}$ with those arrows is the filler, and the omitted face is forced (associativity at $n=3$).

> [!note]- Derivation
> By Step 1 the inner horn $\Lambda^n_i$ specifies all spine edges $f_1,\dots,f_n$. A functor $[n]\to\mathcal{C}$ is *uniquely determined* by these $n$ composable arrows — its value on any arrow $a\to b$ in $[n]$ is the composite $f_b\circ\dots\circ f_{a+1}$, which is well-defined and unique because composition in $\mathcal{C}$ is associative. So there is exactly one $n$-simplex of $N(\mathcal{C})$ with the given spine, and it agrees with the horn on every face $d^j$, $j\ne i$ (those faces are sub-strings, determined by sub-collections of the $f_k$). Hence the filler exists and is unique; the omitted face $d^i$ is the sub-string obtained by composing $f_i$ and $f_{i+1}$, automatically consistent by associativity. (At $n=3$ this consistency is exactly the associativity $(h\circ g)\circ f = h\circ(g\circ f)$.)

**Step 4: Conclusion.** Every inner horn of $N(\mathcal{C})$ has a unique filler, so $N(\mathcal{C})$ is a [[Def - Quasi-Category|quasi-category]] — the case where composition is single-valued.

> [!note]- Derivation
> Steps 2–3 show that for every $n\ge 2$ and $0<i<n$, the inner horn $\Lambda^n_i\to N(\mathcal{C})$ has exactly one filler. In particular fillers *exist*, which is the [[Def - Quasi-Category|quasi-category]] axiom, so $N(\mathcal{C})$ is a quasi-category. The extra fact that the filler is *unique* places $N(\mathcal{C})$ in the special class characterised in [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|the nerve theorem]]: the quasi-categories with unique inner fillers are precisely the nerves of ordinary categories, where composition is honestly single-valued rather than defined up to homotopy.

> [!note]- Complete formal solution
> Let $\mathcal{C}$ be a category. A map $\Lambda^n_i\to N(\mathcal{C})$ ($0<i<n$) specifies a compatible family of composable strings on all faces but the $i$th; since every spine edge of $\Delta^n$ lies in some included face, the horn determines all arrows $f_1,\dots,f_n$ of a string $A_0\xrightarrow{f_1}\cdots\xrightarrow{f_n}A_n$ (Step 1). A functor $[n]\to\mathcal{C}$ is uniquely determined by its spine $(f_1,\dots,f_n)$, its value on $a\to b$ being $f_b\circ\dots\circ f_{a+1}$ (associative, hence well-defined). This functor is the unique $n$-simplex extending the horn; for $n=2$ it realises the composite $g\circ f$ (Step 2), for $n\ge 3$ it is forced by associativity (Step 3). Hence every inner horn has a unique filler, so $N(\mathcal{C})$ is a [[Def - Quasi-Category|quasi-category]] with single-valued composition. $\quad\blacksquare$

---

# Key Takeaways

**Inner-horn filling in a nerve *is* composition, and its uniqueness *is* single-valuedness — this is the concrete content of the chapter's central theorem.** The base case $\Lambda^2_1$ makes it vivid: the two edges of the horn are composable arrows, and the unique filler's long edge is their composite. There is no choice because $\mathcal{C}$ has exactly one composite of two arrows. Carrying this picture forward, "a quasi-category is a category where the filler need not be unique" becomes "composition need not be single-valued", which is the whole conceptual move of §H.4. The trigger to internalise: when you see an inner horn in a nerve, read it as "compose these arrows", and the uniqueness as "there is one answer".

**A functor out of $[n]$ is determined by its spine, which is why nerve horn-filling is purely about composition and associativity.** The key structural fact is that a string of $n$ composable arrows is determined by the $n$ individual arrows, with all longer composites forced by associativity. An inner horn always retains the full spine, so the filler is determined; existence is composition (dimension $2$), and consistency of the omitted face is associativity (dimension $3$) and its higher analogues. The reusable diagnostic: to fill a horn in a nerve, locate the spine, check it is fully specified, and read off the unique extending functor — the omitted face is then automatic.

**Outer horns are deliberately *not* required, and this is exactly what keeps $\infty$-categories from collapsing to groupoids.** This proof fills only inner horns; the outer horns $\Lambda^n_0,\Lambda^n_n$ generally do *not* fill in $N(\mathcal{C})$ (filling them would invert arrows, as in [[Def - Kan Complex and the Nerve]]). This is the right behaviour: a general category has non-invertible morphisms, and demanding outer fillers would force them invertible, turning $N(\mathcal{C})$ into a Kan complex / $\infty$-groupoid. The lesson, central to the whole chapter: the inner/outer distinction is the $\infty$-category / $\infty$-groupoid distinction, and proving "nerve = quasi-category" must, and does, use only the inner horns.
