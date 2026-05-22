---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Basis"
  - "Def - Linear Independence"
  - "Def - Linear Combination and Span"
tags: [algebra, linear-algebra]
---

# Problem Statement

Prove that $1, z, z^2, \ldots, z^n$ is a basis of $\mathcal{P}_n(F)$, the vector space of polynomials over $F$ of degree at most $n$.

(Here $F$ is a field with infinitely many elements — in our standing convention $F = \mathbb{R}$ or $\mathbb{C}$. The result holds for any infinite field; for finite fields the statement is the same but the proof of linear independence requires more care because polynomial equality as a function is not the same as polynomial equality as a formal expression.)

**Recall.**

![[Def - Basis#The Definition]]

The space $\mathcal{P}_n(F)$ consists of all functions $p : F \to F$ of the form
$$p(z) = a_0 + a_1 z + a_2 z^2 + \cdots + a_m z^m$$
for some $a_0, \ldots, a_m \in F$ with $m \leq n$. Two polynomials are equal as elements of $\mathcal{P}_n(F)$ if and only if they are equal as functions $F \to F$ — i.e. give the same value at every $z \in F$.

A list is a basis of $V$ if it is linearly independent and spans $V$ (LADR Def 2.26).

---

# Convergent Strategy

**Problem class:** This is a *canonical basis* problem — verifying that a concretely given list, here the powers $1, z, \ldots, z^n$, satisfies both basis conditions in an explicitly described space. The point is to internalise the standard basis of polynomial spaces; the technique generalises (different powers, different shifts $(x - c)^k$, Bernstein polynomials, Legendre polynomials, etc.). Almost every later basis of a polynomial space is proven a basis by reduction to this one.

**Assumption pattern:** The two ingredients are (a) the definition of $\mathcal{P}_n(F)$ as polynomials of degree at most $n$, which immediately makes the powers $1, z, \ldots, z^n$ a *spanning* list by definition (every polynomial of degree at most $n$ is by construction a linear combination of $1, z, \ldots, z^n$); and (b) the fact (assumed here and proved in chapter 4) that a polynomial that vanishes at every $z \in F$ (with $F$ infinite) must be the zero polynomial — equivalently, the coefficients of a polynomial are uniquely determined by the function it computes. (For $F = \mathbb{R}$ or $\mathbb{C}$ this is immediate: a nonzero polynomial of degree $m$ has at most $m$ roots.)

**Theorem routing:** Spanning is immediate from the definition. Independence requires the polynomial-uniqueness fact above: if $a_0 + a_1 z + \cdots + a_n z^n = 0$ as a function on $F$ (i.e. for every $z \in F$), then all $a_i = 0$. This is the precise statement that licenses the move from "polynomial vanishes everywhere" to "all coefficients are zero". The fact is itself a theorem (LADR 4.8), but it is intuitive enough that we will use it here without re-proving — the entire proof of independence reduces to it.

**Key decision point:** The crucial recognition is that *linear independence of polynomials* is equivalent to *uniqueness of coefficients of a polynomial as a function*. This is not obvious at the outset: a polynomial *expression* $a_0 + a_1 z + \cdots + a_n z^n$ has its coefficients on its sleeve, but as a *function* the coefficients are recovered by some procedure (e.g. successive differentiation at 0, or evaluation at $n + 1$ points). The fact that this recovery is well-defined — that two expressions with different coefficients give different functions — is what makes linear independence work.

---

# Legal Operations Used

1. **Test polynomial linear independence by reading off leading coefficient (operation 9).** A combination $\sum a_i z^i = 0$ that has nonzero degree-$k$ coefficient gives a polynomial of degree $k$ as a function, with $k \leq n$ leading coefficient $a_k \neq 0$. But the zero polynomial has degree $-\infty$, not $k$, so $a_k = 0$ — contradiction. Iterating downwards in degree, all coefficients must vanish.

2. **Verify spanning from the definition of the space (implicit).** The space $\mathcal{P}_n(F)$ is *defined* as polynomials of degree at most $n$, which are by definition the linear combinations of $1, z, z^2, \ldots, z^n$. So spanning is essentially tautological.

---

# Hints

> [!note]- Hint 1
> The two basis conditions must be verified. Spanning should follow immediately from the definition of $\mathcal{P}_n(F)$. The work is in independence.

> [!note]- Hint 2
> For independence: suppose $a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n = 0$ for *all* $z \in F$. What does this say about the coefficients $a_i$?

> [!note]- Hint 3
> Use the fact that a nonzero polynomial of degree at most $n$ has at most $n$ roots. If the polynomial vanishes at every $z \in F$ and $F$ is infinite, the polynomial has infinitely many roots, so it cannot be nonzero — it must be the zero polynomial, with all coefficients zero.

---

# Solution

**Plan.** I will verify each of the two basis conditions. Spanning is immediate from the definition of $\mathcal{P}_n(F)$. Independence requires the standard fact (LADR 4.8) that a nonzero polynomial of degree at most $n$ has at most $n$ roots, so a polynomial vanishing on the infinite field $F$ must be the zero polynomial.

**Step 1: The list $1, z, \ldots, z^n$ spans $\mathcal{P}_n(F)$.**

> [!note]- Derivation
> A polynomial $p \in \mathcal{P}_n(F)$ is, by definition, a function $p : F \to F$ given by an expression $p(z) = a_0 + a_1 z + a_2 z^2 + \cdots + a_m z^m$ for some $a_0, \ldots, a_m \in F$ with $m \leq n$. We may always append zero coefficients to make the expression have exactly $n + 1$ terms: $p(z) = a_0 + a_1 z + \cdots + a_n z^n$, with $a_{m+1} = \cdots = a_n = 0$.
>
> So $p = a_0 \cdot 1 + a_1 \cdot z + a_2 \cdot z^2 + \cdots + a_n \cdot z^n$ is a linear combination of $1, z, z^2, \ldots, z^n$. Hence the list spans $\mathcal{P}_n(F)$.

**Step 2: The list $1, z, \ldots, z^n$ is linearly independent.**

> [!note]- Derivation
> Suppose $a_0, a_1, \ldots, a_n \in F$ and
> $$a_0 \cdot 1 + a_1 \cdot z + a_2 \cdot z^2 + \cdots + a_n \cdot z^n = 0$$
> as an element of $\mathcal{P}_n(F)$ — that is, as a function $F \to F$. So for every $z \in F$,
> $$a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n = 0.$$
> Consider the polynomial (over $F$) $q(z) = a_0 + a_1 z + \cdots + a_n z^n$. It vanishes at every $z \in F$. If $q$ were nonzero, it would have degree $d \leq n$ (where $d$ is the largest index with $a_d \neq 0$), and a nonzero polynomial of degree $d$ has at most $d$ roots. But $q$ has every $z \in F$ as a root, and $F$ is infinite. So $q$ must be the zero polynomial, meaning $a_0 = a_1 = \cdots = a_n = 0$.
>
> Hence the only solution of the vanishing equation is the trivial one, so the list is linearly independent.

**Step 3: Combining.**

> [!note]- Derivation
> By Step 1 the list spans $\mathcal{P}_n(F)$. By Step 2 the list is linearly independent. By the definition of basis, the list $1, z, z^2, \ldots, z^n$ is a basis of $\mathcal{P}_n(F)$.
>
> Counting: the list has length $n + 1$, so $\dim \mathcal{P}_n(F) = n + 1$. (Note the off-by-one: degree at most $n$ gives $n + 1$ basis vectors.)

> [!note]- Sanity check by direct coefficient comparison
> The proof above uses the "polynomial with infinitely many roots is zero" fact. Alternatively, one can argue by evaluating successive derivatives at $0$: from $\sum a_i z^i = 0$ identically, evaluating at $z = 0$ gives $a_0 = 0$; differentiating and evaluating at $0$ gives $a_1 = 0$; differentiating $k$ times and evaluating at $0$ gives $k! a_k = 0$, hence $a_k = 0$ (over a field where $k! \neq 0$, true for $F$ of characteristic $0$ or large enough characteristic). This route gives the same conclusion via a different bridge.

> [!note]- Complete formal solution
> We show that $1, z, z^2, \ldots, z^n$ is a [[Def - Basis|basis]] of $\mathcal{P}_n(F)$, where $F$ is an infinite field.
>
> *Spanning.* Every polynomial $p \in \mathcal{P}_n(F)$ has, by definition, an expression $p(z) = \sum_{i=0}^m a_i z^i$ for some coefficients $a_i \in F$ and some $m \leq n$. Padding with zero coefficients if necessary, we write $p(z) = \sum_{i=0}^n a_i z^i$ with $a_{m+1} = \cdots = a_n = 0$. This expresses $p$ as a linear combination of $1, z, \ldots, z^n$, so the list spans $\mathcal{P}_n(F)$.
>
> *Independence.* Suppose $\sum_{i=0}^n a_i z^i = 0$ in $\mathcal{P}_n(F)$ — meaning, as a function $F \to F$, $\sum_{i=0}^n a_i z^i = 0$ for every $z \in F$. The polynomial $q(z) = \sum_{i=0}^n a_i z^i$ has every element of $F$ as a root. Since $F$ is infinite and a nonzero polynomial of degree $\leq n$ over a field has at most $n$ roots (LADR 4.8 / fundamental fact of polynomial algebra), $q$ must be the zero polynomial, i.e. all $a_i = 0$.
>
> So the only vanishing combination is the trivial one, and the list is linearly independent.
>
> Hence $1, z, z^2, \ldots, z^n$ is a basis of $\mathcal{P}_n(F)$, and $\dim \mathcal{P}_n(F) = n + 1$. $\qquad\blacksquare$

---

# Key Takeaways

**Polynomial linear independence is "coefficients are uniquely determined".** The exercise turns on the fact that two polynomial expressions giving the same function on an infinite field must have the same coefficients. This is *the* polynomial-ring fact that makes linear-algebraic arguments about polynomial spaces work. The list $1, z, \ldots, z^n$ is linearly independent precisely because no two distinct polynomials of degree $\leq n$ give the same function — i.e. the coefficient map is injective. Whenever you need to prove a list of polynomials linearly independent, the fundamental tool is: write out a vanishing combination, treat it as a polynomial in $z$, and read off coefficients (either by polynomial-degree arguments, by evaluating at well-chosen points, or by repeated differentiation).

**The off-by-one: degree at most $n$, basis of length $n + 1$.** This is the most common point of confusion in polynomial-space dimension. $\mathcal{P}_n(F)$ — degree at most $n$ — has basis $1, z, z^2, \ldots, z^n$ of length $n + 1$, so $\dim \mathcal{P}_n(F) = n + 1$. The list includes the constant polynomial $1 = z^0$ as the first entry. Always count basis vectors, not maximum exponent.

**This basis is one of infinitely many.** The basis $1, z, \ldots, z^n$ is the *standard* basis, but many others exist. The shifted basis $1, (z - c), (z - c)^2, \ldots, (z - c)^n$ for any $c \in F$ is also a basis (the change-of-basis matrix being the triangular shift matrix). The Lagrange basis $\{\prod_{j \neq i} (z - z_j) / (z_i - z_j)\}_{i=0}^n$, for distinct $z_0, \ldots, z_n \in F$, is also a basis — and is the basis for *interpolation* (the coordinate of a polynomial in this basis is its value at $z_i$). Different bases are chosen for different problems: the standard basis is for symbolic manipulation, shifted bases for problems with a privileged point, Lagrange basis for interpolation, orthogonal-polynomial bases for inner-product-space problems.

**Trigger-reaction: see a polynomial space → reach for the standard basis.** When you encounter a polynomial space in a problem, the standard basis is the first thing to put on the table. Its existence makes computation immediate: every polynomial has a vector of coefficients in $F^{n+1}$, and operations on polynomials (addition, scalar multiplication, sometimes multiplication) become linear-algebra operations on these vectors. The standard basis is the bridge from "polynomial space" to "$F^{n+1}$".
