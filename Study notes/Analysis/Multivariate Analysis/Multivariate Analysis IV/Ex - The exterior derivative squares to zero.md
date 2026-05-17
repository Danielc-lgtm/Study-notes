---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Differential Form"
  - "Def - The Wedge Product"
  - "Def - The Exterior Derivative"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $\Omega \subseteq \mathbb{R}^n$ be open and let $\alpha \in \Lambda^k(\Omega)$ be a smooth $k$-form.

1. Prove that $d(d\alpha) = 0$; that is, the [[Def - The Exterior Derivative|exterior derivative]] applied twice is the zero operator on $\Lambda^k(\Omega)$. Identify precisely the two ingredients the proof uses: the antisymmetry of the wedge product and the symmetry of mixed partial derivatives.
2. Deduce, working in $\mathbb{R}^3$ and using the dictionary "$d$ on a $0$-form is $\operatorname{grad}$, $d$ on a $1$-form is $\operatorname{curl}$, $d$ on a $2$-form is $\operatorname{div}$", the two classical identities
$$\operatorname{curl}\operatorname{grad} f = 0, \qquad \operatorname{div}\operatorname{curl} F = 0,$$
for every smooth function $f$ and smooth vector field $F$.

**Recall:**

![[Def - The Exterior Derivative#The Definition]]

The [[Def - The Exterior Derivative|exterior derivative]] of $\alpha = \sum_j a_j\,dx_{j_1}\wedge\cdots\wedge dx_{j_k}$ is $d\alpha = \sum_{j,\ell}(\partial a_j/\partial x_\ell)\,dx_\ell\wedge dx_{j_1}\wedge\cdots\wedge dx_{j_k}$.

The two facts the proof rests on:

- **Antisymmetry of the wedge.** By the [[Def - The Wedge Product|wedge product]], $dx_\ell\wedge dx_m = -\,dx_m\wedge dx_\ell$, and any basic form with a repeated factor is zero.
- **Symmetry of mixed partials (Schwarz's theorem).** For a $C^2$ function $a$, $\dfrac{\partial^2 a}{\partial x_\ell\,\partial x_m} = \dfrac{\partial^2 a}{\partial x_m\,\partial x_\ell}$. Since the coefficients of a smooth form are smooth, this applies to every coefficient.

---

# Convergent Strategy

**Problem class.** This is a *structural identity* problem: prove an algebraic property of an operator, holding for all inputs. As the [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] strategy records, identity proofs in this topic are won by translating to forms and watching a symmetry collide with an antisymmetry.

**Assumption pattern.** The only assumptions are that $\alpha$ is smooth (so its coefficients are $C^2$, licensing Schwarz) and that $\Omega$ is open (so partials are defined). There is nothing geometric — the result is purely the algebra of $d$.

**Theorem routing.** Apply the definition of $d$ twice, producing a double sum $\sum_{\ell, m}\partial_m\partial_\ell a_j\,dx_m\wedge dx_\ell\wedge dx_j$. Then pair the $(\ell, m)$ term against the $(m, \ell)$ term: the coefficient is symmetric (Schwarz) while the basic form is antisymmetric (wedge), so each pair cancels. Part 2 routes through the grad/curl/div dictionary established in [[Ex - Computing wedge products and exterior derivatives]].

**Key decision point.** The non-obvious step is *how to pair the terms*. The double sum is not visibly zero term-by-term; it is zero only when you group the term indexed $(\ell, m)$ with the term indexed $(m, \ell)$ and observe the two carry opposite signs but equal coefficients. Seeing that this pairing is exhaustive and sign-reversing is the entire content of the proof.

---

# Legal Operations Used

1. **Compute $d$ of a form** — applied twice, to $\alpha$ and then to $d\alpha$.
2. **Use $d\circ d = 0$ as an algebraic shortcut** — this exercise *proves* the shortcut, then in part 2 immediately exploits it.
3. **Express divergence, curl, and gradient as instances of $d$** — part 2 is entirely the translation: a gradient is $d$ of a $0$-form, a curl is $d$ of a $1$-form, so the composites are $d^2$.

---

# Hints

> [!note]- Hint 1
> Write $\alpha = \sum_j a_j\,dx_j$ (multi-index $j$ of length $k$). Apply $d$ once to get $d\alpha = \sum_{j,\ell}\partial_\ell a_j\,dx_\ell\wedge dx_j$. Now apply $d$ again — the coefficient of the inner form is $\partial_\ell a_j$, so you differentiate *it*, producing a second derivative.

> [!note]- Hint 2
> After applying $d$ twice you have a double sum over $\ell$ and $m$ of $\partial_m\partial_\ell a_j\,dx_m\wedge dx_\ell\wedge dx_j$. Fix a multi-index $j$ and a pair of distinct indices $\{\ell, m\}$. How many terms of the double sum involve exactly these two indices, and how do their basic forms compare?

> [!note]- Hint 3
> The term indexed $(\ell, m)$ has basic form $dx_m\wedge dx_\ell\wedge dx_j$; the term indexed $(m, \ell)$ has basic form $dx_\ell\wedge dx_m\wedge dx_j$. These two basic forms differ by a sign. What about their coefficients $\partial_m\partial_\ell a_j$ and $\partial_\ell\partial_m a_j$? (Terms with $\ell = m$ vanish on their own.)

> [!note]- Hint 4
> For part 2, recall from [[Ex - Computing wedge products and exterior derivatives]] that a gradient field $\operatorname{grad} f$ corresponds to the $1$-form $df$, and the curl corresponds to $d$ of a $1$-form. So $\operatorname{curl}\operatorname{grad} f$ is $d(df) = d^2 f$. Identify the $2$-form / vector field correspondence and read off the identity.

---

# Solution

The proof is a single observation: applying $d$ twice produces a coefficient that is *symmetric* in two indices, summed against a basic form that is *antisymmetric* in those indices, and a symmetric thing against an antisymmetric thing sums to zero.

**Step 1: apply $d$ twice and expose the double sum.**

For $\alpha = \sum_j a_j\,dx_j$, two applications of $d$ give
$$d(d\alpha) = \sum_{j}\sum_{\ell, m} \frac{\partial^2 a_j}{\partial x_m\,\partial x_\ell}\; dx_m\wedge dx_\ell\wedge dx_{j_1}\wedge\cdots\wedge dx_{j_k}.$$

> [!note]- Derivation
> By definition, $d\alpha = \sum_j\sum_\ell(\partial_\ell a_j)\,dx_\ell\wedge dx_j$, where $dx_j$ abbreviates $dx_{j_1}\wedge\cdots\wedge dx_{j_k}$. This is a $(k+1)$-form whose coefficient (of the basic form $dx_\ell\wedge dx_j$) is the function $\partial_\ell a_j$.
>
> Apply $d$ again. The exterior derivative differentiates each coefficient and wedges on a new differential:
> $$d(d\alpha) = \sum_j\sum_\ell\sum_m \frac{\partial(\partial_\ell a_j)}{\partial x_m}\;dx_m\wedge\big(dx_\ell\wedge dx_j\big) = \sum_j\sum_{\ell, m}\partial_m\partial_\ell a_j\;dx_m\wedge dx_\ell\wedge dx_j.$$
> Since $\alpha$ is smooth, $a_j \in C^\infty$, so the second partials $\partial_m\partial_\ell a_j$ exist and are continuous. The whole expression is a $(k+2)$-form.

**Step 2: pair the $(\ell, m)$ term with the $(m, \ell)$ term — they cancel.**

For each fixed $j$ and each unordered pair $\{\ell, m\}$ with $\ell \neq m$, the double sum contains exactly two terms; their coefficients are equal (Schwarz) and their basic forms are opposite (wedge antisymmetry), so the two cancel. Terms with $\ell = m$ vanish individually. Hence $d(d\alpha) = 0$.

> [!note]- Derivation
> Fix the multi-index $j$. Consider the inner double sum $\sum_{\ell, m}\partial_m\partial_\ell a_j\,dx_m\wedge dx_\ell\wedge dx_j$.
>
> *Diagonal terms ($\ell = m$).* The basic form is $dx_\ell\wedge dx_\ell\wedge dx_j$, which contains a repeated factor and is therefore zero. So every diagonal term drops out.
>
> *Off-diagonal terms ($\ell \neq m$).* Group the term with ordered index $(\ell, m)$ together with the term with ordered index $(m, \ell)$:
> $$\partial_m\partial_\ell a_j\;dx_m\wedge dx_\ell\wedge dx_j \;+\; \partial_\ell\partial_m a_j\;dx_\ell\wedge dx_m\wedge dx_j.$$
> Two facts collapse this to zero. By **Schwarz's theorem on mixed partials** (applicable because $a_j$ is smooth), the two coefficients are equal:
> $$\partial_m\partial_\ell a_j = \partial_\ell\partial_m a_j.$$
> By the **antisymmetry of the wedge product**, swapping the two leading differentials reverses the sign:
> $$dx_\ell\wedge dx_m\wedge dx_j = -\,dx_m\wedge dx_\ell\wedge dx_j.$$
> Substituting, the pair becomes
> $$\partial_m\partial_\ell a_j\;dx_m\wedge dx_\ell\wedge dx_j \;-\; \partial_m\partial_\ell a_j\;dx_m\wedge dx_\ell\wedge dx_j = 0.$$
> Every off-diagonal pair cancels, every diagonal term is already zero, and the sum over $j$ is a sum of zeros. Therefore $d(d\alpha) = 0$.
>
> The proof uses *exactly* two ingredients, and they are dual: a symmetry (of second derivatives) and an antisymmetry (of the wedge). Remove either — work with a non-$C^2$ coefficient so Schwarz fails, or with a commutative product so the wedge is symmetric — and the cancellation breaks. The identity $d^2 = 0$ is precisely the statement that these two facts are in perfect opposition.

**Step 3: deduce $\operatorname{curl}\operatorname{grad} = 0$.**

For a smooth function $f$ on $\mathbb{R}^3$, the gradient field $\operatorname{grad} f$ corresponds to the $1$-form $df$. The curl of a vector field corresponds to $d$ of its $1$-form. Hence $\operatorname{curl}\operatorname{grad} f$ corresponds to $d(df) = 0$, so $\operatorname{curl}\operatorname{grad} f = 0$.

> [!note]- Derivation
> Under the dictionary of [[Ex - Computing wedge products and exterior derivatives]]: a vector field $G = (G_1, G_2, G_3)$ corresponds to the $1$-form $\varphi_G = G_1\,dx + G_2\,dy + G_3\,dz$, and the gradient of $f$ is the vector field whose $1$-form is exactly $df = (\partial_x f)\,dx + (\partial_y f)\,dy + (\partial_z f)\,dz$. So $\varphi_{\operatorname{grad} f} = df$.
>
> The curl is $d$ on $1$-forms: $d\varphi_G$ is the $2$-form whose three coefficients are the components of $\operatorname{curl} G$. Applying this to $G = \operatorname{grad} f$:
> $$d\varphi_{\operatorname{grad} f} = d(df) = 0 \quad\text{by Step 2.}$$
> The $2$-form $d(df)$ is zero, so all three of its coefficients vanish, and those coefficients are the components of $\operatorname{curl}\operatorname{grad} f$. Hence $\operatorname{curl}\operatorname{grad} f = 0$.

**Step 4: deduce $\operatorname{div}\operatorname{curl} = 0$.**

For a smooth vector field $F$ on $\mathbb{R}^3$, the curl corresponds to $d$ of the $1$-form $\varphi_F$, a $2$-form. The divergence corresponds to $d$ of a $2$-form, a $3$-form. Hence $\operatorname{div}\operatorname{curl} F$ corresponds to $d(d\varphi_F) = 0$, so $\operatorname{div}\operatorname{curl} F = 0$.

> [!note]- Derivation
> The vector field $F$ has $1$-form $\varphi_F = F_1\,dx + F_2\,dy + F_3\,dz$. Its exterior derivative $d\varphi_F$ is a $2$-form, and (by the dictionary) the $2$-form encoding a vector field $G$ is $\eta_G = G_1\,dy\wedge dz + G_2\,dz\wedge dx + G_3\,dx\wedge dy$, with $d\varphi_F = \eta_{\operatorname{curl} F}$.
>
> The divergence is $d$ on $2$-forms: $d\eta_G = (\operatorname{div} G)\,dx\wedge dy\wedge dz$. Applying this to $G = \operatorname{curl} F$:
> $$d\eta_{\operatorname{curl} F} = d(d\varphi_F) = 0 \quad\text{by Step 2.}$$
> So $(\operatorname{div}\operatorname{curl} F)\,dx\wedge dy\wedge dz = 0$, forcing $\operatorname{div}\operatorname{curl} F = 0$.

> [!note]- Complete formal solution
> **Part 1.** Write $\alpha = \sum_j a_j\,dx_j$ with $a_j \in C^\infty(\Omega)$. Then $d\alpha = \sum_{j,\ell}\partial_\ell a_j\,dx_\ell\wedge dx_j$, and
> $$d(d\alpha) = \sum_j\sum_{\ell, m}\partial_m\partial_\ell a_j\;dx_m\wedge dx_\ell\wedge dx_j.$$
> Terms with $\ell = m$ have a repeated differential and vanish. For $\ell \neq m$, group $(\ell, m)$ with $(m, \ell)$:
> $$\partial_m\partial_\ell a_j\,dx_m\wedge dx_\ell\wedge dx_j + \partial_\ell\partial_m a_j\,dx_\ell\wedge dx_m\wedge dx_j.$$
> By Schwarz's theorem $\partial_m\partial_\ell a_j = \partial_\ell\partial_m a_j$, and by wedge antisymmetry $dx_\ell\wedge dx_m\wedge dx_j = -\,dx_m\wedge dx_\ell\wedge dx_j$; the pair sums to zero. Hence $d(d\alpha) = 0$.
>
> **Part 2.** In $\mathbb{R}^3$, a vector field $G$ has $1$-form $\varphi_G = \sum G_j\,dx_j$ and $2$-form $\eta_G$; the dictionary gives $\varphi_{\operatorname{grad} f} = df$, $d\varphi_G = \eta_{\operatorname{curl} G}$, and $d\eta_G = (\operatorname{div} G)\,dx\wedge dy\wedge dz$. Then $\operatorname{curl}\operatorname{grad} f$ corresponds to $d(df) = 0$, and $\operatorname{div}\operatorname{curl} F$ corresponds to $d(d\varphi_F) = 0$, both by Part 1. Therefore $\operatorname{curl}\operatorname{grad} f = 0$ and $\operatorname{div}\operatorname{curl} F = 0$. $\blacksquare$

---

# Key Takeaways

**A symmetry summed against an antisymmetry is zero — this is the engine of $d^2 = 0$ and of much else.** The proof contains exactly one idea: the coefficient $\partial_m\partial_\ell a_j$ is symmetric under $\ell \leftrightarrow m$, the basic form $dx_m\wedge dx_\ell\wedge dx_j$ is antisymmetric, and their product summed over all $(\ell, m)$ cancels in pairs. This "symmetric tensor contracted with antisymmetric tensor vanishes" pattern is one of the most reusable facts in all of multilinear algebra and analysis. It appears whenever a symmetric object (a Hessian, a metric, a second derivative) meets an antisymmetric one (a wedge, a determinant, a commutator). Recognizing the pattern lets you predict that an expression vanishes *before* computing it: if you can see one factor is symmetric in two indices and the other antisymmetric in the same two, the sum is zero. The identity $d^2 = 0$ is the cleanest instance, but the technique generalizes far beyond it.

**$d^2 = 0$ is a single fact wearing many costumes, and the costume changes by the degree.** The same proof, applied in degree $0$, gives $\operatorname{curl}\operatorname{grad} = 0$; applied in degree $1$, gives $\operatorname{div}\operatorname{curl} = 0$. A first course in vector calculus presents these as two separate identities, each verified by a separate index computation, and offers no reason they should both be true. The reason is that they are *the same theorem* — the nilpotence of $d$ — read at two different degrees, and the grad/curl/div dictionary is what makes the disguise. The practical lesson: whenever you meet a composite of two vector-calculus operators and suspect it vanishes, do not reach for an index grind; ask whether the inner operator produces an *exact* form (a gradient is $d$ of a function; a curl is $d$ of a $1$-form), and if so, $d^2 = 0$ kills the composite in one line. This is also why the de Rham complex is a *complex*: $d^2 = 0$ is precisely the condition that consecutive arrows compose to zero, which is what makes cohomology — the measurement of closed-modulo-exact — definable at all.

**The hypothesis "smooth" is doing real work, and it is the Schwarz half of the proof.** It is easy to read $d^2 = 0$ as a purely formal identity and forget that it *requires* the coefficients to be twice continuously differentiable, because Schwarz's theorem on the equality of mixed partials can fail for functions whose second partials are not continuous. The standard counterexample — a function whose mixed partials at the origin disagree — would make $d(d\alpha) \neq 0$ if its second partials entered as a form coefficient. This is why the topic insists on *smooth* forms, and why the general Stokes theorem is stated for $C^2$ surfaces: the antisymmetry of the wedge is free, but the symmetry of mixed partials is a genuine analytic hypothesis. When a result in this subject seems "purely algebraic", check whether it secretly leans on Schwarz — $d^2 = 0$ does.
