---
type: topic
subject: higher-categories
chapter: "Leinster Ch.2, App. A, D"
title: "Higher Categories — Operads and Multicategories"
tags: [category-theory, higher-categories, foundations]
---

# Notation Registry

One standing convention frames the whole chapter. The word **operad** comes in two flavours that must be kept apart: **symmetric** (the operations carry symmetric-group actions permuting their inputs) and **plain** or **non-symmetric** (no such action; inputs are ordered). Unless a statement says otherwise, "operad" means the symmetric flavour, because that is the one tracking genuinely multilinear and commutative examples; the plain flavour is the right one when inputs are intrinsically ordered (words, planar trees). The same split applies to multicategories. A second convention: we work in a symmetric monoidal base $(\mathcal{V}, \otimes, \mathbb{1})$ — usually $\mathbf{Set}$, but $\mathbf{Top}$ (topological operads), $\mathbf{Vect}_k$ or chain complexes (algebraic operads) are the cases that matter — and we suppress associators and unitors by [[Thm - Mac Lane Coherence Theorem|coherence]], treating $\otimes$ as strict when convenient.

- $\mathcal{M}, \mathcal{N}$ — multicategories; their objects are **colours** $a, b, c$
- $\mathcal{M}(a_1, \dots, a_n; b)$ — set of **multimaps** with $n$ inputs $a_1, \dots, a_n$ and output $b$; $n$ is the **arity**
- $\theta \circ (\varphi_1, \dots, \varphi_k)$ — **substitution**: graft $\varphi_i$ onto the $i$th input of $\theta$
- $P, Q$ — operads; $P(n)$ — the set (object) of **$n$-ary operations**; $\mathrm{id} \in P(1)$ — the unit operation
- $\gamma : P(k) \otimes P(n_1) \otimes \dots \otimes P(n_k) \to P(n_1 + \dots + n_k)$ — operadic **composition**
- $\circ_i : P(k) \otimes P(n) \to P(k + n - 1)$ — **partial composition** (insert into the $i$th slot)
- $S_n$ — symmetric group; $\theta \cdot \sigma$ — the right $S_n$-action on $P(n)$; $\sigma\langle n_1, \dots, n_k\rangle$ — **block permutation**
- $\mathrm{End}_X(n) = \mathrm{Hom}(X^{\otimes n}, X)$ — the **endomorphism operad** of an object $X$
- $\rho : P \to \mathrm{End}_X$, or $\rho_n : P(n) \otimes X^{\otimes n} \to X$ — a **$P$-algebra structure** on $X$
- $\mathrm{SymSeq}(\mathcal{V})$ — **symmetric sequences** ($S$-modules); $\circ$ — the **composition product**; $I$ — its unit (concentrated in arity $1$)
- $T_P(X) = \coprod_n P(n) \otimes_{S_n} X^{\otimes n}$ — the **operadic monad** (Schur functor) of $P$; $\otimes_{S_n}$ — coinvariants
- $\mathcal{F}(E)$ — the **free operad** on a symmetric sequence $E$; its operations are $E$-labelled rooted trees
- $\mathrm{Assoc}, \mathrm{Comm}, \mathrm{Lie}$ — the associative, commutative, Lie operads; $\mathrm{Assoc}^{\mathrm{ns}}$ — non-symmetric associative
- $E_n$ — the **little $n$-disks** (or little $n$-cubes) operad; $\Omega^n Y$ — the **$n$-fold loop space**; $A_\infty, E_\infty$ — the homotopy-coherent associative and commutative operads

---

# Motivation

Here is the entire chapter in one sentence: an operad is the abstract pattern of a single algebraic structure — its operations and the equations among them — divorced from any particular set those operations act on. Ordinary category theory is built around morphisms with one input: functions, [[Def - Group|group]] [[Def - Homomorphism|homomorphisms]], continuous maps each eat a single argument, and a category records exactly these. But mathematics is full of operations that eat *several* arguments and cannot honestly be reduced to one-argument pieces — the multiplication of a [[Def - Ring|ring]], the bracket of a Lie algebra, an $n$-linear form, the concatenation of loops. A [[Def - Multicategory|multicategory]] is the structure that holds these multi-input operations: it has objects and, for each tuple of objects, a set of multimaps out of that tuple, composing by substitution. When all the inputs and outputs share a single type, a multicategory becomes an [[Def - Operad|operad]]: a sequence $P(n)$ of "$n$-ary operations of one type", with a unit, a symmetric-group action permuting inputs, and a composition $\gamma$ that plugs operations into the slots of operations.

The payoff is that **choosing an operad chooses a kind of algebra**. The associative operad's [[Def - Algebra for an Operad|algebras]] are monoids; the commutative operad's are commutative monoids; the Lie operad's are Lie algebras; the little-disks operad's (up to homotopy) are iterated loop spaces. One definition of "algebra over an operad" subsumes monoid, ring, associative algebra, commutative algebra, Lie algebra, and their homotopy-coherent versions, distinguished only by which operad you plug in. The operad is the *type*; an algebra is a *realisation* of that type on an object, given by a morphism $P \to \mathrm{End}_X$ into the [[Def - Endomorphism Operad|endomorphism operad]] of all genuine operations on $X$.

