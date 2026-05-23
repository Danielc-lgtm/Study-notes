---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - The Tangent Space"
  - "Def - Derivation at a Point"
  - "Def - Tangent Vector via Equivalence Classes of Curves"
  - "Def - Coordinate Tangent Vectors"
  - "Def - The Differential of a Smooth Map"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold and $p \in M$. We compare three constructions of the tangent space at $p$:
- $T_{p}M$ = derivations of $C^{\infty}(M)$ at $p$ ([[Def - The Tangent Space]]);
- $V_{p}M$ = equivalence classes of smooth curves through $p$ under "same velocity" ([[Def - Tangent Vector via Equivalence Classes of Curves]]);
- $\mathrm{Chart}_{p}(M)$ = tuples $(v^{1}, \dots, v^{n})$ per chart with the Jacobian transformation law.

The natural map from $V_{p}M$ to $T_{p}M$ sends $[\gamma] \mapsto v_{\gamma}$ where $v_{\gamma}(f) = (f \circ \gamma)'(0)$. The natural map from $\mathrm{Chart}_{p}(M)$ to $T_{p}M$, given a chart $(U, \varphi)$, sends $(v^{1}, \dots, v^{n}) \mapsto v^{i}\,\partial/\partial x^{i}|_{p}$. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Statement

> **Theorem (Equivalence of Tangent Vector Definitions).** Let $M$ be a smooth $n$-manifold and $p \in M$. There are canonical vector-space isomorphisms
> $$V_{p}M \;\xleftarrow{\sim}\; T_{p}M \;\xrightarrow{\sim}\; \mathrm{Chart}_{p}(M),$$
> commuting with the differentials of every smooth map $F : M \to N$.
>
> Concretely:
>
> 1. The map $\Theta : V_{p}M \to T_{p}M$, $[\gamma] \mapsto v_{\gamma}$, where $v_{\gamma}(f) = (f \circ \gamma)'(0)$, is a well-defined bijection. It carries the vector-space structure on $T_{p}M$ uniquely back to $V_{p}M$.
> 2. For any chart $(U, \varphi)$ at $p$, the map $\Psi_{\varphi} : \mathbb{R}^{n} \to T_{p}M$, $(v^{1}, \dots, v^{n}) \mapsto v^{i}\,\partial/\partial x^{i}|_{p}$, is a vector-space isomorphism. Under change of chart from $\varphi$ to $\tilde\varphi$, the components $(v^{i})$ and $(\tilde v^{j})$ are related by the Jacobian: $\tilde v^{j} = (\partial \tilde x^{j}/\partial x^{i})(\varphi(p))\,v^{i}$.
>
> Moreover the maps $\Theta$ and $\Psi_{\varphi}$ are **natural in $F$**: for a smooth map $F : M \to N$, the differentials $dF_{p}$ defined separately in the curve picture ($[\gamma] \mapsto [F \circ \gamma]$), the derivation picture ($v \mapsto (f \mapsto v(f \circ F))$), and the chart picture (Jacobian matrix multiplication) all agree under the isomorphisms.

> **Corollary 1.** $T_{p}M$ has dimension $n$. (Proved separately as [[Thm - Dimension of the Tangent Space]].)
>
> **Corollary 2.** Every tangent vector is the velocity of some smooth curve through $p$.

The technical core is the **derivation-curve bijection** ($\Theta$ above), proved via Taylor's theorem with remainder applied to a derivation at the origin of $\mathbb{R}^{n}$.

---

# Motivation

This theorem is the technical heart of Chapter 3 of Lee and of differential geometry's foundations. Without it, the three pictures of a tangent vector — derivation, curve class, chart tuple — would be three separate concepts, each with its own theory, each appearing in a different style of textbook, with no way to translate between them. *With* it, all three pictures collapse into a single object viewable from three angles, and one can use whichever picture is most convenient for the problem at hand.

The reason the result is non-obvious is that the three definitions look *radically* different. A derivation is a linear-and-Leibniz operator on an infinite-dimensional algebra $C^{\infty}(M)$ — completely algebraic. A curve class is a geometric object — a smooth path through $p$ modulo a velocity equivalence relation. A chart tuple is $n$ numbers transforming by a specific rule — purely calculational. That all three describe the same finite-dimensional vector space is a remarkable structural fact.

The proof of the derivation-curve bijection is the technical heart. Surjectivity is straightforward: a chart gives every derivation a component expression $v = v^{i}\,\partial/\partial x^{i}|_{p}$, and the coordinate curve $\gamma(t) = \varphi^{-1}(\varphi(p) + tv)$ realizes $v$ as a velocity. Injectivity is harder and is where Taylor's theorem enters: two curves with the same velocity-derivation must agree on the coordinate functions $x^{i}$ at first order, hence have the same coordinate-component derivatives, hence be equivalent. The deepest part is showing that *every* linear-and-Leibniz operator at $a \in \mathbb{R}^{n}$ is a directional derivative $D_{v}|_{a}$ for some $v \in \mathbb{R}^{n}$ — this is Lee's Proposition 3.2, and the proof uses Taylor's theorem with integral remainder to write any smooth $f$ as a constant plus a first-order term plus a quadratic-vanishing remainder, then observes that the derivation kills both the constant and the remainder, leaving exactly the directional-derivative value.

