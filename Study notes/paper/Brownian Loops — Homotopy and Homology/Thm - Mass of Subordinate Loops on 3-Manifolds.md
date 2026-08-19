---
type: theorem
subject: probability-geometry
prereqs:
  - "Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length"
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Subordinate Brownian Loop Measure"
  - "Def - Weighted Potential Measure"
  - "Thm - Homotopy Decomposition for 3-Manifolds"
  - "Lemma - Hyperbolic 3-Space Strip Integral"
  - "Lemma - Collapsing the Time Integral of the Subordinate Kernel"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 7.2"
---

# Notation

- $\mathbb{H}^3 = \{(z, y) : z \in \mathbb{C},\, y > 0\}$ — hyperbolic 3-space (upper half-space model), metric $ds^2 = (|dz|^2 + dy^2)/y^2$, volume $d\!\operatorname{vol}_{\mathbb{H}^3} = y^{-3}\,dA(z)\,dy$.
- $\Gamma \subset \mathrm{PSL}(2, \mathbb{C})$ — a geometrically finite Kleinian group; $X = \Gamma\backslash\mathbb{H}^3$ a hyperbolic 3-manifold.
- $\gamma \in \mathcal{P}_X$ — primitive closed geodesic, complex length $L_\gamma = \ell_\gamma + i\theta_\gamma$; $\tau \in \Gamma$ its loxodromic representative in standard form $\tau(z, y) = (e^{L_\gamma} z, e^{\ell_\gamma} y)$; $\mathcal{F}_\tau = \{(z, y) : 1 \le y < e^{\ell_\gamma}\}$ the fundamental slab.
- $m \in \mathbb{Z}_{\ge 1}$; $L := m L_\gamma = m\ell_\gamma + i m \theta_\gamma$ — complex length of the $m$-th iterate $\tau^m(z, y) = (e^L z, e^{m\ell_\gamma} y)$.
- $\phi : (0, \infty) \to (0, \infty)$ — a **Bernstein function** (concave, non-decreasing, with completely-monotone derivative); its subordinator $(S_t)_{t \ge 0}$ is a non-decreasing càdlàg process with Laplace transform $\mathbb{E}[e^{-\lambda S_t}] = e^{-t \phi(\lambda)}$; law of $S_t$ is $\psi^\phi_t$, a probability measure on $[0, \infty)$.
- $p_{\mathbb{H}^3}(t, z, w) = (4\pi t)^{-3/2} \frac{u}{\sinh u}\,e^{-t - u^2/(4t)}$ — the Brownian heat kernel on $\mathbb{H}^3$, $u = d(z, w)$.
- $p^\phi_{\mathbb{H}^3}(t, z, w) := \int_{[0, \infty)} p_{\mathbb{H}^3}(s, z, w)\,\psi^\phi_t(ds)$ — the subordinate kernel.
- $\mu^\phi_X$ — the subordinate Brownian loop measure on $X$: loop measure of $Y = B \circ S$ where $B$ is Brownian motion on $\mathbb{H}^3$ and $S$ is a $\phi$-subordinator.
- $C_X(\gamma^m)$ — free homotopy class of loops winding $m$ times around $\gamma$; $\mu^\phi_X(C_X(\gamma^m))$ its subordinate loop-measure mass.
- $V_\phi$ — the **weighted potential measure** on $(0, \infty)$: $V_\phi(ds) = \int_0^\infty \psi^\phi_t(ds)\,\frac{dt}{t}$.

> [!recall]- Hyperbolic 3-space $\mathbb{H}^3$
> **Formally:** $\mathbb{H}^3 := \{(z, y) : z \in \mathbb{C},\, y > 0\}$ with metric $ds^2 = (|dz|^2 + dy^2)/y^2$ and volume $d\!\operatorname{vol}_{\mathbb{H}^3} = y^{-3}\,dA(z)\,dy$; isometry group $\mathrm{PSL}(2, \mathbb{C})$.
> **In words:** the 3D analogue of the upper half-plane — complex horizontal coordinate $z$, positive height $y$, ruler shrinking as height grows.
> **Concretely:** vertical geodesic from $(0, 1)$ to $(0, 2)$ has hyperbolic length $\log 2$; a Euclidean $\varepsilon$-box at height $y$ has hyperbolic volume $\varepsilon^3/y^3$. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

