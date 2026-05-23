---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Basis"
  - "Def - Dimension"
  - "Thm - Length of Linearly Independent List Bounded by Length of Spanning List"
  - "Thm - Every Spanning List Contains a Basis"
  - "Thm - Every Linearly Independent List Extends to a Basis"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional vector space with $\dim V = n$, and let $v_1, \ldots, v_n$ be a list of $n$ vectors in $V$. Prove that the following are equivalent:

1. $v_1, \ldots, v_n$ is a [[Def - Basis|basis]] of $V$.
2. $v_1, \ldots, v_n$ is linearly independent.
3. $v_1, \ldots, v_n$ spans $V$.

(This is LADR 2.38 and 2.42 combined; it is the **length-of-basis shortcut**, operation 3 from the topic page.)

**Recall.**

![[Def - Basis#The Definition]]

The relevant theorems are:

- **Length inequality (LADR 2.22).** ![[Thm - Length of Linearly Independent List Bounded by Length of Spanning List#Statement]]

- **Spanning list contains a basis (LADR 2.30).** ![[Thm - Every Spanning List Contains a Basis#Statement]]

- **Independent list extends to a basis (LADR 2.32).** ![[Thm - Every Linearly Independent List Extends to a Basis#Statement]]

---

# Convergent Strategy

**Problem class:** This is a *length-of-basis* problem, the canonical use of the length inequality together with the two structural theorems of §2B. The problem class is "given a list of the right length, show that one of the two basis conditions implies the other for free." Almost every concrete problem of showing "$v_1, \ldots, v_n$ is a basis of $V$" passes through this shortcut when $\dim V = n$ is known: instead of verifying both spanning *and* independence, you verify only one and invoke this equivalence.

**Assumption pattern:** The crucial assumption is the **length** of the list: $n = \dim V$. This length being exactly the [[Def - Dimension|dimension]] is what makes the shortcut available — too short and the list cannot span, too long and it cannot be independent. Both the structural theorems (2.30 reducing spanning to basis, 2.32 extending independence to basis) preserve the basis property and either decrease or increase length, so when the input length equals the basis length, no actual reduction or extension can happen.

**Theorem routing:** (1) $\implies$ (2) and (1) $\implies$ (3) are trivial by the definition of basis. (2) $\implies$ (1) uses [[Thm - Every Linearly Independent List Extends to a Basis|2.32]]: a linearly independent list of length $n$ extends to a basis, but every basis has length $n$, so no extension is needed — the list is *already* a basis. (3) $\implies$ (1) uses [[Thm - Every Spanning List Contains a Basis|2.30]]: a spanning list of length $n$ reduces to a basis, but every basis has length $n$, so no reduction is needed — the list is *already* a basis. The equivalence (2) $\iff$ (3) follows by composing through (1).

**Key decision point:** The crucial step is recognising that "every basis has length $n$" — the well-definedness of [[Def - Dimension|dimension]] by [[Thm - Bases are Equinumerous|2.34]] — is what closes the loops. Without 2.34, the reduction/extension would produce a basis of some unknown length, and one could not conclude that the procedure does *nothing*. Students sometimes forget this dependency and produce circular proofs.

---

# Legal Operations Used

1. **Reduce a spanning list to a basis (operation 1).** Applied to a spanning list of length $n$: reduction is the identity if no vector is redundant, and otherwise produces a basis of length $< n$. Combined with 2.34, the latter is impossible — every basis has length $n$.

2. **Extend an independent list to a basis (operation 2).** Applied to an independent list of length $n$: extension adds vectors making the basis longer, or adds zero vectors. The former contradicts 2.34; the latter is the desired outcome.

3. **Length-of-basis shortcut (operation 3).** This *is* the operation being demonstrated.

---

# Hints

> [!note]- Hint 1
> Both directions (independent $\implies$ basis) and (spanning $\implies$ basis) use one structural theorem of §2B together with the well-definedness of dimension.

> [!note]- Hint 2
> For (2) $\implies$ (1): apply [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] to the independent list. It produces a basis containing the original list. What can you say about the length of that basis?

> [!note]- Hint 3
> Every basis of $V$ has length $\dim V = n$, by [[Thm - Bases are Equinumerous|2.34]]. So the extension promised by 2.32 has length $n$ — the same as the original list. Hence the extension adds zero vectors. The original list was already a basis.

---

# Solution

**Plan.** The proof has three implications to verify: (1) $\implies$ (2), (1) $\implies$ (3), and the symmetric pair (2) $\implies$ (1) and (3) $\implies$ (1). The first two are trivial by definition. The non-trivial step is (2) $\implies$ (1), which uses 2.32 to extend the list to a basis, and 2.34 to argue the extension is trivial because both objects already have length $n$. The dual argument gives (3) $\implies$ (1) using 2.30. Together these give all three equivalences.

**Step 1: (1) $\implies$ (2) and (1) $\implies$ (3) are immediate.**

> [!note]- Derivation
> By definition, a basis is a list that is both linearly independent and spans $V$. So if $v_1, \ldots, v_n$ is a basis, it is linearly independent (giving (2)) and spans $V$ (giving (3)).

**Step 2: (2) $\implies$ (1). A linearly independent list of length $n$ is a basis.**

> [!note]- Derivation
> Suppose $v_1, \ldots, v_n$ is linearly independent in $V$. By [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]], this list extends to a basis $v_1, \ldots, v_n, w_1, \ldots, w_k$ of $V$ for some $k \geq 0$ and some vectors $w_j \in V$ (the extension is constructive but its specific form is not needed here).
>
> By [[Thm - Bases are Equinumerous|LADR 2.34]] (well-definedness of dimension), every basis of $V$ has length $\dim V = n$. So the extended basis has length $n$. But it also has length $n + k$. Therefore $k = 0$: no vectors are added in the extension.
>
> Hence the original list $v_1, \ldots, v_n$ *is* the basis produced by the extension procedure. So $v_1, \ldots, v_n$ is a basis of $V$.

**Step 3: (3) $\implies$ (1). A spanning list of length $n$ is a basis.**

> [!note]- Derivation
> Dually to Step 2. Suppose $v_1, \ldots, v_n$ spans $V$. By [[Thm - Every Spanning List Contains a Basis|LADR 2.30]], this list reduces to a basis $B$ that is a sublist of $v_1, \ldots, v_n$. The reduction has length $\leq n$.
>
> By [[Thm - Bases are Equinumerous|LADR 2.34]], $|B| = \dim V = n$. So the reduction has length exactly $n$, equal to the original list's length. Hence no vectors are deleted: the reduction is the original list.
>
> So $v_1, \ldots, v_n$ is itself the basis produced by the reduction. It is a basis of $V$.

**Step 4: Combine.**

> [!note]- Derivation
> (1) $\Leftrightarrow$ (2) is the conjunction of Step 1 (forward direction) and Step 2 (backward direction).
>
> (1) $\Leftrightarrow$ (3) is the conjunction of Step 1 (forward direction) and Step 3 (backward direction).
>
> Hence (2) $\Leftrightarrow$ (3) by composition: (2) $\Rightarrow$ (1) $\Rightarrow$ (3) and conversely.

> [!note]- Complete formal solution
> Let $v_1, \ldots, v_n$ be a list of $n$ vectors in $V$ where $n = \dim V$.
>
> **(1) $\Rightarrow$ (2) and (1) $\Rightarrow$ (3).** By [[Def - Basis|definition]], a basis is a list that is linearly independent and spans $V$. So if $v_1, \ldots, v_n$ is a basis, it satisfies both (2) and (3).
>
> **(2) $\Rightarrow$ (1).** Assume $v_1, \ldots, v_n$ is linearly independent. By [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]], the list extends to a basis $v_1, \ldots, v_n, w_1, \ldots, w_k$ of $V$ for some $k \geq 0$. By [[Thm - Bases are Equinumerous|LADR 2.34]], every basis of $V$ has length $n$, so the extended basis has length $n$. Since the extended basis has length $n + k$ as a list, we get $n + k = n$, so $k = 0$. Hence the original list $v_1, \ldots, v_n$ is itself the basis.
>
> **(3) $\Rightarrow$ (1).** Assume $v_1, \ldots, v_n$ spans $V$. By [[Thm - Every Spanning List Contains a Basis|LADR 2.30]], the list reduces to a basis $B \subseteq \{v_1, \ldots, v_n\}$. By LADR 2.34, $|B| = n$. Since $B$ is a sublist of a list of length $n$ and has length $n$, $B$ is the full list itself. So $v_1, \ldots, v_n$ is a basis.
>
> **(2) $\Leftrightarrow$ (3) follows by composition.** $\qquad\blacksquare$

---

# Key Takeaways

**The length shortcut converts verification from two conditions to one.** This exercise's whole point is operational: when you have a list whose length matches the dimension of the ambient space, you only need to verify *one* of the two basis conditions, not both. This nearly halves the work of "show that this is a basis" problems. The trigger is the appearance of a list of length $\dim V$, the action is "verify independence (usually easier) or spanning (usually harder), whichever is the more economical", and the conclusion is "by 2.38 or 2.42, the list is a basis." Recognising this pattern is essential to efficient problem-solving in §2C and beyond.

**The shortcut depends on well-definedness of dimension.** The argument in Step 2 hinges on "the extended basis has length $n + k$ as a list, but $n$ by 2.34". Without the well-definedness of dimension (2.34), this contradiction-by-counting would not be available, and the shortcut would fail. So the result demonstrates the **utility** of having a basis-independent invariant: the integer $n$ that 2.34 manufactures is what closes the loop. Whenever you use the shortcut, you are implicitly using the dimension theorem.

**The two structural theorems are dual and converge to bases.** The proof uses both 2.30 (spanning $\to$ basis by reduction) and 2.32 (independent $\to$ basis by extension), in symmetric roles. This is the chapter's main message in microcosm: bases are the meeting point of two converging operations, and the shortcut is the corollary of that convergence at the right length. When you internalise this duality, you will see that essentially every problem in §2B and §2C uses one or both of 2.30/2.32, and the length-of-basis shortcut is the immediate Friday-afternoon consequence.

**Counterexamples when the length is wrong.** It is instructive to record what fails when the length differs from $\dim V$. If the list is too short (length $< n$): it cannot span (any spanning list has length $\geq n$ by 2.22 against the basis), so condition (3) fails automatically — even if (2) holds. If the list is too long (length $> n$): it cannot be independent (any independent list has length $\leq n$ by 2.22), so (2) fails automatically. So the equivalence (2) $\iff$ (3) genuinely depends on the length being exactly $n$.