---

# Sources and Targets

**Sources (Input Broadening).**

The precondition of the theorem is "a smooth manifold and a point". This is universal — every result in differential geometry has access to it. The skill is in recognizing when one of the *equivalent* presentations is unexpectedly available.

The first source is **a smooth curve through $p$**. Whenever a problem hands you a curve $\gamma : J \to M$ with $\gamma(0) = p$, you get a tangent vector $\gamma'(0) \in T_{p}M$ for free — the velocity. This converts geometric problems (paths on a manifold) into algebraic problems (tangent vectors and linear maps). The bridge $B \to A$ here is: "a curve through $p$ exists" implies "we have at least one specific tangent vector at $p$", and via Proposition 3.23 (Lee), every tangent vector is realized this way. Example: when computing $T_{I}\mathrm{SO}(n)$, the natural curves to try are $\gamma(t) = e^{tA}$ for various matrices $A$; the equivalence theorem certifies that the resulting velocity vectors $A$ are exactly the tangent space.

The second source is **a coordinate chart around $p$**. Whenever a chart is available, the coordinate basis $\partial/\partial x^{i}|_{p}$ is available, and the bridge "components transform by the Jacobian" lets one translate to other charts. The equivalence theorem says these chart-tuples are tangent vectors in the abstract sense too. Example: computing $dF_{p}$ as a Jacobian matrix in coordinates — the equivalence theorem certifies that the matrix is *the* differential, not just one of many possible coordinate representations.

The third source is **a derivation at $p$**. Whenever one constructs an algebraic operator on $C^{\infty}(M)$ satisfying linearity and Leibniz, the equivalence theorem says one has constructed a tangent vector — even though the construction never mentioned curves or charts. Example: the **Lie derivative at $p$** acts on $C^{\infty}(M)$ by $(\mathcal{L}_{X} f)(p) = X_{p}(f)$, where $X_{p}$ is a derivation at $p$; the equivalence theorem says this is just "evaluate the directional derivative".

**Targets (Output Amplification).**

The conclusion is "$V_{p}M \cong T_{p}M \cong \mathrm{Chart}_{p}(M)$, and the isomorphisms are natural in $F$". Combined with various downstream property $D$ it yields striking results.

Target 1: **combined with the differential-via-curve formula (Corollary 3.25), the equivalence theorem becomes a computational tool**. The formula says $dF_{p}(v) = (F \circ \gamma)'(0)$ for any curve $\gamma$ realizing $v$. This is far faster than the Jacobian-expansion approach when $F$ is given by a formula and the right curve is obvious. The combination "equivalence theorem + curve formula" is the workhorse of practical differential geometry. Example: for matrix inversion $F(A) = A^{-1}$ on $\mathrm{GL}(n)$, computing $dF_{I}$ by Jacobian is painful (you have to differentiate the entries of $A^{-1}$ with respect to the entries of $A$ — a fourth-rank tensor calculation), but via the curve $\gamma(t) = I + tH$ it is one line: $(F \circ \gamma)'(0) = -H$.

Target 2: **combined with the existence of a smooth structure on $TM$, the equivalence theorem makes the global differential $dF : TM \to TN$ smooth**. The chart-tuple picture says that in natural coordinates on $TM$, $dF$ is given by $(x, v) \mapsto (\hat{F}(x), D\hat{F}_{x} \cdot v)$, which is manifestly smooth in $(x, v)$. The equivalence theorem certifies this calculation gives *the* differential, not a chart-dependent approximation. So $dF$ is smooth, hence $T : \mathrm{Diff} \to \mathrm{Diff}$ is a functor on actual smooth manifolds.

Target 3: **combined with linearity of the differential, the equivalence theorem implies the chain rule in coordinate form is the Jacobian product**. If $F : M \to N$ and $G : N \to P$ are smooth, then the matrix of $d(G \circ F)_{p}$ is the product of the matrices of $dG_{F(p)}$ and $dF_{p}$. This is just the matrix-product chain rule from multivariate calculus, but now applied chart-by-chart and *certified by the equivalence theorem* to give the manifold differential.

Target 4: **combined with a Lie group structure, the equivalence theorem yields the Lie algebra**. For a Lie group $G$, the tangent space at the identity $T_{e}G$ inherits a Lie bracket from the commutator of left-invariant vector fields. The equivalence theorem says this bracket can be computed either by the curve formula (find one-parameter subgroups $\gamma_{X}, \gamma_{Y}$ realizing $X, Y$ and look at the commutator $\gamma_{X}(s)\gamma_{Y}(t)\gamma_{X}(s)^{-1}\gamma_{Y}(t)^{-1}$) or by the derivation formula (commutator of vector fields as algebraic operators). The two computations give the same answer — a non-trivial cross-check.