> [!recall]- Kleinian group $\Gamma$ and hyperbolic 3-manifold $X = \Gamma\backslash\mathbb{H}^3$
> **Formally:** $\Gamma \subset \mathrm{PSL}(2, \mathbb{C})$ discrete and torsion-free; $X = \Gamma\backslash\mathbb{H}^3$ the quotient hyperbolic 3-manifold.
> **In words:** 3D analogue of a Fuchsian group and its quotient surface. Fold $\mathbb{H}^3$ by a discrete symmetry group to get a 3-manifold with the same local geometry as $\mathbb{H}^3$ but non-trivial global topology (handles, cusps, knot complements).
> **Concretely:** the figure-eight knot complement $S^3 \setminus K_8$ is a finite-volume hyperbolic 3-manifold; simpler Euclidean analogue is $\mathbb{R}^3/\mathbb{Z}^3$ (the flat 3-torus).

> [!recall]- Loxodromic $\tau$, complex length $L_\gamma = \ell_\gamma + i\theta_\gamma$, iterate $\tau^m$
> **Formally:** $\tau \in \mathrm{PSL}(2, \mathbb{C})$ non-parabolic, non-elliptic, with standard form $\tau(z, y) = (e^{L_\gamma} z, e^{\ell_\gamma} y)$; its axis is the vertical geodesic $\{(0, y) : y > 0\}$. The $m$-th iterate $\tau^m$ has standard form $(z, y) \mapsto (e^{mL_\gamma} z, e^{m\ell_\gamma} y)$ and complex length $L = m L_\gamma = m\ell_\gamma + i m\theta_\gamma$.
> **In words:** a "screw motion" that slides everything along its axis by hyperbolic distance $\ell_\gamma$ and simultaneously rotates around the axis by angle $\theta_\gamma$; iterating $m$ times slides $m\ell_\gamma$ and rotates $m\theta_\gamma$. The complex number $L_\gamma$ bundles slide and twist into one bookkeeping symbol.
> **Concretely:** $\tau(z, y) = (2 i z, 2 y)$: $\ell_\gamma = \log 2$, $\theta_\gamma = \pi/2$; then $\tau^2(z, y) = (-4 z, 4 y)$ ($L = 2\log 2 + i\pi$, i.e. rotate $180°$ and double twice). At $m\theta_\gamma$ equal to a multiple of $2\pi$ the rotation becomes trivial modulo $2\pi$. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

> [!recall]- The $\mathbb{H}^3$ heat kernel $p_{\mathbb{H}^3}(t, z, w)$
> **Formally:** $p_{\mathbb{H}^3}(t, z, w) = (4\pi t)^{-3/2}\,\frac{u}{\sinh u}\,e^{-t - u^2/(4t)}$ where $u = d(z, w)$ is the hyperbolic distance; this is the fundamental solution of $\partial_t f = \frac12 \Delta_{\mathbb{H}^3} f$.
> **In words:** the probability density of a 3D hyperbolic Brownian particle being near $w$ at time $t$ given it started at $z$. Equals the flat-3D Gaussian $(4\pi t)^{-3/2} e^{-u^2/(4t)}$ times two curvature corrections: $u/\sinh u$ (suppresses long paths because negative curvature spreads paths thin) and $e^{-t}$ (uniform exponential decay, reflecting that hyperbolic Brownian motion escapes to infinity).
> **Concretely:** at $u = 1$, $t = 1$: $p_{\mathbb{H}^3} \approx 0.0141$ vs. flat-space $0.0350$; the $u/\sinh u$ and $e^{-t}$ factors suppress by about $60\%$. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

> [!recall]- Bernstein function $\phi$, subordinator $(S_t)$, subordinate process $Y = B \circ S$
> **Formally:** $\phi : (0, \infty) \to (0, \infty)$ is a **Bernstein function** if it is $C^\infty$, concave, non-decreasing, with completely monotone derivative $\phi'$. Its **subordinator** is a non-decreasing càdlàg Lévy process $(S_t)_{t \ge 0}$ with Laplace transform $\mathbb{E}[e^{-\lambda S_t}] = e^{-t \phi(\lambda)}$; write $\psi^\phi_t$ for the law of $S_t$ (a probability measure on $[0, \infty)$). The **subordinate process** $Y_t = B_{S_t}$ (Brownian motion time-changed by $S$) has transition kernel $p^\phi(t, z, w) = \int_{[0, \infty)} p(s, z, w)\,\psi^\phi_t(ds)$.
> **In words:** a subordinator is a "random clock" that runs forward but in jumps rather than continuously. Composing a Brownian motion with a subordinator gives a *jump* process — the composition covers Brownian paths with pieces skipped over — whose density at time $t$ is the Brownian density averaged over how far the random clock has advanced.
> **Concretely:** $\phi(\lambda) = \lambda$: subordinator is the identity $S_t = t$, subordinate process is ordinary Brownian motion, $p^\phi = p$. $\phi(\lambda) = \lambda + \kappa$: $S_t = t$ but the process is killed at rate $\kappa$; $p^\phi = e^{-\kappa t} p$. $\phi(\lambda) = \lambda^{\alpha/2}$ ($0 < \alpha < 2$): $S_t$ is an $\alpha/2$-stable subordinator, subordinate process is the (rotationally invariant) $\alpha$-stable Lévy process. See [[Def - Bernstein Function, Subordinator, and Subordination]] and [[Def - Subordinate Brownian Loop Measure]].

