---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Pullback of a Covariant Tensor Field"
  - "Def - Tensor Field on a Manifold"
  - "Thm - Pullback Commutes with Tensor Product"
tags: [geometry, differential-geometry, pullback]
---

# Problem Statement

Let $M = \{(r, \theta) : r > 0,\ |\theta| < \pi/2\}$ and $N = \{(x, y) : x > 0\}$, both as open submanifolds of $\mathbb{R}^2$. Let $F : M \to N$ be the smooth map $F(r, \theta) = (r\cos\theta, r\sin\theta)$ (polar to Cartesian). On $N$, consider the covariant 2-tensor field

$$A = x^2\, dy \otimes dy.$$

Compute the pullback $F^*A$, expressed in the coordinates $(r, \theta)$ on $M$.

**Recall:**

A [[Def - Tensor Field on a Manifold|covariant 2-tensor field]] on a manifold $N$ is, at each point $q \in N$, a bilinear functional $A_q : T_qN \times T_qN \to \mathbb{R}$, varying smoothly with $q$. In a chart $(y^i)$ on $N$, $A$ is written $A = A_{ij}(y)\, dy^i \otimes dy^j$, with $A_{ij}(y)$ the smooth component functions.

The [[Def - Pullback of a Covariant Tensor Field|pullback]] of a covariant tensor field $A$ on $N$ by a smooth map $F : M \to N$ is the covariant tensor field $F^*A$ on $M$ defined pointwise by

$$(F^*A)_p(v_1, \dots, v_k) = A_{F(p)}(dF_p(v_1), \dots, dF_p(v_k)).$$

The key computational tool is the **[[Thm - Pullback Commutes with Tensor Product|naturality identities]]**: $F^*(f\,B) = (f \circ F)\, F^*B$ for any smooth function $f$ on $N$ and any covariant tensor field $B$, and $F^*(A \otimes B) = F^*A \otimes F^*B$. Pullback of a function is composition: $F^*f = f \circ F$. Pullback of a 1-form $dy^i$ on $N$ is the differential of the $i$-th coordinate function of $F$: $F^*(dy^i) = dF^i$, which by the chain rule equals $(\partial F^i / \partial x^a)\, dx^a$ — see [[Def - Pullback of a Covector Field]].

---

# Convergent Strategy

