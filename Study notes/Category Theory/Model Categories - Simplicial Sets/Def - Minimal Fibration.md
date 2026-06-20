---
type: definition
subject: model-categories
prereqs:
  - "Def - Kan Fibration and Anodyne Extension"
  - "Def - Simplicial Homotopy Group"
  - "Def - Kan Complex and the Nerve"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $p : E \to B$ is a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]] of [[Def - Simplicial Set|simplicial sets]]. Two $n$-simplices $\sigma, \tau \in E_n$ are **$p$-related** if they have the same image $p\sigma = p\tau$ in $B_n$ and the same boundary, $d_i\sigma = d_i\tau$ for all $i$. They are **fibrewise homotopic rel $\partial$**, written $\sigma \sim_p \tau$, if there is an $(n+1)$-simplex $H \in E_{n+1}$ that is a homotopy from $\sigma$ to $\tau$ fixing the boundary and lying over the degenerate homotopy $s_n(p\sigma)$ in $B$ (made precise below). A **fibrewise homotopy equivalence over $B$** between fibrations $p : E \to B$ and $p' : E' \to B$ is a pair of maps over $B$ whose composites are fibrewise homotopic to the identities. The full registry is on [[Model Categories — The Model Category of Simplicial Sets]].

---

# Axiom Motivation

The problem minimal fibrations solve is *rigidity*. A [[Def - Kan Fibration and Anodyne Extension|Kan fibration]] $p : E \to B$ carries a great deal of homotopical redundancy: over a single simplex of $B$ there can be many simplices of $E$ that are fibrewise homotopic to each other rel boundary but not equal. This redundancy is harmless for homotopy-theoretic purposes — fibrewise-homotopic simplices represent the same homotopy class — but it is fatal for any argument that needs to *transport a simplex along an isomorphism of the base and conclude equality*. The two most important such arguments are (a) showing that a fibration over a contractible base is a product (local triviality), and (b) Quillen's proof that geometric realisation preserves finite products. Both need "fibrewise homotopic $\Rightarrow$ equal", which is false in general. The definition of a minimal fibration is engineered to make exactly that implication true.

So we *define away* the redundancy. Call a Kan fibration **minimal** if any two $p$-related simplices that are fibrewise homotopic rel boundary are already equal. This is the strongest possible "no redundancy" condition: it says the simplices of $E$ are in bijection with their fibrewise homotopy classes, so the total space is as small as a fibration with the given homotopy type can be. The name is apt — among all fibrations fibrewise homotopy equivalent to a given one, the minimal models are the smallest.

The reason this is the right definition, rather than some weaker tidiness condition, is what it *buys*. Two theorems follow and justify it. First, **every Kan fibration admits a minimal model**: $E$ deformation-retracts fibrewise onto a sub-simplicial-set $E' \subseteq E$ on which $p$ restricts to a minimal fibration, and $E \to B$, $E' \to B$ are fibrewise homotopy equivalent. The construction is a transfinite "thinning": go through the simplices of $E$ in increasing dimension, and whenever two are fibrewise homotopic rel boundary, discard one; the Kan condition guarantees this can be done compatibly with faces. So minimality costs nothing — one can always reduce to it. Second, **minimal fibrations are fibre bundles**: if $p : E \to B$ is minimal and $B$ is connected, then $p$ is a *bundle* with constant fibre $F$ — pulling back along any simplex $\Delta^n \to B$ gives a product $F \times \Delta^n$. This is the simplicial form of local triviality, and it is *false* for non-minimal fibrations, where the pullback can be a non-trivial fibration over $\Delta^n$.

What breaks if we weaken "fibrewise homotopic rel $\partial$ $\Rightarrow$ equal" to, say, "$\Rightarrow$ equal up to a degeneracy"? Then degenerate redundancy survives, the simplex–class bijection fails, and the bundle theorem collapses: pullback along a simplex of $B$ no longer gives a strict product, only a fibration trivial up to homotopy — which is exactly the situation we were trying to escape. What if we strengthen it to "any two $p$-related simplices are equal", dropping the homotopy hypothesis? Then we are demanding that $p$ be a *monomorphism* on the relevant simplices, which forces the fibre to be a point — far too strong, killing all interesting fibrations. Minimality is the Goldilocks condition: weak enough that every fibration has a minimal model, strong enough that minimal fibrations are bundles.

---

# The Definition

Let $p : E \to B$ be a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]].

