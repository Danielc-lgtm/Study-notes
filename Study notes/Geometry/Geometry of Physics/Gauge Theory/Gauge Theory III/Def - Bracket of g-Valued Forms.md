---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Lie-Algebra-Valued Differential Form"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - The Wedge Product on a Manifold"
tags: [geometry, gauge-theory, differential-forms, lie-algebras]
---

# Notation

$M$ is a smooth manifold, $\mathfrak{g}$ a finite-dimensional Lie algebra with bracket $[\,\cdot\,,\,\cdot\,]_\mathfrak{g} : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$, and $\Omega^p(M; \mathfrak{g}) = \Omega^p(M) \otimes \mathfrak{g}$ the space of [[Def - Lie-Algebra-Valued Differential Form|\mathfrak{g}-valued p-forms]]. We write $\alpha \wedge \beta$ for the ordinary wedge product of forms and $[\xi, \eta]$ for the Lie bracket on $\mathfrak{g}$. The new bracket of two $\mathfrak{g}$-valued forms is also denoted $[\,\cdot\,,\,\cdot\,]$ — the context (form-degree) disambiguates.

---

# Axiom Motivation

The first question this definition must answer: why do we need a bracket of $\mathfrak{g}$-valued forms at all? The reason is the Cartan structural equation. The curvature of a connection $\omega$ on a principal bundle is $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$. The first term $d\omega$ is the ordinary exterior derivative of a $\mathfrak{g}$-valued 1-form — well defined from the previous page. The second term is a $\mathfrak{g}$-valued 2-form built from $\omega$, and for it to make sense as an object on the same level as $d\omega$ we need an operation that takes two $\mathfrak{g}$-valued 1-forms and produces a $\mathfrak{g}$-valued 2-form. The bracket of forms is precisely this operation.

What should the definition be? On a $\mathfrak{g}$-valued form, two natural pieces of structure are competing for attention: the wedge product (which combines forms) and the Lie bracket of $\mathfrak{g}$ (which combines Lie-algebra elements). The most economical definition combines both: on simple tensors $\alpha \otimes \xi$ and $\beta \otimes \eta$, take the wedge of the forms and the bracket of the Lie-algebra elements:
$$
[\alpha \otimes \xi, \beta \otimes \eta] := (\alpha \wedge \beta) \otimes [\xi, \eta].
$$
This is the unique definition that is bilinear, $C^\infty(M)$-bilinear (so it depends pointwise on the values), and graded-symmetric in the correct way — the wedge contributes a $(-1)^{pq}$ on swapping, the bracket contributes a $-1$, and they multiply.

Why this and not some other combination? Three reasons. (i) **Bilinearity over $C^\infty(M)$**: the bracket must be $C^\infty(M)$-bilinear so it commutes with restriction to open sets and pullback under maps; the wedge product is the unique such operation on forms. (ii) **Compatibility with the matrix case**: when $\mathfrak{g}$ is a matrix Lie algebra and we identify $[\xi, \eta] = \xi\eta - \eta\xi$, the bracket of forms reduces — after computation — to $[\alpha, \beta] = \alpha \wedge \beta - (-1)^{pq}\beta \wedge \alpha$, where the wedge is the matrix wedge (entry-wise wedge of matrix-valued forms). In particular, for two 1-forms $\alpha$ and $\beta$, $[\alpha, \beta] = \alpha \wedge \beta + \beta \wedge \alpha$ (anticommutator). And for $\alpha$ a 1-form with itself, $\tfrac{1}{2}[\alpha, \alpha] = \alpha \wedge \alpha$ (matrix wedge, not symmetric: $\alpha \wedge \alpha \neq 0$ for matrix-valued $\alpha$ because the matrix entries do not commute under wedge). This is the foundational identity that makes the Cartan structural equation work uniformly across all formulations. (iii) **Graded Jacobi**: the bracket satisfies the graded Jacobi identity, making $\Omega^\bullet(M; \mathfrak{g})$ a graded Lie algebra.

What would break if we dropped any of these features? If the bracket failed bilinearity, the curvature would not be a tensor. If it failed compatibility with the matrix case, the structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega] = d\omega + \omega \wedge \omega$ (for matrix groups) would have two inconsistent forms. If it failed graded Jacobi, the Bianchi identity would not hold automatically.

The graded symmetry deserves a moment's reflection. For ordinary forms, $\alpha \wedge \beta = (-1)^{pq}\beta \wedge \alpha$. For the Lie bracket on $\mathfrak{g}$, $[\eta, \xi] = -[\xi, \eta]$. Combining: $[\beta \otimes \eta, \alpha \otimes \xi] = (\beta \wedge \alpha) \otimes [\eta, \xi] = (-1)^{pq}(\alpha \wedge \beta) \otimes (-[\xi, \eta]) = (-1)^{pq+1}[\alpha \otimes \xi, \beta \otimes \eta]$. So $[\beta, \alpha] = (-1)^{pq+1}[\alpha, \beta]$ for forms of degrees $p$ and $q$. In particular, $[\alpha, \alpha] = 0$ for $\alpha$ of *even* degree, but $[\alpha, \alpha]$ need not vanish for $\alpha$ of *odd* degree — and indeed this nonvanishing is the entire content of the non-abelian curvature term.

