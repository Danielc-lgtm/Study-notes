---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Branch of the Logarithm"
  - "Def - Domain in the Complex Plane"
  - "Thm - Properties of the Complex Exponential"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}^\times = \mathbb{C} \setminus \{0\}$ — an open subset avoiding the origin. **Simply connected** means: every closed curve in $U$ is contractible to a point inside $U$, equivalently $U$ has trivial fundamental group. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Statement

> **Theorem (existence of a logarithm on simply connected domains).** Let $U \subseteq \mathbb{C}^\times = \mathbb{C} \setminus \{0\}$ be a simply connected domain. Then there exists a holomorphic [[Def - Branch of the Logarithm|branch of the logarithm]] $\lambda : U \to \mathbb{C}$, i.e., a holomorphic function satisfying $\exp(\lambda(z)) = z$ for all $z \in U$, and its derivative is $\lambda'(z) = 1/z$. The branch is unique up to an additive constant in $2\pi i \mathbb{Z}$, fixed by choosing a base point $z_0 \in U$ and a value $\lambda_0 \in \exp^{-1}(z_0)$.
>
> Conversely, if a branch of $\log$ exists on a domain $U \subseteq \mathbb{C}^\times$, then every closed piecewise $C^1$ curve $\gamma$ in $U$ has winding number zero around the origin: $\int_\gamma dw/w = 0$.

---

# Motivation

We want a function $\log z$ on the largest possible domain. Since $\exp : \mathbb{C} \to \mathbb{C}^\times$ is surjective but $2\pi i$-periodic, a continuous inverse — a [[Def - Branch of the Logarithm|branch of the logarithm]] — must "choose" one of the infinitely many pre-images at each $z$, consistently. This choice obstructs at *loops* in the domain: tracing a path around the origin once, the argument changes by $2\pi$ continuously, and the chosen branch must change by $2\pi i$ — but a single-valued function on a domain cannot do that.

The theorem identifies the precise obstruction: a branch exists on $U$ iff $U$ has no closed curve with nonzero winding number around $0$. For simply connected $U \subseteq \mathbb{C}^\times$, every closed curve has winding number $0$ (since the curve is contractible to a point, which has winding zero). So branches exist on every simply connected $U \subseteq \mathbb{C}^\times$.

This is the first place complex analysis meets topology: the *topological* property "simply connected" determines an *analytic* property "branches of $\log$ exist". The same pattern repeats throughout the subject: existence of antiderivatives, existence of harmonic conjugates, validity of Cauchy's theorem — all are governed by the topology of the domain.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$U$ simply connected, $U \subseteq \mathbb{C}^\times$".

The first disguised source is **a star-shaped or convex subdomain of $\mathbb{C}^\times$**: every such set is simply connected (closed curves contract via the star-segment homotopy). *Example:* the open right half-plane, the slit plane, any disc not containing $0$.

The second disguised source is **a contractible open subset of $\mathbb{C}^\times$**: by definition, contractibility means there is a homotopy of the identity to a point, which automatically makes the space simply connected.

The third disguised source is **a domain obtained by deleting a half-line from $\mathbb{C}$, where the half-line passes through $0$**: e.g., the slit plane $\mathbb{C} \setminus (-\infty, 0]$. The slit "cuts" the obstructing loop and makes the resulting domain simply connected.

**Targets (Output Amplification)**

The conclusion is "a branch $\lambda : U \to \mathbb{C}$ with $\exp(\lambda(z)) = z$ exists, and is holomorphic with $\lambda'(z) = 1/z$".

Combine with **a base point.** Property $D$: a choice of base point $z_0 \in U$ and a choice of value $\lambda_0 \in \mathbb{C}$ with $\exp(\lambda_0) = z_0$. The amplified result: $\lambda$ is *uniquely* determined by these choices. So branches are a finite (countable) family parametrized by the choice of $\lambda_0$ (which is unique up to $2\pi i \mathbb{Z}$).

Combine with **complex powers.** Property $D$: an exponent $\alpha \in \mathbb{C}$. The amplified result: a single-valued $z^\alpha = \exp(\alpha \lambda(z))$ on $U$. So every simply connected $U \subseteq \mathbb{C}^\times$ supports single-valued complex powers, with branch-dependence captured by the choice of $\lambda$.

