---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Local Maximum Modulus Principle"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$D \subseteq \mathbb{C}$ a bounded domain; $f : D \to \mathbb{C}$ holomorphic and continuous on $\overline D$. $\partial D$ — the boundary; $\overline D$ — the closure. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

The global maximum modulus principle is the natural propagation of the local version: if $f$ is holomorphic on a bounded domain, continuous on the closure, then the maximum of $|f|$ on $\overline D$ is attained *on the boundary $\partial D$*. The maximum *can* be attained inside, but only if $f$ is constant.

This is the workhorse of complex-analytic inequalities. Bounds on $|f|$ throughout $D$ reduce to bounds on $\partial D$, and one can often estimate $|f|$ on the boundary much more easily than in the interior.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on bounded $D$, continuous on $\overline D$".

The first disguised source is **$f$ continuous on $\overline D$, holomorphic on $D$ (the interior)**: very common. Often a function defined by an integral or limit, known to be continuous on the closure but only holomorphic inside.

**Targets (Output Amplification)**

The conclusion is "$\max_{\overline D} |f| = \max_{\partial D} |f|$, with strict inequality on the interior unless $f$ is constant".

Combine with **boundary bounds.** Property $D$: a bound on $\partial D$. The amplified result: same bound throughout $D$. Used to prove $f$ has small magnitude in $D$ when it does on the boundary.

Combine with **Schwarz lemma.** Property $D$: a holomorphic $f : D(0, 1) \to D(0, 1)$ with $f(0) = 0$. The amplified result: $|f(z)| \leq |z|$ via max modulus applied to $f(z)/z$.

Combine with **uniqueness theorems.** Property $D$: two holomorphic functions with the same boundary values. The amplified result: they are equal — apply max modulus to the difference.

---

# Why Is It True

$\overline D$ is compact (closed and bounded). $|f|$ is continuous on $\overline D$, hence attains its max at some $z^* \in \overline D$.

Case 1: $z^* \in \partial D$. The max is on the boundary. Done.

Case 2: $z^* \in D$ (interior). Then $|f|$ has a local max at $z^*$ in the open set $D$. By [[Thm - Local Maximum Modulus Principle]] applied at $z^*$, $f$ is constant on a disc around $z^*$. By the identity theorem (or by extending the argument via the connectedness of $D$ — see [[Thm - Constant on a Domain if Derivative is Zero]] applied to $f - f(z^*)$, which has zero derivative on a disc hence on all of $D$), $f$ is constant on all of $D$. By continuity, $f$ is constant on $\overline D$, so the max on $\overline D$ equals the max on $\partial D$ (both equal $|f(z^*)|$).

In either case, the max on $\overline D$ equals the max on $\partial D$.

---

# What Makes This Hard

The non-obvious step is the propagation from "$f$ constant on a disc around the interior max" to "$f$ constant on $D$" — this uses connectedness. Once that is granted (via [[Thm - Constant on a Domain if Derivative is Zero]] or the identity theorem), the result is automatic.

---

# Rederivation Scaffold

**High-level strategy:**
Compactness gives a max on $\overline D$. If interior, local max modulus gives $f$ constant on a disc, propagate to $D$ by connectedness, conclude $f$ constant.

**Subgoal decomposition:**

1. **Compactness:** $|f|$ attains its max on $\overline D$.
2. **If max on boundary:** done.
3. **If max in interior:** apply local max modulus + connectedness; $f$ constant on $D$, hence on $\overline D$.

---

# Lemma Decomposition

(No new lemmas beyond [[Thm - Local Maximum Modulus Principle]].)

---

# Formal Proof

> [!note]- Complete formal proof
> $\overline D$ is closed and bounded in $\mathbb{C}$ (a metric space), hence compact. $|f|$ is continuous on $\overline D$, so by extreme value theorem $|f|$ attains its max at some $z^* \in \overline D$ with $|f(z^*)| = \max_{\overline D}|f|$.
>
> If $z^* \in \partial D$, the max equals $\max_{\partial D}|f|$.
>
> If $z^* \in D$ (interior), choose $r > 0$ with $D(z^*, r) \subseteq D$. Then $|f(z)| \leq |f(z^*)|$ for $z \in D(z^*, r)$, so $|f|$ has a local max at $z^*$. By [[Thm - Local Maximum Modulus Principle]], $f$ is constant on $D(z^*, r)$.
>
> Let $S = \{z \in D : f(z) = f(z^*)\}$. $S$ is nonempty ($z^* \in S$), closed in $D$ (continuity), and open in $D$ (by the local max modulus argument repeated at each point of $S$). By connectedness of $D$, $S = D$. So $f \equiv f(z^*)$ on $D$.
>
> By continuity on $\overline D$, $f \equiv f(z^*)$ on $\overline D$. Hence $\max_{\partial D}|f| = |f(z^*)| = \max_{\overline D}|f|$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Uniqueness of boundary value problems.** Two holomorphic $f, g$ on $D$ continuous on $\overline D$ with $f = g$ on $\partial D$: apply max modulus to $f - g$, get $|f - g| \leq \max_{\partial D}|f - g| = 0$ throughout $D$. So holomorphic functions are determined by boundary values — a strong form of uniqueness.

**Schwarz lemma.** Map $D(0, 1) \to D(0, 1)$ holomorphically with $f(0) = 0$: define $g(z) = f(z)/z$, holomorphic on $D(0, 1)$ (removable singularity at $0$). On $|z| = 1 - \varepsilon$, $|g| \leq 1/(1 - \varepsilon)$. Max modulus: $|g| \leq 1/(1 - \varepsilon)$ on $|z| \leq 1 - \varepsilon$; let $\varepsilon \to 0$: $|g| \leq 1$ on $D(0, 1)$, so $|f(z)| \leq |z|$.

---

# Bridges

- **[[Thm - Local Maximum Modulus Principle]]** — the local version, propagated.

- **[[Thm - Constant on a Domain if Derivative is Zero]]** — used for the connectedness argument.

- **[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]** — provides the same kind of "extend from a small set to a domain" propagation.
