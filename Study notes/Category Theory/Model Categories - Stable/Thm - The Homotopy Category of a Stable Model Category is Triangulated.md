---
type: theorem
subject: model-categories
prereqs:
  - "Def - Stable Model Category"
  - "Def - Triangulated Category"
  - "Thm - The Homotopy Category of a Model Category"
  - "Def - Cofibrant and Fibrant Objects"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$\mathcal{M}$ is a [[Def - Stable Model Category|stable model category]] — a pointed [[Def - Model Category|model category]] whose suspension $\Sigma$ is an equivalence on $\mathrm{Ho}(\mathcal{M})$. Write $0$ for the zero object, $\Sigma$ and $\Omega$ for suspension and loop (mutually inverse equivalences, by stability), and $[X, Y] = \mathrm{Ho}(\mathcal{M})(X, Y)$. For a map $f \colon X \to Y$, the **homotopy cofiber** $Cf$ is the homotopy pushout of $0 \leftarrow X \xrightarrow{f} Y$; the **cofiber sequence** of $f$ is $X \xrightarrow{f} Y \to Cf \to \Sigma X$. The cofiber sequence and the connecting map come from the previous chapter on **pointed model categories and cofiber/fiber sequences** (named in bold, not yet written up). The full registry is on [[Model Categories — Stable Model Categories and Triangulated Categories]].

---

# Statement

> **Theorem (Homotopy category of a stable model category).** Let $\mathcal{M}$ be a [[Def - Stable Model Category|stable model category]]. Then the homotopy category $\mathrm{Ho}(\mathcal{M})$ is a [[Def - Triangulated Category|triangulated category]], with:
> - **shift** the suspension equivalence $\Sigma$ (its inverse $\Sigma^{-1} = \Omega$ exists by stability), and
> - **distinguished triangles** exactly the diagrams isomorphic in $\mathrm{Ho}(\mathcal{M})$ to a **cofiber sequence** $X \xrightarrow{f} Y \to Cf \to \Sigma X$.
>
> In particular the hom-sets $[X, Y]$ are abelian groups with bilinear composition (so $\mathrm{Ho}(\mathcal{M})$ is additive), and for every object $W$ and every distinguished triangle, $\mathrm{Hom}_{\mathrm{Ho}(\mathcal{M})}(W, -)$ and $\mathrm{Hom}_{\mathrm{Ho}(\mathcal{M})}(-, W)$ yield long exact sequences of abelian groups.

---

# Motivation

This theorem is the reason triangulated categories exist in nature rather than only on paper. Verdier wrote down the axioms TR1–TR4 abstractly, but the question that makes them worth caring about is: *where do triangulated categories come from?* The answer this theorem gives is that they come from **stable model categories** — and since the [[Def - Chain Map and Chain Homotopy|derived category]], the stable homotopy category, and the stable module category are all homotopy categories of stable model categories, this single theorem manufactures essentially every triangulated category one meets.

The deeper role is conceptual unification. Before this theorem, the long exact sequence of homology (in algebra), the long exact sequence of a cofiber sequence (in topology), and the octahedral diagrams (in algebraic geometry) looked like three separate pieces of machinery, each proved by hand in its own setting. The theorem says they are one phenomenon: each is the long exact sequence of a distinguished triangle, and the triangles are cofiber sequences in a stable model category. It tells you that you never have to re-prove the formal properties of long exact sequences — you prove them once, from the model-category axioms, and they hold everywhere.

It also draws the line that the previous chapter could not. The homotopy category of *any* pointed model category is **pre-triangulated** — it has cofiber and fiber sequences — but it is triangulated only when the model category is stable. This theorem is the "stable $\Rightarrow$ triangulated" half; its converse-flavored companion, the [[Thm - Characterization of Stable Model Categories|characterization theorem]], shows stability is also necessary.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathcal{M}$ is a stable model category." The skill is recognizing, in a problem that never says the word "stable," that this hypothesis is met.

The first disguised source is **a category of chain complexes, or anything quasi-isomorphism-localized**. Whenever you are handed $\mathbf{Ch}(R)$, or complexes of sheaves, or any setting where you "invert quasi-isomorphisms," you are in a stable model category, because the degree shift of complexes is a visibly invertible suspension. The bridge $B \to A$ is "shift of complexes $=$ invertible $\Sigma$." *Example problem:* given a short exact sequence of complexes, produce its long exact sequence of homology — recognize that you are in $D(R)$, the short exact sequence gives a triangle, and the theorem's long exact sequence is the homology sequence.

