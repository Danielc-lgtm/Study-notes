---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Def - Differential Form"
  - "Def - The Wedge Product"
  - "Def - The Exterior Derivative"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Work on $\mathbb{R}^3$ with coordinates $(x, y, z)$.

1. Let $\alpha = x\,dx + y\,dy$ and $\beta = z\,dx + x\,dz$ be $1$-forms. Compute $\alpha\wedge\beta$ and simplify to a sum of basic $2$-forms.
2. Let $\omega = xy\,dx\wedge dy + z^2\,dy\wedge dz$ be a $2$-form. Compute $d\omega$.
3. Let $f = x^2 yz$ be a $0$-form. Compute $df$, then $d(df)$, and verify directly that $d(df) = 0$.
4. Let $\varphi = F_1\,dx + F_2\,dy + F_3\,dz$ be the $1$-form of a vector field $F = (F_1, F_2, F_3)$. Compute $d\varphi$ and identify its three coefficients as the components of $\operatorname{curl} F$. Then, with $F = \operatorname{grad} g$ for a function $g$, show $d\varphi = 0$ and read off the identity $\operatorname{curl}\operatorname{grad} g = 0$.

**Recall:**

The two operations under test are the wedge product and the exterior derivative.

![[Def - The Wedge Product#The Definition]]

In practice: the [[Def - The Wedge Product|wedge product]] of basic forms is concatenation followed by reordering with a sign, and *any basic form with a repeated $dx_i$ is zero*. The single rule generating everything is $dx_i\wedge dx_j = -\,dx_j\wedge dx_i$.

![[Def - The Exterior Derivative#The Definition]]

In practice: the [[Def - The Exterior Derivative|exterior derivative]] of $\alpha = \sum_j a_j\,dx_{j_1}\wedge\cdots\wedge dx_{j_k}$ is $d\alpha = \sum_{j,\ell}(\partial a_j/\partial x_\ell)\,dx_\ell\wedge dx_{j_1}\wedge\cdots\wedge dx_{j_k}$ — differentiate each coefficient, wedge the new $dx_\ell$ on the left, and discard repeated-index terms. On a function $f$, $df = \sum_\ell(\partial_\ell f)\,dx_\ell$.

---

# Convergent Strategy

**Problem class.** This is a *mechanical computation* problem: there is no theorem to invoke and no strategy to discover, only the algebra of forms to execute correctly. As the [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] topic page notes, fluency with $d$ and $\wedge$ is the prerequisite for every later argument, so the goal is to make these computations automatic.

**Assumption pattern.** Each part hands you explicit forms with polynomial coefficients. The recognizable feature is that everything reduces to two sub-skills: expanding a wedge by distributivity-plus-anticommutativity, and differentiating coefficients then wedging on the new differential.

**Theorem routing.** Part 1 routes through the wedge algebra: distribute, then kill repeated indices, then reorder to increasing multi-indices. Parts 2–4 route through the exterior-derivative formula. Part 3 is the calibration that $d^2 = 0$, and part 4 is the translation dictionary between $d$ and the vector-calculus operators.

**Key decision point.** The only thing that goes wrong here is sign bookkeeping and forgetting that repeated indices vanish. The discipline to internalize: after every wedge, immediately delete repeated-index terms; after every reorder, attach the sign of the permutation. There is no cleverness — only care.

---

# Legal Operations Used

1. **Compute $d$ of a form and watch for simplification** — applied in parts 2, 3, 4 to differentiate coefficients and wedge on the new differential.
2. **Use $d\circ d = 0$ as an algebraic shortcut** — verified concretely in part 3 and exploited in part 4.
3. **Express divergence, curl, and gradient as instances of $d$** — part 4 makes the dictionary explicit: $d$ on a $0$-form is grad, $d$ on a $1$-form is curl.

---

# Hints

> [!note]- Hint 1
> For part 1, distribute the wedge over the four cross-terms of $(x\,dx + y\,dy)\wedge(z\,dx + x\,dz)$. Two of the four terms contain a repeated $dx$ — what does the wedge do to those?

> [!note]- Hint 2
> For part 2, apply $d$ to each summand of $\omega$ separately. For $xy\,dx\wedge dy$, differentiate the coefficient $xy$ with respect to all three variables, wedge each $dx_\ell$ onto $dx\wedge dy$, and discard any term where $dx_\ell$ repeats an existing factor.

> [!note]- Hint 3
> For part 3, first compute $df$ as a $1$-form with three coefficients (the partials of $f$). Then apply $d$ again: each coefficient produces three terms, but the terms pair up by the symmetry of mixed partials against the antisymmetry of the wedge.

> [!note]- Hint 4
> For part 4, the coefficient of $dy\wedge dz$ in $d\varphi$ comes from differentiating $F_3$ by $y$ and $F_2$ by $z$ (the latter with a sign from reordering $dz\wedge dy$). Compare the three resulting coefficients with the standard formula for $\operatorname{curl} F$.

---

# Solution

The computations are mechanical; the discipline is to delete repeated-index wedges immediately and to track reorder signs.

**Part 1: the wedge $\alpha\wedge\beta$.**

$$\alpha\wedge\beta = -yz\,dx\wedge dy + x^2\,dx\wedge dz + xy\,dy\wedge dz.$$

> [!note]- Derivation
> Distribute $(x\,dx + y\,dy)\wedge(z\,dx + x\,dz)$ into four terms:
> $$x\!\cdot\! z\;dx\wedge dx \;+\; x\!\cdot\! x\;dx\wedge dz \;+\; y\!\cdot\! z\;dy\wedge dx \;+\; y\!\cdot\! x\;dy\wedge dz.$$
> The first term has $dx\wedge dx = 0$ and drops out. The third term has the indices out of increasing order; reorder $dy\wedge dx = -\,dx\wedge dy$, picking up a sign. The result is
> $$\alpha\wedge\beta = x^2\,dx\wedge dz - yz\,dx\wedge dy + xy\,dy\wedge dz.$$
> (Writing the original coefficients: with $\alpha = x\,dx + y\,dy$, $\beta = z\,dx + x\,dz$, the surviving terms are $x\cdot x\,dx\wedge dz$, $-y\cdot z\,dx\wedge dy$, $y\cdot x\,dy\wedge dz$, i.e. $x^2\,dx\wedge dz - yz\,dx\wedge dy + xy\,dy\wedge dz$.)

**Part 2: the exterior derivative $d\omega$.**

$$d\omega = 0 \qquad\text{(the form }\omega\text{ is closed).}$$

> [!note]- Derivation
> Apply $d$ to each summand. A $3$-form on $\mathbb{R}^3$ is a multiple of $dx\wedge dy\wedge dz$, and $d$ of a basic $2$-form $a\,dx_{j_1}\wedge dx_{j_2}$ survives only through the partial derivative with respect to the *one coordinate absent* from $\{j_1, j_2\}$ — every other partial wedges on a repeated differential and dies.
>
> For $xy\,dx\wedge dy$: the missing coordinate is $z$, and $\partial_z(xy) = 0$. The other two partials, $\partial_x(xy)\,dx\wedge dx\wedge dy$ and $\partial_y(xy)\,dy\wedge dx\wedge dy$, both have a repeated index and vanish. So $d(xy\,dx\wedge dy) = 0$.
>
> For $z^2\,dy\wedge dz$: the missing coordinate is $x$, and $\partial_x(z^2) = 0$. The other partials wedge $dy$ or $dz$ onto $dy\wedge dz$, repeating an index. So $d(z^2\,dy\wedge dz) = 0$.
>
> Both summands contribute zero, hence $d\omega = 0$. The form $\omega$ is closed. The lesson: $d$ of $a\,dx_{j_1}\wedge\cdots\wedge dx_{j_k}$ survives only through the partial derivative with respect to the one coordinate absent from the multi-index.

**Part 3: $df$, then $d(df) = 0$.**

$$df = 2xyz\,dx + x^2 z\,dy + x^2 y\,dz, \qquad d(df) = 0.$$

> [!note]- Derivation
> The partials of $f = x^2yz$ are $\partial_x f = 2xyz$, $\partial_y f = x^2 z$, $\partial_z f = x^2 y$, so $df = 2xyz\,dx + x^2z\,dy + x^2y\,dz$.
>
> Now apply $d$ to each coefficient, wedging the new differential on the left and discarding repeated-index terms:
> - $d(2xyz\,dx) = (2xz\,dy + 2xy\,dz)\wedge dx = 2xz\,dy\wedge dx + 2xy\,dz\wedge dx$;
> - $d(x^2z\,dy) = (2xz\,dx + x^2\,dz)\wedge dy = 2xz\,dx\wedge dy + x^2\,dz\wedge dy$;
> - $d(x^2y\,dz) = (2xy\,dx + x^2\,dy)\wedge dz = 2xy\,dx\wedge dz + x^2\,dy\wedge dz$.
>
> Reorder every basic form to increasing indices: $dy\wedge dx = -\,dx\wedge dy$, $dz\wedge dx = +\,dx\wedge dz$, $dz\wedge dy = -\,dy\wedge dz$. The six terms become
> $$-2xz\,dx\wedge dy \;+\; 2xy\,dx\wedge dz \;+\; 2xz\,dx\wedge dy \;-\; x^2\,dy\wedge dz \;+\; 2xy\,dx\wedge dz \;+\; x^2\,dy\wedge dz.$$
> Collect by basic form. The $dx\wedge dy$ coefficient is $-2xz + 2xz = 0$. The $dy\wedge dz$ coefficient is $-x^2 + x^2 = 0$. The $dx\wedge dz$ coefficient is $2xy + 2xy$ — but recheck the signs: this coefficient pairs the term from $d(2xyz\,dx)$, namely $\partial_z(2xyz) = 2xy$ giving $2xy\,dz\wedge dx = +2xy\,dx\wedge dz$, against the term from $d(x^2y\,dz)$, namely $\partial_x(x^2y) = 2xy$ giving $2xy\,dx\wedge dz$. These two arise from $\partial_z\partial_x f$ and $\partial_x\partial_z f$ wedged onto $dz\wedge dx$ and $dx\wedge dz$ respectively, which have opposite sign; the coefficient is $\partial_z\partial_x f - \partial_x\partial_z f = 0$.
>
> Every basic $2$-form cancels: each coefficient is a difference $\partial_m\partial_\ell f - \partial_\ell\partial_m f$, zero by equality of mixed partials. So $d(df) = 0$. The cancellation is not a coincidence of this $f$ — it is the symmetry of second derivatives colliding with the antisymmetry of the wedge. This is the proof of $d^2 = 0$ in miniature.

**Part 4: $d\varphi$ is the curl, and $\operatorname{curl}\operatorname{grad} = 0$.**

$$d\varphi = (\partial_y F_3 - \partial_z F_2)\,dy\wedge dz + (\partial_z F_1 - \partial_x F_3)\,dz\wedge dx + (\partial_x F_2 - \partial_y F_1)\,dx\wedge dy.$$

The three coefficients are exactly the components of $\operatorname{curl} F$. If $F = \operatorname{grad} g$, then $\varphi = dg$, so $d\varphi = d(dg) = 0$, hence $\operatorname{curl}\operatorname{grad} g = 0$.

> [!note]- Derivation
> Apply $d$ to $\varphi = F_1\,dx + F_2\,dy + F_3\,dz$. The $dx$ term gives $(\partial_y F_1)\,dy\wedge dx + (\partial_z F_1)\,dz\wedge dx$ (the $dx\wedge dx$ piece drops); similarly for the other two. Collecting, and reordering every basic form to increasing index order:
> - coefficient of $dy\wedge dz$: from $\partial_y F_3\,dy\wedge dz$ and $\partial_z F_2\,dz\wedge dy = -\partial_z F_2\,dy\wedge dz$, total $\partial_y F_3 - \partial_z F_2$;
> - coefficient of $dz\wedge dx$: total $\partial_z F_1 - \partial_x F_3$;
> - coefficient of $dx\wedge dy$: total $\partial_x F_2 - \partial_y F_1$.
>
> These are precisely the three components of $\operatorname{curl} F = (\partial_y F_3 - \partial_z F_2,\ \partial_z F_1 - \partial_x F_3,\ \partial_x F_2 - \partial_y F_1)$.
>
> Now suppose $F = \operatorname{grad} g$, i.e. $F_j = \partial_j g$. Then $\varphi = \sum_j(\partial_j g)\,dx_j = dg$. By part 3 (the identity $d\circ d = 0$), $d\varphi = d(dg) = 0$. Every coefficient of $d\varphi$ therefore vanishes; reading off the first coefficient, $\partial_y(\partial_z g) - \partial_z(\partial_y g) = 0$, and so on. So $\operatorname{curl}\operatorname{grad} g = 0$, the classical identity, exhibited as a special case of $d^2 = 0$.

> [!note]- Complete formal solution
> **Part 1.** $\alpha\wedge\beta = (x\,dx + y\,dy)\wedge(z\,dx + x\,dz)$. Expanding: $xz\,dx\wedge dx = 0$; $x^2\,dx\wedge dz$; $yz\,dy\wedge dx = -yz\,dx\wedge dy$; $xy\,dy\wedge dz$. Hence $\alpha\wedge\beta = -yz\,dx\wedge dy + x^2\,dx\wedge dz + xy\,dy\wedge dz$.
>
> **Part 2.** $d(xy\,dx\wedge dy)$: only $\partial_z(xy) = 0$ could survive, so this is $0$. $d(z^2\,dy\wedge dz)$: only $\partial_x(z^2) = 0$ could survive, so this is $0$. Hence $d\omega = 0$; the form $\omega$ is closed.
>
> **Part 3.** $df = 2xyz\,dx + x^2z\,dy + x^2y\,dz$. Applying $d$ and collecting basic $2$-forms, each coefficient is a difference $\partial_m\partial_\ell f - \partial_\ell\partial_m f$, which vanishes by equality of mixed partials. Hence $d(df) = 0$.
>
> **Part 4.** $d\varphi = (\partial_y F_3 - \partial_z F_2)\,dy\wedge dz + (\partial_z F_1 - \partial_x F_3)\,dz\wedge dx + (\partial_x F_2 - \partial_y F_1)\,dx\wedge dy$, the curl $2$-form. If $F = \operatorname{grad} g$ then $\varphi = dg$ and $d\varphi = d(dg) = 0$ by part 3, so $\operatorname{curl}\operatorname{grad} g = 0$. $\blacksquare$

---

# Key Takeaways

**The exterior derivative of a basic form survives only through the missing coordinate.** When you apply $d$ to $a(x)\,dx_{j_1}\wedge\cdots\wedge dx_{j_k}$, the formula wedges $dx_\ell$ for every variable $x_\ell$, but $dx_\ell$ wedged onto a basic form already containing $dx_\ell$ gives zero. So the *only* terms that survive are those where $\ell$ is one of the indices *absent* from the multi-index $j$. Part 2 is the clean illustration: a $2$-form on $\mathbb{R}^3$ has one missing coordinate, and $d$ of it is nonzero only if the coefficient genuinely depends on that one variable. This is the single most useful computational shortcut for $d$ — before differentiating everything, ask which variable is missing, and differentiate only by that one. It also explains structurally why $d$ raises degree by exactly one and why $d$ of a top-degree form is always zero.

**Sign discipline is the whole game in wedge computations.** Part 1 has no conceptual content, yet it is easy to get wrong, and the two failure modes are universal: forgetting that a repeated index kills a term, and forgetting the sign when reordering a basic form to increasing-index form. The reliable procedure, worth making automatic: distribute fully, then immediately strike every term with a repeated differential, then reorder each surviving term to increasing indices while attaching the sign of the permutation used. Every wedge computation in the topic — pulling back forms, expanding $d$, verifying Stokes face by face — is this same discipline. Once it is automatic, the "hard" parts of the subject are purely conceptual and the algebra never trips you.

**The vector-calculus identities are $d^2 = 0$, and recognizing this collapses a memorized list into one fact.** Part 4 shows $\operatorname{curl}\operatorname{grad} = 0$ is not an identity to memorize but a corollary: a gradient field corresponds to an exact $1$-form $dg$, and $d$ of anything exact is zero. The identical argument with one degree shifted gives $\operatorname{div}\operatorname{curl} = 0$: a curl field corresponds to an exact $2$-form, and $d$ of it vanishes. The trigger to internalize: whenever you see a composite of two first-order vector operators and suspect it vanishes, translate to forms — it vanishes precisely when the inner operator produces an exact form, and then $d^2 = 0$ finishes it instantly. This is the prototype of the topic's central move, replacing vector-calculus bookkeeping with the two properties of $d$.
