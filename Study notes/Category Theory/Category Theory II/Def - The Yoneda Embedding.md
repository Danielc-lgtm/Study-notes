---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Presheaf"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a locally small category and $[\mathcal{C}^{op}, \mathbf{Set}]$ its [[Def - Presheaf|presheaf category]]. The **Yoneda embedding** is denoted $\mathbf{y}$ (some texts use よ, the hiragana for the first syllable of Yoneda, or $\sharp$); we write $\mathbf{y}A = \mathcal{C}(-, A)$ for the representable presheaf of $A$. Objects $A, B, X$; morphism $f : A \to B$. The full registry is on [[Category Theory II — Universal Properties, Representability, and the Yoneda Lemma]].

---

# Axiom Motivation

We have two hom-functors attached to each object: the covariant $\mathcal{C}(A, -)$ and the contravariant $\mathcal{C}(-, A)$ (see [[Def - Hom-Functor and Representable Functor]]). The first asks "how does $A$ see the category, looking out?"; the second asks "how is $A$ seen, looking in?". The Yoneda embedding is the observation that the *second* assignment, $A \mapsto \mathcal{C}(-, A)$, is itself a functor — and an extraordinarily faithful one, faithful enough to embed $\mathcal{C}$ entirely inside the world of presheaves.

To see that it is a functor we must check that a morphism $f : A \to B$ induces a morphism of presheaves $\mathcal{C}(-, A) \Rightarrow \mathcal{C}(-, B)$, naturally and respecting composition. The induced morphism is *post*composition: at each test object $X$, send an arrow $g : X \to A$ to $f \circ g : X \to B$. Call this $f_* = \mathcal{C}(-, f)$. It is a natural transformation because postcomposition by $f$ commutes with precomposition by any $h : X' \to X$ — that commutation is just associativity, $f \circ (g \circ h) = (f \circ g) \circ h$. And $(g \circ f)_* = g_* \circ f_*$ holds for the same reason. So $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$, $A \mapsto \mathcal{C}(-, A)$, $f \mapsto f_*$, is a genuine covariant functor. (It is covariant — not contravariant — even though each $\mathcal{C}(-, A)$ is contravariant *in $X$*; the variance in $X$ and the variance in $A$ are separate slots of the hom-bifunctor.)

Why is this the construction worth singling out, rather than, say, $A \mapsto \mathcal{C}(A, -)$? Both are functors. But the contravariant hom-functor $\mathcal{C}(-, A)$ is a *presheaf*, so $\mathbf{y}$ lands in the presheaf category — the free cocompletion, the universe with all colimits — and the [[Thm - The Yoneda Lemma|Yoneda lemma]] will show $\mathbf{y}$ is *full and faithful* (see [[Thm - The Yoneda Embedding is Fully Faithful]]). That is the payoff that motivates fixing this exact construction: it realizes the chapter's slogan as a theorem. An object is determined by the network of arrows into it, because $\mathbf{y}$ is injective on objects-up-to-isomorphism and bijective on morphisms. The covariant assignment $A \mapsto \mathcal{C}(A, -)$ is equally good but contravariant (it is a functor $\mathcal{C}^{op} \to [\mathcal{C}, \mathbf{Set}]$), and one usually fixes the contravariant-presheaf convention so that "embedding into presheaves" is the headline.

---

# The Definition

Let $\mathcal{C}$ be a locally small category.

The **(covariant) Yoneda embedding** is the functor
$$\mathbf{y} : \mathcal{C} \longrightarrow [\mathcal{C}^{op}, \mathbf{Set}]$$
defined on objects by $\mathbf{y}A = \mathcal{C}(-, A)$ (the [[Def - Hom-Functor and Representable Functor|representable presheaf]] of $A$) and on a morphism $f : A \to B$ by the natural transformation
$$\mathbf{y}f = f_* = \mathcal{C}(-, f) : \mathcal{C}(-, A) \Rightarrow \mathcal{C}(-, B), \qquad (\mathbf{y}f)_X : g \mapsto f \circ g.$$

Dually, the **contravariant Yoneda embedding** is the functor
$$\mathbf{y}' : \mathcal{C}^{op} \longrightarrow [\mathcal{C}, \mathbf{Set}], \qquad A \mapsto \mathcal{C}(A, -),$$
sending $f : A \to B$ to the precomposition transformation $f^* : \mathcal{C}(B, -) \Rightarrow \mathcal{C}(A, -)$.

The two are the two slots of the single hom-bifunctor $\mathcal{C}(-, -) : \mathcal{C}^{op} \times \mathcal{C} \to \mathbf{Set}$. The fundamental property — proved in [[Thm - The Yoneda Embedding is Fully Faithful]] using the [[Thm - The Yoneda Lemma|Yoneda lemma]] — is that **$\mathbf{y}$ is full and faithful**, so it identifies $\mathcal{C}$ with the full subcategory of $[\mathcal{C}^{op}, \mathbf{Set}]$ on the representable presheaves.

---

# Categorical / Structural Definition

The Yoneda embedding is the *curried* form of the hom-bifunctor. Recall that a functor of two variables $\mathcal{C}^{op} \times \mathcal{C} \to \mathbf{Set}$ can be curried into a functor $\mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$, fixing the second variable and letting it become the index of the target functor category. Currying $\mathcal{C}(-, -)$ in its second variable produces exactly $\mathbf{y}$. This is the structural reason $\mathbf{y}$ is automatically functorial and natural: it inherits everything from the bifunctoriality of $\mathrm{Hom}$.

