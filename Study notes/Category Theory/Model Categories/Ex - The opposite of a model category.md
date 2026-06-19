---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Model Category"
  - "Def - Opposite Category and Duality"
  - "Def - Lifting Property and the Retract Argument"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{M}$ be a model category. Show that the opposite category $\mathcal{M}^{op}$ is again a model category, where:
- the weak equivalences of $\mathcal{M}^{op}$ are the (opposites of the) weak equivalences of $\mathcal{M}$;
- the **cofibrations of $\mathcal{M}^{op}$ are the fibrations of $\mathcal{M}$**, and the **fibrations of $\mathcal{M}^{op}$ are the cofibrations of $\mathcal{M}$**.

Verify that each of the five axioms for $\mathcal{M}^{op}$ follows from the corresponding axiom for $\mathcal{M}$, tracking carefully which axiom maps to which. Then explain how this single fact lets every theorem about cofibrations be converted into a theorem about fibrations for free, and identify what a cylinder object and left homotopy in $\mathcal{M}$ become in $\mathcal{M}^{op}$.

**Recall:**

The [[Def - Opposite Category and Duality|opposite category]] $\mathcal{M}^{op}$ has the same objects as $\mathcal{M}$ and a morphism $X \to Y$ in $\mathcal{M}^{op}$ for each morphism $Y \to X$ in $\mathcal{M}$, with composition reversed. Limits in $\mathcal{M}$ are colimits in $\mathcal{M}^{op}$ and vice versa; the initial object of $\mathcal{M}$ is the terminal object of $\mathcal{M}^{op}$.

![[Def - Model Category#The Definition]]

The [[Def - Lifting Property and the Retract Argument|left and right lifting properties]] are interchanged under reversal of all arrows: $i$ has the LLP against $p$ in $\mathcal{M}$ iff (the opposite of) $p$ has the LLP against (the opposite of) $i$ in $\mathcal{M}^{op}$.

---

# Convergent Strategy

**Problem class:** This is a duality problem — establishing that the model-category axioms are self-dual under reversing arrows and swapping cofibrations with fibrations. It is the structural backbone behind operation 7 on the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Legal Operations|topic page]] ("dualize"), and it is what halves the labour in the entire subject.

**Assumption pattern:** The recognizable feature is that every concept in the definition comes in a left/right or initial/terminal pair, and reversing arrows swaps the members of each pair. Recognizing that the axiom list is *symmetric* under this swap — cofibration $\leftrightarrow$ fibration, LLP $\leftrightarrow$ RLP, colimit $\leftrightarrow$ limit — is the whole insight.

**Theorem routing:** No theorem is needed; the proof is a systematic translation. The route is to check, axiom by axiom, that the $\mathcal{M}^{op}$ version of axiom MC$k$ is exactly the $\mathcal{M}$ version of the *dual* axiom — MC1 is self-dual, MC2 is self-dual (composition reverses but "two of three" is symmetric), MC3 is self-dual, and MC4/MC5 each swap their two clauses.

**Key decision point:** The one place to be careful is tracking the factorization axiom MC5: in $\mathcal{M}$ a map factors as (cofibration, trivial fibration) and as (trivial cofibration, fibration). Reversing the arrows turns the first into a factorization as (trivial fibration of $\mathcal{M}$, cofibration of $\mathcal{M}$) read backwards — and you must check this is exactly the (trivial cofibration of $\mathcal{M}^{op}$, fibration of $\mathcal{M}^{op}$) factorization. Getting the order reversal right is the crux.

---

# Legal Operations Used

1. **Operation 7 from the topic page (dualize).** This exercise *is* the justification of that operation: it proves that passing to $\mathcal{M}^{op}$ is a legal move that preserves the model-category structure with cofibrations and fibrations swapped.

