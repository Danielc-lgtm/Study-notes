---
type: definition
subject: higher-categories
prereqs:
  - "Def - Multicategory"
  - "Def - Monoidal Category"
  - "Def - Monad and Comonad"
tags: [category-theory, higher-categories, foundations]
---

# Notation

An **operad** $P$ (in $\mathbf{Set}$) is a sequence of sets $P(0), P(1), P(2), \dots$, where $P(n)$ is the set of **$n$-ary operations** — abstract operations that take $n$ inputs and produce one output. We picture an element $\theta \in P(n)$ as a node with $n$ input wires (numbered $1, \dots, n$) and one output wire. There is a distinguished **unit** $\mathrm{id} \in P(1)$, the do-nothing operation. The symmetric group $S_n$ acts on $P(n)$ on the right, written $\theta \cdot \sigma$ or $\sigma^* \theta$, relabelling the inputs. The **operadic composition** (or substitution) takes an operation $\theta \in P(k)$ and operations $\varphi_1 \in P(n_1), \dots, \varphi_k \in P(n_k)$, plugs $\varphi_i$ into the $i$th input of $\theta$, and returns an operation of arity $n_1 + \dots + n_k$:
$$\gamma : P(k) \times P(n_1) \times \dots \times P(n_k) \longrightarrow P(n_1 + \dots + n_k), \qquad (\theta; \varphi_1, \dots, \varphi_k) \mapsto \theta \circ (\varphi_1, \dots, \varphi_k).$$
There is also a slimmer **partial composition** $\circ_i$ inserting a single operation into the $i$th slot, $\circ_i : P(k) \times P(n) \to P(k + n - 1)$. The two formulations are equivalent. Throughout, $\mathbb{1}$ denotes the unit object of whatever monoidal category we work in. The full notation registry is on [[Higher Categories — Operads and Multicategories]].

A **non-symmetric (plain) operad** is the same data with the $S_n$-action deleted; a **symmetric operad** keeps it. We say "operad" for the symmetric flavour unless noted.

---

# Axiom Motivation

An operad is the answer to a question you have probably asked without naming it: *what is the abstract pattern of a single algebraic structure, stripped of any particular set it acts on?* A monoid is a set with an associative unital binary product. A commutative monoid adds commutativity. An associative algebra is a vector space with such a product; a Lie algebra has a bracket satisfying antisymmetry and Jacobi. Each of these is a *type of structure*, and each type is specified by a list of operations of various arities together with the equations they satisfy. An operad is precisely that list of operations and equations, packaged so that it can act on any object whatsoever. The structure is divorced from the carrier; $P(n)$ is "all the $n$-ary operations the structure provides", before you ever choose a set for them to operate on.

The cleanest way to see why this forces the definition is to start from the one example that has to work: the **endomorphism operad**. Fix a set (or vector space) $X$ and let $\mathrm{End}_X(n) = \mathrm{Hom}(X^n, X)$ be the genuine $n$-ary operations on $X$ — the $n$-input functions. This collection obviously has a unit (the identity $X \to X$ in arity $1$), an $S_n$-action (permute the arguments of a function), and a composition (substitute functions into the slots of a function), and these satisfy associativity and unit laws because they do so for honest functions. An operad is the abstraction of exactly this structure: it is "a thing that maps to some $\mathrm{End}_X$", a recipe for operations that an actual object can then realise. This immediately tells you what an algebra over $P$ must be — a map $P \to \mathrm{End}_X$ — and it tells you which axioms $P$ needs, namely whatever $\mathrm{End}_X$ satisfies, since $P$ must be able to land inside it.

The first axiom is **associativity of composition**. There are two ways to compose three layers of operations — substitute the bottom layer into the middle and then into the top, or assemble the top two first — and they must agree. Drop it and the substitution of a tree of operations has no well-defined value, so "the operation built by this wiring diagram" is ambiguous. In $\mathrm{End}_X$ this is automatic: nesting functions is associative because function application is. The operad axiom demands the abstraction inherit this.

The second axiom is **unitality**: the unit $\mathrm{id} \in P(1)$ must satisfy $\theta \circ (\mathrm{id}, \dots, \mathrm{id}) = \theta$ and $\mathrm{id} \circ \theta = \theta$. Without it, $\mathrm{id}$ is just some unary operation, and there is no operation that "passes its input through unchanged" — but every realisation $\mathrm{End}_X$ has the genuine identity function, so the abstraction must have a unit mapping to it.

