---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Thm - The Inverse Function Theorem"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

The [[Thm - The Inverse Function Theorem|inverse function theorem]] gives a local inverse *only* where the derivative is invertible. This exercise probes what happens at points where the hypothesis fails.

1. For $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^3$: show $f'(0) = 0$, so the inverse function theorem does not apply at $0$. Is $f$ nevertheless invertible near $0$? Is the inverse smooth?
2. For $f : \mathbb{R}^2 \to \mathbb{R}^2$, $f(x,y) = (x^2 - y^2,\ 2xy)$ (the complex squaring map $z \mapsto z^2$): compute $Jf$ and find every point where $\det Jf = 0$. At such a point, show $f$ is genuinely *not* injective on any neighbourhood.
3. For $F : \mathbb{R}^{2\times 2} \to \mathbb{R}^{2\times 2}$, $F(X) = X^2$: show $F$ *is* a local diffeomorphism near the identity $I$, but is *not* a local diffeomorphism near $A = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}$, and diagnose which hypothesis fails.

**Recall:**

The objects in play are the Jacobian matrix and the precise hypothesis of the inverse function theorem.

![[Thm - The Inverse Function Theorem#Statement]]

By the [[Thm - The Inverse Function Theorem|inverse function theorem]], a $C^1$ map $F$ between equal-dimensional Euclidean spaces is a local $C^1$-diffeomorphism near a point $p_0$ *provided* $DF(p_0)$ is invertible. When $DF(p_0)$ is *not* invertible — when $\det JF(p_0) = 0$ — the theorem says nothing, and one expects (and here verifies) that invertibility genuinely fails: the map may collapse a direction, fold, or branch. Note the theorem's condition is *sufficient*, not necessary: $x \mapsto x^3$ shows a map can be globally invertible even where the derivative vanishes, but the inverse then fails to be smooth.

---

# Convergent Strategy

**Problem class.** This is a *diagnostic* exercise on the boundary of the inverse function theorem's domain of applicability. The [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Problem-Solving Strategy|topic strategy]] notes that when $\det Jf = 0$ the theorem simply does not apply, and one should *expect and verify* that invertibility fails — typically by folding.

**Assumption pattern.** Each part presents a map at a point where the Jacobian determinant vanishes. The task is not to apply the theorem but to understand what its failure means: distinguish "theorem inapplicable" from "map genuinely non-invertible".

**Theorem routing.** There is no theorem to route *to*; the exercise routes *away* from the inverse function theorem. Part 1 shows the hypothesis is sufficient but not necessary. Part 2 shows that at a singular Jacobian a smooth map can be a genuine two-to-one fold. Part 3 contrasts a good point and a bad point of the same map.

**Key decision point.** The crux is the distinction the exercise is built to install: $\det Jf(p_0) = 0$ means the *inverse function theorem cannot be invoked*, which is *not* the same as "$f$ is not invertible". It can still be invertible (Part 1), or genuinely not (Parts 2, 3). When the hypothesis fails you must investigate the map directly — the theorem has nothing to say either way.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Check a Jacobian determinant to test the inverse function theorem's hypothesis.** Compute $\det Jf$ and locate its zero set; the theorem applies precisely off that set.

2. **Investigate the map directly where the hypothesis fails.** When $\det Jf(p_0) = 0$, examine $f$ near $p_0$ by hand — test injectivity, look for folds — since the theorem is silent.

---

# Hints

> [!note]- Hint 1
> For $f(x) = x^3$: $f'(x) = 3x^2$, so $f'(0) = 0$ — the inverse function theorem does not apply at $0$. But $x^3$ is strictly increasing, hence bijective. Its inverse is $x^{1/3}$. Is $x^{1/3}$ differentiable at $0$?

> [!note]- Hint 2
> For the squaring map $f(x,y) = (x^2-y^2, 2xy)$: $Jf = \begin{pmatrix} 2x & -2y \\ 2y & 2x\end{pmatrix}$, $\det Jf = 4(x^2+y^2)$. This vanishes only at the origin. To see non-injectivity near $0$: $f(-x,-y) = f(x,y)$.

> [!note]- Hint 3
> The map $z \mapsto z^2$ sends $z$ and $-z$ to the same point. In any neighbourhood of the origin there are pairs $\pm(x,y)$, both mapped to the same image — so $f$ is two-to-one near $0$ and cannot be injective there.

> [!note]- Hint 4
> For $F(X) = X^2$: the derivative is $DF(X)H = XH + HX$. At $X = I$, $DF(I)H = 2H$, invertible — local diffeomorphism. At $X = A = \operatorname{diag}(1,-1)$, both $A$ and $-A$ wait... compute $A^2 = I$; and $I^2 = I$. So both $A$ and $I$ square to $I$ — there are *distinct* square roots of $I$ arbitrarily... examine $DF(A)H = AH + HA$ and find $H \neq 0$ with $AH + HA = 0$.

---

# Solution

The inverse function theorem's hypothesis — invertible derivative — is *sufficient*, not necessary, and where it fails the theorem is simply silent. The three parts show the three things that can then happen: the map stays invertible but the inverse loses smoothness; the map folds and loses injectivity; or the derivative collapses a direction outright.

**Step 1: $x^3$ — invertible, but the inverse is not smooth.**

$f'(0) = 0$, so the inverse function theorem does not apply at $0$. Yet $f(x) = x^3$ is a bijection of $\mathbb{R}$; its inverse $f^{-1}(x) = x^{1/3}$ is continuous but **not differentiable at $0$**.

> [!note]- Derivation
> $f'(x) = 3x^2$, so $f'(0) = 0$ — the derivative at the origin is the zero map, not invertible. The [[Thm - The Inverse Function Theorem|inverse function theorem]] requires an invertible derivative, so it cannot be invoked at $0$.
>
> But $f(x) = x^3$ is *strictly increasing* on all of $\mathbb{R}$ (if $a < b$ then $a^3 < b^3$), hence injective, and it is surjective onto $\mathbb{R}$. So $f$ *is* globally invertible, with inverse $f^{-1}(x) = x^{1/3}$. This shows the inverse function theorem's hypothesis is **sufficient but not necessary**: a map can be invertible even where its derivative vanishes.
>
> What the failure of the hypothesis *does* cost is the *smoothness* of the inverse. The inverse $x^{1/3}$ has derivative $\tfrac13 x^{-2/3}$, which blows up as $x \to 0$ — $x^{1/3}$ has a vertical tangent at the origin and is not differentiable there. This is exactly what the inverse function theorem would have guaranteed (a $C^1$ inverse) had its hypothesis held: the conclusion "the inverse is smooth" fails precisely where the hypothesis "$f'$ invertible" fails. Geometrically, $f$ is *infinitely flat* at $0$ — it crushes a neighbourhood toward $0$ to third order — so undoing it stretches infinitely, and the stretch is the failure of differentiability.

**Step 2: The squaring map — a genuine fold, not injective.**

$Jf(x,y) = \begin{pmatrix} 2x & -2y \\ 2y & 2x\end{pmatrix}$ with $\det Jf = 4(x^2+y^2)$, vanishing only at the origin. There $f$ is **not injective on any neighbourhood**: $f(-x,-y) = f(x,y)$ always.

> [!note]- Derivation
> Differentiating $f_1 = x^2 - y^2$, $f_2 = 2xy$:
> $$Jf(x,y) = \begin{pmatrix} 2x & -2y \\ 2y & 2x\end{pmatrix}, \qquad \det Jf = (2x)(2x) - (-2y)(2y) = 4x^2 + 4y^2 = 4(x^2+y^2).$$
> This is nonzero everywhere *except* the origin, where it is $0$. So the [[Thm - The Inverse Function Theorem|inverse function theorem]] applies at every point but $(0,0)$, and at $(0,0)$ it is silent.
>
> At the origin the map is genuinely non-invertible. The map is the complex squaring $z \mapsto z^2$ (with $z = x + iy$), and $(-z)^2 = z^2$, that is,
> $$f(-x,-y) = \big((-x)^2-(-y)^2,\ 2(-x)(-y)\big) = (x^2-y^2,\ 2xy) = f(x,y).$$
> Every point and its negative have the same image. In *any* neighbourhood of the origin — however small — there are pairs of distinct points $(x,y)$ and $(-x,-y)$ that $f$ identifies, so $f$ is **two-to-one** near the origin and cannot be injective on any neighbourhood of it. The map *folds* the plane onto itself, doubling angles: it is a genuine branch point. The vanishing of $\det Jf$ at the origin is the analytic signature of this fold — the linearization $Df(0,0) = 0$ collapses the whole plane to a point, and the nonlinear map inherits a two-to-one branching.

**Step 3: Matrix squaring — a good point and a bad point.**

$F(X) = X^2$ has derivative $DF(X)H = XH + HX$. At $X = I$, $DF(I)H = 2H$ is invertible — $F$ is a local diffeomorphism near $I$. At $X = A = \operatorname{diag}(1,-1)$, $DF(A)$ is **not** invertible, so $F$ is not a local diffeomorphism near $A$.

> [!note]- Derivation
> The derivative of $F(X) = X^2$ is computed from $F(X + H) = (X+H)^2 = X^2 + XH + HX + H^2$; the linear-in-$H$ part is $DF(X)H = XH + HX$.
>
> *At $X = I$:* $DF(I)H = IH + HI = 2H$. This is the linear map $H \mapsto 2H$, which is invertible (inverse $H\mapsto\tfrac12 H$). By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $F$ is a local $C^\infty$-diffeomorphism from a neighbourhood of $I$ onto a neighbourhood of $F(I) = I$ — there is a smooth "matrix square root" defined near $I$.
>
> *At $X = A = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}$:* $DF(A)H = AH + HA$. We show this linear map has a nontrivial kernel, hence is not invertible. Take $H = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}$:
> $$AH = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}\begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}, \quad HA = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 0 & 0\end{pmatrix}.$$
> So $DF(A)H = AH + HA = \begin{pmatrix} 0 & 1\\0&0\end{pmatrix} + \begin{pmatrix} 0 & -1\\0&0\end{pmatrix} = 0$. A nonzero $H$ in the kernel means $DF(A)$ is *not injective*, hence not invertible. The hypothesis of the [[Thm - The Inverse Function Theorem|inverse function theorem]] fails at $A$, so it cannot certify a local inverse there.
>
> And indeed $F$ is genuinely badly behaved near $A$: both $A$ and $-A$ are square roots of $A^2 = I$, and $F(A) = A^2 = I = I^2 = F(I)$ — so $F$ maps the distinct points $A$ and $I$ to the same image $I$. More to the point, near $A$ the map $F$ fails to be injective in the direction of the kernel vector $H$ (the curve $t\mapsto A + tH$ has $F$ changing only to second order along it), so $F$ is not a diffeomorphism of any neighbourhood of $A$.

