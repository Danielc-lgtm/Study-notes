---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Globular Operad"
  - "Def - Contraction on a Globular Operad"
  - "Def - The Free Strict ω-Category Monad"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Let $(T, \eta, \mu)$ be the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] on **globular sets**, $T1 = \mathrm{pd}$ the **pasting diagrams**, $\partial : \mathrm{pd}(m+1) \to \mathrm{pd}(m)$ the boundary. Let $\mathbf{OC}$ be the category of [[Def - Globular Operad|globular]] **operads-with-[[Def - Contraction on a Globular Operad|contraction]]**: objects $(P, \chi)$, morphisms contraction-preserving operad maps. For a pasting diagram $\pi$, $P(\pi)$ is the fibre of operations over $\pi$, $\mathrm{Par}_P(\pi)$ the set of parallel pairs over $\partial\pi$, and $(s,t) : P(\pi) \to \mathrm{Par}_P(\pi)$ the source-target pairing. The initial object is written $(L, \chi)$, the **Batanin–Leinster operad**. The full symbol registry is on [[Higher Categories — Globular Operads and Weak n-Categories]]. The notions **strict ω-category** and **tame** are from chapters not yet in the vault; they are restated as needed.

---

# Statement

> **Theorem (Existence of the initial operad-with-contraction; Leinster 9.2.2).** The category $\mathbf{OC}$ of globular operads-with-contraction has an **initial object** $(L, \chi)$. That is, there is a globular operad $L$ equipped with a contraction $\chi$ such that for every globular operad-with-contraction $(P, \chi')$ there exists a *unique* operad map $f : L \to P$ preserving the contraction:
> $$
> f\big(\chi_\pi(\alpha^-, \alpha^+)\big) = \chi'_\pi\big(f\alpha^-, f\alpha^+\big) \qquad \text{for all } \pi,\ (\alpha^-, \alpha^+) \in \mathrm{Par}_L(\pi).
> $$
> The pair $(L, \chi)$ is determined up to unique isomorphism by this universal property.

> **Companion (finite-dimensional form; Leinster 9.3).** For each $n \in \mathbb{N}$, the category $\mathbf{OC}_n$ of $n$-globular operads-with-contraction (a precontraction on a **tame** map) likewise has an initial object $(L_n, \chi)$. In the top dimension $n$, contractibility forces the source-target pairing to be a *bijection*, so $L_n$ is determined by its $(n-1)$-dimensional part.

The two forms agree under truncation: $L_n$ is the $n$-dimensional shadow of $L$, with the single extra top-dimensional rigidity supplied by tameness.

---

# Motivation

This theorem is the load-bearing existence result of the whole Batanin–Leinster definition. Without it, "a weak $\omega$-category is an $L$-algebra" would be vacuous — there would be no $L$ to take algebras of. The definition of weak $\omega$-category commits, in advance, to using *the* initial operad-with-contraction; the theorem is the guarantee that such an object exists and is unique, so that the definition refers to something real and canonical rather than to a wish.

The role the theorem plays is to convert a *universal property* into a *construction*. We argued, when motivating the definition, that the operad for weak $\omega$-categories should be the freely-generated, minimal one carrying a contraction — initial in $\mathbf{OC}$. But initiality is an existence claim about a category that is far from obviously well-behaved: $\mathbf{OC}$ mixes the algebraic structure of an operad (composition, units, associativity) with the lifting structure of a contraction (a chosen filler for every parallel pair, in every dimension), and it is not a priori clear these can be freely generated together without contradiction or infinite regress. The theorem says they can, by an explicit dimension-by-dimension construction that alternately closes under operadic composition and under contraction. It is the moment the definition becomes legitimate.

There is also a methodological lesson. The construction *interleaves* two closure operations — close under composition, then under contraction, then under composition again — and the fact that this interleaving converges (produces a genuine operad-with-contraction, not just a formal limit) is the technical heart. This same "free model of a theory with two interacting kinds of generators" pattern recurs whenever one builds free higher-categorical structures, and the proof technique here is its prototype.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal precondition is "we are in the category $\mathbf{OC}$", which seems to offer little room for disguised inputs. The real sources are the *abstract structural facts* that make the existence proof go through, and recognizing when those facts hold lets you apply the same existence machinery far beyond globular operads.

The first disguised source is **cartesianness of the underlying monad $T$**. The construction of $L$ relies, at every stage, on the slice category $[\mathbb{G}^{op},\mathbf{Set}]/T1$ carrying a well-behaved substitution product, which holds precisely because $T$ is a [[Def - The Free Strict ω-Category Monad|cartesian monad]]. The bridge "$T$ cartesian $\implies$ free operads-with-structure exist" is non-obvious: it converts an analytic-looking condition on naturality squares into the existence of a freely-generated algebraic-and-lifting structure. *Example application:* the cubical analogue, using the free strict $n$-tuple-category monad (also cartesian), gives an initial cubical operad-with-contraction by the *same* argument — you check cartesianness and the proof transfers.

The second disguised source is **the presence of a free-forgetful adjunction with monadic forgetful functor between $\mathbf{OC}$ and a category of "raw" collections**. Initial objects are free objects on the empty generating set, so an initial operad-with-contraction is the value of a left adjoint at the initial collection. Whenever you can exhibit the forgetful functor "operad-with-contraction $\mapsto$ underlying globular set" as monadic (or as having a left adjoint built by a transfinite small-object-style construction), initiality follows. *Example application:* recognizing that "operad-with-a-system-of-compositions-and-a-coherence" also has a monadic forgetful functor yields *its* initial object — Batanin's variant operad — by the same adjoint-existence reasoning.

The third disguised source is **a dimension-by-dimension (inductive) presentability**. The construction works because the structure in dimension $n$ depends only on dimensions $< n$ plus a single closure step, so one can build $L$ by induction on dimension. Any higher-structure that is "generated layer by layer with finitary closure at each layer" admits the same inductive free construction. *Example application:* Grothendieck–Maltsiniotis **coherators** generate free $\infty$-groupoids by an analogous layered closure, and the existence of the free coherent structure is proved the same way.

**Targets (Output Amplification)**

The bare conclusion is "$(L, \chi)$ exists and is initial". Combined with other facts it does much more.

Combine initiality with **the functoriality of the algebra construction** $P \mapsto \mathrm{Alg}(P)$. Since $L$ is initial, there is a unique map $L \to P$ for every operad-with-contraction $P$, hence a canonical functor $\mathrm{Alg}(P) \to \mathrm{Alg}(L) = \mathbf{Wk\text{-}\omega\text{-}Cat}$. The amplified result is: *every algebra for every operad-with-contraction is canonically a weak $\omega$-category*. This is non-obvious because it turns a single existence statement into a universal *recipe* for producing weak $\omega$-categories from any contractible operad — including endomorphism operads of contractible globular sets.

Combine initiality with **the trivial contraction on the terminal operad $1$**. The terminal globular operad admits a unique contraction, making $(1, \chi_1)$ the *terminal* object of $\mathbf{OC}$ as well; the unique map $L \to 1$ induces $\mathbf{Str\text{-}\omega\text{-}Cat} \to \mathbf{Wk\text{-}\omega\text{-}Cat}$, and contractibility of $L$ (which makes every $L(\pi)$ non-empty) upgrades this to a *full and faithful* embedding. The amplified result is the precise statement that strict $\omega$-categories are weak ones, with strict functors agreeing — a corollary that depends on $L$ being both initial and contractible.

Combine initiality with **truncation** to get the finite-dimensional theory. Applying the construction in $n$ dimensions, with tameness enforced on top, yields $L_n$ and hence the definition of weak $n$-category; comparing $L_n$ with explicit small operads in low dimensions yields the classification $\mathbf{Wk\text{-}0\text{-}Cat} \simeq \mathbf{Set}$, $\mathbf{Wk\text{-}1\text{-}Cat} \simeq \mathbf{Cat}$, $\mathbf{Wk\text{-}2\text{-}Cat} \simeq \mathbf{UBicat}_{str}$ (see [[Thm - Weak 2-Categories are Bicategories]]). The amplified result is that the abstract existence theorem, specialized and computed, *recovers the classical low-dimensional notions*, which is the sanity check that the definition is correct.

---

# Why Is It True

Forget the formal construction and ask why one should *expect* a freely-generated operad-with-contraction to exist. The two kinds of data — operadic composition and contraction lifts — both add new operations, and the worry is that adding operations of one kind could create new obligations of the other kind without end, so that the process never closes off. The reason it does close off is that **both closure operations strictly raise the "complexity" of the operations they produce in a well-founded way, and at each fixed dimension only finitely much is generated before the next dimension is needed.**

Here is the mechanism. Build $L$ by induction on dimension. Suppose $L$ is known and is an operad-with-contraction up to and including dimension $n-1$. To produce dimension $n$, do two closures. First, **close under contraction**: for every $n$-dimensional pasting diagram $\pi$ and every parallel pair $(\alpha^-, \alpha^+)$ of already-constructed $(n-1)$-dimensional operations over $\partial\pi$, throw in a new $n$-operation $\chi_\pi(\alpha^-, \alpha^+)$ with that source and target. Second, **close under $n$-dimensional operadic composition and units**: throw in all composites and identities of the operations now present in dimension $n$. Crucially, each closure feeds the other only *within* dimension $n$ — contraction lifts depend on dimension $n-1$, which is already finished, and composition combines dimension-$n$ operations among themselves. There is no feedback that reaches back down to disturb lower dimensions, because source and target of an $n$-operation live in dimension $n-1$, which is frozen. So the generation is well-founded: it terminates at each dimension and proceeds upward forever, producing a genuine $\omega$-dimensional operad.

> **The one-line mechanism:** *initiality holds because building $L$ is a stratified free construction — dimension $n$ is generated from the frozen dimension $n-1$ by alternately lifting parallel pairs (contraction) and forming composites (operad), with no downward feedback, so each stage closes off and the tower never stalls.*

Uniqueness is the easy half and is pure abstract nonsense: any two initial objects of a category are uniquely isomorphic, because the unique maps between them compose to the identities (the unique self-map of an initial object is the identity). So the content is entirely in existence — in the convergence of the stratified construction — and the universal property comes for free once existence is in hand.

The finite-dimensional case is the same construction with one twist at the very top. In dimension $n$ of an $n$-category there is no dimension $n+1$ to receive future coherence cells, so the lifts cannot be deferred and must instead be *forced into equalities*: this is **tameness**, and it makes the top-dimensional source-target pairing a bijection rather than a surjection. The construction still converges — it just identifies, rather than defers, in the top layer.

---

# What Makes This Hard

The non-obvious step is seeing that the interleaving of two closures (contraction, then operadic composition) at each dimension actually *terminates* and yields a structure satisfying *both* sets of axioms simultaneously — most people either fear an infinite regress within a single dimension or fail to check that the contraction $\chi$ remains a contraction after composites are added. The common error is to construct the operad $L$ first (closing under composition) and only then try to bolt on a contraction, which fails because the freely-added coherence cells are themselves operations that must be composable; contraction and composition must be generated *together*. The subtle finite-dimensional pitfall is forgetting tameness in the top dimension, which silently produces a precontractible-but-not-contractible $n$-operad — an object that looks right but admits spurious distinct parallel top cells.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Construct $(L, \chi)$ by induction on dimension. At each dimension, alternately close under contraction (lift every parallel pair) and under operadic composition-and-units, using that lower dimensions are already frozen so the closures do not interfere downward. Then verify the universal property by defining the unique map $L \to P$ dimension by dimension, forced at each step by "preserve operadic structure and preserve contraction".

**Subgoal decomposition:**

1. **Set up the inductive skeleton.** Define $L$ in dimension $0$ (a single point: the only $0$-operation is the identity) and assume $L$ built and consistent up to dimension $n-1$.
   - *Hint:* In dimension $0$ there are no parallel pairs to lift and the only pasting diagram is the point, so $L(0)$ is forced to be a one-element set.
   - *Why needed:* Provides the base case and the frozen lower structure on which dimension $n$ is built.

2. **Close under contraction in dimension $n$.** For every $n$-pasting diagram $\pi$ and every parallel pair $(\alpha^-, \alpha^+) \in \mathrm{Par}_L(\pi)$ of $(n-1)$-operations, freely adjoin $\chi_\pi(\alpha^-, \alpha^+) \in L(\pi)$ with the prescribed source, target, and shape.
   - *Hint:* These are the new coherence cells; their source and target live in the frozen dimension $n-1$, so adjoining them disturbs nothing below.
   - *Why needed:* Supplies the contraction's lifts, the data that makes $L$ contractible.

3. **Close under operadic composition and units in dimension $n$.** Adjoin all operadic composites and identities of the $n$-operations present after Step 2, then repeat Steps 2–3 until no new operations appear in dimension $n$.
   - *Hint:* Composition of $n$-operations stays in dimension $n$ and only reads source/target in dimension $n-1$; the alternation closes off because no closure creates obligations below dimension $n$.
   - *Why needed:* Makes $L$ an operad in dimension $n$; the alternation is what lets composition and contraction coexist.

4. **Verify $(L, \chi)$ is an operad-with-contraction.** Check the operad axioms (associativity, unitality) and the contraction axioms (source/target/shape) hold in all dimensions.
   - *Hint:* Both hold by construction at each dimension because everything was freely adjoined to satisfy exactly these equations.
   - *Why needed:* Confirms $(L,\chi)$ is an object of $\mathbf{OC}$.

5. **Prove initiality.** Given any $(P, \chi') \in \mathbf{OC}$, define $f : L \to P$ by induction on dimension: on generators forced by contraction, $f$ must send $\chi_\pi(\alpha^-,\alpha^+) \mapsto \chi'_\pi(f\alpha^-, f\alpha^+)$; on composites, $f$ must respect composition. Show this is forced (uniqueness) and well-defined (existence).
   - *Hint:* Every operation of $L$ is built from contraction-lifts and composites; "preserve contraction" and "preserve composition" determine $f$ on each, with no freedom.
   - *Why needed:* Establishes the universal property, hence initiality and uniqueness up to unique isomorphism.

---

# Lemma Decomposition

> [!note]- Lemma 1: The terminal globular operad admits a unique contraction
> **Statement:** The terminal globular operad $1$ (one operation per pasting diagram) admits exactly one contraction, making $(1, \chi_1)$ the terminal object of $\mathbf{OC}$.
>
> **Hint:** Each fibre $1(\pi)$ is a singleton, so each $\chi_\pi : \mathrm{Par}_1(\pi) \to 1(\pi)$ has a one-element codomain and is therefore uniquely determined; check the source/target/shape conditions hold automatically.
>
> **Why needed:** It identifies the terminal object of $\mathbf{OC}$ and is the target of the map $L \to 1$ used to embed strict $\omega$-categories into weak ones; it also shows $\mathbf{OC}$ has both an initial and a terminal object.
>
> > [!note]- Full proof
> > For each pasting diagram $\pi$ the fibre $1(\pi) = \{\ast\}$ is a singleton. A contraction component $\chi_\pi : \mathrm{Par}_1(\pi) \to 1(\pi)$ is a function into a one-element set, hence the unique constant function; so at most one contraction exists. It is a genuine contraction because the source, target, and shape conditions assert equalities in $1(\partial\pi)$ and $\mathrm{pd}$ that are automatic: $s(\ast), t(\ast)$ are the unique operation over $\partial\pi$, and the parallel pair $(\alpha^-,\alpha^+) \in \mathrm{Par}_1(\pi)$ necessarily has $\alpha^- = \alpha^+ = \ast$ since $1(\partial\pi)$ is a singleton, so the source/target conditions $s(\ast)=\alpha^-$, $t(\ast)=\alpha^+$ hold, and $d(\ast) = \pi$ by definition. For terminality: for any $(P,\chi')$ there is a unique operad map $P \to 1$ (since $1$ is the terminal collection), and it preserves contractions vacuously because the target fibres are singletons. $\blacksquare$

> [!note]- Lemma 2: Stratified closure does not disturb lower dimensions
> **Statement:** Adjoining contraction-lifts and operadic composites in dimension $n$ leaves the operations and axioms in dimensions $< n$ unchanged.
>
> **Hint:** The source and target of an $n$-operation lie in dimension $n-1$; no closure operation in dimension $n$ produces or alters an operation of dimension $< n$.
>
> **Why needed:** It is the well-foundedness that makes the inductive construction converge — without it, building dimension $n$ could create new obligations below, and the induction would not terminate.
>
> > [!note]- Full proof
> > A contraction-lift $\chi_\pi(\alpha^-,\alpha^+)$ adjoined in Step 2 is an $n$-operation; its only interaction with lower dimensions is through its source $\alpha^-$ and target $\alpha^+$, which are *pre-existing* $(n-1)$-operations — nothing new is created below. An operadic composite of $n$-operations adjoined in Step 3 is again an $n$-operation, with source and target obtained by composing the (frozen) sources and targets in dimension $n-1$; again nothing below is created or altered. The operad and contraction axioms involving only dimensions $< n$ therefore continue to hold unchanged. Hence the structure in dimensions $< n$ is frozen, and the dimension-$n$ closure can be carried out in isolation. $\blacksquare$

> [!note]- Lemma 3: The map out of an initial object is forced and well-defined
> **Statement:** For any $(P, \chi') \in \mathbf{OC}$, there is exactly one contraction-preserving operad map $f : L \to P$.
>
> **Hint:** Every operation of $L$ is generated by contraction-lifts and operadic composites; "preserve contraction" fixes $f$ on lifts and "preserve composition" fixes $f$ on composites, so $f$ is determined; well-definedness follows because $L$ was freely generated, so no relations can be violated.
>
> **Why needed:** This is the universal property itself — existence and uniqueness of $f$ — and hence the statement of initiality.
>
> > [!note]- Full proof
> > *Uniqueness.* Define $f$ by induction on dimension. In dimension $0$, $L(0)$ is a singleton and $f$ is forced. Suppose $f$ is determined in dimensions $< n$. Any $n$-operation of $L$ arises, by construction, either as a contraction-lift $\chi_\pi(\alpha^-,\alpha^+)$ or as an operadic composite of lower-built $n$-operations. For a lift, the contraction-preservation equation forces $f(\chi_\pi(\alpha^-,\alpha^+)) = \chi'_\pi(f\alpha^-, f\alpha^+)$, with the right-hand side already determined since $\alpha^\pm$ have dimension $n-1$. For a composite, operad-map-ness forces $f$ of the composite to be the composite of the $f$-images, again already determined. So $f$ is unique.
> >
> > *Existence.* Define $f$ by the very formulas just shown to be forced; this is possible because $L$ is *freely* generated by these operations subject only to the operad and contraction axioms, so the formulas are consistent — any equation holding in $L$ is a consequence of those axioms, and $P$ satisfies the corresponding axioms, so the equation is respected. Thus $f$ is a well-defined contraction-preserving operad map. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We construct $(L, \chi)$ and verify initiality.
>
> **Step 0 — the ambient structure exists.** Because $T$ is a [[Def - The Free Strict ω-Category Monad|cartesian monad]], the slice category $\mathcal{E} = [\mathbb{G}^{op}, \mathbf{Set}]/T1$ of collections carries an associative, unital substitution product $\otimes$, so "globular operad" = monoid in $(\mathcal{E}, \otimes)$ is well-posed, and the notion of a contraction on a collection is defined. Thus $\mathbf{OC}$ is a genuine category. (This is exactly the role of the cartesianness theorem of the previous page.)
>
> **Step 1 — base of the induction.** Define $L$ in dimension $0$ by $L(0) = \{\mathrm{id}\}$, the one-element set; there is a unique $0$-pasting diagram (the point) and no parallel pairs in dimension $0$, so this is forced and trivially satisfies all axioms.
>
> **Step 2 — inductive step, contraction closure.** Assume $L$ is constructed and is an operad-with-contraction up to and including dimension $n-1$. For every $n$-pasting diagram $\pi$ and every parallel pair $(\alpha^-, \alpha^+) \in \mathrm{Par}_L(\pi)$ of $(n-1)$-operations over $\partial\pi$, freely adjoin an $n$-operation $\chi_\pi(\alpha^-, \alpha^+) \in L(\pi)$ with $s = \alpha^-$, $t = \alpha^+$, $d = \pi$.
>
> **Step 3 — inductive step, operadic closure.** Freely adjoin to dimension $n$ all operadic composites and identities of the $n$-operations present, then re-run Steps 2–3 until dimension $n$ stabilises. By Lemma 2 these closures do not affect dimensions $< n$, so the alternation is confined to dimension $n$ and terminates (each step only combines or lifts already-listed data with sources/targets in the frozen dimension $n-1$). This defines $L$ in dimension $n$, with its contraction $\chi$ and operad structure.
>
> **Step 4 — $(L, \chi) \in \mathbf{OC}$.** By Lemma 2 the construction yields a consistent $\omega$-dimensional globular set $L$. The operad axioms hold because Step 3 freely adjoined exactly the composites and identities subject to associativity and unitality; the contraction axioms hold because Step 2 freely adjoined lifts with exactly the prescribed source, target, and shape. Hence $(L, \chi)$ is a globular operad-with-contraction.
>
> **Step 5 — initiality.** By Lemma 3, for every $(P, \chi') \in \mathbf{OC}$ there is a unique contraction-preserving operad map $f : L \to P$. Therefore $(L, \chi)$ is initial in $\mathbf{OC}$.
>
> **Step 6 — uniqueness up to unique isomorphism.** Any two initial objects of a category are uniquely isomorphic: if $(L, \chi)$ and $(L', \chi')$ are both initial, the unique maps $L \to L'$ and $L' \to L$ compose to unique self-maps, which must be the (unique) identities, so the maps are mutually inverse isomorphisms. Hence $(L, \chi)$ is determined up to unique isomorphism. $\blacksquare$
>
> **Finite-dimensional form.** Repeat in $n$ dimensions with the free strict $n$-category monad $T^{(n)}$ (cartesian by Leinster Thm F.2.1). The only change is in the top dimension $n$: there is no dimension $n+1$ to receive deferred coherence, so contractibility requires the source-target pairing $(s,t) : L_n(\pi) \to \mathrm{Par}_{L_n}(\pi)$ to be a *bijection* (a precontraction on a **tame** map), which forces $L_n(\pi)$ in dimension $n$ to be exactly $\mathrm{Par}_{L_n}(\pi)$. The construction otherwise proceeds identically and yields the initial object $(L_n, \chi)$ of $\mathbf{OC}_n$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Free coherent structures in homotopy theory (coherators).** The Grothendieck–Maltsiniotis definition of $\infty$-groupoid is built from a **coherator**: a globular theory freely generated by "all admissible operations and all coherence cells exist". Showing that an initial coherator exists is the homotopy-theoretic twin of this theorem, proved by the same stratified "close under operations, then under coherences" induction. The non-obvious transfer is recognizing that "coherator" plays the role of "operad-with-contraction" once one passes from operads to globular theories.

**The small object argument in model categories.** The proof's interleaving of two closures until convergence is the operadic shadow of the **small object argument**, which factors maps by transfinitely interleaving pushouts of generating cofibrations. The source property that makes both arguments work is "smallness/finiteness at each stage so the construction closes off". A reader who has internalized the small object argument should recognize the same convergence logic here, applied to operations-and-coherences instead of cofibrations.

**Free algebras for an equational theory.** At its most elementary, this theorem is "the free model of a two-sorted equational theory (operations + lifts) exists", a special case of the general existence of free algebras for finitary monads. Casting the theorem this way — and then noting the extra subtlety is that one of the "sorts" (the contraction) is a *lifting* condition rather than an operation — shows where the standard universal-algebra machinery applies and where it must be extended.

---

# Bridges

- **[[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)|Weak ω-Category]]** — this theorem is what makes that definition legitimate. The object $L$ whose existence is proved here is the operad whose algebras *are* the weak $\omega$-categories. Without the theorem, the phrase "an $L$-algebra" would name nothing; with it, the phrase names a canonical, uniquely-determined category $\mathrm{Alg}(L)$.

- **[[Thm - Weak 2-Categories are Bicategories]]** — the finite-dimensional form of this theorem produces $L_2$, the initial tame $2$-operad-with-contraction. Computing $L_2$ explicitly (it is generated by the operad of trees, $L_2 = (I^2_1)_\ast \delta_\ast \mathrm{tr}$ in Leinster's notation) is precisely the input that the $2$-categories theorem then compares with the operad for unbiased bicategories. The existence here is the prerequisite for the identification there.

- **[[Def - The Free Strict ω-Category Monad|Cartesianness of the monad]]** — the unsung hero of the proof. Step 0 of the formal proof uses cartesianness to make the substitution product, hence the very category $\mathbf{OC}$, well-defined. The theorem is, in a sense, "cartesianness, cashed out": a cartesian monad's slice supports free operads-with-structure, and $L$ is the most important such free object.

- **[[Def - Algebra for a Monad|The algebra construction]]** — initiality is useful only because $P \mapsto \mathrm{Alg}(P)$ is functorial. The unique map $L \to P$ induces $\mathrm{Alg}(P) \to \mathbf{Wk\text{-}\omega\text{-}Cat}$, so this theorem plus functoriality of algebras is what lets *any* contractible operad's algebras be reinterpreted as weak $\omega$-categories.

---

# Unlocked by This

> [!tip] Batanin's Operad and Variants with a System of Compositions *(from Higher Operads)*
> The same existence argument, run for the category of operads-equipped-with-a-**system of compositions**-and-a-**coherence**, produces **Batanin's original operad**. That the two initial objects yield equivalent categories of algebras is the sense in which the Batanin and Leinster definitions of weak $\omega$-category coincide.

> [!tip] Initial Coherators and Grothendieck ∞-Groupoids *(from Higher Category Theory)*
> Replacing "operad-with-contraction" by **Grothendieck–Maltsiniotis coherator** and re-running the stratified free construction gives the free $\infty$-groupoid theory. The **homotopy hypothesis** conjectures its algebras model homotopy types; this existence theorem is the algebraic template for the coherator's existence.
