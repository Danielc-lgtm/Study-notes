---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Simply Connected Domain in Complex Analysis"
  - "Def - Holomorphic Function"
  - "Def - Winding Number"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is open and simply connected. $f : U \to \mathbb{C}$ is holomorphic. $\gamma$ is a closed piecewise $C^1$ curve in $U$. The full registry lives on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Statement

> **Theorem (Cauchy's Theorem for Simply Connected Domains).** Let $U \subseteq \mathbb{C}$ be open and simply connected, and let $f : U \to \mathbb{C}$ be holomorphic. Then for every closed piecewise $C^1$ curve $\gamma$ in $U$,
> $$\int_\gamma f(z)\, dz = 0.$$
> Equivalently, $f$ has a primitive on $U$: there exists a holomorphic $F : U \to \mathbb{C}$ with $F' = f$.

---

# Motivation

The local Cauchy theorem of [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]] says that on a star-shaped domain, every closed integral of a holomorphic function vanishes. This is enough to derive the Cauchy integral formula, Taylor series expansion, and many other foundational results — but the star-shaped hypothesis is awkward in applications. Many natural domains (the slit plane, the strip $\{|\operatorname{Im} z| < \pi\}$, the union of two overlapping discs) are simply connected but not star-shaped, and we want Cauchy's theorem on them too.

The full Cauchy theorem for simply connected domains removes the star-shaped hypothesis. The simple-connectedness condition (every closed curve has zero winding number around every point of the complement) is exactly what is needed: it captures the topological essence of "the curve bounds a region inside $U$", which is what makes the closed integral vanish. The condition is not merely sufficient — it is *necessary* (on the annulus, $\int_{|z|=1} dz/z = 2\pi i \neq 0$, and the failure is exactly that the unit circle has nonzero winding number around the missing centre).

This is the cleanest, most useful form of Cauchy's theorem, and it is the one we will use for every application: existence of primitives, existence of logarithms, residue theorem, Cauchy integral formula in its general form.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$U$ is simply connected, $f$ holomorphic on $U$". The sources are situations leading us to this hypothesis.

The first disguised source is **a star-shaped domain.** Property $B$: $U$ is star-shaped about some $z_0$ (every $z \in U$ has the segment $[z_0, z] \subseteq U$). Bridge: star-shaped implies simply connected (the radial homotopy contracts every loop to $z_0$). The simpler Cauchy theorem for star-shaped domains is a special case.

The second disguised source is **a convex domain.** Property $B$: $U$ is convex. Bridge: convex implies star-shaped (about every point), implies simply connected. All discs, half-planes, the upper half-plane, strips, are convex.

The third disguised source is **a domain homeomorphic to a disc.** Property $B$: $U$ is the image of a disc under a homeomorphism, or more generally, $U$ has trivial fundamental group. Bridge: trivial $\pi_1$ = simply connected. This handles many domains that look topologically simple but are not convex.

The fourth disguised source is **a domain whose complement (in $\hat{\mathbb{C}}$) is connected.** Property $B$: $\hat{\mathbb{C}} \setminus U$ is connected as a subset of the Riemann sphere. Bridge: this is equivalent to simple-connectedness for open $U \subseteq \mathbb{C}$. The slit plane $\mathbb{C} \setminus (-\infty, 0]$ has complement $(-\infty, 0] \cup \{\infty\}$, connected in $\hat{\mathbb{C}}$, so simply connected.

**Targets (Output Amplification)**

The conclusion is "every closed integral of $f$ over a curve in $U$ vanishes, equivalently $f$ has a primitive on $U$".

Combine the conclusion with **specific choice of $f$.** Property $D$: $f = 1/z$ on a simply connected domain $U$ avoiding $0$. Amplified result $E$: $1/z$ has a primitive on $U$, i.e., a branch of $\log z$ exists on $U$. This is one of the most-used corollaries.

