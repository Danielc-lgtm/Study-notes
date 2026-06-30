---
type: theorem
subject: model-categories
prereqs:
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Def - Pullback and Pushout"
  - "Def - Adjunction"
  - "Thm - The Homotopy Category of a Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Pointed Model Category Suspension and Loop|pointed model category]] with zero object $*$, homotopy category $\mathrm{Ho}(\mathcal{C})$, [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma$ and [[Def - Pointed Model Category Suspension and Loop|loop]] $\Omega$. We write $[X, Y] = \mathrm{Ho}(\mathcal{C})(X, Y)$ for the morphisms in the homotopy category, a pointed set with basepoint the zero map. We write $\Sigma X = * \cup_X \mathrm{Cyl}(X) \cup_X *$ (the homotopy pushout of $* \leftarrow X \rightarrow *$) and $\Omega Y = * \times_Y \mathrm{Path}(Y) \times_Y *$ (the homotopy pullback of $* \rightarrow Y \leftarrow *$), using a [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] $\mathrm{Cyl}(X)$ and [[Def - Cylinder Object, Path Object, and Homotopy|path object]] $\mathrm{Path}(Y)$. An [[Def - Adjunction|adjunction]] $\Sigma \dashv \Omega$ is a natural bijection $[\Sigma X, Y] \cong [X, \Omega Y]$. The full symbol registry is on [[Model Categories — Pointed Model Categories and Cofiber Sequences]].

---

# Statement

> **Theorem (Suspension–Loop Adjunction).** Let $\mathcal{C}$ be a pointed model category. The suspension and loop functors on the homotopy category are adjoint, $\Sigma \dashv \Omega$: there is a bijection
> $$[\Sigma X, Y] \;\cong\; [X, \Omega Y]$$
> natural in $X, Y \in \mathrm{Ho}(\mathcal{C})$. Equivalently, $\Sigma : \mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$ is left adjoint to $\Omega : \mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$, with unit $\eta_X : X \to \Omega\Sigma X$ and counit $\varepsilon_Y : \Sigma\Omega Y \to Y$ satisfying the triangle identities.

> **Companion form (via the interval).** When $\mathcal{C}$ is a pointed simplicial (or topological) model category, $\Sigma X = X \wedge S^1$ and $\Omega Y = \mathrm{Map}_*(S^1, Y)$, and the adjunction is the derived smash–hom adjunction $[X \wedge S^1, Y] \cong [X, \mathrm{Map}_*(S^1, Y)]$ — the homotopy category's reflection of the strict adjunction $-\wedge S^1 \dashv \mathrm{Map}_*(S^1, -)$.

The two forms agree: the general homotopy-(co)limit definition specializes to the smash/mapping-space form whenever the interval $S^1$ is available.

---

# Motivation

This theorem is the structural keystone of the chapter. Everything that follows — cofiber sequences becoming long exact sequences, fiber sequences being the dual story, the whole pre-triangulated package — runs on the single fact that $\Sigma$ and $\Omega$ are adjoint. The reason the adjunction is doing so much work is that it is the mechanism that *converts a cofiber sequence into a fiber sequence and back*. A cofiber sequence ends in $\Sigma X$; mapping out of it, $[\Sigma X, Z]$, is the same as $[X, \Omega Z]$, which is what you map into in a fiber sequence. The adjunction is the hinge on which the two dual exact sequences turn into each other.

There is also a foundational payoff. In ordinary homotopy theory one *proves* the suspension–loop adjunction by hand for spaces, juggling continuous maps and [[Def - Homotopy|homotopies]]. The theorem says this is not a fact about topology at all: it holds in *every* pointed model category, for the abstract reason that suspension is a homotopy colimit (a derived left adjoint) and loop is the dual homotopy limit. The classical statement $\pi_{n+1}(Y) \cong \pi_n(\Omega Y)$ and the whole loop-space machinery are corollaries of a general adjunction, not special features of spaces. This is the model-category program in miniature: a theorem proved once abstractly, then specialized for free.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is "$\mathcal{C}$ pointed model category," which is mild; the real source question is: in what guise does a problem present a situation to which $\Sigma \dashv \Omega$ applies, when no suspension is named?

