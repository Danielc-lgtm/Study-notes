---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Sard's Theorem for Smooth Maps"
  - "Def - Regular and Critical Points"
  - "Def - Set of Measure Zero on a Manifold"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

We test [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] on three concrete maps, computing the critical set by hand and checking directly that the critical values form a Lebesgue-null set — exactly what Sard's theorem predicts.

**Part (a).** Let $f:\mathbb{R}^2\to\mathbb{R}^2$ be the map
$$f(x,y)=(x^2-y^2,\;2xy).$$
Find the set $\operatorname{Crit}(f)$ of critical points, the set $f(\operatorname{Crit}(f))$ of critical values, and verify that the critical values have Lebesgue measure zero in $\mathbb{R}^2$.

**Part (b).** Let $f:\mathbb{R}^2\to\mathbb{R}$ be the map
$$f(x,y)=x^3-3xy^2.$$
Find $\operatorname{Crit}(f)$ and $f(\operatorname{Crit}(f))$, and verify that the critical values have Lebesgue measure zero in $\mathbb{R}$.

**Part (c).** Let $f:\mathbb{R}\to\mathbb{R}^2$ be any smooth map. Show that *every* point of $\mathbb{R}$ is a critical point, so that the set of critical values coincides with the full image $f(\mathbb{R})$, and conclude from Sard's theorem that $f(\mathbb{R})$ has Lebesgue measure zero in $\mathbb{R}^2$. (This is the boundary case $(k+1)n>m$ of Sard's Step 5 with $k=0$, worked out in full in the companion exercise [[Ex - The Deeply Critical Set and Taylor Expansion]].)

**Recall:**

The objects in play are smooth maps between open subsets of Euclidean spaces, the Jacobian criterion for a critical point, Lebesgue-null sets, and Sard's theorem.

