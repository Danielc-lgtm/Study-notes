---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ and $V \subseteq \mathbb{R}^m$ are open; $f : U \to V$ and $g : V \to \mathbb{R}^k$ are functions; $x_\circ \in U$ and $z_\circ = f(x_\circ) \in V$. The total derivative is $Df_{x_\circ} : \mathbb{R}^n \to \mathbb{R}^m$ (see [[Def - The Total Derivative and Differentiability]]); $Jf(x_\circ)$ is its Jacobian matrix (see [[Def - Partial Derivatives and the Jacobian Matrix]]); $\|L\|$ is the operator norm of a linear map $L$. The composite is $g \circ f : U \to \mathbb{R}^k$, $(g\circ f)(x) = g(f(x))$. The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Statement

> **The Chain Rule.** Let $U \subseteq \mathbb{R}^n$ and $V \subseteq \mathbb{R}^m$ be open, $f : U \to V$ differentiable at $x_\circ \in U$, and $g : V \to \mathbb{R}^k$ differentiable at $z_\circ = f(x_\circ)$. Then the composite $g \circ f : U \to \mathbb{R}^k$ is differentiable at $x_\circ$, and its derivative is the composite of the derivatives:
> $$D(g \circ f)_{x_\circ} = Dg_{f(x_\circ)} \circ Df_{x_\circ}.$$
> Equivalently, at the level of Jacobian matrices, $D(g\circ f)$ is the **matrix product**
> $$J(g \circ f)(x_\circ) = Jg(f(x_\circ)) \cdot Jf(x_\circ),$$
> and componentwise $\dfrac{\partial (g\circ f)_i}{\partial x_j}(x_\circ) = \sum_{\ell=1}^m \dfrac{\partial g_i}{\partial z_\ell}(f(x_\circ))\,\dfrac{\partial f_\ell}{\partial x_j}(x_\circ)$.

---

# Motivation

Single-variable calculus has the chain rule $(g\circ f)'(x) = g'(f(x))\,f'(x)$ — to differentiate a composite, multiply the derivatives. The question this theorem answers is: what survives when $f$ and $g$ are maps between Euclidean spaces of arbitrary dimension?

The answer is the cleanest possible generalisation, and it is the conceptual centrepiece of the whole topic. In one variable the derivative is a number and the rule is "multiply the numbers". In several variables the derivative is a *linear map*, and the rule is "**compose the linear maps**": $D(g\circ f) = Dg \circ Df$. This is not merely an analogy — it is the same statement, because in one variable the linear maps $\mathbb{R}\to\mathbb{R}$ are exactly the scalar multiplications, and composing two scalar multiplications *is* multiplying the scalars. The chain rule says the construction $f \mapsto Df$ respects composition; it is, in the language of category theory, the statement that $D$ is a functor.

Why should one expect this? Differentiability means $f$ is approximated near $x_\circ$ by its linear part, and $g$ is approximated near $z_\circ$ by its linear part. The composite $g\circ f$ is then approximated by the composite of those linear parts — and the composite of two linear maps is again linear, so $g\circ f$ has a linear approximation, which is exactly differentiability. The only real work in the proof is checking that the *remainders* of the two approximations, when composed, do not spoil this — and they do not.

The matrix form of the rule, $J(g\circ f) = Jg \cdot Jf$, is where the theorem pays a structural dividend. Matrix multiplication is not an arbitrary definition; it was *constructed* so that the matrix of a composite of linear maps is the product of the matrices. The chain rule is the place that construction earns its keep: it says differentiating a composite is matrix multiplication. This is also the form that turns into the transformation law of tensor calculus — the Jacobian is how components transform under a change of coordinates, and the chain rule for a chain of coordinate changes is the consistency of those transformations. Computationally, the chain rule is the single most-used tool in the topic: every coordinate change, every function presented as a chain of simpler maps, is differentiated by it.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ differentiable at $x_\circ$, $g$ differentiable at $f(x_\circ)$".

The first disguised source is **$f$ and $g$ are $C^1$**. The property $B$ is "$f \in C^1(U)$ and $g \in C^1(V)$". The bridge is [[Thm - Continuous Partials Imply Differentiability]]: $C^1$ implies differentiable at every point. The implication is so routine it is invisible, but it is the practical entry point: in applications one almost never verifies differentiability directly — one checks the partials are continuous. *Example problem:* the composite of two coordinate changes given by explicit smooth formulas is differentiable, and its Jacobian is the matrix product.

