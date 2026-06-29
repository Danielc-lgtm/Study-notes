---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Classification of Four-Vectors"
  - "Def - Minkowski Space and the Metric"
  - "Thm - Two Lemmas on Causal Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

In Euclidean space the Cauchy-Schwarz inequality reads $|\mathbf{u}\cdot\mathbf{v}| \leq |\mathbf{u}||\mathbf{v}|$. In Minkowski space the inequality *reverses* for timelike vectors.

1. Let $U, V$ be timelike four-vectors. Prove the **reversed Cauchy-Schwarz inequality**
$$
(U\cdot V)^2 \;\geq\; (U\cdot U)(V\cdot V) \qquad\Longleftrightarrow\qquad |U\cdot V| \;\geq\; \|U\|\,\|V\|,
$$
with equality if and only if $U$ and $V$ are collinear (parallel).
2. Deduce, for *future-directed* timelike $U, V$, the **reversed triangle inequality**
$$
\|U + V\| \;\geq\; \|U\| + \|V\|,
$$
again with equality iff collinear. (This is the geometric content of the [[Thm - The Reversed Triangle Inequality|twin paradox]]: the straight worldline is longest in proper time.)
3. Explain conceptually *why* the inequality reverses — which Euclidean step fails, and what the indefinite signature does to it.

**Recall:**

