---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Characteristic Function"
  - "Ex - Differentiation under the integral sign"
tags: [probability, advanced-probability]
---

# Problem Statement

**(a)** Compute the [[Def - Characteristic Function|characteristic function]] of the standard Gaussian $N(0,1)$, confirming $\varphi(t)=e^{-t^2/2}$.

**(b)** Show that if $\mathbb{E}|X|^k<\infty$ then $\varphi_X\in C^k$ with $\varphi_X^{(k)}(0)=i^k\mathbb{E}[X^k]$ — moments are derivatives of $\varphi$ at $0$.

**(c)** Use the convolution-to-product property to show that a sum of independent Gaussians is Gaussian, with means and variances adding.

**Recall:**

![[Def - Characteristic Function#The Definition]]

---

# Convergent Strategy

**Problem class:** computing with characteristic functions — extracting moments, exploiting the product property.

**Assumption pattern:** (a) the Gaussian's characteristic function solves an ODE (differentiate, integrate by parts); (b) [[Ex - Differentiation under the integral sign|differentiation under the integral]] with the integrable dominator $|x|^k$; (c) independence $\Rightarrow$ characteristic functions multiply.

---

# Legal Operations Used

1. **Differentiate $\varphi$ under the integral** ([[Ex - Differentiation under the integral sign|DCT]]).
2. **Integration by parts** / an ODE for the Gaussian.
3. **$\varphi_{X+Y}=\varphi_X\varphi_Y$** for independent $X,Y$.

---

# Hints

> [!note]- Hint 1
> (a): $\varphi'(t)=\int ix\,e^{itx}g(x)\,dx$ where $g(x)=(2\pi)^{-1/2}e^{-x^2/2}$. Integrate by parts using $g'(x)=-xg(x)$ to get $\varphi'(t)=-t\varphi(t)$.

> [!note]- Hint 2
> (b): $|x|^k\in L^1(\mu_X)$ dominates the $k$-th $t$-derivative of $e^{itx}$; differentiate under the integral $k$ times, evaluate at $t=0$.

> [!note]- Hint 3
> (c): $\varphi_{X+Y}=\varphi_X\varphi_Y$; multiply the Gaussian exponentials.

---

# Solution

**Step 1 — (a) The Gaussian characteristic function.** With density $g(x)=(2\pi)^{-1/2}e^{-x^2/2}$, $\varphi(t)=\int e^{itx}g(x)\,dx$. Since $|x|$ is integrable against $g$, [[Ex - Differentiation under the integral sign|differentiate under the integral]]:
$$\varphi'(t)=\int ix\,e^{itx}g(x)\,dx=-i\int e^{itx}g'(x)\,dx=-i\big[\underbrace{e^{itx}g(x)}_{\to0}\big]_{-\infty}^\infty+i\int(it)e^{itx}g(x)\,dx=-t\,\varphi(t),$$
using $g'(x)=-xg(x)$ and integration by parts. The ODE $\varphi'=-t\varphi$ with $\varphi(0)=1$ solves to $\varphi(t)=e^{-t^2/2}$.

**Step 2 — (b) Moments as derivatives.** If $\mathbb{E}|X|^k<\infty$, then $|x|^k\in L^1(\mu_X)$ dominates $\partial_t^j e^{itx}=(ix)^je^{itx}$ for $j\le k$ (since $|(ix)^j|=|x|^j\le1+|x|^k$). By [[Ex - Differentiation under the integral sign|differentiation under the integral]] iterated $k$ times, $\varphi_X\in C^k$ and
$$\varphi_X^{(k)}(t)=\int(ix)^k e^{itx}\,d\mu_X(x),\qquad\text{so}\qquad\varphi_X^{(k)}(0)=\int(ix)^k\,d\mu_X=i^k\,\mathbb{E}[X^k].$$
Moments are read off the Taylor coefficients of $\varphi_X$ at $0$: $\varphi_X(t)=\sum_{j=0}^k\frac{i^j\mathbb{E}[X^j]}{j!}t^j+o(t^k)$.

**Step 3 — (c) Sum of independent Gaussians.** Let $X\sim N(m_1,\sigma_1^2)$, $Y\sim N(m_2,\sigma_2^2)$ independent. Their characteristic functions are $\varphi_X(t)=e^{im_1t-\sigma_1^2t^2/2}$, $\varphi_Y(t)=e^{im_2t-\sigma_2^2t^2/2}$. By the [[Def - Characteristic Function|convolution-to-product property]],
$$\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)=e^{i(m_1+m_2)t-(\sigma_1^2+\sigma_2^2)t^2/2}.$$
This is the characteristic function of $N(m_1+m_2,\sigma_1^2+\sigma_2^2)$; since [[Def - Characteristic Function|characteristic functions determine laws]], $X+Y\sim N(m_1+m_2,\sigma_1^2+\sigma_2^2)$ — the Gaussian family is closed under independent sums, with means and variances adding.

> [!note]- Complete formal solution
> (a) Differentiating under the integral and integrating by parts with $g'=-xg$ gives $\varphi'=-t\varphi$, $\varphi(0)=1$, so $\varphi(t)=e^{-t^2/2}$. (b) $|x|^k\in L^1(\mu_X)$ dominates the derivatives of $e^{itx}$; differentiating under the integral $k$ times and setting $t=0$ gives $\varphi_X^{(k)}(0)=i^k\mathbb{E}[X^k]$. (c) $\varphi_{X+Y}=\varphi_X\varphi_Y=e^{i(m_1+m_2)t-(\sigma_1^2+\sigma_2^2)t^2/2}$, so $X+Y\sim N(m_1+m_2,\sigma_1^2+\sigma_2^2)$. $\blacksquare$

---

# Key Takeaways

**The characteristic function packages a law into a function from which moments fall out as derivatives at $0$ ($\varphi^{(k)}(0)=i^k\mathbb{E}[X^k]$) and independent sums become products.** These two properties are the entire reason characteristic functions exist. Moments-as-derivatives is the Fourier "smoothness $\leftrightarrow$ decay" duality, established by [[Ex - Differentiation under the integral sign|differentiation under the integral]]; it is the device that makes the [[Thm - Central Limit Theorem|CLT]] computation — Taylor-expand $\varphi_X$ to second order — possible.

**[[Def - Convolution|Convolution]] becoming multiplication is what makes characteristic functions the natural tool for sums of independent variables.** The law of a sum is a [[Ex - Independence and the factorisation of expectation|convolution]], intractable directly; $\varphi_{X+Y}=\varphi_X\varphi_Y$ turns it into a product. "Sum of independent Gaussians is Gaussian" is then one line of multiplying exponentials — and the same factorisation, applied to $n$ identical copies and Taylor-expanded, *is* the proof of the [[Thm - Central Limit Theorem|central limit theorem]]. The Gaussian's special role is its self-dual characteristic function $e^{-t^2/2}$, whose logarithm is exactly quadratic.
