---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Singular Simplex"
  - "Def - Kan Complex and the Nerve"
  - "Thm - Geometric Realization is Left Adjoint to the Singular Nerve"
  - "Def - Topological Space"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $Y$ be a [[Def - Topological Space|topological space]]. Show that the singular simplicial set $\mathrm{Sing}(Y)$, with $\mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|, Y)$ the set of [[Def - Singular Simplex|singular n-simplices]], is a [[Def - Kan Complex and the Nerve|Kan complex]]: *every* horn $\Lambda^n_i\to\mathrm{Sing}(Y)$ (inner and outer, $0\le i\le n$) has a filler. Use that the geometric horn $|\Lambda^n_i|$ is a **retract** of the solid simplex $|\Delta^n|$. Conclude that $\mathrm{Sing}(Y)$ is the **fundamental ∞-groupoid** of $Y$, and hence that Kan complexes are exactly the ∞-groupoids.

**Recall:**

![[Def - Singular Simplex#The Definition]]

The singular simplicial set has $\mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|, Y)$, the continuous maps from the geometric $n$-simplex into $Y$; faces and degeneracies are precomposition with the geometric coface/codegeneracy maps. A [[Def - Kan Complex and the Nerve|Kan complex]] fills *all* horns. A *retract* of $|\Delta^n|$ onto $|\Lambda^n_i|$ is a continuous $r:|\Delta^n|\to|\Lambda^n_i|$ with $r\circ\iota = \mathrm{id}$ for the inclusion $\iota$.

---

# Convergent Strategy

**Problem class:** This is a "verify all horns fill" problem of the strongest kind (Kan, not merely quasi-category) — the "fill" target of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]], here resolved geometrically. The routine is to translate a simplicial horn-filling problem into a topological extension problem via the adjunction, then solve the extension by a retraction.

**Assumption pattern:** The recognisable feature is that $\mathrm{Sing}(Y)$ is defined by *mapping geometric simplices into $Y$*. So a simplicial horn $\Lambda^n_i\to\mathrm{Sing}(Y)$ is, by the [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|realisation–singular adjunction]], a continuous map $|\Lambda^n_i|\to Y$, and filling it is extending that map over $|\Delta^n|$.

**Theorem routing:** The route is: simplicial horn $\to$ (adjunction) $\to$ continuous map out of the geometric horn $\to$ (retraction $|\Delta^n|\to|\Lambda^n_i|$) $\to$ extension over $|\Delta^n|$ $\to$ (adjunction) $\to$ filler. The key geometric input is the retraction, which exists for *every* face, hence for *all* horns.

**Key decision point:** The non-obvious choice — and the reason the conclusion is *Kan* rather than just *quasi-category* — is recognising that the retraction $|\Lambda^n_i|\hookrightarrow|\Delta^n|$ exists for **outer** horns too, not only inner ones. A solid simplex deformation-retracts onto any of its horns, regardless of which face is omitted. This is what makes $\mathrm{Sing}(Y)$ fill all horns and be an $\infty$-groupoid.

---

# Legal Operations Used

1. **Operation 2 (compute simplices via the universal property).** $\mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|, Y)$ — simplices are singular simplices.

2. **Operation 7 (the realisation–singular adjunction).** A horn $\Lambda^n_i\to\mathrm{Sing}(Y)$ corresponds to a map $|\Lambda^n_i|\to Y$, by $|{-}|\dashv\mathrm{Sing}$.

3. **Operation 3 (translate horn-filling into a geometric extension).** Filling the horn is extending a map out of the geometric horn over the solid simplex, solved by a retraction.

---

# Hints

> [!note]- Hint 1
> A horn $\Lambda^n_i\to\mathrm{Sing}(Y)$ is a compatible family of singular simplices on the faces. By the [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|adjunction]], what continuous map does this assemble into?

> [!note]- Hint 2
> It assembles into a continuous map $|\Lambda^n_i|\to Y$ out of the *geometric* horn (the union of the corresponding geometric faces). A filler is an extension over $|\Delta^n|$.

