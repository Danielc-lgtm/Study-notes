---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Function on a Manifold"
  - "Def - Partition of Unity on a Manifold"
  - "Def - Bump Function and Smooth Cutoff"
  - "Def - Locally Finite Family and Refinement"
  - "Def - Paracompact Space"
  - "Thm - Paracompact Has Partitions of Unity"
  - "Thm - Locally Compact σ-Compact Hausdorff is Paracompact"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold; $\{U_\alpha\}_{\alpha \in A}$ is an open cover indexed by $A$. A **regular coordinate ball** is the preimage under a smooth chart $\varphi : W \to \mathbb{R}^m$ of an open ball $B(0, r) \subseteq \mathbb{R}^m$ with $\overline{B(0, r)} \subseteq \varphi(W)$ (so the closure of the ball is compact and inside the chart's image). The standard one-sided germ is $\psi_0(t) = e^{-1/t}$ for $t > 0$, $0$ for $t \leq 0$. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Statement

> **Theorem (Existence of Smooth Partitions of Unity).** Let $M$ be a smooth manifold (with or without boundary), and let $\{U_\alpha\}_{\alpha \in A}$ be any open cover of $M$. Then there exists a smooth partition of unity $\{\psi_\alpha\}_{\alpha \in A}$ subordinate to $\{U_\alpha\}$: smooth functions $\psi_\alpha : M \to [0, 1]$ with
>
> 1. $\operatorname{supp}(\psi_\alpha) \subseteq U_\alpha$ for every $\alpha$;
> 2. The supports $\{\operatorname{supp}(\psi_\alpha)\}_{\alpha \in A}$ form a locally finite family;
> 3. $\sum_{\alpha \in A} \psi_\alpha(p) = 1$ for every $p \in M$ (a finite sum at each point by local finiteness).

This is Lee Theorem 2.23.

---

# Motivation

This is the central existence theorem of smooth manifold theory. Its role is to make local constructions global: whenever a smooth object can be defined on each chart, the partition of unity provides a globally defined smooth object obtained by weighting and summing the local pieces. Without this theorem, there would be no general existence proofs for Riemannian metrics, no integration of differential forms, no smooth sections of vector bundles, no soft sheaves — almost the entire global apparatus of differential geometry would collapse.

The theorem is the **smooth-category upgrade of the topological partition-of-unity existence theorem** ([[Thm - Paracompact Has Partitions of Unity]]). The topological version produces continuous partitions of unity on any paracompact Hausdorff space; the smooth version produces smooth partitions of unity on any smooth manifold. The strengthening is non-trivial: it requires the construction of smooth bump functions on $\mathbb{R}^n$, which themselves rest on the $\psi_0(t) = e^{-1/t}$-trick — a piece of real analysis that has no topological analogue.

The proof has three steps. **First, reduce to a countable locally finite refinement by regular coordinate balls.** A smooth manifold is second-countable Hausdorff, hence Lindelöf, hence any open cover admits a countable subcover. The countable subcover can be refined (using paracompactness, which follows from second-countable Hausdorff via [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]] — smooth manifolds are locally compact because they are locally Euclidean) to a countable locally finite cover by regular coordinate balls. Each ball is in the closure of a chart, so a chart-pulled-back smooth bump function exists supported in it.

