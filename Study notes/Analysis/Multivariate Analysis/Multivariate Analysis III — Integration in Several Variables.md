---
type: topic
subject: multivariate-analysis
chapter: "3.1-3.3"
title: "Multivariate Analysis III — Integration in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Notation Registry

- $\mathbb{R}^n$ — Euclidean $n$-space; points written $x = (x_1, \dots, x_n)$, with the Euclidean norm $|x| = (x_1^2 + \cdots + x_n^2)^{1/2}$
- $R = I_1 \times \cdots \times I_n$ — a **cell** (or box, or rectangle): a product of closed bounded intervals $I_\nu = [a_\nu, b_\nu]$
- $\ell(I)$ — the length of an interval $I$; $V(R) = \ell(I_1) \cdots \ell(I_n)$ — the **volume** of a cell
- $P = \{R_\alpha\}$ — a **partition** of a cell $R$ into subcells obtained by partitioning each interval factor
- $P \succ Q$ — "$P$ refines $Q$": $P$ is obtained by further subdividing $Q$
- $\operatorname{maxsize}(P) = \max_\alpha \operatorname{diam}(R_\alpha)$ — the mesh of a partition
- $\overline{I}_P(f) = \sum_\alpha (\sup_{R_\alpha} f) \, V(R_\alpha)$ — the **upper Darboux sum**
- $\underline{I}_P(f) = \sum_\alpha (\inf_{R_\alpha} f) \, V(R_\alpha)$ — the **lower Darboux sum**
- $\overline{I}(f) = \inf_P \overline{I}_P(f)$ — the **upper integral**; $\underline{I}(f) = \sup_P \underline{I}_P(f)$ — the **lower integral**
- $\int_R f \, dV$, $\int_R f \, dV(x)$ — the Riemann integral (also $dA$ when $n = 2$, or simply $dx$)
- $\mathcal{R}(R)$ — the set of Riemann integrable functions on the cell $R$
- $\chi_S$ — the indicator (characteristic) function of a set $S$, equal to $1$ on $S$ and $0$ elsewhere
- $\operatorname{cont}^+(S) = \overline{I}(\chi_S)$, $\operatorname{cont}^-(S) = \underline{I}(\chi_S)$ — upper and lower **Jordan content**
- $V(S)$ or $\mu_J(S)$ — the **Jordan measure** of a Jordan-measurable set $S$, the common value of upper and lower content
- $\partial S$ (Taylor writes $bS$) — the **topological boundary** of $S$; $\mathring{S}$ — the interior; $\overline{S}$ — the closure
- a **nil set** (content-zero set, **Jordan-null set**) — a set $\Sigma$ with $\operatorname{cont}^+(\Sigma) = 0$
- $m^*(S) = \inf\{\sum_{k \geq 1} V(R_k) : S \subseteq \bigcup_k R_k\}$ — the **Lebesgue outer measure** (countable covers allowed)
- $DG(x)$ — the Jacobian (total derivative) matrix of a map $G$ at $x$; $\det DG(x)$ — the Jacobian determinant
- $\mathrm{GL}(n, \mathbb{R})$ — the group of invertible real $n \times n$ matrices
- a **$C^1$ diffeomorphism** $G : O \to \Omega$ — a continuously differentiable bijection between open sets with continuously differentiable inverse
- $\Gamma(s) = \int_0^\infty t^{s-1} e^{-t} \, dt$ — Euler's gamma function; $\Gamma(n+1) = n!$, $\Gamma(\tfrac12) = \sqrt{\pi}$

---

# Motivation

In one variable, integration is a story about area under a graph, and the Riemann integral is built by chopping the domain interval into small pieces, estimating the function from above and below on each piece, and squeezing. Almost everything in this topic is that story told again in $\mathbb{R}^n$ — but the retelling is not a formality, because two things that were invisible in one dimension become the entire substance of the subject.

The first is the question of **which sets you are even allowed to integrate over**. In one variable you integrate over an interval, and an interval is an interval; there is nothing to discuss. In $\mathbb{R}^n$ you want to integrate over a disk, a ball, a triangle, the region between two surfaces — and none of these is a box. You cannot partition a disk into subdisks. The fix is to put the region inside a big box, extend the function by zero outside, and integrate that. But the extended function has a jump discontinuity all along the *boundary* of the region, and now the integral exists only if that boundary is negligible. This is what **Jordan measure** is for: it measures sets, and it declares a set "integrable as a domain" — Jordan measurable — exactly when its boundary has content zero. The single most important fact in §3.1, the **Lebesgue criterion**, makes this precise for functions too: a bounded function is Riemann integrable if and only if its set of discontinuities is small in the measure-theoretic sense. Integrability is a statement about the *size of the bad set*.

