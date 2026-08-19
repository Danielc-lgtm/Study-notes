---
type: remark
subject: hyperbolic-geometry
prereqs:
  - "Def - Hyperbolic Plane"
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §3.0 — placing a primitive hyperbolic in standard form as coordinates on its axis"
---

# Notation

- $\mathbb{H}^2 = \{z = x + iy \in \mathbb{C} : y > 0\}$ — the upper half-plane, metric $ds^2 = (dx^2 + dy^2)/y^2$.
- $\mathrm{PSL}(2, \mathbb{R})$ — the orientation-preserving isometry group of $\mathbb{H}^2$, acting by Möbius transformations $z \mapsto (az + b)/(cz + d)$ with $ad - bc = 1$; elements identified modulo $\pm I$.
- $\tau \in \mathrm{PSL}(2, \mathbb{R})$ — a **hyperbolic** isometry: it has two distinct fixed points on the boundary circle $\partial\mathbb{H}^2 = \mathbb{R} \cup \{\infty\}$, both real, no fixed point inside $\mathbb{H}^2$; equivalently $|\mathrm{tr}\,\tau| > 2$.
- **Axis of $\tau$** — the unique geodesic in $\mathbb{H}^2$ joining $\tau$'s two boundary fixed points; it is the set of interior points $z \in \mathbb{H}^2$ with $d(z, \tau z)$ *minimal*, and the minimum equals the translation length.
- $\ell = \ell_\tau > 0$ — the **translation length** of $\tau$: the hyperbolic distance $\tau$ moves any point on its axis.
- $\tau_0 : z \mapsto e^\ell z$ — the **standard form** of a hyperbolic isometry with translation length $\ell$; represented by the matrix $\mathrm{diag}(e^{\ell/2}, e^{-\ell/2}) \in \mathrm{PSL}(2, \mathbb{R})$.
- $\gamma$ — the closed geodesic on $X = \Gamma\backslash\mathbb{H}^2$ arising as the projection of the axis; length $\ell_\gamma = \ell$.
- $\mathcal{F}_\tau = \{z \in \mathbb{H}^2 : 1 \le \mathrm{Im}\,z < e^\ell\}$ — the fundamental strip of $\langle\tau_0\rangle$.

> [!recall]- Hyperbolic isometry of $\mathbb{H}^2$
> **Formally:** an element $\tau \in \mathrm{PSL}(2, \mathbb{R})$ is *hyperbolic* if $|\mathrm{tr}\,\tau| > 2$. Equivalently: its two fixed points $p_-, p_+$ lie on $\partial\mathbb{H}^2 = \mathbb{R} \cup \{\infty\}$, are distinct and real, and no point inside $\mathbb{H}^2$ is fixed. The unique geodesic joining $p_-$ to $p_+$ is $\tau$'s *axis*, and $\tau$ acts on the axis by translation of a fixed hyperbolic distance $\ell > 0$ — the translation length.
> **In words:** hyperbolic elements are the "slide-along-a-geodesic" isometries. They pick a specific geodesic (the axis) and shift every point on it by a fixed distance $\ell$. Off the axis, points are dragged along parallel curves (equidistants), and the displacement $d(z, \tau z) \ge \ell$ with equality iff $z$ is on the axis.
> **Concretely:** the matrix $\mathrm{diag}(e^{\ell/2}, e^{-\ell/2})$ acts by $z \mapsto e^\ell z$ (dividing top by bottom). Its fixed points are $0$ and $\infty$; the axis is the imaginary half-line $\{iy : y > 0\}$; the distance from $iy$ to $e^\ell (iy) = i e^\ell y$ along the axis is $\int_y^{e^\ell y} du/u = \ell$. See [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length]].

> [!recall]- Möbius action of $\mathrm{PSL}(2, \mathbb{R})$ on $\mathbb{H}^2$
> **Formally:** $\mathrm{PSL}(2, \mathbb{R})$ acts by $\begin{pmatrix} a & b \\ c & d\end{pmatrix} \cdot z = (az + b)/(cz + d)$; the action is transitive on $\mathbb{H}^2$ (any point to any point) and preserves the metric $ds^2 = (dx^2 + dy^2)/y^2$. Conjugation in $\mathrm{PSL}(2, \mathbb{R})$ is a change of coordinates: $q \tau q^{-1}$ acts on $q(z)$ the way $\tau$ acts on $z$; in particular, conjugating by any isometry $q$ that sends the axis of $\tau$ to the axis of $q \tau q^{-1}$ produces the same abstract action written in new coordinates.
> **In words:** $\mathrm{PSL}(2, \mathbb{R})$ is rich enough to move any geodesic (a half-circle or vertical line) to any other by a single isometry — so any axis can be moved to the imaginary axis by a suitable conjugation.
> **Concretely:** the isometry $q(z) = -1/z$ sends $0 \leftrightarrow \infty$ (swapping the two ends of the imaginary axis, reversing its orientation); the isometry $q(z) = z + a$ (real $a$) translates points and sends the vertical geodesic $x = 0$ to $x = a$.

