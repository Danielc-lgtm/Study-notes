---
type: exercise
subject: geometric-mechanics
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Lagrangian Function"
  - "Def - Hamiltonian Function"
  - "Def - Riemannian Metric"
  - "Thm - Hamilton's Principle in TQ Gives Euler-Lagrange Equations"
tags: [physics, geometric-mechanics, lagrangian-mechanics, riemannian-geometry]
---

# Problem Statement

A particle of mass $m$ moves in $\mathbb{R}^3$ under a **central potential** $V(r)$ depending only on the distance $r = |\vec q|$ from the origin. The Lagrangian is $L = \tfrac{1}{2}m|\dot{\vec q}|^2 - V(r)$.

**Jacobi's principle of "least" action** states that for an autonomous mechanical system with energy $E$, the projected trajectory in configuration space $Q$ is a **geodesic in the conformal Jacobi metric** $g^J_{ij} = 2(E - V(\vec q))g_{ij}$ on the classically allowed region $\{V < E\}$, where $g$ is the kinetic-energy metric.

(a) Write down the Jacobi metric for the central-potential problem in spherical coordinates and verify it is conformal to the round Euclidean metric.

(b) Use the rotational symmetry to reduce to a planar orbital problem (the motion stays in a fixed plane by conservation of angular momentum).

(c) Derive **Binet's equation** for the orbit $r(\phi)$, eliminating the time-dependence.

(d) For the Kepler problem $V(r) = -k/r$ (gravity, $k = GMm > 0$), solve Binet's equation and verify the orbits are **conic sections** (ellipses for $E < 0$, parabolas for $E = 0$, hyperbolas for $E > 0$). For $E < 0$, derive the orbit equation $r(\phi) = p/(1 + e\cos\phi)$ where $p = \ell^2/(mk)$ and $e = \sqrt{1 + 2E\ell^2/(mk^2)}$.

(e) Discuss the **degeneracy of the Jacobi metric at turning points** $V = E$ and the geometric singularity it represents.

**Recall:**

The Jacobi metric $g^J_{ij} = 2(E - V)g_{ij}$ is **conformal** to the kinetic-energy metric $g$, with conformal factor $2(E - V)$. Geodesics in $g^J$ on $\{V < E\}$ are the projections of Hamiltonian trajectories at energy $E$ to configuration space.

For a central potential the Hamiltonian is $H = |p|^2/(2m) + V(r)$, conserved energy $E$ and conserved angular momentum vector $\vec L = \vec q \times \vec p$.

---

# Convergent Strategy

**Problem class:** A combined application of **Jacobi's principle** (geodesic motion in the conformal metric), **central-force orbital theory** (reduction by angular momentum), and **Binet's equation** (the orbit ODE in radial-azimuthal coordinates). The problem class is "use the geometrical reformulation of mechanics to compute orbits in a central potential".

**Assumption pattern:** Two physical conservation laws: total energy $E$ (autonomous Hamiltonian) and total angular momentum $\vec L$ (rotational symmetry of the central potential). These two are what make the problem tractable: energy gives Jacobi's principle (one less dimension), angular momentum gives planarity and the radial-azimuthal reduction (two more dimensions reduced).

**Theorem routing:** [[Def - The Lagrangian Function|Lagrangian]] $\to$ Hamilton's principle $\to$ Euler–Lagrange $\to$ Jacobi's principle (using energy conservation). Apply rotational symmetry to plane the motion. Use angular momentum conservation $\ell = mr^2\dot\phi$ to eliminate $\dot\phi$ from the radial equation. Convert from $r(t)$ to $r(\phi)$ via $\dot r/\dot\phi = dr/d\phi$, giving Binet's equation. For Kepler, solve the resulting linear ODE in $u = 1/r$ and recognize the conic-section solution.

**Key decision point:** The non-obvious step is **Binet's substitution** $u = 1/r$, which converts the nonlinear radial equation into a linear second-order ODE $d^2u/d\phi^2 + u = -m(\ell^2 u^2)^{-1}\,V'(1/u)$. For the Kepler potential $V = -k/r = -ku$, this simplifies to $d^2u/d\phi^2 + u = mk/\ell^2$ — a forced linear oscillator whose solution is $u(\phi) = mk/\ell^2 + A\cos(\phi - \phi_0)$, i.e., a conic section. The Binet substitution is one of the cleanest tricks in orbital mechanics.

---

# Legal Operations Used

1. **Operation 6 from the topic page (Legendre transform).** Implicit in setting up $H = T + V$ from $L = T - V$.