The structural backbone of the chapter is a single chain of identifications, each licensing the next, that places operads inside the most familiar algebra there is:

$$
\underbrace{\text{operad}}_{\text{a type of algebra}}
\;=\;
\underbrace{\text{one-object multicategory}}_{\text{collapse the colours}}
\;=\;
\underbrace{\text{monoid in symmetric sequences}}_{(\mathrm{SymSeq}, \circ, I)}
\;\rightsquigarrow\;
\underbrace{\text{a monad } T_P}_{\text{whose algebras are } P\text{-algebras}}.
$$

The middle equality is [[Thm - Operads as Monoids in Symmetric Sequences|the theorem that an operad is a monoid in symmetric sequences]], which dissolves the apparently ad hoc operad axioms into "it is a monoid, and you already know what those are" — exactly as a ring is a [[Def - Monoid in a Monoidal Category|monoid in Ab]] and a [[Def - Monad and Comonad|monad]] is a monoid in endofunctors. The final arrow realises every operad as a special kind of monad, the "analytic" ones built from a graded pile of operations, which is why operad theory is a refinement of monad theory and why everything from [[Thm - The Free Operad|free operads]] to homotopy-coherent resolutions follows from monoidal algebra.

The chapter assumes fluency in ordinary category theory: [[Def - Category|categories]], [[Def - Functor|functors]], [[Def - Natural Transformation|natural transformations]] (Chapter I), [[Def - Adjunction|adjunctions]] (Chapter IV), [[Def - Monoidal Category|monoidal categories]], [[Def - Monoid in a Monoidal Category|monoids in them]], and [[Def - Monad and Comonad|monads]] (Chapter V). From outside category theory the topological examples lean on the loop space and [[Def - Higher Homotopy Group|higher homotopy groups]], recalled at point of use. No prior exposure to operads is assumed — that is what we are building. This is Leinster's Chapter 2 with Appendices A (symmetric structures) and D (trees), supplemented by May's topological examples.

---

# Concept Map

## §1 Classical Multicategories

- **[[Def - Multicategory]]**
	- A **multicategory** (coloured operad) has objects (colours) and, for each tuple $(a_1, \dots, a_n)$ and object $b$, a set of multimaps $\mathcal{M}(a_1, \dots, a_n; b)$ — the "operations with $n$ inputs and one output" — with identities, a substitution composition $\theta \circ (\varphi_1, \dots, \varphi_k)$ (graft each $\varphi_i$ onto the $i$th input of $\theta$), and (in the symmetric flavour) an $S_n$-action permuting inputs, all subject to associativity, unit, and equivariance axioms. It is to multilinear maps what a [[Def - Category|category]] is to functions: a category is the special case where only arity-$1$ multimaps are non-empty. A multicategory arising from a tensor product (with $\mathcal{M}(a_1, \dots, a_n; b) = \mathcal{V}(a_1 \otimes \dots \otimes a_n, b)$) is called **representable**, and a representable multicategory is exactly a [[Def - Monoidal Category|monoidal category]].

> [!tip] Unlocked: [[Def - Generalized Multicategory|Generalized Multicategories]] *(from Higher Categories — [[Def - Generalized Operad|Generalized Operads]])*
> Replacing the implicit free-monoid monad $(-)^*$ (lists of inputs) by an arbitrary **cartesian monad** $T$ produces **$T$-[[Def - Multicategory|multicategories]]**, the framework unifying [[Def - Category|categories]] ($T = \mathrm{id}$), classical multicategories ($T = (-)^*$), and **globular operads** ($T$ the free strict $\omega$-category monad) under one definition. The whole next chapter is this generalisation.

> [!tip] Unlocked: PROPs and Wiring Diagrams *(from Categorical Systems Theory)*
> Allowing operations with several *outputs* as well as several inputs gives **PROPs** and the **wiring-diagram operads** of categorical systems theory and **compositional game theory**; these are the combinatorial backbone for composing open systems, Bayesian networks, and processes — the user's agent-foundations program runs on exactly this multi-input/multi-output substitution calculus.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 Classical Multicategories]]

- **[[Ex - A category is a multicategory with unary maps only]]** (⭐⭐)
	- Show that ordinary [[Def - Category|categories]] are exactly multicategories whose only non-empty multimap sets are unary, and that the unary part of any multicategory is a category. Drills vacuous-axiom discharge and arity-count closure.

- **[[Ex - The multicategory of multilinear maps]]** (⭐⭐)
	- Verify that $k$-vector spaces with multilinear maps form a symmetric multicategory $\mathbf{Vect}_k^{\otimes}$, and that it is representable with representing objects the tensor products — so the universal property of $\otimes$ *is* representability.

