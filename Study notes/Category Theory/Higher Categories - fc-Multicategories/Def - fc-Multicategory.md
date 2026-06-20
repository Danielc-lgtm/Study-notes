---
type: definition
subject: higher-categories
prereqs:
  - "Def - Category"
  - "Def - 2-Category and Bicategory"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $\mathcal{C}$ denotes an **fc-multicategory**. Its data live in four layers, and we fix notation for each. **Objects** are written $A, B, C, \dots$ and are drawn as dots. A **vertical $1$-cell** is written $f : A \to A'$ with a downward arrow; vertical $1$-cells compose strictly and associatively, exactly like morphisms in a [[Def - Category|category]]. A **horizontal $1$-cell** is written $m : A \nrightarrow B$ (a "slashed" arrow, or just a labelled arrow drawn horizontally); horizontal $1$-cells do **not** come with a composition law of their own. A **$2$-cell** is the genuinely new piece: it has a *string* of horizontal $1$-cells along its top edge and a *single* horizontal $1$-cell along its bottom edge, with vertical $1$-cells closing up the two sides. We draw a typical $2$-cell as

$$
\begin{array}{ccccccc}
A_0 & \xrightarrow{m_1} & A_1 & \xrightarrow{m_2} & \cdots & \xrightarrow{m_n} & A_n \\
f \downarrow & & & \Downarrow\,\theta & & & \downarrow g \\
B_0 & & & \xrightarrow{\;\;\;p\;\;\;} & & & B_n
\end{array}
$$

so $\theta$ has domain the string $(m_1, m_2, \dots, m_n)$ of $n$ horizontal $1$-cells (with $A_0 \xrightarrow{m_1} A_1 \xrightarrow{m_2} \cdots \xrightarrow{m_n} A_n$), codomain the single horizontal $1$-cell $p : B_0 \nrightarrow B_n$, left boundary the vertical $1$-cell $f : A_0 \to B_0$ and right boundary $g : A_n \to B_n$. We allow $n = 0$: then the domain string is empty and lives at a single object $A_0 = A_n$, and the $2$-cell looks like a "unit" or "nullary" cell. The full symbol registry is on the parent page [[Higher Categories — fc-Multicategories and Weak Double Categories]]. The free-category monad on directed graphs, which generates this structure, is written $\mathrm{fc}$; the seed for "fc" is "**f**ree **c**ategory".

---

# Axiom Motivation

The structures of higher category theory keep running into the same friction: composition wants to be *partial* and *strung-out*, but the frameworks we have force it to be *total* and *binary*. A [[Def - Monoidal Category|monoidal category]] gives a single binary tensor $\otimes$ and asks for associativity coherence. A [[Def - 2-Category and Bicategory|bicategory]] gives a composition of $1$-cells that is associative only up to coherent isomorphism. A double category gives two directions of composition that must interchange. Each of these is a *fully composable* world: any two composable arrows have a composite, and the labour is in the coherence data that make the composites associate. The fc-multicategory is the structure you reach when you decide to stop forcing composites to exist and instead *record* what a composite would be — a $2$-cell whose top is the string you wanted to compose and whose bottom is the answer.

Here is the design problem stated plainly. We want a single framework that simultaneously contains bicategories, monoidal categories, double categories, and ordinary [[Def - Multicategory|multicategories]] as special cases, with no coherence axioms beyond the bare minimum. The unifying observation, due to Leinster, is that all of these are *generalised multicategories* — a [[Def - Generalized Multicategory|multicategory relative to a monad]] $T$ — and the right monad here is the **free-category monad** $\mathrm{fc}$ on the category of directed graphs. A directed graph is a set of vertices and a set of edges with source and target maps; the free category on it has the same vertices and has *paths* (strings of composable edges) as morphisms. So a $T$-multicategory for $T = \mathrm{fc}$ has, as its "multimaps", operations whose input is a *path* of horizontal $1$-cells and whose output is a single one. That is exactly the $2$-cell drawn above. The four-layer structure is not invented; it is *forced* by the shape of $\mathrm{fc}$.

