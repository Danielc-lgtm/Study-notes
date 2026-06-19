---
type: definition
subject: category-theory
prereqs:
  - "Def - Cone and Cocone"
  - "Def - Initial and Terminal Object"
  - "Def - Product and Coproduct"
  - "Def - Hom-Functor and Representable Functor"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]], $J$ a small index category, and $D : J \to \mathcal{C}$ a diagram. We write $\lim D$ (also $\lim_J D$) for the **limit** and $\operatorname{colim} D$ (also $\operatorname{colim}_J D$) for the **colimit**. A [[Def - Cone and Cocone|cone]] over $D$ with apex $X$ is written $\lambda : \Delta_X \Rightarrow D$ with legs $\lambda_j : X \to D_j$; a cocone under $D$ with nadir $X$ is $\mu : D \Rightarrow \Delta_X$ with legs $\mu_j : D_j \to X$. The hom-set is $\mathcal{C}(X, Y)$. The full registry is on [[Category Theory III — Limits and Colimits]].

This is a compound page: it defines the dual pair **limit** and **colimit** together, since one is the other taken in the [[Def - Opposite Category and Duality|opposite category]] ($\operatorname{colim}_J D = (\lim_{J^{op}} D^{op})^{op}$), and every theorem about one mirrors a theorem about the other.

---

# Axiom Motivation

You already have [[Def - Cone and Cocone|cones]]: an object mapping compatibly into a whole diagram. There are usually many cones over a given diagram — the question a limit answers is *which one is the best*. The right notion of "best" is universality, and the choice between two readings of universality is what the definition must settle.

Picture the cones over $D$ as forming their own category: objects are cones, and a morphism from a cone with apex $X$ to one with apex $X'$ is a map $h : X \to X'$ of apexes through which each leg factors. The **limit** is the *terminal* object of this category — the universal cone, the one every other cone maps into uniquely. Spelled out: $\lim D$ is an object equipped with a limit cone $(\pi_j : \lim D \to D_j)$ such that for *every* cone $(\lambda_j : X \to D_j)$ there is a *unique* map $u : X \to \lim D$ with $\pi_j \circ u = \lambda_j$ for all $j$. The limit factors every compatible family through itself, with no choice left open.

Why terminal and not initial? Because we want the limit to *receive* the comparison maps — to be the universal *target* that all cones funnel into. A cone with apex $X$ is a way of "approximating the diagram from a single object"; the limit is the optimal approximation, the one all others factor through. If you asked for the *initial* cone instead, you would get something useless in general (often it does not exist, and when it does it is not the construction anyone wants). The terminal choice is forced by what limits are for: to be the universal solution to "map compatibly into $D$". Existence of the unique factorisation says the limit captures every compatible family; uniqueness says it adds no spurious structure — together, exactly the [[Def - Universal Property and Universal Arrow|universal property]] that pins $\lim D$ down up to unique isomorphism.

There is a second, equivalent definition that is often more useful for *computing*, via [[Def - Hom-Functor and Representable Functor|representability]]. The assignment $X \mapsto \mathrm{Cone}(X, D)$, the set of cones over $D$ with apex $X$, is a functor $\mathcal{C}^{op} \to \mathbf{Set}$ (precompose legs with $X' \to X$). A limit of $D$ is a **representation** of this functor: an object $\lim D$ with a natural isomorphism
$$\mathcal{C}(X, \lim D) \;\cong\; \mathrm{Cone}(X, D)$$
natural in $X$. Reading the isomorphism: *a map into the limit is the same as a cone over the diagram*. The universal cone is the image of $1_{\lim D}$ under this bijection. These two definitions — terminal cone, and representation of $\mathrm{Cone}(-, D)$ — say the same thing, by the [[Thm - The Yoneda Lemma|Yoneda lemma]]; the first is geometric, the second is what you reach for when proving formulas.

The colimit is the exact dual. It is the *initial* [[Def - Cone and Cocone|cocone]] under $D$: an object $\operatorname{colim} D$ with legs $(\iota_j : D_j \to \operatorname{colim} D)$ such that every cocone factors *out of* it uniquely. Equivalently it represents $X \mapsto \mathrm{Cone}(D, X)$ covariantly: $\mathcal{C}(\operatorname{colim} D, X) \cong \mathrm{Cone}(D, X)$ — *a map out of the colimit is a cocone under the diagram*. Where the limit is the universal way to map *into* $D$, the colimit is the universal way to map *out of* $D$; where limits glue compatible families into one target, colimits glue the diagram itself into one source.

The unifying payoff to keep in mind: by varying the shape $J$, the single definition above specialises to *every* universal construction met so far. Discrete $J$: [[Def - Product and Coproduct|product/coproduct]]. Parallel pair: [[Def - Equalizer and Coequalizer|equalizer/coequalizer]]. Cospan/span: [[Def - Pullback and Pushout|pullback/pushout]]. Empty $J$: [[Def - Initial and Terminal Object|terminal/initial object]]. Tower: [[Def - Direct and Inverse Limits|inverse/direct limit]]. One definition, indexed by shape, is the whole subject.

---

# The Definition

Let $D : J \to \mathcal{C}$ be a diagram of shape $J$.

A **limit** of $D$ is a cone $(\pi_j : L \to D_j)_{j \in J}$ over $D$ that is **terminal** in the category of cones over $D$: for every cone $(\lambda_j : X \to D_j)_{j}$ there exists a *unique* morphism $u : X \to L$ such that
$$\pi_j \circ u = \lambda_j \qquad \text{for all } j \in J.$$
The object $L$ is written $\lim D$ and the maps $\pi_j$ are the **limit projections** (or **legs**). Equivalently, $\lim D$ is a representation of the functor $\mathrm{Cone}(-, D) : \mathcal{C}^{op} \to \mathbf{Set}$, that is, an object with a natural isomorphism $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D)$ in $X$.

