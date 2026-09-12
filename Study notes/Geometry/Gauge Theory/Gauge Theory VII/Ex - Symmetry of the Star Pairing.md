---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Hodge Star in Arbitrary Signature"
  - "Thm - Properties of the Hodge Star in Arbitrary Signature"
  - "Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $V$ be an oriented real vector space of dimension $n$, equipped with a non-degenerate symmetric bilinear form $\langle\cdot,\cdot\rangle$ of index $p$ (the number of negative signs in a diagonalisation, well-defined by Sylvester's law of inertia), and let $\star:\Lambda^k V^* \to \Lambda^{n-k} V^*$ be the associated Hodge star. Prove the **symmetry of the star pairing**: for all $\omega,\eta \in \Lambda^k V^*$,
$$\omega \wedge \star\eta = \eta \wedge \star\omega = (-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol}.$$
Then deduce the corresponding statement in integrated form. Let $(M,g)$ be an oriented compact semi-Riemannian manifold of dimension $n$ and constant index $p$, let $\mathrm{vol}_g$ be its volume form, and define the **$L^2$ inner product** on $k$-forms by $\langle\omega,\eta\rangle_{L^2} := \int_M \langle\omega,\eta\rangle_g\,\mathrm{vol}_g$. Show that for all $\omega,\eta \in \Omega^k(M)$,
$$\int_M \omega \wedge \star\eta = (-1)^p\,\langle\omega,\eta\rangle_{L^2}.$$

This is Bär's property (3.5) of the Hodge star (Proposition 3.1.8(4)), together with its integrated consequence, which is the identity every first-variation computation in electrodynamics and Yang–Mills theory (§7.2–§7.4) silently rests on: it turns the wedge integral $\int_M \omega\wedge\star\eta$ into a symmetric, signature-corrected $L^2$ pairing, and symmetry is exactly what lets one integrate by parts inside the variation of the action.

**Recall:**

The objects in play are the induced inner product and volume form on the exterior powers of a semi-Euclidean space, the Hodge star defined through the wedge pairing, and one algebraic property of the star (that it is an isometry up to the sign $(-1)^p$).

