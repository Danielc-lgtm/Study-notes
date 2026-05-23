---
type: topic
subject: complex-analysis
chapter: "3.1-3.4"
title: "Complex Analysis III — Winding Numbers, Simply Connected Domains, Laurent Series, Singularities, Residues"
tags: [analysis, complex-analysis]
---

# Notation Registry

- $z, w, a \in \mathbb{C}$ — complex variables and base points
- $D(a, r), \overline{D(a, r)}$ — open/closed discs
- $A(a; r, R) = \{z : r < |z - a| < R\}$ — annulus around $a$ with inner radius $r$, outer $R$
- $\gamma : [a, b] \to \mathbb{C}$ — a piecewise $C^1$ curve (closed unless noted)
- $I(\gamma; w)$ — **winding number** of $\gamma$ around $w \notin \gamma^*$
- $\sum_{n=-\infty}^\infty c_n (z - a)^n$ — Laurent series (two-sided)
- $\sum_{n=1}^\infty c_{-n} (z - a)^{-n}$ — the **principal part** of a Laurent series at $a$
- $\sum_{n=0}^\infty c_n (z - a)^n$ — the **regular** (or **holomorphic**) part
- $\operatorname{Res}_a f$ — the **residue** of $f$ at $a$ (the coefficient $c_{-1}$ of $(z - a)^{-1}$ in the Laurent expansion around $a$)
- $\operatorname{ord}_a f$ — the **order** of $f$ at $a$: integer $k$ such that $f(z) = (z - a)^k g(z)$ near $a$ with $g$ holomorphic, $g(a) \neq 0$; positive for zeros, negative for poles
- A function is **meromorphic** on $D$ if holomorphic on $D$ except at a discrete set of poles
- $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ — the Riemann sphere

---

# Motivation

§3.1–§3.4 are where complex analysis goes from a powerful local theory (CIF, Liouville, identity theorem on a disc) to a *global* theory that handles singularities, non-simply-connected domains, and the *evaluation* of integrals. The new ingredients are the **winding number**, the **Laurent series**, the **classification of isolated singularities** into removable, pole, and essential, and the master theorem of the chapter: the **residue theorem**, which gives a clean evaluation of contour integrals in terms of a single local invariant (the residue) at each enclosed singularity.

§3.1 introduces the **winding number** $I(\gamma; w)$, which counts how many times a closed curve $\gamma$ winds around a point $w$. The definition has two flavors: topological (a continuous lift of the angle function under $\theta \mapsto e^{i\theta}$) and integral (the formula $I(\gamma; w) = \frac{1}{2\pi i}\int_\gamma \frac{1}{z - w}\,dz$). They agree for piecewise $C^1$ curves, and the integral formula is what makes the winding number computable. Properties: integer-valued, locally constant in $w$ off $\gamma^*$, zero in the unbounded component of $\mathbb{C} \setminus \gamma^*$, additive under concatenation. The winding number is the first *topological invariant* of complex analysis — it captures the homotopy class of a closed curve in $\mathbb{C} \setminus \{w\}$, and via the loop $|z| = r$ around the origin, it is the integer that distinguishes $\pi_1(\mathbb{C}^\times) = \mathbb{Z}$.

§3.2 introduces **simply connected domains** — domains $D$ in which every closed curve has winding number zero around every point of $\mathbb{C} \setminus D$. (Equivalently: every closed curve is null-homotopic, every map of $S^1$ into $D$ extends to a disc, $\pi_1(D) = 0$.) The full **Cauchy theorem for simply connected domains** then says: on a simply connected open $D \subseteq \mathbb{C}$, every holomorphic function has a primitive, and every closed integral vanishes. This is the full generality of Cauchy beyond the star-shaped case, and it underwrites the existence of $\log$ branches on simply connected domains avoiding $0$, the existence of conformal maps (Riemann mapping theorem in [[Complex Analysis IV — Mapping Theory and Applications|CA IV]]), and the well-definedness of integrals modulo homotopy.

§3.3 introduces **Laurent series and singularities**. A function holomorphic on an annulus $A(a; r, R)$ admits a *two-sided* expansion $f(z) = \sum_{n=-\infty}^\infty c_n (z - a)^n$ converging on the annulus, with the positive-power part holomorphic on $D(a, R)$ and the negative-power part holomorphic on $\{|z - a| > r\}$ (and vanishing at $\infty$). When $f$ has an **isolated singularity** at $a$ (i.e., $f$ is holomorphic on a punctured disc $D(a, R) \setminus \{a\}$), the Laurent series around $a$ classifies the singularity into three types:

