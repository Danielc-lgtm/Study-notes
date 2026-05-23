---
type: exercise
subject: thermodynamics
difficulty: "⭐⭐"
prereqs:
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - The First Law of Thermodynamics"
  - "Def - Absolute Temperature and Entropy"
  - "Def - Adiabatic Process and Adiabatic Distribution"
tags: [physics, thermodynamics, ideal-gas, carnot-cycle]
---

# Problem Statement

The **Carnot cycle** is a closed reversible quasistatic process consisting of four legs:

1. Isothermal expansion at hot temperature $T_h$ from volume $V_1$ to volume $V_2$.
2. Adiabatic expansion from $T_h$ to $T_c$, volume increasing from $V_2$ to $V_3$.
3. Isothermal compression at cold temperature $T_c$ from $V_3$ to $V_4$.
4. Adiabatic compression from $T_c$ to $T_h$, volume decreasing from $V_4$ to $V_1$.

For an ideal gas working substance:

1. Draw the cycle in $(p, V)$ coordinates. Identify each leg and the direction of traversal.
2. Draw the cycle in $(T, S)$ coordinates. Verify it becomes a rectangle and identify the dimensions.
3. Compute the efficiency $\eta = W_{\text{net}} / Q_h$ where $W_{\text{net}}$ is the total work done by the gas around the cycle and $Q_h$ is the heat absorbed at the hot reservoir.
4. Show that $\eta = 1 - T_c/T_h$ using either picture.

**Recall:**

The [[Def - The First Law of Thermodynamics|first law of thermodynamics]] is $dU = \delta Q - \delta W$, which integrated around a closed cycle gives $\oint dU = 0$, hence $W_{\text{net}} = \oint \delta W = \oint \delta Q = Q_{\text{net}}$.

The [[Def - Absolute Temperature and Entropy|second law in differential form]] is $\delta Q = T\, dS$ for quasistatic reversible processes. Along an isotherm, $T$ is constant, so $\int \delta Q = T \Delta S$.

An [[Def - Adiabatic Process and Adiabatic Distribution|adiabatic process]] has $\delta Q = 0$, hence $dS = 0$ — entropy is constant along an adiabat.

For an ideal gas, $S = (f/2) nR \log T + nR \log V + \text{const}$.

---

# Convergent Strategy

**Problem class:** This is a cycle-efficiency problem of the type "compute net work and heat absorbed around a closed path in the state space". The recurring pattern is: (i) draw the cycle in coordinates where each leg is geometrically simple, (ii) compute the heat and work along each leg using the first law and the appropriate restriction (isothermal: $dU = 0$, adiabatic: $\delta Q = 0$), (iii) sum to get the total. The $(T, S)$ picture is the *clever* coordinate choice that makes the cycle a rectangle and the efficiency a ratio of areas.