2. **Operation 2 from the topic page (lift across a square), tracked under reversal.** The lifting axiom MC4 is checked by observing that a lifting square in $\mathcal{M}^{op}$ is a lifting square in $\mathcal{M}$ with the arrows reversed and the left/right roles swapped.

---

# Hints

> [!note]- Hint 1
> Write out what each piece of data of $\mathcal{M}^{op}$ is in terms of $\mathcal{M}$: objects are the same, a map $X \to Y$ in $\mathcal{M}^{op}$ is a map $Y \to X$ in $\mathcal{M}$, the initial object of $\mathcal{M}^{op}$ is $*_\mathcal{M}$, the terminal is $\varnothing_\mathcal{M}$, limits and colimits swap.

> [!note]- Hint 2
> For MC4: a commuting square in $\mathcal{M}^{op}$ with $i^{op}$ on the left and $p^{op}$ on the right corresponds to a square in $\mathcal{M}$ with $p$ on the left and $i$ on the right (everything reversed). A lift in one is a lift in the other.

> [!note]- Hint 3
> For MC5: the factorization $f = p \circ i$ in $\mathcal{M}$ becomes $f^{op} = i^{op} \circ p^{op}$ in $\mathcal{M}^{op}$. If $i$ is a cofibration of $\mathcal{M}$ then $i^{op}$ is a fibration of $\mathcal{M}^{op}$; if $p$ is a trivial fibration of $\mathcal{M}$ then $p^{op}$ is a trivial cofibration of $\mathcal{M}^{op}$. So the $\mathcal{M}$-factorization (cofibration, trivial fibration) becomes the $\mathcal{M}^{op}$-factorization (trivial cofibration, fibration).

> [!note]- Hint 4
> For the cylinder: a cylinder object in $\mathcal{M}$ factors the fold map $A \sqcup A \to A$ (a colimit construction). In $\mathcal{M}^{op}$ this becomes a factorization of the diagonal $A \to A \times A$ (a limit construction) — which is exactly a path object. So a path object in $\mathcal{M}$ is a cylinder object in $\mathcal{M}^{op}$, and right homotopy in $\mathcal{M}$ is left homotopy in $\mathcal{M}^{op}$.

---

# Solution

The proof is a disciplined dictionary: every datum and axiom of $\mathcal{M}^{op}$ is translated back to $\mathcal{M}$, where it becomes the dual datum or axiom, which $\mathcal{M}$ satisfies by hypothesis. The cylinder/path swap is read off at the end.

**Step 1: The data of $\mathcal{M}^{op}$ translates correctly.**

> [!note]- Derivation
> $\mathcal{M}^{op}$ has the same objects as $\mathcal{M}$. We declare: weak equivalences of $\mathcal{M}^{op}$ are the reversals of weak equivalences of $\mathcal{M}$; cofibrations of $\mathcal{M}^{op}$ are the reversals of fibrations of $\mathcal{M}$; fibrations of $\mathcal{M}^{op}$ are the reversals of cofibrations of $\mathcal{M}$. Consequently a *trivial* cofibration of $\mathcal{M}^{op}$ (cofibration $\cap\, \mathcal{W}$) is the reversal of a trivial fibration of $\mathcal{M}$, and a trivial fibration of $\mathcal{M}^{op}$ is the reversal of a trivial cofibration of $\mathcal{M}$. The initial object of $\mathcal{M}^{op}$ is the terminal $*$ of $\mathcal{M}$ and vice versa.

**Step 2: MC1 (bicompleteness) holds.**

> [!note]- Derivation
> A small limit in $\mathcal{M}^{op}$ is a small colimit in $\mathcal{M}$, which exists; a small colimit in $\mathcal{M}^{op}$ is a small limit in $\mathcal{M}$, which exists. So $\mathcal{M}^{op}$ is bicomplete. MC1 is self-dual.

**Step 3: MC2 and MC3 hold.**

