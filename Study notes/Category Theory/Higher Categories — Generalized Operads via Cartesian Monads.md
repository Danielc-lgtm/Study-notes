---
type: topic
subject: higher-categories
chapter: "HC4"
title: "Higher Categories — Generalized Operads via Cartesian Monads"
tags: [category-theory, higher-categories, foundations]
---

# Notation Registry

This chapter works in a fixed ambient category $\mathcal{E}$ together with a monad $T$ on it. The standing convention is that $\mathcal{E}$ **has pullbacks** and a **terminal object** $1$, and that $T$ is **cartesian** in the sense of §1 (it preserves pullbacks and its unit and multiplication are cartesian natural transformations). Two running instances should be kept in mind throughout: $\mathcal{E} = \mathbf{Set}$ with $T =$ the free-monoid monad, and $\mathcal{E} = \mathbf{Set}$ with $T =$ the identity monad. The reader who fixes these two examples in working memory will be able to decode every abstract statement on the page.

- $\mathcal{C}, \mathcal{D}, \mathcal{E}$ — categories; $\mathcal{E}$ is the ambient category carrying the monad $T$
- $A, B, C, X, Y$ — objects; $f, g, h$ — morphisms
- $1$ — a terminal object of $\mathcal{E}$ (the object with exactly one map from every other object)
- $T : \mathcal{E} \to \mathcal{E}$ — a monad's endofunctor; $\eta : 1_{\mathcal{E}} \Rightarrow T$ its unit; $\mu : T^2 \Rightarrow T$ its multiplication
- $T^2 = T \circ T$, $T^3 = T \circ T \circ T$ — iterated endofunctor
- $\eta_A : A \to TA$, $\mu_A : T^2 A \to TA$ — components of unit and multiplication at $A$
- $A \times_C B$ — the pullback of $A \to C \leftarrow B$ (the "fibre product")
- $C_0$ — the object-of-objects of a $T$-multicategory; $C_1$ — the object-of-arrows
- $\mathrm{dom} : C_1 \to T C_0$ — the domain (source) map; $\mathrm{cod} : C_1 \to C_0$ — the codomain (target) map
- $\mathrm{ids} : C_0 \to C_1$ — the identities map; $\mathrm{comp} : C_1 \times_{T C_0} T C_1 \to C_1$ — the composition map
- $E(\mathcal{E})$ or $(\mathcal{E}, T)\text{-}\mathbf{Multicat}$ — the category of $T$-multicategories
- $\mathbf{Set}$, $\mathbf{Cat}$, $\mathbf{Gph}$ (directed graphs), $\mathbf{GSet}$ (globular sets) — named ambient categories
- $T = \mathrm{id}$ — the identity monad; $T = (-)^{*}$ — the free-monoid monad $X \mapsto \coprod_{n \geq 0} X^n$
- $\mathbb{T}$ — the free-strict-$\omega$-category monad on globular sets (forward reference)
- $\mathbf{y}$ — Yoneda embedding (when it appears); $\cong$ — isomorphism; $\Rightarrow$ — natural transformation

---

# Motivation

Here is the entire chapter in one sentence: *a multicategory, an operad, a category, and a globular operad are all the same kind of thing — a monoid in spans — and the only thing that changes from one to the next is the monad you build the spans out of.* This is Leinster's "generalized operad" program, and its payoff is a single definition that swallows half of higher category theory.

To see why such a unification is even possible, recall what an ordinary [[Def - Category|category]] is, stripped to its bones. You have a set of objects, a set of arrows, two functions $\mathrm{dom}, \mathrm{cod}$ telling you the source and target of each arrow, an identity-assigning function, and a composition rule defined on the set of *composable pairs*. The composable pairs are exactly a pullback: $\{(g,f) : \mathrm{dom}(g) = \mathrm{cod}(f)\}$. So a small category is a pair of sets with structure maps where composition is defined over a pullback. Now look at a classical **[[Def - Multicategory|multicategory]]** (an [[Def - Operad|operad]] with many objects). The difference is that an arrow no longer has a single object as its source — it has a *finite list* of objects, $(a_1, \dots, a_n) \to b$. The composition of multimaps grafts a tree of inputs into a single multimap. The bookkeeping looks more complicated, but it is the *same* bookkeeping with one change: where a category's arrow had domain an object, a multicategory's arrow has domain a *list of objects*, and where a category composed over composable pairs, a multicategory composes over composable *trees*.

"List of objects" and "tree of multimaps" are not ad hoc. The operation "form a finite list" is a monad on $\mathbf{Set}$ — the [[Def - Free-Forgetful Adjunction|free-monoid monad]] $X \mapsto X^{*} = \coprod_{n \geq 0} X^n$, whose unit is the singleton list and whose multiplication is concatenation. The composable trees are exactly the pullbacks that this monad produces. The realization that organizes the whole chapter is that *the only place the monad enters the definition of a category is in saying what the domain of an arrow is allowed to be*. Replace the identity monad (domain is a single object) by the free-monoid monad (domain is a list), and the definition of a category turns into the definition of a multicategory, with no other change. The structural backbone of the chapter is therefore the substitution table

$$\text{generalized multicategory} \;=\; \text{monoid in } T\text{-spans}, \qquad T = \begin{cases} \mathrm{id} & \rightsquigarrow \text{ categories} \\ (-)^{*} & \rightsquigarrow \text{ classical multicategories / operads} \\ \mathbb{T} & \rightsquigarrow \text{ globular operads (HC7)} \end{cases}$$

which we will derive, not merely assert.

