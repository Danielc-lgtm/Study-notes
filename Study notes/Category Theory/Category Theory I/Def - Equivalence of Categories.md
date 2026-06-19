---
type: definition
subject: category-theory
prereqs:
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Notation

An equivalence is a pair of [[Def - Functor|functors]] $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ together with [[Def - Natural Transformation|natural isomorphisms]] $\eta : 1_{\mathcal{C}} \xRightarrow{\sim} GF$ and $\varepsilon : FG \xRightarrow{\sim} 1_{\mathcal{D}}$. We write $\mathcal{C} \simeq \mathcal{D}$ for "$\mathcal{C}$ and $\mathcal{D}$ are equivalent" and reserve $\mathcal{C} \cong \mathcal{D}$ (isomorphism of categories) for the strictly stronger relation where $GF = 1_{\mathcal{C}}$ and $FG = 1_{\mathcal{D}}$ on the nose. The functor $G$ is a **quasi-inverse** of $F$. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

When should two [[Def - Category|categories]] be regarded as "the same"? The naive answer — isomorphic, meaning there are functors $F, G$ with $GF = 1_{\mathcal{C}}$ and $FG = 1_{\mathcal{D}}$ — is almost never the right one, and seeing why pins down the correct definition. Consider the category $\mathbf{FinVect}_k$ of finite-dimensional [[Def - Vector Space|vector spaces]] and the category $\mathbf{Mat}_k$ whose objects are the natural numbers and whose morphisms $m \to n$ are $n \times m$ matrices over $k$. Every linear-algebra computation is "the same" in these two categories — choosing a basis turns a space into a number and a linear map into a matrix. They ought to count as the same category. But they are *not isomorphic*: $\mathbf{FinVect}_k$ has a proper class of objects (one for every finite-dimensional space, and there are many spaces of each dimension), while $\mathbf{Mat}_k$ has exactly one object per dimension. No bijection of objects exists, so no isomorphism of categories exists.

The lesson is that **isomorphism of categories asks too much: it demands equality of objects, but category theory only ever cares about objects up to isomorphism.** The fix is to relax "equal" to "isomorphic" in exactly the places where equality was demanded. An isomorphism wanted $GF = 1_{\mathcal{C}}$, an equality of functors, which forces $GF(A) = A$ on the nose. We weaken this to $GF \cong 1_{\mathcal{C}}$, a [[Def - Natural Transformation|natural isomorphism]] — so $GF(A)$ need only be *naturally isomorphic* to $A$, not equal. Likewise $FG \cong 1_{\mathcal{D}}$. That single relaxation, from $=$ to $\cong$, is the entire definition of equivalence, and it is forced by the principle that objects are interchangeable with isomorphic objects.

Why must the isomorphisms be *natural*, rather than just a choice of $GF(A) \cong A$ for each $A$? Because an unnatural family of isomorphisms is exactly the kind of basis-dependent, choice-laden comparison that the [[Def - Natural Transformation|double-dual story]] taught us to distrust. Naturality is what guarantees that the comparison $GF \cong 1$ commutes with all morphisms, so that the equivalence respects the categorical structure and not just the objects. **Drop naturality** and you would have functors that are pointwise-invertible-up-to-iso but do not coherently transport morphisms — useless for transferring theorems between the categories. The natural isomorphisms $\eta, \varepsilon$ are the coherence that makes equivalence a working tool.

---

# The Definition

An **equivalence of categories** between $\mathcal{C}$ and $\mathcal{D}$ is a pair of [[Def - Functor|functors]]
$$F : \mathcal{C} \to \mathcal{D}, \qquad G : \mathcal{D} \to \mathcal{C},$$
together with [[Def - Natural Transformation|natural isomorphisms]]
$$\eta : 1_{\mathcal{C}} \xRightarrow{\;\sim\;} GF \qquad \text{and} \qquad \varepsilon : FG \xRightarrow{\;\sim\;} 1_{\mathcal{D}}.$$
When such data exist, $\mathcal{C}$ and $\mathcal{D}$ are **equivalent**, written $\mathcal{C} \simeq \mathcal{D}$, and $G$ is a **quasi-inverse** of $F$. A single functor $F$ is called **an equivalence** if it can be completed to such a quadruple $(F, G, \eta, \varepsilon)$.

This is strictly weaker than an **isomorphism of categories**, which requires $GF = 1_{\mathcal{C}}$ and $FG = 1_{\mathcal{D}}$ as equalities of functors (equivalently, $F$ bijective on objects and on each hom-set). Every isomorphism of categories is an equivalence; the converse fails (e.g. $\mathbf{FinVect}_k \simeq \mathbf{Mat}_k$ but they are not isomorphic).

The fundamental recognition criterion, proved on [[Thm - Characterization of Equivalence]]:
$$F \text{ is an equivalence} \iff F \text{ is full, faithful, and essentially surjective.}$$

---

# Categorical / Structural Definition

Equivalence is the correct notion of "sameness" for objects of the 2-category $\mathbf{Cat}$, and it is precisely **isomorphism in the 2-categorical sense**: two objects of a 2-category are equivalent when there are 1-cells $F, G$ between them whose composites are isomorphic (via 2-cells) to the identities, rather than equal. So "equivalence of categories" is "isomorphism in $\mathbf{Cat}$ read up to 2-cells", exactly as "isomorphism of objects" is "sameness up to morphisms". The pattern is self-similar: each level of the hierarchy compares the level below up to the next level's isomorphisms.

