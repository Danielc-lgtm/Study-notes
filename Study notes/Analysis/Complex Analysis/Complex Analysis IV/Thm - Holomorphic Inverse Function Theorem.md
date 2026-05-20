---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Local Mapping Degree"
  - "Def - Holomorphic Function"
  - "Def - Conformal Map"
tags: [analysis, complex-analysis]
---

# Notation

$f$ is holomorphic at $a$ with $f'(a) \neq 0$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Motivation

The holomorphic inverse function theorem is the complex-analytic analog of the [[Thm - The Inverse Function Theorem|real inverse function theorem]]. It says: if $f$ is holomorphic at $a$ with $f'(a) \neq 0$, then $f$ is locally a biholomorphism — there exist neighborhoods of $a$ and $f(a)$ between which $f$ is a holomorphic bijection with holomorphic inverse.

This is automatic from the local mapping degree theorem (the case $k = 1$): when $f'(a) \neq 0$, the local mapping degree is $1$, so $f$ is locally $1$-to-$1$, hence locally bijective.

The remarkable feature: in the holomorphic setting, the inverse function theorem requires *less*. In the real case, one needs the full Jacobian determinant to be nonzero (an $n \times n$ matrix condition); in the complex case, just $f'(a) \neq 0$ (a single number condition). And the inverse is automatically *holomorphic*, not just differentiable.

The theorem characterizes when a holomorphic function is *conformal* (preserves angles, see [[Def - Conformal Map]]): $f'(a) \neq 0$ is exactly the conformality condition. So this theorem says **a holomorphic function is locally a conformal equivalence exactly where its derivative is nonzero**.

---

# Sources and Targets

**Sources (Input Broadening)**

**$f'(a) \neq 0$.** The precondition. Common situations:

**$f$ is a polynomial with no critical point at $a$.** $f'$ is a polynomial; check $f'(a) \neq 0$ directly.

**$f$ is an exponential or trigonometric function.** $e^z$ has $f'(z) = e^z \neq 0$ everywhere; $\sin z$ has $f'(z) = \cos z \neq 0$ wherever $\cos z \neq 0$. So such functions are locally biholomorphic everywhere outside critical points.

**$f$ is a Möbius transformation.** $f(z) = (az + b)/(cz + d)$ has $f'(z) = (ad - bc)/(cz + d)^2 \neq 0$ everywhere (since $ad - bc \neq 0$). So Möbius maps are conformal automorphisms of $\hat{\mathbb{C}}$ — locally biholomorphic at every point.

**Targets (Output Amplification)**

Combine with **the global injectivity question.** Property $D$: $f'$ is nonzero on a domain $D$. Amplified result $E$: $f$ is locally injective at every point of $D$; *global* injectivity is *not* implied (this is the local-vs-global distinction). For instance, $e^z$ has $f' = e^z \neq 0$ everywhere but is not globally injective (it's $2\pi i$-periodic).

Combine with **Riemann mapping construction.** Property $D$: building biholomorphisms between domains. Amplified result $E$: candidate maps are constructed by composing holomorphic functions with nonzero derivatives at the relevant points.

Combine with **change-of-variables in integrals.** Property $D$: a holomorphic substitution $z = f(w)$ in a contour integral. Amplified result $E$: $\int g(z)\,dz = \int g(f(w)) f'(w)\,dw$. The change-of-variables is licensed by the local biholomorphism.

---

# Why Is It True

The proof is immediate from the [[Thm - Local Mapping Degree|local mapping degree theorem]] with $k = 1$.

If $f'(a) \neq 0$, then $f - f(a)$ has a simple zero at $a$ (since $f(z) - f(a) = f'(a)(z - a) + O((z - a)^2)$, the leading term is $f'(a)(z - a)$ with $f'(a) \neq 0$). So the local degree is $1$.

By local mapping degree, for $w$ sufficiently close to $f(a)$, the equation $f(z) = w$ has exactly one solution in a small disc around $a$. So $f$ is locally injective (and surjective onto its image), hence a bijection between a neighborhood of $a$ and a neighborhood of $f(a)$.

