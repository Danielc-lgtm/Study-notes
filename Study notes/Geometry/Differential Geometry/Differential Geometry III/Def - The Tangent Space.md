---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - The Smooth Functions Ring"
  - "Def - Derivation at a Point"
  - "Def - Vector Space"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a [[Def - Smooth Manifold|smooth n-manifold]] and $p \in M$. $C^{\infty}(M)$ denotes the ring of [[Def - Smooth Function on a Manifold|smooth real-valued functions]] on $M$. A **derivation at $p$** is a linear map $v : C^{\infty}(M) \to \mathbb{R}$ satisfying the Leibniz rule $v(fg) = f(p)\,v(g) + g(p)\,v(f)$; see [[Def - Derivation at a Point]]. We write $T_{p}M$ for the tangent space and use lowercase letters $v, w$ for tangent vectors. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Axiom Motivation

We want a notion of "tangent space at $p \in M$" that satisfies four desiderata: (i) it is a finite-dimensional real vector space, of dimension equal to $\dim M$; (ii) it is intrinsic — defined using only $M$ and its smooth functions, with no ambient $\mathbb{R}^{N}$ involved; (iii) every smooth map between manifolds induces a linear map between tangent spaces; (iv) when $M$ is an open subset of $\mathbb{R}^{n}$, $T_{p}M$ recovers the geometric tangent space $\mathbb{R}^{n}$ canonically. These four together pin the construction down — and the derivation definition is the cleanest construction that achieves them.

The need for (ii) is forced by the move to abstract manifolds. A submanifold of $\mathbb{R}^{N}$ has a tangent space defined as a subspace of the ambient $\mathbb{R}^{N}$ (see [[Def - The Tangent Space to a Submanifold]]), but for a manifold given only by charts and atlas — with no embedding — this is unavailable. The naive idea "take a tangent vector to be a tuple of $n$ numbers" fails because it would depend on the choice of chart. The way out, found by Lie, Cartan, and the modern school, is to define the tangent space using only $C^{\infty}(M)$, which is itself coordinate-free.

The cleanest such construction is **derivations**. A derivation at $p$ — see [[Def - Derivation at a Point]] — is a linear map $v : C^{\infty}(M) \to \mathbb{R}$ satisfying the Leibniz product rule. The set of derivations is automatically a vector space under pointwise operations (linearity and Leibniz are preserved by linear combinations), addressing desideratum (i). The construction is manifestly intrinsic, addressing (ii). The induced linear map between tangent spaces is given by $(dF_{p}(v))(f) = v(f \circ F)$ for a smooth map $F : M \to N$ — pre-composition makes derivations *covariant*, addressing (iii). And on $\mathbb{R}^{n}$, every derivation at $a$ is a directional derivative $D_{v}|_{a}$ for a unique $v \in \mathbb{R}^{n}$ (proved as [[Thm - Equivalence of Tangent Vector Definitions|Proposition 3.2 of Lee]]), addressing (iv) canonically — no choice of basis required.

Why pick derivations rather than equivalence classes of curves? Both definitions are valid (and equivalent — see [[Thm - Equivalence of Tangent Vector Definitions]]), but derivations are *cleaner* for proofs. Adding two equivalence classes of curves requires choosing representatives and showing the sum-class is independent of the choice — there is real work to do, in a chart. Adding two derivations is just $(v_{1} + v_{2})(f) := v_{1}(f) + v_{2}(f)$, which is manifestly linear and Leibniz by inspection. The vector-space structure on $T_{p}M$ is *transparent* in the derivation formulation and *constructible-but-not-transparent* in the curve formulation. For the same reason, functoriality of the construction (the chain rule for $dF$) is two lines in the derivation picture and a calculation in the curve picture.

Why not the chart-tuple definition? The chart-tuple definition — "$T_{p}M$ is the set of equivalence classes of $n$-tuples, one per chart, related by Jacobians" — addresses (i) and (iv) cleanly but obscures (ii) and (iii). The tuple definition forces every theorem to be checked across charts and the chain rule to be proven via the multivariate chain rule. It is the working definition for physicists computing components, but it is heavy for proofs. The derivation definition is the modern standard precisely because it factors the chart calculations out of the theory and into the equivalence theorem.

