---
type: definition
subject: higher-categories
prereqs:
  - "Def - Generalized Multicategory"
  - "Def - Cartesian Monad"
  - "Def - Initial and Terminal Object"
  - "Def - Monoid in a Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $\mathcal{E}$ is a category with [[Def - Pullback and Pushout|pullbacks]] and a terminal object $1$, and $(T, \eta, \mu)$ is a [[Def - Cartesian Monad|cartesian monad]] on $\mathcal{E}$. A **$T$-operad** is a [[Def - Generalized Multicategory|T-multicategory]] $C$ whose object-of-objects is terminal, $C_0 = 1$. We then write $P := C_1$ for the **object of operations**, $T1$ for the **arity object**, and the structure maps become $\mathrm{ar} : P \to T1$ (arity), $e : 1 \to P$ (unit operation), and $\mathrm{comp} : P \times_{T1} TP \to P$ (operadic composition). For $\mathcal{E} = \mathbf{Set}, T = (-)^{*}$ we recover $P(n) = \mathrm{ar}^{-1}(n)$, the set of $n$-ary operations. The full symbol registry is on [[Higher Categories — Generalized Operads via Cartesian Monads]].

---

# Axiom Motivation

A $T$-operad is what you get from a [[Def - Generalized Multicategory|T-multicategory]] by demanding there be essentially *one object*. The motivation is the same as the relationship between a [[Def - Category|category]] and a [[Def - Monoid in a Monoidal Category|monoid]]: a monoid is a one-object category, where "one object" means the object-of-objects is the terminal set $1$. Make the analogous restriction in the generalized setting — set $C_0 = 1$ — and ask what survives.

Two things happen, and the interplay between them is the whole point. First, the *colours collapse*: with only one object there is nothing to label inputs and outputs by, so the multicategory becomes "single-sorted" or "monochromatic". Second — and this is the subtlety that makes operads richer than monoids — the *arities do not collapse*. The domain map was $\mathrm{dom} : C_1 \to T C_0$; setting $C_0 = 1$ turns it into $\mathrm{ar} : P \to T1$, and $T1$ is generally far from trivial. It is the object of *arity-shapes*: for $T = (-)^{*}$ it is $1^{*} = \mathbb{N}$, so even with one object there is a different "slot" for each natural-number arity, and $P$ decomposes as a sequence of operation-objects $P(0), P(1), P(2), \dots$. This is exactly why a $(-)^{*}$-operad is a classical operad and not merely a monoid: the monoid case ($T = \mathrm{id}$, $T1 = 1$) is the degenerate one where there is a single arity.

Now derive the axioms. The unit operation $e : 1 \to P$ is the generalization of "the identity arrow": it is the unique unary operation that does nothing, the operadic unit, picked out by $\mathrm{ids} : C_0 = 1 \to C_1 = P$. Drop it and there is no neutral element for composition — you cannot express "feed an operation straight through". The composition $\mathrm{comp} : P \times_{T1} TP \to P$ is grafting: an operation $\theta$ of arity-shape $s \in T1$ is composed with a $T1$-shaped family of operations, one per input slot, producing a single operation whose arity is the *flattened* shape. The matching condition — that the family's arities fit the slots of $\theta$ — is encoded by the pullback over $T1$, and this is where [[Def - Cartesian Monad|cartesianness]] is needed: without it the grafting is not associative, exactly as in the multicategory case. **Drop associativity** and a tower of substitutions depends on grouping (for $T = (-)^{*}$, the classical operad associativity $\theta \circ (\theta_1 \circ \cdots) = (\theta \circ \theta_i) \circ \cdots$ fails); **drop unitality** and the unit operation no longer acts neutrally, so $P(1)$ fails to contain a genuine identity.

The test "could a reader invent this?" passes cleanly: take the multicategory definition, set the object-of-objects to terminal, and notice that the only data that survives in non-trivial form is the operation-object $P$ over the arity object $T1$. The single most clarifying move when meeting a new cartesian monad is therefore to compute $T1$ — it tells you, before anything else, what the operads over $T$ look like.

---

# The Definition

Let $(T, \eta, \mu)$ be a [[Def - Cartesian Monad|cartesian monad]] on a category $\mathcal{E}$ with pullbacks and terminal object $1$.

A **$T$-operad** is a [[Def - Generalized Multicategory|T-multicategory]] $C$ with $C_0 = 1$. Spelled out, it is:

- an object $P \in \mathcal{E}$ (the **object of operations**),
- a morphism $\mathrm{ar} : P \to T1$ (the **arity**, recording the shape of each operation),
- a morphism $e : 1 \to P$ (the **unit operation**), with $\mathrm{ar} \circ e = \eta_1 : 1 \to T1$,
- a morphism $\mathrm{comp} : P \times_{T1} TP \to P$ (**operadic composition**), where the pullback is of $\mathrm{ar} : P \to T1$ against $T(!) \circ \cdots$ matching the flattened arity,

subject to **associativity** and **left/right unitality**, the one-object specializations of the [[Def - Generalized Multicategory|T-multicategory]] axioms.

Equivalently, in span-and-monoid form: a $T$-operad is a **monoid in the monoidal category of "collections" over $T1$** — i.e. a monoid for the substitution tensor product on the slice-like category $\mathcal{E}/T1$ induced by $T$. (When $\mathcal{E} = \mathbf{Set}, T = (-)^{*}$, this is exactly "a monoid in non-symmetric sequences under the substitution product".)

A **morphism of $T$-operads** $P \to P'$ is a map commuting with $\mathrm{ar}$, $e$, and $\mathrm{comp}$. A $T$-operad is **cartesian over $T$** when its arity map $\mathrm{ar} : P \to T1$ is, together with the structure, a cartesian map — the condition relevant for globular operads (HC7).

---

# Categorical / Structural Definition

A $T$-operad is a [[Def - Monoid in a Monoidal Category|monoid]] in a monoidal category built from $T$. Concretely, consider the slice category $\mathcal{E}/T1$, whose objects are maps $X \to T1$ ("collections of $X$-elements graded by arity-shape"). The monad $T$ induces a **substitution tensor product** $\otimes$ on $\mathcal{E}/T1$: given collections $X \to T1$ and $Y \to T1$, their substitution $X \otimes Y$ is formed by the pullback that records "an $X$-operation with a $T$-shaped family of $Y$-operations plugged into its slots", then flattening the arity via $\mu$. The unit object is $\eta_1 : 1 \to T1$ (the trivial unary operation). A monoid in $(\mathcal{E}/T1, \otimes, \eta_1)$ is precisely a $T$-operad: the monoid multiplication is operadic composition, the monoid unit is the unit operation, and associativity/unitality of the monoid are operadic associativity/unitality.

