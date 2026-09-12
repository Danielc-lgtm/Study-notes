---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - The Hopf Bundle"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Def - Homotopy"
  - "Def - Homotopy Equivalence and Contractible Space"
  - "Def - Characteristic Class"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a compact Lie group and $M$ a smooth manifold. We write $E \to B$ for a [[Def - Principal G-Bundle|principal G-bundle]] with total space $E$ and base $B$, and $P \to M$ for the principal $G$-bundle we wish to classify. For a continuous map $f\colon M \to B$, $f^*E \to M$ denotes the [[Def - Operations on Vector Bundles and Pull-Back Bundles|pull-back bundle]], whose total space is $f^*E = \{(m, e) \in M \times E : f(m) = \pi_E(e)\}$ with projection $(m,e) \mapsto m$. We write $[M; B]$ for the set of homotopy classes of continuous maps $M \to B$; two maps $f_0, f_1$ lie in the same class when they are [[Def - Homotopy|homotopic]], written $f_0 \simeq f_1$. For a real inner-product space we use $\lVert \cdot \rVert$ for the Euclidean norm.

The group $U(1) = \{\lambda \in \mathbb{C} : |\lambda| = 1\}$ acts on $\mathbb{C}^{n}$ coordinatewise, $\lambda \cdot (z_0, \dots, z_{n-1}) = (\lambda z_0, \dots, \lambda z_{n-1})$. We write $\mathbb{H}$ for the quaternions, $Sp(1) = \{q \in \mathbb{H} : q\bar q = |q|^2 = 1\}$ for the unit quaternions (the compact symplectic group in rank one), and $\mathbb{HP}^n$ for quaternionic projective space. Following the source we use the explicit isomorphism $Sp(1) \xrightarrow{\;\cong\;} SU(2)$, $q = z + wj \mapsto \begin{pmatrix} z & w \\ -\bar w & \bar z \end{pmatrix}$, proved on [[Ex - SU(2) is the Group of Unit Quaternions]]; the two names $Sp(1)$ and $SU(2)$ are used interchangeably.

The sphere $S^m \subset \mathbb{R}^{m+1}$ is the unit sphere. We use the complex identification $S^{2N+1} = \{z \in \mathbb{C}^{N+1} : \lVert z \rVert = 1\}$ (so $\mathbb{C}^{N+1} = \mathbb{R}^{2N+2}$ and $m = 2N+1$) and the quaternionic identification $S^{4N+3} = \{h \in \mathbb{H}^{N+1} : \lVert h \rVert = 1\}$ (so $\mathbb{H}^{N+1} = \mathbb{R}^{4N+4}$ and $m = 4N+3$).

**Standing convention (right actions).** Principal bundles in this series carry a *right* $G$-action; $R_g(p) = p \cdot g$. The scalar action of $U(1)$ on $\mathbb{C}^{N+1}$ above is written on the left but is abelian, so left and right coincide; the quaternionic action of the non-abelian group $Sp(1)$ on $\mathbb{H}^{N+1}$ is taken to be right scalar multiplication, $(h_0, \dots, h_N) \cdot q = (h_0 q, \dots, h_N q)$, exactly so that it is a right action.

> [!warning] Convention: category and cohomology
> The source (Haydys §2.4) works in the **topological** category — continuous maps, topological principal bundles, and singular cohomology $H^\bullet(-; R)$ with a coefficient ring $R$. This series keeps $M$, $B$, and all classifying maps **smooth** wherever they are used concretely (the spaces $\mathbb{CP}^N$, $\mathbb{HP}^N$, $M$ are smooth manifolds), and it takes the cohomology of $B$ to be **de Rham cohomology** $H^\bullet_{dR}(B)$, consistently with the coordinator's decision to work with de Rham classes and the group $\operatorname{Pic}(M)$ until singular cohomology is built in chapter XII. The one-line dictionary: where the source writes $c \in H^\bullet(B; \mathbb{R})$ and $f^*c \in H^\bullet(M; \mathbb{R})$ with singular cohomology, we read $c \in H^\bullet_{dR}(B)$ and $f^*c \in H^\bullet_{dR}(M)$ with the de Rham pull-back. The two agree under the de Rham isomorphism, a comparison this series does not make and does not need.

This is a compound page: it defines four interlocking notions — a **classifying bundle** for $G$, its **classifying space** $B$, the **classifying map** of a given bundle, and the **characteristic class** $f^*c$ it induces — together with the two explicit classifying bundles $S^\infty \to \mathbb{CP}^\infty$ (for $U(1)$) and $S^\infty \to \mathbb{HP}^\infty$ (for $Sp(1)$). They belong on one page because the classifying map is meaningless without the classifying bundle it maps into, and the characteristic class is exactly what one reads off a classifying map; the concrete spaces are the only two cases this series constructs by hand.

---

# Axiom Motivation