---

# Why Is It True

The equivalence is a structural fact about *first-order behaviour* at a point, and the underlying reason is that **first-order behaviour at $p$ has $n$ degrees of freedom on an $n$-manifold, and all three definitions are designed to capture exactly those degrees of freedom**.

Here is the picture. Around $p$, the algebra $C^{\infty}(M)$ filters by order of vanishing: smooth functions vanishing at $p$ form an ideal $\mathfrak{m}_{p}$; functions whose first-order Taylor expansion vanishes at $p$ form the squared ideal $\mathfrak{m}_{p}^{2}$. The quotient $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$ is an $n$-dimensional vector space — the **cotangent space** — recording "first-order behaviour at $p$". A tangent vector at $p$, in any of the three pictures, is a linear functional on $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$.

**The derivation picture**: a derivation $v$ at $p$ annihilates constants (so it factors through $\mathfrak{m}_{p}$) and annihilates products of two functions vanishing at $p$ (so it factors through $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$). So $v$ is a linear functional on $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$, i.e., an element of the dual $(\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2})^{*}$. This is $n$-dimensional.

**The curve picture**: a curve $\gamma$ through $p$ produces, for each $f \in C^{\infty}(M)$ near $p$, a number $(f \circ \gamma)'(0)$. The map $f \mapsto (f \circ \gamma)'(0)$ vanishes on constants and on $\mathfrak{m}_{p}^{2}$ (by the product rule for derivatives), so factors through $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$ and gives an element of $(\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2})^{*}$. The equivalence relation on curves is "same image in this dual" — so curve classes are *literally* elements of $(\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2})^{*}$.

**The chart-tuple picture**: in a chart with coordinates $x^{i}$, the cotangent space $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$ has basis $\{[x^{i} - x^{i}(p)] : 1 \leq i \leq n\}$ (the "first-order" coordinate functions), so its dual has basis $\partial/\partial x^{i}|_{p}$. A chart-tuple is the dual-basis expansion.

**The bolded one-liner mechanism summary: all three definitions are realizations of the same finite-dimensional dual space $(\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2})^{*}$, and the equivalence theorem proves this by exhibiting the natural isomorphisms.**

Concretely, the proof of the derivation-curve bijection runs by Taylor's theorem with integral remainder. On $\mathbb{R}^{n}$ centered at $a$, any smooth $f$ admits the expansion
$$f(x) = f(a) + \sum_{i} (x^{i} - a^{i})\,g_{i}(x), \qquad g_{i} \in C^{\infty},\, g_{i}(a) = \partial f/\partial x^{i}(a).$$
A derivation $v$ at $a$ annihilates the constant $f(a)$ and, by the Leibniz rule applied to each $(x^{i} - a^{i})\,g_{i}$, gives $v(f) = \sum_{i} (g_{i}(a) \cdot v(x^{i} - a^{i})) = \sum_{i} v^{i}\,\partial f/\partial x^{i}(a)$ where $v^{i} = v(x^{i})$. So $v$ is exactly the directional derivative $D_{v}|_{a}$, and the bijection derivation $\leftrightarrow$ vector is established. The manifold case reduces to this via a chart.

The naturality (commutativity with differentials) is a routine check: $dF_{p}$ in each picture is defined by the natural operation — pre-composition for derivations, post-composition for curves, Jacobian multiplication for chart-tuples — and these agree under the isomorphisms.

---

# What Makes This Hard

The hardest step is the **Taylor-expansion argument** showing that every derivation at $a \in \mathbb{R}^{n}$ is a directional derivative. People stuck on the proof typically (a) try to prove this in the manifold case directly, missing that the right approach is to *reduce to Euclidean space via a chart* and then run the Euclidean argument; (b) get the wrong remainder bound in Taylor's theorem — one needs the remainder to lie in $\mathfrak{m}_{p}^{2}$ (a sum of products of two vanishing factors), not just to be quadratic in size, because the Leibniz rule annihilates the former cleanly. The most common error is forgetting that a derivation annihilates constants — without this, the constant term $f(a)$ contributes spuriously and the calculation fails.

A secondary subtlety is **vector-space structure on $V_{p}M$**: how do you add two equivalence classes of curves? The answer is "via the isomorphism to $T_{p}M$" — you cannot meaningfully add curves directly without choosing a chart. This is why the derivation definition is preferred for proofs: in $T_{p}M$ the addition is pointwise on functions, manifestly well-defined; in $V_{p}M$ it has to be defined indirectly. This subtlety is the technical reason the equivalence theorem is needed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Reduce to $\mathbb{R}^{n}$ via a chart. In $\mathbb{R}^{n}$, prove three facts: (a) every derivation annihilates constants and double-vanishing products; (b) every smooth function admits a Taylor expansion $f(x) = f(a) + (x^{i} - a^{i})g_{i}(x)$ with $g_{i}(a) = \partial_{i} f(a)$; (c) combining (a) and (b), a derivation $v$ is determined by its values $v^{i} = v(x^{i})$, with $v = v^{i}\,\partial/\partial x^{i}|_{a}$. This gives the derivation-vector bijection on $\mathbb{R}^{n}$. The manifold case follows by transporting via a chart. The curve-vector bijection then comes from realizing each derivation as the velocity of a coordinate-line curve and checking that the curve-equivalence relation matches.