The second disguised source is **a category built to invert suspension** — spectra, or any stabilization. If the construction's *purpose* was to make $\Sigma$ invertible, stability is automatic and the theorem applies. The bridge is "stabilization $\Rightarrow$ $\Sigma$ equivalence by construction." *Example problem:* show the cofiber sequence of a map of spectra induces a long exact sequence of stable homotopy groups — recognize $\mathcal{SH}$ is stable, the cofiber sequence is a triangle, and apply $\pi_* = [\mathbb{S}, -]$.

The third disguised source is **a Quillen equivalence to a known stable model category**. Stability and triangulation are homotopy-invariant, so any model category [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalent]] to a stable one is itself stable with the *same* triangulated homotopy category. The bridge is "Quillen equivalence transports stability." *Example problem:* a new model of spectra (symmetric spectra, orthogonal spectra) is Quillen equivalent to the classical one, so its homotopy category is triangulated and equivalent to $\mathcal{SH}$ without re-checking TR1–TR4.

**Targets (Output Amplification)**

The bare conclusion is "$\mathrm{Ho}(\mathcal{M})$ is triangulated." Combined with other inputs it does much more.

Combine the conclusion with **a (co)homology or hom functor**. The triangulated structure, plus any homological functor $H \colon \mathrm{Ho}(\mathcal{M}) \to \mathbf{Ab}$, immediately yields a long exact sequence for every cofiber sequence. The further result $E$ is computational: vanishing and isomorphism statements about $H$ follow by sandwiching in the long exact sequence. This is nonobvious because the theorem itself says nothing about $H$ — the amplification is that *any* hom-out-of-$W$ functor is automatically homological once the category is triangulated.

Combine the conclusion with **a compact generator**. Triangulated $+$ a [[Def - Compact Weak Generator|compact weak generator]] feeds directly into the **Schwede–Shipley** recognition theorem, whose conclusion is that $\mathcal{M}$ presents modules over a ring spectrum. The further result is an *identification* of the entire homotopy theory as algebra. This combination is the engine of the chapter's vista, and it is nonobvious because it converts a structural statement (triangulated) into a concrete one (modules over $\mathrm{End}(G)$).

Combine the conclusion with **a t-structure**. Triangulated $+$ a t-structure yields an abelian **heart** sitting inside $\mathrm{Ho}(\mathcal{M})$, with the triangulated category glued from it. The further result $E$ is that ordinary homological algebra (the heart) and the derived/stable phenomena (the triangles) coexist in one category, which is how $\mathbf{Mod}_R$ is recovered inside $D(R)$. Nonobvious because it exhibits the *source* abelian category as a substructure of its own derived category.

---

# Why Is It True

The theorem feels inevitable once you see that **stability collapses three a priori different sequences into one**. Picture a map $f \colon X \to Y$. Unstably it generates two different infinite sequences: the *cofiber* (Puppe) sequence going *up* in degree, $X \to Y \to Cf \to \Sigma X \to \Sigma Y \to \cdots$, built by repeatedly crushing; and the *fiber* sequence going *down*, $\cdots \to \Omega Y \to Ff \to X \to Y$, built by repeatedly taking homotopy fibers. In a pointed model category these are genuinely distinct and neither is reversible. Stability says $\Sigma$ and $\Omega$ are inverse, so "going up by $\Sigma$" and "going down by $\Omega^{-1}$" are the same move: the cofiber sequence and the fiber sequence become *one bi-infinite sequence* that you can read in either direction. A bi-infinite sequence of maps, where each consecutive pair has the next as its cofiber, is precisely a (rotatable) distinguished triangle.

Now the axioms. **TR1** is just "every map has a homotopy cofiber" (it does, by factoring and taking a homotopy pushout) plus "the cofiber of an identity is $0$" (crushing $X$ inside $X$ leaves nothing). **TR2 (rotation)** is the Puppe phenomenon: the cofiber of $Y \to Cf$ is $\Sigma X$, so rotating the triangle one click gives another cofiber sequence — the sign $-\Sigma f$ is the bookkeeping of how the suspension coordinate flips. **TR3** is the functoriality-up-to-homotopy of the homotopy pushout: a commuting square on $(X, Y)$ induces a map on pushouts, hence on cofibers. **TR4 (octahedron)** is the **pasting law for homotopy pushouts**: the cofiber of a composite $g \circ f$ is built by pasting the cofiber square of $f$ to that of $g$, and the octahedron is exactly the diagram recording this pasting.