This is the operadic specialization of the [[Def - Generalized Multicategory#Categorical / Structural Definition|monoid-in-T-spans]] picture: a $T$-multicategory is a monoid in the *bicategory* of $T$-spans, and a $T$-operad is the endomorphism-monoid at the single object $1$, which lives in the *monoidal category* of endo-$T$-spans on $1$, i.e. $\mathcal{E}/T1$ with substitution. The general slogan — **operad = monoid in a category of collections under substitution** — specializes the symmetric-sequence statement of HC3 (operad = monoid in symmetric sequences) to the non-symmetric, $T$-parameterized setting, and explains why the two definitions of "operad" agree where they overlap.

---

# Relate to Other Fields / Compression

A $T$-operad is *a theory of $T$-shaped operations on a single sort*. This is the categorical distillation of "an algebraic structure given by operations of various arities, closed under substitution". In universal algebra, a (non-symmetric, single-sorted) **Lawvere-style theory** restricted to its operations is essentially a $(-)^{*}$-operad. In programming-language theory, a $T$-operad is the signature of an algebraic effect or a term-rewriting system whose terms substitute. In topology, a topological $T$-operad (with $\mathcal{E} = \mathbf{Top}$) encodes the higher coherences of a space's multiplication, the most famous being the little-$n$-disks operad $E_n$.

**True name:** *a $T$-operad is the one-object case of a $T$-multicategory; its operations are graded by the arity object $T1$, and it is a monoid under substitution*. When you meet a $T$-operad, the first computation is always $T1$: it is $1$ for the identity monad (so a $T$-operad is a monoid), $\mathbb{N}$ for the list monad (so a $T$-operad is a classical operad with a set $P(n)$ of $n$-ary operations), and the globular pasting diagrams for $\mathbb{T}$ (so a $T$-operad is a globular operad). $T1$ is the single object that tells you what kind of operad you have.

---

# Examples / Corollaries

**Is an instance — a monoid ($\mathcal{E} = \mathbf{Set}$, $T = \mathrm{id}$).** With the identity monad, $T1 = 1$, so there is a single arity and $P$ is just a set with a unit element $e : 1 \to P$ and a composition $P \times_1 P = P \times P \to P$ that is associative and unital — a [[Def - Monoid in a Monoidal Category|monoid]]. This is the operadic analogue of "a one-object category is a monoid": a $\mathrm{id}$-operad *is* a monoid.

**Is an instance — a classical non-symmetric operad ($\mathcal{E} = \mathbf{Set}$, $T = (-)^{*}$).** Now $T1 = 1^{*} = \mathbb{N}$, so the arity map $\mathrm{ar} : P \to \mathbb{N}$ partitions $P$ into sets $P(n)$ of $n$-ary operations. The unit lives in $P(1)$, and composition is the classical substitution $P(k) \times P(n_1) \times \cdots \times P(n_k) \to P(n_1 + \cdots + n_k)$. This is exactly a plain (non-symmetric) operad. *Example:* the **associative operad** $\mathrm{Assoc}$ with $P(n) = 1$ for all $n$ (one $n$-ary operation, "multiply $n$ things in order"); its algebras are monoids.

**Is an instance — a globular operad ($\mathcal{E} = \mathbf{GSet}$, $T = \mathbb{T}$).** Taking the free-strict-$\omega$-category monad on globular sets, $T1 = \mathbb{T}1$ is the set of **globular pasting diagrams** — the shapes in which higher cells paste together. A $\mathbb{T}$-operad with $\mathrm{ar} : P \to \mathbb{T}1$ cartesian is a **[[Def - Globular Operad|globular operad]]**: an operation of arity a given pasting diagram is "a way to compose that diagram into a single cell". Its algebras are weak higher categories of that signature (HC7).

**Is NOT an instance — a symmetric operad directly.** A symmetric operad has $S_n$ acting on $P(n)$, encoding that inputs can be permuted. This is **not** a $T$-operad for the multiset monad, because that monad is not [[Def - Cartesian Monad|cartesian]]. Symmetric operads are monoids in *symmetric* sequences (HC3), a different monoidal category; the generalized-operad framework, run on a cartesian monad, produces only the non-symmetric ones.

**Is NOT an instance — a $T$-multicategory with two objects.** A $T$-multicategory whose $C_0$ has two elements is a *coloured* operad, not a $T$-operad: an operad in this strict sense must have $C_0 = 1$. The two-object case is genuinely more data (operations are sorted by which colours occupy their slots), and collapsing it to one object loses the colouring.

**Calibration check.** Compute $T1$ for the identity, list, and free-category monads, and read off that the corresponding operads are monoids, classical operads, and "operads over linear graphs". For $T = (-)^{*}$, verify that the associative operad $P(n) = 1$ has exactly one operation per arity and that its composition is forced, so that its algebras are monoids. If you can explain why $C_0 = 1$ collapses colours but not arities, you have understood the definition.

---

# Unlocked by This

> [!tip] Algebras for a Generalized Operad *(from this chapter)*
> A $T$-operad $P$ acts on objects: an **[[Def - Algebra for a Generalized Operad|algebra]]** for $P$ is an object $X$ with an action $P \times_{T1} TX \to X$ respecting unit and composition. This is the §3 destination — algebras for the associative operad are monoids, algebras for a globular operad are weak higher categories.

> [!tip] The Endomorphism Operad and Recognition *(from Algebraic Topology)*
> Every object $X$ has an **endomorphism operad** $\mathrm{End}(X)$ with $\mathrm{End}(X)(n) = \mathcal{E}(TX\text{-slot}, X)$ (for $\mathbf{Set}$, $\mathrm{Hom}(X^n, X)$), and a $P$-algebra structure on $X$ is exactly an operad map $P \to \mathrm{End}(X)$. In topology, $X$ is an $n$-fold loop space iff it is an algebra for the little-$n$-disks operad $E_n$ — **May's recognition principle**.

> [!tip] Globular Operads and Weak ω-Categories *(from Higher Category Theory)*
> The $\mathbb{T}$-operads over globular sets are the **globular operads**. Equipping the initial one with a **contraction** (chosen weak composites and coherence cells) gives the Batanin–Leinster operad $L$, and a **weak ω-category** is an $L$-algebra. This chapter's one-object generalized operad is the exact vehicle for that definition (HC7).
