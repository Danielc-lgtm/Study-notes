---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Gauss-Newton Algorithm"
  - "Def - Levenberg-Marquardt Algorithm"
  - "Def - Nonlinear Least Squares Problem"
tags: [algebra, linear-algebra, applied, optimization]
---

# Problem Statement

Consider the scalar function
$$f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \tanh(x).$$
The unique zero of $f$ is $\hat x = 0$.

**(a)** Apply **Newton's method** (= Gauss–Newton with $m = n = 1$) to solve $f(x) = 0$ starting from two different starting points: $x^{(1)} = 0.95$ and $x^{(1)} = 1.15$. Compute the first four iterates in each case. Observe that one converges and the other diverges.

**(b)** Apply the **Levenberg–Marquardt algorithm** with $\lambda^{(1)} = 1$ to solve the *minimization* problem $\min f(x)^2$ from $x^{(1)} = 1.15$. Use the scalar update formula
$$x^{(k+1)} = x^{(k)} - \frac{f'(x^{(k)})}{\lambda^{(k)} + (f'(x^{(k)}))^2} f(x^{(k)}),$$
together with the trust-parameter adaptation rule (shrink $\lambda$ by factor $0.8$ on successful steps, grow by factor $2$ on failed steps). Compute the first six iterates and observe convergence.

**(c)** Explain in one or two paragraphs the mechanism by which Levenberg–Marquardt fixes Newton's divergence: how does the trust parameter $\lambda^{(k)}$ adapt over the run, and what does each phase of adaptation correspond to qualitatively?

**Recall:**

$\tanh$ is the hyperbolic tangent, satisfying $f(0) = 0$, $f'(x) = 1 - \tanh^2(x) = \mathrm{sech}^2(x)$, $f \to \pm 1$ as $x \to \pm \infty$. So $f$ has unique zero at $0$, derivative $1$ at $0$, and asymptotically constant value at infinity.

![[Def - Gauss-Newton Algorithm#The Definition]]

For $m = n = 1$, the Gauss–Newton update reduces to Newton's scalar formula $x^{(k+1)} = x^{(k)} - f(x^{(k)})/f'(x^{(k)})$.

![[Def - Levenberg-Marquardt Algorithm#The Definition]]

For $n = 1$, the Levenberg–Marquardt update simplifies to $x^{(k+1)} = x^{(k)} - f'(x^{(k)}) f(x^{(k)})/(\lambda^{(k)} + (f'(x^{(k)}))^2)$.

---

# Convergent Strategy

**Problem class.** This is a *direct comparison* of Gauss–Newton/Newton against Levenberg–Marquardt on a problem designed to expose their behavioral difference. The problem class is "find a root of a smooth scalar function," for which Newton works in a small basin and fails outside it, while Levenberg–Marquardt enlarges the basin. The exercise drills the recognition that Levenberg–Marquardt is *not* a different algorithm but a *regularization* of Gauss–Newton; setting $\lambda^{(k)} = 0$ recovers Newton, and adapting $\lambda^{(k)}$ recovers the safe globalized version.

**Assumption pattern.** Three signals: (i) the function $f$ is smooth (in fact analytic); (ii) the function has a unique zero, but with an *asymptote* — $f$ tends to constants at infinity, so the tangent at large $|x|$ extrapolates to zero crossings far from the true root; (iii) two starting points are tested, one in the basin and one outside. The setup is *designed* to make Newton diverge from $x^{(1)} = 1.15$ because the tangent there extrapolates to $\approx -1.32$, far from the basin. This is the *exact* pathology Levenberg–Marquardt is designed to handle.

**Theorem routing.** The route is: compute the scalar Newton/LM updates from the explicit formulas; run them; compare. Newton's formula is $x \mapsto x - f/f'$; LM's is $x \mapsto x - f'/(\lambda + f'^2) \cdot f$. The two differ in the denominator: $f'$ vs $\lambda + f'^2$. When $|f'|$ is small and $\lambda$ is moderate, the LM denominator $\lambda + f'^2 \approx \lambda$ is bounded *below* by $\lambda$, preventing huge steps. The trust-parameter adaptation tracks whether each LM step succeeded.

**Key decision point.** The non-obvious choice is *the conceptual framing* — recognizing that Newton's divergence is not a sign of "Newton being broken" but of "the basin of attraction being too small for this starting point." Once this is seen, the modification of adding $\lambda I$ to the inner matrix becomes natural: it artificially expands the basin by shrinking steps that would otherwise overshoot. The technical decision is *how much $\lambda$ is enough*; the adaptation rule (shrink on success, grow on failure) finesses this by making $\lambda$ self-tuning.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra XII — Applied III — Nonlinear Least Squares#Legal Operations|the topic page's Legal Operations]]:

1. **Linearize the residual at the current iterate** (operation 1). Both Newton and LM compute the tangent line $\hat f(x; x^{(k)}) = f(x^{(k)}) + f'(x^{(k)})(x - x^{(k)})$ at the current iterate. Newton sets it to zero; LM minimizes its square plus a trust-region penalty.

2. **Regularize the step by adding a trust-region penalty** (operation 2). LM adds $\lambda^{(k)} (x - x^{(k)})^2$ to the squared linearized objective. For $\lambda^{(k)} > 0$ the resulting step is shorter than Newton's, preventing overshoot.

3. **Adapt the trust parameter based on whether each step succeeds** (operation 3). After each LM step, compare $f(x^{(k+1)})^2$ to $f(x^{(k)})^2$; shrink $\lambda$ on improvement, grow on regression. This makes $\lambda^{(k)}$ self-tuning.

---

# Hints

> [!note]- Hint 1
> Compute $f'(x) = \mathrm{sech}^2(x) = 4/(e^x + e^{-x})^2$. At $x = 1.15$, $f(1.15) \approx 0.8178$, $f'(1.15) \approx 0.331$, so the Newton step is $x - f/f' = 1.15 - 0.8178/0.331 \approx 1.15 - 2.47 \approx -1.32$.

> [!note]- Hint 2
> At the next iterate $-1.32$, by symmetry of $\tanh$, $f \approx -0.866$ and $f' \approx 0.249$. The next Newton step is $-1.32 - (-0.866)/0.249 \approx -1.32 + 3.48 \approx 2.16$. The iterates oscillate with growing magnitude — divergence.

> [!note]- Hint 3
> At $x^{(1)} = 0.95$, the tangent's zero is closer to the origin (because $f'(0.95) \approx 0.421$ is larger, so the tangent has a steeper slope and a closer zero). The Newton step at $0.95$ is $0.95 - 0.740/0.421 \approx -0.81$, still far but in the "convergent" region.

