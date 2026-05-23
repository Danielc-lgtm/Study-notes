---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Integral Curve of a Vector Field"
  - "Thm - The Contraction Mapping Principle"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold. $X \in \mathfrak{X}(M)$ is a smooth [[Def - Smooth Vector Field|vector field]]. An [[Def - Integral Curve of a Vector Field|integral curve]] of $X$ is a smooth curve $\gamma : J \to M$ satisfying $\gamma'(t) = X_{\gamma(t)}$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Statement

> **Theorem (Local existence and uniqueness of integral curves).** Let $M$ be a smooth manifold and $X \in \mathfrak{X}(M)$ a smooth vector field. For every $p \in M$ there exist $\varepsilon > 0$ and a smooth integral curve $\gamma : (-\varepsilon, \varepsilon) \to M$ of $X$ with $\gamma(0) = p$. If $\gamma_1 : J_1 \to M$ and $\gamma_2 : J_2 \to M$ are two integral curves of $X$ with $\gamma_1(t_0) = \gamma_2(t_0)$ for some $t_0 \in J_1 \cap J_2$, then $\gamma_1 = \gamma_2$ on $J_1 \cap J_2$.

> **Corollary (Maximal integral curve).** For every $p \in M$ there is a unique maximal integral curve $\gamma^{(p)} : \mathcal{D}^{(p)} \to M$ of $X$ with $\gamma^{(p)}(0) = p$, defined on an open interval $\mathcal{D}^{(p)} \subseteq \mathbb{R}$ containing $0$.

> **Corollary (Smooth dependence on initial point).** The function $(t, p) \mapsto \gamma^{(p)}(t)$ is smooth on the open set $\mathcal{D} = \{(t, p) : t \in \mathcal{D}^{(p)}\} \subseteq \mathbb{R} \times M$. (This is part of the [[Thm - Fundamental Theorem on Flows]].)

---

# Motivation

Once we have the notion of vector field and the notion of integral curve, the most basic question is **whether integral curves exist** and **whether they are unique** when they do. Without an answer to this, the rest of the chapter is built on sand: the [[Def - Flow of a Vector Field|flow]] would not be well-defined, the [[Thm - Commuting Flows Theorem]] would have no flows to compare, the [[Thm - Canonical Form for a Nonvanishing Vector Field|Straightening Theorem]] would have no integral curves to straighten.

The answer is satisfying: integral curves exist locally, are unique, and depend smoothly on the starting point. The mechanism for the answer is a reduction: an integral curve in a chart is exactly a solution to a system of autonomous first-order ODEs, and the existence-and-uniqueness theory for ODEs — [[Thm - The Contraction Mapping Principle|Picard–Lindelöf]] — handles this case. The manifold input adds nothing analytic; it only adds the geometric job of gluing chart-local results into a global statement.

The role of this theorem in the chapter is therefore as the analytic gateway: it imports the contraction mapping principle into differential geometry. Every flow construction in the chapter ultimately depends on this theorem, and every existence statement traces back to Picard–Lindelöf via this theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ is a smooth vector field on a smooth manifold". The skill is recognizing this hypothesis in disguise.

The first disguised source is **a smooth ODE system $\dot x = f(x)$ on an open subset of $\mathbb{R}^n$ with smooth $f$**. The bridge is direct: $f$ is the components of a smooth vector field $X = f^i \partial_i$ on $U \subseteq \mathbb{R}^n$, and solutions of the ODE are exactly integral curves of $X$. So whenever an autonomous smooth first-order ODE appears — in physics, in economics, in biology — this theorem applies. The non-obviousness: the ODE system is the "intrinsic" object; rewriting it as a vector field gives access to the differential-geometric toolkit.

The second disguised source is **a smooth $\mathbb{R}$-action $\phi : \mathbb{R} \times M \to M$**, which generates a complete vector field $X_p = \frac{d}{dt}|_{t=0} \phi(t, p)$. The bridge: starting from the action, the infinitesimal generator $X$ is automatically smooth, and the action itself is the flow of $X$, so the integral curves are $t \mapsto \phi(t, p)$. The implication "smooth $\mathbb{R}$-action $\implies$ smooth vector field with global flow" is the geometric content of the bijection between complete vector fields and one-parameter group actions; existence-and-uniqueness is hidden inside this bijection, certifying that the action is uniquely determined by its generator.