**Subgoal decomposition:**

1. **Constants are annihilated.** Show $v(c) = 0$ for any constant function $c$.
   - *Hint:* Apply $v$ to $1 = 1 \cdot 1$ using the Leibniz rule.
   - *Why needed:* This is the base case for "derivations are first-order".

2. **Double-vanishing products are annihilated.** If $f(a) = g(a) = 0$, then $v(fg) = 0$.
   - *Hint:* Apply the Leibniz rule directly: $v(fg) = f(a)v(g) + g(a)v(f) = 0 + 0 = 0$.
   - *Why needed:* Combined with subgoal 1, this implies $v$ kills the squared ideal $\mathfrak{m}_{a}^{2}$, so $v$ factors through $\mathfrak{m}_{a}/\mathfrak{m}_{a}^{2}$.

3. **Taylor expansion with remainder in $\mathfrak{m}_{a}^{2}$.** For $f \in C^{\infty}(\mathbb{R}^{n})$ and $a \in \mathbb{R}^{n}$, write $f(x) = f(a) + (x^{i} - a^{i})\,g_{i}(x)$ where $g_{i}(a) = \partial f/\partial x^{i}(a)$.
   - *Hint:* Use $f(x) - f(a) = \int_{0}^{1} (d/dt) f(a + t(x - a))\,dt = \int_{0}^{1} (x^{i} - a^{i})\,\partial_{i} f(a + t(x-a))\,dt = (x^{i} - a^{i})\,g_{i}(x)$ with $g_{i}(x) = \int_{0}^{1} \partial_{i} f(a + t(x-a))\,dt$. Then $g_{i}(a) = \int_{0}^{1} \partial_{i} f(a)\,dt = \partial_{i} f(a)$.
   - *Why needed:* This is the technical heart — it lets us write every smooth $f$ as a constant plus a sum of products of two vanishing factors (after subtracting $f(a)$, what remains is a sum of $(x^{i} - a^{i}) \cdot (g_{i} - g_{i}(a) + g_{i}(a))$).

4. **Compute $v(f)$ via Taylor.** Using subgoals 1, 2, and the Taylor expansion, show $v(f) = v^{i}\,\partial f/\partial x^{i}(a)$ where $v^{i} = v(x^{i})$.
   - *Hint:* From subgoal 3, $f(x) = f(a) + \sum_{i} (x^{i} - a^{i})\,g_{i}(x)$. Apply $v$ using linearity and the Leibniz rule. The constant $f(a)$ contributes $0$ (subgoal 1). Each term $(x^{i} - a^{i})\,g_{i}(x)$ contributes $v(x^{i} - a^{i})\,g_{i}(a) + (x^{i} - a^{i})(a) \cdot v(g_{i})$; but $(x^{i} - a^{i})(a) = 0$ and $v(x^{i} - a^{i}) = v(x^{i})$ (since $a^{i}$ is constant), so the contribution is $v(x^{i})\,g_{i}(a) = v^{i}\,\partial_{i} f(a)$.
   - *Why needed:* This identifies every Euclidean derivation as a directional derivative — the punchline of the proof.

5. **The derivation-vector bijection on $\mathbb{R}^{n}$.** Subgoal 4 shows the map $v \mapsto (v(x^{1}), \dots, v(x^{n}))$ from $T_{a}\mathbb{R}^{n}$ to $\mathbb{R}^{n}$ is injective (and obviously surjective via $(v^{i}) \mapsto v^{i}\,\partial/\partial x^{i}|_{a}$).
   - *Hint:* Injectivity by subgoal 4; surjectivity by direct construction.
   - *Why needed:* This is the equivalence on the local model.

6. **Transport to a manifold via a chart.** Given a chart $(U, \varphi)$ on $M$ around $p$, the chart induces a vector-space isomorphism $T_{p}U \cong T_{\varphi(p)}\hat{U} \cong \mathbb{R}^{n}$. Then $T_{p}M \cong T_{p}U$ (locality of derivations, see [[Def - Derivation at a Point]]).
   - *Hint:* Use that a derivation at $p$ is determined by its action on functions defined near $p$ (locality), and that any chart gives a diffeomorphism with an open subset of $\mathbb{R}^{n}$.
   - *Why needed:* Lifts subgoal 5 from the local model to the abstract manifold.

