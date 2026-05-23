---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Distribution Function"
  - "Def - Lebesgue Measure"
  - "Def - Random Variable"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $F$ be a [[Def - Distribution Function|distribution function]] and $g(u)=\inf\{t:F(t)\ge u\}$ its quantile function.

**(a)** Prove the equivalence $g(u)\le t\iff u\le F(t)$, for $u\in(0,1)$, $t\in\mathbb{R}$.

**(b)** Deduce: if $U$ is [[Def - Lebesgue Measure|uniform]] on $(0,1)$, then $X=g(U)$ has distribution function $F$.

**(c)** Conclude that *every* probability law on $\mathbb{R}$ is the law of a function of a single uniform random variable, and that any sequence of laws can be realised on one probability space.

**Recall:**

![[Def - Distribution Function#The Definition]]

---

# Convergent Strategy

**Problem class:** constructing a random variable with a *prescribed* law.

**Assumption pattern:** $F$ is non-decreasing and right-continuous; its generalised inverse $g$ converts the *uniform* law into $F$. The whole computation rests on the equivalence (a), which encodes right-continuity.

**Theorem routing:** (a) right-continuity makes the infimum in $g$ attained; (b) $\mathbb{P}(g(U)\le t)=\mathbb{P}(U\le F(t))=F(t)$.

---

# Legal Operations Used

1. **The quantile equivalence** $g(u)\le t\iff u\le F(t)$.
2. **Pushforward of the uniform law** through $g$.

---

# Hints

> [!note]- Hint 1
> $\{t:F(t)\ge u\}$ is an interval $[g(u),\infty)$ — *closed* on the left because $F$ is right-continuous, so the inf is attained.

> [!note]- Hint 2
> (b): $\mathbb{P}(X\le t)=\mathbb{P}(g(U)\le t)=\mathbb{P}(U\le F(t))$ by (a). For uniform $U$, $\mathbb{P}(U\le s)=s$.

---

# Solution

**Step 1 — (a).** Fix $u\in(0,1)$. The set $I_u=\{t:F(t)\ge u\}$ is an interval ($F$ non-decreasing) of the form $[g(u),\infty)$ or $(g(u),\infty)$. Right-continuity of $F$ forces it to be *closed*: if $t_n\downarrow g(u)$ with $F(t_n)\ge u$, then $F(g(u))=\lim F(t_n)\ge u$, so $g(u)\in I_u$. Hence $I_u=[g(u),\infty)$, and $u\le F(t)\iff t\in I_u\iff t\ge g(u)$, i.e. $g(u)\le t\iff u\le F(t)$.

**Step 2 — (b).** Let $U\sim\text{Unif}(0,1)$, $X=g(U)$. For any $t$,
$$\mathbb{P}(X\le t)=\mathbb{P}(g(U)\le t)\overset{\text{(a)}}{=}\mathbb{P}(U\le F(t))=F(t),$$
the last step because $\mathbb{P}(U\le s)=s$ for $s\in[0,1]$ (uniform law) and $F(t)\in[0,1]$. So $X$ has distribution function $F$, i.e. law $\mu_F$.

**Step 3 — (c).** Given *any* probability law $\mu$ on $\mathbb{R}$, take its distribution function $F$ and the uniform space $((0,1),\mathcal{B},\lambda)$; then $g(U)$ has law $\mu$. So every law is realised as a function of one uniform variable. For a *sequence* of prescribed laws $(\mu_i)$: take an infinite [[Thm - Product Measure|product]] of uniform spaces, with coordinates $U_1,U_2,\dots$ independent uniform; then $X_i=g_i(U_i)$ are independent with $X_i\sim\mu_i$ — all on the single space $(0,1)^{\mathbb{N}}$.

> [!note]- Complete formal solution
> (a) $\{t:F(t)\ge u\}=[g(u),\infty)$ — closed because right-continuity gives $F(g(u))\ge u$; so $g(u)\le t\iff u\le F(t)$. (b) $\mathbb{P}(g(U)\le t)=\mathbb{P}(U\le F(t))=F(t)$. (c) Every law's distribution function $F$ gives $g$, and $g(U)$ realises it; an independent product of uniforms realises any sequence of laws on one space. $\blacksquare$

---

# Key Takeaways

**The quantile transform realises *every* law on $\mathbb{R}$ as a deterministic function of a single uniform random variable — $X=F^{-1}(U)$.** This is inverse-transform sampling, the foundation of Monte Carlo simulation, and the theoretical reason the [[Def - Lebesgue Measure|uniform distribution]] generates all of one-dimensional probability. The entire content is the order-reversing equivalence $g(u)\le t\iff u\le F(t)$, which is right-continuity of $F$ made into an identity.

**It is also the device that "puts all random variables on one probability space."** An abstract theorem may posit independent variables with assorted laws; the quantile transform plus an infinite [[Thm - Product Measure|product]] of uniforms constructs them concretely on $(0,1)^{\mathbb{N}}$. This is why one may always *assume* a probability space rich enough to carry whatever independent sequence a proof requires — existence is never an obstacle, and the [[Thm - Strong Law of Large Numbers|laws of large numbers]] and the [[Thm - Central Limit Theorem|CLT]] may be stated for "an i.i.d. sequence" without worrying whether one exists.
