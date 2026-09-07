---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs: ["Thm - Sobolev Embedding, Compactness, and Multiplication"]
tags: [gauge-theory, sobolev-embedding, circle]
---

# Prerequisite Concepts

- [[Thm - Sobolev Embedding, Compactness, and Multiplication]]

# Problem Statement

Prove directly that $W^{1,2}(S^1)\hookrightarrow C^0(S^1)$ and that bounded subsets are precompact in $C^0$.

# Solution

> [!solution]- Solution
> Write $u=\bar u+u_0$, where $\bar u=(2\pi)^{-1}\int u$. Some $\theta_0$ satisfies $u_0(\theta_0)=0$. Hence
> $$|u_0(\theta)|\le\int_{\theta_0}^\theta|u'|\le\sqrt{2\pi}\|u'\|_{L^2},$$
> while $|\bar u|\le(2\pi)^{-1/2}\|u\|_{L^2}$. This proves the continuous estimate. Also
> $$|u(\theta)-u(\phi)|\le\|u'\|_{L^2}|\theta-\phi|^{1/2}.$$
> A bounded $W^{1,2}$ family is uniformly bounded and equicontinuous; Arzelà–Ascoli supplies a uniformly convergent subsequence. Density extends the argument from smooth functions to all of $W^{1,2}$.

