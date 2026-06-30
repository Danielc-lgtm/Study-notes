---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Exterior Derivative"
  - "Def - The Hodge Star"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\vec{v}$ be a vector field on a spacelike hyperplane $\Sigma$ (the $x^0 = 0$ slice) of flat spacetime, with metric-dual $1$-form $\underline{v}$ (components $v_i$). Show that the curl of $\vec{v}$ is recovered from the exterior derivative of $\underline{v}$ followed by a Hodge star.

1. Compute the components of the $2$-form $\mathbf{d}\underline{v}$ and confirm they are $(\mathbf{d}\underline{v})_{\alpha\beta} = \partial_\alpha v_\beta - \partial_\beta v_\alpha$, with **no** Christoffel terms.
2. Define the curl as $\boldsymbol{\nabla}\times\vec{v} := \star\mathbf{d}\underline{v}$ restricted to $\Sigma$ (a vector via the metric dual) and, working in inertial Cartesian coordinates with a right-handed orthonormal basis, show its components are $(\boldsymbol{\nabla}\times\vec{v})^i = \epsilon^{ijk}\partial_j v_k$, the standard Cartesian curl.
3. Use the result to explain why the two classical vector-calculus identities $\boldsymbol{\nabla}\times(\boldsymbol{\nabla}f) = 0$ and $\boldsymbol{\nabla}\cdot(\boldsymbol{\nabla}\times\vec{v}) = 0$ are both instances of $\mathbf{d}^2 = 0$.

**Recall:**

