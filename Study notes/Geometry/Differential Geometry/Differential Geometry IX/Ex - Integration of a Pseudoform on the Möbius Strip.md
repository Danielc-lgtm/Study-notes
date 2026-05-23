---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Pseudoform (Twisted Form)"
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Volume Form"
  - "Def - Density on a Manifold"
  - "Ex - The Sphere is Orientable but the Möbius Strip is Not"
tags: [geometry, differential-geometry, integration, mobius]
---

# Problem Statement

Let $E$ be the Möbius strip, constructed as the quotient of the cylinder $\mathbb{R} \times (-1, 1)$ by the identification $(x, y) \sim (x + 1, -y)$. Equip $E$ with the induced flat Riemannian metric $ds^2 = dx^2 + dy^2$ (well-defined because the identification is an [[Def - Isometry|isometry]]).

**(a)** Show that the local expression $\omega = dx \wedge dy$ defines a globally well-defined pseudo-$2$-form on $E$, even though no global ordinary $2$-form can be nowhere-vanishing on $E$.

**(b)** Compute the integral $\int_E \omega$ and verify it equals the geometric area $2$ of the strip.

**(c)** Show by explicit calculation that any attempt to write $\omega$ as an ordinary $2$-form globally fails: in any candidate, the form must vanish somewhere.

**Recall:**

The objects in play are the Möbius strip as a non-orientable smooth manifold, the pseudo-$2$-form construction, and the integration of [[Def - Pseudoform (Twisted Form)|pseudoforms]].

