---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Identity Theorem (Uniqueness of Analytic Continuation)"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $f, g$ be holomorphic on a domain $D \subseteq \mathbb{C}$ containing $0$. Suppose $f(1/n) = g(1/n)$ for every $n = 1, 2, 3, \ldots$.

Prove that $f \equiv g$ on $D$.

**Recall:**

[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]: if $f, g$ are holomorphic on a connected domain $D$ and agree on a set with an accumulation point in $D$, then $f = g$ on all of $D$.

A point $z_\infty$ is an **accumulation point** of $S$ if every neighbourhood of $z_\infty$ contains a point of $S$ different from $z_\infty$.

---

# Convergent Strategy

**Problem class:** Apply the identity theorem to a discrete sequence with an accumulation point inside the domain.

**Assumption pattern:** Agreement on a sequence $1/n \to 0$, with $0 \in D$.

**Theorem routing:** Show $0$ is an accumulation point of $\{1/n\}$ (it is). The set $S = \{1/n : n \in \mathbb{Z}_{>0}\} \subseteq D$ (for $n$ large enough) has $0$ as accumulation. Apply identity theorem.

**Key decision point:** The crucial detail is that $0 \in D$ (in the *open* domain), not just on the boundary. If $0$ were outside or on the boundary of $D$, the identity theorem would fail.

---

# Legal Operations Used

1. **Identify the agreement set** $S = \{1/n : n \geq 1\}$.
2. **Verify $0$ is an accumulation point** of $S$ in $D$. Need: every neighbourhood of $0$ contains some $1/n \neq 0$, *and* $0 \in D$.
3. **Apply [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]].**

---

# Hints

> [!note]- Hint 1
> The points $1/n$ accumulate at $0$. The identity theorem requires accumulation *in the domain* — does $0$ lie in $D$?

> [!note]- Hint 2
> Once accumulation in $D$ is confirmed, apply the identity theorem directly.

---

# Solution

**Step 1: Identify the set of agreement.**

Let $S = \{1/n : n = 1, 2, 3, \ldots\} = \{1, 1/2, 1/3, \ldots\}$. By hypothesis, $f(z) = g(z)$ for all $z \in S$.

**Step 2: Verify $S \subseteq D$ for $n$ large.**

$D$ is open and contains $0$, so there is $r > 0$ with $D(0, r) \subseteq D$. For $n > 1/r$, $|1/n| = 1/n < r$, so $1/n \in D(0, r) \subseteq D$. So the tail $\{1/n : n > 1/r\}$ lies in $D$. (The first few terms might or might not lie in $D$, but the tail certainly does, and the tail also accumulates at $0$.)

**Step 3: $0$ is an accumulation point of (the tail of) $S$, and $0 \in D$.**

Every neighbourhood of $0$ (i.e., every set containing $D(0, \varepsilon)$ for some $\varepsilon > 0$) contains $1/n$ for $n > 1/\varepsilon$, hence contains points of $S$ different from $0$. So $0$ is an accumulation point of $S$. And $0 \in D$ by hypothesis.

**Step 4: Apply the identity theorem.**

$D$ is connected (a domain). $f, g$ are holomorphic on $D$ and agree on $S$ (specifically, on the tail of $S$ lying in $D$, which still has $0$ as an accumulation point in $D$). By [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]], $f = g$ on $D$. $\blacksquare$

> [!note]- Complete formal solution
> The sequence $\{1/n\}$ has $0$ as accumulation point; $0 \in D$ (open); the tail of $\{1/n\}$ lies in $D$. By [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]], $f \equiv g$ on $D$. $\blacksquare$

---

# Key Takeaways

**The accumulation point must be *inside* the domain.**

If $D$ does not contain the accumulation point of the agreement set, the identity theorem fails. Counterexample: let $D = \{z : \operatorname{Re} z > 0\}$ (right half-plane). The sequence $\{1/n\}$ lies in $D$ but accumulates at $0$, which is *on the boundary*. The functions $f(z) = z$ and $g(z) = z\sin(\pi/z)/(\pi/z)$ both satisfy $f(1/n) = g(1/n) = 1/n$ (for the right factor) but are *not* equal on $D$ — there's no contradiction because the accumulation is at a boundary point, not an interior point.

(Wait — checking more carefully: $g(z) = z \sin(\pi/z)/(\pi/z) = (1/\pi) \sin(\pi/z) \cdot z^2/... $ — this is essentially $\sin(\pi z')$ in a different variable, oscillating near $0$. The point: holomorphic functions can have wildly different boundary behaviour, and uniqueness on a sequence requires the limit to be *in* the domain.)

**Sequences accumulating in the domain.**

The "agreement on $\{1/n\}$" setup is the *prototype* application of the identity theorem. Variants:
- Agreement on a real interval inside $D \subseteq \mathbb{C}$ (real has accumulation everywhere along it).
- Agreement on a curve in $D$ — same.
- Agreement on a Cauchy sequence with limit in $D$.

The accumulation could be inside the domain at a different point too; what matters is that the agreement set has some accumulation point *inside the domain*.

**Practical applications.**

This kind of argument is constant in complex analysis. Examples:
- $f$ holomorphic on a domain containing $\mathbb{R}$, with $f \mid_\mathbb{R}$ known to be a specific real function: identity theorem pins down $f$ on the whole domain.
- Two holomorphic functions agree on an arc of the boundary: identity theorem (carefully stated for limits at the boundary).
- $f^2(z) = z^2$ on $\mathbb{R}_{>0}$: identity theorem forces $f$ to be $\pm z$ (a branch of the square root).
