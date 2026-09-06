---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Cotangent Space and Cotangent Bundle"
  - "Thm - Vector Bundle Construction Lemma"
  - "Def - Transition Function of a Vector Bundle"
  - "Def - The Tangent Bundle"
tags: [geometry, differential-geometry, cotangent, construction]
---

# Problem Statement

Let $M$ be a smooth $n$-manifold. Construct the cotangent bundle $T^*M$ as a smooth rank-$n$ vector bundle over $M$ by applying the [[Thm - Vector Bundle Construction Lemma|vector bundle construction lemma]] to the following data:

- The open cover $\{U_\alpha\}$ of $M$ by coordinate charts $(U_\alpha, \varphi_\alpha)$ from a smooth atlas.
- The fibre at $p \in M$: $T_p^*M = (T_pM)^*$, the dual of the tangent space.
- The candidate trivializations $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^n$, $\Phi_\alpha(\omega_i dx^i_\alpha|_p) = (p, \omega_1, \dots, \omega_n)$, where $(dx^1_\alpha, \dots, dx^n_\alpha)$ is the coordinate coframe on $U_\alpha$.

Explicitly:
(a) Compute the transition function $\tau_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathrm{GL}(n, \mathbb{R})$ between two such trivializations.
(b) Verify the cocycle condition.
(c) Apply the construction lemma to conclude $T^*M$ is a smooth rank-$n$ vector bundle.

**Recall:**

$$\text{Tangent transition functions: } J_{\alpha\beta} = (\partial x^j_\alpha / \partial x^i_\beta)_{j,i} \in \mathrm{GL}(n, \mathbb{R}).$$

The [[Def - Dual Basis|dual basis]] under change of basis transforms by the inverse transpose. The fibrewise dual functor on vector bundles inherits transitions by inverse transpose.

For the [[Thm - Vector Bundle Construction Lemma|construction lemma]]: open cover, fibres of constant [[Def - Dimension|dimension]], candidate trivializations (bijective, fibrewise linear), smooth transition functions satisfying the cocycle $\tau_{\alpha\gamma} = \tau_{\alpha\beta} \tau_{\beta\gamma}$ — these data assemble into a unique smooth rank-$k$ vector bundle.

---

# Convergent Strategy

**Problem class:** Constructing a vector bundle from cocycle data. The construction lemma is the engine — the actual work is identifying the right transition functions and verifying the cocycle.

**Assumption pattern:** $M$ is given as a smooth manifold with a smooth atlas. The candidate fibres are the dual spaces $T_p^*M$. The candidate trivializations come from the coordinate coframe. The key step is to compute how the trivializations differ on overlaps — i.e., the transition functions.

**Theorem routing:** Use the linear-algebraic fact that dual bases transform by inverse transpose ([[Def - Dual Basis]]) to compute the transitions. Verify the cocycle by the chain rule (which gives the cocycle on $TM$) combined with the algebra of inverse transposes $(AB)^{-T} = B^{-T} A^{-T}$ (which gives the cocycle on $T^*M$). Apply the [[Thm - Vector Bundle Construction Lemma]].

**Key decision point:** The decisive step is computing the transition function from the dual-basis transformation. The order of indices and the placement of "inverse" vs "transpose" can easily get muddled; the cleanest computation goes through the dual-basis identity $dx^i_\alpha = (\partial x^i_\alpha / \partial x^j_\beta) dx^j_\beta$.

---

# Legal Operations Used

1. **Operation 10 from the topic page (take the dual bundle to flip variance).** The cotangent bundle is the dual of the tangent bundle, with inverse-transpose-Jacobian transitions.

2. **Operation 3 from the topic page (apply the vector-bundle construction lemma).** This is the engine of the construction.

3. **Operation 8 from the topic page (verify the cocycle condition).** The chain rule on Jacobians plus the algebra of inverse transposes verifies the cocycle for $T^*M$.

4. **Operation 2 from the topic page (read off transition functions to change trivialization).** The transition function from the coordinate-coframe trivialization in chart $\alpha$ to that in chart $\beta$ is the dual basis change of basis matrix.

---

# Hints

> [!note]- Hint 1
> Start by recalling how the coordinate frame $(\partial/\partial x^i_\alpha)$ transforms between two charts. On the overlap, $\partial/\partial x^i_\alpha = (\partial x^j_\beta/\partial x^i_\alpha) \partial/\partial x^j_\beta$ — the Jacobian transformation.