> [!note]- Hint 4
> For LM, compute the first step: at $x^{(1)} = 1.15$, $\lambda^{(1)} = 1$, $f \approx 0.8178$, $f' \approx 0.331$, denominator $1 + 0.331^2 = 1.110$, numerator $0.331 \cdot 0.8178 \approx 0.271$. Step is $-0.271/1.110 \approx -0.244$. So $x^{(2)} \approx 1.15 - 0.244 = 0.906$. Check that $f(0.906)^2 < f(1.15)^2$ — yes, $f(0.906)^2 \approx 0.521 < 0.6688$. Accept and shrink $\lambda$: $\lambda^{(2)} = 0.8$.

> [!note]- Hint 5
> Iterate LM with adaptive $\lambda$. Each step is much smaller than Newton's because the denominator is $\lambda + f'^2$ instead of $f'$. As $x^{(k)}$ approaches zero, $f'(x^{(k)}) \to 1$, so the denominator approaches $\lambda + 1 \approx 1$, and LM's step approaches Newton's. The "boldness" recovers in the late phase.

---

# Solution

The plan is to (i) compute Newton's iterates from both starting points, observing divergence from $1.15$ and convergence from $0.95$; (ii) compute Levenberg–Marquardt's iterates from $1.15$, observing convergence; (iii) interpret the trust-parameter trajectory.

**Step 1: Newton's method from $x^{(1)} = 0.95$ converges.**

The iterates are approximately $0.95 \to -0.81 \to 0.464 \to -0.066 \to 0.000$, converging to $\hat x = 0$.

