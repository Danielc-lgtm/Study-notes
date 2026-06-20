---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - The Quillen Model Structure on Topological Spaces"
  - "Def - Higher Homotopy Group"
  - "Def - Cofibrant and Fibrant Objects"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

In the [[Def - The Quillen Model Structure on Topological Spaces|Quillen model structure]] on $\mathbf{Top}$:

**(a)** Show that the boundary inclusion $S^{n-1} \hookrightarrow D^n$ is a cofibration but **not** a weak homotopy equivalence (so not a trivial cofibration).

**(b)** Show that the bottom-inclusion $D^n \hookrightarrow D^n \times I$ is a **trivial** cofibration (a cofibration that is also a weak homotopy equivalence).

**(c)** Explain what each of these two maps generates: the first the cofibrations, the second the trivial cofibrations.

**Recall:**

The generating cofibrations of the Quillen model structure are $I_{\text{top}} = \{S^{n-1} \hookrightarrow D^n\}$ and the generating trivial cofibrations are $J_{\text{top}} = \{D^n \hookrightarrow D^n \times I\}$. A **cofibration** is a retract of a relative cell complex; a **weak homotopy equivalence** induces isomorphisms on all [[Def - Higher Homotopy Group|homotopy groups]]; a **trivial cofibration** is a cofibration that is also a weak equivalence. A space is **cofibrant** when $\emptyset \to X$ is a cofibration. The disk $D^n$ is contractible; the sphere $S^{n-1}$ has $\pi_{n-1}(S^{n-1}) \cong \mathbb{Z}$ for $n \geq 1$.

---

# Convergent Strategy

**Problem class:** This is a "classify specific maps" problem that anchors the generators of the model structure to concrete geometry. The routine is to check each of the three model-category properties (cofibration, weak equivalence) against the definitions, using homotopy groups for the weak-equivalence part.

**Assumption pattern:** The recognisable structure is "a generating (trivial) cofibration", and the assumptions are the contractibility of $D^n$ (giving the weak equivalence in (b)) and the nontriviality of $\pi_{n-1}(S^{n-1})$ (obstructing the weak equivalence in (a)). The cell-attachment description of cofibrations is what makes both inclusions cofibrations almost by definition.

**Theorem routing:** Part (a): $S^{n-1}\hookrightarrow D^n$ is a single cell attachment, hence a relative cell complex, hence a cofibration; it is not a weak equivalence because $\pi_{n-1}$ differs. Part (b): $D^n \hookrightarrow D^n \times I$ is a deformation retract (so a weak equivalence by homotopy invariance of $\pi_*$) and a cofibration (it is the cell-attachment-like inclusion in $J_{\text{top}}$). Part (c): cite the role of generators in [[Thm - Topological Spaces Form a Model Category|the recognition theorem]] and the small object argument.

**Key decision point:** The non-obvious point is in (a): showing $S^{n-1}\hookrightarrow D^n$ is *not* a weak equivalence requires producing an invariant that distinguishes the two spaces. The natural choice is $\pi_{n-1}$ ($\mathbb{Z}$ for the sphere, $0$ for the contractible disk), and choosing the *right* degree $n-1$ — not $\pi_n$ or $\pi_0$ — is the decision that makes the obstruction visible.

---

# Legal Operations Used

1. **Operation 5 from the topic page (attach a cell).** Both inclusions are cell-attachment-type maps; recognising them as such is what makes them cofibrations.

2. **Operation 4 from the topic page (recognise a fibration / use homotopy-lifting intuition).** Used indirectly: the trivial cofibration in (b) is exactly the map that fibrations lift against, dual to the homotopy lifting property.

---

# Hints

> [!note]- Hint 1
> A relative cell complex built from a *single* cell $S^{n-1}\hookrightarrow D^n$ is that very inclusion. So why is $S^{n-1}\hookrightarrow D^n$ a cofibration almost by definition?

> [!note]- Hint 2
> To show $S^{n-1}\hookrightarrow D^n$ is not a weak equivalence, find a homotopy group where the source and target differ. $D^n$ is contractible (all $\pi_k = 0$); what is $\pi_{n-1}(S^{n-1})$?

