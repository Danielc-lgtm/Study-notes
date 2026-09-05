---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Function on a Manifold"
  - "Def - Support of a Function"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry]
---

# Notation

$M$ denotes a smooth manifold (the bump-function notion makes sense on any topological space, but we typically demand smoothness, which requires a smooth structure). $A \subseteq M$ is a closed subset; $U \subseteq M$ is an open set containing $A$. The **standard one-sided germ** is
$$\psi_0(t) = \begin{cases} e^{-1/t} & t > 0 \\ 0 & t \leq 0 \end{cases},$$
a smooth function on $\mathbb{R}$ whose every derivative at $0$ equals $0$. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

This is a compound page: it defines two interlocking notions — **bump function** and **smooth cutoff** — because they are introduced together and none is fully usable without the others.

---

# Axiom Motivation

We want a smooth function on a smooth manifold that is constantly equal to $1$ on a prescribed closed set $A$ and constantly equal to $0$ outside a prescribed open neighbourhood $U$ of $A$. Such a function is a *smooth interpolation* between "all the way on" and "all the way off" — a smooth version of a step function. The challenge is that the natural step function ($1$ on $A$, $0$ off $U$) is discontinuous, while continuous interpolations (such as a linear ramp between $A$ and $\partial U$) are not smooth.

The fix begins in one [[Def - Dimension|dimension]]. We need a smooth function $\eta : \mathbb{R} \to [0, 1]$ that equals $1$ on $(-\infty, r_1]$ and $0$ on $[r_2, \infty)$, smoothly transitioning in between. The naive linear ramp fails at $r_1$ and $r_2$. The naive polynomial fix — say, a cubic spline — fails because polynomials are not $C^\infty$ at their transition points unless they are constant.

The key insight is the existence of a *single* smooth function whose derivatives at one endpoint all vanish: the function
$$\psi_0(t) = e^{-1/t}, \quad t > 0; \quad \psi_0(t) = 0, \quad t \leq 0.$$
This function is smooth on $\mathbb{R}$, with $\psi_0^{(k)}(0) = 0$ for every $k \geq 0$. The verification is a computation: for $t > 0$, $\psi_0^{(k)}(t) = p_k(t) e^{-1/t}/t^{2k}$ for some polynomial $p_k$, and as $t \to 0^+$ the exponential dominates the polynomial, so $\psi_0^{(k)}(0^+) = 0$. From the left, $\psi_0^{(k)}(0^-) = 0$ trivially. The two one-sided derivatives agree, so $\psi_0^{(k)}(0)$ exists and equals $0$.

This function is *smooth but not analytic at $0$*: its Taylor series at $0$ is $0 + 0t + 0t^2 + \ldots$, which converges to $0$ everywhere — but $\psi_0$ is not zero on $(0, \infty)$. The Taylor series at $0$ fails to recover $\psi_0$. This non-analyticity is *the property that makes bump functions possible*: it is precisely the slack between $C^\infty$ and $C^\omega$ that lets us build cutoffs. **There are no nonzero analytic bump functions on a connected domain** (an analytic function vanishing on a nonempty open set vanishes on the whole connected component by the identity theorem), so the entire local-to-global machinery of differential geometry rests on the $C^\infty$-vs-$C^\omega$ gap.

From $\psi_0$ we build a *smooth cutoff* — a smooth function transitioning from $1$ to $0$ over an interval:
$$h(t) = \frac{\psi_0(r_2 - t)}{\psi_0(r_2 - t) + \psi_0(t - r_1)}.$$
The denominator is positive for all $t$ (one of $r_2 - t$, $t - r_1$ is always positive, so one of the $\psi_0$ values is positive). For $t \leq r_1$, $\psi_0(t - r_1) = 0$, so the denominator equals the numerator, hence $h(t) = 1$. For $t \geq r_2$, $\psi_0(r_2 - t) = 0$, so the numerator is $0$ and $h(t) = 0$. In between, $h$ is smooth (ratio of smooth functions with nonzero denominator) and takes values strictly between $0$ and $1$.

In higher [[Def - Dimension|dimensions]], take a radial bump: $H : \mathbb{R}^n \to [0, 1]$, $H(x) = h(|x|)$ with $h$ a cutoff transitioning from $1$ on $|x| \leq r_1$ to $0$ on $|x| \geq r_2$. This $H$ is smooth (composition of the smooth cutoff with the smooth norm — except at $0$, where $H$ is constant $1$, hence smooth). The support of $H$ is $\overline{B(0, r_2)}$.

To upgrade to a manifold, pull the Euclidean bump back through a chart. Given $A \subseteq U \subseteq M$ with $A$ closed and $U$ open, cover $A$ by charts (using paracompactness if $A$ is non-compact), build Euclidean bumps on each chart, weight by a partition of unity, sum. The result is a smooth manifold-level bump.

*Why bump functions matter:* they are the atomic ingredient for all "local construction extended to global" arguments. A partition of unity is a normalized family of bump functions. The smooth extension lemma multiplies the function to be extended by bumps. The construction of Riemannian metrics weights local metrics by bumps. The construction of connections, volume forms, sections of bundles — all use bumps.