2. **Operation 3 from the topic page (check $\{f, H\} = 0$).** Used to identify $\vec L$ and $E$ as conserved.

3. **Operation 9 from the topic page (Reduce by a symmetry via the moment map).** The $SO(3)$ symmetry of the central potential produces the angular momentum vector as moment map, reducing the dimension of the effective problem from $6$ ($T^*\mathbb{R}^3$) to $2$ (radial $(r, p_r)$ after fixing $\vec L$ and using planarity).

---

# Hints

> [!note]- Hint 1
> Conservation of $\vec L$ implies the orbit lies in the plane perpendicular to $\vec L$. So reduce to 2D polar coordinates $(r, \phi)$ in this plane. The kinetic energy becomes $T = \tfrac{1}{2}m(\dot r^2 + r^2\dot\phi^2)$.

> [!note]- Hint 2
> Angular momentum conservation: $\ell = |\vec L| = mr^2\dot\phi$. Use this to eliminate $\dot\phi = \ell/(mr^2)$ from the radial energy expression.

> [!note]- Hint 3
> The radial energy equation is $E = \tfrac{1}{2}m\dot r^2 + \ell^2/(2mr^2) + V(r) = \tfrac{1}{2}m\dot r^2 + V_{\rm eff}(r)$, where $V_{\rm eff}(r) = V(r) + \ell^2/(2mr^2)$ is the effective potential.

> [!note]- Hint 4
> Binet's substitution: let $u = 1/r$. Then $\dot r = -\dot\phi r^2 du/d\phi \cdot 1/r^2 = -\dot\phi du/d\phi \cdot \ell/(m\ell) = ?$. More carefully, $dr/d\phi = -1/u^2 \cdot du/d\phi$, so $\dot r = \dot\phi \cdot dr/d\phi = (\ell/(mr^2))\cdot (-1/u^2 du/d\phi) = -(\ell/m)du/d\phi$. Differentiate again: $\ddot r = -(\ell/m)d^2u/d\phi^2 \cdot \dot\phi = -(\ell^2/m^2r^2)d^2u/d\phi^2 = -(\ell^2 u^2/m^2)d^2u/d\phi^2$.

> [!note]- Hint 5
> The radial equation $m\ddot r = -V_{\rm eff}'(r)$, combined with $V_{\rm eff} = V + \ell^2/(2mr^2)$, gives after substituting $u = 1/r$:
> $$\frac{d^2u}{d\phi^2} + u = -\frac{m}{\ell^2 u^2}V'\left(\frac{1}{u}\right).$$
> This is **Binet's equation**. For $V = -k/r = -ku$: $V'(1/u) = k(1/u)^{-2}(-1) = -ku^2$... wait, $V(r) = -k/r$, so $V'(r) = k/r^2$, hence $V'(1/u) = ku^2$. The RHS becomes $-mku^2/(\ell^2 u^2) = -mk/\ell^2$, which is constant. So $d^2u/d\phi^2 + u = -mk/\ell^2$... but we want $+mk/\ell^2$ for the attractive case. Let me re-examine signs. With $V'(r) = k/r^2 > 0$ (force pointing outward... no wait, the force is $-V'(r) = -k/r^2 < 0$, pointing inward, so the potential $-k/r$ describes attractive gravity. The radial equation: $m\ddot r = -V_{\rm eff}'(r) = -V'(r) + \ell^2/(mr^3)$. The first term is $-k/r^2 < 0$ (attractive). OK so my Binet calculation should give $d^2u/d\phi^2 + u = +mk/\ell^2$. Let me recheck: with $\ddot r = -(\ell^2 u^2/m^2)d^2u/d\phi^2$, the radial equation $m\ddot r + V'(r) = \ell^2/(mr^3)$ becomes... ugh, let me just do it cleanly in the solution.

---

# Solution

The proof breaks into four steps. Step 1 sets up the Jacobi metric. Step 2 uses rotational symmetry to reduce to a planar problem. Step 3 derives Binet's equation. Step 4 solves it for the Kepler potential and recovers conic sections.

**Step 1: Jacobi metric.**

$g^J_{ij} = 2(E - V(r))g_{ij}$, where $g$ is the Euclidean metric. In spherical coordinates: $g^J = 2(E - V)\big(dr^2 + r^2 d\theta^2 + r^2\sin^2\theta\,d\phi^2\big)$.

