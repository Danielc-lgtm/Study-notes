---
type: definition
subject: higher-categories
prereqs:
  - "Def - The Free Strict ω-Category Monad"
  - "Def - Monad and Comonad"
  - "Def - Pullback and Pushout"
  - "Def - Algebra for a Monad"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Let $(T, \eta, \mu)$ be the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] on the category $[\mathbb{G}^{op}, \mathbf{Set}]$ of **globular sets**, and write $T1 = \mathrm{pd}$ for the globular set of **pasting diagrams**, with $\mathrm{pd}(m)$ the set of $m$-dimensional pasting diagrams and $\partial : \mathrm{pd}(m+1) \to \mathrm{pd}(m)$ the boundary. A **collection** is a globular set $P$ equipped with a map $d : P \to T1$; the **fibre** over a pasting diagram $\pi \in \mathrm{pd}(m)$ is written $P(\pi) = d^{-1}(\pi) \subseteq P(m)$, the set of **operations of shape $\pi$**. I write $1$ for the terminal globular set (one cell in each dimension), which is also the terminal globular operad. For operations I use Greek letters $\theta, \phi, \psi$; the operadic composite of $\theta$ with a family $(\phi_i)$ is written $\theta \circ (\phi_1, \dots, \phi_k)$ or $\theta(\phi_1, \dots, \phi_k)$, and the unit operation of shape $\pi$ is $1_\pi$. The full symbol registry is on [[Higher Categories — Globular Operads and Weak n-Categories]].

The terms **generalized operad** (alias **$T$-operad**), **generalized multicategory**, **operad**, **multicategory**, and **strict ω-category** refer to constructions whose dedicated pages are not yet in the vault; they appear in bold and are restated here as needed.

---

# Axiom Motivation

The question this definition answers is sharp: *what is the algebraic theory whose models are "higher categories with a prescribed system of composition operations"?* A strict $\omega$-category is the answer for one specific, maximally rigid choice of operations. We want to vary that choice — to allow many different ways of composing the same pasting diagram, or weak ways that are only defined up to coherence — and a **globular operad** is exactly the bookkeeping device that records such a choice and lets it act.

Begin from the strict case and ask what data it carries. A **strict $\omega$-category** is a $T$-algebra: a globular set $X$ with an action $TX \to X$ assigning to every labelled pasting diagram a single composite cell, associatively and unitally. Notice what is rigid here: for each pasting diagram $\pi$ there is *exactly one* composition operation. The terminal globular set $1$, viewed as a collection via the identity map $1 \to T1$... no — the terminal *operad* is the collection $1 \xrightarrow{!} T1$ whose fibre over each $\pi$ is a single point, encoding "one composite per shape". The desideratum for the general notion is to replace this "one point per fibre" by an arbitrary set $P(\pi)$ of operations of shape $\pi$, while keeping the ability to compose operations and to act on a globular set. That is a globular operad.

So the data must be: (1) a globular set $P$, with $P(\pi)$ the operations of shape $\pi$; (2) a map $d : P \to T1$ recording the shape of each operation; (3) a composition that, given an operation $\theta$ of shape $\pi$ and operations $\phi_i$ filling the cells of $\pi$, produces a composite operation whose shape is the pasting-together of the $\phi_i$ into $\pi$; (4) units. Each ingredient is forced. Drop (2), the shape map, and "operations of shape $\pi$" is meaningless — you could not say which operations are composable, because composability is governed by matching shapes. Drop (3), composition, and you have a mere collection of operations with no algebra; you could never *use* the operations to build composites of composites, which is the entire point. Drop (4), units, and identities disappear — there is no "do nothing" operation, so the resulting algebras would lack identity cells and fail to generalize categories.

The non-negotiable axiom is the one most easily overlooked: **the shape map $d$ must be a cartesian map of collections.** Concretely this means that composing operations interacts correctly with the boundary structure — the fibre of a composite is determined by the fibres of the parts via a pullback. Why is this forced? Because $T$ is a [[Def - The Free Strict ω-Category Monad|cartesian monad]], the slice category $[\mathbb{G}^{op}, \mathbf{Set}] / T1$ carries a *substitution* monoidal product $\otimes$ for which the identity $T1 \to T1$ is the unit, and a globular operad is precisely a **monoid** in $([\mathbb{G}^{op}, \mathbf{Set}] / T1, \otimes)$. The cartesianness is exactly what makes $\otimes$ associative and unital. If $d$ were not cartesian, the substitution product would not be well-defined on $P$, and the associativity axiom of the operad — "there is a unique composite of any tree of operations" — could not even be stated. This is the place the previous page's theorem (that $T$ is cartesian) earns its keep.

