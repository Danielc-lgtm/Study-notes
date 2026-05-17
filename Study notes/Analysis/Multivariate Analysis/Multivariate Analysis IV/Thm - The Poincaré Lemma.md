---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Differential Form"
  - "Def - The Exterior Derivative"
  - "Def - Pullback of a Differential Form"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $U \subseteq \mathbb{R}^n$ is open. A form $\omega$ is **closed** if $d\omega = 0$ and **exact** if $\omega = d\beta$ for some form $\beta$, called a **primitive** or **potential**. A set $U$ is **star-shaped** with respect to a point $p$ if for every $x \in U$ the whole segment from $p$ to $x$ lies in $U$; **convex** sets are star-shaped with respect to every point. A set is **contractible** if it can be continuously deformed within itself to a point. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Statement

> **The Poincaré Lemma.** Let $U \subseteq \mathbb{R}^n$ be a contractible open set — in particular, any convex or star-shaped open set. Then every closed form on $U$ is exact: if $\omega \in \Lambda^k(U)$ satisfies $d\omega = 0$ (with $k \ge 1$), there exists $\beta \in \Lambda^{k-1}(U)$ with $\omega = d\beta$.
>
> Equivalently, the [[Def - The Exterior Derivative|exterior derivative]] has no cohomology on a contractible domain: $H^k_{\mathrm{dR}}(U) = 0$ for all $k \ge 1$.
>
> For a closed $1$-form $\omega = \sum_j F_j\,dx_j$ on a star-shaped domain (with respect to the origin), an explicit primitive is the function
> $$f(x) = \int_0^1 \sum_j F_j(tx)\,x_j\;dt, \qquad df = \omega.$$

---

# Motivation

The identity $d \circ d = 0$ says every exact form is closed. The Poincaré lemma asks the converse: is every closed form exact? The question is not idle — it is the question of whether a *potential exists*. A closed $1$-form is a curl-free vector field; the lemma asks whether it is a gradient. A closed $2$-form in $\mathbb{R}^3$ is a divergence-free field; the lemma asks whether it is a curl. The whole practical machinery of "find a potential function" depends on knowing when closedness is enough.

The honest answer is: *not always*. The angular form $d\theta$ on the punctured plane is closed everywhere yet has no global primitive — there is no single-valued angle function, because going once around the origin the angle jumps by $2\pi$. So closedness alone does not give exactness. What the Poincaré lemma identifies is the *exact extra hypothesis* that does: the domain must have no holes. On a domain that can be shrunk continuously to a point — a convex set, a ball, a star-shaped region — there is nowhere for an obstruction to hide, and every closed form is exact.

Why should the *shape* of the domain matter to a question that looks purely about differentiation? Because exactness is a *global* property. Locally, near any point, a closed form is always exact — you can always find a primitive on a small ball. The issue is whether the local primitives, defined on overlapping pieces, can be *glued* into one global primitive. On a contractible domain they can, because the domain has the homotopy type of a point and there is no topological obstruction to gluing. On a domain with a hole, the local primitives can fail to match up as you go around the hole, and the mismatch — a single number, the period — is the obstruction. The Poincaré lemma is the statement that the obstruction vanishes precisely when there is no hole to carry it. It is the local half of de Rham cohomology: it says the gap between closed and exact is *invisible locally*, so that gap, when it appears globally, is a pure measure of topology.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$\omega$ is closed and $U$ is contractible.* The skill is recognizing both halves in disguise.

The first disguised source is **a vector field with vanishing curl on a convex domain**. The property $B$: "$F$ is $C^1$ with $\operatorname{curl} F = 0$ on a convex open set." The bridge: $\operatorname{curl} F = 0$ is exactly the closedness $d\omega = 0$ of the associated $1$-form $\omega = \sum F_j\,dx_j$ (the equality of cross-partials $\partial_j F_k = \partial_k F_j$), and a convex set is star-shaped, hence contractible. The non-obvious step is recognizing the integrability conditions $\partial_j F_k = \partial_k F_j$ as the coordinate form of $d\omega = 0$. *Example problem:* show a curl-free field on a ball has a potential — exactly the lemma.

