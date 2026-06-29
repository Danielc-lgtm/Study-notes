---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Rapidity"
  - "Thm - Boosts Compose by Adding Rapidities"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and boosts along the $x$-axis.

1. By multiplying the two boost matrices in **velocity** form, $\Lambda[v_1]\Lambda[v_2]$ with $\Lambda[v] = \gamma\begin{pmatrix} 1 & v \\ v & 1 \end{pmatrix}$, show directly that the result is the boost $\Lambda[w]$ with $w = (v_1 + v_2)/(1 + v_1 v_2)$. (This is Tong's "little bit of algebra".)
2. Redo the composition in **rapidity** form, $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1 + \varphi_2]$, and recover the same $w = \tanh(\varphi_1 + \varphi_2)$. Note how much shorter the calculation is.
3. A rocket moves at $v_1 = 0.8$ relative to Earth and fires a probe at $v_2 = 0.8$ relative to itself, in the same direction. Find the probe's Earth-frame speed, both via the velocity formula and via rapidities.
4. A particle receives $N$ successive identical boosts, each adding rapidity $\Delta\varphi$ in the instantaneous rest frame. Find its final velocity and show it approaches but never reaches $1$ as $N \to \infty$.

**Recall:**

![[Thm - Boosts Compose by Adding Rapidities#Statement]]

The [[Def - Rapidity|rapidity]] $\varphi$ is defined by $v = \tanh\varphi$, $\gamma = \cosh\varphi$, $\gamma v = \sinh\varphi$. The boost in rapidity form is the [[Def - Boosts as Hyperbolic Rotations|hyperbolic rotation]] $\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}$. The hyperbolic addition formulas are $\cosh(a+b) = \cosh a\cosh b + \sinh a\sinh b$ and $\sinh(a+b) = \sinh a\cosh b + \cosh a\sinh b$.

---

# Convergent Strategy

**Problem class.** A *compute-a-relativistic-effect* problem (combining velocities) that doubles as a demonstration of why [[Def - Rapidity|rapidity]] is the right variable. The [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group#Problem-Solving Strategy|topic strategy]] says: to combine collinear velocities, switch to rapidity, add, convert back.

**Assumption pattern.** Collinear boosts — the hypothesis of [[Thm - Boosts Compose by Adding Rapidities|rapidity additivity]]. The signpost is "same direction": all motions along one axis, which is exactly when rapidities simply add and no Thomas rotation appears.

**Theorem routing.** Part 1 is a direct matrix multiplication identifying the product as a boost; Part 2 is the one-line [[Thm - Boosts Compose by Adding Rapidities|additivity theorem]]; Parts 3–4 apply $w = \tanh(\varphi_1 + \cdots)$. The route is: velocities $\to$ rapidities ($\varphi = \tanh^{-1}v$) $\to$ add $\to$ velocities ($v = \tanh\varphi$).

**Key decision point.** The decision is *not to iterate the velocity formula*. For two boosts the velocity formula is bearable; for $N$ boosts it is hopeless, while $N$ rapidities sum trivially. Recognising that the nonlinearity of velocity addition is an artefact of the wrong coordinate — and that rapidity linearises it — is the whole lesson, and Part 4 is the payoff that makes it undeniable.

---

# Legal Operations Used

1. **Switch to rapidity to make boosts additive (operation 6 from the topic page).** Convert each velocity to its rapidity $\varphi = \tanh^{-1}v$; the nonlinear composition becomes a sum.

2. **Add velocities relativistically (operation 5 from the topic page).** Part 1 carries out the direct velocity-form multiplication, reproducing $w = (v_1 + v_2)/(1 + v_1 v_2)$ as the long way round.

3. **Apply the Lorentz transformation to map between frames (operation 1 from the topic page).** Each boost is a frame change; composing them is composing frame changes, here all along one axis.

---

# Hints

> [!note]- Hint 1
> In velocity form, $\Lambda[v_1]\Lambda[v_2] = \gamma_1\gamma_2\begin{pmatrix} 1 & v_1 \\ v_1 & 1 \end{pmatrix}\begin{pmatrix} 1 & v_2 \\ v_2 & 1 \end{pmatrix}$. Multiply out; the result should be $\gamma_1\gamma_2(1 + v_1 v_2)$ times a matrix of the boost form. Read off the velocity as the off-diagonal-over-diagonal ratio.

> [!note]- Hint 2
> In rapidity form there is nothing to compute: the [[Thm - Boosts Compose by Adding Rapidities|additivity theorem]] gives $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1 + \varphi_2]$ immediately, so $w = \tanh(\varphi_1 + \varphi_2)$, and expanding $\tanh$ of a sum reproduces Part 1.

> [!note]- Hint 3
> $\tanh^{-1}(0.8) \approx 1.0986$. Add the two rapidities to get $\approx 2.197$, then $w = \tanh(2.197) \approx 0.9756$. Check with the velocity formula: $(0.8 + 0.8)/(1 + 0.64) = 1.6/1.64$.

> [!note]- Hint 4
> $N$ boosts of rapidity $\Delta\varphi$ give total rapidity $N\Delta\varphi$, so $v_N = \tanh(N\Delta\varphi)$. As $N \to \infty$, $N\Delta\varphi \to \infty$ and $\tanh \to 1$, but $\tanh < 1$ for every finite argument.

---

# Solution

The exercise contrasts the same physical operation done two ways. Step 1 grinds out the matrix product in velocity variables and recovers the velocity-addition law the hard way. Step 2 does it in rapidity variables in one line. Steps 3 and 4 apply the result: a concrete two-boost number, and the $N$-boost limit that shows the speed of light is an unreachable ceiling. The throughline is that rapidity turns a nonlinear composition into addition.

**Step 1: velocity-form multiplication gives $w = (v_1+v_2)/(1+v_1 v_2)$.**

> [!note]- Derivation
> With $\Lambda[v] = \gamma\begin{pmatrix} 1 & v \\ v & 1 \end{pmatrix}$,
> $$\Lambda[v_1]\Lambda[v_2] = \gamma_1\gamma_2\begin{pmatrix} 1 & v_1 \\ v_1 & 1 \end{pmatrix}\begin{pmatrix} 1 & v_2 \\ v_2 & 1 \end{pmatrix} = \gamma_1\gamma_2\begin{pmatrix} 1 + v_1 v_2 & v_1 + v_2 \\ v_1 + v_2 & 1 + v_1 v_2 \end{pmatrix}.$$
> Factor out $1 + v_1 v_2$ from the matrix:
> $$= \gamma_1\gamma_2(1 + v_1 v_2)\begin{pmatrix} 1 & \dfrac{v_1 + v_2}{1 + v_1 v_2} \\[2mm] \dfrac{v_1 + v_2}{1 + v_1 v_2} & 1 \end{pmatrix}.$$
> This has the boost form $\gamma_w\begin{pmatrix} 1 & w \\ w & 1 \end{pmatrix}$ with
> $$w = \frac{v_1 + v_2}{1 + v_1 v_2}, \qquad \gamma_w = \gamma_1\gamma_2(1 + v_1 v_2).$$
> (One checks $\gamma_w = (1 - w^2)^{-1/2}$ directly, confirming the overall factor is the correct $\gamma$ for velocity $w$.) So the composite of two collinear boosts is the single boost of velocity $w = (v_1 + v_2)/(1 + v_1 v_2)$ — the [[Thm - Relativistic Velocity Addition|relativistic velocity-addition law]].

**Step 2: rapidity-form multiplication is one line.**

> [!note]- Derivation
> Write $v_i = \tanh\varphi_i$, so $\Lambda[v_i] = \Lambda[\varphi_i] = \begin{pmatrix} \cosh\varphi_i & \sinh\varphi_i \\ \sinh\varphi_i & \cosh\varphi_i \end{pmatrix}$. By [[Thm - Boosts Compose by Adding Rapidities|rapidity additivity]] (the hyperbolic addition formulas applied to the entries),
> $$\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1 + \varphi_2].$$
> Hence the composed velocity is $w = \tanh(\varphi_1 + \varphi_2)$. Expanding,
> $$w = \tanh(\varphi_1 + \varphi_2) = \frac{\tanh\varphi_1 + \tanh\varphi_2}{1 + \tanh\varphi_1\tanh\varphi_2} = \frac{v_1 + v_2}{1 + v_1 v_2},$$
> the same result as Step 1 with none of the matrix bookkeeping. The denominator $1 + v_1 v_2$ that took a factoring step to produce in Step 1 is here just the denominator of the $\tanh$ addition formula.

