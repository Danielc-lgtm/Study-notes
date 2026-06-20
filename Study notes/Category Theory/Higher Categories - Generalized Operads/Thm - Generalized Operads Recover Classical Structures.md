---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Generalized Multicategory"
  - "Def - Generalized Operad"
  - "Def - Cartesian Monad"
  - "Def - Category"
  - "Def - Monoid in a Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, the ambient category is $\mathbf{Set}$ unless stated otherwise, and $(T, \eta, \mu)$ is a [[Def - Cartesian Monad|cartesian monad]] on it. We use three monads: the **identity monad** $T = \mathrm{id}$; the **free-monoid (list) monad** $T = (-)^{*}$, $X \mapsto X^{*} = \coprod_{n \geq 0} X^n$; and (over globular sets $\mathbf{GSet}$) the **free-strict-$\omega$-category monad** $\mathbb{T}$. A [[Def - Generalized Multicategory|T-multicategory]] has data $(C_0, C_1, \mathrm{dom} : C_1 \to T C_0, \mathrm{cod} : C_1 \to C_0, \mathrm{ids}, \mathrm{comp})$; a [[Def - Generalized Operad|T-operad]] is the case $C_0 = 1$, with arity $\mathrm{ar} : P \to T1$. We write $\simeq$ for equivalence of categories. The full symbol registry is on [[Higher Categories — Generalized Operads via Cartesian Monads]].

---

# Statement

> **Theorem (Recovery of classical structures).** Let the ambient category be $\mathbf{Set}$.
> 1. For the **identity monad** $T = \mathrm{id}$, the category of $T$-multicategories is equivalent to the category of small [[Def - Category|categories]], $(\mathbf{Set}, \mathrm{id})\text{-}\mathbf{Multicat} \simeq \mathbf{Cat}$, and $T$-operads are equivalent to [[Def - Monoid in a Monoidal Category|monoids]].
> 2. For the **free-monoid monad** $T = (-)^{*}$, the category of $T$-multicategories is equivalent to the category of classical (plain, non-symmetric) **multicategories**, and $T$-operads are equivalent to classical non-symmetric **operads**.
> 3. Each equivalence restricts to algebras: an algebra for a $\mathrm{id}$-operad (a monoid) is a monoid-set acted on; an algebra for a $(-)^{*}$-operad is a classical operad-algebra; in particular, algebras for the associative operad are monoids.

> **Theorem (Globular instance).** Over [[Def - Globular Set|globular sets]] $\mathbf{GSet}$ with $T = \mathbb{T}$ the [[Def - The Free Strict ω-Category Monad|free-strict-ω-category monad]], $T$-operads are exactly the **[[Def - Globular Operad|globular operads]]**, and their algebras are the weak higher categories of the corresponding signature (HC7). The three rows $T = \mathrm{id},\ (-)^{*},\ \mathbb{T}$ assemble into the chapter's unifying table.

---

# Motivation

This is the theorem that justifies the abstraction. Section 1 introduced cartesian monads, and §2 wrote down a definition — "monoid in $T$-spans" — that is short, slick, and, taken on its own, gives no reason to believe it captures anything one already cares about. The danger of any unifying definition is that it unifies nothing: it might be a formally pretty box that the intended examples do not actually fit into. This theorem removes that danger by proving, as honest equivalences of categories, that the box contains exactly the structures it was designed to contain.

The point is not that there is a vague analogy between $T$-multicategories and categories or operads. The point is that they are *the same*, up to equivalence. A small category is not "like" a $\mathrm{id}$-multicategory; the two categories of structures are equivalent, with explicit functors both ways. A classical multicategory is not "modelled by" a $(-)^{*}$-multicategory; they are equivalent. This is what licenses the central move of the whole chapter — proving a fact once about $T$-multicategories and reading it off for categories, multicategories, operads, and globular operads simultaneously. Without the recovery theorem, the framework would be a hopeful generalization; with it, the framework is a genuine common refinement, and every generic theorem (free constructions, algebras, slicing) is automatically a theorem about all the classical instances at once.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "fix a cartesian monad and a recognizable target structure". The skill is recognizing, in the wild, that a classical structure is secretly a $T$-multicategory for a particular $T$.