What does it cost to make this work? Not every monad will do. For "domain a $T$-shape of objects" to support a sensible composition, the monad has to interact correctly with pullbacks — the composable configurations have to *be* pullbacks, and grafting has to respect them. The exact condition is that $T$ is **cartesian**: it preserves pullbacks, and the naturality squares of its unit and multiplication are pullbacks. This is §1. With a cartesian monad in hand, §2 builds the definition of a $T$-**multicategory** as a monad-graph — an object-of-objects $C_0$, an object-of-arrows $C_1$, a domain map $\mathrm{dom} : C_1 \to T C_0$ landing in the $T$-shape of objects, a codomain map $\mathrm{cod} : C_1 \to C_0$, and identity and composition maps satisfying associativity and unitality — equivalently a monoid in the bicategory of $T$-spans. A $T$-**operad** is the one-object case, $C_0 = 1$. Section 3 defines what it means to *act*: an algebra for a $T$-operad, which recovers [[Def - Group|groups]], monoids, $T$-algebras, and the algebras of classical operads as special cases, and we finally lay the unifying table on the desk and read it off.

The reader is assumed to be fluent with [[Def - Category|categories]], [[Def - Functor|functors]], and [[Def - Natural Transformation|natural transformations]]; comfortable with [[Def - Monad and Comonad|monads]] $(T, \eta, \mu)$ and with the slogan that a monad is a monoid in endofunctors; and comfortable with [[Def - Pullback and Pushout|pullbacks]] and [[Def - Limit and Colimit|limits]] as universal cones. Familiarity with the *classical* notion of a **multicategory** and **operad** (Leinster Chapter 2, the previous chapter HC3) helps but is not required: every example restates what it needs. No knowledge of higher category theory is assumed; the globular and $\omega$-categorical material is presented purely as the destination this machinery was built to reach.

---

# Concept Map

## §1 Cartesian Monads

- **[[Def - Cartesian Monad]]**
	- A monad $(T, \eta, \mu)$ on a category $\mathcal{E}$ with [[Def - Pullback and Pushout|pullbacks]] is **cartesian** if (i) $T$ preserves pullbacks, and (ii) the unit $\eta$ and multiplication $\mu$ are **cartesian** natural transformations, meaning every naturality square is a pullback. Concretely, for $\eta$ this says the square with corners $A, B, TA, TB$ built from $f : A \to B$ and the units $\eta_A, \eta_B$ is a pullback; similarly for $\mu$. The condition is exactly what lets one form "composable $T$-shapes" as pullbacks and have $T$ respect them. The identity monad is cartesian; the free-monoid monad $X \mapsto X^{*}$ is cartesian; the free-commutative-monoid and the [[Def - Algebra for a Monad|powerset]] monads are **not**.

- **[[Thm - The Free Multicategory Monad]]**
	- For a cartesian monad $T$ on a suitable $\mathcal{E}$, the construction "freely generate a $T$-multicategory from a $T$-graph" is itself a cartesian monad $T^{+}$ on the category of $T$-graphs, whose algebras are exactly the $T$-[[Def - Multicategory|multicategories]]. Specializing to $\mathcal{E} = \mathbf{Set}$, $T = \mathrm{id}$ gives the free-category monad on directed graphs; $T = (-)^{*}$ gives the free-(plain)-multicategory monad. This $(-)^{+}$ operation can be iterated, and that iteration is the engine behind [[Def - Opetope|opetopes]] (HC6). The theorem is what guarantees free $T$-multicategories exist and that the framework is closed under its own construction.

> [!tip] Unlocked: [[Def - The Free Strict ω-Category Monad|The Free Strict ω-Category Monad]] *(from Higher Category Theory)*
> The free-category monad produced by the $(-)^{+}$ construction is the bottom rung of a ladder. Run an analogous free construction on **globular sets** — graphs with cells in every [[Def - Dimension|dimension]] — and you get the **free strict ω-category monad** $\mathbb{T}$, whose operations are the *globular pasting diagrams*. That $\mathbb{T}$ is itself cartesian is the fact that makes **globular operads** possible, and hence makes the Batanin–Leinster definition of a weak $\omega$-category possible (HC7).

> [!tip] Unlocked: Familially Representable Functors *(from Categorical Algebra)*
> A monad is cartesian and "finitary in the right way" precisely when its functor is **familially representable** — a coproduct of representables, $TX \cong \coprod_i \mathcal{E}(C_i, X)$. This is **Carboni–Johnstone**'s characterization, and it explains *why* the free-monoid monad is cartesian (its operations are the finite ordinals, a small family of arities) while the free-commutative-monoid monad is not (symmetry collapses the family). It is the bridge from the bicategory-of-spans picture to the combinatorics of arities.

- **[[Ex - The list monad is cartesian]]** (⭐⭐)
	- Verify that the free-monoid (list) monad $X \mapsto X^{*}$ is cartesian: it preserves pullbacks, and the unit and multiplication squares are pullbacks. The technique is shape-reconstruction — a list of structured things is a structure of equal-length lists, and the length data is exactly the pullback. The ordered (symmetry-free) nature of lists is load-bearing.

- **[[Ex - The free-commutative-monoid monad is not cartesian]]** (⭐⭐⭐)
	- Refute cartesianness of the multiset (free-commutative-monoid) monad by exhibiting one multiplication square that is not a pullback: $\{\{a\},\{a,b\}\}$ and $\{\{a,a\},\{b\}\}$ flatten to the same multiset with the same shape but are distinct. The symmetric quotient forgets the partition of a repeated element, which is why symmetric operads fall outside the framework.

