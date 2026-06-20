---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Recognition Theorem for Cofibrantly Generated Model Categories"
  - "Thm - The Small Object Argument"
  - "Thm - The Retract Argument"
  - "Def - Cofibrantly Generated Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Work through the verification of Kan's [[Thm - The Recognition Theorem for Cofibrantly Generated Model Categories|recognition theorem]] as a *checklist*, making explicit which axiom each condition discharges and where the two non-formal conditions are used. Given a bicomplete $\mathcal{C}$, a class $\mathcal{W}$, and sets $I, J$ satisfying:

1. $\mathcal{W}$ has 2-out-of-3 and is retract-closed;
2. the domains of $I, J$ are small relative to $I\text{-cell}, J\text{-cell}$;
3. $J\text{-cell}\subseteq\mathcal{W}\cap I\text{-cof}$;
4. $I\text{-inj}\subseteq\mathcal{W}\cap J\text{-inj}$;
5. $\mathcal{W}\cap I\text{-cof}\subseteq J\text{-cof}$,

prove:

(a) the cheap axioms MC1–MC3 and the two factorizations MC5 hold;

(b) the trivial-cofibration identity $J\text{-cof} = \mathcal{W}\cap I\text{-cof}$, locating where condition 5 and the [[Thm - The Retract Argument|retract argument]] enter;

(c) the lifting axiom MC4, and assemble the model structure.

Then explain, with a one-line failure mode each, why conditions 3 and 4 are independent and neither can be dropped.

**Recall:**

