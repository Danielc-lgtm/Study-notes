---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Directed Set and Direct System"
  - "Def - Module"
  - "Def - Ring"
  - "Def - Ring Homomorphism"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Fix a [[Def - Directed Set and Direct System|directed set]] $(I,\leq)$ and a category $\mathcal{C}\in\{\text{Sets, Groups, Rings, }R\text{-modules, }R\text{-algebras}\}$. A [[Def - Directed Set and Direct System|direct system]] is $D=\big((X_i),(f_{ij})\big)$ with $f_{ij}:X_i\to X_j$ for $i\leq j$; an [[Def - Directed Set and Direct System|inverse system]] is $E=\big((Y_i),(h_{ij})\big)$ with $h_{ij}:Y_j\to Y_i$ for $i\leq j$. We write $\coprod_i X_i$ for the disjoint union (coproduct), $\prod_i Y_i$ for the product, $[x_i]$ for the class of $x_i\in X_i$ in the direct limit, and $(y_i)_i$ for a thread in the inverse limit. The canonical maps are $\lambda_j:X_j\to\varinjlim X_i$ (into the direct limit) and $\pi_j:\varprojlim Y_i\to Y_j$ (out of the inverse limit). The full registry is on [[Commutative Algebra X — Completions and Limits]].

This is a compound page: it defines two dual notions — the **direct limit** $\varinjlim X_i$ and the **inverse limit** $\varprojlim Y_i$ — together with the **universal properties** that characterise each, because they are mirror images of one another and the completion of the next section is an instance of the second.

---

# Axiom Motivation

We have two operations to make precise, and they are opposite. The first is **"take the union of a family of objects that are not literally subsets of one another, but are glued by a compatible system of maps"**. The second is **"collect all the consistent threads through a tower of approximations"**. The constructions below are the unique reasonable answers; the way to invent them is to write down what we want each to *do* — i.e. its universal property — and then find an explicit object that does it.

**Inventing the direct limit from "generalised union".** Suppose the $X_i$ were genuine subsets of one big set $X$, with $f_{ij}$ the inclusions. Then their union is the smallest object containing every $X_i$ compatibly, and it has a defining feature: a map *out of* the union to any target $A$ is the same as a compatible family of maps $g_i:X_i\to A$ (compatible meaning $g_j|_{X_i}=g_i$, i.e. $g_j\circ f_{ij}=g_i$). When the $X_i$ are *not* subsets — only related by abstract maps $f_{ij}$ — we *define* the union to be the object with exactly this feature. That is the universal property of the direct limit: it is the universal receiver of compatible maps out of the system. Now build it concretely. Every element of every $X_i$ should appear, so start with the disjoint union $\coprod_i X_i$. But $x_i$ and its image $f_{ij}(x_i)$ should be "the same element", so quotient by the smallest equivalence relation forcing $x_i\sim f_{ij}(x_i)$. Directedness of $I$ is exactly what makes this relation come out clean: $x_i\sim x_j$ iff they have a common image $f_{ik}(x_i)=f_{jk}(x_j)$ for some $k\geq i,j$ — and transitivity of "$\sim$" is the place the common-upper-bound axiom is spent (combine the two witnessing indices into one). The result $\varinjlim X_i=\big(\coprod X_i\big)/\sim$ inherits a $\mathcal{C}$-structure by operating on representatives pushed into a common stage, and one checks it has the universal property. Why this and not a variant? If we quotiented by a *smaller* relation we would not have glued enough (some $f_{ij}(x_i)$ would stay distinct from $x_i$, violating the property); by a *larger* one we would identify elements no compatible map need identify (violating universality). The equivalence relation is forced.

**Inventing the inverse limit from "consistent threads".** Now the dual desideratum. We have a tower $\cdots\to Y_2\to Y_1\to Y_0$ of coarser and coarser approximations and we want the object of "all the information you could specify at every level at once, consistently". Its defining feature should be: a map *into* this object from any source $B$ is the same as a compatible family of maps $g_i:B\to Y_i$ (compatible meaning $h_{ij}\circ g_j=g_i$ — the level-$j$ data, projected down, agrees with the level-$i$ data). That is the universal property of the inverse limit: the universal *source* of compatible maps into the system. Build it concretely: a single "consistent specification" is a choice $y_i\in Y_i$ for every $i$ such that the choices agree under the projections, $y_i=h_{ij}(y_j)$. The set of all such threads sits inside the product $\prod_i Y_i$ as
$$\varprojlim Y_i = \Big\{(y_i)_i\in\textstyle\prod_i Y_i : y_i=h_{ij}(y_j)\ \forall\,i\leq j\Big\},$$
a sub-object because the thread condition is preserved by the operations of $\mathcal{C}$. The projections $\pi_j:(y_i)\mapsto y_j$ are the canonical maps, and one checks universality directly.