The first disguised source is **a derived smash–hom (or tensor–cotensor) adjunction**. Whenever $\mathcal{C}$ is enriched, tensored, and cotensored over pointed spaces or simplicial sets — which holds for $\mathbf{Top}_*$, $\mathbf{sSet}_*$, symmetric spectra, and any [[Def - Quillen Adjunction and Quillen Equivalence|Quillen]]-simplicial model category — the strict adjunction $-\wedge K \dashv \mathrm{Map}_*(K, -)$ exists for every pointed space $K$. Taking $K = S^1$ and deriving gives $\Sigma \dashv \Omega$. The implication "enriched over $\mathbf{sSet}_*$ $\Rightarrow$ has $\Sigma \dashv \Omega$" is non-obvious because the enrichment is extra structure that one might not connect to suspension. *Example problem:* on chain complexes $\mathrm{Ch}(R)$, the cotensor by $S^1$ is the shift, so the smash–hom adjunction becomes "shift up $\dashv$ shift down," recovering $X[1] \dashv X[-1]$.

The second disguised source is **a pair of dual homotopy (co)limit diagrams**. Any time a construction is "the homotopy cofiber of a map to the terminal object," it is a suspension; any time it is "the homotopy fiber of a map from the initial object," it is a loop. Recognizing a homotopy pushout with two corners at $*$ as a suspension lets you apply the adjunction. *Example problem:* given a homotopy cofiber sequence, identify its last term as $\Sigma$ of the first, then use $[\Sigma X, Z] \cong [X, \Omega Z]$ to rewrite the induced map on mapping sets as a map into a loop space — this is the step that converts the cofiber long exact sequence into the fiber one.

The third disguised source is **a Quillen adjunction $F \dashv G$ between pointed model categories that commutes with the interval**. If $F$ preserves the homotopy pushouts defining suspension (which a left [[Def - Quillen Adjunction and Quillen Equivalence|Quillen functor]] does, being a derived left adjoint), then $LF \circ \Sigma \cong \Sigma \circ LF$, and the suspension–loop adjunction transports across $F \dashv G$. The non-obvious content is that left Quillen functors commute with suspension *because* both are derived left adjoints. *Example problem:* geometric realization $|-| : \mathbf{sSet}_* \to \mathbf{Top}_*$ is left Quillen, so $|\Sigma X| \simeq \Sigma|X|$ and the simplicial and topological suspension–loop adjunctions match — which is part of why the two categories present the same homotopy theory.

**Targets (Output Amplification)**

The bare conclusion is a bijection $[\Sigma X, Y] \cong [X, \Omega Y]$. Combined with other facts it does much more.

Combine the adjunction with **the cofiber sequence of a map**. A cofiber sequence $X \to Y \to C_f \to \Sigma X$ and the adjunction together produce, for each test $Z$, both the long exact sequence $\cdots \to [\Sigma X, Z] \to [C_f, Z] \to [Y, Z] \to [X, Z]$ and its rewriting $[\Sigma X, Z] = [X, \Omega Z]$, which threads the cofiber sequence's tail into a fiber sequence's head. The further result is the **agreement of cofiber and fiber long exact sequences** ([[Thm - The Puppe Cofiber and Fiber Sequences Agree]]): the adjunction is the precise isomorphism identifying the two.

Combine the adjunction with **the group structure on $[\Sigma X, Y]$**. Because $\Sigma X$ is a homotopy cogroup object (it carries a co-multiplication from pinching the suspension coordinate), $[\Sigma X, Y]$ is a *group*, abelian on $[\Sigma^2 X, Y]$. Transporting along the adjunction, $[X, \Omega Y]$ inherits the same group structure, now from $\Omega Y$ being a homotopy group object. The further result $E$ is that **loop spaces are group objects up to homotopy** and double loop spaces are abelian — the Eckmann–Hilton conclusion — extracted purely from the adjunction and the co-group on the suspension.

