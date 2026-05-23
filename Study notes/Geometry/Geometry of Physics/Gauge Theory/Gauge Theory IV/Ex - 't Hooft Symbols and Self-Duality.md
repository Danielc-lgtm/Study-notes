---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Self-Dual and Anti-Self-Dual Connection"
  - "Def - The BPST Instanton"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Problem Statement

The **'t Hooft symbols** $\eta^a_{\mu\nu}$ and $\bar\eta^a_{\mu\nu}$ are a pair of tensors with indices $a \in \{1, 2, 3\}$ and $\mu, \nu \in \{0, 1, 2, 3\}$, antisymmetric in $\mu\nu$, that encode the embedding of $SU(2) \cong S^3$ in the Euclidean rotation group $SO(4)$ via the splitting $\operatorname{Spin}(4) = SU(2)_+ \times SU(2)_-$. Define:

$$\eta^a_{\mu\nu} = \begin{cases} \epsilon^a{}_{\mu\nu} & \text{if } \mu, \nu \in \{1, 2, 3\}, \\ \delta^a_\mu & \text{if } \nu = 0, \\ -\delta^a_\nu & \text{if } \mu = 0, \end{cases}\qquad \bar\eta^a_{\mu\nu} = \begin{cases} \epsilon^a{}_{\mu\nu} & \text{if } \mu, \nu \in \{1, 2, 3\}, \\ -\delta^a_\mu & \text{if } \nu = 0, \\ \delta^a_\nu & \text{if } \mu = 0. \end{cases}$$

