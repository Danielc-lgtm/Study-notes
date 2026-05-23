---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Covering Space"
  - "Def - Universal Cover"
  - "Def - Deck Transformation Group"
  - "Def - Regular (Galois) Covering"
  - "Def - Normal Subgroup"
  - "Thm - Lifting Criterion for Continuous Maps"
tags: [geometry, algebraic-topology, topology, galois]
---

# Notation

$X$ is a path-connected, locally path-connected, semi-locally simply connected topological space with base point $x_0$. $\widetilde X$ is the universal cover with base point $\tilde x_0 \in p^{-1}(x_0)$. For a connected pointed cover $(\tilde X', \tilde x_0') \to (X, x_0)$, the associated subgroup is $H := p_*\pi_1(\tilde X', \tilde x_0') \leq \pi_1(X, x_0)$. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Statement

> **Theorem (Galois Correspondence for Covering Spaces).** Let $X$ be a path-connected, locally path-connected, semi-locally simply connected topological space with base point $x_0$, and let $\widetilde X \to X$ be its universal cover. There is a natural bijection
> $$
> \left\{ \begin{matrix} \text{isomorphism classes} \\ \text{of connected pointed covers} \\ (\tilde X', \tilde x_0') \to (X, x_0) \end{matrix} \right\}
> \;\;\longleftrightarrow\;\;
> \left\{ \begin{matrix} \text{subgroups} \\ H \leq \pi_1(X, x_0) \end{matrix} \right\}
> $$
> given by $(\tilde X', \tilde x_0') \mapsto H := p_*\pi_1(\tilde X', \tilde x_0')$ in one direction, and $H \mapsto (\widetilde X / H, \tilde x_0)$ in the other (where $H$ acts on $\widetilde X$ as a subgroup of the deck group $\pi_1(X, x_0)$).
>
> Under this bijection:
> 1. **Inclusion structure:** $\tilde X_1$ dominates $\tilde X_2$ (i.e., there is a covering $\tilde X_1 \to \tilde X_2$ over $X$) iff $H_1 \subseteq H_2$.
> 2. **Regular covers:** $(\tilde X', \tilde x_0')$ is a [[Def - Regular (Galois) Covering|regular cover]] iff $H$ is a [[Def - Normal Subgroup|normal subgroup]] of $\pi_1(X, x_0)$. The deck group is then $\pi_1(X, x_0) / H$.
> 3. **Universal cover:** corresponds to $H = \{1\}$, with deck group $\pi_1(X, x_0)$.
> 4. **Trivial cover ($X$ itself):** corresponds to $H = \pi_1(X, x_0)$.
> 5. **Number of sheets:** equals the index $[\pi_1(X, x_0) : H]$.

Unpointed covers correspond to **conjugacy classes** of subgroups.

This is the central structural theorem of the chapter — it converts a geometric classification problem (the covers of $X$) into a purely algebraic problem (the subgroup lattice of $\pi_1(X)$).

---

# Motivation

Once you know the fundamental group $\pi_1(X)$, you have access to a complete invariant of the covering-space theory of $X$: every connected cover is determined (up to base-point-preserving isomorphism) by a subgroup of $\pi_1(X)$, and every subgroup arises from a cover. The lattice of covers, with its operations of fibre products (intersections of subgroups) and dominations (subgroup inclusions), is *isomorphic* to the lattice of subgroups of $\pi_1(X)$ inverted.

This is the **Galois correspondence** of topology — named because it has exactly the structure of the Galois correspondence in field theory:
- field extensions $\leftrightarrow$ covers
- Galois group acting on the extension $\leftrightarrow$ deck group acting on the cover
- subextensions $\leftrightarrow$ intermediate covers
- subgroups of the Galois group $\leftrightarrow$ subgroups of $\pi_1$ (inverted)
- normal subgroups $\leftrightarrow$ regular (Galois) covers
- trivial subgroup $\leftrightarrow$ universal cover (= "algebraic closure")

The depth of the theorem is that the algebra captures *everything* about the geometry: not just the *number* of covers, but their domination relations, their automorphism groups, their fibre cardinalities, all readable off the subgroup lattice.

