---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Boosts as Hyperbolic Rotations"
  - "Def - Rapidity"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

Work in $1+1$ dimensions, $c = 1$, with the boost $\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}$ on $(t, x)$.

1. Show that $\Lambda[\varphi]$ has real eigenvalues $e^{\varphi}$ and $e^{-\varphi}$, with eigenvectors the two null directions $n_\pm = (1, \pm 1)$. Contrast with the Euclidean rotation $R[\theta]$, whose eigenvalues $e^{\pm i\theta}$ are complex and which has no real eigenvectors.
2. Introduce light-cone (null) coordinates $u = t + x$, $w = t - x$. Show that in these coordinates the boost acts diagonally, $u \mapsto e^{\varphi}u$, $w \mapsto e^{-\varphi}w$, and that the interval is $\Delta s^2 = uw$. Conclude that the boost manifestly preserves the interval and that its [[Def - Classification of Four-Vectors|null]] structure is the eigenbasis.
3. Use the diagonal action to re-prove that collinear boosts [[Thm - Boosts Compose by Adding Rapidities|add rapidities]] in one line.
4. Identify the eigenvalue $e^{\varphi}$ as the relativistic [[Def - Rapidity|Doppler]] factor $k$, and show that composing boosts multiplies Doppler factors.

**Recall:**