- **[[Ex - Every symmetric monoidal category has an underlying multicategory]]** (⭐⭐⭐)
	- Build the underlying multicategory $\mathcal{V}^{\otimes}$ of a symmetric [[Def - Monoidal Category|monoidal category]] and prove the converse: representable multicategories are monoidal categories, with all coherence coming free from uniqueness of representing objects.

## §2 Classical Operads

- **[[Def - Operad]]**
	- An **operad** $P$ is a sequence of sets (objects) $P(n)$ of $n$-ary operations, with a unit $\mathrm{id} \in P(1)$, an $S_n$-action, and a composition $\gamma$ plugging operations into operations, satisfying associativity, unit, and equivariance. It is exactly a **one-object [[Def - Multicategory|multicategory]]** (collapse the colours) and exactly a **monoid in symmetric sequences** ([[Thm - Operads as Monoids in Symmetric Sequences|the structural theorem]]). The associative operad $\mathrm{Assoc}(n) = S_n$, commutative operad $\mathrm{Comm}(n) = *$, and Lie operad $\mathrm{Lie}(n)$ (dimension $(n-1)!$) are the basic examples; a **plain** operad drops the $S_n$-action, the right setting for ordered inputs.

- **[[Def - Endomorphism Operad]]**
	- For an object $X$ of a closed symmetric [[Def - Monoidal Category|monoidal category]], the **endomorphism operad** is $\mathrm{End}_X(n) = \mathrm{Hom}(X^{\otimes n}, X)$, the genuine $n$-ary operations on $X$, with composition by substitution of maps, unit $1_X$, and the $S_n$-action permuting tensor factors. Its axioms are *inherited* from associativity of composition in the ambient category — the [[Def - Operad|operad]] axioms were reverse-engineered to be "whatever $\mathrm{End}_X$ satisfies". It is the universal target for operad actions: $\mathrm{Operad}(P, \mathrm{End}_X)$ is the set of $P$-algebra structures on $X$.

> [!tip] Unlocked: A∞ and E∞ [[Def - Operad|Operads]] *(from Operadic Homotopy Theory)*
> Replacing strict equations by coherent [[Def - Homotopy|homotopies]] gives the **A∞-operad** (associativity up to a contractible space of higher homotopies, the associahedra) and the **E∞-operad** (commutativity up to all higher homotopies). An **E∞-ring** is an E∞-algebra in spectra, the homotopical replacement for a commutative ring and the basic object of modern stable homotopy theory and **derived algebraic geometry**.

> [!tip] Unlocked: Koszul Duality *(from Operadic Homotopy Theory)*
> Quadratic operads come in dual pairs: **Koszul duality** sends $\mathrm{Comm}$ to $\mathrm{Lie}$ and $\mathrm{Assoc}$ to itself, packaging the relationship between an algebra type and its deformation/cohomology theory. It is the operadic shadow of the bar–cobar adjunction and underlies **deformation quantisation**.

> [!note] Exercise Index — §2
> [[Exercise Index - §2 Classical Operads]]

- **[[Ex - The associative and commutative operads]]** (⭐⭐)
	- Define $\mathrm{Assoc}(n) = S_n$ and $\mathrm{Comm}(n) = *$, prove their algebras are [[Def - Monoid in a Monoidal Category|monoids]] and commutative monoids, and exhibit the unique operad map $\mathrm{Assoc} \to \mathrm{Comm}$ as "commutative $\Rightarrow$ associative". The $S_n$-action is the commutativity dial.

- **[[Ex - Symmetric versus plain operads]]** (⭐⭐)
	- Show the symmetrisation $\mathrm{Sym}(Q)(n) = Q(n) \times S_n$ is left adjoint to forgetting the action, that $\mathrm{Sym}(\mathrm{Assoc}^{\mathrm{ns}}) = \mathrm{Assoc}$, and that $\mathrm{Comm}$ is *not* any symmetrisation (its action is not free).

- **[[Ex - Verifying the endomorphism operad axioms]]** (⭐⭐)
	- Verify $\mathrm{End}_X$ is a symmetric operad from first principles, and prove a [[Def - Algebra for an Operad|P-algebra]] is exactly a morphism $P \to \mathrm{End}_X$; read $\mathrm{End}_X(1)$ as the endomorphism monoid and $\mathrm{End}_X(0)$ as the elements of $X$.

- **[[Thm - Operads as Monoids in Symmetric Sequences]]**
	- $(\mathrm{SymSeq}(\mathcal{V}), \circ, I)$ is a monoidal category under the **composition product** $\circ$, and an [[Def - Operad|operad]] is exactly a [[Def - Monoid in a Monoidal Category|monoid]] in it: the operadic composition $\gamma$ is the monoid multiplication, the unit $\mathrm{id}$ is the monoid unit, and equivariance is absorbed into the definition of $\circ$. As a corollary, $P \mapsto T_P$ realises every operad as a [[Def - Monad and Comonad|monad]] whose algebras are the $P$-algebras — operads are the "analytic" monads. This is the structural definition of an operad, replacing three axioms with "monoid in symmetric sequences".

