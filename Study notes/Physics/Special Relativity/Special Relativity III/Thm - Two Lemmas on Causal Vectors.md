---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Classification of Four-Vectors"
  - "Def - The Null Cone and the Time Arrow"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. The metric is $\eta = \mathrm{diag}(1,-1,-1,-1)$; the scalar product is $U\cdot V = \eta_{\mu\nu}U^\mu V^\nu = U^0V^0 - U^1V^1 - U^2V^2 - U^3V^3$; the norm of a timelike vector is $\|U\| = \sqrt{U\cdot U}$. An orthonormal basis $(e_0,e_1,e_2,e_3)$ has $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$, $e_\alpha\cdot e_\beta = 0$ ($\alpha\neq\beta$). The [[Def - The Null Cone and the Time Arrow|null cone]] has two sheets $\mathcal{I}^+, \mathcal{I}^-$; two causal vectors are in the *same sheet* if both are future-directed or both past-directed. Full registry on [[Special Relativity III — Minkowski Spacetime and the Metric]].

> [!warning] Convention: signature
> These are Gourgoulhon's Lemmas 1.4.2, translated to our **mostly-minus** signature. In Gourgoulhon's mostly-plus convention the criterion is $\vec u\cdot\vec v < 0$; flipping the overall sign of the scalar product gives our criterion $U\cdot V > 0$. The proofs below are his, with $e_0\cdot e_0 = +1$ (ours) in place of his $-1$, so every sign has been carried through carefully.

---

# Statement

> **Lemma 1 (timelike vectors).** Let $U$ and $V$ be two timelike four-vectors. Then $U$ and $V$ lie in the same sheet of the [[Def - The Null Cone and the Time Arrow|null cone]] (both future-directed or both past-directed) if and only if
> $$U\cdot V > 0.$$

> **Lemma 2 (null vectors).** Let $U$ and $V$ be two null, non-collinear four-vectors. Then $U$ and $V$ lie in the same sheet of the null cone if and only if
> $$U\cdot V > 0.$$

Together they give the structural corollary that drives the chapter:

> **Corollary (convexity of the future-causal cone).** The sum of two future-directed causal (timelike or null) vectors is future-directed and causal; it is timelike unless both summands are parallel null vectors, in which case it is null. Hence the future-directed causal vectors form a convex cone.

---

# Motivation

The [[Def - The Null Cone and the Time Arrow|time arrow]] is a *choice* of one sheet of the null cone as the future. For that choice to be physically meaningful, "future-directed" must be a coherent notion: two future-directed vectors must be recognisable as such, and combining future-directed motions must stay future-directed. These two lemmas are what make the time arrow coherent, and they do it with a single computable criterion — the *sign of a scalar product*.

The role of the lemmas is to convert a statement about *which sheet of the cone* a vector lies in — a global, geometric, seemingly hard-to-check condition — into a statement about $U\cdot V$, a one-line computation. This is the same move the chapter makes everywhere: replace geometry with an algebraic invariant. Lemma 1 handles timelike vectors (the interiors of the sheets), Lemma 2 the null vectors (the sheets themselves), and between them they cover all causal vectors.

The importance is in the corollary. That the sum of future-causal vectors is future-causal is exactly what is needed for the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] (a chain of worldline segments stays future-timelike, so proper times add the way they should), for the consistency of [[Def - Four-Momentum and Rest Mass|four-momentum conservation]] (the total momentum of future-moving particles is future-timelike, so the system has a well-defined rest frame and positive invariant mass), and for the very notion of an arrow of time (combining future-directed processes never produces a past-directed one). Without the lemmas these facts would have to be checked case by case; with them they are corollaries of one sign.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition of each lemma is "$U, V$ are causal" (timelike for Lemma 1, null for Lemma 2). The point of input broadening is to recognise the situations that supply causal vectors.

The first disguised source is **"$U$ is a four-velocity"**. Every massive particle's [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is future-directed timelike with $U\cdot U = 1$. So any problem mentioning two particles' four-velocities is a Lemma 1 situation, and $U\cdot V$ is the (invariant) relative Lorentz factor $\gamma_{\text{rel}}$ between them — automatically positive, certifying they move into the same future. *Example problem:* show that the relative speed of two massive particles is always less than light, by computing $U\cdot V = \gamma_{\text{rel}} > 1$.

