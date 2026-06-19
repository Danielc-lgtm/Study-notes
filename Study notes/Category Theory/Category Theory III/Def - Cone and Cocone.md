---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Natural Transformation"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]] and $J$ is a small **index category** (the "shape"). A **diagram** of shape $J$ in $\mathcal{C}$ is a [[Def - Functor|functor]] $D : J \to \mathcal{C}$; we write $D_j$ for the object $D(j)$ and $D(f) : D_j \to D_k$ for the morphism assigned to $f : j \to k$ in $J$. For an object $X \in \mathcal{C}$, the **constant functor** $\Delta_X : J \to \mathcal{C}$ sends every object of $J$ to $X$ and every morphism to $1_X$. A **cone** over $D$ with apex $X$ is a [[Def - Natural Transformation|natural transformation]] $\lambda : \Delta_X \Rightarrow D$; a **cocone** under $D$ with nadir $X$ is a natural transformation $\mu : D \Rightarrow \Delta_X$. The full registry is on [[Category Theory III — Limits and Colimits]].

This is a compound page: it defines the dual pair **cone** and **cocone**, because a cone over $D$ is exactly a cocone under $D$ viewed in the [[Def - Opposite Category and Duality|opposite category]], and the [[Def - Limit and Colimit|limit and colimit]] are defined as the universal members of these two families.

---

# Axiom Motivation

Before you can speak of "the limit of a diagram", you need to say what a diagram is and what it means to sit over one. A **diagram** is not an informal picture; it is a functor $D : J \to \mathcal{C}$ from a small index category $J$. The category $J$ is the *shape* — its objects are the vertices and its morphisms are the edges that the diagram must respect. A discrete $J$ (no arrows) gives a diagram that is just a family of objects; a parallel pair $\bullet \rightrightarrows \bullet$ gives two objects and two maps; a cospan $\bullet \to \bullet \leftarrow \bullet$ gives the shape whose limit is a [[Def - Pullback and Pushout|pullback]]. Choosing $J$ chooses which kind of [[Def - Limit and Colimit|(co)limit]] you are about to take. This is the unification: products, equalizers, pullbacks, terminal objects, and inverse limits are *the same construction* applied to different shapes.

Now, what is a cone? Intuitively it is an object $X$ that "maps compatibly into the whole diagram". Concretely, a cone with apex $X$ is a family of legs $\lambda_j : X \to D_j$, one for each vertex $j$, such that the legs respect every edge: for each $f : j \to k$ in $J$, the triangle commutes,
$$D(f) \circ \lambda_j = \lambda_k.$$
The picture is a point $X$ above the diagram with a leg dropping to each vertex, and the commutativity says that going from $X$ to $D_j$ and then along the diagram to $D_k$ is the same as going from $X$ straight to $D_k$ — the legs are *consistent* with the diagram's own arrows. Without the commutativity condition the legs would be an arbitrary unrelated family; the condition is exactly what makes the cone "compatible with the structure" of $D$, and it is the only sensible requirement to impose.

The decisive observation — the one that makes the definition feel inevitable rather than ad hoc — is that this commutativity is *precisely* the [[Def - Natural Transformation|naturality]] condition for a natural transformation $\lambda : \Delta_X \Rightarrow D$ from the constant functor at $X$. The constant functor sends every object to $X$ and every morphism to $1_X$; a natural transformation out of it assigns to each $j$ a component $\lambda_j : X \to D_j$, and its naturality square for $f : j \to k$ reads $D(f) \circ \lambda_j = \lambda_k \circ 1_X = \lambda_k$ — exactly the cone condition. So a cone is not a new gadget: it is a natural transformation $\Delta_X \Rightarrow D$, and the whole theory of [[Def - Limit and Colimit|limits]] is the theory of *universal* natural transformations out of constant functors. This is why limits live naturally in [[Def - Functor Category|functor categories]].

A cocone is the dual: reverse the legs. A cocone under $D$ with nadir $X$ is a family $\mu_j : D_j \to X$ with $\mu_k \circ D(f) = \mu_j$ for each $f : j \to k$ — an object *below* the diagram receiving a compatible leg from each vertex, equivalently a natural transformation $D \Rightarrow \Delta_X$. The choice of "over/under" and "apex/nadir" is purely a visual convention; what matters is the direction of the legs, into the diagram (cone) or out of it (cocone). The reason both are needed is that limits are universal cones and colimits are universal cocones, and the two are genuinely different objects in almost every category.

---

# The Definition

Let $D : J \to \mathcal{C}$ be a diagram of shape $J$.

A **cone over $D$ with apex (or summit) $X \in \mathcal{C}$** is a natural transformation $\lambda : \Delta_X \Rightarrow D$. Explicitly, it is a family of morphisms, the **legs**,
$$\big(\lambda_j : X \to D_j\big)_{j \in J},$$
such that for every morphism $f : j \to k$ in $J$,
$$D(f) \circ \lambda_j = \lambda_k.$$

A **cocone under $D$ with nadir $X$** is a natural transformation $\mu : D \Rightarrow \Delta_X$: a family of legs $\big(\mu_j : D_j \to X\big)_{j \in J}$ such that for every $f : j \to k$,
$$\mu_k \circ D(f) = \mu_j.$$

