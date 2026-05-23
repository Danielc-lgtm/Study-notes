---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Coordinate Chart and Atlas"
  - "Def - Transition Function"
  - "Def - Topological Manifold"
tags: [geometry, differential-geometry]
---

# Notation

Throughout, $M$ is a topological $n$-manifold. An [[Def - Coordinate Chart and Atlas|atlas]] $\mathcal{A} = \{(U_\alpha, \varphi_\alpha)\}_{\alpha \in I}$ on $M$ is a collection of charts whose domains cover $M$. Two charts are **smoothly compatible** if their [[Def - Transition Function|transition function]] is a diffeomorphism (or the overlap is empty). For full notation see [[Differential Geometry I — Smooth Manifolds and Atlases]].

This is a compound page: it defines three interlocking notions — **smooth atlas**, **compatibility of atlases**, and **smooth structure** (equivalently maximal smooth atlas) — because they are introduced together and none is fully usable without the others.

---

# Axiom Motivation

We have a topological manifold $M$ with a [[Def - Coordinate Chart and Atlas|covering atlas]] of charts $\varphi_\alpha : U_\alpha \to \widehat{U}_\alpha \subseteq \mathbb{R}^n$, and we want to make calculus on $M$ well-defined. The argument of [[Def - Transition Function]] shows that calculus is consistent across overlapping charts precisely when the [[Def - Transition Function|transition functions]] $\varphi_\beta \circ \varphi_\alpha^{-1}$ are smooth. So the first natural condition on an atlas — promoting it from "an atlas" to "an atlas suitable for calculus" — is that every pair of charts be smoothly compatible. This defines a **smooth atlas**.

But now a subtle problem arises: many different smooth atlases can describe "the same calculus" on $M$. For example, take $\mathbb{R}^n$ with the single-chart atlas $\mathcal{A}_1 = \{(\mathbb{R}^n, \mathrm{id})\}$, and compare with $\mathcal{A}_2 = \{(B_1(x), \mathrm{id}|_{B_1(x)}) : x \in \mathbb{R}^n\}$, an atlas consisting of every unit ball with the identity (Lee, page 13). These are different atlases — different sets of charts — but a function $f : \mathbb{R}^n \to \mathbb{R}$ is smooth with respect to either one if and only if it is smooth in the ordinary sense of multivariable calculus. So $\mathcal{A}_1$ and $\mathcal{A}_2$ define the same notion of smoothness. The smooth structure on $\mathbb{R}^n$ should not depend on whether we cover with one chart or with infinitely many.

We need an equivalence relation that identifies $\mathcal{A}_1$ and $\mathcal{A}_2$. The right relation is: $\mathcal{A}_1 \sim \mathcal{A}_2$ iff $\mathcal{A}_1 \cup \mathcal{A}_2$ is *also* a smooth atlas — i.e., every chart of $\mathcal{A}_1$ is smoothly compatible with every chart of $\mathcal{A}_2$. This is reflexive (any atlas is compatible with itself) and symmetric (the compatibility condition is symmetric in the two charts). Transitivity requires a small argument: if $\mathcal{A}_1 \sim \mathcal{A}_2$ and $\mathcal{A}_2 \sim \mathcal{A}_3$, we need that any chart $(U, \varphi) \in \mathcal{A}_1$ is smoothly compatible with any chart $(W, \theta) \in \mathcal{A}_3$. The argument (Cascini Lemma 1.22): on a triple overlap, factor $\theta \circ \varphi^{-1} = (\theta \circ \psi^{-1}) \circ (\psi \circ \varphi^{-1})$ for some chart $(V, \psi) \in \mathcal{A}_2$ containing the point of interest; both factors are smooth by compatibility with $\mathcal{A}_2$, so the composition is smooth. Hence $\sim$ is an equivalence relation, and the equivalence classes are the candidate "smooth structures".

There is then a choice of formalism: a smooth structure is *either* (a) an equivalence class of smooth atlases under $\sim$, or (b) a *maximal* smooth atlas — a smooth atlas that contains every chart smoothly compatible with all its members. The two formulations are equivalent: each equivalence class has a unique maximal element (the union of all atlases in the class), and conversely each maximal atlas is the union of all atlases compatible with itself. We follow the *maximal atlas* convention because it is technically more convenient — checking whether a chart is in the smooth structure means checking smooth compatibility with one atlas of the class, not with every atlas in the equivalence class.

