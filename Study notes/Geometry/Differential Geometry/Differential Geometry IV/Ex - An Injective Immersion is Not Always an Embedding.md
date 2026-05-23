---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Immersion, Submersion, and Embedding"
  - "Def - Embedded Submanifold"
  - "Def - Immersed Submanifold"
  - "Def - Subspace Topology"
tags: [geometry, differential-geometry]
---

# Problem Statement

Show by example that an **injective smooth immersion** need not be a **smooth embedding**: exhibit a smooth manifold $N$, a smooth manifold $M$, and a smooth map $F : N \to M$ such that
1. $F$ is injective;
2. $F$ is a smooth immersion (i.e., $dF_p$ is injective at every $p \in N$);
3. $F$ is *not* a smooth embedding — that is, $F$ is not a [[Def - Homeomorphism|homeomorphism]] onto its image $F(N)$ in the [[Def - Subspace|subspace]] topology of $M$.

Two canonical examples are requested: the **figure-eight curve** (compact image, non-compact domain) and the **irrational line on the torus** (dense image). Explain in each case which aspect of "embedding" fails.

**Recall:**

A **smooth embedding** $F : N \to M$ is a smooth immersion that is a homeomorphism onto its image (with the [[Def - Subspace Topology|subspace topology]] from $M$).