> [!note]- Derivation
> MC2: if $f^{op}, g^{op}$ are composable in $\mathcal{M}^{op}$ with composite $f^{op} \circ g^{op} = (g \circ f)^{op}$, then two of $f^{op}, g^{op}, (gf)^{op}$ being weak equivalences means two of $f, g, gf$ are weak equivalences in $\mathcal{M}$, so the third is (MC2 in $\mathcal{M}$), hence the third in $\mathcal{M}^{op}$ is. MC2 is self-dual. MC3: a retract diagram in $\mathcal{M}^{op}$ is a retract diagram in $\mathcal{M}$ with arrows reversed; reversal sends "retract of a fibration" to "retract of a cofibration" etc., and since each class of $\mathcal{M}$ is retract-closed, so is each class of $\mathcal{M}^{op}$. MC3 is self-dual.

**Step 4: MC4 (lifting) holds.**

> [!note]- Derivation
> A commuting square in $\mathcal{M}^{op}$ with $i^{op}$ on the left and $p^{op}$ on the right corresponds, by reversing every arrow, to a commuting square in $\mathcal{M}$ with $p$ on the *left* and $i$ on the *right*. A diagonal lift in the $\mathcal{M}^{op}$-square is exactly a diagonal lift in the $\mathcal{M}$-square (the same morphism, reversed). Now suppose $i^{op}$ is a cofibration of $\mathcal{M}^{op}$ (so $i$ is a fibration of $\mathcal{M}$) and $p^{op}$ is a trivial fibration of $\mathcal{M}^{op}$ (so $p$ is a trivial cofibration of $\mathcal{M}$). The corresponding $\mathcal{M}$-square has the trivial cofibration $p$ on the left and the fibration $i$ on the right, which lifts by MC4 in $\mathcal{M}$. The other clause (trivial cofibration of $\mathcal{M}^{op}$ on the left, fibration on the right) corresponds to a cofibration / trivial fibration lifting in $\mathcal{M}$. So both clauses of MC4 in $\mathcal{M}^{op}$ follow from the two clauses of MC4 in $\mathcal{M}$ — with the clauses swapped.

**Step 5: MC5 (factorization) holds.**

> [!note]- Derivation
> A map $f^{op} : X \to Y$ in $\mathcal{M}^{op}$ is a map $f : Y \to X$ in $\mathcal{M}$. Factor $f = p \circ i$ in $\mathcal{M}$ with $i$ a cofibration, $p$ a trivial fibration. Reversing, $f^{op} = i^{op} \circ p^{op}$, where $p^{op}$ is a trivial cofibration of $\mathcal{M}^{op}$ and $i^{op}$ is a fibration of $\mathcal{M}^{op}$ — this is the (trivial cofibration, fibration) factorization required in $\mathcal{M}^{op}$. Symmetrically, the $\mathcal{M}$-factorization $f = q \circ j$ (trivial cofibration, fibration) reverses to the (cofibration, trivial fibration) factorization of $f^{op}$. So both factorizations of MC5 in $\mathcal{M}^{op}$ follow from those in $\mathcal{M}$, with the two factorizations swapped.

**Step 6: Consequences — free dualization, and cylinder/path swap.**

> [!note]- Derivation
> Since $\mathcal{M}^{op}$ is a model category, any theorem proved for all model categories applies to $\mathcal{M}^{op}$; translating its statement back through the dictionary (cofibration $\leftrightarrow$ fibration, colimit $\leftrightarrow$ limit, LLP $\leftrightarrow$ RLP) yields the dual theorem for $\mathcal{M}$. Concretely, a cylinder object in $\mathcal{M}$ factors the fold map $A \sqcup A \xrightarrow{\nabla} A$ as a cofibration followed by a weak equivalence; reversing, this is a factorization of the diagonal $A \xrightarrow{\Delta} A \times A$ as a weak equivalence followed by a fibration — exactly a path object in $\mathcal{M}^{op}$. Hence a path object for $A$ in $\mathcal{M}$ is a cylinder object for $A$ in $\mathcal{M}^{op}$, and a right homotopy in $\mathcal{M}$ is a left homotopy in $\mathcal{M}^{op}$. This is why one only proves cylinder/left-homotopy statements and gets the path/right-homotopy ones for free.

