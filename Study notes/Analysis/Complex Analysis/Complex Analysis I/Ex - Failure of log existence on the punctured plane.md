---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Branch of the Logarithm"
  - "Thm - Existence of a Logarithm on Simply Connected Domains"
  - "Thm - Properties of the Complex Exponential"
tags: [analysis, complex-analysis]
---

# Problem Statement

Prove that there is no continuous function $\lambda : \mathbb{C}^\times \to \mathbb{C}$ satisfying $\exp(\lambda(z)) = z$ for all $z \in \mathbb{C}^\times$.

Provide two proofs:

(a) **Topological proof.** Trace $\lambda$ around the unit circle and derive a contradiction from continuity.

(b) **Integration proof.** If a branch existed on $\mathbb{C}^\times$, then $1/z$ would have a primitive on $\mathbb{C}^\times$, contradicting $\int_{|z|=1} dz/z = 2\pi i \neq 0$.

**Recall:**

A [[Def - Branch of the Logarithm|branch of the logarithm]] on an open $U \subseteq \mathbb{C}^\times$ is a continuous $\lambda : U \to \mathbb{C}$ with $\exp(\lambda(z)) = z$. If $\lambda$ exists, it is holomorphic with $\lambda'(z) = 1/z$. By [[Thm - Existence of a Logarithm on Simply Connected Domains]], branches exist iff every closed curve in $U$ has winding number $0$ around $0$.

---

# Convergent Strategy

**Problem class:** Showing a continuous extension is *impossible*.

**Assumption pattern:** Suppose for contradiction that $\lambda$ exists on all of $\mathbb{C}^\times$. The obstruction is topological: $\mathbb{C}^\times$ is not simply connected.

**Theorem routing:** Two routes. (a) Use continuity to trace $\lambda$ around the unit circle. (b) Use the primitive characterization and direct computation of $\int dz/z$ on the unit circle.

**Key decision point:** The unit circle $|z| = 1$ has winding number $1$ around $0$ — this is the obstruction.

---

# Legal Operations Used

1. **Suppose for contradiction** $\lambda$ exists on $\mathbb{C}^\times$.
2. **Parametrize the unit circle** $\gamma(t) = e^{it}$ for $t \in [0, 2\pi]$.
3. **Compute $\lambda(\gamma(t))$** using $\exp(\lambda(\gamma(t))) = \gamma(t)$.
4. **Use continuity** to deduce $\lambda$ along the loop equals $i t + (\text{constant})$ continuously.
5. **Derive contradiction** from $\lambda(\gamma(0)) = \lambda(\gamma(2\pi))$ (since $\gamma$ is closed) versus the requirement $\lambda(\gamma(2\pi)) = \lambda(\gamma(0)) + 2\pi i$.

Alternatively:
1'. **Compute $\int_{|z|=1} dz/z = 2\pi i$** directly.
2'. **Note** that if $\lambda$ is a primitive of $1/z$, the integral around the closed curve is $0$ — contradiction.

---

# Hints

> [!note]- Hint 1
> Parametrize the unit circle as $\gamma(t) = e^{it}, t \in [0, 2\pi]$. Then $\lambda(\gamma(t))$ must satisfy $\exp(\lambda(\gamma(t))) = e^{it}$, so $\lambda(\gamma(t)) = it + 2\pi i k(t)$ for some integer-valued function $k$. Continuity of $\lambda$ forces $k$ continuous, hence constant.

> [!note]- Hint 2
> For the integration proof: $\lambda'(z) = 1/z$ on $\mathbb{C}^\times$. So $\lambda$ is a primitive of $1/z$. By the fundamental theorem of contour integration, the integral of $1/z$ around any closed curve is $0$. But $\int_{|z|=1} dz/z = \int_0^{2\pi} (ie^{it}/e^{it})\,dt = 2\pi i$. Contradiction.

---

# Solution

**(a) Topological proof.**

Suppose for contradiction $\lambda : \mathbb{C}^\times \to \mathbb{C}$ continuous with $\exp(\lambda(z)) = z$ for all $z \in \mathbb{C}^\times$.

Parametrize the unit circle by $\gamma(t) = e^{it}$ for $t \in [0, 2\pi]$. The composition $\lambda \circ \gamma : [0, 2\pi] \to \mathbb{C}$ is continuous, and $\exp(\lambda(\gamma(t))) = e^{it}$.

By [[Thm - Properties of the Complex Exponential|properties of $\exp$]], $\exp(\lambda(\gamma(t))) = \exp(it)$ means $\lambda(\gamma(t)) - it \in 2\pi i\mathbb{Z}$. So $\lambda(\gamma(t)) = it + 2\pi i \cdot k(t)$ for some function $k : [0, 2\pi] \to \mathbb{Z}$.

> [!note]- $k$ is continuous, hence constant
> $k(t) = (\lambda(\gamma(t)) - it)/(2\pi i)$ is continuous as a composition of continuous functions. A continuous map from a connected set $[0, 2\pi]$ to the discrete set $\mathbb{Z}$ is constant.

