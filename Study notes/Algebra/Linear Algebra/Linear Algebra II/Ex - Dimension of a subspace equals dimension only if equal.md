---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Subspace"
  - "Def - Dimension"
  - "Def - Basis"
  - "Thm - Every Linearly Independent List Extends to a Basis"
  - "Thm - Bases are Equinumerous"
tags: [algebra, linear-algebra]
---

# Problem Statement

(LADR 2.39.) Suppose $V$ is finite-dimensional and $U$ is a subspace of $V$ with $\dim U = \dim V$. Prove that $U = V$.

**Recall.** A [[Def - Subspace|subspace]] $U$ of a vector space $V$ is a subset closed under addition and scalar multiplication that contains $0$. The [[Def - Dimension|dimension]] $\dim V$ of a finite-dimensional space is the length of any basis (well-defined by [[Thm - Bases are Equinumerous|LADR 2.34]]). A subspace of a finite-dimensional space is itself finite-dimensional, with $\dim U \leq \dim V$ ([[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|LADR 2.25]] and its corollary).

The crucial theorem here is [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]]: every linearly independent list extends to a basis. This is what closes the loop in the proof.

---

# Convergent Strategy

**Problem class:** This is the *equality-from-dimension* problem, one of the most-used patterns in §2C. The problem class is "two [[Def - Subspace|subspaces]], one inside the other, with the same dimension; show they are equal". The technique generalises immediately to any context where one wants to bypass element-by-element comparison in favor of a dimension count.

**Assumption pattern:** Two hypotheses: $U \subseteq V$ (containment) and $\dim U = \dim V$ (numerical equality). The conclusion is $U = V$ — an equality of [[Def - Subspace|subspaces]]. The challenge is to convert the numerical equality into the set equality without ever computing what is in $V \setminus U$.

**Theorem routing:** The route is: take a basis of $U$, view it as a linearly independent list in $V$ (independence is preserved when expanding the ambient), apply [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] to extend to a basis of $V$. By [[Thm - Bases are Equinumerous|2.34]], the extension has length $\dim V = \dim U$, equal to the original basis of $U$. So the extension adds zero vectors — the original list is already a basis of $V$. Hence its span is $V$, and the span is $U$, so $U = V$.

**Key decision point:** The non-obvious move is recognising that **a basis of $U$ is also a linearly independent list in $V$**. This is the structural insight: linear independence is a property of the list and the scalar field, not of the ambient space — it does not "lose" or "gain" when we view the list in a larger space. This is the bridge that lets us apply 2.32 inside $V$ to a list originally chosen inside $U$.

---

# Legal Operations Used

1. **Bound a subspace dimension by extending a basis to the ambient (operation 5).** Take a basis of $U$, view it in $V$, extend by 2.32.

2. **Apply the length-of-basis shortcut (operation 3).** Implicitly: the extended list has length $\dim V$, and it is independent (basis of $U$, viewed in $V$), so [[Ex - A list with the right length is a basis iff spanning iff independent]] says it is a basis of $V$.

3. **Apply [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] explicitly.** The extension procedure adjoins additional vectors to form a basis of $V$; when no vectors are needed, the original list was already a basis.

---

# Hints

> [!note]- Hint 1
> Pick a basis of $U$. View it as a list in $V$. Is it still linearly independent?

> [!note]- Hint 2
> Linear independence is a property of the list and the scalar field, not of the ambient space. So a basis of $U$ is a linearly independent list in $V$.

> [!note]- Hint 3
> Apply [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]] to the basis of $U$ (viewed as an independent list in $V$). The extension produces a basis of $V$. What is its length?

> [!note]- Hint 4
> Every basis of $V$ has length $\dim V$ (by [[Thm - Bases are Equinumerous|2.34]]). And every basis of $U$ has length $\dim U$. By hypothesis these are equal. So the extension procedure adds zero vectors. What does this mean about the basis of $U$?

---

# Solution

**Plan.** Take a basis of $U$, view it as a linearly independent list in $V$, extend to a basis of $V$ via [[Thm - Every Linearly Independent List Extends to a Basis|2.32]]. The extension adds zero vectors (because $\dim U = \dim V$, so the basis of $U$ already has the maximum allowed length). Hence the basis of $U$ is itself a basis of $V$, and its span is therefore both $U$ and $V$, forcing $U = V$.

**Step 1: Pick a basis of $U$, and view it in $V$.**

> [!note]- Derivation
> By [[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|LADR 2.25]], $U$ is finite-dimensional (as a subspace of finite-dimensional $V$). So $U$ has a basis $u_1, \ldots, u_m$, where $m = \dim U$.
>
> The list $u_1, \ldots, u_m$ is, by definition of basis, linearly independent in $U$. Linear independence is a property of the list and the scalar field: the equation $a_1 u_1 + \cdots + a_m u_m = 0$ (in $U$, equivalently in $V$, since they share the zero vector) has only the trivial solution. So $u_1, \ldots, u_m$ is also linearly independent in $V$.

**Step 2: Extend to a basis of $V$ using LADR 2.32.**

> [!note]- Derivation
> Since $u_1, \ldots, u_m$ is linearly independent in the finite-dimensional space $V$, by [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]] this list extends to a basis $u_1, \ldots, u_m, w_1, \ldots, w_k$ of $V$, for some $k \geq 0$ and some vectors $w_1, \ldots, w_k \in V$.

