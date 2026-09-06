---
type: theorem
subject: gauge-theory
prereqs: ["Def - Smooth Fredholm Map and Regular Value"]
tags: [gauge-theory, sard-smale, transversality]
---

# Statement

> [!theorem] Sard–Smale
> If $f:X\to Y$ is a $C^r$ Fredholm map between separable Banach manifolds and $r>\max\{0,\operatorname{ind}f\}$, its regular values form a residual subset of $Y$.

> [!theorem] Parametric transversality
> Let $F:X\times P\to Y$ be smooth and transverse to a submanifold $Z\subset Y$. If each partial map $F_p$ is Fredholm relative to $Z$, then for a residual set of $p\in P$, $F_p$ is transverse to $Z$.

# Proof Architecture

> [!proof]- Formal Proof
> Cover $X$ by countably many Kuranishi neighborhoods. In each, the critical-value question reduces to Sard's theorem for the finite-dimensional kernel-to-cokernel map; the complement of regular values is meagre locally. Countability makes the intersection of the local open-dense conditions residual. The differentiability bound is exactly the finite-dimensional Sard bound for the Kuranishi dimension.
>
> For the parametric statement, $W=F^{-1}(Z)$ is a Banach submanifold by transversality. The projection $\pi:W\to P$ is Fredholm, and $p$ is a regular value of $\pi$ exactly when $F_p\pitchfork Z$. Sard–Smale applied to $\pi$ gives the residual set.

# Warning

Residual means a countable intersection of open dense sets; it need not have full measure in an infinite-dimensional space. Transversality gives smoothness, not compactness.

