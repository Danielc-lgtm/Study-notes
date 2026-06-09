---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Nullstellensatz Correspondence (radical ideals and varieties)"
  - "Thm - The Strong Nullstellensatz"
  - "Def - Affine Variety and the Vanishing Set"
  - "Def - The Coordinate Ring and the Ideal of a Set"
  - "Def - Radical of an Ideal and the Nilradical"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be an algebraically closed field and let $X, Y$ be algebraic subsets of $k^n$. Consider the two candidate identities:
$$\text{(i)}\quad I(X \cup Y) \overset{?}{=} I(X) \cap I(Y), \qquad\qquad \text{(ii)}\quad I(X \cap Y) \overset{?}{=} I(X) + I(Y).$$
**One is always true; the other needs a $\sqrt{\,\cdot\,}$ over one side.** Determine which, state the corrected identity, prove both, and show by example that the radical cannot be dropped. (This is Example Sheet 3, Question 6(c).)

**Recall:**

The objects in play are the vanishing set, the ideal of a set, the radical, and the Nullstellensatz correspondence.

![[Def - Affine Variety and the Vanishing Set#The Definition]]

![[Thm - The Strong Nullstellensatz#Statement]]

For $X \subseteq k^n$, $I(X) = \{f : f(x) = 0\ \forall x \in X\}$ is the [[Def - The Coordinate Ring and the Ideal of a Set|ideal of the set]], always [[Def - Radical of an Ideal and the Nilradical|radical]]. The **sum** $I(X) + I(Y) = \{f + g : f \in I(X), g \in I(Y)\}$ is the smallest ideal containing both; the **intersection** $I(X) \cap I(Y)$ is the largest ideal contained in both. The [[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|Nullstellensatz correspondence]] makes $V, I$ inverse, inclusion-reversing bijections between algebraic sets and radical ideals over an algebraically closed field.

---

# Convergent Strategy

**Problem class.** This is a *lattice-translation* problem: it computes how the dictionary $X \leftrightarrow I(X)$ carries the geometric operations $\cup, \cap$ to algebraic operations, and pins down exactly where the radical is forced. It is the working content of "the Nullstellensatz correspondence is an *anti-isomorphism of lattices*" — union $\leftrightarrow$ intersection, intersection $\leftrightarrow$ sum-then-radical.

**Assumption pattern.** $X, Y$ are *algebraic sets* over an *algebraically closed* $k$, so the [[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|correspondence]] is available and $V(I(X)) = X$. The union identity (i) is *formal* and needs no Nullstellensatz; the intersection identity (ii) needs the strong Nullstellensatz to insert the radical, because $I(X) + I(Y)$ can fail to be radical even though $I(X), I(Y)$ are.

**Theorem routing.** For (i): a function vanishes on $X \cup Y$ iff it vanishes on $X$ and on $Y$, directly giving $I(X \cup Y) = I(X) \cap I(Y)$ — no theorem needed. For (ii): the naive sum gives the wrong answer, so apply $V$ to $I(X) + I(Y)$ (getting $V(I(X) + I(Y)) = V(I(X)) \cap V(I(Y)) = X \cap Y$ by the [[Def - Affine Variety and the Vanishing Set|formal property]] $V(\mathfrak a + \mathfrak b) = V(\mathfrak a) \cap V(\mathfrak b)$), then apply $I$ and use the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] $I(V(\mathfrak b)) = \sqrt{\mathfrak b}$ to land $I(X \cap Y) = \sqrt{I(X) + I(Y)}$.

**Key decision point.** The non-obvious insight is *why the radical is forced on (ii) and not (i)*. The geometric operation $\cup$ corresponds to $\cap$ of ideals, and the intersection of two radical ideals *is* radical, so no radical is needed. But $\cap$ of varieties corresponds to $+$ of ideals, and the sum of two radical ideals *need not be radical* — geometrically, two varieties can be *tangent*, and the sum ideal then carries a nilpotent recording the higher-order contact. The radical strips that nilpotent, recovering the honest ideal of the intersection. Recognising "$+$ of radicals can fail to be radical, $\cap$ cannot" is the crux; the counterexample must therefore be a *tangential* (non-transverse) intersection.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz#Legal Operations|the topic page's Legal Operations]]:

1. **Translate a union/intersection of varieties via $I$ directly.** Vanishing on a union is vanishing on each piece — this gives (i) with no machinery.

2. **Push $V$ through a sum of ideals.** $V(\mathfrak a + \mathfrak b) = V(\mathfrak a) \cap V(\mathfrak b)$, the formal property converting $+$ to $\cap$.

3. **Apply $I(V(-)) = \sqrt{(-)}$ to insert the radical.** The strong Nullstellensatz on the sum ideal produces the radical in (ii).

4. **Use $V(I(X)) = X$ for algebraic sets.** Recover $X, Y$ from their ideals to close the loop.

5. **Detect non-radicality via a tangential intersection.** A tangency produces a nilpotent in the sum ideal, the counterexample to dropping $\sqrt{\cdot}$.

---

# Hints

> [!note]- Hint 1
> Start with (i). A polynomial vanishes on $X \cup Y$ exactly when it vanishes on $X$ *and* on $Y$. Translate "vanishes on $X$ and on $Y$" into ideal language — is it $\cap$ or $+$? No Nullstellensatz is needed for this one.

> [!note]- Hint 2
> (i) is the true one: $I(X \cup Y) = I(X) \cap I(Y)$, because $I(X) \cap I(Y) = \{f : f \in I(X) \text{ and } f \in I(Y)\}$ is exactly the functions vanishing on both. Now (ii): why is $I(X \cap Y) = I(X) + I(Y)$ *false*? Compute $V$ of the right side first.

> [!note]- Hint 3
> $V(I(X) + I(Y)) = V(I(X)) \cap V(I(Y)) = X \cap Y$. So $I(X) + I(Y)$ has the *right variety* — but it may not be the *full ideal* of that variety. Apply $I$ to both sides and use the strong Nullstellensatz $I(V(\mathfrak b)) = \sqrt{\mathfrak b}$. What do you get?

> [!note]- Hint 4
> $I(X \cap Y) = I(V(I(X) + I(Y))) = \sqrt{I(X) + I(Y)}$. The radical is necessary: for the counterexample, take two curves *tangent* at a point. Try $X = V(Y - X^2)$ (a parabola) and $Y = V(Y)$ (the $x$-axis) in $k^2$ — they meet only at the origin, but $I(X) + I(Y) = (Y - X^2, Y) = (X^2, Y)$ contains $X^2$ but not $X$, so it is not radical, while $I(X \cap Y) = I(\{0\}) = (X, Y)$.

---

# Solution

The union identity (i) is true and elementary — vanishing on a union is vanishing on each piece. The intersection identity (ii) is false as stated; the correct version is $I(X \cap Y) = \sqrt{I(X) + I(Y)}$, obtained by noting the sum ideal has the right variety but possibly a nilpotent, which the strong Nullstellensatz radical removes. The counterexample is a tangency, where the sum ideal records the contact order as a nilpotent.

**Step 1: Identity (i) is true: $I(X \cup Y) = I(X) \cap I(Y)$.**

A function vanishes on $X \cup Y$ iff it vanishes on both $X$ and $Y$ — which is exactly membership in $I(X) \cap I(Y)$.

> [!note]- Derivation
> For any $f$,
> $$f \in I(X \cup Y) \iff f(z) = 0 \ \forall z \in X \cup Y \iff \big(f(x) = 0\ \forall x \in X\big) \text{ and } \big(f(y) = 0\ \forall y \in Y\big) \iff f \in I(X) \text{ and } f \in I(Y) \iff f \in I(X) \cap I(Y).$$
> So $I(X \cup Y) = I(X) \cap I(Y)$. No algebraic closure or Nullstellensatz is used; this holds for any subsets $X, Y \subseteq k^n$ over any field. (Note both sides are automatically radical, consistent with no $\sqrt{\cdot}$ being needed — the intersection of radical ideals is radical.)

**Step 2: The sum ideal $I(X) + I(Y)$ has variety $X \cap Y$.**

Pushing $V$ through the sum converts $+$ into $\cap$ of varieties.

> [!note]- Derivation
> By the [[Def - Affine Variety and the Vanishing Set|formal property]] $V(\mathfrak a + \mathfrak b) = V(\mathfrak a) \cap V(\mathfrak b)$ (a point kills $\mathfrak a + \mathfrak b$ iff it kills both $\mathfrak a$ and $\mathfrak b$),
> $$V(I(X) + I(Y)) = V(I(X)) \cap V(I(Y)) = X \cap Y,$$
> using $V(I(X)) = X$, $V(I(Y)) = Y$ since $X, Y$ are algebraic ([[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|correspondence]]). So the sum ideal cuts out exactly the intersection — but it may not be the *full* ideal of that intersection.

**Step 3: Identity (ii) corrected: $I(X \cap Y) = \sqrt{I(X) + I(Y)}$.**

Applying $I$ to Step 2 and using the strong Nullstellensatz inserts the radical.

> [!note]- Derivation
> Apply $I$ to the equation $V(I(X) + I(Y)) = X \cap Y$ from Step 2:
> $$I(X \cap Y) = I\big(V(I(X) + I(Y))\big).$$
> By the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]], $I(V(\mathfrak b)) = \sqrt{\mathfrak b}$ for any ideal $\mathfrak b$; with $\mathfrak b = I(X) + I(Y)$,
> $$I(X \cap Y) = \sqrt{I(X) + I(Y)}.$$
> This is the corrected identity. The radical appears because, although $I(X)$ and $I(Y)$ are radical, their *sum* need not be — and $I(X \cap Y)$, being an ideal of a set, must be radical, so it equals the radical of the sum, not the sum itself.

**Step 4: The radical cannot be dropped — a tangency counterexample.**

Take a parabola tangent to a line; the sum ideal contains $X^2$ but not $X$.

> [!note]- Derivation
> In $k^2$, let $X = V(T_2 - T_1^2)$ (the parabola $T_2 = T_1^2$) and $Y = V(T_2)$ (the $T_1$-axis). Their ideals are $I(X) = (T_2 - T_1^2)$ and $I(Y) = (T_2)$, both prime hence radical. They meet only at the origin: $T_2 = T_1^2$ and $T_2 = 0$ force $T_1 = 0$, so $X \cap Y = \{(0,0)\}$, with $I(X \cap Y) = I(\{0\}) = (T_1, T_2)$.
>
> Now compute the sum:
> $$I(X) + I(Y) = (T_2 - T_1^2,\ T_2) = (T_1^2,\ T_2),$$
> since $T_2 - (T_2 - T_1^2) = T_1^2$. This ideal contains $T_1^2$ but **not** $T_1$ (every element of $(T_1^2, T_2)$ has no linear-in-$T_1$ term with zero $T_2$-part). So $(T_1^2, T_2) \subsetneq (T_1, T_2)$ is a *proper* subideal — it is **not radical**, because $T_1^2 \in (T_1^2, T_2)$ but $T_1 \notin (T_1^2, T_2)$. Yet
> $$\sqrt{I(X) + I(Y)} = \sqrt{(T_1^2, T_2)} = (T_1, T_2) = I(X \cap Y),$$
> confirming the corrected identity *and* that the radical is essential: the naive $I(X) + I(Y) = (T_1^2, T_2)$ is strictly smaller than $I(X \cap Y) = (T_1, T_2)$. The nilpotent $\bar T_1$ in $k[T]/(T_1^2, T_2)$ records the *tangency* — the parabola and line meet to second order at the origin, "intersection multiplicity $2$", which the radical erases to recover the reduced point.

> [!note]- Complete formal solution
> **Claim.** Over an algebraically closed $k$, for algebraic sets $X, Y \subseteq k^n$: $I(X \cup Y) = I(X) \cap I(Y)$ (always), and $I(X \cap Y) = \sqrt{I(X) + I(Y)}$ (the radical cannot be dropped).
>
> *(i)* $f \in I(X \cup Y) \iff f$ vanishes on $X$ and on $Y$ $\iff f \in I(X) \cap I(Y)$. Done, no machinery.
>
> *(ii)* $V(I(X) + I(Y)) = V(I(X)) \cap V(I(Y)) = X \cap Y$. Applying $I$ and the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] $I(V(\mathfrak b)) = \sqrt{\mathfrak b}$: $I(X \cap Y) = \sqrt{I(X) + I(Y)}$.
>
> *Radical necessary.* $X = V(T_2 - T_1^2)$, $Y = V(T_2)$: $X \cap Y = \{0\}$, $I(X \cap Y) = (T_1, T_2)$, but $I(X) + I(Y) = (T_1^2, T_2) \subsetneq (T_1, T_2)$ is not radical ($T_1^2 \in$, $T_1 \notin$). So the sum alone is too small; $\sqrt{(T_1^2, T_2)} = (T_1, T_2)$ recovers it. $\blacksquare$

