---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Curvature 2-Form on a Principal Bundle"
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Exterior Covariant Derivative on Associated Bundles"
  - "Def - Adjoint Bundle"
tags: [geometry, gauge-theory, principal-bundles, curvature]
---

# Notation

$P \to M$ a principal $G$-bundle, $\omega$ a connection 1-form, $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$ its [[Def - Curvature 2-Form on a Principal Bundle|curvature 2-form]]. In a local trivialisation by $s : U \to P$: $A = s^*\omega$, $F = s^*\Omega = dA + \tfrac{1}{2}[A, A]$. The induced connection on the [[Def - Adjoint Bundle|adjoint bundle]] $\mathrm{Ad}\,P$ has [[Def - Exterior Covariant Derivative on Associated Bundles|exterior covariant derivative]] $d_\nabla$ (also written $d_\omega$ or $d_A$).

---

# Statement

> **Theorem (Bianchi identity).** Let $\omega$ be a connection 1-form on a principal $G$-bundle $P \to M$ with curvature 2-form $\Omega$. Then
> $$
> d_\omega \Omega := d\Omega + [\omega, \Omega] = 0
> $$
> identically on $P$.
> 
> Equivalently, on the base $M$, the field strength $F \in \Omega^2(M; \mathrm{Ad}\,P)$ satisfies
> $$
> d_\nabla F = dF + [A, F] = 0
> $$
> in any local trivialisation, where $d_\nabla$ is the exterior covariant derivative on $\mathrm{Ad}\,P$-valued forms.
> 
> In matrix-group notation, the equation reads $dF + A \wedge F - F \wedge A = 0$, or in components
> $$
> \partial_\mu F^a_{\nu\rho} + \partial_\nu F^a_{\rho\mu} + \partial_\rho F^a_{\mu\nu} + f^a{}_{bc}(A^b_\mu F^c_{\nu\rho} + A^b_\nu F^c_{\rho\mu} + A^b_\rho F^c_{\mu\nu}) = 0.
> $$

> **Abelian special case ($G = U(1)$).** $[A, F] = 0$ identically, so the Bianchi identity reduces to $dF = 0$. In Minkowski-space components, this gives $\partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu} + \partial_\rho F_{\mu\nu} = 0$ — the geometric half of Maxwell's equations (Faraday's law $\nabla \times \mathbf{E} + \partial_t \mathbf{B} = 0$ together with the magnetic Gauss law $\nabla \cdot \mathbf{B} = 0$).

---

# Motivation

The Bianchi identity is a **geometric identity** — true for every connection on every principal bundle, by construction. It is *not* a dynamical equation (those are the Yang-Mills equations); it is a kinematic constraint that contains no physics — only geometry.

The motivation is two-stranded.

**First**, the Bianchi identity is the *automatic consequence* of the structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$ together with $d^2 = 0$ and the Jacobi identity for the bracket. So it is forced once you have a curvature — every connection's curvature satisfies it, no extra assumption needed.

**Second**, the Bianchi identity is the *covariant form* of "$dF = 0$ for an exact form". For abelian gauge theory, $F = dA$ is exact (locally), so $dF = d^2A = 0$ trivially — that is the standard "the divergence of an exact form is zero". For non-abelian gauge theory, $F$ is not exact (the connection $A$ is not globally defined), but the *covariant* derivative still vanishes — $d_\omega F = 0$, with the covariant correction $[A, F]$ accounting for the non-triviality of the connection.

Historically, the identity is named after **Luigi Bianchi**, who derived an analogous identity for the Riemann curvature tensor of Riemannian geometry: $R^a{}_{b\mu\nu;\rho} + R^a{}_{b\nu\rho;\mu} + R^a{}_{b\rho\mu;\nu} = 0$ — the cyclic-in-last-three-indices identity (the *second* Bianchi identity; the *first* is the algebraic $R^a{}_{[bcd]} = 0$). The principal-bundle Bianchi identity is the general form of the second Bianchi identity, valid for any gauge group, not just $O(n)$ of Riemannian geometry.

The physical content of the Bianchi identity, in the abelian case $G = U(1)$, is exactly "no magnetic monopoles" (in the absence of Dirac strings): $\nabla \cdot \mathbf{B} = 0$ and Faraday's law $\nabla \times \mathbf{E} + \partial_t \mathbf{B} = 0$. The non-abelian generalisation is the corresponding *colour-Gauss law* and *colour-Faraday law* of QCD and electroweak theory — same identities, but with the matrix indices of $\mathfrak{g}$ playing the role of colour or weak isospin.