So $k(t) = k_0$ constant. Hence $\lambda(\gamma(t)) = it + 2\pi i k_0$ for all $t \in [0, 2\pi]$.

But $\gamma(0) = \gamma(2\pi) = 1$, so $\lambda(\gamma(0)) = \lambda(\gamma(2\pi))$. Compute:
$$\lambda(\gamma(0)) = 0 + 2\pi i k_0 = 2\pi i k_0,$$
$$\lambda(\gamma(2\pi)) = 2\pi i + 2\pi i k_0.$$

Equality forces $0 = 2\pi i$, contradiction. So no continuous $\lambda$ exists on $\mathbb{C}^\times$. $\blacksquare$

**(b) Integration proof.**

Suppose for contradiction $\lambda$ exists on $\mathbb{C}^\times$. By [[Def - Branch of the Logarithm|definition of branch]] (and the inverse-function-theorem argument), $\lambda$ is holomorphic on $\mathbb{C}^\times$ with $\lambda'(z) = 1/z$.

> [!note]- Why $\lambda$ is holomorphic
> $\exp$ is holomorphic with nonzero derivative everywhere. Locally, by the inverse function theorem (or directly: $\lambda(z) - \lambda(z_0) = \log(z/z_0) + \text{integer}$ locally, where the integer is fixed by continuity, so $\lambda$ inherits holomorphicity from local sections of $\exp^{-1}$).

So $\lambda$ is a primitive of the holomorphic function $f(z) = 1/z$ on $\mathbb{C}^\times$. By the fundamental theorem of contour integration ([[Thm - Fundamental Theorem of Contour Integration]] in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]), for any closed curve $\gamma$ in $\mathbb{C}^\times$:
$$\int_\gamma \frac{dz}{z} = \lambda(\gamma(b)) - \lambda(\gamma(a)) = 0 \quad \text{(since } \gamma \text{ closed)}.$$

But compute directly with $\gamma(t) = e^{it}, t \in [0, 2\pi]$:
$$\int_\gamma \frac{dz}{z} = \int_0^{2\pi} \frac{1}{e^{it}} \cdot ie^{it}\,dt = \int_0^{2\pi} i\,dt = 2\pi i.$$

We have $0 = 2\pi i$, contradiction. So no branch exists on $\mathbb{C}^\times$. $\blacksquare$

> [!note]- Complete formal solution
> **(a)** Suppose $\lambda : \mathbb{C}^\times \to \mathbb{C}$ continuous, $\exp(\lambda(z)) = z$. Parametrize unit circle $\gamma(t) = e^{it}$. The function $t \mapsto \lambda(\gamma(t)) - it$ is continuous and takes values in $2\pi i\mathbb{Z}$ (since $\exp(\lambda(\gamma(t))) = e^{it}$ means the difference lies in the kernel of $\exp$). A continuous integer-valued function on $[0, 2\pi]$ is constant. So $\lambda(\gamma(t)) = it + 2\pi i k_0$. But $\gamma(0) = \gamma(2\pi)$ forces $\lambda(\gamma(0)) = \lambda(\gamma(2\pi))$, i.e., $2\pi i k_0 = 2\pi i + 2\pi i k_0$, contradiction.
>
> **(b)** If $\lambda$ exists, $\lambda$ is a primitive of $1/z$ on $\mathbb{C}^\times$. By the fundamental theorem of contour integration, $\int_{|z|=1} dz/z = 0$. But direct computation $\int_0^{2\pi}(ie^{it}/e^{it})\,dt = 2\pi i \neq 0$. Contradiction. $\blacksquare$

---

# Key Takeaways

**Topological obstruction to a continuous lift.**

The punctured plane $\mathbb{C}^\times$ has a nontrivial loop (the unit circle, with winding number $1$ around $0$), and *that loop is the obstruction* to continuously inverting $\exp$. The lesson generalizes: continuous lifts of maps through covering maps exist iff the topological obstruction vanishes. For $\exp : \mathbb{C} \to \mathbb{C}^\times$, the obstruction is exactly $\pi_1(\mathbb{C}^\times) \neq 0$.

**$\int dz/z$ as the prototypical "winding integral".**

The integral $\int dz/z$ around the unit circle equals $2\pi i$ — a single specific nonzero number. This is the most fundamental contour integral in complex analysis, and it is the *source* of all "winding number" phenomena. The general winding number $I(\gamma; 0) = \frac{1}{2\pi i}\int_\gamma dz/z$ counts how many times $\gamma$ wraps around $0$, and it is the integer invariant that obstructs the existence of branches.

**Local vs. global existence.**

The local existence of branches (near every point of $\mathbb{C}^\times$) is automatic: $\exp$ is a local biholomorphism. The *global* existence fails on $\mathbb{C}^\times$ because the local branches *do not glue together* into a single continuous function. The gluing failure is exactly the topological obstruction. The pattern recurs throughout: local existence is easy (analysis), global existence is topological (does the obstruction vanish?).
