---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Metric Duality and Index Manipulation"
  - "Def - Minkowski Space and the Metric"
  - "Def - Four-Vector"
tags: [physics, special-relativity]
---

# Problem Statement

Work in an orthonormal frame with $\eta = \mathrm{diag}(1,-1,-1,-1)$ and inverse $\eta^{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$ (numerically the same).

1. For the four-vector $X^\mu = (5, 3, -2, 0)$, compute the lowered components $X_\mu = \eta_{\mu\nu}X^\nu$, then raise them back, $\eta^{\mu\nu}X_\nu$, and confirm you recover $X^\mu$. Verify $X_\mu X^\mu = X\cdot X$.
2. Prove the identity $\eta^{\mu\rho}\eta_{\rho\nu} = \delta^\mu{}_\nu$ from $\eta = \mathrm{diag}(1,-1,-1,-1)$, and explain why this is exactly the statement that raising and lowering are inverse operations.
3. Distinguish the **dual basis** $e^\mu$ (defined by $\langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu$) from the **metric dual** of a basis vector $\underline{e}_\mu = \Phi_g(e_\mu) = g(e_\mu, \cdot)$. Show $\langle\underline{e}_\mu, e_\nu\rangle = \eta_{\mu\nu} \neq \delta_{\mu\nu}$, so the two are *not* the same, and find the relation $\underline{e}_\mu = \eta_{\mu\nu}e^\nu$ between them.

**Recall:**

![[Def - Metric Duality and Index Manipulation#The Definition]]

A [[Def - Four-Vector|four-vector]] $X^\mu$ has its index lowered by $\eta$ to give a [[Def - Metric Duality and Index Manipulation|linear form]] $X_\mu = \eta_{\mu\nu}X^\nu$. The dual basis satisfies $\langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu$. The musical isomorphism $\Phi_g$ sends $X \mapsto g(X,\cdot)$.

---

# Convergent Strategy

**Problem class.** An *index-calculus verification* — confirm the mechanics of raising and lowering, and pin down the dual-basis-versus-metric-dual distinction that is the classic source of confusion. The [[Special Relativity III — Minkowski Spacetime and the Metric#Problem-Solving Strategy|topic strategy]] notes that index expressions are controlled by "one $\eta$ per index, contracted indices once up once down".

**Assumption pattern.** Explicit components plus the orthonormal $\eta$. The recognition step is that lowering flips the spatial signs in our signature, and that the inverse metric is needed to raise back.

**Theorem routing.** Part 1 is direct application of $\eta$. Part 2 is a one-line matrix computation, $\eta^{-1}\eta = I$, reinterpreted as $\flat$ and $\sharp$ being inverse ([[Def - Metric Duality and Index Manipulation|non-degeneracy]]). Part 3 contrasts the metric-free dual basis with the metric dual, using $\langle\underline{e}_\mu, e_\nu\rangle = g(e_\mu,e_\nu) = \eta_{\mu\nu}$.

**Key decision point.** The crux of part 3 is that the dual basis is defined *combinatorially* (Kronecker delta) while the metric dual uses $g$, so they coincide only if $\eta = I$ — which it is not. Conflating them is the standard error; the decision is to keep "the form that reads off the $\mu$-th component" ($e^\mu$) separate from "the form $g$-dual to $e_\mu$" ($\underline{e}_\mu$).

---

# Legal Operations Used

1. **Operation 4 (lower and raise indices with $\eta$):** the core of parts 1 and 3.

2. **Operation 2 (compute the scalar product by the Minkowski matrix):** $X\cdot X$ and the verification $X_\mu X^\mu = X\cdot X$.

3. **Illegal-but-tempting operation 4 (copying components unchanged when lowering):** this exercise shows the correct rule $X_i = -X^i$ and the check that detects the error.

---

# Hints

> [!note]- Hint 1
> Lower: $X_0 = \eta_{00}X^0 = +X^0 = 5$; $X_i = \eta_{ii}X^i = -X^i$, so $X_1 = -3$, $X_2 = +2$, $X_3 = 0$. Thus $X_\mu = (5,-3,2,0)$. Raise back with $\eta^{\mu\nu}$ (same diagonal) and the signs flip again, returning $X^\mu = (5,3,-2,0)$.

> [!note]- Hint 2
> $X_\mu X^\mu = (5)(5) + (-3)(3) + (2)(-2) + (0)(0) = 25 - 9 - 4 + 0 = 12$. Compare $X\cdot X = 25 - 9 - 4 - 0 = 12$. They agree — the contraction $X_\mu X^\mu$ equals the scalar square.

> [!note]- Hint 3
> $\eta^{\mu\rho}\eta_{\rho\nu}$: both factors are $\mathrm{diag}(1,-1,-1,-1)$, so their product is $\mathrm{diag}(1,1,1,1) = \delta^\mu{}_\nu$ (each diagonal entry squares to $+1$). This says applying $\flat$ then $\sharp$ is the identity.

> [!note]- Hint 4
> For part 3: $\langle\underline{e}_\mu, e_\nu\rangle = g(e_\mu, e_\nu) = \eta_{\mu\nu}$ by definition of the metric dual, whereas $\langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu$. Since $\eta_{\mu\nu} \neq \delta_{\mu\nu}$ (the spatial entries are $-1$, not $+1$), $\underline{e}_\mu \neq e^\mu$. To find the relation, write $\underline{e}_\mu = c_{\mu\nu}e^\nu$ and contract with $e_\rho$: $c_{\mu\rho} = \eta_{\mu\rho}$, so $\underline{e}_\mu = \eta_{\mu\nu}e^\nu$.

---

# Solution

Lowering flips spatial signs, raising flips them back, and the dual basis is metric-free while the metric dual carries $\eta$. Step 1 does the explicit raise/lower; Step 2 proves the inverse identity; Step 3 separates the two notions of "dual".

**Step 1: lower, raise back, and check the contraction.**

> [!note]- Derivation
> Lower with $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$: $X_0 = X^0 = 5$, $X_1 = -X^1 = -3$, $X_2 = -X^2 = +2$, $X_3 = -X^3 = 0$. So
> $$X_\mu = (5, -3, 2, 0).$$
> Raise back with $\eta^{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$: $X^0 = X_0 = 5$, $X^1 = -X_1 = 3$, $X^2 = -X_2 = -2$, $X^3 = -X_3 = 0$, recovering $X^\mu = (5,3,-2,0)$ — the round trip $\flat$ then $\sharp$ is the identity. Now the contraction:
> $$X_\mu X^\mu = (5)(5) + (-3)(3) + (2)(-2) + (0)(0) = 25 - 9 - 4 = 12,$$
> which equals $X\cdot X = (5)^2 - (3)^2 - (-2)^2 - 0 = 25 - 9 - 4 = 12$. The contraction of a vector with its lowered form is the scalar square — the calibration check that lowering was done correctly. (Had one wrongly set $X_\mu = X^\mu$, the contraction would give $25 + 9 + 4 = 38$, the Euclidean square, flagging the error.)

**Step 2: $\eta^{\mu\rho}\eta_{\rho\nu} = \delta^\mu{}_\nu$ and the inverse property.**

> [!note]- Derivation
> Both $\eta^{\mu\rho}$ and $\eta_{\rho\nu}$ are the diagonal matrix $\mathrm{diag}(1,-1,-1,-1)$. Their matrix product has $(\mu,\nu)$ entry $\sum_\rho \eta^{\mu\rho}\eta_{\rho\nu}$, which for a diagonal matrix is $\eta^{\mu\mu}\eta_{\mu\nu}$ (no sum) $= (\eta_{\mu\mu})^2\delta_{\mu\nu}$. Each diagonal entry squares to $+1$: $(+1)^2 = 1$ and $(-1)^2 = 1$. So the product is $\mathrm{diag}(1,1,1,1) = \delta^\mu{}_\nu$:
> $$\eta^{\mu\rho}\eta_{\rho\nu} = \delta^\mu{}_\nu.$$
> This *is* the statement that raising and lowering are inverse: lowering $X^\nu \mapsto X_\rho = \eta_{\rho\nu}X^\nu$ then raising $X_\rho \mapsto \eta^{\mu\rho}X_\rho = \eta^{\mu\rho}\eta_{\rho\nu}X^\nu = \delta^\mu{}_\nu X^\nu = X^\mu$ returns the original. By [[Def - Metric Duality and Index Manipulation|non-degeneracy]], $\eta$ is invertible, $\eta^{\mu\nu}$ is its inverse, and the musical isomorphisms $\flat = \Phi_g$, $\sharp = \Phi_g^{-1}$ are mutually inverse maps $E \leftrightarrow E^*$.

**Step 3: dual basis versus metric dual.**

> [!note]- Derivation
> The **dual basis** $(e^\mu)$ is defined purely by the pairing $\langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu$ — the form $e^\mu$ reads off the $\mu$-th component of a vector, no metric involved. The **metric dual** of the basis vector $e_\mu$ is $\underline{e}_\mu := \Phi_g(e_\mu) = g(e_\mu, \cdot)$, a form built using $g$. Their pairings differ:
> $$\langle\underline{e}_\mu, e_\nu\rangle = g(e_\mu, e_\nu) = \eta_{\mu\nu}, \qquad \langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu.$$
> Since $\eta_{\mu\nu} \neq \delta_{\mu\nu}$ — the spatial diagonal entries are $-1$, not $+1$ — we have $\underline{e}_\mu \neq e^\mu$ (Gourgoulhon's Remark 1.16). To relate them, expand $\underline{e}_\mu = c_{\mu\nu}e^\nu$ in the dual basis and pair with $e_\rho$:
> $$\eta_{\mu\rho} = \langle\underline{e}_\mu, e_\rho\rangle = c_{\mu\nu}\langle e^\nu, e_\rho\rangle = c_{\mu\nu}\delta^\nu{}_\rho = c_{\mu\rho},$$
> so $c_{\mu\nu} = \eta_{\mu\nu}$ and
> $$\underline{e}_\mu = \eta_{\mu\nu}\,e^\nu.$$
> Concretely, $\underline{e}_0 = e^0$ (since $\eta_{00} = +1$) but $\underline{e}_i = -e^i$ (since $\eta_{ii} = -1$): the metric dual of a spatial basis vector is *minus* the corresponding dual-basis form. This is the basis-level shadow of "lowering flips spatial signs", and confusing $\underline{e}_\mu$ with $e^\mu$ silently drops the metric.

> [!note]- Complete formal solution
> *Part 1.* $X_\mu = \eta_{\mu\nu}X^\nu = (5,-3,2,0)$; raising back, $\eta^{\mu\nu}X_\nu = (5,3,-2,0) = X^\mu$. Contraction $X_\mu X^\mu = 25 - 9 - 4 = 12 = X\cdot X$. *Part 2.* $\eta^{\mu\rho}\eta_{\rho\nu} = \mathrm{diag}(1,-1,-1,-1)^2 = \mathrm{diag}(1,1,1,1) = \delta^\mu{}_\nu$, which says $\sharp\circ\flat = \mathrm{id}$; non-degeneracy makes $\eta$ invertible with inverse $\eta^{\mu\nu}$. *Part 3.* $\langle\underline{e}_\mu, e_\nu\rangle = g(e_\mu,e_\nu) = \eta_{\mu\nu} \neq \delta_{\mu\nu} = \langle e^\mu, e_\nu\rangle$, so $\underline{e}_\mu \neq e^\mu$; expanding and pairing gives $\underline{e}_\mu = \eta_{\mu\nu}e^\nu$, i.e. $\underline{e}_0 = e^0$, $\underline{e}_i = -e^i$. $\blacksquare$

---

# Key Takeaways

**Lowering flips the spatial signs, raising flips them back, and the contraction $X_\mu X^\mu = X\cdot X$ is the check that you did it right.** The mechanical content of metric duality in our signature is "time component unchanged, space components flip sign": $X_0 = X^0$, $X_i = -X^i$. The single most common error in all of relativistic computation is to copy components unchanged when changing index height, silently dropping three minus signs; the diagnostic that catches it is to verify $X_\mu X^\mu$ equals the scalar square $(X^0)^2 - |\mathbf{X}|^2$, since the wrong rule gives the Euclidean $(X^0)^2 + |\mathbf{X}|^2$ instead. The trigger to apply $\eta$ explicitly: any time an equation has indices that do not match up-and-down, or any time a vector must become a form (or vice versa). The reusable rule is "one $\eta$ per index, contracted indices once up once down", and the contraction check is free insurance against sign errors.

**Raising and lowering are inverse because $\eta\eta^{-1} = I$, and that one identity is the non-degeneracy of the metric in action.** The relation $\eta^{\mu\rho}\eta_{\rho\nu} = \delta^\mu{}_\nu$ underlies every index manipulation: it is what makes $\flat$ and $\sharp$ mutually inverse, what lets double contractions collapse, and what guarantees the round trip "lower then raise" returns the original vector. Structurally it is the statement that the [[Def - Metric Duality and Index Manipulation|metric is non-degenerate]] — its matrix is invertible — which is exactly the condition that the vector-to-form map $\Phi_g$ is an isomorphism. The transferable lesson: whenever a tensor expression contains $\eta^{\mu\rho}\eta_{\rho\nu}$ (or $g^{\mu\rho}g_{\rho\nu}$ in the curved case), replace it by $\delta^\mu{}_\nu$ and simplify; this contraction is the workhorse identity of index gymnastics, and recognising it on sight is what makes long tensor calculations tractable.

**The dual basis is metric-free; the metric dual carries $\eta$ — and conflating them is the subtle error that drops the metric.** The pitfall this exercise isolates is that "the dual of a basis vector" is ambiguous: the *dual basis* $e^\mu$ (defined by the Kronecker pairing, no metric) and the *metric dual* $\underline{e}_\mu = g(e_\mu,\cdot)$ are different objects, related by $\underline{e}_\mu = \eta_{\mu\nu}e^\nu$, so $\underline{e}_i = -e^i$ for spatial indices. Gourgoulhon flags this (Remark 1.16) precisely because it is easy to assume they coincide — which they do only in a Euclidean orthonormal basis where $\eta = I$. The diagnostic: whenever you read "the dual basis" in a relativistic context, ask whether it is the combinatorial dual (no metric) or the metric dual (with $\eta$); the index calculus is consistent only if the metric is applied exactly once per index height change, never silently absorbed into a "dual" that secretly used $g$.