A **morphism of cones** from $(\lambda : \Delta_X \Rightarrow D)$ to $(\lambda' : \Delta_{X'} \Rightarrow D)$ is a morphism $h : X \to X'$ in $\mathcal{C}$ such that $\lambda'_j \circ h = \lambda_j$ for every $j$ — a map between apexes through which each leg of the source factors. Cones over $D$ and their morphisms form the **category of cones over $D$**. Dually, cocones under $D$ form the category of cocones, with a morphism $h : X \to X'$ satisfying $h \circ \mu_j = \mu'_j$.

---

# Relate to Other Fields / Compression

A cone is the categorical form of a "compatible family", which appears everywhere under different names. In analysis and algebra, a **compatible system** in an inverse limit — a sequence $(x_n)$ with $f_{n,m}(x_n) = x_m$ for $n \ge m$ — is exactly a cone over the tower diagram, and the [[Def - Directed Set and Direct System|inverse system]] formalism is the special case $J = (\mathbb{N}, \ge)$. A **section** of a family of objects is a cone; a **gluing of local data** is a cocone. When you prove something "componentwise but compatibly", you are constructing a cone.

**True name:** a cone over $D$ is a natural transformation $\Delta_X \Rightarrow D$ — "a single object mapping into the whole diagram, consistently with the diagram's own arrows". The operational version: to give a cone is to give a leg for each vertex and check one triangle per edge. Once you internalise that a cone *is* a natural transformation, the fact that $\mathrm{Cone}(-, D) = \mathcal{C}^J(\Delta_{(-)}, D)$ is a functor — and limits are its representations — becomes transparent.

---

# Examples / Corollaries

**Is an instance — a cone over a discrete diagram is a family of maps.** If $J$ is discrete (only identity arrows), a cone over $D = (A_i)$ with apex $X$ is just a family $(\lambda_i : X \to A_i)$ with *no* commutativity conditions, since there are no non-identity edges. The universal such cone is the [[Def - Product and Coproduct|product]] $\prod_i A_i$. This is the simplest case and shows that "no edges" means "no compatibility".

**Is an instance — a cone over a parallel pair.** For $D = (f, g : A \rightrightarrows B)$, a cone with apex $X$ is a pair $\lambda_A : X \to A$, $\lambda_B : X \to B$ with $f \circ \lambda_A = \lambda_B$ and $g \circ \lambda_A = \lambda_B$; the two force $f \lambda_A = g \lambda_A$, so the cone reduces to a single map $X \to A$ equalizing $f, g$. The universal cone is the [[Def - Equalizer and Coequalizer|equalizer]].

**Is an instance — a cone over a cospan is a commuting square corner.** For $D = (A \to C \leftarrow B)$, a cone with apex $X$ is a pair $X \to A$, $X \to B$ agreeing over $C$. The universal cone is the [[Def - Pullback and Pushout|pullback]]. A cocone under the span $A \leftarrow C \to B$ is the data completing a pushout square.

**Is an instance — a cocone over a sequence is a colimit cocone.** For the tower $A_0 \to A_1 \to A_2 \to \cdots$ (shape $J = (\mathbb{N}, \le)$), a cocone with nadir $X$ is a compatible family $\mu_n : A_n \to X$ with $\mu_{n+1} \circ (A_n \to A_{n+1}) = \mu_n$. The universal cocone is the [[Def - Direct and Inverse Limits|direct (sequential) colimit]] $\varinjlim A_n$; the dual cone over $A_0 \leftarrow A_1 \leftarrow \cdots$ has the inverse limit as its universal member.

**Is NOT an instance — an incompatible family is not a cone.** A family of maps $\lambda_j : X \to D_j$ that fails the triangle condition for some edge $f : j \to k$ — that is, $D(f) \circ \lambda_j \ne \lambda_k$ — is not a cone, even though it is a perfectly good family of maps. In $\mathbf{Set}$, with $D = (f, g : A \rightrightarrows B)$ and $\lambda_A : X \to A$ chosen so that $f \lambda_A \ne g \lambda_A$, no choice of $\lambda_B$ makes a cone, because the apex's single map to $A$ cannot satisfy both triangles at once. Compatibility is a real constraint.

**Calibration check.** Verify that the identity cone $\Delta_D \Rightarrow D$... — more precisely, that for the trivial shape $J = \{\bullet\}$ a cone with apex $X$ is just a single morphism $X \to D_\bullet$. Check that a morphism of cones into a *limit* cone is unique. If you can state the cocone conditions by reversing every arrow in the cone conditions, you have understood the duality.

---

# Unlocked by This

> [!tip] Limits and Colimits *(from this chapter)*
> A cone and cocone are exactly the raw material of [[Def - Limit and Colimit|limits and colimits]]: a limit is the *universal* (terminal) cone, a colimit the *universal* (initial) cocone. Everything in this chapter — products, equalizers, pullbacks and their duals — is a universal (co)cone over a chosen shape $J$.

> [!tip] Weighted Limits and Ends *(from Enriched Category Theory)*
> Replacing the constant-functor apex by a general **weight** functor $W : J \to \mathbf{Set}$ gives **weighted limits**; the diagonal case $J^{op} \times J$ gives **ends and coends**, the integral calculus of category theory used for Kan extensions and the **enriched** Yoneda lemma (Chapter VII).
