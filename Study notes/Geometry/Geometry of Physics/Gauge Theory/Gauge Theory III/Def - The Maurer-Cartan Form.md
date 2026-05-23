---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - Left-Invariant Vector Field"
  - "Def - Lie-Algebra-Valued Differential Form"
tags: [geometry, gauge-theory, lie-groups, differential-forms]
---

# Notation

$G$ is a Lie group with [[Def - The Lie Algebra of a Lie Group|Lie algebra]] $\mathfrak{g} = T_e G$. For $g \in G$, $L_g : G \to G$ is the **left-translation** map $h \mapsto gh$, and $(dL_g)_h : T_h G \to T_{gh} G$ is its differential. A vector field $X \in \mathfrak{X}(G)$ is **left-invariant** if $(dL_g)_h X_h = X_{gh}$ for all $g, h \in G$. The basis of left-invariant vector fields obtained by left-translating a basis $\{E_R\}$ of $\mathfrak{g}$ is denoted $\{X^R\}$, and the dual basis of left-invariant 1-forms is $\{\sigma^R\}$ — that is, $\sigma^R(X^S) = \delta^R_S$ at every point of $G$.

> [!warning] Convention — left vs. right invariance
> Throughout we use the **left-invariant** Maurer-Cartan form $\theta_G = g^{-1}dg$ (matrix-group notation) for which the Maurer-Cartan equation reads $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = 0$. The right-invariant analogue $dg\,g^{-1}$ satisfies the equation with the opposite sign of the bracket. Frankel and Kobayashi-Nomizu use the left convention; some physics references use the right. When in doubt, verify by checking $\theta_G(X) = X$ for $X \in \mathfrak{g}$ treated as a left-invariant vector field at the identity.

---

# Axiom Motivation

What is the canonical $\mathfrak{g}$-valued 1-form on a Lie group $G$? Once one accepts that a Lie group is the geometric object that carries $\mathfrak{g}$ as its tangent space at the identity, one is led to ask: is there a *natural* way to identify each tangent space $T_g G$ with $\mathfrak{g}$, and to encode this identification as a differential form? The answer is yes, and the form that does it is the Maurer-Cartan form.

The construction is forced by group structure. For each $g \in G$, the left-translation $L_g : G \to G$, $h \mapsto gh$, is a diffeomorphism. Its differential at the identity, $(dL_g)_e : \mathfrak{g} = T_e G \to T_g G$, is a linear isomorphism — so it provides a canonical identification of $T_g G$ with $\mathfrak{g}$. *Inverting* this isomorphism gives a canonical map $T_g G \to \mathfrak{g}$, namely $(dL_{g^{-1}})_g : T_g G \to T_e G = \mathfrak{g}$. This is the Maurer-Cartan form $\theta_G$ at $g$:
$$
\theta_G(X)|_g := (dL_{g^{-1}})_g(X), \quad X \in T_g G.
$$
The form takes a tangent vector at $g$ and left-translates it back to the identity, where it lives in $\mathfrak{g}$.

A natural alternative would be to use right-translation, $\tilde\theta_G(X)|_g := (dR_{g^{-1}})_g(X)$. This is the **right-invariant Maurer-Cartan form**, and it differs from the left-invariant one by a sign in the structural equation. Both exist; both are canonical. The choice between them is conventional and fixed for life when one writes down the first formula.

Why is this the *right* definition? Three reasons.

First, it is **basis-free**: $\theta_G$ is defined without choosing coordinates or a basis of $\mathfrak{g}$. The definition uses only the group structure (left-translation) and the smooth structure of $G$, both of which are canonical to $G$.

Second, in any basis $\{E_R\}$ of $\mathfrak{g}$ with left-invariant vector fields $X^R$ and dual left-invariant 1-forms $\sigma^R$, the form $\theta_G$ decomposes as $\theta_G = E_R \otimes \sigma^R$. This is the "tuple of left-invariant 1-forms" description. The verification is immediate: $\theta_G(X^S)|_g = (dL_{g^{-1}})_g X^S_g = X^S_e = E_S$, since $X^S$ is left-invariant, and $\sigma^R(X^S) = \delta^R_S$, so $E_R \otimes \sigma^R$ evaluated on $X^S$ gives $E_R \delta^R_S = E_S$ — agreeing with $\theta_G(X^S)$.

Third, it satisfies the **Maurer-Cartan equation** $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = 0$, the universal template for the structural equation of every connection. This is no accident: $\theta_G$ is *exactly* the canonical flat connection on the trivial bundle $G \to \mathrm{pt}$ over a point, viewed as a principal $G$-bundle, and its curvature must vanish — that vanishing is the Maurer-Cartan equation. See [[Thm - Maurer-Cartan Equation]] for the proof.

