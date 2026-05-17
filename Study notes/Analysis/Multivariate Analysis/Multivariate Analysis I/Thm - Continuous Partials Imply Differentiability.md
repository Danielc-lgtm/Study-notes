---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f : U \to \mathbb{R}^m$; $x_\circ \in U$; $h = (h_1, \dots, h_n) \in \mathbb{R}^n$. The $j$-th partial derivative is $\partial_j f$ (see [[Def - Partial Derivatives and the Jacobian Matrix]]); $e_1, \dots, e_n$ is the standard basis. We say $f \in C^1(U)$ when all partials $\partial_1 f, \dots, \partial_n f$ exist and are continuous on $U$. The total derivative is $Df_{x_\circ}$ (see [[Def - The Total Derivative and Differentiability]]). The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Statement

> **Continuous partials imply differentiability.** Let $U \subseteq \mathbb{R}^n$ be open and $f : U \to \mathbb{R}^m$. If every partial derivative $\partial_j f$ exists on all of $U$ and is continuous on $U$ — that is, $f \in C^1(U)$ — then $f$ is differentiable at every point of $U$, and its derivative is the linear map with matrix $Jf(x_\circ) = (\partial_j f_i(x_\circ))$.

---

# Motivation

The definition of differentiability — the existence of a linear map approximating $f$ to $o(|h|)$ — is conceptually right but practically forbidding. To verify it directly you must produce the linear map and then check a limit over *all* directions of approach. Nobody wants to do that for every function. We need a *checkable* sufficient condition, and this theorem supplies the one everyone actually uses.

The condition is: compute the partial derivatives and confirm they are continuous. Partial derivatives are computed by the rules of one-variable calculus — they are mechanical. Checking continuity of an explicit expression is routine. So the theorem converts the hard question "is $f$ differentiable?" into the easy question "are the partials continuous?", and in practice that is how differentiability is *always* established for functions given by formulas. The function $(\sin x)(\sin y)$ is differentiable because its partials $\cos x \sin y$ and $\sin x \cos y$ are visibly continuous — no limit is computed.

The theorem also draws the precise line in the regularity hierarchy. There are three conditions: partials *exist*; $f$ is *differentiable*; $f$ is *continuously differentiable* ($C^1$). The implications run $C^1 \Rightarrow \text{differentiable} \Rightarrow \text{partials exist}$, and **both arrows are strict** — neither reverses. Mere existence of partials does not give differentiability (the function $xy/(x^2+y^2)$). Differentiability does not give $C^1$ (a function can be differentiable with a discontinuous partial). This theorem is the *upper* implication, and the word "continuous" in its hypothesis is doing all the work: it is exactly the strengthening of "partials exist" that buys differentiability. Drop continuity and the theorem is false.

Why should continuity of the partials be the right amount of extra strength? The proof is the explanation. Differentiability fails for $xy/(x^2+y^2)$ because the partials, while existing, are wildly discontinuous at the origin — they take different values along different approaches. The proof below telescopes $f$'s increment into $n$ one-variable increments and controls each with the mean value theorem; the error terms it produces are exactly *differences of partial derivatives at nearby points*, and continuity of the partials is precisely what forces those differences to zero. Continuity of the partials is the hypothesis the proof needs and nothing more.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f \in C^1$" — all partials exist and are continuous.

The first disguised source is **$f$ is given by an explicit formula built from elementary functions**. The property $B$ is "$f$ is a finite composition of polynomials, exponentials, trigonometric functions, etc.". The bridge is that the partials are then computed by the Analysis I rules and come out as expressions of the same elementary type, which are continuous on their natural domain. The implication is nonobvious only in that it is so automatic one forgets it is an implication. *Example problem:* show any polynomial map $\mathbb{R}^n \to \mathbb{R}^m$ is differentiable everywhere.

The second disguised source is **$f$ is a sum, product, or composite of $C^1$ functions**. The property $B$ is "$f$ is assembled from $C^1$ pieces". The bridge is that $C^1$ is closed under these operations — the product rule and the [[Thm - The Chain Rule|chain rule]] express the partials of the combination through the (continuous) partials of the pieces. *Example problem:* a function defined by an integral $g(x) = \int_a^b K(x, t)\,dt$ with $K$ jointly $C^1$ is itself $C^1$ in $x$.

**Targets (Output Amplification)**

The conclusion is "$f$ is differentiable on $U$, with $Df = $ the Jacobian".

