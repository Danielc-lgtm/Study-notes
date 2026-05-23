---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Group"
tags: [geometry, differential-geometry, lie-groups, algebra]
---

# Notation

A Lie group is written $(G, m, i, e)$ or simply $G$: the smooth manifold $G$, the multiplication map $m : G \times G \to G$, the inversion map $i : G \to G$, and the identity element $e \in G$. The notation $L_g : G \to G$ denotes left translation $L_g(h) = gh$, and $R_g : G \to G$ denotes right translation $R_g(h) = hg$. Both are diffeomorphisms of $G$, because they have smooth inverses $L_{g^{-1}}$ and $R_{g^{-1}}$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Axiom Motivation

The thing we are trying to axiomatize is **simultaneous structure**: a set that is at once a smooth manifold and a group, with the two structures compatible. The motivating examples are abundant and have been computed in earlier chapters without naming them: $\mathrm{GL}(n, \mathbb{R})$ is the open subset of $M(n, \mathbb{R})$ consisting of invertible matrices, with matrix multiplication and inversion; the circle $S^1 \subseteq \mathbb{C}$ has multiplication of unit complex numbers and complex inversion; the additive group $(\mathbb{R}^n, +)$ has translation as multiplication and negation as inversion. In every case, the multiplication and inversion are perfectly ordinary smooth maps between Euclidean spaces or smooth manifolds. The Lie group axioms are the demand that this is **always** the case — that the two structures cohere — and they are designed to make this demand as parsimonious as possible.

The most natural way to think of a group is as a set $G$ with three structure maps: multiplication $m : G \times G \to G$, inversion $i : G \to G$, and the constant map picking out the identity, $\eta : \{*\} \to G$, sending $* \mapsto e$. The group axioms — associativity, identity, inverse — become commutative diagrams involving $m, i, \eta$ and the product $G \times G$. **A Lie group is a group in which $G$ is a smooth manifold and all three structure maps are smooth.** The identity map $\eta$ is automatically smooth (it is a constant map to a point of $G$, and constant maps are smooth), so the demand reduces to: $m$ and $i$ are smooth. The further demand that "$G$ is a group" requires the algebraic axioms (associativity, identity, inverses) to hold as identities of smooth maps — but these are properties of the maps, not additional smoothness assumptions. Hence the minimal data is exactly what we wrote down: smooth manifold + smooth multiplication + smooth inversion.

Why both **smoothness of multiplication** and **smoothness of inversion**? It is tempting to ask whether one might follow from the other. The answer is "almost" — in fact, **for connected topological groups whose underlying space is a topological manifold, smoothness of multiplication forces smoothness of inversion via the inverse function theorem**, because the differential of $m(g, \cdot) : G \to G$ at the identity is right-translation by $g$, which is invertible. But the cleanest axiomatization demands both, because (i) it makes the definition manifestly equivalent to "$G$ is a group object in $\mathbf{Man}$" without requiring an auxiliary theorem, and (ii) it makes the verification of "$G$ is a Lie group" symmetric in multiplication and inversion, which is closer to the user's intuition. The redundancy is not a bug; it is a convenience.

What breaks if we **drop smoothness of multiplication**? Then $G$ is only a topological group living on a smooth manifold, with no relationship between the algebra and the calculus. The tangent space $T_e G$ exists as a vector space but acquires no Lie algebra structure from the (non-smooth) group operation, and the central machinery of the chapter — left-invariant vector fields, the exponential map, the adjoint representation — has nothing to feed on. A concrete example: take $\mathbb{R}$ with its usual smooth manifold structure but a group operation $a \star b = (a^3 + b^3)^{1/3}$ defined via inverse-cubing; this is a continuous group (in fact homeomorphic to $\mathbb{R}$ as a topological group) but the multiplication is not smooth at $0$, and the resulting "topological group on a smooth manifold" has no Lie algebra. The smoothness of $m$ is what makes the calculus on $G$ talk to the group structure.

What breaks if we **weaken the manifold structure** — say, allow $G$ to be only a topological manifold (no smooth atlas)? This is the regime of **topological groups**, and they form a much wider class than Lie groups. Topological groups include the $p$-adic numbers $\mathbb{Z}_p$, profinite groups, infinite-dimensional groups like $\mathrm{Homeo}(M)$, and many "wild" groups with no manifold structure at all. Hilbert's fifth problem (resolved by Gleason, Montgomery, and Zippin in 1952) asked whether every locally Euclidean topological group is automatically a Lie group; the answer is **yes**, which is a striking theorem: topological groups with smooth-manifold underlying spaces are exactly Lie groups, with no extra smoothness assumption needed. But for a clean axiomatization we keep "smooth manifold" in the definition, since this is what makes the calculus we want to do immediately available.