> [!note]- Complete formal solution
> Define $\mathcal{M}^{op}$ with weak equivalences $=$ reversals of $\mathcal{W}$, cofibrations $=$ reversals of fibrations of $\mathcal{M}$, fibrations $=$ reversals of cofibrations of $\mathcal{M}$.
>
> **MC1:** limits and colimits swap under op, and $\mathcal{M}$ is bicomplete, so $\mathcal{M}^{op}$ is. **MC2:** "two of three" is symmetric under reversing composition order, so it transfers. **MC3:** retract diagrams reverse to retract diagrams, and reversal swaps the classes consistently with their retract-closure in $\mathcal{M}$. **MC4:** a lifting square in $\mathcal{M}^{op}$ with a cofibration left / trivial fibration right reverses to a lifting square in $\mathcal{M}$ with a trivial cofibration left / fibration right, which lifts; the other clause reverses to the cofibration / trivial fibration clause. **MC5:** the $\mathcal{M}$-factorization (cofibration, trivial fibration) reverses to the $\mathcal{M}^{op}$-factorization (trivial cofibration, fibration), and vice versa.
>
> Hence $\mathcal{M}^{op}$ is a model category. A path object in $\mathcal{M}$ (factoring the diagonal) reverses to a cylinder object in $\mathcal{M}^{op}$ (factoring the fold), and right homotopy in $\mathcal{M}$ is left homotopy in $\mathcal{M}^{op}$, which is why every cofibration/left-homotopy theorem dualizes to a fibration/right-homotopy theorem for free. $\blacksquare$

---

# Key Takeaways

**The model-category axioms are self-dual, which is the deepest labour-saving fact in the subject.** Every definition comes in a dual pair — cofibration/fibration, initial/terminal, colimit/limit, LLP/RLP, cylinder/path, left/right homotopy — and the axioms are symmetric under swapping each pair. The consequence is that you only ever prove half the theorems: establish a statement about cofibrations and left homotopy, then invoke "$\mathcal{M}^{op}$ is a model category" to obtain the fibration / right-homotopy version with no further work. This is operation 7 on the topic page made rigorous, and recognizing when a result you need is the *dual* of one you have is a reflex worth building. The trigger is any fibration-or-limit statement whose cofibration-or-colimit analogue you already know.

**Tracking the order-reversal in factorizations is where duality arguments are won or lost.** Reversing arrows not only swaps cofibrations with fibrations but *reverses composition order*, so the factorization $f = p \circ i$ becomes $f^{op} = i^{op} \circ p^{op}$ — the factors trade places as well as classes. The common error is to swap the classes but forget to reverse the order, which produces a nonsensical "factorization." The same care is needed for any composite construction (mapping cylinders, towers, transfinite composites): under op, the order reverses. Once you internalize "op reverses both the arrows and their order," duality becomes mechanical.

**A path object is literally a cylinder object in the opposite category, which explains why the homotopy theory has a left/right symmetry.** The two notions of homotopy — left (via cylinders, sensitive to the domain) and right (via path objects, sensitive to the codomain) — are not two unrelated definitions but a single definition viewed in $\mathcal{M}$ and in $\mathcal{M}^{op}$. This is why the coincidence theorem (left homotopy = right homotopy on bifibrant objects) is so natural: bifibrancy is self-dual, and on self-dual objects the two views must agree. Whenever you find yourself proving something about right homotopy or path objects, check whether the left-homotopy version is already in hand and dualize; conversely, this symmetry is the reason [[Def - Cylinder Object, Path Object, and Homotopy]] develops only the left/cylinder side in detail.
