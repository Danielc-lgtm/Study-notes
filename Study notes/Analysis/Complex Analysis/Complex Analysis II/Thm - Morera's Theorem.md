---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Contour Integral"
  - "Thm - Goursat's Theorem (Cauchy for a Triangle)"
  - "Thm - Existence of a Primitive iff Closed Integrals Vanish"
  - "Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)"
tags: [analysis, complex-analysis]
---

# Notation

$D \subseteq \mathbb{C}$ a domain (or just a disc); $f : D \to \mathbb{C}$ continuous. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

Morera's theorem is the partial converse to Goursat: it says vanishing of triangle integrals (or equivalently, all closed-curve integrals) of a *continuous* function $f$ forces $f$ to be holomorphic. This converts a hypothesis about *integrals* into a conclusion about *differentiability*.

This is the standard tool for proving an "unknown" function is holomorphic — typically functions defined as integrals, infinite series, or limits, where we can verify the integral condition more easily than direct complex differentiability. The signature application is to show that uniform limits of holomorphic functions are holomorphic.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ continuous on $D$, $\int_\Delta f\,dz = 0$ for every triangle $\Delta \subseteq D$".

The first disguised source is **$f = \lim f_n$ uniformly on compacts**, where each $f_n$ is holomorphic. Then $\int_\Delta f_n\,dz = 0$ (by Goursat) and by uniform convergence on the compact triangle, $\int_\Delta f\,dz = \lim \int_\Delta f_n\,dz = 0$. So $f$ inherits Morera's hypothesis and is holomorphic.

The second disguised source is **$f$ given as an integral $f(z) = \int_a^b \varphi(z, s)\,ds$** where $\varphi$ is continuous and $\varphi(\cdot, s)$ is holomorphic for each $s$. By Fubini and Cauchy on $\varphi(\cdot, s)$, $\int_\Delta f\,dz = \int_\Delta \int \varphi\,ds\,dz = \int \int_\Delta \varphi\,dz\,ds = 0$. So $f$ is holomorphic. See [[Thm - Holomorphic Dependence on a Parameter]].

The third disguised source is **a function with a known boundary condition or a vanishing condition** on simple test curves. Morera converts this into holomorphicity.

**Targets (Output Amplification)**

The conclusion is "$f$ is holomorphic on $D$".

Combine with **Morera-by-disc.** It suffices to check vanishing of triangle integrals on every disc inside $D$ — by exhaustion of $D$ by discs, holomorphicity on each disc gives global holomorphicity.

---

# Why Is It True

Locally, on any disc $D(w, r) \subseteq D$: by [[Thm - Existence of a Primitive iff Closed Integrals Vanish]] (specifically, the variant via triangles, see Lemma 2.1.6), the vanishing of triangle integrals provides a primitive $F$ on $D(w, r)$ with $F'(z) = f(z)$.

Since $F$ is holomorphic on the disc, by [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)|the analyticity theorem]], $F$ has a power series, hence $F \in C^\infty$, hence $f = F' \in C^\infty$. In particular, $f$ is *holomorphic* (a complex derivative of a holomorphic function is holomorphic, by analyticity).

So on every disc inside $D$, $f$ is holomorphic. Holomorphicity is a local condition, so $f$ is holomorphic on the whole $D$. $\blacksquare$

The deep observation: the *existence of a primitive* from the vanishing condition is the key step. Once a primitive $F$ is available, the analyticity of $F$ propagates to $f = F'$.

---

# What Makes This Hard

The non-obvious step is realizing that the hypothesis can be exploited via the *construction of a local primitive* on each disc. The hypothesis is "global" (in terms of triangle integrals), but the conclusion is "local" (in terms of differentiability), and the bridge is the local primitive. The common error: trying to deduce $f$ is differentiable directly from the integral hypothesis — there is no direct route; the primitive is the intermediary.

---

# Rederivation Scaffold

**High-level strategy:**
On each disc inside $D$, build a primitive $F$ from the vanishing-of-triangles hypothesis. $F$ is holomorphic; by analyticity, $F' = f$ is also holomorphic.

