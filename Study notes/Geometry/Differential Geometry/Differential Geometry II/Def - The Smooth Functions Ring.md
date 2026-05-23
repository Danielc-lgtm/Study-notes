---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Function on a Manifold"
  - "Def - Ring"
  - "Def - Field"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold. $C^\infty(M)$ is the set of smooth functions $M \to \mathbb{R}$. Operations are pointwise: $(f + g)(p) = f(p) + g(p)$, $(fg)(p) = f(p) g(p)$, $(\lambda f)(p) = \lambda f(p)$ for $\lambda \in \mathbb{R}$. The constant function with value $c \in \mathbb{R}$ is denoted by $c$ or $\underline c$; the zero function is $0$, the constant $1$ function is $1$. For a smooth map $F : M \to N$, **pullback** is $F^* : C^\infty(N) \to C^\infty(M)$, $F^*(g) = g \circ F$. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Axiom Motivation

We have defined smooth functions $M \to \mathbb{R}$ in [[Def - Smooth Function on a Manifold]]. There are many of them — every constant, every coordinate function, every bump function, every polynomial in coordinate functions, every smooth function on $\mathbb{R}^n$ pulled back through a chart. The natural next question is *what structure do they form?* The pointwise operations suggest themselves: sum, product, scalar multiple — and these turn out to be the foundation of an entire algebraic perspective on smooth manifolds.

The first observation is that $C^\infty(M)$ is closed under each of these operations. If $f, g$ are smooth, then so are $f + g$ (sum of smooth Euclidean functions is smooth), $fg$ (product is smooth), $\lambda f$ for $\lambda \in \mathbb{R}$ (scalar multiple is smooth). Each verification is a chart calculation: $\widehat{f + g} = \widehat f + \widehat g$, $\widehat{fg} = \widehat f \cdot \widehat g$, etc. So $C^\infty(M)$ is a subset of the set of all functions $M \to \mathbb{R}$, closed under pointwise sum, product, and scalar multiplication — the algebraic structure inherited from $\mathbb{R}$.

The second observation is that these operations satisfy the axioms of a commutative [[Def - Ring|ring]] with $1$ ([[Def - Ring]]): associativity and commutativity of $+$ and $\cdot$, distributivity of $\cdot$ over $+$, the existence of additive inverses ($-f$ is smooth when $f$ is), the existence of $0$ (the zero function), and the existence of $1$ (the constant function $1$). All these are inherited pointwise from $\mathbb{R}$ — and $\mathbb{R}$ is itself a field, hence a commutative [[Def - Ring|ring]] with $1$.

The third observation is more interesting: the *constants* $\mathbb{R} \hookrightarrow C^\infty(M)$ form a [[Def - Subring|subring]], and they act centrally on every element of $C^\infty(M)$ (constant $\lambda$ commutes with every $f$ under multiplication). This makes $C^\infty(M)$ a **commutative $\mathbb{R}$-algebra**: a commutative ring with $1$ that is also a real vector space, with scalar multiplication and ring multiplication compatible: $\lambda(fg) = (\lambda f)g = f(\lambda g)$.

*Why pointwise operations?* Because pointwise operations are the only natural operations on $\mathbb{R}$-valued functions that respect *evaluation*: $(f + g)(p) = f(p) + g(p)$ is the only definition that makes evaluation $f \mapsto f(p)$ into a ring homomorphism $C^\infty(M) \to \mathbb{R}$. The evaluation [[Def - Homomorphism|homomorphisms]] $\operatorname{ev}_p : C^\infty(M) \to \mathbb{R}$ are central to the algebraic viewpoint: they are surjective (since constants are smooth), and their kernels $\mathfrak{m}_p = \{f : f(p) = 0\}$ are *maximal [[Def - Ideal|ideals]]* of $C^\infty(M)$. The cotangent space at $p$ will turn out to be $\mathfrak{m}_p / \mathfrak{m}_p^2$ (an algebraic incarnation of "first-order vanishing").