In practice, this theorem is the engine of two complementary moves: when computing $\pi_1$ is hard but constructing covers is easy (or vice versa), you can switch sides. For example, $\pi_1(\mathrm{SO}(3))$ is computed by exhibiting the universal cover $\mathrm{SU}(2) \cong S^3$ and observing its deck group is $\mathbb{Z}/2$; conversely, the classification of $k$-fold covers of a space with $\pi_1 = G$ is reduced to listing subgroups of $G$ of index $k$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare ("$X$ sufficiently nice with universal cover"), but the theorem can be deployed under disguises.

The first source is **knowledge of $\pi_1(X)$ alone**. With $\pi_1(X)$ in hand, you can classify all connected covers of $X$ without knowing anything about $X$ geometrically beyond its $\pi_1$. The bridge: $\pi_1(X) = G$ → subgroups of $G$ → covers of $X$. So once $\pi_1$ is computed (perhaps by Seifert-van Kampen), the entire covering theory is known abstractly.

The second source is **a specific simply-connected cover** $\widetilde X \to X$, *or* a known cover whose total space has a known $\pi_1$. From this, $\pi_1(X)$ is computable (as the deck group, if the cover is universal, or as the appropriate extension otherwise). The bridge: known cover + universal-cover criterion → $\pi_1$. So the Galois correspondence is also a *computational* tool, not just classificatory.

The third source is **a quotient by a free properly discontinuous group action** $X = \tilde X / \Gamma$. Such a quotient is a covering map; if $\tilde X$ is simply connected, then $\pi_1(X) = \Gamma$ and the cover is universal. The bridge: free + properly discontinuous + simply connected total space → universal cover → $\pi_1 = \Gamma$. This is how $\pi_1(T^n) = \mathbb{Z}^n$, $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$, $\pi_1$ of hyperbolic surfaces are all computed.

**Targets (Output Amplification)**

The conclusion is a structural bijection; combined with other tools, it amplifies into specific identifications.

The first combination is **with simple subgroup computation in well-known groups**: knowing $\pi_1(X)$ and the subgroup lattice of a familiar group gives the classification of covers. For $X = S^1$ with $\pi_1 = \mathbb{Z}$, subgroups are $n\mathbb{Z}$ for $n \geq 0$ — so covers of $S^1$ are exactly the $n$-fold covers ($z \mapsto z^n$) for finite $n$ and the universal cover $\mathbb{R} \to S^1$. Combined: Galois correspondence + subgroup lattice of $\mathbb{Z}$ = full classification.

The second combination is **with index computations**: the number of sheets of a cover equals the index of the subgroup. So $k$-sheeted covers of $X$ correspond to index-$k$ subgroups of $\pi_1(X)$. This is a finitary count when $\pi_1(X)$ is finite or when only finite-index subgroups are considered. Combined: Galois correspondence + subgroup index = sheet-counting tool.

The third combination is **with the normaliser-quotient formula**: the deck group of a (possibly non-regular) cover equals $N_{\pi_1}(H) / H$. Combined with subgroup analysis in specific groups, this lets you compute deck groups of non-universal covers. For regular covers (normal subgroups), this collapses to $\pi_1 / H$.

The fourth combination is **with the universal-covering-group construction** (in the Lie group case): for a connected Lie group $G$, the universal cover $\widetilde G$ inherits a Lie group structure with discrete central kernel $\pi_1(G)$. Combined with the Galois correspondence applied to $G$ as a topological space, this gives the classification of all Lie groups with a given Lie algebra. Combined: Galois correspondence + Lie-group-structure-lifting = "all groups with Lie algebra $\mathfrak{g}$ are quotients of the unique simply-connected one."

---

# Why Is It True

The intuition is that the universal cover **collects all the loops of $X$ into a simply-connected object**, and the deck group action records the loop-structure exactly. Every other cover is then obtained by quotienting away some of that structure.

**The bolded one-liner: the universal cover is a "principal $\pi_1$-bundle" — fibres are torsors for $\pi_1$ — and connected covers of $X$ are exactly the "associated bundles" $\widetilde X / H$ for $H \leq \pi_1$, with the subgroup determining which loop-classes are forgotten.**

