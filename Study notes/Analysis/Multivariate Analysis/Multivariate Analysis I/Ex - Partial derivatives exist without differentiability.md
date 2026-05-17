---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Def - Directional Derivative and the Gradient"
  - "Thm - Differentiability Implies Continuity"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Consider $f : \mathbb{R}^2 \to \mathbb{R}$ defined by
$$f(x,y) = \begin{cases} \dfrac{xy}{\sqrt{x^2+y^2}} & (x,y) \neq (0,0), \\[2mm] 0 & (x,y) = (0,0). \end{cases}$$

1. Show that both partial derivatives $\partial_x f(0,0)$ and $\partial_y f(0,0)$ **exist** and equal $0$.
2. Show that $f$ is **continuous** at the origin.
3. Show that $f$ is **not differentiable** at the origin. (Do this two ways: by showing the directional derivative is not linear in the direction, and by showing the defining $o(|h|)$ limit fails along a path.)

Thus the existence of all partial derivatives is *strictly weaker* than differentiability — even for a function that is continuous.

**Recall:**

The objects in tension are partial derivatives, differentiability, and the directional derivative.

The $j$-th [[Def - Partial Derivatives and the Jacobian Matrix|partial derivative]] $\partial_j f(0,0)$ is the one-variable derivative of $f$ restricted to the $j$-th coordinate axis. Existence of all $n$ partials is the *weakest* of the regularity conditions.

