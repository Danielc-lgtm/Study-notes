---
type: exercise
subject: gauge-theory
prereqs: ["Def - Seiberg-Witten Invariant"]
tags: [gauge-theory, seiberg-witten, exercise]
---

# Prerequisite Concepts

- [[Def - Seiberg-Witten Invariant]]

# Exercise

Suppose the Seiberg–Witten moduli space has dimension $d$. Explain why the point class defines a numerical invariant only when $d$ is even, and recover the signed-count definition when $d=0$.

> [!solution]- Solution
> The class $\mu$ lies in $H^2(\mathcal M;\mathbb Z)$, so $\mu^k$ has degree $2k$. Pairing with the fundamental class is numerical exactly when $2k=d$. No integer $k$ exists for odd $d$. If $d=0$, then $k=0$ and $\mu^0=1$; hence $\langle1,[\mathcal M]\rangle$ is the sum of the orientation signs of its finitely many points.
