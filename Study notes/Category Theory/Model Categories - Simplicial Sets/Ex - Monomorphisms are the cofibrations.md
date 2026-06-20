---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Kan Fibration and Anodyne Extension"
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Pullback and Pushout"
  - "Thm - Simplicial Sets Form a Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that in the Kan–Quillen [[Thm - Simplicial Sets Form a Model Category|model structure]] on $\mathbf{sSet}$, the cofibrations are exactly the monomorphisms. Precisely: prove that a map $f : A \to B$ of [[Def - Simplicial Set|simplicial sets]] lies in $\mathrm{cof}(I) = \mathrm{LLP}(\mathrm{RLP}(I))$, where $I = \{\partial\Delta^n \hookrightarrow \Delta^n : n \ge 0\}$, if and only if $f$ is a monomorphism (injective in every dimension). Deduce that every simplicial set is [[Def - Cofibrant and Fibrant Objects|cofibrant]].

**Recall:**

A [[Def - Simplicial Set|simplicial set]] is a functor $X : \Delta^{op} \to \mathbf{Set}$; a map is a natural transformation, so it is a **monomorphism** exactly when each component $f_n : A_n \to B_n$ is injective. The **boundary** $\partial\Delta^n \subset \Delta^n$ is the union of the $n+1$ faces of the standard $n$-simplex.

A map $i$ has the **left [[Def - Lifting Property and the Retract Argument|lifting property]]** against $p$ (and $p$ the right lifting property against $i$) if every commuting square with $i$ on the left and $p$ on the right admits a diagonal lift. For a set $I$, $\mathrm{RLP}(I)$ is the class with the right lifting property against every member of $I$, and $\mathrm{cof}(I) = \mathrm{LLP}(\mathrm{RLP}(I))$ is the **saturation** of $I$.

A simplex $\sigma \in B_n$ is **non-degenerate** if it is not $s_i\tau$ for any lower simplex $\tau$; every simplex is uniquely a degeneracy of a non-degenerate one (Eilenberg–Zilber). An object $X$ is **cofibrant** if $\varnothing \to X$ is a cofibration.

---

# Convergent Strategy