7. **The derivation-curve bijection.** The map $V_{p}M \to T_{p}M$, $[\gamma] \mapsto (f \mapsto (f \circ \gamma)'(0))$, is well-defined (the equivalence is exactly "same image") and bijective.
   - *Hint:* Well-definedness: by the equivalence relation, $\gamma_{1} \sim \gamma_{2}$ iff $(f \circ \gamma_{1})'(0) = (f \circ \gamma_{2})'(0)$ for all $f$, so they give the same derivation. Surjectivity: given $v \in T_{p}M$ with chart components $v^{i}$, take $\gamma(t) = \varphi^{-1}(\varphi(p) + tv)$. Then $(f \circ \gamma)'(0) = v^{i}\,\partial \hat{f}/\partial x^{i}(\varphi(p)) = v(f)$.
   - *Why needed:* Establishes the second isomorphism in the theorem.

8. **Naturality with $dF$.** Check that for $F : M \to N$, the differential defined by each of the three pictures gives the same map after the isomorphisms are applied.
   - *Hint:* For curves: $[\gamma] \mapsto [F \circ \gamma]$, sending to derivation $f \mapsto (f \circ F \circ \gamma)'(0) = v_{\gamma}(f \circ F) = (dF_{p}(v_{\gamma}))(f)$. For charts: Jacobian matrix multiplication matches the derivation formula by direct expansion.
   - *Why needed:* Shows the isomorphisms are not just bijections of sets but isomorphisms of functorial constructions.

---

# Lemma Decomposition

> [!note]- Lemma 1: Constants are annihilated by derivations
> **Statement:** Let $v$ be a derivation at $a \in M$ (or at $a \in \mathbb{R}^{n}$). For any constant function $c \in C^{\infty}(M)$, $v(c) = 0$.
>
> **Hint:** Apply the Leibniz rule to $1 = 1 \cdot 1$ to deduce $v(1) = 0$. Then use linearity.
>
> **Why needed:** This is the base case for "derivations are first-order". Without it, the constant term of $f$ in the Taylor expansion would contribute to $v(f)$ and break the directional-derivative identification.
>
> > [!note]- Full proof
> > $v(1) = v(1 \cdot 1) = 1 \cdot v(1) + 1 \cdot v(1) = 2\,v(1)$ by the Leibniz rule applied at $a$ (using $1(a) = 1$). Subtracting: $v(1) = 0$. Then for any constant $c$, $v(c) = v(c \cdot 1) = c \cdot v(1) = 0$ by linearity.

> [!note]- Lemma 2: Double-vanishing products are annihilated
> **Statement:** Let $v$ be a derivation at $a$. If $f(a) = g(a) = 0$, then $v(fg) = 0$.
>
> **Hint:** Apply the Leibniz rule directly.
>
> **Why needed:** Combined with Lemma 1, this shows derivations factor through $\mathfrak{m}_{a}/\mathfrak{m}_{a}^{2}$, identifying them with elements of an $n$-dimensional dual.
>
> > [!note]- Full proof
> > $v(fg) = f(a)\,v(g) + g(a)\,v(f) = 0 \cdot v(g) + 0 \cdot v(f) = 0$ directly from the Leibniz rule.

> [!note]- Lemma 3: Taylor expansion with smooth coefficients
> **Statement:** For $f \in C^{\infty}(\mathbb{R}^{n})$ and $a \in \mathbb{R}^{n}$, there exist smooth functions $g_{i}$ on a neighbourhood of $a$ such that
> $$f(x) \;=\; f(a) + \sum_{i=1}^{n} (x^{i} - a^{i})\,g_{i}(x), \qquad g_{i}(a) = \frac{\partial f}{\partial x^{i}}(a).$$
>
> **Hint:** Use the fundamental theorem of calculus along the line from $a$ to $x$: $f(x) - f(a) = \int_{0}^{1} \frac{d}{dt} f(a + t(x - a))\,dt$. Differentiate inside the integral and rearrange.
>
> **Why needed:** This is the technical heart — it gives a *smooth* (not just analytic, not Taylor-series) expansion of any $C^{\infty}$ function as constant + linear-in-coordinates with smooth coefficients. Without this, the proof that every derivation is a directional derivative would fail.
>
> > [!note]- Full proof
> > For $x$ in a convex neighbourhood of $a$, the line $a + t(x - a)$, $t \in [0, 1]$, lies in $\mathrm{dom}(f)$. By the fundamental theorem of calculus,
> > $$f(x) - f(a) = \int_{0}^{1} \frac{d}{dt} f(a + t(x - a))\,dt.$$
> > By the chain rule, $\frac{d}{dt} f(a + t(x - a)) = \sum_{i} (x^{i} - a^{i})\,\partial_{i} f(a + t(x - a))$. So
> > $$f(x) - f(a) = \sum_{i} (x^{i} - a^{i}) \int_{0}^{1} \partial_{i} f(a + t(x - a))\,dt.$$
> > Define $g_{i}(x) = \int_{0}^{1} \partial_{i} f(a + t(x - a))\,dt$. Each $g_{i}$ is smooth (smooth dependence on $x$ through the integrand). At $x = a$, $g_{i}(a) = \int_{0}^{1} \partial_{i} f(a)\,dt = \partial_{i} f(a)$, as claimed.

> [!note]- Lemma 4: Every derivation at $a \in \mathbb{R}^{n}$ is a directional derivative
> **Statement:** For $a \in \mathbb{R}^{n}$ and $v \in T_{a}\mathbb{R}^{n}$, $v(f) = v^{i}\,\partial f/\partial x^{i}(a)$ where $v^{i} = v(x^{i})$. Hence the map $T_{a}\mathbb{R}^{n} \to \mathbb{R}^{n}$, $v \mapsto (v(x^{1}), \dots, v(x^{n}))$, is a vector-space isomorphism.
>
> **Hint:** Apply $v$ to the Taylor expansion of Lemma 3, using Lemmas 1 and 2 to kill the constant and the "second-order remainder" piece. What is left is the directional derivative.
>
> **Why needed:** This is the equivalence theorem on the local model $\mathbb{R}^{n}$. The manifold case follows by transport via a chart.
>
> > [!note]- Full proof
> > By Lemma 3, $f = f(a) + \sum_{i} (x^{i} - a^{i})\,g_{i}$ with $g_{i}(a) = \partial_{i} f(a)$. Apply $v$:
> > $$v(f) = v(f(a)) + \sum_{i} v((x^{i} - a^{i})\,g_{i}).$$
> > $v(f(a)) = 0$ by Lemma 1.
> >
> > For each term $v((x^{i} - a^{i})\,g_{i})$, apply the Leibniz rule:
> > $$v((x^{i} - a^{i})\,g_{i}) = (x^{i} - a^{i})(a)\,v(g_{i}) + g_{i}(a)\,v(x^{i} - a^{i}).$$
> > The first contribution is $0$ since $(x^{i} - a^{i})(a) = 0$. The second is $g_{i}(a)\,v(x^{i}) - g_{i}(a)\,v(a^{i})$, and $v(a^{i}) = 0$ by Lemma 1 (since $a^{i}$ is constant). So the term is $g_{i}(a)\,v(x^{i}) = \partial_{i} f(a)\,v^{i}$.
> >
> > Summing: $v(f) = \sum_{i} v^{i}\,\partial_{i} f(a)$. Hence $v$ is the directional-derivative operator $D_{v}|_{a}$ with $v$ the geometric vector $(v^{1}, \dots, v^{n})$. The map $v \mapsto (v(x^{1}), \dots, v(x^{n}))$ has inverse $(v^{1}, \dots, v^{n}) \mapsto v^{i}\,\partial/\partial x^{i}|_{a}$, and both are linear — so it is a vector-space isomorphism.

> [!note]- Lemma 5: The derivation-curve correspondence is a bijection
> **Statement:** The map $\Theta : V_{p}M \to T_{p}M$, $[\gamma] \mapsto v_{\gamma}$ where $v_{\gamma}(f) = (f \circ \gamma)'(0)$, is a well-defined bijection.
>
> **Hint:** Well-definedness is by the definition of the curve-equivalence. Injectivity by the same definition. Surjectivity by realizing each tangent vector as a velocity (Proposition 3.23).
>
> **Why needed:** Establishes the second isomorphism in the theorem statement.
>
> > [!note]- Full proof
> > *Well-defined:* if $\gamma_{1} \sim \gamma_{2}$, then by definition $(f \circ \gamma_{1})'(0) = (f \circ \gamma_{2})'(0)$ for all $f$, so $v_{\gamma_{1}} = v_{\gamma_{2}}$. Hence $\Theta$ is well-defined on equivalence classes.
> >
> > *Injective:* if $\Theta([\gamma_{1}]) = \Theta([\gamma_{2}])$, then $(f \circ \gamma_{1})'(0) = (f \circ \gamma_{2})'(0)$ for all $f$, which is the definition of $\gamma_{1} \sim \gamma_{2}$. So $[\gamma_{1}] = [\gamma_{2}]$.
> >
> > *Surjective:* given $v \in T_{p}M$, pick a chart $(U, \varphi)$ at $p$ and write $v = v^{i}\,\partial/\partial x^{i}|_{p}$ in the coordinate basis. Define $\gamma(t) = \varphi^{-1}(\varphi(p) + tv)$ for $|t|$ small. Then $\gamma(0) = p$ and the chain rule gives, for any $f$, $(f \circ \gamma)'(0) = \partial_{i}(f \circ \varphi^{-1})(\varphi(p))\,v^{i} = v(f)$. So $\Theta([\gamma]) = v$. Hence $\Theta$ is surjective.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** With notation as above, $V_{p}M \cong T_{p}M \cong \mathrm{Chart}_{p}(M)$ as vector spaces, with the isomorphisms natural in $F$.
>
> *Proof.* We establish each isomorphism separately.
>
> **Step 0 (well-posedness of curve picture).** Verify that the relation $\gamma_{1} \sim \gamma_{2} \iff (f \circ \gamma_{1})'(0) = (f \circ \gamma_{2})'(0)$ for all smooth $f$ defined near $p$ is an equivalence relation: reflexivity, symmetry, and transitivity are immediate from the corresponding properties of equality in $\mathbb{R}$.
>
> **Step 1 (derivation-vector isomorphism on $\mathbb{R}^{n}$).** This is Lemma 4 (above): for $a \in \mathbb{R}^{n}$, the map $v \mapsto (v(x^{1}), \dots, v(x^{n}))$ is a vector-space isomorphism $T_{a}\mathbb{R}^{n} \to \mathbb{R}^{n}$, with inverse $(v^{i}) \mapsto v^{i}\,\partial/\partial x^{i}|_{a}$. The proof uses Lemmas 1, 2, and 3 (constants annihilated, double-vanishing annihilated, Taylor expansion).
>
> **Step 2 (transport to manifold via chart).** Let $(U, \varphi)$ be a chart at $p$. By locality of derivations (Lemma in [[Def - Derivation at a Point]]), $T_{p}M = T_{p}U$. The diffeomorphism $\varphi : U \to \hat{U} \subseteq \mathbb{R}^{n}$ induces an isomorphism $d\varphi_{p} : T_{p}U \to T_{\varphi(p)}\hat{U}$. And $T_{\varphi(p)}\hat{U} = T_{\varphi(p)}\mathbb{R}^{n}$ (open subset has the same tangent space). Composing: $T_{p}M \cong T_{\varphi(p)}\mathbb{R}^{n} \cong \mathbb{R}^{n}$, with the chart basis $\partial/\partial x^{i}|_{p}$ corresponding to the standard basis $\partial/\partial x^{i}|_{\varphi(p)}$ of $\mathbb{R}^{n}$. This establishes the chart-tuple isomorphism.
>
> **Step 3 (change of chart formula).** Suppose $(U, \varphi)$ and $(V, \tilde\varphi)$ are two charts at $p$, with coordinates $x^{i}$ and $\tilde x^{j}$. Applying $\partial/\partial x^{i}|_{p}$ to $\tilde x^{j}$: $(\partial/\partial x^{i}|_{p})(\tilde x^{j}) = \partial(\tilde\varphi \circ \varphi^{-1})^{j}/\partial x^{i}(\varphi(p)) = \partial \tilde x^{j}/\partial x^{i}(\varphi(p))$. Hence the components transform contragrediently by the Jacobian.
>
> **Step 4 (derivation-curve isomorphism).** This is Lemma 5 (above): the map $\Theta : V_{p}M \to T_{p}M$ is a well-defined bijection. It is linear after vector-space structure is transported from $T_{p}M$ to $V_{p}M$.
>
> **Step 5 (naturality with $dF$).** For a smooth map $F : M \to N$ and $v \in T_{p}M$, the derivation-picture differential $dF_{p}(v)$ acts on $f \in C^{\infty}(N)$ by $(dF_{p}(v))(f) = v(f \circ F)$. The curve-picture differential of $[\gamma]$ is $[F \circ \gamma]$, which under $\Theta$ corresponds to the derivation $f \mapsto (f \circ F \circ \gamma)'(0) = v_{\gamma}(f \circ F) = (dF_{p}(v_{\gamma}))(f)$. These agree. For the chart-tuple picture, the Jacobian-matrix multiplication formula matches the derivation formula by direct expansion in coordinate bases — Lee equation (3.9). So the three differentials agree under the isomorphisms, establishing naturality.
>
> The three constructions are isomorphic as functors from pointed smooth manifolds to vector spaces. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebraic geometry — Zariski tangent space.** For an affine variety $X = V(I) \subseteq \mathbb{A}^{n}$ over a field $k$, the local ring at a point $p \in X$ is $\mathcal{O}_{X, p}$ with maximal ideal $\mathfrak{m}_{p}$. The **Zariski tangent space** is $(\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2})^{*}$, the dual of the quotient. The same argument as in the proof above shows this dual classifies "first-order data" at $p$ — derivations $D : \mathcal{O}_{X, p} \to k$ satisfying linearity and Leibniz at $p$. So the Zariski tangent space *is* the algebraic-geometric analogue of $T_{p}M$, with the same proof structure. The smoothness of $X$ at $p$ is exactly the condition that the Zariski tangent space has the right dimension.

