---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Classification of Four-Vectors"
  - "Def - Minkowski Space and the Metric"
  - "Def - The Null Cone and the Time Arrow"
tags: [physics, special-relativity]
---

# Problem Statement

A **null** (lightlike) four-vector is a nonzero vector $X$ with $X\cdot X = 0$. This is the property with no Euclidean analogue, and the source of much of the chapter's strangeness.

1. Exhibit a nonzero null vector explicitly and verify $X\cdot X = 0$. Show that in a Euclidean space, by contrast, $X\cdot X = 0$ forces $X = 0$, and pinpoint exactly which property of the metric is responsible for the difference.
2. Show that the null vectors, together with the zero vector, form a **cone**: if $X$ is null then so is $\lambda X$ for every $\lambda \in \mathbb{R}$. Show further that the sum of two null vectors is *generally not* null, by an explicit example.
3. Physically: show that the displacement four-vector of a light ray is null, and that "two distinct events separated by zero interval" means "joined by a light ray" — so zero norm does **not** mean the events coincide.

**Recall:**

![[Def - Classification of Four-Vectors#The Definition]]

The scalar square under the [[Def - Minkowski Space and the Metric|Minkowski metric]] is $X\cdot X = (X^0)^2 - (X^1)^2 - (X^2)^2 - (X^3)^2$. A vector is [[Def - Classification of Four-Vectors|null]] if it is nonzero with $X\cdot X = 0$. The [[Def - The Null Cone and the Time Arrow|null cone]] is the set of null vectors together with the zero vector. A light ray moves at $c = 1$, so over a coordinate time $\Delta t$ it covers spatial distance $|\Delta\mathbf{x}| = \Delta t$.

---

# Convergent Strategy

**Problem class.** A *definitional probe* — verify and internalise the defining feature of indefiniteness, that nonzero vectors can have zero scalar square. The [[Special Relativity III — Minkowski Spacetime and the Metric#Problem-Solving Strategy|topic strategy]] and the calibration checks single this out as the litmus test for understanding the Minkowski metric.

**Assumption pattern.** The only assumption is the indefinite metric itself. The recognition step is that the null condition $X\cdot X = 0$ is a balance between the positive time term and the negative space terms — possible only because the metric has both signs.

**Theorem routing.** Part 1 contrasts indefinite with positive-definite: positive-definiteness is exactly the property whose *absence* allows null vectors. Part 2 uses homogeneity of the quadratic form (degree two) for the cone property and an explicit computation for the non-additivity. Part 3 identifies the light-ray displacement and invokes the [[Def - The Null Cone and the Time Arrow|null cone / light cone]] correspondence.

**Key decision point.** The crux is recognising that "$X\cdot X = 0$ with $X \neq 0$" is *not* a contradiction in an indefinite metric — the positive and negative contributions cancel — whereas in a Euclidean metric the scalar square is a sum of squares and vanishes only at zero. The temptation is to import the Euclidean reflex "zero norm $\Rightarrow$ zero vector"; the entire point is that this reflex is illegal here.

---

# Legal Operations Used

1. **Operation 2 (compute the scalar product by the Minkowski matrix):** verify $X\cdot X = 0$ for the null example and for the sum.

2. **Operation 3 (classify by the sign of the scalar square):** the null class is the $X\cdot X = 0$ case.

3. **Illegal-but-tempting operation 1 (treating the metric as positive definite):** this exercise is the explicit demonstration of why "zero norm implies zero vector" is illegal.

---

# Hints

> [!note]- Hint 1
> Take $X = (1,1,0,0)$. Then $X\cdot X = 1 - 1 = 0$, yet $X \neq 0$: null. In a Euclidean metric, $X\cdot X = (X^0)^2 + (X^1)^2 + \cdots$ is a sum of squares, zero only if every component is zero. The difference is the *sign*: positive-definiteness forbids cancellation, indefiniteness permits it.

> [!note]- Hint 2
> For the cone: $(\lambda X)\cdot(\lambda X) = \lambda^2(X\cdot X) = \lambda^2\cdot 0 = 0$, so every scalar multiple of a null vector is null. For non-additivity, add two null vectors pointing in different spatial directions, e.g. $(1,1,0,0) + (1,-1,0,0) = (2,0,0,0)$, and compute its scalar square.

> [!note]- Hint 3
> A light ray over time $\Delta t$ moves $|\Delta\mathbf{x}| = \Delta t$ (speed $c = 1$). Its displacement $\Delta x^\mu = (\Delta t, \Delta\mathbf{x})$ has $\Delta s^2 = \Delta t^2 - |\Delta\mathbf{x}|^2 = \Delta t^2 - \Delta t^2 = 0$: null. So two events on a light ray have zero interval but are distinct.

---

# Solution

Null vectors exist because the metric is indefinite — positive and negative terms cancel. Step 1 exhibits one and contrasts with the Euclidean case; Step 2 establishes the cone structure and the failure of additivity; Step 3 connects zero interval to light rays.

**Step 1: a nonzero null vector, and why Euclidean space forbids it.**

> [!note]- Derivation
> Take $X = (1,1,0,0)$. By the [[Def - Minkowski Space and the Metric|Minkowski matrix]],
> $$X\cdot X = (1)^2 - (1)^2 - 0 - 0 = 1 - 1 = 0, \qquad X \neq 0.$$
> So $X$ is [[Def - Classification of Four-Vectors|null]]. In a *Euclidean* space the scalar square is the sum of squares $X\cdot X = (X^0)^2 + (X^1)^2 + (X^2)^2 + (X^3)^2$, which is $\geq 0$ and equals zero only when every $X^\mu = 0$, i.e. $X = 0$. The property responsible is **positive-definiteness**: a positive-definite form has $X\cdot X > 0$ for all $X \neq 0$, so it forbids null vectors. The Minkowski form is *indefinite* — one positive and three negative diagonal entries — so the positive time contribution $(X^0)^2$ can be exactly cancelled by the negative space contribution $-|\mathbf{X}|^2$, and that cancellation is a nonzero null vector. Null vectors exist *because* the metric is not positive definite; this is the calibration check for understanding indefiniteness.

**Step 2: the null cone, and the failure of additivity.**

> [!note]- Derivation
> *Cone property.* The quadratic form is homogeneous of degree two, so for any scalar $\lambda$,
> $$(\lambda X)\cdot(\lambda X) = \lambda^2\,(X\cdot X) = \lambda^2\cdot 0 = 0.$$
> Hence every scalar multiple of a null vector is null: the null vectors (with $0$) form a [[Def - The Null Cone and the Time Arrow|cone]], closed under scaling.
>
> *Non-additivity.* Take two null vectors with different spatial directions, $X = (1,1,0,0)$ and $Y = (1,-1,0,0)$ (check $Y\cdot Y = 1 - 1 = 0$). Their sum is
> $$X + Y = (2,0,0,0), \qquad (X+Y)\cdot(X+Y) = 4 - 0 = 4 > 0,$$
> which is **timelike**, not null. So the null cone is *not* a subspace — it is not closed under addition. (It is closed under addition only when the two null vectors are collinear, in which case the sum is again null; this is the degenerate case in the [[Thm - Two Lemmas on Causal Vectors|convexity corollary]].) This is the geometric meaning of "cone, not plane": rays through the origin, not a flat subspace.

**Step 3: light rays have null displacement; zero interval ≠ coincidence.**

> [!note]- Derivation
> A light ray travels at $c = 1$, so over coordinate time $\Delta t$ it covers spatial distance $|\Delta\mathbf{x}| = \Delta t$. Its displacement four-vector is $\Delta x^\mu = (\Delta t, \Delta\mathbf{x})$, with
> $$\Delta s^2 = \Delta x\cdot\Delta x = \Delta t^2 - |\Delta\mathbf{x}|^2 = \Delta t^2 - \Delta t^2 = 0.$$
> So the displacement of a light ray is null. Concretely, a pulse emitted at $P = (0,0,0,0)$ and absorbed at $Q = (1,1,0,0)$ has $\Delta s^2 = 0$, yet $P \neq Q$: the two events are *distinct* but separated by *zero interval*. The conclusion is the headline non-Euclidean fact (Gourgoulhon Remark 1.6, Tong §7.3.1): in Minkowski space, zero "distance" between two events does **not** mean they coincide — it means they are joined by a light ray, lying on each other's [[Def - The Null Cone and the Time Arrow|light cones]]. This is exactly why $\mathbb{M}$ carries a *pseudo*-metric, not a metric.

> [!note]- Complete formal solution
> $X = (1,1,0,0)$ has $X\cdot X = 1 - 1 = 0$ with $X \neq 0$: null. In a Euclidean metric $X\cdot X$ is a sum of squares, zero only at $X = 0$; the difference is positive-definiteness, which the indefinite Minkowski metric lacks, so the positive time term and negative space terms can cancel. The null vectors form a cone, since $(\lambda X)\cdot(\lambda X) = \lambda^2(X\cdot X) = 0$; but the cone is not a subspace, since $(1,1,0,0) + (1,-1,0,0) = (2,0,0,0)$ has scalar square $4 > 0$ (timelike). A light ray over time $\Delta t$ has $|\Delta\mathbf{x}| = \Delta t$, so its displacement $(\Delta t, \Delta\mathbf{x})$ has $\Delta s^2 = \Delta t^2 - \Delta t^2 = 0$: distinct events on a light ray have zero interval, so zero norm does not imply coincidence. $\blacksquare$

---

# Key Takeaways

**Null vectors are the signature of indefiniteness, and "zero norm implies zero vector" is the single most dangerous Euclidean reflex to unlearn.** The defining strangeness of the Minkowski metric is that a *nonzero* vector can have zero scalar square, and the reason is precisely that the metric is not positive definite: the positive time term and the negative space terms can cancel. In a Euclidean space the scalar square is a sum of squares and vanishes only at the origin, so there are no null vectors; the existence of the null cone is exactly the statement that the signature is $(1,3)$ and not $(4,0)$. The trigger to catch the error: any step that concludes "$X = 0$" from "$X\cdot X = 0$", or that treats the norm as positive definite, is illegal in Minkowski space and must be flagged. The repair, when positive-definiteness is genuinely needed, is to restrict to a spacelike subspace (such as an observer's rest space), where $-g$ is a genuine Euclidean inner product and the reflex is legal again.

**The null vectors form a cone, not a subspace — closed under scaling, not under addition — and this is the geometry of the light cone.** The homogeneity of the quadratic form makes every scalar multiple of a null vector null, so the null set is a union of rays through the origin: a cone. But it is *not* a subspace, because the sum of two non-collinear null vectors is timelike (their spatial parts partially cancel while their time parts add). This is why one speaks of the null *cone* and never the null *plane*, and it is the algebraic content of the picture of a double cone separating the timelike interior from the spacelike exterior. The reusable observation: whenever you add causal vectors, do not assume the type is preserved — compute the scalar square of the sum, where the cross term $2X\cdot Y$ carries the result; only collinear null vectors sum to null, the degenerate edge case of the [[Thm - Two Lemmas on Causal Vectors|convexity corollary]].

**Zero interval between distinct events means a light ray joins them, and this is what makes spacetime a pseudo-metric space.** The physical payoff is that the interval fails the defining axiom of a distance: $d(P,Q) = 0$ does not force $P = Q$, because any two events on a common light ray have zero interval. This is not a defect of the construction but its content — the null-separated pairs are exactly the causally-marginal ones, connectible only by light, lying on each other's light cones. The transferable lesson, valid throughout relativity and into general relativity, is that "distance" in a Lorentzian geometry is a pseudo-metric: it can vanish between distinct points (null separation) and be imaginary (spacelike separation, where $\Delta s$ is imaginary though $\Delta s^2$ is a fine real number). The null directions are the boundary of causal influence, and their zero norm is the precise statement that light marks the edge of what can be reached.
