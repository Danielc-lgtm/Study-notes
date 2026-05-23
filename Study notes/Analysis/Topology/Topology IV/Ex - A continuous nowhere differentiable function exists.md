---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Baire Category Theorem"
  - "Def - Nowhere Dense and Meager"
  - "Def - Cauchy Sequence and Complete Metric Space"
tags: [analysis, topology, baire, functional-analysis, nowhere-differentiable]
---

# Problem Statement

Let $C[0, 1]$ denote the Banach space of continuous functions $f : [0, 1] \to \mathbb{R}$ with the supremum norm $\|f\|_\infty = \sup_{t \in [0, 1]} |f(t)|$.

Show that the set of functions $f \in C[0, 1]$ that are **nowhere differentiable** on $[0, 1]$ is residual (and hence dense) in $C[0, 1]$. In particular, such functions exist.

**Recall:**

$C[0, 1]$ is a [[Def - Cauchy Sequence and Complete Metric Space|complete metric space]] with the uniform metric (in fact, a Banach space). The [[Thm - Baire Category Theorem|Baire category theorem]] applies: $C[0, 1]$ is not meager in itself, so any meager subset has dense complement.

A "residual" set is the complement of a meager set; equivalently, it contains a countable intersection of dense open sets.

---

# Convergent Strategy

**Problem class:** Use Baire's theorem to show existence of an object with a "rare" property (here, nowhere differentiability), without constructing it explicitly.

