---
type: topic
subject: model-categories
chapter: "7-8"
title: "Model Categories — Stable Model Categories and Triangulated Categories"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation Registry

Throughout this chapter $\mathcal{M}$ denotes a **pointed** model category — one whose initial object $\varnothing$ and terminal object $*$ coincide, giving a **zero object** $0$. The homotopy category is $\mathrm{Ho}(\mathcal{M})$, the localization of $\mathcal{M}$ at its weak equivalences. The chapter is built around one functor on $\mathrm{Ho}(\mathcal{M})$: the **suspension** $\Sigma$, the homotopy cofiber of $X \to 0$, with right adjoint the **loop** $\Omega$. The single hypothesis that organizes everything is that $\Sigma$ be an *equivalence* of categories; a pointed model category with this property is called **stable**. On the abstract side, $\mathcal{T}$ denotes a **triangulated category**, $\Sigma$ (also written $[1]$) its shift, and a **distinguished triangle** is a diagram $X \to Y \to Z \to \Sigma X$.

- $\mathcal{M}, \mathcal{N}$ — pointed model categories; $\mathcal{T}, \mathcal{S}$ — triangulated categories; $\mathcal{C}, \mathcal{D}$ — ordinary categories
- $0$ — the **zero object** (initial $=$ terminal); $0 \colon X \to Y$ — the zero morphism, the composite $X \to 0 \to Y$
- $\mathrm{Ho}(\mathcal{M})$ — the homotopy category; $[X, Y]$ — the abelian group $\mathrm{Ho}(\mathcal{M})(X, Y)$ of homotopy classes (in the stable case)
- $\Sigma$ — **suspension** (also the **shift**, written $[1]$); $\Omega$ — **loop**; $\Sigma \dashv \Omega$ on $\mathrm{Ho}(\mathcal{M})$
- $X[n] = \Sigma^n X$ — the $n$-fold shift, defined for all $n \in \mathbb{Z}$ when $\Sigma$ is invertible
- $X \xrightarrow{f} Y \to Cf \to \Sigma X$ — the **cofiber sequence** of $f$; $Cf$ is the homotopy cofiber
- $X \to Y \to Z \to \Sigma X$ — a **distinguished triangle**; the fourth map is the **connecting** or **boundary** map
- TR1–TR4 — the axioms of a triangulated category; TR4 is the **octahedral axiom**
- $\mathbf{Ch}(R)$ — chain complexes of $R$-modules; $D(R)$ — the **derived category** of a ring $R$
- $R, S$ — rings (associative, unital); $\mathbf{Mod}_R$ — right $R$-modules; $\mathrm{End}(P)$ — the endomorphism ring of $P$
- $\mathcal{SH}$ — the **stable homotopy category** (the homotopy category of spectra)
- $G$ — a **weak generator**; $G$ **compact** if $[G, -]$ commutes with coproducts
- $\mathrm{Hom}_{\mathcal{T}}(X, Y)$ or $\mathcal{T}(X, Y)$ — morphisms in $\mathcal{T}$; an **additive** category has these be abelian groups with bilinear composition

---

# Motivation

Here is the whole chapter in one sentence: **a stable model category is one where suspension is reversible, and the price of reversibility is that the homotopy category acquires a rigid algebraic skeleton called a triangulated structure.** Everything below unpacks that sentence.

Start with the unstable picture from the previous chapter. In a pointed model category — one with a [[Def - Cofibrant and Fibrant Objects|zero object]] $0$ that is both initial and terminal — every map $f \colon X \to Y$ has a **cofiber**, the homotopy pushout of $0 \leftarrow X \xrightarrow{f} Y$, which you should picture as "$Y$ with $X$ crushed to a point." Crushing $X$ inside the cone on $X$ produces the **suspension** $\Sigma X$, the homotopy pushout of $0 \leftarrow X \to 0$. In spaces this is the honest suspension: $\Sigma S^n = S^{n+1}$. Dually there is a **loop** functor $\Omega$, and on the homotopy category $\Sigma$ is left adjoint to $\Omega$, exactly as the based loop space is right adjoint to reduced suspension. This much is the content of **pointed model categories and the Puppe cofiber sequence** (the previous chapter). It is genuinely directional: suspension only goes one way. You can suspend a space, but you cannot in general *desuspend* it — $S^1$ is a suspension of $S^0$, but most spaces are not suspensions of anything.

The decisive move of this chapter is to **demand that you can desuspend.** A pointed model category is **stable** when $\Sigma \colon \mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathcal{M})$ is an *equivalence of categories*. Equivalently, the adjunction $\Sigma \dashv \Omega$ becomes an adjoint *equivalence*: $\Omega$ undoes $\Sigma$. The instant this holds, three things happen at once, and they are the spine of the chapter:

$$\Sigma \text{ invertible} \;\Longrightarrow\; \mathrm{Ho}(\mathcal{M}) \text{ is additive} \;\Longrightarrow\; \text{cofiber sequences} = \text{fiber sequences} \;\Longrightarrow\; \mathrm{Ho}(\mathcal{M}) \text{ is triangulated.}$$

