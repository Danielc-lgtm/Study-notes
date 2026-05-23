---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthonormal Basis"
  - "Thm - Gram-Schmidt Procedure"
tags: [algebra, linear-algebra]
---

# Problem Statement

In the inner product space $V = \mathcal{P}(\mathbb{R})$ of real polynomials, with inner product
$$
\langle p, q\rangle = \int_{-1}^{1} p(x) q(x)\, dx,
$$
apply [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] to the monomial sequence $1, x, x^2, x^3$ to produce an orthonormal list of the first four polynomials in this inner product. Verify that the result, suitably scaled, gives the **Legendre polynomials**:
$$
P_0(x) = 1, \quad P_1(x) = x, \quad P_2(x) = \tfrac{1}{2}(3x^2 - 1), \quad P_3(x) = \tfrac{1}{2}(5x^3 - 3x).
$$

(The Legendre polynomials are conventionally normalized so that $P_n(1) = 1$ for each $n$; this differs from $L^2$-orthonormalization. Show that the orthogonal-but-not-normalized Gram-Schmidt outputs are scalar multiples of the Legendre polynomials.)

**Recall:**

![[Thm - Gram-Schmidt Procedure#Statement]]

The first four monomials $1, x, x^2, x^3$ in $\mathcal{P}_3 \subseteq \mathcal{P}(\mathbb{R})$ are linearly independent. The Gram-Schmidt procedure produces orthonormal polynomials $e_1, e_2, e_3, e_4$ with $\operatorname{span}(e_1, \dots, e_k) = \operatorname{span}(1, x, \dots, x^{k-1})$ for each $k$.

The basic integrals on $[-1, 1]$:
$$
\int_{-1}^1 x^n\, dx = \begin{cases} 2/(n+1) & n \text{ even}, \\ 0 & n \text{ odd}. \end{cases}
$$

---

# Convergent Strategy

**Problem class.** This is a *construct an orthonormal list* problem in a specific inner product space. The strategy is mechanical: apply Gram-Schmidt step by step, observing the parity simplifications.

**Assumption pattern.** The inner product $\int_{-1}^1 fg$ gives the integrals $\int_{-1}^1 x^j x^k\, dx = 2/(j+k+1)$ if $j+k$ is even, $0$ if $j+k$ is odd. So even monomials are orthogonal to odd monomials *automatically* — Gram-Schmidt within $\{1, x^2, x^4, \dots\}$ and within $\{x, x^3, x^5, \dots\}$ proceed independently.

**Theorem routing.** Direct application of the [[Thm - Gram-Schmidt Procedure|Gram-Schmidt procedure]]:
1. $f_1 = 1$, $\|f_1\|^2 = 2$, $e_1 = 1/\sqrt{2}$.
2. $f_2 = x -$ (projection of $x$ onto $\operatorname{span}(e_1)$). By parity, $\langle x, 1\rangle = \int_{-1}^1 x\, dx = 0$, so $f_2 = x$. Normalize: $\|x\|^2 = 2/3$, so $e_2 = x\sqrt{3/2}$.
3. $f_3 = x^2 -$ (projection of $x^2$ onto $\operatorname{span}(e_1, e_2)$). The projection onto $e_2$ vanishes by parity; the projection onto $e_1$ gives $\langle x^2, e_1\rangle = (2/3)/\sqrt{2}$, so $f_3 = x^2 - 1/3$.
4. $f_4 = x^3 -$ (projection of $x^3$ onto $\operatorname{span}(e_1, e_2, e_3)$). The projection onto $e_1, e_3$ vanishes by parity; the projection onto $e_2$ involves $\langle x^3, x\rangle = 2/5$, leading to $f_4 = x^3 - (3/5)x$.

**Key decision point.** Whether to normalize at each step or carry the un-normalized $f_k$'s through and normalize at the end. The procedure formula uses $\langle v_k, f_j\rangle/\|f_j\|^2$ if you use un-normalized $f_j$, or $\langle v_k, e_j\rangle$ if you use normalized $e_j$. Both are correct.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VI — §6 Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Orthogonalize via Gram-Schmidt** (operation 2). The procedure is the technique being applied.

2. **Take the inner product with a basis vector to extract a coefficient** (operation 6). The projection coefficients are inner products against the previous orthonormal basis vectors.

3. **Use Pythagoras to break a norm into orthogonal pieces** (operation 4), implicitly, in computing $\|f_k\|$.

---

# Hints

> [!note]- Hint 1
> Observe parity: on $[-1, 1]$ with the symmetric inner product, even monomials are orthogonal to odd monomials. So Gram-Schmidt of $\{1, x, x^2, x^3\}$ splits into independent Gram-Schmidt of $\{1, x^2\}$ and $\{x, x^3\}$.

> [!note]- Hint 2
> Start with $f_1 = 1$. Compute $\|1\|^2 = \int_{-1}^1 1\, dx = 2$. So $e_1 = 1/\sqrt{2}$.

> [!note]- Hint 3
> For $f_2 = x$: the projection onto $e_1$ is $\langle x, e_1\rangle e_1 = (1/\sqrt{2})\int_{-1}^1 x\, dx \cdot e_1 = 0$. So $f_2 = x$, and $\|x\|^2 = 2/3$, so $e_2 = x\sqrt{3/2}$.

> [!note]- Hint 4
> For $f_3 = x^2 - (\text{projections})$: the projection onto $e_2$ vanishes by parity ($\langle x^2, x\rangle = 0$). The projection onto $e_1$ is $\langle x^2, 1/\sqrt{2}\rangle e_1 = (1/\sqrt{2}) \cdot (2/3) \cdot (1/\sqrt{2}) = 1/3$. So $f_3 = x^2 - 1/3$.

> [!note]- Hint 5
> For $f_4 = x^3 - (\text{projections})$: the projections onto $e_1, e_3$ vanish by parity. The projection onto $e_2$ is $\langle x^3, e_2\rangle e_2 = \sqrt{3/2}\cdot \int_{-1}^1 x^4\, dx \cdot e_2 = \sqrt{3/2}\cdot (2/5)\cdot e_2 = (2/5)\sqrt{3/2}\cdot \sqrt{3/2}\, x = (3/5) x$. So $f_4 = x^3 - (3/5)x$.

> [!note]- Hint 6
> Compare to Legendre: $P_2 = (1/2)(3x^2 - 1)$, so $f_3 = x^2 - 1/3 = (2/3)P_2$. And $P_3 = (1/2)(5x^3 - 3x)$, so $f_4 = x^3 - (3/5)x = (2/5)P_3$. The $f_k$'s are scalar multiples of the Legendre polynomials.

---

# Solution

The strategy is to apply Gram-Schmidt step by step, exploiting the parity structure to eliminate half the inner products.

**Plan:** Step 1 sets up the integrals. Steps 2-5 apply the Gram-Schmidt procedure to $1, x, x^2, x^3$. Step 6 verifies that the un-normalized outputs $f_k$ are scalar multiples of Legendre polynomials.

**Step 1: Basic integrals on $[-1, 1]$.**

The moment integrals are $\int_{-1}^1 x^n\, dx = 2/(n+1)$ for $n$ even, and $0$ for $n$ odd.

> [!note]- Derivation
> Direct integration: $\int_{-1}^1 x^n\, dx = [x^{n+1}/(n+1)]_{-1}^1 = (1 - (-1)^{n+1})/(n+1) = 2/(n+1)$ if $n$ is even, $0$ if $n$ is odd.
>
> Specific cases used below: $\int_{-1}^1 1\, dx = 2$, $\int_{-1}^1 x^2 dx = 2/3$, $\int_{-1}^1 x^4 dx = 2/5$, $\int_{-1}^1 x^6 dx = 2/7$.

**Step 2: $f_1 = 1$ and $e_1 = 1/\sqrt{2}$.**

> [!note]- Derivation
> $f_1 = v_1 = 1$. Then $\|f_1\|^2 = \langle 1, 1\rangle = \int_{-1}^1 1\, dx = 2$, so $\|f_1\| = \sqrt{2}$ and $e_1 = f_1/\|f_1\| = 1/\sqrt{2}$.

**Step 3: $f_2 = x$ and $e_2 = x\sqrt{3/2}$.**

> [!note]- Derivation
> Project $v_2 = x$ onto $\operatorname{span}(e_1)$:
> $$\langle x, e_1\rangle = \langle x, 1/\sqrt{2}\rangle = \frac{1}{\sqrt{2}}\int_{-1}^1 x\, dx = 0$$
> (the integrand is odd over a symmetric interval). So the projection is zero, and $f_2 = x - 0 = x$.
>
> Normalize: $\|f_2\|^2 = \int_{-1}^1 x^2 dx = 2/3$, $\|f_2\| = \sqrt{2/3}$, $e_2 = x/\sqrt{2/3} = x\sqrt{3/2}$.

**Step 4: $f_3 = x^2 - 1/3$ and $e_3 = (x^2 - 1/3)\sqrt{45/8}$.**

> [!note]- Derivation
> Project $v_3 = x^2$ onto $\operatorname{span}(e_1, e_2)$:
> $$\langle x^2, e_1\rangle = \frac{1}{\sqrt{2}}\int_{-1}^1 x^2 dx = \frac{1}{\sqrt{2}}\cdot \frac{2}{3} = \frac{\sqrt{2}}{3}.$$
> $$\langle x^2, e_2\rangle = \sqrt{3/2}\int_{-1}^1 x^3 dx = 0$$
> (odd integrand). So
> $$f_3 = x^2 - \frac{\sqrt{2}}{3}\cdot\frac{1}{\sqrt{2}} - 0 = x^2 - \frac{1}{3}.$$
>
> Normalize: $\|f_3\|^2 = \int_{-1}^1 (x^2 - 1/3)^2 dx = \int_{-1}^1 (x^4 - (2/3)x^2 + 1/9)dx = 2/5 - (2/3)(2/3) + (2)(1/9) = 2/5 - 4/9 + 2/9 = 2/5 - 2/9$.
>
> Common denominator $45$: $18/45 - 10/45 = 8/45$. So $\|f_3\| = \sqrt{8/45}$, and $e_3 = f_3/\sqrt{8/45} = (x^2 - 1/3)\sqrt{45/8}$.

**Step 5: $f_4 = x^3 - (3/5)x$ and $e_4 = (x^3 - (3/5)x)\sqrt{175/8}$.**

> [!note]- Derivation
> Project $v_4 = x^3$ onto $\operatorname{span}(e_1, e_2, e_3)$:
> $$\langle x^3, e_1\rangle = \frac{1}{\sqrt{2}}\int_{-1}^1 x^3 dx = 0 \quad \text{(odd)}.$$
> $$\langle x^3, e_2\rangle = \sqrt{3/2}\int_{-1}^1 x^4 dx = \sqrt{3/2}\cdot \frac{2}{5} = \frac{2}{5}\sqrt{3/2}.$$
> $$\langle x^3, e_3\rangle = \sqrt{45/8}\int_{-1}^1 x^3(x^2 - 1/3) dx = \sqrt{45/8}\left(\int_{-1}^1 x^5 dx - (1/3)\int_{-1}^1 x^3 dx\right) = 0$$
> (both integrands odd).
>
> So
> $$f_4 = x^3 - \frac{2}{5}\sqrt{3/2}\cdot \sqrt{3/2}\, x = x^3 - \frac{2}{5}\cdot \frac{3}{2}\, x = x^3 - \frac{3}{5}x.$$
>
> Normalize: $\|f_4\|^2 = \int_{-1}^1 (x^3 - (3/5)x)^2 dx = \int_{-1}^1 (x^6 - (6/5)x^4 + (9/25)x^2) dx = 2/7 - (6/5)(2/5) + (9/25)(2/3) = 2/7 - 12/25 + 6/25 = 2/7 - 6/25$.
>
> Common denominator $175$: $50/175 - 42/175 = 8/175$. So $\|f_4\| = \sqrt{8/175}$, and $e_4 = f_4/\sqrt{8/175} = (x^3 - (3/5)x)\sqrt{175/8}$.

**Step 6: Verify the $f_k$'s are scalar multiples of Legendre polynomials.**

The classical Legendre polynomials are $P_0(x) = 1$, $P_1(x) = x$, $P_2(x) = (3x^2 - 1)/2$, $P_3(x) = (5x^3 - 3x)/2$. We check that our $f_k$'s match these up to constants.

> [!note]- Derivation
> - $f_1 = 1 = P_0$. ✓
> - $f_2 = x = P_1$. ✓
> - $f_3 = x^2 - 1/3 = (3x^2 - 1)/3 = (2/3) \cdot P_2(x)$. So $f_3 = (2/3) P_2$. ✓
> - $f_4 = x^3 - (3/5)x = (5x^3 - 3x)/5 = (2/5) P_3(x)$. So $f_4 = (2/5) P_3$. ✓
>
> The un-normalized Gram-Schmidt outputs $f_k$ are scalar multiples of the Legendre polynomials. The normalization conventions differ — Legendre's $P_n(1) = 1$ versus our $\|e_n\| = 1$ — but the orthogonality structure is identical.

> [!note]- Complete formal solution
> Apply [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] to $1, x, x^2, x^3$ in $\mathcal{P}(\mathbb{R})$ with $\langle p, q\rangle = \int_{-1}^1 pq$. By parity, odd monomials are orthogonal to even monomials.
>
> $f_1 = 1$, $\|f_1\| = \sqrt{2}$, $e_1 = 1/\sqrt{2}$.
>
> $f_2 = x$ (the projection of $x$ onto $\operatorname{span}(1)$ vanishes by parity), $\|f_2\| = \sqrt{2/3}$, $e_2 = x\sqrt{3/2}$.
>
> $f_3 = x^2 - 1/3$ (after projecting onto $e_1$; the projection onto $e_2$ vanishes by parity), $\|f_3\|^2 = 8/45$, $e_3 = (x^2 - 1/3)\sqrt{45/8}$.
>
> $f_4 = x^3 - (3/5)x$ (after projecting onto $e_2$; projections onto $e_1, e_3$ vanish by parity), $\|f_4\|^2 = 8/175$, $e_4 = (x^3 - (3/5)x)\sqrt{175/8}$.
>
> Comparing to Legendre polynomials $P_0 = 1, P_1 = x, P_2 = (3x^2 - 1)/2, P_3 = (5x^3 - 3x)/2$:
> - $f_1 = P_0$, $f_2 = P_1$, $f_3 = (2/3)P_2$, $f_4 = (2/5)P_3$.
>
> The Gram-Schmidt outputs $f_k$ are scalar multiples of the Legendre polynomials. The Legendre normalization $P_n(1) = 1$ differs from the $L^2$-normalization $\|e_n\| = 1$. $\blacksquare$

---

# Key Takeaways

**Gram-Schmidt applied to monomials produces classical orthogonal polynomials.** The Legendre polynomials are *the* orthogonal polynomials on $[-1, 1]$ with weight $1$, in the sense that they are obtained by Gram-Schmidting $1, x, x^2, x^3, \dots$ with the inner product $\int_{-1}^1 fg$. Different weights give different classical families: weight $e^{-x^2}$ on $\mathbb{R}$ gives **Hermite polynomials** (with applications in the quantum harmonic oscillator); weight $(1 - x^2)^{-1/2}$ on $[-1, 1]$ gives **Chebyshev polynomials** (with applications in numerical analysis and polynomial approximation); weight $e^{-x}$ on $[0, \infty)$ gives **Laguerre polynomials** (with applications in the hydrogen atom). The transferable lesson: every classical orthogonal polynomial family is "Gram-Schmidt applied to monomials with a specific inner product".

**Parity is the structural simplification that makes the computation tractable.** Under the symmetric interval $[-1, 1]$ and the unweighted integral inner product, even and odd polynomials are orthogonal. This means Gram-Schmidt of $\{1, x, x^2, x^3\}$ effectively decomposes into Gram-Schmidt of $\{1, x^2\}$ (even) and $\{x, x^3\}$ (odd) — and these two halves do not interact. The transferable lesson: whenever the inner product respects a symmetry of the underlying space (parity, periodicity, rotation), the Gram-Schmidt procedure inherits the symmetry and can be carried out independently on the symmetric and antisymmetric [[Def - Subspace|subspaces]]. This pattern recurs whenever Gram-Schmidt is applied in a physics or signal-processing context.

**Different normalizations are common; what matters is orthogonality.** The Gram-Schmidt procedure produces $L^2$-orthonormal polynomials ($\|e_n\| = 1$), but the classical Legendre polynomials use a different normalization ($P_n(1) = 1$). The two conventions differ by scalar factors but agree on the *direction* of each polynomial in $\mathcal{P}(\mathbb{R})$. The orthogonality structure — which is what makes these polynomials useful — is preserved across normalizations. The transferable lesson: when comparing to classical results, identify the normalization being used; the "shape" (zeros, parity) is invariant, but specific numerical values depend on the normalization.

**The orthogonality of Legendre polynomials underlies many computational methods.** The Legendre polynomials are the basis for **Gauss-Legendre quadrature** — a high-accuracy numerical integration scheme that uses Legendre roots as quadrature nodes. They are also used in **spherical harmonics** expansions of functions on $S^2$ (which decompose into Legendre polynomials in the polar angle and Fourier modes in the azimuthal angle). And they are the basis for **Legendre series expansions** in many problems in classical physics involving the wave equation, heat equation, or potential theory on a sphere. The orthonormality property derived in this exercise is the technical foundation for all these applications. The transferable lesson: orthonormality is what makes a polynomial family computationally useful, and Gram-Schmidt is the systematic procedure for producing orthonormal families adapted to any inner product.
