---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Higher-Order Derivatives and Ck Maps"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f : U \to \mathbb{R}$ (the vector-valued case reduces componentwise). Second partials are $\partial_i\partial_j f = \partial_i(\partial_j f)$. The class $C^2(U)$ consists of functions whose first and second partials all exist and are continuous (see [[Def - Higher-Order Derivatives and Ck Maps]]). The standard basis is $e_1, \dots, e_n$. The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Statement

> **Schwarz's Theorem (equality of mixed partials).** Let $U \subseteq \mathbb{R}^n$ be open and $f \in C^2(U)$. Then for every $x \in U$ and all indices $i, j \in \{1, \dots, n\}$,
> $$\partial_i\partial_j f(x) = \partial_j\partial_i f(x).$$
> The order of differentiation in a mixed second partial is irrelevant. Consequently, for $f \in C^k(U)$ and any indices $i_1, \dots, i_k$, the partial $\partial_{i_1}\cdots\partial_{i_k} f$ is unchanged under any permutation of the indices — so $\partial^\alpha f$ in multi-index notation is well-defined.

---

# Motivation

A higher derivative of a multivariate function is, on its face, an *ordered* operation: differentiate in $x_j$, then in $x_i$, and a priori swapping the two could give a different answer. If it did, the entire bookkeeping of higher derivatives would be a combinatorial nightmare — a $k$-th derivative would carry an ordered string of $k$ indices, the Hessian would not be symmetric, the multinomial coefficients in Taylor's theorem would not collapse, and multi-index notation would be meaningless. Schwarz's theorem is the result that rescues all of this: under a mild and natural hypothesis, the order does not matter.

The hypothesis is exactly "$f \in C^2$": the second partials exist and are continuous. This is mild — every function given by an honest formula satisfies it — and the theorem then says all mixed partials of order two commute. The same hypothesis at order $k$ ($f \in C^k$) makes all partials of order $\le k$ order-independent, since any permutation is a composite of adjacent transpositions and each adjacent transposition is a single instance of the $C^2$ result.

Why should one expect commutativity? The clue is a symmetric quantity. Look at the "second difference" of $f$ over a small square with corner $(x_1, x_2)$ and side $h$: the alternating sum $f(x_1+h, x_2+h) - f(x_1+h, x_2) - f(x_1, x_2+h) + f(x_1, x_2)$. This number is *manifestly symmetric* under swapping the two coordinates — it is the same expression. And it can be related to *both* $\partial_2\partial_1 f$ and $\partial_1\partial_2 f$ by reading the square's two pairs of opposite edges in the two possible orders. Two readings of one symmetric quantity, in the limit, must agree. That is the whole idea; the theorem is the rigorous version, and continuity of the second partials is what licenses the limit.

The necessity of the continuity hypothesis is not pedantry. There genuinely exist functions whose mixed partials *both exist* yet *disagree* — the standard one is $xy(x^2-y^2)/(x^2+y^2)$ at the origin, with $\partial_x\partial_y f = -1$ but $\partial_y\partial_x f = +1$ (see [[Ex - A function with unequal mixed partials]]). For that function the second partials exist but are not continuous at the origin, and the limit step of the proof fails. So Schwarz's theorem is a genuine theorem with a genuine hypothesis, and the hypothesis is the precise dividing line.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f \in C^2$" — second partials exist and are continuous.

The first disguised source is **$f$ is given by an elementary formula**. The property $B$ is "$f$ is built from polynomials, exponentials, and trigonometric functions". The bridge is that such an $f$ is $C^\infty$, hence $C^2$, so its mixed partials commute automatically. The implication is invisible in practice — one swaps partials of an explicit formula without a second thought — but it is exactly this theorem being used. *Example problem:* verifying $\partial_x\partial_y f = \partial_y\partial_x f$ for any explicit $f$ needs no computation, only the observation that $f$ is smooth.

The second disguised source is **$f$ is a solution of a second-order PDE with continuous data**. The property $B$ is "$f$ is $C^2$ because the equation forces it (or by an elliptic regularity argument)". The bridge is that once $C^2$ is known, the symmetry of the Hessian is available. *Example problem:* in deriving the heat or wave equation, one freely commutes $\partial_t\partial_x$ — legal because the solution is $C^2$.

The third disguised source is **$f$ has continuous second partials on a region but is only claimed $C^2$ there, not globally**. The property $B$ is "$f \in C^2$ on an open subset $V \subseteq U$". The bridge is that the theorem is local — it holds at every point where $f$ is $C^2$ — so the conclusion holds on $V$ even if $f$ misbehaves elsewhere. *Example problem:* a piecewise function that is $C^2$ away from a bad set has symmetric Hessian everywhere on the good set.