**Assumption pattern:** Differentiability of $f$ at a single point $t_0$ would force, for nearby $s$, $|f(t) - f(s)| / |t - s|$ to be bounded (close to $f'(t_0)$). This is a local condition. The set of $f$ differentiable *anywhere* is the union over $t_0$ of "differentiable at $t_0$" — a small set if the local conditions are sufficiently restrictive.

**Theorem routing:** Define, for each integer $n$, the set $U_n := \{f \in C[0,1] : \forall t \in [0,1], \exists s \neq t \text{ with } |(f(t) - f(s))/(t - s)| > n\}$. Show: (a) $U_n$ is open; (b) $U_n$ is dense. By Baire, $\bigcap U_n$ is residual; every $f \in \bigcap U_n$ is nowhere differentiable (since differentiability at $t$ would give a uniform bound on difference quotients, contradicting $U_n$ for large $n$).

**Key decision point:** The choice of $U_n$ — capturing "the function is sufficiently kinky everywhere" — is essential. Density comes from approximating any continuous function by piecewise linear "zig-zag" functions; openness comes from the openness of "the difference quotient is large at some $s$".

---

# Legal Operations Used

1. **Identify "bad" set as countable intersection of open dense.** The functions *differentiable somewhere* form a meager set, written as a countable union of nowhere dense sets.

2. **Open-dense via density of zig-zag functions.** Any continuous function can be approximated by zig-zag functions with arbitrarily steep slopes.

3. **Apply Baire to conclude residuality.** Intersection of countably many dense opens is residual; in particular dense, in particular nonempty.

---

# Hints

> [!note]- Hint 1
> Define $U_n := \{f \in C[0, 1] : \forall t \in [0, 1], \exists s \neq t \text{ in } [0, 1] \text{ with } |(f(t) - f(s))/(t - s)| > n\}$. (Bredon's Corollary 17.6.)

> [!note]- Hint 2
> Openness of $U_n$: if $f \in U_n$, then for each $t$ there is $s_t \neq t$ with the difference quotient large. The condition "this quotient is $> n$" is open in $f$. Use a finite cover of $[0, 1]$ by neighborhoods (compactness) to make the bound uniform.

> [!note]- Hint 3
> Density of $U_n$: given any $f \in C[0, 1]$ and $\epsilon > 0$, construct a zig-zag function $g$ within $\epsilon$ of $f$ with slopes everywhere $> n$. By uniform continuity of $f$, choose a fine grid; build $g$ as a sawtooth with peaks/troughs alternating quickly enough.

> [!note]- Hint 4
> Conclude: by Baire, $\bigcap_n U_n$ is residual. Every $f \in \bigcap U_n$ is nowhere differentiable: if $f$ were differentiable at $t$ with $f'(t) = L$, then $\lim_{s \to t} (f(s) - f(t))/(s - t) = L$, so the difference quotient is bounded near $t$, contradicting $f \in U_n$ for $n > |L| + 1$.

---

# Solution

The proof breaks into five steps that execute the standard Baire-genericity template. Step 1 defines $U_n$ as the set of functions whose difference quotients exceed $n$ at some witness near every point; Step 2 shows $U_n$ is open via strict-inequality stability and a finite subcover using compactness of $[0,1]$; Step 3 shows $U_n$ is dense via zig-zag approximation, where any continuous function is uniformly approximated by a sawtooth with arbitrarily steep slopes; Step 4 invokes Baire to conclude $\bigcap U_n$ is residual; Step 5 verifies that membership in $\bigcap U_n$ contradicts differentiability at any point. The non-obvious move is in Step 3 — the zig-zag construction simultaneously approximates uniformly *and* enforces large local slopes, which is what couples "dense in $C[0,1]$" to "kinky everywhere."

**Step 1: Define the candidate residual set.**

For each positive integer $n$, define
$$U_n := \left\{ f \in C[0, 1] : \forall t \in [0, 1], \exists s \neq t \text{ in } [0, 1] \text{ with } \left|\frac{f(t) - f(s)}{t - s}\right| > n \right\}.$$

The claim: $\bigcap_{n \geq 1} U_n$ is residual in $C[0, 1]$, and every function in this intersection is nowhere differentiable.

**Step 2: $U_n$ is open in $C[0, 1]$.**

> [!note]- Derivation
> Fix $f \in U_n$. By definition, for each $t$, there is $s_t \neq t$ with $|(f(t) - f(s_t))/(t - s_t)| > n$. The quotient is *strictly* greater than $n$, so there is some margin: $|(f(t) - f(s_t))/(t - s_t)| > n + \epsilon(t)$ for some $\epsilon(t) > 0$.
>
> By continuity of $f$, the open condition $|(g(t) - g(s_t))/(t - s_t)| > n + \epsilon(t)/2$ holds for all $g$ in a neighborhood of $f$. Specifically: if $\|g - f\|_\infty < \delta(t)$ for sufficiently small $\delta(t)$, the quotient changes by less than $\epsilon(t)/2$ in any region where $|t - s_t| \geq c$ for some $c > 0$.
>
> Apply this to each $t$, and use a finite subcover (compactness of $[0, 1]$): there are finitely many points $t_1, \dots, t_k$ with neighborhoods $V_i \subseteq [0, 1]$ covering $[0, 1]$, and the "$s_{t_i}$"-witness gives a strict inequality $> n + \epsilon_i/2$ uniform for $g$ within $\delta_i$ of $f$. Let $\delta := \min_i \delta_i$; then for $g$ within $\delta$ of $f$, each $g$ has a witness for each $t$ (using the witness $s_{t_i}$ for $t \in V_i$ with appropriate constant), so $g \in U_n$.
>
> Hence $U_n$ is open.

**Step 3: $U_n$ is dense in $C[0, 1]$.**

> [!note]- Derivation
> Given $f \in C[0, 1]$ and $\epsilon > 0$. We construct $g \in U_n$ with $\|g - f\|_\infty < \epsilon$.
>
> Choose $m$ large so that $1/m < \epsilon$. By uniform continuity of $f$ on $[0, 1]$ (compact), there is $k$ such that $|x - y| < 1/k \implies |f(x) - f(y)| < 1/m$. Take $k$ further so that $k > nm$, i.e., the slope $1/(1/k) = k > nm$ allows us to push the zig-zag slopes high.
>
> Divide $[0, 1]$ into $k$ subintervals of length $1/k$: $[a_i, a_{i+1}]$ with $a_i = i/k$. On each $[a_i, a_{i+1}]$, define a sawtooth: $g$ takes value $y_i := f(a_i)$ at $a_i$, drops to $y_i - 1/m$ at the midpoint of $[a_i, a_i + 1/(3k)]$, rises back through $y_i$ and to $y_i + 1/m$ at the midpoint of $[a_i + 2/(3k), a_{i+1}]$, then linearly to $y_{i+1} := f(a_{i+1})$.
>
> *Uniform bound:* $|g(t) - f(t)| \leq |g(t) - y_i| + |y_i - f(t)| \leq 1/m + 1/m = 2/m < \epsilon$ (after taking $m$ large enough). So $\|g - f\|_\infty < \epsilon$.
>
> *Steep slopes:* on each segment of length $1/(3k)$, $g$ varies by $1/m$. Slope = $(1/m)/(1/(3k)) = 3k/m > 3n$. So for any $t \in [a_i, a_{i+1}]$, choose $s =$ adjacent kink point; then $|g(t) - g(s)|/|t - s|$ is at least $n$ (a bit more, by the slope).
>
> Hence $g \in U_n$, and $\|g - f\|_\infty < \epsilon$. So $U_n$ is dense.

**Step 4: Conclude $\bigcap U_n$ is residual.**

> [!note]- Derivation
> $C[0, 1]$ is a complete metric space. Each $U_n$ is open and dense (Steps 2, 3). By [[Thm - Baire Category Theorem]] (in the form "countable intersection of dense opens is dense"), $\bigcap_n U_n$ is dense. Its complement, the union of meager sets $C[0, 1] \setminus U_n$, is meager. So $\bigcap U_n$ is residual.

**Step 5: Every $f \in \bigcap U_n$ is nowhere differentiable.**

> [!note]- Derivation
> Suppose $f \in \bigcap_n U_n$ and $f$ is differentiable at some $t_0$. Then $f'(t_0) = L$ for some $L \in \mathbb{R}$, meaning $\lim_{s \to t_0} (f(s) - f(t_0))/(s - t_0) = L$. So $|(f(s) - f(t_0))/(s - t_0)|$ is bounded near $t_0$ — say, $\leq |L| + 1$ for $s$ in some neighborhood of $t_0$.
>
> But $f \in U_n$ for every $n$, so for any $n$ there is $s_n \neq t_0$ with $|(f(t_0) - f(s_n))/(t_0 - s_n)| > n$. Taking $n > |L| + 1$ gives a contradiction (the bound from differentiability would limit the quotient to $\leq |L| + 1$ for $s_n$ near $t_0$, but the quotient is $> n > |L| + 1$, so $s_n$ must be *bounded away* from $t_0$ — but then we need to consider the full $[0, 1]$, and the supremum of $|(f(t_0) - f(s))/(t_0 - s)|$ over $s$ in $[0, 1] \setminus \{t_0\}$ is *finite* by continuity of $f$ on the compact $[0, 1]$. Specifically, for $|s - t_0|$ bounded below by $\delta > 0$, the difference quotient is $\leq 2 \|f\|_\infty / \delta$, bounded. So the supremum is finite, contradicting the requirement $> n$ for every $n$.)
>
> Hence $f$ has no point of differentiability. $f$ is nowhere differentiable.

> [!note]- Complete formal solution
> Define $U_n \subseteq C[0, 1]$ as in Step 1. Each $U_n$ is open (Step 2) and dense (Step 3, by approximation with zig-zag functions). By [[Thm - Baire Category Theorem]] applied to the complete metric space $C[0, 1]$, $\bigcap_n U_n$ is residual (dense). Every $f \in \bigcap U_n$ is nowhere differentiable (Step 5). In particular, such $f$ exists. $\blacksquare$
>
> *Explicit example (Weierstrass):* the function $W(x) = \sum_{n=0}^\infty a^n \cos(b^n \pi x)$ with $0 < a < 1$ and $ab > 1 + 3\pi/2$ is continuous and nowhere differentiable (proved by Weierstrass directly, without Baire). Baire gives existence; Weierstrass gives a constructive example.

---

# Key Takeaways

**Baire gives existence of "exotic" objects.** This is the prototype "generic = strange" theorem in analysis: the "typical" continuous function is nowhere differentiable, even though our intuition (built from polynomials, exponentials, sines) suggests smooth functions are the norm. The lesson: smoothness is *atypical* — it's a strong condition satisfied by a meager set.

**The technique: bad set = countable union of nowhere-dense, complement is residual.** Trigger-reaction pattern: "want to show some property holds for a 'generic' element in a Banach space $\Rightarrow$ (i) write the bad set as a countable union of closed sets with empty interior; (ii) apply Baire". This proves generic continuous functions are nowhere differentiable, generic measurable functions have bad pointwise behavior, generic dynamical systems have minimal closed invariant sets, and many other "genericity" statements.

**Openness from continuity + compactness.** The set $U_n$ is open because the condition "$|f(t) - f(s_t)|/|t - s_t| > n$ at some $s_t \neq t$" is a *strict* inequality that survives small perturbations in $f$. Compactness of $[0, 1]$ is essential: it allows a finite subcover to make the perturbation bound uniform across all $t$.

**Density from zig-zag approximation.** The key analytic step: any continuous function is approximated uniformly by a zig-zag (sawtooth) function with arbitrarily steep slopes. The zig-zag function necessarily has difference quotients arbitrarily large on every interval, so it lies in $U_n$ for any $n$. This is the "constructive" content: any continuous function is close to a "kinky" one.

**Baire-generic vs. measure-generic.** The Baire-residual set of nowhere differentiable functions is large in the topological sense. In contrast, in measure-theoretic terms: with the Wiener measure on $C[0, 1]$ (Brownian motion measure), almost-every continuous function (measure-1) is nowhere differentiable. The two notions of "generic" agree in this case, but they can differ. *Example:* the set of normal numbers in $[0, 1]$ is measure-$1$ but Baire-meager.