---

# The Definition

Let $M$ be a smooth manifold, $A \subseteq M$ a closed subset, $U \subseteq M$ an open set with $A \subseteq U$.

A **smooth bump function for $A$ supported in $U$** is a smooth function $\psi : M \to \mathbb{R}$ satisfying:

(1) $0 \leq \psi(p) \leq 1$ for every $p \in M$;
(2) $\psi(p) = 1$ for every $p \in A$;
(3) $\operatorname{supp}(\psi) \subseteq U$.

A **smooth cutoff function** on $\mathbb{R}$ (with parameters $r_1 < r_2$) is a smooth function $h : \mathbb{R} \to [0, 1]$ with $h \equiv 1$ on $(-\infty, r_1]$, $0 < h < 1$ on $(r_1, r_2)$, and $h \equiv 0$ on $[r_2, \infty)$. The standard construction (Lee Lemma 2.21):
$$h(t) = \frac{\psi_0(r_2 - t)}{\psi_0(r_2 - t) + \psi_0(t - r_1)},$$
where $\psi_0(t) = e^{-1/t}$ for $t > 0$ and $\psi_0(t) = 0$ for $t \leq 0$.

A **radial smooth bump on $\mathbb{R}^n$** (with inner radius $r_1$ and outer radius $r_2$, $0 < r_1 < r_2$) is $H : \mathbb{R}^n \to [0, 1]$, $H(x) = h(|x|)$, where $h$ is the cutoff above. It satisfies $H = 1$ on $\overline{B(0, r_1)}$, $0 < H < 1$ on $B(0, r_2) \setminus \overline{B(0, r_1)}$, and $H = 0$ on $\mathbb{R}^n \setminus B(0, r_2)$, with $\operatorname{supp}(H) = \overline{B(0, r_2)}$.

The general existence theorem on a smooth manifold is [[Thm - Existence of Smooth Bump Functions]]: for any closed $A \subseteq M$ and open $U \supseteq A$, a smooth bump function for $A$ supported in $U$ exists.

---

# Relate to Other Fields / Compression

A bump function is **the smooth-category analogue of a Urysohn function**. In topology, [[Thm - Urysohn's Lemma|Urysohn's lemma]] says that on a normal space, any two disjoint closed sets can be separated by a continuous function: there is a continuous $g : M \to [0, 1]$ with $g \equiv 0$ on one set and $g \equiv 1$ on the other. The bump-function existence theorem upgrades this to smoothness: on a smooth manifold (which is automatically normal because it is paracompact Hausdorff), any closed set and the complement of an open neighbourhood can be separated by a *smooth* function. The proof of the smooth version is, in essence, "do Urysohn with smooth $\psi_0$-based bumps instead of continuous Urysohn-style bumps".

The construction is also related to the **convolution mollifier** in PDE / harmonic analysis: a compactly supported smooth function $\rho$ on $\mathbb{R}^n$ with $\int \rho = 1$, used to smooth out distributions or singular functions by convolution $f * \rho$. The same $\psi_0$-based construction provides mollifiers; the only added requirement is normalization $\int \rho = 1$.

**True name:** *a bump function is a smooth indicator function with a soft boundary*. The official definition specifies the values $1$ on $A$ and $0$ outside $U$; the operational meaning is that it interpolates smoothly between "fully on inside $A$" and "fully off outside $U$".

---

# Examples / Corollaries

**Is an instance: the standard Euclidean bump on $\mathbb{R}^n$.** $H : \mathbb{R}^n \to [0, 1]$, $H(x) = h(|x|)$ with $h$ as above, $r_1 = 1$, $r_2 = 2$. Equals $1$ on $\overline{B(0, 1)}$, vanishes outside $B(0, 2)$, smooth everywhere. The reference example for every chart-based bump construction.

**Is an instance: bump along an axis.** Let $h$ be a one-sided cutoff equal to $1$ on $(-\infty,1/4]$ and zero on $[1/2,\infty)$. Then $\psi(t)=h(|t|)$ is smooth: away from $0$ this follows by composition, and near $0$ it is the constant $1$. It equals $1$ on $[-1/4,1/4]$ and has support in $[-1/2,1/2]\subset(-1,1)$. Composing with the $i$th coordinate gives a cutoff in that coordinate; multiplying such cutoffs over all coordinates gives a compactly supported box bump on $\mathbb{R}^n$.

**Is an instance: chart-pulled-back Euclidean bump.** Given a chart $(U, \varphi)$ on $M$ with $\varphi(U) \supseteq \overline{B(0, r_2)}$, and a Euclidean bump $H$ supported in $\overline{B(0, r_2)}$, define
$$\widetilde H(p) = \begin{cases} H(\varphi(p)) & p \in U \\ 0 & p \notin U \end{cases}.$$
This is a smooth function on $M$ supported in $\varphi^{-1}(\overline{B(0, r_2)}) \subseteq U$. (Smoothness at boundary points: in any chart contained in $M \setminus U$, $\widetilde H \equiv 0$, which is smooth.) The standard recipe for building manifold-level bumps from Euclidean ones.