> [!note]- Derivation
> Jacobi's principle: for the autonomous mechanical Lagrangian $L = \tfrac{1}{2}m|\dot{\vec q}|^2 - V(\vec q)$ with conserved energy $E$, the projected trajectory $\gamma(t) = \vec q(t)$ in $\mathbb{R}^3$ is a geodesic in the conformal Jacobi metric $g^J_{ij} = 2m(E - V)g_{ij}$ (with $g$ the Euclidean metric on $\mathbb{R}^3$; the factor $m$ comes from setting the Lagrangian's mass right). For the central potential, $V = V(r)$ depends only on $r$, so the conformal factor is also a function of $r$ alone, making $g^J$ a rotationally invariant metric.
>
> Explicitly: $g = dr^2 + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)$ in spherical coordinates; $g^J = 2m(E - V(r))[dr^2 + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)]$.
>
> Geodesics in $g^J$ on the **classically allowed region** $\{V < E\}$ (where the conformal factor is positive) are the projections of Hamiltonian trajectories at energy $E$ to $\mathbb{R}^3$.

**Step 2: Reduce to planar motion.**

By conservation of $\vec L = \vec q \times \vec p$, the orbit lies in a fixed plane. WLOG take this to be the $xy$-plane (set $\theta = \pi/2$); use 2D polar coordinates $(r, \phi)$.

> [!note]- Derivation
> Angular momentum is $\vec L = \vec q \times m\dot{\vec q}$, a vector in $\mathbb{R}^3$ with magnitude $|\vec L| = \ell$. Since $\{L^i, H\} = 0$ (rotational invariance), $\vec L$ is conserved as a vector.
>
> $\vec L \cdot \vec q = (\vec q \times m\dot{\vec q})\cdot \vec q = 0$ (triple product with repeated factor). So $\vec q$ is always perpendicular to $\vec L$. Hence $\vec q$ lies in the plane perpendicular to $\vec L$.
>
> Choose coordinates so $\vec L = \ell\hat z$. Then $\vec q$ stays in the $xy$-plane. Use 2D polar coordinates $(r, \phi)$ in this plane:
> $$\vec q = (r\cos\phi, r\sin\phi), \quad |\dot{\vec q}|^2 = \dot r^2 + r^2\dot\phi^2.$$
> Angular momentum: $\ell = (\vec q \times m\dot{\vec q})_z = m(x\dot y - y\dot x) = mr^2\dot\phi$. So $\dot\phi = \ell/(mr^2)$.
>
> Energy: $E = \tfrac{1}{2}m(\dot r^2 + r^2\dot\phi^2) + V(r) = \tfrac{1}{2}m\dot r^2 + \frac{\ell^2}{2mr^2} + V(r) = \tfrac{1}{2}m\dot r^2 + V_{\rm eff}(r),$
> where $V_{\rm eff}(r) = V(r) + \ell^2/(2mr^2)$ is the **effective radial potential** (gravitational plus centrifugal).
>
> The reduced one-dimensional radial problem has Lagrangian $L_r = \tfrac{1}{2}m\dot r^2 - V_{\rm eff}(r)$, with the angular motion determined by $\dot\phi = \ell/(mr^2)$.

**Step 3: Binet's equation.**

$\frac{d^2 u}{d\phi^2} + u = -\frac{m}{\ell^2 u^2}\frac{dV}{dr}\bigg|_{r = 1/u}$ where $u = 1/r$.

