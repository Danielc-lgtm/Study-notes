---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Closed and Exact Forms"
  - "Def - de Rham Cohomology"
tags: [geometry, differential-geometry, cohomology, poincare-lemma]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open. $U$ is **star-shaped** about a point $c \in U$ if for every $x \in U$ the segment $\{c + t(x - c) : t \in [0, 1]\}$ lies in $U$; **convex** sets are star-shaped about every point, and balls and rectangles are convex. $\mathbb{H}^n = \{x \in \mathbb{R}^n : x^n \geq 0\}$ is the upper half-space. A $k$-form $\omega \in \Omega^k(U)$ is **closed** if $d\omega = 0$ and **exact** if $\omega = d\beta$ for some $(k-1)$-form $\beta$ on $U$, called a **primitive**. The de Rham cohomology $H^k_{dR}(U)$ is the quotient $Z^k(U) / B^k(U)$ — see [[Def - de Rham Cohomology]].

---

# Statement

> **Theorem ([[Thm - The Poincaré Lemma|Poincaré Lemma]] on a Star-Shaped Region).** Let $U \subseteq \mathbb{R}^n$ or $U \subseteq \mathbb{H}^n$ be an open star-shaped set. Then for every $k \geq 1$:
> $$H^k_{dR}(U) = 0.$$
> Equivalently, every closed $k$-form on $U$ is exact: if $\omega \in \Omega^k(U)$ satisfies $d\omega = 0$ with $k \geq 1$, there exists $\beta \in \Omega^{k-1}(U)$ with $\omega = d\beta$.

> **Corollary (Cohomology of contractible manifolds).** If $M$ is a contractible smooth manifold, $H^k_{dR}(M) = 0$ for every $k \geq 1$. In particular, $H^k_{dR}(\mathbb{R}^n) = 0$ and $H^k_{dR}(\mathbb{H}^n) = 0$ for $k \geq 1$.

> **Corollary (Local exactness).** For any smooth manifold $M$ and any $p \in M$, there is a neighborhood of $p$ on which every closed form is exact. (Apply the Poincaré lemma in a chart diffeomorphic to a ball.)

The $1$-form version on $\mathbb{R}^n$ is [[Thm - The Poincaré Lemma]] from `Multivariate Analysis IV`; this theorem generalizes from $1$-forms to all degrees, and from $\mathbb{R}^n$ to contractible (via [[Thm - Homotopy Invariance of de Rham Cohomology]]).

---

# Motivation

The basic question is whether the local construction of a primitive function, available for closed $1$-forms on $\mathbb{R}^n$ via the Fundamental Theorem of Calculus (integrate along straight lines from a basepoint), has a higher-degree analogue. For closed $1$-forms on $\mathbb{R}^n$ — the [[Thm - The Poincaré Lemma|Euclidean Poincaré lemma]] of `Multivariate Analysis IV` — the answer is yes, and the explicit primitive is $f(x) = \int_0^1 \sum_j F_j(tx) x_j \, dt$. For higher-degree forms we need to generalize this construction.

The conceptual content of the theorem is that *closedness is locally enough for exactness*. Equivalently: *all obstructions to exactness are global*. The de Rham cohomology of a contractible domain vanishes in positive degrees because there is no global topology — no holes, no loops — for an obstruction to hide in. The Poincaré lemma is the foundation of every de Rham computation, because it says cohomology can be patched together from local pieces, each of which is trivial.

The reason the lemma is stated on *star-shaped* (rather than just convex, or just simply connected) sets is that the proof needs a *canonical contraction* — a [[Def - Homotopy|homotopy]] from the identity to a constant — and star-shapedness gives the simplest such contraction, the radial straight-line scaling $H(x, t) = c + t(x - c)$. The full statement, that any contractible domain has trivial positive-degree cohomology, then follows by combining the star-shaped case with [[Thm - Homotopy Invariance of de Rham Cohomology]]: contractibility says there is *some* [[Def - Homotopy|homotopy]] from the identity to a constant, and homotopy invariance then transfers the star-shaped result to the general contractible setting.