The graded Leibniz with respect to $d$ follows from the rule. Specifically:
$$
d[\alpha, \beta] = [d\alpha, \beta] + (-1)^p[\alpha, d\beta].
$$
This is what allows the Bianchi identity to be derived from a one-line computation:
$$
d\Omega = d^2\omega + \tfrac{1}{2}d[\omega, \omega] = 0 + \tfrac{1}{2}\big([d\omega, \omega] - [\omega, d\omega]\big) = [d\omega, \omega] = [\Omega - \tfrac{1}{2}[\omega, \omega], \omega] = [\Omega, \omega],
$$
where the last step uses $[[Thm - Bianchi Identity for Principal Connections|Thm - Bianchi Identity for Principal Connections]] + (-1)^{qp}[\beta, [\gamma, \alpha]] + (-1)^{rq}[\gamma, [\alpha, \beta]] = 0$ for $\alpha, \beta, \gamma$ of degrees $p, q, r$.
4. **Matrix-group case:** if $\mathfrak{g}$ is a matrix Lie algebra and we identify $\mathfrak{g}$-valued forms with matrices of forms, then
$$
[\alpha, \beta] = \alpha \wedge \beta - (-1)^{pq}\beta \wedge \alpha,
$$
where the wedge on the right is the matrix wedge (entries multiplied by the wedge of their forms). In particular for a 1-form $\alpha$: $\tfrac{1}{2}[\alpha, \alpha] = \alpha \wedge \alpha$.

---

# Categorical / Structural Definition

The triple $(\Omega^\bullet(M; \mathfrak{g}), d, [\,\cdot\,,\,\cdot\,])$ is a **differential graded Lie algebra (DGLA)**: a $\mathbb{Z}$-graded vector space (with grading by form-degree) equipped with a degree-$+1$ derivation $d$ satisfying $d^2 = 0$, and a graded-symmetric bracket of degree $0$ satisfying graded Jacobi and graded Leibniz with $d$.

Categorically, the bracket is the image of $\Omega^p(M) \otimes_\mathbb{R} \Omega^q(M) \otimes_\mathbb{R} (\mathfrak{g} \otimes_\mathbb{R} \mathfrak{g}) \to \Omega^{p+q}(M) \otimes_\mathbb{R} \mathfrak{g}$ obtained by composing the wedge product on the form factor with the Lie bracket on the Lie-algebra factor, then reassembling. This is the unique natural transformation of this form — the bracket is forced by the structure of the tensor product.

---

# Relate to Other Fields / Compression

The graded Lie algebra structure of $\Omega^\bullet(M; \mathfrak{g})$ is the same construction that appears in:

- **The de Rham complex of a Lie group**: $\Omega^\bullet(G; \mathbb{R})$ with the wedge product is a graded commutative algebra; tensoring with $\mathfrak{g}$ and using the Lie bracket gives the bracket structure on left-invariant forms, which restricts to the Chevalley-Eilenberg differential on $\Lambda^\bullet \mathfrak{g}^*$.
- **Deformation theory**: a DGLA controls a deformation problem — the solutions of $d\omega + \tfrac{1}{2}[\omega, \omega] = 0$ modulo the gauge action are the (formal) moduli space of deformations. For $\Omega^\bullet(M; \mathfrak{g})$, these are flat $G$-connections on $M$, classified by representations $\pi_1(M) \to G$.
- **String theory and supergeometry**: the BV-BRST formalism uses DGLA structures pervasively; the bracket of $\mathfrak{g}$-valued forms is the prototype.

**True name:** the bracket of forms is *the matrix commutator wedge product when $\mathfrak{g}$ is a matrix Lie algebra*. The formula $[\alpha, \beta] = \alpha \wedge \beta - (-1)^{pq}\beta \wedge \alpha$ for matrix-valued forms is the operational form physicists actually compute with. For 1-forms it reads $[\alpha, \beta] = \alpha \wedge \beta + \beta \wedge \alpha$ (anticommutator wedge); for $\alpha = \beta$, $[\alpha, \alpha] = 2\alpha \wedge \alpha$, so $\tfrac{1}{2}[\alpha, \alpha] = \alpha \wedge \alpha$ — the identity that lets the Cartan structural equation be written as $\Omega = d\omega + \omega \wedge \omega$ in matrix notation.

---

# Examples / Corollaries