Combine the conclusion with **a Cauchy-kernel structure.** Property $D$: $f(z) = g(z)/(z - w)$ for $g$ holomorphic and $w \notin U$. Amplified result $E$: the integral $\int_\gamma g(z)/(z - w)\,dz = 0$, and (with $w \in U$) the Cauchy integral formula $f(w) = (2\pi i)^{-1} \int_\gamma f(z)/(z - w)\,dz$ holds.

Combine the conclusion with **a meromorphic $f$ with isolated singularities.** Property $D$: $f$ is meromorphic with singularities at $a_1, \ldots, a_n$ inside $\gamma$. Amplified result $E$: the residue theorem $\int_\gamma f\,dz = 2\pi i \sum I(\gamma; a_i) \operatorname{Res}_{a_i} f$. This is how the residue theorem is derived from Cauchy plus residues.

---

# Why Is It True

The proof reduces the global statement to a finite combinatorial sum of *local* Cauchy theorems (each one Goursat on a triangle, or equivalently Cauchy on a disc).

**The mechanism in one line.** *Simple-connectedness gives a continuous homotopy $H : [0, 1]^2 \to U$ from $\gamma$ to a constant; uniform continuity of $H$ lets us tile $[0, 1]^2$ into a square grid fine enough that each small square's image lies in some open disc inside $U$; Cauchy-on-a-disc kills the integral around each small square's image; summing, interior edges of the grid cancel pairwise (each interior edge is traversed once by each adjacent square in opposite directions), and only the boundary of the unit square survives — which integrates to $\int_\gamma f\,dz$ on the bottom edge and $0$ on the other three.* The full argument is Lemma 3 below.

**Why simple-connectedness is exactly the right hypothesis.** The grid argument needs every small square's image to lie in a disc inside $U$. Without simple-connectedness, the loop need not bound a contractible region — for instance, the unit circle in $\mathbb{C}^\times$ encloses the missing point $0$, and *no* homotopy in $\mathbb{C}^\times$ can contract it. In that case the grid argument has no homotopy $H$ to set up, and indeed $\int_{|z|=1} dz/z = 2\pi i \neq 0$ shows the theorem genuinely fails. So simple-connectedness is not just sufficient for the closed-integral statement to hold, it is the precise condition under which the grid-and-cancel proof goes through.

**Equivalent route via primitives.** A holomorphic $f$ with a primitive $F$ on $U$ has $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a)) = 0$ for every closed $\gamma$ — closed-loop integrals of derivatives vanish. So existence of a primitive immediately implies the closed-integral statement, and conversely vanishing of closed integrals implies path-independence of $F(z) := \int_{z_0}^z f\,dw$, hence well-definedness of the primitive. The two statements are equivalent; the grid argument proves the closed-integral version directly, and Lemma 2 (disc primitive) is the building block of the alternate primitive-construction route.

---

# What Makes This Hard

The non-obvious step is **upgrading the local Cauchy theorem (triangles, discs, star-shaped) to the global one** — recognizing that the simple-connectedness condition is exactly what is needed for the local-to-global passage. A frequent source of confusion is conflating "simply connected" with "convex" or "star-shaped"; these are sufficient but not necessary, and the full theorem requires the weakest form (simple-connectedness). Another common error is to apply the theorem to a closed curve on a non-simply-connected domain *without* checking the simple-connectedness hypothesis; the theorem then fails (the annulus is the classical counterexample).

---

# Rederivation Scaffold

**High-level strategy:**
Use the local Cauchy theorem (on triangles, via Goursat) plus the simple-connectedness assumption to show that every closed integral can be written as a finite sum of triangle integrals (each zero). Equivalently, construct a primitive by path integration, with simple-connectedness ensuring path-independence.

**Subgoal decomposition:**

1. **Local Cauchy theorem on triangles.** Show $\int_{\partial T} f\,dz = 0$ for any triangle $T$ inside a disc on which $f$ is holomorphic.
   - *Hint:* Goursat's bisection argument from [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]].
   - *Why needed:* It is the irreducible local content.

