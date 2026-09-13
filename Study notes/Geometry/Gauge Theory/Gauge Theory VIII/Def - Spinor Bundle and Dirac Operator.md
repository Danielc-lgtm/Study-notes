---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Clifford Bundle and Bundle of Clifford Modules"
  - "Def - Connection on a Vector Bundle"
  - "Def - Metric-Compatible Connection"
  - "Def - Induced Connection on Tensor Bundles"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth, oriented Riemannian manifold of dimension $n$, with metric $g = \langle\cdot,\cdot\rangle$; we write $|v|^2 = \langle v, v\rangle$ for $v \in T_mM$. All bundles are smooth. Sections of a vector bundle $E \to M$ are written $\Gamma(E)$, and $\Omega^p(M; E) = \Gamma(\Lambda^p T^*M \otimes E)$. The musical isomorphism $\flat : T_mM \to T_m^*M$ sends $v \mapsto v^\flat = \langle v, \cdot\rangle$, with inverse $\sharp : T_m^*M \to T_mM$; both are $C^\infty(M)$-linear bundle isomorphisms and isometries for the induced metric on $T_m^*M$. A **local orthonormal frame** of $TM$ over an open set $U \subseteq M$ is an $n$-tuple $(e_1, \dots, e_n)$ of sections with $\langle e_i, e_j\rangle = \delta_{ij}$ pointwise; its **dual coframe** $(e^1, \dots, e^n)$ of $T^*M$ satisfies $e^i(e_j) = \delta_{ij}$, and then $(e^i)^\sharp = e_i$.

The **Clifford bundle** $\operatorname{Cl}(M) = \operatorname{Fr}_{SO} \times_{SO(n)} \operatorname{Cl}(\mathbb{R}^n)$ is the bundle of algebras with fibre $\operatorname{Cl}(T_mM) \cong \operatorname{Cl}(T_m^*M)$, and $\nabla^{LC}$ is the connection it inherits from the [[Def - Levi-Civita Connection|Levi-Civita connection]], which is a **derivation** of the fibrewise Clifford product; both are constructed on [[Def - Clifford Bundle and Bundle of Clifford Modules|the Clifford-bundle page]]. A **bundle of Clifford modules** is recalled from that page:

![[Def - Clifford Bundle and Bundle of Clifford Modules#Bundle of Clifford modules]]

Concretely, a bundle of Clifford modules is a real (or complex) vector bundle $E \to M$ with a smooth bundle map $\operatorname{Cl} : TM \otimes E \to E$, $(v, e) \mapsto v \cdot e$, satisfying $v \cdot (v \cdot e) = -|v|^2\, e$ for all $v \in T_mM$, $e \in E_m$; equivalently (Proposition 4 of that page) an algebra-bundle homomorphism $\operatorname{Cl}(M) \to \operatorname{End}(E)$, under which we write $\phi \cdot e$ for the action of $\phi \in \Gamma(\operatorname{Cl}(M))$. Polarising $v \cdot (v \cdot e) = -|v|^2 e$ gives $v \cdot (w \cdot e) + w \cdot (v \cdot e) = -2\langle v, w\rangle e$, used repeatedly below.

We equip $E$ with a fibre metric $\langle\cdot,\cdot\rangle_E$: a smooth Euclidean inner product when $E$ is real, or a smooth Hermitian inner product (conjugate-linear in the first slot) when $E$ is complex; we suppress the subscript and write $\langle\cdot,\cdot\rangle$ for it. Since $\nabla^{LC}$ acts on $\operatorname{Cl}(M)$ and $\nabla$ (to be introduced) acts on $E$, the symbol $\nabla$ without a superscript always means the connection on $E$. The scalar curvature and curvature tensor do not appear on this page; the [[Def - Curvature of a Vector-Bundle Connection|curvature]] $F_\nabla \in \Omega^2(M; \operatorname{End}E)$ is named only in the forward references.

> [!warning] Convention: Clifford sign
> The series uses $v \cdot v = -|v|^2 \cdot 1$ (Haydys's convention, adopted on every page of this chapter). The vault's [[Def - Clifford Algebra|Clifford algebra page]] is stated for a general quadratic form as $\varphi(v)^2 = Q(v)\cdot 1$; the dictionary is $\operatorname{Cl}(\mathbb{R}^n) = \operatorname{Cl}(\mathbb{R}^n, Q)$ with $Q(v) = -|v|^2$. The opposite convention $v \cdot v = +|v|^2$ gives a genuinely different algebra and a Dirac operator squaring to $-\Delta$ rather than $+\Delta$; the module axiom's sign is what makes the eventual $D^2$ a nonnegative Laplacian.

This is a compound page: it defines three interlocking notions — a **Dirac bundle** (a bundle of Clifford modules carrying a compatible metric and connection, Haydys's three conditions), the **Dirac operator** $D$ of a Dirac bundle, and the **spinor bundle** $\slashed{S}$ and **spin Dirac operator** $\slashed{D}$ (named here, constructed in §8.3) — because they are one package: the Dirac operator is the point of the Dirac-bundle axioms, and the spinor bundle is the single most important example, singled out so that this page is the front door to the operator that organises the rest of the chapter and all of Seiberg–Witten theory.

---

# Axiom Motivation

The whole of §8.2–§8.4 is built to transplant one flat-space fact to a curved manifold. On $\mathbb{R}^n$ one chooses constant matrices $\gamma_1, \dots, \gamma_n$ acting on a vector space $V$ with $\gamma_i \gamma_j + \gamma_j \gamma_i = -2\delta_{ij}$, sets $D = \sum_i \gamma_i \partial_i$ on $V$-valued functions, and finds
$$D^2 = \sum_{i,j} \gamma_i \gamma_j\, \partial_i \partial_j = \tfrac12\sum_{i,j}(\gamma_i\gamma_j + \gamma_j\gamma_i)\,\partial_i\partial_j = -\sum_i \partial_i^2 = \Delta \qquad \text{(} \partial_i\partial_j \text{ symmetric in } i,j\text{; then the Clifford relation),}$$
so that $D$ is a *square root of the Laplacian*. This is Dirac's factorisation, and it is the reason Dirac operators exist at all: a first-order operator whose square is a Laplacian sees curvature to first order and detects topology through its kernel (the index theorem of chapter IX and Seiberg–Witten theory of chapter XI). To reproduce the construction on a manifold $M$ we must replace the constant $\gamma_i$ by Clifford multiplication that varies from point to point — this is exactly a bundle of Clifford modules — and replace $\partial_i$ by a covariant derivative $\nabla$. The question this definition answers is: *which* metric-and-connection data on $E$ make the resulting operator $D = \operatorname{Cl}\circ\nabla$ behave like the flat Dirac operator — formally self-adjoint, and squaring to a nonnegative Laplacian plus curvature?

We want two properties to survive the transplant, and each forces one axiom. First, $D$ should be **formally self-adjoint**: $\int_M \langle Ds_1, s_2\rangle\,\mathrm{vol} = \int_M \langle s_1, Ds_2\rangle\,\mathrm{vol}$ for compactly supported sections. Formal self-adjointness is what makes the spectrum real, makes $\ker D$ and $\operatorname{coker}D$ dual, and turns the Weitzenböck identity into vanishing theorems. Second, $D^2$ should be a **Weitzenböck Laplacian** $\nabla^*\nabla + \mathcal{R}$, with $\nabla^*\nabla \ge 0$ the connection Laplacian and $\mathcal{R}$ a zero-order curvature term. Reading the flat computation, the three axioms of a Dirac bundle are precisely the conditions under which the manipulations above remain legal on $M$.

**Condition (1): the connection $\nabla$ on $E$ is metric.** In the flat model, self-adjointness of $D$ is integration by parts, and integration by parts of a covariant derivative uses $X\langle s_1, s_2\rangle = \langle \nabla_X s_1, s_2\rangle + \langle s_1, \nabla_X s_2\rangle$ — the metric-compatibility identity. If $\nabla$ is not [[Def - Metric-Compatible Connection|metric-compatible]], differentiating the inner product leaves an extra term and $D$ fails to be symmetric. *What breaks if we drop it.* Take $M = \mathbb{R}^n$, $E = \Lambda T^*M$ with its natural Clifford multiplication and metric, but replace the Levi-Civita connection by $\nabla_X = \nabla^{LC}_X + \lambda(X)\,\mathrm{id}$ for a nonzero real $1$-form $\lambda$. Then
$$\langle \nabla_X \phi, \psi\rangle + \langle \phi, \nabla_X \psi\rangle = X\langle\phi,\psi\rangle + 2\lambda(X)\langle\phi,\psi\rangle \neq X\langle\phi,\psi\rangle \qquad \text{(the two } \lambda(X)\langle\phi,\psi\rangle \text{ terms add rather than cancel, since scalar multiplication is self-adjoint),}$$
so (1) fails; and one checks that the associated $D$ acquires an antisymmetric-in-the-wrong-way zero-order term and is no longer formally self-adjoint. The strengthening that would restore matters is exactly metric-compatibility: force the local connection endomorphisms to be skew-adjoint. Dropping (1) breaks [[Thm - Dirac Operators are Formally Self-Adjoint|self-adjointness]].

**Condition (2): $\langle v \cdot e_1, v \cdot e_2\rangle = |v|^2 \langle e_1, e_2\rangle$ (Clifford multiplication scales the metric by $|v|^2$).** This is the second half of integration by parts: passing $e_i\cdot$ across the inner product in $\langle e_i\cdot\nabla_{e_i}s_1, s_2\rangle$ requires $e_i\cdot$ to be skew-adjoint, and (2) is equivalent to skew-adjointness (proved in The Definition below). *What breaks if we drop it.* Keep $M = \mathbb{R}^n$ and the trivial module bundle $E = \mathbb{R}^n \times V$ with constant $\gamma_i$, but put on $V$ a Euclidean metric for which the $\gamma_i$ are **self-adjoint** rather than skew (for a generic metric they are neither). Then for a unit vector $v$, $\langle v\cdot e, v\cdot e\rangle = \langle \gamma_v^2 e, e\rangle_{\text{if self-adjoint}}$ need not equal $\langle e,e\rangle$, condition (2) fails, and $D = \sum\gamma_i\partial_i$ is no longer formally self-adjoint. The condition captures precisely that Clifford multiplication by a unit vector is an *orthogonal* transformation of each fibre — geometrically, that the Clifford action is compatible with the metric on $E$ the way it is compatible with the metric on $TM$.

**Condition (3): $\nabla(\phi \cdot s) = (\nabla^{LC}\phi)\cdot s + \phi\cdot \nabla s$ for $\phi \in \Gamma(\operatorname{Cl}(M))$, $s \in \Gamma(E)$ (the connection is compatible with the module structure).** This is the manifold replacement for "the $\gamma_i$ are constant". In the flat computation of $D^2$ one silently commutes $\nabla_{e_i}$ past $e_j\cdot$; on a manifold the Clifford field $e_j$ is not parallel, and (3) is exactly the product rule that lets $\nabla^{LC}e_j$ be tracked. Without it, $D$ is still a first-order operator, but $D^2$ is not $\nabla^*\nabla + \mathcal{R}$ and there is no [[Thm - Weitzenbock Formula for the Dirac Operator|Weitzenböck formula]]. *What breaks if we drop it, and the sharp form.* Take again $E = \mathbb{R}^n\times V$ flat, but perturb the trivial connection to $\nabla_X = d_X + \beta(X)\,T$ for a real $1$-form $\beta$ and a fixed skew-adjoint $T \in \mathfrak{so}(V)$ (so (1) and (2) still hold). Since $\nabla^{LC}$ on the trivial flat $\operatorname{Cl}(M)$ is $d$,
$$\nabla_X(\phi\cdot s) - \big((\nabla^{LC}_X\phi)\cdot s + \phi\cdot\nabla_X s\big) = \beta(X)\big(T(\phi\cdot s) - \phi\cdot(Ts)\big) = \beta(X)\,[T,\, \phi\cdot]\,s \qquad \text{(Leibniz for } d \text{ cancels the } d \text{-terms; only the } T \text{-terms remain),}$$
which vanishes for all $\phi$ if and only if $T$ commutes with every Clifford multiplication, that is $T$ lies in the commutant of $\operatorname{Cl}(\mathbb{R}^n)$ acting on $V$. Choosing $T$ skew-adjoint but outside the commutant — for $n = 2$, $V = \mathbb{C}^2$ with $\gamma_1, \gamma_2$ the Pauli-type generators, the skew-adjoint endomorphisms form the $4$-dimensional $\mathfrak{u}(2)$ while the derivation-inducing ones (Clifford multiplication by $\mathfrak{spin}(2) = \mathbb{R}\,\gamma_1\gamma_2$, plus scalars) span only $2$ dimensions, so most choices of $T$ break (3) — gives a connection satisfying (1) and (2) but not (3). The sharp lesson is that (3) forces the local connection form of $\nabla$ to act by Clifford multiplication by elements of $\mathfrak{spin}(n) \subset \operatorname{Cl}^0(\mathbb{R}^n)$; this is exactly why, in §8.3, the spinor bundle's connection is the Levi-Civita connection read through the isomorphism $\mathfrak{so}(n) \cong \mathfrak{spin}(n)$, and there is no freedom in it.

A reader who has grasped these three points can invent the definition: to make $D = \operatorname{Cl}\circ\nabla$ formally self-adjoint, demand that $\nabla$ be metric (1) and that Clifford multiplication be skew-adjoint (2); to make $D^2$ a Weitzenböck Laplacian, demand that $\nabla$ differentiate Clifford products by the Leibniz rule against $\nabla^{LC}$ (3).

---

# The Definition

We define the Dirac bundle, prove the equivalent forms of condition (2), define the Dirac operator, and prove that its frame formula is frame-independent.

## Dirac bundle

> **Definition (Dirac bundle).** A **Dirac bundle** over an oriented Riemannian manifold $M$ is a [[Def - Clifford Bundle and Bundle of Clifford Modules|bundle of Clifford modules]] $E \to M$, equipped with a fibre metric $\langle\cdot,\cdot\rangle$ (Euclidean if $E$ is real, Hermitian if $E$ is complex) and a [[Def - Connection on a Vector Bundle|connection]] $\nabla$ on $E$, such that:
> 1. **(metric)** $\nabla$ is [[Def - Metric-Compatible Connection|metric-compatible]]: $X\langle s_1, s_2\rangle = \langle \nabla_X s_1, s_2\rangle + \langle s_1, \nabla_X s_2\rangle$ for all vector fields $X$ and $s_1, s_2 \in \Gamma(E)$;
> 2. **(Clifford multiplication is metric)** $\langle v\cdot e_1, v\cdot e_2\rangle = |v|^2\,\langle e_1, e_2\rangle$ for all $m \in M$, $v \in T_mM$, $e_1, e_2 \in E_m$;
> 3. **(compatibility)** $\nabla(\phi\cdot s) = (\nabla^{LC}\phi)\cdot s + \phi\cdot\nabla s$ for all $\phi \in \Gamma(\operatorname{Cl}(M))$ and $s \in \Gamma(E)$, where $\nabla^{LC}$ is the [[Def - Clifford Bundle and Bundle of Clifford Modules|Levi-Civita connection on the Clifford bundle]].

In the complex (Hermitian) case, $\langle\cdot,\cdot\rangle$ is conjugate-linear in the first argument, and since Clifford multiplication is by *real* tangent vectors, no conjugation enters conditions (1)–(2). The Euclidean and Hermitian cases are treated uniformly below; the only place the choice matters is the codomain of the fibre metric ($\mathbb{R}$ or $\mathbb{C}$), and every identity we prove holds verbatim.

## The three faces of condition (2)

Condition (2) is stated as a scaling law, but it is the same statement as "unit vectors act orthogonally" and as "Clifford multiplication is skew-adjoint". The equivalence is short and worth having in hand, because different proofs on later pages invoke different faces of it (the exercise [[Ex - Clifford Multiplication is Skew-Adjoint on a Dirac Bundle|Clifford multiplication is skew-adjoint on a Dirac bundle]] is this proposition drilled).

> **Proposition 1 (equivalent forms of (2)).** Let $E$ be a bundle of Clifford modules with a fibre metric. The following are equivalent:
> - (2) $\langle v\cdot e_1, v\cdot e_2\rangle = |v|^2\langle e_1, e_2\rangle$ for all $v \in T_mM$, $e_1, e_2 \in E_m$;
> - (2′) for every unit vector $v$ ($|v| = 1$), the map $v\cdot : E_m \to E_m$ preserves the fibre metric, i.e. is orthogonal (unitary in the complex case);
> - (2″) for every $v \in T_mM$, Clifford multiplication $v\cdot$ is **skew-adjoint**: $\langle v\cdot e_1, e_2\rangle = -\langle e_1, v\cdot e_2\rangle$ for all $e_1, e_2 \in E_m$.

> [!note]- Full proof of Proposition 1
> We prove (2) $\Leftrightarrow$ (2′) and (2) $\Leftrightarrow$ (2″); together these give the three-way equivalence. Fix a point $m$ and work in the fibre $E_m$; $v, w$ denote elements of $T_mM$ and $e_1, e_2$ elements of $E_m$.
>
> **(2) $\Rightarrow$ (2′).** Assume (2) and let $|v| = 1$. Then $\langle v\cdot e_1, v\cdot e_2\rangle = |v|^2\langle e_1, e_2\rangle = \langle e_1, e_2\rangle$ (by (2), then $|v|^2 = 1$), which says $v\cdot$ preserves the inner product; a metric-preserving linear endomorphism of a finite-dimensional inner-product space is orthogonal (respectively unitary). This is (2′).
>
> **(2′) $\Rightarrow$ (2).** Assume (2′) and let $v \neq 0$; write $v = |v|\,u$ with $u = v/|v|$ a unit vector. Clifford multiplication is linear in the vector slot, so $v\cdot e = |v|\,(u\cdot e)$, and
> $$\langle v\cdot e_1, v\cdot e_2\rangle = |v|^2\,\langle u\cdot e_1, u\cdot e_2\rangle = |v|^2\,\langle e_1, e_2\rangle \qquad \text{(linearity in the vector slot; then } u\cdot \text{ preserves the metric by (2′), } |u| = 1\text{).}$$
> For $v = 0$ both sides vanish. This is (2).
>
> **(2″) $\Rightarrow$ (2).** Assume (2″). Then
> $$\langle v\cdot e_1, v\cdot e_2\rangle = -\langle e_1, v\cdot(v\cdot e_2)\rangle = -\langle e_1, -|v|^2 e_2\rangle = |v|^2\langle e_1, e_2\rangle \qquad \text{(skew-adjointness (2″) applied to the first factor; then the Clifford relation } v\cdot(v\cdot e_2) = -|v|^2 e_2\text{).}$$
> This is (2).
>
> **(2) $\Rightarrow$ (2″).** Assume (2). In the identity (2), replace $e_2$ by $v\cdot e_2$:
> $$\langle v\cdot e_1,\ v\cdot(v\cdot e_2)\rangle = |v|^2\,\langle e_1,\ v\cdot e_2\rangle \qquad \text{(condition (2) with second argument } v\cdot e_2\text{).}$$
> On the left, $v\cdot(v\cdot e_2) = -|v|^2 e_2$ (Clifford relation), so the left side equals $\langle v\cdot e_1, -|v|^2 e_2\rangle = -|v|^2\langle v\cdot e_1, e_2\rangle$. Hence
> $$-|v|^2\,\langle v\cdot e_1, e_2\rangle = |v|^2\,\langle e_1, v\cdot e_2\rangle.$$
> For $v \neq 0$ we have $|v|^2 \neq 0$; dividing by $|v|^2$ gives $\langle v\cdot e_1, e_2\rangle = -\langle e_1, v\cdot e_2\rangle$. For $v = 0$ both sides are $0$. This is (2″), for every $v$. $\blacksquare$

The polarised form of skew-adjointness will be used later: from (2″), replacing $v$ by $v + w$ and expanding by bilinearity, $\langle v\cdot e_1, w\cdot e_2\rangle + \langle w\cdot e_1, v\cdot e_2\rangle = 0$ whenever $\langle v, w\rangle = 0$; more directly, (2″) itself is the clean statement and is what the self-adjointness and Weitzenböck proofs invoke.

## The Dirac operator

Let $E$ be a Dirac bundle. The connection is a first-order operator $\nabla : \Gamma(E) \to \Omega^1(M; E) = \Gamma(T^*M \otimes E)$. Compose it with the fibrewise **Clifford contraction**
$$c : T^*M \otimes E \to E, \qquad c(\alpha \otimes e) = \alpha^\sharp \cdot e,$$
which raises the index of the covector $\alpha \in T_m^*M$ to the vector $\alpha^\sharp \in T_mM$ and then multiplies. The composite is the object we want.

> **Definition (Dirac operator).** The **Dirac operator** of a Dirac bundle $E$ is the first-order differential operator
> $$D := c \circ \nabla : \ \Gamma(E) \xrightarrow{\ \nabla\ } \Gamma(T^*M \otimes E) \xrightarrow{\ c\ } \Gamma(E).$$
> In any local oriented orthonormal frame $(e_1, \dots, e_n)$ of $TM$ with dual coframe $(e^i)$, since $\nabla s = \sum_i e^i \otimes \nabla_{e_i} s$ and $c(e^i \otimes t) = (e^i)^\sharp \cdot t = e_i \cdot t$,
> $$Ds = \sum_{i=1}^n e_i \cdot \nabla_{e_i} s.$$

> **Proposition 2 (the frame formula is frame-independent).** The section $Ds = \sum_i e_i\cdot\nabla_{e_i}s$ does not depend on the choice of local orthonormal frame; it equals the invariantly defined section $c(\nabla s)$.

> [!note]- Full proof of Proposition 2
> **We must show** that $\sum_i e_i\cdot\nabla_{e_i}s$ is the value of a frame-independent construction, so that computing it in two different orthonormal frames gives the same section of $E$.
>
> **Step 0 — the Clifford contraction is a bundle map.** The map $c : T^*M \otimes E \to E$ is the composite of two $C^\infty(M)$-linear bundle maps: first $\sharp \otimes \operatorname{id}_E : T^*M \otimes E \to TM \otimes E$, where the [[Def - Metric-Compatible Connection|musical isomorphism]] $\sharp$ is $C^\infty(M)$-linear because it is induced by the metric tensor pointwise; then Clifford multiplication $\operatorname{Cl} : TM \otimes E \to E$, which is a smooth bundle map by the very definition of a bundle of Clifford modules. A composite of $C^\infty(M)$-linear bundle maps is a $C^\infty(M)$-linear bundle map, so $c$ is a bundle map: its value $c(t)_m$ at $m$ depends only on $t_m \in (T^*M \otimes E)_m$, not on how $t$ is written in any frame.
>
> **Step 1 — $\nabla s$ is a frame-independent section.** For $s \in \Gamma(E)$, the covariant derivative $\nabla s$ is a well-defined element of $\Gamma(T^*M \otimes E) = \Omega^1(M; E)$, determined by $(\nabla s)(X) = \nabla_X s$ for vector fields $X$; this is intrinsic to the connection and uses no frame.
>
> **Step 2 — the frame formula computes $c(\nabla s)$.** Fix a local oriented orthonormal frame $(e_i)$ with dual coframe $(e^i)$. Expanding $\nabla s$ in this frame, $\nabla s = \sum_i e^i \otimes (\nabla s)(e_i) = \sum_i e^i \otimes \nabla_{e_i}s$ (evaluating the $E$-valued $1$-form on the frame vectors and using that $(e^i)$ is dual to $(e_i)$). Applying $c$ and using Step 0 together with $(e^i)^\sharp = e_i$ (the coframe dual to an orthonormal frame is raised to that same frame),
> $$c(\nabla s) = \sum_i c\big(e^i \otimes \nabla_{e_i}s\big) = \sum_i (e^i)^\sharp \cdot \nabla_{e_i}s = \sum_i e_i \cdot \nabla_{e_i}s \qquad \text{(} c \text{ linear over } C^\infty(M) \text{, Step 0; then } (e^i)^\sharp = e_i\text{).}$$
>
> **Conclusion.** The right-hand side $\sum_i e_i\cdot\nabla_{e_i}s$ was computed in an arbitrary orthonormal frame and equals the single frame-independent section $c(\nabla s)$ of Steps 0–1. Therefore any two orthonormal frames give the same $Ds$, and $D = c \circ \nabla$ is well defined. $\blacksquare$

## The spinor bundle and the spin Dirac operator (named here, built in §8.3)

The single most important Dirac bundle is the **spinor bundle**. On a **spin manifold** — an oriented Riemannian $M$ with a chosen [[Def - Spin Structure and Spin-c Structure|spin structure]], a principal $\operatorname{Spin}(n)$-bundle $P$ double-covering the frame bundle — one fixes a complex Hermitian $\operatorname{Cl}(\mathbb{R}^n)$-module $\slashed{S}$ with its restricted $\operatorname{Spin}(n)$-action $\rho$ and forms the associated bundle
$$\slashed{S} := P \times_{\operatorname{Spin}(n),\,\rho} \slashed{S}.$$
With Clifford multiplication induced fibrewise and the connection induced from the Levi-Civita connection on $P$, $\slashed{S}$ is a Dirac bundle, and its Dirac operator is the **spin Dirac operator** $\slashed{D}$. The verification of the three Dirac-bundle conditions, and the construction of the connection, belong to [[Def - Spin-c Dirac Operator Twisted by a Connection|the spin$^c$ Dirac-operator page]] of §8.3, together with the spin$^c$ generalisation $\slashed{D}_A$ that Seiberg–Witten theory uses; we name $\slashed{S}$ and $\slashed{D}$ here so that this page is the front door to them. In dimension four $\slashed{S} = \slashed{S}^+ \oplus \slashed{S}^-$, Clifford multiplication by a $1$-form is odd (interchanging the summands), and $\slashed{D}$ has the off-diagonal block form $\slashed{D} = \begin{pmatrix} 0 & \slashed{D}^- \\ \slashed{D}^+ & 0\end{pmatrix}$; this too is proved in §8.3.

---

# Categorical / Structural Definition

Two structural readings clarify what kind of object a Dirac operator is.

**The module structure is a homomorphism of algebra bundles.** By Proposition 4 of [[Def - Clifford Bundle and Bundle of Clifford Modules|the Clifford-bundle page]], a bundle of Clifford modules is the same as a homomorphism of algebra bundles $c : \operatorname{Cl}(M) \to \operatorname{End}(E)$, and the module's metric-and-connection axioms have a clean reading in this language: (2″) says $c$ lands, on the degree-one part $TM$, in the **skew-adjoint** endomorphisms $\mathfrak{so}(E)$ (respectively $\mathfrak{u}(E)$); (3) says $c$ is a **parallel** bundle map, $\nabla^{\operatorname{End}} c = 0$, for the connection $\nabla^{\operatorname{End}}$ on $\operatorname{Hom}(\operatorname{Cl}(M), \operatorname{End}(E))$ induced by $\nabla^{LC}$ and $\nabla$ (this is the invariant restatement of the Leibniz identity, using the [[Def - Induced Connection on Tensor Bundles|induced connection on tensor and hom bundles]]). A Dirac bundle is thus a bundle of Clifford modules whose Clifford homomorphism is metric and parallel.

**The Dirac operator is the natural first-order operator attached to the pair (connection, Clifford action).** Among first-order differential operators $\Gamma(E) \to \Gamma(E)$, those of the form $c \circ \nabla$ for a bundle map $c : T^*M \otimes E \to E$ are exactly the ones whose **principal symbol** $\sigma_D(\xi) \in \operatorname{End}(E_m)$ (the top-order part, $\sigma_D(\xi)e = c(\xi \otimes e)$ for $\xi \in T_m^*M$) is $C^\infty$-linear in $e$ and given by contracting $\xi$ against $c$. For the Dirac operator, $\sigma_D(\xi) = \xi^\sharp \cdot$ is Clifford multiplication by the raised covector, and the Clifford relation $\sigma_D(\xi)^2 = (\xi^\sharp \cdot)^2 = -|\xi|^2 \operatorname{id}$ makes $\sigma_D(\xi)$ invertible for $\xi \neq 0$ — this is precisely the statement that $D$ is [[Thm - Laplacians and Dirac Operators are Elliptic|elliptic]] (chapter IX). The Dirac operator is, in one phrase, *the first-order operator whose symbol is Clifford multiplication*.

---

# Relate to Other Fields / Compression

**True name.** The official definition presents $D$ as a composite $c \circ \nabla$; its operational characterisation is the pair of properties it was built to have. Operationally, a Dirac operator on a Dirac bundle is *a formally self-adjoint first-order elliptic operator whose square is $\nabla^*\nabla + \mathcal{R}$*: self-adjoint because $\nabla$ is metric and Clifford multiplication skew-adjoint (conditions 1–2, proved on [[Thm - Dirac Operators are Formally Self-Adjoint|the self-adjointness page]]), elliptic because the symbol is Clifford multiplication (the Clifford relation, chapter IX), and Weitzenböck because $\nabla$ differentiates Clifford products (condition 3, proved on [[Thm - Weitzenbock Formula for the Dirac Operator|the Weitzenböck page]]). Whenever one meets a first-order operator with these three features one is looking at a Dirac operator, whatever the bundle is called.

In **quantum field theory**, the flat model $D = \sum_i \gamma_i \partial_i$ is the spatial part of the physicists' Dirac operator; the Minkowski-signature operator $i\gamma^\mu \partial_\mu$ acting on Dirac spinors, whose square is the Klein–Gordon operator, is the Lorentzian version of the factorisation $D^2 = \Delta$ (with signs from the indefinite metric). The vault's [[Def - Spin Connection and the Dirac Operator|spin-connection Dirac operator]] writes $\slashed{D}$ in a local frame through the spin connection $1$-form; it is the same operator as the $\slashed{D}$ named here, in coordinates rather than as $\operatorname{Cl}\circ\nabla$. In **index theory**, the kernel and cokernel of the chiral half $\slashed{D}^+$ compute topological invariants: the Atiyah–Singer index theorem gives $\operatorname{ind}\slashed{D}^+$ as a characteristic number, and this is the engine of Rokhlin's theorem in chapter XIII. In **Hodge theory**, the Dirac operator of the Clifford module $\Lambda T^*M$ is $d + d^*$ (proved on [[Thm - The Hodge-de Rham Operator is a Dirac Operator|the Hodge–de Rham page]]), so the abstract Dirac operator specialises to the operator whose kernel is the harmonic forms; the Weitzenböck formula then specialises to the Bochner identity relating the Hodge Laplacian to the connection Laplacian and Ricci curvature.

---

# Examples / Corollaries

**Is an instance — the smallest case, $\mathbb{R}^1$ with $E = \mathbb{R}\times\mathbb{C}$.** Take $M = \mathbb{R}$ with the flat metric, so $\operatorname{Cl}(\mathbb{R}^1)$ is generated by $e_1$ with $e_1^2 = -1$, hence $\operatorname{Cl}(\mathbb{R}^1) \cong \mathbb{C}$. Let $E = \mathbb{R}\times\mathbb{C}$, with Clifford multiplication $e_1 \cdot z := iz$ (so $e_1\cdot(e_1\cdot z) = i(iz) = -z = -|e_1|^2 z$, verifying the module axiom), the standard Hermitian metric $\langle z, w\rangle = \bar z w$, and $\nabla = d$ the trivial connection. We verify the three conditions clause by clause.
- **(1) metric.** With $\nabla = d$ and the constant metric, $\tfrac{d}{dx}\langle z(x), w(x)\rangle = \langle z', w\rangle + \langle z, w'\rangle$ holds by the product rule for $\tfrac{d}{dx}$ applied to $\bar z w$ (the metric coefficients are constant), so $d$ is metric-compatible.
- **(2) Clifford multiplication is metric.** By Proposition 1 it suffices to check skew-adjointness of $e_1\cdot = i$: $\langle iz, w\rangle = \overline{iz}\,w = -i\bar z w$ and $-\langle z, iw\rangle = -\bar z (iw) = -i\bar z w$, so $\langle iz, w\rangle = -\langle z, iw\rangle$; multiplication by $i$ is skew-adjoint, hence (2) holds (for $v = t e_1$, $\langle v\cdot z, v\cdot w\rangle = t^2\langle iz, iw\rangle = t^2\bar z w = |v|^2\langle z,w\rangle$).
- **(3) compatibility.** Here $\operatorname{Cl}(M) = \mathbb{R}\times\mathbb{C}$ is the trivial algebra bundle with $\nabla^{LC} = d$; for $\phi : \mathbb{R} \to \mathbb{C}$ and $s : \mathbb{R} \to \mathbb{C}$, $\phi\cdot s$ is pointwise product, and $d(\phi\cdot s) = (d\phi)s + \phi\,ds = (\nabla^{LC}\phi)\cdot s + \phi\cdot\nabla s$ by the Leibniz rule for $d$.
So $E$ is a Dirac bundle, and its Dirac operator is $Ds = e_1\cdot\nabla_{e_1}s = i\,s'$, i.e. $D = i\,\tfrac{d}{dx}$. As a check on the motivating identity, $D^2 s = i\tfrac{d}{dx}(i s') = i^2 s'' = -s'' = \Delta s$, so $D$ is the square root of the $1$-dimensional Laplacian $\Delta = -\tfrac{d^2}{dx^2}$.

**Is an instance — flat $\mathbb{R}^n$ with a constant Clifford module.** Let $M = \mathbb{R}^n$ flat, and let $(V, \langle\cdot,\cdot\rangle_V)$ be a Hermitian (or Euclidean) $\operatorname{Cl}(\mathbb{R}^n)$-module for which each generator $\gamma_i := e_i\cdot : V \to V$ is skew-adjoint (such a metric always exists: average any metric over the finite group $\{\pm e_I\}$ generated by the $e_i$, or take the quaternionic modules of [[Thm - Low-Dimensional Clifford Algebras and the Quaternionic Spinor Modules|the low-dimensional Clifford-algebra page]], whose Hermitian structure has this property). Put $E = \mathbb{R}^n \times V$ with the constant metric and $\nabla = d$. Then:
- **(1)** $d$ is metric because $V$'s metric is constant, exactly as in the previous example.
- **(2)** each $\gamma_i$ is skew-adjoint by hypothesis, so $v\cdot = \sum_i v_i \gamma_i$ is skew-adjoint for every $v = \sum v_i e_i$; Proposition 1 gives (2).
- **(3)** the Clifford bundle is trivial with $\nabla^{LC} = d$ and constant structure, so for a $\operatorname{Cl}(\mathbb{R}^n)$-valued function $\phi$ and a $V$-valued function $s$, $d(\phi\cdot s) = (d\phi)\cdot s + \phi\cdot ds$ by the Leibniz rule for $d$ applied to the bilinear Clifford action (the action itself is constant in $x$).
Its Dirac operator is $Ds = \sum_i \gamma_i \partial_i s$, and $D^2 = \Delta = -\sum_i\partial_i^2$ by the flat computation in Axiom Motivation. This is the model on which every local computation in §8.4 is based; the quaternionic instances $n = 3, 4$ (where $D$ takes the explicit form $i\partial_1 + j\partial_2 + k\partial_3$ and its four-dimensional analogue) are worked out on the flat-space page of §8.4.

**Is NOT an instance — $\Lambda T^*M$ with a non-metric connection.** The exterior bundle $E = \Lambda T^*M$, with Clifford multiplication $v\cdot\phi = v^\flat\wedge\phi - \iota_v\phi$ and its natural metric, *is* a Dirac bundle when equipped with the Levi-Civita connection (that is the content of [[Thm - The Hodge-de Rham Operator is a Dirac Operator|the Hodge–de Rham page]], where $D = d + d^*$). But equip it instead with $\nabla_X := \nabla^{LC}_X + \lambda(X)\,\operatorname{id}$ for a fixed nonzero real $1$-form $\lambda$ on $M$ (say $M = \mathbb{R}^n$, $\lambda = dx^1$). The Clifford multiplication and the metric are unchanged, so conditions (2) and (3) still hold — for (3), the scalar $\lambda(X)\operatorname{id}$ commutes with every $\phi\cdot$ and cancels between the two sides, so the extra term is invisible to the compatibility identity. But condition (1) fails: for $\phi \neq 0$,
$$\langle\nabla_X\phi, \psi\rangle + \langle\phi, \nabla_X\psi\rangle = X\langle\phi,\psi\rangle + 2\lambda(X)\langle\phi,\psi\rangle \qquad \text{(metric-compatibility of } \nabla^{LC} \text{, then the two } \lambda(X) \text{ scalar terms, which are self-adjoint and add),}$$
which differs from $X\langle\phi,\psi\rangle$ by $2\lambda(X)\langle\phi,\psi\rangle \neq 0$. So $(E, \nabla)$ violates (1) and is *not* a Dirac bundle; its associated operator $\sum_i e_i\cdot\nabla_{e_i}$ is not formally self-adjoint. This isolates condition (1): dropping metric-compatibility, and nothing else, already destroys the definition.

**Corollary — the Dirac operator is a first-order differential operator.** Since $\nabla$ is first-order and $c$ is a (zero-order) bundle map, $D = c\circ\nabla$ is a first-order differential operator; its principal symbol at $\xi \in T_m^*M$ is $\sigma_D(\xi) = \xi^\sharp\cdot \in \operatorname{End}(E_m)$, Clifford multiplication by $\xi^\sharp$, as computed in the structural definition. This is the input to ellipticity in chapter IX.

> [!warning] Convention: the sign of the Dirac operator
> The series writes $D = \sum_i e_i\cdot\nabla_{e_i}$ (Haydys; Lawson–Michelsohn, *Spin Geometry*, use the identical convention), with the Clifford sign $v\cdot v = -|v|^2$ fixed above. Some physics texts instead write the Dirac operator as $i\gamma^\mu\partial_\mu$ with a Hermitian (rather than skew-Hermitian) convention for the $\gamma^\mu$; the factor $i$ converts skew-adjoint Clifford multiplication into self-adjoint operators and matches the Lorentzian signature. To convert, multiply the physicists' $\gamma^\mu$ by $-i$ (or the operator by $\mp i$) and change the metric sign; the two operators have the same kernel and the same square up to sign. The vault's [[Def - Spin Connection and the Dirac Operator|spin-connection Dirac operator]] uses the series' convention, written through the spin connection in an orthonormal frame; it is the same $\slashed{D}$.

**Calibration check.** Three quick verifications the reader can carry out from the page. (i) On the $\mathbb{R}^1$ example, confirm formal self-adjointness directly: for compactly supported $z, w : \mathbb{R} \to \mathbb{C}$, $\int \langle iz', w\rangle\,dx = \int \overline{iz'}\,w\,dx = \int (-i)\bar z' w\,dx = \int (-i)(-\bar z w')\,dx$ (integration by parts, boundary terms vanish) $= \int \bar z (iw')\,dx = \int \langle z, iw'\rangle\,dx$, so $\int\langle Dz, w\rangle = \int\langle z, Dw\rangle$. (ii) Re-derive (2″) $\Rightarrow$ (2) in one line: $\langle v\cdot e_1, v\cdot e_2\rangle = -\langle e_1, v\cdot v\cdot e_2\rangle = |v|^2\langle e_1, e_2\rangle$. (iii) Confirm that in the non-example only clause (1) fails, by checking that the extra scalar term $\lambda(X)\operatorname{id}$ is self-adjoint (breaking (1)) yet commutes with Clifford multiplication (preserving (3)) and does not touch the fibre metric or Clifford action (preserving (2)).

---

# Unlocked by This

> [!tip] Formal self-adjointness of the Dirac operator *(from Gauge Theory VIII, §8.2)*
> Conditions (1) and (2) together make $D$ formally self-adjoint on a closed manifold: $\int_M\langle Ds_1, s_2\rangle\,\mathrm{vol} = \int_M\langle s_1, Ds_2\rangle\,\mathrm{vol}$, proved on [[Thm - Dirac Operators are Formally Self-Adjoint|the self-adjointness page]] via a pointwise divergence identity. This is what makes $\ker D \cong \operatorname{coker}D$ and underlies the index computations.

> [!tip] Ellipticity of the Dirac operator *(from Gauge Theory IX)*
> The principal symbol $\sigma_D(\xi) = \xi^\sharp\cdot$ is invertible for $\xi \neq 0$ (with inverse $-|\xi|^{-2}\xi^\sharp\cdot$, by the Clifford relation), so $D$ is elliptic; proved on [[Thm - Laplacians and Dirac Operators are Elliptic|the ellipticity page]]. Ellipticity plus self-adjointness on a closed manifold makes $D$ Fredholm with $\operatorname{coker}D \cong \ker D$.

> [!tip] The Weitzenböck formula *(from Gauge Theory VIII, §8.4)*
> Condition (3) makes $D^2 = \nabla^*\nabla + \mathcal{R}$, the [[Thm - Weitzenbock Formula for the Dirac Operator|Weitzenböck identity]], with $\mathcal{R}$ the [[Def - Curvature Endomorphism of a Dirac Bundle|curvature endomorphism]]; for the spinor bundle this is the Lichnerowicz formula $\slashed{D}^2 = \nabla^*\nabla + \tfrac14 s_g$, from which positive scalar curvature forces $\ker\slashed{D} = 0$.

> [!tip] The spinor bundle and the twisted Dirac operator *(from Gauge Theory VIII, §8.3)*
> On a spin (or spin$^c$) manifold the [[Def - Spin Structure and Spin-c Structure|spinor bundle]] $\slashed{S}$ is the canonical Dirac bundle, with [[Def - Spin-c Dirac Operator Twisted by a Connection|spin$^c$ Dirac operator]] $\slashed{D}_A$; the exercise [[Ex - The Twisted Bundle of a Dirac Bundle is a Dirac Bundle|twisting a Dirac bundle]] shows $\slashed{S}\otimes E$ is again a Dirac bundle, giving the twisted operators that carry the Seiberg–Witten equations.

> [!tip] The Hodge–de Rham operator *(from Gauge Theory VIII, §8.2)*
> The exterior bundle $\Lambda T^*M$ is a Dirac bundle whose Dirac operator is $d + d^*$, on [[Thm - The Hodge-de Rham Operator is a Dirac Operator|the Hodge–de Rham page]]; the abstract theory thus recovers the operator whose kernel is the harmonic forms.