The lemma is *false* without contractibility. The standing counterexample, since [[Thm - The Poincaré Lemma|Multivariate Analysis IV]], is the angular form $d\theta = (-y\,dx + x\,dy)/(x^2 + y^2)$ on $\mathbb{R}^2 \setminus \{0\}$: closed everywhere, but $\int_{S^1} d\theta = 2\pi \neq 0$, so $d\theta$ is not exact. The hole at the origin carries a non-trivial cohomology class, and the punctured plane is not contractible. So the Poincaré lemma is both a positive existence result (when the hypothesis holds) and a sharp characterization (without contractibility, all bets are off).

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$\omega$ is closed and $U$ is contractible.* The skill is recognizing both halves in disguise.

The first disguised source is **a $k$-form whose coefficients satisfy a system of mixed-partial conditions, on a ball or convex domain.** Property $B$: the coefficients $f_I$ of $\omega = \sum_I f_I dx^I$ satisfy the integrability identities making $d\omega = 0$ (which for $1$-forms is the symmetry $\partial_i f_j = \partial_j f_i$, for $2$-forms the cyclic identities, etc.). On a ball, these PDE-style conditions imply exactness — there is a $(k-1)$-form whose exterior derivative is $\omega$, equivalently a system of compatible primitive equations is solvable. This is the source pattern in which the lemma is recognized as a *PDE existence result*.

The second disguised source is **a closed form on a manifold with a contractible cover.** Property $B$: the manifold $M$ admits a cover by open sets $\{U_\alpha\}$ each diffeomorphic to a ball (a "good cover"). The bridge: on each $U_\alpha$ the Poincaré lemma gives a local primitive $\beta_\alpha$, and the global existence question reduces to whether the local primitives glue. The non-obvious step is recognizing that the cohomology of $M$ is encoded entirely in the *gluing data* of these local primitives, not in their existence. This is the input pattern that motivates Mayer–Vietoris and Čech-de Rham.

The third disguised source is **a homotopy equivalence to a star-shaped or convex domain.** Property $B$: a smooth map $F : V \to U$ from your domain $V$ to a star-shaped $U$, with smooth homotopy inverse. The bridge: by [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance]], $H^*_{dR}(V) \cong H^*_{dR}(U) = 0$ in positive degrees. The application: extracting the Poincaré-lemma conclusion for domains that are not literally star-shaped but only have the same homotopy type. For instance, $\mathbb{R}^n$ minus a ray (not convex but star-shaped about a point off the ray), or the complement of any closed contractible set in a convex domain.

**Targets (Output Amplification)**

The conclusion $C$: *every closed $k$-form on $U$ is exact for $k \geq 1$, with an explicit primitive given by the homotopy operator.*

Combine $C$ with **the explicit form of the homotopy operator.** On a star-shaped domain, the homotopy operator is $h\omega = \int_0^1 \iota_X \omega \circ H_t^* \, dt$, where $X$ is the radial vector field and $H_t$ is the contraction; for a closed $1$-form $\omega = \sum F_j dx^j$, this explicitly gives the primitive $f(x) = \int_0^1 \sum F_j(tx) x_j \, dt$. The further result $E$ is a *constructive* solution to the PDE system "$df = \omega$" or "$d\beta = \omega$" — not just existence but an integral formula. The non-obviousness: the formula tells you *what* the primitive is, not just that one exists.

Combine $C$ with **the existence of a good cover** (a cover by open sets each diffeomorphic to a contractible domain, with all finite intersections also contractible). The further result $E$ is the **Čech–de Rham spectral sequence**: cohomology of $M$ is computed entirely from the combinatorics of the cover, with each cohomology contribution coming purely from the gluing data. The non-obvious payoff: a local existence theorem becomes the foundation of a global classification of cohomology.

Combine $C$ with **the differential of the boundary inclusion.** For a manifold with boundary $M$, the Poincaré lemma applied to a tubular neighborhood of $\partial M$ in $M$ (which is homotopy equivalent to $\partial M \times [0, 1)$, hence to $\partial M$) plus extension lemmas gives that closed forms near the boundary are essentially determined by their boundary restriction. The further result $E$: cohomology can be computed by "doubling" — gluing $M$ to itself along $\partial M$ — in the same way Mayer–Vietoris computes cohomology of unions.

