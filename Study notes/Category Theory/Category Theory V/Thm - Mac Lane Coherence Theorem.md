---
type: theorem
subject: category-theory
prereqs:
  - "Def - Monoidal Category"
  - "Def - Natural Transformation"
  - "Def - Functor"
  - "Def - Equivalence of Categories"
tags: [category-theory, foundations]
---

# Notation

Throughout, $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ is a [[Def - Monoidal Category|monoidal category]]: associator $\alpha_{A,B,C} : (A\otimes B)\otimes C \to A\otimes(B\otimes C)$, left unitor $\lambda_A : I \otimes A \to A$, right unitor $\rho_A : A \otimes I \to A$. A **formal diagram** is one whose vertices are iterated tensor products of objects (with various bracketings and inserted copies of $I$) and whose edges are composites of identities, tensors $f \otimes g$, and components of $\alpha, \lambda, \rho$ and their inverses. A monoidal category is **strict** if $\alpha, \lambda, \rho$ are all identities. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

---

# Statement

> **Theorem (Mac Lane coherence — "all diagrams commute").** In any [[Def - Monoidal Category|monoidal category]], every formal diagram built from the associator $\alpha$, the unitors $\lambda, \rho$, their inverses, identities, and the tensor functor $\otimes$ commutes. Equivalently: between any two iterated tensor products of the same sequence of objects (differing only in bracketing and in inserted unit factors), there is a *unique* canonical isomorphism composed of associators and unitors.

> **Theorem (Mac Lane coherence — strictification form).** Every monoidal category is monoidally equivalent to a **strict** monoidal category. That is, there is a strict monoidal category $\mathcal{C}_{\mathrm{str}}$ and a [[Def - Equivalence of Categories|monoidal equivalence]] $\mathcal{C} \simeq \mathcal{C}_{\mathrm{str}}$.

The two forms are equivalent: "all formal diagrams commute" is exactly what is needed for the strictification functor to be well-defined, and conversely strictness makes every formal diagram trivially commute.

---

# Motivation

The coherence theorem is the permission slip that makes the whole calculus of [[Def - Monoidal Category|monoidal categories]] usable. As soon as the tensor product is associative only *up to* the isomorphism $\alpha$, a tower $A_1 \otimes \cdots \otimes A_n$ has many bracketings, and you reach them from one another by inserting associators. The terror is ambiguity: if two different chains of associators connecting the same pair of bracketings gave *different* isomorphisms, then "the canonical map from this bracketing to that one" would be meaningless, and every computation in a monoidal category would carry an unmanageable bookkeeping of which associators you happened to apply. Coherence dispels the terror by proving the chains always agree.

The practical upshot is that you may **drop the parentheses**. Writing $A \otimes B \otimes C$ without specifying a bracketing is legitimate, because all bracketings are *canonically and uniquely* the same. Likewise you may silently delete unit factors, treating $I \otimes A$ and $A$ as identical. This is exactly what everyone does when manipulating tensor products of vector spaces, modules, or Hilbert spaces, and what string-diagram and tensor-network notations rely on: the diagram does not record bracketing, and coherence is the theorem that says it need not.

The strictification form gives the same permission in a different package: not only *may* you pretend $\otimes$ is strictly associative, you may actually *replace* your category by an equivalent one where it is. So no generality is lost by proving theorems for strict monoidal categories — the slogan "a monad is a monoid in the strict monoidal category of endofunctors" is rigorous precisely because the endofunctor category happens to be strict, and coherence guarantees the general weak case reduces to it.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a monoidal category" — the pentagon and triangle axioms. The disguised sources are situations where those two axioms hold without being checked directly.

A first disguised source is **a category with finite [[Def - Product and Coproduct|products]]**. Here $\otimes = \times$, $I$ is the terminal object, and the associator and unitors are the unique isomorphisms commuting with projections. The pentagon and triangle hold automatically by the universal property — uniqueness of maps into a product forces every formal diagram to commute. The non-obvious step is that products are monoidal *for free*, so coherence applies without verifying anything. *Example problem:* deduce that all reassociation isomorphisms of $A \times B \times C \times D$ agree, directly from the universal property.

