---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Parallel Transport"
  - "Def - Covariant Derivative along a Curve"
  - "Thm - Parallel Transport is an Isometry for Metric-Compatible Connections"
tags: [geometry, riemannian-geometry, parallel-transport, holonomy]
---

# Problem Statement

On the unit 2-sphere $S^2$ with the round metric $g = d\theta^2 + \sin^2\theta\,d\varphi^2$, parallel-transport a tangent vector around the **geodesic triangle** with vertices at the north pole $N = (0, *)$, the point $A = (\pi/2, 0)$, and the point $B = (\pi/2, \pi/2)$. (The triangle's sides are three great-circle arcs.)

Show that the parallel-transported vector returns to its starting point rotated by exactly $\pi/2$ — the **holonomy angle** of the loop. Verify this answer by a second method using the integrated Gauss-Bonnet formula: $\text{holonomy angle} = \int_T K\,dA$ for $T$ the triangular region and $K = 1$ the Gaussian curvature of the unit sphere.

**Recall:**

![[Def - Parallel Transport#The Definition]]

A **geodesic** on $S^2$ is a great-circle arc. Parallel transport along a geodesic preserves the angle to the velocity vector (in addition to length). On a 2-dimensional Riemannian manifold, the **holonomy angle** of parallel transport around a closed loop equals the integrated Gaussian curvature over the enclosed region (this is the local statement of the Gauss-Bonnet theorem).

The Gaussian curvature of the unit sphere is $K = 1$ everywhere. The triangle in this problem has three right angles at $N, A, B$, and encloses a spherical area equal to $\pi/2$ — one-eighth of the total sphere area $4\pi$.

---

# Convergent Strategy

**Problem class:** A parallel-transport / holonomy computation on a surface — the prototypical example of "curvature ≠ flat" producing a nonzero geometric phase under parallel transport. Two routes: direct ODE solution segment by segment, or the global Gauss-Bonnet shortcut.

**Assumption pattern:** The closed loop consists of three great-circle arcs, each of which is a geodesic. Parallel transport along a geodesic is highly constrained: the velocity $\dot\gamma$ is parallel (by the geodesic equation), and any orthogonal direction is also parallel-transported as a rigid rotation. So along each segment, parallel transport rotates the frame by exactly the angle between the start and end velocities — which is determined by the geometry of the meeting.

**Theorem routing:** Use the angle-preservation property of parallel transport along geodesics ([[Thm - Parallel Transport is an Isometry for Metric-Compatible Connections]] applied with $V = W$): the angle of the transported vector relative to the geodesic is preserved. At each vertex, parallel transport from the incoming geodesic's velocity frame to the outgoing geodesic's velocity frame changes the reference direction by the turning angle of the path. The total rotation is the sum of turning angles, which equals $2\pi$ minus the sum of interior angles (Gauss-Bonnet for spherical triangles).

**Key decision point:** The non-obvious move is recognising that the holonomy is the *defect* of the triangle's interior angle sum from $\pi$ (the Euclidean value). The three angles are each $\pi/2$, summing to $3\pi/2$, so the defect is $3\pi/2 - \pi = \pi/2$ — which is the holonomy angle. The Gauss-Bonnet formula $\int K\,dA + \int\kappa_g\,ds + \sum(\pi - \alpha_i) = 2\pi\chi$ applied to a geodesic triangle ($\kappa_g = 0$, $\chi = 1$ for a disc) gives $\int K\,dA = 2\pi - \sum(\pi - \alpha_i) = \sum\alpha_i - \pi$ — the angle defect. For the unit sphere $K = 1$, this is also the area of the triangle, $\pi/2$.

---

# Legal Operations Used

1. **Operation 4 from the topic page (Solve the parallel transport ODE along a curve).** Along each geodesic segment, the parallel transport is determined by the rotation of the segment's velocity from start to end. For a meridian or equatorial arc, this is computed directly.

2. **Operation 9 from the topic page (Use metric-compatibility to differentiate inner products freely).** Combined with the parallel-transport property, this gives angle-preservation: the angle between a parallel-transported vector and the parallel-transported velocity vector is constant along the geodesic.

---

# Hints

> [!note]- Hint 1
> Along a geodesic, the velocity vector $\dot\gamma$ is parallel-transported (the very meaning of "geodesic"). So any tangent vector at the start, decomposed into components along $\dot\gamma$ and perpendicular to $\dot\gamma$, has its components parallel-transported as: the $\dot\gamma$-component stays along the (parallel-transported) velocity; the perpendicular component stays perpendicular. Both lengths are preserved.

> [!note]- Hint 2
> At each vertex of the triangle, the incoming and outgoing geodesics meet at a specific angle. For the triangle $N, A, B$ on the unit sphere, the three angles are each $\pi/2$. (Check: at $N$, the two meridians to $A$ and $B$ differ in longitude by $\pi/2$; at $A$ and $B$, the meridian and the equator meet at right angles.)

> [!note]- Hint 3
> The holonomy angle is the **angle defect** of the geodesic triangle: the sum of interior angles minus $\pi$ (the Euclidean value). For this triangle: $3 \cdot (\pi/2) - \pi = \pi/2$. So the parallel-transported vector returns rotated by $\pi/2$.

> [!note]- Hint 4
> Verify via Gauss-Bonnet: $\int_T K\,dA = $ area $= \pi/2$ on the unit sphere (the triangle is one octant), confirming the holonomy angle is $\pi/2$.

---

# Solution

**Plan paragraph.** The solution has three steps. Step 1 sets up the triangle and identifies the three geodesic segments and their angles of meeting. Step 2 tracks a tangent vector through parallel transport along each segment, using the principle that on a geodesic, the angle to the velocity is conserved. Step 3 verifies via Gauss-Bonnet, computing the triangle's area as the holonomy.

**Step 1: Set up the geodesic triangle.**

Vertices: $N = $ north pole (parametrised as $\theta = 0$), $A = (\theta = \pi/2, \varphi = 0)$, $B = (\theta = \pi/2, \varphi = \pi/2)$.

Sides (all great-circle arcs):
- **Side $NA$:** the meridian from $N$ to $A$, with $\varphi = 0$ fixed and $\theta$ varying from $0$ to $\pi/2$. Velocity direction: $\partial_\theta$ (southward).
- **Side $AB$:** the equatorial arc from $A$ to $B$, with $\theta = \pi/2$ fixed and $\varphi$ varying from $0$ to $\pi/2$. Velocity direction at $A$: $\partial_\varphi$ (eastward).
- **Side $BN$:** the meridian from $B$ back to $N$, with $\varphi = \pi/2$ fixed and $\theta$ varying from $\pi/2$ to $0$. Velocity direction at $B$: $-\partial_\theta$ (northward).

Interior angles (each is the angle between the two sides meeting at the vertex):
- At $N$: the two meridians at $\varphi = 0$ and $\varphi = \pi/2$ meet at angle $\pi/2$ (they differ by $\pi/2$ in longitude).
- At $A$: the meridian (going north-south) meets the equator (going east-west) at angle $\pi/2$.
- At $B$: same as $A$, the meridian meets the equator at $\pi/2$.

Sum of interior angles: $3\pi/2$. Angle defect (sum minus $\pi$): $\pi/2$.

> [!note]- Derivation
> Use spherical coordinates. The two meridians at $\varphi = 0, \pi/2$ meet at the north pole — at the pole the angle between the two meridians equals their longitude difference, which is $\pi/2$. At $A = (\pi/2, 0)$, the meridian's tangent is $\partial_\theta$ (a unit vector in the round metric since $g_{\theta\theta} = 1$) and the equator's tangent is $\partial_\varphi$ (which has unit length at $\theta = \pi/2$ since $g_{\varphi\varphi} = \sin^2(\pi/2) = 1$). These are orthogonal directions, so the angle is $\pi/2$. Same at $B$.

**Step 2: Track parallel transport segment by segment.**

Start at $N$ with an initial tangent vector $v_0 \in T_N S^2$. Convention: take $v_0$ pointing along the direction towards $A$, i.e., along the meridian at $\varphi = 0$ (so $v_0$ is aligned with $\partial_\theta$ in the chart valid at $A$).

*Segment $NA$ (meridian, parallel transport from $N$ to $A$).* The meridian $\varphi = 0$ is a geodesic, with velocity $\dot\gamma = \partial_\theta$ (in arc-length parametrisation since $g_{\theta\theta} = 1$). The velocity is parallel along itself, so the parallel transport of $v_0$ is the vector that started aligned with the velocity and remains aligned with the velocity. At $A$, the velocity is $\partial_\theta|_A$, so the parallel-transported vector is $\partial_\theta|_A$ — pointing south at $A$.

*Segment $AB$ (equator, parallel transport from $A$ to $B$).* At $A$, the incoming vector is $\partial_\theta|_A$, pointing south. The outgoing velocity (along the equator) is $\partial_\varphi|_A$ (unit length at the equator). The angle between $\partial_\theta|_A$ and $\partial_\varphi|_A$ is $\pi/2$ (they are orthogonal). Along the equator, parallel transport preserves angles to the velocity $\partial_\varphi$, so the parallel-transported vector stays at angle $\pi/2$ to the equatorial velocity. At $B$, the equatorial velocity is $\partial_\varphi|_B$, and the parallel-transported vector is at $\pi/2$ to it, namely $-\partial_\theta|_B$ (pointing *north* from $B$ — perpendicular to $\partial_\varphi$, with the orientation determined by parallel transport along a geodesic, which preserves the right-hand rule). Wait, more carefully: on the equator at $A$, $\partial_\theta|_A$ points south (towards $\theta = \pi$, away from the pole) and $\partial_\varphi|_A$ points east. The "left perpendicular to $\partial_\varphi|_A$" (i.e., $90°$ counterclockwise from the eastward velocity, viewed from outside the sphere with normal pointing outward) is $-\partial_\theta|_A$ (north). So $\partial_\theta|_A$ is the *right perpendicular* to $\partial_\varphi|_A$. Along parallel transport on the equator, this "right perpendicular" relation is preserved. At $B$, the velocity is $\partial_\varphi|_B$ (east), and the right perpendicular is $\partial_\theta|_B$ (south). So the parallel-transported vector at $B$ is $\partial_\theta|_B$, pointing south.

*Segment $BN$ (meridian, parallel transport from $B$ to $N$).* The meridian's velocity at $B$ is $-\partial_\theta|_B$ (pointing north, towards the pole). The incoming vector is $\partial_\theta|_B$ (pointing south, away from the pole). The angle between them is $\pi$ (they are opposite). Along the meridian (a geodesic), parallel transport preserves the angle to the velocity: the angle stays $\pi$. At $N$, the meridian's velocity (in the limit) is $-\partial_\theta$ — pointing into the north pole, which from the chart at the south side of the pole is the direction "into the pole from $\varphi = \pi/2$". The parallel-transported vector is at angle $\pi$ to this, i.e., pointing "out of the pole towards $\varphi = \pi/2$" — which in the original chart (centred at $\varphi = 0$) is the direction $\partial_\theta$ in the chart with $\varphi = \pi/2$, equivalently rotated by $\pi/2$ from the original $v_0$ direction (which was $\partial_\theta$ in the $\varphi = 0$ chart).

**Net rotation:** the original vector $v_0$ pointing "towards $A$" returns rotated to a vector pointing "towards $B$" — a rotation by $\pi/2$ counterclockwise (when viewed from outside the sphere).

> [!note]- Derivation
> The cleanest way to track parallel transport at a vertex is to use a *parallel orthonormal frame* along each segment. On a geodesic, the velocity $\dot\gamma$ (unit-speed) and its left perpendicular $\dot\gamma^\perp$ form a parallel orthonormal frame. At a vertex where two geodesics meet at angle $\alpha$ (interior angle), the change from the incoming parallel frame to the outgoing parallel frame is a rotation by $\pi - \alpha$ (the turning angle). The total rotation around the loop is the sum of turning angles, which for a polygon is $2\pi - \sum\alpha_i$ (the exterior-angle sum). For a closed loop on a flat plane this is $2\pi$ (Euclidean); for a loop on a curved surface, the difference $\sum(\pi - \alpha_i) - 2\pi = -\sum\alpha_i + \pi(n - 2)$ (Euclidean defect for an $n$-gon) needs to be corrected by the integrated curvature.
>
> For a geodesic triangle: $n = 3$ interior angles summing to $\pi$ in the flat case. On a curved surface, $\sum\alpha_i - \pi = \int K\,dA$ (Gauss-Bonnet). Here $\sum\alpha_i = 3(\pi/2) = 3\pi/2$, so $\int K\,dA = 3\pi/2 - \pi = \pi/2$. This is the **angle defect**, which equals the *holonomy angle* of parallel transport around the loop.
>
> Computing directly: starting vector at $N$, transported around the loop, returns rotated by the angle defect $\pi/2$. The sign convention: the rotation is counterclockwise when viewed from outside the sphere (the natural orientation of the loop).

**Step 3: Verify via Gauss-Bonnet.**

The triangle $NAB$ is the spherical region $\{(\theta, \varphi) : 0 \leq \theta \leq \pi/2, 0 \leq \varphi \leq \pi/2\}$ — one octant of the sphere. Its area (using $dA = \sin\theta\,d\theta\,d\varphi$):
$$
\text{Area} = \int_0^{\pi/2}\int_0^{\pi/2}\sin\theta\,d\theta\,d\varphi = \int_0^{\pi/2}d\varphi \cdot \int_0^{\pi/2}\sin\theta\,d\theta = (\pi/2)(1) = \pi/2.
$$
On the unit sphere $K = 1$, so $\int_T K\,dA = \pi/2$. This is the **holonomy angle** by the Gauss-Bonnet formula applied to a geodesic triangle: $\text{holonomy} = \int_T K\,dA = \pi/2$. ✓ Matches Step 2.

> [!note]- Derivation
> The Gauss-Bonnet formula for a geodesic polygon on a Riemannian 2-manifold: $\int_D K\,dA = \sum_i \alpha_i - (n-2)\pi$ where $\alpha_i$ are the interior angles and $n$ is the number of vertices. For our triangle ($n = 3$, all $\alpha_i = \pi/2$): RHS = $3(\pi/2) - \pi = \pi/2$. LHS (since $K = 1$): area of the triangle. So area = $\pi/2$, consistent with one octant of the unit sphere (total area $4\pi$, divided by 8 = $\pi/2$). The angle defect = the integrated curvature = the holonomy.

> [!note]- Complete formal solution
> **The geodesic triangle $NAB$ on the unit sphere.** Vertices $N$ (north pole), $A = (\pi/2, 0)$, $B = (\pi/2, \pi/2)$. Sides are great-circle arcs: meridian $NA$ at $\varphi = 0$, equator $AB$ from $\varphi = 0$ to $\varphi = \pi/2$, meridian $BN$ at $\varphi = \pi/2$. All three interior angles are $\pi/2$.
>
> **Holonomy via segment-by-segment parallel transport.** Along each geodesic segment, parallel transport preserves angles to the velocity vector. At each vertex with interior angle $\alpha$, the parallel-transported vector picks up a turn of $\pi - \alpha$ relative to the new geodesic's velocity. Around the loop, the total turn is $\sum(\pi - \alpha_i) = 3\pi - 3(\pi/2) = 3\pi/2$. Subtracting the "trivial" loop rotation $2\pi$ (which a parallel-transported vector picks up around a flat-plane loop with zero defect): the parallel-transport rotation is $3\pi/2 - 2\pi = -\pi/2$, i.e., the vector returns rotated by $\pi/2$ in the *opposite* sense to the loop traversal. The magnitude of the holonomy angle is $\pi/2$.
>
> **Holonomy via Gauss-Bonnet.** Area of the spherical triangle (one octant of the unit sphere): $\pi/2$. Integrated curvature $\int_T K\,dA = (1)(\pi/2) = \pi/2$. By the Gauss-Bonnet formula for geodesic polygons, this equals the angle defect $\sum\alpha_i - (n-2)\pi = 3(\pi/2) - \pi = \pi/2$. ✓
>
> The holonomy angle of parallel transport around the geodesic triangle is **$\pi/2$**. $\blacksquare$

---

# Key Takeaways

**On a 2D Riemannian manifold, the holonomy around a closed loop equals the integrated Gaussian curvature inside.** This is one of the most beautiful and useful identities in differential geometry. It says that the **global** holonomy is determined by the **local** curvature, integrated. The proof goes via the orthonormal-frame formulation: parallel transport in 2D is rotation by some angle, and the angle is the integral of the connection 1-form around the loop, which by Stokes' theorem equals the integral of the curvature 2-form inside. For 2D, the curvature 2-form is $K\,dA$, giving the formula. The reusable insight: whenever you have a closed loop on a 2D Riemannian manifold and want to know the holonomy, just integrate $K\,dA$ — no need to solve the parallel-transport ODE. This generalises in higher dimensions: holonomy around a small loop is approximated by the curvature operator $R(X, Y)$ to leading order, with the integrated curvature being the global generalisation.

**Geodesic triangles have angle defect equal to the integrated curvature.** On a flat plane, geodesic triangle angles sum to $\pi$. On a positively curved surface (sphere), the angles sum to *more* than $\pi$, with the excess equal to the integrated curvature (the area of the triangle on the unit sphere). On a negatively curved surface (hyperbolic plane), the angles sum to *less* than $\pi$. The deviation is the **Gauss-Bonnet defect**. For the unit sphere, the maximum triangle has total angle close to $3\pi$ (covering almost the whole sphere), giving total area close to $4\pi$. This is one of the cleanest tests of curvature: "stand on a surface, draw a geodesic triangle, measure the angles, and the defect tells you the integrated curvature".

**Parallel transport along a geodesic is rotation aligned with the velocity — the cleanest building block.** The reason the segment-by-segment computation worked is that parallel transport along a *geodesic* is fully constrained by one fact: the velocity itself is parallel. So any tangent vector $v$ decomposes into a component along $\dot\gamma$ (parallel-transported as a multiple of $\dot\gamma$) and a component perpendicular (parallel-transported as a multiple of $\dot\gamma^\perp$, with the perpendicular direction itself parallel-transported). On a geodesic, parallel transport is just "drag the orthonormal frame along". The complications arise only at vertices, where the two meeting geodesics have different velocities, and one must rotate the frame from the incoming to the outgoing velocity. This trick — using geodesic segments and tracking the vertex rotations — is the standard approach to all holonomy calculations on 2D surfaces.

**Foucault's pendulum experiment is exactly this — parallel transport around a latitude circle.** The pendulum at latitude $\theta_0$ has its swing direction parallel-transported (approximately, ignoring damping and Earth's gravity) along the daily circle of constant latitude. The holonomy angle per day is $2\pi(1 - \cos\theta_0)$, which is the integrated Gaussian curvature of the spherical cap above the latitude $\theta_0$: $\int_{\text{cap}} K\,dA = 2\pi(1 - \cos\theta_0)$ on the unit sphere. At the pole ($\theta_0 = 0$) the holonomy is $2\pi(1 - 1) = 0$ (no rotation — the cap is a point), wait that's the cap area zero. Let me recompute: the cap above latitude $\theta_0$ has area $2\pi(1 - \cos\theta_0)$ on the unit sphere; the latitude circle bounds this cap with holonomy = cap area = $2\pi(1 - \cos\theta_0)$. At the equator ($\theta_0 = \pi/2$, $\cos = 0$): holonomy $2\pi$, full rotation per day. At the pole ($\theta_0 = 0$, $\cos = 1$): holonomy $0$, no rotation. Foucault's experiment at latitude $\theta_0 = 48°$ in Paris gave rotation rate of about $2\pi(1 - \cos 48°)/24\,\text{hr} \approx 11°/\text{hr}$. This is the cleanest physical demonstration of parallel transport, and it is the same computation as the triangle holonomy in this exercise.
