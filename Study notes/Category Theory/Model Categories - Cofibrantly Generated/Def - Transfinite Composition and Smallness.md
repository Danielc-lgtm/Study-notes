---
type: definition
subject: model-categories
prereqs:
  - "Def - Limit and Colimit"
  - "Def - Pullback and Pushout"
  - "Def - Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a cocomplete category — it has all small colimits, in particular all the transfinite colimits below. An **ordinal** $\lambda$ is identified with the well-ordered set of all smaller ordinals, so "$\beta < \lambda$" and "$\beta \in \lambda$" mean the same thing, and $\lambda$ may be regarded as a category (a poset, hence a category with one arrow $\beta \to \gamma$ whenever $\beta \leq \gamma$). A **cardinal** $\kappa$ is an ordinal not in bijection with any smaller ordinal. A cardinal $\kappa$ is **regular** if it is not the supremum of fewer than $\kappa$ smaller ordinals — equivalently, a $\kappa$-indexed union of sets each of size $< \kappa$ has size $< \kappa$. We write $\mathrm{cf}(\lambda)$ for the **cofinality** of $\lambda$, the least cardinality of a cofinal subset; $\lambda$ is regular precisely when $\mathrm{cf}(\lambda) = \lambda$. The hom-set is $\mathcal{C}(A,B)$. The full symbol registry is on [[Model Categories — Cofibrantly Generated Model Categories and the Small Object Argument]].

This is a compound page: it defines three interlocking notions — the **$\lambda$-sequence**, its **transfinite composition**, and **smallness of an object relative to a class of maps** — because they are introduced together and none is fully usable without the others. The transfinite composition is the colimit of a $\lambda$-sequence, and smallness is the statement that the hom-functor out of an object commutes with such colimits.

---

# Axiom Motivation

The right way to discover these definitions is to ask what it takes for a transfinite construction to *terminate in a usable way*. We are going to build objects by an infinite process: start with $X_0$, attach something to get $X_1$, attach more to get $X_2$, and keep going — not just through the natural numbers, but through all the ordinals up to some $\lambda$, taking unions ("colimits") at the limit stages. The end product is the colimit $X_\lambda = \mathrm{colim}_{\beta<\lambda} X_\beta$. This is exactly how a CW complex is assembled, and it is exactly how the small object argument factors a map. The whole subject of cofibrant generation rests on it.

So the first thing we need is a precise notion of "an ordinal-indexed chain whose limit stages are colimits." A naive functor $X : \lambda \to \mathcal{C}$ is not enough: it would let the value at a limit ordinal $\gamma$ be anything, disconnected from the earlier stages. We want the value at every limit stage to be *forced* by the earlier values — to be their colimit — because otherwise "transfinite composition" would not compose anything; the limit stages would carry independent data. The condition that pins this down is that $X$ **preserves colimits**, equivalently that for every limit ordinal $\gamma < \lambda$ the natural map $\mathrm{colim}_{\beta<\gamma} X_\beta \to X_\gamma$ is an isomorphism. A functor with this property is a $\lambda$-sequence, and now the chain really is a single tower with no hidden choices at the limits.

Given such a tower, the object we care about is the colimit $\mathrm{colim}_{\beta<\lambda} X_\beta$, and the map we care about is the canonical $X_0 \to \mathrm{colim}_{\beta<\lambda} X_\beta$ from the bottom of the tower to the top. This map is the **transfinite composition** of the tower — the infinite-stage analogue of composing $X_0 \to X_1 \to X_2$ into a single map $X_0 \to X_2$. The name is apt: it is what you get by composing all the maps in the tower at once, including across the limit stages.

Now the crucial question. We will build a map $g : Z \to Y$ as a transfinite composition and then want to test it against a generator $i : A \to B$ by lifting: given a commuting square with $A \to Z$ on top, can we fill in a diagonal? The square's top edge is a map $A \to Z = \mathrm{colim}_\beta Z_\beta$ into the colimit. To solve the lifting problem we built the tower precisely so that *every* such map was handled at some stage — but only if the map $A \to \mathrm{colim}_\beta Z_\beta$ actually *comes from* some bounded stage $A \to Z_\beta$. If instead the map genuinely uses the entire infinite tower — if it "escapes to infinity," touching cofinally many stages and factoring through none — then it was never on any stage's to-do list, and no lift was ever supplied. The construction fails.

