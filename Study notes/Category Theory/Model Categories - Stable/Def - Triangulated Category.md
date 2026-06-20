---
type: definition
subject: model-categories
prereqs:
  - "Def - Abelian Group"
  - "Def - Category"
  - "Def - Functor"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{T}$ is a category whose hom-sets $\mathrm{Hom}_{\mathcal{T}}(X, Y)$ (also written $\mathcal{T}(X, Y)$) are [[Def - Abelian Group|abelian groups]] with bilinear composition — that is, $\mathcal{T}$ is **additive** (see the per-axiom discussion). The shift is an additive automorphism $\Sigma \colon \mathcal{T} \to \mathcal{T}$, also written $[1]$, with iterates $X[n] = \Sigma^n X$ for all $n \in \mathbb{Z}$ (the inverse $\Sigma^{-1} = [-1]$ exists because $\Sigma$ is an automorphism). A **triangle** is a diagram $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$; its third map $w$ lands in the shift of the first object and is called the **connecting** or **boundary** map. We write $0$ for the zero object and $0 \colon X \to Y$ for the zero morphism. The full symbol registry is on [[Model Categories — Stable Model Categories and Triangulated Categories]].

This is a compound page in spirit: it defines an *additive category*, a *shift*, a *distinguished triangle*, and the four axioms TR1–TR4 together, because none of these is usable without the others — a triangulated category *is* the package.

---

# Axiom Motivation

The right way to discover this definition is to ask what survives when you try to do homological algebra in a category that has *no kernels and no cokernels*. In an abelian category — modules over a ring, say — the fundamental object is the short exact sequence $0 \to X \to Y \to Z \to 0$, and the fundamental tool is the long exact sequence it induces under a derived functor. But the moment you pass to the [[Def - Chain Map and Chain Homotopy|derived category]] $D(R)$, where you have inverted quasi-isomorphisms so that complexes related by a chain homotopy equivalence become *equal*, the abelian structure collapses. A chain map no longer has a well-defined kernel object; "the image of a map" stops making sense. Yet the thing you actually wanted — the long exact sequence — survives. The axioms of a triangulated category are the minimal bookkeeping needed to keep the long exact sequence alive after the abelian structure is gone.

So the desideratum is sharp: we want a category, additive but not abelian, in which (i) every map can be completed to something that plays the role of a short exact sequence, and (ii) applying any hom-functor to that something yields a long exact sequence. The "something" is the **distinguished triangle** $X \to Y \to Z \to \Sigma X$, and the appearance of the *shift* $\Sigma X$ in the fourth slot is the first surprise. Why is it there? Because in the derived category the cokernel of $X \hookrightarrow Y$ is replaced by the **mapping cone** $Z = Cf$, and the mapping cone of an injection of complexes is quasi-isomorphic to the honest cokernel — but the cone construction *also* shifts degree, so the natural continuation of the sequence is not $Z \to 0$ but $Z \to \Sigma X$, recording the attaching data. The triangle is a short exact sequence that has been bent into a loop by the shift; this is exactly why it is drawn as a triangle.

Now consider why **additivity** is required and what breaks without it. We need hom-sets to be abelian groups so that "exactness" — the equality of an image and a kernel of induced maps — even has a meaning at the level of the long exact sequence. If we dropped additivity and allowed arbitrary hom-sets, the long exact sequence (the entire point) could not be stated: there would be no zero map to be the image, no group in which to measure exactness. Additivity is also why finite products and coproducts coincide (they become **biproducts** $X \oplus Y$), which is needed because a triangle on a direct sum should split as a sum of triangles. Strengthening additivity all the way to *abelian* would, by contrast, be too strong: it would reintroduce kernels and cokernels and force the category back into ordinary homological algebra, defeating the purpose. The Goldilocks condition is additive-but-not-abelian.

