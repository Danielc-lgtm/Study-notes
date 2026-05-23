---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Adjoint Bundle"
  - "Thm - Gauge Transformation Law for Local Connection 1-Forms"
tags: [geometry, gauge-theory, principal-bundles, affine-spaces, moduli]
---

# Problem Statement

Let $P \to M$ be a principal $G$-bundle and let $\mathcal{A}(P)$ denote the set of all [[Def - Connection 1-Form on a Principal Bundle|connection 1-forms]] on $P$.

**(a) Show that the difference of two connections $\omega_1 - \omega_2$ is a *horizontal and equivariant* $\mathfrak{g}$-valued 1-form on $P$**, i.e., satisfies $(\omega_1 - \omega_2)(\xi^*) = 0$ for all $\xi \in \mathfrak{g}$ and $R_g^*(\omega_1 - \omega_2) = \mathrm{Ad}_{g^{-1}}(\omega_1 - \omega_2)$.

**(b)** Show that horizontal equivariant $\mathfrak{g}$-valued 1-forms on $P$ are in canonical bijection with 1-form sections of the [[Def - Adjoint Bundle|adjoint bundle]] $\mathrm{Ad}\,P$, i.e., elements of $\Omega^1(M; \mathrm{Ad}\,P)$. Conclude that $\omega_1 - \omega_2$ descends to a 1-form on $M$ with values in $\mathrm{Ad}\,P$.

**(c) Conclude that the space $\mathcal{A}(P)$ is an affine space modelled on $\Omega^1(M; \mathrm{Ad}\,P)$**: for any reference connection $\omega_0 \in \mathcal{A}(P)$, every connection is of the form $\omega = \omega_0 + \pi^*\eta$ for a unique 1-form section $\eta \in \Omega^1(M; \mathrm{Ad}\,P)$ (where $\pi^*$ is the pullback from base to total space).

**(d) Compute the curvature of $\omega_0 + \pi^*\eta$** and show
$$
F_{\omega_0 + \pi^*\eta} = F_{\omega_0} + d_{\omega_0}\eta + \tfrac{1}{2}[\eta, \eta],
$$
where $d_{\omega_0}$ is the [[Def - Exterior Covariant Derivative on Associated Bundles|exterior covariant derivative]] on $\Omega^\bullet(M; \mathrm{Ad}\,P)$. This is the affine expansion of the curvature, used pervasively in Yang-Mills moduli theory.

**Recall:**