Combine the adjunction with **invertibility of $\Sigma$ (stability)**. If $\Sigma$ is an equivalence then the unit $\eta : X \to \Omega\Sigma X$ and counit $\varepsilon : \Sigma\Omega Y \to Y$ are isomorphisms, so $\Omega = \Sigma^{-1}$. The further result is that $\mathrm{Ho}(\mathcal{C})$ becomes a **triangulated category**: the adjunction supplies the inverse shift, and the cofiber/fiber sequences merge into distinguished triangles. The adjunction is thus the seed of the entire stable theory of the next chapter.

---

# Why Is It True

Forget the formal proof and think about what the adjunction *says* in the simplest case, $\mathbf{Top}_*$. A map $\Sigma X \to Y$ out of the suspension is a map out of "$X$ with a suspension coordinate"; it is a family of maps $X \to Y$ parametrized by the suspension interval, pinned at the basepoint at both ends. But "a path of maps $X \to Y$ that starts and ends at the constant basepoint map" is the same as "a single map $X \to (\text{based loops in } Y)$" — you just regroup which variable is which. The suspension coordinate on the source becomes the loop coordinate on the target. That regrouping is the entire content; it is the exponential law $\mathrm{Map}(A \times I, B) \cong \mathrm{Map}(A, \mathrm{Map}(I, B))$, restricted to the based pieces.

The model-category proof is the homotopical version of exactly this regrouping. The key is that $\Sigma$ is built from a homotopy *pushout* and $\Omega$ from a homotopy *pullback*, and pushouts and pullbacks are themselves adjoint to the diagonal:
$$\mathrm{colim} \dashv \Delta \dashv \mathrm{lim}.$$
Derive this adjunction and restrict it to the pushout/pullback shape whose two outer legs are the zero object, and you get $\Sigma \dashv \Omega$. The mapping-set bijection is the universal property of the homotopy pushout read against $Y$, composed with the universal property of the homotopy pullback read from $X$:
$$[\Sigma X, Y] = [\text{hocolim}(* \leftarrow X \rightarrow *), Y] \cong \text{holim}\big([*, Y] \leftarrow [X, Y] \rightarrow [*, Y]\big) \cong [X, \text{holim}(* \rightarrow Y \leftarrow *)] = [X, \Omega Y].$$
The middle isomorphism is the defining property of a homotopy colimit (maps out of a homotopy colimit are the homotopy limit of the maps out of the pieces); the last is the defining property of the homotopy limit.

**The one-line mechanism: $\Sigma$ is a homotopy colimit and $\Omega$ is the dual homotopy limit, and "maps out of a colimit = maps into the matching limit" is the adjunction.** Once you see suspension as a derived left adjoint and loop as the matching derived right adjoint, the adjunction is not a computation but a definition unwound.

---

# What Makes This Hard

The trap is **well-definedness on the homotopy category**: $\Sigma$ and $\Omega$ are defined by choices (a cylinder object, a path object), so one must check the bijection does not depend on those choices and is natural in $\mathrm{Ho}(\mathcal{C})$, where morphisms are themselves equivalence classes. The non-obvious step is that the strict adjunction one might write (between the point-set constructions) is *not* an adjunction on the nose — only its derived version is — so the proof must either work entirely in $\mathrm{Ho}(\mathcal{C})$ or carefully track cofibrant/fibrant replacements. The common error is to "prove" the adjunction by the naive exponential law without checking that the homotopy colimit/limit, not the strict ones, are what appear; the strict pushout of $* \leftarrow X \rightarrow *$ is just $*$, so a strict argument proves the trivial (wrong) statement $[*, Y] \cong [X, *]$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Reduce to bifibrant objects so that $[\,,]$ is computed by homotopy classes. Build the unit $\eta : X \to \Omega\Sigma X$ and counit $\varepsilon : \Sigma\Omega Y \to Y$ from the (co)cone structure of the cylinder and path object, then verify the triangle identities up to homotopy — equivalently, exhibit the bijection $[\Sigma X, Y] \cong [X, \Omega Y]$ directly as the derived form of $\mathrm{colim} \dashv \Delta \dashv \mathrm{lim}$.

**Subgoal decomposition:**