The second is the question of **how you actually compute**. A genuine $n$-fold integral, defined as a limit of sums over an $n$-dimensional grid, is not something you can evaluate by hand. Two theorems rescue computation. **Fubini's theorem** says that an $n$-dimensional integral can be unwound into $n$ nested one-dimensional integrals, done one variable at a time — this is the only reason multiple integrals are tractable at all, and it is what lets you integrate over the region "between two graphs". **Differentiation under the integral sign** is its close cousin: when an integral depends on a parameter, you can often compute its derivative by differentiating inside, which turns hard integrals into solvable differential equations. And the **change of variables formula** is the multidimensional substitution rule: it says that bending the domain by a diffeomorphism $G$ multiplies the volume element by the Jacobian determinant $|\det DG|$. The Jacobian is not a fudge factor — it is exactly the local volume-distortion of $G$, and the formula is the precise statement that integration sees only how $G$ stretches space. Polar, cylindrical, and spherical coordinates are the famous instances, and they turn otherwise impossible integrals — the Gaussian, the volume of a ball — into routine computations.

So this topic answers two questions that one-variable calculus never had to ask: *what is a legitimate region*, and *how do you reduce an $n$-dimensional computation to one-dimensional ones*. The answers — Jordan measure, the Lebesgue criterion, Fubini, change of variables — are the working machinery of every later subject that integrates, from probability to **differential forms** to **special relativity**.

---

# Concept Map

## §3.1 Jordan Measure and the Riemann Integral

- **[[Def - Jordan Measure]]**
	- The **Jordan content** of a bounded set $S \subseteq \mathbb{R}^n$ is built from finite covers and finite interior packings by cells: the **upper content** $\operatorname{cont}^+(S)$ is the infimum of total cell-volume in a finite cover, the **lower content** $\operatorname{cont}^-(S)$ is the supremum over finite packings, and $S$ is **Jordan measurable** when the two agree. Equivalently, $S$ is Jordan measurable if and only if its boundary $\partial S$ is a **nil set** (has content zero). The disk, the ball, and any region bounded by finitely many continuous graphs are Jordan measurable; the rationals in a box are not. Jordan measure is finitely additive but not countably additive, which is exactly the gap that **Lebesgue measure** later closes.

- **[[Def - The Riemann Integral in Several Variables]]**
	- For a bounded $f : R \to \mathbb{R}$ on a cell $R$, partition $R$ into subcells, form the **upper Darboux sum** $\overline{I}_P(f) = \sum_\alpha (\sup_{R_\alpha} f) V(R_\alpha)$ and the **lower Darboux sum** $\underline{I}_P(f)$; $f$ is **Riemann integrable** when the upper integral $\overline{I}(f) = \inf_P \overline{I}_P(f)$ equals the lower integral $\underline{I}(f) = \sup_P \underline{I}_P(f)$, and the common value is $\int_R f \, dV$. The integral over a Jordan-measurable region $S$ is defined by extending $f$ by zero, $\int_S f = \int_R \chi_S f$. The integral is linear, monotone, and (by the multidimensional Darboux theorem) equals the limit of Riemann sums for any partition sequence with mesh tending to zero.

- **[[Thm - The Lebesgue Criterion for Riemann Integrability]]**
	- A bounded function $f : R \to \mathbb{R}$ on a cell is Riemann integrable if and only if its set of discontinuities has **Lebesgue outer measure zero** — coverable by countably many cells of arbitrarily small total volume. This is the sharp characterization: continuity is sufficient, a content-zero (nil) discontinuity set is sufficient, but the exact dividing line is the *outer-measure-zero* condition, which is genuinely weaker because it allows countable covers. It is the bridge between the Riemann and Lebesgue theories: the criterion is stated in Lebesgue's language even though the integral is Riemann's, and it explains precisely which functions Riemann integration can and cannot handle.

- **[[Ex - A Jordan-measurable region]]**
	- Show the closed unit disk $\{x^2 + y^2 \leq 1\}$ is Jordan measurable by proving its boundary circle has content zero. (⭐)

- **[[Ex - A bounded set that is not Jordan measurable]]**
	- Show that $\mathbb{Q}^n \cap [0,1]^n$ — the rational points of the unit cube — has upper content $1$ and lower content $0$, hence is not Jordan measurable. (⭐⭐)

- **[[Ex - Integrability of a function with a discontinuity set]]**
	- Decide Riemann integrability of functions with prescribed discontinuity sets: a function discontinuous on a circle (integrable), and the indicator of the rationals (not integrable), using the Lebesgue criterion both ways. (⭐⭐)

> [!note] Exercise Index — §3.1 Jordan Measure and the Riemann Integral
> [[Exercise Index - §3.1 Jordan Measure and the Riemann Integral]]

## §3.2 Fubini's Theorem and Iterated Integrals

