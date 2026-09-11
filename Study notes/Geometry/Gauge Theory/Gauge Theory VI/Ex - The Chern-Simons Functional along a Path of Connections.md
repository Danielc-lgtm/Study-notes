---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Four-Dimensional Formula for the Chern-Simons Functional"
  - "Thm - Transgression Formula and the Chern-Simons Form"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Manifold with Boundary and Induced Orientation"
  - "Def - Chern-Simons Functional"
  - "Thm - Critical Points of the Chern-Simons Functional are the Flat Connections"
tags: [geometry, gauge-theory]
---

# Problem Statement

Throughout, $M$ is a closed oriented three-dimensional manifold, $G = SU(2)$, and $P \to M$ is a principal $SU(2)$-bundle; by the classification of principal $SU(2)$-bundles this $P$ is trivial, so we fix once and for all a trivialisation and identify a connection with its connection one-form $A \in \Omega^1(M; \mathfrak{su}(2))$. The Lie algebra $\mathfrak{su}(2)$ is the space of trace-free skew-Hermitian $2 \times 2$ complex matrices, and $\operatorname{tr}$ denotes the ordinary matrix trace on $2\times2$ matrices. The curvature of $A$ is $F_A = dA + A \wedge A \in \Omega^2(M; \mathfrak{su}(2))$ (for the matrix group $SU(2)$ the bracket term $\tfrac12[A \wedge A]$ equals $A \wedge A$), the **Chern–Simons three-form** is
$$\operatorname{cs}(A) := \operatorname{tr}\!\Big(A \wedge dA + \tfrac{2}{3}\, A \wedge A \wedge A\Big) \in \Omega^3(M),$$
and the **Chern–Simons functional** is $\vartheta(A) = \tfrac{1}{8\pi^2} \int_M \operatorname{cs}(A)$, read here as a real number attached to the fixed trivialisation (the reduction modulo $\mathbb{Z}$ that makes it trivialisation-independent is not needed for this exercise, since a smooth path of connections stays in one trivialisation).

Let $t \mapsto A_t$, for $t \in [t_0, t_1]$, be a smooth path of connections in $\Omega^1(M; \mathfrak{su}(2))$; write $\dot{A}_t := \partial_t A_t \in \Omega^1(M; \mathfrak{su}(2))$ for its velocity and $F_{A_t} = dA_t + A_t \wedge A_t$ for the curvature of the connection at time $t$. Form the compact oriented four-manifold with boundary $X := M \times [t_0, t_1]$, with $t$ the coordinate on the interval, oriented by the product orientation in which a frame $(\partial_t, e_1, e_2, e_3)$ of $T X$ is positive exactly when $(e_1, e_2, e_3)$ is a positive frame of $TM$ (that is, the "interval-direction-first" orientation, $\mathrm{vol}_X = dt \wedge \mathrm{vol}_M$). Prove the two assertions of Haydys's Exercise 96(a), second display:

1. **(Integral form.)** With $\mathbb{A}$ the connection on $X$ whose restriction to each slice $M \times \{t\}$ is $A_t$ (built precisely in Step 1),
$$\vartheta(A_{t_1}) - \vartheta(A_{t_0}) = \frac{1}{8\pi^2} \int_{M \times [t_0, t_1]} \operatorname{tr}\!\big(F_{\mathbb{A}} \wedge F_{\mathbb{A}}\big) .$$

2. **(Differential form.)** Consequently
$$\frac{d}{dt}\, \vartheta(A_t) = \frac{1}{4\pi^2} \int_M \operatorname{tr}\!\big(F_{A_t} \wedge \dot{A}_t\big),$$
which is exactly the first-variation (critical-point) formula $d\vartheta_A(a) = \tfrac{1}{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a)$ evaluated at $A = A_t$ and $a = \dot{A}_t$.

This reproves part (c) of the four-dimensional formula theorem as a stand-alone Stokes computation and connects it to the differential of $\vartheta$.

> [!warning] Corrected source typo
> In Haydys's Exercise 96(a) the second display reads $\vartheta(A_t) - \vartheta(A_{t_0}) = \int_{M \times [t_0, t]} \operatorname{tr}(F_A \wedge F_A)$, without the factor $\tfrac{1}{8\pi^2}$ that the definition of $\vartheta$ carries (Appendix B, item 6, of the content map). The corrected identity, restored above and proved below, carries the $\tfrac{1}{8\pi^2}$ so that both sides are genuinely equal.

**Recall:**

The objects in play are the Chern–Simons three-form and functional, the transgression identity that makes $\operatorname{tr}(F \wedge F)$ exact, Stokes' theorem on a manifold with boundary, and the induced orientation on that boundary.