A second disguised source is **a category with a universal bilinear tensor**. For [[Def - Tensor Product of Vector Spaces|vector spaces]] or [[Def - Tensor Product of Modules|modules]], the associator comes from the universal property of $\otimes$ as the classifier of bilinear maps. The pentagon holds because both routes classify the same multilinear map. The non-obvious bridge is that "universal multilinear object" implies coherence. *Example problem:* show the associator $(U \otimes V) \otimes W \cong U \otimes (V \otimes W)$ from the universal property of multilinear maps and conclude all bracketings of a tensor of modules agree.

A third disguised source is **a strict monoidal category**, where $\alpha, \lambda, \rho$ are identities. Coherence is trivially true (every formal diagram is built from identities), and the strictification form lets you *transport* this triviality to weak categories. The non-obvious recognition is that $([\mathcal{C},\mathcal{C}], \circ, 1)$ is strict, so monads live in a category where coherence is free. *Example problem:* explain why no associators clutter the monad axioms.

**Targets (Output Amplification)**

The conclusion is "all formal diagrams commute / every monoidal category strictifies." Combined with other facts it does much more.

Combine with **a [[Def - Monoid in a Monoidal Category|monoid object]] computation**. Coherence lets you suppress $\alpha, \lambda, \rho$ when verifying the monoid associativity and unit axioms, so checking "this is a [[Def - Ring|ring]]" or "this is a monad" never drowns in structural isomorphisms. The further result is that the monoid axioms in any monoidal category reduce to their strict form, which is why "monoid in $(\mathbf{Ab},\otimes)$ is a ring" is a clean computation.

Combine with **string-diagram calculus**. Coherence is precisely what validates planar string diagrams: a diagram records only the series/parallel structure, not bracketing, and coherence says bracketing was irrelevant. The further result, when the category is also braided or symmetric, is the validity of *braided* and *symmetric* string diagrams (with crossings), underpinning quantum-information and **TQFT** computations.

Combine with **functoriality of structure**. Once strictified, a monoidal functor (e.g. a **TQFT** $\mathrm{Cob}_n \to \mathbf{Vect}_k$) can be defined without tracking coherence isomorphisms, and proofs about it simplify. The further result is that the entire theory of monoidal functors and natural transformations can be developed in the strict setting and transported back.

---

# Why Is It True

The intuition is that the pentagon and triangle are not two random axioms — they are exactly the *generators* of all coherence, in the sense of a presentation. Think of the different bracketings of $A_1 \otimes \cdots \otimes A_n$ as the vertices of a graph (the associahedron), with associators as edges. A priori, two paths between the same vertices might give different isomorphisms. The pentagon axiom says that the *smallest non-trivial* such pair of paths — the two ways to reassociate four factors — agree. The miracle is that *every* larger coherence reduces to the pentagon: any two paths in the associahedron can be connected by a sequence of pentagon-shaped faces, so if all pentagons commute, all paths agree. The triangle axiom plays the same role for unit insertions: it is the one relation that, once imposed, forces every way of deleting unit factors to agree.

**The single mechanism: the pentagon and triangle are a complete set of relations for the "reassociation and unit" rewriting system, so once they hold, every reassociation has a unique normal form and any two reassociations are equal.** This is why the proof connects to **proof theory**: it is a normalization / confluence result. The canonical isomorphism between two bracketings is the unique rewriting between two terms to a common normal form, and the pentagon/triangle are the critical-pair confluences that guarantee the rewriting is well-defined — the same shape of argument as Gentzen's cut-elimination and Newman's lemma.

For the strictification form, the mechanism is to replace each object by the "list of its tensor factors with a chosen normal-form bracketing." Tensor of normal forms is concatenation, which is strictly associative; coherence guarantees the resulting category is monoidally equivalent to the original, because the chosen normal-form isomorphisms are unique and compatible.

---

# What Makes This Hard

