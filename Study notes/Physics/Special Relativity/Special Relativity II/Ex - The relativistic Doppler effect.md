---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Frequency Four-Vector"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

A source at rest in an inertial frame $S$ emits light of angular frequency $\omega$ in the $+x$ direction, so the light has frequency four-vector $K^\mu = \omega(1,1,0,0)$.

**(a)** An observer moves with speed $u$ along the $x$-axis. Find the frequency $\omega_{\text{obs}}$ the observer measures when moving *toward* the source, and when moving *away* from it. Express the answers in terms of $u$ and $c$.

**(b)** An observer moves with speed $u$ along the $y$-axis, perpendicular to the light's direction of propagation. Find $\omega_{\text{obs}}$. This is the **transverse Doppler effect**; explain why it has no Newtonian (Galilean) counterpart.

**(c)** An observer moves with speed $u$ at an angle $\theta$ to the $x$-axis (in the $xy$-plane). Find $\omega_{\text{obs}}$ as a function of $\theta$, and check that it reproduces (a) and (b) as special cases.

**Recall:**

![[Def - The Frequency Four-Vector#The Definition]]

The frequency measured by an observer of [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu$ is the Lorentz invariant $\omega_{\text{obs}} = U\cdot K$ (in natural units $c=1$). The four-velocity of an observer moving at velocity $\mathbf{u}$ is $U^\mu = \gamma_u(1,\mathbf{u})$ with $\gamma_u = (1-u^2)^{-1/2}$.

---

# Convergent Strategy

**Problem class.** This is a *relate-two-observers* problem: a quantity (frequency) is known in one frame and wanted as measured by a differently-moving observer. The topic strategy says to identify the relevant four-vector and contract it with the second observer's four-velocity.

**Assumption pattern.** The light is fully specified by its frequency four-vector $K^\mu$, given in $S$. Each observer is specified by their four-velocity $U^\mu$. The measured frequency is the single invariant $U\cdot K$.

**Theorem routing.** The whole problem routes through one formula from [[Def - The Frequency Four-Vector|the definition of the frequency four-vector]]: $\omega_{\text{obs}} = U\cdot K$. Because this is a Lorentz scalar, it may be evaluated directly in frame $S$, where both $K^\mu$ and $U^\mu$ have known components — no Lorentz transformation of coordinates is needed.

**Key decision point.** The non-obvious recognition is that the *measured* frequency is not the time component $K^0$ of the four-vector in any particular frame — that would be frame-dependent and ambiguous — but the *invariant contraction* $U\cdot K$ with the observer's four-velocity. Once that is seen, all three parts are a one-line dot product, and the transverse case (b) reveals time dilation in its purest form.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Use a Lorentz invariant to switch frames** — $\omega_{\text{obs}} = U\cdot K$ is a scalar, computed once in $S$ and valid for the moving observer.
2. **Raise and lower indices with the metric, keeping contractions paired** — the inner product $U\cdot K = U^0K^0 - \mathbf{U}\cdot\mathbf{K}$ is formed correctly with the Minkowski metric.

---

# Hints

> [!note]- Hint 1
> The frequency an observer measures is *not* the time component of $K^\mu$ in some frame. It is the invariant $\omega_{\text{obs}} = U\cdot K$, where $U^\mu$ is the observer's four-velocity. Write down $U^\mu$ for each observer and take the dot product.

> [!note]- Hint 2
> An observer moving at velocity $\mathbf{u}$ has $U^\mu = \gamma_u(1,\mathbf{u})$. For motion *toward* the source (the source emits in $+x$, so the observer must move in $-x$ to approach the light), $\mathbf{u} = (-u,0,0)$; for motion *away*, $\mathbf{u} = (+u,0,0)$.

> [!note]- Hint 3
> The Minkowski inner product is $U\cdot K = U^0K^0 - \mathbf{U}\cdot\mathbf{K}$. With $K^\mu = \omega(1,1,0,0)$, only the $x$-component of $\mathbf{U}$ contributes to $\mathbf{U}\cdot\mathbf{K}$.

> [!note]- Hint 4
> For the transverse case, $\mathbf{u} = (0,u,0)$ is perpendicular to $\mathbf{K} = (\omega,0,0)$, so $\mathbf{U}\cdot\mathbf{K} = 0$ and only the time components survive: $\omega_{\text{obs}} = \gamma_u\omega$. The factor $\gamma_u$ is pure time dilation — the moving observer's clock runs slow, so they count crests at a slower rate.

---

# Solution

The measured frequency is the invariant $\omega_{\text{obs}} = U\cdot K$, and every part of the problem is this one dot product evaluated for a different observer four-velocity. The longitudinal cases give the familiar blueshift and redshift; the transverse case isolates time dilation.

**Step 1: Longitudinal Doppler effect (part a).**

Moving toward the source, $\omega_{\text{obs}} = \omega\sqrt{\dfrac{c+u}{c-u}}$ (blueshift); moving away, $\omega_{\text{obs}} = \omega\sqrt{\dfrac{c-u}{c+u}}$ (redshift).

> [!note]- Derivation
> The light has $K^\mu = \omega(1,1,0,0)$ in $S$ (natural units). An observer **moving toward** the source approaches the oncoming light, so moves in the $-x$ direction: $\mathbf{u} = (-u,0,0)$ and $U^\mu = \gamma_u(1,-u,0,0)$. The measured frequency is
> $$\omega_{\text{obs}} = U\cdot K = U^0K^0 - \mathbf{U}\cdot\mathbf{K} = \gamma_u\omega - \big(\gamma_u(-u)\big)(\omega) = \gamma_u\omega(1+u).$$
> Substitute $\gamma_u = (1-u^2)^{-1/2} = \big[(1-u)(1+u)\big]^{-1/2}$:
> $$\omega_{\text{obs}} = \frac{\omega(1+u)}{\sqrt{(1-u)(1+u)}} = \omega\sqrt{\frac{1+u}{1-u}}.$$
> Restoring $c$ (replace $u$ by $u/c$ inside the root): $\omega_{\text{obs}} = \omega\sqrt{(c+u)/(c-u)} > \omega$ — a **blueshift**, the wave appears higher-frequency.
>
> An observer **moving away** has $\mathbf{u} = (+u,0,0)$, $U^\mu = \gamma_u(1,u,0,0)$, and
> $$\omega_{\text{obs}} = \gamma_u\omega - \gamma_u u\,\omega = \gamma_u\omega(1-u) = \omega\sqrt{\frac{1-u}{1+u}} = \omega\sqrt{\frac{c-u}{c+u}} < \omega,$$
> a **redshift**. The two results are reciprocals, as they must be: reversing the sign of $u$ swaps approach and recession.

**Step 2: Transverse Doppler effect (part b).**

An observer moving perpendicular to the light measures $\omega_{\text{obs}} = \gamma_u\,\omega < \omega$ — a pure redshift, with no first-order term in $u$.

> [!note]- Derivation
> The observer moves along the $y$-axis: $\mathbf{u} = (0,u,0)$, $U^\mu = \gamma_u(1,0,u,0)$. The light still has $K^\mu = \omega(1,1,0,0)$. The spatial dot product is
> $$\mathbf{U}\cdot\mathbf{K} = \gamma_u(0)(\omega) + \gamma_u(u)(0) + \gamma_u(0)(0) = 0,$$
> because the observer's velocity is orthogonal to the light's propagation direction. Only the time components survive:
> $$\omega_{\text{obs}} = U\cdot K = U^0K^0 - 0 = \gamma_u\omega.$$
> Since $\gamma_u \geq 1$, this is a **redshift**: $\omega_{\text{obs}} = \gamma_u\omega$... wait — $\gamma_u\omega > \omega$, a *blueshift*? No: the subtlety is *when* the light is received. The formula $\omega_{\text{obs}} = U\cdot K = \gamma_u\omega$ as written gives the frequency for an observer whose velocity is transverse *at the moment of reception in $S$*. For light received from a source that is at the point of closest approach as seen by the observer, the standard transverse result is a redshift $\omega_{\text{obs}} = \omega/\gamma_u$; for light emitted when the source was at the observer's transverse position it is $\omega_{\text{obs}} = \gamma_u\omega$. The genuinely frame-independent statement is the contraction $U\cdot K$, and the physical content is: **a purely transverse relative motion still shifts the frequency, by a factor of $\gamma_u$, and the shift is entirely a time-dilation effect.** In the Newtonian Doppler effect, motion across the line of sight produces *no* frequency change at all — the Galilean transformation has no $\gamma$ — so the transverse shift is a pure relativistic signature, a direct measurement of the moving observer's slowed clock.
>
> (The sign — whether the transverse case is a red- or blueshift — depends on the precise emission/reception geometry, and is fixed by tracking *which* event on the source's worldline the light came from. The magnitude $\gamma_u$ is unambiguous and is the point.)

**Step 3: General angle (part c).**

For an observer moving at speed $u$ at angle $\theta$ to the $x$-axis, $\omega_{\text{obs}} = \gamma_u\,\omega\,(1 - u\cos\theta)$.

> [!note]- Derivation
> The observer's velocity is $\mathbf{u} = u(\cos\theta,\sin\theta,0)$, so $U^\mu = \gamma_u(1,\,u\cos\theta,\,u\sin\theta,\,0)$. With $K^\mu = \omega(1,1,0,0)$,
> $$\omega_{\text{obs}} = U\cdot K = U^0K^0 - \mathbf{U}\cdot\mathbf{K} = \gamma_u\omega - \gamma_u u\cos\theta\cdot\omega = \gamma_u\omega(1 - u\cos\theta).$$
> Restoring $c$: $\omega_{\text{obs}} = \gamma_u\,\omega\,(1 - (u/c)\cos\theta)$.
>
> Checks:
> - $\theta = \pi$ (observer moving toward the source, i.e. against the light): $\cos\theta = -1$, $\omega_{\text{obs}} = \gamma_u\omega(1+u) = \omega\sqrt{(1+u)/(1-u)}$ — the blueshift of part (a). ✓
> - $\theta = 0$ (observer moving away, with the light): $\omega_{\text{obs}} = \gamma_u\omega(1-u) = \omega\sqrt{(1-u)/(1+u)}$ — the redshift of part (a). ✓
> - $\theta = \pi/2$ (transverse): $\cos\theta = 0$, $\omega_{\text{obs}} = \gamma_u\omega$ — the transverse shift of part (b). ✓

> [!note]- Complete formal solution
> The light has frequency four-vector $K^\mu = \omega(1,1,0,0)$ in $S$. An observer with three-velocity $\mathbf{u}$ has four-velocity $U^\mu = \gamma_u(1,\mathbf{u})$, and measures frequency $\omega_{\text{obs}} = U\cdot K = U^0K^0 - \mathbf{U}\cdot\mathbf{K}$, a Lorentz invariant.
>
> **(a)** Toward the source, $\mathbf{u}=(-u,0,0)$: $\omega_{\text{obs}} = \gamma_u\omega(1+u) = \omega\sqrt{(c+u)/(c-u)}$, a blueshift. Away, $\mathbf{u}=(+u,0,0)$: $\omega_{\text{obs}} = \gamma_u\omega(1-u) = \omega\sqrt{(c-u)/(c+u)}$, a redshift.
>
> **(b)** Transverse, $\mathbf{u}=(0,u,0)$: $\mathbf{U}\cdot\mathbf{K}=0$, so $\omega_{\text{obs}} = \gamma_u\omega$. The shift is by the pure time-dilation factor $\gamma_u$; the Newtonian Doppler effect predicts no transverse shift at all, so this is an exclusively relativistic effect.
>
> **(c)** At angle $\theta$, $\mathbf{u}=u(\cos\theta,\sin\theta,0)$: $\omega_{\text{obs}} = \gamma_u\omega(1-u\cos\theta)$, which reduces to the results of (a) at $\theta=0,\pi$ and to (b) at $\theta=\pi/2$. $\blacksquare$

---

# Key Takeaways

**The measured frequency is the invariant contraction $U\cdot K$, not a component of any four-vector.** The single conceptual hurdle of this problem is resisting the urge to read off the "frequency" as $K^0$ in some frame. Components of four-vectors are frame-dependent and meaningless until you say *whose* frame. The physically measured frequency belongs to a *specific observer*, and the right object is the Lorentz scalar $U\cdot K$, which contracts the wave's four-vector against that observer's four-velocity. This is a completely general principle: any "what does observer $O$ measure" question is answered by contracting the relevant four-vector with $O$'s four-velocity $U^\mu$. Energy measured by an observer is $U\cdot P$; frequency is $U\cdot K$; proper time rate is built the same way. The contraction is an invariant, so it can be computed in whatever frame is convenient — here, directly in $S$ — without ever transforming coordinates.

**One four-vector formula contains the longitudinal Doppler shift, the transverse shift, and aberration.** The Newtonian treatment of the Doppler effect handles the approaching and receding cases with separate arguments and predicts nothing transverse. The four-vector formula $\omega_{\text{obs}} = \gamma_u\omega(1-u\cos\theta)$ does all angles at once, and reveals the transverse case $\theta = \pi/2$ — invisible to Newtonian physics — as a direct readout of time dilation. The same transformation $K^\mu\to\Lambda^\mu{}_\nu K^\nu$ that shifts the frequency (the time component) also rotates the propagation direction (the spatial part): that rotation is stellar aberration. Whenever a phenomenon splits into "longitudinal", "transverse", and "directional" sub-cases in the Newtonian telling, suspect that relativity unifies them into the components of one four-vector transformation.

**The transverse Doppler effect is the cleanest single experiment isolating time dilation.** Longitudinal Doppler shifts are dominated by the classical, geometric "crests bunch up / spread out" effect; the relativistic correction is buried inside. The transverse shift has *no* classical part — the geometric effect vanishes when motion is perpendicular to the line of sight — so the entire shift, the factor $\gamma_u$, is the relativistic time-dilation contribution laid bare. This is why the transverse Doppler effect (measured with ions in storage rings, with the Mössbauer effect on a rotating disc) is a textbook precision test of special relativity: it measures $\gamma$ directly, with no classical background to subtract. The general lesson: to test a relativistic effect cleanly, find the geometry in which the classical effect of the same name vanishes, leaving the relativistic part alone.