Why should reversibility force *addition*? Because once $\Sigma$ is invertible, every object is a double loop object ($X \cong \Omega^2 \Sigma^2 X$), and a double loop object carries a canonical, automatically *abelian* group structure on its homotopy classes of maps — the same Eckmann–Hilton reason that $\pi_n$ is abelian for $n \geq 2$. So $[X, Y] = \mathrm{Ho}(\mathcal{M})(X, Y)$ is not merely a set but an **abelian group**, and composition is bilinear: the homotopy category is **additive** (this is where [[Def - Abelian Group|abelian-group]] structure enters the categorical picture). And the cofiber sequence $X \to Y \to Cf \to \Sigma X$, which unstably is genuinely different from the fiber sequence $\Omega Z \to Ff \to X \to Y$, becomes *the same sequence* up to shift once $\Sigma$ and $\Omega$ are mutually inverse. The result is a category in which every map sits inside a canonical "triangle" $X \to Y \to Z \to \Sigma X$ that behaves like a short exact sequence but is self-perpetuating in both directions.

That structure — an additive category, an invertible shift $\Sigma$, and a class of distinguished triangles satisfying four axioms (TR1–TR4, the last being the **octahedral axiom**) — is what Verdier abstracted in the 1960s under the name **triangulated category**, originally to make sense of derived categories in algebraic geometry. The two great examples are the **derived category** $D(R)$ of a ring, where the triangles are the mapping cones of chain maps and the long exact sequence of homology *is* the triangle's induced long exact sequence, and the **stable homotopy category** $\mathcal{SH}$ of spectra, where suspension is invertible by construction. This chapter shows these are not coincidences: each is $\mathrm{Ho}(\mathcal{M})$ for a stable model category, and the triangulated structure is forced.

The chapter closes with two further questions, both pointing forward. First, *recognition*: when is $\mathrm{Ho}(\mathcal{M})$ as simple as possible — equivalent to modules over a ring? The answer (Schwede–Shipley) is that this happens exactly when $\mathrm{Ho}(\mathcal{M})$ is generated by a single **compact** object, and then $\mathcal{M}$ presents modules over its **endomorphism ring spectrum**. Second, *vistas* (Hovey's final chapter): what is the relationship between this whole apparatus and the modern theory of **stable ∞-categories**, which repairs the one genuine defect of triangulated categories — the fact that the cone is not functorial? We will see that triangulated categories are the shadow that a stable model category, or a stable ∞-category, casts on the level of homotopy categories.

This chapter assumes the previous model-category material: [[Def - Model Category|model categories]] and their [[Thm - The Homotopy Category of a Model Category|homotopy category]], [[Def - Cofibrant and Fibrant Objects|cofibrant and fibrant objects]], the [[Def - Cylinder Object, Path Object, and Homotopy|cylinder/path-object]] notion of homotopy, [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunctions and equivalences]], and especially the **pointed model category, suspension/loop functors, and the cofiber/fiber sequences** of the previous chapter (which has not yet been written up, so those are named in bold below rather than linked). From algebra you need only the idea of an [[Def - Abelian Group|abelian group]], a [[Def - Ring|ring]], a [[Def - Module|module]], and a [[Def - Chain Map and Chain Homotopy|chain complex with its chain homotopies]]. No prior exposure to triangulated categories or spectra is assumed.

---

# Concept Map

## §1 Triangulated Categories

- **[[Def - Triangulated Category]]**
	- A **triangulated category** is an [[Def - Abelian Group|additive]] category $\mathcal{T}$ (hom-sets are abelian groups, composition bilinear, finite products $=$ coproducts $=$ biproducts) equipped with an automorphism $\Sigma$ (the **shift** or **suspension**, written $[1]$) and a class of **distinguished triangles** $X \to Y \to Z \to \Sigma X$ satisfying four axioms: TR1 (identities are triangles; every map extends to one; triangles are closed under isomorphism), TR2 (a triangle may be **rotated**, with a sign), TR3 (any two maps of the first two terms of a triangle extend to a map of triangles), and TR4 (the **octahedral axiom**, governing the cofiber of a composite). The defining consequence is that applying $\mathrm{Hom}_{\mathcal{T}}(W, -)$ or $\mathrm{Hom}_{\mathcal{T}}(-, W)$ to a distinguished triangle yields a **long exact sequence** of abelian groups. The motivating instance is the [[Def - Chain Map and Chain Homotopy|derived category]] of a ring, whose triangles are mapping cones.

