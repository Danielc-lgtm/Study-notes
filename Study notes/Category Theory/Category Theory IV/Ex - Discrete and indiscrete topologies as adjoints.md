---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Adjunction"
  - "Def - Topological Space"
  - "Def - Free-Forgetful Adjunction"
tags: [category-theory, foundations]
---

# Problem Statement

Let $U : \mathbf{Top}\to\mathbf{Set}$ be the forgetful functor sending a topological space to its underlying set. Define two functors $\mathbf{Set}\to\mathbf{Top}$:
- $\mathrm{Disc}$, equipping a set $S$ with the **discrete** topology (every subset open);
- $\mathrm{Indisc}$, equipping $S$ with the **indiscrete** topology (only $\emptyset$ and $S$ open).

**(a)** Prove $\mathrm{Disc}\dashv U$: $\mathbf{Top}(\mathrm{Disc}\,S, Y)\cong\mathbf{Set}(S, UY)$.

**(b)** Prove $U\dashv\mathrm{Indisc}$: $\mathbf{Top}(X, \mathrm{Indisc}\,S)\cong\mathbf{Set}(UX, S)$.

**(c)** Conclude the chain $\mathrm{Disc}\dashv U\dashv\mathrm{Indisc}$ and identify the units and counits.

**Recall:**

A [[Def - Topological Space|topological space]] $(X,\tau)$ is a set with a collection $\tau$ of open sets closed under arbitrary unions and finite intersections, containing $\emptyset, X$. A [[Def - Continuous Map|continuous map]] is one whose preimages of opens are open. The discrete topology is the *finest* (largest $\tau$); the indiscrete is the *coarsest* (smallest $\tau$).

