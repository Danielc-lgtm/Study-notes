---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Locally Uniform Convergence"
  - "Def - Holomorphic Function"
  - "Thm - Cauchy's Theorem for Simply Connected Domains"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is open, $f_n : U \to \mathbb{C}$ is a sequence of holomorphic functions converging locally uniformly to $f : U \to \mathbb{C}$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Motivation

This is the cornerstone fact making locally uniform convergence the "right" convergence for complex analysis: *limits preserve holomorphicity*. If a sequence $f_n$ of holomorphic functions converges locally uniformly to $f$, then $f$ is also holomorphic, and moreover all derivatives converge: $f_n^{(k)} \to f^{(k)}$ locally uniformly for every $k$.

The corresponding fact in real analysis fails dramatically. Pointwise limits of continuous functions need not be continuous (let alone differentiable). Even uniform limits of $C^\infty$ functions can fail to be $C^1$. The Bernstein polynomials approximate any continuous function uniformly, including nowhere-differentiable ones.

But for holomorphic functions, the rigidity is so strong that locally uniform convergence forces *all* the derivatives to converge. This is essentially because the derivative of a holomorphic function can be expressed as a contour integral (Cauchy's formula), and integration is robust under uniform limits.

This theorem is the foundation of *normal families* (Montel's theorem), *infinite products* of holomorphic functions, *Dirichlet series and zeta functions*, and the construction of biholomorphisms in the Riemann mapping theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

**Convergent series of holomorphic functions.** Property $B$: $\sum_{n=0}^\infty g_n(z)$ where each $g_n$ is holomorphic and the series converges locally uniformly. Bridge: partial sums $f_N = \sum_{n \leq N} g_n$ are holomorphic; locally uniform convergence to $f = \sum$ gives $f$ holomorphic. Used for power series, Laurent series, Dirichlet series.

**Cauchy sequence of holomorphic functions.** Property $B$: $f_n$ holomorphic and Cauchy in the locally uniform sense. Bridge: complete metric space structure; the Cauchy sequence converges to a limit, which is then holomorphic.

**Convergent integral of holomorphic functions in a parameter.** Property $B$: $F(z) = \int g(z, t)\,dt$ for $g(z, t)$ holomorphic in $z$, the integral converging in a suitable sense. Bridge: discretize the integral, use locally uniform convergence of Riemann sums.

**Targets (Output Amplification)**

Combine with **the Cauchy formula structure.** Property $D$: $f_n^{(k)}(z) = (k!/(2\pi i))\oint f_n(\zeta)/(\zeta - z)^{k+1}\,d\zeta$. Amplified result $E$: $f^{(k)}$ given by the same formula, with $f_n$ replaced by $f$. So convergence of derivatives is built into the theorem.

Combine with **Hurwitz's theorem.** Property $D$: $f_n$ nonvanishing. Amplified result $E$: $f$ is either identically zero or nonvanishing ([[Thm - Hurwitz's Theorem|Hurwitz]]).

Combine with **Montel's theorem.** Property $D$: a family of holomorphic functions, locally uniformly bounded. Amplified result $E$: the family is *normal* — every sequence has a locally uniformly convergent subsequence, with holomorphic limit. Foundation of the Riemann mapping theorem.

---

# Why Is It True

The key idea is **Morera's theorem**: a continuous function $f$ on $U$ with $\oint_\Delta f\,dz = 0$ for every triangle $\Delta \subset U$ is holomorphic. So to show $f$ is holomorphic, show its triangle integrals all vanish.

For each holomorphic $f_n$, Cauchy's theorem gives $\oint_\Delta f_n\,dz = 0$. Each triangle $\Delta$ is compact, so $f_n \to f$ uniformly on $\Delta$. Uniform convergence on a compact set commutes with integration: $\oint_\Delta f\,dz = \lim_n \oint_\Delta f_n\,dz = 0$. By Morera, $f$ is holomorphic.

For derivatives: by the Cauchy integral formula, $f_n^{(k)}(z) = (k!/(2\pi i))\oint_C f_n(\zeta)/(\zeta - z)^{k+1}\,d\zeta$ for a small circle $C$ around $z$ inside $U$. Uniform convergence of $f_n \to f$ on $C$ gives uniform convergence of the integrands, hence convergence of $f_n^{(k)}(z) \to (k!/(2\pi i))\oint_C f(\zeta)/(\zeta - z)^{k+1}\,d\zeta = f^{(k)}(z)$. The convergence is uniform on compact subsets of the interior of $C$, hence locally uniform.

The conceptual point: *holomorphic functions are determined by their boundary values via Cauchy*. So convergence on a boundary curve (uniform on a compact set) determines convergence of the function and all its derivatives in the interior. Real-variable functions have no such "boundary-to-interior" rigidity.

---

# What Makes This Hard

The non-obvious step is **using Morera's theorem to prove holomorphicity of the limit**. Most people instinctively try to verify the Cauchy-Riemann equations or differentiate term-by-term, but these approaches are clunky. Morera converts the problem to "triangle integrals are zero", which interchanges cleanly with locally uniform convergence (uniform on the compact triangle).

Common confusion: Morera's theorem is *Cauchy's theorem in reverse* — Cauchy says holomorphic ⟹ triangle integrals zero; Morera says continuous + triangle integrals zero ⟹ holomorphic. The two together characterize holomorphicity by an integral condition.

---

# Rederivation Scaffold

**High-level strategy:**
Use Morera's theorem. The locally uniform convergence on each triangle (compact) gives $\oint_\Delta f\,dz = \lim_n \oint_\Delta f_n\,dz = 0$. Hence $f$ is holomorphic. Derivatives convergence by the Cauchy integral formula applied to compact subsets.