Combine the conclusion with **[[Thm - Differentiability Implies Continuity|differentiability implies continuity]]**. The further result $E$: a $C^1$ function is continuous — and one gets the *value* of the derivative as a bonus. This is the standard route to continuity of explicitly-given functions: differentiate, check the partials are continuous, conclude continuity. The combination is useful because it is far cheaper than an $\varepsilon$–$\delta$ estimate.

Combine the conclusion with **the chain rule and the mean value inequality**. Once $f$ is known differentiable, [[Thm - The Chain Rule|the chain rule]] and [[Thm - The Mean Value Inequality|the mean value inequality]] become available — both take "differentiable" or "$C^1$" as hypothesis. The further result $E$: $C^1$ on a convex set with bounded Jacobian gives Lipschitz continuity. This theorem is the gatekeeper: it certifies the hypothesis that the rest of the topic's machinery requires.

Combine the conclusion with **the inverse function theorem** (downstream). A $C^1$ map with invertible Jacobian at a point is, by the inverse function theorem of **Multivariate Analysis II**, a local diffeomorphism. This theorem supplies the "$C^1$" half of that hypothesis. The combination is the foundation of the local theory of maps.

---

# Why Is It True

The guiding idea is the most reliable move in the whole subject: **a multivariate increment can be walked off one coordinate at a time.**

Suppose, for simplicity, $f$ is scalar and we want to understand $f(x_\circ + h) - f(x_\circ)$. The two points $x_\circ$ and $x_\circ + h$ differ in all $n$ coordinates at once, which is hard to handle. So do not go directly. Walk from $x_\circ$ to $x_\circ + h$ along a *staircase*: first change coordinate $1$ only, then coordinate $2$ only, and so on, $n$ steps, each step moving along a single coordinate axis. The total change $f(x_\circ + h) - f(x_\circ)$ is the sum of the $n$ changes along the steps — a telescoping sum.

Now each step is a one-variable problem: along the $j$-th step only $x_j$ varies. The change in $f$ over that step is governed by the $j$-th partial derivative, and the one-variable mean value theorem says the change equals $\partial_j f$ evaluated at some intermediate point on the step, times the coordinate increment $h_j$. So
$$f(x_\circ + h) - f(x_\circ) = \sum_{j=1}^n \partial_j f(\xi_j)\,h_j,$$
where $\xi_j$ is a point on the $j$-th step.

Compare this with what differentiability would demand: $f(x_\circ + h) - f(x_\circ) = \sum_j \partial_j f(x_\circ)\,h_j + R(h)$ with $R(h) = o(|h|)$. Subtracting, the remainder is
$$R(h) = \sum_{j=1}^n \big(\partial_j f(\xi_j) - \partial_j f(x_\circ)\big)\,h_j.$$
This is the heart of the matter. The remainder is a sum of terms, each a *difference of the partial derivative $\partial_j f$ at two points* — the staircase point $\xi_j$ and the base point $x_\circ$ — multiplied by $h_j$. As $h \to 0$, every staircase point $\xi_j$ is squeezed towards $x_\circ$ (it lies within $|h|$ of it). If the partials are **continuous**, the difference $\partial_j f(\xi_j) - \partial_j f(x_\circ)$ therefore goes to zero. And $|h_j| \le |h|$, so each term is (something going to zero) times (something $\le |h|$), which is $o(|h|)$. The remainder dies at the right rate, and $f$ is differentiable.

Now the punchline about *why continuity is essential*. The whole argument is sound regardless — the staircase decomposition and the mean value theorem only need the partials to *exist*. What we cannot do without continuity is the final step: forcing $\partial_j f(\xi_j) - \partial_j f(x_\circ) \to 0$. If the partials are discontinuous, the value of $\partial_j f$ at the staircase point $\xi_j$ need not approach its value at $x_\circ$ even as $\xi_j \to x_\circ$, the remainder need not be $o(|h|)$, and differentiability genuinely fails. Continuity of the partials is not a convenience of the proof; it is the exact hypothesis that closes the last gap.

---

# What Makes This Hard

The non-obvious step is the **staircase decomposition**: replacing the single all-coordinates-at-once increment $f(x_\circ + h) - f(x_\circ)$ by a telescoping sum of $n$ single-coordinate increments, so that the one-variable mean value theorem can be applied to each. Most people get stuck trying to handle all coordinates simultaneously. The most common error is to apply the mean value theorem and then *forget that the intermediate points $\xi_j$ are not $x_\circ$* — the remainder is a sum of differences $\partial_j f(\xi_j) - \partial_j f(x_\circ)$, and it is only the *continuity* of the partials that drives these differences to zero; omitting this is omitting the entire reason the hypothesis says "continuous".