**Functional analysis — Fréchet derivative.** For a smooth function $f : B \to B'$ between Banach spaces, the **Fréchet derivative** $Df_{a}$ at $a \in B$ is the bounded linear operator $B \to B'$ best approximating $f$ near $a$. The same equivalence theorem holds in infinite dimensions: the directional derivative (curve picture: $\gamma(t) = a + tv$ for $v \in B$) and the operator definition (Fréchet picture) coincide. The proof structure is unchanged — Taylor's theorem with remainder applied to a smooth map between Banach spaces. This is the input for the calculus of variations and optimization on function spaces.

**Lie theory — Lie algebra of a matrix Lie group.** For a matrix Lie group $G \subseteq \mathrm{GL}(n, \mathbb{R})$ defined by smooth equations, the Lie algebra $\mathfrak{g} = T_{I}G$ can be computed via *any* of three definitions: as the set of matrices $A$ for which $e^{tA} \in G$ for all $t$ (one-parameter subgroup picture), as derivations of $C^{\infty}(G)$ at $I$, or as the kernel of the differential of the defining equations. The equivalence theorem certifies these three computations agree. Example: for $\mathrm{SO}(n) = \{A : A^{T}A = I\}$, the curve picture gives $\dot A(0)^{T} + \dot A(0) = 0$, i.e., $\mathfrak{so}(n)$ is skew-symmetric matrices. See [[Ex - Tangent Space of the General Linear Group at the Identity]].

