---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Def - Higher-Order Derivatives and Ck Maps"
  - "Thm - The Inverse Function Theorem"
  - "Thm - The Implicit Function Theorem"
tags: [analysis, multivariate-analysis]
---

# Notation

$M$ is a subset of $\mathbb{R}^n$; $d$ is an integer with $0 < d < n$, the intended **dimension**, and $k \geq 1$ the intended smoothness class. A **$C^k$-diffeomorphism** is a bijective $C^k$ map between open sets whose inverse is also $C^k$. For a map $f$, $Df_p$ is the total derivative at $p$ and $Jf(p)$ its Jacobian matrix; $Df_p$ has **maximal rank** when its matrix has the largest rank its shape allows ($n-d$ for a map $\mathbb{R}^n\to\mathbb{R}^{n-d}$, namely surjective; $d$ for a map $\mathbb{R}^d\to\mathbb{R}^n$, namely injective). The **graph** of a map $g : V \to \mathbb{R}^{n-d}$ is $\{(x, g(x)) : x \in V\}$. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Axiom Motivation

We want a precise notion of a "smooth curved space sitting inside $\mathbb{R}^n$" — a curve, a surface, a hypersurface, their higher-dimensional analogues. The whole subject of differential geometry needs such an object, and §2.1 already needed it informally: the constraint sets on which Lagrange multipliers operate are exactly these. So ask: what is the *minimal* property that captures "smooth curved $d$-dimensional space" and excludes the pathologies?

Start with the things we definitely want *in*: the unit sphere, a torus, the graph of any smooth function, a plane. And the things we want *out*: a set with a corner (the boundary of a square), a set that crosses itself (a figure-eight), a set with a cusp ($y^3 = x^2$), a cone with its vertex, a set that is a curve in one place and a surface in another. What single property separates these?

The first idea is "$M$ is the image of a smooth map". This is too weak. The image of $t \mapsto (t^2, t^3)$ is the cusped curve $y^3 = x^2$ — a smooth map can have a non-smooth image, because the parametrization can slow to a halt (zero derivative) and create a kink. So we must demand the parametrization's derivative *never degenerate* — maximal rank everywhere. That rules out the cusp.

The second idea is "$M$ is a level set $\{f = 0\}$". Also too weak on its own. The level set $\{x^2 - y^2 = 0\}$ is the union of two crossing lines; $\{x^2+y^2-z^2 = 0\}$ is a cone with a singular vertex. A level set can cross itself or pinch — precisely where the defining function's derivative degenerates, $\nabla f = 0$. So again we must demand the derivative have maximal rank.

The cleanest formulation, and the one taken as the definition, abstracts what is *common* to all the good cases and distinguishes them from all the bad ones: a good $d$-dimensional space is one that, *near each of its points, can be flattened* — straightened by a smooth change of coordinates of the ambient space into a piece of the flat coordinate subspace $\mathbb{R}^d \times \{0\}$. This is the **submanifold chart** condition. It is the right desideratum for several reasons. It is *local* — it only ever talks about a neighbourhood of a point — which is correct, since being a smooth space is a local matter (a curve can be smooth everywhere even if it is knotted globally). It is *diffeomorphism-invariant* — straightenability does not depend on a chosen parametrization. And it directly *excludes* every pathology: at a corner, a crossing, a cusp, or a cone vertex, no diffeomorphism of the ambient space can flatten $M$ onto $\mathbb{R}^d\times\{0\}$, because a diffeomorphism preserves the local "number of branches" and the existence of a tangent space, and the pathologies fail exactly these.

What breaks if we *weaken* the definition — drop "diffeomorphism" to "homeomorphism"? Then we admit topological submanifolds, which can be wildly non-smooth — a continuous but nowhere-differentiable curve would qualify, and we lose the ability to differentiate, to have tangent spaces, to do calculus on $M$. The whole point is to keep $M$ smooth enough that calculus transfers to it. What breaks if we *strengthen* it — demand a *global* straightening? Then we exclude the sphere: no single diffeomorphism of $\mathbb{R}^3$ flattens the whole sphere onto a plane (the sphere is compact, a plane is not). The genuinely curved, globally interesting spaces require the flattening to be *local*, patched together from neighbourhood to neighbourhood — and that patching is the entire content of the subject.

The remarkable fact, proved as a proposition rather than built into the definition, is that the three competing ideas — straightenable, locally a level set with maximal-rank derivative, locally a maximal-rank image, locally a graph — are all *equivalent*. So one can take any of them as the definition; the others become theorems. We take straightening as primary because it is the most symmetric and most clearly diffeomorphism-invariant, but the *graphical* description is the one to picture and the *implicit* description is the one to compute with.

---

# The Definition

Let $0 < d < n$ and $k \geq 1$ be integers.