The distinction between Bianchi (geometric, automatic) and Yang-Mills (dynamical, from an action principle) is one of the most important conceptual points in gauge theory. They look formally similar — both involve $d_\omega$ acting on a curvature-related quantity ($F$ for Bianchi, $\star F$ for Yang-Mills) — but they play utterly different roles. Bianchi is true for every connection; Yang-Mills selects which connections are physical.

---

# Sources and Targets

**Sources (input broadening).**

*Source 1: A connection 1-form $\omega$ on $P$.* By the structural equation, $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$, and Bianchi $d_\omega\Omega = 0$ follows automatically. Bridge: any connection automatically satisfies Bianchi. Example: the Levi-Civita connection on the orthonormal frame bundle satisfies the second Bianchi identity for the Riemann tensor.

*Source 2: A local gauge potential $A$ on a base chart.* By the local structural equation, $F = dA + \tfrac{1}{2}[A, A]$, and the local Bianchi $dF + [A, F] = 0$ follows. Bridge: local gauge data → local field strength → local Bianchi. Example: in QCD, the gluon field strength $G^a_{\mu\nu}$ satisfies the colour-Bianchi $D_\mu \tilde G^{a\,\mu\nu} = 0$ where $\tilde G^{\mu\nu} = \tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}G_{\rho\sigma}$ is the dual field strength.

*Source 3: Any flat connection ($\Omega = 0$).* Then Bianchi is trivially satisfied ($d_\omega \cdot 0 = 0$). Bridge: flat connection → trivial Bianchi → all curvature-based observables vanish. Example: any flat $G$-bundle (whose classifying map factors through $BG_{\text{disc}}$) has all $F$-derived characteristic classes vanishing in real cohomology.

**Targets (output amplification).**

