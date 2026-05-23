---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Differential Form"
  - "Def - The Exterior Derivative"
  - "Thm - The General Stokes Theorem"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $\Omega \subseteq \mathbb{R}^2$ is a compact region with piecewise-$C^1$ boundary $\partial\Omega$, oriented counterclockwise (the induced orientation, keeping $\Omega$ on the left). Functions $f, g$ (or $P, Q$) are $C^1$ on $\Omega$. A vector field is $X = (X_1, X_2)$; $\operatorname{div} X = \partial_x X_1 + \partial_y X_2$; $\operatorname{curl} X = \partial_x X_2 - \partial_y X_1$ (the scalar planar curl); $\nu$ is the outward unit normal, $\tau$ the forward unit tangent. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Statement

> **Green's Theorem.** Let $\Omega \subseteq \mathbb{R}^2$ be a compact region with piecewise-$C^1$ boundary $\partial\Omega$, oriented counterclockwise, and let $f, g$ be $C^1$ functions on a neighbourhood of $\Omega$. Then
> $$\iint_\Omega\Big(\frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}\Big)\,dx\,dy = \oint_{\partial\Omega}\big(f\,dx + g\,dy\big).$$
>
> **Divergence form.** Writing $g = X_1$, $f = -X_2$ for a vector field $X = (X_1, X_2)$,
> $$\iint_\Omega\operatorname{div} X\;dx\,dy = \oint_{\partial\Omega} X\cdot\nu\;ds.$$
>
> **Curl (circulation) form.** Writing $f = X_1$, $g = X_2$,
> $$\iint_\Omega\operatorname{curl} X\;dx\,dy = \oint_{\partial\Omega} X\cdot\tau\;ds.$$
>
> **Area corollary.** Taking $f = 0, g = x$ (or $f = -y, g = 0$, or the average),
> $$\operatorname{area}(\Omega) = \oint_{\partial\Omega} x\,dy = -\oint_{\partial\Omega} y\,dx = \frac{1}{2}\oint_{\partial\Omega}(x\,dy - y\,dx).$$

---

# Motivation

Green's theorem is the first place the abstract promise of the calculus of forms — that integrating a derivative over a region reduces to a boundary integral — becomes a concrete, computable tool. The question it answers is practical: *given a double integral over a planar region, can it be turned into a single integral over the boundary curve, and vice versa?* The answer is yes whenever the integrand of the double integral has the shape of a planar curl, and the trade is often enormously favourable — a curve is one-dimensional, a region two-dimensional, and the easier of the two is the one you compute.

There is a second motivation, more conceptual. Before forms, the divergence theorem and the Kelvin-Stokes theorem in the plane looked like two different statements: one about outflow across a boundary, one about circulation along it. Green's theorem reveals they are *the same statement*. The single identity $\iint_\Omega(\partial_x g - \partial_y f) = \oint_{\partial\Omega}(f\,dx + g\,dy)$, read with one assignment of $f, g$ to a vector field, is the planar divergence theorem; read with the other assignment, it is the planar circulation theorem. The choice of which classical theorem you are looking at is just a relabelling. This is the first concrete payoff of the unifying frame: Green's theorem is the $2$-dimensional case of [[Thm - The General Stokes Theorem|the general Stokes theorem]], obtained by taking $\beta = f\,dx + g\,dy$ and noting $d\beta = (\partial_x g - \partial_y f)\,dx\wedge dy$.

The area corollary deserves its own sentence of motivation. It says the area of a region — an honestly two-dimensional quantity — can be computed by walking around the boundary and accumulating a single integral. This is not a curiosity: it is the principle behind the planimeter, the mechanical instrument that measures the area of a shape by tracing its outline, and behind every algorithm that computes the area of a polygon from its vertices.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$: *$\Omega$ is a compact planar region with piecewise-$C^1$ boundary, oriented counterclockwise, and the integrand has the form of a planar curl or divergence.*

The first disguised source is **a region given by inequalities or as the area between curves**. The property $B$: "$\Omega = \{a \le x \le b,\ \phi(x) \le y \le \psi(x)\}$ or a finite union of such." The bridge: such a region has a piecewise-$C^1$ boundary (the two graphs plus two vertical segments), so Green's theorem applies; the orientation is counterclockwise. The non-obvious step is recognizing that an *elementary region* — the kind double integrals are routinely set up over — automatically satisfies the boundary hypothesis. *Example problem:* converting a double integral over a region between two parabolas into a boundary line integral.

