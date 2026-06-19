---
type: theorem
subject: category-theory
prereqs:
  - "Def - Limit and Colimit"
  - "Def - Product and Coproduct"
  - "Def - Equalizer and Coequalizer"
  - "Def - Complete and Cocomplete Category"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]], $J$ a small index category with object-set $\mathrm{ob}\,J$ and morphism-set $\mathrm{mor}\,J$, and $D : J \to \mathcal{C}$ a diagram with objects $D_j$ and maps $D(f) : D_j \to D_k$ for $f : j \to k$. We write $\prod$ for [[Def - Product and Coproduct|products]] with projections $\pi$, and $\mathrm{eq}$ for [[Def - Equalizer and Coequalizer|equalizers]]. For a morphism $f$ of $J$ we write $\mathrm{dom}\,f$ and $\mathrm{cod}\,f$ for its source and target objects. The full registry is on [[Category Theory III — Limits and Colimits]].

---

# Statement

> **Theorem (products and equalizers give all limits).** Let $\mathcal{C}$ be a category and $D : J \to \mathcal{C}$ a diagram with $J$ small. Suppose the products $P = \prod_{j \in \mathrm{ob}\,J} D_j$ and $Q = \prod_{f \in \mathrm{mor}\,J} D_{\mathrm{cod}\,f}$ exist in $\mathcal{C}$. Define two morphisms $s, t : P \to Q$ by their components: for each $f : j \to k$ in $J$,
> $$\pi_f \circ s = \pi_k \qquad\text{and}\qquad \pi_f \circ t = D(f) \circ \pi_j,$$
> where $\pi_j : P \to D_j$ and $\pi_f : Q \to D_k$ are the product projections. Then the limit of $D$ exists and is the equalizer of $s$ and $t$:
> $$\lim D \;=\; \mathrm{eq}\big(s, t : P \rightrightarrows Q\big),$$
> with limit projections $\pi_j \circ e$, where $e : \mathrm{eq}(s,t) \to P$ is the equalizer inclusion.

> **Corollary (criterion for completeness).** If $\mathcal{C}$ has all small products and all equalizers, then $\mathcal{C}$ is [[Def - Complete and Cocomplete Category|complete]]. If $\mathcal{C}$ has all *finite* products and all equalizers, then $\mathcal{C}$ has all finite limits. Dually, all small coproducts and coequalizers make $\mathcal{C}$ cocomplete, with $\operatorname{colim} D$ the coequalizer of two maps between coproducts.

---

# Motivation

There are infinitely many shapes $J$, hence infinitely many kinds of limit, and checking a category against each shape separately would be hopeless. This theorem collapses the infinite checklist to *two* items. It says that products and equalizers are not merely two examples of limits among many — they are a *generating set*: every limit is assembled from a product (to gather all the vertices) and an equalizer (to impose the edges). Once you have those two constructions, you have all of them, for free.

The motivation is entirely practical. To prove that $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Top}$, $\mathbf{Mod}_R$ are [[Def - Complete and Cocomplete Category|complete]], you do not verify pullbacks, inverse limits, and equalizers of large diagrams one at a time; you verify products and equalizers, and this theorem supplies the rest. It is the reduction that makes completeness a finite verification, and it is the reason the [[Def - Complete and Cocomplete Category|definition of complete]] can be stated as "has products and equalizers". The formula also tells you *how* to compute any limit explicitly: build the product over the vertices, then cut out the sub-object where the edges are respected. That "cutting out by an equation" is the equalizer, and the equation is "the projection to $D_k$ agrees with the composite-through-$f$".

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "has products and equalizers". The skill is recognising, in a category presented some other way, that it secretly has these.

The first disguised source is **a category equipped with a limit-creating functor to $\mathbf{Set}$ (or another complete category)**. If a [[Def - Functor|forgetful functor]] $U : \mathcal{C} \to \mathbf{Set}$ [[Def - Preservation, Reflection, and Creation of Limits|creates limits]], then because $\mathbf{Set}$ has products and equalizers, so does $\mathcal{C}$, and the theorem makes $\mathcal{C}$ complete. The non-obvious step is that you never construct the product or equalizer in $\mathcal{C}$ by hand — you inherit them from $\mathbf{Set}$ through creation. *Example problem:* show $\mathbf{Grp}$ is complete by noting $U : \mathbf{Grp} \to \mathbf{Set}$ creates products (the direct product) and equalizers (the agreement-subgroup), then invoke the theorem.

