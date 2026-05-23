---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Vector Bundle"
  - "Def - Connection on a Vector Bundle"
  - "Def - Curvature of a Vector-Bundle Connection"
tags: [geometry, gauge-theory, curvature, trivial-bundle]
---

# Problem Statement

Let $E = M \times \mathbb{R}^K$ be the trivial rank-$K$ real vector bundle over a smooth manifold $M$, with the global frame $(e_1, \dots, e_K)$ given by the standard basis of $\mathbb{R}^K$ at every point. Define the **trivial connection** $\nabla_0$ on $E$ by $\nabla_0\sigma = d\sigma$ componentwise — i.e., if $\sigma = \sum_\alpha\sigma^\alpha e_\alpha$, then $\nabla_0\sigma = \sum_\alpha(d\sigma^\alpha)e_\alpha$.

**(a)** Verify $\nabla_0$ is a connection (linearity + Leibniz).

**(b)** Compute the connection 1-form matrix $\omega$ of $\nabla_0$ in the global frame, and the curvature 2-form matrix $F$.

**(c)** Conclude: the trivial bundle with trivial connection has zero curvature. Conversely, a non-zero curvature in any frame proves the bundle does not admit a global frame with that flat connection.

**Recall:**

![[Def - Curvature of a Vector-Bundle Connection#The Definition]]

A connection $\nabla$ on $E \to M$ is an $\mathbb{R}$-linear map $\Gamma(E) \to \Gamma(E \otimes T^*M)$ with Leibniz rule $\nabla(f\sigma) = f\nabla\sigma + \sigma \otimes df$. The curvature in a local frame is $F = d\omega + \omega \wedge \omega$.

---

# Convergent Strategy

**Problem class:** This is a basic computational exercise verifying the definition of a connection and the curvature formula on the simplest possible example. The point is twofold: (i) to confirm that the trivial connection truly is a connection (verifying linearity and Leibniz), and (ii) to compute its curvature directly from the structure equation, confirming that flatness is automatic in the global frame. The exercise serves as a *calibration* for the general curvature formula: if you cannot compute curvature on the trivial bundle, you cannot compute it anywhere.

**Assumption pattern:** The bundle is fully described by its global trivialization $E \cong M \times \mathbb{R}^K$, and the connection is defined by "componentwise $d$" in this trivialization. Every quantity is expressible in terms of standard exterior calculus on $M$; no curvature can hide in the structure because the trivialization is global.

**Theorem routing:** Linearity and Leibniz for $\nabla_0$ follow directly from the linearity and Leibniz properties of the exterior derivative $d$ acting on each component. The connection 1-form $\omega$ is read off the equation $\nabla_0 e_\beta = e_\alpha \otimes \omega^\alpha{}_\beta$: since the frame vectors $e_\beta$ are *constant* in the trivialization (their components are the constant Kronecker delta function $\delta^\alpha_\beta$), $\nabla_0 e_\beta = 0$, so $\omega = 0$. The curvature formula then gives $F = d(0) + 0 \wedge 0 = 0$.

**Key decision point:** The non-obvious step is recognizing that the conclusion "trivial connection has zero curvature" *depends on the choice of trivialization* — specifically, on using the *standard* frame given by the global trivialization. If one changes frame to a non-global frame (say a moving frame depending on $p$), the same connection $\nabla_0$ will produce a *non-zero* $\omega$ in the new frame (with $\omega = c^{-1}dc$ being the Maurer-Cartan correction), and the curvature in the new frame will be $F = d\omega + \omega \wedge \omega$ — which, computed naively, looks non-zero but actually vanishes by the structure equation. The trick is that the *invariant* curvature 2-form is zero; only the *frame-dependent expression* of $\omega$ varies.

---

# Legal Operations Used

1. **Choose a local trivialization (chart) and compute everything component-wise** (operation 1 of the topic page). Here the choice is the global trivialization, in which all components reduce to ordinary calculus on $M$.

2. **Apply the curvature formula $F = d\omega + \omega \wedge \omega$** (operation 2). With $\omega = 0$ in the global frame, both terms vanish, giving $F = 0$.

4. **Use the Leibniz rule to break covariant derivatives apart** (operation 4). Verifying $\nabla_0$ is a connection requires verifying Leibniz, which follows from Leibniz for $d$ on each component.

---

# Hints

> [!note]- Hint 1
> In the global frame $(e_1, \dots, e_K)$, the basis sections $e_\beta : M \to E$ have *constant* component functions $\sigma^\alpha = \delta^\alpha_\beta$ (the Kronecker delta). The exterior derivative of a constant function is zero.

> [!note]- Hint 2
> The connection 1-form $\omega^\alpha{}_\beta$ is defined by $\nabla_0 e_\beta = e_\alpha \otimes \omega^\alpha{}_\beta$. Compute $\nabla_0 e_\beta$ using the trivial-connection formula $\nabla_0\sigma = d\sigma$ componentwise.

> [!note]- Hint 3
> The curvature $F = d\omega + \omega \wedge \omega$ depends only on $\omega$. With $\omega = 0$ identically, every term in the formula is zero.

> [!note]- Hint 4 (for the converse)
> If a bundle $E \to M$ admits a connection with non-zero curvature in *every* frame, then it cannot be trivial (in the sense of admitting a global frame in which the connection is the trivial one). More precisely, a flat bundle (admitting a flat connection) need not be trivial — only simply-connected ones must be. The Wilson lines of a flat connection encode the bundle's monodromy.

---

# Solution

The proof is short. Part (a) verifies $\nabla_0$ satisfies linearity and Leibniz by direct computation, reducing to known properties of $d$. Part (b) reads off $\omega = 0$ from the definition applied to the global frame, hence $F = d(0) + 0 \wedge 0 = 0$. Part (c) interprets: the trivial connection on the trivial bundle is *flat*. The contrapositive — a non-zero curvature in any chosen frame is an obstruction to a global trivialization — is one of the standard ways to detect non-trivial bundles.

**Step 1: $\nabla_0$ is a connection (linearity and Leibniz).**

> [!note]- Derivation
> *Linearity.* For $\sigma_1, \sigma_2 \in \Gamma(E)$, $a, b \in \mathbb{R}$:
> $$\nabla_0(a\sigma_1 + b\sigma_2) = \sum_\alpha d(a\sigma_1^\alpha + b\sigma_2^\alpha)e_\alpha = \sum_\alpha(a\,d\sigma_1^\alpha + b\,d\sigma_2^\alpha)e_\alpha = a\nabla_0\sigma_1 + b\nabla_0\sigma_2.$$
> Uses $\mathbb{R}$-linearity of $d$ on functions.
>
> *Leibniz.* For $f \in C^\infty(M)$, $\sigma \in \Gamma(E)$:
> $$\nabla_0(f\sigma) = \sum_\alpha d(f\sigma^\alpha)e_\alpha = \sum_\alpha[(df)\sigma^\alpha + f\,d\sigma^\alpha]e_\alpha = (df)\sum_\alpha\sigma^\alpha e_\alpha + f\sum_\alpha(d\sigma^\alpha)e_\alpha = \sigma \otimes df + f\nabla_0\sigma.$$
> Uses the Leibniz rule for $d$ on functions.
>
> Hence $\nabla_0$ is a connection.

**Step 2: $\omega = 0$ in the global frame.**

> [!note]- Derivation
> Compute $\nabla_0 e_\beta$ for each $\beta = 1, \dots, K$. The section $e_\beta : M \to E$ has component functions $\sigma^\alpha = \delta^\alpha_\beta$ — *constant* functions (always $0$ or $1$). Therefore:
> $$\nabla_0 e_\beta = \sum_\alpha d(\delta^\alpha_\beta)\,e_\alpha = \sum_\alpha 0 \cdot e_\alpha = 0.$$
>
> Comparing to the defining equation $\nabla_0 e_\beta = e_\alpha \otimes \omega^\alpha{}_\beta$: we have $e_\alpha \otimes \omega^\alpha{}_\beta = 0$ for every $\beta$. Since the $e_\alpha$ are a basis, all coefficients vanish: $\omega^\alpha{}_\beta = 0$ for all $\alpha, \beta$.
>
> In matrix form: $\omega = 0$, the zero matrix of 1-forms.

**Step 3: Curvature $F = 0$.**

> [!note]- Derivation
> Apply the structure equation $F = d\omega + \omega \wedge \omega$ with $\omega = 0$:
> $$F = d(0) + 0 \wedge 0 = 0.$$
>
> Both terms vanish trivially. The curvature 2-form is identically zero. The connection $\nabla_0$ is **flat**.

**Step 4: The converse — non-trivial bundles have non-zero curvature in every frame.**

> [!note]- Derivation
> Suppose $\nabla$ is a connection on $E$ whose curvature $F$ is non-zero in *some* (hence every, by tensoriality) frame. Then $\nabla$ cannot be the trivial connection on a trivial bundle, because the trivial connection has $F = 0$.
>
> More strongly: if a bundle admits *any* flat connection, that bundle's first Chern class (for line bundles) or other characteristic classes must vanish. For the tangent bundle $TS^2$, the first Chern class is $\chi(S^2) = 2 \ne 0$, so $TS^2$ admits *no* flat connection — *any* connection on $TS^2$ has non-zero curvature somewhere on $S^2$.
>
> The contrapositive is one of the standard ways to detect bundle non-triviality: compute the curvature of *some* connection (any will do), check whether it integrates to a non-zero topological invariant (e.g., $\int_{S^2}F/(2\pi) \ne 0$ for line bundles on $S^2$), and conclude non-triviality from the non-vanishing.

> [!note]- Complete formal solution
> Let $E = M \times \mathbb{R}^K$ be the trivial rank-$K$ real vector bundle over $M$, with global frame $(e_\alpha)_{\alpha=1}^K$ given by the standard basis of $\mathbb{R}^K$ at each point. Define $\nabla_0\sigma = \sum_\alpha(d\sigma^\alpha)e_\alpha$ for $\sigma = \sum_\alpha\sigma^\alpha e_\alpha$.
>
> **Linearity:** Follows from $\mathbb{R}$-linearity of $d$ on each component.
>
> **Leibniz:** $\nabla_0(f\sigma) = \sum_\alpha d(f\sigma^\alpha)e_\alpha = \sum_\alpha[(df)\sigma^\alpha + f\,d\sigma^\alpha]e_\alpha = \sigma \otimes df + f\nabla_0\sigma$.
>
> Hence $\nabla_0$ is a connection.
>
> **Connection 1-form:** $\nabla_0 e_\beta = \sum_\alpha d(\delta^\alpha_\beta)e_\alpha = 0$. Comparing with $\nabla_0 e_\beta = e_\alpha \otimes \omega^\alpha{}_\beta$, all $\omega^\alpha{}_\beta = 0$. Hence $\omega = 0$ in the global frame.
>
> **Curvature:** $F = d\omega + \omega \wedge \omega = d(0) + 0 \wedge 0 = 0$. The curvature is identically zero. $\blacksquare$

> [!warning] What "trivial" means — and what it doesn't
> "Trivial bundle with trivial connection" is a very specific statement: the bundle is $M \times \mathbb{R}^K$ as a *bundle* (admits a global frame), and the connection is the "componentwise $d$" *in that specific global frame*. A *non-trivial* connection on a *trivial* bundle is perfectly possible (and common): on $M \times \mathbb{R}$, for any 1-form $A \in \Omega^1(M)$, the operator $\nabla = d + A$ is a connection with $\omega = A$ and $F = dA$ — non-zero whenever $A$ is not closed. So flatness of the connection ≠ triviality of the bundle; non-flatness of *every* connection ⟹ non-triviality of the bundle (the contrapositive).

---

# Key Takeaways

**Triviality of the bundle ≠ flatness of the connection.**

This exercise drills the subtle distinction between *trivial bundle* (admits a global frame) and *flat connection* (zero curvature). The trivial bundle with trivial connection is flat, but the trivial bundle admits many *non-trivial* connections — for any 1-form $A$ on $M$, the connection $d + A$ on $M \times \mathbb{R}$ has curvature $F = dA$, which is generally non-zero. Conversely, a non-trivial bundle (one without a global frame) may or may not admit a flat connection: $TS^2$ does not (any connection has non-zero curvature, by Gauss-Bonnet / Poincaré-Hopf), but a flat line bundle over the torus $T^2$ corresponding to a non-trivial $\pi_1$-representation is non-trivial (as a bundle with connection) yet has $F = 0$.

**The contrapositive: non-zero curvature detects bundle non-triviality.**

If a bundle admits *any* connection whose curvature integrates to a non-zero topological invariant over some closed cycle, the bundle cannot be trivial (and cannot admit a flat connection, in the simply-connected case). This is one of the principal applications of curvature in geometry: to *detect* non-trivial topology by *computing* curvature integrals. The first Chern number $\frac{1}{2\pi}\int_\Sigma F$ for line bundles is the prototypical example; higher characteristic classes generalize this.

**Computational reliability comes from working in the right frame.**

The choice of global frame is what makes this computation trivial. The same connection $\nabla_0$ in a different (non-global) frame would have a *non-zero* connection 1-form $\omega = c^{-1}dc$ (where $c$ is the change of frame), but the curvature would still compute to zero (the Maurer-Cartan piece $c^{-1}dc$ is flat). The lesson is: when checking flatness, use a global frame if one exists; the computation is then transparent. When working in a non-global frame (e.g., on a non-trivial bundle, where no global frame exists), be prepared to compute $\omega \wedge \omega$ and $d\omega$ separately, with cancellations possibly happening or not.
