---
type: lemma
subject: probability-geometry
prereqs:
  - "Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length"
  - "Def - Heat Kernel and Heat Semigroup"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §7.2 strip-integral derivation"
---

# Notation

- $\mathbb{H}^3 = \{(z, y) : z \in \mathbb{C},\, y > 0\}$ — hyperbolic 3-space (upper half-space model) with Riemannian metric $ds^2 = (|dz|^2 + dy^2)/y^2$ and volume form $d\!\operatorname{vol}_{\mathbb{H}^3} = y^{-3}\,dA(z)\,dy$, where $dA$ is Euclidean area on $\mathbb{C}$.
- $u = d(\cdot, \cdot)$ — hyperbolic distance between two points of $\mathbb{H}^3$.
- $p_{\mathbb{H}^3}(t, z, w) = \dfrac{1}{(4\pi t)^{3/2}}\,\dfrac{u}{\sinh u}\,e^{-t - u^2/(4t)}$ — the (Brownian) heat kernel on $\mathbb{H}^3$; depends on $z, w$ only through $u = d(z, w)$.
- $\tau : \mathbb{H}^3 \to \mathbb{H}^3$, $\tau(z, y) = (e^{L_\gamma} z,\, e^{\ell_\gamma} y)$ — a loxodromic isometry in standard form, with **complex length** $L_\gamma = \ell_\gamma + i\theta_\gamma \in \mathbb{C}$ (real part $\ell_\gamma > 0$ the translation length, imaginary part $\theta_\gamma \in \mathbb{R}/2\pi\mathbb{Z}$ the holonomy angle around the vertical axis).
- $m \in \mathbb{Z}_{\ge 1}$; $L := m L_\gamma = m\ell_\gamma + i m\theta_\gamma$ — complex length of the $m$-th iterate $\tau^m : (z, y) \mapsto (e^L z,\, e^{m\ell_\gamma} y)$.
- $\mathcal{F}_\tau = \{(z, y) \in \mathbb{H}^3 : 1 \le y < e^{\ell_\gamma}\}$ — **fundamental slab** of the cyclic group $\langle\tau\rangle$: each $\langle\tau\rangle$-orbit meets it exactly once (because $\tau$ scales $y$ by the real factor $e^{\ell_\gamma}$).

> [!recall]- Hyperbolic 3-space $\mathbb{H}^3$ (upper half-space model)
> **Formally:** $\mathbb{H}^3 := \{(z, y) : z \in \mathbb{C},\, y > 0\}$ carries the Riemannian metric $ds^2 = (|dz|^2 + dy^2)/y^2$ and volume form $d\!\operatorname{vol}_{\mathbb{H}^3} = y^{-3}\,dA(z)\,dy$ ($dA$ Euclidean 2-D area on $\mathbb{C}$); its isometry group is $\mathrm{PSL}(2, \mathbb{C})$. Hyperbolic distance $u = d((z_1, y_1), (z_2, y_2))$ satisfies $\cosh u = 1 + \frac{|z_1 - z_2|^2 + (y_1 - y_2)^2}{2 y_1 y_2}$.
> **In words:** the 3-dimensional analogue of the upper half-plane you know from the surface theory. Points are labelled by a complex "horizontal" coordinate $z$ and a positive "height" $y$; the same set of numbers as ordinary 3D upper half-space but with a rescaled ruler that shrinks Euclidean distances as height grows, giving constant negative curvature. Volumes shrink as $1/y^3$ (three metric-factors of $1/y$ multiplied together).
> **Concretely:** the vertical geodesic from $(0, 1)$ to $(0, 2)$ has hyperbolic length $\int_1^2 dy/y = \log 2$. A Euclidean-tiny 3D ball of side $\varepsilon$ centred at height $y$ has Euclidean volume $\varepsilon^3$ but *hyperbolic* volume $\varepsilon^3/y^3$: the higher you are, the smaller you look, in exact mirror of the 2D $\mathbb{H}^2$ picture. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