The matrix-group notation $\theta_G = g^{-1}dg$ deserves clarification. For a matrix Lie group $G \subseteq \mathrm{GL}(n)$, points of $G$ are matrices, and $dg$ denotes the matrix-valued 1-form whose entries are $dg^i_j$ — the differentials of the matrix entries as functions on $G$. Multiplication by $g^{-1}$ on the left gives a matrix-valued 1-form $g^{-1}dg$. Evaluated on a tangent vector $X$ at $g$ (which we can think of as a matrix of derivatives), this gives $g^{-1} \cdot X = (dL_{g^{-1}})_g(X)$ — exactly the Maurer-Cartan form. So $\theta_G = g^{-1}dg$ is just the convenient matrix-group notation for the universal left-translation-back-to-identity operation.

What if we required $\theta_G$ to be both left and right invariant? On a non-abelian group this is impossible — the only such form would have to satisfy $\theta_G(X) = \theta_G(\mathrm{Ad}_g X)$ for all $X, g$, which together with the canonical normalisation $\theta_G(\xi^*) = \xi$ forces $\mathrm{Ad}_g = \mathrm{id}$ for all $g$, i.e., $G$ is abelian. The asymmetry between left and right invariance is the price of non-commutativity.

---

# The Definition

Let $G$ be a Lie group with Lie algebra $\mathfrak{g} = T_e G$.

The **(left-invariant) Maurer-Cartan form** on $G$ is the $\mathfrak{g}$-valued 1-form $\theta_G \in \Omega^1(G; \mathfrak{g})$ defined by
$$
\theta_G(X)|_g := (dL_{g^{-1}})_g(X), \quad X \in T_g G.
$$
Equivalently, in a basis $\{E_R\}$ of $\mathfrak{g}$ with left-invariant vector fields $X^R$ and dual left-invariant 1-forms $\sigma^R$ ($\sigma^R(X^S) = \delta^R_S$):
$$
\theta_G = E_R \otimes \sigma^R = \sum_R E_R \otimes \sigma^R.
$$
Equivalently, if $\xi \in \mathfrak{g}$ and $\xi^L \in \mathfrak{X}(G)$ is the left-invariant vector field with $\xi^L_e = \xi$, then $\theta_G(\xi^L_g) = \xi$ for every $g \in G$.

For a matrix Lie group $G \subseteq \mathrm{GL}(n)$, the form may be written in the convenient matrix notation
$$
\theta_G = g^{-1}dg,
$$
where $dg$ is the matrix-valued 1-form whose $(i,j)$-entry is $dg^i_j$ (the differential of the matrix-entry coordinate function).

The **right-invariant Maurer-Cartan form** is the analogous construction with right-translation:
$$
\tilde\theta_G(X)|_g := (dR_{g^{-1}})_g(X), \quad \tilde\theta_G = dg\, g^{-1} \text{ for matrix groups},
$$
satisfying $d\tilde\theta_G - \tfrac{1}{2}[\tilde\theta_G, \tilde\theta_G] = 0$ — the opposite sign.

---

# Relate to Other Fields / Compression

The Maurer-Cartan form is **the canonical flat connection on $G$ viewed as a principal $G$-bundle over a point**. Indeed: $G \to \{*\}$ is trivially a principal $G$-bundle (the right action of $G$ on itself by right multiplication is free and transitive), and a connection on this bundle is a $\mathfrak{g}$-valued 1-form on $G$ satisfying equivariance and verticality. The Maurer-Cartan form satisfies both — equivariance is the statement $R_g^*\theta_G = \mathrm{Ad}_{g^{-1}}\theta_G$ (a computation using $L_{g^{-1}h^{-1}} = L_{g^{-1}} \circ L_{h^{-1}}$); verticality is $\theta_G(\xi^*) = \xi$ where $\xi^*$ is the [[Def - Fundamental Vector Field of a Principal Bundle|fundamental vector field]] (which for $G \to *$ coincides with the left-invariant vector field). The curvature of this connection is, by the Cartan structural equation, $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G]$, which vanishes by the [[Thm - Maurer-Cartan Equation|Maurer-Cartan equation]] — so the canonical flat connection is, indeed, flat.

