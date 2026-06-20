---
type: definition
subject: higher-categories
prereqs:
  - "Def - Generalized Operad"
  - "Def - Cartesian Monad"
  - "Def - Algebra for a Monad"
  - "Def - Monoid in a Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $(T, \eta, \mu)$ is a [[Def - Cartesian Monad|cartesian monad]] on a category $\mathcal{E}$ with [[Def - Pullback and Pushout|pullbacks]] and terminal object $1$, and $P$ is a [[Def - Generalized Operad|$T$-operad]] with operation-object $P$, arity $\mathrm{ar} : P \to T1$, unit $e : 1 \to P$, and composition $\mathrm{comp} : P \times_{T1} TP \to P$. An **algebra** for $P$ is an object $X \in \mathcal{E}$ with an action $h$. We write $!_X : X \to 1$ for the unique map to the terminal object, so $T(!_X) : TX \to T1$ grades $TX$ by arity-shape, and $P \times_{T1} TX$ is the pullback of $\mathrm{ar}$ against $T(!_X)$. The full symbol registry is on [[Higher Categories — Generalized Operads via Cartesian Monads]].

---

# Axiom Motivation

An operad is a *theory of operations*; an algebra is a *place where those operations actually act*. The definition is forced by spelling out what "act" should mean and demanding that acting respects the operad's unit and composition. The cleanest analogy is a [[Def - Algebra for a Monad|monad algebra]] or a group action: the operad is the abstract gadget, the algebra is the object it operates on, and the action axioms say the abstract composition law is realized by genuine composition of operations on the object.

Think first about the classical case to fix intuition, then generalize. For the associative operad $\mathrm{Assoc}$ (one $n$-ary operation per $n$), an algebra is a set $X$ on which each $n$-ary operation acts as a map $X^n \to X$ — and "respecting composition" forces all these to come from a single associative binary multiplication, so an $\mathrm{Assoc}$-algebra is exactly a [[Def - Monoid in a Monoidal Category|monoid]]. The general definition must reproduce this: an operation of arity-shape $s$ must act, on an object $X$, as a map from "the $s$-shaped configuration of elements of $X$" to $X$. The $s$-shaped configurations of $X$ are exactly the elements of $TX$ lying over $s$, so the action is a single map
$$h : P \times_{T1} TX \longrightarrow X,$$
out of the pullback "operation together with a matching $T$-shape of inputs". This is the only sensible domain: an operation of arity-shape $s$ can only act on inputs forming a shape-$s$ configuration, which is the matching condition the pullback enforces.

Now the two axioms. The **unit axiom** demands that the unit operation $e$ act as the identity: feeding a single element through the do-nothing operation returns that element. Concretely $h$ composed with the inclusion of $(e, \eta_X) : X \to P \times_{T1} TX$ is the identity $1_X$. Drop it and the unary identity operation could scramble inputs — the algebra would not be a faithful place for the operad to act, and for $\mathrm{Assoc}$ the multiplication's unit law would fail. The **associativity axiom** demands that "act by a grafted operation" equal "act by the pieces, then act by the top operation". This is the compatibility of $h$ with $\mathrm{comp}$ and $\mu$: the two ways of evaluating an operation-of-operations on a configuration agree. Drop it and an algebra would assign *different* results to the same composite operation depending on how it is parenthesized — for $\mathrm{Assoc}$ this is exactly the failure of $x(yz) = (xy)z$. Each axiom is the algebra-level shadow of an operad axiom; together they say the action is a genuine, coherent realization.

There is a structural reformulation that makes the definition inevitable. A $T$-operad $P$ determines a monad $T_P$ on $\mathcal{E}$ — roughly $T_P X = P \times_{T1} TX$, "decorate a $T$-shape of $X$ by an operation of matching arity" — and the operad axioms are exactly what make $T_P$ a monad. An algebra for $P$ *is* an [[Def - Algebra for a Monad|Eilenberg–Moore algebra]] for $T_P$. From this angle the unit and associativity axioms are not chosen; they are the monad-algebra axioms transported through the construction $P \mapsto T_P$, so a reader who knows monad algebras can *derive* the operad-algebra axioms rather than memorize them.

---

# The Definition

Let $P$ be a [[Def - Generalized Operad|$T$-operad]] over a [[Def - Cartesian Monad|cartesian monad]] $(T, \eta, \mu)$ on $\mathcal{E}$.

