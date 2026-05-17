---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - The Chain Rule"
  - "Thm - The Mean Value Inequality"
  - "Thm - The Contraction Mapping Principle"
  - "Def - Higher-Order Derivatives and Ck Maps"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open and $f : U \to \mathbb{R}^n$ is a map between Euclidean spaces of the *same* dimension. $Df_x$ is the **total derivative** at $x$, a linear map $\mathbb{R}^n \to \mathbb{R}^n$; $Jf(x)$ is its matrix, the Jacobian. The map $f$ is $C^k$ if all partial derivatives up to order $k$ exist and are continuous. A **diffeomorphism** $U \to V$ is a bijective $C^1$ map with $C^1$ inverse; a $C^k$-diffeomorphism if both are $C^k$. We write $\operatorname{Id}$ for the identity map, $|x|$ for the Euclidean norm, $\lVert L\rVert$ for the operator norm of a linear map $L$, and $B_r(x)$ for the open ball. The **symmetric part** of a matrix $M$ is $\tfrac12(M + M^T)$. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Statement

> **Inverse function theorem.** Let $U \subseteq \mathbb{R}^n$ be open, $f \in C^k(U, \mathbb{R}^n)$ with $k \geq 1$, and let $x_0 \in U$ be a point at which the total derivative $Df_{x_0} : \mathbb{R}^n \to \mathbb{R}^n$ is **invertible**. Then there is an open neighbourhood $U_0$ of $x_0$ such that:
>
> 1. $f$ is **injective** on $U_0$;
> 2. $V := f(U_0)$ is **open**;
> 3. the inverse $g := (f|_{U_0})^{-1} : V \to U_0$ is of class $C^k$, and its derivative is
> $$Dg_{f(x)} = (Df_x)^{-1} \quad\text{for all } x \in U_0, \qquad\text{equivalently}\qquad Dg_y = (Df_{g(y)})^{-1} \quad\text{for all } y \in V.$$
>
> In short, $f$ restricts to a $C^k$-diffeomorphism $U_0 \to V$. The conclusion is **local**: it concerns a neighbourhood $U_0$ of $x_0$, not all of $U$.
>
> **Global criterion (companion).** If $U$ is open and *convex* and $f \in C^1(U, \mathbb{R}^n)$ has the property that the symmetric part of $Df_x$ is positive definite at *every* $x \in U$, then $f$ is injective on all of $U$ and maps it diffeomorphically onto an open set.

---

# Motivation

In one variable, a function with $f'(x_0) \neq 0$ is locally invertible: a nonzero derivative means $f$ is strictly monotone through $x_0$, so it has a well-defined inverse near $f(x_0)$, and the inverse's derivative is $1/f'(x_0)$. This theorem is the several-variable version, and it answers a question that is genuinely deep in dimension $\geq 2$: *when can a nonlinear map be undone?*

The honest difficulty is that in several variables there is no "monotonicity" to fall back on. A map $f : \mathbb{R}^n \to \mathbb{R}^n$ can twist, fold, and overlap in ways no one-variable function can. What survives is the *linear approximation*. Near $x_0$, $f$ looks like the affine map $x \mapsto f(x_0) + Df_{x_0}(x - x_0)$, and an affine map is invertible exactly when its linear part $Df_{x_0}$ is — a finite, checkable, linear-algebra condition: $\det Jf(x_0) \neq 0$. The theorem is the statement that *this linear-algebraic invertibility propagates to the nonlinear map*, in a neighbourhood. The linear approximation being invertible is enough to force the genuine, nonlinear $f$ to be invertible nearby.

The value of the theorem is exactly this transfer: it converts a hard nonlinear question — "can I solve $f(x) = y$ for $x$?" — into a trivial linear one — "is the Jacobian determinant nonzero?". It also guarantees the inverse is as *smooth* as $f$, and gives its derivative for free by the formula $Dg = (Df)^{-1}$, which is just the chain rule applied to $g \circ f = \operatorname{Id}$.