The condition that forbids this escape is **smallness**. We demand that the object $A$ be such that every map $A \to \mathrm{colim}_\beta X_\beta$ into a transfinite colimit factors through a bounded stage $X_\beta$, and does so essentially uniquely. Stated functorially, this is the requirement that the hom-functor $\mathcal{C}(A,-)$ **commute with the transfinite colimit**: the canonical map
$$\mathrm{colim}_{\beta<\lambda}\, \mathcal{C}(A, X_\beta) \longrightarrow \mathcal{C}\big(A,\, \mathrm{colim}_{\beta<\lambda} X_\beta\big)$$
is a bijection. Surjectivity says every map $A \to X_\lambda$ factors through some stage (no escape); injectivity says two maps that agree at the top already agree at some stage (no spurious identification at infinity). This is the exact, minimal condition under which a transfinite construction can be probed by $A$.

What goes wrong if we *drop* the commutation condition? Take $A$ to be a set of size $\aleph_0$ and build, in $\mathbf{Set}$, the $\omega$-sequence $X_n = \{0,1,\dots,n\}$ with inclusions; the colimit is $\mathbb{N}$, and the identity-like map $\mathbb{N} \to \mathbb{N}$ (taking $A = \mathbb{N}$) does *not* factor through any finite $X_n$. So $\mathbb{N}$ is not small relative to this $\omega$-sequence — at length $\omega$. The fix is to demand the commutation only for $\lambda$ large enough relative to $|A|$: that is what the cardinal $\kappa$ in the definition does. We ask for the commutation for all regular $\lambda \geq \kappa$, where $\kappa$ is chosen above the "size" of $A$. With $\kappa = \aleph_1$, every map out of a countable set into an $\aleph_1$-colimit *does* factor boundedly, because $\aleph_1$ is regular and the image of a countable set is countable, hence cofinally bounded below $\aleph_1$.

What goes wrong if we drop **regularity** of $\lambda$? Regularity is the condition that a $\lambda$-indexed union of $<\kappa$-small pieces cannot reach the top unless one piece already does. If $\lambda$ is *singular* — say $\lambda = \aleph_\omega$, which is the supremum of the countably many cardinals $\aleph_n$ — then a map out of $A$ can be assembled from cofinally many stages (one fragment from each $\aleph_n$) without factoring through any single stage, exactly because the cofinal sequence is short. Singular $\lambda$ breaks bounded factorization even for small $A$. This is why the definition quantifies only over *regular* $\lambda \geq \kappa$: regularity is precisely what makes "below $\lambda$" closed under the kind of sup that a single map out of $A$ can produce.

The test of a good definition is whether one could invent it from the need. Here the need is "a transfinite construction whose colimit can be probed at finite stages," and the three pieces fall out in order: a tower that is genuinely a tower (the $\lambda$-sequence), the map it composes (transfinite composition), and the property of a probe object that lets the probe see the colimit through its finite stages (smallness, with its cardinal $\kappa$ and regularity hypothesis tuning the construction to the size of the probe).

---

# The Definition

Let $\mathcal{C}$ be a cocomplete category and $\lambda$ an ordinal, regarded as a category.

**$\lambda$-sequence.** A **$\lambda$-sequence** in $\mathcal{C}$ is a colimit-preserving functor $X : \lambda \to \mathcal{C}$, written $X_0 \to X_1 \to \cdots \to X_\beta \to \cdots$. Colimit-preservation means exactly that for every limit ordinal $\gamma < \lambda$ the canonical map $\mathrm{colim}_{\beta<\gamma} X_\beta \to X_\gamma$ is an isomorphism.

**Transfinite composition.** The **transfinite composition** (or **composite**) of the $\lambda$-sequence $X$ is the canonical morphism
$$X_0 \longrightarrow \mathrm{colim}_{\beta<\lambda} X_\beta.$$
If $D$ is a class of morphisms of $\mathcal{C}$, a **transfinite composition of maps of $D$** is the composite of a $\lambda$-sequence (for some ordinal $\lambda$) in which each map $X_\beta \to X_{\beta+1}$ belongs to $D$.

**Smallness.** Let $D$ be a class of morphisms and $\kappa$ a cardinal. An object $A$ of $\mathcal{C}$ is **$\kappa$-small relative to $D$** if for every regular cardinal $\lambda \geq \kappa$ and every $\lambda$-sequence $X$ all of whose maps $X_\beta \to X_{\beta+1}$ lie in $D$, the canonical map of sets
$$\mathrm{colim}_{\beta<\lambda}\, \mathcal{C}(A, X_\beta) \longrightarrow \mathcal{C}\big(A,\, \mathrm{colim}_{\beta<\lambda} X_\beta\big)$$
is a bijection. The object $A$ is **small relative to $D$** if it is $\kappa$-small relative to $D$ for some cardinal $\kappa$, and **small** if it is small relative to the class of all morphisms.

