---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Classification of Four-Vectors"
  - "Def - Minkowski Space and the Metric"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Problem Statement

Let $U$ be a timelike four-vector and let $X \neq 0$ be a four-vector orthogonal to $U$, that is $U\cdot X = 0$.

1. Prove that $X$ is **spacelike**: $X\cdot X < 0$. (Equivalently: the orthogonal complement $U^\perp = \{X : U\cdot X = 0\}$ consists, apart from $0$, entirely of spacelike vectors.)
2. Deduce that the metric $g$ restricted to the three-dimensional subspace $U^\perp$ is **negative definite**, so that $-g$ is a genuine Euclidean inner product on $U^\perp$. Identify $U^\perp$ physically as the **local rest space** of an observer whose four-velocity is $U$.
3. Show by an explicit example that the analogous statement *fails* for a *null* $U$: a nonzero vector orthogonal to a null vector need not be spacelike — it can be null (indeed parallel to $U$).

**Recall:**

![[Def - Classification of Four-Vectors#The Definition]]

The scalar product under the [[Def - Minkowski Space and the Metric|Minkowski metric]] is $U\cdot X = \eta_{\mu\nu}U^\mu X^\nu$. A vector is timelike if $U\cdot U > 0$, spacelike if $X\cdot X < 0$, null if $X\cdot X = 0$. The [[Def - Metric Duality and Index Manipulation|orthogonal complement]] of $U$ is $U^\perp = \{X : U\cdot X = 0\}$, of dimension $3$ by non-degeneracy. The technique throughout is operation 1: choose an orthonormal basis with $e_0$ along $U$.

---

# Convergent Strategy

**Problem class.** A *structural theorem* of indefinite-metric geometry — the single most reusable one in the chapter, since it is the foundation of "the space an observer sees". The [[Special Relativity III — Minkowski Spacetime and the Metric#Insights|topic insights]] flag this as the true name of the orthogonal complement of a timelike vector.

**Assumption pattern.** $U$ is timelike (so $U\cdot U > 0$ and $U$ can be the time axis) and $X$ is orthogonal to it. The signpost is "orthogonal to a timelike vector": that is exactly the condition that places $X$ in the spacelike complement.

**Theorem routing.** Operation 1: choose $e_0 = U/\|U\|$, so $U$ has only a time component. Orthogonality $U\cdot X = 0$ then forces $X^0 = 0$ ([[Def - Metric Duality and Index Manipulation|the scalar product reads off the time component]]), and a vector with vanishing time component has $X\cdot X = -|\mathbf{X}|^2 < 0$ — spacelike. The restriction-to-$U^\perp$ statement is then immediate.

**Key decision point.** The crux is that aligning $e_0$ with $U$ turns "orthogonal to $U$" into "has zero time component", after which spacelikeness is automatic. The contrast with the null case is the decision point: for null $U$ there is no rest frame ($U$ has no unit normalisation), the argument breaks, and $U$ is orthogonal to *itself* — so the complement contains a null vector.

---

# Legal Operations Used

1. **Operation 1 (choose an adapted orthonormal basis):** set $e_0 = U/\|U\|$ so $U$ is purely temporal.

2. **Operation 2 (compute the scalar product by the Minkowski matrix):** $U\cdot X = \|U\|X^0$ and $X\cdot X = -|\mathbf{X}|^2$ in the adapted basis.

3. **Operation 7 (build the orthogonal complement of a vector):** the entire exercise characterises $U^\perp$ as spacelike, the local rest space.

4. **Operation 3 (classify by the sign of the scalar square):** the conclusion $X\cdot X < 0$ is the spacelike classification.

---

# Hints

> [!note]- Hint 1
> Use operation 1: since $U$ is timelike, $e_0 = U/\|U\|$ is a unit timelike vector; complete to an orthonormal basis. Then $U = \|U\|e_0$ has only a time component.

> [!note]- Hint 2
> Write $X = X^0 e_0 + X^i e_i$ and impose $U\cdot X = 0$. Compute $U\cdot X = \|U\|X^0\,(e_0\cdot e_0) = \|U\|X^0$ (since $e_0\cdot e_0 = +1$ and $e_0\cdot e_i = 0$). Orthogonality forces $X^0 = 0$.

> [!note]- Hint 3
> With $X^0 = 0$, compute $X\cdot X = (X^0)^2 - |\mathbf{X}|^2 = -|\mathbf{X}|^2$. Since $X \neq 0$ and $X^0 = 0$, the spatial part $\mathbf{X} \neq 0$, so $X\cdot X = -|\mathbf{X}|^2 < 0$: spacelike. The restriction of $g$ to $U^\perp = \mathrm{span}\{e_1,e_2,e_3\}$ is $\mathrm{diag}(-1,-1,-1)$, negative definite.

> [!note]- Hint 4
> For part 3: take $U = (1,1,0,0)$, null. The vector $X = (1,1,0,0) = U$ itself satisfies $U\cdot X = U\cdot U = 0$ (null vectors are self-orthogonal!) but $X\cdot X = 0$, not $< 0$. So orthogonal-to-null does not imply spacelike — a null vector is orthogonal to itself. The argument needed $U$ timelike to give $e_0$ a normalisation.

---

# Solution

Aligning the basis with $U$ turns orthogonality into "zero time component", forcing spacelikeness. Step 1 sets up the adapted basis; Step 2 derives $X^0 = 0$ and $X\cdot X < 0$ and reads off the rest space; Step 3 shows the null case fails because a null vector is self-orthogonal.

**Step 1: align $e_0$ with $U$.**

> [!note]- Derivation
> $U$ timelike means $U\cdot U > 0$, so $\|U\| = \sqrt{U\cdot U} > 0$ and $e_0 := U/\|U\|$ is a unit timelike vector. Complete to an orthonormal basis $(e_0,e_1,e_2,e_3)$ with $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$, $e_0\cdot e_i = 0$ (such a completion exists by indefinite-metric [[Ex - Constructing an orthonormal basis (Gram-Schmidt with indefinite metric)|Gram-Schmidt]]). In this basis $U = \|U\|\,e_0$: a single, time-only component.

**Step 2: orthogonality forces $X^0 = 0$, hence $X$ spacelike; $U^\perp$ is the rest space.**

> [!note]- Derivation
> Expand $X = X^0 e_0 + X^i e_i$. The orthogonality condition is
> $$0 = U\cdot X = \|U\|\,e_0\cdot(X^0 e_0 + X^i e_i) = \|U\|\big(X^0(e_0\cdot e_0) + X^i(e_0\cdot e_i)\big) = \|U\|\,X^0,$$
> using $e_0\cdot e_0 = +1$, $e_0\cdot e_i = 0$. Since $\|U\| > 0$, this forces $X^0 = 0$: a vector orthogonal to $U$ has no time component *in the rest frame of $U$*. Then
> $$X\cdot X = (X^0)^2 - |\mathbf{X}|^2 = 0 - |\mathbf{X}|^2 = -|\mathbf{X}|^2.$$
> Because $X \neq 0$ and $X^0 = 0$, the spatial part is nonzero, $|\mathbf{X}|^2 > 0$, so $X\cdot X = -|\mathbf{X}|^2 < 0$: **$X$ is spacelike**. This holds for every nonzero $X \in U^\perp$, so the [[Def - Metric Duality and Index Manipulation|orthogonal complement]] $U^\perp = \mathrm{span}\{e_1,e_2,e_3\}$ is entirely spacelike (apart from $0$). On it, $g$ has matrix $\mathrm{diag}(-1,-1,-1)$ — **negative definite** — so $-g$ is a genuine positive-definite Euclidean inner product on the three-dimensional $U^\perp$. Physically, $U^\perp$ is the **local rest space** of an [[Def - Observer and Local Rest Space|observer]] whose four-velocity is $U$: the directions that observer calls "purely spatial", on which lengths and angles are ordinary Euclidean ones.

**Step 3: the null case fails — a null vector is self-orthogonal.**

> [!note]- Derivation
> Take $U = (1,1,0,0)$, which is null: $U\cdot U = 1 - 1 = 0$. The vector $X = U = (1,1,0,0)$ satisfies
> $$U\cdot X = U\cdot U = 0,$$
> so $X$ is orthogonal to $U$ — but $X\cdot X = 0$, so $X$ is **null**, not spacelike. The conclusion of part 1 fails for null $U$. The reason is structural: the proof needed $U$ *timelike* to form the unit vector $e_0 = U/\|U\|$, and $\|U\| = 0$ for a null vector forbids this. More tellingly, a null vector is **orthogonal to itself** ($U\cdot U = 0$), so $U \in U^\perp$: the orthogonal complement of a null vector *contains the null vector*, and is therefore not entirely spacelike. (In fact $U^\perp$ for null $U$ is a *degenerate* three-dimensional subspace tangent to the light cone, containing the null direction $U$ and a two-dimensional spacelike part.) This degeneracy is exactly why a photon has no rest frame and no clean "rest space".

> [!note]- Complete formal solution
> $U$ timelike gives $\|U\| > 0$; set $e_0 = U/\|U\|$ and complete to an orthonormal basis, so $U = \|U\|e_0$. For $X$ with $U\cdot X = 0$: expanding $X = X^0 e_0 + X^i e_i$ gives $U\cdot X = \|U\|X^0 = 0$, so $X^0 = 0$, whence $X\cdot X = -|\mathbf{X}|^2 < 0$ (since $X \neq 0$ forces $\mathbf{X} \neq 0$): $X$ is spacelike. Thus $U^\perp = \mathrm{span}\{e_1,e_2,e_3\}$ carries $g = \mathrm{diag}(-1,-1,-1)$, negative definite, so $-g$ is Euclidean on it — the local rest space of the observer with four-velocity $U$. For null $U = (1,1,0,0)$ the statement fails: $X = U$ has $U\cdot X = U\cdot U = 0$ yet $X\cdot X = 0$, since a null vector is self-orthogonal and has no unit normalisation. $\blacksquare$

---

# Key Takeaways

**Orthogonal to a timelike vector means spacelike, and this single fact is the local rest space of every observer.** The structural heart of the chapter is barely an inequality: any nonzero vector Minkowski-orthogonal to a timelike vector $U$ is spacelike. Read forwards, it says the three-dimensional orthogonal complement $U^\perp$ is entirely spacelike, so the metric restricted to it is *negative definite* and $-g$ is a genuine Euclidean inner product there. This is what licenses the whole apparatus of "the space an observer sees": fix the observer's timelike four-velocity $U$ as the time direction, and $U^\perp$ is their Euclidean three-space, on which lengths, angles, and the Pythagorean theorem all hold in the ordinary way. The trigger to reach for this: any time an [[Def - Observer and Local Rest Space|observer]], a rest frame, a "simultaneity slice", or a "purely spatial" direction appears, the relevant object is the orthogonal complement of a timelike vector, and on it you may compute as in Euclidean geometry. It is the precise reason that relativity, for a single observer, reduces to ordinary three-dimensional physics plus a time direction.

**The proof is operation 1 in two lines, and that is the master technique of the chapter.** The entire argument is: choose $e_0$ along $U$, so $U$ becomes purely temporal; then orthogonality $U\cdot X = 0$ reads off $X^0 = 0$; then $X\cdot X = -|\mathbf{X}|^2 < 0$ is automatic. No diagram, no inequality manipulation — just the adapted orthonormal basis collapsing the scalar product to the time component. This is the same two-line move that proves the [[Thm - Two Lemmas on Causal Vectors|two lemmas on causal vectors]] and the [[Ex - The reversed Cauchy-Schwarz inequality for timelike vectors|reversed Cauchy-Schwarz inequality]], and recognising that all three are the *same* computation (align the basis, read the surviving component) is the unifying insight of the chapter's problem-solving. Whenever a claim about the indefinite metric involves a distinguished timelike vector, the first move is always to make it the time axis.

**The null case fails because a null vector is orthogonal to itself, and that failure is exactly why photons have no rest frame.** The instructive contrast is that the statement is *false* for a null $U$: the orthogonal complement of a null vector contains the null vector itself ($U\cdot U = 0$), so it is not all spacelike but degenerate, tangent to the light cone. The proof breaks at the very first step, where $\|U\| = 0$ forbids forming the unit time axis $e_0 = U/\|U\|$ — the same obstruction that prevents Gram-Schmidt from pivoting on a null vector. Physically this is the statement that a photon has no rest frame: there is no observer for whom light is at rest, no "rest space" orthogonal to a null four-velocity in the clean spacelike sense. The transferable diagnostic: the dichotomy "timelike has a rest space / null does not" traces entirely to self-orthogonality of null vectors, and any construction that secretly assumes a timelike normalisation will fail on the null cone — a recurring trap when extending observer-based reasoning to light.