**Targets (Output Amplification)**

The conclusion is "$\partial_i\partial_j f = \partial_j\partial_i f$".

Combine the conclusion with **the matrix of second partials**. The Hessian $D^2 f = (\partial_i\partial_j f)$ is then a *symmetric* matrix. The further result $E$: by the spectral theorem, $D^2 f$ has an orthonormal eigenbasis and real eigenvalues, so its definiteness is a clean eigenvalue criterion — the basis of the second-derivative test for extrema. The combination is nonobvious because symmetry of the Hessian is what connects calculus to the spectral theory of linear algebra.

Combine the conclusion with **the multinomial theorem**. Since order does not matter, the $k$-th derivative depends only on the *counts* $\alpha$, and the number of orderings realising a given count is the multinomial coefficient $k!/\alpha!$. The further result $E$: the multivariate Taylor expansion has coefficients $\partial^\alpha f/\alpha!$ rather than an unmanageable sum over ordered strings — this theorem is what makes [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] compact.

Combine the conclusion with **a string of partials of order $> 2$**. Any permutation of $k$ indices is a product of adjacent transpositions; each adjacent transposition is one application of Schwarz. The further result $E$: all partials of order $\le k$ of a $C^k$ function are order-independent, so $\partial^\alpha f$ is well-defined for all $|\alpha| \le k$. The combination is the bridge from the order-$2$ statement to the full multi-index calculus.

---

# Why Is It True

The intuition lives in a *symmetric quantity*: the second difference of $f$ over a small square.

Take a function of two variables — the general case reduces to this by freezing all other coordinates — and a small square in the plane with corner $(x_1, x_2)$ and side length $h$. Form the alternating corner sum
$$F(h) = f(x_1+h,\, x_2+h) - f(x_1+h,\, x_2) - f(x_1,\, x_2+h) + f(x_1,\, x_2).$$
This is the discrete "mixed second difference" — it differences $f$ once in each direction. The crucial observation is that **$F(h)$ is symmetric**: swapping the roles of the two coordinates leaves the expression literally unchanged (the middle two terms trade places). So whatever $F(h)$ tells us about the second derivative, it must tell us something symmetric.

Now read $F(h)$ in two ways, by grouping the four corners into pairs of opposite edges.

*First reading — vertical edges first.* Group the corners into the two vertical edges of the square. $F(h)$ is the difference between (the change in $f$ along the right edge) and (the change in $f$ along the left edge) — that is, a difference of differences in $x_2$. Applying the one-variable mean value theorem once in $x_2$ and once in $x_1$ produces $F(h) = \partial_1\partial_2 f$ evaluated at some interior point of the square, times $h^2$.

*Second reading — horizontal edges first.* Group instead into the two horizontal edges. By the symmetric argument, $F(h) = \partial_2\partial_1 f$ evaluated at some (possibly different) interior point, times $h^2$.

Equate the two readings and cancel $h^2$:
$$\partial_1\partial_2 f(\text{point near corner}) = \partial_2\partial_1 f(\text{another point near corner}).$$
Both points lie inside the square of side $h$, so as $h \to 0$ both are squeezed onto the corner $(x_1, x_2)$. If the second partials are **continuous**, both sides converge to their values at the corner, and the equality survives the limit: $\partial_1\partial_2 f(x_1,x_2) = \partial_2\partial_1 f(x_1,x_2)$.

One should expect this because $F(h)$ *is* the second derivative in disguise — dividing by $h^2$ gives, in the limit, the mixed second derivative — and $F(h)$ being a symmetric expression means the mixed second derivative cannot care about order. The only thing that could spoil the argument is the limit: the two evaluation points are *not* the corner, they are merely near it, and forcing their values to the corner value is exactly what continuity buys. Drop continuity and the two readings still hold for each fixed $h$, but their limits as $h \to 0$ need not coincide — which is precisely how the counterexample escapes.

---

# What Makes This Hard

The non-obvious step is introducing the **symmetric second difference** $F(h)$ in the first place — the proof does not differentiate $f$ directly, it differences it over a square and then reads that one symmetric quantity two ways. People stuck on the theorem are usually trying to manipulate $\partial_i\partial_j f$ and $\partial_j\partial_i f$ directly, with no symmetric object to equate them through. The genuine subtlety is that the mean value theorem is applied *twice* and the two intermediate points it produces are *interior to the square, not the corner* — the conclusion $\partial_1\partial_2 f = \partial_2\partial_1 f$ at those points is exact, but transferring it to the corner needs the $h\to0$ limit, and that limit is legal only because the second partials are *continuous*. The most common error is to omit the continuity hypothesis or to forget that it is consumed precisely in this final limit; without it the theorem is false.