---

# Rederivation Scaffold

**High-level strategy:**
Reduce to a scalar $f$ by componentwise differentiability. Walk from $x_\circ$ to $x_\circ + h$ along a staircase of $n$ single-coordinate steps, apply the one-variable mean value theorem to each step, then show the resulting remainder is $o(|h|)$ using continuity of the partials.

**Subgoal decomposition:**

1. **Reduce to $m = 1$.** It suffices to treat a scalar function.
   - *Hint:* $f$ is differentiable iff each component $f_i$ is; partials and Jacobian split rowwise.
   - *Why needed:* The mean value theorem is a statement about scalar functions.

2. **Set up the staircase.** Write $f(x_\circ + h) - f(x_\circ)$ as a telescoping sum over points $z_0 = x_\circ$, $z_j = x_\circ + (h_1, \dots, h_j, 0, \dots, 0)$, $z_n = x_\circ + h$.
   - *Hint:* $f(x_\circ + h) - f(x_\circ) = \sum_{j=1}^n \big(f(z_j) - f(z_{j-1})\big)$ — insert and cancel.
   - *Why needed:* It turns one $n$-variable increment into $n$ one-variable increments.

3. **Mean value theorem on each step.** Show $f(z_j) - f(z_{j-1}) = \partial_j f(\xi_j)\,h_j$ for some point $\xi_j$ on the segment $[z_{j-1}, z_j]$.
   - *Hint:* Along this segment only the $j$-th coordinate moves; apply the one-variable mean value theorem to that single-variable function.
   - *Why needed:* It expresses each step's change through a partial derivative.

4. **Identify and bound the remainder.** With candidate $L(h) = \sum_j \partial_j f(x_\circ)\,h_j$, show $R(h) = f(x_\circ + h) - f(x_\circ) - L(h) = \sum_j \big(\partial_j f(\xi_j) - \partial_j f(x_\circ)\big) h_j$ is $o(|h|)$.
   - *Hint:* As $h \to 0$, $\xi_j \to x_\circ$; continuity of $\partial_j f$ kills the differences; $|h_j| \le |h|$.
   - *Why needed:* It verifies the definition of differentiability with $L$ the Jacobian.

---

# Lemma Decomposition

> [!note]- Lemma 1: Staircase decomposition of an increment
> **Statement:** For $z_0 = x_\circ$ and $z_j = x_\circ + (h_1, \dots, h_j, 0, \dots, 0)$, so $z_n = x_\circ + h$, one has $f(x_\circ + h) - f(x_\circ) = \sum_{j=1}^n \big(f(z_j) - f(z_{j-1})\big)$.
>
> **Hint:** This is a telescoping sum — write it out and cancel.
>
> **Why needed:** It converts the all-coordinates increment into a sum of single-coordinate increments, each amenable to the one-variable mean value theorem.
>
> > [!note]- Full proof
> > The sum $\sum_{j=1}^n \big(f(z_j) - f(z_{j-1})\big)$ telescopes: every interior term $f(z_j)$ for $1 \le j \le n-1$ appears once with a plus sign and once with a minus sign, leaving $f(z_n) - f(z_0) = f(x_\circ + h) - f(x_\circ)$. The points $z_j$ form a staircase: $z_{j-1}$ and $z_j$ differ only in the $j$-th coordinate, by $h_j$. For these points to lie in $U$ one needs $h$ small enough; since $U$ is open this holds for $|h|$ below some threshold, and the convexity of a small ball around $x_\circ$ guarantees the whole staircase stays inside $U$.