> [!tip] Unlocked: Derived Category of Coherent Sheaves *(from Algebraic Geometry)*
> Replacing modules over a ring by **coherent sheaves** on an algebraic variety $X$, and chain complexes by complexes of such sheaves, produces the **bounded derived category** $D^b(\mathrm{Coh}\,X)$ — a triangulated category that has become *the* invariant of a variety in modern algebraic geometry. Two varieties can be non-isomorphic yet have equivalent derived categories (**derived equivalence**, e.g. a variety and its dual under a **Fourier–Mukai transform**), and the **Bondal–Orlov reconstruction theorem** says that for a variety with ample (anti)canonical bundle, $D^b(\mathrm{Coh}\,X)$ remembers $X$ entirely. See the self-contained algebraic-geometry callout in [[Def - Triangulated Category#Examples / Corollaries]].

- **[[Thm - The Homotopy Category of a Stable Model Category is Triangulated]]**
	- If $\mathcal{M}$ is a stable model category, then $\mathrm{Ho}(\mathcal{M})$ is a triangulated category: the shift is the suspension $\Sigma$ (an equivalence by stability), and the distinguished triangles are the diagrams isomorphic to **cofiber sequences** $X \to Y \to Cf \to \Sigma X$. The additive structure comes from the double-loop-object Eckmann–Hilton argument; TR1–TR3 are repackagings of the formal properties of homotopy pushouts and the Puppe sequence; TR4 is the statement that the cofiber of a composite is built from the cofibers of the factors, which follows from the pasting law for homotopy pushouts. This is the bridge that produces *every* triangulated category arising in nature.

> [!tip] Unlocked: The Stable Homotopy Category and Generalized Cohomology *(from Algebraic Topology)*
> The homotopy category of **spectra**, $\mathcal{SH}$, is the universal stable model category built from spaces — formally, it inverts suspension on pointed spaces. Its triangulated structure is the home of all **generalized cohomology theories** (ordinary cohomology, $K$-theory, cobordism), each of which is represented by a spectrum via **Brown representability**, the statement that a cohomology-theory-like functor on $\mathcal{SH}$ is corepresentable. The shift $\Sigma$ here is the genuine invertible suspension, and $\pi_n^s(S^0) = [\Sigma^n \mathbb{S}, \mathbb{S}]$ are the stable homotopy groups of spheres.

- **[[Ex - The long exact sequence induced by a distinguished triangle]]** (⭐⭐)
	- From the axioms alone, show that $\mathrm{Hom}_{\mathcal{T}}(W, -)$ sends a distinguished triangle to a long exact sequence, the cornerstone computational fact.
- **[[Ex - Rotation of a triangle is forced by the axioms]]** (⭐⭐)
	- Show TR2 is not independent decoration: derive that the rotated triangle is distinguished and identify exactly where the sign $-\Sigma f$ is needed for consistency.
- **[[Ex - The octahedral axiom as the third isomorphism theorem]]** (⭐⭐⭐)
	- Interpret TR4 in $D(R)$ as a homotopy-coherent version of the statement that the cofiber of $g \circ f$ sits in a triangle with the cofibers of $f$ and $g$, recovering the third isomorphism theorem on homology.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 Triangulated Categories]]

## §2 Stable Model Categories

- **[[Def - Stable Model Category]]**
	- A **stable model category** is a pointed model category $\mathcal{M}$ in which the suspension functor $\Sigma \colon \mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathcal{M})$ is an equivalence of categories (equivalently, the adjunction $\Sigma \dashv \Omega$ is an adjoint equivalence; equivalently every object is "infinitely desuspendable"). Stability is a property, not extra structure: it is checked on the homotopy category. The point of the definition is that it is the minimal hypothesis on a pointed model category under which the cofiber and fiber sequences coincide and $\mathrm{Ho}(\mathcal{M})$ becomes triangulated. Examples: $\mathbf{Ch}(R)$ with quasi-isomorphisms (so $\mathrm{Ho} = D(R)$), spectra, and stable module categories over a self-injective ring.

> [!tip] Unlocked: Stable ∞-Category *(from Higher Category Theory)*
> The modern refinement of "stable model category" is the **stable ∞-category**: an ∞-category with a zero object in which suspension is invertible and finite limits agree with finite colimits. Its homotopy category is triangulated, but — crucially — the ∞-category remembers the *coherence data* (the actual cones and their higher homotopies) that a triangulated category throws away, which is why the cone becomes functorial there. Every stable model category presents a stable ∞-category; this is the cleanest statement of what the model-category apparatus of this chapter is *for*.

- **[[Thm - Characterization of Stable Model Categories]]**
	- A **pre-triangulated category** (the homotopy category of a pointed model category, equipped with its compatible cofiber and fiber sequences and the adjunction $\Sigma \dashv \Omega$) is **triangulated** if and only if $\Sigma$ is invertible — equivalently, if and only if the model category is stable. This is the precise sense in which "triangulated" $=$ "pre-triangulated $+$ desuspendable." The forward direction installs the triangulated axioms from the pre-triangulated structure once $\Sigma$ is an equivalence; the reverse shows triangulation forces $\Sigma$ to be an automorphism. It pins down stability as exactly the dividing line between the directional unstable world and the symmetric stable one.

> [!tip] Unlocked: t-Structure and the Heart *(from Homological Algebra)*
> A **t-structure** on a triangulated category $\mathcal{T}$ is a pair of full subcategories behaving like "complexes concentrated in non-negative / non-positive degrees"; its **heart** is an abelian category, and $\mathcal{T}$ is glued from the heart by the triangles. The standard t-structure on $D(R)$ has heart $\mathbf{Mod}_R$, recovering ordinary homological algebra inside the derived category; exotic t-structures (perverse sheaves) are the source of much of modern representation theory and geometry.