The first disguised source is **a structure whose arrows have single-object sources** — any [[Def - Category|category]], internal category, or category-like gadget. The recognition is that "source is one object" means $T = \mathrm{id}$, so the structure is a $\mathrm{id}$-multicategory and the theorem identifies it with a category. *Example problem:* show that a one-object internal category in $\mathcal{E}$ is an internal [[Def - Monoid in a Monoidal Category|monoid]], by combining the $\mathrm{id}$-instance with the operad ($C_0 = 1$) collapse.

The second disguised source is **a structure whose arrows have list-shaped (multi-input) sources** — a multicategory, a coloured operad, an algebraic signature with ordered arities. The recognition is "source is a finite list" $\Rightarrow T = (-)^{*}$. *Example problem:* identify a PRO (a strict monoidal category on objects $0, 1, 2, \dots = \mathbb{N}$ with addition) data as a $(-)^{*}$-structure, reading the list-arity off the tensor.

The third disguised source is **a structure whose cells have pasting-diagram sources** — a globular or higher-categorical structure. The recognition is "source is a pasting diagram" $\Rightarrow T = \mathbb{T}$, so the structure is a $\mathbb{T}$-operad, a globular operad. *Example problem:* recognize that a strict $\omega$-category is an algebra for the *terminal* globular operad, then weaken to a contractible operad to get a weak $\omega$-category (HC7).

**Targets (Output Amplification)**

The bare conclusion is "$T$-multicategories $\simeq$ [classical structure]". Combined with other facts it transfers theorems wholesale.

Combine the equivalence with **a generic theorem about $T$-multicategories**, e.g. [[Thm - The Free Multicategory Monad|the free T-multicategory monad]]. Transporting along the equivalence yields the classical free-category and free-multicategory monads *for free*, with no separate construction. The further result is that "free category on a graph" and "free operad on a signature" are one theorem seen through two monads — a genuine economy, not a coincidence.

Combine the equivalence with **the algebra identification (part 3)**. Knowing that $\mathrm{Assoc}$-algebras are monoids, plus the equivalence, lets one read classical structure theorems (e.g. "monoids are the algebras of the simplest operad") as instances of the operad-algebra framework. The further result is a uniform definition of "model of a theory" that covers monoids, operad-algebras, and weak higher categories in one stroke.

Combine the equivalence with **iteration (the globular instance)**. Once $\mathbb{T}$-operads are identified with globular operads, the entire chapter's machinery — algebras, contractions, initiality — descends to the globular world, producing the Batanin–Leinster definition of weak $\omega$-categories. The further result $E$ is an algebraic definition of higher categories built entirely from the recovery theorem plus §1–§3.

---

# Why Is It True

Each equivalence is proved the same way: write out the $T$-multicategory data, substitute the concrete monad, and watch the abstract structure maps turn, term by term, into the classical axioms. The whole content is in computing $T C_0$, because that single object controls what the domain of an arrow is.

For $T = \mathrm{id}$: $T C_0 = C_0$, so $\mathrm{dom} : C_1 \to C_0$ is an ordinary source map. The composable-configuration pullback $C_1 \times_{C_0} C_1$ is the set of composable pairs. Associativity and unitality of $\mathrm{comp}$ are the category axioms verbatim. So a $\mathrm{id}$-multicategory *is* a small category, and the functors both ways (forget that the domain is a "$\mathrm{id}$-shape"; remember it) are mutually inverse equivalences. Setting $C_0 = 1$ gives a one-object category, which is a [[Def - Monoid in a Monoidal Category|monoid]].

For $T = (-)^{*}$: $T C_0 = C_0^{*}$ is the set of finite lists of objects, so $\mathrm{dom}(\theta)$ is the *input list* $(a_1, \dots, a_n)$ of an arrow $\theta$, and $\mathrm{cod}(\theta) = b$ is its output — a multimap $(a_1, \dots, a_n) \to b$. The composable configurations are "a multimap with a list of multimaps feeding its inputs", and $\mathrm{comp}$ is exactly classical operadic substitution. The axioms become the multicategory axioms. Setting $C_0 = 1$ collapses colours but, because $T1 = 1^{*} = \mathbb{N}$ is non-trivial, leaves a set $P(n)$ of operations for each arity $n$ — a classical operad.