In **Cartan geometry** (Cartan's program of unifying Riemannian, conformal, projective, and parabolic geometries), a Cartan geometry modelled on $G/H$ is a principal $H$-bundle equipped with a $\mathfrak{g}$-valued 1-form that pointwise mimics the Maurer-Cartan form of $G$. The Maurer-Cartan equation holds in the flat (Klein-geometric) case; its failure for a general Cartan geometry is the curvature. So the Maurer-Cartan form is the *universal local model* for connection 1-forms, against which all curvature is measured.

In **Lie theory**, the Maurer-Cartan form encodes the entire local structure of $G$: from $\theta_G$ alone, the multiplication of $G$ near the identity can be reconstructed via the BCH formula. Equivalently, the dual structure-constant equation $d\sigma^R = -\tfrac{1}{2}C^R_{ST}\sigma^S \wedge \sigma^T$ (which is the basis form of the Maurer-Cartan equation) determines the Lie algebra structure constants $C^R_{ST}$ entirely.

**True name:** the Maurer-Cartan form is *the universal recipe for translating tangent vectors on $G$ back to $\mathfrak{g}$*. Every operation on $G$ that depends on infinitesimal behaviour — exponential map, adjoint representation, Cartan decomposition, connection theory — passes through this form. In matrix-group notation, $g^{-1}dg$ is the form one *always* writes down first when starting any calculation on a Lie group.

---

# Examples / Corollaries

**Example ($G = \mathbb{R}^n$, additive).** $\mathfrak{g} = \mathbb{R}^n$ with trivial bracket. Left-translation is $L_g(h) = g + h$, with differential the identity at every point. So $\theta_G(X)|_g = X$ — the Maurer-Cartan form is just $dx = (e_R \otimes dx^R)$, where $e_R$ is the standard basis of $\mathbb{R}^n$. The Maurer-Cartan equation $d\theta + \tfrac{1}{2}[\theta, \theta] = 0$ reduces to $d(dx) = 0$ since $[\,\cdot\,,\,\cdot\,] = 0$ — a trivial identity. Abelian groups give the simplest Maurer-Cartan structure.

**Example ($G = U(1)$).** $\mathfrak{g} = i\mathbb{R}$. Parametrise $g = e^{i\theta}$. Then $g^{-1}dg = e^{-i\theta} \cdot i e^{i\theta}\,d\theta = i\,d\theta$. So $\theta_G = i\,d\theta$, a single $i\mathbb{R}$-valued 1-form. The Maurer-Cartan equation is trivial ($d(d\theta) = 0$, $[\theta_G, \theta_G] = 0$ since abelian).

**Example ($G = SU(2)$).** $\mathfrak{g} = \mathfrak{su}(2) = \{i\sigma_a/2 : a = 1, 2, 3\}$ (anti-Hermitian traceless $2 \times 2$ matrices), with $[i\sigma_a/2, i\sigma_b/2] = -\varepsilon_{abc}\,i\sigma_c/2$ (use $[\sigma_a, \sigma_b] = 2i\varepsilon_{abc}\sigma_c$). Parametrise $g = \cos(\theta/2) - i\sin(\theta/2)(n^a\sigma_a)$ with $n^a n_a = 1$. The Maurer-Cartan form is $\theta_{SU(2)} = (i\sigma_a/2)\otimes\sigma^a$, where the $\sigma^a$ are three left-invariant 1-forms on the group manifold $S^3$. They satisfy $d\sigma^a + \tfrac{1}{2}\varepsilon^a{}_{bc}\sigma^b \wedge \sigma^c = 0$ — the Maurer-Cartan equation in basis form. See [[Ex - The Maurer-Cartan Form on SU(2)]] for the full computation.

**Example ($G = \mathrm{GL}(n; \mathbb{R})$).** $\mathfrak{g} = \mathfrak{gl}(n) = M_n(\mathbb{R})$. In matrix notation, $\theta_G = g^{-1}dg$, an $n \times n$ matrix of 1-forms on $G$. The Maurer-Cartan equation is $d(g^{-1}dg) + (g^{-1}dg) \wedge (g^{-1}dg) = 0$, which expands directly: $d(g^{-1}dg) = -g^{-1}(dg)g^{-1} \wedge dg = -(g^{-1}dg) \wedge (g^{-1}dg)$, so $d\theta_G + \theta_G \wedge \theta_G = 0$. Combined with $\tfrac{1}{2}[\theta_G, \theta_G] = \theta_G \wedge \theta_G$ for matrix groups (1-forms), this gives the desired equation.

**Is NOT an instance:** the form $dg \cdot g^{-1}$ is the *right-invariant* Maurer-Cartan form, not the left-invariant one. They differ by a sign in the structural equation. Mixing them is a common error.

**Is NOT an instance:** the gauge potential $A = s^*\omega$ on the base of a principal bundle is *not* a Maurer-Cartan form in general — it is the pullback of a connection 1-form on the principal bundle. The Maurer-Cartan form is the special case where the connection is the canonical flat connection $\theta_G$ on the trivial bundle $G \to *$.

**Corollary.** The Maurer-Cartan form satisfies $L_h^* \theta_G = \theta_G$ for every $h \in G$ — it is left-invariant (left-translation pulls it back to itself). This is immediate from $L_{g^{-1}} \circ L_h = L_{g^{-1}h}$.

**Corollary.** The Maurer-Cartan form satisfies $R_g^* \theta_G = \mathrm{Ad}_{g^{-1}} \theta_G$ — the equivariance property that makes it a principal connection. Proof: $R_g^* \theta_G(X)|_h = \theta_G((dR_g)_h X)|_{hg} = (dL_{(hg)^{-1}})_{hg}(dR_g)_h X = (dL_{g^{-1}} \circ dL_{h^{-1}} \circ dR_g)_h X = (dL_{g^{-1}} \circ dR_g)_e \theta_G(X)|_h = \mathrm{Ad}_{g^{-1}} \theta_G(X)|_h$, where the last step uses the standard identity $L_{g^{-1}} \circ R_g = \mathrm{Ad}_{g^{-1}}$ at the identity.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that $\theta_G$ takes the left-invariant vector field $X^R$ (with $X^R_e = E_R$) to the constant value $E_R \in \mathfrak{g}$ at every point of $G$; (ii) for $G = \mathrm{GL}(1) = \mathbb{R}^\times$ (multiplicative group), compute $\theta_G = g^{-1}dg = dg/g = d(\log|g|)$, the logarithmic differential; (iii) explain why $\theta_G$ is *not* exact globally on a non-simply-connected group like $U(1)$ — it locally equals $d(\log g)$, but $\log g$ is multivalued, mod $2\pi i$, so the integral $\oint_{S^1} \theta_{U(1)} = 2\pi i \neq 0$ detects the non-trivial $H^1(U(1); \mathbb{R}) = \mathbb{R}$.

---

# Unlocked by This

> [!tip] Maurer-Cartan Equation *(from Gauge Theory III)*
> The Maurer-Cartan form satisfies the universal structural identity $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = 0$, the template for every curvature formula in gauge theory. See [[Thm - Maurer-Cartan Equation]] for the proof and the universal-template interpretation.

> [!tip] Connections as Pullbacks of Maurer-Cartan *(from Gauge Theory III)*
> For the trivial principal bundle $P = M \times G$, every connection 1-form $\omega \in \Omega^1(P; \mathfrak{g})$ can be written as $\omega = \mathrm{pr}_G^* \theta_G + \pi^* A$, where $\mathrm{pr}_G : M \times G \to G$ is the projection, $\pi : M \times G \to M$, and $A$ is the gauge potential in the canonical section $s : M \to M \times G$, $x \mapsto (x, e)$. So every connection on a trivial bundle is the Maurer-Cartan form plus a base-coupling term; for non-trivial bundles, this is still true locally on each trivialising chart, and the gluing data on overlaps is governed by the Maurer-Cartan form composed with transition functions. The bridge to general connection theory.

> [!tip] Cartan Geometry *(from Differential Geometry)*
> A **Cartan geometry** modelled on a homogeneous space $G/H$ is a principal $H$-bundle equipped with a $\mathfrak{g}$-valued 1-form that pointwise reproduces the Maurer-Cartan form of $G$. Cartan's unification of Riemannian, conformal, projective, and parabolic geometries proceeds by varying the choice of $(G, H)$: $(ISO(n), O(n))$ gives Riemannian; $(SO(n+1,1), SO(n) \times O(1,1))$ gives conformal; $(SL(n+1), \text{maximal parabolic})$ gives projective. The Maurer-Cartan equation $d\theta + \tfrac{1}{2}[\theta, \theta] = 0$ holds in the flat (Klein geometry) case; its failure for a general Cartan geometry is the curvature. The Maurer-Cartan form is the universal local model in this entire program.

> [!tip] BCH Formula and Local Structure *(from Lie Theory)*
> The Maurer-Cartan form on $G$ encodes the multiplication map of $G$ near the identity entirely. Specifically, the multiplication $\mu : G \times G \to G$ pulls $\theta_G$ back to $\mu^*\theta_G = \mathrm{Ad}_{g_2^{-1}}\mathrm{pr}_1^*\theta_G + \mathrm{pr}_2^*\theta_G$ on $G \times G$, which together with the unit and inverse axioms determines $\mu$ near the identity. This is the differential-geometric content of the **Baker-Campbell-Hausdorff (BCH) formula** $\log(\exp X \exp Y) = X + Y + \tfrac{1}{2}[X, Y] + \tfrac{1}{12}[X, [X, Y]] + \cdots$, and exhibits the Maurer-Cartan form as the local-structure invariant of the Lie group.
