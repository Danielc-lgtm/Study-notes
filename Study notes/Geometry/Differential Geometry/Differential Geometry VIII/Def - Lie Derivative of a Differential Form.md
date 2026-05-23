---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Vector Field on a Manifold"
  - "Def - Flow of a Vector Field"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Def - Lie Derivative of a Vector Field"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. $X$ is a smooth vector field on $M$ with flow $\phi^X_t : U_t \to M$ ($U_t \subseteq M$ an appropriate open set; flow is defined on an open subset of $\mathbb{R} \times M$). $\omega \in \Omega^k(M)$ is a smooth differential $k$-form. The Lie derivative is $\mathcal{L}_X\omega \in \Omega^k(M)$ — same degree as $\omega$. The full registry is on [[Differential Geometry VIII — Differential Forms]].

---

# Axiom Motivation

The Lie derivative on differential forms continues the Lie derivative on vector fields ([[Def - Lie Derivative of a Vector Field]]) and on general tensor fields with one structural twist: **for differential forms, the pullback $\phi_t^*\omega$ is well-defined whether or not the flow is a diffeomorphism on the whole region of interest**, so the Lie derivative can be defined globally with cleaner regularity than for vector fields. This is one of the structural advantages of forms.

The geometric motivation is uniform with the Lie derivative in other contexts: we want to know how a geometric quantity changes when it is *dragged* along by the flow of a vector field. For a vector field $Y$, the Lie derivative $\mathcal{L}_X Y$ records how $Y$ deviates from being invariant under $\phi^X_t$. For a function $f$, $\mathcal{L}_X f = X(f)$ is the directional derivative. For a form $\omega$, the natural construction is to pull $\omega$ back by $\phi^X_t$ (which moves the form from time-$t$ position back to time-$0$ position, comparable with the original $\omega$) and differentiate in $t$ at $t = 0$. The result is the *infinitesimal pullback* — the rate at which the form changes in the eyes of the flow.

The pullback is the right operation (rather than, say, pushforward) for two reasons. **Structural:** as discussed at length in [[Def - Pullback of a Differential Form on a Manifold]], pullback is the universally-defined natural operation on forms; pushforward requires invertibility. **Geometric:** pulling $\omega$ from its position at time $t$ back to time $0$ asks "how would $\omega$ look at the starting point if I undid the flow?" — the natural question for measuring change.

The definition is then
$$\mathcal{L}_X\omega = \frac{d}{dt}\bigg|_{t=0}(\phi^X_t)^*\omega,$$
with the understanding that the derivative exists because $\omega$ is smooth, the flow $\phi^X_t$ is smooth in $(t, p)$, and the pullback is constructed from smooth ingredients.

**The miracle, and the actual reason this definition is useful, is Cartan's magic formula** $\mathcal{L}_X = d\iota_X + \iota_X d$. It says the geometric definition above equals an algebraic composite of $d$ and $\iota_X$ — two static, chart-independent operations that involve no flow. The proof is by induction on degree (functions, then $1$-forms of the form $u\,dv$, then general forms by Leibniz), and the result is that *one never actually needs the flow definition for computation*. In practice the formula above is the definition that *justifies* calling $\mathcal{L}_X$ "the Lie derivative" — making it match the flow concept — while Cartan's magic formula is the working tool.

**What breaks if we omit the pullback and just plug $\phi^X_t(p)$ into $\omega$?** Then we would not be comparing $\omega$ at different points; we would just be evaluating $\omega$ at the moving point $\phi^X_t(p)$, getting a function (the value of $\omega$ at that point applied to some tangent vectors) whose derivative is meaningful but is not a form. The pullback is what makes the derivative produce a form back, rather than just a scalar at $p$.

**Why the requirement that $X$ be smooth?** Because the flow $\phi^X_t$ is only smooth when $X$ is smooth, and the differentiation in $t$ requires smoothness for the result to be a smooth form. Continuous vector fields have flows but not smooth ones; for general theory one fixes $C^\infty$.

**What if the flow is not complete?** The Lie derivative is still well-defined: for each compact set $K \subset M$ there is $\epsilon > 0$ such that $\phi^X_t$ is defined on $K$ for $|t| < \epsilon$, and the derivative at $t = 0$ uses only this small-time behavior. Completeness of the flow is not required.

