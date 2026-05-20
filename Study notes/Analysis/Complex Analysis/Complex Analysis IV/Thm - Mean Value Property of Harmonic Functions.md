---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Harmonic Function"
  - "Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)"
tags: [analysis, complex-analysis, pde]
---

# Notation

$u : U \to \mathbb{R}$ is harmonic on an open set containing the closed disc $\overline{D(a, R)}$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Mean Value Property of Harmonic Functions).** Let $u : U \to \mathbb{R}$ be harmonic on an open set $U$, and let $a \in U$ and $R > 0$ be such that $\overline{D(a, R)} \subset U$. Then for every $r \in (0, R]$,
> $$u(a) = \frac{1}{2\pi}\int_0^{2\pi} u(a + r e^{i\theta})\,d\theta.$$
> Equivalently, the value of $u$ at the centre of any disc is the average of its values on the bounding circle. Integrating in $r$ also yields the **volume mean value formula** $u(a) = \frac{1}{\pi R^2}\iint_{D(a, R)} u\,dA$.

---

# Motivation

The mean value property says: a harmonic function's value at the centre of any disc equals the average of its values on the boundary circle. Equivalently, harmonic functions have *no local sources or sinks* — they are perfectly balanced.

This is the **defining feature of harmonic functions** (in some treatments, it is taken as the definition: a continuous $u$ with $u(a) = (1/(2\pi))\int_0^{2\pi} u(a + re^{i\theta})\,d\theta$ for all sufficiently small $r$ is harmonic). It implies the maximum principle, the Liouville-style theorems for harmonic functions, and uniqueness of the Dirichlet problem.

The proof is short and elegant: harmonic functions are real parts of holomorphic functions (on simply connected pieces), and holomorphic functions satisfy the mean value property by Cauchy's integral formula at the centre. Taking real parts gives the harmonic mean value property.

---

# Sources and Targets

**Sources (Input Broadening)**

**$u$ harmonic on a domain containing a closed disc.** Direct hypothesis.

**$u$ continuous + has mean value property locally.** Reverse direction: continuous functions with the mean value property are harmonic. This is the *Bôcher characterization* and is the basis of the Perron method.

**$u$ subharmonic ($\Delta u \geq 0$).** Property $B$: weaker than harmonic. Bridge: subharmonic implies the mean value *inequality* — $u(a) \leq $ average on a circle, not equality.

**Targets (Output Amplification)**

Combine with **continuity in $r$.** Property $D$: $u(a)$ equals the average for all $r$. Amplified result $E$: $u$ is *real-analytic* (smooth + mean value property + analytic continuation gives real-analyticity).

Combine with **the maximum modulus principle.** Property $D$: $u$ attains a max at $a$. Amplified result $E$: $u(a) \geq u(a + re^{i\theta})$ for all small $r$. But $u(a) = $ average, forcing $u$ to be constant on the circle, hence locally constant.

---

# Why Is It True

Harmonic ⟺ real part of holomorphic on simply connected domains. For a disc $\overline{D(a, R)}$, which is simply connected, write $u = \operatorname{Re} f$ for some holomorphic $f$ on $U$.

By Cauchy's integral formula at the centre $a$:
$$f(a) = \frac{1}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{z - a}\,dz.$$
Substituting $z = a + re^{i\theta}$, $dz = ire^{i\theta}\,d\theta$:
$$f(a) = \frac{1}{2\pi i}\int_0^{2\pi}\frac{f(a + re^{i\theta})}{re^{i\theta}}\cdot ire^{i\theta}\,d\theta = \frac{1}{2\pi}\int_0^{2\pi} f(a + re^{i\theta})\,d\theta.$$

Taking real parts:
$$u(a) = \operatorname{Re} f(a) = \frac{1}{2\pi}\int_0^{2\pi}\operatorname{Re} f(a + re^{i\theta})\,d\theta = \frac{1}{2\pi}\int_0^{2\pi} u(a + re^{i\theta})\,d\theta.$$

The mean value property holds.

---

# What Makes This Hard

The proof is short, but its **interpretation as a fundamental property of harmonic functions** is what matters. A common conceptual gap: students forget that the mean value property *characterizes* harmonic functions among continuous functions. The Perron method for solving the Dirichlet problem on general domains uses subharmonic functions (mean value inequality) and the "subharmonic-maximum" construction, all powered by this characterization.

---

# Rederivation Scaffold

**High-level strategy:**
Write $u = \operatorname{Re} f$ for holomorphic $f$ on a small disc. Apply Cauchy's integral formula to $f$ at the centre, evaluating along the boundary circle. Take real parts.

**Subgoal decomposition:**

1. **Restrict to a small disc** containing $\overline{D(a, R)}$. The disc is simply connected.

