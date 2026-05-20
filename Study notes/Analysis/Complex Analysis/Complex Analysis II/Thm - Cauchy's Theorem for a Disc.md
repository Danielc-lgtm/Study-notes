---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Cauchy's Theorem for a Star-Shaped Domain"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$D = D(a, r) \subseteq \mathbb{C}$ — an open disc; $f : D \to \mathbb{C}$ holomorphic; $\gamma$ a closed piecewise $C^1$ curve in $D$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Statement

> **Theorem (Cauchy's theorem for a disc).** Let $D = D(a, r) \subseteq \mathbb{C}$ be an open disc and $f : D \to \mathbb{C}$ holomorphic. Then $f$ has a primitive on $D$, and for every closed piecewise $C^1$ curve $\gamma$ in $D$:
> $$\int_\gamma f(z)\,dz = 0.$$

---

# Motivation

The disc version of Cauchy's theorem is the *workhorse* of practical complex analysis. Most local arguments — building primitives, justifying CIF, deriving local power series — happen on a disc, where Cauchy's theorem is automatic. This is a special case of the star-shaped theorem (a disc is star-shaped about any of its points, indeed convex), but it deserves a separate statement because of its universality.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on a disc $D$, $\gamma$ closed in $D$".

The first disguised source is **any holomorphic function on an open set, restricted to a small disc**: every point of an open set has a disc neighbourhood, so disc Cauchy applies locally everywhere.

The second disguised source is **$f$ continuous on $D$, holomorphic except at finitely many points**: the extended Goursat theorem and the star-shaped argument extend to this case.

**Targets (Output Amplification)**

The conclusion is "$\int_\gamma f\,dz = 0$".

Combine with **construction of primitives.** Property $D$: a disc and a holomorphic $f$. The amplified result: $f$ has a primitive on the disc, given by integrating from any base point.

Combine with **the Cauchy integral formula.** Property $D$: a disc and a point $w$ inside, plus a holomorphic $f$. The amplified result: $f(w) = \frac{1}{2\pi i}\oint f(z)/(z - w)\,dz$ — see [[Thm - Cauchy Integral Formula]].

---

# Why Is It True

A disc is convex, hence star-shaped (with respect to any point of the disc, e.g., the centre $a$). By [[Thm - Cauchy's Theorem for a Star-Shaped Domain]], $f$ has a primitive on $D$ and $\int_\gamma f\,dz = 0$ for every closed $\gamma$ in $D$. That is the entire argument.

The disc version is *the* most-used form because most local arguments in complex analysis happen on a small disc neighbourhood.

---

# What Makes This Hard

Nothing genuinely hard — it is a direct specialization of the star-shaped theorem. The only thing to remember: discs are convex, hence star-shaped about every interior point.

---

# Rederivation Scaffold

**High-level strategy:**
Note that the disc is star-shaped. Apply [[Thm - Cauchy's Theorem for a Star-Shaped Domain]].

---

# Lemma Decomposition

> [!note]- Lemma 1: Discs are convex
> **Statement:** An open disc $D(a, r) \subseteq \mathbb{C}$ is convex: for $z_1, z_2 \in D(a, r)$ and $t \in [0, 1]$, $tz_1 + (1-t)z_2 \in D(a, r)$.
>
> > [!note]- Full proof
> > $|tz_1 + (1-t)z_2 - a| = |t(z_1 - a) + (1-t)(z_2 - a)| \leq t|z_1 - a| + (1-t)|z_2 - a| < tr + (1-t)r = r$. So $tz_1 + (1-t)z_2 \in D(a, r)$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $D(a, r)$ is convex, hence star-shaped (with respect to any point). By [[Thm - Cauchy's Theorem for a Star-Shaped Domain]], $\int_\gamma f\,dz = 0$ for every closed piecewise $C^1$ $\gamma$ in $D(a, r)$, and $f$ has a primitive on the disc. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Local primitives everywhere.** For any holomorphic $f$ on an open set $U$, every point $w \in U$ has a disc $D(w, r) \subseteq U$ on which $f$ has a primitive (by this theorem). So holomorphic functions have *local* primitives everywhere; global primitives depend on the topology of $U$.

**Local power series via CIF.** A holomorphic function on a disc has a local power series expansion at every point. This will be proved in [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]] using CIF, which builds on Cauchy on the disc.

---

# Bridges

- **[[Thm - Cauchy's Theorem for a Star-Shaped Domain]]** — the parent theorem.

- **[[Thm - Cauchy Integral Formula]]** — built on top.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — uses disc Cauchy plus CIF to give local power series.
