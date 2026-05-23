---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Complete Vector Field"
  - "Def - Flow of a Vector Field"
  - "Thm - Fundamental Theorem on Flows"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $M$ be a smooth manifold and $X \in \mathfrak{X}(M)$ a smooth vector field with **compact support** — i.e. $\operatorname{supp} X := \overline{\{p \in M : X_p \neq 0\}}$ is a compact subset of $M$.

Show that $X$ is **complete**: every maximal integral curve of $X$ is defined for all $t \in \mathbb{R}$.

**Corollary.** Every smooth vector field on a compact manifold is complete.

**Recall:**

A smooth vector field is [[Def - Complete Vector Field|complete]] if its maximal flow has flow domain $\mathcal{D} = \mathbb{R} \times M$, equivalently every maximal integral curve is defined on all of $\mathbb{R}$.

The [[Thm - Fundamental Theorem on Flows|Fundamental Theorem on Flows]] gives existence and uniqueness of the maximal flow; the question is whether the flow domain is all of $\mathbb{R} \times M$ or is strictly smaller.

A smooth vector field with **compact support** is one whose support — the closure of the set where $X$ is nonzero — is compact. On compact manifolds, every smooth vector field has compact support automatically (the support is contained in the compact manifold).

The key lemma is the **Uniform Time Lemma** (Lee Lemma 9.15): if there is some $\varepsilon > 0$ such that for every $p \in M$ the integral curve through $p$ exists at least on $(-\varepsilon, \varepsilon)$, then $X$ is complete.

---

# Convergent Strategy

**Problem class:** Completeness verification — given a vector field with a strong but easily checked structural condition (compact support), conclude the global existence of the flow. The class is "establish completeness from a structural hypothesis"; the route is via the uniform time lemma.

**Assumption pattern:** Compact support $K = \operatorname{supp} X$. By definition, $X$ vanishes off $K$ (well, off the closure of where it is nonzero, but $X$ is identically zero outside $K$ since support is the closure). For points off $K$, integral curves are constant (since $X_p = 0$), hence trivially defined for all $t$. For points in $K$, the integral curve exists locally and we need a uniform existence interval — this is where compactness of $K$ does its work.

**Theorem routing:** [[Thm - Existence and Uniqueness of Integral Curves]] (local existence with smooth dependence) ⟶ uniform time lemma (extract a uniform $\varepsilon$ from compactness of $K$) ⟶ completeness.

**Key decision point:** The non-obvious move is to extract a *uniform* existence time $\varepsilon$ from the local existence times $\varepsilon_p$ obtained at each point. Without compactness, the $\varepsilon_p$ might shrink to zero as $p$ varies, and no uniform bound would exist. Compactness of the support is what licences the open-cover/finite-subcover trick that gives the uniform bound. The choice to apply the lemma to $K$ (not to all of $M$) is also key — for points outside $K$, the vector field is zero, so no positive existence time is needed.

---

# Legal Operations Used

1. **Operation 10 from the topic page (exploit compact support for completeness).** Apply the uniform time lemma to the compact support of $X$. The pattern is to extract from compactness a single $\varepsilon$ bounding the existence time of integral curves through points of the support.

2. **Operation 4 from the topic page (differentiate the flow at $t = 0$ to recover the vector field), implicitly.** Outside the support, $X_p = 0$, so the integral curve through $p$ is the constant curve, which is defined for all $t$. This is the trivial half of completeness.

3. **Operation 3 from the topic page (use the group law of the flow).** Combine the local existence on the bounded interval $(-\varepsilon, \varepsilon)$ with the group law $\phi_{s+t} = \phi_s \circ \phi_t$ to extend the integral curve to all of $\mathbb{R}$ by iteration.

---

# Hints

> [!note]- Hint 1
> Cover the compact support $K$ by finitely many open sets, on each of which Picard–Lindelöf gives a positive existence time. The minimum of these existence times is a *uniform* bound $\varepsilon$ working for every $p \in K$.

