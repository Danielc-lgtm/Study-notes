---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Maximum Relative Velocity is c"
  - "Def - Velocity Relative to an Observer"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$ in the mostly-minus signature, with $\mathcal{O}$ an inertial observer of four-velocity $U_0$:

1. Starting from the orthogonal decomposition $U = \Gamma(U_0 + V)$ of a massive particle's four-velocity, derive the master relation $\Gamma^2(1 - |\mathbf V|^2) = 1$ and deduce $|\mathbf V| < 1$. Identify precisely *where* in the derivation the bound is forced.
2. A hypothetical **tachyon** moves on a *spacelike* worldline. Show that for such a particle the relative velocity satisfies $|\mathbf V| > 1$: the speed of light is the *minimum*, not the maximum, of a tachyon's speed relative to an ordinary observer.
3. Two particle beams cross at the origin of $\mathcal{O}$'s frame, beam $A$ moving at $+0.9$ along $e_1$ and beam $B$ at $-0.9$ along $e_1$. Compute (a) the *closing speed* of the two beams as $\mathcal{O}$ measures it, and (b) the speed of beam $B$'s particles in the rest frame of beam $A$'s particles. Explain why one can exceed $c$ and the other cannot.
4. Show that no finite sequence of boosts, however many, can carry a massive particle to $|\mathbf V| = c$, by relating the speed to the rapidity.

**Recall:**

The exercise rests on the maximum-relative-velocity theorem and the causal classification.

![[Thm - Maximum Relative Velocity is c#Statement]]

A four-vector is [[Def - Classification of Four-Vectors|classified]] by the sign of its Minkowski norm: timelike ($X \cdot X > 0$), null ($X \cdot X = 0$), spacelike ($X \cdot X < 0$). A massive particle's worldline is timelike; a photon's is null; a tachyon's would be spacelike. The [[Def - Velocity Relative to an Observer|relative velocity]] $V$ is spacelike with speed $|\mathbf V| = \sqrt{-V\cdot V}$.

---

# Convergent Strategy

**Problem class.** A *prove-a-bound* problem, the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|second strategy]]: the speed limit is established not by a dynamical argument (infinite energy) but by imposing the unit-norm constraint on the four-velocity decomposition and demanding the Lorentz factor be real.

**Assumption pattern.** A four-velocity decomposed against an observer is the source; the unit-norm constraint $U \cdot U = 1$ is the lever. The tachyon part flips the worldline class from timelike to spacelike, which flips the sign of the norm and the inequality. The two-beam part sets up a *closing speed* (a coordinate difference, which can exceed $c$) versus a *relative speed* (a genuine four-velocity quantity, which cannot) — the central distinction.

**Theorem routing.** Part 1 is the proof of [[Thm - Maximum Relative Velocity is c]] itself: expand $U \cdot U = 1$ using $U = \Gamma(U_0 + V)$ and read off $1 - |\mathbf V|^2 > 0$. Part 2 applies the same algebra to a spacelike tangent, where the [[Def - Classification of Four-Vectors|classification]] flips the sign and gives $|\mathbf V| > 1$. Part 3 contrasts the lab-frame closing speed (the Galilean difference, allowed to reach $2c$) with the genuine relative speed obtained via [[Thm - Relativistic Velocity Addition|velocity addition]] (bounded by $c$). Part 4 relates $|\mathbf V| = \tanh\varphi$ to the rapidity, where $\varphi < \infty$ gives $|\mathbf V| < 1$.

**Key decision point.** The crux of the whole exercise is the distinction in part 3 between a *closing speed* — the rate at which the gap between two objects shrinks as measured by a third observer, which is a coordinate difference and may legitimately exceed $c$ — and a *relative speed* — the speed of one object in the other's rest frame, which is a four-velocity scalar product and may not. Conflating the two is the classic error; the resolution is that a closing speed is not the speed of any single object relative to any single frame.

---

# Legal Operations Used

1. **Use the unit-norm constraint** (operation 4 from the topic page). Imposing $U \cdot U = 1$ on the decomposition gives $\Gamma^2(1-|\mathbf V|^2) = 1$, the source of the bound.

2. **Classify a four-vector by the sign of its norm** (operation 9). The worldline tangent's norm — positive (timelike), zero (null), negative (spacelike) — determines whether $|\mathbf V|$ is below, equal to, or above $c$.