> [!note]- Lemma 2: One-variable mean value theorem on a single step
> **Statement:** For each $j$, there is a point $\xi_j$ on the segment from $z_{j-1}$ to $z_j$ with $f(z_j) - f(z_{j-1}) = \partial_j f(\xi_j)\,h_j$.
>
> **Hint:** Along $[z_{j-1}, z_j]$ only $x_j$ varies; define a one-variable function and apply the one-variable mean value theorem.
>
> **Why needed:** It expresses each staircase step through the $j$-th partial derivative — this is where the hypothesis "$\partial_j f$ exists" enters.
>
> > [!note]- Full proof
> > Fix $j$ and define $\varphi : [0, h_j] \to \mathbb{R}$ (or $[h_j, 0]$ if $h_j < 0$) by $\varphi(t) = f(z_{j-1} + t e_j)$ — the function $f$ along the $j$-th step, a function of one real variable. By hypothesis $\partial_j f$ exists on $U$, so $\varphi$ is differentiable with $\varphi'(t) = \partial_j f(z_{j-1} + t e_j)$. The one-variable mean value theorem gives $t^* $ strictly between $0$ and $h_j$ with $\varphi(h_j) - \varphi(0) = \varphi'(t^*)\,h_j$. Writing $\xi_j = z_{j-1} + t^* e_j$, a point on the segment $[z_{j-1}, z_j]$, this reads $f(z_j) - f(z_{j-1}) = \partial_j f(\xi_j)\,h_j$.

> [!note]- Lemma 3: The remainder is $o(|h|)$
> **Statement:** With $L(h) = \sum_j \partial_j f(x_\circ) h_j$, the remainder $R(h) = \sum_{j=1}^n \big(\partial_j f(\xi_j) - \partial_j f(x_\circ)\big) h_j$ satisfies $|R(h)|/|h| \to 0$ as $h \to 0$.
>
> **Hint:** Bound $|h_j| \le |h|$; as $h \to 0$ each $\xi_j \to x_\circ$; use continuity of $\partial_j f$.
>
> **Why needed:** It verifies the $o(|h|)$ condition in the definition of differentiability — this is the step that consumes the *continuity* hypothesis.
>
> > [!note]- Full proof
> > Combining Lemmas 1 and 2, $f(x_\circ + h) - f(x_\circ) = \sum_j \partial_j f(\xi_j) h_j$, so $R(h) = \sum_j \big(\partial_j f(\xi_j) - \partial_j f(x_\circ)\big) h_j$. By the triangle inequality and $|h_j| \le |h|$,
> > $$\frac{|R(h)|}{|h|} \le \sum_{j=1}^n \big|\partial_j f(\xi_j) - \partial_j f(x_\circ)\big| \cdot \frac{|h_j|}{|h|} \le \sum_{j=1}^n \big|\partial_j f(\xi_j) - \partial_j f(x_\circ)\big|.$$
> > Each $\xi_j$ lies on the staircase, hence within distance $|h|$ of $x_\circ$, so $\xi_j \to x_\circ$ as $h \to 0$. Since each $\partial_j f$ is **continuous** at $x_\circ$, $\partial_j f(\xi_j) \to \partial_j f(x_\circ)$, so every term of the bounding sum tends to $0$. The sum has $n$ terms, hence $|R(h)|/|h| \to 0$. (This is the unique place continuity is used.)

---

# Formal Proof

