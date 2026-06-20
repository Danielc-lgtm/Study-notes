---
type: definition
subject: higher-categories
prereqs:
  - "Def - Category"
  - "Def - 2-Category and Bicategory"
  - "Def - fc-Multicategory"
  - "Def - Functor"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A **double category** $\mathbb{D}$ has two kinds of $1$-cell and one kind of $2$-cell. We write objects as $A, B, C, \dots$; **vertical $1$-cells** as $f : A \to A'$ (downward arrows), composed by $\circ$ and strictly associative; **horizontal $1$-cells** as $m : A \nrightarrow B$ (slashed horizontal arrows), composed by $\odot$ (read "then"), so $m \odot m' : A \nrightarrow C$ for $m : A \nrightarrow B$, $m' : B \nrightarrow C$; and **$2$-cells** as squares
$$
\begin{array}{ccc}
A & \xrightarrow{\;m\;} & B \\
f \downarrow & \ \ \alpha \Downarrow & \downarrow g \\
A' & \xrightarrow{\;m'\;} & B'
\end{array}
$$
with top $m$, bottom $m'$, left $f$, right $g$. A $2$-cell has *one* horizontal $1$-cell on top and *one* on the bottom — this is the difference from the string-topped $2$-cells of an [[Def - fc-Multicategory|fc-multicategory]]. The horizontal unit at an object $A$ is written $\mathrm{U}_A : A \nrightarrow A$ (or $1_A^h$). The vertical identity is $1_A : A \to A$. The full registry is on [[Higher Categories — fc-Multicategories and Weak Double Categories]]. "Weak" refers to the horizontal direction: horizontal composition $\odot$ is associative and unital only up to coherent invertible $2$-cells, exactly as $1$-cell composition is in a [[Def - 2-Category and Bicategory|bicategory]].

---

# Axiom Motivation

A category has objects and one kind of arrow. The world, repeatedly, has objects and *two* kinds of arrow that deserve equal billing: in topology, continuous maps and cobordisms; in algebra, ring homomorphisms and bimodules; in logic, functions and relations; in geometry, smooth maps and spans. A double category is the structure that lets two arrow-types coexist on the same objects and *interact through squares*. The motivating demand is symmetry of attention: neither arrow-type should be subordinate. A vertical arrow $f : A \to A'$ is a "map", a horizontal arrow $m : A \nrightarrow B$ is a "process" or "correspondence", and a $2$-cell is a way of saying "this square commutes up to the data $\alpha$".

Why two compositions and why one law connecting them? Because each arrow-type composes in its own direction — vertical maps compose vertically, horizontal processes compose horizontally — and the only thing that could make the two directions a *single* coherent structure is a law saying you can build a big square out of small squares in either order and get the same answer. That law is the **interchange law**: given a $2 \times 2$ grid of $2$-cells, composing each row horizontally and then the two results vertically equals composing each column vertically and then horizontally. Drop interchange and the $2$-cells no longer paste; you have two unrelated category structures glued along their objects, not a double category. The interchange law is the exact analogue of the [[Thm - The Interchange Law|interchange law]] in a $2$-category, which is itself the statement that horizontal and vertical pasting of $2$-cells commute.

Now, why "weak"? In a **strict** double category, horizontal composition $\odot$ is strictly associative and strictly unital, just like vertical composition. That is asking a lot, and most naturally-occurring examples fail it on the nose. Bimodules are the cleanest witness: the tensor product $(M \otimes_S N) \otimes_T P$ and $M \otimes_S (N \otimes_T P)$ are only *canonically isomorphic*, not equal, and the unit bimodule $R$ acts as a unit only up to isomorphism ($R \otimes_R M \cong M$). If you insisted on strictness you would have to throw away bimodules, or pretend isomorphic things are equal — and the second is exactly the kind of dishonest move that coherence theory exists to avoid. So we weaken the horizontal direction: associativity and unitality of $\odot$ hold up to *invertible* $2$-cells (the associator $a$ and unitors $l, r$), subject to coherence axioms (a pentagon and a triangle) that guarantee all the ways of re-bracketing a horizontal composite agree.

