---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Model Category"
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a bicomplete category (all small limits and colimits exist). Show that taking the weak equivalences to be the isomorphisms and *both* the cofibrations and the fibrations to be *all* maps of $\mathcal{C}$ defines a model structure. Verify all five Quillen axioms. Then identify the homotopy category $\mathrm{Ho}(\mathcal{C})$ for this model structure, and determine which objects are cofibrant and which are fibrant.

(There are two further "trivial" model structures on $\mathcal{C}$, obtained by instead making the cofibrations or the fibrations equal to the isomorphisms; comment briefly on whether they are also model structures.)

**Recall:**

A [[Def - Model Category|model category]] is a bicomplete category with three classes of maps — weak equivalences, cofibrations, fibrations — satisfying:

![[Def - Model Category#The Definition]]

A map $i$ has the **left lifting property** against $p$ (and $p$ the **right lifting property** against $i$) if every commuting square with $i$ on the left and $p$ on the right admits a diagonal filler:

![[Def - Lifting Property and the Retract Argument#The Definition]]

The [[Thm - The Homotopy Category of a Model Category|homotopy category]] $\mathrm{Ho}(\mathcal{C})$ is the localization $\mathcal{C}[\mathcal{W}^{-1}]$ at the weak equivalences.

---

# Convergent Strategy

**Problem class:** This is an axiom-verification problem — the first of the five recurring targets named on the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Sources and Targets|topic page]]. The routine for such problems is to dispatch the cheap axioms (MC1, MC2, MC3) directly and then concentrate on lifting (MC4) and factorization (MC5). Here the structure is so degenerate that even MC4 and MC5 are easy, which is exactly why it is a good first exercise: it isolates the *shape* of an axiom check without the difficulty.

**Assumption pattern:** The decisive feature is that the weak equivalences are the isomorphisms and the other two classes are everything. This means "trivial cofibration" = "trivial fibration" = "isomorphism," and the lifting and factorization axioms reduce to statements about isomorphisms, which are automatic. Recognizing that the trivial maps collapse to isomorphisms is what unlocks the whole problem.

**Theorem routing:** No deep theorem is needed; the route is straight from the definitions. For the homotopy category, route through [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]]: since every map is both a cofibration and a fibration, every object is bifibrant, and the weak equivalences being isomorphisms means the homotopy relation is trivial, so $\mathrm{Ho}(\mathcal{C}) = \mathcal{C}$.

**Key decision point:** The one genuine subtlety is factorization. You must produce, for every map $f$, a factorization as (cofibration)-then-(trivial fibration) and as (trivial cofibration)-then-(fibration). The non-obvious choice is to factor through an identity: $f = f \circ \mathrm{id}$ or $f = \mathrm{id} \circ f$, putting the isomorphism (identity) in the slot that must be trivial. Getting which slot needs the identity right is the crux.

---

# Legal Operations Used

1. **Operation 8 from the topic page (recognize a class by its lifting property), used in reverse.** Here every map is declared a cofibration and a fibration outright, so we instead *check* that the lifting axiom holds for these declared classes rather than deriving the classes from lifting. The trivial maps being isomorphisms is what makes the lifts exist.

2. **Operation 1 from the topic page (factor a map), via the identity.** The factorizations are built by inserting an identity map, so that the factor required to be trivial (an isomorphism) is literally an identity.

3. **Operation 5 from the topic page (use 2-out-of-3).** MC2 is checked by the standard fact that isomorphisms satisfy 2-out-of-3: if two of $f, g, gf$ are isomorphisms, so is the third.

---

# Hints

> [!note]- Hint 1
> Figure out first what "trivial cofibration" and "trivial fibration" mean in this model structure. Since trivial means "also a weak equivalence" and the weak equivalences are the isomorphisms, both trivial classes are exactly the isomorphisms.

> [!note]- Hint 2
> For the lifting axiom MC4: one side of every lifting square is now an isomorphism. If $p$ is a trivial fibration (= isomorphism), can you always lift? Set the diagonal to $p^{-1}$ composed with the bottom map.

> [!note]- Hint 3
> For factorization MC5, write $f = \mathrm{id} \circ f$ and $f = f \circ \mathrm{id}$. Check which one puts the identity (an isomorphism, hence both a trivial cofibration and a trivial fibration) in the slot the axiom requires to be trivial.

> [!note]- Hint 4
> For the homotopy category: every object is bifibrant, and since the weak equivalences are already isomorphisms, there is nothing to invert that was not already invertible. Use [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]] or argue directly that the localization is $\mathcal{C}$ itself.