The motivation question that drives the rest of the chapter: how do we *specify* a smooth structure? The maximal atlas has uncountably many charts in general, so we cannot write it down directly. The answer is given by [[Thm - Smooth Structure from Maximal Atlas]]: every smooth atlas is contained in a *unique* maximal smooth atlas (Lee Proposition 1.17). So to specify a smooth structure, we specify *any* smooth atlas, and the maximal atlas is then determined uniquely. The two atlases $\mathcal{A}_1$ and $\mathcal{A}_2$ above specify the same smooth structure precisely because $\mathcal{A}_1 \cup \mathcal{A}_2$ is a smooth atlas.

This is also where [[Def - Dimension|dimension]] and analytical-class flexibility enter. By choosing different compatibility conditions on transition functions, one gets different categories of manifolds: $C^k$-compatibility gives $C^k$-manifolds; real-analytic ($C^\omega$) compatibility gives real-analytic manifolds; holomorphic compatibility (on charts to $\mathbb{C}^n$) gives complex manifolds. The smooth ($C^\infty$) case is the standard one, but the structural picture — atlas, compatibility, equivalence class, maximal atlas — is identical in all of them.

A final motivation: why insist on the *maximal* atlas, rather than just storing an equivalence class? The maximal-atlas formulation lets us talk about *the* smooth charts of $M$ unambiguously: a chart is "smooth" iff it lies in the maximal atlas, iff it is smoothly compatible with every chart of any given smooth atlas. This eliminates the bookkeeping of equivalence classes from later definitions ("a smooth function is one whose representation in every chart of the smooth structure is smooth", with no need to specify *which* atlas). It is the technically cleaner approach.

---

# The Definition

Let $M$ be a topological $n$-manifold.

**Smooth atlas.** A **smooth atlas** on $M$ is an atlas $\mathcal{A} = \{(U_\alpha, \varphi_\alpha)\}_{\alpha \in I}$ such that any two charts $(U_\alpha, \varphi_\alpha), (U_\beta, \varphi_\beta) \in \mathcal{A}$ are smoothly compatible — that is, either $U_\alpha \cap U_\beta = \emptyset$, or the [[Def - Transition Function|transition function]] $\varphi_\beta \circ \varphi_\alpha^{-1}$ is a [[Def - Diffeomorphism|diffeomorphism]] between the open subsets $\varphi_\alpha(U_\alpha \cap U_\beta)$ and $\varphi_\beta(U_\alpha \cap U_\beta)$ of $\mathbb{R}^n$.

**Compatibility of atlases.** Two smooth atlases $\mathcal{A}$ and $\mathcal{B}$ on $M$ are **compatible** (equivalently, **equivalent**) if $\mathcal{A} \cup \mathcal{B}$ is a smooth atlas — equivalently, every chart in $\mathcal{A}$ is smoothly compatible with every chart in $\mathcal{B}$. Compatibility is an equivalence relation on the set of smooth atlases on $M$ (reflexivity, symmetry, and transitivity all hold; transitivity is Cascini Lemma 1.22 or Lee Exercise 1.18).

**Maximal smooth atlas.** A smooth atlas $\mathcal{A}$ on $M$ is **maximal** (or **complete**) if it is not properly contained in any larger smooth atlas — equivalently, every chart that is smoothly compatible with every chart in $\mathcal{A}$ is already in $\mathcal{A}$.

**Smooth structure.** A **smooth structure** on $M$ is, equivalently:
- An equivalence class of compatible smooth atlases on $M$; or
- A maximal smooth atlas on $M$.

The equivalence of the two formulations is the content of [[Thm - Smooth Structure from Maximal Atlas]] (Lee Proposition 1.17): every smooth atlas $\mathcal{A}$ is contained in a *unique* maximal smooth atlas $\overline{\mathcal{A}}$, called the **smooth structure determined by $\mathcal{A}$**; and two smooth atlases determine the same smooth structure iff their union is a smooth atlas. In practice we usually specify a smooth structure by giving a representative smooth atlas (typically a small one), with the understanding that the maximal atlas is its uniquely determined extension.

A chart $(U, \varphi)$ is a **smooth chart** if it belongs to the maximal smooth atlas — equivalently, if it is smoothly compatible with every chart in some (equivalently every) smooth atlas representing the smooth structure.

