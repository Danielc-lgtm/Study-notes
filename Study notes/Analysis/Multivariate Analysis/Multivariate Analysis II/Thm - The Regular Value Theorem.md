---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Submanifold of Euclidean Space"
  - "Def - The Tangent Space to a Submanifold"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - The Implicit Function Theorem"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open and $f \in C^k(U, \mathbb{R}^{n-d})$, $k \geq 1$, $0 < d < n$. For $c \in \mathbb{R}^{n-d}$ the **level set** is $f^{-1}(c) = \{x \in U : f(x) = c\}$. The total derivative $Df_p : \mathbb{R}^n \to \mathbb{R}^{n-d}$ is **surjective** (has **maximal rank** $n-d$) when its Jacobian matrix has $n-d$ linearly independent rows. A point $p$ with $Df_p$ surjective is a **regular point**; a value $c$ is a **regular value** if *every* point of $f^{-1}(c)$ is a regular point (in particular if $f^{-1}(c)$ is empty). A value that is not regular is a **critical value**. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Statement

> **Regular value theorem.** Let $U \subseteq \mathbb{R}^n$ be open, $f \in C^k(U, \mathbb{R}^{n-d})$ with $k \geq 1$, and let $c \in \mathbb{R}^{n-d}$ be a **regular value** of $f$ — that is, the derivative $Df_p$ is surjective at every point $p$ with $f(p) = c$.
>
> Then the level set $M = f^{-1}(c)$, if nonempty, is a **$d$-dimensional $C^k$ submanifold** of $\mathbb{R}^n$. Its [[Def - The Tangent Space to a Submanifold|tangent space]] at any point $p \in M$ is
> $$T_p M = \ker Df_p = \{v \in \mathbb{R}^n : Df_p(v) = 0\},$$
> the kernel of the derivative; equivalently, the normal space is spanned by the gradients of the component functions $f_1, \dots, f_{n-d}$.

---

# Motivation

By far the most common way a curved space appears in mathematics is as a *solution set of equations*: the sphere is $\{|x|^2 = 1\}$, the orthogonal group is $\{A^TA = I\}$, an energy surface in mechanics is $\{E = \text{const}\}$, the mass shell of a particle is $\{\langle p,p\rangle = -m^2\}$. The question this theorem answers is the basic one: *when is such a solution set a genuine smooth space — a [[Def - Submanifold of Euclidean Space|submanifold]] — and not a set with corners, crossings, or cusps?*

We already know the danger. The level set $\{x^2 - y^2 = 0\}$ is two crossing lines; $\{x^2 + y^2 - z^2 = 0\}$ is a cone with a singular vertex. Level sets *can* be pathological. But we also noticed where the pathology sits: at the crossing point of the lines, and at the cone's vertex, the gradient of the defining function *vanishes*. The theorem makes this observation into a clean criterion: a level set is a submanifold *wherever the defining map's derivative has maximal rank*, and if that holds at every point of the level set — if the value $c$ is *regular* — the whole level set is a submanifold.

The value of the theorem is that it converts a *geometric* question — "is this set smooth, and what is its dimension and tangent space?" — into a *linear-algebraic* one — "does the Jacobian have maximal rank at each point?". You never construct charts by hand. You write the set as $f^{-1}(c)$, compute $Df$, and check its rank pointwise on the set. The dimension of the resulting manifold is read off immediately ($n$ minus the number of independent equations), and the tangent space comes out for free as $\ker Df_p$. This is the standard manufacturing device for submanifolds, and it is the theorem that makes §2.3 operational.

The theorem is also a perfect instance of the **local-to-global** principle: the [[Thm - The Implicit Function Theorem|implicit function theorem]] gives, at *each* point separately, a local graph picture; the regular value theorem observes that when the rank condition holds *everywhere* on the level set, these local pictures *assemble* into a global submanifold structure. The global object is built by checking a local condition at every point.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$c$ is a regular value: $Df$ is surjective at every point of $f^{-1}(c)$". The skill is recognizing regularity.

The first disguised source is **a scalar equation with nonvanishing gradient.** Property $B$: $f : \mathbb{R}^n \to \mathbb{R}$ and $\nabla f \neq 0$ at every point of $\{f = c\}$. The bridge: for a scalar map, "$Df_p$ surjective" means "$Df_p \neq 0$", i.e. $\nabla f(p) \neq 0$ — surjectivity onto $\mathbb{R}$ is just nonvanishing. So *any* level set of a scalar function with nonvanishing gradient is a hypersurface of dimension $n-1$. The non-obviousness: the abstract "maximal rank" condition becomes the very concrete "the gradient is not zero". *Example:* the sphere, $\{|x|^2 = 1\}$ with $\nabla(|x|^2) = 2x \neq 0$ on the sphere — see [[Ex - The sphere as a regular level set]].

