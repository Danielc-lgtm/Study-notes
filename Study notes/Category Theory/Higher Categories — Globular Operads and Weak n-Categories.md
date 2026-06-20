---
type: topic
subject: higher-categories
chapter: "HC7 / Leinster 8–9"
title: "Higher Categories — Globular Operads and Weak n-Categories"
tags: [category-theory, higher-categories, foundations]
---

# Notation Registry

**Standing convention.** Throughout this chapter "category" means *strict* category unless qualified, and "$\omega$-category" means a globular higher category of unbounded dimension. We work over **globular sets** — presheaves on the globe category — and *all* higher-categorical structure is encoded by operations sitting over **pasting diagrams**. The single most important convention to fix in working memory: a globular operad's operations are indexed not by a number (an arity) but by a *pasting diagram* (a shape), and "weak" enters the theory in exactly one place — by enlarging the operad of operations from the rigid terminal one to the contractible initial one. Two pages this chapter constantly references, **Def - Globular Set** and **Def - Strict n-Category and Strict ω-Category**, belong to an earlier chapter not yet in the vault, so they appear here in bold rather than as wikilinks; everything they supply is restated where needed.

- $\mathbb{G}$ — the **globe category**: objects $[0], [1], [2], \dots$; parallel arrows $\sigma, \tau : [n] \to [n+1]$ with $\sigma\sigma = \tau\sigma$, $\sigma\tau = \tau\tau$
- **globular set** $X$ — a presheaf $X : \mathbb{G}^{op} \to \mathbf{Set}$; sets $X(n)$ of $n$-cells with source/target $s, t : X(n+1) \to X(n)$, $ss = ts$, $st = tt$
- $[\mathbb{G}^{op}, \mathbf{Set}]$ — the category of globular sets
- $(T, \eta, \mu)$ — the **free strict $\omega$-category monad** on globular sets; cartesian
- $T1 = \mathrm{pd}$ — the globular set of **pasting diagrams**; $\mathrm{pd}(m)$ the $m$-dimensional ones
- $\partial : \mathrm{pd}(m+1) \to \mathrm{pd}(m)$ — the **boundary** operator (the common source/target on $1$)
- $(-)^{\ast}$ — the free-monoid (finite-list) functor on $\mathbf{Set}$; $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$
- $P \xrightarrow{d} T1$ — a **collection**; $P(\pi) = d^{-1}(\pi)$ the **fibre**, the operations of shape $\pi$
- $\theta, \phi, \psi$ — operations of a globular operad; $\theta \circ (\phi_x)$ — operadic composite; $1_\pi$ — unit operation of shape $\pi$
- $1$ — the **terminal globular operad** (one operation per shape); its algebras are strict $\omega$-categories
- $\mathrm{Par}_P(\pi)$ — parallel pairs $(\alpha^-, \alpha^+)$ of operations over $\partial\pi$; $(s,t) : P(\pi) \to \mathrm{Par}_P(\pi)$ the source-target pairing
- $\chi$ — a **contraction**; $\chi_\pi : \mathrm{Par}_P(\pi) \to P(\pi)$ its components
- $\mathbf{OC}$ — the category of globular **operads-with-contraction**; $(L, \chi)$ — its initial object, the **Batanin–Leinster operad**
- $\mathrm{Alg}(P)$ — the category of algebras for a globular operad $P$ (algebras for the induced monad $T_P$)
- $\mathbf{Wk\text{-}\omega\text{-}Cat} = \mathrm{Alg}(L)$ — weak $\omega$-categories; $\mathbf{Wk\text{-}n\text{-}Cat} = \mathrm{Alg}(L_n)$ — weak $n$-categories
- $T^{(n)}$ — free strict $n$-category monad on $n$-globular sets; $L_n$ — initial $n$-operad-with-contraction
- $\mathbf{UBicat}_{str}$ — unbiased bicategories with unbiased strict functors; $\mathrm{tr}(k)$ — $k$-leafed trees

---

# Motivation

Here is the entire chapter in one sentence: a weak $\omega$-category is an algebra for the initial contractible globular operad. Every word in that sentence is a definition this chapter builds, and the payoff is that the most coherence-laden object in mathematics — a higher category in which composition is associative, unital, and interchanging only up to an infinite tower of coherent higher cells — is captured by a single, finite, conceptual phrase.

The problem this chapter solves is the central problem of higher category theory: *how do you define a weak $n$-category, let alone a weak $\omega$-category, without writing down infinitely many coherence axioms?* The naive route writes the coherence data by hand. In dimension $2$ this gives Bénabou's bicategory: associators and unitors, plus the pentagon and triangle axioms. In dimension $3$ it gives the tricategory of Gordon–Power–Street, whose definition runs for pages and whose coherence axioms already strain human verification. In dimension $4$ the hand-written approach has essentially never been completed. And $\omega$ is hopeless by this method — there is no end to the axioms. So a different idea is needed: a *uniform mechanism* that generates the entire coherence tower from a single principle, in every dimension at once.

