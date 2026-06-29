---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Group"
  - "Thm - Invariance of the Spacetime Interval"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Problem Statement

Let $g = \mathrm{diag}(1,-1,-1,-1)$ be the Minkowski metric and recall the orthogonal group $O(2)$ is characterised as the linear maps preserving the Euclidean norm, equivalently the matrices $H$ with $H^{\mathsf T} I\, H = I$.

1. Define the **Lorentz group** $O(1,3)$ as the set of $4\times 4$ real matrices $\Lambda$ with $\Lambda^{\mathsf T} g\, \Lambda = g$. Show directly from this defining equation — *without* writing any matrix entries — that $O(1,3)$ is a group under matrix multiplication: closed under products, containing the identity, and closed under inverses.
2. Show that the defining equation is equivalent to "$\Lambda$ preserves the Minkowski inner product": $(\Lambda X)\cdot(\Lambda Y) = X\cdot Y$ for all $X, Y$.
3. Explain the name *pseudo-orthogonal*: state precisely what is changed in passing from the characterisation of $O(2)$ (or $O(4)$) to that of $O(1,3)$, and why that single change is the whole of special relativity.
4. Deduce that $(\det\Lambda)^2 = 1$ and that $\Lambda^{-1} = g\,\Lambda^{\mathsf T} g$.

**Recall:**

