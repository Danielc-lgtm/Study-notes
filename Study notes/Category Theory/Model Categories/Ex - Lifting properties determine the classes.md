---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Model Category"
  - "Def - Lifting Property and the Retract Argument"
  - "Thm - The Retract Argument"
  - "Thm - Closure Properties of the Model Structure"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{M}$ be a model category. Prove that a map $f$ is a **cofibration if and only if it has the left lifting property with respect to every trivial fibration.** Then deduce, as corollaries, that:

(a) the cofibrations are closed under retracts;

(b) the cofibrations are closed under pushout (the [[Def - Pullback and Pushout|cobase change]] of a cofibration is a cofibration);

(c) the cofibrations are closed under coproducts.

Throughout, you may use the factorization axiom MC5, the lifting axiom MC4, the retract axiom MC3, and the retract argument; you may *not* assume the closure theorem [[Thm - Closure Properties of the Model Structure]] as a black box — you are proving (the cofibration part of) it.

**Recall:**

![[Def - Lifting Property and the Retract Argument#The Definition]]

The retract argument, the key tool:

![[Thm - The Retract Argument#Statement]]

A map factors (MC5) as a cofibration followed by a trivial fibration, and as a trivial cofibration followed by a fibration; cofibrations lift against trivial fibrations (MC4); each class is retract-closed (MC3).

---

# Convergent Strategy

**Problem class:** This is the substantial half of an axiom-consequence theorem — proving the lifting characterization of cofibrations and then deriving closure properties. It is the central instance of the "establish closure" target on the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Sources and Targets|topic page]], and it is the workhorse behind operation 8 ("recognize a class by its lifting property").

**Assumption pattern:** The given is the full model structure. The recognizable feature is that one direction of the iff is the axiom MC4 (cofibration $\Rightarrow$ lifts) and the other direction needs a *construction* — and the only construction available that turns a lifting property into class membership is the retract argument applied to a factorization. Spotting that you must factor the map first is the key.

**Theorem routing:** The route is: forward direction from MC4; backward direction by factoring (MC5), lifting against the produced trivial fibration, and applying [[Thm - The Retract Argument|the retract argument]] plus MC3. The corollaries then follow formally because any class defined by a one-sided lifting property is automatically closed under retracts, pushouts, and coproducts.

**Key decision point:** The non-obvious move is in the backward direction: given that $f$ lifts against all trivial fibrations, you do not know $f$ is a cofibration yet, so you must *manufacture* a cofibration to retract onto — which you do by factoring $f$. Choosing to factor as (cofibration, trivial fibration), so that $f$ lifts against the second factor, is the decisive choice; the (trivial cofibration, fibration) factorization would be useless here.

---

# Legal Operations Used

1. **Operation 1 from the topic page (factor a map).** The backward direction begins by factoring $f$ as a cofibration followed by a trivial fibration, manufacturing the cofibration that $f$ will be shown to retract onto.

2. **Operation 3 from the topic page (run the retract argument).** The factorization plus the lifting hypothesis feed [[Thm - The Retract Argument|the retract argument]] to exhibit $f$ as a retract of its cofibration factor.

3. **Operation 9 from the topic page (push out a cofibration).** Corollary (b) is the statement that this operation is legal, proved here from the lifting characterization.

---

# Hints

> [!note]- Hint 1
> The forward direction ("cofibration $\Rightarrow$ lifts against trivial fibrations") is *exactly* the lifting axiom MC4. Do not overthink it.

> [!note]- Hint 2
> For the backward direction, you cannot check "$f$ is a cofibration" directly. Factor $f = p \circ i$ using MC5, with $i$ a cofibration and $p$ a trivial fibration. Now what does your hypothesis say about $f$ and $p$?

> [!note]- Hint 3
> $f$ lifts against all trivial fibrations, and $p$ is a trivial fibration, so $f$ lifts against $p$. By [[Thm - The Retract Argument|the retract argument]], $f$ is a retract of $i$. Now use that $i$ is a cofibration and MC3.

> [!note]- Hint 4
> For the corollaries: once you know "cofibration = LLP against all trivial fibrations," each corollary is a formal property of *any* class defined by a left lifting property. For pushouts, take a square testing the pushout against a trivial fibration, restrict it to the original cofibration, lift, and extend over the pushout by its universal property. Coproducts are the special case of pushout (or argued the same way).

---

# Solution

The proof establishes the iff — forward by MC4, backward by factor-lift-retract — and then notes that each corollary is automatic for a class defined by a left lifting property. The corollaries reuse the standard "restrict the square, lift, extend by universal property" chase.

**Step 1: Forward direction.**

Every cofibration has the LLP against every trivial fibration.

> [!note]- Derivation
> This is the cofibration/trivial-fibration clause of the lifting axiom MC4: in any square with a cofibration on the left and a trivial fibration on the right, a diagonal lift exists.

**Step 2: Backward direction.**

If $f$ has the LLP against every trivial fibration, then $f$ is a cofibration.

> [!note]- Derivation
> By MC5, factor $f = p \circ i$ with $i$ a cofibration and $p$ a trivial fibration. By hypothesis $f$ lifts against every trivial fibration, in particular against $p$. By [[Thm - The Retract Argument|the retract argument]] (LLP form), $f$ is a retract of $i$. Since $i$ is a cofibration and cofibrations are closed under retracts (MC3), $f$ is a cofibration.

**Step 3: Corollary (a) — retract closure.**

> [!note]- Derivation
> Let $f$ be a retract of a cofibration $g$. By the iff, $g$ has the LLP against all trivial fibrations. We show $f$ does too. Given a retract diagram $A \xrightarrow{a} A' \xrightarrow{a'} A$, $B \xrightarrow{b} B' \xrightarrow{b'} B$ (composites identities) with $g : A' \to B'$, and a square testing $f$ against a trivial fibration $p$ (top $u$, bottom $v$), precompose with the retraction-side maps $a', b'$ to get a square testing $g$ against $p$. Lift it to $\ell : B' \to X$, and then $\ell \circ b : B \to X$ lifts the original square. So $f$ has the LLP against all trivial fibrations, hence is a cofibration. (This re-proves MC3 for cofibrations from the lifting characterization.)