1. **Reduce to a bijection of homotopy classes.** Replace $X$ by a cofibrant model and $Y$ by a fibrant model so that $[\Sigma X, Y] = \pi(\Sigma X, Y)$ and $[X, \Omega Y] = \pi(X, \Omega Y)$.
   - *Hint:* Suspension is computed on cofibrant objects, loop on fibrant ones; cofibrant/fibrant replacement does not change the homotopy type.
   - *Why needed:* It turns the abstract $\mathrm{Ho}$-statement into a concrete statement about homotopy classes of point-set maps, where the cylinder and path object are available.

2. **Establish the strict exponential law for the interval.** In the point-set category, exhibit a natural isomorphism between maps $\mathrm{Cyl}(X) \to Y$ with both ends sent to the basepoint and maps $X \to \mathrm{Path}(Y)$ with both endpoints at the basepoint.
   - *Hint:* This is $\mathrm{colim} \dashv \Delta \dashv \mathrm{lim}$ for the pushout/pullback shape: a cocone under $* \leftarrow X \rightarrow *$ with apex $Y$ is the same as a cone over $* \rightarrow Y \leftarrow *$ with apex $X$, both being "an $X$-family of based loops."
   - *Why needed:* It is the algebraic core — the bijection before passing to homotopy.

3. **Descend the bijection to homotopy classes.** Show the strict bijection respects the homotopy relations on both sides, so it induces $\pi(\Sigma X, Y) \cong \pi(X, \Omega Y)$.
   - *Hint:* A homotopy of maps $\mathrm{Cyl}(X) \to Y$ corresponds under the exponential law to a homotopy of maps $X \to \mathrm{Path}(Y)$; the cylinder on the cylinder matches the path object on the path object.
   - *Why needed:* It is the step that makes the bijection live on $\mathrm{Ho}(\mathcal{C})$ rather than on point-set maps.

4. **Identify unit and counit and check the triangle identities.** Extract $\eta_X : X \to \Omega\Sigma X$ as the image of $\mathrm{id}_{\Sigma X}$ and $\varepsilon_Y : \Sigma\Omega Y \to Y$ as the image of $\mathrm{id}_{\Omega Y}$, and verify $(\Omega\varepsilon)\circ(\eta\Omega) = \mathrm{id}_\Omega$ and $(\varepsilon\Sigma)\circ(\Sigma\eta) = \mathrm{id}_\Sigma$ in $\mathrm{Ho}(\mathcal{C})$.
   - *Hint:* The triangle identities are formal consequences of any hom-set adjunction once the bijection is natural; alternatively read them off the (co)cone descriptions.
   - *Why needed:* It packages the bijection as a genuine adjunction with the unit/counit that the pre-triangulated structure later uses.

---

# Lemma Decomposition

> [!note]- Lemma 1: Suspension is a derived left adjoint (homotopy colimit)
> **Statement:** $\Sigma X = \mathrm{hocolim}(* \leftarrow X \rightarrow *)$ is the total left derived functor of the strict pushout functor $\mathrm{colim} : \mathcal{C}^{\,\Lambda} \to \mathcal{C}$ along the diagram shape $\Lambda = (\bullet \leftarrow \bullet \rightarrow \bullet)$, applied to the constant-at-$*$ legs.
>
> **Hint:** The pushout is left adjoint to the constant-diagram functor $\Delta$; derive both. Cofibrant replacement of the diagram (making the legs cofibrations) computes the homotopy pushout.
>
> **Why needed:** It supplies the "maps out of a homotopy colimit = homotopy limit of maps out" universal property, which is the left half of the adjunction bijection.
>
> > [!note]- Full proof
> > The pushout functor $\mathrm{colim} : \mathcal{C}^\Lambda \to \mathcal{C}$ is left adjoint to the constant-diagram functor $\Delta : \mathcal{C} \to \mathcal{C}^\Lambda$, by the universal property of the colimit: a map $\mathrm{colim}\, D \to Y$ is the same as a cocone $D \to \Delta Y$. With the projective (or Reedy) model structure on $\mathcal{C}^\Lambda$, this is a Quillen adjunction, so it derives to an adjunction $\mathrm{hocolim} = L\mathrm{colim} \dashv \Delta$ on homotopy categories. Cofibrantly replacing the diagram $* \leftarrow X \rightarrow *$ means replacing the legs by cofibrations $X \rightarrowtail \mathrm{Cyl}(X)\text{-halves}$; the colimit of the replaced diagram is $* \cup_X \mathrm{Cyl}(X) \cup_X * = \Sigma X$. Hence $\Sigma X = \mathrm{hocolim}(* \leftarrow X \rightarrow *)$, and for any $Y$, $[\Sigma X, Y] = \mathrm{Ho}(\mathcal{C})(\mathrm{hocolim}\, D, Y) \cong \mathrm{holim}\,\mathrm{Ho}(\mathcal{C})(D, Y)$, the homotopy limit of the diagram of mapping sets $[*, Y] \leftarrow [X, Y] \rightarrow [*, Y]$.