The third disguised source is **a left-invariant vector field on a Lie group**. The bridge: left-invariance plus smoothness gives a global flow (because the existence interval is uniformly bounded below by the equivariance of left translation; see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]]). So every element of $\mathfrak{g} = T_e G$ extends to a left-invariant vector field on all of $G$, with a uniquely determined integral curve through every point — the foundation of the exponential map.

**Targets (Output Amplification)**

The conclusion is "there exists a unique smooth integral curve". On its own this is an existence statement; combined with one further property $D$ it becomes a positive structural result.

The first combination is **existence-and-uniqueness combined with compactness gives completeness.** Property $D$: the support of $X$ is compact (or $M$ is compact). The amplified result: every integral curve of $X$ is defined for all $t \in \mathbb{R}$, i.e. $X$ is [[Def - Complete Vector Field|complete]]. The bridge is the uniform time lemma: by compactness, there is a single $\varepsilon > 0$ such that every integral curve exists at least on $(-\varepsilon, \varepsilon)$, and the group law extends to all time. See [[Ex - Compactly Supported Vector Fields are Complete]].

The second combination is **uniqueness combined with $F$-relatedness gives flow naturality.** Property $D$: $F : M \to N$ is smooth with $X \sim_F X'$. Then $F$ takes integral curves of $X$ to integral curves of $X'$ (Lee Proposition 9.6), because both $F \circ \gamma$ and $\gamma_{F(p)}^{X'}$ are integral curves of $X'$ starting at $F(p)$, and uniqueness forces them equal. The conclusion is that $F$ semiconjugates the flow of $X$ to the flow of $X'$, $F \circ \phi^X_t = \phi^{X'}_t \circ F$ — the foundation of [[Def - F-Related Vector Fields|naturality]].

The third combination is **smooth dependence on initial conditions combined with compactness of a parameter space gives smoothness of derived quantities.** Property $D$: a family of starting points $p_s$ depending smoothly on $s \in K$ for $K$ compact, and a smooth functional $F(\gamma)$ of integral curves. Then $s \mapsto F(\gamma_{p_s})$ is smooth on $K$. The amplification is that any "smooth integral of $X$" — flow-line average, mean exit time, action integral — inherits the smoothness from this theorem.

---

# Why Is It True

**The mechanism in one sentence: in any chart, the integral-curve equation is an autonomous ODE with smooth (hence Lipschitz) right-hand side, and Picard's iteration on a small enough function-space ball is a contraction whose unique fixed point is the integral curve.**

Unpacking this: in a chart $(U, (x^i))$ around $p$, the integral curve condition $\gamma'(t) = X_{\gamma(t)}$ becomes the system $\dot \gamma^i = X^i(\gamma)$, with smooth right-hand side $X^i$. Equivalently, in integrated form, $\gamma(t) = p + \int_0^t X(\gamma(s))\,ds$. The right-hand side defines an operator $T$ on continuous curves valued in some small ball around $p$, sending $\gamma$ to $p + \int_0^t X(\gamma(s))\,ds$. A fixed point of $T$ is exactly an integral curve.

Picard–Lindelöf says: on a small enough function-space ball — concretely, curves $\gamma : [-\varepsilon, \varepsilon] \to B$ with the supremum metric, where $B$ is a small ball around $p$ — $T$ is a contraction. The reason is that the Lipschitz constant of $X$ on $B$ is finite (smooth function on a compact set), and multiplying it by the small time $\varepsilon$ gives a Lipschitz factor for $T$ that is less than $1$. The contraction mapping principle then delivers a unique fixed point — the unique integral curve on $(-\varepsilon, \varepsilon)$.

Uniqueness on overlapping domains: two integral curves $\gamma_1, \gamma_2$ agreeing at $t_0$ must agree on a neighbourhood (Picard–Lindelöf uniqueness in that neighbourhood), so the set $\{t : \gamma_1(t) = \gamma_2(t)\}$ is open. It is also closed (by continuity), and contains $t_0$, so it equals the connected component containing $t_0$ — the whole common domain. This is why two integral curves agreeing at *one* point agree *everywhere* they are both defined.

Smoothness as a function of starting point: the standard smoothness conclusion of Picard–Lindelöf in $\mathbb{R}^n$ says the fixed point depends smoothly on the parameters (here, the starting point $p$). The contraction mapping principle, applied to a Banach space of curves depending on $p$, gives a fixed point in the parameter category that is smooth in $p$.