![[Def - Pseudoform (Twisted Form)#The Definition]]

The Möbius strip can be defined either as the quotient $E = [\mathbb{R} \times (-1, 1)]/\sim$ with $(x, y) \sim (x + 1, -y)$, or equivalently as a rank-$1$ non-trivial real line bundle over $S^1$. The non-trivial bundle structure is what makes it non-orientable — the fiber's orientation reverses after one trip around the base. See [[Ex - The Sphere is Orientable but the Möbius Strip is Not]] for the proof of non-orientability via a global-section obstruction.

Recall that on an oriented chart $(U, \varphi)$, the integral of an ordinary $n$-form $\omega = f(x)\,dx^1 \wedge \cdots \wedge dx^n$ supported in $U$ is $\int_U f(\varphi(x))\,dx^1\cdots dx^n$ — a positively-signed Riemann integral. For [[Def - Pseudoform (Twisted Form)|pseudoforms]] the formula is *the same* in each chart, but the orientation-flip rule of the pseudoform guarantees that the integrals on overlapping charts agree without requiring positive Jacobian on transitions.

---

# Convergent Strategy

**Problem class.** This is a *check well-definedness of an integration construction on a non-orientable manifold* problem. The classical-form construction is unavailable, so the only legal route runs through pseudoforms or densities. The exercise drills the distinction between the two failure modes ("no global section" — which dooms ordinary forms) and the pseudoform fix (orientation-twist).

**Assumption pattern.** The hypothesis is geometric: the manifold is a specific concrete object (a quotient of a strip), it carries a flat Euclidean metric, and the metric is invariant under the identification map. The flatness ensures the area form in each chart is exactly $dx \wedge dy$; the invariance under the identification map is exactly what makes the pseudoform compatible with the transition function. These two facts together are what allow $dx \wedge dy$ to be lifted to a well-defined pseudoform.

**Theorem routing.** The route is: (i) Use the local trivialization of the bundle to write down the candidate pseudoform $dx \wedge dy$ in two charts covering $E$, (ii) check the transition relation: under the identifying chart the Jacobian is $-1$, so the ordinary $2$-form changes by a sign, but the chart's orientation also flips, so the *pseudoform* — which carries an extra orientation-sign factor — is invariant, (iii) integrate via Riemann integration in each chart and observe that the partition-of-unity sum gives a coherent total. The well-definedness check uses [[Def - Pseudoform (Twisted Form)|the orientation-flip rule of pseudoforms]] in its critical role.

**Key decision point.** The non-obvious step is realising that the failure of the Möbius strip's ordinary-form integration is *exactly* compensated by the failure of the orientation-respecting Jacobian: both fail with sign $-1$ across the identifying chart, and their ratio is $+1$. This cancellation of "sign change in the form" with "sign change in the chart orientation" is the whole content of the pseudoform construction. A reader who doesn't isolate the two sign sources will see only one and conclude (incorrectly) that the integral cannot be defined.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem#Legal Operations|the topic page's Legal Operations]]:

1. **Pull back to a chart and integrate** (operation 1). Applied in each of two overlapping charts on the Möbius strip. The strip's structure is a $1$-dimensional cylinder bundle over $S^1$, covered by two contractible charts, on each of which $dx \wedge dy$ pulls back to the standard Euclidean area form on a rectangle.

2. **Exhibit a nowhere-vanishing top-form to prove orientability** — *in its negation form* (operation 6, used in reverse). The whole point of (c) is to show that *no* candidate ordinary $2$-form is nowhere-vanishing; this is the standard mechanism by which one *disproves* orientability, and the failure of operation 6 is precisely why one needs pseudoforms.

3. **Reduce to half-space and FTC in the boundary direction** (operation 5) — implicitly. The integration over the strip with two boundary components $y = \pm 1$ involves the standard Fubini reduction in $y$, which is the FTC content of Stokes's theorem here, even though we are integrating a $2$-form on a $2$-manifold (no boundary integration is needed because the integrand is supported in the interior).

---

# Hints

> [!note]- Hint 1
> The Möbius strip is non-orientable, so no ordinary global $2$-form can be nowhere-vanishing. But pseudoforms have an *extra* sign factor that exactly compensates: when a transition map flips orientation, the pseudoform also flips, and the product is invariant. Cover the strip with two charts whose transition map you can write down explicitly, and check that the candidate local expression $dx \wedge dy$ satisfies the pseudoform compatibility condition.

> [!note]- Hint 2
> Cover the strip with two charts: $U_1 = (0, 0.6) \times (-1, 1)$ and $U_2 = (0.4, 1) \times (-1, 1) \cup (1, 1.1) \times (-1, 1)$ — the second chart wraps around the identification. The transition between $U_1$ and $U_2$ is the identity on the overlap $0.4 < x < 0.6$, but the transition on the *other* overlap $(0, 0.1) \subset U_1$ vs $(1, 1.1) \subset U_2$ uses the identification $(x, y) \mapsto (x - 1, -y)$, with Jacobian $-1$.

> [!note]- Hint 3
> For part (b), parametrize the strip in a single chart $[0, 1] \times (-1, 1)$ (using a partition of unity to handle the boundary identification cleanly) and integrate $dx \wedge dy$ in this chart. The answer is $1 \cdot 2 = 2$, which matches the geometric area.

> [!note]- Hint 4
> For part (c), use the orientability criterion ([[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]]) in its contrapositive form: $E$ is non-orientable, so any candidate ordinary $2$-form must vanish somewhere. The proof of non-orientability in [[Ex - The Sphere is Orientable but the Möbius Strip is Not]] gives an explicit obstruction — chase any candidate form once around the core circle and observe that it must agree with its own sign-reversal, forcing it to vanish.

---

# Solution

The strategy is to construct the pseudoform $\omega$ explicitly in two overlapping charts, verify the pseudoform compatibility condition on the orientation-reversing transition, compute the integral in a chart that covers all of $E$ minus a measure-zero seam, and verify the answer matches the geometric area. Part (c) then uses the non-orientability of $E$ to rule out any ordinary-form representation.

**Step 1: Choose charts and verify the pseudoform compatibility.**

Cover $E$ by two charts $\phi_1 : U_1 \to V_1 := (0, 0.6) \times (-1, 1) \subset \mathbb{R}^2$ and $\phi_2 : U_2 \to V_2 := (0.4, 1.1) \times (-1, 1) \subset \mathbb{R}^2$, where $\phi_1, \phi_2$ are the obvious inclusions modulo the quotient identification. The transition $\phi_2 \circ \phi_1^{-1}$ is the identity on the overlap $0.4 < x < 0.6$ (Jacobian $+1$) and on the overlap $(0, 0.1) \subset V_1$ vs $(1, 1.1) \subset V_2$ uses the identifying map $(x, y) \mapsto (x + 1, -y)$ with Jacobian $-1$.

In each chart, declare the local pseudo-$2$-form to be $\omega = dx \wedge dy$ in *that* chart's orientation. The compatibility under the orientation-reversing transition is automatic: on the orientation-reversing overlap, the ordinary $2$-form $dx \wedge dy$ in chart 1 pulls back to $-dx \wedge dy$ in chart 2 (because the Jacobian is $-1$), but the *orientation* of chart 2 on this overlap is the opposite of chart 1's, so the **pseudo**form's value is $(-1) \cdot (\text{chart-2 form-value}) = (-1)(-dx \wedge dy) = dx \wedge dy$ — agreeing with chart 1's value.

> [!note]- Derivation
> Write the transition explicitly. On the overlap $(0, 0.1) \subset V_1$, a point $(x, y) \in V_1$ corresponds to the equivalence class $(x, y) \sim (x + 1, -y) \in V_2$. So the transition map in coordinates is $\tau : V_1|_{(0,0.1)} \to V_2|_{(1,1.1)}$, $\tau(x, y) = (x + 1, -y)$. The Jacobian is
> $$D\tau = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad \det D\tau = -1.$$
>
> An *ordinary* $2$-form $\eta = f(x, y)\,dx \wedge dy$ in chart $2$ pulls back to chart $1$ via $\tau^*$:
> $$\tau^*\eta = f(\tau(x, y))\,\det(D\tau)\,dx \wedge dy = -f(x + 1, -y)\,dx \wedge dy.$$
>
> If we *want* the ordinary forms in the two charts to agree on the overlap — i.e., for $\eta$ to come from a globally well-defined ordinary $2$-form — we need $f(x + 1, -y) = -f(x, y)$. This sign-twist condition is the obstruction: any continuous $f$ satisfying it must vanish along the curve where the sign flips, which is everywhere along the strip's core. So no globally nowhere-vanishing ordinary $2$-form exists.
>
> For a *pseudo*form, the rule is different. By the orientation-flip rule, $\omega(p, -\mathfrak{o}_p) = -\omega(p, \mathfrak{o}_p)$, so $\omega$ flips sign when the chart's orientation flips. The transition map $\tau$ with $\det D\tau = -1$ reverses the chart's orientation. So the "pullback" rule for a pseudoform is
> $$\tau^*_{\mathrm{pseudo}}\omega = \mathrm{sgn}(\det D\tau)\cdot\tau^*_{\mathrm{form}}\omega = (-1)(-1)\,dx \wedge dy = dx \wedge dy.$$
>
> The two minus signs cancel, and the pseudoform $\omega = dx \wedge dy$ in chart $1$ is consistent with the pseudoform $\omega = dx \wedge dy$ in chart $2$ on the orientation-reversing overlap. (On the orientation-preserving overlap $0.4 < x < 0.6$ there is nothing to check; both signs are $+1$.) The pseudoform is globally well-defined.

**Step 2: Compute the integral.**

Parametrize $E$ by the half-open rectangle $[0, 1) \times (-1, 1)$ — a fundamental domain for the quotient. The pseudoform $\omega$ in this fundamental domain is just $dx \wedge dy$, integrated against the Euclidean area:
$$\int_E \omega = \int_0^1\int_{-1}^1 dy\,dx = 1 \cdot 2 = 2.$$
This is the geometric area of the strip.

> [!note]- Derivation
> A partition of unity $\{\psi_1, \psi_2\}$ subordinate to the two-chart cover lets us write $\int_E\omega = \int_E\psi_1\omega + \int_E\psi_2\omega$. Each summand is a Riemann integral in the corresponding chart. By the well-definedness check in Step 1, the sum is independent of the partition.
>
> Alternatively, since the identification identifies a measure-zero seam $\{x = 0\}$ with $\{x = 1\}$, the half-open fundamental domain $[0, 1) \times (-1, 1)$ covers the entire strip without overlap. So
> $$\int_E\omega = \int_{[0,1) \times (-1,1)} dx \wedge dy = \int_0^1\int_{-1}^1 dy\,dx.$$
> The inner integral is $\int_{-1}^1 dy = 2$ (the width of the strip), and the outer integral is $\int_0^1 dx = 1$ (the circumference of the core circle). The total is $2 \cdot 1 = 2$.
>
> This matches the geometric area: the Möbius strip, regarded as a rectangle of [[Def - Dimension|dimensions]] $1 \times 2$ before gluing, has area $1 \cdot 2 = 2$, and the gluing preserves area because the identification map is an [[Def - Isometry|isometry]].

**Step 3: Show no ordinary $2$-form representation exists.**

Suppose, for contradiction, that $\eta$ is a smooth nowhere-vanishing ordinary $2$-form on $E$. Then by [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]], $E$ would be orientable. But the Möbius strip is non-orientable (see [[Ex - The Sphere is Orientable but the Möbius Strip is Not]]). Contradiction.

A more concrete failure: any candidate ordinary form $\eta = f(x,y)\,dx \wedge dy$ in the fundamental domain must, by the well-definedness condition on the orientation-reversing overlap, satisfy $f(x+1, -y) = -f(x, y)$ for all $(x, y)$ in the overlap. Setting $x = 0.5$ and $y = 0$ gives $f(1.5, 0) = -f(0.5, 0)$; but the identification puts $(1.5, 0) \sim (0.5, 0)$ in $E$, so $f(1.5, 0) = f(0.5, 0)$. Together these force $f(0.5, 0) = 0$, and the same argument forces $f = 0$ along the entire core circle $\{y = 0\}$. So $\eta$ vanishes on a $1$-dimensional submanifold — it is not nowhere-vanishing.

> [!note]- Derivation
> The continuous-function obstruction is the concrete content of "no nowhere-vanishing global section." Any smooth $f$ on the strip that satisfies the sign-twist $f(x+1, -y) = -f(x, y)$ must vanish at every fixed point of the involution $(x, y) \mapsto (x + 1, -y)$ — fixed points being those satisfying both $x + 1 \equiv x \pmod 1$ (automatic) and $y = -y$ (so $y = 0$). The fixed-point set is the core circle $\{y = 0\}$. At every fixed point, the sign-twist forces $f = -f$, hence $f = 0$.
>
> So the core circle is a curve along which any candidate ordinary form vanishes. The candidate cannot represent the area — its integral on the strip would be the same as the integral on the strip minus the core circle, which is *two* disjoint pieces; but the form changes sign across the core, so the integrals over the two pieces cancel and the total is zero. The form represents nothing of geometric content.

> [!note]- Complete formal solution
> *Part (a).* Cover the Möbius strip $E$ by two charts $(\phi_1, V_1)$, $(\phi_2, V_2)$ with $V_1 = (0, 0.6) \times (-1, 1)$ and $V_2 = (0.4, 1.1) \times (-1, 1)$. The transition $\tau = \phi_2 \circ \phi_1^{-1}$ is the identity on the orientation-preserving overlap $V_1 \cap V_2 \cap \{0.4 < x < 0.6\}$ and is $(x, y) \mapsto (x + 1, -y)$ on the orientation-reversing overlap $V_1 \cap V_2 \cap \{0 < x < 0.1\}$, with Jacobian $\det D\tau = -1$.
>
> Declare the candidate pseudo-$2$-form to be $\omega = dx \wedge dy$ in each chart's orientation. On the orientation-preserving overlap, both charts give the same form, no check needed. On the orientation-reversing overlap, the pseudoform transformation rule is
> $$\tau^*_{\mathrm{pseudo}}\omega = \mathrm{sgn}(\det D\tau)\,\tau^*_{\mathrm{form}}\omega.$$
> The form pullback contributes $\tau^*_{\mathrm{form}}(dx \wedge dy) = \det(D\tau)\,dx \wedge dy = -dx \wedge dy$. The sign factor is $\mathrm{sgn}(-1) = -1$. Their product is $(-1)(-dx \wedge dy) = dx \wedge dy$, which agrees with chart $1$'s value. The pseudoform is globally well-defined.
>
> *Part (b).* The fundamental domain $D = [0, 1) \times (-1, 1)$ covers $E$ minus a measure-zero seam. In this domain $\omega = dx \wedge dy$ is the Euclidean area form, so
> $$\int_E \omega = \int_D dx \wedge dy = \int_0^1\int_{-1}^1 dy\,dx = 1 \cdot 2 = 2.$$
> This equals the geometric area of the strip (a $1 \times 2$ rectangle glued isometrically).
>
> *Part (c).* By [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]], if $E$ admitted a nowhere-vanishing ordinary $2$-form, $E$ would be orientable. But $E$ is non-orientable. Hence no such form exists.
>
> Concretely, a candidate ordinary form $\eta = f(x, y)\,dx \wedge dy$ in the fundamental domain must satisfy the form-compatibility condition $f(x + 1, -y) = -f(x, y)$ on the orientation-reversing overlap (this is the pullback formula $\tau^*\eta = (\det D\tau)\,\eta$). At every fixed point of the involution $(x, y) \mapsto (x + 1, -y)$ — i.e., for every $y = 0$ — this forces $f(x, 0) = -f(x, 0)$, so $f(x, 0) = 0$. The candidate vanishes along the core circle, hence is not nowhere-vanishing. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to "orient the Möbius strip by picking the orientation that is well-defined on one chart and extending it." This always fails: extending the orientation around the core circle returns to the starting chart with the opposite orientation. The pseudoform construction *embraces* this failure rather than fighting it — the form changes sign when the orientation does, and the integral is well-defined despite the orientation being undefined globally. Trying to integrate an "ordinary" form by ignoring the orientation-reversal is mathematically dishonest and gives the answer $0$ (the two halves of the strip contribute opposite signs and cancel).