![[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms#The Definition]]

A **generalized orthonormal basis** of $(V,\langle\cdot,\cdot\rangle)$ is a basis $e_1,\dots,e_n$ with $\langle e_i,e_j\rangle = 0$ for $i \ne j$ and $\langle e_j,e_j\rangle = \epsilon_j \in \{+1,-1\}$; the **index** $p$ counts the $j$ with $\epsilon_j = -1$. The **induced inner product** on $\Lambda^k V^*$ is $\langle\omega,\eta\rangle = \sum_{i_1 < \dots < i_k} \epsilon_{i_1}\cdots\epsilon_{i_k}\,\omega(e_{i_1},\dots,e_{i_k})\,\eta(e_{i_1},\dots,e_{i_k})$; it is symmetric because each summand is symmetric under exchanging $\omega$ and $\eta$. The **volume form** is $\mathrm{vol} = e_1^* \wedge \dots \wedge e_n^*$ for a positively oriented generalized orthonormal basis.

![[Def - Hodge Star in Arbitrary Signature#The Definition]]

The **Hodge star** $\star:\Lambda^k V^* \to \Lambda^{n-k} V^*$ is the unique linear map satisfying the **defining relation**
$$\alpha \wedge \beta = \langle\star\alpha,\beta\rangle\,\mathrm{vol} \qquad \text{for all } \alpha \in \Lambda^k V^*,\ \beta \in \Lambda^{n-k} V^*.$$
Its existence and uniqueness are established in [[Thm - Existence and Uniqueness of the Hodge Star]]; the key structural input is that the induced inner product on each $\Lambda^m V^*$ is non-degenerate, so that a linear functional on $\Lambda^{n-k}V^*$ is represented by a unique element $\star\alpha$.

> [!warning] Convention: three Hodge stars
> This series uses **Bär's convention** $\alpha \wedge \beta = \langle\star_B\alpha,\beta\rangle\,\mathrm{vol}$ throughout ($\star = \star_B$ on this page). Two other conventions appear in the literature and in earlier vault chapters, and the identity proved here is exactly what relates them:
> - The vault's Hodge Theory I star $\star_V$ (see [[Def - The Hodge Star Operator]]) is defined by $\alpha \wedge \star_V\beta = \langle\alpha,\beta\rangle\,\mathrm{vol}$ for $\alpha,\beta \in \Lambda^k V^*$. Comparing this with the result below shows $\star_B = (-1)^p\,\star_V$.
> - The convention $\star'\alpha \wedge \beta = \langle\alpha,\beta\rangle\,\mathrm{vol}$ satisfies $\star' = (-1)^{k(n-k)}\star_V$.
>
> All three coincide in Riemannian signature ($p=0$), in every degree. On Minkowski space $(-,+,+,+)$, $p=1$, so $\star_B = -\star_V$; for instance $\star_B(dt \wedge dx) = dy \wedge dz$ while $\star_V(dt \wedge dx) = -dy \wedge dz$.

The single algebraic fact this solution invokes is property (3) of the star (Bär's (3.4)), which is proved in full on the theorem page and drilled separately in [[Ex - The Hodge Star is an Isometry up to the Sign of the Index]]:

![[Thm - Properties of the Hodge Star in Arbitrary Signature#Statement]]

The property used below is
$$\langle\star\omega,\star\eta\rangle = (-1)^p\,\langle\omega,\eta\rangle \qquad \text{for all } \omega,\eta \in \Lambda^k V^*,$$
the statement that $\star:\Lambda^k V^* \to \Lambda^{n-k} V^*$ is an isometry when $p$ is even and an anti-isometry (isometry up to the global sign $(-1)^p$) when $p$ is odd.

---

# Convergent Strategy

**Problem class.** This is a *reduce-a-wedge-integral-to-an-inner-product* problem, the archetype of the manipulations that convert a variational integrand into something one can integrate by parts. The quantity $\omega \wedge \star\eta$ is an $n$-form, hence a multiple of $\mathrm{vol}$; the task is to identify that multiple. The recognisable signature of the class is that the star appears on exactly one of the two factors under a wedge, and one wants to trade the geometric object $\omega\wedge\star\eta$ for the algebraic scalar $\langle\omega,\eta\rangle$.

**Assumption pattern.** Only two hypotheses do any work. The *defining relation of the star* is used once, and it is the sole bridge between "wedge" and "inner product". The *isometry-up-to-sign property* (3) is used once, to remove the star from inside the inner product it created. Non-degeneracy of the form and the finite dimension of $V$ enter only implicitly, through the fact that $\star$ and the properties recalled above exist at all. The symmetry claim $\omega\wedge\star\eta = \eta\wedge\star\omega$ then needs nothing beyond the *symmetry of $\langle\cdot,\cdot\rangle$*, which every inner product has.

**Theorem routing.** The route is short and forced. Apply the [[Def - Hodge Star in Arbitrary Signature|defining relation]] with $\star\eta$ placed in the second slot, which produces $\omega\wedge\star\eta = \langle\star\omega,\star\eta\rangle\,\mathrm{vol}$; then apply property (3) from [[Thm - Properties of the Hodge Star in Arbitrary Signature]] to rewrite $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$. Symmetry of the resulting expression under $\omega \leftrightarrow \eta$ is immediate from symmetry of the inner product. The integrated statement is obtained by integrating the pointwise identity over $M$, using compactness only to guarantee that the smooth integrand is integrable.

**Key decision point.** The one non-obvious move is *where to insert the star*. The defining relation reads $\alpha\wedge\beta = \langle\star\alpha,\beta\rangle\,\mathrm{vol}$ with $\alpha \in \Lambda^k$ and $\beta \in \Lambda^{n-k}$. In the target expression $\omega\wedge\star\eta$, the second factor $\star\eta$ already lives in $\Lambda^{n-k}$, so it is $\beta$, and $\omega$ is $\alpha$. Recognising that "the star has already been applied to the second slot" is exactly what lets the defining relation fire directly, with no rearrangement. The temptation is to first move the star onto $\omega$ or to expand in a basis; both are unnecessary detours that the defining relation short-circuits.

---

# Legal Operations Used

This solution deploys the following operations, in the sense of the topic page's Legal Operations for the Hodge star (numbers to be reconciled once the [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory|chapter topic page]] is assembled):

1. **Convert a wedge into an inner product through the defining relation.** Whenever an $n$-form $\alpha\wedge\beta$ with $\deg\alpha + \deg\beta = n$ appears, replace it by $\langle\star\alpha,\beta\rangle\,\mathrm{vol}$. Here $\alpha = \omega$ and $\beta = \star\eta$, so no reshaping is needed before the relation applies.

2. **Strip a star out of an inner product using an isometry identity.** Property (3), $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$, removes the star from both arguments at the cost of the global sign $(-1)^p$. This is the operation that turns a star-laden pairing back into a bare one.

3. **Exploit symmetry of the inner product to swap factors.** Because $\langle\omega,\eta\rangle = \langle\eta,\omega\rangle$, the scalar $(-1)^p\langle\omega,\eta\rangle$ is unchanged under $\omega \leftrightarrow \eta$; running the same two operations with the roles of $\omega$ and $\eta$ exchanged yields $\eta\wedge\star\omega = (-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$, giving the two-sided equality.

4. **Integrate a pointwise tensorial identity over a compact manifold.** A pointwise equality between smooth $n$-forms integrates to an equality of integrals; on a compact $M$ the integrands are integrable, and the definition $\langle\omega,\eta\rangle_{L^2} = \int_M\langle\omega,\eta\rangle_g\,\mathrm{vol}_g$ packages the right-hand side.

---

# Hints

> [!note]- Hint 1
> The expression $\omega\wedge\star\eta$ is a top-degree form: $\deg\omega = k$ and $\deg\star\eta = n-k$. So it is *some* scalar multiple of $\mathrm{vol}$, and the whole exercise is to name that scalar. The only tool that converts a wedge of complementary-degree forms into a scalar is the defining relation of the star. Which of $\omega$, $\star\eta$ plays the role of "the thing the star is applied to" in that relation?

> [!note]- Hint 2
> The defining relation is $\alpha\wedge\beta = \langle\star\alpha,\beta\rangle\,\mathrm{vol}$ for $\alpha\in\Lambda^k$, $\beta\in\Lambda^{n-k}$. In $\omega\wedge\star\eta$ take $\alpha = \omega$ and $\beta = \star\eta$ (which is already in $\Lambda^{n-k}$). You get $\omega\wedge\star\eta = \langle\star\omega,\star\eta\rangle\,\mathrm{vol}$. Now you have a star inside an inner product — is there a property that pulls it out?

> [!note]- Hint 3
> Property (3) of the Hodge star says $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$. Substitute. For the second equality $\eta\wedge\star\omega = \omega\wedge\star\eta$, do not compute again from scratch: note that both equal $(-1)^p$ times an inner product, and that the inner product is symmetric.

> [!note]- Hint 4
> For the $L^2$ statement, the pointwise identity $\omega\wedge\star\eta = (-1)^p\langle\omega,\eta\rangle_g\,\mathrm{vol}_g$ holds at every point of $M$, with $\star$, $\langle\cdot,\cdot\rangle_g$ and $\mathrm{vol}_g$ the fibrewise operators of the metric. Integrate both sides over $M$. Compactness of $M$ guarantees the smooth $n$-form $\omega\wedge\star\eta$ has finite integral; the factor $(-1)^p$ is a constant and comes outside.

---

# Solution

The proof is two applications of results already on the shelf: the defining relation of the star inserts a star into an inner product, and property (3) takes it back out at the cost of $(-1)^p$. Symmetry of the whole expression is then symmetry of the inner product. The manifold statement is nothing more than integrating the pointwise identity, with compactness ensuring the integral exists.

**Step 1: Apply the defining relation with $\star\eta$ in the second slot.**

The form $\omega\wedge\star\eta$ is expressed through the induced inner product as $\langle\star\omega,\star\eta\rangle\,\mathrm{vol}$.

> [!note]- Derivation
> Fix $\omega,\eta \in \Lambda^k V^*$. Then $\omega \in \Lambda^k V^*$ and $\star\eta \in \Lambda^{n-k} V^*$, so the pair $(\omega,\star\eta)$ has complementary degrees $k$ and $n-k$ and the [[Def - Hodge Star in Arbitrary Signature|defining relation]] of the star applies with $\alpha = \omega$, $\beta = \star\eta$:
> $$\omega \wedge \star\eta = \langle\star\omega,\star\eta\rangle\,\mathrm{vol} \qquad \text{(defining relation of }\star\text{, with }\alpha=\omega,\ \beta=\star\eta).$$
> No rearrangement was needed: the star is already applied to the factor $\eta$ that sits in the second slot, which is precisely the position the defining relation requires.

**Step 2: Remove the star from the inner product via property (3).**

The pairing $\langle\star\omega,\star\eta\rangle$ equals $(-1)^p\langle\omega,\eta\rangle$, giving $\omega\wedge\star\eta = (-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$.

> [!note]- Derivation
> By property (3) of [[Thm - Properties of the Hodge Star in Arbitrary Signature|the Hodge star]] — the statement that $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$ for all $\omega,\eta\in\Lambda^kV^*$, which holds because $\star$ maps a generalized orthonormal basis of $\Lambda^kV^*$ to a generalized orthonormal basis of $\Lambda^{n-k}V^*$ multiplying the product of signs by $(-1)^p$ — we substitute into the result of Step 1:
> $$\omega \wedge \star\eta = \langle\star\omega,\star\eta\rangle\,\mathrm{vol} = (-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol} \qquad \text{(Step 1; then property (3))}.$$
> This establishes the first of the two claimed equalities, $\omega\wedge\star\eta = (-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$.

**Step 3: Obtain the symmetric form by exchanging $\omega$ and $\eta$.**

Running Steps 1 and 2 with $\omega$ and $\eta$ interchanged, and using symmetry of the inner product, gives $\eta\wedge\star\omega = (-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$ as well.

> [!note]- Derivation
> The computation of Steps 1 and 2 used nothing about $\omega$ and $\eta$ beyond their both lying in $\Lambda^k V^*$, so it holds verbatim with their roles exchanged:
> $$\eta \wedge \star\omega = \langle\star\eta,\star\omega\rangle\,\mathrm{vol} = (-1)^p\,\langle\eta,\omega\rangle\,\mathrm{vol} \qquad \text{(defining relation with }\alpha=\eta,\ \beta=\star\omega\text{; then property (3))}.$$
> The induced inner product is **symmetric**, $\langle\eta,\omega\rangle = \langle\omega,\eta\rangle$ (each term of its defining sum is symmetric under exchanging its two form-arguments), so
> $$\eta \wedge \star\omega = (-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol}.$$
> Combining this with Step 2, both $\omega\wedge\star\eta$ and $\eta\wedge\star\omega$ equal the same $n$-form $(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$, hence
> $$\omega \wedge \star\eta = \eta \wedge \star\omega = (-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol}.$$

**Step 4: Integrate over a compact manifold to obtain the $L^2$ identity.**

Integrating the pointwise identity over $M$ turns the wedge integral into the signature-corrected $L^2$ inner product.

> [!note]- Derivation
> Let $(M,g)$ be oriented, compact, and semi-Riemannian of dimension $n$ and constant index $p$, and let $\omega,\eta \in \Omega^k(M)$ be smooth $k$-forms. At each point $x \in M$ the tangent space $T_xM$ with the bilinear form $g_x$ is a semi-Euclidean space of dimension $n$ and index $p$, and the fibrewise Hodge star, inner product, and volume form are exactly the linear-algebraic operators to which Steps 1–3 apply. Hence, as an identity of smooth $n$-forms on $M$,
> $$\omega \wedge \star\eta = (-1)^p\,\langle\omega,\eta\rangle_g\,\mathrm{vol}_g \qquad \text{(Steps 1–3, applied pointwise on each } T_xM).$$
> Both sides are smooth $n$-forms; because $M$ is **compact**, every smooth $n$-form is integrable, so we may integrate the identity over the oriented manifold $M$:
> $$\int_M \omega \wedge \star\eta = \int_M (-1)^p\,\langle\omega,\eta\rangle_g\,\mathrm{vol}_g = (-1)^p \int_M \langle\omega,\eta\rangle_g\,\mathrm{vol}_g \qquad \text{(integrate the pointwise identity; }(-1)^p\text{ is a constant)}.$$
> By the definition $\langle\omega,\eta\rangle_{L^2} = \int_M \langle\omega,\eta\rangle_g\,\mathrm{vol}_g$ this is
> $$\int_M \omega \wedge \star\eta = (-1)^p\,\langle\omega,\eta\rangle_{L^2},$$
> as required.

> [!note]- Complete formal solution
> **Claim.** Let $V$ be an oriented $n$-dimensional real vector space with a non-degenerate symmetric bilinear form of index $p$, and $\star$ the associated Hodge star. Then for all $\omega,\eta \in \Lambda^k V^*$,
> $$\omega \wedge \star\eta = \eta \wedge \star\omega = (-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol}.$$
> Consequently, on an oriented compact semi-Riemannian manifold $(M,g)$ of dimension $n$ and index $p$, $\int_M \omega\wedge\star\eta = (-1)^p\langle\omega,\eta\rangle_{L^2}$ for all $\omega,\eta \in \Omega^k(M)$.
>
> *Proof.* Fix $\omega,\eta \in \Lambda^k V^*$. Since $\star\eta \in \Lambda^{n-k}V^*$, the defining relation of the Hodge star, $\alpha\wedge\beta = \langle\star\alpha,\beta\rangle\,\mathrm{vol}$ for $\alpha\in\Lambda^kV^*$ and $\beta\in\Lambda^{n-k}V^*$, applies with $\alpha=\omega$ and $\beta=\star\eta$:
> $$\omega\wedge\star\eta = \langle\star\omega,\star\eta\rangle\,\mathrm{vol}.$$
> By property (3) of the Hodge star, $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$, whence
> $$\omega\wedge\star\eta = (-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol}. \tag{$*$}$$
> Interchanging $\omega$ and $\eta$ in $(*)$ gives $\eta\wedge\star\omega = (-1)^p\langle\eta,\omega\rangle\,\mathrm{vol}$; since $\langle\cdot,\cdot\rangle$ is symmetric, $\langle\eta,\omega\rangle = \langle\omega,\eta\rangle$, so $\eta\wedge\star\omega = (-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$. Thus $\omega\wedge\star\eta$ and $\eta\wedge\star\omega$ are equal, and both equal $(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$.
>
> For the integrated statement, let $(M,g)$ be oriented, compact, semi-Riemannian of dimension $n$ and constant index $p$, and $\omega,\eta \in \Omega^k(M)$. Applying $(*)$ to $(T_xM,g_x)$ at each $x$ yields the identity of smooth $n$-forms $\omega\wedge\star\eta = (-1)^p\langle\omega,\eta\rangle_g\,\mathrm{vol}_g$. Compactness of $M$ makes each side integrable, and integrating,
> $$\int_M \omega\wedge\star\eta = (-1)^p\int_M \langle\omega,\eta\rangle_g\,\mathrm{vol}_g = (-1)^p\,\langle\omega,\eta\rangle_{L^2}.\qquad\blacksquare$$

> [!warning] Illegal but tempting shortcut: assuming $\int_M \omega\wedge\star\eta$ is symmetric in the Lorentzian sign
> It is tempting to conclude directly from graded-commutativity of the wedge product, $\omega\wedge\star\eta = (-1)^{k(n-k)}\star\eta\wedge\omega$, that $\int_M\omega\wedge\star\eta$ is symmetric, hoping the sign $(-1)^{k(n-k)}$ vanishes. But graded-commutativity relates $\omega\wedge\star\eta$ to $\star\eta\wedge\omega$, not to $\eta\wedge\star\omega$ — the star sits on the wrong factor — and its sign $(-1)^{k(n-k)}$ is generally not $+1$. The genuine symmetry $\omega\wedge\star\eta = \eta\wedge\star\omega$ comes from the symmetry of the *inner product* after both stars have been converted, not from any symmetry of the wedge; and the correct global sign is $(-1)^p$, controlled by the *index*, not by $k(n-k)$. Conflating the two signs is precisely the error the three-way convention callout above is meant to prevent.

> [!note]- Independent check on Minkowski 2-forms
> Take $V = \mathbb{R}^{1,3}$ with $(-,+,+,+)$, so $n=4$, $p=1$, and $\omega = \eta = dt\wedge dx$ (a $2$-form, $k=2$). From Bär's star table, $\star(dt\wedge dx) = dy\wedge dz$, so the left-hand side is $\omega\wedge\star\eta = (dt\wedge dx)\wedge(dy\wedge dz) = dt\wedge dx\wedge dy\wedge dz = \mathrm{vol}$. The right-hand side is $(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$; here $\langle dt\wedge dx, dt\wedge dx\rangle = \epsilon_t\epsilon_x = (-1)(+1) = -1$ and $p=1$, so $(-1)^1\cdot(-1)\,\mathrm{vol} = +\mathrm{vol}$. The two sides agree. Note that the individual signs $\langle\omega,\eta\rangle = -1$ and $(-1)^p = -1$ each differ from the Euclidean expectation, and it is their product that restores $+\mathrm{vol}$ — the reason the bare wedge integral, not the inner product, is what appears in the action.

---

# Key Takeaways

**The wedge integral $\int_M\omega\wedge\star\eta$ *is* the $L^2$ inner product, up to the fixed sign $(-1)^p$, and this is the identity that makes variational calculus on forms possible.** Every action functional built from the field strength — the electromagnetic action $\tfrac12\int_M F\wedge\star F$, the Yang–Mills action $\tfrac12\int_M\langle F\wedge\star F\rangle$ — is, by this result, $\pm\tfrac12$ the squared $L^2$-norm of the curvature. The reason this matters operationally is that $L^2$ pairings are symmetric and admit integration by parts, whereas a raw wedge integral advertises neither. When one perturbs a connection $A \mapsto A + t\eta$ and differentiates the action, the cross term is $\int_M d\eta\wedge\star F$; the present identity is what certifies that this equals a genuine $L^2$ pairing $\pm\langle d\eta, F\rangle_{L^2}$, so that moving $d$ onto $\star F$ (via Stokes and the codifferential) is a legitimate adjoint operation and produces the field equation $d\star F = 0$ or $d^\nabla\star F = 0$. Whenever a variational problem lives on differential forms, expect this identity to be the hinge on which the Euler–Lagrange equation turns.

**Symmetry of the pairing traces back to symmetry of the underlying inner product, not to any symmetry of the wedge product — and the correct global sign is governed by the index $p$, never by $k(n-k)$.** The trigger for reaching for this result is the appearance of $\omega\wedge\star\eta$ where one wants to swap the two forms; the transferable diagnostic is to convert *both* stars away first (defining relation, then property (3)) and only then invoke symmetry, because symmetry is a property of $\langle\cdot,\cdot\rangle$ and is invisible at the level of wedges. The sign $(-1)^p$ is the same signature correction that appears in the double-star formula $\star\star = (-1)^{k(n-k)+p}$ and in the isometry property $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$; in Riemannian signature it disappears, which is why the Riemannian formula $\int_M\omega\wedge\star\eta = \langle\omega,\eta\rangle_{L^2}$ carries no sign and why one must be vigilant when passing to Lorentzian spacetime, where a stray $-1$ changes the sign of an energy.

**This computation is also the concrete proof that the series' star $\star_B$ and the Riemannian-chapter star $\star_V$ differ by exactly $(-1)^p$.** The vault's Hodge Theory I operator is defined by $\alpha\wedge\star_V\beta = \langle\alpha,\beta\rangle\,\mathrm{vol}$; the identity proved here reads $\alpha\wedge\star_B\beta = (-1)^p\langle\alpha,\beta\rangle\,\mathrm{vol} = \langle\alpha,\beta\rangle\cdot(-1)^p\,\mathrm{vol}$, so comparing the two defining relations forces $\star_B\beta = (-1)^p\star_V\beta$. This is why chapters VIII–XI, which work in Riemannian signature, may cite the Hodge Theory I pages freely (there $p=0$ and the two stars coincide), while chapter VII's Lorentzian pages must keep the $(-1)^p$ explicit. The reusable lesson: when two texts define "the Hodge star" by superficially different wedge relations, the discrepancy is always a sign, and pinning it down is a one-line computation with the defining relation — do it once, record it in a convention callout, and never guess it again. A companion drill on the sign machinery is [[Ex - The Hodge Star is an Isometry up to the Sign of the Index]], and the double-star sign is isolated in [[Ex - Double Star Sign in Arbitrary Signature]].