Each of the four axioms answers a specific failure. **TR1** demands that identities sit in triangles ($X \xrightarrow{1} X \to 0 \to \Sigma X$), that triangles are stable under isomorphism, and — the substantive part — that *every* map $f$ extends to a triangle $X \xrightarrow{f} Y \to Z \to \Sigma X$. Drop the last clause and you cannot complete a map to anything, so operation "take the cone" disappears and no long exact sequence can ever be formed. **TR2 (rotation)** demands that a triangle may be rotated, $Y \to Z \to \Sigma X \xrightarrow{-\Sigma u} \Sigma Y$ being distinguished whenever $X \to Y \to Z \to \Sigma X$ is. Without it the three objects of a triangle would play asymmetric roles, and the long exact sequence — which runs symmetrically in both directions through all shifts — could not close up; rotation is what makes the sequence bi-infinite. The mysterious *sign* $-\Sigma u$ is forced: it is what makes "rotate three times" return you to the suspended original with the correct sign, the triangulated echo of the sign in the boundary of a simplex. **TR3 (morphisms of triangles)** demands that a commuting square on the first two objects extends to a map of whole triangles. Without it you could not compare triangles, and the five lemma — the engine that turns the long exact sequence into isomorphism statements — would have nothing to act on. **TR4 (the octahedral axiom)** is the subtle one: it governs how the cones of $f$, $g$, and $g \circ f$ fit together, and without it the long exact sequences of composable maps would not be compatible. It is the triangulated avatar of the third isomorphism theorem $(G/K)/(L/K) \cong G/L$: the cofiber of a composite is the cofiber of the cofibers.

The honest caveat, which the motivation must include because it explains a later chapter: TR3 asks only that *a* fill-in map of triangles exist, **not that it be unique**. This non-uniqueness is a genuine defect — the cone is not a functor of the map — and it is not repairable within the axioms. It is the reason triangulated categories are best seen as the $1$-categorical shadow of a richer structure (a **stable ∞-category** or stable model category) where the missing coherence lives. A reader who has internalized this caveat could reinvent the whole definition: it is "additive category $+$ invertible shift $+$ a notion of cone that is good enough to produce long exact sequences but, by design, only good enough."

---

# The Definition

A **triangulated category** is an [[Def - Abelian Group|additive]] category $\mathcal{T}$ together with:

- an **additive automorphism** $\Sigma \colon \mathcal{T} \to \mathcal{T}$ (the **shift** or **suspension**, written $[1]$), and
- a class of **distinguished triangles**, each a diagram of the form
$$X \xrightarrow{\ u\ } Y \xrightarrow{\ v\ } Z \xrightarrow{\ w\ } \Sigma X,$$

satisfying the following axioms.

**(TR1)**
(a) Every morphism $u \colon X \to Y$ is the first map of some distinguished triangle $X \xrightarrow{u} Y \to Z \to \Sigma X$.
(b) For every object $X$, the triangle $X \xrightarrow{\,1_X\,} X \to 0 \to \Sigma X$ is distinguished.
(c) Any triangle isomorphic to a distinguished triangle is distinguished. (A morphism of triangles is a triple $(f, g, h)$ making the three squares commute; an isomorphism of triangles is one with all three of $f, g, h$ isomorphisms.)

**(TR2)** (Rotation.) The triangle $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ is distinguished if and only if its rotation
$$Y \xrightarrow{\ v\ } Z \xrightarrow{\ w\ } \Sigma X \xrightarrow{\ -\Sigma u\ } \Sigma Y$$
is distinguished.

**(TR3)** (Morphisms of triangles.) Given two distinguished triangles and morphisms $f \colon X \to X'$, $g \colon Y \to Y'$ with $g \circ u = u' \circ f$ (the left square commutes), there exists a morphism $h \colon Z \to Z'$ completing $(f, g, h)$ to a morphism of triangles (the other two squares commute). The map $h$ need not be unique.

**(TR4)** (The octahedral axiom.) Given morphisms $u \colon X \to Y$ and $v \colon Y \to Z$ with composite $vu \colon X \to Z$, complete each of $u$, $v$, $vu$ to distinguished triangles with cones $Z' = C(u)$, $X' = C(v)$, $Y' = C(vu)$. Then there are morphisms making
$$Z' \to Y' \to X' \to \Sigma Z'$$
a distinguished triangle, compatibly with the maps already present, so that the four triangles fit together as the faces of an octahedron.