**Is NOT an instance: the indicator function $\chi_A$.** For $A$ closed, $\chi_A$ is $1$ on $A$ and $0$ off $A$ — superficially a bump. But $\chi_A$ is not even continuous (jumps at $\partial A$), let alone smooth. A bump function smooths out the jump over a neighbourhood.

**Is NOT an instance: a continuous Urysohn function.** The continuous function $g$ provided by Urysohn's lemma separates closed sets but is generally not smooth. The smooth bump function is the upgrade. A continuous Urysohn function is to a smooth bump as $|x|$ is to a smooth approximation of $|x|$.

**Is NOT an instance: a polynomial.** No polynomial $p : \mathbb{R} \to \mathbb{R}$ is a bump function (polynomials are unbounded and have no compact support unless they are constant, in which case they don't separate). The non-rigidity of $C^\infty$ over polynomial / analytic functions is essential.

**Corollary (smooth $\psi_0$).** The one-sided germ $\psi_0(t) = e^{-1/t}$ for $t > 0$, $\psi_0(t) = 0$ for $t \leq 0$ is smooth on $\mathbb{R}$. *Proof:* induction on $k$ shows $\psi_0^{(k)}$ exists and has the form $p_k(t) e^{-1/t}/t^{2k}$ for $t > 0$ (with $p_k$ a polynomial of degree $\leq k$), tends to $0$ as $t \to 0^+$, and the left derivative is $0$. (Lee Lemma 2.20.)

**Corollary (smooth cutoff transitions from $1$ to $0$).** The cutoff $h(t) = \psi_0(r_2 - t)/(\psi_0(r_2 - t) + \psi_0(t - r_1))$ is smooth on $\mathbb{R}$, equals $1$ on $(-\infty, r_1]$, equals $0$ on $[r_2, \infty)$, and takes values strictly in $(0, 1)$ on $(r_1, r_2)$. (Lee Lemma 2.21.)

**Corollary (radial smooth bump in $\mathbb{R}^n$).** $H(x) = h(|x|)$ with $h$ as above is smooth on $\mathbb{R}^n$, equal to $1$ on $\overline{B(0, r_1)}$, supported in $\overline{B(0, r_2)}$. (Lee Lemma 2.22.) Smoothness at $0$: $H$ is constantly $1$ in a neighbourhood of $0$, hence smooth there.

**Corollary (existence on manifolds).** For any smooth manifold $M$, closed $A \subseteq M$, and open $U \supseteq A$, a smooth bump function for $A$ supported in $U$ exists. See [[Thm - Existence of Smooth Bump Functions]].

**Calibration check.** Verify the following: (i) $\psi_0^{(k)}(0) = 0$ for $k = 0, 1, 2$ by direct calculation. (ii) The cutoff $h$ with $r_1 = 0, r_2 = 1$ satisfies $h(1/2) \in (0, 1)$ — compute it. (iii) The radial bump $H$ with $r_1 = 1, r_2 = 2$ has support exactly $\overline{B(0, 2)}$ (verify the closure). (iv) The pullback of an Euclidean bump through a chart is smooth on all of $M$, not just on the chart domain — verify the smoothness at points outside the chart.

---

# Unlocked by This

> [!tip] Smooth Partitions of Unity *(from Differential Geometry)*
> Once smooth bump functions exist for arbitrary closed-open pairs, a **smooth partition of unity** subordinate to any open cover can be constructed: refine the cover to be locally finite, build a bump on each cover element (equal to $1$ on a smaller closed shrinkage), sum, normalize. See [[Def - Partition of Unity on a Manifold]] and [[Thm - Existence of Smooth Partitions of Unity]].

> [!tip] Smooth Extension from Closed Sets *(from Differential Geometry)*
> A smooth function defined on a closed subset extends smoothly to the whole manifold. The construction uses bump functions (one bump for each neighbourhood-extension, summed via a partition of unity). See [[Thm - Smooth Extension Lemma]].

> [!tip] Mollifiers and Smoothing in PDE *(from Analysis)*
> The same $\psi_0$-based construction produces **mollifiers**: compactly supported smooth functions $\rho_\epsilon$ on $\mathbb{R}^n$ with $\int \rho_\epsilon = 1$ and support shrinking to $\{0\}$. Convolution $f * \rho_\epsilon$ smooths an arbitrary distribution to a $C^\infty$ function, recovering $f$ as $\epsilon \to 0$. This is the standard regularization technique in PDE theory.

> [!tip] Compactly Supported Test Functions $\mathcal{D}(\mathbb{R}^n)$ *(from Distribution Theory)*
> The space of compactly supported smooth functions on $\mathbb{R}^n$ (or on a manifold) is the standard space of **test functions** in distribution theory. The existence of "many" such functions — supplied by the bump-function construction — is what makes distribution theory non-trivial. Without bumps, the space of test functions would be too thin to produce interesting distributions.
