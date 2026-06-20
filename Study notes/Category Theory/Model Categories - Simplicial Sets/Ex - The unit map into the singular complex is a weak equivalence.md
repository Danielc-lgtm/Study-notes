---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Thm - Geometric Realization is a Quillen Equivalence"
  - "Thm - Geometric Realization is Left Adjoint to the Singular Nerve"
  - "Def - Simplicial Homotopy Group"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Assume the counit $\varepsilon_Y : |\mathrm{Sing}\,Y| \to Y$ is a weak homotopy equivalence for every [[Def - Topological Space|space]] $Y$ (this is the geometric core of [[Thm - Geometric Realization is a Quillen Equivalence]], proved via [[Def - Minimal Fibration|minimal fibrations]]). Using only this and the triangle identities of the [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|adjunction]] $|{-}| \dashv \mathrm{Sing}$, prove that the unit
$$\eta_X : X \longrightarrow \mathrm{Sing}\,|X|$$
is a weak equivalence in $\mathbf{sSet}$ for every [[Def - Simplicial Set|simplicial set]] $X$. Conclude that $|{-}| \dashv \mathrm{Sing}$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]].

**Recall:**

For an adjunction $|{-}| \dashv \mathrm{Sing}$ with unit $\eta : \mathrm{id} \Rightarrow \mathrm{Sing}\,|{-}|$ and counit $\varepsilon : |\mathrm{Sing}\,{-}| \Rightarrow \mathrm{id}$, the **triangle identities** are
$$\varepsilon_{|X|} \circ |\eta_X| = \mathrm{id}_{|X|}, \qquad \mathrm{Sing}(\varepsilon_Y) \circ \eta_{\mathrm{Sing}\,Y} = \mathrm{id}_{\mathrm{Sing}\,Y}.$$

A map $f$ in $\mathbf{sSet}$ is a **weak equivalence** iff $|f|$ is a weak homotopy equivalence in $\mathbf{Top}$ ([[Thm - Simplicial Sets Form a Model Category]]). Weak homotopy equivalences satisfy **two-out-of-three**: if two of $f, g, gf$ are weak equivalences, so is the third.

A [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]] is a **Quillen equivalence** iff the derived unit (on [[Def - Cofibrant and Fibrant Objects|cofibrant]] objects) and derived counit (on fibrant objects) are weak equivalences.

---

# Convergent Strategy

**Problem class:** This is a *comparison* problem of the comparison world (topic-page Problem-Solving Strategy): deduce one half of a Quillen equivalence (the unit) from the other (the counit), purely formally. The routine is the triangle-identity trick: the unit, realised, appears in a triangle identity alongside the counit, and two-out-of-three transfers the weak-equivalence property.

**Assumption pattern:** The recognisable feature is "counit is a weak equivalence + adjunction triangle identities". The triangle identity $\varepsilon_{|X|} \circ |\eta_X| = \mathrm{id}$ packages $\eta$, $\varepsilon$, and an identity into a single composite, which is exactly the setup for two-out-of-three. The recognition is that the *definition* of weak equivalence in $\mathbf{sSet}$ (via realisation) is what lets a fact about $|\eta_X|$ become a fact about $\eta_X$.

**Theorem routing:** The route is: triangle identity $\varepsilon_{|X|}\circ|\eta_X| = \mathrm{id}_{|X|}$ $\to$ $\varepsilon_{|X|}$ is a weak homotopy equivalence (hypothesis) and $\mathrm{id}$ is one $\to$ two-out-of-three forces $|\eta_X|$ to be a weak homotopy equivalence $\to$ by definition of weak equivalences in $\mathbf{sSet}$, $\eta_X$ is a weak equivalence. Then assemble: every object cofibrant, every space fibrant, derived unit and counit both weak equivalences $\Rightarrow$ Quillen equivalence.

**Key decision point:** The crux is noticing that "$\eta_X$ is a weak equivalence" is *defined* to mean "$|\eta_X|$ is a weak homotopy equivalence", so the triangle identity (which involves $|\eta_X|$, not $\eta_X$) lands exactly on the right object. The natural confusion is to try to argue about $\eta_X$ directly in $\mathbf{sSet}$; the point is that the simplicial weak equivalences are *defined* through realisation, so one never leaves the realised picture.

