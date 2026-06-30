---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity"
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
tags: [physics, special-relativity]
---

# Problem Statement

The equivalence principle says a gravitational field can be transformed away by going to a freely-falling frame. The qualifier *locally* is essential. This exercise pins down what part of gravity *cannot* be transformed away and identifies it with curvature.

Consider a spherical mass $M$ (a planet) and two small test particles dropped from rest, both at distance $r$ from the centre, separated by a small horizontal displacement $\vec\xi$ with $|\vec\xi| = \xi \ll r$.

1. *Newtonian tidal forces.* Compute the *relative* acceleration $\ddot{\vec\xi}$ of the two particles in the Newtonian field $\Phi = -GM/r$. Show that for $\vec\xi$ horizontal the particles accelerate *toward* each other at $\ddot\xi = -(GM/r^3)\xi$, and that for $\vec\xi$ vertical they accelerate *apart* at $\ddot\xi = +2(GM/r^3)\xi$ (the head and tail of the body stretched along the field). Identify the **tidal tensor** $E_{ij} = \partial_i\partial_j\Phi$ controlling these accelerations.
2. *Trace property.* Show that the tidal tensor is traceless, $E^i{}_i = \nabla^2\Phi = 0$ in vacuum (where Poisson is $\nabla^2\Phi = 0$). Conclude that tidal forces have no "monopole" — they always have the pattern of stretching in one direction and compressing in the perpendicular ones, so a freely-falling small region is squeezed into a prolate shape oriented toward the source.
3. *Failure of the equivalence-principle substitution.* Show explicitly that the relative acceleration $\ddot{\vec\xi}$ between two test particles in a real gravitational field is *not* zero, while in a uniformly accelerated frame in empty Minkowski space it *is* zero — so no choice of acceleration can mimic the field over a region containing two separated test particles.
4. *Order of magnitude.* For $M = M_\oplus$, $r = R_\oplus$, $\xi = 1\,\mathrm{m}$, find the tidal acceleration $\ddot\xi$ and compare to $g$. For an astronaut in low-Earth orbit ($r = R_\oplus + 400\,\mathrm{km}$, $\xi = 2\,\mathrm{m}$ — head to foot), find $\ddot\xi$ — this is the "microgravity" residual the astronaut actually feels.
5. *Geodesic deviation.* State (without proof) the **geodesic deviation equation** in general relativity:
$$\frac{D^2 \xi^\mu}{D\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu u^\rho \xi^\sigma,$$
where $R^\mu{}_{\nu\rho\sigma}$ is the **Riemann curvature tensor** and $u$ the four-velocity. Compare its Newtonian limit $\ddot\xi^i = -E^i{}_j \xi^j$ with your result from part 1 and identify which components of $R^\mu{}_{\nu\rho\sigma}$ reduce to $E_{ij}$.

**Recall:**

![[Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity#Statement]]

The equivalence principle is *local* — it asserts the indistinguishability of a uniform gravitational field and a uniformly accelerated frame only over a region small enough that the field is uniform. The residual gravity, irremovable by any change of frame, is the **tidal field**: the relative acceleration of nearby freely-falling test bodies, controlled in Newton by the tidal tensor $E_{ij} = \partial_i \partial_j \Phi$ and in general relativity by the Riemann curvature $R^\mu{}_{\nu\rho\sigma}$.

---

# Convergent Strategy

**Problem class.** A *boundary-of-a-theorem* problem: take a principle (the equivalence principle) and locate exactly where it breaks down. The strategy is to construct the configuration that distinguishes the two situations the principle claims are equivalent (real field vs accelerated frame in vacuum), then identify the geometric object encoding the difference (curvature).

**Assumption pattern.** Two ingredients: (i) a Newton-or-relativistic field that is *not* uniform — typically a $1/r$ field with a definite source — and (ii) a configuration with at least two test particles, so the *relative* motion can be probed. Tidal effects vanish for a single particle (which always free-falls weightlessly) and for any uniform field (which can be globally transformed away); they appear only when both spatial separation and field inhomogeneity are present.

**Theorem routing.** Part 1 is straightforward Newton: Taylor-expand the gravitational acceleration $\vec g(\vec r + \vec\xi) = \vec g(\vec r) + (\vec\xi\cdot\nabla)\vec g + \cdots$, the second term being the tidal acceleration. Part 2 uses Poisson in vacuum. Part 3 is a contradiction by construction. Part 4 plugs in numbers. Part 5 anticipates the general-relativistic content: the tidal tensor is the leading component of the Riemann curvature, and the geodesic deviation equation is the relativistic generalisation of Newtonian tidal effects.

**Key decision point.** The crux is the recognition that *two test particles* are required to expose the tidal field — one particle gives only the equivalence principle (free fall is locally inertial), and the tidal effect is a statement about how two nearby free-fall trajectories diverge from being parallel. This is precisely the *deviation* in geodesic deviation, and it is the obstruction to the parallel transport of a tangent vector around a closed loop — that is, the curvature.

---

# Legal Operations Used

1. **Invoke the equivalence principle to swap a gravitational field for an accelerated frame** (operation 2 from the topic page): part 3 *fails* to do this — the impossibility of the substitution over a finite region is the exercise's main point.

2. **Take the Newtonian (weak, slow) limit** (operation 1 from the topic page): part 5 takes the Newtonian limit of the geodesic deviation equation to recover the tidal tensor.

3. **Linearise about Minkowski: write $g = \eta + h$** (operation 7 from the topic page): the relation between the Newtonian tidal tensor and components of the Riemann curvature uses the weak-field expansion $g_{00} = 1 + 2\Phi/c^2$.

---

# Hints

> [!note]- Hint 1
> The gravitational acceleration of a particle at position $\vec r_0 + \vec\xi$ is $\vec g = -\nabla\Phi(\vec r_0 + \vec\xi) \approx -\nabla\Phi(\vec r_0) - (\vec\xi\cdot\nabla)\nabla\Phi(\vec r_0)$. The first term is the same for both particles (they fall together as a "centre"); the difference between the two particles' accelerations is $-(\vec\xi\cdot\nabla)\nabla\Phi = -E\cdot\vec\xi$ with $E_{ij} = \partial_i\partial_j\Phi$. For $\Phi = -GM/r$: compute $\partial_i\partial_j\Phi$ and act on horizontal vs vertical $\vec\xi$.

> [!note]- Hint 2
> Trace: $E^i{}_i = \partial_i\partial^i\Phi = \nabla^2\Phi$. In vacuum Poisson gives $\nabla^2\Phi = 0$, so $\text{tr}(E) = 0$. Eigenvalues of $E$ for a point mass: along the radial direction $\partial_r^2(-GM/r) = -2GM/r^3$ — wait, with signs: $\Phi = -GM/r$, $\partial_r\Phi = GM/r^2$, so $\partial_r^2\Phi = -2GM/r^3$. The eigenvalue of $-E$ in the radial direction is $+2GM/r^3$ (stretching). In the angular directions the eigenvalues sum to the negative of this (so $-GM/r^3$ each), giving compression. The eigenvalues are $(+2, -1, -1)\cdot GM/r^3$ — the prolate stretching pattern.

> [!note]- Hint 3
> Two test particles released at separation $\vec\xi$ from rest in a real $1/r$ field have relative acceleration $\ddot{\vec\xi} = -E\cdot\vec\xi \neq 0$ (parts 1–2). Two test particles released at separation $\vec\xi$ from rest in an accelerated frame in empty Minkowski space *are inertial* in the global frame and remain parallel — relative acceleration $0$ in any frame. The two situations are distinguishable by measuring $\ddot{\vec\xi}$, so they are not physically equivalent over the region containing both particles.

> [!note]- Hint 4
> $GM_\oplus/R_\oplus^3 = (g/R_\oplus) = (9.8)/(6.4\times 10^6) \approx 1.5\times 10^{-6}\,\mathrm{s}^{-2}$. For $\xi = 1\,\mathrm{m}$ at the surface, vertical tidal acceleration $\approx 2\times 1.5\times 10^{-6} = 3\times 10^{-6}\,\mathrm{m\,s^{-2}}$ — a factor $3\times 10^{-7}$ smaller than $g$, completely negligible for a $1\,\mathrm{m}$ body on Earth. For an astronaut at $400\,\mathrm{km}$ altitude with $\xi = 2\,\mathrm{m}$: $GM/r^3 \approx 1.2\times 10^{-6}\,\mathrm{s}^{-2}$, giving $\ddot\xi \approx 5\times 10^{-6}\,\mathrm{m\,s^{-2}}$ — order $5\,\mu g$, the microgravity floor of orbital free-fall environments.

> [!note]- Hint 5
> In the Newtonian limit the four-velocity is dominated by the time component $u^\mu \approx (1, 0, 0, 0)$, so the geodesic deviation equation becomes $\ddot\xi^i \approx -R^i{}_{00j}\xi^j$, comparing with $\ddot\xi^i = -E^i{}_j \xi^j$ identifies $R^i{}_{00j} = E^i{}_j = \partial_i\partial_j\Phi$. The Riemann tensor's $R^i{}_{00j}$ component is the Newtonian tidal tensor — this is the cleanest statement that *curvature is the relativistic generalisation of the second derivatives of the Newtonian potential*.

---

# Solution

The exercise constructs the boundary of the equivalence principle by exhibiting a *measurement* — the relative acceleration of two test particles — that distinguishes a real gravitational field from any accelerated frame in empty space. The distinguishing quantity is the *tidal tensor*, the second derivatives of the potential, which in general relativity becomes the Riemann curvature. The reusable thread: the equivalence principle removes the gravitational field at a point and its first derivatives at that point, but the second derivatives — the inhomogeneity — are *frame-invariant* and constitute the irreducible content of gravity.

**Step 1: Newtonian tidal forces from $1/r$.**

> [!note]- Derivation
> The gravitational potential of a point mass $M$ is $\Phi(\vec r) = -GM/r$ with $r = |\vec r|$. The gravitational acceleration is $\vec g(\vec r) = -\nabla\Phi$:
> $$g_i = -\partial_i\Phi = -GM\,\partial_i(1/r) = -GM\,(-x_i/r^3) = -GM\,x_i/r^3.$$
> So $\vec g = -(GM/r^3)\vec r$, the attractive radial field.
>
> Now consider two particles, one at $\vec r$ (the "centre") and one at $\vec r + \vec\xi$. Their accelerations differ:
> $$\Delta g_i = g_i(\vec r + \vec\xi) - g_i(\vec r) \approx \xi^j\,\partial_j g_i = -\xi^j\,\partial_j\partial_i\Phi = -E_{ij}\,\xi^j,$$
> where the **tidal tensor** is
> $$E_{ij} \equiv \partial_i\partial_j\Phi.$$
> The relative acceleration $\ddot{\vec\xi} = \Delta\vec g = -E\cdot\vec\xi$.
>
> *Computing $E_{ij}$ for the point mass:*
> $$\partial_i\partial_j\left(-\frac{GM}{r}\right) = -GM\,\partial_i\partial_j(1/r) = -GM\left(\frac{3 x_i x_j}{r^5} - \frac{\delta_{ij}}{r^3}\right) = \frac{GM}{r^3}\left(\delta_{ij} - \frac{3 x_i x_j}{r^2}\right).$$
> Pick coordinates so the mass is at the origin and the particles are near the point $\vec r = r\,\vec e_z$ (i.e., $x_i x_j/r^2 = \delta_{iz}\delta_{jz}$). Then:
> $$E_{ij} = \frac{GM}{r^3}\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 - 3 \end{pmatrix} = \frac{GM}{r^3}\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -2 \end{pmatrix}.$$
> *Horizontal $\vec\xi = \xi\,\vec e_x$*: $\ddot{\vec\xi} = -E\cdot\vec\xi$ gives $\ddot\xi = -(GM/r^3)\xi$. The particles accelerate *toward each other*. $\checkmark$
>
> *Vertical $\vec\xi = \xi\,\vec e_z$*: $\ddot\xi = -(-2GM/r^3)\xi = +2(GM/r^3)\xi$. The particles accelerate *apart*. $\checkmark$
>
> The pattern: a body falling toward a point mass is *stretched* along the radial direction and *squeezed* in the perpendicular plane. This is the classical tidal pattern, and it is responsible for tidal bulges on Earth (sun and moon both stretch the Earth radially), tidal disruption of comets passing too close to a planet, and tidal heating of moons by Jupiter.

**Step 2: The tidal tensor is traceless in vacuum.**

> [!note]- Derivation
> Trace: $E^i{}_i = \delta^{ij}E_{ij} = \delta^{ij}\partial_i\partial_j\Phi = \nabla^2\Phi$. In vacuum (no matter at the field point), Poisson's equation $\nabla^2\Phi = 4\pi G\rho$ gives $\nabla^2\Phi = 0$, so $\text{tr}(E) = 0$.
>
> Explicit check from part 1: the eigenvalues of $E$ at the field point are $(GM/r^3)\cdot(1, 1, -2)$, summing to $0$. $\checkmark$
>
> *Consequence:* the eigenvalues of any tidal tensor in vacuum sum to zero, so they cannot all be of the same sign. The tidal field always has both stretching (positive eigenvalues, particles accelerate apart) and compressing (negative eigenvalues, particles accelerate together) directions — a freely-falling small region is squeezed in some directions and stretched in others, never uniformly contracted or expanded. The familiar pattern is the prolate "stretching toward the source, squeezing perpendicular" eigenstructure $(+2, -1, -1)$ for a point mass.
>
> This is why a freely-falling small ball of dust forms an elongated shape oriented along the line to the source rather than just shrinking — and why the lunar tide produces two bulges, one on the near side and one on the far side of the Earth.

**Step 3: The equivalence-principle substitution fails over a finite region.**

> [!note]- Derivation
> Two physical configurations:
>
> *Configuration A: real gravitational field.* Two test particles, separated by $\vec\xi$, freely falling near a planet of mass $M$. Their relative acceleration is $\ddot{\vec\xi} = -E\cdot\vec\xi$, generically nonzero with the pattern of part 1.
>
> *Configuration B: uniformly accelerated frame in empty Minkowski space.* Two test particles, separated by $\vec\xi$, freely floating in a cabin which accelerates rigidly at some uniform $\vec a_0$. In the *global* inertial frame the two particles are inertial — they have $\ddot{\vec\xi} = 0$ globally — and this is a Lorentz invariant statement (the proper acceleration of each particle is zero). In the *cabin* frame both particles feel the same uniform pseudo-force $-\vec a_0$, identical for both, so their relative acceleration $\ddot{\vec\xi}_{\mathrm{cabin}}$ is also zero. Either way, $\ddot{\vec\xi} = 0$.
>
> So a measurement of the *relative* acceleration of two test particles distinguishes A from B: in A it is $-E\cdot\vec\xi$, in B it is zero. The equivalence principle's claim that A and B are physically equivalent is *false* over any region containing two separated test particles.
>
> *The fix.* The equivalence principle holds at a single event (the centre of the cabin, say), where both particles in A see the same gravitational field $\vec g(\vec r_0)$ — that field can be cancelled by accelerating the cabin at $\vec a_0 = -\vec g(\vec r_0)$, and the centre particle becomes inertial. Away from that one point the substitution fails by an amount $-E\cdot\vec\xi$, *linear* in the displacement. So the equivalence principle is exact at a *point* and to *zero-th order* in $\vec\xi$; it fails at first order in $\vec\xi$ for the relative motion of nearby particles, and the failure size is the tidal tensor.
>
> This is the precise mathematical statement of "the equivalence principle holds locally", and the failure beyond first order is gravity's irreducible content — the part that no choice of accelerated frame can remove.

**Step 4: Order of magnitude.**

> [!note]- Derivation
> For Earth: $GM_\oplus/R_\oplus^2 = g_\oplus = 9.8\,\mathrm{m\,s^{-2}}$ and $GM_\oplus/R_\oplus^3 = g_\oplus/R_\oplus = 9.8/(6.4\times 10^6) \approx 1.53\times 10^{-6}\,\mathrm{s}^{-2}$.
>
> *Surface, $\xi = 1\,\mathrm{m}$ vertical:* $\ddot\xi = 2\times 1.53\times 10^{-6}\times 1 = 3.1\times 10^{-6}\,\mathrm{m\,s^{-2}}$ — about $3\times 10^{-7}\,g$, utterly negligible for a $1\,\mathrm{m}$ body. The tides on a human-scale object on Earth's surface are not perceptible.
>
> *Low Earth orbit, $r = R_\oplus + 400\,\mathrm{km} \approx 6.78\times 10^6\,\mathrm{m}$, $\xi = 2\,\mathrm{m}$ (astronaut head-to-foot):* $GM_\oplus/r^3 \approx 6.674\times 10^{-11}\times 5.97\times 10^{24}/(6.78\times 10^6)^3 \approx 1.28\times 10^{-6}\,\mathrm{s}^{-2}$. Then $\ddot\xi \approx 2\times 1.28\times 10^{-6}\times 2 = 5.1\times 10^{-6}\,\mathrm{m\,s^{-2}}$ — about $5\times 10^{-7}\,g$, or $0.5\,\mu g$.
>
> This is the *microgravity floor* of free-fall environments. An astronaut in orbit is *almost* in a Minkowski inertial frame — the equivalence principle has cancelled the dominant gravity — but the tidal residual is the leftover $\sim 0.5\,\mu g$ between her head and feet, oriented to stretch her radially toward the Earth. For sensitive experiments (protein crystal growth, certain materials science, biological cultures) this is the limit that an orbital lab cannot push below: it is the unavoidable curvature of spacetime, not an engineering imperfection.

**Step 5: Geodesic deviation and the Riemann tensor.**

> [!note]- Derivation
> In general relativity, two nearby freely-falling test particles are described by two geodesics with tangent vectors $u^\mu$, and the small connecting vector $\xi^\mu$ between them obeys the **geodesic deviation equation**:
> $$\frac{D^2 \xi^\mu}{D\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu u^\rho \xi^\sigma,$$
> where $D/D\tau$ is the covariant derivative along the worldline and $R^\mu{}_{\nu\rho\sigma}$ is the Riemann curvature tensor. The vault's [[Riemannian Geometry III — Riemann Curvature and Topology]] introduces the Riemann tensor on a Riemannian manifold; the Lorentzian version differs only in signature.
>
> *Newtonian limit.* For slow motion, $u^\mu \approx (1, 0, 0, 0)$ and $D^2/D\tau^2 \approx \partial_t^2 = \ddot{\phantom{\xi}}$ (covariant derivative collapses to partial in the Newtonian limit), so the equation becomes
> $$\ddot\xi^i \approx -R^i{}_{00j}\,\xi^j.$$
> Comparing with the Newtonian tidal result $\ddot\xi^i = -E^i{}_j\xi^j = -(\partial^i\partial_j\Phi)\xi^j$:
> $$\boxed{\;R^i{}_{00j} = \partial^i\partial_j\Phi = E^i{}_j.\;}$$
> The Newtonian tidal tensor *is* the spatial-time-time-spatial component of the Riemann curvature tensor in the weak-field limit. This is the precise sense in which "curvature is the relativistic generalisation of the tidal tensor", and it is the structural identification that licenses interpreting "gravity is curvature" as a refined statement of Newtonian tides.
>
> The Ricci scalar curvature $R^\mu{}_{\mu\nu\rho}$ takes the trace, which (by the trace-free property in vacuum) gives $R_{00} = \nabla^2\Phi = 4\pi G\rho$ — exactly Poisson's equation. So Einstein's equations, in the appropriate component, reduce to Poisson, with the source $T_{00} = \rho c^2$ identifying $G_{00} = R_{00} - \tfrac12 R \cdot 1 \to 8\pi G T_{00}/c^4$ recovering Newton.
>
> This identification — Riemann tensor in vacuum is the tidal tensor, Ricci tensor sources matter via Poisson — is the cleanest single statement of why general relativity reduces to Newton in the appropriate limit. The exercise has reached the doorway of general relativity by following the equivalence principle to its boundary and finding the curvature waiting there.

> [!note]- Complete formal solution
> (1) From $\Phi = -GM/r$, $E_{ij} = \partial_i\partial_j\Phi = (GM/r^3)(\delta_{ij} - 3x_i x_j/r^2)$, with eigenvalues $(GM/r^3)\cdot(1,1,-2)$ along $(\hat\theta_1, \hat\theta_2, \hat r)$. Horizontal $\vec\xi$: $\ddot\xi = -(GM/r^3)\xi$, particles converge. Vertical: $\ddot\xi = +2(GM/r^3)\xi$, particles diverge — the prolate tidal stretching. (2) $\text{tr}(E) = \nabla^2\Phi = 0$ in vacuum (Poisson with $\rho = 0$), so eigenvalues sum to zero; the tidal pattern is always stretch + compress, never uniform contraction. (3) In configuration A (real field) $\ddot{\vec\xi} = -E\cdot\vec\xi \neq 0$; in configuration B (accelerated frame in vacuum) both particles are inertial in the global frame, so $\ddot{\vec\xi} = 0$. Measurement of relative acceleration distinguishes A from B over any region containing two separated particles, so the equivalence-principle substitution fails at first order in $\vec\xi$; it is exact only at a point. (4) $GM_\oplus/R_\oplus^3 \approx 1.5\times 10^{-6}\,\mathrm{s}^{-2}$, so a $1\,\mathrm{m}$ vertical body on Earth feels tides of $3\,\mu\mathrm{m\,s^{-2}}$ ($3\times 10^{-7}\,g$, negligible); an astronaut in low Earth orbit ($r = R_\oplus + 400\,\mathrm{km}$, $\xi = 2\,\mathrm{m}$) feels $\sim 5\,\mu\mathrm{m\,s^{-2}} \sim 0.5\,\mu g$ — the irreducible microgravity floor. (5) The Newtonian limit of the geodesic deviation equation is $\ddot\xi^i = -R^i{}_{00j}\xi^j$, identifying $R^i{}_{00j} = E^i{}_j = \partial^i\partial_j\Phi$. The Newtonian tidal tensor is a specific component of the Riemann curvature, and curvature is the relativistic generalisation of the second derivatives of the gravitational potential — the precise sense in which "gravity is curvature". $\blacksquare$

---

# Key Takeaways

**The equivalence principle is exact at a point and to first order in displacement; the tidal tensor is the second-order obstruction, and it is what no acceleration can mimic.** The most important refinement of the equivalence principle is that it removes the gravitational field at one event (and to zeroth order around it), but the *gradient* of the field — the tidal tensor $E_{ij} = \partial_i\partial_j\Phi$ — is a frame-invariant tensor that no acceleration can transform away. Two test particles separated by $\vec\xi$ in a real field accelerate relative to each other at $-E\cdot\vec\xi$, while in any accelerated frame in empty Minkowski space they remain parallel. The reusable pattern: whenever the equivalence principle is invoked, check whether the measurement is sensitive to first derivatives of the field (in which case the substitution is fine) or second derivatives (in which case it fails). The substitution is exact for things like a single particle's free fall and a clock's tick rate, but it fails for the *relative* motion of two particles, the focusing of a bundle of geodesics, or any measurement that probes the inhomogeneity of the field. This is why the equivalence principle is conventionally stated with the word *locally* — it is a *pointwise* equivalence with a known, finite-displacement correction.

**Tidal forces are traceless in vacuum, so the tidal pattern is always "stretch + compress", never uniform contraction.** A subtle but important structural fact: Poisson's equation in vacuum, $\nabla^2\Phi = 0$, is the statement that the tidal tensor is traceless, which forces the eigenvalues to sum to zero. So a freely-falling small ball of dust does not just shrink or expand — it changes *shape* into a prolate ellipsoid oriented toward the source, with one stretching direction and two compressing ones (for a point-mass field). This explains, with no further calculation, why ocean tides on Earth have two bulges (not one — the near and far sides both stretch radially toward the Moon), why a comet passing too close to Jupiter (within the Roche limit) is stretched into a string of fragments rather than crushed, and why a freely-falling laboratory in space cannot achieve true zero-gravity — it can only minimise the trace-free residual. The structural lesson: vacuum tidal effects are *shape-changing*, never volume-changing, and the volume-changing part of curvature requires matter (the Ricci tensor) to be nonzero.

**The Riemann curvature tensor is the relativistic generalisation of the tidal tensor — specifically $R^i{}_{00j} = \partial^i\partial_j\Phi$ in the weak-field limit.** The cleanest statement of "gravity is curvature" is the geodesic deviation equation $\ddot\xi^i = -R^i{}_{00j}\xi^j$, which in the Newtonian limit reduces to the tidal-tensor relation $\ddot\xi^i = -E^i{}_j\xi^j$. The Riemann tensor is the *frame-invariant* encoding of the tidal field, generalised to general matter distributions and arbitrary frames. The bridge to Einstein's equation is that the *Ricci* tensor (the trace of Riemann) reduces in the weak-field limit to the Laplacian of the potential, so the Ricci-matter coupling $R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = (8\pi G/c^4)T_{\mu\nu}$ recovers Poisson in the appropriate component. This identification — curvature is tidal, Ricci is Poisson — is what makes general relativity the natural completion of the equivalence-principle-plus-Newton picture: it is exactly the theory in which the geometry encodes the tidal forces that cannot be transformed away. The reusable thread: any time you encounter the equivalence principle, ask "what is the residual that no frame can remove?" — and the answer is always curvature, in some form.
