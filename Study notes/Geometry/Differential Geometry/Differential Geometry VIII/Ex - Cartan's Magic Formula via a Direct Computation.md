---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Thm - Cartan's Magic Formula"
  - "Def - Lie Derivative of a Differential Form"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Interior Product (Contraction with a Vector Field)"
tags: [geometry, differential-geometry]
---

# Problem Statement

Verify Cartan's magic formula $\mathcal{L}_X = d\iota_X + \iota_X d$ on $\Omega^k(M)$ for $k = 0$ and $k = 1$ by direct computation.

(a) Verify $\mathcal{L}_X f = (d\iota_X + \iota_X d)f$ for any smooth function $f \in C^\infty(M)$, using the flow definition $\mathcal{L}_X f = \frac{d}{dt}|_{t=0}(f \circ \phi^X_t)$ on the left side.

(b) For a $1$-form $\omega = u\,dv$ (with $u, v \in C^\infty(M)$), compute both $\mathcal{L}_X(u\,dv)$ and $(d\iota_X + \iota_X d)(u\,dv)$ from the definitions and show they are equal. The left side is computed using the Leibniz rule for $\mathcal{L}_X$; the right side using the Leibniz rules for $d$ and $\iota_X$.

(c) Conclude by linearity that Cartan's formula holds on all $1$-forms.

(d) Apply Cartan's formula to give a one-line proof that $\mathcal{L}_X d = d \mathcal{L}_X$ on $\Omega^\bullet(M)$.

**Recall:**