The remarkable content is that *all three definitions yield the same vector space*, naturally. This is the technical heart of the chapter, proved as [[Thm - Equivalence of Tangent Vector Definitions]]. The proof reduces to Taylor's theorem with remainder applied to a derivation at $a \in \mathbb{R}^{n}$, which forces $v$ to be a linear combination $v = v^{i}\,\partial/\partial x^{i}|_{a}$ with $v^{i} = v(x^{i})$.

A reader who has never seen this definition could invent it by the following route. Recognise that on $\mathbb{R}^{n}$, vectors and directional-derivative operators are interchangeable. Notice that directional-derivative operators satisfy two algebraic identities (linearity, Leibniz). Promote these identities to a definition. Verify (by Taylor's theorem) that this captures the geometric vectors on $\mathbb{R}^{n}$. Adopt the same definition on abstract manifolds. The crucial step is the trust that an algebraic axiomatization can be equivalent to the geometric picture — and that trust is rewarded by the equivalence theorem.

---

# The Definition

Let $M$ be a smooth manifold and $p \in M$. The **tangent space** to $M$ at $p$ is the real vector space
$$T_{p}M \;=\; \{\, v : C^{\infty}(M) \to \mathbb{R} \mid v \text{ is } \mathbb{R}\text{-linear and satisfies the Leibniz rule at } p\,\}$$
of all [[Def - Derivation at a Point|derivations at p]], with vector-space operations defined pointwise on functions:
$$(v_{1} + v_{2})(f) = v_{1}(f) + v_{2}(f), \qquad (cv)(f) = c \cdot v(f).$$

The elements of $T_{p}M$ are called **tangent vectors** to $M$ at $p$.

By [[Thm - Dimension of the Tangent Space]], $T_{p}M$ is finite-dimensional with $\dim T_{p}M = \dim M$. By [[Thm - Equivalence of Tangent Vector Definitions]], the same vector space arises in three equivalent ways:

- as the space of derivations $v : C^{\infty}(M) \to \mathbb{R}$ at $p$ (this definition);
- as the set $V_{p}M$ of equivalence classes $[\gamma]$ of smooth curves $\gamma$ with $\gamma(0) = p$, under the equivalence $\gamma_{1} \sim \gamma_{2}$ iff $(f \circ \gamma_{1})'(0) = (f \circ \gamma_{2})'(0)$ for every smooth $f$ (see [[Def - Tangent Vector via Equivalence Classes of Curves]]);
- as the chart-tuple space $\{(v^{1}, \dots, v^{n}) \mid \text{for each chart, related by Jacobians}\}$.

The three definitions are interchangeable, and the choice between them is a matter of which is most convenient for the problem at hand.

---

# Categorical / Structural Definition

The tangent-space construction $(M, p) \mapsto T_{p}M$ is a **covariant functor** from the category $\mathrm{Diff}_{*}$ of pointed smooth manifolds to the category $\mathrm{Vec}_{\mathbb{R}}$ of real vector spaces. We unpack what this means and why it matters.

A **pointed smooth manifold** is a pair $(M, p)$ with $M$ a smooth manifold and $p \in M$ a distinguished point. A **morphism of pointed smooth manifolds** $(M, p) \to (N, q)$ is a smooth map $F : M \to N$ with $F(p) = q$. These objects and morphisms form a category $\mathrm{Diff}_{*}$ — composition is composition of maps, identities are identity maps.

The category $\mathrm{Vec}_{\mathbb{R}}$ has real vector spaces as objects and real-linear maps as morphisms. (See [[Def - Vector Space]] and [[Def - Linear Map]].)

A **covariant functor** $T : \mathrm{Diff}_{*} \to \mathrm{Vec}_{\mathbb{R}}$ is a rule that assigns
- to each pointed manifold $(M, p)$, a vector space $T(M, p)$,
- to each smooth pointed map $F : (M, p) \to (N, q)$, a linear map $T(F) : T(M, p) \to T(N, q)$,

such that identities go to identities and composition is preserved:
$$T(\mathrm{id}_{M}) = \mathrm{id}_{T(M,p)}, \qquad T(G \circ F) = T(G) \circ T(F).$$

The construction $T(M, p) := T_{p}M$ on objects and $T(F) := dF_{p}$ on morphisms is precisely such a functor. The two functor axioms are the content of [[Thm - Chain Rule for the Differential]]. The whole chapter — three equivalent definitions of $T_{p}M$, the differential, the chain rule, the coordinate formula, the velocity-of-curve formula — is the proof that this functor exists and is well-defined.

**Why the functor viewpoint matters.** Three reasons.

First, it captures the *naturality* of the tangent-space construction. Naturality means: there is a *canonical* way to identify $T_{p}M$ with the analogous space defined by any other equivalent recipe (derivation, curve class, chart tuple), and the canonical identification commutes with the differentials of every smooth map. Concretely, the equivalence of the three tangent-vector definitions is the statement that *three different functors are isomorphic as functors*, with the isomorphism commuting with every $dF$. Naturality is what justifies the slogan "the tangent space is intrinsic to the manifold, not chart-dependent".

Second, it makes the tangent bundle's functoriality immediate. The global construction $T : \mathrm{Diff} \to \mathrm{Diff}$, sending $M \mapsto TM$ and $F \mapsto dF$, is itself a covariant functor — see [[Thm - The Tangent Bundle is a Smooth Manifold]] and [[Def - The Tangent Bundle]]. Higher iterates $T^{k}M$ are also functorial, leading to the formalism of jet bundles.

Third, it situates the tangent space in the broader context of **infinitesimal linearization functors**. Other examples include: the Zariski tangent space functor in algebraic geometry; the Lie algebra functor $\mathfrak{g} = T_{e}G$ from Lie groups to Lie algebras (which preserves the bracket — a richer structure); the cotangent functor (contravariant, sending $F$ to $dF_{p}^{*}$); the Kähler-differentials functor in commutative algebra. All these are different incarnations of the same idea: a "linearization at a point" is a functor from a category of structured spaces to a linear category.

The Lee construction makes the functor structure obvious: $T(M, p) = T_{p}M$ is *defined* using only $C^{\infty}(M)$, and $T(F) = dF_{p}$ is *defined* by pre-composition $(dF_{p}(v))(f) = v(f \circ F)$. The chain rule $T(G \circ F) = T(G) \circ T(F)$ is then immediate from the associativity of composition: $((d(G \circ F)_{p})(v))(f) = v(f \circ G \circ F) = (dF_{p}(v))(f \circ G) = (dG_{F(p)} \circ dF_{p})(v)(f)$.

---

# Relate to Other Fields / Compression

In **multivariate analysis**, the tangent space at a point of an open subset $U \subseteq \mathbb{R}^{n}$ is canonically $\mathbb{R}^{n}$ itself — there is no curvature or bending to worry about. The total derivative $Df_{x_{0}} : \mathbb{R}^{n} \to \mathbb{R}^{m}$ from [[Def - The Total Derivative and Differentiability]] is the manifold differential in this special case, with $T_{x_{0}}U \cong \mathbb{R}^{n}$ and $T_{f(x_{0})}\mathbb{R}^{m} \cong \mathbb{R}^{m}$ canonically. The manifold construction is a coordinate-free packaging of the multivariate construction that preserves the algebraic content while shedding the dependence on the ambient $\mathbb{R}^{n}$.

In **special relativity**, the tangent space at an event $p$ of [[Def - Minkowski Space and the Metric|Minkowski space]] is the space of [[Def - Four-Vector|four-vectors]] at $p$ — four-velocities, four-momenta, and so on. The flat geometry of Minkowski space makes $T_{p}M$ canonically identified with $\mathbb{R}^{4}$ at every $p$, which is why one rarely sees explicit tangent-space language in introductory special relativity. The distinction becomes important in general relativity, where the spacetime is curved and $T_{p}M$ varies non-trivially with $p$.

In **algebraic geometry**, the same definition applied to the local ring $\mathcal{O}_{X, p}$ at a point of a variety produces the **Zariski tangent space** $(\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2})^{*}$. For smooth varieties this matches the differential-geometric tangent space; at singular points it is larger, and the discrepancy *defines* singularities.