We have spent this chapter building principal $G$-bundles one at a time — the [[Def - The Hopf Bundle|Hopf bundle]], [[Def - Frame Bundle of a Vector Bundle|frame bundles]], bundles reconstructed from [[Def - Transition Functions and the Cocycle Condition|cocycles]]. The organising question of the subject is the opposite of construction: **given a base $M$ and a group $G$, what are all the principal $G$-bundles over $M$, up to isomorphism?** We want a single space or a single invariant that sees every bundle at once. The classifying-bundle construction answers this by turning the classification problem into a homotopy problem, and the definition below is forced by asking what such a universal object must satisfy.

The desideratum is a *universal* principal $G$-bundle $E \to B$: one so large that every principal $G$-bundle $P \to M$ over every manifold is a [[Def - Operations on Vector Bundles and Pull-Back Bundles|pull-back]] $f^*E$ of it along some map $f\colon M \to B$, and so that the map $f$ is determined up to homotopy by the isomorphism class of $P$. If such an $E \to B$ exists, then isomorphism classes of bundles over $M$ are in bijection with homotopy classes $[M; B]$, and the entire classification is transported to the homotopy theory of the fixed space $B$. Two properties of $E$ turn out to be exactly what is needed, and we can see why each is required by asking what fails when it is dropped.

**Why $E$ must be contractible.** Suppose $E$ classifies every bundle universally. Take $M = E$ itself and the bundle $E \to B$ (with $M = E$, the map is $\pi_E$). The identity bundle $E \to E$ is classified by some $f\colon E \to B$; but $E \to E$ is trivial (it has the tautological global section, the identity), and a trivial bundle is classified by a constant map (a trivial bundle is the pull-back of $E$ along any map factoring through a point, since the pull-back of anything along a constant is trivial). Consistency of "the classifying map is unique up to homotopy" then forces $\pi_E \colon E \to B$ to be homotopic to a constant, which pushes all the topology of $E$ into $B$ and leaves $E$ with no homotopy of its own. Concretely: if $E$ had a non-trivial homotopy group $\pi_k(E) \neq 0$, then a $k$-sphere inside $E$ could detect a bundle over $S^k$ that is not seen from $B$, and universality would fail in dimension $k$. The clean condition that kills every homotopy group of $E$ at once is that $E$ be **contractible** — its identity map is homotopic to a constant. A contractible $E$ carries no bundle information of its own, so all of it lives on $B$, where we can read it.

**Why the $G$-action must be free.** For $E \to B := E/G$ to be a principal $G$-bundle at all, the fibres must be single $G$-orbits on which $G$ acts simply transitively; a principal action is in particular [[Def - Free, Transitive, Effective, and Proper Group Actions|free]] (no non-identity element fixes a point). If the action had a fixed point $e_0$ with stabiliser $H \neq \{1\}$, the orbit through $e_0$ would be $G/H$, not a copy of $G$, and $E \to E/G$ would fail to be a principal $G$-bundle near $e_0$ — the "fibre" there would be too small. So freeness is not decoration; it is the precondition for the quotient map to be a principal bundle in the first place. Together with contractibility this is the whole definition.

**Why $G$ is required to be compact.** For the quotient map $E \to E/G$ to be a genuine principal bundle we need the action to be not only free but [[Def - Free, Transitive, Effective, and Proper Group Actions|proper]], so that $E/G$ is Hausdorff and the local product structure exists. A free action of a *compact* group is automatically proper, because the map $G \times E \to E \times E$, $(g, e) \mapsto (g \cdot e, e)$, has compact-fibred, closed image when $G$ is compact. This is precisely why the definition restricts to compact Lie groups $G$: it is the hypothesis under which "free" upgrades to "principal quotient" for free.

**Why characteristic classes, and not $[M; B]$ directly** (source Remark following Theorem 70; item $R2.4.4$). Even granting universality, the set $[M; B]$ of homotopy classes is usually intractable to compute — it is a homotopy-theoretic object with no linear structure and no obvious invariants. The way out is to push a fixed cohomology class $c$ on the fixed space $B$ forward to $M$ through the classifying map: $f \mapsto f^*c$. Cohomology is computable (it has Mayer–Vietoris, it is a group, it is a ring), and $f^*c$ depends only on the homotopy class of $f$, hence only on the bundle. So characteristic classes are the *computable shadow* of the intractable set $[M; B]$: they lose information in general, but they are the invariants one can actually evaluate, and for the two groups treated below they turn out to be complete.

If a reader accepts that the goal is to represent bundles as pull-backs of one universal bundle, the two clauses "contractible" and "free" are the minimal conditions making that possible, and the characteristic-class construction is the obvious way to extract computable numbers from the resulting map. The definition can be reinvented from these desiderata.

---

# The Definition

**Classifying bundle and classifying space** (source Definition 69; item $D2.4.1$). Let $G$ be a compact Lie group. A topological space $E$ equipped with a continuous $G$-action is a **classifying bundle for $G$** if

