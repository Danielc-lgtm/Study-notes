---
type: definition
subject: model-categories
prereqs:
  - "Def - Triangulated Category"
  - "Def - Stable Model Category"
  - "Def - Limit and Colimit"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{T}$ is a [[Def - Triangulated Category|triangulated category]] that has all (small) **coproducts** $\coprod_i X_i$ — typically $\mathcal{T} = \mathrm{Ho}(\mathcal{M})$ for a [[Def - Stable Model Category|stable model category]] $\mathcal{M}$ that is cocomplete. We write $[X, Y] = \mathrm{Hom}_{\mathcal{T}}(X, Y)$ for the morphism [[Def - Abelian Group|abelian group]], $\Sigma$ for the shift, and $\Sigma^n X = X[n]$ for its iterates ($n \in \mathbb{Z}$). For an object $G$, the functors $[G, -]$ and $[\Sigma^n G, -]$ are the **detectors** associated with $G$. The endomorphism ring object is $\mathrm{End}(G)$, with homotopy groups $\pi_n \mathrm{End}(G) = [\Sigma^n G, G]$. The full registry is on [[Model Categories — Stable Model Categories and Triangulated Categories]].

This is a compound page: it defines a **weak generator**, the notion of a **compact** (or **small**) object, the combined **compact weak generator**, and the related notion of a **finitely generated model category** — because the recognition theory that motivates all of them needs the four together.

---

# Axiom Motivation

The motivation is a single question: when is a triangulated category — a priori a wild, kernel-free, cone-non-functorial object — as tractable as a category of [[Def - Module|modules]] over a ring? The answer turns on two independent properties of a chosen object $G$, and the definition is the conjunction of exactly those two.

The first property is **generation**: $G$ should be rich enough that nothing is invisible to it. In ordinary [[Def - Module|module]] theory, the free module $R$ generates $\mathbf{Mod}_R$ because every module is a quotient of a free one, equivalently because $\mathrm{Hom}_R(R, M) = M$ detects $M$ entirely — if $\mathrm{Hom}_R(R, M) = 0$ then $M = 0$. We want the triangulated analogue. The naive demand "every object is a colimit of copies of $G$" is too strong and too structure-dependent in a triangulated setting (colimits behave badly). The right, weakest demand is *detection*: $G$ together with its shifts should detect nonzero objects, i.e. if $[\Sigma^n G, X] = 0$ for all $n$ then $X = 0$. This is the **weak generator** condition. Why include all shifts? Because in a triangulated category an object lives "in all degrees at once" — the shifts of $G$ are as much a part of $G$'s reach as $G$ itself, and a single fixed $G$ without its shifts would miss objects concentrated in degrees $G$ does not see. Drop the shifts and the sphere spectrum $\mathbb{S}$ would fail to generate $\mathcal{SH}$, even though it morally should; including the shifts is what makes generation match the intuition.

What breaks if we drop generation entirely? Then $\mathcal{T}$ could contain a nonzero object invisible to $G$ — a "phantom" piece of the category that no amount of mapping out of $G$ can see — and any attempt to reconstruct $\mathcal{T}$ from $\mathrm{End}(G)$-modules would silently lose that piece. Generation is exactly the no-blind-spots axiom.

The second property is **compactness** (the term "small" is synonymous in this context). Generation alone is not enough to get a *module-category* description, because the dictionary "$X \leftrightarrow [G, X]$" must convert **coproducts** in $\mathcal{T}$ into **direct sums** of $\mathrm{End}(G)$-modules. That conversion is the statement that $[G, -]$ commutes with coproducts: $[G, \coprod_i X_i] \cong \bigoplus_i [G, X_i]$. This is **not automatic** — for a general object the canonical map $\bigoplus_i [G, X_i] \to [G, \coprod_i X_i]$ is injective but can fail to be surjective, because a map out of $G$ into an infinite coproduct might genuinely "spread across infinitely many summands." Compactness is exactly the condition that it cannot: a map out of a compact object factors through a *finite* sub-coproduct. The word names the topological intuition — a compact object is one for which "covers have finite subcovers," transplanted to category theory as "maps into colimits factor through finite stages."

What breaks if we drop compactness? Generation without compactness still detects objects, but the equivalence with $\mathrm{End}(G)$-modules fails: the module category has all direct sums, but $[G, -]$ would not match $\mathcal{T}$'s coproducts to them, so the comparison functor would not be an equivalence. The canonical illustration is that the **sphere spectrum is compact** (a finite spectrum maps into a coproduct through finitely many summands) which is *why* $\mathcal{SH}$ is "modules over $\mathbb{S}$," whereas a non-compact generator would not yield such a clean description. Compactness is the finiteness axiom that makes the algebra honest.

Could a reader invent the conjunction? Yes: start from "I want $\mathcal{T} \simeq \mathrm{Mod}\text{-}\mathrm{End}(G)$," and ask what $G$ must satisfy for the functor $X \mapsto [G, X]$ to be an equivalence. Faithful detection of objects forces *generation*; matching coproducts to direct sums forces *compactness*. The two desiderata are independent and jointly exactly what is needed — which is why the definition pairs them, and why the recognition theorem (Schwede–Shipley) has exactly this hypothesis.

