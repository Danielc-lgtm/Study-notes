---
type: exercise
subject: thermodynamics
difficulty: "⭐⭐"
prereqs:
  - "Def - Absolute Temperature and Entropy"
  - "Def - The First Law of Thermodynamics"
  - "Def - Quasistatic Process"
tags: [physics, thermodynamics, ideal-gas, entropy, irreversibility]
---

# Problem Statement

A gas of $n$ moles of an ideal gas is enclosed in chamber $A$ of volume $V_1$, with an evacuated chamber $B$ of volume $V_2 - V_1$ connected via a valve. The walls are insulating. At time $t = 0$ the valve is opened. The gas rushes irreversibly into chamber $B$, eventually filling both with total volume $V_2 > V_1$.

1. Compute the change in internal energy $\Delta U$ during the free expansion.
2. Compute the change in temperature $\Delta T$.
3. Compute the change in entropy $\Delta S$ between initial and final equilibrium states.
4. Verify the second-law inequality $\Delta S \geq 0$ for this adiabatic (no heat exchanged with environment) but irreversible process, and identify it as a strict inequality.

**Recall:**

[[Def - The First Law of Thermodynamics|First law]]: $\Delta U = Q - W$ between equilibrium states. For an insulated container with no piston motion against external pressure, $Q = 0$ and $W = 0$ (no work is done against zero external pressure during free expansion).

[[Def - Absolute Temperature and Entropy|Second law]]: $\Delta S \geq 0$ for any process in a thermally isolated system, with equality iff reversible. Even for non-quasistatic processes, $\Delta S$ is computed as a state-function difference using $dS = \delta Q_{\text{rev}}/T$ along *any* reversible path between the same endpoints.

For an ideal gas, $S = (f/2) nR \log T + nR \log V + \text{const}$ (see [[Ex - Compute the Entropy of an Ideal Gas]]). Internal energy $U = (f/2) nRT$ depends only on $T$.

---

# Convergent Strategy

**Problem class:** A state-function-difference problem in the presence of an irreversible process. The recurring pattern: (i) observe that initial and final states are equilibrium states (in $M$), so state-function differences are well-defined; (ii) compute those differences using *any* convenient reversible path connecting the same endpoints, since the state-function is path-independent; (iii) interpret the result via the second-law inequality.

**Assumption pattern:** Free expansion is *adiabatic* (no heat exchanged with environment, insulated container) and *involves no external work* (the gas expands into vacuum, so the external pressure is zero). Both Q and W with the environment are zero. The process is *not quasistatic* (intermediate states are not in $M$).

**Theorem routing:** The first law gives $\Delta U = Q - W = 0 - 0 = 0$. For an ideal gas, $\Delta U = 0$ forces $\Delta T = 0$ (since $U$ depends only on $T$). For $\Delta S$, use the explicit formula $S(T, V)$: at constant $T$, $\Delta S = nR \log(V_2/V_1) > 0$. The result is positive entropy change, consistent with the second-law inequality, with strict inequality reflecting irreversibility.

**Key decision point:** The non-obvious choice is to compute $\Delta S$ using the *state-function formula*, *not* by integrating $\int \delta Q_{\text{actual}}/T$ — the actual process exchanges $Q_{\text{actual}} = 0$ with the environment, which would naively give $\Delta S = 0$. The point is that $\Delta S$ for the system depends only on the endpoint states, *not* on the actual process; the formula $\Delta S = \int \delta Q_{\text{rev}}/T$ requires a *reversible* substitute path between the same endpoints (here: isothermal expansion).

---

# Legal Operations Used

1. **Operation 1 from the topic page (split a 1-form using the first law).** The first law applied between endpoints (with $Q = W = 0$) gives $\Delta U = 0$ without integrating along the irreversible path.

2. **Operation 7 from the topic page (bound entropy change for irreversible processes).** Compute $\Delta S$ as the state-function difference, and verify $\Delta S \geq 0$ for the adiabatic isolated process. The inequality is strict because the process is irreversible.

3. **Operation 8 from the topic page (recognise state function via path-independence).** Entropy is a state function: $\Delta S$ depends only on initial and final states, not on the irreversible path.

---

# Hints

> [!note]- Hint 1
> For the first law applied to the system: $Q = 0$ (insulated container), $W = 0$ (gas does no work on the vacuum). So $\Delta U = Q - W = 0$. The first law applies between equilibrium states even for non-quasistatic processes.

> [!note]- Hint 2
> For an ideal gas, $U = (f/2)nRT$ depends only on $T$. So $\Delta U = 0$ implies $\Delta T = 0$ — the gas has the same temperature after free expansion as before.

