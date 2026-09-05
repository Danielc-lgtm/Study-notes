---
type: topic
subject: differential-geometry
chapter: "3.1-3.4"
title: "Differential Geometry III — Tangent Vectors and the Differential"
tags: [geometry, differential-geometry]
---

# Notation Registry

Throughout this topic $M$ and $N$ are smooth manifolds (Hausdorff, second-countable, with a smooth structure in the sense of [[Def - Smooth Manifold]]), of dimensions $m$ and $n$ respectively. All maps between manifolds are smooth in the sense of [[Def - Smooth Map between Manifolds]] unless stated otherwise. We use the Einstein summation convention: a repeated index, once up and once down, is summed over its range; an upper index "in a denominator" counts as a lower index, so $\partial/\partial x^{i}$ has $i$ as a lower index, and $v^{i}\,\partial/\partial x^{i}$ is a sum.

- $p, q$ — points of a manifold; $p \in M$ usually
- $f, g$ — smooth real-valued functions on (an open subset of) $M$; the ring of all smooth functions on $M$ is $C^{\infty}(M)$, see [[Def - The Smooth Functions Ring]]
- $F : M \to N$ — a smooth map between manifolds
- $T_{p}M$ — the **tangent space** to $M$ at $p$, see [[Def - The Tangent Space]]
- $v, w$ — tangent vectors, elements of $T_{p}M$
- $v(f)$ or $vf$ — the action of a derivation $v \in T_{p}M$ on a function $f \in C^{\infty}(M)$, producing a real number
- $dF_{p} : T_{p}M \to T_{F(p)}N$ — the **differential** of $F$ at $p$, see [[Def - The Differential of a Smooth Map]]
- $dF : TM \to TN$ — the **global differential**, the union of the $dF_{p}$ over $p \in M$
- $(U, \varphi)$ — a [[Def - Coordinate Chart and Atlas|smooth chart]] on $M$; the components of $\varphi$ are the local coordinates $x^{1}, \dots, x^{m}$
- $\partial/\partial x^{i}|_{p}$ — the $i$-th **coordinate tangent vector** at $p$ associated with the chart $(U, \varphi)$, see [[Def - Coordinate Tangent Vectors]]
- $\gamma : J \to M$ — a smooth curve, where $J \subseteq \mathbb{R}$ is an interval
- $\gamma'(t_{0})$ or $\dot{\gamma}(t_{0})$ — the **velocity** of $\gamma$ at $t_{0}$, an element of $T_{\gamma(t_{0})}M$, see [[Def - Velocity of a Curve]]
- $TM = \bigsqcup_{p \in M} T_{p}M$ — the **tangent bundle**, see [[Def - The Tangent Bundle]]
- $\pi : TM \to M$, $(p, v) \mapsto p$ — the natural projection of the tangent bundle
- $D_{v}|_{a}$ — the directional-derivative operator at $a \in \mathbb{R}^{n}$ in the direction $v$: $D_{v}|_{a} f = \frac{d}{dt}\big|_{t=0} f(a + tv)$
- $\mathrm{GL}(n, \mathbb{R})$ — the general linear group of invertible $n \times n$ real matrices, an open subset of the vector space $M_{n}(\mathbb{R})$

A **standing convention** for this topic: every manifold is *finite-dimensional* and *smooth in the $C^{\infty}$ sense*. Lee's primary definition of $T_{p}M$ is **derivations of $C^{\infty}(M)$ at $p$**; we adopt this convention because it makes the vector-space structure transparent and gives coordinate-independent definitions of the differential, velocities, and the tangent bundle for free. Two other definitions (equivalence classes of curves; "geometric" tangent vectors paired with a chart) are introduced and proved equivalent — they are useful for different computations.

---

# Motivation

Here is the entire topic in one sentence: **a tangent vector at $p \in M$ is a first-order local linear operator on smooth functions**, and the assembly of all such operators is a finite-dimensional vector space $T_{p}M$ whose [[Def - Dimension|dimension]] equals the [[Def - Dimension|dimension]] of $M$. Everything in this chapter is the unpacking of that sentence.

The need is forced on us by the move from $\mathbb{R}^{n}$ to abstract manifolds. In Euclidean space, a "tangent vector at $a$" is just a vector in $\mathbb{R}^{n}$ with its tail attached at $a$ — the **geometric tangent vector**, see [[Def - The Tangent Space to a Submanifold]]. The same idea works for a submanifold of $\mathbb{R}^{n}$: a tangent vector to a sphere at the north pole is a vector in the ambient $\mathbb{R}^{3}$ that is orthogonal to the radius. But on an abstract manifold there is no ambient $\mathbb{R}^{N}$; there is only the manifold itself. We need a definition of tangent vector that uses *nothing but $M$ and the smooth functions on $M$*. That is the conceptual leap.

The way out, due to a long line of geometers, is to notice that even in $\mathbb{R}^{n}$ a tangent vector $v$ at $a$ is fully captured by what it does to functions: it produces the directional derivative
$$D_{v}|_{a} f \;=\; \frac{d}{dt}\bigg|_{t=0} f(a + tv) \;=\; v^{i}\, \frac{\partial f}{\partial x^{i}}(a).$$
Two different vectors give two different directional derivatives, so the map "vector $\mapsto$ directional-derivative operator" is injective; and every linear operator on $C^{\infty}(\mathbb{R}^{n})$ that satisfies the Leibniz product rule $D(fg) = f(a)\,Dg + g(a)\,Df$ turns out to be a directional derivative at $a$ for a unique $v$. So in $\mathbb{R}^{n}$, **vectors are derivations**. The right move on an abstract manifold is to *take that as the definition*: a tangent vector at $p$ is a linear map $v : C^{\infty}(M) \to \mathbb{R}$ satisfying the Leibniz rule at $p$. This is desideratum (i) of an abstract tangent space — no ambient space needed.

Two further perspectives compete for attention, and we will prove all three equivalent in [[Thm - Equivalence of Tangent Vector Definitions]]. The **curve picture** says a tangent vector is an equivalence class of smooth curves $\gamma$ through $p$, where two curves are equivalent if their compositions $f \circ \gamma$ have the same derivative at $0$ for every smooth $f$. The **chart picture** says a tangent vector is a tuple $(v^{1}, \dots, v^{n})$ that transforms by the Jacobian under change of chart. These three definitions are useful in different settings: the derivation picture makes the vector-space structure obvious and is the cleanest for proofs; the curve picture is what you reach for when computing; the chart picture is the physicist's working definition. The equivalence theorem is one of the foundational results of differential geometry, and it is the technical hinge of this chapter.