The additive structure is the one genuinely non-formal input, and it comes from **Eckmann–Hilton**. Because $\Sigma$ is invertible, every object satisfies $X \cong \Omega^2 \Sigma^2 X$, so $X$ is a double loop object. The set $[W, X] = [W, \Omega^2 \Sigma^2 X] = [\Sigma^2 W, \Sigma^2 X]$ carries *two* compatible binary operations (loop concatenation in each of the two loop coordinates), and any set with two unital binary operations satisfying the interchange law is an abelian group with the two operations equal. So the hom-sets are abelian groups for free.

The one-line mechanism: **once $\Sigma$ is invertible, the cofiber and fiber sequences of a map merge into a single bi-infinite, rotatable sequence — and "a rotatable sequence whose consecutive cofibers reproduce it" is exactly a distinguished triangle.**

---

# What Makes This Hard

The genuinely hard step is **TR4, the octahedral axiom**: identifying it with the pasting law for homotopy pushouts requires building the octahedron's faces as four interlocking homotopy-pushout squares and checking the comparison map is the connecting map, which is where most expositions become diagram-heavy. The second pitfall is **the additive structure**: students try to put the group structure on hom-sets by hand and fail, missing that it is forced by the double-loop (Eckmann–Hilton) structure and is therefore automatic and automatically abelian. The most common error is **conflating "pre-triangulated" with "triangulated"** — assuming a pointed model category is already triangulated without using stability, which silently breaks rotation (TR2 needs $\Sigma$ invertible to rotate backwards).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Define the shift to be $\Sigma$ (invertible by stability) and the distinguished triangles to be the cofiber sequences. Inherit the additive structure from the double-loop-object/Eckmann–Hilton argument. Then verify TR1–TR4 by translating each into a statement about homotopy pushouts: existence (TR1), the Puppe sequence (TR2), functoriality of pushouts (TR3), and the pasting law (TR4).

**Subgoal decomposition:**

1. **$\mathrm{Ho}(\mathcal{M})$ is additive.** Show each $[X, Y]$ is an abelian group with bilinear composition.
   - *Hint:* Stability gives $X \cong \Omega^2 \Sigma^2 X$, a double loop object; apply Eckmann–Hilton.
   - *Why needed:* "Triangulated" requires "additive"; without it the long exact sequence has no groups to be exact in.

2. **Define shift and triangles; check well-definedness.** Set $[1] = \Sigma$, distinguished $=$ isomorphic-to-cofiber-sequence.
   - *Hint:* $\Sigma$ is an equivalence (stability), so $[1]$ is an automorphism with inverse $\Omega$.
   - *Why needed:* The shift *must* be invertible for any of TR1–TR4 to make sense; this is exactly where stability is used.

3. **TR1.** Every map embeds in a triangle; $1_X$ gives $X \to X \to 0$; triangles closed under iso.
   - *Hint:* The homotopy cofiber of any map exists by factoring and taking a homotopy pushout; the cofiber of $1_X$ is $0$.
   - *Why needed:* Provides the basic supply of triangles.

4. **TR2 (rotation).** The rotate of a cofiber sequence is a cofiber sequence, with sign $-\Sigma f$.
   - *Hint:* The Puppe sequence: the cofiber of $Y \to Cf$ is $\Sigma X$; track the suspension coordinate to get the sign.
   - *Why needed:* Makes the sequence bi-infinite and symmetric; needs stability to rotate backwards.

5. **TR3 (morphisms).** A commuting square on $(X, Y)$ extends to a map of triangles.
   - *Hint:* Homotopy pushout is functorial up to homotopy; induce the map on cofibers.
   - *Why needed:* Lets triangles be compared; powers the five-lemma arguments.

6. **TR4 (octahedron).** The cones of $f$, $g$, $g \circ f$ fit into an octahedron.
   - *Hint:* Paste the homotopy-pushout square of $f$ to that of $g$; the pasting law gives the comparison triangle $Cf \to C(gf) \to Cg \to \Sigma Cf$.
   - *Why needed:* The only axiom about composites; without it long exact sequences of composable maps are incompatible.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\mathrm{Ho}(\mathcal{M})$ is additive (hom-sets are abelian groups)