> [!recall]- Loxodromic isometry and complex length $L_\gamma = \ell_\gamma + i\theta_\gamma$
> **Formally:** an isometry $\tau \in \mathrm{PSL}(2, \mathbb{C})$ is **loxodromic** if, after conjugation in $\mathrm{PSL}(2, \mathbb{C})$, it takes the *standard form* $\tau(z, y) = (e^{L_\gamma} z,\, e^{\ell_\gamma} y)$ for some $L_\gamma = \ell_\gamma + i\theta_\gamma \in \mathbb{C}$ with $\ell_\gamma > 0$. Its **axis** is the vertical geodesic $\{(0, y) : y > 0\}$, invariant under $\tau$; along it $\tau$ acts by pure translation of length $\ell_\gamma$. Off the axis the action combines translation up the axis by $\ell_\gamma$ with rotation by the angle $\theta_\gamma$ about the axis. The pair $(\ell_\gamma, \theta_\gamma)$ is packaged as the single complex number $L_\gamma$, the **complex length**.
> **In words:** think of $\tau$ as a screw motion: it slides everything up along a fixed line ("axis") by a fixed hyperbolic distance $\ell_\gamma$ *and* twists everything around that line by a fixed angle $\theta_\gamma$. The complex number $L_\gamma$ bundles the slide and the twist so that "$e^{L_\gamma}$" acts on the horizontal $\mathbb{C}$-plane at each height as multiplication by a complex number of modulus $e^{\ell_\gamma}$ and argument $\theta_\gamma$ — i.e. simultaneous scaling and rotation. The 3D generalisation of the 2D hyperbolic $\tau(z) = e^{\ell_\gamma} z$ that only translated.
> **Concretely:** with $\ell_\gamma = \log 2$ and $\theta_\gamma = \pi/2$, $\tau(z, y) = (2 i z,\, 2y)$: the point $(1, 1)$ maps to $(2i, 2)$, then to $(2 i \cdot 2i, 4) = (-4, 4)$, then to $(2 i \cdot -4, 8) = (-8 i, 8)$ — height doubling each step and the horizontal coordinate rotating $90°$ per step while its modulus doubles. The point $(0, 1)$ on the axis maps to $(0, 2)$, then $(0, 4)$: pure translation. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

> [!recall]- The $\mathbb{H}^3$ heat kernel $p_{\mathbb{H}^3}(t, z, w)$
> **Formally:** the fundamental solution of $\partial_t u = \tfrac12 \Delta_{\mathbb{H}^3} u$ (Brownian motion generator) on $\mathbb{H}^3$ is the function $p_{\mathbb{H}^3} : (0, \infty) \times \mathbb{H}^3 \times \mathbb{H}^3 \to (0, \infty)$ given by the closed form $p_{\mathbb{H}^3}(t, z, w) = \dfrac{1}{(4\pi t)^{3/2}}\,\dfrac{u}{\sinh u}\,e^{-t - u^2/(4t)}$ where $u = d(z, w)$. It depends on $z, w$ only through the distance $u$, and it integrates to $1$ in either argument. The $e^{-t}$ factor is the spectral shift $e^{-(\frac{n-1}{2})^2 t}$ specialised to $n = 3$ (bottom of the $L^2$ spectrum of $-\tfrac12\Delta_{\mathbb{H}^3}$ is $1$).
> **In words:** the probability density that a Brownian particle started at $z$ is found near $w$ at time $t$. In flat 3D space this would be the Gaussian $(4\pi t)^{-3/2}\,e^{-u^2/4t}$; on $\mathbb{H}^3$ that Gaussian is multiplied by two curvature corrections — $u/\sinh u$ (which suppresses the density at large distances because negative curvature "spreads paths thin") and $e^{-t}$ (a uniform-in-space exponential decay reflecting the fact that a Brownian particle on $\mathbb{H}^3$ escapes to infinity almost surely).
> **Concretely:** at $t = 1$, $u = 1$: $p_{\mathbb{H}^3}(1, z, w) = (4\pi)^{-3/2}\,(1/\sinh 1)\,e^{-1 - 1/4} \approx 0.0141$, versus the *flat*-space value $(4\pi)^{-3/2}\,e^{-1/4} \approx 0.0350$. At $t = 1$, $u \to 0$: the curvature corrections $u/\sinh u \to 1$ and $e^{-u^2/4t} \to 1$, so $p_{\mathbb{H}^3}(1, z, z) = (4\pi)^{-3/2}\,e^{-1} \approx 0.0165$ — the on-diagonal value is *smaller* than flat by exactly the spectral-shift factor $e^{-1}$. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]] and [[Def - Heat Kernel and Heat Semigroup]].