The structure:

1. **Construction of cover from subgroup.** Given $H \leq \pi_1(X)$, the quotient $\widetilde X / H$ (where $H$ acts as the corresponding subgroup of $\pi_1$ = deck group of $\widetilde X$) is a topological space; the projection $\widetilde X / H \to X$ is a covering map. The fibre over $x_0$ is $\pi_1(X) / H$ (the coset space), with cardinality the index of $H$. So every subgroup gives a cover.

2. **Recovery of subgroup from cover.** Given a connected pointed cover $(\tilde X', \tilde x_0') \to X$, the image $p_*\pi_1(\tilde X', \tilde x_0') \leq \pi_1(X, x_0)$ is a subgroup. The lifting criterion guarantees this subgroup determines the cover up to base-point-preserving isomorphism.

3. **Bijection.** The maps cover → subgroup and subgroup → cover are mutual inverses, modulo verifying that $\widetilde X / H$ has the right $\pi_1$-subgroup, which is a calculation.

4. **Normal subgroups → regular covers.** $\widetilde X / H \to X$ is regular iff $H$ is normal, because the deck group $\mathrm{Deck}(\widetilde X / H) / X = N_{\pi_1}(H)/H$, and regularity means transitive action on fibres iff $N_{\pi_1}(H) = \pi_1$ iff $H$ is normal.

5. **Universal cover → trivial subgroup.** $\widetilde X / \{1\} = \widetilde X$, simply connected, deck group = $\pi_1 / \{1\} = \pi_1$.

The whole theorem is the universal cover + lifting criterion + a calculation of $\pi_1$ of the quotient $\widetilde X / H$. Each ingredient has been built up in the previous theorems.

---

# What Makes This Hard

The conceptual content is clean, but two technical points are easy to miss. **First**, the bijection is on *base-point-preserving* isomorphism classes. Without base points, two pointed covers can correspond to *conjugate* subgroups (because changing the base point in the fibre conjugates the subgroup by an element of $\pi_1$). So unpointed covers ↔ conjugacy classes of subgroups, not subgroups themselves. **Second**, the inverse construction $H \mapsto \widetilde X / H$ requires you to *know* the universal cover exists (which is why the three conditions on $X$ — path-connected, locally path-connected, semi-locally simply connected — are essential). **Third**, the bijection requires the lifting criterion to verify that two covers giving the same subgroup must be isomorphic; this is where the lifting criterion's depth is essential.

A common error: assuming the deck group of a cover equals $\pi_1(X) / p_*\pi_1(\tilde X)$ without verifying regularity. This quotient does not even make sense if $p_*\pi_1(\tilde X)$ is not normal. The correct formula in general is $\mathrm{Deck} = N_{\pi_1}(H)/H$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build the universal cover; for each subgroup $H \leq \pi_1(X)$, construct the quotient $\widetilde X / H$ as a cover; verify that the resulting cover has $\pi_1$-image exactly $H$; conversely, given a cover, identify its $\pi_1$-image, lift the identity through the universal cover, and recover the cover as a quotient.

**Subgoal decomposition:**

1. **The universal cover exists.** $\widetilde X$ exists by the standard construction (homotopy classes of paths from $x_0$), provided $X$ is path-connected, locally path-connected, semi-locally simply connected.
   - *Hint:* Pre-built construction; see [[Def - Universal Cover]].
   - *Why needed:* The bijection's source.

2. **Subgroup $\to$ cover.** For $H \leq \pi_1(X)$, the deck-group action gives an action of $H$ on $\widetilde X$ (as a subgroup of $\mathrm{Deck}(\widetilde X / X) = \pi_1(X)$). The quotient $\widetilde X / H$ is a topological space, and the map $\widetilde X / H \to X$ is a covering with fibre $\pi_1(X)/H$.
   - *Hint:* Verify that the $H$-action is free properly discontinuous, so the quotient is a manifold/CW complex with cover structure.
   - *Why needed:* The construction direction.