The second disguised source is **a double integral whose integrand is a difference of partial derivatives**. The property $B$: "the integrand is $\partial_x g - \partial_y f$ for some $C^1$ functions, or can be made so by solving $\partial_x g =$ (part of the integrand)." The bridge: any integrand of this shape is $d\beta$ for $\beta = f\,dx + g\,dy$, so Green converts it to $\oint\beta$. The non-obviousness: a generic-looking integrand may secretly be a curl, found by *antidifferentiating* — given an integrand $h$, look for $g$ with $\partial_x g = h$ and set $f = 0$. *Example problem:* an integrand $2$ is $\partial_x(2x) - \partial_y(0)$, so $\iint_\Omega 2 = \oint 2x\,dy$, giving twice the area.

The third disguised source is **a closed curve along which you want to integrate**. The property $B$: "a piecewise-$C^1$ closed curve $\gamma$ and a vector field defined on the region it bounds." The bridge: the curve is the boundary of a planar region, and Green converts the line integral $\oint_\gamma$ into a double integral. The non-obvious step is the reverse direction — recognizing that a *circulation* around a loop is best evaluated as a double integral of the curl. *Example problem:* the work of a field around a closed loop, computed by integrating its curl over the enclosed region.

**Targets (Output Amplification)**

The conclusion $C$: the equality of a double integral and a boundary line integral.

Combine $C$ with **an integrand that is identically $1$**. If the double integral's integrand is the constant $1$, then $\iint_\Omega 1 = \operatorname{area}(\Omega)$, and $C$ expresses the area as a boundary integral $\oint_{\partial\Omega}(x\,dy - y\,dx)/2$. The further result $E$ is the **area formula**: a two-dimensional measurement reduced to a one-dimensional integral, computable from a parametrization of the boundary alone. The non-obviousness: area, intrinsically a region quantity, is recoverable from boundary data.

Combine $C$ with **a curl-free field on the region**. If $\operatorname{curl} X = 0$ throughout $\Omega$, the curl form of $C$ gives $\oint_{\partial\Omega} X\cdot\tau\,ds = 0$ — every closed line integral of $X$ vanishes. The further result $E$, combined with the [[Thm - The Poincaré Lemma|Poincaré lemma]], is that $X$ is conservative on $\Omega$ (has a potential), provided $\Omega$ is simply connected. The non-obviousness: a local condition (vanishing curl) plus a topological condition (simple connectivity) yields a global conclusion (path-independence).

Combine $C$ with **a singular point excised from the region**. If a field has a singularity inside $\Omega$, apply $C$ to the region with a small disk removed; the boundary now has two components, and $C$ relates the outer circulation to the circulation around the singularity. The further result $E$ is that the integral around a small loop encircling the singularity is a well-defined invariant — the residue, or the period — independent of the loop's size. This is the mechanism behind the angular form's nonzero period in [[Ex - A closed form that is not exact]].

---

# Why Is It True

Green's theorem is true for the same reason every Stokes-type theorem is true: the contributions from the interior of the region cancel, and only the boundary survives. But in the plane the mechanism can be seen with no machinery at all, by slicing.

Take the simplest piece of the theorem, $\iint_\Omega\partial_y f\,dx\,dy = -\oint_{\partial\Omega} f\,dx$, and suppose $\Omega$ is the region between two graphs, $\phi(x) \le y \le \psi(x)$ for $x \in [a,b]$. Slice the region into thin vertical strips. On one strip at horizontal position $x$, integrate $\partial_y f$ in $y$ from $\phi(x)$ to $\psi(x)$: the Fundamental Theorem of Calculus collapses this to $f(x, \psi(x)) - f(x, \phi(x))$ — the values of $f$ at the *top and bottom* of the strip, where the strip meets the boundary. The interior of the strip contributes nothing net; only its two boundary endpoints do. Now integrate over all strips, i.e. over $x$: you accumulate $\int_a^b[f(x,\psi) - f(x,\phi)]\,dx$, which is precisely the line integral of $f\,dx$ along the bottom edge minus along the top edge — that is, $-\oint f\,dx$ around the boundary with the correct counterclockwise orientation. The vertical edges contribute nothing because $dx = 0$ along them. So the double integral became a boundary integral by the one-variable Fundamental Theorem of Calculus applied slice by slice.

