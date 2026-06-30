---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Christoffel Symbols"
  - "Def - Arbitrary Coordinates and the Coordinate Basis"
tags: [physics, special-relativity]
---

# Problem Statement

On flat spacetime in spherical coordinates $(x^\alpha) = (ct,r,\theta,\varphi)$ the metric is $g_{\alpha\beta} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$.

1. Write the inverse metric $g^{\alpha\beta}$.
2. Using the Christoffel formula $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\mu}(\partial_\alpha g_{\mu\beta}+\partial_\beta g_{\alpha\mu}-\partial_\mu g_{\alpha\beta})$, compute all nonzero Christoffel symbols.
3. Verify your answers against the known list $\Gamma^r{}_{\theta\theta}=-r$, $\Gamma^r{}_{\varphi\varphi}=-r\sin^2\theta$, $\Gamma^\theta{}_{r\theta}=1/r$, $\Gamma^\theta{}_{\varphi\varphi}=-\sin\theta\cos\theta$, $\Gamma^\varphi{}_{r\varphi}=1/r$, $\Gamma^\varphi{}_{\theta\varphi}=\cot\theta$.
4. Confirm that the time coordinate contributes no Christoffel symbols, and remark on the sign-independence of the result between signatures.

**Recall:**

![[Def - Christoffel Symbols#The Definition]]

The Christoffel formula is valid only in a coordinate basis, and the symbols are symmetric in their lower indices, $\Gamma^\gamma{}_{\alpha\beta}=\Gamma^\gamma{}_{\beta\alpha}$.

---

# Convergent Strategy

**Problem class.** A *compute-the-connection-from-the-metric* problem, the central mechanical drill of [[Def - Christoffel Symbols]]. The route is: invert the (diagonal) metric, then evaluate the formula term by term, exploiting diagonality and the symmetry in $\alpha\beta$.

**Assumption pattern.** The metric is diagonal, so $g^{\gamma\mu}$ is diagonal and the sum over $\mu$ in the formula collapses to $\mu = \gamma$. Only the few metric components that depend on $r$ or $\theta$ have nonzero derivatives ($g_{\theta\theta} = -r^2$, $g_{\varphi\varphi} = -r^2\sin^2\theta$), so only Christoffels with the right index pattern survive.

**Theorem routing.** Part 1 inverts a diagonal matrix. Part 2 applies the formula of [[Def - Christoffel Symbols]]. Parts 3–4 are checks.

**Key decision point.** The labour-saving choice is to use diagonality to set $\mu = \gamma$ immediately, and the symmetry $\Gamma^\gamma{}_{\alpha\beta} = \Gamma^\gamma{}_{\beta\alpha}$ to compute each symbol once. The only nonzero derivatives are $\partial_r g_{\theta\theta} = -2r$, $\partial_r g_{\varphi\varphi} = -2r\sin^2\theta$, $\partial_\theta g_{\varphi\varphi} = -2r^2\sin\theta\cos\theta$, so the entire computation is driven by these three.

---

# Legal Operations Used

1. **Compute Christoffel symbols from the metric** (operation 2 from the topic page). Invert $g$, then evaluate $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\mu}(\partial_\alpha g_{\mu\beta}+\partial_\beta g_{\alpha\mu}-\partial_\mu g_{\alpha\beta})$, using diagonality and lower-index symmetry.

---

# Hints

> [!note]- Hint 1
> For a diagonal metric, $g^{\alpha\alpha} = 1/g_{\alpha\alpha}$ (no sum). So $g^{(ct)(ct)} = 1$, $g^{rr} = -1$, $g^{\theta\theta} = -1/r^2$, $g^{\varphi\varphi} = -1/(r^2\sin^2\theta)$.

> [!note]- Hint 2
> Because $g^{\gamma\mu}$ is diagonal, only $\mu = \gamma$ survives: $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\gamma}(\partial_\alpha g_{\gamma\beta}+\partial_\beta g_{\alpha\gamma}-\partial_\gamma g_{\alpha\beta})$ (no sum on $\gamma$). The only nonzero metric derivatives are $\partial_r g_{\theta\theta}$, $\partial_r g_{\varphi\varphi}$, $\partial_\theta g_{\varphi\varphi}$.

> [!note]- Hint 3
> To get $\Gamma^r{}_{\theta\theta}$ take $\gamma=r$, $\alpha=\beta=\theta$: $\Gamma^r{}_{\theta\theta} = \tfrac12 g^{rr}(\partial_\theta g_{r\theta}+\partial_\theta g_{\theta r}-\partial_r g_{\theta\theta}) = \tfrac12(-1)(0+0-(-2r)) = \tfrac12(-1)(2r) = -r$.

> [!note]- Hint 4
> $\Gamma^\theta{}_{r\theta}$ has $\gamma=\theta$, $\{\alpha,\beta\}=\{r,\theta\}$: $\Gamma^\theta{}_{r\theta} = \tfrac12 g^{\theta\theta}(\partial_r g_{\theta\theta}+\partial_\theta g_{r\theta}-\partial_\theta g_{r\theta}) = \tfrac12(-1/r^2)(\partial_r(-r^2)) = \tfrac12(-1/r^2)(-2r) = 1/r$. Note both factors carry a sign and they cancel — this is the signature-independence.