> **The whole theorem is the single computation "what is $T C_0$?": one object for $\mathrm{id}$, a list for $(-)^{*}$, a pasting diagram for $\mathbb{T}$ — and that object *is* the allowed source of an arrow, so the classical structure is read straight off.**

The globular instance is the same computation in a different ambient category: $\mathbb{T} C_0$ is the globular set of pasting diagrams on $C_0$, so the domain of an operation is a pasting diagram, and a $\mathbb{T}$-operad is exactly a globular operad. The reason all three work uniformly is that nothing in the $T$-multicategory definition refers to the *internal nature* of $T$-shapes; it only uses that they form a cartesian monad. Substituting a specific $T$ specializes the shapes without disturbing the axioms.

---

# What Makes This Hard

The conceptual content is light, but two technical traps catch people. The first is mistaking an *equivalence* for a mere *bijection on objects*: one must exhibit functors in both directions and check they are mutually (naturally) inverse, including on morphisms — a multicategory morphism must correspond to a $(-)^{*}$-multicategory morphism, not just the objects. Skipping the morphism check leaves an "equivalence" that is only an object-level analogy. The second trap is the operad collapse for $(-)^{*}$: it is tempting to think $C_0 = 1$ trivializes the structure (as it does for $T = \mathrm{id}$, where a one-object category is a monoid with a single arity), but here $T1 = \mathbb{N}$ keeps infinitely many arities alive, so the one-object case is a full operad, not a monoid. Forgetting that the richness lives in $T1$ rather than $C_0$ is the characteristic error.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
For each monad, compute $T C_0$ (and $T C_1$), substitute into the $T$-multicategory data and axioms, and recognize the classical axioms. Then build explicit functors both ways and check they are mutually inverse, giving an equivalence. Specialize to $C_0 = 1$ for the operad statements, watching $T1$.

**Subgoal decomposition:**

1. **Identity monad gives categories.** Show a $\mathrm{id}$-multicategory is a small category.
   - *Hint:* $T C_0 = C_0$, so $\mathrm{dom}$ is the ordinary source and the composition pullback is composable pairs; the axioms are the category axioms.
   - *Why needed:* The base case anchoring the table and the $\mathrm{id}$ row.

2. **One-object identity gives monoids.** Show a $\mathrm{id}$-operad ($C_0 = 1$) is a monoid.
   - *Hint:* $T1 = 1$, so there is one arity; $P$ is a set with associative unital composition.
   - *Why needed:* The operad column of the $\mathrm{id}$ row.

3. **Free-monoid monad gives multicategories.** Show a $(-)^{*}$-multicategory is a classical multicategory.
   - *Hint:* $T C_0 = C_0^{*}$, so $\mathrm{dom}$ is the input list; $\mathrm{comp}$ is operadic substitution.
   - *Why needed:* The $(-)^{*}$ row; the central nontrivial recovery.

4. **One-object free-monoid gives operads.** Show a $(-)^{*}$-operad is a classical non-symmetric operad.
   - *Hint:* $T1 = \mathbb{N}$, so $\mathrm{ar} : P \to \mathbb{N}$ slices $P$ into $P(n)$; composition is the classical $P(k) \times \prod P(n_i) \to P(\sum n_i)$.
   - *Why needed:* The operad column of the $(-)^{*}$ row; shows $C_0 = 1$ does not trivialize.

5. **Algebras transport.** Show the algebra notions match, in particular $\mathrm{Assoc}$-algebras are monoids.
   - *Hint:* The induced monad $T_P$ matches the classical operad's monad; Eilenberg–Moore algebras coincide.
   - *Why needed:* Part 3, the rightmost column.

6. **Globular instance.** Over $\mathbf{GSet}$ with $T = \mathbb{T}$, show $T$-operads are globular operads.
   - *Hint:* $\mathbb{T}1$ is the globular pasting diagrams; $\mathrm{ar} : P \to \mathbb{T}1$ assigns each operation its shape.
   - *Why needed:* The $\mathbb{T}$ row and the bridge to HC7.

---

# Lemma Decomposition

