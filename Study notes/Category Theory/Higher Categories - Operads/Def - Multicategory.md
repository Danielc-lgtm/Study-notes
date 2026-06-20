---
type: definition
subject: higher-categories
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A multicategory (also called a **coloured operad**) $\mathcal{M}$ has a class of **objects** (or **colours**) $a, b, c, \dots$, exactly as a category does. What changes is the morphisms. Instead of a hom-set $\mathcal{M}(a,b)$ of arrows with one source, a multicategory has, for every finite list of objects $a_1, \dots, a_n$ ($n \geq 0$) and every object $b$, a set of **multimaps**
$$\mathcal{M}(a_1, \dots, a_n; b),$$
the maps "with $n$ inputs and one output". We draw such a multimap as a node with $n$ wires coming in (labelled $a_1, \dots, a_n$ from left to right) and one wire going out (labelled $b$). The number $n$ is the **arity**. For each object $a$ there is an **identity** multimap $1_a \in \mathcal{M}(a; a)$ of arity $1$. Composition is **substitution into inputs**: given $\theta \in \mathcal{M}(b_1, \dots, b_k; c)$ and, for each $i$, a multimap $\varphi_i \in \mathcal{M}(a_{i,1}, \dots, a_{i,n_i}; b_i)$, there is a composite
$$\theta \circ (\varphi_1, \dots, \varphi_k) \in \mathcal{M}(a_{1,1}, \dots, a_{k,n_k};\, c)$$
obtained by grafting each $\varphi_i$ onto the $i$th input of $\theta$. The full notation registry is on [[Higher Categories — Operads and Multicategories]].

When the multimaps additionally carry an action of the symmetric groups — a way to permute the inputs $a_1, \dots, a_n$ — the multicategory is called **symmetric**; without it, **plain** (or **non-symmetric**). Unless stated otherwise "multicategory" means the symmetric flavour, since that is the one tracking the genuinely multilinear examples.

---

# Axiom Motivation

The right way to arrive at a multicategory is to notice that ordinary category theory is built around a prejudice: a morphism has *one* input. This is exactly right for functions, group homomorphisms, and continuous maps — each of those eats a single argument. But a great deal of mathematics is about operations that eat *several* arguments at once and cannot be honestly decomposed into one-argument pieces. The multiplication of a [[Def - Ring|ring]] is a map $R \times R \to R$; the bracket of a Lie algebra is a map $\mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$; a bilinear form is a map $V \times V \to k$. The category $\mathbf{Vect}_k$ records the *linear* maps $V \to W$, but the bilinear, trilinear, and $n$-linear maps — the operations that actually make algebra interesting — are invisible to it. A multicategory is the structure that puts them back: it remembers, for each tuple of objects, the multilinear operations out of that tuple.

So the desideratum is a gadget with objects and with operations of every arity, that we can *compose* the way multivariable functions compose: plug the outputs of several operations into the inputs of another. Once you accept that, the axioms write themselves, because they are forced by the demand that grafting behave like genuine substitution.

The first axiom is **associativity of substitution**, and it is the subtle one because there are two visibly different ways to compose three layers of multimaps. Given a top multimap $\theta$, a middle row of multimaps $\varphi_i$, and a bottom row of multimaps $\psi_{ij}$, you can first graft the $\psi$'s into the $\varphi$'s and then graft the results into $\theta$, or first graft the $\varphi$'s into $\theta$ and then graft the $\psi$'s into that. The axiom demands these agree. Drop it and "the composite of a three-layer tree" is ambiguous — and since the entire point of a multicategory is that compositions of operations make sense, an ambiguous composite is fatal. Concretely: in $\mathbf{Vect}_k$, building a trilinear map by first composing two bilinear maps and then a third, versus composing them in the other order, must give the same trilinear map, because the underlying multilinear function is the same either way. Associativity is the abstract assertion that the multicategory does not invent distinctions the multilinear functions do not see.

The second axiom is the **unit law**. The arity-$1$ identity $1_a$ must do nothing when grafted: $\theta \circ (1_{a_1}, \dots, 1_{a_n}) = \theta$ and $1_b \circ \theta = \theta$. Drop unitality and the identity multimaps lose their meaning — a multimap could be altered merely by plugging identities into its inputs, which is absurd if $1_a$ is to be "the operation that returns its argument untouched". The unit axiom is what guarantees that the arity-$1$ part of a multicategory is an honest ordinary category sitting inside it.