---

# Why Is It True

**The single sentence: the homotopy operator $h$ satisfies $dh + hd = \mathrm{id}$ on positive-degree forms; applied to a closed form, this reads $\omega = d(h\omega)$, exhibiting $h\omega$ as the primitive.**

The argument has three movements. *First*, on a star-shaped domain there is a canonical contraction $H : U \times [0, 1] \to U$, $H(x, t) = c + t(x - c)$, smoothly deforming the identity ($t = 1$) to the constant map at $c$ ($t = 0$). This is the geometric input that lets us define a homotopy operator at all.

*Second*, the contraction induces, on the algebra of forms, a *chain homotopy* operator $h : \Omega^k(U) \to \Omega^{k-1}(U)$, built by integration along the homotopy. Concretely, for a form $\omega$, define $h\omega = \int_0^1 \iota_S H^*\omega \, dt$, where $S$ is the vector field $\partial_t$ on $U \times I$ and $\iota_S$ is interior product. This $h$ is the algebraic shadow of the geometric contraction $H$.

*Third*, the homotopy operator satisfies the **chain homotopy identity**

$$d h + h d = H_1^* - H_0^* = \mathrm{id}^* - c^* = \mathrm{id} - c^*,$$

where $c^*$ is the pullback by the constant map at $c$, which on positive-degree forms is zero (since the constant map factors through a point, and there are no forms of positive degree on a point). So on positive-degree forms, $dh + hd = \mathrm{id}$.

The conclusion is immediate. For a closed $\omega$ (i.e. $d\omega = 0$) of degree $k \geq 1$,

$$\omega = (dh + hd)(\omega) = d(h\omega) + h(d\omega) = d(h\omega) + 0 = d(h\omega),$$

so $h\omega$ is a primitive of $\omega$, exhibiting $\omega$ as exact.

The chain homotopy identity $dh + hd = \mathrm{id} - c^*$ has a beautiful conceptual meaning. It says the algebraic operation $dh + hd$ (which mixes "antiderivative" $h$ with "derivative" $d$) is the *identity minus a constant projection*. On forms of positive degree the constant projection vanishes, so $dh + hd = \mathrm{id}$ — every form $\omega$ is canonically a "boundary of its antiderivative plus an antiderivative of its boundary." For closed $\omega$ the second summand vanishes, and what remains is the exactness $\omega = d(h\omega)$.

This generalizes to general contractible domains via [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance]]: any homotopy from $\mathrm{id}_M$ to a constant map gives an analogous homotopy operator, and the identity $dh + hd = \mathrm{id} - (\text{constant pullback})$ continues to hold. The constant pullback being zero on positive-degree forms gives $\omega = d(h\omega)$ exactly as before.

---

# What Makes This Hard

The conceptual obstacle is believing that **closedness is not always enough** — the lemma is *false* without contractibility, and the angular form $d\theta$ on the punctured plane is the standing counterexample. In the proof, the non-obvious step is the **construction of the homotopy operator**: writing down a canonical integral expression for $h\omega$ that satisfies $dh + hd = \mathrm{id}$ requires recognizing that integration along the contraction parameter $t$ is the natural way to "invert" $d$ on the form level. The most common error is to expect the formula to work without using the closedness hypothesis — but $h$ is well-defined on *all* forms; what is special about closed ones is that the term $h(d\omega)$ vanishes, leaving $\omega = d(h\omega)$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Construct a homotopy operator $h$ from a contraction; verify that it satisfies the chain homotopy identity $dh + hd = \mathrm{id}$ on positive-degree forms (the constant-pullback term vanishing for degree reasons); apply this to a closed form to extract a primitive.

**Subgoal decomposition:**

1. **Define the homotopy.** Set $H : U \times I \to U$, $H(x, t) = c + t(x - c)$, with $c$ the center of star-shapedness. So $H(\cdot, 1) = \mathrm{id}$ and $H(\cdot, 0) = c$ (the constant map at $c$).
   - *Hint:* Star-shapedness is precisely what makes this $H$ land in $U$ for every $(x, t) \in U \times I$.
   - *Why needed:* The homotopy operator is built by integrating against this homotopy.