- **[[Ex - The identity and powerset monads]]** (⭐)
	- Show the identity monad is cartesian (everything is a degenerate pullback) and the powerset monad is not (its unit square admits non-singleton subsets). The lesson: good Eilenberg–Moore behaviour does not imply cartesianness; the singleton sub-family condition is a sharp, geometric constraint.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 Cartesian Monads]]

## §2 T-Operads and T-Multicategories

- **[[Def - Generalized Multicategory]]**
	- A **$T$-multicategory** (for a [[Def - Cartesian Monad|cartesian monad]] $T$ on $\mathcal{E}$) is an object-of-objects $C_0 \in \mathcal{E}$, an object-of-arrows $C_1 \in \mathcal{E}$, structure maps $\mathrm{dom} : C_1 \to T C_0$ and $\mathrm{cod} : C_1 \to C_0$, an identities map $\mathrm{ids} : C_0 \to C_1$, and a composition map $\mathrm{comp} : C_1 \times_{T C_0} T C_1 \to C_1$ defined over the pullback of "composable configurations", satisfying associativity and unitality. Equivalently it is a **monoid in the bicategory of $T$-spans** $C_0 \nrightarrow C_0$. Taking $T = \mathrm{id}$ recovers an internal [[Def - Category|category]]; taking $\mathcal{E} = \mathbf{Set}, T = (-)^{*}$ recovers a classical **[[Def - Multicategory|multicategory]]**, where an arrow has a finite list of objects as input.

- **[[Def - Generalized Operad]]**
	- A **$T$-operad** is a $T$-multicategory with one object: $C_0 = 1$, the terminal object. The data collapse to a single object $P = C_1$ with a map $P \to T1$ (recording the "arity-shape" of each operation), a unit $1 \to P$, and a composition $P \times_{T1} TP \to P$. When $\mathcal{E} = \mathbf{Set}, T = (-)^{*}$, the set $T1 = 1^{*} = \mathbb{N}$ is the natural numbers, the map $P \to \mathbb{N}$ assigns each operation its arity $n$, and $P$ is exactly a classical (non-symmetric) **[[Def - Operad|operad]]** with sets of $n$-ary operations $P(n)$. A $T$-operad is thus the "single sorted" or "monochromatic" generalized multicategory.

- **[[Thm - Generalized Operads Recover Classical Structures]]**
	- Fixing $\mathcal{E} = \mathbf{Set}$: with $T = \mathrm{id}$, $T$-multicategories are small [[Def - Category|categories]] and $T$-operads are [[Def - Monoid in a Monoidal Category|monoids]]; with $T = (-)^{*}$, $T$-multicategories are classical **[[Def - Multicategory|multicategories]]** and $T$-operads are classical non-symmetric **[[Def - Operad|operads]]**; over globular sets with $T = \mathbb{T}$, $T$-operads are **[[Def - Globular Operad|globular operads]]** (HC7). Each identification is an *equivalence of categories*, not a loose analogy, and is proved by unwinding the span/pullback data into the classical axioms. This theorem is the chapter's reason for existing: it certifies that the abstract definition is genuinely a common generalization.

> [!tip] Unlocked: [[Def - fc-Multicategory|fc-Multicategories]] and [[Def - Weak Double Category|Weak Double Categories]] *(from Higher Category Theory)*
> Choose $\mathcal{E} = \mathbf{Gph}$ (directed graphs) and $T = fc$ the **free-category monad**. The resulting $fc$-multicategories — Leinster's **fc-multicategories** (HC5) — have objects, vertical arrows, horizontal arrows, and 2-cells shaped like a string of horizontals on top with one on the bottom. They simultaneously generalize bicategories, monoidal categories, plain multicategories, and double categories, all by varying *which* of the four cell types you forget.

> [!tip] Unlocked: Monads in a Bicategory and the Burroni Picture *(from Higher Category Theory)*
> The slogan "$T$-multicategory = monoid in $T$-spans" is an instance of **Burroni**'s observation that a category internal to $\mathcal{E}$ is a monad in the bicategory $\mathrm{Span}(\mathcal{E})$. Generalizing the span bicategory to the $T$-span bicategory $\mathrm{Span}_T(\mathcal{E})$ and taking monads there gives $T$-multicategories — the same identification that recovers a small category from a monad in $\mathrm{Span}(\mathbf{Set})$, with the arities woven in by $T$.

- **[[Ex - A category is an identity-multicategory]]** (⭐⭐)
	- Unwind a $\mathrm{id}$-multicategory and show it is exactly a small category, the equivalence $(\mathbf{Set}, \mathrm{id})\text{-}\mathbf{Multicat} \cong \mathbf{Cat}$. The whole content is $T C_0 = C_0$; the genuine obligation is to check the equivalence on *morphisms* (multicategory maps are functors), not just objects.

- **[[Ex - A classical operad is a free-monoid-operad]]** (⭐⭐)
	- Unwind a $(-)^{*}$-operad ($C_0 = 1$) and show it is a classical non-symmetric operad with sets $P(n)$. The decisive computation is $T1 = \mathbb{N}$; the trap to avoid is concluding "one object, so a monoid" — collapsing colours does not collapse arities.

- **[[Ex - Computing the arity object T1]]** (⭐)
	- Compute $T1$ for the identity, list, free-category, and globular monads, and read off that their operads are monoids, classical operads, linear-graph-operads, and globular operads. Installs the reflex "new cartesian monad $\rightsquigarrow$ compute $T1$"; watch out for the terminal object in $\mathbf{Gph}$ (one vertex, one loop).