![[Def - The Total Derivative and Differentiability#The Definition]]

$f$ is [[Def - The Total Derivative and Differentiability|differentiable]] at $x_\circ$ when a linear $L$ exists with $f(x_\circ+h)-f(x_\circ)-L(h) = o(|h|)$.

![[Def - Directional Derivative and the Gradient#The Definition]]

If $f$ is differentiable, the [[Def - Directional Derivative and the Gradient|directional derivative]] satisfies $\partial_v f(x_\circ) = Df_{x_\circ}(v)$, hence is **linear in $v$**. Non-linearity of $v \mapsto \partial_v f$ is therefore a certificate of non-differentiability.

![[Thm - Differentiability Implies Continuity#Statement]]

This exercise's function is continuous, so the discontinuity route to non-differentiability ([[Thm - Differentiability Implies Continuity]]) is *unavailable* — a more refined obstruction is needed.

---

# Convergent Strategy

**Problem class.** This is a *separating-example* problem for the lower gap of the regularity ladder: "partials exist" versus "differentiable". It is the companion of [[Ex - A function differentiable but not continuously differentiable]], which separates the upper gap. As the [[Multivariate Analysis I — Differentiation in Several Variables#Insights|topic page]] stresses, each strict gap needs a named witness; this is the witness for the lower gap, and it is sharper than the usual one because the function is also continuous.

**Assumption pattern.** The function is a degree-$2$ numerator over a degree-$1$ denominator (in the homogeneity sense): it is **positively homogeneous of degree $1$**, meaning $f(tx, ty) = t\,f(x,y)$ for $t > 0$. A degree-$1$ homogeneous function is the danger zone for differentiability: it is "linear along rays" but its behaviour across rays can be anything. Such a function is differentiable at the origin if and only if it is *globally linear*, and this one visibly is not. The recognisable feature is homogeneity of degree exactly $1$ with a non-linear ray dependence.

**Theorem routing.** Part 1 computes the partials at the origin from the limit definition; $f$ is identically zero on each axis, so both partials are $0$. Part 2 proves continuity by the bound $|f(x,y)| \le \tfrac12\sqrt{x^2+y^2}$, from $|xy| \le \tfrac12(x^2+y^2)$. Part 3 attacks non-differentiability. The cheapest obstruction — discontinuity, via [[Thm - Differentiability Implies Continuity]] — is *blocked* by Part 2. So we climb to the next obstruction: compute the directional derivative $\partial_v f(0,0)$ in a general direction and show it is *not linear in $v$*. Since differentiability would force $\partial_v f(0,0) = Df_{(0,0)}(v)$, linear in $v$, non-linearity is a contradiction.

**Key decision point.** The non-obvious move is recognising that continuity does *not* rescue differentiability and choosing the right obstruction. The instinct after Parts 1–2 — partials exist, function is continuous — is to expect differentiability. The decisive realisation is that the candidate derivative is forced to be $L = 0$ (from the zero partials), so differentiability would mean $f(h) = o(|h|)$, i.e. $f$ vanishes faster than first order; but a degree-$1$ homogeneous function vanishes *exactly* to first order along any ray, so it can be $o(|h|)$ only if it is identically zero near the origin. It is not. The directional-derivative test packages this cleanly: $\partial_v f(0,0)$ exists for every $v$ but is a non-linear function of $v$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Compute partials at the suspect point from the limit definition.** $\partial_x f(0,0) = \lim_{t\to0}(f(t,0)-f(0,0))/t$; the function vanishes on each axis, so both partials are $0$.

2. **Recover the forced candidate derivative.** Zero partials force the only candidate to be $L = 0$.

3. **Restrict to a line to compute directional derivatives.** Evaluate $f$ along the ray $t \mapsto tv$ and differentiate in $t$ — this gives $\partial_v f(0,0)$ for every direction $v$.

4. **Disprove differentiability via non-linearity of the directional derivative.** Differentiability forces $\partial_v f(0,0)$ to be linear in $v$; exhibit its non-linearity.

5. **Disprove the $o(|h|)$ condition along a path.** As an independent confirmation, show $|f(h) - L(h)|/|h|$ does not tend to $0$ along the diagonal $h = (t,t)$.

---

# Hints

> [!note]- Hint 1
> For Part 1, restrict $f$ to the $x$-axis: what is $f(t, 0)$? The numerator $xy$ has a factor of $y = 0$. So $f$ is identically $0$ along each axis, and the partials at the origin — which only see $f$ along the axes — are $0$.

> [!note]- Hint 2
> For Part 2, you need $|f(x,y)| \to 0$ as $(x,y)\to(0,0)$. Use the inequality $|xy| \le \tfrac12(x^2+y^2)$ (it is $(|x|-|y|)^2 \ge 0$ rearranged). Then $|f| = |xy|/\sqrt{x^2+y^2} \le \tfrac12(x^2+y^2)/\sqrt{x^2+y^2} = \tfrac12\sqrt{x^2+y^2}$.

> [!note]- Hint 3
> For Part 3, the candidate derivative is forced by Part 1 to be $L = 0$. So differentiability would mean $f(h) = o(|h|)$. Compute the directional derivative: for $v = (v_1, v_2)$, $\partial_v f(0,0) = \lim_{t\to0} f(tv)/t$. Use homogeneity — $f(tv_1, tv_2) = t\,f(v_1,v_2)$ for $t > 0$ — to evaluate this.

> [!note]- Hint 4
> For Part 3, you should find $\partial_v f(0,0) = f(v_1, v_2) = v_1 v_2/\sqrt{v_1^2+v_2^2}$. Is this linear in $v$? Check: is $\partial_{2v} f = 2\,\partial_v f$? Is $\partial_{v+w}f = \partial_v f + \partial_w f$? Try $v = e_1$, $w = e_2$: then $\partial_v f = \partial_w f = 0$ but $\partial_{v+w}f = \partial_{(1,1)}f = 1/\sqrt2 \neq 0$. Non-additive — hence not the restriction of a linear map — hence $f$ is not differentiable.

---

# Solution

The function is positively homogeneous of degree $1$: it is linear along every ray from the origin, but the slope of that linearity depends on the ray. Differentiability would demand a *single* linear map governing all rays at once. The partials see only the two coordinate-axis rays, on which $f$ is flat, so they are zero — but the diagonal ray has a non-zero slope, and no linear map can be flat along the axes and tilted along the diagonal.

**Step 1: Both partial derivatives at the origin exist and equal $0$.**

$\partial_x f(0,0) = \partial_y f(0,0) = 0$.

> [!note]- Derivation
> Restrict $f$ to the $x$-axis: for $t \neq 0$, $f(t, 0) = (t \cdot 0)/\sqrt{t^2 + 0} = 0$, and $f(0,0) = 0$. So $f \equiv 0$ on the $x$-axis, and by the limit definition of the [[Def - Partial Derivatives and the Jacobian Matrix|partial derivative]],
> $$\partial_x f(0,0) = \lim_{t\to0}\frac{f(t,0) - f(0,0)}{t} = \lim_{t\to0}\frac{0 - 0}{t} = 0.$$
> By the symmetry $f(x,y) = f(y,x)$, also $f \equiv 0$ on the $y$-axis and $\partial_y f(0,0) = 0$. Both partials exist. The array of partials is the zero row vector, so *if* $f$ were differentiable its derivative would be the zero linear map $L = 0$.

**Step 2: $f$ is continuous at the origin.**

$|f(x,y)| \le \tfrac12\sqrt{x^2+y^2} \to 0$, so $f(x,y) \to 0 = f(0,0)$.

> [!note]- Derivation
> For all real $x, y$, expanding $(|x| - |y|)^2 \ge 0$ gives $2|x||y| \le x^2 + y^2$, i.e. $|xy| \le \tfrac12(x^2+y^2)$. Hence for $(x,y) \neq (0,0)$,
> $$|f(x,y)| = \frac{|xy|}{\sqrt{x^2+y^2}} \le \frac{\tfrac12(x^2+y^2)}{\sqrt{x^2+y^2}} = \tfrac12\sqrt{x^2+y^2} = \tfrac12|h|,$$
> writing $h = (x,y)$. As $(x,y) \to (0,0)$, $|h| \to 0$, so $|f(x,y)| \to 0 = f(0,0)$. Therefore $f$ is continuous at the origin. (Consequently the discontinuity obstruction of [[Thm - Differentiability Implies Continuity]] is unavailable — non-differentiability must be shown by a finer argument.)

**Step 3: The directional derivative $\partial_v f(0,0)$ exists for every $v$ but is not linear in $v$.**

$\partial_v f(0,0) = v_1 v_2/\sqrt{v_1^2+v_2^2}$, which is not additive in $v$.

> [!note]- Derivation
> Fix a direction $v = (v_1, v_2) \neq 0$. By the definition of the [[Def - Directional Derivative and the Gradient|directional derivative]] and the fact that $f$ is positively homogeneous of degree $1$ — for $t > 0$, $f(tv_1, tv_2) = (t^2 v_1 v_2)/\sqrt{t^2(v_1^2+v_2^2)} = (t^2 v_1 v_2)/(t\sqrt{v_1^2+v_2^2}) = t\,f(v_1,v_2)$ —
> $$\partial_v f(0,0) = \lim_{t\to0}\frac{f(tv) - f(0,0)}{t} = \lim_{t\to0}\frac{t\,f(v_1,v_2)}{t} = f(v_1, v_2) = \frac{v_1 v_2}{\sqrt{v_1^2+v_2^2}}.$$
> (For $t < 0$ the same computation holds since $f$ is even under $v \mapsto -v$ in a way that makes the one-sided limits agree; in any case the limit exists.) So the directional derivative exists in **every** direction.
>
> But $v \mapsto \partial_v f(0,0)$ is **not linear**. Take $v = e_1 = (1,0)$ and $w = e_2 = (0,1)$:
> $$\partial_{e_1} f(0,0) = \frac{1\cdot0}{\sqrt{1}} = 0, \qquad \partial_{e_2} f(0,0) = 0, \qquad \partial_{e_1+e_2} f(0,0) = \partial_{(1,1)}f(0,0) = \frac{1\cdot1}{\sqrt{2}} = \frac{1}{\sqrt2}.$$
> Linearity would require $\partial_{e_1+e_2}f = \partial_{e_1}f + \partial_{e_2}f = 0 + 0 = 0$, but $\partial_{e_1+e_2}f = 1/\sqrt2 \neq 0$. So $v \mapsto \partial_v f(0,0)$ is not additive, hence not linear.

**Step 4: $f$ is not differentiable at the origin.**

> [!note]- Derivation
> If $f$ were [[Def - The Total Derivative and Differentiability|differentiable]] at the origin, then for every direction $v$ the directional derivative would satisfy $\partial_v f(0,0) = Df_{(0,0)}(v)$, and $Df_{(0,0)}$ being a linear map, $v \mapsto \partial_v f(0,0)$ would be linear. Step 3 shows it is not. Contradiction; $f$ is not differentiable at the origin.
>
> *Independent confirmation via the $o(|h|)$ limit.* By Step 1 the only candidate is $L = 0$, so differentiability means $|f(h) - f(0,0) - L(h)|/|h| = |f(h)|/|h| \to 0$. Test along the diagonal $h = (t,t)$, $t > 0$:
> $$\frac{|f(t,t)|}{|h|} = \frac{1}{|h|}\cdot\frac{t\cdot t}{\sqrt{t^2+t^2}} = \frac{1}{t\sqrt2}\cdot\frac{t^2}{t\sqrt2} = \frac{t^2}{2t^2} = \frac12.$$
> The ratio is constantly $\tfrac12$ along the diagonal, so it does not tend to $0$ as $h \to 0$. The defining limit fails; $f$ is not differentiable.

> [!note]- Complete formal solution
> **Claim.** $f$ has both partials at the origin and is continuous there, yet is not differentiable there.
>
> *Partials.* $f(t,0) = 0 = f(0,t)$ for all $t$, so $\partial_x f(0,0) = \lim_{t\to0}(0-0)/t = 0$ and likewise $\partial_y f(0,0) = 0$. The only candidate derivative is $L = 0$.
>
> *Continuity.* From $|xy| \le \tfrac12(x^2+y^2)$, for $(x,y)\neq0$, $|f(x,y)| = |xy|/\sqrt{x^2+y^2} \le \tfrac12\sqrt{x^2+y^2} \to 0$, so $f$ is continuous at the origin.
>
> *Non-differentiability.* $f$ is positively homogeneous of degree $1$: $f(tv) = t f(v)$ for $t > 0$. Hence the directional derivative $\partial_v f(0,0) = \lim_{t\to0} f(tv)/t = f(v) = v_1 v_2/\sqrt{v_1^2+v_2^2}$ exists for every $v$. With $v = e_1$, $w = e_2$: $\partial_v f(0,0) = \partial_w f(0,0) = 0$ but $\partial_{v+w}f(0,0) = 1/\sqrt2 \neq 0$, so $v \mapsto \partial_v f(0,0)$ is not linear. Differentiability would force it to equal the linear map $Df_{(0,0)}$, a contradiction. (Equivalently, along $h = (t,t)$ the ratio $|f(h)|/|h| = \tfrac12$ does not tend to $0$.) Therefore $f$ is not differentiable at the origin. $\blacksquare$

---

# Key Takeaways

**The existence of all partial derivatives is the weakest regularity condition and does not even interact with continuity, let alone differentiability.** This exercise pins down the lower gap of the regularity ladder, and the lesson generalises into a permanent warning. Partial derivatives are computed by freezing all variables but one, so they only probe $f$ along the $n$ coordinate axes — a set of measure zero, $n$ one-dimensional slices through an $n$-dimensional domain. Anything $f$ does *off* the axes is completely invisible to the partials. A function can therefore have all $n$ partials and be discontinuous (the textbook $xy/(x^2+y^2)$), or — as here — be continuous and still not differentiable. The operational consequence: when a problem hands you "all partials exist", you have been given almost nothing. You may write down the candidate Jacobian, but you have no licence to call it the derivative. Differentiability is a separate question requiring either [[Thm - Continuous Partials Imply Differentiability]] (continuity of the partials) or a direct check.

**Degree-$1$ positive homogeneity is the precise danger zone for differentiability at the origin.** A function with $f(tx) = t f(x)$ for $t > 0$ is linear along every ray, and that is exactly enough to make it look differentiable while not being so. The candidate derivative, if it exists, must be $L = 0$ unless $f$ is globally linear — because along a ray $f(tv) = t f(v)$ vanishes to order *exactly* one, and the $o(|h|)$ condition demands vanishing *faster* than order one. So a degree-$1$ homogeneous function is differentiable at the origin if and only if it is the restriction of a linear map. This is a reusable diagnostic: when you meet a function homogeneous of degree $1$, do not test differentiability by computing partials — ask directly whether the function is linear. If the ray-slope $f(v)/|v|$ depends on the direction $v$, it is not, and the function is not differentiable. The same principle, with the threshold shifted, says degree-$\lambda$ homogeneous functions with $\lambda > 1$ are automatically differentiable at the origin (they vanish to order $> 1$) and those with $\lambda < 1$ are typically not even continuous there.

**Choose the obstruction by its cost: discontinuity first, non-linear directional derivative second, the raw $o(|h|)$ limit last.** Proving non-differentiability is not one technique but a hierarchy, and the skill is starting at the cheap end. The cheapest certificate is *discontinuity*: by [[Thm - Differentiability Implies Continuity]], a function discontinuous at a point cannot be differentiable there, and this is a one-line argument. When the function is continuous — as here — that route is closed and you climb to the next: compute the directional derivative in a general direction and test whether it is *linear in the direction*, since differentiability forces $\partial_v f = Df(v)$ to be linear. A single failure of additivity, like $\partial_{e_1+e_2}f \neq \partial_{e_1}f + \partial_{e_2}f$, finishes the proof. Only if even that test passes — if all directional derivatives exist and assemble linearly into the candidate $L$ — do you descend to the raw definition and hunt for a path along which $|f(h)-L(h)|/|h|$ stays away from zero. Always start cheap; the diagonal-path computation is a last resort, not a first move.
