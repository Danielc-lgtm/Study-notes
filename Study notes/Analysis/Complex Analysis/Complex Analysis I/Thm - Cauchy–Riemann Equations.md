---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ open; $f : U \to \mathbb{C}$; $w = c + id \in U$. We write $f = u + iv$ with $u, v : U \to \mathbb{R}$ real-valued (viewing $U \subseteq \mathbb{R}^2$ via $(x, y) \leftrightarrow x + iy$). Partial derivatives: $u_x = \partial u/\partial x$, etc. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Motivation

[[Def - Holomorphic Function|Complex differentiability]] is defined via a limit that is *direction-independent*: $(f(z) - f(w))/(z - w)$ must have the same limit as $z \to w$ from every direction in $\mathbb{C}$. This is two real-valued conditions on top of the real differentiability of the pair $(u, v)$ — and the question is, *which* two? The Cauchy–Riemann theorem identifies them: they are $u_x = v_y$ and $u_y = -v_x$. These are the *operational form* of complex differentiability, and every concrete check of holomorphicity goes through them.

The theorem also gives the formula $f'(w) = u_x + i v_x$. This is the *complex* derivative reconstructed from real partials, which is what makes the theorem usable computationally.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ is complex differentiable at $w$" *or* — for the converse — "$u, v$ are real-differentiable at $w$ and satisfy CR". Recognizing the latter is the practical skill.

The first disguised source is **$u, v \in C^1$ on $U$ with CR holding**: continuously differentiable partials are *more* than enough for real differentiability, by a standard real analysis result. So this is the most common cleanest sufficient condition, and the theorem's converse direction applies. *Example:* check $f(z) = e^z$ is holomorphic by computing $u = e^x \cos y, v = e^x \sin y$, both $C^\infty$, and verifying CR.

The second disguised source is **$f$ given by a formula in $z$ alone, no $\bar z$**: such a formula is automatically holomorphic by composition of holomorphic functions. The CR equations are satisfied automatically because $\partial f/\partial \bar z = 0$ in the Wirtinger sense. *Example:* $f(z) = z^3 + z \cos z + e^{z^2}$ — no $\bar z$, so holomorphic. No need to compute real and imaginary parts.

The third disguised source is **a $C^1$ map $f : \mathbb{R}^2 \to \mathbb{R}^2$ whose Jacobian is a rotation-scaling matrix** $\begin{pmatrix} a & -b \\ b & a\end{pmatrix}$. This is exactly the matrix form of the CR equations, and *equivalent* to complex differentiability with derivative $a + ib$. *Example:* the linear map $(x, y) \mapsto (ax - by, bx + ay)$ is holomorphic ($= (a + ib) z$).

**Targets (Output Amplification)**

The conclusion is "$f$ is complex differentiable at $w$" with the derivative formula.

Combine the conclusion with **harmonicity of partials**. Property $D$: $u, v$ have continuous second partials. Then differentiating CR once more gives $\Delta u = \Delta v = 0$ (see [[Thm - Real and Imaginary Parts of a Holomorphic Function are Harmonic]]). So the *combination* "$f$ holomorphic + $C^2$" yields $u, v$ harmonic. The nonobviousness is that *every* holomorphic function has harmonic real and imaginary parts.

Combine the conclusion with **a global constraint on $f'$.** Property $D$: $f'(w) = 0$ for every $w$ in a [[Def - Domain in the Complex Plane|domain]] $D$. Then $f$ is constant (see [[Thm - Constant on a Domain if Derivative is Zero]]). The combination is "$f$ holomorphic on $D$ + derivative identically zero $\Rightarrow$ $f$ constant".

Combine the conclusion with **conformality of $Df$ as a real-linear map**. Property $D$: the linear part of $f$ at $w$ has the form $a + ib$ acting on $\mathbb{C}$. The amplified result: $f$ preserves angles at $w$ (since multiplication by $a + ib = re^{i\theta}$ is rotation by $\theta$ followed by scaling by $r$). This is the **conformal map** interpretation of holomorphic functions.

---

# Why Is It True

