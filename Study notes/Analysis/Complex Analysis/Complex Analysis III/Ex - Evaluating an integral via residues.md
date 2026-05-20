---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Residue Theorem"
  - "Thm - Real Rational Integrals via Residues"
  - "Thm - Computing Residues"
tags: [analysis, complex-analysis]
---

# Problem Statement

Evaluate
$$\int_{-\infty}^\infty \frac{dx}{1 + x^2}$$
by the residue theorem, and verify the answer is $\pi$.

**Recall:**

![[Thm - Real Rational Integrals via Residues#Notation]]

For $P/Q$ rational with $\deg Q \geq \deg P + 2$ and $Q$ having no real zeros, $\int_{-\infty}^\infty P/Q\,dx = 2\pi i \sum_{\operatorname{Im} w > 0}\operatorname{Res}_w(P/Q)$.

---

# Convergent Strategy

**Problem class:** Real integral evaluation by closing the real-axis contour with a large upper semicircle. The integrand decays fast enough at infinity that the semicircle contribution vanishes.

**Assumption pattern:** $1/(1 + x^2)$ is rational, $\deg Q - \deg P = 2 \geq 2$ (satisfies the decay condition), and $1 + x^2$ has no real zeros (its zeros are $\pm i$). All conditions for the rational integrals theorem are met.

**Theorem routing:** [[Thm - Real Rational Integrals via Residues|rational integrals via residues]] with $P = 1, Q = 1 + z^2$. Identify upper-half-plane poles, compute their residues, multiply by $2\pi i$.

**Key decision point:** Close in the upper or lower half-plane? Either works; convention is upper. The upper-half-plane pole is at $z = i$, the lower at $z = -i$.

---

# Legal Operations Used

1. **Extend $1/(1+x^2)$ to $f(z) = 1/(1 + z^2)$**, holomorphic on $\mathbb{C}\setminus\{\pm i\}$.
2. **Form the closed contour** $\Gamma_R = [-R, R] \cup C_R$, upper semicircle.
3. **Apply the residue theorem** to $\Gamma_R$.
4. **Bound the semicircle integral** by ML estimate.
5. **Take $R \to \infty$** to obtain the real-axis integral.

---

# Hints

> [!note]- Hint 1
> $1 + z^2 = (z - i)(z + i)$, so poles at $z = \pm i$. Only $z = i$ is in the upper half-plane.

> [!note]- Hint 2
> Compute $\operatorname{Res}_i 1/(1 + z^2)$ using the simple-pole formula: $1/(z + i)|_{z = i} = 1/(2i)$.

> [!note]- Hint 3
> Apply the residue theorem: $\oint_{\Gamma_R} dz/(1+z^2) = 2\pi i \cdot 1/(2i) = \pi$.

> [!note]- Hint 4
> Show the semicircle integral vanishes: $|1/(1+z^2)| \leq 1/(R^2 - 1)$ on $|z| = R$, and length is $\pi R$, so $|\int_{C_R}| \leq \pi R/(R^2 - 1) \to 0$.

---

# Solution

**Step 1: Set up the contour and identify the upper-half-plane poles**

The function $f(z) = 1/(1 + z^2) = 1/((z - i)(z + i))$ has simple poles at $z = \pm i$. Only $z = i$ is in the upper half-plane.

Close the real axis with the upper semicircle $C_R = \{|z| = R, \operatorname{Im} z \geq 0\}$, oriented counterclockwise, giving the contour $\Gamma_R = [-R, R] \cup C_R$.

**Step 2: Apply the residue theorem**

> [!note]- Derivation
> For $R > 1$, the contour $\Gamma_R$ encloses only the pole $z = i$. By [[Thm - Residue Theorem|the residue theorem]],
> $$\oint_{\Gamma_R} \frac{dz}{1 + z^2} = 2\pi i \cdot \operatorname{Res}_i \frac{1}{1 + z^2}.$$
>
> Compute the residue: $\operatorname{Res}_i 1/(1 + z^2) = \lim_{z \to i}(z - i)/((z - i)(z + i)) = 1/(2i)$. So $\oint_{\Gamma_R} dz/(1 + z^2) = 2\pi i \cdot 1/(2i) = \pi$.

**Step 3: Bound the semicircle contribution**

> [!note]- Derivation
> On $|z| = R$, $|1 + z^2| \geq |z|^2 - 1 = R^2 - 1$ for $R > 1$, so $|1/(1 + z^2)| \leq 1/(R^2 - 1)$. By the ML estimate:
> $$\left|\int_{C_R}\frac{dz}{1 + z^2}\right| \leq \pi R \cdot \frac{1}{R^2 - 1} = \frac{\pi R}{R^2 - 1} \to 0 \text{ as } R \to \infty.$$

**Step 4: Take $R \to \infty$**

> [!note]- Derivation
> Decomposing $\oint_{\Gamma_R} = \int_{-R}^R + \int_{C_R}$:
> $$\int_{-R}^R \frac{dx}{1 + x^2} + \int_{C_R}\frac{dz}{1 + z^2} = \pi.$$
> Sending $R \to \infty$, the semicircle term vanishes:
> $$\int_{-\infty}^\infty \frac{dx}{1 + x^2} = \pi.$$

> [!note]- Complete formal solution
> Let $f(z) = 1/(1 + z^2)$, which has simple poles at $z = \pm i$. Define the contour $\Gamma_R = [-R, R] \cup C_R$, where $C_R$ is the upper semicircle $|z| = R, \operatorname{Im} z \geq 0$, oriented counterclockwise.
>
> For $R > 1$, $\Gamma_R$ encloses only the pole $z = i$. By the residue theorem:
> $$\oint_{\Gamma_R} f(z)\,dz = 2\pi i \cdot \operatorname{Res}_i f = 2\pi i \cdot \frac{1}{2i} = \pi,$$
> using $\operatorname{Res}_i f = 1/(z + i)|_{z = i} = 1/(2i)$.
>
> The semicircle contribution: $|f(z)| \leq 1/(R^2 - 1)$ on $|z| = R$, so by ML, $|\int_{C_R} f\,dz| \leq \pi R/(R^2 - 1) \to 0$.
>
> Letting $R \to \infty$, the real-axis integral converges to the desired value:
> $$\int_{-\infty}^\infty \frac{dx}{1 + x^2} = \pi. \quad\blacksquare$$
>
> *Verification via real-variable calculus:* $\int dx/(1 + x^2) = \arctan x$, so $\int_{-\infty}^\infty dx/(1 + x^2) = \arctan(\infty) - \arctan(-\infty) = \pi/2 - (-\pi/2) = \pi$. ✓

---

# Key Takeaways

**The standard real-integral-via-residues recipe in four steps.** (1) Extend the real integrand to a meromorphic function on $\mathbb{C}$. (2) Close the contour with a large semicircle. (3) Apply the residue theorem, summing residues of upper-half-plane poles. (4) Verify the semicircle vanishes by ML estimate. This recipe handles all rational integrals with $\deg Q \geq \deg P + 2$.

**Trigger-reaction pattern — "integrate a rational function over $\mathbb{R}$" → "find upper-half-plane poles, sum residues".** The pattern is so automatic for rational integrands that one barely thinks about the contour anymore: identify poles, compute residues, multiply by $2\pi i$.

**Sanity-check via real-variable evaluation when possible.** For simple integrands like $1/(1 + x^2)$, the real-variable answer ($\arctan$) is known; verifying the contour-integral answer against it builds confidence in the technique. This sanity check is essential when learning, but later one trusts the residue theorem for harder integrals where the real-variable approach fails.

**The choice of upper vs lower semicircle is arbitrary for rational integrands; the answers agree.** Closing in the lower half-plane (clockwise) would give $-2\pi i \cdot \operatorname{Res}_{-i} f = -2\pi i \cdot (-1/(2i)) = \pi$. Same answer. The sum of upper-half and lower-half residues is the negative of the residue at infinity (which is $0$ here), so the choice is consistent.