> [!recall]- Weighted potential measure $V_\phi$
> **Formally:** $V_\phi$ is the Borel measure on $(0, \infty)$ defined by $V_\phi(ds) := \int_0^\infty \psi^\phi_t(ds)\,\frac{dt}{t}$: for each Borel $A \subseteq (0, \infty)$, $V_\phi(A) = \int_0^\infty \mathbb{P}(S_t \in A)\,\frac{dt}{t}$.
> **In words:** $V_\phi$ packages all $\phi$-dependence in a single measure on the "subordination-variable axis" $s \in (0, \infty)$. It is a $dt/t$-average of the laws of the subordinator, and once you have it, the class-mass formula reduces to a single integral against $V_\phi$ (no $t$-integral left).
> **Concretely:** Brownian $\phi(\lambda) = \lambda$: $S_t = t$ deterministically, so $\psi^\phi_t = \delta_t$ and $V_\phi(A) = \int_0^\infty \mathbf{1}_{t \in A}\,\frac{dt}{t} = \int_A ds/s$ — $V_\phi(ds) = ds/s$. Killed $\phi(\lambda) = \lambda + \kappa$: $\psi^\phi_t = e^{-\kappa t}\delta_t$ (defective), $V_\phi(ds) = e^{-\kappa s}\,ds/s$. See [[Def - Weighted Potential Measure]].

> [!recall]- Fundamental slab $\mathcal{F}_\tau = \{(z, y) : 1 \le y < e^{\ell_\gamma}\}$
> **Formally:** for $\tau(z, y) = (e^{L_\gamma} z, e^{\ell_\gamma} y)$, the slab $\mathcal{F}_\tau$ is a fundamental region for $\langle\tau\rangle$: each $\langle\tau\rangle$-orbit meets it exactly once.
> **In words:** one full period of the height-scaling action of $\tau$ — the 3D analogue of the fundamental strip in the surface theory.
> **Concretely:** with $\ell_\gamma = \log 2$ the slab is the layer $\{1 \le y < 2\}$; the point $(1 + i, 3)$ has $\tau^{-1}(1 + i, 3) = (e^{-L_\gamma}(1+i), 3/2)$ in the slab.

> [!recall]- From earlier sections — [[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]]
> **Formally:** $\mu^E_X(C_X(\gamma^m)) = \int_0^\infty \frac{dt}{t} \int_{\mathcal{F}_\tau} p^E_{\mathbb{H}^3}(t, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w)$ for any $\Gamma$-invariant Dirichlet-form kernel $p^E_{\mathbb{H}^3}$ on $\mathbb{H}^3$.
> **In words:** the mass of a free homotopy class on the 3-manifold equals a single upstairs-kernel integral from a point to its $\tau^m$-image, integrated over one geodesic period (the slab) and over time with weight $dt/t$. The 3D analogue of Theorem 3.2.
> **Concretely:** when the Dirichlet form is Brownian motion, $p^E = p_{\mathbb{H}^3}$ (the explicit heat kernel above); when it is the subordinate variant $p^\phi_{\mathbb{H}^3}$, the same formula holds with $p^E$ replaced by $p^\phi_{\mathbb{H}^3}$. See [[Thm - Homotopy Decomposition for 3-Manifolds]].

