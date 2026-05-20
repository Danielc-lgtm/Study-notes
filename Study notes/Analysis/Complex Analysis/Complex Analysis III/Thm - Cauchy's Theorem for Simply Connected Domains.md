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

The intuition is that on a simply connected domain, every closed curve bounds a region inside the domain (in the homological sense: winding number zero around every external point), so the integral over that curve picks up no contribution from anything outside.

More concretely: simple-connectedness says no closed curve has nonzero winding number around any complementary point. Cauchy's theorem on a triangle (proved via Goursat's lemma in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]) says the integral over any triangle vanishes. By a triangulation argument, any closed curve in a region can be approximated by a sum of triangle boundaries — provided the region is "simply connected enough" that the triangulation can be done within the region. Simple-connectedness is exactly the topological condition that makes the triangulation argument go through globally.

A second intuition, more directly tied to primitives: integrating $f$ along a path from a basepoint $z_0$ to $z$ gives a function $F(z) = \int_{z_0}^z f\,dw$ — but this is well-defined only if the integral does not depend on the path chosen. On a simply connected domain, any two paths from $z_0$ to $z$ together form a closed loop (one followed by the reverse of the other), and the closed loop has winding number zero around the complement. So Cauchy's theorem makes the closed integral vanish, hence the path-independence, hence the well-definedness of $F$. And $F'(z) = f(z)$ by the fundamental theorem of calculus (in complex form: the integrand at the endpoint).

So one should expect Cauchy's theorem on simply connected domains because *simple-connectedness is the topological condition that makes primitives well-defined*, and the existence of a primitive immediately implies that closed integrals vanish (closed integral of a derivative is always zero).

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

> [!note]- Lemma 3: Path independence on simply connected $U$
> **Statement:** If $U$ is simply connected, $f$ holomorphic on $U$, and $\gamma_1, \gamma_2$ are paths from $z_0$ to $z$ in $U$, then $\int_{\gamma_1} f = \int_{\gamma_2} f$.
>
> **Hint:** Form the closed loop $\gamma = \gamma_1 - \gamma_2$. Show $\int_\gamma f\,dz = 0$ by covering $\gamma$ with discs and using local primitives.
>
> > [!note]- Full proof
> > Form the closed loop $\gamma = \gamma_1 \cdot \gamma_2^{-1}$ in $U$. By compactness, $\gamma^*$ can be covered by finitely many open discs $D_1, \ldots, D_n$ inside $U$, with each $D_i$ containing a connected sub-arc of $\gamma$. On each $D_i$, by Lemma 2, $f$ has a primitive $F_i$. The change in $F_i$ across the sub-arc of $\gamma$ in $D_i$ equals the integral of $f$ over that sub-arc. At overlaps between $D_i, D_{i+1}$, the primitives differ by a constant (both have derivative $f$). Going around the closed loop, the sum of changes is zero — provided the loop's "topology" allows the primitives to be glued consistently. Simple-connectedness ensures this: the obstruction to gluing is a winding-number term around any singularity of $f$, but $f$ has no singularities in $U$, and the loop has zero winding around the complement, so no obstruction arises.

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