> [!note]- Hint 2
> The Uniform Time Lemma (Lee 9.15) says: if every integral curve $\phi^{(p)}$ exists at least on $(-\varepsilon, \varepsilon)$ for some $\varepsilon > 0$ independent of $p$, then $X$ is complete. The proof is to iterate the group law: $\phi_t = \phi_\varepsilon \circ \phi_{t - \varepsilon}$, $\phi_t = \phi_\varepsilon \circ \phi_\varepsilon \circ \phi_{t - 2\varepsilon}$, and so on, extending $\phi_t$ to all $t$.

> [!note]- Hint 3
> For points $p \in M$ with $X_p = 0$ (which includes all points outside $\operatorname{supp} X$), the integral curve is the constant curve $\phi^{(p)}(t) \equiv p$. So existence for all $t$ is automatic there; the real work is at points where $X$ is nonzero.

---

# Solution

The proof has three steps. Step 1 uses local Picard–Lindelöf and compactness of $K = \operatorname{supp} X$ to extract a uniform existence time $\varepsilon > 0$. Step 2 handles points outside $K$, where integral curves are constant. Step 3 invokes the uniform time lemma to conclude completeness. The non-obvious move in Step 1 is the open-cover/finite-subcover step — without compactness, no uniform $\varepsilon$ would exist.

**Step 1: Extract a uniform existence time on the support.**

For each $p \in K = \operatorname{supp} X$, [[Thm - Existence and Uniqueness of Integral Curves]] gives an open neighbourhood $U_p \subseteq M$ of $p$ and $\varepsilon_p > 0$ such that for every $q \in U_p$, the integral curve $\phi^{(q)}$ is defined on $(-\varepsilon_p, \varepsilon_p)$. The family $\{U_p\}_{p \in K}$ is an open cover of $K$. By compactness, extract a finite subcover $U_{p_1}, \dots, U_{p_n}$, and set $\varepsilon := \min(\varepsilon_{p_1}, \dots, \varepsilon_{p_n}) > 0$. Then every integral curve starting in $K$ exists at least on $(-\varepsilon, \varepsilon)$.

> [!note]- Derivation (Step 1)
> By [[Thm - Existence and Uniqueness of Integral Curves]] and the smoothness of the flow in initial conditions, for each $p \in K$ there is an open neighbourhood $U_p \ni p$ and $\varepsilon_p > 0$ such that the flow $\phi$ is defined and smooth on $(-\varepsilon_p, \varepsilon_p) \times U_p$.
>
> $\{U_p\}_{p \in K}$ is an open cover of the compact set $K$. By compactness, finitely many $U_{p_1}, \dots, U_{p_n}$ cover $K$. Set $\varepsilon := \min(\varepsilon_{p_1}, \dots, \varepsilon_{p_n}) > 0$ (the minimum of finitely many positive numbers).
>
> For any $p \in K$, $p$ lies in some $U_{p_k}$, and the integral curve $\phi^{(p)}$ from $p$ is defined at least on $(-\varepsilon_{p_k}, \varepsilon_{p_k}) \supseteq (-\varepsilon, \varepsilon)$.

**Step 2: Handle points off the support.**

For $p \notin K$, $X_p = 0$ (since $K$ is the closure of the set where $X$ is nonzero, and outside the closure $X$ is zero by definition of closure). The constant curve $\phi^{(p)}(t) \equiv p$ satisfies $\gamma'(t) = 0 = X_{\gamma(t)}$, so it is an integral curve from $p$. By uniqueness it is *the* maximal integral curve from $p$, and it is defined for all $t \in \mathbb{R}$.

