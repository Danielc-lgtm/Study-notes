---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Change of Variables Formula"
  - "Thm - Fubini's Theorem"
  - "Ex - The Gaussian integral via polar coordinates"
  - "Def - The Riemann Integral in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $B^n = \{x \in \mathbb{R}^n : |x| \leq 1\}$ be the closed unit ball, and $V_n = V(B^n)$ its volume.

1. Using [[Thm - Fubini's Theorem|Fubini's theorem]], establish the **slicing recursion** $V_n = V_{n-1}\cdot\displaystyle\int_{-1}^1 (1 - t^2)^{(n-1)/2}\,dt$.
2. Derive the closed form
$$V_n = \frac{\pi^{n/2}}{\Gamma\!\left(\tfrac{n}{2} + 1\right)},$$
where $\Gamma$ is the gamma function, by a second method: integrate the Gaussian $e^{-|x|^2}$ over $\mathbb{R}^n$ in two ways.
3. Check the two methods agree, and compute $V_1, V_2, V_3, V_4$.

**Recall:**

![[Thm - Fubini's Theorem#Statement]]

![[Thm - The Change of Variables Formula#Statement]]

The **gamma function** is $\Gamma(s) = \int_0^\infty t^{s-1}e^{-t}\,dt$ for $s > 0$. It satisfies $\Gamma(s+1) = s\,\Gamma(s)$, $\Gamma(1) = 1$ (so $\Gamma(n+1) = n!$), and $\Gamma(\tfrac12) = \sqrt\pi$. The **Gaussian integral** (see [[Ex - The Gaussian integral via polar coordinates]]) is $\int_{\mathbb{R}} e^{-x^2}\,dx = \sqrt\pi$, hence $\int_{\mathbb{R}^n} e^{-|x|^2}\,dV = \pi^{n/2}$. A function of $|x|$ alone is **radial**; in polar/spherical coordinates the volume element of the sphere of radius $\rho$ scales as $\rho^{n-1}$, so $\int_{\mathbb{R}^n} g(|x|)\,dV = n V_n\int_0^\infty g(\rho)\,\rho^{n-1}\,d\rho$.

---

# Convergent Strategy

**Problem class.** This is a *volume computation* attacked by two routes — a slicing recursion (Fubini) and a Gaussian-integral identity (change of variables). The [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] notes that establishing a measure or volume is a recurring target, and that recursion across dimension and matching coordinates to symmetry are the two engines.

**Assumption pattern.** The unit ball is radially symmetric and *sliceable*: fixing the last coordinate $x_n = t$, the cross-section is a ball of radius $\sqrt{1-t^2}$ in $\mathbb{R}^{n-1}$. Radial symmetry feeds the change-of-variables route; sliceability feeds the Fubini recursion.

**Theorem routing.** *Route 1 (Fubini):* slice $B^n$ at height $x_n = t$; the slice is $\sqrt{1-t^2}\cdot B^{n-1}$, whose volume is $(1-t^2)^{(n-1)/2}V_{n-1}$ by the linear scaling case of the change of variables formula. Integrating over $t$ gives the recursion. *Route 2 (Gaussian):* compute $\int_{\mathbb{R}^n} e^{-|x|^2}\,dV$ two ways — as $\pi^{n/2}$ (Fubini, product of one-dimensional Gaussians), and as $nV_n\int_0^\infty e^{-\rho^2}\rho^{n-1}d\rho$ (radial change of variables) — and equate.

**Key decision point.** The cleverness of Route 2 is to compute a *known* integral ($\int e^{-|x|^2} = \pi^{n/2}$) in a second way that *contains the unknown* $V_n$. The radial form $\int_{\mathbb{R}^n} g(|x|)\,dV = nV_n\int_0^\infty g(\rho)\rho^{n-1}d\rho$ exposes $V_n$ as a coefficient; choosing $g(\rho) = e^{-\rho^2}$ makes the remaining $\rho$-integral a gamma function. Equating the two evaluations solves for $V_n$ in closed form — far cleaner than unrolling the recursion of Route 1, which produces the same answer but only after evaluating a chain of $\int(1-t^2)^k\,dt$ integrals.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Reduce a multiple integral to iterated single integrals (Fubini).** Used both to slice $B^n$ (Route 1) and to factor $\int e^{-|x|^2}$ into one-dimensional Gaussians (Route 2).

2. **Use a linear change of variables to compute volumes.** The slice $\sqrt{1-t^2}\,B^{n-1}$ is a linear image of $B^{n-1}$, so its volume is $(1-t^2)^{(n-1)/2}V_{n-1}$.

3. **Change variables by a diffeomorphism, inserting the Jacobian.** The radial-integral formula $\int g(|x|)\,dV = nV_n\int g(\rho)\rho^{n-1}d\rho$ is the spherical change of variables.

4. **One-variable substitution.** The $\rho$-integral $\int_0^\infty e^{-\rho^2}\rho^{n-1}d\rho$ is converted to a gamma function by $s = \rho^2$.

---

# Hints

> [!note]- Hint 1
> For the recursion, slice the ball by the hyperplane $x_n = t$. For fixed $t \in [-1,1]$, the set of points $(x_1,\dots,x_{n-1})$ with $(x_1,\dots,x_{n-1},t) \in B^n$ is described by $x_1^2 + \cdots + x_{n-1}^2 \leq 1 - t^2$. What shape is that?

> [!note]- Hint 2
> The slice is a ball of radius $\sqrt{1-t^2}$ in $\mathbb{R}^{n-1}$. Scaling a region in $\mathbb{R}^{n-1}$ by a factor $\lambda$ multiplies its volume by $\lambda^{n-1}$ (the linear case of the change of variables formula, with $A = \lambda I$, $|\det A| = \lambda^{n-1}$). So the slice has $(n-1)$-volume $(1-t^2)^{(n-1)/2}V_{n-1}$. Integrate over $t$.

> [!note]- Hint 3
> For the closed form, compute $\int_{\mathbb{R}^n} e^{-|x|^2}\,dV$ twice. First way: $e^{-|x|^2} = \prod_j e^{-x_j^2}$, so by Fubini the integral is $(\int_{\mathbb{R}} e^{-x^2}dx)^n = \pi^{n/2}$.

> [!note]- Hint 4
> Second way: $e^{-|x|^2}$ is radial, so use $\int_{\mathbb{R}^n} g(|x|)\,dV = nV_n\int_0^\infty g(\rho)\rho^{n-1}\,d\rho$ with $g(\rho) = e^{-\rho^2}$. The $\rho$-integral becomes a gamma function under $s = \rho^2$: $\int_0^\infty e^{-\rho^2}\rho^{n-1}d\rho = \tfrac12\Gamma(n/2)$. Equate the two evaluations and solve for $V_n$.

---

# Solution

The ball is both sliceable (giving a Fubini recursion) and radially symmetric (letting the Gaussian integral pin down a closed form). The two methods are independent and agree.

**Step 1: The slicing recursion.**

$V_n = V_{n-1}\displaystyle\int_{-1}^1 (1-t^2)^{(n-1)/2}\,dt$.

> [!note]- Derivation
> Slice $B^n$ by the hyperplane $x_n = t$. The cross-section is
> $$\{(x_1,\dots,x_{n-1}) : x_1^2 + \cdots + x_{n-1}^2 + t^2 \leq 1\} = \{x' \in \mathbb{R}^{n-1} : |x'|^2 \leq 1 - t^2\},$$
> which for $|t| \leq 1$ is the closed ball of radius $\sqrt{1-t^2}$ in $\mathbb{R}^{n-1}$ — that is, the scaled ball $\sqrt{1-t^2}\cdot B^{n-1}$. Scaling a region of $\mathbb{R}^{n-1}$ by the factor $\lambda = \sqrt{1-t^2}$ is the linear map $\lambda I$, with $|\det(\lambda I)| = \lambda^{n-1}$; by the linear case of the [[Thm - The Change of Variables Formula|change of variables formula]], the slice has $(n-1)$-dimensional volume
> $$V_{n-1}(\text{slice}) = \lambda^{n-1}V_{n-1} = (1 - t^2)^{(n-1)/2}\,V_{n-1}.$$
> By [[Thm - Fubini's Theorem|Fubini's theorem]], the $n$-volume of $B^n$ is the integral of its cross-sectional $(n-1)$-volumes:
> $$V_n = \int_{-1}^1 V_{n-1}(\text{slice})\,dt = V_{n-1}\int_{-1}^1 (1-t^2)^{(n-1)/2}\,dt.$$
> This recursion, with the base case $V_1 = 2$ (the unit "ball" in $\mathbb{R}^1$ is $[-1,1]$), determines all $V_n$ — but evaluating the chain of integrals $\int(1-t^2)^{(n-1)/2}dt$ is laborious, so we obtain the closed form by the cleaner second route and then return to confirm consistency.

**Step 2: The Gaussian integral, computed by Fubini.**

$\displaystyle\int_{\mathbb{R}^n} e^{-|x|^2}\,dV = \pi^{n/2}$.

> [!note]- Derivation
> The integrand factors across coordinates: $e^{-|x|^2} = e^{-(x_1^2 + \cdots + x_n^2)} = \prod_{j=1}^n e^{-x_j^2}$. It is absolutely integrable on $\mathbb{R}^n$, so the product form of [[Thm - Fubini's Theorem|Fubini's theorem]] gives
> $$\int_{\mathbb{R}^n} e^{-|x|^2}\,dV = \prod_{j=1}^n \int_{-\infty}^\infty e^{-x_j^2}\,dx_j = \left(\int_{-\infty}^\infty e^{-x^2}\,dx\right)^{\!n} = (\sqrt\pi)^n = \pi^{n/2},$$
> the one-dimensional Gaussian $\int e^{-x^2}dx = \sqrt\pi$ being the result of [[Ex - The Gaussian integral via polar coordinates]].

**Step 3: The Gaussian integral, computed by the radial change of variables.**

$\displaystyle\int_{\mathbb{R}^n} e^{-|x|^2}\,dV = n V_n\cdot\tfrac12\,\Gamma\!\left(\tfrac{n}{2}\right)$.

> [!note]- Derivation
> The integrand $e^{-|x|^2}$ is *radial* — a function of $|x|$ alone. In spherical coordinates, a radial integral over $\mathbb{R}^n$ reduces to a single $\rho$-integral weighted by the surface area of the sphere of radius $\rho$. Concretely, the sphere of radius $\rho$ has $(n-1)$-dimensional surface area $\rho^{n-1}\cdot|\mathbb{S}^{n-1}|$ where $|\mathbb{S}^{n-1}| = nV_n$ is the surface area of the unit sphere (differentiate $V(\rho B^n) = \rho^n V_n$ in $\rho$: $\frac{d}{d\rho}(\rho^n V_n) = n\rho^{n-1}V_n$). Hence the spherical change of variables gives
> $$\int_{\mathbb{R}^n} g(|x|)\,dV = nV_n\int_0^\infty g(\rho)\,\rho^{n-1}\,d\rho.$$
> Apply this with $g(\rho) = e^{-\rho^2}$:
> $$\int_{\mathbb{R}^n} e^{-|x|^2}\,dV = nV_n\int_0^\infty e^{-\rho^2}\,\rho^{n-1}\,d\rho.$$
> Evaluate the $\rho$-integral by the substitution $s = \rho^2$, so $\rho = s^{1/2}$, $d\rho = \tfrac12 s^{-1/2}\,ds$, and $\rho^{n-1} = s^{(n-1)/2}$:
> $$\int_0^\infty e^{-\rho^2}\rho^{n-1}\,d\rho = \int_0^\infty e^{-s}\,s^{(n-1)/2}\cdot\tfrac12 s^{-1/2}\,ds = \tfrac12\int_0^\infty e^{-s}\,s^{n/2 - 1}\,ds = \tfrac12\,\Gamma\!\left(\tfrac{n}{2}\right),$$
> recognizing the last integral as $\Gamma(n/2)$ (with $s^{n/2-1} = s^{(n/2)-1}$). Therefore
> $$\int_{\mathbb{R}^n} e^{-|x|^2}\,dV = nV_n\cdot\tfrac12\,\Gamma\!\left(\tfrac{n}{2}\right).$$

**Step 4: Equate and solve for $V_n$.**

$V_n = \dfrac{\pi^{n/2}}{\Gamma(n/2 + 1)}$.

> [!note]- Derivation
> Steps 2 and 3 are two evaluations of the same integral $\int_{\mathbb{R}^n} e^{-|x|^2}\,dV$, so they are equal:
> $$\pi^{n/2} = nV_n\cdot\tfrac12\,\Gamma\!\left(\tfrac{n}{2}\right).$$
> Solve for $V_n$:
> $$V_n = \frac{2\,\pi^{n/2}}{n\,\Gamma(n/2)}.$$
> Simplify the denominator using the functional equation $\Gamma(s+1) = s\,\Gamma(s)$ with $s = n/2$: $\frac{n}{2}\,\Gamma(n/2) = \Gamma(n/2 + 1)$, so $n\,\Gamma(n/2) = 2\,\Gamma(n/2 + 1)$. Hence
> $$V_n = \frac{2\,\pi^{n/2}}{2\,\Gamma(n/2 + 1)} = \frac{\pi^{n/2}}{\Gamma\!\left(\tfrac{n}{2} + 1\right)}. \qquad \blacksquare$$

**Step 5: Consistency check and small cases.**

> [!note]- Derivation
> *Recursion check.* The closed form should satisfy the Step 1 recursion. The integral $\int_{-1}^1(1-t^2)^{(n-1)/2}dt$ is a beta-function integral equal to $\frac{\sqrt\pi\,\Gamma(\frac{n+1}{2})}{\Gamma(\frac{n}{2}+1)}$. Then
> $$V_{n-1}\cdot\frac{\sqrt\pi\,\Gamma(\frac{n+1}{2})}{\Gamma(\frac n2 + 1)} = \frac{\pi^{(n-1)/2}}{\Gamma(\frac{n+1}{2})}\cdot\frac{\sqrt\pi\,\Gamma(\frac{n+1}{2})}{\Gamma(\frac n2 + 1)} = \frac{\pi^{n/2}}{\Gamma(\frac n2 + 1)} = V_n,$$
> so the closed form is consistent with the Fubini recursion.
>
> *Small cases.* Using $\Gamma(1) = 1$, $\Gamma(\tfrac12) = \sqrt\pi$, $\Gamma(\tfrac32) = \tfrac12\sqrt\pi$, $\Gamma(2) = 1$, $\Gamma(\tfrac52) = \tfrac34\sqrt\pi$, $\Gamma(3) = 2$:
> $$V_1 = \frac{\pi^{1/2}}{\Gamma(3/2)} = \frac{\sqrt\pi}{\tfrac12\sqrt\pi} = 2, \qquad V_2 = \frac{\pi}{\Gamma(2)} = \frac{\pi}{1} = \pi,$$
> $$V_3 = \frac{\pi^{3/2}}{\Gamma(5/2)} = \frac{\pi^{3/2}}{\tfrac34\sqrt\pi} = \frac{4\pi}{3}, \qquad V_4 = \frac{\pi^2}{\Gamma(3)} = \frac{\pi^2}{2}.$$
> These are the familiar values: $[-1,1]$ has length $2$, the unit disk has area $\pi$, the unit ball has volume $\tfrac43\pi$.

> [!note]- Complete formal solution
> *Recursion.* Slicing $B^n$ at $x_n = t$ gives the $(n-1)$-ball of radius $\sqrt{1-t^2}$, of volume $(1-t^2)^{(n-1)/2}V_{n-1}$ by linear scaling; [[Thm - Fubini's Theorem|Fubini]] gives $V_n = V_{n-1}\int_{-1}^1(1-t^2)^{(n-1)/2}\,dt$.
>
> *Closed form.* Compute $\int_{\mathbb{R}^n}e^{-|x|^2}\,dV$ two ways. By Fubini and the one-dimensional Gaussian, it is $(\sqrt\pi)^n = \pi^{n/2}$. By the radial change of variables, $\int_{\mathbb{R}^n}g(|x|)\,dV = nV_n\int_0^\infty g(\rho)\rho^{n-1}d\rho$, and with $g = e^{-\rho^2}$ the substitution $s = \rho^2$ turns the $\rho$-integral into $\tfrac12\Gamma(n/2)$, giving $nV_n\cdot\tfrac12\Gamma(n/2)$. Equate: $\pi^{n/2} = \tfrac n2 V_n\Gamma(n/2) = V_n\Gamma(n/2+1)$, so
> $$V_n = \frac{\pi^{n/2}}{\Gamma(n/2+1)}.$$
> This satisfies the recursion (the $t$-integral is the beta value $\sqrt\pi\,\Gamma(\tfrac{n+1}{2})/\Gamma(\tfrac n2+1)$) and gives $V_1 = 2$, $V_2 = \pi$, $V_3 = \tfrac43\pi$, $V_4 = \tfrac12\pi^2$. $\blacksquare$

---

# Key Takeaways

**Compute a known integral two ways, one of which contains the unknown.** Route 2 is a model of a powerful technique: the Gaussian integral $\int_{\mathbb{R}^n}e^{-|x|^2}$ is *already known* to be $\pi^{n/2}$, but evaluating it a second time — by the radial change of variables — produces an expression $nV_n\cdot\tfrac12\Gamma(n/2)$ that contains the genuinely unknown quantity $V_n$. Equating the two evaluations solves for $V_n$. The trigger for this technique is: you want a quantity $Q$ that appears as a coefficient or factor inside some integral; find an integral whose value you know independently and which exposes $Q$, then equate. It is the integral-calculus analogue of "evaluate both sides of an identity". The radial form $\int g(|x|)\,dV = nV_n\int g(\rho)\rho^{n-1}d\rho$ is the lever that exposes $V_n$, and the gamma function is what the leftover $\rho$-integral always becomes.

**Slicing plus linear scaling gives a dimensional recursion; radial symmetry plus the Gaussian gives the closed form.** The two routes illustrate the two engines named in the topic strategy. Fubini-slicing reduces $V_n$ to $V_{n-1}$ by cutting the ball into cross-sections, each a *scaled copy* of a lower-dimensional ball — and the linear case of the change of variables formula ($\lambda I$ scales volume by $\lambda^{n-1}$) is what turns the geometric scaling into the algebraic factor $(1-t^2)^{(n-1)/2}$. This recursion is correct but computationally heavy. The change-of-variables route, exploiting radial symmetry, bypasses the recursion entirely and lands the closed form in one equation. The general lesson: when a quantity is defined recursively across dimension, look for a generating-function-style identity (here the Gaussian integral) that captures all dimensions at once and yields the closed form directly.

**The gamma function is the universal output of radial integrals.** Every radial integral over $\mathbb{R}^n$, after the substitution $s = \rho^2$ (or $s = \rho$), produces an integral $\int_0^\infty e^{-s}s^{\alpha-1}\,ds = \Gamma(\alpha)$. The appearance of $\Gamma(n/2+1)$ in $V_n$ is not a coincidence but the signature of having integrated a radial function in $n$ dimensions: the exponent $n/2$ is half the dimension because the substitution $s = \rho^2$ halves powers, and the gamma function is precisely the device that interpolates the factorial to non-integer (here half-integer) arguments. Recognizing $\int_0^\infty e^{-\rho^2}\rho^{n-1}d\rho = \tfrac12\Gamma(n/2)$ on sight is the reusable skill — it converts any Gaussian-weighted radial integral into a gamma value, and it is why $\Gamma$ pervades the volumes and surface areas of spheres, the moments of the normal distribution, and the partition functions of statistical mechanics.
