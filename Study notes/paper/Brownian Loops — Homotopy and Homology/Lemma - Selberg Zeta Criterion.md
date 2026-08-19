---
type: lemma
subject: probability-geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Def - The Loop-Length Integral"
  - "Thm - Mass of a Subordinate Brownian Loop Class"
tags: [paper, brownian-loops, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Lemma 4.2"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ — a geometrically finite hyperbolic surface (the quotient of the upper half-plane by a discrete isometry group $\Gamma$).
- $\mathcal P_X$ — the set of primitive oriented closed geodesics of $X$; each $\gamma \in \mathcal P_X$ has a definite length $\ell_\gamma > 0$.
- $\tau \in \Gamma$ — a primitive hyperbolic element representing $\gamma$; in standard coordinates $\tau : z \mapsto e^{\ell_\gamma} z$.
- $m \ge 1$ — the winding number of a loop around $\gamma$; the total translation length is $L := m\ell_\gamma > 0$.
- $C_X(\gamma^m)$ — the free homotopy class of loops on $X$ that wind $m$ times around $\gamma$.
- $\phi : (0,\infty) \to (0,\infty)$ — a Bernstein function (Assumption 2.3 of the paper); it drives a subordinated Brownian motion on $\mathbb H^2$.
- $I_\phi(L)$ — the loop-length integral $\int_0^\infty \frac{e^{-s/4} e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds)$, a positive real-valued function of $L$.
- $\mu^\phi_X$ — the $\phi$-subordinate loop measure on $X$; $\mu^\phi_X(C_X(\gamma^m))$ is the mass of the class $C_X(\gamma^m)$.
- $s \in \mathbb R$ — the **spectral/zeta variable**, ranging over reals with $s > \delta$. (This $s$ is unrelated to the subordination internal-clock variable in $I_\phi$; both letters are traditional in their own contexts.)
- $\delta \in (0, 1]$ — the critical exponent of $\Gamma$.
- $Z_X(s) := \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ — the Selberg zeta function, convergent for $s > \delta$.
- $C > 0$ — a real positive constant.

> [!recall]- Hyperbolic surface $X = \Gamma\backslash\mathbb H^2$
> **Formally:** $\mathbb H^2 = \{x + iy \in \mathbb C : y > 0\}$ with the Riemannian metric $ds^2 = (dx^2 + dy^2)/y^2$; its isometry group is $\mathrm{PSL}(2, \mathbb R)$ acting by Möbius transformations. A **Fuchsian group** $\Gamma \subset \mathrm{PSL}(2, \mathbb R)$ is a discrete subgroup; assumed torsion-free, its action on $\mathbb H^2$ is fixed-point-free, and the quotient $X = \Gamma\backslash\mathbb H^2$ (identify $z, hz$ for every $h \in \Gamma$) is a smooth surface inheriting the hyperbolic metric.
> **In words:** the upper half-plane, given a curved ruler so that distance shrinks near the real axis. Pick a discrete group of rigid motions with no fixed points, glue together points that a motion moves between; the result is a curved surface with a nontrivial global shape (handles, holes, cusps) but the same local geometry as $\mathbb H^2$.
> **Concretely:** the Euclidean analogue is the flat torus $T^2 = \mathbb R^2 / \mathbb Z^2$: take $\Gamma = \mathbb Z^2$ acting by integer translations; the quotient is a unit square with opposite edges glued. In the hyperbolic setting, a genus-2 surface (two-holed pretzel) is $\Gamma\backslash\mathbb H^2$ for a specific 4-generator Fuchsian $\Gamma$. Full detail: [[Def - Fuchsian Group and the Hyperbolic Quotient Surface]].

> [!recall]- Primitive closed geodesic $\gamma$ and its length $\ell_\gamma$
> **Formally:** an element $\tau \in \mathrm{PSL}(2, \mathbb R)$ is **hyperbolic** if it is conjugate to $\tau_0 : z \mapsto e^\ell z$ for some $\ell > 0$; the number $\ell$ is $\tau$'s **translation length** — the hyperbolic distance $\tau$ moves points along its invariant geodesic (its **axis**). $\tau \in \Gamma$ is **primitive** if $\tau \ne \sigma^k$ for any $\sigma \in \Gamma$ and $k \ge 2$. Every non-trivial, non-peripheral free homotopy class on $X = \Gamma\backslash\mathbb H^2$ contains a unique closed geodesic $\gamma$, of length $\ell_\gamma$ equal to the translation length of a primitive hyperbolic $\tau$ representing that class; $\tau^m$ represents the class of $\gamma$ traversed $m$ times.
> **In words:** hyperbolic elements are the "translations along a specific line" among the isometries of $\mathbb H^2$: pick a geodesic, slide everything along it by a fixed distance. Primitive means "not a proper power of anything else." On the surface, every loop that genuinely wraps around at least one hole (not through a cusp) is homotopic to a unique shortest curve — a closed geodesic — of a definite length $\ell_\gamma$; iterating the loop $m$ times traces the geodesic $m$ times.
> **Concretely:** with $\tau_0 : z \mapsto e^\ell z$ acting on $\mathbb H^2$, the axis is the imaginary half-line, and the distance from $i$ to $\tau_0(i) = e^\ell i$ along it is $\int_1^{e^\ell} dy/y = \ell$; so $\tau_0$ slides points along the axis by exactly $\ell$. The quotient $\langle\tau_0\rangle\backslash\mathbb H^2$ is a cylinder, and the axis projects to a closed geodesic of length $\ell$ on it. Full detail: [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length]].