![[Def - The Exterior Derivative#The Definition]]

The Hodge star $\star$ sends a $2$-form on a $3$-space to a $1$-form (and conversely); on the Levi-Civita tensor $\epsilon_{ijk}$ of the orthonormal spatial frame, $(\star\mathbf{d}\underline{v})^i \propto \epsilon^{ijk}(\mathbf{d}\underline{v})_{jk}$ (see [[Def - The Hodge Star]]).

---

# Convergent Strategy

**Problem class.** A *recognise-a-vector-calculus-operator-in-disguise* problem (operation 9 from the topic page). The route is: form $\mathbf{d}\underline{v}$ (partial derivatives only), take the Hodge dual, and match against the Cartesian curl.

**Assumption pattern.** A $1$-form on a $3$-space; the Hodge star on a $3$-space sends $2$-forms to $1$-forms (i.e. vectors via the metric), which is exactly the dimension count that makes the curl a vector in three dimensions. The orthonormal right-handed basis is needed so that $\epsilon^{ijk}$ is the ordinary Levi-Civita symbol.

**Theorem routing.** Part 1 uses the exterior-derivative formula of [[Def - The Exterior Derivative]] and the cancellation of Christoffels. Part 2 applies the Hodge star of [[Def - The Hodge Star]]. Part 3 invokes $\mathbf{d}^2 = 0$ from [[Thm - Properties of the Exterior Derivative]].

**Key decision point.** The crux is that the curl is special to three dimensions because only there does the Hodge star carry a $2$-form (which $\mathbf{d}$ of a $1$-form always is) back to a $1$-form. In four dimensions $\mathbf{d}\underline{v}$ stays a $2$-form (the electromagnetic field strength), which is why "curl" generalises to "$\mathbf{d}$ of a $1$-form" rather than to a vector.

---

# Legal Operations Used

1. **Antisymmetrise to get the exterior derivative, then drop the Christoffels** (operation 6 from the topic page) for Part 1.
2. **Recognise a vector-calculus operator in disguise and convert** (operation 9 from the topic page) for Part 2.
3. **Use $\mathbf{d}^2 = 0$** (operation 7 from the topic page) for Part 3.

---

# Hints

> [!note]- Hint 1
> $(\mathbf{d}\underline{v})_{\alpha\beta} = \nabla_\alpha v_\beta - \nabla_\beta v_\alpha$. Write out the Christoffel terms: $-\Gamma^\mu{}_{\beta\alpha}v_\mu + \Gamma^\mu{}_{\alpha\beta}v_\mu$. By symmetry $\Gamma^\mu{}_{\alpha\beta} = \Gamma^\mu{}_{\beta\alpha}$ they cancel, leaving $\partial_\alpha v_\beta - \partial_\beta v_\alpha$.

> [!note]- Hint 2
> The independent components of the antisymmetric $(\mathbf{d}\underline{v})_{ij}$ are $(\mathbf{d}\underline{v})_{12} = \partial_1 v_2 - \partial_2 v_1$, $(\mathbf{d}\underline{v})_{23} = \partial_2 v_3 - \partial_3 v_2$, $(\mathbf{d}\underline{v})_{31} = \partial_3 v_1 - \partial_1 v_3$ — exactly the three components of the curl.

> [!note]- Hint 3
> The Hodge star packages the antisymmetric $2$-form into a vector: $(\star\mathbf{d}\underline{v})^i = \tfrac12\epsilon^{ijk}(\mathbf{d}\underline{v})_{jk} = \epsilon^{ijk}\partial_j v_k$. For example $(\boldsymbol{\nabla}\times\vec{v})^1 = \epsilon^{1jk}\partial_j v_k = \partial_2 v_3 - \partial_3 v_2$.

> [!note]- Hint 4
> $\boldsymbol{\nabla}\times\boldsymbol{\nabla}f$ is $\star\mathbf{d}(\mathbf{d}f) = \star\,\mathbf{d}^2 f = 0$. And $\boldsymbol{\nabla}\cdot(\boldsymbol{\nabla}\times\vec{v})$ involves $\mathbf{d}$ of the $2$-form $\mathbf{d}\underline{v}$, i.e. $\mathbf{d}^2\underline{v} = 0$. Both vanish for the *same* reason.

---

# Solution

The plan: Step 1 computes $\mathbf{d}\underline{v}$ and notes the Christoffels cancel. Step 2 takes the Hodge dual and matches the Cartesian curl. Step 3 derives the two classical curl identities from $\mathbf{d}^2 = 0$.

**Step 1: $\mathbf{d}\underline{v}$ has only partial-derivative components.**

> [!note]- Derivation
> By the exterior-derivative formula, $(\mathbf{d}\underline{v})_{\alpha\beta} = \nabla_\alpha v_\beta - \nabla_\beta v_\alpha$. Expand the covariant derivatives:
> $$(\mathbf{d}\underline{v})_{\alpha\beta} = (\partial_\alpha v_\beta - \Gamma^\mu{}_{\beta\alpha}v_\mu) - (\partial_\beta v_\alpha - \Gamma^\mu{}_{\alpha\beta}v_\mu) = \partial_\alpha v_\beta - \partial_\beta v_\alpha + (\Gamma^\mu{}_{\alpha\beta} - \Gamma^\mu{}_{\beta\alpha})v_\mu.$$
> The coordinate-basis Christoffels are symmetric, $\Gamma^\mu{}_{\alpha\beta} = \Gamma^\mu{}_{\beta\alpha}$, so the last bracket vanishes:
> $$(\mathbf{d}\underline{v})_{\alpha\beta} = \frac{\partial v_\beta}{\partial x^\alpha} - \frac{\partial v_\alpha}{\partial x^\beta}.$$
> This holds in *any* coordinate system, with no connection terms — the exterior derivative is metric-free. The independent spatial components are $(\mathbf{d}\underline{v})_{12} = \partial_1 v_2 - \partial_2 v_1$, $(\mathbf{d}\underline{v})_{23} = \partial_2 v_3 - \partial_3 v_2$, $(\mathbf{d}\underline{v})_{31} = \partial_3 v_1 - \partial_1 v_3$.

**Step 2: The Hodge dual is the Cartesian curl.**

> [!note]- Derivation
> Work in inertial Cartesian coordinates on $\Sigma$ with a right-handed orthonormal basis, so the spatial Levi-Civita symbol is the ordinary $\epsilon^{ijk}$ with $\epsilon^{123} = +1$ (and metric-duality just lowers/raises with $\delta_{ij}$ up to sign). The Hodge star sends the $2$-form $\mathbf{d}\underline{v}$ on the $3$-space $\Sigma$ to a $1$-form, whose vector dual has components
> $$(\boldsymbol{\nabla}\times\vec{v})^i := (\star\mathbf{d}\underline{v})^i = \tfrac12\,\epsilon^{ijk}(\mathbf{d}\underline{v})_{jk} = \tfrac12\,\epsilon^{ijk}(\partial_j v_k - \partial_k v_j) = \epsilon^{ijk}\partial_j v_k,$$
> using the antisymmetry of $\epsilon^{ijk}$ to combine the two terms. Componentwise:
> $$(\boldsymbol{\nabla}\times\vec{v})^1 = \partial_2 v_3 - \partial_3 v_2, \quad (\boldsymbol{\nabla}\times\vec{v})^2 = \partial_3 v_1 - \partial_1 v_3, \quad (\boldsymbol{\nabla}\times\vec{v})^3 = \partial_1 v_2 - \partial_2 v_1.$$
> These are exactly the components of the standard Cartesian curl $\nabla\times\mathbf{v}$. So the curl *is* the Hodge dual of the exterior derivative of the metric-dual $1$-form — the exterior derivative is a generalised curl, and in three dimensions the Hodge star repackages it as a vector.

**Step 3: Both classical curl identities are $\mathbf{d}^2 = 0$.**

> [!note]- Derivation
> *Curl of a gradient.* The gradient is $\mathbf{d}f$ (a $1$-form), so its curl is $\boldsymbol{\nabla}\times\boldsymbol{\nabla}f = \star\mathbf{d}(\mathbf{d}f) = \star(\mathbf{d}^2 f) = \star\,0 = 0$. Hence $\boldsymbol{\nabla}\times\boldsymbol{\nabla}f = 0$ for every scalar $f$ — because $\mathbf{d}^2 f = 0$ (equality of mixed partials).
>
> *Divergence of a curl.* The curl $\boldsymbol{\nabla}\times\vec{v}$ corresponds to the $2$-form $\mathbf{d}\underline{v}$, and its divergence corresponds (via the codifferential identity $\boldsymbol{\nabla}\!\cdot\sim\star\mathbf{d}\star$) to applying $\mathbf{d}$ again: it involves $\mathbf{d}(\mathbf{d}\underline{v}) = \mathbf{d}^2\underline{v} = 0$. Hence $\boldsymbol{\nabla}\cdot(\boldsymbol{\nabla}\times\vec{v}) = 0$ for every field $\vec{v}$.
>
> Both identities are therefore the *single* statement $\mathbf{d}^2 = 0$ — applied to a $0$-form $f$ in the first case and to a $1$-form $\underline{v}$ in the second. This is why the two facts, which look unrelated in vector-calculus notation and are usually proved by separate index manipulations, are the same theorem: the nilpotency of the exterior derivative, which is itself just the equality of mixed partial derivatives.

> [!note]- Complete formal solution
> $(\mathbf{d}\underline{v})_{\alpha\beta} = \nabla_\alpha v_\beta - \nabla_\beta v_\alpha = \partial_\alpha v_\beta - \partial_\beta v_\alpha$ (the symmetric Christoffel terms cancel). In Cartesian coordinates on $\Sigma$ with a right-handed orthonormal basis, the Hodge dual is $(\boldsymbol{\nabla}\times\vec{v})^i = \tfrac12\epsilon^{ijk}(\mathbf{d}\underline{v})_{jk} = \epsilon^{ijk}\partial_j v_k$, the standard Cartesian curl. The identities $\boldsymbol{\nabla}\times\boldsymbol{\nabla}f = \star\mathbf{d}\mathbf{d}f = 0$ and $\boldsymbol{\nabla}\cdot(\boldsymbol{\nabla}\times\vec{v}) \sim \mathbf{d}\mathbf{d}\underline{v} = 0$ are both the nilpotency $\mathbf{d}^2 = 0$. $\blacksquare$

---

# Key Takeaways

**The curl is the Hodge dual of the exterior derivative, and "$\mathbf{d}$ of a $1$-form" is the dimension-independent generalisation.** The classical curl is a three-dimensional accident: the exterior derivative of a $1$-form is always a $2$-form, and only in three dimensions does the Hodge star carry a $2$-form back to a $1$-form (a vector). So the operation "take the antisymmetrised derivative $\partial_{[i}v_{j]}$" — the genuine content — generalises to all dimensions as $\mathbf{d}\underline{v}$, while its repackaging as a vector via $\star$ is special to $\mathbb{R}^3$. On four-dimensional spacetime, $\mathbf{d}A$ of the electromagnetic potential $1$-form stays a $2$-form, the field strength $F$, whose six components are the three electric and three magnetic field components — the "spacetime curl" of the potential. The transferable insight is to think of curl not as "$\nabla\times$" but as "$\mathbf{d}$ of a $1$-form", which tells you immediately how it behaves in any dimension and on any (even curved) space.

**The Christoffel symbols cancel in the curl because antisymmetrisation kills the symmetric connection — this is why curl needs no metric.** A reader who has just learned the covariant derivative might expect the curl, being a derivative, to carry Christoffel corrections; it does not, and the reason is the heart of why the exterior derivative is special. The covariant derivative $\nabla_\alpha v_\beta$ has a symmetric Christoffel term $-\Gamma^\mu{}_{\beta\alpha}v_\mu$; the antisymmetrisation $\nabla_\alpha v_\beta - \nabla_\beta v_\alpha$ subtracts $-\Gamma^\mu{}_{\alpha\beta}v_\mu$, and the two cancel by $\Gamma^\mu{}_{\alpha\beta} = \Gamma^\mu{}_{\beta\alpha}$. So the curl is built from partial derivatives alone and is the same in every coordinate system — which is exactly why $\nabla\times\mathbf{v}$ has the same form in Cartesian coordinates regardless of any background structure, and why the homogeneous Maxwell equations are coordinate-invariant. The diagnostic is: whenever you antisymmetrise a covariant derivative, drop the Christoffels and use partials.

**The two classical curl identities are one theorem, $\mathbf{d}^2 = 0$, applied to a $0$-form and a $1$-form.** Vector calculus presents $\nabla\times\nabla f = 0$ and $\nabla\cdot(\nabla\times\mathbf{v}) = 0$ as two separate identities, each proved by its own index juggling, and they feel like coincidences. They are the same fact: the exterior derivative is nilpotent, $\mathbf{d}^2 = 0$, and applying this to the $0$-form $f$ gives the first identity (gradient is closed) while applying it to the $1$-form $\underline{v}$ gives the second (the curl-$2$-form is closed). The underlying reason is the most elementary fact in calculus — mixed partial derivatives commute. Recognising that "curl grad $= 0$" and "div curl $= 0$" are two readings of $\mathbf{d}^2 = 0$ is the kind of unification the exterior calculus exists to provide, and it is the seed of the homogeneous Maxwell equations $\mathbf{d}F = 0$, which are *also* an instance of nilpotency since $F = \mathbf{d}A$.