Once we have $T_{p}M$ as a vector space, the rest follows. A smooth map $F : M \to N$ induces a linear map $dF_{p} : T_{p}M \to T_{F(p)}N$, the **differential** of $F$ at $p$, defined by $(dF_{p}(v))(f) = v(f \circ F)$ — push the derivation through composition with $F$. The differential satisfies the chain rule $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ and the identity rule $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$, which is precisely the statement that $T_{p}$ is a *functor* from pointed smooth manifolds to vector spaces. In local coordinates the differential is represented by the Jacobian matrix of $F$ — so the manifold differential is the [[Def - The Total Derivative and Differentiability|total derivative]] of multivariate analysis, computed chart by chart and patched to be coordinate-independent. The Jacobian is the coordinate matrix of $df_{p}$ in coordinate bases; the coordinate-free $df_{p}$ is what the Jacobian was secretly all along.

Finally, gluing the tangent spaces $T_{p}M$ as $p$ varies produces the **tangent bundle** $TM = \bigsqcup_{p \in M} T_{p}M$, a smooth manifold of dimension $2 \dim M$ with a natural projection $\pi : TM \to M$. The tangent bundle is the natural home of vector fields, velocities of curves, and dynamical systems on $M$; it is the setting in which Lagrangian mechanics lives, and it is the first non-trivial example of a [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|vector bundle]]. The smoothness of the chart-induced trivializations is the content of [[Thm - The Tangent Bundle is a Smooth Manifold]].

The three definitions, the differential, the chain rule, the coordinate basis, the velocity of a curve, the tangent bundle — these are not seven disconnected things; they are seven faces of the same object. The point of this chapter is to make all seven faces visible and to prove they are the same face.

This topic assumes a working command of [[Differential Geometry I — Smooth Manifolds and Atlases|smooth manifolds]] and [[Differential Geometry II — Smooth Maps and Partitions of Unity|smooth maps and partitions of unity]] — in particular the chart-and-atlas formalism, smooth functions on a manifold, and the existence of bump functions. It also leans on the multivariate-analysis [[Def - The Total Derivative and Differentiability|total derivative]] as the local prototype and on [[Def - Vector Space|finite-dimensional vector spaces]] and [[Def - Linear Map|linear maps]] from linear algebra.

---

# Concept Map

## §3.1 Tangent Vectors as Derivations

- **[[Def - Derivation at a Point]]**
	- A **derivation at $p \in M$** is a linear map $v : C^{\infty}(M) \to \mathbb{R}$ that satisfies the Leibniz product rule $v(fg) = f(p)\,v(g) + g(p)\,v(f)$. The Leibniz rule is what makes the derivation "first-order": constants are annihilated, products of two functions vanishing at $p$ are annihilated, and only the first-order behaviour of $f$ at $p$ survives. The set of all derivations at $p$ is a real vector space under pointwise operations. On $\mathbb{R}^{n}$ every derivation at $a$ has the form $v^{i}\,\partial/\partial x^{i}|_{a}$ for a unique tuple $(v^{1}, \dots, v^{n})$ — so derivations and geometric vectors coincide on Euclidean space.

- **[[Def - The Tangent Space]]**
	- The **tangent space** $T_{p}M$ is the real vector space of derivations of $C^{\infty}(M)$ at $p$. Its elements are called **tangent vectors at $p$**. A reader can equally well think of an element of $T_{p}M$ as an equivalence class of smooth curves through $p$ or as a Jacobian-transforming tuple under change of chart — these definitions are equivalent (see [[Thm - Equivalence of Tangent Vector Definitions]]). The dimension of $T_{p}M$ equals the dimension of $M$, and the assignment $(M, p) \mapsto T_{p}M$, $F \mapsto dF_{p}$ is a covariant functor from pointed smooth manifolds to vector spaces.

- **[[Def - Tangent Vector via Equivalence Classes of Curves]]**
	- Two smooth curves $\gamma_{1}, \gamma_{2}$ with $\gamma_{i}(0) = p$ are **equivalent** if $(f \circ \gamma_{1})'(0) = (f \circ \gamma_{2})'(0)$ for every smooth $f$ defined near $p$ — they "have the same velocity at $p$". A **tangent vector at $p$** in this picture is an equivalence class $[\gamma]$. This is the geometrically intuitive definition: a tangent vector is a velocity, and equivalent curves trace the same instantaneous motion at $p$. The drawback is that the vector-space structure is not obvious — adding two equivalence classes requires picking representatives carefully — which is why the derivation definition is the default.

- **[[Thm - Equivalence of Tangent Vector Definitions]]**
	- The three definitions — derivations of $C^{\infty}(M)$ at $p$, equivalence classes of curves through $p$, and geometric tangent vectors in a chart — yield naturally isomorphic vector spaces. The isomorphism from curves to derivations sends $[\gamma]$ to the derivation $f \mapsto (f \circ \gamma)'(0)$; the isomorphism from a chart $(U, \varphi)$ to derivations sends $(v^{1}, \dots, v^{n})$ to $v^{i}\,\partial/\partial x^{i}|_{p}$. The equivalence is the technical hinge of this chapter — it lets us switch between pictures depending on what is convenient.

- **[[Thm - Dimension of the Tangent Space]]**
	- For an $n$-dimensional smooth manifold $M$ and any $p \in M$, the tangent space $T_{p}M$ is an $n$-dimensional real vector space. The proof uses any chart $(U, \varphi)$ around $p$ together with the local nature of derivations: a derivation $v$ is determined by its values on a small neighbourhood of $p$, so $T_{p}M \cong T_{p}U \cong T_{\varphi(p)}\mathbb{R}^{n}$, and the last space is $n$-dimensional with basis $\partial/\partial x^{i}|_{\varphi(p)}$. The corollary is that *every* tangent space, at every point of every $n$-manifold, looks the same as a vector space.

> [!tip] Unlocked: [[Def - The Lie Algebra of a Lie Group|Lie Algebra of a Lie Group]] *(from Lie Theory)*
> For a [[Def - Group|group]] $G$ that is also a smooth manifold with smooth multiplication and inversion (a **Lie group** — to be developed in [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]]), the tangent space $T_{e}G$ at the identity carries an extra structure, the **Lie bracket**, making it a **Lie algebra** $\mathfrak{g}$. The bracket on $\mathfrak{g}$ comes from the commutator of left-invariant vector fields; it is the infinitesimal version of group commutators. The exponential map $\exp : \mathfrak{g} \to G$ then re-inflates the infinitesimal structure into the group. The whole machine starts with the tangent space at one point.

