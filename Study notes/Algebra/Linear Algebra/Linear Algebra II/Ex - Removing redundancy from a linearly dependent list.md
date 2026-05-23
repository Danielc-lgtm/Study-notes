---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Linear Independence"
  - "Def - Linear Combination and Span"
tags: [algebra, linear-algebra]
---

# Problem Statement

(LADR 2.21, illustrative example.) Consider the list
$$(1, 2, 3),\;(6, 5, 4),\;(15, 16, 17),\;(8, 9, 7)$$
in $\mathbb{R}^3$.

(a) Show that this list is linearly dependent.

(b) Find the smallest $k \in \{1, 2, 3, 4\}$ such that the $k$th vector lies in the span of its predecessors (this $k$ is identified by the linear dependence lemma). For this $k$, exhibit the explicit linear combination of the predecessors that equals the $k$th vector.

**Recall.** A list $v_1, \ldots, v_m$ is [[Def - Linear Independence|linearly dependent]] if some nontrivial combination vanishes, equivalently (linear dependence lemma, LADR 2.19) some $v_k$ lies in $\operatorname{span}(v_1, \ldots, v_{k-1})$. Removing this $v_k$ does not change the span of the list.

A list of length $> \dim V$ is automatically dependent: in $\mathbb{R}^3$, any list of length $\geq 4$ is dependent because four linearly independent vectors would contradict the length inequality ([[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|LADR 2.22]]) applied to the basis $e_1, e_2, e_3$ of $\mathbb{R}^3$.

---

# Convergent Strategy

**Problem class:** This is a *find-the-first-redundancy* problem, the diagnostic use of the linear dependence lemma. Given a list known to be dependent, identify the *smallest* index $k$ such that $v_k$ is a combination of its predecessors — this is the "first place dependency appears" in the left-to-right reading order. The technique generalises to identifying the structure of dependencies in any list, and it is the inner workhorse of the reduction algorithm in [[Thm - Every Spanning List Contains a Basis|LADR 2.30]].

**Assumption pattern:** The list has length 4 in a 3-dimensional space, so it is automatically dependent (no list of length 4 is independent in $\mathbb{R}^3$). The dependency could appear at $k = 1$, 2, 3, or 4. The procedure: test each $k$ in order. $k = 1$ requires $v_1 \in \operatorname{span}() = \{0\}$, i.e. $v_1 = 0$. $k = 2$ requires $v_2 \in \operatorname{span}(v_1)$, i.e. $v_2$ is a scalar multiple of $v_1$. $k = 3$ requires $v_3 \in \operatorname{span}(v_1, v_2)$, a 2D linear system. $k = 4$ would require $v_4 \in \operatorname{span}(v_1, v_2, v_3)$, a 3D linear system.

**Theorem routing:** The lemma 2.19 says the smallest such $k$ exists in any dependent list, and identifies the redundant vector. The procedure is to test $k = 1, 2, 3, 4$ in order and stop at the first that works. The output is the value of $k$ together with the explicit coefficients in the combination $v_k = \sum b_i v_i$.

**Key decision point:** Solving a 2D linear system is unavoidable for testing $k = 3$. The student must be comfortable manipulating linear systems, recognising consistency, and reading off explicit coefficients. For higher [[Def - Dimension|dimensions]] the systems grow, and Gaussian elimination is the standard tool.

---

# Legal Operations Used

1. **Test scalar-multiple dependency.** For $k = 2$: check whether $v_2 = c v_1$ for some scalar $c$. Equivalently, the ratios of coordinates must be the same. Easy: $(6, 5, 4) = c(1, 2, 3)$ would require $c = 6/1 = 5/2 = 4/3$, all of which differ.

2. **Test 2D-span membership via linear system.** For $k = 3$: $v_3 = a v_1 + b v_2$ is a system of 3 equations in 2 unknowns. Solve the first two and check the third.

3. **Solve a linear system by elimination.** Standard manipulation.

---

# Hints

> [!note]- Hint 1
> Check $k = 1, 2, 3, 4$ in order. The smallest one for which $v_k$ is in the span of the predecessors is the answer.

