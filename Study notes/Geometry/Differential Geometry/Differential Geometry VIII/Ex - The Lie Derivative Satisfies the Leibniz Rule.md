---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Lie Derivative of a Differential Form"
  - "Thm - Cartan's Magic Formula"
  - "Def - The Wedge Product on a Manifold"
  - "Def - Pullback of a Differential Form on a Manifold"
tags: [geometry, differential-geometry]
---

# Problem Statement

Prove that the Lie derivative of differential forms satisfies the (ungraded) Leibniz rule with respect to the wedge product: for any smooth vector field $X$ on a smooth manifold $M$ and any smooth differential forms $\omega \in \Omega^k(M)$, $\eta \in \Omega^\ell(M)$,
$$\mathcal{L}_X(\omega \wedge \eta) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta.$$

Note that this rule is **ungraded** (no sign $(-1)^k$) — unlike the Leibniz rule for $d$ or $\iota_X$, which carry such signs.

(a) Prove the identity using the flow definition $\mathcal{L}_X = \frac{d}{dt}|_{t=0}(\phi^X_t)^*$ and the fact that pullback respects the wedge product.

(b) Prove the identity using Cartan's magic formula and the graded Leibniz rules for $d$ and $\iota_X$. Show that the sign cross-terms cancel, leaving the ungraded answer.

**Recall:**

