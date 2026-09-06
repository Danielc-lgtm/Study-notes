---
type: exercise
subject: gauge-theory
prereqs: ["Def - Gauge Action and Seiberg-Witten Moduli Space"]
tags: [gauge-theory, seiberg-witten, stabilizer]
---

# Exercise

Let $X$ be connected and let $g:X\to U(1)$ fix a Seiberg–Witten configuration $(\psi,A)$ under
$$(\psi,A)\cdot g=(g^{-1}\psi,A+2g^{-1}dg).$$
Prove that $g$ is constant. Deduce that the stabilizer is trivial when $\psi\not\equiv0$, whereas it is the constant circle when $\psi\equiv0$.

> [!solution]- Solution
> Equality of the connection components gives $g^{-1}dg=0$, hence $dg=0$. Since $X$ is connected, $g$ is constant. If $\psi$ is nonzero at some point, $g^{-1}\psi=\psi$ there forces that constant to be $1$. If $\psi\equiv0$, every constant $g\in U(1)$ fixes both components, so the stabilizer is exactly $U(1)$.

# Why this matters

Irreducibility is exactly the condition that makes the gauge action free. The slice theorem therefore produces an honest local manifold quotient only away from reducibles.
