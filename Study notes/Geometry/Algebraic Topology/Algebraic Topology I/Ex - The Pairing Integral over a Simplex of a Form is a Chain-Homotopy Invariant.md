---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Def - de Rham Cohomology"
  - "Def - Singular Homology"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, algebraic-topology, de-rham, stokes]
---

# Problem Statement

Let $M$ be a smooth manifold. For a closed smooth $p$-form $\omega \in \Omega^p(M)$ and a smooth singular $p$-cycle $c \in Z_p^\infty(M; \mathbb{R})$, the integral $\int_c \omega = \sum_i a_i \int_{\sigma_i} \omega$ (extended $\mathbb{R}$-linearly from the simplex-wise integral $\int_\sigma \omega = \int_{\Delta^p} \sigma^* \omega$) defines a real number. Show that this number depends only on the de Rham cohomology class $[\omega] \in H^p_{dR}(M)$ and the singular homology class $[c] \in H_p(M; \mathbb{R})$ — i.e., it is invariant under modifying $\omega$ by an exact form and modifying $c$ by a boundary.

**Recall:**

A closed form is $\omega \in \Omega^p(M)$ with $d\omega = 0$. An exact form is $\omega = d\eta$ for some $(p-1)$-form $\eta$. The [[Def - de Rham Cohomology|de Rham cohomology]] is $H^p_{dR}(M) = \{\text{closed }p\text{-forms}\}/\{\text{exact }p\text{-forms}\}$.

A singular cycle is $c \in C_p(M; \mathbb{R})$ with $\partial c = 0$. A boundary is $c = \partial b$ for some $(p+1)$-chain $b$. The [[Def - Singular Homology|singular homology]] is $H_p(M; G) = \{\text{cycles}\}/\{\text{boundaries}\}$.

The pairing is $\langle \omega, c \rangle = \int_c \omega$. [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] says $\int_{\partial b} \omega = \int_b d\omega$ for a smooth chain $b$ and a smooth form $\omega$.

---

# Convergent Strategy

**Problem class:** This is a well-definedness exercise: verify that a candidate function — defined on representatives — actually descends to a function on equivalence classes. The class is "show a function defined on pairs of representatives is independent of the choices, so it gives a well-defined map on cohomology classes." This is the well-definedness step in the construction of the de Rham homomorphism.

**Assumption pattern:** We have a smooth manifold $M$, a closed form $\omega$, and a smooth singular cycle $c$. We are given two types of "change" that should leave the pairing invariant:
- $\omega \to \omega' = \omega + d\eta$ (change of de Rham representative by an exact form)
- $c \to c' = c + \partial b$ (change of homology representative by a boundary)

**Theorem routing:** [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] is the single tool needed for both checks. The two computations are dual: closed form + boundary cycle gives an integral over the boundary, which by Stokes equals the integral of $d$(form) over the chain, which is zero because the form is closed. Exact form + cycle gives an integral of $d$(form) over the cycle, which by Stokes equals the integral of the form over the boundary of the cycle, which is zero because the cycle is closed.

**Key decision point:** The non-obvious step is recognising that the *same* identity from Stokes — $\int_{\partial \alpha} \beta = \int_\alpha d\beta$ — handles both checks at once. The two situations are dual: in the form-change check, we use $\int_c d\eta = \int_{\partial c} \eta = 0$; in the cycle-change check, we use $\int_{\partial b} \omega = \int_b d\omega = 0$. The roles of "boundary" and "exterior derivative" swap, but Stokes is the same identity providing the bridge.

---

# Legal Operations Used

1. **Apply Stokes's theorem to convert boundary integrals into integrals of exterior derivatives** (analogous to operation 3 from the topic page). For a smooth chain $b$ and a smooth form $\eta$: $\int_{\partial b} \eta = \int_b d\eta$.

2. **Use $\partial c = 0$ for a cycle and $d\omega = 0$ for a closed form** (operation 3 again, restated). The cycle and closed-form hypotheses kill the boundary-of-a-cycle term and the exterior-derivative-of-a-closed-form term, respectively.