---

# Rederivation Scaffold

**High-level strategy:**
Reduce to two variables. Form the symmetric corner-difference $F(h)$ over a small square. Evaluate it two ways — by applying the one-variable mean value theorem first in one coordinate, then the other, and vice versa — obtaining $F(h) = \partial_1\partial_2 f(\cdot)h^2 = \partial_2\partial_1 f(\cdot)h^2$. Cancel $h^2$ and let $h\to0$, using continuity of the second partials.

**Subgoal decomposition:**

1. **Reduce to $n = 2$.** It suffices to prove $\partial_1\partial_2 f = \partial_2\partial_1 f$ for a function of two variables.
   - *Hint:* For general $n$ and indices $i \neq j$, freeze all variables but $x_i, x_j$; the rest are spectators.
   - *Why needed:* The square argument is two-dimensional.

2. **Form the symmetric difference.** Define $F(h) = f(x_1+h,x_2+h) - f(x_1+h,x_2) - f(x_1,x_2+h) + f(x_1,x_2)$.
   - *Hint:* Note $F(h)$ is invariant under swapping the two coordinates.
   - *Why needed:* It is the one symmetric object both mixed partials are read from.

3. **First reading.** Show $F(h) = \partial_2\partial_1 f(\xi)\,h^2$ for some $\xi$ inside the square.
   - *Hint:* Write $F(h) = \varphi(1) - \varphi(0)$ with $\varphi(t) = f(x_1+th, x_2+h) - f(x_1+th, x_2)$; apply the mean value theorem in $t$, then again in $x_2$.
   - *Why needed:* It expresses $F(h)$ through one order of differentiation.

4. **Second reading.** Show $F(h) = \partial_1\partial_2 f(\eta)\,h^2$ for some $\eta$ inside the square.
   - *Hint:* Same argument with the roles of the two coordinates exchanged — legal because $F(h)$ is symmetric.
   - *Why needed:* It expresses $F(h)$ through the other order.

5. **Equate and take the limit.** Cancel $h^2$ to get $\partial_2\partial_1 f(\xi) = \partial_1\partial_2 f(\eta)$; let $h\to0$ so $\xi,\eta\to(x_1,x_2)$; continuity gives $\partial_2\partial_1 f = \partial_1\partial_2 f$ at the corner.
   - *Hint:* Both $\xi$ and $\eta$ lie in the square of side $h$, hence within $h\sqrt2$ of the corner.
   - *Why needed:* It is the conclusion; continuity of the second partials is consumed here.

---

# Lemma Decomposition

> [!note]- Lemma 1: First evaluation of the symmetric difference
> **Statement:** For $f \in C^2$ and small $h > 0$, $F(h) = \partial_2\partial_1 f(\xi)\,h^2$ for some point $\xi$ in the open square $(x_1, x_1+h)\times(x_2, x_2+h)$.
>
> **Hint:** Set $\varphi(t) = f(x_1+th, x_2+h) - f(x_1+th, x_2)$; then $F(h) = \varphi(1)-\varphi(0)$. Apply the one-variable mean value theorem to $\varphi$, then once more.
>
> **Why needed:** It expresses $F(h)$ through the partial taken in the order "first $x_1$, then $x_2$".
>
> > [!note]- Full proof
> > Define $\varphi : [0,1]\to\mathbb{R}$ by $\varphi(t) = f(x_1+th, x_2+h) - f(x_1+th, x_2)$. Then $\varphi(1) = f(x_1+h,x_2+h) - f(x_1+h,x_2)$ and $\varphi(0) = f(x_1,x_2+h) - f(x_1,x_2)$, so $F(h) = \varphi(1) - \varphi(0)$. Since $f$ has continuous first partials, $\varphi$ is differentiable with $\varphi'(t) = h\big[\partial_1 f(x_1+th, x_2+h) - \partial_1 f(x_1+th, x_2)\big]$. By the one-variable mean value theorem there is $t_1\in(0,1)$ with $F(h) = \varphi(1)-\varphi(0) = \varphi'(t_1)$, i.e.
> > $$F(h) = h\big[\partial_1 f(x_1+t_1 h, x_2+h) - \partial_1 f(x_1+t_1 h, x_2)\big].$$
> > Now apply the one-variable mean value theorem to the function $s \mapsto \partial_1 f(x_1+t_1 h, x_2+sh)$ (differentiable in $s$ because $f$ has continuous second partials, with derivative $h\,\partial_2\partial_1 f$): there is $s_1\in(0,1)$ with $\partial_1 f(x_1+t_1h, x_2+h) - \partial_1 f(x_1+t_1h, x_2) = h\,\partial_2\partial_1 f(x_1+t_1h, x_2+s_1 h)$. Hence $F(h) = h^2\,\partial_2\partial_1 f(\xi)$ with $\xi = (x_1+t_1h, x_2+s_1h)$, a point inside the square.