Why allow a *string* on top rather than a single horizontal $1$-cell? Because that is the whole point: the string is the thing you have not yet composed. If you demanded that every $2$-cell have a single horizontal $1$-cell on top, you would be back to a double category, where horizontal composition is a given operation. By allowing strings of any length $n$, including $n = 0$, the framework lets *horizontal composites be data carried by $2$-cells*. A composite of $m_1, \dots, m_n$ is then a chosen $2$-cell from the string to some single $p$ with universal properties — and whether such composites exist, and how coherently, is precisely what distinguishes a plain fc-multicategory from a [[Def - Weak Double Category|weak double category]] (where they always exist) from a bicategory (where additionally the vertical structure is trivial).

What breaks if we drop the composition axiom for $2$-cells? Everything: without a way to substitute a $2$-cell into one slot of another, the four layers are just disconnected data and no "category-like" reasoning is possible. The composition law is multicategory-style substitution. Given a $2$-cell $\theta$ with top string $(m_1, \dots, m_n)$ and bottom $p$, and for each $i$ a $2$-cell $\theta_i$ with top a string $S_i$ and bottom $m_i$, we may substitute the $\theta_i$ into $\theta$ to get a $2$-cell with top the concatenated string $S_1 \cdots S_n$ and bottom $p$. This is the free-category monad's multiplication $\mu : \mathrm{fc}\,\mathrm{fc} \Rightarrow \mathrm{fc}$ at work: a path of paths flattens to a single path. If you instead tried to compose $2$-cells the way you compose $2$-cells in a bicategory — only along matching single boundaries — you could never glue a *string* into a *slot*, and the multicategorical flavour would be lost.

What breaks if we drop the identity axioms? The identity $2$-cells are what make the four layers cohere into a single organism. For each horizontal $1$-cell $m : A \nrightarrow B$ there is an identity $2$-cell $1_m$ with top the length-one string $(m)$, bottom $m$, and identity vertical boundaries; it is a two-sided unit for substitution. For each object $A$ there is — in the fully-fledged versions — a unit horizontal $1$-cell and a unit $2$-cell. Dropping these is like dropping identities from a category: composition loses its anchor, and the "do nothing" operation, which every well-posed substitution calculus needs, disappears. A reader who has internalised that "a monad has a unit because composition needs an identity, and a multiplication because composition needs to be associative" can invent the fc-multicategory axioms by transcribing those two demands into the four-layer, string-input setting.

---

# The Definition

An **fc-multicategory** $\mathcal{C}$ consists of the following data.

1. A class of **objects** $A, B, C, \dots$.