The second disguised source is **$f$ is a curve, $g$ is a scalar field** — the case $n = 1$. The property $B$ is "$\gamma : I \to V$ is a differentiable curve and $g : V \to \mathbb{R}$ is differentiable". The bridge is that the chain rule specialises to $(g\circ\gamma)'(t) = Dg_{\gamma(t)}(\gamma'(t)) = \nabla g(\gamma(t)) \cdot \gamma'(t)$. The nonobviousness is in recognising that "rate of change of $g$ along a moving point" is an instance of the chain rule. *Example problem:* the rate of change of temperature felt by a particle moving through a temperature field.

The third disguised source is **$f$ has the special structure $x \mapsto x_\circ + tv$ — restriction to a line**. The property $B$ is "$f(t) = x_\circ + tv$ is an affine curve". The bridge is that the chain rule then computes $\frac{d}{dt} g(x_\circ + tv) = Dg_{x_\circ+tv}(v) = \partial_v g$. This is the most important disguised source: it is how the mean value theorem and Taylor's theorem are *proved*. *Example problem:* any time a multivariate problem is reduced to a one-variable problem along a segment.

**Targets (Output Amplification)**

The conclusion is "$g\circ f$ differentiable, with $D(g\circ f) = Dg\circ Df$".

Combine the conclusion with **the structure of $f$ as a coordinate change**. If $f$ is an invertible coordinate change, applying the chain rule to $f \circ f^{-1} = \mathrm{id}$ gives $Df_{f^{-1}(y)} \circ D(f^{-1})_y = \mathrm{id}$, so $D(f^{-1})_y = (Df)^{-1}$ — the derivative of the inverse is the inverse of the derivative. The further result $E$ is the differentiation rule for inverse functions, and the recognition that $Df$ must be an *invertible* linear map for $f$ to be invertible. This is the seed of the inverse function theorem (**Multivariate Analysis II**).

Combine the conclusion with **a known invariance of $f$ or $g$**. If $g$ satisfies an identity — homogeneity, symmetry, constancy along a family — composing with a suitable $f$ and applying the chain rule extracts a relation among the partials. The further result $E$ is **Euler's identity** for homogeneous functions: from $g(tx) = t^\lambda g(x)$, differentiating in $t$ at $t = 1$ via the chain rule yields $\sum_j x_j \partial_j g(x) = \lambda g(x)$. The combination is nonobvious because it converts a global symmetry into a local differential identity.

Combine the conclusion with **the one-variable calculus toolkit**. Restricting a multivariate $g$ to a curve produces a one-variable function to which the mean value theorem, Taylor's theorem, and the fundamental theorem of calculus all apply; the chain rule is the translation dictionary. The further result $E$ is the entire program of proving multivariate theorems by reduction to one variable. This is the chain rule's most structural use.

---

# Why Is It True

The intuition is to think of differentiability as a *promise of linear approximation*, and to compose the promises.

When $f$ is differentiable at $x_\circ$, it promises: near $x_\circ$, $f$ behaves like the affine map $h \mapsto f(x_\circ) + Df_{x_\circ}(h)$, with an error negligible against $|h|$. When $g$ is differentiable at $z_\circ = f(x_\circ)$, it promises: near $z_\circ$, $g$ behaves like $w \mapsto g(z_\circ) + Dg_{z_\circ}(w)$, with an error negligible against the input displacement.

Now feed $f$'s output into $g$. A point $x_\circ + h$ near $x_\circ$ is sent by $f$ to a point near $z_\circ$, displaced by approximately $Df_{x_\circ}(h)$. Then $g$ acts on that, displacing $g$'s value by approximately $Dg_{z_\circ}$ applied to that displacement — that is, by approximately $Dg_{z_\circ}\big(Df_{x_\circ}(h)\big)$. So the net effect of $g\circ f$ on the displacement $h$ is, to leading order, $Dg_{z_\circ}\circ Df_{x_\circ}$ applied to $h$. The composite of two linear maps is a linear map, so $g\circ f$ is approximated near $x_\circ$ by an affine map whose linear part is $Dg_{z_\circ}\circ Df_{x_\circ}$ — and being approximated by an affine map with negligible error *is* differentiability, with that linear part as the derivative.

One should expect this for the same reason one expects $(ab)$ to be the scaling factor when you scale by $b$ and then by $a$: each map *multiplies displacements by its derivative* (now a linear map rather than a number), and doing two maps in succession multiplies by the two derivatives in succession. The derivative is the "amplification factor" of a map, and amplification factors of a composition multiply — here, compose.