**Why universal properties, not the formulas, are the real definitions.** The disjoint-union-mod-identification and the threads-in-a-product are *models* of the limits; their true identity is the universal property, for three reasons. First, the property pins each limit down *up to unique isomorphism*, so any two constructions that satisfy it are canonically the same — this is how one proves $\varprojlim k[T]/(T^n)\cong k[[T]]$ without ever matching elements. Second, the property is what you actually *use*: to build a map to/from a limit you supply a compatible family, never an explicit element. Third, the property makes the **duality** transparent: the inverse limit's property is the direct limit's property with every arrow reversed, so $\varprojlim$ in $\mathcal{C}$ is $\varinjlim$ in $\mathcal{C}^{\mathrm{op}}$. The reason this chapter cares is that the most important inverse limit — the [[Def - The I-adic Completion|$\mathfrak{a}$-adic completion]] $\varprojlim R/\mathfrak{a}^n$ — is *defined* by this property, and every fact about completions is a cashed-out instance of the inverse-limit universal property.

---

# The Definition

Let $(I,\leq)$ be a directed set.

## Direct limit (colimit)

Let $D=\big((X_i),(f_{ij})\big)$ be a direct system. The **direct limit** of $D$ is
$$\varinjlim X_i \;=\; \Big(\coprod_{i\in I} X_i\Big)\big/\!\sim,$$
where $\sim$ is the smallest equivalence relation with $x_i\sim f_{ij}(x_i)$ for all $i\leq j$ and $x_i\in X_i$. Explicitly, for $x_i\in X_i$ and $x_j\in X_j$,
$$x_i\sim x_j \iff \exists\,k\geq i,j \text{ with } f_{ik}(x_i)=f_{jk}(x_j).$$
It carries the structure of an object of $\mathcal{C}$: to add (or multiply) $[x_i]$ and $[x_j]$, push both into a common stage $X_k$ ($k\geq i,j$) via $f_{ik},f_{jk}$ and operate there. The **canonical maps** are $\lambda_j:X_j\to\varinjlim X_i$, $x_j\mapsto[x_j]$, and they satisfy $\lambda_j\circ f_{ij}=\lambda_i$.

## Inverse limit (limit)

Let $E=\big((Y_i),(h_{ij})\big)$ be an inverse system. The **inverse limit** of $E$ is the sub-object of the product
$$\varprojlim Y_i \;=\; \Big\{(y_i)_{i\in I}\in\textstyle\prod_{i\in I} Y_i : y_i=h_{ij}(y_j)\ \text{for all } i\leq j\Big\},$$
with operations performed coordinatewise. The **canonical maps** are the projections $\pi_j:\varprojlim Y_i\to Y_j$, $(y_i)\mapsto y_j$, and they satisfy $h_{ij}\circ\pi_j=\pi_i$.

---

# Categorical / Structural Definition

The two limits are characterised by **universal properties**, which are their true definitions.

**Direct limit (universal property).** Given a direct system $D$, an object $A$, and a *compatible family* of morphisms $(g_i:X_i\to A)_{i\in I}$ — meaning $g_j\circ f_{ij}=g_i$ for all $i\leq j$ — there is a *unique* morphism $g:\varinjlim X_i\to A$ such that $g\circ\lambda_j=g_j$ for every $j$. In other words, $\varinjlim X_i$ is the universal object receiving the system: maps out of it correspond bijectively to compatible families of maps out of the stages. Categorically it is the **colimit** of the functor $D:(I,\leq)\to\mathcal{C}$.