*Target 1: Chern-Weil closure.* For any $\mathrm{Ad}$-invariant polynomial $p$ on $\mathfrak{g}$, the form $p(F) \in \Omega^{2k}(M; \mathbb{R})$ is closed: $d\,p(F) = 0$. Proof: $d\,p(F) = p'(F) \cdot dF = p'(F) \cdot (-[A, F]) = -[A, p'(F)\cdot F]$, but the bracket of $\mathrm{Ad}$-invariant polynomial values with $A$ vanishes (by $\mathrm{Ad}$-invariance of $p$), so $d\,p(F) = 0$. Combined with $\mathrm{Ad}$-invariance: the class $[p(F)]$ is independent of the connection.

*Target 2: Topological charge of Yang-Mills.* For $SU(2)$-bundle over $S^4$ or $\mathbb{R}^4$ with decay conditions, $\int \mathrm{tr}(F \wedge F)/8\pi^2 \in \mathbb{Z}$ is the **instanton number** — a topological invariant computable from $F$ via Bianchi-implied closedness.

*Target 3: Conservation of gauge currents.* Combined with the Yang-Mills equation $d_\omega \star F = j$, the Bianchi identity $d_\omega F = 0$ implies $d_\omega \star j = 0$ — covariant conservation of the gauge current $j$. This is the gauge-covariant analogue of "the current is divergenceless".

---

# Why Is It True

**The bolded one-liner:** *The Bianchi identity is the integrability condition $d^2 = 0$ on $\omega$, augmented by the Jacobi identity for the bracket — and the formula $d_\omega F = d_\omega(d\omega + \tfrac{1}{2}[\omega, \omega])$ collapses to zero by both.*

The intuition is direct. Start with the structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$. Take the exterior derivative:
$$
d\Omega = d^2\omega + \tfrac{1}{2}d[\omega, \omega] = 0 + \tfrac{1}{2}\big([d\omega, \omega] - [\omega, d\omega]\big) = [d\omega, \omega]
$$
using $d^2 = 0$ and the graded Leibniz of the bracket: $d[\alpha, \beta] = [d\alpha, \beta] + (-1)^p[\alpha, d\beta]$ for $\alpha$ of degree $p$ (here $p = 1$, so $-[\omega, d\omega] = -[d\omega, \omega]$... wait, signs):

Let me redo: $d[\omega, \omega] = [d\omega, \omega] + (-1)^1 [\omega, d\omega] = [d\omega, \omega] - [\omega, d\omega]$. Using graded symmetry of the bracket: $[\omega, d\omega] = (-1)^{1\cdot 2 + 1}[d\omega, \omega] = -[d\omega, \omega]$. So $d[\omega, \omega] = [d\omega, \omega] - (-[d\omega, \omega]) = 2[d\omega, \omega]$. Hence $\tfrac{1}{2}d[\omega, \omega] = [d\omega, \omega]$.

So $d\Omega = [d\omega, \omega]$.

Now substitute $d\omega = \Omega - \tfrac{1}{2}[\omega, \omega]$:
$$
d\Omega = [\Omega - \tfrac{1}{2}[\omega, \omega], \omega] = [\Omega, \omega] - \tfrac{1}{2}[[\omega, \omega], \omega].
$$
The second term involves $[[\omega, \omega], \omega]$, which by the graded Jacobi identity equals zero. (Jacobi: for $\omega$ of odd degree 1, the triple bracket $[\omega, [\omega, \omega]]$ vanishes by symmetry — verifiable directly from the graded Jacobi identity for three odd-degree forms.)

So $d\Omega = [\Omega, \omega] = -[\omega, \Omega]$ (graded symmetry: $[\Omega, \omega] = (-1)^{2\cdot 1 + 1}[\omega, \Omega] = -[\omega, \Omega]$). Hence
$$
d\Omega + [\omega, \Omega] = 0
$$
— the Bianchi identity. ∎

The proof is a one-line computation: the structural equation is differentiated, $d^2 = 0$ kills one term, the bracket Leibniz collapses another, and the Jacobi identity kills the last. The whole thing is the *integrability condition* on a connection 1-form, lifted to the curvature.

For the **local form** on the base: pull back along a section, use that $s^*$ commutes with $d$ and the bracket, and get $d F + [A, F] = 0$ in the local trivialisation. The component formula $\partial_\mu F^a_{\nu\rho} + \partial_\nu F^a_{\rho\mu} + \partial_\rho F^a_{\mu\nu} + f^a{}_{bc}(A^b_\mu F^c_{\nu\rho} + \text{cyclic}) = 0$ is the antisymmetric sum of partial derivatives plus the non-abelian correction.

For the **abelian case**, $[A, F] = 0$ identically, so the Bianchi identity reduces to $dF = 0$. In Minkowski-space components with $F = \tfrac{1}{2}F_{\mu\nu}dx^\mu \wedge dx^\nu$, $dF = \tfrac{1}{6}(\partial_\rho F_{\mu\nu} + \partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu})dx^\rho \wedge dx^\mu \wedge dx^\nu = 0$, which gives the four equations $\partial_{[\rho} F_{\mu\nu]} = 0$. In 3+1 dimensions, decomposing $F_{\mu\nu}$ into $\mathbf{E}$ (electric) and $\mathbf{B}$ (magnetic), this reads $\nabla \cdot \mathbf{B} = 0$ and $\nabla \times \mathbf{E} + \partial_t \mathbf{B} = 0$ — the geometric half of Maxwell.

---

# What Makes This Hard

The computational difficulty is the graded sign tracking in the bracket Leibniz and the Jacobi identity. For $\omega$ of degree 1, the formula $d[\omega, \omega] = 2[d\omega, \omega]$ involves a combination of the Leibniz signs and the graded antisymmetry of the bracket; getting these right requires care. Similarly, the Jacobi identity for three copies of $\omega$ (all of degree 1) gives $[\omega, [\omega, \omega]] = 0$ — a non-trivial fact, true by the graded Jacobi identity, but easy to miscount.

The conceptual difficulty is internalising that the Bianchi identity is a *geometric identity* — true for every connection, not a dynamical constraint. People often confuse it with the Yang-Mills equation $d_\omega \star F = 0$, which is the dynamical equation that connections must satisfy to be solutions of the equations of motion. The distinction: Bianchi is automatic; Yang-Mills is a constraint. They look formally similar (both $d_\omega$ acting on a curvature-related quantity), but they play opposite roles.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Differentiate the structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$. Use $d^2 = 0$ to kill $d^2\omega$. Use the graded Leibniz rule for the bracket with $d$ to expand $d[\omega, \omega]$. Substitute $d\omega = \Omega - \tfrac{1}{2}[\omega, \omega]$ from the structural equation. Use the Jacobi identity (in the form $[\omega, [\omega, \omega]] = 0$) to eliminate the triple-bracket term. The result is $d\Omega + [\omega, \Omega] = 0$.

