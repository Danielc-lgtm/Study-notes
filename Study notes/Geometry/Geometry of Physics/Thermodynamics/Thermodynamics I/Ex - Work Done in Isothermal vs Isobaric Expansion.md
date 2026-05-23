---
type: exercise
subject: thermodynamics
difficulty: "⭐"
prereqs:
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - The First Law of Thermodynamics"
tags: [physics, thermodynamics, ideal-gas]
---

# Problem Statement

A simple ideal gas of $n$ moles undergoes a quasistatic expansion from state $A = (V_1, T_1)$ to state $B = (V_2, T_2)$, with $V_2 > V_1$.

1. Compute the work $W$ done by the gas along an **isothermal** path: $T = T_1$ constant throughout. Assume $T_1 = T_2$ for this path (so the path is genuinely isothermal).
2. Compute the work $W$ done by the gas along an **isobaric** path: $p$ constant throughout. Determine the relation between $T_1, T_2, V_1, V_2$ for an isobaric path to exist.
3. Compute the work along a **two-leg path**: first isothermal at $T_1$ from $V_1$ to $V_2$, then isochoric at $V_2$ from $T_1$ to $T_2$. Verify the result differs from the single-leg paths, illustrating path-dependence.
4. Verify that $\Delta U = U(B) - U(A)$ is the same for all paths, illustrating that internal energy is a state function.

**Recall:**

The [[Def - Heat 1-Form and Work 1-Form|work 1-form]] for a simple gas is $\delta W = p\, dV$. For an ideal gas $p = nRT/V$.

The [[Def - The First Law of Thermodynamics|first law]]: $dU = \delta Q - \delta W$, with $dU$ exact.

For an ideal gas, $U = (f/2) nRT$ depends only on $T$.

---

# Convergent Strategy

**Problem class:** A direct-computation problem of the type "compute the line integral of a 1-form along a specified path". The recurring pattern: parametrise each leg of the path, evaluate the integrand $\delta W = p\, dV$ in coordinates, integrate.

**Assumption pattern:** Quasistatic processes (paths in $M$). The two specific path types (isothermal, isobaric) are chosen to make the integral elementary. The contrast in answers illustrates path-dependence of work.

**Theorem routing:** Direct integration of $\int p\, dV$ along each parametrised path. For isothermal paths, $p = nRT_1/V$; for isobaric, $p$ is constant. For the two-leg path, integrate separately along each leg and sum.

**Key decision point:** The non-obvious choice is to *also* compute $\Delta U$ to demonstrate that even though work is path-dependent, the state function $U$ is not — this is the experimental content of the first law.

---

# Legal Operations Used

1. **Operation 3 from the topic page (restrict a 1-form to a process).** Along each leg, $\delta W = p(V, T)\, dV$ specialises to an ordinary integral once the path is parametrised.

2. **Operation 1 from the topic page (split using the first law).** Verifying $\Delta U$ is path-independent uses $\Delta U = U(B) - U(A) = (f/2)nR(T_2 - T_1)$ regardless of path.

---

# Hints

> [!note]- Hint 1
> For the isothermal path: along $T = T_1$, $p = nRT_1/V$. So $\delta W = (nRT_1/V)\, dV$, and
> $$W_{\text{iso-T}} = \int_{V_1}^{V_2} \frac{nRT_1}{V}\, dV = nRT_1 \log(V_2/V_1).$$

> [!note]- Hint 2
> For the isobaric path: $p$ constant, so $\delta W = p\, dV = p(V_2 - V_1)$. But for an ideal gas, $p$ constant and $V$ changing means $T$ changes too: $pV_1 = nRT_1$ and $pV_2 = nRT_2$. So an isobaric path from $(V_1, T_1)$ to $(V_2, T_2)$ exists iff $V_2/V_1 = T_2/T_1$ (both ratios equal $p/p = 1$ implies they are equal). The work is $W_{\text{iso-p}} = p(V_2 - V_1) = nR(T_2 - T_1)$.

> [!note]- Hint 3
> For the two-leg path: first leg isothermal at $T_1$ from $V_1$ to $V_2$ gives $W_1 = nRT_1 \log(V_2/V_1)$ as in Hint 1. Second leg isochoric at $V_2$ from $T_1$ to $T_2$ has $dV = 0$, so $\delta W = p\, dV = 0$, and $W_2 = 0$. Total work: $W_{\text{two-leg}} = nRT_1 \log(V_2/V_1) + 0$.

> [!note]- Hint 4
> Compare to the isobaric work: $nR(T_2 - T_1)$ versus $nRT_1 \log(V_2/V_1)$ from the two-leg path. These are not equal in general — work depends on the path even though endpoints are the same.

---

# Solution

The proof is direct computation of three line integrals. Step 1 evaluates the isothermal work. Step 2 evaluates the isobaric work (requiring $V_2/V_1 = T_2/T_1$ for consistency). Step 3 evaluates the two-leg path. Step 4 verifies that $\Delta U$ is independent of path. The non-obvious comparison is the direct numerical inequality of the work integrals — illustrating that $\delta W$ is not exact.

