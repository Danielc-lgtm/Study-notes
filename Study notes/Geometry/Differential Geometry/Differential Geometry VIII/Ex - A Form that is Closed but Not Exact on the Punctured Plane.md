---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Closed and Exact Forms"
  - "Def - Exterior Derivative on a Manifold"
  - "Thm - d-Squared-is-Zero"
  - "Thm - The General Stokes Theorem"
tags: [geometry, differential-geometry, cohomology]
---

# Problem Statement

Consider the $1$-form on the **punctured plane** $M = \mathbb{R}^2 \setminus \{0\}$:
$$\omega = \frac{-y\,dx + x\,dy}{x^2 + y^2}.$$

(a) Verify that $\omega$ is smooth on $M$ (i.e., the denominator does not vanish where the form is defined).

(b) Compute $d\omega$ and show that $\omega$ is **closed**: $d\omega = 0$ on $M$.

(c) Compute $\int_{S^1}\omega$ where $S^1$ is the unit circle parametrized counterclockwise.

(d) Conclude that $\omega$ is **not exact** on $M$. State and justify the relationship to $H^1_{dR}(M) \cong \mathbb{R}$.

(e) Explain why this $\omega$ is locally exact (find a local primitive $\theta$ — the angle function — on any simply connected open subset of $M$).

(f) State the cohomological interpretation: the period $\int_{S^1}\omega = 2\pi$ is the value of the integration pairing $\int : H^1_{dR}(M) \times H_1(M) \to \mathbb{R}$ on the generator $[\omega]$ and the generator $[S^1]$.

**Recall:**

A form $\omega \in \Omega^k(M)$ is **closed** if $d\omega = 0$; **exact** if $\omega = d\eta$ for some $\eta \in \Omega^{k-1}(M)$.

[[Thm - The General Stokes Theorem]]: $\int_M d\eta = \int_{\partial M}\eta$ for an oriented compact manifold $M$ with boundary $\partial M$ and a smooth $(k-1)$-form $\eta$ of compact support. Corollary: $\int_C d\eta = 0$ for any closed loop $C$ (boundary of nothing locally).

$H^1_{dR}(M) = \{\text{closed }1\text{-forms}\}/\{\text{exact }1\text{-forms}\}$ — the first de Rham cohomology group of $M$.

---

# Convergent Strategy

**Problem class:** This is the prototypical "closed-but-not-exact" exercise. The route is: (a) verify well-definedness, (b) compute $d\omega = 0$ directly, (c) compute the period $\int_{S^1}\omega = 2\pi$, (d) deduce non-exactness from Stokes' theorem (an exact form integrates to zero around any closed loop).

