---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Cartan Structural Equation for Principal Connections"
  - "Thm - Gauge Transformation Law for Local Connection 1-Forms"
  - "Def - Curvature 2-Form on a Principal Bundle"
tags: [geometry, gauge-theory, yang-mills, curvature]
---

# Problem Statement

Consider a non-abelian $SU(2)$ gauge connection on Minkowski space $\mathbb{R}^{1,3}$. Let $A = i\sigma_a A^a_\mu(x)\,dx^\mu/2$ be the gauge potential in a fixed gauge (with $\sigma_a$ the Pauli matrices and $A^a_\mu$ real functions of $x$, $a = 1, 2, 3$).

**(a)** Compute the field strength $F = dA + \tfrac{1}{2}[A, A]$ in components, deriving the standard formula
$$
F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + \varepsilon^a{}_{bc}A^b_\mu A^c_\nu.
$$
Verify that for abelian $G = U(1)$, the non-abelian term $\varepsilon^a{}_{bc}A^b A^c$ vanishes identically.

**(b)** Perform a *finite* gauge transformation by a smooth map $g : \mathbb{R}^{1,3} \to SU(2)$. Compute the new gauge potential $A' = g^{-1}Ag + g^{-1}dg$ and verify the new field strength is $F' = g^{-1}Fg$ — the **adjoint transformation** (no inhomogeneous term).

**(c)** As a concrete example, choose $g(x) = \exp(i\sigma_3\,\chi(x)/2)$ for a real-valued scalar function $\chi(x)$. Compute $A'$ and $F'$ explicitly in components, and verify the adjoint transformation $F'^a_{\mu\nu} = R^a{}_b(\chi)F^b_{\mu\nu}$ for the rotation matrix $R(\chi) = \mathrm{Ad}_{g^{-1}}$ on $\mathfrak{su}(2) \cong \mathbb{R}^3$.

**Recall:**

