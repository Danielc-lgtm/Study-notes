---
type: topic
subject: complex-analysis
chapter: "2"
title: "Complex Analysis II — Contour Integration, Cauchy's Theorem, and its Consequences"
tags: [analysis, complex-analysis]
---

# Notation Registry

- $z, w \in \mathbb{C}$ — complex variables; $a \in \mathbb{C}$ — a base point
- $D = D(a, r) = \{z : |z - a| < r\}$ — open disc
- $\partial D = \{z : |z - a| = r\}$ — boundary circle
- $\gamma : [a, b] \to \mathbb{C}$ — a curve, $C^1$ or piecewise $C^1$ unless noted
- $\gamma^*$ — the trace (image) of $\gamma$
- $\int_\gamma f \,dz = \int_a^b f(\gamma(t)) \gamma'(t)\, dt$ — contour integral
- $L(\gamma) = \int_a^b |\gamma'(t)|\, dt$ — length of $\gamma$
- $F$ — a primitive (antiderivative) of $f$: a holomorphic $F$ with $F' = f$
- $f^{(n)}(a)$ — $n$-th derivative
- $\sum c_n (z - a)^n$ — power series with $c_n = f^{(n)}(a)/n!$
- $M(r) = \sup\{|f(z)| : |z - a| = r\}$ — sup of $|f|$ on a circle

---

# Motivation

§2 of complex analysis is the explosion: starting from the apparently innocent local condition of complex differentiability, every powerful global theorem of the subject comes tumbling out. The engine is **contour integration** and the central result, **Cauchy's theorem**, which states that the integral of a holomorphic function around a closed contour in a "good enough" region is zero. From that single fact, in three or four steps, one gets the Cauchy integral formula, the fact that holomorphic functions are infinitely differentiable, Liouville's theorem, the fundamental theorem of algebra, the maximum modulus principle, Morera's theorem, the identity theorem, and the full equivalence between holomorphicity and local power-series representability. This is one of the most stunning chains of implications in all of mathematics, and the job of this topic is to lay it out cleanly.

The chapter starts with **contour integrals**. For $f : U \to \mathbb{C}$ continuous and $\gamma : [a, b] \to U$ piecewise $C^1$, the contour integral is $\int_\gamma f\,dz = \int_a^b f(\gamma(t)) \gamma'(t)\,dt$. It is a complex number computed by ordinary real integration, but the geometry of the path matters: reversing the path negates the integral, concatenating paths adds, the integral over a closed path is what we care about. The **ML estimate** gives the universal bound $|\int_\gamma f\,dz| \leq M \cdot L(\gamma)$ where $M = \sup_\gamma |f|$ and $L$ is the path length. This is a tool we will use over and over again.

The crucial relationship is the **fundamental theorem for contour integrals**: if $f$ has a primitive $F$ (a holomorphic $F$ with $F' = f$) on a domain containing $\gamma$, then $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$. In particular, the integral around a closed loop is zero. The deep observation is the *converse*: if $\int_\gamma f\,dz = 0$ for every closed loop in a domain, then $f$ has a primitive. So the existence of a primitive is *equivalent* to vanishing of all closed-loop integrals. The whole game of Cauchy's theorem is to identify *when* this vanishing happens.

**Cauchy's theorem** is the answer. In its most basic form: for $f$ holomorphic on a *star-shaped* (or more generally simply-connected) domain $D$ and $\gamma$ a closed piecewise $C^1$ curve in $D$, $\int_\gamma f\,dz = 0$. The proof goes through **Goursat's theorem** — the version for the boundary of a triangle, where the path is the boundary of the triangle and the domain need not even be star-shaped. Goursat is proved by a clever subdivision argument: bisect the triangle into four smaller ones, choose the one with the largest integral, iterate, and use the local linearization of $f$ to bound the limiting integral. From Goursat to the disc version is automatic: build a primitive by integrating along radial-then-horizontal paths, since any closed curve in a disc bounds something.

The first major consequence is the **Cauchy integral formula** (CIF): for $f$ holomorphic on a disc $D(a, R)$, every $w \in D(a, \rho)$ with $\rho < R$ satisfies $f(w) = \frac{1}{2\pi i}\int_{|z - a| = \rho} \frac{f(z)}{z - w}\,dz$. This is the *reproduction formula* — the value of $f$ at any interior point is recovered from its values on a surrounding circle. The proof: apply Cauchy's theorem to $g(z) = (f(z) - f(w))/(z - w)$ on a region with a small disc around $w$ removed, then take the radius of the small disc to zero. The CIF is the engine of every rigidity result in complex analysis.

From CIF, four immediate consequences. **Liouville's theorem**: a bounded entire function is constant — proved by the CIF estimate $|f'(a)| \leq M/r$ as $r \to \infty$. **Fundamental theorem of algebra**: every non-constant polynomial has a complex root — by Liouville applied to $1/p$. **Higher derivatives**: $f^{(n)}(w) = \frac{n!}{2\pi i}\int_{|z - a| = \rho} \frac{f(z)}{(z - w)^{n+1}}\,dz$ for every $n$, in particular every holomorphic function is $C^\infty$. **Local power series expansion**: every holomorphic $f$ on $D(a, R)$ equals its Taylor series $\sum c_n (z - a)^n$ with $c_n = f^{(n)}(a)/n!$, with this series converging on $D(a, R)$. The last fact closes the loop with [[Complex Analysis I — Basic Notions|CA I]]: *holomorphic = locally a power series*.

From local power series representability, two more theorems. **Morera's theorem**: a continuous $f$ on a disc whose integral around every triangle is zero is holomorphic — the converse of (Goursat's version of) Cauchy. This is the standard tool for proving an unknown function is holomorphic. **Principle of isolated zeros**: if $f$ is holomorphic and not identically zero, its zeros are isolated. By the power-series representation, near a zero $w$, $f(z) = (z - w)^k g(z)$ with $g(w) \neq 0$, so the zero is isolated. From this, the **identity theorem**: two holomorphic functions on a connected open set agreeing on a set with an accumulation point are equal everywhere. This is one of the most-used theorems in complex analysis: it converts pointwise agreement at countably many points into agreement on a domain.

