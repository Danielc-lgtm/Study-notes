---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Adjunction"
  - "Thm - The Homotopy Category of a Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a **pointed** [[Def - Model Category|model category]]: its initial object $\varnothing$ and terminal object $*$ coincide, giving a **zero object** $0$. The [[Thm - The Homotopy Category of a Model Category|homotopy category]] is $\mathrm{Ho}(\mathcal{M})$. On $\mathrm{Ho}(\mathcal{M})$ there is a **suspension** functor $\Sigma$ — the homotopy cofiber of $X \to 0$, equivalently the homotopy pushout of $0 \leftarrow X \to 0$ — with right [[Def - Adjunction|adjoint]] the **loop** functor $\Omega$, the homotopy fiber of $0 \to X$. We write $\Sigma \dashv \Omega$, with unit $\eta \colon \mathrm{id} \to \Omega\Sigma$ and counit $\varepsilon \colon \Sigma\Omega \to \mathrm{id}$. The construction of $\Sigma$, $\Omega$, and the adjunction belongs to the previous chapter on **pointed model categories and cofiber/fiber sequences**; since that chapter is not yet written up, those objects are named in bold here rather than wikilinked. The full registry is on [[Model Categories — Stable Model Categories and Triangulated Categories]].

---

# Axiom Motivation

The definition you are about to meet has *one* clause — "suspension is an equivalence" — so the motivation is not a per-axiom failure analysis but an answer to the question: why is *this one condition* the right dividing line, and what exactly does it buy?

Begin with what the previous chapter gave us. A pointed model category has a zero object, hence a suspension $\Sigma$ and a loop $\Omega$, and on the homotopy category these are adjoint, $\Sigma \dashv \Omega$. In topology these are the reduced suspension and the based loop space, and the adjunction is the classical $[\Sigma X, Y] \cong [X, \Omega Y]$. Crucially this structure is *directional*: $\Sigma$ raises "dimension," $\Omega$ lowers it, and the two are adjoint but **not inverse**. The unit $\eta \colon X \to \Omega \Sigma X$ and counit $\varepsilon \colon \Sigma \Omega X \to X$ are generally not isomorphisms. In spaces this is visible and unavoidable: $\Omega \Sigma X$ is the free loop construction (a James-type object), wildly larger than $X$, and $\Sigma$ is not even essentially surjective — most spaces are not suspensions of anything. You can go up but you cannot reliably come back down.

The desideratum is to identify the regime where you *can* come back down — where suspension is reversible — because that is the regime in which homotopy theory becomes *linear*, and linearity is what makes a homotopy theory computable in the way ordinary homological algebra is computable. The single cleanest way to demand reversibility is to require that $\Sigma$ be an **equivalence of categories** on $\mathrm{Ho}(\mathcal{M})$. This is the definition of **stable**. The reason this is the *right* condition, and not some nearby variant, is that it is simultaneously the weakest condition that makes everything work and the strongest that any natural example satisfies.

Consider weakening it. One might ask only that $\Sigma$ be *fully faithful* (the unit $\eta$ an isomorphism, so no information is lost on suspending) without requiring essential surjectivity (every object is a suspension). But then there are objects that cannot be desuspended, and the cofiber sequence $X \to Y \to Cf \to \Sigma X$ cannot be rotated backwards into a fiber sequence — you would have a pre-triangulated category that is still not triangulated. The famous concrete witness is **connective spectra**, or pointed spaces themselves: $\Sigma$ is "half-invertible" but objects in low degrees obstruct full inversion. So fully-faithful-but-not-essentially-surjective is too weak; it is precisely the gap between pre-triangulated and triangulated.

Consider strengthening it. One might demand that $\Sigma$ be the *identity*, or that the model category be enriched in chain complexes from the start. That is far too strong: it would exclude the stable homotopy category $\mathcal{SH}$ (where $\Sigma$ is a nontrivial autoequivalence) and the stable module category. The whole content of the subject is that "$\Sigma$ is *an* equivalence" — possibly a highly nontrivial one — already forces all the structure, without demanding that the equivalence be trivial. Naturality also forbids strengthening: $\Sigma$ is determined by the model structure, so we are not free to legislate what it equals, only whether it is invertible.

Here is the test that this condition could be *invented*: suppose you wanted the cofiber sequence and the fiber sequence of a map to be the same sequence, so that "crush the source" and "take the homotopy fiber" agree. Cofiber sequences are built from $\Sigma$; fiber sequences from $\Omega$. They agree exactly when $\Sigma$ and $\Omega$ are mutually inverse, i.e. exactly when $\Sigma$ is an equivalence. So a reader who decided "I want fibers and cofibers to coincide" would arrive *unavoidably* at the stability condition. Likewise, a reader who wanted $[X, Y]$ to be an abelian group rather than a pointed set would discover that this is automatic once every object is a double loop object $X \cong \Omega^2\Sigma^2 X$, which again is exactly invertibility of $\Sigma$ (via the Eckmann–Hilton argument). The definition is the common cause of every good property of the stable world.

