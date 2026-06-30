---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Cofiber and Fiber Sequence"
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a [[Def - Pointed Model Category Suspension and Loop|pointed model category]] and $f : X \to Y$ a map of cofibrant objects, with [[Def - Cofiber and Fiber Sequence|homotopy cofiber]] $i : Y \to C_f$.

1. Prove that the [[Def - Homotopy|homotopy]] cofiber of $i : Y \to C_f$ is canonically weakly equivalent to the [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma X$, by pasting homotopy-pushout squares.
2. Conclude that the cofiber sequence extends to the infinite **Puppe sequence**
$$X \xrightarrow{f} Y \xrightarrow{i} C_f \xrightarrow{\partial} \Sigma X \xrightarrow{-\Sigma f} \Sigma Y \to \cdots,$$
with each consecutive triple a cofiber sequence and $\partial$ the connecting map.
3. State the dual: the homotopy fiber of $p : F_f \to X$ is $\Omega Y$, giving the dual Puppe fiber sequence.

**Recall:**

![[Def - Cofiber and Fiber Sequence#The Definition]]

The [[Def - Cofiber and Fiber Sequence|homotopy cofiber]] $C_f$ of $f$ is the [[Def - Pullback and Pushout|homotopy pushout]] of $* \leftarrow X \xrightarrow{f} Y$; the [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma X$ is the homotopy pushout of $* \leftarrow X \rightarrow *$. The **pasting lemma** for homotopy pushouts: if the left square and the right square of a horizontal pair are homotopy pushouts, so is the outer rectangle.

---

# Convergent Strategy

**Problem class:** This is a "paste cartesian squares to extend a sequence" exercise — the structural computation that turns a three-term cofiber sequence into an infinite one. The routine is to stack two homotopy-pushout squares and apply the pasting lemma.

**Assumption pattern:** The assumptions are that $C_f$ is the homotopy pushout of $* \leftarrow X \xrightarrow{f} Y$ (a square with a corner at $*$) and that the cofiber of $i$ is again such a square. Stacking them, the shared edge $Y \to C_f$ is internal, and the outer rectangle is a homotopy pushout of $* \leftarrow X \rightarrow *$ — which is the suspension. The pasting lemma is the one structural fact that does all the work.

**Theorem routing:** The entire argument routes through the **pasting lemma for homotopy pushouts**: glue the cofiber square of $f$ to the cofiber square of $i$; the outer rectangle's homotopy-pushout property identifies $C_i = \Sigma X$. The dual routes through the pasting lemma for homotopy pullbacks.

**Key decision point:** The non-obvious choice is to set up the *second* square correctly — the cofiber square of $i : Y \to C_f$ has corners $Y, C_f, *, C_i$, and one must see that gluing it to the first square along the edge $Y \to C_f$ produces an outer rectangle with corners $X, *, *, C_i$, whose homotopy-pushout content is exactly $\Sigma X$. Choosing to collapse $Y$ (rather than $X$ again) is what makes the cone on $X$ reappear as the suspension.

---

# Legal Operations Used

1. **Operation 4 from the topic page (paste (co)cartesian squares to extend a sequence).** This is the central operation; the whole exercise is its prototype.

2. **Operation 3 from the topic page (recognize a homotopy pushout square with a corner at $*$).** Both squares are cofiber squares, identified by their $*$ corner.

3. **Operation 7 from the topic page (rotate a (co)fiber sequence).** Part (2) uses that each consecutive triple in the Puppe sequence is again a cofiber sequence — the rotation that makes the sequence infinite.

---

# Hints

> [!note]- Hint 1
> Draw two squares side by side. Left square: $X \to Y$ on top, $* \to C_f$ on bottom (the cofiber square of $f$). Right square: $Y \to C_f$ on top, $* \to C_i$ on bottom (the cofiber square of $i$). They share the edge $Y \to C_f$.

> [!note]- Hint 2
> The outer rectangle has top $X \to C_f$? No — re-read: the outer rectangle's top is $X \to Y \to C_f$ collapsed, and its corners are $X$, $*$ (from the left bottom-left), and $C_i$. Apply the pasting lemma: the outer rectangle is a homotopy pushout.

> [!note]- Hint 3
> The outer rectangle is the homotopy pushout of $* \leftarrow X \rightarrow *$ (both legs factoring through the collapses), which is exactly $\Sigma X$. Hence $C_i \simeq \Sigma X$.

---

# Solution

The solution pastes the cofiber square of $f$ onto the cofiber square of $i$ and reads $C_i = \Sigma X$ off the outer rectangle, then rotates to get the infinite Puppe sequence and dualizes.

**Step 1: $C_i \simeq \Sigma X$ by pasting.**

> [!note]- Derivation
> Set up two horizontally adjacent squares:
> $$
> \begin{array}{ccccc}
> X & \xrightarrow{\ f\ } & Y & \xrightarrow{\ i\ } & C_f \\
> \downarrow & & \downarrow & & \downarrow \\
> * & \xrightarrow{\ \ } & C_f & \xrightarrow{\ \ } & C_i
> \end{array}
> $$
> The **left square** $[X \to Y,\ * \to C_f]$ is the [[Def - Pullback and Pushout|homotopy pushout]] defining $C_f = C_f$ — i.e. the cofiber square of $f$ (here I have arranged the bottom-left to be $*$ and the shared middle column to be $C_f$). The **right square** $[Y \to C_f,\ * \to C_i]$ is the cofiber square of $i$, a homotopy pushout defining $C_i$. The two squares share the middle column.
>
> By the **pasting lemma for homotopy pushouts** (if both squares are homotopy pushouts, so is the outer rectangle), the outer rectangle $[X \to C_f,\ * \to C_i]$ is a homotopy pushout. But following the maps, the outer rectangle exhibits $C_i$ as the homotopy pushout in which $X$ maps to $*$ on one side and the composite $X \to Y \to C_f$ — which is null, since $i \circ f = 0$ (the composite in a cofiber sequence is zero) — collapses on the other. Thus the outer rectangle is the homotopy pushout of $* \leftarrow X \rightarrow *$, i.e.
> $$C_i \;\simeq\; * \cup_X * \ (\text{derived}) \;=\; \Sigma X.$$
> Concretely: the mapping cone $C_i$ collapses $Y$ inside $C_f = Y \cup_X CX$, leaving the cone $CX$ with its base $X$ also collapsed — that is the double cone $\Sigma X$. The induced map $C_f \to C_i = \Sigma X$ is the connecting map $\partial$.

**Step 2: The infinite Puppe sequence.**

> [!note]- Derivation
> Step 1 shows the cofiber of $i$ is $\Sigma X$, so $Y \xrightarrow{i} C_f \xrightarrow{\partial} \Sigma X$ is again a cofiber sequence (it is the cofiber sequence of $i$). [[Def - Cofiber and Fiber Sequence|Rotating]] repeats the argument: the cofiber of $\partial : C_f \to \Sigma X$ is $\Sigma Y$, the cofiber of $\Sigma f$ is $\Sigma C_f$, and so on. Applying $\Sigma$ to the whole sequence and tracking the orientation introduces a sign at each re-suspension (the suspension co-multiplication reverses orientation under one rotation), giving
> $$X \xrightarrow{f} Y \xrightarrow{i} C_f \xrightarrow{\partial} \Sigma X \xrightarrow{-\Sigma f} \Sigma Y \xrightarrow{-\Sigma i} \Sigma C_f \xrightarrow{-\Sigma\partial} \Sigma^2 X \to \cdots,$$
> with each consecutive triple a cofiber sequence. This is the Puppe sequence: a single map $f$ generates an infinite exact sequence because the cofiber operation loops back to the suspension rather than producing endlessly new objects.

**Step 3: The dual fiber statement.**

> [!note]- Derivation
> Dualize every arrow. The homotopy fiber of $p : F_f \to X$ is computed by pasting two homotopy-*pullback* squares (the fiber square of $f$ and the fiber square of $p$), and the outer rectangle is the homotopy pullback of $* \rightarrow Y \leftarrow *$, i.e. $\Omega Y$. So the fiber of the fiber is the loop, and one gets the dual Puppe fiber sequence
> $$\cdots \to \Omega^2 Y \to \Omega F_f \to \Omega X \xrightarrow{-\Omega f} \Omega Y \xrightarrow{\partial} F_f \xrightarrow{p} X \xrightarrow{f} Y.$$

> [!note]- Complete formal solution
> **(1)** Place the cofiber square of $f$ (corners $X, Y, *, C_f$) adjacent to the cofiber square of $i$ (corners $Y, C_f, *, C_i$), sharing the column through $C_f$. Both are homotopy pushouts, so by the pasting lemma the outer rectangle is a homotopy pushout. Its content is the homotopy pushout of $* \leftarrow X \rightarrow *$ (using $i \circ f = 0$), which is $\Sigma X$. Hence $C_i \simeq \Sigma X$, and the induced $C_f \to \Sigma X$ is $\partial$.
>
> **(2)** Since $Y \to C_f \to \Sigma X$ is the cofiber sequence of $i$, rotation iterates the construction, yielding the infinite Puppe sequence with signs $-\Sigma f$, $-\Sigma i$, $\dots$ from the orientation reversal under re-suspension.
>
> **(3)** Dually, pasting homotopy-pullback squares gives the fiber of $p : F_f \to X$ as $\Omega Y$, and the dual Puppe fiber sequence $\cdots \to \Omega Y \to F_f \to X \to Y$. $\blacksquare$

---

# Key Takeaways

**The cofiber of the cofiber is the suspension — this single identity makes every cofiber sequence infinite.** The whole reason a three-term cofiber sequence $X \to Y \to C_f$ extends forever is that asking "what is the cofiber of $i$?" returns $\Sigma X$ rather than a brand-new object. The trigger to remember is that the cofiber operation, iterated, *loops back to the suspension*, so you never have to compute new objects — you suspend. This is the structural fact behind the Puppe sequence and, in the derived category, behind the rotation of distinguished triangles. The dual — fiber of the fiber is the loop — is the same insight in a mirror, and together they are why the (co)fiber calculus is so economical: two operations and a shift generate everything.

**Pasting homotopy-(co)cartesian squares is the universal technique for extending sequences.** The proof is nothing but stacking two homotopy-pushout squares and invoking the pasting lemma, and this pattern recurs throughout homotopy theory: the Mayer–Vietoris sequence, the long exact sequence of a triple, the octahedral axiom, and the connecting maps in spectral sequences are all assembled by pasting (co)cartesian squares. The transferable diagnostic is that whenever you need to relate three terms of a sequence to the next, draw the relevant squares with the shared edge and apply the pasting lemma; the outer rectangle delivers the new term for free. Internalizing "the outer rectangle of two homotopy pushouts is a homotopy pushout" is worth more than memorizing any individual long exact sequence.

**The signs are honest orientation data, not bookkeeping noise.** The $-\Sigma f$ that appears after the connecting map is the orientation reversal of the suspension coordinate under one rotation, and it is the same sign that governs the rotation axiom of triangulated categories. Dropping it produces an inconsistent calculus — the long exact sequences would fail to splice correctly. The reusable lesson is that in any (co)fiber or triangle calculus, the signs track how the suspension circle is oriented, and they must be carried; when a computation seems off by a sign, the cause is almost always a missed orientation flip from re-suspending. Treating the signs as meaningful (rather than as an annoyance) is what keeps the rotation and agreement theorems coherent.