The second disguised source is **a divergence-free field on a star-shaped domain in $\mathbb{R}^3$**. The property $B$: "$\operatorname{div} G = 0$ on a star-shaped open set." The bridge: $\operatorname{div} G = 0$ is the closedness of the $2$-form $\eta_G$ associated to $G$, and the lemma then produces a $1$-form primitive, i.e. a vector field $F$ with $G = \operatorname{curl} F$ — a **vector potential**. The non-obviousness: a divergence-free field is *not* obviously a curl, yet on a contractible domain it always is. *Example problem:* the existence of a magnetic vector potential $A$ with $B = \operatorname{curl} A$, given $\operatorname{div} B = 0$.

The third disguised source is **any domain that retracts onto a point**, even if not literally convex. The property $B$: "$U$ admits a continuous deformation, fixing a basepoint, shrinking $U$ to that point." The bridge: contractibility is exactly what the homotopy-invariance proof needs; star-shaped is the special case where the deformation is the straight-line scaling. The non-obvious step is that the lemma needs only the *homotopy type* of a point, not convexity. *Example problem:* a closed form on $\mathbb{R}^n$ minus a single ray is exact, because that domain, though not convex, is contractible.

**Targets (Output Amplification)**

The conclusion $C$: *$\omega = d\beta$ for some primitive $\beta$, explicitly constructible on a star-shaped domain.*

Combine $C$ with **a covering of a general domain by contractible pieces**. On any open set, the lemma applies to each member of a cover by balls, producing local primitives. The further result $E$ is that the failure of these local primitives to glue is a *finite-dimensional* obstruction — de Rham cohomology — because the lemma trivializes everything *within* each ball, leaving only the gluing data. The non-obviousness: a local existence theorem becomes the foundation of a global classification.

Combine $C$ with **path-independence of line integrals**. For a closed $1$-form on a contractible domain, $C$ produces a potential $f$, and then $\int_\gamma\omega = f(\gamma(1)) - f(\gamma(0))$ depends only on the endpoints. The further result $E$ is that every line integral of a curl-free field on a simply connected domain is path-independent — and conversely, path-independence is how you *detect* exactness. The combination is the bridge between "has a potential" and "integrates to a difference of endpoint values".

Combine $C$ with **the gauge freedom $\beta \mapsto \beta + d\gamma$**. The primitive $\beta$ is never unique: any $\beta + d\gamma$ is another primitive, since $d(\beta + d\gamma) = d\beta = \omega$. The further result $E$ is that the set of primitives is a coset, and the freedom to add an exact form is precisely the *gauge freedom* of physics — the electromagnetic potential is defined only up to $d\gamma$. The non-obviousness: the non-uniqueness in the lemma *is* gauge invariance.

---

# Why Is It True

The cleanest way to believe the Poincaré lemma is to watch the explicit construction work in the $1$-form case, and then to see why the construction is really a statement about homotopy.

Take a closed $1$-form $\omega = \sum F_j\,dx_j$ on a domain star-shaped about the origin. We want a function $f$ with $df = \omega$, that is, $\partial_j f = F_j$ for all $j$. The Fundamental Theorem of Calculus suggests defining $f(x)$ as the integral of $\omega$ along *some* path from the origin to $x$ — and on a star-shaped domain there is a canonical such path, the straight segment $t \mapsto tx$. So set $f(x) = \int_0^1\omega$ along that segment $= \int_0^1\sum_j F_j(tx)\,x_j\,dt$.