![[Def - Classification of Four-Vectors#The Definition]]

A vector is [[Def - Classification of Four-Vectors|timelike]] if $X\cdot X > 0$; its norm is $\|X\| = \sqrt{X\cdot X}$. For future-directed timelike $U, V$, [[Thm - Two Lemmas on Causal Vectors|Lemma 1]] gives $U\cdot V > 0$ (same sheet). The technique is operation 1: align $e_0$ with one of the vectors, reducing the problem to the Euclidean spatial part.

---

# Convergent Strategy

**Problem class.** A *reversed inequality of indefinite-metric geometry* — the chapter's signature kind of result, where a familiar Euclidean inequality runs backwards. The [[Special Relativity III — Minkowski Spacetime and the Metric#Problem-Solving Strategy|topic strategy]] says: mimic the Euclidean proof and watch the minus sign flip the conclusion.

**Assumption pattern.** $U, V$ timelike (part 1), future-directed (part 2). Timelikeness lets one of them be the time axis; future-directedness gives $U\cdot V > 0$ via [[Thm - Two Lemmas on Causal Vectors|Lemma 1]], which is what removes the absolute value and lets the triangle inequality follow. The signpost is "two timelike vectors and an inequality" — reach for the adapted basis.

**Theorem routing.** Operation 1: set $e_0 = U/\|U\|$. Then $U\cdot U, U\cdot V, V\cdot V$ become expressions in $V$'s components, and the inequality reduces to the *ordinary* Cauchy-Schwarz inequality on the spatial part $\mathbf{V}$ — but contributing with the *opposite* sign, which flips $\leq$ to $\geq$. Part 2 follows by squaring $\|U+V\|$ and inserting part 1; [[Thm - Two Lemmas on Causal Vectors|Lemma 1]] supplies $U\cdot V > 0$.

**Key decision point.** The crux is that, in the rest frame of $U$, the cross term $U\cdot V$ involves only $V^0$ while the Euclidean Cauchy-Schwarz inequality bounds the *spatial* overlap — and because the spatial part enters the Minkowski norm with a *minus* sign, the Euclidean bound appears on the "wrong side", reversing the inequality. The natural error is to expect $\leq$ by analogy; the indefinite signature is exactly what inverts it.

---

# Legal Operations Used

1. **Operation 1 (choose an adapted orthonormal basis):** set $e_0 = U/\|U\|$, reducing both vectors to components with $U$ purely temporal.

2. **Operation 2 (compute the scalar product by the Minkowski matrix):** all three products $U\cdot U$, $U\cdot V$, $V\cdot V$ in the adapted basis.

3. **Operation 6 (use the two lemmas on causal vectors):** [[Thm - Two Lemmas on Causal Vectors|Lemma 1]] gives $U\cdot V > 0$ for future timelike $U, V$, needed to drop the absolute value in part 2.

4. **Operation 8 (polarise):** part 2 expands $\|U+V\|^2 = U\cdot U + 2U\cdot V + V\cdot V$, the quadratic-form route to the triangle inequality.

---

# Hints

> [!note]- Hint 1
> Choose $e_0 = U/\|U\|$, so $U = (\|U\|, \mathbf{0})$ in the adapted basis. Write $V = (V^0, \mathbf{V})$. Then $U\cdot U = \|U\|^2$, $U\cdot V = \|U\|V^0$, $V\cdot V = (V^0)^2 - |\mathbf{V}|^2$.

> [!note]- Hint 2
> The inequality $(U\cdot V)^2 \geq (U\cdot U)(V\cdot V)$ becomes $\|U\|^2(V^0)^2 \geq \|U\|^2[(V^0)^2 - |\mathbf{V}|^2]$, i.e. $(V^0)^2 \geq (V^0)^2 - |\mathbf{V}|^2$, i.e. $|\mathbf{V}|^2 \geq 0$ — always true! Equality iff $\mathbf{V} = 0$, i.e. $V \parallel e_0 \parallel U$.

> [!note]- Hint 3
> For the triangle inequality, square: $\|U+V\|^2 = (U+V)\cdot(U+V) = U\cdot U + 2U\cdot V + V\cdot V = \|U\|^2 + \|V\|^2 + 2U\cdot V$. By [[Thm - Two Lemmas on Causal Vectors|Lemma 1]], $U\cdot V > 0$, and by part 1, $U\cdot V \geq \|U\|\|V\|$. So $\|U+V\|^2 \geq \|U\|^2 + \|V\|^2 + 2\|U\|\|V\| = (\|U\| + \|V\|)^2$. Take square roots.

> [!note]- Hint 4
> For part 3: in the Euclidean proof, the spatial overlap $|\mathbf{V}|^2$ contributes with a $+$ sign to $V\cdot V$, giving $\leq$. In Minkowski space $V\cdot V = (V^0)^2 - |\mathbf{V}|^2$, so $|\mathbf{V}|^2$ enters with a $-$ sign and *subtracts* from $V\cdot V$, which is exactly what pushes $(U\cdot V)^2$ *above* $(U\cdot U)(V\cdot V)$ — the reversal.

---

# Solution

Aligning $e_0$ with $U$ reduces the inequality to the trivial $|\mathbf{V}|^2 \geq 0$, but with the spatial term entering the norm with a minus sign, which flips $\leq$ to $\geq$. Step 1 sets up the adapted basis and proves part 1; Step 2 derives the triangle inequality using Lemma 1; Step 3 isolates the reversal mechanism.

**Step 1: the reversed Cauchy-Schwarz inequality.**

> [!note]- Derivation
> Since $U$ is timelike, set $e_0 = U/\|U\|$ and complete to an orthonormal basis, so $U = (\|U\|, 0, 0, 0)$. Write $V = (V^0, \mathbf{V})$ with $\mathbf{V} = (V^1,V^2,V^3)$. Then, by the [[Def - Minkowski Space and the Metric|Minkowski matrix]],
> $$U\cdot U = \|U\|^2, \qquad U\cdot V = \|U\|\,V^0, \qquad V\cdot V = (V^0)^2 - |\mathbf{V}|^2.$$
> Substitute into the claimed inequality $(U\cdot V)^2 \geq (U\cdot U)(V\cdot V)$:
> $$\|U\|^2 (V^0)^2 \;\geq\; \|U\|^2\big[(V^0)^2 - |\mathbf{V}|^2\big].$$
> Divide by $\|U\|^2 > 0$:
> $$(V^0)^2 \;\geq\; (V^0)^2 - |\mathbf{V}|^2 \quad\Longleftrightarrow\quad |\mathbf{V}|^2 \;\geq\; 0,$$
> which holds always. So $(U\cdot V)^2 \geq (U\cdot U)(V\cdot V)$. Since $V$ is timelike, $V\cdot V > 0$, and both sides are non-negative ($U\cdot U > 0$ too), so taking square roots gives $|U\cdot V| \geq \|U\|\,\|V\|$. **Equality** holds iff $|\mathbf{V}|^2 = 0$, i.e. $\mathbf{V} = 0$, i.e. $V = (V^0,\mathbf{0}) = (V^0/\|U\|)\,U$ — exactly when $V$ is collinear with $U$.

**Step 2: the reversed triangle inequality.**

> [!note]- Derivation
> Let $U, V$ be *future-directed* timelike. Expand (operation 8, polarisation):
> $$\|U+V\|^2 = (U+V)\cdot(U+V) = U\cdot U + 2\,U\cdot V + V\cdot V = \|U\|^2 + \|V\|^2 + 2\,U\cdot V.$$
> (First, $U+V$ is timelike by the [[Thm - Two Lemmas on Causal Vectors|convexity corollary]], so $\|U+V\|$ is defined.) By [[Thm - Two Lemmas on Causal Vectors|Lemma 1]], future timelike $U, V$ have $U\cdot V > 0$, so $|U\cdot V| = U\cdot V$, and part 1 gives $U\cdot V \geq \|U\|\,\|V\|$. Therefore
> $$\|U+V\|^2 \geq \|U\|^2 + \|V\|^2 + 2\|U\|\,\|V\| = \big(\|U\| + \|V\|\big)^2.$$
> Both sides non-negative, so $\|U+V\| \geq \|U\| + \|V\|$. Equality holds iff $U\cdot V = \|U\|\|V\|$, i.e. iff $U \parallel V$. This is the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]]: read along worldlines, the straight (inertial) path $U+V$ has *more* proper time than the bent path of legs $U$ then $V$ — the twin who travels (a bent worldline) ages less.

