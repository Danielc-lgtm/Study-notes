---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Reversed Triangle Inequality"
  - "Def - Classification of Four-Vectors"
  - "Def - Proper Time"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$.

1. **Reversed Cauchy–Schwarz.** For two future-pointing timelike four-vectors $U, V$, prove $U\cdot V \ge \|U\|\,\|V\|$ (the *reverse* of the Euclidean inequality), with equality iff $U \parallel V$. Hence prove the reversed triangle inequality $\|U + V\| \ge \|U\| + \|V\|$.
2. **Longest worldline.** Two events $A$ and $R$ are timelike-separated, with $R - A = (2T, 0, 0, 0)$ in some frame. Compare the proper time along (i) the straight inertial worldline from $A$ to $R$, and (ii) a bent worldline that goes from $A$ to an intermediate event $P = (T, vT, 0, 0)$ and then to $R$. Show the straight one is longer, and compute the deficit.
3. Generalise: prove that *any* timelike worldline from $A$ to $R$ has proper time at most that of the straight inertial worldline, with equality only for the straight line. (This is the longest-worldline / clock-extremisation principle.)
4. Interpret the result as the resolution of the twin paradox: the travelling twin (bent worldline) ages less than the stay-at-home twin (straight worldline), purely as a consequence of the geometry.

**Recall:**