**Subgoal decomposition:**

1. **For each disc inside $D$: build a primitive $F$.** Use Lemma 2.1.6 in Cambridge (existence of primitive from vanishing triangle integrals on a star-shaped domain like a disc).

2. **$F$ holomorphic on the disc.** By construction.

3. **$F$ analytic (locally a power series).** By [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]].

4. **$F'$ holomorphic.** Termwise differentiation of the power series gives a holomorphic derivative.

5. **$f = F'$ holomorphic on the disc, hence on $D$ globally.**

---

# Lemma Decomposition

> [!note]- Lemma 1: Local primitive from triangle vanishing
> **Statement:** If $f$ is continuous on a disc $D(a, r)$ and $\int_\Delta f\,dz = 0$ for every triangle in the disc, then $f$ has a primitive on $D(a, r)$.
>
> **Hint:** Define $F(w) = \int_{[a, w]} f\,dz$ along the line segment from $a$ to $w$. Use vanishing of triangle integrals to show $F$ is well-defined and differentiable.
>
> **Why needed:** Provides the holomorphic primitive whose derivative is $f$.
>
> > [!note]- Full proof
> > Cambridge Lemma 2.1.6: define $F(w) = \int_{[a, w]} f\,dz$ (line segment from $a$ to $w$, in the disc by convexity). For small $h$, the triangle with vertices $a, w, w + h$ lies in the disc; vanishing of its integral gives $F(w + h) - F(w) = \int_{[w, w + h]} f\,dz$, and the difference-quotient argument (as in [[Thm - Existence of a Primitive iff Closed Integrals Vanish]]) shows $F'(w) = f(w)$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix any disc $D(w, r) \subseteq D$. The hypothesis "$\int_\Delta f\,dz = 0$ for every triangle $\Delta$" restricts to this disc.
>
> By Lemma 1 (Cambridge Lemma 2.1.6), $f$ has a primitive $F$ on $D(w, r)$ — i.e., $F$ is holomorphic with $F' = f$.
>
> By [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]], $F$ has a convergent power series on $D(w, r)$, so $F \in C^\infty$ and in particular $F' = f$ is holomorphic (the derivative of a power series is a power series).
>
> Since this holds on every disc inside $D$, $f$ is holomorphic on $D$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Uniform limits of holomorphic functions are holomorphic.** If $f_n \to f$ uniformly on compacts and each $f_n$ holomorphic, then for any triangle $\Delta$: $\int_\Delta f_n\,dz = 0$ (Goursat), and $\int_\Delta f\,dz = \lim \int_\Delta f_n\,dz = 0$ (uniform convergence on the compact triangle). By Morera, $f$ holomorphic. This is the proof of "the space of holomorphic functions is closed under uniform convergence on compacts" — a key fact for Montel's theorem and conformal mapping.

**Holomorphic dependence on a parameter.** $g(z) = \int_a^b \varphi(z, s)\,ds$ for $\varphi$ continuous, holomorphic in $z$. Triangle integrals of $g$ swap with $\int ds$ (Fubini), giving $0$ by Cauchy on each $\varphi(\cdot, s)$. Morera: $g$ holomorphic. See [[Thm - Holomorphic Dependence on a Parameter]].

**Schwarz reflection.** If $f$ is holomorphic on the upper half-disc, continuous on the real diameter, and real-valued there, then $f$ extends across the real axis via $\tilde f(\bar z) = \overline{f(z)}$. Morera (with the real axis treated as a triangle edge) proves the extension is holomorphic. See [[Ex - Schwarz reflection principle (mini-version)]].

---

# Bridges

- **[[Thm - Goursat's Theorem (Cauchy for a Triangle)]]** — the partial inverse direction.

- **[[Thm - Existence of a Primitive iff Closed Integrals Vanish]]** — provides the local primitive.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — gives that the primitive is $C^\infty$, hence so is the derivative.

- **[[Thm - Holomorphic Dependence on a Parameter]]** — the canonical application.