> [!warning] Illegal but tempting: $I(X \cap Y) = I(X) + I(Y)$ without the radical
> The symmetry with identity (i) makes it irresistible to write $I(X \cap Y) = I(X) + I(Y)$. It is false: the sum of two radical ideals need not be radical, because two varieties can meet *non-transversally* (tangentially), and the sum ideal then carries a nilpotent encoding the contact order. The parabola–line example has $I(X) + I(Y) = (T_1^2, T_2)$, missing $T_1$. The repair is the radical: $I(X \cap Y) = \sqrt{I(X) + I(Y)}$, always. The asymmetry between (i) and (ii) traces to a structural fact — *intersection* of radical ideals is radical, but *sum* of radical ideals is not — which is the algebraic shadow of the geometric fact that unions are "clean" but intersections can be "tangent".

---

# Key Takeaways

**The Nullstellensatz correspondence is an anti-isomorphism of lattices, and the radical marks where it is not naive.** The dictionary $X \leftrightarrow I(X)$ swaps $\cup \leftrightarrow \cap$ and $\cap \leftrightarrow +$ (up to radical), reversing inclusions throughout. The clean half is union-to-intersection (no radical); the subtle half is intersection-to-sum, where the radical is forced because the sum of radical ideals need not be radical. The trigger to remember: whenever you translate a *geometric intersection* into a *sum of ideals*, you must take the radical — the bare sum gives a possibly non-reduced (scheme-theoretic) intersection, and only the radical recovers the classical variety. This is the prototype of the recurring lesson that "$+$ of ideals is the scheme-theoretic operation; $\sqrt{+}$ is the variety-theoretic one".

