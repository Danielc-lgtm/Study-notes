---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Thm - Riemann's Removable Singularity Theorem"
tags: [analysis, complex-analysis]
---

# Notation

$\mathbb{D} = \{z : |z| < 1\}$ is the open unit disc. $f : \mathbb{D} \to \mathbb{D}$ is holomorphic with $f(0) = 0$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Schwarz Lemma).** Let $f : \mathbb{D} \to \mathbb{D}$ be holomorphic with $f(0) = 0$. Then
> $$|f(z)| \leq |z| \text{ for all } z \in \mathbb{D}, \qquad\text{and}\qquad |f'(0)| \leq 1.$$
> Moreover, if equality $|f(z_0)| = |z_0|$ holds at some $z_0 \in \mathbb{D} \setminus \{0\}$, or if $|f'(0)| = 1$, then $f$ is a rotation: there exists $\theta \in \mathbb{R}$ with $f(z) = e^{i\theta} z$ for all $z \in \mathbb{D}$.

---

# Motivation

Schwarz's lemma is a deceptively simple but powerful constraint on holomorphic self-maps of the unit disc fixing the origin. It says: such a map must contract the disc — $|f(z)| \leq |z|$ for all $z$, and $|f'(0)| \leq 1$. Moreover, equality (anywhere) forces $f$ to be a rotation.

This is one of the cornerstones of modern complex function theory. It is the source of the classification of automorphisms of the disc, the proof of the Riemann mapping theorem's uniqueness, the Pick interpolation theorem, the theory of bounded analytic functions, and the modern theory of Möbius-invariant function spaces (Hardy, Bergman, Bloch).

The intuition: a holomorphic map of the disc to itself fixing the origin can't expand things. The bound $|f(z)| \leq |z|$ is exact in the sense that *equality holds* for rotations $f(z) = e^{i\theta} z$, which are the only "extremal" maps.

---

# Sources and Targets

**Sources (Input Broadening)**

**$f : \mathbb{D} \to \mathbb{D}$ holomorphic, $f(0) = 0$.** Direct hypothesis.

**$f : \mathbb{D} \to \mathbb{D}$ holomorphic with $f(a) = b$ for some $a, b$.** Reduce to the basic case: pre- and post-compose with Möbius automorphisms of $\mathbb{D}$ that move $a$ to $0$ and $b$ to $0$. The composed function fixes $0$, and Schwarz applies.

**$f : \mathbb{D} \to V$ holomorphic for some domain $V$.** Apply via a conformal map $\phi : V \to \mathbb{D}$ (when one exists). $\phi \circ f : \mathbb{D} \to \mathbb{D}$, apply Schwarz.

**Targets (Output Amplification)**

Combine with **the classification of disc automorphisms.** Property $D$: $f : \mathbb{D} \to \mathbb{D}$ biholomorphic. Amplified result $E$: $f$ is a Möbius transformation of a specific form — see [[Thm - Conformal Automorphisms of the Unit Disc]].

Combine with **the Pick interpolation theorem.** Property $D$: given values of $f$ at finitely many points of $\mathbb{D}$. Amplified result $E$: criteria for existence of $f : \mathbb{D} \to \mathbb{D}$ interpolating these values.

Combine with **Riemann mapping uniqueness.** Property $D$: two biholomorphisms $U \to \mathbb{D}$. Amplified result $E$: they differ by a disc automorphism, which is a 3-parameter family.

---

# Why Is It True

The proof has a beautifully simple structure using the **maximum modulus principle**.

Consider $g(z) := f(z)/z$ for $z \in \mathbb{D}\setminus\{0\}$. Since $f(0) = 0$, by [[Thm - Riemann's Removable Singularity Theorem|Riemann's removable singularity theorem]], $g$ extends to a holomorphic function on $\mathbb{D}$ with $g(0) = f'(0)$.

On any circle $|z| = r$ with $r < 1$: $|g(z)| = |f(z)|/|z| \leq 1/r$ (since $|f(z)| \leq 1$). By the maximum modulus principle applied to $g$ on $\{|z| \leq r\}$, $|g| \leq 1/r$ everywhere on $\{|z| \leq r\}$.

