---
type: definition
subject: gauge-theory
prereqs:
  - "Def - The Yang-Mills Lagrangian"
  - "Def - The Yang-Mills Field Strength"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Prerequisite Concepts

- [[Def - The Yang-Mills Lagrangian]]
- [[Def - The Yang-Mills Field Strength]]

# Notation

$(M, g)$ is an oriented 4-dimensional (pseudo-)Riemannian manifold; $P \to M$ a principal $G$-bundle for a compact Lie group $G$; $\mathcal{A}$ the space of all connections on $P$; $\mathcal{G}$ the group of gauge transformations (smooth sections of the adjoint bundle of automorphisms of $P$). The space $\mathcal{A}$ is an affine space modelled on $\Omega^1(M; \operatorname{ad} P)$ — the difference of two connections is a $\mathfrak{g}$-valued 1-form. The group $\mathcal{G}$ acts on $\mathcal{A}$, and the quotient $\mathcal{A}/\mathcal{G}$ is the **moduli space of connections**.

For a connection $A \in \mathcal{A}$, $F_A$ is its field strength (curvature). The $L^2$ inner product on $\mathfrak{g}$-valued $k$-forms uses the metric $g$, the Hodge star $\star$, and the trace pairing: $(\alpha, \beta) = -\int_M\operatorname{tr}(\alpha \wedge \star\beta)$.

Wider conventions are in [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons]].

---

# Axiom Motivation

The Yang–Mills action $S_{\text{YM}}[A]$ is a real-valued functional on the infinite-dimensional space of connections $\mathcal{A}$. Its role is twofold: as the variational source of the Yang–Mills equations (its critical points are Yang–Mills connections), and as the *measure of how much curvature a configuration carries* (its value is the squared $L^2$-norm of the curvature). Both roles follow from a single definition.

*Why the squared norm of $F$?* The natural geometric quantity associated to a connection is its curvature $F$, a $\mathfrak{g}$-valued 2-form. To turn this into a number, one needs a norm — and the natural norm comes from the metric on $M$ (giving the Hodge star and the $L^2$ pairing on forms) combined with an invariant inner product on $\mathfrak{g}$ (giving the trace pairing). The combination $\|F\|^2_{L^2} = \int_M \langle F, F\rangle\,\operatorname{vol}_g$ is the unique natural scalar built from $F$ alone (up to overall constants and the topological term $\int\operatorname{tr}(F\wedge F)$, which is a different gauge-invariant quantity).

*Why integrate over $M$?* The integrand $\operatorname{tr}(F\wedge\star F)$ is a 4-form on $M$ (since $F$ is a 2-form and $\star F$ is a $(4-2) = 2$-form, the wedge is a 4-form). Integrating a 4-form over a 4-manifold gives a number, the action $S_{\text{YM}}$. Integration over $M$ also makes $S_{\text{YM}}$ a *non-local* functional — the action of a connection at a point depends on its values everywhere — which is essential for the Euler–Lagrange equations to be PDEs rather than algebraic equations.

*Why is $S_{\text{YM}}$ gauge-invariant?* Under $A \to A^g = gAg^{-1} - (i/q)dg \cdot g^{-1}$, the curvature transforms homogeneously $F \to gFg^{-1}$, and the trace is conjugation-invariant: $\operatorname{tr}(gFg^{-1}\cdot \star gFg^{-1}) = \operatorname{tr}(gF\star F g^{-1}) = \operatorname{tr}(F\star F)$. So $S_{\text{YM}}[A^g] = S_{\text{YM}}[A]$: the action descends to a well-defined functional on the moduli space $\mathcal{A}/\mathcal{G}$. This is the necessary condition for $S_{\text{YM}}$ to be physical.

*Why is $S_{\text{YM}}$ non-negative (in Euclidean signature)?* The pointwise inner product $\langle F, F\rangle = -\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})/2$ is positive-definite on the space of $\mathfrak{g}$-valued 2-forms (this uses the positivity of the trace form on $\mathfrak{g} \subset \mathfrak{u}(N)$ and the positivity of the metric in Euclidean signature). Integration preserves non-negativity, so $S_{\text{YM}}[A] \ge 0$ with equality iff $F = 0$ — that is, iff the connection is flat. This non-negativity is what makes existence theorems (minimum-energy configurations, instantons) approachable via variational methods.

*Why is $S_{\text{YM}}$ critical at the Yang–Mills equation?* Variational principles require $S$ to be differentiable on $\mathcal{A}$. Since $\mathcal{A}$ is affine, "differentiable" means the Gateaux derivative $\delta S[A]\cdot\delta A = \lim_{t\to 0}\tfrac1t(S[A + t\delta A] - S[A])$ exists for compactly-supported $\delta A$. The functional $S_{\text{YM}}$ is *quadratic* in $A$ (after expanding $F = dA - iqA\wedge A$ into linear-plus-non-linear-in-$A$ pieces), so it is automatically differentiable, and the variation is $\delta S_{\text{YM}} = (\delta F, F) = (d_A\delta A, F) = (\delta A, d_A^* F)$ — an inner product with $d_A^* F$. Setting this to zero for all $\delta A$ gives $d_A^* F = 0$, the YM equation.

