---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Quasi-Category"
  - "Def - Kan Complex and the Nerve"
  - "Def - Category"
  - "Def - Groupoid"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$\mathcal{D}$ is a [[Def - Quasi-Category|quasi-category]]: a [[Def - Simplicial Set|simplicial set]] with inner-horn fillers. Its $0$-simplices are **objects**, its $1$-simplices **morphisms**. Two parallel morphisms $f, g : x \to y$ are **homotopic** ($f \simeq g$) if there is a $2$-simplex $\sigma$ with $d_2\sigma = f$, $d_1\sigma = g$, $d_0\sigma = \mathrm{id}_y = s_0 y$. We write $[f]$ for the homotopy class. The **homotopy category** is $\mathrm{ho}(\mathcal{D})$. The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

---

# Statement

> **Theorem (Homotopy category).** Let $\mathcal{D}$ be a [[Def - Quasi-Category|quasi-category]]. There is an ordinary [[Def - Category|category]] $\mathrm{ho}(\mathcal{D})$, the **homotopy category**, with:
> - objects the $0$-simplices $\mathcal{D}_0$;
> - morphisms $x \to y$ the **homotopy classes** $[f]$ of $1$-simplices $f : x \to y$ (homotopy is an equivalence relation on each set of parallel morphisms);
> - composition $[g] \circ [f] = [h]$, where $h = d_1\sigma$ for *any* $2$-simplex $\sigma$ with $d_2\sigma = f$, $d_0\sigma = g$ (such $\sigma$ exists by inner-horn filling, and $[h]$ is independent of the choice);
> - identities $[\,\mathrm{id}_x\,] = [s_0 x]$.

> **Corollary 1.** For an ordinary category $\mathcal{C}$, $\mathrm{ho}(N(\mathcal{C})) \cong \mathcal{C}$ — the homotopy category of a [[Def - Kan Complex and the Nerve|nerve]] recovers the original category (composites are already unique, so homotopy classes are singletons).

> **Corollary 2.** If $\mathcal{D}$ is a [[Def - Kan Complex and the Nerve|Kan complex]] (an $\infty$-groupoid), then $\mathrm{ho}(\mathcal{D})$ is a [[Def - Groupoid|groupoid]] — every morphism is invertible. In particular $\mathrm{ho}(\mathrm{Sing}\,Y) = \Pi_1(Y)$, the fundamental groupoid of a space $Y$.

---

# Motivation

A quasi-category has, in general, no single composite of two morphisms — only a contractible space of candidate composites, encoded by the many fillers of an inner horn. This is exactly the structure that makes $\infty$-categories powerful, but it is also more than you often need. Frequently you want the ordinary-categorical shadow: objects, morphisms, and a single well-defined composite — the data you would write on a blackboard. The homotopy category is that shadow. It throws away all the higher cells and remembers morphisms only up to homotopy, restoring single-valued composition at the cost of forgetting the homotopies that witnessed the non-uniqueness.

The theorem is the assertion that this throwing-away is *coherent* — that the result really is a category. The danger is real: composition is defined by *choosing* a $2$-simplex filling an inner horn, and there are many such fillers, so one must check the homotopy class of the composite does not depend on the choice. That it does not is precisely what the higher inner fillers guarantee, and it is the technical heart of the theorem. Once it holds, $\mathrm{ho}$ becomes the bridge that lets ordinary-categorical intuition survive into the $\infty$-world: $\mathrm{ho}(N\mathcal{C}) = \mathcal{C}$ says categories are unchanged, and $\mathrm{ho}(\mathrm{Sing}\,Y) = \Pi_1(Y)$ says spaces give their fundamental groupoid. It is the functor that connects the new homotopy-coherent world back to the familiar one.

---

# Sources and Targets

**Sources (Input Broadening)**

The input is any quasi-category, so the source question is *when you want to extract ordinary-categorical data from a homotopy-coherent structure.*

