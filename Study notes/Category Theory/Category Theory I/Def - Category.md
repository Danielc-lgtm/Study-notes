---
type: definition
subject: category-theory
prereqs:
  - "Def - Group"
  - "Def - Homomorphism"
tags: [category-theory, foundations]
---

# Notation

A category is written $\mathcal{C}, \mathcal{D}, \mathcal{E}$. Its objects are $A, B, C, X, Y$, and we write $A \in \mathcal{C}$ as shorthand for "$A$ is an object of $\mathcal{C}$". The collection of morphisms (also called arrows or maps) from $A$ to $B$ is the **hom-set** $\mathcal{C}(A, B)$, also written $\mathrm{Hom}_{\mathcal{C}}(A, B)$; a morphism $f \in \mathcal{C}(A, B)$ is displayed as $f : A \to B$ or $A \xrightarrow{f} B$. We call $A$ the **domain** (source) and $B$ the **codomain** (target). Composition of $f : A \to B$ and $g : B \to C$ is written $g \circ f : A \to C$ (read right-to-left, "$g$ after $f$"). The identity morphism on $A$ is $1_A$ or $\mathrm{id}_A$. Named categories are set in bold: $\mathbf{Set}, \mathbf{Grp}, \mathbf{Ab}, \mathbf{Ring}, \mathbf{CRing}, \mathbf{Mod}_R, \mathbf{Vect}_k, \mathbf{Top}, \mathbf{Rel}, \mathbf{Cat}$. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

Start from a single observation: in almost every part of mathematics, the interesting objects come paired with a notion of structure-preserving map, and these maps **compose**. Sets have functions; functions compose. [[Def - Group|Groups]] have [[Def - Homomorphism|homomorphisms]]; homomorphisms compose. [[Def - Topological Space|Topological spaces]] have [[Def - Continuous Map|continuous maps]]; continuous maps compose. [[Def - Vector Space|Vector spaces]] have [[Def - Linear Map|linear maps]]; linear maps compose. In every case there is also a "do nothing" map — the identity — and composition is associative because it is, underneath, composition of functions. A category is the abstraction of exactly this much: a world of objects, the arrows between them, and a law for stringing arrows together. Nothing else. We deliberately forget what the objects *are* — sets, groups, spaces — and remember only how the arrows compose.

Why strip away the objects' internal nature? Because an astonishing amount of mathematics depends only on the composition pattern, not on what is being composed. "Isomorphism", "product", "kernel", "quotient", "free construction" can all be phrased purely in terms of arrows and how they compose, and once phrased that way the same theorem applies to groups, spaces, modules, and sheaves at once. The category axioms are the smallest set of rules that make this transfer possible.

Now ask which rules are forced. We need composition to be a partial operation: $g \circ f$ should be defined exactly when the codomain of $f$ matches the domain of $g$, because an arrow out of $B$ can only follow an arrow into $B$. **What breaks if we drop associativity?** Associativity says $(h \circ g) \circ f = h \circ (g \circ f)$ for any composable triple $A \xrightarrow{f} B \xrightarrow{g} C \xrightarrow{h} D$. Without it, a chain of arrows $A \to B \to C \to D$ has no unambiguous composite — the answer depends on the order in which you collapse the chain, so a "path" of arrows does not name a single morphism. Every diagram-chasing argument, the whole language of [[Def - Commutative Diagram|commutative diagrams]], silently assumes that any two ways of bracketing a path agree; associativity is what licenses writing $h \circ g \circ f$ with no brackets at all. Function composition is associative for free, so the axiom costs nothing in the examples while buying unambiguous paths everywhere.

**What breaks if we drop the identity axiom?** Each object $A$ must carry a morphism $1_A : A \to A$ with $1_A \circ f = f$ and $g \circ 1_A = g$ whenever these composites make sense. Drop it and you lose the ability to say "do nothing", and with it the ability to define an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]]: an iso is a morphism with a two-sided inverse, and "inverse" is defined by $g \circ f = 1_A$, $f \circ g = 1_B$. No identities, no inverses, no notion of two objects being "the same". The identity is also what pins each object down inside the arrow world — in fact one can recover the objects entirely from the identities, since objects correspond bijectively to the idempotent identity arrows. A structure with associative composition but no identities is a **semicategory**, and it is too impoverished to do category theory in.

The test of the definition is whether you could invent it. You can: write down "objects, arrows between them, a partial composition matching domains to codomains", then demand the two things that any reasonable notion of composition must satisfy — that long chains compose unambiguously (associativity) and that there is a neutral do-nothing arrow (identity). That is the entire definition. The conceptual leap is not the axioms; it is the decision to take *arrows*, not *elements*, as the primitive notion.

---

# The Definition

A **category** $\mathcal{C}$ consists of:

- a collection $\mathrm{ob}(\mathcal{C})$ of **objects**;
- for every ordered pair of objects $A, B$, a collection $\mathcal{C}(A, B)$ of **morphisms** from $A$ to $B$ (the **hom-set**);
- for every object $A$, a distinguished **identity** morphism $1_A \in \mathcal{C}(A, A)$;
- for every triple $A, B, C$, a **composition** function
$$\circ : \mathcal{C}(B, C) \times \mathcal{C}(A, B) \longrightarrow \mathcal{C}(A, C), \qquad (g, f) \longmapsto g \circ f,$$

subject to two axioms:

1. **Associativity.** For all $f : A \to B$, $g : B \to C$, $h : C \to D$,
$$(h \circ g) \circ f = h \circ (g \circ f).$$

2. **Identity (unit).** For all $f : A \to B$,
$$1_B \circ f = f = f \circ 1_A.$$

One usually requires that distinct hom-sets be disjoint, so that every morphism has a single well-defined domain and codomain.

**Size.** A category is **locally small** if every hom-set $\mathcal{C}(A, B)$ is a genuine set (not a proper class). It is **small** if, in addition, the collection of objects is a set. A category that is not small is **large**. The point of the distinction is set-theoretic hygiene: $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Top}$ have a proper class of objects (there is no set of all sets), so they are large but locally small, while a single group regarded as a category (below) is small. The distinction matters once we form [[Def - Functor Category|functor categories]] and invoke the **Yoneda lemma**, where "locally small" is exactly the hypothesis that makes the hom-set a set one can map into.

---

# Relate to Other Fields / Compression

A category is a **typed monoid**. Recall a monoid is a set with an associative binary operation and a two-sided unit — a [[Def - Group|group]] without inverses. A monoid is exactly a category with one object: the elements *are* the morphisms (all of type $\ast \to \ast$), the operation is composition, and the unit is the identity. A general category relaxes the single object to many, so that not every pair of morphisms can be composed — composition is now *typed* by domains and codomains. This is the cleanest compression: **a category is a monoid in which multiplication is partial, defined only when the types match.** Equivalently, a category is a [[Def - Group|group]]-like algebra of composable arrows with the inverses and the single-object restriction both removed.

There is a second compression worth carrying. A [[Def - Group|group]] is a one-object category in which every arrow is invertible (a one-object [[Def - Groupoid|groupoid]]); a [[Def - Topological Space|preorder]] is a category with at most one arrow between any two objects. So three a-priori unrelated structures — monoids, groups, preorders — are all degenerate categories, recovered by restricting the number of objects or the number of arrows between a pair. Category theory does not generalize these structures by adding features; it generalizes them by *removing restrictions* on an arrow algebra.

**True name:** *an algebra of composable, typed arrows with unambiguous paths* — the operative content is that any directed path of arrows composes to a single morphism (associativity), and every object has a do-nothing arrow (identity). When you reason inside a category you are reasoning about paths in a typed graph, modulo the rule that a path's composite depends only on its endpoints-and-route, never on the bracketing.

---

# Examples / Corollaries

**$\mathbf{Set}$.** Objects are sets, morphisms are functions, composition is function composition, identities are identity functions. This is the prototype, and the source of the intuition for every other category. Associativity and the unit laws hold because they hold for functions.

**$\mathbf{Grp}$ and $\mathbf{Ab}$.** Objects are [[Def - Group|groups]] (respectively [[Def - Abelian Group|abelian groups]]), morphisms are group [[Def - Homomorphism|homomorphisms]]. The composite of two homomorphisms is a homomorphism, and the identity map of a group is a homomorphism, so the axioms hold. $\mathbf{Ab}$ is the full [[Def - Subcategory|subcategory]] of $\mathbf{Grp}$ on the abelian groups.

**$\mathbf{Ring}$ and $\mathbf{CRing}$.** Objects are [[Def - Ring|rings]] (respectively commutative rings), morphisms are [[Def - Ring Homomorphism|ring homomorphisms]] (preserving $1$). $\mathbf{CRing}$ is the home of the algebraic-geometry dictionary: its opposite $\mathbf{CRing}^{\mathrm{op}}$ is equivalent to the category of **affine schemes**.

**$\mathbf{Mod}_R$ and $\mathbf{Vect}_k$.** For a fixed ring $R$, objects are [[Def - Module|left $R$-modules]] and morphisms are $R$-linear [[Def - Module Homomorphism|module homomorphisms]]. When $R = k$ is a field this is $\mathbf{Vect}_k$, the category of [[Def - Vector Space|vector spaces]] and [[Def - Linear Map|linear maps]].

**$\mathbf{Top}$.** Objects are [[Def - Topological Space|topological spaces]], morphisms are [[Def - Continuous Map|continuous maps]]. The composite of continuous maps is continuous and the identity is continuous.