> [!note]- Lemma 2: Second evaluation of the symmetric difference
> **Statement:** For $f \in C^2$ and small $h > 0$, $F(h) = \partial_1\partial_2 f(\eta)\,h^2$ for some point $\eta$ in the open square $(x_1, x_1+h)\times(x_2, x_2+h)$.
>
> **Hint:** Repeat Lemma 1 with the two coordinates exchanged — $F(h)$ is symmetric, so the same expression is being differenced.
>
> **Why needed:** It expresses the *same* $F(h)$ through the opposite order "first $x_2$, then $x_1$".
>
> > [!note]- Full proof
> > $F(h)$ is symmetric under swapping the two coordinate roles: $f(x_1+h,x_2+h) - f(x_1+h,x_2) - f(x_1,x_2+h) + f(x_1,x_2)$ is unchanged if one writes it as $f(x_1+h,x_2+h) - f(x_1,x_2+h) - f(x_1+h,x_2) + f(x_1,x_2)$. Apply the argument of Lemma 1 verbatim with the coordinates exchanged: set $\psi(t) = f(x_1+h, x_2+th) - f(x_1, x_2+th)$, so $F(h) = \psi(1)-\psi(0)$; the mean value theorem in $t$ and then in $x_1$ yields $F(h) = h^2\,\partial_1\partial_2 f(\eta)$ for some $\eta$ inside the square.

---

# Formal Proof

> [!note]- Complete formal proof
> **Reduction to two variables.** For general $n$ and fixed indices $i \neq j$, hold all variables except $x_i, x_j$ constant; the statement $\partial_i\partial_j f = \partial_j\partial_i f$ becomes a statement about the two-variable function $(x_i, x_j) \mapsto f(\dots)$. (If $i = j$ there is nothing to prove.) So assume $n = 2$ and prove $\partial_1\partial_2 f = \partial_2\partial_1 f$.
>
> Fix $x = (x_1, x_2) \in U$. Since $U$ is open, for all sufficiently small $h > 0$ the closed square with corners $(x_1, x_2)$, $(x_1+h, x_2)$, $(x_1, x_2+h)$, $(x_1+h, x_2+h)$ lies in $U$. Define the symmetric corner-difference
> $$F(h) = f(x_1+h, x_2+h) - f(x_1+h, x_2) - f(x_1, x_2+h) + f(x_1, x_2).$$
>
> By Lemma 1, there is a point $\xi(h)$ in the open square with
> $$F(h) = \partial_2\partial_1 f\big(\xi(h)\big)\,h^2.$$
> By Lemma 2, there is a point $\eta(h)$ in the open square with
> $$F(h) = \partial_1\partial_2 f\big(\eta(h)\big)\,h^2.$$
> Equating the two expressions and dividing by $h^2 > 0$,
> $$\partial_2\partial_1 f\big(\xi(h)\big) = \partial_1\partial_2 f\big(\eta(h)\big).$$
> Both $\xi(h)$ and $\eta(h)$ lie inside the square of side $h$ with corner $x$, so $|\xi(h) - x| \le h\sqrt2$ and $|\eta(h) - x| \le h\sqrt2$; hence $\xi(h) \to x$ and $\eta(h) \to x$ as $h \to 0$.
>
> Since $f \in C^2(U)$, the second partials $\partial_2\partial_1 f$ and $\partial_1\partial_2 f$ are **continuous** on $U$. Letting $h \to 0$ in the displayed equality and using continuity,
> $$\partial_2\partial_1 f(x) = \lim_{h\to0}\partial_2\partial_1 f(\xi(h)) = \lim_{h\to0}\partial_1\partial_2 f(\eta(h)) = \partial_1\partial_2 f(x).$$
> Since $x$ was arbitrary, $\partial_1\partial_2 f = \partial_2\partial_1 f$ on $U$.
>
> **Higher order.** For $f \in C^k$ and indices $i_1, \dots, i_k$, any permutation is a composite of adjacent transpositions. An adjacent transposition swaps two consecutive differentiations $\partial_{i_\ell}\partial_{i_{\ell+1}}$, which is the $C^2$ case just proved applied to the function $\partial_{i_{\ell+2}}\cdots\partial_{i_k} f$ (which is $C^2$ since $f \in C^k$). Composing, every permutation of the indices leaves the iterated partial unchanged, so $\partial^\alpha f$ is well-defined. $\blacksquare$
>
> *(Remark: the only use of continuity of the second partials is the final limit. For each fixed $h$ the two evaluations of $F(h)$ are exact; it is the passage to $h\to0$ that requires continuity, and exactly here the counterexample of [[Ex - A function with unequal mixed partials]] escapes.)*