![[Def - Chern-Simons Functional#The Definition]]

![[Thm - Transgression Formula and the Chern-Simons Form#Statement]]

The one consequence of the transgression theorem we use is its final display: for any $A \in \Omega^1(Y; \mathfrak{su}(2))$ on any manifold $Y$,
$$d\, \operatorname{cs}(A) = \operatorname{tr}\!\big(F_A \wedge F_A\big), \qquad \operatorname{cs}(A) = \operatorname{tr}\!\Big(A \wedge dA + \tfrac{2}{3} A \wedge A \wedge A\Big),$$
so the four-form $\operatorname{tr}(F_A \wedge F_A)$ is exact with an explicit primitive. This is Haydys's equation (97); see [[Thm - Transgression Formula and the Chern-Simons Form|the transgression theorem]] for its proof and [[Ex - The Chern-Simons Form Transgresses the Second Chern Form|the companion drill]] for the bare expansion.

![[Thm - Stokes' Theorem on Manifolds#Statement]]

![[Def - Manifold with Boundary and Induced Orientation#The Definition]]

The induced-orientation convention is "outward normal first": a frame $(v_1, v_2, v_3)$ of $T_p(\partial X)$ is positive for the induced orientation exactly when $(\nu, v_1, v_2, v_3)$ is positive in $T_p X$, where $\nu$ is the outward-pointing normal.

![[Thm - The Four-Dimensional Formula for the Chern-Simons Functional#Statement]]

Part (c) of this theorem is precisely assertion 1 above; the point of the exercise is to derive it directly rather than to quote it. Finally, the differential to be matched is the one proved on [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|the critical-point theorem]]: for $a \in \Omega^1(M; \mathfrak{su}(2))$, $d\vartheta_A(a) = \tfrac{1}{4\pi^2} \int_M \operatorname{tr}(F_A \wedge a)$, whose vanishing for all $a$ characterises the flat connections.

The trace obeys the graded-cyclicity rule for matrix-valued forms: if $\alpha$ has degree $p$ and $\beta$ has degree $q$ then $\operatorname{tr}(\alpha \wedge \beta) = (-1)^{pq} \operatorname{tr}(\beta \wedge \alpha)$. This single rule drives every sign below.

---

# Convergent Strategy

**Problem class.** This is a *reduce-a-boundary-difference-to-a-bulk-integral* problem: the left-hand side is a difference of the same functional at two endpoints, and the right-hand side is an integral over the region between them. The recognisable signature is that the integrand of the difference, $\operatorname{cs}(A)$, is a form whose exterior derivative is the bulk integrand, $\operatorname{tr}(F \wedge F)$. Whenever a quantity is "$\int_{\text{boundary}} (\text{primitive})$" and its primitive has a clean exterior derivative, the tool is Stokes' theorem, and the difference-of-endpoints structure of $\partial(M \times [t_0, t_1])$ produces the two-term boundary automatically.

**Assumption pattern.** Two hypotheses do all the work. First, $M$ is *three*-dimensional: this is what kills the purely spatial four-form $F_{A_t} \wedge F_{A_t}$ (a four-form on a three-manifold slice is zero) and leaves only the terms that carry the interval direction $dt$. Second, $M$ is *closed* (compact without boundary), so that $\partial X = \partial(M \times [t_0, t_1])$ consists solely of the two end slices $M \times \{t_1\}$ and $M \times \{t_0\}$, with no side boundary $\partial M \times [t_0, t_1]$ to contribute. If either hypothesis failed — a four-dimensional $M$, or a $M$ with boundary — extra terms would survive and the clean identity would break.

**Theorem routing.** The route is: build the path connection $\mathbb{A}$ on $X$ in temporal gauge (no $dt$-component); compute $F_{\mathbb{A}} = F_{A_t} + dt \wedge \dot{A}_t$ by splitting the exterior derivative on $X$ into its $M$-part and its $t$-part; apply the *transgression identity* (97) from [[Thm - Transgression Formula and the Chern-Simons Form]] to write $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}}) = d\,\operatorname{cs}(\mathbb{A})$; apply *[[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]]* and the *[[Def - Manifold with Boundary and Induced Orientation|induced boundary orientation]]* to turn $\int_X d\,\operatorname{cs}(\mathbb{A})$ into $\int_M \operatorname{cs}(A_{t_1}) - \int_M \operatorname{cs}(A_{t_0}) = 8\pi^2(\vartheta(A_{t_1}) - \vartheta(A_{t_0}))$. For the differential form, reduce the integrand $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}})$ to $2\, dt \wedge \operatorname{tr}(\dot{A}_t \wedge F_{A_t})$, integrate over the interval by Fubini, and differentiate by the fundamental theorem of calculus, landing on the differential of [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|the critical-point theorem]].

**Key decision point.** The one genuinely creative move is the *choice of the connection $\mathbb{A}$ on $X$*: taking it in temporal gauge, with no component along $dt$, so that its restriction to each slice is exactly $A_t$ and its curvature splits cleanly as $F_{\mathbb{A}} = F_{A_t} + dt \wedge \dot{A}_t$. Any other extension of the family $\{A_t\}$ to a connection on $X$ would give the same left-hand and right-hand sides (both are determined by the endpoints and by $\operatorname{tr}(F \wedge F)$'s cohomological role), but only the temporal-gauge choice makes the curvature and its square transparent. The second decision is orienting $X$ so that $\mathrm{vol}_X = dt \wedge \mathrm{vol}_M$: this is exactly the orientation for which the induced orientation on the top slice is $+M$ and on the bottom slice is $-M$, giving the difference $\vartheta(A_{t_1}) - \vartheta(A_{t_0})$ with the correct sign.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (referred to by the descriptive names of the topic page's Legal Operations; the orchestrator will reconcile the numbering once the topic page is assembled):

1. **Split the exterior derivative on a product.** On $X = M \times [t_0, t_1]$ write $d_X = d_M + dt \wedge \partial_t$, so that the exterior derivative of a $t$-dependent spatial form separates into its $M$-derivative and its $t$-derivative. This is how $F_{\mathbb{A}}$ acquires its two pieces.

2. **Transgress $\operatorname{tr}(F \wedge F)$ to an exact form.** Apply operation "the second Chern form is exact via Chern–Simons" from [[Thm - Transgression Formula and the Chern-Simons Form]]: on any manifold, $\operatorname{tr}(F_A \wedge F_A) = d\,\operatorname{cs}(A)$. Here it is applied to $\mathbb{A}$ on the four-manifold $X$.

3. **Convert a bulk integral of an exact form into a boundary integral (Stokes).** Since $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}}) = d\,\operatorname{cs}(\mathbb{A})$ is exact on $X$, [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] replaces $\int_X d\,\operatorname{cs}(\mathbb{A})$ by $\int_{\partial X}\operatorname{cs}(\mathbb{A})$.