![[Thm - Cartan's Magic Formula#Statement]]

The Lie derivative on a function: $\mathcal{L}_X f = X(f) = df(X)$.

The interior product on a $1$-form: $\iota_X\omega = \omega(X)$, which is a $0$-form (function).

Graded Leibniz for $d$: $d(\omega \wedge \eta) = d\omega \wedge \eta + (-1)^{\deg\omega}\omega \wedge d\eta$.

Graded anti-derivation for $\iota_X$: $\iota_X(\omega \wedge \eta) = \iota_X\omega \wedge \eta + (-1)^{\deg\omega}\omega \wedge \iota_X\eta$.

Ungraded Leibniz for $\mathcal{L}_X$ on wedges: $\mathcal{L}_X(\omega \wedge \eta) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta$.

---

# Convergent Strategy

**Problem class:** This is a "verify an algebraic identity by direct computation" problem, drilling Cartan's magic formula. The route is to compute both sides of the formula on a generating set of forms (functions in (a); basic $1$-forms $u\,dv$ in (b)) and match.

**Assumption pattern:** $X$ is a smooth vector field; $\omega = u\,dv$ is a basic $1$-form built from two smooth functions. Both sides use the standard Leibniz rules for $d$, $\iota_X$, $\mathcal{L}_X$. The "magic" is that the bookkeeping works out: the various Leibniz cross-terms exactly cancel to give the same answer.

**Theorem routing:** Use the [[Def - Lie Derivative of a Differential Form|flow definition of ℒ_X]] on the left side; use the [[Def - Exterior Derivative on a Manifold|chart formula for d]] and the [[Def - Interior Product (Contraction with a Vector Field)|definition of ι_X]] on the right side. The Leibniz rules for each operator are what enable the propagation from a single basic form to all forms.

**Key decision point:** The strategy of taking $\omega = u\,dv$ (a single basic $1$-form built from two functions) is what makes the bookkeeping manageable. A general $1$-form on a chart is $\sum_i u_i\,dx^i$, but each term has the form "function times $d$ of another function", so it suffices to check the formula on $u\,dv$ and use linearity.

---

# Legal Operations Used

1. **Use Cartan's magic formula instead of computing flows** (operation 2) — even though we are *proving* Cartan's formula here, we are using its right side $(d\iota_X + \iota_X d)\omega$ as the *target* of the computation. The left side $\mathcal{L}_X\omega$ uses the flow.

2. **Use $d^2 = 0$ as a one-line shortcut** (operation 4) — appears in the cancellation of $d^2(v)$ terms in part (b).

---

# Hints

> [!note]- Hint 1
> For (a), the right side is $\iota_X(df) + d(\iota_X f) = df(X) + d(0) = X(f)$. The left side is $X(f)$ by the chain rule. Both sides agree.

> [!note]- Hint 2
> For (b), expand $\mathcal{L}_X(u\,dv) = \mathcal{L}_X u \cdot dv + u \cdot \mathcal{L}_X(dv)$ using the ungraded Leibniz rule for $\mathcal{L}_X$ on wedges.

> [!note]- Hint 3
> $\mathcal{L}_X(dv) = d(\mathcal{L}_X v) = d(Xv)$ — this is because $\mathcal{L}_X$ commutes with $d$ on functions (a fact provable from the flow definition independently of Cartan's formula).

> [!note]- Hint 4
> For the right side in (b), $\iota_X(u\,dv) = u \cdot \iota_X(dv) = u \cdot dv(X) = u \cdot Xv$. Then $d(\iota_X(u\,dv)) = d(u \cdot Xv) = du \cdot Xv + u \cdot d(Xv)$.

> [!note]- Hint 5
> For (d), apply Cartan's formula to $d\omega$: $\mathcal{L}_X(d\omega) = (d\iota_X + \iota_X d)(d\omega) = d\iota_X(d\omega) + \iota_X d^2\omega = d\iota_X d\omega + 0$. Also $d(\mathcal{L}_X\omega) = d(d\iota_X\omega + \iota_X d\omega) = 0 + d\iota_X d\omega$. The two sides agree.

---

# Solution

The proof has four steps. Step 1 verifies Cartan's formula on functions ($k = 0$). Step 2 verifies it on basic $1$-forms $u\,dv$. Step 3 propagates by linearity. Step 4 derives the commutation $\mathcal{L}_X d = d\mathcal{L}_X$ in one line.

**Step 1: Cartan's formula on a function $f$.**

Compute the right side: $\iota_X f = 0$ (no degree-$(-1)$ forms), so $d\iota_X f = 0$. $\iota_X(df) = df(X) = X(f)$. So $(d\iota_X + \iota_X d)f = X(f)$.

Compute the left side: $\mathcal{L}_X f = \frac{d}{dt}\big|_{t=0}(\phi^X_t)^*f = \frac{d}{dt}\big|_{t=0}(f \circ \phi^X_t)$. At $t = 0$, the chain rule gives $\frac{d}{dt}|_{t=0}(f \circ \phi^X_t)(p) = df_p(X_p) = (X(f))(p)$.

Both sides equal $X(f)$. ✓

> [!note]- Derivation
> Right side: $\iota_X f = 0$ on functions (by convention, since interior product is degree-decreasing and there are no $(-1)$-forms). So the first term $d(\iota_X f) = 0$. The second term: $\iota_X(df) = (df)(X) = X(f)$, the directional derivative.
>
> Left side: $\mathcal{L}_X f = \frac{d}{dt}\big|_{t=0}(\phi^X_t)^*f$. By definition, $(\phi^X_t)^*f = f \circ \phi^X_t$. At $t = 0$, $\phi^X_0 = \operatorname{id}$, and $\frac{d}{dt}|_{t=0}\phi^X_t(p) = X_p$ (the defining property of the flow). By the chain rule, $\frac{d}{dt}|_{t=0}f(\phi^X_t(p)) = df_p\left(\frac{d}{dt}|_{t=0}\phi^X_t(p)\right) = df_p(X_p) = X_p(f)$.
>
> So both sides equal $X(f)$, and Cartan's formula holds on functions.

**Step 2: Cartan's formula on a basic $1$-form $\omega = u\,dv$.**

Compute the left side using the Leibniz rule for $\mathcal{L}_X$:
$$\mathcal{L}_X(u\,dv) = (\mathcal{L}_X u) \cdot dv + u \cdot \mathcal{L}_X(dv).$$
Using $\mathcal{L}_X u = X(u) = Xu$ (Step 1) and $\mathcal{L}_X(dv) = d(\mathcal{L}_X v) = d(Xv)$ (the commutation of $\mathcal{L}_X$ with $d$ on functions, which can be verified directly from the flow definition: $\mathcal{L}_X(dv) = \frac{d}{dt}|_{t=0}(\phi^X_t)^*(dv) = \frac{d}{dt}|_{t=0}d((\phi^X_t)^*v) = d\frac{d}{dt}|_{t=0}(v \circ \phi^X_t) = d(Xv)$):
$$\mathcal{L}_X(u\,dv) = Xu \cdot dv + u \cdot d(Xv).$$

Compute the right side. First $\iota_X(u\,dv) = u \cdot \iota_X(dv) = u \cdot dv(X) = u \cdot Xv$. Now $d(\iota_X(u\,dv)) = d(u \cdot Xv) = du \cdot Xv + u \cdot d(Xv)$. (Using the standard product rule for $d$ on a product of functions, which is the $k = 0$ case of graded Leibniz.)

Since $\iota_X(u\,dv)=u(Xv)$ is a function, the ordinary Leibniz rule gives
$$d(\iota_X(u\,dv))=d(u(Xv))=(Xv)\,du+u\,d(Xv).$$

Next, $d(u\,dv) = du \wedge dv + u \cdot d^2(v) = du \wedge dv$ (using $d^2 v = 0$). So $\iota_X(d(u\,dv)) = \iota_X(du \wedge dv) = \iota_X(du) \wedge dv + (-1)^1 du \wedge \iota_X(dv) = (Xu)\,dv - du \wedge (Xv) = (Xu)\,dv - (Xv)\,du$ (the last by $du \wedge (Xv) = (Xv)\,du$, since $Xv$ is a scalar function and the wedge of a scalar function with $du$ is just scalar multiplication).

Summing: $(d\iota_X + \iota_X d)(u\,dv) = [(Xv)\,du + u\,d(Xv)] + [(Xu)\,dv - (Xv)\,du] = (Xu)\,dv + u\,d(Xv)$.

This matches the left side! ✓

> [!note]- Derivation
> **Left side:** $\mathcal{L}_X(u\,dv) = (\mathcal{L}_X u)\,dv + u\,(\mathcal{L}_X dv)$ by the (ungraded) Leibniz rule for $\mathcal{L}_X$ on wedges (here a $0$-form $u$ times a $1$-form $dv$). $\mathcal{L}_X u = X(u) = Xu$ (Step 1 of the present exercise / directional derivative). $\mathcal{L}_X(dv) = d(\mathcal{L}_X v) = d(Xv)$.
>
> Justification of $\mathcal{L}_X(dv) = d(Xv)$: Directly from the flow definition, $\mathcal{L}_X(dv) = \frac{d}{dt}|_{t=0}(\phi^X_t)^*(dv) = \frac{d}{dt}|_{t=0}d((\phi^X_t)^*v) = d(\frac{d}{dt}|_{t=0}v\circ \phi^X_t) = d(Xv)$, using naturality of $d$ under pullback (i.e., pullback commutes with $d$) and linearity of $d$ to commute it past the $t$-derivative.
>
> So $\mathcal{L}_X(u\,dv) = (Xu)\,dv + u\,d(Xv)$.
>
> **Right side:** Compute $\iota_X$ and $d$ separately.
>
> $\iota_X(u\,dv) = u \cdot \iota_X(dv) = u \cdot dv(X) = u \cdot Xv$. (A $0$-form / function.)
>
> $d(\iota_X(u\,dv)) = d(u \cdot Xv) = du \cdot (Xv) + u \cdot d(Xv)$. (Leibniz on a product of two functions, both regarded as $0$-forms. The result is a $1$-form.)
>
> Writing $du \cdot (Xv) = (Xv)\,du$ since $Xv$ is a scalar function: $d(\iota_X(u\,dv)) = (Xv)\,du + u\,d(Xv)$.
>
> $d(u\,dv) = du \wedge dv + u \wedge d(dv) = du \wedge dv + u \cdot d^2(v) = du \wedge dv$ (using $d^2 = 0$ on the function $v$). This is a $2$-form.
>
> $\iota_X(du \wedge dv)$: by the graded anti-derivation rule for $\iota_X$ on a wedge of two $1$-forms (each $k = 1$, $\ell = 1$):
> $$\iota_X(du \wedge dv) = (\iota_X du)\,dv + (-1)^1\,du \wedge \iota_X(dv) = (Xu)\,dv - du \wedge (Xv) = (Xu)\,dv - (Xv)\,du.$$
>
> Sum: $d(\iota_X(u\,dv)) + \iota_X(d(u\,dv)) = (Xv)\,du + u\,d(Xv) + (Xu)\,dv - (Xv)\,du = (Xu)\,dv + u\,d(Xv)$.
>
> The $(Xv)\,du$ terms cancel.
>
> **Compare:** Left and right sides both equal $(Xu)\,dv + u\,d(Xv)$. ✓

**Step 3: Propagate by linearity.**

A general $1$-form $\omega \in \Omega^1(M)$ is locally a sum $\omega = \sum_i u_i\,dv_i$ where each $u_i, v_i \in C^\infty$. Both $\mathcal{L}_X$ and $(d\iota_X + \iota_X d)$ are $\mathbb{R}$-linear operators, so verifying the formula on each $u_i\,dv_i$ (Step 2) propagates by linearity to all of $\omega$.

> [!note]- Derivation
> Both sides of Cartan's formula are $\mathbb{R}$-linear in $\omega$. Verification on basic terms $u\,dv$ (Step 2) implies verification on linear combinations (each term satisfies the identity, sum of identities is the identity for the sum).

**Step 4: $\mathcal{L}_X d = d\mathcal{L}_X$ in one line.**

By Cartan, $\mathcal{L}_X(d\omega) = (d\iota_X + \iota_X d)(d\omega) = d\iota_X d\omega + \iota_X d^2\omega = d\iota_X d\omega + 0$.

By Cartan applied to $\omega$, $\mathcal{L}_X\omega = d\iota_X\omega + \iota_X d\omega$, so $d(\mathcal{L}_X\omega) = d(d\iota_X\omega + \iota_X d\omega) = 0 + d\iota_X d\omega = d\iota_X d\omega$.

Both sides equal $d\iota_X d\omega$. ✓

> [!note]- Derivation
> $\mathcal{L}_X d\omega - d\mathcal{L}_X\omega = (d\iota_X + \iota_X d)(d\omega) - d(d\iota_X + \iota_X d)\omega = d\iota_X d\omega + \iota_X d^2\omega - d^2\iota_X\omega - d\iota_X d\omega = 0 + 0 - 0 + 0 = 0$ (using $d^2 = 0$ to kill two of the four terms and the remaining two cancel).
>
> So $\mathcal{L}_X d = d\mathcal{L}_X$. The proof is a one-line manipulation using Cartan's formula plus $d^2 = 0$.

> [!note]- Complete formal solution
> **(a) Cartan on functions.** $\iota_X f = 0$, $d(\iota_X f) = 0$, $\iota_X(df) = df(X) = X(f)$. Sum: $X(f)$. Independently, $\mathcal{L}_X f = \frac{d}{dt}|_{t=0}(f \circ \phi^X_t) = df(X) = X(f)$. Both sides equal $X(f)$.
>
> **(b) Cartan on $\omega = u\,dv$.** Compute the right side:
> $\iota_X(u\,dv) = u\,Xv$; $d(\iota_X(u\,dv)) = (Xv)\,du + u\,d(Xv)$.
> $d(u\,dv) = du \wedge dv$; $\iota_X(du \wedge dv) = (Xu)\,dv - (Xv)\,du$.
> Sum: $(Xv)\,du + u\,d(Xv) + (Xu)\,dv - (Xv)\,du = (Xu)\,dv + u\,d(Xv)$.
>
> Compute the left side: $\mathcal{L}_X(u\,dv) = (Xu)\,dv + u\,\mathcal{L}_X(dv) = (Xu)\,dv + u\,d(Xv)$ — using $\mathcal{L}_X(dv) = d(Xv)$, which follows from naturality of $d$ under flow pullback.
>
> Both sides equal $(Xu)\,dv + u\,d(Xv)$. ✓
>
> **(c) Linearity.** $\mathbb{R}$-linearity of both sides plus verification on basic terms propagates to all $1$-forms.
>
> **(d) $\mathcal{L}_X d = d\mathcal{L}_X$.** By Cartan, $\mathcal{L}_X d\omega = d\iota_X d\omega + \iota_X d^2\omega = d\iota_X d\omega + 0$. Also $d\mathcal{L}_X\omega = d^2 \iota_X\omega + d\iota_X d\omega = 0 + d\iota_X d\omega$. Both equal $d\iota_X d\omega$.
>
> $\blacksquare$

---

# Key Takeaways

**Cartan's magic formula is the one-line proof tool for most identities involving the Lie derivative of forms.** The commutation $\mathcal{L}_X d = d\mathcal{L}_X$, which would otherwise require a substantial proof, is two lines of Cartan + $d^2 = 0$. The product rule $\mathcal{L}_X(\omega \wedge \eta) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta$ can be derived from Cartan and the Leibniz rules for $d, \iota_X$. The whole "Cartan calculus" — the Lie superalgebra of operations on $\Omega^\bullet(M)$ — is organized by this single formula. The trigger pattern in problem-solving: "compute or verify something involving $\mathcal{L}_X$" → write down Cartan's formula and compute the right side.

**The key bookkeeping in Cartan's formula is the cancellation of cross-terms.** In the proof on $u\,dv$, the term $(Xv)\,du$ appears in two places — once from $d(\iota_X(u\,dv))$ and once from $\iota_X(d(u\,dv))$ — with opposite signs. The cancellation is what makes the formula work. The signs come from the graded Leibniz rules (sign $(-1)^k$ for $\iota_X$ passing through $\omega \in \Omega^k$, and similarly for $d$), and they cancel because of the careful structural setup of $d, \iota_X$ as graded anti-derivations. The "magic" in Cartan's formula is precisely the cancellation.

**The flow definition of $\mathcal{L}_X$ is essential for *meaning* but rarely used for *computation*.** The flow definition $\mathcal{L}_X\omega = \frac{d}{dt}|_{t=0}(\phi^X_t)^*\omega$ tells you *why* $\mathcal{L}_X$ deserves to be called "the rate of change of $\omega$ under the flow of $X$". But computing this directly requires solving the flow ODE, then pulling back, then differentiating — three steps, each requiring its own setup. Cartan's formula reduces all of this to two algebraic operations ($d$ of one form, $\iota_X$ of another), neither of which involves any flow. In practice, **you almost never use the flow definition for computation; you always use Cartan's formula**. The flow definition is for understanding; Cartan's formula is for working.

**The interplay $\mathcal{L}_X d = d\mathcal{L}_X$ is the structural identity that makes de Rham cohomology Lie-algebra-equivariant.** This commutation says: applying $d$ to a form and then computing its Lie derivative is the same as computing the Lie derivative first and then applying $d$. The closed forms $\ker d$ are therefore preserved by the Lie derivative, and so are the exact forms $\operatorname{im} d$, hence the quotient $H^k_{dR}(M)$ — the de Rham cohomology — admits a Lie algebra action by $\mathfrak{X}(M)$. The trivial case (each $\mathcal{L}_X$ acts as zero on $H^k_{dR}$) recovers the cohomological statement: the Lie derivative of a closed form is exact, hence cohomologously zero. The non-trivial case (when the action is nontrivial) gives **equivariant cohomology** and the **Cartan model**, the foundation of equivariant differential geometry.