> [!note]- Complete formal proof
> By the componentwise characterisation of differentiability ([[Def - The Total Derivative and Differentiability]]), $f : U \to \mathbb{R}^m$ is differentiable at $x_\circ$ if and only if each component $f_i : U \to \mathbb{R}$ is, and the partials and Jacobian split rowwise. So we may assume $m = 1$ and $f : U \to \mathbb{R}$ scalar.
>
> Fix $x_\circ \in U$. Since $U$ is open, choose $\delta > 0$ with the closed ball $\overline{B}(x_\circ, \delta) \subseteq U$; for $|h| < \delta$ the entire staircase below lies in $U$ by convexity of the ball.
>
> **Staircase.** Set $z_0 = x_\circ$ and $z_j = x_\circ + (h_1, \dots, h_j, 0, \dots, 0)$, so $z_n = x_\circ + h$. By telescoping (Lemma 1),
> $$f(x_\circ + h) - f(x_\circ) = \sum_{j=1}^n \big(f(z_j) - f(z_{j-1})\big).$$
>
> **Mean value theorem.** For each $j$, the function $t \mapsto f(z_{j-1} + t e_j)$ is differentiable on the relevant interval with derivative $\partial_j f(z_{j-1} + t e_j)$ (the partial exists on $U$ by hypothesis). By the one-variable mean value theorem (Lemma 2) there is a point $\xi_j$ on the segment $[z_{j-1}, z_j]$ with
> $$f(z_j) - f(z_{j-1}) = \partial_j f(\xi_j)\,h_j.$$
> Hence
> $$f(x_\circ + h) - f(x_\circ) = \sum_{j=1}^n \partial_j f(\xi_j)\,h_j.$$
>
> **Candidate derivative and remainder.** Let $L : \mathbb{R}^n \to \mathbb{R}$ be the linear map $L(h) = \sum_{j=1}^n \partial_j f(x_\circ)\,h_j$ — its matrix is the Jacobian row $Jf(x_\circ)$. Then
> $$R(h) := f(x_\circ + h) - f(x_\circ) - L(h) = \sum_{j=1}^n \big(\partial_j f(\xi_j) - \partial_j f(x_\circ)\big)\,h_j.$$
>
> **The remainder is $o(|h|)$.** Using $|h_j| \le |h|$ and the triangle inequality (Lemma 3),
> $$\frac{|R(h)|}{|h|} \le \sum_{j=1}^n \big|\partial_j f(\xi_j) - \partial_j f(x_\circ)\big|.$$
> As $h \to 0$, each $\xi_j$ lies within $|h|$ of $x_\circ$, hence $\xi_j \to x_\circ$. Each partial $\partial_j f$ is continuous on $U$, so $\partial_j f(\xi_j) \to \partial_j f(x_\circ)$, and the right-hand side — a finite sum of $n$ terms each tending to $0$ — tends to $0$. Therefore $|R(h)|/|h| \to 0$, i.e. $R(h) = o(|h|)$.
>
> By the definition of differentiability, $f$ is differentiable at $x_\circ$ with $Df_{x_\circ} = L$, the linear map of matrix $Jf(x_\circ)$. Since $x_\circ \in U$ was arbitrary, $f$ is differentiable on $U$. $\blacksquare$
>
> *(Remark: the proof uses only the existence of the partials and their continuity at the single point $x_\circ$ — together with their existence on a neighbourhood, so that the staircase is defined. The mean value theorem in Lemma 2 can be replaced by the fundamental theorem of calculus if one prefers an integral remainder; the structure is identical.)*

---

# Cross-Field Exercise Suggestions

**Functions defined by integrals.** A function $g(x) = \int_a^b K(x,t)\,dt$ with $K$ jointly $C^1$ has continuous partials $\partial_{x_j} g = \int_a^b \partial_{x_j} K\,dt$ (differentiation under the integral sign), hence is $C^1$, hence differentiable. The application is nonobvious because differentiability of an integral-defined function looks like it should require a delicate limit interchange, whereas this theorem reduces it to "the partials are continuous".

**Matrix-valued maps.** The map $X \mapsto X^2$ on $M(n,\mathbb{R}) \cong \mathbb{R}^{n^2}$ has partials (with respect to the entries) that are linear in $X$, hence continuous, so the map is differentiable everywhere — recovering $DS(X)Y = XY + YX$ without expanding $(X+Y)^2$. The point is that the $n^2$-variable differentiability is certified by a continuity check on polynomial partials.

**Potential functions in physics.** A force field $F = \nabla V$ derived from a $C^1$ potential $V$ is automatically a continuous (indeed differentiable) vector field. Whenever a physical quantity is given as the gradient of a smooth potential, this theorem silently guarantees the regularity that the subsequent analysis assumes.

---

# Bridges

- **[[Thm - Differentiability Implies Continuity|Differentiability implies continuity]]** — the companion implication. Chained with this theorem: $C^1 \Rightarrow$ differentiable $\Rightarrow$ continuous. Together they place differentiability strictly between "$C^1$" and "partials exist".

- **[[Def - Partial Derivatives and the Jacobian Matrix|Existence of partial derivatives]]** — the hypothesis this theorem strengthens. Existence alone is *not* enough (the function $xy/(x^2+y^2)$); the theorem isolates "continuity of the partials" as the exact extra ingredient.

- **The one-variable mean value theorem** — the engine of the proof, applied $n$ times, once per staircase step. The multivariate result is built entirely from $n$ one-variable applications.

- **[[Thm - The Mean Value Inequality|The mean value inequality]]** — a downstream consumer. It takes "$C^1$" as hypothesis, and this theorem is what certifies that hypothesis from a partial-derivative computation.

- **The fundamental theorem of calculus** — an alternative engine. Replacing the mean value theorem by the FTC on each step gives the same result with an explicit integral remainder $A_j(x,y) = \int_0^1 \partial_j f(\cdots)\,dt$, which is the form most convenient for quantitative estimates.