**Step 3: the rocket-and-probe numbers.**

> [!note]- Derivation
> *Velocity formula:* $w = (0.8 + 0.8)/(1 + 0.8\cdot 0.8) = 1.6/1.64 = 0.9756$.
>
> *Rapidity:* each rapidity is $\varphi_1 = \varphi_2 = \tanh^{-1}(0.8) = \tfrac12\ln\frac{1+0.8}{1-0.8} = \tfrac12\ln\frac{1.8}{0.2} = \tfrac12\ln 9 \approx 1.0986$. The total is $\varphi_{\text{tot}} = \varphi_1 + \varphi_2 = \ln 9 \approx 2.1972$, and
> $$w = \tanh(\ln 9) = \frac{e^{\ln 9} - e^{-\ln 9}}{e^{\ln 9} + e^{-\ln 9}} = \frac{9 - 1/9}{9 + 1/9} = \frac{80/9}{82/9} = \frac{80}{82} = 0.9756.$$
> Both methods agree: the probe moves at $0.9756$ relative to Earth — close to but below $c$, even though the naive sum "$0.8 + 0.8 = 1.6$" exceeds it.

**Step 4: $N$ boosts never reach $c$.**

> [!note]- Derivation
> Each boost adds $\Delta\varphi$ in rapidity, so after $N$ boosts the total rapidity is $\varphi_N = N\Delta\varphi$ (additivity, applied $N$ times). The final velocity is
> $$v_N = \tanh(N\Delta\varphi).$$
> Since $\tanh$ is strictly increasing with horizontal asymptote $1$, $v_N$ increases monotonically toward $1$ as $N \to \infty$, but $\tanh(N\Delta\varphi) < 1$ for *every* finite $N$. No finite number of sub-light boosts reaches the speed of light; $c$ corresponds to infinite rapidity. (For a continuously accelerating rocket with constant proper acceleration $a$, $\Delta\varphi \to a\,d\tau$ and $\varphi(\tau) = a\tau$, giving $v(\tau) = \tanh(a\tau) \to 1$ — the relativistic rocket asymptotes to light speed but never attains it.) Trying to argue with velocities — "each boost adds $\approx 0.8$, so a few boosts exceed $c$" — is exactly the Galilean error the velocity-addition law corrects; in rapidity the impossibility is transparent because $\tanh$ is bounded.

