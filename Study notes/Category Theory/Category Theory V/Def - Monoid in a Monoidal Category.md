---
type: definition
subject: category-theory
prereqs:
  - "Def - Monoidal Category"
  - "Def - Monad and Comonad"
  - "Def - Ring"
  - "Def - Functor"
tags: [category-theory, foundations]
---

# Notation

Throughout, $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ is a [[Def - Monoidal Category|monoidal category]]: tensor $\otimes$, unit object $I$, associator $\alpha$, unitors $\lambda, \rho$. A monoid object is written $(M, m, e)$ with **multiplication** $m : M \otimes M \to M$ and **unit** $e : I \to M$. By [[Thm - Mac Lane Coherence Theorem|coherence]] we suppress $\alpha, \lambda, \rho$ when convenient, treating $\otimes$ as strictly associative and unital. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

---

# Axiom Motivation

A monoid in the ordinary sense is a set $M$ with an associative binary operation $M \times M \to M$ and a unit element $1 \in M$. The element $1$ can be repackaged as a function $e : \{*\} \to M$ from the one-point set, $e(*) = 1$. Now both pieces of data are *functions*: a multiplication $m : M \times M \to M$ and a unit $e : 1 \to M$, where $1$ is the terminal/unit object of $(\mathbf{Set}, \times)$. Written this way, nothing about the definition refers to *elements* — it refers only to the Cartesian product, the one-point set, and two maps. The insight is that the definition makes sense in *any* [[Def - Monoidal Category|monoidal category]] once we replace $\times$ by $\otimes$ and $1$ by the unit object $I$. We get a monoid object $(M, m : M \otimes M \to M, e : I \to M)$, and the only question is which equations the axioms become.

The first axiom is **associativity**. For a set monoid, $(xy)z = x(yz)$. Element-free, this says the two ways of multiplying three factors agree: $m \circ (m \otimes 1_M) = m \circ (1_M \otimes m)$ as maps $M \otimes M \otimes M \to M$. The left side multiplies the first two factors then the result with the third; the right multiplies the last two then the first with the result. In a non-strict monoidal category the two triple-tensors $(M \otimes M) \otimes M$ and $M \otimes (M \otimes M)$ are only isomorphic via the associator $\alpha$, so the axiom must include it: $m \circ (m \otimes 1) = m \circ (1 \otimes m) \circ \alpha_{M,M,M}$. Drop associativity and "the product of three factors" is ambiguous — exactly the failure that associativity exists to forbid, now stated for objects.

The second axiom is **unitality**. For a set monoid, $1 \cdot x = x = x \cdot 1$. Element-free, this says that multiplying by the unit on either side is the identity: $m \circ (e \otimes 1_M) = \lambda_M$ and $m \circ (1_M \otimes e) = \rho_M$ as maps $I \otimes M \to M$ and $M \otimes I \to M$, where the unitors $\lambda, \rho$ identify $I \otimes M$ and $M \otimes I$ with $M$. The unitors appear because in a general monoidal category $I \otimes M$ is not literally $M$; it is isomorphic to it via $\lambda$. Drop unitality and $e$ is just some map $I \to M$ with no special relationship to $m$ — not a unit at all.

Why exactly these two? Because they are the element-free transcription of the *only* two monoid axioms. The remarkable payoff is that *changing the ambient monoidal category changes what a monoid is*, while the definition stays fixed:
- in $(\mathbf{Set}, \times)$ you recover ordinary monoids;
- in $(\mathbf{Ab}, \otimes)$ a multiplication $M \otimes M \to M$ is a *bilinear* map $M \times M \to M$, and an additive group with an associative unital bilinear multiplication is exactly a [[Def - Ring|ring]];
- in $(\mathbf{Vect}_k, \otimes)$ you get a unital associative $k$-algebra;
- in $([\mathcal{C},\mathcal{C}], \circ)$ a multiplication $T \circ T \Rightarrow T$ with a unit $1 \Rightarrow T$ is exactly the multiplication and unit of a [[Def - Monad and Comonad|monad]].

A reader could invent this: take the element-free form of "associative unital binary operation," replace product by tensor, and you have the definition. The genius is not the definition — it is realizing that one definition, by varying the ambient monoidal category, *is* the definition of monoid, ring, algebra, and monad simultaneously.