> [!note]- Lemma 1: The identity monad recovers categories and monoids
> **Statement:** $(\mathbf{Set}, \mathrm{id})\text{-}\mathbf{Multicat} \simeq \mathbf{Cat}$, and $(\mathbf{Set}, \mathrm{id})$-operads $\simeq$ [[Def - Monoid in a Monoidal Category|monoids]].
>
> **Hint:** $T C_0 = C_0$, so all data and axioms are literally those of a category; $C_0 = 1$ gives a one-object category, i.e. a monoid.
>
> **Why needed:** Establishes the base row of the table and confirms the framework is conservative ($\mathrm{id}$ changes nothing).
>
> > [!note]- Full proof
> > With $T = \mathrm{id}$, the data of a $T$-multicategory are $C_0, C_1$, $\mathrm{dom}, \mathrm{cod} : C_1 \to C_0$, $\mathrm{ids} : C_0 \to C_1$, and $\mathrm{comp} : C_1 \times_{C_0} C_1 \to C_1$ over the composable-pairs pullback — exactly the data of a small category. The associativity and unitality axioms are exactly the category axioms. The functor $\Phi : (\mathbf{Set},\mathrm{id})\text{-}\mathbf{Multicat} \to \mathbf{Cat}$ sending this data to the evident category, and $\Psi$ in reverse, are mutually inverse on objects and morphisms (a morphism of $\mathrm{id}$-multicategories is a pair of maps commuting with the structure, i.e. a functor). Hence an equivalence (in fact an isomorphism) of categories. Setting $C_0 = 1$: $T1 = 1$, $P = C_1$ is a set, $\mathrm{ar} : P \to 1$ is unique, $e : 1 \to P$ a unit, $\mathrm{comp} : P \times P \to P$ associative and unital — a monoid. $\square$

> [!note]- Lemma 2: The free-monoid monad recovers multicategories and operads
> **Statement:** $(\mathbf{Set}, (-)^{*})\text{-}\mathbf{Multicat} \simeq \mathbf{Multicat}$ (plain, non-symmetric), and $(\mathbf{Set}, (-)^{*})$-operads $\simeq$ classical non-symmetric operads.
>
> **Hint:** $T C_0 = C_0^{*}$, so $\mathrm{dom}$ is the input list and $\mathrm{comp}$ is operadic substitution; $C_0 = 1$ gives $T1 = \mathbb{N}$ and a set $P(n)$ per arity.
>
> **Why needed:** The central recovery, and the one that shows the framework genuinely captures operads.
>
> > [!note]- Full proof
> > With $T = (-)^{*}$, $T C_0 = \coprod_n C_0^n$, so an arrow $\theta \in C_1$ has $\mathrm{dom}(\theta) = (a_1, \dots, a_n) \in C_0^n$ and $\mathrm{cod}(\theta) = b \in C_0$ — a multimap $(a_1, \dots, a_n) \to b$. The pullback $C_1 \times_{T C_0} T C_1$ is the set of pairs (a multimap $\theta$, a list of multimaps $\theta_1, \dots, \theta_n$ whose outputs are $a_1, \dots, a_n$), and $\mathrm{comp}$ produces the substituted multimap $\theta \circ (\theta_1, \dots, \theta_n)$. The axioms become exactly the (non-symmetric) multicategory axioms (associativity and unitality of substitution). The functor to $\mathbf{Multicat}$ and its inverse agree on objects and morphisms (a $(-)^{*}$-multicategory morphism is a map of objects and an arity-respecting map of multimaps = a multicategory functor), so the categories are equivalent. Setting $C_0 = 1$: $T1 = 1^{*} = \mathbb{N}$, so $\mathrm{ar} : P \to \mathbb{N}$ partitions $P = \coprod_n P(n)$; the unit is in $P(1)$ and composition is $P(k) \times P(n_1) \times \cdots \times P(n_k) \to P(n_1 + \cdots + n_k)$ — a classical non-symmetric operad. $\square$

