---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f : U \to \mathbb{R}^m$; $x_\circ \in U$; $h \in \mathbb{R}^n$ a small increment. The total derivative $Df_{x_\circ} : \mathbb{R}^n \to \mathbb{R}^m$ is the linear map of [[Def - The Total Derivative and Differentiability]]; $\|Df_{x_\circ}\|$ is its operator norm, the smallest constant with $|Df_{x_\circ}(h)| \le \|Df_{x_\circ}\|\,|h|$. We write $R(h) = o(|h|)$ for $|R(h)|/|h| \to 0$. The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Statement

> **Differentiability implies continuity.** Let $U \subseteq \mathbb{R}^n$ be open and $f : U \to \mathbb{R}^m$. If $f$ is differentiable at $x_\circ \in U$, then $f$ is continuous at $x_\circ$.

---

# Motivation

A definition of "differentiable" earns its name only if it is at least as strong as "continuous" — a function with a corner or a jump should not count as smooth. In one variable this is a familiar reassurance: differentiable functions are continuous. The multivariate definition of differentiability ([[Def - The Total Derivative and Differentiability]]) is a genuine condition — the existence of a linear map approximating $f$ to $o(|h|)$ — and the first thing to confirm is that it has not accidentally become *weaker* than continuity. This theorem is that confirmation.

The result also matters in the negative direction, and that is how it is most used. It supplies the cheapest possible test for *non*-differentiability: if a function is discontinuous at a point, it is not differentiable there, full stop, and no computation with the limit definition is needed. Many of the standard pathologies of the subject — functions with all partial derivatives but no total derivative — are exposed precisely this way: they are discontinuous, and discontinuity kills differentiability outright. So the theorem is both a sanity check on the definition and a one-line decision procedure.

There is a subtlety worth flagging at the outset. Differentiability implies continuity. But the *existence of partial derivatives* does **not** imply continuity — a function can have every partial at a point and be discontinuous there. This is exactly the gap between "partials exist" and "differentiable", and this theorem is what makes the gap visible: it is the property that differentiability has and that mere partial-differentiability lacks.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ is differentiable at $x_\circ$". The skill is recognising differentiability when it is not handed to you directly.

The first disguised source is **$f$ has continuous partial derivatives near $x_\circ$**. The property $B$ is "$f \in C^1$ on a neighbourhood of $x_\circ$". The bridge is [[Thm - Continuous Partials Imply Differentiability]]: continuity of the partials upgrades to differentiability, which then feeds this theorem. The implication is nonobvious because continuity of the *partials* is a statement about behaviour along axes, while the conclusion is continuity of $f$ itself in every direction. *Example problem:* a function given by an explicit smooth formula is continuous — verify it via differentiability rather than by an $\varepsilon$–$\delta$ estimate.

The second disguised source is **$f$ is a composite of differentiable maps**. The property $B$ is "$f = g \circ \varphi$ with $\varphi$ differentiable at $x_\circ$ and $g$ differentiable at $\varphi(x_\circ)$". The bridge is [[Thm - The Chain Rule]], which makes $f$ differentiable; this theorem then makes it continuous. The nonobvious part is that continuity of a composite is being deduced not from continuity of the pieces but from their *differentiability*. *Example problem:* show that a function built by composing coordinate changes is continuous wherever the pieces are differentiable.

**Targets (Output Amplification)**

The conclusion is "$f$ is continuous at $x_\circ$".

Combine the conclusion with **the contrapositive**. The most-used form of the theorem is "discontinuous $\Rightarrow$ not differentiable". The further result $E$: a one-line proof of non-differentiability for any function shown to be discontinuous, with no appeal to the limit definition. This is nonobvious only in that it inverts the theorem's direction — but it is where the theorem does its real work, since proving non-differentiability directly from the definition is laborious.

Combine the conclusion with **the extreme value theorem**. If $f$ is differentiable on a compact set (more precisely, differentiable on an open set containing a compact $K$), then $f$ is continuous, hence — being continuous on the compact $K$ — attains its maximum and minimum on $K$. The further result $E$ is the existence of extrema, the entry point to optimisation. The combination is useful because differentiability is often the hypothesis actually available, and this theorem is the bridge from "differentiable" to "continuous" that the extreme value theorem requires as *its* input.

---

# Why Is It True

The intuition is the same one that makes the theorem true in one variable, and it is almost a tautology once the definition of differentiability is unpacked.

To be differentiable at $x_\circ$ is to satisfy $f(x_\circ + h) = f(x_\circ) + Df_{x_\circ}(h) + R(h)$ with $R(h) = o(|h|)$. Look at what happens to the increment $f(x_\circ + h) - f(x_\circ)$ as $h \to 0$. It equals $Df_{x_\circ}(h) + R(h)$, a sum of two terms, and both terms vanish.

