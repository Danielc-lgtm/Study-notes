---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Kan Fibration and Anodyne Extension"
  - "Thm - Simplicial Sets Form a Model Category"
  - "Thm - The Retract Argument"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Prove the Gabriel–Zisman characterisation: in the Kan–Quillen [[Thm - Simplicial Sets Form a Model Category|model structure]] on $\mathbf{sSet}$, a map is an **[[Def - Kan Fibration and Anodyne Extension|anodyne extension]]** (a member of the saturation of the horn inclusions) if and only if it is a **trivial cofibration** (a monomorphism that is a weak equivalence). Equivalently, the anodyne maps are exactly $\mathrm{LLP}(\{$[[Def - Kan Fibration and Anodyne Extension|Kan fibrations]]$\})$.

You may use the following two facts established in [[Thm - Simplicial Sets Form a Model Category]]: (i) every anodyne map is a weak equivalence (and a monomorphism); (ii) the small object argument factors any map $f$ as an anodyne map followed by a Kan fibration.

**Recall:**

![[Def - Kan Fibration and Anodyne Extension#The Definition]]

A **trivial cofibration** is a monomorphism that is a weak equivalence. The [[Thm - The Retract Argument|retract argument]] says: if $f = p \circ i$ with $i \in \mathrm{LLP}(\mathcal{R})$ and $p \in \mathcal{R}$, and if $f \in \mathrm{LLP}(\mathcal{R})$, then $f$ is a retract of $i$.

---

# Convergent Strategy

**Problem class:** This is an *identify-the-trivial-class* problem of the lifting world (topic-page Problem-Solving Strategy): show that an explicitly generated left class (anodyne = saturation of horns) equals an implicitly defined class (trivial cofibrations). The routine for "generated class = lifting-defined class" is the [[Thm - The Retract Argument|retract argument]] applied to a small-object-argument factorisation.

**Assumption pattern:** The recognisable feature is that we have *two* descriptions of a class and want to identify them: the constructive "built from horns" and the property-level "mono + weak equivalence". The bridge fact (i) gives anodyne $\Rightarrow$ trivial cofibration cheaply; the hard direction, trivial cofibration $\Rightarrow$ anodyne, is where the retract argument earns its keep, fed by the factorisation (ii).

**Theorem routing:** The easy direction routes: anodyne $\to$ (fact (i)) mono + weak equivalence $\to$ trivial cofibration. The hard direction routes: trivial cofibration $f$ $\to$ factor $f = p \circ i$ with $i$ anodyne, $p$ Kan fibration (fact (ii)) $\to$ $p$ is a weak equivalence by two-out-of-three $\to$ $p$ is a *trivial* Kan fibration, so $f$ has the left lifting property against it $\to$ [[Thm - The Retract Argument|retract argument]]: $f$ is a retract of $i$ $\to$ $f$ anodyne (anodyne closed under retract).

**Key decision point:** The crux is recognising that the residual fibration $p$ in the factorisation is not just a Kan fibration but a *trivial* one (a weak equivalence), so that $f$ — being a cofibration *and* a weak equivalence — lifts against it. This is the single use of the weak-equivalence hypothesis on $f$, and it is what makes the retract argument applicable. Forgetting that $p$ is trivial is the natural error.

---

# Legal Operations Used

1. **Operation 5 from the topic page (factor a map via the small object argument).** Fact (ii) is exactly this: factor the trivial cofibration as anodyne-then-Kan-fibration.

2. **Operation 3 from the topic page (recognise and use an anodyne map).** The closure of anodyne maps under retract — part of the definition — is what converts "$f$ is a retract of an anodyne map" into "$f$ is anodyne".

3. **The [[Thm - The Retract Argument|retract argument]].** This is the engine that exhibits $f$ as a retract of the anodyne factor $i$, using that $f$ lifts against the trivial fibration $p$.

---

# Hints

> [!note]- Hint 1
> One inclusion is immediate from fact (i): anodyne maps are monos and weak equivalences, hence trivial cofibrations.

> [!note]- Hint 2
> For the converse, take a trivial cofibration $f$ and apply fact (ii): factor $f = p \circ i$ with $i$ anodyne and $p$ a Kan fibration. What can you say about $p$ using two-out-of-three?

> [!note]- Hint 3
> $f$ and $i$ are both weak equivalences (the latter by fact (i)), so $p$ is a weak equivalence — a *trivial* Kan fibration. A trivial cofibration lifts against a trivial fibration (by the lifting axiom MC4, or because trivial fibrations have RLP against all monos). So $f$ lifts against $p$.

> [!note]- Hint 4
> Now $f = p \circ i$, $i$ anodyne, $p$ a trivial fibration, and $f$ lifts against $p$. Apply the [[Thm - The Retract Argument|retract argument]]: $f$ is a retract of $i$. Anodyne maps are closed under retract, so $f$ is anodyne.

---

# Solution

One inclusion is the cheap fact that anodyne maps are trivial cofibrations. The converse is the retract argument: factor a trivial cofibration as anodyne-then-Kan-fibration; the residual fibration is trivial, so the cofibration lifts against it, exhibiting the cofibration as a retract of the anodyne factor — hence anodyne.

**Step 1: Anodyne $\Rightarrow$ trivial cofibration.**

> [!note]- Derivation
> By fact (i), every [[Def - Kan Fibration and Anodyne Extension|anodyne map]] is a monomorphism and a weak equivalence. A monomorphism is a cofibration ([[Ex - Monomorphisms are the cofibrations|cofibrations are exactly the monomorphisms]]), so an anodyne map is a cofibration that is a weak equivalence — a trivial cofibration. This gives $\{$anodyne$\} \subseteq \{$trivial cofibrations$\}$.

**Step 2: Factor a trivial cofibration.**

> [!note]- Derivation
> Let $f : A \to B$ be a trivial cofibration. By fact (ii) (the small object argument against the horn inclusions $J$), factor
> $$f : A \xrightarrow{\ i\ } C \xrightarrow{\ p\ } B,$$
> with $i$ anodyne and $p$ a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]].