**$C^k$ and other variants.** Replacing "$\varphi_\beta \circ \varphi_\alpha^{-1}$ is a diffeomorphism" with "$\varphi_\beta \circ \varphi_\alpha^{-1}$ and its inverse are $C^k$" gives the notion of a **$C^k$-atlas** and **$C^k$-structure** ($k \geq 0$). The $C^0$ case is just topological compatibility, recovering the topological manifold structure. Replacing $\mathbb{R}^n$ with $\mathbb{C}^n$ and "smooth" with "holomorphic" gives complex-analytic atlases and complex manifolds; real-analytic ($C^\omega$) atlases give real-analytic manifolds.

---

# Categorical / Structural Definition

A smooth atlas on $M$ is a coherent family of *local model identifications* $\varphi_\alpha : U_\alpha \to \widehat{U}_\alpha$, where coherence is encoded by the cocycle condition on transition functions and the smoothness of those transitions. Categorically, a smooth atlas is a *trivializing cover of $M$ in the pseudogroup of local [[Def - Diffeomorphism|diffeomorphisms]] of $\mathbb{R}^n$* — that is, $M$ is locally isomorphic to $\mathbb{R}^n$ via charts whose composition (transition function) is a morphism in the diffeomorphism pseudogroup.

The maximal smooth atlas is then the *germ* of this data: the union of all locally isomorphic trivializations, equivalent to the *sheaf of smooth coordinate systems* on $M$. The associated structure sheaf is the **sheaf of smooth functions** $C^\infty_M$, which assigns to each open $U \subseteq M$ the $\mathbb{R}$-algebra $C^\infty(U)$ of smooth functions; a smooth manifold is recovered from this sheaf, since the maximal atlas can be read off from it.

In sheaf-theoretic language: a smooth manifold is a locally ringed space $(M, C^\infty_M)$ such that, locally, $(M, C^\infty_M)$ is isomorphic to $(\widehat{U}, C^\infty_{\widehat{U}})$ for some open $\widehat{U} \subseteq \mathbb{R}^n$. The smooth structure is the entire $C^\infty_M$ sheaf, and a "smooth atlas" is a finite or countable collection of charts witnessing the local-isomorphism property.

This perspective makes the smooth-structure construction look identical to the construction of schemes (locally ringed spaces locally isomorphic to $(\mathrm{Spec}\, A, \mathcal{O}_{\mathrm{Spec}\, A})$), complex manifolds (locally isomorphic to $(\widehat{U}, \mathcal{O}^{\mathrm{hol}}_{\widehat{U}})$ with $\widehat{U} \subseteq \mathbb{C}^n$), and $C^k$-manifolds (replacing the smooth sheaf with the $C^k$ sheaf). The chart-and-atlas formalism is just an explicit witness for the local-isomorphism property; the smooth structure as a maximal atlas, or equivalently as a sheaf, is the genuinely intrinsic datum.

A morphism of smooth manifolds $f : (M, C^\infty_M) \to (N, C^\infty_N)$ is a morphism of locally ringed spaces — a continuous map $f : M \to N$ together with a sheaf homomorphism $f^* : C^\infty_N \to f_* C^\infty_M$. This is exactly a **smooth map** in the conventional sense (developed in [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]]).

---

# Relate to Other Fields / Compression

**True name:** A smooth structure on $M$ is "an equivalence class of compatible atlases, equivalently a maximal smooth atlas, equivalently the sheaf of smooth functions on $M$." Whenever you need to verify "$M$ has smooth structure $\mathcal{S}$", you produce an atlas representing $\mathcal{S}$ and check smooth compatibility; whenever you need to use $\mathcal{S}$, you may invoke any smoothly compatible chart and treat it as belonging to $\mathcal{S}$.

In **algebraic geometry**, the analogue is the **structure sheaf** $\mathcal{O}_X$ of a scheme $X$. A scheme is a topological space equipped with the sheaf of *regular functions*, locally isomorphic to the sheaf of regular functions on an affine scheme $\mathrm{Spec}\, A$. The "atlas" is the choice of affine open cover, and the "smooth atlas / smooth structure" is the sheaf $\mathcal{O}_X$ on the entire scheme. The bridge: $C^\infty_M$ for smooth manifolds is the differential-geometric analogue of $\mathcal{O}_X$ for schemes, and many constructions transfer (cohomology, derived categories, deformation theory).

