---
type: topic
subject: model-categories
chapter: "2.2-2.5"
title: "Model Categories — Examples in Detail"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation Registry

This chapter is the proving ground for the axioms set up in [[Model Categories — Quillen's Axiomatization of Homotopy Theory]]. There the five axioms were stated and the homotopy category was built abstractly; here we *check* the axioms on three concrete categories — chain complexes, topological spaces, and stable module categories — and read off what their homotopy categories are. We use the classical Quillen axioms MC1–MC5 throughout, and we freely use the language of [[Def - Cofibrant and Fibrant Objects|cofibrant and fibrant objects]], the [[Thm - The Retract Argument|retract argument]], and [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunctions]] from that chapter without re-deriving them.

A standing convention: $R$ denotes a ring, **associative with a unit $1$ but not necessarily commutative**, and "module" means **left $R$-module** unless stated otherwise. When $R$ is commutative this distinction evaporates. For the third section $R$ is a **Frobenius ring** (defined there), where the projective and injective modules coincide.

- $R$ — a ring (associative, unital, possibly non-commutative); $\mathbf{Mod}_R$ — left $R$-modules
- $\mathbf{Ch}(R)$ — chain complexes of left $R$-modules, with differential $d$ of degree $-1$ ($d_n : C_n \to C_{n-1}$, $d^2 = 0$)
- $H_n(C) = \ker d_n / \operatorname{im} d_{n+1}$ — the $n$-th **homology** of a complex $C$
- a **quasi-isomorphism** — a chain map inducing an isomorphism on every $H_n$; written $\xrightarrow{\sim}$
- $S^n$ — the **sphere complex**: the module $R$ concentrated in degree $n$, zero differential
- $D^n$ — the **disk complex**: $R$ in degrees $n$ and $n-1$ with the identity differential between them, so $H_*(D^n) = 0$
- $D(R)$ — the **derived category** of $R$, the homotopy category of $\mathbf{Ch}(R)$
- $\mathbf{Top}$ — topological spaces and continuous maps; $\mathbf{Top}_*$ — pointed spaces
- a **weak homotopy equivalence** — a map inducing isomorphisms on all [[Def - Higher Homotopy Group|homotopy groups]] $\pi_n$ (and a bijection on $\pi_0$); written $\xrightarrow{\sim}$
- a **Serre fibration** — a map with the homotopy lifting property against all disks $D^n$
- $S^{n-1} \hookrightarrow D^n$ — the boundary-sphere inclusion into the $n$-disk; $D^n \times \{0\} \hookrightarrow D^n \times [0,1]$ — the bottom-inclusion
- a **relative cell complex** — a map built by transfinitely attaching cells $S^{n-1} \hookrightarrow D^n$
- $\underline{\operatorname{Hom}}_R(M,N)$ — the $R$-module morphisms; $\operatorname{PHom}(M,N)$ — those factoring through a projective
- $\underline{\mathbf{Mod}}_R$ or $\operatorname{StMod}(R)$ — the **stable module category** of a Frobenius ring $R$
- $\Omega M$ — the syzygy (kernel of a projective cover); $\Sigma M = \Omega^{-1} M$ — the cosyzygy / suspension

---

# Motivation

The previous chapter was an exercise in faith: we wrote down five axioms and proved that any category satisfying them has a computable homotopy category. But faith is not understanding. The axioms are only worth imposing if real, important categories satisfy them — and not in a contrived way, but in a way that makes the abstract apparatus reproduce constructions you already know. This chapter pays the debt. We take the three categories Quillen and his successors had in mind and verify, in full, that they are model categories: **chain complexes of [[Def - Module|modules]]**, where the homotopy category turns out to be the derived category $D(R)$ and the abstract machine reproduces homological algebra; **topological spaces**, where the homotopy category is the classical homotopy category of CW complexes and the machine reproduces algebraic topology; and **stable module categories**, where the homotopy category is a genuinely new object that nonetheless fits the same template.

The reason these three are worth doing *in detail* rather than citing is that each illustrates a different way the axioms get satisfied, and together they teach you how to recognise a model structure in the wild. In $\mathbf{Ch}(R)$ the weak equivalences are quasi-[[Def - Isomorphism|isomorphisms]] and the construction is purely algebraic; the cofibrant objects are the complexes of projectives, and "cofibrant replacement" is *exactly* projective resolution. This is the cleanest place to watch the slogan "everything derived is an ordinary functor with a replacement bolted on the front" come true, because the derived tensor product computes **Tor** and derived Hom computes **Ext** — the founding constructions of homological algebra. In $\mathbf{Top}$ the weak equivalences are the [[Def - Higher Homotopy Group|weak homotopy equivalences]], the construction is geometric, and the hard axiom is factorisation, which is supplied by attaching cells. In a stable module category the weak equivalences are isomorphisms but the morphisms themselves are quotiented — you throw away every map that factors through a projective — and the resulting category is already its own homotopy category. The three examples sit at increasing distance from the topological intuition that motivated the subject, and seeing the axioms hold in all three is what convinces you the abstraction was the right one.

There is a unifying picture worth stating up front. In each case the same dictionary applies:

$$\text{weak equivalences} = \text{maps to invert}, \qquad \text{cofibrant objects} = \text{the resolutions}, \qquad \mathrm{Ho} = \text{the localized category you already half-knew}.$$

For chain complexes the resolutions are projective resolutions and $\mathrm{Ho}$ is $D(R)$; for spaces the resolutions are CW approximations and $\mathrm{Ho}$ is the homotopy category of CW complexes; for Frobenius modules the resolutions are trivial (every object is bifibrant) and $\mathrm{Ho}$ is the stable category. Whenever you meet a new homotopy theory, this is the dictionary to fill in.

This chapter assumes you have the axioms and their consequences from [[Model Categories — Quillen's Axiomatization of Homotopy Theory|the previous chapter]] at your fingertips: the meaning of [[Def - Model Category|model category]], the [[Thm - The Retract Argument|retract argument]], [[Def - Cofibrant and Fibrant Objects|(co)fibrant replacement]], the [[Thm - The Homotopy Category of a Model Category|fundamental theorem]], and [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunctions]]. From algebra you should recall what a [[Def - Module|module]] is, what a [[Def - Ring|ring]] is, what a [[Def - Projective Module|projective module]] is, and what a [[Def - Chain Map and Chain Homotopy|chain map and chain homotopy]] are. From topology you need [[Def - Topological Space|topological spaces]], [[Def - Homotopy|homotopy]], and [[Def - Higher Homotopy Group|homotopy groups]]. No prior acquaintance with derived categories, Serre [[Def - Fibration|fibrations]], or Frobenius [[Def - Ring|rings]] is assumed — those are built here.

---

# Concept Map

## §1 Chain Complexes and the Projective Model Structure

> [!note]- Recall: chain complexes and quasi-isomorphisms (self-contained background)
> A **chain complex** of left $R$-modules is a sequence of [[Def - Module|modules]] $\cdots \to C_{n+1} \xrightarrow{d_{n+1}} C_n \xrightarrow{d_n} C_{n-1} \to \cdots$ with $d_n \circ d_{n+1} = 0$ for all $n$ — "the boundary of a boundary is zero". The condition $d^2 = 0$ forces $\operatorname{im} d_{n+1} \subseteq \ker d_n$, and the **homology** $H_n(C) = \ker d_n / \operatorname{im} d_{n+1}$ measures the failure of exactness at degree $n$: it is the cycles modulo the boundaries. A **chain map** $f : C \to D$ is a degreewise family $f_n : C_n \to D_n$ commuting with the differentials, $d^D_n f_n = f_{n-1} d^C_n$; every chain map induces maps $H_n(f) : H_n(C) \to H_n(D)$. A **quasi-isomorphism** is a chain map that is an isomorphism on every $H_n$ — these are the maps the derived category is built to invert, and they are emphatically *not* isomorphisms of complexes. See [[Def - Chain Map and Chain Homotopy]] for the full treatment.

- **[[Def - Projective Model Structure on Chain Complexes]]**
	- The **projective model structure** on $\mathbf{Ch}(R)$ takes weak equivalences to be quasi-isomorphisms, fibrations to be the degreewise surjective chain maps, and cofibrations to be the monomorphisms with degreewise-[[Def - Projective Module|projective]] cokernel. Every object is fibrant (every chain map onto a point is surjective), and the cofibrant objects are exactly the bounded-below complexes of projectives — so cofibrant replacement is projective resolution. The generating cofibrations are the sphere-into-disk inclusions $S^{n-1} \hookrightarrow D^n$ and the generating trivial cofibrations are $0 \hookrightarrow D^n$.

- **[[Thm - Chain Complexes of Modules Form a Model Category]]**
	- The three classes above satisfy MC1–MC5, making $\mathbf{Ch}(R)$ a [[Def - Model Category|model category]]. Bicompleteness is degreewise; 2-out-of-3 and retracts are formal; the lifting and factorization axioms are proved with the disk and sphere complexes, factorization being the algebraic small-object argument that attaches $D^n$'s. The homotopy category is the **derived category** $D(R)$, and the abstract homotopy relation on cofibrant objects is exactly [[Def - Chain Map and Chain Homotopy|chain homotopy]].

> [!tip] Unlocked: The Derived Category and Triangulated Structure *(from Homological Algebra)*
> The homotopy category $\mathrm{Ho}(\mathbf{Ch}(R))$ *is* the **derived category** $D(R)$ — the universal place where quasi-isomorphisms become invertible. By the [[Thm - The Homotopy Category of a Model Category|fundamental theorem]], a morphism in $D(R)$ between bounded-below complexes is a chain-homotopy class of maps between projective resolutions; this is the model-categorical explanation of why $D(R)$ is *computable* at all. The derived functors $\mathbf{Tor}$ and $\mathbf{Ext}$ are the total derived functors of $\otimes_R$ and $\mathrm{Hom}_R$, and the cofiber sequences of the model structure equip $D(R)$ with the **distinguished triangles** of a **triangulated category**.

> [!tip] Unlocked: The Derived Category of Coherent Sheaves *(from Algebraic Geometry)*
> Replacing modules over a ring by sheaves of modules on a scheme, the very same projective (or injective) model structure on chain complexes of sheaves produces $D(\mathrm{Coh}\,X)$, the **derived category of coherent sheaves** — the home of modern intersection theory, Fourier–Mukai transforms, and the categorical formulation of mirror symmetry. The chain-complex story of this section is the affine, single-ring shadow of that geometric construction.

- **[[Ex - Identifying the cofibrant objects in chain complexes]]** (⭐⭐)
	- Show that a bounded-below complex is cofibrant in the projective model structure if and only if it is degreewise projective, and that cofibrant replacement of a module (as a complex in degree zero) is its projective resolution.
- **[[Ex - Sphere and disk complexes and the lifting axiom]]** (⭐⭐)
	- Compute $\mathbf{Ch}(R)(D^n, C)$ and $\mathbf{Ch}(R)(S^n, C)$ in terms of the chain [[Def - Group|groups]] and cycles of $C$, and use this to show a map has the RLP against $\{S^{n-1} \hookrightarrow D^n\}$ exactly when it is a degreewise-surjective quasi-isomorphism.
- **[[Ex - The projective model structure presents the derived category]]** (⭐⭐⭐)
	- Prove that $\mathrm{Ho}(\mathbf{Ch}(R)) \simeq D(R)$, identifying the abstract homotopy relation with chain homotopy and fibrant–cofibrant replacement with projective resolution.
- **[[Ex - The derived tensor product computes Tor on chain complexes]]** (⭐⭐⭐)
	- Show that the total left derived functor of $-\otimes_R N$ computes $\mathrm{Tor}^R_*(M, N)$ by replacing $M$ with a complex of projectives, and check the answer against a direct projective resolution of $M = \mathbb{Z}/n$ over $R = \mathbb{Z}$.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 Chain Complexes and the Projective Model Structure]]

## §2 Topological Spaces

> [!note]- Recall: weak homotopy equivalences and CW complexes (self-contained background)
> A continuous map $f : X \to Y$ is a **weak homotopy equivalence** if it induces a bijection $\pi_0(X) \to \pi_0(Y)$ on path components and an isomorphism on all [[Def - Higher Homotopy Group|homotopy groups]] $\pi_n(X, x) \to \pi_n(Y, f(x))$ for every basepoint $x$ and every $n \geq 1$. This is strictly weaker than a [[Def - Homotopy Equivalence and Contractible Space|homotopy equivalence]] (a map with a continuous homotopy inverse): for "nice" spaces — CW complexes — Whitehead's theorem says the two notions coincide, but for pathological spaces (the Warsaw circle, say) a weak equivalence need not be a homotopy equivalence. A **CW complex** is a space built by starting from a discrete set of points and inductively gluing $n$-cells (copies of the disk $D^n$) along their boundary spheres $S^{n-1}$; these are exactly the spaces homotopy theory is "about". See [[Def - Higher Homotopy Group]] and [[Def - Homotopy]].

- **[[Def - The Quillen Model Structure on Topological Spaces]]**
	- The **Quillen (Serre) model structure** on $\mathbf{Top}$ takes weak equivalences to be the weak homotopy equivalences, fibrations to be the **Serre fibrations** (maps with the homotopy lifting property against all disks), and cofibrations to be the retracts of relative cell complexes. Every space is fibrant; the cofibrant spaces are the retracts of CW complexes, so cofibrant replacement is CW approximation. The generating cofibrations are $\{S^{n-1} \hookrightarrow D^n\}_{n \geq 0}$ and the generating trivial cofibrations are the bottom-inclusions $\{D^n \hookrightarrow D^n \times [0,1]\}$.

- **[[Thm - Topological Spaces Form a Model Category]]**
	- These three classes satisfy MC1–MC5, making $\mathbf{Top}$ a [[Def - Model Category|model category]]. Bicompleteness is standard point-set topology; the hard axioms are lifting (proved by adjunction from the homotopy lifting property) and factorization (Quillen's small-object argument attaching cells from $\{S^{n-1} \hookrightarrow D^n\}$). The homotopy category is the classical homotopy category of CW complexes and homotopy classes of maps, so this model structure *is* algebraic topology in axiomatic dress.

> [!tip] Unlocked: [[Thm - The Homotopy Hypothesis|The Homotopy Hypothesis]] and Spaces as ∞-Groupoids *(from Higher Category Theory)*
> Once $\mathbf{Top}$ is a model category, the Quillen equivalence $|{-}| \dashv \mathrm{Sing}$ with [[Def - Simplicial Set|simplicial sets]] (developed in the simplicial-sets chapter) says that combinatorial and geometric models of homotopy types agree. This is the entry point to the **homotopy hypothesis**: spaces *are* **∞-groupoids**, and the [[Def - Kan Complex and the Nerve|Kan complexes]] are their combinatorial avatars. The Serre fibrations of this section become the **Kan fibrations** on the other side of the equivalence.

> [!tip] Unlocked: The Mixed Model Structure *(from Homotopical Algebra)*
> There is a second model structure on $\mathbf{Top}$, the **mixed (Cole) model structure**, whose weak equivalences are still the weak homotopy equivalences but whose fibrations are the **Hurewicz fibrations** (homotopy lifting against *all* spaces, not just disks). Its cofibrant objects are the spaces with the homotopy type of a CW complex — a slightly larger class than the Quillen-cofibrant ones — and it interpolates between the Quillen structure and the Strøm (Hurewicz) structure. It illustrates the key lesson of the chapter: the *weak equivalences* fix the homotopy theory, while the cofibrations and fibrations are a tunable presentation.

- **[[Ex - Every space is fibrant in the Quillen model structure]]** (⭐)
	- Show directly from the definition of a Serre fibration that the map $X \to *$ from any space to the one-point space is a Serre fibration, so every object of $\mathbf{Top}$ is fibrant.
- **[[Ex - Serre fibrations via the homotopy lifting property]]** (⭐⭐)
	- Prove that a map has the right lifting property against the bottom-inclusions $D^n \hookrightarrow D^n \times [0,1]$ if and only if it has the homotopy lifting property against all disks, i.e. it is a Serre fibration, via the adjunction with the cylinder.
- **[[Ex - The inclusion of a sphere into a disk is a cofibration]]** (⭐⭐)
	- Show that $S^{n-1} \hookrightarrow D^n$ is a Quillen cofibration but not a weak equivalence, while the bottom-inclusion $D^n \hookrightarrow D^n \times [0,1]$ is a trivial cofibration, and explain what each generates.
- **[[Ex - Weak homotopy equivalence need not be a homotopy equivalence]]** (⭐⭐⭐)
	- Exhibit a weak homotopy equivalence that is not a homotopy equivalence (the inclusion of a point into the Warsaw circle, or the map from a CW approximation to a non-CW space), and locate exactly where Whitehead's theorem's CW hypothesis is used.

> [!note] Exercise Index — §2
> [[Exercise Index - §2 Model Structures on Topological Spaces]]

## §3 Stable Module Categories and Comodules

> [!note]- Recall: projective, injective, and self-injective rings (self-contained background)
> A [[Def - Module|module]] $P$ is **projective** if every surjection onto $P$ splits — equivalently, $P$ is a direct summand of a free module, equivalently $\mathrm{Hom}(P, -)$ is exact. Dually, $I$ is **injective** if every injection out of $I$ splits, equivalently $\mathrm{Hom}(-, I)$ is exact. In general these are different classes. A ring is **self-injective** (or quasi-Frobenius, when also Noetherian) if $R$ is injective as a module over itself, which forces **projective = injective** for all finitely generated modules. The standard example is a group algebra $k[G]$ for a *finite* group $G$ over a field $k$ — this is the setting of modular representation theory. See [[Def - Projective Module]] and [[Def - Ring]].

- **[[Def - Stable Module Category over a Frobenius Ring]]**
	- Over a **Frobenius ring** $R$ (projective and injective modules coincide), the **stable module category** $\underline{\mathbf{Mod}}_R$ has the same objects as $\mathbf{Mod}_R$ but morphisms $\underline{\operatorname{Hom}}(M,N) = \operatorname{Hom}(M,N)/\operatorname{PHom}(M,N)$, killing every map that factors through a projective. It is the homotopy category of a model structure on $\mathbf{Mod}_R$ in which weak equivalences are the **stable equivalences**, cofibrations are the monomorphisms, and fibrations are the epimorphisms — so every object is both cofibrant and fibrant. The suspension $\Sigma$ is the cosyzygy functor, an autoequivalence making $\underline{\mathbf{Mod}}_R$ triangulated.

> [!tip] Unlocked: Tate Cohomology and Modular Representation Theory *(from Homological Algebra)*
> For $R = k[G]$ with $G$ finite, the stable module category is where **Tate cohomology** $\hat{H}^*(G; M)$ lives: it splices ordinary group cohomology with homology across degree zero, and $\hat{H}^n(G; M) = \underline{\operatorname{Hom}}(\Omega^n k, M)$ is computed entirely by stable maps. The stable category is the natural home of modular representation theory's "infinite tail" — everything visible after discarding the projective (= injective) summands.

> [!tip] Unlocked: Comodules over a Hopf Algebra and Stable [[Def - Homotopy|Homotopy]] *(from Stable Homotopy Theory)*
> The dual construction — **comodules** over a Hopf algebra — carries an analogous model structure, and the case of the dual Steenrod algebra produces the algebraic model governing the $E_2$-page of the **Adams spectral sequence**. This is one rung down from the model category of **spectra**, whose homotopy category is the **stable homotopy category**; the stable module category is the cleanest finite-dimensional rehearsal of that machinery.

- **[[Ex - Stable equivalence and maps through projectives]]** (⭐⭐)
	- Show that $\operatorname{PHom}(M,N)$, the maps factoring through a projective, is a [[Def - Subgroup|subgroup]] of $\operatorname{Hom}(M,N)$ closed under composition on both sides, so the quotient stable category is well-defined.
- **[[Ex - Projective objects become zero in the stable category]]** (⭐⭐)
	- Prove that a module $P$ is isomorphic to $0$ in $\underline{\mathbf{Mod}}_R$ if and only if $P$ is projective, and conclude that the stable category collapses exactly the "trivial" part of representation theory.
- **[[Ex - The syzygy is the loop functor on the stable category]]** (⭐⭐⭐)
	- For a Frobenius ring, show that the syzygy $\Omega M$ (kernel of a projective cover) is well-defined up to stable isomorphism and provides a loop functor inverse to the suspension, making $\underline{\mathbf{Mod}}_R$ a triangulated category.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 Stable Module Categories and Comodules]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The work of this chapter is concentrated on a small number of recurring goals, all of them instances of the general targets from [[Model Categories — Quillen's Axiomatization of Homotopy Theory|the foundations chapter]] but made concrete. The first and most laborious is **verifying the five axioms on a specific category** — given a candidate triple $(\mathcal{W}, \mathrm{cof}, \mathrm{fib})$ on $\mathbf{Ch}(R)$ or $\mathbf{Top}$, check MC1–MC5, where the cheap axioms (bicompleteness, 2-out-of-3, retracts) fall immediately and all the real work is in lifting (MC4) and factorization (MC5). The second is **identifying the cofibrant and fibrant objects**: in each example one class is trivial (every space is fibrant; every Frobenius module is both) and the other is the "resolutions" of the subject (complexes of projectives, retracts of CW complexes). The third is **naming the homotopy category** — proving $\mathrm{Ho}(\mathbf{Ch}(R)) \simeq D(R)$, or that $\mathrm{Ho}(\mathbf{Top})$ is the homotopy category of CW complexes, or that the stable category is its own homotopy category. The fourth is **computing a derived functor concretely** — showing the derived tensor product computes Tor, or that a homotopy colimit is a mapping cylinder. A fifth, structural, is **identifying the generating (trivial) cofibrations**, the finite list of maps from which the small object argument builds every factorization; pinning these down ($S^{n-1} \hookrightarrow D^n$ for both spaces and chain complexes) is what makes the verification feasible at all.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped, and recognising them is the whole craft. **A degreewise or pointwise statement** is the richest source in $\mathbf{Ch}(R)$: surjectivity of a chain map, projectivity of a cokernel, exactness — all are checked one degree at a time, reducing a complex problem to module theory. **A lifting property against the generators** is the source that powers every recognition: a map is a fibration if and only if it lifts against the generating trivial cofibrations, and you never check against the whole class, only the generators. **Projectivity of an object**, in both the chain-complex and Frobenius settings, is the hypothesis that makes maps split, lifts exist, and the cofibrant replacement be a resolution; whenever a problem hands you a projective, expect to use that $\mathrm{Hom}(P, -)$ is exact. **The homotopy lifting property** is the topological source: a Serre fibration is precisely a map you can lift homotopies along, and this is what one checks to recognise fibrations of spaces. Finally **an adjunction** — the cylinder–path adjunction $-\times[0,1] \dashv (-)^{[0,1]}$ in $\mathbf{Top}$, or the tensor–hom adjunction in $\mathbf{Ch}(R)$ — converts a lifting problem into an extension problem and is the standard device for proving MC4. The recurring move is to route a source to a target: a degreewise statement routes a chain-complex axiom to module theory; a lifting-against-generators statement routes through the small object argument to a full factorization; projectivity routes to the identification of cofibrant objects with resolutions.

---

# Legal Operations

These are the concrete moves that nearly every verification in this chapter uses. Everything is self-contained, building on the abstract operations of [[Model Categories — Quillen's Axiomatization of Homotopy Theory|the foundations chapter]] but specialised to the three examples.

**Legal operations:**

1. **Check a chain-complex condition one degree at a time.** Surjectivity of a chain map, injectivity, exactness, and projectivity of a cokernel are all *degreewise* notions: a chain map $f$ is a fibration in $\mathbf{Ch}(R)$ precisely when each $f_n : C_n \to D_n$ is a surjection of [[Def - Module|modules]]. *Trigger:* you must verify an axiom about a chain map. *Pattern:* "in degree $n$, the map is $f_n$, which is surjective because…" — reduce the homotopy-theoretic claim to module theory.

2. **Probe a complex with the sphere and disk complexes.** A chain map out of $S^n$ picks out an $n$-cycle; a chain map out of $D^n$ picks out an arbitrary element of $C_n$ (with its boundary in degree $n-1$). Formally $\mathbf{Ch}(R)(S^n, C) = Z_n(C)$ (the $n$-cycles) and $\mathbf{Ch}(R)(D^n, C) = C_n$. *Trigger:* you need to translate a lifting problem against $\{S^{n-1} \hookrightarrow D^n\}$ into an algebraic statement. *Pattern:* "lifting against $S^{n-1} \hookrightarrow D^n$ means filling a cycle to a chain, i.e. surjectivity onto cycles plus a homology condition."

3. **Replace a module by its projective resolution.** A single [[Def - Module|module]] $M$, viewed as a complex concentrated in degree zero, has cofibrant replacement its [[Def - Projective Module|projective]] resolution $P_\bullet \xrightarrow{\sim} M$. *Trigger:* a construction requires a cofibrant input — the derived tensor product, derived Hom, any derived functor. *Pattern:* "resolve $M$ by projectives, apply the functor degreewise, take homology" — this is the recipe for Tor and Ext.

4. **Recognise a fibration of spaces by the homotopy lifting property.** A continuous map $p : E \to B$ is a Serre fibration exactly when, given a homotopy $H : X \times [0,1] \to B$ (for $X$ a disk) and a lift of its bottom $X \times \{0\}$, the whole homotopy lifts. *Trigger:* you must verify a map of spaces is a fibration. *Pattern:* fibre bundles, covering maps, and path-space projections are all Serre fibrations by exhibiting the lifted homotopy; see [[Def - The Quillen Model Structure on Topological Spaces]].

5. **Attach a cell, or transfinitely attach cells.** Factorization in both $\mathbf{Top}$ and $\mathbf{Ch}(R)$ is performed by Quillen's small object argument: glue on copies of $D^n$ (or the disk complex) along their boundaries to fix up a map until it lifts against everything it needs to. *Trigger:* you need to factor a map as (trivial) cofibration followed by (trivial) fibration. *Pattern:* "build the relative cell complex by attaching all cells whose boundary maps into the source" — the **small object argument** does this transfinitely.

6. **Use the cylinder–path adjunction to convert lifting into extension.** In $\mathbf{Top}$, lifting a homotopy $X \times [0,1] \to B$ is adjoint to extending a map $X \to B^{[0,1]}$ into the path space; this is how the homotopy lifting property is checked against the bottom-inclusion. *Trigger:* a lifting problem against a cylinder inclusion. *Pattern:* "by the exponential adjunction, this lift is a map into the path space, which exists because…".

7. **Quotient out maps through projectives.** In the stable setting, two parallel maps are identified if their difference factors through a [[Def - Projective Module|projective]]; this is the passage from $\mathbf{Mod}_R$ to $\underline{\mathbf{Mod}}_R$. *Trigger:* you want to work in the stable category, or to show a map is stably zero. *Pattern:* "this map factors as $M \to P \to N$ with $P$ projective, hence it is zero stably"; see [[Def - Stable Module Category over a Frobenius Ring]].

8. **Take the syzygy or cosyzygy to suspend or loop.** Over a Frobenius ring, $\Omega M$ (the kernel of a projective cover $P \twoheadrightarrow M$) and $\Sigma M = \Omega^{-1} M$ (the cokernel of an injective hull, which exists because injective = projective) are inverse autoequivalences of the stable category. *Trigger:* you need the loop or suspension functor, or a distinguished triangle. *Pattern:* "the cosyzygy $\Sigma M$ shifts the triangle; the short exact sequence $0 \to M \to P \to \Sigma M \to 0$ is the cofiber sequence."

9. **Dualize between projective and injective.** The projective model structure on $\mathbf{Ch}(R)$ has an injective sibling (cofibrations = degreewise monos, fibrations = degreewise epis with injective kernel), and the two present the same derived category. *Trigger:* projective resolutions are awkward but injective ones are easy, or vice versa. *Pattern:* "compute Ext by an injective resolution of the second argument instead of a projective resolution of the first."

**Illegal but tempting operations:**

> [!warning] 1. Treating a quasi-isomorphism as an isomorphism of complexes
> A quasi-isomorphism $f : C \xrightarrow{\sim} D$ induces an isomorphism on homology, and it is tempting to conclude $C$ and $D$ are isomorphic complexes, or that $f$ has a chain-map inverse. Both are false: the projective resolution $\cdots \to 0 \to \mathbb{Z} \xrightarrow{n} \mathbb{Z} \to 0$ of $\mathbb{Z}/n$ over $\mathbb{Z}$ is quasi-isomorphic to $\mathbb{Z}/n$ concentrated in degree zero, but the two complexes are not isomorphic and there is no chain map back. The operation becomes legal only after passing to the **derived category** $D(R)$ — there the quasi-isomorphism *is* invertible, but its inverse is a zig-zag, not a chain map, unless both complexes are cofibrant.

> [!warning] 2. Assuming a weak homotopy equivalence has a continuous inverse
> A weak homotopy equivalence of spaces induces isomorphisms on all [[Def - Higher Homotopy Group|homotopy groups]], so it is tempting to invert it up to homotopy. This fails for non-CW spaces: there is a weak equivalence from a CW approximation onto the Warsaw circle, but no homotopy inverse exists because the Warsaw circle has the wrong local structure. The repair is [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]] — Whitehead's theorem guarantees a homotopy inverse only **between CW (cofibrant) complexes**, which is exactly why the homotopy category is built from cofibrant objects.

> [!warning] 3. Expecting the strict tensor product to be homotopy-invariant
> Computing $M \otimes_R N$ directly and treating the answer as well-defined up to quasi-isomorphism is wrong, because $\otimes_R$ is not exact: tensoring the quasi-isomorphism $(\mathbb{Z} \xrightarrow{n} \mathbb{Z}) \xrightarrow{\sim} \mathbb{Z}/n$ with $\mathbb{Z}/n$ does not give a quasi-isomorphism — it loses the $\mathrm{Tor}_1$ information. The operation is legal only after **replacing one factor by a complex of projectives**, which is what the derived tensor product $\otimes^{\mathbf{L}}_R$ does; the discrepancy between $\otimes$ and $\otimes^{\mathbf{L}}$ is precisely $\mathbf{Tor}$.

> [!warning] 4. Believing every model structure on a category is unique
> Having built the Quillen model structure on $\mathbf{Top}$, it is tempting to speak of "the" model structure. But $\mathbf{Top}$ also carries the Strøm (Hurewicz) model structure, whose weak equivalences are genuine homotopy equivalences, and the mixed model structure interpolating between them. These present *different* homotopy categories (the Strøm structure inverts fewer maps). A model structure is data, not a property; naming the weak equivalences is what pins down which homotopy theory you mean, and only then is the structure determined up to the choice of cofibrations and fibrations.

---

# Problem-Solving Strategy

Every problem in this chapter is one of the targets above, and the route is determined the moment you classify it. The overarching tactic is **transport the question to the concrete category and check the axiom there**, rather than reasoning abstractly. Abstract model-category theory tells you *what* to check; the content of this chapter is *how* to check it in $\mathbf{Ch}(R)$, $\mathbf{Top}$, and $\underline{\mathbf{Mod}}_R$.

If the problem **asks you to verify an axiom on chain complexes**, reduce everything to a degreewise statement about [[Def - Module|modules]]. Bicompleteness is degreewise (limits and colimits of complexes are computed degree by degree); 2-out-of-3 follows because homology is functorial; retracts are formal. The two hard axioms reduce to algebra: lifting against $\{S^{n-1} \hookrightarrow D^n\}$ becomes a statement about cycles and surjectivity (use legal operation 2), and factorization is the algebraic small object argument attaching disk complexes (operation 5). The single most useful realisation is that the cofibrant objects are the complexes of projectives, so cofibrant replacement is projective resolution — once you see this, every "compute a derived functor" problem becomes "resolve and apply the functor".

If the problem **asks you to verify an axiom on spaces**, the cheap axioms are point-set topology and the hard ones are lifting and factorization. Lifting is proved by the homotopy lifting property reformulated through the cylinder–path adjunction (operation 6); factorization is Quillen's small object argument attaching cells $\{S^{n-1} \hookrightarrow D^n\}$ (operation 5). The recognition skill is identifying Serre fibrations — fibre bundles, covering maps, and path fibrations are the stock examples — and identifying cofibrant objects as retracts of CW complexes. Whenever a space appears that is not obviously CW, the move is CW approximation, the topological cofibrant replacement.

If the problem **asks about the stable module category**, the governing fact is that *every object is bifibrant*, so the category is already its own homotopy category and there is no replacement step. The work shifts to understanding the quotient $\operatorname{Hom}/\operatorname{PHom}$: a map is stably zero exactly when it factors through a [[Def - Projective Module|projective]] (operation 7), the suspension is the cosyzygy (operation 8), and the triangulated structure comes from short exact sequences. The key decision is recognising when a module is projective — over a Frobenius ring, projective equals injective, which is the hypothesis that makes the syzygy functor invertible.

If the problem **asks you to identify a homotopy category**, route through the [[Thm - The Homotopy Category of a Model Category|fundamental theorem]]: determine the bifibrant objects and what homotopy of maps between them means. For chain complexes this gives chain homotopy and hence $D(R)$; for spaces it gives homotopy classes of maps of CW complexes; for Frobenius modules it gives the stable category directly. The skill, in every case, is recognising the "resolutions" of the subject as the cofibrant objects.

The meta-strategy that threads through all of this: **in each concrete example, find the dictionary entry "what is a cofibrant object here?" first, because it tells you everything else.** Cofibrant objects are projective complexes (chain complexes), retracts of CW complexes (spaces), or every object (Frobenius modules); knowing them tells you what cofibrant replacement does, hence how derived functors are computed, hence what the homotopy category is. Every question in this chapter is, at bottom, the question "what are the good objects on which I can compute, and how do I replace a bad object by a good one?"

---

# Most Reusable Properties

- **[[Def - Projective Model Structure on Chain Complexes|The Projective Model Structure]]**: cofibrant = complex of projectives, fibrant = everything, weak equivalence = quasi-isomorphism. This is the most reusable single structure in the chapter because it makes the entire apparatus of homological algebra into a special case of homotopy theory. **Typical use:** any time you must compute a derived functor (Tor, Ext, derived (co)limit), the recipe is "replace by a complex of projectives and apply the functor"; the projective model structure is the justification that this is well-defined and homotopy-invariant. It is also the template you copy when building model structures on chain complexes of sheaves or of comodules.

- **[[Thm - Chain Complexes of Modules Form a Model Category|The Identification of Ho with D(R)]]**: the derived category is a homotopy category, and its morphisms are chain-homotopy classes of maps between resolutions. **Typical use:** whenever you need to *compute* in $D(R)$ — to evaluate a Hom in the derived category, or to know when two complexes are isomorphic there — replace both by complexes of projectives and take chain-homotopy classes. This is what turns the inscrutable zig-zag definition of $D(R)$ into something you can calculate with, and it is the model-categorical source of the triangulated structure.

- **[[Def - The Quillen Model Structure on Topological Spaces|The Quillen Model Structure on Top]]**: cofibrant = retract of CW, fibrant = everything, weak equivalence = weak homotopy equivalence, generators $\{S^{n-1} \hookrightarrow D^n\}$. **Typical use:** this is the bridge that makes "model category" the right abstraction — classical algebraic topology is literally this one example. Reach for it to recognise Serre fibrations, to justify CW approximation as cofibrant replacement, and to compute homotopy (co)limits of spaces (the homotopy pushout of $* \leftarrow X \to *$ is the suspension $\Sigma X$).

- **The generating cofibrations $\{S^{n-1} \hookrightarrow D^n\}$**: a finite list of maps that generates the entire cofibration class via the small object argument, shared by $\mathbf{Top}$ and $\mathbf{Ch}(R)$. **Typical use:** to check a map is a fibration you test the RLP against the generators only, never the whole class; to build a factorization you attach cells from this set. The fact that the same generators appear in spaces and in chain complexes is the deepest structural parallel in the chapter, and it is the reason both categories are **cofibrantly generated** — see the forthcoming **[[Def - Cofibrantly Generated Model Category|Cofibrantly Generated Model Categories]]** chapter and its **small object argument**.

- **[[Def - Stable Module Category over a Frobenius Ring|Projective = Injective on a Frobenius Ring]]**: the defining property of a Frobenius ring, which makes the syzygy functor an autoequivalence. **Typical use:** it is what lets you suspend and loop in $\underline{\mathbf{Mod}}_R$ and equips the stable category with a triangulated structure with no further input. Recognising a ring as Frobenius — a finite group algebra, a finite-dimensional Hopf algebra, a complete intersection's local ring — immediately gives you a triangulated stable category to work in.

---

# Bridges

1. **Homological algebra — the derived category is a homotopy category.** On $\mathbf{Ch}(R)$ with quasi-isomorphisms as weak equivalences, the [[Thm - The Homotopy Category of a Model Category|fundamental theorem]] identifies $\mathrm{Ho}(\mathbf{Ch}(R))$ with the derived category $D(R)$. Concretely: the cofibrant objects are the bounded-below complexes of [[Def - Projective Module|projectives]], the abstract homotopy relation is [[Def - Chain Map and Chain Homotopy|chain homotopy]], and cofibrant replacement of a [[Def - Module|module]] $M$ (as a complex in degree zero) is its projective resolution $P_\bullet \to M$. The derived functors **Tor** and **Ext** are then the total left and right derived functors of $\otimes_R$ and $\mathrm{Hom}_R$ — for instance $\mathrm{Tor}^R_n(M,N) = H_n(P_\bullet \otimes_R N)$ — so the entire edifice of homological algebra is homotopy theory carried out in chain complexes. This is the cleanest demonstration that "derived" everywhere means "ordinary functor after resolution".

2. **Algebraic topology — the homotopy category of spaces.** The Quillen model structure on $\mathbf{Top}$ recovers classical homotopy theory exactly. The weak equivalences are the [[Def - Higher Homotopy Group|weak homotopy equivalences]], the cofibrant objects are the retracts of CW complexes, every space is fibrant, and the abstract cylinder object $\mathrm{Cyl}(A)$ is the honest topological cylinder $A \times [0,1]$, so the abstract [[Def - Homotopy|homotopy]] relation is the classical one. By the fundamental theorem, $\mathrm{Ho}(\mathbf{Top})$ is the category of CW complexes and homotopy classes of maps. The homotopy pushout of $* \leftarrow X \to *$ — the derived version of collapsing $X$ two ways — is the suspension $\Sigma X$, computed by the double mapping cylinder; this is where the suspension of topology meets the homotopy colimits of the foundations chapter.

3. **Stable homotopy theory — the stable module category as a finite model of spectra.** Over a Frobenius ring, the suspension $\Sigma$ in $\underline{\mathbf{Mod}}_R$ is an *autoequivalence* (the cosyzygy), so the category is already **stable** — looping and suspension are inverse — without inverting any maps. This is the algebraic shadow of the stable homotopy category of **spectra**, where one formally inverts the topological suspension to make it invertible; the difference is that the Frobenius condition makes invertibility automatic in finite dimensions. The triangulated structure of $\underline{\mathbf{Mod}}_R$ — distinguished triangles coming from short exact sequences $0 \to M \to P \to \Sigma M \to 0$ — is the same structure that the stable homotopy category carries, and it is why both belong to the world of **triangulated categories**.

4. **Algebraic geometry — derived categories of sheaves.** Replacing the ring $R$ by the structure sheaf of a scheme $X$ and modules by sheaves of $\mathcal{O}_X$-modules, the projective (more usefully, the injective) model structure on chain complexes of sheaves produces the **derived category of coherent sheaves** $D(\mathrm{Coh}\,X)$. This is the home of Serre duality, Fourier–Mukai transforms, and the categorical statement of homological mirror symmetry, where the derived category of one space is equivalent to a Fukaya category of its mirror. The single-ring story of §1 is the affine local model: $\mathrm{Spec}\,R$ is one affine chart, and the global derived category is assembled from these charts. The model-categorical viewpoint is what makes the assembly — and the resulting **triangulated** structure — rigorous.

---

# Insights

**The unifying frame: every homotopy theory in this chapter is governed by the question "what are the cofibrant objects?"** The three examples look unrelated — algebra, topology, representation theory — but they are organised by a single dictionary. The weak equivalences say what to invert (quasi-isomorphisms, weak homotopy equivalences, stable equivalences); the cofibrant objects are the "resolutions" on which everything is computed (complexes of projectives, retracts of CW complexes, every Frobenius module); and the homotopy category is the localized category you half-knew already ($D(R)$, the homotopy category of CW complexes, the stable category). Once you know the cofibrant objects, cofibrant replacement is determined (projective resolution, CW approximation, the identity), and from cofibrant replacement everything else follows — derived functors, the homotopy category, the (co)fiber sequences. When you meet a new category and want to do homotopy theory in it, the first and most important question is not "what are the fibrations?" but "what are the good objects I am allowed to compute with, and how do I replace a bad object by a good one?"

**The true name of "cofibrant replacement" is "resolution".** In every classical setting the word "resolution" already meant "replace a hard object by an equivalent complex of nice ones", and the model-categorical word for the same act is cofibrant replacement. A projective resolution of a module *is* its cofibrant replacement in $\mathbf{Ch}(R)$; a CW approximation of a space *is* its cofibrant replacement in $\mathbf{Top}$; an injective resolution is a fibrant replacement in the injective model structure. The reason resolutions are ubiquitous in mathematics is that they are the universal device for making a functor homotopy-invariant, and the reason they always come with a quasi-isomorphism back to the original is that the replacement must not change the homotopy type. Whenever you see the word "resolution" — projective, injective, flat, free, simplicial, CW — read "cofibrant or fibrant replacement", and the model-categorical machinery applies.

**The same generators $\{S^{n-1} \hookrightarrow D^n\}$ run both topology and algebra, and this is not a coincidence.** In $\mathbf{Top}$ the generating cofibrations are the inclusions of boundary spheres into disks; in $\mathbf{Ch}(R)$ they are the inclusions of the sphere complex $S^{n-1}$ into the disk complex $D^n$. The notation is deliberately identical because the role is identical: in both cases attaching a "disk" along its "sphere" is the elementary move from which the small object argument builds every factorization, and "fibration" means "lifts homotopies across cells" in both. This is the structural reason chain complexes and spaces feel like the same subject in two costumes — they are both **cofibrantly generated** by analogous cellular data, and the analogy between cells in topology and disk complexes in algebra is exact, not loose. The forthcoming **Cofibrantly Generated Model Categories** chapter makes this the basis of a general recognition theorem.

**A model structure is data you choose, not a property a category has.** The clearest lesson of $\mathbf{Top}$ carrying three different model structures (Quillen, Strøm, mixed) is that "is $\mathbf{Top}$ a model category?" is the wrong question — the right one is "which homotopy theory do you want?". The weak equivalences encode that choice and determine the homotopy category up to equivalence; the cofibrations and fibrations are a presentation, tunable to make whichever computations you face convenient. The projective and injective model structures on $\mathbf{Ch}(R)$ present the *same* derived category through different cofibrant objects, chosen depending on whether projective or injective resolutions are easier for the functor at hand. Internalising this dissolves the apparent rigidity of the axioms: you are not discovering the model structure, you are designing it, subject only to the constraint that the weak equivalences are fixed in advance.