> [!note]- Lemma 2: Loop is the dual derived right adjoint (homotopy limit)
> **Statement:** $\Omega Y = \mathrm{holim}(* \rightarrow Y \leftarrow *)$ is the total right derived functor of the strict pullback functor along $\Lambda^{op}$, and for any $X$, $[X, \Omega Y] \cong \mathrm{holim}\,([X, *] \rightarrow [X, Y] \leftarrow [X, *])$.
>
> **Hint:** Dualize Lemma 1: the pullback is right adjoint to $\Delta$; derive with the Reedy/injective model structure and fibrant-replace the diagram using a path object.
>
> **Why needed:** It supplies the right half of the bijection — "maps into a homotopy limit = homotopy limit of maps into" — which must match the right-hand diagram from Lemma 1.
>
> > [!note]- Full proof
> > The pullback functor $\mathrm{lim} : \mathcal{C}^{\Lambda^{op}} \to \mathcal{C}$ is right adjoint to $\Delta$, and with the injective (or Reedy) model structure this is a Quillen adjunction $\Delta \dashv \mathrm{lim}$, deriving to $\Delta \dashv \mathrm{holim}$. Fibrantly replacing $* \rightarrow Y \leftarrow *$ replaces the legs by [[Def - Fibration|fibrations]] via a path object, and the limit of the replaced diagram is $* \times_Y \mathrm{Path}(Y) \times_Y * = \Omega Y$. For any $X$, $[X, \Omega Y] = \mathrm{Ho}(\mathcal{C})(X, \mathrm{holim}\, D') \cong \mathrm{holim}\,\mathrm{Ho}(\mathcal{C})(X, D')$, the homotopy limit of $[X, *] \rightarrow [X, Y] \leftarrow [X, *]$.