---

# The Definition

A **stable model category** is a pointed [[Def - Model Category|model category]] $\mathcal{M}$ in which the suspension functor
$$\Sigma \colon \mathrm{Ho}(\mathcal{M}) \longrightarrow \mathrm{Ho}(\mathcal{M})$$
is an **equivalence of categories**.

Equivalent formulations (each "if and only if"):

1. **The adjunction is an adjoint equivalence.** The unit $\eta \colon \mathrm{id} \to \Omega\Sigma$ and counit $\varepsilon \colon \Sigma\Omega \to \mathrm{id}$ of $\Sigma \dashv \Omega$ on $\mathrm{Ho}(\mathcal{M})$ are natural isomorphisms; equivalently $\Omega$ is an inverse equivalence to $\Sigma$.

2. **Loop is also an equivalence.** $\Omega \colon \mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathcal{M})$ is an equivalence (since a right adjoint to an equivalence is an equivalence and inverse to it).

3. **Cofiber sequences are fiber sequences.** Every cofiber sequence is, up to the natural isomorphism $\Sigma \cong \Omega^{-1}$, a fiber sequence; the two notions coincide.

4. **Every object is infinitely desuspendable.** For every $X$ and every $n \geq 0$ there is an object $Y$ with $\Sigma^n Y \cong X$ in $\mathrm{Ho}(\mathcal{M})$, naturally.

These are properties of the *homotopy category*, so stability is a **property** of a pointed model category, not extra structure on it.

---

# Categorical / Structural Definition

The structural content is best phrased through the **pre-triangulated category** of the previous chapter. The homotopy category of any pointed model category carries: a zero object; the adjoint pair $\Sigma \dashv \Omega$; a class of cofiber sequences and a class of fiber sequences, compatibly linked by connecting maps. This package is a **pre-triangulated category** — it has all the data of a triangulated category *except* that $\Sigma$ may fail to be invertible. (Both "pre-triangulated category" and the suspension/loop apparatus live in the not-yet-written previous chapter, so they are bold here.)

In this language, **stable** is the single condition that promotes pre-triangulated to triangulated: $\mathcal{M}$ is stable $\iff$ the pre-triangulated $\mathrm{Ho}(\mathcal{M})$ has invertible $\Sigma$ $\iff$ $\mathrm{Ho}(\mathcal{M})$ is [[Def - Triangulated Category|triangulated]]. This is precisely the content of the [[Thm - Characterization of Stable Model Categories|characterization theorem]]. The structural slogan: a stable model category is a *presentation, by a model structure, of a triangulated homotopy category* — and, one level up, of a **stable ∞-category**, which is the structure $\mathcal{M}$ is really a model for.

Note the parallel with the unstable situation. Just as an ordinary [[Def - Model Category|model category]] is a presentation of an (∞,1)-category and the [[Thm - The Homotopy Category of a Model Category|homotopy category]] is its $1$-categorical shadow, a *stable* model category is a presentation of a stable ∞-category and the *triangulated* homotopy category is its $1$-categorical shadow. Stability is the homotopy-invariant condition that survives to, and is detected on, the homotopy category.

---

# Relate to Other Fields / Compression

Stability is the homotopy-theoretic instance of a pattern visible throughout mathematics: **the linearization that comes from making an operation invertible.** Inverting multiplication turns a monoid into a group; inverting suspension turns a pointed homotopy theory into a stable, additive, triangulated one. In each case the inversion forces commutativity-like rigidity — abelian groups from group completion, abelian-group-valued hom-functors from suspension inversion (Eckmann–Hilton). The phrase "stable" is borrowed from the Freudenthal suspension theorem: the homotopy groups $\pi_{n+k}(\Sigma^k X)$ *stabilize* (become independent of $k$) for large $k$, and the stable model category is the home of those stable phenomena.

**True name:** the true name of stability is "**$\Sigma$ is invertible**." The official definition — $\Sigma$ is an equivalence — and the operational reflex are the same here, which is unusual and worth noting: when you see "stable," you should literally apply $\Sigma^{\pm n}$ freely and identify cofibers with fibers, because that is the entire content. There is no gap between definition and use.

A second compression: stability is to pointed model categories as *invertibility of the shift* is to additive categories. A pointed model category always has a suspension; stability is the extra condition that the suspension can be undone, exactly as an additive category always has a candidate shift in mind but is triangulated only when that shift is an automorphism.