3. **The new cover has $\pi_1$-image $H$.** Compute $\pi_1(\widetilde X / H)$ and verify the image of $p_*$ is $H$.
   - *Hint:* The map $\widetilde X \to \widetilde X / H$ is itself a cover with deck group $H$; loops in $\widetilde X / H$ lift to paths in $\widetilde X$ ending in the $H$-orbit, projecting down to loops in $X$ classified by elements of $H$.
   - *Why needed:* Inverse of step 4.

4. **Cover $\to$ subgroup.** Given $(\tilde X', \tilde x_0')$ a connected pointed cover, set $H := p_*\pi_1(\tilde X', \tilde x_0')$.
   - *Hint:* Obvious by definition.
   - *Why needed:* The reverse direction.

5. **Bijection.** Steps 2 and 4 are mutual inverses up to base-point-preserving isomorphism: $\tilde X' \cong \widetilde X / H$ via the lifting criterion (lift $\mathrm{id}_X : X \to X$ through $\tilde X'$; the lift is a covering $\widetilde X \to \tilde X'$ whose deck group is $H$, so $\tilde X' = \widetilde X / H$).
   - *Hint:* Lifting criterion applied to the universal cover $\widetilde X \to X$ through $\tilde X' \to X$.
   - *Why needed:* The bijection structure.

6. **Normality ↔ regularity.** $H$ is normal iff the deck group of $\widetilde X / H \to X$ is $\pi_1(X)/H$, transitive on each fibre.
   - *Hint:* Compute $\mathrm{Deck}(\widetilde X / H \to X) = N_{\pi_1(X)}(H)/H$; transitive on fibre = $\pi_1(X)$ acts via $\pi_1(X)/H$ on the fibre.
   - *Why needed:* Refinement of the bijection.

---

# Lemma Decomposition

> [!note]- Lemma 1: $H \leq \pi_1(X)$ acts freely and properly discontinuously on $\widetilde X$
> **Statement:** Any subgroup $H \leq \pi_1(X) = \mathrm{Deck}(\widetilde X / X)$ acts on $\widetilde X$ freely (no fixed points except identity) and properly discontinuously (each point has a neighbourhood disjoint from its $H$-translates by non-identity elements).
>
> **Hint:** Inherit from the deck-group action of $\pi_1(X)$, which is free and properly discontinuous on the universal cover.
>
> **Why needed:** Makes the quotient $\widetilde X / H$ a manifold/CW complex and the projection a covering map.
>
> > [!note]- Full proof
> > The full deck group $\pi_1(X)$ acts on $\widetilde X$ freely (a non-identity deck transformation has no fixed point — any fixed point would force the transformation to be the identity by uniqueness of lifts) and properly discontinuously (each point has a neighbourhood in an evenly covered preimage, hence disjoint from its non-trivial translates). Any subgroup $H \leq \pi_1(X)$ inherits both properties: $H$-orbits are contained in $\pi_1(X)$-orbits, so $H$-action is also free and properly discontinuous.

> [!note]- Lemma 2: $\widetilde X / H$ is a covering space of $X$
> **Statement:** The quotient $\widetilde X / H$ is a topological space, and the natural projection $\widetilde X / H \to X$ (induced by $\widetilde X \to X$) is a covering map. The fibres have cardinality $|\pi_1(X)/H| = [\pi_1(X) : H]$.
>
> **Hint:** Free properly discontinuous actions on covers descend to covers, with the quotient by $H$ inheriting the covering structure.
>
> **Why needed:** Constructs the cover from a subgroup.
>
> > [!note]- Full proof
> > Since $H$ acts freely properly discontinuously, $\widetilde X / H$ is Hausdorff and the quotient map $q : \widetilde X \to \widetilde X / H$ is a covering map with deck group $H$. The composition $p \circ s^{-1}$ where $s$ is a local section of $q$ provides local trivializations for $\widetilde X / H \to X$ (using evenly covered neighbourhoods of $X$ from $\widetilde X \to X$). The fibre over $x \in X$ is $p^{-1}(x)/H = \pi_1(X)/H$ as $H$-cosets in the fibre of $\widetilde X$, hence has cardinality $[\pi_1(X) : H]$.