2. For each ordered pair of objects $(A, A')$, a class of **vertical $1$-cells** $f : A \to A'$, together with a strictly associative and unital composition making the objects and vertical $1$-cells into an ordinary [[Def - Category|category]] $\mathcal{C}_v$ (the *vertical category*). The identity vertical $1$-cell of $A$ is $1_A$.

3. For each ordered pair of objects $(A, B)$, a class of **horizontal $1$-cells** $m : A \nrightarrow B$. There is **no** composition imposed on horizontal $1$-cells; $A$ is the *source* and $B$ the *target* of $m$.

4. For each $n \geq 0$, each string of horizontal $1$-cells
$$A_0 \xrightarrow{m_1} A_1 \xrightarrow{m_2} \cdots \xrightarrow{m_n} A_n,$$
each horizontal $1$-cell $p : B_0 \nrightarrow B_n$, and each pair of vertical $1$-cells $f : A_0 \to B_0$, $g : A_n \to B_n$, a class of **$2$-cells**
$$\theta : (m_1, \dots, m_n) \Longrightarrow p$$
with left boundary $f$ and right boundary $g$, written with the square diagram of the Notation section.

5. A **composition** (substitution) of $2$-cells: given a $2$-cell
$$\theta : (m_1, \dots, m_n) \Rightarrow p \quad\text{with boundaries } f, g,$$
and, for each $i \in \{1, \dots, n\}$, a $2$-cell
$$\theta_i : S_i \Rightarrow m_i \quad\text{with boundaries } f_i, f_{i+1},$$
where $S_i$ is a string of horizontal $1$-cells from $A_{i-1}'$ to $A_i'$ and the boundaries match ($f_1, \dots, f_{n+1}$ form a compatible chain), there is a composite $2$-cell
$$\theta \cdot (\theta_1, \dots, \theta_n) : S_1 S_2 \cdots S_n \Rightarrow p$$
with the concatenated string $S_1 \cdots S_n$ as top, $p$ as bottom, and outer vertical boundaries $f \circ f_1$ and $g \circ f_{n+1}$.

6. **Identity $2$-cells**: for each horizontal $1$-cell $m : A \nrightarrow B$, a $2$-cell $1_m : (m) \Rightarrow m$ with identity vertical boundaries.

This data is required to satisfy **associativity** of substitution (substituting strings into strings into strings is unambiguous, mirroring the associativity of path-concatenation) and the **unit laws** ($1_p \cdot (\theta_1, \dots, \theta_n) = \theta$ where the left input has length matching, and $\theta \cdot (1_{m_1}, \dots, 1_{m_n}) = \theta$). Together these say exactly that $\mathcal{C}$ is a monoid in the bicategory of $\mathrm{fc}$-spans — see the Categorical / Structural Definition.

---

# Categorical / Structural Definition

The slick definition is one line: **an fc-multicategory is an $\mathrm{fc}$-multicategory** — a [[Def - Generalized Multicategory|generalized multicategory]] for the **free-category monad** $\mathrm{fc}$ on the category $\mathbf{Gph}$ of directed graphs. Unpacking this is the whole content, and it is worth doing because it explains where the four-layer shape comes from.

A **directed graph** is a pair of sets $\big(G_1 \rightrightarrows G_0\big)$ — a set $G_0$ of vertices, a set $G_1$ of edges, and two maps $s, t : G_1 \to G_0$ (source and target). A morphism of graphs is a pair of functions commuting with $s$ and $t$. The category $\mathbf{Gph}$ has finite limits, in particular pullbacks. The **free-category monad** $\mathrm{fc} : \mathbf{Gph} \to \mathbf{Gph}$ sends a graph $G$ to the graph $\mathrm{fc}(G)$ with the same vertices and with *paths* as edges: an edge of $\mathrm{fc}(G)$ from $A$ to $B$ is a finite string $A = A_0 \xrightarrow{e_1} A_1 \xrightarrow{e_2} \cdots \xrightarrow{e_n} A_n = B$ of composable edges of $G$, including the empty path at each vertex. The unit $\eta : G \to \mathrm{fc}(G)$ sends an edge to the length-one path; the multiplication $\mu : \mathrm{fc}\,\mathrm{fc}(G) \to \mathrm{fc}(G)$ flattens a path-of-paths into a single path by concatenation. This monad is **cartesian**: it preserves pullbacks and its unit and multiplication are cartesian natural transformations (their naturality squares are pullbacks). Cartesianness is exactly the hypothesis that makes the theory of [[Def - Generalized Multicategory|generalized multicategories]] go through, because it lets one speak of $T$-spans and compose them.

Now feed $T = \mathrm{fc}$ into the general recipe. A **$T$-multicategory** is a diagram
$$T C_0 \xleftarrow{\;\mathrm{dom}\;} C_1 \xrightarrow{\;\mathrm{cod}\;} C_0$$
in $\mathbf{Gph}$ — an object-of-objects graph $C_0$, an object-of-cells graph $C_1$, with a "domain" map landing in $T C_0$ (so the domain of a cell is a *path* in $C_0$) and a "codomain" map landing in $C_0$ (so the codomain is a *single* edge) — equipped with identities and a composition making it a monoid for the substitution product on $T$-spans. Read off the layers: the vertices of $C_0$ are the **objects**; the edges of $C_0$ are the **horizontal $1$-cells**; the vertices of $C_1$ over a pair of $C_0$-vertices, with their own source/target into the vertical structure, give the **vertical $1$-cells** and the **$2$-cells**; the domain landing in $T C_0 = \mathrm{fc}(C_0)$ is exactly the statement "the top of a $2$-cell is a path (string) of horizontal $1$-cells". The monoid structure on $T$-spans is precisely the substitution composition (5) and identities (6) above. So the four-layer, string-on-top picture is not an arbitrary choice — it is the image of the path-monad $\mathrm{fc}$ under the universal generalized-multicategory construction.

---

# Relate to Other Fields / Compression

The fc-multicategory is best understood as the **least committal home for "horizontal composition that has not happened yet"**. Every nearby structure is obtained by deciding *how much* horizontal composition to force. Force every string to have a chosen universal composite and you get a [[Def - Weak Double Category|weak double category]]. Force that *and* collapse the vertical category to be trivial (one object, only identity vertical $1$-cells) and you get a [[Def - 2-Category and Bicategory|bicategory]]. Collapse instead to a single object and a single horizontal $1$-cell type and you get a [[Def - Monoidal Category|monoidal category]] or, with trivial vertical structure, an ordinary [[Def - Multicategory|multicategory]]. This is the content of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]].

