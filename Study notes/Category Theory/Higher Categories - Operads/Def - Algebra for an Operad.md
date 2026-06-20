---
type: definition
subject: higher-categories
prereqs:
  - "Def - Operad"
  - "Def - Endomorphism Operad"
  - "Def - Monad and Comonad"
  - "Def - Monoid in a Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Let $P$ be an [[Def - Operad|operad]] in a closed [[Def - Monoidal Category|symmetric monoidal category]] $(\mathcal{V}, \otimes, \mathbb{1})$, with operations $P(n)$, unit $\mathrm{id} \in P(1)$, symmetric action, and composition $\gamma$. An **algebra over $P$** (or **$P$-algebra**) is an object $X \in \mathcal{V}$ carrying an action of $P$. The action is presented in either of two equivalent ways: as **structure maps**
$$\rho_n : P(n) \otimes X^{\otimes n} \longrightarrow X \qquad (n \geq 0),$$
each $S_n$-invariant (where $S_n$ acts diagonally on $P(n) \otimes X^{\otimes n}$), or as an **operad morphism** $\rho : P \to \mathrm{End}_X$ into the [[Def - Endomorphism Operad|endomorphism operad]]. In $\mathbf{Set}$ the first form is a map $P(n) \times X^n \to X$, $(\theta, x_1, \dots, x_n) \mapsto \theta(x_1, \dots, x_n)$, "evaluate the abstract operation $\theta$ on the elements $x_i$". The full notation registry is on [[Higher Categories — Operads and Multicategories]].

---

# Axiom Motivation

An [[Def - Operad|operad]] is a pile of abstract operations; it does nothing until it acts. The whole reason operads exist is to *be made concrete* on an object, and a $P$-algebra is exactly that: an object on which each abstract $n$-ary operation $\theta \in P(n)$ becomes a real $n$-ary operation. The definition is forced by a single demand — that the action *respect the operad structure* — and once you spell out what that means you have invented the notion of algebra.

Start from the only sensible idea of action. Each $\theta \in P(n)$ should determine a genuine operation $X^{\otimes n} \to X$. Bundling these over all $\theta$ of a fixed arity gives a single map $\rho_n : P(n) \otimes X^{\otimes n} \to X$ (in $\mathbf{Set}$: $(\theta, x_1, \dots, x_n) \mapsto \theta(x_1, \dots, x_n)$). Now ask which coherence conditions $\rho$ must satisfy for this to deserve the word "action".

The first condition is **compatibility with composition** (associativity of the action). The operad lets you compose operations: $\gamma(\theta; \varphi_1, \dots, \varphi_k)$ is the operation obtained by plugging the $\varphi_i$ into $\theta$. Acting with this composite must agree with first acting with the $\varphi_i$ and then acting with $\theta$ on the results. Symbolically, $\rho$ applied to $\gamma(\theta; \varphi_1, \dots, \varphi_k)$ equals $\rho(\theta)$ applied to $\rho(\varphi_1), \dots, \rho(\varphi_k)$. Drop this and the abstract composition of operations bears no relation to the concrete composition of their actions — so "the operation built by this wiring diagram acts as the corresponding wiring of actions" fails, and the operad's whole organising principle is lost. This is the operad-action analogue of the [[Def - Algebra for a Monad|monad-algebra]] associativity square $\mu$ acting compatibly.

The second condition is the **unit law**: the unit operation $\mathrm{id} \in P(1)$ must act as the identity of $X$, $\rho(\mathrm{id}) = 1_X$. Without it, the "do-nothing" operation could scramble $X$, and there would be no anchor making $\rho$ a genuine action rather than an arbitrary family of maps. This is the analogue of the monad-algebra unit law $\rho \circ \eta = 1$.

