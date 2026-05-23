---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Field"
  - "Def - Abelian Group"
tags: [algebra, linear-algebra]
---

# Notation

A vector space is written $(V, +, \cdot)$ over a field $\mathbb{F}$: the underlying set $V$, the vector addition $+ : V \times V \to V$, and the scalar multiplication $\cdot : \mathbb{F} \times V \to V$, usually with the dot suppressed so that $\lambda v$ means $\lambda \cdot v$. Elements of $V$ are **vectors** (sometimes also **points**); elements of $\mathbb{F}$ are **scalars**. The additive identity of $V$ is $0_V$, or just $0$ when context permits — and the same symbol $0$ is also used for the scalar zero in $\mathbb{F}$. The additive inverse of $v$ is $-v$. Throughout this topic $\mathbb{F}$ denotes $\mathbb{R}$ or $\mathbb{C}$, with $\mathbb{F}^n$ the space of $n$-tuples and $\mathbb{F}^S$ the space of functions $S \to \mathbb{F}$.

See [[Linear Algebra I — §1 Vector Spaces]] for the full notation registry.

---

# Axiom Motivation

The thing we are trying to axiomatize is **the structure shared by all "spaces of arrows on which addition and scaling make sense"**. The motivating examples are the plane $\mathbb{R}^2$, ordinary space $\mathbb{R}^3$, and the higher-dimensional spaces $\mathbb{F}^n$, but also the spaces of solutions of linear differential equations, the spaces of polynomials of bounded degree, the spaces of functions on a set, the space of signed measures, and the tangent space to a manifold at a point. In each case there is a notion of "adding two things in the space" and "multiplying a thing by a scalar from $\mathbb{F}$", and *these are the only two operations*. The vector space axioms are the attempt to write down exactly the rules that "addition" and "scaling" must obey, so that any theorem proved from them speaks about every one of these examples at once.

The cleanest way to read the axioms is to split them into three [[Def - Group|groups]]. **Group one** says $(V, +, 0)$ is an [[Def - Abelian Group|abelian group]] — addition is commutative, associative, has an identity, and admits inverses. **Group two** says the scalar action $\mathbb{F} \curvearrowright V$ is unital and associative: $1 \cdot v = v$ and $(ab) \cdot v = a \cdot (b \cdot v)$. **Group three** is two distributive laws that tie the scalar action to addition on each side: $a(u+v) = au + av$ (distributing a scalar over a vector sum) and $(a+b)v = av + bv$ (distributing a scalar sum over a vector). Read this way, the seven-bullet definition collapses to "abelian group plus a compatible scalar action", and it stops being a list to be memorized and becomes a unit to be understood.

Each axiom captures one feature, and dropping it kills exactly that feature. **Drop commutativity of addition**, $u + v = v + u$: you would have to keep track of the order in which you summed arrows. The geometric content of vector addition — the parallelogram law, the fact that summing $u + v$ gives the same arrow no matter how the parallelogram is traversed — would be lost. The axiom is what makes "the sum of these $n$ vectors" well-defined without specifying an order. **Drop associativity of addition**: the same problem as for [[Def - Group|groups]] — the bracketing of $u_1 + \dots + u_n$ would matter, and the notion of a long sum would not be well-defined. **Drop the additive identity**: there is no "zero vector", and several constructions break instantly. The span of the empty list cannot be defined; the smallest subspace cannot be defined; the kernel of a linear map cannot be defined. **Drop additive inverses**: you can add and scale but you cannot subtract. Then $v + u = v + w$ no longer implies $u = w$. Many proofs (the linear-dependence lemma, the proof that bases have the same length) depend on cancellation, which comes from additive inverses.

**Drop $1 \cdot v = v$**: scalar multiplication could become trivial (e.g. $\lambda v = 0$ for every $\lambda, v$ would satisfy every other axiom). The unital axiom is the one that forces scalar multiplication to be non-degenerate, in the sense that it actually acts. **Drop $(ab) v = a(bv)$**: scaling by $2$ then by $3$ would not have to equal scaling by $6$, and successive scalings would not commute with the field's multiplication. The whole point of the scalar action is to be compatible with the scalars' own arithmetic, and this is the axiom that enforces it. **Drop $a(u + v) = au + av$**: scaling and addition would not commute, and the central manipulation of linear algebra — pull a scalar inside a sum, pull a sum inside a scalar — would fail. The proof that a span is closed under addition uses precisely this. **Drop $(a + b) v = av + bv$**: the same problem on the other side; the proof that span is closed under scalar multiplication uses this. The two distributive laws play symmetric roles and are jointly the entire glue between $V$'s additive structure and $\mathbb{F}$'s.

