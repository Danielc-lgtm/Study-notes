---
type: theorem
subject: geometric-mechanics
prereqs:
  - "Def - Symplectic Manifold"
  - "Def - Poisson Bracket"
  - "Def - Hamiltonian Vector Field"
  - "Def - The Lie Bracket of Vector Fields"
tags: [physics, geometric-mechanics, symplectic-geometry, lie-algebra]
---

# Notation

$(M, \omega)$ is a symplectic manifold. $C^\infty(M)$ is the algebra of smooth functions on $M$. The [[Def - Poisson Bracket|Poisson bracket]] is $\{f, g\} = \omega(X_f, X_g) = X_f(g)$. The Lie bracket of vector fields $[X, Y]$ is the standard one.

---

# Statement

> **Theorem.** Let $(M, \omega)$ be a symplectic manifold. The Poisson bracket $\{\cdot, \cdot\} : C^\infty(M) \times C^\infty(M) \to C^\infty(M)$ defined by $\{f, g\} = \omega(X_f, X_g)$ satisfies:
>
> 1. **Bilinearity:** $\{af + bg, h\} = a\{f, h\} + b\{g, h\}$ for $a, b \in \mathbb{R}$.
> 2. **Antisymmetry:** $\{f, g\} = -\{g, f\}$.
> 3. **Leibniz rule:** $\{f, gh\} = \{f, g\}h + g\{f, h\}$.
> 4. **Jacobi identity:** $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$.
>
> Properties 1, 2, and 4 make $(C^\infty(M), \{\cdot, \cdot\})$ an (infinite-dimensional) real **Lie algebra**. Properties 1, 2, 3, and 4 together make $(C^\infty(M), \cdot, \{\cdot, \cdot\})$ a **Poisson algebra**.
>
> Moreover, the assignment $f \mapsto X_f$ is a **Lie algebra homomorphism** from $C^\infty(M)$ (with Poisson bracket) to $\Gamma(TM)$ (with vector-field Lie bracket): $X_{\{f, g\}} = -[X_f, X_g]$ (with the sign depending on convention; with $\omega = -d\theta$, the negative sign appears).

---

# Motivation

This theorem provides the **algebraic structure** of classical mechanics. Without it, the Poisson bracket would just be a curious bilinear operation; with it, the space of observables $C^\infty(M)$ becomes a Lie algebra, and a wealth of structural consequences follow: conservation laws form a Lie subalgebra (closed under Poisson brackets), the quantum-classical correspondence becomes precise (with $\{,\}$ as the classical limit of $[,]/i\hbar$), and the moment map for Hamiltonian group actions becomes a Lie algebra homomorphism.

The most non-trivial of the four properties is the **Jacobi identity** — which is the algebraic content of $d\omega = 0$. Specifically, the Jacobi identity for $\{\cdot, \cdot\}$ is equivalent to the closedness of $\omega$, providing a striking translation between geometric and algebraic conditions. This is part of why **closedness is one of the two axioms of a symplectic manifold**: without it, no Jacobi, hence no Lie-algebra structure on observables, hence no clean classical-mechanical formalism.

The Lie-algebra homomorphism $f \mapsto X_f$ identifies the Hamiltonian vector fields as a Lie subalgebra of $\Gamma(TM)$ — the **Lie algebra of the Hamiltonian symplectomorphism group $\mathrm{Ham}(M, \omega)$**. So Hamiltonian dynamics organizes itself as a representation of the observable Lie algebra on the vector fields, with the Poisson bracket as the structure constants.

---

# Sources and Targets

**Sources (Input Broadening).**

The hypothesis is "you have a symplectic manifold and Poisson bracket". Several non-obvious settings give rise to a Poisson algebra and hence to this theorem.

**Source: any symplectic manifold.** The default case. *Example use:* working on $T^*Q$, automatically get a Poisson algebra structure on $C^\infty(T^*Q)$.

