---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Def - The Lorentz Transformation"
  - "Def - Galilean Spacetime and Its Failure"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, giving the $c$-restored form where it aids recognition. Two inertial frames $S$ and $S'$ have coordinates $(t, x)$ and $(t', x')$ in $1+1$ dimensions (transverse $y, z$ are appended at the end), with $S'$ moving at velocity $v$ along $x$ and origins coinciding at $t = t' = 0$. The Lorentz factor is $\gamma = \gamma_v = (1 - v^2)^{-1/2}$. We write the transformation as $x' = f(x,t)$, $t' = g(x,t)$ while deriving its form, and as a matrix $\Lambda$ once linear. Full registry on [[Special Relativity I — Postulates and Lorentz Transformations]].

---

# Statement

> **Theorem (Uniqueness of the Lorentz transformation).** Let $S$ and $S'$ be inertial frames with $S'$ moving at velocity $v$ along the common $x$-axis and origins coinciding at $t = t' = 0$. Assume only:
> (i) the law of inertia holds in both frames (free particles move in straight lines);
> (ii) the spatial origin of $S'$ ($x' = 0$) follows $x = vt$ in $S$;
> (iii) space is isotropic and no inertial frame is preferred (the principle of relativity);
> (iv) light propagates at speed $c$ in both frames (the constancy of light).
> Then the coordinate transformation relating $S$ and $S'$ is uniquely the Lorentz boost
> $$x' = \gamma(x - vt), \qquad t' = \gamma(t - vx), \qquad y' = y, \qquad z' = z, \qquad \gamma = \frac{1}{\sqrt{1 - v^2}}.$$
> No other transformation satisfies (i)–(iv).

> **Corollary (Galilean limit).** Dropping (iv) and instead imposing absolute time $t' = t$ forces $\gamma = 1$ and returns the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]] $x' = x - vt$, $t' = t$. Imposing (i)–(iii) alone leaves a one-parameter family with $\gamma = \gamma_v$ undetermined, fixing some invariant speed (possibly infinite); (iv) selects the member whose invariant speed is exactly $c$.

---

# Motivation

A physical theory earns its authority when its central equations are not guessed but *forced* — when one can show that, given a short list of physical demands, no other law is possible. The Lorentz transformation is the paradigm case, and this theorem is the proof. The [[Def - Galilean Spacetime and Its Failure|Galilean transformation]] has just been demolished by the constancy of light; something must replace it; and the claim is that the replacement is not a matter of taste or convention but is determined to the last coefficient by the two [[Def - Inertial Frame and the Postulates of Special Relativity|postulates]] together with the law of inertia.

The importance is twofold. First, it converts special relativity from a collection of strange formulas into a *deduction*: time dilation, length contraction, and velocity addition are not independent postulates but consequences of this one transformation, which is itself a consequence of the postulates. Second, it isolates exactly which Newtonian assumption was wrong. The derivation keeps linearity, keeps the moving-origin condition, keeps the relativity principle — and the *only* thing it changes is the value of one coefficient $\gamma$, forced away from the Galilean $\gamma = 1$ by the constancy of light. The casualty is absolute time: the clock equation acquires a position-dependent term $t' = \gamma(t - vx)$, and simultaneity becomes relative. This theorem is where one sees, line by line, that giving up the absolute clock is not optional.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypotheses are four physical demands; the point of input-broadening is to recognise the many guises each wears in a problem.

The first disguised source is **"the map sends straight worldlines to straight worldlines"** standing in for hypothesis (i). Any time a problem stipulates that both frames are inertial — or that free particles look free in both, or that the transformation is "affine", or that it has a constant Jacobian — hypothesis (i) is in force and linearity follows. The bridge is the affine-geometry fact that a bijection of $\mathbb{R}^n$ carrying lines to lines is linear (given a fixed origin). *Example problem:* a problem states only that two observers are inertial and asks for the most general transformation between them; recognise that linearity is already granted and write $x' = \alpha_1 x + \alpha_2 t$ immediately.

