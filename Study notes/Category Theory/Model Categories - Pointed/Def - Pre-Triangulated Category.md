---
type: definition
subject: model-categories
prereqs:
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Cofiber and Fiber Sequence"
  - "Thm - The Suspension-Loop Adjunction"
  - "Def - Initial and Terminal Object"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{T}$ is a [[Def - Initial and Terminal Object|pointed]] category — a category with a zero object $*$, hence a [[Def - Pointed Model Category Suspension and Loop|zero map]] $0$ between every pair of objects — equipped with an adjoint pair of [[Thm - The Suspension-Loop Adjunction|functors]] $\Sigma \dashv \Omega$, with unit $\eta : \mathrm{id} \to \Omega\Sigma$ and counit $\varepsilon : \Sigma\Omega \to \mathrm{id}$. The motivating instance is $\mathcal{T} = \mathrm{Ho}(\mathcal{C})$ for a pointed model category $\mathcal{C}$, with $\Sigma, \Omega$ the suspension and loop. A **cofiber sequence** is a diagram $X \to Y \to Z \to \Sigma X$; a **fiber sequence** is a diagram $\Omega Z \to X \to Y \to Z$. Objects are $X, Y, Z$, maps $f, g, h$; the connecting map of a sequence is written with a $\partial$ or as the third map. The full symbol registry is on [[Model Categories — Pointed Model Categories and Cofiber Sequences]].

---

# Axiom Motivation

The aim is to write down, as a self-contained list of axioms, exactly the structure that $\mathrm{Ho}(\mathcal{C})$ carries by virtue of the constructions in this chapter — so that one can later reason about "homotopy categories of pointed model categories" without ever returning to the model category. This is the standard move that produced abelian categories from module categories and triangulated categories from derived categories: distill the formal properties, forget the construction. A pre-triangulated category is the distillation for the **pointed, not-yet-stable** case; a [[Def - Cofiber and Fiber Sequence|triangulated category]] (next chapter) is the distillation once suspension is invertible.

Why these specific ingredients? Take them one at a time, asking what breaks if each is dropped.

First, **a zero object**. Without it there is no zero map, and "$Z \to \Sigma X$ extends a sequence in which $f$ becomes null" has no meaning — there is no basepoint in $\mathcal{T}(A, B)$ for an exact sequence of pointed sets to be exact *at*. The zero object is what makes every hom-set pointed, and the entire exactness apparatus is exactness of pointed sets. Drop it and you cannot even state the axioms about exact sequences of $\mathcal{T}(-, Z)$.