> [!note]- Hint 2
> $k = 1$: $v_1 = (1, 2, 3)$ should be the zero vector. It is not, so $k = 1$ does not work.
>
> $k = 2$: $(6, 5, 4) = c(1, 2, 3)$ for some $c$? Check the ratios: $6/1 = 6$, $5/2 = 2.5$, $4/3 \approx 1.33$. Different, so $(6, 5, 4)$ is not a scalar multiple of $(1, 2, 3)$. $k = 2$ does not work.

> [!note]- Hint 3
> $k = 3$: $(15, 16, 17) = a(1, 2, 3) + b(6, 5, 4)$? Set up the system: $15 = a + 6b$, $16 = 2a + 5b$, $17 = 3a + 4b$. Solve the first two for $a, b$, then check the third.

> [!note]- Hint 4
> Solving the first two equations: from the first, $a = 15 - 6b$. Substituting into the second: $16 = 2(15 - 6b) + 5b = 30 - 7b$, so $b = 2$. Then $a = 15 - 12 = 3$. Check the third: $3a + 4b = 9 + 8 = 17$. ✓ So $(15, 16, 17) = 3(1, 2, 3) + 2(6, 5, 4)$. The smallest $k$ is $k = 3$.

---

# Solution

**Plan.** The list is automatically dependent (length 4 in $\mathbb{R}^3$). We find the smallest $k$ for which $v_k \in \operatorname{span}(v_1, \ldots, v_{k-1})$ by trying $k = 1, 2, 3, 4$ in order. We expect $k = 3$ given the example's setup; we verify by solving an explicit linear system.

**Step 1: The list is linearly dependent.**

> [!note]- Derivation
> Length 4 in $\mathbb{R}^3$. By [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|LADR 2.22]] applied to any list of length $> \dim V = 3$, the list cannot be linearly independent. So it is dependent.

**Step 2: Test $k = 1$.**

> [!note]- Derivation
> Is $v_1 = (1, 2, 3) \in \operatorname{span}()$? The span of the empty list is $\{0\}$. $(1, 2, 3) \neq 0$, so no. $k = 1$ does not work.

**Step 3: Test $k = 2$.**

> [!note]- Derivation
> Is $v_2 = (6, 5, 4) \in \operatorname{span}((1, 2, 3))$? Equivalently, is $(6, 5, 4) = c(1, 2, 3)$ for some $c \in \mathbb{R}$? From the first coordinate, $c = 6$. But then $c \cdot 2 = 12$, while the second coordinate of $v_2$ is 5. So no. $k = 2$ does not work.

**Step 4: Test $k = 3$.**

> [!note]- Derivation
> Is $v_3 = (15, 16, 17) \in \operatorname{span}((1, 2, 3), (6, 5, 4))$? Set up the system $v_3 = a v_1 + b v_2$:
> $$\begin{cases} 15 = a + 6b \\ 16 = 2a + 5b \\ 17 = 3a + 4b \end{cases}$$
> From the first equation: $a = 15 - 6b$. Substituting into the second: $16 = 2(15 - 6b) + 5b = 30 - 12b + 5b = 30 - 7b$, so $7b = 14$, $b = 2$. Then $a = 15 - 12 = 3$. Check the third equation: $3a + 4b = 9 + 8 = 17$. ✓
>
> So $(15, 16, 17) = 3 \cdot (1, 2, 3) + 2 \cdot (6, 5, 4)$, hence $v_3 \in \operatorname{span}(v_1, v_2)$.

**Step 5: Conclude.**

> [!note]- Derivation
> The smallest $k$ such that $v_k \in \operatorname{span}(v_1, \ldots, v_{k-1})$ is $k = 3$, with the explicit relation
> $$(15, 16, 17) = 3 \cdot (1, 2, 3) + 2 \cdot (6, 5, 4).$$
>
> By [[Def - Linear Combination and Span|the linear dependence lemma]], removing $(15, 16, 17)$ from the list does not change the span. Equivalently, the relation
> $$3 \cdot (1, 2, 3) + 2 \cdot (6, 5, 4) - 1 \cdot (15, 16, 17) + 0 \cdot (8, 9, 7) = 0$$
> witnesses the linear dependence of the original list.