**Submanifold (submanifold-chart definition).** A nonempty subset $M \subseteq \mathbb{R}^n$ is a **$d$-dimensional $C^k$ submanifold of $\mathbb{R}^n$** if for every point $p_0 \in M$ there exist an open set $U \subseteq \mathbb{R}^n$ containing $p_0$, an open set $V \subseteq \mathbb{R}^n$ containing $0$, and a $C^k$-diffeomorphism $\Psi : U \to V$ such that
$$\Psi(M \cap U) = \{y \in V : y_{d+1} = y_{d+2} = \dots = y_n = 0\}.$$
The map $\Psi$ is called a **submanifold chart**: it straightens the piece $M\cap U$ onto a flat slice of the coordinate subspace $\mathbb{R}^d\times\{0\}$. The integer $d$ is the **dimension** and $n - d$ the **codimension**.

The following four conditions on a nonempty $M \subseteq \mathbb{R}^n$ are **equivalent**, and any may serve as the definition.

1. **(Chart / straightening)** As above: $M$ is locally straightenable by a $C^k$-diffeomorphism.

2. **(Implicit representation)** For every $p_0 \in M$ there are an open $U \ni p_0$ and a map $f \in C^k(U, \mathbb{R}^{n-d})$ with $Df_{p_0}$ of maximal rank ($= n-d$, i.e. surjective), such that
$$M \cap U = \{x \in U : f(x) = 0\}.$$
Near each point, $M$ is the zero set of a map with surjective derivative.

3. **(Parametric representation)** For every $p_0 \in M$ there are an open $V \subseteq \mathbb{R}^d$, a point $y_0 \in V$, and a map $G \in C^k(V, \mathbb{R}^n)$ with $G(y_0) = p_0$ and $DG_{y_0}$ of maximal rank ($= d$, i.e. injective), such that $G$ maps $V$ (restricted to small open subsets) onto neighbourhoods of $p_0$ in $M$. Near each point, $M$ is the image of an *immersion* — a maximal-rank parametrization.

4. **(Graphical representation)** For every $p_0 \in M$ there are an open $U \ni p_0$, an open $V \subseteq \mathbb{R}^d$, a map $g \in C^k(V, \mathbb{R}^{n-d})$, and a permutation $P$ of the $n$ coordinates such that
$$M \cap U = P\big(\operatorname{graph}(g)\big),$$
where $\operatorname{graph}(g) = \{(x, g(x)) : x \in V\}$. Near each point, $M$ is — after relabelling coordinates — the graph of a $C^k$ function of $d$ of them.

---

# Relate to Other Fields / Compression

A submanifold of $\mathbb{R}^n$ is the *concrete model* of the central object of differential geometry, the **abstract smooth manifold**. The abstract definition keeps exactly the local picture — a space covered by charts to $\mathbb{R}^d$ with smooth transition maps — but discards the ambient $\mathbb{R}^n$. The relationship is tight: every submanifold is an abstract manifold (the submanifold charts form an atlas), and Whitney's embedding theorem says every abstract manifold is diffeomorphic to a submanifold of some $\mathbb{R}^N$. So "submanifold of $\mathbb{R}^n$" and "abstract $d$-manifold" describe the same class of objects; the abstract definition is preferred only because it frees the geometry from a chosen embedding.

The four equivalent representations are the same object seen through four lenses, and each is standard in a different field. The **implicit** representation — $M$ as $\{f = 0\}$ — is how submanifolds appear in physics and analysis: an energy surface in mechanics, a constraint set in optimization, the mass shell in relativity. The **parametric** representation — $M$ as the image of an immersion — is how surfaces are described in computer graphics and classical surface theory (the first and second fundamental forms live on a parametrization). The **graphical** representation is the local normal form used to *prove* things, because a graph is the simplest case. The **chart** representation is the one that generalizes to abstract manifolds. The bridge connecting implicit and graphical is precisely the [[Thm - The Implicit Function Theorem|implicit function theorem]] — it *is* the theorem that a maximal-rank level set is locally a graph.

In algebraic geometry the analogous object is a **smooth variety**, the zero set of polynomials with maximal-rank Jacobian; the implicit representation is literally this definition with "$C^k$" replaced by "polynomial". The pathologies excluded here — cusps, nodes, cone vertices — are exactly the *singular points* of a variety, and a submanifold is the differential-geometric counterpart of a *smooth* (nonsingular) variety.

---

# Examples / Corollaries

**Is an instance — the unit sphere $S^{n-1}$.** The sphere $\{|x|^2 = 1\}$ is an $(n-1)$-dimensional $C^\infty$ submanifold of $\mathbb{R}^n$. Implicitly, it is $\{f = 0\}$ for $f(x) = |x|^2 - 1$, and $Df_x = 2x^T$ has rank $1$ (maximal) at every point of the sphere since $x \neq 0$ there. Graphically, each hemisphere is the graph $x_n = \pm\sqrt{1 - x_1^2 - \dots - x_{n-1}^2}$. Parametrically, spherical coordinates parametrize it off the poles. All four representations are available — see [[Ex - The sphere as a regular level set]].