**Step 3: Length analysis forces $k = 0$.**

> [!note]- Derivation
> By [[Thm - Bases are Equinumerous|LADR 2.34]], every basis of $V$ has length $\dim V$. So the extended basis has length $\dim V$. As a list, the extended basis has length $m + k = \dim U + k$.
>
> By hypothesis, $\dim U = \dim V$. So $\dim U + k = \dim V = \dim U$, giving $k = 0$.

**Step 4: Conclude $U = V$.**

> [!note]- Derivation
> Since $k = 0$, the "extended" basis is just $u_1, \ldots, u_m$ — the original basis of $U$. So $u_1, \ldots, u_m$ is a basis of $V$.
>
> By definition of basis, $\operatorname{span}(u_1, \ldots, u_m) = V$. But $u_1, \ldots, u_m$ is also a basis of $U$, so $\operatorname{span}(u_1, \ldots, u_m) = U$.
>
> Hence $U = V$. $\qquad\blacksquare$

> [!note]- Sanity check by the length-of-basis shortcut
> An alternative route: by [[Ex - A list with the right length is a basis iff spanning iff independent]], a linearly independent list of length $\dim V$ in $V$ is automatically a basis of $V$. The basis $u_1, \ldots, u_m$ of $U$, viewed in $V$, has length $m = \dim U = \dim V$ and is linearly independent in $V$. So it is automatically a basis of $V$. Hence $V = \operatorname{span}(u_1, \ldots, u_m) = U$.
>
> This route is essentially the same argument repackaged: the length-of-basis shortcut *is* the consequence of 2.32 combined with 2.34, derived in that exercise.

> [!note]- Complete formal solution
> Let $V$ be a finite-dimensional vector space and $U \subseteq V$ a subspace with $\dim U = \dim V$. We show $U = V$.
>
> By [[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|LADR 2.25]], $U$ is finite-dimensional. Let $u_1, \ldots, u_m$ be a basis of $U$, with $m = \dim U$.
>
> The list $u_1, \ldots, u_m$ is linearly independent in $V$: any non-trivial vanishing combination in $V$ would also be one in $U$ (since both spaces share the same zero vector), contradicting independence of the basis of $U$.
>
> Since $V$ is finite-dimensional and $u_1, \ldots, u_m$ is linearly independent in $V$, by [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]] this list extends to a basis $u_1, \ldots, u_m, w_1, \ldots, w_k$ of $V$ for some $k \geq 0$.
>
> By [[Thm - Bases are Equinumerous|LADR 2.34]], every basis of $V$ has length $\dim V$. So $m + k = \dim V = \dim U = m$, giving $k = 0$.
>
> Hence $u_1, \ldots, u_m$ is itself a basis of $V$, so $\operatorname{span}(u_1, \ldots, u_m) = V$. But $u_1, \ldots, u_m$ is also a basis of $U$, so $\operatorname{span}(u_1, \ldots, u_m) = U$. Therefore $U = V$. $\qquad\blacksquare$

---

# Key Takeaways

**Dimension-equality forces space-equality in nested finite-dimensional subspaces.** This is the "non-shrinking" property of subspaces of equal dimension: in a finite-dimensional space, a subspace of full dimension is the whole space. The exercise's converse is trivial — if $U = V$ then $\dim U = \dim V$ — so the exercise is the "shrinking direction": equality of [[Def - Dimension|dimensions]], in the presence of containment, forces equality of subspaces. This is a *uniquely finite-dimensional* phenomenon: in infinite-dimensional spaces, a proper subspace can be isomorphic to the whole space ($\ell^2$ has many proper subspaces isomorphic to itself, e.g. the closed span of $e_2, e_3, e_4, \ldots$).

**Linear independence is a property of the list and the field, not of the ambient space.** This is the structural fact that allows a basis of $U$ to be reused as an independent list in $V$. The exercise illustrates the bidirectional nature of independence: a list that is independent in $U$ stays independent when viewed in $V$, and a list that is independent in $V$ but lies inside $U$ is independent in $U$. The notion is *intrinsic to the list*. (Spanning, by contrast, is *not* a property of the list alone — it depends on what is being spanned. A list can span $U$ but not span $V$.)

**The result is one half of "subspace lattice is a complete lattice with dimension as a rank function".** The subspaces of a finite-dimensional $V$, ordered by inclusion, form a complete modular lattice. Dimension is the **rank function** on this lattice — a function assigning a non-negative integer to each subspace, monotone with respect to inclusion (containment), and satisfying $\dim U + \dim W = \dim(U + W) + \dim(U \cap W)$ (the dimension formula). Modular lattices with rank functions are studied in matroid theory; this exercise is the property *"the rank function takes its maximum exactly on the top element of the lattice"*. The maximum of dimension is $\dim V$, achieved only on $V$ itself.

**Trigger-reaction pattern.** "Two subspaces with $U \subseteq V$, asked whether $U = V$ → compute their [[Def - Dimension|dimensions]]; if equal, conclude $U = V$." This is one of the most-used techniques in §2C and beyond. Every problem of the form "show this subspace is the whole space" in finite dimensions reduces, via this exercise, to a dimension count.
