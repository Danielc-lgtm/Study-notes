---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Differentiation Under the Integral Sign"
  - "Thm - Fubini's Theorem"
  - "Def - The Riemann Integral in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

For real parameters $b > a > 0$, evaluate the **Frullani integral**
$$I(a,b) = \int_0^\infty \frac{e^{-ax} - e^{-bx}}{x} \, dx.$$

The integrand is genuinely awkward — the factor $1/x$ obstructs any direct antiderivative, and at $x = 0$ the numerator also vanishes, so the integrand is bounded there but has no elementary primitive. Treat the integral as a function of the upper parameter $b$ and differentiate.

**Recall:**

![[Thm - Differentiation Under the Integral Sign#Statement]]

[[Thm - Differentiation Under the Integral Sign|Differentiation under the integral sign]]: if $F(t) = \int_R f(x,t)\,dx$ and $\partial_t f$ is continuous and dominated by a fixed integrable function $M(x)$ (uniformly for $t$ near the point of interest), then $F$ is differentiable and
$$F'(t) = \int_R \frac{\partial f}{\partial t}(x,t)\,dx.$$
On the unbounded domain $(0,\infty)$ the domination hypothesis — not mere continuity — is what licenses the interchange. An exponential bound $|\partial_t f| \leq C e^{-cx}$ supplies the dominating function.

---

# Convergent Strategy

**Problem class.** This is a *parameter-integral* evaluation: an integral with no elementary antiderivative, attacked by treating a parameter as the variable. The [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] is to differentiate in the parameter, obtain a tractable expression, and integrate the resulting differential equation.

**Assumption pattern.** The integrand carries a parameter $b$ in a position — the exponent of $e^{-bx}$ — where differentiating in $b$ is *simplifying*: $\partial_b e^{-bx} = -x\,e^{-bx}$, and the factor $x$ produced cancels the obstructing $1/x$. This is the recognizable signature of a Feynman-trick problem: a parameter whose derivative kills the hard part of the integrand.

**Theorem routing.** Set $F(b) = I(a,b)$. Differentiating under the integral sign, $F'(b) = \int_0^\infty \partial_b\big(\frac{e^{-ax}-e^{-bx}}{x}\big)\,dx = \int_0^\infty e^{-bx}\,dx = 1/b$ — the $1/x$ is gone and the integral is elementary. Integrating the differential equation $F'(b) = 1/b$ gives $F(b) = \ln b + C$; the constant is fixed by the known value $F(a) = I(a,a) = 0$.

**Key decision point.** Two non-obvious points. First, *which* parameter to differentiate in — $b$, because $e^{-bx}$ is the term whose $b$-derivative produces the cancelling factor $x$. Second, the domination check: on $(0,\infty)$ continuity of $\partial_b f$ is not enough; one must exhibit an integrable dominating function for $\partial_b f = e^{-bx}$, valid uniformly for $b$ in a neighbourhood — here $e^{-bx} \leq e^{-b_0 x}$ for $b \geq b_0 > 0$, and $e^{-b_0 x}$ is integrable on $(0,\infty)$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Differentiate under the integral sign to introduce a differential equation.** $F(b) = I(a,b)$ is differentiated in $b$ to get $F'(b) = 1/b$.

2. **Verify the domination hypothesis.** $\partial_b f = e^{-bx}$ is dominated, uniformly for $b \geq b_0$, by the integrable $e^{-b_0 x}$.

3. **Solve the resulting differential equation and fix the constant.** $F'(b) = 1/b$ integrates to $\ln b + C$; the boundary value $F(a) = 0$ determines $C$.

---

# Hints

> [!note]- Hint 1
> Do not attack the integral directly — $1/x$ has no friendly antiderivative. Instead think of $I(a,b)$ as a function of one of its parameters. Which parameter, when you differentiate the integrand with respect to it, produces a factor that *cancels* the $1/x$?

> [!note]- Hint 2
> Differentiate with respect to $b$. The only $b$-dependent term is $-e^{-bx}/x$, and $\frac{\partial}{\partial b}\big(-\frac{e^{-bx}}{x}\big) = e^{-bx}$. The $1/x$ has vanished. So formally $F'(b) = \int_0^\infty e^{-bx}\,dx$.

> [!note]- Hint 3
> Before trusting that swap, you are on the unbounded domain $(0,\infty)$, so you need a dominating function for $\partial_b f = e^{-bx}$. For $b$ near a fixed $b_0 > 0$, bound $e^{-bx} \leq e^{-b_0 x}$, and check $\int_0^\infty e^{-b_0 x}\,dx < \infty$.

> [!note]- Hint 4
> $\int_0^\infty e^{-bx}\,dx = 1/b$, so $F'(b) = 1/b$. Integrate: $F(b) = \ln b + C$. To find $C$, use a value of $b$ where you know $F$ outright — what is $I(a,a)$, when the two exponentials coincide?

---

# Solution

The factor $1/x$ blocks every direct approach, but differentiating in the parameter $b$ produces a factor of $x$ that cancels it. The integral becomes a one-line differential equation for $F(b) = I(a,b)$.

**Step 1: Set up the parameter integral and check domination.**

Let $F(b) = \int_0^\infty \frac{e^{-ax}-e^{-bx}}{x}\,dx$ with $a$ fixed. The integrand's $b$-partial $\partial_b f = e^{-bx}$ is dominated, for $b$ in a neighbourhood of any $b_0 > a$, by the integrable function $e^{-b_0 x}$.

> [!note]- Derivation
> Write $f(x,b) = \dfrac{e^{-ax} - e^{-bx}}{x}$. For fixed $x > 0$ this is differentiable in $b$, and only the second term depends on $b$:
> $$\frac{\partial f}{\partial b}(x,b) = \frac{\partial}{\partial b}\left( -\frac{e^{-bx}}{x} \right) = -\frac{1}{x}\cdot(-x)\,e^{-bx} = e^{-bx}.$$
> Note that $\partial_b f = e^{-bx}$ is continuous and — crucially — *free of the $1/x$ factor*. To invoke [[Thm - Differentiation Under the Integral Sign|differentiation under the integral sign]] on the *unbounded* domain $(0,\infty)$, continuity is not sufficient; a fixed integrable dominating function is required. Restrict attention to $b$ in an interval $[b_0, b_1]$ with $0 < b_0$. There, since $x > 0$,
> $$|\partial_b f(x,b)| = e^{-bx} \leq e^{-b_0 x} =: M(x),$$
> and $M$ is integrable on $(0,\infty)$: $\int_0^\infty e^{-b_0 x}\,dx = 1/b_0 < \infty$. So $\partial_b f$ is dominated by the integrable $M$, uniformly for $b \in [b_0, b_1]$, and differentiation under the integral sign is licensed on that interval. Since $b_0$ can be taken arbitrarily small and $b_1$ arbitrarily large, the rule holds for every $b > 0$.
>
> (At $x = 0$ the integrand $f(x,b)$ itself is bounded — $\frac{e^{-ax}-e^{-bx}}{x} \to b - a$ as $x \to 0^+$ by L'Hôpital — so there is no singularity at the lower endpoint; the only delicate region is $x \to \infty$, handled by the exponential domination.)

**Step 2: Differentiate — the $1/x$ cancels.**

$\displaystyle F'(b) = \int_0^\infty e^{-bx}\,dx = \frac{1}{b}$.

> [!note]- Derivation
> By Step 1, differentiation under the integral sign applies:
> $$F'(b) = \int_0^\infty \frac{\partial f}{\partial b}(x,b)\,dx = \int_0^\infty e^{-bx}\,dx.$$
> This integral is elementary. For $b > 0$,
> $$\int_0^\infty e^{-bx}\,dx = \left[ -\frac{1}{b}e^{-bx} \right]_{x=0}^{x=\infty} = 0 - \left(-\frac{1}{b}\right) = \frac{1}{b}.$$
> So $F'(b) = 1/b$. The obstructing $1/x$ is gone: differentiating in $b$ multiplied the integrand by $x$ (and a sign), exactly cancelling the denominator.

**Step 3: Integrate the differential equation.**

$F(b) = \ln b + C$ for some constant $C$.

> [!note]- Derivation
> The relation $F'(b) = 1/b$ is a differential equation for $F$ as a function of $b$ (with $a$ held fixed). Integrating,
> $$F(b) = \int \frac{1}{b}\,db = \ln b + C,$$
> where $C$ is a constant of integration — it may depend on the fixed parameter $a$, so write $C = C(a)$.

**Step 4: Fix the constant using a known value.**

At $b = a$ the integrand vanishes identically, so $F(a) = 0$; hence $C(a) = -\ln a$ and $F(b) = \ln(b/a)$.

> [!note]- Derivation
> Evaluate $F$ at the special value $b = a$. Then the two exponentials coincide, $e^{-ax} - e^{-ax} = 0$, so the integrand is identically zero and
> $$F(a) = \int_0^\infty \frac{e^{-ax} - e^{-ax}}{x}\,dx = \int_0^\infty 0\,dx = 0.$$
> Substituting $b = a$ into $F(b) = \ln b + C(a)$ gives $0 = \ln a + C(a)$, so $C(a) = -\ln a$. Therefore
> $$F(b) = \ln b - \ln a = \ln\frac{b}{a},$$
> that is,
> $$I(a,b) = \int_0^\infty \frac{e^{-ax} - e^{-bx}}{x}\,dx = \ln\frac{b}{a}. \qquad \blacksquare$$
>
> *Sanity checks.* The answer is positive when $b > a$, consistent with $e^{-ax} > e^{-bx}$ making the integrand positive. It vanishes at $b = a$. And it is antisymmetric, $I(a,b) = -I(b,a)$, as the integrand's antisymmetry under swapping $a, b$ demands.

> [!note]- Complete formal solution
> Fix $a > 0$ and set $F(b) = \int_0^\infty \frac{e^{-ax}-e^{-bx}}{x}\,dx$ for $b > 0$. The integrand is bounded near $x = 0$ (its limit there is $b - a$) and the $b$-partial is $\partial_b f = e^{-bx}$, which for $b \geq b_0 > 0$ satisfies $e^{-bx} \leq e^{-b_0 x}$ with $\int_0^\infty e^{-b_0 x}\,dx = 1/b_0 < \infty$. So $\partial_b f$ is dominated by an integrable function and [[Thm - Differentiation Under the Integral Sign|differentiation under the integral sign]] gives
> $$F'(b) = \int_0^\infty e^{-bx}\,dx = \frac{1}{b}.$$
> Hence $F(b) = \ln b + C$. Since $F(a) = \int_0^\infty \frac{e^{-ax}-e^{-ax}}{x}\,dx = 0$, the constant is $C = -\ln a$, and
> $$I(a,b) = F(b) = \ln(b/a). \qquad \blacksquare$$

---

# Key Takeaways

**The Feynman trick: when an integral resists, differentiate in a parameter chosen so the derivative simplifies the integrand.** The whole method is to read the integral as a function $F$ of a parameter, differentiate, discover that $F'$ is a *tractable* integral, solve the resulting differential equation, and pin the constant with a known value of $F$. The art is in the choice of parameter: pick the one whose derivative *attacks the obstruction*. Here the obstruction is the $1/x$, and differentiating $e^{-bx}$ in $b$ produces a factor $x$ that cancels it exactly. The trigger to reach for this technique is an integrand containing a parameter in a "soft" position — an exponent, a power, a coefficient — such that differentiating there visibly simplifies the integrand; and if the integral carries *no* parameter, the move is to *manufacture* one (write the integrand as itself evaluated at a parameter value, e.g. $\frac{e^{-ax}-e^{-bx}}{x} = \int_a^b e^{-tx}\,dt$, which is this same problem in disguise via Fubini).

**On an unbounded domain the domination hypothesis is the real content — continuity is not enough.** Differentiation under the integral sign is an interchange of a derivative and an integral, and on $(0,\infty)$ it can fail without a fixed integrable dominating function for $\partial_b f$. The discipline is to *name the dominating function before swapping*: here $e^{-bx} \leq e^{-b_0 x}$ for $b \geq b_0$, and $e^{-b_0 x}$ is integrable. Exponential decay is the most common supplier of domination, which is why parameter integrals involving $e^{-bx}$, $e^{-bx^2}$, or $e^{-b|x|}$ are the natural habitat of this technique. Skipping the domination check is the standard error — it works often enough to be tempting and fails exactly when mass escapes to infinity, so the safe habit is to exhibit $M(x)$ explicitly every time the domain is unbounded.

**The constant of integration is recovered from a degenerate value of the parameter.** Solving $F'(b) = 1/b$ gives $F$ only up to a constant; the constant is fixed by evaluating $F$ at a parameter value where the integral becomes trivial. The reliable choice is a *degenerate* value — here $b = a$, where the two exponentials cancel and the integrand is identically zero. This is general: after integrating the differential equation, look for a parameter value at which the integrand vanishes, or telescopes, or reduces to a known integral, and read off the constant there. The technique is incomplete without this step — the differential equation alone determines $F$ only up to an additive constant, and the boundary value is what makes the answer definite.