The third condition is **equivariance**: $\rho_n$ must be $S_n$-invariant, so that relabelling the inputs of an abstract operation matches relabelling the elements you feed it: $\rho(\theta \cdot \sigma)(x_1, \dots, x_n) = \rho(\theta)(x_{\sigma(1)}, \dots, x_{\sigma(n)})$. Drop it and the symmetric structure of $P$ — the very thing distinguishing commutative from associative — would have no effect on the algebra, so a $\mathrm{Comm}$-algebra would not actually be commutative. Equivariance is what lets the operad's symmetry impose symmetry on the algebra.

The cleanest way to see that these three conditions are exactly right is the **endomorphism-operad reformulation**. The genuine $n$-ary operations on $X$ form the [[Def - Endomorphism Operad|endomorphism operad]] $\mathrm{End}_X$, with $\mathrm{End}_X(n) = \mathrm{Hom}(X^{\otimes n}, X)$. The three conditions above say precisely that $\rho : P \to \mathrm{End}_X$ is a **morphism of operads** — it preserves composition, unit, and symmetric action. So a $P$-algebra is a map of operads $P \to \mathrm{End}_X$, full stop. This is the slogan to memorise: *a $P$-algebra is an interpretation of the abstract operations of $P$ as actual operations on $X$.* A reader could invent it from "I want the abstract operations to act, respecting how they compose, the do-nothing one, and how they permute" — which is just "a map into the operad of all operations on $X$".

---

# The Definition

Let $P$ be an operad in a closed symmetric monoidal category $(\mathcal{V}, \otimes, \mathbb{1})$. A **$P$-algebra** is an object $X \in \mathcal{V}$ together with morphisms
$$\rho_n : P(n) \otimes X^{\otimes n} \longrightarrow X \qquad (n \geq 0)$$
satisfying:

**Associativity.** For all $k$ and $n_1, \dots, n_k$, the square comparing "compose in $P$ then act" with "act then act" commutes:
$$\rho\big(\gamma(\theta; \varphi_1, \dots, \varphi_k)\big) = \rho(\theta)\big(\rho(\varphi_1), \dots, \rho(\varphi_k)\big),$$
as morphisms $P(k) \otimes P(n_1) \otimes \dots \otimes P(n_k) \otimes X^{\otimes(n_1 + \dots + n_k)} \to X$.

**Unit.** $\rho_1(\mathrm{id} \otimes -) = 1_X : X \to X$.

**Equivariance.** Each $\rho_n$ is invariant under the diagonal $S_n$-action on $P(n) \otimes X^{\otimes n}$:
$$\rho_n(\theta \cdot \sigma, x_1, \dots, x_n) = \rho_n(\theta, x_{\sigma(1)}, \dots, x_{\sigma(n)}).$$

