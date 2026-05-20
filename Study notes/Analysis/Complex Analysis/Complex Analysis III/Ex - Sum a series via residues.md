---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Residue Theorem"
  - "Thm - Computing Residues"
  - "Def - Removable Singularity, Pole, Essential Singularity"
tags: [analysis, complex-analysis]
---

# Problem Statement

Use the function $f(z) = \pi\cot(\pi z)/z^2$ and a sequence of large square contours $\Gamma_N$ to show that
$$\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}.$$

**Recall:**

![[Thm - Residue Theorem#Notation]]

$\pi\cot(\pi z) = \pi\cos(\pi z)/\sin(\pi z)$ has simple poles at every integer $n \in \mathbb{Z}$, with residue $1$ at each.

---

# Convergent Strategy

**Problem class:** Summation of an infinite series by contour integration. The function $\pi\cot(\pi z) g(z)$ has poles at every integer with residue $g(n)$ (when $g$ has no pole at $n$), so the sum $\sum_n g(n)$ appears as a sum of residues.

**Assumption pattern:** $g(z) = 1/z^2$ has a double pole at $z = 0$ (and is otherwise entire). The product $\pi\cot(\pi z)/z^2$ has simple poles at integers $n \neq 0$ (from $\cot$) with residues $1/n^2$, and a higher-order pole at $z = 0$ (from $1/z^2$ combined with $\cot$'s simple pole there).

**Theorem routing:** Apply the residue theorem to a large square contour $\Gamma_N$ enclosing the integers $-N, \ldots, N$. The integral vanishes as $N \to \infty$ (the integrand decays on the contour). The sum of all enclosed residues equals zero in the limit; the contributions from integers $n \neq 0$ give $2\sum_{n=1}^\infty 1/n^2$ (by symmetry); the contribution from $n = 0$ has a residue computable by the order-$k$ formula.

**Key decision point:** Recognize that $\cot(\pi z)$ is bounded uniformly on the square contour $\Gamma_N$ when $N$ is large — this is what makes the integral over $\Gamma_N$ vanish, allowing the "sum of residues = 0" identity to give the desired sum.

---

# Legal Operations Used

1. **Identify the poles** of $\pi\cot(\pi z)/z^2$: at every $n \in \mathbb{Z}$.
2. **Compute the residue at each pole**:
   - At $n \neq 0$: simple pole from $\cot$, residue $= 1/n^2 \cdot 1 = 1/n^2$.
   - At $n = 0$: combined pole (cot has simple pole, $1/z^2$ has double pole = triple pole total). Compute via Laurent expansion or higher-order formula.
3. **Apply the residue theorem** on a large square $\Gamma_N$ of side $2N + 1$ centred at the origin: $\oint_{\Gamma_N} = 2\pi i \cdot (\text{sum of residues inside})$.
4. **Show the contour integral vanishes** as $N \to \infty$: $|\cot(\pi z)|$ is bounded on $\Gamma_N$, $1/z^2$ decays as $1/N^2$, contour length is $4(2N + 1) = O(N)$. Total: $O(N \cdot 1/N^2) = O(1/N) \to 0$.
5. **Equate** "sum of residues = 0" and solve for $\sum 1/n^2$.

---

# Hints

> [!note]- Hint 1
> The residue at integer $n \neq 0$ of $\pi\cot(\pi z)/z^2$: $\pi\cot(\pi z)$ has residue $1$ at $z = n$, and $1/z^2$ at $z = n$ is just $1/n^2$. So the residue of the product is $1/n^2$.

> [!note]- Hint 2
> The residue at $z = 0$: $\pi\cot(\pi z) = 1/z - (\pi^2/3) z - (\pi^4/45) z^3 - \ldots$ (Laurent expansion). Dividing by $z^2$: $\pi\cot(\pi z)/z^2 = 1/z^3 - \pi^2/(3z) - \pi^4 z/45 - \ldots$. The coefficient of $1/z$ — the residue — is $-\pi^2/3$.

> [!note]- Hint 3
> By the residue theorem: $\oint_{\Gamma_N}\pi\cot(\pi z)/z^2\,dz = 2\pi i\,[(-\pi^2/3) + \sum_{0 < |n| \leq N} 1/n^2]$.

> [!note]- Hint 4
> The contour integral $\oint_{\Gamma_N}\pi\cot(\pi z)/z^2\,dz \to 0$ as $N \to \infty$: $|\cot(\pi z)|$ is bounded uniformly on $\Gamma_N$ (key fact), $|1/z^2| \leq 1/N^2$ on $\Gamma_N$, length is $O(N)$, total bound $O(N \cdot 1/N^2 \cdot B) = O(1/N) \to 0$ (where $B$ is the bound on $\pi\cot(\pi z)$).

> [!note]- Hint 5
> Setting the contour integral to $0$: $-\pi^2/3 + 2\sum_{n=1}^\infty 1/n^2 = 0$ (using symmetry $1/n^2 = 1/(-n)^2$), so $\sum_{n=1}^\infty 1/n^2 = \pi^2/6$.

---

# Solution

**Step 1: Identify poles and compute residues**

The function $f(z) = \pi\cot(\pi z)/z^2$ has poles at every integer $n \in \mathbb{Z}$.

> [!note]- Derivation
> **Residue at $n \neq 0$.** $\pi\cot(\pi z) = \pi\cos(\pi z)/\sin(\pi z)$ has a simple pole at $z = n$: $\sin(\pi z)$ has a simple zero with $(\sin)'(\pi n) = \pi\cos(\pi n) = \pi (-1)^n$, and $\pi\cos(\pi n) = \pi(-1)^n$. By the quotient formula, $\operatorname{Res}_n \pi\cot(\pi z) = \pi(-1)^n/(\pi (-1)^n) = 1$.
>
> The factor $1/z^2$ at $z = n$ is holomorphic with value $1/n^2$. So $\operatorname{Res}_n[\pi\cot(\pi z)/z^2] = 1 \cdot 1/n^2 = 1/n^2$.
>
> **Residue at $n = 0$.** Use the Laurent expansion of $\pi\cot(\pi z)$ around $0$:
> $$\pi\cot(\pi z) = \frac{1}{z} - \frac{\pi^2 z}{3} - \frac{\pi^4 z^3}{45} - \ldots$$
> (This is a standard expansion; the leading $1/z$ comes from $\cos(\pi z)/\sin(\pi z) \approx 1/(\pi z)$ near $0$, and the higher terms are from the Taylor expansions of $\sin, \cos$.)
>
> Dividing by $z^2$:
> $$\frac{\pi\cot(\pi z)}{z^2} = \frac{1}{z^3} - \frac{\pi^2}{3z} - \frac{\pi^4 z}{45} - \ldots$$
> The coefficient of $1/z$ is $-\pi^2/3$. So $\operatorname{Res}_0[\pi\cot(\pi z)/z^2] = -\pi^2/3$.

**Step 2: Apply the residue theorem on a large square**

> [!note]- Derivation
> Let $\Gamma_N$ be the square contour with vertices at $\pm (N + 1/2) \pm i(N + 1/2)$, traversed counterclockwise. This square has the integers $-N, \ldots, N$ on the interior. By the residue theorem,
> $$\oint_{\Gamma_N}\frac{\pi\cot(\pi z)}{z^2}\,dz = 2\pi i \left[-\frac{\pi^2}{3} + \sum_{0 < |n| \leq N}\frac{1}{n^2}\right].$$
> By symmetry $1/(-n)^2 = 1/n^2$, so $\sum_{0 < |n| \leq N} 1/n^2 = 2\sum_{n = 1}^N 1/n^2$.

**Step 3: Show $\oint_{\Gamma_N}f\,dz \to 0$ as $N \to \infty$**

> [!note]- Derivation
> **Key fact: $|\cot(\pi z)|$ is bounded uniformly on $\Gamma_N$.** On the vertical sides $\operatorname{Re} z = \pm(N + 1/2)$: $\cot(\pi z) = \cos(\pi z)/\sin(\pi z)$, and at these vertical lines $\sin(\pi z) = \sin(\pm(N + 1/2)\pi + i\pi y) = \pm\cos(N\pi)\cos(i\pi y) = \pm(-1)^N\cosh(\pi y)$, so $|\sin(\pi z)| = \cosh(\pi y) \geq 1$ for all $y$. Similarly $|\cos(\pi z)| = |\sin(i\pi y)| \leq \sinh(\pi|y|)$. So $|\cot(\pi z)| \leq \tanh(\pi|y|) \leq 1$ on the vertical sides.
>
> On the horizontal sides $\operatorname{Im} z = \pm(N + 1/2)$: $|\cot(\pi z)| = |\cos(\pi z)/\sin(\pi z)|$. With $z = x + iy$ and $|y| = N + 1/2$, $|\cos(\pi z)| \leq \cosh(\pi(N + 1/2))$ and $|\sin(\pi z)| \geq |\sinh(\pi(N + 1/2))|$ (this requires care, but the bound holds for large $N$). So $|\cot(\pi z)| \leq \coth(\pi(N + 1/2)) \to 1$ as $N \to \infty$.
>
> So $|\pi\cot(\pi z)| \leq B$ for some constant $B$ uniform in $N$, on all of $\Gamma_N$.
>
> **ML estimate.** $|1/z^2| \leq 1/(N + 1/2)^2$ on $\Gamma_N$ (distance to origin is at least $N + 1/2$). Length of $\Gamma_N$ is $4(2N + 1) = O(N)$. So
> $$\left|\oint_{\Gamma_N}\frac{\pi\cot(\pi z)}{z^2}\,dz\right| \leq O(N) \cdot \frac{B}{(N + 1/2)^2} = O(1/N) \to 0.$$

**Step 4: Solve for the sum**

> [!note]- Derivation
> Combining Steps 2 and 3: as $N \to \infty$,
> $$0 = 2\pi i\left[-\frac{\pi^2}{3} + 2\sum_{n=1}^\infty\frac{1}{n^2}\right],$$
> so $2\sum_{n=1}^\infty 1/n^2 = \pi^2/3$, hence $\sum_{n=1}^\infty 1/n^2 = \pi^2/6$.

> [!note]- Complete formal solution
> Consider $f(z) = \pi\cot(\pi z)/z^2$. Poles: every $n \in \mathbb{Z}$.
>
> Residues: at $n \neq 0$ (simple poles from $\cot$), $\operatorname{Res}_n f = 1/n^2$. At $n = 0$ (triple pole), using the Laurent expansion $\pi\cot(\pi z) = 1/z - \pi^2 z/3 - \ldots$, we get $\operatorname{Res}_0 f = -\pi^2/3$.
>
> Apply the residue theorem on a square contour $\Gamma_N$ of side $2(N + 1/2)$:
> $$\oint_{\Gamma_N} f\,dz = 2\pi i\left[-\frac{\pi^2}{3} + 2\sum_{n=1}^N\frac{1}{n^2}\right].$$
>
> The integral vanishes as $N \to \infty$: $|\cot(\pi z)|$ is uniformly bounded on $\Gamma_N$ (standard estimate), $|1/z^2| \leq 1/N^2$, contour length $= O(N)$, total $O(1/N)$.
>
> Hence $-\pi^2/3 + 2\sum_{n=1}^\infty 1/n^2 = 0$, giving $\sum_{n=1}^\infty 1/n^2 = \pi^2/6$. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "sum $\sum_n g(n)$ over integers" → "contour-integrate $\pi\cot(\pi z) g(z)$".** This is the master technique for evaluating sums using residues. The function $\pi\cot(\pi z)$ has residue $1$ at every integer, so $\pi\cot(\pi z)\cdot g(z)$ has residue $g(n)$ at each integer $n$ (when $g$ is holomorphic at $n$). The contour integral picks up $\sum g(n)$ plus possible extra residues at poles of $g$.

**The contour-vanishing argument requires $|cot(\pi z)|$ to be bounded uniformly.** This is the key technical step. The boundedness on the *vertical* sides of the square contour (where $|\sin(\pi z)| \geq \cosh(\pi y) \geq 1$) is crucial; the boundedness on horizontal sides follows from the exponential growth of both $\sin$ and $\cos$. The standard "square of side $2(N + 1/2)$" choice is what makes the bound work — taking sides through integers would put zeros of $\sin$ on the contour, breaking everything.

**This bridges complex analysis to (zeta-function-style) number theory without being number theory.** The Basel problem $\sum 1/n^2 = \pi^2/6$ is the simplest of an infinite family: $\sum 1/n^{2k} = (-1)^{k-1}(2\pi)^{2k} B_{2k}/(2(2k)!)$ for Bernoulli numbers $B_{2k}$ (Euler's formula). All these follow from the same template — contour integration of $\pi\cot(\pi z) g(z)$ for suitable $g$. The general framework is *Mellin transforms and Dirichlet series*, which we do not develop here.

**The trick is "sum of residues = 0", not "sum of residues = $2\pi i\,\text{integral}$".** Often the contour integral vanishes by decay, giving the cleaner identity "sum of residues = $0$". This is what makes the technique work for *evaluating* sums (rather than just relating them).

**Other useful "generating" functions for series:**
- $\pi\cot(\pi z)$ for $\sum_n g(n)$.
- $\pi/\sin(\pi z)$ for $\sum_n (-1)^n g(n)$ (alternating sums; the function has residues $(-1)^n$ at integers).
- $\psi(z) = \Gamma'(z)/\Gamma(z)$ (digamma) for similar harmonic-like sums.