A test of whether the definition is correctly motivated is to ask: are there "redundant" axioms that follow from the others? A few mild ones — the uniqueness of the additive identity, the uniqueness of inverses, $0 v = 0_V$, $a \cdot 0_V = 0_V$, $(-1) v = -v$ — all follow from the listed axioms (see [[Thm - Uniqueness of Additive Identity and Inverses]]). They are not axioms because they are theorems. But the additive-inverse axiom genuinely cannot be dropped: it does not follow from $0v = 0$ alone unless one also imposes $0v = 0$ as an axiom (LADR Exercise 1B.5 makes this swap explicit). The axioms as listed are not strictly minimal; they are *clean*. They group naturally into "$V$ is an abelian group" and "$\mathbb{F}$ acts on it linearly", and the cost of redundancy is more than paid for in clarity.

One could ask whether to allow the scalar set to be more general. Replace the field $\mathbb{F}$ by a [[Def - Ring|ring]] $R$ and you get a [[Def - Module|module]]. Modules are genuine generalizations and are not artificially abstract: every abelian group is a $\mathbb{Z}$-module, and the [[Def - Polynomial Ring|polynomial ring]] $\mathbb{F}[x]$ acts on a vector space the moment an operator $T$ is chosen. But [[Def - Module|modules]] over a [[Def - Ring|ring]] fail many of the theorems that hold for vector spaces over a field — a module need not have a basis, [[Def - Dimension|dimension]] is not always well-defined, and the rank-nullity theorem becomes subtler. The reason vector-space theory is so clean is the field axiom of multiplicative inverses, which licences the division in Gaussian elimination and ultimately delivers the existence of bases.

---

# The Definition

Let $\mathbb{F}$ be a field. A **vector space over $\mathbb{F}$** is a set $V$ together with two operations — an **addition** $+ : V \times V \to V$ and a **scalar multiplication** $\cdot : \mathbb{F} \times V \to V$, with $\lambda \cdot v$ usually written $\lambda v$ — such that the following hold for all $u, v, w \in V$ and all $a, b \in \mathbb{F}$:

1. **Commutativity of addition.** $u + v = v + u$.
2. **Associativity of addition.** $(u + v) + w = u + (v + w)$.
3. **Additive identity.** There exists $0 \in V$ with $v + 0 = v$ for all $v \in V$.
4. **Additive inverses.** For every $v \in V$ there exists $w \in V$ with $v + w = 0$.
5. **Multiplicative identity.** $1 \cdot v = v$ (where $1$ is the multiplicative identity of $\mathbb{F}$).
6. **Associativity of scalar multiplication.** $(ab) v = a(bv)$.
7. **Distributivity over vector addition.** $a (u + v) = au + av$.
8. **Distributivity over scalar addition.** $(a + b) v = av + bv$.

A **real vector space** is a vector space over $\mathbb{R}$; a **complex vector space** is one over $\mathbb{C}$. Elements of $V$ are called **vectors** (or **points**); elements of $\mathbb{F}$ are called **scalars**.

The additive identity $0 \in V$ is unique, and each $v$ has a unique additive inverse; both facts are theorems following from the axioms — see [[Thm - Uniqueness of Additive Identity and Inverses]]. Consequently the additive inverse can be denoted $-v$ unambiguously, and subtraction $u - v$ is defined as $u + (-v)$.

---

# Categorical / Structural Definition

A vector space over $\mathbb{F}$ is precisely a **module over the field $\mathbb{F}$** (see [[Def - Module]]). In categorical language, the category $\mathbf{Vect}_{\mathbb{F}}$ has objects the $\mathbb{F}$-vector spaces and arrows the [[Linear Algebra III — §3A–D Linear Maps|linear maps]]; it sits inside $\mathbf{Mod}_R$ ([[Def - Module|modules]] over a [[Def - Ring|ring]] $R$) as the special case $R = \mathbb{F}$. The categorical features that distinguish $\mathbf{Vect}_{\mathbb{F}}$ from a generic module category are striking and worth naming up front:

**Every short exact sequence splits**: if $0 \to U \to V \to W \to 0$ is exact in $\mathbf{Vect}_{\mathbb{F}}$, then $V \cong U \oplus W$. This fails for general modules (it fails already for abelian groups, since $0 \to \mathbb{Z} \to \mathbb{Z} \to \mathbb{Z}/2 \to 0$ does not split). The splitting is what makes [[Def - Direct Sum|direct sum decompositions]] always available, and is the structural reason behind the existence of complementary [[Def - Subspace|subspaces]].

