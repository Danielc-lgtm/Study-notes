---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]] with a functor $\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ (the **tensor product**) and a distinguished object $I$ (the **unit object**). We write $A \otimes B$ for the tensor of objects and $f \otimes g$ for the tensor of morphisms. The structural [[Def - Natural Transformation|natural isomorphisms]] are the **associator** $\alpha_{A,B,C} : (A \otimes B) \otimes C \to A \otimes (B \otimes C)$, the **left unitor** $\lambda_A : I \otimes A \to A$, the **right unitor** $\rho_A : A \otimes I \to A$, and (when present) the **braiding** $\beta_{A,B} : A \otimes B \to B \otimes A$. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

This is a compound page: it defines three nested notions — **monoidal**, **braided monoidal**, and **symmetric monoidal** category — because each is obtained from the previous by adding one piece of structure (a braiding) or one axiom ($\beta^2 = 1$), and the distinctions between them carry real mathematical content.

---

# Axiom Motivation

We already have a notion of *strict* monoidal category: a [[Def - Monoid in a Monoidal Category|monoid]] in $\mathbf{Cat}$, i.e. a category with an associative tensor functor and a unit object, where $(A \otimes B) \otimes C$ and $A \otimes (B \otimes C)$ are *equal* and $I \otimes A = A = A \otimes I$ on the nose. The trouble is that almost no naturally occurring tensor product is strictly associative. The Cartesian product of sets is the canonical offender: $(A \times B) \times C$ consists of pairs $((a,b),c)$, while $A \times (B \times C)$ consists of pairs $(a,(b,c))$, and these are *not the same set* — they are merely canonically isomorphic. The same holds for the [[Def - Tensor Product of Vector Spaces|tensor product of vector spaces]], for direct sums, for the smash product, and for nearly every monoidal-looking operation in mathematics. Insisting on strict equality would exclude all of them.

The fix is to replace equality by *coherent isomorphism*. We do not demand $(A \otimes B) \otimes C = A \otimes (B \otimes C)$, only that there be a natural isomorphism $\alpha_{A,B,C}$ between them; likewise unitors $\lambda_A : I \otimes A \cong A$ and $\rho_A : A \otimes I \cong A$ instead of equalities. But this raises a new danger. Once associativity holds only up to isomorphism, a long tensor product $A \otimes B \otimes C \otimes D$ can be re-bracketed in several ways, and different *sequences* of associator-applications connect the same two bracketings. If two such sequences disagreed, "the" canonical isomorphism would be ill-defined and the structure would be useless. We must require that all such sequences *agree*. The minimal condition that guarantees this is **Mac Lane's pentagon axiom**: the two ways of re-associating $((A\otimes B)\otimes C)\otimes D$ to $A\otimes(B\otimes(C\otimes D))$ — one going "around the top" through $(A\otimes B)\otimes (C \otimes D)$, the other "around the bottom" through three single moves — must coincide.

Why is the pentagon *enough*? This is the content of [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]: the pentagon (for re-bracketing) together with the **triangle axiom** (for how the unitors interact with the associator at the unit object) force *every* diagram of associators and unitors to commute. Drop the pentagon and you can build a five-object diagram of associators that fails to commute, so re-bracketing becomes ambiguous. Drop the triangle and the unit isomorphisms become incompatible with associativity — for instance $\lambda_I$ and $\rho_I : I \otimes I \to I$ could differ, so "the" way to delete a unit factor would be ambiguous. Each axiom kills a specific incoherence; together they are exactly the coherence the construction needs.

Now the braiding. In $(\mathbf{Set}, \times)$ and $(\mathbf{Vect}_k, \otimes)$ there is also a natural isomorphism $A \otimes B \cong B \otimes A$ swapping the factors. This is *extra* structure — composition of endofunctors, $([\mathcal{C},\mathcal{C}], \circ)$, has no such swap, since $F \circ G \not\cong G \circ F$ in general. When a swap $\beta_{A,B} : A \otimes B \to B \otimes A$ exists and is coherent with the associator, we call $\mathcal{C}$ **braided**. Coherence here is two **hexagon axioms**, which say that braiding past a tensor $B \otimes C$ agrees with braiding past $B$ and then past $C$ (with the associators inserted to make the types match). Drop the hexagons and the braiding need not interact predictably with re-bracketing.