The word **local** is the theorem's defining caveat, and it is not an apology — it is a precise statement of what linearization can promise. An invertible derivative at *every* point still does not give a globally invertible map: linearization sees only an infinitesimal neighbourhood, and global injectivity is a genuinely stronger fact requiring a genuinely stronger hypothesis. The companion criterion at the end of the statement is one such hypothesis, and being precise about exactly when local invertibility can be upgraded to global is one of the central disciplines of this topic.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$Df_{x_0}$ is an invertible linear map". The skill is recognizing this without computing a determinant from scratch.

The first disguised source is **a map that is the identity plus a small perturbation.** Property $B$: $f = \operatorname{Id} + \varphi$ where $\varphi$ has small derivative, $\lVert D\varphi\rVert < 1$. The bridge: then $Df = I + D\varphi$, and a matrix within distance $< 1$ of the identity is invertible (its inverse is the Neumann series $\sum(-D\varphi)^k$). The non-obviousness: a *smallness* condition on a perturbation, not a determinant computation, certifies invertibility. *Example:* this is exactly the situation engineered in the proof — after composing with $(Df_{x_0})^{-1}$, the map becomes a small perturbation of the identity.

The second disguised source is **a map whose derivative at the base point is a known invertible map — a rotation, a scaling, the matrix exponential's derivative.** Property $B$: $Df_{x_0}$ is recognizably one of the standard invertible linear maps. The bridge is direct, but the recognition saves work. *Example:* the matrix exponential $\operatorname{Exp}(X) = e^X$ has $D\operatorname{Exp}(0) = \operatorname{Id}$, instantly invertible, so $\operatorname{Exp}$ is a local diffeomorphism near $0$ — the foundation of the Lie-group/Lie-algebra correspondence.

The third disguised source is **a coordinate change whose Jacobian determinant is a familiar nonvanishing expression.** Property $B$: $f$ is a coordinate transformation (polar, spherical, cylindrical) whose Jacobian determinant is a known function. The bridge: that determinant is nonzero away from an explicit small set. *Example:* polar coordinates $(r,\theta) \mapsto (r\cos\theta, r\sin\theta)$ have $\det Jf = r$, nonzero for $r > 0$, so they are a local diffeomorphism everywhere off the origin — see [[Ex - Local invertibility of a nonlinear map]].

**Targets (Output Amplification)**

The conclusion is "$f$ is a local $C^k$-diffeomorphism near $x_0$".

Combine the conclusion with **a global injectivity hypothesis.** Property $D$: $f$ is *also* known to be globally injective (by periodicity considerations, properness, or the positive-definite-symmetric-part criterion). The amplified result $E$: $f$ is a *global* diffeomorphism onto its image. The combination is non-obvious and important: the inverse function theorem alone never gives this, and the topic stresses that the upgrade from local to global always costs a separate, nameable hypothesis.

Combine the conclusion with **a topological boundary condition.** Property $D$: $Df$ is invertible on a region $\Omega$ and $f$ pushes $\partial\Omega$ far from a target point $q_0$ — say $|f(x) - q_0| \geq R$ on $\partial\Omega$. The amplified result $E$: $f(\Omega)$ *contains the ball* $B_R(q_0)$ — a *surjectivity* statement, proved by a minimization argument. The non-obviousness: local invertibility plus a boundary estimate yields a global covering of a ball.

Combine the conclusion with **the change-of-variables formula for integrals.** Property $D$: $f$ is a local diffeomorphism, so $|\det Df|$ is the local volume-distortion factor. The amplified result $E$: integrals transform by $\int_{f(U_0)}h = \int_{U_0}(h\circ f)|\det Df|$. The inverse function theorem is what licenses the substitution $y = f(x)$ in a multivariable integral.

---

# Why Is It True

The theorem has a clean three-part logic, and each part has its own intuition.

**Reduce to a perturbation of the identity.** First, translate so $x_0 = 0$ and $f(x_0) = 0$, costing nothing. Then *precompose with a linear map*: instead of $f$, study $F = (Df_0)^{-1}\circ f$. This is legitimate because $(Df_0)^{-1}$ is an invertible linear map, and inverting a composition with an invertible linear map is trivial. The payoff is that $DF_0 = (Df_0)^{-1}\circ Df_0 = \operatorname{Id}$ — the new map has *derivative exactly the identity at the base point*. So $F$ is, to first order, the identity, and by continuity of the derivative, $F = \operatorname{Id} + \varphi$ with $\varphi$ having *small* derivative on a small ball. We have reduced the general invertible-derivative case to the special case "identity plus a small perturbation".

