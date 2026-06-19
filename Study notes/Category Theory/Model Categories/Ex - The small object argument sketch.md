---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Model Category"
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Limit and Colimit"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Sketch the **small object argument**, the standard construction of the factorizations required by axiom MC5, for the Quillen model structure on $\mathbf{Top}$.

(a) Let $I = \{S^{n-1} \hookrightarrow D^n : n \geq 0\}$ be the set of boundary-inclusions of disks (the **generating cofibrations**; for $n = 0$ this is $\varnothing \hookrightarrow D^0 = *$). Describe the transfinite construction that factors an arbitrary continuous map $f : X \to Y$ as $X \to Z \to Y$, where $X \to Z$ is built by repeatedly attaching disks and $Z \to Y$ has the right lifting property with respect to every map in $I$.

(b) Explain why the map $Z \to Y$ produced is a **Serre fibration** (RLP against $I$ is, by definition, being a Serre fibration), and why $X \to Z$ is a (relative cell complex, hence a) cofibration.

(c) State the role of the **smallness** hypothesis on the domains $S^{n-1}$ (compactness of spheres), and where it is used in the construction.

You are asked for a careful sketch with the key constructions named, not a complete proof with all transfinite bookkeeping.

**Recall:**

![[Def - Lifting Property and the Retract Argument#The Definition]]

A map $p$ has the **RLP against $I$** if for every $n$ and every commuting square with $S^{n-1} \hookrightarrow D^n$ on the left and $p$ on the right, a diagonal lift exists — this is precisely the homotopy lifting property against disks, i.e. $p$ is a **Serre fibration**. A **relative cell complex** is a map built as a transfinite composite of pushouts of coproducts of maps in $I$ ([[Def - Pullback and Pushout|pushouts]] = attaching cells).

---

# Convergent Strategy

**Problem class:** This is a construction-sketch problem — exhibiting the machine that produces the factorizations MC5 demands. It is the ⭐⭐⭐ companion to the axiom-verification exercises: the hard axiom in any model structure is factorization, and the small object argument is *the* way it is proved. It realizes the "verify the axioms" target on the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Sources and Targets|topic page]] at its hardest.

**Assumption pattern:** The decisive input is the *set* $I$ of generating cofibrations and the smallness (compactness) of their domains. Recognizing that you only need to solve lifting problems against the *generators*, then iterate, is the conceptual unlock — the full classes are forced by [[Thm - Closure Properties of the Model Structure|the lifting characterization]] and do not need to be handled directly.

**Theorem routing:** The route is: build $Z$ by transfinitely attaching cells to kill all lifting problems against $I$; the result $Z \to Y$ lifts against $I$ by construction (Serre fibration); $X \to Z$ is a relative cell complex hence a cofibration by pushout-closure ([[Ex - Lifting properties determine the classes]]); smallness guarantees the transfinite process terminates because maps out of compact domains factor through a finite stage.

**Key decision point:** The non-obvious choice is *what to attach at each stage*: you attach one cell for every commuting square (lifting problem) currently without a lift, via a single big pushout of a coproduct of generators. The subtlety is that attaching cells creates *new* lifting problems, so you must iterate transfinitely — and the decision that makes it terminate is to iterate far enough (to a sufficiently large ordinal) that smallness forces every problem to be solved at some earlier stage.

---

# Legal Operations Used

1. **Operation 9 from the topic page (push out a cofibration).** Each stage of the construction attaches cells via a pushout of a coproduct of generating cofibrations; pushout-closure guarantees the result stays a cofibration.

2. **Operation 1 from the topic page (factor a map).** The entire exercise is the construction underlying this operation — it is how MC5 is realized in $\mathbf{Top}$.

3. **Operation 8 from the topic page (recognize a class by its lifting property).** The output map $Z \to Y$ is a Serre fibration precisely because it has the RLP against $I$, and the lifting characterization promotes "RLP against generators" to "RLP against all trivial cofibrations."

---

# Hints

> [!note]- Hint 1
> The goal is to make $Z \to Y$ solve every lifting problem against a generator $S^{n-1} \hookrightarrow D^n$. A lifting problem is a commuting square: $S^{n-1} \to Z$, $D^n \to Y$, agreeing on $S^{n-1}$. To *force* a lift, attach a disk $D^n$ to $Z$ along the given $S^{n-1} \to Z$.