![[Def - Boosts as Hyperbolic Rotations#The Definition]]

A vector $X$ is [[Def - Classification of Four-Vectors|null]] (lightlike) if $X\cdot X = 0$; the null vectors form the light cone, in $1+1$ dimensions the two lines $t = \pm x$. The [[Def - Rapidity|rapidity]] is $\varphi$ with $v = \tanh\varphi$, $\gamma = \cosh\varphi$; the Doppler factor for motion along the line of sight is $k = e^{\varphi} = \gamma(1 + v)$.

---

# Convergent Strategy

**Problem class.** A *structural* problem — diagonalise the boost and read its geometry off the eigenstructure. It makes precise the slogan "a boost is a [[Def - Boosts as Hyperbolic Rotations|hyperbolic rotation]]" by exhibiting the difference from a rotation at the level of eigenvalues (real vs complex).

**Assumption pattern.** The boost matrix and the indefinite metric. The key recognisable feature is that the metric factors as $\Delta s^2 = t^2 - x^2 = (t+x)(t-x) = uw$, which signals that null coordinates diagonalise everything — the boost, the metric, and the composition law.

**Theorem routing.** Part 1 is an eigenvalue computation; Part 2 is the change to null coordinates where the boost is diagonal; Part 3 reads additivity off the diagonal; Part 4 names the eigenvalue physically. The route is: characteristic polynomial $\to$ eigenvectors $=$ null directions $\to$ diagonalise $\to$ composition $=$ multiplication of exponentials.

**Key decision point.** The decisive move is to change to *null coordinates* $u = t+x$, $w = t-x$ instead of staying in $(t,x)$. In $(t,x)$ the boost is a full $2\times 2$ matrix and additivity needs the hyperbolic addition formulas; in $(u,w)$ it is diagonal and additivity is "exponents add". Recognising that the light cone is the boost's eigenbasis is the insight that simplifies the entire chapter's computations.

---

# Legal Operations Used

1. **Classify by the sign of the norm (operation 9 from the topic page).** The eigenvectors turn out to be exactly the null directions; the exercise is built on the timelike/spacelike/null trichotomy.

2. **Switch to rapidity / hyperbolic-rotation form (operation 6 from the topic page).** The boost is handled in its hyperbolic-rotation form, and the diagonalisation makes the rapidity the additive exponent.

3. **Compute an invariant in the convenient coordinates (operation 7 from the topic page).** Null coordinates are the convenient frame: the interval $\Delta s^2 = uw$ is manifestly preserved because $u \mapsto e^\varphi u$, $w \mapsto e^{-\varphi}w$ keeps $uw$ fixed.

---

# Hints

> [!note]- Hint 1
> The characteristic polynomial of $\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}$ is $\lambda^2 - 2\cosh\varphi\,\lambda + (\cosh^2\varphi - \sinh^2\varphi) = \lambda^2 - 2\cosh\varphi\,\lambda + 1$. Solve; the roots multiply to $1$.

> [!note]- Hint 2
> Test the vectors $(1, 1)$ and $(1, -1)$ directly. $\Lambda[\varphi](1,1)^{\mathsf T} = (\cosh\varphi + \sinh\varphi)(1,1)^{\mathsf T} = e^{\varphi}(1,1)^{\mathsf T}$, since $\cosh\varphi + \sinh\varphi = e^{\varphi}$.

> [!note]- Hint 3
> In coordinates $u = t + x$, $w = t - x$, the eigenvectors $(1, \pm 1)$ become the coordinate axes. So the boost is diagonal: $u \mapsto e^{\varphi}u$, $w \mapsto e^{-\varphi}w$. And $uw = (t+x)(t-x) = t^2 - x^2$.

> [!note]- Hint 4
> Composing $u \mapsto e^{\varphi_1}u$ then $u \mapsto e^{\varphi_2}u$ gives $u \mapsto e^{\varphi_1}e^{\varphi_2}u = e^{\varphi_1 + \varphi_2}u$. Exponents add. The factor $e^{\varphi}$ is the Doppler shift $k$.

---

# Solution

The exercise diagonalises the boost and reaps the consequences. Step 1 finds the real eigenvalues $e^{\pm\varphi}$ and shows the eigenvectors are the null directions — the first sharp difference from a rotation. Step 2 changes to null coordinates, where the boost is diagonal and the metric is $uw$, making interval-preservation obvious. Step 3 reads additivity straight off the diagonal. Step 4 identifies the eigenvalue as the Doppler factor.

**Step 1: real eigenvalues $e^{\pm\varphi}$, null eigenvectors.**

> [!note]- Derivation
> The characteristic polynomial is
> $$\det(\Lambda[\varphi] - \lambda I) = (\cosh\varphi - \lambda)^2 - \sinh^2\varphi = \lambda^2 - 2\cosh\varphi\,\lambda + (\cosh^2\varphi - \sinh^2\varphi) = \lambda^2 - 2\cosh\varphi\,\lambda + 1.$$
> The roots are $\lambda = \cosh\varphi \pm \sqrt{\cosh^2\varphi - 1} = \cosh\varphi \pm \sinh\varphi = e^{\pm\varphi}$, both *real*. Their product is $e^{\varphi}e^{-\varphi} = 1 = \det\Lambda[\varphi]$, consistent.
>
> The eigenvectors: for $\lambda = e^{\varphi}$, solve $(\cosh\varphi - e^{\varphi})t + \sinh\varphi\, x = 0$; since $\cosh\varphi - e^{\varphi} = -\sinh\varphi$, this is $-\sinh\varphi\,t + \sinh\varphi\,x = 0$, i.e. $t = x$, the null direction $n_+ = (1, 1)$. Likewise $\lambda = e^{-\varphi}$ gives $t = -x$, the direction $n_- = (1, -1)$. Both eigenvectors are [[Def - Classification of Four-Vectors|null]]: $n_\pm\cdot n_\pm = 1 - 1 = 0$.
>
> *Contrast with rotation.* The Euclidean rotation $R[\theta] = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ has characteristic polynomial $\lambda^2 - 2\cos\theta\,\lambda + 1$ with roots $e^{\pm i\theta}$ — *complex* (for $\theta \neq 0, \pi$), and no real eigenvectors. A rotation spins every real direction; a boost fixes two real null directions. This is the eigenvalue signature of the difference between definite (circular, complex eigenvalues) and indefinite (hyperbolic, real eigenvalues) geometry.

**Step 2: null coordinates diagonalise the boost; $\Delta s^2 = uw$.**

> [!note]- Derivation
> Set $u = t + x$, $w = t - x$ (the coordinates along the null eigenvectors). Then $t = (u+w)/2$, $x = (u-w)/2$. Apply the boost $t' = \cosh\varphi\,t + \sinh\varphi\,x$, $x' = \sinh\varphi\,t + \cosh\varphi\,x$:
> $$u' = t' + x' = (\cosh\varphi + \sinh\varphi)(t + x) = e^{\varphi}u, \qquad w' = t' - x' = (\cosh\varphi - \sinh\varphi)(t - x) = e^{-\varphi}w.$$
> So in null coordinates the boost is the diagonal matrix $\mathrm{diag}(e^{\varphi}, e^{-\varphi})$ — it stretches one null axis and shrinks the other by reciprocal factors.
>
> The interval factors in these coordinates:
> $$\Delta s^2 = t^2 - x^2 = (t+x)(t-x) = uw.$$
> The boost sends $uw \mapsto (e^{\varphi}u)(e^{-\varphi}w) = uw$, so it *manifestly* preserves the interval — the reciprocal stretch factors cancel. This is the cleanest possible proof of [[Thm - Invariance of the Spacetime Interval|interval invariance]] in $1+1$ dimensions: in null coordinates it is the statement that $\mathrm{diag}(e^\varphi, e^{-\varphi})$ preserves the product $uw$.

**Step 3: additivity in one line.**

> [!note]- Derivation
> Apply $\Lambda[\varphi_2]$ then $\Lambda[\varphi_1]$ in null coordinates: $u \mapsto e^{\varphi_2}u \mapsto e^{\varphi_1}e^{\varphi_2}u = e^{\varphi_1 + \varphi_2}u$, and $w \mapsto e^{\varphi_2}{}^{-1}\!\cdots = e^{-(\varphi_1 + \varphi_2)}w$. The composite is $\mathrm{diag}(e^{\varphi_1 + \varphi_2}, e^{-(\varphi_1 + \varphi_2)}) = \Lambda[\varphi_1 + \varphi_2]$. **Multiplying the diagonal exponential factors adds the exponents — which is rapidity additivity** ([[Thm - Boosts Compose by Adding Rapidities]]). No hyperbolic addition formulas are needed; in the eigenbasis the group law is just multiplication of scalars.

**Step 4: the eigenvalue is the Doppler factor.**

> [!note]- Derivation
> The eigenvalue $k = e^{\varphi} = \cosh\varphi + \sinh\varphi = \gamma(1 + v)$ is exactly the relativistic [[Def - Rapidity|Doppler]] shift factor for light moving in the $+x$ direction (the $u$ null direction). A light pulse's frequency, carried on the null direction $u$, is multiplied by $k = e^{\varphi}$ under the boost; one on $w$ (the $-x$ direction) is divided by $k$. Because the boost acts on $u$ by multiplication by $e^{\varphi}$, **composing boosts multiplies the Doppler factors**: $k_1 k_2 = e^{\varphi_1}e^{\varphi_2} = e^{\varphi_1 + \varphi_2}$, the Doppler factor of the composite boost. So "rapidities add" and "Doppler factors multiply" are the same statement, related by $k = e^{\varphi}$ — the logarithm of the Doppler factor is the rapidity.

> [!note]- Complete formal solution
> The boost $\Lambda[\varphi]$ has characteristic polynomial $\lambda^2 - 2\cosh\varphi\,\lambda + 1$, roots $e^{\pm\varphi}$ (real), with eigenvectors the null directions $(1, \pm 1)$ (since $\cosh\varphi \pm \sinh\varphi = e^{\pm\varphi}$); a Euclidean rotation instead has complex eigenvalues $e^{\pm i\theta}$ and no real eigenvectors. In null coordinates $u = t+x$, $w = t-x$ the boost is diagonal, $u \mapsto e^\varphi u$, $w \mapsto e^{-\varphi}w$, the interval is $\Delta s^2 = uw$, and interval-preservation is immediate from $e^\varphi e^{-\varphi} = 1$. Composing boosts multiplies the diagonal factors, $e^{\varphi_1}e^{\varphi_2} = e^{\varphi_1+\varphi_2}$, which is rapidity additivity. The eigenvalue $k = e^\varphi = \gamma(1+v)$ is the relativistic Doppler factor, and composing boosts multiplies Doppler factors. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to "diagonalise" by finding eigenvectors and forgetting they are null, treating them as an ordinary orthonormal eigenbasis. But the eigenvectors $(1, \pm 1)$ are *not* orthonormal in the Minkowski metric — they are null, with $n_\pm\cdot n_\pm = 0$ and $n_+\cdot n_- = 2 \neq 0$ — so the usual "$\Lambda = U D U^{\mathsf T}$ with $U$ orthogonal" does not apply. The correct statement is that the boost is diagonal in the null *basis* (a non-orthonormal change of coordinates), and the metric in that basis is the off-diagonal $\Delta s^2 = uw$, not a sum of squares. Mixing up the null basis with an orthonormal one leads to sign errors in the metric.

---

# Key Takeaways

**Real versus complex eigenvalues is the eigenvalue fingerprint of indefinite versus definite geometry.** The single sharpest way to see that a boost is *not* a rotation is at the level of eigenvalues: a rotation has complex eigenvalues $e^{\pm i\theta}$ on the unit circle and no real eigenvectors (it spins everything), while a boost has real eigenvalues $e^{\pm\varphi}$ off the unit circle and two real eigenvectors (it stretches the null directions). This is the spectral shadow of the metric signature — definite forms give compact, circular, complex-eigenvalue isometries; indefinite forms give non-compact, hyperbolic, real-eigenvalue ones. The trigger to remember: when an isometry has real eigenvalues $\lambda$ and $1/\lambda$ off the unit circle, you are looking at a boost (a hyperbolic rotation), and its eigenvectors are the null directions the metric singles out.

**Null (light-cone) coordinates diagonalise the boost and trivialise the chapter.** The reusable technique is the change to $u = t + x$, $w = t - x$, in which the boost becomes $\mathrm{diag}(e^{\varphi}, e^{-\varphi})$ and the metric becomes the product $uw$. In these coordinates every fact about boosts becomes a fact about scalar multiplication: interval invariance is $e^{\varphi}e^{-\varphi} = 1$, rapidity additivity is $e^{\varphi_1}e^{\varphi_2} = e^{\varphi_1 + \varphi_2}$, and the Doppler effect is the multiplication of the $u$-component by $e^{\varphi}$. Whenever a $1+1$ relativistic computation looks messy in $(t, x)$, switch to null coordinates — the boost diagonalises and the algebra collapses. This is the relativistic analogue of diagonalising a rotation in the complex coordinates $x \pm iy$, with the imaginary unit replaced by the splitting of the real light cone.

**"Rapidities add" and "Doppler factors multiply" are one statement under $k = e^{\varphi}$.** The exercise reveals that the additive parameter (rapidity) and the multiplicative parameter (Doppler factor) are logarithm and exponential of each other: $k = e^{\varphi}$, so $\varphi = \ln k$. Additivity of rapidity is multiplicativity of the Doppler factor, and the eigenvalue of the boost on a null direction is precisely $k$. This unifies two facts usually learned separately — the velocity-composition law and the compounding of Doppler shifts through a chain of moving sources — into one: the boost acts on light-cone components by multiplication, so the natural invariant of a chain of boosts is the *product* of Doppler factors, equivalently the *sum* of rapidities. Recognising a quantity that *multiplies* under composition (like $k$) signals that its logarithm is the additive group coordinate, a pattern that recurs whenever a one-parameter group acts by scaling.