**Assumption pattern:** The Carnot cycle uses *reversible quasistatic* processes throughout — every leg is a smooth path in $M$ with well-defined $T$ and $p$. The reversibility is essential: it lets us write $\delta Q = T\, dS$ on each isotherm and use $dS = 0$ on each adiabat. The working substance is an ideal gas for the explicit computation, but the efficiency formula $\eta = 1 - T_c/T_h$ holds for *any* reversible Carnot cycle (this is Carnot's theorem) — the ideal-gas computation is just the simplest verification.

**Theorem routing:** The first law $\oint dU = 0$ converts net work into net heat absorbed. The second law $\delta Q = T\, dS$ converts heat along each isotherm into $T \Delta S$. The adiabats give zero $\Delta S$ — they are vertical lines in the $(T, S)$ picture. So the cycle is a rectangle with horizontal sides being isotherms and vertical sides being adiabats, with the net heat absorbed equal to the area. The efficiency $\eta = W_{\text{net}}/Q_h = (Q_h - Q_c)/Q_h = 1 - Q_c/Q_h = 1 - T_c \Delta S / (T_h \Delta S) = 1 - T_c/T_h$.

**Key decision point:** The non-obvious choice is to switch from $(p, V)$ coordinates (where the Carnot cycle is a curvilinear shape bounded by hyperbolic isotherms and the steeper adiabats $pV^\gamma = \text{const}$) to $(T, S)$ coordinates (where the cycle is a clean rectangle). The geometric simplification is dramatic: in $(p, V)$ the area computation requires integrating $p\, dV$ along each curved leg; in $(T, S)$ the area is just $\Delta T \cdot \Delta S = (T_h - T_c) \Delta S$, computed by inspection. The choice of coordinates that makes the cycle's boundary simple is the entire trick.

---

# Legal Operations Used

1. **Operation 1 from the topic page (split a 1-form using the first law).** Around the cycle, $\oint dU = 0$ converts $W_{\text{net}} = Q_{\text{net}}$. On each isotherm, $dU = 0$ for an ideal gas (since $U$ depends only on $T$), so $\delta Q = \delta W$ on each isotherm.

2. **Operation 3 from the topic page (restrict a 1-form to a process).** On each leg of the cycle, the restriction of $\delta Q$ or $\delta W$ to that leg reduces to an elementary integral: isothermal gives $\delta Q = (nRT/V)\, dV$; adiabatic gives $\delta Q = 0$.

3. **Operation 6 from the topic page (integrate along an adiabat).** Along the adiabatic legs (2) and (4), $\delta Q = 0$ and the first law gives $dU = -\delta W$; integrating, the work done equals $-\Delta U = -(C_V)(T_f - T_i)$, automatically converting temperature changes into work.

---

# Hints

> [!note]- Hint 1
> Start by sketching each leg. In $(p, V)$ coordinates: isotherms are hyperbolas $pV = \text{const}$, adiabats are steeper curves $pV^\gamma = \text{const}$ where $\gamma = 1 + 2/f > 1$. In $(T, S)$ coordinates: isotherms are horizontal lines ($T = \text{const}$), adiabats are vertical lines ($S = \text{const}$).

> [!note]- Hint 2
> The net work done by the gas around the cycle equals the area enclosed by the cycle in $(p, V)$ coordinates (since $\oint p\, dV$ = enclosed area, by Stokes/Green). Similarly, the net heat absorbed equals the area in $(T, S)$ coordinates (since $\oint T\, dS =$ enclosed area). By the first law, these two areas are equal.

> [!note]- Hint 3
> Compute $Q_h$ as the heat absorbed during the isothermal expansion at $T_h$. Use $\delta Q = T\, dS$ with $T = T_h$ constant: $Q_h = T_h (S_2 - S_1) = T_h \Delta S$ where $\Delta S$ is the entropy change along the hot isotherm. Compute $Q_c$ similarly as heat released at $T_c$.

> [!note]- Hint 4
> For an ideal gas the entropy change on the hot isotherm is $\Delta S = nR \log(V_2/V_1)$ (from the formula $S = (f/2) nR \log T + nR \log V$ at constant $T$). The four corners of the Carnot rectangle in $(T, S)$ have coordinates $(T_h, S_1), (T_h, S_2), (T_c, S_2), (T_c, S_1)$ — observe that the entropy change on the cold isotherm is the same $-\Delta S$, by virtue of the adiabats being vertical.

---

# Solution

The proof breaks into four steps. Step 1 draws and labels the cycle in $(p, V)$. Step 2 reorganises the same cycle in $(T, S)$, where it becomes a rectangle. Step 3 computes the heat $Q_h$ absorbed at the hot reservoir and $Q_c$ released at the cold reservoir directly from the rectangle's geometry. Step 4 combines to give $\eta = 1 - T_c/T_h$. The non-obvious move is in Step 2, where the choice of $(T, S)$ coordinates collapses the curved $(p, V)$ shape to a clean rectangle, making the efficiency formula visible by inspection.

**Step 1: The Carnot cycle in $(p, V)$ coordinates.**

> [!note]- Derivation
> The four legs are:
>
> - **Leg 1 (isothermal expansion at $T_h$):** $V_1 \to V_2$, along the hyperbola $p = nRT_h/V$. The gas absorbs heat $Q_h$ from the hot reservoir and does work $W_1 = \int_{V_1}^{V_2} (nRT_h/V)\, dV = nR T_h \log(V_2/V_1)$. Internal energy is unchanged ($dU = 0$ at constant $T$ for an ideal gas), so $Q_h = W_1$.
>
> - **Leg 2 (adiabatic expansion):** $V_2 \to V_3$, along the curve $T V^{2/f} = T_h V_2^{2/f}$, ending at $T = T_c$. No heat exchange ($\delta Q = 0$); the gas does work at the expense of internal energy, with $W_2 = -\Delta U = -(f/2) nR (T_c - T_h) = (f/2) nR (T_h - T_c)$.
>
> - **Leg 3 (isothermal compression at $T_c$):** $V_3 \to V_4$, along $p = nRT_c/V$. The gas releases heat $|Q_c|$ to the cold reservoir; $W_3 = nR T_c \log(V_4/V_3) < 0$ (work done on the gas), so $-Q_c = -W_3 > 0$ — equivalently $Q_c = nR T_c \log(V_4/V_3)$ is negative (heat lost by gas).
>
> - **Leg 4 (adiabatic compression):** $V_4 \to V_1$, along $TV^{2/f} = T_c V_4^{2/f}$, ending at $T_h$. No heat exchange; work done on the gas is $-\Delta U = (f/2) nR (T_h - T_c)$, so $W_4 = -(f/2) nR (T_h - T_c)$.
>
> The cycle in $(p, V)$ is a curvilinear quadrilateral: two hyperbolic isotherms ($pV = nR T_{h,c}$) and two steeper adiabats ($pV^\gamma = \text{const}$). The shape is convex but not simple to compute areas of directly.

**Step 2: The Carnot cycle in $(T, S)$ coordinates is a rectangle.**

> [!note]- Derivation
> Using $S = (f/2) nR \log T + nR \log V + \text{const}$:
>
> - At the start (state 1, $T_h, V_1$): $S_1 = (f/2) nR \log T_h + nR \log V_1$.
> - End of leg 1 (state 2, $T_h, V_2$): $S_2 = (f/2) nR \log T_h + nR \log V_2 = S_1 + nR \log(V_2/V_1)$. Set $\Delta S := nR \log(V_2/V_1)$.
> - End of leg 2 (state 3, $T_c, V_3$): along the adiabat $TV^{2/f} = T_h V_2^{2/f}$, so $V_3 = V_2 (T_h/T_c)^{f/2}$, and $S_3 = (f/2) nR \log T_c + nR \log V_3 = (f/2)nR \log T_c + nR \log V_2 + (f/2) nR \log(T_h/T_c)$. Compute: $(f/2) nR (\log T_c + \log(T_h/T_c)) = (f/2) nR \log T_h$, so $S_3 = (f/2) nR \log T_h + nR \log V_2 = S_2$ — entropy is unchanged on the adiabat, as required.
> - End of leg 3 (state 4, $T_c, V_4$): $S_4 = S_3 + nR \log(V_4/V_3)$. For the cycle to close, $S_4 = S_1$, which forces $V_4/V_3 = V_1/V_2$ (so the cold isothermal compression has the same entropy change as the hot expansion, but reversed in sign).
>
> So the four corners are $(T_h, S_1), (T_h, S_2), (T_c, S_2), (T_c, S_1)$ — a rectangle with vertical sides (adiabats, constant $S$) of length $T_h - T_c$ and horizontal sides (isotherms, constant $T$) of length $\Delta S$.

**Step 3: The heat absorbed at the hot reservoir and released at the cold reservoir.**

> [!note]- Derivation
> Along the hot isotherm (leg 1), $T = T_h$ constant. So $\int \delta Q = \int T_h\, dS = T_h \Delta S$, where $\Delta S = S_2 - S_1 = nR \log(V_2/V_1) > 0$. So $Q_h = T_h \Delta S > 0$ — heat is absorbed by the gas.
>
> Along the cold isotherm (leg 3), $T = T_c$ constant, and the entropy decreases by $\Delta S$ (from $S_2$ to $S_1$). So $\int \delta Q = T_c \cdot (-\Delta S) = -T_c \Delta S$, meaning the heat absorbed is negative — the gas releases heat $|Q_c| = T_c \Delta S$ to the cold reservoir.
>
> By the first law around the cycle, $\oint dU = 0$, so $W_{\text{net}} = Q_{\text{net}} = Q_h + Q_c = T_h \Delta S - T_c \Delta S = (T_h - T_c) \Delta S$. Notice this equals the area of the $(T, S)$ rectangle: width $\Delta S$, height $T_h - T_c$. The $(T, S)$ picture makes the net work visible by inspection.

**Step 4: The Carnot efficiency $\eta = 1 - T_c/T_h$.**

> [!note]- Derivation
> The efficiency is defined as $\eta := W_{\text{net}}/Q_h$ — net work output per unit heat absorbed from the hot reservoir (the "input" energy).
>
> Substituting: $\eta = (T_h - T_c) \Delta S / (T_h \Delta S) = (T_h - T_c)/T_h = 1 - T_c/T_h$.
>
> The $\Delta S$ cancels. The efficiency depends only on the two reservoir temperatures, not on the working substance, the volumes, or the precise shape of the cycle in $(p, V)$. This is **Carnot's theorem**: all reversible cycles operating between two reservoirs at $T_h$ and $T_c$ have the same efficiency $\eta = 1 - T_c/T_h$, and this is the maximum possible efficiency for any heat engine operating between those reservoirs.

> [!note]- Complete formal solution
> Set up the Carnot cycle as four reversible quasistatic legs of an ideal gas: isothermal expansion at $T_h$ from $V_1$ to $V_2$; adiabatic expansion from $(T_h, V_2)$ to $(T_c, V_3)$; isothermal compression at $T_c$ from $V_3$ to $V_4$; adiabatic compression from $(T_c, V_4)$ to $(T_h, V_1)$.
>
> *Step 1 ($(p, V)$ picture):* Isotherms are hyperbolas $p = nRT/V$, adiabats are steeper curves $pV^\gamma = \text{const}$ ($\gamma = 1 + 2/f$). The cycle traces a closed curvilinear quadrilateral.
>
> *Step 2 ($(T, S)$ picture):* Using $S = (f/2)nR \log T + nR \log V + \text{const}$, the four corners have coordinates $(T_h, S_1), (T_h, S_2), (T_c, S_2), (T_c, S_1)$ — a rectangle. Cycle closure forces $V_4/V_3 = V_1/V_2$.
>
> *Step 3 (heats):* $Q_h = T_h(S_2 - S_1) = T_h \Delta S$ where $\Delta S = nR \log(V_2/V_1)$. $Q_c = -T_c \Delta S$ (heat absorbed by gas; positive heat released to cold reservoir).
>
> *Step 4 (efficiency):* By the first law around the cycle, $W_{\text{net}} = Q_h + Q_c = (T_h - T_c)\Delta S$. The efficiency is
> $$\boxed{\eta = \frac{W_{\text{net}}}{Q_h} = \frac{(T_h - T_c)\Delta S}{T_h \Delta S} = 1 - \frac{T_c}{T_h}.}$$
> The result is independent of the working substance and the cycle's volumes; it depends only on the two reservoir temperatures.

> [!warning] Illegal but tempting alternative: integrating $p\, dV$ around the $(p, V)$ cycle directly
> One might be tempted to compute $W_{\text{net}} = \oint p\, dV$ by integrating along each leg of the $(p, V)$ cycle: $\int p\, dV$ along each hyperbolic isotherm gives $nRT \log(V_f/V_i)$, and along each adiabat $\int p\, dV = -\Delta U$. Summing these *does* give the correct $W_{\text{net}} = (T_h - T_c)\Delta S$, but the algebra is tedious and the connection to $T_h, T_c$ is not transparent — the adiabats contribute work that exactly *cancels between the two adiabatic legs* (by symmetry of the temperature ranges), and only the isotherms contribute net work. The $(T, S)$ picture makes this cancellation manifest: the adiabats are vertical lines and contribute zero $T\, dS$, while the isotherms contribute $\pm T \Delta S$. The lesson: choose coordinates that respect the symmetries of the process.

---

# Key Takeaways

**The $(T, S)$ picture is the right coordinate system for cycle problems.** Carnot's theorem and the efficiency formula become visible by inspection in $(T, S)$ coordinates because the cycle becomes a rectangle with sides parallel to the coordinate axes. This is a recurring lesson: when faced with a cycle problem, choose coordinates in which the natural physical processes (isotherms, adiabats, isobars, isochores) are straight coordinate lines. For Carnot the answer is $(T, S)$; for Otto and Diesel cycles different choices are natural (since these cycles involve isobars and isochores rather than isotherms and adiabats). The trigger-reaction pattern is "see a cycle → find coordinates in which the cycle is geometrically simple".

**The Carnot efficiency is universal — independent of working substance.** The derivation above used an ideal gas to compute $\Delta S = nR \log(V_2/V_1)$, but the cancellation $\Delta S$ in the numerator and denominator means the final formula $\eta = 1 - T_c/T_h$ contains no reference to the substance. This is **Carnot's theorem** in its strongest form: *every* reversible cycle operating between two reservoirs at $T_h$ and $T_c$ has efficiency $\eta = 1 - T_c/T_h$, regardless of working substance, regardless of the specific cycle shape. The reason is that the universality of absolute temperature (zeroth law combined with Caratheodory's principle) makes $T$ a substance-independent quantity, and the efficiency depends only on $T_h, T_c$. This is a remarkable consequence of the second law and one of the deepest results in classical thermodynamics.