1. $E$ is [[Def - Homotopy Equivalence and Contractible Space|contractible]], and
2. the $G$-action on $E$ is [[Def - Free, Transitive, Effective, and Proper Group Actions|free]].

Setting $B := E/G$, the quotient map $\pi\colon E \to B$ is a principal $G$-bundle (the action of the compact group $G$ is free, hence proper, so the quotient is a principal bundle by the reduction to [[Def - Free, Transitive, Effective, and Proper Group Actions|proper free actions]]). The base $B$ is called the **classifying space** for $G$.

**Classifying map.** Let $P \to M$ be a principal $G$-bundle. A **classifying map** for $P$ is a continuous map $f\colon M \to B$ together with an isomorphism $P \cong f^*E$ of principal $G$-bundles. We say $f$ *classifies* $P$.

**Characteristic class** (source Definition 71; item $D2.4.2$). Let $f\colon M \to B$ be a smooth map and let $c \in H^\bullet_{dR}(B)$ be a de Rham cohomology class of the classifying space. The **characteristic class** of the bundle $f^*E \to M$ determined by $c$ is
$$
f^*c \;\in\; H^\bullet_{dR}(M),
$$
the image of $c$ under the pull-back $f^* \colon H^\bullet_{dR}(B) \to H^\bullet_{dR}(M)$ on de Rham cohomology. The naturality established in the Examples section shows that $f^*c$ depends only on the homotopy class of $f$, hence only on the bundle $f^*E$.

**The classifying bundle for $U(1)$** (source, item $D2.4.3$). Consider the tower of $U(1)$-equivariant inclusions
$$
S^1 \hookrightarrow S^3 \hookrightarrow S^5 \hookrightarrow \cdots \hookrightarrow S^{2N+1} \hookrightarrow \cdots, \qquad
(z_0, \dots, z_{N}) \mapsto (z_0, \dots, z_{N}, 0),
$$
each covering the inclusion $\mathbb{CP}^N \hookrightarrow \mathbb{CP}^{N+1}$, $[z_0 : \cdots : z_N] \mapsto [z_0 : \cdots : z_N : 0]$ (source Remark, item $R2.4.2$: the commutative ladder of spheres over projective spaces). The **direct limit** (union with the weak topology) is
$$
S^\infty \;:=\; \varinjlim_N S^{2N+1}, \qquad
\mathbb{CP}^\infty \;:=\; \varinjlim_N \mathbb{CP}^N,
$$
and $S^\infty \to \mathbb{CP}^\infty$ is the classifying bundle for $U(1)$. Explicitly, as a set
$$
S^\infty = \Big\{(z_0, z_1, z_2, \dots) : z_i \in \mathbb{C},\ z_i = 0 \text{ for all but finitely many } i,\ \textstyle\sum_i |z_i|^2 = 1 \Big\},
$$
carrying the **weak (colimit) topology**: a subset $C \subseteq S^\infty$ is closed if and only if $C \cap S^{2N+1}$ is closed in $S^{2N+1}$ for every $N$. The freeness of the $U(1)$-action and the contractibility of $S^\infty$ are verified in the Examples section; the quotient at each finite stage is $S^{2N+1}/U(1) = \mathbb{CP}^N$ (this is the higher [[Def - The Hopf Bundle|Hopf bundle]], see [[Def - Complex Projective Space as a Quotient]]), so $S^\infty/U(1) = \mathbb{CP}^\infty$.

