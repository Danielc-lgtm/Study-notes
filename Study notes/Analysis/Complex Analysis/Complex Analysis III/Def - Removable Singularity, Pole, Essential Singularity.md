---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Isolated Singularity"
  - "Def - Laurent Series"
tags: [analysis, complex-analysis]
---

# Notation

Throughout, $a \in \mathbb{C}$ is an isolated singularity of $f$, meaning $f$ is holomorphic on a punctured disc $D(a, R) \setminus \{a\}$ for some $R > 0$. The Laurent expansion around $a$ is $f(z) = \sum_{n=-\infty}^\infty c_n (z - a)^n$. The integer $k$ denotes the order of a pole. The full registry lives on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Axiom Motivation

Once we know $f$ is holomorphic on a punctured disc and has a Laurent expansion there, we ask: what kind of singularity does $f$ have at the puncture? The classification has to be a *complete trichotomy* — every isolated singularity falls into exactly one of a small number of buckets — and the buckets have to be *meaningful*: each one should correspond to a specific qualitative behaviour of $f$ near the puncture.

The Laurent expansion provides the dividing line. The negative-power part $\sum_{n \geq 1} c_{-n}(z - a)^{-n}$ — the *principal part* — encodes the singular behaviour. The size of this part dictates how badly $f$ behaves at $a$.

Three cases, distinguished by the number of nonzero $c_{-n}$ for $n \geq 1$:

**Zero nonzero negative coefficients.** The principal part is identically zero, so the Laurent series reduces to a power series. It defines a holomorphic function on the full disc $D(a, R)$, including the centre. The original $f$ might not have been defined at $a$, or might have been defined to some other value, but the Laurent expansion at $a$ gives a unique consistent value. The singularity was *not really there* — it was an artifact of how $f$ was defined, and the function extends holomorphically. This is the **removable** case. The typical example is $(\sin z)/z$ at $z = 0$: the formula seems to blow up, but the Laurent expansion is just $1 - z^2/6 + \ldots$.

**Finitely many, with a largest negative power $-k$ for some $k \geq 1$.** The principal part is a finite sum $c_{-k}(z - a)^{-k} + \ldots + c_{-1}(z - a)^{-1}$. As $z \to a$, the dominant term is $c_{-k}(z - a)^{-k}$, which blows up like $(z - a)^{-k}$. So $|f(z)| \to \infty$ as $z \to a$. The function $g(z) = (z - a)^k f(z)$ has a removable singularity at $a$ with nonzero value $c_{-k}$ — multiplying by $(z - a)^k$ shifts the Laurent series so that the most-negative term becomes constant. This is the **pole of order $k$** case. The typical example is $1/(z - a)^k$.

**Infinitely many nonzero negative coefficients.** The principal part has infinitely many terms, and the qualitative behaviour of $f$ near $a$ is wild. No multiplication by $(z - a)^k$ for any finite $k$ removes all negative powers — the principal part is genuinely infinite-dimensional. As $z$ approaches $a$, $|f(z)|$ neither tends to a finite limit (which would make it removable, by the Riemann theorem) nor tends to infinity (which would make it a pole). Instead, $|f|$ oscillates: in every punctured neighborhood, $f$ takes values arbitrarily close to every complex number (Casorati–Weierstrass), and in fact takes every complex value with at most one exception infinitely often (Picard). This is the **essential** case. The typical example is $e^{1/z}$ at $z = 0$.

Why these three buckets and not others? Because the Laurent expansion provides a complete invariant of the singularity type, and the only natural distinctions are "how many nonzero negative coefficients?" with three meaningful answers: zero (removable), positive-finite (pole), or infinite (essential). Each bucket has a clean characterization in terms of $|f|$ behaviour ($|f|$ bounded vs $|f| \to \infty$ vs neither), and each one has its own theory and computational technique.

The compound nature of this definition reflects the fact that the three cases are *parallel* — they share a common framework (the Laurent expansion at an isolated singularity) and are distinguished only by where in the framework they sit. Defining them separately would obscure the unity of the trichotomy; defining them together makes the structure visible.

---

# The Definition

Let $a \in \mathbb{C}$ be an isolated singularity of $f$, with Laurent expansion $f(z) = \sum_{n=-\infty}^\infty c_n (z - a)^n$ on $D(a, R) \setminus \{a\}$.