---

# Solution

The proof verifies the five axioms in turn, using throughout that the trivial cofibrations and trivial fibrations both equal the isomorphisms; then identifies $\mathrm{Ho}(\mathcal{C}) = \mathcal{C}$ because the weak equivalences are already isomorphisms. The only step with content is factorization, handled by inserting an identity.

**Step 1: The trivial classes are the isomorphisms.**

A trivial cofibration is a cofibration (= any map) that is a weak equivalence (= isomorphism), so it is an isomorphism; likewise every trivial fibration is an isomorphism, and conversely every isomorphism lies in both trivial classes.

> [!note]- Derivation
> By definition trivial cofibration $=$ cofibration $\cap\, \mathcal{W}$. Here cofibrations $=$ all maps and $\mathcal{W} =$ isomorphisms, so trivial cofibrations $=$ isomorphisms. Identically, trivial fibrations $=$ fibrations $\cap\, \mathcal{W} =$ all maps $\cap$ isomorphisms $=$ isomorphisms.

**Step 2: MC1, MC2, MC3 hold.**

Bicompleteness is assumed. Isomorphisms satisfy 2-out-of-3, and all three classes are closed under retracts.

> [!note]- Derivation
> MC1: $\mathcal{C}$ is bicomplete by hypothesis. MC2: if two of $f, g, gf$ are isomorphisms, so is the third — if $f, g$ iso then $gf$ iso; if $g, gf$ iso then $f = g^{-1}(gf)$ iso; if $f, gf$ iso then $g = (gf)f^{-1}$ iso. MC3: the classes "all maps" are trivially closed under retracts; and the isomorphisms are closed under retracts (a retract of an isomorphism is an isomorphism — chase the retract diagram, the retraction provides the inverse).

**Step 3: MC4 (lifting) holds.**

In a square with a cofibration on the left and a trivial fibration (= isomorphism) on the right, the lift is $p^{-1}$ composed with the bottom map; dually for the other case.

> [!note]- Derivation
> Case 1: $i$ a cofibration, $p$ a trivial fibration, so $p$ is an isomorphism. Given a square with top $u$, bottom $v$ (so $p u = v i$), set $h = p^{-1} v$. Then $p h = v$, and $h i = p^{-1} v i = p^{-1} p u = u$, so $h$ is a lift. Case 2: $i$ a trivial cofibration (isomorphism), $p$ a fibration. Set $h = u\, i^{-1}$. Then $h i = u$ and $p h = p u i^{-1} = v i i^{-1} = v$. Both lifting axioms hold.

**Step 4: MC5 (factorization) holds.**

Every map factors via an inserted identity.

> [!note]- Derivation
> Given $f : A \to B$, write $f = f \circ \mathrm{id}_A$: here $\mathrm{id}_A$ is a cofibration (every map is) and is an isomorphism hence a trivial fibration — wait, we need the *first* factor a cofibration and the *second* a trivial fibration. So instead write $f = \mathrm{id}_B \circ f$: the first factor $f$ is a cofibration (every map is) and the second factor $\mathrm{id}_B$ is an isomorphism, hence a trivial fibration. This gives the (cofibration, trivial fibration) factorization. For the (trivial cofibration, fibration) factorization, write $f = f \circ \mathrm{id}_A$: the first factor $\mathrm{id}_A$ is an isomorphism, hence a trivial cofibration, and the second factor $f$ is a fibration (every map is). Both required factorizations exist.

**Step 5: Identify the homotopy category and the (co)fibrant objects.**

Every object is bifibrant, and $\mathrm{Ho}(\mathcal{C}) = \mathcal{C}$.

