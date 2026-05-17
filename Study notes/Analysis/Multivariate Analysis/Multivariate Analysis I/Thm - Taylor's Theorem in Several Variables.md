---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Higher-Order Derivatives and Ck Maps"
  - "Thm - The Chain Rule"
  - "Thm - Schwarz's Theorem on Mixed Partials"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f : U \to \mathbb{R}$ scalar (the vector case reduces componentwise); $x_0 \in U$ and $h \in \mathbb{R}^n$ an increment with the segment $[x_0, x_0+h] \subseteq U$. A multi-index is $\alpha \in \mathbb{N}^n$ with $|\alpha| = \sum\alpha_j$, $\alpha! = \prod\alpha_j!$, $h^\alpha = \prod h_j^{\alpha_j}$, $\partial^\alpha = \partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$ (see [[Def - Higher-Order Derivatives and Ck Maps]]). The class $C^{k+1}(U)$ is defined there; $D^2 f(x_0)$ is the Hessian. The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Statement

> **Taylor's Theorem in Several Variables.** Let $U \subseteq \mathbb{R}^n$ be open, $f \in C^{k+1}(U)$ with $k \ge 0$, and let $x_0 \in U$, $h \in \mathbb{R}^n$ with the segment from $x_0$ to $x_0 + h$ contained in $U$. Then
> $$f(x_0 + h) = \sum_{\substack{\alpha \in \mathbb{N}^n \\ |\alpha| \le k}} \frac{\partial^\alpha f(x_0)}{\alpha!}\, h^\alpha \;+\; R_{k+1}(x_0, h),$$
> where the **integral remainder** is
> $$R_{k+1}(x_0, h) = \int_0^1 (k+1)(1-t)^k \sum_{|\alpha| = k+1} \frac{\partial^\alpha f(x_0 + th)}{\alpha!}\, h^\alpha\, dt,$$
> and $R_{k+1}(x_0, h) = O(|h|^{k+1})$ as $h \to 0$.
>
> The degree-$k$ polynomial $P_k(h) = \sum_{|\alpha|\le k}\frac{\partial^\alpha f(x_0)}{\alpha!}h^\alpha$ is the **$k$-th order Taylor polynomial** of $f$ at $x_0$. The order-one and order-two terms are, explicitly, $\nabla f(x_0)\cdot h$ and $\frac12\,h\cdot D^2 f(x_0)\,h$, so
> $$f(x_0+h) = f(x_0) + \nabla f(x_0)\cdot h + \tfrac12\,h\cdot D^2 f(x_0)\,h + R_3(x_0,h).$$

---

# Motivation

A differentiable function is, near a point, well-approximated by an affine function — its first-order Taylor polynomial. But "well" here means only $o(|h|)$: the error shrinks faster than the displacement, and no more is promised. For many purposes this is too crude. To decide whether a critical point is a minimum or a maximum the linear term vanishes and you must see the *quadratic* term. To understand the leading behaviour of a function, to compute limits, to control errors quantitatively, you need approximation by polynomials of higher degree, with a *quantified* remainder. Taylor's theorem is that tool.

The one-variable Taylor theorem does exactly this: $f(x_0 + h) = \sum_{j\le k} \frac{f^{(j)}(x_0)}{j!}h^j + R_{k+1}$, polynomial approximation with an explicit remainder. The question is how it survives in $n$ variables, where a "$j$-th derivative" is no longer a single number but a whole family of partials.

The answer is the cleanest possible, and it is bought entirely with machinery already in hand. The deep idea is the universal move of the topic: **restrict to the segment**. Set $\varphi(t) = f(x_0 + th)$, a function of one real variable. The one-variable Taylor theorem applies to $\varphi$ verbatim. All that remains is to translate the derivatives of $\varphi$ back into derivatives of $f$ — and the chain rule does that, with $\varphi^{(j)}(t)$ turning out to be a sum, over all multi-indices $\alpha$ of length $j$, of $\partial^\alpha f$ times $h^\alpha$. The combinatorics of which multi-indices appear, and with what coefficients, is governed by the **multinomial theorem**, and the multinomial coefficient $j!/\alpha!$ is exactly what produces the clean factor $1/\alpha!$ in the final formula.