The second disguised source is **"the relative velocity is given"** standing in for hypotheses (ii) and (iii) together. A stated relative velocity $v$ fixes the moving-origin condition (the $S'$ origin is at $x = vt$) and, through isotropy, the evenness $\gamma_v = \gamma_{-v}$. The bridge is that "moving at $v$" is precisely the statement $x' = 0 \Leftrightarrow x = vt$, while "no preferred frame" forces the same $\gamma$ in the forward and inverse maps. *Example problem:* given that $S'$ moves at $v$, derive that the inverse transformation is obtained by $v \to -v$ — this is hypothesis (iii) in action, not an extra assumption.

The third disguised source is **"some signal has the same speed in both frames"** standing in for hypothesis (iv). The crucial input need not be phrased as "light": any worldline asserted to have an identical speed in $S$ and $S'$ plays the role light plays, fixing $\gamma$. The bridge is that the condition "$x = wt$ in $S$ maps to $x' = wt'$ in $S'$" for a common speed $w$ pins $\gamma$ to $(1 - v^2/w^2)^{-1/2}$; light is the case $w = c$. *Example problem:* a thought experiment posits a hypothetical signal of invariant speed $w$; the *same* derivation yields a "Lorentz transformation" with $c$ replaced by $w$, showing that the universal speed is whatever signal is invariant.

**Targets (Output Amplification)**

The conclusion is the boost formula together with $\gamma = (1 - v^2)^{-1/2}$.

Combine the conclusion with **a specific event or worldline**. Feeding any event's $S$-coordinates through the boost gives its $S'$-coordinates; specialising to two events on a clock's worldline yields time dilation, to the two ends of a rod yields length contraction, to a composite velocity yields the addition law. The combination is useful because *every* elementary relativistic effect is the boost applied to a cleverly chosen pair of events. *Example:* the proper time between two events at the same place in $S$ is read off $t' = \gamma t$ directly.

Combine the conclusion with **the requirement of consistency under composition**. Two boosts of velocities $v_1, v_2$ along the same axis must compose to another valid transformation; carrying out the matrix product and demanding the result again have boost form yields the velocity-addition law $(v_1 + v_2)/(1 + v_1 v_2)$ and shows the boosts form a one-parameter group. The combination is nonobvious because it turns a uniqueness statement into a *group* statement — the boosts along an axis are forced to be closed under composition, hence to be a subgroup of the [[Def - The Lorentz Group|Lorentz group]]. *Example:* deriving [[Thm - Relativistic Velocity Addition|relativistic velocity addition]] purely from composing two instances of this theorem's output.

Combine the conclusion with **the interval $\Delta s^2 = \Delta t^2 - \Delta x^2$**. Substituting the boost into $\Delta t'^2 - \Delta x'^2$ and watching it reduce to $\Delta t^2 - \Delta x^2$ shows the transformation preserves the interval; this elevates the boost to "the interval-preserving linear map", the structural definition of the [[Def - The Lorentz Group|Lorentz group]]. The combination is the bridge from this postulate-based derivation to the geometric reorganisation of [[Thm - Invariance of the Spacetime Interval|the next chapter]]. *Example:* proving that the value of $\gamma$ forced here is exactly the value that makes $\Delta s^2$ invariant.

---

# Why Is It True

The result is true because each physical demand removes exactly one degree of freedom from the most general transformation, and four demands suffice to remove all four.

**Each postulate kills one unknown; the constancy of light is the only numerical input, and it is what forces $\gamma \ne 1$.**

Start with the most general transformation that could relate two frames: in $1+1$ dimensions a map $(t, x) \mapsto (t', x')$ has, a priori, infinitely many degrees of freedom. The law of inertia collapses this to a linear map — four real coefficients. The moving-origin condition spends two of them, forcing the spatial equation into $x' = \gamma(x - vt)$ with one unknown scale $\gamma$ and leaving the time equation $t' = \beta_1 x + \beta_2 t$ with two more. Isotropy and reciprocity tie the time coefficients to $\gamma$ and force $\gamma$ to be even in $v$, but they do not fix its *value* — at this stage the transformation is determined up to the single function $\gamma_v$, and *any* choice gives a self-consistent "relativity" with some invariant speed. (The Galilean transformation is the choice $\gamma = 1$, invariant speed infinite.) Only the second postulate carries a number. Demanding that one specific worldline — a light ray — have the *same* speed $c$ in both frames is one equation, and it is exactly the equation needed to solve for $\gamma$. The value it returns, $\gamma = (1 - v^2)^{-1/2}$, is greater than $1$ for every $v \ne 0$, which is the precise sense in which the constancy of light pushes the transformation away from the Galilean one.

The cleanest way to *feel* why $\gamma$ comes out as it does: the two light conditions, read forward and backward, give $t' = \gamma(1 - v)t$ and $t = \gamma(1 + v)t'$. Multiply them and the $t, t'$ cancel, leaving $1 = \gamma^2(1 - v)(1 + v) = \gamma^2(1 - v^2)$. The product structure is the heart of it: the forward light condition carries a factor $(1 - v)$, the backward one a factor $(1 + v)$, and the principle of relativity (same $\gamma$ both ways) forces their geometric mean to be $\gamma^{-1}$. That is why the answer is $1/\sqrt{1 - v^2}$ and not something else — it is the geometric mean of the Doppler-like factors $(1 \mp v)$, which is exactly the [[Ex - The k-calculus (Bondi) derivation|Bondi k-factor]] picture in disguise.

Finally, the time transformation is not an independent input — it is forced. Once the spatial equation $x' = \gamma(x - vt)$ and its inverse $x = \gamma(x' + vt')$ are both known with the same $\gamma$, substituting one into the other and solving for $t'$ leaves no freedom: $t' = \gamma(t - vx)$ is the only possibility. The clock equation was, in Tong's phrase, "already lurking" in the consistency of the two spatial relations.

---

# What Makes This Hard

The conceptual hurdle is believing that the postulates *suffice* — that no extra assumption sneaks in — so the place to be vigilant is the evenness $\gamma_v = \gamma_{-v}$, which is easy to assume without realising it is a consequence of isotropy and the relativity principle rather than a free gift. The most common technical error is in the light-condition step: students substitute $x = ct$ into $x' = \gamma(x - vt)$ but forget that they must *also* demand $x' = ct'$ and use the inverse relation, so they end up with one equation for two unknowns and cannot solve for $\gamma$. The subtle point is that the time equation is *derived*, not posited: a derivation that writes down $t' = \gamma(t - vx)$ as an assumption has begged the question.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Strip the transformation down by applying the four demands in order — linearity from inertia, the moving-origin form $x' = \gamma(x - vt)$, evenness of $\gamma$ from isotropy, and finally the light condition to solve for $\gamma$ — then recover the clock equation by substituting the spatial relation into its inverse. Work in $1+1$ dimensions and append the trivial transverse equations $y' = y$, $z' = z$ at the very end.

**Subgoal decomposition:**

1. **Linearity.** Show the transformation is linear: $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$.
   - *Hint:* Inertial frames carry the law of inertia, so straight worldlines map to straight worldlines; a line-preserving map fixing the origin is linear.
   - *Why needed:* It reduces the unknown from arbitrary functions to four numbers.

2. **Spatial form from the moving origin.** Reduce the spatial equation to $x' = \gamma(x - vt)$.
   - *Hint:* The $S'$ origin $x' = 0$ is the worldline $x = vt$; the spatial equation must vanish exactly there, so $x' \propto (x - vt)$.
   - *Why needed:* It spends two coefficients and isolates the single scale $\gamma$.

3. **Evenness of $\gamma$.** Show $\gamma_v = \gamma_{-v}$.
   - *Hint:* Either $\gamma$ depends only on $v^2$ (isotropy), or run the derivation in mirror-reflected frames $\tilde x = -x$, $\tilde x' = -x'$ where the relative velocity is $-v$ and compare.
   - *Why needed:* It guarantees the forward and inverse transformations share one $\gamma$, the quantitative form of the relativity principle.

4. **Solve for $\gamma$ with the light condition.** Impose $x = t \Rightarrow x' = t'$ to get $\gamma = (1 - v^2)^{-1/2}$.
   - *Hint:* Substitute the light ray into $x' = \gamma(x - vt)$ and into the inverse $x = \gamma(x' + vt')$; this gives $t' = \gamma(1-v)t$ and $t = \gamma(1+v)t'$; multiply.
   - *Why needed:* The constancy of light is the one numerical input; it fixes the value of $\gamma$.

5. **Recover the clock equation.** Derive $t' = \gamma(t - vx)$.
   - *Hint:* Substitute $x' = \gamma(x - vt)$ into the inverse $x = \gamma(x' + vt')$ and solve the resulting equation for $t'$, using $\gamma^2(1 - v^2) = 1$.
   - *Why needed:* It completes the transformation and exhibits the position-dependent term that abolishes absolute time.

---

# Lemma Decomposition

> [!note]- Lemma 1: The transformation is linear
> **Statement:** A coordinate change between two inertial frames, fixing the common origin, has the form $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$ with constant coefficients $\alpha_i = \alpha_i(v)$.
>
> **Hint:** Free particles trace straight lines in both frames; a map carrying every straight line to a straight line and fixing the origin is linear.
>
> **Why needed:** It is the foundation — it turns the search for arbitrary functions $f, g$ into a search for four numbers, making the remaining demands tractable.
>
> > [!note]- Full proof
> > By the law of inertia (built into [[Def - Inertial Frame and the Postulates of Special Relativity|"inertial frame"]]), a free particle has constant velocity in $S$, so its worldline is a straight line in the $(t,x)$ plane; since $S'$ is also inertial, the image worldline is straight in $(t', x')$. Thus the map $(t,x) \mapsto (t',x')$ carries straight lines to straight lines. A bijection of $\mathbb{R}^2$ (more generally $\mathbb{R}^n$, $n \ge 2$) that maps every straight line to a straight line is an affine map (the fundamental theorem of affine geometry); fixing the origin (the frames coincide at $t = t' = 0$) removes the translation, leaving a linear map. Hence $x' = \alpha_1 x + \alpha_2 t$ and $t' = \alpha_3 x + \alpha_4 t$, with the $\alpha_i$ depending only on the relative velocity $v$. $\blacksquare$