---

# The Definition

Let $\mathcal{T}$ be a [[Def - Triangulated Category|triangulated category]] with all coproducts, and $G$ an object.

**Weak generator.** $G$ is a **weak generator** of $\mathcal{T}$ if its shifts detect nonzero objects:
$$\big[\,\Sigma^n G,\ X\,\big] = 0 \ \text{ for all } n \in \mathbb{Z} \quad\Longrightarrow\quad X \cong 0.$$
Equivalently, the smallest full triangulated subcategory of $\mathcal{T}$ containing $G$ and closed under coproducts is all of $\mathcal{T}$.

**Compact (small) object.** $G$ is **compact** (also **small** or **finite**) if the functor $[G, -]$ commutes with arbitrary coproducts: for every family $\{X_i\}_{i \in I}$, the canonical map
$$\bigoplus_{i \in I} \big[\,G,\ X_i\,\big] \ \xrightarrow{\ \cong\ } \ \big[\,G,\ \textstyle\coprod_{i \in I} X_i\,\big]$$
is an isomorphism.

**Compact weak generator.** $G$ is a **compact weak generator** if it is both a weak generator and compact.

**Finitely generated model category.** A cofibrantly generated [[Def - Model Category|model category]] is **finitely generated** if it has sets of generating cofibrations and generating trivial cofibrations whose domains and codomains are **finite** relative to the cofibrations (their hom-functors commute with the relevant filtered colimits) — the model-category-level finiteness that makes the compact objects of $\mathrm{Ho}(\mathcal{M})$ plentiful and well-behaved. In the stable case, finite generation is the input that guarantees a compact generator on the homotopy category.

---

# Categorical / Structural Definition

Generation and compactness are both purely categorical and worth stating without the triangulated trimmings.

*Compactness* is the general categorical notion of a **compact (finitely presentable) object**: $G$ is compact if $\mathrm{Hom}(G, -)$ preserves the relevant colimits — filtered colimits in the unenriched setting, coproducts in the triangulated/additive setting (where, because every object is a coproduct of shifts of generators built by triangles, coproduct-preservation is the operative form). It is the exact categorical transcription of "maps out of $G$ are determined by finite data."

*Generation* is the categorical notion of a **(strong/weak) generator**, an object $G$ such that the functor $\mathrm{Hom}(G, -)$ (here together with its shifts) is **conservative** — it reflects isomorphisms, equivalently it detects the zero object. A family that jointly detects zero is a **generating set**; a single such object is a generator.

The conjunction has a Yoneda-flavored reading. The functor $X \mapsto [\Sigma^\bullet G, X]$ sends $\mathcal{T}$ into **graded modules over the graded endomorphism ring** $[\Sigma^\bullet G, G]$ (in the ∞/spectral setting, *modules over the endomorphism ring spectrum* $\mathrm{End}(G)$). Generation makes this functor conservative; compactness makes it preserve coproducts. A conservative coproduct-preserving exact functor between triangulated categories with a generator is an equivalence — which is the structural skeleton of the **Schwede–Shipley** recognition theorem. So "compact weak generator" is precisely the hypothesis under which the representable functor $[G, -]$ implements an equivalence onto a module category, the homotopical descendant of the classical Morita theorem.

---

# Relate to Other Fields / Compression

This is the homotopy-theoretic instance of **Morita theory**. Classically, an abelian category $\mathcal{A}$ with a **compact projective generator** $P$ is equivalent to $\mathbf{Mod}_{\mathrm{End}(P)}$ via $X \mapsto \mathrm{Hom}(P, X)$; the prototype is $P = R$ recovering $\mathcal{A} = \mathbf{Mod}_R$ with $\mathrm{End}(R) = R$. Replacing the abelian category by a triangulated one and the ordinary endomorphism ring by an **endomorphism ring spectrum** gives the present situation: a compact weak generator $G$ presents $\mathcal{T}$ as modules over $\mathrm{End}(G)$. The two notions of "compact projective generator" and "compact weak generator" are the same idea in the abelian and triangulated worlds respectively.

**True name:** the true name of a compact weak generator is "**the one ring(-spectrum) that $\mathcal{T}$ is modules over**." When you find a compact weak generator, you have found the ring whose module category *is* your triangulated category. The operational reflex is: on seeing a candidate generator, do not picture detection abstractly — picture $\mathcal{T} \simeq \mathrm{Mod}\text{-}\mathrm{End}(G)$ and ask what $\mathrm{End}(G)$ is.

A compression worth holding: **compactness is finiteness, generation is faithfulness.** The two axioms are orthogonal — finiteness of $G$ (compact) and visibility of $\mathcal{T}$ from $G$ (generation) — and conflating them is the most common confusion. A large object can generate without being compact (e.g. an infinite coproduct of spheres generates $\mathcal{SH}$ but is not compact); a compact object can fail to generate (e.g. a single suspension of $\mathbb{S}$ in a category with extra summands).

