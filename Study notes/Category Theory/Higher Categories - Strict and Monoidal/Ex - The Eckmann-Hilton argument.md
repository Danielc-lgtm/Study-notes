---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Strict n-Category and Strict ω-Category"
  - "Def - 2-Category and Bicategory"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $S$ be a set carrying **two** binary operations $\circ$ and $\star$ that:
- share a common two-sided unit $e$ (so $e\circ a = a\circ e = a$ and $e\star a = a\star e = a$ for all $a$), and
- satisfy the **interchange law** $(a\star b)\circ(c\star d) = (a\circ c)\star(b\circ d)$ for all $a,b,c,d\in S$.

(a) **Eckmann–Hilton.** Prove that $\circ = \star$, that this common operation is associative *and commutative*, and that $e$ is its unit.

(b) Interpret the result in a strict $2$-category: the $2$-cells $\alpha:1_A\Rightarrow 1_A$ from the identity $1$-cell of an object $A$ to itself form a [[Def - Monoid in a Monoidal Category|commutative monoid]] under either ($=$ both) composition; equivalently, the **endomorphisms of the identity object** in a [[Def - Monoidal Category|monoidal category]] form a commutative monoid.

(c) Deduce the topological corollary: the higher homotopy groups $\pi_n(X,x)$ are **abelian** for $n\geq 2$.

**Recall:**

In a [[Def - Strict n-Category and Strict ω-Category|strict 2-category]], $2$-cells admit vertical composition $\circ_1$ and horizontal composition $\circ_0$, subject to the [[Thm - The Interchange Law|interchange law]]; identity $2$-cells are units for both. A [[Def - Monoid in a Monoidal Category|commutative monoid]] is a monoid whose multiplication satisfies $ab=ba$.

---

# Convergent Strategy

**Problem class:** This is a *dimension-shift / forced-structure* problem from the topic page: a purely algebraic identity (interchange) is shown to force commutativity, and the consequence is read off at three levels (sets, $2$-categories, topology). It is the canonical demonstration that interchange is the seed of commutativity.

**Assumption pattern:** The only hypotheses are a shared unit and interchange. The unlock is to feed *units* into the four slots of the interchange law: inserting $e$'s in clever positions makes the two operations collide. Recognising that "shared unit + interchange" is enough to force everything — equality, associativity, commutativity — is the entire content; no other axiom is used.

**Theorem routing:** Part (a) is a direct four-line manipulation of the interchange law with strategic unit insertions. Part (b) routes through the topic page's [[Def - 2-Category and Bicategory|monoidal = one-object bicategory]] identification: $2$-cells on the identity $1$-cell are endo-$2$-cells with two compositions sharing a unit, so (a) applies. Part (c) routes through the standard fact that $\pi_n(X)$ carries two concatenation operations (in two coordinate directions) sharing a unit and satisfying interchange, so (a) again applies.

**Key decision point:** The non-obvious moves are the *specific unit insertions*. To prove $\circ=\star$ you compute $a\star b$ by writing $a = a\circ e$, $b = e\circ b$ and applying interchange; to prove commutativity you write $a = e\star a$, $b = b\star e$ instead. Choosing where to place the units is the whole trick; a reader who does not see which slots to fill will be stuck despite having all the hypotheses. The trap is trying to prove commutativity directly without first establishing $\circ=\star$.

---

# Legal Operations Used

1. **Operation 8 from the topic page (run the Eckmann–Hilton argument).** Part (a) *is* operation 8: two unital operations sharing a unit and interchanging are equal, associative, and commutative.

2. **Operation 7 from the topic page (restrict to one object/cell to descend the periodic table).** Part (b) restricts a $2$-category to the identity $1$-cell of one object, landing in the degenerate situation operation 8 governs.

---

# Hints

> [!note]- Hint 1
> Everything follows from inserting the shared unit $e$ into the four slots of $(a\star b)\circ(c\star d)=(a\circ c)\star(b\circ d)$ and using that $e$ is a unit for both operations.

> [!note]- Hint 2
> To compare the two operations, compute $a\circ b$ by writing $a = a\star e$ and $b = e\star b$ (legal since $e$ is a $\star$-unit), then apply interchange to $(a\star e)\circ(e\star b)$.

> [!note]- Hint 3
> The same computation read with the roles of $\circ$ and $\star$ swapped gives the reverse equality; combining the two collapses $\circ$ and $\star$ to one operation. Then to get commutativity, run interchange on $(e\star a)\circ(b\star e)$.