> **Statement:** In a stable model category, every $[X, Y]$ carries a natural abelian group structure with bilinear composition, and finite products and coproducts coincide.
>
> **Hint:** Stability gives $X \cong \Omega^2 \Sigma^2 X$; a double loop object's homotopy classes carry two unital binary operations satisfying interchange — Eckmann–Hilton forces them to agree and to be abelian.
>
> **Why needed:** "Additive" is part of the definition of a triangulated category; this lemma supplies it.
>
> > [!note]- Full proof
> > By stability, $\Sigma$ is an equivalence with inverse $\Omega$, so for any $Y$ we have $Y \cong \Sigma^2 \Omega^2 Y$, i.e. every object is (canonically) a *double* loop object $Y \cong \Omega^2 Z$ with $Z = \Sigma^2 Y$. For a single loop object $\Omega Z$, concatenation of loops makes $[X, \Omega Z]$ a group, natural in $X$ (this is the same construction that makes $\pi_1$ a group). For a double loop object $\Omega^2 Z$, the set $[X, \Omega^2 Z]$ carries *two* such group operations — one from each loop coordinate — and they are unital and satisfy the interchange law $(a \cdot b) * (c \cdot d) = (a * c) \cdot (b * d)$ because the two coordinates are independent. The Eckmann–Hilton argument then shows the two operations coincide and the common operation is commutative. Hence $[X, Y]$ is an abelian group, natural in both variables, so composition is bilinear. Bilinear composition with a zero object forces finite products and coproducts to agree (the biproduct), completing additivity. $\blacksquare$

> [!note]- Lemma 2: Homotopy cofibers exist and TR1 holds
> **Statement:** Every map $f \colon X \to Y$ in $\mathrm{Ho}(\mathcal{M})$ admits a homotopy cofiber $Cf$, giving a cofiber sequence $X \to Y \to Cf \to \Sigma X$; the cofiber of $1_X$ is $0$; and the class of cofiber sequences is closed under isomorphism.
>
> **Hint:** Factor $f$ as a cofibration followed by a weak equivalence and take the pushout along $X \to 0$; functoriality of homotopy pushouts gives isomorphism-closure.
>
> **Why needed:** TR1 is the basic supply of distinguished triangles; without it no map can be completed to a triangle.
>
> > [!note]- Full proof
> > Replacing $f$ by a cofibration $X \rightarrowtail Y'$ between cofibrant objects (using factorization and cofibrant replacement), the **homotopy cofiber** is the pushout $Cf = Y' \sqcup_X 0$, which is a homotopy pushout because one leg is a cofibration. The canonical map $Cf \to \Sigma X$ arises because $\Sigma X$ is the homotopy cofiber of $Y' \to Cf$ (crush $Y'$). The cofiber of $1_X$ is $X \sqcup_X 0 = 0$. Closure under isomorphism is immediate from the universal property of the homotopy pushout: an isomorphism of the input data induces an isomorphism of cofibers. $\blacksquare$

> [!note]- Lemma 3: The Puppe rotation (TR2)
> **Statement:** If $X \xrightarrow{f} Y \to Cf \xrightarrow{\partial} \Sigma X$ is a cofiber sequence, then $Y \to Cf \xrightarrow{\partial} \Sigma X \xrightarrow{-\Sigma f} \Sigma Y$ is again a cofiber sequence.
>
> **Hint:** Show the homotopy cofiber of $Y \to Cf$ is $\Sigma X$, by computing the iterated homotopy pushout; the sign tracks the orientation of the suspension coordinate.
>
> **Why needed:** Rotation makes the triangle bi-infinite and is TR2; it requires $\Sigma$ invertible to rotate in both directions.
>
> > [!note]- Full proof
> > Form the diagram of homotopy pushouts: $Cf = Y \sqcup_X 0$, and then the homotopy cofiber of $Y \to Cf$ is $Cf \sqcup_Y 0 = (Y \sqcup_X 0) \sqcup_Y 0 = 0 \sqcup_X 0 = \Sigma X$, using the pasting law for homotopy pushouts. This identifies the next cofiber as $\Sigma X$ and the connecting map as $\partial$. Iterating once more identifies the cofiber of $Cf \to \Sigma X$ as $\Sigma Y$, with the comparison to the suspended map $\Sigma f$ carrying a sign $-1$ coming from the interchange of the two pushout coordinates (the suspension is built from a square, and rotating the square reverses one orientation). Stability ($\Sigma$ invertible) lets the same argument run backwards, giving rotation in both directions. $\blacksquare$

