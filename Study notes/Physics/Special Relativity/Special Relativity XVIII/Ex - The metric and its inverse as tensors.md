---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Tensors on Minkowski Space"
  - "Def - Metric Duality and Index Manipulation"
  - "Def - Tensor Operations"
tags: [physics, special-relativity]
---

# Problem Statement

Work in mostly-minus signature, $c = 1$.

1. Show that the metric components $g_{\alpha\beta} = g(e_\alpha, e_\beta)$ are the components of a type-$(0,2)$ [[Def - Tensors on Minkowski Space|tensor]], and verify they transform by the bilinear-form law $g' = {}^{t}P\,g\,P$ under a change of basis.
2. Define the inverse metric $g^{\alpha\beta}$ (inverse matrix of $g_{\alpha\beta}$) and show it is the components of a type-$(2,0)$ tensor $g^{-1} = g^{\alpha\beta}\,e_\alpha\otimes e_\beta$, with $g_{\alpha\rho}g^{\rho\beta} = \delta_\alpha{}^\beta$.
3. In an orthonormal frame, verify $\eta^{\mu\nu} = \eta_{\mu\nu}$ numerically (the metric is its own inverse matrix), and explain why this is a frame-dependent coincidence, not a tensor equation.
4. Show that raising both indices of the metric gives the inverse metric, $g^{\alpha\beta} = g^{\alpha\mu}g^{\beta\nu}g_{\mu\nu}$, and that raising one index of the metric gives the Kronecker delta, $g^\alpha{}_\beta = \delta^\alpha{}_\beta$.

**Recall:**