A **colimit** of $D$ is a cocone $(\iota_j : D_j \to L')_{j \in J}$ under $D$ that is **initial** in the category of cocones under $D$: for every cocone $(\mu_j : D_j \to X)_j$ there exists a *unique* $u : L' \to X$ with $u \circ \iota_j = \mu_j$ for all $j$. The object $L'$ is written $\operatorname{colim} D$, with **colimit injections** $\iota_j$. Equivalently $\operatorname{colim} D$ represents $\mathrm{Cone}(D, -) : \mathcal{C} \to \mathbf{Set}$, giving $\mathcal{C}(\operatorname{colim} D, X) \cong \mathrm{Cone}(D, X)$.

When every diagram of shape $J$ has a limit, $\mathcal{C}$ **has all $J$-shaped limits**; if this holds for all small $J$, $\mathcal{C}$ is [[Def - Complete and Cocomplete Category|complete]] (dually, cocomplete).

The following table records which classical construction is the $J$-shaped (co)limit for each shape:

$$
\begin{array}{lll}
\textbf{shape } J & \textbf{limit} & \textbf{colimit} \\
\text{empty} & \text{terminal object } 1 & \text{initial object } 0 \\
\text{discrete} & \text{product } \textstyle\prod_i D_i & \text{coproduct } \textstyle\coprod_i D_i \\
\text{parallel pair } \rightrightarrows & \text{equalizer} & \text{coequalizer} \\
\text{cospan } \bullet\!\to\!\bullet\!\leftarrow\!\bullet & \text{pullback} & - \\
\text{span } \bullet\!\leftarrow\!\bullet\!\to\!\bullet & - & \text{pushout} \\
(\mathbb{N}, \ge) & \text{inverse limit } \varprojlim & - \\
(\mathbb{N}, \le) & - & \text{direct colimit } \varinjlim
\end{array}
$$

---

# Categorical / Structural Definition

The definition *is* categorical, so this section records the three equivalent faces and how they relate. A limit of $D : J \to \mathcal{C}$ is, equivalently: **(i)** a terminal object in the category of cones over $D$; **(ii)** a representation of $\mathrm{Cone}(-, D) : \mathcal{C}^{op} \to \mathbf{Set}$, i.e. an object $\lim D$ with $\mathcal{C}(-, \lim D) \cong \mathrm{Cone}(-, D)$; **(iii)** a [[Def - Universal Property and Universal Arrow|universal arrow]] from the constant-diagram functor $\Delta : \mathcal{C} \to \mathcal{C}^J$ to the object $D \in \mathcal{C}^J$ — that is, the limit functor (when it exists) is the right adjoint to $\Delta$, with $\lim = \Delta^R$ and the limit cone the counit. The colimit is dually the left adjoint $\operatorname{colim} = \Delta^L$.

Reading (iii) is the deepest: **taking limits is right adjoint to the diagonal, and taking colimits is left adjoint to the diagonal.** The hom-set adjunction $\mathcal{C}^J(\Delta_X, D) \cong \mathcal{C}(X, \lim D)$ is precisely "cones over $D$ with apex $X$ are maps $X \to \lim D$", and $\mathcal{C}^J(D, \Delta_X) \cong \mathcal{C}(\operatorname{colim} D, X)$ is the colimit version. This is why [[Thm - Right Adjoints Preserve Limits|right adjoints preserve limits]] applies to $\lim$ itself, and why limits commute with limits.

---

# Relate to Other Fields / Compression

A limit is the universal "compatible system assembled into one object"; a colimit is the universal "diagram quotiented/glued into one object". The inverse limit $\varprojlim$ of a tower of rings (used to build completions like the $p$-adics $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n$) is a limit; the direct limit $\varinjlim$ of an increasing union (the union of a chain of subgroups, the stalk of a sheaf, the localisation as a filtered colimit) is a colimit. See [[Def - Direct and Inverse Limits]] and [[Thm - The Inverse Limit and Completeness]] for the special case $J = (\mathbb{N}, \le/\ge)$.

**True name:** $\lim D$ is "the object whose maps-in are cones over $D$"; $\operatorname{colim} D$ is "the object whose maps-out are cocones under $D$". The single most useful operational fact is the representability isomorphism $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D)$ — when you need to know a map into a limit, you produce a compatible family, and vice versa.

