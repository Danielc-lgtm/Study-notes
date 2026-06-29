---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Classification of Four-Vectors"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Problem Statement

In Minkowski space with metric $\eta = \mathrm{diag}(1,-1,-1,-1)$, you are given the four vectors
$$
v_0 = (2,1,0,0), \quad v_1 = (1,1,0,0), \quad v_2 = (0,0,1,0), \quad v_3 = (0,0,0,1).
$$

1. Verify that $v_0$ is timelike, and run the indefinite-metric Gram-Schmidt procedure to produce an orthonormal basis $(e_0,e_1,e_2,e_3)$ with $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$, $e_\alpha\cdot e_\beta = 0$ for $\alpha\neq\beta$, starting from $e_0 \parallel v_0$.
2. Explain precisely where the procedure differs from the Euclidean Gram-Schmidt — both in the normalisation step (dividing by $\sqrt{|v\cdot v|}$ rather than $\sqrt{v\cdot v}$) and in the requirement that exactly one basis vector be timelike.
3. Show by an example that the procedure *fails* if you try to start it from a *null* vector, and explain why.

**Recall:**

![[Def - Minkowski Space and the Metric#The Definition]]

A vector is [[Def - Classification of Four-Vectors|timelike]] if $X\cdot X > 0$, spacelike if $X\cdot X < 0$, null if $X\cdot X = 0$. The norm is $\|X\| = \sqrt{|X\cdot X|}$. The orthogonal projection of $Y$ onto a non-null vector $X$ is $\frac{X\cdot Y}{X\cdot X}X$ ([[Def - Metric Duality and Index Manipulation|metric duality]] guarantees this is well-defined when $X\cdot X \neq 0$). By **Sylvester's law of inertia**, the signature $(1,3)$ is an invariant, so any orthonormal basis has exactly one timelike and three spacelike members.

---

# Convergent Strategy

**Problem class.** A *constructive* problem — build an orthonormal (pseudo-orthonormal) basis adapted to a given vector — which the [[Special Relativity III — Minkowski Spacetime and the Metric#Problem-Solving Strategy|topic strategy]] flags as the workhorse move (operation 1): align the basis with the geometry, then compute. It is the indefinite-metric analogue of the standard Gram-Schmidt orthogonalisation.

**Assumption pattern.** The given $v_0$ is timelike (you check this first), which is the signpost that it can serve as the *time* axis $e_0$; the remaining $v_i$ supply the spatial directions after the timelike part is projected out. The presence of one timelike vector among the data is exactly what makes a $(1,3)$ orthonormal basis constructible.

**Theorem routing.** The procedure is the projection formula $Y \mapsto Y - \frac{X\cdot Y}{X\cdot X}X$ applied repeatedly, legitimate because $X\cdot X \neq 0$ at each step (this is where [[Def - Metric Duality and Index Manipulation|non-degeneracy on the chosen vector]] is used), followed by normalisation $X \mapsto X/\|X\|$ with $\|X\| = \sqrt{|X\cdot X|}$. [[Def - Classification of Four-Vectors|Sylvester's law of inertia]] guarantees the output has signature $(1,3)$.

**Key decision point.** The crux is that the projection coefficient is $\frac{X\cdot Y}{X\cdot X}$, and this requires $X\cdot X \neq 0$ — so the procedure must *start from a non-null vector* and at each stage subtract along non-null vectors. Starting from a null vector divides by zero; this is the one essential difference from Euclidean Gram-Schmidt, where every nonzero vector has positive norm and projection is always defined.

---

# Legal Operations Used

1. **Operation 1 (choose an adapted orthonormal basis):** the entire exercise is this operation made explicit — building the basis with $e_0$ along the timelike $v_0$.

2. **Operation 2 (compute the scalar product by the Minkowski matrix):** every inner product $v_\alpha\cdot v_\beta$ is computed as $v^0_\alpha v^0_\beta - \sum_i v^i_\alpha v^i_\beta$.

3. **Operation 3 (classify by the sign of the scalar square):** used to verify $v_0$ is timelike before taking it as $e_0$, and to check each constructed vector is timelike or spacelike as required.

4. **Operation 7 (orthogonal projection onto a non-null vector):** the projection $\frac{X\cdot Y}{X\cdot X}X$ subtracts the component of $Y$ along $X$ at each step.

---

# Hints

> [!note]- Hint 1
> Start by checking $v_0\cdot v_0 = 4 - 1 = 3 > 0$, so $v_0$ is timelike. Normalise: $e_0 = v_0/\sqrt{3}$, with $e_0\cdot e_0 = +1$. The remaining basis vectors must be spacelike and orthogonal to $e_0$.

> [!note]- Hint 2
> To get $e_1$, project the timelike part out of $v_1$: form $w_1 = v_1 - \frac{e_0\cdot v_1}{e_0\cdot e_0}e_0 = v_1 - (e_0\cdot v_1)e_0$. Compute $e_0\cdot v_1$ using the Minkowski matrix. Then check $w_1$ is spacelike and normalise by $\sqrt{-w_1\cdot w_1}$ (note the minus sign under the root, because $w_1\cdot w_1 < 0$).

> [!note]- Hint 3
> $v_2 = (0,0,1,0)$ and $v_3 = (0,0,0,1)$ are already orthogonal to $e_0$ and to $w_1$ (check: their inner products vanish) and are spacelike with $v_2\cdot v_2 = -1$. So $e_2 = v_2$, $e_3 = v_3$ with no further work. The non-trivial part is only $e_0$ and $e_1$.

> [!note]- Hint 4
> For part 3: try to start from the null vector $n = (1,1,0,0)$, with $n\cdot n = 0$. The projection coefficient $\frac{n\cdot Y}{n\cdot n}$ has a zero denominator — undefined. This is the structural obstruction: Gram-Schmidt needs non-null pivots, and null vectors are exactly those you cannot project along.

---

# Solution

The procedure is Euclidean Gram-Schmidt with two modifications: divide by $\sqrt{|v\cdot v|}$ in the normalisation, and accept that exactly one resulting vector is timelike (the others spacelike), as forced by Sylvester's law. Step 1 normalises the timelike $v_0$ to $e_0$; Step 2 projects the timelike part out of $v_1$ to get the spacelike $e_1$; Step 3 observes $v_2, v_3$ are already orthonormal; Step 4 explains the failure at a null pivot.

**Step 1: $e_0 = v_0/\sqrt{3}$, a unit timelike vector.**

> [!note]- Derivation
> Compute the scalar square by the [[Def - Minkowski Space and the Metric|Minkowski matrix]]:
> $$v_0\cdot v_0 = (2)^2 - (1)^2 - 0 - 0 = 4 - 1 = 3 > 0,$$
> so $v_0$ is [[Def - Classification of Four-Vectors|timelike]] with norm $\|v_0\| = \sqrt{3}$. Set
> $$e_0 = \frac{v_0}{\sqrt{3}} = \tfrac{1}{\sqrt 3}(2,1,0,0),$$
> which has $e_0\cdot e_0 = \frac{1}{3}(3) = +1$. This is the time axis of the new basis.

**Step 2: $e_1 = (1,2,0,0)/\sqrt{3}$, a unit spacelike vector orthogonal to $e_0$.**

> [!note]- Derivation
> Project the $e_0$-component out of $v_1 = (1,1,0,0)$. First
> $$e_0\cdot v_1 = \tfrac{1}{\sqrt 3}\big[(2)(1) - (1)(1)\big] = \tfrac{1}{\sqrt 3}(2 - 1) = \tfrac{1}{\sqrt 3}.$$
> Then
> $$w_1 = v_1 - (e_0\cdot v_1)\,e_0 = (1,1,0,0) - \tfrac{1}{\sqrt 3}\cdot\tfrac{1}{\sqrt 3}(2,1,0,0) = (1,1,0,0) - \tfrac13(2,1,0,0) = \big(\tfrac13,\tfrac23,0,0\big).$$
> Check orthogonality: $e_0\cdot w_1 = \tfrac{1}{\sqrt3}[(2)(\tfrac13) - (1)(\tfrac23)] = \tfrac{1}{\sqrt3}(\tfrac23 - \tfrac23) = 0$. Good. Now classify $w_1$:
> $$w_1\cdot w_1 = \big(\tfrac13\big)^2 - \big(\tfrac23\big)^2 = \tfrac19 - \tfrac49 = -\tfrac39 = -\tfrac13 < 0,$$
> so $w_1$ is **spacelike**. Normalise by $\sqrt{|w_1\cdot w_1|} = \sqrt{1/3} = 1/\sqrt3$:
> $$e_1 = \frac{w_1}{1/\sqrt3} = \sqrt3\,\big(\tfrac13,\tfrac23,0,0\big) = \tfrac{1}{\sqrt3}(1,2,0,0),$$
> with $e_1\cdot e_1 = \frac{1}{3}(1 - 4) = -1$. The minus sign under the normalising root — $\sqrt{|w_1\cdot w_1|}$ not $\sqrt{w_1\cdot w_1}$ — is the first place the indefinite metric departs from the Euclidean procedure.

**Step 3: $e_2 = v_2$, $e_3 = v_3$ — already orthonormal.**

> [!note]- Derivation
> Both $v_2 = (0,0,1,0)$ and $v_3 = (0,0,0,1)$ have zero time component, so $e_0\cdot v_2 = e_0\cdot v_3 = 0$, and zero overlap with $w_1$ (which has support only in the $0,1$ directions), so $e_1\cdot v_2 = e_1\cdot v_3 = 0$. They are mutually orthogonal ($v_2\cdot v_3 = 0$) and spacelike: $v_2\cdot v_2 = -1$, $v_3\cdot v_3 = -1$. Hence $e_2 = v_2$, $e_3 = v_3$ require no projection or rescaling. The basis
> $$e_0 = \tfrac{1}{\sqrt3}(2,1,0,0),\quad e_1 = \tfrac{1}{\sqrt3}(1,2,0,0),\quad e_2 = (0,0,1,0),\quad e_3 = (0,0,0,1)$$
> is orthonormal with signature $(1,3)$: one timelike, three spacelike, as Sylvester's law demands.

**Step 4: starting from a null vector fails.**

> [!note]- Derivation
> Suppose one tried to begin the procedure from the null vector $n = (1,1,0,0)$, $n\cdot n = 1 - 1 = 0$. The very first normalisation $n/\|n\| = n/\sqrt{|n\cdot n|} = n/0$ is undefined; and the projection of any later vector $Y$ along $n$, namely $\frac{n\cdot Y}{n\cdot n}n$, has a zero denominator. The procedure requires *non-null pivots*. The reason is structural: the [[Def - Metric Duality and Index Manipulation|orthogonal projection]] onto $X$ uses $\frac{1}{X\cdot X}$, which exists only for $X\cdot X \neq 0$. A null vector is orthogonal to itself ($n\cdot n = 0$), so "projecting onto $n$" is ill-defined — there is no component of $n$ along itself to normalise. This is the essential way the indefinite metric breaks Euclidean Gram-Schmidt, where every nonzero vector has $X\cdot X > 0$ and pivots are always available.

> [!note]- Complete formal solution
> $v_0\cdot v_0 = 4 - 1 = 3 > 0$, so $v_0$ is timelike; set $e_0 = v_0/\sqrt3$, $e_0\cdot e_0 = +1$. Project: $e_0\cdot v_1 = \frac{1}{\sqrt3}(2-1) = \frac{1}{\sqrt3}$, so $w_1 = v_1 - (e_0\cdot v_1)e_0 = (1,1,0,0) - \frac13(2,1,0,0) = (\frac13,\frac23,0,0)$, with $w_1\cdot w_1 = \frac19 - \frac49 = -\frac13 < 0$ (spacelike); normalise by $\sqrt{1/3}$ to get $e_1 = \frac{1}{\sqrt3}(1,2,0,0)$, $e_1\cdot e_1 = -1$. Both $v_2 = (0,0,1,0)$ and $v_3 = (0,0,0,1)$ are already orthogonal to $e_0, e_1$ and spacelike with scalar square $-1$, so $e_2 = v_2$, $e_3 = v_3$. The resulting basis is orthonormal with signature $(1,3)$. The procedure differs from Euclidean Gram-Schmidt in (i) normalising by $\sqrt{|v\cdot v|}$, so spacelike vectors are divided by $\sqrt{-v\cdot v}$, and (ii) producing exactly one timelike member, forced by Sylvester's law of inertia. It fails if started from a null vector $n$, because the projection coefficient $\frac{n\cdot Y}{n\cdot n}$ and the normalisation $n/\|n\|$ both divide by $n\cdot n = 0$: null vectors cannot be pivots. $\blacksquare$

---

# Key Takeaways

**Gram-Schmidt survives the indefinite metric, but only across non-null pivots, and that single restriction is the whole story.** The Euclidean orthogonalisation procedure — subtract the projection onto each previously-built vector, then normalise — carries over verbatim to Minkowski space, with two cosmetic changes (normalise by $\sqrt{|v\cdot v|}$; accept one timelike output) and one essential one: every vector you project along must have $v\cdot v \neq 0$, because the projection coefficient is $\frac{v\cdot Y}{v\cdot v}$. The trigger to recognise this pattern is any request to build a frame, a rest space, or an orthogonal complement in a space with an indefinite form: reach for Gram-Schmidt, but scan for null vectors first, since they are exactly the vectors that cannot serve as pivots. This is the same obstruction that makes null vectors orthogonal to themselves and that prevents a "rest frame" of a photon — the geometry refuses to give a null direction a normalised partner.

**The normalisation $\sqrt{|v\cdot v|}$ and the forced signature are where Euclidean intuition must yield to Sylvester's law.** In a Euclidean space every orthonormal basis vector has $e\cdot e = +1$; in Minkowski space exactly one has $+1$ and three have $-1$, and no choice of procedure can change this count, because by Sylvester's law of inertia the signature $(1,3)$ is a basis-independent invariant of the metric. The practical consequence is that you do not get to decide how many timelike basis vectors to produce — the data $v_0$ being timelike determines that $e_0$ is the timelike one, and the rest come out spacelike automatically. The reusable diagnostic: if your construction ever yields two timelike or zero timelike basis vectors, you have made an arithmetic error, because the signature is fixed. This is the constructive face of the warning that no orthonormal basis can have all four vectors of scalar square $+1$.

**Aligning the basis with a timelike vector is the master computational move, and this exercise is its mechanics.** The reason the topic strategy insists on operation 1 — choose $e_0$ along a timelike vector — is that it reduces a distinguished vector to a single component and kills cross terms in every subsequent scalar product. This exercise builds exactly such a basis explicitly, and the same construction underlies the proofs of the [[Thm - Two Lemmas on Causal Vectors|two lemmas on causal vectors]], the [[Ex - The reversed Cauchy-Schwarz inequality for timelike vectors|reversed Cauchy-Schwarz inequality]], and the description of an [[Def - Observer and Local Rest Space|observer's local rest space]] (which is precisely the spacelike span $\{e_1,e_2,e_3\}$ orthogonal to the observer's timelike $e_0$). Once you can produce the adapted basis by hand, every "indefinite-metric" computation becomes a short Euclidean computation on the spacelike complement plus a clean time direction, and the apparent difficulty of the Lorentzian signature evaporates.