---

# The Definition

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ be a monoidal category. A **monoid (object)** in $\mathcal{C}$ is a triple $(M, m, e)$ where $M$ is an object, $m : M \otimes M \to M$ is the multiplication, and $e : I \to M$ is the unit, such that:

**Associativity** ($M \otimes M \otimes M \to M$):
$$m \circ (m \otimes 1_M) \;=\; m \circ (1_M \otimes m) \circ \alpha_{M,M,M}.$$

**Unitality** ($I \otimes M \to M$ and $M \otimes I \to M$):
$$m \circ (e \otimes 1_M) = \lambda_M, \qquad m \circ (1_M \otimes e) = \rho_M.$$

A **morphism of monoids** $(M, m, e) \to (M', m', e')$ is a morphism $f : M \to M'$ in $\mathcal{C}$ with $f \circ m = m' \circ (f \otimes f)$ and $f \circ e = e'$.

If $\mathcal{C}$ is **braided** with braiding $\beta$, a monoid is **commutative** if $m \circ \beta_{M,M} = m$. A **comonoid** is the formal dual: $(C, \Delta : C \to C \otimes C, \varepsilon : C \to I)$ with coassociativity and counitality.

---

# Categorical / Structural Definition

The definition *is* the structural one; the content is the table of specializations. Fixing the ambient monoidal category $\mathcal{V}$ and reading off "monoid in $\mathcal{V}$" yields:

$$\begin{array}{l|l}
\text{Monoidal category } \mathcal{V} & \text{Monoid in } \mathcal{V} \\ \hline
(\mathbf{Set}, \times, 1) & \text{ordinary monoid} \\
(\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z}) & \text{ring} \\
(\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z}) \text{ commutative monoid} & \text{commutative ring} \\
(\mathbf{Vect}_k, \otimes_k, k) & k\text{-algebra} \\
(\mathbf{Mod}_R, \otimes_R, R) & R\text{-algebra} \\
([\mathcal{C},\mathcal{C}], \circ, 1_{\mathcal{C}}) & \text{monad on } \mathcal{C} \\
(\mathbf{Cat}, \times, \mathbf{1}) & \text{strict monoidal category} \\
(\mathbf{Top}, \times, \ast) & \text{topological monoid}
\end{array}$$

The entry that closes this chapter is the sixth: a monoid in the [[Def - Functor Category|endofunctor category]] $([\mathcal{C},\mathcal{C}], \circ, 1_{\mathcal{C}})$ is precisely a [[Def - Monad and Comonad|monad]]. The multiplication $m : M \otimes M \to M$ is, with $\otimes = \circ$ and $M = T$, a natural transformation $T \circ T \Rightarrow T$, i.e. $\mu$; the unit $e : I \to M$ is $1_{\mathcal{C}} \Rightarrow T$, i.e. $\eta$; the associativity and unitality axioms become the monad axioms verbatim (the associator and unitors are identities since the endofunctor category is *strict* monoidal). This is the rigorous content of Wadler's slogan "a monad is a monoid in the category of endofunctors."

---

# Relate to Other Fields / Compression

This single definition is the most economical statement of what "an algebraic structure with one associative operation and a unit" means. It is why the theory of [[Def - Ring|rings]], the theory of $k$-algebras, and the theory of [[Def - Monad and Comonad|monads]] are structurally identical: each is the theory of monoids, run in a different ambient category. Modules over a ring, bimodules, the tensor product of algebras, and the universal enveloping algebra all have one-line definitions in terms of monoid objects and their modules.

**True name:** a monoid object is an **associative unital multiplication in a tensor world** — the element-free shadow of "set with an associative product and a unit," with the unit element repackaged as a map $I \to M$ out of the unit object. When you see "multiplication $M \otimes M \to M$ with a unit $I \to M$," recognize a monoid regardless of which category you are in, and import everything you know about monoids.

The deepest compression is the meta-statement that *categorification turns the slot "set" into a parameter*. The monoid axioms were always about a binary operation; by abstracting "set with product" to "object in a monoidal category," the same axioms generate an entire zoo of structures. A monad is the most surprising inhabitant of the zoo, because its "elements" are natural transformations and its "multiplication" is functor composition.