![[Thm - Cartan's Magic Formula#Statement]]

The Lie derivative via flow: $\mathcal{L}_X\omega = \frac{d}{dt}\big|_{t=0}(\phi^X_t)^*\omega$.

Pullback respects wedge: $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$ (see [[Def - Pullback of a Differential Form on a Manifold]]).

Graded Leibniz for $d$: $d(\omega \wedge \eta) = d\omega \wedge \eta + (-1)^k\omega \wedge d\eta$ for $\omega \in \Omega^k$.

Graded anti-derivation for $\iota_X$: $\iota_X(\omega \wedge \eta) = \iota_X\omega \wedge \eta + (-1)^k\omega \wedge \iota_X\eta$ for $\omega \in \Omega^k$.

---

# Convergent Strategy

**Problem class:** This is a "verify a Leibniz rule" problem. Two proof routes are available: via the flow definition and pullback (which gives the ungraded result immediately), and via Cartan's formula plus the graded Leibniz rules for $d$ and $\iota_X$ (where the sign cancellations are the substantive step).

**Assumption pattern:** $X$ is a smooth vector field; $\omega, \eta$ are smooth forms of arbitrary degrees. The structure available is the flow of $X$ (smooth in $t$ for each fixed point) and the algebraic operations $d, \iota_X$ on $\Omega^\bullet$. Both routes give the same Leibniz rule because the underlying operator $\mathcal{L}_X$ is uniquely determined.

**Theorem routing:** Route (a) uses the [[Def - Pullback of a Differential Form on a Manifold|pullback]] respecting wedge, plus the product rule $\frac{d}{dt}(\omega(t) \wedge \eta(t)) = \dot\omega(t) \wedge \eta(t) + \omega(t) \wedge \dot\eta(t)$ for $1$-parameter families of forms. Route (b) uses [[Thm - Cartan's Magic Formula]] applied to $\omega \wedge \eta$ and the graded Leibniz rules for $d$ and $\iota_X$ — the sign tracking is the substantive work.

**Key decision point:** Recognizing that the Leibniz rule for $\mathcal{L}_X$ is *ungraded*, while the rules for $d$ and $\iota_X$ are graded. The reason is that $\mathcal{L}_X$ has *degree* $0$ as an operator on $\Omega^\bullet$ (it preserves the degree of the form), whereas $d$ and $\iota_X$ change the degree by $\pm 1$ — so $d$ and $\iota_X$ carry signs when passing through a form of degree $k$, while $\mathcal{L}_X$ does not.

---

# Legal Operations Used

1. **Use Cartan's magic formula instead of computing flows** (operation 2) — in route (b), Cartan's formula is the central tool.

2. **Exploit naturality: $F^*$ commutes with everything that matters** (operation 7) — in route (a), pullback respects the wedge product, which is what makes the flow definition propagate to the Leibniz rule.

---

# Hints

> [!note]- Hint 1
> Route (a): $(\phi^X_t)^*(\omega \wedge \eta) = (\phi^X_t)^*\omega \wedge (\phi^X_t)^*\eta$. Differentiate this in $t$ at $t = 0$ using the product rule.

> [!note]- Hint 2
> Route (b): apply Cartan to $\omega \wedge \eta$: $\mathcal{L}_X(\omega \wedge \eta) = d\iota_X(\omega \wedge \eta) + \iota_X d(\omega \wedge \eta)$. Expand each using the graded Leibniz rules.

> [!note]- Hint 3
> In Route (b), the four cross-terms (sign-positive from $d \circ \iota_X$, sign-negative from $\iota_X \circ d$, etc.) cancel pairwise, leaving the four direct terms — two of which combine to $\mathcal{L}_X\omega \wedge \eta$ and the other two to $\omega \wedge \mathcal{L}_X\eta$.

---

# Solution

The proof has two routes. Route (a) uses the flow definition and pullback. Route (b) uses Cartan's formula and the graded Leibniz rules.

**Route (a): via the flow definition.**

By the pullback identity, $(\phi^X_t)^*(\omega \wedge \eta) = (\phi^X_t)^*\omega \wedge (\phi^X_t)^*\eta$.

Differentiate both sides at $t = 0$. The left side gives $\mathcal{L}_X(\omega \wedge \eta)$ by definition. The right side, by the product rule for the derivative of a wedge product of $t$-dependent forms (which follows from bilinearity of the wedge over $\mathbb{R}$):
$$\frac{d}{dt}\bigg|_{t=0}((\phi^X_t)^*\omega \wedge (\phi^X_t)^*\eta) = \left(\frac{d}{dt}\bigg|_{t=0}(\phi^X_t)^*\omega\right) \wedge \eta + \omega \wedge \left(\frac{d}{dt}\bigg|_{t=0}(\phi^X_t)^*\eta\right) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta.$$

(At $t = 0$, $(\phi^X_0)^*\omega = \omega$ and $(\phi^X_0)^*\eta = \eta$, so the "evaluation at $t = 0$" of the un-differentiated factors gives $\omega$ and $\eta$.)

So $\mathcal{L}_X(\omega \wedge \eta) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta$. ✓

> [!note]- Derivation
> $(\phi^X_t)^*(\omega \wedge \eta) = (\phi^X_t)^*\omega \wedge (\phi^X_t)^*\eta$ by the pullback-respects-wedge identity.
>
> Let $\Omega(t) = (\phi^X_t)^*\omega$ and $E(t) = (\phi^X_t)^*\eta$. Both are smooth families of forms in $t$. The wedge is $\mathbb{R}$-bilinear, hence the product rule for differentiation gives
> $$\frac{d}{dt}(\Omega(t) \wedge E(t)) = \dot\Omega(t) \wedge E(t) + \Omega(t) \wedge \dot E(t).$$
> Evaluate at $t = 0$: $\Omega(0) = \omega$, $E(0) = \eta$, $\dot\Omega(0) = \mathcal{L}_X\omega$, $\dot E(0) = \mathcal{L}_X\eta$. So
> $$\mathcal{L}_X(\omega \wedge \eta) = \frac{d}{dt}\bigg|_0(\phi^X_t)^*(\omega \wedge \eta) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta. \quad\Box$$

**Route (b): via Cartan's magic formula.**

By Cartan, $\mathcal{L}_X(\omega \wedge \eta) = d\iota_X(\omega \wedge \eta) + \iota_X d(\omega \wedge \eta)$. Expand each term using the graded Leibniz rules.

**First term:** $\iota_X(\omega \wedge \eta) = \iota_X\omega \wedge \eta + (-1)^k\omega \wedge \iota_X\eta$ for $\omega \in \Omega^k$. So
$$d(\iota_X(\omega \wedge \eta)) = d(\iota_X\omega \wedge \eta) + (-1)^k d(\omega \wedge \iota_X\eta).$$

Apply graded Leibniz for $d$ to each: $\iota_X\omega$ has degree $k - 1$ and $\omega$ has degree $k$, so the sign in the second term is $(-1)^k$, but in the first term the sign on the wedge with $\eta$ is $(-1)^{k-1}$. Specifically:
$$d(\iota_X\omega \wedge \eta) = d(\iota_X\omega) \wedge \eta + (-1)^{k-1}\iota_X\omega \wedge d\eta,$$
$$d(\omega \wedge \iota_X\eta) = d\omega \wedge \iota_X\eta + (-1)^k \omega \wedge d(\iota_X\eta).$$

Combining:
$$d(\iota_X(\omega \wedge \eta)) = d\iota_X\omega \wedge \eta + (-1)^{k-1}\iota_X\omega \wedge d\eta + (-1)^k d\omega \wedge \iota_X\eta + (-1)^{2k}\omega \wedge d\iota_X\eta$$
$$= d\iota_X\omega \wedge \eta - (-1)^k \iota_X\omega \wedge d\eta + (-1)^k d\omega \wedge \iota_X\eta + \omega \wedge d\iota_X\eta.$$

**Second term:** $d(\omega \wedge \eta) = d\omega \wedge \eta + (-1)^k \omega \wedge d\eta$. So
$$\iota_X d(\omega \wedge \eta) = \iota_X(d\omega \wedge \eta) + (-1)^k \iota_X(\omega \wedge d\eta).$$

Apply graded $\iota_X$-Leibniz to each: $d\omega$ has degree $k + 1$ and $\omega$ has degree $k$, so:
$$\iota_X(d\omega \wedge \eta) = \iota_X(d\omega) \wedge \eta + (-1)^{k+1} d\omega \wedge \iota_X\eta,$$
$$\iota_X(\omega \wedge d\eta) = \iota_X\omega \wedge d\eta + (-1)^k \omega \wedge \iota_X(d\eta).$$

Combining:
$$\iota_X d(\omega \wedge \eta) = \iota_X d\omega \wedge \eta + (-1)^{k+1} d\omega \wedge \iota_X\eta + (-1)^k \iota_X\omega \wedge d\eta + (-1)^{2k}\omega \wedge \iota_X d\eta$$
$$= \iota_X d\omega \wedge \eta - (-1)^k d\omega \wedge \iota_X\eta + (-1)^k \iota_X\omega \wedge d\eta + \omega \wedge \iota_X d\eta.$$

**Sum of the two:** Add the expanded $d\iota_X(\omega \wedge \eta)$ and $\iota_X d(\omega \wedge \eta)$:

$d\iota_X\omega \wedge \eta + \iota_X d\omega \wedge \eta + [-(-1)^k + (-1)^k]\iota_X\omega \wedge d\eta + [(-1)^k - (-1)^k]d\omega \wedge \iota_X\eta + \omega \wedge d\iota_X\eta + \omega \wedge \iota_X d\eta$

$= (d\iota_X + \iota_X d)\omega \wedge \eta + 0 + 0 + \omega \wedge (d\iota_X + \iota_X d)\eta$

$= \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta$. ✓

The cross-terms $\iota_X\omega \wedge d\eta$ and $d\omega \wedge \iota_X\eta$ cancel pairwise.

> [!note]- Derivation
> Apply Cartan's formula to $\omega \wedge \eta$:
> $$\mathcal{L}_X(\omega \wedge \eta) = d(\iota_X(\omega \wedge \eta)) + \iota_X(d(\omega \wedge \eta)).$$
>
> Expand $\iota_X(\omega \wedge \eta) = \iota_X\omega \wedge \eta + (-1)^k\omega \wedge \iota_X\eta$.
>
> Apply $d$:
> $d(\iota_X\omega \wedge \eta) = d(\iota_X\omega) \wedge \eta + (-1)^{k-1}\iota_X\omega \wedge d\eta$.
> $d((-1)^k\omega \wedge \iota_X\eta) = (-1)^k d\omega \wedge \iota_X\eta + (-1)^k (-1)^k \omega \wedge d(\iota_X\eta) = (-1)^k d\omega \wedge \iota_X\eta + \omega \wedge d(\iota_X\eta)$.
>
> Sum: $d\iota_X(\omega \wedge \eta) = d\iota_X\omega \wedge \eta + (-1)^{k-1}\iota_X\omega \wedge d\eta + (-1)^k d\omega \wedge \iota_X\eta + \omega \wedge d\iota_X\eta$.
>
> Expand $d(\omega \wedge \eta) = d\omega \wedge \eta + (-1)^k \omega \wedge d\eta$.
>
> Apply $\iota_X$:
> $\iota_X(d\omega \wedge \eta) = \iota_X(d\omega) \wedge \eta + (-1)^{k+1} d\omega \wedge \iota_X\eta$.
> $\iota_X((-1)^k \omega \wedge d\eta) = (-1)^k \iota_X\omega \wedge d\eta + (-1)^{2k}\omega \wedge \iota_X(d\eta) = (-1)^k \iota_X\omega \wedge d\eta + \omega \wedge \iota_X d\eta$.
>
> Sum: $\iota_X d(\omega \wedge \eta) = \iota_X d\omega \wedge \eta + (-1)^{k+1} d\omega \wedge \iota_X\eta + (-1)^k \iota_X\omega \wedge d\eta + \omega \wedge \iota_X d\eta$.
>
> **Add the two sums:** The $d\omega \wedge \iota_X\eta$ terms have coefficients $(-1)^k$ from the first sum and $(-1)^{k+1} = -(-1)^k$ from the second; they cancel. The $\iota_X\omega \wedge d\eta$ terms have coefficients $(-1)^{k-1} = -(-1)^k$ from the first and $(-1)^k$ from the second; they cancel.
>
> Remaining: $(d\iota_X\omega + \iota_X d\omega) \wedge \eta + \omega \wedge (d\iota_X\eta + \iota_X d\eta) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta$ by Cartan applied to each factor.

> [!note]- Complete formal solution
> Two proofs are given.
>
> **Route (a) via flow:** $(\phi^X_t)^*(\omega \wedge \eta) = (\phi^X_t)^*\omega \wedge (\phi^X_t)^*\eta$ by the wedge-respecting property of pullback. Differentiate at $t = 0$ using the product rule:
> $$\mathcal{L}_X(\omega \wedge \eta) = (\mathcal{L}_X\omega) \wedge \eta + \omega \wedge (\mathcal{L}_X\eta).$$
>
> **Route (b) via Cartan:** Expand $\mathcal{L}_X(\omega \wedge \eta) = d\iota_X(\omega \wedge \eta) + \iota_X d(\omega \wedge \eta)$ using the graded Leibniz rules for $\iota_X$ and $d$. The cross-terms $\iota_X\omega \wedge d\eta$ and $d\omega \wedge \iota_X\eta$ each appear twice with opposite signs and cancel. The remaining four terms regroup as $(d\iota_X + \iota_X d)\omega \wedge \eta + \omega \wedge (d\iota_X + \iota_X d)\eta = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta$.
>
> $\blacksquare$

---

# Key Takeaways

**The Lie derivative is *ungraded* on the wedge product, despite $d$ and $\iota_X$ each being *graded*.** This is because $\mathcal{L}_X$ has *degree zero* — it preserves the degree of a form. So passing $\mathcal{L}_X$ through a form $\omega$ in a wedge product costs no signs, whereas passing $d$ or $\iota_X$ through $\omega$ costs $(-1)^{\deg\omega}$. The structural reason: the sign comes from anticommuting the operator past the basic $1$-forms of $\omega$, and a degree-zero operator does not "occupy a slot" that could be anticommuted. Cartan's formula combines two graded operators ($d$, $\iota_X$) into an ungraded one ($\mathcal{L}_X$), and the signs cancel in exactly the right way to produce the ungraded Leibniz rule.

**Two distinct proof routes give the same result — and the cleaner proof depends on context.** Route (a) is shorter and more conceptual: pullback respects wedge, differentiate, done. Route (b) is longer and more technical, but it illustrates the algebraic mechanism (how the graded signs of $d$ and $\iota_X$ cancel) and is the route one uses when proving more elaborate identities that involve composites of Lie derivatives. Both routes are worth knowing; pick the one that fits the problem at hand. The trigger pattern: a problem involving the flow of $X$ explicitly → route (a); a problem involving algebraic identities in the Cartan calculus → route (b).

**The ungraded Leibniz rule propagates to higher-order products by iteration.** $\mathcal{L}_X(\omega_1 \wedge \omega_2 \wedge \omega_3) = \mathcal{L}_X\omega_1 \wedge \omega_2 \wedge \omega_3 + \omega_1 \wedge \mathcal{L}_X\omega_2 \wedge \omega_3 + \omega_1 \wedge \omega_2 \wedge \mathcal{L}_X\omega_3$, by iterating the binary Leibniz rule. In general, $\mathcal{L}_X(\omega_1 \wedge \cdots \wedge \omega_n) = \sum_i \omega_1 \wedge \cdots \wedge \mathcal{L}_X\omega_i \wedge \cdots \wedge \omega_n$ — the "derivative landing on each factor" pattern, with no signs. This is the same pattern as the Leibniz rule for the derivative of a product of functions, generalized to forms.

**The Lie derivative is a *derivation* of the wedge algebra, with respect to the graded-commutative structure.** A derivation is an additive map $D : A \to A$ on an algebra satisfying $D(ab) = (Da)b + a(Db)$ — the ungraded Leibniz rule. $\mathcal{L}_X$ is such a derivation on $\Omega^\bullet(M)$. By contrast, $d$ and $\iota_X$ are **anti-derivations** (or graded derivations), satisfying the rule with a sign factor. The trio $d, \iota_X, \mathcal{L}_X$ thus consists of two anti-derivations and one derivation, with Cartan's formula expressing the third in terms of the first two. The whole framework of the Cartan calculus organizes operations on $\Omega^\bullet(M)$ into derivations and anti-derivations.