> [!tip] Cotangent Space *(from Differential Geometry)*
> The dual of $T_{p}M$ is the **cotangent space** $T^{*}_{p}M$, see [[Def - Dual Space]] for the linear-algebra prototype. Its elements are linear functionals on tangent vectors — covectors, or 1-forms at $p$. The canonical 1-form on $T^{*}_{p}M$ is $df_{p}$, the differential of $f$ at $p$ viewed as a covector, since $df_{p}(v) = v(f)$ pairs tangent vectors against functions. The cotangent bundle $T^{*}M$ will be developed in [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]] and is the natural setting for Hamiltonian mechanics.

> [!note] Exercise Index — §3.1
> [[Exercise Index - §3.1 Tangent Vectors as Derivations]]

## §3.2 The Differential of a Smooth Map

- **[[Def - The Differential of a Smooth Map]]**
	- Given a smooth map $F : M \to N$ and a point $p \in M$, the **differential** of $F$ at $p$ is the linear map $dF_{p} : T_{p}M \to T_{F(p)}N$ defined by $(dF_{p}(v))(f) = v(f \circ F)$ for $v \in T_{p}M$ and $f \in C^{\infty}(N)$. The recipe is: take a derivation at $p$, push it forward by pre-composition with $F$, and you get a derivation at $F(p)$. In local coordinates the matrix of $dF_{p}$ relative to the coordinate bases is the Jacobian matrix of $F$, so $dF_{p}$ is the coordinate-free incarnation of the [[Def - The Total Derivative and Differentiability|total derivative]].

- **[[Thm - Chain Rule for the Differential]]**
	- For smooth maps $F : M \to N$ and $G : N \to P$ and any $p \in M$, $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$, and $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$. These two identities are exactly the statement that $T_{p}$ is a **covariant functor** from the category of pointed smooth manifolds to the category of real vector spaces. As a corollary, if $F$ is a [[Def - Diffeomorphism|diffeomorphism]] then $dF_{p}$ is a vector-space isomorphism for every $p$, with $(dF_{p})^{-1} = d(F^{-1})_{F(p)}$.

- **[[Ex - The Differential is Linear and Functorial]]** (⭐)
	- Verify directly from the definition $(dF_{p}(v))(f) = v(f \circ F)$ that $dF_{p}$ is linear, that the chain rule holds, and that the differential of the identity is the identity. A routine but foundational unwinding.

- **[[Ex - The Differential of a Diffeomorphism is an Isomorphism]]** (⭐)
	- Using the chain rule, show that if $F : M \to N$ is a [[Def - Diffeomorphism|diffeomorphism]] then $dF_{p} : T_{p}M \to T_{F(p)}N$ is a linear isomorphism, with inverse $d(F^{-1})_{F(p)}$. Conclude that diffeomorphic manifolds have the same dimension.

- **[[Ex - Computing the Differential in Local Coordinates]]** (⭐⭐)
	- Given a smooth map $F : M \to N$ between manifolds with charts $(U, \varphi)$ and $(V, \psi)$, derive the formula $dF_{p}(\partial/\partial x^{i}|_{p}) = (\partial \hat{F}^{j}/\partial x^{i})(\hat{p})\, \partial/\partial y^{j}|_{F(p)}$ where $\hat{F} = \psi \circ F \circ \varphi^{-1}$ is the coordinate representative. The Jacobian appears as the matrix of $dF_{p}$.

> [!tip] Unlocked: [[Def - Rank of a Smooth Map|Rank of a Smooth Map]] *(from Differential Geometry)*
> The **rank** of $F$ at $p$ is the rank of the linear map $dF_{p}$. Constant-rank maps fall into three classes — submersions ($dF_{p}$ surjective), immersions ($dF_{p}$ injective), and embeddings (injective immersions that are [[Def - Homeomorphism|homeomorphisms]] onto their images) — and the [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|rank theorem]] gives a local normal form for each. The differential is the algebraic shadow that controls all of submanifold theory.

> [!note] Exercise Index — §3.2
> [[Exercise Index - §3.2 The Differential of a Smooth Map]]

## §3.3 Computations in Coordinates

- **[[Def - Coordinate Tangent Vectors]]**
	- Given a smooth chart $(U, \varphi)$ with coordinates $x^{1}, \dots, x^{n}$ around $p \in M$, the **$i$-th coordinate tangent vector at $p$** is the derivation $\partial/\partial x^{i}|_{p}$ defined by $(\partial/\partial x^{i}|_{p})(f) = (\partial \hat{f}/\partial x^{i})(\varphi(p))$, where $\hat{f} = f \circ \varphi^{-1}$ is the coordinate representative of $f$. These $n$ derivations form a basis for $T_{p}M$ — the **coordinate basis** induced by the chart. Every $v \in T_{p}M$ has a unique expansion $v = v^{i}\,\partial/\partial x^{i}|_{p}$ where the components are $v^{i} = v(x^{i})$, applying $v$ to the $i$-th coordinate function as a smooth real-valued function.

- **[[Def - Velocity of a Curve]]**
	- For a smooth curve $\gamma : J \to M$ defined on an interval $J \subseteq \mathbb{R}$ and a point $t_{0} \in J$, the **velocity** of $\gamma$ at $t_{0}$ is the tangent vector $\gamma'(t_{0}) = d\gamma_{t_{0}}(d/dt|_{t_{0}}) \in T_{\gamma(t_{0})}M$. Concretely, $\gamma'(t_{0})$ is the derivation that sends $f$ to $(f \circ \gamma)'(t_{0})$ — the rate of change of $f$ along $\gamma$ at time $t_{0}$. In any chart, the coordinate components of $\gamma'(t_{0})$ are the derivatives of the component functions of $\gamma$. Every tangent vector at $p$ arises as the velocity of some smooth curve through $p$.

- **[[Ex - Tangent Vectors as Velocities of Coordinate Curves]]** (⭐)
	- For a chart $(U, \varphi)$ around $p$, define the $i$-th coordinate curve $\gamma_{i}(t) = \varphi^{-1}(\varphi(p) + t\,e_{i})$. Show that $\gamma_{i}'(0) = \partial/\partial x^{i}|_{p}$. This grounds the abstract coordinate vector in a literal curve along the $i$-th coordinate axis.

- **[[Ex - Tangent Space to a Sphere at the North Pole]]** (⭐⭐)
	- Compute $T_{N}S^{2}$ where $N = (0, 0, 1)$ is the north pole, using stereographic-projection coordinates from $N$. Show that the coordinate basis at $N$ consists of two tangent vectors, and identify them with two specific elements of $\mathbb{R}^{3}$ orthogonal to the radius — recovering the geometric tangent space [[Def - The Tangent Space to a Submanifold|to the embedded sphere]].