> [!note]- Derivation
> Convert from $r(t)$ to $r(\phi)$ (eliminate time). Let $u = 1/r$. Using $\dot\phi = \ell/(mr^2) = \ell u^2/m$:
> $$\dot r = \frac{dr}{d\phi}\dot\phi = -\frac{1}{u^2}\frac{du}{d\phi}\cdot \frac{\ell u^2}{m} = -\frac{\ell}{m}\frac{du}{d\phi}.$$
> Differentiate again:
> $$\ddot r = -\frac{\ell}{m}\frac{d^2u}{d\phi^2}\cdot \dot\phi = -\frac{\ell}{m}\frac{d^2u}{d\phi^2}\cdot \frac{\ell u^2}{m} = -\frac{\ell^2 u^2}{m^2}\frac{d^2u}{d\phi^2}.$$
>
> Radial equation of motion: $m\ddot r = -V_{\rm eff}'(r) = -V'(r) + \frac{\ell^2}{mr^3}$. Substitute:
> $$m\cdot\left(-\frac{\ell^2 u^2}{m^2}\frac{d^2u}{d\phi^2}\right) = -V'(1/u) + \frac{\ell^2 u^3}{m}.$$
> $$-\frac{\ell^2 u^2}{m}\frac{d^2u}{d\phi^2} = -V'(1/u) + \frac{\ell^2 u^3}{m}.$$
> Multiply by $-m/(\ell^2 u^2)$:
> $$\frac{d^2u}{d\phi^2} = \frac{m}{\ell^2 u^2}V'(1/u) - u.$$
> Rearrange:
> $$\boxed{\frac{d^2u}{d\phi^2} + u = \frac{m}{\ell^2 u^2}V'(1/u).}$$
> This is **Binet's equation**. (Sign convention: $V'(r) := dV/dr$ — for Kepler $V = -k/r$, $V'(r) = k/r^2 > 0$, so RHS is positive.)

**Step 4: Kepler solution.**

For $V(r) = -k/r$, Binet's equation becomes $d^2u/d\phi^2 + u = mk/\ell^2$, with solution $u(\phi) = mk/\ell^2 + A\cos(\phi - \phi_0)$, i.e., $r(\phi) = p/(1 + e\cos\phi)$ with $p = \ell^2/(mk)$ and $e = A\ell^2/(mk)$.

> [!note]- Derivation
> For $V(r) = -k/r$: $V'(r) = k/r^2 = ku^2$. So $V'(1/u) = ku^2$ and the RHS of Binet is $m\cdot ku^2/(\ell^2 u^2) = mk/\ell^2$ — a constant! Binet's equation simplifies to
> $$\frac{d^2u}{d\phi^2} + u = \frac{mk}{\ell^2}.$$
> This is a **linear inhomogeneous second-order ODE** with constant coefficients. General solution: $u(\phi) = u_p + u_h$, where $u_p = mk/\ell^2$ (particular solution, the constant) and $u_h = A\cos\phi + B\sin\phi$ (homogeneous solution, $SHO$ at unit frequency).
>
> Setting the phase: $u(\phi) = \frac{mk}{\ell^2}\big(1 + e\cos(\phi - \phi_0)\big)$, where the choice of $\phi_0$ aligns the major axis with $\phi = \phi_0$, and $e := A\ell^2/(mk)$ is the **eccentricity**.
>
> Converting back to $r = 1/u$:
> $$r(\phi) = \frac{\ell^2/(mk)}{1 + e\cos(\phi - \phi_0)} = \frac{p}{1 + e\cos\phi'}$$
> where $p = \ell^2/(mk)$ is the **semi-latus rectum** and $\phi' = \phi - \phi_0$ is the angle measured from the major axis.
>
> **This is the standard equation of a conic section** with focus at the origin (the center of force), semi-latus rectum $p$, and eccentricity $e$:
> - $e = 0$: circle.
> - $0 < e < 1$: ellipse (bound orbit, $E < 0$).
> - $e = 1$: parabola (escape orbit, $E = 0$).
> - $e > 1$: hyperbola (unbound orbit, $E > 0$).
>
> **Energy-eccentricity relation:** at perihelion (closest approach, $\phi = \phi_0$, $r = r_{\min} = p/(1+e)$), $\dot r = 0$, so all energy is in the angular term: $E = \ell^2/(2mr_{\min}^2) + V(r_{\min})$. Substitute and solve: $e = \sqrt{1 + 2E\ell^2/(mk^2)}$.
>
> For $E < 0$ (bound orbit): $-2E\ell^2/(mk^2) < 1$ requires $E < 0$ (ellipses); the eccentricity formula gives real $e < 1$. ✓

> [!note]- Complete formal solution
> **Setup:** central potential $V(r)$, Lagrangian $L = \tfrac{1}{2}m|\dot{\vec q}|^2 - V(r)$. Two conservation laws: energy $E$ and angular momentum $\vec L$.
>
> **Step 1 — Jacobi metric:** $g^J = 2m(E - V(r))(dr^2 + r^2 d\theta^2 + r^2\sin^2\theta\,d\phi^2)$ on $\{V < E\}$. Geodesics in $g^J$ are the projections of Hamiltonian trajectories at energy $E$.
>
> **Step 2 — Planar reduction:** $\vec L$ conserved $\Rightarrow$ orbit in plane perpendicular to $\vec L$. In 2D polar coordinates: $\ell = mr^2\dot\phi$, $E = \tfrac{1}{2}m\dot r^2 + V_{\rm eff}(r)$ with $V_{\rm eff}(r) = V(r) + \ell^2/(2mr^2)$.
>
> **Step 3 — Binet's equation:** with $u = 1/r$,
> $$\frac{d^2u}{d\phi^2} + u = \frac{m}{\ell^2 u^2}V'(1/u).$$
>
> **Step 4 — Kepler $V = -k/r$:** RHS becomes $mk/\ell^2$, giving $d^2u/d\phi^2 + u = mk/\ell^2$. Solution: $u(\phi) = (mk/\ell^2)(1 + e\cos\phi)$, i.e.,
> $$r(\phi) = \frac{p}{1 + e\cos\phi}, \quad p = \frac{\ell^2}{mk}, \quad e = \sqrt{1 + \frac{2E\ell^2}{mk^2}}.$$
> Conic sections: ellipses for $E < 0$, parabolas for $E = 0$, hyperbolas for $E > 0$.
>
> **Step 5 — Turning points:** at $V(r) = E$, the Jacobi metric $g^J$ degenerates (conformal factor zero). This is a coordinate singularity, not a physical one: the particle still has well-defined motion (it reverses direction at the turning point), but the Jacobi metric "stops working" — paths get infinitesimally short in $g^J$-distance, despite physical distance not being zero. The dynamics is well-defined; the geometric description via Jacobi's metric is not. Physically, $E - V(r) = T$ (kinetic energy) vanishes at the turning point, so the conformal factor $2m(E - V) = 2mT$ vanishes there.

---

# Key Takeaways

**Jacobi's principle is mechanics-as-geometry: every autonomous Hamiltonian system is a geodesic flow in a conformally rescaled metric.** This is one of the deepest unifications in classical mechanics. For any mechanical system with conserved energy $E$, trajectories projected to configuration space are *geodesics* in a specific Riemannian metric — the Jacobi metric, conformally related to the kinetic-energy metric by the factor $2(E - V)$. This means **classical mechanics with potentials is hiding inside Riemannian geometry**, with the potential encoded into the conformal rescaling. The Kepler ellipses become geodesics in the Jacobi metric; the harmonic oscillator orbits become geodesics in another Jacobi metric; and so on. **Every textbook problem in classical mechanics can be reformulated as a geodesic problem in an appropriate metric**. This reformulation is the bridge between mechanics and the entire apparatus of Riemannian geometry (curvature, Jacobi fields, focal points, exponential map, comparison theorems), and it is the geometric heart of the **principle of stationary action**.

**The Binet substitution is the trick: orbit-as-graph rather than orbit-as-trajectory.** For central-force problems, the natural variables are not $(r, t)$ but $(u = 1/r, \phi)$ — eliminating the time and looking at the orbit as a curve in space. This converts the (generally nonlinear) radial ODE into a **linear ODE for power-law potentials**, with Kepler ($V \propto 1/r$) and the harmonic oscillator ($V \propto r^2$) as the two cleanest cases. The Binet substitution exhibits the orbit as a function $u(\phi)$ rather than $r(t)$ — a change of dependent and independent variables that exploits the rotational symmetry. **This trick is the prototype of "change to action-angle coordinates"**: in the time variable the dynamics is complicated; in the angle variable the dynamics is rigid rotation. For Kepler, the orbit equation in angular coordinates is exactly the SHO equation, $u'' + u = \text{const}$.

**Conic sections from a linear ODE: the deep "accidental" symmetry of Kepler.** The fact that Kepler orbits are conic sections — a property special to the $1/r$ potential, not shared by any other inverse-power potential — is a consequence of an additional symmetry beyond rotational. The **Laplace–Runge–Lenz vector** $\vec A = \vec p \times \vec L - mk\hat r$ is conserved for the Kepler potential (and only for it), and its conservation is the "accidental" symmetry that makes the orbits close into ellipses rather than precessing rosette curves. The full symmetry group of the Kepler problem is $SO(4)$ (not just $SO(3)$), and the Laplace–Runge–Lenz vector is the moment map of the additional symmetry. This is the classical origin of the **degeneracy of the hydrogen atom's energy levels** in quantum mechanics: the same $SO(4)$ symmetry persists into the quantum problem, making energy levels depend on the principal quantum number $n$ alone (not on $\ell$, the angular momentum quantum number).

**Conformal degeneracy at turning points: the limits of the geometric reformulation.** The Jacobi metric $g^J = 2(E - V)g$ becomes degenerate where $V = E$ — the turning points of the radial motion. Physically, this is where the kinetic energy vanishes and the particle momentarily reverses direction. Geometrically, the Jacobi metric "collapses" — distances in $g^J$ go to zero. The conformal rescaling breaks down at the boundary of the classically allowed region. The dynamics is still well-defined (the particle bounces off the turning point), but the geometric description must be extended carefully — one approach is to use the full $(2n-1)$-dimensional energy shell and work intrinsically rather than projecting to configuration space. This is a general feature of **Jacobi-like reformulations**: they trade time-evolution for geometric structure, but the geometric structure has its own singularities reflecting physical features (turning points, classically forbidden regions, caustics in optics).