> [!recall]- Fundamental slab $\mathcal{F}_\tau$ for $\langle\tau\rangle$
> **Formally:** for the loxodromic $\tau(z, y) = (e^{L_\gamma} z,\, e^{\ell_\gamma} y)$, the cyclic group $\langle\tau\rangle = \{\tau^k : k \in \mathbb{Z}\}$ acts on $\mathbb{H}^3$ with orbits $\{(e^{k L_\gamma} z,\, e^{k \ell_\gamma} y) : k \in \mathbb{Z}\}$. Because $y$ scales by the real factor $e^{\ell_\gamma}$, each orbit meets the *slab* $\mathcal{F}_\tau := \{(z, y) \in \mathbb{H}^3 : 1 \le y < e^{\ell_\gamma}\}$ exactly once (the horizontal rotation $\theta_\gamma$ is intrinsic to a given height and does not affect which slab you land in). So $\mathcal{F}_\tau$ is a fundamental region for $\langle\tau\rangle$.
> **In words:** slice $\mathbb{H}^3$ into horizontal layers indexed by height $y$; $\tau$ multiplies $y$ by the real number $e^{\ell_\gamma}$ (and separately rotates the horizontal $\mathbb{C}$-coordinate), so one full "period" of $\tau$ carries a point from height $y$ to height $e^{\ell_\gamma} y$. The slab $\mathcal{F}_\tau$ is one full period — every $\langle\tau\rangle$-orbit crosses it exactly once. Quotienting $\mathbb{H}^3$ by $\langle\tau\rangle$ glues the top face $y = e^{\ell_\gamma}$ to the bottom face $y = 1$ by the map $(z, e^{\ell_\gamma}) \mapsto (e^{-L_\gamma} z, 1)$, producing a 3D "solid torus with a twist".
> **Concretely:** with $\ell_\gamma = \log 2$, $\theta_\gamma = 0$, the slab is $\{(z, y) : 1 \le y < 2\}$ — an infinite horizontal 3D layer between heights $1$ and $2$. The point $(1 + i, 1)$ is in the slab; the point $(2 + 2i, 4)$ is not, and its representative is $\tau^{-2}(2 + 2i, 4) = ((2 + 2i)/4,\, 1) = ((1 + i)/2,\, 1)$, which lies in the slab. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

---

# Statement

> **Lemma ($\mathbb{H}^3$ strip integral; unnumbered in the paper, derived in §7.2).** Let $\tau : \mathbb{H}^3 \to \mathbb{H}^3$ be a loxodromic isometry in standard form with complex length $L_\gamma = \ell_\gamma + i\theta_\gamma$, and let $m \ge 1$ with $L := m L_\gamma$. Then for every $t > 0$,
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t,\, w,\, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^{L} - 1|^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4t)}.$$
> Equivalently, using $|e^{a + ib} - 1|^2 = 2 e^a (\cosh a - \cos b)$ and $2\pi \cdot \tfrac{2t}{(4\pi t)^{3/2}} = \tfrac{1}{\sqrt{4\pi t}}$,
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t,\, w,\, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) \;=\; \frac{\ell_\gamma}{2\,(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))}\cdot\frac{e^{-t - (m\ell_\gamma)^2/(4t)}}{\sqrt{4\pi t}}.$$

---

# In One Line

