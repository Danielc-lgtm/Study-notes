---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Kan Fibration and Anodyne Extension"
  - "Def - Lifting Property and the Retract Argument"
  - "Thm - Simplicial Sets Form a Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Call a map $p : E \to B$ of [[Def - Simplicial Set|simplicial sets]] a **trivial fibration** if it has the right [[Def - Lifting Property and the Retract Argument|lifting property]] against every boundary inclusion $\partial\Delta^n \hookrightarrow \Delta^n$ ($n \ge 0$). Show that $p$ is then a trivial fibration if and only if it has the right lifting property against *every* monomorphism of simplicial sets. Deduce that a trivial fibration is in particular a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]].

**Recall:**

A map $p$ has the **right [[Def - Lifting Property and the Retract Argument|lifting property]]** against $i$ if every commuting square with $i$ on the left and $p$ on the right has a diagonal lift. $\mathrm{RLP}(\mathcal{S})$ is the class with the right lifting property against every member of $\mathcal{S}$.

A **monomorphism** is a level-wise injection; by the [[Ex - Monomorphisms are the cofibrations|cofibration exercise]], every monomorphism is a transfinite composite of [[Def - Pullback and Pushout|pushouts]] of boundary inclusions $\partial\Delta^n \hookrightarrow \Delta^n$.

The boundary inclusions are the generating cofibrations $I = \{\partial\Delta^n \hookrightarrow \Delta^n\}$; the horn inclusions are the generating trivial cofibrations $J = \{\Lambda^n_k \hookrightarrow \Delta^n\}$ ([[Thm - Simplicial Sets Form a Model Category]]).

---

# Convergent Strategy

**Problem class:** This is a *lifting-against-a-saturated-class* problem of the lifting world (topic-page Problem-Solving Strategy): we promote "lifts against the generators $I$" to "lifts against the whole saturation $\mathrm{cof}(I) =$ monomorphisms". The universal routine is that the right lifting property against a set $\mathcal{S}$ automatically extends to the saturation of $\mathcal{S}$, because the right lifting property is preserved by the operations that build the saturation.

**Assumption pattern:** The recognisable feature is "RLP against the generators". This is exactly the input to the general lemma $\mathrm{RLP}(\mathcal{S}) = \mathrm{RLP}(\mathrm{cof}(\mathcal{S}))$. The recognition to make is that lifting against the small explicit set $I$ is the *same* as lifting against the enormous class of all monomorphisms — you never have to check more than the boundary inclusions.

**Theorem routing:** The route is: RLP against $I$ $\to$ RLP against pushouts of $I$ (lift in the pushout by the universal property) $\to$ RLP against transfinite composites (lift stage by stage, take colimit) $\to$ RLP against retracts $\to$ RLP against $\mathrm{cof}(I) = \{$monomorphisms$\}$ (using the [[Ex - Monomorphisms are the cofibrations|cellular description of monos]]). The corollary routes through $J \subseteq \{$mono$\}$.

**Key decision point:** The crux is the transfinite-composite step: lifting against an infinite composite of cofibrations requires building the lift *inductively* over the stages and then taking the colimit, checking the partial lifts are compatible. The natural wrong move is to try to lift "all at once"; the right move is to lift one cell at a time and assemble, which is where smallness of the cell domains is silently used.

---

# Legal Operations Used

1. **Operation 2 from the topic page (build a cofibration by attaching cells)** — used in reverse: the monomorphism we must lift against is decomposed into its cells, and we lift against each cell.

2. **The closure of $\mathrm{RLP}$ classes under pushout, transfinite composition, and retract (from [[Def - Kan Fibration and Anodyne Extension]]).** This is the engine: the right lifting property propagates from the generators to the saturation through exactly these three operations.

3. **The cellular description of monomorphisms (from [[Ex - Monomorphisms are the cofibrations]]).** This identifies $\mathrm{cof}(I)$ with the monomorphisms, so "lifts against $\mathrm{cof}(I)$" *is* "lifts against all monomorphisms".

---

# Hints

> [!note]- Hint 1
> One direction is trivial: boundary inclusions are monomorphisms, so "RLP against all monos" obviously implies "RLP against the boundary inclusions". The content is the converse.

