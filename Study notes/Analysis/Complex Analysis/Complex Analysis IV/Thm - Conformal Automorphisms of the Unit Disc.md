---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Schwarz Lemma"
  - "Def - Möbius Transformation"
  - "Def - Conformal Map"
tags: [analysis, complex-analysis]
---

# Notation

$\mathbb{D} = \{z : |z| < 1\}$ is the open unit disc. $\operatorname{Aut}(\mathbb{D})$ is the group of biholomorphic automorphisms $\mathbb{D} \to \mathbb{D}$. A **Blaschke factor** is $B_a(z) = (z - a)/(1 - \bar a z)$ for $a \in \mathbb{D}$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Conformal Automorphisms of the Unit Disc).** A holomorphic map $f : \mathbb{D} \to \mathbb{D}$ is a biholomorphic automorphism if and only if there exist $\theta \in \mathbb{R}$ and $a \in \mathbb{D}$ such that
> $$f(z) = e^{i\theta}\,\frac{z - a}{1 - \bar a\, z}, \qquad z \in \mathbb{D}.$$
> Equivalently, $\operatorname{Aut}(\mathbb{D})$ consists exactly of the compositions of rotations $z \mapsto e^{i\theta}z$ and Blaschke factors $B_a(z) = (z - a)/(1 - \bar a z)$, and is a real $3$-parameter Lie group isomorphic to $\operatorname{PSU}(1,1) \cong \operatorname{PSL}_2(\mathbb{R})$.

---

# Motivation

Once we know that the unit disc has biholomorphic automorphisms (e.g., rotations $z \mapsto e^{i\theta}z$), we ask: what *are* all of them? The answer is striking and clean: the group $\operatorname{Aut}(\mathbb{D})$ consists exactly of the Möbius transformations of the form $e^{i\theta}(z - a)/(1 - \bar a z)$ for $\theta \in \mathbb{R}, a \in \mathbb{D}$.

This is a 3-real-parameter family (parameters $\theta$ and the real and imaginary parts of $a$). It is the simplest nontrivial automorphism group in complex analysis, and it has a beautiful structure: the group $\operatorname{Aut}(\mathbb{D})$ is isomorphic to $\operatorname{PSU}(1, 1)$, the projective special unitary group of signature $(1, 1)$ — equivalently, $\operatorname{PSL}_2(\mathbb{R})$ via the Cayley transform.

This group has a geometric interpretation: it is the **isometry group of the Poincaré disc model of hyperbolic geometry**. The Poincaré metric $ds^2 = 4|dz|^2/(1 - |z|^2)^2$ on $\mathbb{D}$ makes the disc into the hyperbolic plane, and automorphisms of $\mathbb{D}$ preserve this metric exactly.

The proof has two steps: first, show that any automorphism fixing the origin must be a rotation (this is the Schwarz lemma applied twice). Second, reduce the general case to fixing the origin by pre-composing with a Möbius transformation that moves the fixed point to the origin.

---

# Sources and Targets

**Sources (Input Broadening)**

**Biholomorphism $\mathbb{D} \to \mathbb{D}$.** The standard hypothesis.

**Holomorphic bijection of $\mathbb{D}$.** Equivalent. Biholomorphism is automatic by [[Thm - Holomorphic Inverse Function Theorem|the holomorphic inverse function theorem]] applied at every point (since the bijection has nowhere-zero derivative by Schwarz).

**A specific automorphism with known fixed point.** Property $B$: an automorphism $f$ with $f(a) = a$ for some $a \in \mathbb{D}$. Bridge: compose with Möbius to reduce to $a = 0$; then $f$ is a rotation.

**Targets (Output Amplification)**

Combine with **the Riemann mapping theorem.** Property $D$: a biholomorphism $\phi : U \to \mathbb{D}$ exists from a simply connected $U \subset \mathbb{C}$. Amplified result $E$: all biholomorphisms $U \to \mathbb{D}$ are $\phi$ composed with an element of $\operatorname{Aut}(\mathbb{D})$ — a 3-parameter family.

Combine with **hyperbolic isometries.** Property $D$: the Poincaré disc model. Amplified result $E$: orientation-preserving isometries of the hyperbolic plane are exactly $\operatorname{Aut}(\mathbb{D})$, leading to the rich theory of hyperbolic surfaces and Fuchsian groups.

---

# Why Is It True

The proof has two steps.

**Step 1: Automorphisms fixing $0$ are rotations.** If $f \in \operatorname{Aut}(\mathbb{D})$ with $f(0) = 0$, apply Schwarz's lemma: $|f(z)| \leq |z|$ and $|f'(0)| \leq 1$. Now $f^{-1}$ is also in $\operatorname{Aut}(\mathbb{D})$ with $f^{-1}(0) = 0$, so by Schwarz applied to $f^{-1}$: $|f^{-1}(w)| \leq |w|$ for all $w \in \mathbb{D}$, equivalently $|f(z)| \geq |z|$ for all $z \in \mathbb{D}$ (substituting $w = f(z)$).