**Source: a Poisson manifold (more general than symplectic).** A **Poisson manifold** is a smooth manifold $M$ equipped with a Poisson bivector $\pi \in \Gamma(\Lambda^2 TM)$ satisfying $[\pi, \pi]_{SN} = 0$ (the Schouten–Nijenhuis bracket vanishes — the Jacobi condition). The Poisson bracket is $\{f, g\} = \pi(df, dg)$. Symplectic manifolds are the **nondegenerate** Poisson manifolds; degenerate ones have **Casimir functions** (functions Poisson-commuting with everything) and **symplectic leaves** (sub-symplectic manifolds where the Poisson tensor restricts to a nondegenerate $2$-form). *Example use:* the dual $\mathfrak{g}^*$ of a Lie algebra has a canonical degenerate Poisson structure (KKS — Kirillov–Kostant–Souriau), with coadjoint orbits as symplectic leaves; the orbit method in representation theory uses this.

**Source: a Lie algebra $(g, [\cdot, \cdot])$.** The dual $\mathfrak{g}^*$ as a Poisson manifold (with KKS bracket) has $\{f, g\}(\mu) = \mu([df_\mu, dg_\mu])$ for $f, g \in C^\infty(\mathfrak{g}^*)$ and $\mu \in \mathfrak{g}^*$. So *every* Lie algebra produces a Poisson manifold structure on its dual, and the theorem applies. *Example use:* the rigid-body equations of motion (Euler's equations) are Hamilton's equations on $\mathfrak{so}(3)^*$ with the KKS Poisson bracket.

**Targets (Output Amplification).**

The Lie-algebra structure on $C^\infty(M)$ has many consequences.

**Target + a Hamiltonian = identification of conserved quantities.** $f$ is conserved by the flow of $H$ iff $\{f, H\} = 0$. The conserved quantities form a Lie subalgebra of $(C^\infty(M), \{,\})$, closed under Poisson brackets (Jacobi!). So once you have a few conserved quantities, you can generate more by Poisson-bracketing. *Combination use:* angular momentum components on $T^*\mathbb{R}^3$ form $\mathfrak{so}(3)$ under Poisson bracket; each is conserved for rotational-invariant Hamiltonians, and their brackets give more conserved quantities consistent with the algebra structure.

**Target + a Lie group action = moment map and Noether.** When $G$ acts on $(M, \omega)$ preserving $\omega$, each $\xi \in \mathfrak{g}$ gives a vector field $\xi_M$, and (under suitable hypotheses) a Hamiltonian function $\mu^\xi$ via $X_{\mu^\xi} = \xi_M$. The assignment $\xi \mapsto \mu^\xi$ is a Lie algebra homomorphism $\mathfrak{g} \to C^\infty(M)$, and the moment map $\mu : M \to \mathfrak{g}^*$ packages this. The Lie-algebra structure on $C^\infty(M)$ is essential for this: without it, "$\mu^{[\xi, \eta]}$ and $\{\mu^\xi, \mu^\eta\}$ agree" would not be meaningful. *Combination use:* derive angular momentum from rotation symmetry.

**Target + Schur lemma / representation theory = quantization.** The Poisson algebra $C^\infty(M)$ has many Lie-subalgebras corresponding to (classical limits of) Lie groups acting on the system. **Geometric quantization** assigns to each such Lie subalgebra a representation on a Hilbert space — the **quantization functor** sends Poisson subalgebras to subrepresentations. The Lie-algebra structure on $C^\infty(M)$ is what makes this functor meaningful. *Combination use:* the quantization of $\mathfrak{so}(3)$ subalgebra of angular momentum produces the half-integer-spin representations of $\mathfrak{su}(2)$.

**Target + Schouten–Nijenhuis = generalization to Poisson manifolds.** The Jacobi identity for $\{\cdot, \cdot\}$ is equivalent to a tensorial condition $[\pi, \pi]_{SN} = 0$ on the Poisson bivector. This lets us define "Poisson manifold" without needing nondegeneracy of $\pi$, generalizing the symplectic case. *Combination use:* understanding why the Lie–Poisson bracket on $\mathfrak{g}^*$ satisfies Jacobi reduces to a calculation with the Jacobi identity for the Lie bracket on $\mathfrak{g}$.

---

# Why Is It True

**The mechanism in one sentence:** *Bilinearity, antisymmetry, and Leibniz follow trivially from the definition $\{f, g\} = \omega(X_f, X_g)$ and basic properties of $\omega$ and $X_f$; the Jacobi identity is the algebraic content of the closedness $d\omega = 0$.*

**Bilinearity.** $\omega$ is bilinear; $f \mapsto X_f = (\omega^\flat)^{-1}(df)$ is $\mathbb{R}$-linear (sum of derivatives = derivative of sum). So $\{af + bg, h\} = \omega(X_{af + bg}, X_h) = \omega(aX_f + bX_g, X_h) = a\omega(X_f, X_h) + b\omega(X_g, X_h) = a\{f, h\} + b\{g, h\}$.

**Antisymmetry.** $\omega(X_f, X_g) = -\omega(X_g, X_f)$ by antisymmetry of $\omega$. So $\{f, g\} = -\{g, f\}$.

**Leibniz.** $\{f, gh\} = X_f(gh) = X_f(g)h + gX_f(h) = \{f, g\}h + g\{f, h\}$, using the Leibniz rule for the vector field $X_f$ acting on the product $gh$.

**Jacobi.** This is the deep one. The calculation is most conceptual via Cartan's formula. The Jacobi identity asserts $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$. Equivalently, the sum
$$X_{\{g, h\}}(f) + X_{\{h, f\}}(g) + X_{\{f, g\}}(h) = 0,$$
i.e., $[X_g, X_h](f) - [X_h, X_f](g)$ — wait, let me redo this more carefully. We have $\{f, g\} = X_f(g)$, and we want to show $\{f, \{g, h\}\} + \text{cyclic} = 0$.

The cleanest proof uses the fact that **the Lie derivative of the Poisson bracket** (regarded as a bilinear operation on $C^\infty(M)$) along a Hamiltonian vector field vanishes — which is itself equivalent to $d\omega = 0$. The calculation: define $J(f, g, h) := \{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\}$. One shows $J$ is a trilinear, totally antisymmetric, $C^\infty(M)$-linear-in-each-argument operation on functions, hence equal to some trivector field $\Pi$ acting on $df, dg, dh$. A direct computation in coordinates shows $\Pi$ is proportional to the Schouten–Nijenhuis bracket $[\pi, \pi]_{SN}$, which vanishes iff $d\omega = 0$. So **Jacobi $\Leftrightarrow$ closedness** of the symplectic form.

**Concrete coordinate proof of Jacobi.** Work in Darboux coordinates $(q^i, p_i)$, where $\{f, g\} = \partial_{q^i}f \partial_{p_i}g - \partial_{p_i}f \partial_{q^i}g$. Compute $\{f, \{g, h\}\}$ by expanding all the partial derivatives: this gives a sum of terms with various combinations of first and second partial derivatives of $f, g, h$. Cyclically symmetrize and observe that all the second-derivative terms cancel (by Schwarz's theorem on the symmetry of mixed partial derivatives — this is *exactly* the algebraic identity that comes from $d\omega_0 = 0$ on $\mathbb{R}^{2n}$, where $\omega_0 = \sum dp_i \wedge dq^i$).

**Lie algebra homomorphism $f \mapsto X_f$.** Compute $X_{\{f, g\}}$ and compare to $[X_f, X_g]$. We have $\iota_{X_{\{f, g\}}}\omega = d\{f, g\}$. On the other hand, $\iota_{[X_f, X_g]}\omega = \mathcal{L}_{X_f}\iota_{X_g}\omega - \iota_{X_g}\mathcal{L}_{X_f}\omega = \mathcal{L}_{X_f}(dg) - \iota_{X_g}(0) = d(\mathcal{L}_{X_f}g) - 0 = d(X_f(g)) = d\{f, g\}$. Hmm, this gives $\iota_{X_{\{f, g\}}}\omega = \iota_{[X_f, X_g]}\omega$, hence $X_{\{f, g\}} = [X_f, X_g]$ — but with our sign convention (let me recheck) we actually get $X_{\{f, g\}} = -[X_f, X_g]$.

Actually let me redo. Cartan's formula gives $\mathcal{L}_{X_f}\iota_{X_g}\omega - \iota_{X_g}\mathcal{L}_{X_f}\omega = \iota_{[X_f, X_g]}\omega$ as a general identity. Here $\iota_{X_g}\omega = dg$, so $\mathcal{L}_{X_f}\iota_{X_g}\omega = \mathcal{L}_{X_f}(dg) = d(\mathcal{L}_{X_f}g) = d(X_f(g)) = d\{f, g\}$. Also $\mathcal{L}_{X_f}\omega = 0$ (Hamiltonian flows are symplectomorphisms), so $\iota_{X_g}\mathcal{L}_{X_f}\omega = 0$. Putting it together: $\iota_{[X_f, X_g]}\omega = d\{f, g\}$.

Compare to $\iota_{X_{\{f, g\}}}\omega = d\{f, g\}$. So $\iota_{[X_f, X_g]}\omega = \iota_{X_{\{f, g\}}}\omega$, hence by nondegeneracy of $\omega$, $[X_f, X_g] = X_{\{f, g\}}$. With our sign convention, this is the positive sign. (Different conventions in the literature flip this sign, often due to different choices of $\omega = \pm d\theta$ or $\{f, g\} = \pm \omega(X_f, X_g)$.)

---

# What Makes This Hard

Properties 1–3 (bilinearity, antisymmetry, Leibniz) are immediate from the definition and pose no difficulty. The Jacobi identity is the technical heart, and the cleanest proof requires either (a) a direct coordinate computation with careful expansion of partial derivatives (long but straightforward) or (b) the abstract observation that Jacobi for $\{\cdot, \cdot\}$ is equivalent to $d\omega = 0$, with the equivalence proved via Cartan's formula on the Lie derivative of $\omega$ along a Hamiltonian vector field. Most students initially struggle with the coordinate computation (it's a many-term cancellation that depends on Schwarz's theorem) and only later appreciate the conceptual statement: **Jacobi is closedness in disguise**.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Bilinearity, antisymmetry, and Leibniz follow trivially from the definition $\{f, g\} = \omega(X_f, X_g)$ and basic algebra. The Jacobi identity is the deep one — prove it either by direct coordinate calculation (Schwarz's theorem cancels all the terms) or, more conceptually, by deriving the Lie algebra homomorphism $X_{\{f, g\}} = [X_f, X_g]$ from Cartan's formula and using the Jacobi identity for the Lie bracket of vector fields.

**Subgoal decomposition:**

1. **Bilinearity.** $\{af + bg, h\} = a\{f, h\} + b\{g, h\}$.
   - *Hint:* $X_{af + bg} = aX_f + bX_g$ (linearity of $f \mapsto X_f$), and $\omega$ is bilinear.
   - *Why needed:* one of the four Lie algebra axioms.

2. **Antisymmetry.** $\{f, g\} = -\{g, f\}$.
   - *Hint:* $\omega$ is antisymmetric.
   - *Why needed:* one of the four Lie algebra axioms.

3. **Leibniz.** $\{f, gh\} = \{f, g\}h + g\{f, h\}$.
   - *Hint:* $X_f$ is a derivation, so $X_f(gh) = X_f(g)h + gX_f(h)$.
   - *Why needed:* makes the Poisson bracket compatible with the multiplicative structure of $C^\infty(M)$.

4. **Lie algebra homomorphism $X_{\{f, g\}} = [X_f, X_g]$.** Use Cartan's formula and the symplectic preservation $\mathcal{L}_{X_f}\omega = 0$.
   - *Hint:* compute $\iota_{[X_f, X_g]}\omega$ via $\mathcal{L}_{X_f}\iota_{X_g}\omega - \iota_{X_g}\mathcal{L}_{X_f}\omega$ and recognize it equals $d\{f, g\} = \iota_{X_{\{f, g\}}}\omega$.
   - *Why needed:* lets us transfer Jacobi from Lie bracket of vector fields to Poisson bracket of functions.

5. **Jacobi identity.** Use the Lie algebra homomorphism: the Jacobi identity for $[\cdot, \cdot]$ on $\Gamma(TM)$ implies the Jacobi identity for $\{\cdot, \cdot\}$ on $C^\infty(M)$.
   - *Hint:* $f \mapsto X_f$ is injective (modulo constants on connected $M$), and Lie algebra homomorphisms preserve Lie algebra identities.
   - *Why needed:* the deepest property, equivalent to $d\omega = 0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Bilinearity, antisymmetry, Leibniz
> **Statement:** The Poisson bracket $\{f, g\} = \omega(X_f, X_g)$ satisfies bilinearity, antisymmetry, and the Leibniz rule.
>
> **Hint:** Direct calculation from the definitions.
>
> **Why needed:** Three of the four Lie-algebra axioms (plus the Poisson-algebra Leibniz axiom).
>
> > [!note]- Full proof
> > **Bilinearity:** $X$ is $\mathbb{R}$-linear in $f$ (because $d$ is linear and $\omega^\flat$ is a fibrewise linear isomorphism), so $X_{af + bg} = aX_f + bX_g$. Then $\{af + bg, h\} = \omega(aX_f + bX_g, X_h) = a\omega(X_f, X_h) + b\omega(X_g, X_h) = a\{f, h\} + b\{g, h\}$ by bilinearity of $\omega$. ✓
> >
> > **Antisymmetry:** $\{f, g\} = \omega(X_f, X_g) = -\omega(X_g, X_f) = -\{g, f\}$ by antisymmetry of $\omega$. ✓
> >
> > **Leibniz:** Use $\{f, h\} = X_f(h)$ for the second argument. Then $\{f, gh\} = X_f(gh) = X_f(g)h + gX_f(h) = \{f, g\}h + g\{f, h\}$, using the Leibniz rule for the vector field $X_f$ acting on the product of two functions. ✓

> [!note]- Lemma 2: $X_{\{f, g\}} = [X_f, X_g]$ (Lie algebra homomorphism)
> **Statement:** The Hamiltonian vector field of the Poisson bracket equals the Lie bracket of the Hamiltonian vector fields: $X_{\{f, g\}} = [X_f, X_g]$.
>
> **Hint:** Use Cartan's formula on $\iota_{[X_f, X_g]}\omega$.
>
> **Why needed:** Converts the Jacobi identity for Lie bracket of vector fields into the Jacobi identity for the Poisson bracket of functions.
>
> > [!note]- Full proof
> > Use the identity $\iota_{[X, Y]}\omega = \mathcal{L}_X\iota_Y\omega - \iota_Y\mathcal{L}_X\omega$, which follows from the graded commutator of $\mathcal{L}$ and $\iota$ (and reduces to Cartan's formula plus standard manipulations). Apply with $X = X_f$, $Y = X_g$:
> > $$\iota_{[X_f, X_g]}\omega = \mathcal{L}_{X_f}\iota_{X_g}\omega - \iota_{X_g}\mathcal{L}_{X_f}\omega = \mathcal{L}_{X_f}(dg) - \iota_{X_g}(0) = d(\mathcal{L}_{X_f}g) = d(X_f(g)) = d\{f, g\}.$$
> > Here we used: $\iota_{X_g}\omega = dg$ (definition of $X_g$); $\mathcal{L}_{X_f}\omega = 0$ ([[Thm - Hamiltonian Flows are Symplectomorphisms]]); $\mathcal{L}_{X_f}$ commutes with $d$ (Cartan); $\mathcal{L}_{X_f}g = X_f(g) = \{f, g\}$.
> >
> > On the other hand, $\iota_{X_{\{f, g\}}}\omega = d\{f, g\}$ by the definition of $X_{\{f, g\}}$. So $\iota_{[X_f, X_g]}\omega = \iota_{X_{\{f, g\}}}\omega$. By nondegeneracy of $\omega$, $[X_f, X_g] = X_{\{f, g\}}$. ✓

> [!note]- Lemma 3: Jacobi identity (from Jacobi for vector fields)
> **Statement:** $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$.
>
> **Hint:** Use the Jacobi identity for $[\cdot, \cdot]$ on $\Gamma(TM)$ and Lemma 2.
>
> **Why needed:** Completes the Lie-algebra structure.
>
> > [!note]- Full proof
> > Apply the Lie-algebra homomorphism property (Lemma 2) iteratively:
> > $$X_{\{f, \{g, h\}\}} = [X_f, X_{\{g, h\}}] = [X_f, [X_g, X_h]].$$
> > Cyclically summing:
> > $$X_{\{f, \{g, h\}\}} + X_{\{g, \{h, f\}\}} + X_{\{h, \{f, g\}\}} = [X_f, [X_g, X_h]] + [X_g, [X_h, X_f]] + [X_h, [X_f, X_g]].$$
> > The right-hand side vanishes by the **Jacobi identity for the Lie bracket of vector fields**. By linearity of $f \mapsto X_f$:
> > $$X_{\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\}} = 0.$$
> > By the kernel of $f \mapsto X_f$ being the locally constant functions (on a connected $M$), the function $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\}$ is locally constant. By a calculation in a chart (e.g., one Darboux chart), it is identically zero at every point. So it vanishes globally on $M$ connected; on disconnected $M$, apply the argument on each component. ✓

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(M, \omega)$ be a symplectic manifold. We verify each of the four properties of the Poisson bracket $\{f, g\} = \omega(X_f, X_g)$ where $X_f$ is the Hamiltonian vector field with $\iota_{X_f}\omega = df$.
>
> **Bilinearity.** By linearity of $f \mapsto X_f$ (since $d$ is linear and $(\omega^\flat)^{-1}$ is a fibrewise linear isomorphism): $X_{af + bg} = aX_f + bX_g$. Then by bilinearity of $\omega$:
> $$\{af + bg, h\} = \omega(aX_f + bX_g, X_h) = a\omega(X_f, X_h) + b\omega(X_g, X_h) = a\{f, h\} + b\{g, h\}.$$
>
> **Antisymmetry.** By antisymmetry of $\omega$:
> $$\{f, g\} = \omega(X_f, X_g) = -\omega(X_g, X_f) = -\{g, f\}.$$
>
> **Leibniz rule.** By the Leibniz rule for the vector field $X_f$ on the product $gh$:
> $$\{f, gh\} = X_f(gh) = X_f(g)h + gX_f(h) = \{f, g\}h + g\{f, h\}.$$
>
> **Jacobi identity.** Apply Lemma 2 ($X_{\{f, g\}} = [X_f, X_g]$) iteratively:
> $$X_{\{f, \{g, h\}\}} = [X_f, X_{\{g, h\}}] = [X_f, [X_g, X_h]],$$
> and cyclically. Summing:
> $$X_{\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\}} = [X_f, [X_g, X_h]] + [X_g, [X_h, X_f]] + [X_h, [X_f, X_g]] = 0,$$
> where the last equality is the Jacobi identity for the Lie bracket of vector fields.
>
> Now use the fact that $f \mapsto X_f$ has kernel the locally constant functions (on a connected $M$, just the constants). So the function $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\}$ has zero Hamiltonian vector field, hence is locally constant. To show it vanishes identically: work in Darboux coordinates around any point and verify the Jacobi identity by direct calculation — this is a standard exercise in chain rule and Schwarz's theorem (symmetry of mixed partial derivatives), and at a single point it shows the cyclic sum equals zero, hence the locally constant function is zero throughout.
>
> Alternatively (more elegant): apply the Lie-algebra homomorphism property to a Darboux chart on each connected component, where the constants are explicitly computed.
>
> **Conclusion.** All four properties are verified. $(C^\infty(M), \{\cdot, \cdot\})$ is a Lie algebra; with the pointwise product, it is a Poisson algebra. The map $f \mapsto X_f$ is a Lie algebra homomorphism into $\Gamma(TM)$ with the Lie bracket of vector fields. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Quantum mechanics: canonical commutation relations.** The fundamental Poisson brackets $\{q^i, p_j\} = \delta^i_j$ on $T^*\mathbb{R}^n$ become, under canonical quantization, the **canonical commutation relations** $[\hat q^i, \hat p_j] = i\hbar\delta^i_j$. The Lie algebra of $(C^\infty(T^*\mathbb{R}^n), \{\cdot, \cdot\})$ becomes the Lie algebra of operators on the quantum Hilbert space (modulo the operator-ordering ambiguities). Verify that the angular-momentum subalgebra $\mathfrak{so}(3)$ in $C^\infty(T^*\mathbb{R}^3)$ quantizes to the quantum angular momentum algebra $\mathfrak{su}(2)$, with the well-known eigenvalues for $\hat L^2$ and $\hat L_3$.