2. **Find holomorphic $f$ with $u = \operatorname{Re} f$.** Use [[Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)|harmonic conjugate existence]].

3. **Apply Cauchy's integral formula at $a$.** $f(a) = (2\pi i)^{-1}\oint f(z)/(z - a)\,dz$.

4. **Parametrize and simplify.** $z = a + re^{i\theta}$, integrand becomes $f(a + re^{i\theta})/(re^{i\theta}) \cdot ire^{i\theta}\,d\theta = if(a + re^{i\theta})\,d\theta$. Integral: $(1/(2\pi))\int_0^{2\pi}f(a + re^{i\theta})\,d\theta$.

5. **Take real parts.** $u(a) = (1/(2\pi))\int_0^{2\pi}u(a + re^{i\theta})\,d\theta$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $u$ be harmonic on $U$ with $\overline{D(a, R)} \subset U$. Choose $R' < R$ such that $\overline{D(a, R')}$ is contained in a slightly larger open disc $D(a, R'')$ on which we can find a harmonic conjugate (such a disc exists; any disc is simply connected).
>
> By [[Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)|the harmonic conjugate theorem]], there exists a holomorphic $f$ on $D(a, R'')$ with $\operatorname{Re} f = u$ on this disc.
>
> For any $r$ with $0 < r < R''$, apply Cauchy's integral formula to $f$:
> $$f(a) = \frac{1}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{z - a}\,dz.$$
>
> Parametrize $z = a + re^{i\theta}$ for $\theta \in [0, 2\pi]$, so $dz = ire^{i\theta}\,d\theta$. Substituting:
> $$f(a) = \frac{1}{2\pi i}\int_0^{2\pi}\frac{f(a + re^{i\theta})}{re^{i\theta}} \cdot ire^{i\theta}\,d\theta = \frac{1}{2\pi}\int_0^{2\pi}f(a + re^{i\theta})\,d\theta.$$
>
> Take real parts:
> $$u(a) = \operatorname{Re} f(a) = \frac{1}{2\pi}\int_0^{2\pi}\operatorname{Re} f(a + re^{i\theta})\,d\theta = \frac{1}{2\pi}\int_0^{2\pi} u(a + re^{i\theta})\,d\theta.$$
>
> Since $R'' > R$, $r$ can be any value in $(0, R)$ (and the formula extends to $r = R$ by continuity). $\blacksquare$
>
> **Converse (Bôcher).** A continuous function $u$ on $U$ with the mean value property for all sufficiently small discs is harmonic. *Proof:* it satisfies the maximum principle, hence locally minimum and continuous; one can show $u$ is a limit of Poisson-style harmonic functions and is hence harmonic. (Detailed proof in Stein.)

---

# Cross-Field Exercise Suggestions

**Maximum principle as a corollary.** A non-constant harmonic $u$ on a domain $D$ has no interior maximum. *Proof:* if $u(a)$ is a local max, then $u(a) \geq u(a + re^{i\theta})$ on a small circle, and $u(a) = $ average. So $u(a + re^{i\theta}) = u(a)$ on the entire circle (average equality requires pointwise equality). $u$ is locally constant; by connectedness, globally constant. Contradiction with non-constant.

**Volume mean value formula.** The mean value property extends to *volume* averages: $u(a) = (1/\pi r^2)\int_{D(a, r)} u\,dA$ — the average over the *disc*, not just the boundary circle. *Proof:* integrate the circle-average formula over radii.

**Generalization to higher dimensions.** Harmonic functions on $\mathbb{R}^n$ have mean value property over spheres: $u(a) = (1/\sigma_n)\int_{S^{n-1}}u(a + r\omega)\,d\sigma(\omega)$ where $\sigma_n$ is the surface area of the unit sphere. The proof generalizes Cauchy's integral formula (now requiring Green's identities).

---

# Bridges

- **[[Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)]]** — used in the proof.

- **Cauchy's integral formula** (in CA II) — the holomorphic analog.

- **[[Thm - Maximum Principle for Harmonic Functions]]** — direct corollary.

- **[[Thm - Poisson Integral Formula]]** — generalization to interior points other than the centre.

---

# Unlocked by This

> [!tip] Maximum and Minimum Principles *(from §3.6+)*
> The mean value property is the foundation of [[Thm - Maximum Principle for Harmonic Functions|max/min principles]].

> [!tip] Poisson Integral *(from §3.6+)*
> The mean value formula is the special case $a = $ centre of disc; [[Thm - Poisson Integral Formula|Poisson]] gives the general case.

> [!tip] Subharmonic and Perron Method *(from PDE)*
> The mean value *inequality* defines **subharmonic functions** ($\Delta u \geq 0$), used in the Perron method for solving Dirichlet problems on general domains.