---

# Key Takeaways

**Non-orientability is the obstruction to nowhere-vanishing top-forms, and the pseudoform construction is the minimal fix.** The Möbius strip is the simplest example of a manifold where an ordinary $2$-form cannot be nowhere-vanishing — the orientability criterion forces *every* candidate form to vanish somewhere, on a $1$-dimensional submanifold (the core circle in this case). The reusable principle is that whenever a problem asks you to integrate a top-form on a non-orientable manifold, the only way out is to switch to a *pseudoform* (or, equivalently, a density). The trigger is the appearance of a non-orientable manifold ($\mathbb{RP}^{2k}$, the Klein bottle, the Möbius strip, the orientation double cover seen from above) combined with a question about integration. The diagnostic that distinguishes pseudoforms from densities: if you need to differentiate, wedge, or apply Stokes's theorem, use a pseudoform; if you only need to integrate scalars, a density suffices. The Möbius strip example also shows the *mechanism* concretely — the two sign-failures (form-side and orientation-side) cancel, and this cancellation is the precise content of the pseudoform definition.

**The "sign factor" in the pseudoform is exactly the missing factor in the change-of-variables formula.** The deep reason ordinary forms fail to integrate on non-orientable manifolds is that the form transforms by $\det DF$ but the Riemann integral demands $|\det DF|$ — and these differ by $\mathrm{sgn}(\det DF)$, the orientation-change sign. The pseudoform inserts exactly this missing factor into the form's transformation rule. So the pseudoform construction can be viewed as "do the change-of-variables formula's sign-rectification *inside* the form, instead of outside." Once you internalize this, the pseudoform is no longer a mysterious "twisted" object — it is the form notation upgraded to compensate for the only obstruction (the sign of the Jacobian) that prevents arbitrary forms from being integrated chart-by-chart. The transferable pattern: whenever an object naturally transforms by some factor (here $J$) and the integral demands a different factor (here $|J|$), the "twist by the difference" construction (here $\mathrm{sgn}(J)$) is the minimal fix.