The third piece of data — present only in the symmetric flavour — is the **symmetric group action and its equivariance**. A multimap $\varphi \in \mathcal{M}(a_1, \dots, a_n; b)$ has its inputs in a definite order, but for genuinely multilinear operations the order is a presentation choice: a bilinear map $V \times V \to W$ can have its two arguments swapped to give another bilinear map. So we ask that each $\sigma \in S_n$ act, sending $\mathcal{M}(a_1, \dots, a_n; b)$ to $\mathcal{M}(a_{\sigma^{-1}(1)}, \dots, a_{\sigma^{-1}(n)}; b)$, and we demand this action be **compatible with substitution** (the equivariance axiom): permuting the inputs of a composite is the same as permuting at the appropriate level and reshuffling. The equivariance axiom is exactly what lets you treat the inputs of a multilinear operation as an unordered family while still being able to write them down in a row. Drop equivariance and the symmetric action is decorative, disconnected from composition, and you cannot, for example, deduce that a symmetric bilinear form composed with itself stays symmetric.

The test of whether these axioms are right: could a reader who has only ever seen multilinear algebra invent the definition? Yes. Start from "the multilinear maps out of tuples of vector spaces", ask what structure they carry — you can compose them by substitution, there is an identity, and you can permute arguments — and demand that these be coherent. You land on exactly the symmetric multicategory axioms.

---

# The Definition

A **(symmetric) multicategory** $\mathcal{M}$ consists of:

1. a class of **objects** $\mathrm{ob}(\mathcal{M})$;
2. for each $n \geq 0$, each tuple $(a_1, \dots, a_n)$ of objects, and each object $b$, a set $\mathcal{M}(a_1, \dots, a_n; b)$ of **multimaps**;
3. for each object $a$, an **identity** $1_a \in \mathcal{M}(a; a)$;
4. **composition** functions
$$\mathcal{M}(b_1, \dots, b_k; c) \times \prod_{i=1}^k \mathcal{M}(a_{i,1}, \dots, a_{i,n_i}; b_i) \longrightarrow \mathcal{M}(a_{1,1}, \dots, a_{k,n_k}; c),$$
written $(\theta; \varphi_1, \dots, \varphi_k) \mapsto \theta \circ (\varphi_1, \dots, \varphi_k)$;
5. for each $n$, tuple $(a_1, \dots, a_n)$, object $b$, and permutation $\sigma \in S_n$, a **symmetry**
$$\sigma^* : \mathcal{M}(a_1, \dots, a_n; b) \longrightarrow \mathcal{M}(a_{\sigma^{-1}(1)}, \dots, a_{\sigma^{-1}(n)}; b),$$

subject to the axioms:

**Associativity.** For composable $\theta$, $(\varphi_i)$, $(\psi_{ij})$,
$$\theta \circ (\varphi_1 \circ (\psi_{1,1}, \dots), \ \dots, \ \varphi_k \circ (\dots, \psi_{k, n_k})) = \big(\theta \circ (\varphi_1, \dots, \varphi_k)\big) \circ (\psi_{1,1}, \dots, \psi_{k,n_k}).$$

**Unit.** $1_b \circ \theta = \theta$ and $\theta \circ (1_{a_1}, \dots, 1_{a_n}) = \theta$ for every $\theta \in \mathcal{M}(a_1, \dots, a_n; b)$.

**Equivariance.** The assignment $\sigma \mapsto \sigma^*$ is an action of $S_n$ (so $(\sigma\tau)^* = \tau^* \sigma^*$ and $1^* = \mathrm{id}$), and it is compatible with composition: permuting the inputs of $\theta$ and permuting the blocks/arguments of the $\varphi_i$ before grafting agrees with permuting the inputs of the grafted result. (The precise form requires the block permutation $\sigma\langle n_1, \dots, n_k\rangle$ induced on the $\sum n_i$ inputs by a permutation $\sigma \in S_k$ of the blocks, together with permutations inside each block.)