---

# Solution

The plan: invert the diagonal metric (Step 1), then drive the whole computation from the three nonzero metric derivatives, getting each Christoffel by setting $\mu=\gamma$ and reading off which index pattern survives (Step 2), and finally check the list and the sign-independence (Step 3).

**Step 1: The inverse metric.**

> [!note]- Derivation
> The metric is diagonal, so the inverse is the reciprocal of each diagonal entry:
> $$g^{\alpha\beta} = \mathrm{diag}\!\left(1,\,-1,\,-\frac{1}{r^2},\,-\frac{1}{r^2\sin^2\theta}\right).$$
> The only nonzero partial derivatives of the metric components are
> $$\partial_r g_{\theta\theta} = \partial_r(-r^2) = -2r, \qquad \partial_r g_{\varphi\varphi} = \partial_r(-r^2\sin^2\theta) = -2r\sin^2\theta, \qquad \partial_\theta g_{\varphi\varphi} = \partial_\theta(-r^2\sin^2\theta) = -2r^2\sin\theta\cos\theta.$$
> Everything else is constant, so any Christoffel symbol whose formula does not involve one of these three derivatives vanishes.

**Step 2: The nonzero Christoffel symbols.**

> [!note]- Derivation
> Diagonality forces $\mu=\gamma$ in $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\gamma}(\partial_\alpha g_{\gamma\beta}+\partial_\beta g_{\alpha\gamma}-\partial_\gamma g_{\alpha\beta})$ (no sum on $\gamma$). Take each surviving derivative in turn.
>
> *From $\partial_r g_{\theta\theta} = -2r$:*
> $$\Gamma^r{}_{\theta\theta} = \tfrac12 g^{rr}\,(-\partial_r g_{\theta\theta}) = \tfrac12(-1)(2r) = -r,$$
> $$\Gamma^\theta{}_{r\theta} = \Gamma^\theta{}_{\theta r} = \tfrac12 g^{\theta\theta}\,(\partial_r g_{\theta\theta}) = \tfrac12\Big(-\tfrac{1}{r^2}\Big)(-2r) = \tfrac1r.$$
>
> *From $\partial_r g_{\varphi\varphi} = -2r\sin^2\theta$:*
> $$\Gamma^r{}_{\varphi\varphi} = \tfrac12 g^{rr}\,(-\partial_r g_{\varphi\varphi}) = \tfrac12(-1)(2r\sin^2\theta) = -r\sin^2\theta,$$
> $$\Gamma^\varphi{}_{r\varphi} = \Gamma^\varphi{}_{\varphi r} = \tfrac12 g^{\varphi\varphi}\,(\partial_r g_{\varphi\varphi}) = \tfrac12\Big(-\tfrac{1}{r^2\sin^2\theta}\Big)(-2r\sin^2\theta) = \tfrac1r.$$
>
> *From $\partial_\theta g_{\varphi\varphi} = -2r^2\sin\theta\cos\theta$:*
> $$\Gamma^\theta{}_{\varphi\varphi} = \tfrac12 g^{\theta\theta}\,(-\partial_\theta g_{\varphi\varphi}) = \tfrac12\Big(-\tfrac{1}{r^2}\Big)(2r^2\sin\theta\cos\theta) = -\sin\theta\cos\theta,$$
> $$\Gamma^\varphi{}_{\theta\varphi} = \Gamma^\varphi{}_{\varphi\theta} = \tfrac12 g^{\varphi\varphi}\,(\partial_\theta g_{\varphi\varphi}) = \tfrac12\Big(-\tfrac{1}{r^2\sin^2\theta}\Big)(-2r^2\sin\theta\cos\theta) = \frac{\cos\theta}{\sin\theta} = \cot\theta.$$
> All other Christoffel symbols are zero.

**Step 3: Check, time-independence, and sign-independence.**

> [!note]- Derivation
> The six symbols (each with its symmetric partner) match the stated list exactly:
> $$\Gamma^r{}_{\theta\theta}=-r,\quad \Gamma^r{}_{\varphi\varphi}=-r\sin^2\theta,\quad \Gamma^\theta{}_{r\theta}=\tfrac1r,\quad \Gamma^\theta{}_{\varphi\varphi}=-\sin\theta\cos\theta,\quad \Gamma^\varphi{}_{r\varphi}=\tfrac1r,\quad \Gamma^\varphi{}_{\theta\varphi}=\cot\theta.$$
> *No time Christoffels.* Every nonzero symbol carries only spatial indices $r,\theta,\varphi$. This is because $g_{(ct)(ct)} = 1$ is constant and the metric has no time–space cross terms, so $\partial g$ never produces a time index. The time direction is "flat" in these coordinates, exactly as in three-dimensional Euclidean spherical geometry — indeed these are precisely the Christoffel symbols of Euclidean $\mathbb{R}^3$ in spherical coordinates.
>
> *Sign-independence.* In each computation the factor $g^{\gamma\gamma}$ (upper, carrying one sign flip between signatures) multiplies a derivative $\partial g_{\cdots}$ (lower, carrying the opposite flip), so the two signs cancel and the Christoffel symbol is the *same* in mostly-minus and mostly-plus. For instance $\Gamma^\theta{}_{r\theta} = \tfrac12 g^{\theta\theta}\partial_r g_{\theta\theta}$: in mostly-plus $g^{\theta\theta} = +1/r^2$ and $\partial_r g_{\theta\theta} = +2r$, giving the same $1/r$. This confirms the claim that the Christoffel formula is signature-independent.