The second disguised source is **a category with a terminal object and pullbacks**. Products are pullbacks over the terminal object and equalizers are pullbacks of the diagonal, so "terminal object + pullbacks" is logically equivalent to "products + equalizers" in the *finite* case. The non-obviousness is the translation: a problem that hands you fibre products and a one-point object has secretly handed you all finite limits. *Example problem:* show a category of sheaves, presented as having a terminal sheaf and fibre products, is finitely complete.

The third disguised source is **a functor category or a slice category over a complete base**. If $\mathcal{C}$ is complete then $\mathcal{C}^{\mathcal{A}}$ and $\mathcal{C}/c$ are complete, with limits computed [[Thm - Limits in Set and in Functor Categories|pointwise]] (resp. created by the projection). The non-obvious recognition is that "presheaves on $\mathcal{A}$" or "objects over $c$" inherit products and equalizers objectwise, so the theorem applies without rebuilding anything. *Example problem:* conclude that the presheaf category $[\mathcal{A}^{op}, \mathbf{Set}]$ is complete.

**Targets (Output Amplification)**

The conclusion is "$\lim D$ exists and equals an explicit equalizer of products".

Combine with **the explicit formula in $\mathbf{Set}$**. In $\mathbf{Set}$ the product is the cartesian product and the equalizer is the agreement-subset, so the theorem's formula specialises to $\lim D = \{(x_j) \in \prod_j D_j : D(f)(x_j) = x_k \text{ for all } f : j \to k\}$ — the set of compatible families. The further result is a *computational recipe* for every limit in $\mathbf{Set}$, and via [[Thm - Limits in Set and in Functor Categories|representability]] for every limit in any category, expressed as compatible families of maps. See [[Thm - Limits in Set and in Functor Categories]].

Combine with **the dual statement**. Reading the theorem in $\mathcal{C}^{op}$ gives: coproducts and coequalizers generate all colimits, with $\operatorname{colim} D$ the coequalizer of two maps between coproducts. The further result is that establishing cocompleteness also reduces to two checks; this is how one proves $\mathbf{Set}$ and $\mathbf{Top}$ cocomplete and how the **small object argument** (in model categories) builds colimits.

Combine with **finiteness control**. If you only have *finite* products and equalizers you get all *finite* limits; tracking the cardinality of $\mathrm{ob}\,J$ and $\mathrm{mor}\,J$ through the construction shows a category with $\kappa$-small products and equalizers has all $\kappa$-small limits. The further result is the calibrated statements used for **lex** (finite-limit) categories, **$\kappa$-accessible** categories, and the **adjoint functor theorem**'s size hypotheses.

---

# Why Is It True

The idea is to separate the two jobs a limit does. A [[Def - Cone and Cocone|cone]] over $D$ has to do two things: it must supply a leg $\lambda_j : X \to D_j$ for *every vertex* $j$, and those legs must *respect every edge*, $D(f) \circ \lambda_j = \lambda_k$. The first job — a leg for every vertex, with no constraints — is exactly a map into the product $P = \prod_j D_j$. So a *family* of legs (forgetting compatibility) is precisely an element of $\mathcal{C}(X, P)$.

Now impose the edges. For each edge $f : j \to k$ the cone condition demands $D(f) \circ \lambda_j = \lambda_k$. Package all these demands into the big product $Q = \prod_{f} D_{\mathrm{cod}\,f}$, one slot per edge. There are two natural maps $P \to Q$: the map $t$ that, in the slot for $f : j \to k$, applies $D(f)$ to the $j$-component (this is "the left side of the cone equation"), and the map $s$ that just copies the $k$-component (the "right side"). A family of legs respects *all* the edges precisely when these two maps agree on it — that is, precisely when it lands in the equalizer $\mathrm{eq}(s, t)$.

> **A limit is "a leg per vertex (a product) subject to a relation per edge (an equalizer)".** The product gathers the vertices; the equalizer enforces the arrows; the equation $s = t$ literally *is* the cone-commutativity condition collected across all edges.