The hyperbolic-3-space analogue of Wang–Xue's 2D strip integral: the space-integral of the heat kernel from a point to its $\tau^m$-image over one $\langle\tau\rangle$-period is a completely explicit 1-D Gaussian in $\sqrt{t}$ with a purely-geometric prefactor built from the complex length. Because the $\mathbb{H}^3$ heat kernel has closed form (unlike the $\mathbb{H}^2$ one, which needs a Selberg-transform integral), the identity is *derived* directly instead of imported.

---

# Why It's True

**Mechanism (one sentence).** *In standard form the distance $u = d(w, \tau^m w)$ depends on the horizontal coordinate $z$ only through its modulus $|z| = r$; the polar $\varphi$-integral yields $2\pi$; the substitution $r \to u$ cancels the $1/\sinh u$ factor in $p_{\mathbb{H}^3}$; and what remains is a one-dimensional Gaussian $\int_{m\ell_\gamma}^\infty u\, e^{-u^2/(4t)}\,du$ that integrates in closed form.*

Three ingredients make this work. First, **the distance depends only on $|z|$**: in the standard form $\tau^m(z, y) = (e^L z, e^{m\ell_\gamma} y)$, hyperbolic distance from $(z, y)$ to $(e^L z, e^{m\ell_\gamma} y)$ is a function of $|z|$ (through $|e^L - 1|^2 |z|^2$) and $y$ only — the angular coordinate $\varphi = \arg z$ drops out because a rigid rotation of the horizontal plane about the axis is a hyperbolic isometry. Second, **the $y$-integral is elementary**: the volume form contains $y^{-3}$, the substitution $r \to u$ pulls out a factor $y^2$, and $\int_1^{e^{\ell_\gamma}} y^{-1}\,dy = \ell_\gamma$ — one period of the log ruler is exactly the translation length. Third, **the $u$-integral is Gaussian**: the $u/\sinh u$ factor in $p_{\mathbb{H}^3}$ is exactly what the change of variables $r \to u$ needs to cancel, leaving $u\,e^{-u^2/(4t)}$ whose primitive is $-2t\,e^{-u^2/(4t)}$.