Two pieces of earlier machinery are silently essential. The **chain rule** is what computes $\varphi^{(j)}$. **Schwarz's theorem** is what makes the answer expressible in multi-index notation at all: $\varphi^{(j)}$ involves partials of $f$ taken in many orders, and only because those partials are order-independent (for a $C^k$ function) can they be collected by multi-index $\alpha$ rather than by ordered string. Taylor's theorem is the payoff of $\S1.3$: it is where higher derivatives, the $C^k$ classes, and Schwarz's theorem combine into a usable approximation.

The order-two term deserves its own billing. It is $\frac12 h\cdot D^2 f(x_0) h$, the quadratic form of the Hessian. When $x_0$ is a critical point the linear term vanishes and this quadratic form is the leading behaviour of $f - f(x_0)$ — so whether $f$ has a minimum, maximum, or saddle at $x_0$ is decided by the definiteness of the Hessian. This is the second-derivative test, and it is the launching point of the optimisation theory in **Multivariate Analysis II**.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f \in C^{k+1}$" (for the integral remainder; $C^k$ suffices for a Lagrange-type remainder).

The first disguised source is **$f$ is given by an elementary formula**. The property $B$ is "$f$ is built from polynomials, exponentials, trigonometric functions". The bridge is that such $f$ is $C^\infty$, so the theorem applies to any order $k$. *Example problem:* compute the degree-$2$ Taylor polynomial of any explicit smooth function.

The second disguised source is **$f$ is obtained by substituting a multivariate expression into a known one-variable function**. The property $B$ is "$f(x) = g(u(x))$ with $g$ a one-variable function of known Taylor series and $u$ a polynomial". The bridge is that one can substitute the known expansion of $g$ and collect terms by total degree — this is far faster than computing partials. *Example problem:* expand $\sqrt{1 + x - y^2}$ by substituting into the binomial series for $\sqrt{1+t}$ (see [[Ex - Second-order Taylor expansion of a function]]).