> [!note]- Lemma 2: The spatial equation is $x' = \gamma(x - vt)$
> **Statement:** Hypothesis (ii) reduces the spatial equation to $x' = \gamma(x - vt)$ for a single coefficient $\gamma = \gamma_v$.
>
> **Hint:** The spatial origin of $S'$ is $x' = 0$; in $S$ it is the worldline $x = vt$. The linear function $x'$ must vanish exactly on this line.
>
> **Why needed:** It collapses the two spatial coefficients into one unknown scale $\gamma$, the only quantity the light condition will need to determine.
>
> > [!note]- Full proof
> > From Lemma 1, $x' = \alpha_1 x + \alpha_2 t$. The spatial origin of $S'$ is the set $x' = 0$; by hypothesis (ii) this is the worldline $x = vt$ in $S$. So $x' = 0$ whenever $x = vt$, i.e. the linear form $\alpha_1 x + \alpha_2 t$ vanishes on the line $x - vt = 0$. A linear function of $(x,t)$ vanishing on the line $x - vt = 0$ is a multiple of $(x - vt)$: $\alpha_1 x + \alpha_2 t = \gamma\,(x - vt)$ for some constant $\gamma = \alpha_1$ (matching coefficients: $\alpha_2 = -\gamma v$). Hence $x' = \gamma(x - vt)$, with $\gamma = \gamma_v$ a single function of the relative velocity. $\blacksquare$