The 2D analogue (Wang–Xue's Lemma 3.4) uses the same three ingredients but with Fermi coordinates on the strip and the $\mathbb{H}^2$ heat kernel expressed as a Selberg-type integral. In 3D the heat kernel is elementary, so the whole derivation is elementary.

---

# Proof

> [!note]- Gap-free proof
> **Step 1 — distance from $w$ to $\tau^m w$.** Write $w = (z, y)$. Then $\tau^m w = (e^L z,\, e^{m\ell_\gamma} y)$. The hyperbolic distance $u = d(w, \tau^m w)$ satisfies
> $$\cosh u \;=\; 1 + \frac{|z - e^L z|^2 + (y - e^{m\ell_\gamma} y)^2}{2\, y \cdot e^{m\ell_\gamma} y} \;=\; 1 + \frac{|e^L - 1|^2\,|z|^2 + (1 - e^{m\ell_\gamma})^2\,y^2}{2\,e^{m\ell_\gamma}\,y^2}$$
> (using the standard distance formula in the upper half-space model, applied to the two points $(z, y)$ and $(e^L z, e^{m\ell_\gamma} y)$). Split the numerator's two terms:
> $$\cosh u \;=\; \underbrace{1 + \frac{(1 - e^{m\ell_\gamma})^2}{2\,e^{m\ell_\gamma}}}_{= \cosh(m\ell_\gamma)} \;+\; \frac{|e^L - 1|^2\,|z|^2}{2\,e^{m\ell_\gamma}\,y^2}.$$
> The identity $1 + \frac{(1 - e^a)^2}{2 e^a} = \cosh a$ is elementary: expand $(1 - e^a)^2 = 1 - 2 e^a + e^{2a}$ so the fraction is $\frac{1 - 2 e^a + e^{2a}}{2 e^a} = \frac{e^{-a} - 2 + e^a}{2} = \cosh a - 1$; add $1$ to get $\cosh a$. Applied with $a = m\ell_\gamma$ this gives the first term. The auxiliary identity $|e^{a + ib} - 1|^2 = 2 e^a (\cosh a - \cos b)$ (used below) is proved by direct computation: $|e^{a + ib} - 1|^2 = (e^a \cos b - 1)^2 + (e^a \sin b)^2 = e^{2a} - 2 e^a \cos b + 1 = 2 e^a (\tfrac{e^a + e^{-a}}{2} - \cos b)$.
>
> The upshot: writing $r := |z|$, at fixed $y$ the distance $u$ depends on the horizontal coordinate $z$ only through $r$, and satisfies
> $$\cosh u \;=\; \cosh(m\ell_\gamma) \;+\; \frac{|e^L - 1|^2\,r^2}{2\,e^{m\ell_\gamma}\,y^2}. \tag{$\ast$}$$
>
> **Step 2 — set up the spatial integral in polar coordinates.** The volume form on $\mathbb{H}^3$ in coordinates $(z, y)$ with $z = x + i\eta \in \mathbb{C}$ is $d\!\operatorname{vol}_{\mathbb{H}^3} = y^{-3}\,dA(z)\,dy = y^{-3}\,dx\,d\eta\,dy$. Introduce polar coordinates $z = r e^{i\varphi}$ ($r \ge 0$, $\varphi \in [0, 2\pi)$) so $dA(z) = r\,dr\,d\varphi$. Since the integrand $p_{\mathbb{H}^3}(t, w, \tau^m w) = p_{\mathbb{H}^3}(t, u)$ depends on $w$ only through $u$, and by $(\ast)$ $u$ depends on the horizontal only through $r$, the $\varphi$-integral is trivial and yields $\int_0^{2\pi} d\varphi = 2\pi$:
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) \;=\; 2\pi \int_1^{e^{\ell_\gamma}}\!\!\int_0^\infty p_{\mathbb{H}^3}(t, u(r, y))\,r\,dr\,\frac{dy}{y^3}. \tag{$\dagger$}$$
>
> **Step 3 — change of variables $r \to u$ at fixed $y$.** Differentiate $(\ast)$ in $r$ at fixed $y$: since $\cosh u$'s derivative in $u$ is $\sinh u$,
> $$\sinh u\,\frac{du}{dr} \;=\; \frac{|e^L - 1|^2\, r}{e^{m\ell_\gamma}\,y^2} \qquad \Longrightarrow \qquad r\,dr \;=\; \frac{e^{m\ell_\gamma}\,y^2}{|e^L - 1|^2}\,\sinh u\,du.$$
> As $r$ ranges over $[0, \infty)$, $\cosh u$ ranges over $[\cosh(m\ell_\gamma), \infty)$ by $(\ast)$, so $u$ ranges over $[m\ell_\gamma, \infty)$ (since $u \ge 0$ and $\cosh$ is monotonic on $[0, \infty)$). Substitute in $(\dagger)$ using the explicit heat kernel $p_{\mathbb{H}^3}(t, u) = \frac{1}{(4\pi t)^{3/2}} \frac{u}{\sinh u}\,e^{-t - u^2/(4t)}$:
> $$\int_0^\infty p_{\mathbb{H}^3}(t, u(r, y))\,r\,dr \;=\; \int_{m\ell_\gamma}^\infty \frac{1}{(4\pi t)^{3/2}}\,\frac{u}{\sinh u}\,e^{-t - u^2/(4t)} \cdot \frac{e^{m\ell_\gamma}\,y^2}{|e^L - 1|^2}\,\sinh u\,du.$$
> The $\sinh u$ factors cancel exactly — this is why the $\mathbb{H}^3$ derivation is clean:
> $$\int_0^\infty p_{\mathbb{H}^3}(t, u(r, y))\,r\,dr \;=\; \frac{e^{m\ell_\gamma}\,y^2}{|e^L - 1|^2}\cdot\frac{e^{-t}}{(4\pi t)^{3/2}}\int_{m\ell_\gamma}^\infty u\,e^{-u^2/(4t)}\,du.$$
>
> **Step 4 — evaluate the elementary $u$-Gaussian.** For $a \ge 0$ and $t > 0$,
> $$\int_a^\infty u\,e^{-u^2/(4t)}\,du \;=\; \Big[-2t\,e^{-u^2/(4t)}\Big]_a^\infty \;=\; 2t\,e^{-a^2/(4t)},$$
> since $u\,e^{-u^2/(4t)} = -\frac{d}{du}[2t\,e^{-u^2/(4t)}]$. Apply with $a = m\ell_\gamma$:
> $$\int_{m\ell_\gamma}^\infty u\,e^{-u^2/(4t)}\,du \;=\; 2t\,e^{-(m\ell_\gamma)^2/(4t)}.$$
> Substituting back,
> $$\int_0^\infty p_{\mathbb{H}^3}(t, u(r, y))\,r\,dr \;=\; \frac{e^{m\ell_\gamma}\,y^2}{|e^L - 1|^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4t)}. \tag{$\ddagger$}$$
>
> **Step 5 — do the $y$-integral.** The factor $y^2$ in $(\ddagger)$ meets the $y^{-3}$ in $(\dagger)$ leaving $y^{-1}$; and $\int_1^{e^{\ell_\gamma}} y^{-1}\,dy = \log(e^{\ell_\gamma}) - \log 1 = \ell_\gamma$. So $(\dagger)$ becomes
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) \;=\; 2\pi\,\frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4t)}. \tag{first form}$$
> This is the first form claimed.
>
> **Step 6 — simplify to the second form.** The auxiliary identity $|e^{L} - 1|^2 = 2 e^{m\ell_\gamma}(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))$ (proved in Step 1) gives $\frac{e^{m\ell_\gamma}}{|e^L - 1|^2} = \frac{1}{2(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))}$; and the constant $2\pi \cdot \frac{2t}{(4\pi t)^{3/2}}$ simplifies as
> $$2\pi \cdot \frac{2t}{(4\pi t)^{3/2}} \;=\; \frac{4\pi t}{(4\pi t)^{3/2}} \;=\; \frac{1}{(4\pi t)^{1/2}} \;=\; \frac{1}{\sqrt{4\pi t}}.$$
> Therefore
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t, w, \tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w) \;=\; \frac{\ell_\gamma}{2(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))}\cdot\frac{e^{-t - (m\ell_\gamma)^2/(4t)}}{\sqrt{4\pi t}}. \tag{second form} \qquad \blacksquare$$