**Every vector space has a basis**, hence is free as a module (see [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]). The proof uses the axiom of choice in the infinite-dimensional case, but the finite-dimensional case is constructive and is the engine of Gaussian elimination. Free modules over a generic ring exist but most modules are not free; in $\mathbf{Vect}_{\mathbb{F}}$ *all* objects are free.

**Categorically, a vector space is an abelian group object together with an $\mathbb{F}$-action**, where the action is itself a group homomorphism $\mathbb{F} \to \operatorname{End}_{\mathbf{Ab}}(V)$ from the multiplicative monoid of $\mathbb{F}$ into the endomorphisms of $V$ as an abelian group. Reading the action this way exposes the symmetry: the additive group $(V, +)$ is one half, the scalar action is the other, and the two distributivities glue them.

The dual viewpoint — every vector space is the **free module on its basis** — is what makes linear algebra "the easy module theory": you can always reduce a question about a finite-dimensional vector space to a question about $\mathbb{F}^n$ by choosing coordinates.

---

# Relate to Other Fields / Compression

A vector space is **an abelian group with a linear action of the field $\mathbb{F}$**. The additive structure $(V, +, 0)$ is a perfectly ordinary [[Def - Abelian Group|abelian group]]; the scalar multiplication is an additional structure on top, a way of scaling vectors by field elements that respects both additive structures (on $V$ and on $\mathbb{F}$). Stripping the scalar action would leave a bare abelian group, which is a strictly weaker structure — for instance $\mathbb{R}$ and $\mathbb{R}^2$ are isomorphic as abelian groups (both are $\mathbb{Q}$-vector spaces of uncountable dimension) but not as $\mathbb{R}$-vector spaces.

A vector space is also **the most general object that looks like $\mathbb{F}^n$ up to choice of basis**. Every finite-dimensional vector space over $\mathbb{F}$ is isomorphic to $\mathbb{F}^n$ for some unique $n$ (its dimension), but the isomorphism depends on a choice of basis. This is the source of the "vectors are platonic objects, coordinate tuples are one viewing" frame: the vector is an element of $V$ independent of any basis, while the tuple $(x_1, \dots, x_n) \in \mathbb{F}^n$ depends on a chosen basis to identify it with a vector. Different bases give different tuples for the *same* vector, related by the [[Linear Algebra III — §3A–D Linear Maps|change-of-basis formula]]. Almost every conceptual difficulty in linear algebra (and most of its surprises) stem from confusing the vector with one of its representations.

**True name:** the operational true name of a vector space is "a set on which you can take linear combinations". A linear combination $a_1 v_1 + \dots + a_n v_n$ is just an iterated application of the two operations, and every meaningful construction in linear algebra — spans, linear maps, kernels, ranges, bases — is built out of linear combinations. When you reach for the axioms in a proof, what you almost always need is closure under linear combinations, not the axioms one by one.

---

# Examples / Corollaries

**Is an instance: $\mathbb{F}^n$, the standard $n$-dimensional space.** With $\mathbb{F}$ a field and $n \geq 0$, the set $\mathbb{F}^n = \{(x_1, \dots, x_n) : x_i \in \mathbb{F}\}$ with coordinate-wise addition and scalar multiplication. This is the motivating example and the prototype: every finite-dimensional vector space over $\mathbb{F}$ is isomorphic to $\mathbb{F}^n$ for a unique $n$, once a basis is chosen. The case $n = 0$ gives the trivial vector space $\{0\}$, with one element and a single way to add and scale it.

**Is an instance: $\mathbb{F}^\infty$, the space of all sequences.** The set $\{(x_1, x_2, \dots) : x_i \in \mathbb{F}\}$ with component-wise operations is a vector space over $\mathbb{F}$. It is **infinite-dimensional**, and it is the natural home of sequences in analysis. See [[Ex - F^infinity is not the union of finite-dimensional subspaces]] for a structural distinction between $\mathbb{F}^\infty$ and its finite-dimensional pieces.

