---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Vector Space"
tags: [algebra, linear-algebra]
---

# Problem Statement

(a) Show that $\mathbb{F}^\infty$, the set of all sequences $(x_1, x_2, \dots)$ with $x_i \in \mathbb{F}$, is a [[Def - Vector Space|vector space]] over $\mathbb{F}$ under pointwise operations $(x_1, x_2, \dots) + (y_1, y_2, \dots) = (x_1 + y_1, x_2 + y_2, \dots)$ and $\lambda (x_1, x_2, \dots) = (\lambda x_1, \lambda x_2, \dots)$.

(b) More generally, for any nonempty set $S$, show that $\mathbb{F}^S$ — the set of functions $S \to \mathbb{F}$ — is a vector space over $\mathbb{F}$ under pointwise operations.

(LADR Example 1.23 and Exercise 1B.7.)

**Recall:**

A [[Def - Vector Space|vector space]] over $\mathbb{F}$ is a set with pointwise-defined addition and scalar multiplication satisfying:

![[Def - Vector Space#The Definition]]

---

# Convergent Strategy

**Problem class:** This is a **verify-is-a-vector-space** problem — confirm a candidate satisfies all eight axioms. The pattern reuses verification techniques: each axiom translates from the candidate space to the underlying $\mathbb{F}$-arithmetic, where it is known.

**Assumption pattern:** The arithmetic in $\mathbb{F}$ satisfies all the field axioms. The operations on $\mathbb{F}^S$ are pointwise, so each axiom reduces to checking the corresponding property pointwise in $\mathbb{F}$.

**Theorem routing:** Direct — pointwise definitions reduce each vector-space axiom to a field axiom of $\mathbb{F}$. The verification is mechanical but worth doing once to internalize that the "function space" construction works for any vector space, not just $\mathbb{R}$ or $\mathbb{C}$.

**Key decision point:** The non-obvious recognition is that **$\mathbb{F}^n = \mathbb{F}^{\{1, \dots, n\}}$**: tuples are functions from a finite indexing set. So $\mathbb{F}^n, \mathbb{F}^\infty = \mathbb{F}^\mathbb{N}, \mathbb{F}^\mathbb{R}, \mathcal{P}(\mathbb{F}) \subseteq \mathbb{F}^\mathbb{F}$ all fall under the same construction. Recognizing this uniformity is the start of seeing function spaces as the natural generalization of $\mathbb{F}^n$.

---

# Legal Operations Used

1. **Verify a candidate vector space by checking the eight axioms pointwise** (operation 1 from the topic page). Applied here: each axiom of $\mathbb{F}^S$ reduces to its pointwise instance in $\mathbb{F}$. Since $\mathbb{F}$ is a [[Def - Field|field]], the pointwise instances hold by the field axioms, hence the global axioms hold.

2. **Define operations pointwise on a function space.** The pattern $(f + g)(s) := f(s) + g(s)$ and $(\lambda f)(s) := \lambda f(s)$ packages addition and scalar multiplication of functions in terms of operations of the codomain. This is the function-space construction, applicable for any codomain that is itself a vector space (or even just an abelian group, for addition).

---

# Hints

> [!note]- Hint 1
> Each of the eight vector-space axioms involves equations between vectors. With pointwise operations, the equation holds iff it holds at each point.

> [!note]- Hint 2
> The zero vector in $\mathbb{F}^S$ is the constant function $0_S : S \to \mathbb{F}$ with $0_S(s) = 0$ for every $s$. The additive inverse of $f$ is $-f$ defined by $(-f)(s) = -f(s)$.

---

# Solution

Plan: verify each axiom by reducing to its pointwise instance in $\mathbb{F}$.

**Step 1: $\mathbb{F}^S$ is closed under the operations.**

> [!note]- Derivation
> Addition and scalar multiplication of functions $S \to \mathbb{F}$, defined pointwise, are again functions $S \to \mathbb{F}$. So both operations are well-defined.

**Step 2: Verify each vector-space axiom pointwise.**

> [!note]- Derivation
> For each $s \in S$:
> - **Commutativity:** $(f + g)(s) = f(s) + g(s) = g(s) + f(s) = (g + f)(s)$. So $f + g = g + f$.
> - **Associativity of addition:** $((f + g) + h)(s) = f(s) + g(s) + h(s) = (f + (g + h))(s)$.
> - **Additive identity:** $(f + 0_S)(s) = f(s) + 0 = f(s)$, so $f + 0_S = f$.
> - **Additive inverses:** Define $(-f)(s) = -f(s)$; then $(f + (-f))(s) = f(s) - f(s) = 0 = 0_S(s)$.
> - **Multiplicative identity:** $(1 \cdot f)(s) = 1 \cdot f(s) = f(s)$.
> - **Associativity of scalar multiplication:** $((ab) f)(s) = (ab) f(s) = a(b f(s)) = (a (bf))(s)$.
> - **Distributivity over vector addition:** $(a(f + g))(s) = a(f(s) + g(s)) = a f(s) + a g(s) = (af + ag)(s)$.
> - **Distributivity over scalar addition:** $((a + b) f)(s) = (a + b) f(s) = a f(s) + b f(s) = (af + bf)(s)$.
>
> Each axiom holds pointwise in $\mathbb{F}$ (by the field axioms for $\mathbb{F}$), hence holds globally as functions. So $\mathbb{F}^S$ is a vector space.

> [!note]- Complete formal solution
> Let $S$ be a nonempty set and $\mathbb{F}^S$ the set of functions $S \to \mathbb{F}$, with operations $(f + g)(s) = f(s) + g(s)$ and $(\lambda f)(s) = \lambda f(s)$ for all $f, g \in \mathbb{F}^S$, $\lambda \in \mathbb{F}$, $s \in S$.
>
> Each of the eight vector-space axioms holds pointwise in $\mathbb{F}$, hence holds globally on $\mathbb{F}^S$. Specifically:
> - The zero function $0_S$ with $0_S(s) = 0$ for every $s$ is an additive identity: $(f + 0_S)(s) = f(s) + 0 = f(s)$, so $f + 0_S = f$.
> - The additive inverse of $f$ is $-f$ defined by $(-f)(s) = -f(s)$: $(f + (-f))(s) = f(s) - f(s) = 0$.
> - Commutativity and associativity of $+$, the multiplicative identity, associativity of scalar multiplication, and both distributive laws all hold pointwise by the field axioms for $\mathbb{F}$ and the pointwise definition of operations on $\mathbb{F}^S$.
>
> Hence $\mathbb{F}^S$ is a vector space over $\mathbb{F}$.
>
> *Special case:* $\mathbb{F}^n = \mathbb{F}^{\{1, \dots, n\}}$ by identifying $(x_1, \dots, x_n)$ with the function $i \mapsto x_i$. Similarly $\mathbb{F}^\infty = \mathbb{F}^\mathbb{N}$. So both fall under the general $\mathbb{F}^S$ construction. $\blacksquare$

---

# Key Takeaways

**Pointwise operations make function spaces into vector spaces "for free".** The reason $\mathbb{F}^S$ is automatically a vector space, for any set $S$, is that each axiom is *pointwise* — an equation that holds at each $s \in S$ separately. Since $\mathbb{F}$ is a field (hence satisfies all the axioms), the pointwise instance of each vector-space axiom is automatic, and the global axiom follows. This is the structural reason function spaces are *everywhere*: they cost nothing to construct, and every familiar function space (continuous, smooth, polynomial, $L^p$, etc.) is a subspace of some $\mathbb{F}^S$. The recipe "$\mathbb{F}^S$ = pointwise-operations-on-functions" is the prototype of a vast family of natural vector spaces.

**$\mathbb{F}^n$ and $\mathbb{F}^\infty$ are special cases of the function-space construction.** Identifying $\mathbb{F}^n$ with $\mathbb{F}^{\{1, \dots, n\}}$ — n-tuples as functions on a finite indexing set — reveals that the coordinate construction is a function-space construction in disguise. This makes the formal generalization from $\mathbb{F}^n$ to $\mathbb{F}^\infty$ to $\mathbb{F}^\mathbb{R}$ (real-valued functions on $\mathbb{R}$) a uniform structural pattern, not a sequence of unrelated examples. The same generalization carries the same proofs of the vector-space axioms, with $S$ replaced as appropriate. Recognizing the unifying pattern simplifies handling of all coordinate-like spaces.

**Subspaces of function spaces capture qualitative properties of functions.** The continuous, differentiable, integrable, polynomial, even, odd, periodic, bounded, $L^p$ functions are all subspaces of $\mathbb{F}^S$ for an appropriate $S$. The general framework of vector spaces packages these "spaces of nice functions" uniformly, and lets the abstract theory of linear maps apply to operators like differentiation, integration, and Fourier transform. This is the conceptual bridge from algebra to functional analysis: function spaces are vector spaces, and the operators of analysis are linear maps between them.
