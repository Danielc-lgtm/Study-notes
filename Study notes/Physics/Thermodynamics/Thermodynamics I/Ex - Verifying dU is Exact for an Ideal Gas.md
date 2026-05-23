---
type: exercise
subject: thermodynamics
difficulty: "⭐"
prereqs:
  - "Def - The First Law of Thermodynamics"
  - "Def - Closed and Exact Forms"
tags: [physics, thermodynamics, ideal-gas]
---

# Problem Statement

For a simple ideal gas with $U = (f/2) nRT$ and equation of state $pV = nRT$, verify that:

1. The differential $dU$ is an exact 1-form on the state space $M = \{(V, T) : V, T > 0\}$.
2. The integral $\int_\gamma dU$ along any path $\gamma$ from $(V_i, T_i)$ to $(V_f, T_f)$ depends only on the endpoints.
3. Around a closed cycle $\gamma$, $\oint dU = 0$, illustrating that $U$ is a state function.

**Recall:**

The [[Def - The First Law of Thermodynamics|first law of thermodynamics]] asserts $dU$ is exact: $U$ is a globally defined function on $M$ and $dU$ is its differential. The 1-form $dU = (f/2)nR\, dT$ for an ideal gas (since $U$ depends only on $T$).

A 1-form $\omega = a\, dV + b\, dT$ is [[Def - Closed and Exact Forms|exact]] iff there exists a function $\Phi$ with $\omega = d\Phi$, equivalently (on $\mathbb{R}^2$) iff $\omega$ is closed: $\partial a/\partial T = \partial b/\partial V$.

---

# Convergent Strategy

**Problem class:** This is a direct-verification problem of the type "show a given 1-form is exact". The recurring pattern: express the 1-form in coordinates, check the closed-iff-exact criterion (cross-partials), then integrate along any convenient path and verify the answer depends only on endpoints.

**Assumption pattern:** $U(T) = (f/2) nRT$ depends only on $T$ for an ideal gas — this is the substantive fact, derivable from the kinetic theory or imposed as an empirical property. Once $U$ is a function on $M$, $dU$ is automatically exact.

**Theorem routing:** Exactness of $dU$ is the content of the first law of thermodynamics. The cross-partial test and the path-independence test are two ways to verify this on a specific example.