What if we *strengthen* the definition by demanding each fibre $P(\pi)$ be a single point? We recover exactly the terminal operad $1$, whose algebras are strict $\omega$-categories: the rigid case is the maximally-strengthened globular operad. What if we *weaken* by dropping the requirement that operations of shape $\pi$ live in dimension matching $\pi$ (i.e. dropping globularity of $P$)? Then $P$ is no longer a globular set and the notion of "acting on a globular set's cells of the right dimension" is lost; the algebras would not be globular structures at all. The Goldilocks definition is: a globular set $P$, cartesian over $T1$, with associative unital substitution — a monoid in the substitution-product slice.

The test of the motivation: a reader who knows that a classical **operad** is "a sequence of sets $P(n)$ of $n$-ary operations with a substitution composition $P(k) \times P(n_1) \times \cdots \to P(n_1 + \cdots + n_k)$ and a unit" should be able to see a globular operad as the same idea with "arity $n$" replaced by "pasting-diagram shape $\pi$" and "substitution of operations into the $k$ inputs" replaced by "substitution of operations into the cells of $\pi$" — and should predict that the role of the symmetric group in symmetric operads is played here by nothing, because pasting diagrams have no symmetry.

---

# The Definition

> A **globular operad** is a **generalized operad** for the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] $T$. Spelled out, it consists of:
> 1. a **collection**: a globular set $P$ together with a map $d : P \to T1$ of globular sets, written $P \xrightarrow{d} T1$;
> 2. a **composition**: for each pasting diagram $\pi \in \mathrm{pd}(m)$, each operation $\theta \in P(\pi)$, and each family $(\phi_x)$ of operations of $P$ indexed by and matching the constituent cells $x$ of $\pi$, a composite operation
> $$
> \theta \circ (\phi_x)_x \in P\big(\textstyle\sum_x \phi_x \text{ pasted into } \pi\big);
> $$
> 3. **units**: for each pasting diagram $\pi$ a unit operation $1_\pi \in P(\pi)$;
>
> subject to the requirement that $d$ be a **cartesian** map and that composition be associative and unital. Equivalently and most efficiently: a globular operad is a **monoid in the monoidal category** $\big([\mathbb{G}^{op}, \mathbf{Set}] / T1,\ \otimes\big)$, where $\otimes$ is the substitution product induced by the cartesian monad $T$, with unit the identity collection $T1 \xrightarrow{\mathrm{id}} T1$.

The summary slogan of the definition (Leinster 8.2): *a globular operad is a collection of operations together with a unique composite for any family of operations that might plausibly be composed.*

The **fibre** $P(\pi) = d^{-1}(\pi)$ is the set of operations of shape $\pi$. An operation $\theta \in P(\pi)$ is to be read as "an abstract way of composing any labelled diagram of shape $\pi$"; its source and target are the operations $s(\theta), t(\theta) \in P(\partial\pi)$ over the boundary of $\pi$.

The **terminal globular operad** is the collection $1 \xrightarrow{!} T1$ with $1$ the terminal globular set, so $P(\pi) = \{\ast\}$ for every $\pi$: exactly one operation per shape. This is the globular operad whose algebras are the **strict $\omega$-categories**.

---

# Categorical / Structural Definition

The cleanest formulation is the monoid-in-a-monoidal-category one, and it is worth unpacking because it is how the existence proofs and the contraction theory are actually run. Because $T$ is cartesian, the slice category $\mathcal{E} = [\mathbb{G}^{op}, \mathbf{Set}] / T1$ of **collections** carries a monoidal structure $\otimes$, the **substitution product**. On objects, given collections $P \xrightarrow{d} T1$ and $Q \xrightarrow{e} T1$, their product $P \otimes Q$ has, as its operations, the pairs "an operation $\theta$ of $P$ of shape $\pi$, together with a $Q$-operation filling each cell of $\pi$", with the resulting shape obtained by substitution; cartesianness of $T$ makes this a [[Def - Pullback and Pushout|pullback]] construction and guarantees $\otimes$ is associative up to canonical isomorphism, with unit the collection $T1 \xrightarrow{\mathrm{id}} T1$.