2. **Define the homotopy operator.** For $\omega \in \Omega^k(U)$, define $h\omega \in \Omega^{k-1}(U)$ by
   $$h\omega = \int_0^1 \iota_{\partial_t}(H^*\omega) \, dt,$$
   where $\iota_{\partial_t}$ contracts with the $t$-direction vector field on $U \times I$.
   - *Hint:* The pullback $H^*\omega$ is a form on $U \times I$; contracting with $\partial_t$ drops degree by one and produces a form on $U$ (after integrating over $t \in [0, 1]$).
   - *Why needed:* This $h$ is the candidate primitive operator.

3. **Verify the chain homotopy identity.** Compute $dh + hd$ on a general form $\omega$, using Cartan's magic formula $\mathcal{L}_X = d \iota_X + \iota_X d$ applied to the vector field $\partial_t$ on $U \times I$, plus the Fundamental Theorem of Calculus.
   - *Hint:* $\int_0^1 \mathcal{L}_{\partial_t} H^*\omega \, dt = \int_0^1 \partial_t (H^*\omega) \, dt = H_1^*\omega - H_0^*\omega$.
   - *Why needed:* The identity $dh + hd = H_1^* - H_0^*$ is what lets us conclude $\omega = d(h\omega)$ for closed $\omega$.

4. **Apply to closed forms.** For closed $\omega$ of degree $k \geq 1$: $H_1^*\omega = \omega$ (since $H_1 = \mathrm{id}$); $H_0^*\omega = 0$ (since $H_0$ is constant and $\omega$ has positive degree). So $dh\omega + hd\omega = \omega - 0 = \omega$. Since $d\omega = 0$, this gives $d(h\omega) = \omega$.
   - *Hint:* "Constant pullback of a positive-degree form is zero" is the lemma that kills the boundary term.
   - *Why needed:* This is the conclusion — $h\omega$ is the primitive.

---

# Lemma Decomposition

> [!note]- Lemma 1: Constant pullback annihilates positive-degree forms
> **Statement:** Let $c : U \to U$ be a constant map, $c(x) = c_0$ for all $x$, and let $\omega \in \Omega^k(U)$ with $k \geq 1$. Then $c^*\omega = 0$.
>
> **Hint:** Compute $c^*\omega$ using the formula for pullback of a form via a smooth map, and observe that the differential of a constant map is zero.
>
> **Why needed:** This is what makes the right side of the chain homotopy identity $dh + hd = H_1^* - H_0^*$ reduce to just $\mathrm{id} = H_1^*$ on positive-degree closed forms.
>
> > [!note]- Full proof
> > For any smooth map $F : U \to V$ and any form $\omega \in \Omega^k(V)$ with $k \geq 1$, the pullback is $(F^*\omega)_x(v_1, \dots, v_k) = \omega_{F(x)}(dF_x(v_1), \dots, dF_x(v_k))$. For $F = c$ constant, $dc_x = 0$ everywhere (the differential of a constant map is zero), so $dc_x(v_i) = 0$ for every $i$, and $(c^*\omega)_x(v_1, \dots, v_k) = \omega_{c_0}(0, 0, \dots, 0) = 0$ since $\omega_{c_0}$ is multilinear. Hence $c^*\omega = 0$.

