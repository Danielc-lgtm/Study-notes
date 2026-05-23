---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The BPST Instanton"
  - "Def - Gauge-Covariant Derivative"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Problem Statement

Compute the **$SU(2)$ holonomy** of the BPST instanton

$$A = \frac{\rho^2}{\rho^2 + r^2}\, g^{-1}dg, \qquad g(x) = \frac{x_0 - i\vec\sigma\cdot\vec x}{r},$$

around a circle in the equatorial plane $\{x : x_2 = x_3 = 0, x_0^2 + x_1^2 = R^2\}$ of radius $R$, parameterised as $x_0 = R\cos\theta$, $x_1 = R\sin\theta$, $x_2 = x_3 = 0$, with $\theta \in [0, 2\pi)$. The holonomy is

$$\operatorname{Hol}_C(A) = \mathcal{P}\exp\left(-\oint_C A\right),$$

where $\mathcal{P}\exp$ is the path-ordered exponential.

Specifically:
(a) Compute the pullback of $A$ to the loop $C$, expressing it as $A|_C = f(R, \theta)\, d\theta \cdot (\text{some }\mathfrak{su}(2)\text{ element})$.
(b) Compute the holonomy in the limit $R \to \infty$ (the loop at infinity), where $A \to g^{-1}dg$ is pure gauge.
(c) Compute the holonomy in the limit $R \to 0$ (a small loop near the centre), where $A \to 0$.
(d) Compute the holonomy at finite $R$ and discuss its dependence on $R/\rho$.

**Recall:**