**Fibrewise homotopy rel boundary.** Two $n$-simplices $\sigma, \tau \in E_n$ with the same image $p\sigma = p\tau =: \beta$ and the same boundary ($d_i\sigma = d_i\tau$ for all $i$) are **fibrewise homotopic rel $\partial$**, $\sigma \sim_p \tau$, if there exists $H \in E_{n+1}$ with
$$d_n H = \sigma, \quad d_{n+1} H = \tau, \quad d_i H = s_n(d_i\sigma)\ (0 \le i \le n-1), \quad p H = s_n \beta.$$
That is, $H$ is a simplicial homotopy from $\sigma$ to $\tau$ that is constant on the boundary and projects to the *degenerate* homotopy on $\beta$ — a homotopy living entirely in the fibre direction. Because $p$ is a Kan fibration this is an equivalence relation on the simplices over each $\beta$ with each fixed boundary.

**Minimal fibration.** The Kan fibration $p : E \to B$ is **minimal** if
$$\sigma \sim_p \tau \ \Longrightarrow\ \sigma = \tau$$
for all $n$ and all $\sigma, \tau \in E_n$: any two simplices that are $p$-related (same projection, same boundary) and fibrewise homotopic rel $\partial$ are equal. A **minimal Kan complex** is a minimal fibration over the point $\ast = \Delta^0$ — a Kan complex in which homotopic-rel-boundary simplices coincide.

**Minimal model.** A **minimal model** of a Kan fibration $p : E \to B$ is a sub-simplicial-set $E' \subseteq E$ that is a strong fibrewise deformation retract of $E$ over $B$, such that $p|_{E'} : E' \to B$ is a minimal fibration. Every Kan fibration has a minimal model, and any two minimal models of $p$ are isomorphic over $B$.

---

# Categorical / Structural Definition

Structurally, a minimal fibration is a **fibre bundle** internal to $\mathbf{sSet}$: a Kan fibration that is locally (over each simplex of the base) a product. Precisely, $p : E \to B$ is a minimal fibration if and only if for every simplex $\beta : \Delta^n \to B$ the [[Def - Pullback and Pushout|pullback]] $\beta^* E \to \Delta^n$ is isomorphic over $\Delta^n$ to the projection $F \times \Delta^n \to \Delta^n$, with $F$ the fibre, *and* these trivialisations are compatible under the face and degeneracy maps of $B$. The compatible trivialisations assemble into a single datum: an action of the [[Def - Path-Product and the Fundamental Group|fundamental groupoid]] $\Pi_1(B)$ (more precisely the fundamental ∞-groupoid) on the fibre $F$ by self-equivalences. So a minimal fibration over a connected $B$ is *classified* by a fibre $F$ together with a homotopy action of the loops of $B$ — exactly the data of a fibration in the homotopy-theoretic sense, now made strict.

This is the simplicial incarnation of the classical statement that fibrations over a paracompact base are classified by maps into a classifying space $B\mathrm{hAut}(F)$. Minimality is what turns the *homotopy class* of classifying data into an *isomorphism class* of strict bundles: among all fibrations with a given classifying map, the minimal one is the canonical strict representative. The structural slogan is **minimal fibration = strictified homotopy fibration = fibre bundle with structure ∞-group $\mathrm{hAut}(F)$**.

---

# Relate to Other Fields / Compression

A minimal fibration is the combinatorial form of a **fibre bundle**, and the existence of minimal models is the combinatorial form of the topological fact that every [[Def - Kan Fibration and Anodyne Extension|Serre fibration]] is, up to fibre homotopy equivalence, as rigid as a bundle. The compression: **a Kan fibration carries redundant simplices; minimise to remove them, and what is left is a bundle.** This trades a flabby fibration for a rigid one of the same fibre homotopy type, the exact move needed whenever a proof requires "homotopic $\Rightarrow$ equal".

In differential geometry the analogue is choosing a *connection* or a *good cover* to make a fibre bundle locally trivial in a usable way; here the minimisation plays that role purely combinatorially, with no smoothness or local-triviality input — it is generated entirely by horn-filling. The minimal Kan complex (minimal fibration over a point) is the analogue of a CW complex with no redundant cells, or of a reduced word in combinatorial group theory: the smallest representative of a homotopy type.

**True name:** a minimal fibration is **"a Kan fibration with no redundant simplices — a combinatorial fibre bundle"**, and the operational fact is the slogan *every Kan fibration retracts fibrewise onto a minimal one*. When you see "minimal fibration", picture a fibre bundle; when a proof needs rigidity, the trigger-reaction is *minimise first*.

---

# Examples / Corollaries

**Is an instance — the projection $F \times B \to B$ for $F$ a minimal Kan complex.** If $F$ is a minimal Kan complex then the trivial bundle $F \times B \to B$ is a minimal fibration: two simplices over the same base simplex with the same boundary that are fibrewise homotopic differ only in the $F$-coordinate, and minimality of $F$ forces them equal. These trivial bundles are the local model every minimal fibration is built from.