![[Def - Tensors on Minkowski Space#The Definition]]

The [[Def - Minkowski Space and the Metric|metric]] $g$ is a symmetric type-$(0,2)$ tensor with components $g_{\alpha\beta}$. Its **inverse** $g^{\alpha\beta}$ is the matrix inverse, used to [[Def - Metric Duality and Index Manipulation|raise indices]]. Under a change of basis $e'_\alpha = P^\beta{}_\alpha e_\beta$, a bilinear form's matrix transforms by $g' = {}^{t}P\,g\,P$ (Gourgoulhon 14.24).

---

# Convergent Strategy

**Problem class.** A *structural* problem establishing that the metric and its inverse are genuine tensors, exercising the [[Def - Tensors on Minkowski Space|change-of-basis law]] and [[Def - Metric Duality and Index Manipulation|metric duality]]. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: identify the type, then the transformation law is forced.

**Assumption pattern.** The metric is a bilinear form, so type $(0,2)$ — two lower indices. Its inverse, being defined by the inverse matrix relation, must transform oppositely (type $(2,0)$, two upper indices). The orthonormal special case $\eta = \mathrm{diag}(1,-1,-1,-1)$, self-inverse as a matrix, is the source of part 3's "coincidence."

**Theorem routing.** Part 1: apply the type-$(0,2)$ change-of-basis law and recognise it as the bilinear matrix law $g' = {}^tP g P$. Part 2: define $g^{\alpha\beta}$ by the inverse relation and show it transforms as type $(2,0)$ (by $P^{-1}$ on each index). Part 3: compute $\eta^{-1}$ directly. Part 4: raise indices of $g_{\mu\nu}$ using $g^{\alpha\mu}$ and simplify with the inverse relation.

**Key decision point.** The crux is part 3's distinction between a *numerical* coincidence and a *tensor* equation. The components $\eta^{\mu\nu}$ and $\eta_{\mu\nu}$ are equal as arrays *only in an orthonormal frame* — they are components of *different* tensors (type $(2,0)$ versus type $(0,2)$), which transform differently, so the equality cannot be a tensor identity. In a curvilinear frame $g^{\alpha\beta} \neq g_{\alpha\beta}$. Recognising that "the metric equals its inverse" is a basis-dependent statement, not a covariant one, is the lesson.

---

# Legal Operations Used

1. **Operation 1 from the topic page (raise/lower with the metric).** Part 4 raises the metric's indices to recover the inverse metric and the Kronecker delta.

2. **Operation 3 from the topic page (tensor product).** The inverse metric is written $g^{-1} = g^{\alpha\beta}e_\alpha\otimes e_\beta$, a tensor-product expansion of a type-$(2,0)$ tensor.

---

# Hints

> [!note]- Hint 1
> The metric is the bilinear form $g(\vec u, \vec v) = g_{\alpha\beta}u^\alpha v^\beta$, a type-(0,2) tensor. Its components are $g_{\alpha\beta} = g(e_\alpha, e_\beta)$, and under $e'_\alpha = P^\beta{}_\alpha e_\beta$, multilinearity gives $g'_{\alpha\beta} = g(e'_\alpha, e'_\beta) = P^\mu{}_\alpha P^\nu{}_\beta g_{\mu\nu}$, which in matrix form is $g' = {}^tP g P$.

> [!note]- Hint 2
> The inverse metric is *defined* by $g_{\alpha\rho}g^{\rho\beta} = \delta_\alpha{}^\beta$. For this defining relation to be a tensor equation (the right side is the type-$(1,1)$ identity), $g^{\rho\beta}$ must transform with *two upper* indices — type $(2,0)$ — so that the contraction with the type-$(0,2)$ metric gives the invariant $\delta$.

> [!note]- Hint 3
> $\eta = \mathrm{diag}(1,-1,-1,-1)$; its matrix inverse is $\mathrm{diag}(1, -1, -1, -1)$ — the same matrix, since each diagonal entry is its own reciprocal ($1/1 = 1$, $1/(-1) = -1$). But $\eta^{\mu\nu}$ (type $(2,0)$) and $\eta_{\mu\nu}$ (type $(0,2)$) transform by $P^{-1}$ and $P$ respectively, so their equality is basis-specific.

---

# Solution

The exercise certifies that both $g_{\alpha\beta}$ and $g^{\alpha\beta}$ are honest tensors and clarifies the orthonormal-frame coincidence $\eta^{\mu\nu} = \eta_{\mu\nu}$. The plan: confirm the metric is type $(0,2)$ via its transformation law (Step 1), the inverse metric is type $(2,0)$ via its defining relation (Step 2), explain the self-inverse coincidence as frame-dependent (Step 3), and verify the index-raising consistency relations (Step 4).

**Step 1: $g_{\alpha\beta}$ is a type-$(0,2)$ tensor, transforming by $g' = {}^tP\,g\,P$.**

> [!note]- Derivation
> The metric is the bilinear map $g : E\times E \to \mathbb{R}$, a [[Def - Tensors on Minkowski Space|type-(0,2) tensor]] by definition (two vector slots). Its components are $g_{\alpha\beta} = g(e_\alpha, e_\beta)$. Under $e'_\alpha = P^\mu{}_\alpha e_\mu$, bilinearity gives
> $$g'_{\alpha\beta} = g(e'_\alpha, e'_\beta) = g(P^\mu{}_\alpha e_\mu, P^\nu{}_\beta e_\nu) = P^\mu{}_\alpha P^\nu{}_\beta\, g(e_\mu, e_\nu) = P^\mu{}_\alpha P^\nu{}_\beta\, g_{\mu\nu}.$$
> This is the type-$(0,2)$ law (one $P$ per lower index), and in matrix form $g'_{\alpha\beta} = (P^{\mathsf T})_\alpha{}^\mu g_{\mu\nu}P^\nu{}_\beta$, i.e. $g' = {}^{t}P\,g\,P$ — the standard change-of-basis law for the matrix of a bilinear form.

**Step 2: $g^{\alpha\beta}$ is a type-$(2,0)$ tensor with $g_{\alpha\rho}g^{\rho\beta} = \delta_\alpha{}^\beta$.**

> [!note]- Derivation
> Define $g^{\alpha\beta}$ as the entries of the inverse matrix of $(g_{\alpha\beta})$, so $g_{\alpha\rho}g^{\rho\beta} = \delta_\alpha{}^\beta$. We must show this transforms as a type-$(2,0)$ tensor. From Step 1, $g'_{\alpha\beta} = P^\mu{}_\alpha P^\nu{}_\beta g_{\mu\nu}$, i.e. $g' = {}^tP g P$; inverting, $(g')^{-1} = P^{-1}g^{-1}({}^tP)^{-1} = P^{-1}g^{-1}\,{}^t(P^{-1})$. In index form,
> $$g'^{\alpha\beta} = (P^{-1})^\alpha{}_\mu(P^{-1})^\beta{}_\nu\, g^{\mu\nu},$$
> which is exactly the type-$(2,0)$ law (one $P^{-1}$ per upper index). Hence $g^{\alpha\beta}$ are the components of a genuine tensor $g^{-1} = g^{\alpha\beta}e_\alpha\otimes e_\beta$ (Gourgoulhon's "inverse metric," eq 14.30), and the relation $g_{\alpha\rho}g^{\rho\beta} = \delta_\alpha{}^\beta$ is a tensor equation (both sides type $(1,1)$).

**Step 3: $\eta^{\mu\nu} = \eta_{\mu\nu}$ in an orthonormal frame is a coincidence, not a tensor equation.**

> [!note]- Derivation
> In an orthonormal frame, $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$. Its matrix inverse has diagonal entries $1/1 = 1$ and $1/(-1) = -1$, so $\eta^{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$ as well: numerically the same array. But this is *not* a tensor equation. The left side $\eta^{\mu\nu}$ is the component array of a type-$(2,0)$ tensor (transforms by $P^{-1}$ on each index); the right side $\eta_{\mu\nu}$ is that of a type-$(0,2)$ tensor (transforms by $P$). They are equal *as arrays* only in this particular (orthonormal) basis; in a curvilinear frame — say spherical coordinates, where $g_{\mu\nu} = \mathrm{diag}(1, -1, -r^2, -r^2\sin^2\theta)$ — the inverse is $g^{\mu\nu} = \mathrm{diag}(1, -1, -1/r^2, -1/(r^2\sin^2\theta))$, manifestly different. So "the metric equals its inverse" is a frame-dependent statement about a special basis, not a covariant identity; a genuine tensor equation holds in *all* bases.

**Step 4: raising both indices of $g$ gives $g^{-1}$; raising one gives $\delta$.**

> [!note]- Derivation
> *Both indices.* [[Def - Metric Duality and Index Manipulation|Raise]] both indices of $g_{\mu\nu}$ with the inverse metric:
> $$g^{\alpha\beta} := g^{\alpha\mu}g^{\beta\nu}g_{\mu\nu} = g^{\alpha\mu}\big(g^{\beta\nu}g_{\nu\mu}\big) = g^{\alpha\mu}\delta^\beta{}_\mu = g^{\alpha\beta},$$
> using $g^{\beta\nu}g_{\nu\mu} = \delta^\beta{}_\mu$. Consistent: raising both indices of the metric returns the inverse metric.
>
> *One index.* Raise one index of $g_{\mu\nu}$:
> $$g^\alpha{}_\nu := g^{\alpha\mu}g_{\mu\nu} = \delta^\alpha{}_\nu,$$
> the Kronecker delta. So the metric with one index raised *is* the identity tensor — which is why $\delta^\alpha{}_\nu$ is the "mixed-index metric," and why raising then lowering any index is the identity ($g^{\alpha\mu}g_{\mu\beta} = \delta^\alpha{}_\beta$). This is the consistency that makes the whole raising/lowering calculus self-coherent.

> [!note]- Complete formal solution
> **(1)** $g$ is type $(0,2)$; $g'_{\alpha\beta} = P^\mu{}_\alpha P^\nu{}_\beta g_{\mu\nu}$, i.e. $g' = {}^tP g P$.
> **(2)** Inverting, $g'^{\alpha\beta} = (P^{-1})^\alpha{}_\mu(P^{-1})^\beta{}_\nu g^{\mu\nu}$, the type-$(2,0)$ law, so $g^{\alpha\beta}$ is a tensor with $g_{\alpha\rho}g^{\rho\beta} = \delta_\alpha{}^\beta$.
> **(3)** $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$ has matrix inverse $\eta^{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$, numerically equal — but as components of type-$(2,0)$ and type-$(0,2)$ tensors they transform differently, so the equality is basis-specific (it fails in curvilinear coordinates).
> **(4)** $g^{\alpha\mu}g^{\beta\nu}g_{\mu\nu} = g^{\alpha\beta}$ (raise both → inverse metric); $g^{\alpha\mu}g_{\mu\nu} = \delta^\alpha{}_\nu$ (raise one → Kronecker delta). $\blacksquare$

---

# Key Takeaways

**The metric and its inverse are genuinely different tensors that happen to share components in an orthonormal frame.** The metric $g_{\alpha\beta}$ is type $(0,2)$ and the inverse metric $g^{\alpha\beta}$ is type $(2,0)$; they live in different spaces and transform by inverse matrices. Their numerical equality $\eta^{\mu\nu} = \eta_{\mu\nu}$ in an orthonormal frame is a property of that special basis — it is what "orthonormal" means — and it dissolves the moment one moves to curvilinear coordinates, where $g^{\alpha\beta}$ is the literal matrix inverse of $g_{\alpha\beta}$ and looks completely different. The transferable lesson is to distinguish a *tensor equation* (holds in every basis, e.g. $g_{\alpha\rho}g^{\rho\beta} = \delta_\alpha{}^\beta$) from a *component coincidence* (holds in a special basis, e.g. $\eta^{\mu\nu} = \eta_{\mu\nu}$). When you see two component arrays equated, ask whether they are components of the same-type tensor — if not, the equation is basis-dependent and will break in another frame. This becomes essential in [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative|curvilinear coordinates]] and in general relativity, where one almost never works in an orthonormal frame.

**The metric with one index raised is the identity tensor.** The relation $g^\alpha{}_\beta = \delta^\alpha{}_\beta$ is the keystone of the raising/lowering calculus: it says that the metric and its inverse are mutually inverse as the maps "lower" and "raise," so that doing one then the other returns the original. This is why one never writes $g^\alpha{}_\beta$ as a separate object — it is just $\delta^\alpha{}_\beta$ — and why $g^{\alpha\mu}g_{\mu\beta}X^\beta = X^\alpha$. The reusable consequence is the consistency of all index manipulations: any chain of raises and lowers that returns each index to its original position is the identity, so you can move indices around freely without worrying that the operations fail to compose. Whenever a computation produces $g$ contracted with $g^{-1}$ on a shared index, replace it immediately by a Kronecker delta and continue.

**The bilinear-form law $g' = {}^tP\,g\,P$ is the matrix face of the type-$(0,2)$ tensor law.** Recognising that the abstract "one $P$ per lower index" rule is, for a two-index object, the familiar matrix congruence $g' = {}^tP g P$ connects the index calculus to ordinary linear algebra. The same identification shows that the inverse metric transforms by the inverse congruence, and that an *endomorphism* (type $(1,1)$, e.g. a Lorentz transformation) transforms by similarity $T' = P^{-1}T P$ instead — three different matrix laws ($\,{}^tP g P$ for bilinear forms, $P^{-1}TP$ for endomorphisms, $P^{-1}$ and $P$ for vectors and forms) all unified as special cases of the single tensor transformation rule. Knowing which matrix law a given object obeys, by reading its index structure, is the bridge between abstract tensor algebra and concrete matrix computation, and it prevents the common error of using the wrong transformation (e.g. similarity for a bilinear form, which would be wrong unless $P$ is orthogonal).