The only thing the intuition glosses is the errors. Each promise comes with a remainder, and the proof must check that when you compose, the remainders do not accumulate into something larger than $o(|h|)$. They do not, for two reasons that the proof makes precise: $g$'s linear part $Dg_{z_\circ}$ is a *bounded* linear map, so it cannot inflate $f$'s small remainder $R_f(h) = o(|h|)$ into anything worse than $o(|h|)$; and $g$'s own remainder $R_g$, being $o(\text{its input})$ and fed an input of size $O(|h|)$, is itself $o(|h|)$. Boundedness of the linear maps is the quiet hypothesis that keeps the errors in line — the same boundedness that made [[Thm - Differentiability Implies Continuity|differentiability imply continuity]].

---

# What Makes This Hard

The non-obvious step is not the formula — "compose the derivatives" is easy to guess — but the **error bookkeeping**: showing that the total remainder $R_2(h) = Dg(R_f(h)) + R_g(Df(h) + R_f(h))$ is $o(|h|)$. The two error terms are controlled differently and the proof must handle each: the first because $Dg$ is a *bounded* linear map (so it does not inflate $f$'s $o(|h|)$ remainder), the second because $g$'s remainder $R_g$ is $o$ of *its* input, and that input has size $O(|h|)$. The most common error is to treat $R_g(Df(h)+R_f(h))$ as automatically $o(|h|)$ without noting that $g$'s remainder is small relative to $g$'s input, not relative to $h$, so the input must first be shown to be $O(|h|)$. A second frequent slip is getting the order of composition backwards — it is $Dg \circ Df$ (outer derivative first), matching $Jg \cdot Jf$, not the reverse.

---

# Rederivation Scaffold

**High-level strategy:**
Substitute $f$'s linear approximation into $g$'s linear approximation. Collect everything linear in $h$ — this gives the candidate derivative $Dg\circ Df$ — and bundle everything else into a remainder $R_2(h)$. Then show $R_2(h) = o(|h|)$ by controlling its two pieces with boundedness of $Dg$ and with the smallness of $g$'s remainder.

**Subgoal decomposition:**

1. **Write both approximations.** $f(x_\circ + h) = f(x_\circ) + Df_{x_\circ}(h) + R_f(h)$ with $R_f = o(|h|)$; $g(z_\circ + w) = g(z_\circ) + Dg_{z_\circ}(w) + R_g(w)$ with $R_g(w) = o(|w|)$.
   - *Hint:* This is just the definition of differentiability for each of $f$ and $g$.
   - *Why needed:* The two approximations are the raw material to be composed.

2. **Substitute.** Set $w = f(x_\circ + h) - f(x_\circ) = Df_{x_\circ}(h) + R_f(h)$, and expand $g(f(x_\circ + h))$.
   - *Hint:* Plug $w$ into $g$'s formula; use linearity of $Dg_{z_\circ}$ to split $Dg_{z_\circ}(w)$.
   - *Why needed:* It produces the linear-in-$h$ term and isolates the remainder.

3. **Identify the linear term and the remainder.** The linear part is $Dg_{z_\circ}(Df_{x_\circ}(h))$; everything else is $R_2(h) = Dg_{z_\circ}(R_f(h)) + R_g(w)$.
   - *Hint:* The candidate derivative is $Dg_{z_\circ}\circ Df_{x_\circ}$, a composite of linear maps, hence linear.
   - *Why needed:* It names what must be proved differentiable-with-derivative.

4. **Show $R_2(h) = o(|h|)$.** Bound each piece.
   - *Hint:* $|Dg_{z_\circ}(R_f(h))| \le \|Dg_{z_\circ}\|\,|R_f(h)| = o(|h|)$. For $R_g(w)$: first show $|w| \le C|h|$ for small $h$ (boundedness of $Df$ plus $|R_f| \le |h|$), then $R_g(w) = o(|w|) = o(|h|)$.
   - *Why needed:* It verifies the $o(|h|)$ condition, completing the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: A bounded linear map sends an $o(|h|)$ quantity to an $o(|h|)$ quantity
> **Statement:** If $L : \mathbb{R}^m \to \mathbb{R}^k$ is linear and $R(h) = o(|h|)$ as $h\to0$, then $L(R(h)) = o(|h|)$.
>
> **Hint:** Use $|L(R(h))| \le \|L\|\,|R(h)|$.
>
> **Why needed:** It controls the first error term, $Dg_{z_\circ}(R_f(h))$ — $g$'s linear part cannot inflate $f$'s small remainder.
>
> > [!note]- Full proof
> > A linear map on $\mathbb{R}^m$ is bounded: $|L(v)| \le \|L\|\,|v|$ for a finite constant $\|L\|$. Hence $|L(R(h))| \le \|L\|\,|R(h)|$, so $|L(R(h))|/|h| \le \|L\|\cdot|R(h)|/|h| \to \|L\|\cdot 0 = 0$. Thus $L(R(h)) = o(|h|)$.

> [!note]- Lemma 2: The intermediate displacement is $O(|h|)$
> **Statement:** With $w = w(h) = Df_{x_\circ}(h) + R_f(h)$, there is a constant $C$ and a radius $\delta > 0$ such that $|w(h)| \le C|h|$ for $|h| < \delta$.
>
> **Hint:** Bound the linear part by $\|Df_{x_\circ}\|\,|h|$ and the remainder by $|h|$ (valid once $|h|$ is small, since $|R_f(h)|/|h| \to 0$).
>
> **Why needed:** $g$'s remainder $R_g$ is small relative to *its input* $w$; to convert that into smallness relative to $h$, the input $w$ must be shown to be at most a constant times $|h|$.
>
> > [!note]- Full proof
> > $|w(h)| \le |Df_{x_\circ}(h)| + |R_f(h)| \le \|Df_{x_\circ}\|\,|h| + |R_f(h)|$. Since $R_f(h) = o(|h|)$, there is $\delta > 0$ with $|R_f(h)| \le |h|$ for $|h| < \delta$. Then $|w(h)| \le (\|Df_{x_\circ}\| + 1)\,|h| =: C|h|$ for $|h| < \delta$.

> [!note]- Lemma 3: $g$'s remainder composed with $w$ is $o(|h|)$
> **Statement:** $R_g(w(h)) = o(|h|)$ as $h \to 0$.
>
> **Hint:** Write $|R_g(w)|/|h| = \big(|R_g(w)|/|w|\big)\cdot\big(|w|/|h|\big)$ and use Lemma 2.
>
> **Why needed:** It controls the second error term — the contribution of $g$'s own remainder.
>
> > [!note]- Full proof
> > For $h$ with $w(h) \neq 0$, factor $|R_g(w)|/|h| = \big(|R_g(w)|/|w|\big)\cdot\big(|w|/|h|\big)$. As $h \to 0$, $w \to 0$ (Lemma 2 gives $|w| \le C|h| \to 0$), so the first factor $|R_g(w)|/|w| \to 0$ because $R_g(w) = o(|w|)$. The second factor is bounded by $C$ (Lemma 2). A factor tending to $0$ times a bounded factor tends to $0$, so $|R_g(w)|/|h| \to 0$. When $w(h) = 0$, $R_g(w) = R_g(0) = 0$, contributing nothing. Hence $R_g(w(h)) = o(|h|)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : U \to V$ be differentiable at $x_\circ$ and $g : V \to \mathbb{R}^k$ differentiable at $z_\circ = f(x_\circ)$. Write $L = Df_{x_\circ}$ and $M = Dg_{z_\circ}$, both linear.
>
> By differentiability of $f$ and $g$, for small $h$ and small $w$,
> $$f(x_\circ + h) = f(x_\circ) + L(h) + R_f(h), \qquad R_f(h) = o(|h|),$$
> $$g(z_\circ + w) = g(z_\circ) + M(w) + R_g(w), \qquad R_g(w) = o(|w|).$$
>
> Fix small $h$ and set $w = w(h) = f(x_\circ + h) - f(x_\circ) = L(h) + R_f(h)$, so $f(x_\circ + h) = z_\circ + w$. Then
> $$
> \begin{aligned}
> (g\circ f)(x_\circ + h) &= g(z_\circ + w) = g(z_\circ) + M(w) + R_g(w) \\
> &= (g\circ f)(x_\circ) + M\big(L(h) + R_f(h)\big) + R_g(w) \\
> &= (g\circ f)(x_\circ) + \underbrace{M(L(h))}_{\text{linear in } h} + \underbrace{M(R_f(h)) + R_g(w)}_{=: \, R_2(h)},
> \end{aligned}
> $$
> using the linearity of $M$ to split $M(L(h) + R_f(h)) = M(L(h)) + M(R_f(h))$.
>
> The map $h \mapsto M(L(h)) = (M\circ L)(h)$ is linear, being a composite of linear maps. It remains to show $R_2(h) = o(|h|)$.
>
> *First term.* By Lemma 1, since $M$ is a bounded linear map and $R_f(h) = o(|h|)$, we have $M(R_f(h)) = o(|h|)$.
>
> *Second term.* By Lemma 2, $|w(h)| \le C|h|$ for small $h$; by Lemma 3, $R_g(w(h)) = o(|h|)$.
>
> Therefore $R_2(h) = M(R_f(h)) + R_g(w(h))$ is a sum of two $o(|h|)$ quantities, hence $o(|h|)$.
>
> We have shown $(g\circ f)(x_\circ + h) = (g\circ f)(x_\circ) + (M\circ L)(h) + o(|h|)$, so by the definition of differentiability $g\circ f$ is differentiable at $x_\circ$ with
> $$D(g\circ f)_{x_\circ} = M\circ L = Dg_{f(x_\circ)} \circ Df_{x_\circ}.$$
> Passing to matrices in the standard bases, the matrix of a composite of linear maps is the product of the matrices, so $J(g\circ f)(x_\circ) = Jg(f(x_\circ))\cdot Jf(x_\circ)$, and the $(i,j)$ entry of this product is $\sum_\ell \partial_{z_\ell} g_i\,\partial_{x_j} f_\ell$, the componentwise chain rule. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Differentiating the determinant.** The map $\det : GL(n,\mathbb{R}) \to \mathbb{R}$ composed with a matrix-valued curve $t \mapsto A(t)$ yields, by the chain rule, **Jacobi's formula** $\frac{d}{dt}\det A(t) = \det A(t)\cdot\operatorname{tr}\big(A(t)^{-1}A'(t)\big)$. The application is nonobvious because the derivative of the determinant looks like a combinatorial nightmare until the chain rule organises it.