> [!recall]- From earlier sections — $\mathbb{H}^3$ strip integral ([[Lemma - Hyperbolic 3-Space Strip Integral]])
> **Formally:** $\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) = 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4t)}$, derived directly from the explicit heat kernel by polar coordinates on the horizontal $\mathbb{C}$-plane and the change of variables $r = |z| \to u = d(w, \tau^m w)$ that cancels the $1/\sinh u$ in $p_{\mathbb{H}^3}$.
> **In words:** the space integral of the $\mathbb{H}^3$ heat kernel from a point to its $\tau^m$-image over one slab is completely explicit — a 1-D Gaussian in $\sqrt{t}$ with a purely-geometric prefactor built from the complex length.
> **Concretely:** at $\theta_\gamma = 0$, $|e^L - 1|^2 = (e^{m\ell_\gamma} - 1)^2$ and the identity reduces to $\int_{\mathcal{F}_\tau} = 2\pi\,\frac{e^{m\ell_\gamma}\ell_\gamma}{(e^{m\ell_\gamma} - 1)^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4t)}$. See [[Lemma - Hyperbolic 3-Space Strip Integral]].

> [!recall]- From earlier sections — [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]
> **Formally:** for any $\phi$-subordinator with laws $(\psi^\phi_t)$ and any Borel measurable $h : (0, \infty) \to [0, \infty]$, $\int_0^\infty \frac{dt}{t} \int_{[0, \infty)} h(s)\,\psi^\phi_t(ds) = \int_{(0, \infty)} h(s)\,V_\phi(ds)$.
> **In words:** the two-parameter integral against $(t, s)$ with weight $dt/t$ reduces to a single integral against $V_\phi$: the weighted potential measure absorbs the $t$-integral. This is what turns "$\int_0^\infty \frac{dt}{t} \int p_{\mathbb{H}^3}(s, \cdot)\psi^\phi_t(ds)$" into "$\int p_{\mathbb{H}^3}(s, \cdot)\,V_\phi(ds)$".
> **Concretely:** with Brownian $\phi(\lambda) = \lambda$, $V_\phi(ds) = ds/s$, so the identity reads $\int_0^\infty h(t)\,dt/t = \int_0^\infty h(s)\,ds/s$ — tautological. For killed $\phi(\lambda) = \lambda + \kappa$: $V_\phi(ds) = e^{-\kappa s}\,ds/s$ and the identity reads $\int_0^\infty \frac{dt}{t}\,e^{-\kappa t} h(t) = \int_0^\infty h(s)\,e^{-\kappa s}\,ds/s$. See [[Lemma - Collapsing the Time Integral of the Subordinate Kernel]].

---

# Statement

> **Theorem (subordinate mass, 3-manifolds; Belyaev–Huseynli 7.2).** Let $X = \Gamma\backslash\mathbb{H}^3$ be a geometrically finite hyperbolic 3-manifold, $\gamma \in \mathcal{P}_X$ a primitive closed geodesic (complex length $L_\gamma = \ell_\gamma + i\theta_\gamma$), $\tau$ its loxodromic representative in standard form, $m \ge 1$ (so $L := m L_\gamma$). Let $\phi$ be a Bernstein function of the paper (non-compound-Poisson) and $\mu^\phi_X$ the corresponding subordinate Brownian loop measure on $X$. Then
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\int_{(0, \infty)} \frac{2 s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4 s)}\,V_\phi(ds).$$

---

# In One Line

The subordinate loop-measure mass of the class $C_X(\gamma^m)$ on a 3-manifold is a single 1-D integral in the subordination variable $s$: [[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]] evaluated via the closed-form $\mathbb{H}^3$ strip integral ([[Lemma - Hyperbolic 3-Space Strip Integral]]) and [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]. The complex length enters through the denominator $|e^L - 1|^2 = 2 e^{m\ell_\gamma}(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))$.

---

# Why It's True

**Mechanism (one sentence).** *Theorem 7.1 gives the slab-integral formula for $\mu^\phi_X$ (using $p^E = p^\phi_{\mathbb{H}^3}$); expanding the subordinate kernel as an $s$-mixture of Brownian kernels, evaluating the $s$-integrated slab integral in closed form via the $\mathbb{H}^3$ strip integral, and collapsing the $t$-integral against $V_\phi$ using Lemma 2.11, produces the explicit formula.*

