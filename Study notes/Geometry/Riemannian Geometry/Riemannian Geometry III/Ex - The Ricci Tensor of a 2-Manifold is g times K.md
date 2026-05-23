---
type: exercise
subject: riemannian-geometry
difficulty: "⭐"
prereqs:
  - "Def - Ricci Tensor"
  - "Def - Sectional Curvature"
  - "Def - Einstein Manifold"
tags: [geometry, riemannian-geometry, curvature, einstein]
---

# Problem Statement

Let $(M, g)$ be a $2$-dimensional Riemannian manifold with Gauss curvature $K$. Show that the [[Def - Ricci Tensor|Ricci tensor]] satisfies
$$\mathrm{Ric} = K\, g.$$
Conclude that *every* $2$-dimensional Riemannian manifold is an [[Def - Einstein Manifold|Einstein manifold]].

**Recall:**

The Ricci tensor is defined as $\mathrm{Ric}(X, Y) = \mathrm{tr}(Z \mapsto R(Z, X)Y) = R^a_{\;XaY}$. In an orthonormal frame $(e_a)$, $\mathrm{Ric}(e_i, e_i) = \sum_{j \ne i}K(e_i \wedge e_j)$ — the sum of sectional curvatures of the $n - 1$ planes containing $e_i$.

A Riemannian manifold of dimension $n \ge 3$ is **Einstein** if $\mathrm{Ric} = \lambda g$ for some constant $\lambda$. (In dim $2$, the same condition trivially holds with $\lambda = K$, but the **dimension restriction $n \ge 3$** in the strict definition is what makes "Einstein" a nontrivial condition.)

The [[Def - Sectional Curvature|Gauss curvature]] of a $2$-D Riemannian manifold is the unique sectional curvature (only one $2$-plane at each point).

---

# Convergent Strategy

**Problem class:** Tensor identity. Reduce a definition involving traces to a comparison of two tensors of the same type. The computation is one line; the conceptual content is *why* this trivial identity in dim $2$ is the source of the Schur's-lemma-type structure in higher dimensions.

**Assumption pattern:** $\dim M = 2$. This makes the Ricci tensor a $2 \times 2$ symmetric matrix at each point. There is only one $2$-plane (the whole tangent space), so there is only one sectional curvature value at each point — the Gauss curvature $K$.

**Theorem routing:** Direct computation. In an orthonormal frame $(e_1, e_2)$, $\mathrm{Ric}(e_i, e_i) = \sum_{j \ne i} K(e_i \wedge e_j) = K(e_1 \wedge e_2) = K$ (since the only $2$-plane is $T_pM$ itself, and the only sectional curvature is $K$). So $\mathrm{Ric}(e_i, e_i) = K = K \cdot \langle e_i, e_i\rangle = K \cdot g(e_i, e_i)$. For off-diagonal $\mathrm{Ric}(e_1, e_2)$: $\sum_{a}\langle R(e_a, e_1)e_2, e_a\rangle = \langle R(e_2, e_1)e_2, e_2\rangle = 0$ (the $a = 1$ term vanishes by antisymmetry of $R$ in first pair, $a = 2$ vanishes since $\langle R(e_2, e_1)e_2, e_2\rangle = R_{2221}$ which equals $0$ by antisymmetry in the first pair $(2, 2)$).

**Key decision point:** Recognising that in dim $2$, there is *one* tangent $2$-plane at each point, so "sectional curvature" is a single function — the Gauss curvature. This eliminates any subtlety: the sum in the Ricci-tensor formula collapses to a single term.

---

# Legal Operations Used

1. **Operation 4 from the topic page (trace Riemann to descend to Ricci).** Direct application: trace the Riemann tensor to get $\mathrm{Ric}$, then compare to $Kg$.

---

# Hints

> [!note]- Hint 1
> Use the orthonormal-frame formula: $\mathrm{Ric}(e_i, e_i) = \sum_{j \ne i}K(e_i \wedge e_j)$. In dim $2$, there is only $j = 3 - i$, so the sum is a single term.