In **physics**, a smooth structure on spacetime is a choice of "what counts as a smooth field configuration" — the equations of general relativity, Yang–Mills theory, and the Standard Model are formulated as PDEs *in* the smooth structure, and the structure is part of the kinematic setup of the theory. The smoothness class can be relaxed in low regularity (e.g., distributional solutions in shock-wave general relativity), but the underlying smooth manifold structure of spacetime is the default arena.

In **dynamical systems and ergodic theory**, the smooth structure of phase space is what makes "flow" mean a smooth one-parameter family of diffeomorphisms — see [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]]. Without a smooth structure, the flow of a vector field cannot be defined; with a $C^0$-only structure, only continuous flow makes sense.

In **representation theory** of Lie groups, every Lie group $G$ is a smooth manifold; representations are smooth homomorphisms $G \to \mathrm{GL}(V)$. The smooth structure on $G$ is what allows the **exponential map** and the Lie algebra to be defined — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]].

---

# Examples / Corollaries

**Is an instance: the standard smooth structure on $\mathbb{R}^n$.** The single chart $\{(\mathbb{R}^n, \mathrm{id})\}$ is a smooth atlas (vacuously, since there is only one chart). It determines the **standard smooth structure** on $\mathbb{R}^n$, and the maximal atlas consists of *all* charts $(U, \varphi)$ such that $\varphi : U \to \widehat{U}$ is a diffeomorphism in the ordinary calculus sense. This is the structure used throughout calculus.

**Is an instance: the standard smooth structure on $S^n$.** The two-chart stereographic atlas (Lee Problem 1-7, see [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]]) is a smooth atlas, with the transition function $u \mapsto u/|u|^2$ on $\mathbb{R}^n \setminus \{0\}$ being smooth. It determines a smooth structure on $S^n$, the **standard smooth structure**. The graph-coordinate atlas (Lee Example 1.4) determines the same smooth structure — the two atlases are compatible. This equivalence is precisely what [[Ex - Compatibility of Two Atlases on the Sphere]] proves.

**Is an instance: the standard smooth structure on $\mathbb{RP}^n$.** The $(n+1)$-chart affine atlas (see [[Ex - Real Projective Space is a Smooth Manifold]]) is smooth, with rational transition functions. It determines the standard smooth structure.

**Is an instance: smooth structures on products.** If $(M_i, \mathcal{A}_i)$ are smooth manifolds, the product atlas $\{(U_\alpha \times V_\beta, \varphi_\alpha \times \psi_\beta) : (U_\alpha, \varphi_\alpha) \in \mathcal{A}_1, (V_\beta, \psi_\beta) \in \mathcal{A}_2\}$ is smooth on $M_1 \times M_2$. See [[Thm - Product of Smooth Manifolds is a Smooth Manifold]].

**Is an instance: the non-standard smooth structure on $\mathbb{R}$.** The chart $\psi(x) = x^3$ defines a smooth atlas $\{(\mathbb{R}, \psi)\}$ that is *not* compatible with the standard one (Lee Example 1.23): the transition function from standard to $\psi$ is $y \mapsto y^{1/3}$, not smooth at $0$. So $(\mathbb{R}, \psi)$ and $(\mathbb{R}, \mathrm{id})$ define two distinct smooth structures on the same topological manifold $\mathbb{R}$. They are, however, diffeomorphic via the map $x \mapsto x^3$ (which is a [[Def - Homeomorphism|homeomorphism]] in standard coordinates, hence a chart change, but is a *diffeomorphism* between the two smooth structures — see [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]]). The lesson: there can be multiple smooth structures on a topological manifold that are diffeomorphic to each other but distinct as smooth structures.

**Is an instance (deep): exotic smooth structures on $\mathbb{R}^4$.** Donaldson and Freedman showed that $\mathbb{R}^4$ admits uncountably many distinct smooth structures, no two diffeomorphic to each other. (For $n \neq 4$, $\mathbb{R}^n$ has a unique smooth structure up to diffeomorphism.) This is one of the most remarkable phenomena in differential topology and is invisible from this chapter's elementary perspective.

**Is NOT an instance: an atlas with one smooth and one non-smooth-compatible chart.** Take $\mathbb{R}$ with the atlas $\{(\mathbb{R}, \mathrm{id}), (\mathbb{R}, x \mapsto x^3)\}$. The transition function $y \mapsto y^{1/3}$ is not smooth at $0$, so the *atlas* is not smooth — even though each individual chart is a [[Def - Homeomorphism|homeomorphism]]. This atlas defines no smooth structure; to extract a smooth structure, one must drop one of the two charts.