Why not a different functional, like $\int \operatorname{tr}(F\wedge F)$ or $\int \operatorname{tr}(F^3)$? The first is the *topological term* $\theta\cdot 8\pi^2 k$ — a number depending only on the bundle and homotopy class of the connection, not on the connection itself, so its variation vanishes identically and it produces no field equations. The second is *trilinear* in $F$, not Lorentz-invariant in 4D in the usual way (you need 4 derivative slots to soak up $F^3$), and produces equations of motion non-linear at leading order — physically unhealthy. The squared norm $\int|F|^2$ is the right functional.

---

# The Definition

Let $(M, g)$ be an oriented 4-dimensional (pseudo-)Riemannian manifold, $P \to M$ a principal $G$-bundle for a compact Lie group $G$, and $A$ a smooth connection on $P$ with field strength $F$. The **Yang–Mills action functional** is the real-valued functional on the space $\mathcal{A}$ of connections defined by

$$S_{\text{YM}}[A] = -\frac{1}{2}\int_M \operatorname{tr}(F \wedge \star F).$$

Equivalently, in components,

$$S_{\text{YM}}[A] = -\frac{1}{4}\int_M \operatorname{tr}(F_{\mu\nu}F^{\mu\nu})\,\sqrt{|g|}\,d^4x,$$

and in coordinate-free Hilbert-space form (using the $L^2$ inner product on $\Omega^2(M; \operatorname{ad} P)$),

$$S_{\text{YM}}[A] = \frac{1}{2}(F, F)_{L^2} = \frac{1}{2}\|F_A\|^2_{L^2}.$$

**Properties:**
1. *Non-negativity (Euclidean signature):* $S_{\text{YM}}[A] \ge 0$, with $= 0$ iff $A$ is flat ($F = 0$).
2. *Gauge invariance:* $S_{\text{YM}}[A^g] = S_{\text{YM}}[A]$ for any $g \in \mathcal{G}$.
3. *Variational derivative:* $\delta S_{\text{YM}}/\delta A = d_A^* F$, where $d_A^* = -\star d_A\star$ (up to a sign depending on degree and signature) is the formal adjoint of $d_A$.
4. *Critical points:* $A$ is a critical point of $S_{\text{YM}}$ iff $d_A^* F = 0$, equivalently $d_A\star F = 0$ (the **Yang–Mills equation**).
5. *Topological lower bound (Euclidean, $G = SU(N)$):* $S_{\text{YM}}[A] \ge 8\pi^2|k|$, where $k = \frac{1}{8\pi^2}\int_M\operatorname{tr}(F\wedge F)$ is the second Chern number, with equality iff $A$ is self-dual ($k \ge 0$) or anti-self-dual ($k \le 0$).

When matter fields $\psi$ are present coupled to $A$ by minimal coupling, the full action is $S = S_{\text{matter}}[\psi, A] + S_{\text{YM}}[A]$, and varying with respect to $A$ produces the YM equation with source: $d_A\star F = \star J$, where $J = J^\mu dx^\mu \otimes T^a$ is the matter current.

---

# Relate to Other Fields / Compression

The Yang–Mills functional is the **infinite-dimensional analogue of a Morse function** on the space of connections $\mathcal{A}$. The critical points are the YM connections; the Hessian of $S_{\text{YM}}$ at a critical point detects the local minimum/maximum/saddle structure. Modulo gauge transformations, the moduli space $\mathcal{A}/\mathcal{G}$ has a stratification by the index of the Hessian, and Morse theory on this infinite-dimensional space — formalised by **Atiyah and Bott** in their 1982 work on Yang–Mills over Riemann surfaces — gives cohomological information about $\mathcal{A}/\mathcal{G}$ in terms of the homology of the critical strata. This is the gauge-theory version of Morse theory and the seed of **Atiyah–Bott equivariant cohomology**.

The functional is also the **action of the simplest non-linear sigma model on connections**: viewing $\mathcal{A}$ as a "manifold" with $L^2$ metric and the action $S_{\text{YM}}$ as a "height function", the gradient flow $\partial_t A = -\nabla S_{\text{YM}}[A] = -d_A^* F$ produces the **Yang–Mills heat flow**, the parabolic relaxation that drives any initial connection to a Yang–Mills connection (under suitable convergence hypotheses). This is the analogue of the harmonic-map heat flow for $\sigma$-models and the Ricci flow for metrics. **Uhlenbeck's compactness theorem** controls the limits of YM heat flow and is the technical foundation of all modern gauge-theory existence results.

**True name:** the YM action is the *squared $L^2$-norm of the curvature*. The operational form $S_{\text{YM}} = \tfrac12\|F\|^2$ is what you reach for to prove positivity, derive the BPS bound, or analyse the gradient flow. The component formula is the *expression* in a chart; the structural identity $S = \tfrac12\|F\|^2$ is what makes the theory tractable as a Riemannian-geometric problem on $\mathcal{A}/\mathcal{G}$.