**Subgoal decomposition:**

1. **Subgoal 1:** Compute $d\Omega = d^2\omega + \tfrac{1}{2}d[\omega, \omega]$.
   - *Hint:* Apply $d$ to the structural equation; use $d^2 = 0$.
   - *Why needed:* Sets up the calculation.

2. **Subgoal 2:** Expand $d[\omega, \omega]$ using graded Leibniz.
   - *Hint:* $d[\omega, \omega] = [d\omega, \omega] - [\omega, d\omega]$ for $\omega$ of degree 1; use graded symmetry $[\omega, d\omega] = -[d\omega, \omega]$ to simplify to $d[\omega, \omega] = 2[d\omega, \omega]$.
   - *Why needed:* Reduces the calculation to a single bracket term.

3. **Subgoal 3:** Substitute $d\omega = \Omega - \tfrac{1}{2}[\omega, \omega]$ into $[d\omega, \omega]$.
   - *Hint:* This gives $[d\omega, \omega] = [\Omega, \omega] - \tfrac{1}{2}[[\omega, \omega], \omega]$.
   - *Why needed:* Re-expresses everything in terms of $\Omega$ and $\omega$.

4. **Subgoal 4:** Apply Jacobi to eliminate the triple-bracket.
   - *Hint:* $[[\omega, \omega], \omega] = 0$ by graded Jacobi for three odd-degree forms.
   - *Why needed:* Eliminates the only non-Bianchi term.

5. **Subgoal 5:** Conclude $d\Omega + [\omega, \Omega] = 0$.
   - *Hint:* Combine subgoals 1–4 and use graded symmetry $[\Omega, \omega] = -[\omega, \Omega]$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $d[\omega, \omega] = 2[d\omega, \omega]$ for $\omega$ of degree 1
> **Statement:** For a $\mathfrak{g}$-valued 1-form $\omega$,
> $$
> d[\omega, \omega] = 2[d\omega, \omega].
> $$
> 
> **Hint:** Apply the graded Leibniz rule $d[\alpha, \beta] = [d\alpha, \beta] + (-1)^p[\alpha, d\beta]$ for $\alpha = \beta = \omega$ (both of degree 1). Get $d[\omega, \omega] = [d\omega, \omega] + (-1)^1[\omega, d\omega] = [d\omega, \omega] - [\omega, d\omega]$. Now use graded symmetry $[\omega, d\omega] = (-1)^{pq+1}[d\omega, \omega]$ with $p = 1, q = 2$: $[\omega, d\omega] = (-1)^{2+1}[d\omega, \omega] = -[d\omega, \omega]$. So $d[\omega, \omega] = [d\omega, \omega] - (-[d\omega, \omega]) = 2[d\omega, \omega]$.
> 
> **Why needed:** The first computational step in deriving Bianchi.
> 
> > [!note]- Full proof
> > Graded Leibniz: $d[\alpha, \beta] = [d\alpha, \beta] + (-1)^{|\alpha|}[\alpha, d\beta]$. For $\alpha = \beta = \omega$ (degree 1): $d[\omega, \omega] = [d\omega, \omega] - [\omega, d\omega]$.
> > 
> > Graded symmetry: $[\beta, \alpha] = (-1)^{|\alpha||\beta| + 1}[\alpha, \beta]$. For $\alpha = d\omega$ (degree 2), $\beta = \omega$ (degree 1): $[\omega, d\omega] = (-1)^{2 \cdot 1 + 1}[d\omega, \omega] = -[d\omega, \omega]$.
> > 
> > Substituting: $d[\omega, \omega] = [d\omega, \omega] - (-[d\omega, \omega]) = 2[d\omega, \omega]$.