- **[[Thm - Fubini's Theorem]]**
	- For an integrable function on a product of cells, the multiple integral equals the **iterated integral**: $\int_{A \times B} f \, dV = \int_A \big( \int_B f(x,y) \, dy \big) dx$, and one may integrate in either order. For a region of the form $\Omega = \{(x,y) : x \in \Sigma, \ g_0(x) \leq y \leq g_1(x)\}$ between two continuous graphs over a Jordan-measurable base $\Sigma$, the integral of a continuous $f$ reduces to $\int_\Sigma \int_{g_0(x)}^{g_1(x)} f(x,y) \, dy \, dx$. Fubini is what makes multiple integrals computable: it converts one $n$-dimensional limit-of-sums into $n$ nested one-dimensional integrals. The hypothesis — integrability on the product, or boundedness with a nil discontinuity set — cannot be dropped.

- **[[Thm - Differentiation Under the Integral Sign]]**
	- If $F(t) = \int_R f(x, t) \, dx$ and the partial derivative $\partial f / \partial t$ exists and is continuous (or is dominated by a fixed integrable function), then $F$ is differentiable and $F'(t) = \int_R \frac{\partial f}{\partial t}(x,t) \, dx$ — the derivative passes inside the integral. With variable limits $a(t), b(t)$, the **Leibniz rule** adds boundary terms $f(b(t),t) b'(t) - f(a(t),t) a'(t)$. This is the parameter-integral cousin of Fubini (both are statements that two limit operations commute), and it is the engine of the "Feynman trick": introduce a parameter, differentiate to get a tractable differential equation for $F$, solve, and specialize.

- **[[Ex - An iterated integral over a non-rectangular region]]**
	- Integrate $f(x,y) = xy$ over the triangle with vertices $(0,0), (1,0), (1,1)$ by setting up the iterated integral with variable inner limits. (⭐)

- **[[Ex - Reversing the order of integration]]**
	- Evaluate $\int_0^1 \int_x^1 e^{y^2} \, dy \, dx$ — impossible in the given order — by swapping to $dx \, dy$ via a careful redescription of the region. (⭐⭐)

- **[[Ex - A parameter integral by differentiation under the integral sign]]**
	- Compute $\int_0^\infty \frac{e^{-ax} - e^{-bx}}{x} \, dx = \ln(b/a)$ by differentiating with respect to a parameter to collapse the integrand. (⭐⭐)

> [!note] Exercise Index — §3.2 Fubini's Theorem and Iterated Integrals
> [[Exercise Index - §3.2 Fubini's Theorem and Iterated Integrals]]

## §3.3 The Change of Variables Formula

- **[[Thm - The Change of Variables Formula]]**
	- If $G : O \to \Omega$ is a $C^1$ diffeomorphism between open sets of $\mathbb{R}^n$ and $f$ is integrable on $\Omega$, then $\int_\Omega f(y) \, dV(y) = \int_O f(G(x)) \, |\det DG(x)| \, dV(x)$. The Jacobian determinant $|\det DG(x)|$ is the local volume-distortion factor of $G$: it is what a small box at $x$ has its volume multiplied by under $G$. The linear case ($G = A$, a matrix) is $V(A(S)) = |\det A| \, V(S)$; the general formula is this linear fact applied infinitesimally and assembled by integration. Polar, cylindrical, and spherical coordinates are the standard instances, and the diffeomorphism hypothesis is essential — it is what guarantees the formula counts each point of $\Omega$ exactly once.

- **[[Ex - The Gaussian integral via polar coordinates]]**
	- Evaluate $\int_{-\infty}^\infty e^{-x^2} \, dx = \sqrt{\pi}$ by squaring it into a double integral and changing to polar coordinates. (⭐)

- **[[Ex - The volume of the n-dimensional ball]]**
	- Derive $V_n = \pi^{n/2} / \Gamma(n/2 + 1)$ for the volume of the unit ball in $\mathbb{R}^n$, via a slicing recursion (Fubini) cross-checked against the Gaussian integral. (⭐⭐)

- **[[Ex - A nonlinear change of variables]]**
	- Evaluate $\iint_R (x+y) \, dx \, dy$ over a parallelogram-image region using the substitution $u = x+y$, $v = x-y$, computing the Jacobian and the new region of integration. (⭐⭐)

> [!tip] Unlocked: Integration of Differential Forms *(from Multivariate Analysis IV)*
> Once you can integrate over Jordan-measurable regions and you understand that the change of variables formula transports an integral by the Jacobian, you can define the **integral of a differential $k$-form** over an oriented region. The form $f \, dx_1 \wedge \cdots \wedge dx_n$ integrates exactly so that the [[Def - Pullback of a Differential Form|pullback]] under $G$ reproduces the change of variables formula automatically — the wedge product is built precisely so that $\det DG$ appears on its own. See [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

> [!tip] Unlocked: Lebesgue Integration *(from Measure Theory)*
> Jordan measure is finitely additive but fails to be countably additive, and the Riemann integral cannot interchange limits with integration without uniform convergence. **Lebesgue measure** and the **Lebesgue integral** repair both defects; the Lebesgue criterion above already shows that the natural language for integrability is measure-theoretic. See [[Measure Theory I — §1 Measure Spaces]] and [[Measure Theory II — §2 Integration]].

> [!note] Exercise Index — §3.3 The Change of Variables Formula
> [[Exercise Index - §3.3 The Change of Variables Formula]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises of multidimensional integration chase a small number of recurring goals. The most basic is to **decide integrability** — given a function or a region, is the integral defined at all? In one variable this was rarely in doubt; here it is a genuine question, and the answer is always routed through the size of a bad set (the discontinuity set of a function, or the boundary of a region). A second target is to **evaluate an integral exactly** — to produce a closed-form number or formula — and this is almost never done from the definition; it is done by *reducing* the integral, either to iterated one-dimensional integrals via Fubini or to a simpler integral via a change of variables. A third target is to **establish a measure or volume**: the volume of a ball, an ellipsoid, a region between surfaces. A fourth, more structural, is to **justify an interchange of two limiting operations** — swapping the order of integration, or moving a derivative inside an integral — where the content of the problem is precisely checking the hypothesis that licenses the swap. Underlying all four is a single game: an $n$-dimensional integral is intractable as stated, so every problem is the project of *transforming it into something one-dimensional and computable* while certifying that the transformation is legal.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **A continuity hypothesis** on the integrand is the richest source: continuous functions are integrable, and the Lebesgue criterion extends this to functions whose discontinuities form a nil set. **A region described by inequalities or by graphs** is a source for Fubini: a region $\{g_0(x) \leq y \leq g_1(x)\}$ is built to be unwound into an iterated integral, and recognizing this shape is half the battle. **A diffeomorphism, or a coordinate system, is given or can be built** — polar, spherical, linear — and this is the source that triggers change of variables; the assumption to verify is that the map is a $C^1$ bijection with nonvanishing Jacobian. **An integral depends on a parameter**, which is the source for differentiation under the integral sign. **A symmetry of the integrand or domain** — rotational symmetry, a product structure $e^{-|x|^2} = \prod e^{-x_i^2}$ — is a source that suggests which coordinate change or which factorization to use. The recurring move is to route a source to a target: a graph-described region routes through Fubini to an evaluation; a symmetry routes through change of variables to a collapse; a parameter routes through Leibniz to a differential equation. The [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|Problem-Solving Strategy]] section makes these routes explicit.

---

# Legal Operations

These are the moves almost every problem in this topic is assembled from. When stuck, scan the list. Everything is self-contained: a reader with no background should follow each operation from its description.

**Legal operations:**

1. **Extend a function by zero off a region, then integrate over a box.** To integrate $f$ over a non-box region $S$, define $\tilde f = f$ on $S$ and $\tilde f = 0$ outside, place $S$ in a cell $R$, and set $\int_S f := \int_R \tilde f \, dV$. This is the *only* way the integral over a disk, a ball, or a triangle is even defined — see [[Def - The Riemann Integral in Several Variables]]. The catch, and the trigger for the next operation, is that $\tilde f$ has discontinuities along $\partial S$, so this is legal precisely when $\partial S$ is small.

2. **Certify integrability by measuring the discontinuity set.** Whenever you must show an integral *exists*, do not estimate Darboux sums by hand — instead identify where the integrand is discontinuous and show that set is negligible. If the discontinuity set is a nil set (content zero), or more sharply has Lebesgue outer measure zero, the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]] delivers integrability. The trigger is any "show $f$ is integrable" or "show $S$ is Jordan measurable" request: for the region, the discontinuity set of $\chi_S$ is exactly $\partial S$.

3. **Show a set is nil by covering it with continuous graphs.** A content-zero set is one coverable by finitely many cells of arbitrarily small total volume. The workhorse fact is that the graph of a continuous function over a closed bounded base is nil — so any boundary assembled from finitely many such graphs (a circle, a sphere, the boundary of a region between graphs) is nil. The trigger: you need "$\partial S$ has content zero" and $\partial S$ is visibly a finite union of graphs.

4. **Reduce a multiple integral to iterated single integrals (Fubini).** Replace $\int_{A \times B} f$ by $\int_A (\int_B f \, dy) \, dx$, integrating one variable at a time and treating the others as constants. For a region between two graphs, the inner limits become functions of the outer variables. This is the primary computational tool; see [[Thm - Fubini's Theorem]]. The trigger is *any* request to actually evaluate a multiple integral.

5. **Reverse the order of integration.** Fubini permits either order. When the inner integral is intractable in the given order, redescribe the region from the other variable's point of view and integrate the other way. The trigger is an inner integral with no elementary antiderivative (the classic $\int e^{y^2} \, dy$); the work is entirely in re-reading the region's inequalities.

6. **Change variables by a diffeomorphism, inserting the Jacobian.** Substitute $y = G(x)$ and replace $dV(y)$ by $|\det DG(x)| \, dV(x)$, also rewriting the region of integration as $G^{-1}(\Omega)$. See [[Thm - The Change of Variables Formula]]. The trigger is a domain or integrand with a symmetry that a coordinate system respects — radial symmetry calls for polar or spherical coordinates, a linear deformation calls for a matrix substitution.

7. **Use a linear change of variables to compute volumes.** A special case worth isolating: for an invertible matrix $A$, $V(A(S)) = |\det A| \, V(S)$. This evaluates the volume of any ellipsoid (an image of a ball) or parallelepiped (an image of a cube) in one line. The trigger is a region that is the linear image of a region whose volume you already know.

8. **Differentiate under the integral sign to introduce a differential equation.** When an integral $F(t) = \int f(x,t) \, dx$ resists direct evaluation, differentiate in the parameter $t$: $F'(t) = \int \partial_t f \, dx$, which is often far simpler. Solve the resulting differential equation for $F$ and fix the constant by a known value of $F$. See [[Thm - Differentiation Under the Integral Sign]]. The trigger is an integral that *contains a parameter*, or into which a parameter can be artificially inserted.

9. **Squeeze with simpler functions (the approximation operation).** Trap a hard $f$ between functions $\psi_\nu \leq f \leq \varphi_\nu$ that are piecewise constant or continuous, with $\int(\varphi_\nu - \psi_\nu) \to 0$; then $f$ is integrable and its integral is the common limit. This is the engine inside the proofs of Fubini and change of variables, and it is directly useful whenever you must integrate a function or region built from simpler approximable pieces. The trigger is a function that is "almost" piecewise constant or continuous.

**Illegal but tempting operations:**

> [!warning] 1. Swapping the order of integration without an integrability hypothesis
> Fubini's theorem licenses $\int\int f \, dy \, dx = \int\int f \, dx \, dy$ *only when $f$ is integrable on the product* (or, in the Lebesgue setting, when $\int\int |f| < \infty$). It is tempting to swap orders mechanically, but for a non-integrable $f$ the two iterated integrals can both exist and *disagree*. The standard counterexample is $f(x,y) = (x^2 - y^2)/(x^2 + y^2)^2$ on $(0,1)^2$: integrating $dy$ then $dx$ gives $-\pi/4$, the other order gives $+\pi/4$. The function is not integrable (it is unbounded near the origin and $\int\int|f| = \infty$), and that failure is exactly what permits the contradiction. Always confirm integrability — via continuity, the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]], or absolute integrability — before swapping.

> [!warning] 2. Applying change of variables when $G$ is not injective
> The [[Thm - The Change of Variables Formula|change of variables formula]] requires $G$ to be a diffeomorphism — in particular *injective*. It is tempting to use polar coordinates $G(r,\theta) = (r\cos\theta, r\sin\theta)$ on the full closed rectangle $[0,\rho] \times [0,2\pi]$, but $G$ is not injective there: every point on the segment $\theta = 0$ is identified with the corresponding point on $\theta = 2\pi$, and the entire edge $r = 0$ collapses to the origin. If $G$ folds the domain, the formula overcounts. The repair is that the failure set has content zero: $G$ *is* a diffeomorphism on the open rectangle $(0,\rho) \times (0,2\pi)$, the omitted boundary is nil, so the integral is unchanged — but this argument must be made, not assumed.

> [!warning] 3. Differentiating under the integral sign with no domination
> Moving $\frac{d}{dt}$ inside $\int f(x,t) \, dx$ is an interchange of two limits — a derivative and an integral — and like all such interchanges it can fail. It is tempting to differentiate inside automatically. But without a hypothesis controlling $\partial_t f$ uniformly — continuity on a compact parameter range, or a fixed integrable dominating function $|\partial_t f| \leq M(x)$ — the derivative of the integral need not equal the integral of the derivative. Mass can escape: consider $f(x,t) = t^3/(t^2 + x^2)^2$-type bumps on $(0,\infty)$ that concentrate as $t \to 0$. The [[Thm - Differentiation Under the Integral Sign|Leibniz rule]] is valid exactly when the differentiated integrand is dominated.

> [!warning] 4. Treating Jordan content as countably additive
> Jordan measure is *finitely* additive: the content of a finite disjoint union is the sum of the contents. It is tempting to extend this to countable unions, but it fails. Each rational point in $[0,1]^n$ is a single point of content zero, yet their countable union $\mathbb{Q}^n \cap [0,1]^n$ is not Jordan measurable at all (upper content $1$, lower content $0$). Countable additivity is precisely the axiom Jordan measure lacks and **Lebesgue measure** supplies; this gap is the reason measure theory exists. See the [[Multivariate Analysis III — Integration in Several Variables#Bridges|Bridges]] section.

---

# Problem-Solving Strategy

The problems of this topic are won at the moment you classify which of two questions you are facing — *does this integral exist?* or *what is its value?* — because the two route to entirely different toolkits.

If the problem **asks whether an integral exists**, or whether a set is a legitimate domain, you are in an integrability problem, and the instrument is never the definition. Estimating Darboux sums directly is a trap; it is slow and it teaches nothing. Instead, locate the *bad set* and measure it. For a function, the bad set is its set of discontinuities, and by the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]] the function is Riemann integrable if and only if that set has Lebesgue outer measure zero. For a region $S$, the question "is $S$ Jordan measurable" is the question "is $\chi_S$ integrable", and the discontinuity set of $\chi_S$ is exactly the boundary $\partial S$ — so $S$ is Jordan measurable precisely when $\partial S$ has content zero. The recurring sub-skill is therefore proving a set is small, and the standard route is to exhibit it as a finite union of graphs of continuous functions, each of which is nil. A circle is two graphs; a sphere is two graphs; the boundary of a region between two surfaces is built from graphs. Once the bad set is recognized as such a union, integrability is immediate.

If the problem **asks for the value** of a multiple integral, you are in an evaluation problem, and the strategy is always *reduction to one dimension*. There are two reduction engines, and the choice between them is dictated by the shape of the domain and the symmetry of the integrand. The first engine is [[Thm - Fubini's Theorem|Fubini's theorem]]: if the region can be described as lying between two graphs — $g_0(x) \leq y \leq g_1(x)$ over a base $\Sigma$ — then the integral unwinds into an iterated integral with the inner limits being those graphs. The single most common difficulty here is that the iterated integral is *intractable in the order you first wrote it*, and the fix is to reverse the order: redescribe the same region from the other variable's standpoint and integrate the other way. This is why a region must be understood as a *set of inequalities you can solve for either variable*, not as a fixed nested integral. The second engine is the [[Thm - The Change of Variables Formula|change of variables formula]]: if the integrand or the domain has a symmetry — radial symmetry of $e^{-|x|^2}$, the spherical shape of a ball, a linear shear — choose the coordinate system that respects it (polar, spherical, or a matrix substitution), and the symmetry collapses the integral. The decisive check before invoking the formula is that the chosen map is a genuine $C^1$ diffeomorphism; coordinate maps like polar coordinates fail injectivity on a boundary, and one must note that the failure set is nil before proceeding. A third, lighter tool belongs here too: if the integral carries a parameter, [[Thm - Differentiation Under the Integral Sign|differentiation under the integral sign]] converts it into a differential equation for the parameter-dependence, which is often solvable when the integral itself is not.

A meta-strategy threads through both cases: **the hard part is almost always certifying a hypothesis, not performing a manipulation.** Swapping integration order, changing variables, differentiating inside — each is a one-line move, but each is valid only under a condition (integrability, the diffeomorphism property, domination of the differentiated integrand), and a problem that looks like a computation is often really a problem of checking that condition. The reason this matters beyond exam technique is the reader's stated concern about far-out-of-distribution generalization: these hypotheses are not decoration, they are the exact boundary between a true statement and a false one. The counterexamples in the Legal Operations section — the order-swap that gives $\pm\pi/4$, the non-injective polar map that overcounts — are not pathologies to be memorized but the precise demonstrations of *what the hypothesis is buying*. When applying any of these theorems in an unfamiliar setting, the safe procedure is to name the hypothesis explicitly and verify it, because the manipulation will be correct exactly when the hypothesis holds.

---

# Most Reusable Properties

- **[[Thm - The Lebesgue Criterion for Riemann Integrability|The Lebesgue Criterion]]**: $f$ Riemann integrable $\iff$ its discontinuity set has outer measure zero. This is the most reusable single fact in §3.1 because it replaces an infinite verification (no partition can be checked one at a time) with a finite, geometric one: find where $f$ jumps, and show that set is small. Reach for it whenever a problem asks "is this integrable" — including the disguised version "is this region Jordan measurable", where the discontinuity set is the boundary. It is also the conceptual bridge to measure theory: it is stated in Lebesgue's language, and it is the precise diagnosis of which functions Riemann integration handles.

- **[[Thm - Fubini's Theorem|Fubini's Theorem]]**: a multiple integral equals an iterated integral, in either order. This is the workhorse of *computation*. The recognizable setup is any request to evaluate $\int\int f$, and the typical pattern is to describe the region between graphs, write the iterated integral, and — if stuck — reverse the order. It combines with change of variables (do the substitution, then iterate) and with differentiation under the integral sign (which is itself a Fubini-type interchange). Recognize its applicability the instant a domain can be sliced: for every fixed value of one variable, the cross-section in the others is an interval or a known set.

- **[[Thm - The Change of Variables Formula|The Change of Variables Formula]]**: $\int_\Omega f(y) \, dy = \int_O f(G(x)) \, |\det DG(x)| \, dx$. This is the tool for *exploiting symmetry*. Its typical use is to match a coordinate system to the geometry — polar for disks, spherical for balls, linear for parallelepipeds and ellipsoids — so that the transformed integrand or region becomes a product or a simple shape. The Jacobian $|\det DG|$ is the reusable concept: it is the local volume-distortion of $G$, the same number whether you think of it analytically (a determinant of partials) or geometrically (the volume of the image of a unit cube). Combine it with Fubini to finish almost any concrete evaluation.

- **The graph of a continuous function is a nil set**: $\{(x, g(x)) : x \in \Sigma\}$ has content zero for continuous $g$ on a closed bounded base. This humble fact is the universal certificate of smallness. Its typical use is to prove a boundary is nil — and therefore a region is Jordan measurable, and therefore the integral over it is defined — by recognizing the boundary as a finite union of graphs. It is what makes "ordinary-looking regions" (disks, balls, regions between surfaces) legitimate domains of integration in the first place.

- **The Jacobian as local volume-distortion**: $|\det DG(x)|$ is the factor by which $G$ multiplies the volume of an infinitesimal box at $x$; for a linear map $A$, exactly, $V(A(S)) = |\det A| V(S)$. This is reusable as a *conceptual anchor*, not just a formula: it tells you, before any computation, that integration is blind to everything about $G$ except how it stretches space, and it explains why the determinant — and not some other combination of the partials — is the right factor. It is the seed from which the change of variables formula, and later the entire theory of integration of differential forms, grows.

---

# Bridges

1. **Measure theory — Jordan measure is the finitely-additive precursor of Lebesgue measure.** Jordan measure and Lebesgue measure are built the same way — cover a set by cells and infimize total volume — with one decisive difference: Jordan content (see [[Def - Jordan Measure]]) allows only *finite* covers, while the [[Def - Lebesgue Measure|Lebesgue outer measure]] $m^*(S) = \inf\{\sum_{k\geq 1} V(R_k) : S \subseteq \bigcup_k R_k\}$ allows *countable* covers. This single change upgrades finite additivity to **countable additivity**, the defining axiom of a [[Def - Measure and Measure Space|measure]] (see [[Measure Theory I — §1 Measure Spaces]]). The gap is visible and concrete: $\mathbb{Q}^n \cap [0,1]^n$ is not Jordan measurable, because no finite cover of cells of small total volume reaches every rational, yet it is Lebesgue measurable with measure zero, because a countable cover can. Two precise correspondences make the bridge exact. First, a bounded set $S$ is **Jordan measurable if and only if its boundary $\partial S$ is a Lebesgue-null set** — Jordan measurability is a measure-theoretic condition on the boundary. Second, a bounded function is **Riemann integrable if and only if its discontinuity set is Lebesgue-null**, which is exactly the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]]: Riemann integrability is diagnosed in the language of Lebesgue measure even though the Riemann integral predates it. When $S$ is Jordan measurable, its Jordan measure equals its Lebesgue measure, and when $f$ is Riemann integrable, its Riemann integral equals its [[Measure Theory II — §2 Integration|Lebesgue integral]] — so the Lebesgue theory is a genuine extension, agreeing with the Riemann theory wherever the latter is defined and succeeding (interchange of limits, integration of badly discontinuous functions) where it fails. The notion of a **null set** that organizes all of this is the same [[Def - Null Set and Completion|null set]] of measure theory.

2. **Differential forms — change of variables is pullback, and the Jacobian is built in.** The [[Thm - The Change of Variables Formula|change of variables formula]] looks like it carries an awkward correction factor $|\det DG|$. The theory of [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|differential forms]] reveals that the factor is not a correction at all — it is automatic. An $n$-form $\omega = f \, dy_1 \wedge \cdots \wedge dy_n$ is an object designed to be integrated over an oriented $n$-dimensional region, and its [[Def - Pullback of a Differential Form|pullback]] $G^*\omega$ under a map $G$ satisfies $G^*(dy_1 \wedge \cdots \wedge dy_n) = \det DG \cdot dx_1 \wedge \cdots \wedge dx_n$ — the determinant appears *because the wedge product is antisymmetric and multilinear*, which is exactly the algebra of how volumes transform. So the change of variables formula is the single statement $\int_\Omega \omega = \int_O G^*\omega$, with the Jacobian emerging from the [[Def - The Wedge Product|wedge product]] rather than being inserted by hand. The absolute value $|\det DG|$ in this topic's formula is the price of working with unoriented regions; differential forms keep the sign and thereby keep track of [[Def - Orientation and the Integral of a Form|orientation]], which is what makes Stokes' theorem possible.

3. **Probability theory — integration over regions is computing probabilities.** A continuous probability distribution on $\mathbb{R}^n$ is given by a density $p(x) \geq 0$ with $\int_{\mathbb{R}^n} p = 1$, and the probability that the random point lands in a region $S$ is the integral $\int_S p \, dV$. Every tool of this topic is therefore a tool of probability: Fubini's theorem is the statement that a joint distribution can be integrated one coordinate at a time, which is how **marginal distributions** are computed; the change of variables formula is exactly the rule for the **density of a transformed random variable** $Y = G(X)$, where the new density picks up a factor $|\det DG^{-1}|$; and the requirement that $S$ be Jordan measurable is why probabilities are assigned to "events" — measurable sets — and not arbitrary subsets. The Gaussian integral $\int e^{-|x|^2} = \pi^{n/2}$, computed in this topic by polar coordinates, is precisely the normalization constant of the multivariate normal distribution.

4. **Special relativity — invariant integration on Minkowski space.** Integration over regions of $\mathbb{R}^n$ underlies the formulation of physical quantities as integrals over spacetime. In **special relativity** (see [[Special Relativity I — Lorentz Transformations and Minkowski Space]]), one integrates densities — of charge, of energy-momentum — over four-dimensional regions, and the question of which quantities are physically meaningful is the question of which integrals are *invariant under Lorentz transformations*. A Lorentz transformation is a linear map $\Lambda$ with $|\det \Lambda| = 1$, so by the linear change of variables formula $V(\Lambda(S)) = |\det \Lambda| V(S) = V(S)$: four-dimensional volume is Lorentz-invariant, which is the integration-theoretic content of the statement that the spacetime volume element $dt \, dx \, dy \, dz$ is an invariant. The change of variables formula is thus the precise reason certain spacetime integrals are observer-independent.

---

# Insights

**The unifying frame: integration is the project of reducing an $n$-dimensional problem to one-dimensional ones, and every theorem in this topic is a license to do so.** A multiple integral, defined as a limit of sums over an $n$-dimensional grid, is unevaluable as it stands — there is no procedure for it. The whole topic is the collection of legal ways to dismantle it. Fubini dismantles it into nested single integrals. Change of variables dismantles it by deforming the domain into a shape — a box, a product — that Fubini can then handle. Differentiation under the integral sign dismantles a *family* of integrals by converting it into an ordinary differential equation in one variable. Even the integrability theory serves this frame: the Lebesgue criterion tells you when the dismantling is legitimate, by certifying that the bad set is too small to obstruct it. Read this way, the topic has one idea and three implementations, and a problem is solved by recognizing which implementation the domain and integrand are asking for.

**The true name of integrability is "the bad set is negligible".** The official definition of Riemann integrability — upper integral equals lower integral — is the right thing to *state* but the wrong thing to *think*, because it quantifies over all partitions and can never be checked directly. The operational characterization, the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]], is that $f$ is integrable exactly when its set of discontinuities has measure zero. This is what you actually reach for, and it reframes integrability entirely: a function fails to be integrable not because it is "too wild" in some vague sense, but because it is discontinuous on a set that is genuinely large. The indicator of the rationals fails because it is discontinuous *everywhere*; a function with a jump along a single curve succeeds because a curve is negligible. Integrability is a verdict on the size of one specific set, and once you internalize this, the entire integrability theory becomes a single question asked of different bad sets.

