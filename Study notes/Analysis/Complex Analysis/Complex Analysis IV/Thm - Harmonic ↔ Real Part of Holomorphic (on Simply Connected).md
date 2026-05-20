---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Harmonic Function"
  - "Def - Holomorphic Function"
  - "Def - Simply Connected Domain in Complex Analysis"
  - "Thm - Cauchy's Theorem for Simply Connected Domains"
tags: [analysis, complex-analysis, pde]
---

# Notation

$U \subseteq \mathbb{R}^2 \cong \mathbb{C}$ is a simply connected open set. $u : U \to \mathbb{R}$ is real-valued; $f : U \to \mathbb{C}$ is the holomorphic function whose real part is $u$, with imaginary part $v$ (the **harmonic conjugate**). Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Harmonic ↔ Real Part of Holomorphic).** Let $U \subseteq \mathbb{C}$ be open and simply connected, and let $u : U \to \mathbb{R}$ be a $C^2$ function. Then $u$ is harmonic on $U$ if and only if there exists a holomorphic function $f : U \to \mathbb{C}$ with $\operatorname{Re} f = u$ on $U$.
>
> The imaginary part $v = \operatorname{Im} f$ is called a **harmonic conjugate** of $u$, and is unique up to an additive real constant. Conversely, on any open set (not necessarily simply connected), the real and imaginary parts of every holomorphic function are harmonic.

---

# Motivation

We know: real and imaginary parts of holomorphic functions are harmonic. The converse direction is more subtle: given a harmonic $u$, is there a holomorphic $f$ whose real part is $u$?

The answer: **yes, if the domain is simply connected**. On a non-simply-connected domain, the harmonic conjugate may fail to exist globally — even though it always exists locally. The canonical counterexample: $u(x, y) = \log|z|$ on $\mathbb{C}\setminus\{0\}$ (harmonic) has *no* global harmonic conjugate (the conjugate would be $\arg z$, multivalued).

This theorem reveals the *interplay between harmonic functions and the topology of the domain*. Simple connectivity is precisely the right condition for global harmonic conjugates. Without it, harmonic functions still exist, but they live on a richer space — the universal cover of the domain, where the conjugate exists in a multivalued sense.

The theorem is foundational for the rest of CA IV's harmonic theory: combined with Cauchy theory for holomorphic functions, it transfers all the rigidity properties of holomorphic functions to harmonic functions (mean value property, maximum principle, Liouville-style theorems, etc.).

---

# Sources and Targets

**Sources (Input Broadening)**

**Harmonic on a simply connected domain.** The clean hypothesis.

**Harmonic on a convex domain.** Convex ⟹ simply connected, so directly applies.

**Harmonic on a disc.** Discs are simply connected; harmonic conjugates always exist.

**Harmonic on a domain locally diffeomorphic to a disc.** Even on non-simply-connected domains, harmonic conjugates exist *locally* (on any small disc around any point). The global obstruction is the only issue.

**Targets (Output Amplification)**

Combine with **Cauchy's integral formula for holomorphic functions.** Property $D$: $f = u + iv$ holomorphic. Amplified result $E$: $u$ is recoverable from boundary values via the Poisson kernel — see [[Thm - Poisson Integral Formula]].

Combine with **Liouville's theorem.** Property $D$: $u$ bounded harmonic on $\mathbb{C}$. Amplified result $E$: $u$ is constant. (By applying Liouville to $f$ such that $u = \operatorname{Re} f$.)

Combine with **the maximum/minimum principle.** Property $D$: $u$ harmonic, attaining max on the interior of a domain. Amplified result $E$: $u$ constant (by max modulus principle applied to $e^f$ or similar).

---

# Why Is It True

We have two directions to prove.

**(⇒) Real part of holomorphic is harmonic.** If $f = u + iv$ is holomorphic, the Cauchy-Riemann equations give $u_x = v_y, u_y = -v_x$. Differentiating: $u_{xx} = v_{yx}, u_{yy} = -v_{xy}$. Adding: $u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0$ (by equality of mixed partials, since $u, v$ are smooth). So $u$ is harmonic. Similarly $v$.

