---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - Connection on a Vector Bundle"
  - "Def - Exterior Derivative on a Manifold"
tags: [geometry, gauge-theory, curvature, Bianchi]
---

# Notation

$E \to M$ is a smooth vector bundle with a connection $\nabla$, local connection 1-form $\omega$, and curvature 2-form $F = d\omega + \omega \wedge \omega$ (see [[Def - Connection on a Vector Bundle]] and [[Def - Curvature of a Vector-Bundle Connection]]). The **exterior covariant derivative** $d_\nabla : \Omega^k(M, \mathrm{End}(E)) \to \Omega^{k+1}(M, \mathrm{End}(E))$ acts on $\mathrm{End}(E)$-valued forms by $d_\nabla(\alpha) = d\alpha + [\omega, \alpha]$, where $[\omega, \alpha]$ is the graded commutator. For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Statement

> **Theorem (Second Bianchi Identity).** Let $\nabla$ be a connection on a smooth vector bundle $E \to M$ with curvature 2-form $F$. Then
> $$d_\nabla F = 0,$$
> equivalently, in a local frame, $dF + \omega \wedge F - F \wedge \omega = 0$. In components (acting on three vector fields $X, Y, Z \in \mathfrak{X}(M)$), the cyclic identity:
> $$\nabla_X F(Y, Z) + \nabla_Y F(Z, X) + \nabla_Z F(X, Y) = F([X, Y], Z) + F([Y, Z], X) + F([Z, X], Y).$$
> When $[X, Y] = [Y, Z] = [Z, X] = 0$ (e.g., for coordinate vector fields), the right side vanishes and the identity simplifies to:
> $$\nabla_X F(Y, Z) + \nabla_Y F(Z, X) + \nabla_Z F(X, Y) = 0.$$

---

# Motivation

The Bianchi identity is the universal differential identity satisfied by the curvature of *every* connection on *every* vector bundle — for any structure group, on any manifold, no matter how strange the bundle or connection. It is a *free* statement: it costs nothing, applies always, and constrains how the curvature can vary in spacetime.

The geometric meaning is that **the curvature is itself "closed" with respect to the connection's exterior covariant derivative**. The connection $\nabla$ extends from sections of $E$ to $E$-valued forms; on $\mathrm{End}(E)$-valued forms (like $F$), the natural derivative is $d_\nabla$. The Bianchi identity says $F$ is $d_\nabla$-closed.