The **maximum modulus principle** rounds out the chapter: a non-constant holomorphic function on a domain cannot attain a local maximum of its modulus. Proved by the CIF — at any interior $w$, $|f(w)| \leq M(r)$ for the max modulus $M(r)$ on the surrounding circle, with equality forcing $f$ to be constant on the circle, then by analytic continuation on the whole domain. This converts a *local* maximum into a *global* statement: if $|f|$ has a local max in a domain, $f$ is constant.

The unifying frame for §2: **Cauchy's theorem is rigidity**. The vanishing of contour integrals is the local form; the integral formula is the global form; power-series representability is the algebraic form; the identity theorem is the analytical form. They are facets of one underlying fact: a holomorphic function is determined by its values on any one-dimensional curve, hence is enormously rigid as a function of two real variables. Everything you can do with this rigidity — bounding, extending, identifying, constraining — is the substance of complex analysis.

---

# Concept Map

## §2.1 Contour Integrals and Fundamental Theorem

- **[[Def - Contour Integral]]**
	- For $f : U \to \mathbb{C}$ continuous and $\gamma : [a, b] \to U$ piecewise $C^1$, the **contour integral** is $\int_\gamma f\,dz := \int_a^b f(\gamma(t)) \gamma'(t)\,dt$, a complex number. It is parametrization-invariant (under increasing $C^1$ reparametrizations of $[a,b]$), additive over concatenations, and reverses sign on reversing $\gamma$. The contour integral is the central object of the chapter — every theorem is a statement about its value on a particular contour.

- **[[Thm - ML Estimate]]**
	- For $f$ continuous on $\gamma^*$ and $M \geq \sup_{z \in \gamma^*} |f(z)|$ with $L = L(\gamma) = \int_a^b |\gamma'(t)|\,dt$, $\left|\int_\gamma f\,dz\right| \leq M \cdot L$. The proof is direct: $|\int_a^b f(\gamma(t))\gamma'(t)\,dt| \leq \int_a^b |f(\gamma(t))| |\gamma'(t)|\,dt \leq M \int_a^b |\gamma'(t)|\,dt = ML$. This is the universal tool for bounding integrals — when you can bound $|f|$ on the path, you can bound the integral.