> [!note]- Complete formal solution
> *Part 1.* $f(x) = x^3$, $f'(x) = 3x^2$, $f'(0) = 0$: inverse function theorem inapplicable at $0$. But $x^3$ is strictly increasing, so bijective, with inverse $x^{1/3}$ — invertible. The inverse $x^{1/3}$ has derivative $\tfrac13 x^{-2/3} \to \infty$ as $x\to 0$, so it is not differentiable at $0$. The hypothesis is sufficient, not necessary; its failure costs smoothness of the inverse.
>
> *Part 2.* $f(x,y) = (x^2-y^2, 2xy)$, $Jf = \begin{pmatrix} 2x & -2y\\2y&2x\end{pmatrix}$, $\det Jf = 4(x^2+y^2) = 0$ only at the origin. There $f(-x,-y) = f(x,y)$, so $f$ is two-to-one on every neighbourhood of $0$ — not injective. The map is the fold $z\mapsto z^2$.
>
> *Part 3.* $F(X) = X^2$, $DF(X)H = XH + HX$. At $I$: $DF(I)H = 2H$, invertible — local diffeomorphism. At $A = \operatorname{diag}(1,-1)$: with $H = \begin{pmatrix}0&1\\0&0\end{pmatrix}$, $DF(A)H = AH + HA = 0$, so $DF(A)$ has nontrivial kernel and is not invertible — $F$ is not a local diffeomorphism near $A$. $\blacksquare$