**(⇐) Harmonic on simply connected implies real part of holomorphic.** Given $u$ harmonic on simply connected $U$, we construct $v$ such that $f = u + iv$ is holomorphic.

The construction: by Cauchy-Riemann, we need $v_x = -u_y, v_y = u_x$. So $v$ is determined (up to a constant) by its gradient: $\nabla v = (-u_y, u_x)$.

The 1-form $\omega = -u_y\,dx + u_x\,dy$ is the "candidate $dv$". For $\omega$ to be exact (i.e., for $v$ to exist with $dv = \omega$), $\omega$ must be closed: $\partial(-u_y)/\partial y = \partial(u_x)/\partial x$, i.e., $-u_{yy} = u_{xx}$, i.e., $u_{xx} + u_{yy} = 0$. Yes — this is exactly the harmonicity condition!

So $\omega$ is closed. On a simply connected domain, closed 1-forms are exact (the *Poincaré lemma* for simply connected domains, equivalently Cauchy's theorem for the 1-form $\omega$). So $\omega = dv$ for some $v : U \to \mathbb{R}$, unique up to a constant.

Setting $f = u + iv$: by construction, $u_x = v_y, u_y = -v_x$, the Cauchy-Riemann equations. So $f$ is holomorphic.

---

# What Makes This Hard

The non-obvious step is **recognizing that the existence of the harmonic conjugate is a problem in differential forms / homotopy theory**. The 1-form $\omega = -u_y\,dx + u_x\,dy$ is closed iff $u$ is harmonic, and exact iff $v$ exists. *Closed implies exact* on simply connected domains, but not in general — this is the Poincaré lemma / first de Rham cohomology vanishing.

A common error is to define $v$ by an explicit integral $v(z) = \int_{z_0}^z \omega$ without checking the integral is path-independent. On non-simply-connected domains, different paths give different values (differing by integer multiples of $2\pi$ for the $\log|z|$ example), so $v$ is multivalued.

---

# Rederivation Scaffold

**High-level strategy:**
Forward direction: Cauchy-Riemann + equality of mixed partials gives harmonicity. Reverse direction: the 1-form $\omega = -u_y\,dx + u_x\,dy$ is closed by harmonicity, hence exact on simply connected $U$, giving $v$ with $\nabla v = (-u_y, u_x)$. Then $u + iv$ satisfies Cauchy-Riemann.

**Subgoal decomposition:**

1. **(⇒) $f = u + iv$ holomorphic ⟹ $u, v$ harmonic.** Cauchy-Riemann + equality of mixed partials.

2. **(⇐) $u$ harmonic ⟹ exists holomorphic $f$ with $\operatorname{Re} f = u$.**
   a. Construct the candidate 1-form $\omega = -u_y\,dx + u_x\,dy$.
   b. Verify $\omega$ is closed using $u$ harmonic.
   c. Use simple connectivity to conclude $\omega$ is exact: $\omega = dv$.
   d. Verify $f = u + iv$ satisfies Cauchy-Riemann.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **(⇒) Direction.** Let $f = u + iv$ be holomorphic on $U$. Cauchy-Riemann: $u_x = v_y, u_y = -v_x$. Both $u, v$ are smooth (holomorphic ⟹ infinitely differentiable). Differentiating: $u_{xx} = (v_y)_x = v_{yx}$ and $u_{yy} = (-v_x)_y = -v_{xy}$. By equality of mixed partials (smooth), $v_{xy} = v_{yx}$, so
> $$u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0.$$
> Hence $u$ is harmonic. Similarly $v_{xx} + v_{yy} = -u_{xy} + u_{yx} = 0$, so $v$ is harmonic.
>
> **(⇐) Direction.** Let $u : U \to \mathbb{R}$ be harmonic on simply connected $U$.
>
> Define the 1-form $\omega := -u_y\,dx + u_x\,dy$ on $U$. To check $\omega$ is closed: $d\omega = d(-u_y\,dx) + d(u_x\,dy) = -u_{yy}\,dy\wedge dx + u_{xx}\,dx\wedge dy = (u_{xx} + u_{yy})\,dx\wedge dy = 0$, using $u$ harmonic.
>
> On simply connected $U$, every closed 1-form is exact (Poincaré lemma for $\mathbb{R}^2$; equivalent to Cauchy's theorem for the corresponding holomorphic 1-form, after combining with $du = u_x\,dx + u_y\,dy$). So there exists $v : U \to \mathbb{R}$ with $dv = \omega$, i.e., $v_x = -u_y, v_y = u_x$. The $v$ is unique up to an additive constant.
>
> Verify $f = u + iv$ is holomorphic: $u_x = v_y, u_y = -v_x$ are the Cauchy-Riemann equations. By the [[Thm - Cauchy–Riemann Equations|CR equations]], $f$ is holomorphic. $\blacksquare$
>
> **Uniqueness of conjugate.** If $v, \tilde v$ are both harmonic conjugates of $u$ on a connected $U$, then $f - \tilde f = i(v - \tilde v)$ is holomorphic with purely imaginary values, hence (by Cauchy-Riemann or open mapping) constant.

---

# Cross-Field Exercise Suggestions

**Find the harmonic conjugate of $u(x, y) = x^2 - y^2$.** Compute $-u_y = 2y, u_x = 2x$. So $v_x = 2y, v_y = 2x$. Integrate: $v(x, y) = 2xy + C$. Check: $u + iv = x^2 - y^2 + i(2xy) = (x + iy)^2 = z^2$. ✓

**The non-simply-connected obstruction.** On $\mathbb{C}^\times$, $u(x, y) = \log\sqrt{x^2 + y^2} = \log|z|$ is harmonic. Compute $-u_y = -y/(x^2 + y^2), u_x = x/(x^2 + y^2)$. So $v_x = -y/(x^2 + y^2), v_y = x/(x^2 + y^2)$. Integrate $v$ along the path $\gamma$ from $1$ to $z$: $v(z) = \int_\gamma (-y\,dx + x\,dy)/(x^2 + y^2)$. This integral depends on the path's winding number around $0$ (it's $2\pi$ times the winding number). So $v$ is multivalued on $\mathbb{C}^\times$, with values differing by $2\pi k$. On a simply connected subset (e.g., the slit plane), $v = \arg z$ is well-defined.

**Solving Laplace's equation by complex analysis.** Find a harmonic function $u$ on the upper half-plane with $u(x, 0) = $ a specified function $f(x)$. Strategy: find a holomorphic $g$ on $\mathbb{H}$ with $\operatorname{Re} g(x) = f(x)$ on the boundary; then $u = \operatorname{Re} g$.

---

# Bridges

- **[[Def - Harmonic Function]]** — the object.

- **[[Thm - Cauchy–Riemann Equations]]** — the link between holomorphic and real-variable conditions.

- **[[Def - Simply Connected Domain in Complex Analysis]]** — the topological condition.

- **[[Thm - Cauchy's Theorem for Simply Connected Domains]]** — gives the existence of primitives, equivalently exactness of closed 1-forms.

---

# Unlocked by This

> [!tip] Mean Value and Maximum Principle *(from §3.6+)*
> Harmonic functions inherit [[Thm - Mean Value Property of Harmonic Functions|mean value]] and [[Thm - Maximum Principle for Harmonic Functions|maximum principle]] from the corresponding holomorphic properties.

> [!tip] Poisson Integral *(from §3.6+)*
> Real parts of holomorphic functions evaluated at boundary values via Cauchy integral give the [[Thm - Poisson Integral Formula|Poisson integral formula]].

> [!tip] De Rham Cohomology *(from Topology)*
> The harmonic conjugate problem is the first de Rham cohomology $H^1$ of the domain: $H^1(U) = 0$ ⟺ all closed 1-forms are exact ⟺ harmonic conjugates exist globally.