> [!note]- Lemma 3: The two matching diagrams coincide, giving the bijection
> **Statement:** The homotopy limit of $[*, Y] \leftarrow [X, Y] \rightarrow [*, Y]$ (from Lemma 1) is canonically isomorphic to the homotopy limit of $[X, *] \rightarrow [X, Y] \leftarrow [X, *]$ (from Lemma 2), and both equal the based loop set of $[X, Y]$ at its basepoint $0$.
>
> **Hint:** Both diagrams have the singleton $[*, Y] = [X, *] = *$ at the two ends and $[X, Y]$ in the middle; their homotopy limit is "loops in $[X,Y]$ based at $0$," computed identically from either side.
>
> **Why needed:** It is the identification that turns the left-half computation into the right-half computation, yielding $[\Sigma X, Y] \cong [X, \Omega Y]$.
>
> > [!note]- Full proof
> > Since $*$ is a zero object, $[*, Y]$ and $[X, *]$ are singletons (the basepoint of the respective hom-set). A homotopy limit (= homotopy pullback) of a cospan $* \rightarrow A \leftarrow *$ is the based loop object of $A$ at the chosen point — the homotopy fiber over the point of the path fibration — and this is symmetric in the two singleton legs. Both diagrams from Lemmas 1 and 2 are such a cospan/span with $A = [X, Y]$ and both legs the basepoint $0$. Therefore their homotopy limits agree, giving the chain
> > $$[\Sigma X, Y] \cong \mathrm{holim}([*,Y] \leftarrow [X,Y] \rightarrow [*,Y]) = \Omega[X,Y]_0 = \mathrm{holim}([X,*] \rightarrow [X,Y] \leftarrow [X,*]) \cong [X, \Omega Y].$$
> > Naturality in $X$ and $Y$ is inherited from naturality of each homotopy (co)limit.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{C}$ be a pointed model category.
>
> **Step 0 — reductions and well-posedness.** Replace $X$ by a cofibrant model and $Y$ by a fibrant model; this does not change $[\,,]$. On cofibrant $X$ the suspension $\Sigma X = * \cup_X \mathrm{Cyl}(X) \cup_X *$ is defined and is a homotopy colimit; on fibrant $Y$ the loop $\Omega Y = * \times_Y \mathrm{Path}(Y) \times_Y *$ is defined and is a homotopy limit. Both descend to functors on $\mathrm{Ho}(\mathcal{C})$, independent of the choice of cylinder and path object up to canonical isomorphism (the constructions are derived functors, hence well-defined on $\mathrm{Ho}$).
>
> **Step 1 — suspension as homotopy colimit.** By Lemma 1, $\Sigma X = \mathrm{hocolim}(* \leftarrow X \rightarrow *)$, so for every $Y$,
> $$[\Sigma X, Y] \;\cong\; \mathrm{holim}\big([*, Y] \leftarrow [X, Y] \rightarrow [*, Y]\big).$$
>
> **Step 2 — loop as homotopy limit.** By Lemma 2, $\Omega Y = \mathrm{holim}(* \rightarrow Y \leftarrow *)$, so for every $X$,
> $$[X, \Omega Y] \;\cong\; \mathrm{holim}\big([X, *] \rightarrow [X, Y] \leftarrow [X, *]\big).$$
>
> **Step 3 — match the diagrams.** Because $*$ is a zero object, $[*, Y]$ and $[X, *]$ are singletons. By Lemma 3 the two homotopy limits in Steps 1 and 2 are both the based loop set $\Omega[X, Y]_0$ of the hom-set $[X, Y]$ at its basepoint, hence canonically isomorphic. Composing,
> $$[\Sigma X, Y] \;\cong\; \Omega[X, Y]_0 \;\cong\; [X, \Omega Y],$$
> naturally in $X$ and $Y$.
>
> **Step 4 — unit, counit, triangle identities.** A natural hom-set bijection is an adjunction. Define $\eta_X : X \to \Omega\Sigma X$ as the image of $\mathrm{id}_{\Sigma X} \in [\Sigma X, \Sigma X]$ under the bijection with $Y = \Sigma X$, and $\varepsilon_Y : \Sigma\Omega Y \to Y$ as the image of $\mathrm{id}_{\Omega Y} \in [\Omega Y, \Omega Y]$ under the bijection with $X = \Omega Y$. Naturality of the bijection forces the triangle identities $(\Omega\varepsilon)\circ(\eta\Omega) = \mathrm{id}_\Omega$ and $(\varepsilon\Sigma)\circ(\Sigma\eta) = \mathrm{id}_\Sigma$, the standard consequence of a natural hom-isomorphism. Hence $\Sigma \dashv \Omega$ as functors on $\mathrm{Ho}(\mathcal{C})$. $\blacksquare$
>
> **Companion form.** If $\mathcal{C}$ is a pointed simplicial model category, the cotensor and tensor by the simplicial circle $S^1 = \Delta^1/\partial\Delta^1$ give $\Sigma X \simeq X \wedge S^1$ and $\Omega Y \simeq \mathrm{Map}_*(S^1, Y)$ on bifibrant objects, and the bijection above is the derived form of the strict adjunction $-\wedge S^1 \dashv \mathrm{Map}_*(S^1, -)$.

---

# Cross-Field Exercise Suggestions

**The shift adjunction in the derived category.** In $D(R)$, identify $\Sigma = [1]$ (degree shift up) and $\Omega = [-1]$ (shift down), and verify the adjunction $[X[1], Y] \cong [X, Y[-1]]$ directly from the definition of the shift on chain complexes. Here the unit and counit are [[Def - Isomorphism|isomorphisms]] — the example where the suspension–loop adjunction is an *equivalence*, foreshadowing triangulation. The non-obvious recognition is that the degree shift, an utterly algebraic operation, is the same construction as topological suspension.