**True name:** A tangent vector at $p$ is "a velocity through $p$" — the geometric picture of a curve passing through $p$ with an instantaneous direction-and-speed. The derivation formulation is a clean algebraic re-encoding; the chart-tuple formulation is a calculational realization. But the picture that should fire in your head when you read "tangent vector at $p$" is a curve $\gamma$ with $\gamma(0) = p$ and a velocity arrow $\gamma'(0)$ at $p$. This is the picture every concrete computation in differential geometry uses.

---

# Examples / Corollaries

**Tangent space of $\mathbb{R}^{n}$ at $a$.** $T_{a}\mathbb{R}^{n}$ is canonically isomorphic to $\mathbb{R}^{n}$, via $v \mapsto D_{v}|_{a}$ where $D_{v}|_{a} f = (d/dt)|_{0} f(a + tv) = v^{i}\,\partial f/\partial x^{i}(a)$. This is the prototype of every tangent space — see [[Thm - Equivalence of Tangent Vector Definitions]] for the proof that every derivation has this form. The coordinate basis is $\partial/\partial x^{i}|_{a}$, the usual partial derivatives.

**Tangent space of an open subset of $\mathbb{R}^{n}$.** If $U \subseteq \mathbb{R}^{n}$ is open and $a \in U$, the inclusion $\iota : U \hookrightarrow \mathbb{R}^{n}$ induces an isomorphism $d\iota_{a} : T_{a}U \to T_{a}\mathbb{R}^{n} \cong \mathbb{R}^{n}$. The proof uses bump functions: every smooth function on $U$ can be extended (after multiplication by a bump) to a smooth function on $\mathbb{R}^{n}$, and locality of derivations makes the extension's choice irrelevant. So tangent vectors at $a$ to an open subset are just tangent vectors to $\mathbb{R}^{n}$.