> [!note]- Lemma 3: $\gamma$ is an even function of $v$
> **Statement:** $\gamma_v = \gamma_{-v}$.
>
> **Hint:** Either invoke isotropy ($\gamma$ depends only on $v^2 = \mathbf{v}\cdot\mathbf{v}$), or repeat Lemma 2's argument in spatially reflected frames where the relative velocity is $-v$ and compare the two expressions.
>
> **Why needed:** It forces the forward map and its inverse to carry the *same* $\gamma$; without it the two frames would not be on equal footing, violating the principle of relativity.
>
> > [!note]- Full proof
> > *Isotropy argument.* By hypothesis (iii) space has no preferred direction, so the scalar $\gamma$ can depend on the velocity only through its magnitude, $\gamma = \gamma(v^2)$. Since $(-v)^2 = v^2$, $\gamma_{-v} = \gamma_v$.
> >
> > *Reciprocity argument (independent).* Introduce frames $\tilde S, \tilde S'$ identical to $S, S'$ but measuring the $x$-coordinate in the opposite direction: $\tilde x = -x$, $\tilde x' = -x'$. Then $\tilde S$ moves at velocity $-v$ relative to $\tilde S'$ (same physical motion, opposite axis convention). Applying Lemma 2 to this pair gives $\tilde x' = \gamma_{-v}(\tilde x + v\tilde t)$. Substituting $\tilde x = -x$, $\tilde x' = -x'$, $\tilde t = t$ yields $-x' = \gamma_{-v}(-x + vt)$, i.e. $x' = \gamma_{-v}(x - vt)$. Comparing with $x' = \gamma_v(x - vt)$ from Lemma 2 forces $\gamma_v = \gamma_{-v}$. (The alternative sign choice $\kappa = -1$ in matching the reflected transformation corresponds to an additional spatial reflection, not the identity at $v = 0$, and is discarded — see [[Ex - Reciprocity and the evenness of the Lorentz factor]].) $\blacksquare$