**Two charts and one orientation-reversing transition are the entire content of "non-orientable."** The Möbius strip's non-orientability is captured by a single transition map with $\det D\tau = -1$ between two charts. This is the *complete* obstruction — there is nothing more to non-orientability than "you cannot consistently sign the charts." The pseudoform handles this single sign-change by definition, which is why the integral is well-defined on *any* non-orientable manifold (not just the Möbius strip). The takeaway is that one should not think of non-orientability as a global mystery but as a local sign-flip that the right object (pseudoform / density / oriented double cover) handles automatically. Related: the Klein bottle requires *two* orientation-reversing transitions, but they multiply to $(-1)(-1) = +1$ around any loop (the Klein bottle is non-orientable but the orientation flips twice around each homology-generating loop) — and the pseudoform construction handles this with no change.

**The Riemannian volume "form" on a non-orientable Riemannian manifold is automatically a pseudoform.** The classical formula $\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$ uses a positive square root and an oriented coordinate frame — so on a non-orientable manifold it is a pseudo-$n$-form, not an ordinary $n$-form. This explains why "the volume of $\mathbb{RP}^2$" makes sense (it is $\int_{\mathbb{RP}^2}\omega_g$ in the pseudoform sense) even though $\mathbb{RP}^2$ has no global ordinary volume form. Whenever you compute geometric quantities (area, volume) on a Riemannian manifold without worrying about orientation, you are implicitly using the pseudoform notion. The companion exercise in the topic is [[Ex - The Sphere is Orientable but the Möbius Strip is Not]], which proves the non-orientability of $E$; this exercise then uses that fact to motivate the pseudoform machinery.