**Polar, spherical, and arbitrary coordinate changes.** Whenever a partial differential equation is rewritten in new coordinates — the Laplacian in polar coordinates, say — every derivative transforms by the chain rule applied to the coordinate change. The application is nonobvious in that the messy coordinate-changed PDE is, mechanically, just $Jg\cdot Jf$ unpacked.

**Backpropagation in neural networks.** A deep network is a long composite $g_L \circ \cdots \circ g_1$ of differentiable layers; training computes the gradient of the loss by the chain rule, $J(g_L\circ\cdots\circ g_1) = Jg_L\cdots Jg_1$, evaluated right-to-left. The application is out-of-distribution because "backpropagation" sounds like an algorithm of its own, whereas it is precisely the matrix-product form of the chain rule, computed in a memory-efficient order.

**Euler's identity for homogeneous functions.** If $f$ is positively homogeneous of degree $\lambda$, $f(rx) = r^\lambda f(x)$, differentiating both sides in $r$ via the chain rule and setting $r = 1$ gives $\sum_j x_j\partial_j f(x) = \lambda f(x)$. The application is nonobvious because a global scaling symmetry is converted into a pointwise differential identity by a single use of the chain rule.

---

# Bridges

- **The one-variable chain rule $(g\circ f)' = g'(f)\,f'$** — the special case $n = m = k = 1$. There the linear maps are scalar multiplications and composing them is multiplying the scalars, so "compose the derivatives" reads as "multiply the derivatives".