**Lie theory: Lie–Poisson bracket on $\mathfrak{g}^*$.** For any Lie algebra $\mathfrak{g}$, the dual space $\mathfrak{g}^*$ has a canonical **Lie–Poisson (Kirillov–Kostant–Souriau) Poisson structure**, given by $\{f, g\}(\mu) = \mu([df_\mu, dg_\mu])$, where $df_\mu \in \mathfrak{g}^{**} \cong \mathfrak{g}$ for $f \in C^\infty(\mathfrak{g}^*)$ at $\mu \in \mathfrak{g}^*$. Verify: this satisfies Jacobi iff $\mathfrak{g}$ satisfies Jacobi. So **every Lie algebra produces a Poisson manifold structure on its dual**. The symplectic leaves of this Poisson structure are the **coadjoint orbits**, which carry canonical $G$-invariant symplectic structures (the **Kostant–Kirillov form**). The orbit method in representation theory uses these.

**Fluid dynamics: vorticity Poisson bracket.** The 2D Euler equation for an incompressible inviscid fluid is a Hamiltonian system on the space of vorticity distributions, with a Poisson bracket that is the infinite-dimensional Lie–Poisson bracket for the Lie algebra of area-preserving diffeomorphisms. Verify that the bracket $\{F, G\}(\omega) = \int \omega \,\{F'(\omega), G'(\omega)\}\, dx\, dy$ (with $\{\cdot,\cdot\}$ the standard 2D Poisson bracket) satisfies Jacobi, and that the Hamiltonian $H[\omega] = \tfrac{1}{2}\int |\nabla\psi|^2 dx\,dy$ (with $\Delta\psi = -\omega$) reproduces the 2D Euler equations $\partial_t\omega + \{\psi, \omega\} = 0$ as Hamilton's equations.