What if we **strengthen the axioms** by also requiring multiplication to be **analytic** rather than merely smooth? This gives the smaller class of **real-analytic Lie groups**. Every Lie group in the smooth sense is automatically real-analytic (this is a theorem; the underlying smooth manifold structure can be upgraded to a real-analytic structure compatibly with the group law). So the demand for analyticity is redundant on the level of objects, but not on the level of morphisms — a smooth Lie group homomorphism is automatically analytic, again by a non-trivial theorem. We work in the smooth category because it is the most natural for the techniques (partitions of unity, the inverse function theorem, etc.) and the analyticity comes free.

A particularly interesting question is the **dimension axiom**: should we demand $G$ be finite-dimensional? The objects of greatest interest in this chapter are finite-dimensional, and the major structural theorems (closed subgroup theorem, Lie correspondence, classification) are stated for finite-dimensional Lie groups. **Infinite-dimensional Lie groups** — diffeomorphism groups $\mathrm{Diff}(M)$, gauge groups, loop groups $LG$ — exist and are very important in geometric mechanics, gauge theory, and string theory, but they require additional functional-analytic machinery (Banach manifolds, Fréchet manifolds, tame Fréchet spaces) and the finite-dimensional theorems do not all transfer cleanly. Lee, following standard convention, restricts to finite-dimensional Lie groups, and so do we; the infinite-dimensional generalization is left to **Geometric Mechanics** and **Gauge Theory**.

The summary: the four pieces — smooth-manifold $G$, smooth $m$, smooth $i$, the group axioms — are each forced by one feature of "manifold + group simultaneously": the manifold structure provides the calculus, smooth $m$ ties calculus to the algebra, smooth $i$ makes the algebra reversible in a calculus-compatible way, and the group axioms make it all a group. Drop any one and you lose exactly that feature.

---

# The Definition

A **Lie group** is a smooth manifold $G$ equipped with a group structure $(m, i, e)$ such that the multiplication map $m : G \times G \to G$, $m(g, h) = gh$, and the inversion map $i : G \to G$, $i(g) = g^{-1}$, are both smooth. Equivalently:

- $G$ is a [[Def - Smooth Manifold|smooth manifold]] (Hausdorff, second countable, locally Euclidean, equipped with a maximal smooth atlas);
- $G$ is a [[Def - Group|group]] (a set with an associative binary operation, identity element, and inverses);
- the structure maps $m$ and $i$ are [[Def - Smooth Map between Manifolds|smooth maps]] of manifolds.

The **dimension** of $G$ as a Lie group is its dimension as a smooth manifold. We assume throughout that all Lie groups are finite-dimensional unless explicitly stated otherwise.

A **Lie group of dimension $0$** is a discrete countable group with the discrete topology — every $0$-dimensional smooth manifold is a countable discrete set, and the group structure imposes no further smoothness condition (any function from a discrete space is smooth). So finite groups and countably infinite discrete groups are degenerate Lie groups.

---

# Categorical Definition

Two complementary categorical formulations of "Lie group" illuminate the structure, and both are useful in practice.

**A Lie group is a group object in the category of smooth manifolds $\mathbf{Man}$.** A **group object** in a category $\mathcal{C}$ with finite products is an object $G$ equipped with three morphisms — multiplication $m : G \times G \to G$, identity $e : 1 \to G$ (where $1$ is the terminal object), and inversion $i : G \to G$ — such that the following diagrams commute, encoding associativity, the unit law, and the inverse law purely in terms of morphisms and products:

- *Associativity:* $m \circ (m \times \mathrm{id}_G) = m \circ (\mathrm{id}_G \times m) : G \times G \times G \to G$.
- *Unit:* $m \circ (e \times \mathrm{id}_G) \circ \lambda^{-1} = \mathrm{id}_G$ where $\lambda : G \to 1 \times G$ is the canonical isomorphism, and symmetrically on the right.
- *Inverse:* $m \circ (i \times \mathrm{id}_G) \circ \Delta = e \circ !$ where $\Delta : G \to G \times G$ is the diagonal and $! : G \to 1$ is the unique morphism to the terminal object, and symmetrically.