The linear term $Df_{x_\circ}(h)$ vanishes because **linear maps on $\mathbb{R}^n$ are continuous**: a linear map sends small vectors to small vectors, quantitatively $|Df_{x_\circ}(h)| \le \|Df_{x_\circ}\|\,|h| \to 0$. (This is a fact about linear maps in finite dimensions — they are automatically bounded, hence continuous.) The remainder term $R(h)$ vanishes because $R(h) = o(|h|)$ means $|R(h)|/|h| \to 0$, and a fortiori $|R(h)| \to 0$: something that is small *even compared to $|h|$* is certainly small in absolute terms.

So $f(x_\circ + h) - f(x_\circ)$ is the sum of two quantities each going to zero, hence goes to zero, which is exactly continuity. One should *expect* this: differentiability says $f$ is *approximated* by something continuous (an affine map) with a *negligible* error, and being close to a continuous function with a vanishing error cannot leave you discontinuous. The whole content is that the definition of differentiability already builds in "the increment is controlled by $|h|$", and any control by $|h|$ that disappears as $h \to 0$ is continuity.

The single place this could fail to be a tautology — and the place that genuinely uses finite dimensionality — is the claim that the linear term is continuous. In infinite dimensions a linear map need not be bounded, and "differentiable" is then *defined* to require a bounded linear map precisely so that this theorem survives. In $\mathbb{R}^n$ every linear map is bounded for free, so the issue does not arise.

---

# What Makes This Hard

The theorem is genuinely easy, and the only real trap is conceptual: confusing it with the false statement "existence of partial derivatives implies continuity". Differentiability — the existence of a *total* derivative — implies continuity; the existence of partials does not, and the standard counterexample $xy/(x^2+y^2)$ has both partials yet is discontinuous at the origin. The second, smaller slip is forgetting *why* the linear term $Df_{x_\circ}(h)$ tends to zero: it is the continuity of linear maps on $\mathbb{R}^n$, equivalently the bound $|Df_{x_\circ}(h)| \le \|Df_{x_\circ}\|\,|h|$, and naming this bound is the one substantive step.

---

# Rederivation Scaffold

**High-level strategy:**
Write the definition of differentiability as an explicit equation for the increment $f(x_\circ + h) - f(x_\circ)$, then send $h \to 0$ and observe that each term on the right side vanishes.

**Subgoal decomposition:**

1. **Write the increment.** Show $f(x_\circ + h) - f(x_\circ) = Df_{x_\circ}(h) + R(h)$ with $R(h) = o(|h|)$.
   - *Hint:* This is just the definition of differentiability, rearranged.
   - *Why needed:* It splits the increment into two analysable pieces.

2. **Kill the linear term.** Show $Df_{x_\circ}(h) \to 0$ as $h \to 0$.
   - *Hint:* $|Df_{x_\circ}(h)| \le \|Df_{x_\circ}\|\,|h|$ — linear maps on $\mathbb{R}^n$ are bounded.
   - *Why needed:* It is one of the two terms; the bound $\|Df_{x_\circ}\| \cdot |h| \to 0$.

3. **Kill the remainder.** Show $R(h) \to 0$ as $h \to 0$.
   - *Hint:* $R(h) = o(|h|)$ gives $|R(h)|/|h| \to 0$, so $|R(h)| = (|R(h)|/|h|)\cdot|h| \to 0 \cdot 0 = 0$.
   - *Why needed:* It is the other term; together with step 2 the increment vanishes.

4. **Conclude continuity.** The increment $f(x_\circ + h) - f(x_\circ) \to 0$, so $f(x_\circ + h) \to f(x_\circ)$.
   - *Hint:* This is the definition of continuity at $x_\circ$.
   - *Why needed:* It is the target.

---

# Lemma Decomposition

> [!note]- Lemma 1: A linear map on $\mathbb{R}^n$ is bounded, hence continuous
> **Statement:** Every linear map $L : \mathbb{R}^n \to \mathbb{R}^m$ has a finite operator norm $\|L\| = \sup_{|h| \le 1} |L(h)| < \infty$, and satisfies $|L(h)| \le \|L\|\,|h|$ for all $h$. In particular $L(h) \to 0$ as $h \to 0$.
>
> **Hint:** Expand $h = \sum_j h_j e_j$ and use the triangle inequality together with $|h_j| \le |h|$.
>
> **Why needed:** It is the only substantive step — it makes the linear term in the increment vanish.
>
> > [!note]- Full proof
> > Write $h = \sum_{j=1}^n h_j e_j$. By linearity $L(h) = \sum_j h_j L(e_j)$, so by the triangle inequality $|L(h)| \le \sum_j |h_j|\,|L(e_j)|$. Each coordinate satisfies $|h_j| \le |h|$ (a coordinate is bounded by the Euclidean norm), so $|L(h)| \le |h| \sum_j |L(e_j)| =: C\,|h|$ with $C = \sum_j |L(e_j)|$ a finite constant. Thus $\|L\| \le C < \infty$, and $|L(h)| \le \|L\|\,|h| \to 0$ as $h \to 0$. (Finiteness of $C$ is where $\mathbb{R}^n$ being finite-dimensional is used: the sum has $n$ terms.)

