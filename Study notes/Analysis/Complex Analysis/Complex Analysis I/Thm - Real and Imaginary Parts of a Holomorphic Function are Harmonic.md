---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Thm - Cauchy–Riemann Equations"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ open; $f = u + iv : U \to \mathbb{C}$ holomorphic with $u, v$ real and $C^2$ on $U$. The **Laplacian** is $\Delta u = u_{xx} + u_{yy}$. A function is **harmonic** if $\Delta u = 0$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Motivation

The Cauchy–Riemann equations $u_x = v_y, u_y = -v_x$ are first-order PDEs linking $u$ and $v$. Differentiating once more (legitimate because $f$ holomorphic implies $u, v$ are $C^\infty$, by the regularity theorem of [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]) gives a *second-order* consequence: both $u$ and $v$ separately satisfy Laplace's equation $\Delta u = 0$. This is the bridge between complex analysis and the classical theory of **harmonic functions** in two variables — and through it, to potential theory, electrostatics, fluid dynamics, and the maximum principle.

This is one of the strongest constraints in complex analysis. Holomorphic functions are not arbitrary — their real and imaginary parts must each satisfy the Laplace equation, which is itself a strong restriction (harmonic functions have the mean value property, maximum principle, etc.). The class of holomorphic functions is pegged to the class of *conjugate harmonic pairs*: pairs $(u, v)$ of harmonic functions linked by CR.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f = u + iv$ holomorphic on $U$".

The first disguised source is **$f$ is an analytic function on a complex domain**: by the equivalence "holomorphic = analytic" (proved in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]), every analytic function inherits the harmonicity of its real and imaginary parts. *Example:* $f(z) = \sin z$ is entire; its real part $u(x, y) = \sin x \cosh y$ and imaginary part $v(x, y) = \cos x \sinh y$ are both harmonic on $\mathbb{R}^2$ — directly verifiable.

The second disguised source is **$f$ is a power series with positive radius of convergence**: such an $f$ is holomorphic on its disc of convergence (by [[Thm - Power Series is Holomorphic with Termwise Derivative]]), hence its real and imaginary parts are harmonic on the disc.

**Targets (Output Amplification)**

The conclusion is "$u, v$ are harmonic, i.e., $\Delta u = \Delta v = 0$".

Combine with **the maximum principle for harmonic functions.** Property $D$: $u$ continuous on $\overline U$ for $U$ bounded. The amplified result: $u$ attains its maximum on $\partial U$. This recovers the [[Thm - (Global) Maximum Modulus Principle|maximum modulus principle]] for $|f|$ (which is $\sqrt{u^2 + v^2}$, harmonic-like) and propagates.

Combine with **the Poisson integral formula.** Property $D$: $u$ continuous on a closed disc, harmonic in the interior. The amplified result: $u$ is recovered from its boundary values via $u(0) = \frac{1}{2\pi}\int_0^{2\pi} u(re^{i\theta})\,d\theta$ — the mean value property. The complex-analytic analog is the [[Thm - Cauchy Integral Formula|Cauchy integral formula]].

