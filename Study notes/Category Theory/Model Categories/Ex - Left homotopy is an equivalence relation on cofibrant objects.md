---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{M}$ be a model category, $A$ a **cofibrant** object, and $B$ any object. Prove that **left homotopy** $\simeq_\ell$ is an equivalence relation on the set $\mathcal{M}(A, B)$ of maps $A \to B$.

You should prove:

(a) **Reflexivity:** $f \simeq_\ell f$ for every $f$.

(b) **Symmetry:** if $f \simeq_\ell g$ then $g \simeq_\ell f$.

(c) **Transitivity:** if $f \simeq_\ell g$ and $g \simeq_\ell h$ then $f \simeq_\ell h$.

Along the way, establish and use the key lemma: **when $A$ is cofibrant, the two end-inclusions $\mathrm{i}_0, \mathrm{i}_1 : A \to \mathrm{Cyl}(A)$ are trivial cofibrations.** State clearly where cofibrancy of $A$ and where the two-out-of-three axiom are used.

**Recall:**

![[Def - Cylinder Object, Path Object, and Homotopy#The Definition]]

An object $A$ is [[Def - Cofibrant and Fibrant Objects|cofibrant]] if $\varnothing \to A$ is a cofibration. A trivial cofibration is a cofibration that is also a weak equivalence; trivial cofibrations are closed under pushout, and a pushout of a cofibration is a cofibration.

---

# Convergent Strategy

**Problem class:** This is the central well-behavedness theorem of the homotopy relation — proving $\simeq_\ell$ is an equivalence relation under the cofibrancy hypothesis. It is the technical heart that [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]] depends on, and it exemplifies the "establish closure / equivalence" target on the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Sources and Targets|topic page]].

**Assumption pattern:** The decisive hypothesis is that $A$ is cofibrant. This is what upgrades the end-inclusions into the cylinder to *trivial cofibrations*, which is the property powering symmetry (swap the ends) and transitivity (glue cylinders and lift). Recognizing that "cofibrant $A$ $\Rightarrow$ $\mathrm{i}_0, \mathrm{i}_1$ trivial cofibrations" is the lemma everything routes through is the unlock.

**Theorem routing:** Reflexivity uses the cylinder's structure map directly. Symmetry uses a cylinder automorphism swapping the ends. Transitivity is the hard part: glue two cylinders along the shared end (a pushout), check the glued object is again a cylinder using two-out-of-three, then map out of it. The key lemma routes through 2-out-of-three (the end-inclusion is a weak equivalence because $\sigma \mathrm{i}_k = \mathrm{id}_A$) and pushout-closure (the inclusion into the cylinder is a cofibration because $A \sqcup A \to \mathrm{Cyl}(A)$ is and $A$ is cofibrant).