> [!note] Exercise Index — §2
> [[Exercise Index - §2 T-Operads and T-Multicategories]]

## §3 Algebras and the Unifying Picture

- **[[Def - Algebra for a Generalized Operad]]**
	- An **algebra for a $T$-operad** $P$ is an object $X \in \mathcal{E}$ together with an action $h : P \times_{T1} TX \to X$ compatible with the unit and composition of $P$ — equivalently, $X$ is an algebra for the monad on $\mathcal{E}/1 = \mathcal{E}$ that $P$ determines. When $T = (-)^{*}$ and $P$ is the classical operad, an algebra is a set $X$ with operations $P(n) \times X^n \to X$, recovering the classical notion: algebras for the associative operad are [[Def - Monoid in a Monoidal Category|monoids]], algebras for the commutative operad are commutative monoids. The general slogan is: *a $T$-operad is a theory of $T$-shaped operations, and its algebras are the structures that realize that theory*.

- **The Unifying Table**
	- The single display that this entire chapter exists to produce: across the three rows $T = \mathrm{id}$, $T = (-)^{*}$, $T = \mathbb{T}$, the four columns "$T$-graph", "$T$-multicategory", "$T$-operad", "algebra for the $T$-operad" specialize respectively to (directed graph / small category / monoid / set-with-monoid-action), (signature / multicategory / operad / operad-algebra), and (globular set / globular multicategory / globular operad / weak $\omega$-category-of-that-signature). Reading any *row* gives a classical theory; reading any *column* gives a uniform construction. The table is reproduced and drilled in [[Ex - Reading the unifying table across three monads]].

> [!tip] Unlocked: Batanin–Leinster Weak ω-Categories *(from Higher Category Theory)*
> Once algebras for globular operads are in hand, a **weak ω-category** is defined as an algebra for the *initial globular operad equipped with a contraction* — the operad whose operations are "all coherence cells you are forced to have, and no more". Composition becomes a *chosen* operation supplied by the operad rather than a property, which is exactly what makes the definition algebraic and well-behaved (HC7). This is the summit the chapter's machinery was built to reach.

> [!tip] Unlocked: [[Def - Operad|Operads]] in Topology and the Recognition Principle *(from Algebraic Topology)*
> Taking the ambient category to be **Top** rather than $\mathbf{Set}$, an algebra for the little-$n$-disks operad $E_n$ is exactly an $n$-fold loop space (up to [[Def - Homotopy|homotopy]]) — **May's recognition principle**. The generalized framework explains the recognition principle's shape: a space carries the operations of $E_n$ acting coherently, i.e. it is an algebra for a topological operad, and the operad encodes precisely the higher associativities of loop concatenation.

- **[[Ex - Algebras for the associative operad are monoids]]** (⭐⭐)
	- Show that an algebra for the associative operad $\mathrm{Assoc}$ (one operation per arity) is exactly a monoid. The mechanism: the unique ternary operation must equal both of its substitutes, and that coincidence *is* the associativity law $x(yz) = (xy)z$; the binary operation determines all the higher ones.

- **[[Ex - The induced monad of a generalized operad]]** (⭐⭐)
	- Construct the monad $T_P X = P \times_{T1} TX$ associated to a $T$-operad $P$ and prove its Eilenberg–Moore algebras are the $P$-algebras. The multiplication composes operations and flattens shapes in parallel, kept aligned by cartesianness; for $T = (-)^{*}$, $T_P X = \coprod_n P(n) \times X^n$.

- **[[Ex - Reading the unifying table across three monads]]** (⭐⭐⭐)
	- Assemble the four-column table (graph / multicategory / operad / algebra) for $T = \mathrm{id}, (-)^{*}, \mathbb{T}$ and articulate the two reading directions: a *row* is one coherent theory, a *column* is one uniform construction. Conflating them — expecting "operad" to mean a fixed object across rows — is the characteristic error.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 Algebras and the Unifying Picture]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The problems of this chapter cluster around five recurring goals. The first and most frequent is **verifying or refuting that a given monad is cartesian** — checking the two pullback conditions (functor preserves pullbacks; unit and multiplication squares are pullbacks), or producing a counterexample square that fails to be a pullback. The second is **unwinding a generalized definition into a classical one**: given that $T$ is the identity or the free-monoid monad, show that the span/pullback data of a $T$-multicategory are *exactly* the axioms of a category or a multicategory, an equivalence-of-categories statement. The third is **identifying $T1$ and the arity map**, since $T1$ is the object of "arity shapes" and computing it (the natural numbers for $(-)^{*}$, the one-point set for $\mathrm{id}$, the globular pasting diagrams for $\mathbb{T}$) tells you what an operad over $T$ even looks like. The fourth is **constructing algebras and computing the induced monad**, showing that a $T$-operad determines a monad whose algebras are the operad-algebras. The fifth is **recognizing a classical structure as a generalized one** — the input-broadening target: seeing that monoids, categories, operads, and globular operads are all rows of one table. These five — check cartesianness, unwind to classical, compute $T1$, build algebras, recognize the row — are the targets because each pins down one face of the single object "monoid in $T$-spans".

**Sources — what assumptions do we usually leverage?**