**The classifying bundle for $Sp(1) \cong SU(2)$** (source, item $D2.4.6$). The unit quaternions $Sp(1)$ act freely on the unit sphere of $\mathbb{H}^{N+1}$ by right scalar multiplication,
$$
S^{4N+3} = \Big\{(h_0, \dots, h_N) \in \mathbb{H}^{N+1} : \textstyle\sum_i |h_i|^2 = 1\Big\}, \qquad
(h_0, \dots, h_N) \cdot q = (h_0 q, \dots, h_N q),
$$
giving principal $Sp(1)$-bundles $S^{4N+3} \to \mathbb{HP}^N$. (In the source's display the sphere is printed as $\{(h_0, \dots, h_n) \in \mathbb{H}^n : \sum |h_i|^2 = 1\}$; there are $n+1$ coordinates, so the corrected ambient space is $\mathbb{H}^{n+1}$, as written here.) The tower $S^7 \hookrightarrow S^{11} \hookrightarrow \cdots$ over $\mathbb{HP}^1 \hookrightarrow \mathbb{HP}^2 \hookrightarrow \cdots$ (item $R2.4.2$, quaternionic half) has direct limit $S^\infty \to \mathbb{HP}^\infty$, the classifying bundle for $Sp(1)$.

> [!warning] Convention: the definition of $[M; \mathbb{CP}^\infty]$
> For a compact manifold $M$ this series **defines**
> $$[M; \mathbb{CP}^\infty] \;:=\; \varinjlim_N\, [M; \mathbb{CP}^N]$$
> as the direct limit of the sets of homotopy classes of maps into the finite projective spaces, along the maps induced by the inclusions $\mathbb{CP}^N \hookrightarrow \mathbb{CP}^{N+1}$. We take this as the definition precisely so that no theorem about compact subsets of an infinite-dimensional direct-limit space is needed: every map from a compact $M$ into $\mathbb{CP}^\infty$ that we ever use, and every homotopy between such maps, has image in a finite stage $\mathbb{CP}^N$, and the direct-limit set records exactly these. For a reader who prefers the CW-theoretic viewpoint, this agrees with the set of homotopy classes of maps into the CW-complex $\mathbb{CP}^\infty$ (because a compact set meets only finitely many cells); we do not use this agreement. The same convention defines $[M; \mathbb{HP}^\infty] := \varinjlim_N [M; \mathbb{HP}^N]$.

> [!note] Scope remarks (not proved and not used in this series)
> The following facts from the source are stated for orientation only. They are never proved here, never wikilinked, and no argument in the series leans on them.
> - **Existence of a classifying bundle for every compact Lie group $G$** (source Theorem/remark, items $I2.4.1$–$I2.4.2$): one construction is Milnor's infinite join $E = G * G * G * \cdots$, which is contractible and carries a free $G$-action. This series constructs the classifying bundle *by hand* only for $U(1)$ and $Sp(1)$, the two cases needed.
> - **The general classification theorem** (source Theorem 70, items $I2.4.1$, $I2.4.2$): for every compact $G$ and every manifold $M$, $f \mapsto f^*E$ is a bijection from isomorphism classes of principal $G$-bundles over $M$ onto $[M; B]$. The series proves the analogous statement only for $G = U(1)$ and $G = Sp(1)$, on [[Thm - Line Bundles over Compact Manifolds are Pulled Back from Projective Space]] and the two classification pages below.
> - **The CW structure of $\mathbb{CP}^\infty$ and $\mathbb{HP}^\infty$** (item $I2.4.3$, remaining half): $\mathbb{CP}^\infty$ has one cell in each even dimension and $\mathbb{HP}^\infty$ one cell in each dimension divisible by four.
> - **The infinite Grassmannian $\operatorname{Gr}_k(\mathbb{C}^\infty)$ as the classifying space for $U(k)$** (source Remark 91, item $I3.1.5$): Chern classes of a rank-$k$ complex bundle can be defined as pull-backs of universal classes on $\operatorname{Gr}_k(\mathbb{C}^\infty)$.

---

# Categorical / Structural Definition

The classifying bundle has a clean universal-property reading that explains the word "classifying". Fix $G$ compact and let $\mathbf{Bun}_G$ denote the functor sending a manifold $M$ to the *set* $\mathbf{Bun}_G(M)$ of isomorphism classes of principal $G$-bundles over $M$, and sending a map $h\colon M' \to M$ to the pull-back operation $h^* \colon \mathbf{Bun}_G(M) \to \mathbf{Bun}_G(M')$. This is a contravariant functor from manifolds to sets, because pull-back is functorial: $(\mathrm{id})^* = \mathrm{id}$ and $(f \circ h)^* = h^* \circ f^*$ up to natural isomorphism of bundles.

A classifying bundle $E \to B$ makes this functor **representable**: the assignment
$$
[M; B] \;\longrightarrow\; \mathbf{Bun}_G(M), \qquad [f] \;\longmapsto\; [f^*E],
$$
is a natural transformation from the homotopy-classes functor $[-\,; B]$ to $\mathbf{Bun}_G$, and the general classification theorem (a scope remark above) asserts it is a natural *isomorphism*. In this language $B$ is a representing object for $\mathbf{Bun}_G$ on the homotopy category, and $E \to B$ is the *universal* bundle: it is the value of the identity of $B$, and every bundle is obtained from it by a unique-up-to-homotopy pull-back. Naturality is the statement, proved below in the concrete cases, that pulling a bundle back along $h\colon M' \to M$ corresponds to precomposing the classifying map with $h$.

The characteristic-class construction is then the composite of two natural transformations: represent the bundle as a homotopy class $[f]$, then apply the fixed cohomology class $c \in H^\bullet_{dR}(B)$ via $f \mapsto f^*c$. Because $H^\bullet_{dR}(-)$ is itself a contravariant functor and $f \mapsto f^*c$ is natural in $M$, the characteristic class $P \mapsto (\text{class of } f^*c)$ is a natural transformation $\mathbf{Bun}_G \Rightarrow H^\bullet_{dR}(-)$ — a rule assigning to every $G$-bundle a cohomology class of its base, compatibly with pull-back. This is the structural content of the phrase "characteristic class": it is exactly a natural transformation from the bundle functor to a cohomology functor.