> [!note]- Hint 3
> For (b): the inclusion $D^n \hookrightarrow D^n \times I$ as the bottom $D^n \times \{0\}$ has a deformation retraction onto it (slide down the $I$-coordinate). A deformation retract induces isomorphisms on all homotopy groups — why does that make the inclusion a weak equivalence?

---

# Solution

Each map is checked against the two defining properties. The sphere-disk inclusion is a single cell, hence a cofibration, but separates the spaces at $\pi_{n-1}$ so it is not a weak equivalence; the bottom-inclusion is a deformation retract, hence a trivial cofibration. The roles as generators follow from the recognition theorem.

**Step 1 (a): $S^{n-1}\hookrightarrow D^n$ is a cofibration but not a weak equivalence.**

> [!note]- Derivation
> *Cofibration.* A relative cell complex is built by attaching cells $S^{k-1}\hookrightarrow D^k$. The inclusion $S^{n-1} \hookrightarrow D^n$ is the attachment of a single $n$-cell to the space $S^{n-1}$ — indeed it is *the* generating cofibration in $I_{\text{top}}$. A relative cell complex consisting of one cell is that inclusion itself, so $S^{n-1}\hookrightarrow D^n$ is a relative cell complex, hence a cofibration. (No retract is needed; it is already a cell complex.)
>
> *Not a weak equivalence.* The disk $D^n$ is contractible, so $\pi_k(D^n) = 0$ for all $k$. The sphere $S^{n-1}$, for $n \geq 1$, has $\pi_{n-1}(S^{n-1}) \cong \mathbb{Z}$ (the degree of a self-map; for $n = 1$ this is $\pi_0(S^0) = \{\pm\}$, two points, while $\pi_0(D^1) = *$). The inclusion induces $\pi_{n-1}(S^{n-1}) = \mathbb{Z} \to \pi_{n-1}(D^n) = 0$, which is not an isomorphism. So $S^{n-1}\hookrightarrow D^n$ is not a weak homotopy equivalence, hence not a trivial cofibration.

**Step 2 (b): $D^n \hookrightarrow D^n \times I$ is a trivial cofibration.**

> [!note]- Derivation
> *Cofibration.* The bottom-inclusion $D^n \hookrightarrow D^n \times I$, $x \mapsto (x, 0)$, is the generating trivial cofibration in $J_{\text{top}}$. It is a relative cell complex (one can present $D^n \times I$ as built from $D^n$ by attaching cells; concretely $(D^n, S^{n-1})$-relative cells), so it is a cofibration. More simply, it is a *closed inclusion that is a deformation retract*, and such inclusions are cofibrations in $\mathbf{Top}$.
>
> *Weak equivalence.* The map $r : D^n \times I \to D^n$, $(x, t) \mapsto x$, is a strong deformation retraction onto the bottom $D^n \times \{0\}$: the homotopy $G((x,t), s) = (x, (1-s)t)$ slides everything down to the bottom, fixing the bottom throughout. A deformation retraction is a [[Def - Homotopy Equivalence and Contractible Space|homotopy equivalence]], hence induces isomorphisms on all [[Def - Higher Homotopy Group|homotopy groups]], so the inclusion is a weak homotopy equivalence. Being both a cofibration and a weak equivalence, it is a trivial cofibration.

**Step 3 (c): the roles as generators.**

> [!note]- Derivation
> By [[Thm - Topological Spaces Form a Model Category|the recognition theorem]], the Quillen model structure is cofibrantly generated by $I_{\text{top}} = \{S^{n-1}\hookrightarrow D^n\}$ and $J_{\text{top}} = \{D^n \hookrightarrow D^n \times I\}$. This means:
> - The **cofibrations** are exactly the retracts of transfinite cell-attachments built from $I_{\text{top}}$ (relative cell complexes); equivalently the maps with the left lifting property against all trivial fibrations. So $S^{n-1}\hookrightarrow D^n$ *generates* the cofibrations: every cofibration is assembled from copies of it (and its retracts).
> - The **trivial cofibrations** are generated by $J_{\text{top}}$: every trivial cofibration is a retract of a transfinite composite of pushouts of bottom-inclusions $D^n \hookrightarrow D^n \times I$. So this map generates the trivial cofibrations.
>
> The small object argument uses these two sets to manufacture the factorizations MC5: attaching $I_{\text{top}}$-cells gives the (cofibration, trivial fibration) factorization, and attaching $J_{\text{top}}$-cylinders gives the (trivial cofibration, fibration) factorization.