---

# Claim / Identity

> **Claim (standard form as coordinates on the axis).** Every hyperbolic $\tau \in \mathrm{PSL}(2, \mathbb{R})$ with translation length $\ell > 0$ is $\mathrm{PSL}(2, \mathbb{R})$-conjugate to
> $$\tau_0 : z \mapsto e^\ell z, \tag{$\star$}$$
> whose axis is the imaginary half-line $\{iy : y > 0\}$ and whose translation length along that axis is exactly $\ell$. Under this conjugation:
> 1. $\tau_0$ acts on imaginary parts by rescaling: $\mathrm{Im}(\tau_0 z) = e^\ell\,\mathrm{Im}(z)$.
> 2. The orbits of the cyclic subgroup $\langle\tau_0\rangle$ in $\mathbb{H}^2$ are geometric sequences in $\mathrm{Im}(z)$: $\{e^{k\ell} z : k \in \mathbb{Z}\}$, one representative per orbit lying in the horizontal band $1 \le \mathrm{Im}(z) < e^\ell$.
> 3. The band $\mathcal{F}_\tau = \{z : 1 \le \mathrm{Im}(z) < e^\ell\}$ is a fundamental region for $\langle\tau_0\rangle$ on $\mathbb{H}^2$.
> 4. For any $\Gamma$-invariant kernel $p^E_{\mathbb{H}^2}$, the strip integral $\int_{\mathcal{F}_\tau} p^E_{\mathbb{H}^2}(t, z, \tau^m z)\,d\rho_{\mathbb{H}^2}(z)$ is coordinate-independent: replacing $\tau$ with $q\tau q^{-1}$ (any $q \in \mathrm{PSL}(2, \mathbb{R})$) and $\mathcal{F}_\tau$ with $q\mathcal{F}_\tau$ leaves the integral unchanged.

---

# In One Line

The "diagonal" form $z \mapsto e^\ell z$ is the natural coordinate for a primitive hyperbolic element because it makes its axis (the imaginary half-line) and its action (multiplication of $\mathrm{Im}(z)$ by $e^\ell$) trivially visible, turning every $\langle\tau\rangle$-orbit into a geometric sequence in $\mathrm{Im}(z)$ and every fundamental region into a horizontal band; this is why the paper's strip-integral formula for a class-mass takes its clean explicit form.

---

# Why It's True

**Mechanism (one sentence).** *Every hyperbolic isometry of $\mathbb{H}^2$ has an axis; any $\mathrm{PSL}(2, \mathbb{R})$-isometry sending that axis to the imaginary half-line conjugates $\tau$ into standard form, and $\Gamma$-invariance of the kernel makes the strip integral independent of which such coordinate system we chose.*

Two facts do all the work:

1. **$\mathrm{PSL}(2, \mathbb{R})$ acts transitively on geodesics** of $\mathbb{H}^2$ (any half-circle or vertical line can be sent to any other by an isometry). So the axis of $\tau$ can be moved to the imaginary axis by a single isometry $q \in \mathrm{PSL}(2, \mathbb{R})$; after conjugating by $q$, the new element $q\tau q^{-1}$ has the imaginary axis as its axis and acts on it by translating a distance $\ell$ — the only such element (with the given orientation) is $z \mapsto e^\ell z$.

2. **The strip integral is a conjugation-invariant.** Applying an isometry $q^{-1}$ to the whole integrand (substitute $w = q^{-1} z$, Jacobian 1) rewrites $\int_{\mathcal{F}_\tau} p^E_{\mathbb{H}^2}(t, z, \tau^m z)\,d\rho_{\mathbb{H}^2}(z)$ as $\int_{q^{-1}\mathcal{F}_\tau} p^E_{\mathbb{H}^2}(t, w, q^{-1}\tau^m q\,w)\,d\rho_{\mathbb{H}^2}(w)$ — the same integral written in the standard-form coordinates.