## §3 Algebras, Free Operads, and Examples

- **[[Def - Algebra for an Operad]]**
	- A **$P$-algebra** is an object $X$ with structure maps $\rho_n : P(n) \otimes X^{\otimes n} \to X$ (equivalently a morphism $P \to \mathrm{End}_X$, equivalently an algebra for the monad $T_P$), satisfying associativity, unit, and equivariance: "the abstract operations of $P$ become genuine operations on $X$, coherently". Choosing $P$ chooses the kind of algebra — monoid, commutative monoid, Lie algebra, $n$-fold loop space. The free $P$-algebra on $X$ is $T_P(X) = \coprod_n P(n) \otimes_{S_n} X^{\otimes n}$.

> [!tip] Unlocked: Markov Categories and the Probability Monad *(from Categorical Probability)*
> The structure "$P(n) \otimes X^{\otimes n} \to X$" is the operadic face of an *action*, and probability monads (Giry, distribution) are commutative monads whose algebras are convex/affine spaces; **Markov categories** package the copy-discard structure of probability as a symmetric monoidal category whose underlying multicategory holds the multi-input stochastic maps. The user's categorical-probability and agent-foundations program reads conditioning and marginalisation as exactly such multi-input operations.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 Algebras, Free Operads, and Examples]]

- **[[Thm - The Free Operad]]**
	- The forgetful functor from [[Def - Operad|operads]] to symmetric sequences has a left [[Def - Adjunction|adjoint]] $\mathcal{F}$, the **free operad**: $\mathcal{F}(E)(n) = \coprod_T \bigotimes_{v} E(|v|)$ over $E$-labelled rooted trees with $n$ leaves, composition by grafting, unit the trivial tree. It is the free monoid $\coprod_n E^{\circ n}$ in $(\mathrm{SymSeq}, \circ, I)$, and its universal property says an operad map $\mathcal{F}(E) \to P$ is just a choice of operation in $P$ for each generator. Every operad is a quotient $\mathcal{F}(E)/R$ — a presentation by generators and relations.

- **[[Ex - The free operad on one binary operation]]** (⭐⭐⭐)
	- Compute $\mathcal{F}(E)$ for one binary generator: planar binary trees counted by Catalan numbers, algebras are magmas, and the quotient by associativity gives $\mathrm{Assoc}^{\mathrm{ns}}$. The doorway to $A_\infty$ via the associahedra.

- **[[Ex - An operad induces a monad whose algebras agree]]** (⭐⭐⭐)
	- Build the operadic monad $T_P(X) = \coprod_n P(n) \otimes_{S_n} X^n$, prove $P$-algebras are its [[Def - Algebra for a Monad|Eilenberg–Moore algebras]], and recognise $T_{\mathrm{Assoc}}$ (lists, free monoid) and $T_{\mathrm{Comm}}$ (multisets, free commutative monoid).

