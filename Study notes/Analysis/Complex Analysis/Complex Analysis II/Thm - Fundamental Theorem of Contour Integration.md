---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Contour Integral"
  - "Def - Primitive (Antiderivative)"
  - "Def - Curve and C1 Curve"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ open; $f : U \to \mathbb{C}$ continuous; $F : U \to \mathbb{C}$ a primitive of $f$ on $U$ (holomorphic, $F' = f$); $\gamma : [a, b] \to U$ piecewise $C^1$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

The complex analog of the fundamental theorem of calculus. In real one-variable analysis, $\int_a^b f(x)\,dx = F(b) - F(a)$ where $F' = f$. The complex version: $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$, where the integral is along *any* curve $\gamma$ from $\gamma(a)$ to $\gamma(b)$ in $U$. The integral depends only on the endpoints, not on the path — *provided $f$ has a primitive on $U$*. This is the "path-independence" theorem.

The immediate consequence: $\int_\gamma f\,dz = 0$ for every closed loop $\gamma$ in $U$ (since $\gamma(a) = \gamma(b)$). This is the local form of Cauchy's theorem — and indeed, the way Cauchy's theorem on simply connected domains is *proved* is by constructing a primitive.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ has a primitive $F$ on $U$".

The first disguised source is **$f$ is holomorphic on a simply connected domain**: then by Cauchy's theorem (see [[Thm - Cauchy's Theorem for a Star-Shaped Domain]] and its extensions), $f$ has a primitive, and the FT applies.

The second disguised source is **$f$ is a derivative of a known function**: e.g., $f(z) = z^n$ has primitive $z^{n+1}/(n+1)$ on $\mathbb{C}$ (for $n \neq -1$); $f(z) = e^z$ has primitive $e^z$; $f(z) = 1/z$ has primitive $\log z$ on simply connected $U \subseteq \mathbb{C}^\times$. So integrals of these against any curve evaluate via endpoints.

**Targets (Output Amplification)**

The conclusion is "$\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$".

Combine with **path independence.** Property $D$: two paths $\gamma_1, \gamma_2$ from $z_1$ to $z_2$. The amplified result: $\int_{\gamma_1} f\,dz = \int_{\gamma_2} f\,dz$. Used to deform contours.

Combine with **closed-loop vanishing.** Property $D$: $\gamma$ closed. The amplified result: $\int_\gamma f\,dz = 0$. This is the local Cauchy theorem.

---

# Why Is It True

The proof is the chain rule applied to the composition $F \circ \gamma$, integrated.

For $C^1$ $\gamma$: by the chain rule, $(F \circ \gamma)'(t) = F'(\gamma(t))\gamma'(t) = f(\gamma(t))\gamma'(t)$. So $F \circ \gamma : [a, b] \to \mathbb{C}$ is a real-parameter primitive of the integrand of $\int_\gamma f\,dz$. By the real-variable fundamental theorem of calculus:
$$\int_a^b f(\gamma(t))\gamma'(t)\,dt = [F(\gamma(t))]_a^b = F(\gamma(b)) - F(\gamma(a)).$$
That is the entire argument. The piecewise case adds up: on each $C^1$ piece, the formula holds; summing telescopes.

The deep observation: this is *exactly* the same proof as the real one-variable fundamental theorem of calculus, with the difference being that we are integrating along a *parametrized curve in $\mathbb{C}$* rather than along an interval in $\mathbb{R}$. The chain rule respects the complex structure, and the integration is reduced to a real integral over $[a, b]$.

---

# What Makes This Hard

The conceptual difficulty is appreciating that the result *depends on the existence of $F$* — and existence is itself a hard, topology-dependent question. The proof is trivial once $F$ exists. The error to avoid: applying the theorem when $f$ does *not* have a primitive on $U$ (e.g., $1/z$ on $\mathbb{C}^\times$). The conclusion "integrals around loops vanish" is then false, as $\int_{|z|=1} dz/z = 2\pi i$.

---

# Rederivation Scaffold

**High-level strategy:**
Apply the chain rule to $F \circ \gamma$ to get $(F \circ \gamma)'(t) = f(\gamma(t))\gamma'(t)$. Apply the real fundamental theorem of calculus on $[a, b]$.

**Subgoal decomposition:**

1. **For $C^1$ $\gamma$.** Apply chain rule, integrate.
2. **For piecewise $C^1$.** Sum over pieces; the endpoint values telescope.

---

# Lemma Decomposition

> [!note]- Lemma 1: $C^1$ case
> **Statement:** For $C^1$ $\gamma : [a, b] \to U$: $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$.
>
> **Hint:** Chain rule + real FTC.
>
> > [!note]- Full proof
> > By the chain rule on the composition $F \circ \gamma$ (with $F$ complex differentiable, $\gamma$ real differentiable): $(F \circ \gamma)'(t) = F'(\gamma(t)) \gamma'(t) = f(\gamma(t))\gamma'(t)$. By the real one-variable fundamental theorem of calculus (applied separately to real and imaginary parts of $F \circ \gamma$):
> > $$\int_\gamma f\,dz = \int_a^b f(\gamma(t))\gamma'(t)\,dt = \int_a^b (F \circ \gamma)'(t)\,dt = F(\gamma(b)) - F(\gamma(a)). \quad \blacksquare$$

> [!note]- Lemma 2: Piecewise $C^1$ case
> **Statement:** For piecewise $C^1$ $\gamma$ with partition $a = t_0 < t_1 < \ldots < t_n = b$ and $\gamma|_{[t_{i-1}, t_i]}$ $C^1$: $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$.
>
> > [!note]- Full proof
> > By Lemma 1 applied to each piece: $\int_{\gamma|_{[t_{i-1}, t_i]}} f\,dz = F(\gamma(t_i)) - F(\gamma(t_{i-1}))$. Summing over $i = 1, \ldots, n$ telescopes to $F(\gamma(t_n)) - F(\gamma(t_0)) = F(\gamma(b)) - F(\gamma(a))$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Combine Lemmas 1 and 2. For $\gamma$ closed ($\gamma(a) = \gamma(b)$), the conclusion is $\int_\gamma f\,dz = 0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Computing $\int z^n\,dz$ on any curve.** For $n \neq -1$, primitive $z^{n+1}/(n+1)$ on $\mathbb{C}$ (or $\mathbb{C}^\times$ for $n < -1$); the integral is the endpoint difference. For $n = -1$: no global primitive, theorem inapplicable, must compute directly — and the integral around a loop is *nonzero*.

**Integrals of $e^z$ along arbitrary paths.** Primitive $e^z$ on $\mathbb{C}$, so $\int_\gamma e^z\,dz = e^{\gamma(b)} - e^{\gamma(a)}$. Independent of path. Trivializes a class of integrals.

**Path-independence as a feature.** The theorem says: when a primitive exists, the integral is independent of the path. In physics, this is conservation of energy in a conservative force field. The "no primitive on $\mathbb{C}^\times$" obstruction for $1/z$ is the topological analog of a non-conservative force.

---

# Bridges

- **[[Def - Primitive (Antiderivative)]]** — the object whose existence makes the theorem applicable.

- **[[Thm - Existence of a Primitive iff Closed Integrals Vanish]]** — the converse direction: vanishing of closed-loop integrals implies existence of a primitive.

- **[[Thm - Cauchy's Theorem for a Star-Shaped Domain]]** — provides primitives on star-shaped domains via integration.
