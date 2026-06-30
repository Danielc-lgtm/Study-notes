---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - Tensor Operations"
tags: [physics, special-relativity]
---

# Problem Statement

Work in four dimensions, $c = 1$.

1. Prove the graded-commutativity rule $B\wedge A = (-1)^{pq}A\wedge B$ for a $p$-form $A$ and a $q$-form $B$. Treat first the case of one-forms ($p = q = 1$), then a one-form and a two-form ($p = 1, q = 2$), then the general case.
2. Deduce that any *odd*-degree form squares to zero under $\wedge$ (e.g. $a\wedge a = 0$ for a one-form, $\omega\wedge\omega = 0$ for a three-form), while an even-degree form need not.
3. Verify associativity $(a\wedge b)\wedge c = a\wedge(b\wedge c)$ for three one-forms by computing both sides on three vectors.
4. Conclude that the wedge of $p$ one-forms is totally antisymmetric in the factors, and vanishes if any two factors coincide.

**Recall:**

![[Def - Alternate Forms and the Exterior Product#The Definition]]

The [[Def - Alternate Forms and the Exterior Product|exterior product]] is associative and graded-commutative: $B\wedge A = (-1)^{pq}A\wedge B$. For one-forms, $a\wedge b = a\otimes b - b\otimes a$. The grading is by degree, and the sign $(-1)^{pq}$ counts the parity of moving a degree-$q$ form past a degree-$p$ form.

---

# Convergent Strategy

**Problem class.** A *structural* problem proving the algebraic identities of the [[Def - Alternate Forms and the Exterior Product|exterior algebra]]. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: work from the definition, tracking signs of permutations.

**Assumption pattern.** The definition of $\wedge$ as an antisymmetrised tensor product, and the parity of permutations, are the only inputs. The sign $(-1)^{pq}$ is the signature of the permutation that interleaves $p$ and $q$ slots — moving each of the $q$ factors of $B$ past each of the $p$ factors of $A$ costs one sign, $pq$ in total.

**Theorem routing.** Part 1: for one-forms, $b\wedge a = b\otimes a - a\otimes b = -(a\wedge b)$ directly; the general case counts the interleaving permutation. Part 2: set $A = B$ of odd degree in the rule. Part 3: expand both triple wedges. Part 4: compose transpositions.

**Key decision point.** The crux is the sign $(-1)^{pq}$: it is *not* always $-1$. Two one-forms anticommute ($(-1)^{1\cdot1} = -1$), but a one-form and a two-form *commute* ($(-1)^{1\cdot2} = +1$). The parity depends on the *product* of degrees. Getting this right — and in particular realising that even-degree forms can commute with everything and need not square to zero — is the lesson, and a common source of sign errors.

---

# Legal Operations Used

1. **Operation 4 from the topic page (wedge two forms).** The entire exercise manipulates wedge products via the sign rule $B\wedge A = (-1)^{pq}A\wedge B$.

2. **Operation 3 from the topic page (tensor product).** Used in parts 1 and 3 to expand wedges of one-forms as antisymmetrised tensor products.

---

# Hints

> [!note]- Hint 1
> For one-forms, $b\wedge a = b\otimes a - a\otimes b = -(a\otimes b - b\otimes a) = -a\wedge b$, so $(-1)^{1\cdot1} = -1$. For a $p$-form past a $q$-form, count the transpositions needed to move the $q$ factors past the $p$ factors: $p\cdot q$ of them, giving $(-1)^{pq}$.

> [!note]- Hint 2
> Set $B = A$ with $A$ of odd degree $p$ in $B\wedge A = (-1)^{pq}A\wedge B$: $A\wedge A = (-1)^{p^2}A\wedge A = (-1)^p A\wedge A = -A\wedge A$ (odd $p$), forcing $A\wedge A = 0$. For even $p$, $(-1)^{p^2} = +1$ and no constraint.

> [!note]- Hint 3
> Both $(a\wedge b)\wedge c$ and $a\wedge(b\wedge c)$ equal the totally antisymmetrised $a\otimes b\otimes c$, i.e. $\sum_{\sigma\in\mathfrak{S}_3}(-1)^{k(\sigma)}a_{\sigma}\otimes b_\sigma\otimes c_\sigma$ — six terms. Compute both groupings and check they agree.

---

# Solution

The exterior algebra's two defining identities — graded-commutativity and associativity — are proved by tracking permutation signs. The plan: prove $B\wedge A = (-1)^{pq}A\wedge B$ case by case (Step 1), deduce that odd forms square to zero (Step 2), verify associativity on a triple wedge (Step 3), and conclude total antisymmetry of a wedge of one-forms (Step 4).

**Step 1: $B\wedge A = (-1)^{pq}A\wedge B$.**

> [!note]- Derivation
> *One-form past one-form ($p = q = 1$).* Directly from the definition,
> $$b\wedge a = b\otimes a - a\otimes b = -(a\otimes b - b\otimes a) = -\,a\wedge b,$$
> so $b\wedge a = (-1)^{1\cdot1}a\wedge b = -a\wedge b$. One-forms anticommute.
>
> *One-form past two-form ($p = 1, q = 2$).* Let $A = a$ (one-form), $B = b\wedge c$ (two-form). Moving $a$ past $b\wedge c$ means moving it past $b$ (one sign) and then past $c$ (one sign): $a\wedge(b\wedge c) = -(b\wedge a)\wedge c = +(b\wedge c)\wedge a$, using one-form anticommutation twice. So $a\wedge B = (+1)B\wedge a$, i.e. $(-1)^{1\cdot2} = +1$: a one-form and a two-form **commute**.
>
> *General case.* Write $A = a_1\wedge\cdots\wedge a_p$ and $B = b_1\wedge\cdots\wedge b_q$ (every form is a sum of such; by bilinearity it suffices to check these). To turn $A\wedge B$ into $B\wedge A$, move each $b_j$ leftward past all $p$ of the $a_i$. Each such pass is $p$ one-form transpositions, contributing $(-1)^p$; doing this for all $q$ of the $b_j$ gives $(-1)^{pq}$. Hence $B\wedge A = (-1)^{pq}A\wedge B$.

**Step 2: odd-degree forms square to zero; even-degree need not.**

> [!note]- Derivation
> Apply the rule with $B = A$ of degree $p$:
> $$A\wedge A = (-1)^{p\cdot p}A\wedge A = (-1)^{p^2}A\wedge A = (-1)^p A\wedge A,$$
> since $p^2 \equiv p \pmod 2$. For **odd** $p$, $(-1)^p = -1$, so $A\wedge A = -A\wedge A$, forcing
> $$A\wedge A = 0 \quad (p \text{ odd}).$$
> Thus $a\wedge a = 0$ for a one-form and $\omega\wedge\omega = 0$ for a three-form. For **even** $p$, $(-1)^p = +1$ and the identity $A\wedge A = A\wedge A$ is vacuous — no constraint — so an even-degree form *can* have $A\wedge A \neq 0$. Example: the field strength $F$ (a two-form) has $F\wedge F = 2(\mathbf E\cdot\mathbf B)\,\varepsilon \neq 0$ in general (it is, up to a constant, the second field invariant). Even forms behave like commuting variables; odd forms like anticommuting (Grassmann) ones.

**Step 3: associativity of the triple wedge.**

> [!note]- Derivation
> For three one-forms $a, b, c$, both $(a\wedge b)\wedge c$ and $a\wedge(b\wedge c)$ equal the totally antisymmetrised tensor product. Compute $(a\wedge b)\wedge c$ on vectors $(\vec u, \vec v, \vec w)$. Using the definition and expanding, the result is the $3\times3$ determinant
> $$\big((a\wedge b)\wedge c\big)(\vec u, \vec v, \vec w) = \det\begin{pmatrix} \langle a,\vec u\rangle & \langle a,\vec v\rangle & \langle a,\vec w\rangle \\ \langle b,\vec u\rangle & \langle b,\vec v\rangle & \langle b,\vec w\rangle \\ \langle c,\vec u\rangle & \langle c,\vec v\rangle & \langle c,\vec w\rangle \end{pmatrix},$$
> the signed sum over the six permutations $\sigma\in\mathfrak{S}_3$ of $(-1)^{k(\sigma)}\langle a,\vec u_{\sigma(1)}\rangle\langle b, \vec u_{\sigma(2)}\rangle\langle c, \vec u_{\sigma(3)}\rangle$. The same expansion of $a\wedge(b\wedge c)$ gives the identical determinant (the determinant does not care how the rows were grouped). Since both equal the same fully-antisymmetrised object, $(a\wedge b)\wedge c = a\wedge(b\wedge c)$. The wedge of $p$ one-forms is the $p\times p$ determinant of pairings, and the determinant is manifestly associative.

**Step 4: total antisymmetry of a wedge of one-forms.**

> [!note]- Derivation
> By Step 1, swapping any two *adjacent* one-form factors flips the sign: $\cdots a_i\wedge a_{i+1}\cdots = -\cdots a_{i+1}\wedge a_i\cdots$. Since any permutation is a composition of adjacent transpositions, swapping any two factors $a_i, a_j$ flips the sign, and a general permutation $\sigma$ gives
> $$a_{\sigma(1)}\wedge\cdots\wedge a_{\sigma(p)} = (-1)^{k(\sigma)}\,a_1\wedge\cdots\wedge a_p.$$
> The wedge is totally antisymmetric in its factors. Consequently, if any two factors coincide ($a_i = a_j$ for $i \neq j$), swapping them leaves the wedge unchanged but the sign rule flips it, so the wedge is $0$. This is why $e^{\alpha_1}\wedge\cdots\wedge e^{\alpha_p}$ is nonzero only for *distinct* indices, recovering the dimension count $\binom{4}{p}$.

> [!note]- Complete formal solution
> **(1)** One-forms: $b\wedge a = b\otimes a - a\otimes b = -a\wedge b$. General: moving each of $q$ factors of $B$ past $p$ factors of $A$ costs $(-1)^{pq}$, so $B\wedge A = (-1)^{pq}A\wedge B$. (One-form $\wedge$ two-form: $(-1)^2 = +1$, they commute.)
> **(2)** $A\wedge A = (-1)^p A\wedge A$, so $A\wedge A = 0$ for odd $p$; for even $p$ no constraint (e.g. $F\wedge F \neq 0$).
> **(3)** Both groupings of $a\wedge b\wedge c$ equal the $3\times3$ determinant of pairings, hence are equal: associativity.
> **(4)** Adjacent swaps flip the sign, so a wedge of one-forms is totally antisymmetric and vanishes if two factors coincide. $\blacksquare$

---

# Key Takeaways

**Graded-commutativity is $(-1)^{pq}$, not $-1$ — even-degree forms can commute and need not square to zero.** The single most error-prone fact in the exterior algebra is that the sign in $B\wedge A = (-1)^{pq}A\wedge B$ depends on the *product* of the degrees. One-forms anticommute ($(-1)^{1\cdot1} = -1$), but a one-form commutes with a two-form ($(-1)^{1\cdot2} = +1$), and two two-forms commute ($(-1)^{2\cdot2} = +1$). The reusable rule: a form behaves like an anticommuting (Grassmann) variable if its degree is *odd*, and like an ordinary commuting variable if its degree is *even*. So odd forms square to zero ($a\wedge a = 0$, $\omega\wedge\omega = 0$ for a three-form), but even forms need not ($F\wedge F \neq 0$ for the field strength — it is the second field invariant). Whenever you reorder a wedge product, compute $(-1)^{pq}$ from the degrees, and never assume the sign is $-1$; this catches a large fraction of sign errors in form computations and is essential for the Chern-form and field-invariant calculations of later chapters.

**A wedge of one-forms is a determinant, and determinants explain associativity and total antisymmetry at once.** The triple wedge $a\wedge b\wedge c$ is the $3\times3$ determinant of pairings, and the $p$-fold wedge of one-forms is the $p\times p$ determinant. This single identification proves both associativity (the determinant is one object regardless of grouping) and total antisymmetry (swapping rows of a determinant flips its sign), and it explains the vanishing on repeated factors (a determinant with a repeated row is zero). The reusable consequence is that any computation with wedges of one-forms can be done as a determinant — and conversely, any determinant can be read as a wedge — which is the bridge between the exterior algebra and linear algebra. The top wedge $e^0\wedge e^1\wedge e^2\wedge e^3$ is the full $4\times4$ determinant, which is why a linear map acts on it by multiplication by $\det$, and why the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] is "the determinant tensor."

**Odd forms are Grassmann variables; this is the algebraic seed of fermions.** The fact that odd-degree forms anticommute and square to zero is not just a computational rule — it is the same algebra that governs fermionic fields in quantum theory. Grassmann (anticommuting) numbers $\theta$ satisfy $\theta^2 = 0$ and $\theta_1\theta_2 = -\theta_2\theta_1$, exactly like one-forms under $\wedge$, and the path integral for fermions is built on this algebra. The transferable insight: whenever an object squares to zero and anticommutes, it is "fermionic," and the exterior algebra is the prototype. In the relativistic setting this connects the differential forms of electromagnetism (bosonic, even-degree field strength) to the spinor fields of matter (fermionic, the Grassmann-odd sector), and it is why supersymmetry — which mixes the two — is naturally formulated with differential forms and Grassmann coordinates on the same footing. For the immediate purposes of this chapter, the lesson is simpler: treat odd forms with the anticommuting-variable rules and even forms with the commuting-variable rules, and the sign bookkeeping becomes automatic.