> [!note]- Complete formal solution
> *Velocity form.* $\Lambda[v_1]\Lambda[v_2] = \gamma_1\gamma_2\begin{pmatrix} 1+v_1v_2 & v_1+v_2 \\ v_1+v_2 & 1+v_1v_2 \end{pmatrix} = \gamma_1\gamma_2(1+v_1v_2)\begin{pmatrix} 1 & w \\ w & 1 \end{pmatrix}$ with $w = (v_1+v_2)/(1+v_1v_2)$, a boost of velocity $w$.
>
> *Rapidity form.* With $v_i = \tanh\varphi_i$, $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1+\varphi_2]$ by additivity, so $w = \tanh(\varphi_1+\varphi_2) = (v_1+v_2)/(1+v_1v_2)$.
>
> *Numbers.* $v_1 = v_2 = 0.8 \Rightarrow w = 1.6/1.64 = 0.9756$; equivalently $\varphi_{\text{tot}} = 2\tanh^{-1}(0.8) = \ln 9$, $w = \tanh(\ln 9) = 80/82 = 0.9756$.
>
> *$N$ boosts.* Total rapidity $N\Delta\varphi$, final velocity $v_N = \tanh(N\Delta\varphi) \to 1^-$ as $N\to\infty$ but $< 1$ for all finite $N$: the speed of light is an unreachable ceiling, corresponding to infinite rapidity. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> For the $N$-boost problem it is tempting to iterate the velocity-addition formula $N$ times. This is correct but a computational nightmare (a nested fraction $N$ levels deep), and worse, it *obscures* the key fact that the limit is exactly $1$: from the velocity recursion alone it is not obvious the sequence converges to $c$ rather than overshooting. In rapidity the sum is $N\Delta\varphi$ and the bound $\tanh < 1$ makes the ceiling self-evident. The rule: never iterate velocity addition; iterate rapidity addition.

---

# Key Takeaways

**Rapidity linearises boost composition — convert, add, convert back.** The transferable procedure is: whenever collinear velocities must be combined, do not reach for $(v_1 + v_2)/(1 + v_1 v_2)$, convert each to its rapidity $\varphi = \tanh^{-1}v$, add the rapidities (subtract for an inverse), and convert the sum back with $v = \tanh\varphi$. The matrix multiplication of Step 1 and the one-liner of Step 2 give the same answer, but the rapidity route scales: for $N$ boosts it is a single sum where the velocity formula is an $N$-fold nested fraction. The trigger is any chain of collinear frame changes, accelerations, or relayed signals; the diagnostic is "are these all along one line?" — if so, rapidities add. This is the relativistic instance of the general principle that the canonical coordinate on a one-parameter group turns its nonlinear law into addition.

**The speed of light is a ceiling because $\tanh$ is bounded while rapidity is not.** The reason no chain of sub-light boosts ever reaches $c$ is not a numerical coincidence in the velocity formula — it is the boundedness of $\tanh$. Rapidity ranges over all of $\mathbb{R}$, so it can be added without limit, but its image under $\tanh$ stays in $(-1, 1)$ and only approaches the endpoints. This converts the awkward dynamical question "can you accelerate to $c$?" into the transparent analytic fact "$\tanh$ has horizontal asymptotes". The same observation governs the relativistic rocket (constant proper acceleration gives $v = \tanh(a\tau) \to 1$) and the impossibility of bringing a massive particle to light speed with finite energy. Whenever a "can you reach the limit?" question arises in relativity, translate it to rapidity, where the limit is at infinity.

**The denominator in velocity addition is the cross term of a hyperbolic sum.** A subtle but illuminating point: the mysterious $1 + v_1 v_2$ in the velocity-addition law is not an ad hoc correction — it is precisely the denominator produced by dividing $\sinh(\varphi_1 + \varphi_2)$ by $\cosh(\varphi_1 + \varphi_2)$ and clearing $\cosh\varphi_1\cosh\varphi_2$. In Step 1 it appeared only after a factoring trick; in Step 2 it fell out of the $\tanh$ addition formula automatically. Recognising the velocity formula as "$\tanh$ of a sum in disguise" demystifies every feature at once: the denominator (cross term), the $c$-fixed-point ($\tanh(\infty) = 1$ composed with anything stays $1$), and the sub-light closure ($\tanh$ of a finite sum stays finite). This is the payoff of having the *right* parametrisation: structural facts become visible that are invisible in the wrong variable.