Structurally, $\mathbf{y}$ is characterized by a universal property of its own: $[\mathcal{C}^{op}, \mathbf{Set}]$ is the **free cocompletion** of $\mathcal{C}$, and $\mathbf{y}$ is the universal functor from $\mathcal{C}$ into a cocomplete category. Any functor $\mathcal{C} \to \mathcal{E}$ into a cocomplete category extends, essentially uniquely, to a colimit-preserving functor $[\mathcal{C}^{op}, \mathbf{Set}] \to \mathcal{E}$ along $\mathbf{y}$. This is the precise sense in which "presheaves are colimits of representables" and $\mathbf{y}$ is the inclusion of the generators.

---

# Relate to Other Fields / Compression

The Yoneda embedding is the rigorous form of the maxim *an object is its functor of relationships*. It says: replace $A$ by the presheaf $\mathcal{C}(-, A)$ that records all probes into $A$, and you lose nothing — neither objects (up to iso) nor morphisms. Every theorem that holds about presheaves can be specialized back to objects of $\mathcal{C}$, and the embedding is the bridge.

In algebraic geometry this is not a metaphor but the literal definition of the subject's objects: **Spec** is the (contravariant) Yoneda embedding $\mathbf{CRing}^{op} \to [\mathbf{CRing}, \mathbf{Set}]$, sending a ring $R$ to the affine scheme it represents, and the category of **affine schemes** is by definition the image of this embedding, so $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$. See [[Thm - The Yoneda Embedding is Fully Faithful]] and [[Ex - A scheme is determined by its functor of points]].

**True name:** the Yoneda embedding is *"send an object to all the ways of mapping into it"*. The trigger-reaction: whenever you want to prove two objects are isomorphic, or compute the morphisms between them, or show a construction is canonical, the move is to apply $\mathbf{y}$ and reason about the representable presheaves instead — the Yoneda lemma then turns natural transformations into elements and morphisms into hom-set bijections.

---

# Examples / Corollaries

**Is an instance — Cayley's theorem.** For a group $G$ regarded as a one-object category $BG$, the Yoneda embedding sends the unique object to the right $G$-set $G$ (with right-multiplication action), and embeds $G$ into the automorphisms of that $G$-set, hence into the symmetric group on the underlying set $G$. This is exactly **Cayley's theorem** — every group is a subgroup of a permutation group — recovered as a special case of Yoneda. Worked at [[Ex - Yoneda generalizes Cayley's theorem]].

**Is an instance — Spec in algebraic geometry.** The contravariant Yoneda embedding $\mathbf{CRing}^{op} \to [\mathbf{CRing}, \mathbf{Set}]$ sends a commutative ring $R$ to the functor $\mathrm{Spec}(R) : S \mapsto \mathbf{CRing}(R, S)$, the functor of points of the affine scheme. Full faithfulness of $\mathbf{y}$ is the statement that a morphism of affine schemes $\mathrm{Spec}(R) \to \mathrm{Spec}(S)$ is the same as a ring homomorphism $S \to R$ — the ring-geometry dictionary.

**Is an instance — the embedding of $\Delta$ into simplicial sets.** The simplex category $\Delta$ embeds into simplicial sets via $\mathbf{y}$, sending $[n]$ to the **standard $n$-simplex** $\Delta^n = \Delta(-, [n])$. The Yoneda lemma here says an $n$-simplex of a simplicial set $X$ is the same as a map $\Delta^n \to X$, the engine of all simplicial reasoning.

**Is NOT an instance — a non-full functor.** A functor can be injective on objects without being a Yoneda embedding: the inclusion of a non-full subcategory is injective on objects but typically not full. The defining feature of $\mathbf{y}$ is *fullness* — it sees *every* natural transformation between representables as a morphism of $\mathcal{C}$ — and that is exactly what fails for a generic injective-on-objects functor. The point of [[Thm - The Yoneda Embedding is Fully Faithful]] is that $\mathbf{y}$ never fails this.

**Calibration check.** Verify that $\mathbf{y}$ sends $1_A$ to the identity transformation of $\mathcal{C}(-, A)$ and a composite $g \circ f$ to $(g \circ f)_* = g_* \circ f_*$. Confirm that the component of $\mathbf{y}f$ at the object $A$ itself, $(\mathbf{y}f)_A : \mathcal{C}(A, A) \to \mathcal{C}(A, B)$, sends $1_A \mapsto f$ — this single fact is the seed of the proof that $\mathbf{y}$ is fully faithful.

---

# Unlocked by This

> [!tip] The Yoneda Lemma and Full Faithfulness *(from this chapter)*
> The [[Thm - The Yoneda Lemma|Yoneda lemma]] computes natural transformations out of $\mathbf{y}A$, and as a corollary shows $\mathbf{y}$ is [[Thm - The Yoneda Embedding is Fully Faithful|fully faithful]]: $\mathcal{C}(A, B) \cong \mathrm{Nat}(\mathcal{C}(-, A), \mathcal{C}(-, B))$.

> [!tip] AffSch ≃ CRing^op and the Functor of Points *(from Algebraic Geometry)*
> **Spec** is the Yoneda embedding for $\mathbf{CRing}$. The equivalence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$ is full faithfulness of $\mathbf{y}$ specialized to rings, and it is the statement that affine geometry *is* commutative algebra read backwards.

> [!tip] Enriched and ∞-categorical Yoneda *(from Higher Category Theory)*
> Yoneda generalizes to **enriched categories** (the enriched Yoneda lemma, with hom-objects in a monoidal base) and to **quasi-categories** / $\infty$-categories (Lurie's $\infty$-categorical Yoneda), where it remains the central structural theorem and underwrites the theory of presentable and accessible $\infty$-categories.