> [!note]- Hint 3
> Entropy is a state function: $\Delta S$ depends only on initial and final equilibrium states, not on the actual (irreversible) path. Use the formula $S = (f/2) nR \log T + nR \log V + \text{const}$. At constant $T$ (initial and final), $\Delta S = nR (\log V_2 - \log V_1) = nR \log(V_2/V_1)$.

> [!note]- Hint 4
> Since $V_2 > V_1$, $\log(V_2/V_1) > 0$, so $\Delta S > 0$. This is consistent with the second law $\Delta S \geq 0$ for adiabatic isolated processes, with strict inequality reflecting irreversibility.
>
> The fictitious *reversible* substitute path that would give the same $\Delta S$: isothermal expansion at the (constant) temperature $T$, against a piston with infinitesimally slow motion. Along this reversible path, the heat absorbed from a reservoir is $Q_{\text{rev}} = nRT \log(V_2/V_1) = T \Delta S$ — nonzero, in contrast to the $Q_{\text{actual}} = 0$ of the real irreversible process.

---

# Solution

The proof is in four short steps. Step 1 applies the first law between endpoints. Step 2 uses Joule's law for an ideal gas to get $\Delta T = 0$. Step 3 uses the entropy formula to compute $\Delta S$. Step 4 verifies the second-law inequality. The non-obvious move is in Step 3, where the entropy change is computed via the state-function formula despite the actual process being irreversible — illustrating that $\Delta S$ for the system is *not* the integral of $\delta Q_{\text{actual}}/T$ (which would give zero for this adiabatic process).

**Step 1: $\Delta U = 0$.**

> [!note]- Derivation
> The container is thermally insulated: $Q_{\text{actual}} = 0$ (no heat from environment). The gas expands into vacuum: $W_{\text{actual}} = \int p_{\text{ext}}\, dV = 0$ since $p_{\text{ext}} = 0$ (vacuum exerts no resistance).
>
> By the first law between equilibrium endpoints: $\Delta U = U(V_2, T_2) - U(V_1, T_1) = Q - W = 0$. So $U$ is unchanged.

**Step 2: $\Delta T = 0$ for an ideal gas.**

> [!note]- Derivation
> For an ideal gas $U = (f/2) nRT$ depends only on $T$. So $\Delta U = (f/2) nR (T_2 - T_1) = 0$ forces $T_2 = T_1$.
>
> Note: this is special to ideal gases. For real gases (Van der Waals, etc.) $U = U(T, V)$ depends on volume too, and $\Delta U = 0$ does not force $\Delta T = 0$ — leading to the **Joule coefficient** $(\partial T/\partial V)_U$, nonzero for real gases.

**Step 3: $\Delta S = nR \log(V_2/V_1) > 0$.**

> [!note]- Derivation
> Use the entropy formula $S(T, V) = (f/2) nR \log T + nR \log V + \text{const}$. At constant $T$:
> $$\Delta S = S(T, V_2) - S(T, V_1) = nR \log V_2 - nR \log V_1 = nR \log(V_2/V_1).$$
> Since $V_2 > V_1$, $\Delta S > 0$.
>
> **Alternative computation via reversible substitute path:** Consider the reversible *isothermal* expansion at temperature $T = T_1 = T_2$ from $V_1$ to $V_2$. Along this path, $dU = 0$ (ideal gas), so $\delta Q_{\text{rev}} = \delta W_{\text{rev}} = (nRT/V)\, dV$. Integrating: $Q_{\text{rev}} = nRT \log(V_2/V_1)$. Then $\Delta S = \int dS = \int \delta Q_{\text{rev}}/T = Q_{\text{rev}}/T = nR \log(V_2/V_1)$. Same answer — confirming that the state-function $\Delta S$ depends only on endpoints.

**Step 4: $\Delta S > 0$, second law satisfied with strict inequality.**

> [!note]- Derivation
> The free expansion is **adiabatic** in the strong sense (no heat exchanged with environment, isolated container). The second law for adiabatic isolated processes gives $\Delta S \geq 0$, with equality iff the process is reversible.
>
> Here $\Delta S = nR \log(V_2/V_1) > 0$ (strict inequality), reflecting that the free expansion is *irreversible*: you cannot push the gas back into the smaller chamber without doing work and releasing heat to the environment. The irreversibility is qualitatively obvious — gas does not spontaneously congregate into a corner of the container — and is quantified by $nR \log(V_2/V_1)$, the entropy "produced" by the irreversibility.
>
> Microscopically, $\Delta S = nR \log(V_2/V_1) = k_B N \log(V_2/V_1) = k_B \log[(V_2/V_1)^N]$, the logarithm of the ratio of phase-space volumes — exactly Boltzmann's $S = k_B \log W$ applied to the multiplicity of microstates after expansion versus before. The macroscopic entropy increase is the macroscopic shadow of microscopic phase-space spreading.