> [!note]- Lemma 4: The light condition forces $\gamma = (1 - v^2)^{-1/2}$
> **Statement:** Imposing that a light ray $x = t$ in $S$ is a light ray $x' = t'$ in $S'$ yields $\gamma^2(1 - v^2) = 1$, hence $\gamma = (1 - v^2)^{-1/2}$ (positive root).
>
> **Hint:** Use both the forward spatial equation and the inverse (with the same $\gamma$, by Lemma 3); the two light conditions multiply to cancel the times.
>
> **Why needed:** This is the only step that uses the second postulate; it supplies the single number that determines the transformation.
>
> > [!note]- Full proof
> > By Lemma 2 and Lemma 3, $x' = \gamma(x - vt)$ and, viewing $S$ from $S'$ (which sees $S$ move at $-v$, same $\gamma$ by Lemma 3), $x = \gamma(x' + vt')$. A light ray in $S$ has $x = t$ (speed $c = 1$); substituting into the forward equation,
> > $$x' = \gamma(t - vt) = \gamma(1 - v)\,t.$$
> > By the second postulate the same ray has $x' = t'$ in $S'$, so $t' = \gamma(1 - v)t$. The same ray viewed through the inverse, with $x' = t'$, gives $x = \gamma(x' + vt') = \gamma(1 + v)t'$, and since $x = t$, $t = \gamma(1 + v)t'$. Multiply the two scalar relations:
> > $$t' \cdot t = \gamma^2(1 - v)(1 + v)\,t\,t' = \gamma^2(1 - v^2)\,t\,t'.$$
> > Cancelling $t\,t' \ne 0$ gives $1 = \gamma^2(1 - v^2)$, so $\gamma = (1 - v^2)^{-1/2}$. The positive root is taken because $\gamma \to +1$ as $v \to 0$ (the transformation must reduce to the identity). With $c$ restored, $\gamma = (1 - v^2/c^2)^{-1/2}$; note $\gamma$ is real only for $|v| < c$. $\blacksquare$