![[Def - The BPST Instanton#The Definition]]

The **holonomy** of a connection $A$ around a smooth loop $C : [0, 1] \to M$ is the parallel-transport map $\operatorname{Hol}_C(A) \in G$ obtained by solving $d\psi/dt + A(\dot C)\psi = 0$ along $C$ with $\psi(0) = e_C(0)$, returning to $\psi(1) = \operatorname{Hol}_C(A)\cdot e_C(0)$. For $G$ non-abelian, the formal solution is the path-ordered exponential $\operatorname{Hol}_C(A) = \mathcal{P}\exp(-\oint_C A)$.

For a contractible loop, the holonomy depends on the field strength enclosed (via a Stokes-type theorem) and reduces to the abelian formula $\operatorname{Hol}(A) = \exp(-\int_\Sigma F)$ when the gauge field is abelian.

---

# Convergent Strategy

**Problem class.** This is a *holonomy computation* exercise — given an explicit gauge connection and an explicit loop, compute the parallel-transport operator. The general technique is to set up the ODE $d\psi/dt + A(\dot C)\psi = 0$ along the loop and solve it.

**Assumption pattern.** Three structural inputs combine: (a) the explicit BPST formula; (b) a specific loop $C$ (here, an equatorial circle); (c) the path-ordered-exponential framework for solving the holonomy ODE.

**Theorem routing.** The route: (1) parameterise the loop and compute $A(\dot C)$ explicitly along it; (2) recognise that for this specific loop, the gauge generator $A(\dot C)$ is *constant in $\theta$* — a special simplification owing to the $SO(2)$ symmetry of the equatorial-plane loop; (3) the path-ordered exponential then reduces to an ordinary matrix exponential, evaluable explicitly.

**Key decision point.** The non-obvious choice is to exploit the *symmetry* of the loop: the equatorial circle is invariant under the $SO(2)$ rotation in the $(x_0, x_1)$ plane, and the gauge potential pulled back to the circle inherits this symmetry. As a result, $A(\dot C)$ is constant in $\theta$, and the path-ordered exponential collapses to an ordinary exponential. For a generic loop (not symmetric), the holonomy would require numerically integrating the ODE.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory IV — Yang–Mills Fields and Instantons#Legal Operations|the topic page's Legal Operations]]:

1. **Compute $g^{-1}dg$ via the explicit matrix derivative** (operation 6). The Maurer–Cartan form computed in [[Ex - Computing the Field Strength of the BPST Instanton]] is the starting point.

2. **Use the trace pairing on the Lie algebra as an inner product** (operation 5). Used to compute the squared norm $|A|^2$ along the loop and to identify the holonomy as a rotation in $SU(2)$.

---

# Hints

> [!note]- Hint 1
> Along the loop $C$, $r = R$ (constant) and $x = (R\cos\theta, R\sin\theta, 0, 0)$. Compute $g(x)$ and $g^{-1}(x)$ explicitly, then $dg/d\theta$ and $A(\dot C) = g^{-1}(dg/d\theta)\cdot\rho^2/(\rho^2+R^2)$.

> [!note]- Hint 2
> $g(x) = (R\cos\theta - i\sigma_1 R\sin\theta)/R = \cos\theta - i\sigma_1\sin\theta = \exp(-i\sigma_1\theta)$. So $g$ along $C$ is a rotation by $\theta$ around the $\sigma_1$-axis in $SU(2)$.

> [!note]- Hint 3
> $g^{-1}(dg/d\theta) = \exp(i\sigma_1\theta)\cdot(-i\sigma_1)\exp(-i\sigma_1\theta) = -i\sigma_1$ (since $\sigma_1$ commutes with itself and with its exponentials). So $A(\dot C) = -i\sigma_1\cdot\rho^2/(\rho^2+R^2)$, *constant in $\theta$*. The holonomy is then $\operatorname{Hol}_C = \exp(-\oint A) = \exp(2\pi\cdot i\sigma_1\cdot\rho^2/(\rho^2+R^2))$.

---

# Solution

The strategy is to exploit the $SO(2)$ symmetry of the loop: $A(\dot C)$ turns out to be constant in $\theta$, so the path-ordered exponential collapses to an ordinary matrix exponential, computable explicitly.

**Step 1: Parameterise the loop and compute $g(x)$ along $C$.**

For $x = (R\cos\theta, R\sin\theta, 0, 0)$, $r = R$ (constant). So
$$g(x) = (x_0 - i\vec\sigma\cdot\vec x)/r = (R\cos\theta - i\sigma_1\cdot R\sin\theta)/R = \cos\theta\cdot I - i\sin\theta\cdot\sigma_1 = e^{-i\sigma_1\theta}.$$

So $g|_C$ is a rotation by $\theta$ around the $\sigma_1$-axis of $SU(2)$, varying as $\theta$ traces the loop.

> [!note]- Derivation
> Direct substitution: $x = (R\cos\theta, R\sin\theta, 0, 0)$ has $x_0 = R\cos\theta$ and $\vec x = (R\sin\theta, 0, 0) = R\sin\theta\cdot\hat e_1$. So $\vec\sigma\cdot\vec x = \sigma_1\cdot R\sin\theta$. And $r = |x| = \sqrt{R^2\cos^2\theta + R^2\sin^2\theta} = R$. Then $g = (R\cos\theta - i\sigma_1 R\sin\theta)/R = \cos\theta - i\sigma_1\sin\theta$. By the identity $e^{-i\sigma_1\theta} = \cos\theta - i\sigma_1\sin\theta$ (using $\sigma_1^2 = I$), this is $g = e^{-i\sigma_1\theta}$.

**Step 2: Compute $A(\dot C)$ along $C$.**

$g^{-1}(dg/d\theta) = -i\sigma_1$, so $A(\dot C) = (\rho^2/(\rho^2+R^2))(-i\sigma_1)$.

> [!note]- Derivation
> $g = e^{-i\sigma_1\theta}$, $g^{-1} = e^{+i\sigma_1\theta}$, $dg/d\theta = -i\sigma_1 e^{-i\sigma_1\theta}$. So $g^{-1}(dg/d\theta) = e^{i\sigma_1\theta}\cdot(-i\sigma_1)e^{-i\sigma_1\theta} = -i\sigma_1\cdot e^{i\sigma_1\theta}e^{-i\sigma_1\theta} = -i\sigma_1$ (using that $\sigma_1$ commutes with its own exponential).
>
> Hence $A(\dot C) d\theta = \rho^2/(\rho^2+R^2)\cdot(-i\sigma_1)\,d\theta$ along $C$.

**Step 3: Compute the holonomy.**

Since $A(\dot C)$ is constant in $\theta$ (with value $-i\sigma_1\cdot\rho^2/(\rho^2+R^2)$), the path-ordered exponential reduces to an ordinary exponential:
$$\operatorname{Hol}_C(A) = \exp\left(-\int_0^{2\pi}A(\dot C)\,d\theta\right) = \exp\left(-2\pi\cdot(-i\sigma_1)\cdot\frac{\rho^2}{\rho^2+R^2}\right) = \exp\left(2\pi i\sigma_1\cdot\frac{\rho^2}{\rho^2+R^2}\right).$$

In $SU(2)$ this is a rotation by angle $\alpha(R) = 2\pi\cdot\rho^2/(\rho^2+R^2)$ around the $\sigma_1$-axis.

> [!note]- Derivation
> The path-ordered exponential $\mathcal{P}\exp(-\int A) = \mathcal{P}\exp(\int_0^{2\pi}d\theta\cdot i\sigma_1\rho^2/(\rho^2+R^2))$. Since $i\sigma_1$ commutes with itself, the path ordering is irrelevant — it equals the ordinary integral $\int_0^{2\pi}d\theta = 2\pi$. So $\mathcal{P}\exp = \exp(2\pi i\sigma_1\cdot\rho^2/(\rho^2+R^2))$.
>
> In $SU(2)$, $\exp(i\sigma_1\alpha) = \cos\alpha\cdot I + i\sin\alpha\cdot\sigma_1$ — a rotation by angle $2\alpha$ around the $\sigma_1$-axis (using the standard $SU(2)$-as-rotations correspondence). Our $\alpha = 2\pi\rho^2/(\rho^2+R^2)$, so the rotation angle in $SU(2)$ is $2\alpha = 4\pi\rho^2/(\rho^2+R^2)$.

**Step 4: Limits.**

*$R \to \infty$ (large loop, asymptotic):* $\rho^2/(\rho^2+R^2) \to 0$, so $\alpha \to 0$ and $\operatorname{Hol}_C \to I$. *No holonomy at infinity*, consistent with the asymptotic pure-gauge configuration being globally trivial (a winding-1 map $g$ but evaluated on a *non-contractible* loop in $S^3_\infty$ — which the equatorial $S^1$ is).

Actually, wait — the equatorial circle $S^1 \subset S^3_\infty$ is *contractible* in $S^3$ (any loop on $S^3$ is contractible because $\pi_1(S^3) = 0$), so the holonomy at infinity must reduce to $\exp(-\int_{\text{disk}}F) = I$ since $F \to 0$. The vanishing of $\alpha$ in this limit is consistent.

*$R \to 0$ (small loop near centre):* $\rho^2/(\rho^2+R^2) \to 1$, so $\alpha \to 2\pi$ and $\operatorname{Hol}_C \to \exp(2\pi i\sigma_1) = \cos(2\pi)I + i\sin(2\pi)\sigma_1 = I$. *Hol also trivial.* This is because the loop encloses essentially zero flux (the field strength is concentrated near the centre but the small loop area $\pi R^2 \to 0$ as $R \to 0$).

*Intermediate $R$:* For $R = \rho$ (the natural scale), $\alpha = 2\pi\cdot(1/2) = \pi$, giving $\operatorname{Hol}_C = \exp(i\pi\sigma_1) = \cos\pi\cdot I + i\sin\pi\cdot\sigma_1 = -I$. So at the intersection of the natural scales, the holonomy is *minus the identity* — a non-trivial element of $SU(2)$.

> [!note]- Derivation
> Substituting $R$-values into $\alpha = 2\pi\rho^2/(\rho^2+R^2)$:
> - $R = 0$: $\alpha = 2\pi$, $\exp(2\pi i\sigma_1) = I$ (since $2\pi$ is the period of the exponential map on the imaginary line of $SU(2)$).
> - $R = \rho$: $\alpha = \pi$, $\exp(i\pi\sigma_1) = \cos\pi I + i\sin\pi\sigma_1 = -I$.
> - $R = \infty$: $\alpha = 0$, $\exp(0) = I$.
>
> The holonomy is a *non-monotone* function of $R$ on the BPST instanton, with peak deviation at $R \approx \rho$ (the instanton scale). This is the physical signature of the instanton: the holonomy "rotates by an angle proportional to the enclosed instanton density".

> [!note]- Complete formal solution
> *Setup.* Loop $C$: $x = (R\cos\theta, R\sin\theta, 0, 0)$ for $\theta \in [0, 2\pi)$. BPST $A = (\rho^2/(\rho^2+r^2))g^{-1}dg$, $g = (x_0 - i\vec\sigma\cdot\vec x)/r$.
>
> *Step 1.* Along $C$, $g = e^{-i\sigma_1\theta}$, a rotation around the $\sigma_1$-axis.
>
> *Step 2.* $g^{-1}(dg/d\theta) = -i\sigma_1$ (constant in $\theta$, by the abelian-subalgebra structure of $\langle\sigma_1\rangle$). So $A(\dot C) = -i\sigma_1\cdot\rho^2/(\rho^2+R^2)$.
>
> *Step 3.* Holonomy $\operatorname{Hol}_C = \exp(2\pi i\sigma_1\cdot\rho^2/(\rho^2+R^2)) = \cos\alpha\cdot I + i\sin\alpha\cdot\sigma_1$ with $\alpha = 2\pi\rho^2/(\rho^2+R^2)$.
>
> *Step 4.* Limits: $R \to 0 \Rightarrow I$. $R \to \infty \Rightarrow I$. $R = \rho \Rightarrow -I$ (centre of $SU(2)$). Generic $R$: a non-trivial rotation around the $\sigma_1$-axis.
>
> *Physical interpretation.* The holonomy of BPST around an equatorial circle is a function of $R/\rho$ that interpolates from $I$ at small $R$ (no enclosed flux), through $-I$ at $R = \rho$ (half-rotation, the centre of $SU(2)$ representing maximum "twist"), to $I$ at large $R$ (the asymptotic gauge transformation wraps trivially on the equatorial circle, which is contractible in $S^3$). $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to compute the holonomy by *non-abelian Stokes' theorem*: $\operatorname{Hol}_C = \exp(-\int_\Sigma F)$ for $\Sigma$ a disk bounding $C$. *This formula is wrong in non-abelian gauge theory* — the path-ordered exponential of a non-abelian gauge field around a loop does *not* equal the ordinary exponential of the surface integral. The error: in non-abelian theory, parallel transport at different points of the surface does not commute, so the integral $\int_\Sigma F$ is "ordered" in a sense that the formula does not capture. For BPST, the abelian-looking simplification works only because the gauge potential pulled back to the loop lies entirely in the *abelian* subalgebra $\langle\sigma_1\rangle$ — a coincidence of the specific loop geometry, not a general phenomenon.

---

# Key Takeaways

**Holonomy of a non-abelian gauge field is a path-ordered exponential.** Unlike the abelian case where $\operatorname{Hol}(A) = \exp(-\oint A)$, the non-abelian holonomy requires path-ordering: $\operatorname{Hol}(A) = \mathcal{P}\exp(-\oint A)$. The path-ordering accounts for the fact that gauge transformations at different points do not commute. *Only when the integrand lies in an abelian subalgebra throughout the loop* does the path-ordering trivialise to an ordinary exponential. The transferable lesson: for non-abelian holonomy computations, always check whether the loop has a symmetry that confines the gauge potential to an abelian subalgebra — if so, the calculation simplifies dramatically. If not, the holonomy must be computed by solving the ODE directly (typically numerically).

**The BPST holonomy on an equatorial circle is a non-monotone function of $R/\rho$.** The angle $\alpha(R) = 2\pi\rho^2/(\rho^2+R^2)$ starts at $2\pi$ for $R = 0$ (representing a full rotation, which is $I$ in $SU(2)$), decreases to $\pi$ at $R = \rho$ (representing the centre $-I$), and goes to $0$ at $R = \infty$ (representing $I$ again). The peak "deviation" from the identity occurs at the natural instanton scale $R = \rho$ — a physical signature of the instanton's localisation. The transferable principle: *non-trivial holonomy concentrates at the scale of the underlying field strength*. For soliton-type solutions, holonomy is a useful probe of the soliton's location and scale.

**The exponential map on $SU(2)$ has period $2\pi$ on each axis.** $\exp(2\pi i\sigma_a) = I$ for any Pauli matrix $\sigma_a$ — *not* the more naive $2\pi i$ period one might expect from the $U(1)$ case. This is because $\sigma_a$ has eigenvalues $\pm 1$, so $\exp(it\sigma_a)$ has eigenvalues $e^{\pm it}$, and the two eigenvalues simultaneously return to $1$ when $t = 2\pi$. The transferable principle: *exponential map periods on non-abelian groups depend on the spectrum of the generator*, not just on $2\pi$. For higher-rank groups like $SU(3)$, the exponential map has more complex periodicity behaviour depending on which Lie-algebra direction the generator points in.
