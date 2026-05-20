---
type: topic
subject: complex-analysis
chapter: "1"
title: "Complex Analysis I — Basic Notions, Cauchy–Riemann, Power Series, exp/log"
tags: [analysis, complex-analysis]
---

# Notation Registry

- $z = x + iy$ — a complex number; $x = \operatorname{Re} z$, $y = \operatorname{Im} z$
- $\bar z = x - iy$ — complex conjugate; $|z| = \sqrt{x^2 + y^2}$ — modulus; $\arg z \in (-\pi, \pi]$ — principal argument
- $D(a, r) = \{z : |z - a| < r\}$ — open disc of radius $r$ centred at $a$
- $\overline{D(a, r)} = \{z : |z - a| \leq r\}$ — closed disc
- $D = D(0, 1)$ — the unit open disc
- $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$ — the punctured plane
- A **domain** $D \subseteq \mathbb{C}$ is a nonempty path-connected open set
- $U, V, W$ — open subsets of $\mathbb{C}$
- $f : U \to \mathbb{C}$ — a function of a complex variable; $f(z) = u(x, y) + i\,v(x, y)$ with $u, v$ real-valued
- $f'(w)$ — complex derivative at $w$
- **Holomorphic on $U$**: $f$ is (complex) differentiable at every point of $U$
- **Entire**: holomorphic on all of $\mathbb{C}$
- $\frac{\partial}{\partial z} = \tfrac12\left(\frac{\partial}{\partial x} - i\frac{\partial}{\partial y}\right)$ and $\frac{\partial}{\partial \bar z} = \tfrac12\left(\frac{\partial}{\partial x} + i\frac{\partial}{\partial y}\right)$ — Wirtinger derivatives
- $u_x = \partial u/\partial x$, etc.
- $\sum c_n (z - a)^n$ — power series with centre $a$; **radius of convergence** $R \in [0, \infty]$
- $\exp(z), \log z, z^\alpha$ — complex exponential, logarithm (branch-dependent), power
- $\gamma : [a, b] \to \mathbb{C}$ — a curve; $\gamma'(t)$ — derivative (real-variable)
- $C^1$ — continuously differentiable

---

# Motivation

Complex analysis is, at its heart, the study of one stupendous fact: that the *simple* assumption of having a *complex* derivative — a derivative defined exactly as in real analysis but in the complex plane — is *enormously* stronger than the apparently parallel condition in real variables. A function $f : \mathbb{R} \to \mathbb{R}$ that is differentiable once might be differentiable nowhere else. A function $f : \mathbb{C} \to \mathbb{C}$ that is differentiable once on an open set is *automatically* differentiable infinitely many times, equal to its Taylor series on every disc, determined by its values on any tiny arc, and rigid in ways that no real-differentiable function ever is. The job of this topic is to understand *why* — to peel back what makes complex differentiability so absurdly strong, and to set up the machinery that exploits it.

The starting point is **complex differentiability**. Take $f : U \to \mathbb{C}$ defined on an open $U \subseteq \mathbb{C}$, and ask: does the limit $f'(w) = \lim_{z \to w} (f(z) - f(w))/(z - w)$ exist? Defining differentiability this way *looks* like a copy of the real case, but now $z$ approaches $w$ from *every* direction in the plane, and the ratio is a *complex* number. Setting $f = u + iv$ with $u, v$ real-valued, this dual constraint translates into a condition on the partials: $u_x = v_y$ and $u_y = -v_x$, the **Cauchy–Riemann equations**. They are not a side-effect of complex differentiability — they *are* complex differentiability, made visible at the level of real partial derivatives. The deep observation is that they are a system of *linear* PDEs satisfied by $u$ and $v$, and one consequence is that both $u$ and $v$ are *harmonic* ($\Delta u = u_{xx} + u_{yy} = 0$ and similarly for $v$). The class of holomorphic functions is thus pegged to the class of pairs of *conjugate harmonic functions*, and the rigidity of complex analysis flows from the rigidity of harmonic functions in two variables. This is the first major insight of the topic.

