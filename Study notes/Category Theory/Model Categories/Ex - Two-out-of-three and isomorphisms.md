---
type: exercise
subject: model-categories
difficulty: "⭐"
prereqs:
  - "Def - Model Category"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{M}$ be a model category with class of weak equivalences $\mathcal{W}$. Using only the two-out-of-three axiom (MC2) and the retract axiom (MC3), prove the following.

(a) Every identity map $\mathrm{id}_X$ is a weak equivalence, and $\mathcal{W}$ is closed under composition.

(b) Every isomorphism of $\mathcal{M}$ is a weak equivalence.

(c) ("Two-out-of-six" warm-up.) If $h \circ g$ and $g \circ f$ are weak equivalences, then $f$, $g$, $h$, and $h \circ g \circ f$ are all weak equivalences — *provided* one also knows $\mathcal{W}$ is closed under retracts and that any map factors through its image appropriately; for this exercise, prove the weaker statement that if $g \circ f$ and $f$ are weak equivalences then $g$ is, and if $g \circ f$ and $g$ are weak equivalences then $f$ is.

**Recall:**

A [[Def - Model Category|model category]] has weak equivalences satisfying the two-out-of-three axiom and the retract axiom:

> **(MC2) Two-out-of-three.** If $f$ and $g$ are composable and two of $f$, $g$, $g \circ f$ are weak equivalences, then so is the third.

> **(MC3) Retracts.** Each of the three classes is closed under retracts.

An [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]] is a map $f$ with a two-sided inverse $f^{-1}$, so $f^{-1} f = \mathrm{id}$ and $f f^{-1} = \mathrm{id}$.

---

# Convergent Strategy

**Problem class:** This is a pure axiom-consequence problem: extract the elementary facts about weak equivalences that the axioms force, before any of the deeper machinery is built. It belongs to the "establish closure" target on the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Sources and Targets|topic page]], in its simplest form.

**Assumption pattern:** The only assumptions are MC2 and MC3. The recognizable pattern is that every claim is about *which maps must be weak equivalences*, and the only tool for promoting a map into $\mathcal{W}$ is MC2 (sandwich it between known weak equivalences) or MC3 (exhibit it as a retract of one). For identities and isomorphisms, the standard trick is to use that they compose to identities.

**Theorem routing:** No theorem beyond the axioms is needed. The route is: (a) and (b) from MC2 applied to composites involving identities and inverses; (c) is the literal content of MC2.

**Key decision point:** The one non-obvious move is in part (b): to show an isomorphism $f$ is a weak equivalence, you must produce a composite involving $f$ that you already know is a weak equivalence. The choice is to use $\mathrm{id} = f^{-1} f$ — but this requires first knowing identities are weak equivalences (part a), which itself requires a seed. The seed is that $\mathrm{id} = \mathrm{id} \circ \mathrm{id}$ and applying MC2 to this with all three maps equal.

---

# Legal Operations Used

1. **Operation 5 from the topic page (use 2-out-of-three to certify a weak equivalence).** This is the workhorse of the entire exercise: every promotion of a map into $\mathcal{W}$ is an application of MC2 to a carefully chosen composite.

2. **Operation 3 from the topic page (run the retract argument), in the form of retract-closure of $\mathcal{W}$.** Used only to note that $\mathcal{W}$ being retract-closed (MC3) is what would be needed for the full two-out-of-six; the weaker statement we prove uses only MC2.

---

# Hints

> [!note]- Hint 1
> For identities: apply MC2 to the composite $\mathrm{id}_X = \mathrm{id}_X \circ \mathrm{id}_X$. You need a seed — some weak equivalence to start from. Notice that *any* model category has at least one weak equivalence (e.g. produced by factoring; but more simply, argue you can bootstrap from the axioms alone).