The upshot is that **coordinates are a choice, not a datum**, and the paper's choice of $\tau_0 : z \mapsto e^\ell z$ is the coordinate in which the geometry becomes trivial to compute in: $\langle\tau_0\rangle$-orbits are geometric sequences in $y = \mathrm{Im}(z)$, so a fundamental region is a horizontal band (a "period" of the rescaling), which unrolls to a cylinder.

---

# Derivation

> [!note]- Gap-free derivation
> **Step 1 — every hyperbolic element has a two-endpoint axis.** Let $\tau \in \mathrm{PSL}(2, \mathbb{R})$ with $|\mathrm{tr}\,\tau| > 2$. Lift to $\tilde\tau \in \mathrm{SL}(2, \mathbb{R})$; the characteristic polynomial $\lambda^2 - (\mathrm{tr}\,\tilde\tau)\lambda + 1 = 0$ has two distinct real roots $\lambda_\pm$ with $\lambda_+ \lambda_- = 1$ and $|\lambda_+| > 1 > |\lambda_-|$. The eigenvectors give two distinct real lines in $\mathbb{R}^2$, hence two distinct points $p_\pm \in \partial\mathbb{H}^2 = \mathbb{R} \cup \{\infty\}$ fixed by $\tau$. The unique geodesic in $\mathbb{H}^2$ joining $p_-$ to $p_+$ is $\tau$'s axis.
>
> **Step 2 — any two boundary pairs are $\mathrm{PSL}(2, \mathbb{R})$-related.** $\mathrm{PSL}(2, \mathbb{R})$ acts triply transitively on the boundary circle $\partial\mathbb{H}^2$; in particular, given two ordered distinct pairs $(p_-, p_+)$ and $(0, \infty)$ on $\mathbb{R} \cup \{\infty\}$, there is a $q \in \mathrm{PSL}(2, \mathbb{R})$ with $q(p_-) = 0$ and $q(p_+) = \infty$. This $q$ sends the axis of $\tau$ (the geodesic from $p_-$ to $p_+$) to the imaginary half-line (the geodesic from $0$ to $\infty$).
>
> **Step 3 — the conjugated element is diagonal.** Consider $\tau' := q \tau q^{-1}$. It fixes $q(p_-) = 0$ and $q(p_+) = \infty$, so its matrix representative is upper-triangular with $\infty$-fixed and lower-triangular with $0$-fixed, i.e. diagonal: $\tau' = \mathrm{diag}(\lambda, \lambda^{-1})$ for some $\lambda \in \mathbb{R} \setminus \{0\}$ (representative modulo sign). Choosing the branch $\lambda = e^{\ell/2} > 1$ (or reversing orientation by post-conjugating with $z \mapsto -1/z$ if $\lambda < 0$), we get $\tau' = \mathrm{diag}(e^{\ell/2}, e^{-\ell/2})$, which acts on $\mathbb{H}^2$ by
> $$\tau'(z) \;=\; \frac{e^{\ell/2} z + 0}{0 + e^{-\ell/2}} \;=\; e^\ell z. \tag{$\star$}$$
>
> **Step 4 — check the translation length matches.** The distance from $iy$ to $\tau'(iy) = i e^\ell y$ along the axis is
> $$\int_y^{e^\ell y} \frac{du}{u} \;=\; \log e^\ell \;=\; \ell,$$
> independent of $y$. So $\tau'$ has translation length $\ell$ along its axis; by isometry, $\tau$ had the same translation length along the original axis. The choice $\lambda = e^{\ell/2}$ is thus consistent with $\tau$'s translation length.
>
> **Step 5 — the action on imaginary parts.** For $z = x + iy$, $\tau_0 z = e^\ell z = e^\ell x + i e^\ell y$, so $\mathrm{Im}(\tau_0 z) = e^\ell \mathrm{Im}(z)$. Therefore the $\langle\tau_0\rangle$-orbit of $z$ is $\{\tau_0^k z : k \in \mathbb{Z}\} = \{e^{k\ell}z : k \in \mathbb{Z}\}$, whose imaginary parts are the geometric sequence $\{e^{k\ell}\,\mathrm{Im}(z)\}$.
>
> **Step 6 — the strip is a fundamental region for $\langle\tau_0\rangle$.** Each orbit's imaginary parts form a geometric sequence with ratio $e^\ell$; that sequence meets the half-open interval $[1, e^\ell)$ in exactly one value (for any $y > 0$, the unique $k \in \mathbb{Z}$ with $e^{k\ell} y \in [1, e^\ell)$ is $k = -\lfloor(\log y)/\ell\rfloor$). So the horizontal band $\mathcal{F}_\tau := \{z : 1 \le \mathrm{Im}(z) < e^\ell\}$ meets each $\langle\tau_0\rangle$-orbit in exactly one point — a fundamental region.
>
> **Step 7 — the strip integral is coordinate-independent.** Suppose we did not conjugate to standard form, and worked with the original $\tau$ (axis $A$, some fundamental region $\mathcal{F}_A$ for $\langle\tau\rangle$). The kernel $p^E_{\mathbb{H}^2}$ is $\mathrm{PSL}(2, \mathbb{R})$-invariant (in the important cases — Brownian, subordinate Brownian — because the underlying Laplacian is, and in general for a $\Gamma$-invariant Dirichlet form the invariance holds under any $q \in \mathrm{PSL}(2, \mathbb{R})$ that lies in $\Gamma$; but the identity used here is that of the kernel *along the axis of $\tau$*, and it is enough that the axis of $\tau$ maps to the axis of $\tau_0$ by an isometry — the Brownian and subordinate-Brownian kernels are then equal along the two axes). Substituting $w = q^{-1} z$ in the strip integral:
> $$\int_{\mathcal{F}_A} p^E_{\mathbb{H}^2}(t, z, \tau^m z)\,d\rho_{\mathbb{H}^2}(z) \;=\; \int_{q^{-1}\mathcal{F}_A} p^E_{\mathbb{H}^2}(t, q^{-1}z, q^{-1}\tau^m z)\,d\rho_{\mathbb{H}^2}(w)$$
> where the substitution is $w = q^{-1}z$, Jacobian $1$ (isometry), and using $\mathrm{PSL}(2, \mathbb{R})$-invariance of the kernel with element $q^{-1}$; then $q^{-1}\tau^m z = q^{-1}\tau^m q\,w = (q^{-1}\tau q)^m w = \tau_0^m w$. The region $q^{-1}\mathcal{F}_A$ is a fundamental region for $\langle\tau_0\rangle = q^{-1}\langle\tau\rangle q$; since the integrand $w \mapsto p^E_{\mathbb{H}^2}(t, w, \tau_0^m w)$ is $\langle\tau_0\rangle$-invariant (same $\Gamma$-invariance argument as in Step 4 of [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]), the integral is the same over any such fundamental region — in particular over the strip $\mathcal{F}_\tau$. So
> $$\int_{\mathcal{F}_A} p^E_{\mathbb{H}^2}(t, z, \tau^m z)\,d\rho_{\mathbb{H}^2}(z) \;=\; \int_{\mathcal{F}_\tau} p^E_{\mathbb{H}^2}(t, w, \tau_0^m w)\,d\rho_{\mathbb{H}^2}(w),$$
> i.e. the standard-form computation gives the correct answer regardless of coordinates. $\blacksquare$