Second, **the adjunction $\Sigma \dashv \Omega$, not merely a functor $\Sigma$**. A triangulated category demands $\Sigma$ be an *equivalence*; a pre-triangulated category is weaker — it asks only that $\Sigma$ have a right adjoint $\Omega$. This is the precise extra generality needed to cover homotopy categories that are *not stable*, such as $\mathrm{Ho}(\mathbf{Top}_*)$ itself, where $\Sigma$ is very far from invertible (most spaces are not suspensions, and $\Omega\Sigma X \not\simeq X$ in general — that is the Freudenthal suspension theorem's domain). If you strengthened "adjunction" to "equivalence" you would exclude the main example the theory is built to describe. If you weakened it to "just a functor $\Sigma$ with no $\Omega$," you would lose the fiber sequences entirely and with them the dual long exact sequence; the adjunction is exactly what makes the cofiber and fiber pictures two faces of one structure (this is the content of the agreement theorem).

Third, **two classes of distinguished sequences — cofiber and fiber — rather than one**. In a triangulated category the invertibility of $\Sigma$ lets you convert any fiber sequence into a cofiber sequence (rotate and apply $\Sigma^{\pm 1}$), so a single class of distinguished triangles suffices. Pre-triangulated has no such luxury: with $\Sigma$ non-invertible the cofiber sequences and fiber sequences are genuinely different data, and you must axiomatize both. Drop the fiber sequences and you lose the long exact sequence in $\mathcal{T}(Z, -)$; drop the cofiber sequences and you lose the one in $\mathcal{T}(-, Z)$. The compatibility axioms tie them together: the connecting maps $\partial$ for cofiber and fiber sequences must be related by the unit and counit of $\Sigma \dashv \Omega$, which is precisely the statement that "the two notions agree up to sign" can even be formulated abstractly.

Fourth, the **compatibility (rotation, replacement, and the long-exact-sequence) axioms**. These are the analogues of the triangulated axioms TR1–TR3, adapted to a non-invertible $\Sigma$. Rotation says a cofiber sequence $X \to Y \to Z \to \Sigma X$ stays a cofiber sequence when shifted along, with the loop/suspension correcting the ends; this is what makes the three-term sequence equivalent to the infinite Puppe sequence. Replacement (the analogue of TR1) says every map sits in a cofiber sequence and isomorphic diagrams are simultaneously cofiber sequences; without it the class of distinguished sequences would not be closed under the moves you actually perform. The exactness axiom demands that $\mathcal{T}(-, Z)$ carry cofiber sequences to exact sequences of pointed sets and $\mathcal{T}(Z, -)$ carry fiber sequences to exact sequences — this is the payload, the reason the structure is useful, and it is imposed because it is the property that holds in $\mathrm{Ho}(\mathcal{C})$ and that all applications use. Could a reader invent these? Yes: start from "I want the homotopy category to support long exact sequences computing mapping sets," observe that you need a basepoint (zero object), a shift to make the sequences infinite (suspension), a dual shift for the dual sequences (loop, hence the adjunction), and closure conditions so the bookkeeping is consistent (the compatibility axioms). Each axiom is the minimal hypothesis making one of those four desires true.

The honest caveat, which Hovey stresses, is that the full list of pre-triangulated axioms is *technical* — there are coherence conditions relating the connecting maps to $\eta$ and $\varepsilon$ that are tedious to state and are exactly the conditions verified by the homotopy category. The conceptual content is the four ingredients above; the fine print is bookkeeping ensuring they cohere.

---

# The Definition

A **pre-triangulated category** is a [[Def - Initial and Terminal Object|pointed]] category $\mathcal{T}$ together with:

1. an **adjunction** $\Sigma \dashv \Omega$ of endofunctors $\Sigma, \Omega : \mathcal{T} \to \mathcal{T}$, with unit $\eta : \mathrm{id} \to \Omega\Sigma$ and counit $\varepsilon : \Sigma\Omega \to \mathrm{id}$;
2. a class of **cofiber sequences** $X \xrightarrow{f} Y \xrightarrow{g} Z \xrightarrow{h} \Sigma X$, and a class of **fiber sequences** $\Omega Z \xrightarrow{h} X \xrightarrow{f} Y \xrightarrow{g} Z$, each closed under isomorphism;

satisfying the following axioms (Hovey 6.5):

- **(Existence and naturality.)** For every map $f : X \to Y$ there is a cofiber sequence $X \xrightarrow{f} Y \to Z \to \Sigma X$ and, dually, a fiber sequence $\Omega Z \to F \to X \xrightarrow{f} Y$; the trivial sequence $X \xrightarrow{\mathrm{id}} X \to * \to \Sigma X$ is a cofiber sequence, and dually.
- **(Rotation.)** $X \xrightarrow{f} Y \xrightarrow{g} Z \xrightarrow{h} \Sigma X$ is a cofiber sequence if and only if $Y \xrightarrow{g} Z \xrightarrow{h} \Sigma X \xrightarrow{-\Sigma f} \Sigma Y$ is, and the corresponding statement (with the loop and the unit/counit corrections) holds for fiber sequences.
- **(Compatibility of the classes.)** Cofiber and fiber sequences are matched through the adjunction: a cofiber sequence $X \to Y \to Z \to \Sigma X$ corresponds, under $\Sigma \dashv \Omega$, to a fiber sequence $\Omega Z \to X \to Y \to Z$, with connecting maps related by $\eta$ and $\varepsilon$ (this is the abstract form of the agreement theorem).
- **(Long exact sequences.)** For every object $W$, applying $\mathcal{T}(-, W)$ to a cofiber sequence yields a long exact sequence of pointed sets
$$\cdots \to \mathcal{T}(\Sigma X, W) \to \mathcal{T}(Z, W) \to \mathcal{T}(Y, W) \to \mathcal{T}(X, W),$$
and applying $\mathcal{T}(W, -)$ to a fiber sequence yields a long exact sequence
$$\mathcal{T}(W, \Omega Z) \to \mathcal{T}(W, X) \to \mathcal{T}(W, Y) \to \mathcal{T}(W, Z).$$

The basic theorem of the chapter (Hovey 6.5) is that the homotopy category of any pointed model category is pre-triangulated, with $\Sigma, \Omega$ the suspension and loop and the (co)fiber sequences the Puppe sequences of [[Def - Cofiber and Fiber Sequence]].

---

# Categorical / Structural Definition

The structural essence is: a pre-triangulated category is **an additive-like setting where short maps have been promoted to long exact sequences by a shift functor that is only half-invertible.** Compare three points on a ladder of increasing structure.

A **pointed category** has a zero object, hence zero maps and pointed hom-sets — enough to *speak* of kernels and cokernels but not enough to relate them. A **pre-triangulated category** adds the adjoint shift $\Sigma \dashv \Omega$ and the two families of distinguished sequences, so that every map generates an infinite cofiber sequence (computing maps out, via $\mathcal{T}(-, W)$) and an infinite fiber sequence (computing maps in, via $\mathcal{T}(W, -)$); the shift is one-directional, so cofiber and fiber genuinely differ. A **triangulated category** is the special case in which $\Sigma$ is an *equivalence* (so $\eta, \varepsilon$ are isomorphisms): then $\Omega = \Sigma^{-1}$, the two families collapse into one class of **distinguished triangles** $X \to Y \to Z \to \Sigma X$, and one imposes the additional octahedral axiom TR4. So:
$$\text{pointed category} \;\subset\; \text{pre-triangulated category} \;\xrightarrow{\;\Sigma \text{ invertible}\;}\; \text{triangulated category}.$$

The forgetful direction is also illuminating: forgetting the (co)fiber classes from a pre-triangulated category leaves a pointed category with an adjunction; forgetting that $\Sigma$ is *only* adjoint (assuming it is invertible) and adding TR4 gives triangulated. Pre-triangulated is the precise level at which "$\mathrm{Ho}$ of a pointed model category" lives, and stabilizing the model category (next chapter) is exactly the operation that makes $\Sigma$ invertible and lifts pre-triangulated to triangulated.

---

# Relate to Other Fields / Compression

The closest relative is the **triangulated category** of homological algebra, and the relationship is exactly "drop the invertibility of the shift." A triangulated category — the derived category $D(R)$, the stable homotopy category, the stable module category — has a shift $\Sigma = [1]$ that is an equivalence and one class of distinguished triangles $X \to Y \to Z \to X[1]$ obeying TR1–TR4. A pre-triangulated category keeps everything except invertibility: it has the shift *as a left adjoint*, two classes of sequences instead of one, and no octahedral axiom (the octahedral axiom is most naturally stated when the shift is invertible). This is why Hovey introduces pre-triangulated as the **structure $\mathrm{Ho}(\mathcal{C})$ always has**, and triangulated as the structure it has **when $\mathcal{C}$ is stable**.

**True name:** a pre-triangulated category is the **homotopy category of a pointed model category, axiomatized** — equivalently, "a triangulated category before the shift has been inverted." Operationally, what you reach for is not the axiom list but the two consequences: *every map has a cofiber sequence giving a long exact sequence of maps out, and every map has a fiber sequence giving a long exact sequence of maps in.* If you can state those two long exact sequences and rotate them, you are using the pre-triangulated structure, and you almost never need the coherence fine print.

The other relative is the **abelian category**, and the analogy sharpens the picture. An abelian category turns each short exact sequence $0 \to A \to B \to C \to 0$ into the *data* you compute with, and a [[Def - Cofiber and Fiber Sequence|derived functor]] turns it into a long exact sequence. A (pre-)triangulated category does this in one step: the cofiber sequence *is* the homotopy-correct short exact sequence, and the long exact sequence of $\mathcal{T}(-, W)$ is automatic. So pre-triangulated categories are to homotopy theory what abelian categories are to homological algebra — the abstract home in which "exact sequence" lives — with the crucial difference that the shift functor is built in rather than emergent.

---

# Examples / Corollaries

**Is an instance — $\mathrm{Ho}(\mathbf{Top}_*)$.** The homotopy category of pointed spaces is pre-triangulated: $\Sigma$ is the suspension, $\Omega$ the loop, cofiber sequences are Puppe sequences of cofibrations, fiber sequences are Puppe sequences of fibrations, and the long exact sequences are the long exact sequences of pairs and of fibrations. It is **not** triangulated, because $\Sigma$ is not invertible — $\Omega\Sigma X \not\simeq X$ in general (e.g. for $X = S^0$). This is the canonical example showing pre-triangulated is strictly weaker than triangulated and is exactly the case the extra generality was invented for.

**Is an instance — $\mathrm{Ho}(\mathbf{sSet}_*)$.** Pointed simplicial sets give the same pre-triangulated category as pointed spaces (the two model the same homotopy theory). Again $\Sigma$ is not invertible, so it is pre-triangulated but not triangulated.

**Is an instance — but also triangulated — the derived category $D(R)$.** The homotopy category of the pointed model category $\mathrm{Ch}(R)$ is pre-triangulated with $\Sigma = [1]$ the degree shift. Here $\Sigma$ *is* invertible (shift down by one), so $D(R)$ is moreover triangulated: it is the boundary case where the pre-triangulated structure upgrades. This example shows the inclusion "triangulated $\subset$ pre-triangulated" is real — every triangulated category is pre-triangulated with $\Omega = \Sigma^{-1}$ and a single sequence class.

**Is NOT an instance — an unpointed homotopy category.** $\mathrm{Ho}(\mathbf{Top})$ (unbased) is not pre-triangulated: it has no zero object, so no zero maps, so no pointed hom-sets and no exact sequences. The structure simply cannot be stated. Passing to $\mathrm{Ho}(\mathbf{Top}_*)$ is required.

**Is NOT an instance — a pointed category with $\Sigma$ but no exactness.** Equip a pointed category with an endofunctor $\Sigma$ having a right adjoint $\Omega$ but declare *every* three-term sequence "distinguished." Then $\mathcal{T}(-, W)$ does not send these to exact sequences (there is no reason for image to equal kernel), so the long-exact-sequence axiom fails. Having a shift adjunction is necessary but nowhere near sufficient; the distinguished classes must be the *genuine* (co)fiber sequences for exactness to hold.

**Calibration check.** Verify three things. First, that any triangulated category is pre-triangulated by setting $\Omega = \Sigma^{-1}$, taking the single class of distinguished triangles as both cofiber and fiber sequences, and checking the long exact sequence axiom is the standard one for triangulated categories. Second, that in $\mathrm{Ho}(\mathbf{Top}_*)$ the failure of $\Sigma$ to be invertible blocks the triangulated structure but not the pre-triangulated one. Third, that the rotation axiom turns a three-term cofiber sequence into the infinite Puppe sequence by repeated shifting.

---

# Unlocked by This

> [!tip] Triangulated Category and the Octahedral Axiom *(from the next chapter)*
> When the model category is **stable** — $\Sigma : \mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$ an equivalence — the pre-triangulated structure becomes a **triangulated category**: $\Omega = \Sigma^{-1}$, the cofiber and fiber sequences merge into one class of distinguished triangles, and one gains the octahedral axiom TR4. This is the framework of derived categories, the stable homotopy category, and Verdier's localization. The forward page is **Def - Triangulated Category** in the Stable chapter.

> [!tip] Stable $\infty$-Categories *(from higher category theory)*
> The $\infty$-categorical refinement replaces "homotopy category with extra structure" by a **stable $\infty$-category**, where (co)fiber sequences are not extra data but are detected by the requirement that a square is a pushout iff it is a pullback. Passing to the homotopy category of a stable $\infty$-category recovers a triangulated category; pre-triangulated categories are the model-categorical shadow of this cleaner $\infty$-world.

> [!tip] t-Structures and Hearts *(from derived algebraic geometry)*
> A **t-structure** on a triangulated category carves out an abelian "heart," reconstructing an abelian category from the triangulated one and organizing perverse sheaves and weight filtrations. t-structures presuppose the triangulated (hence pre-triangulated) structure built here, and they are the bridge back from homotopy theory to ordinary homological algebra.