> [!note]- Lemma 2: Jacobi triple-bracket $[\omega, [\omega, \omega]] = 0$ for $\omega$ of degree 1
> **Statement:** For a $\mathfrak{g}$-valued 1-form $\omega$,
> $$
> [\omega, [\omega, \omega]] = 0, \quad \text{equivalently} \quad [[\omega, \omega], \omega] = 0.
> $$
> 
> **Hint:** Graded Jacobi for three copies of $\omega$. The graded Jacobi identity for forms of degrees $p, q, r$ is $(-1)^{pr}[\alpha, [\beta, \gamma]] + (-1)^{qp}[\beta, [\gamma, \alpha]] + (-1)^{rq}[\gamma, [\alpha, \beta]] = 0$. For $\alpha = \beta = \gamma = \omega$ (all degree 1), this becomes $3 \cdot [\omega, [\omega, \omega]] = 0$ (all signs are $(-1)^1 = -1$, and all three triples are the same). Hence $[\omega, [\omega, \omega]] = 0$.
> 
> **Why needed:** Eliminates the triple-bracket term in the Bianchi derivation.
> 
> > [!note]- Full proof
> > Graded Jacobi: $(-1)^{pr}[\alpha, [\beta, \gamma]] + (-1)^{qp}[\beta, [\gamma, \alpha]] + (-1)^{rq}[\gamma, [\alpha, \beta]] = 0$ for forms $\alpha, \beta, \gamma$ of degrees $p, q, r$.
> > 
> > Apply with $\alpha = \beta = \gamma = \omega$, $p = q = r = 1$: $(-1)^1[\omega, [\omega, \omega]] + (-1)^1[\omega, [\omega, \omega]] + (-1)^1[\omega, [\omega, \omega]] = -3[\omega, [\omega, \omega]] = 0$. So $[\omega, [\omega, \omega]] = 0$. (Equivalently, by graded symmetry, $[[\omega, \omega], \omega] = (-1)^{2 \cdot 1 + 1}[\omega, [\omega, \omega]] = -[\omega, [\omega, \omega]] = 0$.)

> [!note]- Lemma 3: $d\Omega = [\Omega, \omega]$ (intermediate step)
> **Statement:** $d\Omega = [\Omega, \omega]$.
> 
> **Hint:** Differentiate $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$: $d\Omega = d^2\omega + \tfrac{1}{2}d[\omega, \omega] = 0 + [d\omega, \omega]$ by $d^2 = 0$ and Lemma 1. Substitute $d\omega = \Omega - \tfrac{1}{2}[\omega, \omega]$: $[d\omega, \omega] = [\Omega - \tfrac{1}{2}[\omega, \omega], \omega] = [\Omega, \omega] - \tfrac{1}{2}[[\omega, \omega], \omega] = [\Omega, \omega] - 0 = [\Omega, \omega]$ by Lemma 2.
> 
> **Why needed:** The intermediate form of Bianchi before rewriting as $d_\omega\Omega = 0$.
> 
> > [!note]- Full proof
> > $d\Omega = d(d\omega + \tfrac{1}{2}[\omega, \omega]) = d^2\omega + \tfrac{1}{2}d[\omega, \omega] = 0 + \tfrac{1}{2}\cdot 2[d\omega, \omega] = [d\omega, \omega]$ (using $d^2 = 0$ and Lemma 1).
> > 
> > Substitute $d\omega = \Omega - \tfrac{1}{2}[\omega, \omega]$: $[d\omega, \omega] = [\Omega, \omega] - \tfrac{1}{2}[[\omega, \omega], \omega] = [\Omega, \omega] - 0 = [\Omega, \omega]$ (Lemma 2 eliminates the second term).

> [!note]- Lemma 4: $[\Omega, \omega] = -[\omega, \Omega]$ (graded symmetry)
> **Statement:** $[\Omega, \omega] = -[\omega, \Omega]$.
> 
> **Hint:** Graded symmetry of the bracket of $\mathfrak{g}$-valued forms: $[\beta, \alpha] = (-1)^{pq+1}[\alpha, \beta]$. For $\alpha = \omega$ (degree 1), $\beta = \Omega$ (degree 2): $[\Omega, \omega] = (-1)^{2+1}[\omega, \Omega] = -[\omega, \Omega]$.
> 
> **Why needed:** Rewrites Lemma 3 in the form $d\Omega + [\omega, \Omega] = 0$.
> 
> > [!note]- Full proof
> > Graded symmetry: $[\beta, \alpha] = (-1)^{|\alpha||\beta| + 1}[\alpha, \beta]$. Apply with $\alpha = \omega, \beta = \Omega$: $[\Omega, \omega] = (-1)^{1 \cdot 2 + 1}[\omega, \Omega] = -[\omega, \Omega]$.

---

# Formal Proof