**The Jacobian is volume-distortion, and this is why a determinant — and nothing else — appears.** The change of variables formula could superficially carry any number of correction factors; that it carries exactly $|\det DG|$ is forced, and the reason is geometric. The derivative $DG(x)$ is the best linear approximation to $G$ near $x$, and a linear map $A$ multiplies every volume by exactly $|\det A|$ — this is the linear case of the formula, and it is *the definition* of the determinant up to sign. So $|\det DG(x)|$ is the factor by which an infinitesimal box at $x$ has its volume scaled by $G$, and the change of variables formula is nothing but this infinitesimal statement integrated up. The lesson generalizes: whenever a transformation acts on an integral, the correct correction factor is its local volume-distortion, and the determinant is the algebraic name of that geometric quantity. This is also the seed of differential forms, where the antisymmetry of the wedge product *is* the algebra of oriented volume.

**Hypotheses are the boundary between true and false, not technical clutter — and the counterexamples are the proof.** A recurring temptation, especially when generalizing a familiar technique to an unfamiliar setting, is to treat the hypotheses of Fubini, change of variables, and the Leibniz rule as fine print. They are not. Each theorem is an interchange of two limiting operations, and each has an explicit counterexample showing that without the hypothesis the conclusion is *false*: the function $(x^2-y^2)/(x^2+y^2)^2$ has both iterated integrals existing and unequal because it is not integrable; polar coordinates on a closed rectangle overcount because the map is not injective; a concentrating bump shows that differentiating inside an integral fails without domination. The right mental model is that each hypothesis names exactly the failure mode it rules out — integrability rules out the order-swap discrepancy, injectivity rules out overcounting, domination rules out escaping mass. When you apply one of these theorems in a context far from where you learned it, the reliable procedure is not to trust the manipulation but to name the hypothesis and check it; the manipulation is correct precisely on the set where the hypothesis holds, and the counterexamples mark its boundary.