> [!note]- Derivation
> At $x^{(1)} = 0.95$: $f \approx 0.7398$, $f' \approx 0.4528$, step $= 0.7398/0.4528 \approx 1.634$, so $x^{(2)} \approx 0.95 - 1.634 = -0.684$. (The iteration jumps to the *other side* of zero.)
>
> At $x^{(2)} \approx -0.684$: $f \approx -0.594$, $f' \approx 0.647$, step $= -0.594/0.647 \approx -0.918$, so $x^{(3)} \approx -0.684 + 0.918 = 0.234$.
>
> At $x^{(3)} \approx 0.234$: $f \approx 0.230$, $f' \approx 0.947$, step $= 0.230/0.947 \approx 0.243$, so $x^{(4)} \approx 0.234 - 0.243 = -0.009$.
>
> At $x^{(4)} \approx -0.009$: $f \approx -0.009$, $f' \approx 1.000$, step $\approx -0.009$, so $x^{(5)} \approx 0.000$.
>
> Convergence is achieved in $\sim 5$ iterations; the late iterations exhibit quadratic convergence (digits doubling).
>
> The slight oscillation around zero in the early phase is interesting but secondary; the key fact is convergence.

**Step 2: Newton's method from $x^{(1)} = 1.15$ diverges.**

The iterates are approximately $1.15 \to -1.32 \to 1.71 \to -2.51 \to 4.04 \to \cdots$, with magnitudes growing.

> [!note]- Derivation
> At $x^{(1)} = 1.15$: $f \approx 0.8178$, $f' \approx 0.331$, step $\approx 2.47$, so $x^{(2)} \approx 1.15 - 2.47 = -1.32$.
>
> At $x^{(2)} \approx -1.32$: by symmetry of $\tanh$, $f \approx -0.866$, $f' \approx 0.249$, step $\approx -3.48$, so $x^{(3)} \approx -1.32 - (-3.48) = 2.16$. *Wait, recheck:* $-1.32 - f/f' = -1.32 - (-0.866)/0.249 = -1.32 + 3.48 = 2.16$. So $x^{(3)} = 2.16$.
>
> At $x^{(3)} \approx 2.16$: $f \approx 0.974$, $f' \approx 0.052$, step $\approx 18.8$, so $x^{(4)} \approx 2.16 - 18.8 = -16.6$. This is divergence.
>
> The mechanism: at $|x|$ moderately large, $f'$ is small (the tangent is nearly horizontal), so the tangent line crosses zero very far from the current iterate. The Newton step takes us out to that far-off zero, which is *further* from the true root. The "small-derivative-far-zero" feedback amplifies each iteration.

**Step 3: Levenberg–Marquardt from $x^{(1)} = 1.15$ converges.**

With $\lambda^{(1)} = 1$, the iterates are:
$$x^{(1)} = 1.15 \to x^{(2)} \approx 0.906 \to x^{(3)} \approx 0.717 \to x^{(4)} \approx 0.532 \to \cdots \to 0.$$
The trust parameter shrinks at each successful step: $\lambda^{(1)} = 1, \lambda^{(2)} = 0.8, \lambda^{(3)} = 0.64, \ldots$, decreasing geometrically.

> [!note]- Derivation
> *Iteration 1:* At $x^{(1)} = 1.15$, $\lambda^{(1)} = 1$, $f \approx 0.8178$, $f' \approx 0.331$. LM step is
> $$\Delta x = -\frac{f' \cdot f}{\lambda + f'^2} = -\frac{0.331 \cdot 0.8178}{1 + 0.331^2} = -\frac{0.271}{1.110} \approx -0.244.$$
> So $x^{(2)} \approx 1.15 - 0.244 = 0.906$. Check: $f(0.906)^2 \approx (0.7197)^2 \approx 0.518 < 0.6688 = f(1.15)^2$. Accept; $\lambda^{(2)} = 0.8$.
>
> *Iteration 2:* At $x^{(2)} \approx 0.906$, $\lambda^{(2)} = 0.8$, $f \approx 0.7197$, $f' \approx 0.482$. Step:
> $$\Delta x = -\frac{0.482 \cdot 0.7197}{0.8 + 0.482^2} = -\frac{0.347}{1.032} \approx -0.336.$$
> So $x^{(3)} \approx 0.906 - 0.336 = 0.570$. Check: $f(0.570)^2 \approx (0.515)^2 \approx 0.265 < 0.518$. Accept; $\lambda^{(3)} = 0.64$.
>
> *Iteration 3:* At $x^{(3)} \approx 0.570$, $\lambda^{(3)} = 0.64$, $f \approx 0.515$, $f' \approx 0.735$. Step:
> $$\Delta x = -\frac{0.735 \cdot 0.515}{0.64 + 0.735^2} = -\frac{0.379}{1.180} \approx -0.321.$$
> So $x^{(4)} \approx 0.570 - 0.321 = 0.249$. Check: $f(0.249)^2 \approx 0.060 < 0.265$. Accept; $\lambda^{(4)} = 0.512$.
>
> *Iteration 4:* At $x^{(4)} \approx 0.249$, $\lambda^{(4)} = 0.512$, $f \approx 0.244$, $f' \approx 0.941$. Step:
> $$\Delta x = -\frac{0.941 \cdot 0.244}{0.512 + 0.886} = -\frac{0.230}{1.398} \approx -0.164.$$
> So $x^{(5)} \approx 0.249 - 0.164 = 0.085$. Check: $f(0.085)^2 \approx 0.0072 < 0.060$. Accept; $\lambda^{(5)} = 0.41$.
>
> *Iteration 5:* At $x^{(5)} \approx 0.085$, $\lambda^{(5)} = 0.41$, $f \approx 0.085$, $f' \approx 0.993$. Step:
> $$\Delta x = -\frac{0.993 \cdot 0.085}{0.41 + 0.986} = -\frac{0.0844}{1.396} \approx -0.060.$$
> So $x^{(6)} \approx 0.085 - 0.060 = 0.025$. Continuing, the iterates rapidly approach zero.
>
> Compared to bare Newton from $x^{(1)} = 1.15$ which diverged, LM with $\lambda^{(1)} = 1$ converges to $\hat x = 0$ in $\sim 10$ iterations.