**Example.** For $\mathfrak{g} = \mathfrak{su}(2) = \{i\sigma_a : a = 1, 2, 3\}$ with $[\sigma_a, \sigma_b] = 2i\varepsilon_{abc}\sigma_c$ (Pauli matrices), and two $\mathfrak{su}(2)$-valued 1-forms $A = i\sigma_a A^a$, $B = i\sigma_b B^b$, the bracket is
$$
[A, B] = [i\sigma_a, i\sigma_b] \otimes A^a \wedge B^b = -[\sigma_a, \sigma_b] \otimes A^a \wedge B^b = -2i\varepsilon_{abc}\sigma_c \otimes A^a \wedge B^b = -2\varepsilon_{abc}(i\sigma_c) \otimes A^a \wedge B^b.
$$
In particular $\tfrac{1}{2}[A, A] = -\varepsilon_{abc}(i\sigma_c) \otimes A^a \wedge A^b$, the non-abelian self-coupling term in the Yang-Mills field strength.

**Example.** For abelian $\mathfrak{g} = \mathfrak{u}(1) = i\mathbb{R}$, the Lie bracket vanishes identically: $[\xi, \eta]_\mathfrak{g} = 0$ for all $\xi, \eta$. Hence $[\alpha, \beta] = 0$ for all $\mathfrak{u}(1)$-valued forms — the bracket is trivial, and the Cartan structural equation collapses to $F = dA$ (electromagnetism).

**Corollary.** For a 1-form $A$ and a 2-form $B$ valued in $\mathfrak{g}$, $[A, B]$ is a 3-form valued in $\mathfrak{g}$. In a matrix-group convention, $[A, B] = A \wedge B - B \wedge A$ (the matrix commutator of wedges, no sign for the swap since $1 \cdot 2 = 2$ is even).

**Corollary (key identity).** For any $\mathfrak{g}$-valued 1-form $\omega$,
$$
[\omega, [\omega, \omega]] = 0
$$
identically — a direct consequence of graded Jacobi applied to three copies of $\omega$ (all odd-degree). This identity is what makes the proof of the Bianchi identity collapse to one line.

**Is NOT an instance:** $\alpha \wedge \beta$ for ordinary ($\mathbb{R}$-valued) forms is *not* the bracket of $\mathfrak{g}$-valued forms — they have different output spaces. The bracket reduces to zero if $\mathfrak{g}$ is abelian; the wedge does not.

**Is NOT an instance:** the matrix product $\alpha \cdot \beta$ of matrix-valued forms (no graded sign) is *not* the bracket — it lacks the antisymmetry of the Lie bracket. The bracket is the commutator $\alpha \beta - (-1)^{pq}\beta\alpha$, not the product.

**Calibration check.** If you have understood the definition, you should be able to: (i) prove that $[\alpha, \alpha] = 0$ for even-degree $\alpha$ but not in general for odd-degree $\alpha$, by computing both cases from graded symmetry; (ii) verify the graded Leibniz $d[\alpha, \beta] = [d\alpha, \beta] + (-1)^p[\alpha, d\beta]$ on simple tensors $\alpha = a \otimes \xi$, $\beta = b \otimes \eta$, using only the definition and the ordinary Leibniz of $d$ on forms; (iii) for matrix Lie algebra $\mathfrak{g}$, derive the formula $[\alpha, \beta] = \alpha\beta - (-1)^{pq}\beta\alpha$ (matrix wedge) from the basis-component definition $[\alpha, \beta] = [E_R, E_S]\,\alpha^R \wedge \beta^S$ by writing $E_R E_S - E_S E_R$ explicitly.

---

# Unlocked by This

> [!tip] Cartan Structural Equation *(from Gauge Theory III)*
> The bracket of forms is the key ingredient in the Cartan structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$ — without the bracket, there is no curvature formula for non-abelian connections. The non-abelian term $\tfrac{1}{2}[\omega, \omega]$ is precisely the contribution of the bracket of $\omega$ with itself. See [[Thm - Cartan Structural Equation for Principal Connections]].

> [!tip] Bianchi Identity *(from Gauge Theory III)*
> The Bianchi identity $d\Omega + [\omega, \Omega] = 0$ uses the bracket of forms to combine $\omega$ (a 1-form) with $\Omega$ (a 2-form) into a 3-form. The proof is a one-line computation using graded Jacobi $[\omega, [\omega, \omega]] = 0$. See [[Thm - Bianchi Identity for Principal Connections]].

> [!tip] L-infinity Algebras *(from Higher Algebra)*
> The DGLA $\Omega^\bullet(M; \mathfrak{g})$ is the simplest example of an **$L_\infty$-algebra** — the homotopy-theoretic generalisation that allows graded Jacobi to hold only up to coherent higher homotopies. $L_\infty$-algebras are the natural setting for **derived deformation theory** (Kontsevich) and for the **BV formalism** of gauge theory quantisation. The Maurer-Cartan equation generalises to "$L_\infty$ Maurer-Cartan" equations involving brackets of three, four, and higher arities.
