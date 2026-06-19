---
type: theorem
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Def - Equivalence of Categories"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a model category with weak equivalences $\mathcal{W}$. The **localization** $\mathcal{M}[\mathcal{W}^{-1}]$ is the universal category receiving a functor $\gamma : \mathcal{M} \to \mathcal{M}[\mathcal{W}^{-1}]$ sending every map of $\mathcal{W}$ to an isomorphism; we write $\mathrm{Ho}(\mathcal{M}) = \mathcal{M}[\mathcal{W}^{-1}]$ for the **homotopy category**. We write $Q$ for cofibrant replacement, $R$ for fibrant replacement (see [[Def - Cofibrant and Fibrant Objects]]), $\simeq$ for the homotopy relation, and $\pi(A,B) = \mathcal{M}(A,B)/\!\simeq$ for homotopy classes of maps between bifibrant objects (see [[Def - Cylinder Object, Path Object, and Homotopy]]). The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

---

# Statement

> **The Homotopy Category of a Model Category (Fundamental Theorem).** Let $\mathcal{M}$ be a model category. Then the localization $\mathrm{Ho}(\mathcal{M}) = \mathcal{M}[\mathcal{W}^{-1}]$ exists (its hom-classes are genuine sets), and there is an equivalence of categories
> $$\mathrm{Ho}(\mathcal{M}) \;\simeq\; \mathcal{M}_{cf}/\!\simeq,$$
> where $\mathcal{M}_{cf}$ is the full subcategory of **bifibrant** (fibrant–cofibrant) objects and $\mathcal{M}_{cf}/\!\simeq$ is the category whose objects are the bifibrant objects and whose morphisms are **homotopy classes** of maps. Moreover, for arbitrary objects $X, Y$,
> $$\mathrm{Ho}(\mathcal{M})(X, Y) \;\cong\; \pi\big(QRX,\, QRY\big),$$
> the set of homotopy classes of maps between bifibrant replacements; the localization functor $\gamma$ acts as the identity on objects and sends a map to its homotopy class after replacement.

---

# Motivation

This is the theorem that justifies the entire apparatus. The whole point of a model category was to make the localization $\mathcal{M}[\mathcal{W}^{-1}]$ — the category obtained by formally inverting the weak equivalences — *computable*, and this theorem delivers exactly that. Recall the problem it solves: the abstract localization has morphisms that are equivalence classes of arbitrarily long zig-zags $X \leftarrow \bullet \to \bullet \leftarrow \cdots \to Y$, with no algorithm for deciding when two zig-zags are equal, and even a real risk that the hom-classes fail to be sets. You cannot do mathematics in such a category.

The fundamental theorem says: you never need the zig-zags. Every object is weakly equivalent to a bifibrant one (replace by $QRX$), and between bifibrant objects, two maps that become equal in the localization are *exactly* the maps that are homotopic in the concrete sense of [[Def - Cylinder Object, Path Object, and Homotopy]] — connected by a cylinder. So a morphism in $\mathrm{Ho}(\mathcal{M})$ from $X$ to $Y$ is just a homotopy class of honest maps $QRX \to QRY$. The opaque zig-zag collapses to a single arrow up to homotopy. This is why the derived category $D(R)$ — which is $\mathrm{Ho}(\mathbf{Ch}(R))$ — can be treated as a concrete category of complexes-up-to-chain-homotopy rather than an inscrutable formal construction, and it is the reason every "compute in the homotopy category" argument in topology and homological algebra is legitimate.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is just "$\mathcal{M}$ is a model category," but the theorem is *invoked* from several recognizable situations.

The first disguised source is **a localization you want to compute concretely.** Whenever you meet a category obtained by inverting a class of equivalences — the derived category, the stable homotopy category, the homotopy category of spaces — and you want to describe its morphisms, you look for a model structure with those weak equivalences and apply this theorem. The non-obvious step is recognizing that an ad hoc localization carries a hidden model structure. *Example problem:* describe morphisms in the derived category $D(R)$ as chain-homotopy classes of maps between projective resolutions — this is the theorem applied to $\mathbf{Ch}(R)$.