---

# Legal Operations Used

1. **Operation 7 from the topic page (pass to realisation).** The simplicial weak equivalence $\eta_X$ is detected by its realisation $|\eta_X|$, which is where the triangle identity and two-out-of-three operate.

2. **The triangle identities (from [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]).** The identity $\varepsilon_{|X|}\circ|\eta_X| = \mathrm{id}_{|X|}$ is the algebraic relation that connects the unit to the counit.

3. **Two-out-of-three for weak equivalences (from [[Def - Model Category]] / [[Thm - Simplicial Sets Form a Model Category]]).** Applied to the triangle-identity composite, it transfers the weak-equivalence property from $\varepsilon_{|X|}$ and $\mathrm{id}$ to $|\eta_X|$.

---

# Hints

> [!note]- Hint 1
> You are *given* the counit is a weak equivalence and asked about the unit. The two are linked by a triangle identity. Write down the triangle identity that involves $|\eta_X|$.

> [!note]- Hint 2
> The identity is $\varepsilon_{|X|} \circ |\eta_X| = \mathrm{id}_{|X|}$. The composite is the identity (a weak homotopy equivalence) and $\varepsilon_{|X|}$ is a weak homotopy equivalence by hypothesis (it is the counit at the space $|X|$). What does two-out-of-three give for $|\eta_X|$?

> [!note]- Hint 3
> Two-out-of-three on $\varepsilon_{|X|} \circ |\eta_X| = \mathrm{id}$: since the composite and $\varepsilon_{|X|}$ are weak homotopy equivalences, so is $|\eta_X|$. Now recall: what does "$\eta_X$ is a weak equivalence *in $\mathbf{sSet}$*" mean?

> [!note]- Hint 4
> Weak equivalences in $\mathbf{sSet}$ are *defined* as the maps whose realisation is a weak homotopy equivalence. So "$|\eta_X|$ is a weak homotopy equivalence" *is* "$\eta_X$ is a weak equivalence". Done.

> [!note]- Hint 5
> For the conclusion: in $\mathbf{sSet}$ every object is cofibrant, in $\mathbf{Top}$ every object is fibrant; you now have derived unit (on cofibrant $X$) and derived counit (on fibrant $Y$) both weak equivalences, which is the definition of Quillen equivalence.

---

# Solution

The unit follows from the counit by one application of a triangle identity and two-out-of-three: the realised unit $|\eta_X|$ sits in the identity $\varepsilon_{|X|}\circ|\eta_X| = \mathrm{id}$, and since the other two maps are weak homotopy equivalences, so is $|\eta_X|$ — which, by definition of simplicial weak equivalences, means $\eta_X$ is a weak equivalence.

**Step 1: Write the triangle identity at $X$.**

> [!note]- Derivation
> The [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|adjunction]] $|{-}| \dashv \mathrm{Sing}$ has triangle identities; the relevant one is
> $$\varepsilon_{|X|} \circ |\eta_X| = \mathrm{id}_{|X|},$$
> a commuting triangle in $\mathbf{Top}$: realise the unit $\eta_X : X \to \mathrm{Sing}|X|$ to get $|\eta_X| : |X| \to |\mathrm{Sing}|X||$, then apply the counit $\varepsilon_{|X|} : |\mathrm{Sing}|X|| \to |X|$; the composite is the identity on $|X|$.

**Step 2: Apply two-out-of-three.**

> [!note]- Derivation
> In this composite, the total map $\mathrm{id}_{|X|}$ is a weak homotopy equivalence (the identity always is), and $\varepsilon_{|X|}$ is a weak homotopy equivalence by the standing hypothesis (the counit at the space $|X|$). By [[Def - Model Category|two-out-of-three]] for weak homotopy equivalences applied to $\mathrm{id}_{|X|} = \varepsilon_{|X|} \circ |\eta_X|$, the remaining map $|\eta_X|$ is a weak homotopy equivalence.

**Step 3: Translate back to $\mathbf{sSet}$.**