The complex derivative $f'(w) = p + iq$ encodes how $f$ infinitesimally maps the *complex* plane near $w$. As a real-linear map $\mathbb{R}^2 \to \mathbb{R}^2$, multiplication by $p + iq$ has the matrix $\begin{pmatrix} p & -q \\ q & p\end{pmatrix}$ — a rotation-scaling. The CR equations are exactly the statement that the Jacobian matrix of $f = (u, v) : \mathbb{R}^2 \to \mathbb{R}^2$ has this special form.

Concretely: the Jacobian of $(u, v)$ is $\begin{pmatrix} u_x & u_y \\ v_x & v_y\end{pmatrix}$. For this to be a rotation-scaling matrix, we need $u_x = v_y$ (the diagonal entries equal) and $u_y = -v_x$ (the off-diagonal entries opposite). These are the CR equations.

So complex differentiability is the *extra structure* on top of real differentiability: real differentiability says the function is approximated by *some* linear map; complex differentiability says it is approximated by a *complex-linear* map, equivalently a rotation-scaling. CR equations are the linear-algebra condition on the matrix.

The forward direction is direct: if $f'(w) = p + iq$ exists, then approaching $w$ along the real axis ($z = w + h$, $h \in \mathbb{R}$) gives $f'(w) = u_x + i v_x$ at $w$; approaching along the imaginary axis ($z = w + ih$) gives $f'(w) = v_y - i u_y$. Equating real and imaginary parts: $p = u_x = v_y$ and $q = v_x = -u_y$. The two axial directions alone determine the CR equations.

The reverse direction is more subtle: from CR plus real differentiability of $u, v$, we must construct a complex derivative. Real differentiability gives $u(x, y) = u(c, d) + u_x(c,d)(x - c) + u_y(c,d)(y - d) + o(\sqrt{(x-c)^2 + (y-d)^2})$ and similarly for $v$. Combine: $f(z) = f(w) + (u_x + iv_x)(x - c) + (u_y + iv_y)(y - d) + o(|z - w|)$. Using CR to replace $u_y$ and $v_y$ by $-v_x$ and $u_x$: the linear part becomes $(u_x + iv_x)((x - c) + i(y - d)) = (u_x + iv_x)(z - w)$. So $f(z) = f(w) + (u_x + iv_x)(z - w) + o(|z - w|)$, which is exactly complex differentiability with $f'(w) = u_x + iv_x$.

---

# What Makes This Hard

The non-obvious step is in the *converse* direction: from CR equations + real differentiability, one must algebraically combine the linear terms in $(x - c)$ and $(y - d)$ to assemble the complex linear term in $(z - w)$. The trick is to use CR equations to *rewrite* $u_y$ as $-v_x$ and $v_y$ as $u_x$, so that the linear part factors as $(u_x + iv_x)(z - w)$. The most common error is to assume that having all partial derivatives exist (without continuity, hence without real differentiability) is enough — the [[Ex - A function with all partials but not differentiable|Looman–Menchoff counterexample]] shows this can fail.

---

# Rederivation Scaffold

**High-level strategy:**
The forward direction tests $f'(w)$ along the real and imaginary axes, picking off $u_x, v_x, u_y, v_y$ and equating. The reverse uses real differentiability to write $f(z) - f(w)$ as a linear combination of $(x - c)$ and $(y - d)$ plus an $o$-term, then uses CR to factor the linear part as a complex multiple of $(z - w)$.

**Subgoal decomposition:**

1. **Forward: extract $f'(w)$ from the real-axis direction.** Approach via $z = w + h$, $h \in \mathbb{R}$.
   - *Hint:* $(f(w + h) - f(w))/h \to f'(w)$; the real and imaginary parts give $u_x + iv_x$.
   - *Why needed:* identifies two of the four partials.

2. **Forward: extract $f'(w)$ from the imaginary-axis direction.** Approach via $z = w + ih$.
   - *Hint:* $(f(w + ih) - f(w))/(ih) \to f'(w)$; gives $-iu_y + v_y = v_y - iu_y$.
   - *Why needed:* identifies the other two partials; equating with the previous gives CR.

3. **Reverse: write the real-differentiable expansion of $f(z) - f(w)$.**
   - *Hint:* $f(z) - f(w) = (u_x + iv_x)(x - c) + (u_y + iv_y)(y - d) + o(|z - w|)$.
   - *Why needed:* the basic real-differentiability decomposition.