So the equalizer of $s$ and $t$ is exactly the universal object carrying a compatible family of legs — which is the limit. The construction is not a clever trick; it is the only way to express "compatible family" using the two primitives, and it works because "compatible family" decomposes cleanly into "family" (product) and "compatible" (equalizer). The reason the theorem needs *all* small products (not just binary) is that $J$ may have infinitely many vertices and edges, so $P$ and $Q$ are products over possibly infinite index sets — which is exactly why infinite products are needed for full (as opposed to finite) completeness.

---

# What Makes This Hard

The hard part is *defining the two maps $s, t : P \to Q$ correctly*, because they are specified component-wise through the universal property of $Q$, and the indexing is easy to get backwards. The slot of $Q$ indexed by $f : j \to k$ holds an element of $D_k = D_{\mathrm{cod}\,f}$; the map $t$ must put $D(f)(\text{$j$-th coordinate})$ there while $s$ puts the $k$-th coordinate, and swapping these or mis-indexing the product collapses the argument. The second subtlety is remembering that the limit *projections* are $\pi_j \circ e$ (project to the $j$-slot, after including the equalizer), not $\pi_j$ alone. Most errors are bookkeeping with the two product projections $\pi_j$ (on $P$) and $\pi_f$ (on $Q$), not conceptual.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Express "cone over $D$ with apex $X$" as "a map $X \to P$ that equalizes $s$ and $t$", then read off that the universal such object is $\mathrm{eq}(s,t)$. The product encodes the legs; the equalizer encodes the cone conditions.

**Subgoal decomposition:**

1. **Maps into $P$ are families of legs.** A map $X \to P = \prod_j D_j$ is the same as a family $(\lambda_j : X \to D_j)_j$, with no compatibility imposed.
   - *Hint:* This is the universal property of the product.
   - *Why needed:* It identifies the "leg data" of a cone with $\mathcal{C}(X, P)$.

2. **Define $s, t : P \to Q$.** Use the universal property of $Q = \prod_f D_{\mathrm{cod}\,f}$ to define $s$ by $\pi_f s = \pi_{\mathrm{cod}\,f}$ and $t$ by $\pi_f t = D(f) \circ \pi_{\mathrm{dom}\,f}$.
   - *Hint:* Each is determined by giving one component per edge $f$.
   - *Why needed:* $s = t$ on a family will encode all cone conditions at once.

3. **Equalizing $s, t$ = being a cone.** Show a family $\lambda : X \to P$ satisfies $s \lambda = t \lambda$ iff $D(f)\lambda_j = \lambda_k$ for all $f : j \to k$.
   - *Hint:* Compare $\pi_f s \lambda = \lambda_k$ with $\pi_f t \lambda = D(f)\lambda_j$ in each slot.
   - *Why needed:* It identifies cones with maps factoring through the equalizer.

4. **The equalizer is the limit.** Conclude $\mathrm{eq}(s,t)$ with legs $\pi_j \circ e$ is the universal cone.
   - *Hint:* A cone $X \to D$ corresponds to $X \to P$ equalizing $s,t$, which factors uniquely through $e$.
   - *Why needed:* Universality of the equalizer becomes universality of the limit.

---

# Lemma Decomposition

> [!note]- Lemma 1: Families of legs are maps into the product of vertices
> **Statement:** For $P = \prod_{j} D_j$, the assignment $\lambda \mapsto (\pi_j \circ \lambda)_j$ is a bijection between morphisms $X \to P$ and families $(\lambda_j : X \to D_j)_{j \in \mathrm{ob}\,J}$.
>
> **Hint:** This is precisely the universal property of the product, with no edge conditions involved.
>
> **Why needed:** It turns the "leg data" of a cone into a single arrow, the raw material the equalizer will constrain.
>
> > [!note]- Full proof
> > By the universal property of the product $\prod_j D_j$, a morphism $X \to \prod_j D_j$ is uniquely determined by, and conversely determines, a family of morphisms $(X \to D_j)_j$ via post-composition with the projections $\pi_j$. This is a natural bijection $\mathcal{C}(X, P) \cong \prod_j \mathcal{C}(X, D_j)$.

