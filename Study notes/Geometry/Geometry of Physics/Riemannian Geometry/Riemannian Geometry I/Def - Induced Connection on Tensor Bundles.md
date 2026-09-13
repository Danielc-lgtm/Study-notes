---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Tensor Field on a Manifold"
  - "Def - Cotangent Space and Cotangent Bundle"
tags: [geometry, riemannian-geometry, connections, tensor-bundles]
---

# Notation

$(M, \nabla)$ — a smooth manifold with an affine connection on $TM$. $T^{(r, s)}M = TM^{\otimes r} \otimes T^*M^{\otimes s}$ — the bundle of $(r, s)$-tensors (covariant order $s$, contravariant order $r$). $X, Y, Z$ — vector fields; $\alpha, \beta$ — 1-forms; $T, S$ — tensor fields. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

We have an affine connection $\nabla$ on $TM$, defined to differentiate vector fields ([[Def - Affine Connection on a Vector Bundle]]). But geometry produces many more objects than just vector fields: 1-forms, $(0, 2)$-tensors like the metric $g$, $(1, 2)$-tensors like the torsion, $(0, 4)$-tensors like the Riemann tensor, differential forms in general. To differentiate any of these covariantly, we need a connection on the corresponding tensor bundle.

The natural question: given $\nabla$ on $TM$, is there a *canonical* extension to a connection on every tensor bundle $T^{(r, s)}M$? The answer is yes, and the extension is uniquely characterised by three natural conditions:

1. **$\nabla$ on functions is just $d$:** for $f \in C^\infty(M)$, $\nabla f = df$. This is forced because a function is a $(0, 0)$-tensor and the only natural "derivative" is the differential.

2. **$\nabla$ on $TM$ is the given connection:** for $X \in \mathfrak{X}(M)$, the extension of $\nabla$ to $TM$ is the original $\nabla$. (Tautologically true.)

3. **$\nabla$ is a Leibniz derivation over tensor product:** for tensor fields $T, S$, $\nabla(T \otimes S) = (\nabla T) \otimes S + T \otimes (\nabla S)$. This is the natural compatibility of the connection with the tensor algebra.

4. **$\nabla$ commutes with contractions:** for any contraction $C^a_b : T^{(r, s)}M \to T^{(r-1, s-1)}M$ (a pair-up of one upper and one lower index), $\nabla \circ C = C \circ \nabla$ in the sense $\nabla_X(CT) = C(\nabla_X T)$. Equivalently, taking a covariant derivative and contracting commute. This is the natural compatibility of the connection with the linear-algebraic operation of "pair an upper and a lower index".

These four conditions uniquely determine the extension of $\nabla$ to every tensor bundle. Here is how the determination works for 1-forms (cotangent vectors). Take $\alpha \in \Omega^1(M)$ and any $Y \in \mathfrak{X}(M)$. The contraction $\alpha(Y) = C(\alpha \otimes Y) \in C^\infty(M)$ is a function, so $\nabla_X(\alpha(Y)) = X(\alpha(Y))$ by condition (1). On the other hand, $\nabla_X(\alpha(Y)) = \nabla_X(C(\alpha \otimes Y)) = C(\nabla_X(\alpha \otimes Y)) = C(\nabla_X\alpha \otimes Y + \alpha \otimes \nabla_X Y) = (\nabla_X\alpha)(Y) + \alpha(\nabla_X Y)$ by conditions (3) and (4). Equating:
$$
(\nabla_X\alpha)(Y) = X(\alpha(Y)) - \alpha(\nabla_X Y).
$$
This is the formula for the covariant derivative of a 1-form. It says: the rate of change of $\alpha(Y)$ in the direction of $X$ is the rate at which $\alpha$ itself changes (acting on $Y$) plus the rate at which $Y$ changes (paired with $\alpha$). Rearranging gives the formula above.

The same procedure works for any tensor: write the tensor as a tensor product of vector and covector fields, pair with appropriate dual factors to get a function, apply $d$ on the function side, and isolate the derivative of the tensor. For a $(0, 2)$-tensor $T(Y, Z) = T_{ij}Y^iZ^j$:
$$
(\nabla_X T)(Y, Z) = X(T(Y, Z)) - T(\nabla_X Y, Z) - T(Y, \nabla_X Z).
$$
This is the formula one uses for differentiating the metric: $(\nabla_X g)(Y, Z) = X(g(Y, Z)) - g(\nabla_X Y, Z) - g(Y, \nabla_X Z)$, and the metric-compatibility condition is precisely $\nabla g = 0$.

**Why these axioms and not others?** The Leibniz rule (3) is the only natural way to extend a derivation from a basic case to tensor products — it is what makes the connection respect the *algebra* of tensors. Commutation with contractions (4) is the only natural way to make the connection respect the *duality* of vectors and covectors. Together they force the formulas above; without them, "differentiation of tensors" would be ambiguous, with each contraction picking up a "different" derivative.

