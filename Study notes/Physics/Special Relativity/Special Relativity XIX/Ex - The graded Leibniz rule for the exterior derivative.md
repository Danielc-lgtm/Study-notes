---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Exterior Derivative"
  - "Def - Alternate Forms and the Exterior Product"
tags: [physics, special-relativity]
---

# Problem Statement

Prove the graded Leibniz rule for the exterior derivative: for a differential $p$-form $A$ and any differential form $B$,
$$\mathbf{d}(A\wedge B) = \mathbf{d}A\wedge B + (-1)^{p}\,A\wedge\mathbf{d}B.$$

1. Prove it first for the case $A = f$ a $0$-form (so $p = 0$), recovering $\mathbf{d}(fB) = \mathbf{d}f\wedge B + f\,\mathbf{d}B$.
2. Prove the general case by expanding $A$ and $B$ in a coordinate basis and applying the ordinary product rule, tracking the sign carefully.
3. Explain precisely where the sign $(-1)^p$ comes from, and verify that $\mathbf{d}$ is a *derivation* of the exterior algebra (a derivation only when $p$ is even, in the ungraded sense).

**Recall:**

![[Def - The Exterior Derivative#The Definition]]

The wedge product is graded-anticommutative: $\alpha\wedge\beta = (-1)^{pq}\beta\wedge\alpha$ for a $p$-form $\alpha$ and $q$-form $\beta$ (see [[Def - Alternate Forms and the Exterior Product]]). In a coordinate basis $e^\alpha = \mathbf{d}x^\alpha$ and $\mathbf{d}(\mathbf{d}x^\alpha) = 0$.

---

# Convergent Strategy

**Problem class.** A *prove-a-derivation-property* problem (operation 8 from the topic page is the application; this exercise establishes it). The route is the ordinary product rule on components, with the wedge anticommutativity supplying the sign.

**Assumption pattern.** Forms expanded as $A = A_I\,\mathbf{d}x^I$ (multi-index notation) with $\mathbf{d}x^I = \mathbf{d}x^{\alpha_1}\wedge\cdots\wedge\mathbf{d}x^{\alpha_p}$; the key facts are that $\mathbf{d}$ of a coordinate differential is zero and that the wedge of a $1$-form past a $p$-form costs $(-1)^p$.

**Theorem routing.** Part 1 is the scalar-times-form product rule. Part 2 is the general expansion. Part 3 isolates the sign.

**Key decision point.** The crux is the sign bookkeeping: when $\mathbf{d}$ "hits" the $B$ factor, the new differential $\mathbf{d}x^\gamma$ it produces must be moved from the front past the $p$ wedge factors $\mathbf{d}x^{\alpha_1}\cdots\mathbf{d}x^{\alpha_p}$ of $A$ to sit with $B$, and each of the $p$ transpositions costs a factor $-1$, giving $(-1)^p$. Getting this sign right is the entire content.

---

# Legal Operations Used

1. **Apply the graded Leibniz rule to a wedge product** (operation 8 from the topic page) — here we *prove* the rule.
2. **Antisymmetrise to get the exterior derivative, then drop the Christoffels** (operation 6 from the topic page). Use the partial-derivative form of $\mathbf{d}$.

---

# Hints

> [!note]- Hint 1
> For $A = f$ a scalar, $fB$ has components $f B_I$, and $\mathbf{d}(fB)$ antisymmetrises $\partial_\gamma(f B_I) = (\partial_\gamma f)B_I + f\partial_\gamma B_I$. The first piece is $\mathbf{d}f\wedge B$, the second $f\,\mathbf{d}B$ — no sign issue because $p = 0$.

> [!note]- Hint 2
> Write $A = A_I\,\mathbf{d}x^I$, $B = B_J\,\mathbf{d}x^J$ with $\mathbf{d}x^I = \mathbf{d}x^{\alpha_1}\wedge\cdots\wedge\mathbf{d}x^{\alpha_p}$. Then $A\wedge B = A_I B_J\,\mathbf{d}x^I\wedge\mathbf{d}x^J$, and since $\mathbf{d}(\mathbf{d}x^I\wedge\mathbf{d}x^J) = 0$ (each factor is closed), $\mathbf{d}(A\wedge B) = \mathbf{d}(A_I B_J)\wedge\mathbf{d}x^I\wedge\mathbf{d}x^J$.

> [!note]- Hint 3
> $\mathbf{d}(A_I B_J) = (\mathbf{d}A_I)B_J + A_I\,\mathbf{d}B_J$ (scalar product rule). The first term reassembles $\mathbf{d}A\wedge B$. For the second, $A_I(\mathbf{d}B_J)\wedge\mathbf{d}x^I\wedge\mathbf{d}x^J$: move the $1$-form $\mathbf{d}B_J$ rightward past $\mathbf{d}x^I$ (which has $p$ factors).

> [!note]- Hint 4
> Moving a $1$-form past a $p$-form: $\mathbf{d}B_J\wedge\mathbf{d}x^I = (-1)^p\,\mathbf{d}x^I\wedge\mathbf{d}B_J$ by graded anticommutativity (one transposition per factor, $p$ factors). This produces the $(-1)^p$.

---

# Solution

The plan: Step 1 handles the scalar case (no sign). Step 2 expands general forms, uses that coordinate differentials are closed so $\mathbf{d}$ only hits the coefficient functions, and applies the scalar product rule. Step 3 extracts the sign by moving the new differential past the $p$ factors of $A$.

**Step 1: The scalar case.**

> [!note]- Derivation
> Let $A = f$ be a $0$-form ($p = 0$) and $B$ a $q$-form with components $B_J$. The product $fB$ has components $fB_J$, and
> $$\mathbf{d}(fB) = \mathbf{d}(fB_J)\wedge\mathbf{d}x^J = \big[(\partial_\gamma f)B_J + f(\partial_\gamma B_J)\big]\mathbf{d}x^\gamma\wedge\mathbf{d}x^J,$$
> using the ordinary product rule on the scalar $fB_J$ and the fact that $\mathbf{d}(\mathbf{d}x^J) = 0$. The first piece is $(\partial_\gamma f)\mathbf{d}x^\gamma\wedge B_J\mathbf{d}x^J = \mathbf{d}f\wedge B$; the second is $f(\partial_\gamma B_J)\mathbf{d}x^\gamma\wedge\mathbf{d}x^J = f\,\mathbf{d}B$. Hence
> $$\mathbf{d}(fB) = \mathbf{d}f\wedge B + f\,\mathbf{d}B,$$
> which is the rule with $(-1)^p = (-1)^0 = +1$.

**Step 2: The general expansion.**

> [!note]- Derivation
> Expand $A = A_I\,\mathbf{d}x^I$ and $B = B_J\,\mathbf{d}x^J$, where $I = (\alpha_1<\cdots<\alpha_p)$, $J = (\beta_1<\cdots<\beta_q)$ are increasing multi-indices and $\mathbf{d}x^I = \mathbf{d}x^{\alpha_1}\wedge\cdots\wedge\mathbf{d}x^{\alpha_p}$. Then $A\wedge B = A_I B_J\,\mathbf{d}x^I\wedge\mathbf{d}x^J$, a sum of coefficient-functions times wedges of coordinate differentials. Since every coordinate differential is closed, $\mathbf{d}(\mathbf{d}x^I\wedge\mathbf{d}x^J) = 0$, and the exterior derivative acts only on the coefficient function $A_I B_J$:
> $$\mathbf{d}(A\wedge B) = \mathbf{d}(A_I B_J)\wedge\mathbf{d}x^I\wedge\mathbf{d}x^J = \big[(\mathbf{d}A_I)B_J + A_I(\mathbf{d}B_J)\big]\wedge\mathbf{d}x^I\wedge\mathbf{d}x^J,$$
> by the ordinary product rule on the scalars $A_I, B_J$ (here $\mathbf{d}A_I = \partial_\gamma A_I\,\mathbf{d}x^\gamma$ is a $1$-form).

**Step 3: Extracting the sign.**

> [!note]- Derivation
> The first term assembles directly: $(\mathbf{d}A_I)\wedge\mathbf{d}x^I\wedge B_J\mathbf{d}x^J = (\mathbf{d}A)\wedge B$, since $(\mathbf{d}A_I)\wedge\mathbf{d}x^I = \mathbf{d}(A_I\mathbf{d}x^I) = \mathbf{d}A$ (each $\mathbf{d}x^I$ closed).
>
> The second term needs the sign. We have $A_I(\mathbf{d}B_J)\wedge\mathbf{d}x^I\wedge\mathbf{d}x^J$, but to recognise $A\wedge\mathbf{d}B$ we want $A_I\,\mathbf{d}x^I\wedge(\mathbf{d}B_J)\wedge\mathbf{d}x^J$. The $1$-form $\mathbf{d}B_J$ currently sits to the *left* of the $p$-fold wedge $\mathbf{d}x^I$; moving it to the *right* of $\mathbf{d}x^I$ requires commuting a $1$-form past a $p$-form. By graded anticommutativity, $\mathbf{d}B_J\wedge\mathbf{d}x^I = (-1)^{1\cdot p}\,\mathbf{d}x^I\wedge\mathbf{d}B_J = (-1)^p\,\mathbf{d}x^I\wedge\mathbf{d}B_J$ (one sign per transposition, $p$ transpositions). Hence
> $$A_I(\mathbf{d}B_J)\wedge\mathbf{d}x^I\wedge\mathbf{d}x^J = (-1)^p A_I\,\mathbf{d}x^I\wedge(\mathbf{d}B_J)\wedge\mathbf{d}x^J = (-1)^p A\wedge\mathbf{d}B.$$
> Combining the two terms,
> $$\boxed{\;\mathbf{d}(A\wedge B) = \mathbf{d}A\wedge B + (-1)^p A\wedge\mathbf{d}B.\;}$$
> The sign $(-1)^p$ is exactly the cost of sliding the new differential $\mathbf{d}B_J$ (degree $1$) past the $p$ factors of $A$ — a single transposition for each factor. So $\mathbf{d}$ is a **graded derivation** of degree $+1$ on the exterior algebra: it satisfies the product rule with the grading sign. (It is an ordinary, ungraded derivation only when $p$ is even, where the sign is $+1$.)

> [!note]- Complete formal solution
> Write $A = A_I\mathbf{d}x^I$ ($p$-form), $B = B_J\mathbf{d}x^J$. Since coordinate differentials are closed, $\mathbf{d}(A\wedge B) = \mathbf{d}(A_I B_J)\wedge\mathbf{d}x^I\wedge\mathbf{d}x^J = [(\mathbf{d}A_I)B_J + A_I\mathbf{d}B_J]\wedge\mathbf{d}x^I\wedge\mathbf{d}x^J$. The first term is $\mathbf{d}A\wedge B$. In the second, moving the $1$-form $\mathbf{d}B_J$ past the $p$-fold $\mathbf{d}x^I$ costs $(-1)^p$ by graded anticommutativity, giving $(-1)^p A\wedge\mathbf{d}B$. Hence $\mathbf{d}(A\wedge B) = \mathbf{d}A\wedge B + (-1)^p A\wedge\mathbf{d}B$. The case $p=0$ gives $\mathbf{d}(fB) = \mathbf{d}f\wedge B + f\mathbf{d}B$. The sign is the transposition cost of the degree-$1$ operator $\mathbf{d}$ past the $p$ factors of $A$, making $\mathbf{d}$ a graded derivation of degree $+1$. $\blacksquare$

---

# Key Takeaways

**The sign $(-1)^p$ is the cost of sliding the degree-$1$ operator $\mathbf{d}$ past the $p$ factors of $A$ — it is anticommutativity bookkeeping, not a convention.** The graded Leibniz rule looks like an arbitrary decoration of the ordinary product rule, but the sign has a precise and memorable origin: when the exterior derivative acts on the second factor $B$, it produces a new one-form differential that must commute past the $p$ wedge factors of the first factor $A$ to reach its place, and each transposition of adjacent wedge factors costs $-1$. With $p$ factors to pass, the total cost is $(-1)^p$. This is the same mechanism that gives every "graded" sign in differential geometry and in the algebra of fermionic operators: a degree-$1$ object moving past a degree-$p$ object picks up $(-1)^p$. Once you see the sign as a transposition count, you never have to memorise it, and you can extend it to graded commutators and to the signs in the formulas for the Lie derivative and the interior product.

**$\mathbf{d}$ is a graded derivation, which is what makes the exterior calculus an algebra with a calculus on it.** The Leibniz rule is precisely the statement that $\mathbf{d}$ differentiates products — it is the property that elevates $\mathbf{d}$ from a mere linear map to a *derivation* of the exterior algebra, the algebraic structure that lets you compute the exterior derivative of any wedge by differentiating the factors one at a time. Together with $\mathbf{d}^2 = 0$ and the rule that $\mathbf{d}f$ is the gradient, the graded Leibniz rule *characterises* the exterior derivative uniquely, so these three properties are the axioms one would use to define $\mathbf{d}$ abstractly on any manifold. The practical importance is that whenever a Lagrangian or a current is built by wedging forms — $A\wedge\mathbf{d}A$ in Chern–Simons theory, $F\wedge\star F$ in the Maxwell action — its exterior derivative is computed by this rule, and the sign is what determines whether the object is closed.

**The Leibniz rule is the engine behind the existence of conserved currents and topological terms.** A recurring move in field theory is to show that some wedge product of forms is closed, hence (on a contractible region) exact, hence integrable to a conserved or topological quantity — and the Leibniz rule is what lets you compute its exterior derivative. For instance, $\mathbf{d}(A\wedge\mathbf{d}A) = \mathbf{d}A\wedge\mathbf{d}A + (-1)^1 A\wedge\mathbf{d}\mathbf{d}A = \mathbf{d}A\wedge\mathbf{d}A$ (the second term dies by $\mathbf{d}^2 = 0$), revealing the Chern–Simons structure; and $\mathbf{d}(F\wedge\star F)$ governs the energy flux of the electromagnetic field. The transferable diagnostic is that any time you must differentiate a product of forms — to check closedness, to integrate by parts, to derive a conservation law — the graded Leibniz rule is the tool, and the $(-1)^p$ sign is the one thing you must not drop.