The third disguised source is **$f$ is $C^k$ but not $C^{k+1}$**. The property $B$ is "$f$ has continuous partials only up to order $k$". The bridge is the variant of the theorem (Proposition 2.1.5 in Taylor's text) holding for $C^k$ functions, with a remainder $R_k$ of size $o(|h|^k)$ involving differences $\partial^\alpha f(sx) - \partial^\alpha f(0)$. *Example problem:* a function known only to be $C^2$ still admits a second-order expansion with an $o(|h|^2)$ remainder.

**Targets (Output Amplification)**

The conclusion is the expansion $f(x_0+h) = P_k(h) + R_{k+1}$.

Combine the conclusion with **$x_0$ being a critical point**. If $\nabla f(x_0) = 0$, the linear term vanishes and $f(x_0+h) - f(x_0) = \frac12 h\cdot D^2 f(x_0)h + O(|h|^3)$. The further result $E$: the sign of $f - f(x_0)$ near $x_0$ is governed by the definiteness of the Hessian — positive definite gives a local minimum, negative definite a maximum, indefinite a saddle. This is the **second-derivative test**, nonobvious because a *local* extremum question is answered by the *eigenvalues* of a matrix.

Combine the conclusion with **the uniqueness of the Taylor polynomial**. Any degree-$k$ polynomial $P$ with $f(x_0+h) - P(h) = o(|h|^k)$ has exactly the Taylor coefficients $\partial^\alpha f(x_0)/\alpha!$ (this is Corollary 2.1.4 / 10.34 in the sources). The further result $E$: one can read off all partials of $f$ up to order $k$ from *any* good polynomial approximation, however obtained — by substitution, by series manipulation — without computing a single partial. The combination is nonobvious because it inverts the theorem: the expansion determines the derivatives.

Combine the conclusion with **the explicit remainder bound**. The integral remainder yields $|R_{k+1}| \le C|h|^{k+1}\sup_{|\alpha|=k+1}|\partial^\alpha f|$. The further result $E$: a *quantitative* error bound for the polynomial approximation, the input to numerical-analysis error estimates and to convergence proofs for power series. The combination is useful because it converts the qualitative "$o$" into a usable inequality.

---

# Why Is It True

The whole theorem is the one-variable Taylor theorem viewed through a single moving point.

The function $f$ near $x_0$ is an object on an $n$-dimensional domain, which is hard to expand directly. So do not. Pick the direction $h$ and walk along the straight segment $t \mapsto x_0 + th$, $t \in [0,1]$. Along this segment $f$ becomes the one-variable function $\varphi(t) = f(x_0 + th)$, and $f(x_0 + h)$ is just $\varphi(1)$. The one-variable Taylor theorem expands $\varphi(1)$ around $\varphi(0)$:
$$\varphi(1) = \varphi(0) + \varphi'(0) + \tfrac12\varphi''(0) + \cdots + \tfrac1{k!}\varphi^{(k)}(0) + (\text{remainder}).$$
This is already the theorem in disguise — $\varphi(1) = f(x_0+h)$, $\varphi(0) = f(x_0)$. Everything left is translating $\varphi^{(j)}(0)$ into the language of $f$.

That translation is the chain rule. Differentiating $\varphi(t) = f(x_0 + th)$ once: the inner map is $t \mapsto x_0 + th$ with velocity $h$, so $\varphi'(t) = \nabla f(x_0+th)\cdot h = \sum_j \partial_j f(x_0+th)\,h_j$. Differentiating again applies the chain rule to each $\partial_j f$, producing $\varphi''(t) = \sum_{j,\ell}\partial_\ell\partial_j f\,h_j h_\ell$. Inductively, $\varphi^{(j)}(t)$ is a sum over all *ordered* strings of $j$ indices of a $j$-th partial of $f$ times the corresponding product of components of $h$.

Now the key combinatorial fact, and the reason multi-index notation appears. The function $f$ is $C^k$, so by [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]] those $j$-th partials do not care about the order of differentiation — they depend only on *how many times each variable is differentiated*, i.e. only on the multi-index $\alpha$ with $|\alpha| = j$. So collect the ordered strings by their multi-index. The number of ordered strings that collapse to a given $\alpha$ is the multinomial coefficient $j!/\alpha!$ — the same count that appears in expanding $(h_1 + \cdots + h_n)^j$. Therefore
$$\varphi^{(j)}(t) = \sum_{|\alpha|=j}\frac{j!}{\alpha!}\,\partial^\alpha f(x_0+th)\,h^\alpha,$$
and dividing by $j!$ (as the Taylor formula does) cancels the $j!$ and leaves the clean coefficient $1/\alpha!$. Summing over $j \le k$ gives the multi-index Taylor polynomial; the one-variable remainder, translated the same way, gives the integral remainder.

One should *expect* the theorem to look exactly like this, because the only genuinely new ingredients over the one-variable case are (i) the chain rule, which converts $\frac{d}{dt}$ into a directional derivative, and (ii) the multinomial theorem, which is pure algebra. The depth is in $\S1.3$'s earlier results — Schwarz's theorem in particular — which is what permits the order-blind multi-index bookkeeping. Take those for granted and Taylor's theorem in $n$ variables is *literally* Taylor's theorem in one variable.

---

# What Makes This Hard

The conceptual step — restrict to the segment, $\varphi(t) = f(x_0+th)$, and quote one-variable Taylor — is short and clean; the genuine difficulty is the **combinatorics of the higher derivatives of $\varphi$**. Computing $\varphi^{(j)}$ and recognising that it equals $\sum_{|\alpha|=j}\frac{j!}{\alpha!}\partial^\alpha f\,h^\alpha$ requires both the chain rule applied $j$ times and the multinomial counting argument, and the multinomial coefficient $j!/\alpha!$ — which is exactly what cancels against the $1/j!$ to leave $1/\alpha!$ — is the step most people get wrong. A second subtlety: collecting partials by multi-index is legal *only* because the function is $C^k$, so [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]] makes them order-independent; forgetting that the multi-index notation silently depends on Schwarz is a common conceptual gap.