4. **Read off the induced orientations of the two end slices.** With $X$ oriented by $dt \wedge \mathrm{vol}_M$, the top slice inherits $+M$ and the bottom slice inherits $-M$, so the boundary integral is the endpoint difference $\int_M \operatorname{cs}(A_{t_1}) - \int_M \operatorname{cs}(A_{t_0})$.

5. **Pull back a form to a slice (naturality).** For the inclusion $\iota_t : M \to X$, $x \mapsto (x,t)$, one has $\iota_t^* \mathbb{A} = A_t$ and hence $\iota_t^* \operatorname{cs}(\mathbb{A}) = \operatorname{cs}(A_t)$, because pull-back commutes with $d$, with $\wedge$, and with the trace.

6. **Discard vanishing terms by degree and by the $dt \wedge dt = 0$ rule.** A four-form purely in the $M$-directions vanishes on the three-manifold $M$, and any term with two $dt$-factors vanishes; this collapses the expansion of $F_{\mathbb{A}} \wedge F_{\mathbb{A}}$ to a single surviving term.

7. **Integrate over the interval by Fubini and differentiate by the fundamental theorem of calculus.** With the "$dt$-first" orientation, $\int_X dt \wedge \beta_t = \int_{t_0}^{t_1}\big(\int_M \beta_t\big)\, dt$, and differentiating the resulting antiderivative recovers $\tfrac{d}{dt}\vartheta(A_t)$.

---

# Hints

> [!note]- Hint 1
> The two definitions of $\vartheta$ — the three-dimensional integral of $\operatorname{cs}(A)$ over $M$ and the four-dimensional integral of $\operatorname{tr}(F \wedge F)$ over a bounding $X$ — are linked by a single pointwise identity: $\operatorname{tr}(F_A \wedge F_A) = d\,\operatorname{cs}(A)$. You are being asked to run this identity on the specific four-manifold $X = M \times [t_0, t_1]$. What is the boundary of $X$, and what does Stokes give you?

> [!note]- Hint 2
> To use $X = M \times [t_0, t_1]$ you first need a connection on it whose slices are the given $A_t$. Take the *temporal-gauge* connection $\mathbb{A}$: in the product coordinates it has no $dt$-component and its spatial part at time $t$ is $A_t$. Split $d_X = d_M + dt\wedge\partial_t$ and compute $F_{\mathbb{A}} = d_X\mathbb{A} + \mathbb{A}\wedge\mathbb{A}$. You should find two pieces: a spatial curvature and a piece carrying $dt$.

> [!note]- Hint 3
> With $F_{\mathbb{A}} = F_{A_t} + dt \wedge \dot{A}_t$, expand $F_{\mathbb{A}} \wedge F_{\mathbb{A}}$ into four terms. Two of them die immediately: $F_{A_t} \wedge F_{A_t}$ is a four-form built only from the three $M$-directions (so it is zero on the three-manifold slice), and the term with two $dt$-factors contains $dt \wedge dt = 0$. What is left is a single term proportional to $dt$.

> [!note]- Hint 4
> Apply Stokes to $\int_X d\,\operatorname{cs}(\mathbb{A})$. The boundary is the top slice $M \times \{t_1\}$ and the bottom slice $M \times \{t_0\}$. Orient $X$ by $dt \wedge \mathrm{vol}_M$; then the outward normal is $+\partial_t$ on top and $-\partial_t$ on the bottom, so "outward normal first" gives the top slice orientation $+M$ and the bottom slice orientation $-M$. Because $\iota_t^* \operatorname{cs}(\mathbb{A}) = \operatorname{cs}(A_t)$, the boundary integral is $\int_M \operatorname{cs}(A_{t_1}) - \int_M \operatorname{cs}(A_{t_0})$. Divide by $8\pi^2$.