**Probability theory — generators of Markov processes.** A time-homogeneous Markov process on a smooth manifold has an **infinitesimal generator** $L$ acting on $C^{\infty}(M)$, defined by $(Lf)(p) = \lim_{t \to 0^{+}} (\mathbb{E}_{p}[f(X_{t})] - f(p))/t$. For diffusion processes, $L$ is a second-order differential operator at each point, and its first-order part — the "drift" — is a derivation at each point, hence a vector field. The equivalence theorem is what licenses calling the first-order part a "vector field" rather than an abstract operator.

---

# Bridges

- **The derivation-vector bijection is a special case of the Hochschild-Kostant-Rosenberg theorem.** In commutative algebra, derivations of a smooth $\mathbb{R}$-algebra valued in the algebra itself are governed by Kähler differentials, and the structure is fully captured by the **HKR theorem**: for a smooth manifold, the Hochschild cohomology of $C^{\infty}(M)$ is the algebra of polyvector fields on $M$. The derivation-vector bijection at a point is the degree-1 piece of HKR. This deep structural fact undergirds the entire framework of differential geometry as commutative algebra.

- **The chart-tuple definition is the classical tensor calculus formulation.** Physicists from Einstein onward defined tangent vectors as "components transforming by the Jacobian rule under change of chart". The equivalence theorem rigorously justifies this by showing the modern abstract definition produces objects whose components do transform that way. The reverse direction — recovering an abstract object from chart-tuple data — is what the theorem licenses, and what physics textbooks implicitly assume.