The Batanin–Leinster answer rests on a structural observation that, once seen, is hard to unsee: **weak composition and coherence are the same phenomenon — a chosen lift of a parallel pair against a boundary, one dimension up.** An associator is a $2$-cell from $(hg)f$ to $h(gf)$; both bracketings are parallel $1$-dimensional composites, and the associator is a filler between them. The pentagon equation is, in turn, witnessed by a $3$-cell filling between two parallel composites of associators; and so on forever. A single closure condition — "every parallel pair of operations lifts to a cell one dimension up" — therefore generates associators, the pentagon, the pentagon's coherence, and the whole infinite tower automatically. That condition is a **contraction**, and the operad freely generated by it is the Batanin–Leinster operad $L$.

The architecture of the chapter is a three-step backbone, and it is worth holding as a single picture:
$$
\textbf{free strict $\omega$-category monad } T \;\rightsquigarrow\; \textbf{globular operad } P \xrightarrow{d} T1 \;\rightsquigarrow\; \textbf{contraction } \chi \text{ on } P \;\rightsquigarrow\; \textbf{weak $\omega$-category} = L\text{-algebra}.
$$
Section §1 builds $T$ and proves the one fact everything depends on — that $T$ is *cartesian*, with operations the pasting diagrams. Section §2 defines a **globular operad** as a $T$-operad: a collection of abstract composition operations indexed by pasting shapes, with substitution. Section §3 adds the **contraction** that injects weakness and coherence, takes the initial such operad $L$, and *defines* a weak $\omega$-category as an $L$-algebra — then validates the definition by proving its dimension-$2$ instances are exactly bicategories.

This chapter is the culmination of the higher-operads programme (Leinster Chapters 8–9), and it assumes you have met the surrounding machinery. You should have refreshed: **globular sets** and **strict $\omega$-categories** (the substrate and the rigid model), [[Def - Monad and Comonad|monads]] and [[Def - Algebra for a Monad|their algebras]] (the language of $T$ and of $P$-algebras), the idea of a **cartesian monad** and of a **generalized operad** / **$T$-operad** (the framework, from the preceding chapter), [[Def - Pullback and Pushout|pullbacks]] (cartesianness is stated with them), and classical **operads** and **multicategories** (the prototype this generalizes). A reader who knows what a [[Def - 2-Category and Bicategory|bicategory]] is will find §3 anchored by the theorem that weak $2$-categories *are* bicategories. The reward for the climb is a definition of weak higher category that fits on one line and works in every dimension.

---

# Concept Map

## §1 The Free Strict ω-Category Monad

- **[[Def - The Free Strict ω-Category Monad]]**
	- The monad $(T, \eta, \mu)$ on **globular sets** whose algebras are the strict $\omega$-categories; equivalently $T = UF$ for the free–forgetful adjunction $F \dashv U$ with $\mathbf{Str\text{-}\omega\text{-}Cat}$. Its operations are **pasting diagrams**: $T1 = \mathrm{pd}$, with $\mathrm{pd}(0) = 1$ and $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$, so a pasting diagram is a list of lower pasting diagrams. The load-bearing theorem is that $T$ is **cartesian** ($T$ preserves pullbacks; $\eta, \mu$ have pullback naturality squares), which is exactly what licenses the globular-operad framework. The strictness is deliberate: weakness is injected later by changing the operad, not the monad.

- **[[Ex - Computing the low-dimensional pasting diagrams]]** (⭐)
	- Identify $\mathrm{pd}(0)$, $\mathrm{pd}(1) \cong \mathbb{N}$, and several elements of $\mathrm{pd}(2)$ via the recursion $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$, and compute the boundary $\partial : \mathrm{pd}(2) \to \mathrm{pd}(1)$ on examples.

- **[[Ex - The free strict omega-category monad is cartesian on a slice]]** (⭐⭐)
	- Verify, for the truncation to $1$-globular sets, that the free-category monad's unit and multiplication have pullback naturality squares, isolating why cartesianness holds dimension by dimension via the free-monoid monad.

- **[[Ex - Pasting diagrams as labelled composites]]** (⭐⭐)
	- Show that for a globular set $X$, an element of $(TX)(m)$ is a pasting diagram together with a compatible labelling of its cells by cells of $X$, and that the projection $TX \to T1$ forgets the labels.

> [!tip] Unlocked: Generalized Operads and the Cartesian-Monad Recipe *(from Higher Operads)*
> Once $T$ is known to be cartesian, the entire theory of **generalized operads** ($T$-operads) becomes available over it. The recipe "cartesian monad $T$ on a presheaf category $\rightsquigarrow$ theory of $T$-shaped higher categories" is uniform: $T = (-)^{\ast}$ gives classical **operads**, $T = \mathrm{id}$ gives **categories**, the free-category monad gives **fc-multicategories**, and this $T$ gives globular operads.

> [!tip] Unlocked: Opetopic and Cubical Higher Categories *(from Higher Category Theory)*
> Swapping the globular $T$ for the free strict $n$-tuple-category monad yields *cubical* higher categories; replacing it by the slice construction on the identity operad yields **opetopes** and the Baez–Dolan opetopic definition. The globular $T$ of this section is one corner of that landscape.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 The Free Strict ω-Category Monad]]

## §2 Globular Operads