Does this $f$ have the right partial derivatives? Differentiate under the integral sign with respect to $x_j$. You get two kinds of term: one from differentiating the explicit $x_j$ factor, giving $\int_0^1 F_j(tx)\,dt$ plus pieces; and one from differentiating $F_k(tx)$ through the chain rule, giving $\int_0^1\sum_k(\partial_j F_k)(tx)\,t\,x_k\,dt$. Now use closedness: $d\omega = 0$ says $\partial_j F_k = \partial_k F_j$. Substituting, the chain-rule term becomes $\int_0^1\sum_k(\partial_k F_j)(tx)\,t\,x_k\,dt$. And $\sum_k(\partial_k F_j)(tx)\,x_k$ is exactly the derivative of $F_j(tx)$ with respect to $t$. So the whole integrand reassembles into $\frac{d}{dt}\big(t\,F_j(tx)\big)$, and $\int_0^1\frac{d}{dt}(tF_j(tx))\,dt = [tF_j(tx)]_0^1 = F_j(x)$. The Fundamental Theorem of Calculus closes the loop. So $\partial_j f = F_j$, i.e. $df = \omega$.

Notice exactly where the two hypotheses were used. *Star-shapedness* was used to have a canonical path — the segment $tx$ — lying inside the domain, so that $F_j(tx)$ makes sense for all $t \in [0,1]$. *Closedness* was used to convert the chain-rule term, via $\partial_j F_k = \partial_k F_j$, into a total $t$-derivative that telescopes. Remove star-shapedness and the path may leave the domain; remove closedness and the integrand does not reassemble. Both are essential, and the proof shows it.

The conceptual heart, valid for all degrees, is this: the construction is integration along the homotopy $H(t, x) = tx$ that contracts the domain to the origin. The lemma is true because $U$ is contractible — because there *is* such a homotopy. A homotopy from the identity map to the constant map induces, on forms, an operator (the "homotopy operator" or "chain homotopy") $h$ satisfying $dh + hd = \operatorname{id}$ on positive-degree forms. Apply this identity to a closed form $\omega$: the $hd\omega$ term vanishes because $d\omega = 0$, leaving $\omega = d(h\omega)$, so $h\omega$ is the primitive. The explicit integral above is exactly $h\omega$ for the straight-line contraction. One should *expect* the lemma to hold whenever the domain is contractible, because a contraction is precisely a homotopy to a constant, and a homotopy to a constant gives the algebraic identity $dh + hd = \operatorname{id}$ that turns closedness into exactness.

---

# What Makes This Hard

The conceptual obstacle is believing that **closedness is not enough on its own** — the lemma is *false* without the contractibility hypothesis, and the punctured plane is the standing counterexample, so the theorem is as much about the hypothesis as about the conclusion. In the proof, the non-obvious step is the **reassembly of the differentiated integrand into a total $t$-derivative**: after differentiating under the integral sign, the expression looks like an unrelated sum of terms, and only the substitution $\partial_j F_k = \partial_k F_j$ (which *is* the closedness hypothesis) collapses it into $\frac{d}{dt}(tF_j(tx))$. The most common error is to forget that closedness is used here — to think the construction $f(x) = \int_0^1 F(tx)\cdot x\,dt$ produces a potential for *any* field, when in fact it produces one only when the field is curl-free.

---

# Rederivation Scaffold

**High-level strategy:** On a star-shaped domain, define the primitive by integrating the form along the straight segment from the basepoint to $x$; differentiate under the integral sign; use closedness to collapse the result into a total $t$-derivative, then apply the Fundamental Theorem of Calculus.

**Subgoal decomposition:**

1. **Define the candidate primitive.** For a closed $1$-form $\omega = \sum F_j\,dx_j$ on a domain star-shaped about $0$, set $f(x) = \int_0^1\sum_j F_j(tx)\,x_j\,dt$.
   - *Hint:* This is $\int_0^1\omega$ along the segment $t \mapsto tx$ — the only canonical path on a star-shaped domain.
   - *Why needed:* The Fundamental Theorem of Calculus only produces a primitive if you integrate the form along *some* path; star-shapedness supplies it.

