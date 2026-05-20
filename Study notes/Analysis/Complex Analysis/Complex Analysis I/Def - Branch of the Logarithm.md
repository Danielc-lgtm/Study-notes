---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Complex Exponential and Trigonometric Functions"
  - "Def - Holomorphic Function"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}^\times = \mathbb{C} \setminus \{0\}$ is an open subset of the punctured plane. A *branch* is a continuous function $\lambda : U \to \mathbb{C}$ with $\exp(\lambda(z)) = z$. The **principal branch** is denoted $\operatorname{Log}$ (capital $L$), to distinguish it from real $\log = \ln$. The **principal argument** $\operatorname{Arg}(z) \in (-\pi, \pi)$ (or $(-\pi, \pi]$, depending on convention) for $z \in \mathbb{C} \setminus (-\infty, 0]$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Axiom Motivation

The real logarithm is the inverse of the real exponential: $\log x$ is the unique real number whose exponential is $x$, for $x > 0$. The real exponential is *injective* — it is strictly increasing — and so its inverse is single-valued. The complex case is harder because complex $\exp$ is *not* injective: it is periodic with period $2\pi i$, so $\exp(z) = \exp(z + 2\pi i)$, and every nonzero $w \in \mathbb{C}^\times$ has *infinitely many* logarithms, differing by integer multiples of $2\pi i$.

This is the core obstruction: there is no canonical "the" logarithm of $w$. If we want $\log w$ to be a function — a single value for each input — we must *choose* which of the infinitely many candidate values to assign. A **branch** is exactly such a choice, made continuously over an open set: a continuous function $\lambda : U \to \mathbb{C}$ with $\exp(\lambda(z)) = z$ for all $z \in U$. The continuity requirement forces consistency — small changes in $z$ must produce small changes in $\lambda(z)$, ruling out arbitrary point-by-point choices.

Why is the continuous condition strong? Because $\exp$ is a covering map $\mathbb{C} \to \mathbb{C}^\times$ — it is locally invertible (since $\exp'(z) = \exp(z) \neq 0$), but the local inverses *do not glue together* on regions with non-trivial topology. Specifically, if $U$ contains a closed loop $\gamma$ around $0$, then tracing $\lambda$ along $\gamma$ must return to a value differing from the starting value by an integer multiple of $2\pi i$ (the change in argument around the loop). Continuity forces this change to be *the same on every traversal*, but for a function on $U$, the value at the endpoint must equal the starting value — contradiction if the loop has nonzero winding number. So a branch of $\log$ exists on $U$ if and only if $U$ has no closed loop around $0$ — a *topological* condition.

The **principal branch** $\operatorname{Log}$ is the specific choice that is most useful: define it on the slit plane $\mathbb{C} \setminus (-\infty, 0]$ by $\operatorname{Log}(z) = \log|z| + i\operatorname{Arg}(z)$ with $\operatorname{Arg}(z) \in (-\pi, \pi)$ (or $(-\pi, \pi]$). This is well-defined because the slit removes the negative real axis where the argument would jump from $\pi$ to $-\pi$. On any *simply connected* subdomain of $\mathbb{C}^\times$, *some* branch exists — but it may not coincide with $\operatorname{Log}$.

The discipline of always *specifying which branch* before manipulating $\log z$ is one of the hardest disciplines of complex analysis. Identities like $\log(z_1 z_2) = \log z_1 + \log z_2$ are correct *up to a $2\pi i$ shift*, and the shift depends on the branches chosen. This is a permanent source of subtle errors and the reason "branch cuts" appear so frequently in contour integration.

That a branch, when it exists, is automatically holomorphic with derivative $1/z$ is a beautiful consequence of being a continuous inverse of the holomorphic map $\exp$ — by the inverse function theorem applied locally, $\lambda$ is differentiable wherever $\exp' \neq 0$ (everywhere), with $\lambda'(z) = 1/\exp'(\lambda(z)) = 1/z$.

---

# The Definition

Let $U \subseteq \mathbb{C}^\times$ be open.

**Branch of the logarithm.** A **branch of the logarithm on $U$** is a continuous function $\lambda : U \to \mathbb{C}$ such that
$$\exp(\lambda(z)) = z \qquad \text{for all } z \in U.$$

**Properties of branches.** Whenever a branch $\lambda$ exists on $U$:
1. $\lambda$ is holomorphic on $U$ with $\lambda'(z) = 1/z$.
2. Any two branches $\lambda_1, \lambda_2$ on $U$ differ by a constant $2\pi i k$ for some integer $k \in \mathbb{Z}$.

**Principal branch.** Let $U_0 = \mathbb{C} \setminus (-\infty, 0] = \{z \in \mathbb{C}^\times : z \notin (-\infty, 0]\}$ — the **slit plane**. The **principal branch** of the logarithm is
$$\operatorname{Log}(z) := \log|z| + i \operatorname{Arg}(z), \qquad z \in U_0,$$
where $\log|z|$ is the real natural logarithm of the modulus, and $\operatorname{Arg}(z) \in (-\pi, \pi)$ is the unique argument of $z$ in this open interval.

When the domain is clear and one is using the principal branch, we often write just $\log z$ for $\operatorname{Log}(z)$.

**Existence criterion.** A branch of the logarithm exists on an open $U \subseteq \mathbb{C}^\times$ if and only if there is no closed curve in $U$ with nonzero winding number around $0$. In particular, branches exist on every simply connected $U \subseteq \mathbb{C}^\times$ but *not* on the full punctured plane $\mathbb{C}^\times$. See [[Thm - Existence of a Logarithm on Simply Connected Domains]].

---

# Relate to Other Fields / Compression

In **topology**, the existence of a continuous logarithm on $U \subseteq \mathbb{C}^\times$ is the statement that the inclusion $U \hookrightarrow \mathbb{C}^\times$ lifts through the covering map $\exp : \mathbb{C} \to \mathbb{C}^\times$. Lifting criteria from covering space theory ($\pi_1(U) \to \pi_1(\mathbb{C}^\times) = \mathbb{Z}$ trivial) give the topological characterization.

In **algebraic geometry**, the multivalued nature of $\log$ is captured by working on the **universal cover** of $\mathbb{C}^\times$, which is $\mathbb{C}$ itself via the map $z \mapsto e^z$. The logarithm becomes single-valued on this cover. This is the entry point to Riemann surface theory.

In **differential equations**, $\log z$ is the integral $\int_1^z dw/w$, taken along any path from $1$ to $z$ in $U$. The path-dependence of the integral (it changes by $2\pi i$ for each winding around $0$) is exactly the multivaluedness of the logarithm. This identifies $\log$ with the antiderivative of $1/z$ and links the branch theory to [[Def - Primitive (Antiderivative)|primitives]] in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]].