---

# Rederivation Scaffold

**High-level strategy:**
Restrict $f$ to the segment, $\varphi(t) = f(x_0+th)$. Apply the one-variable Taylor theorem to $\varphi$ on $[0,1]$. Compute $\varphi^{(j)}$ by the chain rule and the multinomial theorem, obtaining $\varphi^{(j)}(t) = \sum_{|\alpha|=j}\frac{j!}{\alpha!}\partial^\alpha f(x_0+th)h^\alpha$. Substitute back; the $j!$ cancels the one-variable $1/j!$.

**Subgoal decomposition:**

1. **Restrict to the segment.** Define $\varphi(t) = f(x_0 + th)$ on an open interval containing $[0,1]$.
   - *Hint:* $U$ is open and the segment is in $U$, so $\varphi$ is defined on a slightly larger interval.
   - *Why needed:* It reduces the problem to one variable, where Taylor's theorem is known.

2. **Compute $\varphi^{(j)}$.** Show $\varphi^{(j)}(t) = \sum_{|\alpha|=j}\frac{j!}{\alpha!}\partial^\alpha f(x_0+th)\,h^\alpha$.
   - *Hint:* Induct on $j$ using the chain rule; the inductive step is the counting identity relating $\partial_i\partial^\alpha$ to $\partial^\beta$ with $|\beta|=|\alpha|+1$, which is where the multinomial coefficient enters.
   - *Why needed:* It is the dictionary translating $\varphi$'s derivatives into $f$'s partials.

3. **Apply one-variable Taylor to $\varphi$.** Write $\varphi(1) = \sum_{j\le k}\frac{\varphi^{(j)}(0)}{j!} + \int_0^1\frac{(1-t)^k}{k!}\varphi^{(k+1)}(t)\,dt$.
   - *Hint:* This is the one-variable Taylor theorem with integral remainder, applied at $t=1$ around $t=0$.
   - *Why needed:* It is the actual expansion; only translation remains.

4. **Substitute and simplify.** Insert the formula for $\varphi^{(j)}$; the $j!$ cancels, leaving $\sum_{|\alpha|\le k}\frac{\partial^\alpha f(x_0)}{\alpha!}h^\alpha$ plus the integral remainder.
   - *Hint:* $\frac1{j!}\cdot\frac{j!}{\alpha!} = \frac1{\alpha!}$; the remainder integrand becomes $\sum_{|\alpha|=k+1}\frac{(k+1)!}{\alpha!}\partial^\alpha f\,h^\alpha / k!$.
   - *Why needed:* It produces the final multi-index formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: The $j$-th derivative of the restriction
