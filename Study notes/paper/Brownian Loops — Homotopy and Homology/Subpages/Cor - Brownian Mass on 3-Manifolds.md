---
type: corollary
subject: probability-geometry
prereqs:
  - "Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length"
  - "Def - Brownian Loop Measure"
  - "Def - Weighted Potential Measure"
  - "Thm - Mass of Subordinate Loops on 3-Manifolds"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 7.3"
---

# Notation

- $\mathbb{H}^3 = \{(z, y) : z \in \mathbb{C},\, y > 0\}$ — hyperbolic 3-space (upper half-space model), metric $ds^2 = (|dz|^2 + dy^2)/y^2$.
- $\Gamma \subset \mathrm{PSL}(2, \mathbb{C})$ — geometrically finite Kleinian group; $X = \Gamma\backslash\mathbb{H}^3$ — a hyperbolic 3-manifold.
- $\gamma \in \mathcal{P}_X$ — a primitive closed geodesic; $L_\gamma = \ell_\gamma + i\theta_\gamma \in \mathbb{C}$ its **complex length** ($\ell_\gamma > 0$ translation, $\theta_\gamma \in \mathbb{R}/2\pi\mathbb{Z}$ holonomy).
- $\tau \in \Gamma$ — its loxodromic representative in standard form $\tau(z, y) = (e^{L_\gamma} z,\, e^{\ell_\gamma} y)$.
- $m \in \mathbb{Z}_{\ge 1}$; $L := m L_\gamma$; $C_X(\gamma^m)$ the free homotopy class of loops winding $m$ times around $\gamma$.
- $\mu_X$ — the (pure) **Brownian loop measure** on $X$: the special case of $\mu^\phi_X$ with Bernstein function $\phi(\lambda) = \lambda$, i.e. the loop measure of ordinary Brownian motion on $X$.

> [!recall]- Hyperbolic 3-space $\mathbb{H}^3$
> **Formally:** $\mathbb{H}^3 := \{(z, y) : z \in \mathbb{C},\, y > 0\}$ with metric $ds^2 = (|dz|^2 + dy^2)/y^2$ and volume form $y^{-3}\,dA(z)\,dy$; isometry group $\mathrm{PSL}(2, \mathbb{C})$.
> **In words:** the 3-dimensional analogue of the upper half-plane, with a complex horizontal coordinate $z$ and a positive vertical coordinate $y$; ruler shrinks as height grows, giving constant negative curvature.
> **Concretely:** vertical geodesic from $(0, 1)$ to $(0, 2)$ has length $\log 2$; hyperbolic volume of a Euclidean $\varepsilon$-box at height $y$ is $\varepsilon^3/y^3$. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

> [!recall]- Kleinian group and 3-manifold $X = \Gamma\backslash\mathbb{H}^3$
> **Formally:** $\Gamma \subset \mathrm{PSL}(2, \mathbb{C})$ discrete, torsion-free, geometrically finite; $X = \Gamma\backslash\mathbb{H}^3$ inherits a smooth hyperbolic metric of constant curvature $-1$.
> **In words:** the 3D analogue of a Fuchsian group and its quotient surface — fold $\mathbb{H}^3$ by a discrete symmetry group to make a hyperbolic 3-manifold (which may have handles, cusps, or knotted structure).
> **Concretely:** the figure-eight knot complement is a hyperbolic 3-manifold of finite volume $\approx 2.03$; the flat 3-torus $\mathbb{R}^3/\mathbb{Z}^3$ is the Euclidean analogue.