The compression to internalise is the analogy with [[Def - Multicategory|multicategories]] themselves. An ordinary multicategory replaces a category's "arrows take one input" with "arrows take a *list* of inputs", and a category is recovered as the special case where the only allowed input-lists have length one with composites. An fc-multicategory does the *same move one dimension up*: it replaces a double category's "$2$-cells have one horizontal $1$-cell on top" with "$2$-cells have a *list* (string) of horizontal $1$-cells on top". The free-monoid monad on $\mathbf{Set}$ powers the first move; the free-category monad on $\mathbf{Gph}$ powers the second. They are the same idea applied to graphs instead of sets.

**True name:** an fc-multicategory is *a virtual double category* — "virtual" because horizontal composites are not given but only *represented* by universal $2$-cells, exactly as in a multicategory the tensor of the inputs is not given but represented by multimaps. When you see "fc-multicategory" in Leinster, read "virtual double category" (the now-standard name due to Cruttwell–Shulman); the two are the same structure, and the latter name tells you what to picture: a double category in which horizontal composition is potential rather than actual.

---

# Examples / Corollaries

**Is an instance — any ordinary [[Def - Multicategory|multicategory]].** Take an fc-multicategory with a single object $\ast$ and only the identity vertical $1$-cell. Then horizontal $1$-cells $\ast \nrightarrow \ast$ are just "types", and a $2$-cell with top $(m_1, \dots, m_n)$ and bottom $p$ is exactly a multimap $(m_1, \dots, m_n) \to p$. Substitution of $2$-cells becomes multicategory composition. So plain multicategories are the "one object, trivial vertical structure" fc-multicategories — the string-on-top is the list-of-inputs of a multimap.

**Is an instance — any [[Def - Monoidal Category|monoidal category]].** Specialise further to a single horizontal $1$-cell type as well: one object $\ast$, one horizontal $1$-cell $\ast \nrightarrow \ast$ for each *object* of the monoidal category $\mathcal{V}$ (so horizontal $1$-cells $=$ objects of $\mathcal{V}$), and $2$-cells $(X_1, \dots, X_n) \Rightarrow Y$ equal to morphisms $X_1 \otimes \cdots \otimes X_n \to Y$ in $\mathcal{V}$. Substitution is composition together with $\otimes$. Here the empty string ($n = 0$) corresponds to the monoidal unit $I$, and the associativity of substitution encodes the coherence of $\otimes$ — this is one half of why coherence "comes for free" in the fc-multicategory packaging.

**Is an instance — any [[Def - 2-Category and Bicategory|bicategory]].** A bicategory $\mathcal{B}$ becomes an fc-multicategory with one object [in the sense of "no vertical structure"] per object of $\mathcal{B}$, horizontal $1$-cells $=$ the $1$-cells of $\mathcal{B}$, and a $2$-cell $(m_1, \dots, m_n) \Rightarrow p$ equal to a $2$-cell of $\mathcal{B}$ from the composite $m_n \circ \cdots \circ m_1$ to $p$. The string on top *is* the pasting that a bicategory would compose; packaging it as data rather than as a forced composite is exactly what removes the need to choose bracketings and to state associativity coherence by hand. See [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]].