**A non-radical sum ideal is the algebra detecting tangency and intersection multiplicity.** The counterexample is not a pathology but the first glimpse of a deep idea: the nilpotent in $k[T]/(T_1^2, T_2)$ measures that the parabola and line meet *to second order*, an intersection multiplicity of $2$. The radical erases this, collapsing the "fat point" to a reduced point. The diagnostic to carry: when $I(X) + I(Y)$ is non-radical, the varieties are tangent or otherwise non-transverse along their intersection, and the non-radical part *counts the contact*. This is exactly the data that **scheme theory** preserves (by *not* taking the radical) and that classical variety theory discards — Bézout's theorem, which counts intersection points *with multiplicity*, lives precisely in the non-radical sum. Recognising "non-radical sum = hidden multiplicity" connects this exercise to enumerative geometry.

**Push operations through $V$ and $I$, then patch with the strong Nullstellensatz.** The mechanical method for any identity relating geometric and algebraic operations is: write the geometric side, apply $V$ or $I$ to convert, use the *formal* properties of $V$ ($V(\mathfrak a + \mathfrak b) = V(\mathfrak a) \cap V(\mathfrak b)$, $V(\mathfrak a \cap \mathfrak b) = V(\mathfrak a) \cup V(\mathfrak b)$) which need no Nullstellensatz, and finally insert the radical wherever the round trip $I \circ V$ appears, via $I(V(\mathfrak b)) = \sqrt{\mathfrak b}$. The radical enters exactly at the $I \circ V$ steps and nowhere else. This recipe — formal properties for the easy direction, strong Nullstellensatz for the radical — derives every entry of the lattice dictionary and is the same method used in [[Ex - The radical as the intersection of maximal ideals containing it]]. The single fact to internalise: $V$'s properties are free, but $I \circ V = \sqrt{\cdot}$ costs a radical.