> **Statement:** For $f \in C^{k+1}(U)$ and $\varphi(t) = f(x_0+th)$, for every $j \le k+1$,
> $$\varphi^{(j)}(t) = \sum_{|\alpha|=j}\frac{j!}{\alpha!}\,\partial^\alpha f(x_0+th)\,h^\alpha.$$
>
> **Hint:** Induct on $j$. The base case $j=1$ is the chain rule; the step uses $\frac{d}{dt}\partial^\alpha f(x_0+th) = \sum_i\partial_i\partial^\alpha f(x_0+th)h_i$ and a counting identity for multi-indices.
>
> **Why needed:** It is the entire bridge between the one-variable expansion of $\varphi$ and the multi-index expansion of $f$.
>
> > [!note]- Full proof
> > *Base case $j=1$.* By [[Thm - The Chain Rule]] applied to $\varphi = f\circ\gamma$ with $\gamma(t) = x_0+th$, $\gamma'(t)=h$: $\varphi'(t) = \sum_{i=1}^n\partial_i f(x_0+th)h_i = \sum_{|\alpha|=1}\frac{1!}{\alpha!}\partial^\alpha f(x_0+th)h^\alpha$, since for $|\alpha|=1$, $\alpha! = 1$.
> >
> > *Inductive step.* Suppose the formula holds for $j$. Differentiate in $t$, applying the chain rule to each $\partial^\alpha f(x_0+th)$:
> > $$\varphi^{(j+1)}(t) = \sum_{|\alpha|=j}\frac{j!}{\alpha!}\Big(\sum_{i=1}^n\partial_i\partial^\alpha f(x_0+th)\,h_i\Big)h^\alpha = j!\sum_{|\alpha|=j}\sum_{i=1}^n\frac{\partial_i\partial^\alpha f(x_0+th)\,h_i h^\alpha}{\alpha!}.$$
> > For each pair $(\alpha, i)$, $\partial_i\partial^\alpha f = \partial^\beta f$ and $h_i h^\alpha = h^\beta$ where $\beta$ is $\alpha$ with $\beta_i = \alpha_i + 1$ (using [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]] to write $\partial_i\partial^\alpha = \partial^\beta$). A given $\beta$ with $|\beta| = j+1$ arises from $(\alpha, i)$ for each $i$ with $\beta_i \ge 1$, namely $\alpha = \beta - e_i$, and then $\frac1{\alpha!} = \frac{\beta_i}{\beta!}$ (since $\alpha_i! = (\beta_i-1)!$ and $\beta_i! = \beta_i\cdot(\beta_i-1)!$). Therefore
> > $$\varphi^{(j+1)}(t) = j!\sum_{|\beta|=j+1}\partial^\beta f(x_0+th)\,h^\beta\sum_{i:\,\beta_i\ge1}\frac{\beta_i}{\beta!} = j!\sum_{|\beta|=j+1}\frac{\partial^\beta f\,h^\beta}{\beta!}\sum_i\beta_i.$$
> > Since $\sum_i\beta_i = |\beta| = j+1$, the inner sum is $j+1$, giving $\varphi^{(j+1)}(t) = (j+1)!\sum_{|\beta|=j+1}\frac{\partial^\beta f(x_0+th)h^\beta}{\beta!}$, completing the induction.