---

# Key Takeaways

**A vanishing Jacobian determinant means the inverse function theorem is *inapplicable*, which is not the same as the map being non-invertible.** This is the precise logical point the exercise installs. The theorem's hypothesis "$Df$ invertible" is *sufficient* for a local diffeomorphism, not *necessary*. So when $\det Jf(p_0) = 0$, three things become possible and the theorem distinguishes none of them: the map may still be invertible but with a non-smooth inverse ($x^3$), or it may fold and lose injectivity (the squaring maps), or worse. The discipline is to never read "$\det Jf = 0$" as "$f$ not invertible" — read it as "the theorem says nothing; investigate $f$ directly". Conversely, never read "$\det Jf \neq 0$" as "$f$ globally invertible" — that is the local/global error of the companion exercise.

**A singular Jacobian is the analytic signature of a fold or branch point.** When $\det Jf(p_0) = 0$ the linearization $Df(p_0)$ collapses at least one direction — it has nontrivial kernel — and the nonlinear map typically inherits a *folding* behaviour along that direction: it ceases to be locally one-to-one. The squaring maps $x\mapsto x^3$, $z\mapsto z^2$, and $X\mapsto X^2$ all illustrate this: at the bad point the derivative degenerates and the map becomes many-to-one (a branch point of $z^2$ is exactly two-to-one). When you find $\det Jf = 0$ at a point, the productive next move is to look for the *kernel direction* of $Df$ and test injectivity along it — the kernel direction is where the fold happens.

**To diagnose failure, exhibit the kernel vector explicitly.** In Part 3 the cleanest proof that $F$ is not a local diffeomorphism near $A$ is to *produce* a nonzero matrix $H$ with $DF(A)H = 0$. A linear map with a nonzero kernel vector is provably non-injective, hence non-invertible, hence the inverse function theorem provably fails — no determinant computation needed in the abstract matrix setting. The general technique: when a derivative is suspected singular, do not just assert it; *write down* a nonzero vector it kills. This is both the most convincing proof and the most informative one, because the kernel vector *is* the direction along which the map degenerates.

**The smoothness of the inverse is exactly what the invertibility hypothesis buys.** Part 1 isolates this cleanly: $x^3$ is invertible despite $f'(0) = 0$, but its inverse $x^{1/3}$ is not differentiable at $0$. Had $f'(0)$ been invertible, the inverse function theorem would have guaranteed a $C^1$ — indeed $C^\infty$ — inverse. So the theorem's hypothesis is not really about *existence* of an inverse (continuity and strict monotonicity can give that); it is about the inverse being *as smooth as $f$*. When you see a map that is invertible but whose inverse has a vertical tangent, a cusp, or a corner, suspect that the derivative degenerated somewhere — the loss of smoothness in the inverse is the shadow of the lost invertibility hypothesis.