The other half, $\iint_\Omega\partial_x g = \oint g\,dy$, is the same argument with horizontal strips. Adding the two halves gives the full theorem. The deep point — and the reason this is "really" Stokes — is that each slice computation is the Fundamental Theorem of Calculus in one transverse direction, and the integration over the remaining direction just sweeps the boundary. The general Stokes theorem is this picture made dimension-independent: interior cancels, boundary survives, with the one-variable Fundamental Theorem doing the work in the transverse direction. One should *expect* Green's theorem to hold because slicing always reduces a planar double integral to a stack of one-variable integrals, and the Fundamental Theorem of Calculus always turns a one-variable integral of a derivative into boundary data.

---

# What Makes This Hard

The genuine subtlety is not the proof for a simple region — which is the slicing argument above — but **handling regions that are not simple**: regions with holes, or with boundaries that are not single graphs. The standard resolution, and the step most often fumbled, is to **decompose $\Omega$ into simple pieces** and observe that the line integrals along the internal cuts cancel in pairs (each cut is traversed twice, in opposite directions). The second common error is **orientation of the boundary**: the theorem holds with the counterclockwise (region-on-the-left) orientation, and using the clockwise orientation silently negates the right-hand side; for a region with a hole, the *inner* boundary must be traversed *clockwise* for the induced orientation to be consistent.

---

# Rederivation Scaffold

**High-level strategy:** Recognize Green's theorem as the $2$-dimensional case of the general Stokes theorem with $\beta = f\,dx + g\,dy$; or, self-contained, prove it by slicing a simple region and applying the Fundamental Theorem of Calculus, then extend to general regions by decomposition.

**Subgoal decomposition:**

1. **Identify the form.** Set $\beta = f\,dx + g\,dy$ and compute $d\beta = (\partial_x g - \partial_y f)\,dx\wedge dy$.
   - *Hint:* The exterior derivative of a $1$-form in two variables has a single coefficient.
   - *Why needed:* It exhibits the integrand of the double integral as $d\beta$, so Green's theorem becomes $\int_\Omega d\beta = \int_{\partial\Omega}\beta$.

2. **Prove the simple-region case by slicing.** For $\Omega = \{\phi(x) \le y \le \psi(x)\}$, show $\iint_\Omega\partial_y f = -\oint f\,dx$ by integrating in $y$ first (Fundamental Theorem of Calculus) then in $x$; similarly $\iint_\Omega\partial_x g = \oint g\,dy$.
   - *Hint:* The $y$-integral of $\partial_y f$ is $f(x,\psi) - f(x,\phi)$; recognize the result as a line integral along top and bottom edges.
   - *Why needed:* It is the base case; the vertical edges contribute zero because $dx = 0$ there.

3. **Extend to general regions by decomposition.** Cut $\Omega$ into finitely many simple pieces; apply step 2 to each; sum.
   - *Hint:* Internal cut segments are traversed twice with opposite orientation and cancel.
   - *Why needed:* It removes the "simple region" restriction, covering regions with holes and complicated boundaries.

---

# Lemma Decomposition

> [!note]- Lemma 1: Green's theorem for the $\partial_y f$ half on a vertically simple region
> **Statement:** If $\Omega = \{(x,y) : a \le x \le b,\ \phi(x) \le y \le \psi(x)\}$ with $\phi, \psi$ piecewise $C^1$, then $\iint_\Omega\partial_y f\,dx\,dy = -\oint_{\partial\Omega} f\,dx$.
>
> **Hint:** Integrate in $y$ first by the Fundamental Theorem of Calculus, then read the result as a line integral.
>
> **Why needed:** It is one of the two halves of the simple-region case; the other is symmetric.
>
> > [!note]- Full proof
> > By Fubini, $\iint_\Omega\partial_y f\,dx\,dy = \int_a^b\Big(\int_{\phi(x)}^{\psi(x)}\partial_y f\,dy\Big)dx = \int_a^b\big[f(x,\psi(x)) - f(x,\phi(x))\big]\,dx$, the inner integral by the Fundamental Theorem of Calculus. Now $\int_a^b f(x,\phi(x))\,dx$ is the line integral of $f\,dx$ along the bottom edge (traversed left-to-right, the counterclockwise direction), and $\int_a^b f(x,\psi(x))\,dx$ is the integral along the top edge traversed left-to-right — which is *against* the counterclockwise direction. So $\oint_{\partial\Omega} f\,dx = \int_{\text{bottom}} - \int_{\text{top, L-to-R}} + \int_{\text{verticals}}$. Along the vertical edges $x$ is constant so $dx = 0$ and they contribute nothing. Hence $\oint_{\partial\Omega} f\,dx = \int_a^b f(x,\phi) - \int_a^b f(x,\psi) = -\iint_\Omega\partial_y f$. $\square$