> [!note]- Lemma 2: One-variable Taylor theorem with integral remainder
> **Statement:** For $\varphi \in C^{k+1}$ on an interval containing $[0,1]$, $\varphi(1) = \sum_{j=0}^k\frac{\varphi^{(j)}(0)}{j!} + \int_0^1\frac{(1-t)^k}{k!}\varphi^{(k+1)}(t)\,dt$.
>
> **Hint:** This is the standard one-variable result; it is proved by repeated integration by parts starting from $\varphi(1) - \varphi(0) = \int_0^1\varphi'(t)\,dt$.
>
> **Why needed:** It is the expansion that the multivariate theorem is translated from.
>
> > [!note]- Full proof
> > The one-variable Taylor theorem with integral remainder. From the fundamental theorem of calculus $\varphi(1) = \varphi(0) + \int_0^1\varphi'(t)\,dt$, integrate by parts repeatedly with the antiderivative $-(1-t)^{j}/j!$ of $(1-t)^{j-1}/(j-1)!$: each integration by parts peels off one term $\varphi^{(j)}(0)/j!$ and raises the order of the derivative under the integral by one. After $k$ steps one reaches $\sum_{j=0}^k\varphi^{(j)}(0)/j! + \int_0^1\frac{(1-t)^k}{k!}\varphi^{(k+1)}(t)\,dt$. (Full details: Appendix A.4 of Taylor; Exercise 9 of §1.1.)

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f \in C^{k+1}(U)$, $x_0 \in U$, and $h \in \mathbb{R}^n$ with the segment $[x_0, x_0+h] \subseteq U$. Since $U$ is open, there is $\varepsilon > 0$ with $x_0 + th \in U$ for $t \in (-\varepsilon, 1+\varepsilon)$. Define
> $$\varphi : (-\varepsilon, 1+\varepsilon) \to \mathbb{R}, \qquad \varphi(t) = f(x_0 + th).$$
> Since $f \in C^{k+1}$ and $t \mapsto x_0+th$ is smooth, $\varphi \in C^{k+1}$ by the chain rule.
>
> By Lemma 1, for each $j \le k+1$,
> $$\varphi^{(j)}(t) = \sum_{|\alpha|=j}\frac{j!}{\alpha!}\,\partial^\alpha f(x_0+th)\,h^\alpha.$$
>
> By Lemma 2 (one-variable Taylor with integral remainder), applied to $\varphi$ at $t = 1$ around $t = 0$,
> $$f(x_0+h) = \varphi(1) = \sum_{j=0}^k\frac{\varphi^{(j)}(0)}{j!} + \int_0^1\frac{(1-t)^k}{k!}\varphi^{(k+1)}(t)\,dt.$$
>
> *Polynomial part.* Substituting Lemma 1 at $t = 0$,
> $$\sum_{j=0}^k\frac{\varphi^{(j)}(0)}{j!} = \sum_{j=0}^k\frac1{j!}\sum_{|\alpha|=j}\frac{j!}{\alpha!}\partial^\alpha f(x_0)h^\alpha = \sum_{j=0}^k\sum_{|\alpha|=j}\frac{\partial^\alpha f(x_0)}{\alpha!}h^\alpha = \sum_{|\alpha|\le k}\frac{\partial^\alpha f(x_0)}{\alpha!}h^\alpha.$$
> The factor $j!$ from Lemma 1 cancels the $1/j!$ from the one-variable formula — this cancellation is the whole reason the coefficient is the clean $1/\alpha!$.
>
> *Remainder.* Substituting Lemma 1 at order $k+1$,
> $$\int_0^1\frac{(1-t)^k}{k!}\varphi^{(k+1)}(t)\,dt = \int_0^1\frac{(1-t)^k}{k!}\sum_{|\alpha|=k+1}\frac{(k+1)!}{\alpha!}\partial^\alpha f(x_0+th)h^\alpha\,dt.$$
> Since $(k+1)!/k! = k+1$, this equals
> $$R_{k+1}(x_0,h) = \int_0^1 (k+1)(1-t)^k\sum_{|\alpha|=k+1}\frac{\partial^\alpha f(x_0+th)}{\alpha!}h^\alpha\,dt.$$
>
> *Remainder size.* Since $f \in C^{k+1}$, each $\partial^\alpha f$ ($|\alpha|=k+1$) is continuous, hence bounded by some $M$ on the compact segment $[x_0,x_0+h]$. With $|h^\alpha| \le |h|^{|\alpha|} = |h|^{k+1}$ and $\int_0^1(k+1)(1-t)^k\,dt = 1$,
> $$|R_{k+1}(x_0,h)| \le M|h|^{k+1}\sum_{|\alpha|=k+1}\frac1{\alpha!} = C\,|h|^{k+1},$$
> so $R_{k+1}(x_0,h) = O(|h|^{k+1})$.
>
> Combining the polynomial part and the remainder gives the stated formula. The order-one term is $\sum_{|\alpha|=1}\partial^\alpha f(x_0)h^\alpha = \nabla f(x_0)\cdot h$; the order-two term is $\sum_{|\alpha|=2}\frac{\partial^\alpha f(x_0)}{\alpha!}h^\alpha = \frac12\sum_{i,j}\partial_i\partial_j f(x_0)h_i h_j = \frac12 h\cdot D^2 f(x_0)h$. $\blacksquare$
>
> *(Remark: a variant — Proposition 2.1.5 in Taylor — holds for $f \in C^k$ only, with the remainder $R_k(x_0,h) = \sum_{|\alpha|=k}\frac{k}{\alpha!}\big(\int_0^1(1-t)^{k-1}[\partial^\alpha f(x_0+th)-\partial^\alpha f(x_0)]\,dt\big)h^\alpha$, which is $o(|h|^k)$.)*

---

# Cross-Field Exercise Suggestions