The second disguised source is **a "homotopy classes of maps" set you want to organize into a category.** If you have, for each pair of objects, a set $[X, Y]$ of homotopy classes and you want composition to be well-defined and associative, this theorem certifies that the $[X,Y]$ assemble into a category equivalent to a localization. The non-obvious step is that well-definedness of composition on homotopy classes is *exactly* the bifibrancy hypothesis at work. *Example problem:* verify that homotopy classes of maps between CW complexes form a category — the homotopy category of spaces.

The third disguised source is **needing the localization to be a genuine category (set-sized homs).** When a formal localization threatens set-theoretic trouble, exhibiting a model structure resolves it, because the theorem expresses the homs as $\pi(QRX, QRY)$, manifestly sets. The non-obvious step is that the model structure is what tames the size problem. *Example problem:* show that the homotopy category of topological spaces is locally small, despite the naive localization not obviously being so.

**Targets (Output Amplification)**

The conclusion is the concrete description of $\mathrm{Ho}(\mathcal{M})$; combined with other facts it amplifies.

Combine the conclusion with **a Quillen adjunction.** Given the concrete description of both homotopy categories, a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]] descends to a derived adjunction, and a Quillen equivalence to an equivalence $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$. The amplified result $E$ is the comparison of homotopy theories — see [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] — which depends on knowing $\mathrm{Ho}$ concretely on each side.

Combine the conclusion with **Whitehead's theorem.** Between bifibrant objects, a weak equivalence is a homotopy equivalence (this is part of the theorem's proof). The amplified result is that an isomorphism in $\mathrm{Ho}(\mathcal{M})$ between bifibrant objects lifts to an actual map of $\mathcal{M}$ with a homotopy inverse — the abstract Whitehead theorem, which in $\mathbf{Top}$ is the classical statement that a weak homotopy equivalence between CW complexes is a homotopy equivalence.

Combine the conclusion with **the homotopy relation's structure.** Since $\mathrm{Ho}(\mathcal{M})(X, Y) = \pi(QRX, QRY)$ and $\pi$ is built from cylinder objects, any extra structure on cylinders (suspensions, loop objects) gives extra structure on the homotopy category — the suspension functor, the cofibre/fibre sequences, and ultimately the triangulated structure in the stable case. The amplified result is the entire toolkit of the homotopy category.

---

# Why Is It True

The argument has two movements. First, *reduce to bifibrant objects.* Every $X$ is connected to a bifibrant $QRX$ by a chain of weak equivalences ($X \xrightarrow{\sim} RX \xleftarrow{\sim} QRX$), and in the localization weak equivalences are invertible, so $X$ and $QRX$ become isomorphic in $\mathrm{Ho}(\mathcal{M})$. Hence $\mathrm{Ho}(\mathcal{M})$ is equivalent to the full subcategory on bifibrant objects, and the only question is what the morphisms between bifibrant objects become.

Second, *identify those morphisms as homotopy classes.* Here is the crux. Between bifibrant objects, two maps $f, g$ become equal in $\mathrm{Ho}(\mathcal{M})$ if and only if $f \simeq g$ (they are homotopic). One direction is easy: a homotopy $\mathrm{Cyl}(A) \to B$ becomes, after inverting the weak equivalence $\sigma : \mathrm{Cyl}(A) \xrightarrow{\sim} A$, a proof that $f$ and $g$ agree — because $\sigma$-inverse identifies the two end-inclusions $\mathrm{i}_0, \mathrm{i}_1$. The other direction is the content: if $f$ and $g$ become equal in the localization, they were already homotopic. This is where bifibrancy is essential — it is exactly the hypothesis (from [[Def - Cylinder Object, Path Object, and Homotopy]]) that makes homotopy an equivalence relation and makes the homotopy relation *detect* equality in the localization. The one-line mechanism:

**inverting the weak equivalences does nothing more than collapse homotopic maps, and between bifibrant objects "homotopic" is already an equivalence relation, so the localization is just the homotopy-class quotient.**