> [!note]- Complete formal solution
> **(a)** $S^{n-1}\hookrightarrow D^n$ is the attachment of a single $n$-cell, hence a relative cell complex, hence a cofibration. It is not a weak equivalence: $D^n$ is contractible so $\pi_{n-1}(D^n) = 0$, while $\pi_{n-1}(S^{n-1}) \cong \mathbb{Z}$ ($n \geq 1$), so the induced map on $\pi_{n-1}$ is $\mathbb{Z} \to 0$, not an isomorphism.
>
> **(b)** $D^n \hookrightarrow D^n \times I$ (the bottom-inclusion) is a closed inclusion and a deformation retract via $G((x,t),s) = (x,(1-s)t)$; deformation retracts are homotopy equivalences, hence weak equivalences. It is a cofibration (a relative cell complex / closed deformation-retract inclusion). So it is a trivial cofibration.
>
> **(c)** By cofibrant generation ([[Thm - Topological Spaces Form a Model Category]]), $I_{\text{top}} = \{S^{n-1}\hookrightarrow D^n\}$ generates the cofibrations (= retracts of relative $I_{\text{top}}$-cell complexes = LLP against trivial fibrations) and $J_{\text{top}} = \{D^n\hookrightarrow D^n \times I\}$ generates the trivial cofibrations; the small object argument uses them for the two MC5 factorizations. $\blacksquare$

---

# Key Takeaways

**A single cell attachment is the atom of cofibrations, and "is it a weak equivalence?" is settled by one homotopy group.** The reusable pattern is that membership in the cofibration class is recognised by cell structure — if a map attaches cells, it is a cofibration — while the weak-equivalence question is a separate check using homotopy (or homology) groups. The trigger "is this map a (trivial) cofibration?" splits into two independent questions: cofibration (cell structure) and weak equivalence (an invariant). The sphere-disk inclusion is the cleanest case: a cofibration by construction, not a weak equivalence because exactly one homotopy group ($\pi_{n-1}$) detects the difference between a sphere and a contractible disk. Choosing the right degree to test is the skill; the sphere $S^{n-1}$ "lives in" degree $n-1$, which is where its nontrivial homotopy sits.

**Deformation retracts are the cleanest trivial cofibrations, and contractibility is the source of triviality.** Part (b) shows the master example of a trivial cofibration: a closed inclusion that is a deformation retract. The retraction makes it a homotopy equivalence (hence weak equivalence), and the closed-inclusion structure makes it a cofibration. The diagnostic to carry forward: whenever you need a trivial cofibration, look for a deformation retract; the inclusion of a space into something that deformation-retracts back onto it is automatically one. This is why the cylinder inclusions generate the trivial cofibrations — the cylinder always retracts onto its bottom — and it is the topological face of "attach an acyclic disk" in chain complexes, where the disk complex $D^n$ is contractible and $0 \hookrightarrow D^n$ is the trivial cofibration.

**The two generating sets do completely different jobs, and keeping them straight is the key to the small object argument.** $I_{\text{top}}$ generates the cofibrations and is used to build the (cofibration, trivial fibration) factorization; $J_{\text{top}}$ generates the trivial cofibrations and builds the (trivial cofibration, fibration) factorization. Confusing them — or thinking one set suffices — is the most common error in setting up a cofibrantly generated model structure. The transferable principle: every cofibrantly generated model category comes with *two* generating sets, $I$ (cofibrations) and $J$ (trivial cofibrations), and the recognition theorem's hypotheses are conditions relating $I$, $J$, and the weak equivalences. When you build or verify such a structure, always identify both sets and check that $J$-cells are weak equivalences while $I$-cells need not be — exactly the contrast between (a) and (b).