The third piece is **equivariance**: the $S_n$-action must interact correctly with composition, so that permuting the inputs of a composite agrees with permuting at the levels and reshuffling the blocks. The reason this is non-negotiable is the same as in $\mathrm{End}_X$: if $f(x_1, x_2, x_3)$ is a function and you substitute $g(y_1, y_2)$ into the first slot, then swapping the two arguments of $g$ versus swapping the corresponding two inputs of the composite must give the same function. Equivariance is the statement that the abstract operations relabel their inputs the way real functions do. Strip equivariance and you have a *non-symmetric* operad — which is exactly right when the inputs are genuinely ordered (think: a binary tree where left and right children are different), and exactly wrong when they are interchangeable.

There is one more thing the motivation should make inevitable: **why "one object"?** A multicategory has many colours; an operad has one. The operad is the special case where all inputs and the output have the same type — the right setting for a *single* algebraic structure on a *single* underlying object. The moment you want structures relating several types (an algebra together with a module over it), you need colours back, and you are doing multicategory theory. So an operad is precisely a one-object [[Def - Multicategory|multicategory]]: the entire definition above is the multicategory axioms with the colours collapsed to a point.

---

# The Definition

A **(symmetric) operad** $P$ in $\mathbf{Set}$ consists of:

1. a sequence of sets $P(n)$ for $n \geq 0$;
2. a **unit** $\mathrm{id} \in P(1)$;
3. a right action of the symmetric group $S_n$ on $P(n)$ for each $n$;
4. **composition** maps, for all $k \geq 0$ and $n_1, \dots, n_k \geq 0$,
$$\gamma : P(k) \times P(n_1) \times \dots \times P(n_k) \longrightarrow P(n_1 + \dots + n_k);$$

satisfying:

**Associativity.** For $\theta \in P(k)$, $\varphi_i \in P(n_i)$, and $\psi_{i,j} \in P(m_{i,j})$,
$$\gamma\big(\gamma(\theta; \varphi_1, \dots, \varphi_k);\ \psi_{1,1}, \dots, \psi_{k, n_k}\big) = \gamma\big(\theta;\ \gamma(\varphi_1; \psi_{1,1}, \dots), \dots, \gamma(\varphi_k; \dots, \psi_{k, n_k})\big).$$

**Unit.** $\gamma(\mathrm{id}; \theta) = \theta$ and $\gamma(\theta; \mathrm{id}, \dots, \mathrm{id}) = \theta$ for all $\theta \in P(n)$.

**Equivariance.** For $\sigma \in S_k$ and $\tau_i \in S_{n_i}$,
$$\gamma(\theta \cdot \sigma; \varphi_1, \dots, \varphi_k) = \gamma(\theta; \varphi_{\sigma^{-1}(1)}, \dots, \varphi_{\sigma^{-1}(k)}) \cdot \sigma\langle n_1, \dots, n_k\rangle,$$
$$\gamma(\theta; \varphi_1 \cdot \tau_1, \dots, \varphi_k \cdot \tau_k) = \gamma(\theta; \varphi_1, \dots, \varphi_k) \cdot (\tau_1 \oplus \dots \oplus \tau_k),$$
where $\sigma\langle n_1, \dots, n_k\rangle \in S_{n_1 + \dots + n_k}$ is the **block permutation** that moves the $k$ blocks according to $\sigma$, and $\tau_1 \oplus \dots \oplus \tau_k$ is the block-diagonal permutation acting within the blocks.

Equivalently, $P$ may be given by **partial compositions** $\circ_i : P(k) \times P(n) \to P(k+n-1)$ (insert into the $i$th slot only), satisfying parallel and sequential associativity laws, unit laws, and equivariance. A **non-symmetric operad** drops item (3) and the equivariance axiom.

A **morphism of operads** $f : P \to Q$ is a family $f_n : P(n) \to Q(n)$ preserving the unit, the composition $\gamma$, and the symmetric actions.

The definition transports verbatim to any **symmetric monoidal category** $(\mathcal{V}, \otimes, \mathbb{1})$: an operad in $\mathcal{V}$ is a sequence of objects $P(n) \in \mathcal{V}$ with an $S_n$-action, a unit $\mathbb{1} \to P(1)$, and composition morphisms $P(k) \otimes P(n_1) \otimes \dots \otimes P(n_k) \to P(\sum n_i)$ in $\mathcal{V}$. Operads in $\mathbf{Top}$ (topological operads), in $\mathbf{Vect}_k$ or chain complexes (algebraic operads), and in $\mathbf{Set}$ are the cases that matter most.

---

# Categorical / Structural Definition