> [!recall]- Loxodromic $\tau$, complex length $L_\gamma = \ell_\gamma + i\theta_\gamma$
> **Formally:** $\tau \in \mathrm{PSL}(2, \mathbb{C})$ non-parabolic non-elliptic, standard form $\tau(z, y) = (e^{L_\gamma} z,\, e^{\ell_\gamma} y)$: translates along its axis by $\ell_\gamma$ and rotates around it by $\theta_\gamma$. The iterate $\tau^m$ has complex length $m L_\gamma = m\ell_\gamma + i m\theta_\gamma$.
> **In words:** a screw motion — slide along a fixed line by $\ell_\gamma$ and simultaneously twist around it by $\theta_\gamma$; the complex length bundles slide and twist.
> **Concretely:** $\tau(z, y) = (2 i z, 2 y)$: $\ell_\gamma = \log 2$, $\theta_\gamma = \pi/2$; iterating four times ($m = 4$) gives $\tau^4(z, y) = (16 z, 16 y)$ (twist returns to identity: $4\theta_\gamma = 2\pi$).

> [!recall]- Brownian loop measure $\mu_X$ and $V_\phi = ds/s$
> **Formally:** the **Brownian loop measure** $\mu_X$ on $X$ is the Le Jan loop measure of ordinary Brownian motion on $X$ — the special case $\phi(\lambda) = \lambda$ of $\mu^\phi_X$. Concretely $\mu_X(A) = \int_0^\infty \frac{dt}{t}\int_X \mathbb{W}^t_{z\to z, X}(A)\,d\!\operatorname{vol}_X(z)$ with $\mathbb{W}^t_{z\to z, X}$ the Brownian bridge measure. The subordinator is trivial ($S_t = t$), so $\psi^\phi_t = \delta_t$ and the **weighted potential measure** is $V_\phi(ds) = ds/s$.
> **In words:** the Brownian loop measure is the archetype loop measure — it counts Brownian loops on $X$ with the scale-invariant weight $dt/t$. When you specialise the subordinate framework to $\phi(\lambda) = \lambda$, the subordinator is the identity clock (no jumps, no killing), and the "weighted potential measure" reduces to the simple measure $ds/s$ on the positive reals.
> **Concretely:** for $\phi(\lambda) = \lambda$ the identity $\mathbb{E}[e^{-\lambda S_t}] = e^{-t\phi(\lambda)}$ reads $\mathbb{E}[e^{-\lambda t}] = e^{-\lambda t}$, so $S_t = t$ almost surely; $V_\phi(A) = \int_0^\infty \psi^\phi_t(A)\,dt/t = \int_0^\infty \mathbf{1}_{t \in A}\,dt/t = \int_A ds/s$. See [[Def - Brownian Loop Measure]] and [[Def - Weighted Potential Measure]].

> [!recall]- From earlier sections — [[Thm - Mass of Subordinate Loops on 3-Manifolds|Theorem 7.2]]
> **Formally:** for a Bernstein $\phi$ and the subordinate loop measure $\mu^\phi_X$, $\mu^\phi_X(C_X(\gamma^m)) = 2\pi\,\frac{e^{m\ell_\gamma}\ell_\gamma}{|e^L - 1|^2}\int_{(0, \infty)} \frac{2 s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4 s)}\,V_\phi(ds)$ where $L = m L_\gamma$.
> **In words:** the mass of any subordinate loop class on the 3-manifold is a single 1-D integral in the subordination variable $s$ against $V_\phi$; the geometry enters through the prefactor $e^{m\ell_\gamma}/|e^L - 1|^2$ and the Gaussian $e^{-(m\ell_\gamma)^2/(4s)}$. Specialising $\phi$ to Brownian ($V_\phi(ds) = ds/s$) will give the pure-Brownian class-mass in closed form.
> **Concretely:** at $\theta_\gamma = 0$ (no twist), $|e^L - 1|^2 = (e^{m\ell_\gamma} - 1)^2$ and the prefactor is $e^{m\ell_\gamma}/(e^{m\ell_\gamma} - 1)^2$. See [[Thm - Mass of Subordinate Loops on 3-Manifolds]].