A clean structural restatement uses the **skeleton**. A skeleton $\mathrm{sk}(\mathcal{C})$ is a full [[Def - Subcategory|subcategory]] containing exactly one object from each isomorphism class. Then $\mathcal{C} \simeq \mathcal{D}$ if and only if $\mathrm{sk}(\mathcal{C}) \cong \mathrm{sk}(\mathcal{D})$ — two categories are equivalent precisely when their skeletons are *isomorphic*. This isolates the difference between $\simeq$ and $\cong$ to a single source: equivalence ignores the multiplicity of isomorphic copies of each object, while isomorphism counts them. Passing to a skeleton is "deduplicating isomorphic objects", and equivalence is exactly the relation that survives this deduplication.

---

# Relate to Other Fields / Compression

**True name:** *isomorphism with "equal objects" relaxed to "naturally isomorphic objects"* — operationally, $F$ is an equivalence iff it is [[Def - Full, Faithful, and Essentially Surjective Functor|full, faithful, and essentially surjective]]. In practice one almost never verifies the four-tuple $(F, G, \eta, \varepsilon)$ directly; one checks the three properties of $F$ and invokes [[Thm - Characterization of Equivalence|the characterization]] to manufacture $G$. That theorem is the working definition.

Equivalence is the categorical version of every "the same up to harmless relabelling" statement in mathematics. Two bases of a vector space give "the same" linear algebra; two presentations of a group give "the same" group; two atlases give "the same" manifold. In each case the precise statement is an equivalence of the appropriate categories, and the "harmless relabelling" is the natural isomorphism $\eta$. The slogan: **isomorphism is for objects, equivalence is for categories; both mean "the same", but equivalence forgives the redundancy of isomorphic copies.**

---

# Examples / Corollaries

**Finite-dimensional vector spaces and matrices.** $\mathbf{FinVect}_k \simeq \mathbf{Mat}_k$. The functor $\mathbf{Mat}_k \to \mathbf{FinVect}_k$ sends $n \mapsto k^n$ and a matrix to the corresponding linear map; it is full, faithful (a linear map $k^m \to k^n$ is exactly an $n \times m$ matrix), and essentially surjective (every finite-dimensional space is isomorphic to some $k^n$). It is not an isomorphism because the object-counts differ. This is the cleanest equivalence to keep in mind.

**A category and its skeleton.** Any category $\mathcal{C}$ is equivalent to any skeleton $\mathrm{sk}(\mathcal{C})$ via the inclusion, which is fully faithful (it is a full [[Def - Subcategory|subcategory]]) and essentially surjective (every object is isomorphic to its chosen representative). $\mathbf{Mat}_k$ above is a skeleton of $\mathbf{FinVect}_k$.

**Affine schemes and commutative rings (preview).** The contravariant **Spec** functor (see [[Def - Functor]]) is one half of an equivalence $\mathbf{CRing}^{\mathrm{op}} \simeq \mathbf{AffSch}$, the equivalence on which algebraic geometry is founded. A commutative ring and the affine scheme it defines carry identical information; the equivalence is the precise form of "geometry is dual to algebra".

**Is NOT an equivalence — $\mathbf{Set} \not\simeq \mathbf{Set}^{\mathrm{op}}$.** No equivalence exists between $\mathbf{Set}$ and its [[Def - Opposite Category and Duality|opposite]]. An equivalence preserves all categorical properties, in particular it would have to send the initial object $\emptyset$ (unique map *out* to each set) to an initial object of $\mathbf{Set}^{\mathrm{op}}$, which is a terminal object of $\mathbf{Set}$, a singleton. But $\mathbf{Set}(\emptyset, \emptyset)$ is a singleton while $\mathbf{Set}(1, 1)$ is a singleton too — the obstruction is finer: $\mathbf{Set}(X, \emptyset) = \emptyset$ for $X \neq \emptyset$, whereas dually $\mathbf{Set}(1, X) = X$ is never empty, so the initial/terminal asymmetry cannot be matched. (The §1.2 exercise [[Ex - Set is not equivalent to its opposite|carries this out in full]].) This shows equivalence is a genuine constraint, not automatic.

**Is NOT an isomorphism though an equivalence.** $\mathbf{FinVect}_k \simeq \mathbf{Mat}_k$ is the running witness that $\simeq$ is strictly weaker than $\cong$: equivalent categories can have wildly different numbers of objects.

**Calibration check.** Verify that equivalence is an equivalence relation on categories (reflexive via identities; symmetric by swapping $F, G, \eta, \varepsilon$ appropriately; transitive by composing). Verify that an equivalence preserves [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphisms]], monos, epis, and (later) limits and colimits — it preserves every property expressible in the language of categories. Confirm you can name the three properties of $F$ that characterize an equivalence, and explain why "essentially surjective" rather than "surjective on objects" is what appears.

---

# Unlocked by This

> [!tip] Morita Equivalence *(from Ring and Representation Theory)*
> Two [[Def - Ring|rings]] are **Morita equivalent** when their module categories are equivalent, $\mathbf{Mod}_R \simeq \mathbf{Mod}_S$. This is the right notion of "same representation theory", and it is strictly coarser than ring isomorphism: $R$ and the matrix ring $M_n(R)$ are always Morita equivalent though rarely isomorphic. Equivalence of categories is the engine.

> [!tip] Derived Equivalences and Tilting *(from Homological Algebra and Algebraic Geometry)*
> Equivalences of **derived categories** — equivalences $D^b(\mathcal{A}) \simeq D^b(\mathcal{B})$ between bounded derived categories — encode deep dualities such as Beilinson's resolution, tilting theory, and (conjecturally) homological mirror symmetry. The whole subject of derived equivalence is "equivalence of categories" applied to **triangulated categories**.

> [!tip] Equivalence in Higher Categories *(from Higher Category Theory)*
> In an **∞-category**, equivalence becomes the only sensible notion of sameness at every level, and "equal" is systematically replaced by "equivalent". This is the univalence principle of **homotopy type theory** seen from the categorical side: isomorphic objects are genuinely indistinguishable.