**An operad is a one-object [[Def - Multicategory|multicategory]].** Given an operad $P$, build a multicategory with a single object $\star$ by setting $\mathcal{M}(\star, \dots, \star; \star) = P(n)$ for the $n$-fold tuple; substitution and the symmetric action transfer directly, and the multicategory axioms become exactly the operad axioms. Conversely the endomorphism multimaps at any single colour of a multicategory form an operad. This is the cleanest possible compression of the definition: everything you know about multicategories specialises, and the one-colour assumption is what makes an operad govern a single algebraic structure.

**An operad is a monoid in symmetric sequences.** This is the deeper structural statement, and it is the subject of a full theorem. A **symmetric sequence** (or **$S$-module**) is a sequence of $S_n$-sets $P(n)$ — that is, a functor from the groupoid of finite sets and bijections to $\mathbf{Set}$. The collection of symmetric sequences carries a (non-symmetric) monoidal product, the **composition product** $\circ$, defined by
$$(P \circ Q)(n) = \coprod_{k \geq 0} P(k) \times_{S_k} \Big( \coprod_{n_1 + \dots + n_k = n} \mathrm{Ind}_{S_{n_1} \times \dots \times S_{n_k}}^{S_n}\, Q(n_1) \times \dots \times Q(n_k) \Big),$$
whose unit $I$ is the symmetric sequence concentrated in arity $1$. An operad is exactly a **monoid in $(\text{symmetric sequences}, \circ, I)$**: the multiplication $\mu : P \circ P \to P$ is the operadic composition $\gamma$, and the unit $\eta : I \to P$ is $\mathrm{id} \in P(1)$. See [[Thm - Operads as Monoids in Symmetric Sequences]]. This places operads in the same conceptual slot as monoids, rings, and monads — each is "a monoid in the appropriate monoidal category" (see [[Def - Monoid in a Monoidal Category|monoid in a monoidal category]]).

---

# Relate to Other Fields / Compression

The slogan that organises everything is: **an operad is a presentation-free description of a type of algebraic structure, and its algebras are the structures of that type.** The associative operad presents monoids; the commutative operad presents commutative monoids; the Lie operad presents Lie algebras. Choosing an operad is choosing a kind of algebra; an algebra is a realisation of the operad inside some object.

There is a tight three-way analogy worth carrying. An operad is to its algebras as a [[Def - Monad and Comonad|monad]] is to its algebras as a group is to its actions. Each is a gadget whose whole purpose is to *act*; the operad records "operations of every arity with substitution", the monad records "an endofunctor with multiplication", the group records "invertible symmetries with composition". In fact every operad $P$ gives rise to a monad $T_P$ on $\mathbf{Set}$ (or $\mathbf{Vect}_k$), $T_P(X) = \coprod_n P(n) \times_{S_n} X^n$, whose [[Def - Algebra for a Monad|monad-algebras]] coincide with the $P$-algebras. So operads are a class of especially well-behaved monads — the "polynomial" or "analytic" ones — and operad theory is a refinement of monad theory in which the monad is built from a graded pile of operations rather than handed over as an opaque endofunctor.

**True name:** an operad is *the symmetries-and-composition data of a single algebraic structure*. The official definition is a sequence of $S_n$-sets with $\gamma$, $\mathrm{id}$, and equivariance; the name to keep is "the abstract operations of one type of algebra". When you meet a class of algebraic objects defined by operations and equations among them — and crucially when those operations have *no relations forcing them to be generated by a binary one* — reach for an operad. The payoff phrase: *to specify a kind of algebra is to specify an operad; to give such an algebra is to give a map from that operad to an endomorphism operad.*

---

# Examples / Corollaries

**Is an instance — the associative operad $\mathrm{Assoc}$.** Set $\mathrm{Assoc}(n) = S_n$, the symmetric group itself, with $S_n$ acting by right multiplication; composition is the evident shuffling of orderings. An element of $\mathrm{Assoc}(n)$ is an *ordering* of $n$ inputs, and the operad encodes "multiply $n$ things in a specified order". Its algebras are exactly [[Def - Monoid in a Monoidal Category|monoids]] (associative unital), because a $\mathrm{Assoc}$-algebra structure on $X$ is a choice of associative product. The non-symmetric version has $\mathrm{Assoc}(n) = \{*\}$ a single point in each arity: one operation per arity, "the product of $n$ things in their given order".

**Is an instance — the commutative operad $\mathrm{Comm}$.** Set $\mathrm{Comm}(n) = \{*\}$, a single point in every arity, with trivial $S_n$-action; there is exactly one $n$-ary operation, and permuting its inputs does nothing — which is precisely commutativity. Its algebras are [[Def - Monoid in a Monoidal Category|commutative monoids]] (or, in $\mathbf{Vect}_k$, commutative associative algebras). The contrast with $\mathrm{Assoc}$ is the cleanest illustration of how the $S_n$-action carries the algebra's symmetry: same arity-wise size in the *non-symmetric* world, but $\mathrm{Assoc}(n) = S_n$ remembers order while $\mathrm{Comm}(n) = *$ forgets it.