> [!note]- Hint 4
> For (b): in a [[Def - Monoidal Category|monoidal category]], the unit object $I$ has $\mathrm{End}(I)=\{f:I\to I\}$ with two operations — composition $\circ$ and tensor $\otimes$ (restricted to endomorphisms of $I$, using $I\otimes I\cong I$) — sharing the unit $1_I$ and interchanging. For (c): $\pi_n$ has horizontal and vertical concatenation of $n$-cubes/spheres.

---

# Solution

The plan: (a) four short applications of interchange with unit insertions, in the order "$\circ=\star$, then commutative, then associative." (b) and (c) are the same algebraic fact applied to two standard structures that have two unital interchanging operations. The entire result flows from the four-slot interchange identity fed with units.

**Step 1: $\circ = \star$.**

> [!note]- Derivation
> Take any $a,b\in S$. Using that $e$ is a unit for $\star$, write $a = a\star e$ and $b = e\star b$. Then
> $$a\circ b = (a\star e)\circ(e\star b) \overset{\text{interchange}}{=} (a\circ e)\star(e\circ b) = a\star b,$$
> using that $e$ is a unit for $\circ$ in the last step. So $a\circ b = a\star b$ for all $a,b$: the two operations are **equal**. Write $\cdot$ for the common operation.

**Step 2: Commutativity.**

> [!note]- Derivation
> Now use the *other* unit insertion. Write $a = e\star a$ and $b = b\star e$. Then
> $$a\cdot b = a\circ b = (e\star a)\circ(b\star e) \overset{\text{interchange}}{=} (e\circ b)\star(a\circ e) = b\star a = b\cdot a,$$
> using Step 1 ($\star=\circ=\cdot$) and the unit laws. So $a\cdot b = b\cdot a$: the common operation is **commutative**.

**Step 3: Associativity and unit.**

> [!note]- Derivation
> Associativity: take $a,b,c$ and insert a unit to expose interchange. Compute, using $e$ as the $\star$-unit,
> $$(a\cdot b)\cdot c = (a\cdot b)\circ(e\star c) = (a\star e)\circ(b\dots)\dots$$
> Cleanly: since $\circ=\star=\cdot$ and using interchange once more,
> $$(a\cdot b)\cdot c = (a\star b)\circ(e\star c) = (a\circ e)\star(b\circ c) = a\star(b\circ c) = a\cdot(b\cdot c).$$
> So $\cdot$ is **associative**. The unit: $e$ is a unit for both $\circ$ and $\star$ by hypothesis, hence for $\cdot$. Therefore $(S,\cdot,e)$ is a **commutative monoid**, and the originally distinct $\circ,\star$ are one and the same commutative-monoid operation.

**Step 4: The $2$-categorical and topological corollaries.**

> [!note]- Derivation
> *(b) Strict $2$-category.* Fix an object $A$ and consider the $2$-cells $\alpha:1_A\Rightarrow 1_A$ (endo-$2$-cells of the identity $1$-cell). These are closed under both vertical composition $\circ_1$ and horizontal composition $\circ_0$ (since $1_A\circ_0 1_A = 1_A$, horizontal composition of such $2$-cells lands back among them). Both compositions have the same unit, the identity $2$-cell $1_{1_A}$, and they satisfy the [[Thm - The Interchange Law|interchange law]]. By (a), $\circ_0=\circ_1$ and the common operation is a **commutative monoid** on $\mathrm{End}(1_A)$. The monoidal-category version is the same statement via [[Def - 2-Category and Bicategory|monoidal = one-object bicategory]]: the endomorphisms of the unit object $I$ carry composition and tensor (using $I\otimes I\cong I$), sharing the unit $1_I$ and interchanging, so $\mathrm{End}(I)$ is a commutative monoid. (For $\mathbf{Vect}_k$ this recovers that $\mathrm{End}(k)=k$ is commutative.)
>
> *(c) Higher homotopy groups.* For $n\geq 2$, an element of $\pi_n(X,x)$ is a homotopy class of maps $(I^n,\partial I^n)\to(X,x)$ from the $n$-cube. There are $n$ different concatenation operations $+_i$ ($1\leq i\leq n$), gluing two cubes along the $i$-th coordinate direction; all share the constant map as unit, and any two of them, say $+_1$ and $+_2$, satisfy the interchange law (gluing in direction $1$ then direction $2$ equals gluing in direction $2$ then direction $1$, up to reparametrization, which is a homotopy). Since $n\geq 2$ there *are* at least two such operations. By (a) applied to $\pi_n(X,x)$ with $\circ=+_1$, $\star=+_2$: the two are equal and the group is **abelian**. For $n=1$ there is only one concatenation, so the argument does not apply, consistent with $\pi_1$ being generally non-abelian.

