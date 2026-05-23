---
type: theorem
subject: hodge-theory
prereqs:
  - "Def - The Codifferential"
  - "Def - The L2 Inner Product on Differential Forms"
  - "Def - Exterior Derivative on a Manifold"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, hodge-theory, differential-forms]
---

# Notation

$(M, g)$ is a smooth oriented Riemannian $n$-manifold. The exterior derivative is $d : \Omega^k \to \Omega^{k+1}$; the codifferential is $\delta = (-1)^{n(k+1) + 1}\star d\star : \Omega^k \to \Omega^{k-1}$; the $L^2$ inner product is $\langle\cdot, \cdot\rangle_{L^2} = \int_M\langle\cdot,\cdot\rangle_g\operatorname{vol}_n$. We write $\partial M$ for the boundary of $M$ (empty when $M$ is closed); $i : \partial M \hookrightarrow M$ for the inclusion. The full notation registry is in [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

---

# Statement

> **Theorem (Codifferential is the $L^2$-adjoint of $d$ on closed manifolds).** Let $(M, g)$ be a closed oriented Riemannian $n$-manifold. For any $\alpha \in \Omega^{k-1}(M)$ and $\beta \in \Omega^k(M)$,
> $$\langle d\alpha, \beta\rangle_{L^2} = \langle\alpha, \delta\beta\rangle_{L^2}.$$
> Equivalently, $d$ and $\delta$ are formal adjoints of each other with respect to the $L^2$ inner product on differential forms.

> **Corollary (Manifolds with boundary).** On a compact oriented Riemannian manifold with boundary $\partial M$, the same calculation gives
> $$\langle d\alpha, \beta\rangle_{L^2} - \langle\alpha, \delta\beta\rangle_{L^2} = \int_{\partial M}\alpha \wedge \star\beta.$$
> The boundary term vanishes if $\alpha$ vanishes on $\partial M$ (tangential boundary condition on $\alpha$) or if $\star\beta$ vanishes on $\partial M$ (normal boundary condition on $\beta$).

---

# Motivation

The theorem is the working tool that makes the entire $L^2$-theory of Hodge work. It says: integration by parts on forms — moving the derivative from one form onto another — produces no boundary term on a closed Riemannian manifold, and the operator that "absorbs" the moved derivative is exactly $\delta = \pm\star d\star$. The [[Def - Hodge Laplacian|Hodge Laplacian]] $\Delta = d\delta + \delta d$ is then self-adjoint and nonnegative; the Hodge decomposition is an orthogonal direct sum; harmonic forms are the orthogonal complement of exact-plus-coexact forms — every structural result downstream uses this single adjointness.

The result is also the reason why the [[Def - The Codifferential|codifferential]] is defined the way it is. The definition $\delta = (-1)^{n(k+1)+1}\star d\star$ looks ad hoc, but it is in fact the *unique* operator on $\Omega^{k-1}$ (sending $\Omega^k$ to $\Omega^{k-1}$) that makes $\langle d\alpha, \beta\rangle = \langle\alpha, \delta\beta\rangle$ hold without a sign or boundary term on a closed manifold. The peculiar sign convention is the price of this adjointness — it is what tracks how the wedge product, the double-star, and Stokes' theorem combine to produce a single clean identity.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: a closed oriented Riemannian manifold and forms of complementary degrees ($k - 1$ and $k$). Several non-obvious sources lead to the conditions for this theorem.

The most common source is **a variational problem on forms**. Property $B$: a functional $F(\omega) = \int_M L(\omega, d\omega)\operatorname{vol}_n$ to be minimized over forms in some class. The bridge to the adjoint theorem is integration by parts in the Euler–Lagrange equation: $0 = \delta F/\delta\omega$ involves $\int_M d\alpha\wedge(\text{stuff})$ which, by adjointness, equals $\int_M\alpha\wedge\delta(\text{stuff})$, exposing the variational equation in the cleanest form. Example: minimizing $\|\omega\|^2$ over closed forms in a cohomology class — the Euler–Lagrange equation is $\delta\omega = 0$ ("coclosed"), derived precisely by the adjoint theorem.

A second source is **a PDE of Laplacian type involving $d$**. Property $B$: an equation like $d\beta = \rho$ to be solved. The bridge is the adjoint identity: $\langle\rho, \alpha\rangle = \langle d\beta, \alpha\rangle = \langle\beta, \delta\alpha\rangle$ for any $\alpha$. So the existence of a solution requires $\langle\rho, \alpha\rangle = 0$ for all $\alpha$ in the kernel of $\delta$ on $\Omega^k$ — i.e., $\rho$ must be orthogonal to coclosed forms. This is the **Fredholm alternative**, derived from adjointness.

A third source is **a Stokes' theorem application that requires "moving a $d$ around"**. Property $B$: an integral of a derivative one wants to convert to a non-derivative form. The bridge is the adjoint identity used "in reverse": $\int_M d\alpha\wedge\beta = \int_M\alpha\wedge\delta\beta$ on a closed manifold (after applying $\star$ to convert the wedge into the inner product). Example: in the proof of the Hodge decomposition, decomposing $\Omega^k$ requires showing that the image of $d$ is exactly the orthogonal complement of coclosed forms — adjointness is the bridge.

**Targets (Output Amplification)**

The conclusion is the adjoint identity $\langle d\alpha, \beta\rangle = \langle\alpha, \delta\beta\rangle$. Combined with other facts, this produces several powerful results.

The most powerful combination is **adjoint identity plus self-adjointness of $\Delta$ on a closed manifold gives the kernel-image decomposition**. The adjoint identity $\langle d\alpha, \beta\rangle = \langle\alpha, \delta\beta\rangle$ together with $\Delta = d\delta + \delta d$ self-adjoint gives, for any $\omega$: $\langle\Delta\omega, \omega\rangle = \|d\omega\|^2 + \|\delta\omega\|^2 \geq 0$, so $\Delta\omega = 0$ iff $d\omega = 0$ and $\delta\omega = 0$. This is the structural reason for the **harmonic = closed-and-coclosed** equivalence on closed manifolds.

A second combination is **adjoint identity plus Stokes' theorem gives the boundary correction**. On a manifold with boundary, the analogous calculation produces $\langle d\alpha, \beta\rangle - \langle\alpha, \delta\beta\rangle = \int_{\partial M}\alpha\wedge\star\beta$. This is the **Green's identity** for forms — the analog of Green's $\int_M(\nabla^2 u\cdot v - u\cdot\nabla^2 v) = \int_{\partial M}(v\nabla u - u\nabla v)\cdot\hat n$ for scalar functions. The boundary term controls the difference between adjointness in the closed-manifold case and the bounded-domain case, and is the basis for boundary-value Hodge theory.

A third combination is **adjoint identity plus orthogonality structure**: $\langle d\alpha, \beta\rangle = 0$ for all $\alpha$ iff $\delta\beta = 0$, equivalently $\beta\perp d\Omega^{k-1}$ iff $\beta$ is coclosed. Symmetrically, $\langle\alpha,\delta\gamma\rangle = 0$ for all $\gamma$ iff $d\alpha = 0$, equivalently $\alpha\perp\delta\Omega^{k+1}$ iff $\alpha$ is closed. So the orthogonal complement of exact forms is coclosed forms, and vice versa. This is the **algebraic skeleton of the Hodge decomposition**: $\Omega^k = \mathcal{H}^k \oplus d\Omega^{k-1}\oplus\delta\Omega^{k+1}$ is encoded in the adjoint identity.

A fourth combination is **adjoint identity plus characterization of harmonic forms**: a form $\omega$ is harmonic iff $\omega\perp d\Omega^{k-1}\oplus\delta\Omega^{k+1}$, the orthogonal complement of exact-plus-coexact. The proof: $\omega$ harmonic iff $d\omega = 0$ and $\delta\omega = 0$ iff $\langle\omega, d\alpha\rangle = 0$ and $\langle\omega,\delta\gamma\rangle = 0$ for all $\alpha,\gamma$ iff $\omega\perp d\Omega^{k-1}$ and $\omega\perp\delta\Omega^{k+1}$. This characterization is what makes the harmonic projection in the Hodge decomposition equivalent to orthogonal projection in $L^2$ onto the kernel of $\Delta$.

---

# Why Is It True

The intuition is a single picture: **integration by parts in the form of $d$ produces a boundary term, and the boundary term vanishes on a closed manifold**.

Specifically, the Leibniz rule for $d$ on the wedge product $\alpha\wedge\star\beta$ (with $\alpha \in \Omega^{k-1}$, $\star\beta \in \Omega^{n-k}$) gives
$$d(\alpha\wedge\star\beta) = d\alpha\wedge\star\beta + (-1)^{k-1}\alpha\wedge d\star\beta.$$
The left side is a "total derivative" — it is $d$ of something. Stokes' theorem says
$$\int_M d(\alpha\wedge\star\beta) = \int_{\partial M}\alpha\wedge\star\beta.$$
On a closed manifold ($\partial M = \emptyset$), the boundary integral vanishes, so
$$0 = \int_M d\alpha\wedge\star\beta + (-1)^{k-1}\int_M\alpha\wedge d\star\beta.$$
The first term is $\langle d\alpha,\beta\rangle$ by the defining identity of $\star$. The second term needs more work: $\alpha\wedge d\star\beta$ should be rewritten as $\alpha\wedge\star(\star^{-1}d\star\beta) = \langle\alpha, \star^{-1}d\star\beta\rangle_g\operatorname{vol}_n$. By the double-star formula on $(k-1)$-forms in degree $n - k + 1 =$ shifted appropriately, $\star^{-1} = (-1)^{(k-1)(n-k+1)+s}\star$. So
$$(-1)^{k-1}\int_M\alpha\wedge d\star\beta = (-1)^{k-1}(-1)^{(k-1)(n-k+1)+s}\langle\alpha,\star d\star\beta\rangle = (\text{sign})\langle\alpha, \star d\star\beta\rangle.$$
The total sign combines to $(-1)^{n(k+1)+1}$ in Riemannian signature ($s = 0$ — the calculation gets messier with $s > 0$). So the equation becomes
$$\langle d\alpha,\beta\rangle = (-1)^{n(k+1)}\langle\alpha,\star d\star\beta\rangle = -(-1)^{n(k+1)+1}\langle\alpha,\star d\star\beta\rangle = \langle\alpha, \delta\beta\rangle$$
using $\delta = (-1)^{n(k+1)+1}\star d\star$. The signs all conspire to give the clean adjoint identity.

**The one-line mechanism summary:** **the adjoint identity is Stokes' theorem applied to the Leibniz rule for $d$ on the wedge $\alpha\wedge\star\beta$, with the boundary term killed by closedness of $M$ and the sign tracking organized by the definition $\delta = \pm\star d\star$.**

The deeper reason is structural: on a closed Riemannian manifold, every operation that produces a "total derivative" $d(\text{something})$ contributes nothing to the integral, by Stokes. So the difference between $d$ and its adjoint $\delta$ is exactly the boundary information — and that information vanishes on a closed manifold, making them adjoints. On a manifold with boundary, the boundary information is exactly the surface integral $\int_{\partial M}\alpha\wedge\star\beta$, recovering the boundary-corrected version.

---

# What Makes This Hard

The proof itself is short but the sign tracking is exquisite. Most errors come from one of three places: **the sign in the graded Leibniz rule for $d$** on the wedge product (which depends on the degree of $\alpha$); **the sign from the double-star formula** when converting $\alpha\wedge d\star\beta$ back into an inner product (which depends on degrees and signature); and **the conventional sign in the definition of $\delta$** (which Frankel, Lee, and Warner all use the same way but some physics texts negate).

The most common error: **conflating the sign in the Riemannian and pseudo-Riemannian cases**. The Riemannian formula $\delta = (-1)^{n(k+1)+1}\star d\star$ has an additional $(-1)^s$ in the pseudo-Riemannian case from the double-star formula. On Lorentzian $4$D and $1$-forms (so $k = 1$, $n = 4$, $s = 1$), the sign becomes $(-1)^{4\cdot 2 + 1}\cdot(-1) = (-1)^9\cdot(-1) = +1$, while the Riemannian formula at the same degrees gives $(-1)^{4\cdot 2 + 1} = -1$. The two signs differ by exactly the $(-1)^s$ factor from the metric signature.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The adjoint identity is Stokes' theorem applied to the graded Leibniz rule for $d$ on $\alpha\wedge\star\beta$. The boundary term vanishes on a closed manifold, leaving an identity that, after sign-tracking via the double-star formula, expresses $\delta$ in terms of $\star d\star$ and gives the adjoint identity.

**Subgoal decomposition:**

1. **Apply the graded Leibniz rule to $d(\alpha\wedge\star\beta)$.** Expand using $d(\omega\wedge\eta) = d\omega\wedge\eta + (-1)^{\deg\omega}\omega\wedge d\eta$.
   - *Hint:* $\alpha$ has degree $k - 1$, $\star\beta$ has degree $n - k$, total degree of wedge is $n - 1$, $d$ raises to $n$.
   - *Why needed:* Produces the two terms whose sum is a total derivative.

2. **Integrate over $M$ and apply Stokes' theorem.** $\int_M d(\alpha\wedge\star\beta) = \int_{\partial M}\alpha\wedge\star\beta$.
   - *Hint:* On a closed manifold $\partial M = \emptyset$, so the boundary integral is $0$.
   - *Why needed:* Converts the wedge derivative into a boundary term that vanishes on closed manifolds.

3. **Identify the first term as $\langle d\alpha, \beta\rangle$.**
   - *Hint:* $\int_M d\alpha\wedge\star\beta = \langle d\alpha, \beta\rangle$ by the defining identity of $\star$.
   - *Why needed:* Brings the equation into the $L^2$-inner-product language.

4. **Rewrite the second term as $\langle\alpha, \pm\star d\star\beta\rangle$.**
   - *Hint:* $\alpha\wedge d\star\beta = \alpha\wedge\star\star^{-1}d\star\beta = \langle\alpha, \star^{-1}d\star\beta\rangle\operatorname{vol}_n$. Use the double-star formula to compute $\star^{-1}$ on $(k-1)$-forms in degree $n - k + 1$.
   - *Why needed:* Brings the second term into the inner-product language; this is where the sign-tracking happens.

5. **Track signs to identify the result as $\langle\alpha, \delta\beta\rangle$.**
   - *Hint:* Combine the sign $(-1)^{k-1}$ from Leibniz, the sign $(-1)^{(k-1)(n-k+1)+s}$ from $\star^{-1}$, and the convention sign in $\delta = (-1)^{n(k+1)+1}\star d\star$. Verify the total is $+1$.
   - *Why needed:* The clean form $\langle d\alpha,\beta\rangle = \langle\alpha,\delta\beta\rangle$ requires the sign in the definition of $\delta$ to absorb all the auxiliary signs.

6. **(Corollary)** Manifold with boundary: keep the boundary term, identify it as $\int_{\partial M}\alpha\wedge\star\beta$, observe vanishing under tangential / normal boundary conditions.
   - *Why needed:* Extends the result to bounded domains; the basis for boundary-value Hodge theory.

---

# Lemma Decomposition

> [!note]- Lemma 1: Graded Leibniz rule for $d$ on the wedge $\alpha\wedge\star\beta$
> **Statement:** For $\alpha \in \Omega^{k-1}(M)$ and $\beta \in \Omega^k(M)$,
> $$d(\alpha\wedge\star\beta) = d\alpha\wedge\star\beta + (-1)^{k-1}\alpha\wedge d\star\beta.$$
>
> **Hint:** Apply the graded Leibniz rule $d(\omega\wedge\eta) = d\omega\wedge\eta + (-1)^{\deg\omega}\omega\wedge d\eta$ with $\omega = \alpha$ (degree $k - 1$) and $\eta = \star\beta$ (degree $n - k$).
>
> **Why needed:** Produces the central identity from which all sign-tracking proceeds; the sum on the right is a total derivative.
>
> > [!note]- Full proof
> > Direct application of the graded Leibniz rule for $d$, which is part of the definition of $d$ ([[Def - Exterior Derivative on a Manifold]]). With $\omega = \alpha$ of degree $k - 1$ and $\eta = \star\beta$ of degree $n - k$, the sign of the second term is $(-1)^{\deg\omega} = (-1)^{k-1}$.

> [!note]- Lemma 2: Stokes' theorem kills the boundary on a closed manifold
> **Statement:** On a closed oriented manifold $M$, $\int_M d\omega = 0$ for any $\omega \in \Omega^{n-1}(M)$.
>
> **Hint:** $\int_M d\omega = \int_{\partial M}\omega$ by [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]], and $\partial M = \emptyset$ on a closed manifold.
>
> **Why needed:** Kills the boundary term in the integration of the Leibniz identity; this is what makes adjointness exact (no boundary correction) on closed manifolds.
>
> > [!note]- Full proof
> > By Stokes' theorem, $\int_M d\omega = \int_{\partial M}\omega$. On a closed manifold, $\partial M = \emptyset$, so the right side is the integral of $\omega$ over the empty set, which is $0$.

