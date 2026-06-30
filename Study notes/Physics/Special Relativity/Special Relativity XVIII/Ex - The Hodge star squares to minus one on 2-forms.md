---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Hodge Star"
  - "Thm - Hodge Star and the Exterior Product"
  - "Def - The Levi-Civita Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

Work in four-dimensional Lorentzian spacetime, mostly-minus signature, $c = 1$.

1. State the general double-Hodge identity $\star\star A = (-1)^{p+1}A$ for a $p$-form, and specialise it to $p = 0, 1, 2, 3, 4$. In particular obtain $\star^2 = -1$ on $2$-forms.
2. Verify $\star^2 = -1$ on $2$-forms by direct computation on a basis $2$-form, $\star\star(e^0\wedge e^1) = -e^0\wedge e^1$.
3. Trace the sign $-1$ to its source: show it is $(-1)^{p(n-p)}\,\mathrm{sgn}(\det g)$ evaluated at $n = 4, p = 2$, and that the decisive factor is $\mathrm{sgn}(\det g) = -1$ (the Lorentzian signature), *not* the combinatorial part.
4. Contrast with the Euclidean case: show that in a positive-definite four-space ($\det g > 0$) one would have $\star^2 = +1$ on $2$-forms, with real eigenvalues $\pm1$.

**Recall:**