> [!recall]- The Gaussian-type integral $\int_0^\infty s^{-3/2} e^{-a s - b/s}\,ds$
> **Formally:** for $a, b > 0$, $\int_0^\infty s^{-3/2} e^{-a s - b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{a b}}$. Derived by completing the square: set $u = \sqrt{a s} - \sqrt{b/s}$, then $a s + b/s = u^2 + 2\sqrt{a b}$ and $du = \frac12(\sqrt{a/s} + \sqrt{b}/s^{3/2})\,ds$; the integrand rearranges to $\sqrt{\pi/b}\,e^{-2\sqrt{a b}}$ times the standard Gaussian in $u$ integrated over $\mathbb{R}$.
> **In words:** a standard modified-Bessel-related identity that turns a "small-$s$ Gaussian in $1/\sqrt{s}$ against a large-$s$ decay $e^{-a s}$" into an exponential in the geometric mean $\sqrt{a b}$.
> **Concretely:** at $a = 1$, $b = 1$: $\int_0^\infty s^{-3/2}e^{-s - 1/s}\,ds = \sqrt{\pi}\,e^{-2}$. Full proof: given in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.1]].

---

# Statement

> **Corollary (Brownian mass, 3-manifolds; Belyaev–Huseynli 7.3).** Let $X = \Gamma\backslash\mathbb{H}^3$ be a geometrically finite hyperbolic 3-manifold, $\gamma \in \mathcal{P}_X$ a primitive closed geodesic (complex length $L_\gamma = \ell_\gamma + i\theta_\gamma$), and $m \ge 1$. Then the Brownian loop-measure mass of the class $C_X(\gamma^m)$ is
> $$\mu_X\big(C_X(\gamma^m)\big) \;=\; \frac{1}{m}\cdot\frac{1}{|e^{m L_\gamma} - 1|^2} \;=\; \frac{e^{-m\ell_\gamma}}{2 m\,(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))} \;=\; \frac{1}{m}\Big[(e^{m\ell_\gamma} - 1)^2 + 4 e^{m\ell_\gamma}\sin^2\frac{m\theta_\gamma}{2}\Big]^{-1}.$$

---

# In One Line

The exact 3-manifold analogue of the surface formula $\mu_X(C_X(\gamma^m)) = \frac{1}{m}\frac{1}{e^{m\ell_\gamma} - 1}$: replace $e^{m\ell_\gamma} - 1$ by $|e^{m L_\gamma} - 1|^2 = 2 e^{m\ell_\gamma}(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))$ — the *square* absorbs the extra transverse dimension, and $\cos(m\theta_\gamma)$ registers the horizontal twist. When $\theta_\gamma = 0$ (no twist), the mass collapses to $\frac{1}{m(e^{m\ell_\gamma} - 1)^2}$, the square of the surface answer.

---

# Why It's True

**Mechanism (one sentence).** *Theorem 7.2 with $V_\phi(ds) = ds/s$ gives a 1-D integral $\int_0^\infty s^{-3/2} e^{-s - (m\ell_\gamma)^2/(4 s)}\,ds$ that evaluates via the standard identity $\int_0^\infty s^{-3/2} e^{-a s - b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{a b}}$; the constants align so that the answer is $\frac{1}{m}\frac{1}{|e^{m L_\gamma} - 1|^2}$.*

**The role of the two equivalent forms.** Writing the answer three ways is not decoration — each form is the "natural" one from a different viewpoint. The compact form $\frac{1}{m|e^{m L_\gamma} - 1|^2}$ is the direct analogue of the surface formula, with $|e^{m L_\gamma} - 1|^2$ playing the role that $|e^{m\ell_\gamma} - 1|^2 = (e^{m\ell_\gamma} - 1)^2$ plays in 2D. The $\cosh - \cos$ form exposes the structure as a difference of two hyperbolic/trigonometric quantities and makes the $\theta_\gamma \to 0$ limit transparent. The $\sin^2$ form makes the *positivity* of the denominator manifest (both $(e^{m\ell_\gamma} - 1)^2 \ge 0$ and $\sin^2 \ge 0$) and shows that the "correction" for the twist is a strictly positive additive term — the twist strictly *decreases* the mass.