When $\mathcal{C} = \mathbf{Set}$, the terminal object is a one-point set, an arrow $1 \to G$ is the same as a choice of element of $G$, and the commuting diagrams unwind into the ordinary group axioms — so a group object in $\mathbf{Set}$ is exactly an ordinary group. When $\mathcal{C} = \mathbf{Man}$ (smooth manifolds and smooth maps), the terminal object is the one-point manifold $\{*\}$, an arrow $\{*\} \to G$ is a smooth map from a point — equivalently, a single element of $G$ (no smoothness content), and the diagrams give the Lie group axioms with all maps required to be smooth.

The categorical viewpoint makes several constructions automatic. The **category of Lie groups** $\mathbf{LieGrp}$ has Lie groups as objects and Lie group homomorphisms (smooth group homomorphisms) as morphisms. The **product of Lie groups** $G \times H$ — as a smooth manifold, with componentwise multiplication — is the categorical product in $\mathbf{LieGrp}$. The **kernel** of a Lie group homomorphism $F : G \to H$ is the equalizer of $F$ with the constant map to $e_H$, which is automatically a closed Lie subgroup (its smooth manifold structure follows from the closed subgroup theorem). The categorical viewpoint also delivers the right notion of "Lie group object" in other categories: in the category of complex manifolds one gets **complex Lie groups**; in the category of algebraic varieties over a field $k$ one gets **algebraic groups**; in the category of supermanifolds one gets **Lie supergroups**. The same diagram, interpreted in a different category, automatically gives the right notion.

**The Lie functor.** The assignment $G \mapsto \mathrm{Lie}(G) = T_e G$ (with its bracket from left-invariant vector fields) and $F \mapsto F_* = dF_e$ defines a functor

$$\mathrm{Lie} : \mathbf{LieGrp} \longrightarrow \mathbf{LieAlg}$$

from the category of Lie groups to the category of finite-dimensional real Lie algebras. Functoriality means that $(F \circ G)_* = F_* \circ G_*$ and $(\mathrm{id}_G)_* = \mathrm{id}_{\mathfrak{g}}$, both of which are direct consequences of the chain rule for the differential at $e$. The **Lie correspondence** is the deep statement that restricting $\mathrm{Lie}$ to the full subcategory $\mathbf{LieGrp}^{1\text{-conn}}$ of connected simply connected Lie groups gives an **equivalence of categories** with $\mathbf{LieAlg}$ (Lee Thm 20.21 and Problem 20-18) — every finite-dimensional Lie algebra is the Lie algebra of a unique simply connected Lie group, and Lie algebra homomorphisms lift uniquely to Lie group homomorphisms. The Lie functor is the linearization functor, and on the simply connected side it loses no information.

---

# Relate to Other Fields / Compression

A Lie group is a **group object in $\mathbf{Man}$**, the smooth-manifold incarnation of the same template that produces ordinary groups, topological groups, algebraic groups, and group schemes. The single set of axioms — associativity, unit, inverse, expressed as commuting diagrams — produces the right species of group in each category. This is the cleanest compression: Lie groups sit one categorical interpretation away from ordinary groups, just as Lie algebras sit one categorical reformulation away from associative algebras.

From the differential geometry side, a Lie group is a **smooth manifold equipped with a left action on itself that is free and transitive**. The action is left multiplication: $G$ acts on $G$ by $g \cdot h = gh$, and this action is free (only $e$ has fixed points) and transitive (every element is in one orbit). The free transitive action is what makes a Lie group **homogeneous**: every point looks like every other, with left translation providing the diffeomorphism. This homogeneity is the geometric source of the rigidity that makes Lie groups so much more tractable than general manifolds.

**True name:** A Lie group is **a manifold whose tangent bundle is trivializable in a canonical way, with the trivialization compatible with a group structure on the base**. The canonical trivialization is $TG \cong G \times \mathfrak{g}$ via $(g, X) \mapsto d(L_g)_e(X)$ — every left-invariant vector field gives a global section, and these span the tangent bundle. This characterization makes it manifest that *every Lie group is parallelizable* (Lee Cor 8.39), and it points to the central operational fact: **a vector field on $G$ is the same data as a function $G \to \mathfrak{g}$**, with left-invariant vector fields being the constant functions. This operational form is what one actually reaches for when computing.

---

# Examples / Corollaries