**Key decision point:** Transitivity is where the difficulty concentrates. You have homotopies $H : \mathrm{Cyl}(A) \to B$ (from $f$ to $g$) and $H' : \mathrm{Cyl}'(A) \to B$ (from $g$ to $h$), using possibly different cylinders. The non-obvious move is to glue the two cylinders along the copy of $A$ where they meet ($g$'s end), forming a new object, and prove this glued object is a cylinder for $A$ — which requires the cofibrancy of $A$ to make the gluing a pushout of trivial cofibrations, and 2-out-of-three to certify the new structure map is a weak equivalence.

---

# Legal Operations Used

1. **Operation 6 from the topic page (build a homotopy as a map out of a cylinder).** Every part constructs or manipulates a left homotopy as a map $\mathrm{Cyl}(A) \to B$.

2. **Operation 5 from the topic page (use two-out-of-three).** Used to show the end-inclusions are weak equivalences (since $\sigma \mathrm{i}_k = \mathrm{id}$) and to certify that the glued cylinder's structure map is a weak equivalence.

3. **Operation 9 from the topic page (push out a cofibration / trivial cofibration).** The transitivity gluing is a pushout, and pushout-closure of trivial cofibrations is what keeps the glued object a cylinder.

4. **Operation 4 from the topic page (replace by a cofibrant model), in spirit.** The hypothesis "$A$ cofibrant" is exactly the replacement assumption that makes the relation well-behaved.

---

# Hints

> [!note]- Hint 1
> Reflexivity is easy: a left homotopy from $f$ to $f$ is a map $\mathrm{Cyl}(A) \to B$ restricting to $f$ on both ends. Use $f \circ \sigma$ where $\sigma : \mathrm{Cyl}(A) \to A$ is the structure map (recall $\sigma \mathrm{i}_0 = \sigma \mathrm{i}_1 = \mathrm{id}_A$).

> [!note]- Hint 2
> Key lemma: $\mathrm{i}_0 : A \to \mathrm{Cyl}(A)$ is a cofibration because $A \sqcup A \to \mathrm{Cyl}(A)$ is a cofibration and $A$ is cofibrant (so the inclusion $A \to A \sqcup A$ of one summand is a cofibration — it is a pushout of $\varnothing \to A$). It is a weak equivalence because $\sigma \mathrm{i}_0 = \mathrm{id}_A$ and $\sigma$ is a weak equivalence, so by two-out-of-three $\mathrm{i}_0$ is too.

> [!note]- Hint 3
> Symmetry: a cylinder $\mathrm{Cyl}(A)$ for $A$ becomes a cylinder with the ends swapped — the same object, with $\mathrm{i}_0$ and $\mathrm{i}_1$ interchanged, still a valid cylinder. A homotopy $H$ from $f$ to $g$ for the original is a homotopy from $g$ to $f$ for the swapped cylinder.

> [!note]- Hint 4
> Transitivity: given $H : \mathrm{Cyl}(A) \to B$ ($f \to g$) and $H' : \mathrm{Cyl}'(A) \to B$ ($g \to h$), glue $\mathrm{Cyl}(A)$ and $\mathrm{Cyl}'(A)$ along $A$ via $\mathrm{i}_1$ (end of first) $= \mathrm{i}_0'$ (start of second). The pushout $\mathrm{Cyl}''(A)$ receives $H, H'$ (they agree at $g$), giving a map $\mathrm{Cyl}''(A) \to B$. Show $\mathrm{Cyl}''(A)$ is a cylinder for $A$ (its structure map is a weak equivalence by 2-out-of-three; the inclusion $A \sqcup A \to \mathrm{Cyl}''(A)$ of the outer ends is a cofibration using that the gluing was along a trivial cofibration).

---

# Solution

The solution first proves the end-inclusions are trivial cofibrations when $A$ is cofibrant (the key lemma), then handles reflexivity and symmetry quickly, and finally builds the glued cylinder for transitivity, verifying it is a cylinder via 2-out-of-three and pushout-closure.

**Step 0 (key lemma): For cofibrant $A$, the end-inclusions $\mathrm{i}_0, \mathrm{i}_1 : A \to \mathrm{Cyl}(A)$ are trivial cofibrations.**

> [!note]- Derivation
> Write the cylinder factorization $A \sqcup A \xrightarrow{(\mathrm{i}_0, \mathrm{i}_1)} \mathrm{Cyl}(A) \xrightarrow{\sigma} A$, with $(\mathrm{i}_0, \mathrm{i}_1)$ a cofibration and $\sigma$ a weak equivalence. Since $A$ is cofibrant, $\varnothing \to A$ is a cofibration, and the inclusion $\mathrm{in}_0 : A \to A \sqcup A$ of the first summand is the pushout of $\varnothing \to A$ along $\varnothing \to A$, hence a cofibration (pushout-closure). Then $\mathrm{i}_0 = (\mathrm{i}_0,\mathrm{i}_1) \circ \mathrm{in}_0$ is a composite of cofibrations, hence a cofibration. For the weak-equivalence part: $\sigma \circ \mathrm{i}_0 = \mathrm{id}_A$ (the fold map is the identity on each summand), and $\sigma$ is a weak equivalence, so by two-out-of-three applied to $\mathrm{id}_A = \sigma \circ \mathrm{i}_0$, $\mathrm{i}_0$ is a weak equivalence. Thus $\mathrm{i}_0$ (and symmetrically $\mathrm{i}_1$) is a trivial cofibration. **Cofibrancy of $A$** is used to make $\mathrm{in}_0$ a cofibration; **two-out-of-three** is used to make $\mathrm{i}_0$ a weak equivalence.

**Step 1: Reflexivity.**

> [!note]- Derivation
> Given $f : A \to B$, set $H = f \circ \sigma : \mathrm{Cyl}(A) \to B$. Then $H \circ \mathrm{i}_0 = f \circ \sigma \circ \mathrm{i}_0 = f \circ \mathrm{id}_A = f$ and likewise $H \circ \mathrm{i}_1 = f$. So $H$ is a left homotopy from $f$ to $f$, and $f \simeq_\ell f$. (This needs no cofibrancy.)

**Step 2: Symmetry.**

> [!note]- Derivation
> Suppose $H : \mathrm{Cyl}(A) \to B$ is a left homotopy from $f$ to $g$, so $H \mathrm{i}_0 = f$, $H \mathrm{i}_1 = g$. The *same* object $\mathrm{Cyl}(A)$, with the roles of $\mathrm{i}_0$ and $\mathrm{i}_1$ exchanged, is again a cylinder for $A$: the factorization $A \sqcup A \xrightarrow{(\mathrm{i}_1, \mathrm{i}_0)} \mathrm{Cyl}(A) \xrightarrow{\sigma} A$ still has a cofibration on the left (precompose with the swap automorphism of $A \sqcup A$, which is an isomorphism, hence preserves cofibrations) and the same weak equivalence $\sigma$. With respect to this swapped cylinder, $H$ has $H \mathrm{i}_1 = g$ as its $0$-end and $H \mathrm{i}_0 = f$ as its $1$-end, so $H$ is a left homotopy from $g$ to $f$. Hence $g \simeq_\ell f$.

**Step 3: Transitivity.**

> [!note]- Derivation
> Let $H : \mathrm{Cyl}(A) \to B$ be a homotopy from $f$ to $g$ (ends $\mathrm{i}_0, \mathrm{i}_1$) and $H' : \mathrm{Cyl}'(A) \to B$ a homotopy from $g$ to $h$ (ends $\mathrm{i}_0', \mathrm{i}_1'$). Form the pushout
> $$\mathrm{Cyl}''(A) = \mathrm{Cyl}(A) \;\sqcup_A\; \mathrm{Cyl}'(A), \qquad \text{gluing } \mathrm{i}_1 \sim \mathrm{i}_0',$$
> i.e. identifying the $1$-end of the first cylinder with the $0$-end of the second along $A$. Since (by Step 0) $\mathrm{i}_1 : A \to \mathrm{Cyl}(A)$ is a trivial cofibration, its pushout $\mathrm{Cyl}'(A) \to \mathrm{Cyl}''(A)$ is a trivial cofibration (pushout-closure), and likewise the map $\mathrm{Cyl}(A) \to \mathrm{Cyl}''(A)$ is a weak equivalence. The two structure maps $\sigma, \sigma'$ agree on $A$ (both restrict to $\mathrm{id}_A$ at the glued end), so they induce $\sigma'' : \mathrm{Cyl}''(A) \to A$. Define the two outer end-inclusions $\mathrm{i}_0'' = (\text{incl}) \circ \mathrm{i}_0 : A \to \mathrm{Cyl}''(A)$ and $\mathrm{i}_1'' = (\text{incl}) \circ \mathrm{i}_1' : A \to \mathrm{Cyl}''(A)$.
> *$\mathrm{Cyl}''(A)$ is a cylinder for $A$:* the inclusion of the two outer ends $A \sqcup A \to \mathrm{Cyl}''(A)$ is a cofibration (it is built from the cofibrations $(\mathrm{i}_0,\mathrm{i}_1)$ and the gluing, using cofibrancy of $A$), and $\sigma''$ is a weak equivalence — because $\sigma'' \circ (\mathrm{Cyl}(A) \to \mathrm{Cyl}''(A)) = \sigma$ is a weak equivalence and $\mathrm{Cyl}(A) \to \mathrm{Cyl}''(A)$ is a weak equivalence, so by two-out-of-three $\sigma''$ is a weak equivalence.
> *The glued map:* $H$ and $H'$ agree at the glued end ($H \mathrm{i}_1 = g = H' \mathrm{i}_0'$), so by the universal property of the pushout they induce $H'' : \mathrm{Cyl}''(A) \to B$. Then $H'' \mathrm{i}_0'' = H \mathrm{i}_0 = f$ and $H'' \mathrm{i}_1'' = H' \mathrm{i}_1' = h$. So $H''$ is a left homotopy from $f$ to $h$, and $f \simeq_\ell h$.

> [!note]- Complete formal solution
> **Key lemma (cofibrant $A$).** In $A \sqcup A \xrightarrow{(\mathrm{i}_0,\mathrm{i}_1)} \mathrm{Cyl}(A) \xrightarrow{\sigma} A$, the summand inclusion $A \to A \sqcup A$ is a pushout of the cofibration $\varnothing \to A$, hence a cofibration; composing, $\mathrm{i}_0$ is a cofibration. Since $\sigma \mathrm{i}_0 = \mathrm{id}_A$ and $\sigma \in \mathcal{W}$, two-out-of-three gives $\mathrm{i}_0 \in \mathcal{W}$. So $\mathrm{i}_0, \mathrm{i}_1$ are trivial cofibrations.
>
> **Reflexivity.** $H = f\sigma$ satisfies $H\mathrm{i}_0 = H\mathrm{i}_1 = f$.
>
> **Symmetry.** Swapping $\mathrm{i}_0 \leftrightarrow \mathrm{i}_1$ gives a cylinder for $A$ in which a homotopy from $f$ to $g$ reads as a homotopy from $g$ to $f$.
>
> **Transitivity.** Glue $\mathrm{Cyl}(A) \sqcup_A \mathrm{Cyl}'(A)$ along $\mathrm{i}_1 = \mathrm{i}_0'$. Pushout-closure of trivial cofibrations and two-out-of-three show the result $\mathrm{Cyl}''(A)$ is a cylinder for $A$ (outer ends a cofibration, induced $\sigma''$ a weak equivalence). The homotopies $H, H'$ glue to $H'' : \mathrm{Cyl}''(A) \to B$ with $H''\mathrm{i}_0'' = f$, $H''\mathrm{i}_1'' = h$, so $f \simeq_\ell h$. Hence $\simeq_\ell$ is an equivalence relation on $\mathcal{M}(A,B)$ for cofibrant $A$. $\blacksquare$

---

# Key Takeaways

**Cofibrancy of the domain is exactly the hypothesis that makes the end-inclusions trivial cofibrations, and everything good about left homotopy flows from that.** The single lemma "$A$ cofibrant $\Rightarrow$ $\mathrm{i}_0, \mathrm{i}_1$ are trivial cofibrations" is what powers symmetry (the cylinder can be reflected) and transitivity (cylinders can be glued and stay cylinders). Without cofibrancy the summand inclusion $A \to A \sqcup A$ need not be a cofibration, the end-inclusions need not be trivial cofibrations, and the whole equivalence-relation structure collapses. This is the precise reason [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]] builds the homotopy category from bifibrant objects: you need cofibrancy for left homotopy and (dually) fibrancy for right homotopy. The trigger is "I want left homotopy to behave like an equivalence relation"; the requirement is "make the domain cofibrant."