> [!tip] Unlocked: Tensor Field in Local Coordinates *(from Differential Geometry)*
> Once you have the coordinate basis $\partial/\partial x^{i}$ for $T_{p}M$ and its dual $dx^{i}$ for $T^{*}_{p}M$ (see [[Def - Dual Basis]]), every **tensor field** on $M$ acquires local coordinate components — a $(p,q)$-tensor field is a smooth assignment of multilinear functions, written in coordinates as $T^{i_{1}\dots i_{p}}_{j_{1}\dots j_{q}}\,\partial/\partial x^{i_{1}} \otimes \dots \otimes dx^{j_{q}}$. The change-of-chart formula for tensor components — the famous "transformation law" — is the same Jacobian rule that governs tangent vectors, applied repeatedly. [[Differential Geometry VII — Tensors and Tensor Fields]] develops this.

> [!note] Exercise Index — §3.3
> [[Exercise Index - §3.3 Computations in Coordinates]]

## §3.4 The Tangent Bundle

- **[[Def - The Tangent Bundle]]**
	- The **tangent bundle** of a smooth $n$-manifold $M$ is the disjoint union $TM = \bigsqcup_{p \in M} T_{p}M$, together with the natural projection $\pi : TM \to M$ sending $(p, v)$ to $p$. Each fibre $\pi^{-1}(p) = T_{p}M$ is a real vector space of dimension $n$. The total space $TM$ inherits a topology and a smooth structure that make it into a $2n$-dimensional smooth manifold (see [[Thm - The Tangent Bundle is a Smooth Manifold]]). $TM$ is the natural home of vector fields (smooth sections of $\pi$), of velocities of curves on $M$, and of Lagrangian mechanics — the configuration manifold's velocities live in $TM$.

- **[[Thm - The Tangent Bundle is a Smooth Manifold]]**
	- For any smooth $n$-manifold $M$, the disjoint union $TM = \bigsqcup_{p \in M} T_{p}M$ admits a natural topology and smooth structure making it a $2n$-dimensional smooth manifold. The smooth structure is built from the **natural charts**: each chart $(U, \varphi)$ on $M$ with coordinates $x^{i}$ induces a chart $(\pi^{-1}(U), \tilde\varphi)$ on $TM$ with coordinates $(x^{i}, v^{i})$, where $v^{i}$ are the components of the tangent vector in the coordinate basis. Transition functions are smooth — the position part is the original transition, the velocity part is the Jacobian acting linearly on the fibre. With this structure $\pi$ is smooth.

- **[[Thm - Tangent Space of a Product Manifold]]**
	- For smooth manifolds $M_{1}, \dots, M_{k}$ and a point $p = (p_{1}, \dots, p_{k}) \in M_{1} \times \cdots \times M_{k}$, the map $v \mapsto (d\pi_{1,p}(v), \dots, d\pi_{k,p}(v))$ is a canonical vector-space isomorphism $T_{p}(M_{1} \times \cdots \times M_{k}) \cong T_{p_{1}}M_{1} \oplus \cdots \oplus T_{p_{k}}M_{k}$. The tangent space of a product is the [[Def - Direct Sum|direct sum]] of the factor tangent spaces — products and tangent spaces commute with each other.

- **[[Ex - Tangent Space of the General Linear Group at the Identity]]** (⭐⭐)
	- Compute $T_{I}\mathrm{GL}(n, \mathbb{R})$. Since $\mathrm{GL}(n, \mathbb{R})$ is an open subset of the vector space $M_{n}(\mathbb{R})$ of all $n \times n$ matrices, its tangent space at any point is canonically identified with $M_{n}(\mathbb{R})$ itself. This preview of the Lie algebra $\mathfrak{gl}(n, \mathbb{R}) = M_{n}(\mathbb{R})$ shows the tangent space at the identity of a matrix Lie group is just the matrices.

> [!tip] Unlocked: Vector Field as a Section of TM *(from Differential Geometry)*
> A **vector field** on $M$ is a smooth section of the tangent bundle — a smooth map $X : M \to TM$ with $\pi \circ X = \mathrm{id}_{M}$, so $X$ assigns to each $p \in M$ a tangent vector $X_{p} \in T_{p}M$ smoothly. The space of vector fields is denoted $\Gamma(TM)$ and is a [[Def - Module|module]] over $C^{\infty}(M)$. The flows of vector fields are the dynamical systems on $M$; their Lie bracket measures the failure of two flows to commute. All of this is developed in [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]].