**Step 3: why the inequality reverses.**

> [!note]- Derivation
> Compare the two proofs term by term. The Euclidean Cauchy-Schwarz inequality, proved by considering $(U + tV)\cdot(U+tV) \geq 0$ and the discriminant, ultimately rests on the *positive-definiteness* of the form, which makes the spatial overlap $|\mathbf{V}|^2$ contribute with a $+$ sign and gives $\leq$. In Minkowski space the very same computation runs, but the spatial part of the scalar square enters with a *minus* sign: $V\cdot V = (V^0)^2 - |\mathbf{V}|^2$. So when we compare $(U\cdot V)^2 = \|U\|^2(V^0)^2$ with $(U\cdot U)(V\cdot V) = \|U\|^2[(V^0)^2 - |\mathbf{V}|^2]$, the spatial term $|\mathbf{V}|^2$ has been *subtracted* from the right-hand side, making it *smaller* — so the inequality points the other way, $\geq$ rather than $\leq$. The one sign in the signature is the whole reversal. Equivalently: in the rest frame of $U$, the orthogonal complement $U^\perp$ is [[Ex - A vector orthogonal to a timelike vector is spacelike|spacelike]] (the metric there is *negative* definite), so the "spatial spread" of $V$ counts *against* its Minkowski norm instead of for it. The Euclidean inequality holds, unreversed, on the spacelike complement; it is the one timelike direction, sitting outside that complement with the opposite sign, that flips the global statement.