**Is an instance: $(\mathbb{R}^n, +)$.** Euclidean space with vector addition is an abelian Lie group of dimension $n$. The multiplication $m(x, y) = x + y$ is a polynomial in the coordinates (in fact linear), hence smooth; the inversion $i(x) = -x$ is linear and hence smooth. The Lie algebra is $\mathfrak{g} = T_0 \mathbb{R}^n \cong \mathbb{R}^n$ with the trivial bracket $[X, Y] = 0$.

**Is an instance: $\mathrm{GL}(n, \mathbb{R})$.** The group of invertible real $n \times n$ matrices is an open subset of $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$, so it inherits a smooth manifold structure of dimension $n^2$. Matrix multiplication is polynomial in the entries (hence smooth), and matrix inversion is rational in the entries by Cramer's rule with the determinant — nonzero on $\mathrm{GL}(n)$ — in the denominator (hence smooth). It is the canonical non-abelian Lie group.

**Is an instance: $S^1 \subset \mathbb{C}$.** The unit circle in the complex plane is a $1$-dimensional embedded submanifold of $\mathbb{C}$. With group structure given by complex multiplication, $m((e^{i\theta_1}), (e^{i\theta_2})) = e^{i(\theta_1 + \theta_2)}$, the multiplication is the addition map on angles, which is smooth in any angle chart. The inversion $i(e^{i\theta}) = e^{-i\theta}$ is similarly smooth. The Lie algebra is $\mathbb{R}$ with trivial bracket.

**Is an instance: $\mathrm{O}(n)$ and $\mathrm{SO}(n)$.** The orthogonal group $\mathrm{O}(n) = \{A \in \mathrm{GL}(n, \mathbb{R}) : A^T A = I\}$ is the preimage of $I$ under the smooth map $A \mapsto A^T A$. By the closed subgroup theorem (or directly via [[Thm - Regular Value Theorem on Manifolds|the regular value theorem]]), $\mathrm{O}(n)$ is a smooth submanifold of $\mathrm{GL}(n, \mathbb{R})$ of dimension $\binom{n}{2} = n(n-1)/2$. It has two connected components, distinguished by $\det = \pm 1$; the identity component $\mathrm{SO}(n)$ is connected and is the **rotation group** in $\mathbb{R}^n$.

**Is an instance: $\mathrm{SU}(2)$.** The special unitary group $\mathrm{SU}(2) = \{A \in \mathrm{GL}(2, \mathbb{C}) : A^* A = I, \det A = 1\}$ is, as a smooth manifold, diffeomorphic to the $3$-sphere $S^3$ — see [[Ex - SU(2) is Diffeomorphic to S^3]]. The group structure on $S^3$ corresponding to unit quaternion multiplication makes $S^3$ a Lie group, the only sphere besides $S^1$ to admit a Lie group structure (a deep theorem of Bott–Milnor and Kervaire rules out all other dimensions, with $S^7$ being only an "H-space" — non-associative).

**Is an instance: the Heisenberg group $\mathrm{Heis}(3)$.** The set of $3 \times 3$ real upper-triangular matrices with $1$s on the diagonal, $\mathrm{Heis}(3) = \{\begin{pmatrix} 1 & a & c \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix} : a, b, c \in \mathbb{R}\}$, is a $3$-dimensional Lie group under matrix multiplication. It is nilpotent (its Lie algebra has $[\mathfrak{h}, [\mathfrak{h}, \mathfrak{h}]] = 0$), non-abelian, simply connected, and diffeomorphic to $\mathbb{R}^3$ as a smooth manifold. It is the model for the canonical commutation relations of quantum mechanics, where $a, b, c$ play the role of position, momentum, and a central scalar.

**Is NOT an instance: a topological group on a non-smoothable manifold.** Consider $\mathrm{Homeo}(M)$ for a closed manifold $M$ of dimension $\geq 4$. This is a topological group under composition, but it is infinite-dimensional and not a smooth manifold in any natural way — it does not even have a clear notion of "smooth maps in" or "smooth maps out". Without manifold structure, the Lie-algebra machinery does not start. (One can give $\mathrm{Diff}(M)$ a structure of Fréchet Lie group, but that requires substantial functional-analytic machinery beyond the scope of this chapter.)

**Is NOT an instance: $(\mathbb{Q}, +)$.** The rational numbers under addition form an abelian group, but the underlying space $\mathbb{Q}$ is not a smooth manifold — it is a totally disconnected metric space, not locally Euclidean. So $\mathbb{Q}$ is a topological group but not a Lie group. Its closure $\mathbb{R}$ is a Lie group; the loss of smooth-manifold-ness from $\mathbb{R}$ to $\mathbb{Q}$ is exactly what disqualifies $\mathbb{Q}$.