Combine with **primitives.** Property $D$: a primitive of $1/z$. The amplified result: $\lambda$ *is* a primitive of $1/z$ on $U$ (since $\lambda' = 1/z$). So the existence of branches of $\log$ is equivalent to the existence of primitives of $1/z$.

---

# Why Is It True

The intuition is purely topological: we want to *trace* the value of $\log z$ along paths in $U$. Pick a base point $z_0$, choose a base value $\lambda_0 \in \exp^{-1}(z_0)$, and define $\lambda(z) :=$ the value obtained by tracing continuously along any path from $z_0$ to $z$. The procedure is well-defined iff the traced value is *path-independent* — which, by the **monodromy theorem**, holds iff there is no loop with nonzero winding around the origin.

For simply connected $U$, *every* loop is null-homotopic, hence contracts to a point, and the value traced around it returns to the starting value. So the path-integral construction is single-valued, and $\lambda$ is a branch.

Concretely, the formula is $\lambda(z) = \int_{z_0}^z dw/w + \lambda_0$, the integral taken along any path in $U$ from $z_0$ to $z$. Path-independence follows from $\int_\gamma dw/w = 0$ for every closed $\gamma$ in $U$ (since $\gamma$ has winding zero — proved using Cauchy's theorem on $U$, anticipating CA II material; or more elementarily via the homotopy structure).

The other direction — "if a branch exists on $U$ then every closed curve in $U$ has winding number zero around $0$" — is direct: if $\lambda$ is a branch and $\gamma$ is a closed curve in $U$, then $\lambda(\gamma(t))$ is single-valued and equals $\log r(t) + i\theta(t)$ for some continuous $r, \theta$; closing the curve forces $\theta(b) = \theta(a)$, i.e., zero winding.

---

# What Makes This Hard

The non-obvious step is the *monodromy* argument: that the value obtained by tracing along a path is path-independent in a simply connected domain. The technical heart is showing $\int_\gamma dw/w = 0$ for closed curves in simply connected $U \subseteq \mathbb{C}^\times$ — which is Cauchy's theorem applied to the holomorphic function $1/w$ on $U$. The most common error is to think the obstruction is just "the loop must not encircle the origin once" — it must not encircle with *any nonzero net winding*, which depends on the homotopy class, not just the geometric position.

---

# Rederivation Scaffold

**High-level strategy:**
Pick a base point $z_0 \in U$ and a base value $\lambda_0$ with $\exp(\lambda_0) = z_0$. Define $\lambda(z)$ by integrating $1/w$ along any path from $z_0$ to $z$ in $U$. Show path-independence (using simply-connectedness). Verify $\exp(\lambda(z)) = z$.

**Subgoal decomposition:**

1. **Define $\lambda$ via path integration.** $\lambda(z) := \lambda_0 + \int_\gamma dw/w$ for a path $\gamma$ from $z_0$ to $z$.
   - *Why needed:* the candidate branch.

2. **Path-independence of $\int_\gamma dw/w$.** For any closed $\gamma$ in $U$, $\int_\gamma dw/w = 0$.
   - *Hint:* $1/w$ is holomorphic on $U$, simply connected; apply Cauchy's theorem.
   - *Why needed:* makes $\lambda$ well-defined.

3. **Verify $\exp(\lambda(z)) = z$.**
   - *Hint:* differentiate $\exp(\lambda(z))/z$ along a path; show it is constant; evaluate at $z_0$.
   - *Why needed:* delivers the branch property.

4. **Holomorphicity and the derivative formula.** $\lambda'(z) = 1/z$.
   - *Hint:* differentiate the defining integral.

---

# Lemma Decomposition

> [!note]- Lemma 1: Path-independence of $\int dw/w$ on a simply connected domain
> **Statement:** Let $U \subseteq \mathbb{C}^\times$ be a simply connected domain. For any closed piecewise $C^1$ curve $\gamma$ in $U$, $\int_\gamma dw/w = 0$.
>
> **Hint:** Apply Cauchy's theorem on simply connected domains ([[Thm - Cauchy's Theorem for a Star-Shaped Domain]] for star-shaped; the general simply-connected case in CA III) to the holomorphic function $f(w) = 1/w$.
>
> **Why needed:** Makes the line integral path-independent, hence $\lambda$ well-defined.
>
> > [!note]- Full proof
> > $f(w) = 1/w$ is holomorphic on $\mathbb{C}^\times$, in particular on $U$. Cauchy's theorem (in its simply-connected form, see [[Thm - Cauchy's Theorem for a Star-Shaped Domain]] for the star-shaped case and the general statement in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]/[[Complex Analysis III — Winding, Laurent, Residues|CA III]]) gives $\int_\gamma f\,dw = 0$ for every closed $\gamma$ in $U$.