> [!note]- Complete formal proof
> Differentiate the structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$:
> $$
> d\Omega = d^2\omega + \tfrac{1}{2}d[\omega, \omega].
> $$
> 
> **$d^2\omega = 0$** (basic property of the exterior derivative).
> 
> **$d[\omega, \omega] = 2[d\omega, \omega]$** by Lemma 1 (graded Leibniz + graded symmetry, for $\omega$ of degree 1).
> 
> So $d\Omega = [d\omega, \omega]$.
> 
> **Substitute** $d\omega = \Omega - \tfrac{1}{2}[\omega, \omega]$ (from the structural equation): $[d\omega, \omega] = [\Omega, \omega] - \tfrac{1}{2}[[\omega, \omega], \omega] = [\Omega, \omega] - 0 = [\Omega, \omega]$, where the second term vanishes by Lemma 2 (Jacobi).
> 
> So $d\Omega = [\Omega, \omega] = -[\omega, \Omega]$ by Lemma 4 (graded symmetry).
> 
> Equivalently,
> $$
> d\Omega + [\omega, \Omega] = 0,
> $$
> which is the Bianchi identity $d_\omega\Omega = 0$. ∎
> 
> **Local form on the base.** Pull back along a local section $s : U \to P$. $s^*$ commutes with $d$ and with the bracket, so $s^*(d\Omega + [\omega, \Omega]) = d(s^*\Omega) + [s^*\omega, s^*\Omega] = dF + [A, F] = 0$.
> 
> In components for matrix groups: expanding $F = \tfrac{1}{2}F^a_{\mu\nu}T_a\,dx^\mu \wedge dx^\nu$ and $A = T_a A^a_\sigma\,dx^\sigma$, the identity $dF + [A, F] = 0$ becomes
> $$
> \partial_\mu F^a_{\nu\rho} + \partial_\nu F^a_{\rho\mu} + \partial_\rho F^a_{\mu\nu} + f^a{}_{bc}(A^b_\mu F^c_{\nu\rho} + A^b_\nu F^c_{\rho\mu} + A^b_\rho F^c_{\mu\nu}) = 0.
> $$

---

# Cross-Field Exercise Suggestions

**Second Bianchi identity for the Riemann curvature tensor.** For the Levi-Civita connection on the orthonormal frame bundle, the principal-bundle Bianchi identity specialises to the *second Bianchi identity* of Riemannian geometry: $R^a{}_{b[\mu\nu;\rho]} = 0$ (cyclic sum in the last three indices of the covariant derivative of the Riemann tensor). This is one of the foundational identities of Riemannian geometry, used in the derivation of the Einstein equations $\nabla_\mu G^{\mu\nu} = 0$ (covariant conservation of the Einstein tensor) and in proofs of curvature properties.

**Magnetic Gauss law and Faraday's law from $dF = 0$.** For the abelian $U(1)$-case in 3+1 dimensions, the Bianchi identity $dF = 0$ with $F = \tfrac{1}{2}F_{\mu\nu}dx^\mu \wedge dx^\nu$ gives $\partial_{[\rho}F_{\mu\nu]} = 0$. Decomposing into the electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$ via $F^{0i} = E^i$, $F^{ij} = -\varepsilon^{ijk}B^k$, the four equations reduce to $\nabla \cdot \mathbf{B} = 0$ (magnetic Gauss law: no monopoles) and $\nabla \times \mathbf{E} + \partial_t\mathbf{B} = 0$ (Faraday's law of induction). These are the *geometric* half of Maxwell — the half that says "the curvature is a closed form".

**Topological charge of an instanton.** For an $SU(2)$-bundle over $\mathbb{R}^4$ (or $S^4$ after compactification), the integrand $\mathrm{tr}(F \wedge F)/(8\pi^2)$ is closed (by Bianchi and $\mathrm{Ad}$-invariance of the trace) and integral. Its integral over $S^4$ is the instanton number, an integer classifying the bundle up to isomorphism. **Bianchi closure plus $\mathrm{Ad}$-invariance is exactly the Chern-Weil mechanism**: closed invariant polynomials in the curvature give topological invariants.

**Conservation of gauge currents.** Combined with the matter-coupled Yang-Mills equation $d_\omega \star F = \star j$ (where $j$ is the gauge current sourced by matter), Bianchi $d_\omega F = 0$ implies $d_\omega \star j = 0$ — the covariant conservation of the gauge current. This is the gauge-covariant analogue of "Noether currents are conserved". For QED, the conserved current is the electromagnetic 4-current; for QCD, the colour current; for the Standard Model, the various weak and hypercharge currents.

---

# Bridges