> [!note]- Lemma 3: Translating wedge products into $L^2$ inner products via $\star$
> **Statement:** For $\alpha, \gamma \in \Omega^p(M)$,
> $$\int_M\alpha\wedge\star\gamma = \langle\alpha,\gamma\rangle_{L^2}.$$
>
> **Hint:** This is the defining identity of $\star$, integrated over $M$.
>
> **Why needed:** Converts wedge-product integrals into inner products, which is the form in which adjointness is naturally stated.
>
> > [!note]- Full proof
> > By the defining identity of $\star$ (see [[Def - The Hodge Star Operator]]), $\alpha\wedge\star\gamma = \langle\alpha,\gamma\rangle_g\operatorname{vol}_n$ pointwise. Integrating over $M$: $\int_M\alpha\wedge\star\gamma = \int_M\langle\alpha,\gamma\rangle_g\operatorname{vol}_n = \langle\alpha,\gamma\rangle_{L^2}$ by definition of the $L^2$ inner product.

> [!note]- Lemma 4: Sign-tracking for $\alpha\wedge d\star\beta$ as an inner product
> **Statement:** For $\alpha \in \Omega^{k-1}(M)$ and $\beta \in \Omega^k(M)$,
> $$\alpha\wedge d\star\beta = (-1)^{(k-1)(n-k+1)+s}\langle\alpha, \star d\star\beta\rangle_g\operatorname{vol}_n.$$
>
> **Hint:** Write $d\star\beta = \star\star^{-1}d\star\beta$ where $\star^{-1}$ on $(n - k + 1)$-forms is $(-1)^{(n-k+1)k + s}\star$ (by the double-star formula applied to degree $n - k + 1$ — which inverts to give back the original $k$-form via $(n - (n - k + 1)) = k - 1$… careful). Alternative: directly compute $\star^{-1}$ as the sign making $\star\star^{-1} = \mathrm{id}$.
>
> **Why needed:** Converts the second term in the Leibniz identity into the inner-product form needed for the adjoint identity.
>
> > [!note]- Full proof
> > Apply $\star^{-1}$ to $d\star\beta \in \Omega^{n-k+1}$: $d\star\beta = \star(\star^{-1}d\star\beta)$ with $\star^{-1}d\star\beta \in \Omega^{k-1}$. So $\alpha\wedge d\star\beta = \alpha\wedge\star(\star^{-1}d\star\beta) = \langle\alpha, \star^{-1}d\star\beta\rangle_g\operatorname{vol}_n$ by the defining identity of $\star$ on $(k-1)$-forms.
> >
> > Now compute $\star^{-1}$: by the double-star formula on $(k-1)$-forms, $\star\star = (-1)^{(k-1)(n-k+1)+s}\mathrm{id}$, so $\star^{-1} = (-1)^{(k-1)(n-k+1)+s}\star$. Hence $\star^{-1}d\star\beta = (-1)^{(k-1)(n-k+1)+s}\star d\star\beta$.
> >
> > Substituting back, $\alpha\wedge d\star\beta = (-1)^{(k-1)(n-k+1)+s}\langle\alpha,\star d\star\beta\rangle_g\operatorname{vol}_n$.