> [!note]- Lemma 4: The octahedral axiom (TR4) is the pasting law
> **Statement:** For composable $X \xrightarrow{f} Y \xrightarrow{g} Z$, the cofibers $Cf$, $Cg$, $C(gf)$ fit into a distinguished triangle $Cf \to C(gf) \to Cg \to \Sigma Cf$, compatibly with the three given cofiber sequences.
>
> **Hint:** Build the $3 \times 3$ diagram of homotopy pushouts on the square $f, g$; the pasting law for homotopy pushouts identifies the iterated cofibers and produces the octahedron's fourth triangle.
>
> **Why needed:** TR4 is the only axiom constraining composites; it is what makes long exact sequences of composable maps compatible.
>
> > [!note]- Full proof
> > Consider the diagram whose rows and columns are cofiber sequences built from $f$ and $g$. The key identity is the **pasting law**: in
> > $$\begin{array}{ccc} X & \to & Y \\ \downarrow & & \downarrow \\ 0 & \to & Cf \end{array} \qquad \begin{array}{ccc} Y & \to & Z \\ \downarrow & & \downarrow \\ Cf & \to & C(gf) \end{array}$$
> > if both small squares are homotopy pushouts then so is the outer rectangle, and conversely if the outer rectangle and the left square are homotopy pushouts then so is the right. Applying this to the composite $gf$ shows $C(gf)$ receives $Cf$ and maps to $Cg$, and the homotopy cofiber of $Cf \to C(gf)$ is $Cg$, giving the fourth triangle $Cf \to C(gf) \to Cg \to \Sigma Cf$. The four cofiber sequences (of $f$, $g$, $gf$, and this new one) are the four faces of the octahedron, and they commute by construction of the homotopy pushouts. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{M}$ be a stable model category.
>
> **Step 0 — preconditions.** $\mathcal{M}$ is pointed, so it has a zero object and the suspension/loop functors $\Sigma, \Omega$ on $\mathrm{Ho}(\mathcal{M})$ with $\Sigma \dashv \Omega$. Stability means $\Sigma$ is an equivalence; hence $\Omega$ is its inverse and $\Sigma$ is an automorphism of $\mathrm{Ho}(\mathcal{M})$, so the candidate shift $[1] = \Sigma$ is invertible as required by the definition of a triangulated category. (This is the only place stability is used directly, but it is essential: it is what makes $[1]$ an automorphism and what powers rotation in both directions.)
>
> **Step 1 — additivity.** By Lemma 1, every $[X, Y]$ is an abelian group with bilinear composition and finite products coincide with coproducts. Thus $\mathrm{Ho}(\mathcal{M})$ is an additive category, and $\Sigma$, being an equivalence built from homotopy colimits, is an additive automorphism.
>
> **Step 2 — the class of triangles.** Declare a triangle distinguished if it is isomorphic in $\mathrm{Ho}(\mathcal{M})$ to a cofiber sequence $X \xrightarrow{f} Y \to Cf \to \Sigma X$ (Lemma 2 constructs $Cf$).
>
> **Step 3 — TR1.** By Lemma 2 every map embeds in a cofiber sequence, the cofiber of $1_X$ is $0$, and the class is closed under isomorphism by fiat. So TR1 holds.
>
> **Step 4 — TR2.** By Lemma 3 the rotate of a cofiber sequence is a cofiber sequence, with the sign $-\Sigma f$; invertibility of $\Sigma$ (Step 0) gives rotation in both directions. So TR2 holds.
>
> **Step 5 — TR3.** Given a commuting square on the first two terms of two cofiber sequences, the functoriality up to homotopy of the homotopy pushout (the universal property of $Cf = Y \sqcup_X 0$) induces a map $h \colon Cf \to Cf'$ completing the morphism of triangles. (As the axiom requires, $h$ need not be unique — the homotopy pushout is functorial only up to a non-canonical homotopy.) So TR3 holds.
>
> **Step 6 — TR4.** By Lemma 4 the pasting law for homotopy pushouts produces, for any composable pair, the octahedral triangle $Cf \to C(gf) \to Cg \to \Sigma Cf$ compatibly with the three given cofiber sequences. So TR4 holds.
>
> **Step 7 — the long exact sequence.** With TR1–TR4 in place, the standard argument applies: applying $[W, -]$ to a distinguished triangle and using that $v \circ u = 0$ (from TR1 on $1_X$ and TR3) together with rotation (TR2) yields exactness at each spot, giving the bi-infinite long exact sequence; dually for $[-, W]$.
>
> Therefore $(\mathrm{Ho}(\mathcal{M}), \Sigma, \text{cofiber sequences})$ is a triangulated category. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Homological algebra — the snake lemma as a triangle.** The connecting homomorphism of the snake lemma, and the long exact sequence in homology of a short exact sequence of complexes, are the long exact sequence of a distinguished triangle in $D(R)$. Re-derive the snake lemma's connecting map as the third map $C \to \Sigma A$ of the triangle of $A \to B \to C$. This is nonobvious because the snake lemma is usually proved by an element-chase, whereas here it is structural — the connecting map is *defined* by the triangle.