3. **Add velocities relativistically** (from [[Thm - Relativistic Velocity Addition|velocity addition]]). The genuine relative speed of the two beams is computed by the relativistic composition, not the Galilean sum.

4. **Switch to rapidity** (operation, from [[Def - Rapidity]]). Writing $|\mathbf V| = \tanh\varphi$ converts the speed bound into the finiteness of the (unbounded) rapidity.

---

# Hints

> [!note]- Hint 1
> Expand $U \cdot U = \Gamma^2(U_0 + V)\cdot(U_0 + V)$ using $U_0 \cdot U_0 = 1$, $V \cdot U_0 = 0$, $V \cdot V = -|\mathbf V|^2$. Setting this to $1$ gives $\Gamma^2(1 - |\mathbf V|^2) = 1$. The bound is forced at the step where you demand $\Gamma^2 = 1/(1-|\mathbf V|^2)$ be a positive real — impossible if $|\mathbf V| \ge 1$.

> [!note]- Hint 2
> For a tachyon the worldline tangent $T \propto U_0 + V$ is *spacelike*, $T \cdot T < 0$, so $1 - |\mathbf V|^2 < 0$, giving $|\mathbf V| > 1$. The same algebra, with the worldline class flipped, flips the inequality.

> [!note]- Hint 3
> The *closing speed* is what $\mathcal{O}$ sees: beam $A$ at $+0.9$, beam $B$ at $-0.9$, so the gap shrinks at $0.9 + 0.9 = 1.8 > c$. This is fine — it is a coordinate difference, not the speed of anything in any rest frame. The *relative speed* of $B$ in $A$'s frame is the [[Thm - Relativistic Velocity Addition|relativistic sum]] $(0.9 + 0.9)/(1 + 0.9\cdot0.9) = 1.8/1.81 \approx 0.994 < 1$.

> [!note]- Hint 4
> Write $|\mathbf V| = \tanh\varphi$ with $\varphi$ the rapidity. Composing collinear boosts adds rapidities: $\varphi_{\text{total}} = \varphi_1 + \varphi_2 + \cdots$, which can be any finite real but never $\infty$. Since $\tanh\varphi < 1$ for all finite $\varphi$, no finite chain of boosts reaches $|\mathbf V| = 1$; the speed of light is "rapidity infinity", an asymptote.

---

# Solution

The route is to derive the bound from the unit-norm constraint (locating exactly where $c$ enters), flip the worldline class to see how a tachyon exceeds $c$, then resolve the two-beam puzzle by separating closing speed from relative speed, and finally explain the unreachability via rapidity. Step 1 proves the bound and pinpoints its origin; Step 2 treats the tachyon; Step 3 is the closing-versus-relative-speed distinction; Step 4 is the rapidity argument. The non-obvious thread is that "speed exceeding $c$" can be a harmless coordinate artefact (closing speed) or a genuine impossibility (relative speed), and the four-velocity formalism tells them apart.

**Step 1: The bound $|\mathbf V| < 1$ is the reality condition on $\Gamma$.**

> [!note]- Derivation
> Impose the unit-norm constraint on $U = \Gamma(U_0 + V)$:
> $$1 = U \cdot U = \Gamma^2(U_0 + V)\cdot(U_0 + V) = \Gamma^2\big(\underbrace{U_0\cdot U_0}_{1} + 2\underbrace{V\cdot U_0}_{0} + \underbrace{V\cdot V}_{-|\mathbf V|^2}\big) = \Gamma^2(1 - |\mathbf V|^2).$$
> This is the master relation. Solving for the Lorentz factor,
> $$\Gamma^2 = \frac{1}{1 - |\mathbf V|^2}.$$
> The bound is forced *here*: for a massive particle $\Gamma = U \cdot U_0$ is a finite real number, so $\Gamma^2$ is positive and finite, which requires the denominator $1 - |\mathbf V|^2$ to be positive — that is, $|\mathbf V| < 1$. If $|\mathbf V| = 1$ the denominator vanishes and $\Gamma$ diverges (the four-velocity ceases to exist — the photonic limit); if $|\mathbf V| > 1$ the denominator is negative and $\Gamma^2 < 0$, impossible for a real $\Gamma$. The speed limit is the requirement that a real, finite Lorentz factor exist, which is the requirement that the four-velocity be a genuine timelike unit vector.