---

# Cross-Field Exercise Suggestions

**Symmetry of the Hessian and the second-derivative test.** Schwarz's theorem makes the Hessian $D^2 f$ symmetric, so by the spectral theorem it has real eigenvalues and an orthonormal eigenbasis; the classification of a critical point as a minimum, maximum, or saddle is read off the signs of those eigenvalues. The application is nonobvious because the *symmetry* of the Hessian — a fact about commuting partials — is the hidden bridge from calculus to the spectral theorem.

**Mixed partials in thermodynamics — the Maxwell relations.** Thermodynamic potentials are $C^2$ functions of state variables, and the equality of their mixed second partials *is* the set of Maxwell relations (e.g. $\partial S/\partial V|_T = \partial P/\partial T|_V$). The application is out-of-distribution because a physical identity between measurable quantities turns out to be nothing but Schwarz's theorem applied to a free energy.

**Closedness of exact differential forms.** A $1$-form $df$ obtained from a $C^2$ function is *closed* — the mixed-partial condition $\partial_i(\partial_j f) = \partial_j(\partial_i f)$ is exactly the statement $d(df) = 0$. The application previews **Multivariate Analysis IV**: Schwarz's theorem is the down-to-earth content of the identity $d^2 = 0$ for the exterior derivative.

**Curvature and the Riemann tensor.** In differential geometry the failure of *covariant* derivatives to commute is the curvature tensor; Schwarz's theorem is the flat-space baseline ($\partial_i$ commute) against which curvature is measured. The application is nonobvious in that the entire notion of curvature is "the amount by which the analogue of Schwarz fails".

---

# Bridges

- **[[Def - Higher-Order Derivatives and Ck Maps|Multi-index notation]]** — this theorem is what makes $\partial^\alpha f$ well-defined. Without order-independence, a higher derivative would carry an ordered string of indices and the entire multi-index calculus would collapse.

- **[[Thm - Taylor's Theorem in Several Variables|Taylor's Theorem]]** — a direct consumer. The compact multi-index form of the Taylor expansion, with coefficients $\partial^\alpha f/\alpha!$, depends on the order-independence of partials; the multinomial coefficient $k!/\alpha!$ counts the orderings that Schwarz collapses into one.

- **The spectral theorem for symmetric matrices** — Schwarz makes the Hessian symmetric; the spectral theorem then gives it real eigenvalues and an orthonormal eigenbasis, the foundation of the second-derivative test in **Multivariate Analysis II**.

- **The one-variable mean value theorem** — the engine of the proof, applied four times (twice per reading of the corner-difference).

- **The exterior derivative and $d^2 = 0$** — in **Multivariate Analysis IV**, the identity $d^2 = 0$ for differential forms is, unpacked in coordinates, exactly the equality of mixed partials. Schwarz's theorem is the analytic seed of the entire de Rham complex.

---

# Unlocked by This

> [!tip] The Symmetry of the Hessian and Optimality Tests *(from Multivariate Analysis II)*
> Because mixed partials commute, the Hessian $D^2 f$ is a symmetric matrix, hence diagonalisable with real eigenvalues. The **second-order optimality conditions** — a critical point is a local minimum when the Hessian is positive definite — are read directly off this spectrum.

> [!tip] Closed Forms and the de Rham Complex *(from Multivariate Analysis IV)*
> The equality $\partial_i\partial_j f = \partial_j\partial_i f$ is the coordinate content of $d(df) = 0$. The general identity $d^2 = 0$ for the **exterior derivative** is Schwarz's theorem promoted to differential forms, and it is what makes de Rham cohomology possible.
