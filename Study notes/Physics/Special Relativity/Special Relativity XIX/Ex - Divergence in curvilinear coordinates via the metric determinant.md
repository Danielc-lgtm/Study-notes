---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Divergence of a Vector and Tensor Field"
  - "Def - Christoffel Symbols"
tags: [physics, special-relativity]
---

# Problem Statement

1. Using the determinant formula $\boldsymbol{\nabla}\!\cdot\vec{v} = \frac{1}{\sqrt{-\det g}}\partial_\mu(\sqrt{-\det g}\,v^\mu)$, derive the explicit divergence of a vector field in spherical coordinates $(ct,r,\theta,\varphi)$, where $g_{\alpha\beta} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$.
2. Apply your formula to the radial coordinate basis vector $\vec{v} = \vec{e}_r$ (components $v^\alpha = (0,1,0,0)$) and show $\boldsymbol{\nabla}\!\cdot\vec{e}_r = 2/r$. Confirm the same answer from the connection-coefficient form $\boldsymbol{\nabla}\!\cdot\vec{v} = \partial_\mu v^\mu + \Gamma^\nu{}_{\mu\nu}v^\mu$.
3. Apply it to $\vec{w} = \vec{e}_x$ — a genuinely constant field — expressed in spherical components $w^\alpha = (0,\sin\theta\cos\varphi,\cos\theta\cos\varphi/r,-\sin\varphi/(r\sin\theta))$, and show $\boldsymbol{\nabla}\!\cdot\vec{e}_x = 0$, as it must be.

**Recall:**