> [!note]- Hint 5
> For the differential form, put the surviving integrand $2\, dt \wedge \operatorname{tr}(\dot{A}_t \wedge F_{A_t})$ through Fubini over the interval, obtaining $8\pi^2\big(\vartheta(A_{t_1}) - \vartheta(A_{t_0})\big) = \int_{t_0}^{t_1}\!\big(\int_M 2\,\operatorname{tr}(\dot{A}_s \wedge F_{A_s})\big)\, ds$. Treat $t_1$ as a variable upper limit and differentiate with the fundamental theorem of calculus. Then move $F$ past $\dot A$ with the trace-cyclicity rule to match the sign in the critical-point formula.

---

# Solution

The plan is to run the transgression identity $\operatorname{tr}(F \wedge F) = d\,\operatorname{cs}$ on the cylinder $X = M \times [t_0, t_1]$ for the temporal-gauge connection $\mathbb{A}$ that interpolates the path. Stokes then converts the bulk integral of the exact form $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}})$ into a boundary integral over the two end slices, and the induced orientations turn that boundary integral into the endpoint difference of $\vartheta$; this is assertion 1. For assertion 2 we reduce the bulk integrand to a single $dt$-term, apply Fubini, and differentiate by the fundamental theorem of calculus, arriving at the differential proved on the critical-point theorem.

**Step 1: Build the temporal-gauge connection $\mathbb{A}$ on $X$ and compute its curvature.**

Define $\mathbb{A} \in \Omega^1(X; \mathfrak{su}(2))$ so that at a point $(x, t)$ it acts as $A_t|_x$ on the $M$-directions and as $0$ on $\partial_t$. Its curvature splits as $F_{\mathbb{A}} = F_{A_t} + dt \wedge \dot{A}_t$.

> [!note]- Derivation
> Let $\{x^i\}$ be local coordinates on $M$ and write the path in these coordinates as $A_t = \sum_i a_i(x, t)\, dx^i$ with $a_i(x,t) \in \mathfrak{su}(2)$ smooth in $(x,t)$. The **temporal-gauge connection** on $X = M \times [t_0, t_1]$ is
> $$\mathbb{A} := \sum_i a_i(x, t)\, dx^i \in \Omega^1(X; \mathfrak{su}(2)),$$
> that is, the same coefficient functions now regarded as functions on $X$, with no $dt$-term. By construction its pull-back to the slice $M \times \{t\}$ under $\iota_t : x \mapsto (x, t)$ is $\iota_t^* \mathbb{A} = \sum_i a_i(x, t)\, dx^i = A_t$, so $\mathbb{A}$ is a connection on $X$ restricting to $A_t$ on each slice, as required.
>
> **Split the exterior derivative on the product.** On $X$ the exterior derivative decomposes as $d_X = d_M + dt \wedge \partial_t$, where $d_M$ differentiates only in the $M$-directions and $dt \wedge \partial_t$ collects the $t$-derivative (this is the coordinate statement $d_X f = \sum_i \partial_{x^i} f\, dx^i + \partial_t f\, dt$ for functions, extended to forms by the Leibniz rule). Applying it to $\mathbb{A}$,
> $$d_X \mathbb{A} = \sum_i d_X a_i \wedge dx^i = \sum_i \big(d_M a_i + \partial_t a_i\, dt\big) \wedge dx^i = d_M A_t + dt \wedge \sum_i \partial_t a_i\, dx^i \qquad \text{(split of } d_X\text{; and } \partial_t a_i\, dt \wedge dx^i = dt \wedge \partial_t a_i\, dx^i)$$
> $$= d_M A_t + dt \wedge \dot{A}_t \qquad \text{(definition } \dot A_t = \partial_t A_t = \textstyle\sum_i \partial_t a_i\, dx^i).$$
> **Add the quadratic term.** Since $\mathbb{A}$ has no $dt$-component, $\mathbb{A} \wedge \mathbb{A}$ involves only the $dx^i$, so it equals $A_t \wedge A_t$ (the wedge of the spatial parts). Therefore, using the matrix-group curvature $F = d\mathbb{A} + \mathbb{A}\wedge\mathbb{A}$ from [[Def - Curvature of a Principal Connection|the curvature convention]],
> $$F_{\mathbb{A}} = d_X \mathbb{A} + \mathbb{A} \wedge \mathbb{A} = \big(d_M A_t + dt \wedge \dot{A}_t\big) + A_t \wedge A_t = \big(d_M A_t + A_t \wedge A_t\big) + dt \wedge \dot{A}_t \qquad \text{(regrouping)}$$
> $$= F_{A_t} + dt \wedge \dot{A}_t \qquad \text{(since } F_{A_t} = d_M A_t + A_t \wedge A_t \text{ is the slice curvature).}$$
> Here $F_{A_t}$ is a spatial two-form (no $dt$) and $dt \wedge \dot{A}_t$ carries exactly one $dt$.