The first disguised source is **a space**. Applying $\mathrm{ho}$ to $\mathrm{Sing}(Y)$ yields the [[Def - Path-Product and the Fundamental Group|fundamental groupoid]] $\Pi_1(Y)$, and the automorphism group of a point is $\pi_1(Y)$. The non-obvious step is that $\mathrm{Sing}(Y)$ is a Kan complex, so by Corollary 2 the homotopy category is a groupoid — every path is invertible up to homotopy. *Example problem:* compute $\pi_1(S^1)$ as automorphisms of a vertex in $\mathrm{ho}(\mathrm{Sing}\,S^1)$.

The second disguised source is **an ordinary category presented simplicially**. If a quasi-category turns out to have unique fillers, $\mathrm{ho}$ returns it unchanged; recognising this lets you check "is my $\infty$-category really a $1$-category?". The non-obvious bridge is the [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterisation]]: unique fillers ⟺ nerve ⟺ homotopy classes are singletons. *Example problem:* verify $\mathrm{ho}(N\mathcal{C}) \cong \mathcal{C}$ and conclude $\mathrm{ho}$ is a retraction onto $\mathbf{Cat}$.

The third disguised source is **a derived or stable $\infty$-category**. The homotopy category of a stable $\infty$-category is a [[Thm - Strictification of Bicategories|triangulated]] category; $\mathrm{ho}$ is how one passes from the well-behaved $\infty$-category to the classical (but defective) triangulated one. The non-obvious recognition is that the *failures* of triangulated categories (non-functorial cones) are exactly the higher data that $\mathrm{ho}$ discards. *Example problem:* see why the cone in $\mathrm{ho}$ of a stable $\infty$-category is only defined up to non-canonical isomorphism (the §H.5 motivation).

**Targets (Output Amplification)**

Combine $\mathrm{ho}$ with the **Kan condition** to get a groupoid. The conclusion that $\mathrm{ho}(\mathcal{D})$ is a category, combined with "$\mathcal{D}$ is Kan", gives that every morphism of $\mathrm{ho}(\mathcal{D})$ is invertible. The further result is that an $\infty$-groupoid's homotopy category is a [[Def - Groupoid|groupoid]] — the $1$-truncation of a space — recovering classical low-dimensional homotopy theory. Non-obvious because invertibility is *produced* by outer-horn filling, not assumed.

Combine $\mathrm{ho}$ with the **embedding $N$** to exhibit $\mathbf{Cat}$ as a reflective shadow. The conclusion $\mathrm{ho}(N\mathcal{C}) \cong \mathcal{C}$, combined with full faithfulness of $N$ ([[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve theorem]]), gives that $\mathrm{ho} : \infty\text{-}\mathbf{Cat} \to \mathbf{Cat}$ is left adjoint to $N$ — the universal way to extract a $1$-category from an $\infty$-category. The further result is that any functor from an $\infty$-category to an ordinary category factors through $\mathrm{ho}$. Non-obvious because it makes $\mathrm{ho}$ the *initial* ordinary-categorical approximation.

Combine $\mathrm{ho}$ with **homotopy groups**. For a pointed Kan complex, the morphisms of $\mathrm{ho}$ from the basepoint to itself are $\pi_1$; combined with the higher simplicial homotopy groups, the further result is the **Postnikov/truncation tower**, of which $\mathrm{ho}$ is the bottom ($1$-truncation) layer. Non-obvious because it situates $\mathrm{ho}$ as one stage of a systematic dismantling of the homotopy type.

---

# Why Is It True

The only thing in doubt is well-definedness of composition; everything else is routine. So focus there. Composition is defined by: given $f : x \to y$ and $g : y \to z$, fill the inner horn $\Lambda^2_1$ they form to get a $2$-simplex $\sigma$, and declare $[g]\circ[f] = [d_1\sigma]$. Two choices enter — the representatives $f, g$ within their homotopy classes, and the filler $\sigma$ — and we must show neither affects $[d_1\sigma]$.