> [!note]- Hint 3
> The geometric horn $|\Lambda^n_i|$ is a retract of $|\Delta^n|$: there is a continuous $r:|\Delta^n|\to|\Lambda^n_i|$ fixing the horn (project from the barycentre of the missing face). Then $\hat\phi\circ r:|\Delta^n|\to Y$ extends $\hat\phi$. This works for *every* $i$ — inner and outer.

---

# Solution

The plan: Step 1 translates the simplicial horn into a geometric map via the adjunction. Step 2 exhibits the retraction of the solid simplex onto the horn. Step 3 builds the filler by composing with the retraction, for all horns. Step 4 concludes $\mathrm{Sing}(Y)$ is Kan and identifies it as the fundamental ∞-groupoid.

**Step 1: A horn is a map out of the geometric horn.** A simplicial horn $\phi:\Lambda^n_i\to\mathrm{Sing}(Y)$ corresponds, under $|{-}|\dashv\mathrm{Sing}$, to a continuous map $\hat\phi:|\Lambda^n_i|\to Y$.

> [!note]- Derivation
> By the [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|realisation–singular adjunction]], $\mathbf{sSet}(\Lambda^n_i, \mathrm{Sing}(Y)) \cong \mathbf{Top}(|\Lambda^n_i|, Y)$. So the simplicial map $\phi$ corresponds to a continuous map $\hat\phi:|\Lambda^n_i|\to Y$ out of the geometric realisation of the horn — concretely, the union of the geometric faces $|\Delta^{n-1}|$ glued along their common geometric faces, mapping to $Y$ by the singular simplices that $\phi$ assigns. A filler $\Delta^n\to\mathrm{Sing}(Y)$ corresponds, again by adjunction, to a continuous extension $|\Delta^n|\to Y$ of $\hat\phi$.

**Step 2: The retraction.** The geometric horn $|\Lambda^n_i|$ is a retract (indeed a deformation retract) of the solid simplex $|\Delta^n|$: there is a continuous $r:|\Delta^n|\to|\Lambda^n_i|$ with $r|_{|\Lambda^n_i|} = \mathrm{id}$.

> [!note]- Derivation
> Place a cone point at the barycentre $b_i$ of the omitted $i$th face of $|\Delta^n|$. Radial projection away from $b_i$ pushes every point of the solid simplex (and of the omitted face) onto the union $|\Lambda^n_i|$ of the remaining faces; this map $r:|\Delta^n|\to|\Lambda^n_i|$ is continuous and fixes $|\Lambda^n_i|$ pointwise. Geometrically, $|\Lambda^n_i|$ is a strong deformation retract of the contractible solid simplex. Crucially, this construction works for *every* $i\in\{0,1,\dots,n\}$: the position of the omitted face does not matter, only that one face (and the interior) is being projected away. So the retraction exists for **outer** horns just as for inner ones.

**Step 3: Build the filler, for all horns.** Compose $\hat\phi$ with $r$: the map $\hat\phi\circ r:|\Delta^n|\to Y$ extends $\hat\phi$, giving a filler. This holds for every $i$.

> [!note]- Derivation
> Define $\psi := \hat\phi\circ r : |\Delta^n|\to Y$. It is continuous (composite of continuous maps). On the horn, $\psi|_{|\Lambda^n_i|} = \hat\phi\circ r|_{|\Lambda^n_i|} = \hat\phi\circ\mathrm{id} = \hat\phi$, so $\psi$ extends $\hat\phi$. By the adjunction (Step 1), $\psi$ corresponds to a simplicial map $\Delta^n\to\mathrm{Sing}(Y)$ extending $\phi$ — a filler of the horn. Since the retraction $r$ exists for every $i\in\{0,\dots,n\}$ (Step 2), *every* horn, inner and outer, has a filler.

**Step 4: $\mathrm{Sing}(Y)$ is Kan; it is the fundamental ∞-groupoid.** All horns fill, so $\mathrm{Sing}(Y)$ is a [[Def - Kan Complex and the Nerve|Kan complex]], hence an ∞-groupoid — the fundamental ∞-groupoid of $Y$.