> [!note]- Derivation (Step 2)
> If $p \notin K$, then $p \notin \overline{\{q : X_q \neq 0\}}$, so $p$ is not a limit point of the set where $X$ is nonzero. By continuity of $X$ and the definition of closure, there is a neighbourhood of $p$ where $X = 0$, so in particular $X_p = 0$.
>
> Define $\gamma : \mathbb{R} \to M$ by $\gamma(t) := p$ (constant). Then $\gamma$ is smooth and $\gamma'(t) = 0 = X_p = X_{\gamma(t)}$ for all $t \in \mathbb{R}$. So $\gamma$ is an integral curve of $X$ on $\mathbb{R}$ starting at $p$, defined for all $t$. By the uniqueness clause of [[Thm - Existence and Uniqueness of Integral Curves]], the maximal integral curve through $p$ is at least as long as $\gamma$ — i.e. its domain $\mathcal{D}^{(p)}$ contains $\mathbb{R}$. So $\mathcal{D}^{(p)} = \mathbb{R}$.

**Step 3: Invoke the uniform time lemma.**

By Steps 1 and 2, every integral curve $\phi^{(p)}$ — whether $p$ is in $K$ or not — is defined at least on $(-\varepsilon, \varepsilon)$ (in fact, on all of $\mathbb{R}$ for $p \notin K$, and at least on $(-\varepsilon, \varepsilon)$ for $p \in K$). The Uniform Time Lemma (Lee Lemma 9.15) then gives completeness.

> [!note]- Derivation (Step 3)
> **Uniform Time Lemma:** Suppose that for every $p \in M$ the integral curve $\phi^{(p)}$ exists at least on $(-\varepsilon, \varepsilon)$. Then $\phi^{(p)}$ exists for all $t \in \mathbb{R}$, i.e. $X$ is complete.
>
> *Proof of the lemma applied here.* Suppose for contradiction that $X$ is not complete; then for some $p$, the maximal interval $\mathcal{D}^{(p)} = (a, b)$ has finite right endpoint $b < \infty$ (or the dual case for the left endpoint; the argument is symmetric).
>
> Pick $t_0$ with $b - \varepsilon < t_0 < b$, and let $q := \phi^{(p)}(t_0)$. By hypothesis, the integral curve $\phi^{(q)}$ exists at least on $(-\varepsilon, \varepsilon)$.
>
> Define $\tilde\gamma : (-\varepsilon, t_0 + \varepsilon) \to M$ by
> $$\tilde\gamma(t) = \begin{cases} \phi^{(p)}(t) & \text{if } -\varepsilon < t < b, \\ \phi^{(q)}(t - t_0) & \text{if } t_0 - \varepsilon < t < t_0 + \varepsilon.\end{cases}$$
> These two definitions agree where they overlap, by the group law: $\phi^{(q)}(t - t_0) = \phi_{t - t_0}(q) = \phi_{t - t_0}(\phi_{t_0}(p)) = \phi_t(p) = \phi^{(p)}(t)$.
>
> So $\tilde\gamma$ is a well-defined integral curve of $X$ through $p$, defined on $(-\varepsilon, t_0 + \varepsilon)$, which strictly contains $(a, b) = \mathcal{D}^{(p)}$ since $t_0 + \varepsilon > b$. This contradicts the maximality of $\phi^{(p)}$.
>
> Hence $\mathcal{D}^{(p)} = \mathbb{R}$ for every $p \in M$, i.e. $X$ is complete.