Why does this not lose information, and why are the hom-classes sets? Because the homotopy classes $\pi(QRX, QRY)$ are visibly sets (subquotients of the hom-set $\mathcal{M}(QRX, QRY)$), so the size problem evaporates. And composition is well-defined on homotopy classes precisely because homotopic maps compose to homotopic maps on bifibrant objects — another consequence of the cylinder machinery. The theorem is true because the model structure was designed, axiom by axiom, to make these two movements go through: factorization gives the replacements, lifting gives the homotopies, 2-out-of-3 makes homotopy transitive.

---

# What Makes This Hard

The hard direction is showing that maps equal in the localization are already homotopic — the easy direction (homotopic $\Rightarrow$ equal in $\mathrm{Ho}$) lulls people into thinking the theorem is formal, when in fact the substance is the *converse*. The non-obvious step is that you must work on bifibrant objects throughout: the homotopy relation is only an equivalence relation, and only detects localization-equality, when the domain is cofibrant and the codomain is fibrant, so every comparison must first replace objects by $QRX$. The most common error is to attempt the identification on arbitrary objects, where homotopy is neither symmetric nor transitive and the theorem is simply false. A second subtlety is verifying that composition descends to homotopy classes — that homotopic maps compose to homotopic maps — which again silently uses bifibrancy and the lifting axiom.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show $\mathrm{Ho}(\mathcal{M})$ is equivalent to the full subcategory of bifibrant objects (every object is weakly equivalent to its bifibrant replacement, hence isomorphic in $\mathrm{Ho}$). Then show that on bifibrant objects, the localization functor identifies exactly the homotopy classes — so morphisms in $\mathrm{Ho}$ between bifibrant objects are $\pi(-, -)$. Conclude $\mathrm{Ho}(\mathcal{M}) \simeq \mathcal{M}_{cf}/\!\simeq$ and read off the hom-formula.

**Subgoal decomposition:**

1. **Bifibrant replacement is a weak equivalence.** Show $X$ is connected to $QRX$ by weak equivalences, hence isomorphic in $\mathrm{Ho}(\mathcal{M})$.
   - *Hint:* Use $X \xrightarrow{\sim} RX$ (fibrant replacement) and $QRX \xrightarrow{\sim} RX$ (cofibrant replacement of $RX$).
   - *Why needed:* It reduces the whole category to its bifibrant subcategory.

2. **Homotopy is an equivalence relation on bifibrant objects.** Recall from [[Def - Cylinder Object, Path Object, and Homotopy]] that $\simeq_\ell = \simeq_r = \simeq$ is an equivalence relation when the domain is cofibrant and codomain fibrant.
   - *Hint:* Reflexivity from the cylinder, symmetry from cylinder swap, transitivity from gluing cylinders (uses 2-out-of-3).
   - *Why needed:* So that $\mathcal{M}_{cf}/\!\simeq$ is a well-defined category.

3. **Composition descends to homotopy classes.** Show homotopic maps compose to homotopic maps on bifibrant objects.
   - *Hint:* Post/pre-composing a cylinder homotopy with a map gives a cylinder homotopy.
   - *Why needed:* So $\mathcal{M}_{cf}/\!\simeq$ has well-defined composition.

4. **Homotopic $\Rightarrow$ equal in $\mathrm{Ho}$.** A left homotopy becomes an equality after inverting $\sigma : \mathrm{Cyl}(A) \xrightarrow{\sim} A$.
   - *Hint:* Inverting $\sigma$ forces $\mathrm{i}_0 = \mathrm{i}_1$ in $\mathrm{Ho}$, so $f = H\mathrm{i}_0$ and $g = H\mathrm{i}_1$ agree.
   - *Why needed:* The easy half of the morphism identification.