> [!note]- Lemma 2: An $o(|h|)$ quantity tends to zero
> **Statement:** If $R(h) = o(|h|)$ as $h \to 0$, then $R(h) \to 0$ as $h \to 0$.
>
> **Hint:** Write $|R(h)| = \dfrac{|R(h)|}{|h|}\cdot|h|$ for $h \neq 0$.
>
> **Why needed:** It makes the remainder term in the increment vanish.
>
> > [!note]- Full proof
> > By definition $R(h) = o(|h|)$ means $|R(h)|/|h| \to 0$ as $h \to 0$. For $h \neq 0$, $|R(h)| = \big(|R(h)|/|h|\big)\cdot|h|$, a product of a factor tending to $0$ and a factor tending to $0$, hence $|R(h)| \to 0$. (At $h = 0$ there is nothing to check.) So $R(h) \to 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : U \to \mathbb{R}^m$ be differentiable at $x_\circ \in U$, with total derivative $L = Df_{x_\circ}$. By the definition of differentiability ([[Def - The Total Derivative and Differentiability]]), for $h$ small enough that $x_\circ + h \in U$,
> $$f(x_\circ + h) - f(x_\circ) = L(h) + R(h), \qquad R(h) = o(|h|) \text{ as } h \to 0.$$
> We show the left side tends to $0$ as $h \to 0$.
>
> By Lemma 1, $L$ is a bounded linear map: $|L(h)| \le \|L\|\,|h|$. Since $\|L\| < \infty$ is a fixed constant and $|h| \to 0$, we get $|L(h)| \to 0$, so $L(h) \to 0$.
>
> By Lemma 2, $R(h) = o(|h|)$ implies $R(h) \to 0$.
>
> Therefore
> $$\big|\,f(x_\circ + h) - f(x_\circ)\,\big| = |L(h) + R(h)| \le |L(h)| + |R(h)| \longrightarrow 0 \qquad (h \to 0).$$
> Hence $f(x_\circ + h) \to f(x_\circ)$ as $h \to 0$, which is precisely the statement that $f$ is continuous at $x_\circ$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Discontinuity as an instant non-differentiability certificate.** Given any function defined piecewise — smooth off a set, assigned values on it — the fastest check for differentiability is to test continuity first. If the function jumps, the contrapositive of this theorem ends the matter. This is nonobvious only because one is tempted to reach for the limit definition of the derivative; the theorem says continuity is the cheaper gate.

**Matrix-valued maps.** The inversion map $\Phi(X) = X^{-1}$ on $GL(n,\mathbb{R}) \subseteq M(n,\mathbb{R})$ is differentiable (its derivative at $I$ is $Y \mapsto -Y$), so by this theorem it is continuous — matrix inversion is a continuous operation. The application is nonobvious because continuity of inversion is often proved by hand with Cramer's rule and determinants, whereas differentiability delivers it for free.

**Solutions of differential equations depending on parameters.** When the solution of an ODE is shown to be a differentiable function of its initial data or of a parameter, this theorem immediately gives *continuous* dependence on initial data — a foundational well-posedness statement — without a separate argument.

---

# Bridges

- **[[Thm - Continuous Partials Imply Differentiability|Continuous partials imply differentiability]]** — the natural companion. That theorem provides the most common *source* of differentiability; this theorem extracts continuity from it. Chained, they say: continuous partials $\Rightarrow$ differentiable $\Rightarrow$ continuous.

- **[[Def - Partial Derivatives and the Jacobian Matrix|Existence of partial derivatives]]** — the contrast case. Partials can exist without continuity, so the existence of partials does *not* imply this theorem's conclusion. The theorem is exactly the property that distinguishes genuine differentiability from mere partial-differentiability.

- **The one-variable theorem "differentiable $\Rightarrow$ continuous"** — the special case $n = m = 1$, from which this is the verbatim generalisation: the linear term is continuous, the $o(|h|)$ remainder vanishes, the increment dies.

- **Bounded linear operators in functional analysis** — in infinite dimensions a linear map need not be continuous, so the Fréchet derivative is *defined* to be a *bounded* linear operator precisely so that this theorem continues to hold. The finite-dimensional case hides this because every linear map on $\mathbb{R}^n$ is automatically bounded.