Combine with **Liouville for harmonic functions.** Property $D$: $u$ bounded on $\mathbb{R}^2$ and harmonic. The amplified result: $u$ is constant. Proof: let $v$ be a harmonic conjugate (exists globally on simply connected $\mathbb{R}^2$); then $f = u + iv$ is entire with $|e^f| = e^u$ bounded; by [[Thm - Liouville's Theorem|Liouville]], $e^f$ is constant, hence $f$ is constant. See [[Ex - Liouville for harmonic functions]].

---

# Why Is It True

The proof is one line once the regularity is established: $\Delta u = u_{xx} + u_{yy}$. Differentiating $u_x = v_y$ with respect to $x$: $u_{xx} = v_{yx}$. Differentiating $u_y = -v_x$ with respect to $y$: $u_{yy} = -v_{xy}$. By Schwarz's theorem (mixed partials commute since $v \in C^2$), $v_{yx} = v_{xy}$, so $u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0$.

Same for $v$: differentiate $v_y = u_x$ in $y$ giving $v_{yy} = u_{xy}$; differentiate $v_x = -u_y$ in $x$ giving $v_{xx} = -u_{yx}$. Mixed partials cancel: $v_{xx} + v_{yy} = 0$.

The deeper conceptual reason: complex differentiability is a *first-order* linear condition (the CR equations form a $2 \times 2$ first-order PDE system); differentiating any first-order linear PDE system gives second-order equations on the components, and for the *CR system specifically*, this second-order consequence is the Laplace equation. The CR system is the *first-order elliptic system* whose individual-component consequence is Laplace.

---

# What Makes This Hard

The non-obvious prerequisite is *$C^2$ regularity* of $u, v$ — without it, the second partial derivatives may not exist, and the theorem cannot even be stated. This is *not* automatic from "$f$ complex differentiable", but it *is* automatic from "$f$ holomorphic" (which gives differentiability on a *disc*) via the deep result that holomorphic functions are infinitely differentiable. The common error is to assume $C^2$ without justification when $f$ is only known to be complex differentiable at isolated points.

---

# Rederivation Scaffold

**High-level strategy:**
Establish $u, v \in C^2$ (from holomorphicity via the regularity theorem, or by hypothesis). Differentiate the CR equations once more. Use the symmetry of mixed partials to cancel the cross-terms.

**Subgoal decomposition:**

1. **Establish $u, v \in C^2$.** From holomorphicity and the analyticity equivalence.
   - *Hint:* $f$ holomorphic implies $f \in C^\infty$ on $U$ (by analyticity), so $u, v \in C^\infty$.
   - *Why needed:* legitimizes taking second partials and using Schwarz.

2. **Differentiate $u_x = v_y$ in $x$ and $u_y = -v_x$ in $y$.**
   - *Hint:* gives $u_{xx} = v_{yx}, u_{yy} = -v_{xy}$.
   - *Why needed:* assembles the second-order consequences of CR.

3. **Apply Schwarz (mixed partials commute) and sum.**
   - *Hint:* $v_{yx} = v_{xy}$ since $v \in C^2$.
   - *Why needed:* delivers the Laplacian as a difference of equal terms.

---

# Lemma Decomposition

> [!note]- Lemma 1: $C^2$ regularity from holomorphicity
> **Statement:** If $f$ is holomorphic on $U$, then $u = \operatorname{Re} f$ and $v = \operatorname{Im} f$ are $C^\infty$ on $U$.
>
> **Hint:** Use the analyticity theorem ([[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]): $f$ has local power series, which is $C^\infty$.
>
> **Why needed:** Without this, second partial derivatives need not exist.
>
> > [!note]- Full proof
> > By [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]] (proved in CA II), $f$ is analytic: for each $w \in U$ there is a disc $D(w, r) \subseteq U$ on which $f(z) = \sum c_n (z - w)^n$ converges. This power series is $C^\infty$ in $(x, y)$ (each $z^n = (x + iy)^n$ is a polynomial in $x, y$). So $f \in C^\infty(U)$, and the real/imaginary parts $u, v$ are $C^\infty(U)$.

> [!note]- Lemma 2: Laplace equation for $u$ from CR
> **Statement:** Assume $u, v \in C^2(U)$ and satisfy CR. Then $\Delta u = 0$ on $U$.
>
> **Hint:** Differentiate CR once more; use symmetry of mixed partials.
>
> **Why needed:** This is the substance of the theorem.
>
> > [!note]- Full proof
> > Differentiate $u_x = v_y$ with respect to $x$: $u_{xx} = v_{yx}$. Differentiate $u_y = -v_x$ with respect to $y$: $u_{yy} = -v_{xy}$. Since $v \in C^2$, by Schwarz's theorem $v_{yx} = v_{xy}$. So $u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0$, i.e., $\Delta u = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $u, v \in C^\infty(U)$. By Lemma 2 (applied to $u$ and analogously to $v$, with the roles of CR equations rearranged):
>
> Differentiating $u_x = v_y$ in $x$: $u_{xx} = v_{yx}$.
> Differentiating $u_y = -v_x$ in $y$: $u_{yy} = -v_{xy}$.
> By Schwarz, $v_{yx} = v_{xy}$. So $u_{xx} + u_{yy} = 0$, i.e., $\Delta u = 0$.
>
> Differentiating $v_y = u_x$ in $y$: $v_{yy} = u_{xy}$.
> Differentiating $v_x = -u_y$ in $x$: $v_{xx} = -u_{yx}$.
> By Schwarz, $u_{xy} = u_{yx}$. So $v_{xx} + v_{yy} = -u_{yx} + u_{xy} = 0$, i.e., $\Delta v = 0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Harmonic conjugate construction.** Given a harmonic $u$ on a simply connected domain, find a harmonic $v$ such that $f = u + iv$ is holomorphic. Explicit: integrate $v$ via $dv = -u_y\,dx + u_x\,dy$, which is exact (closed by CR-derived consistency) on simply connected domains.

**Stream function in fluid dynamics.** A 2D incompressible inviscid potential flow has a velocity potential $\phi$ (harmonic) and a stream function $\psi$ (also harmonic), related by CR equations (with sign conventions). The complex velocity $w = \phi + i\psi$ is holomorphic, and the entire theory of complex potentials is built on this.

**Electrostatics in 2D.** The electric potential of a 2D charge distribution is harmonic. The "complex potential" $\phi + i\psi$ is holomorphic where there is no charge, and contour integration evaluates physical quantities like flux.

---

# Bridges

- **[[Thm - Cauchy–Riemann Equations]]** — the first-order parent. Differentiating CR gives the Laplace equation.

- **[[Thm - Cauchy Integral Formula]]** — the complex-analytic version of the Poisson integral formula for harmonic functions; both express the reproduction of $f$ (or $u$) from its boundary values.

- **[[Thm - (Global) Maximum Modulus Principle]]** — harmonic functions satisfy the maximum principle, and the modulus principle for holomorphic $f$ derives from it (since $\log|f|$ is harmonic away from zeros of $f$).

---

# Unlocked by This

> [!tip] Potential Theory *(from PDE)*
> The maximum principle, mean value property, Harnack inequality, and Liouville's theorem for harmonic functions are all *real-variable* consequences of the equivalence with conjugate harmonic pairs. **Potential theory** is the field unifying these and their generalizations to higher dimensions.

> [!tip] Conformal Invariance *(from PDE/Physics)*
> The Laplace equation in 2D is conformally invariant: precomposing $u$ with a holomorphic change of variables preserves harmonicity. This is the basis of conformal field theory in 2D physics.

> [!tip] Hodge Theory *(from Complex Geometry)*
> On compact Kähler manifolds, the **Hodge decomposition** generalizes the conjugate-harmonic-pair structure: harmonic differential forms decompose by holomorphic type.