**Is an instance — the fc-multicategory of rings, bimodules, and maps.** Objects: [[Def - Ring|rings]]. Vertical $1$-cells $R \to S$: ring homomorphisms. Horizontal $1$-cells $R \nrightarrow S$: $(R, S)$-bimodules. A $2$-cell from a string $(M_1, \dots, M_n)$ of bimodules ($M_i$ an $(R_{i-1}, R_i)$-bimodule) to a bimodule $P$, with vertical boundaries $f : R_0 \to S_0$ and $g : R_n \to S_n$: an $(f, g)$-equivariant map $M_1 \otimes_{R_1} \cdots \otimes_{R_{n-1}} M_n \to P$. This is a genuine four-layer example where the vertical category (ring homomorphisms) is non-trivial and horizontal composition (tensor of bimodules) exists, so it is even a [[Def - Weak Double Category|weak double category]]; forgetting that the composites exist and keeping only the $2$-cells recovers the plain fc-multicategory.

**Is NOT an instance — a double category presented with horizontal composition but no $2$-cells over strings.** If you write down objects, two kinds of arrows, and only those $2$-cells whose top is a *single* horizontal $1$-cell (the data of a plain double category), you do **not** automatically have an fc-multicategory: the substitution law (5) requires $2$-cells whose top is a string of length $\neq 1$, and these are exactly what a bare double category omits. The repair is to *define* the string-top $2$-cells from the horizontal composites — a $2$-cell $(m_1, \dots, m_n) \Rightarrow p$ is a double-category $2$-cell $m_1 \odot \cdots \odot m_n \Rightarrow p$ — which is precisely the functor "every double category is an fc-multicategory". Without performing that step, the raw double-category data fails the axioms because the $2$-cell layer is too thin.

**Calibration check.** Convince yourself of three things. First, the $n = 0$ (empty-string) $2$-cells genuinely matter: in the monoidal-category example they are the morphisms $I \to Y$ out of the unit, so deleting them would amputate the unit object. Second, substituting identity $2$-cells $1_{m_i}$ into a $2$-cell $\theta$ returns $\theta$ unchanged — write out the boundaries and check the concatenated string is $(m_1, \dots, m_n)$ again. Third, the vertical category and the horizontal $1$-cells share the *objects*, so an fc-multicategory cannot have "more objects horizontally than vertically" — there is one object class, and both kinds of $1$-cell hang off it.

---

# Unlocked by This

> [!tip] Weak Double Category *(from this chapter)*
> An fc-multicategory in which every string of horizontal $1$-cells has a universal composite is exactly a [[Def - Weak Double Category|weak double category]]. The fc-multicategory is the ambient structure; demanding "all horizontal composites exist and are representable" cuts out the weak double categories inside it, the same way demanding "all tensors exist" cuts representable [[Def - Multicategory|multicategories]] out of all multicategories.

> [!tip] Profunctors, Mod(𝒦), and the calculus of bimodules *(from this chapter and beyond)*
> The "rings, bimodules, maps" example is the prototype of an enormous family: for any nice [[Def - 2-Category and Bicategory|bicategory]] 𝒦, the [[Def - Monad Monoid and Module in a Bicategory|monads, modules, and module maps]] in 𝒦 assemble into an fc-multicategory (and, when composites exist, the bicategory **Mod(𝒦)** of [[Thm - Monoids and Modules Form a Bicategory]]). Taking 𝒦 = **Span(Set)** recovers small categories, functors, and **profunctors**; taking 𝒦 = the bicategory of [[Def - Category|categories]] and profunctors recovers enriched and internal category theory uniformly.

> [!tip] Opetopes via slicing *(from later in Leinster)*
> Iterating a slice construction on generalized multicategories — of which the fc-multicategory is the running fc-example — produces the **opetopes**, the cell shapes of the Baez–Dolan definition of weak $n$-category. The string-on-top $2$-cell is the $2$-dimensional opetope ("many arrows in, one arrow out"); higher opetopes are the same picture one dimension up.