> [!tip] Unlocked: [[Def - Riemannian Metric|Riemannian Metric]] *(from Riemannian Geometry)*
> A **Riemannian metric** on $M$ is a smooth assignment to each $p \in M$ of an [[Def - Inner Product Space|inner product]] on the tangent space $T_{p}M$. Without the tangent bundle this would be impossible to formulate — the inner product needs the tangent spaces, and the smoothness needs them glued into a manifold. A Riemannian metric promotes $M$ from a bare smooth manifold to a metric space with a notion of length, angle, [[Def - Geodesic|geodesic]], and curvature. Riemannian and Lorentzian metrics are the topic of [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

> [!note] Exercise Index — §3.4
> [[Exercise Index - §3.4 The Tangent Bundle]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The recurring goals of exercises in this topic are five. The first is **computing $T_{p}M$ at a specific point**: given a manifold and a point, identify the tangent space as a familiar vector space, usually by finding a chart and reading off the coordinate basis or by realizing the manifold as a submanifold and identifying tangent vectors with velocities of curves. The second is **computing the differential $dF_{p}$ of a given map**: again chart-based, the answer is a Jacobian matrix, but the cleanest computation often uses Corollary 3.25 (the differential is computed by feeding it a curve). The third is **proving linearity, functoriality, or coordinate-independence**: routine verifications that the differential respects composition, that two definitions agree, that a construction is invariant under change of chart. The fourth is **identifying a tangent space at a special point** — at the identity of a Lie group it is the Lie algebra; at the origin of a vector space it is the vector space itself; at a critical point of a function it is where the Hessian lives. The fifth is **building or characterizing the tangent bundle** — verifying its smooth structure, showing a tangent bundle is trivial (or proving it is not), and identifying $TM \cong M \times \mathbb{R}^{n}$ for parallelizable manifolds.

**Sources — what assumptions do we usually leverage?**

The recurring inputs are equally stereotyped. **A chart at $p$** is given, immediately handing over the coordinate basis $\partial/\partial x^{i}|_{p}$ — this is the workhorse, because every concrete computation runs in a chart. **A smooth curve $\gamma$ with $\gamma(0) = p$** is given (or constructed), letting one compute $\gamma'(0)$ as a tangent vector and use Corollary 3.25 to push it through a map: $dF_{p}(\gamma'(0)) = (F \circ \gamma)'(0)$. **A defining equation $f = c$** for a submanifold is given, so tangent vectors at a regular point are exactly $\ker df_{p}$ — this is the bridge from [[Def - The Tangent Space to a Submanifold|the embedded submanifold definition]] to the abstract one. **A diffeomorphism $F$** is given, so $dF_{p}$ is automatically an isomorphism — the chain rule does the work. **A product structure** $M = M_{1} \times M_{2}$ is given, so tangent spaces split as direct sums via [[Thm - Tangent Space of a Product Manifold]]. The recurring routing is: "given a chart, find the coordinate basis"; "given a curve, take its velocity and feed it to $dF$"; "given a defining equation, take the kernel of the differential"; "given a diffeomorphism, transport tangent vectors and the operations they support". The whole game of this topic is choosing which of these sources to leverage and which target to aim for.

---

# Legal Operations

These are the operational moves that almost every exercise in this topic uses. Each is self-contained — a reader can scan the list when stuck and try each in turn.

**Legal operations:**

1. **Compute $dF_{p}(v)$ via a curve.** Given $v \in T_{p}M$, pick any smooth curve $\gamma$ with $\gamma(0) = p$ and $\gamma'(0) = v$ — such a curve exists by [[Def - Velocity of a Curve|the surjectivity of velocity]]. Then $dF_{p}(v) = (F \circ \gamma)'(0)$. *Trigger:* you need to evaluate $dF_{p}$ at a vector and the local coordinate computation is awkward. *Pattern:* the curve does not have to be specially adapted to $F$ — any curve with the right velocity will do, because $dF_{p}$ depends only on $v$, not on which curve realizes it.

2. **Read off coordinate components.** A tangent vector $v \in T_{p}M$ in a chart $(U, x^{1}, \dots, x^{n})$ has unique components $v^{i} = v(x^{i})$, so $v = v^{i}\,\partial/\partial x^{i}|_{p}$. *Trigger:* you need a basis-expansion of $v$ for a concrete formula. *Pattern:* feed $v$ to the coordinate functions one at a time; the outputs are the components.

3. **Push a coordinate basis through $dF_{p}$ to get the Jacobian.** Apply $dF_{p}$ to each $\partial/\partial x^{i}|_{p}$ and expand in the codomain coordinate basis: $dF_{p}(\partial/\partial x^{i}|_{p}) = (\partial \hat{F}^{j}/\partial x^{i})(\hat{p})\,\partial/\partial y^{j}|_{F(p)}$, where $\hat{F} = \psi \circ F \circ \varphi^{-1}$. *Trigger:* you need the matrix of $dF_{p}$. *Pattern:* the matrix's $(j, i)$ entry is the partial derivative of the $j$-th component of $\hat{F}$ with respect to the $i$-th input coordinate.

4. **Recognize an open submanifold and identify tangent spaces.** If $U \subseteq M$ is open and $p \in U$, the inclusion's differential $T_{p}U \to T_{p}M$ is an isomorphism — open submanifolds "see the same tangent space" as the ambient manifold. *Trigger:* you have a manifold defined as an open subset of a larger one (e.g., $\mathrm{GL}(n) \subset M_{n}(\mathbb{R})$). *Pattern:* tangent vectors at $p \in U$ are tangent vectors at $p \in M$ — no extra work.

5. **Use the chain rule to transport tangent vectors across a diffeomorphism.** If $F : M \to N$ is a diffeomorphism, $dF_{p} : T_{p}M \to T_{F(p)}N$ is an isomorphism. *Trigger:* you want to identify $T_{p}M$ with a more familiar space and have a diffeomorphism handy. *Pattern:* find any diffeomorphism (a chart $\varphi : U \to \hat{U} \subseteq \mathbb{R}^{n}$ counts), push tangent vectors through it, and read off the structure on the other side.

6. **Compute the tangent space to a level set as $\ker df_{p}$.** If $M = \{f = c\}$ is a regular level set, then $T_{p}M = \ker df_{p} \subseteq T_{p}\mathbb{R}^{N}$. This works once the [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|regular value theorem]] is in hand, but the idea — that a tangent vector to a level set must be killed by the differential of the defining function — is already a legal move. *Trigger:* a manifold is given as the zero set of a smooth function with surjective differential. *Pattern:* differentiate the defining condition $f(\gamma(t)) = c$ at $t = 0$ to get $df_{p}(\gamma'(0)) = 0$.

7. **Split the tangent space of a product.** For $p = (p_{1}, p_{2}) \in M_{1} \times M_{2}$, $T_{p}(M_{1} \times M_{2}) \cong T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}$ canonically via the projections (see [[Thm - Tangent Space of a Product Manifold]]). *Trigger:* a tangent vector on a product manifold needs to be analyzed component by component. *Pattern:* project to each factor with $d\pi_{i}$; assemble the pieces with the direct-sum isomorphism.

8. **Identify $T_{a}V$ with $V$ for a vector space.** When $V$ is a finite-dimensional vector space treated as a smooth manifold, there is a canonical isomorphism $V \cong T_{a}V$ sending $v$ to the derivation $D_{v}|_{a}$, $f \mapsto (d/dt)|_{0} f(a + tv)$. *Trigger:* the manifold is itself a vector space (or an open subset of one). *Pattern:* tangent vectors at any point are just elements of the vector space — no further work.

9. **Express the velocity of a curve in coordinates.** In a chart with coordinates $x^{i}$, if $\gamma(t) = (\gamma^{1}(t), \dots, \gamma^{n}(t))$, then $\gamma'(t_{0}) = (d\gamma^{i}/dt)(t_{0})\,\partial/\partial x^{i}|_{\gamma(t_{0})}$. *Trigger:* you have a curve in coordinates and need its velocity vector. *Pattern:* differentiate each component function and pair with the corresponding coordinate basis vector.

10. **Use functoriality to derive that diffeomorphic manifolds have isomorphic tangent spaces at corresponding points.** From $dF_{p} \circ d(F^{-1})_{F(p)} = \mathrm{id}$ and the chain rule, $dF_{p}$ is an isomorphism for any diffeomorphism. *Trigger:* you need to transfer a tangent-space construction from one manifold to a diffeomorphic one. *Pattern:* push tangent vectors through the diffeomorphism's differential — the operations transfer for free because $T_{p}$ is a functor.

**Illegal but tempting operations:**

