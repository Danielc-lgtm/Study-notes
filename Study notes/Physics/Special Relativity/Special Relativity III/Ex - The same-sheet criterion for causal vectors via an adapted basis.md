---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Two Lemmas on Causal Vectors"
  - "Def - The Null Cone and the Time Arrow"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

This exercise re-derives Gourgoulhon's two lemmas (§1.4.2) in our mostly-minus convention and applies them.

1. Let $U, V$ be timelike four-vectors. By choosing an orthonormal basis with $e_0$ along $U$, prove that $U$ and $V$ lie in the same sheet of the [[Def - The Null Cone and the Time Arrow|null cone]] if and only if $U\cdot V > 0$.
2. Let $U, V$ be null and non-collinear. By writing $U = u^0(e_0 + e_1)$ and $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$, prove the same criterion $U\cdot V > 0$, and identify where the non-collinearity hypothesis is used.
3. Apply the criterion: given two future-directed four-velocities $U, V$ (so $U\cdot U = V\cdot V = 1$), show $U\cdot V \geq 1$, with equality iff $U = V$, and interpret $U\cdot V$ as the relative Lorentz factor $\gamma_{\text{rel}}$.

**Recall:**

![[Thm - Two Lemmas on Causal Vectors#Statement]]

A four-velocity is a future-directed unit timelike vector, $U\cdot U = 1$. The technique is operation 1: align the orthonormal basis with one of the vectors so the scalar product collapses. Same sheet means both future-directed or both past-directed.

---

# Convergent Strategy

**Problem class.** A *re-derivation and application* of the [[Thm - Two Lemmas on Causal Vectors|causal-vector lemmas]] — practising the adapted-basis technique that is the chapter's master move, then deploying the criterion to a physical question.

**Assumption pattern.** Parts 1 and 2 give two causal vectors and ask for the same-sheet criterion; the signpost is "causal vectors, decide same time-orientation". Part 3 gives two four-velocities (future timelike, unit), so Lemma 1 applies and $U\cdot V$ has a physical meaning.

**Theorem routing.** Operation 1 (adapted basis) reduces each lemma to reading off a single component or a single $1 - \cos\varphi$ factor. Part 3 specialises Lemma 1: with $U\cdot U = V\cdot V = 1$, the reversed Cauchy-Schwarz inequality ([[Ex - The reversed Cauchy-Schwarz inequality for timelike vectors|reversed CS]]) gives $U\cdot V \geq 1$, and the rest-frame computation identifies $U\cdot V = \gamma_{\text{rel}}$.

**Key decision point.** The crux is the *choice of adapted basis*: for timelike $U$, take $e_0 \parallel U$; for null $U$, take $U \parallel e_0 + e_1$ and put $V$ in the $e_0 e_1 e_2$ block. The non-collinearity in part 2 is the decision that keeps $\varphi \neq 0$, hence $1 - \cos\varphi > 0$; dropping it would allow $U\cdot V = 0$ for same-sheet null vectors.

---

# Legal Operations Used

1. **Operation 1 (choose an adapted orthonormal basis):** the whole method — $e_0 \parallel U$ (timelike) or $U \parallel e_0 + e_1$ (null).

2. **Operation 2 (compute the scalar product by the Minkowski matrix):** $U\cdot V = \|U\|V^0$ (Lemma 1) and $u^0v^0(1 - \cos\varphi)$ (Lemma 2).

3. **Operation 6 (use the two lemmas on causal vectors):** part 3 applies Lemma 1 to four-velocities.

4. **Operation 3 (classify by the sign of the scalar square):** the normalisation $U\cdot U = 1$ marks $U$ as future timelike.

---

# Hints

> [!note]- Hint 1
> Lemma 1: with $e_0 = U/\|U\|$, $U = \|U\|e_0$ and $V = V^0 e_0 + V^i e_i$. Then $U\cdot V = \|U\|V^0$ (only $e_0\cdot e_0 = +1$ survives). Same sheet as $U$ (future) means $V^0 > 0$, equivalent to $U\cdot V > 0$.

> [!note]- Hint 2
> Lemma 2: with $U = u^0(e_0 + e_1)$ and $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$, compute $U\cdot V = u^0v^0[(e_0\cdot e_0) + \cos\varphi(e_1\cdot e_1)] = u^0v^0(1 - \cos\varphi)$. Non-collinearity gives $\varphi \neq 0$, so $1 - \cos\varphi > 0$, and $\mathrm{sign}(U\cdot V) = \mathrm{sign}(u^0v^0)$.

> [!note]- Hint 3
> Part 3: for four-velocities, in the rest frame of $U$ we have $U = (1,\mathbf{0})$ and $V = (\gamma, \gamma\mathbf{v})$ with $\gamma = (1-|\mathbf{v}|^2)^{-1/2}$. Then $U\cdot V = \gamma \geq 1$, equality iff $\mathbf{v} = 0$ iff $V = U$. The number $U\cdot V = \gamma_{\text{rel}}$ is the Lorentz factor of $V$ relative to $U$.

---

# Solution

Each lemma is one adapted-basis computation; the application reads $U\cdot V$ as the relative Lorentz factor. Step 1 proves Lemma 1; Step 2 proves Lemma 2 and flags non-collinearity; Step 3 applies the criterion to four-velocities.

**Step 1: same-sheet criterion for timelike vectors.**

> [!note]- Derivation
> $U$ timelike, so $e_0 := U/\|U\|$ is a unit timelike vector; complete to an orthonormal basis with $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$, $e_0\cdot e_i = 0$. Then $U = \|U\|e_0$. Expand $V = V^0 e_0 + V^i e_i$:
> $$U\cdot V = \|U\|\big(V^0(e_0\cdot e_0) + V^i(e_0\cdot e_i)\big) = \|U\|\,V^0.$$
> Taking $e_0 \parallel U$ future-directed, $V$ is in the same (future) sheet iff $V^0 > 0$. Since $\|U\| > 0$, this is iff $U\cdot V > 0$. $\blacksquare$ (This is [[Thm - Two Lemmas on Causal Vectors|Lemma 1]].)

**Step 2: same-sheet criterion for null vectors.**

> [!note]- Derivation
> A null vector is $x^0(e_0 + \hat{\mathbf{n}})$ with $\hat{\mathbf{n}}$ a unit spatial vector. Align the basis so $U = u^0(e_0 + e_1)$; rotate the spatial axes so $V$'s direction lies in the $e_1 e_2$ plane, $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$. Compute, using $e_0\cdot e_0 = +1$, $e_1\cdot e_1 = -1$, cross terms zero:
> $$U\cdot V = u^0 v^0\big[(e_0\cdot e_0) + \cos\varphi(e_1\cdot e_1)\big] = u^0 v^0(1 - \cos\varphi).$$
> **Non-collinearity** of $U, V$ forces $\varphi \neq 0$, so $\cos\varphi < 1$ and $1 - \cos\varphi > 0$. Hence $\mathrm{sign}(U\cdot V) = \mathrm{sign}(u^0 v^0)$, and $U, V$ share a sheet iff $u^0 v^0 > 0$, i.e. iff $U\cdot V > 0$. $\blacksquare$ Were $U, V$ collinear ($\varphi = 0$), we would have $1 - \cos\varphi = 0$ and $U\cdot V = 0$ even though they share a sheet — which is exactly the degenerate parallel-null case excluded by the hypothesis. (This is [[Thm - Two Lemmas on Causal Vectors|Lemma 2]].)

**Step 3: the relative Lorentz factor.**

> [!note]- Derivation
> Let $U, V$ be future-directed four-velocities, $U\cdot U = V\cdot V = 1$. Work in the rest frame of $U$: $U = (1,\mathbf{0})$, and $V = (\gamma, \gamma\mathbf{v})$ where $\mathbf{v}$ is $V$'s spatial velocity in this frame and $\gamma = (1 - |\mathbf{v}|^2)^{-1/2}$ (so that $V\cdot V = \gamma^2 - \gamma^2|\mathbf{v}|^2 = \gamma^2(1 - |\mathbf{v}|^2) = 1$, consistent). Then
> $$U\cdot V = (1)(\gamma) - \mathbf{0}\cdot(\gamma\mathbf{v}) = \gamma = \big(1 - |\mathbf{v}|^2\big)^{-1/2} \geq 1,$$
> with equality iff $\mathbf{v} = 0$, i.e. $V = U$. By [[Thm - Two Lemmas on Causal Vectors|Lemma 1]] (or directly) $U\cdot V > 0$, confirming $U, V$ are in the same future sheet. The invariant $U\cdot V = \gamma_{\text{rel}}$ is the **relative Lorentz factor** — the $\gamma$ of the motion of one particle as seen in the rest frame of the other — and since it is a scalar product of four-vectors it is frame-independent: computed in any frame, $U\cdot V$ gives the same $\gamma_{\text{rel}}$. The relative speed is then $v_{\text{rel}} = \sqrt{1 - (U\cdot V)^{-2}} < 1$: two massive particles always move slower than light relative to each other.

> [!note]- Complete formal solution
> *Lemma 1:* with $e_0 = U/\|U\|$, $U = \|U\|e_0$ and $U\cdot V = \|U\|V^0$; same sheet iff $V^0 > 0$ iff $U\cdot V > 0$. *Lemma 2:* with $U = u^0(e_0 + e_1)$, $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$, $\varphi \neq 0$ by non-collinearity, $U\cdot V = u^0v^0(1 - \cos\varphi)$ and $1 - \cos\varphi > 0$, so same sheet iff $u^0v^0 > 0$ iff $U\cdot V > 0$; collinearity would give $U\cdot V = 0$, the excluded case. *Application:* for four-velocities, in $U$'s rest frame $U = (1,\mathbf{0})$, $V = (\gamma,\gamma\mathbf{v})$, so $U\cdot V = \gamma = (1-|\mathbf{v}|^2)^{-1/2} \geq 1$, equality iff $V = U$; $U\cdot V = \gamma_{\text{rel}}$ is the frame-independent relative Lorentz factor, giving $v_{\text{rel}} = \sqrt{1 - (U\cdot V)^{-2}} < 1$. $\blacksquare$

---

# Key Takeaways

**The adapted basis turns a global question about the null cone into a one-line sign, and that is the whole method of the lemmas.** Both same-sheet criteria are proved by the same move: align the orthonormal basis with one causal vector — $e_0 \parallel U$ for timelike, $U \parallel e_0 + e_1$ for null — so the scalar product collapses to a single readable quantity (a time component, or a $1 - \cos\varphi$ factor). The trigger is any question about whether two causal vectors agree in time-orientation, or any need to know that a sum of future-pointing vectors stays future-pointing. The reusable content is that "which sheet of the null cone?" — a seemingly global, geometric question — is answered by the sign of one invariant scalar product $U\cdot V$, computable in any frame. This is the chapter's recurring conversion of geometry into a single algebraic sign, and the proofs are two lines each precisely because the adapted basis does all the work.

**The relative Lorentz factor is a scalar product of four-velocities, and that makes "relative speed" frame-independent.** The application reveals that $U\cdot V$, for two four-velocities, *is* the relative Lorentz factor $\gamma_{\text{rel}}$ — the $\gamma$ of one particle in the other's rest frame — and because it is a scalar product it is the same in every frame. This is the prototype of the chapter's most powerful labour-saving move: a physically meaningful quantity (here, relative speed) is secretly an invariant scalar product, so it can be computed in whichever frame is convenient and trusted universally. The reflex to install: when two particles' four-velocities appear, reach for $U\cdot V$ — it is $\gamma_{\text{rel}} \geq 1$, automatically positive (same future sheet, by Lemma 1), and it immediately gives the relative speed $v_{\text{rel}} = \sqrt{1 - (U\cdot V)^{-2}} < 1$, the statement that massive particles never reach light speed relative to each other.

**The non-collinearity hypothesis in Lemma 2 is not pedantry — it excludes the genuine degenerate case where the criterion fails.** Lemma 2's requirement that the null vectors be non-collinear is load-bearing: two *parallel* null vectors have $\varphi = 0$, hence $U\cdot V = u^0v^0(1 - \cos 0) = 0$, even though they obviously share a sheet — so the criterion "$U\cdot V > 0$" would falsely report them as not same-sheet. This is exactly the degenerate edge of the [[Thm - Two Lemmas on Causal Vectors|convexity corollary]], where the sum of two future-causal vectors is null (not timelike) precisely when they are parallel null. The transferable diagnostic: whenever a same-sheet or convexity argument involves null vectors, check for collinearity, because the collinear-null case is the unique place where the strict inequality degenerates to equality — and missing it produces a false negative in the causal bookkeeping.