- **Removable**: $c_n = 0$ for all $n < 0$; the Laurent series is a power series and $f$ extends holomorphically to $a$.
- **Pole** of order $k$: $c_n = 0$ for $n < -k$ but $c_{-k} \neq 0$; equivalently, $(z - a)^k f(z)$ has a removable singularity with nonzero value at $a$, equivalently $|f(z)| \to \infty$ as $z \to a$.
- **Essential**: infinitely many $c_n$ with $n < 0$ are nonzero; equivalently, $|f|$ neither tends to a finite limit nor to $\infty$ (Casorati–Weierstrass: the image under any punctured neighborhood is dense in $\mathbb{C}$; the much stronger Great Picard says the image is *all* of $\mathbb{C}$ minus at most one point).

This trichotomy is the *complete classification of isolated singularities* of holomorphic functions, and each case has its own arithmetic. **Riemann's removable singularity theorem** characterizes removability: $a$ is removable iff $f$ is bounded near $a$. Pole characterization: $a$ is a pole iff $|f(z)| \to \infty$. Essential characterization: by Casorati–Weierstrass, iff $f(\{0 < |z - a| < \rho\})$ is dense in $\mathbb{C}$ for every $\rho > 0$.

§3.3 culminates in the **residue theorem**: for a function $f$ meromorphic in an open set containing a closed curve $\gamma$ (and the region it bounds), and assuming $\gamma$ avoids the poles, $\int_\gamma f\,dz = 2\pi i \sum_w I(\gamma; w) \operatorname{Res}_w f$ — the integral equals $2\pi i$ times the sum of *winding-weighted residues*. This is the master theorem for evaluating contour integrals: identify the poles inside the contour, compute their residues, weight by winding number, sum.