An **algebra for $P$** (a **$P$-algebra**) is an object $X \in \mathcal{E}$ together with an **action**
$$h : P \times_{T1} TX \longrightarrow X,$$
where the pullback is of $\mathrm{ar} : P \to T1$ against $T(!_X) : TX \to T1$, satisfying:

1. **Unit law.** Acting by the unit operation $e$ is the identity:
$$h \circ \langle e \circ !_X,\; \eta_X \rangle \;=\; 1_X : X \to X,$$
where $\langle e \circ !_X, \eta_X \rangle : X \to P \times_{T1} TX$ pairs the unit operation with the singleton configuration $\eta_X$.

2. **Associativity law.** Acting by a composite operation equals acting by the pieces and then the top operation: the two evident maps
$$P \times_{T1} T\big(P \times_{T1} TX\big) \longrightarrow X$$
— one using $\mathrm{comp}$ then $h$, the other using $T h$ then $h$ (and $\mu_X$) — agree.

A **morphism of $P$-algebras** $(X, h) \to (X', h')$ is a map $f : X \to X'$ with $f \circ h = h' \circ (1_P \times_{T1} Tf)$. The $P$-algebras and their morphisms form the **category of $P$-algebras**, $P\text{-}\mathbf{Alg}$.

---

# Categorical / Structural Definition

The structural statement is: **a $T$-operad $P$ induces a monad $T_P$ on $\mathcal{E}$, and $P$-algebras are exactly the [[Def - Algebra for a Monad|Eilenberg–Moore algebras]] of $T_P$.** Define
$$T_P X \;=\; P \times_{T1} TX,$$
the object "an operation of $P$ together with a $T$-shaped configuration of $X$ of matching arity". The unit $X \to T_P X$ uses the operadic unit $e$ and $\eta_X$ (the singleton configuration decorated by the do-nothing operation); the multiplication $T_P T_P X \to T_P X$ uses operadic composition $\mathrm{comp}$ together with the monad multiplication $\mu_X$ to flatten a configuration-of-(operation-decorated-configurations) into a single operation-decorated configuration. The $T$-operad axioms (unit, associativity) are precisely what make $(T_P, \ldots)$ a [[Def - Monad and Comonad|monad]]. An Eilenberg–Moore algebra for $T_P$ is an object $X$ with $h : T_P X \to X$ satisfying the monad-algebra axioms, which unwind to exactly the unit and associativity laws above. Hence $P\text{-}\mathbf{Alg} \cong (\mathcal{E})^{T_P}$, the Eilenberg–Moore category.

This is more than bookkeeping. It places operad-algebras inside the well-developed theory of monad-algebras, so that *all* the structural results for Eilenberg–Moore categories — limits computed in the base, the free–forgetful [[Def - Free-Forgetful Adjunction|adjunction]], monadicity criteria — apply at once. It also makes the unifying picture precise: a $T$-operad is "a monad presented by $T$-shaped operations", and its algebras are the structures with that operations-package. The endomorphism construction gives the dual perspective: a $P$-algebra structure on $X$ is the same as an operad map $P \to \mathrm{End}(X)$ into the **endomorphism operad** of $X$, exactly as a representation of a group is a map into a general linear group.

---

# Relate to Other Fields / Compression

The slogan is *operad : algebra :: theory : model*. A $T$-operad is a presentation of an algebraic theory by operations of $T$-arity, and its algebras are the models of that theory in $\mathcal{E}$. This is the operadic refinement of universal algebra: where a Lawvere theory presents operations and *equations*, an operad presents operations and *coherent composition*, which is finer — it remembers how operations are built, not just which equations hold. In homotopy theory this finer memory is essential: an $A_\infty$-algebra is an algebra for the $A_\infty$-operad, a "monoid up to coherent homotopy", and the operad records the entire infinite tower of higher associativities that an equational presentation would flatten away.

**True name:** *a $P$-algebra is an Eilenberg–Moore algebra for the monad $T_P$ that $P$ induces, equivalently an operad map $P \to \mathrm{End}(X)$*. When asked "what are the algebras of this operad?", convert $P$ to its monad $T_P$ and recognize $T_P$-algebras as a familiar category; or, dually, write down the endomorphism operad of a candidate $X$ and ask which operations $P$ supplies. Both routes turn an opaque action into a known structure.