> [!note]- Hint 2
> Apply the dual basis identity ([[Def - Dual Basis]]): the dual bases transform by the inverse transpose. Compute $dx^i_\alpha$ in terms of $dx^j_\beta$ using the inverse Jacobian.

> [!note]- Hint 3
> The transition function $\tau_{\beta\alpha}$ acts on the components of a covector. If $\omega = \omega^\alpha_i dx^i_\alpha = \omega^\beta_j dx^j_\beta$, then $\omega^\beta_j = (\partial x^i_\alpha/\partial x^j_\beta) \omega^\alpha_i$. The matrix is the inverse transpose of the Jacobian.

> [!note]- Hint 4
> Fix the convention $J_{\beta\alpha}=D(x_\beta\circ x_\alpha^{-1})$. The chain rule gives $J_{\gamma\alpha}=J_{\gamma\beta}J_{\beta\alpha}$, and $(AB)^{-T}=A^{-T}B^{-T}$. Hence the dual transitions satisfy the cocycle in the same displayed order.

---

# Solution

**Plan:** Compute the dual-basis transformation under chart change to identify the transition function as the inverse-transpose Jacobian. Verify the cocycle from the chain rule on Jacobians combined with the algebra of inverse transposes. Apply the construction lemma.

**Step 1: Coordinate frame transformation under chart change.**

> [!note]- Derivation
> For two coordinate charts $(U_\alpha, x^i_\alpha)$ and $(U_\beta, x^j_\beta)$ on $M$ with overlap, the tangent space at $p \in U_\alpha \cap U_\beta$ has two bases: $\{\partial/\partial x^i_\alpha|_p\}$ and $\{\partial/\partial x^j_\beta|_p\}$. The chain rule gives
> $$\frac{\partial}{\partial x^i_\alpha}\bigg|_p = \frac{\partial x^j_\beta}{\partial x^i_\alpha}(p) \cdot \frac{\partial}{\partial x^j_\beta}\bigg|_p.$$
> The Jacobian matrix is $J_{\beta\alpha}(p) := (\partial x^j_\beta / \partial x^i_\alpha(p))_{j, i} \in \mathrm{GL}(n, \mathbb{R})$.

**Step 2: Dual basis transformation by inverse transpose.**

> [!note]- Derivation
> The dual basis $(dx^j_\beta)$ to $(\partial/\partial x^i_\beta)$ satisfies $dx^j_\beta(\partial/\partial x^i_\beta) = \delta^j_i$. We want to express $dx^i_\alpha$ in terms of $dx^j_\beta$.
>
> By [[Def - Dual Basis]] applied to the change of basis at the tangent level: if vectors transform by $A$, then dual basis elements transform by $A^{-1}$ (in a specific way). Concretely, the dual basis $dx^i_\alpha$ pairs with $\partial/\partial x^i_\alpha$ to give $\delta^i_j$. Using the chain-rule expansion:
> $$dx^i_\alpha\left( \frac{\partial}{\partial x^j_\beta} \right) = dx^i_\alpha \left( \frac{\partial x^k_\alpha}{\partial x^j_\beta} \frac{\partial}{\partial x^k_\alpha} \right) = \frac{\partial x^k_\alpha}{\partial x^j_\beta} \delta^i_k = \frac{\partial x^i_\alpha}{\partial x^j_\beta}.$$
> So $dx^i_\alpha$ has the expansion $dx^i_\alpha = \frac{\partial x^i_\alpha}{\partial x^j_\beta} dx^j_\beta$, with matrix $(\partial x^i_\alpha / \partial x^j_\beta) = J_{\beta\alpha}^{-1}$ — the inverse Jacobian (viewed appropriately).

**Step 3: Covector components transform by inverse-transpose Jacobian.**