![[Thm - Divergence of a Vector and Tensor Field#Statement]]

The metric determinant in spherical coordinates is $\det g = -r^4\sin^2\theta$, so $\sqrt{-\det g} = r^2\sin\theta$ (with $c = 1$).

---

# Convergent Strategy

**Problem class.** A *compute-a-divergence-in-curvilinear-coordinates* problem, the headline application of [[Thm - Divergence of a Vector and Tensor Field]]. The determinant formula bypasses the Christoffel symbols entirely.

**Assumption pattern.** Spherical coordinates with diagonal metric; the determinant is the product of the diagonal entries, $\det g = -r^4\sin^2\theta$. The two test fields, $\vec{e}_r$ and $\vec{e}_x$, are chosen to probe opposite extremes: $\vec{e}_r$ has constant components but nonzero divergence, $\vec{e}_x$ has varying components but zero divergence.

**Theorem routing.** Part 1 substitutes $\sqrt{-\det g} = r^2\sin\theta$ into the determinant formula. Part 2 applies it to $\vec{e}_r$ and cross-checks with the trace-of-Christoffel form $\Gamma^\nu{}_{\mu\nu}$ from [[Def - Christoffel Symbols]]. Part 3 applies it to $\vec{e}_x$.

**Key decision point.** The instructive choice is to verify the radial result *both* ways — determinant formula and connection-coefficient formula — to see that they agree, and to recognise that the $\vec{e}_x$ case *must* give zero (a constant field has zero divergence) as a sanity check that the curvilinear machinery is correct.

---

# Legal Operations Used

1. **Compute a divergence by the determinant formula** (operation 5 from the topic page). Substitute $\sqrt{-\det g} = r^2\sin\theta$ and differentiate.
2. **Compute Christoffel symbols from the metric** (operation 2 from the topic page). Used for the cross-check via $\Gamma^\nu{}_{\mu\nu}$.

---

# Hints

> [!note]- Hint 1
> $\det g$ of a diagonal matrix is the product of the diagonal entries: $\det g = (1)(-1)(-r^2)(-r^2\sin^2\theta) = -r^4\sin^2\theta$, so $\sqrt{-\det g} = r^2\sin\theta$. The formula becomes $\frac{1}{r^2\sin\theta}\partial_\mu(r^2\sin\theta\,v^\mu)$.

> [!note]- Hint 2
> Expand the sum over $\mu = ct,r,\theta,\varphi$. The factor $r^2\sin\theta$ depends on $r$ and $\theta$ but not $ct$ or $\varphi$, so $\partial_{ct}(r^2\sin\theta\,v^0) = r^2\sin\theta\,\partial_{ct}v^0$ and $\partial_\varphi(r^2\sin\theta\,v^\varphi) = r^2\sin\theta\,\partial_\varphi v^\varphi$.

> [!note]- Hint 3
> $\boldsymbol{\nabla}\!\cdot\vec{v} = \frac{1}{c}\partial_{ct}v^0\cdot c + \frac{1}{r^2}\partial_r(r^2 v^r) + \frac{1}{\sin\theta}\partial_\theta(\sin\theta\,v^\theta) + \partial_\varphi v^\varphi$. (With $c=1$: $\partial_{ct}v^0 + \frac{1}{r^2}\partial_r(r^2 v^r) + \frac{1}{\sin\theta}\partial_\theta(\sin\theta v^\theta) + \partial_\varphi v^\varphi$.) For $\vec{e}_r$, only $v^r = 1$ is nonzero, giving $\frac{1}{r^2}\partial_r(r^2) = 2/r$.

> [!note]- Hint 4
> For the Christoffel check, $\Gamma^\nu{}_{r\nu} = \Gamma^\theta{}_{r\theta}+\Gamma^\varphi{}_{r\varphi} = 1/r + 1/r = 2/r$ (the other traces vanish). With $v^\mu = \delta^\mu_r$, $\boldsymbol{\nabla}\!\cdot\vec{v} = \partial_\mu\delta^\mu_r + \Gamma^\nu{}_{r\nu} = 0 + 2/r$.

---

# Solution

The plan: Step 1 derives the spherical divergence operator from the determinant $\sqrt{-\det g} = r^2\sin\theta$. Step 2 applies it to $\vec{e}_r$ (constant components, divergence $2/r$) and cross-checks via the Christoffel trace. Step 3 applies it to $\vec{e}_x$ (varying components, divergence $0$) as a sanity check.

**Step 1: The spherical divergence operator.**

> [!note]- Derivation
> The metric is diagonal, so its determinant is the product of the diagonal entries:
> $$\det g = (1)\cdot(-1)\cdot(-r^2)\cdot(-r^2\sin^2\theta) = -r^4\sin^2\theta, \qquad \sqrt{-\det g} = r^2\sin\theta.$$
> Substituting into $\boldsymbol{\nabla}\!\cdot\vec{v} = \frac{1}{\sqrt{-\det g}}\partial_\mu(\sqrt{-\det g}\,v^\mu)$ and expanding the sum over $\mu = (ct,r,\theta,\varphi)$, noting that $r^2\sin\theta$ is independent of $ct$ and $\varphi$:
> $$\boldsymbol{\nabla}\!\cdot\vec{v} = \frac{1}{r^2\sin\theta}\Big[\partial_{ct}(r^2\sin\theta\,v^0) + \partial_r(r^2\sin\theta\,v^r) + \partial_\theta(r^2\sin\theta\,v^\theta) + \partial_\varphi(r^2\sin\theta\,v^\varphi)\Big]$$
> $$= \frac{\partial v^0}{\partial(ct)} + \frac{1}{r^2}\frac{\partial}{\partial r}\big(r^2 v^r\big) + \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\big(\sin\theta\,v^\theta\big) + \frac{\partial v^\varphi}{\partial\varphi}.$$
> (Restoring $c$: the first term is $\frac1c\partial_t v^0$.) The spatial part is exactly the classical spherical divergence of vector calculus, with the time term added.

**Step 2: Divergence of $\vec{e}_r$ is $2/r$ — two ways.**

> [!note]- Derivation
> *Determinant formula.* For $\vec{v} = \vec{e}_r$, $v^\alpha = (0,1,0,0)$, so only the radial term survives:
> $$\boldsymbol{\nabla}\!\cdot\vec{e}_r = \frac{1}{r^2}\frac{\partial}{\partial r}(r^2\cdot 1) = \frac{1}{r^2}\cdot 2r = \frac{2}{r}.$$
>
> *Connection-coefficient formula.* Using $\boldsymbol{\nabla}\!\cdot\vec{v} = \partial_\mu v^\mu + \Gamma^\nu{}_{\mu\nu}v^\mu$ with $v^\mu = \delta^\mu_r$ (constant, so $\partial_\mu v^\mu = 0$):
> $$\boldsymbol{\nabla}\!\cdot\vec{e}_r = \Gamma^\nu{}_{r\nu} = \Gamma^{(ct)}{}_{r(ct)} + \Gamma^r{}_{rr} + \Gamma^\theta{}_{r\theta} + \Gamma^\varphi{}_{r\varphi} = 0 + 0 + \frac{1}{r} + \frac{1}{r} = \frac{2}{r}.$$
> The two methods agree. Note the lesson: the components of $\vec{e}_r$ are *constant*, so the naive $\partial_\mu v^\mu = 0$ would give zero — the entire divergence $2/r$ comes from the connection (equivalently from the $r^2$ weighting in the determinant formula), exactly because $\vec{e}_r$ is not a constant field.

**Step 3: Divergence of $\vec{e}_x$ is zero — the sanity check.**

> [!note]- Derivation
> The field $\vec{w} = \vec{e}_x$ is genuinely constant on flat spacetime, so its divergence *must* be zero in any coordinates; the curvilinear computation had better confirm it. Its spherical components are $w^\alpha = (0,\,\sin\theta\cos\varphi,\,\cos\theta\cos\varphi/r,\,-\sin\varphi/(r\sin\theta))$. Apply the spherical divergence operator:
> $$\frac{1}{r^2}\partial_r(r^2 w^r) = \frac{1}{r^2}\partial_r(r^2\sin\theta\cos\varphi) = \frac{1}{r^2}(2r\sin\theta\cos\varphi) = \frac{2\sin\theta\cos\varphi}{r},$$
> $$\frac{1}{\sin\theta}\partial_\theta(\sin\theta\,w^\theta) = \frac{1}{\sin\theta}\partial_\theta\Big(\sin\theta\cdot\frac{\cos\theta\cos\varphi}{r}\Big) = \frac{\cos\varphi}{r\sin\theta}\partial_\theta(\sin\theta\cos\theta) = \frac{\cos\varphi}{r\sin\theta}(\cos^2\theta-\sin^2\theta),$$
> $$\partial_\varphi w^\varphi = \partial_\varphi\Big(\frac{-\sin\varphi}{r\sin\theta}\Big) = \frac{-\cos\varphi}{r\sin\theta}.$$
> Add the three (the time term is zero, $w^0 = 0$). The second and third combine: $\frac{\cos\varphi}{r\sin\theta}(\cos^2\theta-\sin^2\theta) - \frac{\cos\varphi}{r\sin\theta} = \frac{\cos\varphi}{r\sin\theta}(\cos^2\theta-\sin^2\theta-1) = \frac{\cos\varphi}{r\sin\theta}(-2\sin^2\theta) = -\frac{2\sin\theta\cos\varphi}{r}$. This cancels the first term:
> $$\boldsymbol{\nabla}\!\cdot\vec{e}_x = \frac{2\sin\theta\cos\varphi}{r} - \frac{2\sin\theta\cos\varphi}{r} = 0. \checkmark$$
> The divergence vanishes, confirming that the curvilinear formula correctly recognises $\vec{e}_x$ as a constant field despite its position-dependent components.

> [!note]- Complete formal solution
> With $\det g = -r^4\sin^2\theta$, $\sqrt{-\det g} = r^2\sin\theta$, the determinant formula gives the spherical divergence $\boldsymbol{\nabla}\!\cdot\vec{v} = \partial_{ct}v^0 + \frac{1}{r^2}\partial_r(r^2 v^r) + \frac{1}{\sin\theta}\partial_\theta(\sin\theta v^\theta) + \partial_\varphi v^\varphi$. For $\vec{e}_r$ ($v^\alpha = (0,1,0,0)$), only the radial term survives: $\frac{1}{r^2}\partial_r(r^2) = 2/r$; equivalently $\Gamma^\nu{}_{r\nu} = \Gamma^\theta{}_{r\theta}+\Gamma^\varphi{}_{r\varphi} = 2/r$. For $\vec{e}_x$ ($w^\alpha = (0,\sin\theta\cos\varphi,\cos\theta\cos\varphi/r,-\sin\varphi/(r\sin\theta))$), the radial term $\frac{2\sin\theta\cos\varphi}{r}$ is cancelled by the $\theta$ and $\varphi$ terms, giving $\boldsymbol{\nabla}\!\cdot\vec{e}_x = 0$, as required for a constant field. $\blacksquare$

---

# Key Takeaways

**The determinant formula computes any curvilinear divergence without a single Christoffel symbol — that is its entire value.** Confronted with a divergence in spherical, cylindrical, or any curvilinear coordinates, the determinant formula $\boldsymbol{\nabla}\!\cdot\vec{v} = \frac{1}{\sqrt{-\det g}}\partial_\mu(\sqrt{-\det g}\,v^\mu)$ lets you skip the connection entirely: compute $\det g$ (the product of diagonal entries for an orthogonal metric), take $\sqrt{-\det g}$, and the divergence is one over it times the partial of (it times the component). The classical spherical divergence $\frac{1}{r^2}\partial_r(r^2 v^r) + \cdots$ falls out in two lines, and the $\frac{1}{r^2}$ and $\frac{1}{\sin\theta}$ weightings are nothing but the $\sqrt{-\det g}$ factor. The trigger is any divergence or conservation law off inertial coordinates; the diagnostic is that the determinant packages the entire Christoffel trace $\Gamma^\nu{}_{\mu\nu}$ into a single logarithmic derivative, which is exactly why no connection coefficient is needed.

**Constant components do not mean zero divergence, and varying components do not mean nonzero divergence — the two test fields make this unforgettable.** The radial field $\vec{e}_r$ has constant components $(0,1,0,0)$ yet divergence $2/r$, because $\vec{e}_r$ genuinely spreads out as it points radially; the Cartesian field $\vec{e}_x$ has elaborately varying spherical components yet divergence exactly zero, because it is a constant field in disguise. The naive $\partial_\mu v^\mu$ gets both wrong — zero for $\vec{e}_r$, nonzero for $\vec{e}_x$ — while the determinant formula (equivalently the covariant divergence) gets both right. The reusable diagnostic is to *always* sanity-check a curvilinear divergence against the physics: a known constant field must give zero, a known radial field must give the geometric spreading rate, and any other answer signals an error in the connection bookkeeping. This frame-invariance check is the analogue, for tensor calculus, of checking units in elementary physics.

**Cross-checking the determinant formula against the connection form is the way to trust your Christoffel symbols.** Computing $\boldsymbol{\nabla}\!\cdot\vec{e}_r$ both by the determinant formula ($\frac{1}{r^2}\partial_r r^2 = 2/r$) and by the Christoffel trace ($\Gamma^\theta{}_{r\theta}+\Gamma^\varphi{}_{r\varphi} = 2/r$) is more than redundancy: the agreement verifies, in one stroke, both that the determinant was computed correctly and that the Christoffel symbols of the previous exercise are right, since the two routes share no intermediate steps. When a relativistic computation gives an unexpected divergence, recomputing it the other way localises the error to either the determinant or the connection. This habit — solve it twice by independent routes and demand agreement — is the single most reliable defence against sign and bookkeeping mistakes in tensor calculus, and the determinant-versus-connection pair is the cleanest such check available for divergences.