*Why insist on the $\mathbb{R}$-algebra structure (not just the ring structure)?* The reason is that almost every construction in differential geometry leverages real scalars: tangent vectors are $\mathbb{R}$-linear derivations, vector fields are $\mathbb{R}$-linear over the constants, exterior differentiation is $\mathbb{R}$-linear, integration is $\mathbb{R}$-linear. The ring structure captures the multiplicative behaviour; the $\mathbb{R}$-algebra structure adds the linear-algebraic behaviour. Both are needed.

*Why does the ring $C^\infty(M)$ encode the smooth structure?* Lee's Problem 2-10 establishes that a [[Def - Homeomorphism|homeomorphism]] $F : M \to N$ is a [[Def - Diffeomorphism|diffeomorphism]] if and only if pullback $F^* : C(N) \to C(M)$ restricts to an isomorphism $C^\infty(N) \to C^\infty(M)$. So the *algebra* $C^\infty(M)$, sitting inside $C(M)$, contains all the information of the smooth structure. This is the algebraic incarnation of the geometric object — a *ringed-space* description.

*What does it fail to capture?* Without further structure, $C^\infty(M)$ is just an abstract algebra and does not "remember" the topological space $M$ — but the maximal [[Def - Ideal|ideals]] of $C^\infty(M)$ recover the points of $M$ (under suitable conditions: $M$ second-countable Hausdorff), and the Zariski-style topology on $\operatorname{Spec}\,C^\infty(M)$ recovers the topology of $M$. So in principle the algebra knows everything; in practice we keep $M$ and $C^\infty(M)$ as a pair for clarity.

---

# The Definition

Let $M$ be a smooth manifold. The set
$$C^\infty(M) = \{f : M \to \mathbb{R} \mid f \text{ is smooth}\}$$
becomes a **commutative ring with $1$** under the pointwise operations:

**Addition:** $(f + g)(p) = f(p) + g(p)$.

**Multiplication:** $(fg)(p) = f(p) g(p)$.

**Zero:** the function identically $0$.

**One:** the function identically $1$.

**Negation:** $(-f)(p) = -f(p)$.

The ring axioms — associativity, commutativity, distributivity, the existence of additive inverses, and the existence of multiplicative identity — are inherited pointwise from $\mathbb{R}$. A ring homomorphism in the sense of [[Def - Ring Homomorphism]] is what pullback $F^*$ will become.

$C^\infty(M)$ is additionally a **real vector space** under pointwise scalar multiplication $(\lambda f)(p) = \lambda f(p)$, and the ring multiplication is bilinear with respect to this scalar multiplication: $\lambda(fg) = (\lambda f)g = f(\lambda g)$. This makes $C^\infty(M)$ a **commutative $\mathbb{R}$-algebra**: a commutative ring with $1$ that is also a vector space over $\mathbb{R}$, with the two structures compatibly tied together.

The constants form a [[Def - Subring|subring]] (and subalgebra) $\mathbb{R} \hookrightarrow C^\infty(M)$ via $c \mapsto \underline c$, the function identically $c$. This embedding sends the field $\mathbb{R}$ to the centre of $C^\infty(M)$ — in fact, since $C^\infty(M)$ is commutative, every element is "central", but the point is that constants are exactly the central elements that are also constants under any reasonable derivation.

**Pullback.** A smooth map $F : M \to N$ induces an $\mathbb{R}$-algebra homomorphism
$$F^* : C^\infty(N) \to C^\infty(M), \quad F^*(g) = g \circ F.$$
This is well-defined (composition of smooth maps is smooth), respects addition and multiplication (pointwise), sends $1$ to $1$, and is $\mathbb{R}$-linear. The assignment $M \mapsto C^\infty(M)$, $F \mapsto F^*$ is a contravariant functor from $\mathbf{Man}^\infty$ to the category of commutative $\mathbb{R}$-algebras.

---

# Categorical Definition