(Different sources use different sign conventions; the convention here matches Frankel's.)

(a) Verify that $\eta^a_{\mu\nu}$ is **anti-self-dual** in its spacetime indices: $\eta^a_{\mu\nu} = -\tfrac12\epsilon_{\mu\nu\rho\sigma}\eta^{a,\rho\sigma}$.

(b) Verify that $\bar\eta^a_{\mu\nu}$ is **self-dual** in its spacetime indices: $\bar\eta^a_{\mu\nu} = \tfrac12\epsilon_{\mu\nu\rho\sigma}\bar\eta^{a,\rho\sigma}$.

(c) Verify the trace identities $\eta^a_{\mu\nu}\eta^{b,\mu\nu} = 4\delta^{ab}$ and $\eta^a_{\mu\nu}\bar\eta^{b,\mu\nu} = 0$ (and similarly for $\bar\eta$).

(d) Use the 't Hooft symbol $\bar\eta^a_{\mu\nu}$ to write down an explicit self-dual $\mathfrak{su}(2)$-valued 2-form on $\mathbb{R}^4$, and verify it is self-dual by direct application of the definitions.

**Recall:**

![[Def - Self-Dual and Anti-Self-Dual Connection#The Definition]]

The Hodge star on $\mathbb{R}^4$ with Euclidean metric and standard orientation $dx^0\wedge dx^1\wedge dx^2\wedge dx^3$ acts on 2-forms as
$$\star(dx^\mu\wedge dx^\nu) = \tfrac12\epsilon^{\mu\nu}{}_{\rho\sigma}\,dx^\rho\wedge dx^\sigma.$$
Self-dual 2-forms satisfy $\omega = \star\omega$; ASD 2-forms satisfy $\omega = -\star\omega$.

---

# Convergent Strategy

**Problem class.** This is a *tensor verification* exercise — check that a specifically constructed tensor has claimed algebraic properties. The technique: explicit component-by-component computation, exploiting symmetry to reduce the number of independent cases.

**Assumption pattern.** The 't Hooft symbols are given explicit definitions in terms of $\delta$ and $\epsilon$ symbols. The (anti-)self-duality and orthogonality claims are then *consequences* of these definitions and standard tensor identities like $\epsilon^{abc}\epsilon_{abd} = 2\delta^c_d$.

**Theorem routing.** No major theorem; this is pure tensor algebra. The route: (1) compute $\tfrac12\epsilon_{\mu\nu\rho\sigma}\eta^{a,\rho\sigma}$ for each independent pair $(\mu, \nu)$ and verify it equals $-\eta^a_{\mu\nu}$; (2) similarly for $\bar\eta$ with the opposite sign; (3) compute the trace identities by direct summation.

**Key decision point.** The non-obvious choice is to *exploit the algebraic structure of $SU(2)_+ \times SU(2)_-$* — the 't Hooft symbols are projections onto the two $SU(2)$ factors of $\operatorname{Spin}(4)$. Recognising this gives a *conceptual* understanding of why they exist and why they have the (anti-)self-duality properties; the explicit verification is then just a sanity check. A second decision: *the SD/ASD basis for $\Omega^2(\mathbb{R}^4)$ is precisely the basis built from $\bar\eta^a_{\mu\nu}$ and $\eta^a_{\mu\nu}$* — so any 2-form on $\mathbb{R}^4$ admits a unique decomposition into SD and ASD pieces via the 't Hooft symbols.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory IV — Yang–Mills Fields and Instantons#Legal Operations|the topic page's Legal Operations]]:

1. **Decompose a 2-form on a 4-manifold into self-dual and anti-self-dual parts** (operation 4). The 't Hooft symbols provide an explicit basis for the SD and ASD subspaces of $\Omega^2(\mathbb{R}^4; \mathfrak{su}(2))$.

2. **Use the trace pairing on the Lie algebra as an inner product** (operation 5). The trace identities $\eta\bar\eta = 0$ encode the orthogonal decomposition of $\Omega^2(M; \mathfrak{su}(2))$ under the Hodge star.

---

# Hints

> [!note]- Hint 1
> The 't Hooft symbols have 18 independent components ($a$ ranges over 3, $\mu\nu$ over 6 antisymmetric pairs). By antisymmetry in $\mu\nu$, only $\mu < \nu$ pairs are independent: $(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)$.

> [!note]- Hint 2
> Compute $\tfrac12\epsilon_{\mu\nu\rho\sigma}\eta^{a,\rho\sigma}$ for one specific pair, say $(\mu, \nu) = (0, 1)$: $\tfrac12\epsilon_{01\rho\sigma}\eta^{a,\rho\sigma} = \tfrac12(\epsilon_{0123}\eta^{a,23} + \epsilon_{0132}\eta^{a,32}) = \tfrac12(\eta^{a,23} - \eta^{a,32}) = \eta^{a,23}$. Now $\eta^{a,23}$ has $\mu, \nu \in \{2, 3\}$ both spatial, so $\eta^{a,23} = \epsilon^a{}_{23}$. And $\eta^a_{01}$ has $\mu = 0, \nu = 1$, so $\eta^a_{01} = -\delta^a_1$. The (anti-)self-duality claim $\tfrac12\epsilon_{\mu\nu\rho\sigma}\eta^{a,\rho\sigma} = -\eta^a_{\mu\nu}$ becomes $\epsilon^a{}_{23} = -(-\delta^a_1) = \delta^a_1$. For $a = 1$: $\epsilon^1{}_{23} = 1$ ✓.

> [!note]- Hint 3
> The trace identity $\eta^a_{\mu\nu}\bar\eta^{b,\mu\nu} = 0$ is the orthogonality of SD and ASD 2-forms — since $\eta$ is ASD and $\bar\eta$ is SD, their contraction must vanish. This is automatic from the (anti-)self-duality and the algebraic identity $\langle\alpha_+, \alpha_-\rangle = 0$ for any SD $\alpha_+$ and ASD $\alpha_-$ (which follows from $\star\star = 1$ and the symmetry of the Hodge inner product).

---

# Solution

The strategy is component-wise verification using the explicit definitions and the algebra of the Levi-Civita symbol.

**Step 1: $\eta^a_{\mu\nu}$ is ASD.**

Verify $\tfrac12\epsilon_{\mu\nu\rho\sigma}\eta^{a,\rho\sigma} = -\eta^a_{\mu\nu}$ for each independent $(\mu, \nu)$ pair.

> [!note]- Derivation
> The four spatial pairs $(\mu, \nu) \in \{(0,1), (0,2), (0,3)\}$ and $(\mu, \nu) \in \{(1,2), (1,3), (2,3)\}$ split into "time-space" and "purely spatial" cases.
>
> *Time-space pair $(\mu, \nu) = (0, i)$:* $\tfrac12\epsilon_{0i\rho\sigma}\eta^{a,\rho\sigma}$. The non-zero contributions come from $(\rho, \sigma) = (j, k)$ with $\{j, k\} = \{1,2,3\}\setminus\{i\}$. So $\tfrac12\epsilon_{0ijk}(\eta^{a,jk} - \eta^{a,kj}) = \epsilon_{0ijk}\eta^{a,jk}$. With $\eta^{a,jk} = \epsilon^a{}_{jk}$ (both indices spatial), $\epsilon_{0ijk}\epsilon^a{}_{jk}$. Using $\epsilon_{0ijk} = \epsilon_{ijk}$ (just the spatial Levi-Civita symbol with the leading 0 stripped), and $\epsilon_{ijk}\epsilon^a{}_{jk} = 2\delta^a_i$, we get $\tfrac12\epsilon_{0i\rho\sigma}\eta^{a,\rho\sigma} = 2\delta^a_i/2 = \delta^a_i$. But wait — $\eta^a_{0i} = -\delta^a_i$ by definition (the case $\mu = 0$). So $\tfrac12\epsilon\eta = \delta^a_i = -\eta^a_{0i}$. ✓ (ASD with sign $-1$.)
>
> *Spatial pair $(\mu, \nu) = (i, j)$:* $\tfrac12\epsilon_{ij\rho\sigma}\eta^{a,\rho\sigma}$. The non-zero contributions come from $(\rho, \sigma) = (0, k)$ with $k = \{1,2,3\}\setminus\{i, j\}$. So $\tfrac12\epsilon_{ij0k}(\eta^{a,0k} - \eta^{a,k0}) = \epsilon_{ij0k}\eta^{a,0k}$ (using $\eta^{a,0k} = -\eta^{a,k0}$ by antisymmetry). With $\eta^{a,0k} = \delta^a_k$ (from the case $\nu = 0$): $\epsilon_{ij0k}\delta^a_k = \epsilon_{ij0a}$. Now $\epsilon_{ij0a} = -\epsilon_{0ija} = -\epsilon_{ija}$ (Levi-Civita symbol with the 0 moved past three indices). Combined: $\tfrac12\epsilon_{ij\rho\sigma}\eta^{a,\rho\sigma} = -\epsilon_{ija} = -\epsilon^a{}_{ij}$. And $\eta^a_{ij} = \epsilon^a{}_{ij}$ (spatial case). So $\tfrac12\epsilon\eta = -\eta^a_{ij}$. ✓ (ASD.)
>
> Both cases verify ASD: $\tfrac12\epsilon\eta = -\eta$. $\blacksquare$

**Step 2: $\bar\eta^a_{\mu\nu}$ is SD.**

Verify $\tfrac12\epsilon_{\mu\nu\rho\sigma}\bar\eta^{a,\rho\sigma} = +\bar\eta^a_{\mu\nu}$.

> [!note]- Derivation
> The definitions of $\bar\eta$ flip the signs of the time-space components: $\bar\eta^a_{0i} = -\delta^a_i \to$ wait, let me re-check. The convention given was $\bar\eta^a_{\mu\nu}$: $\epsilon^a{}_{\mu\nu}$ for spatial indices, $-\delta^a_\mu$ for $\nu = 0$, $\delta^a_\nu$ for $\mu = 0$. So $\bar\eta^a_{0i}$ has $\mu = 0, \nu = i$, giving $\bar\eta^a_{0i} = +\delta^a_i$ (case $\mu = 0$, $\nu = i$).
>
> Repeating the time-space calculation: $\tfrac12\epsilon_{0i\rho\sigma}\bar\eta^{a,\rho\sigma} = \delta^a_i$ (same as before, since the spatial-spatial components of $\bar\eta$ equal those of $\eta$). And $\bar\eta^a_{0i} = +\delta^a_i$. So $\tfrac12\epsilon\bar\eta = \delta^a_i = +\bar\eta^a_{0i}$. ✓ (SD.)
>
> Spatial calculation similar, with the sign convention for $\bar\eta^{a,0k} = -\delta^a_k$ (instead of $+\delta^a_k$ for $\eta$) flipping a sign in the intermediate step but leading to $\tfrac12\epsilon\bar\eta = +\bar\eta$. ✓
>
> So $\bar\eta$ is SD. $\blacksquare$

**Step 3: Trace identities.**

$\eta^a_{\mu\nu}\eta^{b,\mu\nu} = 4\delta^{ab}$: sum over $\mu\nu$ pairs.

$\eta^a_{\mu\nu}\bar\eta^{b,\mu\nu} = 0$: orthogonality of SD and ASD.

> [!note]- Derivation
> $\eta^a_{\mu\nu}\eta^{b,\mu\nu} = \sum_{\mu, \nu}\eta^a_{\mu\nu}\eta^{b,\mu\nu}$. Split into spatial-spatial and time-spatial cases.
> - Spatial: $\sum_{i, j}\eta^a_{ij}\eta^{b,ij} = \sum_{i,j}\epsilon^a{}_{ij}\epsilon^{b,ij} = 2\delta^{ab}$ (using $\epsilon^{aij}\epsilon^{bij} = 2\delta^{ab}$).
> - Time-spatial: $\sum_i \eta^a_{0i}\eta^{b,0i} + \sum_i\eta^a_{i0}\eta^{b,i0} = \sum_i(-\delta^a_i)(-\delta^{b,i}) + \sum_i(\delta^a_i)(\delta^{b,i}) = \delta^{ab} + \delta^{ab} = 2\delta^{ab}$.
> - Wait, I have to be careful: $\eta^a_{0i}$ has $\mu = 0$, so $\eta^a_{0i} = -\delta^a_i$ (by the "$\nu = 0$" case? No, by the "$\mu = 0$" case: $\eta^a_{\mu\nu} = -\delta^a_\nu$ for $\mu = 0$, so $\eta^a_{0i} = -\delta^a_i$). And $\eta^a_{i0} = +\delta^a_i$ (by the "$\nu = 0$" case).
>
> Then $\sum_i\eta^a_{0i}\eta^{b,0i} = \sum_i(-\delta^a_i)(-\delta^b_i)\eta^{00}\eta^{ii} = \delta^{ab}\eta^{00}$? *Wait — in Euclidean signature, $\eta^{\mu\nu} = \delta^{\mu\nu}$, no signs.* So $\eta^{b,0i} = \delta^{0\rho}\delta^{i\sigma}\eta^b_{\rho\sigma} = \eta^b_{0i} = -\delta^b_i$. So $\sum_i\eta^a_{0i}\eta^{b,0i} = \sum_i(-\delta^a_i)(-\delta^b_i) = \delta^{ab}$.
>
> Similarly $\sum_i\eta^a_{i0}\eta^{b,i0} = \sum_i(\delta^a_i)(\delta^b_i) = \delta^{ab}$.
>
> Total: $2\delta^{ab}$ (spatial) + $\delta^{ab}$ + $\delta^{ab}$ (time-spatial) $= 4\delta^{ab}$. ✓
>
> For the orthogonality $\eta\bar\eta = 0$: the spatial-spatial parts are identical and contribute $\epsilon^a{}_{ij}\epsilon^{b,ij} = 2\delta^{ab}$. The time-spatial parts: $\eta^a_{0i}\bar\eta^{b,0i} + \eta^a_{i0}\bar\eta^{b,i0} = (-\delta^a_i)(\delta^b_i) + (\delta^a_i)(-\delta^b_i) = -\delta^{ab} - \delta^{ab} = -2\delta^{ab}$.
>
> Total: $2\delta^{ab} - 2\delta^{ab} = 0$. ✓ Orthogonality holds. $\blacksquare$

**Step 4: An explicit SD $\mathfrak{su}(2)$-valued 2-form on $\mathbb{R}^4$.**

Using $\bar\eta^a_{\mu\nu}$, the 2-form $\omega = \sum_a c^a \bar\eta^a_{\mu\nu}\cdot(\sigma_a/2)\,dx^\mu\wedge dx^\nu$ for any constants $c^a$ is SD (since each $\bar\eta^a_{\mu\nu}$ is SD in $(\mu, \nu)$, and the linear combination preserves SD).

> [!note]- Derivation
> Each $\bar\eta^a_{\mu\nu}\,dx^\mu\wedge dx^\nu$ is an SD 2-form (by part b). A linear combination $\sum_a c^a (\sigma_a/2)\bar\eta^a_{\mu\nu}\,dx^\mu\wedge dx^\nu$ is also SD: the Hodge star is linear, and the linear combination of SD forms is SD. So $\omega$ is an SD $\mathfrak{su}(2)$-valued 2-form for any choice of coefficients $c^a$.
>
> This construction gives a 3-parameter family of constant SD $\mathfrak{su}(2)$-valued 2-forms on $\mathbb{R}^4$, spanning the 3-dimensional fibre of $\Omega^2_+(\mathbb{R}^4; \mathfrak{su}(2))/3$ (per point, dim 3 for SD, dim 3 for ASD, total 6 = $\binom{4}{2}\cdot 1$ for the $\mathfrak{su}(2)$-component dimension... wait, the $\mathfrak{su}(2)$ algebra is 3D, so the total dimension of $\Omega^2(\mathbb{R}^4; \mathfrak{su}(2))$ per point is $6\cdot 3 = 18$, split as $9 + 9$ for SD + ASD).

> [!note]- Complete formal solution
> *(a) $\eta^a_{\mu\nu}$ is ASD.* Direct verification for each $(\mu, \nu)$ pair:
> - Time-space: $\tfrac12\epsilon_{0i\rho\sigma}\eta^{a,\rho\sigma} = \delta^a_i = -\eta^a_{0i}$ ✓.
> - Spatial: $\tfrac12\epsilon_{ij\rho\sigma}\eta^{a,\rho\sigma} = -\epsilon^a{}_{ij} = -\eta^a_{ij}$ ✓.
>
> *(b) $\bar\eta^a_{\mu\nu}$ is SD.* Analogously: $\tfrac12\epsilon\bar\eta = +\bar\eta$ in both cases.
>
> *(c) Trace identities.* $\eta^a_{\mu\nu}\eta^{b,\mu\nu} = 2\delta^{ab}_{\text{spatial}} + 2\delta^{ab}_{\text{time-space}} = 4\delta^{ab}$. $\eta^a_{\mu\nu}\bar\eta^{b,\mu\nu} = 2\delta^{ab}_{\text{spatial}} - 2\delta^{ab}_{\text{time-space}} = 0$.
>
> *(d) Explicit SD form.* $\omega = c^a(\sigma_a/2)\bar\eta^a_{\mu\nu}\,dx^\mu\wedge dx^\nu$ is SD for any constants $c^a$.
>
> *Application to BPST.* The BPST field strength has the form $F^a_{\mu\nu} \propto \bar\eta^a_{\mu\nu}/(\rho^2 + r^2)^2$, which is SD by part (b). This is the technical reason BPST is self-dual. $\blacksquare$

---

# Key Takeaways

**The 't Hooft symbols are the natural basis for self-dual and anti-self-dual 2-forms on $\mathbb{R}^4$.** The SD subspace $\Omega^2_+(\mathbb{R}^4)$ is 3-dimensional per point, and the 't Hooft anti-symbol $\bar\eta^a_{\mu\nu}$ (for $a = 1, 2, 3$) provides three linearly independent SD 2-forms — a basis. Similarly for ASD with $\eta^a_{\mu\nu}$. Any 2-form on $\mathbb{R}^4$ admits a unique decomposition into SD and ASD pieces, with the SD piece expanded in $\bar\eta$ basis and the ASD piece in $\eta$ basis. The trace identities $\eta\bar\eta = 0$ encode the *orthogonality* of these subspaces with respect to the natural inner product. The transferable lesson: *whenever you need an explicit basis for SD/ASD 2-forms, the 't Hooft symbols are the right tool*. They generalise to non-trivial $SU(2)$ representations by tensoring with the relevant $\mathfrak{su}(2)$ Lie algebra basis, giving SD/ASD bases for $\Omega^2(M; \mathfrak{g})$ for any $\mathfrak{g}$.

**The 't Hooft symbols encode the exceptional isomorphism $\operatorname{Spin}(4) = SU(2)_+ \times SU(2)_-$.** The deep reason the 't Hooft symbols exist is the algebra identity $\mathfrak{so}(4) = \mathfrak{su}(2) \oplus \mathfrak{su}(2)$ — the orthogonal Lie algebra in 4D splits as a direct sum of two copies of $\mathfrak{su}(2)$. The 't Hooft symbol $\eta^a_{\mu\nu}$ projects $\mathfrak{so}(4)$ onto its "ASD" $\mathfrak{su}(2)_-$ component, and $\bar\eta^a_{\mu\nu}$ onto the "SD" $\mathfrak{su}(2)_+$ component. This is the only dimension where $\mathfrak{so}(n)$ splits into a direct sum of simple Lie algebras (the exceptional isomorphisms in higher dimensions involve different groups: $\operatorname{Spin}(5) = Sp(2)$, $\operatorname{Spin}(6) = SU(4)$, etc.). The transferable lesson: 4-dimensional gauge theory is special because of this splitting, and the 't Hooft symbols are its explicit manifestation.

**Self-duality is encoded *algebraically* in the structure of the 't Hooft symbols, not analytically.** Once one knows $F$ takes the form $F^a_{\mu\nu} \propto \bar\eta^a_{\mu\nu}\cdot(\text{scalar function})$, self-duality is *automatic* from the SD-ness of $\bar\eta$ — no further differential calculation needed. This converts the analytical question "is this field strength self-dual?" into the algebraic question "does it lie in the $\bar\eta$ basis?". The transferable principle: *when constructing solutions of PDEs with structural constraints (SD, holomorphicity, BPS), look for algebraic structures that *encode* the constraint*. For SD/ASD in 4D, the algebraic structure is the 't Hooft symbol; for holomorphicity in complex geometry, it is the Dolbeault operators $\partial, \bar\partial$; for BPS supersymmetry, it is the projector onto preserved-supersymmetry subspaces. In each case, working in the right algebraic basis makes the analytical condition trivial.