**Tangent space of $\mathrm{GL}(n, \mathbb{R})$ at the identity.** $\mathrm{GL}(n, \mathbb{R})$ is the open subset $\{A \in M_{n}(\mathbb{R}) : \det A \neq 0\}$ of the vector space $M_{n}(\mathbb{R})$ of all $n \times n$ matrices. So $T_{I}\mathrm{GL}(n, \mathbb{R}) \cong M_{n}(\mathbb{R})$ canonically — every $n \times n$ real matrix arises as a tangent vector at $I$. This is the most important *single* tangent-space computation in geometry, because it identifies the Lie algebra $\mathfrak{gl}(n) = M_{n}(\mathbb{R})$. See [[Ex - Tangent Space of the General Linear Group at the Identity]].

**Tangent space of a finite-dimensional vector space.** If $V$ is a real vector space of dimension $n$ with its standard smooth structure (any linear isomorphism with $\mathbb{R}^{n}$ provides a chart, and any two such isomorphisms are smoothly compatible), then $T_{a}V \cong V$ canonically for every $a \in V$. The isomorphism is $v \mapsto D_{v}|_{a}$, $f \mapsto (d/dt)|_{0} f(a + tv)$. This generalizes the $\mathbb{R}^{n}$ case and is the source of the slogan "tangent vectors to a vector space are elements of the vector space itself".

**Tangent space of a product manifold.** For $p = (p_{1}, p_{2}) \in M_{1} \times M_{2}$, $T_{p}(M_{1} \times M_{2}) \cong T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}$ canonically, with the isomorphism sending $v$ to $(d\pi_{1,p}(v), d\pi_{2,p}(v))$. See [[Thm - Tangent Space of a Product Manifold]].