> [!note]- Sanity check
> Verify the dependence relation directly: $3 \cdot (1, 2, 3) = (3, 6, 9)$, $2 \cdot (6, 5, 4) = (12, 10, 8)$. Sum: $(15, 16, 17)$. So $3 v_1 + 2 v_2 = v_3$, i.e. $3 v_1 + 2 v_2 - v_3 = 0$, a nontrivial vanishing combination. ✓

> [!note]- Complete formal solution
> The list $(1, 2, 3), (6, 5, 4), (15, 16, 17), (8, 9, 7)$ in $\mathbb{R}^3$ has length 4. Since $\dim \mathbb{R}^3 = 3$, by [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|LADR 2.22]] applied with the standard basis as a spanning list of length 3, no linearly independent list in $\mathbb{R}^3$ has length 4. So the list is linearly dependent. This proves part (a).
>
> We find the smallest $k$ such that $v_k \in \operatorname{span}(v_1, \ldots, v_{k-1})$.
>
> *$k = 1$:* $v_1 = (1, 2, 3) \in \operatorname{span}()$ would require $v_1 = 0$, but $v_1 \neq 0$. Skip.
>
> *$k = 2$:* $v_2 = (6, 5, 4) = c \cdot (1, 2, 3)$ for some $c$ would require $c = 6$ (from the first coordinate) and $c = 5/2$ (from the second), inconsistent. Skip.
>
> *$k = 3$:* Solve $(15, 16, 17) = a \cdot (1, 2, 3) + b \cdot (6, 5, 4)$. The first two equations give $a + 6b = 15$, $2a + 5b = 16$, with solution $a = 3, b = 2$. Verify the third: $3 \cdot 3 + 4 \cdot 2 = 9 + 8 = 17$. ✓ So $v_3 = 3 v_1 + 2 v_2$, and $v_3 \in \operatorname{span}(v_1, v_2)$.
>
> The smallest $k$ is $k = 3$, and the explicit relation is $(15, 16, 17) = 3 \cdot (1, 2, 3) + 2 \cdot (6, 5, 4)$. This proves part (b).
> $\qquad\blacksquare$

---

# Key Takeaways

**The linear dependence lemma identifies the *first* redundancy in left-to-right reading.** When a list is dependent, the lemma guarantees that *some* $v_k$ lies in the span of its predecessors; this exercise illustrates how to find the smallest such $k$ by direct testing. The technique is the bookkeeping device that drives the reduction algorithm in [[Thm - Every Spanning List Contains a Basis|2.30]] — at each step, that algorithm asks the same question and deletes the redundant vector. So the exercise is the *atom* of the reduction procedure, and mastering it is a prerequisite for fluently extracting bases from spanning lists.

**Testing membership in a 2D span is a 3-equation, 2-unknown linear system in $\mathbb{R}^3$.** The system is overdetermined (3 equations, 2 unknowns), so it usually has no solution; when it *does* have a solution, that means the third vector is dependent on the first two. The procedure is: solve the first two equations for the two unknowns, then check whether the solution is consistent with the third equation. This is the standard "is this vector in the span of those two" test, and it generalises mechanically to higher [[Def - Dimension|dimensions]] (Gaussian elimination on a matrix).

**The dependence relation has a sign convention.** Once you know $v_3 = 3 v_1 + 2 v_2$, you can express the dependence as $3 v_1 + 2 v_2 - v_3 = 0$. The "$-1$" coefficient of $v_3$ comes from moving it to the other side of the equation. This sign convention shows up in every linear-dependence calculation: the redundant vector picks up a coefficient $-1$ (or any nonzero constant after rescaling) in the vanishing combination.

**Trigger-reaction pattern.** "List of length $> \dim V$ → automatically dependent. To find the first redundancy, test $k = 1, 2, \ldots$ in order, testing each $v_k$ against the span of its predecessors via a linear system." This is the diagnostic technique. In a problem like [[Ex - Constructing a basis from a spanning list]], the same testing identifies which vectors to *delete* from the list — it is the same algorithm, used for a slightly different output.