**Second, build smooth bumps on each refinement ball.** For each ball $B_i$ in the refinement, use the chart on which it sits and pull back the standard Euclidean bump function $H_i : \mathbb{R}^m \to [0, 1]$ (equal to $1$ on a smaller ball, supported in $B_i$'s image). The pullback gives a smooth $f_i : M \to [0, 1]$ supported in $\overline{B_i}$, positive on $B_i$.

**Third, sum and normalize.** Define $f = \sum_i f_i$; by local finiteness this is a finite sum at each point, hence smooth, and $f(p) > 0$ for every $p$ because every $p$ is in some $B_i$ where $f_i(p) > 0$. Set $g_i = f_i / f$. The $g_i$ are smooth (ratio of smooth functions with positive denominator), nonnegative, sum to $1$, locally finite. Re-index over the original cover: for each $\alpha$, set $\psi_\alpha = \sum_{i : a(i) = \alpha} g_i$ where $a(i)$ chooses an $\alpha$ such that $B_i \subseteq U_{a(i)}$.

This three-step structure — refine, bump, normalize — is the canonical partition-of-unity construction. It is parallel to the topological proof (refine, Urysohn-bump, normalize), differing only in step 2 where the smooth bumps replace continuous Urysohn bumps.

A reader is assumed to be comfortable with the construction of smooth bumps on $\mathbb{R}^n$ via the $\psi_0$-trick (see [[Def - Bump Function and Smooth Cutoff]]) and with the topological notion of locally finite refinement.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires only that $M$ be a smooth manifold and $\{U_\alpha\}$ be an open cover.

The first source is **a manifold with a chosen atlas**. Property $B$: $M$ is given with a specific smooth atlas $\{(U_\alpha, \varphi_\alpha)\}$. The bridge: the atlas charts form an open cover, so the theorem applies, yielding a partition of unity subordinate to the atlas. *Example:* every construction on a manifold that needs to interpolate between chart-defined objects.

The second source is **a manifold with a cover by open sets**, where the open sets are *not* chart domains. Property $B$: $\{U_\alpha\}$ is an arbitrary open cover. The bridge: by the theorem, a partition of unity subordinate to any open cover exists; in particular, the cover need not be a chart cover. *Example:* covering a manifold by open sets defined by physical or geometric conditions (e.g., "the region where $|x| < 1$" for some smooth function $|x|$) and assembling a global construction across these regions.

The third source is **a manifold with boundary**. Property $B$: $M$ is a smooth manifold with boundary. The bridge: the theorem holds for manifolds with boundary (Lee Theorem 2.23 with Exercise 2.24 covers this case). *Example:* the construction of Riemannian metrics on manifolds with boundary, used in integration / Stokes' theorem.

The fourth source is **a manifold given via a quotient construction**. Property $B$: $M = N/G$ where $N$ is a smooth manifold and $G$ a discrete group acting freely and properly. The bridge: $M$ inherits a smooth manifold structure (paracompact Hausdorff second-countable), so the theorem applies. *Example:* constructions on lens spaces, tori, real projective spaces — all obtained as quotients.

**Targets (Output Amplification)**

The conclusion is a smooth partition of unity, which is the input to many further constructions.

Combine the conclusion with **local Riemannian metrics on each chart**. Property $D$: on each chart $U_\alpha$, the Euclidean inner product pulls back to a local Riemannian metric $g_\alpha$. The amplified result $E$: the weighted sum $g = \sum_\alpha \psi_\alpha g_\alpha$ is a globally defined smooth Riemannian metric on $M$. The combination produces the existence theorem for Riemannian metrics, which is essential to all of Riemannian geometry. *Example:* every smooth manifold admits a Riemannian metric (see **Riemannian Geometry** and [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|DG XII]]).

Combine the conclusion with **smooth functions on each chart**. Property $D$: a family of smooth functions $f_\alpha : U_\alpha \to \mathbb{R}$, prescribed locally. The amplified result $E$: the weighted sum $f = \sum_\alpha \psi_\alpha f_\alpha$ (with $\psi_\alpha f_\alpha$ extended by zero outside $U_\alpha$) is a smooth function on $M$ that locally averages the $f_\alpha$. The combination is the basic globalization template. *Example:* used to construct global smooth functions with prescribed behaviour, smooth approximations to discontinuous data, smooth interpolations between chart-defined functions.