The physical incarnation in electromagnetism is **the homogeneous Maxwell equations**: $dF = 0$ for the EM field strength $F = dA$. This includes:
- $\nabla \cdot B = 0$ (no magnetic monopoles in the absence of bundle non-triviality)
- $\nabla \times E + \partial_t B = 0$ (Faraday's law of induction)

These are not equations of motion — they hold *automatically* for any field of the form $F = dA$ (which is what the Bianchi identity says: $dF = ddA = 0$). The dynamical equations come from the *other* set, the source equations $\nabla \cdot E = \rho/\epsilon_0$ and $\nabla \times B - \partial_t E = J/\epsilon_0 c^2$, which are *not* automatic and require the action principle to derive.

In general relativity, the **contracted second Bianchi identity** $\nabla_\mu G^{\mu\nu} = 0$ for the Einstein tensor $G^{\mu\nu}$ is the consequence of the geometric Bianchi identity for the Riemann tensor. Through the Einstein field equations $G^{\mu\nu} = 8\pi T^{\mu\nu}$, this forces $\nabla_\mu T^{\mu\nu} = 0$ — *conservation of energy-momentum* is a *geometric identity*, not a separate assumption. This is one of the cleanest demonstrations of how geometry constrains physics: conservation laws follow from the Bianchi identity, automatically.

In Yang-Mills theory, the Bianchi identity $d_A F = 0$ is the homogeneous half of the Yang-Mills equations; the dynamical (Euler-Lagrange) half is $d_A \star F = 0$. Together they describe the dynamics of non-abelian gauge fields. The Bianchi identity is what makes the *instanton* count (a topological invariant of the connection on $\mathbb{R}^4$) finite and well-defined.

The "first" Bianchi identity (for the torsion of an arbitrary affine connection) is a separate but related statement; the second Bianchi is the one universally relevant to bundle curvature. The naming convention is historical and not particularly illuminating; the *second* Bianchi identity is what gauge theory uses.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: any connection on any vector bundle. The Bianchi identity holds in all settings.

**Whenever a curvature appears in physics.** The Bianchi identity is satisfied automatically. In electromagnetism, it gives the homogeneous Maxwell equations *for free*; you do not need to derive them from a Lagrangian. In general relativity, it gives $\nabla_\mu G^{\mu\nu} = 0$ automatically. In Yang-Mills, $d_A F = 0$. The recognition pattern: *whenever you write $F = d\omega + \omega \wedge \omega$ (or $R = d\Gamma + \Gamma \wedge \Gamma$), there is a free identity $d_\nabla F = 0$*.

**Whenever a closed form appears via a Stokes argument.** The Bianchi identity is what makes the curvature 2-form closed (in the abelian case, where $d_\nabla = d$ on the curvature). This is essential for: (a) integrating $F$ over closed surfaces to get topological invariants (first Chern numbers), (b) Stokes' theorem applications relating line integrals of $A$ to surface integrals of $F$ (Aharonov-Bohm).

**In dimensional reduction.** When working in $4 - k$ dimensions by integrating over $k$ dimensions, the Bianchi identity in higher dimensions descends to identities in lower dimensions — for instance, the Kaluza-Klein reduction of the higher-dimensional Bianchi gives multiple lower-dimensional identities.

**Targets (Output Amplification)**

The conclusion $d_\nabla F = 0$ combined with other ingredients:

**Combined with energy-momentum coupling:** $\nabla_\mu T^{\mu\nu} = 0$, conservation of energy-momentum. The contracted Bianchi $\nabla_\mu G^{\mu\nu} = 0$ in general relativity, via Einstein's equations $G = 8\pi T$, forces matter conservation. This is the *strongest* derivation of energy conservation in nature.

**Combined with the action principle:** the homogeneous half of any gauge-field equation of motion. The Yang-Mills action $\int\mathrm{tr}(F \wedge \star F)$ produces only the *inhomogeneous* equations $d_\nabla\star F = 0$; the homogeneous $d_\nabla F = 0$ is the Bianchi identity, automatic, and complements the equations of motion.

**Combined with closedness of $F$ in the abelian case:** integrals of $F$ over closed surfaces give topological invariants. The first Chern number $\frac{1}{2\pi i}\int_\Sigma F$ is a *closed-form integral* — well-defined because $F$ is closed; the value depends only on the homology class of $\Sigma$.

**Combined with Chern-Weil theory:** the Bianchi identity is essential to showing that characteristic class forms (Chern, Pontryagin, Euler) are *closed*, hence have well-defined cohomology classes. The general formula: $d(\mathrm{tr}\,F^k) = k\,\mathrm{tr}(d_\nabla F \wedge F^{k-1}) = 0$ uses Bianchi to make the curvature polynomial closed.

---

# Why Is It True

**One-line mechanism summary:** **The identity $d^2 = 0$ for the exterior derivative, combined with the structure equation $F = d\omega + \omega \wedge \omega$, gives $d_\nabla F = 0$ — Bianchi is just $d^2 = 0$ in disguise.**

The clean way to see this: in a local frame, compute $dF$ directly. $dF = d(d\omega + \omega \wedge \omega) = d^2\omega + d(\omega \wedge \omega)$. The first term is zero ($d^2 = 0$). The second: $d(\omega \wedge \omega) = d\omega \wedge \omega - \omega \wedge d\omega$ (Leibniz on 1-forms, with sign for crossing $\omega$). Compute the bracket: $[\omega, F] = [\omega, d\omega + \omega \wedge \omega] = \omega \wedge d\omega - d\omega \wedge \omega + \omega \wedge \omega \wedge \omega - \omega \wedge \omega \wedge \omega = \omega \wedge d\omega - d\omega \wedge \omega$. So $dF = -[\omega, d\omega] = -[\omega, F]$ (using the cancellation of cubic terms in $\omega$), i.e., $dF + [\omega, F] = 0$, which is $d_\nabla F = 0$.

In the more abstract presentation using $d_\nabla^2 = F \wedge \cdot$: the squared exterior covariant derivative $d_\nabla^2$ acting on any $E$-valued form is multiplication by $F$. So $d_\nabla(d_\nabla\alpha) = F \wedge \alpha$. Applied to $\alpha = 1$ (a constant section), we get $d_\nabla^2(1) = F$. Applying $d_\nabla$ to both sides: $d_\nabla^3(1) = d_\nabla F$. But $d_\nabla^3 = d_\nabla(d_\nabla \cdot d_\nabla) = (d_\nabla^2)d_\nabla = F \cdot d_\nabla$, and acting on $1$: $d_\nabla^3(1) = F \wedge d_\nabla(1) = F \wedge 0 = 0$ (since $d_\nabla 1 = 0$). Hence $d_\nabla F = 0$.

In yet another formulation: $d^2 = 0$ at the level of exterior algebra, and the Bianchi is just $d^2$ for the connection's exterior algebra. This makes the result *structurally automatic*: any $d$-like operator (one satisfying $d^2 = 0$) gives such an identity for the "second derivative".

The bigger picture: the Bianchi identity reflects that the *space of connections* fits into a *chain complex* — connections (degree 0), curvatures (degree 1), and Bianchi (the statement that $d_\nabla$ takes the curvature to zero, hence the curvature is a *cycle* in the relevant complex). This is the framework in which curvature is understood as a cohomology class, with characteristic classes being its various polynomial functionals.

---

# What Makes This Hard

The Bianchi identity itself is short to state and short to prove. The conceptual hurdle is *understanding* why it is "free" — why every curvature satisfies this differential identity without any input from physics or specific bundle structure. The answer is just $d^2 = 0$ at the right level of generality.

Common errors: (i) Forgetting the sign in the bracket $[\omega, F]$ — Bianchi involves a *commutator*, and signs matter for non-abelian connections. (ii) Confusing the Bianchi identity (a *differential identity*) with the equations of motion (a *dynamical constraint*). (iii) Writing it as $dF = 0$ in non-abelian settings — this is only the abelian special case; in general $d_\nabla F = 0 \ne dF$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use the structure equation $F = d\omega + \omega \wedge \omega$ and the fact $d^2 = 0$. Compute $dF$ directly; the result equals $-[\omega, F]$, hence $dF + [\omega, F] = d_\nabla F = 0$.

**Subgoal decomposition:**

1. **Apply $d$ to the structure equation.** $dF = d(d\omega + \omega \wedge \omega) = d^2\omega + d(\omega \wedge \omega)$.
   - *Hint:* $d^2 = 0$ kills the first term.
   - *Why needed:* Reduces the computation to $d(\omega \wedge \omega)$.

2. **Compute $d(\omega \wedge \omega)$.** Using Leibniz for matrix-valued 1-forms with sign convention: $d(\omega \wedge \omega) = d\omega \wedge \omega - \omega \wedge d\omega$.
   - *Hint:* The sign comes from crossing $\omega$ over $\omega$ (sign $(-1)^{\deg\omega} = -1$).
   - *Why needed:* Gives the explicit form of $dF$.

3. **Compute the bracket $[\omega, F]$.** Expanding: $[\omega, F] = \omega \wedge F - F \wedge \omega = \omega \wedge (d\omega + \omega \wedge \omega) - (d\omega + \omega \wedge \omega) \wedge \omega = \omega \wedge d\omega - d\omega \wedge \omega + 0$ (the cubic $\omega \wedge \omega \wedge \omega$ terms cancel by associativity).
   - *Hint:* The cubic terms cancel because $\omega \wedge (\omega \wedge \omega) = (\omega \wedge \omega) \wedge \omega$ by associativity of wedge product.
   - *Why needed:* Allows the comparison with $dF$.

4. **Combine.** $dF + [\omega, F] = (d\omega \wedge \omega - \omega \wedge d\omega) + (\omega \wedge d\omega - d\omega \wedge \omega) = 0$.
   - *Hint:* Direct cancellation.
   - *Why needed:* This is the local-frame form of $d_\nabla F = 0$.

5. **Recognize this as $d_\nabla F = 0$.** The exterior covariant derivative on $\mathrm{End}(E)$-valued forms is $d_\nabla\alpha = d\alpha + [\omega, \alpha]$ (for the graded commutator). Hence $d_\nabla F = dF + [\omega, F] = 0$.
   - *Hint:* Definition of $d_\nabla$ on $\mathrm{End}(E)$-valued forms.
   - *Why needed:* Translates the local computation into the coordinate-invariant statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: Leibniz rule for matrix-valued forms
> **Statement:** For matrix-valued forms $\alpha$ of degree $p$ and $\beta$ of degree $q$, $d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^p \alpha \wedge d\beta$.
>
> **Hint:** This is the standard Leibniz rule for the exterior derivative, extended to matrix-valued forms entry by entry (with matrix product instead of scalar product).
>
> **Why needed:** Computing $d(\omega \wedge \omega)$ requires this Leibniz rule with the sign convention.
>
> > [!note]- Full proof
> > For scalar forms this is the standard Leibniz rule. For matrix-valued forms $\alpha = (\alpha^i{}_j)$, $\beta = (\beta^j{}_k)$, the wedge is $(\alpha \wedge \beta)^i{}_k = \alpha^i{}_j \wedge \beta^j{}_k$ (Einstein summation). Each entry is a sum of scalar wedge products, to which the scalar Leibniz rule applies:
> > $$d(\alpha^i{}_j \wedge \beta^j{}_k) = d\alpha^i{}_j \wedge \beta^j{}_k + (-1)^p\alpha^i{}_j \wedge d\beta^j{}_k = (d\alpha \wedge \beta)^i{}_k + (-1)^p(\alpha \wedge d\beta)^i{}_k.$$
> > For our case $p = 1$, so $d(\omega \wedge \omega) = d\omega \wedge \omega - \omega \wedge d\omega$.

> [!note]- Lemma 2: Cubic terms in $[\omega, F]$ cancel
> **Statement:** $\omega \wedge \omega \wedge \omega - \omega \wedge \omega \wedge \omega = 0$ — the obvious cancellation by associativity.
>
> **Hint:** Wedge product is associative: $\omega \wedge (\omega \wedge \omega) = (\omega \wedge \omega) \wedge \omega$.
>
> **Why needed:** Shows that $[\omega, F]$ involves only the $d\omega$ parts, not the cubic $\omega^3$ parts.
>
> > [!note]- Full proof
> > $\omega \wedge \omega \wedge \omega = \omega \wedge (\omega \wedge \omega) = (\omega \wedge \omega) \wedge \omega$ by associativity. Hence $\omega \wedge (\omega \wedge \omega) - (\omega \wedge \omega) \wedge \omega = 0$. Note: even for non-commutative matrices, the wedge product of matrix-valued forms is associative — only the *commutator* fails to vanish for non-abelian structures.

---

# Formal Proof

> [!note]- Complete formal proof
> **Setup.** Let $\nabla$ be a connection on a vector bundle $E \to M$ with local connection 1-form $\omega$ and curvature 2-form $F = d\omega + \omega \wedge \omega$.
>
> **Compute $dF$.**
> $$dF = d(d\omega + \omega \wedge \omega) = d(d\omega) + d(\omega \wedge \omega) = 0 + (d\omega \wedge \omega - \omega \wedge d\omega) = d\omega \wedge \omega - \omega \wedge d\omega,$$
> using $d^2 = 0$ for the first term and Lemma 1 (Leibniz) for the second.
>
> **Compute $[\omega, F]$.**
> $$[\omega, F] = \omega \wedge F - F \wedge \omega = \omega \wedge (d\omega + \omega \wedge \omega) - (d\omega + \omega \wedge \omega) \wedge \omega$$
> $$= \omega \wedge d\omega + \omega \wedge \omega \wedge \omega - d\omega \wedge \omega - \omega \wedge \omega \wedge \omega = \omega \wedge d\omega - d\omega \wedge \omega,$$
> where the cubic $\omega \wedge \omega \wedge \omega$ terms cancel by Lemma 2.
>
> **Combine.**
> $$dF + [\omega, F] = (d\omega \wedge \omega - \omega \wedge d\omega) + (\omega \wedge d\omega - d\omega \wedge \omega) = 0.$$
>
> **Recognize as $d_\nabla F$.** The exterior covariant derivative on $\mathrm{End}(E)$-valued forms is defined by $d_\nabla\alpha = d\alpha + [\omega, \alpha]$ for the graded commutator $[\omega, \alpha] = \omega \wedge \alpha - (-1)^{\deg\alpha}\alpha \wedge \omega$. Applied to $F$ (degree 2): $d_\nabla F = dF + \omega \wedge F - F \wedge \omega = dF + [\omega, F] = 0$.
>
> **Frame-independence.** The local-frame computation gives $d_\nabla F = 0$ in any frame; tensoriality of $F$ (from [[Thm - Curvature is C-Infinity Linear in Sections]]) and the well-definedness of $d_\nabla$ on $\mathrm{End}(E)$-valued forms ensure this is a globally defined, coordinate-invariant statement.
>
> ▪
>
> **Component form.** Applied to three vector fields $X, Y, Z$:
> $$\sum_{\mathrm{cyc}} \nabla_X F(Y, Z) - \sum_{\mathrm{cyc}} F([X, Y], Z) = 0,$$
> where the sums are cyclic over $(X, Y, Z)$. When the brackets vanish (coordinate fields), this reduces to the cyclic sum $\sum_{\mathrm{cyc}}\nabla_X F(Y, Z) = 0$.

---

# Cross-Field Exercise Suggestions

**General relativity: contracted Bianchi.** Apply the second Bianchi identity to the Riemann tensor: $\nabla_{[\lambda}R^\mu{}_{|\nu|\rho\sigma]} = 0$. Contracting twice gives $\nabla_\mu G^{\mu\nu} = 0$ for the Einstein tensor $G^{\mu\nu} = R^{\mu\nu} - \frac{1}{2}Rg^{\mu\nu}$. Through Einstein's equations, this forces $\nabla_\mu T^{\mu\nu} = 0$ — conservation of stress-energy. *No separate axiom needed; conservation follows from the Bianchi identity.*

**Electromagnetism: homogeneous Maxwell equations.** $dF = 0$ for the EM field strength $F = dA$ is the abelian Bianchi identity. Component form: $\partial_{[\lambda}F_{\mu\nu]} = 0$, equivalently $\nabla \cdot B = 0$ and $\nabla \times E + \partial_t B = 0$. These are *automatic* for any $F$ derived from a potential.

**Yang-Mills: instanton charge quantization.** The second Chern number $c_2 = \frac{1}{8\pi^2}\int_M\mathrm{tr}(F \wedge F)$ for a connection on a principal $G$-bundle is integer-valued (when $G$ is compact). The Bianchi identity ensures $\mathrm{tr}(F \wedge F)$ is closed: $d\mathrm{tr}(F \wedge F) = 2\mathrm{tr}(d_\nabla F \wedge F) = 0$ by Bianchi. This is the basis of instanton number quantization in Yang-Mills theory.

**Cohomology of fibre bundles.** The Bianchi identity makes Chern classes well-defined as elements of de Rham cohomology, independent of the choice of connection. The general Chern-Weil construction takes a polynomial $P$ in the curvature, applies Bianchi to show $dP(F) = 0$, and verifies that the cohomology class $[P(F)]$ is independent of $\nabla$.

---

# Bridges

- **[[Def - Curvature of a Vector-Bundle Connection|Curvature]]** — The Bianchi identity is the natural *next* statement after defining curvature: once you have $F = d\omega + \omega \wedge \omega$, the identity $d_\nabla F = 0$ follows. It is the differential structure of the curvature.

- **$d^2 = 0$ on differential forms** *(from [[Differential Geometry VIII — Differential Forms]])* — The Bianchi identity is essentially $d^2 = 0$ applied to the connection 1-form (after accounting for the non-linear structure equation). The same algebraic fact powers many theorems: existence of de Rham cohomology (kernels modulo images for a chain complex), Poincaré lemma (locally closed = locally exact), Stokes' theorem (the boundary operator squared is zero).

- **Conservation of energy-momentum in general relativity** *(from [[General Relativity I — Einstein's Equations and Schwarzschild]])* — The contracted second Bianchi identity in GR gives $\nabla_\mu G^{\mu\nu} = 0$, which through Einstein's equations $G^{\mu\nu} = 8\pi T^{\mu\nu}$ forces $\nabla_\mu T^{\mu\nu} = 0$. *Conservation of stress-energy is a geometric identity in GR*, not an independent axiom — a profound structural feature of the theory.

- **Chern-Weil theory** *(from [[Algebraic Topology III — Higher Homotopy and Chern Forms]])* — Polynomial expressions in the curvature, like $\mathrm{tr}(F^k)$ and $\det(I + F)$, are closed differential forms *because* of the Bianchi identity. Their de Rham cohomology classes are the **characteristic classes** of the bundle — Chern, Pontryagin, Euler — and they are independent of the connection. The Bianchi identity is the foundational fact that makes Chern-Weil theory work.

- **Homogeneous Maxwell equations** — The classical equations $\nabla \cdot B = 0$, $\nabla \times E + \partial_t B = 0$ are equivalent to $dF = 0$ for the EM field-strength 2-form. They are *not* dynamical equations (those come from $d\star F = J$); they are *kinematical identities* implied by the existence of a potential $A$ with $F = dA$. The Bianchi identity is the modern, coordinate-free statement of this fact.

---

# Unlocked by This

> [!tip] Chern Classes and Characteristic Classes *(from Algebraic Topology)*
> The polynomial $\mathrm{tr}(F^k)$ in the curvature is a closed $2k$-form on $M$ — the closedness follows from the Bianchi identity via $d\,\mathrm{tr}(F^k) = k\,\mathrm{tr}(d_\nabla F \wedge F^{k-1}) = 0$. Its de Rham cohomology class $[\mathrm{tr}(F^k)/(2\pi i)^k]$ is independent of the connection $\nabla$ — this is **Chern-Weil's theorem**. The resulting classes are the **Chern classes** of $E$. The whole theory of characteristic classes — Chern, Pontryagin, Euler — is built on this construction, with the Bianchi identity as the unifying algebraic fact.

> [!tip] Chern-Simons Theory in 3 Dimensions *(from Mathematical Physics)*
> The **Chern-Simons action** for a connection on a principal $G$-bundle over a 3-manifold $M$ is $S_{\mathrm{CS}}[A] = \frac{k}{4\pi}\int_M\mathrm{tr}(A \wedge dA + \frac{2}{3}A \wedge A \wedge A)$ for integer $k$ (the *level*). Its variation produces $d_A F = 0$, i.e., *exactly* the Bianchi identity — making every connection a critical point of the Chern-Simons functional. Hence Chern-Simons is a **topological field theory** (no kinetic term, no dynamics beyond Bianchi). Its quantization gives the **Witten-Reshetikhin-Turaev invariants** of 3-manifolds and the **Jones polynomial** of links — a deep connection between gauge theory and knot theory.