> [!recall]- Free homotopy class $C_X(\gamma^m)$ and winding number $m$
> **Formally:** two oriented closed loops on $X$ are **freely homotopic** if one deforms continuously into the other on $X$ with the basepoint allowed to move; the equivalence classes are **free homotopy classes**. For $\gamma \in \mathcal P_X$ a primitive closed geodesic with hyperbolic representative $\tau \in \Gamma$, the class $C_X(\gamma^m)$ consists of all loops freely homotopic to "$\gamma$ traversed $m$ times", and corresponds to the conjugacy class $[\tau^m]_{\mathrm{conj}} = \{q \tau^m q^{-1} : q \in \Gamma\}$ in $\Gamma$.
> **In words:** two loops are freely homotopic when you can deform one into the other on the surface — sliding the starting point freely; they "go around the same holes in the same pattern." The class $C_X(\gamma^m)$ is the topological type "wind around this specific geodesic $\gamma$ exactly $m$ times."
> **Concretely:** on the torus $T^2 = \mathbb R^2/\mathbb Z^2$, $\Gamma = \mathbb Z^2$ is abelian; free homotopy classes are in bijection with $\mathbb Z^2$ itself — the pair $(a, b)$ labels "$a$ times horizontally, $b$ times vertically." Iterating a primitive class $(1, 0)$ gives $(m, 0)$, the winding-$m$ class of that geodesic. On a hyperbolic surface, $\Gamma$ is non-abelian, so a class is a genuine equivalence class of many group elements, but the picture — one class per topological type — is the same.

> [!recall]- Loop-length integral $I_\phi(L)$ and the class-mass factorisation
> **Formally:** for a Bernstein function $\phi$ with weighted potential measure $V_\phi$ on $(0, \infty)$, and $L > 0$, $I_\phi(L) := \int_0^\infty \frac{e^{-s/4} e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds)$. [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] then states that for a primitive closed geodesic $\gamma$ of length $\ell_\gamma$ and $m \ge 1$, with $L = m\ell_\gamma$, the class-mass factors as $\mu^\phi_X(C_X(\gamma^m)) = \frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)$.
> **In words:** collect every piece of the class-mass that depends on the driving process $\phi$ into one 1-D integral in a dummy variable $s$; call it $I_\phi(L)$. The class-mass then splits cleanly into a **geometric prefactor** $\ell_\gamma/[2\sinh(L/2)]$ and this **process integral** $I_\phi(L)$. That factorisation is exactly the input of the lemma below.
> **Concretely:** for Brownian motion ($\phi(\lambda) = \lambda$, $V_\phi(ds) = ds/s$), $I_\phi(L) = e^{-L/2}/L$; at $L = 1$, $I_\phi(1) = e^{-1/2} \approx 0.607$ and the class-mass is $\ell_\gamma \cdot e^{-1/2}/[L \cdot 2\sinh(1/2)] = 1/(e - 1) \approx 0.582$. Full detail: [[Def - The Loop-Length Integral]].