The second disguised source is **"$P$ is a four-momentum"**. The [[Def - Four-Momentum and Rest Mass|four-momentum]] of a physical particle is future-directed causal — timelike for massive, null for massless. A sum of such momenta is a sum of future-causal vectors, so the corollary applies and the total is future-timelike (provided not all are parallel null). *Example problem:* show that the total four-momentum of a system of particles is timelike, hence the system has a rest frame and an invariant mass $M$ with $M \geq \sum m_i$.

The third disguised source is **"$U$ is a worldline segment"**. A future-directed timelike displacement between two events is a causal vector; the corollary makes the concatenation of two such segments future-timelike. *Example problem:* the [[Thm - The Reversed Triangle Inequality|twin paradox]], where the traveller's outbound and inbound legs $U, V$ are future-timelike and their sum $U+V$ is the stay-at-home twin's displacement.

**Targets (Output Amplification)**

The conclusion is "$U, V$ same sheet $\Leftrightarrow U\cdot V > 0$", and the corollary "future-causal vectors form a convex cone".

Combine the conclusion with **a known time-orientation of one vector**. If $U$ is *known* future-directed and $U\cdot V > 0$, then $V$ is future-directed too. The further result is a test for future-directedness that needs only a scalar product against a reference future vector — typically an observer's four-velocity. The combination is useful because "is $V$ future-directed?" becomes "is $V\cdot U_{\text{obs}} > 0$?", a single sign. *Example:* an observer with four-velocity $U_{\text{obs}}$ measures a particle's energy as $E = P\cdot U_{\text{obs}}$, positive exactly when $P$ is future-directed — physical particles have positive energy.

Combine the corollary with **the reversed Cauchy-Schwarz inequality**. Convexity plus $U\cdot V \geq \|U\|\,\|V\|$ for future-timelike vectors gives the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] $\|U+V\| \geq \|U\| + \|V\|$. The further result is that the straight worldline maximises proper time. The combination is nonobvious because it inverts the Euclidean triangle inequality, and it is the geometric content of the twin paradox.

Combine the corollary with **a sequence of future-causal vectors**. Convexity extends by induction: any finite sum of future-causal vectors is future-causal (timelike unless all parallel null). The further result is that a total four-momentum, however many particles contribute, is future-timelike — the foundation of the centre-of-momentum frame. *Example:* the invariant mass of a multi-particle system, computed as $M^2 = P_{\text{tot}}\cdot P_{\text{tot}} > 0$.

---

# Why Is It True

The whole proof is the technique the chapter is built on: **align an orthonormal basis with one of the vectors, and the scalar product collapses to a sign you can read off.**

For Lemma 1, take $U$ timelike and choose the basis so that $e_0$ points along $U$. Then $U$ has a single nonzero component, $U = \|U\|\,e_0$, sitting purely in the time direction. Expand $V$ in this basis: $V = V^0 e_0 + V^i e_i$. The scalar product $U\cdot V$ now only sees the time component of $V$, because $e_0$ is orthogonal to the spatial $e_i$ and $e_0\cdot e_0 = +1$ in our signature. So $U\cdot V = \|U\|\,V^0$, a positive multiple of $V^0$. And "same sheet as $U$" means $V$ points the same way in time as $U$, i.e. $V^0 > 0$ (since $e_0$ is along $U$, future-directed). Therefore same sheet $\Leftrightarrow V^0 > 0 \Leftrightarrow U\cdot V > 0$. The whole content is that *in the rest frame of $U$, the scalar product reads off the time component of $V$*, and the time component is exactly what decides the sheet.

**In one line: the scalar product of a timelike vector with anything is, in the timelike vector's rest frame, just (its norm) times (the other vector's time component) — so its sign is the sign of that time component, which is the sheet.**

