---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Krull's Height Theorem (Principal Ideal Theorem)"
  - "Def - Krull Dimension and Height"
  - "Def - Associated and Minimal Primes"
  - "Def - Noetherian Ring"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A$ be a Noetherian ring and $x \in A$ an element that is **not a zero divisor** (and not a unit). Prove that every minimal prime ideal $\mathfrak{p}$ of the principal ideal $(x)$ has height *exactly* $1$:
$$\operatorname{ht}\mathfrak{p} = 1 \qquad \text{for every minimal prime } \mathfrak{p} \text{ of } (x).$$

This is **Krull's principal ideal theorem** (ES4 Q8b). The two inequalities split as follows. The upper bound $\operatorname{ht}\mathfrak{p} \leq 1$ is the principal-ideal case of [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]] ($r = 1$). The lower bound $\operatorname{ht}\mathfrak{p} \geq 1$ is where the non-zero-divisor hypothesis enters: it forces $\mathfrak{p}$ to strictly contain some minimal prime of $A$, using the fact (ES2 Q10c) that *every element of a minimal prime is a zero divisor*. Geometrically the statement is that **a hypersurface $V(x)$ has pure codimension one**: cutting by one non-trivial equation drops dimension by exactly one, with no components hiding in higher codimension.

**Recall:**

The objects in play are height, minimal primes of an ideal, zero divisors, and Krull's height theorem.