> [!note]- Lemma 2: Cartan's magic formula and differentiation under the integral
> **Statement:** For a smooth $k$-form $\omega$ on $U \times I$, $\mathcal{L}_{\partial_t}\omega = d \iota_{\partial_t} \omega + \iota_{\partial_t} d\omega$, and $\int_0^1 \mathcal{L}_{\partial_t}\omega \, dt = \omega|_{t=1} - \omega|_{t=0}$ as forms on $U$ (after restriction).
>
> **Hint:** Cartan's magic formula is [[Thm - Cartan's Magic Formula]] from `Differential Geometry VIII`. The integration formula follows from the Fundamental Theorem of Calculus applied componentwise.
>
> **Why needed:** It is the key identity that converts $dh + hd$ into a boundary expression $H_1^* - H_0^*$.
>
> > [!note]- Full proof
> > Cartan's magic formula $\mathcal{L}_X = d\iota_X + \iota_X d$ is a general identity on forms for any vector field $X$; see [[Thm - Cartan's Magic Formula]]. For $X = \partial_t$, this gives $\mathcal{L}_{\partial_t}\omega = d\iota_{\partial_t}\omega + \iota_{\partial_t}d\omega$.
> >
> > For the integration: $\mathcal{L}_{\partial_t}\omega$ at a point is the $t$-derivative of $\omega$ along the integral curves of $\partial_t$, which are just $t \mapsto (x, t)$. So $\mathcal{L}_{\partial_t}\omega(x, t)$ is the $t$-partial of $\omega(x, t)$ (computed in any coordinates). By Fundamental Theorem of Calculus, $\int_0^1 (\partial_t \omega)(x, t)\,dt = \omega(x, 1) - \omega(x, 0)$. In terms of pullbacks by $i_t : U \hookrightarrow U \times I$, this is $i_1^*\omega - i_0^*\omega$.

> [!note]- Lemma 3: The chain homotopy identity
> **Statement:** Let $H : U \times I \to U$ be a smooth homotopy, $H_t = H(\cdot, t)$, and define $h\omega = \int_0^1 i_t^*\iota_{\partial_t}H^*\omega \, dt$ where $i_t : U \to U \times I$, $i_t(x) = (x, t)$. Then on any $k$-form $\omega$ on $U$:
> $$dh\omega + hd\omega = H_1^*\omega - H_0^*\omega.$$
>
> **Hint:** Apply Lemma 2 to $H^*\omega$, using that $H^*$ commutes with $d$, and use Lemma 1 to recognize the resulting boundary terms.
>
> **Why needed:** This is the main computational identity that turns the geometric homotopy into the algebraic chain homotopy.
>
> > [!note]- Full proof
> > Write $\tilde\omega = H^*\omega$ on $U \times I$. By Lemma 2,
> > $$\mathcal{L}_{\partial_t}\tilde\omega = d\iota_{\partial_t}\tilde\omega + \iota_{\partial_t}d\tilde\omega = d\iota_{\partial_t}\tilde\omega + \iota_{\partial_t}H^*d\omega,$$
> > using that pullback commutes with $d$. Integrating over $t \in [0, 1]$ and using Fundamental Theorem of Calculus on the left side:
> > $$\int_0^1 \mathcal{L}_{\partial_t}\tilde\omega \, dt = i_1^*\tilde\omega - i_0^*\tilde\omega = (H \circ i_1)^*\omega - (H \circ i_0)^*\omega = H_1^*\omega - H_0^*\omega.$$
> > On the right side:
> > $$\int_0^1 d\iota_{\partial_t}\tilde\omega \, dt + \int_0^1 \iota_{\partial_t}H^*d\omega \, dt = d \int_0^1 \iota_{\partial_t}\tilde\omega \, dt + \int_0^1 \iota_{\partial_t}H^*d\omega \, dt = dh\omega + hd\omega,$$
> > where $d$ moves outside the $t$-integral by differentiation-under-the-integral.
> > Combining yields $dh\omega + hd\omega = H_1^*\omega - H_0^*\omega$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $U \subseteq \mathbb{R}^n$ be open and star-shaped about $c$, and let $\omega \in \Omega^k(U)$ with $k \geq 1$ be closed (i.e. $d\omega = 0$). We construct a $(k-1)$-form $\beta$ on $U$ with $d\beta = \omega$.
>
> **Step 1 — Define the contraction.** Set $H : U \times \mathbb{R} \to U$ by $H(x, t) = c + t(x - c)$. Star-shapedness of $U$ ensures $H(x, t) \in U$ for $(x, t) \in U \times [0, 1]$. Then $H(\cdot, 1) = \mathrm{id}_U$ and $H(\cdot, 0) = c$ (constant map at $c$).
>
> **Step 2 — Define the homotopy operator.** For $\eta \in \Omega^p(U \times I)$, write $\eta = \eta_1 + dt \wedge \eta_2$ uniquely, where $\eta_1$ and $\eta_2$ involve no $dt$ factors (i.e., $\iota_{\partial_t}\eta_1 = 0$, $\iota_{\partial_t}\eta_2 = 0$, so $\iota_{\partial_t}\eta = \eta_2$). Define $h : \Omega^k(U) \to \Omega^{k-1}(U)$ by
> $$h\omega = \int_0^1 i_t^*\iota_{\partial_t}H^*\omega \, dt,$$
> integrating the $(k-1)$-form-on-$U$-valued function of $t$ over $[0, 1]$.
>
> **Step 3 — Apply Cartan's magic formula and Fundamental Theorem of Calculus.** By Lemma 3,
> $$dh\omega + hd\omega = H_1^*\omega - H_0^*\omega.$$
>
> **Step 4 — Use the hypotheses.** Since $d\omega = 0$, $hd\omega = 0$. Since $H_1 = \mathrm{id}$, $H_1^*\omega = \omega$. Since $H_0$ is constant and $k \geq 1$, $H_0^*\omega = 0$ (Lemma 1). Hence
> $$dh\omega = \omega.$$
>
> Setting $\beta = h\omega$, we have $\beta \in \Omega^{k-1}(U)$ and $d\beta = \omega$. So $\omega$ is exact. $\blacksquare$
>
> **Explicit formula in degree 1.** For $\omega = \sum_j F_j\,dx^j$ a closed $1$-form on a domain star-shaped about $0$, the formula reduces to
> $$h\omega(x) = \int_0^1 \sum_j F_j(tx) x_j \, dt,$$
> recovering the $1$-form Poincaré lemma of `Multivariate Analysis IV`.

