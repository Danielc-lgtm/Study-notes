---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Distribution on a Manifold"
  - "Def - Involutive Distribution"
  - "Thm - The Frobenius Theorem"
tags: [geometry, differential-geometry, frobenius, pde]
---

# Problem Statement

Consider the overdetermined system of first-order partial differential equations for an unknown function $u : \mathbb{R}^2 \to \mathbb{R}$:

$$\frac{\partial u}{\partial x} = \alpha(x, y, u), \qquad \frac{\partial u}{\partial y} = \beta(x, y, u),$$

where $\alpha, \beta$ are smooth functions on an open set $W \subseteq \mathbb{R}^3$.

**(a)** Show that the system has a local solution with prescribed initial value $u(x_0, y_0) = z_0$ for any $(x_0, y_0, z_0) \in W$ if and only if the compatibility condition

$$\frac{\partial \alpha}{\partial y} + \beta\,\frac{\partial \alpha}{\partial z} = \frac{\partial \beta}{\partial x} + \alpha\,\frac{\partial \beta}{\partial z}$$

holds identically on $W$. (Here $z$ denotes the value of $u$ at the point $(x, y)$.)

**(b)** Recognize this compatibility condition as the involutivity of the distribution $D = \mathrm{span}(X, Y)$ on $W \subseteq \mathbb{R}^3$, where

$$X = \partial_x + \alpha(x, y, z)\partial_z, \qquad Y = \partial_y + \beta(x, y, z)\partial_z.$$

**(c)** Conclude: the existence of local solutions is equivalent to the involutivity of $D$, hence to the application of Frobenius's theorem.

**Recall:**