The difficulty is conceptual, not computational: the theorem is *easy to state imprecisely* ("all diagrams commute") and the precision is where the subtlety lives. Two traps. First, "all diagrams commute" is **false** if read naïvely — a diagram involving *specific* non-structural morphisms need not commute; only **formal** diagrams (built solely from $\alpha, \lambda, \rho, \otimes$, identities) are guaranteed to. People over-apply the theorem to diagrams containing actual maps of the category. Second, the proof is genuinely non-trivial and is usually black-boxed: it requires either the associahedron/normal-form combinatorics or a clever induction, and Mac Lane's original argument quietly uses ideas from proof theory. The common error in *using* the theorem is forgetting that the braiding is **not** covered — coherence for symmetric monoidal categories is a separate (and subtler) statement, because a braided diagram can fail to commute even when all associators are suppressed (a double braid $\beta^2$ need not be the identity).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the strictification form, from which the "all formal diagrams commute" form follows. Build a strict monoidal category $\mathcal{C}_{\mathrm{str}}$ whose objects are finite lists of objects of $\mathcal{C}$ and whose tensor is concatenation; define a monoidal equivalence $\mathcal{C} \simeq \mathcal{C}_{\mathrm{str}}$ using the unique normal-form isomorphisms; coherence is exactly the well-definedness of these isomorphisms, which reduces to the pentagon and triangle.

**Subgoal decomposition:**

1. **Define $\mathcal{C}_{\mathrm{str}}$.** Objects = finite sequences $(A_1, \dots, A_n)$ of objects of $\mathcal{C}$; tensor = concatenation; unit = empty sequence.
   - *Hint:* Concatenation is strictly associative and unital, so $\mathcal{C}_{\mathrm{str}}$ is strict.
   - *Why needed:* It is the strict model we map to.

2. **Define the evaluation functor $E : \mathcal{C}_{\mathrm{str}} \to \mathcal{C}$.** Send $(A_1,\dots,A_n)$ to the left-bracketed tensor $((\cdots(A_1 \otimes A_2)\otimes\cdots)\otimes A_n)$.
   - *Hint:* Choose one normal-form bracketing once and for all.
   - *Why needed:* It carries the strict model back into $\mathcal{C}$.

3. **Define the canonical isomorphisms between bracketings.** For any two bracketings of the same sequence, take any chain of associators connecting them.
   - *Hint:* Different chains give the *same* isomorphism — this is the content to prove.
   - *Why needed:* These isomorphisms make $E$ a monoidal equivalence.

4. **Reduce well-definedness to the pentagon and triangle.** Show any two chains of associators are connected by pentagon faces, and any two unit-deletions by triangle faces.
   - *Hint:* This is the associahedron / confluence argument.
   - *Why needed:* It is the heart of coherence.

5. **Conclude.** $E$ is a monoidal equivalence, so $\mathcal{C} \simeq \mathcal{C}_{\mathrm{str}}$ is strict; transporting back, every formal diagram in $\mathcal{C}$ commutes.
   - *Hint:* A formal diagram in $\mathcal{C}$ becomes a diagram of identities in $\mathcal{C}_{\mathrm{str}}$.
   - *Why needed:* It delivers both forms of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The list category is strict monoidal
> **Statement:** Let $\mathcal{C}_{\mathrm{str}}$ have objects finite sequences of objects of $\mathcal{C}$, morphisms suitably defined, tensor = concatenation, unit = empty sequence. Then $\mathcal{C}_{\mathrm{str}}$ is a strict monoidal category.
>
> **Hint:** Concatenation of lists is associative and unital on the nose.
>
> **Why needed:** It provides the strict target of the equivalence.
>
> > [!note]- Full proof
> > For sequences $\mathbf{A} = (A_1,\dots,A_m)$, $\mathbf{B}$, $\mathbf{C}$, concatenation satisfies $(\mathbf{A}\frown\mathbf{B})\frown\mathbf{C} = \mathbf{A}\frown(\mathbf{B}\frown\mathbf{C})$ as sequences (both are the concatenation of all entries in order), and the empty sequence is a two-sided unit, all as literal equalities. The morphisms are defined so that the hom-set $\mathcal{C}_{\mathrm{str}}(\mathbf{A},\mathbf{B})$ matches $\mathcal{C}(E\mathbf{A}, E\mathbf{B})$ for the evaluation $E$ below; composition is inherited. Hence $\otimes = \frown$ is a strictly associative, strictly unital tensor: $\mathcal{C}_{\mathrm{str}}$ is strict monoidal.