---

# Relate to Other Fields / Compression

The classifying space is one instance of **representability**, the pervasive idea that a functor "$M \mapsto \{\text{structures of a given kind on } M\}$" is often computed by mapping into a single fixed space. Complex line bundles are classified by $\mathbb{CP}^\infty$; real line bundles by $\mathbb{RP}^\infty$; rank-$k$ complex bundles by the Grassmannian $\operatorname{Gr}_k(\mathbb{C}^\infty)$; and, in the topological setting, singular cohomology $H^n(-; A)$ is itself represented by the Eilenberg–MacLane space $K(A, n)$, so a degree-$n$ cohomology class *is* a homotopy class of maps into $K(A, n)$. The characteristic-class construction $f \mapsto f^*c$ is the shadow this representability casts on cohomology, and it is the origin of Chern, Pontryagin, Euler, and Stiefel–Whitney classes: each is $f^*$ of a fixed generator on the appropriate classifying space. The general fact that a reasonable contravariant homotopy functor is representable is **Brown representability**, a scope-level statement this series does not use.

There is a second compression through group cohomology. The classifying space $B = E/G$ of a classifying bundle is exactly the space one writes $BG$ in topology, and its cohomology $H^\bullet(BG)$ is the cohomology of the group $G$ in the topological sense. For $G = U(1)$ this is $H^\bullet(BG) = H^\bullet(\mathbb{CP}^\infty)$, a polynomial ring on one degree-two generator, computed in de Rham form on [[Thm - The de Rham Cohomology of Complex Projective Space]]; for $G = Sp(1)$ it is a polynomial ring on one degree-four generator. So "characteristic classes of $G$-bundles" and "the cohomology of $BG$" are the same data, and building a bundle's classifying map is the geometric act of evaluating the group's cohomology on that bundle.

**True name.** Operationally, a classifying bundle for $G$ is *the universal principal $G$-bundle*: the single bundle from which every $G$-bundle is pulled back, distinguished among all $G$-bundles by having a contractible total space. The axiomatic notion of a characteristic class — a natural assignment of a cohomology class to each bundle, satisfying naturality and (for Chern classes) a normalisation and Whitney formula — is developed on [[Def - Characteristic Class]]; the present construction $f \mapsto f^*c$ is the concrete source of every such assignment.

---

# Examples / Corollaries

**Is an instance — $S^\infty \to \mathbb{CP}^\infty$ classifies $U(1)$.** We verify the two defining clauses.

*The $U(1)$-action is free.* Let $z = (z_0, z_1, \dots) \in S^\infty$ and $\lambda \in U(1)$ with $\lambda \cdot z = z$. Since $z$ is a unit vector, some coordinate $z_j \neq 0$; the $j$-th coordinate of $\lambda \cdot z = z$ reads $\lambda z_j = z_j$, so $\lambda = 1$ (dividing by $z_j \neq 0$). Hence no non-identity element of $U(1)$ fixes any point, and the action is free.

*The total space $S^\infty$ is contractible.* This is the one substantial computation on the page, so we isolate it.