**Is an instance: $\mathbb{F}^S$, the space of functions $S \to \mathbb{F}$.** For any set $S$, the functions $f : S \to \mathbb{F}$ form a vector space over $\mathbb{F}$ under pointwise operations: $(f + g)(s) = f(s) + g(s)$ and $(\lambda f)(s) = \lambda f(s)$. This is a uniform construction: $\mathbb{F}^n = \mathbb{F}^{\{1, \dots, n\}}$ and $\mathbb{F}^\infty = \mathbb{F}^{\mathbb{N}}$. The vector space of continuous, differentiable, integrable, or polynomial real-valued functions on an interval are all [[Def - Subspace|subspaces]] of $\mathbb{R}^{[0,1]}$ or $\mathbb{R}^{\mathbb{R}}$.

**Is an instance: $\mathcal{P}(\mathbb{F})$, the space of polynomials with coefficients in $\mathbb{F}$.** With the usual addition and scalar multiplication, $\mathcal{P}(\mathbb{F})$ is an infinite-dimensional vector space over $\mathbb{F}$. Its subspace $\mathcal{P}_m(\mathbb{F})$ of polynomials of degree at most $m$ is finite-dimensional, isomorphic to $\mathbb{F}^{m+1}$ via the coordinate map $a_0 + a_1 x + \dots + a_m x^m \mapsto (a_0, \dots, a_m)$.

**Is an instance: the space of signed measures on a measurable space.** The set of signed measures on $(\Omega, \mathcal{F})$ — see [[Def - Signed Measure]] — forms a real vector space under pointwise operations. This is a bridge into measure theory: linear-algebra notions (norm, dual, basis) acquire measure-theoretic meaning (total variation, Radon-Nikodym, atoms).

**Is an instance: the tangent space to a smooth manifold at a point.** For a smooth manifold $M$ and a point $p \in M$, the tangent space $T_p M$ is an $\mathbb{R}$-vector space of [[Def - Dimension|dimension]] $\dim M$. Locally, $T_p M \cong \mathbb{R}^n$ via any chart, but the vector space is intrinsic; the tuple of coordinates is the chart-dependent representation. See [[Def - The Total Derivative and Differentiability]] for the related notion in $\mathbb{R}^n$.

**Is NOT an instance: $\mathbb{N}$ under addition.** The natural numbers form an abelian monoid but **fail axiom 4** (additive inverses): $3$ has no $w$ with $3 + w = 0$. Even before scalar multiplication enters, the additive structure is wrong. To make it a $\mathbb{Z}$-module (let alone an $\mathbb{R}$-vector space), one passes to $\mathbb{Z}$.

**Is NOT an instance: $\mathbb{R}_{>0}$ with ordinary addition.** The positive reals with the usual addition is a semigroup, again failing axiom 4 (no negative element). Interestingly, $\mathbb{R}_{>0}$ *does* form a real vector space under the operations $u \oplus v = uv$ and $\lambda \odot u = u^\lambda$ — this is the trick whereby exponentials linearize multiplication. The carrier set alone does not determine whether you have a vector space; the operations are part of the data.

**Is NOT an instance: $\mathbb{R} \cup \{\infty, -\infty\}$ with the extended arithmetic of LADR Exercise 1B.6.** The set fails several axioms. The most obvious is that $\infty + (-\infty) = 0$ together with distributivity fails: $(1 + 1) \infty = 2 \infty = \infty$ but $1 \cdot \infty + 1 \cdot \infty = \infty + \infty = \infty$ which is consistent, but $(1 + (-1)) \infty = 0 \cdot \infty = 0$ while $1 \cdot \infty + (-1) \cdot \infty = \infty + (-\infty) = 0$, also consistent — yet associativity of addition fails: $(1 + \infty) + (-\infty) = \infty + (-\infty) = 0$ while $1 + (\infty + (-\infty)) = 1 + 0 = 1$. The non-example illustrates how delicate the axioms are: any breaks in associativity propagate and contaminate the whole structure.

**Corollary (uniqueness of the additive identity).** The zero vector is unique. If $0$ and $0'$ both satisfy axiom 3, then $0' = 0' + 0 = 0 + 0' = 0$, using axiom 3 for $0$ and commutativity. So writing "the" zero vector is justified. This is [[Thm - Uniqueness of Additive Identity and Inverses]].