> [!note]- Hint 2
> For the converse, recall that every monomorphism is built from boundary inclusions by [[Def - Pullback and Pushout|pushout]] and transfinite composition. So it suffices to show: RLP against a map is inherited by pushouts, transfinite composites, and retracts of that map.

> [!note]- Hint 3
> Pushout: given a lifting square against the pushout $C \to C\cup_A A'$, restrict along $A \to A'$ to get a square against the original $A \to A'$, lift there, and glue the lift to the given map on $C$ using the pushout universal property.

> [!note]- Hint 4
> Transfinite composite $A = X_0 \to X_1 \to \dots \to X = \mathrm{colim}\,X_\alpha$: build the lift inductively. Given a lift on $X_\alpha$, extend to $X_{\alpha+1}$ using RLP against $X_\alpha \to X_{\alpha+1}$; at limit stages take the colimit of the partial lifts. The compatible family assembles to a lift on $X$.

> [!note]- Hint 5
> For the corollary: each horn inclusion $\Lambda^n_k \hookrightarrow \Delta^n$ is a monomorphism, so RLP against all monos includes RLP against all horns, which is exactly the Kan condition.

---

# Solution

The "if" direction is immediate since boundary inclusions are monos. The "only if" direction promotes lifting against the generators $I$ to lifting against the saturation $\mathrm{cof}(I)$, by showing the right lifting property survives each of the three saturation operations. The corollary follows because horn inclusions are monomorphisms.

**Step 1: One direction is free.**

> [!note]- Derivation
> Every boundary inclusion $\partial\Delta^n \hookrightarrow \Delta^n$ is a monomorphism. So if $p$ has RLP against all monomorphisms, it in particular has RLP against all boundary inclusions, i.e. $p$ is a trivial fibration in the stated sense. This is the easy inclusion $\mathrm{RLP}(\{$mono$\}) \subseteq \mathrm{RLP}(I)$.

**Step 2: RLP propagates across pushouts.**

> [!note]- Derivation
> Suppose $p \in \mathrm{RLP}(\{i\})$ for $i : A \to A'$, and let $j : C \to C' = C \cup_A A'$ be a [[Def - Pullback and Pushout|pushout]] of $i$ along some $A \to C$. Given a square $(u : C \to E,\ v : C' \to B)$ with $pu = v|_C$: restrict to a square against $i$ via $A \to A' \to C'$, namely $(u|_A \text{ pushed to } A',\ v|_{A'})$; more precisely the map $A' \to C' \xrightarrow{v} B$ together with $A \to C \xrightarrow{u} E$ form a square against $i$. Lift it with $p$'s RLP to get $w : A' \to E$. Then $u$ on $C$ and $w$ on $A'$ agree on $A$ (both restrict to the lift's behaviour), so by the pushout universal property they glue to $\tilde w : C' \to E$ with $p\tilde w = v$, $\tilde w|_C = u$. Hence $p \in \mathrm{RLP}(\{j\})$.

**Step 3: RLP propagates across transfinite composites.**

> [!note]- Derivation
> Let $i : X_0 \to X = \mathrm{colim}_\alpha X_\alpha$ be a transfinite composite of maps $X_\alpha \to X_{\alpha+1}$, each one against which $p$ already lifts. Given a square $(u : X_0 \to E,\ v : X \to B)$ with $pu = v|_{X_0}$: define lifts $w_\alpha : X_\alpha \to E$ by transfinite recursion. Set $w_0 = u$. Given $w_\alpha$, the square $(w_\alpha,\ v|_{X_{\alpha+1}})$ against $X_\alpha \to X_{\alpha+1}$ lifts (by $p$'s RLP against that map) to $w_{\alpha+1}$ extending $w_\alpha$. At a limit ordinal $\lambda$, set $w_\lambda = \mathrm{colim}_{\alpha < \lambda} w_\alpha$ (the partial lifts are compatible by construction). The resulting $w = \mathrm{colim}_\alpha w_\alpha : X \to E$ satisfies $pw = v$, $w|_{X_0} = u$. Hence $p$ lifts against $i$.

**Step 4: RLP propagates across retracts; conclude.**

> [!note]- Derivation
> A retract of a map $i$ against which $p$ lifts is a map $j$ sitting in a retract diagram in the arrow category; a lifting square against $j$ pushes forward to one against $i$ (compose with the retraction data), is solved there, and pulls back to a lift against $j$ — this is the standard [[Def - Lifting Property and the Retract Argument|retract]] argument for lifting. Now, by the [[Ex - Monomorphisms are the cofibrations|cellular description]], every monomorphism is a retract of a transfinite composite of pushouts of boundary inclusions. By Steps 2–4, $p$'s RLP against $I$ propagates through pushout, transfinite composition, and retract, so $p$ has RLP against every monomorphism. With Step 1, $\mathrm{RLP}(I) = \mathrm{RLP}(\{$monomorphisms$\})$.

**Step 5: Trivial fibrations are Kan fibrations.**

> [!note]- Derivation
> Each horn inclusion $\Lambda^n_k \hookrightarrow \Delta^n$ is a monomorphism (a sub-simplicial-set inclusion). By Step 4, a trivial fibration $p$ has RLP against every monomorphism, in particular against every horn inclusion. That is exactly the definition of a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]]. So every trivial fibration is a Kan fibration (and, being a weak equivalence, a *trivial* Kan fibration in the model-structure sense).

