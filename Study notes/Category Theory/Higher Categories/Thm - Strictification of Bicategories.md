---
type: theorem
subject: higher-categories
prereqs:
  - "Def - 2-Category and Bicategory"
  - "Def - Monoidal Category"
  - "Def - Equivalence of Categories"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

A [[Def - 2-Category and Bicategory|bicategory]] $\mathcal{B}$ has $0$-cells, $1$-cells, $2$-cells, with weak (coherent-isomorphism) associativity and unit laws given by the associator $a$ and unitors $l, r$. A **strict $2$-category** is a bicategory whose $a, l, r$ are all identities. A **biequivalence** $\mathcal{B} \to \mathcal{C}$ is a (pseudo)functor that is essentially surjective on $0$-cells and induces [[Def - Equivalence of Categories|equivalences]] on all hom-categories — the bicategorical analogue of an equivalence of categories. A **tricategory** is the (weak) one-dimension-up analogue; a strict $3$-category is a category enriched in strict $2$-categories. The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

---

# Statement

> **Theorem (Coherence / Strictification for Bicategories).** Every [[Def - 2-Category and Bicategory|bicategory]] $\mathcal{B}$ is biequivalent to a strict $2$-category. Consequently every diagram in $\mathcal{B}$ built from associators $a$, unitors $l, r$, and identities commutes ("all coherence diagrams commute").

> **Corollary (Mac Lane coherence, the one-object case).** Every [[Def - Monoidal Category|monoidal category]] is monoidally equivalent to a strict monoidal category; equivalently, every formal diagram built from the associativity and unit isomorphisms in a monoidal category commutes. See [[Thm - Mac Lane Coherence Theorem]].

> **Remark (the failure at dimension three).** The analogous statement fails one dimension up: not every **tricategory** is (tri)equivalent to a strict $3$-category. The best possible result (Gordon–Power–Street) is that every tricategory is triequivalent to a **Gray-category** — a $3$-category strict in everything except the interchange of $1$-cells, which remains weak. So weakness is fully removable at dimension $\le 2$ and irreducibly present from dimension $3$.

---

# Motivation

Bicategories are honest but inconvenient. The honesty is that associativity of $1$-cells holds only up to the associator — which is exactly right for examples like tensor products of bimodules, where strict associativity is false. The inconvenience is that every computation drags associators and unitors along: a product of four $1$-cells can be bracketed five ways, and to compare two expressions you must insert the right associator $2$-cells and check they cancel. If you had to track this coherence data by hand in every proof, bicategory theory would be unusable.

The coherence theorem rescues the situation completely. It says the inconvenience is *cosmetic*: every bicategory is biequivalent to a strict $2$-category, where associativity holds on the nose and no associators appear. So you may, without loss, *pretend* your bicategory is strict — do the computation as if associativity were an equality — and the theorem guarantees the conclusion transports back. This is why working category theorists almost never write down associators: coherence licenses suppressing them. The theorem is, in effect, the permission slip for the entire informal practice of "the obvious diagram commutes".

There is a sharp limit to this convenience, and recognising it is half the value of the theorem. The same coherence statement is *false* for tricategories. The obstruction is real and detectable, and it marks dimension three as the first place where higher category theory becomes irreducibly weak. Understanding why dimension two is special — and three is not — is understanding the shape of the whole subject.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is just "a bicategory", so the source question is *when a problem secretly involves a weak two-dimensional structure whose coherence you would like to suppress.*

The first disguised source is **any monoidal category**, which is a one-object bicategory. The non-obvious step is to notice that a coherence question about $\otimes$ — "does this diagram of associativity isomorphisms commute?" — is an instance of bicategorical coherence, so it is answered uniformly rather than diagram-by-diagram. *Example problem:* show that in any monoidal category the two natural isomorphisms $((A \otimes B)\otimes C)\otimes D \to A \otimes(B \otimes(C \otimes D))$ built from associators are equal — immediate from coherence, painful by hand.