**Step 2: Reduce $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}})$ to a single term.**

Expanding the square and discarding the terms that vanish by degree or by $dt \wedge dt = 0$ leaves
$$\operatorname{tr}\!\big(F_{\mathbb{A}} \wedge F_{\mathbb{A}}\big) = 2\, dt \wedge \operatorname{tr}\!\big(\dot{A}_t \wedge F_{A_t}\big).$$

> [!note]- Derivation
> Substitute $F_{\mathbb{A}} = F_{A_t} + dt \wedge \dot{A}_t$ and expand the wedge square into four terms:
> $$F_{\mathbb{A}} \wedge F_{\mathbb{A}} = F_{A_t} \wedge F_{A_t} \;+\; F_{A_t} \wedge (dt \wedge \dot{A}_t) \;+\; (dt \wedge \dot{A}_t) \wedge F_{A_t} \;+\; (dt \wedge \dot{A}_t) \wedge (dt \wedge \dot{A}_t).$$
> **First term vanishes by dimension.** $F_{A_t} \wedge F_{A_t}$ is a four-form built entirely from the $dx^i$, hence a section of $\Lambda^4 T^*M$; but $\dim M = 3$, so $\Lambda^4 T^*M = 0$ and $F_{A_t} \wedge F_{A_t} = 0$ (this is where the three-dimensionality of $M$ enters).
>
> **Fourth term vanishes by $dt \wedge dt = 0$.** The product $(dt \wedge \dot{A}_t) \wedge (dt \wedge \dot{A}_t)$ contains the factor $dt \wedge dt = 0$ (moving the second $dt$ left past the one-form $\dot A_t$ costs a sign but still lands two $dt$-factors together), so this term is $0$.
>
> **The two middle terms are equal.** In the second term, move $dt$ to the front past the two-form $F_{A_t}$: $F_{A_t} \wedge dt = (-1)^{2 \cdot 1}\, dt \wedge F_{A_t} = dt \wedge F_{A_t}$, so
> $$F_{A_t} \wedge (dt \wedge \dot{A}_t) = dt \wedge F_{A_t} \wedge \dot{A}_t.$$
> Now move $F_{A_t}$ (degree $2$) past $\dot{A}_t$ (degree $1$): $F_{A_t} \wedge \dot{A}_t = (-1)^{2 \cdot 1}\, \dot{A}_t \wedge F_{A_t} = \dot{A}_t \wedge F_{A_t}$, giving $F_{A_t} \wedge (dt \wedge \dot A_t) = dt \wedge \dot{A}_t \wedge F_{A_t}$. The third term is already $(dt \wedge \dot{A}_t) \wedge F_{A_t} = dt \wedge \dot{A}_t \wedge F_{A_t}$. Hence the two middle terms coincide, and
> $$F_{\mathbb{A}} \wedge F_{\mathbb{A}} = 2\, dt \wedge \dot{A}_t \wedge F_{A_t} \qquad \text{(sum of the two equal middle terms; first and fourth are zero).}$$
> **Take the trace.** The trace is linear and $dt$ is a scalar-valued form, so it factors out: $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}}) = 2\, dt \wedge \operatorname{tr}(\dot{A}_t \wedge F_{A_t})$, a three-form on $M$ wedged with $dt$.

**Step 3: Apply the transgression identity and Stokes to prove the integral form (assertion 1).**

The transgression identity makes $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}})$ exact on $X$; Stokes and the induced boundary orientations turn its integral into the endpoint difference of $\vartheta$.

