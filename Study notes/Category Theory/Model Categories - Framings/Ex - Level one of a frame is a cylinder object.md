---
type: exercise
subject: model-categories
difficulty: "⭐"
prereqs:
  - "Def - Cosimplicial and Simplicial Frame"
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Def - Reedy Category and the Reedy Model Structure"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $X^{\bullet}$ be a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on an object $X$ of a model category $\mathcal{M}$, with $X^0 \simeq X$. Show that the degree-$0$ and degree-$1$ data of the frame exhibit $X^1$ as a [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] for $X^0$.

(a) Identify the two cofaces $d^0, d^1 : X^0 \to X^1$ and the codegeneracy $s^0 : X^1 \to X^0$, and the cosimplicial identities they satisfy.

(b) Show that $(d^0, d^1) : X^0 \sqcup X^0 \to X^1$ is a cofibration and $s^0 : X^1 \to X^0$ is a weak equivalence, with $s^0 \circ (d^0, d^1) = \nabla$ the fold map. Conclude $X^1$ is a cylinder object on $X^0$.

(c) Deduce that, for fibrant $Y$, two maps $f, g : X^0 \to Y$ become equal in $\mathrm{Ho}(\mathcal{M})$ if and only if they extend to a map $X^1 \to Y$ — i.e. they lie in the same path component of the [[Def - Homotopy Function Complex|homotopy function complex]] $\mathrm{map}(X, Y)$.

**Recall:**