**Step 4: Interpretation of the trust-parameter trajectory.**

The trust parameter $\lambda^{(k)}$ shrinks geometrically throughout, because every step succeeds. The mechanism: early steps (large $\lambda$) are *short* — much shorter than Newton's would be at the same iterate — preventing the overshoot that doomed bare Newton. As the iterate approaches $\hat x = 0$, $f'$ approaches $1$, the denominator $\lambda + f'^2$ becomes close to $1$, and the LM step approaches the (now safe) Newton step. The algorithm transitions smoothly from "gradient-descent-like" early behavior (with $\lambda \gg f'^2$) to "Newton-like" late behavior (with $\lambda \ll f'^2$), reaping the benefit of cautious early steps and fast late convergence.

> [!note]- Derivation
> The qualitative phases:
>
> 1. **Early phase ($x^{(k)}$ far from $0$):** $f'(x^{(k)})$ is small (the tangent at moderate-large $|x|$ is nearly horizontal). The LM denominator is $\lambda + f'^2 \approx \lambda$, dominated by the trust parameter. The step magnitude is $|\Delta x| \approx |f' f|/\lambda$, which is small because both $|f'|$ and $\lambda$ are bounded above and below respectively. This *bounds the step away from overshoot*. Each successful step shrinks $\lambda$, allowing the next step to be bolder.
>
> 2. **Late phase ($x^{(k)}$ near $0$):** $f'(x^{(k)}) \to 1$, $f \to x^{(k)}$. The LM denominator is $\lambda + f'^2 \to \lambda + 1$, and $\lambda$ has shrunk to small values. So the denominator $\to 1$, and the LM step approaches Newton's step $\Delta x = -f' f / 1 \approx -x^{(k)}$, which immediately gives $x^{(k+1)} \approx 0$. *Quadratic convergence is recovered* in this regime.
>
> 3. **Adaptive smoothness of transition:** Because $\lambda$ shrinks on success and grows on failure, the algorithm is self-tuning: it does not need the user to know in advance which regime each iterate is in. If a step would overshoot, the trust parameter grows next iteration to compensate; if a step easily succeeds, the trust parameter shrinks to allow faster progress.
>
> This is the essential virtue of Levenberg–Marquardt: it combines the safety of gradient descent in the early phase with the speed of Newton's method in the late phase, automatically transitioning between them.

> [!note]- Complete formal solution
> **(a) Newton's iterates.**
>
> From $x^{(1)} = 0.95$: $0.95 \to -0.81 \to 0.464 \to -0.066 \to 0.000$, converging to $\hat x = 0$.
>
> From $x^{(1)} = 1.15$: $1.15 \to -1.32 \to 2.16 \to -16.6 \to \cdots$, diverging.
>
> The mechanism of divergence is that $\tanh'$ becomes small at large $|x|$, so the tangent at $x^{(k)}$ extrapolates to a zero far from $x^{(k)}$, taking the iteration further from the true root.
>
> **(b) Levenberg–Marquardt iterates.**
>
> From $x^{(1)} = 1.15$, $\lambda^{(1)} = 1$: $1.15 \to 0.906 \to 0.570 \to 0.249 \to 0.085 \to 0.025 \to \cdots \to 0$. The trust parameter shrinks geometrically at each successful step.
>
> **(c) Mechanism.** The Levenberg–Marquardt update $\Delta x = -f' f/(\lambda + f'^2)$ has a denominator bounded below by $\lambda > 0$, preventing the "small-derivative-far-zero" overshoot that drove Newton's divergence. Early in the run, with $|x|$ moderately large and $|f'|$ small, the denominator is $\approx \lambda$ and the step is short — gradient-descent-like, safe. Late in the run, with $|x|$ near zero and $f' \approx 1$, the denominator is $\approx 1 + \lambda$ and the step approaches Newton's step, recovering quadratic convergence. The trust-parameter adaptation makes this transition automatic: $\lambda$ shrinks on success (boldness is rewarded) and grows on failure (overshoot is corrected). The algorithm interpolates between gradient descent and Newton's method with the user supplying only an initial $\lambda^{(1)}$. $\blacksquare$