The subordinate kernel is $p^\phi_{\mathbb{H}^3}(t, z, w) = \int_{[0, \infty)} p_{\mathbb{H}^3}(s, z, w)\,\psi^\phi_t(ds)$ (the Brownian kernel averaged over the random clock's law at time $t$). Substituting this into Theorem 7.1's slab-integral formula gives a triple integral in $(t, s, w)$; the spatial integral in $w$ is exactly the strip integral, which is completely explicit; the resulting integrand is a product $h(s)$ depending only on $s$, whose $t$-averaging against $\psi^\phi_t$ and $dt/t$ collapses to a single integral against $V_\phi$ by Lemma 2.11. Nothing about the argument is 3D-specific except the specific closed form of the strip integral.

**The role of the complex length.** In 2D the mass depended on the length $\ell_\gamma$ alone; in 3D the closed-form prefactor $\frac{e^{m\ell_\gamma}}{|e^L - 1|^2}$ absorbs both the translation and the twist. When $\theta_\gamma = 0$ (no twist), $|e^L - 1|^2 = (e^{m\ell_\gamma} - 1)^2$, so the prefactor becomes the *square* of the surface counterpart — the extra factor is the geometric "cross-section" of the geodesic in the extra dimension. When $\theta_\gamma \ne 0$, $|e^L - 1|^2$ also carries the $\cos(m\theta_\gamma)$ dependence, so the mass drops on resonances $m\theta_\gamma \approx 0 \pmod{2\pi}$ where the horizontal rotation nearly closes up.

---

# Proof

> [!note]- Gap-free proof
> **Step 1 — apply Theorem 7.1 to the subordinate Dirichlet-form kernel.** The subordinate process $Y = B \circ S$ on $\mathbb{H}^3$ is a symmetric Markov process whose Dirichlet form is $\Gamma$-invariant (subordination commutes with symmetry). Its transition kernel on $\mathbb{H}^3$ is
> $$p^\phi_{\mathbb{H}^3}(t, z, w) \;=\; \int_{[0, \infty)} p_{\mathbb{H}^3}(s, z, w)\,\psi^\phi_t(ds), \tag{$\ast$}$$
> the Brownian kernel averaged over the law of $S_t$. Applying [[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]] with $p^E := p^\phi_{\mathbb{H}^3}$,
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; \int_0^\infty \frac{dt}{t} \int_{\mathcal{F}_\tau} p^\phi_{\mathbb{H}^3}(t, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w). \tag{$\dagger$}$$
>
> **Step 2 — swap the $s$- and $w$-integrals; apply the $\mathbb{H}^3$ strip integral.** Substitute $(\ast)$ into ($\dagger$). By Tonelli (the integrand is non-negative), swap the $s$-integral against $\psi^\phi_t$ with the spatial integral over $\mathcal{F}_\tau$:
> $$\int_{\mathcal{F}_\tau} p^\phi_{\mathbb{H}^3}(t, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) \;=\; \int_{[0, \infty)} \left[\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(s, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w)\right]\psi^\phi_t(ds).$$
> The inner strip integral is the $\mathbb{H}^3$ strip integral ([[Lemma - Hyperbolic 3-Space Strip Integral]]) at time $s$:
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(s, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\cdot\frac{2 s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4 s)}. \tag{$\ddagger$}$$
> Substituting $(\ddagger)$ back and pulling the $w$-independent prefactor out of the $s$-integral,
> $$\int_{\mathcal{F}_\tau} p^\phi_{\mathbb{H}^3}(t, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\int_{[0, \infty)} h(s)\,\psi^\phi_t(ds),$$
> where
> $$h(s) \;:=\; \frac{2 s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4 s)}. \tag{$\S$}$$
>
> **Step 3 — collapse the $t$-integral against $V_\phi$ via Lemma 2.11.** Substituting into ($\dagger$),
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\int_0^\infty \frac{dt}{t} \int_{[0, \infty)} h(s)\,\psi^\phi_t(ds).$$
> Apply [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] with the non-negative function $h$: $\int_0^\infty \frac{dt}{t} \int h(s)\,\psi^\phi_t(ds) = \int h(s)\,V_\phi(ds)$. Therefore
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\int_{(0, \infty)} \frac{2 s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4 s)}\,V_\phi(ds). \qquad \blacksquare$$

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7.2]] as the closed-form 3-manifold analogue of [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] (which used Wang–Xue's Lemma 3.4); here the strip integral is derived in-house rather than cited. Specialised in [[Cor - Brownian Mass on 3-Manifolds|Corollary 7.3]] to pure Brownian motion ($V_\phi(ds) = ds/s$), giving the explicit Le Jan mass $\frac{1}{m}\frac{1}{|e^{mL_\gamma} - 1|^2}$.
