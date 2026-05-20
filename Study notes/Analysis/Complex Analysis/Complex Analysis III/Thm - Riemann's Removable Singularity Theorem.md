---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Isolated Singularity"
  - "Def - Removable Singularity, Pole, Essential Singularity"
  - "Thm - Laurent Series Theorem"
tags: [analysis, complex-analysis]
---

# Notation

$a \in \mathbb{C}$ is an isolated singularity of $f$, holomorphic on $D(a, R) \setminus \{a\}$. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Motivation

Faced with a holomorphic function on a punctured disc, the first question is: does the puncture matter? Sometimes the function is well-defined and well-behaved as you approach the puncture; sometimes it blows up; sometimes it does worse. Riemann's removable singularity theorem gives the cleanest possible characterization of the first case — *the singularity is removable if and only if $f$ is bounded near $a$*.

This is a remarkably strong statement. *Boundedness* is a soft analytic condition; *removability* is a strong holomorphic condition (the function extends to a holomorphic function on the full disc). The theorem says these are equivalent. The reason: holomorphic functions are extraordinarily rigid — any local boundedness immediately forces them into the rigid framework of power series, with no room for true singular behaviour.

The corollary: to check whether a singularity is removable, you do not need to compute the Laurent expansion; you only need to check $f$ is bounded near $a$. This collapses an *infinite* test (every Laurent coefficient $c_n$ for $n < 0$ must be zero) to a *finite* test (sup of $|f|$ near $a$ is finite).

This theorem is a foundational tool throughout complex analysis. It is used to extend functions across removable singularities, to prove the Riemann mapping theorem, to characterize meromorphic functions, and to set up many contour integration arguments where one needs to know a function extends holomorphically.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ bounded near $a$, $a$ an isolated singularity". The sources broaden this.

The first disguised source is **$f$ has limit at $a$.** Property $B$: $\lim_{z \to a} f(z)$ exists in $\mathbb{C}$. Bridge: existence of a finite limit implies boundedness in a neighborhood. Trigger: a function that "should" be defined at $a$ but is technically not (because the formula has a removable indeterminacy).

The second disguised source is **$f(z)(z - a) \to 0$ as $z \to a$.** Property $B$: $(z - a)f(z) \to 0$. Bridge: this is weaker than boundedness of $f$, but stronger than what's needed to rule out a pole (a pole has $|f(z)| \geq C/|z - a|$, so $(z-a)f(z) \not\to 0$). Riemann's theorem (in this form) says this is equivalent to removability — this is the cleanest form, because it directly excludes both poles and essential singularities. See the formal statement below.

The third disguised source is **$f$ is the difference quotient of a $C^1$ function.** Property $B$: $f(z) = (g(z) - g(a))/(z - a)$ for a holomorphic $g$. Bridge: this function is bounded near $a$ (by the difference quotient bound), hence has a removable singularity, hence extends to $g'(a)$. This is the standard "difference quotient extends to derivative" application.

The fourth disguised source is **$f$ extends continuously to $a$.** Property $B$: $f$ has a continuous extension to $D(a, R)$. Bridge: continuous on a compact disc implies bounded. Conclusion: continuous extension is enough; holomorphic extension follows.

**Targets (Output Amplification)**

The conclusion is "$f$ extends holomorphically to $D(a, R)$".

Combine with **the chain of holomorphic operations.** Property $D$: $g(z) = f(z)^2, f(z) + h(z), \int_\gamma f, \ldots$ — once $f$ extends holomorphically, all standard operations on it also extend. Amplified result $E$: arguments that were "modulo finitely many points" become "everywhere", and one can apply Cauchy theory in the extended domain.

Combine with **the structure of the extended function at $a$.** Property $D$: the extended $f$ has a Taylor expansion $f(z) = \sum_{n \geq 0} c_n (z - a)^n$ near $a$. Amplified result $E$: the *order of vanishing* of $f$ at $a$ — the smallest $n$ with $c_n \neq 0$ — is a well-defined non-negative integer. So $f$ has the structure of either a zero of finite order, or being identically zero locally.