**No engine can exceed Carnot efficiency.** A corollary, sometimes called the **Carnot principle**: any heat engine — reversible or not — operating between reservoirs at $T_h$ and $T_c$ has efficiency $\eta \leq 1 - T_c/T_h$, with equality only for reversible cycles. The proof is by contradiction: suppose an engine has efficiency $\eta' > 1 - T_c/T_h$; use it to drive a Carnot refrigerator in reverse, and the combined cycle absorbs net heat from the cold reservoir without doing net work — violating Clausius's statement of the second law. So **the Carnot efficiency is an upper bound on the efficiency of any heat engine**, and the Carnot cycle is the unique cycle that saturates the bound. This is the engineering content of the second law, and the foundation of refrigeration theory, power-plant analysis, and the impossibility of perpetual-motion machines of the second kind.

**The geometric content: net work equals enclosed area in $(T, S)$.** A direct generalisation: for any reversible cycle, the net heat absorbed (and hence the net work done) equals the area enclosed by the cycle in $(T, S)$ coordinates. This is because $\oint T\, dS$ around a closed curve equals the enclosed area (by Stokes/Green theorem). For Carnot the area is a rectangle; for a Stirling cycle it is a parallelogram; for a general cycle it is whatever closed shape the cycle traces. The $(T, S)$ representation thus provides a clean visualisation of *all* reversible heat engine cycles, with the efficiency reading directly off the area-to-perimeter ratio. This is the geometric face of the second law: cycle efficiency = area / "top side area" in $(T, S)$.