**Is NOT an instance: a "smooth structure" defined by a non-Hausdorff topological manifold.** The line with two origins admits charts and overlap maps that are smooth, but the *space* is not Hausdorff, so the topological-manifold hypothesis fails before we even reach the smooth-structure question. Lee Problem 1-1 shows this is a real pathology.

**Corollary (Lee Exercise 1.18: union and identification).** Two smooth atlases $\mathcal{A}, \mathcal{B}$ determine the same smooth structure iff $\mathcal{A} \cup \mathcal{B}$ is a smooth atlas. This is the practical compatibility test: to show two atlases give the same smooth structure, check pairwise smooth compatibility of charts across the two atlases.

**Corollary (existence of a global single chart).** A topological manifold admits a single-chart smooth atlas iff it is homeomorphic to an open subset of $\mathbb{R}^n$. In particular, $\mathbb{R}^n$ admits a single global chart, but no compact manifold (and in particular no $S^n$ for $n \geq 1$) does.

**Corollary (every topological manifold admitting a smooth structure admits many smooth atlases).** Given a smooth structure $\overline{\mathcal{A}}$, every nonempty subatlas $\mathcal{A}_0 \subseteq \overline{\mathcal{A}}$ that covers $M$ is itself a smooth atlas determining the same smooth structure (since $\overline{\mathcal{A}_0} = \overline{\mathcal{A}}$ by maximality).

**Corollary (smooth structures may differ on the same maximal atlas).** This is *false*: the maximal atlas determines the smooth structure uniquely. The previous corollary clarifies the right statement: different sub-atlases can witness the same smooth structure.

**Calibration check.** Compute the transition function for the change of chart from $(\mathbb{R}^2, \mathrm{id})$ to the polar chart $\psi(r, \theta) = (r\cos\theta, r\sin\theta)$ on its domain, and verify smoothness on the domain where $r > 0$ (so it lies in the standard smooth structure of $\mathbb{R}^2 \setminus \{0\}$). Verify that the trivial 0-dimensional manifold $\{*\}$ admits exactly one smooth structure (the one chart $\varphi : \{*\} \to \mathbb{R}^0$). Verify that the disjoint union of two copies of $\mathbb{R}$ admits a unique smooth structure compatible with the standard structures on each copy.

---

# Unlocked by This

> [!tip] Smooth Manifold *(this chapter)*
> A topological manifold equipped with a smooth structure is a [[Def - Smooth Manifold|smooth manifold]] — the central object of differential geometry. The smooth structure is the *data* that distinguishes a smooth manifold from a topological one, and the rest of the subject is built upon this data.

> [!tip] Smooth Maps and the Category of Smooth Manifolds *(from [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]])*
> Once smooth structures are in place, the morphisms of the smooth-manifold category are **smooth maps**: a map $f : M \to N$ is smooth iff its representation $\psi \circ f \circ \varphi^{-1}$ in any pair of charts is smooth in the ordinary sense. Smoothness is now a well-defined property thanks to the chart-compatibility built into the smooth atlas.

> [!tip] Sheaf of Smooth Functions and the Structure-Sheaf Picture *(from Algebraic Geometry / Differential Geometry)*
> A smooth structure can be recovered from the **sheaf of smooth functions** $C^\infty_M$, which assigns to each open $U \subseteq M$ the algebra $C^\infty(U)$. This is the structural perspective: a smooth manifold is a locally ringed space locally isomorphic to $(\mathbb{R}^n, C^\infty_{\mathbb{R}^n})$, exactly paralleling scheme theory.

> [!tip] Geometric Structures *(from Cartan/Klein Geometry)*
> Replacing the compatibility "diffeomorphism" with a more restrictive class — orientation-preserving, isometric (Riemannian), holomorphic, symplectic — produces other **geometric structures** on $M$. The smooth structure is the maximally flexible base case; every other geometric structure can be viewed as a reduction of the structure group of the transition functions.

> [!tip] Exotic Smooth Structures *(from Differential Topology)*
> A topological manifold can admit multiple smooth structures, even multiple smooth structures that are not diffeomorphic to each other. Milnor's **exotic 7-spheres** (28 distinct smooth structures on $S^7$) and Donaldson's **exotic $\mathbb{R}^4$'s** (uncountably many smooth structures on the topological $\mathbb{R}^4$) are the marquee examples. The existence of exotic structures is one of the most surprising phenomena in mathematics.
