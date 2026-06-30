---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Doppler Effect"
  - "Def - Relativistic Doppler Factor"
  - "Thm - Time Dilation (General Observer)"
tags: [physics, special-relativity]
---

# Problem Statement

The Ives–Stilwell experiment (1938) was the first laboratory confirmation of time dilation, achieved by measuring the second-order (transverse) Doppler effect. Working with $c = 1$ except where restoring $c$ aids recognition:

1. A source moving directly *toward* the observer at speed $V$ emits at proper frequency $f_0$; the received frequency is $f_1$. A source moving directly *away* at the same speed gives $f_2$. Write $f_1$ and $f_2$ using the radial Doppler formula.
2. Show that the **arithmetic mean** $\tfrac12(f_1 + f_2) = \Gamma f_0$, so the mean is shifted from $f_0$ by exactly the Lorentz factor — a second-order ($V^2$) effect that survives even though the first-order shifts cancel.
3. Show that a *non-relativistic* (first-order) theory would predict $\tfrac12(f_1 + f_2) = f_0$ with no shift, so the observed shift is unambiguously relativistic.
4. The modern (Reinhardt et al. 2007) version measures the *product* $f_1 f_2$ instead. Show $f_1 f_2 = f_0^2$ exactly, independent of $V$, and explain why this is an even cleaner test.

**Recall:**

The exercise drills the radial Doppler formula and its averaging.