> [!note]- Derivation
> **Transgress.** By the transgression identity (Haydys's (97)) from [[Thm - Transgression Formula and the Chern-Simons Form|the transgression theorem]], applied to the connection $\mathbb{A}$ on the four-manifold $X$,
> $$\operatorname{tr}\!\big(F_{\mathbb{A}} \wedge F_{\mathbb{A}}\big) = d\, \operatorname{cs}(\mathbb{A}), \qquad \operatorname{cs}(\mathbb{A}) = \operatorname{tr}\!\Big(\mathbb{A} \wedge d\mathbb{A} + \tfrac{2}{3}\, \mathbb{A} \wedge \mathbb{A} \wedge \mathbb{A}\Big) \in \Omega^3(X).$$
> **Integrate and apply Stokes.** $X = M \times [t_0, t_1]$ is a compact oriented four-manifold with boundary and $\operatorname{cs}(\mathbb{A})$ is a smooth three-form on it, so [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] gives
> $$\int_X \operatorname{tr}\!\big(F_{\mathbb{A}} \wedge F_{\mathbb{A}}\big) = \int_X d\, \operatorname{cs}(\mathbb{A}) = \int_{\partial X} \operatorname{cs}(\mathbb{A}) \qquad \text{(transgression identity, then Stokes).}$$
> **Identify the boundary with orientations.** Because $M$ is closed, $\partial X = (M \times \{t_1\}) \sqcup (M \times \{t_0\})$ (there is no side boundary). Orient $X$ by $\mathrm{vol}_X = dt \wedge \mathrm{vol}_M$, as fixed in the problem. On the top slice the outward normal is $\nu = +\partial_t$; the "outward normal first" rule from [[Def - Manifold with Boundary and Induced Orientation|the induced-orientation definition]] declares $(v_1, v_2, v_3)$ positive on $M \times \{t_1\}$ exactly when $(\partial_t, v_1, v_2, v_3)$ is positive in $X$, i.e. exactly when $(v_1, v_2, v_3)$ is positive for $M$; so the top slice carries the orientation $+M$. On the bottom slice the outward normal is $\nu = -\partial_t$, and $(-\partial_t, v_1, v_2, v_3)$ is positive in $X$ exactly when $(\partial_t, v_1, v_2, v_3)$ is negative, i.e. exactly when $(v_1, v_2, v_3)$ is negative for $M$; so the bottom slice carries $-M$.
>
> **Pull back to each slice.** For the inclusion $\iota_t : M \to X$, $\iota_t^* \mathbb{A} = A_t$ (Step 1), and since pull-back commutes with $d$, with $\wedge$, and with the trace, $\iota_t^* \operatorname{cs}(\mathbb{A}) = \operatorname{cs}(\iota_t^*\mathbb{A}) = \operatorname{cs}(A_t)$. Therefore, integrating over the two oriented slices,
> $$\int_{\partial X} \operatorname{cs}(\mathbb{A}) = \int_{M \times \{t_1\}} \operatorname{cs}(\mathbb{A}) + \int_{M \times \{t_0\}} \operatorname{cs}(\mathbb{A}) = \int_M \operatorname{cs}(A_{t_1}) - \int_M \operatorname{cs}(A_{t_0}) \qquad \text{(top slice }=+M\text{, bottom slice }=-M\text{, and }\iota_t^*\operatorname{cs}(\mathbb{A})=\operatorname{cs}(A_t)).$$
> **Divide by $8\pi^2$.** By the definition $\vartheta(A) = \tfrac{1}{8\pi^2}\int_M \operatorname{cs}(A)$,
> $$\int_M \operatorname{cs}(A_{t_1}) - \int_M \operatorname{cs}(A_{t_0}) = 8\pi^2\big(\vartheta(A_{t_1}) - \vartheta(A_{t_0})\big).$$
> Combining the three displayed equalities,
> $$8\pi^2\big(\vartheta(A_{t_1}) - \vartheta(A_{t_0})\big) = \int_X \operatorname{tr}\!\big(F_{\mathbb{A}} \wedge F_{\mathbb{A}}\big), \qquad\text{i.e.}\qquad \vartheta(A_{t_1}) - \vartheta(A_{t_0}) = \frac{1}{8\pi^2}\int_{M \times [t_0, t_1]} \operatorname{tr}\!\big(F_{\mathbb{A}} \wedge F_{\mathbb{A}}\big).$$
> This is assertion 1, and it is exactly part (c) of [[Thm - The Four-Dimensional Formula for the Chern-Simons Functional|the four-dimensional formula theorem]], now proved directly by Stokes on the cylinder.

**Step 4: Fubini and the fundamental theorem of calculus give the differential form (assertion 2).**

Feeding the reduced integrand of Step 2 into the identity of Step 3, integrating over the interval, and differentiating in the upper limit yields $\tfrac{d}{dt}\vartheta(A_t) = \tfrac{1}{4\pi^2}\int_M \operatorname{tr}(F_{A_t} \wedge \dot{A}_t)$.

> [!note]- Derivation
> **Fubini over the interval.** By Step 2 the bulk integrand is $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}}) = 2\, dt \wedge \operatorname{tr}(\dot{A}_t \wedge F_{A_t})$. For the product orientation $\mathrm{vol}_X = dt \wedge \mathrm{vol}_M$, integration of a form of the type $dt \wedge \beta_t$ (with $\beta_t$ a three-form on $M$ depending smoothly on $t$) factors as $\int_X dt \wedge \beta_t = \int_{t_0}^{t_1}\big(\int_M \beta_t\big)\, dt$ (Fubini for the product measure with this orientation ordering). Applying it with $\beta_t = 2\operatorname{tr}(\dot A_t \wedge F_{A_t})$ and using Step 3,
> $$8\pi^2\big(\vartheta(A_{t_1}) - \vartheta(A_{t_0})\big) = \int_X \operatorname{tr}\!\big(F_{\mathbb{A}} \wedge F_{\mathbb{A}}\big) = \int_{t_0}^{t_1} \Big(\int_M 2\, \operatorname{tr}(\dot{A}_s \wedge F_{A_s})\Big)\, ds.$$
> **Differentiate in the upper limit.** The identity holds for every choice of endpoints, so replace $t_1$ by a free variable $t \in [t_0, t_1]$:
> $$8\pi^2\big(\vartheta(A_t) - \vartheta(A_{t_0})\big) = \int_{t_0}^{t} \Big(\int_M 2\, \operatorname{tr}(\dot{A}_s \wedge F_{A_s})\Big)\, ds.$$
> The integrand $s \mapsto \int_M 2\operatorname{tr}(\dot A_s \wedge F_{A_s})$ is continuous in $s$ (it is a smooth function of $s$, since $A_s$ is smooth in $s$ and $M$ is compact), so the fundamental theorem of calculus applies and, differentiating both sides in $t$ (the $\vartheta(A_{t_0})$ term is constant),
> $$8\pi^2\, \frac{d}{dt}\vartheta(A_t) = \int_M 2\, \operatorname{tr}(\dot{A}_t \wedge F_{A_t}), \qquad\text{i.e.}\qquad \frac{d}{dt}\vartheta(A_t) = \frac{1}{4\pi^2}\int_M \operatorname{tr}(\dot{A}_t \wedge F_{A_t}).$$
> **Match the critical-point formula's sign.** Move $F_{A_t}$ (degree $2$) past $\dot{A}_t$ (degree $1$) under the trace: $\operatorname{tr}(\dot{A}_t \wedge F_{A_t}) = (-1)^{2 \cdot 1}\, \operatorname{tr}(F_{A_t} \wedge \dot{A}_t) = \operatorname{tr}(F_{A_t} \wedge \dot{A}_t)$ (no sign), so
> $$\frac{d}{dt}\vartheta(A_t) = \frac{1}{4\pi^2}\int_M \operatorname{tr}(F_{A_t} \wedge \dot{A}_t).$$
> This is exactly $d\vartheta_A(a) = \tfrac{1}{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a)$ from [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|the critical-point theorem]], evaluated at $A = A_t$ and the tangent vector $a = \dot{A}_t$ — as it must be, since $\tfrac{d}{dt}\vartheta(A_t)$ is the directional derivative of $\vartheta$ along the path's velocity.

