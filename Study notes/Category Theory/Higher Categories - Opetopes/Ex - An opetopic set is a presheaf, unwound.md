---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Opetopic Set"
  - "Def - Presheaf"
  - "Def - Natural Transformation"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Unwind the definition of an [[Def - Opetopic Set|opetopic set]] entirely in elementary terms. Show that giving a presheaf $X : \mathbb{O}^{op} \to \mathbf{Set}$ is the same as giving (i) a set $X_O$ of "$O$-cells" for each opetope $O$, together with (ii) restriction functions $X_O \to X_{O'}$ for each face map $O' \to O$, satisfying functoriality. Then verify that a morphism of opetopic sets is a family of functions commuting with restrictions, and exhibit explicitly, for the arity-$2$ opetope, what data its restrictions impose (that a $2$-cell has two specified source $1$-cells and one specified target $1$-cell).

**Recall:**

![[Def - Opetopic Set#The Definition]]

A [[Def - Presheaf|presheaf]] on a category $\mathcal{C}$ is a functor $X : \mathcal{C}^{op} \to \mathbf{Set}$; it assigns a set to each object and a function (going the opposite way) to each morphism, functorially. A [[Def - Natural Transformation|natural transformation]] $f : X \to Y$ between such functors is a family of functions $f_c : X(c) \to Y(c)$ commuting with all the structure maps.

---

# Convergent Strategy

**Problem class:** This is a *translate-an-abstract-definition-into-elementary-data* problem — the structural-world problem class. The goal is to see that "presheaf on $\mathbb{O}$" is not exotic: it is exactly "cells of each shape, with consistent boundary restrictions", and to make the consistency concrete on one face.

**Assumption pattern:** The only assumption is the presheaf definition. The functor's object-part gives the cell-sets; the functor's morphism-part (contravariant) gives the restrictions; functoriality gives the consistency. Recognising that these three are precisely the desiderata "cells, boundaries, consistency" is what makes the translation immediate.

**Theorem routing:** We route through the definition of [[Def - Presheaf|presheaf]] (a contravariant $\mathbf{Set}$-valued functor) and of [[Def - Natural Transformation|natural transformation]], specialised to the category $\mathbb{O}$. No deep theorem is needed; the content is the careful unwinding.

**Key decision point:** The non-obvious choice is to track *which way the restriction maps go*: a face inclusion $O' \to O$ of shapes induces a restriction $X_O \to X_{O'}$ of cells, because the functor is *contravariant*. Getting the variance right is the whole subtlety; the natural but wrong guess is to make cells produce higher cells from boundaries (covariant), which is backwards.

---

# Legal Operations Used

1. **Operation 3 (take the presheaf on a shape category)** from the topic page. The entire exercise is the unwinding of "presheaf on $\mathbb{O}$" into elementary cell-and-restriction data.

2. **Operation 4 (invoke Yoneda to turn a cell into a representable)** from the topic page, used at the end to phrase "an $O$-cell is a map $\mathbf{y}O \to X$" as the slick reformulation of the elementary data.

---

# Hints

> [!note]- Hint 1
> A functor $X : \mathbb{O}^{op} \to \mathbf{Set}$ does two things: it assigns a set $X(O) = X_O$ to each object $O$ of $\mathbb{O}$, and a function $X(\alpha)$ to each morphism $\alpha$ of $\mathbb{O}$. Because the domain is $\mathbb{O}^{op}$, a morphism $\alpha : O' \to O$ in $\mathbb{O}$ becomes a function going $X_O \to X_{O'}$.

> [!note]- Hint 2
> Functoriality says $X(\mathrm{id}_O) = \mathrm{id}_{X_O}$ and $X(\beta \circ \alpha) = X(\alpha) \circ X(\beta)$ — restricting along a composite of face maps agrees with restricting one face at a time. This is the consistency of boundaries.

> [!note]- Hint 3
> For the arity-$2$ opetope $O$, there are face maps from the arrow opetope into $O$ picking out the two source arrows and the one target arrow. The induced restrictions send a $2$-cell of $X$ to its two source $1$-cells and its target $1$-cell.

---

# Solution

The route is a direct unwinding of the functor structure, with attention to contravariance, followed by spelling out the arity-$2$ restrictions and the morphism condition.

**Step 1: The object-part of $X$ gives the cell-sets.**

> [!note]- Derivation
> A functor $X : \mathbb{O}^{op} \to \mathbf{Set}$ assigns to each object $O$ of $\mathbb{O}$ (i.e. each [[Def - Opetope|opetope]]) a set $X(O)$, which we write $X_O$ and call the set of **$O$-cells** of $X$. This is exactly desideratum (i): a set of cells of each opetopic shape.

**Step 2: The morphism-part of $X$ gives the restrictions, contravariantly.**

> [!note]- Derivation
> A morphism $\alpha : O' \to O$ in $\mathbb{O}$ — a face map exhibiting $O'$ inside the boundary of $O$ — is sent by the functor on $\mathbb{O}^{op}$ to a function
> $$X(\alpha) : X_O \longrightarrow X_{O'}.$$
> The direction is reversed: a face *inclusion* of shapes induces a *restriction* of cells. Given an $O$-cell $x \in X_O$, $X(\alpha)(x) \in X_{O'}$ is its $O'$-face. This is desideratum (ii). Functoriality, $X(\mathrm{id}) = \mathrm{id}$ and $X(\beta \circ \alpha) = X(\alpha) \circ X(\beta)$, says: restricting along the identity does nothing, and restricting along a composite of face maps equals restricting step by step. That is exactly the boundary-consistency condition.

**Step 3: The arity-$2$ restrictions impose source and target $1$-cells.**

> [!note]- Derivation
> Let $O$ be the arity-$2$ [[Def - Opetope|opetope]]: two source arrows $f_1, f_2$ and one target arrow $g$. In $\mathbb{O}$ there are face maps $\sigma_1, \sigma_2, \tau : (\text{arrow}) \to O$ picking out the first source, the second source, and the target. The functor induces restrictions
> $$X(\sigma_1), X(\sigma_2), X(\tau) : X_O \longrightarrow X_{(\text{arrow})}.$$
> So a $2$-cell $x \in X_O$ determines three genuine $1$-cells of $X$: its two source arrows $X(\sigma_1)(x), X(\sigma_2)(x)$ and its target arrow $X(\tau)(x)$. Composing further with the endpoint face maps $(\text{point}) \to (\text{arrow})$, functoriality forces these arrows to share endpoints consistently (the target of the first source is the source of the second, etc.), so the source $1$-cells are genuinely composable and the boundary closes up. This is precisely "a $2$-cell has two specified, composable source $1$-cells and one specified target $1$-cell."

**Step 4: A morphism of opetopic sets commutes with restrictions.**

> [!note]- Derivation
> A morphism $f : X \to Y$ is a [[Def - Natural Transformation|natural transformation]] of functors $\mathbb{O}^{op} \to \mathbf{Set}$: a family of functions $f_O : X_O \to Y_O$ such that for every face map $\alpha : O' \to O$,
> $$f_{O'} \circ X(\alpha) \;=\; Y(\alpha) \circ f_O.$$
> In words: applying $f$ and then restricting equals restricting and then applying $f$ — $f$ sends cells to cells *respecting boundaries*. For the arity-$2$ case this says $f$ sends a $2$-cell with given source/target $1$-cells to a $2$-cell whose source/target $1$-cells are the $f$-images of the originals.
>
> Finally, by [[Thm - The Yoneda Lemma|Yoneda]] (Operation 4), $X_O \cong \mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X)$, so all of this elementary cell-and-restriction data is equivalently encoded by maps out of the standard cells $\mathbf{y}O$.

> [!note]- Complete formal solution
> A presheaf $X : \mathbb{O}^{op} \to \mathbf{Set}$ assigns a set $X_O$ to each [[Def - Opetope|opetope]] $O$ (the $O$-cells), and to each face map $\alpha : O' \to O$ a *restriction* $X(\alpha) : X_O \to X_{O'}$ (contravariance: shape inclusions induce cell restrictions), with $X(\mathrm{id}) = \mathrm{id}$ and $X(\beta \circ \alpha) = X(\alpha) \circ X(\beta)$ (boundary consistency). This is exactly data (i)+(ii). For the arity-$2$ opetope $O$, the face maps $\sigma_1, \sigma_2, \tau$ from the arrow induce restrictions sending a $2$-cell to its two source $1$-cells and its target $1$-cell, with shared endpoints forced by functoriality. A morphism $f : X \to Y$ is a [[Def - Natural Transformation|natural transformation]]: functions $f_O$ with $f_{O'} \circ X(\alpha) = Y(\alpha) \circ f_O$, i.e. boundary-respecting. By [[Thm - The Yoneda Lemma|Yoneda]], $X_O \cong \mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X)$. $\blacksquare$

---

# Key Takeaways

**Contravariance is "shapes include, cells restrict".** The single most error-prone point in every presheaf-of-cells theory is the variance, and this exercise pins it down: a face *inclusion* $O' \to O$ of shapes induces a *restriction* $X_O \to X_{O'}$ of cells, because a cell knows its faces, not its cofaces. The trigger to check variance is any time you define a structure as a functor out of a category of shapes: ask "does a bigger shape have more cells or fewer?" — a bigger shape's cell restricts *down* to its faces, so the induced maps go down, which is contravariance. This same reasoning fixes the variance of simplicial sets, sheaves, and the functor of points, and getting it wrong silently inverts the whole theory.

**Functoriality is exactly boundary consistency.** It is tempting to treat the functor axioms ($X(\mathrm{id}) = \mathrm{id}$, $X(\beta\alpha) = X(\alpha)X(\beta)$) as bureaucratic, but here they are the precise statement that the boundaries of cells fit together: restricting to a face of a face equals restricting directly. The reusable insight is that whenever a structure is "objects with consistent incidence data", the consistency is functoriality of a presheaf, and conversely any presheaf *is* such a consistent incidence structure. The trigger is any combinatorial structure with a notion of "face of a face"; recognising the functor laws as the gluing condition lets you import all of presheaf theory at once.

**Yoneda converts cells into maps, and maps are easier.** The exercise ends by noting $X_O \cong \mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X)$ — an $O$-cell is the same as a map from the standard cell $\mathbf{y}O$. This is the move that lets you stop reasoning about raw elements of cell-sets and start reasoning diagrammatically about maps of presheaves, where colimits and lifting properties are available. The trigger is any time a single cell appears as data: replace it by a map out of a representable. This reflex is what turns the filler conditions of the next section (universal niches) into clean lifting/extension statements against maps of representables. See [[Ex - The representable opetope as the standard cell via Yoneda]] for the representables made explicit, and [[Ex - Colimits of opetopic sets are computed pointwise]] for the pointwise structure this unwinding exposes.