---

# Where the paper uses this

This is the $\mathbb{H}^3$ analogue of the Wang–Xue strip integral (Lemma 3.4 in the surface case) — but where the paper **cites** Wang–Xue in §3, in §7.2 it **derives** this identity itself, because the $\mathbb{H}^3$ heat kernel has closed form. The identity is the key computational step turning [[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]]'s abstract slab integral into a completely explicit 1-D integral. It is used immediately to prove [[Thm - Mass of Subordinate Loops on 3-Manifolds|Theorem 7.2]] (substitute at subordination time $s$ and apply [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]) and, downstream, [[Cor - Brownian Mass on 3-Manifolds|Corollary 7.3]] (the specialisation to pure Brownian motion). Full ambient context: [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7.2]].

---

# Verified against

The distance formula $\cosh u = 1 + \frac{|z_1 - z_2|^2 + (y_1 - y_2)^2}{2 y_1 y_2}$ for the upper half-space model is standard (Ratcliffe, *Foundations of Hyperbolic Manifolds*, §4.6). The $\mathbb{H}^3$ heat kernel formula is that of Elstrodt–Grunewald–Mennicke, *Groups Acting on Hyperbolic Space* (Ch. 6). The auxiliary identities $1 + \frac{(1 - e^a)^2}{2 e^a} = \cosh a$ and $|e^{a + ib} - 1|^2 = 2 e^a (\cosh a - \cos b)$ are elementary and verified by direct computation. The Gaussian $\int_a^\infty u\,e^{-u^2/(4t)}\,du = 2t\,e^{-a^2/(4t)}$ is a standard antiderivative. Matches the paper's §7.2 derivation eqs. (88)–(89).