$C^\infty(M)$ is the **structure ring** of the ringed space $(M, \mathcal{O}_M^\infty)$ — the global sections of the sheaf of smooth functions. The category $\mathbf{Man}^\infty$ of smooth manifolds and smooth maps embeds **contravariantly** into the category of commutative $\mathbb{R}$-algebras: $M \mapsto C^\infty(M)$, $F \mapsto F^*$.

This contravariant embedding is *not* fully faithful in general — there exist abstract $\mathbb{R}$-algebras that are isomorphic to $C^\infty(M)$ but are not realized as smooth-function algebras of any other manifold — so the smooth-manifold structure is more than just the ring $C^\infty(M)$. However, when $M$ is appropriately "nice" (Hausdorff, second-countable, no boundary), the recovery is essentially complete: a [[Def - Homeomorphism|homeomorphism]] $F : M \to N$ is a [[Def - Diffeomorphism|diffeomorphism]] iff $F^* : C^\infty(N) \to C^\infty(M)$ is an isomorphism (Lee's Problem 2-10).

This is the smooth-category analogue of the **Gelfand–Naimark theorem** for compact Hausdorff spaces: the category of compact Hausdorff spaces is contravariantly equivalent to the category of commutative C*-algebras via $X \mapsto C(X)$. The smooth analogue is "smooth manifolds correspond contravariantly to certain commutative $\mathbb{R}$-algebras (those that are $C^\infty(M)$ for some smooth manifold)". The class of algebras realized as $C^\infty(M)$ has an abstract characterization (related to the theory of *smooth algebras* and *Fermat reals*), but the characterization is delicate.

The structure $(M, C^\infty(M))$ is a **commutative differential graded algebra** when combined with the de Rham complex of [[Differential Geometry VIII — Differential Forms|DG VIII]] and beyond.

---

# Relate to Other Fields / Compression

$C^\infty(M)$ is **literally the same construction** as the ring of continuous functions $C(M)$, restricted to smooth functions: a subset of $\mathbb{R}$-valued functions on $M$, closed under pointwise sum and product, containing the constants. This is the **commutative $\mathbb{R}$-algebra of admissible functions** template — and it generalizes to:

- $C(X)$, continuous real-valued functions on a topological space $X$;
- $\mathcal{O}(X)$, holomorphic functions on a complex manifold $X$;
- $\mathcal{O}_X(X)$, regular functions on an algebraic variety $X$;
- $L^p(X, \mu)$ (with appropriate modifications), measurable functions modulo a.e. equivalence.

In each case, the function algebra is a commutative ring (and often a $\mathbb{C}$- or $\mathbb{R}$-algebra), maximal ideals correspond to points (under good hypotheses), and morphisms of the underlying space correspond contravariantly to algebra homomorphisms. This is the **algebra-geometry duality** at the heart of modern geometry.

In **algebraic geometry**, the equivalence between commutative rings and affine schemes (Grothendieck) is the extreme form of this duality. Smooth manifold theory is a "shadow" of this — not quite as clean (the algebras $C^\infty(M)$ are not as well-behaved as polynomial rings), but the structural idea is the same.

In **functional analysis**, $C(X)$ for $X$ compact Hausdorff is a Banach algebra, and the Gelfand transform identifies it with a function algebra on its spectrum. $C^\infty(M)$ is a Fréchet algebra under the topology of uniform convergence of all derivatives on compact sets.

**True name:** *$C^\infty(M)$ is the algebra of admissible scalar quantities on $M$*. The operational meaning is that any quantity you can measure on $M$ in a smoothly-varying way — temperature, density, charge, height — is an element of $C^\infty(M)$. The algebra structure encodes the operations you can perform on these quantities: add two temperatures, multiply density by volume, etc.

---

# Examples / Corollaries

**Is an instance: $C^\infty(\mathbb{R}^n)$.** The ring of smooth functions on $\mathbb{R}^n$ is the usual ring of $C^\infty$ functions from multivariable calculus. It contains all polynomials, all rational functions with non-vanishing denominators, $\exp$, $\sin$, $\cos$, smooth bump functions, etc. It is an infinite-dimensional commutative $\mathbb{R}$-algebra.

**Is an instance: $C^\infty(\text{point})$ = $\mathbb{R}$.** The smooth manifold consisting of a single point has $C^\infty(\{*\}) = \mathbb{R}$ — every function on a single point is a real number. This is the terminal object in the algebra direction (the initial object in the manifold direction).

**Is an instance: $C^\infty(S^1)$.** The ring of smooth functions on the circle is the ring of smooth $2\pi$-periodic functions on $\mathbb{R}$ — and via Fourier series, it is in bijection with smooth functions on $S^1$ identified by their Fourier coefficients. It is infinite-dimensional and contains $\{e^{ikt} : k \in \mathbb{Z}\}$ as a dense subset (in the appropriate topology).

**Is an instance: $C^\infty(M)$ for $M$ compact.** If $M$ is compact, every smooth function on $M$ is bounded (continuous on compact $\Rightarrow$ bounded), and every continuous function attains its maximum (see [[Ex - A Continuous Function on a Compact Manifold Attains its Maximum]]). $C^\infty(M)$ is a subalgebra of $C(M)$, dense in the supremum norm (by Stone–Weierstrass-style arguments).

**Is NOT an instance: bounded functions on $M$.** The set of bounded smooth functions on $M$ is *not* a ring containing $1$ in the same sense — it is closed under sum and product, but not under arbitrary scalar multiples (unbounded scalars give unbounded functions). It is a Banach algebra under the supremum norm, not the same algebraic object as $C^\infty(M)$ unless $M$ is compact.

**Is NOT an instance: the ring of *real-analytic* functions $C^\omega(M)$.** This is a strict subalgebra of $C^\infty(M)$ — every real-analytic function is smooth, but most smooth functions are not analytic. The key distinction is that analytic functions are determined globally by their germ at any point (analytic continuation), while smooth functions have *independent* values at different points. So $C^\omega(M)$ is dramatically smaller than $C^\infty(M)$, and the analytic category lacks bump functions, partitions of unity, and the extension lemma.

**Is an instance of an $\mathbb{R}$-algebra homomorphism: pullback by a smooth map.** For $F : M \to N$ smooth, $F^* : C^\infty(N) \to C^\infty(M)$, $F^*(g) = g \circ F$, is an $\mathbb{R}$-algebra homomorphism: $F^*(g_1 + g_2) = (g_1 + g_2) \circ F = g_1 \circ F + g_2 \circ F = F^*(g_1) + F^*(g_2)$, similarly for products and scalars, and $F^*(1) = 1$.

**Is an instance: evaluation at a point.** For $p \in M$, $\operatorname{ev}_p : C^\infty(M) \to \mathbb{R}$, $f \mapsto f(p)$, is a surjective $\mathbb{R}$-algebra homomorphism with kernel $\mathfrak{m}_p = \{f : f(p) = 0\}$, a maximal ideal. The maximal ideals of $C^\infty(M)$ that arise this way are exactly the points of $M$ (under good conditions).

**Corollary (infinite-dimensional).** For any $M$ of [[Def - Dimension|dimension]] $\geq 1$, $C^\infty(M)$ is infinite-dimensional as an $\mathbb{R}$-vector space. *Proof sketch:* take any sequence of points $p_n \in M$ converging to nothing (possible by non-compactness, or by countably many disjoint open balls otherwise), build a bump function around each, get linearly independent smooth functions. (Lee Problem 2-7.)

**Corollary ($\mathbb{R}$ as a subalgebra).** The map $\mathbb{R} \to C^\infty(M)$, $c \mapsto \underline c$ (constant function), is an injective $\mathbb{R}$-algebra homomorphism. So $\mathbb{R}$ is a subalgebra of $C^\infty(M)$, and $C^\infty(M)$ is a (very large) extension of $\mathbb{R}$ as a commutative $\mathbb{R}$-algebra.

**Corollary (functoriality).** Pullback turns the assignment $M \mapsto C^\infty(M)$ into a contravariant functor $\mathbf{Man}^\infty \to \mathbf{CRing}_{\mathbb{R}}$ to commutative $\mathbb{R}$-algebras. The identity goes to the identity, composition reverses: $(G \circ F)^* = F^* \circ G^*$.

**Calibration check.** Verify the following: (i) the ring $C^\infty(\mathbb{R})$ contains the function $e^x$; verify it is a non-zero-divisor (multiplication by $e^x$ is injective). (ii) The ideal $\mathfrak{m}_0 = \{f \in C^\infty(\mathbb{R}) : f(0) = 0\}$ is maximal, with quotient $C^\infty(\mathbb{R})/\mathfrak{m}_0 \cong \mathbb{R}$. (iii) The pullback by inclusion $\iota : (0, 1) \hookrightarrow \mathbb{R}$ is a ring homomorphism $C^\infty(\mathbb{R}) \to C^\infty((0, 1))$ that is *not* surjective (the function $1/x$ is smooth on $(0,1)$ but is not the restriction of any function smooth on $\mathbb{R}$). (iv) For $M$ compact, the constants $\mathbb{R} \subseteq C^\infty(M)$ are the only smooth functions $f$ with $f \cdot g = 0 \Rightarrow g = 0$ for every nonzero $g$ — i.e., $\mathbb{R}$ is the set of units in some appropriate sense (this requires care: every nonzero constant is a unit, but there may be many other units).

---

# Unlocked by This

> [!tip] Tangent Vectors as Derivations *(from Differential Geometry)*
> A **tangent vector at $p \in M$** can be defined as a derivation at $p$ of the algebra $C^\infty(M)$: an $\mathbb{R}$-linear map $v : C^\infty(M) \to \mathbb{R}$ satisfying the Leibniz rule $v(fg) = v(f)g(p) + f(p)v(g)$. This is one of the three standard definitions of the tangent space (the others: equivalence classes of curves, geometric arrows in $\mathbb{R}^n$ via charts), and it is the algebraically cleanest. The tangent space $T_p M$ is the set of all such derivations; it is a finite-dimensional $\mathbb{R}$-vector space of dimension equal to $\dim M$. See [[Differential Geometry III — Tangent Vectors and the Differential|DG III]].

> [!tip] Vector Fields as Derivations *(from Differential Geometry)*
> A **smooth vector field** $X$ on $M$ is, equivalently, a derivation of the $\mathbb{R}$-algebra $C^\infty(M)$: an $\mathbb{R}$-linear $X : C^\infty(M) \to C^\infty(M)$ satisfying $X(fg) = X(f)g + fX(g)$. The Lie bracket $[X, Y] = XY - YX$ is then literally the commutator of derivations, and the space of smooth vector fields is a Lie algebra. This is the algebraic perspective; the geometric perspective (sections of the tangent bundle) is in [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]].

> [!tip] Maximal Ideals and Points *(from Algebraic Geometry / Commutative Algebra)*
> The maximal ideals of $C^\infty(M)$ (that arise from points) correspond bijectively to the points of $M$, via $p \mapsto \mathfrak{m}_p = \{f : f(p) = 0\}$. The cotangent space at $p$ is then $\mathfrak{m}_p / \mathfrak{m}_p^2$ — first-order vanishing modulo second-order vanishing. This algebraic characterization is the bridge to algebraic geometry, where the same definition gives the cotangent space at a point of an algebraic variety.

> [!tip] The Manifold as a Ringed Space *(from Algebraic Geometry / Sheaf Theory)*
> $(M, \mathcal{O}_M^\infty)$ — the manifold together with its sheaf of smooth functions — is a **ringed space**, and the entire category of smooth manifolds embeds in the category of ringed spaces. This makes "smooth manifold" a special case of the algebra-geometry duality at the foundation of modern geometry. Replacing $\mathcal{O}_M^\infty$ by other structure sheaves gives algebraic varieties (polynomial functions), complex manifolds (holomorphic functions), and schemes (any commutative ring locally).