**Step 3: The residual fibration is trivial.**

> [!note]- Derivation
> By fact (i), $i$ is a weak equivalence; by hypothesis $f$ is a weak equivalence. Weak equivalences satisfy two-out-of-three (axiom MC2), so $p$ is a weak equivalence. A Kan fibration that is a weak equivalence is a *trivial fibration*, i.e. it has the right [[Def - Lifting Property and the Retract Argument|lifting property]] against every monomorphism ([[Ex - Trivial fibrations lift against all monomorphisms|trivial fibrations lift against all monos]]).

**Step 4: $f$ lifts against $p$, and the retract argument finishes.**

> [!note]- Derivation
> Since $f$ is a monomorphism and $p$ is a trivial fibration, the square
> $$\begin{array}{ccc} A & \xrightarrow{\ i\ } & C \\ {\scriptstyle f}\downarrow & & \downarrow{\scriptstyle p} \\ B & \xrightarrow{\ \mathrm{id}\ } & B \end{array}$$
> (which commutes: $p i = f = \mathrm{id} \circ f$) admits a lift $r : B \to C$ with $r f = i$ and $p r = \mathrm{id}_B$. This is exactly the data the [[Thm - The Retract Argument|retract argument]] needs: $f$ is a retract of $i$ in the arrow category, via the diagram
> $$\begin{array}{ccccc} A & = & A & = & A \\ {\scriptstyle f}\downarrow & & {\scriptstyle i}\downarrow & & {\scriptstyle f}\downarrow \\ B & \xrightarrow{\ r\ } & C & \xrightarrow{\ p\ } & B \end{array}$$
> with horizontal composites the identities ($\mathrm{id}_A$ on top, $pr = \mathrm{id}_B$ on the bottom). Since the anodyne maps are closed under retract (operation 3, part of the definition of anodyne), and $i$ is anodyne, $f$ is anodyne. This gives $\{$trivial cofibrations$\} \subseteq \{$anodyne$\}$.

> [!note]- Complete formal solution
> ($\subseteq$) By fact (i), anodyne maps are monomorphisms and weak equivalences, hence trivial cofibrations.
>
> ($\supseteq$) Let $f : A \to B$ be a trivial cofibration. Factor $f = p \circ i$ with $i : A \to C$ anodyne and $p : C \to B$ a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]] (fact (ii)). By fact (i) $i$ is a weak equivalence; $f$ is too; so $p$ is a weak equivalence (MC2), hence a *trivial* fibration, with RLP against all monomorphisms. The square $(i, f, p, \mathrm{id}_B)$ then has a lift $r : B \to C$ with $rf = i$, $pr = \mathrm{id}_B$, exhibiting $f$ as a retract of $i$ ([[Thm - The Retract Argument|retract argument]]). Anodyne maps being closed under retract, $f$ is anodyne.
>
> Therefore anodyne extensions $=$ trivial cofibrations $= \mathrm{LLP}(\{$Kan fibrations$\})$. $\quad\blacksquare$

---

# Key Takeaways

**The retract argument is the universal bridge from "generated" to "lifting-defined" classes.** This proof is the canonical use of the [[Thm - The Retract Argument|retract argument]], and the pattern is worth memorising whole: to show a map $f$ in some lifting class $\mathrm{LLP}(\mathcal{R})$ is in a *generated* class $\mathrm{cof}(\mathcal{S})$, factor $f$ via the small object argument as ($\mathrm{cof}(\mathcal{S})$-map)-then-($\mathcal{R}$-map), use that $f$ lifts against the second factor to exhibit $f$ as a retract of the first, and conclude $f \in \mathrm{cof}(\mathcal{S})$ by retract-closure. Every "the trivial cofibrations are exactly the anodyne maps" / "the cofibrations are exactly the $I$-cofibrations" theorem in cofibrantly generated homotopy theory is this argument. The trigger is "two descriptions of a left class, one constructive and one by lifting"; the reaction is "factor, lift, retract".

**Two-out-of-three is how the weak-equivalence hypothesis on $f$ gets used — exactly once.** The whole proof would collapse without noticing that the residual fibration $p$ is *trivial*. That triviality comes from two-out-of-three applied to $f = p \circ i$ with $f$ and $i$ both weak equivalences. This is the single point where the hypothesis "$f$ is a weak equivalence" (as opposed to merely a cofibration) is consumed, and it is what upgrades $p$ from "Kan fibration" to "trivial fibration", which is what $f$ can lift against. The general diagnostic: in a factor-and-lift argument, the property distinguishing your map (here, being a weak equivalence) is almost always spent via two-out-of-three on the factorisation, turning a property of $f$ into a property of the residual factor.

**Gabriel–Zisman makes the model structure checkable by replacing a property with a construction.** The value of the theorem is practical: "trivial cofibration" is a *property* (mono and weak equivalence) that is hard to verify directly, because weak equivalence is defined by realisation; "anodyne" is a *construction* (built from horns by pushout, transfinite composition, retract) that can be exhibited explicitly. Identifying the two means one can *prove* a map is a trivial cofibration by *building* it from horns — no realisation, no homotopy-group computation. This is the constructive-versus-property duality that runs through the whole subject, and recognising which side a problem hands you, and which side you need, is half of solving it.