**Problem class:** This is a *class-identification* problem of the lifting world (see the topic page's Problem-Solving Strategy): we must show a class defined implicitly by a lifting condition, $\mathrm{cof}(I)$, coincides with a class defined explicitly by an elementary property, "monomorphism". The standard routine is to prove the two inclusions separately, using on one side that $\mathrm{cof}(I)$ is the *smallest* saturated class containing $I$ and on the other that monomorphisms *are* saturated and contain $I$.

**Assumption pattern:** The recognisable feature is that the generators are *boundary inclusions*, and a boundary inclusion attaches exactly one non-degenerate simplex. This unlocks the cellular description: any monomorphism is built by attaching the non-degenerate simplices of the target one at a time, each attachment a [[Def - Pullback and Pushout|pushout]] of some $\partial\Delta^n \hookrightarrow \Delta^n$. The Eilenberg–Zilber unique factorisation is what lets us enumerate "the new simplices" cleanly.

**Theorem routing:** The two directions route differently. For "monomorphism $\Rightarrow \mathrm{cof}(I)$" the route is: skeletal filtration $\to$ each step a pushout of a boundary inclusion $\to$ transfinite composite $\to$ membership in $\mathrm{cell}(I) \subseteq \mathrm{cof}(I)$. For "$\mathrm{cof}(I) \Rightarrow$ monomorphism" the route is: monomorphisms form a saturated class (closed under pushout, transfinite composition, retract) containing $I$, and $\mathrm{cof}(I)$ is the smallest such, so $\mathrm{cof}(I) \subseteq \{$mono$\}$. Both use the closure properties from [[Def - Kan Fibration and Anodyne Extension]].

**Key decision point:** The non-obvious choice is to filter $B$ by *skeleta* and attach *non-degenerate* simplices, not arbitrary ones. If you tried to attach every simplex you would re-attach degeneracies and the pushout squares would not be boundary inclusions. The Eilenberg–Zilber lemma is exactly what guarantees that attaching only the non-degenerate simplices, in increasing dimension, recovers all of $B$.

---

# Legal Operations Used

1. **Operation 2 from the topic page (build a cofibration by attaching cells).** This is the heart of the forward direction: $A \hookrightarrow B$ is realised as a transfinite composite of pushouts of boundary inclusions, one per non-degenerate simplex of $B$ not in $A$.

2. **Operation 8 from the topic page (every object is cofibrant).** The deduction that every simplicial set is cofibrant is the special case $A = \varnothing$: $\varnothing \to X$ is injective in every dimension (vacuously), hence a monomorphism, hence a cofibration.

3. **The closure properties of $\mathrm{LLP}(\mathcal{S})$ (from [[Def - Kan Fibration and Anodyne Extension]]).** The reverse direction uses that *any* class of the form $\mathrm{cof}(I)$ is the smallest saturated class containing $I$, against the saturated class of monomorphisms.

---

# Hints

> [!note]- Hint 1
> Prove two inclusions. One direction is "every monomorphism is in $\mathrm{cof}(I)$"; the other is "every map in $\mathrm{cof}(I)$ is a monomorphism". They use opposite facts about saturated classes.

> [!note]- Hint 2
> For the reverse direction, ask: is the class of monomorphisms closed under pushout, transfinite composition, and retract? And does it contain every boundary inclusion? If both, it contains the *smallest* such class, which is $\mathrm{cof}(I)$.

> [!note]- Hint 3
> For the forward direction, filter $B$ by skeleta $A = \mathrm{sk}_{-1} \subseteq \mathrm{sk}_0 \subseteq \mathrm{sk}_1 \subseteq \dots$ where $\mathrm{sk}_n$ adds the non-degenerate simplices of dimension $\le n$ in $B \setminus A$. Show $\mathrm{sk}_{n-1} \hookrightarrow \mathrm{sk}_n$ is a pushout of a coproduct of boundary inclusions $\partial\Delta^n \hookrightarrow \Delta^n$, one per new non-degenerate $n$-simplex.

> [!note]- Hint 4
> The attaching map for a new non-degenerate $n$-simplex $\sigma$ is its boundary $\partial\Delta^n \to \mathrm{sk}_{n-1}$, which is well-defined because all faces $d_i\sigma$ are simplices of dimension $< n$, hence already present (each face is a degeneracy of a non-degenerate simplex of dimension $< n$).

---

# Solution

The proof is two inclusions. The reverse inclusion $\mathrm{cof}(I) \subseteq \{$mono$\}$ is short: monomorphisms form a saturated class containing $I$, so they contain the smallest such class $\mathrm{cof}(I)$. The forward inclusion $\{$mono$\} \subseteq \mathrm{cof}(I)$ is the cellular construction: filter the target by skeleta and attach one non-degenerate simplex at a time. The cofibrancy of every object is the case $A = \varnothing$.

**Step 1: Monomorphisms are saturated and contain $I$, giving $\mathrm{cof}(I) \subseteq \{$mono$\}$.**

> [!note]- Derivation
> A map of [[Def - Simplicial Set|simplicial sets]] is a monomorphism iff each $f_n : A_n \to B_n$ is injective, because mono in a [[Def - Presheaf|presheaf]] category is detected level-wise. In $\mathbf{Set}$, injections are closed under pushout (a pushout of an injection along any map is an injection), transfinite composition (a colimit of a chain of injections is an injection), and retract (a retract of an injection in the arrow category is an injection). Since these colimits in $\mathbf{sSet}$ are computed level-wise, monomorphisms of simplicial sets are likewise closed under pushout, transfinite composition, and retract — they form a *saturated* class. Each boundary inclusion $\partial\Delta^n \hookrightarrow \Delta^n$ is a monomorphism. Now $\mathrm{cof}(I) = \mathrm{LLP}(\mathrm{RLP}(I))$ is, by general nonsense, the *smallest* saturated class containing $I$. Therefore $\mathrm{cof}(I) \subseteq \{$monomorphisms$\}$.

**Step 2: Skeletal filtration of a monomorphism.**

> [!note]- Derivation
> Let $f : A \hookrightarrow B$ be a monomorphism; identify $A$ with its image, a sub-simplicial-set of $B$. Define $\mathrm{sk}_n^A(B) \subseteq B$ to be the sub-simplicial-set generated by $A$ together with all simplices of $B$ of dimension $\le n$. Then
> $$A = \mathrm{sk}_{-1} \subseteq \mathrm{sk}_0 \subseteq \mathrm{sk}_1 \subseteq \cdots, \qquad B = \bigcup_n \mathrm{sk}_n = \operatorname*{colim}_n \mathrm{sk}_n.$$
> By the Eilenberg–Zilber lemma every simplex of $B$ is uniquely a degeneracy of a non-degenerate simplex, so $\mathrm{sk}_n$ differs from $\mathrm{sk}_{n-1}$ exactly by the **non-degenerate** $n$-simplices of $B$ not in $A$ (and their degeneracies, which are forced).

**Step 3: Each skeletal step is a pushout of boundary inclusions.**

> [!note]- Derivation
> Let $S_n$ be the set of non-degenerate $n$-simplices of $B$ not in $A$. For $\sigma \in S_n$, every face $d_i\sigma$ has dimension $n-1$, hence lies in $\mathrm{sk}_{n-1}$; so the boundary of $\sigma$ defines a map $\partial\Delta^n \to \mathrm{sk}_{n-1}$. Assembling over all $\sigma \in S_n$ gives a pushout square
> $$\begin{array}{ccc} \coprod_{\sigma \in S_n} \partial\Delta^n & \longrightarrow & \mathrm{sk}_{n-1} \\ \downarrow & & \downarrow \\ \coprod_{\sigma \in S_n} \Delta^n & \longrightarrow & \mathrm{sk}_n \end{array}$$
> The lower map sends the $\sigma$-th copy of $\Delta^n$ to $\sigma$ (using $\mathbf{sSet}(\Delta^n, B) \cong B_n$, the [[Thm - The Yoneda Lemma|Yoneda]] identification). This square is a [[Def - Pullback and Pushout|pushout]]: $\mathrm{sk}_n$ is obtained from $\mathrm{sk}_{n-1}$ by gluing in each new non-degenerate $\sigma$ along its already-present boundary, which is exactly what the pushout computes. A coproduct of boundary inclusions is in $\mathrm{cell}(I)$, and a pushout of a $\mathrm{cell}(I)$-map is in $\mathrm{cell}(I)$.

**Step 4: Assemble and conclude cofibrancy.**

> [!note]- Derivation
> Each $\mathrm{sk}_{n-1} \hookrightarrow \mathrm{sk}_n$ is in $\mathrm{cell}(I)$ (Step 3), and $A \hookrightarrow B$ is their transfinite composite $\mathrm{colim}_n \mathrm{sk}_n$ (Step 2). Transfinite composites of $\mathrm{cell}(I)$-maps are in $\mathrm{cell}(I) \subseteq \mathrm{cof}(I)$. Hence every monomorphism is in $\mathrm{cof}(I)$, completing $\{$mono$\} \subseteq \mathrm{cof}(I)$. With Step 1, $\mathrm{cof}(I) = \{$monomorphisms$\}$. Finally, for any $X$ the map $\varnothing \to X$ is injective in every dimension (the empty function is injective), so it is a monomorphism, hence a cofibration: **every simplicial set is [[Def - Cofibrant and Fibrant Objects|cofibrant]]**.

> [!note]- Complete formal solution
> ($\mathrm{cof}(I) \subseteq$ mono.) Monomorphisms of simplicial sets are the level-wise injections; in $\mathbf{Set}$ injections are closed under pushout, transfinite composition, and retract, and these colimits are level-wise in $\mathbf{sSet}$, so monomorphisms are a saturated class. Each $\partial\Delta^n \hookrightarrow \Delta^n$ is mono. As $\mathrm{cof}(I)$ is the smallest saturated class containing $I$, $\mathrm{cof}(I) \subseteq \{$mono$\}$.
>
> (mono $\subseteq \mathrm{cof}(I)$.) Let $A \hookrightarrow B$ be mono. Filter by $\mathrm{sk}_n$ = (sub-simplicial-set generated by $A$ and the $\le n$-simplices); then $B = \mathrm{colim}_n \mathrm{sk}_n$ and, by Eilenberg–Zilber, $\mathrm{sk}_n$ adds exactly the non-degenerate $n$-simplices $S_n$ of $B \setminus A$. The square with corners $\coprod_{S_n}\partial\Delta^n,\ \mathrm{sk}_{n-1},\ \coprod_{S_n}\Delta^n,\ \mathrm{sk}_n$ is a pushout (each new $\sigma$ is glued along its already-present boundary), so $\mathrm{sk}_{n-1}\hookrightarrow\mathrm{sk}_n \in \mathrm{cell}(I)$. The transfinite composite $A \hookrightarrow B$ is in $\mathrm{cell}(I) \subseteq \mathrm{cof}(I)$.
>
> Hence cofibrations $= \mathrm{cof}(I) =$ monomorphisms. Taking $A = \varnothing$, every $\varnothing \to X$ is mono, so every simplicial set is cofibrant. $\quad\blacksquare$

---

# Key Takeaways

**Cofibrations are the cheapest class, and that shapes the entire homotopy theory.** The lesson is that in $\mathbf{sSet}$ "cofibration" imposes *no* condition beyond injectivity, so cofibrancy is automatic and free. This is unlike most model categories — chain complexes, spaces — where cofibrant replacement is a real construction. The downstream consequence is that all the homotopical asymmetry of $\mathbf{sSet}$ sits on the *fibrant* side: derived functors out of $\mathbf{sSet}$ never need to resolve the source, only fibrantly replace the target. Whenever you meet the general model-category formalism asking for $QX$, the trigger-reaction is "$QX = X$, skip it". Recognising which side of a model category is the "free" side is one of the first things to determine about any homotopy theory, and here it is decisively the cofibrant side.

**The skeletal filtration is the universal tool for proving things about all monomorphisms.** The technique — filter the target by skeleta, attach non-degenerate cells one dimension at a time, each attachment a pushout of a boundary inclusion — is not specific to this problem. It is the standard induction for *any* statement about cofibrations in a presheaf homotopy theory: to prove a left Quillen functor preserves cofibrations, to build a map out of $B$ extending one out of $A$, to verify a property closed under cell attachment. The trigger is "prove something for every monomorphism / cofibration"; the reaction is "induct over skeleta, reduce to a single boundary-inclusion pushout". The Eilenberg–Zilber unique-factorisation lemma is the silent enabler: it is what guarantees the non-degenerate simplices form a clean, non-redundant set of cells.

**Identifying a lifting-defined class with an elementary class is a two-inclusion saturation argument.** The shape of this proof recurs throughout cofibrantly generated homotopy theory: a class is defined as $\mathrm{cof}(I)$ or $\mathrm{LLP}(\dots)$, and one wants an elementary description. The forward inclusion is always "the elementary class is saturated and contains the generators, hence contains $\mathrm{cof}(I)$"; the reverse is always "the generators have the property and it is preserved by the cell construction, so $\mathrm{cell}(I)$ — hence $\mathrm{cof}(I)$ via retracts — has it". Internalising this template lets you read off, for instance, that the trivial fibrations are exactly the maps with RLP against boundaries, or that anodyne maps are exactly the trivial cofibrations — the same argument with $I$ replaced by $J$. The general principle: *a saturated class is pinned down by its generators plus the closure operations.*