The hypotheses are equally stereotyped. **A monad is given on a category with pullbacks**, the richest source, because cartesianness is then a finite checklist and, once verified, the entire $T$-multicategory machine switches on. **An explicit description of $T$ on objects** — "$T X$ is the set of finite lists / finite multisets / pasting diagrams of elements of $X$" — lets you compute $T1$, $T C_0$, and the composable-configuration pullbacks by hand. **A classical structure is given** (a category, a multicategory, an operad), which one re-reads as span data to land it in the framework, the reverse direction of the unwinding target. **The terminal object $1$ is available**, since $T$-operads live over it and $T1$ is the arity object. **A free construction is in play**, where [[Thm - The Free Multicategory Monad|the free T-multicategory monad]] supplies existence and the universal property that pins the free object down. The recurring move is to route a source to a target: an explicit $T$ routes through the pullback checklist to a cartesianness conclusion; a given classical structure routes through the span re-reading to a recognition; the terminal object routes through $T1$ to an arity description; a free construction routes through the $(-)^{+}$ monad to existence and iteration. The [[Higher Categories — Generalized Operads via Cartesian Monads#Problem-Solving Strategy|Problem-Solving Strategy]] makes these routes explicit.

---

# Legal Operations

These are the moves nearly every problem in this chapter is assembled from. When stuck, scan the list and try each one. Everything here is self-contained: a reader who knows only [[Def - Monad and Comonad|monads]] and [[Def - Pullback and Pushout|pullbacks]] should be able to follow each operation.

**Legal operations:**

1. **Specialize the monad to read off a classical structure.** Whenever a $T$-multicategory or $T$-operad appears abstractly, immediately ask "what is $T$?" and substitute. With $T = \mathrm{id}$ the domain map $\mathrm{dom} : C_1 \to T C_0 = C_0$ is just "source of an arrow" and you are looking at a [[Def - Category|category]]; with $T = (-)^{*}$ the domain lands in lists $C_0^{*}$ and you are looking at a multicategory. *Trigger:* any abstract generalized-operad statement. *Pattern:* "set $T = \ldots$, then $T C_0 = \ldots$, so $\mathrm{dom}$ records $\ldots$, which is the classical $\ldots$".

2. **Compute $T1$ to find the arity object.** A $T$-operad lives over the terminal object, and the arity of an operation is its image in $T1$. The single most clarifying computation in any new example is $T1$. *Trigger:* you are handed a new cartesian monad and want to know what its operads look like. For $(-)^{*}$, $T1 = \mathbb{N}$; for the identity, $T1 = 1$ (operations are unsorted, you get a monoid); for the free-commutative-monoid monad, $T1 = \mathbb{N}$ again but the monad is not cartesian, which is *why* symmetric operads do not fit this exact frame.

3. **Check cartesianness as a two-item checklist.** To prove $T$ cartesian, verify (i) $T$ preserves pullbacks, and (ii) every naturality square of $\eta$ and of $\mu$ is a pullback. To *refute* it, exhibit one square that is not a pullback — usually a multiplication square where $T$ has "merged" distinct configurations. *Trigger:* "is this monad cartesian?". *Pattern:* draw the naturality square for a chosen $f$, compute the actual pullback, and compare.

4. **Form the composable-configuration pullback.** Composition in a $T$-multicategory is defined not on all pairs but on the pullback $C_1 \times_{T C_0} T C_1$ of "arrows whose codomain-shape matches the next arrows' domains". Building this pullback explicitly turns an abstract composition law into a concrete grafting of configurations. *Trigger:* you must define or use $\mathrm{comp}$. *Pattern:* "the composable pairs are those agreeing on $T C_0$, i.e. the pullback of $\mathrm{dom}$ along $T(\mathrm{cod})$".

5. **Translate between span data and monad-graph data.** A $T$-multicategory is equivalently a monoid in $T$-spans and a monad-graph $(C_0, C_1, \mathrm{dom}, \mathrm{cod}, \mathrm{ids}, \mathrm{comp})$. Switch freely: the span picture makes associativity a one-line monoid axiom, the explicit-maps picture makes computations concrete. *Trigger:* an associativity or unitality verification. *Pattern:* "as a monoid in $\mathrm{Span}_T$, associativity is $m \circ (m \otimes 1) = m \circ (1 \otimes m)$; unwound, it is the pasting equation $\ldots$".

6. **Collapse to the one-object case to get an operad.** To pass from multicategory to operad, set $C_0 = 1$. Every $T_C0$-indexed gadget collapses; $\mathrm{dom} : C_1 \to T1$ becomes the arity map. *Trigger:* the problem says "operad" or "single object / single sort". *Pattern:* "set $C_0 = 1$; then $T C_0 = T1$, and the data become $(P \to T1, \text{unit}, \text{comp})$".

7. **Turn an operad into a monad and read its algebras.** A $T$-operad $P$ determines a monad $T_P$ on $\mathcal{E}$ (roughly $X \mapsto P \times_{T1} TX$), and an algebra for $P$ is by definition an [[Def - Algebra for a Monad|algebra for Tₚ]]. *Trigger:* "what are the algebras of this operad?". *Pattern:* "$P$-algebra structure on $X$ is a map $P \times_{T1} TX \to X$ respecting unit and composition; this is exactly an Eilenberg–Moore algebra for $T_P$".

8. **Use the free $T$-multicategory monad for existence and induction.** When a problem needs "the free $T$-multicategory on a $T$-graph" or an inductive construction of operations (trees, pasting diagrams), invoke [[Thm - The Free Multicategory Monad|the free T-multicategory monad]] $T^{+}$, which exists because $T$ is cartesian and is itself cartesian, so the construction can be iterated. *Trigger:* "free", "generated by", or "the operations are all formal composites of". *Pattern:* "by the free $T$-multicategory monad, the free object exists; its arrows are the $T^{+}$-trees on the generators".

9. **Recognize a pullback as a fibre of $T$.** Cartesianness means many squares are pullbacks, so a fibre over a point of $T C_0$ (e.g. "arrows of arity $n$") is computed as a pullback against $\eta$ or $\mu$. *Trigger:* you want the operations of a fixed arity/shape. *Pattern:* "the arity-$n$ part of $P$ is the pullback of $P \to T1$ along the point $n : 1 \to T1$".

**Illegal but tempting operations:**

> [!warning] 1. Treating the free-commutative-monoid (or symmetric / multiset) monad as cartesian
> It is tempting to think every "free algebraic structure" monad is cartesian, so that symmetric operads would fit the frame directly. They do not. The free-commutative-monoid monad $X \mapsto \coprod_n X^n / S_n$ is **not** cartesian: a multiplication naturality square fails to be a pullback because the quotient by the symmetric group $S_n$ merges configurations that the pullback keeps distinct. Concretely, over a two-element set the multiset $\{a,a\}$ has fewer preimages than the pullback predicts. The repair is to *drop symmetry*: the free-monoid (list) monad $X \mapsto X^{*}$ is cartesian, which is why this chapter's classical instances are the **non-symmetric** operads. Symmetric operads require the separate symmetric-sequences machinery of HC3.

> [!warning] 2. Composing arbitrary arrows rather than composable configurations
> One is tempted to compose any two arrows of a $T$-multicategory as in a one-object monoid. But composition is defined only on the **pullback** $C_1 \times_{T C_0} T C_1$ — arrows whose output shape matches the next layer's input. With $T = \mathrm{id}$ this is the familiar "you can only compose $g \circ f$ when $\mathrm{dom}(g) = \mathrm{cod}(f)$"; with $T = (-)^{*}$ it is "you can only graft a list of multimaps into a multimap whose inputs match their outputs". Forgetting the matching condition produces nonsense exactly as composing non-composable arrows in a category does. The matching condition *is* the pullback; there is no composition off it.

> [!warning] 3. Assuming $C_0 = 1$ makes a multicategory trivial
> Setting the object-of-objects to the terminal object feels like it should collapse everything, as a one-object category is "just a monoid". For $T = \mathrm{id}$ that intuition is correct — a one-object category *is* a monoid. But for $T = (-)^{*}$ the one-object case is an entire operad: even with one object there are infinitely many *arities*, so $C_1$ over $T1 = \mathbb{N}$ has a set of operations for each $n$. The terminal-object collapse removes the *colours/sorts*, not the *arities*. The richness lives in $T1$, which is trivial only when $T$ is.

> [!warning] 4. Reading the unifying table down a column instead of across a row
> The table tempts you to compare, say, "multicategory" with "globular operad" because they sit in the same column. But a *theory* is a **row**: fix $T$, and the four entries (graph, multicategory, operad, algebra) of that row are one coherent world. Comparing entries *across rows in the same column* compares the same construction applied to different monads, which is a statement about the construction's uniformity, not about any one theory. The error is to expect "operad" to mean the same set of objects regardless of $T$; it means "$T$-operad", and the $T$ is load-bearing.

---

# Problem-Solving Strategy

Every problem in this chapter is won the moment you answer two questions: *what is the monad $T$*, and *which of the five targets am I chasing*. Answer those and the route is almost forced.

If the problem **asks whether a monad is cartesian**, you are in a verification problem, and the instrument is the two-item checklist of [[Def - Cartesian Monad|the definition]]. The route is mechanical: first check that $T$ preserves [[Def - Pullback and Pushout|pullbacks]] (often by knowing $T$ is a right adjoint, or by direct inspection of how $T$ acts on a pullback square), then check that the naturality squares of the unit $\eta$ and the multiplication $\mu$ are pullbacks. To *refute* cartesianness — the more common and more instructive task — you do not check all squares; you hunt for *one* square that fails, and the productive place to hunt is a multiplication square for a monad that "merges" configurations, because merging is exactly what destroys the pullback property. The free-commutative-monoid and powerset monads fail here, and seeing *why* they fail is more valuable than the dozens of positive verifications.

If the problem **asks you to unwind a generalized definition into a classical one**, the assumption pattern is that $T$ is fixed to be the identity or the free-monoid monad, and the route is to substitute and compare term by term. You write out the span data — $C_0, C_1, \mathrm{dom} : C_1 \to T C_0, \mathrm{cod}, \mathrm{ids}, \mathrm{comp}$ — substitute the concrete $T$, and watch each structure map turn into a classical axiom. The single most important sub-skill is computing $T C_0$: with $T = \mathrm{id}$ it is $C_0$, so $\mathrm{dom}$ is an ordinary source map; with $T = (-)^{*}$ it is the set of finite lists of objects, so $\mathrm{dom}$ assigns each arrow its input *list*. Once $T C_0$ is understood, the composition pullback unwinds into "graft trees of arrows", and associativity becomes the classical associativity of operadic composition. These are equivalences of categories, so the discipline is to exhibit functors both ways and check they are mutually inverse — not merely to note a resemblance.

If the problem **asks what the operads or algebras over a new monad are**, compute $T1$ first, always. $T1$ is the object of arity-shapes, and it controls everything: a $T$-operad is a gadget over $T1$, and its algebras are determined by how operations of each shape act. With $T1 = \mathbb{N}$ you get classically-arity-indexed operations; with $T1 = 1$ you get a single unsorted operation, i.e. a [[Def - Monoid in a Monoidal Category|monoid]]; with $T1$ the globular pasting diagrams you get the operations of a globular operad. After $T1$, build the induced monad $T_P$ and identify its [[Def - Algebra for a Monad|Eilenberg–Moore algebras]] — that is the definition of a $P$-algebra, and recognizing $T_P$-algebras as a familiar category (monoids, commutative monoids, etc.) is the punchline.

If the problem **gives you a classical structure and asks to place it in the framework**, you are running the unwinding in reverse: re-read the classical data as span data. A small category becomes a $\mathrm{Span}(\mathbf{Set})$-monoid; a multicategory becomes a monoid in $(-)^{*}$-spans. The trigger is the phrase "show that [classical thing] is a $T$-multicategory for a suitable $T$", and the only real decision is *which* $T$: read off what the domain of an arrow is allowed to be (one object? a list? a tree? a pasting diagram?) and that determines $T$ uniquely.

A meta-strategy threads through all of the above: **the monad is the entire content, so name it first and everything else follows.** The framework is deliberately thin — it is just "monoid in $T$-spans" — precisely so that all the mathematical substance is concentrated in the choice of $T$ and in the cartesianness that makes that choice legal. Whenever a problem feels abstract, the cure is to fix $T$ to be the identity, solve the now-concrete category-theoretic question, then fix $T = (-)^{*}$ and watch the same argument run with lists in place of single objects. Every result in the chapter is a single argument seen through two or three monads.

---

# Most Reusable Properties

- **[[Def - Cartesian Monad|Cartesianness as a pullback licence]]**: the two conditions "$T$ preserves pullbacks" and "$\eta, \mu$ are cartesian" together say *everything in sight is a pullback*. This is the property to reach for whenever you need to compute a fibre, an arity-part, or a composable-configuration object, because each of those is a pullback and cartesianness guarantees $T$ respects it. Its most powerful disguised use is *negative*: a single failed pullback square is a complete proof that a monad is not cartesian, instantly ruling its operads out of this framework. Recognize its applicability whenever the words "fibre", "shape", "arity", or "composable" appear.

- **[[Def - Generalized Multicategory|The monoid-in-spans identity]]**: $T$-multicategory $=$ monoid in $\mathrm{Span}_T(\mathcal{E})$. This is the workhorse for *proving structural facts uniformly*. The recognizable setup is "verify associativity / unitality of a generalized composition": rather than wrestle with pullbacks, invoke the monoid axioms in the span bicategory and let them discharge the proof in one line. It also explains *why* the framework exists — it is Burroni's "category = monad in spans" with arities — and internalizing it makes the recovery theorem feel inevitable rather than surprising.

- **The arity object $T1$**: the terminal-fibre $T1$ is the object of operation-shapes, and computing it is the fastest route to understanding any new instance. Its typical use is diagnostic: before asking what the operads over $T$ are, compute $T1$ and you will know whether you are getting monoids ($T1 = 1$), classical operads ($T1 = \mathbb{N}$), or something exotic. It is reusable because it converts a question about an entire category of operads into a single object computation.

- **[[Thm - The Free Multicategory Monad|The free T-multicategory monad T⁺]]**: from a cartesian $T$ you get a cartesian $T^{+}$ whose algebras are $T$-multicategories. Its typical use is twofold — it supplies the *existence* of free $T$-multicategories (so "the free operad on a signature" is legitimate), and it supplies *iterability* (you can apply $(-)^{+}$ again), which is the mechanism behind opetopes. Reach for it whenever a construction must be performed "freely" or whenever you want to bootstrap from one cartesian monad to the next rung of the ladder.

- **The substitution table**: $T = \mathrm{id} / (-)^{*} / \mathbb{T}$ giving categories / multicategories / globular operads. This is reusable as a *recognition device*. Whenever you meet a higher-categorical structure, ask which monad makes it a row of the table; if you can find the $T$, you inherit the entire generalized theory — free constructions, algebras, slicing — for free. It is the single highest-leverage mental object in the chapter because it turns "learn this new structure" into "identify the monad".

---

# Bridges

1. **Internal category theory and Burroni's theorem — the $T = \mathrm{id}$ floor.** A [[Def - Category|category internal to 𝓔]] is, by Burroni's observation, exactly a monad in the bicategory $\mathrm{Span}(\mathcal{E})$ of spans $A \leftarrow S \to B$ with composition by pullback. The object-of-objects $C_0$, object-of-arrows $C_1$, source/target/identity/composition are precisely the data of such a monad: the endo-span $C_0 \leftarrow C_1 \to C_0$ with a unit (identities) and a multiplication (composition) over the pullback of composable arrows. The generalized-operad framework is this picture with the span bicategory $\mathrm{Span}(\mathcal{E})$ replaced by the $T$-span bicategory $\mathrm{Span}_T(\mathcal{E})$, where the left leg of a span lands in $T C_0$ rather than $C_0$. Setting $T = \mathrm{id}$ collapses $T$-spans back to spans, so internal categories are the bottom row of the table — this is why "category" and "multicategory" feel like cousins: they are the same monoid-in-spans construction read through two different monads.

2. **Classical operads and the symmetric-sequence story — what the non-symmetric restriction costs.** A classical (symmetric) [[Def - Monoid in a Monoidal Category|operad]] in $\mathbf{Set}$ is a sequence of sets $P(0), P(1), P(2), \dots$ with $S_n$ acting on $P(n)$, a unit in $P(1)$, and a substitution composition $P(k) \times P(n_1) \times \cdots \times P(n_k) \to P(n_1 + \cdots + n_k)$ — equivalently a monoid in symmetric sequences under the substitution product (HC3). The generalized framework recovers the *non-symmetric* operads exactly, via $T = (-)^{*}$, because the list monad keeps inputs in a fixed order and is cartesian, whereas the symmetric operad's order-forgetting is precisely the failure of cartesianness for the free-commutative-monoid monad. So the bridge is sharp: this chapter delivers plain operads cleanly and tells you *why* symmetric operads need extra structure — the symmetry destroys the pullbacks the framework runs on.

3. **Globular operads and the Batanin–Leinster definition of weak ω-categories — the $T = \mathbb{T}$ ceiling.** The free-strict-$\omega$-category monad $\mathbb{T}$ on globular sets is cartesian, and its operations are the **globular pasting diagrams** — the formal shapes in which higher cells can be composed. A **globular operad** is a $\mathbb{T}$-operad: a globular set $P$ with a cartesian map $P \to \mathbb{T}1$ assigning each operation its pasting-diagram shape, plus operadic unit and composition. Its algebras are "weak higher categories of that signature", and the Batanin–Leinster weak $\omega$-category is an algebra for the initial *contractible* globular operad — the one supplying just enough chosen composites and coherence cells. This chapter is the prerequisite machinery: cartesianness of $\mathbb{T}$ (HC7) is exactly the §1 condition, and the globular operad is exactly the §2 definition with $T = \mathbb{T}$. The summit of higher category theory is one row of this table.

4. **fc-multicategories, double categories, and the four-way subsumption.** Taking $T$ to be the **free-category monad** $fc$ on directed graphs produces $fc$-multicategories (HC5): structures with objects, vertical 1-cells, horizontal 1-cells, and 2-cells whose boundary is a *string* of horizontal cells along the top and a single one along the bottom. By selectively forgetting cell types one recovers bicategories (one object, only the 2-cells), monoidal categories (one object, one horizontal type), plain multicategories (collapse the verticals), and weak double categories (keep all four). The bridge is that "which composites are allowed" — single arrows, lists, trees, strings — is governed entirely by which cartesian monad you feed in, so a single definition, instantiated four ways, organizes a zoo of two-dimensional structures that otherwise look unrelated.

---

# Insights

**The unifying frame: a generalized multicategory is a category whose arrows can have $T$-shaped sources.** The whole chapter is the realization that the definition of a category contains exactly one place where you could imagine putting "something other than a single object", and that place is the domain of an arrow. A category insists an arrow goes *object $\to$ object*. Loosen this to *$T$-shape-of-objects $\to$ object*, and you must specify what a $T$-shape is and how shapes compose — but that is precisely the data of a monad, and the requirement that composition be definable over pullbacks is precisely cartesianness. Everything else — identities, associativity, the algebras — is dragged along unchanged. Once you see categories as "$\mathrm{id}$-multicategories", multicategories as "$(-)^{*}$-multicategories", and globular operads as "$\mathbb{T}$-operads", you stop learning these as separate definitions and start instantiating one definition. The frame answers the question "what is the common generalization?" with a single parameter: the monad.

**The true name of a cartesian monad is "a monad whose operations form a well-behaved family of arities".** The official definition — preserves pullbacks, cartesian unit and multiplication — is the right thing to *check* but the wrong thing to *picture*. The operational meaning, made precise by the Carboni–Johnstone characterization, is that $T X$ is a *coproduct of representables*, $T X \cong \coprod_i \mathcal{E}(C_i, X)$: the monad's action is "choose an arity $i$ from a fixed family, then choose how to fill it from $X$". The free-monoid monad is cartesian because its arities are the finite ordinals — a clean, rigid family with no internal symmetry. The free-commutative-monoid monad fails because quotienting by $S_n$ collapses the family and the arities stop being rigid. So when you read "cartesian", do not picture pullback squares — picture a tidy catalogue of arities, each of which can be filled freely. That picture predicts cartesianness faster than the squares do.

**Symmetry is the enemy of cartesianness, and that single fact carves the subject in two.** It is striking that the most natural-seeming monads — multisets, commutative monoids, the symmetric algebra — are exactly the ones excluded from this framework, while the slightly more rigid "ordered list" monad sails through. The reason is structural: a pullback distinguishes configurations that a symmetric quotient deliberately identifies, so the moment you impose a group action that forgets order, a multiplication square stops being a pullback. This is why higher category theory built on cartesian monads (Batanin, Leinster) is *globular and non-symmetric*, while the symmetric world (symmetric operads, $E_\infty$-structures, the little-disks operads) needs a genuinely different technology. Recognizing "is there a symmetry being quotiented?" is the fastest diagnostic for whether a structure lives inside this chapter or outside it.

**The framework is thin on purpose so that all the content lives in the monad.** A recurring surprise for newcomers is how little the definition of a $T$-multicategory says: it is just a monoid in a bicategory of spans. There is no list of higher coherences, no case analysis by dimension, no special handling of degeneracies. This thinness is the design, not a deficiency. By concentrating every structural choice into the single object $T$ and the single property "cartesian", the framework makes the *comparison* of higher-categorical structures tractable: two structures differ exactly insofar as their monads differ. The trigger-reaction pattern is therefore "see a higher structure $\rightsquigarrow$ ask which cartesian monad generates it", and once you can answer, you inherit free constructions, algebras, and slicing without proving anything new — the generic theorems of the framework apply to every row of the table at once.