- **[[Thm - The Mean Value Inequality|The Mean Value Inequality]]** and **[[Thm - Taylor's Theorem in Several Variables|Taylor's Theorem]]** — both are proved by restricting the function to a line, $\varphi(t) = f(x_\circ + tv)$, and the chain rule is exactly what computes $\varphi'(t) = Df_{x_\circ+tv}(v)$. The chain rule is the bridge over which one-variable calculus enters several variables.

- **Matrix multiplication** — the operation was *defined* so that the matrix of a composite of linear maps is the product of matrices. The chain rule $J(g\circ f) = Jg\cdot Jf$ is the calculus statement that this definition is the right one.

- **The differential of a smooth map between manifolds** — the chain rule is the theorem guaranteeing that $df_p$, computed in charts, is independent of the chart chosen, since two charts differ by a transition map and the chain rule makes the derivatives transform consistently.

- **Functoriality** — "$D$ respects composition" is the statement that the derivative is a functor from the category of pointed differentiable maps to the category of linear maps; the chain rule is functoriality made explicit.

---

# Unlocked by This

> [!tip] The Inverse Function Theorem *(from Multivariate Analysis II)*
> Applying the chain rule to $f^{-1}\circ f = \mathrm{id}$ gives $D(f^{-1}) = (Df)^{-1}$ — the derivative of the inverse is the inverse of the derivative. This forces $Df$ to be an invertible linear map wherever $f$ is invertible, and the **inverse function theorem** is the converse: an invertible derivative makes $f$ locally invertible.

> [!tip] The Transformation Law of Tensors *(from Tensor Calculus and Special Relativity)*
> Under a coordinate change $x \mapsto \tilde x$, vector and tensor components transform by the Jacobian, and the chain rule for a chain of coordinate changes is the consistency of this transformation. Demanding that physical laws be tensor equations — invariant under all such changes — is the organising principle of **tensor calculus** and of relativity.