The second disguised source is **a constraint set on which the constraint gradients are linearly independent.** Property $B$: $M = \{g_1 = \dots = g_{n-d} = 0\}$ and the gradients $\nabla g_j$ are linearly independent at each point of $M$. The bridge: stacking the $\nabla g_j$ as rows of the Jacobian, linear independence of the rows *is* surjectivity of $Df$. The non-obviousness: this is exactly the *regularity hypothesis of [[Thm - The Method of Lagrange Multipliers|Lagrange's theorem]]* — the regular value theorem and the clean form of Lagrange multipliers have the *same* source condition. *Example:* an intersection of surfaces meeting transversally.

The third disguised source is **a level set known to avoid the critical points of $f$.** Property $B$: the set of critical points of $f$ (where $Df$ drops rank) is known, and $f^{-1}(c)$ is disjoint from it. The bridge: if no point of the level set is critical, every point is regular, so $c$ is a regular value by definition. The non-obviousness: one need not check rank *everywhere*, only confirm the level set misses the (often lower-dimensional) bad set. By Sard's theorem, *almost every* value is regular, so a generic level set is automatically a submanifold. *Example:* energy surfaces $\{E = c\}$ for non-critical energies $c$.

**Targets (Output Amplification)**

The conclusion is "$f^{-1}(c)$ is a $d$-dimensional $C^k$ submanifold with $T_p M = \ker Df_p$".

Combine the conclusion with **a function to be optimized on the level set.** Property $D$: one wishes to extremise $h$ on $M = f^{-1}(c)$. The amplified result $E$: since $M$ is a submanifold with tangent space $\ker Df_p$, the constrained extrema satisfy $\nabla h \perp T_p M$, i.e. $\nabla h \in \operatorname{span}\{\nabla f_j\}$ — the [[Thm - The Method of Lagrange Multipliers|Lagrange multiplier]] condition. The regular value theorem is what *justifies* the geometric reading of Lagrange's theorem: it guarantees the constraint set genuinely has a tangent space.

Combine the conclusion with **compactness of the level set.** Property $D$: $f^{-1}(c)$ is also bounded (hence compact, being closed). The amplified result $E$: $M$ is a *compact* submanifold — it has finite volume, every continuous function attains extrema on it, and it can be covered by finitely many charts. Compact submanifolds are the well-behaved arena for integration and for Stokes' theorem.

Combine the conclusion with **a group structure on the level set.** Property $D$: $M = f^{-1}(c)$ is also closed under a group operation (matrix multiplication, say). The amplified result $E$: $M$ is a **Lie group** — a manifold and a group at once — and its tangent space at the identity is its Lie algebra. This is exactly how $O(n)$, $\operatorname{SL}_n$, $\operatorname{GL}_n$ are recognized as Lie groups; see [[Ex - The orthogonal group as a submanifold]].

---

# Why Is It True

The theorem is the [[Thm - The Implicit Function Theorem|implicit function theorem]] applied at every point of the level set and then assembled. Seeing this *is* the proof intuition.

Fix a point $p$ of the level set $M = f^{-1}(c)$. By hypothesis, the derivative $Df_p$ is surjective — its $(n-d)\times n$ Jacobian has $n-d$ linearly independent rows, hence $n-d$ linearly independent *columns*. Single those columns out: they correspond to $n-d$ of the coordinates, call them collectively the $y$-variables, and the remaining $d$ coordinates are the $x$-variables. By construction, the partial Jacobian $D_y f(p)$ — the square block of columns we singled out — is invertible. That is *exactly* the hypothesis of the implicit function theorem. So near $p$, the equation $f(x,y) = c$ can be solved for $y$ as a smooth function of $x$: the level set is, near $p$, the *graph* $\{(x, g(x))\}$ of a $C^k$ function.

But a graph is the simplest possible submanifold — it satisfies the [[Def - Submanifold of Euclidean Space|graphical representation]] of a submanifold directly. So $M$ is, near $p$, a $d$-dimensional $C^k$ submanifold. And $p$ was an arbitrary point of $M$: at *every* point, $M$ is locally a graph, hence locally a submanifold. Since being a submanifold is a *local* property — it only requires a good description near each point — and we have a good description near each point, $M$ is a submanifold, full stop. This is the local-to-global step: the rank condition, checked everywhere, makes the local graph pictures cohere into one global manifold.

Why is the dimension $d$? Because the graph is over the $d$ free $x$-variables: the level set has $d$ degrees of freedom, namely $n$ ambient coordinates minus the $n-d$ independent constraints. Each independent equation removes one dimension; surjectivity of $Df$ is precisely the statement that all $n-d$ equations are "independent" in the first-order sense.

Why is the tangent space $\ker Df_p$? Take any $C^1$ curve $\gamma$ inside $M$ through $p$. Since $\gamma(t) \in M = f^{-1}(c)$, we have $f(\gamma(t)) = c$ for all $t$ — a *constant*. Differentiate at $t = 0$ with the chain rule: $Df_p(\gamma'(0)) = 0$. So every velocity vector $\gamma'(0)$, every tangent vector, lies in $\ker Df_p$. That gives one inclusion, $T_p M \subseteq \ker Df_p$. For the reverse, $Df_p$ is surjective so its kernel has dimension exactly $n - (n-d) = d$; and $T_p M$ is also $d$-dimensional (the manifold has dimension $d$); a $d$-dimensional subspace contained in a $d$-dimensional subspace must equal it. So $T_p M = \ker Df_p$. The tangent space is the set of directions in which the constraints do not change to first order — which is geometrically exactly what "tangent to the level set" should mean.

So one should expect the theorem because *a level set is locally a graph wherever the constraints are first-order independent* — and "first-order independent" is precisely "$Df$ has maximal rank". Where the rank drops, two constraints can become tangent to each other, the level set can cross itself or pinch, and the graph picture fails — which is exactly the cone vertex and the crossing lines.

---

# What Makes This Hard

The non-obvious step is recognizing the theorem *is* the [[Thm - The Implicit Function Theorem|implicit function theorem]] in disguise — that "surjective $Df_p$" lets one select $n-d$ columns forming an invertible block, which is the implicit function theorem's hypothesis, making the level set locally a graph. The most common error is to forget that the rank condition must hold at *every* point of the level set, not just one: a value $c$ is regular only if $f^{-1}(c)$ contains *no* critical point, and a single critical point on the level set can make it singular there (the cone $\{x^2+y^2-z^2=0\}$ is a manifold everywhere except its vertex). A second frequent slip is to confuse a *critical point of $f$* with a *point of the level set* — the relevant condition is about the critical points that happen to *lie on* $f^{-1}(c)$.

---

# Rederivation Scaffold

**High-level strategy:**
At each point of the level set, surjectivity of $Df$ lets you pick an invertible square block of the Jacobian; the implicit function theorem then writes the level set locally as a graph. A graph is a submanifold, so the level set is locally a submanifold at every point, hence globally one. The tangent space is computed by differentiating the constancy of $f$ along curves.

**Subgoal decomposition:**

1. **Select an invertible block.** At $p \in M$, use surjectivity of $Df_p$ to find $n-d$ coordinates ("$y$") whose partial Jacobian $D_y f(p)$ is invertible.
   - *Hint:* A surjective $(n-d)\times n$ matrix has $n-d$ independent columns; take those as the $y$-block.
   - *Why needed:* It produces the hypothesis of the implicit function theorem.

2. **Apply the implicit function theorem.** Conclude $M$ is, near $p$, the graph $\{(x, g(x))\}$ of a $C^k$ function.
   - *Hint:* Solve $f(x,y) = c$ for $y$; this is the [[Thm - The Implicit Function Theorem|implicit function theorem]].
   - *Why needed:* It gives the local graphical description of $M$.

3. **Recognize a graph as a submanifold.** Note that a graph of a $C^k$ function satisfies the graphical representation of a submanifold.
   - *Hint:* The graphical representation is one of the four equivalent descriptions of a [[Def - Submanifold of Euclidean Space|submanifold]].
   - *Why needed:* It upgrades "locally a graph" to "locally a submanifold".

4. **Assemble globally.** Since $p$ was arbitrary, $M$ is locally a submanifold at every point, hence a submanifold.
   - *Hint:* Being a submanifold is a purely local property.
   - *Why needed:* This is the local-to-global step yielding the global conclusion.

5. **Compute the tangent space.** Differentiate $f(\gamma(t)) = c$ for a curve $\gamma$ in $M$ to get $T_p M \subseteq \ker Df_p$; match dimensions for equality.
   - *Hint:* Chain rule gives $Df_p(\gamma'(0)) = 0$; both spaces have dimension $d$.
   - *Why needed:* It establishes the tangent-space formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: A surjective linear map admits an invertible square block
> **Statement:** If $L : \mathbb{R}^n \to \mathbb{R}^{n-d}$ is surjective, there is a choice of $n-d$ of the standard coordinates such that the corresponding $(n-d)\times(n-d)$ submatrix of $L$'s matrix is invertible.
>
> **Hint:** Surjectivity means the matrix has rank $n-d$, so it has $n-d$ linearly independent columns.
>
> **Why needed:** It converts the abstract surjectivity hypothesis into the concrete invertible-block hypothesis the implicit function theorem requires.
>
> > [!note]- Full proof
> > $L$ surjective means its matrix has rank $n-d$ (the row rank, equal to the column rank, is maximal). A matrix of rank $n-d$ has $n-d$ linearly independent columns; let $S \subseteq \{1,\dots,n\}$ index such a set of columns, $|S| = n-d$. The $(n-d)\times(n-d)$ submatrix formed by these columns has $n-d$ independent columns, hence is invertible. Designating the coordinates indexed by $S$ as the "$y$-variables" and the rest as the "$x$-variables", this submatrix is exactly the partial Jacobian $D_y(\text{the map})$, and it is invertible.

> [!note]- Lemma 2: A graph is a submanifold with computable tangent space
> **Statement:** For $g \in C^k(V, \mathbb{R}^{n-d})$, $V \subseteq \mathbb{R}^d$ open, the graph $\Gamma = \{(x, g(x)) : x \in V\}$ is a $d$-dimensional $C^k$ submanifold, with $T_{(x,g(x))}\Gamma = \{(v, Dg(x)v) : v \in \mathbb{R}^d\} = \operatorname{im}\begin{pmatrix} I \\ Dg(x)\end{pmatrix}$.
>
> **Hint:** The graph is parametrized by $G(x) = (x, g(x))$, whose derivative is injective.
>
> **Why needed:** It is the step that turns "locally a graph" into "locally a submanifold", and gives the tangent space in the graph case.
>
> > [!note]- Full proof
> > The map $G : V \to \mathbb{R}^n$, $G(x) = (x, g(x))$, is $C^k$ and a homeomorphism onto $\Gamma$ (its inverse is the projection to the $x$-coordinates). Its derivative $DG_x = \begin{pmatrix} I_d \\ Dg(x)\end{pmatrix}$ has rank $d$ (the top block is the identity), so $DG_x$ is injective — $G$ is an immersion. This is exactly the parametric representation of a submanifold, so $\Gamma$ is a $d$-dimensional $C^k$ submanifold. By the parametric form of the [[Def - The Tangent Space to a Submanifold|tangent space]], $T_{(x,g(x))}\Gamma = \operatorname{im} DG_x = \{(v, Dg(x)v) : v \in \mathbb{R}^d\}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $c$ be a regular value of $f \in C^k(U, \mathbb{R}^{n-d})$ and $M = f^{-1}(c)$ nonempty.
>
> **$M$ is a submanifold.** Fix $p \in M$. By hypothesis $Df_p$ is surjective. By Lemma 1, after permuting coordinates write $\mathbb{R}^n = \mathbb{R}^d_x \times \mathbb{R}^{n-d}_y$ so that the partial Jacobian $D_y f(p)$ is invertible. The map $\tilde f(x,y) = f(x,y) - c$ is $C^k$, vanishes at $p = (x_p, y_p)$, and has $D_y\tilde f(p) = D_y f(p)$ invertible. By the [[Thm - The Implicit Function Theorem|implicit function theorem]], there is a cylinder $W = B_r(x_p)\times B_s(y_p)$ and a $C^k$ map $g : B_r(x_p) \to \mathbb{R}^{n-d}$ with
> $$\{x \in W : f(x) = c\} = \{\tilde f = 0\}\cap W = \{(x, g(x)) : x \in B_r(x_p)\}.$$
> Thus $M \cap W$ is (a permutation of) the graph of $g$. By Lemma 2, the graph of $g$ is a $d$-dimensional $C^k$ submanifold, so $M$ satisfies the [[Def - Submanifold of Euclidean Space|graphical representation]] of a submanifold near $p$. Since $p \in M$ was arbitrary and the graphical condition holds near every point, $M$ is a $d$-dimensional $C^k$ submanifold of $\mathbb{R}^n$.
>
> **The tangent space is $\ker Df_p$.** Let $p \in M$ and $v \in T_p M$. By the definition of the [[Def - The Tangent Space to a Submanifold|tangent space]], $v = \gamma'(0)$ for some $C^1$ curve $\gamma$ in $M$ with $\gamma(0) = p$. Since $\gamma(t) \in M = f^{-1}(c)$, the composite $f\circ\gamma$ is constantly $c$. Differentiating at $t = 0$ by the chain rule,
> $$0 = \frac{d}{dt}\Big|_{t=0} f(\gamma(t)) = Df_p(\gamma'(0)) = Df_p(v).$$
> Hence $v \in \ker Df_p$, proving $T_p M \subseteq \ker Df_p$.
> For the reverse inclusion, count dimensions. $Df_p$ is surjective onto $\mathbb{R}^{n-d}$, so by rank–nullity $\dim\ker Df_p = n - (n-d) = d$. And $M$ is a $d$-dimensional submanifold, so $\dim T_p M = d$. A $d$-dimensional subspace ($T_p M$) contained in a $d$-dimensional subspace ($\ker Df_p$) must equal it. Therefore $T_p M = \ker Df_p$. The normal space $(T_p M)^\perp = (\ker Df_p)^\perp$ is the row space of $Df_p$, spanned by $\nabla f_1(p), \dots, \nabla f_{n-d}(p)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Matrix groups as Lie groups.** The orthogonal group $\{A^TA = I\}$, the special linear group $\{\det A = 1\}$, and others are level sets of smooth maps on the space of matrices. Checking that the identity matrix is a regular value of the relevant map proves these are submanifolds — and being also groups, they are *Lie groups*. The application is nonobvious because the "Euclidean space" is the space of matrices and the equations are polynomial; see [[Ex - The orthogonal group as a submanifold]].

**Energy surfaces in classical mechanics.** A conservative mechanical system with energy $E(q,p)$ has every trajectory confined to a level set $\{E = c\}$. For non-critical $c$ — energies that are not equilibria — the regular value theorem makes the energy surface a submanifold of phase space, on which the dynamics is a flow. The application battle-tests the theorem: the *qualitative* theory of phase portraits rests on energy surfaces being genuine manifolds, and the critical energies are exactly where the topology of the surface changes.

**The mass shell in special relativity.** In **special relativity** the four-momenta of a particle of mass $m$ satisfy $\langle p, p\rangle = -m^2$ in the Minkowski metric — a level set of the quadratic form $p \mapsto \langle p,p\rangle$. Its derivative is nonzero off the origin, so $-m^2$ is a regular value and the *mass shell* is a submanifold of momentum space, the relativistic analogue of the sphere. The application is out-of-distribution because the quadratic form is *indefinite* (Minkowski, not Euclidean) — yet the regular value theorem applies verbatim, since it needs only the rank of the derivative.

---

# Bridges

- **[[Thm - The Implicit Function Theorem]]** — the engine. The regular value theorem is the implicit function theorem applied at every point of a level set and assembled; the rank condition is what supplies the implicit function theorem's hypothesis at each point.

- **[[Def - Submanifold of Euclidean Space]]** — the regular value theorem is the bridge from the *implicit* representation of a submanifold to the others; it certifies that a maximal-rank level set satisfies the definition.

- **[[Def - The Tangent Space to a Submanifold]]** — the theorem delivers the tangent space as a kernel, $\ker Df_p$, the most computable of all tangent-space descriptions.

- **[[Thm - The Method of Lagrange Multipliers]]** — the regularity hypothesis here ("$Df$ surjective", "constraint gradients independent") is *identical* to the regularity hypothesis of Lagrange's theorem. The regular value theorem is what guarantees the constraint set genuinely has a tangent space, justifying the geometric reading "$\nabla f \perp T_p M$".

- **Sard's theorem** — the complementary fact that the set of critical values has measure zero, so *almost every* value is regular. Together with the regular value theorem, this says a *generic* level set is automatically a submanifold.

---

# Unlocked by This

> [!tip] Lie Groups and Lie Algebras *(from Lie Theory)*
> A level set that is also closed under a group operation is a **Lie group**. The regular value theorem proves the manifold half; the tangent space at the identity, with the commutator bracket, is the **Lie algebra**. This is how $O(n)$, $\operatorname{SU}(n)$, the Lorentz group are recognized as smooth groups.

> [!tip] Transversality and Intersection Theory *(from Differential Topology)*
> Two submanifolds meet **transversally** when their tangent spaces together span the ambient space; a transversal intersection is again a submanifold — a relative version of the regular value theorem. **Transversality** is the foundation of intersection theory and degree theory.

> [!tip] Cobordism and the Topology of Manifolds *(from Algebraic Topology)*
> Regular level sets of a map and how they change as the value crosses a critical value (Morse theory) encode the topology of the domain. Cobordism — when one manifold is the boundary of another — is studied through regular values of maps to the interval.
