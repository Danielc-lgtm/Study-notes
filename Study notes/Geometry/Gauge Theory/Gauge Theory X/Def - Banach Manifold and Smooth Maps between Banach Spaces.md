---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Lie Group"
  - "Def - Smooth Action of a Lie Group"
tags: [geometry, gauge-theory, functional-analysis]
---

# Notation

Throughout, $X$, $Y$, $Z$ denote **Banach spaces**: real vector spaces (in the sense of [[Def - Vector Space|vector space]]) equipped with a norm $\lVert \cdot \rVert$ that is complete, meaning every Cauchy sequence converges, so that $(X, \lVert \cdot \rVert)$ is a [[Def - Cauchy Sequence and Complete Metric Space|complete metric space]] under the metric $d(x, x') = \lVert x - x' \rVert$. When the norm comes from an inner product $\langle \cdot, \cdot \rangle$ with $\lVert x \rVert = \langle x, x \rangle^{1/2}$ and the space is complete, we call it a **Hilbert space**. A Banach space is **separable** if it has a countable dense subset. We write $U \subset X$ for an open subset, $B_r(x) = \{x' \in X : \lVert x' - x \rVert < r\}$ for the open ball of radius $r$ about $x$, and $\overline{B}_r(x)$ for its closure.

For a linear map $L : X \to Y$ we write $\lVert L \rVert = \sup_{\lVert h \rVert \le 1} \lVert L h \rVert$ for its **operator norm**; $L$ is **bounded** (equivalently, continuous) when $\lVert L \rVert < \infty$. The set of all bounded linear maps $X \to Y$ is denoted $\operatorname{Hom}(X, Y)$; with the operator norm it is itself a Banach space, and it is complete because $Y$ is (this is the standard fact that $\operatorname{Hom}(X, Y)$ inherits completeness from the target). We write $\operatorname{GL}(X, Y) \subset \operatorname{Hom}(X, Y)$ for the bounded linear isomorphisms with bounded inverse, and $\operatorname{Hom}(X) = \operatorname{Hom}(X, X)$.

The **Landau symbol** $o(\lVert h \rVert)$ as $h \to 0$ denotes any function $r(h)$ with $r(0) = 0$ and $\lVert r(h) \rVert / \lVert h \rVert \to 0$ as $\lVert h \rVert \to 0$; equivalently, for every $\varepsilon > 0$ there is $\delta > 0$ with $\lVert r(h) \rVert \le \varepsilon \lVert h \rVert$ whenever $\lVert h \rVert < \delta$.

A **topological space** is called **second countable** if its topology has a countable base (see [[Def - First and Second Countable|first and second countable]]), and **Hausdorff** if distinct points have disjoint neighbourhoods. A space is **metrisable** if its topology is induced by some metric.

This is a compound page: it defines seven interlocking notions — the Fréchet derivative, the classes $C^k$ and $C^\infty$ of maps between open subsets of Banach spaces, Banach and Hilbert manifolds, their tangent spaces, embedded submanifolds, Banach Lie groups, and smooth actions — because they form the single minimal package of differential calculus in infinite dimensions on which every later construction of this chapter (the Fredholm map, the Kuranishi model, the Sard–Smale theorem, the degree, and the equivariant moduli spaces) is built, and because each notion is only meaningful once the one before it is in place.

> [!warning] Convention: "second category" versus "residual"
> Haydys, following older usage, calls a countable intersection of open dense subsets a set **of second category**. This clashes with Baire's own terminology, in which "second category" means merely "not meagre" (not a countable union of nowhere-dense sets). To avoid the collision this series uses the word **residual** for a set containing a countable intersection of open dense subsets, and reserves "of first category / meagre" for its complement class. The precise definition and the proof that a residual subset of a Banach manifold is dense are given on [[Def - Residual Set and Generic Property]]; the present page only fixes the word.

> [!warning] Convention: paracompactness, metrisability, and the Lindelöf property
> Haydys states the Sard–Smale theorem for maps between **paracompact** Banach manifolds. This series builds paracompactness into the definition instead, by requiring every Banach manifold to be Hausdorff and **second countable** and to be modelled on a **separable** Banach space. A second countable manifold modelled on a metrisable model space is itself metrisable, and a second countable space is **Lindelöf** (every open cover has a countable subcover); a metrisable Lindelöf space is paracompact. The one place this chapter actually uses the hypothesis — the passage in [[Thm - Sard-Smale Theorem|the Sard–Smale theorem]] from "critical values are locally nowhere dense" to "critical values are nowhere dense" — needs only the Lindelöf property (a countable subcover of a chart cover), and that property is proved in full where it is used on that page. The vault's [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact|local-compactness route to paracompactness]] does **not** apply here, because an infinite-dimensional Banach space is never locally compact.

---

# Axiom Motivation

Gauge theory studies spaces that are not manifolds in the sense of [[Def - Smooth Manifold|a finite-dimensional smooth manifold]]: the space of all connections on a bundle, the group of gauge transformations, the space of solutions of the Seiberg–Witten equations. These are infinite-dimensional. We nonetheless want to do differential geometry on them — to speak of tangent vectors, differentials, regular values, implicit-function-theorem charts — because the whole strategy of the subject is to realise a moduli space as the zero set of a smooth map between such spaces and then read off its dimension from a linearisation. The question this page answers is: **what is the least structure on an infinite-dimensional space under which the inverse and implicit function theorems, and hence the notion of a smooth submanifold cut out by an equation, still hold?**

The naive answer, "take smooth sections and use the $C^\infty$ topology", fails, and it fails in a way that dictates every clause below. The space $C^\infty(M)$ of smooth functions with its natural topology is complete and metrisable, but its topology is not given by a single norm; it is a **Fréchet space**, whose topology needs a countable family of seminorms (one for each derivative order). On a Fréchet space the inverse function theorem is **false** in general — the obstruction is that the natural candidate for the inverse is built by a contraction argument that requires a single controlling norm, and no such norm exists. The repair, due to the elliptic theory of Chapter IX, is to complete in a **Sobolev norm** $W^{k,p}$: this replaces the Fréchet space $C^\infty$ by a genuine Banach (indeed Hilbert, when $p = 2$) space $H_k$, on which a single norm controls everything and the contraction argument runs. So the first desideratum is a **norm**, not a family of seminorms, and **completeness** in that norm: this is exactly a Banach space.

Now examine the definition of the derivative. In finite dimensions the derivative of $F$ at $x$ is the linear map $d_x F$ with $F(x + h) = F(x) + d_x F \, h + o(\lVert h \rVert)$; every linear map on $\mathbb R^n$ is automatically continuous, so no boundedness clause is needed. In infinite dimensions this is false: there exist unbounded linear maps, and an unbounded "derivative" would be useless — it would not be continuous, the chain rule would break, and the composite of two differentiable maps could fail to be differentiable. So the second desideratum, absent in finite dimensions, is that **$d_x F$ be a bounded (continuous) linear map**. If one dropped the boundedness clause, the concrete failure is immediate: take $X = Y$ the space of finitely supported sequences with the $\ell^2$ norm and $L(x_1, x_2, \dots) = (x_1, 2x_2, 3x_3, \dots)$; this $L$ is linear and everywhere defined but unbounded, so $F(x) = Lx$ would be "differentiable" with derivative $L$, yet $F$ is not even continuous. The strengthening that excludes this is precisely "bounded", and it is the right one: with it, $\operatorname{Hom}(X, Y)$ is a Banach space and the derivative $x \mapsto d_x F$ is itself a map into a Banach space, so the whole scheme can be iterated to define $C^k$.

Next, the manifold clauses. We require the charts to map into open subsets of **one fixed** Banach space, and the transition maps to be smooth in the sense just defined. Fixing the model space is what makes the tangent space well-defined and finite the index computations later; if we allowed different models on different charts, the transition maps would have to be isomorphisms of different Banach spaces and the local index of a Fredholm map would not be chart-independent. We require the model space to be **separable** and the manifold to be **second countable** and **Hausdorff** for the reason given in the second convention callout: without a countable base one loses the Lindelöf property, and the passage from "locally nowhere dense" to "nowhere dense" in the Sard–Smale theorem — the very statement that makes generic transversality useful — collapses. Second countability is not decoration; drop it and the central theorem of the chapter has no proof.

Finally, the submanifold clause carries the one genuinely infinite-dimensional subtlety. In finite dimensions a subspace is cut out of $\mathbb R^n$ as the kernel of a projection, and there is always a complementary subspace. In an arbitrary Banach space a **closed** subspace need not be **complemented**: there may be no closed subspace $X_1$ with $X = X_0 \oplus X_1$. (The classical example is $c_0$ inside $\ell^\infty$, which is closed but has no closed complement — Phillips's theorem.) The implicit function theorem needs the splitting: it produces a chart in which the zero set is a graph over a complement of the kernel, and with no complement there is no graph and no chart. Hence an embedded submanifold is required to be, in a chart, a **closed complemented** subspace, not merely a closed one. If one weakened this to "closed", the implicit function theorem could not be applied and the preimage of a regular value would not, in general, be a manifold — which is exactly the theorem, [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the regular value theorem for Fredholm maps]], that we are building toward. The saving grace, made precise below, is that complementedness is **automatic** in the three cases we ever meet: in a Hilbert space (orthogonal complement), for a finite-dimensional subspace, and for a closed subspace of finite codimension. Since a Fredholm differential has finite-dimensional kernel and finite-codimensional closed image, the splitting we need is always there. A reader who has understood these five pressures — norm not seminorms, completeness, bounded derivative, separability, complemented splitting — could reconstruct every clause of the definition below.

---

# The Definition

The definitions are given in dependency order: first calculus on open subsets of Banach spaces, then the manifolds, then the group and action.

## Differentiability and the Fréchet derivative

Let $X, Y$ be Banach spaces, $U \subset X$ open, and $F : U \to Y$ a map. We say $F$ is **(Fréchet) differentiable at** $x \in U$ if there exists a bounded linear map $d_x F \in \operatorname{Hom}(X, Y)$ such that
$$F(x + h) = F(x) + d_x F \, h + o(\lVert h \rVert) \qquad \text{as } h \to 0,$$
that is, $\lim_{h \to 0} \dfrac{\lVert F(x + h) - F(x) - d_x F \, h \rVert}{\lVert h \rVert} = 0$. The map $d_x F$, when it exists, is unique (proved below as a well-definedness check) and is called the **Fréchet derivative** or **differential** of $F$ at $x$. We say $F$ is **differentiable on $U$** if it is differentiable at every point of $U$, and we then have a map
$$dF : U \to \operatorname{Hom}(X, Y), \qquad x \mapsto d_x F.$$

## The classes $C^k$ and $C^\infty$

We define smoothness inductively, using that $\operatorname{Hom}(X, Y)$ is itself a Banach space.

- $F$ is of class $C^0$ on $U$ if it is continuous.
- $F$ is of class $C^1$ on $U$ if it is differentiable on $U$ and the map $dF : U \to \operatorname{Hom}(X, Y)$ is continuous ($C^0$).
- For $k \ge 2$, $F$ is of class $C^k$ if $F$ is $C^1$ and $dF : U \to \operatorname{Hom}(X, Y)$ is of class $C^{k-1}$. Unwinding, the $j$-th derivative is a map $d^j F : U \to \operatorname{Hom}(X, \operatorname{Hom}(X, \dots, \operatorname{Hom}(X, Y)))$ into the $j$-fold iterated space of bounded operators (canonically the space of bounded $j$-linear maps $X^j \to Y$), required continuous for $j \le k$.
- $F$ is of class $C^\infty$, or **smooth**, if it is $C^k$ for every $k \ge 0$.

A map $F : U \to V$ between open subsets of Banach spaces is a **$C^k$ diffeomorphism** if it is a bijection, $F$ is $C^k$, and $F^{-1}$ is $C^k$.

## Banach and Hilbert manifolds

A **Banach manifold modelled on a separable Banach space $E$** is a topological space $\mathcal X$ that is Hausdorff and second countable, together with an **atlas** $\{(U_\alpha, \varphi_\alpha)\}_{\alpha \in A}$, where the $U_\alpha$ form an open cover of $\mathcal X$ and each **chart** $\varphi_\alpha : U_\alpha \to \varphi_\alpha(U_\alpha) \subset E$ is a [[Def - Homeomorphism|homeomorphism]] onto an open subset of $E$, such that all **transition maps**
$$\varphi_\beta \circ \varphi_\alpha^{-1} : \varphi_\alpha(U_\alpha \cap U_\beta) \longrightarrow \varphi_\beta(U_\alpha \cap U_\beta)$$
are smooth ($C^\infty$) diffeomorphisms between open subsets of $E$. Two atlases are **equivalent** if their union is again an atlas (all cross transition maps smooth); a Banach manifold carries a maximal atlas, its **smooth structure**. When the model space $E$ is a separable Hilbert space, $\mathcal X$ is called a **Hilbert manifold**. When $E = \mathbb R^n$ this reduces exactly to [[Def - Smooth Manifold|the definition of a finite-dimensional smooth manifold]].

A map $\Phi : \mathcal X \to \mathcal Y$ between Banach manifolds is **smooth** if for every $x \in \mathcal X$ there are charts $(U, \varphi)$ about $x$ and $(V, \psi)$ about $\Phi(x)$ with $\Phi(U) \subset V$ such that the local representative $\psi \circ \Phi \circ \varphi^{-1}$ is a smooth map between open subsets of the model spaces; the chain rule below guarantees this does not depend on the choice of charts. This generalises [[Def - Smooth Map between Manifolds|the smooth-map definition]] to infinite dimensions.

## The tangent space

Fix $x \in \mathcal X$. We give the standard two constructions of the **tangent space** $T_x \mathcal X$ and record that they agree, exactly as for [[Def - The Tangent Space|the tangent space of a finite-dimensional manifold]].

- **Via charts (equivalence classes of triples).** Consider triples $(U, \varphi, v)$ where $(U, \varphi)$ is a chart about $x$ and $v \in E$ is a vector of the model space. Declare $(U, \varphi, v) \sim (U', \varphi', v')$ if $v' = d_{\varphi(x)}(\varphi' \circ \varphi^{-1}) \, v$, that is, the derivative of the transition map carries $v$ to $v'$. This is an equivalence relation (checked below), and $T_x \mathcal X$ is the set of equivalence classes, a vector space isomorphic to $E$ via any single chart.
- **Via curves.** A smooth curve through $x$ is a smooth map $c : (-\varepsilon, \varepsilon) \to \mathcal X$ with $c(0) = x$. Declare $c_1 \sim c_2$ if in some (hence, by the chain rule, every) chart $\varphi$ about $x$ one has $(\varphi \circ c_1)'(0) = (\varphi \circ c_2)'(0)$ in $E$. The set of equivalence classes is $T_x \mathcal X$, and $[c] \mapsto (\varphi \circ c)'(0)$ is the isomorphism to $E$ in the chart $\varphi$.

The two constructions correspond under $[c] \leftrightarrow (U, \varphi, (\varphi \circ c)'(0))$, and the correspondence is well-defined precisely by the chain rule. For a smooth map $\Phi : \mathcal X \to \mathcal Y$ the **differential** (or pushforward) $d_x \Phi : T_x \mathcal X \to T_{\Phi(x)} \mathcal Y$ is defined in charts by the Fréchet derivative of the local representative, $[c] \mapsto [\Phi \circ c]$; independence of the chart is again the chain rule.

## Embedded submanifolds

A subset $\mathcal S \subset \mathcal X$ of a Banach manifold is an **embedded submanifold** if for every $s \in \mathcal S$ there is a chart $(U, \varphi)$ of $\mathcal X$ about $s$, with model space $E$, and a **closed complemented** linear subspace $E_0 \subset E$ (that is, there is a closed subspace $E_1$ with $E = E_0 \oplus E_1$ as a topological direct sum), such that
$$\varphi(U \cap \mathcal S) = \varphi(U) \cap E_0.$$
Such a chart is a **submanifold chart**. With the subspace topology and the restricted charts $\varphi|_{U \cap \mathcal S} : U \cap \mathcal S \to \varphi(U) \cap E_0 \subset E_0$, the set $\mathcal S$ is itself a Banach manifold modelled on $E_0$, and the inclusion $\mathcal S \hookrightarrow \mathcal X$ is a smooth [[Def - Immersion, Submersion, and Embedding|embedding]]. Its tangent space is $T_s \mathcal S = d_s(\varphi)^{-1}(E_0) \subset T_s \mathcal X$, a closed complemented subspace. The **codimension** of $\mathcal S$ is $\dim E_1$ (finite or infinite); when $E_0$ has finite codimension we call $\mathcal S$ a submanifold **of finite codimension**, and when $E_0$ is finite-dimensional a **finite-dimensional submanifold**. This is the Banach version of [[Def - Embedded Submanifold|the embedded submanifold]].

The requirement that $E_0$ be **complemented**, not merely closed, is essential and is discussed in the Axiom Motivation and verified as automatic in the three relevant cases in Examples / Corollaries.

## Banach Lie groups and smooth actions

A **Banach Lie group** is a group $G$ that is also a Banach manifold, such that the multiplication $m : G \times G \to G$, $m(g, h) = gh$, and the inversion $\iota : G \to G$, $\iota(g) = g^{-1}$, are smooth maps of Banach manifolds. (Here $G \times G$ carries the product Banach-manifold structure, modelled on $E \oplus E$.) Its **Lie algebra** is $\mathfrak g = T_e G$, the tangent space at the identity $e$, with the bracket of left-invariant vector fields. This is the infinite-dimensional counterpart of [[Def - Lie Group|a Lie group]].

A **smooth (left) action** of a Banach Lie group $G$ on a Banach manifold $\mathcal X$ is a smooth map $a : G \times \mathcal X \to \mathcal X$, written $a(g, x) = g \cdot x$, satisfying $e \cdot x = x$ and $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g, h \in G$ and $x \in \mathcal X$. This is [[Def - Smooth Action of a Lie Group|the smooth action]] with the Banach manifold in place of a finite-dimensional one. For fixed $x$, the **infinitesimal action** is the linear map $\mathfrak g \to T_x \mathcal X$, $\xi \mapsto \frac{d}{dt}\big|_{t=0}\, \exp(t\xi) \cdot x$, whose image is the tangent space to the orbit $G \cdot x$; it recurs in [[Def - Infinitesimal Action and Local Slice|the slice construction]].

---

# Categorical / Structural Definition

Two of the notions above have clean structural readings that are worth recording, because they are what make the definitions robust rather than arbitrary.

**The derivative as best bounded linear approximation, characterised by a universal property.** Among all maps $A : X \to Y$ of the form $h \mapsto \text{constant} + Ah$ with $A \in \operatorname{Hom}(X, Y)$, the affine map $h \mapsto F(x) + d_x F \, h$ is the unique one that agrees with $F$ to first order at $x$, in the precise sense that $F(x + h) - [F(x) + d_x F \, h] = o(\lVert h \rVert)$. Uniqueness (below) says this best approximation, if it exists, is one and only one; this is exactly the property that makes $d_x F$ a well-defined invariant of $F$ and $x$, independent of any coordinates.

**The tangent functor.** The assignments $\mathcal X \mapsto T\mathcal X = \bigsqcup_{x} T_x\mathcal X$ and $(\Phi : \mathcal X \to \mathcal Y) \mapsto (d\Phi : T\mathcal X \to T\mathcal Y)$ form a functor from the category of Banach manifolds and smooth maps to the category of Banach manifolds and smooth maps (each $T\mathcal X$ is a Banach manifold modelled on $E \oplus E$). Functoriality is the two identities
$$d(\mathrm{id}_{\mathcal X}) = \mathrm{id}_{T\mathcal X}, \qquad d(\Psi \circ \Phi) = d\Psi \circ d\Phi,$$
the second of which is the chain rule. It is precisely the demand that $T$ be a functor — that the differential of a composite be the composite of differentials — that forces the derivative to be *bounded*: only bounded linear maps compose to bounded linear maps with the operator-norm estimate $\lVert BA \rVert \le \lVert B \rVert \lVert A \rVert$ that the proof of the chain rule needs. In this sense the boundedness clause is not an extra axiom but the condition that calculus be functorial.

A submanifold, dually, is characterised by a local universal property: $\mathcal S \subset \mathcal X$ is an embedded submanifold if and only if near each of its points it is the zero set of a submersion onto a Banach space with complemented kernel — the local defining equation. This is the reading used throughout the chapter, where moduli spaces appear as zero sets $F^{-1}(y)$ and the submanifold structure comes from a regular value.

---

# Relate to Other Fields / Compression

Banach-space calculus is the meeting point of three subjects. From **functional analysis** it takes the completeness and the operator norm; the fact that $\operatorname{Hom}(X, Y)$ is a Banach space, and that the invertible operators form an open set on which inversion is smooth (via the Neumann series $ (\mathrm{id} - A)^{-1} = \sum_{n \ge 0} A^n$ for $\lVert A \rVert < 1$), is what lets the finite-dimensional inverse function theorem cross over unchanged in form. From **the calculus of variations and partial differential equations** it takes its actual examples: the configuration spaces of gauge theory are Sobolev completions $H_k$ of spaces of sections, and the maps between them are differential operators plus lower-order nonlinearities. From **finite-dimensional differential geometry** it takes the entire vocabulary — atlas, chart, tangent space, submanifold, Lie group, action — with the single structural change that the model $\mathbb R^n$ is replaced by a separable Banach space and "linear map" is everywhere replaced by "bounded linear map".

**True name.** The operational content of "Banach manifold", stripped of the atlas bookkeeping, is this: *a Banach manifold is a space on which one can do first-order calculus with a controlling norm, so that the inverse and implicit function theorems hold and equations cut out submanifolds.* Everything in the definition is in service of that one capability. When later pages say "the space of connections is a Banach manifold" or "the gauge group is a Banach Lie group", the cash value is always that the relevant map has a bounded differential, that its linearisation splits, and that a chart can be produced by a contraction argument — never anything about the abstract topology beyond the second-countability we impose for the Lindelöf property.

The compression to keep is that the passage from finite to infinite dimensions costs exactly two things and no more: **linear maps must be assumed bounded** (automatic in finite dimensions), and **closed subspaces must be assumed complemented** (automatic in finite dimensions). Both costs are paid in advance by the definition, and both are recovered for free in the Hilbert and Fredholm settings we work in.

---

# Examples / Corollaries

Each example is verified against the definition clause by clause; each corollary is proved in full, at the level of [[Thm - The Inverse Function Theorem|the vault's proof standard]], in a collapsible callout.

**Is an instance — a Banach space itself.** Any Banach space $E$ is a Banach manifold modelled on $E$, with the single chart $(\mathcal X, \varphi) = (E, \mathrm{id}_E)$. Verification: $E$ with its norm topology is Hausdorff (a metric space) and, when $E$ is separable, second countable (a countable dense set generates a countable base of balls with rational radii); the one chart covers $E$; there is one transition map, $\mathrm{id}_E \circ \mathrm{id}_E^{-1} = \mathrm{id}_E$, which is smooth (its derivative is the constant map $x \mapsto \mathrm{id}_E$, continuous, and all higher derivatives vanish). The tangent space at every point is canonically $E$, since the single chart identifies $T_x E$ with $E$.

**Is an instance — an open subset.** Any open $U \subset E$ of a separable Banach space is a Banach manifold modelled on $E$, with the single chart $(U, \mathrm{id}_U)$; the verification is identical, using that an open subspace of a second countable Hausdorff space is second countable and Hausdorff. In particular the open set $\operatorname{GL}(X) \subset \operatorname{Hom}(X)$ of invertible operators is a Banach manifold.

**Is an instance — the Sobolev space of sections $H_k(M; E)$.** For a closed manifold $M$ and a vector bundle $E \to M$, the Sobolev space $H_k(M; E) = W^{k,2}(M; E)$ of [[Def - Sobolev Space of Sections|Sobolev sections]] is a separable Hilbert space, hence a Hilbert manifold with one global chart. Verification: it is complete by definition of the Sobolev norm, its norm comes from the $W^{k,2}$ inner product (a Hilbert space), and it is separable because $M$ is compact and smooth sections are dense. These spaces are the configuration spaces of the chapter: the differential of a Fredholm map acts $T_u H_{k+2} = H_{k+2} \to T_{F(u)} H_k = H_k$.

**Is an instance — the affine space of Sobolev connections.** Fix a smooth connection $A_0$ on a line bundle over a four-manifold $M$. The affine space
$$A_0 + H_k(T^*M \otimes i\mathbb R) = \{A_0 + a : a \in H_k(T^*M \otimes i\mathbb R)\}$$
is a Hilbert manifold: it is the image of the Hilbert space $H_k(T^*M \otimes i\mathbb R)$ under the translation $a \mapsto A_0 + a$, and it carries the single global chart $A \mapsto A - A_0 \in H_k(T^*M \otimes i\mathbb R)$. Its tangent space at every point is canonically $H_k(T^*M \otimes i\mathbb R)$, since translation has derivative the identity. This is the space $\mathcal A^{k,2}(P_{\det})$ of [[Def - Sobolev Configuration Space and Gauge Group|Sobolev connections]] used in Seiberg–Witten theory; its affine (not linear) nature is why one fixes a reference connection $A_0$ to get a chart.

**Is an instance — the Sobolev gauge group $\mathcal G^{k} = H_k(M; S^1)$, a Banach Lie group.** Let $M$ be a closed $n$-manifold with $2k > n$, and set $\mathcal G^k = H_k(M; S^1) = \{g \in H_k(M; \mathbb C) : |g| = 1 \text{ pointwise}\}$, the maps to the circle of Sobolev class $k$. We verify each clause of "Banach Lie group".
- *Group.* Since $2k > n$, [[Thm - Sobolev Embedding Theorem|the Sobolev embedding theorem]] gives $H_k(M; \mathbb C) \hookrightarrow C^0(M; \mathbb C)$, so the pointwise condition $|g| = 1$ is meaningful, and [[Thm - Sobolev Multiplication Theorem|the Sobolev multiplication theorem]] makes $H_k(M; \mathbb C)$ a Banach algebra: if $g, h \in H_k$ with $|g| = |h| = 1$ then $gh \in H_k$ with $|gh| = 1$, and $g^{-1} = \bar g \in H_k$ with $|\bar g| = 1$. So $\mathcal G^k$ is closed under multiplication and inversion, hence a group.
- *Banach manifold.* We chart $\mathcal G^k$ by the exponential. By [[Thm - Composition with Analytic Functions on the Sobolev Algebra|composition with analytic functions on the Sobolev algebra]] — for $2k > n$ and $f$ entire, $u \mapsto f \circ u$ is a smooth map $H_k(M; \mathbb C) \to H_k(M; \mathbb C)$ — the map $\xi \mapsto e^{i\xi}$ is smooth from $H_k(M; \mathbb R)$ to $H_k(M; \mathbb C)$ with image in $\mathcal G^k$. Near $g_0 \in \mathcal G^k$ the map $\xi \mapsto g_0 e^{i\xi}$, for $\xi \in H_k(M; \mathbb R)$ small (so that $g_0 e^{i\xi}$ stays in the range where $g \mapsto g_0^{-1}g$ composed with the analytic branch of $\tfrac{1}{i}\log$ near $1 \in S^1$ recovers $\xi$), is a chart onto a neighbourhood of $g_0$; the model space is the separable Hilbert space $H_k(M; \mathbb R)$. Transition maps between two such charts are $\xi \mapsto \tfrac{1}{i}\log(g_0^{-1} g_1 e^{i\xi})$ composed appropriately, smooth by the same analytic-composition theorem. So $\mathcal G^k$ is a Hilbert manifold modelled on $H_k(M; \mathbb R)$.
- *Smooth structure maps.* Multiplication $(g, h) \mapsto gh$ is smooth because it is the restriction of the bilinear bounded (hence smooth) multiplication on the Banach algebra $H_k$; inversion $g \mapsto \bar g$ is the restriction of complex conjugation, a bounded real-linear (hence smooth) map. Its Lie algebra is $T_e \mathcal G^k = H_k(M; i\mathbb R)$, the tangent at the constant map $1$, read off from the chart $\xi \mapsto e^{i\xi}$. The full verification of this last clause is the content of [[Ex - Composition with the Exponential on the Sobolev Algebra|the exercise on composition with the exponential]].

**Is NOT an instance — $C^\infty(M)$ with the $C^\infty$ topology.** The space of smooth functions on a compact manifold $M$, topologised so that $f_j \to f$ means uniform convergence of all derivatives, is complete and metrisable but is **not** a Banach manifold, because its topology is not induced by any single norm: it is a **Fréchet space**, needing the countable family of seminorms $\lVert f \rVert_{C^j} = \sup_{|\alpha| \le j}\sup_M |\partial^\alpha f|$, and it can be shown that no single one of these, nor any single norm, gives the same topology (a normable topology has a bounded neighbourhood of $0$, and no $C^\infty$-neighbourhood is bounded in all seminorms at once). It fails the definition at the model-space clause: the model would have to be a fixed Banach space, and $C^\infty(M)$ is not one. This is precisely why Haydys (footnote 4, p. 51) remarks that one passes to a Sobolev completion to obtain a Banach manifold, and why every configuration space of this chapter is a Sobolev space $H_k$ rather than the smooth space $C^\infty$. ⚠️ [The manifest attributes this non-example to "Haydys footnote 5"; the footnote in the source that discusses replacing $C^\infty$ sections by a Sobolev completion to obtain a Banach manifold is footnote 4 (p. 51). The mathematical content is unchanged; the corrected footnote number is recorded here.]

> [!note]- Corollary (uniqueness of the Fréchet derivative — the well-definedness of the whole framework)
> **Statement.** If $F : U \to Y$ is differentiable at $x \in U$, then the bounded linear map $d_x F$ satisfying $F(x+h) = F(x) + d_x F\, h + o(\lVert h \rVert)$ is unique.
>
> **Proof.** *We need to show* that if two bounded linear maps $A, B \in \operatorname{Hom}(X, Y)$ both serve as the derivative, then $A = B$. Suppose both satisfy the defining relation:
> $$F(x + h) - F(x) - A h = o(\lVert h \rVert), \qquad F(x + h) - F(x) - B h = o(\lVert h \rVert).$$
> **Subtract the two lines.** Subtracting eliminates $F(x+h) - F(x)$ and gives
> $$(B - A) h = \big(F(x+h) - F(x) - A h\big) - \big(F(x+h) - F(x) - B h\big) = o(\lVert h \rVert) \qquad \text{(difference of two } o(\lVert h \rVert) \text{ terms is } o(\lVert h \rVert)\text{).}$$
> **Restrict to a ray and use linearity of $B - A$.** Fix any $v \in X$ with $v \ne 0$ and set $h = t v$ for $t > 0$ small enough that $x + tv \in U$. Then $(B - A)(tv) = t\,(B-A)v$ by linearity, while the right side is $o(\lVert tv \rVert) = o(t)$ since $\lVert tv \rVert = t\lVert v \rVert$. Dividing by $t > 0$,
> $$(B - A) v = \frac{o(t)}{t} \xrightarrow{\ t \to 0^+\ } 0 \qquad \text{(by the definition of } o(t)\text{).}$$
> The left side does not depend on $t$, so $(B - A) v = 0$.
> **Conclude.** Since $v \in X$ was arbitrary, $B - A = 0$, that is $A = B$. Therefore the derivative, when it exists, is unique, and $d_x F$ is a well-defined object. $\blacksquare$

> [!note]- Corollary (the chain rule — the identity that makes charts, tangent spaces, and the tangent functor well-defined)
> **Statement.** Let $X, Y, Z$ be Banach spaces, $U \subset X$ and $V \subset Y$ open, $F : U \to V$ differentiable at $x \in U$, and $G : V \to Z$ differentiable at $y = F(x) \in V$. Then $G \circ F : U \to Z$ is differentiable at $x$, with bounded linear derivative
> $$d_x(G \circ F) = d_y G \circ d_x F.$$
> If moreover $F$ is $C^k$ on $U$ and $G$ is $C^k$ on $V$, then $G \circ F$ is $C^k$ on $U$.
>
> **Proof.** *We need to show* that the bounded linear map $L := d_y G \circ d_x F$ (bounded because a composite of bounded linear maps is bounded, with $\lVert L \rVert \le \lVert d_y G\rVert\, \lVert d_x F\rVert$) satisfies the defining relation $(G\circ F)(x + h) - (G\circ F)(x) - L h = o(\lVert h \rVert)$.
>
> **Step 0 — record the two hypotheses as controlled remainders.** By differentiability of $F$ at $x$ there is a function $r$ with
> $$F(x + h) = F(x) + d_x F\, h + r(h), \qquad \lVert r(h)\rVert = o(\lVert h\rVert) \qquad \text{(differentiability of } F \text{ at } x\text{).} \tag{1}$$
> By differentiability of $G$ at $y$ there is a function $s$ with
> $$G(y + \eta) = G(y) + d_y G\, \eta + s(\eta), \qquad \lVert s(\eta)\rVert = o(\lVert \eta\rVert) \qquad \text{(differentiability of } G \text{ at } y\text{).} \tag{2}$$
> Because $d_x F$ is bounded and $r(h) = o(\lVert h\rVert)$, the increment $\eta(h) := F(x+h) - y = d_x F\, h + r(h)$ satisfies
> $$\lVert \eta(h)\rVert \le \lVert d_x F\rVert\,\lVert h\rVert + \lVert r(h)\rVert \le \big(\lVert d_x F\rVert + 1\big)\lVert h\rVert \quad\text{for } \lVert h\rVert \text{ small} \qquad \text{(triangle inequality; (1)).} \tag{3}$$
>
> **Step 1 — expand $G \circ F$ using (2) with $\eta = \eta(h)$.** Substituting $y + \eta(h) = F(x+h)$ into (2),
> $$ (G \circ F)(x + h) = G(y) + d_y G\,\eta(h) + s(\eta(h)) \qquad \text{(by (2)).}$$
> Insert $\eta(h) = d_x F\, h + r(h)$ from (1) and use linearity of $d_y G$:
> $$= G(y) + d_y G\, d_x F\, h + d_y G\, r(h) + s(\eta(h)) = (G\circ F)(x) + L h + \underbrace{d_y G\, r(h) + s(\eta(h))}_{=:\,\rho(h)} \qquad \text{(linearity of } d_y G;\ L = d_y G\, d_x F\text{).}$$
>
> **Step 2 — show the remainder $\rho(h)$ is $o(\lVert h\rVert)$.** We bound the two terms of $\rho(h)$ separately.
> - **First term.** $\lVert d_y G\, r(h)\rVert \le \lVert d_y G\rVert\,\lVert r(h)\rVert = \lVert d_y G\rVert \cdot o(\lVert h\rVert) = o(\lVert h\rVert)$ (boundedness of $d_y G$; (1)).
> - **Second term.** Given $\varepsilon > 0$, by (2) there is $\delta > 0$ with $\lVert s(\eta)\rVert \le \varepsilon' \lVert \eta\rVert$ whenever $\lVert \eta\rVert < \delta$, where $\varepsilon' := \varepsilon / (\lVert d_x F\rVert + 1)$. By (3), $\lVert \eta(h)\rVert < \delta$ once $\lVert h\rVert$ is small, and then
> $$\lVert s(\eta(h))\rVert \le \varepsilon'\lVert \eta(h)\rVert \le \varepsilon'\big(\lVert d_x F\rVert + 1\big)\lVert h\rVert = \varepsilon\,\lVert h\rVert \qquad \text{(estimate for } s;\ (3);\ \text{choice of } \varepsilon'\text{).}$$
> Since $\varepsilon > 0$ was arbitrary, $\lVert s(\eta(h))\rVert = o(\lVert h\rVert)$.
>
> Adding the two, $\lVert \rho(h)\rVert = o(\lVert h\rVert)$ (sum of two $o(\lVert h\rVert)$ terms).
>
> **Step 3 — read off the derivative.** Combining Steps 1 and 2, $(G\circ F)(x+h) = (G\circ F)(x) + Lh + o(\lVert h\rVert)$, so by the uniqueness corollary above $G \circ F$ is differentiable at $x$ with $d_x(G\circ F) = L = d_y G \circ d_x F$.
>
> **Step 4 — the $C^k$ statement.** The map $x \mapsto d_x(G \circ F)$ factors as
> $$x \longmapsto (d_{F(x)}G,\ d_x F) \longmapsto d_{F(x)}G \circ d_x F,$$
> where the first map is continuous (respectively $C^{k-1}$) as a pair because $dG \circ F$ and $dF$ are (using that $F$ is $C^0$, and inductively $C^{k-1}$, so $dG \circ F$ is $C^{k-1}$ by the inductive hypothesis applied to the composite $dG \circ F$), and the second map, composition $\operatorname{Hom}(Y, Z) \times \operatorname{Hom}(X, Y) \to \operatorname{Hom}(X, Z)$, $(B, A) \mapsto BA$, is bounded bilinear, hence smooth. A composite of a $C^{k-1}$ map with a smooth map is $C^{k-1}$ (by induction on $k$, the base case $k = 1$ being the continuity just shown), so $d(G \circ F)$ is $C^{k-1}$, that is $G \circ F$ is $C^k$. **Therefore** the composite of $C^k$ maps is $C^k$, and in particular the composite of smooth maps is smooth. $\blacksquare$

> [!note]- Corollary (complementedness is automatic in the three cases we use)
> **Statement.** A closed subspace $E_0$ of a Banach space $E$ is complemented (admits a closed complement) in each of the following cases: (a) $E$ is a Hilbert space; (b) $E_0$ is finite-dimensional; (c) $E_0$ has finite codimension. Consequently, when $\mathcal X$ is a Hilbert manifold, or when the modelling subspace $E_0$ of a submanifold is finite-dimensional or of finite codimension, the complementedness clause of "embedded submanifold" is automatically satisfied. In particular the kernel and a complement of the image of a [[Def - Fredholm Operator and Index|Fredholm operator]] always split.
>
> **Proof.** **Case (a): $E$ a Hilbert space.** By [[Thm - Orthogonal Decomposition|the orthogonal decomposition theorem]] — for a closed subspace $E_0$ of a Hilbert space, $E = E_0 \oplus E_0^\perp$ with $E_0^\perp = \{v : \langle v, w\rangle = 0 \ \forall w \in E_0\}$ closed — the orthogonal complement $E_0^\perp$ is a closed subspace and $E = E_0 \oplus E_0^\perp$ is a topological direct sum (the orthogonal projection onto $E_0$ is bounded, of norm $1$). So $E_0$ is complemented, with complement $E_0^\perp$.
>
> **Case (b): $E_0$ finite-dimensional.** Let $e_1, \dots, e_m$ be a basis of $E_0$. By the **Hahn–Banach theorem** (every bounded linear functional on a subspace of a normed space extends to a bounded linear functional on the whole space with the same norm) each coordinate functional $e_j^* : E_0 \to \mathbb R$, $\sum_i a_i e_i \mapsto a_j$ (bounded, since $E_0$ is finite-dimensional and all norms on it are equivalent), extends to a bounded functional $\lambda_j \in E^*$ with $\lambda_j(e_i) = \delta_{ij}$. ⚠️ [The Hahn–Banach extension theorem is used here and in Case (c). It is a standard, short (Zorn's-lemma) result, but the vault currently has no `Thm - Hahn-Banach Theorem` page to wikilink for its complete proof; a dedicated page is needed and this invocation is reported to the orchestrator. Our actual applications in this chapter are all in Hilbert spaces, where Case (a) alone suffices and no such extension is required.] Set $P := \sum_{j=1}^m \lambda_j(\cdot)\, e_j : E \to E$. Then $P$ is bounded (a finite sum of bounded functionals times fixed vectors), $P(e_i) = \sum_j \lambda_j(e_i) e_j = e_i$ so $P|_{E_0} = \mathrm{id}_{E_0}$ and $\operatorname{Im}P = E_0$, and $P^2 = P$ (since $P e_i = e_i$ and $\operatorname{Im}P = E_0$). Thus $P$ is a bounded projection onto $E_0$, and $E_1 := \ker P$ is a closed complement: $E = E_0 \oplus E_1$ (every $v = Pv + (v - Pv)$ with $Pv \in E_0$, $v - Pv \in \ker P$, and $E_0 \cap \ker P = 0$ because $P|_{E_0} = \mathrm{id}$).
>
> **Case (c): $E_0$ closed of finite codimension.** Let $\dim(E / E_0) = m < \infty$ and pick $v_1, \dots, v_m \in E$ whose images form a basis of the quotient $E / E_0$. Set $E_1 := \operatorname{span}\{v_1, \dots, v_m\}$, a finite-dimensional (hence closed, by case (b)'s norm-equivalence, so complete and closed) subspace. Then $E_0 + E_1 = E$ (their images span the quotient) and $E_0 \cap E_1 = 0$ (a nonzero element of $E_1$ has nonzero image in the quotient), so $E = E_0 \oplus E_1$ algebraically; the sum is topological because the projection $E \to E_1$ along $E_0$ has finite rank with the finitely many coordinates given by bounded functionals on $E / E_0$ pulled back to $E$ (the quotient map $E \to E/E_0$ is bounded since $E_0$ is closed). So $E_0$ is complemented by $E_1$.
>
> **Application.** A Fredholm operator $L : X \to Y$ has $\dim \ker L < \infty$ and $\operatorname{Im}L$ closed of finite codimension. By case (b), $\ker L$ is complemented in $X$; by case (c), $\operatorname{Im}L$ is complemented in $Y$. **Therefore** the splittings $X = \ker L \oplus X_1$ and $Y = \operatorname{Im}L \oplus Y_1$ demanded by the Kuranishi model and the regular value theorem always exist. $\blacksquare$

**Calibration check.** First, confirm that the product $\mathcal X \times \mathcal Y$ of Banach manifolds modelled on $E, E'$ is a Banach manifold modelled on $E \oplus E'$, with charts the products of charts and transition maps the products of transition maps (smooth because $(u, v) \mapsto (\phi(u), \psi(v))$ has derivative the block-diagonal $(d\phi, d\psi)$); this is what lets $G \times G \to G$ and $G \times \mathcal X \to \mathcal X$ even be phrased. Second, check that a constant map $F \equiv c$ has $d_x F = 0$ everywhere (the remainder $F(x+h) - F(x) - 0 = 0 = o(\lVert h\rVert)$) and a bounded linear map $F = L$ has $d_x F = L$ everywhere (the remainder $L(x+h) - Lx - Lh = 0$), so both are smooth. Third, verify that the definition of "smooth map between Banach manifolds" is independent of the charts chosen: if $\psi' \circ \Phi \circ \varphi'^{-1}$ is another local representative, it equals $(\psi' \circ \psi^{-1}) \circ (\psi \circ \Phi \circ \varphi^{-1}) \circ (\varphi \circ \varphi'^{-1})$, a composite of the given representative with two smooth transition maps, hence smooth by the chain rule — this is exactly the role the chain rule corollary plays.

---

# Unlocked by This

> [!tip] Fredholm map and its index *(from Gauge Theory X)*
> With smooth maps between Banach manifolds in hand, a smooth map is called a [[Def - Fredholm Map and Its Index|Fredholm map]] when its differential $d_x \Phi$ is a [[Def - Fredholm Operator and Index|Fredholm operator]] at every point; its index is locally constant, hence constant on each component. This is the central object of the chapter.

> [!tip] The Kuranishi model and the regular value theorem *(from Gauge Theory X)*
> The [[Thm - Inverse Function Theorem on Banach Spaces|inverse and implicit function theorems on Banach spaces]] — which need exactly the completeness and bounded-derivative structure defined here — give the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]] and hence [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the theorem that the preimage of a regular value is a finite-dimensional submanifold]]. The complementedness corollary above is what makes the splittings in those theorems legitimate.

> [!tip] The Sard–Smale theorem and genericity *(from Gauge Theory X)*
> Second countability, imposed here, is precisely the Lindelöf hypothesis under which [[Thm - Sard-Smale Theorem|the Sard–Smale theorem]] upgrades "regular values are locally residual" to "regular values are residual, hence dense in the target".

> [!tip] Slices and moduli spaces *(from Gauge Theory X)*
> A smooth action of a Banach Lie group, defined here, is the setting for [[Def - Infinitesimal Action and Local Slice|local slices]] and for the theorem that [[Thm - A Free Action with Slices has a Manifold Quotient|a free action admitting slices has a manifold quotient]].

> [!tip] The Seiberg–Witten configuration space *(from Gauge Theory XI)*
> The examples above — the affine space of Sobolev connections and the Sobolev gauge group — assemble into the [[Def - Sobolev Configuration Space and Gauge Group|configuration space and gauge group]] on which the Seiberg–Witten map is a smooth, gauge-equivariant Fredholm map between Hilbert manifolds.