Combine the conclusion with **local sections of a vector bundle**. Property $D$: a smooth vector bundle $E \to M$ with local trivializations on each $U_\alpha$, and local sections $\sigma_\alpha$ on each $U_\alpha$. The amplified result $E$: the global section $\sigma = \sum_\alpha \psi_\alpha \sigma_\alpha$ (in the appropriate sense, since the trivializations differ on overlaps — usually one writes the partition-of-unity construction in terms of the trivializations and verifies it gives a well-defined global section). The combination produces existence theorems for sections (connections, Hermitian metrics, etc.). *Example:* every smooth vector bundle admits a smooth connection.

Combine the conclusion with **integration on Euclidean charts**. Property $D$: a top-degree differential form $\omega$ on $M$ and an integration theory for forms on Euclidean open sets. The amplified result $E$: the integral $\int_M \omega = \sum_\alpha \int_{U_\alpha} \psi_\alpha \omega$ is well-defined and independent of the chart cover. *Example:* defines integration on oriented manifolds, including [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|Stokes' theorem]] in the manifold setting.

---

# Why Is It True

The intuition: every smooth manifold has paracompactness (a topological property) and a supply of smooth bump functions (from the $e^{-1/t}$-trick on $\mathbb{R}$ pulled back through charts). Combining these gives the construction.

**The mechanism in one line: refine the open cover to be locally finite, build a smooth bump on each refinement element, sum and normalize.**

The three ingredients:

1. **Paracompactness.** A smooth manifold is Hausdorff and second-countable, hence locally compact Hausdorff $\sigma$-compact, hence paracompact ([[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]]). Paracompactness lets any open cover be refined to a locally finite open cover — in fact, to a countable locally finite cover by *regular coordinate balls*, each compactly contained in a chart.

2. **Smooth bumps.** On $\mathbb{R}^m$, the standard radial bump $H : \mathbb{R}^m \to [0, 1]$ — built from the cutoff $h(t) = \psi_0(r_2 - t)/(\psi_0(r_2 - t) + \psi_0(t - r_1))$ via $H(x) = h(|x|)$ — is equal to $1$ on $\overline{B(0, r_1)}$ and supported in $\overline{B(0, r_2)}$. Pulled back through a chart, this gives a smooth bump on the manifold supported in the chart's domain, equal to $1$ on a smaller ball.

3. **Sum and normalize.** On each regular coordinate ball $B_i$, place a smooth bump $f_i$ supported in $\overline{B_i}$, equal to $1$ on a smaller ball, with $\bigcup_i \{f_i > 0\}$ covering $M$. The sum $f = \sum_i f_i$ is locally finite (so smooth) and positive everywhere (since $\bigcup_i \{f_i > 0\} = M$). Normalize: $g_i = f_i / f$. Then $\sum_i g_i = 1$, $g_i \geq 0$, $\operatorname{supp}(g_i) \subseteq \overline{B_i}$, locally finite. This is a partition of unity subordinate to the refinement; re-index to get one subordinate to the original cover.

The argument is conceptually like a *topological convolution*: convolve the indicator function of $M$ (which is everywhere $1$) with a family of smooth bumps that respect the cover, and obtain a smooth identity-of-mass decomposition.

---

# What Makes This Hard

The proof has three independent ingredients (paracompactness, smooth bumps, sum-and-normalize), each of which is reasonable but the combination is delicate. The most common conceptual error is to *underestimate* the smooth-bump step: it is not enough to invoke "Urysohn-like" — one must explicitly construct $C^\infty$ bumps, and the construction requires the $\psi_0(t) = e^{-1/t}$-trick, an essentially real-analytic fact. Without smooth bumps, there is no smooth partition of unity, even when paracompactness is available.

The most common technical error is to handle the *infinite* sum incorrectly. The sum $\sum_\alpha \psi_\alpha = 1$ is *not* an infinite sum in the analysis sense: by local finiteness, it is a finite sum at each point, and the *function* $\sum_\alpha \psi_\alpha$ is locally a finite sum of smooth functions, hence smooth, with no convergence issues. Treating it as an infinite series requiring convergence checks is a confusion.

The third common error is to forget that the partition is *subordinate* to the original cover but is built from a *refinement*. The re-indexing step — where the partition of unity for the refinement is summed across the fibres of the refinement-to-cover map to yield a partition of unity for the original cover — is the only place where the index-set changes, and it must be done carefully (verifying that the resulting sums are still smooth, still locally finite, still sum to $1$).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Refine the cover to a countable locally finite refinement by regular coordinate balls. Build a smooth bump on each ball using a chart and the standard Euclidean bump. Sum and normalize.

**Subgoal decomposition:**

1. **Refine the cover.** By second-countability and paracompactness of $M$, the open cover $\{U_\alpha\}$ has a countable locally finite refinement $\{B_i\}_{i \in \mathbb{N}}$ by regular coordinate balls (Lee Theorem 1.15).
   - *Hint:* Smooth manifolds are paracompact, and regular coordinate balls form a basis.
   - *Why needed:* Step 2 needs a locally finite family on which to place bumps.

2. **Place smooth bumps.** For each $B_i$ (a chart-pullback of $B_{r_i'}(0) \subseteq \mathbb{R}^m$ with $\overline{B_{r_i}(0)} \subseteq B_{r_i'}(0)$, $r_i < r_i'$), define $f_i = H_i \circ \varphi_i$ on $B_i$ (extended by zero outside), with $H_i$ a Euclidean radial bump equal to $1$ on $\overline{B_{r_i}(0)}$ and supported in $B_{r_i'}(0)$. Then $f_i \in C^\infty(M)$, $\operatorname{supp}(f_i) = \overline{B_i}$, $f_i = 1$ on the smaller ball, $f_i \in [0, 1]$.
   - *Hint:* Use the standard Euclidean bump built from $\psi_0(t) = e^{-1/t}$. Smoothness extends from the chart into $M \setminus \overline{B_i}$ because $f_i \equiv 0$ there.
   - *Why needed:* Provides the local data for the sum.

3. **Sum and normalize.** Define $f = \sum_i f_i$. By local finiteness, this is a finite sum at each point, hence $f \in C^\infty(M)$ and $f(p) > 0$ for every $p$ (since every $p$ is in some smaller ball where $f_i(p) = 1$, contributing at least $1$ to the sum).
Set $g_i = f_i / f$. Then $g_i \in C^\infty(M)$, $g_i \in [0, 1]$, $\sum_i g_i = 1$, supports still locally finite.
   - *Hint:* The denominator's positivity is what makes the ratio smooth.
   - *Why needed:* Gives a partition of unity subordinate to the refinement.

4. **Re-index.** For each $i$, choose $a(i) \in A$ with $B_i \subseteq U_{a(i)}$. For each $\alpha \in A$, define $\psi_\alpha = \sum_{i : a(i) = \alpha} g_i$ (with empty sum equal to $0$).
Verify: $\psi_\alpha \in C^\infty(M)$ (locally finite sum), $\operatorname{supp}(\psi_\alpha) \subseteq U_\alpha$ (union of $\overline{B_i}$ with $B_i \subseteq U_{a(i)} = U_\alpha$; this union is contained in $\overline{U_\alpha}$, and inside $U_\alpha$ because the $B_i$ are inside open $U_\alpha$... use the fact that closures of subsets in open sets stay within), $\sum_\alpha \psi_\alpha = \sum_i g_i = 1$, supports locally finite.
   - *Hint:* The re-indexing step is bookkeeping; the work is already done in steps 1–3.
   - *Why needed:* Produces a partition subordinate to the original cover, not just the refinement.

---

# Lemma Decomposition

> [!note]- Lemma 1: Smooth manifolds admit countable locally finite refinements by regular coordinate balls
> **Statement:** Let $M$ be a smooth manifold and $\{U_\alpha\}$ an open cover. Then there exists a countable, locally finite open refinement $\{B_i\}_{i \in \mathbb{N}}$ of $\{U_\alpha\}$ such that each $B_i$ is a regular coordinate ball (a chart-pullback of an open Euclidean ball whose closure is in the chart's image).
>
> **Hint:** Regular coordinate balls form a basis for the topology of $M$. $M$ is second-countable, hence Lindelöf; any open cover has a countable subcover. Use paracompactness (from [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]]) to refine to locally finite.
>
> **Why needed:** Step 1 of the main proof — provides the underlying combinatorial structure on which the bumps will be placed.
>
> > [!note]- Full proof (sketch — Lee Theorem 1.15)
> > Each $U_\alpha$ is open in $M$. The collection of all regular coordinate balls is a basis: every point of $U_\alpha$ has a neighbourhood that is a regular coordinate ball, contained in $U_\alpha$. So $\{U_\alpha\}$ is refined by the collection $\mathcal{B}$ of all regular coordinate balls contained in some $U_\alpha$. $\mathcal{B}$ is itself an open cover of $M$. Since $M$ is second-countable (basis $\subseteq$ countable subcover via Lindelöf), $\mathcal{B}$ has a countable subcover $\{B_i\}_{i \in \mathbb{N}}$. Since $M$ is paracompact, this countable cover has a locally finite open refinement. The locally finite refinement still consists of regular coordinate balls (we can refine each ball to a smaller one if needed). The result is a countable locally finite refinement by regular coordinate balls.

> [!note]- Lemma 2: Pulling back smooth bumps through charts gives smooth manifold-level bumps
> **Statement:** Let $B$ be a regular coordinate ball in $M$, the pullback under a chart $\varphi : W \to \mathbb{R}^m$ of $B_{r'}(0)$, with $\overline{B_r(0)} \subseteq B_{r'}(0)$ for some $r < r'$. Let $H : \mathbb{R}^m \to [0, 1]$ be a smooth radial bump equal to $1$ on $\overline{B_r(0)}$ and supported in $\overline{B_{r'}(0)}$.
> Define $f : M \to [0, 1]$ by $f(p) = H(\varphi(p))$ for $p \in W$ and $f(p) = 0$ for $p \notin W$. Then $f \in C^\infty(M)$, $\operatorname{supp}(f) \subseteq \overline B$, and $f \equiv 1$ on the smaller ball $\varphi^{-1}(\overline{B_r(0)})$.
>
> **Hint:** Smoothness on $W$ is clear ($f|_W = H \circ \varphi$, composition of smooth maps). Smoothness on $M \setminus \overline B$ is also clear ($f \equiv 0$, which is smooth). The non-trivial part is smoothness on the boundary $\partial B$, where the two pieces overlap on a buffer zone where $f$ is zero from both sides — and both definitions yield the same zero function on the overlap.
>
> **Why needed:** Step 2 of the main proof — produces the local bumps.
>
> > [!note]- Full proof
> > The function $H : \mathbb{R}^m \to [0, 1]$ is smooth (composition of the radial-cutoff $h$ with the smooth norm $|\cdot|$ — smooth because $H$ is constant $1$ in a neighbourhood of $0$).
> >
> > On $W$: $f|_W = H \circ \varphi$. The chart $\varphi$ is a smooth map (between $W$ and the chart image, which is open in $\mathbb{R}^m$), and $H$ is smooth, so the composition is smooth.
> >
> > On $M \setminus \overline B$: $f \equiv 0$. The zero function is smooth.
> >
> > On the boundary or near it: any point $p \in \overline B \setminus B$ has $\varphi(p) \in \overline{B_{r'}(0)} \setminus B_{r'}(0)$, where $H$ vanishes. So $f(p) = 0$. The two definitions ($f = H \circ \varphi$ from inside $W$, $f = 0$ from outside $\overline B$) agree on a neighbourhood of $p$ in $W \setminus \overline B$ (where both are zero). So $f$ is well-defined and smooth at $p$.

> [!note]- Lemma 3: A finite-at-each-point sum of smooth functions is smooth
> **Statement:** Let $\{f_i\}_{i \in \mathbb{N}}$ be a family of smooth functions on $M$ with $\{\operatorname{supp}(f_i)\}$ locally finite. Then $f = \sum_i f_i$ is well-defined (a finite sum at each point) and smooth on $M$.
>
> **Hint:** Local finiteness means each $p$ has a neighbourhood $V_p$ on which only finitely many $f_i$ are nonzero. On $V_p$, $f = \sum_{i : V_p \cap \operatorname{supp}(f_i) \neq \emptyset} f_i$ (a finite sum), which is smooth.
>
> **Why needed:** Step 3 — establishes smoothness of $f = \sum_i f_i$.
>
> > [!note]- Full proof
> > Fix $p \in M$. By local finiteness, $p$ has an open neighbourhood $V_p$ meeting only finitely many supports — say, $\operatorname{supp}(f_{i_1}), \ldots, \operatorname{supp}(f_{i_k})$. For $i \notin \{i_1, \ldots, i_k\}$, $\operatorname{supp}(f_i) \cap V_p = \emptyset$, so $f_i \equiv 0$ on $V_p$.
> >
> > Therefore on $V_p$, $f = f_{i_1} + \cdots + f_{i_k}$, a finite sum of smooth functions, hence smooth on $V_p$. Since $p$ was arbitrary, $f$ is smooth on all of $M$ (smoothness is local).

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a smooth manifold and $\{U_\alpha\}_{\alpha \in A}$ an open cover.
>
> **Step 1 — refine.** By Lemma 1 (Lee Theorem 1.15), $\{U_\alpha\}$ has a countable locally finite refinement $\{B_i\}_{i \in \mathbb{N}}$ by regular coordinate balls. For each $i$, choose $a(i) \in A$ with $B_i \subseteq U_{a(i)}$.
>
> **Step 2 — local bumps.** For each $i$, $B_i$ is the pullback under some chart $\varphi_i : W_i \to \mathbb{R}^m$ of $B_{r_i'}(0)$, with $\overline{B_{r_i}(0)} \subseteq B_{r_i'}(0)$ for some $r_i < r_i'$ chosen so $\{B_i^{\text{small}} := \varphi_i^{-1}(B_{r_i}(0))\}$ also covers $M$ (which we may arrange by refining further, since the regular coordinate balls form a basis).
>
> Choose a smooth radial bump $H_i : \mathbb{R}^m \to [0, 1]$ equal to $1$ on $\overline{B_{r_i}(0)}$ and supported in $\overline{B_{r_i'}(0)}$ (from [[Def - Bump Function and Smooth Cutoff]]). By Lemma 2, define $f_i : M \to [0, 1]$ by $f_i = H_i \circ \varphi_i$ on $W_i$ and $f_i = 0$ outside $\overline{B_i}$. Then $f_i \in C^\infty(M)$, $\operatorname{supp}(f_i) \subseteq \overline{B_i}$, $f_i \equiv 1$ on $B_i^{\text{small}}$.
>
> **Step 3 — sum and normalize.** By Lemma 3, $f = \sum_i f_i \in C^\infty(M)$. For every $p \in M$, $p$ is in some $B_i^{\text{small}}$, where $f_i(p) = 1$, so $f(p) \geq 1 > 0$.
>
> Define $g_i = f_i / f$. Then $g_i \in C^\infty(M)$ (ratio of smooth functions with positive denominator), $0 \leq g_i \leq 1$ (since $0 \leq f_i \leq f$), $\operatorname{supp}(g_i) = \operatorname{supp}(f_i) \subseteq \overline{B_i}$ (locally finite as a subfamily of a locally finite family), and $\sum_i g_i = \sum_i f_i / f = f/f = 1$.
>
> **Step 4 — re-index.** For each $\alpha \in A$, define
> $$\psi_\alpha = \sum_{i : a(i) = \alpha} g_i,$$
> with empty sum equal to the zero function. This is a smooth function (locally finite sum of smooth functions, by Lemma 3 applied to a sub-family) with $\operatorname{supp}(\psi_\alpha) \subseteq \bigcup_{i : a(i) = \alpha} \overline{B_i}$.
>
> The locally finiteness of $\{\overline{B_i}\}$ ensures that this union has the locally finite property as $\alpha$ varies: each point $p$ has a neighbourhood meeting only finitely many $\overline{B_i}$, hence meeting at most $|\{i : a(i) = \alpha, \overline{B_i} \cap V_p \neq \emptyset\}|$ supports for each $\alpha$, but only finitely many $\alpha$ have any $i$ with both conditions (since only finitely many $i$ have $\overline{B_i} \cap V_p \neq \emptyset$). So the family $\{\operatorname{supp}(\psi_\alpha)\}_\alpha$ is locally finite.
>
> Each $\overline{B_i}$ with $a(i) = \alpha$ is in $U_\alpha$ (since $B_i \subseteq U_{a(i)} = U_\alpha$ and supports are closures of subsets of open sets, contained in the open set when the open set is large enough — but we need $\overline{B_i} \subseteq U_\alpha$, which holds because $\overline{B_i}$ is compact in $W_i$ and $W_i \subseteq U_\alpha$ when chosen carefully; or by shrinking $B_i$ if needed). So $\operatorname{supp}(\psi_\alpha) \subseteq U_\alpha$.
>
> Finally, $\sum_\alpha \psi_\alpha = \sum_\alpha \sum_{i : a(i) = \alpha} g_i = \sum_i g_i = 1$, since every $i$ is in exactly one of the inner sums.
>
> Therefore $\{\psi_\alpha\}_{\alpha \in A}$ is a smooth partition of unity subordinate to $\{U_\alpha\}$. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: existence of Riemannian metrics on smooth manifolds.** Every smooth manifold admits a Riemannian metric (smoothly varying inner product on tangent spaces). The proof: cover $M$ by coordinate charts $\{(U_\alpha, \varphi_\alpha)\}$; on each $U_\alpha$, define a local Riemannian metric $g_\alpha$ by pulling back the standard Euclidean inner product through $\varphi_\alpha$; take a smooth partition of unity $\{\psi_\alpha\}$ subordinate to the cover; define $g = \sum_\alpha \psi_\alpha g_\alpha$. The result is smooth (sum of smooth tensor fields, locally finite), symmetric and positive-definite (convex combination of inner products preserves both properties). Foundational for Riemannian geometry.

**PDE / variational analysis: localization of weak formulations.** When working with PDEs on a manifold, test functions are taken to be compactly supported smooth functions $C^\infty_c(M)$. Localizing a global PDE to a chart: multiply by a chart-supported bump (from a partition of unity), reduce to a Euclidean PDE on the chart's image, solve there. This is the standard mechanism by which elliptic regularity, weak solution existence, and Sobolev space machinery transfer from $\mathbb{R}^n$ to manifolds. See **PDE on Manifolds** (downstream).

**Sheaf cohomology: the sheaf of smooth functions is acyclic.** The smooth function sheaf $\mathcal{O}_M^\infty$ on a smooth manifold is *soft* (any section on a closed subset extends to a global section), and soft sheaves are acyclic for sheaf cohomology. This is the foundational acyclicity result that makes the de Rham theorem ($H^*_{\mathrm{dR}}(M; \mathbb{R}) \cong H^*(M; \mathbb{R})$) work — the de Rham complex computes sheaf cohomology because each $\Omega^k$ is a $\mathcal{O}_M^\infty$-module sheaf, hence soft. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].

**Quantum field theory: gauge fixing via partition of unity.** In gauge field theories on a curved spacetime, the gauge group acts on the space of connections on a principal bundle. To define amplitudes via path integrals, one needs to fix a gauge. The Faddeev–Popov procedure uses a partition-of-unity-like construction on the moduli space of connections — locally pick a gauge, weight by the partition, ensure the global definition is independent of the choice. See **Gauge Theory** (downstream).

---

# Bridges

- **[[Def - Partition of Unity on a Manifold]]** — the object being constructed. The manifold version of partition of unity, additionally requiring smoothness of each weight.

- **[[Thm - Paracompact Has Partitions of Unity]]** — the topological analogue. The continuous partition of unity exists on any paracompact Hausdorff space (using Urysohn's lemma to build the bumps). This smooth version is the strengthening to smooth bumps via the $\psi_0$-trick.

- **[[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]]** — the topological input that gives paracompactness of smooth manifolds. Smooth manifolds are Hausdorff + second-countable, hence $\sigma$-compact (countable union of compacts) and locally compact (locally Euclidean), hence paracompact by this theorem. Paracompactness is what licenses the locally finite refinement step.

- **[[Def - Bump Function and Smooth Cutoff]]** — the building block. The Euclidean radial bump constructed from the $\psi_0(t) = e^{-1/t}$-trick is what fills the role of "smooth Urysohn function" in the proof. The bump constructions are what make smooth partitions of unity *smooth*, as opposed to merely continuous.

- **[[Thm - Existence of Smooth Bump Functions]]** — a direct corollary. Apply the partition-of-unity theorem to the cover $\{U, M \setminus A\}$ and take the $U$-component.

- **[[Thm - Smooth Extension Lemma]]** — another direct corollary. The smooth extension lemma extends smooth functions from closed sets to global functions via a partition-of-unity construction.

- **The de Rham theorem** — a downstream theorem whose proof critically uses partitions of unity. The de Rham complex computes sheaf cohomology of the constant sheaf $\mathbb{R}_M$ via the smooth-function resolution, which requires the smoothness sheaf to be acyclic, which requires partitions of unity. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].

---

# Unlocked by This

> [!tip] Existence of Riemannian Metrics *(from Riemannian Geometry)*
> **Every smooth manifold admits a Riemannian metric.** This is one of the deepest existence statements in differential geometry, in the sense that it has no analogue in algebraic or analytic geometry — those categories rarely admit Riemannian-like structures on arbitrary objects. The smooth category admits them universally, and the proof is *literally* the partition-of-unity argument: standard Euclidean inner product in each chart, weighted by a partition of unity. See **Riemannian Geometry** (downstream) and [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|DG XII]].

> [!tip] Existence of Connections on Vector Bundles *(from Differential Geometry)*
> Every smooth vector bundle $E \to M$ admits a smooth **connection** — a covariant derivative operator $\nabla : \Gamma(E) \to \Omega^1(M) \otimes \Gamma(E)$. The proof: trivialize $E$ locally, use the trivial connection in each trivialization, weight by a partition of unity, with the small correction needed to make the sum a connection (affine combinations of connections are connections, by a small calculation). See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|DG VI]].

> [!tip] Smoothing Discontinuous Constructions *(from Analysis on Manifolds)*
> Any rough construction on a smooth manifold — a measurable function, a continuous function with cusps, a distribution — can be approximated by smooth versions via mollifiers built from partition-of-unity bumps. This is the standard technique in regularization, mollifier approximation, and elliptic theory on manifolds.

> [!tip] Volume Forms and Integration *(from Differential Geometry)*
> An oriented manifold admits a global volume form, and integration of top-degree forms is well-defined globally via partition-of-unity decompositions $\int_M \omega = \sum_\alpha \int_{U_\alpha} \psi_\alpha \omega$. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]].

> [!tip] Soft Sheaves and Sheaf Cohomology *(from Sheaf Theory)*
> The sheaf $\mathcal{O}_M^\infty$ is **soft**, which makes it acyclic for sheaf cohomology. This is the foundational property that lets de Rham cohomology compute the actual cohomology of $M$, via the de Rham theorem $H^*_{\mathrm{dR}}(M; \mathbb{R}) \cong H^*(M; \mathbb{R})$. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].