---

# Examples / Corollaries

**Is an instance — products, equalizers, pullbacks, terminal objects are all limits.** Each is the $J$-shaped limit for the shape in the table above. This is not an analogy: the equalizer literally *is* $\lim$ of the parallel-pair diagram, and one proves general theorems about all of them at once by proving them about $\lim$. See [[Def - Product and Coproduct]], [[Def - Equalizer and Coequalizer]], [[Def - Pullback and Pushout]].

**Is an instance — limits in $\mathbf{Set}$ are compatible families.** For $D : J \to \mathbf{Set}$, $\lim D = \{(x_j)_{j} \in \prod_j D_j : D(f)(x_j) = x_k \text{ for all } f : j \to k\}$, the set of cones with apex the singleton, i.e. the compatible families. The colimit is $\coprod_j D_j$ modulo the equivalence relation generated by $x_j \sim D(f)(x_j)$. See [[Thm - Limits in Set and in Functor Categories]].

**Is an instance — the inverse limit of $\mathbb{Z}/p^n$.** The tower $\cdots \to \mathbb{Z}/p^3 \to \mathbb{Z}/p^2 \to \mathbb{Z}/p$ has limit the $p$-adic integers $\mathbb{Z}_p = \varprojlim_n \mathbb{Z}/p^n$, the compatible sequences of residues. A point of $\mathbb{Z}_p$ is exactly a cone over the tower with apex the one-point set, which is a coherent choice of residue mod $p^n$ for every $n$.

**Is an instance — a filtered colimit computes a union or stalk.** A **directed colimit** (filtered colimit) over $(\mathbb{N}, \le)$ of an increasing chain $A_0 \hookrightarrow A_1 \hookrightarrow \cdots$ is the union $\bigcup_n A_n$; the stalk of a sheaf at a point is the filtered colimit over open neighbourhoods. Directed colimit and filtered colimit are the same notion (a directed poset is a filtered category), the well-behaved colimits that commute with finite limits in $\mathbf{Set}$.

**Is NOT an instance — not every diagram has a limit.** The limit need not exist. In $\mathbf{Field}$, the product (a limit over a two-point discrete shape) of $\mathbb{Q}$ and $\mathbb{F}_2$ does not exist. In the homotopy category of spaces, pullbacks and pushouts famously fail to exist as genuine (co)limits — which is the motivation for **homotopy limits** and **model categories**. "Has limits of shape $J$" is a property a category may or may not have.

**Is NOT an instance — a non-universal cone is not the limit.** Any object with a cone to $D$ is a *candidate*, but only the terminal one is the limit. In $\mathbf{Set}$, the empty set maps (uniquely, vacuously) into any diagram of nonempty sets via the empty family, giving a cone, but it is not the limit unless the limit happens to be empty. Being a cone is necessary; being terminal among cones is the definition.

**Calibration check.** Verify that $\lim$ over the empty shape is the terminal object and $\operatorname{colim}$ over the empty shape is the initial object. Check that for a diagram indexed by a category *with* a terminal object $t \in J$, $\lim D \cong D_t$ (the limit is just the value at the terminal vertex). If you can read the representability isomorphism $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D)$ in both directions, you have the operational definition.

---

# Unlocked by This

> [!tip] Completeness and the Adjoint Functor Theorem *(from this chapter and Chapter IV)*
> A category with all small limits is [[Def - Complete and Cocomplete Category|complete]]; the existence of limits is the hypothesis of the **General Adjoint Functor Theorem**, which says a limit-preserving functor from a complete category has a left adjoint provided a solution-set condition holds. Limits are the precondition for the entire adjoint-functor machinery.

> [!tip] Kan Extensions *(from Higher Category Theory)*
> A **Kan extension** $\mathrm{Lan}_K F$ / $\mathrm{Ran}_K F$ is computed pointwise as a colimit / limit over a comma category; "all concepts are Kan extensions" (Mac Lane), and limits/colimits are the special case where $K$ maps to the terminal category. This is the gateway to **derived functors** as homotopy Kan extensions.

> [!tip] Homotopy Colimits and Derived Functors *(from Model Categories)*
> Ordinary colimits are not homotopy-invariant; the **homotopy colimit** (e.g. the mapping cone, the bar construction) is the derived functor of $\operatorname{colim}$, and computing it correctly is the central technical problem of **derived** and **stable** homotopy theory (Chapter VI). The failure of $\pi_0$, $H_*$, and $\pi_1$ to preserve strict colimits is exactly what homotopy colimits repair.