> [!note]- Lemma 2: Any two associator chains between the same bracketings agree (pentagon confluence)
> **Statement:** Given two bracketings of a sequence $(A_1,\dots,A_n)$, any two composites of associators connecting them are equal.
>
> **Hint:** Induct on $n$; the inductive step expresses any two reassociation paths as a composite of pentagon faces.
>
> **Why needed:** This is the core coherence statement for associativity; it makes the canonical isomorphisms well-defined.
>
> > [!note]- Full proof
> > For $n \leq 3$ there is at most one associator and nothing to prove. For $n = 4$ the statement is exactly the pentagon axiom, which equates the two paths from $((AB)C)D$ to $A(B(CD))$. For general $n$, the bracketings of $(A_1,\dots,A_n)$ are the vertices of the associahedron $K_{n-1}$, whose two-dimensional faces are pentagons (from four-factor reassociations) and squares (from naturality of $\alpha$, i.e. associators applied to disjoint groups commute). Any two edge-paths between fixed vertices of a simply connected polytope are homotopic through its two-faces; since each pentagon face commutes (pentagon axiom) and each square face commutes (bifunctoriality/naturality of $\otimes$ and $\alpha$), the two paths give equal composites. By induction on $n$ the result holds for all bracketings.

> [!note]- Lemma 3: The evaluation functor is a monoidal equivalence
> **Statement:** The functor $E : \mathcal{C}_{\mathrm{str}} \to \mathcal{C}$ sending a sequence to its (normal-form) tensor is an equivalence of categories, and it is monoidal.
>
> **Hint:** $E$ is fully faithful by construction of the hom-sets, and essentially surjective since every object is the singleton sequence; the monoidal structure maps are the canonical isomorphisms of Lemma 2.
>
> **Why needed:** It establishes $\mathcal{C} \simeq \mathcal{C}_{\mathrm{str}}$ as monoidal categories, the strictification.
>
> > [!note]- Full proof
> > Fully faithful: $\mathcal{C}_{\mathrm{str}}(\mathbf{A},\mathbf{B})$ was *defined* as $\mathcal{C}(E\mathbf{A}, E\mathbf{B})$, so $E$ is a bijection on hom-sets. Essentially surjective: each object $A$ is $E(A)$ for the one-element sequence $(A)$. So $E$ is an equivalence. The monoidal coherence data — natural isomorphisms $E(\mathbf{A}) \otimes E(\mathbf{B}) \cong E(\mathbf{A}\frown\mathbf{B})$ — are the canonical reassociation isomorphisms, which are well-defined by Lemma 2 and satisfy the monoidal-functor axioms because those axioms are again instances of pentagon/triangle. Hence $E$ is a monoidal equivalence.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ be a monoidal category.
>
> **Step 0 — reduce to strictification.** It suffices to prove $\mathcal{C}$ is monoidally equivalent to a strict monoidal category; the "all formal diagrams commute" form then follows by transporting any formal diagram across the equivalence, where it becomes a diagram of identities.
>
> **Step 1 — build the strict model.** By Lemma 1, the list category $\mathcal{C}_{\mathrm{str}}$ (objects = finite sequences of objects of $\mathcal{C}$, tensor = concatenation, unit = empty sequence) is strict monoidal, with hom-sets defined by $\mathcal{C}_{\mathrm{str}}(\mathbf{A},\mathbf{B}) := \mathcal{C}(E\mathbf{A}, E\mathbf{B})$ for the evaluation $E$ below.
>
> **Step 2 — coherence of associators.** By Lemma 2, any two composites of associators between two bracketings of the same sequence are equal; this uses the pentagon axiom (the four-factor case and its iterations) and naturality of $\otimes$. The analogous statement for unit insertions uses the triangle axiom together with Mac Lane's deductions $\lambda_I = \rho_I$ and the compatibility of $\lambda, \rho$ with $\alpha$. Hence between any two bracketings (with inserted units) there is a *unique* canonical isomorphism built from $\alpha, \lambda, \rho$.
>
> **Step 3 — the monoidal equivalence.** By Lemma 3, the evaluation functor $E : \mathcal{C}_{\mathrm{str}} \to \mathcal{C}$ is a monoidal equivalence, its coherence isomorphisms being the canonical isomorphisms of Step 2. Therefore $\mathcal{C} \simeq \mathcal{C}_{\mathrm{str}}$ as monoidal categories, and $\mathcal{C}_{\mathrm{str}}$ is strict.
>
> **Step 4 — conclude.** A formal diagram in $\mathcal{C}$ — built only from $\alpha, \lambda, \rho, \otimes$, identities — maps under the equivalence to a formal diagram in $\mathcal{C}_{\mathrm{str}}$, all of whose structural morphisms are identities, hence commutes; transporting back, the original commutes. So every formal diagram in $\mathcal{C}$ commutes, and every monoidal category strictifies. $\blacksquare$
>
> (Mac Lane's original proof of Step 2 proceeds by a direct induction whose bookkeeping is, surprisingly, governed by the same normalization machinery as Gentzen's cut-elimination; the associahedron picture above is the modern repackaging.)

