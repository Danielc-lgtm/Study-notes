---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a vector space and $U, W$ be subspaces of $V$. Prove that

$$U \cup W \text{ is a subspace of } V \quad \Longleftrightarrow \quad U \subseteq W \text{ or } W \subseteq U.$$

In words: the union of two subspaces is a subspace if and only if one of them contains the other.

(LADR Exercise 1C.12.)

**Recall:**

A [[Def - Subspace|subspace]] is a non-empty subset closed under addition and scalar multiplication:

![[Def - Subspace#The Definition]]

The **union** of two sets is $U \cup W = \{v : v \in U \text{ or } v \in W\}$.

---

# Convergent Strategy

**Problem class:** This is a **biconditional characterization** problem — establish equivalence between two seemingly different conditions on a pair of subspaces. The pattern is to prove each direction separately; usually one direction is easy and one is the substance of the problem.

**Assumption pattern:** Two subspaces $U, W$, with no further structure specified. The proof must work for arbitrary subspaces of arbitrary vector spaces (over $\mathbb{R}$ or $\mathbb{C}$, where this exercise specifically holds — for $\mathbb{F}_2$ the result fails for three subspaces, but for two it holds over any field).

**Theorem routing:** The easy direction (if $U \subseteq W$ then $U \cup W = W$ is a subspace, and similarly with roles reversed) is set-theoretic. The substantive direction (if $U \cup W$ is a subspace, then $U \subseteq W$ or $W \subseteq U$) is proved by **contrapositive**: assume *neither* $U \subseteq W$ nor $W \subseteq U$, find vectors $u \in U \setminus W$ and $w \in W \setminus U$, and exhibit $u + w$ as an element of $V$ that is in neither $U$ nor $W$ — violating $U \cup W$'s closure under addition.

**Key decision point:** The non-obvious choice is the **contrapositive direction**: rather than trying to derive containment directly, prove the contrapositive (failure of containment $\Rightarrow$ failure of subspace property). The reason this is forced: "either $U \subseteq W$ or $W \subseteq U$" is an existential-like assertion that is hard to attack head-on; its negation gives concrete witnesses $u, w$ to manipulate. The pattern "biconditional with a disjunctive conclusion → use contrapositive" recurs throughout algebra.

---

# Legal Operations Used

1. **Verify the subspace closure conditions on $U \cup W$.** The result of the subspace check pins down what is being violated when the conclusion fails — exposing $u + w$ as a non-element of the union.

2. **Manipulate set differences and complements: $u \in U \setminus W$ means $u \in U$ and $u \notin W$.** This is the basic set-theoretic tool that lets us extract concrete witnesses to non-containment.

3. **Contrapositive and proof by contradiction.** The substantive direction uses the contrapositive of "subspace → one contains the other": assume neither contains the other and derive that the union fails closure.

4. **Use subspace closure to deduce: if $u + w \in U$ and $u \in U$, then $w \in U$.** This is the cancellation step that closes the contradiction: subspace closure under inverses (via $-u \in U$) combined with closure under addition gives $w = (u + w) - u \in U$ — contradicting $w \notin U$.

---

# Hints

> [!note]- Hint 1
> Prove the two directions separately. One direction is easy.

> [!note]- Hint 2
> Easy direction: if $U \subseteq W$, what is $U \cup W$?

> [!note]- Hint 3
> Hard direction: prove the *contrapositive*. Assume $U \not\subseteq W$ and $W \not\subseteq U$. Find vectors $u \in U \setminus W$ and $w \in W \setminus U$. Consider $u + w$: which subspace is it in?

> [!note]- Hint 4
> Suppose $u + w \in U \cup W$. Case $u + w \in U$: combined with $u \in U$, this gives $w = (u + w) - u \in U$ (closure under subtraction in $U$), contradicting $w \notin U$. Case $u + w \in W$: symmetric.

> [!note]- Hint 5
> If neither $u + w \in U$ nor $u + w \in W$, then $u + w \notin U \cup W$ — violating closure under addition. Either way, the union is not a subspace.

---

# Solution

The proof breaks into two directions. The forward direction (subspace $\Rightarrow$ one contains the other) is proved by contrapositive: assuming neither containment, we produce vectors $u \in U \setminus W$, $w \in W \setminus U$ whose sum $u + w$ cannot lie in either subspace, violating closure. The reverse direction is essentially trivial: if $U \subseteq W$ then $U \cup W = W$, which is a subspace.

**Step 1: Reverse direction. If $U \subseteq W$ or $W \subseteq U$, then $U \cup W$ is a subspace.**

If $U \subseteq W$ then $U \cup W = W$, which is a subspace. Symmetrically if $W \subseteq U$ then $U \cup W = U$.

> [!note]- Derivation
> Suppose $U \subseteq W$. Then every element of $U$ is in $W$, so $U \cup W = W$. By hypothesis $W$ is a subspace, so $U \cup W = W$ is a subspace. The case $W \subseteq U$ is symmetric: then $U \cup W = U$ is a subspace.

**Step 2: Forward direction (contrapositive). If $U \not\subseteq W$ and $W \not\subseteq U$, then $U \cup W$ is not a subspace.**

We assume neither containment, extract witnesses $u \in U \setminus W$ and $w \in W \setminus U$, and show $u + w$ is in neither $U$ nor $W$.

> [!note]- Derivation
> By assumption $U \not\subseteq W$, so there exists $u \in U \setminus W$ (i.e. $u \in U$ and $u \notin W$). Similarly $W \not\subseteq U$ gives $w \in W \setminus U$. Consider $u + w$. We will show $u + w \notin U \cup W$, which contradicts closure of $U \cup W$ under addition (if it were a subspace).
>
> *Sub-claim: $u + w \notin U$.* Suppose for contradiction $u + w \in U$. Since $u \in U$ and $U$ is a subspace (closed under additive inverses), $-u \in U$, hence $w = (u + w) + (-u) \in U$ by closure of $U$ under addition. But this contradicts $w \notin U$.
>
> *Sub-claim: $u + w \notin W$.* Suppose for contradiction $u + w \in W$. Since $w \in W$ and $W$ is closed under additive inverses, $-w \in W$, hence $u = (u + w) + (-w) \in W$ by closure of $W$. But this contradicts $u \notin W$.
>
> Hence $u + w \notin U \cup W$, but $u \in U \subseteq U \cup W$ and $w \in W \subseteq U \cup W$, so $u, w \in U \cup W$ and $u + w \notin U \cup W$. So $U \cup W$ is not closed under addition, hence not a subspace.

> [!note]- Complete formal solution
> **Claim.** Let $U, W$ be subspaces of a vector space $V$. Then $U \cup W$ is a subspace if and only if $U \subseteq W$ or $W \subseteq U$.
>
> *Proof.* ($\Leftarrow$) If $U \subseteq W$, then $U \cup W = W$, which is a subspace by hypothesis. The case $W \subseteq U$ is symmetric.
>
> ($\Rightarrow$) We prove the contrapositive: if $U \not\subseteq W$ and $W \not\subseteq U$, then $U \cup W$ is not a subspace.
>
> Choose $u \in U \setminus W$ (exists since $U \not\subseteq W$) and $w \in W \setminus U$ (exists since $W \not\subseteq U$). Suppose for contradiction that $u + w \in U \cup W$. Then either $u + w \in U$ or $u + w \in W$.
>
> *Case 1.* $u + w \in U$. Since $u \in U$ and $U$ is a subspace, $-u \in U$ and so $w = (u + w) - u \in U$, contradicting $w \notin U$.
>
> *Case 2.* $u + w \in W$. Since $w \in W$, $-w \in W$ and so $u = (u + w) - w \in W$, contradicting $u \notin W$.
>
> Both cases yield contradictions, so $u + w \notin U \cup W$. But $u, w \in U \cup W$ (each is in one of $U, W$), so $U \cup W$ contains $u, w$ but not $u + w$ — violating closure under addition. Hence $U \cup W$ is not a subspace. $\blacksquare$

> [!warning] Illegal but tempting: assuming subspaces are linear, hence transversal subspaces fail closure "by genericity"
> A tempting non-proof goes: "if $U$ and $W$ are transversal (neither contains the other), then a generic $u + w$ moves out of the union, so closure fails". This is geometric intuition, not proof. The genuine argument extracts a *specific* sum $u + w$ from witnesses and shows it lies in neither piece by exploiting closure under inverses. Without the cancellation step $w = (u + w) - u$, the argument has no engine: closure alone of $U \cup W$ does not contradict anything until we exhibit a concrete violation.

---

# Key Takeaways

**The sum, not the union, is the right join in the subspace lattice.** This exercise pins down precisely when the union of two subspaces "accidentally" remains a subspace: when one contains the other, in which case the union is just the bigger one. In all other cases the union fails closure under addition. The structural consequence is that the union is *not* the join in the lattice $\operatorname{Sub}(V)$: to get the smallest subspace containing both $U$ and $W$ one must add their elements together, forming the [[Def - Sum of Subspaces|sum]] $U + W$. Recognizing this asymmetry — sums are joins, unions are not — is the cleanest mental handle on the subspace lattice. The same pattern appears for any algebraic substructure: in [[Def - Group|group theory]] the smallest subgroup containing $H \cup K$ is the subgroup *generated* by the union, $\langle H \cup K \rangle$, which equals $HK$ for normal $K$, and exceeds the union in general. The union is generally a wrong-shaped object that the algebraic join repairs.

**The contrapositive is the right form for "biconditional with disjunctive conclusion".** When you face an "iff" whose conclusion is a disjunction ("$X$ or $Y$"), trying to prove $X$ or $Y$ directly from the hypothesis is often awkward. The contrapositive — "not $X$ and not $Y$ implies not the hypothesis" — converts a disjunction into a conjunction, which is much easier to work with: it hands you two concrete pieces of information. Here, "neither $U \subseteq W$ nor $W \subseteq U$" gives two witness vectors to manipulate, and their sum is the explicit violation we need. The same maneuver works for: "the polynomial $p$ is reducible $\Leftrightarrow$ $p = q$ or $p = r$ in such-and-such factorization scheme" (contrapositive: $p$ irreducible $\Leftrightarrow$ no such factorization exists, which gives explicit testing), and "the linear map $T$ is invertible $\Leftrightarrow$ injective or surjective in some setting" (contrapositive: $T$ fails invertibility iff witnesses to failure of both). Whenever your conclusion has "or", look at "and-not".

**Subspaces' closure under subtraction is the structural reason this proof works.** The step $w = (u + w) - u$ is the load-bearing manipulation: it uses that subspaces are closed under both addition and additive inverses, equivalently under subtraction. Without subtraction the cancellation could not be performed. This is a special feature of *abelian* algebraic structures (and of any structure with inverses); for non-abelian groups one must be careful with the order of multiplication, and the same technique generalizes only with care. The lesson: *closure under subtraction* (= closure under addition + inverses) is the actual workhorse closure property of subspaces, and is what licenses the standard "express one element as a difference of two known elements" move.

**The result extends partially to more subspaces, with the failure being the subject of a separate exercise.** For three subspaces over an *infinite* field, the result extends: the union of three subspaces is a subspace if and only if one of them contains the union of the other two — i.e. one of them is the largest. But this version fails over $\mathbb{F}_2$ (the two-element field), where $\mathbb{F}_2^2$ has three nontrivial proper subspaces of dimension $1$ whose union is all of $\mathbb{F}_2^2$ but no one of which contains the others — see [LADR Exercise 1C.13](https://linear.axler.net/) and the general result that "no vector space over an infinite field is a finite union of proper subspaces" (a classical qualifying-exam result; [see arXiv 0803.2746](https://arxiv.org/pdf/0803.2746)). The lesson is that union-fails-subspace results depend on the field, and the simple two-subspace case here is special in being field-independent. Recognizing field-sensitivity is a skill that pays dividends in any classification theorem.
