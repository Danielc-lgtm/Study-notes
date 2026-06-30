---
type: exercise
subject: model-categories
difficulty: "⭐"
prereqs:
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Pullback and Pushout"
  - "Def - Initial and Terminal Object"
  - "Def - Cylinder Object, Path Object, and Homotopy"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a [[Def - Pointed Model Category Suspension and Loop|pointed model category]] with zero object $*$.

1. Show that the **strict** pushout of the diagram $* \xleftarrow{} X \xrightarrow{} *$ (both maps the unique map $X \to *$) is $*$ for *every* object $X$. Conclude that the naive "strict suspension" functor $X \mapsto * \sqcup_X *$ is constant at the zero object and carries no information.
2. Explain why this forces the [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma X$ to be defined as the **[[Def - Homotopy|homotopy]]** pushout, and identify the cofibrant-replacement step that fixes the degeneracy.
3. Verify in $\mathbf{Top}_*$ that the homotopy pushout $* \cup_X \mathrm{Cyl}(X) \cup_X *$ is the reduced suspension $\Sigma X = X \wedge S^1$, and check on $X = S^0$ that $\Sigma S^0 \simeq S^1$.

**Recall:**

![[Def - Pullback and Pushout#The Definition]]

A [[Def - Initial and Terminal Object|zero object]] $*$ is both initial and terminal: $\mathcal{C}(*, A)$ and $\mathcal{C}(A, *)$ are singletons for all $A$. The [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma X$ is the **homotopy** pushout of $* \leftarrow X \rightarrow *$; concretely $\Sigma X = * \cup_X \mathrm{Cyl}(X) \cup_X *$, the [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] $\mathrm{Cyl}(X)$ with both end inclusions collapsed to $*$. A homotopy pushout is computed by first replacing the legs of the span by cofibrations, then taking the strict pushout.

---

# Convergent Strategy

**Problem class:** This is a "diagnose the degeneracy" exercise of the kind the topic page's problem-solving strategy puts first: the task is to show a strict (co)limit gives the wrong (trivial) answer and to identify the homotopy correction. The routine is to compute the strict pushout directly from the universal property and watch the terminal object swallow everything.

**Assumption pattern:** The single load-bearing assumption is that $*$ is **terminal**. Terminality makes $\mathcal{C}(A, *)$ a singleton for every $A$, which is exactly what forces a pushout receiving two maps to $*$ to be $*$ again. No model structure is needed for part (1) — it is pure category theory about the terminal object — which is itself the point: the strict construction is degenerate before homotopy theory even enters.

**Theorem routing:** Part (1) routes through the universal property of the [[Def - Pullback and Pushout|pushout]] together with terminality. Part (2) routes through the definition of the homotopy pushout as a strict pushout of a cofibrantly replaced span. Part (3) routes through the explicit cylinder $X \times [0,1]$ in $\mathbf{Top}_*$ and the identification of the double-collapse with the smash $X \wedge S^1$.

**Key decision point:** The interesting decision is recognizing that the degeneracy is caused by *terminality*, not by anything about $X$. A reader might expect the answer to depend on $X$; the lesson is that the strict pushout cannot see $X$ at all because both legs land in the terminal object, and only after replacing those legs by cofibrations (which remember $X$) does the construction become informative.

---

# Legal Operations Used

1. **Operation 1 from the topic page (replace a strict (co)limit by its homotopy version).** This exercise is the canonical instance: it exhibits exactly why the operation is mandatory by showing the strict version is trivial.

2. **Operation 3 from the topic page (recognize a homotopy pushout square with a corner at $*$).** Parts (2) and (3) use that the square defining $\Sigma X$ has two corners at the zero object, so it is a (homotopy) cofiber-type square.

3. **Operation 8 from the topic page (specialize to the enriched formula $\Sigma = -\wedge S^1$).** Part (3) computes the homotopy pushout in $\mathbf{Top}_*$ via the explicit cylinder and identifies it with the smash with $S^1$.

---

# Hints

> [!note]- Hint 1
> For part (1), do not think about $X$ at all. A pushout receiving two maps to a *terminal* object: what is the universal property asking for, and how many cocones are there?

> [!note]- Hint 2
> A cocone under $* \leftarrow X \rightarrow *$ with apex $T$ is a pair of maps $* \to T$ together with the compatibility over $X$. The pushout is the *universal* such apex. Use that $*$ is terminal to see the pushout maps into anything uniquely.

> [!note]- Hint 3
> For part (3), in $\mathbf{Top}_*$ take $\mathrm{Cyl}(X) = X \times [0,1]$. Collapsing $X \times \{0\}$ and $X \times \{1\}$ separately to (the same) point gives the unreduced suspension; reducing along the basepoint gives $X \wedge S^1$. For $X = S^0$ (two points, one the basepoint), $S^0 \times [0,1]$ is two intervals, and collapsing both ends glues them into a circle.

---

# Solution

The solution is three short computations. Part (1) is the universal property of the pushout against a terminal object: the strict pushout is $*$. Part (2) reads off that the homotopy pushout is needed and names the cone replacement. Part (3) is an explicit cylinder computation in $\mathbf{Top}_*$.

**Step 1: The strict pushout of $* \leftarrow X \rightarrow *$ is $*$.**

> [!note]- Derivation
> Write $P = * \sqcup_X *$ for the strict [[Def - Pullback and Pushout|pushout]]. The pushout comes with maps $j_0, j_1 : * \to P$ and is universal: for any object $T$ with maps $t_0, t_1 : * \to T$ agreeing on $X$ (i.e. $t_0 \circ (X \to *) = t_1 \circ (X \to *)$), there is a unique $u : P \to T$ with $u \circ j_0 = t_0$, $u \circ j_1 = t_1$.
>
> I claim $P = *$ satisfies this universal property. Take $T = *$ itself with the maps $j_0 = j_1 : * \to *$ the identity. Now for *any* $T$ and any cocone $(t_0, t_1)$: since $*$ is terminal, there is a unique map $* \to T$, so $t_0 = t_1$ is forced and the cocone is just "the unique map $* \to T$." The induced map $u : * \to T$ is the unique map $* \to T$, which exists and is unique by terminality. Hence $*$ has the pushout's universal property, so $P \cong *$.
>
> Nothing in this argument mentioned $X$. The strict suspension $X \mapsto * \sqcup_X *$ is therefore the constant functor at $*$.

**Step 2: The homotopy pushout is forced, via cofibrant replacement of the legs.**

> [!note]- Derivation
> Because the strict construction is constant, it cannot be the right notion of suspension — a suspension must remember $X$ (in $\mathbf{Top}_*$, $\Sigma S^n = S^{n+1}$ depends entirely on $n$). The model-category fix is the **homotopy pushout**: replace each leg $X \to *$ by a [[Def - Cofibrant and Fibrant Objects|cofibration]] before taking the pushout. Factor $X \to *$ as a cofibration $X \rightarrowtail CX$ (a "cone" on $X$) followed by a trivial fibration $CX \xrightarrow{\sim} *$; do this on both legs. Equivalently, use a [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] $\mathrm{Cyl}(X)$ with end inclusions $\mathrm{i}_0, \mathrm{i}_1 : X \rightarrowtail \mathrm{Cyl}(X)$ (a cofibration $X \sqcup X \rightarrowtail \mathrm{Cyl}(X)$) and form the strict pushout
> $$\Sigma X = * \cup_X \mathrm{Cyl}(X) \cup_X *,$$
> collapsing each end of the cylinder to $*$. Now the cofibrations remember $X$ (the cylinder is built on $X$), so the result is not $*$. This is the suspension. The degeneracy in Step 1 was entirely due to the legs being the *non-cofibration* maps $X \to *$.

**Step 3: In $\mathbf{Top}_*$ the homotopy pushout is $X \wedge S^1$, and $\Sigma S^0 \simeq S^1$.**

> [!note]- Derivation
> In $\mathbf{Top}_*$ (with the Quillen model structure), a cofibrant $X$ has cylinder $\mathrm{Cyl}(X) = X \times [0,1]$, with end inclusions $x \mapsto (x,0)$ and $x \mapsto (x,1)$. Collapsing $X \times \{0\}$ to a point and $X \times \{1\}$ to a point gives the **unreduced suspension** $S X$. Reducing — collapsing also the arc $\{x_0\} \times [0,1]$ through the basepoint $x_0$ — gives the **reduced suspension**, which is exactly the smash product $X \wedge S^1$, since $S^1 = [0,1]/\{0,1\}$ and $X \wedge S^1 = (X \times S^1)/(X \vee S^1)$. Up to the (weak equivalence) reduction, $\Sigma X = X \wedge S^1$.
>
> For $X = S^0 = \{x_0, p\}$ (basepoint $x_0$ and one other point $p$), the cylinder $S^0 \times [0,1]$ is two intervals, $\{x_0\} \times [0,1]$ and $\{p\} \times [0,1]$. Collapsing each end set $S^0 \times \{0\}$ and $S^0 \times \{1\}$ to a single point identifies the two left endpoints and the two right endpoints, gluing the two intervals into a single loop — a circle. Hence $\Sigma S^0 \simeq S^1$, confirming $\Sigma S^n = S^{n+1}$ at $n = 0$.

> [!note]- Complete formal solution
> **(1)** Let $P = * \sqcup_X *$ be the strict pushout. For any $T$ and cocone $(t_0, t_1 : * \to T)$, terminality of $*$ forces $t_0 = t_1$ to be the unique map $* \to T$, and the induced map $P \to T$ must be the unique map $* \to T$. Thus $*$ satisfies the universal property of $P$, so $P \cong *$. As $X$ never entered, the strict suspension functor is constant at $*$.
>
> **(2)** Since the strict suspension forgets $X$, the suspension is defined as the homotopy pushout: replace each leg $X \to *$ by a cofibration (a cone, or equivalently use a cylinder object $\mathrm{Cyl}(X)$ with cofibrant end inclusions) and take $\Sigma X = * \cup_X \mathrm{Cyl}(X) \cup_X *$. The cofibrations retain the data of $X$, so the result is non-trivial. The cofibrant-replacement of the span is the step that fixes the degeneracy.
>
> **(3)** In $\mathbf{Top}_*$, $\mathrm{Cyl}(X) = X \times [0,1]$; collapsing both ends (and reducing along the basepoint arc) gives $X \wedge S^1$, with $S^1 = [0,1]/\{0,1\}$. For $X = S^0$, the cylinder is two intervals and collapsing the two end-sets glues them into a circle, so $\Sigma S^0 \simeq S^1$. $\blacksquare$

---

# Key Takeaways

**The terminal object is what makes strict pointed (co)limits degenerate.** The deepest lesson here is structural and not about $X$ at all: the strict pushout of $* \leftarrow X \rightarrow *$ collapses precisely because $*$ is terminal, so both legs land where every object maps uniquely. This is the source of every "I computed $\Sigma X$ and got the zero object" error in the subject, and the trigger to recognize it is seeing the zero object as a *corner* of a strict (co)limit square. Whenever a construction in a pointed category comes out equal to $*$, suspect a strict (co)limit against the zero object and reach for the homotopy version. The same mechanism makes the strict pullback of $* \rightarrow Y \leftarrow *$ equal to $*$, so the loop functor needs the identical correction by fibrant replacement.

**Cofibrant replacement is what "remembers" the object.** The reason the homotopy pushout is informative while the strict one is not is that replacing the legs $X \to *$ by cofibrations into cones encodes $X$ into the maps themselves. A cofibration is a "good inclusion" that the pushout cannot collapse, so the cylinder built on $X$ survives the gluing and the suspension carries the homotopy type of $X$. The transferable diagnostic is: a homotopy (co)limit differs from the strict one exactly when the strict maps are not (co)[[Def - Fibration|fibrations]], and the replacement is what injects the missing information. This is why the model-category machinery is not optional bookkeeping — the (co)fibrations are the carriers of homotopical content.

**The smash with $S^1$ is the computational shortcut, and the cone-and-collapse is the conceptual picture.** In an enriched category like $\mathbf{Top}_*$ one rarely performs the homotopy pushout by hand; one writes $\Sigma X = X \wedge S^1$ and is done. But the cone-and-collapse construction is what explains *why* $\Sigma X$ is the cofiber of $X \to *$ and hence sits at the end of every cofiber sequence. The habit to build is to compute with the smash formula but think with the homotopy pushout, so that the suspension's role in exact sequences stays visible. The computation $\Sigma S^0 = S^1$ — two intervals glued at their ends into a circle — is the smallest example where both pictures are simultaneously transparent, and it anchors the general fact $\Sigma S^n = S^{n+1}$ that builds every sphere from $S^0$.