> [!note]- Hint 2
> Do this for all lifting problems at once: take the coproduct over all current squares of the generators, and push out. This enlarges $Z$ to $Z_1$. But the maps $D^n \to Y$ now define new lifting problems for $Z_1 \to Y$, so iterate: $Z_0 = X, Z_1, Z_2, \dots$ and take the colimit over a long ordinal.

> [!note]- Hint 3
> Why does iterating terminate? Because $S^{n-1}$ is compact: any map $S^{n-1} \to Z_\infty = \mathrm{colim}\, Z_\alpha$ into the transfinite colimit factors through some finite (or bounded) stage $Z_\alpha$, since a compact image meets only finitely many cells. So the lifting problem was already attended to at stage $\alpha + 1$.

> [!note]- Hint 4
> The map $X = Z_0 \to Z_\infty$ is a transfinite composite of pushouts of coproducts of generators — a relative cell complex — hence a cofibration. The map $Z_\infty \to Y$ has the RLP against every generator, because every square against a generator factors through some $Z_\alpha$ where a cell was attached supplying the lift. RLP against $I$ = Serre fibration.

---

# Solution

The construction iteratively attaches cells to solve all lifting problems against the generators $I$, taking a transfinite colimit; smallness guarantees the colimit map has the right lifting property, while the colimit-side map is a relative cell complex. The plan is: build the tower (Step 1), identify the two factors (Steps 2–3), and locate smallness (Step 4).

**Step 1: The transfinite tower.**

Build $X = Z_0 \to Z_1 \to Z_2 \to \cdots$ by attaching, at each stage, a cell for every unsolved lifting problem against a generator.

> [!note]- Derivation
> Given $f : X \to Y$, set $Z_0 = X$ with the map $f_0 = f : Z_0 \to Y$. At stage $\alpha$, consider the set $S_\alpha$ of all commuting squares
> $$\begin{array}{ccc} S^{n-1} & \to & Z_\alpha \\ \downarrow & & \downarrow f_\alpha \\ D^n & \to & Y \end{array}$$
> (one for each generator and each such square). Form the coproduct of the generators over $S_\alpha$ and push out along the maps $S^{n-1} \to Z_\alpha$:
> $$Z_{\alpha+1} = Z_\alpha \;\sqcup_{\left(\coprod_{S_\alpha} S^{n-1}\right)}\; \left(\coprod_{S_\alpha} D^n\right).$$
> The maps $D^n \to Y$ assemble (with $f_\alpha$) into $f_{\alpha+1} : Z_{\alpha+1} \to Y$. At limit ordinals take colimits. Let $Z = Z_\lambda$ for a suitably large ordinal $\lambda$ and $g = f_\lambda : Z \to Y$; let $j : X \to Z$ be the canonical map.

**Step 2: The colimit-side map $j : X \to Z$ is a relative cell complex, hence a cofibration.**

> [!note]- Derivation
> Each $Z_\alpha \to Z_{\alpha+1}$ is a pushout of a coproduct of generators $S^{n-1} \hookrightarrow D^n$ — that is, an attachment of cells. The map $j : X \to Z$ is the transfinite composite of these. By pushout-closure and coproduct-closure of cofibrations (proved in [[Ex - Lifting properties determine the classes]]) and closure under transfinite composition, $j$ is a cofibration. Concretely $Z$ is $X$ with cells attached, a relative cell complex.

**Step 3: The map $g : Z \to Y$ has the RLP against $I$, i.e. is a Serre fibration.**

> [!note]- Derivation
> Take any commuting square with a generator $S^{n-1} \hookrightarrow D^n$ on the left and $g : Z \to Y$ on the right: a map $u : S^{n-1} \to Z$ and $v : D^n \to Y$ with $g u = v|_{S^{n-1}}$. By smallness (Step 4) $u$ factors through some $Z_\alpha$, so this square was a member of $S_\alpha$, and at stage $\alpha + 1$ we attached the disk $D^n$ along $u$, with the attached cell mapping to $Y$ via $v$. The inclusion $D^n \to Z_{\alpha+1} \to Z$ of this attached cell is exactly a diagonal lift: it restricts to $u$ on $S^{n-1}$ and composes with $g$ to $v$. So every square against a generator has a lift, i.e. $g$ has the RLP against $I$ — which is the definition of a Serre fibration.

