---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - The Wedge Product on a Manifold"
  - "Def - Differential k-Form on a Manifold"
  - "Thm - Wedge Product Properties"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $M$ be a smooth manifold and $\omega, \eta \in \Omega^1(M)$ be smooth $1$-forms on $M$. Prove directly from the determinant convention $(\omega \wedge \eta)(X, Y) = \det(\omega(X)\,\eta(X); \omega(Y)\,\eta(Y))$ — or via the standard expansion — that:

(a) **Antisymmetry on $1$-forms:** $\omega \wedge \eta = -\eta \wedge \omega$, equivalently $\omega \wedge \omega = 0$.

(b) **Graded commutativity rule:** For $\omega \in \Omega^k(M)$ with $k$ odd, $\omega \wedge \omega = 0$. For $\omega \in \Omega^k(M)$ with $k$ even, give an example on $\mathbb{R}^4$ where $\omega \wedge \omega \neq 0$.

(c) **Wedge of $k$ identical $1$-forms vanishes:** For any single $1$-form $\omega \in \Omega^1(M)$ and any $k \geq 2$, $\omega^{\wedge k} = \omega \wedge \cdots \wedge \omega = 0$.

**Recall:**

![[Thm - Wedge Product Properties#Statement]]

The wedge product on a manifold is defined pointwise from the wedge product on alternating tensors: $(\omega \wedge \eta)_p = \omega_p \wedge \eta_p$.

The determinant identity: for $1$-forms $\omega^1, \dots, \omega^k$, $(\omega^1 \wedge \cdots \wedge \omega^k)(v_1, \dots, v_k) = \det(\omega^i(v_j))$.

---

# Convergent Strategy

**Problem class:** This is a "verify an algebraic identity from the definition" problem. The exercise drills the wedge product's algebraic properties — antisymmetry on $1$-forms, the graded commutativity rule, and the squared-zero identity for odd-degree forms.

**Assumption pattern:** The objects are abstract $1$-forms on an arbitrary manifold. The structure available is the definition of $\wedge$ (the determinant convention) and the basic algebraic properties of [[Thm - Wedge Product Properties]]. The route is to evaluate both sides on tangent vectors and use the alternation/antisymmetry of the determinant.

**Theorem routing:** Part (a) is the $k = 1$ case of graded anticommutativity from [[Thm - Wedge Product Properties]] (c). Part (b) is graded anticommutativity applied to $\omega \in \Omega^k$ with $k$ odd, giving $\omega \wedge \omega = -\omega \wedge \omega \Rightarrow \omega \wedge \omega = 0$; for $k$ even, the symplectic-form example on $\mathbb{R}^4$ shows nonzero square. Part (c) follows from (a) iteratively: $\omega \wedge \omega \wedge \cdots = 0$ at the first $\omega \wedge \omega$.

**Key decision point:** The non-obvious step in (a) is recognizing that the identity $\omega \wedge \eta = -\eta \wedge \omega$ is *equivalent* to $\omega \wedge \omega = 0$ in characteristic $\neq 2$: expand $(\omega + \eta) \wedge (\omega + \eta) = 0$ to derive the antisymmetry, and vice versa. This is the "polarization identity" of the wedge product.

---

# Legal Operations Used

1. **Expand a form in coordinates and apply $d$ mechanically** (operation 1) — not really applicable here, since we use abstract properties.

2. **Use the wedge as a determinant** (operation 9). The fundamental identity $(\omega \wedge \eta)(X, Y) = \det(\omega(X), \omega(Y); \eta(X), \eta(Y))$ is the source of antisymmetry: swap $X \leftrightarrow Y$ swaps the rows of the determinant, flipping the sign.

---

# Hints

> [!note]- Hint 1
> Use the determinant identity for the wedge of two $1$-forms. Swap the two arguments and observe what happens.

> [!note]- Hint 2
> For graded anticommutativity, write $\omega \wedge \eta = -\eta \wedge \omega$ (with $k = \ell = 1$); set $\omega = \eta$ to get $\omega \wedge \omega = -\omega \wedge \omega$, so $2\omega \wedge \omega = 0$.

> [!note]- Hint 3
> For the even-degree counterexample on $\mathbb{R}^4$, try $\omega = dx^1 \wedge dx^2 + dx^3 \wedge dx^4$. Compute $\omega \wedge \omega$ — what's the answer?

---

# Solution

The proof has three steps. Step 1 verifies (a) by evaluating both sides on tangent vectors and using the antisymmetry of the determinant. Step 2 uses graded anticommutativity from [[Thm - Wedge Product Properties]] to derive (b): odd-degree forms have zero square, even-degree forms may not, and the symplectic form on $\mathbb{R}^4$ is the canonical example. Step 3 derives (c) by iterating (a).

**Step 1: $\omega \wedge \eta = -\eta \wedge \omega$ for $1$-forms.**

Evaluate both sides on a pair $(X, Y)$ of tangent vectors. By the determinant identity,
$$(\omega \wedge \eta)(X, Y) = \det\begin{pmatrix}\omega(X) & \omega(Y) \\ \eta(X) & \eta(Y)\end{pmatrix} = \omega(X)\eta(Y) - \omega(Y)\eta(X).$$
Similarly,
$$(\eta \wedge \omega)(X, Y) = \det\begin{pmatrix}\eta(X) & \eta(Y) \\ \omega(X) & \omega(Y)\end{pmatrix} = \eta(X)\omega(Y) - \eta(Y)\omega(X) = -[\omega(X)\eta(Y) - \omega(Y)\eta(X)] = -(\omega \wedge \eta)(X, Y).$$
So $\eta \wedge \omega = -\omega \wedge \eta$ pointwise, hence globally.

Setting $\omega = \eta$: $\omega \wedge \omega = -\omega \wedge \omega$, so $2(\omega \wedge \omega) = 0$, hence $\omega \wedge \omega = 0$ (in characteristic $\neq 2$).

> [!note]- Derivation
> Direct computation using the determinant identity.
>
> $(\omega \wedge \eta)(X, Y) = \omega(X)\eta(Y) - \omega(Y)\eta(X)$, by the determinant identity for two $1$-forms.
>
> $(\eta \wedge \omega)(X, Y) = \eta(X)\omega(Y) - \eta(Y)\omega(X) = \omega(Y)\eta(X) - \omega(X)\eta(Y) = -(\omega \wedge \eta)(X, Y)$.
>
> So $\omega \wedge \eta + \eta \wedge \omega = 0$, equivalently $\omega \wedge \eta = -\eta \wedge \omega$.
>
> Setting $\omega = \eta$ gives $\omega \wedge \omega = -\omega \wedge \omega$, hence $\omega \wedge \omega = 0$.

**Step 2: Graded commutativity rule.**

By [[Thm - Wedge Product Properties|graded anticommutativity]], $\omega \wedge \eta = (-1)^{k\ell}\eta \wedge \omega$ for $\omega \in \Omega^k, \eta \in \Omega^\ell$. Setting $\omega = \eta$ and $k = \ell$: $\omega \wedge \omega = (-1)^{k^2}\omega \wedge \omega$. If $k$ is odd, $k^2$ is odd, so $\omega \wedge \omega = -\omega \wedge \omega$, hence $\omega \wedge \omega = 0$.

For $k$ even ($k = 2$), consider $\omega = dx^1 \wedge dx^2 + dx^3 \wedge dx^4$ on $\mathbb{R}^4$. Then
$$\omega \wedge \omega = (dx^1 \wedge dx^2 + dx^3 \wedge dx^4) \wedge (dx^1 \wedge dx^2 + dx^3 \wedge dx^4).$$
Expanding, $dx^1 \wedge dx^2 \wedge dx^1 \wedge dx^2 = 0$ (repeated index), $dx^3 \wedge dx^4 \wedge dx^3 \wedge dx^4 = 0$, but the cross terms:
$$(dx^1 \wedge dx^2) \wedge (dx^3 \wedge dx^4) + (dx^3 \wedge dx^4) \wedge (dx^1 \wedge dx^2) = dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4 + dx^3 \wedge dx^4 \wedge dx^1 \wedge dx^2.$$
By graded anticommutativity, $dx^3 \wedge dx^4 \wedge dx^1 \wedge dx^2 = (-1)^{2 \cdot 2}\,dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4 = dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4$ (using $(-1)^4 = 1$). So $\omega \wedge \omega = 2\,dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4 \neq 0$.

> [!note]- Derivation
> For odd $k$, the graded anticommutativity rule applied with $\omega = \eta$ gives $\omega \wedge \omega = (-1)^{k^2}\omega \wedge \omega = -\omega \wedge \omega$ (since $k^2$ is odd), hence $\omega \wedge \omega = 0$.
>
> For even $k$, the same rule gives $\omega \wedge \omega = (-1)^{k^2}\omega \wedge \omega = \omega \wedge \omega$ (since $k^2$ is even). So no constraint forces $\omega \wedge \omega = 0$; it may or may not vanish.
>
> The example $\omega = dx^1 \wedge dx^2 + dx^3 \wedge dx^4$ on $\mathbb{R}^4$ has $\omega \wedge \omega = 2\,dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4 \neq 0$. This is the symplectic form on $\mathbb{R}^4$, and its square is the Liouville volume form (up to a factor of $2$).

**Step 3: Wedge of $k$ identical $1$-forms vanishes.**

By (a), $\omega \wedge \omega = 0$ for any $1$-form $\omega$. So $\omega^{\wedge k} = \omega \wedge \omega \wedge \omega^{\wedge(k-2)} = 0 \wedge \omega^{\wedge(k-2)} = 0$.

> [!note]- Derivation
> $\omega^{\wedge k} = \omega \wedge (\omega^{\wedge(k-1)})$. For $k \geq 2$, factor out two copies: $\omega^{\wedge k} = (\omega \wedge \omega) \wedge \omega^{\wedge(k-2)} = 0 \wedge \omega^{\wedge(k-2)} = 0$ by part (a). Done.

> [!note]- Complete formal solution
> **Step 1 (antisymmetry on $1$-forms).** Take $\omega, \eta \in \Omega^1(M)$ and tangent vectors $X, Y \in T_pM$. By the determinant identity,
> $$(\omega \wedge \eta)(X, Y) = \det\begin{pmatrix}\omega(X) & \omega(Y) \\ \eta(X) & \eta(Y)\end{pmatrix} = \omega(X)\eta(Y) - \omega(Y)\eta(X).$$
> Similarly $(\eta \wedge \omega)(X, Y) = \eta(X)\omega(Y) - \eta(Y)\omega(X) = -(\omega \wedge \eta)(X, Y)$. So $\eta \wedge \omega = -\omega \wedge \omega$.
>
> Setting $\eta = \omega$ gives $\omega \wedge \omega = -\omega \wedge \omega$, hence $\omega \wedge \omega = 0$.
>
> **Step 2 (graded rule and counterexample).** By [[Thm - Wedge Product Properties]] (c), $\omega \wedge \omega = (-1)^{k^2}\omega \wedge \omega$ for $\omega \in \Omega^k$. If $k$ is odd, $k^2$ is odd, $\omega \wedge \omega = -\omega \wedge \omega \Rightarrow \omega \wedge \omega = 0$. If $k$ is even, no constraint.
>
> Counterexample: $\omega = dx^1 \wedge dx^2 + dx^3 \wedge dx^4 \in \Omega^2(\mathbb{R}^4)$. Compute $\omega \wedge \omega$: the terms $(dx^1 \wedge dx^2) \wedge (dx^1 \wedge dx^2)$ and $(dx^3 \wedge dx^4) \wedge (dx^3 \wedge dx^4)$ vanish (repeated indices), and the cross-terms $(dx^1 \wedge dx^2) \wedge (dx^3 \wedge dx^4) + (dx^3 \wedge dx^4) \wedge (dx^1 \wedge dx^2) = 2\,dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4$ (using graded anticommutativity to flip the second product). So $\omega \wedge \omega = 2\,dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4 \neq 0$.
>
> **Step 3 (iteration).** For any $1$-form $\omega$ and $k \geq 2$, $\omega^{\wedge k} = (\omega \wedge \omega) \wedge \omega^{\wedge(k-2)} = 0$.
>
> $\blacksquare$

---

# Key Takeaways

**The wedge of two identical $1$-forms is zero — but only because the degree is odd.** Many students remember "the wedge of anything with itself is zero" as a general rule; this is only true for *odd-degree* forms. The mechanism is graded anticommutativity: $\omega \wedge \omega = (-1)^{k^2}\omega \wedge \omega$, and the right-hand side is $+\omega \wedge \omega$ for even $k$, so no constraint. The symplectic form on $\mathbb{R}^4$ is the standard counterexample — its square is the Liouville volume form, a top-degree nonzero form. This nuance matters whenever one is working with symplectic or even-degree forms: the algebra is *different* from $1$-form algebra. The trigger pattern is "I'm wedging $\omega$ with itself" — check the parity of $\deg\omega$ before assuming the answer is zero.

**Graded anticommutativity is the algebraic encoding of orientation.** The sign $(-1)^{k\ell}$ in $\omega \wedge \eta = (-1)^{k\ell}\eta \wedge \omega$ counts the number of transpositions needed to swap the $k$ $1$-form factors of $\omega$ past the $\ell$ factors of $\eta$. Each transposition costs a sign by anticommutativity. The whole machinery of orientation in integration theory — that swapping two coordinates of a chart flips the integral's sign — is the consequence of this single algebraic rule. When in doubt about a sign in differential geometry, count the transpositions.

**The determinant identity is the deepest property of the wedge.** $(\omega^1 \wedge \cdots \wedge \omega^k)(v_1, \dots, v_k) = \det(\omega^i(v_j))$ is the *one structural fact* of the wedge product, from which all other properties (bilinearity, associativity, anticommutativity) follow. Whenever a calculation involves the wedge of $1$-forms, recognizing it as a determinant gives access to all the determinant identities. Conversely, whenever a determinant appears in a problem, writing it as a wedge often reveals additional algebraic structure (anticommutativity with other wedges, derivative rules, pullback compatibility). The trigger pattern: see a Jacobian determinant → write it as a wedge of $1$-forms.

**Closed antisymmetric algebra is exactly the right algebra for invariant integration.** The wedge product's algebraic properties (antisymmetry, graded commutativity, the determinant identity) are precisely the structure needed for the integral of a $k$-form over an oriented $k$-submanifold to be coordinate-invariant. Any *non*-antisymmetric multilinear "integrand" would multiply by the full Jacobian matrix under coordinate change, which cannot be canceled by any change-of-variables formula. The antisymmetric structure collapses the Jacobian to its determinant — and the determinant is exactly what change-of-variables can cancel. So the antisymmetry of $\omega \wedge \eta$ at the $1$-form level is the *direct reason* differential forms are the right integrands for oriented integration.