**$\mathbf{Rel}$.** Objects are sets, but a morphism $A \to B$ is a *relation* $R \subseteq A \times B$. Composition is relational composition, $S \circ R = \{(a,c) : \exists b,\ (a,b)\in R \text{ and } (b,c)\in S\}$, and the identity on $A$ is the diagonal $\{(a,a) : a \in A\}$. This shows morphisms need not be functions: $\mathbf{Set}$ sits inside $\mathbf{Rel}$ by sending a function to its graph.

**A poset as a category.** Let $(P, \leq)$ be a partially ordered set. Take the objects to be the elements of $P$, and decree a single morphism $a \to b$ exactly when $a \leq b$ (and none otherwise). Composition is forced — if $a \leq b$ and $b \leq c$ then $a \leq c$ — and is associative because there is at most one arrow between any two objects, so any two parallel composites are automatically equal. Reflexivity $a \leq a$ supplies the identity. **This is the cleanest illustration that "morphism" need not mean "function": here a morphism carries no data beyond its existence.** A category in which every hom-set has at most one element is exactly a preorder.

**A monoid or group as a one-object category.** Let $M$ be a monoid (or [[Def - Group|group]]). Form a category $\mathbf{B}M$ with a single object $\ast$, with $\mathbf{B}M(\ast, \ast) = M$, with composition the monoid multiplication, and with $1_\ast$ the monoid unit. The associativity and unit axioms of the category are *exactly* the monoid axioms. **This is the illustration that a category is a many-object monoid:** restrict to one object and you recover an ordinary monoid; if every arrow is invertible you recover a group (a one-object [[Def - Groupoid|groupoid]]).

**Discrete, walking-arrow, terminal categories.** The **discrete category** on a set $S$ has the elements of $S$ as objects and only identity morphisms — it is a set viewed as a category. The **walking arrow** $\mathbf{2}$ has two objects $0, 1$ and a single non-identity morphism $0 \to 1$. The **terminal category** $\mathbf{1}$ has one object and only its identity. These tiny categories are the *shapes* one maps out of: a functor $\mathbf{2} \to \mathcal{C}$ is exactly a choice of morphism in $\mathcal{C}$, and a functor $\mathbf{1} \to \mathcal{C}$ is exactly a choice of object.

**Is NOT a category — a graph with broken composition.** Take three objects $A, B, C$ with arrows $f : A \to B$ and $g : B \to C$, but decline to provide any arrow $A \to C$. This fails the definition: the composite $g \circ f$ is required to exist and live in the (empty) hom-set $\mathcal{C}(A, C)$. A directed graph becomes a category only when you formally adjoin all composable paths (the **free category** on the graph) and impose associativity; a graph with *some* but not all composites, or with a composition that is not associative — say $(h \circ g) \circ f \neq h \circ (g \circ f)$ for some labelling — is a "graph with partial composition" but not a category. The defect is exactly the missing or ambiguous path.

**Calibration check.** Verify three things. First, that the identity on each object is *unique*: if $1_A$ and $1_A'$ both satisfy the unit law then $1_A = 1_A \circ 1_A' = 1_A'$ — the same one-line argument that uniquely determines the identity of a [[Def - Group|group]]. Second, that a poset really is a category by checking associativity is automatic when hom-sets have at most one element. Third, that a one-object category is the same data as a monoid, so that the category axioms restricted to one object literally become the monoid axioms.

---

# Unlocked by This

> [!tip] Functors, Natural Transformations, and the 2-Category Cat *(from this chapter)*
> Once you have categories, the maps between them are [[Def - Functor|functors]], and the maps between functors are [[Def - Natural Transformation|natural transformations]]. Small categories and functors themselves form a category $\mathbf{Cat}$, which carries the extra structure of a **2-category** because of the natural transformations between functors.

> [!tip] Affine Schemes and the Category CRing *(from Algebraic Geometry)*
> The category $\mathbf{CRing}$ of commutative rings is the algebraic backbone of geometry. Reversing its arrows, $\mathbf{CRing}^{\mathrm{op}}$, is equivalent to the category of **affine schemes**: a commutative ring is "the ring of functions on a space", and a ring map runs backward against the corresponding map of spaces. The contravariance is unpacked in [[Def - Functor]] via the **Spec** construction.

> [!tip] Curry–Howard–Lambek and Cartesian Closed Categories *(from Logic and Type Theory)*
> A category with enough structure (a **cartesian closed category**) is simultaneously a model of typed lambda calculus and of intuitionistic propositional logic: objects are types/propositions, morphisms are programs/proofs, composition is substitution/cut. This three-way dictionary — the **Curry–Howard–Lambek** correspondence — begins with taking "morphism" seriously as "transformation/proof". See [[Def - Cartesian Closed Category]].