---

# Examples / Corollaries

**Is an instance — monoids as algebras for the associative operad.** Over $\mathbf{Set}$ with $T = (-)^{*}$, the associative operad $\mathrm{Assoc}$ has one operation $\nu_n$ of each arity $n$. An algebra is a set $X$ with maps $\nu_n : X^n \to X$, and the operad axioms force $\nu_n$ to be the $n$-fold product of a single associative binary operation $\nu_2$, with $\nu_0$ the unit. So an $\mathrm{Assoc}$-algebra is exactly a [[Def - Monoid in a Monoidal Category|monoid]]. This is the prototype, and it is the operadic explanation of why "monoid" is the most basic algebraic structure.

**Is an instance — commutative monoids as algebras for the commutative operad.** The commutative operad $\mathrm{Comm}$ (which is symmetric, hence strictly a symmetric-operad example, but its algebras illustrate the pattern) has $P(n) = 1$ with $S_n$ acting trivially; its algebras are commutative monoids. The contrast with $\mathrm{Assoc}$ is the cleanest illustration that *the operad is the theory*: same operation-counts, different symmetry, different algebras.

**Is an instance — $T$-algebras as algebras for the terminal $T$-operad.** The terminal $T$-operad $I$ (with $P = T1$, $\mathrm{ar} = 1_{T1}$, every arity-shape having exactly one operation) has $T_I = T$, so its algebras are exactly the [[Def - Algebra for a Monad|Eilenberg–Moore algebras]] for $T$ itself. For $T = (-)^{*}$ these are monoids again; for $T = \mathbb{T}$ they are strict $\omega$-categories. The terminal operad recovers the monad's own algebras, the "no extra coherence" endpoint of the operadic spectrum.

**Is NOT an instance — a set with an arbitrary collection of maps $X^n \to X$.** A set $X$ equipped with *some* maps $X^n \to X$, one for each $n$, is **not** an algebra for any particular operad unless those maps are compatible with a chosen operad's composition and unit. Without the associativity and unit laws relating the arities, the maps are just an unstructured family; the operad is exactly the data that constrains them to cohere. This is the "is NOT" that shows the axioms carry the content.

**Is NOT an instance — a $P$-algebra is not a sub-operad.** It is tempting to conflate "an algebra for $P$" with "a small operad mapping into $P$". They are dual, not the same: a $P$-algebra is a map *out* of the monad $T_P$ onto an object, equivalently a map $P \to \mathrm{End}(X)$ *into* the endomorphism operad; a sub-operad is a map *into* $P$. The algebra is where $P$ acts, not a smaller copy of $P$.

**Calibration check.** Verify that an algebra for the associative operad is a monoid by checking that the binary operation $\nu_2$ generates all $\nu_n$ and that associativity of $\nu_2$ is the operad's associativity law. Verify that algebras for the terminal $T$-operad are $T$-algebras. If you can write the monad $T_P X = P \times_{T1} TX$ and say in one sentence why $T_P$-algebras are $P$-algebras, you have understood the definition.

---

# Unlocked by This

> [!tip] The Unifying Table *(from this chapter)*
> Algebras complete the rightmost column of the chapter's unifying table: across $T = \mathrm{id} / (-)^{*} / \mathbb{T}$, an algebra for the $T$-operad is a monoid-action / operad-algebra / weak-higher-category-of-that-signature. See [[Ex - Reading the unifying table across three monads]].

> [!tip] Batanin–Leinster Weak ω-Categories *(from Higher Category Theory)*
> A **weak ω-category** is defined as an algebra for the initial **contractible** globular operad $L$. The contraction supplies the chosen weak composites and coherence cells, so an $L$-algebra is a globular set with weak, coherent composition in every dimension — the algebraic definition of a higher category (HC7). Algebras for a generalized operad are the exact vehicle.

> [!tip] Homotopy-Coherent Algebra — A∞ and E∞ *(from Algebraic Topology)*
> Algebras for the $A_\infty$-operad are **monoids up to coherent homotopy**, and algebras for the $E_\infty$-operad are coherently-commutative monoids; these are the structures on chain complexes and spaces that compute, for instance, the multiplicative structure of cohomology and the homotopy type of mapping spaces. The operad-algebra framework is what makes "up to coherent homotopy" a precise, manipulable notion.