> [!note]- Corollary (verified): $S^\infty$ is contractible
> **Goal.** We show that the identity map of $S^\infty$ is [[Def - Homotopy|homotopic]] to a constant map; by definition of [[Def - Homotopy Equivalence and Contractible Space|contractibility]] this makes $S^\infty$ contractible. We work with the real direct-limit sphere and specialise afterwards.
>
> **Step 0 — the space, its topology, and cofinality.** Let $\mathbb{R}^{(\infty)} = \{x = (x_0, x_1, \dots) : x_i \in \mathbb{R},\ x_i = 0 \text{ for all but finitely many } i\}$ with the standard inner product $\langle x, y \rangle = \sum_i x_i y_i$ (a finite sum), and $\lVert x \rVert = \langle x, x\rangle^{1/2}$. Put $S^\infty = \{x \in \mathbb{R}^{(\infty)} : \lVert x \rVert = 1\}$ with the **colimit topology** of the finite spheres $S^m = \{x \in S^\infty : x_i = 0 \text{ for } i > m\}$: a set $C \subseteq S^\infty$ is closed if and only if $C \cap S^m$ is closed for every $m$. The inclusions $S^m \hookrightarrow S^{m+1}$ are closed embeddings, so this is a colimit along closed inclusions. The complex filtration $S^{2N+1}$ (unit sphere of $\mathbb{C}^{N+1} = \mathbb{R}^{2N+2}$) and the quaternionic filtration $S^{4N+3}$ (unit sphere of $\mathbb{H}^{N+1} = \mathbb{R}^{4N+4}$) are **cofinal** subsequences of $(S^m)_m$ — every $S^m$ is contained in some $S^{2N+1}$ and in some $S^{4N+3}$, and conversely. Since a colimit over a cofinal subdiagram equals the colimit over the whole diagram, $\varinjlim_N S^{2N+1} = \varinjlim_m S^m = \varinjlim_N S^{4N+3}$ as topological spaces. It therefore suffices to prove contractibility of $\varinjlim_m S^m$ once; both the $U(1)$-space and the $Sp(1)$-space have this same underlying contractible space.
>
> **A continuity lemma we use twice.** *A map $F\colon S^\infty \times [0,1] \to Y$ is continuous if and only if each restriction $F|_{S^m \times [0,1]}$ is continuous.* The "only if" is immediate, as restrictions of a continuous map are continuous. For the "if": the interval $[0,1]$ is locally compact and Hausdorff, so the functor $-\times [0,1]$ on topological spaces is a left adjoint (its right adjoint is the mapping space $\operatorname{Map}([0,1], -)$ with the compact–open topology; this is the exponential law for locally compact Hausdorff exponents). A left adjoint preserves all colimits, so $S^\infty \times [0,1] = \big(\varinjlim_m S^m\big) \times [0,1] = \varinjlim_m \big(S^m \times [0,1]\big)$ carries the colimit topology of the subspaces $S^m \times [0,1]$. A map out of a colimit is continuous if and only if its restriction to each piece is continuous, which is the claim.
>
> **The obstruction the naive homotopy hits.** The tempting straight-line contraction to $e_0 = (1, 0, 0, \dots)$, namely $(x, t) \mapsto \big((1-t)x + t e_0\big)/\lVert (1-t)x + t e_0 \rVert$, is *not* defined: at the antipode $x = -e_0$ the numerator is $(1-t)(-e_0) + t e_0 = (2t - 1)e_0$, which vanishes at $t = \tfrac12$. We repair this by first applying a coordinate shift that moves every point off the offending axis into a fresh coordinate, and only then contracting.
>
> **Step 1 — the identity is homotopic to the shift $T$.** Define the shift map $T\colon S^\infty \to S^\infty$, $T(x_0, x_1, x_2, \dots) = (0, x_0, x_1, \dots)$; it maps $S^m$ isometrically into $S^{m+1}$ and satisfies $\lVert Tx \rVert = \lVert x \rVert$. Define
> $$H\colon S^\infty \times [0,1] \to S^\infty, \qquad H(x, t) = \frac{(1-t)\,x + t\,Tx}{\big\lVert (1-t)\,x + t\,Tx \big\rVert}.$$
> *Well-definedness (the denominator never vanishes).* Write $N(x,t) = (1-t)x + tTx$; in coordinates $N_0 = (1-t)x_0$ and $N_k = (1-t)x_k + t\,x_{k-1}$ for $k \geq 1$. Suppose $N(x,t) = 0$ for some $x \in S^\infty$, $t \in [0,1]$. If $t = 0$ then $N = x$, and $\lVert x \rVert = 1 \neq 0$ (contradiction). If $t = 1$ then $N = Tx$, and $\lVert Tx \rVert = \lVert x \rVert = 1 \neq 0$ (contradiction). If $0 < t < 1$ then $1 - t \neq 0$: from $N_0 = (1-t)x_0 = 0$ we get $x_0 = 0$; then $N_1 = (1-t)x_1 + t x_0 = (1-t)x_1 = 0$ gives $x_1 = 0$; inductively $N_k = (1-t)x_k = 0$ gives $x_k = 0$ for all $k$ (each step using the previously derived $x_{k-1} = 0$ and $1 - t \neq 0$), so $x = 0$, contradicting $\lVert x \rVert = 1$. Hence $N(x,t) \neq 0$ everywhere and $H$ is defined.
> *Endpoints.* $H(x, 0) = x / \lVert x \rVert = x$ (since $\lVert x \rVert = 1$), and $H(x, 1) = Tx / \lVert Tx \rVert = Tx$ (since $\lVert Tx \rVert = 1$). So $H$ is a homotopy from $\mathrm{id}_{S^\infty}$ to $T$.
> *Continuity.* On $S^m \times [0,1]$ the map $H$ is a ratio of the continuous vector-valued function $N$ and its nowhere-zero continuous norm, taking values in $S^{m+1} \subseteq S^\infty$; hence $H|_{S^m \times [0,1]}$ is continuous. By the continuity lemma, $H$ is continuous. Therefore $\mathrm{id}_{S^\infty} \simeq T$.
>
> **Step 2 — the shift $T$ is homotopic to the constant map $e_0$.** With $e_0 = (1, 0, 0, \dots) \in S^0 \subseteq S^\infty$, define
> $$G\colon S^\infty \times [0,1] \to S^\infty, \qquad G(x, t) = \frac{(1-t)\,Tx + t\,e_0}{\big\lVert (1-t)\,Tx + t\,e_0 \big\rVert}.$$
> *Well-definedness.* Write $M(x,t) = (1-t)Tx + t e_0$. Since $Tx = (0, x_0, x_1, \dots)$ has vanishing $0$-th coordinate, $M(x,t) = (t,\ (1-t)x_0,\ (1-t)x_1,\ \dots)$, and its coordinates in slots $0$ and $\geq 1$ occupy disjoint places, so
> $$\big\lVert M(x,t) \big\rVert^2 = t^2 + (1-t)^2 \textstyle\sum_i |x_i|^2 = t^2 + (1-t)^2 \qquad (\text{since } \lVert x \rVert = 1).$$
> The quantity $t^2 + (1-t)^2$ vanishes only if $t = 0$ and $1 - t = 0$ simultaneously, which is impossible; in fact $t^2 + (1-t)^2 \geq \tfrac12 > 0$ for all $t \in [0,1]$ (minimised at $t = \tfrac12$). Hence the denominator is bounded away from zero and $G$ is defined.
> *Endpoints.* $G(x, 0) = Tx / \lVert Tx \rVert = Tx$, and $G(x, 1) = e_0 / \lVert e_0 \rVert = e_0$, the constant map. So $G$ is a homotopy from $T$ to $\mathrm{const}_{e_0}$.
> *Continuity.* On $S^m \times [0,1]$ the numerator $M$ is continuous with values in $S^{m+1}$ and the denominator is continuous and $\geq 1/\sqrt2$; hence $G|_{S^m \times [0,1]}$ is continuous, and by the continuity lemma $G$ is continuous. Therefore $T \simeq \mathrm{const}_{e_0}$.
>
> **Conclusion.** Combining Steps 1 and 2, $\mathrm{id}_{S^\infty} \simeq T \simeq \mathrm{const}_{e_0}$, so the identity of $S^\infty$ is homotopic to a constant. By definition, $S^\infty$ is contractible. By Step 0's cofinality, the same conclusion holds for the direct limits $\varinjlim_N S^{2N+1}$ and $\varinjlim_N S^{4N+3}$, since these are the same topological space. $\blacksquare$

