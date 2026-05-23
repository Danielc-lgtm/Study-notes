---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Closed and Exact Forms"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
tags: [geometry, differential-geometry, de-rham, cohomology, S1]
---

# Problem Statement

Show that $H^1_{dR}(S^1) \cong \mathbb{R}$ by establishing:

(a) The angular 1-form $d\theta$ on $S^1$ is closed but not exact.

(b) The linear map $\int_{S^1} : \Omega^1(S^1) \to \mathbb{R}$ given by $\omega \mapsto \int_{S^1}\omega$ descends to a well-defined linear functional $H^1_{dR}(S^1) \to \mathbb{R}$ that is an isomorphism.

(For $S^1$ parametrize via $\theta \in [0, 2\pi)$ with the convention that $d\theta$ is the closed 1-form whose integral over $S^1$ is $2\pi$.)

**Recall:**

The **de Rham cohomology** in degree $k$ is $H^k_{dR}(M) := \ker d / \mathrm{im}\,d$, the quotient of closed $k$-forms by exact $k$-forms.

A closed form has $d\omega = 0$; an exact form has $\omega = d\eta$ for some $\eta$. Every exact form is closed ($d^2 = 0$), but not conversely.

![[Thm - Stokes' Theorem on Manifolds#Statement]]

For dimension reasons, the only non-trivial de Rham cohomology of $S^1$ is in degrees $0$ and $1$: $H^0_{dR}(S^1) = \mathbb{R}$ (locally constant functions, of which there is only one connected-component-worth, $\mathbb{R}$), and we want to show $H^1_{dR}(S^1) = \mathbb{R}$.

---

# Convergent Strategy

**Problem class:** A de Rham cohomology computation. Identifying $H^1_{dR}(S^1)$ — and the role of the angular form $d\theta$ as a non-trivial cohomology generator — is the prototype of all closed-but-not-exact arguments in differential geometry.

**Assumption pattern:** $S^1$ is a 1-dimensional closed orientable manifold. The angular form $d\theta$ is a candidate generator of $H^1$. The integration functional $\int_{S^1}$ is the natural pairing with the fundamental class of $S^1$.

**Theorem routing:** [[Thm - Stokes' Theorem on Manifolds]] is the load-bearing tool: it converts "$\omega$ exact" into "$\int_{S^1}\omega = 0$" (since $\partial S^1 = \emptyset$). So the integral is the cohomological obstruction. The argument has two parts: (i) $d\theta$ is not exact because $\int_{S^1}d\theta = 2\pi \neq 0$, while exact forms have integral zero (Stokes); (ii) every closed 1-form on $S^1$ is cohomologous to a constant multiple of $d\theta$, with constant $= \int_{S^1}\omega / 2\pi$.

**Key decision point:** The non-obvious step is recognizing that the integration functional $\int_{S^1}$ is *exactly* the de Rham cohomology class — not just a necessary condition, but a complete invariant. The argument uses: if $\omega$ and $\omega'$ are closed 1-forms with the same integral, they are cohomologous. This requires constructing an explicit primitive for $\omega - \omega'$, which is done by integration along $S^1$.

---

# Legal Operations Used

1. **Operation 2 (use Stokes to swap interior for boundary)** from the [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem#Legal Operations|topic page]]. Used in the contrapositive: an exact form has zero integral on a closed manifold, so a form with nonzero integral cannot be exact.

2. **Operation 3 (vanish-by-closed-manifold)** from the topic page. $S^1$ has no boundary, so $\int_{S^1}d\eta = \int_\emptyset\eta = 0$ for any exact $d\eta$.

3. **Construction of a primitive by integration along $S^1$.** For a closed 1-form $\omega$ with zero average ($\int_{S^1}\omega = 0$), we construct $f(\theta) := \int_0^\theta\omega$, which is well-defined (the periodicity of $\omega$ ensures $f(2\pi) = f(0)$). Then $df = \omega$, so $\omega$ is exact.

---

# Hints

> [!note]- Hint 1
> $d\theta$ on $S^1$ is a well-defined 1-form (even though $\theta$ is only defined modulo $2\pi$, the *differential* $d\theta$ is well-defined). Compute $\int_{S^1}d\theta$ directly: it is $2\pi$.

> [!note]- Hint 2
> For exactness: suppose $d\theta = df$ for some smooth $f : S^1 \to \mathbb{R}$. Then by Stokes (or the FTC on $S^1$), $\int_{S^1}d\theta = \int_{\partial S^1}f = 0$ (since $S^1$ has empty boundary). But $\int_{S^1}d\theta = 2\pi \neq 0$. Contradiction.

> [!note]- Hint 3
> For the isomorphism, define a *primitive functional*: given a closed 1-form $\omega$, the average $\bar\omega := \int_{S^1}\omega / 2\pi$ is a real number. Consider $\omega - \bar\omega\,d\theta$; this is closed and has zero integral. Show that any closed 1-form with zero integral is exact by constructing an explicit primitive.

> [!note]- Hint 4
> For a closed 1-form $\omega$ on $S^1$ with $\int_{S^1}\omega = 0$: write $\omega = g(\theta)\,d\theta$ for some smooth periodic $g$. Define $f(\theta) := \int_0^\theta g(s)\,ds$. The condition $\int_0^{2\pi}g = 0$ ensures $f(2\pi) = 0 = f(0)$, so $f$ is well-defined on $S^1$. Then $df = g\,d\theta = \omega$, showing $\omega$ is exact.

---

# Solution

The proof has three steps. **Step 1** verifies $d\theta$ is closed but not exact. **Step 2** defines the period homomorphism $\int_{S^1}$ from $H^1_{dR}(S^1)$ to $\mathbb{R}$. **Step 3** shows this is an isomorphism by exhibiting an inverse: every closed 1-form is cohomologous to a constant multiple of $d\theta$.

**Step 1: $d\theta$ is closed but not exact.**

*Closedness:* $d\theta$ is a 1-form on the 1-manifold $S^1$, so $d(d\theta) \in \Omega^2(S^1) = 0$. Closedness is automatic for top-degree 1-forms on a 1-manifold. Alternatively, $d^2 = 0$ ensures any form of the type $d(\text{something})$ is closed — but $d\theta$ is not globally of this type, as we now show.

> [!note]- Derivation
> On a 1-manifold, $\Omega^2 = 0$, so every 1-form has $d\omega = 0$ automatically. $d\theta$ is closed by this dimension argument. The substantive content is non-exactness.

*Non-exactness:* Compute $\int_{S^1}d\theta$ directly: parametrize $S^1$ by $\theta \in [0, 2\pi)$ (one chart that misses the basepoint, but the basepoint is measure-zero), so
$$\int_{S^1}d\theta = \int_0^{2\pi}d\theta = 2\pi \neq 0.$$
Suppose, for contradiction, $d\theta = df$ for some smooth $f : S^1 \to \mathbb{R}$. By [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] applied to $S^1$ (which has empty boundary),
$$\int_{S^1}d\theta = \int_{S^1}df = \int_{\partial S^1}f = \int_\emptyset f = 0.$$
But we computed $\int_{S^1}d\theta = 2\pi \neq 0$, contradiction. Hence $d\theta$ is not exact.

> [!note]- Derivation
> The key fact: a closed orientable $n$-manifold has $\partial M = \emptyset$, so by Stokes any exact $n$-form integrates to zero. For $n = 1$ and $M = S^1$: any 1-form of the type $df$ has zero integral over $S^1$. The angular form $d\theta$ has integral $2\pi$ — concretely confirmed by the parametrization. Hence $d\theta$ is not in the image of $d : \Omega^0 \to \Omega^1$, so it is not exact.

**Step 2: The period homomorphism descends to cohomology.**

Define
$$\Phi : \Omega^1(S^1) \to \mathbb{R}, \qquad \Phi(\omega) := \int_{S^1}\omega.$$
This is $\mathbb{R}$-linear by linearity of integration.

We claim $\Phi$ descends to a linear functional $\widetilde\Phi : H^1_{dR}(S^1) \to \mathbb{R}$ — that is, $\Phi$ vanishes on exact forms. Indeed, for $\omega = d\eta$ with $\eta \in \Omega^0(S^1) = C^\infty(S^1)$, by Stokes
$$\Phi(d\eta) = \int_{S^1}d\eta = \int_{\partial S^1}\eta = 0.$$
So $\Phi$ vanishes on $\mathrm{im}(d : \Omega^0 \to \Omega^1) = $ exact 1-forms, hence descends to the quotient $\Omega^1/\mathrm{im}\,d = H^1_{dR}(S^1)$.

> [!note]- Derivation
> The de Rham cohomology in degree 1 is $H^1_{dR}(S^1) = \ker(d : \Omega^1 \to \Omega^2)/\mathrm{im}(d : \Omega^0 \to \Omega^1)$. The numerator $\ker(d : \Omega^1 \to \Omega^2)$ is all of $\Omega^1$ (since $\Omega^2 = 0$ on $S^1$). The denominator $\mathrm{im}(d : \Omega^0 \to \Omega^1)$ is the space of exact 1-forms. So $H^1_{dR}(S^1) = \Omega^1(S^1) / d\Omega^0(S^1)$.
>
> The map $\Phi$ is well-defined on $\Omega^1$ and vanishes on $d\Omega^0$ (by Stokes), hence factors through the quotient as $\widetilde\Phi : H^1_{dR}(S^1) \to \mathbb{R}$.

**Step 3: $\widetilde\Phi$ is an isomorphism.**

*Surjectivity:* $\widetilde\Phi([d\theta]) = \int_{S^1}d\theta = 2\pi \neq 0$, so $\widetilde\Phi$ is non-zero, hence surjective (a non-zero linear functional on a real vector space hits all of $\mathbb{R}$).

*Injectivity:* Suppose $\widetilde\Phi([\omega]) = 0$, i.e. $\int_{S^1}\omega = 0$. We must show $\omega$ is exact.

Write $\omega = g(\theta)\,d\theta$ for some smooth periodic $g : \mathbb{R} \to \mathbb{R}$ with $g(\theta + 2\pi) = g(\theta)$ (this is just a coordinate expression: any 1-form on $S^1$ has this form locally, and the periodicity is forced by $\omega$ being globally defined). The hypothesis is $\int_0^{2\pi}g(\theta)\,d\theta = 0$.

Define $f : \mathbb{R} \to \mathbb{R}$ by $f(\theta) := \int_0^\theta g(s)\,ds$.

- $f$ is smooth (it is the integral of a smooth function).
- $f(2\pi) = \int_0^{2\pi}g = 0 = f(0)$, by the zero-average hypothesis.
- $f(\theta + 2\pi) = f(\theta) + \int_\theta^{\theta + 2\pi}g(s)\,ds = f(\theta) + 0 = f(\theta)$, using periodicity of $g$ and the hypothesis (the integral over any period of a periodic function with zero average is zero).

So $f$ is $2\pi$-periodic and descends to a smooth function on $S^1$. Compute:
$$df(\theta) = f'(\theta)\,d\theta = g(\theta)\,d\theta = \omega.$$
Hence $\omega = df$ is exact, so $[\omega] = 0$ in $H^1_{dR}(S^1)$. This proves injectivity.

> [!note]- Derivation
> The key technical step is that $f$ descends from $\mathbb{R}$ to $S^1$ because $f(\theta + 2\pi) = f(\theta)$. This is exactly the zero-average condition, $\int_0^{2\pi}g = 0$: it is the obstruction to $g\,d\theta$ being exact. If $\int_0^{2\pi}g \neq 0$, then $f(\theta + 2\pi) - f(\theta) = \int_0^{2\pi}g \neq 0$, so $f$ does *not* descend to $S^1$, and no globally defined primitive on $S^1$ exists.

**Conclusion.** $\widetilde\Phi : H^1_{dR}(S^1) \to \mathbb{R}$ is a bijective linear map, hence an isomorphism:
$$H^1_{dR}(S^1) \cong \mathbb{R}, \quad\text{generated by the class }[d\theta]\text{ with period }2\pi.$$

> [!note]- Complete formal solution
> **Step 1.** $d\theta$ is a smooth 1-form on $S^1$, closed (automatically, $\Omega^2(S^1) = 0$). It is not exact: if $d\theta = df$, then by [[Thm - Stokes' Theorem on Manifolds]] (with $M = S^1$, $\partial M = \emptyset$),
> $$2\pi = \int_{S^1}d\theta = \int_{S^1}df = \int_{\partial S^1}f = 0,$$
> contradiction. Hence $[d\theta] \neq 0$ in $H^1_{dR}(S^1)$.
>
> **Step 2.** Define $\widetilde\Phi : H^1_{dR}(S^1) \to \mathbb{R}$, $[\omega] \mapsto \int_{S^1}\omega$. This is well-defined: if $\omega' - \omega = d\eta$, then $\int_{S^1}\omega' - \int_{S^1}\omega = \int_{S^1}d\eta = 0$ by Stokes.
>
> **Step 3.** $\widetilde\Phi([d\theta]) = 2\pi \neq 0$, so $\widetilde\Phi$ is non-zero, hence surjective.
>
> **Step 4.** Injectivity. Suppose $\int_{S^1}\omega = 0$. Write $\omega = g(\theta)\,d\theta$ for a smooth periodic $g$ with $\int_0^{2\pi}g = 0$. Define $f(\theta) := \int_0^\theta g(s)\,ds$; then $f(2\pi) = 0 = f(0)$ and $f(\theta + 2\pi) = f(\theta)$ for all $\theta$, so $f$ descends to $C^\infty(S^1)$. We have $df = g\,d\theta = \omega$, so $\omega = df$ is exact, $[\omega] = 0$.
>
> Hence $\widetilde\Phi$ is an isomorphism, and $H^1_{dR}(S^1) \cong \mathbb{R}$, generated by $[d\theta]$. $\blacksquare$

> [!warning] Illegal but tempting: "$\theta$ is a function, so $d\theta = d(\theta)$ is exact"
> One might think: $\theta$ is the angular coordinate, hence a function on $S^1$, hence $d\theta$ is exact. **This is wrong.** $\theta$ is *not* a globally defined smooth function on $S^1$: any continuous choice of "angle" on $S^1$ must jump by $2\pi$ somewhere (typically at a chosen basepoint). The differential $d\theta$ is well-defined globally — locally any branch of $\theta$ gives the same $d\theta$ — but no global function $\theta$ exists whose differential is $d\theta$. The integral $\int_{S^1}d\theta = 2\pi$ is exactly the failure of $\theta$ to be single-valued. This is the standard example of a closed-but-not-exact form, and it is the *generator* of $H^1_{dR}(S^1)$.

---

# Key Takeaways

**Period integrals detect cohomology classes.** The integral of a closed $k$-form over a closed $k$-cycle is a *cohomology invariant* — it is the same for all closed forms in the same cohomology class, by Stokes. Conversely, for $S^1$ (and more generally for closed orientable manifolds via de Rham's theorem), all the cohomological information is captured by such period integrals. The takeaway: whenever you want to know if a closed form is exact, compute its periods; if any period is nonzero, the form is not exact, and its class is a nonzero element of cohomology. This is the *operational* meaning of de Rham cohomology — a closed form mod exact equals the collection of its periods over a basis of homology cycles.

**The angular form $d\theta$ is the universal "winding number" 1-form.** On $\mathbb{R}^2 \setminus \{0\}$, the form $d\theta = (-y\,dx + x\,dy)/(x^2 + y^2)$ generates $H^1_{dR}(\mathbb{R}^2\setminus\{0\}) = \mathbb{R}$ in the same way, with the integral over a closed curve giving $2\pi$ times the winding number of the curve around the origin. The connection between $S^1$ and $\mathbb{R}^2\setminus\{0\}$ is that the latter deformation-retracts onto the former; the cohomology computations are the same, and the generator is the "angular form" in both cases. The takeaway: $d\theta$ is the prototype of all non-exact closed 1-forms, and recognizing it (or its translates) in disguise is the first step of many cohomological arguments.

**The construction of $f(\theta) = \int_0^\theta g$ as a primitive works iff the average vanishes — and this is the cohomological obstruction.** This is the cleanest exhibition of the closed-but-not-exact mechanism: when $\int_0^{2\pi}g = 0$, the antiderivative $f$ closes up and descends to $S^1$, making $g\,d\theta$ exact. When $\int_0^{2\pi}g \neq 0$, $f$ has a "jump" of $\int_0^{2\pi}g$ as $\theta$ winds once around $S^1$, and there is no single-valued primitive on $S^1$. This jump is *exactly* the cohomological invariant. This pattern recurs throughout the theory: integrals over closed cycles obstruct exactness, and de Rham cohomology is precisely the collection of such obstructions.

**Companion exercises.** [[Ex - A Form that is Closed but Not Exact on the Punctured Plane]] in [[Differential Geometry VIII — Differential Forms]] does this same computation on $\mathbb{R}^2\setminus\{0\}$, showing $H^1_{dR}(\mathbb{R}^2\setminus\{0\}) = \mathbb{R}$ with the angular form $d\theta$ as generator. [[Ex - The de Rham Cohomology of R^n is Trivial in Positive Degrees]] in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|the next topic]] shows the Poincaré lemma: on a contractible space all closed forms are exact, hence all positive-degree cohomology vanishes. Together with this exercise, these compute the basic examples of de Rham cohomology and exhibit the role of topology in distinguishing closed from exact.