**The signs are not arbitrary.** Note the *minus* sign in the 1-form formula $(\nabla_X\alpha)(Y) = X(\alpha(Y)) - \alpha(\nabla_X Y)$. This is forced by the contraction-commutation rule: when you split $\nabla_X(C(\alpha \otimes Y))$ via Leibniz and isolate $(\nabla_X\alpha)(Y)$, the $\alpha(\nabla_X Y)$ term subtracts because it is "the change of $Y$ that $\alpha$ sees", which has already been accounted for separately. The sign pattern generalises: for a $(0, s)$-tensor, every lower index gets a minus sign for the corresponding $\nabla_X$-correction. This is the **dual transformation** of covectors under the connection.

**An important consequence: the induced connection on the metric.** Apply the formula to $g$: $(\nabla_X g)(Y, Z) = X g(Y, Z) - g(\nabla_X Y, Z) - g(Y, \nabla_X Z)$. Setting this to zero gives the [[Def - Metric-Compatible Connection|metric-compatibility]] condition $\nabla g = 0$ in its cleanest form. This is the most useful single application of the induced-connection construction.

---

# The Definition

Let $(M, \nabla)$ be a smooth manifold with an affine connection on $TM$. The **induced connection on tensor bundles** is the unique extension of $\nabla$ to a derivation on the entire tensor algebra of $TM$, characterised by the following properties for all $X \in \mathfrak{X}(M)$:

1. **On functions:** $\nabla_X f = X(f)$ for $f \in C^\infty(M)$.

2. **On vector fields:** $\nabla_X Y$ is the original connection on $TM$.

3. **Leibniz over tensor product:** for any tensor fields $T \in \Gamma(T^{(r_1, s_1)}M)$ and $S \in \Gamma(T^{(r_2, s_2)}M)$,
$$
\nabla_X(T \otimes S) = (\nabla_X T) \otimes S + T \otimes (\nabla_X S).
$$

4. **Commutation with contractions:** for any contraction $C : T^{(r, s)}M \to T^{(r-1, s-1)}M$,
$$
\nabla_X(C(T)) = C(\nabla_X T).
$$

These four conditions uniquely determine $\nabla$ on every tensor bundle.

**Explicit formulas in terms of the components.**

For a **1-form** $\alpha \in \Omega^1(M)$:
$$
(\nabla_X\alpha)(Y) = X(\alpha(Y)) - \alpha(\nabla_X Y), \qquad (\nabla_X\alpha)_k = X^i(\partial_i\alpha_k - \Gamma^j_{ik}\alpha_j).
$$

For a **$(0, 2)$-tensor** $T$:
$$
(\nabla_X T)(Y, Z) = X(T(Y, Z)) - T(\nabla_X Y, Z) - T(Y, \nabla_X Z),
$$
$$
(\nabla_X T)_{kl} = X^i(\partial_i T_{kl} - \Gamma^j_{ik}T_{jl} - \Gamma^j_{il}T_{kj}).
$$

For a **$(1, 1)$-tensor** $A$:
$$
(\nabla_X A)(Y) = \nabla_X(A(Y)) - A(\nabla_X Y), \qquad (\nabla_X A)^k{}_l = X^i(\partial_i A^k{}_l + \Gamma^k_{ij}A^j{}_l - \Gamma^j_{il}A^k{}_j).
$$

**General formula.** For a $(r, s)$-tensor $T$ with components $T^{k_1\cdots k_r}{}_{l_1\cdots l_s}$:
$$
(\nabla_X T)^{k_1\cdots k_r}{}_{l_1\cdots l_s} = X^i\Bigl(\partial_i T^{k_1\cdots k_r}{}_{l_1\cdots l_s} + \sum_a \Gamma^{k_a}_{ij}T^{k_1\cdots j\cdots k_r}{}_{l_1\cdots l_s} - \sum_b \Gamma^j_{il_b}T^{k_1\cdots k_r}{}_{l_1\cdots j\cdots l_s}\Bigr).
$$
Each upper index contributes a $+\Gamma$ correction (because vectors transform with $+\Gamma$); each lower index contributes a $-\Gamma$ correction (because covectors transform with $-\Gamma$).

**Differential forms.** For a $k$-form $\omega$, the induced covariant derivative coincides with the exterior derivative $d$ only for the antisymmetrised expression (specifically: $d\omega = \mathrm{Alt}(\nabla\omega)$, the antisymmetrisation of the covariant derivative); $\nabla\omega$ as a general $(0, k+1)$-tensor is not antisymmetric in all arguments. For torsion-free connections, $\nabla\omega$ in components is related to $d\omega$ by $d\omega = (k+1)\,\mathrm{Alt}(\nabla\omega)$.