> [!note]- Lemma 3: Algebras transport across the equivalences
> **Statement:** Under the equivalences of Lemmas 1–2, the algebra notions correspond. In particular, an algebra for the $(-)^{*}$-operad $\mathrm{Assoc}$ (one operation per arity) is a [[Def - Monoid in a Monoidal Category|monoid]].
>
> **Hint:** The induced monad $T_P X = P \times_{T1} TX$ matches the classical operad's monad $X \mapsto \coprod_n P(n) \times X^n$; Eilenberg–Moore algebras coincide.
>
> **Why needed:** Completes part 3, the rightmost column of the table, tying the abstract algebras to the classical ones.
>
> > [!note]- Full proof
> > For a $(-)^{*}$-operad $P$, the induced monad is $T_P X = P \times_{\mathbb{N}} X^{*} = \coprod_n P(n) \times X^n$, which is exactly the classical operad-monad whose algebras are $P$-algebras in the classical sense (sets $X$ with maps $P(n) \times X^n \to X$ satisfying unit and associativity). By the [[Def - Algebra for a Generalized Operad|generalized-algebra]] definition, $P$-algebras are $T_P$-algebras, so the two notions of algebra coincide. For $\mathrm{Assoc}$ with $P(n) = 1$: an algebra is a set with one map $X^n \to X$ per $n$, forced by composition to be the $n$-fold product of a single associative binary operation with unit, i.e. a monoid. $\square$

> [!note]- Lemma 4: The globular monad recovers globular operads
> **Statement:** Over $\mathbf{GSet}$ with $T = \mathbb{T}$ the [[Def - The Free Strict ω-Category Monad|free-strict-ω-category monad]], $\mathbb{T}$-operads are exactly [[Def - Globular Operad|globular operads]], and algebras are weak higher categories of the signature.
>
> **Hint:** $\mathbb{T}1$ is the set of globular pasting diagrams; $\mathrm{ar} : P \to \mathbb{T}1$ records each operation's pasting shape.
>
> **Why needed:** The top row of the table; the bridge to the Batanin–Leinster definition (HC7).
>
> > [!note]- Full proof
> > The monad $\mathbb{T}$ is cartesian (HC7), and $\mathbb{T}1$ is the globular set whose cells are the globular pasting diagrams — the shapes in which higher cells can be composed. A $\mathbb{T}$-operad is a globular set $P$ with arity $\mathrm{ar} : P \to \mathbb{T}1$ (assigning each operation a pasting shape), a unit, and a composition over the pullback, with $\mathrm{ar}$ cartesian — this is exactly the definition of a globular operad. Its [[Def - Algebra for a Generalized Operad|algebras]] are objects of $\mathbf{GSet}$ with coherent composition along the operad's operations, i.e. weak higher categories of that signature. Specializing to the terminal operad gives strict $\omega$-categories; to a contractible operad gives weak $\omega$-categories (HC7). $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Work in $\mathbf{Set}$ for parts 1–3 and in $\mathbf{GSet}$ for the globular instance.
>
> **Step 0 — cartesianness.** Each monad used is cartesian: $\mathrm{id}$ trivially, $(-)^{*}$ because its arities (finite ordinals) are rigid, $\mathbb{T}$ by HC7. So the $T$-multicategory and $T$-operad definitions apply in each case.
>
> **Step 1 — identity monad (Lemma 1).** $T C_0 = C_0$, so the data and axioms of a $\mathrm{id}$-multicategory are those of a small category; the comparison functors are mutually inverse on objects and morphisms, giving $(\mathbf{Set}, \mathrm{id})\text{-}\mathbf{Multicat} \simeq \mathbf{Cat}$. With $C_0 = 1$, $T1 = 1$, recovering a monoid.
>
> **Step 2 — free-monoid monad (Lemma 2).** $T C_0 = C_0^{*}$, so arrows are multimaps and composition is substitution; the comparison functors give $(\mathbf{Set}, (-)^{*})\text{-}\mathbf{Multicat} \simeq \mathbf{Multicat}$. With $C_0 = 1$, $T1 = \mathbb{N}$, partitioning operations by arity and recovering a classical non-symmetric operad.
>
> **Step 3 — algebras (Lemma 3).** The induced monad $T_P$ matches the classical operad-monad $\coprod_n P(n) \times X^n$, so generalized algebras are classical algebras; in particular $\mathrm{Assoc}$-algebras are monoids.
>
> **Step 4 — globular instance (Lemma 4).** Over $\mathbf{GSet}$ with $T = \mathbb{T}$, $\mathbb{T}1$ is the globular pasting diagrams, so $\mathbb{T}$-operads are globular operads and their algebras are weak higher categories.
>
> **Conclusion.** The three monads $\mathrm{id}, (-)^{*}, \mathbb{T}$ give the three rows of the unifying table, each an equivalence of categories specializing the single definition "monoid in $T$-spans". $\blacksquare$