The geometric content of the proof is therefore concentrated entirely in the manifold $\to$ chart reduction: the analytic engine is Picard–Lindelöf, the geometric input is just "smoothness in a chart equals smoothness everywhere".

---

# What Makes This Hard

The conceptual difficulty is recognizing that **the entire content of the theorem is supplied by [[Thm - The Contraction Mapping Principle|the contraction mapping principle]], with no manifold-specific input**: the manifold appears only in the reduction "work in a chart" and the patching "the result is chart-independent by uniqueness". The most common error is to think the manifold setting requires a more elaborate ODE theory; in fact, the ODE theory on $\mathbb{R}^n$ is *identical*. A second subtlety is the global statement: uniqueness extends from any chart neighbourhood to the entire common domain of two integral curves because "agreement" is both open and closed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Work in a chart around $p$; the integral-curve equation becomes an autonomous smooth ODE on an open subset of $\mathbb{R}^n$. Convert to an integral fixed-point equation. Apply [[Thm - The Contraction Mapping Principle|Picard–Lindelöf]] (the contraction mapping principle for the integral operator) to get a unique smooth solution on a small interval. Uniqueness on overlapping domains is "agreement is open and closed".

**Subgoal decomposition:**

1. **In a chart, the integral-curve equation is an autonomous ODE.** Show that in a chart $(U, (x^i))$, $\gamma'(t) = X_{\gamma(t)}$ becomes the system $\dot\gamma^i = X^i \circ \gamma$.
   - *Hint:* Apply the differential of $\gamma$ to $d/dt$ and unpack in coordinates.
   - *Why needed:* Reduces the manifold question to the standard $\mathbb{R}^n$-ODE setup.

2. **The integral form is a fixed-point equation.** Show that $\gamma(t) = p + \int_0^t X(\gamma(s))\,ds$ on $(-\varepsilon, \varepsilon)$ is equivalent to $\gamma$ being a smooth integral curve with $\gamma(0) = p$.
   - *Hint:* Differentiate the integral equation; conversely, integrate the differential equation from $0$ to $t$.
   - *Why needed:* Sets up the contraction mapping principle as the existence engine.

3. **The integral operator is a contraction on a small enough function-space ball.** Show that for $\varepsilon > 0$ and a small ball $B$ around $p$, the operator $T : C^0((-\varepsilon, \varepsilon), B) \to C^0((-\varepsilon, \varepsilon), B)$, $T\gamma(t) = p + \int_0^t X(\gamma(s))\,ds$, satisfies $\sup_t |T\gamma_1(t) - T\gamma_2(t)| \leq L \varepsilon \sup_t |\gamma_1(t) - \gamma_2(t)|$, with $L$ the Lipschitz constant of $X$ on $\overline B$; choose $\varepsilon$ so $L\varepsilon < 1$.
   - *Hint:* $T\gamma_1 - T\gamma_2 = \int_0^t (X(\gamma_1) - X(\gamma_2))\,ds$; bound by Lipschitz.
   - *Why needed:* Picard–Lindelöf produces a fixed point — the integral curve.

4. **Smoothness from the bootstrap.** A continuous fixed point of $T$ satisfies $\gamma' = X \circ \gamma$, hence $\gamma'$ is continuous; differentiating again, $\gamma''$ is the chain-rule derivative of $X \circ \gamma$, hence continuous; induct to get $\gamma \in C^\infty$.
   - *Hint:* Differentiating the equation $\gamma' = X \circ \gamma$ gains one degree of regularity each time, until you reach $C^\infty$ since $X$ is smooth.
   - *Why needed:* Promotes the $C^0$ fixed point to a smooth curve, as required by the integral-curve definition.

5. **Uniqueness globally.** If $\gamma_1$ and $\gamma_2$ agree at $t_0$, the set $\{t : \gamma_1(t) = \gamma_2(t)\}$ is open (local uniqueness in any chart around a point of agreement) and closed (continuity), hence equals the connected common domain $J_1 \cap J_2$.
   - *Hint:* "Open" uses Picard–Lindelöf locally; "closed" uses that the diagonal is closed in $M \times M$ (Hausdorff).
   - *Why needed:* Promotes local uniqueness to global uniqueness, giving the maximal integral curve.

---

# Lemma Decomposition

