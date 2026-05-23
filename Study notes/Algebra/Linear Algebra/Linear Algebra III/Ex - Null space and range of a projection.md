---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
  - "Thm - Fundamental Theorem of Linear Maps"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a vector space and let $P \in \mathcal{L}(V)$ satisfy $P^2 = P$. (Such an operator is called a **projection** or **idempotent**.) Prove that
$$V \;=\; \operatorname{null} P \;\oplus\; \operatorname{range} P.$$

That is, the null space and the range of $P$ are *complementary [[Def - Subspace|subspaces]]* — every $v \in V$ is uniquely $u + w$ with $u \in \operatorname{null} P$ and $w \in \operatorname{range} P$.

**Recall:**

![[Def - Null Space and Range#The Definition]]

Two [[Def - Subspace|subspaces]] $U_1, U_2 \subseteq V$ form a **direct sum** $V = U_1 \oplus U_2$ if every $v \in V$ is uniquely expressible as $v = u_1 + u_2$ with $u_i \in U_i$, equivalently $V = U_1 + U_2$ and $U_1 \cap U_2 = \{0\}$.

A linear map $P$ with $P^2 = P$ is called **idempotent**. Geometric examples: orthogonal projection onto a subspace; projection onto $U_1$ along $U_2$ when $V = U_1 \oplus U_2$.

---

# Convergent Strategy

**Problem class.** This is a *prove a direct sum decomposition* problem. The topic-page Problem-Solving Strategy classifies it under "decompose a domain via $V = \operatorname{null} T \oplus U$": find a complement of the null space, and show it equals the range.

**Assumption pattern.** $P^2 = P$ is the defining feature. This identity is what links the null space and the range — without it, $\operatorname{null} P$ and $\operatorname{range} P$ are arbitrary subspaces (Step 1: their [[Def - Dimension|dimensions]] are bound by [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] but they need not be complementary).

**Theorem routing.** The route is: prove (i) $V = \operatorname{null} P + \operatorname{range} P$ (sum, using $v = (v - Pv) + Pv$), and (ii) $\operatorname{null} P \cap \operatorname{range} P = \{0\}$ (intersection, using $P^2 = P$ to show that a vector in both is zero). These two together imply the direct sum decomposition by the standard direct-sum-criterion.

**Key decision point.** The crucial recognition is the algebraic identity $v = (v - Pv) + Pv$. The term $v - Pv$ is in the null space (since $P(v - Pv) = Pv - P^2 v = Pv - Pv = 0$), and $Pv$ is in the range. This is the *unique* way to split a generic $v$, and the trick is to write this identity down and notice both pieces have the required properties. The "key decision" is using $P^2 = P$ specifically in the form $P(Pv) = Pv$ to conclude that $v - Pv \in \operatorname{null} P$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Decompose a domain via $V = \operatorname{null} T \oplus U$** (operation 9). The conclusion *is* such a decomposition with $U = \operatorname{range} P$.

2. **Compute the null space and range** (operation 2). Used in computing that $v - Pv \in \operatorname{null} P$ and $Pv \in \operatorname{range} P$.

3. **Apply rank–nullity to convert one dimension into another** (operation 3). Used as a sanity check: $\dim \operatorname{null} P + \dim \operatorname{range} P = \dim V$ in the finite-dimensional case, consistent with the direct-sum decomposition.

---

# Hints

> [!note]- Hint 1
> What is the most natural way to write a general $v \in V$ as a sum of "something in $\operatorname{null} P$" and "something in $\operatorname{range} P$"? Try $v = (v - Pv) + Pv$.

> [!note]- Hint 2
> Verify: $(v - Pv) \in \operatorname{null} P$ using $P^2 = P$, and $Pv \in \operatorname{range} P$ by definition. So $V = \operatorname{null} P + \operatorname{range} P$.

> [!note]- Hint 3
> For the intersection $\operatorname{null} P \cap \operatorname{range} P = \{0\}$: suppose $v$ is in both. Then $v = Pw$ for some $w$ (range), and $Pv = 0$ (null space). Apply $P$ to $v = Pw$ and use $P^2 = P$.

---

# Solution

The plan: show $V = \operatorname{null} P + \operatorname{range} P$ via the identity $v = (v - Pv) + Pv$, where both summands are in the appropriate subspace by the idempotent identity $P^2 = P$. Then show the intersection is trivial. The two together give the direct sum decomposition.

**Step 1: $V = \operatorname{null} P + \operatorname{range} P$.**

Every $v \in V$ decomposes as $v = (v - Pv) + Pv$, with $v - Pv \in \operatorname{null} P$ and $Pv \in \operatorname{range} P$.

> [!note]- Derivation
> Let $v \in V$. Define $u := v - Pv$ and $w := Pv$. Clearly $v = u + w$.
>
> Check $u \in \operatorname{null} P$: $P u = P(v - Pv) = Pv - P^2 v = Pv - Pv = 0$ (using $P^2 = P$).
>
> Check $w \in \operatorname{range} P$: $w = Pv$ is by definition the image of $v$ under $P$, hence in $\operatorname{range} P$.
>
> Hence every $v \in V$ is a sum of an element of $\operatorname{null} P$ and an element of $\operatorname{range} P$.

**Step 2: $\operatorname{null} P \cap \operatorname{range} P = \{0\}$.**

If $v$ is in both, then $v = 0$.

> [!note]- Derivation
> Let $v \in \operatorname{null} P \cap \operatorname{range} P$. From $v \in \operatorname{range} P$, write $v = Pw$ for some $w \in V$. From $v \in \operatorname{null} P$, $Pv = 0$.
>
> Apply $P$ to $v = Pw$: $Pv = P(Pw) = P^2 w = Pw = v$ (using $P^2 = P$ in the middle step). So $Pv = v$.
>
> But we also have $Pv = 0$. Hence $v = 0$.

**Step 3: Conclude.**

Steps 1 and 2 together give $V = \operatorname{null} P \oplus \operatorname{range} P$.

> [!note]- Derivation
> The standard criterion for a direct sum $V = U_1 \oplus U_2$: $V = U_1 + U_2$ and $U_1 \cap U_2 = \{0\}$. Step 1 gives the first; Step 2 gives the second. So the decomposition is direct: every $v \in V$ is *uniquely* expressible as $u + w$ with $u \in \operatorname{null} P$, $w \in \operatorname{range} P$.

> [!note]- Complete formal solution
> Let $P \in \mathcal{L}(V)$ satisfy $P^2 = P$.
>
> **$V = \operatorname{null} P + \operatorname{range} P$.** For any $v \in V$, write $v = (v - Pv) + Pv$. Then $P(v - Pv) = Pv - P^2 v = Pv - Pv = 0$, so $v - Pv \in \operatorname{null} P$. And $Pv \in \operatorname{range} P$ by definition.
>
> **$\operatorname{null} P \cap \operatorname{range} P = \{0\}$.** If $v \in \operatorname{null} P \cap \operatorname{range} P$, write $v = Pw$ for some $w$. Then $Pv = P^2 w = Pw = v$, so $v = Pv = 0$ (using $v \in \operatorname{null} P$, i.e., $Pv = 0$).
>
> Hence $V = \operatorname{null} P \oplus \operatorname{range} P$. $\blacksquare$

> [!note]- Sanity check via rank–nullity
> If $V$ is finite-dimensional, [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] gives $\dim V = \dim \operatorname{null} P + \dim \operatorname{range} P$, which is consistent with the direct-sum decomposition $V = \operatorname{null} P \oplus \operatorname{range} P$ (where [[Def - Dimension|dimensions]] of complementary subspaces add to the dimension of the whole space). Conversely, the direct-sum decomposition makes the rank–nullity equation transparent — and even gives a constructive isomorphism $V \cong \operatorname{null} P \oplus \operatorname{range} P$.

---

# Key Takeaways

**The identity $v = (v - Pv) + Pv$ is the key trick for projection decompositions.** Whenever a problem involves an idempotent operator $P$ (or, more generally, any operator with an algebraic identity like $P^2 = P$), this addition-and-subtraction trick splits a vector into the part $P$ kills and the part $P$ preserves. The reusable principle is that *algebraic identities of operators generate decompositions of the underlying space*. The trigger is "you have an operator with a polynomial identity" (idempotent, nilpotent, involution, etc.); the move is to write down the decomposition implied by the identity.

**Idempotents are exactly the projections onto complementary subspace pairs.** This exercise gives one direction: an idempotent $P$ gives a direct-sum decomposition $V = \operatorname{null} P \oplus \operatorname{range} P$, with $P$ acting as the identity on $\operatorname{range} P$ and as zero on $\operatorname{null} P$. The converse also holds: given any direct sum $V = U_1 \oplus U_2$, the **projection onto $U_1$ along $U_2$** (sending $u_1 + u_2 \mapsto u_1$) is an idempotent with $\operatorname{null} = U_2$ and $\operatorname{range} = U_1$. So idempotents and direct-sum decompositions are in bijective correspondence. The reusable principle: any direct-sum problem can be reformulated in terms of idempotents, and vice versa. This is essential in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|eigenspace decomposition]]: each eigenspace projection is an idempotent.

**Algebraic identities on operators are constraints on similarity classes.** Saying $P^2 = P$ is saying $P$ satisfies the polynomial $x^2 - x = x(x - 1)$. The roots of this polynomial — $0$ and $1$ — are the eigenvalues of any projection $P$. Moreover, the operator is **diagonalisable** (with eigenvalues $0$ and $1$) iff it satisfies $x^2 - x = 0$, equivalently $P^2 = P$. Other algebraic identities give similar information: $P^2 = I$ (involution) makes $P$ diagonalisable with eigenvalues $\pm 1$; $P^k = 0$ for some $k$ (nilpotent) means all eigenvalues are zero. The reusable principle: the **minimal polynomial** of an operator (the lowest-degree polynomial it satisfies) controls its similarity class — see [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---