Finally, symmetry. A braiding gives a chosen isomorphism $A \otimes B \to B \otimes A$, but braiding twice, $\beta_{B,A} \circ \beta_{A,B} : A \otimes B \to A \otimes B$, need not be the identity — it could be a non-trivial automorphism. When it *is* the identity for all $A, B$, the braiding is a **symmetry** and $\mathcal{C}$ is **symmetric monoidal**. The distinction is not pedantic: it is exactly the difference between two-dimensional and three-dimensional swapping. In a braided (non-symmetric) category the two strands of $\beta_{A,B}$ cross in a definite over/under sense, like a knot; swapping back, $\beta^2$, is a full twist, not trivial. In a symmetric category strands can pass through each other and the twist undoes. This is why braided categories are the home of knot invariants and quantum groups, while symmetric ones are the home of ordinary algebra and **TQFT**.

---

# The Definition

A **monoidal category** is a category $\mathcal{C}$ equipped with:
- a functor $\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$,
- an object $I \in \mathcal{C}$,
- natural isomorphisms $\alpha_{A,B,C} : (A \otimes B) \otimes C \to A \otimes (B \otimes C)$, $\lambda_A : I \otimes A \to A$, $\rho_A : A \otimes I \to A$,

such that the **pentagon** and **triangle** diagrams commute:

**Pentagon** — the two routes from $((A\otimes B)\otimes C)\otimes D$ to $A\otimes(B\otimes(C\otimes D))$ agree:
$$\alpha_{A,B,C\otimes D} \circ \alpha_{A\otimes B, C, D} \;=\; (1_A \otimes \alpha_{B,C,D}) \circ \alpha_{A, B\otimes C, D} \circ (\alpha_{A,B,C} \otimes 1_D).$$

**Triangle** — the unitors are compatible with the associator:
$$(1_A \otimes \lambda_B) \circ \alpha_{A,I,B} \;=\; \rho_A \otimes 1_B \qquad (\text{as } (A\otimes I)\otimes B \to A \otimes B).$$

A **braided monoidal category** is a monoidal category with a natural isomorphism $\beta_{A,B} : A \otimes B \to B \otimes A$ satisfying the two **hexagon** axioms, which (suppressing associators by coherence) read
$$\beta_{A, B\otimes C} = (1_B \otimes \beta_{A,C}) \circ (\beta_{A,B} \otimes 1_C), \qquad \beta_{A \otimes B, C} = (\beta_{A,C} \otimes 1_B) \circ (1_A \otimes \beta_{B,C}).$$

A **symmetric monoidal category** is a braided monoidal category in which the braiding is its own inverse:
$$\beta_{B,A} \circ \beta_{A,B} = 1_{A \otimes B} \qquad \text{for all } A, B.$$

A monoidal category is **strict** if $\alpha, \lambda, \rho$ are all identities (so $\otimes$ is associative and unital on the nose).

---

# Categorical / Structural Definition

The structural slogan is: **a monoidal category is a "categorified monoid," and a strict one is exactly a [[Def - Monoid in a Monoidal Category|monoid]] in $\mathbf{Cat}$.** A monoid is a set with an associative unital binary operation; a strict monoidal category is a category with an associative unital binary *functor* — the same definition with "set" promoted to "category" and "function" to "functor." The non-strict version weakens the associativity and unit equations to coherent isomorphisms, which is the generic behaviour of categorified structures: equations between objects become natural isomorphisms, and coherence axioms (pentagon, triangle, hexagons) ensure these isomorphisms are unambiguous.

Equivalently, a monoidal category is a **one-object [[Def - 2-Category and Bicategory|bicategory]]**: a bicategory with a single $0$-cell $\star$ has a single hom-category $\mathcal{B}(\star,\star)$, whose objects are the monoidal category's objects, whose composition is $\otimes$, and whose associator and unitors are the bicategory's coherence isomorphisms. This is the cleanest statement of "monoidal = one object up a dimension," and it is the bridge to higher category theory: braided monoidal categories are one-object monoidal $2$-categories, symmetric ones are one-object monoidal $3$-categories, and so on up the **periodic table** of $n$-categories.

---

# Relate to Other Fields / Compression

Monoidal categories are the mathematics of **resources that combine in parallel**. The tensor $A \otimes B$ is "$A$ and $B$ side by side," composition $g \circ f$ is "$f$ then $g$ in series," and a morphism $A \to B$ is a "process turning $A$ into $B$." This two-dimensional algebra — series and parallel — is exactly what string diagrams depict, and it is the formal substrate of quantum information, **TQFT**, Petri nets, electrical circuits, and **compositional game theory**.

**True name:** a monoidal category is a category with a **coherently associative, unital "and"** — a way to put objects side by side that is associative and unital up to canonical isomorphism. The braiding is "the right to swap two things," and symmetry is "swapping twice does nothing." Operationally, when you see a tensor product you should ask three questions in order: is it coherent (pentagon/triangle — almost always yes, by [[Thm - Mac Lane Coherence Theorem|Mac Lane]]), can you swap factors (braided?), and does swapping twice undo (symmetric?).