> [!note]- Lemma 1: An integral curve in a chart is a solution of an autonomous ODE
> **Statement:** Let $\gamma : J \to M$ be a smooth curve passing through the chart domain $(U, (x^i))$, and write $\gamma^i = x^i \circ \gamma$. Then $\gamma$ is an integral curve of $X = X^i \partial_i$ on $U$ if and only if $\dot\gamma^i(t) = X^i(\gamma^1(t), \dots, \gamma^n(t))$ for every $t \in J$ with $\gamma(t) \in U$.
>
> **Hint:** Apply the differential of $\gamma$ to $d/dt|_t$ and expand both sides in the coordinate basis.
>
> **Why needed:** Reduces the manifold-level integral-curve equation to a standard system of ODEs on $\mathbb{R}^n$, where Picard–Lindelöf applies.
>
> > [!note]- Full proof
> > $\gamma'(t) := d\gamma_t(d/dt|_t)$. In the chart, $d\gamma_t(d/dt|_t) = \dot\gamma^i(t)\, \partial_i|_{\gamma(t)}$ (this is the definition of the velocity in coordinates). On the other hand, $X_{\gamma(t)} = X^i(\gamma(t))\,\partial_i|_{\gamma(t)}$. Equating components in the basis $\{\partial_i|_{\gamma(t)}\}$ of $T_{\gamma(t)} M$ gives $\dot\gamma^i(t) = X^i(\gamma(t))$ for each $i$.

> [!note]- Lemma 2: The integral form is equivalent
> **Statement:** Let $X^i$ be smooth on an open ball $B \subseteq \mathbb{R}^n$. A continuous curve $\gamma : (-\varepsilon, \varepsilon) \to B$ satisfies $\dot\gamma^i = X^i \circ \gamma$ with $\gamma(0) = p$ if and only if $\gamma(t) = p + \int_0^t X(\gamma(s))\,ds$ for all $t \in (-\varepsilon, \varepsilon)$, and any such continuous $\gamma$ is automatically smooth.
>
> **Hint:** Differentiate the integral form to recover the differential form; conversely integrate the differential form from $0$ to $t$ using $\gamma(0) = p$.
>
> **Why needed:** The integral form is the input to the contraction mapping principle; the smoothness follows from a regularity bootstrap.
>
> > [!note]- Full proof
> > *($\Rightarrow$)* If $\dot\gamma = X \circ \gamma$ and $\gamma(0) = p$, then by the fundamental theorem of calculus $\gamma(t) - p = \int_0^t \dot\gamma(s)\,ds = \int_0^t X(\gamma(s))\,ds$.
> >
> > *($\Leftarrow$)* If $\gamma(t) = p + \int_0^t X(\gamma(s))\,ds$ then $\gamma$ is continuous; the integrand $s \mapsto X(\gamma(s))$ is continuous, so $\gamma$ is in fact $C^1$ with derivative $X(\gamma(t))$. Differentiating again: $\gamma' = X \circ \gamma$ is $C^1$ (composition of smooth and $C^1$), so $\gamma$ is $C^2$. Induction: if $\gamma$ is $C^k$, then $X \circ \gamma$ is $C^k$, so $\gamma' = X \circ \gamma$ is $C^k$, hence $\gamma$ is $C^{k+1}$. By induction $\gamma \in C^\infty$.