**Inverse limit (universal property).** Given an inverse system $E$, an object $B$, and a compatible family $(g_i:B\to Y_i)_{i\in I}$ — meaning $h_{ij}\circ g_j=g_i$ for all $i\leq j$ — there is a *unique* morphism $g:B\to\varprojlim Y_i$ such that $\pi_j\circ g=g_j$ for every $j$. So $\varprojlim Y_i$ is the universal object mapping to the system: maps into it correspond bijectively to compatible families of maps into the stages. Categorically it is the **limit** of the functor $E:(I,\leq)^{\mathrm{op}}\to\mathcal{C}$.

Each universal property determines its limit up to unique isomorphism: if two objects both satisfy it, the universal maps between them compose to the identity. The two are **dual** — the inverse-limit property is the direct-limit property with every arrow reversed, so $\varprojlim$ in $\mathcal{C}$ equals $\varinjlim$ in the opposite category $\mathcal{C}^{\mathrm{op}}$. The full statements, the proof that the explicit constructions satisfy the properties, and the completeness corollaries are on [[Thm - The Inverse Limit and Completeness]].

---

# Relate to Other Fields / Compression

The cleanest compression: **$\varinjlim$ is the universal object you can map *to* compatibly from every stage (a generalised union), and $\varprojlim$ is the universal object you can map *from* compatibly to every stage (a generalised inverse-of-truncation).** They are dual: reverse the arrows and one becomes the other.

**True name:** the true name of $\varprojlim Y_i$ is **"the set of compatible threads"** — an element is a sequence $(y_i)$ agreeing under projection, and you compute with it level by level. The true name of $\varinjlim X_i$ is **"elements modulo eventual agreement"** — two elements are equal once their images coincide at some later stage, so any finite computation may be carried out inside a single sufficiently-late stage $X_k$. Operationally: for $\varprojlim$, *work modulo each $\mathfrak{a}^n$ and glue*; for $\varinjlim$, *push everything into one stage and finish there*.

This pair of constructions is one of the most pervasive in mathematics. In topology and sheaf theory, the **stalk** of a sheaf $\mathcal{F}$ at $x$ is the direct limit $\varinjlim_{U\ni x}\mathcal{F}(U)$ over the directed set of neighbourhoods — germs of sections. In analysis, the **Cauchy completion** of a metric space, including $\mathbb{R}=\varprojlim(\mathbb{Q}\text{ mod shrinking balls})$ in spirit and $p$-adic $\mathbb{Z}_p$ exactly, is an inverse limit. In Galois theory, $\mathrm{Gal}(\overline{K}/K)=\varprojlim\mathrm{Gal}(L/K)$ over finite subextensions is a profinite group, while $\overline{K}=\varinjlim L$ is the direct limit of the same data with arrows reversed. In homological algebra, $\varinjlim$ over a directed set is exact while $\varprojlim$ is only left exact, with derived functors $\varprojlim^i$ measuring the failure. The completion $\widehat{R}=\varprojlim R/\mathfrak{a}^n$ of [[Def - The I-adic Completion]] is the single instance this chapter is built toward.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}_p$ as an inverse limit.** With $Y_i=\mathbb{Z}/p^i\mathbb{Z}$ and $h_{ij}$ the projections, $\varprojlim Y_i=\mathbb{Z}_p$. A thread $(y_i)$ is a sequence $y_i\in\mathbb{Z}/p^i$ with $y_{i+1}\equiv y_i\pmod{p^i}$ — exactly a base-$p$ expansion running infinitely to the left. The element $-1$ is the thread $(p-1,\ p^2-1,\ p^3-1,\dots)$, i.e. $\dots(p-1)(p-1)(p-1)$.

**Is an instance — the Prüfer group as a direct limit.** With $X_i=\mathbb{Z}/p^i\mathbb{Z}$ and $f_{i,i+1}:\mathbb{Z}/p^i\hookrightarrow\mathbb{Z}/p^{i+1}$ multiplication by $p$ (so $1\mapsto p$), $\varinjlim X_i=\mathbb{Z}(p^\infty)\cong\mathbb{Z}[1/p]/\mathbb{Z}$, the divisible torsion group of $p$-power roots of unity. *Same objects $\mathbb{Z}/p^i$ as the previous example, opposite arrows, utterly different limit.*

**Is an instance — algebraic closure as a direct limit.** $\overline{\mathbb{F}_p}=\varinjlim_i\mathbb{F}_{p^{i!}}$ over the field inclusions is the increasing union of all finite fields; every element lies in some finite stage, so it is algebraic over $\mathbb{F}_p$, and the limit is algebraically closed.