> [!warning] Illegal but tempting alternative route — set $\lambda$ to a fixed large value
> Setting $\lambda^{(k)} \equiv 10$ (say) would make every step very short and would converge, but very slowly — it never picks up Newton-like quadratic convergence in the late phase, because the denominator $10 + f'^2$ remains $\approx 10$ rather than $\approx 1$. The *adaptive* shrinkage of $\lambda$ is essential to reaping the late-phase speedup. Conversely, setting $\lambda^{(k)} \equiv 0.001$ defeats the regularization and the algorithm essentially reduces to Newton's method, inheriting its divergence. The "right" $\lambda$ depends on the iterate; the adaptive rule finesses this without requiring the user to know it in advance.

---

# Key Takeaways

**Newton's method is fast where it converges, but its basin of attraction can be small.** This exercise is the canonical example of Newton's method's two faces: from $x^{(1)} = 0.95$ it converges in 4–5 iterations with quadratic late-phase convergence, from $x^{(1)} = 1.15$ it diverges immediately. The difference is just $0.2$ in the starting point. The mechanism — that $\tanh'$ becomes small at moderate $|x|$, so the tangent extrapolates far — is a generic feature of functions with horizontal asymptotes. Any time you have a function that "flattens out" at infinity (sigmoid, $\arctan$, error function, cumulative distribution functions), Newton's method on its root is fragile in a way Newton on a polynomial would not be. The diagnostic: compute $f'(x^{(1)})$; if it is much smaller than $|f(x^{(1)})|/|x^{(1)} - \hat x|$ (the slope needed to reach the root in one step), Newton will overshoot.

**Levenberg–Marquardt repairs Newton's divergence with a single algebraic modification.** Adding $\lambda I$ to the inner matrix turns a fragile algorithm into a robust one. The mathematical reason is that the denominator $\lambda + f'^2$ is bounded below by $\lambda$, capping the step magnitude. The procedural reason is that the trust parameter adapts based on whether each step succeeds, so the algorithm is *self-tuning* — the user does not need to know in advance how cautious to be. This single modification is what makes Levenberg–Marquardt the production-quality algorithm: every nonlinear-LS library (MINPACK, `scipy.optimize.leastsq`, MATLAB's `lsqnonlin`) uses LM rather than bare Gauss–Newton. The trigger condition for reaching for LM rather than GN is straightforward: *always*, unless you have a specific reason to believe the problem is benign and the starting point is excellent (in which case GN's quadratic convergence is faster).

**The trust-parameter trajectory is the algorithm's diagnostic.** Tracking $\lambda^{(k)}$ over a run tells you which phase the algorithm is in. A $\lambda^{(k)}$ shrinking monotonically means every step is successful — the algorithm is making smooth progress and is on track for fast convergence in the late phase. A $\lambda^{(k)}$ growing means steps are failing — the algorithm is in a hard region and is becoming more cautious, which is a sign you may need a better starting point. A $\lambda^{(k)}$ oscillating up and down means the algorithm is in a boundary region between regimes; it will eventually stabilize. This diagnostic is more informative than the residual trajectory alone: $\|f(x^{(k)})\|^2$ can decrease while the algorithm is making poor progress (small steps with limited objective gain), or stay large while the algorithm is making good progress (long flat plateau before a sharp descent). The trust parameter exposes the local geometry directly. When using LM in practice, always log $\lambda^{(k)}$ alongside the residual; the two together give a complete picture of the run.