A **consequence** packaged into the definition's usefulness: for any object $W$, applying $\mathrm{Hom}_{\mathcal{T}}(W, -)$ to a distinguished triangle yields a long exact sequence of abelian groups
$$\cdots \to [W, \Sigma^{-1}Z] \to [W, X] \xrightarrow{u_*} [W, Y] \xrightarrow{v_*} [W, Z] \xrightarrow{w_*} [W, \Sigma X] \to \cdots,$$
and likewise $\mathrm{Hom}_{\mathcal{T}}(-, W)$ yields a long exact sequence running the other way. (This is a *theorem* from the axioms, proved on [[Thm - The Homotopy Category of a Stable Model Category is Triangulated|the theorem page]] and drilled in [[Ex - The long exact sequence induced by a distinguished triangle]].)

---

# Categorical / Structural Definition

The structural content can be stated without reference to elements at all, which is the point of working in $\mathcal{T}$. *Additive* means $\mathcal{T}$ is enriched in [[Def - Abelian Group|abelian groups]] (each hom-set is an abelian group, composition is $\mathbb{Z}$-bilinear) and has a zero object and finite biproducts — finite products and coproducts exist and coincide, $X \times Y \cong X \oplus Y \cong X \sqcup Y$. The shift $\Sigma$ is an automorphism *of additive categories*: an equivalence $\mathcal{T} \to \mathcal{T}$ that is invertible on the nose (or up to coherent isomorphism) and respects the abelian-group structure on hom-sets.

The cleanest modern phrasing of "distinguished triangle" is via the **cofiber**. In the homotopy category of a stable model category (or a stable ∞-category), a triangle is distinguished precisely when it is isomorphic to one of the form $X \xrightarrow{u} Y \to Cu \to \Sigma X$, where $Cu$ is the **homotopy cofiber** of $u$ — the homotopy pushout of $0 \leftarrow X \xrightarrow{u} Y$ — and the connecting map $Cu \to \Sigma X$ is the canonical map exhibiting $\Sigma X$ as the cofiber of $Y \to Cu$. From this vantage TR1 is "homotopy pushouts exist," TR2 is "the cofiber of $Y \to Cu$ is $\Sigma X$" (the Puppe phenomenon), TR3 is the functoriality-up-to-homotopy of pushouts, and TR4 is the pasting law for homotopy pushouts. The triangulated axioms are thus a *presentation by generators and relations* of the homotopy-categorical shadow of "the category has cofiber sequences and they are invertible under shift." This is exactly the content of the **characterization theorem**: a pre-triangulated structure becomes triangulated when $\Sigma$ is invertible.

---

# Relate to Other Fields / Compression

A triangulated category is what an abelian category *degenerates to* after you invert a class of weak equivalences and lose the kernel/cokernel calculus. The single most useful compression is the dictionary with short exact sequences: the distinguished triangle $X \to Y \to Z \to \Sigma X$ is the derived-category replacement for the short exact sequence $0 \to X \to Y \to Z \to 0$, with two differences — the cokernel $Z$ is replaced by the homotopy-invariant **cone**, and the sequence does not terminate but continues into $\Sigma X$, recording the failure of $X \to Y$ to be a genuine monomorphism. The long exact sequence on homology that every short exact sequence of complexes induces is *literally* the long exact sequence the triangle induces under $H_*$.

**True name:** the true name of a triangulated category is "a category with functorial-enough cofiber sequences and an invertible shift." You should think *cofiber sequence*, not *axiom list*: a distinguished triangle is a map together with its homotopy cofiber and the suspended connecting map, and the four axioms are exactly the formal properties of cofiber sequences that survive passage to the homotopy category. Everything operational — long exact sequences, the five lemma, devissage along a generating class — flows from reading "triangle" as "map and its cone."

The defect to keep in mind for compression purposes: a triangulated category is *additive but not abelian*, so it has biproducts but no kernels, cokernels, images, or honest exact sequences. Any technique from abelian-category homological algebra that uses an *object*-level kernel or image must be translated into a triangle plus a long exact sequence before it can be used here.

