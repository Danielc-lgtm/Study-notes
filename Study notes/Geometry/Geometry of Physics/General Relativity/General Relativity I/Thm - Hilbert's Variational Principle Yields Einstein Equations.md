---
type: theorem
subject: general-relativity
prereqs:
  - "Def - Hilbert Action"
  - "Def - The Einstein Field Equations"
  - "Def - Stress-Energy Tensor"
  - "Def - Einstein Tensor"
tags: [physics, general-relativity, variational-principle, flagship]
---

# Notation

Spacetime $(M, g)$, signature $(+,-,-,-)$, geometrised units. The Hilbert action is $S_\text{grav} = \frac{1}{16\pi G}\int_M R\sqrt{-g}\, d^4x$. A variation of the inverse metric is denoted $\delta g^{\mu\nu}$, and we use $\delta g_{\mu\nu} = -g_{\mu\rho} g_{\nu\sigma}\, \delta g^{\rho\sigma}$ (this sign relation comes from $\delta(g^{\mu\rho} g_{\rho\nu}) = \delta \delta^\mu{}_\nu = 0$). The stress-energy tensor is defined variationally as $T_{\mu\nu} = -(2/\sqrt{-g}) \delta S_\text{matter}/\delta g^{\mu\nu}$. Full registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Statement