**Key decision point:** The non-obvious observation is that for an ideal gas $U$ depends *only* on $T$, not on $V$. This is a special feature of ideal gases (Joule's law), not a consequence of the first law alone. For real gases $U = U(T, V)$ depends on both, and $dU = (\partial U/\partial T)_V\, dT + (\partial U/\partial V)_T\, dV$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (split a 1-form using the first law).** Identify $dU$ as the exact part of $\delta Q - \delta W$.

2. **Operation 8 from the topic page (test exactness via cross-partials).** Check $\partial a/\partial T = \partial b/\partial V$ for the candidate $dU$ in coordinates.

---

# Hints

> [!note]- Hint 1
> Write $dU$ in $(V, T)$ coordinates: $U = (f/2)nRT$ has no $V$-dependence, so $dU = (f/2)nR\, dT$. The coefficient of $dV$ is 0, the coefficient of $dT$ is $(f/2)nR$.

> [!note]- Hint 2
> Check exactness via cross-partials: $\partial(0)/\partial T = 0$ and $\partial((f/2)nR)/\partial V = 0$. Both zero, so they agree — $dU$ is closed, hence exact on the 2-manifold.

> [!note]- Hint 3
> Path-independence: along *any* path $\gamma$ from $(V_i, T_i)$ to $(V_f, T_f)$,
> $$\int_\gamma dU = U(V_f, T_f) - U(V_i, T_i) = (f/2)nR(T_f - T_i).$$
> The answer depends only on the temperature endpoints, not on the path.

---

# Solution

The proof is direct verification in three steps. Step 1 writes $dU$ explicitly. Step 2 verifies exactness via the cross-partial criterion. Step 3 verifies path-independence by integrating $dU$ along two different paths and confirming agreement.

**Step 1: $dU = (f/2) nR\, dT$.**

> [!note]- Derivation
> $U(V, T) = (f/2) nRT$ depends only on $T$ (Joule's law for ideal gas). So $dU = (\partial U/\partial V)_T\, dV + (\partial U/\partial T)_V\, dT = 0 \cdot dV + (f/2)nR\, dT = (f/2)nR\, dT$.

**Step 2: $dU$ is exact (= closed on the 2-manifold).**

> [!note]- Derivation
> Write $dU = a\, dV + b\, dT$ with $a = 0$ and $b = (f/2)nR$. Cross-partials: $\partial a/\partial T = 0$ and $\partial b/\partial V = 0$. They agree, so $dU$ is closed. On the simply connected 2-manifold $M = \{(V, T) : V, T > 0\}$, closed = exact (Poincaré lemma), confirming $dU = dU$ for the function $U = (f/2)nRT$.

**Step 3: $\int_\gamma dU = U(\gamma(1)) - U(\gamma(0))$ along any path.**

> [!note]- Derivation
> Compare two paths from $(V_1, T_1)$ to $(V_2, T_2)$:
>
> *Path A: isobar then isochore.* First go at constant $p_1$ from $(V_1, T_1)$ to $(V_2, T_2')$ where $T_2'$ is determined by $p_1 V_2 = nR T_2'$; then at constant $V_2$ from $T_2'$ to $T_2$.
>
> *Path B: isochore then isobar.* First go at constant $V_1$ from $T_1$ to $T_2''$ where $p_2 V_1 = nR T_2''$; then at constant $p_2$ from $(V_1, T_2'')$ to $(V_2, T_2)$.
>
> Along any path:
> $$\int_\gamma dU = \int_\gamma (f/2)nR\, dT = (f/2)nR \int_\gamma dT.$$
> Since $\int_\gamma dT = T_2 - T_1$ for any path (because $T$ is the integrated coordinate function), the integral is $(f/2)nR(T_2 - T_1) = U(V_2, T_2) - U(V_1, T_1)$ — same for both paths. So $dU$ is path-independent.
>
> Around any closed cycle, $\oint dU = U(\gamma(1)) - U(\gamma(0)) = 0$ since $\gamma(1) = \gamma(0)$.

> [!note]- Complete formal solution
> *Step 1:* $U = (f/2)nRT$ depends only on $T$, so $dU = (f/2)nR\, dT$.
>
> *Step 2:* Cross-partial test: $\partial(0)/\partial T = \partial((f/2)nR)/\partial V = 0$. Equal, so $dU$ is closed, hence exact on the 2-manifold $M$.
>
> *Step 3:* For any path $\gamma$ from $(V_1, T_1)$ to $(V_2, T_2)$, $\int_\gamma dU = (f/2)nR(T_2 - T_1)$, which depends only on endpoints. For a closed cycle, $\oint dU = 0$.

---

# Key Takeaways

**$dU$ is exact ⟺ $U$ is a state function ⟺ the first law of thermodynamics holds.** The cross-partial verification in this exercise is the *simplest* possible test of the first law on an ideal gas. For more complex substances (Van der Waals, real solids, magnetic systems), the verification is analogous: write $dU$ in natural coordinates, check exactness via cross-partials of the coefficients. This always works because the first law *postulates* the existence of $U$ as a state function. The exercise is a sanity check that the ideal-gas formulae are consistent with this postulate.

**The contrast with $\delta Q$ and $\delta W$ is the substantive content.** Both $\delta Q$ and $\delta W$ for an ideal gas have nonzero cross-partial differences (see [[Ex - The Heat 1-Form for an Ideal Gas]]), so neither is exact. Yet their difference $\delta Q - \delta W = dU$ is exact. This is the geometric structure underlying the first law: out of three Pfaffians ($dU, \delta Q, \delta W$), only one is exact, and the other two combine algebraically to recover it. Recognising this asymmetry — exact differential of a state function plus two non-exact transit forms — is the conceptual content of the first law.

**Ideal-gas $U$ depending only on $T$ is a special property called Joule's law.** For a general gas $U = U(T, V)$ depends on both temperature and volume. Joule verified experimentally for *ideal* gases that $(\partial U/\partial V)_T = 0$ — the internal energy is independent of volume at fixed temperature, since ideal-gas molecules have no intermolecular forces. For real gases, $(\partial U/\partial V)_T \neq 0$ and a Joule free-expansion gives a small temperature change (the **Joule coefficient** $(\partial T/\partial V)_U$), measurable in delicate experiments. This is one of the two key thermodynamic differences between real and ideal gases (the other being the Joule-Thomson coefficient).
