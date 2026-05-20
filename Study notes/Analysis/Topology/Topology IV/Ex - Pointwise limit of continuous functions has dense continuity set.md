---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Baire Category Theorem"
  - "Def - Nowhere Dense and Meager"
  - "Def - Continuous Map"
  - "Def - Cauchy Sequence and Complete Metric Space"
tags: [analysis, topology, baire, continuity]
---

# Problem Statement

Let $X$ be a complete metric space and $Y$ a metric space. Let $f_n : X \to Y$ be a sequence of continuous functions converging pointwise to $f : X \to Y$ on $X$ — that is, $f(x) = \lim_{n \to \infty} f_n(x)$ for every $x \in X$.

Show that the set of points where $f$ is continuous is a **residual** subset of $X$ (in particular, dense).

This is Bredon's Corollary 17.4.

**Recall:**

$X$ being a complete metric space is the hypothesis for [[Thm - Baire Category Theorem|Baire's theorem]]. The continuity of $f$ at $x$ is the condition: for every $\epsilon > 0$, there is $\delta > 0$ with $d(x, y) < \delta \Rightarrow d(f(x), f(y)) < \epsilon$. The set of discontinuities of $f$ is the complement.

The **oscillation** of $f$ at $x$ is $\omega_f(x) := \limsup_{r \to 0^+} \operatorname{diam}(f(B_r(x)))$; $f$ is continuous at $x$ iff $\omega_f(x) = 0$.

---

# Convergent Strategy

**Problem class:** Identify the continuity set of a Baire-class-1 function (pointwise limit of continuous functions) using Baire's theorem.

**Assumption pattern:** Each $f_n$ is continuous. Pointwise convergence gives an explicit constraint at each $x$: the sequence $(f_n(x))$ converges. But the convergence need not be uniform — speeds can vary wildly with $x$. The mismatch between pointwise and uniform convergence is what allows $f$ to be discontinuous, but Baire bounds the size of the discontinuity set.

**Theorem routing:** Express the discontinuity set as $\{x : \omega_f(x) > 0\} = \bigcup_k \{x : \omega_f(x) \geq 1/k\}$. Show each $\{x : \omega_f(x) \geq 1/k\}$ is nowhere dense, using uniform convergence on a residual set (combined with continuity of $f_m$ on that set). By Baire, the discontinuity set is meager.

**Key decision point:** The construction of nowhere-dense sets where $\omega_f$ stays large. The key fact: where $f_n$ converges uniformly fast (i.e., $|f_n - f_m| \leq 1/k$ for all $n, m \geq N$), $f$ inherits continuity from the $f_n$'s. So the "oscillation $\geq 1/k$" set lives where this uniform convergence *fails*.

---

# Legal Operations Used

1. **Express the bad set as a meager union.** $\{f \text{ discontinuous}\} = \{\omega_f > 0\} = \bigcup_k \{\omega_f \geq 1/k\}$.

2. **Use uniform convergence at residual points.** On the residual set where $f_n \to f$ uniformly (a Cauchy-in-$n$ condition), $f$ is continuous.

3. **Apply Baire.** The complement (where pointwise convergence fails uniformly) is meager.

---

# Hints

> [!note]- Hint 1
> Define $U_{m, k} := \bigcup_{n \geq m} \{x : d(f_n(x), f_m(x)) > 1/k\}$, an open set. Pointwise convergence implies $\bigcap_m U_{m, k} = \emptyset$.

> [!note]- Hint 2
> By Baire, $\bigcap_m \overline{U_{m, k}}$ is a countable intersection of closed sets, so it's not the whole space unless one of them is. Actually need: $\bigcap_m \overline{U_{m, k}} \subseteq \bigcup_m (\overline{U_{m, k}} - U_{m, k})$, which is a countable union of nowhere dense closed sets (closures minus opens are nowhere dense), hence meager.

> [!note]- Hint 3
> The set where pointwise convergence is uniform of speed $1/k$ — namely the complement of $\bigcap_m \overline{U_{m, k}}$ — is residual. Take the intersection over $k$: residual.

> [!note]- Hint 4
> At a point $y$ where for every $k$ there exists $m_k$ and $\delta_k > 0$ such that $|f_n(x) - f_{m_k}(x)| \leq 1/k$ for $n \geq m_k$ and $d(x, y) < \delta_k$, combined with continuity of $f_{m_k}$, $f$ is continuous at $y$ (by an $\epsilon/3$-argument).

---

# Solution

**Step 1: Set up the relevant open sets.**

For positive integers $m, k$, define
$$U_{m, k} := \bigcup_{n \geq m} \{x \in X : d(f_n(x), f_m(x)) > 1/k\}.$$

This is the set where the sequence $(f_n)$ "hasn't yet" achieved uniform tolerance $1/k$ after stage $m$. Each "$d(f_n(x), f_m(x)) > 1/k$" is open (by continuity of $f_n, f_m$); the union is open.

**Step 2: Pointwise convergence implies $\bigcap_m U_{m, k} = \emptyset$ for each $k$.**

> [!note]- Derivation
> For any $x$, pointwise convergence gives $f_n(x) \to f(x)$, so $(f_n(x))_n$ is Cauchy: there is $m_0(x, k)$ such that $d(f_n(x), f_{m_0}(x)) \leq 1/k$ for all $n \geq m_0$. So $x \notin U_{m_0, k}$. Hence $x \notin \bigcap_m U_{m, k}$. Since this holds for every $x$, $\bigcap_m U_{m, k} = \emptyset$.

**Step 3: $\bigcap_m \overline{U_{m, k}}$ is closed but possibly nonempty. Its decomposition.**

> [!note]- Derivation
> Observe:
> $$\bigcap_m \overline{U_{m, k}} \subseteq \bigcup_m (\overline{U_{m, k}} \setminus U_{m, k}).$$
> *Proof:* if $x \in \bigcap_m \overline{U_{m, k}}$ but $x \notin \bigcup_m (\overline{U_{m, k}} \setminus U_{m, k})$, then for every $m$, $x \in U_{m, k}$. But $\bigcap_m U_{m, k} = \emptyset$ (Step 2). Contradiction.
>
> Each $\overline{U_{m, k}} \setminus U_{m, k}$ is closed (closure of a set minus an open set is closed) with empty interior (a closure minus the corresponding open is the topological boundary, which has empty interior in a complete metric space — actually $\overline{U} - U$ is the boundary $\partial U$ when $U$ is open, and the boundary of an open set is nowhere dense iff... hmm, more careful: $\overline{U} \setminus U = \partial U$, and $\partial U$ has empty interior iff the closure of any nbhd in $\partial U$ hits the open complement of $U$. For open $U$, this is automatic). So each $\overline{U_{m, k}} \setminus U_{m, k}$ is nowhere dense.
>
> Hence $\bigcap_m \overline{U_{m, k}}$ is contained in a countable union of nowhere dense sets, hence meager. By Baire, $X \setminus \bigcap_m \overline{U_{m, k}}$ is residual.

**Step 4: Take the residual set $C := \bigcap_k (X \setminus \bigcap_m \overline{U_{m, k}})$.**

> [!note]- Derivation
> Each $X \setminus \bigcap_m \overline{U_{m, k}}$ is residual (Step 3). The intersection over $k$ is a countable intersection of residual sets, hence residual.

**Step 5: $f$ is continuous at every $y \in C$.**

> [!note]- Derivation
> Fix $y \in C$. For each $k$, $y \notin \bigcap_m \overline{U_{m, k}}$, so there is $m_k$ with $y \notin \overline{U_{m_k, k}}$. So there is $\delta_k > 0$ with $B_{\delta_k}(y) \cap U_{m_k, k} = \emptyset$.
>
> This means: for $x \in B_{\delta_k}(y)$ and $n \geq m_k$, $d(f_n(x), f_{m_k}(x)) \leq 1/k$. Taking $n \to \infty$ and using pointwise convergence: $d(f(x), f_{m_k}(x)) \leq 1/k$.
>
> Now estimate continuity of $f$ at $y$: for $x \in B_{\delta_k}(y)$,
> $$d(f(x), f(y)) \leq d(f(x), f_{m_k}(x)) + d(f_{m_k}(x), f_{m_k}(y)) + d(f_{m_k}(y), f(y)) \leq 1/k + d(f_{m_k}(x), f_{m_k}(y)) + 1/k.$$
>
> By continuity of $f_{m_k}$ at $y$, there is $\delta'_k \leq \delta_k$ with $d(f_{m_k}(x), f_{m_k}(y)) < 1/k$ for $d(x, y) < \delta'_k$. Combining, $d(f(x), f(y)) < 3/k$ for $d(x, y) < \delta'_k$.
>
> So given any $\epsilon > 0$, choose $k > 3/\epsilon$; then $d(x, y) < \delta'_k$ implies $d(f(x), f(y)) < 3/k < \epsilon$. So $f$ is continuous at $y$.

**Step 6: Conclude.**

$C$ is residual in $X$ (Step 4) and $f$ is continuous at every point of $C$ (Step 5). So the continuity set of $f$ is residual.

> [!note]- Complete formal solution
> For each $m, k \in \mathbb{N}_{>0}$, define $U_{m, k} := \bigcup_{n \geq m} \{x : d(f_n(x), f_m(x)) > 1/k\}$, open by continuity of $f_n, f_m$. Pointwise convergence implies $\bigcap_m U_{m, k} = \emptyset$, hence $\bigcap_m \overline{U_{m, k}} \subseteq \bigcup_m (\overline{U_{m, k}} \setminus U_{m, k})$, a countable union of nowhere dense sets (boundaries of opens), hence meager. So $X \setminus \bigcap_m \overline{U_{m, k}}$ is residual.
>
> Let $C := \bigcap_k (X \setminus \bigcap_m \overline{U_{m, k}})$, residual (countable intersection of residuals).
>
> For $y \in C$ and any $k$: choose $m_k$ with $y \notin \overline{U_{m_k, k}}$, and $\delta_k > 0$ with $B_{\delta_k}(y) \cap U_{m_k, k} = \emptyset$. Then for $x \in B_{\delta_k}(y)$ and $n \geq m_k$, $d(f_n(x), f_{m_k}(x)) \leq 1/k$; taking $n \to \infty$, $d(f(x), f_{m_k}(x)) \leq 1/k$. Combined with continuity of $f_{m_k}$ at $y$: $d(f(x), f(y)) \leq 3/k$ for $x$ close to $y$. So $f$ is continuous at $y$.
>
> Hence the continuity set of $f$ contains the residual $C$, so it is residual. $\blacksquare$

---

# Key Takeaways

**Baire class 1 functions are continuous on a dense set.** Functions that are pointwise limits of continuous functions — called **Baire class 1** in descriptive set theory — are continuous on a dense $G_\delta$ subset of their domain. This is a powerful structural result: even though such a function can be discontinuous at many points, its discontinuities form a meager set.

**The "speed of pointwise convergence" varies across the space.** The proof identifies regions where convergence is fast (uniform on a neighborhood) and regions where it is slow. The fast regions are residual; the slow regions are meager. On the fast regions, the limit inherits continuity from the approximating sequence.

**Generalization: Baire's theorem on derivative.** A function $f$ is the derivative of some continuous function $F$ iff... Baire-type analysis classifies derivatives. Specifically, derivatives are Baire class 1, hence continuous on a dense set — so a Riemann-integrable function is "mostly continuous" in the Baire sense.

**Indicator of $\mathbb{Q}$ is NOT a pointwise limit of continuous functions.** The Dirichlet function $\chi_\mathbb{Q}$ (1 on rationals, 0 on irrationals) is discontinuous *everywhere*. So it cannot be a pointwise limit of continuous functions — by the result here, the set of discontinuities would have to be meager, but it's the whole $\mathbb{R}$, not meager. (Note: $\chi_\mathbb{Q}$ is a pointwise limit of pointwise limits of continuous functions, i.e., Baire class 2. The hierarchy is genuine.)

**The trigger-reaction pattern: "Baire + open-dense identification".** This is the standard recipe for many genericity results. Trigger: "want to show some property holds on a dense $G_\delta$ in a Banach space". Reaction: (i) define open sets capturing approximation of the property; (ii) show each is dense; (iii) intersect — Baire gives density of the intersection.

**This generalizes to functions in $\mathcal{B}_1(X, Y)$.** The result holds for any complete metric source $X$ and any metric target $Y$. The proof goes through verbatim. In descriptive set theory, this is the foundational result that Baire class 1 functions are exactly those whose discontinuity set is meager.