> [!note]- Lemma 5: The time transformation is forced to be $t' = \gamma(t - vx)$
> **Statement:** Given $x' = \gamma(x - vt)$ and the inverse $x = \gamma(x' + vt')$ with $\gamma = (1-v^2)^{-1/2}$, the time equation is necessarily $t' = \gamma(t - vx)$.
>
> **Hint:** Substitute the forward spatial equation into the inverse and solve for $t'$; use $\gamma^2(1 - v^2) = 1$.
>
> **Why needed:** It is the climax — the clock equation, not assumed but derived, with the position-dependent term $-\gamma v x$ that destroys absolute time.
>
> > [!note]- Full proof
> > The inverse spatial relation is $x = \gamma(x' + vt')$. Substitute the forward equation $x' = \gamma(x - vt)$:
> > $$x = \gamma\big(\gamma(x - vt) + vt'\big) = \gamma^2(x - vt) + \gamma v t'.$$
> > Solve for $\gamma v t'$:
> > $$\gamma v t' = x - \gamma^2 x + \gamma^2 v t = x(1 - \gamma^2) + \gamma^2 v t.$$
> > Now $1 - \gamma^2 = 1 - \frac{1}{1 - v^2} = \frac{(1 - v^2) - 1}{1 - v^2} = \frac{-v^2}{1 - v^2} = -\gamma^2 v^2$. Hence
> > $$\gamma v t' = -\gamma^2 v^2 x + \gamma^2 v t = \gamma^2 v(t - vx).$$
> > Divide by $\gamma v$ (with $v \ne 0$; the case $v = 0$ is the identity):
> > $$t' = \gamma(t - vx).$$
> > With $c$ restored this is $t' = \gamma(t - vx/c^2)$. Appending the unaffected transverse equations $y' = y$, $z' = z$ (Lemma 6 below) completes the transformation. $\blacksquare$

> [!note]- Lemma 6: The transverse coordinates are unchanged
> **Statement:** Under a boost along $x$, $y' = y$ and $z' = z$.
>
> **Hint:** The most general linear transverse relation is $y' = \kappa y$; symmetry between the frames forces $\kappa = 1$.
>
> **Why needed:** It promotes the $1+1$ result to the full $3+1$ transformation, confirming that only the direction of motion is affected.
>
> > [!note]- Full proof
> > By linearity (Lemma 1, extended to $3+1$) and the coincidence of origins, the transverse equation can only be $y' = \kappa y$ for some constant $\kappa = \kappa(v)$ (there is no $x$ or $t$ dependence: a transverse displacement perpendicular to the motion cannot, by isotropy about the $x$-axis, pick up longitudinal or temporal components). By the symmetry of the two frames, the inverse must read $y = \kappa y'$, so $\kappa^2 = 1$, giving $\kappa = \pm 1$. The value $\kappa = -1$ is a reflection, not the identity at $v = 0$, and is discarded; hence $\kappa = 1$ and $y' = y$. Identically $z' = z$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** Both frames are inertial and share an origin at $t = t' = 0$; the relative velocity $v$ satisfies $|v| < c = 1$ (otherwise no inertial frame relates them, as $\gamma$ would be imaginary). We work in the $(t,x)$ plane and append transverse coordinates at the end.
>
> **Linearity (Lemma 1).** The law of inertia in both frames forces the map $(t,x) \mapsto (t',x')$ to carry straight worldlines to straight worldlines; fixing the origin, it is linear: $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$.
>
> **Spatial form (Lemma 2).** The $S'$ origin $x' = 0$ is the worldline $x = vt$, so $x'$ vanishes on $x - vt = 0$; thus $x' = \gamma(x - vt)$ with a single scale $\gamma = \gamma_v$.
>
> **Evenness (Lemma 3).** Isotropy makes $\gamma$ depend only on $v^2$, so $\gamma_v = \gamma_{-v}$; equivalently the reflected-frame argument yields the same. Consequently the inverse transformation is $x = \gamma(x' + vt')$ with the *same* $\gamma$.
>
> **Determination of $\gamma$ (Lemma 4).** A light ray $x = t$ must satisfy $x' = t'$. Substituting into $x' = \gamma(x - vt)$ gives $t' = \gamma(1 - v)t$; substituting into the inverse with $x' = t'$ gives $t = \gamma(1 + v)t'$. Multiplying, $1 = \gamma^2(1 - v^2)$, so
> $$\gamma = \frac{1}{\sqrt{1 - v^2}} \qquad\left(= \frac{1}{\sqrt{1 - v^2/c^2}}\ \text{with }c\right).$$
>
> **Clock equation (Lemma 5).** Substituting $x' = \gamma(x - vt)$ into the inverse $x = \gamma(x' + vt')$ and solving for $t'$, using $1 - \gamma^2 = -\gamma^2 v^2$, gives
> $$t' = \gamma(t - vx).$$
>
> **Transverse coordinates (Lemma 6).** Isotropy about the $x$-axis and symmetry of the frames force $y' = y$, $z' = z$.
>
> **Assembly.** Collecting,
> $$x' = \gamma(x - vt), \quad t' = \gamma(t - vx), \quad y' = y, \quad z' = z, \quad \gamma = (1 - v^2)^{-1/2},$$
> which is the Lorentz boost. Each step was forced, so the transformation is unique. **Corollary (Galilean limit):** replacing hypothesis (iv) by $t' = t$ forces, in Lemma 5's relation $t' = \gamma(t - vx)$ specialised by $t' = t$ for all $x$, both $\gamma = 1$ and the vanishing of the $vx$ term — returning $x' = x - vt$, $t' = t$. Equivalently $\gamma \to 1$ as $c \to \infty$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Group contraction in Lie theory.** The statement that the Galilean transformation is the $\gamma \to 1$ (equivalently $c \to \infty$) limit of the Lorentz boost is an instance of **İnönü–Wigner contraction** of a Lie group: the [[Def - The Poincaré Group|Poincaré group]] contracts to the Galilean group as $c \to \infty$. A worthwhile exercise is to carry out the contraction at the level of the boost *generators* and watch the time-mixing term, suppressed by $1/c^2$, vanish — recovering the rigid time-slice shear. The application is nonobvious because it reframes a physics limit as an algebraic degeneration of a group.

**The most general transformation compatible with relativity alone.** Drop the second postulate and keep only (i)–(iii): the derivation leaves $\gamma_v$ undetermined, and demanding *consistency under composition* (two boosts compose to a boost) forces $\gamma_v = (1 - v^2/w^2)^{-1/2}$ for some universal constant $w$ (the invariant speed), with $w = \infty$ the Galilean case and $w = c$ the relativistic one. An exercise is to reconstruct this one-parameter family and show that the existence of *any* finite invariant speed already implies the full structure — special relativity is forced by relativity plus the bare existence of a speed limit, with experiment only fixing its value. This is the content of the symmetry-first derivations in the literature.

**Hyperbolic geometry and the Doppler factor.** The factors $(1 - v)$ and $(1 + v)$ whose geometric mean is $\gamma^{-1}$ are the relativistic Doppler factors, and their square root is the [[Ex - The k-calculus (Bondi) derivation|Bondi k-factor]] $k = \sqrt{(1+v)/(1-v)}$. An exercise is to redo the entire determination of $\gamma$ in terms of $k$ (so $\gamma = \tfrac12(k + k^{-1})$, $v = (k^2-1)/(k^2+1)$) and recognise $k = e^{\varphi}$ with $\varphi$ the [[Def - Rapidity|rapidity]] — connecting the postulate derivation to the eigenvalue structure of the boost matrix. The application is surprising because it identifies $\gamma$'s origin as a geometric mean of eigenvalues of the Lorentz map.

---

# Bridges

- **[[Def - The Lorentz Transformation]]** — this theorem *is* the justification of that definition: the boost formula written down there is shown here to be the unique consequence of the postulates. The definition page records the formula and its structure; this page records why no other formula is possible. Together they are the statement and proof of "the Lorentz transformation exists and is unique."

- **[[Thm - Invariance of the Spacetime Interval]]** — the same value $\gamma = (1-v^2)^{-1/2}$ derived here is exactly the value that makes the interval $\Delta t^2 - \Delta x^2$ invariant; substituting this theorem's output into the interval and watching the cross terms cancel is the proof of interval invariance. This theorem derives the boost *from the postulates*; the interval theorem then *characterises* the boost as the interval-preserving map, the bridge to the group-theoretic viewpoint of [[Def - The Lorentz Group|the Lorentz group]].

- **[[Def - Galilean Spacetime and Its Failure]]** — the corollary makes the relationship precise: the Galilean transformation is the degenerate $\gamma = 1$ member of the family this theorem parametrises, recovered by sending $c \to \infty$ or by imposing absolute time. The theorem thus contains both the new law and the old one as its limit, exhibiting Newtonian mechanics as the low-speed approximation rather than a rival.

- **Euclidean rotations from preserving distance** — the structure of this derivation is the indefinite-signature twin of deriving a rotation matrix from "preserves $x^2 + y^2$ and fixes the origin." There, demanding linearity plus preservation of the Euclidean form yields $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$; here, linearity plus the constancy of light yields the boost with $\cosh, \sinh$ in place of $\cos, \sin$. The single sign difference in the invariant form is the whole of relativity.

---

# Unlocked by This

> [!tip] The Lorentz Group as a One-Parameter Family of Boosts *(from SR IV / SR IX)*
> Demanding that this theorem's output be closed under composition forces the boosts along an axis to form a one-parameter group, and parametrising by [[Def - Rapidity|rapidity]] $\varphi$ (with $v = \tanh\varphi$, $\gamma = \cosh\varphi$) makes composition into addition. The full collection of boosts and rotations is the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$, whose structure and Lie algebra organise all of relativistic physics.

> [!tip] Wigner's Classification *(from QFT)*
> Because the postulates single out the [[Def - The Poincaré Group|Poincaré group]] as the symmetry of spacetime, the elementary particles are classified by its irreducible unitary representations — **Wigner's theorem** — labelled by two Casimir invariants, **mass** and **spin**. The uniqueness derived here is the first link in that chain: it is what guarantees there is one definite symmetry group to represent.