> [!note]- Complete formal solution
> Let $X \in \mathfrak{X}(M)$ have compact support $K$.
>
> **Step 1 — Uniform existence on the support.** For each $p \in K$, [[Thm - Existence and Uniqueness of Integral Curves]] (with smooth dependence) gives an open neighbourhood $U_p$ of $p$ and $\varepsilon_p > 0$ such that the flow $\phi$ of $X$ is defined and smooth on $(-\varepsilon_p, \varepsilon_p) \times U_p$. The family $\{U_p\}_{p \in K}$ is an open cover of the compact set $K$; choose a finite subcover $U_{p_1}, \dots, U_{p_n}$, and set $\varepsilon = \min_k \varepsilon_{p_k} > 0$. Then for every $q \in K$, the integral curve $\phi^{(q)}$ is defined on $(-\varepsilon, \varepsilon)$.
>
> **Step 2 — Trivial existence off the support.** If $p \notin K$, then $X = 0$ in a neighbourhood of $p$ (by definition of closure), so the constant curve $\phi^{(p)}(t) \equiv p$ is an integral curve of $X$ defined for all $t$. By uniqueness, $\mathcal{D}^{(p)} = \mathbb{R}$.
>
> **Step 3 — Uniform Time Lemma.** From Steps 1 and 2, for every $p \in M$ the integral curve $\phi^{(p)}$ exists at least on $(-\varepsilon, \varepsilon)$ (with $\varepsilon$ from Step 1).
>
> Suppose for contradiction $\mathcal{D}^{(p)} = (a, b)$ for some $p$ with $b < \infty$. Pick $t_0 \in (b - \varepsilon, b)$ and let $q = \phi^{(p)}(t_0)$. The integral curve $\phi^{(q)}$ exists at least on $(-\varepsilon, \varepsilon)$. Define $\tilde\gamma$ on $(-\varepsilon, t_0 + \varepsilon)$ by
> $$\tilde\gamma(t) = \begin{cases} \phi^{(p)}(t) & -\varepsilon < t < b, \\ \phi^{(q)}(t - t_0) & t_0 - \varepsilon < t < t_0 + \varepsilon. \end{cases}$$
> These agree on the overlap by the group law of the flow. Hence $\tilde\gamma$ is an integral curve through $p$ extending past $b$ — contradicting maximality of $\phi^{(p)}$.
>
> Therefore $\mathcal{D}^{(p)} = \mathbb{R}$ for every $p$. $\qquad\blacksquare$
>
> **Corollary.** On a compact manifold $M$, every smooth vector field $X$ has support contained in the compact $M$, so the support is compact. By the theorem, $X$ is complete.

---

# Key Takeaways

**Compactness gives uniform bounds.** This is the standard pattern: pointwise local information (each point has *some* neighbourhood with *some* good property) plus compactness of the parameter set gives uniform information (there is *one* good property working *everywhere*). The pattern recurs throughout analysis: Heine-Borel, uniform continuity from continuity on compact sets, the uniform boundedness principle. The transfer here is from "Picard–Lindelöf gives existence time $\varepsilon_p$ at each $p$" to "there is a single $\varepsilon$ working uniformly". The trigger is "I have a pointwise local existence statement and I want a global existence statement"; the action is "cover compact set, extract finite subcover, take minimum of existence times".

**Outside the support, dynamics are trivial.** A vector field that vanishes on an open set has constant integral curves there — no dynamics whatsoever. The geometric picture is that the "interesting region" is the support, and off the support the flow is the identity. The trigger for this observation: any problem where a vector field is assumed to vanish on a complement, or to have compact support. The action: handle the complement trivially and concentrate the work on the support.

**The Uniform Time Lemma is the standard completeness gateway.** Whenever you want to upgrade local existence to global existence, the route is the Uniform Time Lemma: prove a uniform existence time, then bootstrap via the group law. The lemma is rarely stated explicitly — it is folded into "compactness implies completeness" — but the proof structure of *every* completeness theorem in differential geometry goes through it (compact support, compact manifold, geodesic completeness on compact Riemannian manifolds, completeness of left-invariant vector fields on Lie groups). Recognise the pattern: pointwise local existence + uniform bound + group law iteration = global existence.

**Completeness is a topological property dressed as an analytic one.** The proof requires no estimate on $X$, no Lipschitz constant calculation, no integral inequality — just the topological fact that the support is compact. This contrasts sharply with the alternative completeness criterion "sublinear growth on $\mathbb{R}^n$", which is purely analytic. Both kinds of criterion exist, but the compactness criterion is the more robust one for manifold geometry, because compactness translates immediately across diffeomorphisms while growth rates do not. This is one reason differential geometry is so much cleaner than the analysis of ODEs on $\mathbb{R}^n$: the topological setting gives strong completeness theorems for free.