The second pillar is **power series**. A power series $\sum c_n (z - a)^n$ converges on a disc $D(a, R)$ — the disc of convergence — and diverges outside its closed disc. Inside, it is holomorphic, equal to its termwise derivative, and equal to its own Taylor series. The radius $R$ is given by the formula $1/R = \limsup |c_n|^{1/n}$, which is sharp; the boundary behaviour can be anything (some power series converge everywhere on the boundary, some at no boundary point, some at a Cantor-set of points). Power series are *the* concrete examples of holomorphic functions, and the converse — every holomorphic function is locally a power series — is one of the central theorems of [[Complex Analysis II — Cauchy's Theorem and its Consequences|Complex Analysis II]]. The whole edifice of the subject rests on the bijective correspondence between holomorphic functions and convergent power series.

Two specific examples bear singling out: the **complex exponential** and the **complex logarithm**. The exponential $\exp(z) = \sum z^n/n!$ converges everywhere (radius $\infty$), is entire, and equals its own derivative — a complex extension of $e^x$. Euler's formula $\exp(iy) = \cos y + i \sin y$ pops out automatically once you separate real and imaginary parts: the trigonometric functions are the imaginary slices of the exponential, and the whole zoo of trigonometric identities is a corollary of $\exp(z + w) = \exp(z) \exp(w)$. The **logarithm**, however, is not single-valued — once you ask "what is $\log z$?" you face the choice of branch, the curse and gift of complex analysis. The principal branch fixes the argument in $(-\pi, \pi]$ and cuts out the negative real axis (where the argument jumps); a *branch* of $\log$ is a continuous function $g : U \to \mathbb{C}$ with $e^{g(z)} = z$, and the obstruction to existence on $U$ is exactly that $U$ contains a loop around $0$ (a topological condition!). This is the first meeting of complex analysis and topology, and it is the entry point to the whole theory of Riemann surfaces, monodromy, and covering spaces.

This topic — §1 of the Cambridge IB notes plus parallel material from Stein and the Complex Methods notes — sets up these foundations. By the end you have: complex differentiability and the Cauchy–Riemann equations; convergent power series, their differentiability, and their identity-of-coefficients property; the complex exponential, $\sin, \cos$, and their identities via Euler's formula; the logarithm and its branches, with the topological obstruction to branch existence. The second topic page picks up with contour integration and Cauchy's theorem, the engine that turns these foundations into the absurd-strength theorems of the subject.

The story to remember: **holomorphicity is a rigidity condition**. A holomorphic function is far more constrained than a real-differentiable one. Cauchy–Riemann is the local manifestation of this constraint; power series expansion is the global manifestation; and every theorem in the subject — Cauchy's integral formula, Liouville, the identity theorem, the maximum modulus principle — is a different facet of "holomorphic functions are rigid".

---

# Concept Map

## §1.1 Domains and Curves

- **[[Def - Domain in the Complex Plane]]**
	- A **domain** $D \subseteq \mathbb{C}$ is a nonempty path-connected open subset. The path-connectedness is essential — without it, holomorphic functions can be locally constant on a component and arbitrary on another, breaking the analytic continuation results. By the topology of $\mathbb{C} \cong \mathbb{R}^2$, path-connected open sets coincide with connected open sets. Standard examples: $\mathbb{C}$, the open disc $D(a, r)$, half-planes, $\mathbb{C} \setminus \{0\}$, $\mathbb{C} \setminus (-\infty, 0]$ (slit plane).

- **[[Def - Curve and C1 Curve]]**
	- A **curve** is a continuous map $\gamma : [a, b] \to \mathbb{C}$. It is **$C^1$** (continuously differentiable) if $\gamma'$ exists and is continuous on $[a, b]$ (with one-sided derivatives at the endpoints). It is **piecewise $C^1$** if $[a, b]$ admits a partition $a = t_0 < t_1 < \ldots < t_n = b$ such that $\gamma|_{[t_{i-1}, t_i]}$ is $C^1$. A curve is **closed** if $\gamma(a) = \gamma(b)$; **simple** if it is injective on $[a, b)$. The image $\gamma^* = \gamma([a, b])$ is the **trace** of the curve; the curve itself is the *parametrization*.

## §1.2 Complex Differentiation and the Cauchy–Riemann Equations

- **[[Def - Holomorphic Function]]**
	- $f : U \to \mathbb{C}$ is **(complex) differentiable at** $w \in U$ if the limit $f'(w) = \lim_{z \to w} (f(z) - f(w))/(z - w)$ exists in $\mathbb{C}$; the limit must exist for every direction of approach. $f$ is **holomorphic at $w$** if it is differentiable on some disc $D(w, r)$, and **holomorphic on $U$** if differentiable at every point of $U$. $f$ is **entire** if holomorphic on $\mathbb{C}$. The same formal rules (sum, product, quotient, chain) hold as in real analysis; the proofs are identical.

- **[[Thm - Cauchy–Riemann Equations]]**
	- For $f = u + iv$ with $u, v$ real and $f$ defined near $w = c + id \in U$: $f$ is complex differentiable at $w$ if and only if $u, v$ are real-differentiable at $(c, d)$ as functions $\mathbb{R}^2 \to \mathbb{R}$ AND satisfy the **Cauchy–Riemann equations** $u_x = v_y$ and $u_y = -v_x$ at $(c, d)$. When this holds, $f'(w) = u_x + i v_x = v_y - i u_y$. The CR equations are *the* condition for real differentiability to upgrade to complex differentiability. The forward direction is direct; the converse requires real differentiability (not just existence of partials) and is the substance of the theorem.

- **[[Thm - Constant on a Domain if Derivative is Zero]]**
	- If $f$ is holomorphic on a domain $D$ and $f'(z) = 0$ for all $z \in D$, then $f$ is constant. The proof uses path-connectedness of $D$: along any $C^1$ path from $w$ to $z$, the chain rule gives $(f \circ \gamma)' = 0$, so $f(\gamma(t))$ is constant, hence $f(z) = f(w)$. Equally true for any $f \in C^1$ with all partials zero — the *complex* version is just the special case under the Cauchy–Riemann linkage.

- **[[Thm - Real and Imaginary Parts of a Holomorphic Function are Harmonic]]**
	- If $f = u + iv$ is holomorphic on $U$ and $u, v$ are $C^2$ (which, by the regularity theorem, is automatic from holomorphic), then $\Delta u = u_{xx} + u_{yy} = 0$ and $\Delta v = 0$ — both real and imaginary parts are **harmonic**. The proof is one line: differentiate the CR equations once more. This is the bridge from complex analysis to potential theory, fluid dynamics (velocity potentials), and electrostatics.

- **[[Ex - Verifying Cauchy–Riemann for z2 and exp(z)]]** (⭐)
	- Verify directly that $f(z) = z^2$ and $f(z) = e^z$ satisfy the CR equations on $\mathbb{C}$. For $z^2$: $u(x,y) = x^2 - y^2, v(x,y) = 2xy$; check $u_x = 2x = v_y$ and $u_y = -2y = -v_x$. For $e^z$: $u = e^x \cos y, v = e^x \sin y$; verify directly.

- **[[Ex - The function f(z) = bar z is not differentiable]]** (⭐)
	- Show that $f(z) = \bar z$ is real-differentiable everywhere but complex-differentiable nowhere. The CR equations fail ($u = x, v = -y, u_x = 1, v_y = -1$). Concretely, the limit $(\bar z - \bar w)/(z - w)$ takes value $1$ along $z = w + t$ and $-1$ along $z = w + it$, so does not exist.

- **[[Ex - A function with all partials but not differentiable]]** (⭐⭐⭐)
	- Looman–Menchoff phenomenon: a function $f$ can satisfy the CR equations everywhere yet not be holomorphic, if real-differentiability fails. Construct an explicit example such as $f(z) = e^{-1/z^4}$ for $z \neq 0$, $f(0) = 0$, which is *not* holomorphic at $0$ despite CR equations holding there.

> [!tip] Unlocked: Harmonic Function Theory *(from Analysis / PDE)*
> The real and imaginary parts of holomorphic functions are exactly the **conjugate harmonic pairs**, and the theory of harmonic functions in 2D is the real-variable shadow of complex analysis. Properties like the mean value property, maximum modulus, the Poisson kernel, and Liouville's theorem all have harmonic analogues — and the bridge is exactly $f = u + iv$ holomorphic. See **harmonic conjugate**, **Poisson integral**, **Laplace equation**.

> [!note] Exercise Index — §1.2
> [[Exercise Index - §1.2 Cauchy–Riemann]]

## §1.3 Power Series

- **[[Def - Power Series and Radius of Convergence]]**
	- A **power series** centred at $a \in \mathbb{C}$ is $\sum_{n=0}^\infty c_n (z - a)^n$ for some sequence $\{c_n\} \subseteq \mathbb{C}$. Its **radius of convergence** is $R = 1/\limsup |c_n|^{1/n}$, with the conventions $1/0 = \infty$, $1/\infty = 0$. The series converges absolutely on $D(a, R)$ and diverges for $|z - a| > R$. Behaviour on the circle $|z - a| = R$ is undetermined — depends on the series.

- **[[Thm - Radius of Convergence Formula and Uniform Convergence on Sub-Discs]]**
	- Let $R = 1/\limsup |c_n|^{1/n}$. Then for $0 < r < R$, the power series $\sum c_n (z - a)^n$ converges uniformly on $\overline{D(a, r)}$. For $|z - a| > R$, the series diverges. The proof for convergence uses the root test; for uniform convergence, the Weierstrass $M$-test with $M_n = |c_n| r^n$. The uniform convergence on compact subsets of the disc is what allows the next theorem: termwise differentiation and integration.

- **[[Thm - Power Series is Holomorphic with Termwise Derivative]]**
	- If $f(z) = \sum c_n (z - a)^n$ has radius of convergence $R$, then $f$ is holomorphic on $D(a, R)$ and $f'(z) = \sum n c_n (z - a)^{n-1}$. The derivative series has the *same* radius $R$ (since $\limsup |n c_n|^{1/n} = \limsup |c_n|^{1/n}$). By induction, $f \in C^\infty$ on $D(a, R)$, $f^{(k)}(a) = k! c_k$, and $f$ equals its Taylor series at $a$ inside $D(a, R)$. This is the prototype "power series defines a holomorphic function" theorem.

- **[[Thm - Identity Theorem for Power Series]]**
	- If $\sum c_n (z - a)^n = \sum d_n (z - a)^n$ on a nonempty open subset of $D(a, R)$, then $c_n = d_n$ for all $n$. The proof: at $z = a$, $c_0 = d_0$; subtract, divide by $(z - a)$, take $z \to a$ for $c_1 = d_1$; iterate. This is the "if two power series agree on an open set, they are equal" theorem, the seed of the much stronger identity theorem for holomorphic functions in [[Complex Analysis II — Cauchy's Theorem and its Consequences|Complex Analysis II]].

- **[[Ex - Computing radii of convergence]]** (⭐)
	- Compute the radii of convergence for: $\sum z^n$ ($R = 1$), $\sum z^n/n!$ ($R = \infty$), $\sum n! z^n$ ($R = 0$), $\sum z^n/n^2$ ($R = 1$). Note convergence on the unit circle differs: $\sum z^n$ diverges everywhere on $|z| = 1$, $\sum z^n/n^2$ converges absolutely everywhere on $|z| = 1$.

- **[[Ex - Termwise differentiation of a power series]]** (⭐⭐)
	- Compute the derivative of $f(z) = \sum_{n=0}^\infty z^n = 1/(1 - z)$ on $D(0, 1)$ in two ways: directly, getting $1/(1 - z)^2$; termwise, getting $\sum_{n=1}^\infty n z^{n-1}$. Verify they agree.

- **[[Ex - Power series with prescribed radius of convergence]]** (⭐⭐)
	- Given any $R \in [0, \infty]$, construct an explicit power series with radius exactly $R$. For $R = 1$, use $\sum z^n$; for general $R > 0$, use $\sum z^n/R^n$; for $R = 0$, use $\sum n! z^n$; for $R = \infty$, use $\sum z^n/n!$.

> [!note] Exercise Index — §1.3
> [[Exercise Index - §1.3 Power Series]]

## §1.4 The Exponential, Trigonometric Functions, and Logarithm

- **[[Def - Complex Exponential and Trigonometric Functions]]**
	- The **complex exponential** is $\exp(z) = \sum_{n=0}^\infty z^n/n!$, with radius of convergence $\infty$. Define $\sin z = (\exp(iz) - \exp(-iz))/(2i)$ and $\cos z = (\exp(iz) + \exp(-iz))/2$ — equivalently, the power series $\sin z = \sum (-1)^n z^{2n+1}/(2n+1)!$ and $\cos z = \sum (-1)^n z^{2n}/(2n)!$. All three are entire. **Euler's formula**: $\exp(iy) = \cos y + i \sin y$ for $y \in \mathbb{R}$.

- **[[Thm - Properties of the Complex Exponential]]**
	- (i) $\exp$ is entire with $\exp'(z) = \exp(z)$. (ii) The addition formula $\exp(z + w) = \exp(z)\exp(w)$ for all $z, w$ (proved by the binomial identity applied to the power series, or by noting both sides are holomorphic and agree on $\mathbb{R}$ then applying the identity theorem). (iii) $\exp(z) \neq 0$ for any $z$ (since $\exp(z) \exp(-z) = 1$). (iv) $\exp(z)$ has period $2\pi i$: $\exp(z + 2\pi i) = \exp(z)$. (v) $\exp : \mathbb{C} \to \mathbb{C}^\times$ is surjective.

- **[[Def - Branch of the Logarithm]]**
	- Given an open $U \subseteq \mathbb{C}^\times$, a **branch of the logarithm on $U$** is a continuous $g : U \to \mathbb{C}$ with $\exp(g(z)) = z$ for all $z \in U$. When it exists, $g$ is automatically holomorphic with $g'(z) = 1/z$. Two branches differ by an integer multiple of $2\pi i$. The **principal branch** $\operatorname{Log}$ is defined on the slit plane $\mathbb{C} \setminus (-\infty, 0]$ by $\operatorname{Log}(z) = \log|z| + i\operatorname{Arg}(z)$ where $\operatorname{Arg}(z) \in (-\pi, \pi)$.

- **[[Thm - Existence of a Logarithm on Simply Connected Domains]]**
	- A branch of the logarithm exists on $U \subseteq \mathbb{C}^\times$ if and only if $U$ has no closed curve with nonzero winding number around $0$. The slit plane works; the punctured plane $\mathbb{C}^\times$ does not (the curve $|z| = 1$ has winding number $1$). For a simply connected $U \subseteq \mathbb{C}^\times$, a branch exists — this is the topological obstruction, the first appearance of the deep link between complex analysis and topology.

- **[[Def - Complex Power]]**
	- For $z \neq 0$ and $\alpha \in \mathbb{C}$, define $z^\alpha := \exp(\alpha \operatorname{Log} z)$ using the principal branch (where defined). For different branches one gets different values. When $\alpha = 1/n$ for integer $n$, $z^{1/n}$ is one of the $n$ $n$-th roots of $z$. For integer $\alpha$, $z^\alpha$ is single-valued and equals the usual power. The multi-valued character is the source of "branch cut" choices needed in integration along contours.

- **[[Ex - Euler's formula and trigonometric identities]]** (⭐)
	- Use $\exp(i(\theta + \phi)) = \exp(i\theta) \exp(i\phi)$ to derive the addition formulas $\cos(\theta + \phi) = \cos\theta\cos\phi - \sin\theta\sin\phi$ and $\sin(\theta + \phi) = \sin\theta\cos\phi + \cos\theta\sin\phi$.

- **[[Ex - Computing log(-1) and log(i)]]** (⭐)
	- Show $\operatorname{Log}(-1)$ is undefined in the principal branch (boundary of slit plane), but other branches give $\operatorname{Log}(-1) = i\pi$ (or $i\pi + 2\pi i k$). Compute $\operatorname{Log}(i) = i\pi/2$ in the principal branch.

- **[[Ex - Failure of log existence on the punctured plane]]** (⭐⭐⭐)
	- Show that no continuous $g : \mathbb{C}^\times \to \mathbb{C}$ satisfies $\exp(g(z)) = z$. Argue topologically: $\exp$ has degree $0$ on any small disc but $\mathbb{C}^\times$ has a loop with winding $1$ around $0$, contradicting any continuous lift.

> [!tip] Unlocked: Riemann Surfaces *(from Complex Geometry)*
> The multi-valued $\log z$ and $\sqrt{z}$ are best understood as single-valued functions on a *covering space* of $\mathbb{C}^\times$ — the **Riemann surface** of the logarithm or square root. This is the gateway to the theory of Riemann surfaces, where multi-valued analytic objects become single-valued on appropriate covering spaces. The branch-cut machinery of §1.4 is the practical handling of multi-valuedness without the abstract setup.

> [!note] Exercise Index — §1.4
> [[Exercise Index - §1.4 Exp, Log, Powers]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

The recurring targets in this opening chapter are: *check holomorphicity* of a specific function (via CR or via power series expansion), *compute the radius of convergence* of a series, *manipulate power series* (compose, multiply, differentiate, integrate), *handle multi-valued functions* (logarithms, powers) via branch choice, and *exhibit equality of two complex functions* using the identity-of-power-series machinery.

A second cluster of targets is *bridge statements*: convert a real-analytic identity to a complex-analytic one (Euler's formula and trig identities), or convert a complex-analytic identity back to a pair of real-analytic statements (the CR equations from holomorphicity).

**Sources — What assumptions do we usually leverage?**

Standard assumption patterns: (1) *a power series representation* — when given, the function is automatically holomorphic and one has the coefficient formula $f^{(n)}(a) = n! c_n$; (2) *holomorphicity on a domain* — implies CR equations, harmonicity of real and imaginary parts, and many rigid constraints proved in [[Complex Analysis II — Cauchy's Theorem and its Consequences|Complex Analysis II]]; (3) *real differentiability + CR* — sufficient for complex differentiability; (4) *simply connectedness of a domain* — guarantees existence of branches of log and square root.

Most problems route through one of these source-target pairs in one or two steps: from a power series and the radius formula to evaluation at a specific point; from CR and harmonicity to a PDE statement; from differentiability of an explicit formula to checking CR by hand.

---

# Legal Operations

1. **Convert holomorphicity to the Cauchy–Riemann equations and back.** This is the foundational move: $f = u + iv$ holomorphic at $w$ if and only if $u, v$ are real-differentiable at $w$ and the CR equations hold. *Trigger:* any holomorphicity statement. *Pattern:* split into real and imaginary parts, check $u_x = v_y, u_y = -v_x$.

2. **Differentiate a power series termwise.** Inside the radius of convergence, $f(z) = \sum c_n (z - a)^n$ is holomorphic with $f'(z) = \sum n c_n (z - a)^{n-1}$, same radius. *Trigger:* you have a power series and want its derivative. *Pattern:* apply the termwise differentiation theorem, identify the new coefficients.

3. **Use the radius of convergence formula.** Apply $R = 1/\limsup |c_n|^{1/n}$ to compute the radius of any explicit series. Special tricks: ratio test $R = \lim |c_n/c_{n+1}|$ when the limit exists. *Trigger:* compute the disc of convergence of an explicit series.

4. **Multiply and compose power series.** The Cauchy product $(\sum a_n z^n)(\sum b_n z^n) = \sum c_n z^n$ with $c_n = \sum_{k=0}^n a_k b_{n-k}$ holds within the intersection of radii. Composition is more subtle — requires inner series to vanish at the centre. *Trigger:* a power series problem involving products or compositions.

5. **Use the addition formula for $\exp$.** $\exp(z + w) = \exp(z) \exp(w)$ holds for all complex $z, w$. *Trigger:* manipulating exponentials, deriving trig identities. *Pattern:* set up the identity, apply addition formula, separate real and imaginary parts.

6. **Choose a branch of the logarithm.** When dealing with multi-valued $\log z$ or $z^\alpha$, choose a branch on a simply connected domain that excludes the singularity at $0$. The slit plane is the default; for more exotic contours, slit along a different ray. *Trigger:* multi-valued function in an integral, in an algebraic manipulation, or in an analytic continuation problem.

7. **Pass from power-series identity to functional identity.** Two power series with the same coefficients give the same function on their common disc of convergence. Conversely, if two power series agree on an open set, their coefficients agree. *Trigger:* equality of two holomorphic functions on a disc. *Pattern:* expand both in power series, compare coefficients.

8. **Use Euler's formula to translate trig to exponential.** $\cos\theta = (e^{i\theta} + e^{-i\theta})/2$, $\sin\theta = (e^{i\theta} - e^{-i\theta})/(2i)$. *Trigger:* a trigonometric identity to verify or an oscillatory integral to evaluate. *Pattern:* convert all trig functions to exponentials, manipulate algebraically, separate real and imaginary.

**Illegal but tempting operations:**

> [!warning] 1. Concluding holomorphicity from existence of partials
> Having $u, v$ with continuous partial derivatives satisfying CR is *not* enough on its own to conclude complex differentiability — you need real differentiability of $u, v$ as maps $\mathbb{R}^2 \to \mathbb{R}$. Continuous partials *do* imply real differentiability (a real analysis theorem), so the standard hypotheses "$u, v \in C^1$ + CR" are sufficient. But "all partials exist" is *not*; the Looman–Menchoff counterexample shows partial-derivative existence + CR can fail to give holomorphicity at isolated points.

> [!warning] 2. Treating $\log z$ as a single-valued function on $\mathbb{C}^\times$
> The logarithm is multi-valued: $\log z$ has values $\log|z| + i(\arg z + 2\pi k)$ for $k \in \mathbb{Z}$. A "branch" is a continuous choice; on $\mathbb{C}^\times$ there is no such global choice. Forgetting this is the source of errors like "$\log(z_1 z_2) = \log z_1 + \log z_2$" — this can fail by a $2\pi i$ shift depending on branches. Always specify the branch.

> [!warning] 3. Differentiating a divergent or conditionally convergent series termwise
> Termwise differentiation is justified *strictly within* the open disc of convergence, where convergence is absolute and uniform on compact subsets. On the boundary $|z - a| = R$, the derivative series may diverge even where the original converges (e.g. $\sum z^n/n$ converges at $z = -1$ but its derivative $\sum z^{n-1}$ does not). Termwise operations require absolute uniform convergence.

> [!warning] 4. Assuming complex differentiable implies real-analytic by definition
> Complex differentiable on an open set implies infinitely differentiable and analytic — this is a *theorem* (proved in [[Complex Analysis II — Cauchy's Theorem and its Consequences|Complex Analysis II]] via Cauchy's integral formula), not a definition. In real variables, $f \in C^1$ does *not* imply $f \in C^\infty$ or analytic. The "$C^1 \Rightarrow C^\infty$" miracle is purely complex.

---

# Problem-Solving Strategy

Problems at this level cluster into three families. The first is **verifying or applying holomorphicity** of a specific function. For a function given by an explicit formula in $z, \bar z, x, y$: separate $u = \operatorname{Re} f$ and $v = \operatorname{Im} f$, compute partials, check CR. If the formula is in terms of $z$ alone (no $\bar z$), the function is automatically holomorphic, since $\partial/\partial \bar z = 0$ — this is the cleanest sufficient condition. If $\bar z$ appears, CR usually fails. The shortcut is the **Wirtinger criterion**: $f$ is holomorphic if and only if $\partial f/\partial \bar z = 0$, where $\partial/\partial \bar z = \tfrac12(\partial_x + i\partial_y)$. This is a one-line check for explicit formulas.

The second family is **power series manipulation**. Given a series, compute its radius of convergence; manipulate by multiplication, differentiation, integration termwise; identify it as a known function. The toolkit: ratio test (when $\lim |c_n/c_{n+1}|$ exists), root test (the universal formula $R = 1/\limsup |c_n|^{1/n}$), termwise differentiation/integration on $D(a, R)$. Specifically for sums of geometric and exponential series, use the explicit formulas $\sum z^n = 1/(1-z)$ for $|z| < 1$ and $\sum z^n/n! = e^z$ everywhere.

The third family is **branch-cut manipulation** for multi-valued functions. The choice of branch is dictated by (a) where the branch points lie (typically at $0, \infty$, and isolated singularities) and (b) where the singularities of the function lie. The principal branch of $\log$ excludes the negative real axis; for contour integrals enclosing $0$, one often chooses a different branch (the "keyhole" contour, in [[Complex Analysis IV — Mapping Theory and Applications|Complex Analysis IV]]). The discipline: state the branch you are using *before* manipulating.

A non-obvious general principle: complex analysis has a **rigidity principle** at every scale. A power series is determined by its coefficients; coefficients are determined by the function (via Cauchy's formula in CA II); the function on a tiny disc determines it on its whole domain (by analytic continuation, in CA II). When you have a holomorphic function and any tiny piece of information about it — a few coefficients, a couple of derivatives at a point, its values on an arc — you have *everything*. This rigidity is the whole point of the subject and the reason complex analysis works as a tool: you can deduce a function's behaviour from minimal data.

---

# Most Reusable Properties

- **[[Thm - Cauchy–Riemann Equations|Cauchy–Riemann]]**: A real-differentiable $f = u + iv$ is holomorphic at $w$ iff $u_x = v_y, u_y = -v_x$ at $w$. This is the bridge between complex and real differentiability and the source of every direct calculation of "is $f$ holomorphic?". Use it any time you have an explicit real formula.

- **[[Thm - Power Series is Holomorphic with Termwise Derivative|Termwise differentiation]]**: A power series is holomorphic inside its disc of convergence, with $f' = \sum n c_n (z - a)^{n-1}$, same radius. This is the foundational manipulation rule for power series and the source of "every power series defines a holomorphic function". Use it whenever you need to differentiate, integrate, or estimate a series.

- **[[Thm - Properties of the Complex Exponential|Properties of exp]]**: $\exp$ is entire, $\exp' = \exp$, addition formula $\exp(z + w) = \exp(z)\exp(w)$, nonzero everywhere, period $2\pi i$. These collapse complex exponential identities and trigonometric identities (via Euler) into one short list. The single property "addition formula" generates the rest.

- **Identity Theorem for Power Series**: Two power series agreeing on an open set are coefficient-wise equal. This is what makes "expand in power series, compare coefficients" work as a uniqueness argument. Used to prove the addition formula for $\exp$, to identify functions, and to prove the strong identity theorem in [[Complex Analysis II — Cauchy's Theorem and its Consequences|Complex Analysis II]].

---

# Bridges

1. **Multivariable Analysis — The Cauchy–Riemann operator as a 1-form.** Define $dz = dx + i\,dy$ and $d\bar z = dx - i\,dy$, with $\partial/\partial z, \partial/\partial \bar z$ the dual basis. Then any complex 1-form $\omega = P\,dx + Q\,dy$ decomposes as $\omega = A\,dz + B\,d\bar z$ for $A = (P - iQ)/2, B = (P + iQ)/2$. The condition for $f$ to be holomorphic is $\partial f/\partial \bar z = 0$, equivalently $df = f'\,dz$ (no $d\bar z$ component) — the **Cauchy–Riemann equations as a closedness condition on a 1-form**. This is the entry point for the de Rham complex on complex manifolds and for $\bar\partial$-cohomology. See [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] for the differential form vocabulary.

2. **Analysis — Harmonic Functions and the Laplace Equation.** Real and imaginary parts of holomorphic functions are harmonic in two variables (satisfy $\Delta u = 0$). The converse holds locally on simply connected domains: every harmonic $u$ has a harmonic conjugate $v$ making $f = u + iv$ holomorphic. So holomorphic functions on planar domains *are* pairs of conjugate harmonic functions. The maximum principle, Liouville's theorem, the mean value property, and the Poisson integral formula all have parallel statements for harmonic and holomorphic functions, and the bridge is exactly $u \mapsto u + iv$. This is the gateway to potential theory.

3. **Linear Algebra — Complex Multiplication as Rotation+Scaling.** A complex number $z = re^{i\theta}$ acts on $\mathbb{C} \cong \mathbb{R}^2$ by multiplication: $w \mapsto zw$. This is the rotation by $\theta$ composed with scaling by $r$ — equivalently, the matrix $\begin{pmatrix} r\cos\theta & -r\sin\theta \\ r\sin\theta & r\cos\theta\end{pmatrix}$ acting on $\mathbb{R}^2$. The Cauchy–Riemann equations are exactly the condition that the differential $Df_w : \mathbb{R}^2 \to \mathbb{R}^2$ is *of this form* — i.e., is multiplication by a complex number. This identification — $\mathbb{C}$-linear maps are the conformal (rotation+scaling) ones — is the deepest geometric content of complex differentiability.

4. **Group Theory — Conformal Group and Möbius Transformations.** The space of all $\mathbb{C}$-linear bijections $\mathbb{C} \to \mathbb{C}$ is $\mathbb{C}^\times$ — multiplication by a nonzero complex number — which is a topological group. The conformal automorphisms of $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ (the Riemann sphere) form the **Möbius group** $\operatorname{PGL}_2(\mathbb{C})$, holomorphic bijections of the form $z \mapsto (az + b)/(cz + d)$. The conformal automorphisms of the unit disc form $\operatorname{PSL}_2(\mathbb{R})$, the prototype of hyperbolic geometry. These groups will reappear in [[Complex Analysis IV — Mapping Theory and Applications|Complex Analysis IV]]. See [[Group Theory I — §1.1–1.2]] for the group-theoretic setup.

5. **Topology — Logarithm and Winding Number.** The obstruction to defining $\log z$ on $\mathbb{C}^\times$ is exactly that $\mathbb{C}^\times$ is not simply connected — it has a loop around the origin with winding number $1$. The notion of winding number, defined in [[Topology IV — §13–17 Quotients, Homotopy, Topological Groups, Convex Bodies, Baire|Topology IV]] via homotopy classes of paths, is the topological obstruction. This is the first appearance of the connection that defines [[Topology IV — §13–17 Quotients, Homotopy, Topological Groups, Convex Bodies, Baire|the fundamental group]]: $\pi_1(\mathbb{C}^\times) = \mathbb{Z}$, and the integer is the winding number. The whole theory of branches and analytic continuation rests on this.

---

# Insights

The **unifying frame** of §1 is that *holomorphic = $\mathbb{C}$-linear differential*. A function $f : \mathbb{C} \to \mathbb{C}$ is holomorphic iff its real differential $Df : \mathbb{R}^2 \to \mathbb{R}^2$ is, at every point, the multiplication-by-a-complex-number action — equivalently, conformal (rotation + scaling, no shear or reflection). This is the operational meaning of the Cauchy–Riemann equations: they are exactly the condition that the Jacobian matrix $\begin{pmatrix} u_x & u_y \\ v_x & v_y\end{pmatrix}$ have the form $\begin{pmatrix} a & -b \\ b & a\end{pmatrix}$. So *holomorphic functions are conformal maps*. Every other property — analyticity, the maximum principle, conformality of biholomorphisms — flows from this single geometric observation.

The **true name** of "holomorphic" is "preserves the complex structure". A complex manifold (or open subset of $\mathbb{C}$) has an extra structure beyond its topology: at each point, a way to multiply tangent vectors by $i$. A holomorphic function is one whose differential commutes with this action of $i$. This is what "Cauchy–Riemann" really says, and it is why holomorphic functions are so rigid: preserving an additional structure is a strong constraint.

A **trigger-reaction pattern** that pervades complex analysis: when you see a real integral or identity that resists direct computation, ask whether it has a complex extension — replace $x$ by $z$, look for branch cuts, deform the contour. The Fourier transform, the Mellin transform, the Laplace transform — each is a real-variable computation made tractable by complex extension. The pattern is: real problem $\to$ complex extension $\to$ holomorphic tools (contour integration, residues) $\to$ answer. This is the operational power of the subject.

A **density-as-strategy** observation: polynomials are dense in holomorphic functions on a compact set (Runge's theorem, a downstream result). So many theorems about holomorphic functions can be proved by checking them on polynomials and approximating. The density-as-strategy is structurally identical to the real-analysis use of polynomials dense in $C[0,1]$ via Weierstrass — same strategy, different ambient space.

A final observation about **the role of $\mathbb{C}$ versus $\mathbb{R}^2$**: as topological spaces, $\mathbb{C}$ and $\mathbb{R}^2$ are identical. The subject of complex analysis is what happens when one adds the *multiplication* on $\mathbb{C}$ — the ability to multiply tangent vectors by $i$ — to the topology and differentiable structure of $\mathbb{R}^2$. That single extra structure unlocks the entire subject. Anything you can do with $\mathbb{R}^2$ alone (calculus, harmonic functions, differential forms) you can do without complex analysis. Anything that genuinely uses $z$ — that uses the multiplication — is complex analysis. The lesson is structural: the leap from $\mathbb{R}^2$ to $\mathbb{C}$ is the leap from analysis on a manifold to analysis on a *holomorphic* manifold, and the difference between the two is the entire content of complex analysis.