**Is an instance — formal power series.** $k[[T]]=\varprojlim_n k[T]/(T^n)$: a thread is a compatible family of polynomial truncations $\big(a_0+a_1T+\cdots+a_{n-1}T^{n-1}\big)_n$, which is precisely a single formal power series $\sum_{m\geq0}a_mT^m$.

**Is NOT an instance — a colimit over a non-directed shape.** The pushout of $\mathbb{Z}\xleftarrow{}\mathbb{Z}\xrightarrow{}\mathbb{Z}$ (a span, indexed by a non-directed poset) is a colimit but not a *direct* limit, and it is not computed by "glue and identify eventually" — it can fail to be exact. The directedness hypothesis is what separates the well-behaved filtered colimits of this chapter from general colimits.

**Is NOT an instance — $\varprojlim$ is not "the intersection".** It is tempting to read $\varprojlim Y_i$ as $\bigcap Y_i$, but the $Y_i$ are generally not subobjects of a common object; $\varprojlim$ is the *thread* construction, which can be strictly larger or smaller than any naive intersection. For instance $\varprojlim(\mathbb{Z}\xleftarrow{p}\mathbb{Z}\xleftarrow{p}\cdots)=0$, not an intersection of copies of $\mathbb{Z}$.

**Corollary — finite computations descend to one stage (direct limit).** Any element of $\varinjlim X_i$ is $[x_k]$ for a single $k$, and any finite set of elements can be represented in a common stage $X_k$ (push along the system using directedness). So equalities and finitely many operations in $\varinjlim$ are decided inside one $X_k$.

**Corollary — a thread is determined by its tail (inverse limit).** Two threads $(y_i),(y_i')$ in $\varprojlim Y_i$ are equal iff $y_i=y_i'$ for all $i$; but compatibility means $y_i$ is determined by $y_j$ for any $j\geq i$, so knowing the thread on a cofinal subset determines it everywhere.

**Calibration check.** Verify that the relation "$x_i\sim x_j$ iff $f_{ik}(x_i)=f_{jk}(x_j)$ for some $k$" is transitive, using directedness explicitly. Check that the inverse-limit thread condition $y_i=h_{ij}(y_j)$ for $\mathbb{Z}/p^i$ is exactly "$y_{i+1}\equiv y_i\pmod{p^i}$", and write the thread for $-1\in\mathbb{Z}_5$. Confirm that reversing every arrow turns the Prüfer-group direct system into the $\mathbb{Z}_p$ inverse system, and that the two limits differ.

---

# Unlocked by This

> [!tip] The structure sheaf via gluing, and the formal completion *(from Algebraic Geometry)*
> Direct limits build **stalks** $\mathcal{O}_{X,x}=\varinjlim_{U\ni x}\mathcal{O}_X(U)$, the local rings of a scheme, from sections on shrinking opens; inverse limits build the **formal completion** $\widehat{\mathcal{O}_{X,x}}=\varprojlim\mathcal{O}_{X,x}/\mathfrak{m}_x^n$, the ring of the formal disk. The two limits are the two ways of zooming in: $\varinjlim$ over neighbourhoods reaches the Zariski-local ring, then $\varprojlim$ over infinitesimal thickenings reaches the analytic-local (formal) ring. Both are pure instances of the constructions on this page.

> [!tip] Profinite groups and the Krull topology *(from Galois Theory)*
> An infinite Galois group $\mathrm{Gal}(\overline{K}/K)=\varprojlim_L\mathrm{Gal}(L/K)$ is an inverse limit of finite groups, hence a compact totally disconnected **profinite group**; the inverse-limit (product) topology is the Krull topology under which the Galois correspondence extends to infinite extensions. The dual direct limit $\overline{K}=\varinjlim L$ recovers the field, and the contravariance between the two is the order-reversal of the fundamental theorem of Galois theory.

> [!tip] Derived limits and $\varprojlim^1$ *(from Homological Algebra)*
> Since $\varprojlim$ is only left exact, it has right derived functors $\varprojlim^i$; the first, $\varprojlim^1$, measures the failure of a surjection of inverse systems to give a surjection of limits and controls phenomena from the universal coefficient theorem in cohomology to the convergence of spectral sequences. It vanishes under the **Mittag-Leffler condition**, which holds for towers of surjections — the reason completion of finitely generated modules is exact.
