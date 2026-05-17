---
type: definition
subject: multivariate-analysis
prereqs: []
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is an open set; $f : U \to \mathbb{R}^m$ a function; $x_\circ \in U$ a fixed point; $h \in \mathbb{R}^n$ a small increment. The Euclidean norm of $v \in \mathbb{R}^n$ is $|v| = (v_1^2 + \cdots + v_n^2)^{1/2}$, and the same symbol $|\cdot|$ denotes the norm on $\mathbb{R}^m$ — the dimension is fixed by context. We write $f = o(|h|)$ as $h \to 0$ to mean $|f(h)|/|h| \to 0$. The components of $f$ are $f_1, \dots, f_m : U \to \mathbb{R}$. The full symbol registry is on the parent page [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Axiom Motivation

We want to say what it means for a function $f : \mathbb{R}^n \to \mathbb{R}^m$ to be differentiable, and the honest way to find the right definition is to ask what the one-variable derivative *was* and which of its faces survives the move to many variables.

In one variable, $f'(x_\circ)$ wears several hats: the slope of the tangent line, the limit of difference quotients, the stretching factor of small intervals, and the coefficient of the best linear approximation. These are all the same number when $n = m = 1$, but they generalise very differently. The difference quotient $\big(f(x_\circ + h) - f(x_\circ)\big)/h$ is the first casualty: in several variables $h$ is a *vector*, and you cannot divide by a vector. The slope-of-tangent picture is geometric and suggestive but hard to turn into a clean definition. The viewpoint that survives — cleanly, and with all its power intact — is the **best linear approximation**.

Here is that viewpoint stated carefully in one variable. To say $f$ is differentiable at $x_\circ$ with derivative $a$ is to say $f(x_\circ + h) = f(x_\circ) + a h + R(h)$ where the error $R(h)$ is *negligible compared to $h$*: $R(h)/h \to 0$. The number $a$ is the coefficient that makes the affine function $h \mapsto f(x_\circ) + ah$ hug $f$ better than any other affine function. Now every word of this generalises. The increment $h$ becomes a vector in $\mathbb{R}^n$. The product $ah$ — the action of "multiply by $a$" — becomes the action of a **linear map** $L : \mathbb{R}^n \to \mathbb{R}^m$, because linear maps are exactly the multivariate analogue of "multiply by a scalar": they are the functions that respect addition and scaling, the simplest non-constant functions there are. The error condition $R(h)/h \to 0$ becomes $|R(h)|/|h| \to 0$, which is the statement $R(h) = o(|h|)$.

So the definition writes itself: $f$ is differentiable at $x_\circ$ if there is a linear map $L$ with $f(x_\circ + h) = f(x_\circ) + L(h) + o(|h|)$. The derivative is no longer a number; it is a linear map. This is the one genuine conceptual leap of the entire subject, and it is worth dwelling on *why this is the right definition and not a nearby variant*.

Why demand a *linear* map, rather than merely a continuous one, or an affine one? Because "differentiable" should mean "well-approximated by something simple", and linear maps are the precise notion of simple. An affine approximation $h \mapsto c + L(h)$ would force $c = f(x_\circ)$ anyway (set $h = 0$), so affine adds nothing. Allowing $L$ to be merely continuous would make the condition vacuous — every continuous $f$ would be "differentiable" with $L = f(x_\circ + \cdot) - f(x_\circ)$ — so linearity is exactly the constraint that gives the definition content.

Why the error condition $o(|h|)$ rather than something weaker or stronger? Weaken it to $o(1)$ — error merely going to zero — and you have only required continuity, since then $f(x_\circ + h) \to f(x_\circ)$; the derivative would carry no information. Strengthen it to $O(|h|^2)$ — error quadratically small — and you would exclude perfectly good differentiable functions like $f(x) = x^{3/2}$ near... well, in one variable $x|x|^{1/2}$, whose error is $o(|h|)$ but not $O(|h|^2)$. The condition $o(|h|)$ is the Goldilocks rate: it is exactly the threshold at which the linear term $L$ is *forced to be unique* (this is the content of the exercise below — two linear maps both fitting to $o(|h|)$ must coincide) while still admitting every function we want to call differentiable. Uniqueness is non-negotiable: a "derivative" that depended on a choice would not be an invariant of $f$.

One last design choice, easy to overlook: why insist the domain $U$ be *open*? Because the limit $h \to 0$ must be taken over *all* directions of approach. At a boundary point some directions leave the domain, and the linear approximation would only be tested on a partial cone of directions — the definition would weaken silently and the derivative could fail to be unique. Openness guarantees a full ball around $x_\circ$ on which the increment $h$ ranges freely, which is exactly what makes "approximation in every direction" a meaningful demand.

---

# The Definition

Let $U \subseteq \mathbb{R}^n$ be open and $f : U \to \mathbb{R}^m$ a function. We say $f$ is **differentiable at** $x_\circ \in U$ if there exists a linear map $L : \mathbb{R}^n \to \mathbb{R}^m$ such that
$$\lim_{h \to 0} \frac{\big|\, f(x_\circ + h) - f(x_\circ) - L(h) \,\big|}{|h|} = 0.$$
Equivalently, writing the remainder $R(h) = f(x_\circ + h) - f(x_\circ) - L(h)$, the condition is $R(h) = o(|h|)$ as $h \to 0$, so that
$$f(x_\circ + h) = f(x_\circ) + L(h) + o(|h|).$$
If such an $L$ exists it is **unique**; it is called the **total derivative** (or **differential**) of $f$ at $x_\circ$, written $Df_{x_\circ}$ or $Df(x_\circ)$. The function $f$ is **differentiable on** $U$ if it is differentiable at every point of $U$.

**Uniqueness.** Suppose $L$ and $L'$ both satisfy the condition. Then $(L - L')(h) = o(|h|)$ as $h \to 0$. For any fixed direction $v \neq 0$, put $h = sv$ with $s \downarrow 0$: linearity gives $(L - L')(sv) = s\,(L-L')(v)$, so $|(L-L')(v)| = |(L-L')(sv)|/s = |(L-L')(sv)|/(|sv|/|v|) = |v| \cdot |(L-L')(sv)|/|sv| \to 0$. Since the left side does not depend on $s$, it is zero, so $(L - L')(v) = 0$ for every $v$, hence $L = L'$.

**Componentwise characterisation.** $f$ is differentiable at $x_\circ$ if and only if each component $f_j : U \to \mathbb{R}$ is differentiable at $x_\circ$, and then $(Df_{x_\circ})_j = (Df_j)_{x_\circ}$ — the $j$-th component of the derivative is the derivative of the $j$-th component. This holds because $|R(h)| \to 0$ at the rate $o(|h|)$ if and only if each $|R_j(h)|$ does, the Euclidean norm being squeezed between the maximum and the sum of the coordinate norms.

---

# Relate to Other Fields / Compression

This definition is the one-variable derivative with "multiplication by a scalar" replaced by "a linear map", and that replacement is the entire generalisation. In one variable the linear maps $\mathbb{R} \to \mathbb{R}$ are exactly the scalar multiplications $h \mapsto ah$, so the linear map $L$ and the number $a = f'(x_\circ)$ carry the same information and the distinction collapses. In several variables the space $\operatorname{Hom}(\mathbb{R}^n, \mathbb{R}^m)$ of linear maps is genuinely larger, and the derivative is one element of it.

The same definition, with $\mathbb{R}^n$ and $\mathbb{R}^m$ replaced by Banach spaces and "linear map" replaced by "bounded linear operator", is the **Fréchet derivative** of functional analysis — the foundation of the calculus of variations and of infinite-dimensional optimisation. Nothing in the definition above used finite-dimensionality except the convenience of components; the genuine content is the $o(|h|)$ approximation by a bounded linear operator. In differential geometry the same idea localised to charts becomes the **differential** $df_p$ of a smooth map between manifolds, a linear map between tangent spaces. The definition here is the common ancestor: differentiability always means "admits a best linear approximation with negligible remainder", and only the ambient spaces and the meaning of "linear" change.

---

# Examples / Corollaries

**Is an instance — every linear map.** If $f = L$ is itself linear, then $f(x_\circ + h) = f(x_\circ) + L(h)$ exactly, with remainder $R(h) = 0 = o(|h|)$. So a linear map is differentiable everywhere and is its own derivative, $Df_{x_\circ} = L$ at every point. This is the sanity check: the best linear approximation to a linear function is the function itself.

**Is an instance — a constant map.** If $f \equiv c$, then $f(x_\circ + h) - f(x_\circ) = 0$, so $L = 0$ works and $Df_{x_\circ}$ is the zero map. Differentiable, derivative zero — as it should be.

**Is an instance — $f(x, y) = (\sin x)(\sin y)$.** This is differentiable everywhere with $Df_{(x,y)}(h_1, h_2) = (\cos x \sin y)\,h_1 + (\sin x \cos y)\,h_2$. One can verify the $o(|h|)$ condition directly from the one-variable Taylor expansions of $\sin$, but in practice one invokes [[Thm - Continuous Partials Imply Differentiability]]: the partials are continuous, so $f$ is differentiable and its derivative is read off from the partials.

**Is NOT an instance — $f(x,y) = xy/(x^2+y^2)$, extended by $f(0,0) = 0$.** This function is not differentiable at the origin — indeed it is not even continuous there, since $f(t,t) = t^2/(2t^2) = \tfrac12$ for all $t \neq 0$ while $f(0,0) = 0$. By [[Thm - Differentiability Implies Continuity]], a discontinuous function cannot be differentiable. Note that both partial derivatives $\partial_x f(0,0)$ and $\partial_y f(0,0)$ nonetheless *exist* and equal $0$ (the function is identically zero on each axis). This is the canonical demonstration that the existence of partials is strictly weaker than differentiability; see [[Ex - Partial derivatives exist without differentiability]].

**Is NOT an instance — the norm $f(x) = |x|$ at the origin.** The Euclidean norm $f : \mathbb{R}^n \to \mathbb{R}$ is differentiable everywhere except at $0$. At $0$, no linear $L$ can satisfy the condition: along $h$ and along $-h$ the increment $|h| - 0$ is the same positive number, but any linear $L$ has $L(-h) = -L(h)$, so $L$ cannot match the increment in both directions. This is the multivariate analogue of $|x|$ failing to be differentiable at $0$ in one variable — a corner.

**Corollary — the derivative, if it exists, is forced.** Because $L$ is unique, the derivative is an invariant of $f$ at $x_\circ$, not a matter of choice. In particular, once differentiability is known, $L$ can be computed by any valid method — for instance from the partial derivatives — and the answer is guaranteed to be *the* derivative. This is what licenses the legal operation "recover the derivative from the partials".

**Calibration check.** Convince yourself that the projection $(x, y) \mapsto x$ is differentiable with derivative the projection itself; that $f(x,y) = x^2 + y^2$ has derivative $Df_{(x,y)}(h_1,h_2) = 2x\,h_1 + 2y\,h_2$ (verify the remainder $h_1^2 + h_2^2$ is $o(|h|)$); and that if $f$ is differentiable at $x_\circ$ then so is $cf$ for any scalar $c$, with $D(cf)_{x_\circ} = c\,Df_{x_\circ}$. If you can also explain why the domain must be open, you have understood every clause.

---

# Unlocked by This

> [!tip] The Fréchet Derivative *(from Functional Analysis)*
> Replacing $\mathbb{R}^n, \mathbb{R}^m$ by Banach spaces and "linear map" by "bounded linear operator" gives the **Fréchet derivative** — the same $o(|h|)$ condition, verbatim. This is the derivative used to differentiate functionals over infinite-dimensional function spaces, the technical core of the calculus of variations.

> [!tip] The Differential of a Smooth Map *(from Differential Geometry)*
> Computed chart by chart, this definition becomes the **differential** $df_p : T_p M \to T_{f(p)} N$ between tangent spaces of manifolds. The insistence here on "linear map" rather than "Jacobian matrix" is exactly what makes the manifold version well-defined, since a manifold has no canonical basis.