Two useful consequences:

- **The strip is a cylinder.** Gluing the top edge $\mathrm{Im}(z) = e^\ell$ of $\mathcal{F}_\tau$ to the bottom edge $\mathrm{Im}(z) = 1$ by the map $z \mapsto z/e^\ell$ produces the quotient $\langle\tau_0\rangle\backslash\mathbb{H}^2$, a *cylinder* (topologically $S^1 \times \mathbb{R}$) with the closed geodesic $\gamma$ as its waist. The paper's strip integral is a computation on this cylinder.
- **Fermi coordinates.** The axis of $\tau_0$ (the imaginary half-line) is the geometric locus where $d(z, \tau_0^m z)$ is minimal, equal to $m\ell$. Points off the axis have $d(z, \tau_0^m z) > m\ell$ by an amount computable via [[Def - Hyperbolic Plane|Fermi coordinates]] (perpendicular distance $\perp$-along-the-axis coordinate). This is the coordinate system in which [[Lemma - Wang-Xue Strip Integral|Lemma 3.4]] evaluates the strip integral in closed form.

---

# Where the paper uses this

The standard form $\tau : z \mapsto e^{\ell_\gamma} z$ is the fixed coordinate underlying every explicit computation in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]] from the moment [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] reduces the class-mass to a strip integral. It is where [[Lemma - Wang-Xue Strip Integral|Lemma 3.4]] does the Fermi-coordinate axis/perpendicular decomposition, and it is the coordinate in which the four closed forms of [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] (§3.1.1–§3.1.4) are written. The same standard-form conjugation is redeployed for hyperbolic 3-manifolds in [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7]], where the analogous loxodromic standard form $\tau : (z, y) \mapsto (e^{L_\gamma} z, e^{\ell_\gamma} y)$ underlies [[Lemma - Hyperbolic 3-Space Strip Integral|Lemma 7.2]] and [[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]].