The second disguised source is **a category of "spans" or "relations" or "profunctors"**, where composition is by pullback or coend and is associative only up to canonical isomorphism. The non-obviousness is that these *look* like ordinary categories but are genuinely bicategories; coherence lets you treat them as strict for computation. *Example problem:* verify a triple composite of spans is well-defined up to canonical iso, then invoke coherence to manipulate it as if strictly associative.

The third disguised source is **a homotopy-coherent diagram** — a functor "up to coherent homotopy" indexed by a small category. Such a diagram lands in a bicategory of "weak functors", and coherence (in its strictification form) lets you replace it by a strictly commuting diagram. The non-obvious recognition is that "commutes up to specified homotopy satisfying higher constraints" *is* bicategorical data. *Example problem:* rectify a pseudo-functor into a strict functor.

**Targets (Output Amplification)**

Combine strictification with **a proof that is clean in the strict case**. The conclusion gives a biequivalent strict $2$-category; combined with a result you can prove easily *assuming* strictness, the further result is that the same result holds in the original weak bicategory, with all associators correctly inserted, *for free*. This is non-obvious leverage: it lets you prove weak statements by strict computations, which is how most bicategorical theorems are actually established.

Combine strictification with the **one-object specialisation**. The conclusion specialises to Mac Lane coherence; combined with the graphical calculus, the further result is that **string diagrams** in a monoidal category may be deformed by planar isotopy and the algebraic identity they encode still holds — because coherence guarantees the bracketing does not matter. This underlies all of categorical quantum mechanics and **TQFT** computation.

Combine the *failure* at dimension three with **the search for genuinely weak phenomena**. Knowing strictification fails for tricategories tells you *where to look* for irreducible higher structure: braidings, the interchange-of-$1$-cells obstruction, $\pi_3(S^2) = \mathbb{Z}$. The further result is a diagnostic: if a construction can be strictified it is "formal", and if it cannot, it carries genuine homotopical content. This is non-obvious because it turns a negative theorem into a tool for detecting real structure.

---

# Why Is It True

The cleanest reason is a Yoneda-style embedding. To strictify a bicategory $\mathcal{B}$, embed it into a strict $2$-category where composition is *honestly* associative — and the strictly associative operation par excellence is *composition of functors*. Concretely, send each object $A$ of $\mathcal{B}$ to the hom-functor it represents, and each $1$-cell to the induced (strict) functor between presheaf categories; composition of $1$-cells becomes composition of functors, which is strictly associative. The associator of $\mathcal{B}$, which measured the failure of strict associativity, is absorbed into a *natural isomorphism* that the embedding renders coherent. The image of $\mathcal{B}$ inside this strict $2$-category is biequivalent to $\mathcal{B}$. **The mechanism: replace the weakly-associative operation by composition of functors, which is strict, and let a Yoneda embedding carry the associator into bookkeeping that the strict structure already handles.**

Why does the same trick fail at dimension three? Because the embedding that strictifies needs the target's composition to be strictly associative *and* to have strictly interchanging compositions in all the relevant directions. At dimension two there is exactly one operation to strictify (horizontal composition of $1$-cells), and functor composition supplies a strict model. At dimension three there are *two* interacting weak operations whose interchange is itself only weak, and no strict structure models both simultaneously: the obstruction is precisely the **braiding** that Eckmann–Hilton produces (see [[Thm - The Interchange Law]]), which is genuinely non-trivial and cannot be made an identity. The deep statement is that the failure of strictification at dimension $3$ *is* the non-triviality of the braiding, equivalently the fact that $\pi_3(S^2) = \mathbb{Z} \ne 0$ — a piece of honest topology that no amount of rewriting can erase.

---

# What Makes This Hard