2. **Differentiate under the integral sign.** Compute $\partial_j f(x)$, getting an explicit term and a chain-rule term.
   - *Hint:* Differentiation under the integral is licensed because the integrand is $C^1$ and $[0,1]$ is compact.
   - *Why needed:* It reduces $\partial_j f = F_j$ to an identity inside the integral.

3. **Invoke closedness.** Replace $\partial_j F_k$ by $\partial_k F_j$ everywhere, using $d\omega = 0$.
   - *Hint:* $d\omega = 0$ in coordinates is exactly $\partial_j F_k = \partial_k F_j$ for all $j, k$.
   - *Why needed:* This is the single step that makes the integrand collapse — without it, the proof fails.

4. **Collapse to a total derivative and finish.** Recognize the integrand as $\frac{d}{dt}(tF_j(tx))$ and integrate by the Fundamental Theorem of Calculus to get $F_j(x)$.
   - *Hint:* $\frac{d}{dt}(tF_j(tx)) = F_j(tx) + t\sum_k(\partial_k F_j)(tx)x_k$ — match this to the integrand from steps 2–3.
   - *Why needed:* It yields $\partial_j f = F_j$, i.e. $df = \omega$, completing the construction.

---

# Lemma Decomposition

> [!note]- Lemma 1: Closedness of a 1-form is the symmetry of cross-partials
> **Statement:** For a $C^1$ $1$-form $\omega = \sum_j F_j\,dx_j$ on $U$, $d\omega = 0$ if and only if $\partial_j F_k = \partial_k F_j$ for all $j, k$.
>
> **Hint:** Compute $d\omega$ directly from the definition of the exterior derivative.
>
> **Why needed:** It is the translation that lets the closedness hypothesis enter the differentiation-under-the-integral computation.
>
> > [!note]- Full proof
> > By definition, $d\omega = \sum_{j,\ell}(\partial_\ell F_j)\,dx_\ell\wedge dx_j = \sum_{\ell < j}(\partial_\ell F_j - \partial_j F_\ell)\,dx_\ell\wedge dx_j$, after collecting the $(\ell, j)$ and $(j, \ell)$ terms using $dx_j\wedge dx_\ell = -dx_\ell\wedge dx_j$. The basic $2$-forms $dx_\ell\wedge dx_j$ ($\ell < j$) are linearly independent, so $d\omega = 0$ if and only if every coefficient $\partial_\ell F_j - \partial_j F_\ell$ vanishes, i.e. $\partial_\ell F_j = \partial_j F_\ell$.

> [!note]- Lemma 2: Differentiation under the integral sign
> **Statement:** If $g(t, x)$ is $C^1$ and $[0,1]$ is compact, then $\partial_{x_j}\int_0^1 g(t, x)\,dt = \int_0^1\partial_{x_j} g(t, x)\,dt$.
>
> **Hint:** This is the standard theorem from [[Multivariate Analysis III — Integration in Several Variables]] on differentiating a parameter integral.
>
> **Why needed:** It is what makes the candidate $f(x) = \int_0^1\sum F_j(tx)x_j\,dt$ differentiable term by term.
>
> > [!note]- Full proof
> > The integrand $g(t, x) = \sum_j F_j(tx)\,x_j$ is $C^1$ in $(t, x)$ jointly, since $F$ is $C^1$. On the compact interval $[0,1]$, the partial $\partial_{x_j} g$ is continuous, hence bounded, and the difference quotients converge uniformly in $t$; the dominated convergence / uniform-convergence criterion then allows the limit defining $\partial_{x_j}$ to pass inside the integral. (This is the differentiation-under-the-integral-sign theorem of the previous topic; the compactness of $[0,1]$ supplies the uniform domination.)

