---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Lifting Property and the Retract Argument"
  - "Thm - The Retract Argument"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Carry out the proof of the retract argument in full diagrammatic detail, in both forms.

(a) Suppose $f = p \circ i$ with $i : A \to C$, $p : C \to B$, and suppose $f$ has the **left lifting property** with respect to $p$. Construct the lift explicitly, draw the resulting retract diagram, and verify that both horizontal composites are identities and that all squares commute, concluding that $f$ is a retract of $i$.

(b) State and prove the **dual** form: if $f = p \circ i$ and $f$ has the **right lifting property** with respect to $i$, then $f$ is a retract of $p$. Do this directly (not merely by citing $\mathcal{M}^{op}$), so that you see the dual diagram explicitly.

**Recall:**

![[Def - Lifting Property and the Retract Argument#The Definition]]

The result to be proved:

![[Thm - The Retract Argument#Statement]]

---

# Convergent Strategy

**Problem class:** This is a diagram-chase verification of a named lemma — a "prove the construction works" problem. It belongs to no deep theorem-routing class; it is a direct application of operation 3 on the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Legal Operations|topic page]] ("run the retract argument"), executed with every arrow drawn.

**Assumption pattern:** The given data is a factorization $f = p \circ i$ together with a lifting property. The recognizable pattern is that the lifting property *produces a map*, and that produced map is the retraction needed to build the retract diagram. The skill is setting up the single square whose lift is exactly the retraction.

**Theorem routing:** The proof is self-contained from the definition of lifting and of retract. The route is: build the lifting square, extract the lift, assemble the retract diagram, verify the identities. The dual is the same with arrows reversed.

**Key decision point:** The crux — the place every attempt either succeeds or fails — is choosing the correct lifting square. You must put $i$ as the top edge and $p$ as the right edge (with $f$ on the left and $\mathrm{id}_B$ on the bottom), so that the lift is a map $B \to C$ that splits $p$ and that, composed appropriately, exhibits $f$ inside $i$. Any other square either does not commute or yields a useless lift.

---

# Legal Operations Used

1. **Operation 2 from the topic page (lift across a square).** The retraction is obtained as the diagonal filler of a single carefully chosen square; this is the only nontrivial step.

2. **Operation 3 from the topic page (run the retract argument).** The exercise is the detailed execution of this operation, making explicit the diagram that operation 3 invokes.

---

# Hints

> [!note]- Hint 1
> The retract diagram you are building has $f$ as the outer verticals and $i$ as the inner vertical. You need a map filling the bottom-left of the diagram — a map $B \to C$. Where can a map $B \to C$ come from? From a lifting property applied to a square.

> [!note]- Hint 2
> Form the square with $f : A \to B$ on the left, $p : C \to B$ on the right, $i : A \to C$ on top, and $\mathrm{id}_B : B \to B$ on the bottom. Check it commutes ($p i = f = \mathrm{id}_B \circ f$).

> [!note]- Hint 3
> The lift of that square is a map $r : B \to C$ with $r f = i$ and $p r = \mathrm{id}_B$. The equation $p r = \mathrm{id}_B$ is what makes the bottom row of the retract diagram compose to an identity.

> [!note]- Hint 4
> For the dual, reverse every arrow: factor $f = p \circ i$, form the square with $f$ on the right, $i$ on the left, $\mathrm{id}_A$ on top, $p$ on the bottom; the RLP of $f$ against $i$ gives a section $s : C \to A$ with $i s = \mathrm{id}_C$... track the indices and you get $f$ as a retract of $p$.

---

# Solution

The solution builds, in each part, the one lifting square whose diagonal is the retraction, then assembles the retract diagram and checks the two horizontal composites are identities. Part (b) mirrors part (a) with arrows reversed.

**Step 1 (a): Set up the lifting square and extract the retraction.**

> [!note]- Derivation
> With $f = p \circ i$ and $f$ having the LLP against $p$, form the square
> $$\begin{array}{ccc} A & \xrightarrow{\ i\ } & C \\ \scriptstyle f \downarrow & & \downarrow \scriptstyle p \\ B & \xrightarrow{\ \mathrm{id}_B\ } & B \end{array}$$
> It commutes: $p \circ i = f = \mathrm{id}_B \circ f$. Since $f$ has the LLP against $p$, there is a diagonal $r : B \to C$ with $r \circ f = i$ (upper triangle) and $p \circ r = \mathrm{id}_B$ (lower triangle).

**Step 2 (a): Assemble the retract diagram and verify.**

> [!note]- Derivation
> Build
> $$\begin{array}{ccccc} A & \xrightarrow{\ \mathrm{id}_A\ } & A & \xrightarrow{\ \mathrm{id}_A\ } & A \\ \scriptstyle f \downarrow & & \downarrow \scriptstyle i & & \downarrow \scriptstyle f \\ B & \xrightarrow{\ r\ } & C & \xrightarrow{\ p\ } & B \end{array}$$
> *Top composite:* $\mathrm{id}_A \circ \mathrm{id}_A = \mathrm{id}_A$. *Bottom composite:* $p \circ r = \mathrm{id}_B$ (Step 1). *Left square:* down-then-right is $r \circ f = i$ (Step 1); right-then-down is $i \circ \mathrm{id}_A = i$. They agree. *Right square:* down-then-right is $p \circ i = f$ (the factorization); right-then-down is $f \circ \mathrm{id}_A = f$. They agree. Both horizontal composites are identities and all squares commute, so the diagram exhibits $f$ as a retract of $i$.

**Step 3 (b): The dual form.**

> [!note]- Derivation
> Suppose $f = p \circ i$ and $f$ has the RLP against $i$. Form the square
> $$\begin{array}{ccc} A & \xrightarrow{\ \mathrm{id}_A\ } & A \\ \scriptstyle i \downarrow & & \downarrow \scriptstyle f \\ C & \xrightarrow{\ p\ } & B \end{array}$$
> It commutes: $f \circ \mathrm{id}_A = f = p \circ i$. Since $f$ has the RLP against $i$, there is a diagonal $s : C \to A$ with $s \circ i = \mathrm{id}_A$ (upper triangle) and $f \circ s = p$ (lower triangle). Now assemble
> $$\begin{array}{ccccc} A & \xrightarrow{\ i\ } & C & \xrightarrow{\ s\ } & A \\ \scriptstyle f \downarrow & & \downarrow \scriptstyle p & & \downarrow \scriptstyle f \\ B & \xrightarrow{\ \mathrm{id}_B\ } & B & \xrightarrow{\ \mathrm{id}_B\ } & B \end{array}$$
> *Top composite:* $s \circ i = \mathrm{id}_A$ (the section equation). *Bottom composite:* $\mathrm{id}_B \circ \mathrm{id}_B = \mathrm{id}_B$. *Left square:* $p \circ i = f = \mathrm{id}_B \circ f$. *Right square:* $f \circ s = p = \mathrm{id}_B \circ p$ (the lift equation). All squares commute and both horizontal composites are identities, so $f$ is a retract of $p$.

> [!note]- Complete formal solution
> **(a)** Given $f = p \circ i$ with $f$ having the LLP against $p$: the square with left $f$, right $p$, top $i$, bottom $\mathrm{id}_B$ commutes since $pi = f$. Its lift $r : B \to C$ satisfies $rf = i$, $pr = \mathrm{id}_B$. The diagram with rows $A \xrightarrow{\mathrm{id}} A \xrightarrow{\mathrm{id}} A$ and $B \xrightarrow{r} C \xrightarrow{p} B$, verticals $f, i, f$, has horizontal composites $\mathrm{id}_A$ and $pr = \mathrm{id}_B$, and both squares commute ($rf = i$, $pi = f$). So $f$ is a retract of $i$.
>
> **(b)** Given $f = p \circ i$ with $f$ having the RLP against $i$: the square with left $i$, right $f$, top $\mathrm{id}_A$, bottom $p$ commutes since $f = pi$. Its lift $s : C \to A$ satisfies $si = \mathrm{id}_A$, $fs = p$. The diagram with rows $A \xrightarrow{i} C \xrightarrow{s} A$ and $B \xrightarrow{\mathrm{id}} B \xrightarrow{\mathrm{id}} B$, verticals $f, p, f$, has horizontal composites $si = \mathrm{id}_A$ and $\mathrm{id}_B$, and both squares commute ($pi = f$, $fs = p$). So $f$ is a retract of $p$. $\blacksquare$

---

# Key Takeaways

**The retraction is always the lift of a square in which the unknown map appears against its own factor.** The entire content of the retract argument is that a lifting property *manufactures the very retraction* you need: given $f = p \circ i$ and a lifting property of $f$, the diagonal of the square pitting $f$ against the relevant factor is the map that splits the factorization. The trigger to recognize is "I have a factorization and a lifting property and I want to conclude membership in a class" — and the reaction is "build the square with the factors on two edges and read off the lift." This move is reused every single time the lifting characterization of the classes is invoked in [[Thm - Closure Properties of the Model Structure]].

**Drawing the square with the correct edges is the whole skill, and it is forced by which composite must become an identity.** In the LLP case the lift must satisfy $p \circ r = \mathrm{id}_B$, so $p$ must be the right edge and $\mathrm{id}_B$ the bottom; in the RLP case the section must satisfy $s \circ i = \mathrm{id}_A$, so $i$ must be the left edge and $\mathrm{id}_A$ the top. Working backwards from "which horizontal composite needs to be an identity" tells you exactly how to orient the square. This back-design from the desired conclusion is a transferable diagram-chase technique: when you know what equation the lift must satisfy, the square that produces it is essentially determined.

**Proving the dual directly, rather than citing the opposite category, builds the reflex of reversing arrows.** Although the dual form follows formally from $\mathcal{M}^{op}$ (see [[Ex - The opposite of a model category]]), executing it by hand teaches you to reverse every arrow and reverse the composition order — turning the section $s : C \to A$ into the analogue of the retraction $r : B \to C$. The two diagrams are mirror images, and seeing them side by side cements the duality between LLP/cofibration arguments and RLP/fibration arguments. Once the mirror is internalized, you can confidently assert "by the dual retract argument" in proofs without re-deriving, which is how the lemma is actually used throughout the subject.