---

# Cross-Field Exercise Suggestions

**PROs and PROPs from monoidal categories.** A strict monoidal category on the object-monoid $\mathbb{N}$ (a PRO) is a $(-)^{*}$-style structure where the tensor encodes list-concatenation of inputs. Recognizing a PRO as living in the $(-)^{*}$ row, and a symmetric PRO (PROP) as needing symmetry it cannot get from a cartesian monad, battle-tests the boundary of the theorem: the non-symmetric structures recover cleanly, the symmetric ones do not.

**Lawvere theories versus operads.** A single-sorted finitary algebraic theory (Lawvere theory) is close to, but not the same as, a $(-)^{*}$-operad: the theory allows operations that *repeat or permute or drop* inputs, which a non-symmetric operad forbids. Comparing the two precisely (the operad is the "linear, ordered" fragment) sharpens understanding of what the cartesian-monad framework includes and excludes.

**Strict $\omega$-categories as terminal-operad algebras.** Identify a strict $\omega$-category as an algebra for the *terminal* globular operad (the one with exactly one operation per pasting shape), then explain why weakening to a *contractible* operad yields a genuinely weaker, more flexible notion. This connects the recovery theorem directly to the homotopy hypothesis and the Batanin–Leinster program (HC7).

---

# Bridges

- **[[Def - Generalized Multicategory|T-multicategories]] and [[Def - Generalized Operad|T-operads]]** — the objects being identified. The theorem is the bridge that turns the abstract §2 definitions into the concrete classical structures, by computing $T C_0$ and $T1$. Everything generic proved about $T$-multicategories descends to categories, multicategories, operads, and globular operads through these equivalences.

- **[[Thm - The Free Multicategory Monad|The free T-multicategory monad]]** — transported. Applying the free-multicategory theorem and then this recovery theorem yields the classical free-category and free-operad constructions as instances, with the same proof. The two theorems together say "free constructions exist and specialize correctly", the engineering backbone of the chapter.

- **Burroni's theorem** — the $\mathrm{id}$ row in disguise. The identification "$\mathrm{id}$-multicategory = small category" is Burroni's "category = monad in $\mathrm{Span}(\mathbf{Set})$" read through this framework; the recovery theorem situates Burroni's result as one instance of a parameterized family.

- **The Batanin–Leinster definition of weak $\omega$-categories (HC7)** — the destination. The globular instance ($\mathbb{T}$-operads = globular operads) is the step that makes the entire weak-$\omega$-category program an application of this chapter: algebras for the initial contractible globular operad are weak $\omega$-categories, and "globular operad" is just "$\mathbb{T}$-operad" via this theorem.

---

# Unlocked by This

> [!tip] The Unifying Table *(from this chapter)*
> This theorem *is* the unifying table made rigorous: the rows $T = \mathrm{id} / (-)^{*} / \mathbb{T}$ give categories / multicategories / globular operads, with monoids / operads / globular operads in the one-object column and the corresponding algebras in the rightmost column. See [[Ex - Reading the unifying table across three monads]] for the full drill.

> [!tip] Batanin–Leinster Weak ω-Categories *(from Higher Category Theory)*
> Because $\mathbb{T}$-operads are globular operads, the definition of a **weak ω-category** as an algebra for the initial contractible globular operad becomes available. This theorem is the link that lets the abstract cartesian-monad machinery deliver a concrete, algebraic definition of higher categories (HC7).

> [!tip] Operads in Other Ambient Categories *(from Algebraic Topology)*
> Replacing $\mathbf{Set}$ by $\mathbf{Top}$ (or chain complexes) in the $(-)^{*}$ row gives topological (or dg-) operads, whose algebras include loop spaces (**May's recognition principle**) and $A_\infty$-algebras. The recovery theorem's structure — "compute $T C_0$, read off the classical axioms" — runs identically over any cartesian-monad-bearing ambient category, so the classical correspondence is robust under change of base.