> [!note]- Lemma 2: Internal cuts cancel under decomposition
> **Statement:** If $\Omega = \Omega_1 \cup \Omega_2$ with $\Omega_1, \Omega_2$ meeting along a common boundary arc $\sigma$, then $\oint_{\partial\Omega_1}\beta + \oint_{\partial\Omega_2}\beta = \oint_{\partial\Omega}\beta$.
>
> **Hint:** The arc $\sigma$ appears in $\partial\Omega_1$ and in $\partial\Omega_2$ with opposite orientations.
>
> **Why needed:** It is what lets the simple-region case be assembled into the general theorem.
>
> > [!note]- Full proof
> > The boundary $\partial\Omega_1$ consists of an outer part (a piece of $\partial\Omega$) and the cut arc $\sigma$; likewise $\partial\Omega_2$. With the counterclockwise (region-on-left) orientation, the cut $\sigma$ is traversed in one direction as part of $\partial\Omega_1$ and in the *opposite* direction as part of $\partial\Omega_2$ — because $\Omega_1$ lies on one side of $\sigma$ and $\Omega_2$ on the other. The line integral along $\sigma$ therefore appears with $+$ in $\oint_{\partial\Omega_1}$ and $-$ in $\oint_{\partial\Omega_2}$, and the two cancel. What remains is the sum of the outer parts, which is exactly $\oint_{\partial\Omega}\beta$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> **Via the general Stokes theorem.** Let $\beta = f\,dx + g\,dy$, a $1$-form on a neighbourhood of $\Omega$. Its exterior derivative is
> $$d\beta = df\wedge dx + dg\wedge dy = (\partial_y f\,dy)\wedge dx + (\partial_x g\,dx)\wedge dy = (\partial_x g - \partial_y f)\,dx\wedge dy,$$
> using $dy\wedge dx = -dx\wedge dy$ and discarding $dx\wedge dx = dy\wedge dy = 0$. By [[Thm - The General Stokes Theorem|the general Stokes theorem]] applied to the compact oriented $2$-surface $\Omega$ with boundary $\partial\Omega$,
> $$\iint_\Omega(\partial_x g - \partial_y f)\,dx\,dy = \int_\Omega d\beta = \int_{\partial\Omega}\beta = \oint_{\partial\Omega}(f\,dx + g\,dy).$$
>
> **Self-contained proof by slicing.** Assume first $\Omega$ is *vertically simple*, $\Omega = \{a \le x \le b,\ \phi(x) \le y \le \psi(x)\}$. By Lemma 1, $\iint_\Omega\partial_y f\,dx\,dy = -\oint_{\partial\Omega} f\,dx$. By the symmetric argument with horizontal strips (valid when $\Omega$ is also *horizontally simple*), $\iint_\Omega\partial_x g\,dx\,dy = \oint_{\partial\Omega} g\,dy$. Adding,
> $$\iint_\Omega(\partial_x g - \partial_y f)\,dx\,dy = \oint_{\partial\Omega}(f\,dx + g\,dy).$$
> For a general region with piecewise-$C^1$ boundary, decompose $\Omega$ into finitely many pieces each both vertically and horizontally simple; the identity holds on each piece, and by Lemma 2 the internal cut integrals cancel when summed, leaving the identity for $\Omega$. $\blacksquare$
>
> **The divergence and curl forms.** Setting $g = X_1, f = -X_2$: $\partial_x g - \partial_y f = \partial_x X_1 + \partial_y X_2 = \operatorname{div} X$, and $f\,dx + g\,dy = -X_2\,dx + X_1\,dy$, which along an arc-length parametrization equals $X\cdot\nu\,ds$ with $\nu = (y', -x')$ the outward normal. Setting $f = X_1, g = X_2$: $\partial_x g - \partial_y f = \operatorname{curl} X$, and $f\,dx + g\,dy = X_1\,dx + X_2\,dy = X\cdot\tau\,ds$ with $\tau$ the unit tangent.
>
> **The area corollary.** Take $f = 0, g = x$: $\partial_x g - \partial_y f = 1$, so $\iint_\Omega 1 = \oint x\,dy$, i.e. $\operatorname{area}(\Omega) = \oint_{\partial\Omega} x\,dy$. Take $f = -y, g = 0$: similarly $\operatorname{area}(\Omega) = -\oint y\,dx$. Averaging the two gives $\operatorname{area}(\Omega) = \tfrac12\oint(x\,dy - y\,dx)$.