> [!warning] 1. Treating a tangent vector as an element of $\mathbb{R}^{n}$ without specifying a chart
> A tangent vector $v \in T_{p}M$ has *no canonical components* — it has components only after a chart is chosen. Writing "$v = (1, 0, 0)$" with no chart attached is meaningless: under a different chart the same $v$ has different components, related by the Jacobian of the transition map. The counterexample is the equator-pointing tangent vector at $(1, 0, 0) \in S^{2}$: in spherical coordinates it has components $(\partial/\partial \theta)|_{p}$, but in stereographic-projection coordinates from the north pole the same vector has components mixing both $\partial/\partial u$ and $\partial/\partial v$. The repair: always state which chart the components refer to, and use the [[Def - Coordinate Tangent Vectors|change-of-chart formula]] to convert.

> [!warning] 2. Adding tangent vectors at different points
> If $v \in T_{p}M$ and $w \in T_{q}M$ with $p \neq q$, the sum $v + w$ is **not defined** — they live in different vector spaces, and there is no canonical way to identify $T_{p}M$ with $T_{q}M$. The counterexample is $M = S^{2}$: a tangent vector at the north pole and a tangent vector at the south pole cannot be added, since the spheres' tangent planes there are different planes in different ambient locations. The repair: to compare tangent vectors at different points you need a **connection** (Levi-Civita, in the Riemannian case) and **parallel transport** along a curve — this is the central insight that makes Riemannian geometry nontrivial. Without a connection, there is no canonical "subtraction of tangent vectors at distinct points", which is why the curvature tensor exists at all.

> [!warning] 3. Assuming $TM \cong M \times \mathbb{R}^{n}$ for every manifold
> Locally, the tangent bundle does look like a product — every chart $(U, \varphi)$ gives a diffeomorphism $\pi^{-1}(U) \cong U \times \mathbb{R}^{n}$. Globally this **almost never works**. The counterexample is the 2-sphere $S^{2}$: by the hairy-ball theorem, every continuous vector field on $S^{2}$ vanishes somewhere, so $TS^{2}$ has no nowhere-zero global section, which means $TS^{2}$ cannot be globally diffeomorphic to $S^{2} \times \mathbb{R}^{2}$ (the latter does admit such a section, namely a constant vector). The repair: $TM \cong M \times \mathbb{R}^{n}$ holds exactly when $M$ is **parallelizable**, e.g., the circle, the torus, Lie [[Def - Group|groups]], and $\mathbb{R}^{n}$ itself; spheres other than $S^{1}, S^{3}, S^{7}$ are not parallelizable.

> [!warning] 4. Identifying tangent vectors with their values on coordinate functions only
> A derivation is a linear map on **all** of $C^{\infty}(M)$, satisfying the Leibniz rule. It is tempting to define a tangent vector by specifying only its values on coordinate functions — and this *does* determine the derivation by linearity and the local nature of derivations — but the construction must be verified to extend consistently to all smooth functions. The counterexample comes from operators that are linear on polynomials but fail the Leibniz rule: $v(f) = f(p) + f'(p)$ would be linear and behave fine on $x^{i}$, but it does not satisfy $v(fg) = f(p)v(g) + g(p)v(f)$. The repair: when defining a tangent vector by its values on a generating set, **check the Leibniz rule** on a product of two non-coordinate functions before declaring it a derivation.

---

# Problem-Solving Strategy

The exercises in this topic split into a small number of recognizable types, and the cost of solving them is paid up front by deciding which type you are looking at. The five types are: compute a specific $T_{p}M$, compute a specific $dF_{p}$, verify an abstract property (linearity, functoriality, coordinate-independence), identify a tangent space at a special point, and reason about the tangent bundle's smooth structure.

When a problem **asks you to compute $T_{p}M$ at a specific $p$**, the productive first move is to **find a chart at $p$**. Any chart suffices — the coordinate basis $\partial/\partial x^{i}|_{p}$ is a basis for $T_{p}M$ no matter which chart. If the manifold is given by a defining equation $f = c$ and you have ambient coordinates, the level-set description $T_{p}M = \ker df_{p}$ is often more efficient. If the manifold is a product, split via [[Thm - Tangent Space of a Product Manifold]]. If the manifold is an open subset of a vector space, identify $T_{p}M$ with the vector space directly. The order of preference is: open-of-vector-space (free), product (split), level set (one differential), chart (always works). The strategy is to **pick the easiest of these representations** before computing.

When a problem **asks you to compute $dF_{p}$ at a specific $v$**, the productive first move is to ask whether you have a curve handy with $\gamma'(0) = v$. If you do — and you usually do, because building one in a chart is $\gamma(t) = \varphi^{-1}(\varphi(p) + tv)$ — then $dF_{p}(v) = (F \circ \gamma)'(0)$ by Corollary 3.25, and you compute the right side by differentiating a function of one real variable. This is almost always faster than expanding $dF_{p}$ in a coordinate basis, especially when $F$ is given by a clever formula rather than an explicit coordinate expression. The Jacobian-matrix approach (legal operation 3) is the alternative — necessary when you want the *full* matrix and not just one column. The decision point is: do I need one vector's image or the whole linear map?

When a problem **asks you to verify functoriality, linearity, or coordinate-independence**, the strategy is to unwind definitions and apply the chain rule. These problems are usually routine but expose where the abstract definitions hide their power. The single most useful trick is *not* to compute in coordinates: the derivation definition handles linearity and functoriality directly, with no Jacobians, and a coordinate computation is genuinely longer.

When a problem **asks you to identify $T_{p}M$ at a special point** — the identity of a Lie group, the origin of a vector space, a critical point of a function — the strategy is to use any extra structure at that point. At the identity of $\mathrm{GL}(n)$, the manifold is open in $M_{n}(\mathbb{R})$, so $T_{I}\mathrm{GL}(n) \cong M_{n}(\mathbb{R})$. At a regular point of $f^{-1}(c)$, the tangent space is $\ker df_{p}$. At a critical point of a real-valued function, the tangent space is the natural setting for the [[Def - Critical Point, Hessian, and Definiteness|Hessian]]. The special points are special because the structure at them is more explicit, not because the tangent-space construction is different.

When a problem **asks about the tangent bundle's smooth structure**, the strategy is always to use the natural charts $(\pi^{-1}(U), \tilde\varphi)$ from a chart $(U, \varphi)$ on $M$. The transition functions are the original transition together with its Jacobian acting linearly on the fibre. Everything about $TM$ — smoothness of $\pi$, smoothness of $dF$, the chart-induced trivialization $\pi^{-1}(U) \cong U \times \mathbb{R}^{n}$ — reduces to verifying smoothness of these transition functions, which is in turn the chain rule.