> A **globular operad** is a **monoid** $(P, \mathrm{comp}, \mathrm{unit})$ in $(\mathcal{E}, \otimes)$: an object $P$ with a multiplication $\mathrm{comp} : P \otimes P \to P$ (the operadic composition) and a unit $\mathrm{unit} : I \to P$ (the operadic identities), satisfying the [[Def - Monoid in a Monoidal Category|monoid axioms]] of associativity and unitality.

This is exactly parallel to the way a classical **operad** is a monoid in the category of symmetric sequences under the substitution product, and to the way a **monoid** in the ordinary sense is a monoid in $(\mathbf{Set}, \times)$. The unifying statement is: *operadic structures are monoids for a substitution product, and the substitution product comes from a cartesian monad.* This monoid viewpoint is what makes the category of globular operads complete and cocomplete with the right limits, and in particular it is what lets one speak of the *initial* globular operad equipped with extra structure — the construction that produces $L$.

There is a second structural reading via **monads**. Each globular operad $P$ induces a monad $T_P$ on globular sets — its "free $P$-algebra" monad — equipped with a cartesian monad map $T_P \Rightarrow T$. A globular operad is thus the same as a cartesian monad over $T$, and a $P$-algebra (next paragraph) is a $T_P$-algebra. This is the bridge to the general theory of [[Def - Monad and Comonad|monads]]: globular operads are precisely the "sub-theories of the theory of strict $\omega$-categories" in a cartesian-monad sense.

An **algebra for a globular operad $P$** is a globular set $X$ together with an action assigning, to each pasting diagram $\pi$, each operation $\theta \in P(\pi)$, and each labelling of $\pi$ by cells of $X$ of matching dimension, a composite cell $\theta_X(\text{labelling}) \in X(m)$, naturally and compatibly with operadic composition and units. Equivalently, a $P$-algebra is an [[Def - Algebra for a Monad|algebra]] for the induced monad $T_P$. The slogan: *the operations of $P$ tell you the legal ways to compose, and an algebra is a globular set in which all those compositions are actually performed.* Algebras for the terminal operad are strict $\omega$-categories; algebras for a richer $P$ are "higher categorical structures of the signature $P$".

---

# Relate to Other Fields / Compression

A globular operad is to a strict $\omega$-category as a classical **operad** is to a monoid, transplanted to the globular world. Recall the classical picture: an operad $P$ is a sequence $P(0), P(1), P(2), \dots$ where $P(n)$ is the set of "abstract $n$-ary operations", with a composition that substitutes operations into the inputs of an operation and a nullary/unary unit; an algebra for $P$ is an object $X$ with structure maps $P(n) \to \mathrm{Hom}(X^n, X)$. Two famous examples fix the analogy: the **associative operad** $\mathrm{Assoc}$, with $\mathrm{Assoc}(n) = n!$ orderings (or the single operation in the non-symmetric case), whose algebras are monoids; and the **commutative operad** $\mathrm{Comm}$, with $\mathrm{Comm}(n) = \{\ast\}$, whose algebras are commutative monoids. A globular operad is the exact analogue with "arity $n$" upgraded to "pasting-diagram shape $\pi$", the substitution following the geometry of pasting rather than the linear order of inputs, and the algebras being globular sets-with-composition rather than sets-with-multiplication.

**True name:** *a globular operad is a "signature for a flavour of $\omega$-category": it lists, for each pasting shape, the available composition operations, and an algebra is an $\omega$-category that performs them.* When solving problems, do not picture the cartesian map abstractly — picture the fibres $P(\pi)$ as "the menu of ways to compose a diagram of shape $\pi$", and picture an algebra as a globular set that has chosen, for each menu item, an actual operation on its cells. The terminal operad has a one-item menu per shape (the strict case); a contractible operad has a rich menu including coherence cells (the weak case).

The deepest compression is the cartesian-monad uniformity. Every "operad-like" notion in higher category theory — classical operads, symmetric operads, **multicategories**, $fc$-multicategories, **opetopes** via iterated slicing — is a $T$-operad for some cartesian monad $T$. Globular operads are the case $T =$ free strict $\omega$-category monad. Holding the family in mind means a single theorem about $T$-operads (initiality, existence of contractions, the algebra construction) specializes to all of them at once.