Let $r \to 1^-$: $|g(z)| \leq 1$ for $z \in \mathbb{D}$. So $|f(z)/z| \leq 1$, i.e., $|f(z)| \leq |z|$ for $z \neq 0$ (trivially $f(0) = 0$ too).

At $z = 0$: $|f'(0)| = |g(0)| \leq 1$ as well.

The equality case: if $|g(z_0)| = 1$ for some $z_0 \in \mathbb{D}$, then $g$ attains an interior maximum of $|g|$ on $\mathbb{D}$, forcing $g$ to be constant. Since $|g| = 1$, $g(z) = e^{i\theta}$ for some constant $\theta \in \mathbb{R}$. So $f(z) = e^{i\theta} z$ — a rotation.

The conceptual content: *holomorphic functions are rigid*, and the maximum modulus principle gives the global bound from the boundary (after the auxiliary function $f/z$ removes the constraint at $0$).

---

# What Makes This Hard

The non-obvious step is **introducing the auxiliary function $f(z)/z$** and applying Riemann's removable singularity theorem to make it holomorphic on the full disc. The trick is to use the fact $f(0) = 0$ to "cancel" the $z$ in the denominator, getting a function holomorphic on the disc rather than just the punctured disc. Then maximum modulus gives the global bound.

A common error is to apply the maximum principle directly to $f$ — but $f$ has its maximum on the *boundary*, not in the interior, so the max principle doesn't tighten $|f| \leq 1$ to $|f| \leq |z|$. The reformulation via $f/z$ is the key.

---

# Rederivation Scaffold