The meta-strategy threading through all of this: **every question in this chapter is the question "what is the linearization of this object at $p$?"**. Tangent vectors are linearizations of curves; the differential is the linearization of a map; the tangent space is the linearized version of the manifold near $p$; the tangent bundle is the global assembly of all these linearizations. When stuck, ask: "what is the linear object behind this nonlinear setup, and how does it look in a coordinate chart?"

---

# Most Reusable Properties

- **[[Thm - Equivalence of Tangent Vector Definitions|Equivalence of Tangent Vector Definitions]]**: derivations ≅ equivalence classes of curves ≅ chart-tuples. This is the most reusable single fact in the chapter because it licenses switching between pictures depending on which makes the problem easier. The derivation picture is what you prove with (linearity, functoriality are obvious); the curve picture is what you compute with (just differentiate $f \circ \gamma$); the chart picture is what you write down on paper (components and matrices). A reader fluent in the equivalence solves problems faster because they pick the right picture for each piece of the argument.

- **Corollary 3.25 — Computing the differential via a curve.** $dF_{p}(v) = (F \circ \gamma)'(0)$ for any curve $\gamma$ with $\gamma(0) = p$, $\gamma'(0) = v$. This is the workhorse for evaluating differentials, especially when $F$ has no explicit coordinate formula or has a clever non-coordinate form. The typical use: you are told $F$ via some construction (matrix multiplication, complex exponentiation, polynomial substitution), you build a curve in $M$, you compose with $F$, and you differentiate at $t = 0$ — no charts needed.

- **[[Thm - Chain Rule for the Differential|Chain Rule for the Differential]]**: $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$. This is the linearization of composition and is the engine behind functoriality. The typical use is to break a complicated map into a chain of simpler ones and compute the differential as a product of Jacobian matrices. The other reusable consequence is that [[Def - Diffeomorphism|diffeomorphisms]] have isomorphic differentials, since $dF \circ d(F^{-1}) = d(\mathrm{id}) = \mathrm{id}$.

- **The Jacobian as the coordinate matrix of $dF_{p}$.** In a chart, $dF_{p}(\partial/\partial x^{i}|_{p}) = (\partial \hat{F}^{j}/\partial x^{i})(\hat{p})\,\partial/\partial y^{j}|_{F(p)}$. This identifies the abstract manifold differential with the concrete Jacobian matrix from multivariate calculus — see [[Def - Partial Derivatives and the Jacobian Matrix]]. The typical use is to pass from coordinate-free statements about $dF$ to explicit numerical computations in a chart, and back.

- **Tangent space of an open subset of a vector space is the vector space.** For $V$ a finite-dimensional vector space and $U \subseteq V$ open, $T_{p}U \cong V$ canonically for every $p$. The typical use is computing tangent spaces of matrix [[Def - Group|groups]] and other vector-space-based manifolds: $T_{I}\mathrm{GL}(n) = M_{n}(\mathbb{R})$, $T_{p}\mathbb{R}^{n} = \mathbb{R}^{n}$, $T_{p}(V \setminus \{0\}) = V$. This is the cheapest tangent-space computation there is.

---

# Bridges

1. **Multivariate analysis — the manifold differential is the chart-by-chart total derivative.** The differential $dF_{p}$ between tangent spaces of manifolds is *literally* the [[Def - The Total Derivative and Differentiability|total derivative]] computed in any chart and lifted to be coordinate-independent. Concretely, if $(U, \varphi)$ is a chart on $M$ around $p$ and $(V, \psi)$ is a chart on $N$ around $F(p)$, the coordinate representative $\hat{F} = \psi \circ F \circ \varphi^{-1}$ is a smooth map between open subsets of Euclidean space, with a total derivative $D\hat{F}_{\varphi(p)} : \mathbb{R}^{m} \to \mathbb{R}^{n}$. After identifying $T_{p}M$ with $T_{\varphi(p)}\mathbb{R}^{m} \cong \mathbb{R}^{m}$ via the chart, $dF_{p}$ *is* $D\hat{F}_{\varphi(p)}$. The Jacobian matrix from [[Def - Partial Derivatives and the Jacobian Matrix]] is the coordinate matrix of $dF_{p}$ in coordinate bases. The conceptual content of the manifold construction is precisely that this Jacobian transforms correctly under change of chart — which is the chain rule for total derivatives.

2. **Submanifolds of Euclidean space — abstract $T_{p}M$ becomes concrete $T_{p}M \subset \mathbb{R}^{N}$.** When $M$ sits inside $\mathbb{R}^{N}$ as a [[Def - Submanifold of Euclidean Space|submanifold]], the abstract tangent space $T_{p}M$ defined here can be identified with the concrete subspace [[Def - The Tangent Space to a Submanifold|TₚM ⊂ ℝᴺ]] consisting of velocities $\gamma'(0)$ of curves in $M$. The identification is via the inclusion $\iota : M \hookrightarrow \mathbb{R}^{N}$: $d\iota_{p}$ sends an abstract tangent vector to its concrete representative in $\mathbb{R}^{N}$. This bridge is what makes the sphere example concrete: the abstract $T_{N}S^{2}$ is a 2-dimensional space; via the inclusion of $S^{2}$ into $\mathbb{R}^{3}$, it becomes the horizontal plane at the north pole, $\{v \in \mathbb{R}^{3} : v_{3} = 0\}$.

3. **Linear algebra — every tangent space is a finite-dimensional vector space, and operations on linear maps lift.** The tangent space $T_{p}M$ is an $n$-dimensional [[Def - Vector Space|real vector space]], and the differential $dF_{p}$ is a [[Def - Linear Map|linear map]] between tangent spaces. Every theorem of finite-dimensional linear algebra — choice of basis, rank-nullity, change of basis matrix — applies pointwise to tangent spaces. The [[Def - Rank of a Linear Map|rank]] of $dF_{p}$ is the local rank of $F$, and the constant-rank theorem (next topic) is the manifold version of [[Thm - Continuous Image of a Compact Space|the structure theorem for linear maps]]. The change-of-chart formula for tangent vectors is the [[Def - Change of Basis Matrix|change-of-basis matrix]] applied fibrewise.

4. **Category theory — $T_{p}$ is a functor from pointed smooth manifolds to vector spaces.** The assignment $(M, p) \mapsto T_{p}M$ on pointed smooth manifolds, with morphism map $F \mapsto dF_{p}$, satisfies the two functor axioms: $d(\mathrm{id})_{p} = \mathrm{id}$ and $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$. This is the proper categorical content of the chain rule: tangent-space construction is a *covariant functor* $T : \mathrm{Diff}_{*} \to \mathrm{Vec}_{\mathbb{R}}$, where $\mathrm{Diff}_{*}$ is the category of pointed smooth manifolds and pointed smooth maps, and $\mathrm{Vec}_{\mathbb{R}}$ is the category of real vector spaces and linear maps. Similarly the global tangent bundle is a functor $T : \mathrm{Diff} \to \mathrm{Diff}$. Functoriality is what guarantees coordinate-independence: $T$ commutes with composition, so any computation in one chart agrees with the computation in another after change of chart.