**Is an instance — the Lie operad $\mathrm{Lie}$.** In $\mathbf{Vect}_k$, $\mathrm{Lie}(n)$ is the multilinear part of the free Lie algebra on $n$ generators; $\dim_k \mathrm{Lie}(n) = (n-1)!$, with a basis of bracketings such as $[x_1, [x_2, x_3]]$ modulo antisymmetry and Jacobi. Its algebras are Lie algebras. This is the example where the operad genuinely earns its keep: the Lie operad is *not* generated freely by its binary operation — Jacobi is a relation in arity three — so "Lie algebra" is not capturable by a monoidal product alone, but it is exactly a $\mathrm{Lie}$-algebra.

**Is an instance — the little $n$-disks operad $E_n$ (topological).** $E_n(k)$ is the space of $k$ disjoint round little $n$-disks embedded in the unit $n$-disk; composition inserts a configuration into each little disk. As $n$ grows the configurations have more room, so $E_1 \subset E_2 \subset \dots$ interpolate from "ordered, no commutativity" ($E_1 \simeq \mathrm{Assoc}$) to "fully commutative up to homotopy" ($E_\infty \simeq \mathrm{Comm}$). Its algebras (up to homotopy) are $n$-fold loop spaces — this is [[Thm - May's Recognition Principle|May's recognition principle]] — and the spaces $E_n(2) \simeq S^{n-1}$ explain why the homology of an $E_n$-algebra carries a degree-$(n-1)$ bracket.

**Is NOT an instance — the sequence $P(n) = \{*\}$ with $\gamma$ that forgets the unit.** Take one operation in each arity but define composition so that $\gamma(\theta; \mathrm{id}, \dots, \mathrm{id}) \neq \theta$ — for instance by always outputting the arity-$0$ operation. The unit axiom fails: $\mathrm{id} \in P(1)$ no longer passes inputs through. This is the reminder that a sequence of sets with *some* composition is not an operad; the unit and associativity laws are exactly what make the composition behave like substitution.

**Is NOT an instance — a graded vector space with a single binary product and no higher coherence.** A vector space $V$ with one bilinear map $V \otimes V \to V$ and nothing else is a (possibly non-associative) magma, not an algebra over any operad until you specify which relations the product satisfies and assemble the resulting operations into a sequence closed under composition. The data "$V$ plus a product" underspecifies an operad; you must say which operad, i.e. which equations.

**Calibration check.** Verify that (i) for any object $X$ of a symmetric monoidal category the sequence $\mathrm{End}_X(n) = \mathrm{Hom}(X^{\otimes n}, X)$ is an operad — this is the [[Def - Endomorphism Operad|endomorphism operad]]; (ii) the non-symmetric associative operad $\mathrm{Assoc}^{\mathrm{ns}}(n) = \{*\}$ and the commutative operad $\mathrm{Comm}(n) = \{*\}$ are *literally the same sequence of sets*, distinguished only by being read in the non-symmetric versus symmetric world; and (iii) $\mathrm{Assoc}(2) = S_2$ has two elements, corresponding to the products $xy$ and $yx$. If you can do these, the definition has landed.

---

# Unlocked by This

> [!tip] Algebra for an Operad *(from this topic)*
> The whole point of an operad is to act. An [[Def - Algebra for an Operad|algebra for an operad]] $P$ is an object $X$ together with an operad morphism $P \to \mathrm{End}_X$, equivalently structure maps $P(n) \otimes X^{\otimes n} \to X$. Choosing $P$ chooses the kind of algebra; this is the payoff definition.

> [!tip] A∞ and E∞ Operads *(from Operadic Homotopy Theory)*
> Replacing strict equations by coherent homotopies gives the **A∞-operad** (associativity up to a contractible space of higher homotopies, governing loop spaces and the chains on $E_1$) and the **E∞-operad** (commutativity up to all higher homotopies). An **E∞-ring** is an E∞-algebra in spectra, the homotopical replacement for a commutative ring and the basic object of modern stable homotopy theory.

> [!tip] Koszul Duality *(from Operadic Homotopy Theory)*
> Many operads come in dual pairs: **Koszul duality** sends $\mathrm{Comm}$ to $\mathrm{Lie}$ and $\mathrm{Assoc}$ to itself, packaging the relationship between an algebra type and its deformation/cohomology theory. It is the operadic shadow of the bar-cobar adjunction and underlies deformation quantisation.