- **[[Def - Globular Operad]]**
	- A **globular operad** is a **generalized operad** for the free strict $\omega$-category monad $T$: a collection $P \xrightarrow{d} T1$ (with $d$ cartesian) carrying associative, unital operadic composition and units. Its fibre $P(\pi)$ is the set of abstract operations of shape $\pi$ — "the ways to compose a labelled diagram of that shape". Equivalently, a globular operad is a [[Def - Monoid in a Monoidal Category|monoid]] in the substitution-product slice $([\mathbb{G}^{op},\mathbf{Set}]/T1, \otimes)$, the globular analogue of "an operad is a monoid in symmetric sequences". The terminal operad $1$ (one operation per shape) has **strict $\omega$-categories** as algebras.

- **[[Ex - Algebras for the terminal globular operad are strict omega-categories]]** (⭐⭐)
	- Show that a $P$-algebra structure for the terminal globular operad $1$ is precisely a strict $\omega$-category structure, by unwinding "one composite per labelled pasting diagram, associatively and unitally".

- **[[Ex - A globular operad map is determined by its action on operations]]** (⭐)
	- Verify that a map of globular operads is a map of collections commuting with composition and units, and that a $P$-algebra structure on $X$ is the same as a globular-operad map $P \to \mathrm{End}(X)$ into the endomorphism operad.

- **[[Ex - The substitution product and why cartesianness is needed]]** (⭐⭐⭐)
	- Construct the substitution product $\otimes$ on collections over $T1$ and show, on an explicit example, that associativity of $\otimes$ uses the cartesianness of $T$ — exhibiting a non-cartesian monad where the product fails.

> [!tip] Unlocked: Algebras as Higher-Categorical Signatures *(from Universal Algebra)*
> A globular operad is a *signature* for a flavour of $\omega$-category, and $P \mapsto \mathrm{Alg}(P)$ is functorial. This is the operadic face of universal algebra: just as a Lawvere theory's models are its algebras, a globular operad's algebras are the higher categories of its prescribed composition structure.

> [!tip] Unlocked: The Endomorphism Operad and Recognition *(from Operad Theory)*
> The **endomorphism operad** $\mathrm{End}(X)$ packages all actual operations on a globular set $X$; a $P$-algebra is a map $P \to \mathrm{End}(X)$. This is the globular analogue of May's recognition principle, where an action of an operad on a space detects the structure (e.g. an $n$-fold loop space) carried by that space.

> [!note] Exercise Index — §2
> [[Exercise Index - §2 Globular Operads]]

## §3 Contractions and Batanin–Leinster Weak ω-Categories

- **[[Def - Contraction on a Globular Operad]]**
	- A **contraction** $\chi$ on a globular operad $P$ supplies, for every pasting diagram $\pi$ and every parallel pair $(\alpha^-, \alpha^+)$ of operations over $\partial\pi$, a chosen operation $\chi_\pi(\alpha^-,\alpha^+) \in P(\pi)$ with source $\alpha^-$, target $\alpha^+$, shape $\pi$. It is a section of the source-target pairing $(s,t) : P(\pi) \to \mathrm{Par}_P(\pi)$ — the directed analogue of a [[Def - Kan Complex and the Nerve|Kan]] filling condition. The single closure "every parallel pair lifts" generates the entire infinite coherence tower: weak composites *and* associators *and* the pentagon *and* its coherences are all lifts, one dimension apart. In the finite-dimensional case, top-dimensional **tameness** forces equalities where no higher cell can defer the relation.

- **[[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)]]**
	- The category $\mathbf{OC}$ of operads-with-contraction has an initial object $(L, \chi)$, the **Batanin–Leinster operad**; a **weak $\omega$-category** is an $L$-algebra, and $\mathbf{Wk\text{-}\omega\text{-}Cat} = \mathrm{Alg}(L)$. A **weak $n$-category** is an $L_n$-algebra for the initial tame $n$-operad-with-contraction $L_n$, equivalently a weak $\omega$-category trivial above dimension $n$. The choice of $L$ is canonical because it is *freely generated* by the contraction — minimal, with no arbitrary extra operations. Strict $\omega$-categories embed (fully and faithfully) via $L \to 1$; any contractible globular set is canonically a weak $\omega$-groupoid.

- **[[Thm - The Initial Contractible Globular Operad Exists]]**
	- The category $\mathbf{OC}$ of globular operads-with-contraction has an initial object $(L, \chi)$, unique up to unique isomorphism; the finite-dimensional category $\mathbf{OC}_n$ likewise has an initial object $L_n$. The construction is a *stratified* free build: dimension $n$ is generated from the frozen dimension $n-1$ by alternately lifting parallel pairs (contraction) and forming composites (operad), with no downward feedback, so each stage closes off and the tower never stalls. Cartesianness of $T$ is what makes the ambient category $\mathbf{OC}$ well-defined.