---

# Cross-Field Exercise Suggestions

**Electromagnetic four-potential.** In a contractible region of Minkowski spacetime, the Maxwell field $F$ (a $2$-form) is closed by the homogeneous Maxwell equation $dF = 0$. The Poincaré lemma then produces a $1$-form $A$ — the **four-potential** — with $F = dA$. The non-uniqueness $A \mapsto A + d\chi$ is the gauge freedom of electromagnetism, exactly the non-uniqueness of primitives in the lemma. This is the foundation of gauge theory.

**Thermodynamic state functions.** In thermodynamics, infinitesimal heat $\delta Q$ is a $1$-form on the state space; it is *not* closed (entropy generation), but the form $\delta Q / T$ (where $T$ is temperature) *is* closed, and on a contractible state space the Poincaré lemma produces a primitive $S$ — the **entropy** — with $dS = \delta Q / T$. The existence of the entropy function is the Poincaré lemma applied to the rescaled heat $1$-form on a contractible thermodynamic state space.

**Hodge theory and harmonic representatives.** On a compact Riemannian manifold, the Poincaré lemma plus the Hodge decomposition theorem produces, for every closed form $\omega$, a unique *harmonic* representative in $[\omega]$: there is a function $f$ with $\Delta f = d^*\omega$ (existence by Hodge theory), and $\omega - df^*$ is harmonic. The Poincaré lemma underwrites the existence half; the harmonicity is the canonical-representative half.

**Conservative force fields and potential energy.** A curl-free force field $F$ on a contractible region of $\mathbb{R}^3$ admits, by the Poincaré lemma applied to the associated $1$-form $\omega_F = F_1\,dx + F_2\,dy + F_3\,dz$, a potential function $U$ with $F = -\nabla U$. Conservation of energy in mechanics is a consequence of the existence of this potential, which is a consequence of the Poincaré lemma.

---

# Bridges

- **[[Thm - The Poincaré Lemma]]** *(from `Multivariate Analysis IV`)* — the Euclidean $1$-form case is the precursor to this theorem. On $\mathbb{R}^n$ for closed $1$-forms, the explicit primitive $f(x) = \int_0^1 \sum F_j(tx) x_j \, dt$ is the same homotopy-operator formula specialized to degree $1$. The manifold version generalizes from $1$-forms to all degrees and from $\mathbb{R}^n$ to star-shaped (and ultimately contractible).