**Corollary (uniqueness of additive inverses).** Each $v \in V$ has exactly one additive inverse. If $w$ and $w'$ both satisfy $v + w = v + w' = 0$, then $w = w + 0 = w + (v + w') = (w + v) + w' = 0 + w' = w'$. The argument uses associativity (axiom 2) crucially. Again, this is in [[Thm - Uniqueness of Additive Identity and Inverses]] and justifies the notation "$-v$".

**Corollary ($0 \cdot v = 0$).** For every $v \in V$, $0 \cdot v = 0$, where the $0$ on the left is the scalar zero and the $0$ on the right is the zero vector. The proof is one line: $0 v = (0 + 0) v = 0v + 0v$, so adding $-(0v)$ to both sides gives $0 = 0v$. This is what licenses the manipulation "drop a scalar zero from a sum".

**Corollary ($(-1) v = -v$).** $(-1) v + v = (-1) v + 1 v = (-1 + 1) v = 0 v = 0$, so $(-1) v$ is the additive inverse of $v$. The scalar $-1$ does its job at the level of vectors. This is what licenses writing $v - u$ for $v + (-u)$ and is used throughout proofs that subspaces are closed under inverses.

**Calibration check.** If you have understood the definition you should be able to (i) verify that $\{0\}$ is a vector space (the trivial one); (ii) check that the set of real-valued sequences with only finitely many nonzero terms is a subspace of $\mathbb{R}^\infty$; (iii) explain in one sentence why the constant-$1$ function is not in the subspace of continuous functions $f : [0,1] \to \mathbb{R}$ with $\int_0^1 f = 0$ (it fails closure under nothing — it just is not in the set, illustrating that subspace conditions are necessary but not sufficient for membership).

---

# Unlocked by This

> [!tip] Linear Map *(from Linear Algebra II–III)*
> Once you have vector spaces, the natural morphisms are **linear maps** — functions $T : V \to W$ between vector spaces over the same field that respect addition and scalar multiplication. The entire theory of linear algebra past this chapter is about these maps: their kernels, ranges, matrices, eigenvalues, and how they decompose. See [[Linear Algebra III — §3A–D Linear Maps]].

> [!tip] Module *(from Algebra)*
> Replace the field by an arbitrary [[Def - Ring|ring]] and you get a [[Def - Module|module]]. Modules are strictly more general than vector spaces, and the theory loses key theorems: bases need not exist, dimension need not be well-defined, and quotients of free modules need not be free. The vector-space theory is the "easy module theory" precisely because every nonzero scalar is invertible.

> [!tip] Affine Space *(from Geometry)*
> Forget the origin and you get an **affine space** — a set on which a vector space acts freely and transitively, so that you can take *differences* of points (giving vectors) but not *sums* of points. Affine spaces model "spacetime without a preferred origin", and the configuration spaces of mechanics. See also [[Linear Algebra IV — §3E–F Products, Quotients, Duality]] for affine subsets.

> [!tip] Banach Space and Hilbert Space *(from Functional Analysis)*
> Equip a vector space with a **norm** and require completeness, and you get a **Banach space**. Equip it with an **inner product** (and require completeness) and you get a **Hilbert space**. These are the right setting for infinite-dimensional vector spaces in analysis: the function spaces $L^p(\mu)$, the Sobolev spaces $H^k$, the spaces of distributions. The finite-dimensional theory developed in this topic generalizes to Banach spaces with substantial new content; Hilbert spaces are the closest infinite-dimensional analogue of $\mathbb{R}^n$ with its dot product.

> [!tip] Tangent Space and Vector Bundle *(from Differential Geometry)*
> At each point of a smooth manifold $M$, the **tangent space** $T_p M$ is a real vector space of dimension $\dim M$. Bundling these vector spaces together gives the **tangent bundle** $TM$, a smooth manifold whose fibre over each point is a vector space. Every theorem of finite-dimensional linear algebra applies pointwise on a smooth manifold, and the resulting machinery — connections, curvature, differential forms — is one of the most consequential applications of linear algebra in physics and geometry. See [[Def - The Total Derivative and Differentiability]] for the linear-algebraic content of the derivative.

> [!tip] Lie Algebra *(from Lie Theory)*
> A **Lie algebra** is a vector space equipped with a bilinear bracket $[\cdot, \cdot] : V \times V \to V$ that is alternating and satisfies the Jacobi identity. Lie algebras are the "tangent spaces at the identity" of [[Def - Group|Lie groups]] and capture the local symmetry structure of geometry and physics. The starting point is the linear structure of the underlying vector space; the bracket is the additional data.

> [!tip] Convex Set, Convex Function *(from Convex Analysis and Optimization)*
> The notions of **convex combination** $\lambda u + (1 - \lambda) v$ with $\lambda \in [0,1]$ and the resulting **convex sets** and **convex functions** are intrinsic to a real vector space: they use only the affine structure plus an ordering on $\mathbb{R}$. Linear programming, support vector machines, and the geometry of optimization all live in this enriched vector-space setting.