> [!note]- Lemma 2: Equalizing $s$ and $t$ encodes the cone conditions
> **Statement:** With $s, t : P \to Q$ defined by $\pi_f s = \pi_{\mathrm{cod}\,f}$ and $\pi_f t = D(f) \circ \pi_{\mathrm{dom}\,f}$, a map $\lambda : X \to P$ satisfies $s \circ \lambda = t \circ \lambda$ if and only if the family $(\lambda_j = \pi_j \lambda)$ is a cone, i.e. $D(f) \circ \lambda_j = \lambda_k$ for every $f : j \to k$.
>
> **Hint:** Two maps into a product agree iff they agree in every component; read the $f$-component of $s\lambda$ and $t\lambda$.
>
> **Why needed:** It is the heart of the theorem — it identifies "cone" with "equalizes $s,t$".
>
> > [!note]- Full proof
> > Two maps $X \to Q = \prod_f D_{\mathrm{cod}\,f}$ are equal iff their composites with every projection $\pi_f$ agree. For $f : j \to k$,
> > $$\pi_f \circ s \circ \lambda = \pi_{\mathrm{cod}\,f} \circ \lambda = \pi_k \circ \lambda = \lambda_k,$$
> > $$\pi_f \circ t \circ \lambda = D(f) \circ \pi_{\mathrm{dom}\,f} \circ \lambda = D(f) \circ \pi_j \circ \lambda = D(f) \circ \lambda_j.$$
> > Hence $s \lambda = t \lambda$ iff $\lambda_k = D(f)\lambda_j$ for every edge $f : j \to k$, which is exactly the cone condition.

> [!note]- Lemma 3: The equalizer of $s,t$ is the limit
> **Statement:** Let $e : E \to P$ be the equalizer of $s, t$. Then $(\pi_j \circ e : E \to D_j)_j$ is a limit cone over $D$.
>
> **Hint:** Cones over $D$ with apex $X$ correspond to maps $X \to P$ equalizing $s,t$, which factor uniquely through $e$.
>
> **Why needed:** It assembles Lemmas 1–2 into the universal property of the limit.
>
> > [!note]- Full proof
> > First, $(\pi_j e)$ is a cone: $e$ equalizes $s, t$, so by Lemma 2 its components satisfy the cone conditions. Now let $(\lambda_j : X \to D_j)$ be any cone. By Lemma 1 it gives a unique $\lambda : X \to P$ with $\pi_j \lambda = \lambda_j$; by Lemma 2, since $(\lambda_j)$ is a cone, $s\lambda = t\lambda$. By the universal property of the equalizer there is a unique $u : X \to E$ with $e u = \lambda$, hence $\pi_j e u = \pi_j \lambda = \lambda_j$ for all $j$ — so $u$ is a cone morphism into $(\pi_j e)$. Uniqueness of $u$ follows from uniqueness in the equalizer and product universal properties. Thus $(\pi_j e)$ is terminal among cones, i.e. a limit cone.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $D : J \to \mathcal{C}$ with $J$ small, and suppose $P = \prod_{j \in \mathrm{ob}\,J} D_j$ and $Q = \prod_{f \in \mathrm{mor}\,J} D_{\mathrm{cod}\,f}$ exist, as do all equalizers.
>
> **Step 0 — the products and equalizer exist.** By hypothesis $P$ and $Q$ exist; the maps $s, t$ defined below are morphisms $P \to Q$, so their equalizer exists by hypothesis. This is the well-posedness needed before the construction makes sense.
>
> **Step 1 — define $s, t : P \to Q$.** By the universal property of $Q$, define $s$ and $t$ by specifying, for each edge $f : j \to k$, their composites with $\pi_f : Q \to D_k$:
> $$\pi_f \circ s := \pi_k : P \to D_k, \qquad \pi_f \circ t := D(f) \circ \pi_j : P \to D_k.$$
> These determine $s, t$ uniquely.
>
> **Step 2 — cones are maps equalizing $s,t$.** By Lemma 1, a map $\lambda : X \to P$ is a family $(\lambda_j = \pi_j\lambda)$. By Lemma 2, $s\lambda = t\lambda$ iff $D(f)\lambda_j = \lambda_k$ for all $f : j \to k$, i.e. iff $(\lambda_j)$ is a cone over $D$.
>
> **Step 3 — form the equalizer.** Let $e : E \to P$ be the equalizer of $s$ and $t$. By Lemma 3, $(\pi_j \circ e)_j$ is a limit cone over $D$, so $\lim D$ exists and equals $E = \mathrm{eq}(s,t)$, with projections $\pi_j \circ e$.
>
> **Step 4 — completeness corollary.** If $\mathcal{C}$ has all small products and all equalizers, then for every small $D$ the objects $P, Q$ and the equalizer exist, so every small limit exists and $\mathcal{C}$ is complete. If $J$ is finite then $\mathrm{ob}\,J$ and $\mathrm{mor}\,J$ are finite, so only finite products are used, giving the finite-limit statement. The dual statements (coproducts + coequalizers $\Rightarrow$ cocomplete) follow by applying the theorem in $\mathcal{C}^{op}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Completeness of module categories from $\mathbf{Ab}$.** For a ring $R$, $\mathbf{Mod}_R$ has products (direct products of modules) and equalizers (the submodule where two homomorphisms agree), so by the theorem it is complete; the same two checks give cocompleteness via coproducts (direct sums) and coequalizers (cokernels). The application is non-obvious because one usually proves module categories complete by citing abelian-category machinery, whereas this gives it from two elementary constructions. See [[Ex - Set is complete and cocomplete]] for the $\mathbf{Set}$ template.