![[Def - The Hodge Star#The Definition]]

The [[Def - The Hodge Star|Hodge star]] satisfies $\star\star A = (-1)^{p+1}A$ on a $p$-form, established in [[Thm - Hodge Star and the Exterior Product]]. On a general pseudo-Riemannian $n$-manifold the identity is $\star\star = (-1)^{p(n-p)}\,\mathrm{sgn}(\det g)$. The [[Def - The Levi-Civita Tensor|Levi-Civita]] determinant satisfies $\det g < 0$ for any Lorentzian metric.

---

# Convergent Strategy

**Problem class.** A *structural* problem isolating the most important single fact of the chapter, $\star^2 = -1$ on $2$-forms, and its signature origin. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: invoke the general double-Hodge identity and specialise, then trace the sign.

**Assumption pattern.** The general identity $\star\star = (-1)^{p(n-p)}\mathrm{sgn}(\det g)$ is the input; $n = 4$, $p = 2$, $\det g < 0$ for Lorentzian signature. The direct computation re-derives the special case from the basis-form table.

**Theorem routing.** Part 1: specialise $(-1)^{p+1}$ to each $p$. Part 2: apply the basis-form Hodge table twice. Part 3: factor $(-1)^{p+1} = (-1)^{p(n-p)}\mathrm{sgn}(\det g)$ and identify the decisive factor. Part 4: flip $\mathrm{sgn}(\det g)$ to $+1$ and recompute.

**Key decision point.** The crux is part 3's attribution of the sign: the combinatorial factor $(-1)^{p(n-p)} = (-1)^{2\cdot2} = +1$ is *trivial* at $p = 2, n = 4$, so the entire minus sign comes from $\mathrm{sgn}(\det g) = -1$, which is the Lorentzian signature. Recognising that $\star^2 = -1$ is a statement about *one timelike direction*, not a combinatorial accident, is the whole point — and it is what makes the self-dual/anti-self-dual decomposition *complex* rather than real.

---

# Legal Operations Used

1. **Operation 7 from the topic page (invert the Hodge star with the sign rule).** The identity $\star\star = (-1)^{p+1}$ is the inversion rule; this exercise establishes and interprets it at $p = 2$.

2. **Operation 6 from the topic page (compute a Hodge dual by contracting into $\varepsilon$).** Used in part 2 for the direct double-dual computation on a basis form.

---

# Hints

> [!note]- Hint 1
> $(-1)^{p+1}$: for $p = 0$, $-1$; $p = 1$, $+1$; $p = 2$, $-1$; $p = 3$, $+1$; $p = 4$, $-1$. So $\star^2 = -1$ on forms of even degree ($0, 2, 4$) and $\star^2 = +1$ on odd degree ($1, 3$).

> [!note]- Hint 2
> From the basis-form table: $\star(e^0\wedge e^1) = -e^2\wedge e^3$ and $\star(e^2\wedge e^3) = +e^0\wedge e^1$. Compose: $\star\star(e^0\wedge e^1) = \star(-e^2\wedge e^3) = -(+e^0\wedge e^1) = -e^0\wedge e^1$.

> [!note]- Hint 3
> $(-1)^{p(n-p)}$ at $n = 4, p = 2$ is $(-1)^4 = +1$. So $\star\star = (+1)\cdot\mathrm{sgn}(\det g) = \mathrm{sgn}(\det g) = -1$, since $\det g < 0$ for Lorentzian signature. The minus is entirely the signature.

---

# Solution

The fact $\star^2 = -1$ on $2$-forms is the chapter's keystone, and its sign is a fingerprint of the Lorentzian signature. The plan: specialise the general identity (Step 1), confirm by direct basis computation (Step 2), attribute the sign to $\mathrm{sgn}(\det g)$ (Step 3), and contrast with the Euclidean case (Step 4).

**Step 1: $\star\star A = (-1)^{p+1}A$; on $2$-forms, $\star^2 = -1$.**

> [!note]- Derivation
> By [[Thm - Hodge Star and the Exterior Product]], $\star\star A = (-1)^{p+1}A$ for a $p$-form $A$. Specialising:
> $$
> \begin{array}{c|ccccc}
> p & 0 & 1 & 2 & 3 & 4 \\\hline
> \star\star = (-1)^{p+1} & -1 & +1 & -1 & +1 & -1
> \end{array}
> $$
> So $\star^2 = -1$ on forms of *even* degree ($0, 2, 4$) and $\star^2 = +1$ on *odd* degree ($1, 3$). The case of interest is $p = 2$:
> $$\star^2 = -1 \quad\text{on } \mathscr{A}_2(E).$$
> Since $4 - p = p = 2$, the Hodge star maps $2$-forms to $2$-forms (an automorphism of the six-dimensional $\mathscr{A}_2(E)$), and squaring gives minus the identity. An operator with $\star^2 = -1$ has no real eigenvalues — the seed of complexification.

**Step 2: direct verification on $e^0\wedge e^1$.**

> [!note]- Derivation
> Using the basis-form Hodge table (from [[Ex - Computing the Hodge dual of a 2-form]]): $\star(e^0\wedge e^1) = -e^2\wedge e^3$ and $\star(e^2\wedge e^3) = +e^0\wedge e^1$. Compose:
> $$\star\star(e^0\wedge e^1) = \star\big(-e^2\wedge e^3\big) = -\star(e^2\wedge e^3) = -\big(+e^0\wedge e^1\big) = -\,e^0\wedge e^1.$$
> Confirmed: $\star^2(e^0\wedge e^1) = -e^0\wedge e^1$. The minus arises as the product of the two signs in the table — $-1$ (electric-type $\to$ magnetic-type) times $+1$ (magnetic-type $\to$ electric-type). The same computation on any of the six basis $2$-forms gives $-1$, so $\star^2 = -1$ on all of $\mathscr{A}_2(E)$.

**Step 3: the sign is $\mathrm{sgn}(\det g)$, the Lorentzian signature.**

> [!note]- Derivation
> On a pseudo-Riemannian $n$-manifold the double-Hodge identity is
> $$\star\star = (-1)^{p(n-p)}\,\mathrm{sgn}(\det g).$$
> The exponent $(-1)^{p+1}$ used above is this formula specialised to $n = 4$ and Lorentzian signature; let us see the two factors separately at $n = 4, p = 2$:
> - *Combinatorial factor:* $(-1)^{p(n-p)} = (-1)^{2\cdot(4-2)} = (-1)^{4} = +1$. **Trivial.**
> - *Signature factor:* $\mathrm{sgn}(\det g) = \mathrm{sgn}(-1) = -1$, since $\det g < 0$ for any Lorentzian metric (one timelike, three spacelike directions).
>
> So $\star\star = (+1)(-1) = -1$ on $2$-forms, and the **entire minus sign comes from $\mathrm{sgn}(\det g)$** — the combinatorial part contributes nothing at $p = n/2 = 2$. The conclusion: $\star^2 = -1$ on $2$-forms is a direct expression of the Lorentzian signature, the single timelike direction making itself felt in the algebra of forms. It is not a permutation accident; it is physics.

**Step 4: in Euclidean signature, $\star^2 = +1$ with real eigenvalues.**

> [!note]- Derivation
> Suppose instead the four-space were *positive-definite* (Riemannian), $g = \mathrm{diag}(1,1,1,1)$, so $\det g = +1 > 0$. Then
> $$\star\star = (-1)^{p(n-p)}\,\mathrm{sgn}(\det g) = (+1)(+1) = +1 \quad\text{on } 2\text{-forms}.$$
> Now $\star$ is an *involution* on $\mathscr{A}_2$, with minimal polynomial $x^2 - 1 = (x-1)(x+1)$ and **real** eigenvalues $\pm1$. The $+1$ eigenspace is the **self-dual** $2$-forms ($\star F = F$) and the $-1$ eigenspace the **anti-self-dual** ($\star F = -F$), each real and three-dimensional, giving a *real* orthogonal decomposition $\mathscr{A}_2 = \mathscr{A}_2^+ \oplus \mathscr{A}_2^-$. This is the setting of Yang-Mills **instantons**: a self-dual gauge field satisfies $\star F = F$, a real equation. The contrast is sharp: the Lorentzian $\star^2 = -1$ forces *complex* eigenvalues $\pm i$ and a *complex* decomposition ($\mathbf E \pm i\mathbf B$), while the Euclidean $\star^2 = +1$ gives *real* eigenvalues $\pm1$ and a *real* decomposition. The one minus sign in the signature is the whole difference.

> [!note]- Complete formal solution
> **(1)** $\star\star = (-1)^{p+1}$: $-1, +1, -1, +1, -1$ for $p = 0, 1, 2, 3, 4$. On $2$-forms, $\star^2 = -1$ (an automorphism with no real eigenvalues).
> **(2)** $\star\star(e^0\wedge e^1) = \star(-e^2\wedge e^3) = -(+e^0\wedge e^1) = -e^0\wedge e^1$.
> **(3)** $\star\star = (-1)^{p(n-p)}\mathrm{sgn}(\det g)$; at $n=4, p=2$ the combinatorial factor is $(-1)^4 = +1$, so $\star\star = \mathrm{sgn}(\det g) = -1$ (Lorentzian, $\det g < 0$). The minus is entirely the signature.
> **(4)** Euclidean ($\det g > 0$): $\star\star = +1$, real eigenvalues $\pm1$, real self-dual/anti-self-dual split (instantons). $\blacksquare$

---

# Key Takeaways

**$\star^2 = -1$ on $2$-forms is the Lorentzian signature speaking, and it forces complexification.** The single most important fact of the chapter is that the Hodge star squares to *minus* the identity on $2$-forms, and the exercise pins down why: at the middle degree $p = n/2 = 2$ the combinatorial factor $(-1)^{p(n-p)}$ is trivially $+1$, so the entire sign is $\mathrm{sgn}(\det g) = -1$, the determinant of any Lorentzian metric being negative. This is not a sign convention or a permutation accident — it is the one timelike direction making itself felt in the algebra of forms. The consequence is profound: an operator with $\star^2 = -1$ has no real eigenvalues, so the natural eigen-objects are complex, and the $2$-forms must be complexified to be diagonalised. The reusable principle is that whenever you meet $\star$ on $2$-forms in spacetime, you are meeting a complex structure ("multiplication by $i$"), and the right variables are the complex combinations $A \mp i\star A$. Tracing the minus sign to the signature is the conceptual key that turns a sign rule into the chirality of electromagnetism.

**The middle degree $p = n/2$ is where the signature decides everything.** At any other degree the combinatorial factor $(-1)^{p(n-p)}$ can itself contribute a sign, but at the self-dual middle degree $p = n/2$ it is always $(-1)^{(n/2)^2}$, which for $n = 4$ is $(-1)^4 = +1$ — so the signature factor $\mathrm{sgn}(\det g)$ is laid bare. This is why the most signature-sensitive Hodge phenomena live in the middle degree: in four dimensions, on $2$-forms; in two dimensions, on $1$-forms (where Lorentzian $\star^2 = +1$ but the complex structure of a Riemann surface gives $\star^2 = -1$ on the Euclidean side, the origin of holomorphic/anti-holomorphic splitting). The transferable insight is that the eigenvalue structure of the Hodge star in middle degree — real $\pm1$ in Riemannian signature, complex $\pm i$ in Lorentzian — is a clean diagnostic of the signature, and it controls whether self-duality is a real condition (instantons) or a complex one (helicity). When working in any even dimension, the middle-degree Hodge star is where to look for the signature's algebraic imprint.

**Euclidean self-duality is real (instantons); Lorentzian self-duality is complex (helicity) — same algebra, opposite sign.** The contrast in part 4 is one of the most instructive in mathematical physics. In Riemannian signature $\star^2 = +1$ on $2$-forms, so self-dual ($\star F = F$) and anti-self-dual ($\star F = -F$) forms are *real*, and a self-dual gauge field is a real, finite-action solution — a Yang-Mills instanton, the basis of much of modern geometry (Donaldson theory) and of non-perturbative gauge dynamics. In Lorentzian signature $\star^2 = -1$, so the eigenvalues are $\pm i$ and the self-dual/anti-self-dual forms are *complex* — for the electromagnetic field they are $\mathbf E \pm i\mathbf B$, the two helicities of the photon. The same algebraic operation (project onto $\star$-eigenspaces) gives a real decomposition in one signature and a complex one in the other, purely because of $\mathrm{sgn}(\det g)$. The reusable lesson: before exploiting self-duality, check the signature — it determines whether you are doing real instanton geometry or complex helicity decomposition, and the two have entirely different flavours despite identical algebra. This single sign is the watershed between Euclidean and Lorentzian field theory.