**Assumption pattern:** The given form $\omega$ is the standard "angular form" — it is the differential of the angle coordinate $\theta$ on any region where $\theta$ is single-valued, but globally on $\mathbb{R}^2 \setminus \{0\}$ the angle is multi-valued. The structure that makes this work is the topology of the punctured plane: it has one hole, encoded by the single nonzero class in $H^1_{dR}(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{R}$.

**Theorem routing:** Step (b) uses the [[Thm - Coordinate Expression for the Exterior Derivative|chart formula for d]]. Step (c) is direct integration. Step (d) uses [[Thm - The General Stokes Theorem]] in the contrapositive: an exact form would have zero period around any loop, so a nonzero period implies non-exactness.

**Key decision point:** The non-obvious step is recognizing that *local exactness* (the form is locally $d\theta$) does *not* imply global exactness, because the local primitives do not patch into a global one — the angle function on $\mathbb{R}^2 \setminus \{0\}$ jumps by $2\pi$ when traversed around the origin. This is the prototype of "closed but not exact", and it is the analytic shadow of the punctured plane having one hole.

---

# Legal Operations Used

1. **Expand a form in coordinates and apply $d$ mechanically** (operation 1) — for computing $d\omega$ in part (b).

2. **Test exactness in two steps: closedness first, periods second** (operation 6) — the structural routine for "is this form exact?"

3. **Use $d^2 = 0$ as a one-line shortcut** (operation 4) — combined with Stokes, gives the non-exactness criterion.

---

# Hints

> [!note]- Hint 1
> For (b), expand $d\omega = d\left(\frac{-y}{x^2+y^2}\right) \wedge dx + d\left(\frac{x}{x^2+y^2}\right) \wedge dy$. Compute the partial derivatives and combine.

> [!note]- Hint 2
> For (c), parametrize $S^1$ as $\gamma(t) = (\cos t, \sin t)$ for $t \in [0, 2\pi]$. Compute $\gamma^*\omega$ as a $1$-form on $[0, 2\pi]$ and integrate.

> [!note]- Hint 3
> For (d): if $\omega = d\eta$ globally on $M$, then by Stokes $\int_{S^1}\omega = \int_{\partial D^2}d\eta$, where $D^2$ would be a disk bounded by $S^1$. But the disk $D^2 = \{(x, y) : x^2 + y^2 \leq 1\}$ is not contained in $M$ — it contains the origin where $\omega$ is undefined.

> [!note]- Hint 4
> For (e): on a simply connected open set $U \subseteq M$ (e.g., the slit plane $\mathbb{R}^2 \setminus \{\text{negative }x\text{-axis}\}$), define the angle function $\theta(x, y) \in (-\pi, \pi)$ unambiguously. Verify $d\theta = \omega$ on $U$.

> [!note]- Hint 5
> For (f), the period $\int_{S^1}\omega = 2\pi$ is exactly the value of the pairing $\int : H^1_{dR}(M) \times H_1(M; \mathbb{R}) \to \mathbb{R}$ on the de Rham class $[\omega]$ and the homology class $[S^1]$. Since the pairing is non-degenerate (by de Rham's theorem), $[\omega] \neq 0$.

---

# Solution

The proof has five steps. Step 1 verifies $\omega$ is smooth on $M$. Step 2 computes $d\omega = 0$ by mechanical application of the chart formula. Step 3 computes $\int_{S^1}\omega = 2\pi$ by direct integration. Step 4 derives non-exactness from Stokes' theorem applied (in the contrapositive). Step 5 explains local exactness and the cohomological meaning.

**Step 1: $\omega$ is smooth on $M$.**

The denominator $x^2 + y^2$ vanishes only at the origin $(0, 0)$, which is removed in $M = \mathbb{R}^2 \setminus \{0\}$. On $M$, both $-y/(x^2+y^2)$ and $x/(x^2+y^2)$ are smooth (rational functions with nonvanishing denominator), so $\omega$ is a smooth $1$-form.

> [!note]- Derivation
> The denominator $x^2 + y^2$ is zero only at $(0, 0)$, which is excluded from $M$. On $M$, both coefficient functions are well-defined smooth functions, so $\omega$ is smooth.

**Step 2: $d\omega = 0$ on $M$.**

By the chart formula, $d\omega = d\left(\frac{-y}{x^2+y^2}\right) \wedge dx + d\left(\frac{x}{x^2+y^2}\right) \wedge dy$. Compute the two differentials:
$$d\left(\frac{-y}{x^2+y^2}\right) = \frac{2xy}{(x^2+y^2)^2}\,dx + \frac{-(x^2+y^2) + 2y^2}{(x^2+y^2)^2}\,dy = \frac{2xy}{(x^2+y^2)^2}\,dx + \frac{y^2 - x^2}{(x^2+y^2)^2}\,dy.$$
$$d\left(\frac{x}{x^2+y^2}\right) = \frac{(x^2+y^2) - 2x^2}{(x^2+y^2)^2}\,dx + \frac{-2xy}{(x^2+y^2)^2}\,dy = \frac{y^2 - x^2}{(x^2+y^2)^2}\,dx + \frac{-2xy}{(x^2+y^2)^2}\,dy.$$

Wedging:
$$d\left(\frac{-y}{x^2+y^2}\right) \wedge dx = \frac{y^2 - x^2}{(x^2+y^2)^2}\,dy \wedge dx = -\frac{y^2-x^2}{(x^2+y^2)^2}\,dx \wedge dy$$
(the $\partial_x$ term wedged with $dx$ gives zero).

$$d\left(\frac{x}{x^2+y^2}\right) \wedge dy = \frac{y^2 - x^2}{(x^2+y^2)^2}\,dx \wedge dy$$
(the $\partial_y$ term wedged with $dy$ gives zero).

Summing: $d\omega = -\frac{y^2 - x^2}{(x^2+y^2)^2}\,dx \wedge dy + \frac{y^2 - x^2}{(x^2+y^2)^2}\,dx \wedge dy = 0$.

So $\omega$ is closed on $M$.

> [!note]- Derivation
> Compute the partials of the two coefficient functions $f = -y/(x^2+y^2)$ and $g = x/(x^2+y^2)$.
>
> $\partial_x f = \partial_x[-y(x^2+y^2)^{-1}] = -y \cdot (-1)(x^2+y^2)^{-2} \cdot 2x = \frac{2xy}{(x^2+y^2)^2}$.
>
> $\partial_y f = \partial_y[-y(x^2+y^2)^{-1}] = -(x^2+y^2)^{-1} + (-y)(-1)(x^2+y^2)^{-2}(2y) = \frac{-(x^2+y^2) + 2y^2}{(x^2+y^2)^2} = \frac{y^2 - x^2}{(x^2+y^2)^2}$.
>
> $\partial_x g = \partial_x[x(x^2+y^2)^{-1}] = (x^2+y^2)^{-1} + x \cdot (-1)(x^2+y^2)^{-2}(2x) = \frac{(x^2+y^2) - 2x^2}{(x^2+y^2)^2} = \frac{y^2 - x^2}{(x^2+y^2)^2}$.
>
> $\partial_y g = \partial_y[x(x^2+y^2)^{-1}] = x \cdot (-1)(x^2+y^2)^{-2}(2y) = \frac{-2xy}{(x^2+y^2)^2}$.
>
> By the closedness condition for a $1$-form on $\mathbb{R}^2$ (from [[Ex - Computing the Exterior Derivative in Coordinates]] part (d)): $\omega = f\,dx + g\,dy$ is closed iff $\partial_y f = \partial_x g$. Check: $\partial_y f = (y^2 - x^2)/(x^2+y^2)^2 = \partial_x g$. So $\omega$ is closed.

**Step 3: $\int_{S^1}\omega = 2\pi$.**

Parametrize $S^1$ by $\gamma(t) = (\cos t, \sin t)$ for $t \in [0, 2\pi]$. Compute the pullback:
$\gamma^*\omega = \frac{-\sin t \cdot d(\cos t) + \cos t \cdot d(\sin t)}{\cos^2 t + \sin^2 t} = -\sin t \cdot (-\sin t)\,dt + \cos t \cdot (\cos t)\,dt = (\sin^2 t + \cos^2 t)\,dt = dt$.

So $\int_{S^1}\omega = \int_0^{2\pi} dt = 2\pi$.

> [!note]- Derivation
> $\gamma(t) = (\cos t, \sin t)$, so $\gamma^*x = \cos t$, $\gamma^*y = \sin t$, $\gamma^*(dx) = d(\cos t) = -\sin t\,dt$, $\gamma^*(dy) = d(\sin t) = \cos t\,dt$.
>
> $\gamma^*\omega = \frac{1}{\cos^2 t + \sin^2 t}(\gamma^*(-y\,dx) + \gamma^*(x\,dy)) = \frac{1}{1}(-\sin t \cdot (-\sin t)\,dt + \cos t \cdot \cos t\,dt) = (\sin^2 t + \cos^2 t)\,dt = dt$.
>
> Integrate: $\int_{S^1}\omega = \int_0^{2\pi} dt = 2\pi$.

**Step 4: $\omega$ is not exact.**

Suppose for contradiction that $\omega = d\eta$ for some smooth $0$-form (function) $\eta$ on $M$. Then by Stokes' theorem applied to the closed loop $S^1$ (which is the boundary of nothing in $M$, since the disk it would bound contains the origin which is not in $M$), but more directly: an exact form $d\eta$ integrated over a closed loop equals $\eta$ evaluated at the boundary points, which is zero (since the loop is closed). So $\int_{S^1}\omega = \int_{S^1}d\eta = 0$. But Step 3 gives $2\pi$, contradiction.

So $\omega$ is closed but not exact.

> [!note]- Derivation
> If $\omega = d\eta$ for $\eta \in C^\infty(M)$, then parametrize $S^1$ as $\gamma(t) = (\cos t, \sin t)$ and integrate:
> $$\int_{S^1}\omega = \int_0^{2\pi}\gamma^*(d\eta) = \int_0^{2\pi} d(\eta \circ \gamma) = \int_0^{2\pi}\frac{d(\eta(\gamma(t)))}{dt}\,dt = \eta(\gamma(2\pi)) - \eta(\gamma(0)) = \eta(1, 0) - \eta(1, 0) = 0.$$
> The third equality uses that pullback commutes with $d$. The final value is zero because $\gamma(0) = \gamma(2\pi) = (1, 0)$ — the loop is closed.
>
> But Step 3 gave $\int_{S^1}\omega = 2\pi \neq 0$. Contradiction. So $\omega$ is not exact.

**Step 5: Local exactness and cohomological meaning.**

On a simply connected open subset $U \subset M$ — e.g., the slit plane $U = \mathbb{R}^2 \setminus \{(x, 0) : x \leq 0\}$ — the angle function $\theta : U \to (-\pi, \pi)$ defined by $\theta(x, y) = \operatorname{atan2}(y, x)$ is smooth and single-valued. Computing $d\theta$ on $U$:
$$d\theta = \frac{\partial \theta}{\partial x}\,dx + \frac{\partial \theta}{\partial y}\,dy = \frac{-y}{x^2+y^2}\,dx + \frac{x}{x^2+y^2}\,dy = \omega|_U.$$

So $\omega$ is locally exact: on every simply connected open set, $\omega = d\theta$ for an explicit local primitive $\theta$.

But $\theta$ does not extend to a single-valued smooth function on all of $M$, because traversing $S^1$ once changes $\theta$ by $2\pi$ (a continuous angle function on $\mathbb{R}^2 \setminus \{0\}$ would be multi-valued). The non-exactness of $\omega$ globally is precisely the failure of these local primitives to patch.

**Cohomologically:** $H^1_{dR}(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{R}$, with the isomorphism given by the period map $[\omega] \mapsto \int_{S^1}\omega$. The class $[\omega] \in H^1_{dR}$ corresponds to $2\pi$, the value of the period; since $2\pi \neq 0$, $[\omega] \neq 0$ in cohomology, confirming non-exactness.

By **de Rham's theorem**, $H^1_{dR}(\mathbb{R}^2 \setminus \{0\}) \cong H^1(\mathbb{R}^2 \setminus \{0\}; \mathbb{R}) \cong \mathbb{R}$, with the generator corresponding to the one $1$-dimensional "hole" at the origin. The form $\omega$ is the prototypical representative of this nonzero class.

> [!note]- Derivation
> $\theta(x, y) = \arctan(y/x)$ on $U = \mathbb{R}^2 \setminus \{(x, 0) : x \leq 0\}$ (the slit plane), with the branch convention that $\theta \in (-\pi, \pi)$. (Or use the standard $\operatorname{atan2}$ function.) Compute the partials:
> $\partial_x \theta = \frac{-y/x^2}{1 + (y/x)^2} = \frac{-y}{x^2 + y^2}$.
> $\partial_y \theta = \frac{1/x}{1 + (y/x)^2} = \frac{x}{x^2 + y^2}$.
> So $d\theta = (\partial_x\theta)\,dx + (\partial_y\theta)\,dy = \frac{-y\,dx + x\,dy}{x^2+y^2} = \omega|_U$. The form $\omega$ is the differential of the angle function on any simply connected subdomain.

> [!note]- Complete formal solution
> **(a) Smoothness:** The denominator $x^2 + y^2$ is nonzero on $M = \mathbb{R}^2 \setminus \{0\}$, so $\omega$ is smooth on $M$.
>
> **(b) Closedness:** Computing $\partial_y(-y/(x^2+y^2)) = (y^2 - x^2)/(x^2+y^2)^2$ and $\partial_x(x/(x^2+y^2)) = (y^2 - x^2)/(x^2+y^2)^2$. They are equal, so $d\omega = (\partial_x g - \partial_y f)\,dx \wedge dy = 0$. ✓
>
> **(c) Period:** $\gamma(t) = (\cos t, \sin t)$, $t \in [0, 2\pi]$. $\gamma^*\omega = dt$, so $\int_{S^1}\omega = 2\pi$.
>
> **(d) Non-exactness:** If $\omega = d\eta$ globally, then $\int_{S^1}\omega = \int_{S^1}d\eta = 0$ by the fundamental theorem of calculus along a closed loop. But $\int_{S^1}\omega = 2\pi \neq 0$, contradiction. So $\omega$ is closed but not exact, and $[\omega] \neq 0$ in $H^1_{dR}(M)$.
>
> **(e) Local exactness:** On any simply connected subdomain $U \subseteq M$, the angle function $\theta$ is single-valued and smooth, with $d\theta = \omega|_U$. Local primitives exist but do not patch into a global primitive.
>
> **(f) Cohomological meaning:** $H^1_{dR}(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{R}$, generated by $[\omega]$, with the period pairing $[\omega] \mapsto \int_{S^1}\omega = 2\pi$ providing the isomorphism. By de Rham's theorem, this matches the singular cohomology $H^1(\mathbb{R}^2 \setminus \{0\}; \mathbb{R}) \cong \mathbb{R}$, which counts the single hole.
>
> $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to apply Stokes' theorem to the unit disk $D^2 \subset \mathbb{R}^2$ (closed disk bounded by $S^1$) to conclude $\int_{S^1}\omega = \int_{D^2}d\omega = 0$ (since $d\omega = 0$). This **fails** because $D^2$ contains the origin, which is *not* in the domain $M$ of $\omega$; the form $\omega$ is not defined on the origin, let alone smooth, so Stokes' theorem does not apply. The whole point of the example is that the topological obstruction (the hole at the origin) blocks the Stokes-style argument that would otherwise force $\int_{S^1}\omega = 0$.

---

# Key Takeaways

**Closed-but-not-exact is the calculus of holes.** This exercise is the *prototype* of the closed-but-not-exact phenomenon, and the lesson is broad: a closed form $\omega$ on a manifold $M$ is exact if and only if all its periods $\int_\gamma\omega$ around closed loops $\gamma$ vanish. The map from closed forms to periods, modulo exact forms (which have zero periods), is the **period pairing** $H^k_{dR}(M) \times H_k(M; \mathbb{R}) \to \mathbb{R}$, and by de Rham's theorem this pairing is non-degenerate. So nonzero periods detect nonzero cohomology classes. The trigger pattern in problem-solving: "is this form exact?" → first compute $d\omega$ (if nonzero, no); if zero, compute periods (if any nonzero, no); if all zero, then $\omega$ is exact.

**Local exactness does not imply global exactness; the obstruction is topology.** The angular form $\omega = -y\,dx/(x^2+y^2) + x\,dy/(x^2+y^2)$ is *locally* exact (it equals $d\theta$ on every simply connected open subset of $M$), but *globally* not exact (no single-valued $\theta$ on all of $M$). The local primitives fail to patch because the angle changes by $2\pi$ when traversed around the origin. The global obstruction is precisely the topology of the punctured plane — its one hole — and the failure to patch is measured by the period $2\pi$. This is the structural pattern in every closed-not-exact example: local primitives exist by the Poincaré lemma; global primitives exist if and only if the local pieces patch, and the patching obstruction is a finite-dimensional invariant (a de Rham cohomology class).

**The Poincaré lemma applies locally but fails globally.** On any contractible open subset of $M$, the Poincaré lemma says every closed form is exact. So locally, the angular form has a primitive. The failure of global exactness happens precisely because $M$ is not contractible — it has the topology of a circle, with $\pi_1(M) \cong \mathbb{Z}$. The cohomology $H^1_{dR}(M) \cong \mathbb{R}$ records exactly one obstruction (the $\mathbb{Z}$-coefficient of $\pi_1$, made into a real number via the period map). For higher-genus surfaces or higher-dimensional manifolds with multiple holes, the same phenomenon scales up: each independent loop gives an independent period, and the dimension of $H^1_{dR}$ counts them.

**Stokes' theorem in the contrapositive is the non-exactness criterion.** If $\omega = d\eta$ globally on $M$, then $\int_\gamma\omega = 0$ for every closed loop $\gamma$ in $M$ (by Stokes applied to $\eta$ on a surface bounded by $\gamma$, or directly by the fundamental theorem of calculus on a parametrization of $\gamma$). The contrapositive — a nonzero period certifies non-exactness — is the standard tool for proving non-exactness. The crucial subtlety is that Stokes' theorem applies *only* when the relevant surface is contained in $M$. For the punctured plane, no disk in $M$ has $S^1$ as boundary (any such disk would contain the origin, which is not in $M$), so Stokes does not say $\int_{S^1}\omega = 0$ — and this failure of Stokes is what makes the nonzero period possible.

**This single example is the seed of de Rham cohomology, electromagnetism, and gauge theory.** The angular form on $\mathbb{R}^2 \setminus \{0\}$ is the simplest example of a nontrivial cohomology class. The generalization to higher dimensions and other topologies gives $H^k_{dR}(M)$ for any manifold. The same form, on $\mathbb{R}^2 \setminus \{0\}$ regarded as a slice of physical space, is the vector potential of a magnetic monopole (the magnetic charge encoded by the $2\pi$ period). The generalization to gauge theory gives **characteristic classes** of fibre bundles, with the period of a curvature form measuring "topological charges" of the gauge field. The single $1$-form on the punctured plane is the entry point to the whole theory of topological field invariants in physics.