> [!note]- Complete formal solution
> **(a)** Writing $a=a\star e$, $b=e\star b$: $a\circ b=(a\star e)\circ(e\star b)=(a\circ e)\star(e\circ b)=a\star b$, so $\circ=\star=:\,\cdot$. Writing $a=e\star a$, $b=b\star e$: $a\cdot b=(e\star a)\circ(b\star e)=(e\circ b)\star(a\circ e)=b\cdot a$, so $\cdot$ is commutative. And $(a\cdot b)\cdot c=(a\star b)\circ(e\star c)=(a\circ e)\star(b\circ c)=a\cdot(b\cdot c)$, so $\cdot$ is associative; $e$ is its unit. Hence $(S,\cdot,e)$ is a commutative monoid and $\circ=\star$.
>
> **(b)** In a strict $2$-category, $\mathrm{End}(1_A)$ is closed under $\circ_0,\circ_1$, both with unit $1_{1_A}$ and satisfying interchange, so by (a) it is a commutative monoid with $\circ_0=\circ_1$. Equivalently $\mathrm{End}(I)$ in a [[Def - Monoidal Category|monoidal category]] is a commutative monoid under $\circ$ ($=\otimes$).
>
> **(c)** For $n\geq 2$, $\pi_n(X,x)$ carries the concatenations $+_1,+_2$ in two coordinate directions, sharing the constant unit and satisfying interchange (Fubini-type reparametrization homotopy); by (a) they coincide and the group is abelian. $\pi_1$ has only one concatenation, so it may be non-abelian. $\qquad\blacksquare$

---

# Key Takeaways

**Interchange plus a shared unit forces commutativity — this is the deepest reason commutativity appears in higher mathematics.** The Eckmann–Hilton argument shows that you almost never need to *assume* commutativity at high dimensions; it is *forced* by the interaction of two operations through interchange. Wherever two unital operations share a unit and interchange — endo-$2$-cells of an identity, endomorphisms of a monoidal unit, higher homotopy groups, the homotopy groups of a topological monoid, the cohomology of an $H$-space — commutativity is automatic. The trigger to internalise is exactly this configuration: *two unital operations on the same elements with a common unit.* When you see it, expect (and exploit) commutativity rather than working to prove it. This single mechanism unifies the abelianness of $\pi_n$, the commutativity of cup product on even classes' interaction, and the symmetry that appears as you climb the periodic table.

**The proof is entirely strategic unit insertion — placing $e$ in the right slots, not algebraic force.** The argument carries no computation beyond four applications of one identity; all the cleverness is in *where* the units go. To prove $\circ=\star$ you decompose each factor with $e$ on the *outside* ($a\star e$, $e\star b$); to prove commutativity you decompose with $e$ on the *inside-swapped* positions ($e\star a$, $b\star e$). This is a reusable proof pattern: when an algebraic identity relates two operations, probe it by substituting the unit into selected arguments, because the unit is the one element that lets you rewrite a single factor as a product without changing it. The same "insert the unit to expose the interaction" tactic recurs in proving that bialgebra structures are compatible, that grouplike elements form a group, and in many Hopf-algebra computations.

**The periodic table predicts the abelianness of $\pi_n$ a century before you compute anything.** Part (c) is not a separate topological theorem but the same algebra applied to a structure that happens to be topological. In the periodic-table frame, $\pi_n(X,x)$ is a $k$-tuply monoidal structure with $k\geq 2$ for $n\geq 2$ (it lives several dimensions up with everything below degenerate), and the table says such structures are at least *braided*, in fact symmetric, hence the group is abelian. This is the explanatory power of the unifying frame: a hard-won classical fact (Hurewicz-era, that higher homotopy groups are abelian) becomes an immediate corollary of "two interchanging operations commute." Whenever a classical result asserts unexpected commutativity at high dimension, look for the two interchanging operations — they are almost always there, and Eckmann–Hilton is doing the work.
