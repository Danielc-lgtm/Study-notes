---
type: theorem
subject: category-theory
prereqs:
  - "Def - Adjunction"
  - "Def - Limit and Colimit"
  - "Thm - Representable Functors Preserve Limits"
  - "Thm - The Yoneda Lemma"
tags: [category-theory, foundations]
---

# Notation

$F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ with $F \dashv G$ (see [[Def - Adjunction]]). $K : \mathcal{J} \to \mathcal{D}$ is a diagram indexed by a small category $\mathcal{J}$; $\lim K$ denotes its [[Def - Limit and Colimit|limit]] (when it exists), with limit cone legs $\lambda_j : \lim K \to Kj$. We write $\mathcal{C}(A, -)$ for the covariant [[Def - Hom-Functor and Representable Functor|hom-functor]]. The full symbol registry is on [[Category Theory IV — Adjunctions]].

---

# Statement

> **Theorem (RAPL / LAPC).** Let $F \dashv G$ with $F : \mathcal{C} \to \mathcal{D}$ left adjoint to $G : \mathcal{D} \to \mathcal{C}$.
>
> - **(RAPL)** The right adjoint $G$ **preserves all limits** that exist in $\mathcal{D}$: if $K : \mathcal{J} \to \mathcal{D}$ has a limit $\lim K$, then $G(\lim K)$ is a limit of $GK$, with limit cone $G\lambda_j$. Equivalently $G(\lim K) \cong \lim (GK)$ canonically.
> - **(LAPC, dual)** The left adjoint $F$ **preserves all colimits** that exist in $\mathcal{C}$: $F(\mathrm{colim}\, D) \cong \mathrm{colim}(FD)$ canonically.
>
> There are **no size restrictions** on the index category $\mathcal{J}$: the statement holds for all small limits and colimits alike.

---

# Motivation

This is the workhorse of the chapter, the single most-used consequence of being an adjoint. It answers two everyday questions at once. First, *computational*: how does a functor interact with products, equalizers, pullbacks, kernels, inverse limits? If the functor is a right adjoint, it commutes with all of them — you may compute the limit before or after applying $G$ and get the same answer. Second, *diagnostic*: it gives the fastest test for whether a functor *can* be an adjoint. If a functor fails to preserve some limit (it does not send the terminal object to a terminal object, say), then it cannot be a right adjoint, so it has no left adjoint.

The pattern it explains is everywhere in algebra. The forgetful functor $\mathbf{Grp}\to\mathbf{Set}$ is a right adjoint, so it preserves limits: the underlying set of a product of groups is the product of the underlying sets, the underlying set of a kernel is the set-theoretic kernel. The free functor $\mathbf{Set}\to\mathbf{Grp}$ is a left adjoint, so it preserves colimits: the free group on a disjoint union is the free product (a coproduct), but the free group does *not* preserve products. The handedness of an adjoint dictates exactly which half of the (co)limit world it respects, and this theorem is the statement of that dictation.

The reason limits attach to *right* adjoints (and not left) is structural and worth holding onto: a limit is defined by a *contravariant* representation — $\lim K$ represents the functor $A \mapsto \lim_j \mathcal{C}(A, Kj)$ of cones — and the right adjoint sits on the right of the hom-set, exactly where it can be commuted past that representation.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "$G$ is a right adjoint", so the source question is: *what tells you a functor is a right adjoint without naming the adjunction explicitly?*

The first source is **a forgetful functor**. Forgetful functors (to $\mathbf{Set}$, or to a less-structured category) are right adjoints by reflex, because their left adjoints are the free constructions. So *any* forgetful functor preserves limits. *Example problem:* compute the product, equalizer, or inverse limit of a diagram of groups by computing it on underlying sets and then equipping the result with the unique group structure — legitimate exactly because $U$ preserves limits.

The second source is **the inclusion of a reflective subcategory**. The inclusion $\iota : \mathcal{D}\hookrightarrow\mathcal{C}$ of a [[Def - Reflective Subcategory|reflective subcategory]] is a right adjoint (to the reflector), so it preserves limits — which is *why* a reflective subcategory is closed under limits taken in the ambient category. *Example problem:* show a product of sheaves is a sheaf, or a product of complete metric spaces is complete, by invoking that the inclusion preserves limits.