Unwinding the bijection: surjectivity says every map $A \to \mathrm{colim}_\beta X_\beta$ factors as $A \to X_\beta \to \mathrm{colim}_\beta X_\beta$ for some $\beta < \lambda$; injectivity says if two maps $A \to X_\beta$, $A \to X_{\beta'}$ become equal in the colimit, they already become equal at some stage $X_\gamma$ with $\gamma \geq \beta, \beta'$.

---

# Categorical / Structural Definition

Smallness is, in the language of category theory, the statement that the representable functor $\mathcal{C}(A,-) : \mathcal{C} \to \mathbf{Set}$ **preserves the relevant filtered colimits**. A $\lambda$-sequence for $\lambda$ a regular cardinal is a particular kind of $\lambda$-filtered diagram, and "$A$ is $\kappa$-small relative to $D$" is precisely "$\mathcal{C}(A,-)$ sends the transfinite composites of $D$-maps (for regular $\lambda \geq \kappa$) to colimits in $\mathbf{Set}$."

This places smallness inside a standard hierarchy. An object $A$ such that $\mathcal{C}(A,-)$ preserves *all* $\kappa$-filtered colimits is called **$\kappa$-compact** (or $\kappa$-presentable); for $\kappa = \aleph_0$ this is **finitely presentable** or **compact**, the categorical generalization of "finitely presented." Smallness relative to a class $D$ is the weaker, class-relative version: we only require commutation with the colimits that actually arise in the small object argument (transfinite composites of $D$-maps), not with every filtered colimit. The two notions agree in the cases that matter most — in a locally presentable category every object is $\kappa$-compact for some $\kappa$, hence small relative to every class — but the relative version is what the small object argument literally needs, and it occasionally holds when full compactness fails.

The transfinite composition itself is the colimit of a diagram indexed by an ordinal, which is the most basic example of a filtered colimit. The colimit-preservation built into the definition of a $\lambda$-sequence is what makes the indexing category $\lambda$ "fill in its own limit ordinals," so the tower is a genuine filtered diagram rather than an arbitrary collection of objects with maps.

---

# Relate to Other Fields / Compression

Smallness is the categorical descendant of **compactness**. In topology, a space $A$ is compact exactly when every open cover has a finite subcover, and a clean reformulation is that a map from $A$ into a directed union $\bigcup_\beta U_\beta$ of open sets factors through some $U_\beta$ — the image, being compact, cannot be spread across infinitely many stages without sitting inside one. That is verbatim the surjectivity half of smallness, with the directed union of opens replaced by a transfinite colimit of cell attachments. The two are not merely analogous: the proof that compact spaces are small *is* the proof that a compact image meets only finitely many cells.

In algebra the same shape recurs as **finite presentation**. A module $M$ is finitely presented exactly when $\mathrm{Hom}(M,-)$ commutes with filtered colimits of modules; an algebra is finitely presented when maps out of it into a filtered colimit of algebras factor through a stage. Each of these is "$M$ is $\aleph_0$-small," and the unifying statement is that *being defined by finite data* is the same as *being detectable at a finite stage of any approximation*. Smallness is this principle promoted to arbitrary cardinals: an object defined by $<\kappa$ data is detectable at a bounded stage of any $\kappa$-long approximation.

**True name:** the operational form of "small" is *"maps out of it cannot escape to infinity"* — every morphism from $A$ into a transfinite colimit already lives at a bounded stage. When you must show a colimit-built object has a lifting property, this is the form to reach for: produce the lifting problem's data at a finite stage, solve it there, and let the colimit inherit the solution.

---

# Examples / Corollaries

**Is an instance — every set is small in $\mathbf{Set}$.** Let $A$ be a set with $|A| = \mu$ and take $\kappa = \mu^+$ (the successor cardinal). For any regular $\lambda \geq \kappa$ and any $\lambda$-sequence of sets, a function $A \to \mathrm{colim}_\beta X_\beta$ assigns to each of the $\mu < \lambda$ elements of $A$ an element living at some stage; since $\lambda$ is regular and there are fewer than $\lambda$ elements, all of these stages are bounded by some $\beta < \lambda$, so the function factors through $X_\beta$. Hence $A$ is $\mu^+$-small relative to all maps. This is why $\mathbf{Set}$ and, more generally, every presheaf category is "small-object-argument-friendly": all objects are small.

**Is an instance — compact spaces are small in $\mathbf{Top}$.** A compact space $A$ is small relative to the relative cell complexes built from $\{S^{n-1}\hookrightarrow D^n\}$: any continuous $A \to \mathrm{colim}_\beta X_\beta$ has compact image, which meets only finitely many of the cells attached along the tower (each cell is attached to a closed subspace, and a compact set in such a colimit is contained in a finite subcomplex), so it factors through a bounded stage. This is the smallness that makes the [[Thm - The Small Object Argument|small object argument]] run in $\mathbf{Top}$; the domains $S^{n-1}$ of the generators are compact, hence small.

**Is an instance — finitely presented modules in $\mathbf{Mod}_R$.** A finitely presented [[Def - Module|module]] $M$ is $\aleph_0$-small relative to all maps: $\mathrm{Hom}_R(M,-)$ commutes with filtered colimits, which contains the $\omega$-sequences and (with a little more care) the longer regular ones. Free modules on finite sets are the basic examples, and they are the domains of the generating cofibrations of the projective model structure on chain complexes.

**Is NOT an instance — $\mathbb{N}$ is not small at length $\omega$ relative to the inclusions $X_n = \{0,\dots,n\}$.** Take $A = \mathbb{N}$ and the $\omega$-sequence $X_n = \{0,1,\dots,n\}$ in $\mathbf{Set}$ with colimit $\mathbb{N}$. The identity map $\mathbb{N} \to \mathbb{N}$ does not factor through any finite $X_n$, so the surjectivity of the smallness map fails for $\lambda = \omega$. This does *not* contradict the previous example: $\omega$ is below the threshold $\kappa = \aleph_1$ for $A = \mathbb{N}$. Smallness is only required for $\lambda \geq \kappa$, and for regular $\lambda \geq \aleph_1$ the factorization is restored. The non-example pinpoints the role of $\kappa$: smallness is a statement about *large enough* $\lambda$, never about all $\lambda$.

**Is NOT an instance — failure at singular $\lambda$.** Consider $A = \mathbb{N}$ and a $\lambda$-sequence with $\lambda = \aleph_\omega$ arranged so that a map $\mathbb{N} \to \mathrm{colim}$ sends $n$ into the $n$-th cofinal stage $X_{\aleph_n}$. Because $\mathrm{cf}(\aleph_\omega) = \aleph_0$, this map touches a cofinal set of stages and factors through none of them. This is exactly why the definition restricts to *regular* $\lambda$: singular cofinality lets a small object's map escape to infinity through a short cofinal ladder.

**Corollary — smallness is monotone in the class and the cardinal.** If $A$ is $\kappa$-small relative to $D$ and $D' \subseteq D$, then $A$ is $\kappa$-small relative to $D'$ (fewer towers to check); and if $A$ is $\kappa$-small relative to $D$ and $\kappa' \geq \kappa$, then $A$ is $\kappa'$-small relative to $D$ (we check fewer, larger $\lambda$). So smallness, once obtained, is robust under shrinking the class and enlarging the threshold.

**Calibration check.** Verify that the colimit-preservation condition in the definition of a $\lambda$-sequence is automatic at successor ordinals and is a genuine constraint only at limit ordinals. Verify that surjectivity of the smallness map is "no escape to infinity" and injectivity is "no identification at infinity." If you can also explain why the threshold for $A = \mathbb{N}$ is $\aleph_1$ and not $\aleph_0$ — that is, why countable length $\omega$ fails but uncountable regular length succeeds — you have understood the interplay of $|A|$, $\kappa$, and regularity.

---

# Unlocked by This

> [!tip] The Small Object Argument *(from this chapter)*
> Smallness of the domains of a generating set $I$ is exactly the hypothesis that lets the [[Thm - The Small Object Argument|small object argument]] terminate: it guarantees the transfinitely-built map has the right lifting property against $I$, because every lifting problem is detected at a bounded stage.

> [!tip] Locally Presentable and Combinatorial Model Categories *(from Higher Category Theory)*
> A category in which a *set* of small objects generates everything under colimits is **locally presentable**, and a cofibrantly generated model structure on such a category is a **combinatorial model category**. Smallness is the 1-categorical shadow of the $\kappa$-compactness condition defining presentable ∞-categories, the foundational objects of Lurie's higher algebra.

> [!tip] Accessible Functors and the Adjoint Functor Theorem *(from Categorical Logic)*
> Functors preserving $\kappa$-filtered colimits are **accessible**, and the interplay of smallness with accessibility underlies the modern (Gabriel–Ulmer) form of the adjoint functor theorem, which guarantees adjoints exist for colimit-preserving functors between locally presentable categories.