A **functor of multicategories** $F : \mathcal{M} \to \mathcal{N}$ assigns objects to objects and multimaps to multimaps of the same arity, preserving identities, composition, and (in the symmetric case) the symmetric action.

A **plain (non-symmetric) multicategory** is the same data and axioms with item (5) and the equivariance axiom deleted.

---

# Categorical / Structural Definition

There are two structural readings, and each is worth having.

**A multicategory is a category with multi-input arrows, formalised via a free-monoid construction.** Recall that the free monoid on a set $X$ is the set $X^* = \coprod_{n \geq 0} X^n$ of finite lists, with concatenation as multiplication; the assignment $X \mapsto X^*$ is the **free-monoid monad** on $\mathbf{Set}$ (see [[Ex - The free monoid monad|the free-monoid monad]]). A plain multicategory is precisely a monoid in the bicategory of spans for this monad — equivalently, the data of an object-of-objects $X$ together with a set of multimaps lying over $X^* \times X$ (a multimap $\mathcal{M}(a_1,\dots,a_n; b)$ lies over the pair $((a_1,\dots,a_n), b) \in X^* \times X$), with substitution as the associative composition. This is not a coincidence of vocabulary: it is the $T = (-)^*$ instance of the general notion of a $T$-multicategory for a [[Def - Monad and Comonad|monad]] $T$, the unifying device of the next chapter. Taking $T$ to be the identity monad gives ordinary categories (lists of length one); taking $T = (-)^*$ gives multicategories.

**A multicategory is the "lax" or "unbiased" version of a monoidal category.** A symmetric monoidal category $(\mathcal{V}, \otimes, I)$ has, for each tuple $a_1, \dots, a_n$, an actual object $a_1 \otimes \dots \otimes a_n$, and an $n$-input multimap should be a single morphism $a_1 \otimes \dots \otimes a_n \to b$. So every symmetric monoidal category $\mathcal{V}$ has an **underlying multicategory** with $\mathcal{V}(a_1, \dots, a_n; b) := \mathcal{V}(a_1 \otimes \dots \otimes a_n, b)$. A multicategory is what is left of this idea when you refuse to assume the tensor product *exists*: you keep the multimaps but drop the requirement that they be represented by a single object. Multicategories that *do* arise from a monoidal structure are called **representable**, and a representable multicategory is the same thing as a monoidal category. This is the precise sense in which a multicategory is a monoidal category with the universal property of $\otimes$ removed and the multimaps kept as primitive.

---

# Relate to Other Fields / Compression

A multicategory is the natural home of **multilinear algebra done abstractly**: it is to multilinear maps what a category is to linear maps. The single most useful instance is the multicategory $\mathbf{Vect}_k^{\otimes}$ underlying $(\mathbf{Vect}_k, \otimes_k)$, whose multimaps $V_1, \dots, V_n; W$ are exactly the $k$-multilinear maps $V_1 \times \dots \times V_n \to W$. The universal property of the tensor product — that multilinear maps out of $V_1 \times \dots \times V_n$ correspond to linear maps out of $V_1 \otimes \dots \otimes V_n$ — is precisely the statement that this multicategory is representable. So the entire theory of tensor products is the statement "the multilinear-map multicategory has a representing object for each tuple".

**True name:** a multicategory is *a system of operations closed under substitution*. The official definition lists sets, identities, composition, and symmetries with axioms; the operational name to carry in your head is "things you can plug into each other's slots, with no constraint that the inputs come one at a time". Whenever you meet a collection of operations of varying arity that compose by feeding outputs into inputs — multilinear maps, logical connectives applied to formulas, terms in an algebraic theory, processes wired together — the structure organising them is a multicategory, and recognising it tells you immediately what to ask: what are the colours, and is it symmetric?

---

# Examples / Corollaries

**Is an instance — every category.** A category $\mathcal{C}$ is exactly a multicategory in which the only non-empty multimap sets have arity $1$: set $\mathcal{C}(a; b) = \mathrm{Hom}_{\mathcal{C}}(a,b)$ and $\mathcal{C}(a_1, \dots, a_n; b) = \emptyset$ for $n \neq 1$. Substitution becomes ordinary composition, and the symmetric action is trivial (the only permutation of one element is the identity). So categories sit inside multicategories as the "linear" (arity-one-only) special case, exactly as functions sit inside multilinear maps.