> [!note]- Lemma 2: Constructed function is the inverse of $\exp$
> **Statement:** Define $\lambda(z) := \lambda_0 + \int_{z_0}^z dw/w$ where the integral is along any path in $U$. Then $\exp(\lambda(z)) = z$.
>
> **Hint:** Show $z \exp(-\lambda(z))$ has zero derivative, evaluate at $z_0$.
>
> **Why needed:** Verifies the branch property.
>
> > [!note]- Full proof
> > Let $g(z) := z \exp(-\lambda(z))$ on $U$. By construction, $\lambda$ is holomorphic on $U$ with $\lambda'(z) = 1/z$ (since the integrand is $1/w$, and the derivative of the integral with respect to the upper endpoint along a path is the integrand evaluated there). Then
> > $$g'(z) = \exp(-\lambda(z)) + z \exp(-\lambda(z))(-\lambda'(z)) = \exp(-\lambda(z))(1 - z\lambda'(z)) = \exp(-\lambda(z))(1 - z \cdot 1/z) = 0.$$
> > By [[Thm - Constant on a Domain if Derivative is Zero]] on the connected $U$, $g$ is constant. Evaluating at $z = z_0$: $g(z_0) = z_0 \exp(-\lambda_0) = z_0 \cdot 1/z_0 = 1$ (since $\exp(\lambda_0) = z_0$). So $g(z) = 1$ for all $z$, i.e., $z = \exp(\lambda(z))$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $U \subseteq \mathbb{C}^\times$ be simply connected. Fix $z_0 \in U$ and choose $\lambda_0 \in \mathbb{C}$ with $\exp(\lambda_0) = z_0$ (exists by surjectivity of $\exp$ onto $\mathbb{C}^\times$).
>
> Define $\lambda : U \to \mathbb{C}$ by $\lambda(z) := \lambda_0 + \int_\gamma dw/w$, where $\gamma$ is any piecewise $C^1$ path in $U$ from $z_0$ to $z$. By Lemma 1, the integral depends only on the endpoints (not on the path).
>
> By the construction (line integral of a continuous function), $\lambda$ is holomorphic on $U$ with $\lambda'(z) = 1/z$.
>
> By Lemma 2, $\exp(\lambda(z)) = z$ for all $z \in U$. So $\lambda$ is a branch of the logarithm.
>
> **Converse.** Suppose a branch $\lambda$ exists on $U$. For any closed piecewise $C^1$ curve $\gamma$ in $U$ with parameter interval $[a, b]$:
> $$\int_\gamma dw/w = \int_a^b \frac{\gamma'(t)}{\gamma(t)}\,dt = \int_a^b (\lambda \circ \gamma)'(t)\,dt = \lambda(\gamma(b)) - \lambda(\gamma(a)) = 0$$
> since $\gamma$ is closed. So the winding number $I(\gamma; 0) = \frac{1}{2\pi i}\int_\gamma dw/w = 0$ for every closed $\gamma$ in $U$, confirming no obstructing loops. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemann surfaces and universal covers.** The space $\mathbb{C}^\times$ is *not* simply connected, but its universal cover *is*: it is the Riemann surface of the logarithm, equivalent to $\mathbb{C}$ via the map $z \mapsto e^z$. On the universal cover, the logarithm is single-valued by construction. This is the algebraic-topological framing of the theorem.

**Sheaves and covering spaces.** A branch of $\log$ is a section of the sheaf $\exp^* \mathcal{O}_{\mathbb{C}^\times}$ — local sections always exist, global sections exist iff the cover trivializes. The criterion of simple-connectedness is exactly the topological criterion for triviality of a covering.

**De Rham cohomology.** The 1-form $dz/z$ on $\mathbb{C}^\times$ is closed but not exact (globally). Its de Rham cohomology class is the generator of $H^1(\mathbb{C}^\times; \mathbb{R}) \cong \mathbb{R}$. The form becomes exact (has a primitive, namely $\log z$) on simply connected subdomains — exactly because $H^1$ vanishes for simply connected open subsets of $\mathbb{C}$.

---

# Bridges

- **[[Def - Branch of the Logarithm]]** — the object whose existence is being characterized.

- **[[Thm - Properties of the Complex Exponential]]** — provides surjectivity, periodicity, and the local invertibility of $\exp$ that make the construction possible.

- **[[Thm - Constant on a Domain if Derivative is Zero]]** — used in the proof to show the constructed function actually inverts $\exp$.

- **[[Thm - Cauchy's Theorem for a Star-Shaped Domain]]** (from CA II) — the source of path-independence; the full simply-connected version is in CA III.