![[Thm - Krull's Height Theorem (Principal Ideal Theorem)#Statement]]

A **minimal prime of an ideal $(x)$** is a [[Def - Associated and Minimal Primes|minimal element]] of $\{\mathfrak{p} \in \operatorname{Spec} A : x \in \mathfrak{p}\}$ — a prime containing $x$ with no smaller prime also containing $x$. A **minimal prime of $A$** is a minimal element of $\operatorname{Spec} A$ itself, equivalently a minimal prime of $(0)$; these have height $0$.

The [[Def - Krull Dimension and Height|height]] $\operatorname{ht}\mathfrak{p}$ is the length of the longest chain of primes ending at $\mathfrak{p}$.

The key input for the lower bound, *minimal primes consist of zero divisors* (ES2 Q10c): if $\mathfrak{q}$ is a minimal prime of a ring $A$, then every $a \in \mathfrak{q}$ is a zero divisor in $A$. Contrapositively, **a non-zero-divisor lies in no minimal prime of $A$**.

---

# Convergent Strategy

**Problem class.** This is a *pin-an-invariant-to-an-exact-value* problem of the squeeze type: prove $\operatorname{ht}\mathfrak{p} \leq 1$ and $\operatorname{ht}\mathfrak{p} \geq 1$ separately. It is the single most consequential special case of dimension theory — the **principal ideal theorem** — and the geometric statement "one equation drops dimension by exactly one" that underwrites all of intersection theory and the theory of divisors. The two halves have completely different characters: the upper bound is a direct citation of the height theorem, while the lower bound is a small but essential argument that *uses the non-zero-divisor hypothesis*, which is exactly the hypothesis that distinguishes "$\leq 1$" from "$= 1$."

**Assumption pattern.** Two hypotheses, each used once. "$A$ Noetherian" is the standing requirement of [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]], which delivers $\operatorname{ht}\mathfrak{p} \leq 1$ for any minimal prime of a $1$-generated ideal. "$x$ is a non-zero-divisor" is the recognisable trigger for the lower bound: it is precisely the condition that lets you invoke "minimal primes consist of zero divisors" (ES2 Q10c) to conclude that $x$ — hence $\mathfrak{p} \ni x$ — cannot be a minimal prime of $A$, so $\mathfrak{p}$ has a prime strictly below it and $\operatorname{ht}\mathfrak{p} \geq 1$. Drop the non-zero-divisor hypothesis and the conclusion genuinely fails: in $k[X,Y]/(XY)$ the element $X$ is a zero divisor and the minimal prime $(X)$ over $(X)$ has height $0$.

**Theorem routing.** The route is: (upper) apply Krull's height theorem with $r = 1$ to get $\operatorname{ht}\mathfrak{p} \leq 1$; (lower) observe $x$ is a non-zero-divisor, invoke ES2 Q10c to learn $x \notin \mathfrak{q}$ for every minimal prime $\mathfrak{q}$ of $A$, conclude that the prime $\mathfrak{p} \ni x$ is not minimal, so (by existence of minimal primes below any prime, ES3 Q11) there is $\mathfrak{q} \subsetneq \mathfrak{p}$ with $\mathfrak{q}$ a minimal prime of $A$, giving the chain $\mathfrak{q} \subsetneq \mathfrak{p}$ of length $1$ and $\operatorname{ht}\mathfrak{p} \geq 1$. Squeeze to $\operatorname{ht}\mathfrak{p} = 1$.

**Key decision point.** The non-obvious move is realising that the *lower* bound is the substantive one and that it is purchased entirely by the non-zero-divisor hypothesis via the lemma "every element of a minimal prime is a zero divisor." Beginners reach for the upper bound (Krull) and stop, mistaking "$\leq 1$" for the theorem; the genuine content of the *principal ideal* theorem — that the height is *exactly* $1$, i.e. the hypersurface is *pure* codimension one with no embedded high-codimension components — is the lower bound. Recognising that "non-zero-divisor" is the exact algebraic encoding of "the equation $x = 0$ does not vanish on any whole component of $\operatorname{Spec} A$" is the conceptual crux.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XII — Dimension Theory#Legal Operations|the topic page's Legal Operations]]:

1. **Bound height by the number of generators (Krull's height theorem).** A minimal prime of an $r$-generated ideal has height $\leq r$; here $r = 1$ gives $\operatorname{ht}\mathfrak{p} \leq 1$.

2. **Detect non-zero-divisors via minimal primes (ES2 Q10c).** Every element of a minimal prime of $A$ is a zero divisor; contrapositively a non-zero-divisor lies in no minimal prime.

3. **Find a minimal prime below any prime (ES3 Q11).** Every prime $\mathfrak{p}$ contains a minimal prime $\mathfrak{q}$ of $A$; if $\mathfrak{p}$ is not itself minimal, $\mathfrak{q} \subsetneq \mathfrak{p}$ strictly.

4. **Exhibit a chain to lower-bound height.** A strict chain $\mathfrak{q} \subsetneq \mathfrak{p}$ of primes below $\mathfrak{p}$ proves $\operatorname{ht}\mathfrak{p} \geq 1$.

5. **Squeeze two inequalities to an exact value.** Combining $\operatorname{ht}\mathfrak{p} \leq 1$ and $\operatorname{ht}\mathfrak{p} \geq 1$ forces $\operatorname{ht}\mathfrak{p} = 1$.

---

# Hints

> [!note]- Hint 1
> Split into $\operatorname{ht}\mathfrak{p} \leq 1$ and $\operatorname{ht}\mathfrak{p} \geq 1$. One of these is a one-word citation of a big theorem you already know. Which big theorem bounds the height of a minimal prime of an ideal by the number of generators?

> [!note]- Hint 2
> The upper bound is [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]] with $r = 1$: a minimal prime of the $1$-generated ideal $(x)$ has height $\leq 1$. No hypothesis on $x$ beyond "Noetherian" is needed for this half. The non-zero-divisor hypothesis must therefore be for the *other* inequality.

> [!note]- Hint 3
> For $\operatorname{ht}\mathfrak{p} \geq 1$ you must produce a prime strictly below $\mathfrak{p}$. The candidate is a minimal prime $\mathfrak{q}$ of $A$ (height $0$). You need $\mathfrak{q} \subsetneq \mathfrak{p}$ *strictly*, i.e. $\mathfrak{p}$ is not itself a minimal prime of $A$. Why is $\mathfrak{p}$ not minimal? Because $x \in \mathfrak{p}$ and $x$ is a non-zero-divisor — recall what ES2 Q10c says about the elements of a minimal prime.

> [!note]- Hint 4
> ES2 Q10c: every element of a minimal prime of $A$ is a zero divisor. Since $x$ is a non-zero-divisor, $x$ lies in *no* minimal prime of $A$, so $\mathfrak{p}$ (which contains $x$) is not minimal. By ES3 Q11, $\mathfrak{p}$ contains some minimal prime $\mathfrak{q}$ of $A$, necessarily $\mathfrak{q} \subsetneq \mathfrak{p}$. That chain has length $1$, so $\operatorname{ht}\mathfrak{p} \geq 1$. Combine with Hint 2.

---

# Solution

The proof is a squeeze whose two halves use the two hypotheses separately. The upper bound $\operatorname{ht}\mathfrak{p} \leq 1$ is the principal-ideal case of Krull's height theorem and uses only Noetherianity. The lower bound $\operatorname{ht}\mathfrak{p} \geq 1$ is the heart of the *principal ideal* statement: the non-zero-divisor hypothesis, via "minimal primes consist of zero divisors," forces $\mathfrak{p}$ to sit strictly above a minimal prime, producing a chain of length one.

**Step 1: $\operatorname{ht}\mathfrak{p} \leq 1$ by Krull's height theorem.**

Since $\mathfrak{p}$ is a minimal prime of the ideal $(x)$ generated by one element, the height theorem gives $\operatorname{ht}\mathfrak{p} \leq 1$.

> [!note]- Derivation
> The ideal $(x)$ is generated by $r = 1$ element. By [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]], every minimal prime $\mathfrak{p}$ of an $r$-generated ideal in a Noetherian ring satisfies $\operatorname{ht}\mathfrak{p} \leq r$. With $r = 1$,
> $$\operatorname{ht}\mathfrak{p} \leq 1.$$
> This half needs nothing about $x$ except that $(x)$ is one-generated and $A$ is Noetherian. (Recall the one-line mechanism behind it: localizing at $\mathfrak{p}$ makes $(x)A_\mathfrak{p}$ primary to the maximal ideal by minimality, and the dimension theorem bounds $\dim A_\mathfrak{p} = \operatorname{ht}\mathfrak{p}$ by the number of generators, here $1$.)