![[Thm - The Reversed Triangle Inequality#Statement]]

A four-vector $X$ is [[Def - Classification of Four-Vectors|timelike]] if $X\cdot X > 0$ and **future-pointing** if $X^0 > 0$; its Minkowski norm is $\|X\| = \sqrt{X\cdot X}$. The [[Def - Proper Time|proper time]] along a timelike worldline is $\tau = \int\sqrt{ds^2} = \int\sqrt{dt^2 - d\mathbf{x}^2}$, the time read by a clock carried along it; for a straight timelike segment $U$ it is $\|U\|$. The forward light cone $\{X : X^0 > |\mathbf{X}|\}$ is convex.

---

# Convergent Strategy

**Problem class.** A *prove-an-inequality / resolve-a-paradox* hybrid. Parts 1–3 are the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] and its worldline corollary; Part 4 is the twin paradox, resolved geometrically per the [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group#Problem-Solving Strategy|topic strategy]].

**Assumption pattern.** Future-pointing timelike vectors — the hypothesis of the reversed triangle inequality. The signpost is "worldline segments with the same endpoints, one straight, one bent": each segment is a future-timelike vector, and the inequality compares the bent total to the straight total.

**Theorem routing.** Part 1 proves the reversed Cauchy–Schwarz in the rest frame of $U$ (using [[Thm - Invariance of the Spacetime Interval|Lorentz invariance]]) and completes the square; Part 2 plugs in numbers; Part 3 inducts over a polygonal worldline and passes to the continuum; Part 4 reads off the twins. The route is: reversed Cauchy–Schwarz $\to$ reversed triangle inequality $\to$ polygonal induction $\to$ continuum $\to$ twin paradox.

**Key decision point.** The decisive recognition is that the inequality *reverses* relative to Euclidean intuition, and that this is because the metric's minus sign flips the direction of Cauchy–Schwarz. A reader who carries Euclidean instinct "proves" the wrong inequality. The second subtlety (Part 3) is that the continuum statement follows from the two-vector statement by *induction over a polygon plus a limit*, not by any new idea.

---

# Legal Operations Used

1. **Compute an invariant in the convenient frame (operation 7 from the topic page).** The reversed Cauchy–Schwarz is proved by evaluating $U\cdot V$ in the rest frame of $U$, where $U = (\|U\|, \mathbf{0})$ and the computation is trivial.

2. **Classify a worldline / four-vector by the sign of its norm (operation 9 from the topic page).** Every segment is future-timelike, and the convexity of the forward cone is what keeps sums admissible.

3. **Apply the reversed triangle inequality (operation: the chapter's signature inequality).** Identifying the straight worldline as the longest in proper time.

---

# Hints

> [!note]- Hint 1
> Evaluate $U\cdot V$ in the rest frame of $U$, where $U = (\|U\|, 0, 0, 0)$ and $V = (V^0, \mathbf{V})$. Then $U\cdot V = \|U\|V^0$. Since $V$ is future-timelike, $V^0 = \sqrt{\|V\|^2 + |\mathbf{V}|^2} \ge \|V\|$. So $U\cdot V \ge \|U\|\|V\|$ — the inequality runs the *opposite* way to Euclidean Cauchy–Schwarz.

> [!note]- Hint 2
> Straight: $\|R - A\| = \sqrt{(2T)^2} = 2T$. Bent: each leg is $(T, \pm vT)$ with norm $\sqrt{T^2 - v^2T^2} = T/\gamma$, total $2T/\gamma$. Since $\gamma > 1$, the bent path's proper time $2T/\gamma$ is less than $2T$. The deficit is $2T(1 - 1/\gamma)$.

> [!note]- Hint 3
> Approximate any timelike worldline by a polygon of $N$ small future-timelike steps $U_1, \dots, U_N$. The reversed triangle inequality applied repeatedly gives $\|\sum_k U_k\| \ge \sum_k \|U_k\|$. The left side is the straight chord's proper time; the right side is the polygon's. Let $N \to \infty$.

> [!note]- Hint 4
> Identify the stay-at-home twin with the straight worldline ($A \to R$) and the traveller with the bent one ($A \to P \to R$). The straight one is longer in proper time, so the traveller ages less. No acceleration bookkeeping is needed — the geometry decides.

---

# Solution

The exercise builds the longest-worldline principle from the ground up. Step 1 proves the reversed Cauchy–Schwarz (the engine) and the reversed triangle inequality (one completing-the-square step). Step 2 computes the twin numbers. Step 3 promotes the two-vector inequality to arbitrary worldlines by induction and a limit. Step 4 reads off the twin paradox as pure geometry.

**Step 1: reversed Cauchy–Schwarz and the reversed triangle inequality.**

> [!note]- Derivation
> *Reversed Cauchy–Schwarz.* By [[Thm - Invariance of the Spacetime Interval|Lorentz invariance]], the scalars $U\cdot V$, $\|U\|$, $\|V\|$ are frame-independent, so evaluate in the rest frame of $U$: there $U = (\|U\|, 0, 0, 0)$ and $V = (V^0, \mathbf{V})$ with $V^0 > 0$ and $\|V\|^2 = (V^0)^2 - |\mathbf{V}|^2 > 0$. Then
> $$U\cdot V = \|U\|\,V^0 - \mathbf{0}\cdot\mathbf{V} = \|U\|\,V^0.$$
> Since $V^0 = \sqrt{\|V\|^2 + |\mathbf{V}|^2} \ge \|V\|$, we get $U\cdot V = \|U\|V^0 \ge \|U\|\|V\|$, with equality iff $|\mathbf{V}| = 0$, i.e. $V \parallel U$. This is the *reverse* of the Euclidean Cauchy–Schwarz $\mathbf{a}\cdot\mathbf{b} \le |\mathbf{a}||\mathbf{b}|$, and the reversal is caused entirely by the minus sign in the metric (which makes the time component dominate).
>
> *Reversed triangle inequality.* First, $U + V$ is future-timelike: $(U+V)^0 = \|U\| + V^0 > 0$ and $(U+V)\cdot(U+V) = \|U\|^2 + 2U\cdot V + \|V\|^2 > 0$ (all three terms positive by the above). So $\|U+V\|$ is real. Now complete the square:
> $$\|U+V\|^2 = \|U\|^2 + 2\,U\cdot V + \|V\|^2 \ge \|U\|^2 + 2\|U\|\|V\| + \|V\|^2 = (\|U\| + \|V\|)^2,$$
> and taking non-negative square roots, $\|U + V\| \ge \|U\| + \|V\|$, with equality iff $U \parallel V$.

**Step 2: the twin numbers.**

> [!note]- Derivation
> *Straight worldline (stay-at-home).* The displacement is $R - A = (2T, 0, 0, 0)$, future-timelike, with proper time
> $$\tau_{\text{straight}} = \|R - A\| = \sqrt{(2T)^2 - 0} = 2T.$$
>
> *Bent worldline (traveller).* The two legs are $U = P - A = (T, vT, 0, 0)$ and $V = R - P = (T, -vT, 0, 0)$, each future-timelike with
> $$\|U\| = \|V\| = \sqrt{T^2 - v^2T^2} = T\sqrt{1 - v^2} = T/\gamma.$$
> The bent worldline's proper time is the sum of the legs, $\tau_{\text{bent}} = \|U\| + \|V\| = 2T/\gamma$. Note $U + V = (2T, 0, 0, 0) = R - A$, so the reversed triangle inequality gives $\|U + V\| = 2T \ge \|U\| + \|V\| = 2T/\gamma$, i.e.
> $$\tau_{\text{straight}} = 2T \ge \frac{2T}{\gamma} = \tau_{\text{bent}},$$
> with strict inequality since $\gamma > 1$ (the legs are not parallel). The **deficit** is
> $$\tau_{\text{straight}} - \tau_{\text{bent}} = 2T\Big(1 - \frac{1}{\gamma}\Big) > 0.$$
> The straight worldline accumulates more proper time; the bent one is "shorter" by $2T(1 - 1/\gamma)$.

**Step 3: any worldline is at most as long as the straight one.**

> [!note]- Derivation
> Let $\Gamma$ be any timelike worldline from $A$ to $R$. Approximate it by a polygon through $N+1$ events $A = X_0, X_1, \dots, X_N = R$, with steps $U_k = X_k - X_{k-1}$, each future-timelike for $N$ large (the worldline is timelike, so small enough chords are too). The polygon's proper time is $\sum_{k=1}^N \|U_k\|$.
>
> Apply the reversed triangle inequality repeatedly (induction on $N$): $\|U_1 + U_2\| \ge \|U_1\| + \|U_2\|$, then $\|(U_1 + U_2) + U_3\| \ge \|U_1 + U_2\| + \|U_3\| \ge \|U_1\| + \|U_2\| + \|U_3\|$, and so on, giving
> $$\Big\|\sum_{k=1}^N U_k\Big\| \ge \sum_{k=1}^N \|U_k\|.$$
> The left side is $\|X_N - X_0\| = \|R - A\| = 2T$, the proper time of the straight worldline. The right side is the polygon's proper time. So the straight chord is at least as long as any inscribed polygon. Refining the polygon ($N \to \infty$) makes its proper time converge from below to $\int_\Gamma \sqrt{ds^2}$, the proper time of $\Gamma$, so
> $$\tau_{\text{straight}} = \|R - A\| \ge \int_\Gamma \sqrt{ds^2} = \tau_\Gamma,$$
> with equality only if every step is parallel to $R - A$, i.e. only if $\Gamma$ is the straight inertial worldline. The inertial worldline **maximises** proper time among all timelike worldlines between two events.

**Step 4: the twin paradox as geometry.**

> [!note]- Derivation
> Identify the stay-at-home twin with the straight worldline $A \to R$ and the travelling twin with the bent worldline $A \to P \to R$ (out to a distant point at speed $v$, then back). By Steps 2–3 the straight worldline has strictly more proper time, so the stay-at-home twin ages $2T$ while the traveller ages only $2T/\gamma < 2T$: **the traveller returns younger.**
>
> The resolution requires no bookkeeping of who feels acceleration and no analysis of the turnaround: it is a statement about the *lengths of two curves in Minkowski space*. The two worldlines genuinely differ — one is straight, one is bent — and by the reversed triangle inequality the straight one is longer in proper time. The apparent "symmetry" of the twins (each sees the other recede and return) is false because the worldlines are geometrically different: only the traveller's bends. The deficit $2T(1 - 1/\gamma)$ is the proper time the traveller loses by taking the bent path, exactly as a Euclidean detour adds distance — except that in Minkowski geometry the detour *subtracts* proper time, because the metric's minus sign makes spatial motion cost ageing.

> [!note]- Complete formal solution
> *Reversed Cauchy–Schwarz.* In the rest frame of $U$, $U\cdot V = \|U\|V^0 \ge \|U\|\|V\|$ since $V^0 = \sqrt{\|V\|^2 + |\mathbf{V}|^2} \ge \|V\|$, equality iff $V \parallel U$. *Reversed triangle inequality.* $U+V$ is future-timelike, and $\|U+V\|^2 = \|U\|^2 + 2U\cdot V + \|V\|^2 \ge (\|U\|+\|V\|)^2$, so $\|U+V\| \ge \|U\|+\|V\|$. *Twins.* Straight: $\|R-A\| = 2T$. Bent legs $U = (T, vT), V = (T,-vT)$ each of norm $T/\gamma$, total $2T/\gamma$, with $U + V = (2T, 0) = R - A$, so $2T \ge 2T/\gamma$, deficit $2T(1 - 1/\gamma)$. *General.* Any timelike worldline, polygonised into future-timelike steps $U_k$, has proper time $\sum\|U_k\| \le \|\sum U_k\| = \|R - A\| = 2T$ by iterated reversed triangle inequality, with equality only for the straight line; taking the polygon limit, the inertial worldline maximises proper time. *Twin paradox.* The stay-at-home twin (straight) ages $2T$, the traveller (bent) ages $2T/\gamma < 2T$; the asymmetry is geometric — only the traveller's worldline bends — and needs no acceleration accounting. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> The seductive wrong move in Part 4 is the symmetry argument: "from the traveller's frame the stay-at-home twin recedes and returns, so by symmetry the stay-at-home twin should be younger." This silently assumes the two situations are interchangeable, which they are not — the worldlines are *geometrically distinct* (one straight, one bent), and the reversed triangle inequality is not symmetric between them. The error is to treat "each sees the other move" as a true symmetry; it is not, because the bent worldline is an objective, frame-independent fact (the traveller's worldline has a corner; the stay-at-home's does not). The geometric resolution sidesteps the entire frame-comparison: lengths of curves are invariant, and the straight one is simply longer.

---

# Key Takeaways

**The triangle inequality reverses in Minkowski space, and one metric sign is the whole reason.** The central reusable fact is that for future-timelike vectors $\|U + V\| \ge \|U\| + \|V\|$ — the *opposite* of the Euclidean triangle inequality — because the underlying Cauchy–Schwarz reverses to $U\cdot V \ge \|U\|\|V\|$. Both reversals trace to the minus sign in the metric, which makes a future-timelike vector's time component dominate its norm. Whenever you compute with timelike four-vectors, suspend Euclidean instinct: sums are *longer* than the sum of parts, straight is *longest*, and "shortest path" intuitions are exactly backwards. The trigger to flip your reasoning is "future-timelike vectors in the forward cone"; the convexity of that cone is what makes the reversed inequalities hold, and they fail outside it (for spacelike vectors, or vectors in opposite cones).

**Straight worldlines maximise proper time — the inertial path is longest, and every detour costs ageing.** This is the geometric content of the twin paradox and the special-relativistic seed of the geodesic principle. In Euclidean space the straight line minimises distance; in Minkowski space the straight (inertial) worldline *maximises* proper time between two timelike-separated events, and any bending strictly reduces it. The proof is the reversed triangle inequality iterated over a polygon and passed to the continuum — no new idea beyond the two-vector inequality. To compare the ageing of observers on different worldlines, you need no time-dilation bookkeeping: just compare how bent the worldlines are, because the straightest ages the most. This principle generalises directly to general relativity, where freely-falling worldlines are the timelike geodesics of *locally* maximal proper time, and "free fall ages the most" is the curved-spacetime twin paradox.

**Geometric arguments dissolve relativistic paradoxes without frame bookkeeping.** The twin paradox is resolved here entirely by the lengths of two curves, with no analysis of who accelerates or what happens at the turnaround. This is the most powerful lesson for handling paradoxes: recast the situation as a statement about Lorentz-invariant quantities (here, proper times, which are the Minkowski lengths of worldlines), and the frame-dependent confusion evaporates because invariants do not depend on the observer. The false "symmetry" between the twins is exposed the moment you notice the worldlines are objectively different shapes — one straight, one bent — a frame-independent fact. Whenever two correct-looking relativistic arguments conflict, look for the invariant quantity that settles the matter unambiguously; the proper time along a worldline is the archetype, and its extremisation by inertial motion is the resolution of an entire class of paradoxes.