Combining: $|f(z)| = |z|$ for all $z \in \mathbb{D}$. By the equality case of Schwarz, $f$ is a rotation: $f(z) = e^{i\theta}z$ for some $\theta \in \mathbb{R}$.

**Step 2: General automorphism via Möbius reduction.** Let $f \in \operatorname{Aut}(\mathbb{D})$ be arbitrary, and let $a = f^{-1}(0) \in \mathbb{D}$ (the preimage of $0$). The Blaschke factor $B_a(z) = (z - a)/(1 - \bar a z)$ is a Möbius transformation. *Check it is in $\operatorname{Aut}(\mathbb{D})$*: $B_a(a) = 0$, $B_a(1/\bar a) = \infty$ (sending the inversive point of $a$ to $\infty$), and on $|z| = 1$: $|B_a(z)|^2 = |z - a|^2/|1 - \bar a z|^2$. Using $|z| = 1 \Rightarrow \bar z = 1/z$, $|1 - \bar a z|^2 = (1 - \bar a z)(1 - a\bar z) = 1 - \bar a z - a\bar z + |a|^2$ and $|z - a|^2 = (z - a)(\bar z - \bar a) = 1 - a\bar z - \bar a z + |a|^2$, so they're equal. Hence $|B_a(z)| = 1$ on $|z| = 1$, and $B_a$ maps $\mathbb{D}$ to $\mathbb{D}$ (by maximum modulus, or direct verification at $0$: $B_a(0) = -a$, $|{-a}| < 1$).

Now $f \circ B_a^{-1} : \mathbb{D} \to \mathbb{D}$ is an automorphism (composition of automorphisms) and fixes $0$ (since $B_a^{-1}(0) = a$ and $f(a) = 0$, so $f \circ B_a^{-1}(0) = f(a) = 0$). By Step 1, $f \circ B_a^{-1}(z) = e^{i\theta}z$, so $f(z) = e^{i\theta}B_a(z) = e^{i\theta}(z - a)/(1 - \bar a z)$.

So every automorphism has this form.

---

# What Makes This Hard

The non-obvious step is **using Schwarz's lemma twice** — once for $f$, once for $f^{-1}$ — to get $|f(z)| = |z|$ exactly. A common mistake is to apply Schwarz only to $f$ and conclude $|f(z)| \leq |z|$, but this doesn't give equality.

The second non-obvious step is the **Möbius reduction to the fixed-point case**. The Blaschke factor $B_a$ is the canonical Möbius transformation sending $a$ to $0$ while preserving $\mathbb{D}$. Many alternative reductions are conceivable, but $B_a$ is the cleanest.

---

# Rederivation Scaffold

**High-level strategy:**
Reduce to the fixed-point-at-$0$ case using a Blaschke factor. For $f \in \operatorname{Aut}(\mathbb{D})$ with $f(0) = 0$: apply Schwarz to $f$ and $f^{-1}$ to get $|f(z)| = |z|$, hence $f$ is a rotation.

**Subgoal decomposition:**

1. **Blaschke factor $B_a$.** For $a \in \mathbb{D}$: $B_a(z) = (z - a)/(1 - \bar a z)$ is an automorphism of $\mathbb{D}$ with $B_a(a) = 0$.

2. **General $f \in \operatorname{Aut}(\mathbb{D})$.** Let $a = f^{-1}(0)$; consider $g = f \circ B_a^{-1}$, which is in $\operatorname{Aut}(\mathbb{D})$ and fixes $0$.

3. **$g$ fixing $0$ is a rotation.** By Schwarz applied to $g$ and to $g^{-1}$, $|g(z)| = |z|$. By the equality case of Schwarz, $g(z) = e^{i\theta}z$.