---

# Examples / Corollaries

**Is an instance — chain complexes, giving $D(R)$.** The category $\mathbf{Ch}(R)$ of [[Def - Chain Map and Chain Homotopy|chain complexes]] of $R$-[[Def - Module|modules]], with quasi-isomorphisms as weak equivalences, is a pointed model category whose suspension is the degree shift $\Sigma X = X[1]$, $X[1]_n = X_{n-1}$. The shift is invertible on $\mathrm{Ho}(\mathbf{Ch}(R)) = D(R)$ — its inverse is $X[-1]$ — so $\mathbf{Ch}(R)$ is **stable**, and $D(R)$ is triangulated. This is the algebraic prototype; see [[Ex - Chain complexes form a stable model category]].

**Is an instance — spectra.** The model category of **spectra** is *constructed* so that suspension is invertible: a spectrum is a sequence of pointed spaces $\{E_n\}$ with maps $\Sigma E_n \to E_{n+1}$, and the homotopy theory is rigged so that $\Sigma$ becomes an equivalence. It is the universal stable model category receiving a functor from pointed spaces — stabilization is exactly the operation that turns the non-stable pointed spaces into the stable spectra. Its homotopy category is $\mathcal{SH}$.

**Is an instance — the stable module category.** Over a self-injective (e.g. group-algebra $kG$) ring $\Lambda$, there is a model structure on $\mathbf{Mod}_\Lambda$ whose homotopy category is the stable module category $\underline{\mathbf{Mod}}_\Lambda$ (maps modulo those factoring through projectives), and there suspension is the cosyzygy $\Omega^{-1}$, which is invertible because projectives and injectives coincide. This is stable, and it is the running example of a stable model category that is neither chain complexes nor spectra.

**Is NOT an instance — pointed topological spaces.** Pointed [[Def - Topological Space|spaces]] form a pointed model category with a perfectly good suspension ($\Sigma S^n = S^{n+1}$) and loop functor, but $\Sigma$ is **not** an equivalence: it is not essentially surjective (most spaces are not suspensions), and the unit $X \to \Omega\Sigma X$ is far from an isomorphism. So pointed spaces are pre-triangulated but **not stable** and their homotopy category is **not triangulated**. This is the canonical non-example; stabilizing it produces spectra. See [[Ex - A pointed model category that is not stable]].

**Is NOT an instance — an unpointed model category.** A model category without a zero object — plain [[Def - Topological Space|topological]] spaces, or simplicial sets — has *no* suspension functor to begin with (there is no object to crush to), so the question of stability does not even arise. Pointedness is a prerequisite: you must have a zero object before you can ask whether $\Sigma$ is invertible.

**Calibration check.** Verify that stability is invariant under [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] (a Quillen equivalence induces an equivalence of homotopy categories commuting with $\Sigma$, so it preserves invertibility of $\Sigma$). Verify that if $\mathcal{M}$ is stable then so is $\mathcal{M}^{op}$ (the suspension of $\mathcal{M}^{op}$ is the loop of $\mathcal{M}$, also an equivalence). And state, without looking, why pointed spaces fail to be stable — if "$\Sigma$ is not essentially surjective; most spaces are not suspensions" comes immediately, you have the definition.

---

# Unlocked by This

> [!tip] Stable ∞-Category *(from Higher Category Theory)*
> A **stable ∞-category** is the structure a stable model category presents: an ∞-category with a zero object in which suspension is invertible, equivalently in which finite limits and finite colimits coincide. Its homotopy category is triangulated, but it remembers the *coherence data* — the actual cones and the higher homotopies witnessing their universal properties — that the triangulated homotopy category discards. This is why the cone is functorial in a stable ∞-category and not in a triangulated category, and it is the modern home of the entire subject (Lurie).

> [!tip] The Stable Homotopy Category and Brown Representability *(from Algebraic Topology)*
> Stabilizing pointed spaces produces **spectra** and the stable homotopy category $\mathcal{SH}$, the universal stable model category built from spaces. Every **generalized cohomology theory** is represented by a spectrum, by **Brown representability**, and the cofiber sequences (now also fiber sequences, by stability) induce the long exact sequences of the cohomology theory. This is the gateway from the abstract definition to the working machinery of algebraic topology.

> [!tip] Schwede–Shipley Recognition *(from Derived Algebra)*
> Among stable model categories, those generated by a single compact object are exactly "modules over a ring spectrum." This is the homotopical Morita theorem; it makes stable model categories the natural setting for **brave new algebra** and **dg-categories**, where ordinary rings are replaced by ring spectra and chain-complex-enriched categories. See [[Def - Compact Weak Generator]].