---

# Examples / Corollaries

**Example 1 — Maxwell action.** For $G = U(1)$ on Minkowski $\mathbb{R}^4$, $S_{\text{YM}}[A] = -\tfrac14\int F_{\mu\nu}F^{\mu\nu}\,d^4x = \tfrac12\int(\vec E^2 - \vec B^2)\,d^4x$ — the classical Maxwell action. Critical points are solutions of Maxwell's equations $\partial_\mu F^{\mu\nu} = 0$, including all radiation fields (plane waves) and static Coulomb configurations.

**Example 2 — BPST instanton action.** For the BPST $SU(2)$ instanton on Euclidean $\mathbb{R}^4$, $S_{\text{YM}}[A_{\text{BPST}}] = 8\pi^2$, exactly. This is the *minimum* action over the class of $k = 1$ connections, achieved by self-duality. The fact that the action is finite and depends only on the topological charge (not on the size $\rho$ or the centre of the instanton) is a manifestation of the conformal invariance of $S_{\text{YM}}$ in 4 dimensions.

**Example 3 — Flat connection (trivial absolute minimum).** On any 4-manifold, the trivial connection $A = 0$ on the trivial bundle has $F = 0$ and hence $S_{\text{YM}}[0] = 0$. More generally, any flat connection (one with $F = 0$) has zero YM action. The space of flat connections modulo gauge equivalence is the **character variety** $\operatorname{Hom}(\pi_1(M), G)/G$, a finite-dimensional algebraic variety, which is the "trivial" critical stratum of $S_{\text{YM}}$.

**Non-example — A non-gauge-invariant "would-be action" $\int|A|^2$.** Consider the functional $S^{\text{wrong}}[A] = \tfrac12\int|A|^2\, d^4x = -\tfrac12\int\operatorname{tr}(A\wedge\star A)$. This is *not* gauge-invariant — under $A \to gAg^{-1} - (i/q)dg\cdot g^{-1}$, the cross-term $\int\operatorname{tr}(A \cdot dg\cdot g^{-1})$ does not cancel. Hence $S^{\text{wrong}}$ does not descend to $\mathcal{A}/\mathcal{G}$ and does not produce well-defined field equations. This is why one cannot simply build the gauge-field action from $A$ alone — gauge invariance forces the use of the curvature $F$, exactly as the gauge principle predicts.

**Calibration check.** A reader who has internalised the definition should be able to: (a) compute $S_{\text{YM}}$ for the constant magnetic field $\vec B = B\hat z$ on the box $[0, L]^4$, obtaining $S = \tfrac12 B^2 L^4$; (b) explain why $S_{\text{YM}}$ is *finite* on $\mathbb{R}^4$ only for instanton-type configurations (those with $F \to 0$ at infinity faster than $1/r^2$); (c) state without proof that $S_{\text{YM}}$ is bounded below by $8\pi^2|k|$ in each topological sector and identify the configurations saturating this bound as the (anti-)self-dual ones.

---

# Unlocked by This

> [!tip] Geometric Analysis on the Space of Connections *(from PDE / Differential Geometry)*
> The Yang–Mills action is a paradigm example of a **geometric variational problem**: an action functional on an infinite-dimensional space of geometric objects (here, connections on a bundle) whose critical points satisfy a non-linear PDE (the YM equation). The space $\mathcal{A}/\mathcal{G}$ has natural infinite-dimensional Riemannian structure, and analytical questions about the existence, regularity, and compactness of YM critical points are answered by **Uhlenbeck's compactness theorem**, **Sedlacek's removable-singularities theorem**, and **Donaldson's theorems on the moduli space of ASD connections**. The same suite of analytical tools applies to harmonic maps, Einstein metrics, and minimal surfaces — making "geometric analysis" a unified field with YM theory as one of its central examples.

> [!tip] Topological Quantum Field Theory *(from Mathematical Physics)*
> Replacing the action $S_{\text{YM}}$ by the topological **Chern–Simons action** $S_{\text{CS}}[A] = \frac{k}{4\pi}\int_Y \operatorname{tr}(A\wedge dA + \tfrac{2}{3}A\wedge A\wedge A)$ on a 3-manifold $Y$ produces a *topological* gauge theory whose path integral is invariant under metric deformations and yields **Witten's invariants of 3-manifolds** (the **Witten–Reshetikhin–Turaev invariants**), the **Jones polynomial of knots** in $S^3$ (as Wilson-loop expectation values in $SU(2)$ Chern–Simons), and the entire framework of **topological quantum field theory** (TQFT) as axiomatised by Atiyah. The YM action and the CS action are two faces of the same gauge-theoretic coin: $dS_{\text{CS}} = \tfrac{k}{4\pi}\operatorname{tr}(F\wedge F)$, the topological term in 4D YM.