---

# Examples / Corollaries

**Is an instance — the derived category $D(R)$.** For a [[Def - Ring|ring]] $R$, the derived category $D(R)$ has as objects the [[Def - Chain Map and Chain Homotopy|chain complexes]] of $R$-[[Def - Module|modules]] and as morphisms the chain-homotopy classes, with quasi-isomorphisms inverted. The shift is the degree shift $X[1]_n = X_{n-1}$ (with differential negated), visibly an automorphism. The distinguished triangles are the diagrams isomorphic to mapping-cone sequences $X \xrightarrow{f} Y \to Cf \to X[1]$. Applying $H_0 = [\,R[0], -\,]$ to such a triangle reproduces the long exact sequence of homology that any short exact sequence of complexes induces. This is the original triangulated category, Verdier's motivating example, and the prototype for everything else.

**Is an instance — the stable homotopy category $\mathcal{SH}$.** The homotopy category of **spectra** is triangulated, with shift the (now invertible) suspension $\Sigma$ and triangles the cofiber sequences of maps of spectra. Here the long exact sequence of a triangle, under the functor $\pi_* = [\,\mathbb{S}, -\,]$, is the long exact sequence of stable homotopy groups associated to a cofiber sequence — the stable analogue of the long exact sequence of a pair in topology. The unit object is the **sphere spectrum** $\mathbb{S}$, and $[\Sigma^n \mathbb{S}, \mathbb{S}] = \pi_{-n}^s$ are the stable homotopy groups of spheres.

**Is an instance — the stable module category.** Over a self-injective (e.g. group-algebra) ring $\Lambda$, the **stable module category** $\underline{\mathbf{Mod}}_\Lambda$ has the same objects as $\mathbf{Mod}_\Lambda$ but morphisms taken modulo maps that factor through a projective. Its shift is $\Omega^{-1}$, the cosyzygy, and its triangles come from short exact sequences. It is triangulated, and it is the homotopy category of a stable model structure — exactly the kind of example the chapter's main theorem produces.

> [!note]- Algebraic geometry background: the derived category of coherent sheaves
> No algebraic geometry is assumed; here is everything needed from scratch.
>
> A **commutative ring** $R$ (think $\mathbb{C}[x, y]$, polynomials in two variables) has a geometric avatar: its **prime spectrum** $\mathrm{Spec}\,R$, the set of prime ideals, topologized so that closed sets are the vanishing loci of collections of polynomials (the **Zariski topology**). An **affine variety** is, up to this dictionary, the same data as a commutative ring: geometry on the left, algebra on the right, with functions on the variety being elements of the ring. A general **variety** (or scheme) $X$ is glued from affine pieces, just as a manifold is glued from Euclidean charts; over each affine piece $\mathrm{Spec}\,R$ the functions form the ring $R$.
>
> A **sheaf** on $X$ assigns, to each open set $U$, an abelian group (or module) $\mathcal{F}(U)$ — "sections over $U$" — compatibly with restriction to smaller opens and gluing of locally-defined sections. A **coherent sheaf** is the geometric version of a finitely generated module: over each affine chart $\mathrm{Spec}\,R$ it is (essentially) a finitely generated $R$-module, and the charts are glued along overlaps. The coherent sheaves on $X$ form an [[Def - Abelian Group|additive]], indeed abelian, category $\mathrm{Coh}\,X$ — kernels, cokernels, and short exact sequences all make sense, exactly as for modules, because everything is modules locally.
>
> Now run the derived-category construction *with $\mathrm{Coh}\,X$ in place of $\mathbf{Mod}_R$*: take bounded chain complexes of coherent sheaves, identify chain-homotopic maps, and invert quasi-isomorphisms (maps inducing isomorphisms on cohomology sheaves). The result is the **bounded derived category** $D^b(\mathrm{Coh}\,X)$. By exactly the argument that makes $D(R)$ triangulated — mapping cones are the cones, the degree shift is the invertible $\Sigma$ — $D^b(\mathrm{Coh}\,X)$ is a **triangulated category**.
>
> Why this is the illuminating example: $D^b(\mathrm{Coh}\,X)$ is, in modern algebraic geometry, *the* invariant of a variety. The categorical concept it illustrates is that a triangulated category can encode geometry too subtle for the underlying space to see. Two *non-isomorphic* varieties can have *equivalent* derived categories — a **derived equivalence**, the most famous being the **Fourier–Mukai** equivalence between an abelian variety and its dual — so $D^b$ is a genuinely coarser-yet-richer invariant than the variety itself. Conversely, the **Bondal–Orlov theorem** says that if the (anti)canonical bundle of $X$ is ample, then $D^b(\mathrm{Coh}\,X)$ determines $X$ completely. The triangulated structure — cones, shifts, long exact sequences of cohomology sheaves — is precisely the machinery in which all of this is stated and proved. This is the running **Algebraic Geometry** bridge of the Category Theory notes, here taking its homological form.