§3.4 then unleashes the residue theorem on **definite real integrals**. Many integrals that resist real-analytic methods (rational functions $\int \frac{P}{Q}\,dx$, trigonometric integrals $\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta$, oscillatory integrals $\int e^{ikx} f(x)\,dx$ with **Jordan's lemma** controlling the upper-arc contribution) become tractable by extending to a complex contour, applying residues, and reading off the real part. The "keyhole" and "rectangular" contours of [[Complex Analysis IV — Mapping Theory and Applications|CA IV]] (and the complex methods PDF) handle even more exotic situations: integrals involving $\log$ or fractional powers, integrals along rays, integrals with cuts and barriers.

The unifying frame for §3.1–3.4: **the value of a contour integral is a sum of local data, weighted by topology**. The local data is the residue (a single complex number per singularity), the topology is the winding number (an integer per singularity), and the sum collapses the entire global integral to a finite sum of products. This is one of the most powerful integration techniques known, and it reflects the deep principle that, in complex analysis, integrals are topological invariants of curves on punctured domains.

---

# Concept Map

## §3.1 Winding Number

- **[[Def - Winding Number]]**
	- For a closed continuous curve $\gamma : [a, b] \to \mathbb{C} \setminus \{w\}$, the **winding number** $I(\gamma; w)$ is the integer counting how many times $\gamma$ winds around $w$. Defined topologically as the difference $\tilde\gamma(b) - \tilde\gamma(a)$ of any continuous lift $\tilde\gamma$ of $\gamma - w$ under $e^{i\cdot} : \mathbb{R} \to \mathbb{C}^\times$, divided by $2\pi$. For piecewise $C^1$ curves, equal to $\frac{1}{2\pi i}\int_\gamma \frac{dz}{z - w}$. Integer-valued, locally constant in $w$ on $\mathbb{C} \setminus \gamma^*$, equal to $0$ in the unbounded component of $\mathbb{C} \setminus \gamma^*$.

- **[[Thm - Existence and Properties of the Winding Number]]**
	- $I(\gamma; w)$ is well-defined (the lift exists by topology — see [[Topology IV — §13–17 Quotients, Homotopy, Topological Groups, Baire|Topology IV]] for lifts) and equal to the integral formula for piecewise $C^1$ $\gamma$. It depends only on the homotopy class of $\gamma$ in $\mathbb{C} \setminus \{w\}$. Reversal: $I(\gamma^{-1}; w) = -I(\gamma; w)$. Concatenation: $I(\gamma_1 \cdot \gamma_2; w) = I(\gamma_1; w) + I(\gamma_2; w)$.

- **[[Ex - Computing the winding number of a circle]]** (⭐)
	- Compute $I(\gamma; 0)$ where $\gamma(t) = e^{2\pi i k t}$ for $t \in [0, 1]$ and $k \in \mathbb{Z}$. Direct evaluation: $I = \frac{1}{2\pi i}\int_0^1 (1/e^{2\pi ikt})(2\pi ik e^{2\pi i k t})\,dt = k$. So $\gamma$ winds $k$ times around $0$.

- **[[Ex - Winding number of a figure eight]]** (⭐⭐)
	- For the figure-eight $\gamma$ in $\mathbb{R}^2$ that wraps clockwise around one loop and counterclockwise around the other, compute the winding number around a point in each loop ($\pm 1$) and around a point outside ($0$).

## §3.2 Simply Connected Domains and Cauchy

- **[[Def - Simply Connected Domain in Complex Analysis]]**
	- An open $U \subseteq \mathbb{C}$ is **simply connected** in the complex-analytic sense if $I(\gamma; w) = 0$ for every closed piecewise $C^1$ $\gamma$ in $U$ and every $w \in \mathbb{C} \setminus U$. This is equivalent (for open subsets of $\mathbb{C}$) to the topological notion of simply-connectedness ($\pi_1(U) = 0$, every loop null-homotopic). The discrepancy in name traces to a few non-equivalent technical definitions for general topological spaces, but on $\mathbb{C}$ they all coincide.

- **[[Thm - Cauchy's Theorem for Simply Connected Domains]]**
	- For $U$ simply connected open in $\mathbb{C}$ and $f$ holomorphic on $U$: every closed piecewise $C^1$ curve $\gamma$ in $U$ has $\int_\gamma f\,dz = 0$, equivalently $f$ has a primitive on $U$. This is the full generality of Cauchy's theorem and the one one typically uses. The proof reduces to triangulating the curve via Goursat-style arguments plus the simple-connectedness assumption.

- **[[Thm - Existence of Log and Square Root on Simply Connected Domains]]**
	- Let $U$ be simply connected and avoid $0$. Then $1/z$ has a primitive on $U$ — i.e., a branch of $\log$ exists on $U$. Likewise, $z^{1/2}$, $z^\alpha$, $\sqrt[n]{z}$ all have branches on simply connected domains avoiding $0$. The slit plane $\mathbb{C} \setminus (-\infty, 0]$ is the prototype, but any simply connected subset of $\mathbb{C}^\times$ works.

> [!note] Exercise Index — §3.1–3.2
> [[Exercise Index - §3.1-3.2 Winding and Simply Connected]]

## §3.3 Laurent Series and Singularities

- **[[Def - Laurent Series]]**
	- A **Laurent series** centred at $a$ is a two-sided formal sum $\sum_{n=-\infty}^\infty c_n (z - a)^n$. It **converges** at $z$ if both $\sum_{n=0}^\infty c_n (z - a)^n$ and $\sum_{n=1}^\infty c_{-n} (z - a)^{-n}$ converge. The natural domain of convergence is an annulus $A(a; r, R)$ with $r = \limsup |c_{-n}|^{1/n}$ and $1/R = \limsup |c_n|^{1/n}$.

- **[[Thm - Laurent Series Theorem]]**
	- Let $f$ be holomorphic on an annulus $A(a; r_0, R_0)$. Then $f(z) = \sum_{n=-\infty}^\infty c_n (z - a)^n$ for $z \in A(a; r_0, R_0)$, with coefficients $c_n = \frac{1}{2\pi i}\int_{|z - a| = \rho} \frac{f(z)}{(z - a)^{n+1}}\,dz$ for any $r_0 < \rho < R_0$. The series converges absolutely on the annulus, uniformly on compact subsets. The proof uses two applications of CIF — one for the inner circle, one for the outer — on the function $f$ split as positive and negative power parts.

- **[[Def - Isolated Singularity]]**
	- A point $a$ is an **isolated singularity** of $f$ if $f$ is holomorphic on some punctured disc $D(a, R) \setminus \{a\}$ but is not (defined or) holomorphic at $a$. The Laurent series at $a$ then classifies $a$ into one of three types: removable, pole of finite order, or essential.

- **[[Def - Removable Singularity, Pole, Essential Singularity]]**
	- Let $a$ be an isolated singularity of $f$, with Laurent series $\sum c_n (z - a)^n$.
		(i) $a$ is **removable** iff $c_n = 0$ for $n < 0$; iff $f$ has a holomorphic extension to $D(a, R)$.
		(ii) $a$ is a **pole of order $k$** iff $c_n = 0$ for $n < -k$ and $c_{-k} \neq 0$; iff $|f(z)| \to \infty$ as $z \to a$.
		(iii) $a$ is **essential** iff infinitely many $c_n$ with $n < 0$ are nonzero; iff $|f|$ has neither a finite limit nor an infinite limit at $a$.
	A function is **meromorphic** on $U$ if its only singularities are poles (no essential, no other types) and these are discrete.

- **[[Thm - Riemann's Removable Singularity Theorem]]**
	- Let $f$ be holomorphic on $D(a, R) \setminus \{a\}$ and bounded near $a$. Then $a$ is removable — $f$ extends holomorphically to $D(a, R)$. The proof: consider $g(z) = (z - a)^2 f(z)$, extended by $g(a) = 0$; show $g$ holomorphic at $a$ (use boundedness of $f$ to verify differentiability), expand in power series around $a$ with leading term order $\geq 2$, factor out $(z-a)^2$ to get the holomorphic extension of $f$.

- **[[Thm - Pole Characterization]]**
	- $a$ is a pole of $f$ if and only if $|f(z)| \to \infty$ as $z \to a$. Equivalently, $1/f$ has a removable singularity at $a$ with $1/f$ extended by $0$. The order of the pole equals the order of the zero of $1/f$ at $a$ (positive integer).

- **[[Thm - Casorati–Weierstrass]]**
	- Let $a$ be an essential singularity of $f$. Then for every $\rho > 0$, the image $f(D(a, \rho) \setminus \{a\})$ is dense in $\mathbb{C}$. The proof is by contradiction: if not dense, then $f$ avoids a disc around some value $w_0$, so $1/(f - w_0)$ is bounded near $a$, hence has a removable singularity, hence $f - w_0 =$ pole or removable — contradicting essential. The much stronger **Great Picard Theorem** (not proved in this chapter) says $f$ takes every complex value with at most one exception infinitely often in every neighborhood of $a$.

- **[[Def - Residue]]**
	- The **residue** of $f$ at an isolated singularity $a$ is $\operatorname{Res}_a f = c_{-1}$, the coefficient of $(z - a)^{-1}$ in the Laurent expansion of $f$ around $a$. Equivalently, $\operatorname{Res}_a f = \frac{1}{2\pi i}\int_{|z - a| = \rho} f(z)\,dz$ for any sufficiently small $\rho > 0$. The residue is the single "obstruction" to $f$ having a primitive on a punctured disc — every other Laurent coefficient is the derivative of a holomorphic function, but $1/(z - a)$ has no primitive on the punctured disc.

- **[[Thm - Residue Theorem]]**
	- Let $f$ be meromorphic on an open $U \subseteq \mathbb{C}$, $\gamma$ a piecewise $C^1$ closed curve in $U$ avoiding the poles of $f$ and null-homotopic in $U$ (or with $U$ simply connected so the condition is automatic). Then $\int_\gamma f\,dz = 2\pi i \sum_{w} I(\gamma; w) \operatorname{Res}_w f$, the sum over poles $w$ of $f$ in $U$. This is the master theorem of contour integration: integrals reduce to local invariants weighted by winding numbers.

- **[[Thm - Computing Residues]]**
	- (i) **Simple pole**: $\operatorname{Res}_a f = \lim_{z \to a}(z - a) f(z)$. (ii) **Pole of order $k$**: $\operatorname{Res}_a f = \frac{1}{(k-1)!} \lim_{z \to a} \frac{d^{k-1}}{dz^{k-1}}[(z - a)^k f(z)]$. (iii) **Ratio of holomorphic functions** $f/g$ with $g$ having a simple zero at $a$ ($g(a) = 0, g'(a) \neq 0$, $f(a) \neq 0$): $\operatorname{Res}_a (f/g) = f(a)/g'(a)$. These formulas avoid computing the full Laurent expansion in most cases.

- **[[Ex - Computing residues at simple poles]]** (⭐)
	- Compute residues of $1/(z^2 - 1)$ at $z = 1, -1$. Factor as $1/((z-1)(z+1))$. By the simple-pole formula, $\operatorname{Res}_{z=1} = 1/(1 + 1) = 1/2$ and $\operatorname{Res}_{z=-1} = 1/(-1 - 1) = -1/2$.

- **[[Ex - Residue at a higher-order pole]]** (⭐⭐)
	- Compute $\operatorname{Res}_{z = 0} (e^z / z^3)$. By the order-3 formula: $\frac{1}{2!}\lim_{z \to 0} (e^z) '' = \frac{1}{2}e^0 = \frac{1}{2}$.

- **[[Ex - Classifying singularities of explicit functions]]** (⭐⭐)
	- Classify the singularities of (a) $1/\sin z$ at $z = 0$ (simple pole, since $\sin z = z + O(z^3)$, residue $1$); (b) $\sin(1/z)$ at $z = 0$ (essential, since $\sin(1/z) = 1/z - 1/(6z^3) + \ldots$ has infinitely many negative powers); (c) $\sin(z)/z$ at $z = 0$ (removable, bounded near $0$, extends to $1$).

> [!note] Exercise Index — §3.3
> [[Exercise Index - §3.3 Laurent and Residues]]

## §3.4 Applications to Real Integrals

- **[[Thm - Real Rational Integrals via Residues]]**
	- For a rational function $P(x)/Q(x)$ with $\deg Q \geq \deg P + 2$ and $Q$ having no real zeros, $\int_{-\infty}^\infty \frac{P(x)}{Q(x)}\,dx = 2\pi i \sum_{\operatorname{Im} w > 0} \operatorname{Res}_w (P/Q)$. The proof: close the real-axis contour by a large upper-semicircle, apply the residue theorem, send the radius to infinity (the semicircle's contribution vanishes by the degree condition + ML estimate).

- **[[Thm - Jordan's Lemma]]**
	- Let $f$ be holomorphic on $\{|z| > R_0\}$ with $|z f(z)| \to 0$ as $|z| \to \infty$ in the upper half plane. Then for any $\alpha > 0$, $\int_{C_R} f(z) e^{i\alpha z}\,dz \to 0$ as $R \to \infty$, where $C_R$ is the upper semicircle $|z| = R, \operatorname{Im} z > 0$. The proof uses the sharp estimate $|e^{i\alpha R e^{i\theta}}| = e^{-\alpha R \sin\theta}$ together with Jordan's inequality $\sin\theta \geq 2\theta/\pi$ on $[0, \pi/2]$.

- **[[Thm - Trigonometric Integrals via Residues]]**
	- For $R(\cos\theta, \sin\theta)$ a rational function with no poles on $S^1$, $\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta = 2\pi i \sum_{|w| < 1} \operatorname{Res}_w \tilde R(z)$ where $\tilde R(z) = \frac{1}{iz} R\left(\frac{z + z^{-1}}{2}, \frac{z - z^{-1}}{2i}\right)$. Substitution $z = e^{i\theta}, dz = iz\,d\theta$ converts the trigonometric integral to a contour integral on $|z| = 1$.

- **[[Ex - Evaluating an integral via residues]]** (⭐⭐)
	- Show $\int_{-\infty}^\infty \frac{dx}{1 + x^2} = \pi$ by residues. Poles at $\pm i$; only $i$ is in the upper half-plane; $\operatorname{Res}_i = 1/(2i)$; integral $= 2\pi i \cdot 1/(2i) = \pi$. Verify the semicircle's contribution vanishes by ML estimate.

- **[[Ex - A trigonometric integral via residues]]** (⭐⭐)
	- Evaluate $\int_0^{2\pi} \frac{d\theta}{5 + 4\cos\theta}$ via the substitution $z = e^{i\theta}$. Convert to a contour integral on $|z| = 1$, identify poles inside, compute residues.

- **[[Ex - Fourier integral via Jordan's lemma]]** (⭐⭐⭐)
	- Evaluate $\int_{-\infty}^\infty \frac{\cos x}{1 + x^2}\,dx$ using residues with $e^{iz}/(1 + z^2)$, the upper semicircle, and Jordan's lemma. Take real parts at the end.

> [!tip] Unlocked: Signal Processing — Transfer functions and stability *(from Linear Systems / EE)*
> The **transfer function** of a linear time-invariant system is a meromorphic function $H(s)$ on $\mathbb{C}$. The **poles of $H$** in the right half-plane (Re $s > 0$) correspond to *unstable* modes (exponentially growing), while poles in the left half-plane are *stable* (decaying). The residue theorem appears in computing the inverse Laplace transform: $f(t) = \frac{1}{2\pi i}\int_{c - i\infty}^{c + i\infty} F(s) e^{st}\,ds = \sum \operatorname{Res}_{s_k}(F(s) e^{st})$, summed over poles. The whole stability and frequency-response theory of signals is a direct application of §3.3–§3.4.

> [!tip] Unlocked: Fluid Dynamics — Complex potential *(from Inviscid Flow)*
> A **2D incompressible irrotational flow** is described by a holomorphic **complex potential** $w(z) = \phi(z) + i\psi(z)$, where $\phi$ is the velocity potential and $\psi$ is the stream function. The complex velocity is $\bar v(z) = w'(z)$. **Simple poles** correspond to *point sources/sinks*; **logarithmic singularities** correspond to *vortices* (with residue = circulation/$2\pi i$); **dipoles** to higher-order singular flows. The **Joukowski transformation** $w = z + 1/z$ maps a circle to an aerofoil shape, used in classical airfoil theory. The whole subject reduces to "find the right holomorphic function on the right domain" — see [[Complex Analysis IV — Mapping Theory and Applications|CA IV]] for conformal mapping.

> [!note] Exercise Index — §3.4
> [[Exercise Index - §3.4 Real Integrals via Residues]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

§3.1–3.4's signature targets are *evaluations*: compute a definite real integral, a contour integral, a residue at a singularity, the sum of a series via integration. These convert analytic problems into algebraic ones (find the poles, compute residues, sum) once the contour deformation is set up.

A second class is *classifications*: given a function with an isolated singularity, identify the type (removable, pole, essential) and the order. This is purely Laurent-series-extraction work.

A third class is *winding-number arguments*: show that a continuous map has a fixed point, an antipode pair, or a specific homotopy class behaviour. The argument principle in [[Complex Analysis IV — Mapping Theory and Applications|CA IV]] is the workhorse for these.

**Sources — What assumptions do we usually leverage?**

Standard hypotheses: (1) *function holomorphic on a punctured disc* — gives a Laurent series, classifies the singularity; (2) *contour bounding a region with finitely many poles* — gives the residue theorem applicability; (3) *function decay on contours at infinity* — gives the vanishing of "side" integrals by ML estimate or Jordan's lemma; (4) *meromorphic on a simply connected domain* — gives that integrals depend only on residues, not on the specific contour.

The pattern is: identify the singularities, identify the contour, verify the decay conditions, sum the residues.

---

# Legal Operations

1. **Identify and classify isolated singularities.** Given an explicit function, locate the punctures and classify each via the Laurent expansion or its surrogate criterion (bounded ⇒ removable; $|f| \to \infty$ ⇒ pole; neither ⇒ essential). *Trigger:* a meromorphic-looking function. *Pattern:* check denominator zeros, expand numerator and denominator in power series near each zero, read off the Laurent leading term.

2. **Compute a residue.** For simple poles, residue = $\lim (z-a)f(z)$ or $f(a)/g'(a)$ for $f/g$. For order-$k$ poles, the $(k-1)$-th derivative trick. For essential singularities, expand the Laurent series and read $c_{-1}$ directly. *Trigger:* applying the residue theorem. *Pattern:* identify pole order, apply the appropriate formula.

3. **Apply the residue theorem.** Sum the residues at all poles inside the closed contour, weighted by winding number, multiplied by $2\pi i$. *Trigger:* a contour integral with isolated singularities. *Pattern:* close the contour if needed, identify enclosed poles, compute residues, sum.

4. **Close a real-axis integral with a semicircle.** For an integral $\int_{-\infty}^\infty f\,dx$ with $f$ decaying suitably, close by a large upper or lower semicircle (choose the half-plane where the integrand decays). The semicircle's integral $\to 0$ by ML estimate or Jordan's lemma. *Trigger:* a real integral that resists direct evaluation. *Pattern:* identify upper- or lower-half-plane poles, residue-sum, take real or imaginary part.

5. **Use Jordan's lemma for oscillatory integrands.** For $\int f(x) e^{i\alpha x}\,dx$ with $f$ rational and decaying, the upper-semicircle contribution vanishes by Jordan. *Trigger:* Fourier-transform-like integral with $e^{i\alpha x}$. *Pattern:* close in the half-plane where $e^{i\alpha z}$ decays ($\operatorname{Im} z > 0$ for $\alpha > 0$).

6. **Substitute $z = e^{i\theta}$ for trigonometric integrals.** Convert $\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta$ into a contour integral on $|z| = 1$ via $\cos\theta = (z + z^{-1})/2, \sin\theta = (z - z^{-1})/(2i), d\theta = dz/(iz)$. *Trigger:* a $2\pi$-periodic integrand. *Pattern:* substitute, identify $|z| = 1$ as the contour, compute residues inside.

7. **Compute winding numbers via the integral formula.** $I(\gamma; w) = \frac{1}{2\pi i}\int_\gamma \frac{dz}{z - w}$ for piecewise $C^1$ $\gamma$. *Trigger:* a topological problem about a curve's winding. *Pattern:* parametrize $\gamma$, compute the integral.

8. **Verify the topology before deforming contours.** Cauchy's theorem allows deformation of contours within a region of holomorphicity, but not across singularities. *Trigger:* deforming or moving a contour. *Pattern:* check the deformation stays within the holomorphic region; if not, account for the residues at crossed singularities.

**Illegal but tempting operations:**

> [!warning] 1. Applying the residue theorem to non-isolated singularities
> The residue theorem requires *isolated* singularities. Branch cuts (continuous singularities), cluster points of poles, and natural boundaries are not isolated and require different techniques (keyhole contours, summation methods). When in doubt, check that the function is meromorphic — that singularities are discrete points where the Laurent expansion is well-defined.

> [!warning] 2. Forgetting the orientation of the contour
> The residue theorem assumes the contour is traversed *counterclockwise* (positive orientation). A clockwise contour gives the *negative* of the residue sum. When in doubt, check the winding number direction; or use $I(\gamma; w)$ explicitly to track orientation.

> [!warning] 3. Confusing residue at infinity with residue at zero
> The residue of $f$ at $\infty$ is $\operatorname{Res}_\infty f = -\operatorname{Res}_0 \frac{1}{z^2} f(1/z)$, which is different from $\operatorname{Res}_0 f$. The negative sign comes from the orientation of large circles around $\infty$. For applications, the rule "sum of all residues on $\hat{\mathbb{C}}$ equals zero" is the cleanest form.

> [!warning] 4. Assuming Jordan's lemma applies for non-oscillatory decay
> Jordan's lemma works because $e^{i\alpha z}$ has *exponential* decay in $\operatorname{Im} z > 0$ (for $\alpha > 0$). It does *not* apply to $e^{-\alpha z}$ on closed upper semicircles (which grows!). For unilateral integrals or Laplace-type transforms, different contour choices (e.g., the Bromwich contour) are needed.

---

# Problem-Solving Strategy

Problems in §3.1–§3.4 cluster into four families. The first is **classifying isolated singularities** of an explicit meromorphic-looking function. The systematic recipe: identify the punctures (where the function fails to be holomorphic), expand in Laurent series near each, read off the negative-power terms. For most "$P(z)/Q(z)$"-style functions, the singularities are zeros of $Q$, and the order of a pole equals the order of the zero of $Q$ minus the order of the zero of $P$ (with negative meaning removable).

The second is **computing residues**. For simple poles of $P/Q$ with $Q(a) = 0, Q'(a) \neq 0$, the formula $P(a)/Q'(a)$ is the cleanest. For higher-order poles, the $(k-1)$-th derivative formula works but is computationally heavy; often easier to expand the numerator in power series, divide by $(z - a)^k$, and read off the coefficient of $(z - a)^{-1}$.

The third is **evaluating contour integrals**. For closed contours in simply connected domains avoiding singularities, the integral is $0$ (Cauchy). For closed contours enclosing poles, apply residues. For unbounded contours (extending real-axis integrals), close with semicircles or rectangles and verify the side-integral contributions vanish.

The fourth is **evaluating real integrals** by extending to a complex contour. The recipe: identify a meromorphic complex extension; choose a contour that gives the desired real integral as one part; close the contour to enclose a finite number of poles; verify the other parts vanish in the limit; equate the real (or imaginary) part to the sum of residues.

A non-obvious general principle: **the choice of contour is the art**. A real-axis integral can be closed by a semicircle, a rectangle, a keyhole, or a more exotic shape — and the right choice depends on (a) where the singularities of the integrand lie, (b) where the integrand decays at infinity, (c) what other "side" contributions are tractable to evaluate or to vanish. Building intuition for this is the substance of the subject, and the keyhole contour for $\int_0^\infty x^\alpha f(x)\,dx$, the rectangular contour for $\int e^{ax}/\cosh(x)\,dx$, the Pochhammer contour for $\int_0^1 x^a(1-x)^b\,dx$, are all classical examples that appear in [[Complex Analysis IV — Mapping Theory and Applications|CA IV]].

---

# Most Reusable Properties

- **[[Thm - Residue Theorem|Residue theorem]]**: $\int_\gamma f\,dz = 2\pi i \sum_w I(\gamma; w) \operatorname{Res}_w f$. The single most-used result in evaluating contour integrals; reduces a global integral to a finite sum of local data weighted by topology. Recognize it whenever a contour integral has isolated singularities.

- **[[Thm - Laurent Series Theorem|Laurent expansion]]**: Every function holomorphic on an annulus has a unique two-sided power series expansion converging there. This is the foundational structure of singularity analysis — every other result in this chapter is downstream of "expand in Laurent series and read off the coefficients".

- **[[Thm - Riemann's Removable Singularity Theorem|Removable singularity criterion]]**: bounded near a puncture ⇒ removable. The cleanest criterion for "the puncture doesn't really matter" and the standard tool for upgrading a holomorphic-on-punctured-disc statement to a holomorphic-on-disc statement.

- **[[Thm - Casorati–Weierstrass]]**: image near an essential singularity is dense in $\mathbb{C}$. The starting tool for "the singularity is genuinely wild", and the seed of Picard's theorem (every value with at most one exception is hit infinitely often).

- **[[Thm - Computing Residues|Residue formulas]]**: $\operatorname{Res}_a(f/g) = f(a)/g'(a)$ for simple poles of $f/g$; the $(k-1)$-th derivative formula for higher-order poles. These collapse residue computations to elementary calculus.

---

# Bridges

1. **Topology — Winding number and the fundamental group.** The winding number $I(\gamma; w)$ is the class of $\gamma$ in $\pi_1(\mathbb{C} \setminus \{w\}) = \mathbb{Z}$, the fundamental group of the punctured plane. The integral formula computes this purely homotopical invariant by an analytic procedure — a classical bridge between [[Topology IV — §13–17 Quotients, Homotopy, Topological Groups, Baire|topology]] and complex analysis. The residue theorem then evaluates contour integrals using this homotopy class, completing the bridge.

2. **Algebraic Topology — De Rham cohomology and integration.** Cauchy's theorem in its general form (closed integrals depend only on homotopy class) says that the holomorphic 1-form $f(z)\,dz$ on a punctured plane is closed but not exact, and its de Rham cohomology class is detected by its periods (integrals around generating loops). For meromorphic functions, the residues at each pole are the "periods" and the residue theorem is the pairing between $H^1$ (homology of loops) and $H_1$ (cohomology of forms). This is the seed of all of complex algebraic geometry and Riemann surface theory.

3. **Signal Processing — Laplace and Z-transforms.** The **Laplace transform** $F(s) = \int_0^\infty f(t) e^{-st}\,dt$ extends a function on $[0, \infty)$ to a holomorphic function on a half-plane $\operatorname{Re} s > c$. The inverse is the Bromwich integral $f(t) = \frac{1}{2\pi i}\int_{c - i\infty}^{c + i\infty} F(s) e^{st}\,ds$, evaluable by residues (closing to a left semicircle). The **Z-transform** is the discrete analog: $X(z) = \sum_{n=0}^\infty x_n z^{-n}$, a Laurent-series-like object. Poles of $X$ inside the unit disc correspond to unstable modes, on the unit disc to marginal, outside to stable. The whole stability theory of linear systems is the complex analysis of §3.3–§3.4.

4. **Fluid Dynamics — Complex potential and the Joukowski transformation.** A 2D incompressible irrotational fluid flow has a complex potential $w(z) = \phi(z) + i\psi(z)$, holomorphic in the flow region. The velocity is $\bar v = w'(z)$. Singularities have physical meaning: a simple pole is a *source* (mass added) or *sink* (mass removed); a logarithmic singularity is a *vortex* (circulation); a dipole is a pair of source/sink at vanishing distance. The Kutta–Joukowski theorem relating circulation to lift, the aerofoil theory of Joukowski, the Schwarz–Christoffel mapping for polygonal domains — all use §3 complex analysis directly. The conformal mapping techniques of [[Complex Analysis IV — Mapping Theory and Applications|CA IV]] are the modern continuation.

5. **Number Theory — Riemann zeta function and the explicit formula.** (Skipped per user instructions, but worth noting in passing for the bigger picture.) The Riemann zeta function $\zeta(s) = \sum 1/n^s$ extends meromorphically to all of $\mathbb{C}$ with a single simple pole at $s = 1$; its zeros encode the distribution of primes. The proof uses contour integration and the residue theorem applied to integrals like $\int \zeta'/\zeta \cdot x^s/s\,ds$ — Riemann's explicit formula. Number theory thus depends on §3.3–§3.4 in a very direct way. We do not develop this here per the topic's scope.

---

# Insights

The **unifying frame** of §3.1–§3.4 is that *meromorphic functions are determined by their residues plus a holomorphic correction*. A meromorphic function on $\mathbb{C}$ with finitely many poles equals $\sum_a R_a(z) + h(z)$ where $R_a$ is the principal part at $a$ (a rational function with pole only at $a$) and $h$ is entire. The full data of the function — up to entire correction — is encoded in finite local data (residues and higher-order principal-part coefficients). This is the seed of every "expansion in poles" theorem, the Mittag-Leffler theorem, partial fraction expansion, the Weierstrass factorization theorem.

The **true name** of "residue" is "the obstruction to being a derivative". A function $f$ holomorphic on a punctured disc $D(a, R) \setminus \{a\}$ has a primitive there iff its residue at $a$ vanishes. The non-primitive content is exactly the residue, and the integral $\int_\gamma f\,dz$ around a loop around $a$ picks up exactly $2\pi i \cdot \operatorname{Res}_a f$ — no other Laurent coefficient contributes. Residues are the *cohomological* data of meromorphic differentials, and the residue theorem is the *period pairing*.

A **trigger-reaction pattern** that becomes second nature: when faced with a real integral that resists direct evaluation, ask "does the integrand extend holomorphically to a domain in $\mathbb{C}$ where I can close the contour?" If yes, identify the poles enclosed, compute residues, verify decay on the closing contour, write the answer. This pattern handles probably 80% of "compute this integral" exercises in a graduate analysis course, and the only variation is the choice of contour.

An **inheritance observation**: the residue of $f$ at a simple pole $a$ is the *local derivative* of $z \mapsto (z - a) f(z)$ evaluated at $a$. The order-$k$ pole formula generalizes this to a higher derivative. So residues are inherited from the *Taylor series of the regularization* — the local power series of the function with the pole "stripped out" by multiplication by $(z - a)^k$.

A final structural observation: §3.3–§3.4 give complex analysis its *computational power*. Up through §2, the theorems are mostly *structural* — rigidity, identity, maximum modulus. With §3, complex analysis becomes a *computational engine*: real integrals, infinite sums, generating functions, characteristic functions, transfer functions, all become tractable through the residue theorem and its accompanying contour-integration techniques. The shift from §2 to §3 is the shift from theorem-proving to problem-solving, and the residue theorem is the universal tool of that shift.