> [!note]- Complete formal solution
> **Claim.** Let $M$ be a closed oriented three-manifold, $A_t \in \Omega^1(M; \mathfrak{su}(2))$ a smooth path of connections for $t \in [t_0, t_1]$, and $X = M \times [t_0, t_1]$ oriented by $\mathrm{vol}_X = dt \wedge \mathrm{vol}_M$. Let $\mathbb{A}$ be the temporal-gauge connection on $X$ with $\iota_t^*\mathbb{A} = A_t$. Then
> $$\vartheta(A_{t_1}) - \vartheta(A_{t_0}) = \frac{1}{8\pi^2}\int_X \operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}}) \qquad\text{and}\qquad \frac{d}{dt}\vartheta(A_t) = \frac{1}{4\pi^2}\int_M \operatorname{tr}(F_{A_t} \wedge \dot{A}_t).$$
>
> In local coordinates $A_t = \sum_i a_i(x,t)\, dx^i$, set $\mathbb{A} = \sum_i a_i(x,t)\, dx^i \in \Omega^1(X;\mathfrak{su}(2))$ (no $dt$-term). With $d_X = d_M + dt \wedge \partial_t$,
> $$F_{\mathbb{A}} = d_X\mathbb{A} + \mathbb{A}\wedge\mathbb{A} = (d_M A_t + A_t \wedge A_t) + dt \wedge \dot{A}_t = F_{A_t} + dt \wedge \dot{A}_t.$$
> Squaring and using $\Lambda^4 T^*M = 0$ (so $F_{A_t}\wedge F_{A_t} = 0$), $dt \wedge dt = 0$, and $\operatorname{tr}(\alpha\wedge\beta) = (-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)$,
> $$\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}}) = 2\, dt \wedge \operatorname{tr}(\dot{A}_t \wedge F_{A_t}).$$
> By the transgression identity $\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}}) = d\,\operatorname{cs}(\mathbb{A})$, and by Stokes on $X$,
> $$\int_X \operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}}) = \int_{\partial X} \operatorname{cs}(\mathbb{A}).$$
> Since $M$ is closed, $\partial X$ is the two end slices; the orientation $dt \wedge \mathrm{vol}_M$ makes the top slice $+M$ and the bottom slice $-M$, and $\iota_t^*\operatorname{cs}(\mathbb{A}) = \operatorname{cs}(A_t)$ by naturality, so
> $$\int_{\partial X}\operatorname{cs}(\mathbb{A}) = \int_M \operatorname{cs}(A_{t_1}) - \int_M \operatorname{cs}(A_{t_0}) = 8\pi^2\big(\vartheta(A_{t_1}) - \vartheta(A_{t_0})\big).$$
> This proves the integral identity. For the differential identity, Fubini for the product orientation gives $\int_X dt \wedge \beta_t = \int_{t_0}^{t_1}(\int_M \beta_t)\, dt$; applied with $\beta_t = 2\operatorname{tr}(\dot A_t \wedge F_{A_t})$ and with $t_1$ replaced by a free upper limit $t$,
> $$8\pi^2\big(\vartheta(A_t) - \vartheta(A_{t_0})\big) = \int_{t_0}^{t}\Big(\int_M 2\,\operatorname{tr}(\dot A_s \wedge F_{A_s})\Big)\, ds.$$
> The integrand is continuous in $s$, so the fundamental theorem of calculus gives $8\pi^2\,\tfrac{d}{dt}\vartheta(A_t) = \int_M 2\,\operatorname{tr}(\dot A_t \wedge F_{A_t})$; moving $F_{A_t}$ past $\dot A_t$ under the trace (no sign, degrees $2$ and $1$) yields $\tfrac{d}{dt}\vartheta(A_t) = \tfrac{1}{4\pi^2}\int_M \operatorname{tr}(F_{A_t} \wedge \dot A_t)$, the critical-point differential at $a = \dot A_t$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to argue "$\operatorname{tr}(F_{\mathbb{A}} \wedge F_{\mathbb{A}})$ is closed and $H^4_{dR}(X) \cong H^4_{dR}(M) = 0$ since $M$ is three-dimensional and $X$ deformation-retracts to $M$, so the integral over $X$ is zero", and conclude $\vartheta(A_{t_1}) = \vartheta(A_{t_0})$. This is false: $X$ has boundary, so the integral of an exact top-form is *not* zero — it is the boundary integral $\int_{\partial X}\operatorname{cs}(\mathbb{A})$, which is exactly the nonzero endpoint difference. Vanishing of $\int_X d\eta$ requires $\partial X = \emptyset$; on a manifold with boundary Stokes turns the bulk integral into a boundary term, and that term is the whole content of the identity. The homotopy-invariance intuition applies to *closed* manifolds only.