For Lemma 2, both vectors are null, so neither has a rest frame, but a similar adapted basis works. Write $U = u^0(e_0 + e_1)$ — any future null vector can be put in this form by rotating space so its spatial part is along $e_1$ and scaling — and write $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$, with $\varphi \neq 0$ since $U, V$ are non-collinear. The scalar product picks up $e_0\cdot e_0 = +1$ from the time parts and $e_1\cdot e_1 = -1$ from the aligned space parts: $U\cdot V = u^0 v^0(1 - \cos\varphi)$. Since $\varphi \neq 0$, $1 - \cos\varphi > 0$, so the sign of $U\cdot V$ is the sign of $u^0 v^0$ — positive exactly when $U$ and $V$ point the same way in time (same sheet). The geometric reason the null case still works is that two distinct null directions are never *exactly* opposite in their spatial parts unless they are on opposite sheets; the angle $\varphi$ measures their spatial misalignment, and $1 - \cos\varphi$ is positive whenever they are not collinear.

The corollary follows because $(U+V)\cdot(U+V) = U\cdot U + 2U\cdot V + V\cdot V$, and for future-causal $U, V$ each term is $\geq 0$ with $U\cdot V > 0$ (by the lemmas, since same sheet), so the sum is positive — timelike — unless $U\cdot U = V\cdot V = 0$ (both null) and $U\cdot V = 0$ (collinear), the single degenerate case. The time component $U^0 + V^0 > 0$ keeps it future-directed.

---

# What Makes This Hard