5. **Topology — the tangent bundle has a natural manifold topology, distinct from the disjoint-union topology.** The tangent bundle $TM$ is the disjoint union $\bigsqcup_{p} T_{p}M$ as a set, but its natural topology is *not* the disjoint-union topology (which would make every fibre a connected component). The natural topology is induced by the charts $\tilde\varphi : \pi^{-1}(U) \to \hat{U} \times \mathbb{R}^{n}$ inherited from charts $(U, \varphi)$ on $M$. In this topology, $TM$ is connected (for $M$ connected), Hausdorff, and second-countable, and $\pi : TM \to M$ is a continuous surjection — in fact a smooth submersion. The manifold topology on $TM$ is what makes "smoothness of a vector field" a meaningful condition.

6. **Special relativity and general relativity — the tangent space is where four-velocities and four-momenta live.** In [[Def - Minkowski Space and the Metric|Minkowski space]] and curved spacetime, the four-velocity of a worldline is a tangent vector to the spacetime manifold at the event. The metric pairs tangent vectors to give the spacetime interval, lengths, and times. The distinction between an event $p$ (a point of spacetime) and a four-velocity $u \in T_{p}M$ (a tangent vector) is the same platonic-vs-representation distinction Lee makes here between $p \in M$ and $v \in T_{p}M$. Special relativity is the case where $M = \mathbb{R}^{4}$ and $T_{p}M \cong \mathbb{R}^{4}$ canonically, so the distinction is invisible; general relativity is the case where this identification fails globally.

---

# Insights

**The unifying frame: a tangent vector is the linearization of a curve at a point.** The textbook *definition* says a tangent vector is a derivation, but the *true name* is "the velocity of a curve through $p$". Every concrete tangent vector you will ever compute arises as $\gamma'(0)$ for some curve, and every derivation $v$ is realized as $\gamma'(0)$ for some $\gamma$ — the surjectivity of velocity is built into the proof of [[Thm - Equivalence of Tangent Vector Definitions]]. The derivation viewpoint is a clean *re-encoding* of the curve picture that makes the vector-space structure transparent (derivations add pointwise, whereas adding curve classes intrinsically requires first transporting the vector-space structure from the derivation model), but it is not the *picture* you should carry. Carry the picture of a curve passing through $p$, with $\gamma'(0)$ as its instantaneous velocity — the derivation is the recipe for differentiating any smooth function along that velocity.

**The true name of $dF_{p}$ is the Jacobian, made coordinate-independent.** The textbook *definition* says $dF_{p}(v) = (F \circ \gamma)'(0)$ or $(dF_{p}(v))(f) = v(f \circ F)$, and these are correct. But the *operational* statement is that in any chart, $dF_{p}$ is the Jacobian matrix of $F$ — and the *only* reason we use the abstract definition rather than the Jacobian is to make explicit that the answer does not depend on the chart. The deeper insight is that the manifold differential was *invented* to give the Jacobian a coordinate-free meaning. When computing, you write down a Jacobian; when proving, you use the abstract definition.

**Three definitions, one object — and the equivalence theorem is the technical heart of this chapter.** Differential geometry is unusual among mathematical subjects in offering *three different definitions* of its central object, all of which appear in standard textbooks. Each definition has a constituency: physicists prefer the chart-tuple definition because it matches how tensors appear in coordinates; geometers prefer the curve definition because it captures motion; algebraists (and Lee) prefer the derivation definition because it makes the vector-space structure and functoriality clean. The equivalence theorem is *not* a technicality — it is what allows the field to function. Without it, a paper using one definition would not connect to a paper using another. Internalizing the three pictures and their isomorphisms is the difference between fluency and stumbling.

**Manifold properties pull back to Euclidean space — but the patching is the content.** The slogan from the polymath insights collection — "manifold properties pull back to Euclidean space" — applies sharply here. The tangent space at $p$, viewed through any chart, is just $\mathbb{R}^{n}$ with its standard basis $\partial/\partial x^{i}$; the differential, viewed in coordinates, is the Jacobian; the velocity of a curve in coordinates is the tuple of component derivatives. So *all the local computations* are Euclidean computations. What the manifold adds is the *patching*: the fact that two charts give the same tangent space (via the Jacobian transition), the fact that two charts give the same differential, the fact that velocities transform correctly. The conceptual leap from $\mathbb{R}^{n}$ to a manifold is entirely contained in checking that the chart-by-chart computation is coordinate-independent — and the proof is always the chain rule.

**The tangent bundle is the first non-trivial vector bundle, and its non-triviality is geometric content.** Locally, $TM$ looks like $U \times \mathbb{R}^{n}$ — every chart gives a local trivialization. Globally, $TM$ is *rarely* a product. This non-triviality is the first concrete manifestation of topology in differential geometry: a 2-sphere's tangent bundle is not $S^{2} \times \mathbb{R}^{2}$ because there is no nowhere-zero vector field on $S^{2}$ (hairy ball theorem). The *measurement* of non-triviality is the subject of characteristic classes (Euler class, Chern class, Pontryagin class), which lie beyond this topic but begin here: $TM$ is trivial exactly when $M$ is parallelizable. Vanishing of the Euler class is a necessary obstruction test for an oriented even-rank bundle, but it is not sufficient for triviality; the remaining Stiefel–Whitney and Pontryagin classes, and sometimes finer invariants, may still obstruct a global frame. The simplest non-trivial vector bundle in the whole subject is $TS^{2}$, and one should hold it in mind as the calibration example for "why we need bundles at all".

**Functoriality is what makes the construction "natural".** That $T_{p}$ is a functor — that $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ — is what justifies the slogan "the tangent space is a *canonical* construction". Naturality means: any two ways of constructing tangent spaces that agree on objects (e.g., the derivation way and the curve way) automatically agree on morphisms (e.g., the differential is the same map either way), provided each way is functorial. The equivalence of the three tangent-vector definitions is really the statement that the three definitions yield isomorphic *functors*, and the isomorphism is natural — it commutes with all the differentials. This is the categorical packaging of "coordinate independence". Naturality is not jargon; it is precisely the conceptual content of the tangent bundle being intrinsic to the manifold rather than chart-dependent.