**Problem class.** This is a pullback computation in coordinates. As the [[Differential Geometry VII — Tensors and Tensor Fields#Problem-Solving Strategy|chapter's problem-solving strategy]] urges, the recipe is to apply the naturality identities ($F^*$ commutes with tensor product, $F^*f = f \circ F$, $F^*dy^i = dF^i$) recursively until the computation reduces to expanding $dF^i$ via the chain rule and simplifying. The substitute-and-expand algorithm.

**Assumption pattern.** Two hypotheses are in play. First, $A$ is expressed in coordinates on $N$ as a product of a function $x^2$ and a tensor product $dy \otimes dy$; this lets us apply both the function-pullback identity and the tensor-product identity. Second, $F$ is the specific polar-to-Cartesian map, with coordinate functions $F^1(r, \theta) = r\cos\theta$ and $F^2(r, \theta) = r\sin\theta$. These two coordinate functions are what feed the chain rule.

**Theorem routing.** The route is: [[Thm - Pullback Commutes with Tensor Product|naturality of pullback]] gives $F^*A = F^*(x^2) \cdot F^*(dy) \otimes F^*(dy)$. Then $F^*(x^2) = (x^2 \circ F)(r, \theta) = (r\cos\theta)^2 = r^2 \cos^2\theta$. And $F^*(dy) = dF^2 = d(r\sin\theta) = \sin\theta\, dr + r\cos\theta\, d\theta$ by the chain rule on $F^2(r, \theta) = r\sin\theta$. Substituting and expanding gives the answer.

**Key decision point.** The non-obvious choice is to use the *naturality identities* to break $A$ apart before computing, rather than directly applying the definition $(F^*A)_p(v_1, v_2) = A_{F(p)}(dF v_1, dF v_2)$. The direct approach requires evaluating $A_{F(p)}$ on $dF v_1$ and $dF v_2$ explicitly for each pair of vectors; the naturality approach breaks the problem into smaller, mechanical steps. For higher-rank tensors with mixed function and tensor-product structure, the naturality approach is the *only* tractable method.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry VII — Tensors and Tensor Fields#Legal Operations|the topic page's Legal Operations]]:

1. **Pull back covariant tensor fields** (operation 5). The central operation: the goal is precisely to compute $F^*A$, and the naturality identities applied recursively are how it is done.

2. **Take the tensor product of two tensor fields** (operation 1). Used implicitly: $A$ is presented as $x^2 \otimes dy \otimes dy$ (with $x^2$ a function regarded as a $(0, 0)$-tensor, and the two $dy$ as 1-forms). The pullback respects this tensor product structure.

3. **Multiply a tensor field by a smooth function** (operation 9). Used to convert $x^2 \otimes dy \otimes dy$ to $x^2 \cdot (dy \otimes dy)$ and back; the pullback distributes over this product as $F^*(x^2) \cdot F^*(dy \otimes dy)$.

4. **Compute components in a chart** (operation 3). The final answer is read off in the $(r, \theta)$ chart on $M$, with the $2 \times 2$ component matrix of $F^*A$ exhibited explicitly.

---

# Hints

> [!note]- Hint 1
> Start by applying the naturality of pullback: $F^*(A \otimes B) = F^*A \otimes F^*B$, and $F^*(f B) = (f \circ F)\, F^*B$. Use these to break $A = x^2 \cdot dy \otimes dy$ into its function part $x^2$ and its tensor-product part $dy \otimes dy$.

> [!note]- Hint 2
> The pullback of the 1-form $dy$ is the differential of the $y$-coordinate function of $F$ — that is, $F^*(dy) = d(y \circ F) = d(r\sin\theta)$. Use the chain rule on $r\sin\theta$ to express $d(r\sin\theta)$ as a linear combination of $dr$ and $d\theta$.

> [!note]- Hint 3
> After computing $F^*(dy) = \sin\theta\, dr + r\cos\theta\, d\theta$, take the tensor product of this 1-form with itself, then multiply by $F^*(x^2) = r^2\cos^2\theta$. Be careful: the tensor product is *not* commutative, so $dr \otimes d\theta \neq d\theta \otimes dr$. Expand the product term by term.

---

# Solution

The proof breaks into three steps. Step 1 applies the naturality identities to reduce $F^*A$ to a product of $F^*(x^2)$ with $F^*(dy) \otimes F^*(dy)$. Step 2 computes $F^*(dy)$ via the chain rule. Step 3 substitutes and expands the tensor product.

**Step 1: Apply naturality to decompose $F^*A$.**

By the naturality identities of [[Thm - Pullback Commutes with Tensor Product]], $F^*A = F^*(x^2 \cdot dy \otimes dy) = F^*(x^2) \cdot F^*(dy) \otimes F^*(dy)$, and $F^*(x^2)$ is the function $x^2$ composed with $F$.

> [!note]- Derivation
> By property (3) of the pullback ($F^*(fB) = (f \circ F)\, F^*B$),
> $$F^*A = F^*(x^2 \cdot (dy \otimes dy)) = (x^2 \circ F) \cdot F^*(dy \otimes dy).$$
> By property (2) of the pullback ($F^*(A \otimes B) = F^*A \otimes F^*B$),
> $$F^*(dy \otimes dy) = F^*(dy) \otimes F^*(dy).$$
> Combining: $F^*A = (x^2 \circ F) \cdot F^*(dy) \otimes F^*(dy)$.
>
> Compute $x^2 \circ F$: at the point $(r, \theta)$ in $M$, $F(r, \theta) = (r\cos\theta, r\sin\theta) = (x, y)$, so $x = r\cos\theta$ and $x^2 = r^2\cos^2\theta$. Hence $(x^2 \circ F)(r, \theta) = r^2 \cos^2\theta$.

**Step 2: Compute $F^*(dy)$ via the chain rule.**

$F^*(dy) = d(y \circ F) = d(r\sin\theta)$, and the chain rule gives $d(r\sin\theta) = \sin\theta\, dr + r\cos\theta\, d\theta$.

> [!note]- Derivation
> The 1-form $dy$ on $N$ has the property $dy(\partial_y) = 1, dy(\partial_x) = 0$ — it is the dual basis vector to $\partial_y$. By the definition of the pullback of a 1-form (or the [[Def - Pullback of a Covector Field|pullback of a covector field]] formula),
> $$F^*(dy) = d(y \circ F),$$
> where $y \circ F$ is the $y$-coordinate of $F$. From $F(r, \theta) = (r\cos\theta, r\sin\theta)$, the $y$-coordinate of $F$ is $r\sin\theta$, so
> $$F^*(dy) = d(r\sin\theta).$$
> Apply the chain rule (or just compute the partials):
> $$d(r\sin\theta) = \frac{\partial(r\sin\theta)}{\partial r}\, dr + \frac{\partial(r\sin\theta)}{\partial \theta}\, d\theta = \sin\theta\, dr + r\cos\theta\, d\theta.$$
> So $F^*(dy) = \sin\theta\, dr + r\cos\theta\, d\theta$.

**Step 3: Substitute and expand.**

Substituting into $F^*A = (x^2 \circ F) \cdot F^*(dy) \otimes F^*(dy)$:

$$F^*A = r^2\cos^2\theta \cdot (\sin\theta\, dr + r\cos\theta\, d\theta) \otimes (\sin\theta\, dr + r\cos\theta\, d\theta).$$

Expand the tensor product by bilinearity:

> [!note]- Derivation
> Distributing the tensor product over the sum (using bilinearity of $\otimes$):
> $$(\sin\theta\, dr + r\cos\theta\, d\theta) \otimes (\sin\theta\, dr + r\cos\theta\, d\theta)$$
> $$= \sin^2\theta\, dr \otimes dr + r\sin\theta\cos\theta\, dr \otimes d\theta + r\sin\theta\cos\theta\, d\theta \otimes dr + r^2\cos^2\theta\, d\theta \otimes d\theta.$$
> Multiplying through by $r^2\cos^2\theta$:
> $$F^*A = r^2\sin^2\theta\cos^2\theta\, dr \otimes dr + r^3\sin\theta\cos^3\theta\, (dr \otimes d\theta + d\theta \otimes dr) + r^4\cos^4\theta\, d\theta \otimes d\theta.$$
> (Note: $dr \otimes d\theta \neq d\theta \otimes dr$ in general, so we keep both cross terms.)

> [!note]- Complete formal solution
> Setting up: $A = x^2\, dy \otimes dy$ on $N$, $F(r, \theta) = (r\cos\theta, r\sin\theta)$, want $F^*A$ on $M$ in the $(r, \theta)$ chart.
>
> *Step 1.* By naturality of pullback,
> $$F^*A = F^*(x^2) \cdot F^*(dy) \otimes F^*(dy) = (r\cos\theta)^2 \cdot F^*(dy) \otimes F^*(dy) = r^2\cos^2\theta \cdot F^*(dy) \otimes F^*(dy).$$
>
> *Step 2.* The pullback of the 1-form $dy$ along $F$ is $F^*(dy) = d(y \circ F) = d(r\sin\theta) = \sin\theta\, dr + r\cos\theta\, d\theta$.
>
> *Step 3.* Substituting and expanding the tensor product:
> $$F^*A = r^2\cos^2\theta\, (\sin\theta\, dr + r\cos\theta\, d\theta) \otimes (\sin\theta\, dr + r\cos\theta\, d\theta)$$
> $$= r^2\sin^2\theta\cos^2\theta\, dr \otimes dr + r^3\sin\theta\cos^3\theta\, (dr \otimes d\theta + d\theta \otimes dr) + r^4\cos^4\theta\, d\theta \otimes d\theta. \quad \blacksquare$$

> [!warning] Illegal but tempting: "the answer is $r^2\cos^2\theta\, dy \otimes dy$"
> A common mistake is to leave the answer in terms of $dy$ rather than pulling back fully. But $dy$ is a 1-form on $N$, not on $M$ — it is not defined on $M$ at all. To express $F^*A$ in coordinates on $M$, one must complete the substitution and expand in $dr, d\theta$. The error reflects the confusion between $F^*$ (which transports the tensor field back to $M$) and a mere rewriting of components in different coordinates of $N$ (which is the transformation rule for components within a single manifold, not pullback between manifolds). The fact that here $M$ and $N$ are essentially the same set with different coordinates can hide this distinction — but it is crucial.

---

# Key Takeaways

**The recipe is "naturality then chain rule".** Pullback in coordinates breaks into two layers. The outer layer uses the naturality of pullback ($F^*$ commutes with tensor product and respects function multiplication) to reduce the problem to pulling back 1-forms and functions. The inner layer uses the chain rule on the coordinate functions of $F$ to compute the pullback of each 1-form $dy^i$ as $dF^i$. The recursion always terminates because 1-forms and functions are the base cases. This recipe scales to any rank, any type, any smooth map — substitute and expand, the Jacobian factors take care of themselves.

**The Jacobian appears automatically.** A common conceptual stumbling block is: "where's the Jacobian determinant in the change-of-variables formula?" The answer is that the Jacobian appears in the *components* of the pulled-back tensor, distributed across the slots. For the volume form $\omega = dx \wedge dy$, the pullback gives $r\, dr \wedge d\theta$ — the $r$ in front is precisely the Jacobian of polar coordinates ($\det J = r$). For tensors of other ranks, the Jacobian factors are spread across multiple slots. The point is: you do not need to multiply by the Jacobian by hand; the pullback formula already includes it.

**Tensor products are not commutative.** When expanding the tensor product $F^*(dy) \otimes F^*(dy) = (\sin\theta\, dr + r\cos\theta\, d\theta) \otimes (\sin\theta\, dr + r\cos\theta\, d\theta)$, the cross terms $dr \otimes d\theta$ and $d\theta \otimes dr$ must be kept separate. They are equal only when we symmetrize (e.g., when computing the symmetric part for a metric) or anti-symmetrize (e.g., for a 2-form). For a generic covariant 2-tensor, both terms have independent component coefficients. This is the key place where the "tensorial" calculus differs from the "form" calculus — in form calculus, $dr \wedge d\theta = -d\theta \wedge dr$, so the cross terms collapse with a sign. For tensors, no such cancellation occurs.

**The substitute-and-expand recipe is the engine of every coordinate calculation in differential geometry.** Whenever you compute the metric in non-Cartesian coordinates, the Christoffel symbols, the Laplace-Beltrami operator, the divergence of a vector field — all of them ultimately go through some version of this exercise: write the abstract object using its coordinate-free definition, substitute the coordinate functions, expand the differentials via the chain rule, multiply out. The key skill is to mechanically execute this without making algebra mistakes, since the calculations grow rapidly with rank and [[Def - Dimension|dimension]]. The exercise [[Ex - The Metric Tensor in Polar Coordinates]] is the most important worked instance: it shows how the Euclidean metric becomes $g = dr \otimes dr + r^2\, d\theta \otimes d\theta$ in polar coordinates, with the famous $r^2$ factor emerging from the same substitution-and-expansion process used here.