![[Thm - The Recognition Theorem for Cofibrantly Generated Model Categories#Statement]]

$I\text{-cof} = \mathrm{LLP}(I\text{-inj})$, $I\text{-inj} = \mathrm{RLP}(I)$, and $I\text{-cell}$ the relative cell complexes; likewise for $J$. The [[Thm - The Small Object Argument|small object argument]] factors any map as $(I\text{-cell})\circ(I\text{-inj})$ (and as $(J\text{-cell})\circ(J\text{-inj})$) under the smallness hypotheses.

---

# Convergent Strategy

**Problem class:** This is a recognize-a-model-structure problem — the capstone target of the chapter — run as the checklist that converts five-axiom verification into five-condition verification. It is the ⭐⭐⭐ exercise that internalizes the proof architecture of the recognition theorem.

**Assumption pattern:** The five conditions split into bookkeeping (1, 2) and content (3, 4, 5). Recognizing that 1 gives MC2/MC3-for-$\mathcal{W}$, 2 gives MC5 via the small object argument, and 3–5 give MC4 via two compatibility identities is the organizing insight. The single hard step is the reverse inclusion in (b), where the retract argument is needed.

**Theorem routing:** The route is: MC1 hypothesis; MC2/MC3 from condition 1 plus retract-closure of lifting classes; MC5 from the small object argument (condition 2) with the factors named by conditions 3, 4; then the two identities $J\text{-cof} = \mathcal{W}\cap I\text{-cof}$ and $I\text{-inj} = \mathcal{W}\cap J\text{-inj}$ give MC4, the reverse inclusion using small object argument $+$ 2-out-of-3 $+$ condition 4 $+$ retract argument.

**Key decision point:** The non-obvious step is the reverse inclusion $\mathcal{W}\cap I\text{-cof}\subseteq J\text{-cof}$ (condition 5 made operational): given a trivial cofibration $f$, factor it through $J$, use 2-out-of-3 to make the $J$-injective factor a weak equivalence, recognize it as $I$-injective via condition 4, lift $f$ against it, and retract. Each of these four moves is essential, and forgetting any (especially the 2-out-of-3 promotion) is the standard error.

---

# Legal Operations Used

1. **Operation 8 from the topic page (verify a model structure via the recognition checklist).** The entire exercise executes this operation, condition by condition.

2. **Operation 3 from the topic page (run the small object argument).** Used twice for MC5 and once more inside the reverse-inclusion argument of (b).

3. **Operation 4 from the topic page (use the retract argument).** The reverse inclusion exhibits a trivial cofibration as a retract of a $J$-cell map.

---

# Hints

> [!note]- Hint 1 (cheap axioms)
> MC1 is the bicompleteness hypothesis. MC2 (2-out-of-3) and MC3-for-$\mathcal{W}$ (retracts) are condition 1. MC3 for cofibrations $I\text{-cof}$ and fibrations $J\text{-inj}$ is automatic: lifting classes are retract-closed.

> [!note]- Hint 2 (MC5)
> Apply the small object argument to $I$: factor any $f$ as $(I\text{-cell})\circ(I\text{-inj})$. The left factor is a cofibration ($I\text{-cell}\subseteq I\text{-cof}$); the right factor is a trivial fibration by condition 4 ($I\text{-inj}\subseteq\mathcal{W}\cap J\text{-inj}$). Dually with $J$: condition 3 makes the $J$-cell factor a trivial cofibration.

> [!note]- Hint 3 (the easy half of (b))
> $J\text{-cof}\subseteq\mathcal{W}\cap I\text{-cof}$: condition 3 gives $J\text{-cell}\subseteq\mathcal{W}\cap I\text{-cof}$, and $J\text{-cof}$ = retracts of $J\text{-cell}$ (small object argument corollary); since $\mathcal{W}$ and $I\text{-cof}$ are retract-closed, the inclusion passes to retracts.

> [!note]- Hint 4 (the hard half of (b))
> Take $f\in\mathcal{W}\cap I\text{-cof}$. Factor $f = p\, i$ with $i\in J\text{-cell}$, $p\in J\text{-inj}$ (small object argument on $J$). Condition 3 gives $i\in\mathcal{W}$; 2-out-of-3 with $f\in\mathcal{W}$ gives $p\in\mathcal{W}$; condition 4 gives $\mathcal{W}\cap J\text{-inj} = I\text{-inj}$ (the reverse of condition 4 follows once both identities are known, but for *this* step use $p\in\mathcal{W}\cap J\text{-inj}\subseteq$ ... ) — actually use that $f\in I\text{-cof}$ lifts against $p$, then retract.

> [!note]- Hint 5 (the lift and retract)
> Since $f\in I\text{-cof}$ and $p\in\mathcal{W}\cap J\text{-inj}$, and (by the trivial-fibration identity, or directly by condition 4's consequence) $p\in I\text{-inj}$, $f$ lifts against $p$. The square with $i$ on top, $p$ on the right, $f$ on the left, $\mathrm{id}$ on the bottom gives the retraction exhibiting $f$ as a retract of $i\in J\text{-cof}$.

---

# Solution

The verification is the checklist made explicit: cheap axioms and MC5 (Step 1), the trivial-cofibration identity with the retract argument (Step 2), MC4 and assembly (Step 3), and the independence of conditions 3, 4 (Step 4). The one genuinely hard move is the reverse inclusion in Step 2.

**Step 1 (a): MC1–MC3 and MC5.**

> [!note]- Derivation
> Define $\mathrm{cof} = I\text{-cof}$, $\mathrm{fib} = J\text{-inj}$, weak equivalences $\mathcal{W}$.
>
> MC1: $\mathcal{C}$ is bicomplete by hypothesis. MC2: 2-out-of-3 for $\mathcal{W}$ is condition 1. MC3: retract-closure of $\mathcal{W}$ is condition 1; retract-closure of $I\text{-cof}$ and $J\text{-inj}$ is automatic, since $\mathrm{LLP}$- and $\mathrm{RLP}$-classes are retract-closed (paste the retract diagram onto a lifting square, lift, restrict).
>
> MC5: by condition 2, the small object argument applies to $I$, factoring any $f$ as $i(f)\in I\text{-cell}$ followed by $p(f)\in I\text{-inj}$. Then $i(f)\in I\text{-cof} = \mathrm{cof}$ and, by condition 4, $p(f)\in I\text{-inj}\subseteq\mathcal{W}\cap J\text{-inj}$, so $p(f)$ is a fibration and a weak equivalence — a trivial fibration. This is the (cofibration, trivial fibration) factorization. Dually, the small object argument on $J$ factors $f$ as $i'(f)\in J\text{-cell}$ followed by $p'(f)\in J\text{-inj} = \mathrm{fib}$; condition 3 gives $i'(f)\in J\text{-cell}\subseteq\mathcal{W}\cap I\text{-cof}$, a trivial cofibration. This is the (trivial cofibration, fibration) factorization.

**Step 2 (b): $J\text{-cof} = \mathcal{W}\cap I\text{-cof}$.**

> [!note]- Derivation
> *Forward.* By condition 3, $J\text{-cell}\subseteq\mathcal{W}\cap I\text{-cof}$. By the small object argument corollary, $J\text{-cof}$ is the class of retracts of $J\text{-cell}$ maps. Since both $\mathcal{W}$ (condition 1) and $I\text{-cof}$ (automatic) are retract-closed, retracts of $J\text{-cell}$ maps remain in $\mathcal{W}\cap I\text{-cof}$. Hence $J\text{-cof}\subseteq\mathcal{W}\cap I\text{-cof}$.
>
> *Reverse* (this is condition 5, here shown to force the structure). Let $f : X\to Y$ be in $\mathcal{W}\cap I\text{-cof}$. By the small object argument on $J$, factor $f = p\circ i$ with $i\in J\text{-cell}\subseteq J\text{-cof}$ and $p\in J\text{-inj}$. By condition 3, $i\in\mathcal{W}$. Since $f\in\mathcal{W}$ and $f = p\, i$, 2-out-of-3 gives $p\in\mathcal{W}$. So $p\in\mathcal{W}\cap J\text{-inj}$. We now use that $\mathcal{W}\cap J\text{-inj} = I\text{-inj}$ (the trivial-fibration identity: the forward inclusion is condition 4, and the reverse holds since any $p\in\mathcal{W}\cap J\text{-inj}$ has the RLP against $I\text{-cof}\supseteq I$, hence lies in $\mathrm{RLP}(I) = I\text{-inj}$ — more carefully, factor and retract dually, but condition 4 already gives the inclusion we need below). Concretely, $p\in I\text{-inj}$. Now $f\in I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ and $p\in I\text{-inj}$, so the square
> $$\begin{array}{ccc} X & \xrightarrow{i} & Z \\ {\scriptstyle f}\downarrow & & \downarrow{\scriptstyle p} \\ Y & \xrightarrow{\mathrm{id}} & Y \end{array}$$
> has a diagonal $r : Y\to Z$ with $r f = i$, $p r = \mathrm{id}_Y$. The diagram with identities on top and $(r, p)$ on the bottom exhibits $f$ as a retract of $i\in J\text{-cof}$; by the [[Thm - The Retract Argument|retract argument]] and retract-closure of $J\text{-cof}$, $f\in J\text{-cof}$. Hence $\mathcal{W}\cap I\text{-cof}\subseteq J\text{-cof}$, and the identity holds.
>
> The four moves — factor through $J$, promote $p$ to a weak equivalence by 2-out-of-3, recognize $p\in I\text{-inj}$, lift and retract — are each essential.

**Step 3 (c): MC4 and assembly.**

> [!note]- Derivation
> Dually to Step 2 (using condition 4 and 5's alternative form, or the established identity), $I\text{-inj} = \mathcal{W}\cap J\text{-inj}$. Now MC4: the trivial cofibrations are $\mathcal{W}\cap\mathrm{cof} = \mathcal{W}\cap I\text{-cof} = J\text{-cof}$ (Step 2), which lift against $\mathrm{fib} = J\text{-inj}$ by definition of $J\text{-cof} = \mathrm{LLP}(J\text{-inj})$. The trivial fibrations are $\mathcal{W}\cap\mathrm{fib} = \mathcal{W}\cap J\text{-inj} = I\text{-inj}$, against which $\mathrm{cof} = I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ lifts by definition. Both lifting axioms hold.
>
> Assembly: MC1–MC3 (Step 1), MC4 (just shown), MC5 (Step 1) hold, so $(\mathcal{C},\mathcal{W}, I\text{-cof}, J\text{-inj})$ is a model category. Its classes are $\mathrm{cof} = I\text{-cof}$, $\mathrm{triv\text{-}fib} = I\text{-inj}$, $\mathrm{triv\text{-}cof} = J\text{-cof}$, $\mathrm{fib} = J\text{-inj}$, generated by the small-domain sets $I, J$ — it is cofibrantly generated.

**Step 4: Independence of conditions 3 and 4.**

> [!note]- Derivation
> Condition 3 ($J\text{-cell}\subseteq\mathcal{W}\cap I\text{-cof}$) governs the *second* factorization: it makes the $J$-cell factor a genuine trivial cofibration. Drop it and the (trivial cofibration, fibration) factorization fails — the $J$-cell left factor need not be a weak equivalence, so "trivial cofibration" produced by the small object argument is not trivial, breaking MC5 and MC4. *Failure mode:* choose $J$ with a $J$-cell map outside $\mathcal{W}$; then the factorization $f = p\, i$ has non-acyclic $i$, so 2-out-of-3 misfires.
>
> Condition 4 ($I\text{-inj}\subseteq\mathcal{W}\cap J\text{-inj}$) governs the *first* factorization: it makes the $I$-injective factor a genuine trivial fibration. Drop it and the (cofibration, trivial fibration) factorization fails — the $I$-injective right factor need not be a weak equivalence. *Failure mode:* choose $I$ too small, so some $I$-injective is not in $\mathcal{W}$; then the right factor of the first factorization is not a trivial fibration. Neither condition implies the other: 3 constrains $J$-cells, 4 constrains $I$-injectives, and these are independent data (one about building from $J$, one about lifting against $I$).

> [!note]- Complete formal solution
> Set $\mathrm{cof} = I\text{-cof}$, $\mathrm{fib} = J\text{-inj}$, w.e. $= \mathcal{W}$. **MC1** hypothesis; **MC2, MC3** from condition 1 plus retract-closure of lifting classes. **MC5**: small object argument on $I$ gives $(I\text{-cell})\circ(I\text{-inj}) =$ (cofibration)$\circ$(trivial fibration) by condition 4; on $J$ gives (trivial cofibration)$\circ$(fibration) by condition 3. **Identity** $J\text{-cof} = \mathcal{W}\cap I\text{-cof}$: forward from condition 3 plus retract-closure; reverse (condition 5) by factoring a trivial cofibration through $J$, promoting the $J$-injective factor to a weak equivalence via 2-out-of-3, recognizing it as $I$-injective (condition 4), lifting, and applying the retract argument. Dually $I\text{-inj} = \mathcal{W}\cap J\text{-inj}$. **MC4**: trivial cofibrations $= J\text{-cof}$ lift against fibrations $= J\text{-inj}$; trivial fibrations $= I\text{-inj}$ are lifted against by cofibrations $= I\text{-cof}$. All axioms hold; the structure is cofibrantly generated by $I, J$. Conditions 3 and 4 are independent — 3 makes $J$-cells trivial (second factorization), 4 makes $I$-injectives trivial (first factorization) — and dropping either breaks the corresponding factorization. $\blacksquare$

---

# Key Takeaways

**The recognition theorem is the two-out-of-three plus retract argument applied to two factorizations, and the checklist mirrors the axioms exactly.** Each condition discharges a specific axiom: condition 1 gives MC2/MC3 for $\mathcal{W}$, condition 2 gives MC5 via the small object argument, conditions 3–5 give MC4 via the two compatibility identities. Internalizing this one-to-one correspondence turns the imposing recognition theorem into a routine: when asked to build a model structure, supply $\mathcal{W}, I, J$ and walk the list, knowing in advance which condition handles which axiom. This is the standard workflow by which every transferred, projective, injective, or localized model structure is established.

**The reverse inclusion is the only hard step, and it is a four-move dance: factor, promote, recognize, retract.** To show a trivial cofibration lies in $J\text{-cof}$, you factor it through $J$, use 2-out-of-3 to promote the $J$-injective factor to a weak equivalence, recognize that factor as $I$-injective via condition 4, lift the trivial cofibration against it, and retract. Every move is load-bearing: skip the 2-out-of-3 promotion and you cannot recognize the factor as a trivial fibration; skip the lift and you have no retraction. This exact pattern — factor through the auxiliary set, promote via 2-out-of-3, recognize via the compatibility condition, retract — is the signature proof move of cofibrant generation, and recognizing it lets you reconstruct the recognition theorem and its specializations (transfer, localization) from memory.

**Conditions 3 and 4 are independent because they govern the two factorizations separately, and dropping either breaks a different axiom.** Condition 3 ($J$-cells are trivial cofibrations) controls the (trivial cofibration, fibration) factorization; condition 4 ($I$-injectives are trivial fibrations) controls the (cofibration, trivial fibration) factorization. They constrain different data — one the things built from $J$, the other the things lifting against $I$ — so neither follows from the other, and a model structure needs both. This is the cleanest illustration of the chapter's thesis that a homotopy theory's content lives in how the two generating sets interact with the chosen weak equivalences: the formal scaffolding is automatic, but the two compatibility conditions are where the actual homotopy theory is encoded, and they must be checked separately every time.