The third source is **a representable functor**, the base case. The hom-functor $\mathcal{C}(A, -)$ preserves limits ([[Thm - Representable Functors Preserve Limits|representable functors preserve limits]]); this is the special case of RAPL where $G = \mathcal{C}(A,-) : \mathcal{C}\to\mathbf{Set}$ is right adjoint to $(-)\times A$-style functors, and it is the lemma the general proof reduces to. *Example problem:* deduce that a limit cone is detected by all hom-sets, i.e. $\mathcal{C}(A, \lim K) \cong \lim \mathcal{C}(A, Kj)$.

**Targets (Output Amplification)**

The conclusion is "$G$ preserves limits"; combined with other facts it does more.

Combine with **the contrapositive for non-existence of adjoints**: if $G$ does *not* preserve some limit (say it sends a terminal object to a non-terminal object), then $G$ is not a right adjoint, so $G$ has no left adjoint. The further result $E$ is a swift impossibility proof: the forgetful functor $\mathbf{Field}\to\mathbf{Set}$ has no left adjoint because the relevant (co)limits misbehave; a functor that does not preserve products cannot be a right adjoint.

Combine with **completeness transfer**: if $\mathcal{D}$ is [[Def - Complete and Cocomplete Category|complete]] and $G : \mathcal{D}\to\mathcal{C}$ is a right adjoint that is also *conservative* or *creates* limits, you can transport completeness and compute limits in $\mathcal{C}$ via $\mathcal{D}$. The further result is a method for proving a category is complete by exhibiting a limit-creating right adjoint to a complete category — the standard route to "$\mathbf{Grp}, \mathbf{Ring}, \mathbf{Top}$ are complete".

Combine with **the explicit limit formula**: RAPL plus the construction of limits from products and equalizers ([[Thm - Products and Equalizers Give All Limits|products and equalizers give all limits]]) lets you verify a functor preserves *all* limits by checking only that it preserves products and equalizers. The further result is an economical preservation test.

---

# Why Is It True

The proof is a chain of natural isomorphisms, and every link is something you already believe. Pick any test object $A \in \mathcal{C}$ and ask how the hom-set $\mathcal{C}(A, G(\lim K))$ behaves. Use the adjunction to slide $A$ across: $\mathcal{C}(A, G(\lim K)) \cong \mathcal{D}(FA, \lim K)$. Now $\lim K$ is a limit *in $\mathcal{D}$*, and a hom-functor into a limit distributes over the limit — that is [[Thm - Representable Functors Preserve Limits|representable functors preserve limits]] — so $\mathcal{D}(FA, \lim K) \cong \lim_j \mathcal{D}(FA, Kj)$. Slide $A$ back across the adjunction inside the limit: $\lim_j \mathcal{D}(FA, Kj) \cong \lim_j \mathcal{C}(A, GKj)$. And distribute the hom-functor back out of the limit: $\lim_j \mathcal{C}(A, GKj) \cong \mathcal{C}(A, \lim_j GKj)$. Read end to end:
$$\mathcal{C}(A, G(\lim K)) \;\cong\; \mathcal{C}(A, \lim (GK)) \qquad \text{naturally in } A.$$
The object $G(\lim K)$ and the object $\lim(GK)$ have *naturally isomorphic* hom-functors. By the [[Thm - The Yoneda Lemma|Yoneda lemma]], they are isomorphic — and a careful chase shows the isomorphism is the canonical comparison built from the cone $G\lambda_j$. So $G(\lim K)$ *is* the limit of $GK$.

> **The mechanism in one line:** the adjunction lets you slide the test object $A$ across the hom-set, where it meets a limit it can be commuted past (because representables preserve limits), and Yoneda turns the resulting natural iso of hom-functors into an iso of objects.