**Subgoal decomposition:**

1. **$f$ is continuous.** Locally uniform convergence of continuous functions gives a continuous limit.

2. **$\oint_\Delta f\,dz = 0$ for every triangle $\Delta \subset U$.** Use $\oint_\Delta f_n\,dz = 0$ (Cauchy) and uniform convergence on $\Delta$ to pass the limit.

3. **By Morera, $f$ is holomorphic.**

4. **Derivative convergence.** Use the Cauchy integral formula $f_n^{(k)}(z) = (k!/(2\pi i))\oint f_n(\zeta)/(\zeta - z)^{k+1}\,d\zeta$ on a circle $C$, and uniform convergence on $C$ to conclude $f_n^{(k)}(z) \to f^{(k)}(z)$, uniformly on compact subsets of the interior.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f_n : U \to \mathbb{C}$ be holomorphic with $f_n \to f$ locally uniformly on $U$.
>
> **Step 1: $f$ is continuous.** Locally uniform convergence implies uniform convergence on every compact $K \subset U$. Since each $f_n$ is continuous (in fact, holomorphic ⟹ continuous), and uniform limits of continuous functions are continuous, $f$ is continuous on every compact subset of $U$, hence continuous on $U$.
>
> **Step 2: $f$ is holomorphic via Morera.** Let $\Delta$ be any closed triangle inside $U$. For each $n$, $\oint_{\partial\Delta} f_n\,dz = 0$ by Cauchy's theorem on the triangle. Since $\Delta$ is compact and $f_n \to f$ uniformly on $\Delta$:
> $$\oint_{\partial\Delta} f\,dz = \oint_{\partial\Delta} \lim_n f_n\,dz = \lim_n \oint_{\partial\Delta} f_n\,dz = 0.$$
> (The first equality uses uniform convergence on the compact $\partial\Delta$; the second uses linearity.)
>
> Since $f$ is continuous on $U$ and $\oint_{\partial\Delta} f\,dz = 0$ for every triangle in $U$, by Morera's theorem $f$ is holomorphic on $U$.
>
> **Step 3: Higher derivatives converge.** Take any $z \in U$ and choose $r > 0$ such that $\overline{D(z, 2r)} \subset U$. Let $C = \{|z - \zeta| = r\}$. By Cauchy's integral formula:
> $$f_n^{(k)}(\zeta) = \frac{k!}{2\pi i}\oint_C \frac{f_n(w)}{(w - \zeta)^{k+1}}\,dw, \quad \zeta \in D(z, r/2).$$
> On $\{(\zeta, w) : |z - \zeta| \leq r/2, |z - w| = r\}$, $|w - \zeta| \geq r/2$, so $1/|w - \zeta|^{k+1} \leq 2^{k+1}/r^{k+1}$. Uniform convergence $f_n \to f$ on $C$ gives uniform convergence of the integrand, hence
> $$f_n^{(k)}(\zeta) \to \frac{k!}{2\pi i}\oint_C \frac{f(w)}{(w - \zeta)^{k+1}}\,dw = f^{(k)}(\zeta),$$
> uniformly for $\zeta \in D(z, r/2)$. Since $z$ was arbitrary, $f_n^{(k)} \to f^{(k)}$ locally uniformly. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Power series convergence.** A power series $\sum a_n z^n$ with radius of convergence $R$ converges locally uniformly on $|z| < R$. The limit is therefore holomorphic on the open disc $|z| < R$, and termwise differentiation is licensed: $(\sum a_n z^n)' = \sum n a_n z^{n-1}$ on the same disc.

**Riemann zeta function.** The series $\zeta(s) = \sum_{n=1}^\infty 1/n^s$ converges locally uniformly on the half-plane $\{\operatorname{Re} s > 1\}$ (by comparison to $\sum 1/n^{1 + \epsilon}$). The limit is therefore holomorphic on $\{\operatorname{Re} s > 1\}$. Analytic continuation extends $\zeta$ meromorphically to $\mathbb{C}$ (with a simple pole at $s = 1$), but the basic holomorphy on $\{\operatorname{Re} s > 1\}$ is established by this theorem.

**Limits of polynomial approximations.** Runge's theorem: every holomorphic function on a domain $U$ can be approximated locally uniformly by rational functions. The limit is holomorphic — but conversely, the limit of any locally uniformly convergent sequence of rationals is holomorphic on the domain of convergence.

**Stieltjes transforms.** The Stieltjes transform $F(z) = \int d\mu(t)/(z - t)$ of a positive measure $\mu$ is holomorphic on $\mathbb{C}\setminus\text{supp}(\mu)$. Viewed as a limit of Riemann sums, it inherits holomorphicity from the holomorphic Riemann-sum approximations.

---

# Bridges

- **[[Def - Locally Uniform Convergence]]** — the convergence notion.

- **Morera's Theorem** (from [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]) — used to prove holomorphicity.

- **[[Thm - Cauchy's Theorem for Simply Connected Domains]]** — used to get triangle integrals zero.

- **[[Thm - Hurwitz's Theorem]]** — direct consequence.

---

# Unlocked by This

> [!tip] Hurwitz's Theorem *(from §3.6)*
> [[Thm - Hurwitz's Theorem|Hurwitz]]: locally uniform limit of nonvanishing is identically zero or nonvanishing.

> [!tip] Montel's Theorem *(from Mapping Theory)*
> A *normal family* is one where every sequence has a locally uniformly convergent subsequence. The limit is holomorphic by this theorem.

> [!tip] Riemann Mapping Theorem *(from §3.5+)*
> Proof uses normal families to extract a convergent subsequence; the limit is then a holomorphic candidate biholomorphism.
