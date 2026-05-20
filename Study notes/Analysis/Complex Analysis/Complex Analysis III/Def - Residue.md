---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Laurent Series"
  - "Def - Isolated Singularity"
  - "Def - Winding Number"
tags: [analysis, complex-analysis]
---

# Notation

Throughout, $a \in \mathbb{C}$ is an isolated singularity of $f$, with Laurent expansion $f(z) = \sum_{n=-\infty}^\infty c_n (z - a)^n$ on a punctured disc $D(a, R) \setminus \{a\}$. The residue of $f$ at $a$ is written $\operatorname{Res}_a f$ or $\operatorname{Res}_{z = a} f(z)$. The full registry lives on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Axiom Motivation

Of all the Laurent coefficients $c_n$ for $n \in \mathbb{Z}$, why is $c_{-1}$ singled out for a name?

The answer comes from integration. Suppose we compute $\oint f(z)\,dz$ around a small circle $|z - a| = \rho$ enclosing the singularity. Termwise (legal because the Laurent series converges uniformly on the circle), each term contributes
$$\oint (z - a)^n\,dz = \begin{cases} 2\pi i & \text{if } n = -1, \\ 0 & \text{otherwise}.\end{cases}$$
The "otherwise" case is just calculus: $(z - a)^n$ for $n \neq -1$ has an antiderivative $(z - a)^{n+1}/(n+1)$, single-valued on the punctured disc, so its closed integral is zero. The $n = -1$ case is different: $1/(z - a)$ has *no* single-valued antiderivative on the punctured disc, because $\log(z - a)$ picks up $2\pi i$ on going around the puncture. So the integral picks out exactly one Laurent coefficient: $c_{-1}$.

This is the *true name* of the residue: $\operatorname{Res}_a f$ is the obstruction to $f$ having a primitive on a punctured disc around $a$. Every other coefficient $c_n$ for $n \neq -1$ contributes a function $(z-a)^n$ whose antiderivative exists, so it does not obstruct primitive-finding. Only $c_{-1}$ obstructs, and the obstruction is measured by the closed integral $\oint f\,dz = 2\pi i c_{-1}$.

This is also what makes the residue *the unit of contour integration*. Any contour integral of a meromorphic function around a closed curve reduces — by the residue theorem — to $2\pi i$ times the sum of residues at enclosed singularities, weighted by winding numbers. The residue is the local data that, summed up with topological weights, gives the global integral. No other Laurent coefficient has this role.

What would break with a different choice? Defining $\operatorname{Res}_a f = c_{-2}$ or $c_0$ would give a quantity with no special integration-theoretic significance — the integral $\oint f\,dz$ would not be a simple multiple of it. The choice $c_{-1}$ is forced by the question "which Laurent coefficient survives contour integration?"

The fact that the residue is a *single complex number* (not a vector of coefficients, not the full Laurent expansion) is also significant. It means that, no matter how wild a function's singularity is — pole of any order, essential — the *integration-theoretic content* of the singularity is captured by a single number. This radical compression is what makes residue calculus so powerful: enormously complicated functions become tractable for integration purposes because all the relevant information about each singularity is a single number.

---

# The Definition

Let $a \in \mathbb{C}$ be an isolated singularity of $f$, with Laurent expansion $f(z) = \sum_{n=-\infty}^\infty c_n (z - a)^n$ on $D(a, R) \setminus \{a\}$. The **residue** of $f$ at $a$ is
$$\operatorname{Res}_a f := c_{-1},$$
the coefficient of $(z - a)^{-1}$ in the Laurent expansion.

**Integral formula.** For any sufficiently small $\rho > 0$,
$$\operatorname{Res}_a f = \frac{1}{2\pi i}\oint_{|z - a| = \rho} f(z)\,dz,$$
where the circle is traversed counterclockwise. By Cauchy's theorem, the integral is independent of $\rho$ (provided the circle is inside the punctured disc of holomorphicity).

---

# Categorical Definition

The residue is the **periods pairing between $H_1$ (homology of loops) and $H^1$ (cohomology of meromorphic differentials)**. The meromorphic 1-form $f(z)\,dz$ on the punctured disc represents a class in $H^1_{\mathrm{dR}}$ of the punctured disc, and the small loop around $a$ represents the generator of $H_1$ of the punctured disc. The pairing
$$\langle [\gamma], [f\,dz]\rangle = \oint_\gamma f\,dz$$
is the residue, up to the factor $2\pi i$. In categorical language, the residue is the value of a *natural functional* on the local cohomology of meromorphic differentials.

For readers unfamiliar with de Rham cohomology: this just means the residue is what survives when you integrate a meromorphic 1-form around a small loop — modding out by exact forms (those of the shape $dg$ for some $g$), only the $c_{-1}/(z - a)$ part of $f$ survives, because all other Laurent terms are derivatives of nice functions.

---

# Relate to Other Fields / Compression

The residue is the simplest example of an **algebraic period** — a number obtained as the integral of an algebraic differential over an algebraic cycle. In algebraic geometry, periods are the link between the algebraic and topological structures of a variety, and the residue is the local building block: every period is a sum of contour integrals near singularities, each contributing $2\pi i \cdot \text{residue}$.

In **partial differential equations**, the analog is the **strength of a point source** in a fundamental solution to a PDE. The fundamental solution of Laplace's equation in $\mathbb{R}^2$, namely $\log|x|/(2\pi)$, satisfies $\Delta u = \delta_0$, and the coefficient $1/(2\pi)$ is the "residue" of the singularity — the strength of the point mass at the origin. The complex-analytic residue is the analog for $1/(z - a)$, which is the holomorphic analog of $\log|z|$.