**The second-derivative test for extrema.** At a critical point ($\nabla f = 0$) the second-order expansion is $f(x_0+h) - f(x_0) = \frac12 h\cdot D^2 f(x_0)h + O(|h|^3)$, so the sign of the increment is the sign of the Hessian quadratic form: positive definite Hessian gives a local minimum. The application is the foundation of optimisation in **Multivariate Analysis II**, nonobvious because a calculus question becomes a linear-algebra eigenvalue question.

**Reading off derivatives without differentiating.** By uniqueness of the Taylor polynomial, expanding a function by substituting a known one-variable series — e.g. $\sqrt{1+x-y^2}$ via the binomial series — and collecting by total degree yields all the partials of $f$ up to that order, with no partial ever computed. The application is nonobvious because it reverses the theorem: the expansion *determines* the derivatives (see [[Ex - Second-order Taylor expansion of a function]]).

**Convergence of power series.** A function whose Taylor remainder $R_{k+1} \to 0$ as $k \to \infty$ on a neighbourhood is *real-analytic* there — its Taylor series converges to it. The remainder bound $|R_{k+1}| \le C|h|^{k+1}$ is the input to such convergence proofs (see [[Ex - Real analyticity in several variables]]). The application is out-of-distribution in that a qualitative regularity property is established by a quantitative remainder estimate.

**The method of steepest descent / Laplace's method.** The asymptotics of integrals $\int e^{-\lambda f(x)}\,dx$ for large $\lambda$ are dominated by neighbourhoods of the minima of $f$, where the second-order Taylor expansion replaces $f$ by a quadratic and the integral becomes Gaussian. The application is nonobvious because an integral asymptotic is computed by a local Taylor expansion of the exponent.

---

# Bridges

- **The one-variable Taylor theorem** — the engine, applied to the restriction $\varphi(t) = f(x_0+th)$. The multivariate theorem is the one-variable theorem plus a translation.

- **[[Thm - The Chain Rule|The Chain Rule]]** — the translator: it computes the derivatives $\varphi^{(j)}$ of the restriction, turning $\frac{d}{dt}$ into directional derivatives of $f$.

- **[[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's Theorem]]** — the silent prerequisite: it makes the partials order-independent, so $\varphi^{(j)}$ can be collected by multi-index $\alpha$ rather than by ordered string, and the multinomial coefficient $j!/\alpha!$ counts the collapse.

- **The multinomial theorem** — $(h_1+\cdots+h_n)^j = \sum_{|\alpha|=j}\frac{j!}{\alpha!}h^\alpha$ — the pure-algebra identity supplying the coefficients; the count $j!/\alpha!$ in Lemma 1 is the multinomial coefficient.

- **The Hessian and the second-derivative test** — the order-two term $\frac12 h\cdot D^2 f\,h$ links Taylor's theorem to the optimality theory of **Multivariate Analysis II**.

---

# Unlocked by This

> [!tip] Second-Order Optimality Conditions *(from Multivariate Analysis II)*
> The order-two Taylor expansion at a critical point is $f(x_0+h)-f(x_0) = \frac12 h\cdot D^2 f(x_0)h + O(|h|^3)$. The **second-order optimality conditions** — minimum when the Hessian is positive definite, saddle when indefinite — are read directly from this, via the spectral theorem applied to the symmetric Hessian.

> [!tip] Real-Analytic Functions *(from this topic)*
> When the remainder $R_{k+1} \to 0$ as $k \to \infty$ on a neighbourhood, the Taylor series converges to $f$ and $f$ is **real-analytic**. Real-analyticity is the regularity class above $C^\infty$, and Taylor's theorem with its remainder bound is the tool that establishes it (see [[Ex - Real analyticity in several variables]]).

> [!tip] Jets and the Local Algebra of Singularities *(from Singularity Theory)*
> The $k$-th Taylor polynomial is the **$k$-jet** of $f$ at $x_0$ — the equivalence class of $f$ modulo functions vanishing to order $> k$. Jet spaces and the local algebra they carry are the setting of singularity theory and of the classification of critical points.
