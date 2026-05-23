---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Yang-Mills Action Functional"
  - "Def - The Yang-Mills Field Strength"
  - "Def - The Yang-Mills Equation"
  - "Def - Gauge-Covariant Derivative"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

$(M, g)$ is an oriented 4-dimensional (pseudo-)Riemannian manifold; $P \to M$ a principal $G$-bundle for a compact Lie group $G$; $\mathcal{A}$ the affine space of connections on $P$; $A \in \mathcal{A}$ a connection with field strength $F$. The exterior covariant derivative is $d_A : \Omega^k(M; \operatorname{ad} P) \to \Omega^{k+1}(M; \operatorname{ad} P)$, and its formal adjoint is $d_A^* = (-1)^{\bullet}\star d_A\star$ — for 2-forms on a Riemannian 4-manifold, $d_A^* F = -\star d_A\star F$.

The $L^2$ inner product on $\mathfrak{g}$-valued $k$-forms is $(\alpha, \beta) = -\int_M \operatorname{tr}(\alpha\wedge\star\beta)$, positive-definite when the trace form on $\mathfrak{g}$ is.

The Yang–Mills action is $S_{\text{YM}}[A] = -\tfrac12\int_M\operatorname{tr}(F\wedge\star F) = \tfrac12\|F\|^2_{L^2}$.