> [!note]- Hint 2
> $\mathrm{Ric}(e_1, e_1) = K(e_1 \wedge e_2) = K$ (the Gauss curvature). Similarly $\mathrm{Ric}(e_2, e_2) = K(e_2 \wedge e_1) = K$ (same plane, same curvature). For the off-diagonal: $\mathrm{Ric}(e_1, e_2) = \sum_a \langle R(e_a, e_1)e_2, e_a\rangle$; the $a = 1$ term vanishes by $R(e_1, e_1) = 0$, the $a = 2$ term is $\langle R(e_2, e_1)e_2, e_2\rangle = R_{2221}$ which vanishes by antisymmetry of $R$ in the first pair (since $R_{ABCD} = -R_{BACD}$ gives $R_{2221} = -R_{2221}$, so $R_{2221} = 0$).

> [!note]- Hint 3
> So in the orthonormal frame, $\mathrm{Ric}_{ij} = K\delta_{ij} = K g_{ij}$. Since this holds in any orthonormal frame (hence for any orthonormal basis at any point), $\mathrm{Ric} = Kg$ globally.

---

# Solution

**Plan:** Show that the Ricci tensor in an orthonormal frame on a $2$-manifold has $\mathrm{Ric}_{ij} = K\delta_{ij}$, deduce $\mathrm{Ric} = Kg$. Conclude every $2$-manifold is "trivially Einstein" (with the qualifier that the definition of Einstein technically requires $n \ge 3$ for the condition to be informative).

**Step 1: Diagonal Ricci components $\mathrm{Ric}(e_i, e_i) = K$.**

> [!note]- Derivation
> Pick an orthonormal frame $(e_1, e_2)$ at a point $p$. The orthonormal-frame formula for Ricci:
> $$\mathrm{Ric}(e_i, e_i) = \sum_{j \ne i} K(e_i \wedge e_j).$$
> In dim $2$, for $i = 1$: $j$ ranges over $\{2\}$, so $\mathrm{Ric}(e_1, e_1) = K(e_1 \wedge e_2)$. The plane $e_1 \wedge e_2$ is the *entire* tangent space $T_pM$, and its sectional curvature is the Gauss curvature $K(p)$. So $\mathrm{Ric}(e_1, e_1) = K$. Similarly $\mathrm{Ric}(e_2, e_2) = K(e_2 \wedge e_1) = K(e_1 \wedge e_2) = K$ (sectional curvature depends only on the unsigned $2$-plane).

**Step 2: Off-diagonal Ricci component $\mathrm{Ric}(e_1, e_2) = 0$.**

> [!note]- Derivation
> $\mathrm{Ric}(e_1, e_2) = \sum_a \langle R(e_a, e_1)e_2, e_a\rangle = R^a_{\;2a1}$ (in component form, with appropriate sign convention).
> Sum over $a = 1, 2$:
> - $a = 1$: $\langle R(e_1, e_1)e_2, e_1\rangle = 0$ since $R(e_1, e_1) = 0$ (antisymmetry).
> - $a = 2$: $\langle R(e_2, e_1)e_2, e_2\rangle = R_{2221}$ (with the standard convention $R_{abcd} = \langle R(e_c, e_d)e_b, e_a\rangle$). By antisymmetry of $R$ in the first pair: $R_{2221} = -R_{2221}$, so $R_{2221} = 0$.
> 
> Hence $\mathrm{Ric}(e_1, e_2) = 0$.

**Step 3: Combine: $\mathrm{Ric} = Kg$.**

> [!note]- Derivation
> The Ricci tensor in the orthonormal frame is $\mathrm{Ric}_{ij} = K\delta_{ij}$. In matrix form, $\mathrm{Ric} = K\cdot I_{2\times 2}$. Since $\delta_{ij} = g_{ij}$ in an orthonormal frame, $\mathrm{Ric}_{ij} = Kg_{ij}$. This identity is frame-independent (both sides are tensors with the same components in *any* frame: the orthonormal-frame computation generalises). So
> $$\mathrm{Ric} = Kg$$
> as tensors on $M$. ∎