- **[[Thm - Homotopy Invariance of de Rham Cohomology]]** — the Poincaré lemma is the special case "homotopy from identity to constant map," and homotopy invariance is the general case "homotopy between arbitrary maps." The same homotopy operator construction works in both cases, with the chain homotopy identity $dh + hd = H_1^* - H_0^*$ giving the Poincaré conclusion when $H_0$ is constant (so $H_0^* = 0$ on positive-degree forms) and the general homotopy-invariance conclusion when $H_0$, $H_1$ are arbitrary.

- **The Mayer–Vietoris sequence** — the Poincaré lemma is the *local* input that powers Mayer–Vietoris computations: on each contractible piece of a cover, the cohomology vanishes in positive degrees, so all the action is in the *gluing data*. Every Mayer–Vietoris computation of $H^*$ — for spheres, tori, projective spaces — runs on iterating the Poincaré lemma at each step plus tracking the gluing via the connecting map $\delta$.

- **The angular form $d\theta$ on $\mathbb{R}^2 \setminus \{0\}$** — the sharpness witness. $d\theta$ is closed on the punctured plane but not exact, certified by $\int_{S^1} d\theta = 2\pi \neq 0$. Since $\mathbb{R}^2 \setminus \{0\}$ is *not* contractible (homotopy equivalent to $S^1$), the Poincaré lemma does not apply, and indeed the conclusion fails. This is the standing counterexample that shows contractibility is essential.

- **Singular cohomology of contractible spaces** — by the [[Thm - The de Rham Theorem (Statement)|de Rham theorem]], $H^k_{dR} \cong H^k_{\mathrm{sing}}(-; \mathbb{R})$. The fact that contractible spaces have trivial singular cohomology in positive degrees (a basic theorem of algebraic topology) is, via this isomorphism, *the same theorem* as the Poincaré lemma. The two viewpoints are completely equivalent on smooth manifolds.

---

# Unlocked by This

> [!tip] **de Rham cohomology of contractible manifolds** *(from this same topic)*
> The immediate corollary: any contractible smooth manifold has $H^k_{dR} = 0$ for $k \geq 1$ and $H^0_{dR} = \mathbb{R}$. This is the foundational computation from which all others are built via Mayer–Vietoris.

> [!tip] **Local exactness in every chart** *(from this same topic)*
> Every smooth manifold has, in a neighborhood of every point, the property that closed forms are exact (since charts are diffeomorphic to balls). This makes the local-to-global discrepancy in cohomology purely a function of the topology of the manifold, not of the forms.

> [!tip] **Local-form primitives in PDE theory** *(from PDE)*
> The Poincaré lemma is the foundational existence theorem for first-order PDE systems with mixed-partial compatibility — every system of mixed-partials whose "curl" condition holds admits a local primitive function. This pattern recurs throughout PDE: integrability conditions on first derivatives equal compatibility of mixed second partials equals exactness of a $1$-form equals existence of a potential function.

> [!tip] **Čech-de Rham theorem and good covers** *(from Algebraic Topology and Sheaf Theory)*
> Every smooth manifold admits a **good cover** — a cover by open sets each diffeomorphic to a ball, with all finite intersections also so. The Poincaré lemma applies to every member and intersection, trivializing the local cohomology. The full cohomology is then encoded in the *Čech cochain complex* of the cover, and the resulting **Čech-de Rham isomorphism** is a powerful computational tool.

> [!tip] **Gauge potentials in field theory** *(from Mathematical Physics)*
> Whenever a "field strength" $F$ is closed (a Bianchi identity), the Poincaré lemma on a contractible spacetime region produces a "gauge potential" $A$ with $F = dA$, unique up to gauge transformation $A \mapsto A + d\chi$. This is the master pattern: every gauge theory — electromagnetism, Yang–Mills, gravity (in some formulations) — is built on a local Poincaré lemma, with the global non-uniqueness being the topological data (monopole charges, instanton number, etc.).