Combine with **a sequence of removable singularities.** Property $D$: $f$ holomorphic on $U$ minus a discrete set $S$, with $f$ bounded near each point of $S$. Amplified result $E$: by Riemann at each point separately, $f$ extends to a function holomorphic on $U$. Used in the proof of many "extension across discrete sets" theorems.

---

# Why Is It True

The intuition: a *holomorphic* function on a punctured disc that does not blow up at the puncture must be "trying" to extend holomorphically — and the rigidity of holomorphic functions does not allow it to fail to extend.

More concretely: consider $g(z) = (z - a)^2 f(z)$, extended to $a$ by $g(a) = 0$. If $f$ is bounded near $a$, then $g(z) \to 0$ as $z \to a$ (because $(z - a)^2 \to 0$ and $f$ stays bounded), so $g$ is continuous at $a$. Moreover, $g$ is differentiable at $a$ with $g'(a) = \lim_{z \to a} (g(z) - 0)/(z - a) = \lim (z - a) f(z) = 0$ (again because $f$ bounded, $(z-a) \to 0$). So $g$ is holomorphic on $D(a, R)$ with $g(a) = 0, g'(a) = 0$.

Expanding $g$ in a Taylor series around $a$: $g(z) = c_2(z - a)^2 + c_3(z - a)^3 + \ldots$ (no $c_0$ or $c_1$ term, since $g(a) = g'(a) = 0$). Dividing by $(z - a)^2$ gives $f(z) = c_2 + c_3(z - a) + \ldots$ — a Taylor series around $a$. So $f$ extends holomorphically with $f(a) = c_2 = g''(a)/2$.

The key conceptual move is multiplying by $(z - a)^2$ to "tame" the singularity into a holomorphic function on the disc, then *dividing* the Taylor coefficients of $g$ to get a Taylor expansion of $f$. This is the recurring trick for working with singularities: multiply by enough $(z - a)$ to eliminate negative-power terms, then read off the resulting Taylor expansion.

The boundedness assumption is what makes the multiplication work: $(z - a)^k f(z)$ would generally not extend continuously to $a$, but if $f$ is bounded, even $(z - a)$ — let alone $(z - a)^2$ — kills the magnitude to zero. The factor $(z - a)^2$ is used (rather than $(z - a)^1$) to get not just $g(a) = 0$ but also $g'(a) = 0$, which is what is needed for the Taylor series of $g$ to start at $(z - a)^2$ and hence yield a Taylor series for $f$ after division.

---

# What Makes This Hard

The non-obvious step is **multiplying by $(z - a)^2$ to construct an auxiliary function $g$ that extends holomorphically across $a$, then reading off the Taylor expansion of $f$ from the Taylor expansion of $g$**. The common mistake is to try to extend $f$ directly — for instance, by defining $f(a) = \lim_{z \to a} f(z)$ — and then trying to verify holomorphicity at $a$ from this; the limit may exist by boundedness (passing to a subsequence) but proving the *complex* differentiability at $a$ without the multiplication trick is hard. A second slip is to use $(z - a)^1$ instead of $(z - a)^2$; this gives $g(a) = 0$ but not $g'(a) = 0$, so the Taylor series of $g$ may start at $(z - a)^1$, and dividing gives a constant — fine, but missing one degree of regularity needed in some applications.

---

# Rederivation Scaffold

**High-level strategy:**
Define $g(z) = (z - a)^2 f(z)$ with $g(a) = 0$. Show $g$ is holomorphic on $D(a, R)$ (continuous and complex differentiable at $a$ thanks to boundedness of $f$). Taylor-expand $g$; its expansion has zero $c_0, c_1$ terms; divide by $(z - a)^2$ to get the Taylor expansion of $f$.

**Subgoal decomposition:**

1. **Define $g(z) = (z - a)^2 f(z)$ with $g(a) = 0$.** Show $g$ is continuous at $a$.
   - *Hint:* $(z - a)^2 \to 0$ and $f$ bounded, so $g(z) \to 0 = g(a)$.

2. **Show $g$ is holomorphic at $a$ with $g'(a) = 0$.** Compute $g'(a) = \lim_{z \to a}(g(z) - g(a))/(z - a) = \lim (z - a) f(z) = 0$ by boundedness of $f$.

3. **Taylor-expand $g$ on $D(a, R)$.** $g(z) = \sum_{n \geq 0} c_n (z - a)^n$ converging on $D(a, R)$. From $g(a) = 0, g'(a) = 0$, conclude $c_0 = c_1 = 0$. So $g(z) = \sum_{n \geq 2} c_n (z - a)^n$.

4. **Divide by $(z - a)^2$.** $f(z) = g(z)/(z - a)^2 = \sum_{n \geq 2} c_n (z - a)^{n - 2} = \sum_{k \geq 0} c_{k+2}(z - a)^k$. This is a Taylor series for $f$ on $D(a, R) \setminus \{a\}$, and extends to $D(a, R)$ by setting $f(a) = c_2$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $(z - a)^2 f(z)$ with value $0$ at $a$ is holomorphic
> **Statement:** If $f$ is holomorphic on $D(a, R) \setminus \{a\}$ and bounded by $M$ near $a$, then $g(z) := (z - a)^2 f(z)$ (with $g(a) := 0$) is holomorphic on $D(a, R)$.
>
> **Hint:** Continuity at $a$ from boundedness; complex differentiability at $a$ from the limit $(z - a) f(z) \to 0$.
>
> > [!note]- Full proof
> > *Continuity at $a$.* $|g(z)| = |z - a|^2 |f(z)| \leq M |z - a|^2 \to 0$ as $z \to a$. So $g$ is continuous at $a$ with $g(a) = 0$.
> >
> > *Complex differentiability at $a$.* The difference quotient: $(g(z) - g(a))/(z - a) = (z - a) f(z)$. Then $|(z - a) f(z)| \leq M |z - a| \to 0$ as $z \to a$. So the difference quotient tends to $0$, i.e., $g'(a) = 0$.
> >
> > *Holomorphicity on $D(a, R) \setminus \{a\}$ already given* (product of holomorphic). So $g$ is holomorphic on $D(a, R)$ with $g(a) = 0, g'(a) = 0$.

> [!note]- Lemma 2: Taylor series of $g$ has no $(z - a)^0$ or $(z - a)^1$ term
> **Statement:** With $g$ as above, $g(z) = \sum_{n \geq 2} c_n (z - a)^n$ on $D(a, R)$, with $c_n = g^{(n)}(a)/n!$.
>
> **Hint:** $g$ holomorphic ⟹ Taylor series; $g(a) = 0 \implies c_0 = 0$; $g'(a) = 0 \implies c_1 = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> Suppose $f$ is holomorphic on $D(a, R) \setminus \{a\}$ and bounded near $a$, say $|f(z)| \leq M$ on $D(a, r_0) \setminus \{a\}$ for some $r_0 \leq R$.
>
> **Step 1.** Define $g(z) := (z - a)^2 f(z)$ on $D(a, R) \setminus \{a\}$, extended by $g(a) := 0$. By Lemma 1, $g$ is holomorphic on $D(a, R)$ with $g(a) = g'(a) = 0$.
>
> **Step 2.** By the Taylor series expansion for holomorphic functions, $g(z) = \sum_{n \geq 0} c_n (z - a)^n$ converging on $D(a, R)$. Since $g(a) = g'(a) = 0$, $c_0 = c_1 = 0$. So $g(z) = \sum_{n \geq 2} c_n (z - a)^n$.
>
> **Step 3.** On $D(a, R) \setminus \{a\}$, divide by $(z - a)^2$:
> $$f(z) = \frac{g(z)}{(z - a)^2} = \sum_{n \geq 2} c_n (z - a)^{n - 2} = \sum_{k \geq 0} c_{k + 2}(z - a)^k.$$
> The right-hand side is a power series converging on $D(a, R)$, defining a holomorphic function $F$ on $D(a, R)$ with $F(z) = f(z)$ on $D(a, R) \setminus \{a\}$ and $F(a) = c_2$. So $f$ extends holomorphically to $D(a, R)$ via $F$. $\blacksquare$

**Alternative formulation.** The theorem also says: $a$ is removable iff $(z - a) f(z) \to 0$ as $z \to a$. *Proof:* if removable, $f$ is bounded near $a$, so $(z - a)f \to 0$. Conversely, if $(z - a)f(z) \to 0$, define $g(z) = (z - a)^2 f(z)$ as above; then $g$ is continuous at $a$ (since $g(z) = (z-a)\cdot (z-a)f(z) \to 0\cdot 0 = 0$) and differentiable at $a$ (since $g(z)/(z-a) = (z-a)f(z) \to 0$); the rest of the argument is identical.

---

# Cross-Field Exercise Suggestions

**Difference quotient extension.** If $f$ is holomorphic on $U$ and $a \in U$, the function $g(z) = (f(z) - f(a))/(z - a)$ has a (potential) singularity at $a$, but it is bounded (by the mean value theorem in a small neighborhood, $|g| \leq \sup|f'|$). By Riemann's theorem, $g$ extends holomorphically to $a$, with $g(a) = f'(a)$.

**Extending holomorphic functions across discrete sets.** If $f$ is holomorphic on $U \setminus S$ for a discrete $S \subseteq U$, and $f$ is bounded near every point of $S$, then $f$ extends holomorphically to $U$. Apply Riemann at each point of $S$ separately. This is the key extension theorem used in many constructions.

**Limit of holomorphic functions.** If $f_n \to f$ pointwise on $U$ with $|f_n| \leq M$ uniformly, and $f_n$ are holomorphic, then $f$ extends to a holomorphic function — but this requires a separate convergence argument (Vitali's theorem, normal families). Riemann's theorem is the local-singularity version.

**Schwarz reflection principle.** A function holomorphic on the upper half-disc and continuous up to the real boundary, taking real values on the boundary, extends holomorphically to the full disc by reflection. The reflection construction uses Riemann's theorem to verify the extended function is holomorphic on the boundary.

---

# Bridges

- **[[Def - Removable Singularity, Pole, Essential Singularity]]** — the trichotomy that Riemann's theorem makes operational for the removable case.

- **[[Thm - Pole Characterization]]** — the analogous characterization for poles ($|f| \to \infty$).

- **[[Thm - Casorati–Weierstrass]]** — the analogous characterization (in a weak form) for essential singularities.

- **[[Thm - Laurent Series Theorem]]** — Riemann's theorem says the Laurent expansion has zero negative-power coefficients when $f$ is bounded; this is the implicit content.

---

# Unlocked by This

> [!tip] Maximum Modulus and Schwarz Lemma *(from §3.5+)*
> The boundedness ⇒ removability principle is what allows the [[Thm - Schwarz Lemma|Schwarz lemma]] to be applied: $f(z)/z$ is bounded near $0$ when $f(0) = 0$, hence extends holomorphically, and the extension is then bounded by maximum modulus.

> [!tip] Algebraic Geometry — Curves and Removable Singularities *(from Algebraic Geometry)*
> The algebraic analog of Riemann's theorem: a rational function on a smooth algebraic curve that is bounded in a neighborhood of a closed point extends regularly across that point. This is the foundational fact that makes the algebraic-geometric notion of "regular function on a curve" coincide with the analytic notion in characteristic 0.