2. **Existence of a primitive on a disc.** Show that on any disc $D \subseteq U$, $f$ has a primitive $F$.
   - *Hint:* Define $F(z) = \int_{z_0}^z f\,dw$ along any path; by Cauchy on triangles, $F$ is well-defined; differentiating gives $F' = f$.
   - *Why needed:* This is the local primitive that we patch globally.

3. **Path-independence on simply connected $U$.** Show that for $z_0, z \in U$, $\int_{\gamma_1} f\,dw = \int_{\gamma_2} f\,dw$ for any two paths $\gamma_1, \gamma_2$ from $z_0$ to $z$.
   - *Hint:* The closed loop $\gamma_1 - \gamma_2$ has zero winding around every external point; by the local-to-global gluing of disc primitives, $\int_{\gamma_1 - \gamma_2} f\,dw = 0$.
   - *Why needed:* Path-independence is what makes the global primitive well-defined.

4. **Construct the global primitive.** Define $F(z) = \int_{z_0}^z f\,dw$; show $F$ is holomorphic with $F' = f$ on $U$.
   - *Hint:* Compute $F(z + h) - F(z)$ by integrating along a short segment; use continuity of $f$.
   - *Why needed:* The existence of a primitive is equivalent to the closed-integral statement.

5. **Closed integrals vanish.** Conclude: $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a)) = 0$ for closed $\gamma$ (since $\gamma(a) = \gamma(b)$).

---

# Lemma Decomposition

> [!note]- Lemma 1: Cauchy's theorem on a triangle (Goursat)
> **Statement:** If $f$ is holomorphic on an open set containing a closed triangle $T$ and its interior, then $\int_{\partial T} f\,dz = 0$.
>
> **Hint:** Bisection argument: subdivide $T$ into 4 sub-triangles by joining midpoints; iterate; use holomorphicity to bound the residual.
>
> **Why needed:** Local Cauchy on triangles is the bedrock; all of Cauchy's theorem builds on it.
>
> *Proved in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]].*

> [!note]- Lemma 2: Existence of a primitive on a disc
> **Statement:** If $f$ is holomorphic on a disc $D$, then there exists a holomorphic $F : D \to \mathbb{C}$ with $F' = f$.
>
> **Hint:** Fix $z_0 \in D$; define $F(z) = \int_{[z_0, z]} f\,dw$ along the straight segment.
>
> > [!note]- Full proof
> > Define $F(z) = \int_{[z_0, z]} f\,dw$. To compute $F'$: for $z, z + h \in D$, the triangle with vertices $z_0, z, z + h$ lies in $D$, so by Goursat $\int_{\partial T} f\,dw = 0$, giving $F(z + h) - F(z) = \int_{[z, z+h]} f\,dw$. By continuity of $f$, $\int_{[z, z+h]} f\,dw = h f(z) + o(h)$, so $F'(z) = f(z)$.