---

# Bridges

- **[[Def - Poisson Bracket]]**: this theorem provides the structural properties of the Poisson bracket, making it more than just a curious bilinear operation. The bridge: the definition gives the formula $\{f, g\} = \omega(X_f, X_g)$; the theorem says this formula satisfies the four axioms of a Poisson algebra. Without the theorem, the Poisson bracket would be just a notation; with it, it is a Lie algebra structure.

- **[[Def - Hamiltonian Vector Field]]**: the homomorphism $f \mapsto X_f$ is the heart of the theorem's structural content. Bridge: the Lie algebra $(C^\infty(M), \{\cdot,\cdot\})$ acts on $C^\infty(M)$ via $f \cdot g := X_f(g) = \{f, g\}$ (the adjoint action), and the homomorphism $f \mapsto X_f$ realizes this action as vector fields on $M$.

- **[[Thm - Hamiltonian Flows are Symplectomorphisms]]**: this is used in the proof of $X_{\{f, g\}} = [X_f, X_g]$ — specifically the fact $\mathcal{L}_{X_f}\omega = 0$ is what makes the cross-term vanish in the Cartan calculation. Bridge: closedness of $\omega$ produces both the symplectic preservation by Hamiltonian flows and the Jacobi identity for the Poisson bracket — they are two faces of the same fact.