> [!note]- Derivation
> By Step 3, $\mathrm{Sing}(Y)$ satisfies the lifting property against all horn inclusions, which is the definition of a [[Def - Kan Complex and the Nerve|Kan complex]]. By [[Ex - Every Kan complex is a quasi-category|the identification of Kan complexes with ∞-groupoids]], $\mathrm{Sing}(Y)$ is an ∞-groupoid: its objects are points of $Y$, its morphisms are paths, its $2$-simplices are homotopies of paths, and every morphism is invertible (paths reverse up to homotopy). This is the **fundamental ∞-groupoid** $\Pi_\infty(Y)$; its [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] is the fundamental groupoid $\Pi_1(Y)$, and its simplicial homotopy groups are the homotopy groups $\pi_n(Y)$. Since *every* space gives a Kan complex this way and conversely every Kan complex is an ∞-groupoid, Kan complexes *are* the ∞-groupoids.

> [!note]- Complete formal solution
> Let $Y$ be a space and $\phi:\Lambda^n_i\to\mathrm{Sing}(Y)$ a horn ($0\le i\le n$).
>
> 1. By $|{-}|\dashv\mathrm{Sing}$ ([[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]), $\phi$ corresponds to a continuous $\hat\phi:|\Lambda^n_i|\to Y$.
> 2. Radial projection from the barycentre of the omitted $i$th face gives a continuous retraction $r:|\Delta^n|\to|\Lambda^n_i|$ with $r|_{|\Lambda^n_i|} = \mathrm{id}$; this exists for every $i$, inner and outer.
> 3. Then $\hat\phi\circ r:|\Delta^n|\to Y$ extends $\hat\phi$, and by adjunction corresponds to a filler $\Delta^n\to\mathrm{Sing}(Y)$ of $\phi$.
>
> So every horn fills: $\mathrm{Sing}(Y)$ is a [[Def - Kan Complex and the Nerve|Kan complex]], the fundamental ∞-groupoid of $Y$. Combined with [[Ex - Every Kan complex is a quasi-category]], Kan complexes are exactly the ∞-groupoids. $\quad\blacksquare$

---

# Key Takeaways

**A map out of a retract always extends — this single topological fact is the entire reason $\mathrm{Sing}(Y)$ is Kan.** If $A$ is a retract of $B$ (via $r:B\to A$ fixing $A$), any map $A\to Y$ extends to $B$ by composing with $r$. Horn-filling for $\mathrm{Sing}(Y)$ is exactly this, with $A = |\Lambda^n_i|$ and $B = |\Delta^n|$. The reusable recognition: lifting/extension problems against an inclusion $A\hookrightarrow B$ are trivial whenever $A$ is a retract of $B$, and many fibrancy proofs reduce to exhibiting such a retraction. The adjunction is what converts the *simplicial* horn-filling into this *topological* extension.

**The retraction exists for *all* horns, which is precisely why $\mathrm{Sing}(Y)$ is an ∞-groupoid rather than merely an ∞-category.** The crucial observation is that the solid simplex retracts onto *any* of its horns — the omitted face can be the first, last, or a middle one. Inner horns would give only a quasi-category; the outer horns, fillable by the *same* retraction, force every morphism to be invertible. This is the geometric origin of the slogan "spaces are ∞-groupoids": a space's morphisms (paths) are all invertible because paths can be reversed, and that reversibility is the outer-horn filling delivered by the retraction. The diagnostic: to upgrade "quasi-category" to "Kan", check whether outer horns fill — for singular complexes they always do, for nerves of non-groupoids they never do.

**The fundamental ∞-groupoid keeps *all* the homotopy, where $\pi_1$ keeps almost none — and this is the upgrade that motivates the whole chapter.** Classical algebraic topology extracts $\pi_1(Y)$ and the higher $\pi_n(Y)$ as separate invariants, discarding the relations among them. The Kan complex $\mathrm{Sing}(Y)$ retains the entire homotopy type: $0$-simplices are points, $1$-simplices paths, $2$-simplices homotopies, and so on, with the homotopy category recovering $\Pi_1(Y)$ and the simplicial homotopy groups recovering all $\pi_n$. The reusable lesson, the bridge to §H.5 and to the **homotopy hypothesis**: the right invariant of a space is not a tower of groups but a single ∞-groupoid, and the right way to do homotopy theory is to work with that combinatorial object directly.