- **The curve definition is what survives to Banach manifolds and infinite-dimensional geometry.** The chart-tuple definition fails in infinite dimensions (no natural Jacobian-tuple structure on an infinite-dimensional vector space), and the derivation definition requires care with the function-space topology. The curve definition — equivalence classes of smooth curves — generalizes verbatim to Banach manifolds. So the curve definition is the most robust under generalization.

- **The cotangent space and the dual statement.** The vector space $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$ — first-order Taylor data at $p$ — is the **cotangent space** $T^{*}_{p}M$ (see [[Def - Dual Space]] for the linear-algebra prototype). The equivalence theorem is dually the statement that $T^{*}_{p}M \cong \mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$ canonically, and that the dual of this is $T_{p}M$. So the cotangent space is the *fundamental* object, and the tangent space is its dual — a structural fact obscured by the historical preference for the tangent picture.

- **Naturality is the technical content.** The equivalence theorem gives bijections between three constructions, but the *useful* content is that the bijections commute with the differential of every smooth map. Without naturality, the three definitions would be unrelated functors on different domains. With naturality, they are the same functor in different guises — and any theorem using $T_{p}M$ holds equally in any of the three pictures.

---

# Unlocked by This

> [!tip] All Subsequent Differential Geometry *(from Differential Geometry)*
> This theorem is the foundation of the rest of differential geometry. Every later result — the chain rule, the rank theorem, vector fields, Lie brackets, differential forms, Stokes' theorem — uses tangent vectors and the differential, and is licensed to switch freely between the three pictures by the equivalence. Without the theorem, the subject would fragment into three parallel theories.

> [!tip] Lie Correspondence *(from Lie Theory)*
> The bijection between Lie groups and Lie algebras (in a suitable category) rests on the equivalence theorem: the tangent space at the identity can be computed via curves (one-parameter subgroups), derivations (left-invariant vector fields), or chart-tuples (matrix entries in an embedding) — all three give the same Lie algebra. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

> [!tip] Jet Bundles *(from Differential Geometry)*
> The equivalence theorem identifies the tangent space with "first-order Taylor data at $p$". Generalizing to "$k$-th order Taylor data at $p$" produces the **jet bundle** $J^{k}(M)$, with $J^{1}(M) = TM$. Jets are the natural setting for higher-order calculus on manifolds — partial differential equations, the Cartan distribution, the variational bicomplex. The equivalence theorem is the order-1 case of the more general jet equivalence.

> [!tip] Synthetic Differential Geometry *(from Category Theory)*
> An alternative foundation called **synthetic differential geometry** takes "infinitesimal" elements seriously and works in a topos where there are non-zero infinitesimals $\varepsilon$ with $\varepsilon^{2} = 0$. In this framework, a tangent vector at $p$ is literally a curve $\gamma : D \to M$ from the "infinitesimal interval" $D = \{\varepsilon : \varepsilon^{2} = 0\}$ with $\gamma(0) = p$, and the equivalence theorem becomes a definitional matter. The classical equivalence theorem is the reflection of this in the topos of sheaves on smooth manifolds.