**Existence of inverse limits in topology.** A profinite group is an [[Def - Direct and Inverse Limits|inverse limit]] over a cofiltered diagram; this theorem guarantees it exists in $\mathbf{Grp}$ (or $\mathbf{Top}$) because the relevant infinite products and equalizers exist. The non-obvious point is that the existence of $\varprojlim$, which one might prove by hand with compatible-sequence constructions, is a corollary of "products + equalizers". This connects to [[Thm - The Inverse Limit and Completeness]].

**Solution-set checks in the adjoint functor theorem.** The General Adjoint Functor Theorem requires the domain to be complete; this theorem reduces verifying that hypothesis to checking products and equalizers, which is how one confirms a presented category (e.g. a category of algebras, a variety of universal algebra) is complete enough to admit free constructions. The application is non-obvious because the adjoint functor theorem is usually stated abstractly, but its completeness hypothesis is discharged precisely here.

---

# Bridges

- **[[Def - Complete and Cocomplete Category|Completeness]]** — this theorem is the *reason* the definition of complete can be phrased as "has products and equalizers". The bridge is the equalizer-of-products formula: it shows the apparently weaker hypothesis (two kinds of limit) implies the apparently stronger conclusion (all small limits), so the two formulations of completeness coincide. Without this theorem, "complete" and "has products and equalizers" would be distinct conditions.

- **[[Thm - Limits in Set and in Functor Categories|Limits in Set]]** — specialising the formula to $\mathcal{C} = \mathbf{Set}$ turns "equalizer of two maps between products" into "the subset of the product of vertices cut out by the cone equations", i.e. the set of compatible families. The bridge is that the abstract construction *becomes* the concrete compatible-family description once products are cartesian products and equalizers are agreement-subsets; this is then exported to all categories by representability.

- **[[Def - Pullback and Pushout|Pullbacks from products and equalizers]]** — the smallest interesting instance of this theorem. The pullback of $f : A \to C$, $g : B \to C$ is the equalizer of $f\pi_1, g\pi_2 : A \times B \rightrightarrows C$, which is exactly the formula here for the cospan-shaped diagram. The bridge shows the pullback is not an independent limit but the equalizer-of-product construction for one specific small shape.

---

# Unlocked by This

> [!tip] The Adjoint Functor Theorems *(from Chapter IV)*
> Completeness — guaranteed here by products and equalizers — is the standing hypothesis of the **General** and **Special Adjoint Functor Theorems**, which produce left adjoints to limit-preserving functors. The reduction to "products + equalizers" is how one verifies the hypothesis in practice for categories of algebras and presheaves.

> [!tip] The Small Object Argument *(from Model Categories, Chapter VI)*
> The dual construction — building colimits from coproducts and coequalizers, iterated transfinitely — is the **small object argument**, the engine that produces the functorial factorizations in a **model category**. The theorem's colimit form is the finite seed of that transfinite machine.