The conceptual hurdle is trusting that a *single component* in an adapted basis captures a *frame-independent* fact: the proof computes $U\cdot V$ in the special frame where $e_0 \parallel U$, but the conclusion (same sheet $\Leftrightarrow U\cdot V > 0$) is frame-independent because $U\cdot V$ is invariant — and beginners worry the choice of frame has smuggled something in. It has not: the *value* $U\cdot V$ is the same in all frames, so computing it in a convenient one is legitimate. The most common technical error is in our-signature bookkeeping: writing $e_0\cdot e_0 = -1$ (Gourgoulhon's convention) instead of $+1$ (ours) flips the criterion to $U\cdot V < 0$, which is wrong here. The second pitfall is forgetting the non-collinearity hypothesis in Lemma 2 — without it $\varphi = 0$ is possible, $1 - \cos\varphi = 0$, and $U\cdot V = 0$ even for same-sheet vectors (two parallel null vectors).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove each lemma by choosing an orthonormal basis adapted to $U$ so that the scalar product collapses to a single sign. For Lemma 1, put $e_0$ along $U$; for Lemma 2, put $U$ along $e_0 + e_1$. Read off that the sign of $U\cdot V$ equals the sign of the relevant time component, which is the sheet. Then prove the corollary by expanding $(U+V)\cdot(U+V)$.

**Subgoal decomposition:**

1. **Lemma 1 — adapt the basis.** Choose an orthonormal basis with $e_0 = U/\|U\|$, so $U = \|U\|\,e_0$.
   - *Hint:* $U$ timelike means $U\cdot U > 0$, so $U/\|U\|$ is a unit timelike vector and can be taken as $e_0$.
   - *Why needed:* It reduces $U$ to a single component, killing the spatial terms in $U\cdot V$.

2. **Lemma 1 — read off the sign.** Compute $U\cdot V = \|U\|\,V^0$ and identify "same sheet" with $V^0 > 0$.
   - *Hint:* $e_0\cdot e_0 = +1$, $e_0\cdot e_i = 0$, so only the time component of $V$ survives.
   - *Why needed:* It is the equivalence "same sheet $\Leftrightarrow U\cdot V > 0$".

3. **Lemma 2 — adapt the basis.** Write $U = u^0(e_0 + e_1)$ and $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$ with $\varphi \neq 0$.
   - *Hint:* Any future null vector is $u^0(e_0 + \hat{\mathbf{n}})$ for a unit spatial $\hat{\mathbf{n}}$; rotate so $U$'s direction is $e_1$, then $V$'s lies in the $e_1 e_2$ plane at angle $\varphi$.
   - *Why needed:* It sets up the one nontrivial computation, with $\varphi$ measuring spatial misalignment.

4. **Lemma 2 — read off the sign.** Compute $U\cdot V = u^0 v^0(1 - \cos\varphi)$ and use $1 - \cos\varphi > 0$.
   - *Hint:* The time parts give $+1$, the aligned $e_1$ parts give $-\cos\varphi$ (since $e_1\cdot e_1 = -1$); $\varphi\neq 0$ makes $1 - \cos\varphi > 0$.
   - *Why needed:* The sign of $U\cdot V$ is then the sign of $u^0 v^0$, which is the sheet.

5. **Corollary — expand the sum.** Show $(U+V)\cdot(U+V) > 0$ for future-causal $U,V$, with the lone null-collinear exception.
   - *Hint:* $(U+V)\cdot(U+V) = U\cdot U + 2U\cdot V + V\cdot V$; each term $\geq 0$ and $U\cdot V > 0$ unless both null and collinear.
   - *Why needed:* It upgrades the two lemmas into the convexity of the future-causal cone.

---

# Lemma Decomposition

> [!note]- Lemma 1: Same-sheet criterion for timelike vectors
> **Statement:** Two timelike vectors $U, V$ are in the same sheet of the null cone if and only if $U\cdot V > 0$.
>
> **Hint:** Put $e_0$ along $U$; then $U\cdot V$ is a positive multiple of $V^0$.
>
> **Why needed:** It is the timelike case, and the prototype for the technique used throughout.
>
> > [!note]- Full proof
> > Since $U$ is timelike, $U\cdot U > 0$, and $e_0 := U/\|U\|$ is a future-directed unit timelike vector (choosing the orientation so that $U$ is future-directed; the past case is identical with signs reversed). Complete $e_0$ to an orthonormal basis $(e_0,e_1,e_2,e_3)$ with $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$, $e_0\cdot e_i = 0$. In this basis $U = \|U\|\,e_0$, a single nonzero component. Expand $V = V^0 e_0 + V^i e_i$. Then
> > $$U\cdot V = \|U\|\,e_0\cdot(V^0 e_0 + V^i e_i) = \|U\|\big(V^0\,(e_0\cdot e_0) + V^i\,(e_0\cdot e_i)\big) = \|U\|\,V^0,$$
> > using $e_0\cdot e_0 = +1$ and $e_0\cdot e_i = 0$. Now $V$ is timelike, and it lies in the same sheet as $U$ (the future sheet, since $e_0 \parallel U$ is future-directed) if and only if its time component in this basis is positive, $V^0 > 0$. Since $\|U\| > 0$, we conclude $V^0 > 0 \Leftrightarrow U\cdot V > 0$. $\blacksquare$

> [!note]- Lemma 2: Same-sheet criterion for null vectors
> **Statement:** Two null, non-collinear vectors $U, V$ are in the same sheet of the null cone if and only if $U\cdot V > 0$.
>
> **Hint:** Write $U = u^0(e_0 + e_1)$, $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$; then $U\cdot V = u^0v^0(1-\cos\varphi)$.
>
> **Why needed:** It is the null case, completing the coverage of all causal vectors.
>
> > [!note]- Full proof
> > A null vector has $X\cdot X = (X^0)^2 - |\mathbf{X}|^2 = 0$, so $|\mathbf{X}| = |X^0|$; writing $X^0 = x^0$ and the spatial direction as a unit vector $\hat{\mathbf{n}}$, every null vector is $X = x^0(e_0 + \hat{\mathbf{n}})$ with $\hat{\mathbf{n}}$ a unit spatial vector. Choose the orthonormal basis so that $U$'s spatial direction is $e_1$: $U = u^0(e_0 + e_1)$. The spatial direction of $V$ then makes some angle $\varphi$ with $e_1$ in the spatial hyperplane; rotating within the spatial directions $e_2,e_3$ we may take it in the $e_1 e_2$ plane, $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$. Non-collinearity of $U, V$ forces $\varphi \neq 0$ (and $\varphi \neq 0 \bmod 2\pi$). Compute, using $e_0\cdot e_0 = +1$, $e_1\cdot e_1 = -1$, and all cross terms zero:
> > $$U\cdot V = u^0 v^0\big[(e_0\cdot e_0) + \cos\varphi\,(e_1\cdot e_1)\big] = u^0 v^0\big[1 - \cos\varphi\big].$$
> > Since $\varphi \neq 0$, $\cos\varphi < 1$, so $1 - \cos\varphi > 0$. Therefore $U\cdot V$ has the same sign as $u^0 v^0$. And $U, V$ lie in the same sheet if and only if $u^0$ and $v^0$ have the same sign, i.e. $u^0 v^0 > 0$. Hence same sheet $\Leftrightarrow U\cdot V > 0$. $\blacksquare$

> [!note]- Lemma 3: Convexity of the future-causal cone
> **Statement:** The sum of two future-directed causal vectors $U, V$ is future-directed causal, timelike unless both are parallel null.
>
> **Hint:** Expand $(U+V)\cdot(U+V)$ and use the two lemmas to sign the cross term.
>
> **Why needed:** It is the corollary that powers the reversed triangle inequality and four-momentum conservation.
>
> > [!note]- Full proof
> > Let $U, V$ be future-directed causal vectors, so $U\cdot U \geq 0$ and $V\cdot V \geq 0$ (with equality iff null). They lie in the same (future) sheet, so by Lemma 1 (if timelike) or Lemma 2 (if null and non-collinear) we have $U\cdot V > 0$; in the remaining case $U, V$ are parallel null, where $U\cdot V = 0$. Now
> > $$(U+V)\cdot(U+V) = U\cdot U + 2\,U\cdot V + V\cdot V \geq 0,$$
> > and the right-hand side is strictly positive unless every term vanishes: $U\cdot U = V\cdot V = 0$ (both null) and $U\cdot V = 0$ (collinear). Hence $U+V$ is timelike except when $U, V$ are parallel null vectors, in which case $U+V$ is null. In all cases the time component $U^0 + V^0 > 0$ (both future-directed), so $U+V$ is future-directed. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Lemma 1.** $U$ timelike gives $U\cdot U > 0$, so $e_0 := U/\|U\|$ is a unit timelike vector; take it future-directed (else reverse all signs). Complete to an orthonormal basis with $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$, $e_0\cdot e_i = 0$. Then $U = \|U\|e_0$ and, expanding $V = V^0 e_0 + V^i e_i$,
> $$U\cdot V = \|U\|\,V^0.$$
> $V$ is in the same (future) sheet as $U$ iff $V^0 > 0$, and since $\|U\| > 0$ this is iff $U\cdot V > 0$.
>
> **Lemma 2.** Every null vector is $X = x^0(e_0 + \hat{\mathbf{n}})$, $\hat{\mathbf{n}}$ a unit spatial vector. Choose the basis with $U = u^0(e_0 + e_1)$ and, rotating spatial axes, $V = v^0(e_0 + \cos\varphi\,e_1 + \sin\varphi\,e_2)$, with $\varphi \neq 0$ by non-collinearity. Then
> $$U\cdot V = u^0 v^0\,(1 - \cos\varphi),$$
> and $1 - \cos\varphi > 0$, so $\mathrm{sign}(U\cdot V) = \mathrm{sign}(u^0 v^0)$. The vectors share a sheet iff $u^0 v^0 > 0$, i.e. iff $U\cdot V > 0$.
>
> **Corollary.** For future-directed causal $U, V$: each scalar square is $\geq 0$, and $U\cdot V > 0$ (same sheet, by Lemma 1 or 2) except when $U, V$ are parallel null, where $U\cdot V = 0$. Then
> $$(U+V)\cdot(U+V) = U\cdot U + 2U\cdot V + V\cdot V \geq 0,$$
> strictly positive unless all terms vanish (both null and collinear). So $U+V$ is timelike, or null in the parallel-null case; and $U^0 + V^0 > 0$ makes it future-directed. Iterating, any finite sum of future-causal vectors is future-causal, hence the future-causal vectors form a convex cone. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The relative Lorentz factor of two observers.** For two [[Def - Four-Velocity and Four-Acceleration|four-velocities]] $U, V$ (future-timelike, $U\cdot U = V\cdot V = 1$), Lemma 1 gives $U\cdot V > 0$, and in fact $U\cdot V = \gamma_{\text{rel}} = (1 - v_{\text{rel}}^2)^{-1/2} \geq 1$, the Lorentz factor of their relative motion. Computing $U\cdot V$ in one frame and reading off $\gamma_{\text{rel}}$ is interval-invariance applied to four-velocities; the application is nonobvious because "relative speed" does not look like a scalar product until you see it is one.

**Positivity of energy.** An observer with four-velocity $U_{\text{obs}}$ measures a particle's energy as $E = P\cdot U_{\text{obs}}$. By Lemma 1 (or 2, for photons), $P$ future-causal and $U_{\text{obs}}$ future-timelike give $P\cdot U_{\text{obs}} > 0$: every observer measures positive energy for a physical particle. The application is out-of-distribution because positivity of energy is usually stated dynamically, yet here it is a corollary of same-sheet geometry.

**Hyperbolic geometry of velocity space.** The future unit timelike vectors form one sheet of the hyperboloid $U\cdot U = 1$, a model of hyperbolic 3-space, and Lemma 1's quantity $U\cdot V = \cosh(\text{hyperbolic distance})$ is the hyperbolic law of cosines. Rapidity is hyperbolic distance, and $U\cdot V > 0$ is the statement that any two points of the hyperboloid are at finite hyperbolic distance. The application connects relativity to non-Euclidean geometry through the same scalar product.

---

# Bridges

- **[[Thm - The Reversed Triangle Inequality]]** — the corollary (convexity of the future-causal cone) is the structural input to the reversed triangle inequality: because $U+V$ stays future-timelike and $U\cdot V \geq \|U\|\|V\|$, one gets $\|U+V\| \geq \|U\|+\|V\|$, the statement that the straight worldline has the longest proper time. These lemmas are the algebraic engine; the reversed triangle inequality is the geometric payoff.

- **[[Def - Four-Momentum and Rest Mass]]** — applied to four-momenta, the corollary shows the total momentum of a system of future-moving particles is future-timelike, so the system has a rest (centre-of-momentum) frame and a positive invariant mass $M = \|P_{\text{tot}}\|$. This is what makes the invariant-mass calculation of collisions well-posed.

- **[[Def - The Null Cone and the Time Arrow]]** — the lemmas are precisely the proof that the time arrow is *consistent*: "future-directed" is a coherent attribute (Lemmas 1, 2 give a frame-independent same-sheet test) and is closed under addition (the corollary). Without them the choice of future sheet would not propagate coherently to all causal vectors.

- **Euclidean angle inequality** — the Euclidean analogue is trivial and instructive by contrast: in a Euclidean space $\mathbf{u}\cdot\mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos\theta$ can have either sign, and there is no "same sheet" because the unit sphere is connected. The two-sheeted hyperboloid of Minkowski space is what makes a sign criterion meaningful, and the indefinite metric is what makes $U\cdot V$ exceed the product of norms rather than be bounded by it.

---

# Unlocked by This

> [!tip] The Reversed Cauchy-Schwarz and Triangle Inequalities *(from §3.2)*
> The same adapted-basis technique, applied to two timelike vectors, gives the **reversed Cauchy-Schwarz inequality** $|U\cdot V| \geq \|U\|\,\|V\|$ (equality iff collinear), and hence the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]]; see [[Ex - The reversed Cauchy-Schwarz inequality for timelike vectors]]. The lemmas and these inequalities are the same fact — the geometry of the indefinite metric on the timelike cone — viewed through the sign and through the magnitude of $U\cdot V$.

> [!tip] Causal Structure and Global Hyperbolicity *(from General Relativity)*
> In curved spacetime the same convexity argument, applied in each tangent space, underlies the local **causal structure**; assembling it globally gives the causality conditions — chronology, stable causality, global hyperbolicity — that are the hypotheses of the **singularity theorems** of general relativity. The future-causal cone of this page is the infinitesimal object whose global integration is the causal future.