**Step 4: Corollary (b) — pushout closure.**

> [!note]- Derivation
> Let $f : A \to B$ be a cofibration and form the pushout along any $A \to A''$, giving $f'' : A'' \to B'' = A'' \sqcup_A B$. Given a square testing $f''$ against a trivial fibration $p$ (top $u : A'' \to X$, bottom $v : B'' \to Y$), restrict along the pushout maps $A \to A''$ and $B \to B''$ to a square testing $f$ against $p$; lift it to $\ell : B \to X$. Now $u : A'' \to X$ and $\ell : B \to X$ agree after restriction to $A$, so by the universal property of the pushout they assemble to $\ell'' : B'' \to X$ with $\ell'' \circ f'' = u$ and $p \circ \ell'' = v$. Thus $f''$ has the LLP against all trivial fibrations and is a cofibration.

**Step 5: Corollary (c) — coproduct closure.**

> [!note]- Derivation
> Let $\{f_j : A_j \to B_j\}$ be cofibrations and form $\bigsqcup f_j : \bigsqcup A_j \to \bigsqcup B_j$. Given a square testing $\bigsqcup f_j$ against a trivial fibration $p$, restrict to each summand to get a square testing $f_j$, lift each to $\ell_j : B_j \to X$, and assemble $\ell = (\ell_j) : \bigsqcup B_j \to X$ by the universal property of the coproduct. It lifts the original square, so $\bigsqcup f_j$ has the LLP against all trivial fibrations and is a cofibration. (Equivalently, a coproduct is a pushout over the initial object, so this is a case of (b).)

> [!note]- Complete formal solution
> **Iff.** ($\Rightarrow$) A cofibration lifts against every trivial fibration by MC4. ($\Leftarrow$) If $f$ lifts against every trivial fibration, factor $f = p \circ i$ (MC5) with $i$ a cofibration and $p$ a trivial fibration; then $f$ lifts against $p$, so by [[Thm - The Retract Argument|the retract argument]] $f$ is a retract of $i$, hence a cofibration by MC3.
>
> **(a)** A retract of a cofibration $g$ has the LLP against all trivial fibrations (paste the retract into any lifting square, lift $g$, push the lift back), hence is a cofibration.
>
> **(b)** A pushout $f''$ of a cofibration $f$ has the LLP against any trivial fibration $p$: restrict a square for $f''$ to one for $f$, lift, and extend over the pushout by its universal property. Hence $f''$ is a cofibration.
>
> **(c)** A coproduct of cofibrations is a pushout over the initial object of cofibrations, hence a cofibration by (b); or directly assemble lifts on each summand. $\blacksquare$

---

# Key Takeaways

**The lifting characterization is what makes cofibrations recognizable in practice, and its proof is the universal "factor-lift-retract" template.** Without it, "cofibration" is an opaque membership in a class whose definition involves the factorizations; with it, a cofibration is anything passing a concrete lifting test against trivial fibrations. The proof template — factor the map, observe it lifts against the trivial-fibration factor, retract — is the single most reused argument in the foundations, appearing in every part of [[Thm - Closure Properties of the Model Structure]] and dualizing to characterize fibrations. The trigger is "I want to show this specific map is a cofibration but I have no access to the factorizations"; the reaction is "show it lifts against all trivial fibrations, then it *is* one."

**Every closure property of a lifting-defined class follows from one chase: restrict the square, lift, extend by the universal property.** Once a class is "maps with LLP against $\mathcal{R}$," it is automatically closed under retracts, pushouts, coproducts, and transfinite composites — because a lifting square testing the new map can always be restricted to a lifting square testing the building blocks, and the universal property of the (co)limit reassembles the partial lifts. This is why proving the lifting characterization *first* is so economical: the closure corollaries then cost almost nothing, whereas proving each closure property from the raw axioms would be painful. The transferable lesson is to always look for a lifting characterization of a class before trying to prove it has good closure properties.

**Pushout-closure of cofibrations is exactly what licenses cell attachment, the building block of the small object argument.** The corollary that the cobase change of a cofibration is a cofibration is the abstract statement that "attaching a cell keeps you in the class of cofibrations" — in $\mathbf{Top}$, attaching $D^n$ along $S^{n-1}$ is a pushout of the generating cofibration $S^{n-1} \hookrightarrow D^n$, and pushout-closure guarantees the result is a cofibration. This is the property the small object argument exploits transfinitely to build factorizations from a set of generators, and it is why this seemingly formal corollary is the practical heart of how cofibrations are constructed. Recognizing a construction as "a pushout of a known cofibration" is the standard way to certify cofibrancy in concrete model categories.