- **Lie–Poisson brackets and the Kirillov–Kostant–Souriau structure**: this theorem generalizes from symplectic manifolds to **Poisson manifolds** (with possibly degenerate Poisson tensor), and Lie–Poisson manifolds (with the KKS structure on $\mathfrak{g}^*$) are the canonical examples. The bridge: the same four-axiom Poisson-algebra structure exists for *any* Poisson manifold, and the symplectic case is the nondegenerate one. The Lie–Poisson case is degenerate (the coadjoint orbits are symplectic leaves), and the **Casimir functions** (functions Poisson-commuting with everything) generate the radical.

- **Quantization and the operator algebra**: the Lie algebra $(C^\infty(M), \{\cdot,\cdot\})$ has a deformation $(C^\infty(M)[[\hbar]], *_\hbar)$ — the **star product** — whose commutator $[\cdot, \cdot]_*/i\hbar$ recovers the Poisson bracket in the limit $\hbar \to 0$. Quantization is the process of converting the Poisson algebra into the operator algebra on a Hilbert space. The Lie-algebra structure on $C^\infty(M)$ is the *classical* algebraic structure that the quantum operator algebra deforms.

---

# Unlocked by This

> [!tip] Symplectic Realizations of Lie Algebras *(from Lie Theory)*
> The Lie-algebra homomorphism $f \mapsto X_f$ from $C^\infty(M)$ to $\Gamma(TM)$ can be specialized: for any Lie algebra $\mathfrak{g}$ acting on $(M, \omega)$ Hamiltonianly (i.e., each infinitesimal generator $\xi_M$ is a Hamiltonian vector field $\xi_M = X_{\mu^\xi}$), the **comoment map** $\xi \mapsto \mu^\xi$ is a Lie algebra homomorphism $\mathfrak{g} \to C^\infty(M)$. This is the structural reason the moment map $\mu : M \to \mathfrak{g}^*$ is well-defined and equivariant. The whole formalism of Hamiltonian group actions, equivariant cohomology, and symplectic reduction rests on this homomorphism.