**Is NOT an instance — an ordinary abelian category $\mathbf{Mod}_R$.** The category of $R$-modules is additive (indeed abelian) and has short exact sequences, but it is **not** triangulated: there is no shift automorphism $\Sigma$. Suspension does not exist among modules, so there is nothing to put in the fourth slot of a triangle, and there is no way to rotate. The repair is to pass to $D(R)$, where the degree shift of complexes supplies the missing invertible $\Sigma$.

**Is NOT an instance — the homotopy category of pointed spaces.** Pointed [[Def - Topological Space|topological]] spaces have a zero object, a suspension $\Sigma$, and cofiber sequences, so their homotopy category is **pre-triangulated**. But $\Sigma$ is *not invertible* — most spaces are not suspensions, and you cannot desuspend $S^1$ within spaces — so the category fails TR2's symmetry and is not triangulated. This is the canonical witness that "pre-triangulated $\neq$ triangulated," and it is exactly what stabilization fixes.

**Calibration check.** Verify that in any triangulated category the composite of two consecutive maps in a triangle is zero ($v \circ u = 0$, since $\mathrm{Hom}(X, -)$ applied to the triangle has $u_* v_* = 0$ at the first object, or directly from TR1 applied to $1_X$). Verify that a triangle $X \xrightarrow{u} Y \to Z \to \Sigma X$ with $u$ an isomorphism forces $Z \cong 0$. And confirm you can state, without looking, why $\mathbf{Mod}_R$ is not triangulated while $D(R)$ is — if the answer "no invertible shift" comes immediately, you have understood the definition.

---

# Unlocked by This

> [!tip] t-Structure and the Heart *(from Homological Algebra)*
> A **t-structure** on $\mathcal{T}$ is a pair of full subcategories $(\mathcal{T}^{\leq 0}, \mathcal{T}^{\geq 0})$ behaving like "complexes in non-negative / non-positive degrees," with the **heart** $\mathcal{T}^{\leq 0} \cap \mathcal{T}^{\geq 0}$ an honest abelian category. The standard t-structure on $D(R)$ has heart $\mathbf{Mod}_R$, so ordinary homological algebra sits *inside* the triangulated category as the heart. Exotic t-structures (perverse sheaves on a variety) are the engine of geometric representation theory.

> [!tip] Derived Functors, Tor and Ext *(from Derived Algebra)*
> Once you have triangles, **derived functors** are just "apply a functor to a triangle built from a resolution and take homology." $\mathrm{Tor}^R_n(M, N)$ and $\mathrm{Ext}^n_R(M, N)$ become the homology and hom-groups of distinguished triangles in $D(R)$, and their long exact sequences are the triangle long exact sequences. The whole subject of **derived/homological algebra** is the calculus of triangles in $D(R)$.

> [!tip] Bridgeland Stability Conditions *(from Algebraic Geometry)*
> A **stability condition** on $D^b(\mathrm{Coh}\,X)$ is a t-structure-like datum (a heart plus a central charge) whose **moduli of stable objects** recover and generalize classical moduli of sheaves. This is a frontier where the triangulated structure feeds directly into enumerative geometry and mirror symmetry; it is only definable because $D^b$ is triangulated.
