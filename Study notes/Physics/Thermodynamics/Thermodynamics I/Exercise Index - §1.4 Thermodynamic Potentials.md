---
type: exercise-index
subject: thermodynamics
section: "1.4"
tags: [physics, thermodynamics, maxwell-relations]
---

## §1.4 Thermodynamic Potentials — Exercises

The exercises of this section drill the algebraic apparatus of thermodynamic potentials and Maxwell relations: deriving identities among partial derivatives via $d^2 = 0$, converting hard-to-measure entropy gradients into easy-to-measure $T, p, V$ derivatives, and applying these identities to compute physically interesting quantities like the Joule-Thomson coefficient and the heat-capacity difference. The recurring theme is **identify the right potential for the problem (its natural variables match the held-constant variables), apply $d^2 = 0$, read off the relation**. Maxwell relations are the workhorse: every "hard" thermodynamic identity reduces to a Maxwell relation plus an equation of state.

- [[Ex - Maxwell's Relation from dG=0]] (⭐) — Derive the Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ from $d^2 G = 0$, and use it to express isothermal entropy change in terms of the thermal expansion coefficient $\alpha$. Direct illustration of the four-step Maxwell-relation derivation pattern. ([[Def - Thermodynamic Potential (U, H, F, G)]], [[Thm - Maxwell Relations from Closedness]], [[Def - Closed and Exact Forms]])

- [[Ex - Mayer's Relation Cp Minus CV from First Law]] (⭐⭐) — Derive the general identity $C_p - C_V = TV\alpha^2/\kappa_T$ via Maxwell relations and the cyclic relation, then specialise to ideal gas $C_p - C_V = nR$. Illustrates the *coordinate-change* technique for relating quantities defined under different constraint patterns. ([[Def - Thermodynamic Potential (U, H, F, G)]], [[Def - The First Law of Thermodynamics]], [[Thm - Maxwell Relations from Closedness]])

- [[Ex - Joule-Thomson Coefficient from Thermodynamic Identities]] (⭐⭐⭐) — Derive the general formula $\mu_{JT} = [T(\partial V/\partial T)_p - V]/C_p$ for the Joule-Thomson coefficient, then compute it for ideal gas (zero) and Van der Waals gas to leading order (with explicit inversion temperature $T_{\text{inv}} = 2a/(Rb)$). Three-step computation tying together the enthalpy, a Maxwell relation, and a real-gas correction. ([[Def - Thermodynamic Potential (U, H, F, G)]], [[Thm - Maxwell Relations from Closedness]], [[Def - The First Law of Thermodynamics]])