**Step 2: A tachyon, with a spacelike worldline, has $|\mathbf V| > 1$.**

> [!note]- Derivation
> Suppose a particle moves on a *spacelike* worldline, with tangent $T \propto U_0 + V$ satisfying $T \cdot T < 0$. The same expansion gives
> $$T \cdot T \propto (U_0 + V)\cdot(U_0 + V) = 1 - |\mathbf V|^2.$$
> For this to be negative (spacelike), we need $1 - |\mathbf V|^2 < 0$, i.e.
> $$|\mathbf V| > 1.$$
> So a tachyon — a particle on a spacelike worldline — moves *faster* than light relative to any ordinary (timelike) observer. For a tachyon the speed of light is a *lower* bound, not an upper one: it can never slow below $c$, just as a massive particle can never reach $c$. The three [[Def - Classification of Four-Vectors|causal classes]] map exactly onto the three velocity regimes — timelike worldline ↔ $|\mathbf V| < 1$, null ↔ $|\mathbf V| = 1$, spacelike ↔ $|\mathbf V| > 1$ — and the speed of light is the seam. (No tachyons are known to exist; were they to, they would allow signalling into the past, see [[Ex - Classifying worldlines and why tachyons would signal into the past]].)

**Step 3: The closing speed is $1.8 > c$ (allowed); the relative speed is $\approx 0.994 < c$ (required).**