**Is an instance — the graph of any $C^k$ function.** For any $g \in C^k(V, \mathbb{R}^{n-d})$ with $V \subseteq \mathbb{R}^d$ open, the graph $\{(x, g(x))\}$ is a $d$-dimensional $C^k$ submanifold of $\mathbb{R}^n$. This is the graphical representation with $P$ the identity. It is the simplest example, and the [[Thm - The Implicit Function Theorem|implicit function theorem]] says *every* submanifold looks like this locally.

**Is an instance — the orthogonal group $O(n)$.** Inside the space of $n\times n$ matrices ($\cong \mathbb{R}^{n^2}$), the set $O(n) = \{A : A^TA = I\}$ is a $C^\infty$ submanifold of dimension $n(n-1)/2$. It is the zero set of $A \mapsto A^TA - I$ into the symmetric matrices, and the derivative has maximal rank everywhere on $O(n)$ — see [[Ex - The orthogonal group as a submanifold]]. This shows submanifolds need not be "surfaces in $\mathbb{R}^3$"; the ambient space can be any Euclidean space.

**Is NOT an instance — the union of two crossing lines.** The set $\{(x,y) : x^2 = y^2\} = \{y = x\}\cup\{y = -x\}$ is not a submanifold: at the origin two branches cross, and no diffeomorphism of $\mathbb{R}^2$ can straighten this onto a single line — the crossing point has "two tangent directions". It is the level set $\{f = 0\}$ of $f = x^2 - y^2$, but $\nabla f(0,0) = 0$, so $0$ is not a regular value and the implicit representation's maximal-rank condition fails exactly at the bad point.

**Is NOT an instance — the cusped curve $y^3 = x^2$.** The set $\{(x,y) : y^3 = x^2\}$ has a cusp at the origin and is not a submanifold there. It *is* the image of the smooth parametrization $t \mapsto (t^3, t^2)$, but $DG_0 = (0,0)$ has rank $0$, not the maximal rank $1$ — the parametrization's derivative degenerates at the cusp, exactly as the parametric representation forbids. This is the example that shows "image of a smooth map" is too weak a notion.

**Is NOT an instance — the closed unit disc.** The closed disc $\{x_1^2 + x_2^2 \leq 1\}$ is not a submanifold (of dimension $2$) of $\mathbb{R}^2$: its boundary points cannot be straightened onto an interior slice of $\mathbb{R}^2$. It is a *manifold with boundary*, a related but distinct notion — a submanifold has no boundary points. (The open disc *is* a $2$-dimensional submanifold; it is open, hence locally all of $\mathbb{R}^2$.)

**Corollary — an open subset of $\mathbb{R}^n$ is an $n$-dimensional submanifold.** Taking $d = n$, the chart condition is satisfied trivially by the identity. So $\mathbb{R}^n$ itself and every open subset are submanifolds of full dimension. (The definition's restriction $d < n$ excludes this trivial case from the interesting theory, but the notion still makes sense.)

**Calibration check.** Verify that a single point $\{p\}$ is a $0$-dimensional submanifold; that a line in $\mathbb{R}^3$ is a $1$-dimensional submanifold (write it as a graph, and as $\{f = 0\}$ for a maximal-rank $f : \mathbb{R}^3 \to \mathbb{R}^2$); that the figure-eight $\{(\sin 2t, \sin t)\}$ is *not* a submanifold (it crosses itself); and that the cone $\{z^2 = x^2 + y^2\}$ in $\mathbb{R}^3$ fails to be a submanifold *only* at the vertex. If you can also explain why "image of a smooth map" admits the cusp but "image of an immersion" does not, you have understood the role of the maximal-rank condition.

---

# Unlocked by This

> [!tip] The Tangent Space *(from this topic)*
> Every submanifold has, at each point, a well-defined [[Def - The Tangent Space to a Submanifold|tangent space]] — a $d$-dimensional linear subspace of $\mathbb{R}^n$ that is the best linear approximation to $M$. The existence of a tangent space is exactly what the pathological non-examples (cusps, crossings) lack.

> [!tip] Abstract Smooth Manifolds *(from Differential Geometry)*
> Discarding the ambient $\mathbb{R}^n$ and keeping only the atlas of charts with smooth transition maps gives the **abstract smooth manifold** — the central object of differential geometry. Whitney's theorem shows every abstract manifold is, after all, a submanifold of some $\mathbb{R}^N$.

> [!tip] Lie Groups *(from Lie Theory)*
> A group that is also a submanifold, with smooth multiplication and inversion, is a **Lie group**. The orthogonal group, the special linear group, and the general linear group are the basic examples — matrix groups that are simultaneously algebraic and geometric objects. See [[Group Theory I — §1.1–1.2]] for the group axioms.

> [!tip] Integration on Manifolds and Stokes' Theorem *(from this subject)*
> Once a set is known to be a submanifold it acquires a notion of $d$-dimensional volume, and differential forms can be integrated over it — the setting for the general Stokes theorem of [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].