> [!note]- Lemma 3: The integrand reassembles into a total $t$-derivative
> **Statement:** For a closed $C^1$ $1$-form, $F_j(tx) + t\sum_k(\partial_j F_k)(tx)\,x_k = \dfrac{d}{dt}\big(t\,F_j(tx)\big)$.
>
> **Hint:** Compute the right side by the product and chain rules, then apply the closedness identity from Lemma 1.
>
> **Why needed:** It is the collapse that turns $\partial_j f$ into an integral of a total derivative, finishable by the Fundamental Theorem of Calculus.
>
> > [!note]- Full proof
> > By the product and chain rules, $\frac{d}{dt}(tF_j(tx)) = F_j(tx) + t\cdot\frac{d}{dt}F_j(tx) = F_j(tx) + t\sum_k(\partial_k F_j)(tx)\,x_k$. By Lemma 1 (closedness), $\partial_k F_j = \partial_j F_k$, so the sum equals $t\sum_k(\partial_j F_k)(tx)\,x_k$. Hence $\frac{d}{dt}(tF_j(tx)) = F_j(tx) + t\sum_k(\partial_j F_k)(tx)\,x_k$, which is exactly the claimed left side.

---

# Formal Proof

> [!note]- Complete formal proof (the 1-form case on a star-shaped domain)
> Let $U \subseteq \mathbb{R}^n$ be open and star-shaped with respect to the origin, and let $\omega = \sum_j F_j\,dx_j$ be a closed $C^1$ $1$-form on $U$. Define $f : U \to \mathbb{R}$ by
> $$f(x) = \int_0^1\sum_{j} F_j(tx)\,x_j\;dt.$$
> Star-shapedness guarantees $tx \in U$ for all $t \in [0,1]$, so the integrand is defined. We show $df = \omega$, i.e. $\partial_j f = F_j$ for each $j$.
>
> **Differentiate under the integral.** By Lemma 2, $\partial_j f(x) = \int_0^1\partial_{x_j}\Big(\sum_k F_k(tx)\,x_k\Big)\,dt$. Compute the integrand: differentiating $\sum_k F_k(tx)\,x_k$ with respect to $x_j$ gives, by the product and chain rules,
> $$\partial_{x_j}\Big(\sum_k F_k(tx)\,x_k\Big) = F_j(tx) + \sum_k(\partial_j F_k)(tx)\,t\,x_k,$$
> the first term from differentiating the explicit factor $x_j$ (only $k = j$ contributes), the sum from differentiating each $F_k(tx)$.
>
> **Invoke closedness and collapse.** By Lemma 3, using $d\omega = 0$, the integrand equals $\dfrac{d}{dt}\big(t\,F_j(tx)\big)$. Therefore
> $$\partial_j f(x) = \int_0^1\frac{d}{dt}\big(t\,F_j(tx)\big)\,dt = \Big[t\,F_j(tx)\Big]_{t=0}^{t=1} = 1\cdot F_j(x) - 0 = F_j(x),$$
> by the Fundamental Theorem of Calculus.
>
> **Conclusion.** Since $\partial_j f = F_j$ for every $j$, we have $df = \sum_j(\partial_j f)\,dx_j = \sum_j F_j\,dx_j = \omega$. So $\omega$ is exact. $\blacksquare$
>
> *Remark on the general degree.* For a closed $k$-form ($k \ge 1$) on a star-shaped domain, the same idea is the **homotopy operator**: define $h\omega$ by integrating $\omega$ against the radial vector field along the contraction $H(t,x) = tx$, explicitly $(h\omega)(x) = \int_0^1 t^{k-1}\,(\iota_x\omega)(tx)\,dt$ where $\iota_x$ is contraction with the position vector. A direct computation gives the chain-homotopy identity $d(h\omega) + h(d\omega) = \omega$ for every $k$-form. If $d\omega = 0$, this reads $\omega = d(h\omega)$, so $h\omega$ is the primitive. The $1$-form computation above is this identity with $k = 1$, where $h\omega = f$ is a function. Contractibility (rather than star-shapedness) suffices, because any contraction homotopy yields such an $h$.

---

# Cross-Field Exercise Suggestions