- **[[Ex - Chain complexes form a stable model category]]** (⭐⭐)
	- Verify that in $\mathbf{Ch}(R)$ the suspension is the shift $X[1]_n = X_{n-1}$, that it is invertible on $D(R)$, and hence that $D(R)$ is stable.
- **[[Ex - A pointed model category that is not stable]]** (⭐⭐)
	- Take pointed topological spaces or pointed simplicial sets and show $\Sigma$ is not essentially surjective (most spaces are not suspensions), so the model category is pointed but not stable.
- **[[Ex - Suspension and loop are inverse equivalences in the stable case]]** (⭐⭐⭐)
	- Show directly that stability forces the unit and counit of $\Sigma \dashv \Omega$ to be isomorphisms, and conversely, tying the definition to the adjoint-equivalence formulation.

> [!note] Exercise Index — §2
> [[Exercise Index - §2 Stable Model Categories]]

## §3 Weak Generators and Vistas

- **[[Def - Compact Weak Generator]]**
	- An object $G$ of a triangulated category $\mathcal{T}$ (with all coproducts) is a **weak generator** if $[G, X] = 0$ for all shifts forces $X = 0$ — equivalently, $G$ and its shifts detect nonzero objects. It is **compact** (or **small**) if $[G, -]$ commutes with arbitrary coproducts, $[G, \coprod_i X_i] \cong \bigoplus_i [G, X_i]$. A model category is **finitely generated** when its weak equivalences and generating cofibrations are controlled by compact objects. The pair "compact weak generator" is the hypothesis that makes a triangulated category as rigid as a category of modules: the sphere $\mathbb{S}$ generates $\mathcal{SH}$, and $R$ itself generates $D(R)$.

> [!tip] Unlocked: Schwede–Shipley Recognition and Endomorphism Ring Spectra *(from Derived Algebra)*
> **Schwede–Shipley.** If a stable model category $\mathcal{M}$ has a single compact weak generator $G$, then $\mathcal{M}$ is Quillen equivalent to modules over the **endomorphism ring spectrum** $\mathrm{End}(G)$ — a ring object in spectra whose homotopy groups are $[\,G, \Sigma^{-*} G\,]$. This is the homotopical upgrade of the Morita-theoretic fact that an abelian category with a compact projective generator is modules over its endomorphism ring. It says: *every* stable homotopy theory with one generator is "modules over a ring," provided you allow the ring to be a **ring spectrum** rather than an ordinary ring, which is the entry point to **brave new algebra** and **dg-categories**.

- **[[Ex - The sphere spectrum is a compact generator of the stable homotopy category]]** (⭐⭐⭐)
	- Show $\mathbb{S}$ generates $\mathcal{SH}$ (its shifts detect nonzero spectra) and is compact (a map out of $\mathbb{S}$ factors through a finite stage), so $\mathcal{SH}$ is "modules over $\mathbb{S}$."
- **[[Ex - R is a compact generator of its derived category]]** (⭐⭐)
	- Show the free module $R$ generates $D(R)$ and is compact, recovering $\mathrm{End}(R) = R$ and exhibiting $D(R)$ as "modules over $R$" in the trivial (Eilenberg–MacLane) case.
- **[[Ex - Identifying the triangulated examples]]** (⭐⭐)
	- Match $D(R)$, $\mathcal{SH}$, the stable module category, and $D^b(\mathrm{Coh}\,X)$ to their generators and decide in each case whether the generator is compact.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 Weak Generators and Vistas]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The recurring goals of this subject form a small, recognizable list. The most frequent is **establishing that a homotopy category is triangulated** — that some category of "homotopy types" carries the algebraic skeleton of distinguished triangles, so that the machinery of long exact sequences becomes available. A second is **computing long exact sequences**: given a map, build its cofiber sequence, apply a (co)homology functor, and read off the resulting long exact sequence — this is the daily bread of homological algebra and stable homotopy. A third is **recognizing a model category as stable**, that is, checking that suspension is invertible, which licenses everything else. A fourth is **identifying a triangulated category up to equivalence**, most sharply via a compact generator and the Schwede–Shipley theorem, which reduces an entire homotopy theory to a single ring(-spectrum). A fifth, more structural, is **transferring information across a triangle or an equivalence**: deducing properties of $Z$ from those of $X$ and $Y$ in a triangle $X \to Y \to Z \to \Sigma X$, or transporting structure along a derived equivalence. These five — triangulate, compute the long exact sequence, verify stability, identify by a generator, propagate along triangles — are the targets, and they recur because each is a way of *making a homotopy theory computable*: you understand a stable homotopy theory when you know its triangles, its generators, and which ordinary algebra it is secretly doing.

**Sources — what assumptions do we usually leverage?**