3. **Use $\mathbb{R}$-linearity of integration** (operation 9). Integration is $\mathbb{R}$-linear, so $\int_c (\omega + d\eta) = \int_c \omega + \int_c d\eta$, decomposing the change into separate terms.

---

# Hints

> [!note]- Hint 1
> The well-definedness of the pairing requires two independent checks. First: changing $\omega$ to $\omega' = \omega + d\eta$ should not change $\int_c \omega$. By linearity of integration, the change is $\int_c (\omega' - \omega) = \int_c d\eta$. This should be zero. Use Stokes's theorem to convert $\int_c d\eta$ into something involving $\partial c$, which is zero by hypothesis.

> [!note]- Hint 2
> Second: changing $c$ to $c' = c + \partial b$ should not change $\int_c \omega$. By linearity, the change is $\int_{c' - c} \omega = \int_{\partial b} \omega$. Use Stokes's theorem to convert this into $\int_b d\omega$. This should be zero because $\omega$ is closed.

> [!note]- Hint 3
> Both checks use Stokes's theorem $\int_{\partial \alpha} \beta = \int_\alpha d\beta$. The roles of "boundary" and "exterior derivative" are different in each check, but the same identity does the work. Combine both checks to show $\int_c \omega = \int_{c'} \omega'$ whenever $\omega - \omega' \in B^p_{dR}$ and $c - c' \in B_p$.

---

# Solution

The proof breaks into two checks, each a one-line application of Stokes's theorem.

**Step 1: Changing the de Rham representative does not change the pairing.**

Let $\omega, \omega' \in Z^p_{dR}(M)$ with $\omega' = \omega + d\eta$ for some $(p-1)$-form $\eta$. For any smooth singular $p$-cycle $c$ ($\partial c = 0$),
$$
\int_c \omega' - \int_c \omega = \int_c (\omega' - \omega) = \int_c d\eta.
$$
By Stokes,
$$
\int_c d\eta = \int_{\partial c} \eta = \int_0 \eta = 0,
$$
since $\partial c = 0$ (the boundary of a cycle is zero).

Hence $\int_c \omega' = \int_c \omega$, independent of which representative of $[\omega]$ we use.

> [!note]- Derivation
> The integration is $\mathbb{R}$-linear: $\int_c (\omega + d\eta) = \int_c \omega + \int_c d\eta$. So the change in the pairing is $\int_c d\eta$.
>
> Stokes's theorem on smooth singular chains: $\int_{\partial \alpha} \beta = \int_\alpha d\beta$ for any smooth chain $\alpha$ and any smooth form $\beta$ (of degree matching to make the integrals defined). Apply with $\alpha = c$ and $\beta = \eta$:
> $$
> \int_c d\eta = \int_{\partial c} \eta.
> $$
> Since $c$ is a cycle, $\partial c = 0$, so $\int_{\partial c} \eta = 0$.

**Step 2: Changing the homology representative does not change the pairing.**

Let $c, c' \in Z_p^\infty(M; \mathbb{R})$ with $c' = c + \partial b$ for some smooth $(p+1)$-chain $b$. For any closed smooth $p$-form $\omega$ ($d\omega = 0$),
$$
\int_{c'} \omega - \int_c \omega = \int_{c' - c} \omega = \int_{\partial b} \omega.
$$
By Stokes,
$$
\int_{\partial b} \omega = \int_b d\omega = \int_b 0 = 0,
$$
since $\omega$ is closed (so $d\omega = 0$).