- **[[Thm - May's Recognition Principle]]**
	- The **little $n$-disks operad** $E_n$ acts on $n$-fold loop spaces $\Omega^n Y$ (place maps-out-of-disks on little disks), and **group-like $E_n$-algebras are exactly $n$-fold loop spaces** up to weak equivalence. The configuration spaces $E_n(k)$ encode "associative and commutative up to coherent homotopy, to the degree $n$ [[Def - Dimension|dimensions]] allow": $E_1 \simeq \mathrm{Assoc}$, $E_\infty \simeq \mathrm{Comm}$. For $n = \infty$, group-like $E_\infty$-spaces are the infinite loop spaces, equivalently connective **spectra**.

- **[[Ex - Loop spaces are algebras over the little intervals operad]]** (⭐⭐⭐)
	- Construct the $E_1$-action on $\Omega Y$, show $E_1 \simeq \mathrm{Assoc}^{\mathrm{ns}}$ (so $E_1$-algebras are $A_\infty$-monoids), and state what [[Thm - May's Recognition Principle|recognition]] adds and why a single homotopy-associative product cannot deloop.

---

# Sources and Targets

**Targets — What do we usually try to prove?**

The recurring goals of operad theory cluster into five kinds. First, **identify the algebras of an operad**: given $P$, show $\mathrm{Alg}_P$ is a known category — monoids, Lie algebras, loop spaces. This is the most common target, and it is achieved by reading the algebra structure off the low-arity generators and the relations. Second, **present an operad by generators and relations** $\mathcal{F}(E)/R$, which makes its (co)homology, deformations, and Koszul duality computable. Third, **compare two operads via morphisms** $P \to Q$, since an operad map induces a restriction $\mathrm{Alg}_Q \to \mathrm{Alg}_P$ and so encodes implications between structure types ("every commutative monoid is a monoid"). Fourth, **recognise a structure as operadic and exploit it** — the spectacular case being May's recognition principle, where an $E_n$-action *characterises* loop spaces rather than merely decorating them. Fifth, **resolve an operad up to homotopy** ($A_\infty$, $E_\infty$), so that its algebras become invariant under weak equivalence; this is the whole point of operads in homotopy theory.

**Sources — What assumptions do we usually leverage?**

The assumptions that drive these proofs are equally patterned. The richest source is **a structure given by operations and equations** — a product satisfying associativity, a bracket satisfying Jacobi — which is a presentation $\mathcal{F}(E)/R$ and hence an operad. A second is **a graded composable family with substitution** (trees, configurations, wiring diagrams, terms): substitution-closure plus associativity make it an operad, and the cleanest check is "is it a monoid in symmetric sequences?". A third is **a multiplication that is associative or commutative only up to homotopy, parametrised by a space** — the signature of a topological operad, where the homotopy type of the configuration spaces measures the coherence. A fourth is **a monad whose underlying functor is a sum of symmetric powers** $\coprod_n P(n) \otimes_{S_n} X^{\otimes n}$, which is automatically $T_P$ for an operad. The routing is direct: presentations route to free-operad and Koszul-duality machinery; substitution families route to the monoid-in-symmetric-sequences theorem; up-to-homotopy multiplications route to recognition principles; analytic monads route to operadic refinements of monad theory.

---

# Legal Operations

**Legal operations:**

1. **Compose operations by substitution.** The fundamental move: plug operations into the slots of an operation, $\theta \circ (\varphi_1, \dots, \varphi_k)$ or partially $\theta \circ_i \varphi$. Every operadic computation is a sequence of substitutions, and associativity guarantees the result is independent of the order of grafting. *Trigger:* a tree or wiring diagram of operations. *Pattern:* "graft bottom-up or top-down — by associativity they agree".

2. **Collapse colours to pass between multicategory and operad.** A one-object [[Def - Multicategory|multicategory]] is an [[Def - Operad|operad]]; the endomorphism multimaps at a single colour of any multicategory form an operad. Use this to import multicategory results to operads and vice versa. *Trigger:* a single-type algebraic structure (operad) versus a multi-type one (multicategory).

3. **Specialise or compute at a fixed arity.** Read $P(0)$ for constants (units, zeros), $P(1)$ for the monoid of unary operations, $P(2)$ for the generating products, $P(3)$ for the relations. Most questions about an operad's algebras are answered by inspecting low arities. *Trigger:* an unfamiliar operad. *Pattern:* "what are the constants ($P(0)$), the unary symmetries ($P(1)$), the products ($P(2)$), and the relations ($P(3)$)?".

4. **Read an algebra as a map into the endomorphism operad.** A [[Def - Algebra for an Operad|P-algebra]] structure on $X$ is a morphism $P \to \mathrm{End}_X$; building algebra structure means choosing where each generator goes, with relations checked once. *Trigger:* "make $X$ a $P$-algebra". *Pattern:* "send each generating operation to a genuine operation on $X$, then verify the relations".

5. **Track the symmetric-group action through composition (equivariance).** The $S_n$-action interacts with $\gamma$ by the block-permutation calculus; equivariance is what makes constructions on coinvariants (the operadic monad, the composition product) well-defined. *Trigger:* permuting inputs, or defining a map out of a $\otimes_{S_n}$ quotient. *Pattern:* "the well-definedness check on coinvariants *is* equivariance".

6. **Build free objects and presentations.** The [[Thm - The Free Operad|free operad]] $\mathcal{F}(E)$ on generators is the operad of $E$-labelled trees; every operad is $\mathcal{F}(E)/R$. Use the universal property to construct operad maps with no coherence checking, and use presentations to compute. *Trigger:* "generators with no/some relations". *Pattern:* "free operad = trees; relations = tree-collapsing congruence".

7. **Suppress coherence by Mac Lane's theorem, and recover coherence from universal properties.** Work as if $\otimes$ is strict ([[Thm - Mac Lane Coherence Theorem|coherence]]); when assembling structure from representing objects, get the associator/unitors free from uniqueness. *Trigger:* a forest of associator [[Def - Isomorphism|isomorphisms]], or a construction from universal objects.

8. **Realise an operad as a monad and transfer monad technology.** Via $P \mapsto T_P$, import free–forgetful adjunctions, bar resolutions, and Eilenberg–Moore algebras to operads. *Trigger:* wanting free algebras, resolutions, or monadicity for operadic algebras.

**Illegal but tempting operations:**

> [!warning] 1. Treating $\mathrm{Assoc}$ and $\mathrm{Comm}$ as "the same up to the symmetric action"
> It is tempting to say $\mathrm{Assoc}(n) = S_n$ and $\mathrm{Comm}(n) = *$ differ only by quotienting out the action, so the operads are "morally equal". They are not: $\mathrm{Assoc}$-algebras are monoids, $\mathrm{Comm}$-algebras are *commutative* monoids, and there is no operad map $\mathrm{Comm} \to \mathrm{Assoc}$ recovering the binary product as commutative — $S_n$ has no fixed point under right multiplication for $n \geq 2$. **Counterexample:** the free monoid on two generators is an $\mathrm{Assoc}$-algebra but not a $\mathrm{Comm}$-algebra. **Repair:** the only legal direction is $\mathrm{Assoc} \to \mathrm{Comm}$ (collapse $S_n$ to a point), inducing $\mathbf{CMon} \hookrightarrow \mathbf{Mon}$; commutativity is genuinely extra symmetric structure, irreducible to the plain world.

> [!warning] 2. Forgetting the automorphism quotient in the free operad
> When building $\mathcal{F}(E)$ over $\mathbf{Vect}_k$ or chain complexes, it is tempting to take $\mathcal{F}(E)(n) = \bigoplus_T \bigotimes_v E(|v|)$ as a bare sum of tensor products. **Counterexample:** a tree $T$ with a non-trivial automorphism (e.g. a symmetric corolla with a symmetric generator) contributes its labelling object's *coinvariants* under $\mathrm{Aut}(T)$, not the full tensor product; ignoring this over-counts and breaks the universal property. **Repair:** use $\mathcal{F}(E)(n) = \bigoplus_T (\bigotimes_v E(|v|))_{\mathrm{Aut}(T)}$; in $\mathbf{Set}$ (and for plain operads with planar trees, no symmetries) the issue is invisible, which is why it is easy to forget.

> [!warning] 3. Assuming a homotopy-associative $H$-space with inverses is a loop space
> The early hope was "homotopy-associative $H$-space + homotopy inverses $\Rightarrow$ loop space". **Counterexample:** there exist homotopy-associative $H$-spaces that are not loop spaces; a single associativity homotopy does not supply the pentagon and higher coherences needed for a delooping. **Repair:** demand a full [[Thm - May's Recognition Principle|E₁-algebra]] structure (associativity up to *coherent* homotopy, the associahedra) *and* group-likeness; then May's recognition principle delivers a loop space. The operad supplies precisely the higher coherences that a bare $H$-space lacks.

> [!warning] 4. Defining the composition product without the symmetric coinvariants
> When constructing $(\mathrm{SymSeq}, \circ)$, it is tempting to set $(P \circ Q)(n)$ as a plain sum over partitions, omitting the $\otimes_{S_k}$ coinvariants and inductions. **Counterexample:** the resulting product is the *non-symmetric* one; its monoids are plain operads, and equivariance is lost, so one wrongly concludes symmetric and non-symmetric operads have the same theory. **Repair:** include $\otimes_{S_k}$ and $\mathrm{Ind}$ exactly so that equivariance is absorbed; this is what makes monoids for $\circ$ be *symmetric* operads ([[Thm - Operads as Monoids in Symmetric Sequences|the structural theorem]]).

---

# Problem-Solving Strategy

The first question to ask of any operad problem is *which way am I going*: am I given an operad and asked about its algebras, or given a structure and asked which operad governs it? These are the two halves of the subject. If you are **given an operad** $P$ and want its algebras, inspect the low arities in order — $P(0)$ for constants the algebra must carry, $P(1)$ for the monoid of unary operations, $P(2)$ for the generating products, $P(3)$ for the relations among them — and assemble the classical structure. The associative and commutative operads are the calibration: both have a binary generator, but $\mathrm{Assoc}(n) = S_n$ remembers order (monoids) while $\mathrm{Comm}(n) = *$ forgets it (commutative monoids), and the difference is *entirely* in the $S_n$-action. Whenever a problem turns on commutativity, it turns on the symmetric structure.

If you are **given a structure** and want its operad, look for operations of various arities composing by substitution. If the operations have intrinsic order (words, planar trees, non-commutative products), it is a [[Def - Operad|plain operad]]; if inputs are interchangeable, symmetric. The cleanest way to verify the axioms is rarely to check them one by one — instead recognise the structure as a **monoid in symmetric sequences** ([[Thm - Operads as Monoids in Symmetric Sequences|the structural theorem]]), which reduces the operad axioms to the single, familiar monoid axioms and absorbs equivariance into the composition product. If the structure is *free* — generators with no relations — it is a [[Thm - The Free Operad|free operad]], the operad of labelled trees, and its algebras are the corresponding "magma-like" structures before relations.

For **building algebra structures**, the move is always the same: a [[Def - Algebra for an Operad|P-algebra]] is a morphism $P \to \mathrm{End}_X$ into the [[Def - Endomorphism Operad|endomorphism operad]], so choose where each *generator* goes and verify the *relations* once; freeness handles all compositions automatically. For **comparing structure types**, build an operad morphism $P \to Q$ and remember the direction reversal: a $Q$-algebra is automatically a $P$-algebra (restriction along the map), so "is every $Q$-algebra a $P$-algebra?" becomes the finite, checkable question "is there an operad map $P \to Q$?".

For the **topological and homotopical** problems, the governing principle is that the *homotopy type of the configuration spaces* measures coherence. A strict equation becomes a contractible space of operations; partial commutativity becomes a connected-but-not-contractible space; the dimension $n$ of the little disks operad dials from associative ($E_1 \simeq \mathrm{Assoc}$) to commutative ($E_\infty \simeq \mathrm{Comm}$) by controlling how much room the disks have to permute. When a multiplication is associative "only up to homotopy", do not ask "does a homotopy exist?" but "what is the homotopy type of the space of operations?" — and an operad is the device that records it. Recognition principles then convert *having* such a structure into *being* a known object (a loop space, a spectrum), provided you also check group-likeness.

The single unifying question of the chapter is: **what kind of algebra is this, and what is the operad that presents it?** Every problem here is an instance — identifying algebras, presenting operads, comparing structures, recognising loop spaces — of pinning down the correspondence between a type of algebra and the operad whose algebras it is.

---

# Most Reusable Properties

- **[[Def - Operad|Operad]] = one-object [[Def - Multicategory|multicategory]] = monoid in symmetric sequences.** The triple identity is the master tool: it lets you check operad axioms by checking monoid axioms, import multicategory results by collapsing colours, and remember the definition without the three-axiom apparatus. **Typical use:** when verifying that a graded composable family is an operad, exhibit it as a monoid for the composition product $\circ$, where equivariance is automatic; this is far cleaner than the axiom-by-axiom check.

- **[[Def - Algebra for an Operad|Algebra over P]] = morphism $P \to \mathrm{End}_X$ = algebra for the monad $T_P$.** The three forms of an algebra structure are interchangeable, and each is the right tool for a different job. **Typical use:** to *build* an algebra, use the morphism form (choose generators' images); to *study all algebras at once*, use the monad form (free–forgetful adjunction, Eilenberg–Moore); to *compute*, use the structure-map form $\rho_n : P(n) \otimes X^{\otimes n} \to X$.

- **[[Thm - The Free Operad|Free operad]] = operad of labelled trees; every operad is $\mathcal{F}(E)/R$.** The universal property builds operad maps with no coherence checking, and the presentation form makes (co)homology and Koszul duality computable. **Typical use:** to define a complicated family of operations as a single operad map, present the source as a free operad and specify only the generators' images; the universal property forces everything else.

- **The $S_n$-action is the commutativity dial.** From the $S_n$-set structure of $P(n)$ you can read how commutative the algebras are: free action means fully non-commutative (each ordering a distinct operation), trivial action means fully commutative. **Typical use:** to predict an unfamiliar operad's algebras, inspect the $S_n$-action on $P(2)$ and $P(n)$ — and to detect that an operad is *not* a symmetrisation, test whether the action is free.

- **Configuration-space homotopy type = coherence (topological operads).** For an operad in $\mathbf{Top}$, the homotopy type of $P(k)$ records how strictly the algebra axioms hold; $E_n(2) \simeq S^{n-1}$ gives a degree-$(n-1)$ bracket on homology. **Typical use:** to decide what algebraic operations an $E_n$-algebra carries on its (co)homology, read them off the topology of the configuration spaces — the Browder bracket and Dyer–Lashof operations come directly from $E_n(2)$ and the $\Sigma_p$-structure of $E_n(p)$.

---

# Bridges

1. **Monoidal categories and the master table of monoids.** An [[Def - Operad|operad]] is a [[Def - Monoid in a Monoidal Category|monoid]] in $(\mathrm{SymSeq}, \circ, I)$, taking its place in the table where a ring is a monoid in $(\mathbf{Ab}, \otimes)$, a $k$-algebra in $(\mathbf{Vect}_k, \otimes)$, and a [[Def - Monad and Comonad|monad]] in $([\mathcal{C},\mathcal{C}], \circ)$. The construction creating the bridge is the *composition product* $\circ$ on symmetric sequences: $(P \circ Q)(n)$ is "a $P$-operation with its slots filled by $Q$-operations, up to symmetric relabelling", and substituting one symmetric sequence into another is the monoidal product whose monoids are operads. The lesson transferred is that "associative unital structure" is one definition, and exotic algebraic objects come from exotic ambient monoidal categories — here, substitution of arity-graded operations.

2. **Monads and universal algebra.** Every operad $P$ yields a monad $T_P(X) = \coprod_n P(n) \otimes_{S_n} X^{\otimes n}$ whose [[Def - Algebra for a Monad|algebras]] are the $P$-algebras, identifying operads with the *analytic* (Schur-polynomial) monads — those whose underlying endofunctor is a sum of arity-graded symmetric-power pieces. The construction is the Schur functor: each $P(n)$ is a "coefficient" and $T_P$ is a "power series in $X$". The bridge runs both ways: monad technology (free–forgetful adjunctions, bar resolutions, Eilenberg–Moore, monadicity) applies to operadic algebras, and conversely operads give a *presentation* of certain monads by generators and relations that opaque monads lack. This is why the free [[Thm - The Free Operad|operad]] and the bar resolutions of $A_\infty$/$E_\infty$ are computable.

3. **Algebraic topology and the recognition of loop spaces.** The little $n$-disks operad $E_n$ in $\mathbf{Top}$ acts on $n$-fold loop spaces by placing maps-out-of-disks on little disks, and [[Thm - May's Recognition Principle|May's recognition principle]] makes the action a *complete* characterisation: group-like $E_n$-algebras are exactly $n$-fold loop spaces. The construction is the bar/classifying-space machine, an inverse to looping. The bridge explains the abelianness of [[Def - Higher Homotopy Group|higher homotopy groups]] (Eckmann–Hilton: $E_n(2) \simeq S^{n-1}$ is connected for $n \geq 2$, forcing homotopy-commutativity) and, for $n = \infty$, identifies group-like $E_\infty$-spaces with connective **spectra**, the doorway to stable homotopy theory and **E∞-ring spectra**.

4. **Algebraic geometry and derived structures (motivational).** Commutative rings are $\mathrm{Comm}$-algebras in $\mathbf{Ab}$, so [[Def - Operad|operads]] sit beneath the entire ring–geometry dictionary; their homotopy-coherent versions are the engine of *derived* algebraic geometry. The bridge: an **E∞-ring** is the operadic replacement for a commutative ring valid in the homotopical world, and the derived category of a scheme, the cotangent complex, and André–Quillen cohomology are all controlled by resolutions of the commutative operad (its Koszul dual being the Lie operad, governing the tangent/deformation theory). A reader who has met the affine-scheme/commutative-ring duality should read "E∞-ring" as "commutative ring done up to coherent homotopy", and the operad as what makes "coherent homotopy" precise.

5. **Categorical systems theory and the user's research program.** Multicategories and their multi-output cousins (PROPs, wiring-diagram operads) are the compositional calculus of open systems — Bayesian networks, **Markov categories**, compositional game theory, the agent-foundations diagrams of categorical systems theory. The bridge is substitution: wiring the output of one process into the input slots of another is operadic composition, and an operad/multicategory is the precise structure governing how systems compose. For categorical probability specifically, conditioning and marginalisation are multi-input stochastic operations living in the underlying multicategory of a Markov category, and the commutativity of the probability monad is exactly the symmetric (commutative-operad) structure on its operations.

---

# Insights

**The unifying frame.** The whole subject is the observation that *a type of algebra and the operad whose algebras it is are the same information*. To specify a kind of algebra — monoid, Lie algebra, loop space — is to specify an operad; to give such an algebra is to give a morphism from that operad to an endomorphism operad. This collapses the apparent diversity of algebraic structures into a single parametrised notion, and it relocates every question about a class of algebras (their free objects, their cohomology, their deformations, their homotopy theory) to a question about the *one* operad governing them, where it becomes uniform. The operad is the platonic structure; an algebra is a representation of it on an object, exactly as a group is the platonic symmetry and a $G$-set is a representation.

**The true name and the trigger.** The operational name of an operad is "the symmetries-and-composition data of a single algebraic structure", and the trigger-reaction pattern is: *see operations of varying arity that compose by substitution, with no constraint forcing them to come from a binary one — reach for an operad*. The qualifier matters. Associativity is generated by a binary product, so monoids can be described by a monoidal product alone; but Jacobi is a genuine arity-three relation, so Lie algebras *cannot* be captured by a tensor product and genuinely need the Lie operad. The diagnostic for "do I need an operad, or does a monoidal structure suffice?" is exactly "are there relations not generated by the binary operation?". When yes, the operad is indispensable.

**Dimension is commutativity, made precise.** The single most beautiful insight of the chapter is that the little-disks operads $E_n$ interpolate from associative to commutative *by dimension*, because the dimension controls how much room the configurations have to move past each other. In $E_1$ (intervals on a line) nothing can slide past anything, so the algebras are merely associative; in $E_n$ for $n \geq 2$ disks can be rotated around each other ($E_n(2) \simeq S^{n-1}$ is connected), forcing homotopy-commutativity; as $n \to \infty$ the configurations have unlimited room and the algebras are fully commutative up to coherent homotopy. This is the operadic statement of the Eckmann–Hilton argument from the [[Def - Higher Homotopy Group|higher homotopy group]] page — "more dimensions force more commutativity" — and it explains in one stroke why loop spaces are associative, double loop spaces have a commutator-like Browder bracket, and infinite loop spaces are commutative. The topology of the operad's spaces *is* the algebra of its algebras.

**Recognition is the reversal from necessary to sufficient.** A structure being present on an object is usually a property the object happens to have. The deepest theorems of the chapter — [[Thm - May's Recognition Principle|May's recognition principle]] foremost — reverse this: having a (group-like) $E_n$-action is *sufficient* to be an $n$-fold loop space, not merely necessary. This is the template for the operadic philosophy in modern mathematics: encode a homotopy-coherent algebraic structure by an operad, verify the structure (plus a group-completion condition), and read off a deep classification. The same reversal turns an $E_\infty$-structure into a spectrum, an $E_2$-structure on Hochschild cochains into Deligne's conjecture, and a symmetric monoidal structure into algebraic $K$-theory. The lesson for problem-solving is to ask, whenever you have verified an operadic structure, whether a recognition principle upgrades it from decoration to characterisation.