With freeness and contractibility verified, $S^\infty$ is a classifying bundle for $U(1)$, and its base is $S^\infty / U(1) = \varinjlim_N (S^{2N+1}/U(1)) = \varinjlim_N \mathbb{CP}^N = \mathbb{CP}^\infty$, using that each finite stage $S^{2N+1} \to \mathbb{CP}^N$ is the [[Def - Complex Projective Space as a Quotient|quotient defining complex projective space]].

**Is an instance — $S^\infty \to \mathbb{HP}^\infty$ classifies $Sp(1)$.** *Freeness.* Let $h = (h_0, \dots) \in S^\infty \subseteq \mathbb{H}^{(\infty)}$ and $q \in Sp(1)$ with $h \cdot q = h$. Some $h_j \neq 0$; the $j$-th coordinate reads $h_j q = h_j$, so $q = h_j^{-1} h_j = 1$ (left-multiplying by $h_j^{-1}$, which exists since $h_j \neq 0$ in the division algebra $\mathbb{H}$). The action is free. *Contractibility.* By Step 0 of the corollary, the underlying space $\varinjlim_N S^{4N+3}$ equals the contractible space $\varinjlim_m S^m$. Hence $S^\infty \to S^\infty/Sp(1) = \varinjlim_N \mathbb{HP}^N = \mathbb{HP}^\infty$ is a classifying bundle for $Sp(1) \cong SU(2)$.

**Corollary (verified) — the characteristic class is well-defined and natural.** Let $E \to B$ be a classifying bundle for $G$, and $c \in H^\bullet_{dR}(B)$.

> [!note]- Naturality and homotopy-invariance of $f \mapsto f^*c$
> **Naturality in the base.** Let $f\colon M \to B$ be smooth and $h\colon M' \to M$ smooth. On differential forms the pull-back is contravariantly functorial, $(f \circ h)^*\omega = h^*(f^*\omega)$ for every $\omega \in \Omega^\bullet(B)$ (chain rule for pull-back of forms), and pull-back commutes with the exterior derivative, $d(f^*\omega) = f^*(d\omega)$, by [[Thm - Pullback Commutes with d for Forms on Manifolds|the theorem that pull-back commutes with the exterior derivative]]. Consequently $f^*$ descends to de Rham cohomology and $(f \circ h)^* = h^* \circ f^*$ there. Applying this to $c$,
> $$(f \circ h)^* c = h^*\big(f^* c\big) \qquad (\text{functoriality of the de Rham pull-back}).$$
> On the bundle side $(f \circ h)^*E = h^*(f^*E)$ (functoriality of the pull-back of principal bundles, [[Def - Operations on Vector Bundles and Pull-Back Bundles|pull-back bundles]]). So the characteristic class of $h^*(f^*E)$ determined by $c$ is $h^*$ of the characteristic class of $f^*E$: the assignment is natural.
>
> **Independence of the classifying map within a homotopy class.** Suppose $f_0, f_1 \colon M \to B$ are smooth and homotopic, $f_0 \simeq f_1$. By the [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance of de Rham cohomology]] — homotopic smooth maps induce the same map on $H^\bullet_{dR}$ — we have $f_0^* = f_1^*$ on $H^\bullet_{dR}(B)$, so
> $$f_0^* c = f_1^* c \qquad (\text{homotopy invariance of de Rham cohomology}).$$
> Moreover the two pulled-back bundles are isomorphic: by [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the theorem that homotopic maps pull back isomorphic principal bundles]], $f_0 \simeq f_1$ gives $f_0^*E \cong f_1^*E$. Therefore the characteristic class $f^*c$ depends only on the homotopy class $[f] \in [M; B]$, and equals a well-defined class of the isomorphism class of the bundle it classifies. (That *every* bundle possesses a classifying map, unique up to homotopy — so that $f^*c$ is defined for all bundles — is the general classification theorem, a scope remark for arbitrary $G$; it is proved in this series for $U(1)$ and $Sp(1)$ on the next pages.) $\blacksquare$

