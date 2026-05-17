---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Thm - Taylor's Theorem in Several Variables"
  - "Def - Higher-Order Derivatives and Ck Maps"
  - "Def - Directional Derivative and the Gradient"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $f(x,y) = \sqrt{1 + x - y^2}$, defined for $(x,y)$ near the origin (where $1 + x - y^2 > 0$).

1. Compute the second-order Taylor polynomial $P_2(x,y)$ of $f$ about the origin — **without computing any partial derivatives** — by substituting into the known one-variable expansion of $\sqrt{1+t}$.
2. Read off the gradient $\nabla f(0,0)$ and the Hessian $D^2 f(0,0)$ from $P_2$, using the uniqueness of the Taylor polynomial.
3. Verify the gradient by direct partial differentiation, as a consistency check.

**Recall:**

The tool is Taylor's theorem together with the uniqueness of the Taylor polynomial.

![[Thm - Taylor's Theorem in Several Variables#Statement]]

[[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] gives $f(x_0+h) = \sum_{|\alpha|\le k}\frac{\partial^\alpha f(x_0)}{\alpha!}h^\alpha + R_{k+1}$. The order-one term is $\nabla f\cdot h$, the order-two term is $\frac12 h\cdot D^2 f\,h$.

**Uniqueness of the Taylor polynomial.** If a degree-$k$ polynomial $P$ satisfies $f(x_0+h) - P(h) = o(|h|^k)$, then $P$ *is* the Taylor polynomial — its coefficients are exactly $\partial^\alpha f(x_0)/\alpha!$. So any polynomial approximation good to order $k$ determines the partials up to order $k$.

The [[Def - Directional Derivative and the Gradient|gradient]] $\nabla f$ and the [[Def - Higher-Order Derivatives and Ck Maps|Hessian]] $D^2 f$ collect the first and second partials.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-derivative* problem — produce a Taylor polynomial — but solved by the efficient route. As the [[Multivariate Analysis I — Differentiation in Several Variables#Problem-Solving Strategy|topic page strategy]] notes, the factorials in the multi-index Taylor formula are a nuisance, and the fast route is often to substitute a known one-variable expansion and read off the coefficients, justified because the Taylor polynomial is unique.

**Assumption pattern.** The function $f$ is a *one-variable function applied to a multivariate expression*: $f = g\circ u$ with $g(t) = \sqrt{1+t}$ a function whose Taylor series is standard and $u(x,y) = x - y^2$ a polynomial. The recognisable feature: "known one-variable function, polynomial argument" — the trigger for substitution rather than partial differentiation.

**Theorem routing.** Part 1: take the one-variable expansion $\sqrt{1+t} = 1 + \tfrac12 t - \tfrac18 t^2 + O(t^3)$, substitute $t = x - y^2$, expand, and discard everything of total degree $> 2$ in $(x,y)$. Part 2: match $P_2$ against the general second-order Taylor form $f(0,0) + \nabla f(0,0)\cdot h + \tfrac12 h\cdot D^2 f(0,0)h$; the [[Thm - Taylor's Theorem in Several Variables|uniqueness]] of the Taylor polynomial guarantees the match reads off the genuine derivatives. Part 3: differentiate $f$ directly and confirm.

**Key decision point.** The non-obvious bookkeeping is *tracking total degree correctly through the substitution*. When $t = x - y^2$ is substituted, $t$ itself contains a degree-$1$ piece ($x$) and a degree-$2$ piece ($-y^2$); $t^2$ contains pieces of degree $2$, $3$, $4$; $t^3$ is degree $\ge 3$. To get the degree-$2$ polynomial, one keeps: from $\tfrac12 t$, both $x$ (degree 1) and $-y^2$ (degree 2); from $-\tfrac18 t^2$, only the degree-$2$ part of $t^2$, which is $x^2$; from $t^3$, nothing. Mis-assigning the degree of $y^2$ — treating it as degree $1$ — is the standard slip.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Approximate by a Taylor polynomial.** Replace $\sqrt{1+t}$ by its degree-$2$ one-variable Taylor polynomial.

2. **Compose by substitution.** Substitute the polynomial $t = x - y^2$ into the one-variable expansion.

3. **Use uniqueness of the Taylor polynomial.** Match the resulting degree-$2$ polynomial to the general Taylor form to extract $\nabla f$ and $D^2 f$ without differentiating.

4. **Compute partials by Analysis I rules** (Part 3 check). Differentiate $f$ directly to confirm the gradient.

---

# Hints

> [!note]- Hint 1
> From Analysis I, $\sqrt{1+t} = 1 + \tfrac12 t - \tfrac18 t^2 + O(t^3)$ as $t \to 0$. Substitute $t = x - y^2$. The catch: when you collect terms by total degree in $(x,y)$, remember that $x$ has degree $1$ but $y^2$ has degree $2$.

> [!note]- Hint 2
> $t = x - y^2$: degree-$1$ part is $x$, degree-$2$ part is $-y^2$. $t^2 = (x-y^2)^2 = x^2 - 2xy^2 + y^4$: the only degree-$\le2$ part is $x^2$. $t^3$ and higher are all degree $\ge 3$. So keep $\tfrac12(x - y^2)$ and $-\tfrac18 x^2$, discard the rest.

> [!note]- Hint 3
> You should get $P_2(x,y) = 1 + \tfrac12 x - \tfrac12 y^2 - \tfrac18 x^2$. Now compare with $f(0,0) + \partial_x f(0,0)\,x + \partial_y f(0,0)\,y + \tfrac12\partial_{xx}f(0,0)\,x^2 + \partial_{xy}f(0,0)\,xy + \tfrac12\partial_{yy}f(0,0)\,y^2$. Match coefficients term by term.

> [!note]- Hint 4
> Matching: the constant gives $f(0,0)=1$; the $x$-coefficient gives $\partial_x f(0,0) = \tfrac12$; there is no $y$ term so $\partial_y f(0,0) = 0$; the $x^2$-coefficient $-\tfrac18$ gives $\partial_{xx}f(0,0) = -\tfrac14$; no $xy$ term gives $\partial_{xy}f(0,0) = 0$; the $y^2$-coefficient $-\tfrac12$ gives $\tfrac12\partial_{yy}f(0,0) = -\tfrac12$, so $\partial_{yy}f(0,0) = -1$.

---

# Solution

The function is $\sqrt{1+t}$ with $t = x - y^2$ — a known one-variable expansion composed with a polynomial. Substituting the one-variable series and truncating at total degree $2$ produces the Taylor polynomial directly, with no partial derivative ever computed; uniqueness of the Taylor polynomial then certifies that the coefficients *are* the derivatives.

**Step 1: The second-order Taylor polynomial is $P_2(x,y) = 1 + \tfrac12 x - \tfrac12 y^2 - \tfrac18 x^2$.**

> [!note]- Derivation
> From the one-variable binomial expansion, valid as $t \to 0$,
> $$\sqrt{1+t} = 1 + \tfrac12 t - \tfrac18 t^2 + O(t^3).$$
> Substitute $t = x - y^2$. The argument $t$ tends to $0$ as $(x,y) \to (0,0)$, so the expansion applies. Track total degree in $(x,y)$, remembering $\deg x = 1$ and $\deg(y^2) = 2$:
> - $1$ — degree $0$.
> - $\tfrac12 t = \tfrac12(x - y^2) = \tfrac12 x - \tfrac12 y^2$ — a degree-$1$ term $\tfrac12 x$ and a degree-$2$ term $-\tfrac12 y^2$.
> - $-\tfrac18 t^2 = -\tfrac18(x - y^2)^2 = -\tfrac18(x^2 - 2xy^2 + y^4)$ — the term $-\tfrac18 x^2$ has degree $2$; the terms $\tfrac14 xy^2$ (degree $3$) and $-\tfrac18 y^4$ (degree $4$) are discarded.
> - $O(t^3)$ — since $t = O(|h|)$ (as $|t| \le |x| + y^2 \le |h| + |h|^2$), $t^3 = O(|h|^3)$, all of total degree $\ge 3$, discarded.
>
> Collecting all terms of total degree $\le 2$,
> $$P_2(x,y) = 1 + \tfrac12 x - \tfrac12 y^2 - \tfrac18 x^2.$$
> By [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]], $f(x,y) - P_2(x,y) = O(|h|^3) = o(|h|^2)$, so $P_2$ is a degree-$2$ polynomial approximating $f$ to order $2$.

**Step 2: $\nabla f(0,0) = (\tfrac12,\ 0)$ and $D^2 f(0,0) = \begin{pmatrix}-\tfrac14 & 0\\ 0 & -1\end{pmatrix}$.**

> [!note]- Derivation
> By the **uniqueness of the Taylor polynomial** — any degree-$2$ polynomial agreeing with $f$ to order $o(|h|^2)$ has exactly the Taylor coefficients $\partial^\alpha f(0,0)/\alpha!$ — the $P_2$ of Step 1 is *the* second-order Taylor polynomial. The general second-order Taylor form is
> $$P_2(x,y) = f(0,0) + \partial_x f(0,0)\,x + \partial_y f(0,0)\,y + \tfrac12\partial_{xx}f(0,0)\,x^2 + \partial_{xy}f(0,0)\,xy + \tfrac12\partial_{yy}f(0,0)\,y^2.$$
> (The $xy$ coefficient is $\partial_{xy}f(0,0)$ and not $\tfrac12$ of it, because the multi-index $\alpha = (1,1)$ has $\alpha! = 1$, whereas $\alpha = (2,0)$ has $\alpha! = 2$.) Matching coefficients with $P_2 = 1 + \tfrac12 x - \tfrac12 y^2 - \tfrac18 x^2$:
> $$f(0,0) = 1, \quad \partial_x f(0,0) = \tfrac12, \quad \partial_y f(0,0) = 0,$$
> $$\tfrac12\partial_{xx}f(0,0) = -\tfrac18 \Rightarrow \partial_{xx}f(0,0) = -\tfrac14, \quad \partial_{xy}f(0,0) = 0, \quad \tfrac12\partial_{yy}f(0,0) = -\tfrac12 \Rightarrow \partial_{yy}f(0,0) = -1.$$
> Therefore
> $$\nabla f(0,0) = \big(\partial_x f, \partial_y f\big)(0,0) = \big(\tfrac12,\ 0\big), \qquad D^2 f(0,0) = \begin{pmatrix}\partial_{xx}f & \partial_{xy}f\\ \partial_{yx}f & \partial_{yy}f\end{pmatrix}(0,0) = \begin{pmatrix}-\tfrac14 & 0\\ 0 & -1\end{pmatrix}.$$
> The Hessian is symmetric, as Schwarz's theorem guarantees for the smooth function $f$.

**Step 3: Direct verification of the gradient.**

> [!note]- Derivation
> Differentiate $f(x,y) = (1 + x - y^2)^{1/2}$ directly by the chain rule:
> $$\partial_x f = \tfrac12(1+x-y^2)^{-1/2}\cdot 1, \qquad \partial_y f = \tfrac12(1+x-y^2)^{-1/2}\cdot(-2y) = -y(1+x-y^2)^{-1/2}.$$
> At the origin, $1 + 0 - 0 = 1$, so
> $$\partial_x f(0,0) = \tfrac12\cdot 1 = \tfrac12, \qquad \partial_y f(0,0) = -0\cdot 1 = 0.$$
> This matches $\nabla f(0,0) = (\tfrac12, 0)$ from Step 2 — the substitution method and direct differentiation agree, as uniqueness of the Taylor polynomial guarantees they must.

> [!note]- Complete formal solution
> **Claim.** $f(x,y) = \sqrt{1+x-y^2}$ has second-order Taylor polynomial $P_2 = 1 + \tfrac12 x - \tfrac12 y^2 - \tfrac18 x^2$ about the origin, with $\nabla f(0,0) = (\tfrac12, 0)$ and $D^2 f(0,0) = \operatorname{diag}(-\tfrac14, -1)$.
>
> Substituting $t = x - y^2$ into $\sqrt{1+t} = 1 + \tfrac12 t - \tfrac18 t^2 + O(t^3)$ and keeping total degree $\le 2$ (with $\deg x = 1$, $\deg y^2 = 2$): $\tfrac12 t$ contributes $\tfrac12 x - \tfrac12 y^2$; $-\tfrac18 t^2$ contributes $-\tfrac18 x^2$; higher terms are degree $\ge 3$. Hence $P_2 = 1 + \tfrac12 x - \tfrac12 y^2 - \tfrac18 x^2$. By uniqueness of the Taylor polynomial ([[Thm - Taylor's Theorem in Several Variables]]), matching against $f(0,0) + \nabla f\cdot h + \tfrac12 h\cdot D^2 f\,h$ gives $\nabla f(0,0) = (\tfrac12, 0)$, $D^2 f(0,0) = \operatorname{diag}(-\tfrac14, -1)$. Direct differentiation confirms $\partial_x f(0,0) = \tfrac12$, $\partial_y f(0,0) = 0$. $\blacksquare$

---

# Key Takeaways

**Substitute a known one-variable expansion rather than computing multivariate partials — the Taylor polynomial is unique, so any route to it is valid.** The most efficient way to expand a function that is "a known one-variable function of a polynomial argument" is never to grind out the partial derivatives. It is to take the one-variable Taylor series off the shelf, substitute the argument, expand, and truncate at the desired total degree. The justification is the *uniqueness* of the Taylor polynomial: any degree-$k$ polynomial agreeing with $f$ to order $o(|h|^k)$ has exactly the Taylor coefficients, so it does not matter how you found it. This converts a calculation that would need six partial derivatives (two first, three second, evaluated at a point) into a one-line substitution. The trigger to use it: recognise $f$ as $g\circ u$ with $g$ a function of known series — $\sqrt{1+t}$, $e^t$, $\log(1+t)$, $(1+t)^a$, $\sin t$ — and $u$ a polynomial.

**Track total degree carefully through the substitution: the degree of the argument's pieces is what matters, not the degree of the original variable.** The one genuine pitfall in the substitution method is degree bookkeeping. When $t = x - y^2$ is substituted, the variable $t$ is *not* uniformly degree $1$ — its piece $x$ is degree $1$ but its piece $y^2$ is degree $2$. Consequently $t^2$ spreads across degrees $2$ through $4$, and to extract the degree-$2$ part of $f$ one must keep only the degree-$2$ part of $t^2$ (here $x^2$) while discarding $xy^2$ and $y^4$. The discipline: when truncating at total degree $k$, expand each power $t^j$ and *re-sort its terms by their total degree in the original variables*, keeping only those of degree $\le k$. Treating $y^2$ as though it were degree $1$ — the standard error — would wrongly retain $xy^2$ and produce a non-polynomial or wrong-degree result.

**The order-two Taylor term is the Hessian quadratic form, and the multi-index factorials are not optional — the $xy$ coefficient is $\partial_{xy}f$, the $x^2$ coefficient is $\tfrac12\partial_{xx}f$.** When matching a computed polynomial to the Taylor form to extract derivatives, the coefficient pattern is dictated by $\partial^\alpha f/\alpha!$, and the factorials differ across terms. For the pure second-order term in $x$, the multi-index is $\alpha = (2,0)$ with $\alpha! = 2$, so the coefficient of $x^2$ is $\partial_{xx}f/2$ — to recover $\partial_{xx}f$ you double the coefficient. For the mixed term, $\alpha = (1,1)$ with $\alpha! = 1$, so the coefficient of $xy$ is $\partial_{xy}f$ itself — no factor of two. This asymmetry is exactly the multinomial coefficient $k!/\alpha!$ from the proof of Taylor's theorem: the mixed monomial $xy$ arises from two orderings of differentiation while $x^2$ arises from one, and the $1/\alpha!$ records it. Getting this factor wrong is the most common error in reading a Hessian off a Taylor polynomial; the safe practice is to write the general Taylor form with the factorials explicit and match against it.