> **Theorem (Hilbert's variational principle for GR).** Let $(M, g)$ be a four-dimensional Lorentzian manifold and let $S = S_\text{grav}[g] + S_\text{matter}[g, \psi]$ be the total action, with
> $$S_\text{grav}[g] = \frac{1}{16\pi G}\int_M R\, \sqrt{-g}\, d^4x$$
> the Hilbert action and $S_\text{matter}[g, \psi]$ the action of all non-gravitational fields $\psi$, depending on the metric and the matter. Define the **matter stress-energy tensor** by
> $$T_{\mu\nu} = -\frac{2}{\sqrt{-g}} \frac{\delta S_\text{matter}}{\delta g^{\mu\nu}}.$$
> Then the variational principle $\delta S = 0$ under variations $\delta g^{\mu\nu}$ of compact support (and under variations $\delta\psi$ of the matter fields) yields:
>
> (i) the **Einstein field equations** $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$;
>
> (ii) the **equations of motion of the matter fields** (the Euler–Lagrange equations of $S_\text{matter}$ with respect to $\psi$).
>
> The variation of the gravitational part gives, schematically,
> $$\delta(R\sqrt{-g}) = \left(R_{\mu\nu} - \frac{1}{2}g_{\mu\nu} R\right)\sqrt{-g}\, \delta g^{\mu\nu} + \text{(total divergence)}.$$
>
> The total divergence (a four-divergence of a vector field) vanishes upon integration over a region in which the variation has compact support, by the divergence theorem.

The corollary is the **Gibbons–Hawking–York** statement: for spacetimes with boundary, the bulk action $\int R\sqrt{-g}\, d^4x$ alone is *not* stationary even when $\delta g$ vanishes on the boundary, because the boundary contribution involves $\delta(\partial g)$. The repair is to add a boundary term $\frac{1}{8\pi G}\int_{\partial M} K\sqrt{|h|}\, d^3 y$ (with $K$ the extrinsic curvature of $\partial M$ and $h$ the induced metric), which exactly cancels the offending boundary contribution.

---

# Motivation

This theorem establishes general relativity as a **Lagrangian field theory** — a member of the same family as electromagnetism (with Lagrangian $-\frac{1}{4} F_{\mu\nu} F^{\mu\nu}$), Yang-Mills theory, and the Standard Model. The Einstein field equations are not postulated independently; they are *derived* as the Euler-Lagrange equations of the simplest non-trivial scalar functional of the metric. This is structurally important for at least four reasons:

(i) **Uniqueness of the equations.** Together with **Lovelock's theorem**, this derivation shows that the Einstein equations are essentially forced by the requirements of (a) diffeomorphism invariance of the action, (b) second-order field equations, (c) being built from the metric and its derivatives. There is very little freedom for modification (only the addition of a cosmological constant in 4D).

(ii) **Stress-energy tensor definition.** The matter stress-energy tensor is *defined* by the variational formula $T_{\mu\nu} = -(2/\sqrt{-g}) \delta S_\text{matter}/\delta g^{\mu\nu}$. This is the unique definition that (a) makes $T_{\mu\nu}$ symmetric, (b) makes it conserved (when the matter equations of motion hold) via diffeomorphism invariance of $S_\text{matter}$ and Noether's second theorem, and (c) reduces to the special-relativistic stress-energy tensor in flat space. So the variational principle simultaneously defines the LHS *and* the RHS of the field equations.

(iii) **Symmetry-conservation correspondence.** Diffeomorphism invariance of $S_\text{matter}$ implies (via Noether) $\nabla^\mu T_{\mu\nu} = 0$ — local energy-momentum conservation. Diffeomorphism invariance of $S_\text{grav}$ implies (via Noether) $\nabla^\mu G_{\mu\nu} = 0$ — the contracted Bianchi identity. So *both* sides of the field equations are automatically divergence-free, making the equations consistent.

(iv) **Quantisation.** The variational principle is the starting point for any quantum theory of gravity: **canonical quantisation** (the Wheeler–DeWitt equation), **path integral** ($Z = \int \mathcal{D}g\, e^{iS/\hbar}$), **functional renormalisation [[Def - Group|group]]** (Weinberg's asymptotic safety). Without an action, none of these approaches is available.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source B₁: Any candidate gravitational theory with a Lagrangian formulation.* Given any proposed gravitational theory, if it can be cast as $S_\text{grav} = \int \mathcal{L}[g]\sqrt{-g}\, d^4x$ for some diffeomorphism-invariant scalar Lagrangian $\mathcal{L}$, then its field equations are the Euler-Lagrange equations of this functional. *Example problem*: in $f(R)$ gravity, $\mathcal{L} = (1/16\pi G) f(R)$, the field equations are $f'(R) R_{\mu\nu} - \frac{1}{2} f(R) g_{\mu\nu} - (\nabla_\mu \nabla_\nu - g_{\mu\nu} \Box) f'(R) = 8\pi G T_{\mu\nu}$ — a modification of Einstein's equations with extra terms involving derivatives of $f'(R)$.

*Source B₂: Diffeomorphism invariance of a matter action implies stress-energy conservation.* If $S_\text{matter}[g, \psi]$ is invariant under diffeomorphisms $x^\mu \to x^\mu + \xi^\mu$, then by Noether's second theorem, $\nabla^\mu T_{\mu\nu} = 0$ — conservation is automatic, not an extra postulate. *Bridge argument*: under an infinitesimal diffeomorphism, $\delta g^{\mu\nu} = -\nabla^\mu \xi^\nu - \nabla^\nu \xi^\mu$ and $\delta\psi = \mathcal{L}_\xi \psi$ (Lie derivative). The condition $\delta S_\text{matter} = 0$ for all $\xi$ vanishing on the boundary forces, after integration by parts and using matter equations of motion, $\int (\nabla^\mu T_{\mu\nu}) \xi^\nu \sqrt{-g}\, d^4x = 0$ for all $\xi$, hence $\nabla^\mu T_{\mu\nu} = 0$. *Example problem*: prove that the stress-energy tensor of a Klein-Gordon scalar field is conserved when the KG equation holds, using only diffeomorphism invariance of the action — without computing the divergence explicitly.

*Source B₃: An effective field theory expansion.* In effective field theory, the gravity Lagrangian is expanded in powers of curvature: $\mathcal{L} = \mathcal{L}_0 (\Lambda) + \mathcal{L}_2 (R) + \mathcal{L}_4 (R^2, R_{\mu\nu}^2, R_{\mu\nu\rho\sigma}^2) + \ldots$ The leading term gives the Einstein equations; higher terms are suppressed by powers of the Planck mass. *Bridge argument*: each term in the action contributes a tensor structure via its Euler-Lagrange equation, and Hilbert's principle systematically computes them. *Example problem*: derive the field equations of **Gauss-Bonnet gravity** in 5D from the action $\int(R + \alpha \mathcal{G})\sqrt{-g}\, d^5 x$ with $\mathcal{G}$ the Gauss-Bonnet term, using Hilbert's variational principle.

**Targets (Output Amplification).**

*Target T₁: Stress-energy tensor for any matter field.* Given the matter Lagrangian, applying the variational formula gives the stress-energy. For the electromagnetic Lagrangian $\mathcal{L} = -\frac{1}{16\pi} F_{\mu\nu} F^{\mu\nu}$, the resulting stress-energy is $T_{\mu\nu} = (1/4\pi)[F_{\mu\rho} F_\nu{}^\rho - \frac{1}{4} g_{\mu\nu} F_{\rho\sigma} F^{\rho\sigma}]$ — the Minkowski stress-energy tensor; see [[Ex - Stress-Energy Tensor of the Electromagnetic Field]]. For the scalar Lagrangian $\mathcal{L} = \frac{1}{2}\partial^\mu\phi\partial_\mu\phi - V(\phi)$, the stress-energy is $T_{\mu\nu} = \partial_\mu\phi\partial_\nu\phi - g_{\mu\nu}\mathcal{L}$. *Useful application*: in numerical simulations of relativistic matter, the stress-energy is read off from the Lagrangian rather than guessed.

*Target T₂: Action and equations of motion for any extension of GR.* Given any new gravitational structure (scalar-tensor theories, $f(R)$, Horndeski, etc.), Hilbert's principle gives the field equations directly. *Useful application*: most papers on **modified gravity** start from an action and derive equations via the variational principle, since the alternative (guessing the equations directly) is far less reliable.

*Target T₃: Path integral for quantum gravity.* The Hilbert action $S_\text{grav}$ is the exponent in the formal path integral $Z = \int \mathcal{D}g\, e^{iS_\text{grav}/\hbar}$. The classical limit $\hbar \to 0$ is the variational principle (stationary phase); the perturbative expansion is around the classical solutions. *Useful application*: **Euclidean quantum gravity** computes black hole entropy by evaluating the on-shell Euclidean action.

---

# Why Is It True

**The mechanism in one sentence: $\delta(R\sqrt{-g})/\delta g^{\mu\nu} = (R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R)\sqrt{-g}$ because the variation produces three terms — from $R$, from $\sqrt{-g}$, and a boundary term from the metric-variation contribution to the Ricci tensor — and the boundary term integrates to zero, leaving the Einstein tensor structure $R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$ exactly.**

To unpack:

**Piece 1: variation of $\sqrt{-g}$.** Using $\delta(\det A) = (\det A) \mathrm{tr}(A^{-1} \delta A)$ for an invertible matrix $A$, applied to $g$:
$$\delta(\det g_{\mu\nu}) = g\, g^{\mu\nu} \delta g_{\mu\nu} = -g\, g_{\mu\nu} \delta g^{\mu\nu},$$
(using $\delta g_{\mu\nu} = -g_{\mu\rho} g_{\nu\sigma} \delta g^{\rho\sigma}$). So $\delta\sqrt{-g} = -\frac{1}{2}\sqrt{-g}\, g_{\mu\nu} \delta g^{\mu\nu}$, which contributes the $-\frac{1}{2} g_{\mu\nu} R$ term to the final answer.

**Piece 2: variation of $R = g^{\mu\nu} R_{\mu\nu}$.** This has two contributions: $\delta R = R_{\mu\nu} \delta g^{\mu\nu} + g^{\mu\nu} \delta R_{\mu\nu}$. The first gives the $R_{\mu\nu}$ term directly. The second gives a **boundary term** — the Palatini identity says $\delta R_{\mu\nu} = \nabla_\rho \delta\Gamma^\rho{}_{\nu\mu} - \nabla_\nu \delta\Gamma^\rho{}_{\rho\mu}$, which when contracted with $g^{\mu\nu}$ and combined with $\sqrt{-g}$ becomes the divergence of a vector field $W^\rho = g^{\mu\nu}\delta\Gamma^\rho{}_{\mu\nu} - g^{\mu\rho}\delta\Gamma^\sigma{}_{\sigma\mu}$:
$$\int g^{\mu\nu}\, \delta R_{\mu\nu}\, \sqrt{-g}\, d^4x = \int \nabla_\rho W^\rho \sqrt{-g}\, d^4 x = \int_{\partial M} W^\rho\, dS_\rho.$$
For compactly-supported variations (i.e., $\delta g = 0$ on the boundary), the boundary integral vanishes, and the $\delta R_{\mu\nu}$ contribution drops out.

**Piece 3: putting it together.** Combining Pieces 1 and 2:
$$\delta(R\sqrt{-g}) = R_{\mu\nu}\sqrt{-g}\, \delta g^{\mu\nu} - \frac{1}{2} g_{\mu\nu} R\sqrt{-g}\, \delta g^{\mu\nu} + (\text{boundary term}).$$
Dropping the boundary term and requiring stationarity ($\int (\cdots) \delta g^{\mu\nu}\sqrt{-g}\, d^4x = 0$ for arbitrary $\delta g^{\mu\nu}$) gives
$$R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = 0 \quad \text{(vacuum case)},$$
the vacuum Einstein equations. Adding the matter action gives $G_{\mu\nu} = 8\pi G T_{\mu\nu}$.

**The deep "why" is gauge symmetry.** The Hilbert action is invariant under [[Def - Diffeomorphism|diffeomorphisms]] of $M$, and this gauge invariance forces (via Noether's second theorem) the divergence-freeness of $G_{\mu\nu}$. So the structure $R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$ that emerges from the variation is *not* a coincidence — it is forced by the requirement of gauge invariance, and the explicit calculation is the manifestation.

**The boundary term and Gibbons–Hawking–York.** For spacetimes with boundary, the boundary term $\int_{\partial M} W^\rho dS_\rho$ does *not* vanish even when $\delta g|_{\partial M} = 0$, because $W^\rho$ involves $\delta\Gamma$, which depends on $\partial\delta g$ — and these do not generally vanish at the boundary. The Gibbons-Hawking-York boundary term $S_\text{GHY} = \frac{1}{8\pi G}\int_{\partial M} K\sqrt{|h|}\, d^3 y$ is constructed to cancel exactly this offending boundary contribution, making the full action $S_\text{grav} + S_\text{GHY}$ stationary under compactly-supported metric variations.

---

# What Makes This Hard

The computational difficulty is in the variation of the Ricci tensor: $\delta R_{\mu\nu} = \nabla_\rho \delta\Gamma^\rho{}_{\nu\mu} - \nabla_\nu \delta\Gamma^\rho{}_{\rho\mu}$ — the **Palatini identity**. Getting this right requires careful tracking of which Christoffel-symbol variations are coordinate-dependent and which are tensorial (note: $\Gamma$ is not a tensor, but $\delta\Gamma$ *is* a tensor, because the inhomogeneous part of the transformation rule for $\Gamma$ is independent of the metric). The other tricky step is the variation of $\sqrt{-g}$, requiring the matrix identity $\delta\ln\det A = \mathrm{tr}(A^{-1}\delta A)$ and the relation between $\delta g_{\mu\nu}$ and $\delta g^{\mu\nu}$.

Common errors: (i) Mistaking $\delta R_{\mu\nu}$ for a non-tensorial expression (it *is* a tensor, even though $\Gamma$ is not); (ii) Forgetting the boundary term and concluding the variation is just $R_{\mu\nu}\sqrt{-g}$ (which would be Einstein's first guess, not the corrected version); (iii) Wrong sign in $\delta g_{\mu\nu}$ vs. $\delta g^{\mu\nu}$, leading to wrong sign in $\sqrt{-g}$ variation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Vary $R\sqrt{-g}$ with respect to $g^{\mu\nu}$ via three separate pieces: (a) the $\sqrt{-g}$ factor, (b) the $g^{\mu\nu}$ in $R = g^{\mu\nu} R_{\mu\nu}$, (c) the Ricci tensor $R_{\mu\nu}$ itself (via Palatini). Show that (c) is a total divergence, hence boundary, and discard it for compactly-supported variations. Combine (a) and (b) to get $(R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R)\sqrt{-g}$. Add matter; the matter variation gives $T_{\mu\nu}$ by definition.

**Subgoal decomposition:**

1. **Variation of the determinant:** Show $\delta\sqrt{-g} = -\frac{1}{2}\sqrt{-g}\, g_{\mu\nu}\, \delta g^{\mu\nu}$.
   - *Hint:* Use $\delta\det A = \det A\,\mathrm{tr}(A^{-1}\delta A)$ and $\delta g_{\mu\nu} = -g_{\mu\rho} g_{\nu\sigma}\delta g^{\rho\sigma}$.
   - *Why needed:* Gives the $-\frac{1}{2} g_{\mu\nu} R$ piece of the Einstein tensor.

2. **Palatini identity:** Show $\delta R_{\mu\nu} = \nabla_\rho \delta\Gamma^\rho{}_{\nu\mu} - \nabla_\nu \delta\Gamma^\rho{}_{\rho\mu}$, where $\delta\Gamma$ is a tensor (despite $\Gamma$ not being a tensor).
   - *Hint:* Differentiate $R^\rho{}_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho{}_{\nu\sigma} - \partial_\nu \Gamma^\rho{}_{\mu\sigma} + \Gamma\Gamma$-terms with respect to $g$, simplify using covariant derivatives (the partial-derivative terms become covariant because $\delta\Gamma$ is a tensor).
   - *Why needed:* Computes the variation of $R$ — the missing piece beyond direct $\delta g^{\mu\nu} R_{\mu\nu}$.

3. **Boundary term identification:** Show that $g^{\mu\nu}\delta R_{\mu\nu} = \nabla_\rho W^\rho$ for an explicit vector $W^\rho$.
   - *Hint:* Use the Palatini identity, contract with $g^{\mu\nu}$, integrate by parts.
   - *Why needed:* Identifies the contribution that vanishes for compactly-supported variations.

4. **Combine pieces for vacuum:** $\delta(R\sqrt{-g}) = (R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R)\sqrt{-g}\, \delta g^{\mu\nu} + \nabla_\rho(W^\rho \sqrt{-g})\, d^4x$.
   - *Hint:* Add Steps 1 and 2; the second term integrates to zero by the divergence theorem.
   - *Why needed:* Vacuum field equations.

5. **Matter variation gives $T_{\mu\nu}$:** Apply the definition $T_{\mu\nu} = -(2/\sqrt{-g})\delta S_\text{matter}/\delta g^{\mu\nu}$, so $\delta S_\text{matter} = -\frac{1}{2} T_{\mu\nu} \delta g^{\mu\nu}\sqrt{-g}\, d^4x$ (factor of $\frac{1}{2}$ from the convention).
   - *Hint:* Definitional.
   - *Why needed:* Source of the field equations.

6. **Full Einstein equations:** Set $\delta S = 0$ for $\delta g^{\mu\nu}$ of compact support; gather coefficients of $\delta g^{\mu\nu}$, divide by $1/(16\pi G)$ to put it in standard form.

---

# Lemma Decomposition

> [!note]- Lemma 1: Variation of the metric determinant
> **Statement:** $\delta\sqrt{-g} = -\frac{1}{2}\sqrt{-g}\, g_{\mu\nu}\, \delta g^{\mu\nu}$.
>
> **Hint:** Use Jacobi's formula $\delta(\det A) = (\det A)\, \mathrm{tr}(A^{-1}\delta A)$, then relate $\delta g_{\mu\nu}$ to $\delta g^{\mu\nu}$.
>
> **Why needed:** Provides the $-\frac{1}{2} g_{\mu\nu} R$ term in the Einstein tensor on the LHS of the field equations.
>
> > [!note]- Full proof
> > $\delta g = \delta\det(g_{\mu\nu}) = g\cdot g^{\mu\nu}\delta g_{\mu\nu}$. Using $\delta g_{\mu\nu} = -g_{\mu\rho} g_{\nu\sigma}\delta g^{\rho\sigma}$: $\delta g = g\cdot g^{\mu\nu}(-g_{\mu\rho} g_{\nu\sigma}\delta g^{\rho\sigma}) = -g\cdot g_{\rho\sigma}\delta g^{\rho\sigma}$. Then $\delta\sqrt{-g} = \delta(-g)^{1/2} = \frac{-\delta g}{2\sqrt{-g}} = \frac{g \cdot g_{\mu\nu}\delta g^{\mu\nu}}{2\sqrt{-g}} = -\frac{1}{2}\sqrt{-g}\, g_{\mu\nu}\delta g^{\mu\nu}$.

> [!note]- Lemma 2: Palatini identity
> **Statement:** $\delta R_{\mu\nu} = \nabla_\rho (\delta\Gamma^\rho{}_{\nu\mu}) - \nabla_\nu (\delta\Gamma^\rho{}_{\rho\mu})$, where $\delta\Gamma^\rho{}_{\mu\nu}$ is a tensor.
>
> **Hint:** Compute $\delta R^\rho{}_{\sigma\mu\nu}$ by differentiating the definition of the Riemann tensor; contract on $\rho = \mu$ to get $\delta R_{\sigma\nu}$. The partial derivative pieces, when added to the $\Gamma\delta\Gamma$ terms, simplify to covariant derivatives.
>
> **Why needed:** The variation of $R$ requires this; it's the only non-trivial step in computing $\delta R$.
>
> > [!note]- Full proof
> > $R^\rho{}_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho{}_{\nu\sigma} - \partial_\nu \Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$. Differentiating: $\delta R^\rho{}_{\sigma\mu\nu} = \partial_\mu (\delta\Gamma^\rho{}_{\nu\sigma}) - \partial_\nu (\delta\Gamma^\rho{}_{\mu\sigma}) + \delta\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} + \Gamma^\rho{}_{\mu\lambda}\delta\Gamma^\lambda{}_{\nu\sigma} - \delta\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma} - \Gamma^\rho{}_{\nu\lambda}\delta\Gamma^\lambda{}_{\mu\sigma}$. Re-grouping: this is exactly $\nabla_\mu(\delta\Gamma^\rho{}_{\nu\sigma}) - \nabla_\nu(\delta\Gamma^\rho{}_{\mu\sigma})$ — the partial-derivative terms become covariant derivatives because $\delta\Gamma$ is a tensor (the inhomogeneous parts of $\Gamma$'s transformation law cancel in the difference). Contracting $\rho = \mu$: $\delta R_{\sigma\nu} = \nabla_\mu(\delta\Gamma^\mu{}_{\nu\sigma}) - \nabla_\nu(\delta\Gamma^\mu{}_{\mu\sigma})$. Symmetrising and relabelling indices gives the stated form. The key fact that $\delta\Gamma$ is a tensor follows from $\Gamma'^\rho{}_{\mu\nu} = \partial x^\rho/\partial x'^\sigma \cdot \partial^2 x'^\sigma/\partial x^\mu \partial x^\nu + \ldots$ — the second-derivative term is independent of the metric, so it doesn't vary.

> [!note]- Lemma 3: Total-divergence form of $g^{\mu\nu}\delta R_{\mu\nu}$
> **Statement:** $g^{\mu\nu}\delta R_{\mu\nu}\, \sqrt{-g} = \nabla_\rho(W^\rho)\,\sqrt{-g}$ for an explicit vector $W^\rho = g^{\mu\nu}\delta\Gamma^\rho{}_{\nu\mu} - g^{\mu\rho}\delta\Gamma^\sigma{}_{\sigma\mu}$.
>
> **Hint:** Combine the Palatini identity (Lemma 2) with the fact that $\nabla_\rho g^{\mu\nu} = 0$, allowing $g^{\mu\nu}$ to pass through the covariant derivative.
>
> **Why needed:** Shows that this contribution to $\delta S_\text{grav}$ is a boundary term, vanishing for compactly-supported variations.
>
> > [!note]- Full proof
> > From Lemma 2: $g^{\mu\nu}\delta R_{\mu\nu} = g^{\mu\nu}[\nabla_\rho(\delta\Gamma^\rho{}_{\nu\mu}) - \nabla_\nu(\delta\Gamma^\rho{}_{\rho\mu})]$. Use $\nabla_\rho g^{\mu\nu} = 0$ to pass $g^{\mu\nu}$ inside: $= \nabla_\rho(g^{\mu\nu}\delta\Gamma^\rho{}_{\nu\mu}) - \nabla_\nu(g^{\mu\nu}\delta\Gamma^\rho{}_{\rho\mu}) = \nabla_\rho(g^{\mu\nu}\delta\Gamma^\rho{}_{\nu\mu}) - \nabla_\nu(g^{\nu\mu}\delta\Gamma^\rho{}_{\rho\mu})$. Relabel in the second term ($\nu \to \rho, \mu \to \mu$): $= \nabla_\rho(g^{\mu\nu}\delta\Gamma^\rho{}_{\nu\mu}) - \nabla_\rho(g^{\rho\mu}\delta\Gamma^\sigma{}_{\sigma\mu})$. So $W^\rho = g^{\mu\nu}\delta\Gamma^\rho{}_{\nu\mu} - g^{\rho\mu}\delta\Gamma^\sigma{}_{\sigma\mu}$, and the result is $\nabla_\rho W^\rho$. By the divergence theorem, $\int \nabla_\rho W^\rho\sqrt{-g}\, d^4x = \int_{\partial M} W^\rho\, dS_\rho$, which vanishes for compactly-supported $\delta g$.

> [!note]- Lemma 4: Vacuum Einstein equations from Hilbert variation
> **Statement:** $\delta(R\sqrt{-g}) = (R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R)\sqrt{-g}\, \delta g^{\mu\nu} + (\text{total divergence})$.
>
> **Hint:** Combine Lemmas 1 (variation of $\sqrt{-g}$), 2 (variation of $R_{\mu\nu}$), and 3 (boundary identification).
>
> **Why needed:** This is the central computation; demanding $\delta S_\text{grav} = 0$ for compactly-supported $\delta g^{\mu\nu}$ gives the vacuum field equations.
>
> > [!note]- Full proof
> > $\delta(R\sqrt{-g}) = (\delta R)\sqrt{-g} + R\,\delta\sqrt{-g}$. The first term: $\delta R = \delta(g^{\mu\nu} R_{\mu\nu}) = R_{\mu\nu}\delta g^{\mu\nu} + g^{\mu\nu}\delta R_{\mu\nu}$. By Lemma 3, the second piece is a total divergence. The second term: by Lemma 1, $R\delta\sqrt{-g} = -\frac{1}{2} R\sqrt{-g}\, g_{\mu\nu}\delta g^{\mu\nu}$. Combining: $\delta(R\sqrt{-g}) = R_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu} + \nabla_\rho W^\rho\sqrt{-g} - \frac{1}{2} g_{\mu\nu} R\sqrt{-g}\,\delta g^{\mu\nu} = (R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R)\sqrt{-g}\,\delta g^{\mu\nu} + \nabla_\rho W^\rho\sqrt{-g}$.

> [!note]- Lemma 5: Matter variation produces stress-energy
> **Statement:** $\delta S_\text{matter} = -\frac{1}{2}\int T_{\mu\nu}\, \delta g^{\mu\nu}\,\sqrt{-g}\, d^4x$, where $T_{\mu\nu} = -(2/\sqrt{-g})\delta S_\text{matter}/\delta g^{\mu\nu}$.
>
> **Hint:** This is the definition of $T_{\mu\nu}$.
>
> **Why needed:** Provides the RHS of the field equations.
>
> > [!note]- Full proof
> > By definition, $T_{\mu\nu} = -(2/\sqrt{-g})\delta S_\text{matter}/\delta g^{\mu\nu}$, equivalently $\delta S_\text{matter}/\delta g^{\mu\nu} = -\frac{1}{2}\sqrt{-g}\, T_{\mu\nu}$. So $\delta S_\text{matter} = \int (\delta S_\text{matter}/\delta g^{\mu\nu})\, \delta g^{\mu\nu}\, d^4 x = -\frac{1}{2}\int T_{\mu\nu}\, \delta g^{\mu\nu}\sqrt{-g}\, d^4x$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0** (well-posedness): We assume $\delta g^{\mu\nu}$ has compact support inside $M$, so all integrations by parts produce vanishing boundary terms. For spacetimes with boundary, the Gibbons-Hawking-York term is added; this does not change the bulk equations.
>
> **Step 1** (gravitational variation): By Lemmas 1, 2, 3, 4,
> $$\delta S_\text{grav} = \frac{1}{16\pi G}\int_M \delta(R\sqrt{-g})\, d^4x = \frac{1}{16\pi G}\int_M (R_{\mu\nu} - \tfrac{1}{2} g_{\mu\nu} R)\,\sqrt{-g}\,\delta g^{\mu\nu}\, d^4x.$$
> (The boundary term $\int\nabla_\rho W^\rho\sqrt{-g}\, d^4 x = 0$ for compactly-supported $\delta g$.)
>
> **Step 2** (matter variation): By Lemma 5,
> $$\delta S_\text{matter} = -\frac{1}{2}\int_M T_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}\, d^4x.$$
>
> **Step 3** (assembly): $\delta S = \delta S_\text{grav} + \delta S_\text{matter} = 0$ for arbitrary compactly-supported $\delta g^{\mu\nu}$ gives:
> $$\frac{1}{16\pi G}(R_{\mu\nu} - \tfrac{1}{2} g_{\mu\nu} R) - \frac{1}{2} T_{\mu\nu} = 0$$
> i.e.,
> $$R_{\mu\nu} - \tfrac{1}{2} g_{\mu\nu} R = 8\pi G\, T_{\mu\nu},$$
> the Einstein field equations $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$.
>
> **Step 4** (matter equations): Varying $\delta S_\text{matter}$ with respect to the matter fields $\psi$ gives, by the Euler-Lagrange equations of $S_\text{matter}$, the equations of motion of the matter (e.g., Maxwell's equations for the EM field, the Klein-Gordon equation for a scalar, the [[Def - Geodesic|geodesic]] equation for a free particle, etc.). $\square$

---

# Cross-Field Exercise Suggestions

**Application 1: Electromagnetism on curved spacetime.** Take $S_\text{matter} = -\frac{1}{16\pi}\int F_{\mu\nu} F^{\mu\nu}\sqrt{-g}\, d^4 x$ and verify that the variational definition $T_{\mu\nu} = -(2/\sqrt{-g})\delta S/\delta g^{\mu\nu}$ produces the Maxwell stress-energy tensor $T_{\mu\nu} = (1/4\pi)[F_{\mu\rho} F_\nu{}^\rho - \frac{1}{4} g_{\mu\nu} F^{\rho\sigma} F_{\rho\sigma}]$. This is done in detail in [[Ex - Stress-Energy Tensor of the Electromagnetic Field]].

**Application 2: Scalar field cosmology.** For a minimally coupled scalar field with action $S_\phi = \int [\frac{1}{2} g^{\mu\nu} \partial_\mu\phi \partial_\nu\phi - V(\phi)]\sqrt{-g}\, d^4 x$, derive the stress-energy tensor and verify it is conserved when the Klein-Gordon equation holds.

**Application 3: $f(R)$ gravity.** Replace the Hilbert action by $S_\text{grav} = (1/16\pi G)\int f(R)\sqrt{-g}\, d^4x$ and derive the modified field equations: $f'(R) R_{\mu\nu} - \frac{1}{2} f(R) g_{\mu\nu} - (\nabla_\mu\nabla_\nu - g_{\mu\nu}\Box) f'(R) = 8\pi G T_{\mu\nu}$. Show that for $f(R) = R - 2\Lambda$, this reduces to the Einstein equations with cosmological constant.

**Application 4: Lovelock gravity in higher [[Def - Dimension|dimensions]].** In 5D, add the **Gauss-Bonnet term** $\mathcal{G} = R^2 - 4R_{\mu\nu}R^{\mu\nu} + R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ to the action: $S = \int(R + \alpha \mathcal{G})\sqrt{-g}\, d^5x$. Show that the resulting field equations still have at most second-order derivatives of the metric — a feature of Lovelock theories.

---

# Bridges

- **[[Def - The Einstein Field Equations]]** — The variational principle is the *derivation* of the field equations, complementing the *axiomatic* presentation. The variational approach reveals their uniqueness (via Lovelock's theorem) and their connection to symmetries (conservation laws via Noether). It is also the gateway to quantisation.

- **Noether's second theorem** — The Hilbert variational principle is the prototypical application of Noether's second theorem: diffeomorphism invariance of the matter action implies $\nabla^\mu T_{\mu\nu} = 0$ identically; diffeomorphism invariance of the gravitational action implies $\nabla^\mu G_{\mu\nu} = 0$ identically. So *both sides* of the field equations are automatically divergence-free, making the equations consistent. The Noether identity formalism applies to any gauge-invariant Lagrangian field theory (Maxwell, Yang-Mills, GR), and the contracted Bianchi identity in GR is the Noether identity for diffeomorphism gauge symmetry.

- **[[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]]** — The Yang-Mills action $S_{YM} = -\frac{1}{4}\int F_{\mu\nu}^a F^{a\mu\nu}\sqrt{-g}\, d^4x$ has the same variational structure: varying with respect to the gauge field $A^a_\mu$ gives the Yang-Mills equations $D^\mu F_{\mu\nu}^a = J_\nu^a$, with gauge invariance forcing covariant conservation of the color current. The structural analogy between GR (Hilbert action $\propto \int R$) and Yang-Mills (action $\propto \int F^2$) is the basis for understanding gravity as a gauge theory; the key difference is the order (Hilbert is linear in curvature, Yang-Mills is quadratic), which makes gravity non-renormalisable but Yang-Mills renormalisable.

- **Path integral quantum gravity** — The variational principle $\delta S = 0$ is the saddle-point limit ($\hbar \to 0$) of the path integral $Z = \int \mathcal{D}g\, e^{iS_\text{grav}/\hbar}$. The classical field equations are stationary-phase configurations; quantum fluctuations are integrated over. In **Euclidean quantum gravity**, Wick rotation $t \to -i\tau$ converts the path integral to $Z = \int \mathcal{D}g\, e^{-S_E/\hbar}$, with the on-shell Euclidean action giving the **Bekenstein-Hawking entropy** of black holes (a remarkable on-shell result). The path integral interpretation makes the variational principle the bridge between classical and quantum gravity.

---

# Unlocked by This

> [!tip] Gibbons-Hawking-York Boundary Term *(from Black Hole Thermodynamics)*
> For spacetimes with boundary (or asymptotically flat spacetimes treated by adding a boundary at infinity), the Hilbert action is not stationary alone; the **Gibbons-Hawking-York boundary term** $S_\text{GHY} = \frac{1}{8\pi G}\int_{\partial M} K\sqrt{|h|}\, d^3 y$ (with $K$ the trace of extrinsic curvature) must be added. Evaluating the full Euclidean action on the Schwarzschild black hole gives $S_E = \beta M/2$, identified with the thermodynamic free energy, yielding the **Bekenstein-Hawking entropy** $S_\text{BH} = A/(4G\hbar)$ — the foundational result of black hole thermodynamics.

> [!tip] Wheeler-DeWitt Equation *(from Canonical Quantum Gravity)*
> The Hamiltonian decomposition of the Hilbert action (ADM formalism) gives a Hamiltonian that is purely a sum of constraints — the **Hamiltonian constraint** and the **momentum constraints**. Canonical quantisation promotes these to operators acting on wavefunctionals $\Psi[h_{ij}]$ over the configuration space of spatial metrics. The Hamiltonian constraint becomes the **Wheeler-DeWitt equation** $\hat{\mathcal{H}}\Psi = 0$, the central equation of canonical quantum gravity. The interpretation (the "problem of time" — the wavefunction has no explicit time evolution) is one of the deep conceptual difficulties.

> [!tip] Asymptotic Safety in Quantum Gravity *(from Functional Renormalisation Group)*
> Weinberg's **asymptotic safety** conjecture posits that quantum gravity, viewed as a non-perturbative QFT of the metric, has a non-trivial UV fixed point making the theory finite at all scales. The Hilbert action is the IR (low-energy) effective action; the RG flow generates higher-curvature terms ($R^2, R_{\mu\nu}R^{\mu\nu}, \ldots$) as one moves to higher energies. Computational evidence (from **functional renormalisation group** methods, e.g., Reuter's $f(R)$ truncation) supports the existence of the fixed point, though full control remains elusive.

> [!tip] Holographic Renormalisation *(from AdS/CFT Correspondence)*
> For asymptotically anti-de Sitter spacetimes, the on-shell Hilbert action diverges at the boundary. **Holographic renormalisation** adds counterterms (including the GHY term and others) to make the action finite. The renormalised action is identified, via **AdS/CFT**, with the generating functional of the dual conformal field theory — the gravitational action computes CFT correlators. This is the technical backbone of the gauge/gravity duality.

> [!tip] Modified Gravity from Action Principles *(from Beyond-Einstein Gravity)*
> Most modifications of GR — **scalar-tensor theories**, **$f(R)$ gravity**, **Horndeski theory**, **TeVeS** (relativistic MOND), **massive gravity** — are formulated by modifying the Hilbert action. The variational principle then gives the modified field equations directly. Comparing the predictions of these theories with observations (solar-system tests, cosmology, gravitational waves) constrains the allowed modifications. The simplicity and predictivity of the variational framework is what makes this systematic study possible.