> [!recall]- Selberg zeta function $Z_X(s)$ and critical exponent $\delta$
> **Formally:** for a hyperbolic surface $X$ with primitive closed geodesics $\mathcal P_X$ of lengths $\{\ell_\gamma\}$, the **Selberg zeta function** is $Z_X(s) := \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ for $\operatorname{Re} s > \delta$; its logarithm expands as $-\log Z_X(s) = \sum_{\gamma}\sum_{m \ge 1}\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$. The **critical exponent** $\delta$ is the infimum of $s > 0$ for which the orbit series $\sum_{h \in \Gamma} e^{-s\,d(z, hz)}$ converges (independent of $z$): it measures how fast the group orbit $\Gamma z$ spreads out. Finite area $\Rightarrow \delta = 1$; infinite area $\Rightarrow \delta < 1$.
> **In words:** a product with one factor per closed geodesic $\gamma$ and per non-negative integer $k$, of a simple exponential shape — the *generating function of the length spectrum* of $X$. Its log expands as a double sum indexed by "geodesic $\gamma$ traversed $m$ times," and it is precisely this log-expansion that the lemma below turns into a formula for the total loop mass. $\delta$ is a single number that measures how fast closed geodesics multiply.
> **Concretely:** for a single-generator toy $\Gamma = \langle \tau_0 : z \mapsto e^\ell z \rangle$ (an infinite cylinder with one closed geodesic of length $\ell$), $Z_X(s) = \prod_{k \ge 0}(1 - e^{-(s+k)\ell})$; at $s = 1$, $\ell = 1$: $Z_X(1) = (1 - e^{-1})(1 - e^{-2})\cdots \approx 0.632 \cdot 0.865 \cdot 0.950 \cdots \approx 0.521$. On a finite-area surface, $\delta = 1$; at $s = 1$ (the edge), $-\log Z_X(1) = +\infty$ and the total loop mass diverges. Full detail: [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

---

# Statement

> **Lemma (Selberg zeta criterion; Belyaev–Huseynli 4.2).** Let $X = \Gamma\backslash\mathbb H^2$ be a geometrically finite hyperbolic surface with critical exponent $\delta$, and $\phi$ a Bernstein function driving a loop measure $\mu^\phi_X$. Suppose there exist constants $C > 0$ and $s \in \mathbb R$ with $s > \delta$, independent of $L$, such that
> $$\frac{L}{2\sinh(L/2)}\,I_\phi(L) \;=\; C \cdot \frac{e^{(1-s)L}}{e^L - 1} \qquad (L > 0).$$
> Then, summing over primitive geodesics $\gamma \in \mathcal P_X$ and winding numbers $m \ge 1$,
> $$\sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^{\infty} \mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; -C\log Z_X(s).$$

---

# In One Line

Whenever the process-integral $I_\phi(L)$ combines with the geometric prefactor to give a class-mass of the *canonical shape* $e^{(1-s)L}/(e^L - 1)$, summing over all non-trivial non-peripheral topological types collapses to $-C \log Z_X(s)$ — the log of the Selberg zeta at that same $s$. This is the master identity of §4: it converts a random-loop sum into a value of a classical spectral generating function.

---

# Why It's True

**Mechanism (one sentence).** *The hypothesis is engineered so that each summand $\mu^\phi_X(C_X(\gamma^m))$ equals $C/m$ times the exact term in the log-expansion of $Z_X(s)$ at frequency $(\gamma, m)$; summing reassembles $-C\log Z_X(s)$ term by term.*

The lemma is a **shape-matching identity**, not a deep theorem. Its role is to isolate the analytic content of the paper's zeta identities: whether a specific process (Brownian, killed, $\alpha$-stable, shifted stable) gives a total mass expressible as $-\log Z_X$ reduces to whether its $I_\phi$ has this canonical shape — a one-line check per process, done in §4.1.1 and §4.1.2. The generating function $Z_X(s)$ is the natural home for the sum because its very *definition* is designed to package the length spectrum $\{\ell_\gamma\}$ into a product; the log-expansion of that product is exactly the double sum over "geodesic traversed $m$ times."

The hypothesis $s > \delta$ is what makes the double sum absolutely convergent (the Selberg product converges only in that half-plane); without it, the rearrangement of terms below is not licensed.

---

# Proof

> [!note]- Gap-free proof of Lemma 4.2
> **Step 1 — rewrite one class-mass via Theorem 3.5.** By [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]], writing $L = m\ell_\gamma$ (so $\ell_\gamma/L = 1/m$),
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L) \;=\; \frac{1}{m}\cdot\frac{L}{2\sinh(L/2)}\,I_\phi(L).$$
> The second equality inserts $\ell_\gamma = L/m$ and pulls the $1/m$ outside.
>
> **Step 2 — apply the shape hypothesis.** By hypothesis, $\frac{L}{2\sinh(L/2)}\,I_\phi(L) = C\cdot e^{(1-s)L}/(e^L - 1)$ for every $L > 0$; in particular for every $L$ of the form $m\ell_\gamma$. Substituting into Step 1,
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; \frac{C}{m}\cdot\frac{e^{(1-s)L}}{e^L - 1} \;=\; \frac{C}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}.$$
>
> **Step 3 — sum over primitive geodesics and winding numbers.** Every $\mu^\phi_X(C_X(\gamma^m)) \ge 0$ (it is a mass), and $C > 0$, so every term in the double sum is non-negative. Tonelli's theorem then allows any order of summation. Summing over $\gamma \in \mathcal P_X$ and $m \ge 1$,
> $$\sum_{\gamma}\sum_{m \ge 1}\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; C\sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^{\infty}\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}.$$
>
> **Step 4 — recognise $-\log Z_X(s)$.** The right-hand double sum is exactly the log-expansion of the Selberg zeta at $s$: from the recall above (or [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]]),
> $$-\log Z_X(s) \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^{\infty}\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1} \qquad (s > \delta).$$
> The absolute convergence of this series in the region $s > \delta$ is the defining feature of $\delta$ (the exponent of convergence of the Poincaré series translates, after taking logs and using the geodesic counting, into absolute convergence of this double series for $s > \delta$); it is precisely what licenses Step 3's application of Tonelli. Substituting,
> $$\sum_{\gamma}\sum_{m \ge 1}\mu^\phi_X\big(C_X(\gamma^m)\big) \;=\; -C\log Z_X(s). \qquad \blacksquare$$

> [!cite]- External input — log-expansion of the Selberg zeta
> **Statement (typed):** for $s > \delta$, $-\log Z_X(s) = \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$, the double series converging absolutely.
> **Why it's true (intuition):** apply $-\log(1 - x) = \sum_{m \ge 1} x^m/m$ to each factor $1 - e^{-(s+k)\ell_\gamma}$ in the double product defining $Z_X$; then interchange the resulting triple sum over $(\gamma, k, m)$ and do the geometric $k$-sum $\sum_{k \ge 0} e^{-km\ell_\gamma} = 1/(1 - e^{-m\ell_\gamma}) = e^{m\ell_\gamma}/(e^{m\ell_\gamma} - 1)$; combining, $e^{-sm\ell_\gamma} \cdot e^{m\ell_\gamma}/(e^{m\ell_\gamma} - 1) = e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma} - 1)$.
> **Source:** Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces* (2nd ed.), Ch. 9; also [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]] on this page's ring.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.1]]. Used directly to prove [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] (the killing case, $C = 1$, $s = \frac12 + \sqrt{1/4 + \kappa}$) and adapted in the proof of [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]] (twisted Ruelle, via a difference of two masses). The lemma is the recurring engine of §4: every zeta identity in the paper factors through it.