**Is an instance — a minimal model of $\mathrm{Sing}(p)$ for a Serre fibration $p$.** For a Serre fibration $p : E \to B$ of [[Def - Topological Space|spaces]], the Kan fibration $\mathrm{Sing}(p) : \mathrm{Sing}(E) \to \mathrm{Sing}(B)$ has a minimal model $M \subseteq \mathrm{Sing}(E)$, a minimal fibration over $\mathrm{Sing}(B)$ fibrewise homotopy equivalent to it. This minimal model is the combinatorial fibre bundle that Quillen uses to prove geometric realisation preserves products (see [[Thm - Geometric Realization is a Quillen Equivalence]]).

**Is an instance — a minimal Kan complex of a space, e.g. an Eilenberg–MacLane complex.** A minimal model of $\mathrm{Sing}(Y)$ for a connected space $Y$ is a minimal Kan complex $M_Y$ with $\pi_n(M_Y) \cong \pi_n(Y)$ and no redundant simplices — the smallest simplicial set carrying the homotopy type of $Y$. For $Y = K(A, n)$ an Eilenberg–MacLane space, the minimal model is the standard minimal $K(A,n)$ complex with $n$-simplices a copy of $A$ and everything above forced.

**Is NOT minimal — a non-trivial Kan fibration with redundant simplices.** The path fibration $P X \to X$ (paths starting at the basepoint, evaluated at the endpoint) realised simplicially is a Kan fibration that is *not* minimal: the contractible total space $PX$ has many fibrewise-homotopic distinct simplices over each base simplex. Its minimal model collapses the contractible total space down, exhibiting $PX \to X$ as fibrewise equivalent to the based-loop bundle $\Omega X \to PX \to X$ in rigid form. The non-minimality is exactly the contractible redundancy of the path space.

**Is NOT minimal — $\mathrm{Sing}(Y)$ itself for $Y \neq \ast$.** The singular complex $\mathrm{Sing}(Y)$ of a non-point space is essentially never minimal: it contains *every* singular simplex, so over any vertex it has uncountably many homotopic-rel-boundary simplices. This is why one passes to a minimal model — $\mathrm{Sing}(Y)$ is the largest model of the homotopy type, the minimal model the smallest.

**Corollary — minimal fibrations are bundles; minimal models are unique.** If $p : E \to B$ is a minimal fibration and $\beta : \Delta^n \to B$ is any simplex, then $\beta^* E \cong F \times \Delta^n$ over $\Delta^n$: a minimal fibration is locally a product. Moreover any two minimal models of a given Kan fibration are isomorphic over $B$ (the thinning is canonical up to isomorphism), so "the" minimal model is well-defined up to isomorphism.

**Corollary — a fibrewise homotopy equivalence of minimal fibrations is an isomorphism.** If $p, p'$ are minimal fibrations over $B$ and $f : E \to E'$ is a fibrewise homotopy equivalence over $B$, then $f$ is an isomorphism. Minimality removes the slack in which a homotopy equivalence could fail to be invertible — this is the rigidity that makes minimal models unique and powers the product-preservation proof.

**Calibration check.** Verify that a minimal fibration over the point is a minimal Kan complex, and that the trivial bundle $F \times B \to B$ is minimal iff $F$ is a minimal Kan complex. Explain why $\mathrm{Sing}(Y)$ is not minimal for $Y \neq \ast$, and why minimisation is therefore necessary. And state the two theorems that justify the definition: existence of minimal models, and minimal-fibrations-are-bundles.

---

# Unlocked by This

> [!tip] Geometric Realisation Preserves Products *(from this chapter)*
> The key lemma behind [[Thm - Geometric Realization is a Quillen Equivalence]] — that $|{-}|$ preserves finite products and that realisation of a minimal fibration is a (Serre) fibre bundle — is proved by minimising: a minimal fibration is a bundle, bundles realise to bundles, and products of bundles behave. Minimality is the rigidity that makes the comparison go through.

> [!tip] Classification of Fibrations *(from Algebraic Topology)*
> Since minimal fibrations over a connected base are classified by their fibre together with a homotopy action of the loops, they give the simplicial form of the **classification of fibrations** by maps into $B\mathrm{hAut}(F)$ — the foundation of obstruction theory and of the theory of **classifying spaces** for structured fibrations.

> [!tip] Minimal Models in Rational Homotopy Theory *(from Homotopy Theory)*
> The idea "replace an object by the smallest one of the same homotopy type, with no redundancy" recurs as the **minimal Sullivan model** of a rational homotopy type — a minimal free commutative differential graded algebra. The minimal Kan complex is its unstable, integral ancestor.
