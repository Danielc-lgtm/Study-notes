---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Connection 1-Forms (Cartan)"
  - "Def - Curvature 2-Forms (Cartan)"
  - "Def - Affine Connection on a Vector Bundle"
tags: [geometry, riemannian-geometry, connections, cartan-formalism, curvature]
---

# Notation

$(M, \nabla)$ — smooth manifold with affine connection on a vector bundle $E \to M$ (typically $E = TM$). $e = (e_a)$ — local frame; $\omega^a{}_b$ — [[Def - Connection 1-Forms (Cartan)|connection 1-forms]]; $\omega$ — connection matrix. $\Omega^a{}_b$ — [[Def - Curvature 2-Forms (Cartan)|curvature 2-forms]]; $\Omega$ — curvature matrix. $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ — the Riemann curvature tensor. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Statement

> **Theorem (Cartan's Second Structural Equation).** Let $E \to M$ be a smooth vector bundle with connection $\nabla$, and let $e = (e_a)$ be a local frame with connection 1-forms $\omega^a{}_b$. Then the curvature 2-forms of $\nabla$ in the frame $e$ satisfy
> $$
> \Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b,
> $$
> equivalently in matrix form $\Omega = d\omega + \omega \wedge \omega$.
>
> The components of the curvature tensor are recovered via $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\,\sigma^c \wedge \sigma^d$, where $R(e_c, e_d)e_b = R^a{}_{bcd}\,e_a$ in the dual coframe $\sigma^a$ to $e$.

---

# Motivation

Cartan's second structural equation is the **defining formula for the curvature 2-forms** in terms of the connection 1-forms. It is the operational tool for computing the Riemann curvature tensor of any concrete metric: once the connection 1-forms are known (typically from Cartan's first structural equation [[Thm - Cartan's First Structural Equation]] in an orthonormal frame), the curvature 2-forms are computed by a single application of this equation, and the Riemann tensor components are read off.

The motivation is twofold. First, the equation provides the most **efficient practical algorithm** for computing the Riemann tensor of a concrete Riemannian or Lorentzian metric — dramatically faster than the coordinate formula $R^l{}_{ijk} = \partial_i\Gamma^l_{jk} - \partial_j\Gamma^l_{ik} + \Gamma^l_{im}\Gamma^m_{jk} - \Gamma^l_{jm}\Gamma^m_{ik}$, which requires computing Christoffel symbols in coordinates first and then taking many derivatives. The Cartan method skips the Christoffel-in-coordinates step entirely.

Second, the equation has a clean **geometric content**: it expresses the second covariant derivative $\nabla\nabla$ acting on the frame: $\nabla\nabla e_b = e_a \otimes \Omega^a{}_b$. The right-hand side $d\omega + \omega \wedge \omega$ has two pieces: the **$d\omega$ term** is the "abelian curvature" — the part of the curvature that arises even when the connection 1-forms commute (the only piece for a $U(1)$ gauge theory like electromagnetism), and the **$\omega \wedge \omega$ term** is the "non-abelian self-interaction" — the part that arises from the non-commutativity of $\omega$ (the only piece for the Maurer-Cartan equation on a Lie [[Def - Group|group]]). For Riemannian geometry both are present whenever the manifold is curved.

The equation generalises to *any* vector bundle with connection; it does *not* require the bundle to be the tangent bundle (unlike Cartan's first structural equation, which uses the soldering form / coframe specific to $TM$). This is why **Yang-Mills theory** in physics uses the same formula $F = dA + A \wedge A$ for the field strength of any gauge group — it is the second structural equation of the corresponding principal-bundle connection.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: any connection on any vector bundle.* The second structural equation always holds — it is a structural identity, not a conditional theorem. The bridge: whenever you have a connection and a frame, the equation $\Omega = d\omega + \omega \wedge \omega$ gives the curvature.

*Source 2: an orthonormal frame with connection 1-forms computed from Cartan's first equation.* This is the standard setup for computing curvature of a Riemannian metric. Combined with the antisymmetry $\omega^a{}_b + \omega^b{}_a = 0$ (metric-compatibility in orthonormal frame), the structure of the calculation often involves only a few nonzero terms.

*Source 3: a principal-bundle connection on a $G$-bundle.* For a connection on a principal bundle, the same equation gives the curvature 2-form as a $\mathfrak{g}$-valued 2-form. This is the **Yang-Mills field strength** $F = dA + A \wedge A$ in gauge theory: for $G = U(1)$ (electromagnetism), $A \wedge A = 0$ and $F = dA$; for non-abelian $G$, both terms are present.

**Targets (Output Amplification)**

*Target combination 1: Second structural equation + algebraic identity $d^2 = 0$ ⟹ Second Bianchi identity.* Take the exterior derivative of $\Omega = d\omega + \omega \wedge \omega$: $d\Omega = d(d\omega) + d(\omega \wedge \omega) = 0 + d\omega \wedge \omega - \omega \wedge d\omega = (\Omega - \omega \wedge \omega) \wedge \omega - \omega \wedge (\Omega - \omega \wedge \omega) = \Omega \wedge \omega - \omega \wedge \Omega$. So $d\Omega + \omega \wedge \Omega - \Omega \wedge \omega = 0$ — the **second Bianchi identity** in differential-form language. The component version is $\nabla_e R_{abcd} + \nabla_c R_{abde} + \nabla_d R_{abec} = 0$.

*Target combination 2: Second structural equation + sharp/musical isomorphism ⟹ sectional curvature.* In an orthonormal frame for a Riemannian manifold, the curvature 2-forms $\Omega^a{}_b$ encode the Riemann tensor via $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\sigma^c \wedge \sigma^d$. The **sectional curvature** in the 2-plane spanned by orthonormal $(e_c, e_d)$ is then $K(e_c \wedge e_d) = R_{cdcd} = g(R(e_c, e_d)e_d, e_c)$, which is read off the matrix coefficients of $\Omega^c{}_d$ in the natural basis. This is the operational tool used to compute sectional curvature in concrete examples.

*Target combination 3: Second structural equation + Chern-Weil theory ⟹ characteristic classes.* For any connection on a complex vector bundle, the curvature 2-form $\Omega$ (an $\mathrm{End}(E)$-valued 2-form) has invariant polynomials — trace, determinant, Pfaffian — that produce closed differential forms whose cohomology classes are **independent of the connection** and are topological invariants of $E$ (Chern classes, Pontryagin classes, Euler class). The integrals over closed manifolds give integer-valued **Chern numbers**. The Gauss-Bonnet theorem $\int_M K\,dA = 2\pi\chi(M)$ for surfaces is the simplest Chern-Weil identity, expressing the Euler characteristic as the trace of the curvature 2-form.

---

# Why Is It True

**Mechanism summary:** **the second structural equation is $\nabla\nabla e_b = e_a \otimes \Omega^a{}_b$ rewritten in the form-language: the matrix $\omega$ acts on the frame by $\nabla e = e\omega$; applying $\nabla$ again gives $\nabla\nabla e = e\omega^2 + e\,d\omega = e(d\omega + \omega \wedge \omega) = e\Omega$. The "extra" $\omega \wedge \omega$ term arises because the second $\nabla$ acts on both $e$ and $\omega$, picking up an additional $\omega$ from the action on $e$.**

The intuition. The first covariant derivative of the frame is $\nabla e = e \omega$, the matrix equation expressing the connection. To compute the second covariant derivative, apply $\nabla$ again: $\nabla(e \omega) = (\nabla e)\omega + e\,d\omega$ (Leibniz for $\nabla$, with $d\omega$ being the exterior derivative on the 1-form). The first term is $(e\omega)\omega = e(\omega \wedge \omega)$, where the wedge product reflects the fact that $\omega$ is a 1-form-valued matrix and the second wedge is the matrix product of $\omega$ with itself in the 1-form sense. The second term is $e \cdot d\omega$. Summing: $\nabla\nabla e = e(d\omega + \omega \wedge \omega) = e \Omega$. This is the structural equation. The remarkable feature: the result is *algebraic* in the section (no derivatives of $v$ appear when we apply $\nabla\nabla$ to a general $v$), which is what makes the curvature a *tensor*.

A different mnemonic: in matrix form $\Omega = d\omega + \omega \wedge \omega$, the wedge product is matrix-valued — $\omega \wedge \omega$ means the matrix whose $(a, b)$ entry is $\omega^a{}_c \wedge \omega^c{}_b$ (summed over $c$). This is *not* zero in general for matrix-valued 1-forms, even though $\alpha \wedge \alpha = 0$ for scalar 1-forms — the non-commutativity of matrix multiplication is what makes it nonzero. This is the source of the non-abelian self-interaction in Yang-Mills theory.

---

# What Makes This Hard

The conceptual difficulty is **the interaction between the wedge product and the matrix product**. For matrix-valued 1-forms $\omega = (\omega^a{}_b)$, the product $\omega \wedge \omega$ does *not* mean the scalar wedge product of $\omega$ with itself (which would be zero) — it means the matrix product where the entries are wedged: $(\omega \wedge \omega)^a{}_b = \omega^a{}_c \wedge \omega^c{}_b$ (summed over $c$). This is generally nonzero because $\omega^a{}_c \wedge \omega^c{}_b \neq -\omega^c{}_b \wedge \omega^a{}_c$ (the matrix indices break the antisymmetry). Students often confuse the two products and incorrectly conclude $\omega \wedge \omega = 0$, leading to wrong curvature formulas.

The mechanical hard part is **the calculation showing $\nabla\nabla v = e\Omega v$ is algebraic in $v$**. The intermediate step $\nabla(e(dv + \omega v)) = e[(\omega \wedge dv) + d(dv) + d(\omega)v - \omega \wedge dv + (\omega \wedge \omega)v] = e[d\omega + \omega \wedge \omega]v$ shows the $dv$ pieces cancel, leaving only an algebraic action on $v$ — this is non-trivial because *a priori* the second covariant derivative might depend on first derivatives of $v$. The cancellation $d(dv) = 0$ (Poincaré lemma) plus the Leibniz interaction is what makes curvature tensorial.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute $\nabla\nabla v$ for a generic section $v$ using the formula $\nabla v = e(dv + \omega v)$. Apply $\nabla$ again, using Leibniz to expand. The $dv$ terms cancel, leaving $\nabla\nabla v = e(d\omega + \omega \wedge \omega)v$. Read off $\Omega = d\omega + \omega \wedge \omega$.

**Subgoal decomposition:**

1. **Write the covariant differential of a section in matrix-column form.** For $v = v^a e_a$, $\nabla v = e(dv + \omega v)$ where $v$ is the column $(v^a)$ and $\omega = (\omega^a{}_b)$ is the connection matrix.
   - *Hint:* This is just the formula $\nabla_X v = (X(v^a) + \omega^a{}_b(X)v^b)e_a$ written with form-valued matrix-column notation.
   - *Why needed:* Sets up the second application of $\nabla$.

2. **Apply $\nabla$ to $\nabla v$.** Use the Leibniz rule for $\nabla$ acting on the product $e \cdot (dv + \omega v)$, treating $e$ as a vector-valued row and $(dv + \omega v)$ as a column-valued 1-form.
   - *Hint:* $\nabla(e \cdot Q) = (\nabla e)Q + e\,dQ$ where $Q$ is a column of 1-forms.
   - *Why needed:* Sets up the cancellation.

3. **Expand and cancel $dv$ terms.** $\nabla\nabla v = (e\omega)(dv + \omega v) + e\,d(dv + \omega v) = e[\omega \wedge (dv + \omega v)] + e[d^2v + d\omega \cdot v - \omega \wedge dv]$. The $\omega \wedge dv$ and $-\omega \wedge dv$ cancel. $d^2v = 0$ by Poincaré.
   - *Hint:* Track the signs carefully using the form-valued matrix-column conventions.
   - *Why needed:* Shows the algebraic result.

4. **Identify the curvature matrix.** What remains is $\nabla\nabla v = e[d\omega + \omega \wedge \omega]v = e\Omega v$ where $\Omega = d\omega + \omega \wedge \omega$ is the curvature matrix.
   - *Hint:* The dependence on $v$ is purely algebraic — no derivatives of $v$.
   - *Why needed:* This is the equation.

5. **Verify the component formula $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\sigma^c \wedge \sigma^d$.** Apply $\nabla\nabla v$ on a pair of vector fields $(X, Y)$ to get $\nabla\nabla v(X, Y) = R(X, Y)v$ (the Riemann tensor); compare with $e\Omega(X, Y)v$ and read off the components.
   - *Hint:* The Riemann tensor on basis vectors is $R(e_c, e_d)e_b = R^a{}_{bcd}e_a$, with the index ordering matching the 2-form expansion.
   - *Why needed:* Connects the structural equation to the standard Riemann tensor.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\nabla\nabla v$ depends algebraically on $v$ (not on $dv$)
> **Statement:** For any section $v$, the second covariant derivative $\nabla\nabla v = e\Omega v$ where $\Omega = d\omega + \omega \wedge \omega$, depending only on $v$ algebraically (no derivatives of $v$ on the right side).
>
> **Hint:** Apply $\nabla$ to $\nabla v = e(dv + \omega v)$ and check that the $dv$ pieces cancel via $d^2 v = 0$ and the Leibniz interaction.
>
> **Why needed:** This is the key structural fact that makes the curvature a *tensor*. Without the cancellation, $\nabla\nabla$ would depend on $dv$ and would not give a tensor.
>
> > [!note]- Full proof
> > Write $\nabla v = e(dv + \omega v)$. Apply $\nabla$ to this, using Leibniz: $\nabla(\nabla v) = \nabla(e)\,(dv + \omega v) + e \cdot d(dv + \omega v)$. The first term: $\nabla e = e \omega$, so $\nabla e \cdot (dv + \omega v) = e\omega \cdot (dv + \omega v) = e[\omega \wedge dv + \omega \wedge \omega v]$ where the wedge handles the form-valued nature. The second term: $d(dv + \omega v) = d^2 v + d\omega \cdot v - \omega \wedge dv = 0 + d\omega \cdot v - \omega \wedge dv$ (using $d^2 = 0$ and the Leibniz rule $d(\omega v) = d\omega \cdot v - \omega \wedge dv$ — the sign coming from the form degree of $\omega$). Summing: $\nabla\nabla v = e[\omega \wedge dv + \omega \wedge \omega v + d\omega \cdot v - \omega \wedge dv] = e[\omega \wedge \omega + d\omega]v = e\Omega v$ where $\Omega = d\omega + \omega \wedge \omega$. The $\omega \wedge dv$ terms cancelled. $\blacksquare$

> [!note]- Lemma 2: The curvature 2-form matches the Riemann tensor in components
> **Statement:** Evaluating $\nabla\nabla v$ on a pair of vector fields $(X, Y)$ gives $\nabla\nabla v(X, Y) = R(X, Y) v$ where $R$ is the Riemann curvature tensor.
>
> **Hint:** Use the antisymmetrisation in $(X, Y)$ inherent in the 2-form structure, and compare with the definition of $R$.
>
> **Why needed:** This shows the curvature 2-form matrix $\Omega$ is the same object as the Riemann tensor.
>
> > [!note]- Full proof (sketch)
> > $\nabla\nabla v$ is a 2-form-valued section, so evaluating on $(X, Y)$ gives $(\nabla\nabla v)(X, Y) = (\nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X, Y]})v = R(X, Y)v$ — exactly the definition of the Riemann tensor. So $\Omega^a{}_b(X, Y) \cdot e_a = R(X, Y)e_b$, i.e., $\Omega^a{}_b(X, Y) = $ $a$-th component of $R(X, Y)e_b$ in the frame $e$. Expanding $R(X, Y)e_b = R^a{}_{bcd}X^c Y^d e_a$ (definition), $\Omega^a{}_b(X, Y) = R^a{}_{bcd}X^c Y^d$. Comparing with $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\sigma^c \wedge \sigma^d$ evaluated on $(X, Y)$: $\tfrac{1}{2}R^a{}_{bcd}(X^c Y^d - Y^c X^d) = R^a{}_{b[cd]}X^c Y^d$. So the components of $\Omega$ encode the antisymmetric part of $R$ in $(c, d)$, which is the full $R$ since $R$ is antisymmetric in $(c, d)$ to begin with. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\nabla$ be a connection on a vector bundle $E$ with local frame $e = (e_a)$, dual coframe $\sigma^a$, and connection 1-forms $\omega^a{}_b$ defined by $\nabla e_b = e_a \otimes \omega^a{}_b$.
>
> **Step 1 — $\nabla v$ in matrix-column form.** For a section $v = v^a e_a$, $\nabla v = \nabla(v^a e_a) = dv^a \otimes e_a + v^a \nabla e_a = dv^a \otimes e_a + v^a\,\omega^b{}_a \otimes e_b$. Relabel and collect: $\nabla v = e_a \otimes (dv^a + \omega^a{}_b v^b)$. In matrix-column notation with $v$ as column $(v^a)$ and $\omega$ as the matrix $(\omega^a{}_b)$: $\nabla v = e(dv + \omega v)$.
>
> **Step 2 — Apply $\nabla$ again.** $\nabla\nabla v = \nabla(e(dv + \omega v))$. By Leibniz: $= (\nabla e)(dv + \omega v) + e \cdot d(dv + \omega v)$.
>
> *First term.* $\nabla e = e \omega$ (matrix-equation). So $(\nabla e)(dv + \omega v) = e\omega(dv + \omega v) = e[\omega \wedge dv + (\omega \wedge \omega)v]$, with the wedges acting in the form-valued matrix-column product (the matrix product of $\omega$ with $dv$ is $\omega \wedge dv$ as a column of 2-forms, and similarly for $\omega \wedge \omega$).
>
> *Second term.* $d(dv + \omega v) = d(dv) + d(\omega v) = 0 + d\omega \cdot v - \omega \wedge dv$, using $d^2 = 0$ and the graded Leibniz $d(\alpha \cdot v) = d\alpha \cdot v + (-1)^{|\alpha|}\alpha \wedge dv = d\alpha \cdot v - \alpha \wedge dv$ (for $\alpha$ a 1-form, sign is $-1$).
>
> So $\nabla\nabla v = e[\omega \wedge dv + (\omega \wedge \omega)v + d\omega \cdot v - \omega \wedge dv] = e[(d\omega + \omega \wedge \omega)v] = e \cdot \Omega \cdot v$ where $\Omega := d\omega + \omega \wedge \omega$.
>
> **Step 3 — Identify $\Omega$ with the Riemann tensor.** By the definition of the second covariant derivative as a 2-form, $\nabla\nabla v$ evaluated on $(X, Y)$ gives $(\nabla\nabla v)(X, Y) = (\nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X, Y]})v = R(X, Y)v$. On the other hand, $(\nabla\nabla v)(X, Y) = e\,\Omega(X, Y)\,v$. So $\Omega(X, Y)v = R(X, Y)v$ as vectors; in components, $\Omega^a{}_b(X, Y) v^b = R^a{}_{bcd}X^c Y^d v^b$, hence $\Omega^a{}_b(X, Y) = R^a{}_{bcd}X^c Y^d = \tfrac{1}{2}R^a{}_{bcd}(X^c Y^d - X^d Y^c)$ (using antisymmetry of $R$ in $(c, d)$), so $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\sigma^c \wedge \sigma^d$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**1. Curvature of the round 2-sphere via Cartan's second equation.** Given the connection 1-form $\omega^1{}_2 = -\cos\theta\,d\varphi$ on $S^2$ (computed from Cartan's first equation), apply the second structural equation: $\Omega^1{}_2 = d\omega^1{}_2 + \omega^1{}_c \wedge \omega^c{}_2 = d(-\cos\theta\,d\varphi) + 0 = \sin\theta\,d\theta \wedge d\varphi = \sigma^1 \wedge \sigma^2$, where $\sigma^1 = d\theta, \sigma^2 = \sin\theta\,d\varphi$. The Gaussian curvature is $K = 1$. See [[Ex - Cartan Structural Equations on S^2]].