**Step 4: Where smallness is used.**

> [!note]- Derivation
> The spheres $S^{n-1}$ are compact. A continuous map from a compact space into a transfinite colimit $Z = \mathrm{colim}_\alpha Z_\alpha$ of (closed $T_1$) inclusions has compact image, which meets only finitely many of the attached cells, hence factors through some $Z_\alpha$ at a bounded stage. This is the "$S^{n-1}$ is small relative to the cell attachments" hypothesis. It is used in Step 3 to guarantee that *every* lifting problem against a generator appears at some finite stage and is therefore solved — without smallness, a lifting problem could "escape to infinity" and never be attended to, and $g$ would fail to be a fibration. Smallness is precisely what makes the transfinite process *terminate* in the relevant sense.

> [!note]- Complete formal solution
> Given $f : X \to Y$, build the tower $Z_0 = X, Z_1, Z_2, \dots$ where $Z_{\alpha+1}$ is the pushout of $Z_\alpha$ along the coproduct of all generators $S^{n-1} \hookrightarrow D^n$ indexed by commuting squares from a generator to $f_\alpha : Z_\alpha \to Y$, with $f_{\alpha+1}$ induced by the maps $D^n \to Y$; take colimits at limit ordinals. Set $Z = Z_\lambda$, $j : X \to Z$, $g : Z \to Y$ for $\lambda$ large.
>
> Then $j$ is a transfinite composite of pushouts of coproducts of generators — a relative cell complex, hence a cofibration (pushout-, coproduct-, and transfinite-composition-closure of cofibrations).
>
> And $g$ has the RLP against every generator: a square from $S^{n-1} \hookrightarrow D^n$ to $g$ has its top map $S^{n-1} \to Z$ factoring through some $Z_\alpha$ by **smallness** (compactness of $S^{n-1}$, whose image meets finitely many cells), so the disk was attached at stage $\alpha + 1$ and the attached cell is the lift. Thus $g$ is a Serre fibration.
>
> Hence $f = g \circ j$ factors as a cofibration followed by a Serre fibration. (The dual run with generating *trivial* cofibrations $\{D^n \hookrightarrow D^n \times [0,1]\}$ produces the (trivial cofibration, fibration) factorization, completing MC5.) $\blacksquare$

---

# Key Takeaways

**You only need to solve lifting problems against the generators; the lifting characterization does the rest.** The small object argument never directly handles the full class of cofibrations or fibrations — it works entirely with the small *set* $I$ of generators, attaching cells to kill lifting problems against $I$. The output map automatically lifts against all of $I$, and [[Thm - Closure Properties of the Model Structure|the closure theorem]] then promotes "RLP against generators" to "RLP against all trivial cofibrations." This reduction from a proper class to a set is what makes the construction possible, and it is the defining feature of a **cofibrantly generated** model category — essentially every model structure in nature is of this form, so this exercise is the template for how factorizations are built everywhere.

**Smallness is the termination condition: it prevents lifting problems from escaping to infinity.** The transfinite tower could in principle run forever without ever solving a given lifting problem, if the relevant map only "appeared at the very end." Compactness of the generator domains forbids this — a map out of a compact space factors through a bounded stage, so every lifting problem is attended to at some finite step. This is the homotopy-theoretic analogue of the way compactness rules out escape-to-infinity in analysis (where a bump can move out but not vanish): smallness guarantees the colimit faithfully reflects the finite stages. Recognizing "I need a smallness/compactness hypothesis to make a transfinite construction terminate" is a transferable diagnostic across the subject.

**Attaching a cell is solving a lifting problem by fiat, and a relative cell complex is the record of all such solutions.** The single move at the heart of the argument is: faced with a square $S^{n-1} \to Z$, $D^n \to Y$ with no lift, *create* the lift by gluing in the disk $D^n$. Doing this universally (for all squares, via one pushout) and iterating produces a relative cell complex, which is therefore exactly the universal object built to make the lifting problems solvable. This reframes "cofibration = retract of a relative cell complex" as "cofibration = retract of the universal solution to all lifting problems against $I$," which is the structural picture of cofibrations you carry into the study of $\mathbf{Top}$, $\mathbf{sSet}$, and $\mathbf{Ch}(R)$ alike.