![[Thm - Sard's Theorem for Smooth Maps#Statement]]

To restate what we shall use: if $f:U\to\mathbb{R}^n$ is smooth on an open set $U\subseteq\mathbb{R}^m$, its **critical values** $f(\operatorname{Crit}(f))$ form a set of Lebesgue measure zero in $\mathbb{R}^n$. Here a point $x\in U$ is a [[Def - Regular and Critical Points|critical point]] when the differential $d_xf:\mathbb{R}^m\to\mathbb{R}^n$ fails to be surjective, and a **critical value** is the image of a critical point.

![[Def - Regular and Critical Points#The Definition]]

For a map $f:U\to\mathbb{R}^n$ with $U\subseteq\mathbb{R}^m$ open, the differential $d_xf$ is represented by the **Jacobian matrix**
$$Df(x)=\left(\frac{\partial f_i}{\partial x_j}(x)\right)_{\substack{1\le i\le n\\ 1\le j\le m}}\in\mathbb{R}^{n\times m},$$
and $d_xf$ is surjective if and only if $Df(x)$ has rank $n$. Thus $x$ is a critical point precisely when $\operatorname{rank}Df(x)<n$. In the two square cases below ($m=n$) this reads $\det Df(x)=0$; when the target is $\mathbb{R}$ ($n=1$) it reads $\nabla f(x)=0$; when $m<n$ it holds at *every* $x$, since a matrix with $m<n$ columns cannot have rank $n$.

![[Def - Set of Measure Zero on a Manifold#The Definition]]

A subset $S\subseteq\mathbb{R}^n$ has **Lebesgue measure zero** when for every $\varepsilon>0$ there is a countable family of open boxes $\{Q_i\}_{i\in\mathbb{N}}$ with $S\subseteq\bigcup_i Q_i$ and $\sum_i\operatorname{vol}(Q_i)<\varepsilon$ (see [[Def - Lebesgue Measure]]). Two facts we use: a finite set is null (cover its finitely many points by tiny boxes); and a countable union of null sets is null (split the budget $\varepsilon$ as $\sum_i\varepsilon/2^{i+1}$).

---

# Convergent Strategy

**Problem class.** These are *verification* problems: the general theorem ([[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]]) guarantees an outcome — critical values are null — and the task is to see the outcome explicitly for maps simple enough to compute the entire critical set by hand. The recognisable signature is that we are handed an *explicit* smooth map and asked about its critical values; the correct first move is always the same, namely to write down the Jacobian and solve $\operatorname{rank}Df(x)<n$.

**Assumption pattern.** Each part turns on the *shape* of the Jacobian. In Part (a) the map is square ($m=n=2$) and the criterion is $\det Df=0$; the special structure of $f$ (it is the complex squaring map $z\mapsto z^2$) makes the determinant a perfect sum of squares, so the critical set collapses to a single point. In Part (b) the target is one-dimensional ($n=1$) and the criterion is $\nabla f=0$; again the special structure ($f=\operatorname{Re}(z^3)$) forces the two gradient equations to have only the origin in common. In Part (c) the domain is *lower-dimensional* than the target ($m=1<2=n$), so the rank criterion is met vacuously at every point and there is nothing to solve — the content is entirely in the nullity conclusion.

**Theorem routing.** For Parts (a) and (b) we do not even need Sard's theorem to *prove* nullity, because the critical-value set turns out to be a single point, which is null by the elementary covering argument recalled above; Sard's theorem is the general statement these two computations *illustrate*. For Part (c) the critical-value set is a genuine curve, not a finite set, and here Sard's theorem does real work: [[Thm - Sard's Theorem for Smooth Maps|it]] asserts $f(\operatorname{Crit}(f))=f(\mathbb{R})$ is null once we have shown every point is critical. The route is: (i) compute $Df$; (ii) solve the rank-deficiency condition; (iii) evaluate $f$ on the critical set; (iv) certify the resulting set is null, by hand for (a),(b) and by citing Sard's theorem for (c).

**Key decision point.** The one genuinely non-mechanical move is *recognising the complex structure* behind the two polynomial maps. Writing $z=x+iy$, Part (a)'s map is $z\mapsto z^2$ and Part (b)'s is $z\mapsto\operatorname{Re}(z^3)$. This is not necessary — one can grind through the Jacobian algebra directly — but it explains at a glance *why* the critical set is so small: a holomorphic map $z\mapsto z^d$ has derivative $dz^{d-1}$, vanishing only at the origin, and the Cauchy–Riemann equations tie the real Jacobian determinant to $|dz^{d-1}|^2$, a sum of squares. Seeing this converts a computation into an explanation.

---

# Legal Operations Used

The moves below are the §10.2 operations for locating and certifying critical values; they will be numbered against [[Gauge Theory X — Fredholm Maps, Transversality, and Degree#Legal Operations|the topic page's Legal Operations]] once that page is assembled.

1. **Reduce "critical point" to a rank condition on the Jacobian.** A point $x$ is critical exactly when $\operatorname{rank}Df(x)<n$; write out $Df(x)$ and read off this condition as a system of equations in $x$. In the square case it is the single equation $\det Df(x)=0$; in the scalar-target case it is $\nabla f(x)=0$.

2. **Solve the rank-deficiency system explicitly.** Treat $\det Df(x)=0$ (or $\nabla f(x)=0$) as a system of polynomial equations and find its full solution set. Here each system has the origin as its only real solution, obtained by exhibiting the equations as sums of squares or by elementary elimination.

3. **Push the critical set forward by $f$.** Evaluate $f$ on $\operatorname{Crit}(f)$ to obtain $f(\operatorname{Crit}(f))$; the critical *values* are what Sard's theorem constrains, not the critical *points*.

4. **Certify a finite set is null by direct covering.** A single point (or any finite set) in $\mathbb{R}^n$ is covered by finitely many boxes of arbitrarily small total volume, hence is Lebesgue-null; no theorem beyond the definition is needed.

5. **Invoke Sard's theorem when the critical-value set is not manifestly small.** When $\operatorname{Crit}(f)$ is large — as in Part (c), where it is all of $\mathbb{R}$ — read the nullity of $f(\operatorname{Crit}(f))$ off [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] rather than by an ad hoc cover.

6. **Detect an underdetermined differential from dimensions alone.** When $m<n$, the Jacobian $Df(x)\in\mathbb{R}^{n\times m}$ has fewer columns than $n$, so its rank is at most $m<n$ and every point is critical; this needs no computation, only the shapes of the spaces.

---

# Hints

> [!note]- Hint 1
> In each part, begin by writing down the Jacobian matrix $Df(x)$ and asking when it *fails* to have full rank $n$. Parts (a) and (b) reduce to a single polynomial equation; part (c) needs no computation at all — look at the size of the matrix.

> [!note]- Hint 2
> For Part (a), the map is square, so "critical" means $\det Df=0$. Compute the $2\times2$ determinant of $Df(x,y)=\begin{pmatrix}2x&-2y\\2y&2x\end{pmatrix}$; you will find it is a sum of two squares. When is a sum of two real squares zero?

> [!note]- Hint 3
> For Part (b), the target is $\mathbb{R}$, so "critical" means the gradient vanishes: $\partial_xf=\partial_yf=0$. From $\partial_yf=-6xy=0$ you get $x=0$ or $y=0$; substitute each into $\partial_xf=3x^2-3y^2=0$ and see that only the origin survives both.

> [!note]- Hint 4
> For Part (c), a linear map $\mathbb{R}\to\mathbb{R}^2$ has rank at most $1$, so $d_xf$ is never onto $\mathbb{R}^2$: every point is critical, and $f(\operatorname{Crit}f)=f(\mathbb{R})$. Now apply Sard's theorem directly. If you want to see *why* the image of a line is thin, recall the estimate of [[Ex - The Deeply Critical Set and Taylor Expansion]]: a smooth curve, restricted to a bounded interval, is Lipschitz, and a Lipschitz image of a $1$-dimensional set cannot fill area.

---

# Solution

The plan is uniform. For each map we form the Jacobian, solve the rank-deficiency condition to find the critical points, evaluate the map there to find the critical values, and certify that the value set is Lebesgue-null. Parts (a) and (b) yield a single critical value, null by inspection; part (c) yields a whole curve, null by Sard's theorem. Throughout, $z=x+iy$ is the complex coordinate, useful for seeing the answers but never required.

**Step 1: Part (a) — critical points of $f(x,y)=(x^2-y^2,2xy)$.**

The Jacobian is $Df=\begin{pmatrix}2x&-2y\\2y&2x\end{pmatrix}$ with $\det Df=4(x^2+y^2)$, which vanishes only at the origin; so $\operatorname{Crit}(f)=\{(0,0)\}$.

> [!note]- Derivation
> Write $f=(f_1,f_2)$ with $f_1(x,y)=x^2-y^2$ and $f_2(x,y)=2xy$. Differentiating,
> $$\frac{\partial f_1}{\partial x}=2x,\quad\frac{\partial f_1}{\partial y}=-2y,\quad\frac{\partial f_2}{\partial x}=2y,\quad\frac{\partial f_2}{\partial y}=2x\qquad\text{(elementary partial differentiation of polynomials).}$$
> Hence the Jacobian matrix is
> $$Df(x,y)=\begin{pmatrix}2x&-2y\\[2pt]2y&2x\end{pmatrix}\qquad\text{(assembling the partials, rows indexed by }f_1,f_2\text{).}$$
> Since $m=n=2$, the differential $d_{(x,y)}f$ is surjective if and only if $Df(x,y)$ is invertible, i.e. $\det Df(x,y)\ne0$ (operation 1). Computing the determinant,
> $$\det Df(x,y)=(2x)(2x)-(-2y)(2y)=4x^2+4y^2=4(x^2+y^2)\qquad\text{(}2\times2\text{ determinant).}$$
> A sum of two real squares vanishes if and only if both vanish, so $\det Df(x,y)=0\iff x=0\text{ and }y=0$ (operation 2). Therefore
> $$\operatorname{Crit}(f)=\{(x,y):\det Df(x,y)=0\}=\{(0,0)\}.$$
> The complex-analytic reason: $f(x,y)=(x^2-y^2,2xy)$ is the real form of $z\mapsto z^2$, whose complex derivative is $2z$; the real Jacobian determinant of a holomorphic map equals $|2z|^2=4|z|^2=4(x^2+y^2)$, vanishing only at $z=0$.

**Step 2: Part (a) — critical values and their nullity.**

Evaluating $f$ at the unique critical point gives $f(0,0)=(0,0)$, so $f(\operatorname{Crit}(f))=\{(0,0)\}$, a single point, which has Lebesgue measure zero in $\mathbb{R}^2$.

> [!note]- Derivation
> By Step 1, $\operatorname{Crit}(f)=\{(0,0)\}$. Pushing forward by $f$ (operation 3),
> $$f(\operatorname{Crit}(f))=\{f(0,0)\}=\{(0^2-0^2,\,2\cdot0\cdot0)\}=\{(0,0)\}\qquad\text{(evaluating }f\text{ at the origin).}$$
> This is a single point of $\mathbb{R}^2$. To certify it is null (operation 4): fix $\varepsilon>0$ and cover $(0,0)$ by the open square $Q=(-\delta,\delta)^2$ with $\delta=\tfrac14\sqrt{\varepsilon}$, so that $\operatorname{vol}(Q)=(2\delta)^2=\varepsilon/4<\varepsilon$ (area of a square). Thus for every $\varepsilon>0$ the point is contained in one box of volume $<\varepsilon$, so it has Lebesgue measure zero by the definition recalled above.
> This is consistent with [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]], which guarantees the critical values are null; here the null set is as small as possible, a single point. Every point of $\mathbb{R}^2\setminus\{(0,0)\}$ is a regular value, and indeed over each such value $f$ is a local diffeomorphism (the two square roots of a non-zero complex number).

**Step 3: Part (b) — critical points of $f(x,y)=x^3-3xy^2$.**

Here $n=1$, so criticality is $\nabla f=0$; the equations $3x^2-3y^2=0$ and $-6xy=0$ have only the origin as common solution, so $\operatorname{Crit}(f)=\{(0,0)\}$.

> [!note]- Derivation
> Differentiating the scalar function $f(x,y)=x^3-3xy^2$,
> $$\frac{\partial f}{\partial x}=3x^2-3y^2,\qquad\frac{\partial f}{\partial y}=-6xy\qquad\text{(polynomial differentiation).}$$
> Since the target is $\mathbb{R}$ ($n=1$), the differential $d_{(x,y)}f=\nabla f(x,y)$ is surjective onto $\mathbb{R}$ if and only if it is non-zero; hence $(x,y)$ is critical exactly when $\nabla f(x,y)=0$ (operation 1), that is,
> $$3x^2-3y^2=0\qquad\text{and}\qquad -6xy=0.$$
> From the second equation, $xy=0$, so $x=0$ or $y=0$ (a product of reals is zero iff a factor is; operation 2).
>
> **Case $x=0$.** The first equation becomes $-3y^2=0$, forcing $y=0$.
>
> **Case $y=0$.** The first equation becomes $3x^2=0$, forcing $x=0$.
>
> The two cases are exhaustive (they are the two ways $xy=0$ can hold) and each yields $(x,y)=(0,0)$. Therefore $\operatorname{Crit}(f)=\{(0,0)\}$. The complex reason: $x^3-3xy^2=\operatorname{Re}\big((x+iy)^3\big)=\operatorname{Re}(z^3)$; its gradient is the real form of the complex number $3z^2$ up to conjugation, and $3z^2=0$ only at $z=0$.

**Step 4: Part (b) — critical values and their nullity.**

Evaluating gives $f(0,0)=0$, so $f(\operatorname{Crit}(f))=\{0\}\subset\mathbb{R}$, a single point of the real line, hence Lebesgue-null in $\mathbb{R}$.

> [!note]- Derivation
> By Step 3, $\operatorname{Crit}(f)=\{(0,0)\}$, and (operation 3)
> $$f(\operatorname{Crit}(f))=\{f(0,0)\}=\{0^3-3\cdot0\cdot0^2\}=\{0\}\qquad\text{(evaluating }f\text{ at the origin).}$$
> A single point $\{0\}\subset\mathbb{R}$ is Lebesgue-null (operation 4): for $\varepsilon>0$ cover it by the interval $(-\varepsilon/4,\varepsilon/4)$ of length $\varepsilon/2<\varepsilon$ (length of an interval). This agrees with [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] for the target $\mathbb{R}$: the critical values are null, and here the only critical value is $0$. Every non-zero real number is a regular value, with $f^{-1}(c)$ a smooth curve — the union of three rays through the origin's angular directions of $\operatorname{Re}(z^3)=c$.

**Step 5: Part (c) — every point of $\mathbb{R}$ is critical, and the image is null.**

For $f:\mathbb{R}\to\mathbb{R}^2$ the differential $d_xf:\mathbb{R}\to\mathbb{R}^2$ has rank at most $1<2$, so it is never surjective; every $x\in\mathbb{R}$ is critical, $f(\operatorname{Crit}(f))=f(\mathbb{R})$, and by Sard's theorem $f(\mathbb{R})$ has measure zero in $\mathbb{R}^2$.

> [!note]- Derivation
> The Jacobian is the column vector
> $$Df(x)=\begin{pmatrix}f_1'(x)\\ f_2'(x)\end{pmatrix}\in\mathbb{R}^{2\times1}\qquad\text{(a map }\mathbb{R}\to\mathbb{R}^2\text{ has a single input variable).}$$
> Its rank is at most $1$, since a matrix with one column has rank $\le1$; and $1<2=n$. Hence $\operatorname{rank}Df(x)<n$ for *every* $x$ (operation 6), so by the Jacobian criterion every point is critical:
> $$\operatorname{Crit}(f)=\mathbb{R}.$$
> Consequently the critical-value set is the entire image (operation 3):
> $$f(\operatorname{Crit}(f))=f(\mathbb{R}).$$
> Now [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] applies to the smooth map $f:\mathbb{R}\to\mathbb{R}^2$: its set of critical values has Lebesgue measure zero in $\mathbb{R}^2$ (operation 5). Since that set is all of $f(\mathbb{R})$, we conclude
> $$f(\mathbb{R})\text{ has Lebesgue measure zero in }\mathbb{R}^2.$$
> In particular $f$ is not surjective, for $\mathbb{R}^2$ is not null. This is precisely Sard's Step 5 in the boundary regime $(k+1)n>m$ with $k=0$, $m=1$, $n=2$: the estimate $(k+1)n=2>1=m$ is what makes the image thin. The companion exercise [[Ex - The Deeply Critical Set and Taylor Expansion]] carries out that estimate with explicit constants (a bounded interval maps under a Lipschitz curve into a set coverable by $r$ squares of side $\sim1/r$, total area $\sim1/r\to0$), and contrasts it with the Peano space-filling curve, a *continuous* surjection $\mathbb{R}\to\mathbb{R}^2$ — showing that smoothness, not mere continuity, is doing the work here.

> [!note]- Complete formal solution
> **Claim.** For $f(x,y)=(x^2-y^2,2xy)$ and $g(x,y)=x^3-3xy^2$ the critical values are the single points $\{(0,0)\}$ and $\{0\}$ respectively, both Lebesgue-null; and every smooth $h:\mathbb{R}\to\mathbb{R}^2$ has $\operatorname{Crit}(h)=\mathbb{R}$ with $h(\mathbb{R})$ Lebesgue-null in $\mathbb{R}^2$.
>
> *(a)* The map $f:\mathbb{R}^2\to\mathbb{R}^2$ is square, so $(x,y)$ is critical iff $\det Df(x,y)=0$. With $Df(x,y)=\begin{pmatrix}2x&-2y\\2y&2x\end{pmatrix}$ we get $\det Df=4x^2+4y^2$, which is zero iff $x=y=0$. Thus $\operatorname{Crit}(f)=\{(0,0)\}$ and $f(\operatorname{Crit}(f))=\{f(0,0)\}=\{(0,0)\}$. A single point of $\mathbb{R}^2$ is null: for $\varepsilon>0$ it lies in a square of area $\varepsilon/4<\varepsilon$. Hence the critical values are null, as Sard's theorem requires.
>
> *(b)* The map $g:\mathbb{R}^2\to\mathbb{R}$ has target $\mathbb{R}$, so $(x,y)$ is critical iff $\nabla g(x,y)=0$, i.e. $3x^2-3y^2=0$ and $-6xy=0$. The second equation gives $x=0$ or $y=0$; either substituted into the first forces the other coordinate to vanish, so $\operatorname{Crit}(g)=\{(0,0)\}$ and $g(\operatorname{Crit}(g))=\{g(0,0)\}=\{0\}$. A single point of $\mathbb{R}$ is null. Hence the critical values are null.
>
> *(c)* For $h:\mathbb{R}\to\mathbb{R}^2$ the Jacobian $Dh(x)\in\mathbb{R}^{2\times1}$ has rank $\le1<2$, so $d_xh$ is never surjective and $\operatorname{Crit}(h)=\mathbb{R}$; thus $h(\operatorname{Crit}(h))=h(\mathbb{R})$. By [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] the critical values of the smooth map $h$ are Lebesgue-null in $\mathbb{R}^2$, so $h(\mathbb{R})$ is null and $h$ is not surjective. $\blacksquare$

> [!warning] A tempting but false shortcut
> One might guess that for a *square* polynomial map like Part (a) the critical set is "generically empty", so that $\det Df$ never vanishes. That is wrong: $\det Df=4(x^2+y^2)$ *does* vanish, at the origin. The correct statement is not that critical points are absent but that critical *values* are null. Confusing the two — treating "few critical values" as "few critical points" — fails badly for Part (c), where the critical points are *all* of $\mathbb{R}$ yet the critical values still form a null set. The nullity lives downstairs, in the target, never upstairs in the source.

---

# Key Takeaways

**The Jacobian criterion turns "critical point" into a solvable equation, and the shape of the domain and target dictates its form.** The single reusable reflex behind every part of this exercise is: to find critical points, write the Jacobian and impose $\operatorname{rank}Df(x)<n$. That abstract inequality specialises to three concrete equations according to dimensions — $\det Df(x)=0$ when $m=n$, $\nabla f(x)=0$ when $n=1$, and the vacuous "always true" when $m<n$. Recognising *which* regime you are in before computing anything is what makes these problems quick: Part (a) is a determinant, Part (b) is a gradient, and Part (c) is settled by counting columns. The trigger is any explicit smooth map together with a question about its critical points, regular values, or the surjectivity of its differential; the reaction is to write $Df$ and read off which regime governs. This same reflex is what one uses in the infinite-dimensional setting to decide when a Fredholm map $F:X\to Y$ has a given point as a regular value, where $\operatorname{rank}$ is replaced by surjectivity of $d_xF$ modulo a finite-dimensional cokernel.

**Nullity is a statement about the target, and Sard's theorem is only needed when the critical set is large.** Parts (a) and (b) do not use Sard's theorem at all: the critical-value set is a single point, and a point is null by the definition of measure zero. Sard's theorem earns its keep only in Part (c), where the critical set is the whole line and the critical-value set is a genuine curve — infinite, uncountable, and yet null. The lesson for spaced practice is to always distinguish the size of $\operatorname{Crit}(f)\subseteq\mathbb{R}^m$ (upstairs) from the size of $f(\operatorname{Crit}(f))\subseteq\mathbb{R}^n$ (downstairs); Sard's theorem constrains only the latter, and it is perfectly consistent for every point of the domain to be critical while the image remains thin. This is exactly why Sard's theorem is the engine of transversality and degree theory: it lets us assert that *most* values are regular even when the critical set is unavoidably enormous.

**The complex structure explains, without proving, why polynomial maps have such small critical sets.** Both polynomial maps here are avatars of the complex power map: $f=z\mapsto z^2$ and $g=z\mapsto\operatorname{Re}(z^3)$. A holomorphic map $z\mapsto z^d$ has complex derivative $dz^{d-1}$, vanishing only at the origin, and the Cauchy–Riemann equations make the real Jacobian determinant equal to $|dz^{d-1}|^2$, a sum of squares that can vanish only where the complex derivative does. Seeing this converts the determinant computation of Part (a) from an algebraic accident into a structural fact: holomorphic maps are critical exactly at the zeros of their derivative, a discrete set. This is a transferable diagnostic — whenever a real map between even-dimensional spaces is secretly holomorphic, expect its critical set to be a proper analytic subvariety, hence small, and expect its critical values to be null not by Sard's theorem but by the far stronger fact that they form a measure-zero analytic set. The companion drills [[Ex - The Deeply Critical Set and Taylor Expansion]] and the anchor [[Thm - Sard's Theorem for Smooth Maps]] carry these ideas to their general, non-holomorphic form.