**Step 2: $x$ lies in no minimal prime of $A$.**

Because $x$ is a non-zero-divisor and every element of a minimal prime is a zero divisor, $x$ avoids all minimal primes of $A$.

> [!note]- Derivation
> By **ES2 Q10c**, if $\mathfrak{q}$ is a minimal prime of $A$ then every element of $\mathfrak{q}$ is a zero divisor in $A$. (Sketch: localize at $\mathfrak{q}$; the local ring $A_\mathfrak{q}$ has a unique prime $\mathfrak{q}A_\mathfrak{q}$, which is therefore its nilradical, so every element of $\mathfrak{q}A_\mathfrak{q}$ is nilpotent; clearing denominators, each $a \in \mathfrak{q}$ satisfies $s a^m = 0$ for some $s \notin \mathfrak{q}$ and $m \geq 1$, making $a$ a zero divisor.)
>
> Contrapositively, a non-zero-divisor lies in no minimal prime. Our $x$ is a non-zero-divisor, so
> $$x \notin \mathfrak{q} \quad \text{for every minimal prime } \mathfrak{q} \text{ of } A.$$

**Step 3: $\mathfrak{p}$ is not a minimal prime of $A$, hence $\operatorname{ht}\mathfrak{p} \geq 1$.**

Since $x \in \mathfrak{p}$ but $x$ is in no minimal prime, $\mathfrak{p}$ is not minimal; a minimal prime $\mathfrak{q} \subsetneq \mathfrak{p}$ then gives a chain of length $1$.

> [!note]- Derivation
> We have $x \in \mathfrak{p}$ (as $\mathfrak{p}$ contains $(x)$). By Step 2, $x$ lies in no minimal prime of $A$. Therefore $\mathfrak{p}$ is *not* a minimal prime of $A$ — if it were, it would contain the non-zero-divisor $x$, contradicting Step 2.
>
> By **ES3 Q11**, every prime ideal contains a minimal prime of $A$: there is a minimal prime $\mathfrak{q}$ of $A$ with $\mathfrak{q} \subseteq \mathfrak{p}$. Since $\mathfrak{p}$ is not minimal, the inclusion is strict, $\mathfrak{q} \subsetneq \mathfrak{p}$. This is a chain of primes
> $$\mathfrak{q} \subsetneq \mathfrak{p}$$
> of length $1$, so by the definition of [[Def - Krull Dimension and Height|height]],
> $$\operatorname{ht}\mathfrak{p} \geq 1.$$

**Step 4: Conclude $\operatorname{ht}\mathfrak{p} = 1$.**

The bounds from Steps 1 and 3 force equality.

> [!note]- Derivation
> From Step 1, $\operatorname{ht}\mathfrak{p} \leq 1$; from Step 3, $\operatorname{ht}\mathfrak{p} \geq 1$. Hence
> $$\operatorname{ht}\mathfrak{p} = 1. \qquad \blacksquare$$
> Geometrically: the hypersurface $V(x) \subseteq \operatorname{Spec} A$ has every irreducible component (= every minimal prime of $(x)$) of codimension exactly one. One non-trivial equation cuts dimension by exactly one.