![[Def - Cylinder Object, Path Object, and Homotopy#The Definition]]

A [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] is a Reedy-cofibrant cosimplicial object that is homotopically constant. Its degree-$1$ latching map is $(d^0, d^1) : X^0 \sqcup X^0 \to X^1$ (a cofibration, by Reedy cofibrancy), and every structure map — in particular the codegeneracy $s^0 : X^1 \to X^0$ — is a weak equivalence.

The cosimplicial identity relating the level-$1$ maps is $s^0 d^0 = s^0 d^1 = \mathrm{id}_{X^0}$ (both cofaces are sections of the codegeneracy).

---

# Convergent Strategy

**Problem class:** This is a "extract elementary homotopy data from a frame" problem — recognizing that the abstract frame contains the classical cylinder of [[Def - Cylinder Object, Path Object, and Homotopy]] in its lowest non-trivial degree. The routine is to translate the Reedy-cofibrancy and homotopical-constancy conditions into the cofibration-and-weak-equivalence factorization that defines a cylinder.

**Assumption pattern:** The two assets are the two frame conditions, each contributing exactly one half of the cylinder axiom: Reedy cofibrancy gives "the degree-$1$ latching map is a cofibration," which is the cofibration $(d^0,d^1)$; homotopical constancy gives "every structure map is a weak equivalence," which is the weak equivalence $s^0$. Recognizing this one-to-one correspondence is the whole insight.

**Theorem routing:** The exercise uses the [[Def - Cosimplicial and Simplicial Frame|frame definition]] and the [[Def - Cylinder Object, Path Object, and Homotopy|cylinder/homotopy definition]] directly; part (c) connects to [[Def - Homotopy Function Complex|homotopy function complexes]] via the identification of $1$-simplices with homotopies, the elementary case of [[Thm - Framings Compute Homotopy Function Complexes]].

**Key decision point:** The non-obvious recognition is that the cosimplicial identity $s^0 d^0 = s^0 d^1 = \mathrm{id}$ is exactly the cylinder's structure equation $\sigma\circ(\mathrm{i}_0,\mathrm{i}_1) = \nabla$. The decision is to read off the cylinder's $\mathrm{i}_0, \mathrm{i}_1, \sigma$ as $d^0, d^1, s^0$ respectively, then verify the cofibration/weak-equivalence conditions follow from the two frame axioms — rather than constructing a cylinder from scratch.

---

# Legal Operations Used

1. **Operation 3 from the topic page (check Reedy cofibrancy via latching maps).** We use Reedy cofibrancy at degree $1$ to conclude $(d^0,d^1)$ is a cofibration.

2. **Operation 6 from the topic page (function complex as corepresentable of a frame).** In (c) we identify $1$-simplices of $\mathrm{map}(X,Y) = \mathcal{M}(X^{\bullet}, Y)$ with maps $X^1\to Y$, i.e. left homotopies.

---

# Hints

> [!note]- Hint 1
> The two cofaces $d^0, d^1 : [0]\to[1]$ give two maps $X^0 \to X^1$ — these are the two "ends." The codegeneracy $s^0 : [1]\to[0]$ gives $s^0 : X^1\to X^0$ — the "interval-collapse." Compare with the cylinder structure maps $\mathrm{i}_0,\mathrm{i}_1,\sigma$.

> [!note]- Hint 2
> Reedy cofibrancy at degree $1$ says the latching map $L_1 X^{\bullet} = X^0\sqcup X^0 \xrightarrow{(d^0,d^1)} X^1$ is a cofibration. Homotopical constancy says $s^0 : X^1\to X^0$ is a weak equivalence.

> [!note]- Hint 3
> The cosimplicial identity $s^0 d^j = \mathrm{id}_{X^0}$ for $j = 0,1$ gives $s^0\circ(d^0,d^1) = \nabla$ (the fold map, identity on each summand). Together with Hint 2 this is *exactly* the definition of a cylinder object factorization $X^0\sqcup X^0 \xrightarrow{\text{cof}} X^1 \xrightarrow{\sim} X^0$.

---

# Solution

The plan is short: Step 1 names the structure maps and identities; Step 2 verifies the cofibration/weak-equivalence/fold-map conditions, concluding $X^1$ is a cylinder; Step 3 reads off the homotopy-class consequence.

**Step 1: The level-$1$ structure maps and their identities.**

> [!note]- Derivation
> In $\Delta$ the object $[1]$ receives two cofaces from $[0]$, namely $d^0, d^1 : [0]\to[1]$ (the two vertices), and maps to $[0]$ by the unique codegeneracy $s^0 : [1]\to[0]$ (collapsing the edge to a point). Applying the frame $X^{\bullet}$:
> $$d^0, d^1 : X^0 \to X^1, \qquad s^0 : X^1 \to X^0.$$
> The cosimplicial identities at this level are $s^0 d^0 = \mathrm{id}_{[0]}$ and $s^0 d^1 = \mathrm{id}_{[0]}$ (collapsing after including either vertex returns the point), so under $X^{\bullet}$:
> $$s^0 \circ d^0 = \mathrm{id}_{X^0} = s^0 \circ d^1.$$
> These are exactly the equations a cylinder's end-inclusions and collapse satisfy.

**Step 2: $X^1$ is a cylinder object on $X^0$.**

> [!note]- Derivation
> Assemble the two cofaces into $(d^0, d^1) : X^0 \sqcup X^0 \to X^1$. By the degree-$1$ latching computation, $L_1 X^{\bullet} = X^0 \sqcup X^0$ and the latching map is precisely $(d^0, d^1)$. Since $X^{\bullet}$ is a frame it is **Reedy cofibrant**, so this latching map is a **cofibration** in $\mathcal{M}$.
>
> The codegeneracy $s^0 : X^1 \to X^0$ is a structure map of the frame, and by **homotopical constancy** every structure map is a **weak equivalence**; so $s^0$ is a weak equivalence.
>
> Finally, the composite $s^0 \circ (d^0, d^1) : X^0\sqcup X^0 \to X^0$ is, by Step 1's identities, the fold map $\nabla$ (it is $\mathrm{id}_{X^0}$ on each summand). So we have a factorization of the fold map
> $$X^0 \sqcup X^0 \;\xrightarrow{\ (d^0,d^1)\ }\; X^1 \;\xrightarrow{\ s^0\ }\; X^0, \qquad s^0\circ(d^0,d^1) = \nabla,$$
> with the first map a cofibration and the second a weak equivalence. This is the definition of a **cylinder object** $X^1 = \mathrm{Cyl}(X^0)$ on $X^0$, with end inclusions $\mathrm{i}_0 = d^0$, $\mathrm{i}_1 = d^1$ and collapse $\sigma = s^0$.

**Step 3: Homotopy classes via level-$1$ extensions.**

> [!note]- Derivation
> Let $Y$ be fibrant. A [[Def - Cylinder Object, Path Object, and Homotopy|left homotopy]] from $f$ to $g$ (both $X^0\to Y$) is a map $H : \mathrm{Cyl}(X^0) \to Y$ with $H d^0 = f$, $H d^1 = g$. By Step 2, $\mathrm{Cyl}(X^0) = X^1$, so a left homotopy is exactly a map $H : X^1 \to Y$ restricting to $f, g$ along the two cofaces — that is, a $1$-simplex of the simplicial set $\mathcal{M}(X^{\bullet}, Y) = \mathrm{map}(X, Y)$ whose two faces are $f$ and $g$.
>
> Since $X^0 \simeq X$ is cofibrant (Reedy cofibrancy at degree $0$) and $Y$ is fibrant, left homotopy is an equivalence relation coinciding with the homotopy relation, and $f, g$ become equal in $\mathrm{Ho}(\mathcal{M})$ iff they are homotopic iff such an $H$ exists. Therefore $f$ and $g$ represent the same element of $[X, Y]$ exactly when they lie in the same path component of $\mathrm{map}(X, Y)$. This is the degree-$1$ shadow of $\pi_0\,\mathrm{map}(X, Y) = [X, Y]$.

> [!note]- Complete formal solution
> **(a)** The cofaces are $d^0, d^1 : X^0\to X^1$, the codegeneracy is $s^0 : X^1\to X^0$, and the cosimplicial identities give $s^0 d^0 = s^0 d^1 = \mathrm{id}_{X^0}$.
>
> **(b)** The latching map $(d^0,d^1) : X^0\sqcup X^0\to X^1$ is a cofibration by Reedy cofibrancy; $s^0$ is a weak equivalence by homotopical constancy; and $s^0\circ(d^0,d^1) = \nabla$ by (a). So $X^0\sqcup X^0 \xrightarrow{(d^0,d^1)} X^1 \xrightarrow{s^0} X^0$ is a cylinder-object factorization of the fold map, exhibiting $X^1 = \mathrm{Cyl}(X^0)$.
>
> **(c)** For fibrant $Y$, a left homotopy $f\simeq g$ is a map $X^1\to Y$ extending $f, g$ along $d^0, d^1$ — a $1$-simplex of $\mathrm{map}(X,Y)$ with faces $f, g$. As $X^0$ is cofibrant and $Y$ fibrant, homotopy is the equivalence relation computing $[X,Y]$, so $f = g$ in $\mathrm{Ho}(\mathcal{M})$ iff $f, g$ are in the same path component of $\mathrm{map}(X,Y)$. $\blacksquare$

---

# Key Takeaways

**A frame is "a coherent system of iterated cylinders," and you can always read the first cylinder off degree $1$.** This exercise makes the slogan concrete: the two frame conditions split exactly into the two halves of the cylinder axiom — Reedy cofibrancy supplies the cofibration $X^0\sqcup X^0 \rightarrowtail X^1$, homotopical constancy supplies the weak equivalence $X^1 \xrightarrow{\sim} X^0$, and the cosimplicial identities supply the fold-map factorization. So every frame *contains* a cylinder object in degree $1$, and the higher degrees contain higher cylinders (cylinders on cylinders, recording homotopies of homotopies). The recognition to carry: when you need a cylinder object and have a frame, do not build one — take $X^1$.

**The degree-$1$ statement is the elementary case of $\pi_0\,\mathrm{map}(X,Y) = [X,Y]$.** The whole point of the homotopy function complex is that its $\pi_0$ is the set of homotopy classes; this exercise verifies that fact in the lowest dimensions by hand. A $0$-simplex of $\mathrm{map}(X,Y) = \mathcal{M}(X^{\bullet}, Y)$ is a map $X^0\to Y$, i.e. a map $X\to Y$; a $1$-simplex is a map $X^1\to Y$, i.e. a homotopy; two $0$-simplices are in the same component iff joined by a $1$-simplex iff homotopic. So path-connectedness in the function complex *is* the homotopy relation, and $\pi_0$ *is* $[X,Y]$. Understanding this degree-$1$ picture is the right entry point to the full framing theorem, which extends it to all higher homotopies.

**Reedy cofibrancy and homotopical constancy are not redundant — each supplies a different half of every elementary homotopy structure.** It is worth noticing that the two frame conditions are doing genuinely different jobs: cofibrancy controls how the ends *embed* (making homotopy extendable and the relation transitive), constancy controls that the cylinder *collapses* correctly (so $X^1$ really has the homotopy type of $X$). Drop cofibrancy and $(d^0,d^1)$ need not be a cofibration, so the "cylinder" does not give a well-behaved homotopy relation (this is the failure of the constant object in [[Ex - The constant cosimplicial object is rarely a frame]]); drop constancy and $s^0$ need not be a weak equivalence, so $X^1$ is not a fattened copy of $X$ but a genuine $1$-dimensional object. The transferable diagnostic: whenever a homotopical construction has a "cofibration condition" and a "weak-equivalence condition," they are almost always controlling embedding and collapse respectively, and both are needed.