> [!note]- Lemma 5: Sign-tracking gives the adjoint identity
> **Statement:** In Riemannian signature ($s = 0$), the sign $(-1)^{k-1}\cdot(-1)^{(k-1)(n-k+1)}$ from combining the Leibniz term and Lemma 4 equals $-(-1)^{n(k+1)+1}$, so the equation $\langle d\alpha, \beta\rangle + (-1)^{k-1}\int_M\alpha\wedge d\star\beta = 0$ becomes $\langle d\alpha, \beta\rangle = \langle\alpha, \delta\beta\rangle$.
>
> **Hint:** $(-1)^{k-1}\cdot(-1)^{(k-1)(n-k+1)} = (-1)^{(k-1)(n-k+2)}$. Expand $(k-1)(n-k+2) = (k-1)n - (k-1)(k-2)$, and use $(k-1)(k-2) \equiv k-1 \pmod 2$ (it's the product of two consecutive integers... actually $(k-1)(k-2) = k^2 - 3k + 2$, parity depends on $k$). Easier: track signs case-by-case for small $k, n$ and confirm consistency with the defining sign of $\delta$.
>
> **Why needed:** The sign-conspiracy is what makes $\langle d\alpha,\beta\rangle = \langle\alpha,\delta\beta\rangle$ hold cleanly with the standard convention $\delta = (-1)^{n(k+1)+1}\star d\star$.
>
> > [!note]- Full proof (Riemannian, $s = 0$)
> > From Lemmas 1, 2, 3, 4: integrating the Leibniz identity and using Stokes,
> > $$0 = \langle d\alpha,\beta\rangle + (-1)^{k-1}\cdot(-1)^{(k-1)(n-k+1)}\langle\alpha,\star d\star\beta\rangle_{L^2}.$$
> > Combined sign: $(-1)^{(k-1)+(k-1)(n-k+1)} = (-1)^{(k-1)(n-k+2)}$.
> >
> > Solving for $\langle d\alpha,\beta\rangle$:
> > $$\langle d\alpha,\beta\rangle = -(-1)^{(k-1)(n-k+2)}\langle\alpha,\star d\star\beta\rangle = (-1)^{(k-1)(n-k+2)+1}\langle\alpha,\star d\star\beta\rangle.$$
> > For this to equal $\langle\alpha,\delta\beta\rangle$ with $\delta = (-1)^{n(k+1)+1}\star d\star$, we need
> > $$(-1)^{(k-1)(n-k+2)+1} = (-1)^{n(k+1)+1},$$
> > i.e., $(k-1)(n-k+2) \equiv n(k+1) \pmod 2$.
> >
> > Expand: $(k-1)(n-k+2) = kn - k^2 + 2k - n + k - 2 = kn - k^2 + 3k - n - 2$. And $n(k+1) = nk + n$. Difference: $(kn - k^2 + 3k - n - 2) - (kn + n) = -k^2 + 3k - 2n - 2 = -(k^2 - 3k) - 2(n+1)$. Modulo $2$: $-(k^2 - 3k) = -k(k - 3) \equiv k(k+1) \pmod 2$, which is even (product of consecutive integers). So the difference is even, and the signs agree. The adjoint identity holds.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $(M, g)$ be a closed oriented Riemannian $n$-manifold. For any $\alpha \in \Omega^{k-1}(M)$ and $\beta \in \Omega^k(M)$, $\langle d\alpha, \beta\rangle_{L^2} = \langle\alpha, \delta\beta\rangle_{L^2}$.
>
> *Proof.* Consider the $(n-1)$-form $\eta = \alpha\wedge\star\beta$. By the graded Leibniz rule for $d$ (Lemma 1),
> $$d\eta = d\alpha\wedge\star\beta + (-1)^{k-1}\alpha\wedge d\star\beta.$$
> By Stokes' theorem on the closed manifold $M$ (Lemma 2), $\int_M d\eta = 0$. Substituting and rearranging:
> $$\int_M d\alpha\wedge\star\beta = -(-1)^{k-1}\int_M\alpha\wedge d\star\beta = (-1)^k\int_M\alpha\wedge d\star\beta.$$
> The left side is $\langle d\alpha, \beta\rangle_{L^2}$ by Lemma 3. The right side, by Lemma 4, equals $(-1)^k(-1)^{(k-1)(n-k+1)+s}\langle\alpha,\star d\star\beta\rangle_{L^2}$. (Here we write the general signature; the Riemannian case is $s = 0$.)
>
> Combining signs: $(-1)^{k + (k-1)(n-k+1) + s}$. Expanding modulo $2$: $k + (k-1)(n-k+1) + s \equiv k + (k-1)(n-k+1) + s \pmod 2$. A direct calculation (Lemma 5 for the Riemannian case) verifies that this sign equals $-(-1)^{n(k+1)+1}\cdot (-1)^s = (-1)^{n(k+1)+s}$ — exactly the sign in the definition of $\delta = (-1)^{n(k+1) + 1}\star d\star$ in Riemannian signature (and the appropriate signature-adjusted sign in pseudo-Riemannian).
>
> Hence $\langle d\alpha,\beta\rangle_{L^2} = \langle\alpha,\delta\beta\rangle_{L^2}$ in either signature, with $\delta$ defined with the appropriate sign convention.
>
> *Corollary (boundary case).* When $M$ has a boundary $\partial M$, Stokes' theorem instead gives $\int_M d\eta = \int_{\partial M}\eta = \int_{\partial M}\alpha\wedge\star\beta$. The same calculation produces
> $$\langle d\alpha,\beta\rangle_{L^2} - \langle\alpha,\delta\beta\rangle_{L^2} = \int_{\partial M}\alpha\wedge\star\beta.$$
> The boundary integral $\int_{\partial M}\alpha\wedge\star\beta$ vanishes if $i^*\alpha = 0$ (the pullback of $\alpha$ to $\partial M$ vanishes — **tangential boundary condition** on $\alpha$) or if $i^*(\star\beta) = 0$ (**normal boundary condition** on $\beta$). $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry — divergence theorem.** On a closed Riemannian manifold, $\int_M(\operatorname{div} X)\operatorname{vol}_g = 0$ for any vector field $X$. The proof: $\operatorname{div} X = -\delta X^\flat$ (where $X^\flat$ is the metric dual $1$-form), so $\int_M(\operatorname{div} X)\operatorname{vol}_g = -\int_M\delta X^\flat\operatorname{vol}_g = -\langle\delta X^\flat, 1\rangle_{L^2} = -\langle X^\flat, d\cdot 1\rangle_{L^2} = -\langle X^\flat, 0\rangle = 0$, applying the adjoint identity with $\alpha = 1$, $\beta = X^\flat$. The divergence theorem on a closed manifold is the adjoint identity in disguise.

**Variational calculus — Euler–Lagrange for $\|\omega\|^2$.** Minimize $F(\omega) = \|\omega\|^2_{L^2}$ over $\omega = \omega_0 + d\eta$ in the cohomology class of $\omega_0$ (closed manifold). First variation: $0 = \frac{d}{dt}F(\omega + td\zeta) = 2\langle\omega, d\zeta\rangle$ for all $\zeta$, equivalently $2\langle\delta\omega,\zeta\rangle = 0$ for all $\zeta$ (by adjointness), equivalently $\delta\omega = 0$. So the minimizer is coclosed; combined with closedness ($\omega$ in the class), the minimizer is harmonic. The Euler–Lagrange derivation *literally is* the adjoint identity.

**Electromagnetism — gauge invariance of Maxwell action.** The Maxwell action on a Lorentzian $4$-manifold is $S = -\frac{1}{4}\int F\wedge\star F$ where $F = dA$ is the electromagnetic curvature. Vary $A \to A + d\chi$ for a function $\chi$ (gauge transformation): $F \to F + d^2\chi = F$, so $S$ is gauge-invariant. The variation $A \to A + a$ for a general $1$-form $a$: $\delta S = -\frac{1}{2}\int da\wedge\star F = -\frac{1}{2}\langle da, F\rangle = -\frac{1}{2}\langle a, \delta F\rangle$ by the adjoint identity. The Euler–Lagrange equation is $\delta F = 0$, equivalently $d\star F = 0$, the source-free Maxwell equation. The adjoint identity is what produces the equation of motion from the action.

---

# Bridges

- **[[Def - Hodge Laplacian|Hodge Laplacian self-adjointness]]** — the Hodge Laplacian $\Delta = d\delta + \delta d$ is self-adjoint as an immediate corollary of the adjoint identity. Computation: $\langle\Delta\alpha,\beta\rangle = \langle d\delta\alpha,\beta\rangle + \langle\delta d\alpha,\beta\rangle = \langle\delta\alpha, \delta\beta\rangle + \langle d\alpha, d\beta\rangle = \langle\alpha,\Delta\beta\rangle$ (using adjointness twice and the fact that $\langle d\alpha, d\beta\rangle$ and $\langle\delta\alpha,\delta\beta\rangle$ are each symmetric in $\alpha,\beta$). Self-adjointness is the gateway to spectral theory.

- **[[Thm - Hodge Decomposition Theorem|Hodge decomposition theorem]]** — the orthogonal direct sum $\Omega^k = \mathcal{H}^k\oplus d\Omega^{k-1}\oplus\delta\Omega^{k+1}$ has each summand orthogonal to the others, and the orthogonality is a direct consequence of the adjoint identity. $\langle d\alpha, \delta\gamma\rangle = \langle d^2\alpha, \gamma\rangle = 0$ (using adjointness and $d^2 = 0$); similar for the other pairs. The adjoint identity is the algebraic skeleton of the decomposition.

- **Green's theorem and the divergence theorem** — on a manifold with boundary, the corollary $\langle d\alpha,\beta\rangle - \langle\alpha,\delta\beta\rangle = \int_{\partial M}\alpha\wedge\star\beta$ is the form-version of the classical Green's theorem $\int_M(\nabla^2 u\cdot v - u\cdot\nabla^2 v)dx = \int_{\partial M}(v\partial_n u - u\partial_n v)dS$. The form-version unifies Green's theorem, the divergence theorem, and the Kelvin–Stokes theorem into a single statement.

- **[[Def - Self-Dual and Anti-Self-Dual Forms|Hodge orthogonality]]** — on a Riemannian $4$-manifold, the self-dual and anti-self-dual decompositions of $\Omega^2$ are orthogonal in the $L^2$ inner product. This orthogonality is a consequence of the adjoint identity (with appropriate sign tracking through $\star$): self-dual and anti-self-dual forms have opposite $\star$-eigenvalues, and the orthogonality follows from skew-symmetry of the bilinear pairing on opposite eigenspaces of a self-adjoint operator.

---

# Unlocked by This

> [!tip] Symmetric Elliptic Operators and Their Spectra *(from Functional Analysis)*
> The adjoint identity $\langle d\alpha,\beta\rangle = \langle\alpha,\delta\beta\rangle$ makes $d$ and $\delta$ into a pair of adjoint first-order operators, and their composition $\Delta = (d + \delta)^2$ is a self-adjoint *second-order* elliptic operator. By the spectral theorem for self-adjoint operators on Hilbert spaces, $\Delta$ has a real discrete spectrum with finite-dimensional eigenspaces (on a closed manifold). This is the foundation of **spectral geometry**: extracting topological and geometric invariants from the spectrum of $\Delta$. The **heat kernel** $e^{-t\Delta}$ has small-time asymptotics encoding curvature invariants, and large-time behavior encoding topological invariants (via the harmonic projection).

> [!tip] Hodge Theory on Manifolds with Boundary *(from PDE Theory)*
> The boundary-corrected adjoint identity $\langle d\alpha,\beta\rangle - \langle\alpha,\delta\beta\rangle = \int_{\partial M}\alpha\wedge\star\beta$ is the basis for **boundary-value Hodge theory**. Two natural boundary conditions emerge: tangential ($i^*\alpha = 0$) and normal ($i^*\star\beta = 0$). Imposing tangential conditions on both $\alpha$ and $\beta$ gives the **absolute** Hodge theorem (representing $H^k(M)$). Imposing normal conditions gives the **relative** Hodge theorem (representing $H^k(M, \partial M)$). The two are related by Lefschetz duality, the manifold-with-boundary version of Poincaré duality, and provide the framework for **Hodge theory on physical bounded domains** — incompressible fluid flow, electromagnetic potential theory, magnetostatics with conducting boundaries.

> [!tip] Yang–Mills Functional and Self-Duality *(from Gauge Theory)*
> The Yang–Mills functional on a principal $G$-bundle over a Riemannian $4$-manifold is $S(A) = \|F_A\|^2_{L^2} = \int_M\langle F_A, F_A\rangle\operatorname{vol}_g$. The Euler–Lagrange equation, derived via the adjoint identity for the bundle-valued exterior derivative $d_A$, is the **Yang–Mills equation** $d_A\star F_A = 0$, equivalently $\delta_A F_A = 0$. The minimum-energy solutions in each topological class are the **instantons** (self-dual connections), saturating the bound $\|F_A\|^2 \geq |c_2|\cdot 8\pi^2$ via the orthogonal decomposition $F = F_+ + F_-$. The entire Yang–Mills theory is constructed using the bundle-valued analogue of the adjoint identity here.