> [!note]- Complete formal solution
> Pick an orthonormal frame $(e_1, e_2)$ at $p$. By the orthonormal-frame Ricci formula $\mathrm{Ric}(e_i, e_i) = \sum_{j \ne i}K(e_i \wedge e_j)$ and the fact that there is only one $2$-plane in $T_pM$: $\mathrm{Ric}(e_i, e_i) = K$ for both $i = 1, 2$. The off-diagonal components vanish by antisymmetry of $R$ in the first pair. Hence $\mathrm{Ric}_{ij} = K\delta_{ij} = Kg_{ij}$ in the orthonormal frame, giving $\mathrm{Ric} = Kg$ as tensors. Every $2$-D Riemannian manifold trivially satisfies the Einstein condition $\mathrm{Ric} = \lambda g$ with $\lambda = K$ — but the standard definition of "Einstein manifold" requires $n \ge 3$, where $\lambda$ being a constant is a nontrivial constraint (by **Schur's lemma**, "$\lambda$ a function" forces "$\lambda$ a constant" in dim $\ge 3$; in dim $2$, $\lambda = K$ can be any function).

---

# Key Takeaways

**Dim 2 is special: the entire Riemann tensor is determined by the single Gauss curvature.** The identity $\mathrm{Ric} = Kg$ in dim $2$ means the Ricci tensor adds no information beyond the Gauss curvature — they are the same data in dim $2$. The scalar curvature is $S = \mathrm{tr}_g \mathrm{Ric} = 2K$ (also just the Gauss curvature, scaled). The Riemann tensor itself has only $\tfrac{1}{12}\cdot 2^2(2^2 - 1) = 1$ independent component, which is again $K$. So *all curvature invariants in dim $2$ are functions of $K$* — the four-fold hierarchy "Riemann → sectional → Ricci → scalar" collapses to a single function. This is the geometric reason that surface theory is so much simpler than higher-dimensional Riemannian geometry.

**Schur's lemma fails in dim 2.** The Einstein-manifold definition requires the constant $\lambda$ in $\mathrm{Ric} = \lambda g$ to be a global constant on $M$, not just a function. In dim $\ge 3$, **Schur's lemma** (a consequence of the second [[Thm - First and Second Bianchi Identities|Bianchi identity]]) says that "$\lambda$ a function" already forces "$\lambda$ a constant"; so the apparently weaker pointwise condition is automatic in high dimension. In dim $2$, this fails: the function $K$ can vary arbitrarily, and the relation $\mathrm{Ric} = Kg$ holds trivially without forcing $K$ to be constant. So **the standard definition of "Einstein manifold" excludes dim $2$ from being informative**.

**Surfaces of constant Gauss curvature are the "true" $2$-D Einstein manifolds.** If we extend the Einstein definition to include "constant Gauss curvature" as the dim-$2$ analogue, we recover the same trichotomy: $K_0 > 0$ (sphere, projective plane), $K_0 = 0$ (flat torus, Klein bottle), $K_0 < 0$ (hyperbolic surfaces of genus $\ge 2$). These are the dim-$2$ space forms. The **uniformisation theorem** (every Riemann surface admits a metric of constant Gauss curvature) is the dim-$2$ analogue of the **Yamabe problem** and the constant-Einstein-metric search in higher dimensions.

**The identity is the foundation for Gauss–Bonnet.** Since $\mathrm{Ric} = Kg$ in dim $2$ and $S = 2K$, the Einstein–Hilbert action $\int S\, dV = 2\int K\, dV$ is, up to a factor, the integral of Gauss curvature — and by the **Gauss–Bonnet theorem**, $\int K\, dV = 2\pi\chi(M)$ for a closed orientable surface. So the Einstein–Hilbert action in dim $2$ is *purely topological*: it equals $4\pi\chi(M)$ regardless of the metric. This is why "$2$-dimensional gravity" is trivial — the variational principle gives no constraints on the metric, since the action is metric-independent. The non-triviality of GR begins in dim $\ge 3$, where $\int S\, dV$ is no longer topological.