A connection 1-form: ![[Def - Connection 1-Form on a Principal Bundle#The Definition]]

The adjoint bundle: ![[Def - Adjoint Bundle#The Definition]]

A 1-form section of $\mathrm{Ad}\,P$ is an element of $\Omega^1(M; \mathrm{Ad}\,P) = \Gamma(T^*M \otimes \mathrm{Ad}\,P)$: locally, a $\mathfrak{g}$-valued 1-form $\eta_\alpha$ on $U_\alpha$, with cocycle $\eta_\beta = \mathrm{Ad}_{g_{\alpha\beta}^{-1}}\eta_\alpha = g_{\alpha\beta}^{-1}\eta_\alpha g_{\alpha\beta}$ on overlaps (no inhomogeneous term).

---

# Convergent Strategy

**Problem class:** This is a *structural / abstract* problem about the *space* of connections, not about a specific connection. The general pattern: identify the algebraic structure of an infinite-dimensional space (the space of connections), realising it as an *affine space* over a vector space (the space of 1-form sections of the adjoint bundle). The exercise is foundational for **moduli theory** of gauge fields.

**Assumption pattern:** Two connections $\omega_1, \omega_2$ on the same $P \to M$ — both satisfying verticality and equivariance. Their difference, being a difference of two objects satisfying the same affine condition, lives in the *linear* (homogeneous) part of the affine structure.

**Theorem routing:** Verticality of both $\omega_1, \omega_2$ → $\omega_1 - \omega_2$ vanishes on fundamental vector fields (horizontality). Equivariance of both → $\omega_1 - \omega_2$ is equivariant. Horizontal + equivariant → descends to a 1-form section of $\mathrm{Ad}\,P$ (analogous to the [[Thm - Cartan Structural Equation for Principal Connections|descent of the curvature]]). The descent is a *canonical* bijection.

**Key decision point:** The non-obvious insight is that the *difference* of two connections is much simpler than either connection individually: connections are affine objects (with the inhomogeneous term making them non-tensors), but their differences are *linear* objects (with the inhomogeneous terms cancelling). This affine structure is *the* organising principle of the space of connections.

---

# Legal Operations Used

1. **Operation 1 (pull back along a section).** Verify the descent by computing $s^*(\omega_1 - \omega_2) = A_1 - A_2$ in any local trivialisation.

2. **Operation 2 (gauge transformation law).** Under change of section, both $A_1$ and $A_2$ get the same inhomogeneous $g^{-1}dg$ term, which cancels in the difference: $A_1 - A_2$ transforms tensorially as $\mathrm{Ad}_{g^{-1}}(A_1 - A_2)$ — exactly as a 1-form section of $\mathrm{Ad}\,P$.

3. **Operation 3 (structural equation).** Compute $F_{\omega_0 + \pi^*\eta} = d(\omega_0 + \pi^*\eta) + \tfrac{1}{2}[\omega_0 + \pi^*\eta, \omega_0 + \pi^*\eta]$ and expand.

5. **Operation 5 (decompose tangent vectors).** Use vertical/horizontal decomposition for the horizontality verification.

8. **Operation 8 (horizontal equivariant form descends).** Apply this principle to conclude $\omega_1 - \omega_2 \in \Omega^1(M; \mathrm{Ad}\,P)$.

9. **Operation 9 (affine structure of $\mathcal{A}(P)$).** This entire exercise *establishes* the affine structure; subsequent calculations rely on it.

---

# Hints

> [!note]- Hint 1
> For part (a): both $\omega_1$ and $\omega_2$ satisfy verticality $\omega_i(\xi^*) = \xi$. Hence $(\omega_1 - \omega_2)(\xi^*) = \xi - \xi = 0$ — horizontal in the sense of vanishing on vertical vectors. Equivariance: both $\omega_i$ satisfy $R_g^*\omega_i = \mathrm{Ad}_{g^{-1}}\omega_i$, so $R_g^*(\omega_1 - \omega_2) = \mathrm{Ad}_{g^{-1}}(\omega_1 - \omega_2)$. ✓

> [!note]- Hint 2
> For part (b): the descent of a horizontal equivariant $\mathfrak{g}$-valued $r$-form on $P$ to an $r$-form section of $\mathrm{Ad}\,P$ on $M$ is a general fact (the same descent that makes the curvature $F$ a section of $\mathrm{Ad}\,P$). The horizontality lets the form depend only on the projection to $TM$; the equivariance ensures the cocycle on overlaps is $\mathrm{Ad}_{g^{-1}}$ — exactly the cocycle for sections of $\mathrm{Ad}\,P$.

> [!note]- Hint 3
> For part (c): given a reference connection $\omega_0$ and any other connection $\omega$, set $\eta := s^*(\omega - \omega_0) \in \Omega^1(U; \mathfrak{g})$ in a local trivialisation by $s$. The cocycle on overlaps is $\mathrm{Ad}$-transformation — no inhomogeneous term — so $\eta$ defines a global 1-form section of $\mathrm{Ad}\,P$.

> [!note]- Hint 4
> Equivalently: $\omega = \omega_0 + (\omega - \omega_0)$ shows every connection is the reference plus a horizontal equivariant form. The "plus" is the affine addition: $\omega_0 + \eta = \omega$ with $\eta = \omega - \omega_0 \in \Omega^1(M; \mathrm{Ad}\,P)$ (after the descent).

> [!note]- Hint 5
> For part (d): expand $F_{\omega_0 + \pi^*\eta} = d(\omega_0 + \pi^*\eta) + \tfrac{1}{2}[\omega_0 + \pi^*\eta, \omega_0 + \pi^*\eta] = d\omega_0 + d(\pi^*\eta) + \tfrac{1}{2}([\omega_0, \omega_0] + 2[\omega_0, \pi^*\eta] + [\pi^*\eta, \pi^*\eta])$. The first and third combine to $F_{\omega_0}$. The cross-term $[\omega_0, \pi^*\eta] + d(\pi^*\eta)$ combines (after pulling back to $M$) to the covariant derivative $d_{\omega_0}\eta$. The last term is $\tfrac{1}{2}[\eta, \eta]$.

---

# Solution

**Plan:** Verify horizontality and equivariance of $\omega_1 - \omega_2$ from the axioms of each $\omega_i$. Apply the descent theorem (horizontal + equivariant → section of $\mathrm{Ad}\,P$) to conclude $\omega_1 - \omega_2 \in \Omega^1(M; \mathrm{Ad}\,P)$. Conclude the affine structure of $\mathcal{A}(P)$. Compute the curvature of $\omega_0 + \pi^*\eta$ using the structural equation.

**Step 1: Horizontality of $\omega_1 - \omega_2$.**

> [!note]- Derivation
> Both $\omega_1$ and $\omega_2$ are connections on the same $P$, hence both satisfy verticality:
> $$
> \omega_1(\xi^*_p) = \xi, \quad \omega_2(\xi^*_p) = \xi \quad \forall \xi \in \mathfrak{g}, p \in P.
> $$
> Subtract:
> $$
> (\omega_1 - \omega_2)(\xi^*_p) = \xi - \xi = 0.
> $$
> So the difference vanishes on every fundamental vector field — equivalently, on every vertical vector. The difference is **horizontal** in the strong sense: $(\omega_1 - \omega_2)|_{V_p P} = 0$.

**Step 2: Equivariance of $\omega_1 - \omega_2$.**

> [!note]- Derivation
> Both $\omega_i$ satisfy equivariance: $R_g^*\omega_i = \mathrm{Ad}_{g^{-1}}\omega_i$. Subtract:
> $$
> R_g^*(\omega_1 - \omega_2) = R_g^*\omega_1 - R_g^*\omega_2 = \mathrm{Ad}_{g^{-1}}\omega_1 - \mathrm{Ad}_{g^{-1}}\omega_2 = \mathrm{Ad}_{g^{-1}}(\omega_1 - \omega_2).
> $$
> So $\omega_1 - \omega_2$ is equivariant.

**Step 3: Descent to a 1-form section of $\mathrm{Ad}\,P$.**

> [!note]- Derivation
> A horizontal equivariant $\mathfrak{g}$-valued $r$-form on $P$ descends to an $r$-form section of $\mathrm{Ad}\,P$ on $M$, by the same argument as for the curvature (see [[Thm - Cartan Structural Equation for Principal Connections]] for the analogous descent). The key points:
> - **Horizontality** ensures the form vanishes on vertical inputs, so when evaluated on horizontal lifts of base vector fields it depends only on the basepoint and the base vectors — not on the choice of horizontal lift in the fibre.
> - **Equivariance** ensures the cocycle on overlapping trivialisations is $\mathrm{Ad}_{g^{-1}}$ — exactly the cocycle for sections of $\mathrm{Ad}\,P$.
> 
> Concretely: in a local trivialisation by $s_\alpha$, the descent gives $s_\alpha^*(\omega_1 - \omega_2) = A_1^\alpha - A_2^\alpha \in \Omega^1(U_\alpha; \mathfrak{g})$, with cocycle on overlaps $A_1^\beta - A_2^\beta = g_{\alpha\beta}^{-1}(A_1^\alpha - A_2^\alpha)g_{\alpha\beta}$. (The inhomogeneous terms $g_{\alpha\beta}^{-1}dg_{\alpha\beta}$ in the gauge transformations of $A_1$ and $A_2$ cancel in the difference.) This is exactly the cocycle for a 1-form section of $\mathrm{Ad}\,P$.
> 
> So $\omega_1 - \omega_2 \in \Omega^1(M; \mathrm{Ad}\,P)$.

**Step 4: Affine structure of $\mathcal{A}(P)$.**

> [!note]- Derivation
> Fix a reference connection $\omega_0 \in \mathcal{A}(P)$. Any other connection $\omega \in \mathcal{A}(P)$ has $\omega - \omega_0 \in \Omega^1(M; \mathrm{Ad}\,P)$ (by Steps 1–3, with $\omega_1 = \omega, \omega_2 = \omega_0$).
> 
> Conversely, for any $\eta \in \Omega^1(M; \mathrm{Ad}\,P)$, the sum $\omega_0 + \pi^*\eta$ — where $\pi^*\eta$ is the pullback of $\eta$ from $M$ to $P$ along the projection $\pi : P \to M$ — is a connection 1-form on $P$. (More precisely: $\pi^*\eta$ is a horizontal $\mathfrak{g}$-valued 1-form on $P$ — horizontal because it is a pullback from the base, with values in $\mathrm{Ad}\,P$ identified with $\mathfrak{g}$ via the chosen section. Adding a horizontal equivariant form to $\omega_0$ preserves both verticality and equivariance.)
> 
> So the map $\eta \mapsto \omega_0 + \pi^*\eta$ is a bijection $\Omega^1(M; \mathrm{Ad}\,P) \to \mathcal{A}(P)$. This is the affine structure: $\mathcal{A}(P)$ is an affine space modelled on the vector space $\Omega^1(M; \mathrm{Ad}\,P)$.

**Step 5: Curvature of $\omega_0 + \pi^*\eta$.**

> [!note]- Derivation
> $$
> F_{\omega_0 + \pi^*\eta} = d(\omega_0 + \pi^*\eta) + \tfrac{1}{2}[\omega_0 + \pi^*\eta, \omega_0 + \pi^*\eta].
> $$
> Expand:
> $$
> = d\omega_0 + d(\pi^*\eta) + \tfrac{1}{2}[\omega_0, \omega_0] + [\omega_0, \pi^*\eta] + \tfrac{1}{2}[\pi^*\eta, \pi^*\eta].
> $$
> 
> Group: $d\omega_0 + \tfrac{1}{2}[\omega_0, \omega_0] = F_{\omega_0}$ (the curvature of $\omega_0$).
> 
> The remaining terms: $d(\pi^*\eta) + [\omega_0, \pi^*\eta] + \tfrac{1}{2}[\pi^*\eta, \pi^*\eta]$. 
> 
> Push down to $M$ via pullback by any local section $s$: $s^*\pi^*\eta = \eta$ (since $\pi \circ s = \mathrm{id}_M$), and $s^*[\omega_0, \pi^*\eta] = [A_0, \eta]$ where $A_0 = s^*\omega_0$. So
> $$
> s^*\big(d(\pi^*\eta) + [\omega_0, \pi^*\eta]\big) = d\eta + [A_0, \eta] = d_{\omega_0}\eta
> $$
> using the [[Def - Exterior Covariant Derivative on Associated Bundles|exterior covariant derivative]] on $\mathrm{Ad}\,P$-valued forms. And $s^*\tfrac{1}{2}[\pi^*\eta, \pi^*\eta] = \tfrac{1}{2}[\eta, \eta]$.
> 
> Combining:
> $$
> s^*F_{\omega_0 + \pi^*\eta} = F_{\omega_0} + d_{\omega_0}\eta + \tfrac{1}{2}[\eta, \eta] \in \Omega^2(U; \mathfrak{g}).
> $$
> Globally, as a section of $\Omega^2(M; \mathrm{Ad}\,P)$:
> $$
> F_{\omega_0 + \pi^*\eta} = F_{\omega_0} + d_{\omega_0}\eta + \tfrac{1}{2}[\eta, \eta].
> $$
> ✓ This is the **affine expansion of the curvature**.

> [!note]- Complete formal solution
> **Part (a).** Verticality: $(\omega_1 - \omega_2)(\xi^*) = \xi - \xi = 0$. Equivariance: $R_g^*(\omega_1 - \omega_2) = \mathrm{Ad}_{g^{-1}}(\omega_1 - \omega_2)$ (linearity of pullback and adjoint action).
> 
> **Part (b).** A horizontal equivariant $\mathfrak{g}$-valued $r$-form on $P$ descends to a section of $\Omega^r(M; \mathrm{Ad}\,P)$: the descent is locally via pullback by sections of $P$, with the equivariance giving the correct $\mathrm{Ad}$-cocycle on overlaps. Applied to $\omega_1 - \omega_2$, we conclude it is a 1-form section of $\mathrm{Ad}\,P$.
> 
> **Part (c).** For any reference $\omega_0 \in \mathcal{A}(P)$, the map $\omega \mapsto \omega - \omega_0$ from $\mathcal{A}(P)$ to $\Omega^1(M; \mathrm{Ad}\,P)$ is a bijection (with inverse $\eta \mapsto \omega_0 + \pi^*\eta$). So $\mathcal{A}(P)$ is an **affine space modelled on $\Omega^1(M; \mathrm{Ad}\,P)$** — every connection is a reference connection plus a 1-form valued in the adjoint bundle.
> 
> **Part (d).** Computing the curvature of $\omega_0 + \pi^*\eta$ via the structural equation gives, after pulling back to $M$:
> $$
> F_{\omega_0 + \pi^*\eta} = F_{\omega_0} + d_{\omega_0}\eta + \tfrac{1}{2}[\eta, \eta].
> $$
> The cross-term $d_{\omega_0}\eta$ is the exterior covariant derivative of $\eta$ as a section of $\mathrm{Ad}\,P$ (= $d\eta + [A_0, \eta]$ in a local trivialisation). The quadratic term $\tfrac{1}{2}[\eta, \eta]$ is the self-bracket of $\eta$ as a $\mathrm{Ad}\,P$-valued 1-form.

> [!warning] Illegal but tempting alternative route
> One might be tempted to *redefine* the space of connections as the linear space of 1-form sections of $\mathrm{Ad}\,P$, rather than as an affine space. This is wrong: there is *no canonical choice* of "zero connection" (the trivial connection $\omega = 0$ does not satisfy the verticality axiom on a non-trivial bundle, since $\omega = 0$ implies $\xi^* \in \ker\omega$ for all $\xi$, which only happens if $V_p P = 0$ — but $V_p P$ has dimension $\dim G > 0$). The affine structure is *essential*: there is no canonical zero, but the differences of connections are well-defined linear objects. Trying to treat $\mathcal{A}(P)$ as a linear space leads to errors in moduli-space arguments and gauge-fixing procedures.

---

# Key Takeaways

**The space of connections is an affine space, not a vector space.** This is a deep structural fact. Connections $\omega$ are not "vectors with a canonical zero" — there is no canonical zero connection on a generic principal bundle. But *differences* of connections ($\omega_1 - \omega_2$) are well-defined elements of the *linear* space $\Omega^1(M; \mathrm{Ad}\,P)$. Choosing a reference connection $\omega_0$ gives a *linearisation* of $\mathcal{A}(P)$, but the choice is non-canonical. This is exactly the same structure as classical affine geometry: a flat plane is an affine space over $\mathbb{R}^2$, with no canonical origin, but differences of points are well-defined translation vectors.

**Yang-Mills moduli theory begins here.** The space of connections $\mathcal{A}(P)$ has an action of the gauge group $\mathcal{G}(P) = \Gamma(P \times_{\mathrm{Adj}} G)$ (the bundle of group elements), and the quotient $\mathcal{M}(P) = \mathcal{A}(P)/\mathcal{G}(P)$ is the **moduli space of connections modulo gauge**. The affine structure of $\mathcal{A}(P)$, combined with the action of $\mathcal{G}(P)$ on it, gives the local model for moduli spaces (after slicing through the gauge orbits via a gauge-fixing condition). For *Yang-Mills* connections (critical points of the Yang-Mills action), $\mathcal{M}_{\text{YM}}(P) \subset \mathcal{M}(P)$ is a finite-dimensional space whose geometry is the source of Donaldson invariants of 4-manifolds.

**The affine expansion of the curvature is the key to perturbative gauge theory.** $F_{\omega_0 + \pi^*\eta} = F_{\omega_0} + d_{\omega_0}\eta + \tfrac{1}{2}[\eta, \eta]$ — *linear* in $\eta$ to first order, *quadratic* to second order. For Yang-Mills theory expanded around an instanton solution $\omega_0$ (with $F_{\omega_0}$ self-dual), the linearisation gives the linearised instanton equations $d_{\omega_0}\eta + \star d_{\omega_0}\eta = 0$, whose solutions modulo gauge are the tangent space to the moduli of self-dual connections. The quadratic and higher terms control the deformation theory of instantons. This expansion is the workhorse of perturbative QFT around classical solutions.

**Trigger-reaction pattern: "difference of two gauge potentials in the same gauge" → "1-form section of $\mathrm{Ad}\,P$ (no inhomogeneous term cancels)".** Whenever you see $A_1 - A_2$ in physics, recognise it as a tensor on $M$ — specifically a 1-form section of the adjoint bundle. This is true even though $A_1$ and $A_2$ individually are not tensors. The cancellation of inhomogeneous gauge terms is what makes this work. Applications: in lattice gauge theory, the *link variables* are gauge potentials in the lattice gauge; their *differences* are well-defined tensors that contribute to gauge-invariant observables.

**Trigger-reaction pattern: "expand around a reference connection" → "perturb by $\eta \in \Omega^1(M; \mathrm{Ad}\,P)$".** Whenever you need to perturbatively vary a connection, do so by an element of $\Omega^1(M; \mathrm{Ad}\,P)$. The variation is then a tensor on $M$, the resulting curvature has the affine expansion above, and the dynamics linearises to a tractable linear PDE on $\Omega^1(M; \mathrm{Ad}\,P)$. This is the universal recipe for linearisation in gauge theory.