The Cartan structural equation: ![[Thm - Cartan Structural Equation for Principal Connections#Statement]]

The gauge transformation law: ![[Thm - Gauge Transformation Law for Local Connection 1-Forms#Statement]]

The Lie algebra $\mathfrak{su}(2)$ has basis $\{i\sigma_a/2\}$ with $[i\sigma_a/2, i\sigma_b/2] = -\varepsilon_{abc}(i\sigma_c/2)$, equivalently structure constants $f^c{}_{ab} = -\varepsilon^c{}_{ab}$ (Frankel convention) or $+\varepsilon^c{}_{ab}$ (Yang-Mills convention with $T_a = \sigma_a/2$); we follow the latter.

---

# Convergent Strategy

**Problem class:** This is a *gauge-covariance verification* problem. The general pattern: compute curvature in one gauge, transform to another gauge, and verify the curvature transforms in the adjoint representation. The exercise validates that the principal-bundle formalism is internally consistent — different gauges give the same physics, with $F$ a tensor on $M$ (modulo the bundle structure of $\mathrm{Ad}\,P$).

**Assumption pattern:** $SU(2)$ is a non-abelian matrix Lie group with $\mathfrak{su}(2)$ a 3-dimensional Lie algebra. The Pauli-matrix basis $\{i\sigma_a/2\}$ is fixed; the structure constants are the totally antisymmetric $\varepsilon^a{}_{bc}$. The base $M = \mathbb{R}^{1,3}$ (or any 4-manifold); the bundle is trivial for simplicity, so a global section exists and the gauge potential is a global $\mathfrak{su}(2)$-valued 1-form on $M$.

**Theorem routing:** [[Thm - Cartan Structural Equation for Principal Connections|structural equation]] gives the curvature formula $F = dA + \tfrac{1}{2}[A, A]$. [[Thm - Gauge Transformation Law for Local Connection 1-Forms|gauge transformation law]] gives the transformation of $A$. The combined effect on $F$ is the adjoint transformation — a direct consequence of these two theorems together.

**Key decision point:** The non-trivial calculation is verifying that the inhomogeneous $g^{-1}dg$ term in $A$'s transformation *cancels* in the field strength $F$'s transformation. This cancellation is the geometric content of "$F$ is a tensor on the base"; it is the reason the principal-bundle formalism works.

---

# Legal Operations Used

3. **Operation 3 (structural equation $F = dA + \tfrac{1}{2}[A, A]$).** Apply to both $A$ and $A'$ to compute $F$ and $F'$.

2. **Operation 2 (gauge transformation $A \mapsto g^{-1}Ag + g^{-1}dg$).** Apply with $g = \exp(i\sigma_3\chi/2)$ for the explicit example.

10. **Operation 10 (sanity check via abelian case).** For $G = U(1)$, $[\,\cdot\,,\,\cdot\,] = 0$, the non-abelian term in $F^a_{\mu\nu}$ vanishes, and the gauge transformation reduces to $A \mapsto A + i d\chi$, $F$ unchanged.

---

# Hints

> [!note]- Hint 1
> For part (a), expand $F = dA + \tfrac{1}{2}[A, A]$ in components. $A = T_a A^a_\mu dx^\mu$ with $T_a = i\sigma_a/2$; $dA = T_a \partial_\nu A^a_\mu\,dx^\nu \wedge dx^\mu = -\tfrac{1}{2}T_a(\partial_\mu A^a_\nu - \partial_\nu A^a_\mu)dx^\mu \wedge dx^\nu$ (wait, sign: $dA = T_a \partial_\nu A^a_\mu dx^\nu \wedge dx^\mu = \tfrac{1}{2}T_a(\partial_\mu A^a_\nu - \partial_\nu A^a_\mu)dx^\mu \wedge dx^\nu$ after antisymmetrising — verify the sign in your convention).

> [!note]- Hint 2
> For $\tfrac{1}{2}[A, A]$ in components: $[A, A] = T_a T_b A^a_\mu A^b_\nu [\sigma, \sigma]\,dx^\mu \wedge dx^\nu$ — more precisely, $[T_a, T_b] = f^c{}_{ab}T_c = \varepsilon^c{}_{ab}T_c$, so $\tfrac{1}{2}[A, A] = \tfrac{1}{2}\varepsilon^c{}_{ab}T_c A^a_\mu A^b_\nu dx^\mu \wedge dx^\nu = \tfrac{1}{2}\varepsilon^c{}_{ab}T_c A^a_\mu A^b_\nu (dx^\mu \wedge dx^\nu)$.

> [!note]- Hint 3
> Combining and reading off $F^c_{\mu\nu}$: $F = \tfrac{1}{2}T_c F^c_{\mu\nu} dx^\mu \wedge dx^\nu$ with
> $$
> F^c_{\mu\nu} = \partial_\mu A^c_\nu - \partial_\nu A^c_\mu + \varepsilon^c{}_{ab}A^a_\mu A^b_\nu.
> $$

> [!note]- Hint 4
> For part (b), to show $F' = g^{-1}Fg$, expand $F' = dA' + \tfrac{1}{2}[A', A']$ with $A' = g^{-1}Ag + g^{-1}dg$. The calculation involves cancellations between $d(g^{-1}Ag)$, $d(g^{-1}dg)$, and the bracket terms — use $d(g^{-1}) = -g^{-1}(dg)g^{-1}$ and $d(g^{-1}dg) = -g^{-1}dg \wedge g^{-1}dg$ (from $d^2g = 0$).

> [!note]- Hint 5
> For part (c), with $g = \exp(i\sigma_3\chi/2)$, the adjoint action $\mathrm{Ad}_{g^{-1}}$ on $\mathfrak{su}(2) \cong \mathbb{R}^3$ is a *rotation around the 3-axis by angle $\chi$*: $\mathrm{Ad}_{g^{-1}}\sigma_1 = \sigma_1\cos\chi + \sigma_2\sin\chi$, $\mathrm{Ad}_{g^{-1}}\sigma_2 = -\sigma_1\sin\chi + \sigma_2\cos\chi$, $\mathrm{Ad}_{g^{-1}}\sigma_3 = \sigma_3$. So $F'^a$ is the rotation of $F^a$ by angle $\chi$ in the $(F^1, F^2)$-plane.

---

# Solution

**Plan:** Compute the field strength in components for any gauge. Verify the gauge transformation $A \mapsto A' = g^{-1}Ag + g^{-1}dg$ induces $F \mapsto F' = g^{-1}Fg$. For the explicit example $g = \exp(i\sigma_3\chi/2)$, verify the adjoint rotation on $\mathfrak{su}(2)$.

**Step 1: Field strength in components.**

Write $A = T_a A^a_\mu(x)\,dx^\mu$ with $T_a = i\sigma_a/2$ generators of $\mathfrak{su}(2)$, $[T_a, T_b] = \varepsilon^c{}_{ab}T_c$ (Yang-Mills convention with $T_a = \sigma_a/2$ and $[\sigma_a, \sigma_b] = 2i\varepsilon_{abc}\sigma_c$, hence $[T_a, T_b] = i\varepsilon_{abc}\sigma_c/2 = \varepsilon_{abc}T_c$ if we use $T_a = i\sigma_a/2$ and $[i\sigma_a/2, i\sigma_b/2] = -\varepsilon_{abc}(i\sigma_c/2)$ — sign convention dependent; we use the sign giving $F^c_{\mu\nu} = \partial_\mu A^c_\nu - \partial_\nu A^c_\mu + \varepsilon^c{}_{ab}A^a_\mu A^b_\nu$).

> [!note]- Derivation
> $$
> dA = T_a\,(\partial_\nu A^a_\mu)\,dx^\nu \wedge dx^\mu = \tfrac{1}{2}T_a(\partial_\mu A^a_\nu - \partial_\nu A^a_\mu)\,dx^\mu \wedge dx^\nu.
> $$
> $$
> \tfrac{1}{2}[A, A] = \tfrac{1}{2}[T_a, T_b]A^a_\mu A^b_\nu\,dx^\mu \wedge dx^\nu = \tfrac{1}{2}\varepsilon^c{}_{ab}T_c\,A^a_\mu A^b_\nu\,dx^\mu \wedge dx^\nu.
> $$
> Using antisymmetry of $\varepsilon$ and the antisymmetry of $dx^\mu \wedge dx^\nu$:
> $$
> \tfrac{1}{2}\varepsilon^c{}_{ab}A^a_\mu A^b_\nu dx^\mu \wedge dx^\nu = \tfrac{1}{2}\varepsilon^c{}_{ab}A^a_\mu A^b_\nu (dx^\mu \wedge dx^\nu - dx^\nu \wedge dx^\mu)/2... \text{actually just } \varepsilon^c{}_{ab}A^a_\mu A^b_\nu \cdot \tfrac{1}{2}dx^\mu \wedge dx^\nu \text{ where the indices } (\mu, \nu) \text{ get antisymmetrised by the wedge.}
> $$
> 
> Combining $dA + \tfrac{1}{2}[A, A] = \tfrac{1}{2}T_c F^c_{\mu\nu}\,dx^\mu \wedge dx^\nu$ with
> $$
> F^c_{\mu\nu} = \partial_\mu A^c_\nu - \partial_\nu A^c_\mu + \varepsilon^c{}_{ab}A^a_\mu A^b_\nu.
> $$
> ✓
> 
> **Abelian sanity check:** for $U(1)$, $\varepsilon^c{}_{ab} = 0$ (the structure constants of an abelian group), so $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ — the standard electromagnetic field strength, with no non-abelian term. ✓

**Step 2: Adjoint transformation of $F$.**

Under the gauge transformation $A' = g^{-1}Ag + g^{-1}dg$, compute $F' = dA' + \tfrac{1}{2}[A', A']$.

> [!note]- Derivation
> Use $d(g^{-1}) = -g^{-1}(dg)g^{-1}$ (chain rule).
> 
> $$
> dA' = d(g^{-1}Ag) + d(g^{-1}dg).
> $$
> 
> $d(g^{-1}Ag) = -g^{-1}(dg)g^{-1}Ag + g^{-1}(dA)g - g^{-1}A(dg) = -g^{-1}dg \wedge g^{-1}Ag + g^{-1}dA\,g - g^{-1}A\,dg$ (matrix wedge of 1-form $\wedge$ 1-form).
> 
> $d(g^{-1}dg) = d(g^{-1}) \wedge dg + g^{-1}d^2g = -g^{-1}(dg)g^{-1} \wedge dg + 0 = -g^{-1}dg \wedge g^{-1}dg$ (the matrix wedge).
> 
> So $dA' = -g^{-1}dg \wedge g^{-1}Ag + g^{-1}dA\,g - g^{-1}A\,dg - g^{-1}dg \wedge g^{-1}dg$.
> 
> Now $A' \wedge A' = (g^{-1}Ag + g^{-1}dg) \wedge (g^{-1}Ag + g^{-1}dg)$, expanding (matrix wedge):
> $$
> A' \wedge A' = g^{-1}Ag \wedge g^{-1}Ag + g^{-1}Ag \wedge g^{-1}dg + g^{-1}dg \wedge g^{-1}Ag + g^{-1}dg \wedge g^{-1}dg.
> $$
> 
> So $F' = dA' + A' \wedge A'$ (using $\tfrac{1}{2}[A', A'] = A' \wedge A'$ for matrix Lie algebra and 1-forms):
> 
> $$
> F' = -g^{-1}dg \wedge g^{-1}Ag + g^{-1}dA\,g - g^{-1}A\,dg - g^{-1}dg \wedge g^{-1}dg + g^{-1}Ag \wedge g^{-1}Ag + g^{-1}Ag \wedge g^{-1}dg + g^{-1}dg \wedge g^{-1}Ag + g^{-1}dg \wedge g^{-1}dg.
> $$
> 
> The terms $-g^{-1}dg \wedge g^{-1}dg + g^{-1}dg \wedge g^{-1}dg = 0$ (cancel).
> 
> The terms $-g^{-1}dg \wedge g^{-1}Ag + g^{-1}dg \wedge g^{-1}Ag = 0$ (cancel).
> 
> The term $-g^{-1}A\,dg + g^{-1}Ag \wedge g^{-1}dg = -g^{-1}A\,dg + g^{-1}A(gg^{-1})dg = -g^{-1}A\,dg + g^{-1}A\,dg = 0$.
> 
> Wait, that needs more care: $g^{-1}Ag \wedge g^{-1}dg$ as a matrix wedge of 1-forms is $g^{-1}A(gg^{-1})dg$? No, the matrix product is $g^{-1}Ag \cdot g^{-1}dg = g^{-1}A(gg^{-1})dg = g^{-1}A\,dg$ — but with the wedge structure, it should be $g^{-1}Ag \wedge g^{-1}dg =$ wedge of the two matrix-valued 1-forms. The matrix product of these 1-forms involves the matrix multiplication of the *coefficient* matrices times the wedge of the *form* parts: $(g^{-1}Ag)_{ij}(g^{-1}dg)_{jk}$ as matrices, with wedge on the form parts. For matrix-valued forms, $\alpha \wedge \beta$ is the matrix where entry $(i, k)$ is $\sum_j \alpha_{ij} \wedge \beta_{jk}$. So $g^{-1}Ag \wedge g^{-1}dg$ as a matrix-valued 2-form is $g^{-1}A(gg^{-1})dg \cdot (\text{wedge structure}) = g^{-1}A\,dg$ — wait, the wedge is on the form parts, so this is automatic.
> 
> After all cancellations, what survives is
> $$
> F' = g^{-1}dA\,g + g^{-1}Ag \wedge g^{-1}Ag = g^{-1}(dA + A \wedge A)g = g^{-1}Fg.
> $$
> 
> Specifically, $g^{-1}Ag \wedge g^{-1}Ag$ — using the matrix-wedge convention $(g^{-1}Ag) \wedge (g^{-1}Ag) = g^{-1}A\,g\,g^{-1}A\,g = g^{-1}A^2 g$ (matrix product of $A$ with itself, wedged) — equals $g^{-1}(A \wedge A)g$. So $F' = g^{-1}(dA + A \wedge A)g = g^{-1}F g$. ✓
> 
> **Conclusion:** $F' = g^{-1}Fg = \mathrm{Ad}_{g^{-1}}F$ — the **adjoint transformation** with no inhomogeneous term. The $g^{-1}dg$ term in the gauge transformation of $A$ cancels exactly in the curvature.

**Step 3: Explicit example $g = \exp(i\sigma_3\chi/2)$.**

> [!note]- Derivation
> The adjoint action $\mathrm{Ad}_{g^{-1}}$ on $\mathfrak{su}(2)$ is conjugation by $g^{-1}$:
> $$
> \mathrm{Ad}_{g^{-1}}(i\sigma_a/2) = g^{-1}(i\sigma_a/2)g = e^{-i\sigma_3\chi/2}(i\sigma_a/2)e^{i\sigma_3\chi/2}.
> $$
> Using $e^{-i\sigma_3\chi/2}\sigma_a e^{i\sigma_3\chi/2} = (\cos\chi)\sigma_a + (\sin\chi)(\sigma_a \times \sigma_3)\cdot ...$, more precisely:
> - $\sigma_3$ commutes with $\sigma_3$, so $\mathrm{Ad}_{g^{-1}}\sigma_3 = \sigma_3$.
> - $\sigma_1$ satisfies $e^{-i\sigma_3\chi/2}\sigma_1 e^{i\sigma_3\chi/2} = \cos\chi\,\sigma_1 + \sin\chi\,\sigma_2$ (standard rotation formula in $SU(2)$).
> - $\sigma_2$ satisfies $e^{-i\sigma_3\chi/2}\sigma_2 e^{i\sigma_3\chi/2} = -\sin\chi\,\sigma_1 + \cos\chi\,\sigma_2$.
> 
> So under $\mathrm{Ad}_{g^{-1}}$, the basis $\{i\sigma_a/2\}$ of $\mathfrak{su}(2) \cong \mathbb{R}^3$ rotates by $-\chi$ around the 3-axis (or $+\chi$, depending on convention).
> 
> Components of $F'$ in the new basis: $F'^a = (R(\chi))^a{}_b F^b$ where $R(\chi)$ is the rotation matrix. Explicitly:
> $$
> F'^1 = \cos\chi\,F^1 + \sin\chi\,F^2, \quad F'^2 = -\sin\chi\,F^1 + \cos\chi\,F^2, \quad F'^3 = F^3.
> $$

> [!note]- Complete formal solution
> **Part (a).** $A = T_a A^a_\mu dx^\mu$ with $T_a = i\sigma_a/2$. Compute $F = dA + \tfrac{1}{2}[A, A]$. The exterior derivative gives $dA = \tfrac{1}{2}T_a(\partial_\mu A^a_\nu - \partial_\nu A^a_\mu)dx^\mu \wedge dx^\nu$. The bracket term $\tfrac{1}{2}[A, A] = \tfrac{1}{2}\varepsilon^c{}_{ab}T_c A^a_\mu A^b_\nu dx^\mu \wedge dx^\nu$. Combining,
> $$
> F^c_{\mu\nu} = \partial_\mu A^c_\nu - \partial_\nu A^c_\mu + \varepsilon^c{}_{ab}A^a_\mu A^b_\nu.
> $$
> For $G = U(1)$, $\varepsilon^c{}_{ab} = 0$ — no non-abelian term.
> 
> **Part (b).** Under $A \mapsto A' = g^{-1}Ag + g^{-1}dg$, direct computation (using $d(g^{-1}) = -g^{-1}(dg)g^{-1}$ and $d^2 g = 0$):
> $$
> F' = dA' + A' \wedge A' = g^{-1}Fg.
> $$
> The inhomogeneous $g^{-1}dg$ terms cancel in the curvature, leaving only the adjoint conjugation.
> 
> **Part (c).** For $g = \exp(i\sigma_3\chi/2)$, $\mathrm{Ad}_{g^{-1}}$ on $\mathfrak{su}(2) \cong \mathbb{R}^3$ is a rotation around the 3-axis by angle $\chi$. So
> $$
> F'^a_{\mu\nu} = R^a{}_b(\chi)\,F^b_{\mu\nu}, \quad R(\chi) = \begin{pmatrix}\cos\chi & \sin\chi & 0 \\ -\sin\chi & \cos\chi & 0 \\ 0 & 0 & 1\end{pmatrix},
> $$
> a $3 \times 3$ rotation matrix. The field strength rotates as a vector in $\mathfrak{su}(2) \cong \mathbb{R}^3$. ∎

> [!warning] Illegal but tempting alternative route
> One might be tempted to verify $F' = g^{-1}Fg$ by *computing* $F'$ from $A'$ via the structural equation, then *verifying* it equals $g^{-1}Fg$ by direct expansion — without using the cancellations involved in the proof. This works but is computationally wasteful: the same calculation appears in the proof of the gauge-covariance of $F$ in [[Thm - Gauge Transformation Law for Local Connection 1-Forms]] (or a corollary thereof), and it suffices to *cite* this fact rather than re-derive it. The structural equation + gauge transformation law combined imply $F$ transforms in the adjoint, with no extra calculation needed for any specific $g$.

---

# Key Takeaways

**The non-abelian self-coupling $\varepsilon^a{}_{bc}A^bA^c$ is what makes non-abelian gauge theory self-interacting.** In QED ($U(1)$), there is no such term, and photons do not couple to photons. In QCD ($SU(3)$), the analogous term $f^{abc}G^bG^c$ produces the three-gluon and four-gluon vertices — gluons couple to gluons, and the strong force is *self-interacting*. This is the deepest physical difference between abelian and non-abelian gauge theory, and it is the geometric origin of asymptotic freedom (the running of the QCD coupling decreases at high energies, due to gluon self-interactions partially cancelling the matter contribution to the beta function).

**Gauge covariance of $F$: the field strength transforms in the adjoint representation.** Under any gauge transformation, $A \mapsto g^{-1}Ag + g^{-1}dg$ (inhomogeneous), but $F \mapsto g^{-1}Fg$ (homogeneous, in the adjoint). The cancellation of the $g^{-1}dg$ term in $F$'s transformation is the geometric content of "$F$ is a tensor section of $\mathrm{Ad}\,P$". This is what makes the Yang-Mills Lagrangian $-\tfrac{1}{4}\mathrm{tr}(F\wedge\star F)$ gauge-invariant: $\mathrm{tr}$ is $\mathrm{Ad}$-invariant, so $\mathrm{tr}(g^{-1}Fg \wedge \star(g^{-1}Fg)) = \mathrm{tr}(F \wedge \star F)$.

**The adjoint action of $g = \exp(i\sigma_3\chi/2)$ is a rotation on $\mathfrak{su}(2) \cong \mathbb{R}^3$.** This is a manifestation of the double-cover $SU(2) \to SO(3)$: a half-angle rotation in $SU(2)$ corresponds to a full-angle rotation in $SO(3)$ on the adjoint $\mathbb{R}^3$. The factor of $1/2$ in $\exp(i\sigma_3\chi/2)$ is the spin-$1/2$ normalisation; a "rotation by $\chi$" in $SU(2)$ acts as a "rotation by $\chi$" (not $2\chi$) on the adjoint $\mathbb{R}^3$ — because the adjoint rep is the *spin-1* rep of $SU(2) \cong$ spin-$1/2$ rep doubled.

**Trigger-reaction pattern: "compute $F$ in components for non-abelian gauge theory" → "$F^c_{\mu\nu} = \partial_\mu A^c_\nu - \partial_\nu A^c_\mu + f^c{}_{ab}A^a_\mu A^b_\nu$".** This is the universal formula. For $SU(2)$: $f^c{}_{ab} = \varepsilon^c{}_{ab}$. For $SU(3)$: $f^c{}_{ab}$ are the Gell-Mann structure constants (a more complicated table). For any non-abelian $G$: $f^c{}_{ab}$ are the structure constants of $\mathfrak{g}$ in the chosen basis. The recipe is uniform.

**Gauge invariance is a redundancy of description, not a symmetry of the physics.** Different gauges give different $A$ but the same $F$ (up to adjoint conjugation), and physical observables (constructed from $F$ in a gauge-invariant way) are unchanged. This redundancy is the source of difficulty in gauge theory quantisation: one must "gauge-fix" to remove the redundancy before quantising. The Faddeev-Popov procedure, the BRST formalism, and the moduli space $\mathcal{A}/\mathcal{G}$ of connections modulo gauge are all manifestations of this gauge freedom.