In **fluid dynamics**, the residue of the complex potential $w(z)$ at a vortex location $a$ is $-i\Gamma/(2\pi)$ where $\Gamma$ is the *circulation* — the line integral of velocity around the vortex. So the residue *is the circulation strength*, up to scaling. For sources/sinks (simple poles of $w'$, not of $w$), the residue of $w'$ gives the mass flux.

In **signal processing**, the residue of a transfer function $H(s)$ at a pole $s_k$ is the *modal amplitude* of the corresponding resonance — when the system is excited, the response amplitude at frequency $\operatorname{Im} s_k$ scales with $\operatorname{Res}_{s_k} H$. Inverse Laplace transforms reduce to sums of $\operatorname{Res}_{s_k}(H(s) e^{st})$, giving the time-domain response as a sum over modes.

---

# Examples / Corollaries

**Simple pole at zero — $1/z$.** $\operatorname{Res}_0 (1/z) = 1$ trivially. More generally, $\operatorname{Res}_a (1/(z - a)) = 1$ for any $a$.

**Higher-order pole, residue from formula — $1/(z - a)^k$.** Laurent expansion has only the $c_{-k}$ term, so $c_{-1} = 0$ for $k \geq 2$. Therefore $\operatorname{Res}_a(1/(z - a)^k) = 0$ for $k \geq 2$. This is a key warning: a higher-order pole *can* have zero residue, and the residue does not tell you whether the singularity is a pole or its order.

**Simple pole via the limit formula.** If $f$ has a simple pole at $a$, then $\operatorname{Res}_a f = \lim_{z \to a}(z - a) f(z)$. For $f(z) = e^z/(z^2 - 1)$ at $z = 1$: $\lim_{z \to 1}(z - 1) e^z/((z - 1)(z + 1)) = e/2$.

**Simple pole as a quotient — $\operatorname{Res}_a(g/h) = g(a)/h'(a)$.** When $h$ has a simple zero at $a$ ($h(a) = 0, h'(a) \neq 0$) and $g(a) \neq 0$, this formula collapses residue computation to evaluating two derivatives. For $f(z) = \cos z/\sin z = \cot z$ at $z = 0$: $\operatorname{Res}_0 \cot z = \cos 0/(\sin)'(0) = 1/\cos 0 = 1$.

**Higher-order pole via derivative formula.** For a pole of order $k$ at $a$, $\operatorname{Res}_a f = \frac{1}{(k-1)!}\lim_{z \to a}\frac{d^{k-1}}{dz^{k-1}}[(z - a)^k f(z)]$. For $f(z) = e^z/z^3$ at $z = 0$: $k = 3$, $(z - 0)^3 f(z) = e^z$, so $\operatorname{Res}_0 f = \frac{1}{2!}\lim_{z \to 0}(e^z)'' = \frac{1}{2}$.

**Essential singularity residue — $e^{1/z}$ at $z = 0$.** Laurent expansion: $\sum_{n=0}^\infty z^{-n}/n!$. The coefficient of $z^{-1}$ is $1/1! = 1$. So $\operatorname{Res}_0 e^{1/z} = 1$. Essential singularities have residues just like poles — the residue formula is the same regardless of singularity type.

**Calibration check — residue is linear.** $\operatorname{Res}_a(\alpha f + \beta g) = \alpha \operatorname{Res}_a f + \beta \operatorname{Res}_a g$. Immediate from the Laurent coefficient interpretation.

**Calibration check — residue at infinity.** Define $\operatorname{Res}_\infty f = -\operatorname{Res}_0 \frac{1}{w^2} f(1/w)$, the negative sign from the orientation of large circles. For a rational function $f$, the sum of all residues on $\hat{\mathbb{C}}$ (including the residue at $\infty$) is zero.

**Corollary — sum of residues of a rational function over $\hat{\mathbb{C}}$ is zero.** $\sum_{a \in \mathbb{C}} \operatorname{Res}_a f + \operatorname{Res}_\infty f = 0$ for any rational function $f$. This is the "global residue theorem" for the Riemann sphere: there is no boundary, so no contribution can escape.

**Corollary — residue is invariant under conformal change of coordinates.** If $\phi$ is a biholomorphism near $a$ with $\phi(a) = b$, and $\omega = f(z)\,dz$ is a meromorphic 1-form, then $\operatorname{Res}_b(\phi_* \omega) = \operatorname{Res}_a \omega$. The residue is a property of the *differential form*, not the function, and the form is the conformally invariant object.

---

# Unlocked by This

> [!tip] Residue Theorem *(from §3.3)*
> The [[Thm - Residue Theorem|residue theorem]] is the workhorse: $\oint_\gamma f\,dz = 2\pi i \sum I(\gamma; w)\operatorname{Res}_w f$, summing over enclosed singularities.

> [!tip] Computing Residues *(from §3.3)*
> The [[Thm - Computing Residues|computing-residues theorem]] gives the standard formulas for residues at simple and higher-order poles without computing the full Laurent expansion.

> [!tip] Real Integrals via Residues *(from §3.4)*
> Once you can compute residues at $\mathbb{C}$-poles of a complex extension, you can [[Thm - Real Rational Integrals via Residues|evaluate real integrals]] by contour closure. The whole calculus of definite integrals via complex analysis runs on this.

> [!tip] Inverse Laplace Transforms *(from Applications)*
> The [[Def - Laplace Transform|inverse Laplace transform]] $f(t) = \frac{1}{2\pi i}\int F(s) e^{st}\,ds$ evaluates as $\sum \operatorname{Res}_{s_k}(F(s) e^{st})$. The poles of $F$ are the modes of the time-domain function; the residues are the modal amplitudes.