**2. Curvature 2-forms of the Schwarzschild metric.** Using the orthonormal coframe and connection 1-forms of the Schwarzschild geometry, apply Cartan's second structural equation to compute the curvature 2-forms. Read off the Riemann tensor components and compute the sectional curvatures (which give the well-known $\pm M/r^3$ tidal forces). See [[Ex - Computing Curvature 2-Forms in an Orthonormal Frame]].

**3. Yang-Mills field strength $F = dA + A \wedge A$.** Verify that the same structural equation, applied to a $\mathfrak{g}$-valued connection 1-form $A$ on a principal $G$-bundle, gives the Yang-Mills field strength. For $G = U(1)$ (electromagnetism), $A \wedge A = 0$ and $F = dA$ is just the electromagnetic field tensor. For $G = SU(2)$ (weak interactions) or $G = SU(3)$ (strong), the $A \wedge A$ term gives the non-abelian self-interaction characteristic of those theories. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

**4. Bianchi identity from $d^2 = 0$.** Apply the exterior derivative to Cartan's second structural equation: $d\Omega = d(d\omega + \omega \wedge \omega) = d\omega \wedge \omega - \omega \wedge d\omega = (\Omega - \omega \wedge \omega) \wedge \omega - \omega \wedge (\Omega - \omega \wedge \omega) = \Omega \wedge \omega - \omega \wedge \Omega$. This gives the **second Bianchi identity** $d\Omega + \omega \wedge \Omega - \Omega \wedge \omega = 0$, automatic from the structural equation.