---

# Key Takeaways

**A difference of a functional at two endpoints of a path is an integral over the mapping cylinder, computed by Stokes on the primitive.** The reusable principle is that a Chern–Simons-type functional $\vartheta(A) = \tfrac{1}{8\pi^2}\int_M \operatorname{cs}(A)$ whose integrand has an exact "square" — here $\operatorname{tr}(F\wedge F) = d\,\operatorname{cs}$ — turns *comparison along a path* into a *bulk integral of the Chern character density* over $M \times [t_0, t_1]$. The trigger to reach for this move is the co-occurrence of two features: a functional built from a primitive $\operatorname{cs}$, and a family of connections you want to compare. The transferable diagnostic is to ask "what is $d$ of my integrand, and does the region between the endpoints have that $d$-image as its natural bulk integrand?" When the answer is yes, form the cylinder, put the family in temporal gauge, and let Stokes do the comparison. The same construction underlies the statement that Chern–Simons is the boundary term of the four-dimensional Yang–Mills / second-Chern action, and it is the geometric origin of instanton Floer theory, where the flow lines between critical points of $\vartheta$ are precisely anti-self-dual connections on the cylinder $M \times \mathbb{R}$.

**Temporal gauge is the canonical way to promote a path of connections on $M$ to a single connection on $M \times I$, and it makes the curvature split cleanly.** The decision to take $\mathbb{A}$ with no $dt$-component is not a loss of generality: any connection on the cylinder restricting to the given slices produces the same endpoint difference (the left-hand side depends only on the endpoints) and the same $\operatorname{tr}(F\wedge F)$-integral (which computes a relative characteristic number), so the temporal-gauge representative is chosen purely because it is computable. Its payoff is the split $F_{\mathbb{A}} = F_{A_t} + dt \wedge \dot{A}_t$: the spatial part is the honest slice curvature and the $dt$-part is the velocity of the path. This split is the workhorse of every "energy along a path" computation in gauge theory — the Yang–Mills energy of a path, the symplectic action, the spectral flow of a family of Dirac operators — and recognising it lets you read off the interpolating four-dimensional object's curvature without any coordinate labour beyond one exterior derivative.

**Three-dimensionality of $M$ is exactly what makes the square of the curvature collapse to a single velocity term, and closedness of $M$ is exactly what makes the boundary the two end slices.** These two hypotheses are not cosmetic. Because $\dim M = 3$, the purely spatial four-form $F_{A_t}\wedge F_{A_t}$ dies, so $\operatorname{tr}(F_{\mathbb{A}}\wedge F_{\mathbb{A}})$ reduces to $2\, dt \wedge \operatorname{tr}(\dot A_t \wedge F_{A_t})$ — a term *linear* in the velocity, which is precisely why differentiating gives back the first variation and why $\vartheta$ has a well-defined gradient flow. Because $M$ is closed, $\partial(M\times[t_0,t_1])$ has no side wall $\partial M \times [t_0,t_1]$, so the boundary integral is a pure endpoint difference with no cross-terms. When you meet a variant — a four-dimensional base, or a manifold with boundary — expect exactly these two simplifications to fail, and expect the extra surviving terms (a genuine $\operatorname{tr}(F\wedge F)$ contribution, or a boundary flux along $\partial M$) to be the whole difference between the clean identity and the general case. The companion drills [[Ex - The Chern-Simons Form Transgresses the Second Chern Form]] and [[Ex - The Differential of the Chern-Simons Functional]] isolate, respectively, the transgression identity and the first-variation computation used here.