> [!note]- Lemma 3: $p_*\pi_1(\widetilde X / H) = H$
> **Statement:** Let $\tilde X' := \widetilde X / H$, with base point $\tilde x_0' := H \cdot \tilde x_0$ (the $H$-orbit). Then $p_*\pi_1(\tilde X', \tilde x_0') = H$ as a subgroup of $\pi_1(X, x_0)$.
>
> **Hint:** A loop $\tilde\gamma'$ in $\tilde X'$ at $\tilde x_0'$ lifts (via $q : \widetilde X \to \tilde X'$) to a path in $\widetilde X$ starting at $\tilde x_0$ and ending in the $H$-orbit $H \cdot \tilde x_0$. Projecting down to $X$ gives a loop classified by an element of $H$ (since the endpoint differs from $\tilde x_0$ by an element of $H \leq \pi_1(X) =$ fibre).
>
> **Why needed:** Verifies that the cover-construction inverts subgroup-extraction.
>
> > [!note]- Full proof
> > A loop $\tilde\gamma'$ in $\tilde X' = \widetilde X / H$ at $\tilde x_0'$ lifts uniquely (via $q : \widetilde X \to \tilde X'$, which is a cover with deck group $H$) to a path $\tilde\gamma$ in $\widetilde X$ starting at $\tilde x_0$. The endpoint $\tilde\gamma(1)$ lies in $q^{-1}(\tilde x_0') = H \cdot \tilde x_0$, so $\tilde\gamma(1) = h \cdot \tilde x_0$ for some $h \in H$. Now $p \circ \tilde\gamma$ is a loop in $X$ at $x_0$; its homotopy class corresponds (via the universal-cover identification $\pi_1(X) =$ fibre $p^{-1}(x_0)$) to the deck transformation taking $\tilde x_0$ to $\tilde\gamma(1) = h \cdot \tilde x_0$, which is exactly $h \in H$. So $p_*[\tilde\gamma'] = h \in H$, giving $p_*\pi_1(\tilde X', \tilde x_0') \subseteq H$.
> >
> > Conversely, any $h \in H$ corresponds to a loop $\gamma$ in $X$ at $x_0$ whose lift to $\widetilde X$ starting at $\tilde x_0$ ends at $h \cdot \tilde x_0 \in H \cdot \tilde x_0$. Projecting that lift via $q$ gives a loop in $\tilde X'$ at $\tilde x_0'$. So $H \subseteq p_*\pi_1(\tilde X', \tilde x_0')$.