---

# Relate to Other Fields / Compression

The compression: **the induced connection on tensor bundles is the unique Leibniz-and-contraction-compatible extension of $\nabla$ on $TM$ to all tensor bundles.** It is the device that makes the metric-compatibility condition writable as $\nabla g = 0$ and that defines covariant derivatives of curvature, torsion, and arbitrary tensor fields — the language in which the second Bianchi identity is most naturally stated.

In **physics**, the induced connection on tensor bundles is what underlies the **covariant divergence** $\nabla_\mu T^{\mu\nu}$ of the energy-momentum tensor — a $(2, 0)$-tensor in general relativity. The conservation law $\nabla_\mu T^{\mu\nu} = 0$ is automatic from the contracted second Bianchi identity for the Einstein tensor $G^{\mu\nu} = R^{\mu\nu} - \tfrac{1}{2}R g^{\mu\nu}$, given the Einstein field equations $G^{\mu\nu} = 8\pi G T^{\mu\nu}$. This is a striking structural feature: the symmetries of the curvature tensor automatically enforce energy-momentum conservation, with no further input.

**True name:** The "true name" of the induced connection is **the connection extended by Leibniz to commute with the tensor algebra and with contractions**. The four axioms (function = $d$, $TM$ given, Leibniz over $\otimes$, commute with $C$) are forced; everything else is derivation. The picture: take any tensor, expand it as a sum of basis products of $e_a$'s and $\sigma^a$'s, differentiate each factor in turn by Leibniz, and read off the result.

---

# Examples / Corollaries

**Example: metric-compatibility in components.** With the induced connection, $\nabla g = 0$ is
$$
\partial_k g_{ij} - \Gamma^l_{ki}g_{lj} - \Gamma^l_{kj}g_{il} = 0,
$$
the **Ricci identity** for the metric. This is the integrability condition that gives the Christoffel formula for the Levi-Civita connection.

**Example: divergence of a vector field.** For $X = X^k\partial_k$, the **divergence** is $\nabla_k X^k = \partial_k X^k + \Gamma^k_{ki}X^i$. Using $\Gamma^k_{ki} = \partial_i \log\sqrt{|g|}$ for the Levi-Civita connection (a standard identity from the Christoffel formula), this becomes $\nabla_k X^k = \tfrac{1}{\sqrt{|g|}}\partial_k(\sqrt{|g|}X^k)$ — the **Voss-Weyl formula** for the divergence on a Riemannian manifold. This is the covariant generalisation of the Euclidean divergence formula.

**Example: covariant Hessian of a function.** For $f \in C^\infty(M)$, $\nabla f = df$ is a 1-form, and $\nabla\nabla f$ is a $(0, 2)$-tensor — the **Hessian** $\mathrm{Hess}(f)$:
$$
\mathrm{Hess}(f)(X, Y) = X(Y(f)) - (\nabla_X Y)(f), \qquad \mathrm{Hess}(f)_{ij} = \partial_i\partial_j f - \Gamma^k_{ij}\partial_k f.
$$
For the Levi-Civita connection $\Gamma^k_{ij}$ is symmetric, so the Hessian is symmetric in $(i, j)$ — corresponding to torsion-freeness. Tracing with the inverse metric gives the **Laplace-Beltrami operator** $\Delta_g f = g^{ij}\mathrm{Hess}(f)_{ij} = g^{ij}\nabla_i\nabla_j f$ — the covariant Laplacian on a Riemannian manifold.

**Example: the covariant derivative of the Riemann curvature tensor.** $R$ is a $(1, 3)$-tensor, so $\nabla R$ is a $(1, 4)$-tensor. Its components are $\nabla_e R^a{}_{bcd}$. The **second Bianchi identity** asserts
$$
\nabla_e R_{abcd} + \nabla_c R_{abde} + \nabla_d R_{abec} = 0
$$
(the cyclic sum over the last three indices vanishes). This is one of the key identities in Riemannian geometry; its contracted form gives the divergence-free property of the Einstein tensor.

**Non-example: $\nabla$ on a tensor by "differentiating components only".** Naively writing $\nabla_X T_{ij} = X^k\partial_k T_{ij}$ does not give the induced connection — it omits the Christoffel corrections from both indices. The correct formula has *two* corrections for a $(0, 2)$-tensor (one for each lower index), with minus signs. The naive expression is not coordinate-invariant: the inhomogeneous Christoffel transformations do not cancel.