The reason there is no size restriction is that nothing in this chain cares how big $\mathcal{J}$ is: the adjunction bijection and the distribution of $\mathcal{C}(A,-)$ over limits hold for limits of any shape. Left adjoints preserve colimits by the dual argument (run it in the opposite categories, where colimits become limits and the handedness flips).

---

# What Makes This Hard

The conceptual difficulty is remembering *which* handedness preserves *which* (co)limit — the single most common error in the entire subject is "the free functor preserves products". The trick to never forgetting: limits are defined by mapping *in* and live on the right of the hom-set, so the *right* adjoint (which sits on the right) preserves them. The technical subtlety in the proof is that the chain of isomorphisms only shows the hom-functors agree; one must invoke Yoneda to descend to an isomorphism of objects, and then verify the isomorphism is the canonical cone-comparison and not just *some* isomorphism — otherwise you have shown $G(\lim K)$ and $\lim(GK)$ are abstractly isomorphic without knowing $G$ sends the limit cone to the limit cone.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Probe $G(\lim K)$ by all hom-sets $\mathcal{C}(A, -)$. Slide $A$ across the adjunction, use that representables preserve limits to commute past the limit, slide back, and apply Yoneda.

**Subgoal decomposition:**

1. **Slide across the adjunction.** Show $\mathcal{C}(A, G(\lim K)) \cong \mathcal{D}(FA, \lim K)$ naturally in $A$.
   - *Hint:* This is the adjunction bijection $\Phi$ at the object $\lim K$.
   - *Why needed:* Moves the test object to the $\mathcal{D}$ side, where the limit lives.

2. **Commute past the limit.** Show $\mathcal{D}(FA, \lim K) \cong \lim_j \mathcal{D}(FA, Kj)$.
   - *Hint:* The covariant hom-functor $\mathcal{D}(FA, -)$ preserves limits — [[Thm - Representable Functors Preserve Limits|representables preserve limits]].
   - *Why needed:* This is the only place the limit is actually used.

3. **Slide back, inside the limit.** Show $\lim_j \mathcal{D}(FA, Kj) \cong \lim_j \mathcal{C}(A, GKj)$.
   - *Hint:* Apply the adjunction bijection levelwise; it is natural, so it commutes with the limit.
   - *Why needed:* Returns to the $\mathcal{C}$ side with $GK$ in view.

4. **Distribute hom back out and apply Yoneda.** Show $\lim_j \mathcal{C}(A, GKj) \cong \mathcal{C}(A, \lim GK)$ and conclude $G(\lim K) \cong \lim GK$.
   - *Hint:* Hom into a limit is the limit of homs again; then Yoneda turns the natural iso of $\mathcal{C}(A,-)$-functors into an object iso, canonically via $G\lambda_j$.
   - *Why needed:* Descends from hom-functors to objects and identifies the comparison as the cone $G\lambda$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Covariant hom-functors preserve limits