> [!note]- Derivation
> *(a) Closing speed, as $\mathcal{O}$ measures it.* Beam $A$ moves at $+0.9$ and beam $B$ at $-0.9$ along $e_1$, both in $\mathcal{O}$'s frame. The gap between them shrinks at the rate
> $$V_{\text{closing}} = |{+}0.9 - ({-}0.9)| = 1.8.$$
> This is $1.8c > c$, and it is perfectly legitimate: the closing speed is not the speed of any single object relative to any single frame — it is the rate at which $\mathcal{O}$ sees the *gap* shrink, a coordinate difference of two velocities, each below $c$. Nothing physical travels at $1.8c$; the bound $|\mathbf V| < c$ applies to the speed of one object in another's rest frame, which a closing speed is not.
>
> *(b) Relative speed of $B$ in $A$'s rest frame.* This *is* a genuine relative velocity — the speed of $B$'s particles as measured by an observer riding beam $A$. Boost to $A$'s rest frame (velocity $+0.9$) and use [[Thm - Relativistic Velocity Addition|relativistic velocity addition]]:
> $$V_{B\text{ in }A} = \frac{V_B' }{\cdots} = \frac{0.9 + 0.9}{1 + (0.9)(0.9)} = \frac{1.8}{1 + 0.81} = \frac{1.8}{1.81} \approx 0.9945.$$
> This is below $c$, as it must be, because it is the speed of one massive particle relative to another's rest frame — a four-velocity scalar product, bounded by the theorem. The resolution of the apparent paradox is that the closing speed ($1.8c$) and the relative speed ($0.994c$) are *different quantities*: the first is a coordinate difference in a third frame, the second is a genuine relative velocity, and only the second is bounded by $c$.

**Step 4: No finite chain of boosts reaches $c$, because rapidity is finite but the speed asymptotes.**

> [!note]- Derivation
> Write the speed in terms of the [[Def - Rapidity|rapidity]] $\varphi$:
> $$|\mathbf V| = \tanh\varphi.$$
> Composing collinear boosts *adds rapidities*: applying boosts of rapidity $\varphi_1, \varphi_2, \ldots, \varphi_n$ in succession gives a total rapidity $\varphi_{\text{total}} = \varphi_1 + \varphi_2 + \cdots + \varphi_n$. For any finite number of finite boosts, $\varphi_{\text{total}}$ is a finite real number, and
> $$|\mathbf V_{\text{total}}| = \tanh\varphi_{\text{total}} < 1\qquad\text{for every finite }\varphi_{\text{total}},$$
> since $\tanh$ asymptotes to $1$ but never reaches it. So no finite sequence of boosts — no finite amount of acceleration — can carry a massive particle to the speed of light. The speed of light is "rapidity infinity": to reach $|\mathbf V| = 1$ would require $\varphi_{\text{total}} = \infty$, an infinite sum of boosts. This is the rapidity face of the speed ceiling: velocity is trapped in $(-1,1)$ while rapidity fills all of $\mathbb{R}$, and the additive structure lives on the rapidity, with $c$ at the unreachable horizon.

> [!note]- Complete formal solution
> Imposing $U \cdot U = 1$ on $U = \Gamma(U_0 + V)$ gives $\Gamma^2(1 - |\mathbf V|^2) = 1$, so $\Gamma^2 = (1 - |\mathbf V|^2)^{-1}$; reality and finiteness of $\Gamma$ force $|\mathbf V| < 1$ (at $|\mathbf V| = 1$, $\Gamma$ diverges; beyond, $\Gamma^2 < 0$). For a tachyon the worldline tangent is spacelike, $1 - |\mathbf V|^2 < 0$, giving $|\mathbf V| > 1$ — light's speed is a tachyon's *minimum*. The three [[Def - Classification of Four-Vectors|causal classes]] are the three velocity regimes. For two beams at $\pm0.9$, the lab closing speed is $1.8 > c$ (a harmless coordinate difference, the speed of nothing in any frame), while the relative speed of one beam in the other's rest frame is the [[Thm - Relativistic Velocity Addition|relativistic sum]] $1.8/1.81 \approx 0.994 < c$ (a genuine relative velocity, bounded). Finally, $|\mathbf V| = \tanh\varphi$ with rapidities adding under composition: any finite chain of boosts gives finite $\varphi$, hence $\tanh\varphi < 1$, so $c$ is unreachable — "rapidity infinity". $\blacksquare$

---

# Key Takeaways

**The speed limit is a reality condition on the Lorentz factor, not a dynamical fact about energy.** The cleanest derivation of $|\mathbf V| < c$ uses no force, no mass increase, no infinite energy — only the unit-norm constraint $U \cdot U = 1$, which forces $\Gamma^2 = (1-|\mathbf V|^2)^{-1}$, and the demand that this be a positive finite real. The speed of light is the value at which $\Gamma$ diverges and beyond which it goes imaginary, signalling that no timelike four-velocity exists. The reusable insight is that the speed limit lives in the *kinematics* — in the structure of a unit timelike vector in an indefinite metric — and the dynamical story (it takes infinite energy to reach $c$, because $E = \Gamma m \to \infty$) is a *consequence* of this kinematic fact, not its cause. Whenever you need to argue that something cannot exceed $c$, the first move is to ask whether it is the speed of a timelike object relative to a frame; if so, the unit-norm constraint settles it geometrically.

**Distinguish a closing speed from a relative speed: only the latter is bounded by $c$.** This is the single most common source of "faster than light" confusion, and the exercise drills the resolution. A *closing speed* is the rate at which a third observer sees the gap between two objects shrink — a difference of two coordinate velocities, which can be anything up to $2c$ and is the speed of *nothing in any rest frame*. A *relative speed* is the speed of one object in the other's rest frame — a genuine four-velocity quantity, $\Gamma = U \cdot U_0$, bounded by $c$. Two beams approaching at $\pm0.9c$ close at $1.8c$ (fine) but each sees the other at $0.994c$ (required). The diagnostic: ask "is this the speed of one thing in one frame, or the rate of change of a gap as seen by a third party?" — the former is bounded, the latter is not. The same distinction resolves apparent superluminal motion in astrophysical jets and the "scissors paradox" of a fast-closing intersection point.

**Rapidity is the unbounded coordinate, and the speed limit is an asymptote, not a wall.** Writing $|\mathbf V| = \tanh\varphi$ recasts the speed ceiling as the finiteness of the rapidity: collinear boosts add rapidities, any finite chain of boosts gives a finite rapidity, and $\tanh$ of a finite number is below $1$, so no amount of boosting reaches $c$. The speed of light is "rapidity infinity", a horizon approached but never attained. This is why rapidity, not velocity, is the natural additive parameter of relativity — the group law of boosts is *addition* on the rapidity, *nonlinear composition* on the velocity — and it explains structurally why the speed limit is unbreakable by composition: you would need to add up to infinite rapidity. The trigger to switch to rapidity: whenever boosts must be composed or iterated, or whenever the nonlinearity of velocity addition is obstructing, replace $|\mathbf V|$ by $\tanh\varphi$ and the composition becomes ordinary addition. The companion exercise on the causal meaning of the bound is [[Ex - Classifying worldlines and why tachyons would signal into the past]].