**Corollary (the induced connection respects raising and lowering of indices via $g$).** If $\nabla$ is metric-compatible ($\nabla g = 0$), then for any tensor $T$ the operations of raising/lowering indices with $g, g^{-1}$ commute with $\nabla$. For example, if $X^i$ are the components of a vector and $X_i = g_{ij}X^j$ are its lowered components, then $(\nabla X)_i = g_{ij}(\nabla X)^j$ — the covariant derivatives of the raised and lowered versions are related by the same metric. This is why one can "raise and lower indices freely" in tensor calculus on a Riemannian manifold with the Levi-Civita connection.

**Corollary (the antisymmetric part of $\nabla\omega$ is $d\omega$).** For a $k$-form $\omega$ and torsion-free $\nabla$, the antisymmetrisation of $\nabla\omega$ in all arguments equals $(d\omega)/(k+1)$. Equivalently, $d\omega(X_0, \ldots, X_k) = \sum_{i=0}^k (-1)^i (\nabla_{X_i}\omega)(X_0, \ldots, \hat X_i, \ldots, X_k)$ — the **coordinate-free formula for the exterior derivative** in terms of the covariant derivative. This is why the exterior derivative does not "see" the Christoffel symbols: in the symmetric Christoffel sum, the corrections cancel via the antisymmetrisation.

**Corollary (Killing's equation).** A vector field $K$ is a **Killing field** (generates a flow of [[Def - Isometry|isometries]]) iff $\mathcal{L}_K g = 0$. Using the induced-connection formula and $\mathcal{L}_X g = \nabla_X g + g(\nabla X^\flat, \cdot) + g(\cdot, \nabla X^\flat)$ (for metric-compatible $\nabla$, $\mathcal{L}_X g = 2\,\mathrm{Sym}(\nabla X^\flat)$), Killing's equation becomes $\nabla_i K_j + \nabla_j K_i = 0$. So a Killing field has *antisymmetric covariant derivative*. This is a key tool for finding symmetries of a Riemannian manifold.

**Calibration check.** If you can perform the following three computations, you have understood the induced connection on tensor bundles. (i) Derive the formula $(\nabla_X\alpha)(Y) = X(\alpha(Y)) - \alpha(\nabla_X Y)$ for the covariant derivative of a 1-form by applying the four axioms to the contraction $\alpha \otimes Y \to \alpha(Y)$. (ii) Write down the Ricci identity $\nabla g = 0$ in components and verify it is satisfied by the Levi-Civita Christoffel formula. (iii) Show that the Hessian of a function on a Riemannian manifold is symmetric (uses torsion-freeness via the symmetric Christoffel symbols).

---

# Unlocked by This

> [!tip] The Second Bianchi Identity and Einstein's Equations *(from Riemannian Geometry / General Relativity)*
> The **second Bianchi identity** $\nabla_e R_{abcd} + \nabla_c R_{abde} + \nabla_d R_{abec} = 0$ is a differential identity satisfied by the Riemann curvature tensor — derivable from the structural equation $d\Omega + \omega \wedge \Omega - \Omega \wedge \omega = 0$ via the formulas of the induced connection. Its contracted form $\nabla_\mu(R^{\mu\nu} - \tfrac{1}{2}R g^{\mu\nu}) = 0$ — the divergence-free property of the Einstein tensor — is what makes the conservation law $\nabla_\mu T^{\mu\nu} = 0$ automatic in general relativity, given the Einstein field equations. See [[Riemannian Geometry III — Riemann Curvature and Topology]] and [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] The Laplace-Beltrami Operator and Hodge Theory *(from Riemannian Geometry / Hodge Theory)*
> The Laplace-Beltrami operator on functions is $\Delta_g f = g^{ij}\nabla_i\nabla_j f = \tfrac{1}{\sqrt{|g|}}\partial_i(\sqrt{|g|}g^{ij}\partial_j f)$, the natural generalisation of the Euclidean Laplacian. It extends to differential forms via the **Hodge Laplacian** $\Delta = d\delta + \delta d$, with $\delta$ the codifferential. **Harmonic forms** ($\Delta\omega = 0$) on a compact oriented Riemannian manifold are in bijection with the de Rham cohomology classes — the **Hodge decomposition theorem**. This is the analytic/PDE side of the de Rham theorem and the gateway to elliptic theory on manifolds. Full development in [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

> [!tip] Yang-Mills Equations for Connections on Vector Bundles *(from Gauge Theory)*
> The induced connection on $\mathrm{End}(E)$ (for $E$ a vector bundle with connection) acts on the curvature 2-form $F \in \Omega^2(M; \mathrm{End}\,E)$, and the **Yang-Mills equations** $\nabla\star F = 0$ are a PDE on connections. The variational characterisation: $\nabla\star F = 0$ are the Euler-Lagrange equations of the Yang-Mills action $S_{\mathrm{YM}} = \tfrac{1}{2}\int\mathrm{tr}(F \wedge \star F)$. The full theory, including self-dual and anti-self-dual solutions (instantons), is the content of [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]].