Why weaken *only* the horizontal direction and keep vertical composition strict? This is a genuine and load-bearing asymmetry. Vertical $1$-cells are the "maps" — homomorphisms, functions, smooth maps — and these *do* compose strictly: $(h \circ g) \circ f = h \circ (g \circ f)$ literally, because they are honest functions. Horizontal $1$-cells are the "processes" — tensors, spans, relations, cobordisms — built by constructions like $\otimes$ or pullback that are associative only up to canonical iso. So the weakness is allocated to exactly the direction that needs it. A reader who has met both a [[Def - Category|category]] (strict) and a [[Def - 2-Category and Bicategory|bicategory]] (weak in its one composition) can invent the weak double category by asking: "what if I keep one strict composition and add a *second*, weak one, glued by squares satisfying interchange?" That is the definition.

What would break if we kept everything strict but dropped the coherence (pentagon/triangle) for the associator and unitors? Then the associativity isomorphisms would exist but might disagree: two different ways of re-bracketing $m_1 \odot m_2 \odot m_3 \odot m_4$ could give *different* isomorphisms to the fully-left-bracketed form, and "the" horizontal composite of four processes would be ill-defined. The pentagon is precisely the minimal condition making all re-bracketings agree (just as in [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]] for monoidal categories), and the triangle ties the unitors to the associator. These are not optional decorations; they are what make "the horizontal composite of a string" a well-defined notion at all — which is exactly the bridge to the [[Def - fc-Multicategory|fc-multicategory]] picture, where a weak double category is an fc-multicategory all of whose strings have a chosen universal composite.

---

# The Definition

A **(pseudo / weak) double category** $\mathbb{D}$ consists of:

1. A **category of objects and vertical $1$-cells** $\mathbb{D}_0$: objects $A, B, \dots$ and vertical $1$-cells $f : A \to A'$ composing strictly and associatively, with identities $1_A$.

2. A **category of horizontal $1$-cells and $2$-cells** $\mathbb{D}_1$: objects are horizontal $1$-cells $m : A \nrightarrow B$; morphisms are $2$-cells $\alpha$, drawn as squares with a top and a bottom horizontal $1$-cell and two vertical sides, composed *vertically* (stacking squares) strictly and associatively.

3. Source and target functors $S, T : \mathbb{D}_1 \to \mathbb{D}_0$ assigning to a horizontal $1$-cell its source/target objects and to a $2$-cell its left/right vertical boundaries.

4. A **horizontal unit** functor $\mathrm{U} : \mathbb{D}_0 \to \mathbb{D}_1$ sending $A \mapsto \mathrm{U}_A : A \nrightarrow A$ and a vertical $1$-cell $f$ to the obvious unit $2$-cell.