The inverse $g = f^{-1}$ is automatically holomorphic: $g$ is continuous (by Lebesgue's theorem on inverses of continuous bijections from open sets), and differentiable at $f(a)$ with $g'(f(a)) = 1/f'(a)$ (chain rule). Since $f'$ is holomorphic and nonzero near $a$, $1/f'$ is holomorphic, and so is $g$.

---

# What Makes This Hard

The non-obvious step is *that the holomorphic version requires less than the real version*. In the real case, the multidimensional inverse function theorem requires the Jacobian matrix to be invertible (a determinant condition on $n^2$ entries). In the complex case, viewed as 2-dimensional real, the Jacobian is the $2 \times 2$ matrix $\begin{pmatrix}u_x & u_y \\ v_x & v_y\end{pmatrix} = \begin{pmatrix}\operatorname{Re} f' & -\operatorname{Im} f' \\ \operatorname{Im} f' & \operatorname{Re} f'\end{pmatrix}$ (using Cauchy-Riemann), with determinant $|f'|^2$. So Jacobian invertible ⟺ $f'(a) \neq 0$, automatically. The single complex condition encodes the full Jacobian condition.

A common mistake is to think the theorem gives a global inverse; it only gives a *local* inverse. The exponential $e^z$ has $f' \neq 0$ everywhere but is $2\pi i$-periodic; its inverse $\log z$ is multivalued.

---

# Rederivation Scaffold

**High-level strategy:**
Apply the local mapping degree theorem with $k = 1$. The $k = 1$ case gives local bijectivity. The inverse is holomorphic by the chain rule plus holomorphicity of $1/f'$.

**Subgoal decomposition:**

1. **Identify $k = 1$.** From $f'(a) \neq 0$, conclude $\operatorname{ord}_a(f - f(a)) = 1$.

2. **Apply local mapping degree.** For $w$ near $f(a)$, $f(z) = w$ has exactly $1$ solution near $a$.

3. **Local bijection.** $f$ is locally a bijection from a neighborhood $U_0 \ni a$ to a neighborhood $V_0 \ni f(a)$.

4. **Inverse is holomorphic.** $g = f^{-1}$ satisfies $f(g(w)) = w$; differentiate with the chain rule to get $g'(w) = 1/f'(g(w))$. RHS is holomorphic in $w$, so $g$ is holomorphic.

---

# Formal Proof

> [!note]- Complete formal proof
> Suppose $f$ is holomorphic at $a$ with $f'(a) \neq 0$.
>
> **Step 1.** $f(z) - f(a) = f'(a)(z - a) + O((z - a)^2)$, a zero of order $1$ at $a$. So the local mapping degree $k$ at $a$ is $1$.
>
> **Step 2.** By [[Thm - Local Mapping Degree|local mapping degree]], there exist $r, \epsilon > 0$ such that for every $w$ with $|w - f(a)| < \epsilon$, the equation $f(z) = w$ has exactly $1$ solution in $D(a, r)$. So $f$ restricted to $D(a, r) \cap f^{-1}(D(f(a), \epsilon))$ is a bijection to $D(f(a), \epsilon)$, and we can take $U_0$ = this intersection (open) and $V_0 = D(f(a), \epsilon)$ (open).
>
> **Step 3.** Let $g : V_0 \to U_0$ be the inverse. $g$ is continuous because $f$ is open (open mapping theorem, derived from local mapping degree — or directly: $f$ on $U_0$ is a continuous bijection from an open set to an open set, so $f^{-1}$ is continuous by general topology).
>
> **Step 4.** $g$ is differentiable at $w = f(a)$:
> $$\lim_{w \to f(a)} \frac{g(w) - g(f(a))}{w - f(a)} = \lim_{w \to f(a)}\frac{g(w) - a}{f(g(w)) - f(a)}.$$
> Setting $z = g(w)$, as $w \to f(a)$ we have $z \to a$ (by continuity of $g$), so the limit equals $\lim_{z \to a}(z - a)/(f(z) - f(a)) = 1/f'(a)$.
>
> Similarly, $g$ is differentiable at every $w \in V_0$ with $g'(w) = 1/f'(g(w))$. Since $g$ is differentiable on all of $V_0$, it is holomorphic on $V_0$, with the explicit formula above.
>
> **Conformality.** $f$ is conformal at $a$ (preserves angles) iff $f'(a) \neq 0$, which is our hypothesis. The theorem confirms that conformal-at-$a$ ⟺ locally biholomorphic at $a$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Exponential as local biholomorphism.** $e^z$ has $(e^z)' = e^z \neq 0$ everywhere. So $e^z$ is locally biholomorphic at every $z \in \mathbb{C}$. Local inverse near $z = 0$: $\log w$ near $w = 1$, on a simply connected neighborhood. Globally, $e^z$ is $2\pi i$-periodic, so not globally injective.

**Power functions as local biholomorphisms.** $z^n$ has $(z^n)' = nz^{n-1} = 0$ at $z = 0$; so $z^n$ is *not* locally biholomorphic at $0$ (the local degree is $n$, not $1$). It *is* locally biholomorphic at every other point. The branch points of $z^{1/n}$ correspond to the failure of local invertibility at $0$.

**Möbius maps as global biholomorphisms.** Every Möbius transformation is globally biholomorphic on $\hat{\mathbb{C}}$. The local theorem gives biholomorphism at each point; the global structure is given by the group property.

**Change of variables in contour integrals.** Substituting $z = f(w)$ in $\int g(z)\,dz$ gives $\int g(f(w))f'(w)\,dw$. The licensing comes from $f$ being a local biholomorphism on each subarc.

---

# Bridges

- **[[Thm - Local Mapping Degree]]** — the $k = 1$ case of local degree gives this theorem.

- **[[Thm - The Inverse Function Theorem]]** — the real analog (from multivariate analysis).

- **[[Def - Conformal Map]]** — $f'(a) \neq 0$ is exactly the conformality condition.

- **[[Thm - Cauchy–Riemann Equations]]** — the complex Jacobian determinant is $|f'|^2$, nonzero iff $f' \neq 0$.

---

# Unlocked by This

> [!tip] Riemann Mapping Theorem *(from §3.5+)*
> The [[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping theorem]] gives global biholomorphisms; the local version is needed in its proof.

> [!tip] Holomorphic Manifolds *(from Complex Geometry)*
> A **complex manifold** is locally biholomorphic to $\mathbb{C}^n$. The local biholomorphisms are the holomorphic functions with full-rank derivative; in dimension $1$, these are the maps with $f' \neq 0$.