**Is NOT an instance: $(\mathbb{R}, \star)$ with $a \star b = (a^3 + b^3)^{1/3}$.** This is a group homeomorphic to $(\mathbb{R}, +)$ via the homeomorphism $\phi(a) = a^{1/3}$ — the relation is $\phi(a + b) = a^{1/3} + b^{1/3}$ wait, actually $(a^3 + b^3)^{1/3}$ is the operation transported from $(\mathbb{R}, +)$ by $\phi(x) = x^{1/3}$, giving $\phi^{-1}(\phi(a) + \phi(b)) = ((a^3)^{1/3} + (b^3)^{1/3})^{... no}$ — let us be careful: define $a \star b = (a^3 + b^3)^{1/3}$ directly. Then $a \star b$ as a function of $(a, b)$ involves a cube root of a sum, which is smooth on $\{(a, b) : a^3 + b^3 \neq 0\}$ but **not smooth at $(0, 0)$** (the derivative of $x^{1/3}$ blows up at $x = 0$). So $(\mathbb{R}, \star)$ is a topological group whose multiplication is not smooth, hence not a Lie group with the standard smooth structure on $\mathbb{R}$. The lesson: smoothness of $m$ is a real condition, easily violated by group operations that are nevertheless continuous.

**Calibration check.** If you can (i) verify $\mathrm{GL}(n, \mathbb{R})$ is an open submanifold of $M(n, \mathbb{R})$ and hence a Lie group of dimension $n^2$; (ii) state the Lie group axioms in their categorical form (group object in $\mathbf{Man}$); (iii) explain why $(\mathbb{Q}, +)$ is not a Lie group even though it is a topological group; and (iv) compute $\dim \mathrm{SO}(3) = 3$ and $\dim \mathrm{SU}(2) = 3$ from the defining equations — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Lie Algebra of a Lie Group *(from this chapter)*
> Every Lie group $G$ has a canonical finite-dimensional **Lie algebra** $\mathfrak{g} = T_e G$ — see [[Def - The Lie Algebra of a Lie Group]]. This is the linear shadow of $G$ at the identity, and it captures, in a single vector space with a bilinear bracket, almost everything about how $G$ multiplies near $e$.

> [!tip] The Exponential Map *(from this chapter)*
> The bridge from $\mathfrak{g}$ back to $G$ is the **exponential map** $\exp : \mathfrak{g} \to G$ — see [[Def - Exponential Map of a Lie Group]]. It is a local diffeomorphism near $0 \in \mathfrak{g}$, takes lines through the origin to one-parameter subgroups, and intertwines Lie group homomorphisms with their Lie algebra differentials via the naturality square.

> [!tip] Principal Bundle *(from Gauge Theory)*
> A **principal $G$-bundle** is a smooth fibre bundle $P \to B$ whose fibre is the Lie group $G$ and on which $G$ acts smoothly, freely, and fibrewise. Principal bundles are the geometric objects encoding gauge symmetries in physics; the structure group's Lie algebra controls the connection forms, and the curvature is a Lie-algebra-valued $2$-form. Maxwell's electromagnetism is the case $G = \mathrm{U}(1)$; Yang–Mills theory is $G = \mathrm{SU}(N)$.

> [!tip] Algebraic Group *(from Algebraic Geometry)*
> An **algebraic group** is a group object in the category of algebraic varieties (or more generally schemes). The same definition as a Lie group, but with "smooth manifold" replaced by "algebraic variety over a field $k$" and "smooth map" by "morphism of varieties". Algebraic groups include $\mathrm{GL}(n, k)$, $\mathrm{SL}(n, k)$, all the classical Lie groups over arbitrary fields, and more exotic examples like reductive groups, semisimple groups, and tori. Over $k = \mathbb{R}$ or $\mathbb{C}$, the underlying topological space of an algebraic group is a Lie group, but in positive characteristic the algebraic side is the only available framework.

> [!tip] Lie Groupoid *(from Differential Geometry, Advanced)*
> A **Lie groupoid** generalizes Lie groups by allowing the multiplication to be only partially defined — a Lie groupoid is a small category in which all morphisms are invertible, the set of objects and the set of morphisms are smooth manifolds, and source/target/multiplication/inversion are smooth maps. Lie groups are the special case where the object set is a single point. Lie groupoids are the right framework for **foliations**, **orbifolds**, and **stacks**, and their infinitesimal counterparts are **Lie algebroids**.