> [!note]- Lemma 4: Cover ↔ Subgroup is a bijection
> **Statement:** The maps $(\tilde X', \tilde x_0') \mapsto H := p_*\pi_1(\tilde X', \tilde x_0')$ and $H \mapsto (\widetilde X / H, H \cdot \tilde x_0)$ are mutual inverses on isomorphism classes of pointed connected covers.
>
> **Hint:** Lemma 3 gives "cover $\to$ subgroup $\to$ cover = identity." For the other direction, lift the identity $X \to X$ through $\tilde X'$ to a covering map $\widetilde X \to \tilde X'$ using the lifting criterion; show $\tilde X'$ is the quotient $\widetilde X / H$.
>
> **Why needed:** Establishes the bijection.
>
> > [!note]- Full proof
> > ($H \to \widetilde X / H \to H$) By Lemma 3.
> >
> > ($\tilde X' \to H \to \widetilde X / H$) Given $\tilde X'$ with $H := p_*\pi_1(\tilde X')$. By the lifting criterion applied to $\widetilde X \to X$ and the cover $\tilde X' \to X$: the universal cover $\widetilde X$ has $\pi_1 = 0$, so $0 \subseteq p_*\pi_1(\tilde X') = H$, and the lift $\tilde X' \to X$ to a map $\widetilde X \to \tilde X'$ exists (with prescribed base point). This lift is a covering map (by general covering-space theory). Its deck group is exactly $H$ (since it is the kernel of $\widetilde X \to \tilde X' \to X$ on $\pi_1$-level, modulo the trivial $\pi_1(\widetilde X) = 0$). So $\tilde X' \cong \widetilde X / H$.

> [!note]- Lemma 5: Regular cover ↔ normal subgroup
> **Statement:** $(\widetilde X / H \to X)$ is a [[Def - Regular (Galois) Covering|regular cover]] iff $H$ is normal in $\pi_1(X)$. The deck group is then $\pi_1(X)/H$.
>
> **Hint:** Regularity means the deck group acts transitively on each fibre, which requires the deck group to be at least as big as the fibre ($\pi_1(X)/H$); the deck group is exactly $N_{\pi_1(X)}(H)/H$, which equals $\pi_1(X)/H$ iff $N_{\pi_1(X)}(H) = \pi_1(X)$ iff $H$ is normal.
>
> **Why needed:** Refines the bijection to the regular subset.
>
> > [!note]- Full proof
> > $\mathrm{Deck}(\widetilde X / H \to X) = N_{\pi_1(X)}(H)/H$ (a deck transformation of $\widetilde X / H$ must come from a self-map of $\widetilde X$ commuting with $H$-action and with the projection to $X$; this is precisely an element of $N_{\pi_1(X)}(H)$ modulo $H$). The fibre of $\widetilde X / H \to X$ has cardinality $[\pi_1(X) : H]$; the deck group acts transitively on the fibre iff $|\mathrm{Deck}| =$ fibre size, i.e., $|N_{\pi_1(X)}(H)/H| = [\pi_1(X) : H]$, i.e., $N_{\pi_1(X)}(H) = \pi_1(X)$, i.e., $H \trianglelefteq \pi_1(X)$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem (Galois Correspondence for Covering Spaces).** As stated.
>
> *Proof.*
>
> **Step 0:** $X$ path-connected, locally path-connected, semi-locally simply connected; universal cover $\widetilde X \to X$ exists ([[Def - Universal Cover]]), with deck group $\pi_1(X, x_0)$.
>
> **Step 1 (subgroup → cover):** For $H \leq \pi_1(X)$, by Lemma 1, $H$ acts freely properly discontinuously on $\widetilde X$, so by Lemma 2 the quotient $\widetilde X / H$ is a topological space with covering map $\widetilde X / H \to X$ and fibres of cardinality $[\pi_1(X) : H]$.
>
> **Step 2 (cover → subgroup):** For a connected pointed cover $(\tilde X', \tilde x_0')$, set $H := p_*\pi_1(\tilde X', \tilde x_0')$.
>
> **Step 3 (bijection):** By Lemma 4, the maps in Step 1 and Step 2 are mutual inverses.
>
> **Step 4 (inclusion structure):** $\tilde X_1$ dominates $\tilde X_2$ iff there is a covering $\tilde X_1 \to \tilde X_2$ over $X$. By the lifting criterion applied to $\tilde X_1 \to X$ and the cover $\tilde X_2 \to X$: the lift exists iff $p_{1*}\pi_1(\tilde X_1) \subseteq p_{2*}\pi_1(\tilde X_2)$, i.e., $H_1 \subseteq H_2$. So domination ↔ subgroup inclusion.
>
> **Step 5 (regular ↔ normal):** Lemma 5.
>
> **Step 6 (universal cover ↔ trivial subgroup):** $\widetilde X = \widetilde X / \{1\}$, with $H = \{1\}$. Deck group $\pi_1(X)/\{1\} = \pi_1(X)$.
>
> **Step 7 (number of sheets):** Fibre cardinality is $[\pi_1(X) : H]$ by Lemma 2.
>
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Galois theory: classifying intermediate fields of $\mathbb{Q}(\sqrt[3]{2}, \omega)/\mathbb{Q}$.** The splitting field of $x^3 - 2$ over $\mathbb{Q}$ has Galois group $S_3$. Subgroups of $S_3$ — $\{1\}, A_3, \langle (12) \rangle, \langle (13) \rangle, \langle (23) \rangle, S_3$ — correspond to intermediate fields, exactly parallel to how the Galois correspondence for covers identifies subgroups with intermediate covers. The normal subgroups $\{1\}, A_3, S_3$ correspond to normal extensions; the non-normal subgroups correspond to non-Galois extensions. The structural parallel is the *content* of the Galois correspondence for covers — Grothendieck's étale fundamental group makes this an actual equivalence.

**Lie theory: classifying connected Lie groups with Lie algebra $\mathfrak{su}(2)$.** The simply-connected Lie group with Lie algebra $\mathfrak{su}(2)$ is $\mathrm{SU}(2) \cong S^3$. Its discrete normal subgroups are subgroups of the centre $Z(\mathrm{SU}(2)) = \{\pm I\}$ — either trivial or all of it. By the Galois correspondence applied to the universal-covering-group construction, the connected Lie groups with this algebra are $\mathrm{SU}(2)$ and $\mathrm{SU}(2)/\{\pm I\} = \mathrm{SO}(3) \cong \mathbb{RP}^3$ — exactly two groups, classified by subgroups of $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$. See [[Ex - SU(2) is the Universal Cover of SO(3)]].

**Number theory: classifying abelian extensions of $\mathbb{Q}_p$.** Local class field theory states that abelian extensions of a local field $\mathbb{Q}_p$ correspond to subgroups of $\mathbb{Q}_p^\times$ (modulo a certain norm subgroup). The topological version of this is the Galois correspondence applied to $\pi_1^{\mathrm{ét}}(\mathrm{Spec}\,\mathbb{Q}_p) = \mathrm{Gal}(\bar{\mathbb{Q}_p}/\mathbb{Q}_p)$, with the abelianization being $\mathbb{Q}_p^\times$ (local Artin reciprocity).

**Geometric topology: classifying covers of a surface.** The fundamental group of a closed orientable surface of genus $g \geq 2$ is $\pi_1(\Sigma_g) = \langle a_1, b_1, \dots, a_g, b_g \mid \prod [a_i, b_i] \rangle$. Subgroup classification of this surface group gives the classification of all covers of $\Sigma_g$. Finite-index subgroups correspond to finite-sheeted covers, which are themselves surfaces of genus determined by the Riemann-Hurwitz formula. The structure is incredibly rich and is the subject of teichmüller theory.

---

# Bridges

- **[[Def - Universal Cover]]** — the universal cover is the *generator* of the entire bijection. Without the universal cover existing, the correspondence has nothing to live on. The three sufficient conditions on $X$ (path-connected, locally path-connected, semi-locally simply connected) are precisely what guarantee the universal cover exists, and hence the Galois correspondence applies.

- **[[Thm - Lifting Criterion for Continuous Maps]]** — the critical technical input. The lifting criterion is what lets you (a) verify the cover ↔ subgroup bijection is well-defined and inverts properly, and (b) show that two covers with the same subgroup must be isomorphic. Without the lifting criterion, the correspondence cannot be proved.

- **Field-theoretic Galois correspondence** — the parallel structure is exact. In field theory, $L/K$ Galois ↔ $\mathrm{Aut}(L/K)$ acts with fixed field $K$. In topology, $\tilde X \to X$ regular ↔ deck group acts with quotient $X$. The normal subgroups in each setting correspond to "intrinsic" subobjects (Galois subextensions, regular subcovers), the non-normal ones to "embedded" subobjects (general subextensions, general subcovers). Grothendieck's étale fundamental group makes the parallel literal: $\pi_1^{\mathrm{ét}}(\mathrm{Spec}\,K) = \mathrm{Gal}(\bar K / K)$, and étale covers ↔ field extensions.

- **[[Def - Deck Transformation Group]]** — the deck group is the *acting group* in the Galois correspondence. The bijection between covers and subgroups also gives a bijection between subgroups of the deck group $\pi_1(X)$ (acting on the universal cover) and quotients of the universal cover — which are exactly the covers. So the deck group of the universal cover is both the "Galois group" of the universal cover (over $X$) and the indexing object for all covers.

- **Profinite completion and étale $\pi_1$** — the Galois correspondence above classifies *all* connected covers, including infinite-sheeted. For algebraic geometry, where one wants only *finite* covers, the relevant group is the profinite completion $\widehat{\pi_1(X)}$, which classifies finite étale covers. The étale fundamental group is automatically profinite, and the étale Galois correspondence is a profinite version of the topological one.