Hence $\int_{c'} \omega = \int_c \omega$, independent of which representative of $[c]$ we use.

> [!note]- Derivation
> Linearity: $\int_{c + \partial b} \omega = \int_c \omega + \int_{\partial b} \omega$. The change is $\int_{\partial b} \omega$.
>
> Stokes's theorem: $\int_{\partial b} \omega = \int_b d\omega$. Since $\omega$ is closed, $d\omega = 0$, and the right side vanishes.

> [!note]- Complete formal solution
> **Theorem.** The pairing $\langle \omega, c \rangle = \int_c \omega$ defined for closed forms $\omega$ and smooth cycles $c$ descends to a well-defined pairing
> $$
> \langle \cdot, \cdot \rangle : H^p_{dR}(M) \times H_p(M; \mathbb{R}) \to \mathbb{R}, \qquad \langle [\omega], [c] \rangle = \int_c \omega.
> $$
>
> *Proof.* We must show: if $\omega, \omega'$ are closed $p$-forms representing the same de Rham class ($\omega - \omega'$ is exact), and $c, c'$ are smooth $p$-cycles representing the same homology class ($c - c'$ is a boundary), then $\int_c \omega = \int_{c'} \omega'$.
>
> *Check 1 (vary form):* $\omega - \omega' = d\eta$ for some $\eta \in \Omega^{p-1}(M)$. By Stokes applied to $c$ (a cycle, $\partial c = 0$),
> $$
> \int_c (\omega - \omega') = \int_c d\eta = \int_{\partial c} \eta = 0.
> $$
> So $\int_c \omega = \int_c \omega'$.
>
> *Check 2 (vary cycle):* $c - c' = \partial b$ for some $b \in C_{p+1}^\infty(M; \mathbb{R})$. By Stokes applied to $\omega'$ (closed, $d\omega' = 0$),
> $$
> \int_{c - c'} \omega' = \int_{\partial b} \omega' = \int_b d\omega' = 0.
> $$
> So $\int_c \omega' = \int_{c'} \omega'$.
>
> Combining: $\int_c \omega = \int_c \omega' = \int_{c'} \omega'$. Hence the pairing depends only on $[\omega]$ and $[c]$. $\qquad\blacksquare$

---

# Key Takeaways

**Stokes's theorem is the bridge between the chain-side and the form-side of the de Rham pairing.** The single identity $\int_{\partial \alpha} \beta = \int_\alpha d\beta$ is what makes the integration pairing well-defined on cohomology classes. The intuition: the boundary operator $\partial$ on chains and the exterior derivative $d$ on forms are *adjoints* under integration. Closed forms (kernel of $d$) pair trivially with boundaries (image of $\partial$); exact forms (image of $d$) pair trivially with cycles (kernel of $\partial$). The pairing descends to a non-degenerate pairing on cohomology classes precisely because these "trivial pairings" are exactly what gets quotiented out.

**The two checks are dual under integration.** Check 1 (vary form) uses $\partial c = 0$ to kill $\int_{\partial c} \eta$. Check 2 (vary cycle) uses $d\omega = 0$ to kill $\int_b d\omega$. Same identity (Stokes), different role for the "killing condition." The duality is a general feature of any pairing built from an operator-and-coboundary structure: closed cocycles pair trivially with boundaries; exact coboundaries pair trivially with cycles. This pattern recurs in every cohomology-vs-homology pairing in mathematics — algebraic geometry, étale cohomology, sheaf cohomology — and the dual-role of Stokes is the prototype.

**This is the well-definedness step of the de Rham homomorphism.** The de Rham theorem ([[Thm - The de Rham Theorem (Full Proof)]]) asserts that the de Rham homomorphism $\mathcal{I} : H^p_{dR}(M) \to H^p(M; \mathbb{R})$, $\mathcal{I}[\omega][c] = \int_c \omega$, is an *isomorphism*. The current exercise establishes that $\mathcal{I}$ is a well-defined *map* — the deep theorem builds on this and shows it is also injective and surjective. So this exercise is the foundation; the de Rham theorem is the superstructure built upon it. Without well-definedness, one cannot even *state* the de Rham theorem coherently.

**The pairing produces a topological invariant.** Once we have well-definedness, the integer (or real, or rational) $\int_c \omega$ depends only on the homology class $[c]$ and the cohomology class $[\omega]$ — both of which are topological invariants (by [[Thm - Homotopy Invariance of Singular Homology]] for homology, and by the de Rham theorem for cohomology). So the smooth-form integral $\int_c \omega$ is a topological number, dependent only on the homotopy type of the space and the choices of $[c]$ and $[\omega]$. This is the source of every "topological invariant computed by an integral" in physics and geometry: winding numbers, magnetic monopole charges, instanton numbers, Chern numbers — all are values of well-defined pairings of cohomology classes against homology classes, given by integration.