**Step 1: Isothermal work $W_{\text{iso-T}} = nRT_1 \log(V_2/V_1)$.**

> [!note]- Derivation
> Along the isothermal path $T = T_1$, $p = nRT_1/V$. So $\delta W = (nRT_1/V)\, dV$:
> $$W_{\text{iso-T}} = \int_{V_1}^{V_2} \frac{nRT_1}{V}\, dV = nRT_1 \log\frac{V_2}{V_1}.$$

**Step 2: Isobaric work $W_{\text{iso-p}} = nR(T_2 - T_1)$, requires $V_2/V_1 = T_2/T_1$.**

> [!note]- Derivation
> Along an isobaric path at constant $p$, $V$ changing from $V_1$ to $V_2$ requires $T$ changing from $T_1$ to $T_2$ via $pV = nRT$: $T_i = pV_i/(nR)$, so $T_2/T_1 = V_2/V_1$ (consistency requirement).
> $$W_{\text{iso-p}} = \int_{V_1}^{V_2} p\, dV = p(V_2 - V_1) = nR T_1 (V_2/V_1 - 1) = nR(T_2 - T_1).$$

**Step 3: Two-leg path work $W_{\text{two-leg}} = nRT_1 \log(V_2/V_1) + 0$.**

> [!note]- Derivation
> *Leg 1 (isothermal at $T_1$, $V_1 \to V_2$):* $W_1 = nRT_1 \log(V_2/V_1)$ as in Step 1.
>
> *Leg 2 (isochoric at $V_2$, $T_1 \to T_2$):* $dV = 0$ along this leg, so $\delta W = p\, dV = 0$ identically, and $W_2 = 0$.
>
> Total: $W_{\text{two-leg}} = nRT_1 \log(V_2/V_1)$. Note this differs from the isobaric work $nR(T_2 - T_1)$ in general — and from any other path's work too.

**Step 4: $\Delta U = (f/2) nR(T_2 - T_1)$ is path-independent.**

> [!note]- Derivation
> Since $U = (f/2)nRT$ depends only on $T$, $\Delta U = U(T_2) - U(T_1) = (f/2)nR(T_2 - T_1)$. This depends only on the endpoint temperatures, not on the path. By the first law, $\Delta Q = \Delta U + W$ along each path: different paths give different $W$, hence different $\Delta Q$, but the same $\Delta U$.

> [!note]- Complete formal solution
> *Step 1 (isothermal):* $W_{\text{iso-T}} = \int_{V_1}^{V_2} (nRT_1/V)\, dV = nRT_1 \log(V_2/V_1)$.
>
> *Step 2 (isobaric):* Requires $V_2/V_1 = T_2/T_1$; $W_{\text{iso-p}} = p(V_2 - V_1) = nR(T_2 - T_1)$.
>
> *Step 3 (two-leg):* First leg gives $nRT_1 \log(V_2/V_1)$, second leg (isochoric) gives 0. Total: $nRT_1 \log(V_2/V_1)$, differing from the isobaric answer.
>
> *Step 4 ($\Delta U$):* Path-independent, $\Delta U = (f/2)nR(T_2 - T_1)$. Confirms first law's content that $U$ is a state function.

---

# Key Takeaways

**Work is a transit quantity, not a state function — the integrals differ on different paths between the same endpoints.** The three paths in this exercise produce three different values for the work $W$, while the endpoint difference $\Delta U$ is the same. This is the experimental content of the first law: $U$ is a state function (path-independent), $W$ is not (path-dependent). The trigger-reaction pattern is "want $W$ → must specify the path completely". For an ideal gas, isothermal expansion gives $nRT \log(V_2/V_1)$; isobaric gives $p \Delta V$; adiabatic gives $-\Delta U$; isochoric gives $0$. Memorising these special-case formulae speeds up cycle-efficiency computations dramatically.

**Isothermal work for an ideal gas is the logarithm of the volume ratio.** The form $W = nRT \log(V_2/V_1)$ is the most-used formula in elementary gas thermodynamics. It appears in: Carnot cycle isothermal legs; reversible expansion against a heat reservoir; chemical-potential differences for ideal solutions ($\mu_2 - \mu_1 = RT \log(c_2/c_1)$, same logarithmic structure). The $\log$ comes from the ideal-gas $p \propto 1/V$ scaling; for non-ideal gases the integral is modified by the equation-of-state corrections (Van der Waals, virial expansion). Recognising the $\log$-of-ratio structure points to ideal-gas behaviour and isothermal processes.

**Isobaric and isochoric processes are computationally trivial; isothermal and adiabatic require integration.** The four "elementary" thermodynamic processes split into two computationally easy ones (isobaric: $W = p\Delta V$; isochoric: $W = 0$) and two requiring an actual integral (isothermal and adiabatic). The Carnot cycle uses only isothermal and adiabatic legs — exactly the harder ones; the Otto and Diesel cycles use isochoric and isobaric legs together with adiabatics — mixing easy and hard. Recognising the computational cost of each process type helps anticipate which cycles will yield clean closed-form efficiencies (Carnot does; Otto and Diesel give algebraic formulae too, but more complicated).