> [!note]- Derivation
> For any object $X$, the map $\varnothing \to X$ is a cofibration (every map is), so $X$ is cofibrant; likewise $X \to *$ is a fibration, so $X$ is fibrant. Hence every object is bifibrant. The localization $\mathcal{C}[\mathcal{W}^{-1}]$ inverts the isomorphisms, which are already invertible, so it changes nothing: $\mathrm{Ho}(\mathcal{C}) = \mathcal{C}$. Via [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]], the homotopy relation on maps between bifibrant objects is trivial here (two maps are homotopic iff equal, since a cylinder for $A$ can be taken to be $A$ itself with the fold map factoring as $A \sqcup A \to A \xrightarrow{\mathrm{id}} A$, and a left homotopy then forces $f = g$), so $\pi(X, Y) = \mathcal{C}(X, Y)$ and $\mathrm{Ho}(\mathcal{C}) \simeq \mathcal{C}$.

> [!note]- Complete formal solution
> Define on the bicomplete category $\mathcal{C}$: weak equivalences $=$ isomorphisms, cofibrations $=$ all maps, fibrations $=$ all maps. Then trivial cofibrations $=$ trivial fibrations $=$ isomorphisms (Step 1).
>
> **MC1** holds by hypothesis. **MC2** holds because isomorphisms satisfy 2-out-of-3. **MC3** holds because "all maps" is retract-closed and isomorphisms are retract-closed.
>
> **MC4:** Given a square with $i$ on the left and a trivial fibration $p$ (an isomorphism) on the right, top $u$, bottom $v$, the diagonal $h = p^{-1}v$ satisfies $hi = u$ and $ph = v$. Given $i$ a trivial cofibration (isomorphism) and $p$ a fibration, the diagonal $h = u i^{-1}$ works. Both lifting axioms hold.
>
> **MC5:** Any $f : A \to B$ factors as $f = \mathrm{id}_B \circ f$ (cofibration then trivial fibration) and as $f = f \circ \mathrm{id}_A$ (trivial cofibration then fibration).
>
> Thus the triple is a model structure. Every object is bifibrant, since $\varnothing \to X$ and $X \to *$ are maps, hence a cofibration and a fibration respectively. The localization inverts isomorphisms, which are already invertible, so $\mathrm{Ho}(\mathcal{C}) \simeq \mathcal{C}$.
>
> **The other trivial structures.** Setting cofibrations $=$ isomorphisms, weak equivalences $=$ isomorphisms, fibrations $=$ all maps is *also* a model structure (dual reasoning), as is the symmetric choice. The structure with $\mathcal{W} =$ all maps, cofibrations $=$ fibrations $=$ isomorphisms is the model structure whose homotopy category is the *terminal* category (everything becomes equivalent). $\blacksquare$

---

# Key Takeaways

**The trivial model structure isolates the *shape* of an axiom check.** Verifying a model structure always means: dispatch MC1–MC3 (usually a sentence each), then do real work on lifting and factorization. This exercise lets you rehearse that shape with all the difficulty stripped away, so that when you later meet $\mathbf{Top}$ or $\mathbf{Ch}(R)$ — where MC5 requires the small object argument — you already know exactly which axioms are the cheap ones and which carry the weight. The discipline of always reducing "trivial cofibration" and "trivial fibration" to their concrete meaning before checking MC4 and MC5 is the single most transferable habit here; in this case both reduce to "isomorphism," which trivializes everything.

**Factorization through an identity is the universal cheap factorization, and getting the slots right is the whole point.** Whenever a class contains all maps, you can factor any $f$ by inserting an identity on either side, and the identity — being an isomorphism — sits in whichever trivial class you need. The trap is putting the identity on the wrong side: the (cofibration, trivial fibration) factorization needs the identity *second*, while the (trivial cofibration, fibration) factorization needs it *first*. This same "factor through an identity or an isomorphism" move recurs whenever one factor of a factorization is allowed to be degenerate, and recognizing it saves you from invoking heavy machinery when none is needed.

**A model structure with isomorphisms as weak equivalences has a trivial homotopy category, which is the sanity check that the framework specializes correctly.** The homotopy category is supposed to be "$\mathcal{C}$ with the weak equivalences inverted"; if the weak equivalences are *already* the isomorphisms, nothing should change, and indeed $\mathrm{Ho}(\mathcal{C}) = \mathcal{C}$. This is the degenerate endpoint of the spectrum: the more weak equivalences you declare (up to "all maps," giving the terminal homotopy category), the more the homotopy category collapses. Keeping this endpoint in mind calibrates your intuition for what a homotopy category *is* — it measures exactly how far the weak equivalences are from being isomorphisms, and when they coincide there is nothing to measure.