The hard part is not believing strictification holds — it is appreciating *why it must fail above dimension two*, which most first encounters skip. The non-obvious step is that "weakness" is not a single dial but accumulates: at dimension two there is one associator to absorb, and Yoneda absorbs it; at dimension three the associator-of-associators and the interchange-of-$1$-cells interact in a way that carries the topological content of $\pi_3(S^2)$, which is an invariant and cannot be trivialised. The common error is to assume, by analogy with dimension two, that all higher weakness is bookkeeping — leading to false "theorems" that every $n$-category strictifies. The correct picture is that *associativity* alone always strictifies, but the *interchange* of compositions does not from dimension three on.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Embed $\mathcal{B}$ into a strict $2$-category via a Yoneda-type construction so that weak composition becomes strict functor composition; show the embedding is a biequivalence; deduce that all coherence diagrams commute. For the limit, locate the obstruction at dimension three in the non-triviality of the braiding.

**Subgoal decomposition:**

1. **Build a strict model.** Construct a strict $2$-category $\mathrm{st}(\mathcal{B})$ whose $1$-cells are (strictly composable) functors, with a (pseudo)functor $\mathcal{B} \to \mathrm{st}(\mathcal{B})$.
   - *Hint:* Use the bicategorical Yoneda embedding $A \mapsto \mathcal{B}(-, A)$ into a $2$-category of (strict) functors; functor composition is strictly associative.
   - *Why needed:* Supplies the strict target into which the weak structure maps.

2. **The embedding is a biequivalence.** Show it is essentially surjective on $0$-cells and an [[Def - Equivalence of Categories|equivalence]] on each hom-category.
   - *Hint:* The bicategorical Yoneda lemma makes the hom-category maps equivalences, just as ordinary Yoneda is fully faithful.
   - *Why needed:* Biequivalence is what licenses transporting statements between $\mathcal{B}$ and the strict model.

3. **All coherence diagrams commute.** Deduce that any diagram of associators and unitors in $\mathcal{B}$ commutes.
   - *Hint:* In the strict model the corresponding diagram is built from identities, hence commutes trivially; transport back along the biequivalence.
   - *Why needed:* This is the usable form of the theorem.

4. **Locate the dimension-three obstruction.** Identify why the analogue fails for tricategories.
   - *Hint:* The interchange of $1$-cell compositions produces a braiding (Eckmann–Hilton); its non-triviality is detected by $\pi_3(S^2) = \mathbb{Z}$ and cannot be strictified.
   - *Why needed:* Delimits the theorem and prevents the false over-extension.

---

# Lemma Decomposition

> [!note]- Lemma 1: Functor composition is strictly associative
> **Statement:** In any $2$-category of categories, functors, and natural transformations, composition of functors satisfies $(H \circ G)\circ F = H \circ(G \circ F)$ on the nose, and identity functors are strict units.
>
> **Hint:** Composition of functors is composition of the underlying object- and morphism-assignments, which is set-function composition — strictly associative.
>
> **Why needed:** It provides the strict operation that the strictification replaces the weak composition by.
>
> > [!note]- Full proof
> > For functors $F : \mathcal{A} \to \mathcal{B}$, $G : \mathcal{B} \to \mathcal{C}$, $H : \mathcal{C} \to \mathcal{D}$, both $(H\circ G)\circ F$ and $H \circ(G\circ F)$ send an object $X$ to $H(G(F(X)))$ and a morphism $u$ to $H(G(F(u)))$ — equal as assignments. The identity functor leaves objects and morphisms unchanged, so it is a strict two-sided unit.

> [!note]- Lemma 2: The bicategorical Yoneda embedding is locally an equivalence
> **Statement:** For a bicategory $\mathcal{B}$, the assignment $A \mapsto \mathcal{B}(-, A)$ extends to a (pseudo)functor into a strict $2$-category of (weak) presheaves whose action on each hom-category $\mathcal{B}(A,B)$ is an [[Def - Equivalence of Categories|equivalence]] of categories.
>
> **Hint:** This is the bicategorical Yoneda lemma: representable presheaves recover the hom-categories up to equivalence, exactly as ordinary Yoneda recovers hom-sets up to bijection.
>
> **Why needed:** Local equivalence plus essential surjectivity is the definition of biequivalence, the conclusion of the theorem.
>
> > [!note]- Full proof
> > (Sketch, the full argument is the bicategorical Yoneda lemma.) The presheaf $2$-category $[\mathcal{B}^{op}, \mathbf{Cat}]$ of weak functors is a $2$-category in which composition is functor composition, hence strict by Lemma 1. The bicategorical Yoneda lemma gives, for each $A, B$, an equivalence $\mathcal{B}(A,B) \simeq [\mathcal{B}^{op},\mathbf{Cat}](\mathcal{B}(-,A), \mathcal{B}(-,B))$, natural in $A, B$. Thus the embedding is fully faithful on $2$-cells and essentially surjective on $1$-cells locally — an equivalence on each hom-category.