- **[[Thm - Weak 2-Categories are Bicategories]]**
	- $\mathbf{Wk\text{-}0\text{-}Cat} \simeq \mathbf{Set}$, $\mathbf{Wk\text{-}1\text{-}Cat} \simeq \mathbf{Cat}$, and $\mathbf{Wk\text{-}2\text{-}Cat} \simeq \mathbf{UBicat}_{str}$ — so a weak $2$-category is precisely an unbiased [[Def - 2-Category and Bicategory|bicategory]], hence essentially a classical bicategory. The mechanism: in dimension $2$ the contraction supplies associators and unitors (tree-generated composites in dimension $1$), and top-dimensional tameness forces them to satisfy every coherence equation — which is exactly bicategory coherence / [[Thm - Mac Lane Coherence Theorem|Mac Lane's theorem]]. This is the validation that the definition is correct in all dimensions.

- **[[Ex - A contraction supplies the associator and unitor cells]]** (⭐⭐)
	- For the relevant low-dimensional pasting diagrams, exhibit the associator and unitor as contraction lifts $\chi_\pi(\alpha^-, \alpha^+)$, identifying $\alpha^-, \alpha^+$ as the two parallel bracketings.

- **[[Ex - Any contractible globular set is a weak omega-category]]** (⭐⭐⭐)
	- Show that if the unique map $X \to 1$ is contractible then $\mathrm{End}(X)$ admits a contraction, the unique map $L \to \mathrm{End}(X)$ is an $L$-algebra structure, and hence $X$ is canonically a weak $\omega$-category — the directed analogue of "a contractible space is an $\infty$-groupoid".

- **[[Ex - Strict omega-categories are weak omega-categories]]** (⭐⭐)
	- Using the unique map $L \to 1$ and contractibility of $L$, show the induced functor $\mathbf{Str\text{-}\omega\text{-}Cat} \to \mathbf{Wk\text{-}\omega\text{-}Cat}$ is full and faithful, so strict $\omega$-categories are exactly the weak ones with identity coherence cells.

- **[[Ex - Why finite-dimensional contractions need tameness]]** (⭐⭐⭐)
	- Exhibit a precontractible $n$-operad that is not contractible (its top-dimensional source-target pairing is not injective) and explain why the missing dimension $n+1$ forces the tameness condition.

> [!tip] Unlocked: The Homotopy Hypothesis and Grothendieck ∞-Groupoids *(from Higher Category Theory)*
> Restricting to invertible cells, weak $\omega$-**groupoids** should be equivalent to topological spaces — Grothendieck's **homotopy hypothesis**. The **Grothendieck–Maltsiniotis** definition via *coherators* is a close relative of "operad-with-contraction"; that a contractible globular set is a weak $\omega$-category is the algebraic mirror of "a contractible space is an $\infty$-groupoid".

> [!tip] Unlocked: The Comparison Problem for Models of (∞,1)-Categories *(from Higher Category Theory)*
> The algebraic definition here sits opposite the geometric ones — [[Def - Quasi-Category|quasi-categories]], Segal categories, complete Segal spaces. For $(\infty,1)$-categories the **Bergner–Joyal–Lurie** comparison proves all these models equivalent (via Quillen equivalences of [[Def - Model Category|model categories]]); for general weak $\omega$-categories the comparison is largely open.

> [!tip] Unlocked: Coherence for Tricategories and the Periodic Table *(from Higher Operads)*
> The $n=2$ validation points to $n=3$: a weak $3$-category should be a **tricategory**, with strictification to **Gray-categories**. One object up the dimensions, the equivalences here form the bottom row of the **Baez–Dolan periodic table** of $k$-tuply monoidal $n$-categories, where Eckmann–Hilton stabilization is made precise.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 Contractions and Batanin-Leinster Weak ω-Categories]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The proofs in this chapter cluster around a small number of recurring goals. The most frequent is **cartesianness**: showing a monad preserves pullbacks and has cartesian unit and multiplication, because cartesianness is the gateway to the entire operad framework — without it there is no substitution product, no fibres, no operad. A second target is **existence of a free/initial object**: the operad $L$, the initial operad-with-contraction, is the object the whole definition rests on, and proving it exists (by a stratified construction that converges) is the chapter's central theorem. A third is **identification of algebras**: given an operad $P$, determine $\mathrm{Alg}(P)$ — that algebras for the terminal operad are strict $\omega$-categories, that algebras for $L_2$ are bicategories. A fourth is **comparison/equivalence of doctrines**: showing two routes to the same higher-categorical notion (operadic vs. explicit, biased vs. unbiased, weak-$n$-category vs. bicategory) agree, validating the abstract definition against the known. A fifth is **reduction to the known in low dimensions**: confirming the machine outputs $\mathbf{Set}$, $\mathbf{Cat}$, $\mathbf{Bicat}$ in dimensions $0, 1, 2$. These five — cartesianness, initial-object existence, algebra identification, doctrine comparison, low-dimensional reduction — recur because each is a way of pinning the abstract definition to something concrete and checkable.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **The monad $T$ is cartesian** — this is the richest source, because it instantly supplies the substitution product, the notion of collection, and the operad axioms; nearly every construction begins "since $T$ is cartesian...". **An operad carries a contraction** — the moment a globular operad is contractible, every parallel pair lifts, so weak composites and coherence cells exist on demand; this is the source that converts "we have an operad" into "we have a weak higher category". **An object is initial (or terminal) in a category of structured operads** — initiality gives a unique structure-preserving map *out*, which (composed with functoriality of $\mathrm{Alg}$) re-expresses any contractible operad's algebras as weak $\omega$-categories. **A structure is tree-generated** — knowing that an operad is generated by the operad of trees (because the contraction is unbiased and trees are the unbiased composites) reduces an abstract comparison to a finite, explicit one. **Tameness holds in the top dimension** — in the finite case this forces top-dimensional coherences to be equalities, which is exactly classical coherence. The recurring move is to route a source to a target: cartesianness routes to the operad framework; a contraction plus initiality routes to "an $L$-algebra"; tree-generation plus tameness routes to a low-dimensional identification. The [[Higher Categories — Globular Operads and Weak n-Categories#Problem-Solving Strategy|Problem-Solving Strategy]] section makes these routes explicit.

---

# Legal Operations

These are the moves nearly every construction and proof in this chapter is assembled from. When stuck, scan the list. Everything is self-contained: a reader with only the language of monads and operads should follow each from the description alone.

**Legal operations:**

1. **Replace a higher-categorical structure by an operad-over-$T1$.** The foundational move: instead of writing composition operations and coherence axioms by hand, encode them as the fibres $P(\pi)$ of a [[Def - Globular Operad|globular operad]] $P \xrightarrow{d} T1$, with the operad axioms doing the bookkeeping. *Trigger:* you face a definition that would otherwise require infinitely many coherence axioms. *Pattern:* "let $P(\pi)$ be the operations of shape $\pi$; let an algebra perform them."

2. **Use cartesianness to form the substitution product and the fibres.** Because $T$ is a [[Def - The Free Strict ω-Category Monad|cartesian monad]], the slice over $T1$ has an associative substitution product $\otimes$, and every collection has well-defined fibres $P(\pi) = d^{-1}(\pi)$. *Trigger:* you need to compose operations or speak of "operations of shape $\pi$". *Pattern:* "by cartesianness, the relevant square is a pullback, so the substitution/fibre is well-defined."

3. **Lift a parallel pair to a coherence cell via a contraction.** Given a [[Def - Contraction on a Globular Operad|contraction]] $\chi$ and a parallel pair $(\alpha^-, \alpha^+)$ over $\partial\pi$, produce the cell $\chi_\pi(\alpha^-, \alpha^+) \in P(\pi)$. *Trigger:* you want an associator, unitor, interchanger, or any coherence cell. *Pattern:* "the two competing composites are parallel over the boundary; lift them to a coherence cell one dimension up."

4. **Take the initial object of a category of structured operads.** To get a canonical operad with prescribed extra structure (a contraction, a system of compositions), form the *initial* such operad — freely generated, minimal, with a unique structure-preserving map to every other. *Trigger:* you want "the" canonical operad of a given flavour. *Pattern:* "let $L$ be initial in $\mathbf{OC}$; then for any $(P,\chi')$ there is a unique map $L \to P$."

5. **Build a free higher structure by stratified (dimension-by-dimension) closure.** Construct an operad-with-extra-structure by induction on dimension, alternating closure under operations and under lifts, using that lower dimensions are frozen so closures do not feed back down. *Trigger:* you must prove a free/initial operad-with-structure exists. *Pattern:* "assume built up to dimension $n-1$; close dimension $n$ under contraction then composition; repeat; no downward feedback, so it converges."

6. **Identify an operad's algebras by unwinding the action.** To compute $\mathrm{Alg}(P)$, unwind a $P$-algebra structure on $X$ as "a chosen composite for each operation, labelling, and shape", then recognize the result as a known structure. *Trigger:* you want to know what $P$-algebras *are*. *Pattern:* "$P$-algebra $=$ map $P \to \mathrm{End}(X)$ $=$ [recognized structure]."

7. **Transport a comparison through monad/operad embeddings.** Replace a hard high-dimensional comparison by an equivalent low-dimensional one using embeddings like "plain operad $=$ one-object $fc$-operad" or "$1$-globular operad $=$ $fc$-operad". *Trigger:* a $2$-dimensional doctrine comparison. *Pattern:* "descend to plain operads of trees; compare there; lift back."

8. **Enforce tameness to strictify the top dimension.** In the finite-dimensional case, demand the top-dimensional source-target pairing be injective, forcing top coherences to be equalities. *Trigger:* defining a weak $n$-category, or recovering classical coherence. *Pattern:* "no dimension $n+1$ to defer to, so parallel top cells with equal image are equal."

9. **Pull a structure back along an operad map.** Given an operad map $f : P \to Q$ and a $Q$-algebra, restrict along $f$ to get a $P$-algebra; dually transport a contraction. *Trigger:* you have structure on one operad and want it on another. *Pattern:* "$f^\ast$ restricts the action; $f$ initial $\implies$ everything maps to $\mathbf{Wk\text{-}\omega\text{-}Cat}$."

**Illegal but tempting operations:**

> [!warning] 1. Defining a globular operad from a non-cartesian map $d : P \to T1$
> It is tempting to call any collection $P \xrightarrow{d} T1$ with a composition an operad. But if $d$ is not **cartesian**, the substitution product $\otimes$ on collections is not associative — composites can land in the wrong fibre, and the operad axioms cannot even be stated. The free *commutative*-monoid monad shows the failure mode in miniature: it is not cartesian (forgetting order breaks the pullback), so there is no good "commutative-monoid operad" theory by this route. The operation becomes legal exactly when $d$ is cartesian — which for operations *over* the cartesian monad $T$ is the defining requirement.

> [!warning] 2. Taking algebras supported in dimensions $\leq n$ and calling them weak $n$-categories
> One would like a weak $n$-category to be just an $L$-algebra concentrated in low dimensions. This is correct *below* the top dimension but wrong *at* it: in dimension $n$ there is no dimension $n+1$ to receive deferred coherence cells, so two parallel $n$-fold composites that should be coherently equal would remain distinct. The concrete failure is a "weak $3$-category" with two distinct parallel $3$-cells over the same boundary that ought to be equal. The fix is **tameness**: the definition uses the initial *tame* $n$-operad-with-contraction $L_n$, forcing equalities in the top dimension. Without tameness you get a precontractible-but-not-contractible structure, a different and worse object.

> [!warning] 3. Concluding weak $2$-categories are biased bicategories under weak functors
> From $\mathbf{Wk\text{-}2\text{-}Cat} \simeq \mathbf{UBicat}_{str}$ it is tempting to read off "weak $2$-category $=$ bicategory" outright. But the maps in $\mathbf{Wk\text{-}2\text{-}Cat}$ are *strict*, so the equivalence is with **unbiased** bicategories and **strict** functors, and $\mathbf{UBicat}_{str}$ is *not* equivalent to classical bicategories under their usual weak functors (the obvious comparison functor is not an equivalence). The counterexample is at the level of morphisms: weak functors of bicategories are not unbiased strict functors. The statement becomes legitimate only after combining with the *separate* biased-equals-unbiased coherence result, and even then the morphism match awaits a definition of weak $2$-functor.

> [!warning] 4. Treating a contraction as supplying *unique* lifts
> Picturing the contraction as choosing the *unique* filler of each parallel pair conflates the weak and strict theories. In the infinite-dimensional case lifts must merely *exist* (the source-target pairing is surjective, not bijective); demanding uniqueness would force the lifted coherence cells to be equalities one dimension down, collapsing weakness back to strictness. Uniqueness *is* correct in exactly one place — the top dimension of an $n$-category, where tameness makes the pairing bijective — but imposing it everywhere destroys the very weakness the contraction was introduced to provide.

---

# Problem-Solving Strategy

The constructions in this chapter are won or lost at the moment you decide *which layer of the backbone* — monad, operad, or contraction — your problem lives in. Almost everything is one of a few types, and each has a characteristic assumption pattern and route.

If the problem **asks you to justify the operad framework itself** — to show a monad supports a theory of operads, or that fibres and substitution are well-defined — then you are in a *cartesianness* problem, and your primary instrument is the cartesian-monad machinery. The route is always the same: exhibit the naturality squares of $\eta$ and $\mu$ as [[Def - Pullback and Pushout|pullbacks]] and show $T$ preserves pullbacks, often by reducing to the free-monoid monad dimension by dimension via $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$. Once cartesianness is in hand, the substitution product, the fibres $P(\pi)$, and the operad axioms all come for free, and you never reprove them. The trigger is any phrase like "operations of shape $\pi$" or "compose these operations" — both presuppose cartesianness.

If the problem **asks what some operad's algebras are** — to identify $\mathrm{Alg}(P)$ for a concrete $P$ — then the assumption pattern is that you have an explicit operad and the route runs through *unwinding the action and recognizing the result*. The single most useful identity is "a $P$-algebra structure on $X$ is a globular-operad map $P \to \mathrm{End}(X)$", which converts an opaque "$X$ is a $P$-algebra" into a concrete "$X$ has these operations, composing thus". For the terminal operad this unwinds to a strict $\omega$-category; for $L_2$ it unwinds (after identifying $L_2$ as tree-generated) to a bicategory. The difficulty is concentrated in *recognizing* the unwound structure as a familiar one, so keep the catalogue of known doctrines (sets, categories, bicategories, monoidal categories) at hand and match against it.

If the problem **asks you to produce a canonical operad with prescribed structure** — most often "the operad for weak $\omega$-categories" — then the route is *initiality plus stratified construction*. You do not write the operad down explicitly; you characterise it by a universal property (initial in $\mathbf{OC}$) and prove it exists by the dimension-by-dimension free build, alternating contraction-closure and operad-closure. The reason this works is the absence of downward feedback: an $n$-operation's source and target live in the frozen dimension $n-1$, so building dimension $n$ never disturbs what is below, and the construction converges. The trigger is "the canonical / freely-generated / initial operad of flavour $X$".

If the problem **asks you to validate the definition against a known case** — to show weak $n$-categories for small $n$ are the expected sets/categories/bicategories — then the route is *compute the small operad explicitly, identify it as tree-generated, and match algebras*. Here two facts do the heavy lifting: the contraction forces the $1$-dimensional operations to be the trees (the unbiased composites), and top-dimensional **tameness** forces the next dimension to be determined by the parallel pairs below. The comparison then reduces to matching two tree-generated operads, which is a finite check (Leinster 9.4.2). The trigger is "show $\mathbf{Wk\text{-}n\text{-}Cat} \simeq \ldots$" for explicit small $n$.

Finally, a meta-strategy threads through all of the above, and it is the single unifying question of the chapter: **every question here is the question "how is weakness injected, and where does coherence come from?"** The answer never changes — weakness and coherence both come from the contraction's lifts of parallel pairs, with the operad $L$ the free repository of those lifts and the cartesian monad $T$ the substrate. When a construction confuses you, locate where in the backbone $T \rightsquigarrow P \rightsquigarrow \chi \rightsquigarrow L\text{-algebra}$ it sits, and ask what the contraction is supplying there. The reason this question is always worth asking is that it cannot mislead: the entire definition is engineered so that *all* of weak composition and *all* of coherence funnel through the one mechanism of lifting a parallel pair one dimension up.

---

# Most Reusable Properties

- **[[Def - The Free Strict ω-Category Monad|Cartesianness of the monad]]**: $T$ preserves pullbacks and $\eta, \mu$ have pullback naturality squares. This is the most-used single fact in the chapter because it is *free infrastructure*: it costs nothing once proved and is invoked the instant any operad-theoretic construction begins. Reach for it whenever you form a substitution product, speak of fibres $P(\pi)$, or state an operad axiom. Its most powerful disguised use is *transfer*: any cartesian monad on a presheaf category supports the same operad theory, so a single proof exports to cubical, opetopic, and $n$-tuple-category variants.

- **[[Def - Globular Operad|The identity "algebra equals map into the endomorphism operad"]]** ($P$-algebra $=$ globular-operad map $P \to \mathrm{End}(X)$): a $P$-algebra structure on a globular set $X$ is exactly a globular-operad map into the endomorphism operad. This is the workhorse for *identification*. The recognizable setup is "what are the algebras of this operad?" — and this identity converts it to "what structure does a map into $\mathrm{End}(X)$ carry?", which is concrete. It is also the engine behind "any contractible globular set is a weak $\omega$-category": build a contraction into $\mathrm{End}(X)$, then map $L$ in.

- **[[Def - Contraction on a Globular Operad|The contraction as a section of the source-target pairing]]**: a contraction is a coherent choice of one-sided inverse to every source-target pairing $(s,t) : P(\pi) \to \mathrm{Par}_P(\pi)$. The reusable move is the equivalence itself — to *produce* coherence cells, supply a contraction; to *use* contractibility, remember $(s,t)$ is surjective so every parallel pair has a lift. Its highest-leverage consequence is that weak composition and coherence are unified: both are lifts, so one mechanism handles both. **Typical use:** whenever a proof needs an associator or any higher coherence, write it as a contraction lift.

- **[[Thm - The Initial Contractible Globular Operad Exists|Initiality of the Batanin–Leinster operad]]**: $(L, \chi)$ is initial in $\mathbf{OC}$, so there is a *unique* contraction-preserving map $L \to P$ for every operad-with-contraction $P$. Its typical use is in *transport*: combined with functoriality of $\mathrm{Alg}$, the unique map $L \to P$ gives a canonical functor $\mathrm{Alg}(P) \to \mathbf{Wk\text{-}\omega\text{-}Cat}$, so every contractible operad's algebras become weak $\omega$-categories. It is also what makes "weak $\omega$-category" a *canonical* notion rather than one of many, since $L$ is determined up to unique isomorphism.

- **[[Thm - Weak 2-Categories are Bicategories|Top-dimensional tameness = coherence]]**: in dimension $n$ of a weak $n$-category, tameness forces the source-target pairing to be a bijection, equating parallel top cells. **Typical use:** recognizing classical coherence theorems (bicategory coherence, [[Thm - Mac Lane Coherence Theorem|Mac Lane]]) as instances of tameness, and computing $L_n$'s top dimension as exactly the set of parallel pairs below — which collapses an infinite construction to a finite description and drives every low-dimensional identification.

---

# Bridges

1. **Classical operad theory — globular operads are the globular member of the cartesian-monad family.** A classical (non-symmetric) **operad** is a sequence of sets $P(n)$ of $n$-ary operations with a substitution composition $P(k) \times P(n_1) \times \cdots \times P(n_k) \to P(n_1 + \cdots + n_k)$ and a unit; its algebras (via maps $P(n) \to \mathrm{Hom}(X^n, X)$) are the structures of a given signature, e.g. monoids for the associative operad, commutative monoids for the commutative operad. A globular operad is the *same construction* with "arity $n$" replaced by "pasting-diagram shape $\pi$" and substitution following the geometry of pasting rather than the linear order of inputs. Both are monoids for a substitution product, and both substitution products come from a [[Def - The Free Strict ω-Category Monad|cartesian monad]] — $(-)^{\ast}$ on sets for classical operads, $T$ on globular sets here. The globular case has no symmetric-group actions precisely because pasting diagrams, unlike $n$-tuples of inputs, have no permutation symmetry.

2. **Simplicial homotopy theory — contraction is the algebraic twin of the Kan filling condition.** A [[Def - Kan Complex and the Nerve|Kan complex]] is a [[Def - Simplicial Set|simplicial set]] in which every horn $\Lambda^n_k \to X$ admits a filler $\Delta^n \to X$; this "fillers exist" condition makes $X$ model a homotopy type with composition defined only up to contractible choice. A contraction on a globular operad is the same philosophy made *algebraic* and *directed*: where a Kan complex merely *has* fillers (a property), a contraction *chooses* them (structure), and where horns are filled, parallel boundary pairs are lifted. This is exactly the divide between the geometric/non-algebraic definitions of higher category ([[Def - Quasi-Category|quasi-categories]], Segal spaces) and the algebraic ones (Batanin, Leinster): fillers-as-property versus fillers-as-chosen-structure. The fact that a contractible globular *set* is a weak $\omega$-groupoid is the directed shadow of "a contractible space is an $\infty$-groupoid".

3. **The homotopy hypothesis — weak $\omega$-groupoids and topological spaces.** Restricting all the machinery of this chapter to *invertible* cells gives weak $\omega$-**groupoids**, and Grothendieck's homotopy hypothesis conjectures these are equivalent to topological spaces / homotopy types. The bridge is concrete: the **Grothendieck–Maltsiniotis** definition of $\infty$-groupoid replaces "operad-with-contraction" by a *coherator* (a globular theory freely generated by "all admissible operations and coherences exist"), and the initial coherator is built by the *same* stratified free construction that produces $L$. The [[Def - Higher Homotopy Group|homotopy groups]] $\pi_n(X)$ of a space and the cells of its fundamental $\omega$-groupoid are two descriptions of one object; this chapter supplies the algebraic side.

4. **Coherence theory — tameness as a uniform coherence theorem.** Classical coherence theorems — [[Thm - Mac Lane Coherence Theorem|Mac Lane's]] for monoidal categories, the pentagon/triangle coherence for [[Def - 2-Category and Bicategory|bicategories]] — are usually proved by intricate rewriting arguments showing "all diagrams of constraint cells commute". This chapter recasts them structurally: in the top dimension of a weak $n$-category, **tameness** forces the source-target pairing to be injective, so any two parallel coherence cells with equal boundary are *equal* — which is precisely "all coherence diagrams commute". So coherence is not proved case by case; it is a single condition (tameness) that the finite-dimensional definition builds in, and [[Thm - Weak 2-Categories are Bicategories|the weak 2-category theorem]] exhibits Mac Lane coherence as its one-object dimension-$2$ instance.

---

# Insights

**The unifying frame: weakness and coherence are one phenomenon, the lift of a parallel pair.** It is tempting to think of weak composition (associativity up to iso) and coherence (the pentagon, the triangle, and their towers) as two separate problems — first define the weak composites, then impose coherence among them. The Batanin–Leinster insight, and the thing this chapter is built to install, is that they are the *same* problem. An associator is a cell filling between two parallel composites; the pentagon is a cell filling between two parallel composites of associators; the pentagon's coherence is a cell filling between two parallel composites of those, and so on forever. Every one is a lift of a parallel pair, one dimension up. So the single condition "all parallel pairs lift" — a contraction — generates the entire infinite coherence tower from one closure, and the operad $L$ is nothing but the free repository of those lifts. Whenever a coherence question arises, the move is the same: find the parallel pair, lift it.

**The true name of "weak $\omega$-category" is "$L$-algebra", and the true name of $L$ is "the free oriented-contractible operad".** The official definition — a globular set carrying an action of the initial operad-with-contraction — is the right thing to *state* but the wrong thing to *picture*. Operationally, a weak $\omega$-category is a globular set in which you can compose any pasteable diagram, in coherently-many ways, with every coherence cell present; and $L$ is the directed, operadic analogue of the free contractible space on a point. When you reason about a weak $\omega$-category, do not unwind the $L$-action; picture "I can compose anything, associativity and units hold up to coherent isomorphism, and the isomorphisms themselves cohere all the way up". The strict case is the degenerate one where the coherences are identities.

**Strictness is the firm ground; weakness is one controlled perturbation.** A recurring temptation in higher category theory is to build weakness into the foundations — to make the base monad itself weak, the composites themselves only-defined-up-to-iso. Batanin and Leinster do the opposite, and it is the source of the theory's tractability: the base monad $T$ is *strict* (its algebras are strict $\omega$-categories, which are easy and cartesian), and weakness is injected at exactly one later point, by replacing the rigid terminal operad $1$ over $T1$ with the contractible initial operad $L$ over the *same* $T1$. Everything hard about coherence is thereby quarantined into the single object $L$, and everything about the substrate stays strict and computable. This "keep the base strict, perturb the operad" pattern is why the definition fits on one line where the explicit definitions do not, and it is a transferable design principle: when a structure threatens to drown in coherence, look for a strict substrate to perturb rather than a weak one to wrestle.

**Tameness reveals coherence theorems as a dimensional accident.** The classical coherence theorems look like deep, hard-won facts about monoidal categories and bicategories. From the operadic vantage they are something humbler and more illuminating: a consequence of running out of room. In a weak $\omega$-category every coherence can be *deferred* to the next dimension — the associativity of associators lives one floor up, indefinitely. In a weak $n$-category the top floor has no floor above it, so the coherences there cannot be deferred and must instead become *equalities* — this is tameness. "All diagrams commute" is therefore not a theorem about the cleverness of monoidal coherence; it is the statement that, with nowhere left to defer to, the highest coherences collapse to equations. The infinite-dimensional theory is in this sense *simpler* than the finite-dimensional one, because it never has to face a top dimension.