![[Def - The Lorentz Group#The Definition]]

A [[Def - Group|group]] is a set with an associative binary operation, an identity element, and an inverse for every element. The Minkowski inner product is $X\cdot Y = \eta_{\mu\nu}X^\mu Y^\nu = X^0Y^0 - X^1Y^1 - X^2Y^2 - X^3Y^3$ ([[Def - Minkowski Space and the Metric]]), and the [[Thm - Invariance of the Spacetime Interval|invariance theorem]] says the Lorentz transformations are exactly the linear maps preserving it. The metric satisfies $g^{\mathsf T} = g$ and $g^2 = I$ (so $g^{-1} = g$) and $\det g = -1$.

---

# Convergent Strategy

**Problem class.** A *structural / verify-a-group* problem, the fourth target type of the [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group#Problem-Solving Strategy|topic strategy]]: take an algebraically-defined set and establish its group structure and basic invariants. The whole point is to work from the *defining equation* $\Lambda^{\mathsf T} g\,\Lambda = g$ abstractly, never touching matrix entries, so the argument transfers verbatim to every pseudo-orthogonal group $O(p,q)$.

**Assumption pattern.** The only hypothesis is the congruence equation $\Lambda^{\mathsf T} g\,\Lambda = g$ with $g$ a fixed invertible symmetric matrix. That single equation supplies everything: invertibility of $\Lambda$ (from $\det g \neq 0$), closure (compose two congruences), and the inverse formula (rearrange). Recognising that $g$ being *invertible* is the load-bearing fact — not its signature — is what makes the proof signature-blind.

**Theorem routing.** Group axioms follow by pure algebra from the defining equation; the inner-product equivalence is the [[Thm - Invariance of the Spacetime Interval|invariance theorem]]'s polarisation argument; the determinant fact is one determinant of the defining equation. No deep theorem is needed — the exercise is about seeing that the abstract equation already contains the group.

**Key decision point.** The non-obvious choice is to *resist* expanding into components. A reader who writes out the $16$ entries of $\Lambda$ and the $10$ equations drowns; the elegant route manipulates $\Lambda^{\mathsf T} g\,\Lambda = g$ as a matrix identity. The second subtlety is order: one must first deduce $\Lambda$ is *invertible* (so that "inverse" even makes sense) before proving the inverse is again Lorentz.

---

# Legal Operations Used

1. **Classify by the defining equation (operation analogous to "compute an invariant").** The defining congruence $\Lambda^{\mathsf T} g\,\Lambda = g$ is itself the membership test; every part of the exercise is an algebraic consequence of it, applied without coordinates.

2. **Take determinants of a matrix equation.** Applying $\det$ to $\Lambda^{\mathsf T} g\,\Lambda = g$ and using multiplicativity of $\det$ and $\det\Lambda^{\mathsf T} = \det\Lambda$ extracts $(\det\Lambda)^2 = 1$ in one line.

3. **Use the metric to raise/lower (operation: index gymnastics with $g$).** Rearranging $\Lambda^{\mathsf T} g\,\Lambda = g$ with $g^{-1} = g$ gives the explicit inverse $\Lambda^{-1} = g\,\Lambda^{\mathsf T} g$.

---

# Hints

> [!note]- Hint 1
> Do not write matrix entries. Treat $\Lambda^{\mathsf T} g\,\Lambda = g$ as an identity among matrices and manipulate it the way you would manipulate $R^{\mathsf T}R = I$ to prove $O(n)$ is a group.

> [!note]- Hint 2
> For closure, suppose $\Lambda_1^{\mathsf T} g\,\Lambda_1 = g$ and $\Lambda_2^{\mathsf T} g\,\Lambda_2 = g$; compute $(\Lambda_1\Lambda_2)^{\mathsf T} g\,(\Lambda_1\Lambda_2)$ and substitute one equation, then the other.

> [!note]- Hint 3
> For invertibility, take $\det$ of the defining equation: $\det g \neq 0$ forces $\det\Lambda \neq 0$. Only then is $\Lambda^{-1}$ defined; to show it is Lorentz, left- and right-multiply the defining equation by $(\Lambda^{-1})^{\mathsf T}$ and $\Lambda^{-1}$.

> [!note]- Hint 4
> For the inner-product equivalence, write $X\cdot Y = X^{\mathsf T} g\, Y$ and compute $(\Lambda X)^{\mathsf T} g\,(\Lambda Y) = X^{\mathsf T}(\Lambda^{\mathsf T} g\,\Lambda)Y$. Use polarisation to argue that preserving all norms $X\cdot X$ is the same as preserving all inner products.

---

# Solution

The exercise is one idea repeated: every claim is a one-line manipulation of the defining congruence $\Lambda^{\mathsf T} g\,\Lambda = g$, never of its entries. Step 1 proves the group axioms abstractly; Step 2 translates the equation into preservation of the inner product; Step 3 isolates the single change ($I \to g$) that names "pseudo-orthogonal"; Step 4 reads off the determinant and inverse. The non-obvious move throughout is to keep $g$ as a symbol and use only that it is invertible and symmetric.

**Step 1: $O(1,3)$ is a group.**

> [!note]- Derivation
> *Identity.* $I^{\mathsf T} g\, I = g$, so $I \in O(1,3)$.
>
> *Closure.* Let $\Lambda_1, \Lambda_2 \in O(1,3)$. Then
> $$(\Lambda_1\Lambda_2)^{\mathsf T} g\,(\Lambda_1\Lambda_2) = \Lambda_2^{\mathsf T}\,\Lambda_1^{\mathsf T} g\,\Lambda_1\,\Lambda_2 = \Lambda_2^{\mathsf T}\,g\,\Lambda_2 = g,$$
> substituting $\Lambda_1^{\mathsf T} g\,\Lambda_1 = g$ first, then $\Lambda_2^{\mathsf T} g\,\Lambda_2 = g$. So $\Lambda_1\Lambda_2 \in O(1,3)$.
>
> *Inverses.* First, $\Lambda$ is invertible: taking $\det$ of $\Lambda^{\mathsf T} g\,\Lambda = g$ gives $(\det\Lambda)^2\det g = \det g$; since $\det g = -1 \neq 0$, $(\det\Lambda)^2 = 1$, so $\det\Lambda \neq 0$ and $\Lambda^{-1}$ exists. Now show $\Lambda^{-1} \in O(1,3)$: from $\Lambda^{\mathsf T} g\,\Lambda = g$, left-multiply by $(\Lambda^{-1})^{\mathsf T} = (\Lambda^{\mathsf T})^{-1}$ and right-multiply by $\Lambda^{-1}$:
> $$(\Lambda^{-1})^{\mathsf T}\,\Lambda^{\mathsf T} g\,\Lambda\,\Lambda^{-1} = (\Lambda^{-1})^{\mathsf T} g\,\Lambda^{-1} \quad\Longrightarrow\quad g = (\Lambda^{-1})^{\mathsf T} g\,\Lambda^{-1},$$
> since the left side telescopes to $g$. So $\Lambda^{-1} \in O(1,3)$.
>
> *Associativity.* Matrix multiplication is associative. Hence $O(1,3)$ is a group.

**Step 2: the defining equation is "preserves the inner product".**

> [!note]- Derivation
> Write the Minkowski inner product as the bilinear form $X\cdot Y = X^{\mathsf T} g\, Y$. For a linear map $\Lambda$,
> $$(\Lambda X)\cdot(\Lambda Y) = (\Lambda X)^{\mathsf T} g\,(\Lambda Y) = X^{\mathsf T}\big(\Lambda^{\mathsf T} g\,\Lambda\big) Y.$$
> If $\Lambda^{\mathsf T} g\,\Lambda = g$, this equals $X^{\mathsf T} g\, Y = X\cdot Y$ for all $X, Y$, so $\Lambda$ preserves the inner product. Conversely, if $(\Lambda X)\cdot(\Lambda Y) = X\cdot Y$ for all $X, Y$, then $X^{\mathsf T}(\Lambda^{\mathsf T} g\,\Lambda - g)Y = 0$ for all $X, Y$; a bilinear form that vanishes on all pairs is the zero form, so $\Lambda^{\mathsf T} g\,\Lambda - g = 0$. (Preserving all the diagonal values $X\cdot X$ already suffices, since by polarisation $2(X\cdot Y) = (X+Y)\cdot(X+Y) - X\cdot X - Y\cdot Y$ recovers the full bilinear form — this is the [[Thm - Invariance of the Spacetime Interval|interval-invariance]] statement.)

**Step 3: why "pseudo-orthogonal".**

> [!note]- Derivation
> The orthogonal group $O(n)$ is the matrices $H$ with $H^{\mathsf T} I\, H = I$, i.e. preserving the *positive-definite* form whose matrix is the identity $I = \mathrm{diag}(1,\dots,1)$. The Lorentz group is the matrices $\Lambda$ with $\Lambda^{\mathsf T} g\,\Lambda = g$, the *same equation with $I$ replaced by $g = \mathrm{diag}(1,-1,-1,-1)$*. The single change is the signature of the form: from all-plus (definite) to one-plus-three-minus (indefinite). "Pseudo-orthogonal" means "orthogonal with respect to an indefinite form". That one sign flip is the entire difference between Euclidean four-space $O(4)$ — no light cone, no boosts, no distinction between time and space — and Minkowski space $O(1,3)$, where the minus signs create the light cone, the timelike/spacelike trichotomy, and every relativistic effect.

**Step 4: determinant and inverse.**

> [!note]- Derivation
> Determinant: shown in Step 1, $(\det\Lambda)^2\det g = \det g$ with $\det g = -1$ gives $(\det\Lambda)^2 = 1$, so $\det\Lambda = \pm 1$.
>
> Inverse: from $\Lambda^{\mathsf T} g\,\Lambda = g$, left-multiply by $g^{-1} = g$: $g\,\Lambda^{\mathsf T} g\,\Lambda = g\, g = I$, so $(g\,\Lambda^{\mathsf T} g)\,\Lambda = I$, identifying $\Lambda^{-1} = g\,\Lambda^{\mathsf T} g$. (This is the relativistic "inverse equals transpose", with the metric conjugating the transpose; in index form $(\Lambda^{-1})^\mu{}_\nu = \Lambda_\nu{}^\mu$.)

> [!note]- Complete formal solution
> Let $O(1,3) = \{\Lambda : \Lambda^{\mathsf T} g\,\Lambda = g\}$, $g = \mathrm{diag}(1,-1,-1,-1)$, $\det g = -1$, $g^{-1} = g$.
>
> *Group.* $I^{\mathsf T} g\, I = g$ gives $I \in O(1,3)$. For $\Lambda_1, \Lambda_2 \in O(1,3)$, $(\Lambda_1\Lambda_2)^{\mathsf T} g\,\Lambda_1\Lambda_2 = \Lambda_2^{\mathsf T}\Lambda_1^{\mathsf T} g\,\Lambda_1\Lambda_2 = \Lambda_2^{\mathsf T} g\,\Lambda_2 = g$, so the product is in $O(1,3)$. Taking $\det$ of the defining equation gives $(\det\Lambda)^2 = 1 \neq 0$, so $\Lambda$ is invertible; conjugating the defining equation by $\Lambda^{-1}$ yields $(\Lambda^{-1})^{\mathsf T} g\,\Lambda^{-1} = g$, so $\Lambda^{-1} \in O(1,3)$. Associativity is inherited from matrix multiplication.
>
> *Inner product.* With $X\cdot Y = X^{\mathsf T} g\, Y$, $(\Lambda X)\cdot(\Lambda Y) = X^{\mathsf T}(\Lambda^{\mathsf T} g\,\Lambda)Y$, which equals $X\cdot Y$ for all $X, Y$ iff $\Lambda^{\mathsf T} g\,\Lambda = g$ (a bilinear form vanishing on all pairs is zero; preserving all $X\cdot X$ suffices by polarisation).
>
> *Pseudo-orthogonality.* $O(1,3)$ is $O(n)$'s defining equation $H^{\mathsf T} I H = I$ with $I$ replaced by the indefinite $g$; the signature change from $(4,0)$ to $(1,3)$ is the only difference.
>
> *Determinant and inverse.* $(\det\Lambda)^2 = 1$, and left-multiplying the defining equation by $g$ gives $g\Lambda^{\mathsf T} g\,\Lambda = I$, so $\Lambda^{-1} = g\,\Lambda^{\mathsf T} g$. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One is tempted to "verify the group axioms" by exhibiting boosts and rotations and checking that products of those are again boosts or rotations. This is both more work and *incomplete*: it only checks the elements you happen to write down, and the product of two non-collinear boosts is a boost *times a rotation*, which can mislead you into thinking the set is not closed. The abstract argument from $\Lambda^{\mathsf T} g\,\Lambda = g$ covers *every* element at once and never needs a parametrisation.

---

# Key Takeaways

**The defining congruence equation contains the entire group structure — work with it abstractly.** The single most transferable lesson is that a matrix group defined by a congruence relation $\Lambda^{\mathsf T} g\,\Lambda = g$ proves itself a group by pure symbol-pushing, with the entries of $\Lambda$ never written down. Closure is "substitute the equation twice", invertibility is "take a determinant", and the inverse-is-in-the-group step is "conjugate the equation". This pattern is identical for $O(n)$ ($g = I$), the symplectic group $Sp(2n)$ ($g = J$, the symplectic form), and the unitary groups (Hermitian congruence). When you meet any "matrices preserving a form", reach first for the abstract manipulation; the component expansion is almost never necessary and almost always a trap. The trigger is the appearance of a fixed invertible matrix sandwiched as $\Lambda^{\mathsf T} g\,\Lambda$.

**Only the invertibility of $g$ is load-bearing for the group axioms; the signature decides the geometry, not the group structure.** Nowhere in Step 1 did the *signs* of $g$ matter — the proof used only $\det g \neq 0$ and $g^{\mathsf T} = g$. This is why $O(p,q)$ is a group for every signature, and why the Lorentz group's group-theoretic skeleton is identical to the rotation group's. The signature enters only when you ask *geometric* questions: whether the group is compact (definite) or non-compact (indefinite), whether there is a light cone, whether boosts exist. Separating "what makes it a group" (invertibility) from "what makes it Lorentzian" (indefinite signature) is the conceptual core of the pseudo-orthogonal viewpoint, and it is why the name puts "pseudo" in front of "orthogonal": same algebra, different sign.

**Preserving the form and preserving the inner product are the same statement, via polarisation.** The equivalence of "$\Lambda^{\mathsf T} g\,\Lambda = g$" with "$\Lambda$ preserves $X\cdot Y$" rests on the fact that a symmetric bilinear form is determined by its diagonal (quadratic form) through polarisation. This is exactly why the [[Thm - Invariance of the Spacetime Interval|interval-invariance theorem]] — which is literally "preserves $\Delta s^2 = X\cdot X$" — already characterises the Lorentz group: invariance of the quadratic form forces invariance of the full bilinear form. Whenever you see "preserves the norm" you may upgrade for free to "preserves the inner product", and whenever a problem gives you a transformation preserving all lengths, you may conclude it preserves all angles and inner products too. This upgrade is one of the most frequently used moves in all of relativistic computation, and its engine is the one-line polarisation identity.