> [!note]- Complete formal solution
> **Claim (Krull's principal ideal theorem).** Let $A$ be Noetherian and $x \in A$ a non-zero-divisor and non-unit. Then every minimal prime $\mathfrak{p}$ of $(x)$ has $\operatorname{ht}\mathfrak{p} = 1$.
>
> *Upper bound.* $(x)$ is generated by one element, so by Krull's height theorem every minimal prime $\mathfrak{p}$ of $(x)$ has $\operatorname{ht}\mathfrak{p} \leq 1$.
>
> *Lower bound.* Every element of a minimal prime of $A$ is a zero divisor (ES2 Q10c), so the non-zero-divisor $x$ lies in no minimal prime of $A$. As $x \in \mathfrak{p}$, the prime $\mathfrak{p}$ is not minimal. By ES3 Q11 there is a minimal prime $\mathfrak{q} \subseteq \mathfrak{p}$, and minimality of $\mathfrak{q}$ together with non-minimality of $\mathfrak{p}$ forces $\mathfrak{q} \subsetneq \mathfrak{p}$. Thus $\operatorname{ht}\mathfrak{p} \geq 1$.
>
> Combining, $\operatorname{ht}\mathfrak{p} = 1$. $\blacksquare$
>
> *Remark (why the hypothesis is needed).* In $A = k[X,Y]/(XY)$, the element $X$ is a zero divisor ($X \cdot Y = 0$) and $(X)$ is itself a minimal prime over $(X)$ of height $0$ — the component $\{X = 0\}$ is a whole irreducible component of $\operatorname{Spec} A$, not a proper subvariety. So without "non-zero-divisor," the conclusion $\operatorname{ht} = 1$ fails.

---

# Key Takeaways

**The principal ideal theorem is "$= 1$," and the lower bound — not the celebrated upper bound — is where the content lives.** It is a near-universal beginner's error to equate Krull's *height theorem* ($\operatorname{ht} \leq r$) with Krull's *principal ideal theorem* ($\operatorname{ht} = 1$). The height theorem is the upper bound and uses only Noetherianity; it says a hypersurface has codimension *at most* one. But the geometric punch of the principal ideal theorem is that the codimension is *exactly* one — that $V(x)$ is **pure** of codimension one, with no embedded components buried deeper. That exactness is the lower bound, and it is bought entirely by the non-zero-divisor hypothesis. The lesson for spaced practice: whenever a result asserts an *exact* height or dimension, expect two arguments of different flavours, and ask which hypothesis supplies the *lower* bound — it is usually a "this element is not a zero divisor / not in any minimal prime" condition, the algebraic way of saying "the equation does not vanish identically on any whole component."

**"Non-zero-divisor" is the algebraic name for "does not vanish on a whole component," via the lemma that minimal primes consist of zero divisors.** The single most reusable idea here is the dictionary entry: $x$ is a non-zero-divisor $\iff$ $x$ lies in no minimal prime of $A$ $\iff$ the hypersurface $V(x)$ contains no irreducible component of $\operatorname{Spec} A$. The bridge is ES2 Q10c — every element of a minimal prime is a zero divisor — whose proof is itself instructive: at a minimal prime the local ring has a single prime, so that prime is the nilradical, so its elements are nilpotent, so globally they are zero divisors. Carrying this equivalence in working memory turns many height computations into one-liners: to show a prime over $(x)$ has positive height, you do not chase chains, you observe that $x$, being a non-zero-divisor, escapes every minimal prime and so its containing prime cannot be minimal.

**This is the algebraic seed of divisor theory: codimension-one cycles come from single equations.** The statement that $(x)$ has pure codimension one is the foundation of the entire theory of **bold plain text — Weil divisors and the divisor class group**. The height-one primes of $A$ are the **bold plain text — prime divisors**, the codimension-one irreducible subvarieties; the free abelian group they generate is the group of Weil divisors, and a non-zero-divisor $x$ produces the **bold plain text — principal divisor** $\operatorname{div}(x) = \sum_{\operatorname{ht}\mathfrak{p}=1} v_\mathfrak{p}(x)\,[\mathfrak{p}]$, a sum over exactly the height-one primes, well-defined precisely *because* the principal ideal theorem guarantees those are the only primes that appear. In a Noetherian UFD this closes a loop with [[Thm - Principal Ideal Domains are Unique Factorization Domains|unique factorization]]: a height-one prime contains an irreducible $p$, and $(p) \subseteq \mathfrak{p}$ with $(p)$ prime of height one forces $(p) = \mathfrak{p}$, so every height-one prime is principal — the divisor class group is trivial. The exercise is thus the gateway from "one equation" to the whole apparatus of divisors and line bundles.

**Each strict inclusion of primes is one equation, and this is the smallest non-trivial instance of "an equation drops dimension by one."** Internalize the picture: in $\operatorname{Spec} A$, passing from a minimal prime $\mathfrak{q}$ (a whole component, codimension $0$) up to a minimal prime $\mathfrak{p}$ of $(x)$ (codimension $1$) is exactly the act of imposing the single condition $x = 0$, and the height jump is exactly $1$. This is the base case of the inductive philosophy that runs through all of dimension theory — $r$ equations drop dimension by at most $r$ (height theorem), and by *exactly* $r$ when they form a **bold plain text — regular sequence** (the complete-intersection case). When you reconstruct this proof later, the mnemonic is: "Krull gives $\leq 1$; non-zero-divisor gives $\geq 1$; together $= 1$ — one honest equation, one step of codimension." The same two-hypothesis structure recurs verbatim in [[Ex - Height plus dimension of the quotient equals dimension]] and in the dimension-of-intersection bounds of [[Ex - The dimension of a polynomial ring is n|the polynomial-ring computation]].