**Is NOT an instance — the finite Hopf bundle $S^{2N+1} \to \mathbb{CP}^N$.** For finite $N$, the sphere $S^{2N+1}$ carries a free $U(1)$-action with quotient $\mathbb{CP}^N$, so clause (2) holds; but $S^{2N+1}$ is **not contractible**, so it is not a classifying bundle. Concretely, a contractible manifold has $H^k_{dR} = 0$ for all $k > 0$ (its identity is homotopic to a constant, so by [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance of de Rham cohomology]] the identity induces both the identity and the zero map on $H^{k>0}_{dR}$, forcing $H^{k>0}_{dR} = 0$), whereas $H^{2N+1}_{dR}(S^{2N+1}) \cong \mathbb{R} \neq 0$. This is exactly why the classification requires passing to the *infinite* limit $S^\infty$: any finite sphere classifies bundles only up to a bounded dimension of the base, and its non-trivial top cohomology obstructs universality. It is the failure of this non-example that the direct-limit construction is designed to overcome.

**Calibration check.** First, the classifying map of a trivial bundle is null-homotopic: the trivial bundle $\underline{G} = M \times G \to M$ is the pull-back of $E \to B$ along any constant map $c_{b_0}\colon M \to B$, $m \mapsto b_0$ (the pull-back of any bundle along a constant map is trivial, since it acquires a global section from the constant), so $[f] = [c_{b_0}]$ is the class of a constant map, and every characteristic class of a trivial bundle is $c_{b_0}^* c = 0$ in positive degree (a constant map induces the zero map on positive-degree cohomology). Second, $[\mathrm{pt}; \mathbb{CP}^\infty]$ is a single point: every map from a point into any space is homotopic to every other (all are "constant"), and by the direct-limit definition $[\mathrm{pt}; \mathbb{CP}^\infty] = \varinjlim_N [\mathrm{pt}; \mathbb{CP}^N]$, each term a one-element set, so the limit is one point — matching the fact that there is exactly one principal $U(1)$-bundle over a point, the trivial one. Third, on a contractible base $M$ every principal $G$-bundle is trivial and its classifying map is null-homotopic, consistent with $[M; B]$ being a single class when $M$ is contractible.

---

# Unlocked by This

> [!tip] First Chern class via the classifying map *(from Gauge Theory III)*
> With $\mathbb{CP}^\infty$ in hand and its de Rham cohomology $H^2_{dR}(\mathbb{CP}^\infty)$ generated by a single class, the topological first Chern class of a $U(1)$-bundle is defined as $c_1^{\mathrm{top}}(P) = -f^*[\omega]$ for a classifying map $f$; see [[Def - First Chern Class via the Classifying Map]]. The minus sign is the convention fixed on that page.

> [!tip] Every line bundle is pulled back from projective space *(from Gauge Theory III)*
> The universality asserted here becomes a proved theorem for $U(1)$ and $Sp(1)$ over compact bases: every complex line bundle over a compact manifold is $f^*\mathcal{O}(-1)$ for a smooth $f\colon M \to \mathbb{CP}^N$, and homotopy classes of such maps classify the bundle. See [[Thm - Line Bundles over Compact Manifolds are Pulled Back from Projective Space]].

> [!tip] Classification of $U(1)$- and $SU(2)$-bundles *(from Gauge Theory III)*
> The homotopy-classification is carried out completely for line bundles over surfaces on [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class]] and for $SU(2)$-bundles over four-manifolds on [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]], where the single integer invariant is the Chern number.

> [!tip] Contractibility of $S^\infty$ as a drill *(from Gauge Theory III)*
> The two-step shift-then-contract argument proved above is isolated as an exercise on [[Ex - S^infinity is Contractible]], where the continuity in the direct-limit topology is checked in detail.