5. **Equal in $\mathrm{Ho}$ $\Rightarrow$ homotopic (on bifibrant objects).** Show the localization functor restricted to bifibrant objects factors through $\pi$ and is bijective on homs.
   - *Hint:* Build $\mathrm{Ho}(\mathcal{M}) \to \mathcal{M}_{cf}/\!\simeq$ and check it is inverse to $\gamma$ on bifibrant objects, using that $\gamma$ inverts weak equivalences and homotopy detects equality.
   - *Why needed:* The substantial half; it gives $\mathrm{Ho}(\mathcal{M})(X,Y) \cong \pi(QRX, QRY)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Every object is isomorphic in $\mathrm{Ho}(\mathcal{M})$ to a bifibrant object
> **Statement:** For every $X$, the bifibrant replacement $QRX$ is connected to $X$ by a zig-zag of weak equivalences, hence $\gamma(QRX) \cong \gamma(X)$ in $\mathrm{Ho}(\mathcal{M})$.
>
> **Hint:** Compose the fibrant-replacement equivalence $X \xrightarrow{\sim} RX$ with the cofibrant-replacement equivalence $QRX \xrightarrow{\sim} RX$.
>
> **Why needed:** It reduces $\mathrm{Ho}(\mathcal{M})$ to its bifibrant full subcategory.
>
> > [!note]- Full proof
> > By [[Def - Cofibrant and Fibrant Objects]], $r_X : X \xrightarrow{\sim} RX$ is a trivial cofibration (a weak equivalence), and $q_{RX} : QRX \xrightarrow{\sim} RX$ is a trivial fibration (a weak equivalence), with $QRX$ bifibrant ($Q$ of a fibrant object is bifibrant, since $Q$ preserves fibrancy as the cofibrant replacement maps are trivial fibrations). The localization $\gamma$ inverts both, giving isomorphisms $\gamma(X) \cong \gamma(RX) \cong \gamma(QRX)$ in $\mathrm{Ho}(\mathcal{M})$.

> [!note]- Lemma 2: Whitehead's theorem — a weak equivalence between bifibrant objects is a homotopy equivalence
> **Statement:** If $f : A \to B$ is a weak equivalence between bifibrant objects, then $f$ has a homotopy inverse.
>
> **Hint:** Factor $f$ as a trivial cofibration then trivial fibration; on bifibrant objects each admits a homotopy-inverse section by lifting.
>
> **Why needed:** It makes weak equivalences between bifibrant objects into isomorphisms in $\mathcal{M}_{cf}/\!\simeq$, matching their inversion in $\mathrm{Ho}$.
>
> > [!note]- Full proof
> > Factor $f = p \circ i$ with $i$ a trivial cofibration and $p$ a fibration; by 2-out-of-3, $p$ is a weak equivalence, hence a trivial fibration. Since $A$ is cofibrant, the trivial cofibration $i : A \to C$ has a retraction up to homotopy (lift $\mathrm{id}_A$ against $i$ in the square with the fibration $C \to *$), so $i$ is a homotopy equivalence; since $B$ is fibrant, the trivial fibration $p$ has a section up to homotopy (lift against $\varnothing \to B$), so $p$ is a homotopy equivalence. Composing, $f$ is a homotopy equivalence.