> [!note]- Complete formal solution
> ($\mathrm{RLP}(\text{mono}) \subseteq \mathrm{RLP}(I)$.) Boundary inclusions are monomorphisms, so lifting against all monos gives lifting against all boundary inclusions.
>
> ($\mathrm{RLP}(I) \subseteq \mathrm{RLP}(\text{mono})$.) The right lifting property against a fixed map is preserved by pushout (glue the lift via the pushout universal property), transfinite composition (build the lift by recursion over stages, colimit at limits), and retract (the retract argument). By the cellular description ([[Ex - Monomorphisms are the cofibrations]]), every monomorphism is a retract of a transfinite composite of pushouts of boundary inclusions; hence $p \in \mathrm{RLP}(I)$ implies $p$ lifts against every monomorphism.
>
> Therefore $\mathrm{RLP}(I) = \mathrm{RLP}(\{\text{monomorphisms}\})$. Since horn inclusions are monomorphisms, every such $p$ is also a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]]. $\quad\blacksquare$

---

# Key Takeaways

**Lifting against the generators is lifting against the whole saturated class — this is the central economy of cofibrant generation.** The result $\mathrm{RLP}(\mathcal{S}) = \mathrm{RLP}(\mathrm{cof}(\mathcal{S}))$ is the reason cofibrantly generated model categories are tractable: to check a map is a fibration you test it against a *small explicit set* of generators, never against the proper class of all cofibrations. The trigger-reaction is: when asked to lift against "all cofibrations" or "all monomorphisms", reduce to the generating set and lift against those only. This single lemma is what makes the small object argument, the recognition theorem, and every fibrancy check in the subject feasible. It is worth knowing that the same lemma in the other variance gives $\mathrm{LLP}(\mathrm{RLP}(\mathcal{S})) = \mathrm{cof}(\mathcal{S})$, the saturation itself.

**The three propagation steps — pushout, transfinite composite, retract — are the universal anatomy of a saturated class.** Every proof that a property survives from generators to saturation has exactly these three steps, and they recur verbatim: showing a left Quillen functor preserves trivial cofibrations, showing weak equivalences are closed under the cell construction, showing a class is saturated. The transfinite-composite step is always the subtle one, because it requires building an object (here, a lift) by recursion over an ordinal and checking compatibility at limit stages; smallness of the cell domains is what guarantees the recursion terminates and the colimit behaves. Internalise the rhythm "pushout (universal property), transfinite (recursion + colimit), retract (retract argument)" and these proofs become mechanical.

**Trivial fibrations are the $I$-injectives, Kan fibrations are the $J$-injectives, and the inclusion $J \subseteq \mathrm{cof}(I)$ is why trivial-implies-fibration.** This exercise quietly establishes the architecture of the two weak factorisation systems: $I$ generates (cofibrations, trivial fibrations), $J$ generates (trivial cofibrations, fibrations). The fact that a trivial fibration is automatically a Kan fibration is the statement $\mathrm{RLP}(I) \subseteq \mathrm{RLP}(J)$, which holds because $J \subseteq \mathrm{cof}(I)$ (horns are monos). Recognising that the two factorisation systems are *nested* in this way — the trivial fibrations sit inside the fibrations — is the structural fact behind the lifting axiom MC4 and the whole interaction of the two factorisations in [[Thm - Simplicial Sets Form a Model Category|the model structure]].