> [!note]- Hint 2
> Actually the cleanest seed: in MC2 take $f = g = \mathrm{id}_X$. Then $g \circ f = \mathrm{id}_X$, and "two of the three are weak equivalences implies the third is" — but you have no weak equivalence yet. Instead use that $\mathcal{W}$ is a *subcategory* (contains identities and is closed under composition by definition in Hovey's formulation), or derive it: the factorization axiom produces weak equivalences, and then MC2 propagates.

> [!note]- Hint 3
> For isomorphisms: once identities are known to be weak equivalences, write $\mathrm{id}_Y = f \circ f^{-1}$ and $\mathrm{id}_X = f^{-1} \circ f$, and apply MC2.

> [!note]- Hint 4
> For (c): "$g \circ f$ and $f$ are weak equivalences implies $g$ is" — apply MC2 directly to the composite $g \circ f$ with the two known weak equivalences being $f$ and $g \circ f$; the third map is $g$.

---

# Solution

The whole solution is repeated application of MC2 to composites chosen so that two of the three maps are already known weak equivalences. The only genuine step is seeding the argument with the fact that $\mathcal{W}$ contains identities, after which isomorphisms and the cancellation statements follow mechanically.

**Step 1: Identities are weak equivalences and $\mathcal{W}$ is closed under composition.**

> [!note]- Derivation
> In the classical Quillen axioms, the three classes are required to *contain all identities and be closed under composition* (they are subcategories) — this is part of the data of a model structure, made explicit in Hovey's formulation. So $\mathrm{id}_X \in \mathcal{W}$ for all $X$, and if $f, g \in \mathcal{W}$ are composable then $g \circ f \in \mathcal{W}$ directly. (Even without assuming $\mathcal{W}$ is a subcategory a priori, closure under composition follows from MC2: if $f, g \in \mathcal{W}$, then two of $f, g, gf$ are weak equivalences, so $gf$ is.) Thus $\mathrm{id}_X \in \mathcal{W}$ and $\mathcal{W}$ is closed under composition.

**Step 2: Isomorphisms are weak equivalences.**

> [!note]- Derivation
> Let $f : X \to Y$ be an isomorphism with inverse $f^{-1}$. Consider the composite $f^{-1} \circ f = \mathrm{id}_X$. By Step 1, $\mathrm{id}_X \in \mathcal{W}$. We do not yet know $f$ or $f^{-1}$ is a weak equivalence, so we cannot apply MC2 to this composite directly with two knowns. Instead use the retract trick: an isomorphism $f$ is a retract of the identity $\mathrm{id}_Y$. The retract diagram is
> $$\begin{array}{ccccc} X & \xrightarrow{f} & Y & \xrightarrow{f^{-1}} & X \\ \scriptstyle f \downarrow & & \downarrow \scriptstyle \mathrm{id}_Y & & \downarrow \scriptstyle f \\ Y & \xrightarrow{\mathrm{id}_Y} & Y & \xrightarrow{\mathrm{id}_Y} & Y \end{array}$$
> The top composite is $f^{-1} f = \mathrm{id}_X$, the bottom composite is $\mathrm{id}_Y$, and the squares commute ($\mathrm{id}_Y \circ f = f = \mathrm{id}_Y \circ f$ and $f \circ f^{-1} = \mathrm{id}_Y = \mathrm{id}_Y \circ \mathrm{id}_Y$). So $f$ is a retract of $\mathrm{id}_Y \in \mathcal{W}$, and by MC3 (retract-closure of $\mathcal{W}$), $f \in \mathcal{W}$.

**Step 3: The cancellation statements.**

> [!note]- Derivation
> Suppose $g \circ f$ and $f$ are weak equivalences. The three composable maps are $f$, $g$, $g \circ f$. Two of them ($f$ and $g \circ f$) lie in $\mathcal{W}$, so by MC2 the third, $g$, lies in $\mathcal{W}$. Symmetrically, if $g \circ f$ and $g$ are weak equivalences, then two of $\{f, g, gf\}$ are weak equivalences, so $f$ is. This is the left- and right-cancellation property of weak equivalences.

> [!note]- Complete formal solution
> **(a)** The three classes of a model structure contain all identities and are closed under composition (part of the definition of a model structure / Hovey's formulation; closure under composition for $\mathcal{W}$ also follows from MC2). Hence $\mathrm{id}_X \in \mathcal{W}$ and $\mathcal{W}$ is closed under composition.
>
> **(b)** An isomorphism $f : X \to Y$ is a retract of $\mathrm{id}_Y$ via the diagram with top row $X \xrightarrow{f} Y \xrightarrow{f^{-1}} X$, bottom row $Y \xrightarrow{\mathrm{id}} Y \xrightarrow{\mathrm{id}} Y$, and verticals $f, \mathrm{id}_Y, f$; the horizontal composites are $f^{-1}f = \mathrm{id}_X$ and $\mathrm{id}_Y$. Since $\mathrm{id}_Y \in \mathcal{W}$ (part a) and $\mathcal{W}$ is retract-closed (MC3), $f \in \mathcal{W}$.
>
> **(c)** If $gf, f \in \mathcal{W}$, then two of $f, g, gf$ are in $\mathcal{W}$, so by MC2 $g \in \mathcal{W}$. If $gf, g \in \mathcal{W}$, then two of $f, g, gf$ are in $\mathcal{W}$, so by MC2 $f \in \mathcal{W}$. $\blacksquare$

---

# Key Takeaways

**Two-out-of-three is the universal tool for proving a map is a weak equivalence, and the skill is choosing the right composite.** Almost every "is this map a weak equivalence?" question in the subject is answered by exhibiting a composite in which the unknown map appears alongside two known weak equivalences. The trigger is: you want to certify $g \in \mathcal{W}$ and you can write $g$ as part of a composite $g \circ f$ or $h \circ g$ where the other pieces are understood. This is the homotopy-theoretic analogue of the way isomorphisms are propagated in ordinary category theory, and internalizing "to show a map is a weak equivalence, sandwich it" resolves a large fraction of routine verifications. The cancellation property proved in (c) is the form you reach for most often.

**Isomorphisms are weak equivalences for a structural reason — they are retracts of identities — not by fiat.** It is tempting to simply declare isomorphisms to be weak equivalences, but the axioms force it, and the forcing is instructive: an isomorphism sits inside an identity as a retract, and weak equivalences inherit membership from retracts (MC3). This same retract-of-identity argument shows that *any* class closed under retracts contains all isomorphisms, which is why isomorphisms are automatically cofibrations and fibrations too (trivial ones, in fact). Recognizing "isomorphism = retract of identity" as the bridge is the transferable insight, and it reappears whenever you need to show a degenerate map lies in a lifting-defined or retract-closed class.

**The axioms encode that weak equivalences behave *exactly* like isomorphisms, except they need not be invertible in $\mathcal{M}$ itself.** Two-out-of-three, closure under composition, and containing identities are precisely the properties of the class of isomorphisms in any category — the model-category axioms impose them on $\mathcal{W}$ so that $\mathcal{W}$ becomes "isomorphisms after localization." This is the conceptual content of the exercise: $\mathcal{W}$ is a *would-be* class of isomorphisms, and MC2 plus MC3 are the minimal closure properties guaranteeing it can be consistently inverted. When you later build $\mathrm{Ho}(\mathcal{M})$ via [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]], these are exactly the properties that make the inversion coherent.
