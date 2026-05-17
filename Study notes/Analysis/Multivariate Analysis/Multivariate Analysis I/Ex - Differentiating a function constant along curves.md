---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Chain Rule"
  - "Thm - The Mean Value Inequality"
  - "Def - Directional Derivative and the Gradient"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $f : \mathbb{R}^2 \to \mathbb{R}$ be differentiable.

1. Suppose $f$ is **constant on every circle centred at the origin** — that is, $f(x,y)$ depends only on $r = \sqrt{x^2+y^2}$. By differentiating the constancy relation along a circle, show that the gradient $\nabla f$ is everywhere **radial**: $\nabla f(x,y)$ is parallel to the position vector $(x,y)$ at every point off the origin.
2. Conversely, suppose $\nabla f$ is everywhere radial. Show that $f$ is constant on every circle centred at the origin. *(Use the mean value inequality along arcs.)*
3. Conclude: a differentiable $f : \mathbb{R}^2\setminus\{0\} \to \mathbb{R}$ is **rotationally symmetric** (a function of $r$ alone) if and only if its gradient is everywhere radial.

**Recall:**

The technique is to differentiate a stated invariance relation, using the chain rule, and to read off a constraint on the gradient.

![[Thm - The Chain Rule#Statement]]

The [[Thm - The Chain Rule|chain rule]] in the curve form: if $\gamma : I \to \mathbb{R}^2$ is a differentiable curve and $f$ is differentiable, then $\frac{d}{dt}f(\gamma(t)) = Df_{\gamma(t)}(\gamma'(t)) = \nabla f(\gamma(t))\cdot\gamma'(t)$.

The [[Def - Directional Derivative and the Gradient|gradient]] $\nabla f$ represents the derivative: $\partial_v f = \nabla f\cdot v$. The gradient is orthogonal to the level sets of $f$.

![[Thm - The Mean Value Inequality#Statement]]

The [[Thm - The Mean Value Inequality|mean value inequality]] (constancy corollary): if the derivative of a function vanishes on a connected set, the function is constant there.

---

# Convergent Strategy

**Problem class.** Part 1 is a *structural identity* problem — "differentiate a given invariance relation to extract a constraint on the derivative" — and Part 2 is a *bounding/constancy* problem. As the [[Multivariate Analysis I — Differentiation in Several Variables#Problem-Solving Strategy|topic page strategy]] states, whenever the hypothesis is an equation valid on an open set or a family of curves, the route is to differentiate that equation with the chain rule; and "prove constant" is the mean value inequality with bound zero.

**Assumption pattern.** The hypothesis is a *symmetry*: $f$ is constant along a family of curves (concentric circles). The recognisable feature: an invariance stated geometrically. The standard move on any symmetry hypothesis is to differentiate the relation expressing it.

**Theorem routing.** Part 1: parametrise a circle by $\gamma(t) = (r\cos t, r\sin t)$; the constancy of $f$ along it means $f(\gamma(t))$ is constant in $t$, so its $t$-derivative is zero; the [[Thm - The Chain Rule|chain rule]] computes that derivative as $\nabla f(\gamma(t))\cdot\gamma'(t)$, and the velocity $\gamma'(t)$ is the *tangent* to the circle, so $\nabla f$ is orthogonal to the circle's tangent, hence radial. Part 2: radial gradient means $\nabla f$ is orthogonal to every circle's tangent, so the directional derivative of $f$ along any circle is zero, so $f$ restricted to a circle has vanishing derivative; the [[Thm - The Mean Value Inequality|mean value inequality]]'s constancy corollary (a circle is connected) makes $f$ constant on the circle.

**Key decision point.** The non-obvious realisation is that "constant along circles" and "gradient radial" are *the same statement viewed from two sides*, mediated by orthogonality. The circle's tangent and its radius are orthogonal. The gradient is orthogonal to level sets. So: $f$ constant on circles $\Leftrightarrow$ circles are level sets $\Leftrightarrow$ $\nabla f \perp$ circle tangents $\Leftrightarrow$ $\nabla f \parallel$ radius. Seeing this orthogonality dictionary is what makes both directions short. The forward direction differentiates; the converse integrates back via the constancy corollary.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Differentiate an identity.** The constancy of $f$ along a circle is an identity in the parameter $t$; differentiate it.

2. **Restrict to a curve and apply the chain rule.** Parametrise a circle as a curve $\gamma(t)$ and use $\frac{d}{dt}f(\gamma(t)) = \nabla f(\gamma(t))\cdot\gamma'(t)$.

3. **Use the gradient identity.** $\partial_v f = \nabla f\cdot v$ — the directional derivative along the circle's tangent is the dot product of $\nabla f$ with that tangent.

4. **Convert a vanishing derivative into constancy.** Apply the mean value inequality's constancy corollary on a connected set (the circle).

---

# Hints

> [!note]- Hint 1
> Parametrise the circle of radius $r$ as $\gamma(t) = (r\cos t, r\sin t)$, $t \in [0, 2\pi]$. The hypothesis says $f$ is constant along this curve: $f(\gamma(t))$ does not depend on $t$. So $\frac{d}{dt}f(\gamma(t)) = 0$. Now use the chain rule to compute that derivative.

> [!note]- Hint 2
> The chain rule gives $\frac{d}{dt}f(\gamma(t)) = \nabla f(\gamma(t))\cdot\gamma'(t)$. Compute $\gamma'(t) = (-r\sin t, r\cos t)$ — this is the velocity, *tangent* to the circle. Setting the derivative to zero: $\nabla f(\gamma(t))\cdot\gamma'(t) = 0$, so $\nabla f$ is orthogonal to the tangent vector of the circle.

> [!note]- Hint 3
> A vector orthogonal to the tangent $(-r\sin t, r\cos t)$ of the circle must be parallel to the radius $(r\cos t, r\sin t) = \gamma(t)$ — in the plane, the orthogonal complement of a line is a line. So $\nabla f(\gamma(t)) \parallel \gamma(t)$: the gradient is radial.

> [!note]- Hint 4
> For Part 2, run the argument backwards. If $\nabla f$ is radial, it is parallel to $\gamma(t)$, hence orthogonal to the tangent $\gamma'(t)$, so $\frac{d}{dt}f(\gamma(t)) = \nabla f\cdot\gamma'(t) = 0$. Thus $t \mapsto f(\gamma(t))$ has zero derivative on the connected interval $[0,2\pi]$ — the constancy corollary of the mean value inequality makes it constant. So $f$ is constant on the circle.

---

# Solution

The exercise is the orthogonality dictionary "$f$ constant on circles $\Leftrightarrow$ $\nabla f$ radial" made precise. Both directions are one application of the chain rule along a circular curve; the forward direction reads the derivative being zero as a constraint, the converse reads the constraint as the derivative being zero and integrates it back.

**Step 1: If $f$ is constant on circles, then $\nabla f$ is radial.**

> [!note]- Derivation
> Fix $r > 0$ and parametrise the circle of radius $r$ by the curve $\gamma : [0,2\pi] \to \mathbb{R}^2$, $\gamma(t) = (r\cos t, r\sin t)$. Its velocity is
> $$\gamma'(t) = (-r\sin t,\ r\cos t),$$
> which is the tangent vector to the circle at $\gamma(t)$.
>
> By hypothesis $f$ takes the same value at every point of this circle, so the function $t \mapsto f(\gamma(t))$ is constant on $[0,2\pi]$, and therefore
> $$\frac{d}{dt}f(\gamma(t)) = 0 \qquad\text{for all } t.$$
> By [[Thm - The Chain Rule|the chain rule]] in curve form,
> $$\frac{d}{dt}f(\gamma(t)) = Df_{\gamma(t)}(\gamma'(t)) = \nabla f(\gamma(t))\cdot\gamma'(t).$$
> Combining, $\nabla f(\gamma(t))\cdot\gamma'(t) = 0$ for every $t$: the gradient is orthogonal to the circle's tangent vector at every point.
>
> Now, at the point $p = \gamma(t) = (r\cos t, r\sin t)$, the tangent $\gamma'(t) = (-r\sin t, r\cos t)$ and the position vector $p$ itself satisfy $\gamma'(t)\cdot p = -r^2\sin t\cos t + r^2\cos t\sin t = 0$ — they are orthogonal. In the plane the orthogonal complement of a non-zero vector is a one-dimensional line, so any vector orthogonal to $\gamma'(t)$ is a scalar multiple of $p$. Since $\nabla f(p)$ is orthogonal to $\gamma'(t)$, it is parallel to $p = (x,y)$. As every point off the origin lies on some circle, $\nabla f$ is radial everywhere on $\mathbb{R}^2\setminus\{0\}$.

**Step 2: If $\nabla f$ is radial, then $f$ is constant on circles.**

> [!note]- Derivation
> Suppose $\nabla f(x,y)$ is parallel to $(x,y)$ at every point off the origin. Fix $r > 0$ and the circle $\gamma(t) = (r\cos t, r\sin t)$ as before.
>
> At each point $\gamma(t)$, the gradient $\nabla f(\gamma(t))$ is parallel to the position vector $\gamma(t)$, and we showed in Step 1 that $\gamma(t)$ is orthogonal to the tangent $\gamma'(t)$. A vector parallel to $\gamma(t)$ is therefore orthogonal to $\gamma'(t)$:
> $$\nabla f(\gamma(t))\cdot\gamma'(t) = 0.$$
> By [[Thm - The Chain Rule|the chain rule]], this is exactly $\frac{d}{dt}f(\gamma(t)) = 0$ for all $t \in [0,2\pi]$.
>
> So the one-variable function $\psi(t) := f(\gamma(t))$ has $\psi'(t) = 0$ on the connected interval $[0,2\pi]$. By the constancy corollary of the [[Thm - The Mean Value Inequality|mean value inequality]] — a function with vanishing derivative on a connected set is constant — $\psi$ is constant. Hence $f$ takes the same value at every point of the circle of radius $r$. Since $r$ was arbitrary, $f$ is constant on every circle centred at the origin.

**Step 3: Rotational symmetry is equivalent to a radial gradient.**

> [!note]- Derivation
> "$f$ is rotationally symmetric" means $f$ takes a value depending only on $r = \sqrt{x^2+y^2}$ — equivalently, $f$ is constant on every circle centred at the origin (two points share an $r$ exactly when they lie on a common such circle). Step 1 shows this implies $\nabla f$ radial; Step 2 shows a radial gradient implies constancy on circles, hence rotational symmetry. The two implications together give the equivalence:
> $$f \text{ rotationally symmetric on } \mathbb{R}^2\setminus\{0\} \quad\Longleftrightarrow\quad \nabla f \text{ radial everywhere on } \mathbb{R}^2\setminus\{0\}.$$

> [!note]- Complete formal solution
> **Claim.** A differentiable $f$ on $\mathbb{R}^2\setminus\{0\}$ is rotationally symmetric iff $\nabla f$ is everywhere radial.
>
> Parametrise the circle of radius $r$ by $\gamma(t) = (r\cos t, r\sin t)$, $\gamma'(t) = (-r\sin t, r\cos t)$; note $\gamma(t)\cdot\gamma'(t) = 0$. By [[Thm - The Chain Rule]], $\frac{d}{dt}f(\gamma(t)) = \nabla f(\gamma(t))\cdot\gamma'(t)$.
>
> ($\Rightarrow$) If $f$ is rotationally symmetric, $f(\gamma(t))$ is constant in $t$, so $\nabla f(\gamma(t))\cdot\gamma'(t) = 0$; thus $\nabla f(\gamma(t))$ is orthogonal to $\gamma'(t)$, hence (in the plane) parallel to $\gamma(t)$ — radial. Every non-origin point lies on such a circle.
>
> ($\Leftarrow$) If $\nabla f$ is radial, then $\nabla f(\gamma(t)) \parallel \gamma(t) \perp \gamma'(t)$, so $\frac{d}{dt}f(\gamma(t)) = \nabla f(\gamma(t))\cdot\gamma'(t) = 0$ on the connected interval $[0,2\pi]$. By the constancy corollary of [[Thm - The Mean Value Inequality]], $f(\gamma(t))$ is constant, so $f$ is constant on each circle — rotationally symmetric. $\blacksquare$

---

# Key Takeaways

**A stated symmetry should be differentiated: an invariance relation becomes a differential constraint via the chain rule.** This is the universal handling of any symmetry hypothesis, and it is one of the highest-yield moves in the subject. Whenever a function is assumed constant along a family of curves, invariant under a group of transformations, or homogeneous of some degree, the hypothesis is an *equation valid on an open set*, and differentiating that equation — with the chain rule doing the differentiation along the relevant curves — extracts a pointwise constraint on the derivative. Here, "constant along circles" differentiated along the circular curve produced "$\nabla f \perp$ tangent". The same move produces Euler's identity from homogeneity, the conservation laws from invariances (Noether's theorem is this idea in the calculus of variations), and the eikonal-type constraints from level-set hypotheses. The trigger is unmistakable: an invariance, stated geometrically or algebraically, is an invitation to differentiate it.

**The orthogonality dictionary — gradient $\perp$ level set, tangent $\perp$ normal — converts geometric hypotheses into algebraic ones and back.** The exercise turned on a single geometric fact: the gradient is orthogonal to level sets, and a circle's tangent is orthogonal to its radius. Chaining these, "$f$ constant on circles" (circles are level sets) is equivalent to "$\nabla f \perp$ circle tangents" (gradient normal to level sets) is equivalent to "$\nabla f \parallel$ radius". Each $\Leftrightarrow$ is an orthogonality statement. This dictionary is reusable far beyond circles: to show a curve stays on a level set, show the velocity is orthogonal to $\nabla f$; to find the normal direction to a surface, compute $\nabla f$; to recognise that a flow preserves a quantity, check the flow's velocity is tangent to that quantity's level sets. Geometry and the algebra of the gradient are two faces of the same coin, and the dot product is the hinge.

**The forward and converse directions of a structural equivalence are differentiate-and-integrate: the chain rule going out, the constancy corollary coming back.** Part 1 and Part 2 are mirror images, and recognising the symmetry is itself a takeaway. The forward direction takes a global statement (constant on circles) and *differentiates* it down to a pointwise condition (radial gradient) — the chain rule is the differentiation. The converse takes the pointwise condition and *integrates* it back up to the global statement — and the integration is the constancy corollary of the mean value inequality, which is precisely "vanishing derivative on a connected set $\Rightarrow$ constant", the multivariate fundamental theorem of calculus in its crudest form. This differentiate-out / integrate-back pairing is the standard architecture for proving that a pointwise differential condition is equivalent to a global structural property; the only subtlety on the return trip is that the constancy corollary needs *connectedness* of the set along which you integrate — here the circle, which is connected, so the corollary applies.
