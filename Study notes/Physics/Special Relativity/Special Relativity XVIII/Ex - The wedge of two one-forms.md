---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - Tensor Operations"
tags: [physics, special-relativity]
---

# Problem Statement

Work in mostly-minus signature, $c = 1$.

1. From the definition $a\wedge b = a\otimes b - b\otimes a$ for one-forms, compute the components $(a\wedge b)_{\mu\nu}$ and verify they are antisymmetric.
2. Evaluate $(a\wedge b)(\vec v, \vec w)$ on two vectors, and show it equals the $2\times 2$ determinant $\langle a, \vec v\rangle\langle b, \vec w\rangle - \langle a, \vec w\rangle\langle b, \vec v\rangle$.
3. Show $a\wedge a = 0$ for any one-form $a$, and that $a\wedge b = 0$ if and only if $a$ and $b$ are linearly dependent.
4. Count the number of independent components of $a\wedge b$ for one-forms in four dimensions, and interpret the wedge geometrically as the oriented plane (bivector) spanned by $a$ and $b$.

**Recall:**

![[Def - Alternate Forms and the Exterior Product#The Definition]]

The [[Def - Alternate Forms and the Exterior Product|exterior product]] of two one-forms is $a\wedge b = a\otimes b - b\otimes a$, an antisymmetric type-$(0,2)$ tensor (a $2$-form). The [[Def - Tensor Operations|tensor product]] of one-forms acts by $(a\otimes b)(\vec v, \vec w) = \langle a, \vec v\rangle\langle b, \vec w\rangle$.

---

# Convergent Strategy

**Problem class.** A *compute-a-tensor-operation* problem exercising the [[Def - Alternate Forms and the Exterior Product|exterior product]] at its simplest. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: expand the definition in components and read off the structure.

**Assumption pattern.** Only the definition $a\wedge b = a\otimes b - b\otimes a$ and the action of a tensor product on vectors are needed. Antisymmetry is built into the definition; the determinant structure emerges from the two-term difference; linear dependence controls vanishing.

**Theorem routing.** Part 1: read components off the definition. Part 2: apply to $(\vec v, \vec w)$ using the tensor-product action. Part 3: set $b = a$ (or $b = \lambda a$) and watch the terms cancel. Part 4: count antisymmetric $4\times 4$ components.

**Key decision point.** The crux is recognising the wedge of two one-forms as a *determinant* — the $2\times 2$ minor built from the four pairings. This determinant structure is what makes the wedge measure oriented area, vanish on dependent inputs, and antisymmetrise. Seeing $a\wedge b$ as "the determinant that detects whether $a, b$ and $\vec v, \vec w$ are aligned" is the conceptual payoff.

---

# Legal Operations Used

1. **Operation 4 from the topic page (wedge two forms).** The entire exercise is the wedge of two one-forms, computed from the definition $a\wedge b = a\otimes b - b\otimes a$.

2. **Operation 3 from the topic page (tensor product).** Used to evaluate $a\otimes b$ on a pair of vectors before subtracting.

---

# Hints

> [!note]- Hint 1
> The components are $(a\wedge b)_{\mu\nu} = (a\wedge b)(e_\mu, e_\nu) = a_\mu b_\nu - b_\mu a_\nu = a_\mu b_\nu - a_\nu b_\mu$. Swapping $\mu\leftrightarrow\nu$ flips the sign — antisymmetric.

> [!note]- Hint 2
> $(a\wedge b)(\vec v, \vec w) = (a\otimes b)(\vec v, \vec w) - (b\otimes a)(\vec v, \vec w) = \langle a, \vec v\rangle\langle b, \vec w\rangle - \langle b, \vec v\rangle\langle a, \vec w\rangle$, which is $\det\begin{pmatrix}\langle a, \vec v\rangle & \langle a, \vec w\rangle \\ \langle b, \vec v\rangle & \langle b, \vec w\rangle\end{pmatrix}$.

> [!note]- Hint 3
> $a\wedge a = a\otimes a - a\otimes a = 0$. More generally, if $b = \lambda a$ then $a\wedge b = \lambda(a\wedge a) = 0$; conversely if $a, b$ independent, some pair $\vec v, \vec w$ gives a nonzero determinant.

---

# Solution

The wedge of two one-forms is the simplest non-trivial $2$-form, and it is a determinant in disguise. The plan: extract its antisymmetric components (Step 1), recognise its action as a $2\times2$ determinant (Step 2), show it vanishes exactly on dependent inputs (Step 3), and count its six independent components as an oriented plane (Step 4).

**Step 1: $(a\wedge b)_{\mu\nu} = a_\mu b_\nu - a_\nu b_\mu$, antisymmetric.**

> [!note]- Derivation
> From $a\wedge b = a\otimes b - b\otimes a$, the components are
> $$(a\wedge b)_{\mu\nu} = (a\wedge b)(e_\mu, e_\nu) = \langle a, e_\mu\rangle\langle b, e_\nu\rangle - \langle b, e_\mu\rangle\langle a, e_\nu\rangle = a_\mu b_\nu - b_\mu a_\nu = a_\mu b_\nu - a_\nu b_\mu.$$
> Swapping the indices: $(a\wedge b)_{\nu\mu} = a_\nu b_\mu - a_\mu b_\nu = -(a\wedge b)_{\mu\nu}$. Antisymmetric, confirming $a\wedge b$ is a [[Def - Alternate Forms and the Exterior Product|2-form]]. The diagonal entries $(a\wedge b)_{\mu\mu} = a_\mu b_\mu - a_\mu b_\mu = 0$ vanish, as they must for an antisymmetric array.

**Step 2: $(a\wedge b)(\vec v, \vec w)$ is a $2\times2$ determinant.**

> [!note]- Derivation
> Apply to vectors $\vec v, \vec w$ using the [[Def - Tensor Operations|tensor-product action]] $(a\otimes b)(\vec v, \vec w) = \langle a, \vec v\rangle\langle b, \vec w\rangle$:
> $$(a\wedge b)(\vec v, \vec w) = \langle a, \vec v\rangle\langle b, \vec w\rangle - \langle b, \vec v\rangle\langle a, \vec w\rangle = \det\begin{pmatrix} \langle a, \vec v\rangle & \langle a, \vec w\rangle \\ \langle b, \vec v\rangle & \langle b, \vec w\rangle \end{pmatrix}.$$
> The wedge is the determinant of the matrix of pairings — the oriented "area" of the parallelogram that $a, b$ measure on $\vec v, \vec w$. This determinant structure is the source of every property of the exterior product: antisymmetry (swapping rows or columns flips sign), and vanishing on dependent inputs (a determinant with a repeated row is zero).

**Step 3: $a\wedge b = 0$ iff $a, b$ are linearly dependent.**

> [!note]- Derivation
> *Vanishing on $a = b$.* $a\wedge a = a\otimes a - a\otimes a = 0$. More generally, if $b = \lambda a$ then $a\wedge b = a\wedge(\lambda a) = \lambda(a\wedge a) = 0$. So linear dependence forces $a\wedge b = 0$.
>
> *Converse.* Suppose $a, b$ are linearly *independent*. Extend to a dual basis; there exist vectors $\vec v, \vec w$ with $\langle a, \vec v\rangle = 1, \langle a, \vec w\rangle = 0, \langle b, \vec v\rangle = 0, \langle b, \vec w\rangle = 1$ (the dual basis vectors to $a, b$). Then $(a\wedge b)(\vec v, \vec w) = 1\cdot1 - 0\cdot0 = 1 \neq 0$, so $a\wedge b \neq 0$. Hence $a\wedge b = 0 \iff a, b$ dependent. (This is the determinant criterion: the $2\times2$ minor is nonzero iff the rows are independent.)

**Step 4: six independent components; the oriented plane spanned by $a$ and $b$.**

> [!note]- Derivation
> An antisymmetric $4\times4$ array $(a\wedge b)_{\mu\nu}$ has independent entries only for $\mu < \nu$: the pairs $(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)$ — exactly $\binom{4}{2} = 6$ of them. These six numbers are the **bivector** components, the coordinates of the oriented plane $\mathrm{span}(a, b)$ in $\Lambda^2 E^*$.
>
> Geometrically, $a\wedge b$ encodes the two-dimensional subspace spanned by $a$ and $b$ *together with* an orientation and an area scale: it is unchanged if $a, b$ are replaced by another basis $a', b'$ of the same plane *with the same orientation and area* (since $a'\wedge b' = (\det M)\,a\wedge b$ where $M$ is the change-of-basis in the plane, $= a\wedge b$ when $\det M = 1$). So $a\wedge b$ is the algebraic representation of "the oriented parallelogram spanned by $a$ and $b$" — the two-dimensional generalisation of the way a vector represents an oriented line segment.

> [!note]- Complete formal solution
> **(1)** $(a\wedge b)_{\mu\nu} = a_\mu b_\nu - a_\nu b_\mu$, antisymmetric (sign flips under $\mu\leftrightarrow\nu$; diagonal vanishes).
> **(2)** $(a\wedge b)(\vec v, \vec w) = \langle a, \vec v\rangle\langle b, \vec w\rangle - \langle a, \vec w\rangle\langle b, \vec v\rangle = \det\begin{pmatrix}\langle a,\vec v\rangle & \langle a,\vec w\rangle\\ \langle b,\vec v\rangle & \langle b,\vec w\rangle\end{pmatrix}$.
> **(3)** $a\wedge a = 0$; if $b = \lambda a$ then $a\wedge b = 0$; if $a, b$ independent, the dual vectors give $(a\wedge b)(\vec v,\vec w) = 1$, so $a\wedge b = 0 \iff a, b$ dependent.
> **(4)** Six independent components ($\binom{4}{2}$, pairs $\mu<\nu$); $a\wedge b$ is the oriented plane (bivector) spanned by $a$ and $b$. $\blacksquare$

---

# Key Takeaways

**The wedge of two one-forms is a determinant, and that determinant is the source of every property.** The single most useful way to think about $a\wedge b$ is as the $2\times2$ determinant $\det\begin{pmatrix}\langle a,\vec v\rangle & \langle a,\vec w\rangle\\ \langle b,\vec v\rangle & \langle b,\vec w\rangle\end{pmatrix}$ of the pairings with two test vectors. Antisymmetry is "swapping two rows of a determinant flips its sign"; vanishing on dependent forms is "a determinant with a repeated row is zero"; the oriented-area interpretation is "a $2\times2$ determinant is a signed area." This determinant viewpoint extends: the wedge of $p$ one-forms is a $p\times p$ determinant, which is why the top wedge $e^0\wedge e^1\wedge e^2\wedge e^3$ computes the full $4\times4$ determinant and why a linear map acts on it by $\det$. Whenever you meet a wedge, picture the determinant of pairings — it tells you immediately when the wedge vanishes (aligned inputs) and what it measures (oriented volume).

**$a\wedge a = 0$ and the dependence criterion are the engine of "wedge kills repetition."** The identity $a\wedge a = 0$, and more generally that a wedge vanishes exactly when its factors are linearly dependent, is what makes the exterior algebra finite and computationally tame: any term in which a one-form repeats drops out. This is used constantly to simplify computations — in $F = dA$ with $A = A_\mu dx^\mu$, the wedge $dx^\mu\wedge dx^\mu$ vanishes, so only the off-diagonal terms of $\partial_\nu A_\mu$ survive (giving the curl structure of the field strength); in checking that a basis of $p$-forms is non-redundant; in proving $d^2 = 0$. The trigger to internalise: any repeated factor in a wedge means the term is zero, and any wedge of more one-forms than the dimension of the space is automatically zero. This single fact removes most of the terms in any exterior-algebra calculation before you compute anything.

**A bivector is to an oriented plane what a vector is to an oriented line.** The six components of $a\wedge b$ encode not the two forms $a$ and $b$ individually but the oriented two-dimensional subspace they span, with an area scale. Two different pairs of one-forms spanning the same oriented plane with the same area give the *same* wedge — the wedge forgets the individual factors and remembers only the plane. This is the geometric meaning of a $2$-form's six components in four dimensions: they parametrise the oriented $2$-planes (the Grassmannian), exactly as a vector's four components parametrise oriented directions. For the electromagnetic field, this is why the six numbers $(\mathbf E, \mathbf B)$ are naturally the components of a $2$-form rather than two separate vectors — they specify an oriented plane in spacetime at each event. The transferable idea: a $p$-form is the algebraic encoding of an oriented $p$-dimensional element, the natural object to integrate over a $p$-surface.