- **[[Thm - Fundamental Theorem of Contour Integration]]**
	- If $f : U \to \mathbb{C}$ has a primitive $F$ (i.e., $F$ holomorphic with $F' = f$) on $U$, and $\gamma : [a, b] \to U$ is piecewise $C^1$, then $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$. In particular, the integral around any closed loop is zero. The proof: chain rule gives $(F \circ \gamma)'(t) = F'(\gamma(t))\gamma'(t) = f(\gamma(t))\gamma'(t)$, so the integral telescopes.

- **[[Thm - Existence of a Primitive iff Closed Integrals Vanish]]**
	- For a continuous $f$ on a *domain* $D$: $f$ has a primitive on $D$ iff $\int_\gamma f\,dz = 0$ for every closed piecewise $C^1$ curve $\gamma$ in $D$. The forward direction is the fundamental theorem. For the converse, fix $a \in D$ and define $F(z) = \int_{a \to z} f\,dz$ — path-independent by hypothesis; verify $F'(z) = f(z)$ at every $z$ using a small path increment. This converts "primitive exists" into "all closed-loop integrals vanish".

- **[[Def - Primitive (Antiderivative)]]**
	- A **primitive** (or antiderivative) of $f : U \to \mathbb{C}$ on a domain $U$ is a holomorphic $F : U \to \mathbb{C}$ with $F'(z) = f(z)$ for all $z \in U$. Two primitives on a domain differ by a constant (their difference has zero derivative, hence is constant on the connected $U$). Primitives need not exist globally: $f(z) = 1/z$ has no primitive on $\mathbb{C}^\times$ (the integral around the unit circle is $2\pi i \neq 0$), but does have primitives locally (branches of $\log$).

- **[[Ex - Computing zn dz on a circle]]** (⭐)
	- Compute $\int_{|z|=1} z^n\,dz$ for integer $n$. For $n \neq -1$, $z^{n+1}/(n+1)$ is a primitive, so the integral is zero. For $n = -1$, parametrize $\gamma(t) = e^{it}$ and compute directly: $\int_0^{2\pi} e^{-it} \cdot ie^{it}\,dt = 2\pi i$. The single nonzero integral $\int 1/z\,dz = 2\pi i$ is the seed of the entire residue theory.

> [!note] Exercise Index — §2.1
> [[Exercise Index - §2.1 Contour Integration]]

## §2.2 Cauchy's Theorem

- **[[Thm - Goursat's Theorem (Cauchy for a Triangle)]]**
	- If $f$ is holomorphic on an open set containing a closed triangle $T$ (including interior), then $\int_{\partial T} f\,dz = 0$. The proof bisects $T$ into four congruent triangles, picks the one with the largest absolute integral, iterates infinitely, and uses the local linearization of $f$ at the limiting point to bound the integral by $\varepsilon \cdot L^2 / 4^n$, which goes to zero. This is the *building block* — Cauchy's theorem for arbitrary closed curves in nice domains is built from triangles.

- **[[Thm - Cauchy's Theorem for a Star-Shaped Domain]]**
	- If $D \subseteq \mathbb{C}$ is a star-shaped open set (with respect to some $a \in D$) and $f$ is holomorphic on $D$, then $f$ has a primitive on $D$ and $\int_\gamma f\,dz = 0$ for every closed piecewise $C^1$ $\gamma$ in $D$. The primitive is $F(z) = \int_a^z f\,dw$ along the line segment (which lies in $D$ by star-shapedness); use Goursat on appropriate triangles to verify $F$ is well-defined and $F'(z) = f(z)$.

- **[[Thm - Cauchy's Theorem for a Disc]]**
	- A disc is star-shaped; the previous theorem specializes: every holomorphic function on a disc has a primitive on that disc, and integrals around closed curves vanish. This is the practical form for most calculations — most arguments reduce to local statements on discs.

- **[[Ex - Verifying Cauchy on a triangle in C minus 0]]** (⭐⭐)
	- Show that for any triangle $T$ not enclosing $0$, $\int_{\partial T} \frac{1}{z}\,dz = 0$, by exhibiting a primitive (branch of $\log$) on a star-shaped neighborhood of $T$.

> [!note] Exercise Index — §2.2
> [[Exercise Index - §2.2 Cauchy's Theorem]]

## §2.3 Cauchy Integral Formula

- **[[Thm - Cauchy Integral Formula]]**
	- Let $D = D(a, r)$ be a disc, $f : D \to \mathbb{C}$ holomorphic, $w \in D$ with $|w - a| < \rho < r$. Then $f(w) = \frac{1}{2\pi i}\int_{|z - a| = \rho} \frac{f(z)}{z - w}\,dz$. The proof: $g(z) = (f(z) - f(w))/(z - w)$ has a removable singularity at $w$ (extend continuously by $f'(w)$), is holomorphic on $D \setminus \{w\}$ and continuous at $w$; apply Cauchy's theorem to $g$ on $D$, conclude the integral of $f(z)/(z - w)$ equals the integral of $f(w)/(z - w)$, evaluate the latter directly to get $f(w) \cdot 2\pi i$. This is the *reproduction* formula — the soul of complex analysis.

- **[[Thm - Mean Value Property for Holomorphic Functions]]**
	- For $f$ holomorphic on $D(a, R)$ and $0 < r < R$, $f(a) = \frac{1}{2\pi}\int_0^{2\pi} f(a + re^{i\theta})\,d\theta$ — the value at the center is the average over the surrounding circle. Direct corollary of CIF with $w = a$. Identical to the mean value property of harmonic functions in $\mathbb{R}^2$, which is no coincidence (real and imaginary parts of $f$ are harmonic).

- **[[Ex - Computing an integral via CIF]]** (⭐)
	- Evaluate $\int_{|z| = 2} \frac{e^z}{z - 1}\,dz$ by CIF: the integrand is $f(z)/(z - 1)$ with $f(z) = e^z$ holomorphic, and $w = 1$ is inside the disc $|z| < 2$. So the integral is $2\pi i \cdot f(1) = 2\pi i e$.

> [!note] Exercise Index — §2.3
> [[Exercise Index - §2.3 CIF and Mean Value]]

## §2.4 Liouville's Theorem and Maximum Modulus

- **[[Thm - Liouville's Theorem]]**
	- Every bounded entire function is constant. Proof: from the CIF derivative formula (next section), $|f'(w)| \leq M/r$ for any $r$, where $M = \sup |f|$. Since $M$ is finite and we can take $r$ arbitrarily large, $f'(w) = 0$ for all $w$, hence $f$ is constant. The pithy form: $\mathbb{C}$ is "too small" to contain a bounded non-constant holomorphic function — a striking contrast with $\mathbb{R}$ (consider $\sin x$).

- **[[Thm - Fundamental Theorem of Algebra]]**
	- Every non-constant polynomial $p(z) \in \mathbb{C}[z]$ has a root in $\mathbb{C}$. Proof: assume not; then $1/p$ is entire and bounded ($1/|p(z)| \to 0$ as $|z| \to \infty$, so $1/p$ is bounded outside a large disc; on the large disc it is bounded by continuity). By Liouville, $1/p$ is constant, hence $p$ is constant — contradiction. This is the *cleanest* proof of FTA, using only complex analysis.

- **[[Thm - Local Maximum Modulus Principle]]**
	- If $f$ is holomorphic on $D(a, r)$ and $|f|$ attains a local maximum at $a$, then $f$ is constant on $D(a, r)$. Proof: from the mean value property, $|f(a)| \leq \frac{1}{2\pi}\int |f(a + \rho e^{i\theta})|\,d\theta \leq |f(a)|$ for $\rho$ small enough that the inequality "$|f| \leq |f(a)|$ on the circle" holds — equality forces $|f| \equiv |f(a)|$ on the circle, and varying $\rho$, on a disc. Then a continuity argument forces $f$ to be constant.

- **[[Thm - (Global) Maximum Modulus Principle]]**
	- If $f$ is holomorphic on a domain $D$ and continuous on $\overline{D}$ with $D$ bounded, then $\max_{\overline D} |f| = \max_{\partial D} |f|$ — the maximum is attained on the boundary. If the maximum is attained in the interior, $f$ is constant. Direct consequence of the local version applied at any interior maximum point.

- **[[Ex - Liouville for harmonic functions]]** (⭐⭐)
	- A bounded harmonic function $u : \mathbb{R}^2 \to \mathbb{R}$ is constant. Idea: let $v$ be a harmonic conjugate (exists locally; need to argue globally on $\mathbb{R}^2$ via simple-connectedness), so $f = u + iv$ is entire. If $u$ is bounded, $e^f$ is bounded entire (since $|e^f| = e^u$). By Liouville, $e^f$ constant, so $f$ is constant (up to $2\pi i$ branch), so $u$ is constant.

> [!note] Exercise Index — §2.4
> [[Exercise Index - §2.4 Liouville and Max Modulus]]

## §2.5 Holomorphic = Analytic, Higher Derivatives, Morera

- **[[Thm - Higher Derivatives via CIF]]**
	- For $f$ holomorphic on $D(a, R)$, $w \in D(a, \rho)$ with $\rho < R$, and every integer $n \geq 0$: $f^{(n)}(w) = \frac{n!}{2\pi i}\int_{|z - a| = \rho} \frac{f(z)}{(z - w)^{n+1}}\,dz$. Proved by differentiating the CIF under the integral sign $n$ times (justified by uniform convergence of difference quotients on compact subsets). In particular, $f \in C^\infty$ — *every holomorphic function is infinitely differentiable*, in striking contrast to real $C^1$ functions.

- **[[Thm - Cauchy Estimates]]**
	- For $f$ holomorphic on $D(a, R)$ with $M(r) = \sup_{|z-a|=r}|f(z)|$, $|f^{(n)}(a)| \leq \frac{n! M(r)}{r^n}$ for any $0 < r < R$. Proof: ML estimate applied to the higher-derivative CIF. The Cauchy estimates are the engine of Liouville's theorem and many other rigidity results — they bound the Taylor coefficients of $f$ by the size of $f$ on a circle.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]**
	- Let $f : D(a, R) \to \mathbb{C}$ be holomorphic. Then $f(z) = \sum_{n=0}^\infty c_n (z - a)^n$ for $z \in D(a, R)$, where $c_n = f^{(n)}(a)/n!$. The power series converges on all of $D(a, R)$. Combined with the converse from CA I (power series are holomorphic), this gives the equivalence: **holomorphic on an open set ⇔ locally a convergent power series**. This is the great structural theorem of the chapter.

- **[[Thm - Morera's Theorem]]**
	- If $f$ is continuous on a domain $D$ and $\int_T f\,dz = 0$ for every triangle $T \subseteq D$ (more generally, for every closed curve), then $f$ is holomorphic on $D$. This is the converse of Goursat: vanishing of triangle integrals upgrades continuity to holomorphicity. Standard use: prove a limit of holomorphic functions is holomorphic (the integral commutes with the limit). Theorem 3.6.2 in [[Complex Analysis III — Winding, Laurent, Residues|CA III]] is the canonical application.

- **[[Thm - Holomorphic Dependence on a Parameter]]**
	- Let $\varphi : D \times [a, b] \to \mathbb{C}$ be continuous with $\varphi(\cdot, s)$ holomorphic for each $s$. Then $g(z) = \int_a^b \varphi(z, s)\,ds$ is holomorphic on $D$, with $g'(z) = \int_a^b (\partial \varphi/\partial z)(z, s)\,ds$. The proof uses Morera plus Fubini to swap the orders of integration. Workhorse for showing integrals depending on a complex parameter are holomorphic.

- **[[Ex - Power series expansion of 1 over (1-z) around 0]]** (⭐)
	- $1/(1-z) = \sum_{n=0}^\infty z^n$ on $|z| < 1$, by geometric series. Verify $c_n = f^{(n)}(0)/n! = n!/n! = 1$.

- **[[Ex - Power series expansion of log(1+z) around 0]]** (⭐⭐)
	- $\operatorname{Log}(1+z) = z - z^2/2 + z^3/3 - \ldots = \sum_{n=1}^\infty (-1)^{n-1} z^n/n$ on $|z| < 1$. Derivation: differentiate to get $1/(1+z)$, geometric series, integrate termwise.

> [!note] Exercise Index — §2.5
> [[Exercise Index - §2.5 Analytic = Holomorphic]]

## §2.6 Isolated Zeros and the Identity Theorem

- **[[Thm - Principle of Isolated Zeros]]**
	- If $f$ is holomorphic on $D(w, R)$ and not identically zero on any neighborhood of $w$, and $f(w) = 0$, then there is a unique integer $k \geq 1$ (the **order of the zero**) and a holomorphic $g : D(w, R) \to \mathbb{C}$ with $g(w) \neq 0$ such that $f(z) = (z - w)^k g(z)$. In particular, $f^{-1}(0)$ has no accumulation points in $D(w, R)$ — zeros are isolated. The proof uses the local power series: $f(z) = \sum c_n (z - w)^n$ with first nonzero coefficient at index $k$, so $f(z) = (z - w)^k \sum c_{k+n}(z - w)^n = (z - w)^k g(z)$.

- **[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]**
	- Let $f, g$ be holomorphic on a connected open $D \subseteq \mathbb{C}$ and suppose $f = g$ on a subset $S \subseteq D$ that has an accumulation point in $D$. Then $f = g$ on all of $D$. Equivalently: the zero set of a nonzero holomorphic function on a connected open set has no accumulation points in the set. The proof: $h = f - g$ has a zero $w$ which is an accumulation of zeros, hence by isolated zeros $h$ is identically zero on a neighborhood; the set of points where $h$ vanishes on a neighborhood is clopen in $D$, hence all of $D$.

- **[[Ex - The identity theorem in action]]** (⭐⭐)
	- Show that if $f, g$ are holomorphic on a domain $D$ and $f(1/n) = g(1/n)$ for $n = 1, 2, \ldots$ with $0 \in D$, then $f = g$ on $D$. The points $\{1/n\}$ accumulate at $0 \in D$, so by identity theorem $f = g$.

- **[[Ex - Uniqueness of sin from real values]]** (⭐⭐)
	- Show that the complex $\sin z$ is the unique entire function agreeing with the real $\sin$ on $\mathbb{R}$. By identity theorem applied to any candidate entire extension minus our $\sin$.

> [!note] Exercise Index — §2.6
> [[Exercise Index - §2.6 Isolated Zeros and Identity]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

§2 has four signature target classes. The first is *evaluating a specific contour integral*, either via direct computation (parametrize, integrate by hand), via finding a primitive (when one exists), or via CIF (when the integrand has the right form $f(z)/(z - w)$). The second is *proving a function is holomorphic* — typically via Morera or via showing it has a power series expansion. The third is *proving a function satisfies a constraint* — Liouville, max modulus, or the identity theorem are the standard tools. The fourth is *constructing an explicit function* — usually by power series or by Cauchy's formula.

**Sources — What assumptions do we usually leverage?**

The standard hypotheses are: holomorphic on a disc (then power series and CIF apply), holomorphic on a simply-connected domain (then primitives exist and Cauchy applies), holomorphic on $\mathbb{C}$ and bounded (then constant by Liouville), holomorphic and zero on a set with accumulation point (then identically zero by identity theorem). Most problems route from one of these through CIF or its consequences to the desired conclusion.

A typical chain: "$f$ is holomorphic with property $P$" $\to$ "CIF applies on a disc" $\to$ "Cauchy estimates give a coefficient bound" $\to$ "the bound forces $P'$" $\to$ "$P'$ is the desired conclusion". This is the engine for almost every theorem in the chapter.

---

# Legal Operations

1. **Apply Cauchy's theorem to deform a contour.** A closed contour in a domain where $f$ is holomorphic can be continuously deformed (within the domain) without changing the integral. *Trigger:* an integral over a curve you want to swap for one over a simpler curve. *Pattern:* find a homotopy (a star-shaped or simply-connected region containing both), apply Cauchy on the difference.

2. **Use CIF to compute an integral.** When the integrand has the form $f(z)/(z - w)^{n+1}$ with $f$ holomorphic and $w$ inside the contour, the integral equals $\frac{2\pi i}{n!} f^{(n)}(w)$. *Trigger:* a contour integral with a "pole-like" singularity at one point. *Pattern:* identify $f, w, n$; check $f$ holomorphic in the relevant region; apply CIF.

3. **Use ML estimate to bound an integral.** $|\int_\gamma f\,dz| \leq M(\gamma) L(\gamma)$ where $M$ is the sup of $|f|$ on the path. *Trigger:* you want to bound an integral, especially in a limit. *Pattern:* identify a path where $|f|$ is small or $L$ is small; choose the path to optimize.

4. **Apply Morera to prove holomorphicity.** A continuous $f$ whose integral around every triangle (or more generally every closed curve) is zero is holomorphic. *Trigger:* you have a function defined by an integral or as a limit, and need to prove it is holomorphic. *Pattern:* compute the triangle integrals via Fubini or interchange of limit and integral; check vanishing.

5. **Use Liouville to force constancy from boundedness.** A bounded entire function is constant. *Trigger:* you have an entire function with a bound. *Pattern:* exhibit the bound, conclude constancy, identify the constant from a single value.

6. **Apply the identity theorem to extend agreement.** Two holomorphic functions on a connected domain agreeing on a set with an accumulation point are equal. *Trigger:* you want to prove $f = g$ on a whole domain knowing only finite or partial agreement. *Pattern:* the agreement set has an accumulation point (e.g., $\mathbb{R} \subseteq \mathbb{C}$, or a sequence $1/n$), conclude global equality.

7. **Use power series for local computation.** Any holomorphic function on $D(a, R)$ equals $\sum c_n (z - a)^n$ with $c_n = f^{(n)}(a)/n!$, converging on the disc. *Trigger:* you want $f$ near a point, or want to manipulate $f$ as an algebraic object. *Pattern:* compute the first few coefficients, identify the series with a known one, deduce $f$.

8. **Apply max modulus to pin a function via boundary values.** A holomorphic function on a bounded domain whose modulus attains its maximum on the interior is constant. *Trigger:* you want to bound $|f|$ on the interior, or to argue $f$ must be constant. *Pattern:* identify boundary values; conclude interior bound; if max attained inside, $f$ constant.

**Illegal but tempting operations:**

> [!warning] 1. Applying Cauchy's theorem to non-simply-connected domains without care
> Cauchy's theorem in its simplest form (closed integrals vanish) needs the domain to be star-shaped or simply-connected. On $\mathbb{C}^\times$, $\int_{|z|=1} 1/z\,dz = 2\pi i \neq 0$. The full Cauchy theorem on simply-connected domains and the residue theorem on non-simply-connected ones in [[Complex Analysis III — Winding, Laurent, Residues|CA III]] together handle the general case. Always check the topology of the domain.

> [!warning] 2. Differentiating under the integral sign without justification
> The interchange of differentiation and integration is *almost always* legal for holomorphic integrands (by Morera + Fubini), but you must specify the justification, especially for improper or unbounded integrals. Compactness of the path or uniform convergence of the parameter dependence is the standard sufficient condition.

> [!warning] 3. Treating "$f$ has a power series" as a strictly local statement
> A holomorphic $f$ on $D(a, R)$ has its full Taylor series at $a$ converging on *all* of $D(a, R)$, not just on some smaller disc. The radius of convergence is at least $R$ — equal to the distance from $a$ to the nearest singularity of $f$ in any (analytic) extension.

> [!warning] 4. Confusing "zeros are isolated" with "zeros form a discrete set globally"
> The isolated zero theorem says: on any compact subset $K \subseteq D$ of a connected domain, a non-identically-zero holomorphic function has finitely many zeros. Globally on $D$ the zero set is countable but not necessarily discrete in $\mathbb{C}$ (it can accumulate at the boundary of $D$). The zero set of $\sin(1/(1-z))$ on $|z| < 1$ accumulates at $z = 1$, which is *on the boundary*, not in the domain.

---

# Problem-Solving Strategy

Problems in §2 cluster into three families: evaluating a contour integral, proving a property of a holomorphic function, and verifying a function is holomorphic.

For **evaluating a contour integral**, the universal first step is to identify the *singularities* of the integrand inside the contour. If there are none, Cauchy's theorem gives $0$ (in a simply-connected domain). If there is one singularity of the form $f(z)/(z - w)^{n+1}$ with $f$ holomorphic, CIF gives the answer. If there are multiple isolated singularities, the residue theorem (in [[Complex Analysis III — Winding, Laurent, Residues|CA III]]) sums up the contributions. For more exotic singularities (branch cuts, essential singularities), more careful contour manipulation is needed.

For **proving a holomorphic property** — boundedness, constancy, growth bounds, factorization — the standard tools are Cauchy estimates, Liouville, and the identity theorem. The pattern: bound $|f|$ on a circle (or growth as $|z| \to \infty$); apply Cauchy estimates to bound $|f^{(n)}(a)|$; conclude $f^{(n)}(a) = 0$ for high $n$ (or all $n$, by Liouville-style argument); conclude $f$ is a polynomial of bounded degree (or constant). This pattern is the *single most powerful* in the subject.

For **verifying a function is holomorphic** — typically when the function is defined by an integral, an infinite sum, or a limit — the tool is Morera's theorem. Show the function is continuous, then verify its triangle integrals vanish by interchanging integral and triangle integral (using Fubini and Cauchy's theorem on the integrand). The interchange is the only nontrivial step, and uniform convergence or dominated convergence usually does the job.

A non-obvious general principle: **Cauchy's theorem is most useful when you can deform a complicated contour to a simple one**. The integral $\int_\gamma f\,dz$ is independent of the path within a region where $f$ is holomorphic. So replacing $\gamma$ by a circle, a line segment, a keyhole contour, or any other tractable curve preserves the value. The art of contour integration is in choosing the right contour to make the computation tractable while preserving the value via Cauchy. This skill becomes essential in [[Complex Analysis III — Winding, Laurent, Residues|CA III]] and [[Complex Analysis IV — Mapping Theory and Applications|CA IV]].

---

# Most Reusable Properties

- **[[Thm - Cauchy Integral Formula|CIF]]**: $f(w) = \frac{1}{2\pi i}\int_{|z - a| = \rho} \frac{f(z)}{z - w}\,dz$ for $f$ holomorphic on a disc containing $w$. The single most important formula in complex analysis — it reproduces $f$ from its boundary values, gives all higher derivatives, and is the engine of every rigidity theorem. Use it any time you have a holomorphic function and want to access its values or derivatives at an interior point from boundary information.

- **[[Thm - Cauchy Estimates]]**: $|f^{(n)}(a)| \leq n!M(r)/r^n$. The universal bound on Taylor coefficients by the sup-norm on a circle. Use it to bound derivatives, to prove Liouville-type statements, and to control how a holomorphic function "spreads" from a small region.

- **[[Thm - Liouville's Theorem|Liouville]]**: bounded entire is constant. The cleanest source of "constancy from boundedness" arguments — proves the fundamental theorem of algebra, the uniqueness of conformal automorphisms of the plane, and the constancy of bounded harmonic functions. Use it any time you have an entire function with a finite bound.

- **[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)|Identity theorem]]**: equality on a set with an accumulation point implies equality on the whole connected domain. The standard tool for extending agreement from finite or countable data to a whole domain. Use it to identify functions, to extend identities from real to complex, and to prove uniqueness of analytic continuations.

- **[[Thm - Morera's Theorem|Morera]]**: vanishing triangle integrals + continuity = holomorphic. The converse of Cauchy and the standard tool for proving an "unknown" function (defined by an integral, a series, or a limit) is holomorphic. Use it whenever Cauchy's theorem cannot be directly applied because the function is not known to be holomorphic a priori.

---

# Bridges

1. **Multivariable Analysis — Cauchy's Integral Formula as Stokes' Theorem.** The Cauchy integral formula is, secretly, a special case of [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|Stokes' theorem]] applied to the 1-form $\omega = f(z)\,dz$. Since $f$ holomorphic ⇔ $d\omega = 0$ (the closedness of $\omega$ as a complex 1-form), $\omega$ is exact on simply-connected domains, and Stokes' theorem applied to the difference of two contours gives Cauchy's theorem. The whole machinery of contour integration is the complex shadow of integration of differential forms.

2. **Real Analysis — Holomorphic ⇒ $C^\infty$ as a Regularity Theorem.** That every holomorphic function is $C^\infty$ is, from the perspective of real analysis, a *regularity theorem*: weak smoothness (single complex derivative) implies full smoothness ($C^\infty$). This is parallel to elliptic regularity in PDE theory: solutions to elliptic equations (the Cauchy–Riemann system is an elliptic system) automatically have higher regularity than the equation requires. The "bootstrap" argument in PDE has the same flavour as the higher-derivative CIF: one derivative gives infinitely many.

3. **Functional Analysis — Cauchy Estimates and Operator Norms.** The Cauchy estimates control how the size of $f$ on a circle bounds the size of its derivatives. In operator theory, the holomorphic functional calculus uses Cauchy's formula to define $f(T)$ for an operator $T$ and a function $f$ holomorphic on the spectrum, with $f(T) = \frac{1}{2\pi i}\oint_\gamma f(z) (z - T)^{-1}\,dz$ — an operator-valued integral around the spectrum. The Cauchy estimates then bound $\lVert f(T)\rVert$ by the sup-norm of $f$ on $\gamma$, giving a powerful operator-norm control.

4. **Probability — Characteristic Functions are Holomorphic.** The **characteristic function** $\varphi(t) = E[e^{itX}]$ of a real random variable extends to a holomorphic function on a strip in $\mathbb{C}$ (the strip determined by the moment generating function's domain). When the random variable has all moments finite, $\varphi$ is entire. The identity theorem then forces the characteristic function to be determined by its values at countably many points — the basis of Levy's continuity theorem ([[Thm - Lévy's Continuity Theorem]]) and other characterization results in [[Advanced Probability II — Convergence and Limit Theorems]].

5. **Algebra — Algebraic Identities via Identity Theorem.** Many algebraic identities (e.g., binomial expansions, generating function identities) can be proven by complex analysis: verify the identity on a small open set of complex numbers (or on the reals, where it is "obvious") and conclude it everywhere by the identity theorem. This pipeline turns algebraic problems into analytic ones. See [[Group Theory I — §1.1–1.2]] for analogous "characters identify representations" results.

---

# Insights

The **unifying frame** of §2 is that *contour integrals measure topology*. A closed contour integral $\oint_\gamma f\,dz$ depends only on the homotopy class of $\gamma$ in the domain where $f$ is holomorphic (a Cauchy's theorem corollary). The integrals around homotopically trivial loops are zero; the integrals around nontrivial loops are topological invariants. This is the *first appearance* of the deep relationship between analysis and topology in complex analysis, and it is the seed of the winding number, residues, and the residue theorem of [[Complex Analysis III — Winding, Laurent, Residues|CA III]].

The **true name** of Cauchy's theorem is "the differential form $f\,dz$ is closed". The condition $df = f'\,dz + 0\,d\bar z$ for holomorphic $f$ means $d(f\,dz) = 0$ — the 1-form is closed in the de Rham complex. Cauchy's theorem is then the statement that closed forms have vanishing integrals over the boundaries of small regions, which is just Stokes. The whole subject is differential forms in disguise, with the extra rigidity coming from the bilinear pairing between real and imaginary parts.

A **trigger-reaction pattern**: when you want to bound the derivatives of a holomorphic function, the trigger is "is there a circle on which I can bound $|f|$?", and the reaction is Cauchy estimates. This is the standard *quantitative* tool in complex analysis, and it has no analog in real analysis (where having a bound on $f$ tells you nothing about $f'$).

A **density-as-strategy** observation: every holomorphic function is a uniform-on-compacts limit of polynomials (Runge's theorem, a downstream result). So properties holding for polynomials, plus continuity under uniform limits, hold for all holomorphic functions. This is the *complex* analog of "$\mathbb{Q}$ is dense in $\mathbb{R}$" — polynomial functions are dense in holomorphic ones on suitable sets, and the strategy of "prove for polynomials, extend by density" is the complex analog of the standard density argument.

A final structural observation: §2's theorems are *all corollaries of one fact*. The fact is that holomorphic functions on a disc equal their Taylor series. From this single equivalence, the CIF follows (integrate $f(z)/(z-w)$ termwise), Liouville follows (an entire function bounded everywhere has Taylor coefficients zero except the constant), the maximum modulus principle follows (a Taylor series whose modulus has an interior max is constant), the identity theorem follows (matching Taylor coefficients on an open set), and Morera's theorem follows (the converse direction of holomorphic-implies-power-series). When stuck on a §2 problem, reduce to local power series — the strategy almost always works.