---

# Examples / Corollaries

**Is an instance — a ring as a monoid in $(\mathbf{Ab}, \otimes)$.** Let $R$ be an [[Def - Abelian Group|abelian group]]. A multiplication $m : R \otimes_{\mathbb{Z}} R \to R$ is exactly a $\mathbb{Z}$-bilinear map $R \times R \to R$ (by the universal property of $\otimes$), and a unit $e : \mathbb{Z} \to R$ is determined by $e(1) =: 1_R$. Associativity and unitality of the monoid object become exactly the ring axioms. So a monoid in $(\mathbf{Ab}, \otimes)$ is a [[Def - Ring|ring]], and a commutative monoid is a commutative ring (full unwinding in [[Ex - Monoids in Vect are algebras and in Ab are rings]]).

**Is an instance — a $k$-algebra as a monoid in $(\mathbf{Vect}_k, \otimes)$.** Same computation over a field: a bilinear associative unital multiplication on a [[Def - Vector Space|vector space]] over $k$ is a unital associative $k$-algebra. Matrix algebras $M_n(k)$, polynomial algebras $k[x]$, and group algebras $k[G]$ are all monoids here.

**Is an instance — a monad as a monoid in $([\mathcal{C},\mathcal{C}], \circ)$.** As in the structural section: $(T, \mu, \eta)$ is a monoid object with $\otimes = \circ$, recovering [[Def - Monad and Comonad|the monad]] definition exactly. This is the loop-closing example of the chapter.

**Is an instance — an ordinary monoid as a monoid in $(\mathbf{Set}, \times)$.** The base case: $M$ a set, $m : M \times M \to M$ the operation, $e : 1 \to M$ picking the identity. A *commutative* monoid in $(\mathbf{Set}, \times)$ (using the swap braiding) is an abelian monoid.

**Is NOT an instance — a non-unital "rng".** An abelian group with an associative bilinear multiplication but *no* unit (a rng, e.g. the even integers $2\mathbb{Z}$ with ordinary multiplication) is **not** a monoid object: it lacks the map $e : \mathbb{Z} \to M$ satisfying unitality. The example isolates the role of the unit axiom — dropping it gives the strictly weaker notion of a semigroup object.

**Is NOT an instance — a Lie algebra in $(\mathbf{Vect}_k, \otimes)$.** A [[Def - Vector Space|vector space]] with the Lie bracket $[\,\cdot\,,\cdot\,] : \mathfrak{g} \otimes \mathfrak{g} \to \mathfrak{g}$ is *not* a monoid object: the bracket is antisymmetric and satisfies the Jacobi identity, not associativity, and there is no unit. Lie algebras are algebras for a different operad, not monoids — showing that "bilinear operation" alone does not make a monoid.

**Calibration check.** Verify that a multiplication $R \otimes_{\mathbb{Z}} R \to R$ is the same data as a bilinear map (universal property of $\otimes$); check that the monoid unit $e : \mathbb{Z} \to R$ is equivalent to choosing $1_R \in R$; and confirm that the monoid axioms in $([\mathcal{C},\mathcal{C}], \circ)$ are *identical* to the monad axioms, not merely analogous.

---

# Unlocked by This

> [!tip] Modules, Bimodules, and the Tensor Product of Algebras *(from Algebra)*
> Once a [[Def - Ring|ring]] or $k$-algebra is a monoid object, its modules are *module objects* over that monoid, bimodules are objects with commuting left and right actions, and the tensor product of algebras is the coproduct of commutative monoids in $(\mathbf{Ab}, \otimes)$.

> [!tip] Hopf Algebras and Quantum Groups *(from Representation Theory)*
> An object that is simultaneously a monoid and a comonoid, with compatible structure, is a bialgebra; adding an antipode gives a **Hopf algebra**. In braided monoidal categories these are the quantum groups, whose braidings solve the Yang–Baxter equation.

> [!tip] Operads and E_n-Algebras *(from Higher Algebra)*
> Monoids are algebras over the associative **operad**; commutative monoids are algebras over the commutative operad; the intermediate $E_n$-operads (governed by braided and symmetric structure) interpolate between them, organizing the hierarchy of associative, braided, and commutative multiplications up to homotopy.