**Bott periodicity as a statement about $\Omega$.** In the stable homotopy category, $\Omega^2$ on the $K$-theory spectrum returns the same spectrum (complex Bott periodicity: $\Omega^2 KU \simeq KU$). This is a statement that the loop functor, iterated twice, is the identity on a particular object — a deep and surprising fixed point of $\Omega$. The suspension–loop adjunction is the formal framework in which "looping" is even an operation one can iterate and ask for periodicity of; the application is non-obvious because periodicity looks like an accident until placed in this adjoint setting.

**[[Def - Group|Group]] completion and loop spaces.** A topological monoid $M$ has a classifying space $BM$ with $\Omega BM \simeq M^{\mathrm{grp}}$, the group completion. Recognizing $\Omega B(-)$ as a composite of a loop functor with a delooping is an application of the adjunction's unit $M \to \Omega\Sigma M$-style maps. The non-obvious bridge is that "group completion" — an algebraic operation on monoids — is computed by looping, and the adjunction is what licenses moving the loop across the classifying-space construction.

---

# Bridges

- **[[Thm - The Puppe Cofiber and Fiber Sequences Agree]]** — the direct payoff. The bijection $[\Sigma X, Z] \cong [X, \Omega Z]$ is the exact isomorphism that identifies the long exact sequence from a [[Def - Cofiber and Fiber Sequence|cofiber sequence]] (which ends in $[\Sigma X, Z]$) with the one from the matching fiber sequence (which begins with $[X, \Omega Z]$). Without this adjunction the two long exact sequences would be unrelated; with it they are the same sequence read twice, agreeing up to sign.

- **[[Def - Adjunction|Adjunctions]] in general** — this is one. The suspension–loop adjunction is the homotopical instance of "colimit $\dashv$ diagonal $\dashv$ limit": $\Sigma$ is a derived colimit (left adjoint), $\Omega$ a derived limit (right adjoint), and the unit/counit are the derived versions of the universal cocone and cone. Every property of adjunctions — uniqueness of adjoints, preservation of (co)limits — applies, so for instance $\Omega$ (a right adjoint) preserves homotopy limits and $\Sigma$ preserves homotopy colimits.

- **[[Thm - The Homotopy Category of a Model Category|The homotopy category]]** — the stage. The adjunction lives on $\mathrm{Ho}(\mathcal{C})$, not $\mathcal{C}$, precisely because $\Sigma$ and $\Omega$ are derived functors; the construction of $\mathrm{Ho}(\mathcal{C})$ as the localization where weak equivalences become isomorphisms is what makes the choice-dependent cylinder and path constructions into honest functors that can be adjoint.

- **Quillen adjunctions and the smash–hom adjunction** — the source. In an enriched model category the strict adjunction $-\wedge S^1 \dashv \mathrm{Map}_*(S^1, -)$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]], and the suspension–loop adjunction is its derived form. This is the most computable route to the theorem and the one that gives the explicit formulas $\Sigma X = X \wedge S^1$, $\Omega Y = \mathrm{Map}_*(S^1, Y)$.

---

# Unlocked by This

> [!tip] Stable Model Categories and the Triangulated Shift *(from the next chapter)*
> When $\Sigma$ is an equivalence, the adjunction's unit and counit become isomorphisms and $\Omega = \Sigma^{-1}$. The model category is then **stable**, $\mathrm{Ho}(\mathcal{C})$ is **triangulated**, and the adjunction supplies the invertible shift functor that triangulated categories require. The suspension–loop adjunction is the precise structure that "stabilizes."

> [!tip] Loop Spaces as Group Objects and the Eckmann–Hilton Argument *(from algebraic topology)*
> The adjunction transports the co-group structure on $\Sigma X$ to a group structure on $\Omega Y$, making **loop spaces group objects up to homotopy** and **double loop spaces abelian**. This is the structural origin of the group structure on $\pi_n$ for $n \ge 1$ and its commutativity for $n \ge 2$ — the Eckmann–Hilton conclusion, read off the adjunction.