> [!note]- Lemma 3: Homotopic maps are identified by the localization; the converse holds on bifibrant objects
> **Statement:** For bifibrant $A, B$ and maps $f, g : A \to B$, one has $\gamma(f) = \gamma(g)$ in $\mathrm{Ho}(\mathcal{M})$ if and only if $f \simeq g$.
>
> **Hint:** Forward: invert the cylinder's structure map. Backward: build a functor $\mathrm{Ho}(\mathcal{M}) \to \mathcal{M}_{cf}/\!\simeq$ and check it inverts $\gamma$.
>
> **Why needed:** It is the morphism identification: $\mathrm{Ho}(\mathcal{M})(A,B) \cong \pi(A,B)$ for bifibrant $A, B$.
>
> > [!note]- Full proof
> > ($f \simeq g \Rightarrow \gamma(f) = \gamma(g)$) Let $H : \mathrm{Cyl}(A) \to B$ be a left homotopy with structure map $\sigma : \mathrm{Cyl}(A) \xrightarrow{\sim} A$ and end inclusions $\mathrm{i}_0, \mathrm{i}_1$. Since $\sigma$ is a weak equivalence, $\gamma(\sigma)$ is an isomorphism, and from $\sigma \mathrm{i}_0 = \mathrm{id}_A = \sigma \mathrm{i}_1$ we get $\gamma(\mathrm{i}_0) = \gamma(\sigma)^{-1} = \gamma(\mathrm{i}_1)$. Then $\gamma(f) = \gamma(H)\gamma(\mathrm{i}_0) = \gamma(H)\gamma(\mathrm{i}_1) = \gamma(g)$.
> >
> > ($\gamma(f) = \gamma(g) \Rightarrow f \simeq g$) Define $\delta : \mathcal{M}_{cf}/\!\simeq \,\to \mathrm{Ho}(\mathcal{M})$ on bifibrant objects by $\delta[h] = \gamma(h)$ (well-defined by the forward direction). By Lemma 1, restricting $\gamma$ to bifibrant objects and quotienting by homotopy gives a functor that is essentially surjective and, by the existence of $\delta$, full and faithful, so $\gamma$ induces a bijection $\pi(A,B) \xrightarrow{\cong} \mathrm{Ho}(\mathcal{M})(A,B)$. In particular $\gamma(f) = \gamma(g)$ forces $[f] = [g]$, i.e. $f \simeq g$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — the localization exists.** We will exhibit a category $\mathcal{M}_{cf}/\!\simeq$ with set-sized homs together with a functor from $\mathcal{M}$ inverting $\mathcal{W}$ and universal among such; this *constructs* $\mathrm{Ho}(\mathcal{M})$ and proves its homs are sets.
>
> **Step 1 — the bifibrant homotopy category is a category.** By Lemma 3 (forward) and the equivalence-relation property of $\simeq$ on bifibrant objects ([[Def - Cylinder Object, Path Object, and Homotopy]]), the homotopy classes $\pi(A,B)$ are well-defined sets, and composition descends (homotopic maps compose to homotopic maps, since pre/post-composing a cylinder homotopy with a map yields a cylinder homotopy). So $\mathcal{M}_{cf}/\!\simeq$ is a category with set-sized homs.
>
> **Step 2 — bifibrant replacement and the comparison functor.** Define $\gamma : \mathcal{M} \to \mathcal{M}_{cf}/\!\simeq$ on objects by $X \mapsto QRX$ and on maps by sending $f$ to the homotopy class of its bifibrant-replacement lift $QRf$. By Lemma 1, $\gamma$ sends every weak equivalence to an isomorphism (Lemma 2, Whitehead, makes a weak equivalence between bifibrant objects a homotopy equivalence, hence an isomorphism in $\mathcal{M}_{cf}/\!\simeq$).
>
> **Step 3 — universality.** Any functor $\Phi : \mathcal{M} \to \mathcal{D}$ inverting $\mathcal{W}$ factors uniquely through $\gamma$: on objects $\Phi(X) \cong \Phi(QRX)$ (Lemma 1), and on maps $\Phi$ identifies homotopic maps (Lemma 3 forward, applied with $\Phi$ in place of $\gamma$), so $\Phi$ descends to $\mathcal{M}_{cf}/\!\simeq$. This is the universal property of localization, so $\mathcal{M}_{cf}/\!\simeq \,\simeq\, \mathcal{M}[\mathcal{W}^{-1}] = \mathrm{Ho}(\mathcal{M})$.
>
> **Step 4 — the hom-formula.** Restricting to bifibrant objects, Lemma 3 gives $\mathrm{Ho}(\mathcal{M})(A,B) \cong \pi(A,B)$. For general $X, Y$, compose with the isomorphisms $X \cong QRX$, $Y \cong QRY$ of Lemma 1 to obtain
> $$\mathrm{Ho}(\mathcal{M})(X,Y) \cong \mathrm{Ho}(\mathcal{M})(QRX, QRY) \cong \pi(QRX, QRY). \qquad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**The derived category as chain-homotopy classes.** Apply the theorem to $\mathbf{Ch}(R)$: bifibrant objects are bounded complexes of projectives, the homotopy relation is [[Def - Chain Map and Chain Homotopy|chain homotopy]], and the theorem gives $D(R)(M, N) = \{\text{chain maps } P_\bullet \to Q_\bullet\}/\text{chain homotopy}$ for projective resolutions $P_\bullet, Q_\bullet$ of $M, N$. This is the model-categorical proof that morphisms in the derived category are computed by resolving and taking chain-homotopy classes — see [[Ex - The homotopy category of chain complexes is the derived category]].