![[Thm - The Frobenius Theorem#Statement]]

![[Def - Involutive Distribution#The Definition]]

---

# Convergent Strategy

**Problem class:** Apply the Frobenius theorem to a PDE compatibility question. Pattern: reformulate the PDE as a question about the integrability of an associated distribution; identify the compatibility condition as involutivity; invoke Frobenius for existence.

**Assumption pattern:** A first-order PDE system for $u(x, y)$ that specifies *both* partial derivatives — overdetermined. The compatibility condition is the cross-partial agreement $\partial_y(\partial_x u) = \partial_x(\partial_y u)$ — Clairaut's theorem applied to the unknown $u$, expanded using the prescribed derivatives via the chain rule.

**Theorem routing:** Reformulation: solutions of the PDE are integral surfaces (graphs) of the distribution $D = \mathrm{span}(X, Y)$ in $(x, y, z)$-space. [[Thm - The Frobenius Theorem]] says integral surfaces exist iff $D$ is involutive. Compute $[X, Y]$ explicitly; the condition $[X, Y] \in D$ reduces to the compatibility condition.

**Key decision point:** The crucial reformulation is the geometric one: solutions are *graphs*, hence $2$-dimensional submanifolds of $(x, y, z)$-space, with tangent spaces forced to be spanned by $X$ and $Y$ (because $\dot u = \alpha, \beta$ along the $x$- and $y$-directions). Once this reformulation is made, the PDE existence question becomes a Frobenius integrability question.

---

# Legal Operations Used

1. **Test involutivity by Lie brackets on a local frame** (operation 4 from the topic page). Compute $[X, Y]$ for the specified $X, Y$ and check whether the result is a linear combination of $X$ and $Y$.

2. **Invoke Frobenius to manufacture integral manifolds** (operation 6 from the topic page). If $D$ is involutive, [[Thm - The Frobenius Theorem|Frobenius]] guarantees integral surfaces; these surfaces, being transverse to $\partial_z$ at the initial point (since $X, Y$ have non-trivial $\partial_x, \partial_y$ components), are graphs of functions of $(x, y)$.

3. **Build a homomorphism (or here, a smooth map) to expose structure** (analogous to operation 3). The map $(x, y) \mapsto (x, y, u(x, y))$ from solution domain to $\mathbb{R}^3$ is the natural parameterization of the integral surface as a graph.

---

# Hints

> [!note]- Hint 1
> The natural reformulation: a solution $u(x, y)$ defines a graph $\Sigma = \{(x, y, u(x, y))\} \subseteq W \subseteq \mathbb{R}^3$. What is the tangent space $T_p\Sigma$ at $p = (x, y, u(x, y))$?

> [!note]- Hint 2
> Compute the partial derivatives of the parameterization $F(x, y) = (x, y, u(x, y))$. The image $dF(\partial_x)$ is $\partial_x + (\partial_x u)\partial_z = \partial_x + \alpha\partial_z = X$ at points of the graph. Similarly $dF(\partial_y) = Y$. So $T_p\Sigma = \mathrm{span}(X_p, Y_p) = D_p$.

> [!note]- Hint 3
> The PDE has a solution iff there is a graph of a function whose tangent space is $D$ everywhere — i.e., iff $D$ has an integral surface that is a graph over $(x, y)$.

> [!note]- Hint 4
> By [[Thm - The Frobenius Theorem]], such integral surfaces exist iff $D$ is involutive — iff $[X, Y] \in D$.

> [!note]- Hint 5
> Compute $[X, Y] = [\partial_x + \alpha\partial_z, \partial_y + \beta\partial_z]$. Expand and collect terms.

---

# Solution

The plan: identify graphs of solutions as integral surfaces of $D$, compute the bracket $[X, Y]$, show that the compatibility condition is exactly $[X, Y] \in D$, and apply Frobenius for existence.

**Step 1: Graphs of solutions are integral surfaces of $D$.**

> [!note]- Derivation
> Suppose $u : U \subseteq \mathbb{R}^2 \to \mathbb{R}$ is a smooth solution of the PDE on an open $U$. Define $F : U \to \mathbb{R}^3$ by $F(x, y) = (x, y, u(x, y))$. The image $\Sigma = F(U)$ is the *graph* of $u$, a smooth embedded $2$-submanifold of $\mathbb{R}^3$ (since $F$ is an injective immersion with everywhere-injective differential).
>
> The tangent space at $p = (x, y, u(x, y)) \in \Sigma$ is spanned by
> $$dF_{(x,y)}(\partial_x) = \partial_x + (\partial_x u)\partial_z|_p, \qquad dF_{(x,y)}(\partial_y) = \partial_y + (\partial_y u)\partial_z|_p.$$
> Using the PDE: $\partial_x u = \alpha$ and $\partial_y u = \beta$. So
> $$dF_{(x,y)}(\partial_x) = \partial_x + \alpha(x, y, u(x, y))\partial_z = X_p, \qquad dF_{(x,y)}(\partial_y) = \partial_y + \beta(x, y, u(x, y))\partial_z = Y_p.$$
> Hence $T_p\Sigma = \mathrm{span}(X_p, Y_p) = D_p$ at every $p \in \Sigma$.
>
> *Conversely:* every integral surface of $D$ that is *transverse to $\partial_z$* (i.e. is a graph over the $(x, y)$-plane) corresponds to a solution $u(x, y)$. Transversality is guaranteed because $D$ at every point contains $\partial_x + \alpha\partial_z$ and $\partial_y + \beta\partial_z$, both transverse to the vertical $\partial_z$; the $2$-plane $D_p$ is therefore transverse to $\partial_z$ everywhere, so any integral surface through $(x_0, y_0, z_0)$ is locally a graph.

**Step 2: Compute $[X, Y]$.**

> [!note]- Derivation
> $[X, Y] = [\partial_x + \alpha\partial_z, \partial_y + \beta\partial_z]$. Use bilinearity and the bracket-of-a-coordinate-field-and-a-scaled-field formula.
>
> Distribute into four terms:
> $$[X, Y] = [\partial_x, \partial_y] + [\partial_x, \beta\partial_z] + [\alpha\partial_z, \partial_y] + [\alpha\partial_z, \beta\partial_z].$$
>
> *Term 1:* $[\partial_x, \partial_y] = 0$.
>
> *Term 2:* $[\partial_x, \beta\partial_z] = (\partial_x \beta)\partial_z + \beta[\partial_x, \partial_z] = (\partial_x \beta)\partial_z + 0 = (\partial_x \beta)\partial_z$.
>
> *Term 3:* $[\alpha\partial_z, \partial_y] = -[\partial_y, \alpha\partial_z] = -((\partial_y \alpha)\partial_z + \alpha[\partial_y, \partial_z]) = -(\partial_y\alpha)\partial_z$.
>
> *Term 4:* $[\alpha\partial_z, \beta\partial_z]$. Use the formula $[fW, gV] = fg[W, V] + f(Wg)V - g(Vf)W$ for $W = V = \partial_z$, $f = \alpha$, $g = \beta$:
> $$[\alpha\partial_z, \beta\partial_z] = \alpha\beta[\partial_z, \partial_z] + \alpha(\partial_z\beta)\partial_z - \beta(\partial_z\alpha)\partial_z = 0 + \alpha(\partial_z\beta)\partial_z - \beta(\partial_z\alpha)\partial_z.$$
>
> Summing all four terms:
> $$[X, Y] = (\partial_x\beta - \partial_y\alpha + \alpha\partial_z\beta - \beta\partial_z\alpha)\partial_z.$$
>
> So $[X, Y] = \left(\frac{\partial\beta}{\partial x} - \frac{\partial\alpha}{\partial y} + \alpha\frac{\partial\beta}{\partial z} - \beta\frac{\partial\alpha}{\partial z}\right)\partial_z$.

**Step 3: Involutivity condition $\iff$ compatibility condition.**

> [!note]- Derivation
> $D = \mathrm{span}(X, Y) = \mathrm{span}(\partial_x + \alpha\partial_z, \partial_y + \beta\partial_z)$. A vector $W = a\partial_x + b\partial_y + c\partial_z$ is in $D$ iff there exist $\lambda, \mu \in \mathbb{R}$ (or functions, in the smooth context) with $W = \lambda X + \mu Y$, i.e. $a = \lambda$, $b = \mu$, $c = \lambda\alpha + \mu\beta$.
>
> For $[X, Y]$: the result is $0\partial_x + 0\partial_y + (\cdots)\partial_z$, with $a = b = 0$. So $\lambda = \mu = 0$, hence $c = 0$. That is, $[X, Y] \in D$ iff the coefficient of $\partial_z$ in $[X, Y]$ vanishes:
> $$\frac{\partial\beta}{\partial x} - \frac{\partial\alpha}{\partial y} + \alpha\frac{\partial\beta}{\partial z} - \beta\frac{\partial\alpha}{\partial z} = 0,$$
> equivalently
> $$\frac{\partial\alpha}{\partial y} + \beta\frac{\partial\alpha}{\partial z} = \frac{\partial\beta}{\partial x} + \alpha\frac{\partial\beta}{\partial z}.$$
> This is the compatibility condition stated in the problem.

**Step 4: Apply Frobenius for existence.**

> [!note]- Derivation
> If the compatibility condition holds (i.e. $[X, Y] = 0$, since the only way for the $\partial_z$-coefficient to vanish is for the entire bracket to vanish): $D$ is involutive. By [[Thm - The Frobenius Theorem]], every point $(x_0, y_0, z_0) \in W$ has a neighborhood with a flat chart for $D$. The integral surface through $(x_0, y_0, z_0)$ is $2$-dimensional and transverse to $\partial_z$ (since $D$ is transverse to $\partial_z$, as both $X$ and $Y$ have non-trivial horizontal components). Hence by the implicit function theorem, the integral surface is locally a graph $\{(x, y, u(x, y)) : (x, y) \in U\}$ for some neighborhood $U$ of $(x_0, y_0)$ and a smooth $u : U \to \mathbb{R}$ with $u(x_0, y_0) = z_0$.
>
> Verify this $u$ solves the PDE: $T_p\Sigma = D_p$, so the tangent vector $dF(\partial_x) = \partial_x + (\partial_x u)\partial_z$ must lie in $D_p = \mathrm{span}(X_p, Y_p)$. Matching components: $(\partial_x u)\partial_z$ must be the $\partial_z$-component obtained from a combination $\lambda X_p + \mu Y_p$ with $\lambda = 1$, $\mu = 0$ (to match $\partial_x$ in the horizontal part). So $\partial_x u = \alpha$. Similarly $\partial_y u = \beta$. Hence $u$ solves the PDE.
>
> *Conversely:* if the PDE has a solution $u$ with $u(x_0, y_0) = z_0$, then the graph $\Sigma = \{(x, y, u(x, y))\}$ is an integral surface of $D$. By Lemma 1 in [[Thm - The Frobenius Theorem]] (the easy direction: integrable $\Longrightarrow$ involutive), $D$ is involutive — which gives the compatibility condition.

> [!note]- Complete formal solution
> *Reformulation:* solutions of the PDE correspond to integral surfaces of $D = \mathrm{span}(X, Y)$ on $W$ that are graphs over the $(x, y)$-plane. The graph of any candidate $u$ has tangent space $\mathrm{span}(X, Y)$ at every point iff $\partial_x u = \alpha, \partial_y u = \beta$. So existence of solutions = existence of (graph-type) integral surfaces of $D$.
>
> By [[Thm - The Frobenius Theorem]], $D$ has integral surfaces through every point of $W$ iff $D$ is involutive iff $[X, Y] \in \Gamma(D)$.
>
> *Compute $[X, Y]$:* $[X, Y] = (\partial_x\beta - \partial_y\alpha + \alpha\partial_z\beta - \beta\partial_z\alpha)\partial_z$.
>
> *Involutivity condition:* $[X, Y]$ has only a $\partial_z$-component, and $D$ has no vectors of the form $c\partial_z$ except zero. So $[X, Y] \in D$ iff the $\partial_z$-coefficient vanishes, i.e.
> $$\partial_y\alpha + \beta\partial_z\alpha = \partial_x\beta + \alpha\partial_z\beta.$$
>
> This is the compatibility condition. When it holds, Frobenius produces an integral surface through each $(x_0, y_0, z_0) \in W$, and transversality with $\partial_z$ makes it a graph, giving a solution $u(x, y)$ with $u(x_0, y_0) = z_0$. When it fails, no such solution exists. $\blacksquare$

---

# Key Takeaways

**Frobenius's theorem is the master existence theorem for overdetermined first-order PDE systems.** Every system of the form $\partial u/\partial x^i = \alpha^i(x, u)$ defines an associated distribution on $(x, u)$-space, with spanning fields $X_i = \partial_{x^i} + \alpha^i\partial_u$. The classical PDE compatibility conditions — that mixed partials commute — are exactly the involutivity of this distribution, $[X_i, X_j] = 0$. Frobenius then says: solvability iff compatibility iff involutivity. This pattern recurs for every overdetermined first-order system in arbitrary [[Def - Dimension|dimension]]; the higher-rank generalization is in Lee's Proposition 19.29. The trigger to recognize: any time you see "PDE for $u$ with all partial derivatives prescribed," reformulate as a distribution-on-jet-space problem and apply Frobenius.

**The compatibility condition is the symmetry of mixed second partials.** Computing $\partial_y(\partial_x u) = \partial_y \alpha(x, y, u(x, y))$ using the chain rule gives $\partial_y\alpha + \beta\partial_z\alpha$ (with $z = u$). Similarly $\partial_x(\partial_y u) = \partial_x\beta + \alpha\partial_z\beta$. Equality of mixed partials (Clairaut's theorem) gives the compatibility condition exactly. So the involutivity condition $[X, Y] \in D$ is, geometrically, the Clairaut equality applied to the unknown function — the geometric meaning of "the second derivative is well-defined" is "the distribution is involutive." The trigger: every cross-partial check in PDE compatibility is a Frobenius involutivity check in disguise.

**The distribution-on-jet-space reformulation is the foundational paradigm of the geometric theory of PDE.** This exercise illustrates the small case (one unknown $u$, two independent variables $x, y$). The full theory — for systems of unknowns $u^a$, arbitrary-order derivatives, nonlinear equations — uses *jet spaces* and *contact systems*, with the same Frobenius-style involutivity test (now called *Cartan's test* in the Cartan–Kähler theory). Every "compatibility condition" for an overdetermined PDE — from the Einstein vacuum equations to the integrability of complex structures (Newlander–Nirenberg) — is an involutivity condition in this paradigm. The trigger: the geometric PDE theorist views a PDE as a distribution on jet space, and Frobenius's theorem as the existence/non-existence dichotomy.

**Existence vs. construction: Frobenius is purely existential, but the proof is constructive.** The Frobenius theorem produces an integral surface; it does *not* explicitly compute it. But the proof — via the canonical-form theorem for commuting vector fields, via composing flows of commuting fields — does give an *algorithm*. To find the solution $u$ given $\alpha, \beta$ satisfying the compatibility condition: integrate $X = \partial_x + \alpha\partial_z$ from the initial point in the $x$-direction (solve an ODE) to extend the solution along the $x$-axis; then for each fixed $x$, integrate $Y = \partial_y + \beta\partial_z$ in the $y$-direction. The compatibility condition ensures consistency. This is the **method of characteristics** in disguise, applied to an overdetermined system. *Companion exercise:* [[Ex - An Involutive Distribution from Three Vector Fields]] illustrates the analogous brackets computation in higher [[Def - Dimension|dimension]].