**Invert the perturbation by contracting.** Now solve $F(x) = y$, i.e. $x + \varphi(x) = y$. Rearrange: $x = y - \varphi(x)$. The right-hand side, as a function of $x$, is a map $T_y(x) = y - \varphi(x)$, and *solving the equation is finding a fixed point of $T_y$*. Why does $T_y$ have a fixed point? Because $\varphi$ has small derivative — say $\lVert D\varphi\rVert \leq \tfrac12$ — so by the [[Thm - The Mean Value Inequality|mean value inequality]] $\varphi$ shrinks distances by a factor $\tfrac12$, and therefore so does $T_y$. A distance-shrinking map on a complete space has a unique fixed point by the [[Thm - The Contraction Mapping Principle|contraction mapping principle]]. That fixed point is the unique $x$ with $F(x) = y$ — so $F$ is *injective* (one fixed point) and *surjective onto a neighbourhood* (a fixed point exists for every $y$ near $0$). The smallness of $\varphi$ is doing all the work: it is what makes $T_y$ a contraction. This is the heart of the theorem, and it is why the contraction mapping principle is its engine.

**The inverse is automatically smooth.** Once $F$ has a continuous inverse $G$, differentiability of $G$ is forced by an algebraic identity. Differentiating $F(G(y)) = y$ with the [[Thm - The Chain Rule|chain rule]] *would* give $DF\cdot DG = \operatorname{Id}$, hence $DG = (DF)^{-1}$ — *if* we knew $G$ were differentiable. The genuine argument runs the implication the other way: from the differentiability of $F$ and the (Lipschitz) continuity of $G$, one shows directly that $G$ satisfies the definition of differentiability with derivative $(DF)^{-1}$. The crucial point is that $(DF)^{-1}$ depends *continuously* on the point (matrix inversion is a smooth operation, being a ratio of polynomials in the entries — Cramer's rule), so $DG$ is continuous, so $G$ is $C^1$. And then a bootstrap: the formula $DG = \theta\circ DF\circ G$, with $\theta$ = matrix inversion, expresses $DG$ as a composition of maps each one degree of smoothness better; iterating, $G$ inherits the full $C^k$ regularity of $f$.

So one should expect the theorem because *invertibility is a robust, open condition*: a linear map close to an invertible one is invertible, and the nonlinear $f$, being close to its invertible linearization on a small enough ball, inherits invertibility — concretely, because the equation $f(x) = y$ becomes a contraction once you strip off the linear part.

The locality is now also clear. The contraction estimate $\lVert D\varphi\rVert \leq \tfrac12$ holds only on a *small* ball — the ball on which $Df$ stays close to $Df_{x_0}$. Outside it, $Df$ may drift, $\varphi$ may stop being a contraction, and $f$ may fold over itself. The neighbourhood $U_0$ is exactly the region where the linearization is still a faithful guide, and nothing in the argument controls $f$ beyond it.

---

# What Makes This Hard

The non-obvious step is the reduction-then-contraction: one must *precompose with $(Df_{x_0})^{-1}$* to turn the problem into "identity plus small perturbation", then recognize that solving $f(x) = y$ is a *fixed-point problem* $x = y - \varphi(x)$ whose contraction constant is supplied by the [[Thm - The Mean Value Inequality|mean value inequality]] bounding $\varphi$ via its small derivative. The most common error is to *believe the conclusion is global* — to think invertible $Df$ everywhere gives a globally invertible $f$ — when it is irreducibly local; a second frequent slip is to assume the inverse is differentiable and read off $DG = (DF)^{-1}$ from the chain rule, when in fact the differentiability of the inverse must itself be *proved* (from differentiability of $f$ and continuity of the inverse) before the chain rule may be applied.

---

# Rederivation Scaffold

**High-level strategy:**
Normalize so $x_0 = 0 = f(x_0)$ and precompose with $(Df_0)^{-1}$ so the derivative at $0$ becomes the identity. The map is then $\operatorname{Id} + \varphi$ with $\varphi$ a small Lipschitz perturbation. Solve $F(x) = y$ by writing it as a fixed-point problem and applying the contraction mapping principle; this gives a continuous local inverse. Then prove the inverse is differentiable, and bootstrap its smoothness.

**Subgoal decomposition:**

1. **Normalize and reduce to a perturbation of the identity.** Replace $f$ by $F = (Df_0)^{-1}\circ f$, so $F(0) = 0$ and $DF_0 = \operatorname{Id}$.
   - *Hint:* Precomposing with the invertible linear map $(Df_0)^{-1}$ does not affect invertibility and makes $DF_0 = \operatorname{Id}$.
   - *Why needed:* It puts the map in the form $\operatorname{Id} + \varphi$ to which the contraction argument applies.

2. **Make $\varphi$ a contraction on a small ball.** With $\varphi = F - \operatorname{Id}$, note $D\varphi_0 = 0$; by continuity, $\lVert D\varphi\rVert \leq \tfrac12$ on a small ball $B_r$.
   - *Hint:* $D\varphi$ is continuous and vanishes at $0$; the mean value inequality turns the derivative bound into $|\varphi(x) - \varphi(x')| \leq \tfrac12|x - x'|$.
   - *Why needed:* The factor $\tfrac12 < 1$ is the contraction constant.

3. **Solve $F(x) = y$ by a fixed point.** For $y$ near $0$, the map $T_y(x) = y - \varphi(x)$ is a contraction; its fixed point is the unique solution.
   - *Hint:* Apply the [[Thm - The Contraction Mapping Principle|contraction mapping principle]] on a suitable complete ball; check $T_y$ maps the ball into itself.
   - *Why needed:* Uniqueness of the fixed point gives injectivity; existence for all $y$ near $0$ gives an open image and a local inverse $G$.

4. **Show the inverse is differentiable with $DG = (DF)^{-1}$.** From differentiability of $F$ and Lipschitz continuity of $G$, verify the definition of differentiability for $G$.
   - *Hint:* Write $y - y_0 = F(G(y)) - F(G(y_0)) = DF_{x_0}(G(y) - G(y_0)) + o(\cdot)$ and invert $DF_{x_0}$; the Lipschitz bound on $G$ controls the error.
   - *Why needed:* It establishes $G \in C^1$, since $(DF)^{-1}$ depends continuously on the point.

5. **Bootstrap the smoothness.** Use $DG = \theta\circ DF\circ G$ with $\theta$ = matrix inversion to upgrade $C^\ell$ to $C^{\ell+1}$.
   - *Hint:* Matrix inversion is $C^\infty$; if $G \in C^\ell$ and $f \in C^k$, the composition shows $DG \in C^{\min(\ell, k-1)}$, hence $G \in C^{\min(\ell+1, k)}$. Induct.
   - *Why needed:* It delivers the full $C^k$ conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: A small Lipschitz perturbation of the identity is injective with open image
> **Statement:** Let $\varphi : U \to \mathbb{R}^n$ be Lipschitz with constant $\lambda < 1$, and $F = \operatorname{Id} + \varphi$. Then whenever $\overline{B_r(x)} \subseteq U$, $F$ is injective on $B_r(x)$ and $B_{(1-\lambda)r}(F(x)) \subseteq F(B_r(x))$; in particular $F(U)$ is open and $F^{-1}$ is Lipschitz with constant $\frac{1}{1-\lambda}$.
>
> **Hint:** For injectivity, $F(x) = F(x')$ gives $x - x' = \varphi(x') - \varphi(x)$, contradicting $\lambda < 1$. For the image, solve $F(x) = y$ as the fixed point of $x \mapsto y - \varphi(x)$.
>
> **Why needed:** It is the core invertibility statement; the inverse function theorem reduces to it after normalization.
>
> > [!note]- Full proof
> > *Injectivity.* If $F(x) = F(x')$ then $x + \varphi(x) = x' + \varphi(x')$, so $|x - x'| = |\varphi(x') - \varphi(x)| \leq \lambda|x - x'|$; since $\lambda < 1$, $|x - x'| = 0$.
> >
> > *Image contains a ball.* Fix $x$ with $\overline{B_r(x)} \subseteq U$ and let $y \in B_{(1-\lambda)r}(F(x))$. Solving $F(\xi) = y$ means $\xi = y - \varphi(\xi)$; this is the fixed point of $T(\xi) = y - \varphi(\xi)$. $T$ is a contraction with constant $\lambda$, and it maps $\overline{B_r(x)}$ into itself: for $\xi \in \overline{B_r(x)}$, $|T(\xi) - x| \leq |y - F(x)| + |\varphi(x) - \varphi(\xi)| \leq (1-\lambda)r + \lambda r = r$. Since $\overline{B_r(x)}$ is complete, the [[Thm - The Contraction Mapping Principle|contraction mapping principle]] gives a fixed point $\xi \in \overline{B_r(x)}$ with $F(\xi) = y$. So $B_{(1-\lambda)r}(F(x)) \subseteq F(B_r(x))$, and as $x$ was arbitrary, $F(U)$ is open.
> >
> > *Lipschitz inverse.* For $y = F(x), y' = F(x')$: $|y - y'| = |x - x' + \varphi(x) - \varphi(x')| \geq |x - x'| - \lambda|x - x'| = (1-\lambda)|x-x'|$, so $|F^{-1}(y) - F^{-1}(y')| \leq \frac{1}{1-\lambda}|y - y'|$.

> [!note]- Lemma 2: The inverse of a differentiable map with invertible derivative is differentiable
> **Statement:** Let $f : U \to V$ and $g : V \to U$ be mutual inverses, $f$ differentiable at $x_0$ with $Df_{x_0}$ invertible, and $g$ Lipschitz. Then $g$ is differentiable at $y_0 = f(x_0)$ with $Dg_{y_0} = (Df_{x_0})^{-1}$.
>
> **Hint:** Substitute $x = g(y)$ into the first-order expansion of $f$ and use the Lipschitz bound to absorb the error.
>
> **Why needed:** It supplies the differentiability of the inverse — which cannot simply be read off the chain rule — and the derivative formula.
>
> > [!note]- Full proof
> > Write $L = Df_{x_0}$. By differentiability of $f$ at $x_0$, as $y \to y_0$,
> > $$y - y_0 = f(g(y)) - f(x_0) = L\big(g(y) - g(y_0)\big) + o\big(|g(y) - g(y_0)|\big).$$
> > Apply $L^{-1}$:
> > $$g(y) - g(y_0) = L^{-1}(y - y_0) + o\big(|g(y) - g(y_0)|\big).$$
> > Since $g$ is Lipschitz with some constant $\Lambda$, $|g(y) - g(y_0)| \leq \Lambda|y - y_0|$, so the error term $o(|g(y)-g(y_0)|)$ is also $o(|y - y_0|)$. Hence $g(y) - g(y_0) = L^{-1}(y - y_0) + o(|y-y_0|)$, which is exactly the statement that $g$ is differentiable at $y_0$ with $Dg_{y_0} = L^{-1} = (Df_{x_0})^{-1}$.

> [!note]- Lemma 3: Matrix inversion is smooth
> **Statement:** The map $\theta : X \mapsto X^{-1}$ on the open set of invertible $n\times n$ matrices is $C^\infty$.
>
> **Hint:** Cramer's rule expresses each entry of $X^{-1}$ as a polynomial in the entries of $X$ divided by $\det X$.
>
> **Why needed:** It powers the bootstrap: $DG = \theta\circ DF\circ G$ shows $G$ gains a derivative of smoothness each induction step.
>
> > [!note]- Full proof
> > By Cramer's rule, $(X^{-1})_{pq} = C_{qp}/\det X$, where the cofactor $C_{qp}$ is, up to sign, the determinant of a submatrix of $X$ — a polynomial in the entries of $X$. The denominator $\det X$ is also a polynomial, and it is nonzero on the set of invertible matrices. So every entry of $X^{-1}$ is a ratio of polynomials with nonvanishing denominator, hence a $C^\infty$ function of the entries of $X$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f \in C^k(U, \mathbb{R}^n)$, $Df_{x_0}$ invertible.
>
> **Normalization.** Replacing $f$ by $\tilde f(x) = f(x + x_0) - f(x_0)$ moves the base point and value to $0$ without changing invertibility, so assume $x_0 = 0$, $f(0) = 0$. Set $L = Df_0$ and $F = L^{-1}\circ f$. Then $F \in C^k$, $F(0) = 0$, and by the chain rule $DF_0 = L^{-1}\circ Df_0 = L^{-1}L = \operatorname{Id}$. Since $L$ is an invertible linear map, $f = L\circ F$ is a $C^k$-diffeomorphism on a set exactly when $F$ is, so it suffices to treat $F$.
>
> **$F$ is a small perturbation of the identity.** Write $\varphi = F - \operatorname{Id}$, so $D\varphi_0 = DF_0 - \operatorname{Id} = 0$. Since $D\varphi$ is continuous, choose $r > 0$ with $\lVert D\varphi_x\rVert \leq \tfrac12$ for all $x \in B_r := B_r(0)$. By the [[Thm - The Mean Value Inequality|mean value inequality]] on the convex set $B_r$, $\varphi$ is Lipschitz on $B_r$ with constant $\tfrac12$.
>
> **Injectivity and open image (parts 1, 2).** By Lemma 1 with $\lambda = \tfrac12$, $F$ is injective on $B_r$, the image $F(B_r)$ is open, and $F^{-1} : F(B_r) \to B_r$ is Lipschitz with constant $2$. Set $U_0 = B_r$ and $V = F(B_r)$ (these refer to $F$; for $f$, take $f(B_r) = L(F(B_r))$, which is open because $L$ is a linear isomorphism, hence an open map). Parts (1) and (2) hold.
>
> **The inverse is $C^1$ (part 3, base case).** Let $G = (F|_{B_r})^{-1}$. By the chain-rule computation $DF_0 = \operatorname{Id}$ and continuity, shrinking $r$ if necessary, $DF_x$ is invertible for *every* $x \in B_r$ (a matrix within $\tfrac12$ of $I$ is invertible). $F$ is differentiable at each $x \in B_r$ and $G$ is Lipschitz, so by Lemma 2, $G$ is differentiable at every $y \in V$ with
> $$DG_y = (DF_{G(y)})^{-1}. \tag{$\ast$}$$
> The right side is a composition $y \mapsto G(y) \mapsto DF_{G(y)} \mapsto (DF_{G(y)})^{-1}$ of the continuous maps $G$, $x \mapsto DF_x$, and $\theta$ (matrix inversion, continuous by Lemma 3). Hence $DG$ is continuous and $G \in C^1$.
>
> **Bootstrap to $C^k$ (part 3, induction).** Suppose $f \in C^k$ and $G \in C^\ell$ for some $\ell \in \{1, \dots, k-1\}$. In ($\ast$), the map $y \mapsto G(y)$ is $C^\ell$; the map $x \mapsto DF_x$ is $C^{k-1}$ (since $F \in C^k$); and $\theta$ is $C^\infty$. So $DG = \theta\circ(DF)\circ G$ is a composition of maps of class $C^\ell$, $C^{k-1}$, $C^\infty$, hence of class $C^{\min(\ell, k-1)} = C^\ell$ (as $\ell \leq k-1$). Therefore $G \in C^{\ell+1}$. Starting from $\ell = 1$ and inducting up to $\ell = k-1$, $G \in C^k$.
>
> Translating back, $g = F^{-1}\circ L^{-1}$ is $C^k$, and the chain rule gives $Dg_{f(x)} = (Df_x)^{-1}$. $\blacksquare$
>
> **Global criterion.** For the companion statement: on a convex $U$ with the symmetric part of $Df$ positive definite everywhere, take distinct $u_1, u_2 \in U$, set $w = u_2 - u_1$, and consider $\psi(t) = w\cdot f(u_1 + tw)$ on $[0,1]$. Then $\psi'(t) = w^T Df(u_1 + tw)\,w = w^T\big[\tfrac12(Df + Df^T)\big]w > 0$, since the symmetric part is positive definite and $w \neq 0$. So $\psi$ is strictly increasing, $\psi(0) \neq \psi(1)$, i.e. $w\cdot f(u_1) \neq w\cdot f(u_2)$, hence $f(u_1) \neq f(u_2)$. So $f$ is injective on all of $U$; combined with the local theorem (which gives openness of the image and local smoothness of the inverse at each point), $f$ is a global diffeomorphism onto an open set. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The matrix exponential and Lie groups.** The map $\operatorname{Exp}(X) = e^X$ on $n\times n$ matrices has $D\operatorname{Exp}(0) = \operatorname{Id}$ (from $e^X = I + X + \tfrac12 X^2 + \cdots$), so by the inverse function theorem $\operatorname{Exp}$ is a local diffeomorphism near $0$, with a smooth local inverse $\operatorname{Log}$. This is the foundation of the Lie group / Lie algebra correspondence: the exponential identifies a neighbourhood of the identity in a matrix group with a neighbourhood of $0$ in its Lie algebra. The application is nonobvious because the "Euclidean space" is the space of matrices and the theorem is being used to *coordinatize a group*.

**Newton's method as a self-improving inverse.** The inverse function theorem's fixed-point construction, with the linear part re-estimated at each step rather than frozen, *is* Newton's method for solving $f(x) = y$. Analyzing the iteration $x_{k+1} = x_k + Df(x_k)^{-1}(y - f(x_k))$ shows quadratic convergence. The application battle-tests the proof: the same contraction idea, with a sharper linearization, yields a fast numerical algorithm.

**Holomorphic inverse functions.** Identify $\mathbb{R}^{2n}$ with $\mathbb{C}^n$. If a $C^1$ map is *holomorphic* and has invertible derivative at a point, the inverse function theorem produces a smooth local inverse — and one can show the inverse is again holomorphic. The application is out-of-distribution because a real-analysis theorem, applied carefully, delivers a complex-analytic conclusion: the holomorphic inverse function theorem.

---

# Bridges

- **[[Thm - The Contraction Mapping Principle]]** — the engine. The inverse is constructed as the fixed point of the contraction $x \mapsto y - \varphi(x)$; the smallness of $\varphi$, arranged by precomposing with $(Df_0)^{-1}$, is the contraction constant.

- **[[Thm - The Implicit Function Theorem]]** — the twin. The implicit function theorem is the inverse function theorem applied to the auxiliary map $(x,y) \mapsto (x, f(x,y))$; conversely the inverse function theorem is the implicit function theorem applied to $F(x,y) = f(x) - y$. They are one theorem in two costumes.

- **[[Thm - The Mean Value Inequality]]** — converts the pointwise derivative bound $\lVert D\varphi\rVert \leq \tfrac12$ into the global Lipschitz/contraction estimate.

- **[[Thm - The Chain Rule]]** — gives the derivative formula $Dg = (Df)^{-1}$ once differentiability of the inverse is established, and powers the smoothness bootstrap.

- **[[Thm - The Regular Value Theorem]]** — a downstream consequence. The regular value theorem (and the equivalence of submanifold descriptions) is the implicit function theorem applied locally, hence ultimately the inverse function theorem.

---

# Unlocked by This

> [!tip] The Rank Theorem *(from Differential Geometry)*
> The inverse function theorem is the maximal-rank case. When $Df$ has *constant* rank $r$ in a neighbourhood, the **rank theorem** says $f$ looks, in suitable local coordinates on both sides, exactly like the linear projection $(x_1,\dots,x_n)\mapsto(x_1,\dots,x_r,0,\dots,0)$. It is proved by two applications of the inverse function theorem.

> [!tip] The Change of Variables Formula *(from Integration Theory)*
> Because a map with invertible derivative is a local diffeomorphism, it can be used as a substitution in a multivariable integral, and the local volume-distortion factor is $|\det Df|$. This is the **change of variables formula** — see [[Multivariate Analysis III — Integration in Several Variables]].

> [!tip] Charts on Lie Groups *(from Lie Theory)*
> Applied to the matrix exponential, the inverse function theorem provides the **exponential chart** identifying a neighbourhood of the identity in a matrix group with its Lie algebra — the local coordinate system in which the group's smooth structure is read off.