> [!note]- Complete formal solution
> With $g_{\alpha\beta} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$ the inverse is $g^{\alpha\beta} = \mathrm{diag}(1,-1,-r^{-2},-(r^2\sin^2\theta)^{-1})$, and the only nonzero metric derivatives are $\partial_r g_{\theta\theta}=-2r$, $\partial_r g_{\varphi\varphi}=-2r\sin^2\theta$, $\partial_\theta g_{\varphi\varphi}=-2r^2\sin\theta\cos\theta$. Diagonality sets $\mu=\gamma$ in $\Gamma^\gamma{}_{\alpha\beta}=\tfrac12 g^{\gamma\gamma}(\partial_\alpha g_{\gamma\beta}+\partial_\beta g_{\alpha\gamma}-\partial_\gamma g_{\alpha\beta})$, yielding $\Gamma^r{}_{\theta\theta}=-r$, $\Gamma^r{}_{\varphi\varphi}=-r\sin^2\theta$, $\Gamma^\theta{}_{r\theta}=1/r$, $\Gamma^\theta{}_{\varphi\varphi}=-\sin\theta\cos\theta$, $\Gamma^\varphi{}_{r\varphi}=1/r$, $\Gamma^\varphi{}_{\theta\varphi}=\cot\theta$ (with symmetric partners), all others zero. No symbol carries a time index because $g_{(ct)(ct)}$ is constant; the result is signature-independent because $g^{\gamma\gamma}$ and $\partial g_{\gamma\gamma}$ flip sign together. $\blacksquare$

---

# Key Takeaways

**Diagonality collapses the Christoffel formula to a one-term sum, and a handful of metric derivatives drive everything.** The general formula sums over $\mu$, but for a diagonal metric $g^{\gamma\mu}$ has only the $\mu=\gamma$ entry, so $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\gamma}(\partial_\alpha g_{\gamma\beta}+\partial_\beta g_{\alpha\gamma}-\partial_\gamma g_{\alpha\beta})$ with no sum. Then the only Christoffels that can be nonzero are those whose three derivative terms include one of the few non-constant metric components — here just $g_{\theta\theta}$ and $g_{\varphi\varphi}$. The practical workflow is therefore: list the nonzero $\partial g$, and for each, read off which $\Gamma$ it feeds. This turns a forbidding $4^3 = 64$-component object into a six-line computation, and the same discipline (diagonal metric, identify non-constant components, read off the surviving symbols) handles cylindrical coordinates, the Schwarzschild metric, and most metrics one meets in practice.

**The spherical Christoffel symbols are purely spatial and identical to those of Euclidean $\mathbb{R}^3$ — the time direction is flat in these coordinates.** Because $g_{(ct)(ct)} = 1$ is constant and there are no time–space cross terms, no Christoffel symbol carries a time index, and the surviving symbols ($\Gamma^r{}_{\theta\theta} = -r$, $\Gamma^\theta{}_{r\theta} = 1/r$, $\cot\theta$, and the rest) are exactly the connection coefficients of three-dimensional Euclidean space in spherical coordinates. This is the precise sense in which special-relativistic spherical coordinates "add nothing new" to the spatial geometry you already know from vector calculus — the relativistic content is entirely in the (here trivial) time part. The transferable lesson is that whenever a metric block is constant and decoupled, it contributes no Christoffel symbols, so you can often reduce a spacetime computation to a lower-dimensional spatial one you have done before.

**The Christoffel formula is signature-independent because the up-index inverse metric and the down-index components flip oppositely.** Each Christoffel symbol is one factor of $g^{\gamma\mu}$ (upper) against derivatives of $g_{\cdots}$ (lower), and under a global sign flip of the metric the inverse picks up one sign while the components pick up the opposite, so the product is unchanged. This is why Gourgoulhon's mostly-plus arrays yield the *same* Christoffel symbols as the mostly-minus arrays used here, and why one never has to re-derive connections when switching conventions. Recognising which quantities are signature-dependent (the metric components themselves, the norm of a vector) and which are signature-independent (the Christoffel symbols, the geodesic equation, and as it happens $\sqrt{-\det g}$ in four dimensions) is part of the discipline of translating between sources, and this exercise makes the cancellation concrete on a specific symbol.