**Why is the Lie derivative not $C^\infty(M)$-linear in $X$?** Because the flow of $fX$ for a function $f$ is *not* simply $\phi^{X}_{f t}$ — that would only be true if $f$ is constant. The dependence on $X$ involves derivatives of $X$ in a non-trivial way (see Cartan's formula: $\iota_X$ is $C^\infty$-linear in $X$, but $d\iota_X$ involves differentiating $X$). This is the same phenomenon as for $\mathcal{L}_X Y = [X, Y]$, which is bilinear over $\mathbb{R}$ but only $C^\infty$-linear in $Y$, not in $X$.

---

# The Definition

Let $M$ be a smooth manifold, $X$ a smooth vector field on $M$, and $\omega \in \Omega^k(M)$ a smooth differential $k$-form. Let $\phi^X_t$ denote the flow of $X$ ([[Def - Flow of a Vector Field]]), defined on an open subset of $\mathbb{R} \times M$ containing $\{0\} \times M$.

The **Lie derivative** of $\omega$ along $X$ is the smooth $k$-form $\mathcal{L}_X\omega \in \Omega^k(M)$ defined pointwise by
$$(\mathcal{L}_X\omega)_p = \frac{d}{dt}\bigg|_{t=0}\big((\phi^X_t)^*\omega\big)_p.$$
Here $(\phi^X_t)^*\omega$ is the [[Def - Pullback of a Differential Form on a Manifold|pullback]] of $\omega$ along the time-$t$ flow map, restricted to the domain where the flow is defined; the derivative in $t$ exists because the integrand is smooth in $(t, p)$ near $t = 0$.

Equivalently and far more usefully for computation, $\mathcal{L}_X$ admits **Cartan's magic formula**:
$$\boxed{\mathcal{L}_X\omega = d(\iota_X\omega) + \iota_X(d\omega) = (d\iota_X + \iota_X d)\omega.}$$
This is [[Thm - Cartan's Magic Formula]]. The boxed identity is the practical definition: it computes $\mathcal{L}_X\omega$ purely algebraically from $\omega$ and $X$, never requiring the flow.

**Algebraic properties.** For smooth $X, Y$ and smooth forms $\omega \in \Omega^k(M)$, $\eta \in \Omega^\ell(M)$:

1. **$\mathbb{R}$-linearity in $\omega$:** $\mathcal{L}_X(\omega + \eta) = \mathcal{L}_X\omega + \mathcal{L}_X\eta$, $\mathcal{L}_X(c\omega) = c\,\mathcal{L}_X\omega$.
2. **Leibniz with wedge:** $\mathcal{L}_X(\omega \wedge \eta) = (\mathcal{L}_X\omega) \wedge \eta + \omega \wedge (\mathcal{L}_X\eta)$. The Leibniz rule is *not* graded — there is no sign because $\mathcal{L}_X$ has degree $0$ as an operator.
3. **Commutes with $d$:** $\mathcal{L}_X(d\omega) = d(\mathcal{L}_X\omega)$. (Immediate from Cartan's formula and $d^2 = 0$.)
4. **Commutes with itself in a Lie-algebra sense:** $\mathcal{L}_X\mathcal{L}_Y - \mathcal{L}_Y\mathcal{L}_X = \mathcal{L}_{[X, Y]}$.
5. **On functions:** $\mathcal{L}_X f = X(f) = df(X)$ for $f \in \Omega^0(M)$.
6. **On a $1$-form $\omega$:** $\mathcal{L}_X\omega(Y) = X\omega(Y) - \omega([X, Y])$ for any vector field $Y$.
7. **Interaction with $\iota_Y$:** $[\mathcal{L}_X, \iota_Y] = \iota_{[X, Y]}$.

**Coordinate expression.** In a chart, for $\omega = \sum'_I \omega_I\,dx^I$, applying Cartan's formula chart-by-chart gives the formula. On a $1$-form $\omega = \omega_i\,dx^i$ with $X = X^j\partial_j$,
$$\mathcal{L}_X\omega = X^j(\partial_j \omega_i)\,dx^i + \omega_j (\partial_i X^j)\,dx^i,$$
i.e., $(\mathcal{L}_X\omega)_i = X^j\partial_j\omega_i + \omega_j\partial_i X^j$. The first term is the "convective" derivative; the second comes from the deformation of the basis $1$-forms under the flow.

**Bridge to MA IV.** The Lie derivative of a form on $\mathbb{R}^n$ specializes to the same algebraic operation under any chart, with Cartan's formula serving as the defining computational tool. The Lie derivative of forms is not given its own MA IV page; this is one of the genuinely new tools provided by the manifold setting.

---

# Categorical Definition

The Lie derivative $\mathcal{L}_X$ is the degree-zero "even" part of the Lie superalgebra of operations on $\Omega^\bullet(M)$ generated by $d$ (degree $+1$, odd) and the family of interior products $\iota_X$ (degree $-1$, odd, parametrised by vector fields). The supercommutator $\{d, \iota_X\} = d\iota_X + \iota_X d$ produces $\mathcal{L}_X$ — degree $0$, even — and the full structure is
$$\mathcal{C}(M) = \mathfrak{X}(M) \otimes \langle d, \iota_X, \mathcal{L}_X\rangle,$$
with relations $\{d, d\} = 0$, $\{\iota_X, \iota_Y\} = 0$, $\{d, \iota_X\} = \mathcal{L}_X$, $[\mathcal{L}_X, \mathcal{L}_Y] = \mathcal{L}_{[X, Y]}$, $[\mathcal{L}_X, d] = 0$, $[\mathcal{L}_X, \iota_Y] = \iota_{[X, Y]}$. This is the **Cartan calculus** Lie superalgebra.

The Lie derivative is also a Lie algebra representation: the map $X \mapsto \mathcal{L}_X$ is a Lie algebra homomorphism from $\mathfrak{X}(M)$ (with the Lie bracket) into the algebra of degree-zero $\mathbb{R}$-linear operators on $\Omega^\bullet(M)$. Property 4 is the homomorphism property; properties 1, 2, 3 say each $\mathcal{L}_X$ is a derivation respecting $d$.

A reader unfamiliar with super-Lie-algebra language can take this paragraph as the assertion that the four operations $\{d, \wedge, \iota_X, \mathcal{L}_X\}$ are *organized* by Cartan's magic formula into a tight algebraic system whose relations encode all the commutators that appear in differential geometry. The single relation $\mathcal{L}_X = d\iota_X + \iota_X d$ implies every other commutator one might need.

---

# Relate to Other Fields / Compression

**The Lie derivative of a form is the rate of pullback under the flow, but in practice it is computed algebraically.** This is the deep point: the *meaning* of $\mathcal{L}_X\omega$ is geometric (how does $\omega$ change under the flow of $X$?), but the *computation* is algebraic via Cartan's magic formula. The dichotomy between "meaning" and "computation" is a recurring theme in differential geometry — the Lie bracket has the same dichotomy ($\mathcal{L}_X Y$ measures how flows of $X$ and $Y$ fail to commute, but is computed by $[X, Y] = XY - YX$ in any chart).

**True name:** The Lie derivative $\mathcal{L}_X\omega$ is "$(d\iota_X + \iota_X d)\omega$". The flow definition justifies the name, but the algebraic identity is what one actually uses.

A trigger-reaction pattern: **see "Lie derivative of a form" → invoke Cartan's magic formula immediately**. Do not open the flow definition; do not differentiate in $t$. Write $\mathcal{L}_X\omega = d\iota_X\omega + \iota_X d\omega$ and compute the two exterior derivatives.

**Bridge to symplectic geometry — symplectic vector fields.** A vector field $X$ on a symplectic manifold $(M, \omega)$ is called **symplectic** if $\mathcal{L}_X\omega = 0$, i.e., the flow preserves the symplectic form. By Cartan's formula plus closedness of $\omega$ ($d\omega = 0$), this reduces to $d(\iota_X\omega) = 0$ — the $1$-form $\iota_X\omega$ is closed. If moreover $\iota_X\omega = dH$ is exact, $X$ is the Hamiltonian vector field of $H$, and the flow preserves $\omega$ for the deepest reason: it is generated by an exact form. **Conservation of phase-space volume (Liouville's theorem)** is the consequence: $\omega^n$ is the volume form, $\mathcal{L}_X(\omega^n) = n\,\omega^{n-1} \wedge \mathcal{L}_X\omega = 0$, so the flow preserves volume.

**Bridge to gauge theory — Killing vector fields.** A vector field $X$ on a Riemannian manifold $(M, g)$ is a **Killing vector field** if $\mathcal{L}_X g = 0$, i.e., the flow is an isometry. This is the symmetry condition for the metric. By Cartan-like manipulations and the structure of the metric, this becomes the Killing equation $\nabla_a X_b + \nabla_b X_a = 0$.

**Bridge to PDE — characteristics.** The method of characteristics for first-order PDE can be phrased as: a function $f$ is constant along the flow of $X$ if and only if $\mathcal{L}_X f = X(f) = 0$. Generalizing, a tensor field is invariant under the flow if and only if its Lie derivative vanishes.

---

# Examples / Corollaries

**Is an instance — Lie derivative of a function.** $\mathcal{L}_X f = (d\iota_X + \iota_X d)f = 0 + \iota_X df = df(X) = X(f)$. The Lie derivative of a function along $X$ is the directional derivative — what students of multivariable calculus call "the rate of change of $f$ in the direction $X$".

**Is an instance — Lie derivative of $dx$ on $\mathbb{R}^n$ along a vector field.** For $X = X^j\partial_j$ and $\omega = dx^i$, Cartan's formula gives
$$\mathcal{L}_X dx^i = d(\iota_X dx^i) + \iota_X(d\,dx^i) = d(X^i) + 0 = dX^i = \sum_j (\partial_j X^i)\,dx^j.$$
So the Lie derivative of a coordinate $1$-form is the differential of the corresponding component function of $X$.

**Is an instance — Lie derivative of $dx \wedge dy$ along $\partial_x$ on $\mathbb{R}^2$.** Compute via Cartan: $\iota_{\partial_x}(dx \wedge dy) = dy$, $d(dy) = 0$, so $d(\iota_{\partial_x}(dx \wedge dy)) = 0$. Also $d(dx \wedge dy) = 0$ (top-degree on $\mathbb{R}^2$), so $\iota_{\partial_x}(d(dx \wedge dy)) = 0$. Therefore $\mathcal{L}_{\partial_x}(dx \wedge dy) = 0$. The form is invariant under the flow of $\partial_x$ — the translation in $x$ — because area is translation-invariant.

**Is an instance — Lie derivative of a volume form along a vector field.** For an $n$-manifold with volume form $\Omega$, $\mathcal{L}_X\Omega = (\operatorname{div}X)\,\Omega$ for an appropriately defined divergence. The proof: $\Omega$ is top-degree so $d\Omega = 0$; Cartan gives $\mathcal{L}_X\Omega = d(\iota_X\Omega)$; the $(n-1)$-form $\iota_X\Omega$ is the flux form of $X$, and $d$ of it equals the divergence times $\Omega$. The flow of $X$ preserves volume if and only if $\operatorname{div}X = 0$.

**Is NOT an instance — Lie derivative is graded.** False. Unlike $d$ and $\iota_X$, which are graded (anti-)derivations, the Lie derivative is an *ungraded* derivation: $\mathcal{L}_X(\omega \wedge \eta) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta$ with no sign. This is because $\mathcal{L}_X$ preserves degree, so passing it across a form costs no signs.

**Is NOT an instance — $\mathcal{L}_X$ is $C^\infty(M)$-linear in $X$.** False. $\mathcal{L}_{fX}\omega \neq f\,\mathcal{L}_X\omega$ in general. The correct identity, from Cartan: $\mathcal{L}_{fX}\omega = f\,\mathcal{L}_X\omega + df \wedge \iota_X\omega$. The extra term comes from differentiating $f$ in $d\iota_{fX}\omega = d(f\,\iota_X\omega) = df \wedge \iota_X\omega + f\,d\iota_X\omega$.

**Is NOT an instance — pulling back commutes with $\mathcal{L}_X$.** Subtle. For a smooth map $F : M \to N$ and a vector field $X$ on $M$, there is no canonical "pushforward of $X$" to $N$ unless $F$ is a diffeomorphism, so $\mathcal{L}_X$ on the $M$-side and the (nonexistent) $\mathcal{L}_{F_*X}$ on the $N$-side don't form a natural commutation. *When $F$ is a diffeomorphism*, $F^*\mathcal{L}_{F_*X}\omega = \mathcal{L}_X(F^*\omega)$ — the Lie derivative is natural under diffeomorphisms. For general smooth maps the right concept involves $F$-related vector fields.

**Corollary — $\mathcal{L}_X$ commutes with $d$.** $\mathcal{L}_X d\omega = (d\iota_X + \iota_X d)(d\omega) = d\iota_X d\omega + 0 = d(\iota_X d\omega) = d(\mathcal{L}_X\omega - d\iota_X\omega) = d\mathcal{L}_X\omega - d^2 \iota_X\omega = d\mathcal{L}_X\omega$. The cross-term vanishes by $d^2 = 0$.

**Corollary — invariant forms.** $\omega$ is invariant under the flow of $X$ if and only if $\mathcal{L}_X\omega = 0$. Equivalently, by Cartan, $d\iota_X\omega + \iota_X d\omega = 0$. For a closed form ($d\omega = 0$), invariance reduces to $d\iota_X\omega = 0$ — the $(k-1)$-form $\iota_X\omega$ is closed.

**Corollary — Lie derivative of a closed form is exact.** If $d\omega = 0$, then by Cartan $\mathcal{L}_X\omega = d(\iota_X\omega)$, which is exact. So the Lie derivative of a closed form is exact, and on the level of de Rham cohomology, the Lie derivative is zero: $[\mathcal{L}_X\omega] = 0$ in $H^k_{dR}(M)$. This is the cohomological statement of "infinitesimal symmetries of a closed form leave its cohomology class fixed".

**Calibration check.** Compute $\mathcal{L}_{\partial_x}(y\,dx)$ on $\mathbb{R}^2$ via Cartan (answer: $0$, since $\iota_{\partial_x}(y\,dx) = y$ and $d(y) = dy$, then $\iota_{\partial_x}(dy) = 0$ — wait, recompute: $\iota_{\partial_x}(y\,dx) = y \cdot dx(\partial_x) = y$. Then $d(y) = dy$. So $d(\iota_{\partial_x}(y\,dx)) = dy$. Now $d(y\,dx) = dy \wedge dx = -dx \wedge dy$, and $\iota_{\partial_x}(-dx \wedge dy) = -(dx(\partial_x)\,dy - dy(\partial_x)\,dx) = -(1\cdot dy - 0) = -dy$. So $\mathcal{L}_{\partial_x}(y\,dx) = dy + (-dy) = 0$ — correct, since $y\,dx$ is invariant under $x$-translation); compute $\mathcal{L}_{\partial_\theta}(d\theta)$ on $\mathbb{R}^2 \setminus \{0\}$ (answer: $0$); verify $\mathcal{L}_X(dx \wedge dy) = (\partial_x X^1 + \partial_y X^2)\,dx \wedge dy$ for $X = X^1 \partial_x + X^2 \partial_y$ on $\mathbb{R}^2$ (the divergence in the plane); confirm $\mathcal{L}_X = \mathcal{L}_X \mathcal{L}_Y - \mathcal{L}_Y \mathcal{L}_X$ where $[X, Y]$ replaces the operator commutator. If you can also explain why $\mathcal{L}_X$ commutes with $d$ (one line via Cartan and $d^2 = 0$), you have understood the operator.

---

# Unlocked by This

> [!tip] Cartan's Magic Formula *(this chapter)*
> The boxed identity $\mathcal{L}_X = d\iota_X + \iota_X d$ is the algebraic heart of the calculus of forms. It is what makes Lie derivatives of forms tractable — never use the flow definition for computation. See [[Thm - Cartan's Magic Formula]].

> [!tip] Liouville's Theorem *(from Symplectic / Statistical Mechanics)*
> On a symplectic manifold $(M, \omega)$ of dimension $2n$, the **Liouville volume form** $\omega^n = \omega \wedge \cdots \wedge \omega$ ($n$ factors) is invariant under any Hamiltonian flow: $\mathcal{L}_{X_H}\omega^n = 0$. The proof is a Cartan-formula calculation: $\mathcal{L}_{X_H}\omega = 0$ (since $\iota_{X_H}\omega = dH$ exact, $\mathcal{L}_{X_H}\omega = d\iota_{X_H}\omega = d^2 H = 0$), and Leibniz propagates this to $\omega^n$. The physical statement: phase-space volume is conserved by Hamiltonian dynamics — the foundation of classical statistical mechanics.

> [!tip] Killing Vector Fields *(from Riemannian Geometry / General Relativity)*
> A **Killing vector field** on a Riemannian (or Lorentzian) manifold $(M, g)$ is a vector field $X$ with $\mathcal{L}_X g = 0$ — the flow is an isometry. The Killing equation $\nabla_a X_b + \nabla_b X_a = 0$ is the differential consequence. Killing vector fields encode continuous symmetries of the metric, and by Noether's theorem each one gives a conserved quantity along geodesics; in general relativity, time-translation Killing vectors give conserved energy, rotational Killing vectors give conserved angular momentum.

> [!tip] Connection Forms and Gauge Symmetry *(from Gauge Theory)*
> On a principal bundle, the difference between two connections is a vertical $1$-form, and an infinitesimal gauge transformation is exactly a Lie derivative of the connection along a vertical vector field. The whole gauge-invariance machinery — connections transform covariantly, curvatures gauge-equivariantly — is computed via Lie derivatives plus the Cartan structure equation.