**High-level strategy:**
Form $g(z) = f(z)/z$. Show $g$ is holomorphic on $\mathbb{D}$ (using $f(0) = 0$ and Riemann's removable singularity theorem). On any circle $|z| = r$, $|g| \leq 1/r$. By maximum modulus, $|g| \leq 1/r$ on the disc $|z| \leq r$. Letting $r \to 1$, $|g| \leq 1$ on $\mathbb{D}$.

**Subgoal decomposition:**

1. **Define $g(z) = f(z)/z$** on $\mathbb{D}\setminus\{0\}$.

2. **Show $g$ extends holomorphically to $\mathbb{D}$** with $g(0) = f'(0)$. Use $f(0) = 0$: $f(z) = f'(0)z + O(z^2)$ near $0$, so $f(z)/z = f'(0) + O(z) \to f'(0)$ as $z \to 0$. Hence $g$ has a removable singularity at $0$.

3. **Bound $g$ on circles $|z| = r$.** $|g(z)| = |f(z)|/r \leq 1/r$ (using $|f| < 1$ on $\mathbb{D}$).

4. **Apply maximum modulus.** $|g(z)| \leq 1/r$ on $\{|z| \leq r\}$.

5. **Let $r \to 1^-$.** $|g(z)| \leq 1$ on $\mathbb{D}$. Equivalent: $|f(z)| \leq |z|$ on $\mathbb{D}$. And $|f'(0)| = |g(0)| \leq 1$.

6. **Equality case.** If $|g(z_0)| = 1$ for some $z_0$, interior maximum forces $g$ to be constant unimodular, so $f(z) = e^{i\theta}z$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : \mathbb{D} \to \mathbb{D}$ be holomorphic with $f(0) = 0$.
>
> **Step 1: Auxiliary function $g(z) = f(z)/z$.** On $\mathbb{D}\setminus\{0\}$, $g$ is holomorphic (quotient of holomorphic, denominator nonzero). At $z = 0$: $f(z) = f'(0)z + O(z^2)$ (Taylor expansion at $0$), so $f(z)/z = f'(0) + O(z) \to f'(0)$ as $z \to 0$. Hence $g$ is bounded near $0$, and by [[Thm - Riemann's Removable Singularity Theorem|Riemann's theorem]] extends to a holomorphic function on $\mathbb{D}$ with $g(0) = f'(0)$.
>
> **Step 2: Maximum modulus on a small disc.** Fix $0 < r < 1$. On $|z| = r$:
> $$|g(z)| = |f(z)|/|z| = |f(z)|/r \leq 1/r,$$
> using $|f(z)| < 1$ on $\mathbb{D}$.
>
> By the maximum modulus principle applied to $g$ on the closed disc $\{|z| \leq r\}$: $|g(z)| \leq 1/r$ for all $|z| \leq r$.
>
> **Step 3: Letting $r \to 1^-$.** For any fixed $z \in \mathbb{D}$, $z \in \{|w| \leq r\}$ for any $r > |z|$. The inequality $|g(z)| \leq 1/r$ holds for all such $r$. Taking $r \to 1^-$: $|g(z)| \leq 1$.
>
> So $|g(z)| \leq 1$ for all $z \in \mathbb{D}$. Equivalently:
> $$|f(z)| = |z||g(z)| \leq |z| \text{ for all } z \in \mathbb{D}.$$
> And $|f'(0)| = |g(0)| \leq 1$.
>
> **Step 4: Equality case.** Suppose $|f(z_0)| = |z_0|$ for some $z_0 \in \mathbb{D}\setminus\{0\}$, i.e., $|g(z_0)| = 1$. The function $g$ is holomorphic on $\mathbb{D}$ with $|g| \leq 1$, attaining $|g| = 1$ at the interior point $z_0$. By the maximum modulus principle, $g$ is constant: $g(z) = c$ for some $c \in \mathbb{C}$ with $|c| = 1$. So $g(z) = e^{i\theta}$ for some $\theta$, and $f(z) = e^{i\theta}z$ — a rotation.
>
> Similarly, if $|f'(0)| = 1$: $|g(0)| = 1$, interior max, $g$ constant, $f$ a rotation.
>
> Conversely, rotations $f(z) = e^{i\theta}z$ have $f(0) = 0$, $|f(z)| = |z|$, $|f'(0)| = 1$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Pick's theorem.** Generalization of Schwarz: if $f : \mathbb{D} \to \mathbb{D}$ holomorphic and $f(a) = b$ (not necessarily $a = 0$), then the **pseudo-hyperbolic distance** $|f(z) - b|/|1 - \bar b f(z)|$ is bounded above by $|z - a|/|1 - \bar a z|$. The proof: pre/post-compose with Möbius automorphisms of $\mathbb{D}$ to reduce to Schwarz.

**Hyperbolic distance preserved by disc automorphisms.** The **hyperbolic distance** $d_h(z_1, z_2) = \tanh^{-1}((z_2 - z_1)/(1 - \bar z_1 z_2))$ in the Poincaré disc model is preserved by automorphisms of $\mathbb{D}$ (which are biholomorphic in our sense). Schwarz says all $f : \mathbb{D} \to \mathbb{D}$ holomorphic fixing $0$ are *contractions* in this hyperbolic metric. For automorphisms ($f$ biholomorphic), equality holds — they are isometries.

**Bounded holomorphic functions.** The class $H^\infty(\mathbb{D})$ of bounded holomorphic functions on the disc has many properties that follow from Schwarz: the norm is the supremum, and pointwise estimates are sharp at fixed points.

---

# Bridges

- **[[Thm - Riemann's Removable Singularity Theorem]]** — used to extend $f/z$ to a holomorphic function on $\mathbb{D}$.

- **Maximum modulus principle** (in CA II) — the engine.

- **[[Thm - Conformal Automorphisms of the Unit Disc]]** — directly derived from Schwarz.

- **[[Thm - Riemann Mapping Theorem (Statement)]]** — uses Schwarz in the uniqueness argument.

---

# Unlocked by This

> [!tip] Conformal Automorphisms of the Disc *(from §3.5+)*
> Schwarz determines [[Thm - Conformal Automorphisms of the Unit Disc|all biholomorphisms]] $\mathbb{D} \to \mathbb{D}$.

> [!tip] Hyperbolic Geometry *(from Differential Geometry)*
> Schwarz is the statement that holomorphic self-maps of $\mathbb{D}$ are *contractions* in the Poincaré-disc hyperbolic metric, foundational for the geometry of the hyperbolic plane.

> [!tip] Nevanlinna–Pick Theory *(from Operator Theory)*
> The **Pick interpolation theorem** characterizes when a holomorphic $f : \mathbb{D} \to \mathbb{D}$ takes prescribed values at finitely many points. Foundational in operator theory, $H^\infty$ control, and signal processing.