**Algebraic topology — the Mayer–Vietoris sequence.** For a space covered by two opens, the Mayer–Vietoris long exact sequence is the long exact sequence of the cofiber sequence relating the cover to the total space, in the stable homotopy category. Recognize the homotopy pushout square of the cover, take its associated triangle, and apply a cohomology functor. Nonobvious because Mayer–Vietoris is classically derived from the long exact sequence of a pair, but both are instances of "apply a homological functor to a triangle."

**Algebraic geometry — the local-to-global triangle for sheaf cohomology.** A short exact sequence of coherent sheaves on a variety gives a distinguished triangle in $D^b(\mathrm{Coh}\,X)$, and applying $R\Gamma$ (derived global sections) yields the long exact sequence of sheaf cohomology. Identify the triangle and the functor. Nonobvious because it shows the cohomology long exact sequence is not special to sheaves — it is the triangle long exact sequence again, with a different homological functor.

---

# Bridges

- **[[Thm - Characterization of Stable Model Categories|Characterization of stable model categories]]** — the companion that closes the loop. This theorem proves "stable $\Rightarrow$ triangulated"; the characterization theorem proves the converse-flavored statement that a pre-triangulated homotopy category is triangulated *exactly when* $\Sigma$ is invertible, so stability is not merely sufficient but the precise dividing line. Together they say: triangulated homotopy categories are exactly the stable ones.

- **[[Thm - The Homotopy Category of a Model Category|The homotopy category of a model category]]** — the unstable predecessor. That theorem constructs $\mathrm{Ho}(\mathcal{M})$ and shows its morphisms are homotopy classes between bifibrant objects; the present theorem adds the stable hypothesis and upgrades the structure from "a category" to "a triangulated category." The construction of $\mathrm{Ho}(\mathcal{M})$ is reused wholesale; only the extra invertibility of $\Sigma$ is new.

- **[[Def - Triangulated Category|Triangulated category]]** — the target structure. The theorem is precisely the statement that this abstract definition is realized by $\mathrm{Ho}(\mathcal{M})$, with the abstract "cone" being the concrete homotopy cofiber and the abstract shift being suspension. Verdier's axioms are reverse-engineered to be exactly what cofiber sequences satisfy, which is why the verification is a translation rather than a discovery.

- **Schwede–Shipley recognition** — the downstream amplifier. Once $\mathrm{Ho}(\mathcal{M})$ is known triangulated, a [[Def - Compact Weak Generator|compact weak generator]] identifies it with modules over a ring spectrum; this theorem supplies the triangulated structure that the recognition theorem then exploits. The pipeline "stable model category $\to$ triangulated $\to$ modules over $\mathrm{End}(G)$" runs through this theorem first.

---

# Unlocked by This

> [!tip] Triangulated Functors and Exact Functors *(from Homological Algebra)*
> A functor between triangulated categories is **triangulated (exact)** if it commutes with the shift and sends distinguished triangles to distinguished triangles. Left/right derived functors of Quillen functors between stable model categories are automatically triangulated, so the derived $\otimes^{\mathbf{L}}$ and $\mathbf{R}\mathrm{Hom}$ are exact functors of triangulated categories — the formal property that makes $\mathrm{Tor}$ and $\mathrm{Ext}$ have long exact sequences in both variables.

> [!tip] Verdier Localization and Quotient Triangulated Categories *(from Derived Algebra)*
> Because $\mathrm{Ho}(\mathcal{M})$ is triangulated, one can form **Verdier quotients** by triangulated subcategories — the triangulated analogue of a quotient category — which is how derived categories of subvarieties, singularity categories, and stable module categories are constructed as quotients. This is unlocked the moment the triangulated structure is available.