---

# Examples / Corollaries

**Is an instance — the principal branch on the slit plane.** $\operatorname{Log}(z) = \log|z| + i\operatorname{Arg}(z)$ for $z \in \mathbb{C} \setminus (-\infty, 0]$. Continuous because $\operatorname{Arg}$ is continuous on this domain. Verify $\exp(\operatorname{Log}(z)) = e^{\log|z|}(\cos\operatorname{Arg}(z) + i\sin\operatorname{Arg}(z)) = |z|(\cos\operatorname{Arg}(z) + i\sin\operatorname{Arg}(z)) = z$.

**Is an instance — branch on the upper half-plane.** $U = \{z : \operatorname{Im} z > 0\}$ is simply connected and avoids $0$, so a branch exists. One natural choice: $\lambda(z) = \log|z| + i\theta(z)$ with $\theta(z) \in (0, \pi)$ the argument in the upper half-plane.

**Is an instance — different branches on the same domain.** On the slit plane, the function $\operatorname{Log}(z) + 2\pi i$ is also a branch (since $\exp$ of it equals $z$). It differs from the principal branch by the constant $2\pi i$.

**Is NOT an instance — no branch exists on the punctured plane $\mathbb{C}^\times$.** The unit circle $|z| = 1$ has winding number $1$ around $0$. Any branch $\lambda$ on $\mathbb{C}^\times$ would have $\lambda(e^{i\cdot 2\pi}) - \lambda(e^{i\cdot 0}) = 2\pi i$ (by tracing the argument), but $\lambda$ is single-valued, so the difference is $0$ — contradiction. See [[Ex - Failure of log existence on the punctured plane]].

**Is NOT an instance of a continuous extension — $\operatorname{Log}$ does not extend continuously across the negative real axis.** As $z \to -1$ from above, $\operatorname{Log}(z) \to i\pi$; from below, $\operatorname{Log}(z) \to -i\pi$. The jump of $2\pi i$ is the periodicity of $\exp$ made manifest.

**Corollary — $\operatorname{Log}(1) = 0$, $\operatorname{Log}(i) = i\pi/2$, $\operatorname{Log}(-i) = -i\pi/2$.** Direct from the formula with $|1| = |i| = |-i| = 1$ and $\operatorname{Arg}(1) = 0, \operatorname{Arg}(i) = \pi/2, \operatorname{Arg}(-i) = -\pi/2$.

**Corollary — derivative of the principal branch.** $\operatorname{Log}'(z) = 1/z$ on the slit plane. This is the chain rule on $\exp(\operatorname{Log}(z)) = z$: $\exp(\operatorname{Log}(z)) \cdot \operatorname{Log}'(z) = 1$, so $\operatorname{Log}'(z) = 1/\exp(\operatorname{Log}(z)) = 1/z$.

**Calibration check.** Compute $\operatorname{Log}(1 + i) = \log\sqrt 2 + i\pi/4$ (modulus $\sqrt 2$, argument $\pi/4$). Check that for a non-principal branch defined on $\mathbb{C} \setminus [0, \infty)$ (slit along the positive real axis instead), the value of $\log(-1)$ is $-i\pi$ (since the argument range there is $(0, 2\pi)$ or $(-2\pi, 0)$, depending on convention). Different domain, different branch, different values.

---

# Unlocked by This

> [!tip] Complex Powers *(from this topic)*
> Once a branch of $\log$ is chosen, [[Def - Complex Power|complex powers]] $z^\alpha = \exp(\alpha \log z)$ are well-defined. The branch ambiguity of $\log$ propagates: $z^\alpha$ for non-integer $\alpha$ is multivalued by factors of $e^{2\pi i \alpha k}$.

> [!tip] Contour Integration with Branch Cuts *(from CA III)*
> Integrals like $\int_0^\infty x^{\alpha-1}/(1+x)\,dx$ are evaluated by contour integration on a "keyhole" contour around a branch cut for $z^{\alpha-1}$. The branch cut is the engine of the computation.

> [!tip] Riemann Surfaces *(from Complex Geometry)*
> The multivaluedness of $\log$ is best captured on the **Riemann surface of the logarithm** — the universal cover $\mathbb{C} \to \mathbb{C}^\times$ via $z \mapsto e^z$, on which $\log$ becomes single-valued. This is the prototype example of a Riemann surface.