**Transitivity is gluing cylinders, and two-out-of-three is what certifies the glued object is still a cylinder.** The deepest step is recognizing that composing homotopies means concatenating cylinders — gluing the end of one to the start of the next — and that the result is a valid cylinder only because the gluing is a pushout of a trivial cofibration (keeping the outer-end inclusion a cofibration) and because two-out-of-three certifies the new structure map is a weak equivalence. This is the concrete mechanism behind the abstract claim, on [[Def - Model Category]], that "dropping two-out-of-three breaks transitivity of homotopy." Seeing exactly where MC2 enters — certifying $\sigma''$ — makes that motivation precise and shows the axiom is load-bearing for this specific construction.

**The reflection-and-concatenation picture is the topological intuition made axiomatic.** Reflexivity (the constant homotopy), symmetry (run the homotopy backwards), and transitivity (concatenate two homotopies) are exactly the operations on paths of maps that you know from topology, abstracted to cylinders. The abstraction is faithful: in $\mathbf{Top}$ the cylinder is $A \times [0,1]$, reflecting it is $t \mapsto 1-t$, and gluing is laying two intervals end to end to get $A \times [0,2] \cong A \times [0,1]$. Carrying this topological picture into the abstract setting is the right way to remember the construction, and the cofibrancy hypothesis is the price of making "the cylinder is a good object" hold without the geometry to fall back on.