**Why the mass is smaller than the surface mass.** The surface formula gives mass of order $e^{-m\ell_\gamma}/m$ for large $m\ell_\gamma$; the 3-manifold formula gives $e^{-2 m\ell_\gamma}/m$. The extra factor of $e^{-m\ell_\gamma}$ is the geometric shrinkage of the "cross-section" of the geodesic in the extra transverse dimension — as you unwind the 3-manifold analogue of the fundamental strip into a slab, the horizontal $\mathbb{C}$-cross-section adds another dimension of area to sweep out.

---

# Proof

> [!note]- Gap-free proof
> **Step 1 — specialise Theorem 7.2 to Brownian motion.** For $\phi(\lambda) = \lambda$, $V_\phi(ds) = ds/s$ (see the recall above). [[Thm - Mass of Subordinate Loops on 3-Manifolds|Theorem 7.2]] becomes
> $$\mu_X(C_X(\gamma^m)) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\int_0^\infty \frac{2 s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4 s)}\,\frac{ds}{s}. \tag{$\dagger$}$$
> Simplify the integrand: $\frac{2 s\,e^{-s}}{(4\pi s)^{3/2}}\cdot\frac{1}{s} = \frac{2\,e^{-s}}{(4\pi)^{3/2} s^{3/2}}$. So
> $$\mu_X(C_X(\gamma^m)) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\cdot\frac{2}{(4\pi)^{3/2}}\int_0^\infty s^{-3/2}\,e^{-s - (m\ell_\gamma)^2/(4 s)}\,ds. \tag{$\ddagger$}$$
>
> **Step 2 — evaluate the Gaussian-type integral.** Apply the identity $\int_0^\infty s^{-3/2} e^{-a s - b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{a b}}$ (recall above) with $a = 1$, $b = (m\ell_\gamma)^2/4$:
> $$\sqrt{\pi/b} \;=\; \sqrt{\pi \cdot \frac{4}{(m\ell_\gamma)^2}} \;=\; \frac{2\sqrt{\pi}}{m\ell_\gamma}, \qquad 2\sqrt{a b} \;=\; 2\sqrt{\frac{(m\ell_\gamma)^2}{4}} \;=\; m\ell_\gamma,$$
> so
> $$\int_0^\infty s^{-3/2}\,e^{-s - (m\ell_\gamma)^2/(4 s)}\,ds \;=\; \frac{2\sqrt{\pi}}{m\ell_\gamma}\,e^{-m\ell_\gamma}. \tag{$\S$}$$
>
> **Step 3 — combine and simplify the constant.** Substituting $(\S)$ into $(\ddagger)$,
> $$\mu_X(C_X(\gamma^m)) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\cdot\frac{2}{(4\pi)^{3/2}}\cdot\frac{2\sqrt{\pi}}{m\ell_\gamma}\,e^{-m\ell_\gamma} \;=\; \frac{1}{m}\cdot\frac{e^{m\ell_\gamma}\,e^{-m\ell_\gamma}}{|e^L - 1|^2}\cdot\underbrace{\frac{2\pi \cdot 2 \cdot 2\sqrt{\pi}}{(4\pi)^{3/2}}}_{\text{constant}}.$$
> Compute the constant: $(4\pi)^{3/2} = 4^{3/2}\pi^{3/2} = 8\pi^{3/2} = 8\pi\sqrt{\pi}$, and $2\pi \cdot 2 \cdot 2\sqrt{\pi} = 8\pi\sqrt{\pi}$. So the constant is $8\pi\sqrt{\pi}/8\pi\sqrt{\pi} = 1$. The $\ell_\gamma$ in the prefactor and the $m\ell_\gamma$ in the denominator combine to give $1/m$; the exponentials cancel: $e^{m\ell_\gamma}\cdot e^{-m\ell_\gamma} = 1$. Therefore
> $$\mu_X(C_X(\gamma^m)) \;=\; \frac{1}{m}\cdot\frac{1}{|e^L - 1|^2} \;=\; \frac{1}{m}\cdot\frac{1}{|e^{m L_\gamma} - 1|^2}. \tag{form 1}$$
>
> **Step 4 — derive the equivalent forms.** Apply the auxiliary identity $|e^{a + ib} - 1|^2 = 2 e^a(\cosh a - \cos b)$ (derived by direct computation: $|e^{a+ib} - 1|^2 = (e^a\cos b - 1)^2 + (e^a\sin b)^2 = e^{2a} - 2 e^a\cos b + 1 = 2 e^a\big(\frac{e^a + e^{-a}}{2} - \cos b\big)$) with $a = m\ell_\gamma$, $b = m\theta_\gamma$:
> $$|e^{m L_\gamma} - 1|^2 \;=\; 2 e^{m\ell_\gamma}\big(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma)\big).$$
> Substituting in form 1,
> $$\mu_X(C_X(\gamma^m)) \;=\; \frac{1}{m}\cdot\frac{1}{2 e^{m\ell_\gamma}(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))} \;=\; \frac{e^{-m\ell_\gamma}}{2 m(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))}. \tag{form 2}$$
>
> For form 3, apply the double-angle identity $\cos(m\theta_\gamma) = 1 - 2\sin^2(m\theta_\gamma/2)$ and expand $\cosh(m\ell_\gamma) = \frac{e^{m\ell_\gamma} + e^{-m\ell_\gamma}}{2}$:
> $$2 e^{m\ell_\gamma}(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma)) \;=\; 2 e^{m\ell_\gamma}\cdot\frac{e^{m\ell_\gamma} + e^{-m\ell_\gamma}}{2} - 2 e^{m\ell_\gamma} + 4 e^{m\ell_\gamma}\sin^2(m\theta_\gamma/2).$$
> The first two terms give $e^{2m\ell_\gamma} + 1 - 2 e^{m\ell_\gamma} = (e^{m\ell_\gamma} - 1)^2$. Therefore $|e^{m L_\gamma} - 1|^2 = (e^{m\ell_\gamma} - 1)^2 + 4 e^{m\ell_\gamma}\sin^2(m\theta_\gamma/2)$, giving
> $$\mu_X(C_X(\gamma^m)) \;=\; \frac{1}{m}\Big[(e^{m\ell_\gamma} - 1)^2 + 4 e^{m\ell_\gamma}\sin^2\frac{m\theta_\gamma}{2}\Big]^{-1}. \qquad \tag{form 3} \blacksquare$$
>
> **Cross-check ($\theta_\gamma = 0$).** With no twist, $\sin(m\theta_\gamma/2) = 0$ and $\cos(m\theta_\gamma) = 1$, so form 2 reads $\frac{e^{-m\ell_\gamma}}{2m(\cosh(m\ell_\gamma) - 1)}$, and using $\cosh a - 1 = 2\sinh^2(a/2)$: $\frac{e^{-m\ell_\gamma}}{4m\sinh^2(m\ell_\gamma/2)}$. Since $2\sinh(a/2) = e^{a/2}(1 - e^{-a})$, $4\sinh^2(m\ell_\gamma/2) = e^{m\ell_\gamma}(1 - e^{-m\ell_\gamma})^2 = e^{-m\ell_\gamma}(e^{m\ell_\gamma} - 1)^2$; so form 2 simplifies to $\frac{1}{m(e^{m\ell_\gamma} - 1)^2}$ — indeed the square of the surface mass $\frac{1}{m(e^{m\ell_\gamma} - 1)}$, as anticipated.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7.2]] as the closed-form 3-manifold analogue of the surface Brownian mass $\frac{1}{m(e^{m\ell_\gamma} - 1)}$. Closes the paper: the same random-loop weights that on a surface gave the Le Jan / Wang–Xue closed form now, on a 3-manifold, produce the same shape packaged by the complex length. The paper remarks that §4–§6's zeta/probability apparatus carries over to 3-manifolds with $\ell_\gamma \to L_\gamma$ and $\sinh^2 \to |e^L - 1|^2$, though this extension is not developed there — flagged as a pointer for future work in [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7]].