![[Def - Adjunction#The Definition]]

---

# Convergent Strategy

**Problem class:** This is an "exhibit adjunctions on both sides of a forgetful functor" problem — the cleanest example of a functor with both a left and a right adjoint, illustrating that the discrete functor is "free" and the indiscrete functor is "cofree".

**Assumption pattern:** The decisive facts are: *every* function out of a discrete space is continuous (finest topology, so all preimages are open), and *every* function into an indiscrete space is continuous (coarsest topology, so the only opens to pull back are $\emptyset, S$, with open preimages). These two "every function is continuous" facts are exactly the two adjunction bijections.

**Theorem routing:** For (a), "continuous maps out of $\mathrm{Disc}\,S$ $=$ all functions out of $S$" gives $\mathrm{Disc}\dashv U$. For (b), "continuous maps into $\mathrm{Indisc}\,S$ $=$ all functions into $S$" gives $U\dashv\mathrm{Indisc}$. Then [[Def - Adjunction|the definition]] assembles the chain, and units/counits are read off as in [[Def - Unit and Counit of an Adjunction]].

**Key decision point:** The non-obvious recognition is *which side each functor adjoins on*. The discrete functor is the **left** adjoint (it makes maps *out* free), the indiscrete the **right** adjoint (it makes maps *in* free). Getting this backwards inverts the bijection. The mnemonic: discrete topology lets you map *out* freely (left adjoint, "free"), indiscrete lets you map *in* freely (right adjoint, "cofree").

---

# Legal Operations Used

1. **Operation 2 from the topic page (recognise a forgetful functor and produce its free left adjoint).** $\mathrm{Disc}$ is the free (left adjoint) functor for $U : \mathbf{Top}\to\mathbf{Set}$.

2. **Operation 1 from the topic page (transpose across the adjunction).** Both bijections are "a continuous map is its underlying function", the transpose being literally the identity on underlying functions.

3. **Operation 6 from the topic page (compose adjunctions)** — implicitly, the chain $\mathrm{Disc}\dashv U\dashv\mathrm{Indisc}$ exhibits a functor with adjoints on both sides.

---

# Hints

> [!note]- Hint 1
> A function from a discrete space is *always* continuous (every preimage is a subset, hence open). So continuous maps $\mathrm{Disc}\,S\to Y$ are exactly functions $S\to UY$.

> [!note]- Hint 2
> A function into an indiscrete space is *always* continuous (the only opens are $\emptyset$ and the whole space, whose preimages are $\emptyset$ and the domain). So continuous maps $X\to\mathrm{Indisc}\,S$ are exactly functions $UX\to S$.

> [!note]- Hint 3
> Units and counits: for $\mathrm{Disc}\dashv U$, the unit $S\to U\mathrm{Disc}\,S$ is the identity function (the underlying set is unchanged), and the counit $\mathrm{Disc}\,UY\to Y$ is the identity-on-points continuous map refining $Y$'s topology to discrete. For $U\dashv\mathrm{Indisc}$, dually.

---

# Solution

Both adjunctions are the same one-line fact in two guises: maps out of a discrete space are unconstrained, maps into an indiscrete space are unconstrained. Each "unconstrained" is an adjunction bijection.

**Step 1: $\mathrm{Disc}\dashv U$ (part a).**

$\mathbf{Top}(\mathrm{Disc}\,S, Y)\cong\mathbf{Set}(S, UY)$, naturally.

> [!note]- Derivation
> A continuous map $\mathrm{Disc}\,S\to Y$ has an underlying function $S\to UY$; restriction to underlying functions is the candidate bijection $\Phi$. It is injective (a continuous map is determined by its underlying function). It is surjective: given *any* function $g : S\to UY$, the map $\mathrm{Disc}\,S\to Y$ with underlying function $g$ is continuous, because for any open $V\subseteq Y$ the preimage $g^{-1}(V)$ is a subset of $S$, hence open in the discrete topology. So every function lifts to a continuous map; $\Phi$ is a bijection.
>
> Naturality: postcomposition with continuous $k : Y\to Y'$ corresponds to postcomposition with $Uk$ on underlying functions; precomposition with $\mathrm{Disc}\,h$ corresponds to precomposition with $h$. So $\Phi$ is natural, and $\mathrm{Disc}\dashv U$.

**Step 2: $U\dashv\mathrm{Indisc}$ (part b).**

$\mathbf{Top}(X, \mathrm{Indisc}\,S)\cong\mathbf{Set}(UX, S)$, naturally.

> [!note]- Derivation
> A continuous map $X\to\mathrm{Indisc}\,S$ has underlying function $UX\to S$; restriction is the candidate bijection. Surjectivity: given any function $g : UX\to S$, the map $X\to\mathrm{Indisc}\,S$ with underlying function $g$ is continuous, because the only open sets of $\mathrm{Indisc}\,S$ are $\emptyset$ and $S$, whose preimages are $\emptyset$ and $X$ — both open in $X$. Injectivity and naturality as before. So $U\dashv\mathrm{Indisc}$.

**Step 3: The chain and its (co)units (part c).**

$\mathrm{Disc}\dashv U\dashv\mathrm{Indisc}$.

> [!note]- Derivation
> Combining Steps 1 and 2, $U$ has $\mathrm{Disc}$ as a left adjoint and $\mathrm{Indisc}$ as a right adjoint: $\mathrm{Disc}\dashv U\dashv\mathrm{Indisc}$.
>
> **For $\mathrm{Disc}\dashv U$:** unit $\eta^L_S : S\to U\mathrm{Disc}\,S = S$ is the identity function (discrete space has the same underlying set). Counit $\varepsilon^L_Y : \mathrm{Disc}\,UY\to Y$ is the identity-on-underlying-set, continuous because the discrete topology is finer than $Y$'s — it is the canonical "discretization-to-$Y$" map.
>
> **For $U\dashv\mathrm{Indisc}$:** unit $\eta^R_X : X\to\mathrm{Indisc}\,UX$ is the identity-on-points map from $X$ to its underlying set with the indiscrete topology, continuous because indiscrete is coarser than $X$. Counit $\varepsilon^R_S : U\mathrm{Indisc}\,S = S\to S$ is the identity function.
>
> The repeated appearance of identity functions reflects that $U\mathrm{Disc} = \mathrm{id}_{\mathbf{Set}} = U\mathrm{Indisc}$: both $\mathrm{Disc}$ and $\mathrm{Indisc}$ are *sections* of $U$ (they leave the underlying set unchanged), so the units/counits on the $\mathbf{Set}$ side are identities. The content lives in the topology-changing (co)units on the $\mathbf{Top}$ side.

> [!note]- Complete formal solution
> **(a)** Restricting a continuous map to its underlying function gives $\Phi : \mathbf{Top}(\mathrm{Disc}\,S, Y)\to\mathbf{Set}(S, UY)$. It is a bijection because every function $S\to UY$ is continuous out of the discrete topology (all preimages open). Natural in both variables. So $\mathrm{Disc}\dashv U$.
>
> **(b)** Dually, every function $UX\to S$ is continuous into the indiscrete topology (only $\emptyset, S$ to pull back), giving $\mathbf{Top}(X,\mathrm{Indisc}\,S)\cong\mathbf{Set}(UX, S)$. So $U\dashv\mathrm{Indisc}$.
>
> **(c)** Hence $\mathrm{Disc}\dashv U\dashv\mathrm{Indisc}$. Units/counits: for $\mathrm{Disc}\dashv U$, $\eta^L_S = \mathrm{id}_S$ and $\varepsilon^L_Y : \mathrm{Disc}\,UY\to Y$ identity-on-points; for $U\dashv\mathrm{Indisc}$, $\eta^R_X : X\to\mathrm{Indisc}\,UX$ identity-on-points and $\varepsilon^R_S = \mathrm{id}_S$. $\blacksquare$

---

# Key Takeaways

**Discrete is "free" (left adjoint), indiscrete is "cofree" (right adjoint) — the handedness is dictated by which maps become unconstrained.** The discrete topology makes *every map out* continuous, so it sits on the left of the hom-set as the left adjoint to forgetting; the indiscrete topology makes *every map in* continuous, so it sits on the right as the right adjoint. This is the general principle that a *left* adjoint to a forgetful functor is the *finest/freest* structure and a *right* adjoint is the *coarsest/cofreest*. The same pattern appears wherever a forgetful functor has both adjoints: the discrete and codiscrete objects, the free and cofree constructions, the left and right Kan extensions. The trigger to look for *both* adjoints is a forgetful functor that "adds no data, only structure", where the finest and coarsest choices are both available.

**A functor with adjoints on both sides is common and structurally rich.** The chain $\mathrm{Disc}\dashv U\dashv\mathrm{Indisc}$ shows $U$ is simultaneously a left and a right adjoint, hence (by [[Thm - Right Adjoints Preserve Limits|RAPL/LAPC]]) preserves both limits *and* colimits — which is why the underlying set of a product, coproduct, quotient, or subspace of topological spaces is the corresponding set-level construction. Such "bireflective" or "adjoint string" situations recur: $\coprod\dashv\Delta\dashv\prod$ for the diagonal, the string $\pi_0\dashv\mathrm{Disc}\dashv U\dashv\mathrm{Indisc}$ extending this one by the connected-components functor, and the four-functor strings in algebraic geometry. When you find one adjoint, always ask whether there is another on the opposite side — the structure on the other side is often equally useful.

**Both adjoints are sections of $U$, so the interesting (co)units live on the structured side.** Because $\mathrm{Disc}$ and $\mathrm{Indisc}$ leave the underlying set unchanged ($U\mathrm{Disc} = U\mathrm{Indisc} = \mathrm{id}$), the units/counits on the $\mathbf{Set}$ side are identities, and the content is concentrated in the topology-comparing maps: $\mathrm{Disc}\,UY\to Y$ (refine to discrete) and $X\to\mathrm{Indisc}\,UX$ (coarsen to indiscrete). These comparison maps encode "$Y$'s topology is coarser than discrete" and "$X$'s topology is finer than indiscrete" — the two ends of the lattice of topologies on a fixed set. This illustrates a general phenomenon: when an adjoint is a section of the forgetful functor, the adjunction's information is the *comparison of structures*, not the change of underlying data, and the (co)unit is exactly that comparison. The companion exercise [[Ex - Abelianization is left adjoint to inclusion|Abelianization is left adjoint to inclusion]] is the contrasting case where the reflector genuinely changes the object (a quotient), so the unit is not an identity.