> [!note]- Complete formal solution
> Set $e_0 = U/\|U\|$, so $U = (\|U\|,\mathbf{0})$, $V = (V^0,\mathbf{V})$. Then $U\cdot U = \|U\|^2$, $U\cdot V = \|U\|V^0$, $V\cdot V = (V^0)^2 - |\mathbf{V}|^2$, and $(U\cdot V)^2 - (U\cdot U)(V\cdot V) = \|U\|^2|\mathbf{V}|^2 \geq 0$, giving $(U\cdot V)^2 \geq (U\cdot U)(V\cdot V)$, hence $|U\cdot V| \geq \|U\|\|V\|$, with equality iff $\mathbf{V} = 0$ iff $V \parallel U$. For future timelike $U, V$: $\|U+V\|^2 = \|U\|^2 + \|V\|^2 + 2U\cdot V$, and Lemma 1 gives $U\cdot V > 0$ while part 1 gives $U\cdot V \geq \|U\|\|V\|$, so $\|U+V\|^2 \geq (\|U\|+\|V\|)^2$ and $\|U+V\| \geq \|U\|+\|V\|$, equality iff collinear. The reversal arises because the spatial overlap $|\mathbf{V}|^2$ enters $V\cdot V$ with a minus sign (indefinite signature), subtracting from the right-hand side and flipping the Euclidean $\leq$ to $\geq$; equivalently, the Euclidean inequality holds unreversed on the spacelike complement $U^\perp$ and is inverted by the one timelike direction. $\blacksquare$

---

# Key Takeaways

**Reversed inequalities are the chapter's signature, and the reversal is always one minus sign in the signature.** The reversed Cauchy-Schwarz and triangle inequalities look paradoxical — the inner product *exceeds* the product of norms, the "straight line" is *longest* — but the cause is mechanical: the spatial part of the Minkowski scalar square enters with a minus sign, so the term that, in Euclidean geometry, makes the inequality go one way, here makes it go the other. The trigger to recognise a reversed inequality: two timelike vectors and a familiar Euclidean inequality. The technique is always the same — align $e_0$ with one of them (operation 1), reducing the statement to an ordinary Euclidean inequality on the spatial part, then track that the spatial term carries the opposite sign. This is the unifying view of the [[Thm - Two Lemmas on Causal Vectors|causal lemmas]], the reversed Cauchy-Schwarz, and the reversed triangle inequality: one computation, one sign, three theorems.

**The reversed triangle inequality is the twin paradox, and it says the inertial worldline maximises proper time.** Part 2 is the deepest single fact in Minkowski geometry: between two timelike-separated events, the straight (inertial) worldline has the *greatest* proper time, and any bending — any acceleration — strictly reduces it. The minus signs flip "shortest" (Euclidean) to "longest" (Minkowski). Read physically, a clock that wanders through space banks less proper time than one that sits still, because spatial motion subtracts from the interval; this is the [[Thm - The Reversed Triangle Inequality|twin paradox]], where the travelling twin (bent worldline) ages less. The reusable principle: to compare the ageing of observers on different worldlines between the same two events, do not do time-dilation bookkeeping — just compare how bent the worldlines are, since the straightest ages the most. This is the special-relativistic seed of the geodesic principle of general relativity, where freely-falling worldlines extremise proper time.

**Euclidean reasoning returns on the spacelike complement, and that is the master reconciliation.** The cleanest way to understand the reversal is that the Euclidean Cauchy-Schwarz inequality holds, *unreversed*, on the spacelike orthogonal complement $U^\perp$ of a timelike vector — where the metric is negative definite, so $-g$ is a genuine Euclidean inner product ([[Ex - A vector orthogonal to a timelike vector is spacelike|orthogonal-to-timelike-is-spacelike]]). The reversal of the *global* inequality is entirely due to the one timelike direction, which sits outside that complement and contributes with the opposite sign. The transferable diagnostic: whenever an indefinite-metric statement seems to invert a Euclidean one, locate the timelike direction responsible and split it off; on the remaining spacelike subspace the Euclidean intuition is exactly correct. This is the same reconciliation that makes an [[Def - Observer and Local Rest Space|observer's rest space]] ordinary Euclidean three-space, and it is the general lesson of the chapter: indefiniteness is not chaos, it is Euclidean geometry plus one direction of opposite sign.