> [!note]- Derivation
> For a covector $\omega \in T_p^*M$ with two expressions $\omega = \omega^\alpha_i dx^i_\alpha = \omega^\beta_j dx^j_\beta$, substitute Step 2:
> $$\omega = \omega^\alpha_i \cdot \frac{\partial x^i_\alpha}{\partial x^j_\beta} dx^j_\beta.$$
> Equating coefficients of $dx^j_\beta$: $\omega^\beta_j = \omega^\alpha_i \cdot \partial x^i_\alpha / \partial x^j_\beta$. As a column-vector relation, $\omega^\beta = (\partial x^i_\alpha / \partial x^j_\beta)^T \omega^\alpha$, where the transpose flips the index roles for matrix multiplication.
>
> The transition function for the cotangent bundle's trivializations is therefore $\tau_{\beta\alpha}(p) := (\partial x^i_\alpha / \partial x^j_\beta(p))^T$ — the transpose of the inverse Jacobian, equivalently the inverse transpose of $J_{\beta\alpha}$: $\tau_{\beta\alpha} = J_{\beta\alpha}^{-T}$.

**Step 4: Verify the cocycle condition.**

> [!note]- Derivation
> The chain rule on $M$: $J_{\gamma\alpha} = J_{\gamma\beta} J_{\beta\alpha}$ on the triple overlap (Jacobian of $\varphi_\gamma \circ \varphi_\alpha^{-1} = (\varphi_\gamma \circ \varphi_\beta^{-1}) \circ (\varphi_\beta \circ \varphi_\alpha^{-1})$ is the product of the Jacobians of the factors).
>
> Inverse-transpose: $J_{\gamma\alpha}^{-T} = (J_{\gamma\beta} J_{\beta\alpha})^{-T}$. Using $(AB)^{-T} = A^{-T} B^{-T}$ — let's verify: $(AB)^{-1} = B^{-1} A^{-1}$, then transposing: $((AB)^{-1})^T = (B^{-1} A^{-1})^T = (A^{-1})^T (B^{-1})^T = A^{-T} B^{-T}$. So $(AB)^{-T} = A^{-T} B^{-T}$.
>
> Therefore $J_{\gamma\alpha}^{-T} = J_{\gamma\beta}^{-T} J_{\beta\alpha}^{-T}$, i.e., $\tau_{\gamma\alpha} = \tau_{\gamma\beta} \tau_{\beta\alpha}$. The cocycle condition holds.

**Step 5: Verify smoothness.**

> [!note]- Derivation
> $J_{\beta\alpha}$ is the Jacobian of the smooth chart transition $\varphi_\beta \circ \varphi_\alpha^{-1}$, so it is smooth on $\varphi_\alpha(U_\alpha \cap U_\beta) \subseteq \mathbb{R}^n$, and pulled back to $U_\alpha \cap U_\beta \subseteq M$ it remains smooth. Matrix inversion is smooth on $\mathrm{GL}(n, \mathbb{R})$ by Cramer's rule. Matrix transposition is smooth (linear, hence $C^\infty$). So $\tau_{\beta\alpha} = J_{\beta\alpha}^{-T}$ is smooth on $U_\alpha \cap U_\beta$.

**Step 6: Apply the construction lemma.**

> [!note]- Derivation
> The data satisfies the hypotheses of [[Thm - Vector Bundle Construction Lemma]]:
> - Open cover $\{U_\alpha\}$ of $M$ (the smooth atlas).
> - Fibres $T_p^*M$ of constant dimension $n$.
> - Bijective fibrewise-linear trivializations $\Phi_\alpha$.
> - Smooth transition functions $\tau_{\beta\alpha} \in \mathrm{GL}(n, \mathbb{R})$ satisfying the cocycle.
>
> The lemma provides $T^*M$ a unique smooth rank-$n$ vector bundle structure over $M$, with the $\Phi_\alpha$ as smooth local trivializations and the coordinate covector fields $dx^i_\alpha$ as smooth local sections.