> [!note]- Complete formal solution
> *Step 1:* First law between equilibrium endpoints: $\Delta U = Q_{\text{actual}} - W_{\text{actual}} = 0 - 0 = 0$.
>
> *Step 2:* For ideal gas $U(T)$, $\Delta U = 0 \Rightarrow \Delta T = 0$. Temperature is unchanged.
>
> *Step 3:* $\Delta S = nR \log(V_2/V_1) > 0$, computed via $S(T, V) = (f/2) nR \log T + nR \log V + \text{const}$ at constant $T$. Same answer from $\Delta S = Q_{\text{rev}}/T$ via the reversible isothermal substitute path.
>
> *Step 4:* $\Delta S > 0$ satisfies the second-law inequality $\Delta S \geq 0$ for adiabatic isolated processes, with strict inequality reflecting irreversibility of free expansion.

> [!warning] Illegal but tempting: computing $\Delta S$ from $\int \delta Q_{\text{actual}}/T$
> Since $Q_{\text{actual}} = 0$ during free expansion, one might be tempted to write $\Delta S = \int_{\gamma_{\text{actual}}} \delta Q/T = 0$. This is *wrong* in two senses. First, $\delta Q/T = dS$ holds only along *quasistatic reversible* paths; free expansion is not quasistatic, so the integrand is not even defined along the actual trajectory (the system passes through non-equilibrium states with no well-defined $T$ or $p$). Second, even if the integrand were defined, the state-function change $\Delta S$ does not equal the integral of $\delta Q_{\text{actual}}/T$ for irreversible processes — the inequality $dS > \delta Q_{\text{actual}}/T_{\text{surr}}$ is exactly the second-law statement that "entropy production exceeds the heat-divided-by-temperature reservoir flux". The correct computation uses a *reversible substitute path* between the same endpoints, along which $\delta Q_{\text{rev}}/T = dS$ holds, giving the same $\Delta S$ as the state-function formula.

---

# Key Takeaways

**State-function changes are path-independent: compute $\Delta S$ from endpoints, not from the actual process.** This is the most important computational fact about entropy in irreversible processes. The actual process is messy, non-quasistatic, with no path in $M$. But $S$ is a state function, so $\Delta S = S(\text{final}) - S(\text{initial})$ — computable from the equilibrium endpoints alone. To evaluate this, use either the explicit formula $S(T, V)$ (if known) or integrate $\delta Q_{\text{rev}}/T$ along a *reversible substitute path* of your choice. The two methods agree (by exactness of $dS$). The trigger-reaction pattern: "irreversible process → use endpoint state-function difference, not actual heat".

**Free expansion of an ideal gas: $\Delta U = \Delta T = 0$, $\Delta S = nR \log(V_2/V_1)$.** These three identities, taken together, are the complete thermodynamic description of free expansion for an ideal gas. They illustrate: (i) the first law (energy conserved when nothing leaves the container); (ii) Joule's law (ideal-gas energy depends only on $T$, so $T$ unchanged); (iii) the second law with strict inequality (entropy increases because the process is irreversible). For a real gas the first identity still holds but the second fails ($\Delta T \neq 0$, captured by the Joule coefficient), and $\Delta S$ acquires extra terms from the intermolecular interactions.

**The microscopic interpretation: $\Delta S = k_B \log(\text{ratio of phase-space volumes})$.** The macroscopic $\Delta S = nR \log(V_2/V_1) = k_B N \log(V_2/V_1)$ has the form $k_B \log[(V_2/V_1)^N]$, the logarithm of the ratio of *N-particle* phase-space volumes accessible in the final vs initial states. This is Boltzmann's $S = k_B \log W$ applied to the multiplicity ratio, and it identifies the macroscopic entropy increase with microscopic phase-space spreading. This is the bridge from Caratheodory's geometric entropy (a function on the macroscopic state manifold) to **statistical mechanics**' microscopic entropy (counting microstates compatible with a macrostate). The Gibbs measure, the maximum-entropy principle, and the equivalence of ensembles all derive from this identification — see [[Def - Absolute Temperature and Entropy#Unlocked by This|the entropy definition's "Unlocked by This" section]].

**The entropy gradient $dS/dV = nR/V$ explains why free expansion is the canonical irreversibility example.** Of all the "natural" irreversible processes (stirring, mixing, free expansion, sudden temperature equilibration), free expansion is the simplest because it involves only volume change at constant temperature, with $\Delta S$ computable from a single logarithm. The pattern $\Delta S \propto \log V$ recurs throughout thermodynamics: in the entropy of mixing (Gibbs paradox), in chemical potentials of ideal solutions, in the dependence of free energy on concentration. Recognising "$\log V$" as the signature of "volume-dependence of entropy for an ideal gas" speeds recognition of these analogous structures in chemistry and biology.