By [[Def - Immersion, Submersion, and Embedding|Lee's Proposition 4.22]], an injective smooth immersion is automatically an embedding when (a) it is an open or closed map, (b) it is a proper map, or (c) the domain $M$ is compact. So failure of embedding requires the domain to be non-compact and the map to fail to be proper / closed / open.

---

# Convergent Strategy

**Problem class:** This is a counterexample-construction exercise — show that the "injective immersion ⟹ embedding" implication fails without additional hypotheses. The standard counterexamples come from "doubling back" of the parametrisation (figure-eight) or "wrapping densely" (irrational line on torus).

**Assumption pattern:** Both examples are smooth curves on $\mathbb{R}^2$ or $T^2$, given by explicit smooth parametrisations from $\mathbb{R}$ (or a sub-interval) into the target. Each is injective (no two distinct parameter values give the same point) and immersive (the derivative never vanishes). The failure of embedding comes from a *topological* mismatch: the subspace topology of the image disagrees with the domain topology.

**Theorem routing:** For each example, the strategy is:
1. Write down the smooth parametrisation explicitly.
2. Verify injectivity and immersion by direct computation.
3. Find a sequence in the domain whose image converges in the subspace topology to a point that *is* in the image, but whose preimages do not converge in the domain topology — this exhibits the topological mismatch.

**Key decision point:** The non-obvious step is *constructing* the bad sequence — picking points whose images cluster near the "problem point" but whose preimages diverge. For the figure-eight, the problem point is the self-intersection at the origin; for the irrational line, the problem is that the image is dense, so any "open arc" in the subspace topology is dense rather than locally Euclidean. The choice of bad sequence is what makes the counterexample work.

---

# Legal Operations Used

1. **Operation 1 (compute the differential in coordinates):** verifying injectivity of the parametrisation's differential is the immersion-check step. For the figure-eight $\beta(t) = (\sin 2t, \sin t)$, the velocity is $\beta'(t) = (2\cos 2t, \cos t)$, which is never zero on $(-\pi, \pi)$. For the irrational line $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$, the velocity is $(2\pi i e^{2\pi i t}, 2\pi i \alpha e^{2\pi i \alpha t})$, with components nonzero.

2. **The contrapositive of operation 6 (compact-domain criterion is the rescue, and its absence is the failure mode):** both counterexamples have non-compact domains (the figure-eight uses $(-\pi, \pi) \cong \mathbb{R}$; the irrational line uses $\mathbb{R}$). Compactness of the domain would force embedding, so the counterexamples must have non-compact domain.

---

# Hints

> [!note]- Hint 1
> A smooth embedding is a smooth immersion that is also a *topological embedding* — a homeomorphism onto its image (subspace topology). Failure of embedding means the domain topology and the subspace-topology-on-image disagree.

> [!note]- Hint 2
> For the figure-eight: consider $\beta : (-\pi, \pi) \to \mathbb{R}^2$, $\beta(t) = (\sin 2t, \sin t)$. Plot the image. What happens as $t \to \pm \pi$? Do those limits give a point in the image?

> [!note]- Hint 3
> For the irrational line: consider $\gamma : \mathbb{R} \to T^2 = S^1 \times S^1$, $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$ for irrational $\alpha$. By Dirichlet's approximation theorem or Weyl equidistribution, $\gamma(\mathbb{Z})$ is dense in $T^2$. What does this say about the subspace topology on the image?

> [!note]- Hint 4
> In each case, find a sequence $(t_n)$ in the domain such that $\beta(t_n)$ or $\gamma(t_n)$ converges in the subspace topology of the target, but $(t_n)$ does *not* converge in the domain topology. This shows the subspace topology has "more convergent sequences" than the domain topology, contradicting "homeomorphism onto image".

---

# Solution

The proof breaks into two examples. The first (figure-eight) shows non-properness via a sequence converging to a "boundary" limit. The second (irrational line) shows non-properness via density.

**Example 1: The figure-eight curve.**

Define $\beta : (-\pi, \pi) \to \mathbb{R}^2$ by $\beta(t) = (\sin 2t, \sin t)$.

> [!note]- Derivation
> *$\beta$ is smooth.* Both components are smooth functions of $t$.
>
> *$\beta$ is injective on $(-\pi, \pi)$.* Suppose $\beta(t_1) = \beta(t_2)$ for $t_1, t_2 \in (-\pi, \pi)$. Then $\sin t_1 = \sin t_2$ and $\sin 2t_1 = \sin 2t_2$. From $\sin t_1 = \sin t_2$: either $t_1 = t_2$ (we're done), or $t_1 + t_2 = \pi$ (or $-\pi$, but both must be in $(-\pi, \pi)$, so $t_1 + t_2 \in (-2\pi, 2\pi) \setminus \{-\pi\}$ if $t_1, t_2 \neq -\pi$ — and we exclude $-\pi$ from the domain). If $t_1 + t_2 = \pi$, then $2t_1 + 2t_2 = 2\pi$, so $\sin 2t_1 = -\sin 2t_2$ (because $\sin(2\pi - \theta) = -\sin \theta$, so $\sin 2t_2 = \sin(2\pi - 2t_1) = -\sin 2t_1$). Combined with $\sin 2t_1 = \sin 2t_2$, this gives $\sin 2t_1 = -\sin 2t_1$, i.e., $\sin 2t_1 = 0$, so $t_1 \in \{0, \pi/2, -\pi/2, \dots\}$. Checking each case (and noting $t_1 + t_2 = \pi$): if $t_1 = 0$, then $t_2 = \pi$, outside the domain; if $t_1 = \pi/2$, then $t_2 = \pi/2 = t_1$; if $t_1 = -\pi/2$, then $t_2 = 3\pi/2$, outside. So $t_1 = t_2$, proving injectivity.
>
> *$\beta$ is an immersion.* The velocity is $\beta'(t) = (2\cos 2t, \cos t)$. This vanishes iff $\cos 2t = 0$ and $\cos t = 0$. From $\cos t = 0$: $t = \pm \pi/2$. From $\cos 2t = 0$: $2t = \pm \pi/2 + k\pi$, i.e., $t = \pm \pi/4 + k\pi/2$. The intersection is empty: $\pm \pi/2$ is not of the form $\pm \pi/4 + k\pi/2$. So $\beta'(t) \neq 0$ for all $t \in (-\pi, \pi)$, and $\beta$ is an immersion.
>
> *$\beta$ is NOT a topological embedding.* Consider the sequences $t_n^- = -\pi + 1/n$ and $t_n^+ = \pi - 1/n$ in $(-\pi, \pi)$. As $n \to \infty$, both sequences converge to the boundary of $(-\pi, \pi)$ — but neither converges *in* $(-\pi, \pi)$. Their images:
> $$\beta(t_n^\pm) = (\sin(2(\pm\pi - 1/n)), \sin(\pm\pi - 1/n)) = (\sin(\mp 2/n), \mp\sin(1/n)) \to (0, 0) \text{ as } n \to \infty.$$
> So $\beta(t_n^-) \to (0,0)$ and $\beta(t_n^+) \to (0, 0)$ in the subspace topology on $\beta((-\pi, \pi))$. But $(0, 0) = \beta(0)$ is in the image, and the *domain* preimages $t_n^\pm$ do not converge to $0$ — they converge to $\pm \pi$, outside the domain.
>
> If $\beta$ were a topological embedding onto its image, then $\beta(t_n^\pm) \to (0, 0)$ in the subspace topology would force $t_n^\pm \to 0$ in the domain topology (the inverse $\beta^{-1}$ would have to be continuous). But $t_n^\pm \to \pm \pi$, not $0$. Contradiction. So $\beta$ is not a topological embedding, and hence not a smooth embedding.

**Example 2: The irrational line on the torus.**

Let $\alpha \in \mathbb{R} \setminus \mathbb{Q}$ (an irrational number). Define $\gamma : \mathbb{R} \to T^2 = S^1 \times S^1$ by $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$.

> [!note]- Derivation
> *$\gamma$ is smooth.* Both components are smooth functions of $t$.
>
> *$\gamma$ is injective.* If $\gamma(t_1) = \gamma(t_2)$, then $e^{2\pi i t_1} = e^{2\pi i t_2}$ and $e^{2\pi i \alpha t_1} = e^{2\pi i \alpha t_2}$. The first gives $t_1 - t_2 \in \mathbb{Z}$; the second gives $\alpha(t_1 - t_2) \in \mathbb{Z}$. Substituting $t_1 - t_2 = k \in \mathbb{Z}$: $\alpha k \in \mathbb{Z}$. If $k \neq 0$, $\alpha = (\alpha k)/k$ would be rational, contradicting irrationality. So $k = 0$, i.e., $t_1 = t_2$.
>
> *$\gamma$ is an immersion.* The velocity is $\gamma'(t) = (2\pi i e^{2\pi i t}, 2\pi i \alpha e^{2\pi i \alpha t})$. Both components are nonzero (they have absolute value $2\pi$ and $2\pi|\alpha|$ respectively), so $\gamma'(t) \neq 0$. Hence $\gamma$ is an immersion.
>
> *$\gamma$ is NOT a topological embedding.* The image $\gamma(\mathbb{R}) \subseteq T^2$ is *dense* in $T^2$. This is a consequence of **Dirichlet's approximation theorem**: for any $\varepsilon > 0$, there exist integers $n, m$ with $|n\alpha - m| < \varepsilon$, so $\gamma(n) = (e^{2\pi i n}, e^{2\pi i \alpha n}) = (1, e^{2\pi i \alpha n})$ where $e^{2\pi i \alpha n}$ is arbitrarily close to $1$. So $(1, 1) = \gamma(0)$ is a limit of $\gamma(n)$ as $n \to \infty$ through a suitable sequence of integers with $|n\alpha - m| \to 0$. But $\mathbb{Z}$ has no limit point in $\mathbb{R}$ (as a discrete subset), so the preimages $n$ do not converge in $\mathbb{R}$.
>
> More carefully: pick a sequence $n_k \in \mathbb{Z}$ with $|n_k| \to \infty$ but $|n_k \alpha - m_k| \to 0$ for suitable integers $m_k$ (exists by Dirichlet). Then $\gamma(n_k) \to \gamma(0) = (1, 1)$ in the subspace topology of $T^2$, but $n_k$ does not converge in $\mathbb{R}$ (it tends to $\pm\infty$). If $\gamma$ were a topological embedding, the convergence in the subspace topology would force convergence in the domain topology, contradiction. So $\gamma$ is not a topological embedding.
>
> *Both $\gamma$ is an immersed submanifold structure on its image* with the topology from $\mathbb{R}$ (rather than the subspace topology from $T^2$), making $\gamma$ a [[Def - Diffeomorphism|diffeomorphism]] onto its image as an *immersed* (not embedded) submanifold of $T^2$. The dense embedding fails; the immersed structure succeeds.

> [!note]- Complete formal solution
>
> **Example 1 (figure-eight).** Define $\beta : (-\pi, \pi) \to \mathbb{R}^2$ by $\beta(t) = (\sin 2t, \sin t)$.
>
> *Smoothness:* both components are smooth in $t$.
>
> *Injectivity:* Suppose $\beta(t_1) = \beta(t_2)$ with $t_1, t_2 \in (-\pi, \pi)$. Then $\sin t_1 = \sin t_2$ and $\sin 2t_1 = \sin 2t_2$. The first gives $t_2 = t_1$ or $t_2 = \pi - t_1$ (mod $2\pi$); the second restricts further to $t_1 = t_2$.
>
> *Immersion:* $\beta'(t) = (2\cos 2t, \cos t)$. Both components zero simultaneously requires $\cos t = 0$ and $\cos 2t = 0$; the first gives $t = \pm\pi/2$, the second gives $t = \pm\pi/4 + k\pi/2$. No common value, so $\beta'(t) \neq 0$ for all $t$.
>
> *Not an embedding:* The sequence $t_n = \pi - 1/n$ has $\beta(t_n) \to (0,0) = \beta(0)$ in $\mathbb{R}^2$, while $t_n \to \pi \notin (-\pi, \pi)$ — so $\beta^{-1}$ (as a map from $\beta((-\pi,\pi))$ with the subspace topology to $(-\pi, \pi)$) is not continuous at $(0, 0)$. Hence $\beta$ is not a topological embedding.
>
> **Example 2 (irrational line on the torus).** For irrational $\alpha$, define $\gamma : \mathbb{R} \to T^2 = S^1 \times S^1$ by $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$.
>
> *Smoothness:* clear from the formula.
>
> *Injectivity:* $\gamma(t_1) = \gamma(t_2)$ implies $t_1 - t_2 \in \mathbb{Z}$ and $\alpha(t_1 - t_2) \in \mathbb{Z}$. Setting $k = t_1 - t_2$: $\alpha k \in \mathbb{Z}$. If $k \neq 0$, $\alpha$ is rational — contradiction. So $t_1 = t_2$.
>
> *Immersion:* $|\gamma'(t)| = 2\pi \sqrt{1 + \alpha^2} \neq 0$ for all $t$.
>
> *Not an embedding:* By Dirichlet's approximation theorem, for any $\varepsilon > 0$ there exist integers $n, m$ with $|n\alpha - m| < \varepsilon$. Then $\gamma(n) = (1, e^{2\pi i n \alpha}) = (1, e^{2\pi i (n\alpha - m)}) \to (1, 1) = \gamma(0)$ as $n \to \infty$ through such integers. But the integers $n$ do not converge in $\mathbb{R}$. So $\gamma^{-1}$ is not continuous at $(1, 1)$, hence $\gamma$ is not a topological embedding.
>
> $\qquad\blacksquare$

---

# Key Takeaways

**Immersion + injection is not embedding — the topology matters.** Smoothness and injectivity at the differential and point levels are *not* enough for embedding. The topological condition "homeomorphism onto image" requires the subspace topology and the domain topology to agree, which can fail in two distinct ways: (a) the domain has a "boundary" the parametrisation approaches but never reaches (figure-eight), and (b) the image is dense in the target (irrational line). Both failures are topological, not differential, and they remind us that embedding is a topological strengthening of immersion. The rescues: compact domain, properness, or open/closed map status; absent these, the failure can occur.

**Compactness as the universal rescue.** The condition "$M$ is compact" is the most common way to rescue "injective immersion ⟹ embedding". The reason: a continuous injective map from a compact space to a Hausdorff space is automatically a homeomorphism onto its image, by the closed map lemma. The figure-eight uses $(-\pi, \pi)$ — non-compact — and that is exactly what allows the boundary-limit failure. If we restricted the figure-eight to $[-\pi/2, \pi/2]$ (compact), the resulting map *would* be an embedding (onto a single arc, not the full figure-eight).

**Density of the irrational line — a Lie-theoretic phenomenon.** The dense-line example is the simplest manifestation of a deeper phenomenon: **non-closed [[Def - Subgroup|subgroups]] of Lie [[Def - Group|groups]] give dense one-parameter subgroups**. The irrational-slope line is the one-parameter subgroup of $T^2$ generated by the Lie algebra element $(1, \alpha)$; the subgroup is not closed in $T^2$ (closures are tori of irrational slope, not lines), hence the embedding fails. This is one of the original motivations for distinguishing embedded from immersed Lie subgroups: closed Lie subgroups are embedded, but non-closed Lie subgroups can be merely immersed. [[Thm - The Closed Subgroup Theorem|The Closed Subgroup Theorem]] (Cartan) makes this precise.

**The immersed-submanifold rescue.** Both bad examples are still *immersed submanifolds* with their own topology — the figure-eight with the topology of $(-\pi, \pi)$ pulled back via $\beta$; the irrational line with the topology of $\mathbb{R}$ pulled back via $\gamma$. So they are smooth $1$-manifolds in their own right, but not embedded in their ambient targets. This is the canonical situation that motivates the [[Def - Immersed Submanifold|immersed submanifold]] definition: subsets of manifolds that are smooth manifolds in their own right, with their own topology, where the inclusion need only be an immersion.

**Cross-link to companion exercises.** This exercise is the canonical counterexample for the immersion / embedding distinction. The companion [[Ex - The Figure-Eight Immersion]] develops the figure-eight in more depth. Future exercises in Lie theory (closed subgroup theorem) will leverage the irrational-line example to illustrate the difference between closed and dense one-parameter subgroups.