- **[[Thm - Cartan Structural Equation for Principal Connections|Cartan structural equation]]** — Bianchi is the *direct consequence* of the structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$ together with $d^2 = 0$ and Jacobi. The two theorems form a kinematic pair: structural equation defines curvature, Bianchi gives its automatic identity. No connection is exempt from either.

- **[[Def - Exterior Covariant Derivative on Associated Bundles|Exterior covariant derivative on $\mathrm{Ad}\,P$]]** — Bianchi reads $d_\nabla F = 0$ in the adjoint bundle, where $d_\nabla$ is the exterior covariant derivative. This makes Bianchi an instance of "the covariant derivative of the curvature is zero" — a fundamental property of any connection, generalising the algebraic Bianchi identity for the Riemann tensor.

- **$dF = 0$ for abelian gauge theory** — for $G = U(1)$, $[A, F] = 0$ and Bianchi reduces to $dF = 0$. This is the "magnetic Gauss + Faraday" half of Maxwell, and it is *manifestly* a consequence of $F$ being locally exact ($F = dA$). The non-abelian Bianchi is the covariant generalisation, with the $[A, F]$ term correcting for the non-globality of $A$.

- **Yang-Mills equation $d_\omega \star F = 0$** — Bianchi and Yang-Mills are *dual* equations: Bianchi is $d_\omega F = 0$ (kinematic), Yang-Mills is $d_\omega \star F = 0$ (dynamical). For **self-dual** connections in 4D ($F = \star F$), Yang-Mills follows from Bianchi automatically. The self-dual moduli space is the source of Donaldson invariants, instanton counting, and Seiberg-Witten theory.

- **Chern-Weil theory and characteristic classes** — Bianchi (combined with $\mathrm{Ad}$-invariance) is the mechanism by which invariant polynomials of $F$ produce closed forms on $M$, hence de Rham cohomology classes — the **Chern classes** for $U(n)$, **Pontryagin classes** for $O(n)$, **Euler class** for $SO(2k)$. These topological invariants of the bundle are independent of the connection, computable from any $\omega$ via $F$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

---

# Unlocked by This

> [!tip] Chern-Weil Theory *(from Algebraic Topology)*
> Bianchi + $\mathrm{Ad}$-invariance imply $d\,p(F) = 0$ for any $\mathrm{Ad}$-invariant polynomial $p$ on $\mathfrak{g}$. So $p(F)$ is a closed form on $M$, representing a de Rham cohomology class **independent of the connection $\omega$**. This is the **Chern-Weil construction**: characteristic classes (Chern, Pontryagin, Euler) of a principal bundle, computable from any connection. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

> [!tip] Yang-Mills and Self-Dual Connections *(from Yang-Mills Theory)*
> Bianchi $d_\omega F = 0$ together with the *self-duality* condition $F = \star F$ in 4D implies the Yang-Mills equation $d_\omega \star F = d_\omega F = 0$ automatically. So **self-dual connections are automatic solutions of Yang-Mills**, and they are the **instantons** of [[Gauge Theory IV — Yang–Mills Fields and Instantons|Gauge Theory IV]]. The self-dual moduli space (modulo gauge) is finite-dimensional with rich topology, the basis of Donaldson theory.

> [!tip] Magnetic Monopoles and the Failure of $F = dA$ Globally *(from Gauge Theory)*
> The abelian Bianchi $dF = 0$ implies $F$ is closed everywhere, hence locally exact ($F = dA_{\text{local}}$ on contractible charts). The *global* exactness ($F = dA_{\text{global}}$) requires the second cohomology class $[F] = 0 \in H^2(M; \mathbb{R})$ to vanish. For the Dirac monopole bundle on $S^2$, the integral $\int_{S^2} F = 4\pi g \neq 0$ shows $[F] \neq 0$ — so no global $A$ exists, and the Dirac string is the price of trying to write one anyway.

> [!tip] Gauge-Covariant Conservation Laws *(from Gauge Theory and Noether)*
> Combined with the matter-coupled Yang-Mills equation $d_\omega \star F = \star j$ (with $j$ the matter current), Bianchi $d_\omega F = 0$ implies $d_\omega \star j = 0$ — the gauge-covariant conservation of the matter current. This is the Noether-theorem statement of "gauge currents are conserved", made covariant under the gauge group. It is the foundation of "current algebra" in particle physics and the basis of Ward-Takahashi identities in quantum field theory.