> [!note]- Lemma 3: Biequivalence transports coherence
> **Statement:** If $\mathcal{B}$ is biequivalent to a strict $2$-category $\mathcal{S}$, then every diagram of associators and unitors in $\mathcal{B}$ commutes.
>
> **Hint:** Push the diagram to $\mathcal{S}$, where the associators/unitors are identities so the diagram is trivially commutative, then pull back along the equivalence.
>
> **Why needed:** Converts "biequivalent to a strict structure" into the usable statement "all coherence diagrams commute".
>
> > [!note]- Full proof
> > A biequivalence induces, on each hom-category, a fully faithful functor. A coherence diagram in $\mathcal{B}$ maps to the corresponding diagram in $\mathcal{S}$; there the associators and unitors are identities, so both legs of the diagram are the same identity $2$-cell and the diagram commutes. Full faithfulness of the hom-category functor reflects this commutativity back to $\mathcal{B}$: two $2$-cells in $\mathcal{B}$ with equal images are equal. Hence the original diagram commutes.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — the strict target.** By Lemma 1, the $2$-category $[\mathcal{B}^{op}, \mathbf{Cat}]$ of weak presheaves on $\mathcal{B}$ with functor composition is a *strict* $2$-category: composition of $1$-cells (functors) is strictly associative and unital.
>
> **Step 1 — the embedding.** Define the (pseudo)functor $y : \mathcal{B} \to [\mathcal{B}^{op}, \mathbf{Cat}]$ on $0$-cells by $y(A) = \mathcal{B}(-, A)$, on $1$-cells $f : A \to B$ by post-composition $\mathcal{B}(-,A) \to \mathcal{B}(-,B)$, and on $2$-cells correspondingly. The associator of $\mathcal{B}$ is carried to a coherent natural isomorphism witnessing the pseudofunctoriality of $y$.
>
> **Step 2 — biequivalence.** By Lemma 2, $y$ is an [[Def - Equivalence of Categories|equivalence]] on each hom-category $\mathcal{B}(A,B)$. Restricting the target to the full image of $y$ (the sub-$2$-category $\mathcal{S}$ spanned by the representables) makes $y : \mathcal{B} \to \mathcal{S}$ essentially surjective on $0$-cells by construction. An essentially-surjective, locally-equivalence pseudofunctor is a **biequivalence**. Since $\mathcal{S}$ is a full sub-$2$-category of a strict $2$-category, $\mathcal{S}$ is strict.
>
> **Step 3 — coherence.** By Lemma 3, biequivalence with the strict $\mathcal{S}$ forces every diagram of associators and unitors in $\mathcal{B}$ to commute. This is the coherence conclusion.
>
> **Specialisation (Mac Lane).** Apply the theorem to a one-object bicategory; by [[Def - 2-Category and Bicategory|the one-object dictionary]] this is a [[Def - Monoidal Category|monoidal category]], and the conclusion becomes "every monoidal category is monoidally equivalent to a strict one", i.e. [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]. $\quad\blacksquare$
>
> **The dimension-three failure (no strictification).** For tricategories the embedding analogous to Step 1 must model *two* weak operations whose interchange is itself weak. Eckmann–Hilton (see [[Thm - The Interchange Law]]) shows the interchange of these operations produces a braiding $2$-cell; in the universal example this braiding is the generator of $\pi_3(S^2) \cong \mathbb{Z}$, a non-zero homotopy class. A strict $3$-category would force this braiding to be an identity, contradicting $\pi_3(S^2) \ne 0$. Hence not every tricategory is triequivalent to a strict $3$-category; the optimal statement is the Gordon–Power–Street theorem that every tricategory is triequivalent to a Gray-category. $\quad\square$