**Is an instance — the multicategory of vector spaces.** Objects are $k$-vector spaces; $\mathbf{Vect}_k(V_1, \dots, V_n; W)$ is the set of $k$-multilinear maps $V_1 \times \dots \times V_n \to W$. The identity $1_V$ is the identity linear map. Substitution is composition of multilinear maps. The symmetric action on $\mathbf{Vect}_k(V, \dots, V; W)$ permutes the arguments, so a symmetric multilinear form is a fixed point of the $S_n$-action. Replacing $\mathbf{Vect}_k$ by $\mathbf{Set}$ with Cartesian product, or by any [[Def - Monoidal Category|monoidal category]], gives the underlying multicategory of that monoidal category in the same way.

**Is an instance — terms of an algebraic theory.** Fix an algebraic theory such as "groups". Take one object, and let the arity-$n$ multimaps be the group-theoretic terms (words) in $n$ variables $x_1, \dots, x_n$, like $x_1 x_2 x_1^{-1}$, modulo the group axioms. Substituting terms into terms is grafting; the identity is the term $x_1$; the symmetric action renames variables. This one-object multicategory is the **Lawvere theory** of groups in operadic clothing — and the special case of a one-object multicategory is exactly what we will call an [[Def - Operad|operad]].

**Is NOT an instance — the "category" of relations as a multicategory of arity one only, with composition that drops the identity law.** If one tries to make a "multicategory" whose arity-$1$ part forgets identities — say, multimaps are binary relations but $1_a$ is taken to be the empty relation — the unit law $1_b \circ \theta = \theta$ fails immediately, since composing with the empty relation yields the empty relation, not $\theta$. The lesson is that the unit multimap must genuinely be a two-sided identity for substitution; a structure with multi-input operations but no honest identities is a *non-unital* multicategory (a legitimate but different object), not a multicategory.

**Is NOT an instance — a bare family of multilinear maps with no $S_n$-equivariance, called symmetric.** Take $\mathbf{Vect}_k$'s multimaps but declare the symmetric action to be trivial (do nothing). Equivariance then fails: the composite of a swap with a substitution does not match a substitution of swapped pieces, because the declared "action" ignores how arguments move under grafting. This is the canonical reminder that the symmetric structure is not just "there exist permutations of inputs" but "permutations interact correctly with composition".

**Calibration check.** Verify that (i) the arity-$1$ multimaps $\mathcal{M}(a; b)$ of any multicategory, with substitution, form an ordinary category; (ii) in the multicategory of vector spaces the composite of a bilinear map $V \times V \to V$ with itself in one slot is a genuine trilinear map, and computing it by the two associativity routes gives the same answer; and (iii) for a one-object multicategory the symmetric action on the arity-$n$ multimaps is an action of $S_n$ on a single set. If you can do all three, you have the definition.

---

# Unlocked by This

> [!tip] Operad *(from this topic)*
> A one-object multicategory is exactly an [[Def - Operad|operad]]: with a single colour the multimap sets become $P(n) = \mathcal{M}(\underbrace{a, \dots, a}_{n}; a)$, the substitution becomes the operadic composition, and the symmetric action becomes the $S_n$-action. Everything in this chapter about operads is the one-object specialisation of multicategory theory.

> [!tip] Generalized Multicategories *(from Higher Categories — Generalized Operads)*
> Replacing the free-monoid monad $(-)^*$ in the structural definition by an arbitrary **cartesian monad** $T$ produces **$T$-multicategories**, the framework that unifies categories ($T = \mathrm{id}$), classical multicategories ($T = (-)^*$), and globular operads ($T = $ free strict $\omega$-category) under one roof. The whole next chapter is this generalisation.

> [!tip] Coloured Operads in Homotopy Theory *(from Operadic Homotopy Theory)*
> Multicategories (= coloured operads) enriched in spaces or chain complexes are the modern tool for encoding **algebraic structures with several interacting types** — a pair (algebra, module), or the input/output wiring of **factorization homology** and **TQFT**. The coloured generality is exactly what lets one operad govern several objects at once.