---

# Cross-Field Exercise Suggestions

**Tensor products of modules and the absence of bracketing.** For [[Def - Module|modules]] over a commutative [[Def - Ring|ring]], deduce from coherence that $M_1 \otimes_R \cdots \otimes_R M_n$ is well-defined without specifying a bracketing, and that this is the universal object classifying $n$-linear maps. The exercise is to see the universal property *prove* the pentagon, then invoke coherence to drop parentheses.

**String diagrams in quantum information.** A quantum circuit is a morphism in a symmetric monoidal category, and its string diagram records only which wires are tensored (parallel) and which composed (series). The exercise is to argue that coherence is exactly the statement that the diagram's *bracketing* of parallel wires is immaterial, so two circuits with the same diagram are equal — the foundation of diagrammatic reasoning in quantum computing.

**Strictifying the endofunctor category.** Verify that $([\mathcal{C},\mathcal{C}], \circ, 1)$ is already strict, so no coherence isomorphisms appear in the [[Def - Monad and Comonad|monad]] axioms, and contrast with $(\mathbf{Vect}_k, \otimes)$, which is weak but strictifies. The exercise clarifies why the slogan "a monad is a monoid in endofunctors" is literally rather than approximately true.

---

# Bridges

- **[[Def - Monoidal Category|Monoidal category]]** — the source of the structure. Coherence is the theorem that makes the pentagon and triangle axioms *sufficient*: those two relations force every other coherence, which is why the definition needs only them and not an infinite list of commuting diagrams.

- **[[Def - Monoid in a Monoidal Category|Monoid objects]]** — the immediate beneficiary. Coherence lets the monoid associativity and unit axioms be checked with $\alpha, \lambda, \rho$ suppressed, so identifying [[Def - Ring|rings]], $k$-algebras, and [[Def - Monad and Comonad|monads]] as monoid objects is a clean computation rather than a fight with structural isomorphisms.

- **Proof theory and normalization** — the surprising kin. The coherence proof is a confluence/normalization result: the canonical isomorphism between two bracketings is the unique rewriting to a common normal form, and the pentagon/triangle are the critical-pair confluences. This is the same mathematics as Gentzen's cut-elimination and Newman's lemma, an instance of the **Curry–Howard** circle of ideas relating proofs, programs, and rewriting.

- **Higher coherence and the associahedron** — the upward generalization. The associahedron $K_n$ whose faces encode the pentagon recurs in operad theory and homotopy theory; the $A_\infty$-structures of topology are "monoids coherently associative up to higher homotopy," with Mac Lane's pentagon the first in an infinite tower of coherence cells.

---

# Unlocked by This

> [!tip] String-Diagram Calculus and Graphical Reasoning *(from Applied Category Theory)*
> Coherence validates string diagrams: a morphism in a (braided/symmetric) monoidal category is determined by its diagram up to the structural isomorphisms coherence trivializes. This is the computational engine of **TQFT**, quantum information, and **compositional game theory**.

> [!tip] A_infinity and E_n Structures *(from Higher Algebra)*
> Weakening "coherently associative" to "associative up to coherent higher homotopy" gives $A_\infty$- and $E_n$-algebras, governed by the associahedra and little-cubes **operads** — the homotopical refinement of monoid objects that drives derived and higher algebra.

> [!tip] Coherence for Symmetric and Braided Categories *(from Quantum Algebra)*
> The braided analogue of coherence is subtler: not all braided diagrams commute (a double braid is a non-trivial automorphism), and the resulting failure is exactly what makes braided categories detect knots and host quantum groups.