---

# Cross-Field Exercise Suggestions

**The planimeter.** A planimeter is a mechanical device that computes the area of a region by tracing its boundary. Its operation is the area corollary of Green's theorem made physical: as the tracer follows $\partial\Omega$, a wheel accumulates the integral $\oint(x\,dy - y\,dx)/2$. The application is striking because a purely mechanical instrument *is* an analog computer for a line integral, and Green's theorem certifies that the line integral is the area.

**The argument principle in complex analysis.** For a holomorphic function $h$, the number of zeros inside a contour is $\frac{1}{2\pi i}\oint_\gamma h'/h\,dz$. Splitting into real and imaginary parts and applying Green's theorem connects this contour integral to a double integral, and the integer-valuedness is the winding-number phenomenon. The application is nonobvious because a *counting* statement about zeros is extracted from a Green's-theorem identity.

**The Bobillier / shoelace formula for polygon area.** For a polygon with vertices $(x_1, y_1), \dots, (x_n, y_n)$, the area is $\tfrac12\big|\sum(x_i y_{i+1} - x_{i+1} y_i)\big|$. This is exactly the area corollary $\tfrac12\oint(x\,dy - y\,dx)$ evaluated on the piecewise-linear boundary, the integral over each edge being an elementary computation. The application is everyday — every computational geometry library uses it — and it is Green's theorem on a polygonal domain.

**Vorticity and circulation in fluid dynamics.** For a planar fluid flow with velocity field $X$, the curl $\operatorname{curl} X$ is the vorticity, and the curl form of Green's theorem says the total vorticity inside a region equals the circulation of the flow around its boundary. The application is foundational to fluid mechanics: it is why vorticity is the *local* density of circulation, and it underlies Kelvin's circulation theorem.

---

# Bridges

- **[[Thm - The General Stokes Theorem|The General Stokes Theorem]]** — Green's theorem is its $2$-dimensional case, obtained by taking $\beta = f\,dx + g\,dy$. Everything specific to Green's theorem — the $\partial_x g - \partial_y f$ integrand, the counterclockwise orientation — is the general theorem specialized to a planar region.

- **[[Thm - The Divergence Theorem|The Divergence Theorem]] and [[Thm - The Kelvin-Stokes Theorem|the Kelvin-Stokes Theorem]]** — the divergence form of Green's theorem *is* the divergence theorem in dimension two; the curl form *is* the Kelvin-Stokes theorem for a planar surface. Green's theorem is the one identity from which both classical planar theorems are read by relabelling.

- **The Fundamental Theorem of Calculus** — the engine of the slicing proof. Each vertical or horizontal slice reduces to a one-variable integral of a derivative, evaluated by the Fundamental Theorem; Green's theorem is that theorem swept across the second variable.

- **The Jordan curve theorem** — Green's theorem presupposes that a simple closed curve bounds a well-defined region with an inside and an outside. The Jordan curve theorem is what guarantees this, and the rotation number / winding number used in its proof is itself computed by a Green's-theorem flux integral.

---

# Unlocked by This

> [!tip] Cauchy's Integral Theorem *(from Complex Analysis)*
> A holomorphic function gives a closed $1$-form $h(z)\,dz$ (closedness is the Cauchy-Riemann equations), and Green's theorem applied to its real and imaginary parts yields $\oint_\gamma h\,dz = 0$ for a contractible contour — **Cauchy's integral theorem**, the foundation of complex analysis.

> [!tip] Conservation Laws in the Plane *(from Continuum Mechanics)*
> The divergence form of Green's theorem is the integral balance law: the rate of accumulation of a conserved quantity in a region equals its flux across the boundary. This is the planar prototype of every continuity equation in fluid dynamics and electromagnetism.