Wider conventions are in [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

---

# Statement

> **Theorem (Yang–Mills equation from the action principle).** A connection $A$ on a principal $G$-bundle over an oriented Riemannian 4-manifold $(M, g)$ is a critical point of the Yang–Mills action $S_{\text{YM}}[A]$ (with respect to all compactly-supported variations $\delta A \in \Omega^1(M; \operatorname{ad} P)$) if and only if its field strength $F$ satisfies the **Yang–Mills equation**
> $$d_A^* F = 0,$$
> equivalently $d_A\star F = 0$. Coupled with a matter current source $J \in \Omega^1(M; \operatorname{ad} P)$, the sourced action $S_{\text{tot}} = S_{\text{YM}}[A] + \int_M \operatorname{tr}(A\wedge\star J)$ has critical points satisfying
> $$d_A^* F = J,$$
> equivalently $d_A\star F = \star J$.

> **Corollary (Bianchi identity).** For *every* connection $A$ (not just Yang–Mills ones), the field strength satisfies the **Bianchi identity** $d_A F = 0$.

> **Corollary (charge conservation).** Applying $d_A$ to both sides of $d_A^* F = J$ and using $d_A^2 F = [F, F] = 0$ (by the Bianchi identity and the symmetry of the bracket), one obtains $d_A^* J = 0$, i.e., $J$ is covariantly conserved on shell.

---

# Motivation

This theorem is the central derivation of the entire chapter. The Yang–Mills action is *postulated* on physical and mathematical grounds (gauge invariance, locality, second-order EOMs, positivity); the Yang–Mills equation is *derived* from the action principle. The relationship between Lagrangian and field equation is the same in Yang–Mills as in any other variational field theory: the action determines the dynamics, and the dynamics manifest as the Euler–Lagrange equations.

Why is this derivation important? Three reasons. First, it makes precise the *gauge invariance* of the field equations: since $S_{\text{YM}}$ is gauge-invariant, its first variation $\delta S$ along a gauge transformation $\delta A = d_A\xi$ for $\xi \in \Omega^0(M; \operatorname{ad} P)$ vanishes identically — this is *Noether's second theorem* applied to the local gauge symmetry, and it forces the equation $d_A^* F = 0$ to be invariant under gauge transformations as well. Second, it identifies the correct *source term* in the presence of matter: varying the total action $S_{\text{matter}} + S_{\text{YM}}$ with respect to $A$ produces the YM equation with source $J^\mu = -\partial\mathcal{L}_{\text{matter}}/\partial A_\mu$, the Noether current of the matter field's gauge symmetry. Third, it places Yang–Mills theory in the universal framework of *Lagrangian field theory*, allowing all the standard techniques (Hamiltonian formalism, path integrals, perturbation theory) to be applied without modification.

The derivation also produces the *Bianchi identity* $d_A F = 0$ as a free byproduct — it holds for every connection, not just critical ones, because it follows from $F$ being defined as a curvature. The pair $(d_A F = 0, d_A^* F = 0)$ is therefore *automatically a system of first-order equations* analogous to Maxwell's pair, with the Bianchi identity playing the role of the "homogeneous" Maxwell equations and the YM equation playing the role of the "inhomogeneous" ones.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition of the theorem is "a connection $A$ on a principal $G$-bundle". Each of the following is a source from which this hypothesis can be extracted in a problem that does not literally mention principal bundles.

A first source is **a vector bundle $E \to M$ with a connection in the standard sense** (e.g., a covariant derivative $\nabla = \partial + \Gamma$ on a vector bundle of rank $N$). Property $B$ is "$E$ is a rank-$N$ vector bundle with connection $\nabla$ compatible with a $G$-structure" (e.g., an orthogonal structure, a Hermitian structure, a holomorphic structure). The bridge is that any such bundle is the associated bundle $E = P \times_\rho V$ of a principal $G$-bundle $P$ (the bundle of $G$-frames in $E$), and any connection on $E$ compatible with the $G$-structure pulls back to a principal connection on $P$. Hence the YM equation $d_A^* F_\nabla = 0$ on the principal-bundle curvature is the same as the corresponding equation on $E$. This is the source behind every "gauge theory on a vector bundle" formulation in physics — QED on the complex line bundle, QCD on the $\mathbb{C}^3$ bundle of quark colour states — even though the underlying mathematical content is principal-bundle-theoretic. Once the principal-bundle formulation is in hand, the variational derivation is universal.

A second source is **a smooth map $\phi : M \to G/H$ into a homogeneous space**. Property $B$ is "$\phi$ is a section of an $G/H$-fibre bundle over $M$" — for instance, the "non-linear sigma model" where the field takes values in a coset space. The bridge is that any such bundle has an associated principal $H$-bundle (the bundle of $H$-frames in the fibres), and the differential $d\phi$ pulls back to give a "connection-like" object that can be analysed by YM-type variational techniques. Many physical models (the chiral Lagrangian, the Skyrme model, the Stiefel–Whitney sigma model) are sigma models on homogeneous spaces, and the YM-type analysis extends to them via this bridge.

A third source is **a holomorphic vector bundle $\mathcal{E} \to X$ on a Kähler manifold**. Property $B$ is "$\mathcal{E}$ is a holomorphic vector bundle and $X$ is a compact Kähler manifold (e.g., a complex projective variety)". The bridge is that any Hermitian metric on $\mathcal{E}$ produces a canonical **Chern connection** — the unique connection compatible with both the metric and the holomorphic structure — and the Yang–Mills equation on the Chern connection becomes the **Hermitian–Yang–Mills equation** $\Lambda F = c\cdot\operatorname{id}$. By the **Donaldson–Uhlenbeck–Yau theorem**, solutions correspond to *polystable* holomorphic vector bundles. The bridge is non-obvious because complex-geometric objects (holomorphic bundles) need not look like gauge-theoretic objects (principal $U(N)$-bundles with connection), but the Chern connection provides the link.

A fourth source is **the Levi-Civita connection on a Riemannian manifold**. Property $B$ is "$M$ is a Riemannian manifold with metric $g$". The bridge is that the orthonormal frame bundle $F_O(M)$ is a principal $O(n)$-bundle (or $SO(n)$ for oriented $M$), and the Levi-Civita connection is a principal connection on $F_O(M)$. The "Yang–Mills equation" for this connection becomes a condition on the Riemann curvature — specifically, **harmonic Riemannian metrics**, satisfying a YM-type variational principle. This is the basis of *gravitational instanton* studies and the **gauge-theoretic formulation of general relativity** (the Palatini–Holst action, the Ashtekar variables).

**Targets (Output Amplification)**

The conclusion of the theorem is $d_A^* F = 0$ (or $d_A^* F = J$ with source). Each of the following combines this with one further property $D$ to give a non-trivial result $E$.

A first combination is **YM equation + Bianchi identity = Maxwell-like system**. The YM equation $d_A^* F = 0$ alone is half the story; combined with the automatic Bianchi identity $d_A F = 0$ (property $D$), one gets a *complete first-order system* on $F$. The result $E$ is the Maxwell-like equations: in components, $\partial_\mu F^{\mu\nu} = \text{commutator terms (non-abelian)} + J^\nu$ and $\partial_{[\mu}F_{\nu\rho]} = \text{commutator terms}$, which reduce to Maxwell's equations exactly for $G = U(1)$ and generalise smoothly to non-abelian $G$. This is the result that *justifies* calling YM "non-abelian Maxwell theory".

A second combination is **YM equation + self-duality $F = \star F$ = trivial verification**. Add the property $D$ that $A$ is self-dual. Then $d_A^* F = -\star d_A\star F = -\star d_A F = 0$ by Bianchi, so the YM equation is *automatically* satisfied (cf. [[Thm - Self-Dual Connections Solve Yang-Mills Automatically]]). The result $E$ is that self-duality is a sufficient condition for being a Yang–Mills connection, and a much-easier first-order PDE to solve than the second-order YM equation. This combination is the entire reason instanton physics is tractable.

A third combination is **YM equation + topological charge $k$ = action quantisation**. Add the property $D$ that the connection has topological charge $k = \int\operatorname{tr}(F\wedge F)/8\pi^2 \in \mathbb{Z}$. Combined with the BPS bound $\|F\|^2 \ge 8\pi^2|k|$ (a consequence of the YM equation only insofar as critical points have minimum action in their topological class), one obtains the action quantisation $S_{\text{YM}}[A] \ge 8\pi^2|k|$, with equality iff $A$ is (anti-)self-dual. The result $E$ is the BPS bound, which classifies the absolute action minima in each topological sector. This combination is non-obvious because the topological charge is integer-valued by topology (not by dynamics), and the variational principle plus the integer charge produces a quantised action.

A fourth combination is **YM equation + gauge fixing = elliptic PDE**. The YM equation is *not* an elliptic PDE on the space of connections, because gauge invariance produces a degenerate "kernel direction" — the gauge orbit. Add the property $D$ of a gauge-fixing condition like the **Coulomb gauge** $d^* A = 0$ or the **Lorenz gauge** $d^* A = 0$, and the gauge-fixed YM equation becomes a *non-linear elliptic system* on the gauge slice. The result $E$ is the basis of all *analytical* gauge-theory results: Uhlenbeck's compactness theorem, Sedlacek's removable-singularities theorem, regularity of YM connections — all of these are theorems about elliptic PDEs on gauge slices. The combination is essential because YM itself is not elliptic; only after gauge fixing does the PDE theory become available.

---

# Why Is It True

The intuition is the same as for any variational principle: **a critical point of an action is one where the "force" — the functional derivative of the action — vanishes**. The whole technical content of the proof is converting the abstract "$\delta S = 0$ for all $\delta A$" into the concrete equation "$d_A^* F = 0$" via integration by parts.

The mechanism, in one bolded sentence: **the variation of the curvature is the covariant exterior derivative of the variation of the connection — $\delta F = d_A(\delta A)$ — and integrating $(d_A\delta A, F) = (\delta A, d_A^* F)$ peels the derivative off $\delta A$ and onto $F$, exposing $d_A^* F$ as the Euler–Lagrange operator**.

The argument unfolds as follows. The variation of $F = dA - iqA\wedge A$ along $A \to A + t\delta A$ at $t = 0$ is, to first order in $t$,
$$\delta F = d(\delta A) - iq[A, \delta A] = d_A(\delta A).$$
The first term comes from varying the $dA$ piece; the second from varying $A\wedge A$, picking up an anticommutator (which, due to the antisymmetry of the wedge product on 1-forms, becomes a commutator). The combination $d + [A, \cdot]$ is precisely the covariant exterior derivative $d_A$.

The first variation of the action is then
$$\delta S_{\text{YM}} = -\int_M \operatorname{tr}(\delta F\wedge\star F) = -\int_M \operatorname{tr}(d_A(\delta A)\wedge\star F) = (\delta A, d_A^* F)_{L^2},$$
where the last step is the *covariant integration by parts*: for any compactly-supported $\delta A$, integration by parts gives $\int \operatorname{tr}(d_A\alpha\wedge\beta) = (-1)^{?}\int\operatorname{tr}(\alpha\wedge d_A\beta)$, and combined with $\star$ this produces the adjoint $d_A^* = -\star d_A\star$ on 2-forms.

The conclusion: $\delta S_{\text{YM}} = (\delta A, d_A^* F)_{L^2}$, which vanishes for *every* compactly-supported $\delta A$ iff $d_A^* F = 0$ pointwise on $M$.

The Bianchi identity emerges as a "free" consequence of the same machinery: applying $d_A$ to the definition $F = dA - iqA\wedge A$ and using $d^2 = 0$ together with the Jacobi identity, one gets $d_A F = 0$ identically. This holds for *every* connection, not just critical ones — it is an algebraic identity, not a dynamical equation.

---

# What Makes This Hard

The most common difficulty is the *covariant integration by parts*: students confuse the formal adjoint of $d_A$ with the formal adjoint of $d$, missing the contribution from the bracket term $[A, \cdot]$. The correct statement is that $d_A^* = (-1)^{\bullet}\star d_A\star$, *with the same $d_A$ on the right-hand side* — i.e., the adjoint of the covariant exterior derivative is built from $d_A\star$, not from $d\star$. A second pitfall is forgetting that $F$ transforms homogeneously under gauge change, so the variation $\delta F = d_A(\delta A)$ is automatically covariant: one does not need to add gauge-transformation terms by hand. A third pitfall is applying the variational principle without checking that $\delta A$ is *compactly supported* (or that boundary contributions vanish for some other reason); the integration by parts produces a boundary term that must be controlled.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Compute the first variation of $F = dA - iqA\wedge A$ along $A \to A + t\delta A$. Then express the variation of $S_{\text{YM}} = \tfrac12(F, F)$ as $(\delta F, F) = (d_A\delta A, F)$. Integrate by parts using the formal adjoint $d_A^* = -\star d_A\star$ to get $(\delta A, d_A^* F)$. Set this to zero for all compactly-supported $\delta A$, conclude $d_A^* F = 0$ pointwise.

**Subgoal decomposition:**

1. **Compute $\delta F$.** Expand $F[A + t\delta A] = d(A + t\delta A) - iq(A + t\delta A)\wedge(A + t\delta A)$ to first order in $t$.
   - *Hint:* The result is $\delta F = d(\delta A) - iq[A, \delta A] = d_A(\delta A)$.
   - *Why needed:* This is the key identity converting the YM Euler–Lagrange computation into a covariant exterior derivative.

2. **Express $\delta S_{\text{YM}}$ as an inner product with $F$.** Use $\delta\|F\|^2/2 = (F, \delta F)$ to get $\delta S = (F, d_A\delta A)$.
   - *Hint:* This is the standard rule for varying a squared norm.
   - *Why needed:* Sets up the integration by parts.

3. **Integrate by parts to get $\delta S = (d_A^* F, \delta A)$.** Use $(F, d_A\delta A) = (d_A^* F, \delta A)$ for compactly-supported $\delta A$.
   - *Hint:* Boundary terms vanish for compactly-supported variations.
   - *Why needed:* Isolates $d_A^* F$ as the Euler–Lagrange operator.

4. **Conclude the YM equation.** Demand $\delta S = 0$ for all compactly-supported $\delta A$, giving $d_A^* F = 0$ pointwise.
   - *Hint:* This uses the fundamental lemma of the calculus of variations.
   - *Why needed:* The pointwise equation is the final result.

5. **Verify the Bianchi identity automatically.** Apply $d_A$ to both sides of $F = dA - iqA\wedge A$ and use $d^2 = 0$ plus Jacobi to get $d_A F = 0$.
   - *Hint:* No variational principle needed; this is an algebraic identity.
   - *Why needed:* Completes the (YM, Bianchi) pair analogous to Maxwell.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\delta F = d_A(\delta A)$
> **Statement:** Under the variation $A \to A + t\delta A$, the first-order change in $F = dA - iq A\wedge A$ is $\delta F = d(\delta A) - iq[A, \delta A] = d_A(\delta A)$.
>
> **Hint:** Expand $F[A + t\delta A]$ to first order in $t$ and collect.
>
> **Why needed:** This identity is the entire bridge between the variation of the action and the YM Euler–Lagrange equation — without it, the variational principle does not produce a covariant equation.
>
> > [!note]- Full proof
> > Let $A_t = A + t\delta A$. Then
> > $$F[A_t] = dA_t - iqA_t\wedge A_t = dA + t\,d(\delta A) - iq(A\wedge A + tA\wedge\delta A + t\delta A\wedge A + t^2\delta A\wedge\delta A).$$
> > The zeroth-order term is $F[A]$; the first-order term in $t$ is
> > $$\delta F = d(\delta A) - iq(A\wedge\delta A + \delta A\wedge A) = d(\delta A) - iq[A, \delta A]_{\text{graded}}.$$
> > For $A$ and $\delta A$ both 1-forms, the graded bracket is $[A, \delta A]_{\text{graded}} = A\wedge\delta A - (-1)^{1\cdot 1}\delta A\wedge A = A\wedge\delta A + \delta A\wedge A$, which combined with the matrix commutator on coefficients gives the formula above. By the definition $d_A = d - iq[A, \cdot]$ on $\mathfrak{g}$-valued 1-forms (acting in the graded sense), $\delta F = d_A(\delta A)$. $\blacksquare$

> [!note]- Lemma 2: $(d_A\alpha, \beta)_{L^2} = (\alpha, d_A^*\beta)_{L^2}$ for compactly-supported $\alpha$
> **Statement:** For $\alpha \in \Omega^k(M; \operatorname{ad} P)$ compactly supported and $\beta \in \Omega^{k+1}(M; \operatorname{ad} P)$, the $L^2$ pairing satisfies $(d_A\alpha, \beta) = (\alpha, d_A^*\beta)$, where $d_A^* = (-1)^{n(k+1)+1}\star d_A\star$ on a Riemannian $n$-manifold.
>
> **Hint:** Integration by parts using $d(\alpha\wedge\star\beta) = d\alpha\wedge\star\beta \pm \alpha\wedge d\star\beta$, combined with the bracket terms.
>
> **Why needed:** This is the integration-by-parts step that converts $(\delta A, d_A^* F)$ from $(F, d_A\delta A)$.
>
> > [!note]- Full proof
> > Recall $d_A\alpha = d\alpha + [\omega, \alpha]$ (with $\omega = -iqA$ the connection 1-form). The $L^2$ pairing is $(\alpha, \beta) = -\int_M \operatorname{tr}(\alpha\wedge\star\beta)$. Compute:
> > $$(d_A\alpha, \beta) = -\int_M\operatorname{tr}((d\alpha + [\omega, \alpha])\wedge\star\beta).$$
> > For the $d\alpha$ part: $d(\operatorname{tr}(\alpha\wedge\star\beta)) = \operatorname{tr}(d\alpha\wedge\star\beta) + (-1)^k\operatorname{tr}(\alpha\wedge d\star\beta)$, so $\operatorname{tr}(d\alpha\wedge\star\beta) = d(\operatorname{tr}(\alpha\wedge\star\beta)) - (-1)^k\operatorname{tr}(\alpha\wedge d\star\beta)$. Integrating, the total-divergence term vanishes by Stokes' theorem on compactly-supported $\alpha$, leaving $-\int\operatorname{tr}(d\alpha\wedge\star\beta) = (-1)^{k+1}\int\operatorname{tr}(\alpha\wedge d\star\beta) = (-1)^{k+1}\int\operatorname{tr}(\alpha\wedge\star(\pm\star^{-1}d\star\beta))$, which simplifies (after using $\star\star = (-1)^{k(n-k)}$ in Riemannian signature) to $(\alpha, \pm\star d\star\beta)$. For the bracket part: $\operatorname{tr}([\omega, \alpha]\wedge\star\beta) = \operatorname{tr}(\omega\alpha\star\beta - \alpha\omega\star\beta) = \operatorname{tr}(\alpha(\star\beta\omega - \omega\star\beta)) = \operatorname{tr}(\alpha\wedge[\star\beta, \omega])$ by cyclicity of trace, which equals $\operatorname{tr}(\alpha\wedge\star[\beta, \omega])$ (since $\star$ commutes with the bracket on coefficients). Combining, $(d_A\alpha, \beta) = (\alpha, d_A^*\beta)$ with $d_A^* = (-1)^{?}\star d_A\star$ — the sign depending on degree and signature.

> [!note]- Lemma 3: Bianchi identity $d_A F = 0$ holds for every connection
> **Statement:** For any connection $A$ with field strength $F = dA - iqA\wedge A$, the covariant exterior derivative satisfies $d_A F = 0$.
>
> **Hint:** Use $d^2 = 0$ and the Jacobi identity on the commutator $[A, A]$.
>
> **Why needed:** The Bianchi identity is the automatic "homogeneous Maxwell" half of the YM-Bianchi pair; it is *not* derived from the action principle but is an algebraic consequence of $F$ being a curvature.
>
> > [!note]- Full proof
> > Compute $d_A F = dF + [\omega, F]$ with $\omega = -iqA$. First, $dF = d(dA - iqA\wedge A) = -iq(dA\wedge A - A\wedge dA) = -iq[dA, A]$ (using $d^2A = 0$). Then $[\omega, F] = -iq[A, dA - iqA\wedge A] = -iq[A, dA] + (iq)^2[A, A\wedge A]$. The first term cancels $dF$ (the brackets $[A, dA]$ and $[dA, A]$ are equal up to sign — they are graded brackets of a 1-form and a 2-form). The second term $[A, A\wedge A]$ vanishes by the *graded Jacobi identity*: for $\mathfrak{g}$-valued forms $\alpha$, $\beta$, $\gamma$, $[\alpha, [\beta, \gamma]] = [[\alpha, \beta], \gamma] + (-1)^{|\alpha||\beta|}[\beta, [\alpha, \gamma]]$, and applied to $[A, [A, A]] = [A, A\wedge A]$ gives zero by symmetry. Hence $d_A F = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A \in \mathcal{A}$ and $\delta A \in \Omega^1(M; \operatorname{ad} P)$ compactly supported.
>
> *Step 0 — Well-definedness.* The action $S_{\text{YM}}[A] = -\tfrac12\int_M\operatorname{tr}(F\wedge\star F)$ is well-defined on $\mathcal{A}$ (the integrand is a globally-defined 4-form, gauge-invariant). The variation $\delta A$ is a $\mathfrak{g}$-valued 1-form on $M$ (the tangent space to $\mathcal{A}$ at $A$), and compact support ensures all boundary integrals vanish.
>
> *Step 1 — Vary the field strength.* By Lemma 1, $\delta F = d_A(\delta A)$.
>
> *Step 2 — Vary the action.* Compute
> $$\delta S_{\text{YM}} = -\frac{1}{2}\delta\int_M\operatorname{tr}(F\wedge\star F) = -\int_M\operatorname{tr}(\delta F\wedge\star F) = -\int_M\operatorname{tr}(d_A(\delta A)\wedge\star F).$$
> Using the $L^2$ inner product notation, $\delta S_{\text{YM}} = (\delta F, F)_{L^2} = (d_A(\delta A), F)_{L^2}$.
>
> *Step 3 — Integrate by parts.* By Lemma 2, $(d_A(\delta A), F)_{L^2} = (\delta A, d_A^* F)_{L^2}$ for compactly-supported $\delta A$, with $d_A^* = -\star d_A\star$ on 2-forms in Riemannian 4D. Hence $\delta S_{\text{YM}} = (\delta A, d_A^* F)_{L^2}$.
>
> *Step 4 — Apply the calculus-of-variations criterion.* $A$ is critical iff $\delta S_{\text{YM}} = 0$ for all compactly-supported $\delta A$, iff $(\delta A, d_A^* F)_{L^2} = 0$ for all such $\delta A$. By the fundamental lemma of the calculus of variations, this requires $d_A^* F = 0$ pointwise on $M$. Equivalently, applying $\star$ to both sides, $d_A\star F = 0$.
>
> *Step 5 — Bianchi identity.* By Lemma 3, $d_A F = 0$ for every connection.
>
> *Step 6 — Sourced case.* When matter is included with action $\int\operatorname{tr}(A\wedge\star J)$ for $J \in \Omega^1(M; \operatorname{ad} P)$ a $\mathfrak{g}$-valued current 1-form, varying gives an additional contribution $\delta\int\operatorname{tr}(A\wedge\star J) = \int\operatorname{tr}(\delta A\wedge\star J) = -(\delta A, J)_{L^2}$, so $\delta S_{\text{tot}} = (\delta A, d_A^* F - J)_{L^2} = 0$ for all $\delta A$ requires $d_A^* F = J$, equivalently $d_A\star F = \star J$.
>
> *Step 7 — Charge conservation.* Apply $d_A$ to both sides of $d_A^* F = J$: $d_A d_A^* F = d_A J$. The LHS equals $-d_A\star d_A\star F$, and using the Bianchi identity $d_A F = 0$ together with $d_A^2\xi = [F, \xi]$ for any 2-form $\xi$ in the adjoint representation, one shows $d_A d_A^* F = 0$ on shell. Hence $d_A J = 0$, the covariant conservation of the source current. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Application 1 — Einstein equations from the Hilbert action.** The Einstein–Hilbert action $S_{\text{EH}} = \frac{1}{16\pi G}\int_M R\sqrt{-g}\,d^4x$ has Euler–Lagrange equation $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = 0$ (vacuum Einstein equations), or $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ with matter. The derivation parallels the YM derivation: vary the action with respect to the dynamical variable (the metric $g_{\mu\nu}$ here, the connection $A_\mu$ for YM), integrate by parts using the metric-compatible covariant derivative, and read off the EL equation. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

**Application 2 — Dirac equation from the Dirac Lagrangian.** Varying the Dirac action $\int\bar\psi(i\gamma^\mu D_\mu - m)\psi$ with respect to $\bar\psi$ (treating $\psi$ and $\bar\psi$ as independent fields, justified because they have eight real components total) gives the Dirac equation $(i\gamma^\mu D_\mu - m)\psi = 0$ directly. Varying with respect to $\psi$ gives the conjugate equation. This is the simplest possible variational derivation in field theory — no integration by parts needed because the Lagrangian is already first-order in derivatives. See [[Spinors and the Dirac Equation]].

**Application 3 — Geodesic equation from the arc-length functional.** For a particle's worldline $\gamma(t)$ in a Riemannian manifold $(M, g)$, the arc length $L[\gamma] = \int\sqrt{g(\dot\gamma, \dot\gamma)}\,dt$ has Euler–Lagrange equation $\nabla_{\dot\gamma}\dot\gamma = 0$ (the geodesic equation). The derivation has the same structure as YM: vary the functional with respect to the dynamical variable ($\gamma$ here, $A$ for YM), integrate by parts using the Levi-Civita covariant derivative, read off the equation. See [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Bridges

- **Connection to [[Thm - Bianchi Identity and Yang-Mills Together Parallel Maxwell]]:** The YM equation $d_A\star F = 0$ and the Bianchi identity $d_A F = 0$ together form a first-order system on the field strength $F$. For $G = U(1)$, this system reduces *exactly* to Maxwell's equations in tensor form: the Bianchi identity gives the two "homogeneous" Maxwell equations ($\operatorname{div}\vec B = 0$, Faraday's law), and the YM equation gives the two "inhomogeneous" Maxwell equations (Gauss's law, Ampère–Maxwell). The non-abelian generalisation keeps the same first-order structure but adds commutator self-interaction terms.

- **Connection to [[Thm - Self-Dual Connections Solve Yang-Mills Automatically]]:** A self-dual connection ($F = \star F$) satisfies the YM equation automatically, because $d_A\star F = d_A F = 0$ by Bianchi. This is the *first-order reduction* of the second-order YM PDE: self-duality (3 equations on $F$) implies YM (3 equations on $F$) via the algebraic identity $\star\star = 1$ in 4D.

- **Connection to [[Thm - Noether's Theorem for Internal Symmetries]]:** The YM equation $d_A^* F = J$ has its source $J$ given by the Noether current of the matter field's gauge symmetry. The chain "matter Lagrangian with gauge symmetry → Noether current → source in YM equation" is the universal mechanism by which matter sources gauge fields. The full $S_{\text{tot}} = S_{\text{matter}} + S_{\text{YM}}$ produces, by simultaneous variation, both the matter equation of motion (with $A$ appearing in the covariant derivative) and the sourced YM equation (with $J$ being the matter Noether current).

- **Connection to the [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition|Hodge decomposition]]:** The space $\Omega^1(M; \operatorname{ad} P)$ on a compact Riemannian manifold admits a *covariant Hodge decomposition* into $\operatorname{im}(d_A) \oplus \operatorname{im}(d_A^*) \oplus \ker(\Delta_A)$, where $\Delta_A = d_A d_A^* + d_A^* d_A$. The YM equation $d_A^* F = 0$ picks out the harmonic component of $\star F$. Gauge transformations correspond to motion along $\operatorname{im}(d_A)$, and the orthogonal direction $\operatorname{im}(d_A^*)$ is the natural "gauge slice" in which the YM equation becomes elliptic.

---

# Unlocked by This

> [!tip] The Yang–Mills Moduli Space and its Geometry *(from Geometric Analysis)*
> The space $\mathcal{M}_{\text{YM}} = \{A : d_A^* F = 0\}/\mathcal{G}$ of Yang–Mills connections modulo gauge equivalence has a rich geometric structure: it is finite-dimensional in each topological sector (when transversality holds), it carries natural Riemannian metrics induced from the $L^2$-metric on the space of connections, and its critical-point Morse theory was developed by **Atiyah and Bott** for the case of Riemann surfaces in 1982. On a 4-manifold the moduli space of *anti-self-dual* YM connections is the celebrated **Donaldson moduli space**, whose topology produces the **Donaldson polynomial invariants** distinguishing smooth 4-manifolds. The variational derivation of the YM equation is the foundational step that allows all of this geometric-analytic machinery to be deployed.