> [!note]- Complete formal solution
> **Setup.** Let $M$ be a smooth $n$-manifold with smooth atlas $\{(U_\alpha, \varphi_\alpha)\}$, coordinates $x^i_\alpha$. Fibres $T_p^*M = (T_pM)^*$. Candidate trivializations $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^n$, $\Phi_\alpha(\omega_i dx^i_\alpha|_p) = (p, \omega_1, \dots, \omega_n)$.
>
> **Step 1: Coordinate basis transformation on $TM$.** $\partial/\partial x^i_\alpha = (\partial x^j_\beta / \partial x^i_\alpha) \partial/\partial x^j_\beta$ (chain rule), with Jacobian matrix $J_{\beta\alpha} \in \mathrm{GL}(n, \mathbb{R})$, $J_{\beta\alpha} = (\partial x^j_\beta / \partial x^i_\alpha)_{j, i}$.
>
> **Step 2: Dual basis transformation on $T^*M$.** Pair $dx^i_\alpha$ with the chain-rule expansion of $\partial/\partial x^j_\beta$ via the basis $\partial/\partial x^k_\alpha$. Pairing gives $dx^i_\alpha(\partial/\partial x^j_\beta) = \partial x^i_\alpha / \partial x^j_\beta$, so $dx^i_\alpha = (\partial x^i_\alpha / \partial x^j_\beta) dx^j_\beta$.
>
> **Step 3: Transition function.** For $\omega = \omega^\alpha_i dx^i_\alpha = \omega^\beta_j dx^j_\beta$, substituting Step 2 gives $\omega^\beta_j = (\partial x^i_\alpha / \partial x^j_\beta) \omega^\alpha_i$. The transformation matrix on the column $\omega$ is $\tau_{\beta\alpha} := J_{\beta\alpha}^{-T}$, the inverse transpose of the tangent Jacobian.
>
> **Step 4: Cocycle.** On the triple overlap, the chain rule gives $J_{\gamma\alpha} = J_{\gamma\beta} J_{\beta\alpha}$. Inverse-transposing and using $(AB)^{-T} = A^{-T} B^{-T}$ (verified by $(AB)^{-1} = B^{-1}A^{-1}$, then transposing), $J_{\gamma\alpha}^{-T} = J_{\gamma\beta}^{-T} J_{\beta\alpha}^{-T}$, i.e., $\tau_{\gamma\alpha} = \tau_{\gamma\beta} \tau_{\beta\alpha}$.
>
> **Step 5: Smoothness.** $J_{\beta\alpha}$ smooth (Jacobian of smooth chart transition); matrix inverse smooth on $\mathrm{GL}(n, \mathbb{R})$ (Cramer); matrix transpose smooth (linear). So $\tau_{\beta\alpha}$ smooth.
>
> **Step 6: Construction lemma.** The data — open cover, constant-dimension fibres, bijective fibrewise-linear trivializations, smooth cocycle in $\mathrm{GL}(n, \mathbb{R})$ — satisfies the hypotheses of [[Thm - Vector Bundle Construction Lemma]]. The lemma gives the unique smooth rank-$n$ vector bundle structure on $T^*M$ with the prescribed trivializations.
> $\qquad\blacksquare$

---

# Key Takeaways

**The cotangent bundle's transition functions are inverse-transpose Jacobians — the algebraic source of "contravariance" of covectors.** Vector components transform with the Jacobian, covector components transform with its inverse transpose, and these together make the pairing $\omega(v)$ invariant. The "contravariance" of covectors is exactly the appearance of inverse transposes. This pattern recurs for every dual or co-bundle construction: tensors of mixed type, exterior powers, etc., all involve inverse-transpose Jacobians for each "lower index". The mnemonic: upper indices transform with $J$, lower indices with $J^{-T}$.

**The construction lemma is the universal tool — every new bundle of multilinear-algebraic origin uses it.** The cotangent bundle is constructed exactly this way; so are tensor bundles, form bundles, jet bundles, symbol bundles, and more. The construction is uniform: identify the fibres (a multilinear-algebra construction), identify the transition functions (the chain-rule version of the multilinear construction), verify the cocycle (a chain-rule manipulation), apply the lemma. The lemma packages the manifold-structure construction so that one need only specify the multilinear data.

**Verifying the cocycle reduces to the chain rule plus algebra of matrix operations.** Once $J_{\gamma\alpha} = J_{\gamma\beta} J_{\beta\alpha}$ on triple overlaps is established (the chain rule for chart transitions), all derived bundles have their cocycles guaranteed by manipulating $J$ — inverse-transposing for duals, tensoring for tensor products, etc. The cocycle verification is essentially algebraic once the underlying chain rule is in place.

**The inverse-transpose appearance distinguishes the cotangent bundle from the tangent bundle.** Although $TM$ and $T^*M$ are non-canonically isomorphic over $M$ (both rank-$n$), the canonical structures differ: their transition functions are inverses of each other (after transposition). This is the structural source of the distinction "vectors push forward, covectors pull back": pushforward requires inverting the differential, pullback uses the differential directly. A Riemannian metric $g$ on $M$ provides the canonical isomorphism $TM \cong T^*M$ via the musical isomorphism $\flat : v \mapsto g(v, \cdot)$; without $g$, no canonical identification exists.
