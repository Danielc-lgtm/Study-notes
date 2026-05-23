---
type: exercise-index
subject: thermodynamics
section: "1.3"
tags: [physics, thermodynamics, entropy]
---

## §1.3 Entropy and Absolute Temperature — Exercises

The exercises of this section drill the computational use of the entropy and absolute temperature: computing $S$ as a state function via integration of $dS = \delta Q/T$, analysing cycles in $(T, S)$ coordinates where adiabats and isotherms become straight lines, and applying the second-law inequality $\Delta S \geq 0$ to irreversible processes. The recurring theme is that **entropy is a state function — its changes depend only on endpoints**, so $\Delta S$ for an irreversible process is computed via a reversible substitute path between the same endpoints, not by integrating $\delta Q_{\text{actual}}/T$ along the actual path.

- [[Ex - Carnot Cycle in Pressure-Volume and in Temperature-Entropy]] (⭐⭐) — Draw the Carnot cycle in two coordinate systems, observe it becomes a rectangle in $(T, S)$, compute the efficiency $\eta = 1 - T_c/T_h$ from the rectangle's geometry. Illustrates the unique geometric simplicity of $(T, S)$ coordinates for cycle analysis. ([[Def - Heat 1-Form and Work 1-Form]], [[Def - The First Law of Thermodynamics]], [[Def - Absolute Temperature and Entropy]], [[Def - Adiabatic Process and Adiabatic Distribution]])

- [[Ex - Compute the Entropy of an Ideal Gas]] (⭐⭐) — Integrate $dS = \delta Q/T$ for an ideal gas to obtain $S(T, V) = (f/2)nR \log T + nR \log V + \text{const}$, then convert to $S(T, p) = C_p \log T - nR \log p + \text{const}$. Identify the additive constant as the bridge to statistical mechanics and the Sackur-Tetrode equation. ([[Def - Heat 1-Form and Work 1-Form]], [[Def - Absolute Temperature and Entropy]], [[Def - Thermodynamic Potential (U, H, F, G)]], [[Thm - The Heat 1-Form is Integrable]])

- [[Ex - Entropy Change in Free Expansion (Irreversible)]] (⭐⭐) — Compute $\Delta S = nR \log(V_2/V_1) > 0$ for an ideal gas in Joule's free expansion, illustrating that the state-function $\Delta S$ for an irreversible process is computed via the entropy formula or a reversible substitute path, not by integrating $\delta Q_{\text{actual}}/T = 0$. Verifies the strict inequality $\Delta S > 0$ for irreversible adiabatic processes. ([[Def - Absolute Temperature and Entropy]], [[Def - The First Law of Thermodynamics]], [[Def - Quasistatic Process]])