The compression unifying this chapter: ordinary [[Def - Monoid in a Monoidal Category|monoids]], [[Def - Ring|rings]], $k$-algebras, and [[Def - Monad and Comonad|monads]] are *the same kind of object* — a monoid — living in different monoidal categories. The monoidal category is the ambient world; the monoid object is the algebraic structure.

---

# Examples / Corollaries

**Is an instance (symmetric) — $(\mathbf{Set}, \times, 1)$.** The Cartesian product, with the one-point set as unit. The associator is the canonical bijection $((a,b),c) \mapsto (a,(b,c))$, the unitors delete the point coordinate, and the braiding $(a,b) \mapsto (b,a)$ is a symmetry. This is the prototype of a Cartesian monoidal category, where $\otimes$ is the categorical [[Def - Product and Coproduct|product]].

**Is an instance (symmetric) — $(\mathbf{Vect}_k, \otimes_k, k)$.** The [[Def - Tensor Product of Vector Spaces|tensor product]] of $k$-vector spaces, with the ground field $k$ as unit. The associator and unitors come from the universal property of the tensor product; the braiding $v \otimes w \mapsto w \otimes v$ is a symmetry. Monoids here are unital associative $k$-algebras.

**Is an instance (symmetric) — $(\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z})$ and $(\mathbf{Mod}_R, \otimes_R, R)$.** The [[Def - Tensor Product of Modules|tensor product of modules]] over a commutative [[Def - Ring|ring]] $R$, with $R$ as unit; symmetric for commutative $R$. Monoids in $(\mathbf{Ab}, \otimes)$ are rings; monoids in $(\mathbf{Mod}_R, \otimes_R)$ are $R$-algebras (see [[Ex - Monoids in Vect are algebras and in Ab are rings]]).

**Is an instance (symmetric) — $(\mathbf{Cat}, \times, \mathbf{1})$.** Categories with the product category as tensor and the terminal category as unit. A monoid here is a strict monoidal category, closing the loop with the structural definition.

**Is an instance but NOT symmetric — $([\mathcal{C},\mathcal{C}], \circ, 1_{\mathcal{C}})$.** The [[Def - Functor Category|endofunctor category]] with composition as tensor and the identity functor as unit. This is strictly associative and unital, hence strict monoidal. But it is **not** braided, let alone symmetric: there is no natural isomorphism $F \circ G \cong G \circ F$ — composing "free group" then "power set" is genuinely different from the reverse. Monoids here are exactly [[Def - Monad and Comonad|monads]]; the lack of symmetry is why monads do not commute.

**Is NOT an instance — a tensor with no coherent associator.** Equip $\mathbf{Set}$ with the "operation" $A \boxtimes B = A$ (project to the first factor). This is functorial but admits no unit object making it unital, and no associator can repair the unit failure — so $(\mathbf{Set}, \boxtimes)$ is not monoidal. The example shows that having a binary functor is far from enough; the unit and coherent isomorphisms are essential.

**Calibration check.** Verify that in $(\mathbf{Set}, \times)$ the associator is the unique bijection commuting with all three projections (this is the universal property of the product at work); check that the braiding on $(\mathbf{Vect}_k, \otimes)$ squares to the identity; and confirm that $([\mathcal{C},\mathcal{C}], \circ)$ has no braiding by exhibiting two endofunctors of $\mathbf{Set}$ with $F\circ G \not\cong G \circ F$.

---

# Unlocked by This

> [!tip] Monoid Objects: Rings, Algebras, and Monads *(from this chapter)*
> Inside any monoidal category you can define a [[Def - Monoid in a Monoidal Category|monoid object]]. Specializing the ambient category gives rings, $k$-algebras, $R$-algebras, and — in the endofunctor category — monads, unifying §5.1 and §5.4.

> [!tip] Topological Quantum Field Theory *(from Mathematical Physics)*
> A **TQFT** is a symmetric monoidal functor $\mathrm{Cob}_n \to \mathbf{Vect}_k$ from the cobordism category to vector spaces. The symmetric monoidal structure encodes "the physics of a disjoint union is the tensor product of the pieces."

> [!tip] Operads and Higher Algebra *(from Algebra and Topology)*
> An **operad** generalizes a monoid object by allowing operations of many arities; operads in a symmetric monoidal category govern algebraic structures (associative, commutative, Lie) up to coherent homotopy, the gateway to higher and **derived** algebra.

> [!tip] Linear Logic and Curry–Howard *(from Logic)*
> A (closed) symmetric monoidal category models the multiplicative fragment of linear logic, with $\otimes$ the linear conjunction and the internal hom the linear implication — an instance of the **Curry–Howard** correspondence between proofs and programs.