---

# Examples / Corollaries

**Is an instance — $R$ in its derived category $D(R)$.** The free module $R$, viewed as a complex concentrated in degree $0$, is a compact weak generator of the [[Def - Chain Map and Chain Homotopy|derived category]] $D(R)$. Generation: $[\Sigma^n R, X] = H_n(X)$, so all these groups vanishing means $X$ is acyclic, hence $\cong 0$ in $D(R)$. Compactness: $[R, -] = H_0$ commutes with direct sums of complexes. Its endomorphism ring is $\mathrm{End}(R) = R$ with no higher homotopy, so the recognition theorem returns the tautology that $D(R)$ is "modules over $R$" — the Eilenberg–MacLane case where the ring spectrum is an ordinary ring. See [[Ex - R is a compact generator of its derived category]].

**Is an instance — the sphere spectrum $\mathbb{S}$ in $\mathcal{SH}$.** The sphere spectrum is a compact weak generator of the stable homotopy category. Generation: $[\Sigma^n \mathbb{S}, X] = \pi_{-n}(X)$, so all homotopy groups vanishing forces $X \cong 0$. Compactness: $\mathbb{S}$ is a finite spectrum, so a map out of it into a coproduct factors through finitely many summands. Here $\mathrm{End}(\mathbb{S}) = \mathbb{S}$ has *rich* higher homotopy — its homotopy groups are the stable homotopy groups of spheres — so the recognition theorem says $\mathcal{SH}$ is "modules over the sphere spectrum," with $\mathbb{S}$ a genuine ring spectrum, not an ordinary ring. See [[Ex - The sphere spectrum is a compact generator of the stable homotopy category]].

**Is an instance — finitely generated model categories.** When $\mathcal{M}$ is a finitely generated stable model category, the (de)suspensions of the domains of the generating cofibrations assemble into a compact generating *set*, and often a single compact generator. This is the model-category-level hypothesis that *produces* a compact weak generator on $\mathrm{Ho}(\mathcal{M})$, and it is how the abstract definition is met in practice.

**Is NOT an instance — an infinite coproduct $\coprod_n \Sigma^n \mathbb{S}$ in $\mathcal{SH}$.** This object *generates* $\mathcal{SH}$ (it contains every sphere), but it is **not compact**: the identity map of $\coprod_n \Sigma^n \mathbb{S}$ does not factor through any finite sub-coproduct, so $[\,\coprod_n \Sigma^n \mathbb{S}, -\,]$ fails to commute with coproducts. It is a generator that is not a compact generator — the clean witness that the two axioms are independent.

**Is NOT an instance — a non-generating compact object.** In $D(R \times S)$ (modules over a product ring), the object $R$ (extended by zero on the $S$ factor) is compact but does **not** generate: it cannot detect complexes supported on the $S$ factor, so $[\Sigma^n R, X] = 0$ does not force $X = 0$. Compact, but blind to half the category — the witness that compactness without generation is insufficient.

**Calibration check.** Verify that in $D(R)$, $[\Sigma^n R, X] = H_n(X)$, and hence why $R$ generates (an acyclic complex is zero in $D(R)$). Verify that the canonical map $\bigoplus_i [G, X_i] \to [G, \coprod_i X_i]$ is *always* injective (a map landing in finitely many summands is determined by its components), so that compactness is exactly the surjectivity of this map. And state, without looking, the two independent things a compact weak generator must do — "detect nonzero objects" and "see coproducts as direct sums" — if both come immediately, you have the definition.

---

# Unlocked by This

> [!tip] Schwede–Shipley Recognition and Endomorphism Ring Spectra *(from Derived Algebra)*
> **Schwede–Shipley.** A [[Def - Stable Model Category|stable model category]] with a single compact weak generator $G$ is [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalent]] to modules over the **endomorphism ring spectrum** $\mathrm{End}(G)$. This is the deepest payoff of the definition: it classifies one-generator stable homotopy theories as module categories over ring spectra, the homotopical Morita theorem and the foundation of **brave new algebra**.

> [!tip] dg-Categories and Brave New Algebra *(from Derived/Higher Algebra)*
> When the higher homotopy of $\mathrm{End}(G)$ is concentrated enough to be modeled by a **differential graded algebra**, the recognition theorem lands in the world of **dg-categories** and their derived module categories — the linear-over-a-base-field shadow of the spectral story. This is the setting for derived algebraic geometry and noncommutative geometry à la Kontsevich.

> [!tip] Telescope and Smashing Localizations *(from Stable Homotopy Theory)*
> Compact objects control **Bousfield localizations** of $\mathcal{SH}$: a localization is **smashing** exactly when it is generated by compact objects, and the celebrated (now resolved) **telescope conjecture** concerns whether every smashing localization is generated by *finite* (compact) spectra. Compactness is the technical hinge of the entire theory of localizations of triangulated categories.