**The homotopy category of spaces and Whitehead.** Apply the theorem to $\mathbf{Top}$: bifibrant objects are CW complexes, the homotopy relation is ordinary homotopy, and Lemma 2 specializes to **Whitehead's theorem** — a weak homotopy equivalence between CW complexes is a homotopy equivalence. This is the surprising payoff that a homotopy-theoretic isomorphism is realized by an actual map.

**Stable homotopy and triangulated structure.** In a stable model category (spectra, or unbounded $\mathbf{Ch}(R)$), the homotopy category inherits a suspension that is invertible and a class of distinguished triangles, making it **triangulated**. The fundamental theorem provides the underlying concrete category on which this structure is defined; recognizing that the triangulated structure lives on $\mathrm{Ho}$, not on $\mathcal{M}$, is the conceptual point.

---

# Bridges

- **[[Def - Cylinder Object, Path Object, and Homotopy]]** — supplies the homotopy relation that becomes the morphisms of $\mathrm{Ho}(\mathcal{M})$. The theorem is the statement that the cylinder-based homotopy relation is *exactly* the equivalence relation that the localization imposes on bifibrant objects; the two notions of "the same map" coincide.

- **[[Def - Cofibrant and Fibrant Objects]]** — supplies the replacements $Q, R$ that reduce arbitrary objects to bifibrant ones. The hom-formula $\pi(QRX, QRY)$ is the theorem's concrete output, and it is computed entirely through these replacements.

- **[[Thm - Quillen Adjunctions Descend to Derived Adjunctions]]** — the natural sequel. Once $\mathrm{Ho}(\mathcal{M})$ is known concretely on each side, a Quillen adjunction induces a derived adjunction between the homotopy categories, and a Quillen equivalence an equivalence — the way one proves two model categories present the same homotopy theory.

- **Localization of categories** — the general framework. This theorem is the special case where the abstract, computationally inert localization $\mathcal{M}[\mathcal{W}^{-1}]$ becomes concrete because the auxiliary model structure supplies a calculus of fractions via homotopies, sidestepping the need for Gabriel–Zisman zig-zags.

---

# Unlocked by This

> [!tip] The Derived Category and Triangulated Categories *(from Homological Algebra)*
> Specializing to $\mathbf{Ch}(R)$ gives the **derived category** $D(R) = \mathrm{Ho}(\mathbf{Ch}(R))$, with morphisms computed as chain-homotopy classes between projective resolutions. The distinguished triangles arising from mapping cones make $D(R)$ a **triangulated category**, and this theorem supplies the underlying concrete category.

> [!tip] Whitehead's Theorem *(from Algebraic Topology)*
> The lemma "weak equivalence between bifibrant objects is a homotopy equivalence" is, in $\mathbf{Top}$, exactly **Whitehead's theorem**: a weak homotopy equivalence between CW complexes is a homotopy equivalence. The model-categorical proof shows this is a formal feature of any model category, not special to spaces.

> [!tip] Presentations of (∞,1)-Categories *(from Higher Category Theory)*
> $\mathrm{Ho}(\mathcal{M})$ is the *homotopy category* (the $1$-categorical truncation) of the **(∞,1)-category** presented by $\mathcal{M}$. The full ∞-categorical localization remembers higher homotopies that $\mathrm{Ho}$ forgets; the fundamental theorem is the bottom layer of the Joyal–Lurie comparison developed in the [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories|Higher Categories]] chapter.