> [!note]- Derivation
> By the [[Thm - Simplicial Sets Form a Model Category|definition of the Kan–Quillen weak equivalences]], a map $f$ of [[Def - Simplicial Set|simplicial sets]] is a weak equivalence precisely when $|f|$ is a weak homotopy equivalence. Step 2 showed $|\eta_X|$ is a weak homotopy equivalence, so $\eta_X : X \to \mathrm{Sing}|X|$ is a weak equivalence in $\mathbf{sSet}$, for every $X$.

**Step 4: Conclude the Quillen equivalence.**

> [!note]- Derivation
> $|{-}| \dashv \mathrm{Sing}$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]] (geometric realisation is left Quillen). To upgrade to a Quillen equivalence we need the *derived* unit (on [[Def - Cofibrant and Fibrant Objects|cofibrant]] objects) and *derived* counit (on fibrant objects) to be weak equivalences. In $\mathbf{sSet}$ every object is cofibrant, so the derived unit at $X$ is $\eta_X$ — a weak equivalence by Step 3. In $\mathbf{Top}$ every object is fibrant, so the derived counit at $Y$ is $\varepsilon_Y$ — a weak homotopy equivalence by hypothesis. Both conditions hold, so $|{-}| \dashv \mathrm{Sing}$ is a Quillen equivalence, and $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$.

> [!note]- Complete formal solution
> The triangle identity of $|{-}| \dashv \mathrm{Sing}$ gives $\varepsilon_{|X|} \circ |\eta_X| = \mathrm{id}_{|X|}$ in $\mathbf{Top}$. The composite is a weak homotopy equivalence (identity) and $\varepsilon_{|X|}$ is one (hypothesis, counit at $|X|$), so by two-out-of-three $|\eta_X|$ is a weak homotopy equivalence. Since simplicial weak equivalences are defined as maps with weak-homotopy-equivalence realisation, $\eta_X$ is a weak equivalence in $\mathbf{sSet}$. As every simplicial set is cofibrant and every space fibrant, the derived unit ($= \eta_X$) and derived counit ($= \varepsilon_Y$) are weak equivalences, so $|{-}| \dashv \mathrm{Sing}$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]], giving $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$. $\quad\blacksquare$

---

# Key Takeaways

**One half of a Quillen equivalence often implies the other by the triangle-identity trick.** The structural lesson is that the unit and counit of an adjunction are not independent: the triangle identities lock them together, so a weak-equivalence statement about one transfers to the other by two-out-of-three. The trigger-reaction: *to show a derived unit is a weak equivalence, look for the triangle identity that expresses its realisation as a factor of an identity, then use two-out-of-three with the (assumed) counit.* This trick recurs throughout the comparison of homotopy theories — proving that a Quillen adjunction is an equivalence almost always reduces the harder of the two unit/counit conditions to the easier one via a triangle identity. It is why one usually proves only the geometrically substantive half (here, the counit) and gets the other for free.

**The definition of weak equivalence by realisation is what makes the formal argument land.** A potential confusion is that the triangle identity lives in $\mathbf{Top}$ (it involves $|\eta_X|$), while we want a statement in $\mathbf{sSet}$ (about $\eta_X$). The resolution is that the simplicial weak equivalences are *defined* through realisation, so "$|\eta_X|$ is a weak homotopy equivalence" and "$\eta_X$ is a weak equivalence" are the *same statement*. The transferable point: when a class of maps is defined by a functor (here, $|{-}|$), facts proved on the image transfer back tautologically — choosing the right definition of weak equivalence is what makes formal arguments like this one go through without any genuine simplicial work.

**The geometric content is isolated in one place — the counit — and everything else is formal.** This exercise makes vivid the division of labour in the proof of the Quillen equivalence: the *only* hard, geometric input is that the counit $\varepsilon_Y$ is a weak homotopy equivalence (which needs [[Def - Minimal Fibration|minimal fibrations]] and product-preservation), and *everything else* — the unit, the descent to homotopy categories — is formal adjunction bookkeeping. The diagnostic to carry into any big comparison theorem: locate the single geometric/analytic fact that does the real work, prove only that, and derive the rest formally. Recognising which step is the irreducible content, and which steps are free, is the difference between a proof that feels like magic and one that feels inevitable.