![[Thm - The Doppler Effect#Special cases]]

The [[Def - Relativistic Doppler Factor|Doppler factor]] for radial motion is $f_{\mathrm{rec}} = \sqrt{(1+V)/(1-V)}\,f_{\mathrm{em}}$ for approach and the reciprocal for recession; equivalently $f_{\mathrm{rec}} = f_{\mathrm{em}}/[\Gamma(1 \mp V)]$. The Lorentz factor is $\Gamma = (1 - V^2)^{-1/2}$, the [[Thm - Time Dilation (General Observer)|time dilation]] factor of the moving source's clock. The first-order (non-relativistic) Doppler formula is $f_{\mathrm{rec}} = (1 \pm V)f_{\mathrm{em}}$, lacking the $\Gamma$.

---

# Convergent Strategy

**Problem class.** An *isolate-a-small-relativistic-correction* problem: a clever combination (the mean, or the product) of two measurements cancels the large first-order effect and exposes the second-order time-dilation factor. The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] for small-correction problems is to find the combination where the Galilean and relativistic predictions first differ.

**Assumption pattern.** Two radial Doppler measurements at $\pm V$, exploiting the symmetry $V \to -V$. The symmetry is the signpost: averaging two opposite-sign shifts cancels the odd (first-order) part and leaves the even (second-order) part, which is the $\Gamma$ factor.

**Theorem routing.** The radial [[Thm - The Doppler Effect|Doppler formula]] gives $f_{1,2} = f_0/[\Gamma(1 \mp V)]$; averaging routes through the algebraic identity $\tfrac12[1/(1-V) + 1/(1+V)] = 1/(1-V^2) = \Gamma^2$ combined with the $1/\Gamma$ prefactor to give $\Gamma f_0$. The product routes through $[\Gamma^2(1-V)(1+V)]^{-1} = [\Gamma^2(1-V^2)]^{-1} = 1$.

**Key decision point.** The crux is choosing the *combination* that cancels the first-order effect: the arithmetic mean cancels the odd part (Ives–Stilwell), the geometric mean / product cancels it more cleanly (Reinhardt). The natural but wrong move is to try to measure the transverse effect *directly* by observing at exactly $90^\circ$, which is experimentally fragile (the slightest misalignment readmits the huge first-order effect); the symmetric-pair trick is robust against this.

---

# Legal Operations Used

1. **Use the Doppler factor in the radial form** (drawing on the topic page's Doppler operations), writing the two opposite-motion frequencies $f_{1,2} = f_0/[\Gamma(1 \mp V)]$.

2. **Take a low-speed / order-by-order limit** (operation 9 from the topic page), to contrast the relativistic mean $\Gamma f_0 = f_0(1 + \tfrac12 V^2 + \cdots)$ with the non-relativistic prediction $f_0$, identifying the second-order shift as the observable.

---

# Hints

> [!note]- Hint 1
> Approach: $f_1 = \sqrt{(1+V)/(1-V)}f_0 = f_0/[\Gamma(1-V)]$. Recession: $f_2 = \sqrt{(1-V)/(1+V)}f_0 = f_0/[\Gamma(1+V)]$. (Both forms are equal; the $1/\Gamma(1\mp V)$ form makes the averaging cleaner.)

> [!note]- Hint 2
> Average: $\tfrac12(f_1 + f_2) = \tfrac{f_0}{2\Gamma}\left[\tfrac{1}{1-V} + \tfrac{1}{1+V}\right]$. Combine the bracket over a common denominator: $\tfrac{(1+V)+(1-V)}{(1-V)(1+V)} = \tfrac{2}{1-V^2} = 2\Gamma^2$. So the mean is $\tfrac{f_0}{2\Gamma}\cdot 2\Gamma^2 = \Gamma f_0$.

> [!note]- Hint 3
> The first-order formula gives $f_1 = (1+V)f_0$, $f_2 = (1-V)f_0$, so $\tfrac12(f_1 + f_2) = f_0$ exactly — no shift. The relativistic mean $\Gamma f_0 = f_0(1 + \tfrac12 V^2 + \cdots)$ differs at *second* order. The presence of any shift in the mean is therefore a pure time-dilation signal.

> [!note]- Hint 4
> Product: $f_1 f_2 = \tfrac{f_0^2}{\Gamma^2(1-V)(1+V)} = \tfrac{f_0^2}{\Gamma^2(1-V^2)} = \tfrac{f_0^2}{1} = f_0^2$, since $\Gamma^2(1-V^2) = 1$. The product is *exactly* $f_0^2$ for any $V$ — no expansion needed, and no need to know $V$ precisely, which is why it is a cleaner test.

---

# Solution

The Ives–Stilwell experiment isolates time dilation by symmetrically averaging two opposite-direction Doppler shifts. Step 1 writes the two radial shifts; Step 2 averages them to get $\Gamma f_0$, a pure second-order signal; Step 3 contrasts with the non-relativistic null prediction; Step 4 gives the modern product test $f_1 f_2 = f_0^2$. The non-obvious move is the symmetric pairing, which cancels the dominant first-order effect and leaves only the relativistic factor.

**Step 1: The two radial Doppler shifts.**

> [!note]- Derivation
> For a source approaching at speed $V$, the radial [[Thm - The Doppler Effect|Doppler]] formula gives
> $$f_1 = \sqrt{\frac{1+V}{1-V}}\,f_0 = \frac{f_0}{\Gamma(1-V)},$$
> using $\Gamma(1-V) = \sqrt{(1-V)/(1+V)}$. For a source receding at the same speed ($V \to -V$),
> $$f_2 = \sqrt{\frac{1-V}{1+V}}\,f_0 = \frac{f_0}{\Gamma(1+V)}.$$
> The first is a blueshift ($f_1 > f_0$), the second a redshift ($f_2 < f_0$).

**Step 2: The mean is $\Gamma f_0$.**

> [!note]- Derivation
> Average the two:
> $$\frac{f_1 + f_2}{2} = \frac{f_0}{2\Gamma}\left[\frac{1}{1-V} + \frac{1}{1+V}\right] = \frac{f_0}{2\Gamma}\cdot\frac{(1+V) + (1-V)}{(1-V)(1+V)} = \frac{f_0}{2\Gamma}\cdot\frac{2}{1-V^2}.$$
> Since $1 - V^2 = 1/\Gamma^2$, the bracket is $2\Gamma^2$, so
> $$\frac{f_1 + f_2}{2} = \frac{f_0}{2\Gamma}\cdot 2\Gamma^2 = \Gamma f_0.$$
> The mean is the rest frequency *times the Lorentz factor* — a pure second-order ($V^2$) shift. Physically: the first-order blueshift of the approaching source and the first-order redshift of the receding source cancel in the mean, leaving only the common time-dilation factor $\Gamma$ by which *both* sources' clocks run slow.

**Step 3: The non-relativistic prediction is null.**

> [!note]- Derivation
> A classical (first-order) Doppler theory gives $f_1 = (1+V)f_0$ and $f_2 = (1-V)f_0$, so
> $$\frac{f_1 + f_2}{2} = \frac{(1+V) + (1-V)}{2}f_0 = f_0,$$
> *no shift at all*. The two first-order shifts cancel exactly, and classically there is nothing left. The relativistic mean $\Gamma f_0 = f_0(1 + \tfrac12 V^2 + \cdots)$ differs at second order. Therefore any nonzero shift of the mean from $f_0$ is *unambiguously* relativistic — it is the time-dilation factor $\Gamma$, with no classical contribution to subtract. Ives and Stilwell, using $\mathrm{H}_2^+, \mathrm{H}_3^+$ ions at $V \sim 4\times 10^{-3}$, measured a shift of the mean of the $\mathrm{H}_\beta$ line by a few picometres, consistent with $\Gamma$ to about $1\%$ — the first laboratory confirmation of time dilation.

**Step 4: The modern product test.**

> [!note]- Derivation
> The Reinhardt et al. (2007) experiment measures the *product* of the two frequencies:
> $$f_1 f_2 = \frac{f_0}{\Gamma(1-V)}\cdot\frac{f_0}{\Gamma(1+V)} = \frac{f_0^2}{\Gamma^2(1-V)(1+V)} = \frac{f_0^2}{\Gamma^2(1-V^2)} = f_0^2,$$
> exactly, since $\Gamma^2(1-V^2) = 1$. So $f_1 f_2 = f_0^2$ holds for *any* $V$, with no approximation. This is a cleaner test than the mean for two reasons: it is an *exact* identity (no second-order expansion is invoked, so there is no truncation error to control), and it does not require knowing $V$ precisely — one simply checks that the product of the two measured frequencies equals the square of the rest frequency. A *non-relativistic* theory would predict $f_1 f_2 = (1+V)(1-V)f_0^2 = (1-V^2)f_0^2 \ne f_0^2$, differing at second order. Using $^7\mathrm{Li}^+$ ions in a storage ring at $V = 0.03c$ and $0.064c$, the Heidelberg group confirmed $f_1 f_2 = f_0^2$ to a relative deviation below $10^{-9}$ — one of the most precise tests of special relativity.

> [!note]- Complete formal solution
> The approach and recession radial Doppler shifts are $f_1 = f_0/[\Gamma(1-V)]$ and $f_2 = f_0/[\Gamma(1+V)]$. Their mean is $\tfrac12(f_1+f_2) = \tfrac{f_0}{2\Gamma}\cdot\tfrac{2}{1-V^2} = \Gamma f_0$, a pure second-order time-dilation shift; a first-order theory gives $\tfrac12(f_1+f_2) = f_0$, so the observed shift is unambiguously relativistic. The product is $f_1 f_2 = f_0^2/[\Gamma^2(1-V^2)] = f_0^2$ exactly, independent of $V$, providing a velocity-independent, expansion-free test confirmed to $10^{-9}$ by Reinhardt et al. $\blacksquare$

---

# Key Takeaways

**Symmetric pairing cancels the first-order effect and exposes the second-order one — the master trick for measuring time dilation through Doppler.** The entire experimental strategy is to combine two measurements related by $V \to -V$ so that the large, odd-in-$V$ first-order Doppler shift cancels, leaving the small, even-in-$V$ second-order time-dilation factor as the sole survivor. This is a completely general technique for isolating a higher-order effect buried under a lower-order one: arrange a symmetry under which the unwanted lower-order term is odd and the wanted higher-order term is even, then take the (even) symmetric combination. The same idea appears throughout precision physics — in cancelling first-order Doppler in atomic-clock comparisons, in two-photon spectroscopy (counter-propagating beams cancel first-order Doppler), and in the design of any experiment where a sought effect is dwarfed by a symmetry-breakable background. The trigger: whenever a second-order effect must be measured against a first-order background, look for a sign-flip symmetry to suppress the background.

**The transverse Doppler effect *is* time dilation, and its survival when first-order shifts cancel is the cleanest possible signature.** The factor $\Gamma$ in the averaged frequency is not a new optical phenomenon — it is exactly the slowing of the moving source's clock, observed as a frequency reddening. The conceptual payoff is that a *frequency* measurement (the mean of two Doppler shifts) is a direct *clock-rate* measurement: you are literally watching the source's clock run slow, encoded in the colour of its light. This is why Ives–Stilwell counts as a time-dilation experiment despite measuring frequencies, and historically it was the *first* such confirmation, predating the atmospheric-muon measurement. The transferable insight is that time dilation and the transverse Doppler effect are the same fact in two languages (clock rate vs. frequency), so any clean measurement of one is a measurement of the other.

**An exact identity beats an expanded one: the product test needs neither a Taylor series nor a known velocity.** The progression from the Ives–Stilwell mean ($\Gamma f_0$, requiring a second-order expansion and a known $V$ to compare) to the Reinhardt product ($f_1 f_2 = f_0^2$, an exact identity for all $V$) illustrates a deep experimental principle: a test built on an *exact* algebraic identity is more powerful than one built on an approximate expansion, because it has no truncation error and is insensitive to the precise value of nuisance parameters. The product $f_1 f_2 = f_0^2$ holds for every $V$, so the experimenter need not measure $V$ accurately — a major advantage, since velocity is hard to measure to high precision. The general lesson for designing precision tests: seek combinations of observables that the theory predicts to be *exactly* constant (here, $f_1 f_2/f_0^2 = 1$), because deviations from an exact constant are far easier to bound than deviations from a velocity-dependent prediction. This is why the modern test reaches $10^{-9}$ where the original reached $10^{-2}$.