> [!note]- Lemma 3: The integral operator is a contraction
> **Statement:** Let $X$ be smooth on a neighborhood of $\bar B$ where $\bar B$ is a closed ball around $p$, with Lipschitz constant $L$ on $\bar B$. Choose $\varepsilon > 0$ such that $L \varepsilon < 1$ and such that, restricting to the appropriate function space (e.g. continuous curves on $[-\varepsilon, \varepsilon]$ starting at $p$ with image in $\bar B$), the operator $T\gamma(t) = p + \int_0^t X(\gamma(s))\,ds$ maps the space to itself. Then $T$ is a contraction with constant $L\varepsilon$.
>
> **Hint:** Bound $|T\gamma_1(t) - T\gamma_2(t)|$ by $\int_0^t |X(\gamma_1(s)) - X(\gamma_2(s))|\,ds \leq L \int_0^t |\gamma_1(s) - \gamma_2(s)|\,ds \leq L \varepsilon \sup |\gamma_1 - \gamma_2|$.
>
> **Why needed:** Once $T$ is a contraction on a complete metric space, [[Thm - The Contraction Mapping Principle]] gives a unique fixed point — the integral curve.
>
> > [!note]- Full proof
> > The space $\mathcal{C} = \{\gamma : [-\varepsilon, \varepsilon] \to \bar B \text{ continuous with } \gamma(0) = p\}$ is a closed subset of $C^0([-\varepsilon, \varepsilon], \mathbb{R}^n)$ with the supremum metric, hence complete. For $\varepsilon$ small enough, $\bar B$ contains $p + \int_0^t X(\gamma)\,ds$ for any $\gamma \in \mathcal{C}$ (bound the integral by $\varepsilon \sup_{\bar B} |X|$ and choose $\varepsilon$ accordingly), so $T : \mathcal{C} \to \mathcal{C}$ is well-defined.
> >
> > Contraction estimate: for $\gamma_1, \gamma_2 \in \mathcal{C}$,
> > $$|T\gamma_1(t) - T\gamma_2(t)| = \left|\int_0^t (X(\gamma_1(s)) - X(\gamma_2(s)))\,ds\right| \leq L|t| \sup |\gamma_1 - \gamma_2| \leq L\varepsilon \sup |\gamma_1 - \gamma_2|.$$
> >
> > Taking the supremum over $t \in [-\varepsilon, \varepsilon]$, $\sup |T\gamma_1 - T\gamma_2| \leq L \varepsilon \sup |\gamma_1 - \gamma_2|$, with $L\varepsilon < 1$ by choice. So $T$ is a contraction.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Reduction to a chart.** Let $p \in M$ and choose a smooth chart $(U, \varphi = (x^1, \dots, x^n))$ around $p$ with $\varphi(p) = 0 \in \mathbb{R}^n$. The chart pulls $X$ back to a smooth vector field $\tilde X = X^i \partial_i$ on the open set $\varphi(U) \subseteq \mathbb{R}^n$. A smooth integral curve of $X$ through $p$ corresponds (via $\varphi$) to a smooth integral curve of $\tilde X$ through $0$ in $\varphi(U)$ — see Lemma 1. So it suffices to prove the theorem on the open subset $\varphi(U) \subseteq \mathbb{R}^n$.
>
> **Step 1 — Local existence.** Let $\bar B \subset \varphi(U)$ be a closed ball around $0$. The components $X^i$ are smooth, hence Lipschitz on $\bar B$ with some constant $L$. Choose $\varepsilon > 0$ with $L \varepsilon < 1$ and $\varepsilon \sup_{\bar B} |X| < \text{radius of } \bar B$. Define $T : \mathcal{C} \to \mathcal{C}$ on the closed [[Def - Subspace|subspace]] $\mathcal{C} \subset C^0([-\varepsilon, \varepsilon], \bar B)$ of curves starting at $0$, by $T\gamma(t) = \int_0^t X(\gamma(s))\,ds$. By Lemma 3, $T$ is a contraction with constant $L\varepsilon < 1$ on the complete metric space $\mathcal{C}$. By [[Thm - The Contraction Mapping Principle]], $T$ has a unique fixed point $\gamma_0 \in \mathcal{C}$. By Lemma 2, $\gamma_0$ is smooth and satisfies $\dot\gamma_0^i = X^i \circ \gamma_0$ with $\gamma_0(0) = 0$, i.e. it is a smooth integral curve of $\tilde X$ on $[-\varepsilon, \varepsilon]$ through $0$. Restricting to $(-\varepsilon, \varepsilon)$ and pushing forward by $\varphi^{-1}$ gives an integral curve of $X$ on $M$ through $p$.
>
> **Step 2 — Local uniqueness in the chart.** If $\gamma_1$ and $\gamma_2$ are two smooth integral curves of $X$ in the chart, defined on a common interval $I$ around $0$ with $\gamma_1(0) = \gamma_2(0) = p$, both are fixed points of $T$ on a sufficiently small subinterval $[-\varepsilon', \varepsilon']$ — uniqueness of the fixed point gives $\gamma_1 = \gamma_2$ on $[-\varepsilon', \varepsilon']$.
>
> **Step 3 — Global uniqueness on common domain.** Suppose $\gamma_1 : J_1 \to M$ and $\gamma_2 : J_2 \to M$ are integral curves of $X$ with $\gamma_1(t_0) = \gamma_2(t_0)$ for some $t_0 \in J_1 \cap J_2$. Let $A = \{t \in J_1 \cap J_2 : \gamma_1(t) = \gamma_2(t)\}$. Then $A$ is non-empty ($t_0 \in A$). $A$ is closed in $J_1 \cap J_2$ because $\gamma_1, \gamma_2$ are continuous and the diagonal of $M \times M$ is closed (Hausdorff). $A$ is open: if $t_1 \in A$, by translation reduce to the case $t_1 = 0$; in a chart around $\gamma_1(0) = \gamma_2(0)$, Step 2 gives $\gamma_1 = \gamma_2$ on a neighbourhood of $0$. Since $J_1 \cap J_2$ is connected, $A = J_1 \cap J_2$.
>
> **Step 4 — Maximal integral curve.** Take the union of all integral curves of $X$ through $p$, parametrized over their respective domains. By Step 3 these all agree on overlaps, so the union is well-defined and is an integral curve on the (open) union $\mathcal{D}^{(p)}$ of all the individual domains. By construction it is maximal. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Existence of solutions to Hamilton's equations.** In Hamiltonian mechanics, the time-evolution is the flow of the Hamiltonian vector field $X_H$ on phase space. Existence and uniqueness of trajectories starting from any initial state is *literally* this theorem, applied to $X_H$. The nonobvious part is recognising that the Hamiltonian equations $\dot q^i = \partial_p H, \dot p^i = -\partial_q H$ are first-order ODEs in $2n$ variables, hence integral curves of the appropriate vector field. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] forward.