The hypotheses are equally stereotyped. **A pointed model category is given**, supplying a zero object, suspension, loop, and cofiber sequences for free — this is the richest source, because it is the entire unstable scaffolding from the previous chapter. **Suspension is known or shown to be invertible**: sometimes by construction (spectra are built to make $\Sigma$ invertible), sometimes by a direct computation (the degree shift on chain complexes is visibly invertible). **A category of chain complexes, or modules, is in play**, so that quasi-isomorphisms, mapping cones, and the projective/injective machinery are available and $\mathrm{Ho} = D(R)$. **A generator is available**, and one needs only to test compactness — whether maps out of it commute with coproducts. **A Quillen equivalence is given**, which descends to an equivalence of homotopy categories and transports the triangulated structure, since stability and triangulation are homotopy-invariant. The recurring move is to route a source to a target: a pointed model category with invertible $\Sigma$ routes through the **main theorem** to a triangulated structure; a triangle plus a homology functor routes to a long exact sequence; a compact generator routes through **Schwede–Shipley** to an identification as modules over a ring spectrum. The [[Model Categories — Stable Model Categories and Triangulated Categories#Problem-Solving Strategy|Problem-Solving Strategy]] makes these routes explicit.

---

# Legal Operations

These are the moves nearly every problem in this chapter is assembled from. When stuck, scan the list and try each. Everything is self-contained: a reader with no homotopy-theory background should be able to follow each operation from the description.

**Legal operations:**

1. **Complete a map to a distinguished triangle.** Given any morphism $f \colon X \to Y$ in a [[Def - Triangulated Category|triangulated category]], axiom TR1 guarantees an object $Z$ (the **cone**) and a triangle $X \xrightarrow{f} Y \to Z \to \Sigma X$. This is the single most-used move: it is the triangulated analogue of "put a map into a short exact sequence." *Trigger:* you have a map and want to understand what it forgets or what it is surjective onto. *Pattern:* "complete $f$ to a triangle and apply a (co)homology functor."

2. **Apply $\mathrm{Hom}(W, -)$ or $\mathrm{Hom}(-, W)$ to get a long exact sequence.** A [[Def - Triangulated Category|distinguished triangle]] becomes, under either hom-functor, a long exact sequence of abelian groups running in both directions through all shifts. This converts a single triangle into infinitely many exactness statements. *Trigger:* you want to compute or constrain a hom-group, an extension group, or a (co)homology group. *Pattern:* "the triangle gives $\cdots \to [W, X] \to [W, Y] \to [W, Z] \to [W, \Sigma X] \to \cdots$."

3. **Rotate a triangle.** By TR2, $X \to Y \to Z \to \Sigma X$ may be rotated to $Y \to Z \to \Sigma X \xrightarrow{-\Sigma f} \Sigma Y$ and backwards to $\Sigma^{-1} Z \to X \to Y \to Z$. Rotation lets you move any of the three objects into the "distinguished" first slot. *Trigger:* a theorem or long exact sequence is stated about the first map of a triangle but the map you care about is the second or third. *Pattern:* "rotate until the map of interest is $f \colon X \to Y$, then apply the result."

4. **Suspend or desuspend.** In a [[Def - Stable Model Category|stable]] category $\Sigma$ is invertible, so you may apply $\Sigma^n$ for any $n \in \mathbb{Z}$ to objects, maps, and entire triangles, and the result is again distinguished. This is the operation that the entire chapter is built to make legal. *Trigger:* an object is "in the wrong degree" for a comparison. *Pattern:* "shift the whole triangle by $[n]$ to line up degrees."

5. **Replace by a cofiber sequence.** When working in $\mathrm{Ho}(\mathcal{M})$ for a [[Def - Model Category|model category]], the distinguished triangles *are* the **cofiber sequences** $X \to Y \to Cf \to \Sigma X$ built from homotopy pushouts. To produce a triangle concretely, factor $f$ and take the homotopy cofiber. *Trigger:* you need an *explicit* triangle, not just an abstract one. *Pattern:* "the cone of $f$ is the homotopy pushout of $0 \leftarrow X \xrightarrow{f} Y$."

6. **Use the octahedral axiom on a composite.** Given $X \xrightarrow{f} Y \xrightarrow{g} Z$, TR4 relates the cones of $f$, $g$, and $g \circ f$ in a single octahedron. This is how the cofiber of a composite is analysed. *Trigger:* two composable maps appear and you want the cone of the composite. *Pattern:* "build the octahedron on $g \circ f$ and read off the triangle relating the three cones."

7. **Test or exhibit a (weak) generator.** To show $G$ is a [[Def - Compact Weak Generator|weak generator]], show $[G, \Sigma^n X] = 0$ for all $n$ forces $X = 0$; to show compactness, show $[G, -]$ commutes with coproducts. *Trigger:* you want to reduce a triangulated category to algebra or to prove an object is zero. *Pattern:* "$X = 0$ because every $G$-detector vanishes on it."

8. **Transport along a Quillen equivalence.** A [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] $\mathcal{M} \simeq \mathcal{N}$ induces an equivalence $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$ that preserves the zero object, suspension, and cofiber sequences, hence the entire triangulated structure. *Trigger:* one model presents the homotopy theory more conveniently than another. *Pattern:* "stability and triangulation are invariant under Quillen equivalence, so prove them in whichever model is easiest."

9. **Identify cofiber and fiber.** In a stable category the cofiber sequence of $f$ and the fiber sequence of $f$ agree up to a shift: $Cf \cong \Sigma(Ff)$. This lets you switch freely between "crush the source" and "take the homotopy fiber." *Trigger:* a problem is phrased with fibers but the available tool is about cofibers (or vice versa). *Pattern:* "in the stable world, $Ff$ and $Cf$ are the same sequence read in opposite directions."

**Illegal but tempting operations:**

> [!warning] 1. Treating the cone as a functor of the map
> It is tempting to think the cone $Z$ in $X \xrightarrow{f} Y \to Z \to \Sigma X$ depends *functorially* on $f$: that a map of maps induces a *canonical* map of cones. It does not. TR3 guarantees that *some* fill-in map of cones exists, but it is **not unique** and there is **no functorial choice** — this is the single deepest defect of triangulated categories. Concretely, in $D(R)$ two homotopic chain maps have the same cone, but a square that commutes only up to homotopy can induce genuinely different maps on cones. The operation becomes legal only when you remember the higher coherence data, which is exactly what a **stable ∞-category** or a stable model category does — the cone *is* functorial upstairs, before passing to the homotopy category.

> [!warning] 2. Forming distinguished triangles in an arbitrary additive category
> A short exact sequence $0 \to X \to Y \to Z \to 0$ in an abelian category looks like a triangle, so one is tempted to call it distinguished in $\mathcal{T}$, the additive category itself. But an ordinary additive (or abelian) category has *no invertible shift* — there is no $\Sigma$ with $\Sigma^{-1}$ — so it cannot be triangulated. The standard non-example is $\mathbf{Mod}_R$ itself: it is additive, it has short exact sequences, but suspension does not exist. The repair is to pass to the **derived category** $D(R)$, where the shift becomes the invertible degree-shift of complexes; only there do the short exact sequences become (a special source of) distinguished triangles.

> [!warning] 3. Assuming a pointed model category is automatically stable
> Having a zero object, suspension, and cofiber sequences is *not* enough for stability. Pointed [[Def - Topological Space|topological]] spaces have all of these, yet $\Sigma$ is not invertible: $S^0$ suspends to $S^1$, but $S^1$ has no desuspension among spaces, and most spaces are not suspensions at all. The homotopy category of pointed spaces is therefore **pre-triangulated** but not triangulated. The operation "desuspend" becomes legal exactly when you stabilize — pass to spectra, where $\Sigma$ is inverted by fiat — and stabilization is the price of admission to the triangulated world.

> [!warning] 4. Reading a triangulated category as if biproducts were direct sums of "subobjects"
> In an [[Def - Abelian Group|additive]] category one is tempted to treat the biproduct $X \oplus Y$ and the triangle's middle term as if triangles were short exact sequences with honest sub- and quotient objects. But triangulated categories have **no kernels or cokernels** in general — they are additive but almost never abelian. The map $X \to Y$ in a triangle has no kernel object; only its *cone* is defined. The standard trap is to try to "take the image" of a map in $D(R)$; there is no such object. What survives is the long exact sequence on homology, which is the correct, weaker shadow of exactness.

---

# Problem-Solving Strategy

The problems in this chapter are won at the moment you decide which of three worlds you are in — the abstract triangulated world, the concrete model-category world, or the generator-and-recognition world — because each has a fixed repertoire.

If the problem is **purely about a triangulated category and its triangles**, the master instrument is the long exact sequence. The route is almost mechanical: identify the relevant triangle (often by completing a given map to one with operation 1), apply $\mathrm{Hom}(W, -)$ or a (co)homology functor to it, and unwind the resulting long exact sequence to extract the group or vanishing you want. The two subtleties are *rotation* and *signs*: a long exact sequence is usually stated about the first map of a triangle, so you may need to rotate (operation 3) to line your map up, and the connecting maps carry the signs forced by TR2. When the problem involves a *composite* of two maps, the octahedral axiom (operation 6) is the specialized tool — it is precisely the statement that the cone of a composite is assembled from the cones of the factors, and it is the only axiom that says anything about composites at all. The guidance is to always ask "what triangle is this map a part of, and what does applying a hom-functor to it tell me?"

If the problem is **about a model category and whether its homotopy category is triangulated**, the route runs through the [[Thm - Characterization of Stable Model Categories|characterization theorem]]: the homotopy category of any pointed model category is **pre-triangulated**, and it is triangulated exactly when suspension is invertible. So the entire task reduces to **checking that $\Sigma$ is an equivalence on $\mathrm{Ho}(\mathcal{M})$** (operation 4's precondition). For chain complexes this is a one-line degree-shift computation; for spectra it is true by construction; for spaces it visibly fails. The non-obvious recognition is that you do *not* re-derive TR1–TR4 by hand — the previous chapter's pre-triangulated structure already supplies them, and stability is the single extra input. When two model categories are in play, remember that stability and triangulation are homotopy-invariant, so a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] (operation 8) lets you check the property in whichever model is most convenient.

If the problem **asks you to identify a triangulated category or reduce it to algebra**, the assumption pattern is the existence of a generator, and the route runs through compactness and the Schwede–Shipley theorem. You first show a candidate object $G$ is a [[Def - Compact Weak Generator|weak generator]] — its shifts detect nonzero objects — and then test whether $[G, -]$ commutes with coproducts to decide compactness (operation 7). If $G$ is a *single compact* generator, the homotopy theory is "modules over $\mathrm{End}(G)$," with $\mathrm{End}(G)$ an honest ring exactly when there are no higher homotopies (as for $D(R)$ with $G = R$) and a genuine **ring spectrum** otherwise (as for $\mathcal{SH}$ with $G = \mathbb{S}$). The decision point is always *compactness*: generation is usually easy, compactness is the real content, and it is exactly the condition that fails for "large" objects and holds for "finite" ones.

A meta-strategy threads through all three worlds: **whenever suspension is invertible, replace "subobject/quotient" thinking by "triangle" thinking.** The reflex from abelian-category algebra — take kernels, take images, chase short exact sequences — must be retrained, because triangulated categories have no kernels or cokernels. The correct reflex is to complete maps to triangles and apply hom-functors. Every question in this chapter is ultimately the question **"what is the cofiber, and what long exact sequence does it generate?"**

---

# Most Reusable Properties

- **[[Def - Triangulated Category|The long exact sequence of a triangle]]**: applying $\mathrm{Hom}(W, -)$ to a distinguished triangle yields a long exact sequence. This is the most-used single fact in the chapter because it is the *only* way exactness survives in a category with no kernels or cokernels. Reach for it whenever a hom-group, an Ext group, or a (co)homology group must be computed or constrained; it converts every triangle into an infinite supply of exactness relations. Its most powerful disguised use is *negative* — proving a group vanishes by sandwiching it between two zeros in the sequence — which is how most "this map is an isomorphism" arguments in $D(R)$ actually run.

- **[[Thm - The Homotopy Category of a Stable Model Category is Triangulated|Cofiber sequences are the distinguished triangles]]**: in $\mathrm{Ho}(\mathcal{M})$ for a stable model category, the triangles are exactly the cofiber sequences. This is the workhorse for *producing* triangles concretely: to get a triangle, factor a map and take its homotopy cofiber. The recognizable setup is "I have a map of spaces/complexes and want a long exact sequence"; the cofiber sequence delivers the triangle, and operation 2 delivers the sequence. It is also what guarantees that the abstract axioms have any models at all.

- **[[Def - Stable Model Category|Stability is invertibility of Σ]]**: a pointed model category is stable iff suspension is an equivalence. The reusable move is the equivalence itself — to *check* triangulation, check that $\Sigma$ is invertible; to *use* stability, freely apply $\Sigma^{\pm n}$ and identify cofibers with fibers (operations 4 and 9). Stability is the hinge on which the whole chapter turns, and it is almost always verified by a single computation on the suspension functor rather than by checking any of the triangulated axioms directly.

- **[[Def - Compact Weak Generator|Compact generation]]**: a single compact weak generator makes a triangulated category as rigid as modules over a ring (spectrum). Its typical use is in *identification* and in *theorem-proving by induction on a generating class*: to prove a statement for all objects, prove it for the generator and check it is closed under triangles, shifts, and coproducts. It is the reason $D(R)$ and $\mathcal{SH}$ are tractable at all, and it is the precise hypothesis behind the Schwede–Shipley recognition theorem.

- **[[Def - Quillen Adjunction and Quillen Equivalence|Homotopy-invariance of the structure]]**: stability, triangulation, and the triangulated structure all descend along Quillen equivalences. The typical use is to *change models*: prove a property in the simplicial-set model, the chain-complex model, or the spectrum model, whichever is most convenient, and transport it. It is what licenses the entire practice of "presenting" a homotopy theory by a model category — the presentation is auxiliary, the triangulated homotopy category is the invariant.

---

# Bridges

1. **Homological algebra — the derived category and the long exact sequence.** The [[Def - Chain Map and Chain Homotopy|derived category]] $D(R)$ is the homotopy category of [[Def - Chain Map and Chain Homotopy|chain complexes]] of $R$-[[Def - Module|modules]] with quasi-isomorphisms inverted, and it is the original triangulated category. A short exact sequence of complexes $0 \to A \to B \to C \to 0$ becomes a distinguished triangle $A \to B \to C \to \Sigma A$ in $D(R)$, and the long exact sequence of homology associated to it is *precisely* the long exact sequence (operation 2) obtained by applying $H_0 = [\,R, -\,]$ to that triangle. So the connecting homomorphism $\partial \colon H_n(C) \to H_{n-1}(A)$ that students meet in a first homology course is the shift map $C \to \Sigma A$ of the triangle, made visible. The derived functors $\mathrm{Tor}$ and $\mathrm{Ext}$ are the homology and hom-groups of triangles built from resolutions; the entire subject of **derived functors** is triangle-computation in $D(R)$.

2. **Algebraic topology — spectra and generalized cohomology.** A **spectrum** is a sequence of pointed spaces $E_n$ with structure maps $\Sigma E_n \to E_{n+1}$; the category of spectra is built precisely so that suspension becomes invertible, making its homotopy category $\mathcal{SH}$ a stable model category's triangulated homotopy category. Every **generalized cohomology theory** — singular cohomology, topological $K$-theory, cobordism — is represented by a spectrum, with the cofiber sequence of a pair of spaces inducing the long exact sequence of the cohomology theory via operation 2. The **stable homotopy groups of spheres** $\pi_n^s = [\Sigma^n \mathbb{S}, \mathbb{S}]$ are the endomorphisms of the unit object $\mathbb{S}$, which by the recognition theorem is the compact generator that makes $\mathcal{SH}$ "modules over the sphere spectrum."

3. **Algebraic geometry — the derived category of coherent sheaves.** Replace $R$-modules by **coherent sheaves** on an algebraic variety $X$ — locally, modules over the coordinate rings glued along overlaps — and complexes of modules by complexes of sheaves. Inverting quasi-isomorphisms produces the bounded derived category $D^b(\mathrm{Coh}\,X)$, a triangulated category that has become the central invariant of $X$. The bridge is exact: the same construction (chain complexes, quasi-isomorphisms, mapping cones as triangles) that gives $D(R)$ gives $D^b(\mathrm{Coh}\,X)$ when the ring is replaced by the *sheaf* of rings on $X$. Distinct varieties can have equivalent derived categories (**Fourier–Mukai** equivalences), so the triangulated structure sees a "derived" notion of geometry finer than isomorphism of varieties; the self-contained account is in [[Def - Triangulated Category#Examples / Corollaries]].

4. **Higher category theory — stable ∞-categories repair functoriality.** The one structural defect of triangulated categories is that the cone is not functorial (illegal operation 1): TR3 gives a fill-in map of cones but no canonical or unique one. The **stable ∞-category** fixes this by retaining the homotopy-coherent data that the homotopy category discards — the actual cones, together with the higher homotopies witnessing their universal properties. A stable ∞-category has a triangulated homotopy category, but unlike a bare triangulated category it *remembers* how the triangles were built, so cones, total complexes, and gluing become functorial. Every [[Def - Stable Model Category|stable model category]] presents a stable ∞-category, and this is the cleanest answer to "what is the model-category apparatus of this chapter ultimately a presentation of." This is the bridge from Hovey's book to the contemporary Lurie-era foundations.

---

# Insights

**The unifying frame: stabilization is the act of making suspension invertible, and triangulation is its receipt.** The single idea behind the entire chapter is that the unstable homotopy world is *directional* — you can suspend but not desuspend — and that forcing reversibility produces a qualitatively new, *linear* world. Every phenomenon in the chapter is downstream of one inversion: additivity (because invertible $\Sigma$ makes everything a double-loop object, and double-loop objects are abelian by Eckmann–Hilton), the coincidence of cofiber and fiber sequences (because $\Omega$ now undoes $\Sigma$), and the triangulated axioms themselves (the algebraic bookkeeping that survives). When you see "stable," translate it instantly to "$\Sigma$ invertible," and when you see "triangulated," translate it to "the algebra left over after stabilization." The triangulated structure is not imposed; it is the inevitable shadow of an invertible suspension.

**The true name of a distinguished triangle is "cofiber sequence."** The axiomatic definition — a class of diagrams closed under rotation and satisfying the octahedral axiom — is the right thing to *check* but the wrong thing to *think*. Operationally, a distinguished triangle is the homotopy-categorical trace of a cofiber sequence $X \to Y \to Cf \to \Sigma X$: crush $X$ inside $Y$ to get $Cf$, then the connecting map records how $X$ was attached. Every time you see a triangle, picture a map and its homotopy cofiber, with the third map measuring the attaching data. This is why the long exact sequence of a triangle *is* the long exact sequence of a pair in topology and the long exact sequence of homology in algebra: those are the cofiber sequence's shadow under a cohomology functor.

**The non-functoriality of the cone is the seam where triangulated categories fail, and it is exactly the seam that ∞-categories were invented to close.** It is tempting to treat triangulated categories as the final word on stable homotopy theory, but they leak: the cone exists but not functorially, so you cannot in general take total complexes, glue triangles, or define a cone *of a map of triangles* canonically. This is not a minor blemish — it is the reason a generation of homological algebra was conducted with carefully hand-chosen resolutions and ad hoc sign conventions. The diagnostic to remember is that *any construction requiring a canonical or natural choice of cone is illegitimate in a triangulated category* and must be performed one level up, in a stable model category or stable ∞-category, where the coherence data lives. Triangulated categories are best understood as the deliberately-forgetful $1$-categorical residue of a richer structure, kept around because they are computable, the same way $\mathrm{Ho}(\mathcal{M})$ is the computable residue of $\mathcal{M}$.

**A trigger-reaction pattern: "compact generator" should fire "modules over a ring spectrum."** Whenever a triangulated category turns out to be generated by a single compact object, the Schwede–Shipley theorem says it *is* a category of modules — over an ordinary ring when there are no higher homotopies, over a ring spectrum in general. This is the homotopical Morita theorem, and it is the deepest single result in the chapter's vista. The reflex to install: on seeing a generator, immediately test compactness (does $[G, -]$ commute with coproducts?), because compactness is the dividing line between "tractable, module-like" and "wild." The same reflex recovers classical Morita theory when the generator is a compact projective in an abelian category, which is the input-type bridge that makes the homotopical statement feel inevitable rather than miraculous.