**(i) Removable singularity.** $a$ is a **removable singularity** of $f$ if $c_n = 0$ for all $n < 0$. Equivalently, the Laurent series is a power series, and $f$ extends holomorphically to $D(a, R)$ by setting $f(a) = c_0$. Equivalent characterizations:
- $f$ is bounded on some punctured disc around $a$ (Riemann's criterion);
- $(z - a)f(z) \to 0$ as $z \to a$;
- $f$ has a holomorphic extension to $a$.

**(ii) Pole of order $k$** (for some integer $k \geq 1$). $a$ is a **pole of order $k$** of $f$ if $c_{-k} \neq 0$ and $c_n = 0$ for all $n < -k$. Equivalent characterizations:
- $f(z) = (z - a)^{-k} g(z)$ for some $g$ holomorphic on $D(a, R)$ with $g(a) \neq 0$;
- $|f(z)| \to \infty$ as $z \to a$ (any-order pole) and $(z - a)^k f(z)$ has a removable singularity at $a$ with nonzero value;
- $1/f$ extends holomorphically to $a$ with a zero of order exactly $k$.

A pole of order $1$ is called a **simple pole**; of order $2$, a **double pole**; etc.

**(iii) Essential singularity.** $a$ is an **essential singularity** of $f$ if infinitely many $c_n$ with $n < 0$ are nonzero. Equivalent characterizations:
- $|f|$ has neither a finite limit nor an infinite limit as $z \to a$;
- $f(D(a, \rho) \setminus \{a\})$ is dense in $\mathbb{C}$ for every $\rho > 0$ ([[Thm - Casorati–Weierstrass|Casorati–Weierstrass]]);
- $f$ takes every value in $\mathbb{C}$ except at most one infinitely often in every punctured neighborhood (Great Picard, beyond IB scope).

**Meromorphic.** $f$ is **meromorphic** on an open $U$ if $f$ is holomorphic on $U$ except at a discrete set of poles (no essential singularities, and the singular set has no accumulation point in $U$).

---

# Relate to Other Fields / Compression

The trichotomy is the **algebraic analog of decomposing a Laurent ring**. In the field $\mathbb{C}((z - a))$ of formal Laurent series with finitely many negative terms, every element is either in $\mathbb{C}[[z - a]]$ (removable, holomorphic at $a$) or has a finite pole (in $z^{-k}\mathbb{C}[[z - a]]$ for some $k \geq 1$). The complex-analytic version adds a third class — the infinite-tailed Laurent series — that has no algebraic analog because algebraic Laurent series are by convention finitely-tailed.

In **algebraic geometry**, a meromorphic function on a Riemann surface is a holomorphic map to the Riemann sphere $\hat{\mathbb{C}}$. The classification of singularities corresponds to: removable = honest map to $\mathbb{C}$; pole = honest map to $\hat{\mathbb{C}}$ (sending pole to $\infty$); essential = no algebraic extension. The "Riemann sphere as one-point compactification of $\mathbb{C}$" exists precisely because poles are removable in $\hat{\mathbb{C}}$.

In **fluid dynamics**, the three types of singularities of the complex potential have direct physical meaning: removable = no singularity, just a regular flow point; pole = source/sink (simple) or dipole (higher order); essential = no clean physical analog (which is why physical models rarely encounter essential singularities). The **logarithmic singularity** $\log(z - a)$ — corresponding to a vortex — is neither pole nor essential in this trichotomy, because $\log$ is multi-valued, not a single-valued holomorphic function with an isolated singularity in our sense.

In **signal processing**, a transfer function's poles correspond to resonant modes (frequencies of natural oscillation). The pole order corresponds to the multiplicity of the mode. Essential singularities do not appear in finite-order linear systems and are physically unusual.

---

# Examples / Corollaries

**Removable — $(\sin z)/z$ at $z = 0$.** Laurent expansion $1 - z^2/6 + z^4/120 - \ldots$ has no negative-power terms. Setting the value at $0$ to be $1$ gives a holomorphic extension. The function $f(z) = (e^z - 1)/z$ at $z = 0$ is another instance.

**Removable — bounded near $0$.** Suppose $f$ is holomorphic on $\{0 < |z| < 1\}$ and $|f(z)| \leq M$ for all such $z$. By Riemann's criterion, $z = 0$ is removable. The Laurent coefficient bound $|c_{-n}| \leq M \rho^n$ for arbitrarily small $\rho$ forces $c_{-n} = 0$ for all $n \geq 1$.

**Simple pole — $1/(z - a)$ at $z = a$.** Laurent expansion is just $1/(z - a)$, so $c_{-1} = 1$, all other $c_n = 0$. Residue $= 1$. Generically, $f(z) = g(z)/(z - a)$ with $g$ holomorphic and $g(a) \neq 0$ has a simple pole at $a$ with residue $g(a)$.

**Double pole — $1/(z - a)^2$ at $z = a$.** Pole of order $2$, residue $= 0$ (the coefficient of $(z - a)^{-1}$ is zero in this Laurent expansion). This shows that *higher-order poles can have residue zero* — the residue is just one Laurent coefficient, not the whole singular behaviour.

**Pole of order $k$ — $1/\sin^k(z)$ at $z = 0$.** Near $0$, $\sin z = z(1 - z^2/6 + \ldots)$, so $\sin^k z = z^k(1 + O(z^2))$, hence $1/\sin^k(z) = (1/z^k)(1 + O(z^2))$. A pole of order $k$ with leading principal-part coefficient $1$.

**Essential — $e^{1/z}$ at $z = 0$.** $e^{1/z} = \sum_{n=0}^\infty z^{-n}/n!$, infinitely many negative-power terms. $|e^{1/z}|$ takes every positive value (and behaves wildly) as $z \to 0$: on the positive real axis approaching $0$, $|e^{1/z}| \to \infty$; on the negative real axis, $|e^{1/z}| \to 0$. Casorati–Weierstrass: $e^{1/z}$ takes values arbitrarily close to every complex number in every punctured neighborhood of $0$. (Great Picard: $e^{1/z}$ takes every value except $0$ infinitely often in every neighborhood.)

**Essential — $\sin(1/z)$ at $z = 0$.** Laurent expansion $\sin(1/z) = 1/z - 1/(3!z^3) + 1/(5!z^5) - \ldots$, infinitely many odd-power negative terms. Same wild behaviour.

**Is NOT an instance of any singularity type — $\log z$ at $z = 0$.** Not isolated (branch cut), so the classification does not apply. The "singularity" of $\log z$ at $0$ is a *branch point*, a different phenomenon requiring Riemann surface theory.

**Calibration check — residue at a simple pole.** For a simple pole at $a$, $\operatorname{Res}_a f = \lim_{z \to a}(z - a) f(z)$. For $1/(z^2 + 1)$ at $z = i$: $\lim_{z \to i}(z - i)/(z^2 + 1) = \lim_{z \to i} 1/(z + i) = 1/(2i)$.

**Calibration check — order of a pole from $1/f$.** If $g = 1/f$ has a zero of order $k$ at $a$ (so $g(z) = (z - a)^k h(z)$ with $h(a) \neq 0$), then $f$ has a pole of order $k$ at $a$.

**Corollary — meromorphic functions on $\mathbb{C}$ are quotients of holomorphic ones.** Any meromorphic $f$ on a domain $U$ is locally of the form $f(z) = g(z)/(z - a)^k$ with $g$ holomorphic and $g(a) \neq 0$ near each pole $a$. Globally, on the Riemann sphere $\hat{\mathbb{C}}$, every meromorphic function is a rational function $P(z)/Q(z)$.

**Corollary — Picard's theorem and the difference between pole and essential.** A pole at $a$: $f$ takes the value $\infty$ "approximately once" — exactly $k$ times if counted with multiplicity in $\hat{\mathbb{C}}$, in the sense that the equation $f(z) = w$ has $k$ solutions near $a$ for $w$ near $\infty$. An essential singularity at $a$: $f$ takes every value in $\mathbb{C}$ (except at most one) *infinitely often* in every punctured neighborhood. The qualitative gap is enormous.

---

# Unlocked by This

> [!tip] Riemann's Removable Singularity Theorem *(from §3.3)*
> The bounded ⇒ removable characterization, [[Thm - Riemann's Removable Singularity Theorem|Riemann's theorem]], is the cleanest criterion for "this singularity doesn't really exist".

> [!tip] Pole Characterization *(from §3.3)*
> The $|f| \to \infty$ ⟺ pole characterization is [[Thm - Pole Characterization|pole characterization]]; it provides a clean computational test for poleness without expanding the Laurent series.

> [!tip] Casorati–Weierstrass *(from §3.3)*
> The density-of-image characterization is [[Thm - Casorati–Weierstrass|Casorati–Weierstrass]]; it is the first qualitative theorem about wild singular behaviour.

> [!tip] Residue and the Residue Theorem *(from §3.3)*
> The single coefficient $c_{-1}$ — the [[Def - Residue|residue]] — is the only Laurent coefficient that survives contour integration; the [[Thm - Residue Theorem|residue theorem]] is built on this.