4. **Reverse: use CR to factor as a complex multiple of $(z - w)$.**
   - *Hint:* substitute $u_y = -v_x, v_y = u_x$; the linear part becomes $(u_x + iv_x)(z - w)$.
   - *Why needed:* this is exactly complex differentiability with derivative $u_x + iv_x$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Forward direction
> **Statement:** If $f = u + iv$ is complex differentiable at $w = c + id$ with $f'(w) = p + iq$, then $u, v$ are real differentiable at $(c, d)$ with $u_x(c,d) = p = v_y(c,d)$ and $v_x(c,d) = q = -u_y(c,d)$.
>
> **Hint:** Approach $w$ along the real and imaginary axes separately; equate real and imaginary parts.
>
> **Why needed:** Establishes CR as a *necessary* condition for complex differentiability.
>
> > [!note]- Full proof
> > By definition $(f(z) - f(w))/(z - w) \to p + iq$ as $z \to w$. Take $z = w + h$ for $h \in \mathbb{R}, h \to 0$:
> > $$\frac{f(w + h) - f(w)}{h} = \frac{u(c + h, d) - u(c, d)}{h} + i\frac{v(c + h, d) - v(c, d)}{h} \to u_x(c, d) + i v_x(c, d).$$
> > So $p = u_x, q = v_x$. Take $z = w + ih$:
> > $$\frac{f(w + ih) - f(w)}{ih} = \frac{1}{i}\left[\frac{u(c, d + h) - u(c, d)}{h} + i\frac{v(c, d + h) - v(c, d)}{h}\right] \to -iu_y + v_y = v_y - iu_y.$$
> > So $p = v_y, q = -u_y$. Combining: $u_x = v_y$ and $u_y = -v_x$. Real differentiability of $u, v$ follows from the algebra of the differentiable expansion.

> [!note]- Lemma 2: Reverse direction
> **Statement:** If $u, v : U \to \mathbb{R}$ are real differentiable at $(c, d) \in U$ and satisfy $u_x(c, d) = v_y(c, d), u_y(c, d) = -v_x(c, d)$, then $f = u + iv$ is complex differentiable at $w = c + id$ with $f'(w) = u_x(c, d) + iv_x(c, d)$.
>
> **Hint:** Write the real-differentiable expansions of $u, v$; use CR to factor.
>
> **Why needed:** This is the substance of the theorem — the converse.
>
> > [!note]- Full proof
> > Real differentiability of $u$ at $(c, d)$ means $u(x, y) = u(c, d) + u_x(c-c) + u_y(y - d) + \varepsilon_1(x, y)$ where $\varepsilon_1/|z - w| \to 0$ as $z \to w$ (partial derivatives evaluated at $(c, d)$). Similarly for $v$ with error $\varepsilon_2$. So
> > $$f(z) - f(w) = (u_x + iv_x)(x - c) + (u_y + iv_y)(y - d) + (\varepsilon_1 + i\varepsilon_2).$$
> > By CR, $u_y = -v_x$ and $v_y = u_x$, so $u_y + iv_y = -v_x + iu_x = i(u_x + iv_x)$. Therefore
> > $$f(z) - f(w) = (u_x + iv_x)[(x - c) + i(y - d)] + (\varepsilon_1 + i\varepsilon_2) = (u_x + iv_x)(z - w) + o(|z - w|).$$
> > Dividing by $z - w$ and letting $z \to w$ gives $f'(w) = u_x + iv_x$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Combine Lemma 1 and Lemma 2.
>
> **($\Rightarrow$).** If $f$ is complex differentiable at $w$ with $f'(w) = p + iq$, then by approaching along the real axis ($z = w + h$, $h \to 0$ in $\mathbb{R}$):
> $$f'(w) = \lim_{h \to 0}\frac{u(c+h, d) - u(c, d) + i(v(c+h, d) - v(c, d))}{h} = u_x(c, d) + iv_x(c, d).$$
> Approaching along the imaginary axis ($z = w + ih$):
> $$f'(w) = \lim_{h \to 0}\frac{u(c, d+h) - u(c, d) + i(v(c, d+h) - v(c, d))}{ih} = \frac{1}{i}(u_y + iv_y) = v_y - iu_y.$$
> Equating real and imaginary parts: $u_x = v_y$ and $v_x = -u_y$. Also, real differentiability of $u, v$ follows from differentiability of $f$ as a map $\mathbb{R}^2 \to \mathbb{R}^2$ (which is a direct consequence of complex differentiability — the limit being one-dimensional in $\mathbb{C}$ but covering all approach directions).
>
> **($\Leftarrow$).** Assume $u, v$ real differentiable at $(c, d)$ and CR holds. By real differentiability,
> $$u(x, y) - u(c, d) = u_x(c, d)(x - c) + u_y(c, d)(y - d) + o(|(x, y) - (c, d)|),$$
> $$v(x, y) - v(c, d) = v_x(c, d)(x - c) + v_y(c, d)(y - d) + o(|(x, y) - (c, d)|).$$
> So
> $$f(z) - f(w) = (u_x + iv_x)(x - c) + (u_y + iv_y)(y - d) + o(|z - w|).$$
> By CR, $u_y = -v_x$ and $v_y = u_x$, so $u_y + iv_y = -v_x + iu_x = i(u_x + iv_x)$. Substituting:
> $$f(z) - f(w) = (u_x + iv_x)[(x - c) + i(y - d)] + o(|z - w|) = (u_x + iv_x)(z - w) + o(|z - w|).$$
> Dividing by $z - w$:
> $$\frac{f(z) - f(w)}{z - w} = (u_x + iv_x) + \frac{o(|z - w|)}{z - w}.$$
> The last term goes to $0$ as $z \to w$ (since $|o(|z-w|)/(z-w)| = o(1)$). Hence $f'(w) = u_x(c, d) + iv_x(c, d)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Conformal maps in fluid dynamics.** A holomorphic function $f : U \to \mathbb{C}$ with $f' \neq 0$ acts as a *conformal map* — preserves angles. In 2D incompressible inviscid flow, velocity fields satisfy CR equations (with the velocity potential and stream function as $u, v$). The CR equations *are* the equations of 2D potential flow.

