---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Cauchy Integral Formula"
tags: [analysis, complex-analysis]
---

# Notation

$f$ holomorphic on $D(a, R)$, $0 < r < R$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

The mean value property is the special case of CIF at the centre: the value of $f$ at the centre equals the average over any surrounding circle. This is the *complex* analog of the mean value property of harmonic functions in real analysis — and is the same statement, applied to either component $u$ or $v$ of $f = u + iv$.

The mean value property is the local form of the maximum modulus principle: if $|f(a)|$ is the average of $|f|$ on a circle around it, then $|f(a)|$ cannot exceed the maximum on the circle — equality forces $|f|$ to be constant on the circle.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on $D(a, R)$, $r < R$".

The first disguised source is **$f$ continuous on $\overline{D(a, r)}$, holomorphic inside**: CIF extends to this case, and so does the mean value property.

**Targets (Output Amplification)**

The conclusion is "$f(a) = (1/2\pi)\int_0^{2\pi} f(a + re^{i\theta})\,d\theta$".

Combine with **the modulus.** Property $D$: take $|.|$ of both sides. The amplified result: $|f(a)| \leq (1/2\pi)\int |f(a + re^{i\theta})|\,d\theta \leq \max_\theta |f(a + re^{i\theta})| = M(r)$. This is the **local maximum modulus** principle.

Combine with **harmonic functions.** Property $D$: $u = \operatorname{Re} f$, $v = \operatorname{Im} f$ are harmonic. The amplified result: harmonic functions also satisfy the mean value property — $u(a) = (1/2\pi)\int u(a + re^{i\theta})\,d\theta$. This is the *complex shadow* of the harmonic-function mean value property.

---

# Why Is It True

Direct from CIF with $w = a$:
$$f(a) = \frac{1}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{z - a}\,dz.$$
Parametrize $z = a + re^{i\theta}$, $dz = ire^{i\theta}d\theta$:
$$f(a) = \frac{1}{2\pi i}\int_0^{2\pi}\frac{f(a + re^{i\theta})}{re^{i\theta}}\cdot ire^{i\theta}\,d\theta = \frac{1}{2\pi}\int_0^{2\pi} f(a + re^{i\theta})\,d\theta.$$
The $r$ and $i$ cancel, leaving the average.

---

# What Makes This Hard

Nothing — direct specialization of CIF. The conceptual content is that this is a *strong* averaging property: the value at the centre equals the average over *any* surrounding circle, not just a particular one. This is the analog of the mean value property of harmonic functions, which is itself a strong constraint.

---

# Rederivation Scaffold

**High-level strategy:**
Apply CIF at $w = a$, parametrize the circle.

---

# Lemma Decomposition

(No lemmas needed beyond CIF.)

---

# Formal Proof

> [!note]- Complete formal proof
> By [[Thm - Cauchy Integral Formula]] with $w = a$:
> $$f(a) = \frac{1}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{z - a}\,dz.$$
> Parametrize $z(t) = a + re^{it}$, $t \in [0, 2\pi]$: $z - a = re^{it}, z'(t) = ire^{it}$, so
> $$f(a) = \frac{1}{2\pi i}\int_0^{2\pi}\frac{f(a + re^{it})}{re^{it}} \cdot ire^{it}\,dt = \frac{1}{2\pi}\int_0^{2\pi}f(a + re^{it})\,dt. \quad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Maximum modulus from MVP.** $|f(a)| = |(1/2\pi)\int f(a + re^{it})\,dt| \leq (1/2\pi)\int |f(a + re^{it})|\,dt \leq \max_t |f(a + re^{it})|$. So $|f|$ at the centre is bounded by its max on the surrounding circle. This is the seed of [[Thm - Local Maximum Modulus Principle]].

**Harmonic conjugate identity.** Real and imaginary parts $u, v$ both satisfy the MVP. So for harmonic $u$: $u(a) = (1/2\pi)\int u(a + re^{it})\,dt$. This is the *real-variable* mean value property of harmonic functions in 2D, proved through complex methods.

---

# Bridges

- **[[Thm - Cauchy Integral Formula]]** — the direct source.

- **[[Thm - Local Maximum Modulus Principle]]** — direct consequence: MVP implies the modulus at the centre is bounded by the max on the circle.

- **[[Ex - Gauss's mean value identity for harmonic functions]]** — applying to $u = \operatorname{Re} f, v = \operatorname{Im} f$ gives the harmonic mean value property.