**Is NOT a tangent vector: a "vector pointing in the direction $\partial_{x}$" without specifying a chart.** A tangent vector at $p$ has a definite value as an operator on $C^{\infty}(M)$, but its *components* depend on the chart. The expression "the tangent vector $(1, 0, 0)$ at $p$" is meaningless on a manifold without naming the chart, because under a different chart the same tangent vector has different components. This is why tangent vectors live in $T_{p}M$ abstractly, not in $\mathbb{R}^{n}$ — the components are chart-dependent, the vector is not.

**Corollary — the tangent space is canonically a vector space.** The pointwise addition and scalar multiplication of derivations preserve linearity and Leibniz, so $T_{p}M$ is automatically a vector space. No choice of basis or chart is needed. This is the cleanest advantage of the derivation definition over the curve definition.

**Corollary — locality.** A tangent vector $v \in T_{p}M$ depends only on the germ of functions at $p$: if $f$ and $g$ agree on any neighbourhood of $p$, then $v(f) = v(g)$. The proof uses bump functions and the Leibniz rule's annihilation of $\psi \cdot (f - g)$ when $\psi$ is supported where $f - g$ vanishes. This justifies treating $v$ as acting on functions defined only locally near $p$, even though the original definition demands a function on all of $M$.

**Calibration check.** Verify that for any $p \in \mathbb{R}^{n}$, the derivation $\partial/\partial x^{1}|_{p}$ takes the coordinate function $x^{1}$ to $1$ and every other coordinate function $x^{i}$ to $0$. Verify that the sum of two derivations is a derivation (check both axioms). Verify that the zero map $v \equiv 0$ is a derivation, providing the additive identity of $T_{p}M$. If you can also explain why the action of a derivation on a constant function must be zero, you have understood the algebraic core of the definition.

---

# Unlocked by This

> [!tip] The Differential $dF_{p}$ *(from Differential Geometry)*
> Every smooth map $F : M \to N$ induces a linear map $dF_{p} : T_{p}M \to T_{F(p)}N$, the **differential** of $F$ at $p$. See [[Def - The Differential of a Smooth Map]]. The functoriality of $T_{p}$ is the content of the [[Thm - Chain Rule for the Differential|chain rule]].

> [!tip] Vector Fields *(from Differential Geometry)*
> A **vector field** on $M$ is a smooth section of the tangent bundle — equivalently, a smooth assignment of a tangent vector $X_{p} \in T_{p}M$ to each $p$. The space of vector fields $\Gamma(TM)$ is a module over $C^{\infty}(M)$ and carries the Lie bracket. All of dynamical systems on manifolds — flows, integral curves, ODEs — lives at this level. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]].

> [!tip] Riemannian Metric *(from Riemannian Geometry)*
> A **Riemannian metric** on $M$ is a smooth assignment to each $p$ of an inner product on $T_{p}M$. Without the tangent space construction, there would be no way to formulate this — the inner product needs $T_{p}M$ as its domain. Riemannian geometry is "differential geometry plus an inner product on each tangent space". See [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

> [!tip] Lie Algebra of a Lie Group *(from Lie Theory)*
> For a Lie group $G$, the tangent space at the identity $T_{e}G$ carries the **Lie bracket**, giving it the structure of a Lie algebra $\mathfrak{g}$. The bracket comes from the commutator of left-invariant vector fields and is the infinitesimal version of group commutation. The whole machinery of Lie theory — exponential map, Lie correspondence, classification — starts with the tangent space at one point. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

> [!tip] Cotangent Space *(from Differential Geometry)*
> The dual of $T_{p}M$, written $T^{*}_{p}M$, is the **cotangent space** at $p$. Its elements are linear functionals on tangent vectors — covectors, or 1-forms at $p$. The canonical covector associated to a smooth function $f$ is $df_{p}$, defined by $df_{p}(v) = v(f)$. The cotangent bundle $T^{*}M$ is the natural setting for Hamiltonian mechanics; see [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].