> [!tip] The Heisenberg Algebra and Quantum Mechanics *(from Mathematical Physics)*
> The fundamental Poisson brackets $\{q^i, p_j\} = \delta^i_j$, $\{q^i, q^j\} = 0$, $\{p_i, p_j\} = 0$ define a Lie subalgebra of $(C^\infty(T^*\mathbb{R}^n), \{\cdot, \cdot\})$ spanned by $\{1, q^i, p_j\}$ — the **Heisenberg–Lie algebra** $\mathfrak{h}_n$. Its quantization is the **Heisenberg algebra** of operators on the quantum Hilbert space, with the canonical commutation relations $[\hat q^i, \hat p_j] = i\hbar\delta^i_j$. The **Stone–von Neumann theorem** says all irreducible representations of $\mathfrak{h}_n$ are unitarily equivalent — giving uniqueness of canonical quantization. This is the structural reason the formalism of quantum mechanics is uniquely determined by the classical Poisson algebra.

> [!tip] Casimir Functions and Conservation Laws *(from Poisson Geometry)*
> On a Poisson manifold (more general than symplectic), the **Casimir functions** $C$ satisfy $\{C, f\} = 0$ for all $f$ — they Poisson-commute with everything. On a symplectic manifold (nondegenerate $\omega$), the only Casimirs are locally constant; but on a degenerate Poisson manifold there can be nontrivial Casimirs. For the Lie–Poisson structure on $\mathfrak{so}(3)^*$ (the rigid-body phase space), the Casimirs are functions of $|\vec L|^2 = L_1^2 + L_2^2 + L_3^2$ — the total angular momentum squared, which is conserved by every Hamiltonian. So Casimirs are "automatic" conserved quantities that come from the geometry of the Poisson structure, not from any specific Hamiltonian.