**Cauchy–Riemann as an elliptic system.** The CR system $u_x - v_y = 0, u_y + v_x = 0$ is the canonical example of a *first-order elliptic system* in PDE theory. Solutions are automatically $C^\infty$ by elliptic regularity — which from the complex-analysis side is the "holomorphic implies $C^\infty$" theorem. The CR system is the prototype for the regularity theory of elliptic equations.

**Wirtinger derivatives and the $\bar\partial$ operator.** Define $\partial/\partial z = \tfrac12(\partial_x - i\partial_y), \partial/\partial \bar z = \tfrac12(\partial_x + i\partial_y)$. The CR equation is $\partial f/\partial \bar z = 0$ — a *single* complex equation. The operator $\bar\partial = \partial/\partial \bar z$ is the fundamental object of several complex variables and the $\bar\partial$-cohomology theory of complex manifolds.

---

# Bridges

- **[[Thm - Real and Imaginary Parts of a Holomorphic Function are Harmonic]]** — differentiating CR once more gives the harmonicity of $u, v$. CR is the *first-order* avatar; harmonicity is the *second-order* consequence.

- **[[Thm - Constant on a Domain if Derivative is Zero]]** — uses CR to convert complex-derivative zero into the four real-partial-derivative-zero condition, then path-connectedness of the domain.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — the full structural result that holomorphic $\Leftrightarrow$ analytic; CR is its local linearization.

---

# Unlocked by This

> [!tip] Harmonic Functions *(from Analysis/PDE)*
> The real and imaginary parts of holomorphic functions are exactly the **conjugate harmonic pairs**. Two-dimensional harmonic analysis is the real-variable shadow of complex analysis, and CR is the bridge.

> [!tip] Conformal Maps *(from CA IV)*
> Holomorphic functions with nonzero derivative are exactly the orientation-preserving conformal maps of planar domains. CR is the local condition for conformality.

> [!tip] $\bar\partial$-Cohomology *(from Several Complex Variables)*
> The Cauchy–Riemann operator $\bar\partial = \partial/\partial \bar z$ extends to complex manifolds, and its cohomology measures the obstruction to solving $\bar\partial u = f$. This is the entry point to **Hodge theory** on Kähler manifolds.