4. **Reconstruct $f$.** $f = g \circ B_a$, so $f(z) = e^{i\theta}B_a(z) = e^{i\theta}(z - a)/(1 - \bar a z)$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **Step 1: Blaschke factor is in $\operatorname{Aut}(\mathbb{D})$.** For $a \in \mathbb{D}$ define $B_a(z) = (z - a)/(1 - \bar a z)$. This is a Möbius transformation. To verify $B_a$ maps $\mathbb{D}$ to $\mathbb{D}$: on $|z| = 1$, $|1 - \bar a z|^2 = 1 - \bar a z - a\bar z + |a|^2 = 1 - 2\operatorname{Re}(\bar a z) + |a|^2$ and $|z - a|^2 = 1 - 2\operatorname{Re}(\bar a z) + |a|^2$, equal. So $|B_a(z)| = 1$ on $|z| = 1$. At $z = 0$: $B_a(0) = -a$, $|-a| < 1$, so $B_a(0) \in \mathbb{D}$. By the maximum/minimum principle for $|B_a|$ on $\overline{\mathbb{D}}$, $|B_a|$ is bounded by $1$ on $\mathbb{D}$ and strictly less on the open disc. So $B_a : \mathbb{D} \to \mathbb{D}$, and similarly $B_a^{-1}$ exists and maps $\mathbb{D}$ to $\mathbb{D}$.
>
> The inverse: $B_a^{-1}(w) = B_{-a}(w) = (w + a)/(1 + \bar a w)$ — direct computation.
>
> **Step 2: Reduction to fixing $0$.** Let $f \in \operatorname{Aut}(\mathbb{D})$. Set $a = f^{-1}(0) \in \mathbb{D}$. Define $g = f \circ B_a^{-1}$. Then $g \in \operatorname{Aut}(\mathbb{D})$ (composition of automorphisms), and $g(0) = f(B_a^{-1}(0)) = f(a) = 0$ (using $B_a^{-1}(0) = B_{-a}(0) = -(-a) = a$, wait, that doesn't look right; let me check: $B_a^{-1}(w) = (w + a)/(1 + \bar a w)$, so $B_a^{-1}(0) = a$. Yes, that's correct).
>
> So $g$ is an automorphism fixing $0$.
>
> **Step 3: Automorphism fixing $0$ is a rotation.** Apply [[Thm - Schwarz Lemma|Schwarz's lemma]] to $g$: $|g(z)| \leq |z|$ for all $z \in \mathbb{D}$, $|g'(0)| \leq 1$.
>
> Apply Schwarz to $g^{-1}$ (also in $\operatorname{Aut}(\mathbb{D})$ fixing $0$): $|g^{-1}(w)| \leq |w|$ for all $w \in \mathbb{D}$. Substituting $w = g(z)$: $|z| \leq |g(z)|$.
>
> Combining: $|g(z)| = |z|$ for all $z \in \mathbb{D}$. By the equality case of Schwarz, $g(z) = e^{i\theta}z$ for some $\theta \in \mathbb{R}$.
>
> **Step 4: Reconstruct $f$.** $g = f \circ B_a^{-1}$, so $f = g \circ B_a$, giving $f(z) = e^{i\theta}B_a(z) = e^{i\theta}(z - a)/(1 - \bar a z)$.
>
> **Step 5: Converse.** Any map of the form $f(z) = e^{i\theta}(z - a)/(1 - \bar a z)$ with $\theta \in \mathbb{R}, a \in \mathbb{D}$ is a composition of a Blaschke factor (automorphism) and a rotation (automorphism), hence an automorphism of $\mathbb{D}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Number of fixed points.** A Möbius transformation has at most two fixed points on $\hat{\mathbb{C}}$ (its fixed points are roots of $cz^2 + (d - a)z - b = 0$, a degree-$\leq 2$ polynomial). For an automorphism of $\mathbb{D}$: exactly one fixed point in $\mathbb{D}$ (if non-identity), determined by $a \in \mathbb{D}$.

**Hyperbolic distance.** The hyperbolic distance from $0$ to a point $z \in \mathbb{D}$ in the Poincaré metric is $\log((1 + |z|)/(1 - |z|))$. Automorphisms of $\mathbb{D}$ preserve this distance — they are the isometries of the hyperbolic plane.

**Subgroup structure.** $\operatorname{Aut}(\mathbb{D})$ has a one-parameter subgroup of rotations ($a = 0$), a two-parameter family of translations-by-Blaschke (modulo rotations), and the natural identification with $\operatorname{PSU}(1, 1) \cong \operatorname{PSL}_2(\mathbb{R})$.

---

# Bridges

- **[[Thm - Schwarz Lemma]]** — the engine.

- **[[Def - Möbius Transformation]]** — Blaschke factors are Möbius.

- **[[Thm - Riemann Mapping Theorem (Statement)]]** — uniqueness of biholomorphism is up to $\operatorname{Aut}(\mathbb{D})$.

---

# Unlocked by This

> [!tip] Hyperbolic Geometry *(from Differential Geometry)*
> $\operatorname{Aut}(\mathbb{D})$ is the orientation-preserving isometry group of the **Poincaré disc model** of the hyperbolic plane. The deep theory of hyperbolic surfaces and Fuchsian groups builds on this.

> [!tip] Hardy Spaces and Reproducing Kernels *(from Functional Analysis)*
> The Hardy space $H^2(\mathbb{D})$ of square-integrable boundary values of holomorphic functions has automorphisms of $\mathbb{D}$ acting on it as isometries (up to scaling by the Blaschke factor). This connects to operator theory and signal processing.