> **Statement:** For any object $X$ and diagram $K : \mathcal{J}\to\mathcal{D}$ with limit $\lim K$, the natural map $\mathcal{D}(X, \lim K) \to \lim_j \mathcal{D}(X, Kj)$ is a bijection.
>
> **Hint:** A morphism into a limit is exactly a [[Def - Cone and Cocone|cone]] from $X$; a cone is exactly a compatible family, i.e. an element of $\lim_j\mathcal{D}(X, Kj)$.
>
> **Why needed:** It is the only nontrivial step in the chain — the place the limit's universal property is used.
>
> > [!note]- Full proof
> > By the universal property of $\lim K$, a morphism $X\to\lim K$ corresponds bijectively to a cone over $K$ with apex $X$: a family $(f_j : X\to Kj)$ with $K\alpha\circ f_j = f_{j'}$ for each $\alpha : j\to j'$ in $\mathcal{J}$. Such a compatible family is precisely an element of the limit $\lim_j\mathcal{D}(X, Kj)$ computed in $\mathbf{Set}$. The correspondence is natural in $X$ (postcomposition), giving the stated bijection.

> [!note]- Lemma 2: The adjunction bijection is natural and commutes with limits
> **Statement:** The family $\Phi_{A, B} : \mathcal{D}(FA, B)\cong\mathcal{C}(A, GB)$, being natural in $B$, induces an isomorphism $\lim_j\mathcal{D}(FA, Kj)\cong\lim_j\mathcal{C}(A, GKj)$.
>
> **Hint:** A natural isomorphism of $\mathbf{Set}$-valued functors induces an isomorphism of their limits, levelwise.
>
> **Why needed:** Lets you transport the limit of homs from the $\mathcal{D}$ side to the $\mathcal{C}$ side.
>
> > [!note]- Full proof
> > The maps $\Phi_{A, Kj}$ are bijections natural in $j$ (naturality in $B$, applied to the morphisms $K\alpha$). A natural isomorphism between two diagrams $\mathcal{J}\to\mathbf{Set}$ induces a bijection between their limits, since the limit is a functor of the diagram. Hence $\lim_j\mathcal{D}(FA, Kj)\cong\lim_j\mathcal{C}(A, GKj)$.

> [!note]- Lemma 3: Yoneda descends a hom-functor iso to an object iso, canonically
> **Statement:** If $\mathcal{C}(A, P)\cong\mathcal{C}(A, Q)$ naturally in $A$, then $P\cong Q$; if moreover the iso is induced by a cone $P\to Kj$ exhibiting $P$ over $GK$, the comparison is the canonical one.
>
> **Hint:** [[Thm - The Yoneda Lemma|Yoneda]]: a natural iso $\mathcal{C}(-, P)\cong\mathcal{C}(-, Q)$ comes from a unique iso $P\cong Q$; track the image of $1_P$.
>
> **Why needed:** Turns the chain of hom-set isomorphisms into a genuine isomorphism of objects sending the limit cone to the limit cone.
>
> > [!note]- Full proof
> > The composite natural iso $\mathcal{C}(A, G\lim K)\cong\mathcal{C}(A, \lim GK)$ is a natural iso of representable functors $\mathcal{C}\to\mathbf{Set}$. By the Yoneda lemma (fully faithful embedding), it is induced by a unique isomorphism $\theta : G\lim K\xrightarrow{\cong}\lim GK$. Chasing $1_{G\lim K}$ through the chain shows $\theta$ is the canonical map comparing the cone $(G\lambda_j : G\lim K\to GKj)$ with the limit cone of $GK$; hence $(G\lambda_j)$ *is* a limit cone for $GK$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F\dashv G$ with bijection $\Phi$, and let $K : \mathcal{J}\to\mathcal{D}$ have a limit $\lim K$ with cone $(\lambda_j : \lim K\to Kj)$.
>
> **Step 0 — what must be shown.** We must show $(G\lambda_j : G\lim K\to GKj)$ is a limit cone for the diagram $GK : \mathcal{J}\to\mathcal{C}$.
>
> **Step 1 — chain of natural isomorphisms.** For every $A\in\mathcal{C}$, natural in $A$:
> $$\mathcal{C}(A, G\lim K) \overset{\Phi}{\cong} \mathcal{D}(FA, \lim K) \overset{\text{Lem 1}}{\cong} \lim_j\mathcal{D}(FA, Kj) \overset{\text{Lem 2}}{\cong} \lim_j\mathcal{C}(A, GKj) \overset{\text{Lem 1}}{\cong} \mathcal{C}(A, \lim GK).$$
> The first uses the adjunction at $\lim K$; the second that $\mathcal{D}(FA,-)$ preserves limits; the third the levelwise adjunction (Lemma 2); the fourth that $\mathcal{C}(A,-)$ preserves limits.
>
> **Step 2 — descend via Yoneda.** The composite is a natural isomorphism $\mathcal{C}(-, G\lim K)\cong\mathcal{C}(-, \lim GK)$. By the [[Thm - The Yoneda Lemma|Yoneda lemma]] (Lemma 3) it is induced by a unique isomorphism $\theta : G\lim K\xrightarrow{\cong}\lim GK$, and the chase identifies $\theta$ with the canonical comparison sending the cone $(G\lambda_j)$ to the limit cone of $GK$.
>
> **Step 3 — conclude.** Therefore $(G\lambda_j)$ is a limit cone for $GK$, i.e. $G(\lim K)\cong\lim(GK)$ canonically. There were no size restrictions on $\mathcal{J}$.
>
> **Step 4 — the dual.** Applying the result to the adjunction $F^{op}\dashv$-style in $\mathcal{C}^{op}, \mathcal{D}^{op}$ (where $G^{op}$ is a *left* adjoint and limits become colimits) yields LAPC: the left adjoint $F$ preserves all colimits. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Underlying sets of algebraic limits.** Use RAPL to show that for any diagram of groups (or rings, or modules), the underlying set of the limit is the limit of the underlying sets: products, equalizers, kernels, and inverse limits are computed "on elements". This is the practical reason algebraic limits are easy. (See [[Ex - Right adjoints preserve limits in practice]].)

**Non-existence of free fields.** Show $\mathbf{Field}\to\mathbf{Set}$ has no left adjoint by exhibiting a (co)limit it would have to preserve and does not — the contrapositive use of LAPC. This is a surprising application: a *negative* existence result proved purely by a preservation obstruction.

**Sheaves are closed under limits.** Using that the inclusion of [[Def - Reflective Subcategory|sheaves into presheaves]] is a right adjoint, conclude a limit of sheaves (computed in presheaves, i.e. objectwise) is again a sheaf. Dually, colimits of sheaves are *not* objectwise — they are sheafified objectwise colimits, because the reflector (a left adjoint) preserves colimits. This delineates exactly where sheaf (co)limits diverge from presheaf ones.

**Geometric realization preserves colimits.** In algebraic topology, geometric realization $|{-}| : \mathbf{sSet}\to\mathbf{Top}$ is a left adjoint (to the singular functor), so it preserves colimits: the realization of a pushout of simplicial sets is a pushout of spaces. This is how CW structures are assembled and is a direct LAPC application.

---

# Bridges

- **[[Thm - Representable Functors Preserve Limits|Representable Functors Preserve Limits]]** — the base case and the lemma the proof reduces to. RAPL is "representables preserve limits, transported through the adjunction": the right adjoint borrows its limit-preservation from the hom-functor it represents.

- **[[Def - Reflective Subcategory|Reflective Subcategories]]** — an immediate application. The inclusion of a reflective subcategory is a right adjoint, so it preserves limits, which is *why* such subcategories are closed under limits; dually the reflector preserves colimits, so colimits in the subcategory are reflected ambient colimits.

- **[[Thm - The Adjoint Functor Theorem|The Adjoint Functor Theorem]]** — the converse direction. RAPL says limit-preservation is *necessary* for a right adjoint; the AFT says limit-preservation *plus* a solution set condition is *sufficient* for the existence of a left adjoint. The two theorems bracket the relationship between adjoints and limits.

- **[[Thm - Products and Equalizers Give All Limits|Products and Equalizers Give All Limits]]** — combines with RAPL to reduce "preserves all limits" to "preserves products and equalizers", an economical test.

---

# Unlocked by This

> [!tip] Brown Representability and Cohomology Theories *(from Algebraic Topology — Cluster 8)*
> RAPL's contrapositive — only limit/colimit-preserving functors can be adjoints — has a homotopical refinement, **Brown representability**: a functor on a nice homotopy category that sends colimits to limits is representable. This is how generalized cohomology theories are shown to be represented by spectra, and it is the homotopy-theoretic shadow of the [[Thm - The Adjoint Functor Theorem|Adjoint Functor Theorem]].

> [!tip] Exactness of Adjoint Functors *(from Homological Algebra)*
> In additive/abelian categories, RAPL/LAPC become **left/right exactness**: a right adjoint is left exact (preserves kernels), a left adjoint is right exact (preserves cokernels). This is why $\mathrm{Hom}$ is left exact and $\otimes$ right exact, and it is the launching point for **derived functors** (Tor, Ext) measuring the failure of exactness. See [[Thm - Tensoring is Right Exact|tensoring is right exact]].