**Geodesic existence on a Riemannian manifold.** The geodesic equation on $(M, g)$ is a second-order ODE; rewriting as a first-order system on the tangent bundle $TM$ — the "geodesic spray" — turns [[Def - Geodesic|geodesics]] into integral curves of a vector field on $TM$. Existence and uniqueness of geodesics with given initial position and velocity is this theorem applied to the spray. The nonobvious part is the lift from second-order to first-order on $TM$.

**Solutions to autonomous differential equations in population biology and economics.** Lotka–Volterra systems, the SIR model, dynamic programming policy iteration — all are autonomous smooth ODEs on an open subset of $\mathbb{R}^n$, hence integral curves of a smooth vector field. The recognition step is to write down the right-hand side as components of a vector field, then quote existence-uniqueness.

**Existence of the geodesic exponential map.** The exponential map $\exp_p : T_p M \to M$ in Riemannian geometry sends $v \in T_p M$ to $\gamma_v(1)$, where $\gamma_v$ is the geodesic starting at $p$ with velocity $v$. The smoothness of $\exp_p$ in $v$ is the smoothness of the integral curves of the geodesic spray in the initial point — Corollary 3 of this theorem, applied on $TM$. The nonobvious part is that smoothness in the *initial vector* (a point in $TM$) is what gives the [[Def - Diffeomorphism|diffeomorphism]] property of $\exp_p$ near $0 \in T_p M$.

---

# Bridges

- **[[Thm - The Contraction Mapping Principle|Contraction Mapping Principle]]** — the analytic engine of this theorem. The integral form of the ODE, $\gamma(t) = p + \int_0^t X(\gamma(s))\,ds$, is a fixed-point equation, and the operator $T : \gamma \mapsto p + \int_0^t X(\gamma(s))\,ds$ is a contraction on a small enough function-space ball. The contraction's unique fixed point is the integral curve. So Picard–Lindelöf — the differential-equation incarnation of the contraction mapping principle — is what makes this theorem true, with no manifold-specific input.

- **[[Thm - Fundamental Theorem on Flows]]** — the global packaging of this theorem. The Fundamental Theorem assembles the integral curves through every point into a single smooth map $\phi : \mathcal{D} \to M$, the maximal flow. The existence and uniqueness here are the *pointwise* statement; the Fundamental Theorem extends this to a *global* construction with smooth dependence on the starting point.

- **Smooth dependence on parameters in Picard–Lindelöf** — the analytical input for the smoothness statement. Picard–Lindelöf says solutions of smooth ODE systems depend smoothly on initial conditions (and on any smooth parameters in the equations). This is exactly the statement that the flow $\phi(t, p)$ is smooth in $p$, and the same Banach-space argument that gives existence also gives smooth dependence.

- **Right-invariance in Lie group flows** — for a left-invariant vector field on a Lie group, the existence interval is uniformly bounded below by translation-equivariance, so the local existence in this theorem upgrades to global existence (completeness). This is the foundation of the exponential map; see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].