---

# Examples / Corollaries

**Is an instance — the terminal globular operad $1$.** The collection $1 \xrightarrow{!} T1$ has exactly one operation of each shape, so composition and units are uniquely determined and the operad axioms hold trivially. Its algebras are precisely the **strict $\omega$-categories**: one composition per pasting diagram, performed strictly. This is the rigid extreme, and it is the operad whose perturbation produces the weak theory.

**Is an instance — the operad $T1$ itself (the "free-living" operad).** The collection $T1 \xrightarrow{\mathrm{id}} T1$ is a globular operad: its operations of shape $\pi$ are the pasting diagrams that *are* $\pi$, i.e. exactly one again, but now the composition is "paste the sub-diagrams in", literally $\mu$. Its algebras are again strict $\omega$-categories. (This and the terminal operad coincide up to the canonical iso identifying their fibres; the distinction matters only when tracking the substitution product's unit.)

**Is an instance — an endomorphism globular operad.** Given a globular set $X$, there is an **endomorphism operad** $\mathrm{End}(X)$ whose operations of shape $\pi$ are *all* actual composition operations on $X$ of that shape, i.e. all functions sending a labelling of $\pi$ by cells of $X$ to a single cell of $X$ over the boundary correctly. A $P$-algebra structure on $X$ is precisely a globular operad map $P \to \mathrm{End}(X)$ — the operadic analogue of "an action is a homomorphism into the endomorphisms". This example is the engine of the statement "any contractible globular set carries a weak $\omega$-category structure": one builds a contraction into $\mathrm{End}(X)$ and pulls back along $L \to \mathrm{End}(X)$.

**Is NOT an instance — an arbitrary collection with non-cartesian shape map.** A globular set $P$ with a map $d : P \to T1$ that is *not* cartesian is a perfectly good collection but generally fails to support an associative substitution: composing operations can land in the wrong fibre or fail to be well-defined. So "collection" alone is not "operad"; the cartesian condition plus associative composition is what upgrades it. This is the analogue of "a sequence of sets $P(n)$ is not an operad until you supply a substitution that is associative."

**Is NOT an instance — a symmetric (classical) operad, naively.** A symmetric operad carries $S_n$-actions on its $n$-ary operations. A globular operad carries no such symmetry: there is no group acting on the cells of a pasting diagram, because the cells sit at fixed, oriented positions. Trying to read a symmetric operad as a globular operad confuses two different cartesian monads (the free-monoid monad on $\mathbf{Set}$ versus $T$ on globular sets). The structures are cousins, not the same.

**Calibration check.** Verify that the terminal operad's algebras are strict $\omega$-categories by checking that "one operation per pasting diagram, acting on labellings" is exactly a strict-$\omega$-category structure. Confirm that for any globular operad $P$ and globular set $X$, a $P$-algebra structure on $X$ is the same as a globular-operad map $P \to \mathrm{End}(X)$. Finally, explain in one sentence why the cartesianness of $T$ is what makes the substitution product $\otimes$ on collections associative — if you can, you have understood why "globular operad = monoid in the substitution slice" is well-posed.

---

# Unlocked by This

> [!tip] Contraction on a Globular Operad *(from this chapter)*
> A globular operad is the object a **contraction** lives on. A contraction supplies, for every parallel pair of operations over a boundary, a chosen operation over the full pasting diagram witnessing them as source and target — encoding weak composition and coherence. See [[Def - Contraction on a Globular Operad]].

> [!tip] Weak ω-Category *(from this chapter)*
> The initial globular operad carrying a contraction is the **Batanin–Leinster operad** $L$; a **weak ω-category** is an $L$-algebra. The whole point of the globular-operad framework is to make "$L$-algebra" a well-defined and canonical notion. See [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)]] and [[Thm - The Initial Contractible Globular Operad Exists]].

> [!tip] Opetopic and Other Operadic Models *(from Higher Operads)*
> Replacing the globular cartesian monad $T$ by the slice construction on the identity operad produces **opetopes** and the Baez–Dolan opetopic definition of weak $n$-category; replacing it by the free strict $n$-tuple-category monad produces cubical higher categories. Globular operads are one corner of a general "cartesian monad $\rightsquigarrow$ higher-categorical signature" dictionary.