5. A **horizontal composition** functor $\odot : \mathbb{D}_1 \times_{\mathbb{D}_0} \mathbb{D}_1 \to \mathbb{D}_1$ (defined on horizontally composable pairs) sending $(m, m')$ to $m \odot m'$ and acting on $2$-cells by horizontal pasting.

6. Natural **associativity** and **unit** isomorphisms (invertible $2$-cells with identity vertical boundaries)
$$a : (m \odot m') \odot m'' \xRightarrow{\ \cong\ } m \odot (m' \odot m''), \qquad l : \mathrm{U}_A \odot m \xRightarrow{\ \cong\ } m, \qquad r : m \odot \mathrm{U}_B \xRightarrow{\ \cong\ } m,$$
subject to the **pentagon** coherence axiom for $a$ and the **triangle** coherence axiom relating $a, l, r$.

These are required to satisfy the **interchange law**: for a $2 \times 2$ grid of $2$-cells, $(\beta \odot \beta') \circ (\alpha \odot \alpha') = (\beta \circ \alpha) \odot (\beta' \circ \alpha')$, where $\circ$ is vertical and $\odot$ horizontal composition of $2$-cells.

When $a, l, r$ are *identities* (strict associativity and unitality of $\odot$), $\mathbb{D}$ is a **strict double category**, equivalently a [[Def - Category|category]] internal to $\mathbf{Cat}$.

---

# Categorical / Structural Definition

There are two complementary structural readings.

**As a category internal to $\mathbf{Cat}$ (strict case), weakened.** A *strict* double category is exactly an internal category in $\mathbf{Cat}$: a pair of categories $\mathbb{D}_1 \rightrightarrows \mathbb{D}_0$ with internal source, target, identity, and composition functors satisfying the category axioms strictly. Reading the internal structure out: objects of $\mathbb{D}_0$ are objects, morphisms of $\mathbb{D}_0$ are vertical $1$-cells, objects of $\mathbb{D}_1$ are horizontal $1$-cells, morphisms of $\mathbb{D}_1$ are $2$-cells. A *weak* double category replaces "internal category" with "internal pseudocategory" — the internal composition is associative and unital only up to coherent invertible $2$-cells, which is the data of (6) above. This is the precise sense in which a double category is "a category of categories": it is a category object whose objects-and-arrows are themselves categories.

**As an fc-multicategory with all composites (the load-bearing reading for this chapter).** A weak double category is exactly an [[Def - fc-Multicategory|fc-multicategory]] in which *every string of horizontal $1$-cells admits a universal (representing) composite*. Recall an fc-multicategory has $2$-cells whose top is a *string* $(m_1, \dots, m_n)$. Say a horizontal $1$-cell $p$ together with a $2$-cell $\iota : (m_1, \dots, m_n) \Rightarrow p$ **represents** the string if every $2$-cell out of the string factors *uniquely* through $\iota$ — that is, $\iota$ is universal among $2$-cells with that top. When such a representing $p$ exists for every string (and for the empty string, giving the horizontal unit), the universal $p$ *is* the horizontal composite $m_1 \odot \cdots \odot m_n$, the factorisations *are* the action of $\odot$ on $2$-cells, and uniqueness forces the associator and unitors and their coherence automatically. So: **fc-multicategory $+$ "all strings representable" $=$ weak double category**. This is the higher-dimensional echo of "multicategory $+$ all tensors representable $=$ monoidal category" — the representability that upgrades a [[Def - Multicategory|multicategory]] to a [[Def - Monoidal Category|monoidal category]], applied to graphs instead of sets.

---

# Relate to Other Fields / Compression

The weak double category is the natural home for **"maps and processes side by side"**, and the single most useful instance to keep in mind is bimodules: rings as objects, ring homomorphisms as vertical maps, bimodules as horizontal processes, equivariant maps as $2$-cells, tensor product as horizontal composition. Almost every weak double category you meet is a variant of this — replace rings by categories and bimodules by [[Def - Generalized Multicategory|profunctors]], or replace rings by spaces and bimodules by spans, or by relations, or by cobordisms. The reason bimodule-tensor is the prototype is that it is *exactly* the construction that is associative-up-to-canonical-iso but not on the nose, which is what "weak in the horizontal direction" was invented to accommodate.

**True name:** a weak double category is *a pseudocategory internal to $\mathbf{Cat}$* — or, in the language of this chapter, *a representable fc-multicategory*. The first name tells you the formal definition (an internal category, with the composition law weakened to a pseudo-law); the second tells you where it sits among the structures of Leinster Chapter 5 and how to test for it: take an fc-multicategory and ask whether horizontal composites exist as universal $2$-cells. If they do, it is a weak double category; if they only sometimes do, it is a genuinely virtual structure and must stay an fc-multicategory.

This compresses a lot. A [[Def - 2-Category and Bicategory|bicategory]] is a weak double category with trivial vertical structure (only identity vertical $1$-cells), so "bicategory" $=$ "one-object-per-object weak double category". A [[Def - Monoidal Category|monoidal category]] is a one-object bicategory, hence a weak double category with one object and trivial vertical structure. So the chain *monoidal category $\subset$ bicategory $\subset$ weak double category* is a chain of "add back a dimension of structure", and the fc-multicategory sits above all of them as the version where horizontal composition is potential rather than actual.

---

# Examples / Corollaries

**Is an instance — $\mathbb{R}\mathrm{ing}$ (rings, homomorphisms, bimodules).** Objects: [[Def - Ring|rings]]. Vertical $1$-cells: ring homomorphisms (strict composition). Horizontal $1$-cells $R \nrightarrow S$: $(R,S)$-bimodules. $2$-cells: bimodule maps compatible with the vertical boundary homomorphisms. Horizontal composition: $M \odot N = M \otimes_S N$ for $M$ an $(R,S)$-bimodule and $N$ an $(S,T)$-bimodule. Associativity holds only up to the canonical isomorphism $(M \otimes_S N) \otimes_T P \cong M \otimes_S (N \otimes_T P)$ — *this is the canonical example of weakness*. The horizontal unit at $R$ is $R$ as an $(R,R)$-bimodule, a unit only up to $R \otimes_R M \cong M$.

**Is an instance — $\mathbb{S}\mathrm{pan}(\mathcal{E})$ (spans in a category with pullbacks).** Objects: objects of $\mathcal{E}$. Vertical $1$-cells: morphisms of $\mathcal{E}$. Horizontal $1$-cells $A \nrightarrow B$: spans $A \leftarrow S \to B$. $2$-cells: maps of spans (with the obvious boundaries). Horizontal composition: composite span via [[Def - Pullback and Pushout|pullback]] over the shared object. Weakness is forced because pullback is associative only up to canonical iso. When $\mathcal{E} = \mathbf{Set}$, this is the prototype underlying [[Def - Monad Monoid and Module in a Bicategory|monads in Span(Set) = small categories]].

**Is an instance — $\mathbb{C}\mathrm{at}$ (categories, functors, profunctors).** Objects: small [[Def - Category|categories]]. Vertical $1$-cells: [[Def - Functor|functors]]. Horizontal $1$-cells $\mathcal{A} \nrightarrow \mathcal{B}$: **profunctors** $\mathcal{A}^{op} \times \mathcal{B} \to \mathbf{Set}$. $2$-cells: natural transformations compatible with the boundary functors. Horizontal composition: profunctor composition via a coend $\int^{a} P(-, a) \times Q(a, -)$, associative up to canonical iso. This weak double category is the universal home of enriched/internal category theory.

**Is NOT an instance (strictly) — bimodules treated as a strict double category.** If you *declared* $(M \otimes_S N) \otimes_T P$ equal to $M \otimes_S (N \otimes_T P)$, you would be asserting a strict double category structure on rings-and-bimodules, and it is **false**: the two tensor products are isomorphic, not identical, so the strict associativity functoriality fails. The repair is exactly weakening — introduce the associator $a$ as an invertible $2$-cell and impose the pentagon. This is why the bimodule example *must* be weak: there is no strict double category of rings and bimodules.

**Is NOT an instance — two categories glued on objects without interchange.** Take the objects to be sets, vertical $1$-cells functions, horizontal $1$-cells functions too, and $2$-cells only the trivially commuting squares; if you then *define* horizontal composition to be function composition but allow $2$-cells that do not respect it, the interchange law fails and you do not have a double category. The interchange law is the non-negotiable compatibility between the two compositions; without it the $2$-cell layer does not paste and the structure is just two categories sharing object names.

**Calibration check.** Verify three things. First, in $\mathbb{R}\mathrm{ing}$, the associator $a$ for bimodules is genuinely the canonical tensor-associativity iso and *not* an identity — pick $R = S = T$ a field and a non-trivial example to feel that the objects differ. Second, a strict double category is the same as a category internal to $\mathbf{Cat}$: take $\mathbb{D}_1 \rightrightarrows \mathbb{D}_0$ both small categories and check the internal-category axioms recover the four-layer data. Third, restricting a weak double category to one object and only the identity vertical $1$-cell yields a [[Def - 2-Category and Bicategory|bicategory]] — confirm the horizontal $1$-cells become the $1$-cells, the $2$-cells become the bicategory $2$-cells, and the associator/unitors become the bicategory's.

---

# Unlocked by This

> [!tip] Mod(𝒦) and the bicategory of bimodules *(from this chapter)*
> When a weak double category's horizontal structure is built from [[Def - Monad Monoid and Module in a Bicategory|monads and modules]] in a [[Def - 2-Category and Bicategory|bicategory]] 𝒦, restricting to the horizontal $1$-cells and $2$-cells (forgetting the vertical maps) gives the **bicategory Mod(𝒦)** of [[Thm - Monoids and Modules Form a Bicategory]]. The double category remembers the maps between the rings; the bicategory remembers only the bimodules.

> [!tip] Equipments and formal category theory *(from later category theory)*
> A weak double category in which every vertical $1$-cell $f$ has companion and conjoint horizontal $1$-cells is a **proarrow equipment** (Wood), the setting in which Kan extensions, the Yoneda lemma, and the theory of [[Def - Generalized Multicategory|profunctors]] can be developed *formally* — purely from the double-category axioms, independently of $\mathbf{Set}$. This is the modern framework for "category theory done category-theoretically".

> [!tip] Cobordism categories and TQFT *(from mathematical physics)*
> Manifolds, smooth maps, and cobordisms form a (symmetric monoidal) double category; a **TQFT** is a structure-preserving functor out of its horizontal part into vector spaces. The double-category packaging keeps track of both the boundary-restriction maps (vertical) and the cobordisms themselves (horizontal), which is the right setting for *extended* topological field theories.