A **morphism of $P$-algebras** $f : (X, \rho) \to (Y, \rho')$ is a morphism $f : X \to Y$ in $\mathcal{V}$ commuting with the structure maps: $f \circ \rho_n = \rho'_n \circ (1_{P(n)} \otimes f^{\otimes n})$ for all $n$. The $P$-algebras and their morphisms form a category $\mathrm{Alg}_P$.

**Equivalent forms.**

- *Endomorphism form.* A $P$-algebra structure on $X$ is exactly a morphism of operads $\rho : P \to \mathrm{End}_X$ into the [[Def - Endomorphism Operad|endomorphism operad]].
- *Monad form.* Define the **operadic monad** (or **Schur functor**) $T_P$ on $\mathcal{V}$ by
$$T_P(X) = \coprod_{n \geq 0} P(n) \otimes_{S_n} X^{\otimes n},$$
where $\otimes_{S_n}$ means the coinvariants of the diagonal $S_n$-action. Then $T_P$ is a [[Def - Monad and Comonad|monad]] (unit from $\mathrm{id} \in P(1)$, multiplication from $\gamma$), and a $P$-algebra is exactly an [[Def - Algebra for a Monad|algebra for the monad]] $T_P$. The three forms — structure maps, operad morphism, monad algebra — describe the same objects.

---

# Categorical / Structural Definition

The structural content is the chain of identifications
$$\{P\text{-algebra structures on } X\} \;\cong\; \mathrm{Operad}(\mathcal{V})\big(P, \mathrm{End}_X\big) \;\cong\; \{T_P\text{-algebra structures on } X\},$$
and the resulting equivalence of categories $\mathrm{Alg}_P \simeq \mathcal{V}^{T_P}$ between $P$-algebras and Eilenberg–Moore algebras for the operadic monad. This is the precise sense in which **operads are a special, well-presented class of monads**: every operad gives a monad $T_P$ whose algebras it controls, and the monads so arising are the *analytic* (or *polynomial/Schur*) monads — those built as a sum of $n$-ary pieces $P(n) \otimes_{S_n} X^{\otimes n}$. The forgetful functor $\mathrm{Alg}_P \to \mathcal{V}$ has a left adjoint, the **free $P$-algebra** functor $X \mapsto T_P(X)$, and the monad of this adjunction is exactly $T_P$ — so the operad presents its category of algebras as a category of algebras over a monad, complete with free–forgetful adjunction.

A second structural reading places this in the [[Def - Monoid in a Monoidal Category|monoid]] picture. Since an operad is a monoid in symmetric sequences under the composition product $\circ$ (see [[Thm - Operads as Monoids in Symmetric Sequences]]), and an object $X$ defines a symmetric sequence concentrated suitably, a $P$-algebra is a **left module over the monoid $P$** in symmetric sequences — the operadic action $\rho$ is the module action. "Algebra over $P$" and "module over the monoid $P$" are the same notion read in two languages.

---

# Relate to Other Fields / Compression

The unifying frame is one sentence: **choosing an operad chooses a kind of algebra, and a $P$-algebra is a realisation of that kind on an object.** This makes operads a machine for *parametrising algebraic structures*. The associative operad's algebras are monoids; the commutative operad's are commutative monoids; the Lie operad's are Lie algebras; the little-disks operad's (up to homotopy) are iterated loop spaces. One definition of "algebra over an operad" subsumes monoid, ring, associative algebra, commutative algebra, Lie algebra, Poisson algebra, and their homotopy-coherent versions, distinguished only by which operad you plug in.

**True name:** a $P$-algebra is *an object on which the abstract operations of $P$ become genuine operations, coherently.* The official definition lists structure maps and three axioms; the name to carry is "an interpretation of $P$ in $X$", or equivalently "a morphism from $P$ to the operations of $X$". When you see a class of algebraic objects and want to study them all at once — their free objects, their (co)homology, their deformations, their homotopy theory — the move is: find the operad whose algebras they are, and transfer the question to the operad, where it becomes uniform across all algebras of that type. This is the operadic analogue of *to study all $G$-sets at once, study $G$*.

---

# Examples / Corollaries

**Is an instance — monoids as $\mathrm{Assoc}$-algebras.** A $\mathrm{Assoc}$-algebra in $\mathbf{Set}$ is exactly a [[Def - Monoid in a Monoidal Category|monoid]]. The operad $\mathrm{Assoc}(n) = S_n$ has, in arity $2$, two operations $xy$ and $yx$; an algebra structure interprets the generating product, and the operad relations force associativity and unitality. In $\mathbf{Vect}_k$ the same operad gives associative unital $k$-algebras. So "monoid" and "$\mathrm{Assoc}$-algebra" are interchangeable descriptions, the second being the one that generalises to homotopy ($A_\infty$-algebras).

**Is an instance — commutative monoids as $\mathrm{Comm}$-algebras.** A $\mathrm{Comm}$-algebra is a commutative monoid (in $\mathbf{Vect}_k$: a commutative associative algebra). Because $\mathrm{Comm}(n) = \{*\}$ with trivial $S_n$-action, the single $n$-ary operation must be invariant under all input permutations — and equivariance of the action turns that invariance into commutativity of the product. This is the textbook case where the $S_n$-structure of the operad *is* the commutativity of the algebra.

**Is an instance — Lie algebras as $\mathrm{Lie}$-algebras.** A $\mathrm{Lie}$-algebra in $\mathbf{Vect}_k$ is a Lie algebra: the action interprets the generating bracket $[-,-] \in \mathrm{Lie}(2)$ as a bilinear map, and the arity-$3$ relations in the operad (antisymmetry and Jacobi) become exactly antisymmetry and the Jacobi identity on the algebra. The Jacobi identity is *not* an extra hypothesis you impose — it is forced by respecting the operad's relations, which is the whole advantage of the operadic viewpoint.

**Is an instance — $n$-fold loop spaces as $E_n$-algebras.** An algebra over the little $n$-disks operad $E_n$ in $\mathbf{Top}$ is, up to homotopy, an $n$-fold loop space — this is [[Thm - May's Recognition Principle|May's recognition principle]]. The structure maps $E_n(k) \times X^k \to X$ say "given $k$ disjoint little $n$-disks and $k$ points of $X$, produce a point of $X$" — exactly the data of multiplying loops with the homotopical slack the configuration spaces encode. This example is why topological operads were invented.

**Is NOT an instance — a set with a binary operation that is associative but where you forget unitality.** A semigroup (associative, no identity) is *not* a $\mathrm{Assoc}$-algebra, because $\mathrm{Assoc}$ has a nullary unit operation $\in \mathrm{Assoc}(0)$ that any algebra must interpret as an identity element; without an identity the unit axiom of the action fails at arity $0$. The fix is the *non-unital* associative operad (no arity-$0$ operation), whose algebras are exactly semigroups — a reminder that the arity-$0$ part of the operad controls units in the algebra.

**Is NOT an instance — a vector space with a bilinear bracket satisfying antisymmetry but not Jacobi.** Such a "pre-Lie magma" is not a $\mathrm{Lie}$-algebra: the action would have to respect the Jacobi relation living in $\mathrm{Lie}(3)$, and it does not. The object is an algebra over a *different*, larger operad (the free operad on an antisymmetric binary operation, with no Jacobi quotient). This shows that the algebra type is exactly as fine as the operad's relations.

**Calibration check.** Verify that (i) an algebra over the trivial operad $P(1) = \{\mathrm{id}\}$, $P(n) = \emptyset$ for $n \neq 1$, is just a plain object (no structure); (ii) a $\mathrm{Comm}$-algebra structure on a set $X$ is determined by its binary operation, since every higher operation is a composite of the binary one — and that operation is forced commutative and associative; and (iii) a morphism of $\mathrm{Assoc}$-algebras is exactly a monoid homomorphism. If you can confirm these, "algebra over an operad" is solid.

---

# Unlocked by This

> [!tip] Free Algebras and the Free Operad *(from this topic)*
> The operadic monad $T_P(X) = \coprod_n P(n) \otimes_{S_n} X^{\otimes n}$ builds the **free $P$-algebra** on any object $X$. When $P$ is itself the [[Thm - The Free Operad|free operad]] on a sequence of generating operations, $T_P(X)$ is the algebra of formal expressions in those operations — the syntactic raw material before relations are imposed.

> [!tip] Homotopy Algebras: A∞ and E∞ *(from Operadic Homotopy Theory)*
> Replacing $P$ by a cofibrant resolution gives **homotopy algebras**: an $A_\infty$-algebra is an algebra over a resolution of $\mathrm{Assoc}$ (associativity up to coherent homotopy), an $E_\infty$-algebra over a resolution of $\mathrm{Comm}$. These are the structures that are invariant under weak equivalence, and the reason operads dominate modern homotopy theory.

> [!tip] Factorization Homology and TQFT *(from Operadic Homotopy Theory)*
> $E_n$-algebras are the local input data for **factorization homology**, which integrates an $E_n$-algebra over an $n$-manifold; the manifold-with-corners gluing realises the algebra's operations geometrically. This is one bridge from operads to **topological quantum field theory**, where the operations of an algebra become the values of a field theory on discs.