**Existence of the electromagnetic potentials.** In a contractible region of spacetime, the homogeneous Maxwell equation $dF = 0$ (a closed $2$-form) implies, by the Poincaré lemma, $F = dA$ for a $1$-form $A$ — the four-potential. The application is fundamental because the *existence* of the vector and scalar potentials of electromagnetism is exactly the Poincaré lemma, and the non-uniqueness $A \mapsto A + d\chi$ is its gauge freedom.

**Exact differential equations and integrating factors.** A first-order ODE $M\,dx + N\,dy = 0$ is "exact" when the $1$-form $M\,dx + N\,dy$ is closed ($\partial_y M = \partial_x N$); the Poincaré lemma then supplies a potential $u$ whose level curves are the solutions. When the form is not closed, an *integrating factor* multiplies it into a closed form. The application is nonobvious because the classical theory of exact ODEs is the Poincaré lemma for $1$-forms in two variables, with the integrating factor as the device that repairs non-closedness.

**Thermodynamics and state functions.** In thermodynamics, the question of whether a quantity (entropy, internal energy) is a *state function* — a function of the state alone, independent of the process path — is the question of whether a certain $1$-form is exact. Heat $\delta Q$ is *not* exact (not a state function), but $\delta Q / T$ is. The application is striking because the entire distinction between state functions and path-dependent quantities is the closed-versus-exact dichotomy, with the Poincaré lemma guaranteeing exactness on the (contractible) space of equilibrium states.

**Conservative force fields in mechanics.** A force field on a contractible region is conservative — derivable from a potential energy — exactly when it is curl-free, by the Poincaré lemma. The application connects the lemma to the conservation of energy: a conservative field admits a potential, and the work done is a difference of potential values, independent of the path.

---

# Bridges

- **[[Thm - The General Stokes Theorem|The General Stokes Theorem]]** — the partner result. Stokes shows exact forms integrate to zero over closed surfaces (closed surfaces are boundaries of nothing in the local picture); the Poincaré lemma shows closed forms are exact on contractible domains. Together they say: on a contractible domain, closed = exact, and integration over cycles is trivial.

- **de Rham cohomology** — the lemma is the computation $H^k_{\mathrm{dR}}(U) = 0$ for $k \ge 1$ and contractible $U$. It is the base case of every cohomology computation: the Mayer-Vietoris argument builds the cohomology of a general space by gluing contractible pieces, each contributing nothing by the Poincaré lemma, so all cohomology comes from the gluing.

- **The angular form $d\theta$ on the punctured plane** — the sharpness witness. $d\theta$ is closed but not exact on $\mathbb{R}^2\setminus\{0\}$, which is *not* contractible. This is the standing proof that the contractibility hypothesis cannot be dropped, and the explicit nontrivial class in $H^1_{\mathrm{dR}}(\mathbb{R}^2\setminus\{0\})$ — see [[Ex - A closed form that is not exact]].

- **Homotopy invariance of de Rham cohomology** — the lemma is the special case "contractible to a point". The general principle, that homotopic maps induce the same map on cohomology, is proved by the same homotopy operator $h$ with $dh + hd = \operatorname{id}$, applied to a general homotopy rather than a contraction.

---

# Unlocked by This

> [!tip] de Rham Cohomology and the Mayer-Vietoris Sequence *(from Algebraic Topology)*
> The Poincaré lemma is the local input — "contractible pieces have no cohomology" — to the Mayer-Vietoris long exact sequence, the inductive tool that computes $H^k_{\mathrm{dR}}$ of a space from the cohomology of an open cover. All of de Rham cohomology is the lemma plus gluing.

> [!tip] Gauge Theory *(from Physics)*
> The non-uniqueness of the primitive — $\beta$ and $\beta + d\gamma$ both work — is **gauge freedom**. In electromagnetism the potential $A$ with $F = dA$ is fixed only up to $A \mapsto A + d\chi$; in non-abelian gauge theory the same redundancy, enriched, is the symmetry group of the Standard Model.