> [!note]- Lemma 3: Closed-loop integral on simply connected $U$ vanishes
> **Statement:** If $U$ is open and simply connected, $f$ is holomorphic on $U$, and $\gamma : [0, 1] \to U$ is a piecewise $C^1$ closed loop ($\gamma(0) = \gamma(1)$), then $\int_\gamma f\,dz = 0$.
>
> **Hint:** Simple-connectedness gives a continuous homotopy $H : [0, 1]^2 \to U$ from $\gamma$ to a constant loop. Tile $[0, 1]^2$ into small squares whose $H$-image fits in some open disc inside $U$, apply [[Thm - Cauchy's Theorem for a Disc|Cauchy-on-a-disc]] to each square, sum: interior edges cancel, only the outer boundary survives, and the outer boundary integrates to $\int_\gamma f - 0 = \int_\gamma f$.
>
> > [!note]- Full proof
> > **Setup.** By the definition of simply connected, there is a continuous $H : [0, 1]^2 \to U$ with $H(s, 0) = \gamma(s)$, $H(s, 1) = \gamma(0)$ (constant), and $H(0, t) = H(1, t) = \gamma(0)$. (Strictly, simple-connectedness gives only continuous $H$; the integral statement we want is about piecewise $C^1$ curves. The standard fix: after a uniform $C^0$ approximation of $H$ by a piecewise-affine map $\tilde H$ whose square grid pulls back to a square grid in $[0, 1]^2$, the integrals along the affine pieces are valid contour integrals. We omit this approximation and assume $H$ is piecewise $C^1$.)
> >
> > **The grid.** Pick $N \in \mathbb{N}$ large enough that for each closed square $Q_{ij} = [(i-1)/N, i/N] \times [(j-1)/N, j/N]$, $i, j \in \{1, \ldots, N\}$, the image $H(Q_{ij})$ has diameter less than $\min_{z \in H([0,1]^2)} \mathrm{dist}(z, \partial U)$. Such $N$ exists by uniform continuity of $H$ on the compact $[0, 1]^2$. Then $H(Q_{ij})$ is contained in an open disc $D_{ij} \subseteq U$ centred at $H((i-\tfrac12)/N, (j-\tfrac12)/N)$. By [[Thm - Cauchy's Theorem for a Disc|Cauchy-on-a-disc]] applied on $D_{ij} \supseteq H(\partial Q_{ij})$:
> > $$\int_{H(\partial Q_{ij})} f\,dz = 0,$$
> > where $\partial Q_{ij}$ is traversed counterclockwise.
> >
> > **Summing the squares.** Sum over $i, j$:
> > $$\sum_{i, j = 1}^N \int_{H(\partial Q_{ij})} f\,dz = 0.$$
> > Each interior edge of the grid — every vertical edge $\{i/N\} \times [(j-1)/N, j/N]$ for $i \in \{1, \ldots, N-1\}$ and every horizontal edge $[(i-1)/N, i/N] \times \{j/N\}$ for $j \in \{1, \ldots, N-1\}$ — is shared between two adjacent squares $Q_{ij}$ and $Q_{i+1, j}$ (or $Q_{ij}$ and $Q_{i, j+1}$), and in the two squares' CCW boundary parametrisations the shared edge appears with opposite directions. So under the map $H$, $\int_{H(\text{edge})} f\,dz$ from one square cancels exactly with the corresponding contribution from the adjacent square (substitution $t \mapsto 1 - t$).
> >
> > **What remains.** The cancellation leaves only the boundary edges of the unit square $\partial[0, 1]^2$, traversed once CCW:
> > - bottom edge $s \in [0, 1]$, $t = 0$: $H(s, 0) = \gamma(s)$, contributing $\int_\gamma f\,dz$;
> > - right edge $s = 1$, $t \in [0, 1]$: $H(1, t) = \gamma(0)$ (constant), contributing $0$;
> > - top edge $s \in [1, 0]$ (reversed), $t = 1$: $H(s, 1) = \gamma(0)$ (constant), contributing $0$;
> > - left edge $s = 0$, $t \in [1, 0]$ (reversed): $H(0, t) = \gamma(0)$ (constant), contributing $0$.
> >
> > So $\int_\gamma f\,dz = 0$. $\blacksquare$
> >
> > **Corollary (path independence).** Given two paths $\gamma_1, \gamma_2 : [0, 1] \to U$ with $\gamma_1(0) = \gamma_2(0) = z_0$, $\gamma_1(1) = \gamma_2(1) = z$, the concatenation $\gamma_1 \cdot \gamma_2^{-1}$ (where $\gamma_2^{-1}(t) = \gamma_2(1-t)$) is a closed loop at $z_0$ with $\int_{\gamma_1 \cdot \gamma_2^{-1}} f\,dz = \int_{\gamma_1} f\,dz - \int_{\gamma_2} f\,dz = 0$, hence $\int_{\gamma_1} f\,dz = \int_{\gamma_2} f\,dz$.

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1 (Goursat on triangles) and Lemma 2 (primitive on a disc), $f$ has a local primitive on every disc inside $U$. By Lemma 3 (path independence), the function $F(z) = \int_{z_0}^z f\,dw$ — defined along any path from a basepoint $z_0$ to $z$ in $U$ — is well-defined on simply connected $U$.
>
> $F$ is holomorphic with $F' = f$: for $z \in U$, choose a disc $D$ around $z$ inside $U$; by Lemma 2 the local primitive $F_D$ on $D$ has $F_D' = f$. The global $F$ differs from $F_D$ by a constant on $D$ (both have $f$ as derivative on the connected $D$), so $F$ is holomorphic on $D$ with $F' = f$. Since $z$ was arbitrary, $F$ is holomorphic on $U$ with $F' = f$.
>
> Therefore, for any closed piecewise $C^1$ curve $\gamma$ in $U$ with $\gamma(a) = \gamma(b)$,
> $$\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a)) = 0. \quad\blacksquare$$

---

# Cross-Field Exercise Suggestions

**Existence of logarithms.** Apply Cauchy's theorem to $f(z) = 1/z$ on a simply connected $U \subseteq \mathbb{C}^\times$. The conclusion is that $1/z$ has a primitive, namely a branch of $\log z$. This is the canonical application: on $\mathbb{C} \setminus (-\infty, 0]$, the principal branch $\log z = \log|z| + i\arg z$ (with $\arg z \in (-\pi, \pi)$) is the unique primitive of $1/z$ vanishing at $z = 1$.

**Residue theorem proof.** The residue theorem is Cauchy's theorem applied to $f$ minus its principal parts: if $f$ is meromorphic on a simply connected $U$ with poles $a_1, \ldots, a_n$ inside $\gamma$, then $f - \sum_i P_i$ (where $P_i$ is the principal part at $a_i$, a rational function with pole only at $a_i$) is holomorphic on $U$, so its integral over $\gamma$ vanishes by Cauchy. The residue theorem then follows by computing each $\int_\gamma P_i\,dz = 2\pi i \cdot I(\gamma; a_i) \cdot \operatorname{Res}_{a_i} f$.

**Existence of harmonic conjugates.** A real-valued harmonic function $u$ on a simply connected $U$ has a harmonic conjugate $v$ such that $f = u + iv$ is holomorphic. Proof: the 1-form $\omega = -u_y\,dx + u_x\,dy$ is closed (by harmonicity), hence exact on a simply connected $U$ (this is a real-variable Cauchy-like statement); its primitive $v$ satisfies the Cauchy-Riemann equations with $u$.

---

# Bridges

- **[[Def - Simply Connected Domain in Complex Analysis]]** — the hypothesis on the domain.

- **[[Thm - Existence and Properties of the Winding Number]]** — winding number is the topological invariant that makes "simply connected" a precise condition.

- **[[Thm - Existence of Log and Square Root on Simply Connected Domains]]** — the most-used corollary of Cauchy's theorem on simply connected domains.

- **[[Thm - Residue Theorem]]** — extends Cauchy to allow isolated singularities, with corrections by residues.

- **[[Thm - Cauchy–Riemann Equations]]** — the local differential characterization of holomorphicity that powers all of Cauchy theory.

---

# Unlocked by This

> [!tip] Riemann Mapping Theorem *(from §3.5+)*
> Cauchy's theorem on simply connected domains is the key step in the [[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping theorem]]: it ensures the conformal map's inverse is holomorphic, which is what biholomorphism requires.

> [!tip] De Rham Cohomology *(from Differential Topology)*
> Cauchy's theorem is the complex-analytic incarnation of *closed implies exact on simply connected*. The general framework is **de Rham cohomology**: on a simply connected manifold, every closed differential form is exact, and the integral around closed loops vanishes. See [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|Multivariate IV]] for the differential-form framework.
