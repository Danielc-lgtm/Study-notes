---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\mathcal{O}$ be an observer with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$), and define the candidate orthogonal projector onto the [[Def - Observer and Local Rest Space|local rest space]] $E_{U_0} = U_0^\perp$ by
$$
\Pi(X) = X - (X\cdot U_0)\,U_0.
$$
Working with $c = 1$ and $\eta = \mathrm{diag}(+1,-1,-1,-1)$:

1. Verify that $\Pi(U_0) = 0$ and that $\Pi(X) = X$ for every $X\in E_{U_0}$.
2. Verify that $\Pi(X)\in E_{U_0}$ for every $X$ (the image lands in the rest space).
3. Prove **idempotence**, $\Pi\circ\Pi = \Pi$.
4. Prove that $\Pi$ is **self-adjoint** (symmetric) with respect to the metric: $g(\Pi X, Y) = g(X, \Pi Y)$ for all $X, Y$.
5. Show that the naive sign-flipped map $\Pi'(X) = X + (X\cdot U_0)U_0$ (Gourgoulhon's mostly-plus sign, mis-imported) is **not** a projector: compute $\Pi'(U_0)$ and $\Pi'\circ\Pi'$.

**Recall:**

![[Def - The Orthogonal Projector onto the Local Rest Space#The Definition]]

The [[Def - Observer and Local Rest Space|local rest space]] is $E_{U_0} = U_0^\perp = \{X : X\cdot U_0 = 0\}$. A **projector** is an idempotent endomorphism ($\Pi^2 = \Pi$); it is **orthogonal** (self-adjoint) when $g(\Pi X, Y) = g(X, \Pi Y)$, equivalently when its kernel is the metric-orthogonal complement of its image.

---

# Convergent Strategy

**Problem class.** A *verify-the-defining-properties* problem: an operator is given by a formula and the task is to confirm it is the orthogonal projector by checking idempotence and self-adjointness. The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] for linear-algebra identities is to compute directly with the metric and the formula, getting the sign right via $U_0\cdot U_0 = +1$.

**Assumption pattern.** The only assumptions are $U_0\cdot U_0 = +1$ and the formula for $\Pi$. The whole exercise is a sequence of direct algebraic checks; the assumption that does the work each time is the unit-norm condition $U_0\cdot U_0 = +1$, which is what makes $\Pi(U_0) = 0$ and idempotence hold. The signpost that this is the *orthogonal* (not oblique) projector is self-adjointness.

**Theorem routing.** Each property follows by direct substitution into $\Pi(X) = X - (X\cdot U_0)U_0$, repeatedly using $U_0\cdot U_0 = +1$. Idempotence routes through "$\Pi(X)\in E_{U_0}$ and $\Pi$ fixes $E_{U_0}$"; self-adjointness routes through the manifest symmetry of $g(\Pi X, Y) = X\cdot Y - (X\cdot U_0)(U_0\cdot Y)$ in $X\leftrightarrow Y$.

**Key decision point.** The non-obvious point is part 5: the sign matters absolutely. In mostly-minus, the correct sign is $-$, matching the Euclidean projector $\mathrm{Id} - \langle u,\cdot\rangle u$, because $U_0\cdot U_0 = +1$ behaves like a Euclidean unit vector. Importing Gourgoulhon's $+$ (correct in his mostly-plus, where $\vec u\cdot\vec u = -1$) gives a map that doubles $U_0$ and is not idempotent — the trap the chapter's convention warning guards against.

---

# Legal Operations Used

1. **Project onto the local rest space** (operation 1 from the topic page). The formula $\Pi(X) = X - (X\cdot U_0)U_0$ is the projector itself; every part of the exercise is a direct computation with it.

2. **Differentiate/contract using $U_0\cdot U_0 = +1$** (the unit-norm condition, used as in operation 7). Each property reduces to substituting $U_0\cdot U_0 = +1$ at the right moment.

---

# Hints

> [!note]- Hint 1
> For $\Pi(U_0)$, substitute $X = U_0$ and use $U_0\cdot U_0 = +1$. For $\Pi(X) = X$ on the rest space, use that $X\cdot U_0 = 0$ there, so the subtracted term vanishes.

> [!note]- Hint 2
> To show $\Pi(X)\in E_{U_0}$, compute $\Pi(X)\cdot U_0$ and check it is zero. You will need $U_0\cdot U_0 = +1$ to cancel.

> [!note]- Hint 3
> For idempotence, you have already shown $\Pi(X)\in E_{U_0}$ and that $\Pi$ fixes $E_{U_0}$. Combine. Or compute $\Pi(\Pi(X))$ directly, using $\Pi(X)\cdot U_0 = 0$.

> [!note]- Hint 4
> For self-adjointness, expand $g(\Pi X, Y) = (X - (X\cdot U_0)U_0)\cdot Y$ and look at whether the result is symmetric under swapping $X$ and $Y$.

> [!note]- Hint 5
> For the wrong-sign map, compute $\Pi'(U_0) = U_0 + (U_0\cdot U_0)U_0 = U_0 + U_0 = 2U_0\neq 0$. A projector must kill its kernel direction; this one doubles it.

---

# Solution

Every part is a one-line substitution into $\Pi(X) = X - (X\cdot U_0)U_0$ using $U_0\cdot U_0 = +1$. Step 1 checks the action on $U_0$ and on the rest space; Step 2 confirms the image lands in the rest space; Step 3 deduces idempotence; Step 4 reads off self-adjointness from a manifestly symmetric expression; Step 5 shows the sign-flipped map fails. The single recurring fact is $U_0\cdot U_0 = +1$.

**Step 1: $\Pi$ kills $U_0$ and fixes the rest space.**

> [!note]- Derivation
> Substitute $X = U_0$:
> $$\Pi(U_0) = U_0 - (U_0\cdot U_0)U_0 = U_0 - (+1)U_0 = 0,$$
> using $U_0\cdot U_0 = +1$. For $X\in E_{U_0}$, by definition $X\cdot U_0 = 0$, so
> $$\Pi(X) = X - 0\cdot U_0 = X.$$
> So $\Pi$ annihilates the four-velocity direction (its kernel contains $\mathrm{Span}(U_0)$) and acts as the identity on the rest space (its image contains $E_{U_0}$).

**Step 2: The image lands in the rest space.**

> [!note]- Derivation
> Compute the inner product of $\Pi(X)$ with $U_0$:
> $$\Pi(X)\cdot U_0 = \big(X - (X\cdot U_0)U_0\big)\cdot U_0 = X\cdot U_0 - (X\cdot U_0)(U_0\cdot U_0) = X\cdot U_0 - (X\cdot U_0) = 0,$$
> using $U_0\cdot U_0 = +1$. So $\Pi(X)\in E_{U_0}$ for every $X$: the image of $\Pi$ is contained in the rest space. Combined with Step 1 (image contains $E_{U_0}$), the image is *exactly* $E_{U_0}$.

**Step 3: Idempotence.**

> [!note]- Derivation
> By Step 2, $\Pi(X)\in E_{U_0}$; by Step 1, $\Pi$ fixes $E_{U_0}$. Therefore $\Pi(\Pi(X)) = \Pi(X)$. Directly:
> $$\Pi(\Pi(X)) = \Pi(X) - \big(\Pi(X)\cdot U_0\big)U_0 = \Pi(X) - 0\cdot U_0 = \Pi(X),$$
> using $\Pi(X)\cdot U_0 = 0$ from Step 2. Hence $\Pi\circ\Pi = \Pi$: $\Pi$ is a projector.

**Step 4: Self-adjointness.**

> [!note]- Derivation
> Expand:
> $$g(\Pi X, Y) = \big(X - (X\cdot U_0)U_0\big)\cdot Y = X\cdot Y - (X\cdot U_0)(U_0\cdot Y).$$
> This expression is **symmetric** under $X\leftrightarrow Y$ (both $X\cdot Y$ and $(X\cdot U_0)(U_0\cdot Y)$ are). Hence it equals $g(X, \Pi Y) = X\cdot Y - (Y\cdot U_0)(U_0\cdot X)$. Therefore $g(\Pi X, Y) = g(X, \Pi Y)$: $\Pi$ is self-adjoint with respect to the metric, the defining property of an *orthogonal* projector (kernel = metric-orthogonal complement of image).

**Step 5: The sign-flipped map is not a projector.**

> [!note]- Derivation
> Take $\Pi'(X) = X + (X\cdot U_0)U_0$ (Gourgoulhon's mostly-plus sign, mis-imported into mostly-minus). Then
> $$\Pi'(U_0) = U_0 + (U_0\cdot U_0)U_0 = U_0 + (+1)U_0 = 2U_0\neq 0.$$
> A projector onto the rest space must kill $U_0$; this map *doubles* it. Idempotence also fails:
> $$\Pi'(\Pi'(X)) = \Pi'(X) + \big(\Pi'(X)\cdot U_0\big)U_0,$$
> and $\Pi'(X)\cdot U_0 = X\cdot U_0 + (X\cdot U_0)(U_0\cdot U_0) = 2(X\cdot U_0)$, so $\Pi'(\Pi'(X)) = \Pi'(X) + 2(X\cdot U_0)U_0 = X + 3(X\cdot U_0)U_0\neq\Pi'(X)$. The map is neither idempotent nor a projection onto anything sensible. The correct mostly-minus sign is $-$, matching the Euclidean form $\mathrm{Id} - \langle u,\cdot\rangle u$.

> [!note]- Complete formal solution
> With $U_0\cdot U_0 = +1$: (1) $\Pi(U_0) = U_0 - (U_0\cdot U_0)U_0 = 0$, and for $X\cdot U_0 = 0$, $\Pi(X) = X$. (2) $\Pi(X)\cdot U_0 = X\cdot U_0 - (X\cdot U_0)(U_0\cdot U_0) = 0$, so $\mathrm{im}\,\Pi\subseteq E_{U_0}$. (3) Since $\Pi(X)\in E_{U_0}$ and $\Pi|_{E_{U_0}} = \mathrm{Id}$, $\Pi\circ\Pi = \Pi$. (4) $g(\Pi X, Y) = X\cdot Y - (X\cdot U_0)(U_0\cdot Y)$ is symmetric in $X, Y$, so $\Pi$ is self-adjoint, hence the *orthogonal* projector. (5) The sign-flipped $\Pi'(X) = X + (X\cdot U_0)U_0$ has $\Pi'(U_0) = 2U_0\neq 0$ and $\Pi'\circ\Pi'\neq\Pi'$, so it is not a projector — the mostly-minus sign must be $-$. $\blacksquare$

---

# Key Takeaways

**Idempotence plus self-adjointness is the complete signature of an orthogonal projector — check both.** A projector is defined by idempotence $\Pi^2 = \Pi$; it is an *orthogonal* projector (as opposed to a skew one) exactly when it is additionally self-adjoint, $g(\Pi X, Y) = g(X, \Pi Y)$. These two properties together pin down the operator uniquely given its image, and verifying them is the standard way to confirm you have written the right projector. The transferable lesson: whenever you propose a "project onto this subspace" operator, do not trust the formula until you have checked $\Pi^2 = \Pi$ (it really is a projection) and $\Pi^\dagger = \Pi$ (it really is orthogonal). The same two checks validate projectors in Hilbert space, density matrices in quantum mechanics ($\rho^2 = \rho$ for pure states), and the projection tensor of the $3+1$ split in general relativity.

**The projector sign is fixed by the norm of the vector you project off, and the norm depends on the signature.** The single most error-prone point in this chapter is the sign in $\Pi(X) = X \mp (X\cdot U_0)U_0$. The correct general formula is $\Pi(X) = X - \dfrac{X\cdot U_0}{U_0\cdot U_0}(X\cdot U_0)\cdots$ — more precisely $\Pi(X) = X - \dfrac{X\cdot U_0}{U_0\cdot U_0}U_0$ — so the coefficient is $-1/(U_0\cdot U_0)$, which is $-1$ in mostly-minus (where $U_0\cdot U_0 = +1$) and $+1$ in mostly-plus (where $\vec u\cdot\vec u = -1$). The mnemonic that prevents the error: in mostly-minus the timelike $U_0$ has *positive* norm, so it behaves like a Euclidean unit vector, and the projector is the familiar Euclidean $\mathrm{Id} - \langle u,\cdot\rangle u$. Importing the wrong sign produces a map that doubles the vector you meant to remove and is not even idempotent — a catastrophic, silent error that part 5 makes vivid. Always sanity-check a projector by confirming it kills the direction it should.

**A projector is a direct-sum decomposition wearing an operator's clothes.** The properties verified here — kills the kernel, fixes the image, idempotent — are exactly the statement that $E = \mathrm{im}\,\Pi\oplus\ker\Pi = E_{U_0}\oplus\mathrm{Span}(U_0)$. Self-adjointness upgrades this to an *orthogonal* decomposition, $\ker\Pi = (\mathrm{im}\,\Pi)^\perp$. Recognising the projector as the algebraic encoding of the rest-space/time-axis splitting is what makes it the workhorse of the chapter: every "spatial part for the observer" is $\Pi(X)$, every "time part" is $X - \Pi(X) = (X\cdot U_0)U_0$, and the metric itself splits as $\eta_{\mu\nu} = (U_0)_\mu(U_0)_\nu + \Pi_{\mu\nu}$. The diagnostic for spotting where a projector belongs: any time you need to resolve a vector or tensor into "along a chosen direction" and "orthogonal to it" parts, build the projector off that direction and split.