---

# Bridges

- **[[Thm - Cartan's First Structural Equation]]** — The two structural equations together capture the entire content of a connection: the first encodes torsion (and, for torsion-free connections, determines $\omega$ from $\sigma$); the second encodes curvature (always determines $\Omega$ from $\omega$). The pair gives the cleanest practical algorithm for computing the Levi-Civita connection and Riemann tensor of any concrete metric.

- **The Riemann curvature tensor** — The curvature 2-forms $\Omega^a{}_b$ are the matrix-valued 2-form repackaging of the Riemann tensor: $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\sigma^c \wedge \sigma^d$. The symmetries of $R$ (antisymmetric in $(a, b)$ from frame-antisymmetry; antisymmetric in $(c, d)$ from 2-form structure; pair-symmetric $R_{abcd} = R_{cdab}$ for Levi-Civita; first Bianchi $R^a{}_{[bcd]} = 0$) are all visible in the structural equations.

- **The Yang-Mills field strength $F = dA + A \wedge A$** — The Cartan structural equation in the principal-bundle setting gives the Yang-Mills field strength of a gauge connection. The same formula governs the electromagnetic field tensor ($G = U(1)$, $A \wedge A = 0$), the weak isospin field strength ($G = SU(2)$), and the QCD gluon field strength ($G = SU(3)$). The non-abelian Yang-Mills equations $d_A\star F = 0$ and the Bianchi identity $d_A F = 0$ are direct consequences.

- **Chern-Weil theory and characteristic classes** — Invariant polynomials of the curvature 2-form (trace, determinant, Pfaffian) produce closed differential forms whose cohomology classes are independent of the connection — the **characteristic classes** of the underlying bundle. The first Chern class is $c_1 = \tfrac{i}{2\pi}\mathrm{tr}\,\Omega$, the Euler class for an oriented bundle is the Pfaffian, etc. Integrals over closed manifolds give integer-valued topological invariants (Chern numbers, Pontryagin numbers). See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

---

# Unlocked by This

> [!tip] The Practical Algorithm for Computing the Riemann Curvature Tensor *(from Riemannian Geometry / General Relativity)*
> Combined with Cartan's first structural equation, the second structural equation provides the fastest practical algorithm for computing the Riemann curvature tensor of any concrete Riemannian or Lorentzian metric. The route: orthonormal coframe $\sigma^a$ → $d\sigma^a$ → connection 1-forms $\omega^a{}_b$ from first equation → $d\omega^a{}_b$ and $\omega \wedge \omega$ → curvature 2-forms $\Omega^a{}_b = d\omega + \omega \wedge \omega$ → Riemann tensor components $R^a{}_{bcd}$. This is the route in every general-relativity textbook for the Schwarzschild, Kerr, FRW, de Sitter, Reissner-Nordström, and Friedmann-Lemaître-Robertson-Walker metrics.

> [!tip] Yang-Mills Theory and the Field Strength *(from Gauge Theory)*
> The same structural equation $F = dA + A \wedge A$ (with $A$ the gauge potential) defines the field strength of any Yang-Mills gauge theory. For abelian $G = U(1)$ this is Maxwell electromagnetism: $A_\mu$ is the vector potential, $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is the field tensor. For non-abelian $G$, the $A \wedge A$ term introduces the self-interaction of the gauge field, leading to the non-linearities of Yang-Mills theory, the existence of instantons, and the asymptotic freedom of QCD. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

> [!tip] Chern-Weil Theory and Characteristic Classes *(from Algebraic Topology)*
> Invariant polynomials of $\Omega$ produce closed forms whose cohomology classes are topological invariants of the bundle — the **Chern classes**, **Pontryagin classes**, **Euler class**. The **Gauss-Bonnet theorem** $\int_M K\,dA = 2\pi\chi(M)$ is the simplest Chern-Weil identity. The **Atiyah-Singer index theorem** generalises this to relate the analytic index of an elliptic operator to topological invariants of the underlying bundles. Full development of characteristic classes in [[Algebraic Topology III — Higher Homotopy and Chern Forms]] and of Chern-Weil theory in **Chern-Weil theory** proper.