Here is the mechanism. Suppose $\sigma$ and $\sigma'$ are two fillers of the *same* horn $(f, g)$, with long edges $h = d_1\sigma$ and $h' = d_1\sigma'$. Build a $3$-simplex problem: the two triangles $\sigma, \sigma'$ together with a degenerate triangle on $g$ assemble into an *inner* $3$-horn $\Lambda^3_1$ (the faces are $\sigma$, $\sigma'$, a degeneracy, and the missing inner face). Filling this inner horn — which the quasi-category condition allows — produces a $3$-simplex whose remaining face is a $2$-simplex exhibiting $h \simeq h'$. So **any two composites of the same pair are homotopic, because a single inner $3$-horn-filler witnesses their homotopy.** The same kind of argument, replacing $f$ or $g$ by a homotopic representative, shows the class $[d_1\sigma]$ is unchanged. Associativity is the analogous statement one dimension up: two ways of composing three morphisms are exhibited as faces of a $4$-simplex obtained by inner-horn filling, hence are homotopic. In one phrase: **the higher inner fillers are exactly the homotopies that make the composition well-defined, associative, and unital on homotopy classes — uniqueness is recovered after quotienting by homotopy.**

For Corollary 1: in a [[Def - Kan Complex and the Nerve|nerve]] $N(\mathcal{C})$, inner horns fill *uniquely*, so the composite $2$-simplex is unique, its long edge is the genuine composite $g\circ f$, and homotopy is trivial (two parallel edges are homotopic only if equal). Hence $\mathrm{ho}(N\mathcal{C})$ has the same morphisms and composition as $\mathcal{C}$: $\mathrm{ho}(N\mathcal{C}) \cong \mathcal{C}$.

For Corollary 2: if $\mathcal{D}$ is Kan, *outer* horns fill too. Given $[f] : x \to y$, fill the outer horn $\Lambda^2_0$ formed by $f$ and $\mathrm{id}_x$ to produce an edge $g : y \to x$ with $[g]\circ[f] = [\mathrm{id}_x]$, i.e. a left inverse; symmetrically a right inverse. So every morphism of $\mathrm{ho}(\mathcal{D})$ is invertible — $\mathrm{ho}(\mathcal{D})$ is a [[Def - Groupoid|groupoid]]. **Outer-horn filling is exactly the production of inverses, so Kan $\Rightarrow$ groupoid.**

---

# What Makes This Hard

The hard step is well-definedness of composition, and specifically the construction of the *correct inner $3$-horn* whose filler witnesses that two composites are homotopic. The non-obvious move is assembling the right combination of faces — two genuine $2$-simplices plus degeneracies — into a horn that is *inner* (so it can be filled) and whose missing face is the homotopy you want. Beginners either skip well-definedness entirely (treating "the composite" as if it were unique, which it is not) or attempt to fix a canonical filler (which is not possible without extra structure). The other common error is conflating the two corollaries' mechanisms: composition's well-definedness uses *inner* $3$-horns, while invertibility in the Kan case uses *outer* $2$-horns — different horns doing different jobs.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Define homotopy of morphisms and show it is an equivalence relation via inner-horn fillers. Define composition by filling $\Lambda^2_1$ and prove the homotopy class of the long edge is independent of representatives and filler, using an inner $\Lambda^3_1$-filler as the witnessing homotopy. Get associativity from a $4$-simplex and units from degeneracies. Then specialise to nerves (unique fillers) and Kan complexes (outer fillers give inverses).

**Subgoal decomposition:**

1. **Homotopy is an equivalence relation.** Show $\simeq$ on parallel morphisms is reflexive, symmetric, transitive.
   - *Hint:* Reflexivity from a degenerate $2$-simplex; symmetry and transitivity from inner-horn fillers.
   - *Why needed:* The morphism sets of $\mathrm{ho}$ are the quotient by $\simeq$.

2. **Composition exists.** Show every composable pair has a composite.
   - *Hint:* Fill the inner horn $\Lambda^2_1$ formed by $f$ and $g$; the long edge is a composite.
   - *Why needed:* Composition must be total.

3. **Composition is well-defined on classes.** Show $[d_1\sigma]$ is independent of the filler $\sigma$ and of the representatives.
   - *Hint:* Two fillers of the same horn assemble into an inner $\Lambda^3_1$ whose filler exhibits their long edges as homotopic.
   - *Why needed:* This is the crux — without it $\mathrm{ho}$ is not a category.

4. **Associativity and units.** Show composition is associative and that $[s_0 x]$ is a two-sided unit.
   - *Hint:* Associativity from an inner $\Lambda^4_\bullet$-filler; units from degenerate $2$-simplices.
   - *Why needed:* The remaining category axioms.

5. **Corollaries.** Nerve: unique fillers make classes singletons, so $\mathrm{ho}(N\mathcal{C})\cong\mathcal{C}$. Kan: outer fillers give inverses, so $\mathrm{ho}$ is a groupoid.
   - *Hint:* For inverses fill the outer horn $\Lambda^2_0$ of $f$ and $\mathrm{id}_x$.
   - *Why needed:* The two named special cases.

---

# Lemma Decomposition

> [!note]- Lemma 1: Homotopy of morphisms is an equivalence relation
> **Statement:** On parallel $1$-simplices $f, g : x \to y$ in a quasi-category, the relation $f \simeq g$ (a $2$-simplex $\sigma$ with $d_2\sigma = f$, $d_1\sigma = g$, $d_0\sigma = \mathrm{id}_y$) is reflexive, symmetric, and transitive.
>
> **Hint:** Reflexivity: $s_1 f$. Symmetry and transitivity: build inner $2$- or $3$-horns from the given homotopies and fill.
>
> **Why needed:** Without it, "homotopy class" is meaningless and $\mathrm{ho}$ has no morphism sets.
>
> > [!note]- Full proof
> > *Reflexive:* the degenerate $2$-simplex $s_1 f$ has $d_2 = f$, $d_1 = f$, $d_0 = s_0 y = \mathrm{id}_y$, so $f \simeq f$. *Symmetric/transitive:* given homotopies as $2$-simplices, assemble an inner horn ($\Lambda^2_1$ for the composite of homotopy-witnessing triangles, or $\Lambda^3_1$ when chaining three) and fill; the resulting face is the required homotopy. (One uses that $\mathrm{id}_y$ behaves as a unit up to homotopy, itself a degenerate-simplex computation.) Hence $\simeq$ is an equivalence relation.

> [!note]- Lemma 2: Composition is independent of the chosen filler
> **Statement:** If $\sigma, \sigma'$ are two $2$-simplices with $d_2 = f$, $d_0 = g$ (fillers of the same inner $2$-horn), then $d_1\sigma \simeq d_1\sigma'$.
>
> **Hint:** The faces $\sigma$, $\sigma'$, and a degeneracy on $g$ form an inner horn $\Lambda^3_1$; its filler's remaining face is a homotopy $d_1\sigma \simeq d_1\sigma'$.
>
> **Why needed:** It is exactly the well-definedness of composition on homotopy classes.
>
> > [!note]- Full proof
> > Consider a $3$-simplex with vertices $x, y, z$ and a repeated vertex, whose faces $d_3, d_0, d_2$ are prescribed to be $\sigma$, the degeneracy $s_0 g$ (or an appropriate degenerate triangle), and $\sigma'$, leaving $d_1$ free — this is an inner horn $\Lambda^3_1$. Filling it (quasi-category condition) yields a $3$-simplex; its $d_1$ face is a $2$-simplex with edges $d_1\sigma$, $d_1\sigma'$, and $\mathrm{id}$, exhibiting $d_1\sigma \simeq d_1\sigma'$. Replacing $f$ or $g$ by homotopic representatives is handled by the same construction with the homotopy triangles inserted, so the composite class depends only on $[f], [g]$.

> [!note]- Lemma 3: Outer-horn filling produces inverses
> **Statement:** In a [[Def - Kan Complex and the Nerve|Kan complex]] $\mathcal{D}$, every morphism $f : x \to y$ has a homotopy inverse, so $\mathrm{ho}(\mathcal{D})$ is a [[Def - Groupoid|groupoid]].
>
> **Hint:** Fill the outer horn $\Lambda^2_0$ given by $f : x \to y$ (the edge $01$) and $\mathrm{id}_x : x \to x$ (the edge $02$) to get an edge $y \to x$.
>
> **Why needed:** It is Corollary 2 and the reason Kan complexes are $\infty$-groupoids.
>
> > [!note]- Full proof
> > The outer horn $\Lambda^2_0 \to \mathcal{D}$ with $d_2 = f$ ($x \to y$) and $d_1 = \mathrm{id}_x$ ($x \to x$) has, in a Kan complex, a filler $\sigma$; its face $d_0\sigma$ is an edge $g : y \to x$ with $[g]\circ[f] = [\mathrm{id}_x]$, a left inverse. The symmetric outer horn $\Lambda^2_2$ gives a right inverse. By the usual argument left and right inverses agree up to homotopy, so $[f]$ is invertible in $\mathrm{ho}(\mathcal{D})$. Hence $\mathrm{ho}(\mathcal{D})$ is a groupoid.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — homotopy classes.** By Lemma 1, $\simeq$ is an equivalence relation on each set of parallel $1$-simplices, so $\mathrm{ho}(\mathcal{D})(x,y) := \{1\text{-simplices } x \to y\}/\simeq$ is well-defined.
>
> **Step 1 — composition exists.** Given $f : x \to y$, $g : y \to z$, the inner horn $\Lambda^2_1 \to \mathcal{D}$ with $d_2 = f$, $d_0 = g$ has a filler $\sigma$ (quasi-category axiom); set $[g]\circ[f] := [d_1\sigma]$.
>
> **Step 2 — composition is well-defined.** By Lemma 2, $[d_1\sigma]$ is independent of the filler $\sigma$ and of the representatives $f, g$. So $\circ$ is a well-defined operation on homotopy classes.
>
> **Step 3 — units.** The degenerate $2$-simplices $s_0$ and $s_1$ exhibit $[s_0 x] = [\mathrm{id}_x]$ as a two-sided unit: $[f]\circ[\mathrm{id}_x] = [f] = [\mathrm{id}_y]\circ[f]$, each by filling the relevant horn with a degeneracy.
>
> **Step 4 — associativity.** For $w \xrightarrow{f} x \xrightarrow{g} y \xrightarrow{h} z$, the two bracketings $([h]\circ[g])\circ[f]$ and $[h]\circ([g]\circ[f])$ appear as $d_1$-faces of a $3$-simplex obtained by filling an inner $\Lambda^3_\bullet$-horn assembled from the composing $2$-simplices; hence they are homotopic, i.e. equal in $\mathrm{ho}(\mathcal{D})$. So $\mathrm{ho}(\mathcal{D})$ is a [[Def - Category|category]].
>
> **Step 5 — Corollary 1 (nerves).** In $N(\mathcal{C})$ inner horns fill *uniquely* ([[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterisation]]), so the composite is the unique long edge $g\circ f$ and parallel edges are homotopic only if equal; thus $\mathrm{ho}(N\mathcal{C})$ has objects, morphisms, and composition identical to $\mathcal{C}$, giving $\mathrm{ho}(N\mathcal{C}) \cong \mathcal{C}$.
>
> **Step 6 — Corollary 2 (Kan).** By Lemma 3, if $\mathcal{D}$ is a [[Def - Kan Complex and the Nerve|Kan complex]] every morphism of $\mathrm{ho}(\mathcal{D})$ is invertible, so $\mathrm{ho}(\mathcal{D})$ is a [[Def - Groupoid|groupoid]]; applied to $\mathrm{Sing}(Y)$ this is the fundamental groupoid $\Pi_1(Y)$. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**The fundamental group of the circle.** $\mathrm{Sing}(S^1)$ is a Kan complex; by Corollary 2 its homotopy category is a groupoid, and the automorphisms of a point form $\pi_1(S^1) \cong \mathbb{Z}$ (see [[Thm - Pi_1 of S^1 is Z]]). The exercise: identify a loop's homotopy class with its winding number and read off the group structure from composition of $1$-simplices. Non-obvious because it recovers a classical computation purely from horn-filling combinatorics, with composition of paths becoming composition in $\mathrm{ho}$.

**Triangulated categories from stable $\infty$-categories.** The homotopy category of a stable $\infty$-category is triangulated, with the shift and distinguished triangles read off from $\infty$-categorical (co)fibre sequences. The exercise: show that the cone, functorial in the $\infty$-category, descends to a non-functorial construction in $\mathrm{ho}$ — the famous defect of triangulated categories. Non-obvious because it pinpoints *what is lost* in passing to $\mathrm{ho}$: exactly the higher cells that made the cone canonical (the §H.5 motivation made precise).

**Recovering a category from a rewriting system.** A confluent, terminating rewriting system presents a category whose morphisms are rewrite sequences up to the confluence relation; this is $\mathrm{ho}$ of the quasi-category of rewrites. The exercise: show that confluence is what makes composition well-defined, mirroring the role of inner-horn filling. Non-obvious because it casts a computer-science normalisation result as an instance of the homotopy-category construction.

---

# Bridges

- **[[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|The nerve characterisation]]** — the inverse relationship. That theorem embeds $\mathbf{Cat}$ into $\mathbf{sSet}$ via $N$ with unique fillers; this theorem provides the retraction $\mathrm{ho}$ with $\mathrm{ho}\circ N \cong \mathrm{id}$. Together they exhibit $\mathrm{ho} \dashv N$, making ordinary categories the $1$-truncation of $\infty$-categories.

- **[[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|$\mathrm{Sing}(Y)$ is a Kan complex]]** — the source of fundamental groupoids. Because $\mathrm{Sing}(Y)$ is Kan, Corollary 2 gives $\mathrm{ho}(\mathrm{Sing}\,Y) = \Pi_1(Y)$, the [[Def - Path-Product and the Fundamental Group|fundamental groupoid]]; the full $\mathrm{Sing}(Y)$ is the fundamental $\infty$-groupoid, and $\mathrm{ho}$ is its bottom truncation.

- **The Postnikov tower** — $\mathrm{ho}$ as the first stage. The homotopy category is the $1$-truncation $\tau_{\le 1}\mathcal{D}$ of a quasi-category; iterating the truncation up the dimensions yields the Postnikov tower, the systematic approximation of an $\infty$-category (or space) by its $n$-truncations. $\mathrm{ho}$ keeps $\pi_0$ and $\pi_1$ and discards everything higher.

---

# Unlocked by This

> [!tip] Truncation and the Postnikov Tower *(from Higher Category Theory)*
> $\mathrm{ho} = \tau_{\le 1}$ is the bottom of the **truncation tower** $\dots \to \tau_{\le 2}\mathcal{D} \to \tau_{\le 1}\mathcal{D} = \mathrm{ho}(\mathcal{D})$, the $\infty$-categorical Postnikov system that approximates any $\infty$-category by its low-dimensional shadows.

> [!tip] Triangulated and Derived Categories *(from Homological Algebra)*
> The homotopy category of a **stable ∞-category** is a **triangulated category**, and of the $\infty$-category of complexes it is the **derived category**. The non-functoriality of cones and the failure of the octahedral data to be canonical are exactly the higher cells $\mathrm{ho}$ forgets — the motivation, made precise, for the $\infty$-categorical enhancements of §H.5.