---

# Cross-Field Exercise Suggestions

**Tensor products of modules.** The bicategory of rings and bimodules has $N \ast M = N \otimes_B M$, associative only up to canonical isomorphism. Coherence licenses writing $P \otimes_C N \otimes_B M$ without brackets and treating it as strictly associative — a convenience used constantly in [[Def - Tensor Product of Modules|module theory]] and homological algebra. The exercise: verify the pentagon for iterated tensor products and then invoke coherence to drop all parentheses thereafter. Non-obvious because the strict-looking notation $\otimes$ hides genuinely weak associativity.

**Braided monoidal categories and knot invariants.** A braided monoidal category is what you get from the "once-degenerate" obstruction to strictification; its braiding $c_{A,B} : A \otimes B \to B \otimes A$ is exactly the non-strictifiable datum, and it produces representations of the braid group, hence knot and link invariants (Jones polynomial). The exercise: show the braiding satisfies the hexagon (Yang–Baxter) and cannot be turned into an identity. Non-obvious because it ties the *failure* of strictification directly to a computable topological invariant.

**Rectification of homotopy-coherent diagrams.** A diagram of spaces commuting only up to coherent homotopy is a pseudofunctor into a bicategory of spaces; strictification (rectification) replaces it by a strictly commuting diagram with the same homotopy colimit. The exercise: rectify a homotopy-coherent triangle. Non-obvious because it is the everyday tool of homotopy theory — "make the diagram strictly commute without changing its homotopy type" — and it is exactly this theorem in action.

---

# Bridges

- **[[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]** — the one-object case. A [[Def - Monoidal Category|monoidal category]] is a one-object bicategory, so strictification of bicategories specialises to "every monoidal category is monoidally equivalent to a strict one", and "all coherence diagrams commute" becomes Mac Lane's statement that any diagram built from $\alpha, \lambda, \rho$ commutes. The proofs are the same Yoneda embedding, with $\otimes$ replaced by horizontal composition.

- **[[Thm - The Interchange Law|The interchange law and Eckmann–Hilton]]** — the source of the dimension-three obstruction. The braiding that makes tricategories non-strictifiable is produced by the Eckmann–Hilton argument applied to the two interchanging $1$-cell compositions; its non-triviality ($\pi_3(S^2) = \mathbb{Z}$) is what coherence cannot remove. So the interchange law both *holds strictly* (an axiom untouched by strictification) and *generates the obstruction* one dimension up.

- **The homotopy hypothesis and rectification** — strictification of $n$-categories is the algebraic shadow of the topological fact that some homotopy-coherent structures rectify and some do not. For $\infty$-*groupoids* (spaces) everything rectifies in the sense that any homotopy type has a strict simplicial model ($\mathrm{Sing}\,X$); for general $\infty$-*categories* the analogue of coherence is built into the [[Def - Quasi-Category|quasi-category]] formalism, which sidesteps strictification entirely by encoding coherence as horn-filling rather than as chosen isomorphisms.

---

# Unlocked by This

> [!tip] Gray-Categories and the Tricategorical Coherence Theorem *(from Higher Category Theory)*
> The optimal three-dimensional result, every tricategory is triequivalent to a **Gray-category** (strict except for a weak interchange of $1$-cells), is the precise measure of irreducible weakness at dimension three. It is the entry point to the coherence theory of $(\infty, n)$-categories.

> [!tip] The Coherence Theorem as a Tool for ∞-Categories *(from Lurie's Higher Algebra)*
> The lesson that hand-managed coherence is hopeless above dimension two is exactly why [[Def - Quasi-Category|quasi-categories]] win: they encode all coherence uniformly as horn-filling, never requiring an explicit associator. Strictification's failure is the motivation for the simplicial approach of §H.4–H.5.
