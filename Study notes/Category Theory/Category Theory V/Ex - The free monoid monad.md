---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Free-Forgetful Adjunction"
  - "Thm - Every Adjunction Gives a Monad"
  - "Def - Monoid in a Monoidal Category"
tags: [category-theory, foundations]
---

# Problem Statement

Let $T : \mathbf{Set} \to \mathbf{Set}$ be the functor $T A = A^* = \coprod_{n \geq 0} A^n$, the set of finite **lists** (words) over $A$, including the empty list. On a function $f : A \to B$, $Tf$ applies $f$ entrywise. Define $\eta_A : A \to A^*$ by $\eta_A(a) = (a)$ (the one-letter list) and $\mu_A : (A^*)^* \to A^*$ by concatenation: a list of lists is flattened into a single list by concatenating its entries in order.

**(a)** Show $(T, \eta, \mu)$ is a [[Def - Monad and Comonad|monad]] on $\mathbf{Set}$.

**(b)** Identify the [[Def - Free-Forgetful Adjunction|free–forgetful adjunction]] inducing it, and confirm $\mu$ is the whiskered counit.

**(c)** Why is this called the "free monoid" monad? Relate its data to the [[Def - Monoid in a Monoidal Category|monoid]] axioms.

**Recall:**

![[Def - Monad and Comonad#The Definition]]

A [[Def - Monoid in a Monoidal Category|monoid]] is a set $M$ with an associative binary operation and a two-sided unit. The **free monoid** on a set $A$ is $A^*$ under concatenation, with unit the empty word; it is free in the sense that any function $A \to UM$ into (the underlying set of) a monoid $M$ extends uniquely to a monoid homomorphism $A^* \to M$. By [[Thm - Every Adjunction Gives a Monad]], the adjunction $F \dashv U$ between $\mathbf{Set}$ and $\mathbf{Mon}$ induces the monad $T = UF$.

---

# Convergent Strategy

**Problem class:** A "certify a monad and recognize its adjunction" problem, identical in shape to [[Ex - The power-set monad]] but with concatenation in place of union. Part (c) additionally asks for the conceptual link to monoids, previewing that the *algebras* of this monad are monoids.

**Assumption pattern:** "Lists, singleton, concatenation" is the signature of the free-monoid construction. The assumption to leverage is the universal property of the free monoid (legal operation 1): maps out of $A^*$ correspond to maps out of $A$, which is the adjunction.

**Theorem routing:** Part (a) is direct verification (operation 2). Part (b) routes through [[Thm - Every Adjunction Gives a Monad]] applied to the free–forgetful adjunction $\mathbf{Set}\rightleftarrows\mathbf{Mon}$. Part (c) routes forward to [[Def - Algebra for a Monad]]: the monad packages "one binary operation, associative, with unit," and its algebras are monoids.

**Key decision point:** The subtlety in (a) is keeping the two whiskerings of $\mu$ distinct: $T\mu$ flattens the *inner* lists of a list-of-lists-of-lists, $\mu T$ flattens the *outer* level. Concatenation's associativity is what makes them agree, and recognizing this as "associativity one level up" is the key insight.

---

# Legal Operations Used

1. **Operation 2 from the topic page (check the monad axioms via whiskering).** Part (a) verifies associativity and unit laws by flattening nested lists, watching $T\mu$ versus $\mu T$.

2. **Operation 1 from the topic page (read a monad off an adjunction).** Part (b) recognizes $T = UF$ for $\mathbf{Set}\rightleftarrows\mathbf{Mon}$ and applies [[Thm - Every Adjunction Gives a Monad]].

3. **Operation 3 from the topic page (build the structure map of an algebra).** Part (c) reads a $T$-algebra structure map $A^* \to A$ as "multiply out a formal word," reconstructing the monoid operation.

---

# Hints

> [!note]- Hint 1
> For (a), associativity acts on a list of lists of lists. Flattening "inner first then outer" must equal "outer first then inner" — both produce one long list of the bottom-level letters in their original left-to-right order.

> [!note]- Hint 2
> The unit laws: wrapping each *letter* of a word as a singleton word (apply $T\eta$) and then concatenating returns the word; wrapping the *whole* word as a one-element list-of-lists (apply $\eta T$) and concatenating also returns the word.

> [!note]- Hint 3
> For (b), the universal property of the free monoid *is* the adjunction: $\mathbf{Mon}(A^*, M) \cong \mathbf{Set}(A, UM)$. The counit $\varepsilon_M : (UM)^* \to M$ multiplies a word of elements of $M$ in $M$.

> [!note]- Hint 4
> For (c), a [[Def - Algebra for a Monad|$T$-algebra]] $a : A^* \to A$ must satisfy $a(\text{singleton } x) = x$ (unit law) and $a$ respects concatenation (associativity law). Setting $x \cdot y = a((x,y))$ and $1 = a(())$ gives an associative unital operation — a monoid.

---

# Solution

The plan: verify the monad axioms by flattening nested lists (Step 1–2); identify the free-monoid adjunction and match $\mu$ to the whiskered counit (Step 3); read the algebra structure map as a monoid operation (Step 4). The crux is that list-concatenation is associative, which is the monad associativity one dimension up.

**Step 1 (a): Associativity.** Flattening commutes with itself: $\mu \circ T\mu = \mu \circ \mu T$.

> [!note]- Derivation
> Let $W \in (A^{**})^* = T^3 A$ be a list $W = (\mathbf{w}_1, \dots, \mathbf{w}_k)$ whose entries $\mathbf{w}_i = (w_{i,1}, \dots, w_{i,n_i})$ are themselves lists of words $w_{i,j} \in A^*$.
>
> $\mu \circ T\mu$: apply $T\mu = \mu$ entrywise to flatten each $\mathbf{w}_i$ into the single word $w_{i,1}\frown\cdots\frown w_{i,n_i} \in A^*$, giving a list of $k$ words; then $\mu$ concatenates them: $w_{1,1}\frown\cdots\frown w_{1,n_1}\frown w_{2,1}\frown\cdots\frown w_{k,n_k}$.
>
> $\mu \circ \mu T$: apply $\mu_{TA} = \mu T$ to flatten the outer list $W$ into one long list of words $(w_{1,1}, \dots, w_{1,n_1}, w_{2,1}, \dots, w_{k,n_k}) \in A^{**}$; then $\mu$ concatenates those words into the same long word.
>
> Both produce the concatenation of all the bottom-level words in their original order. Equal, because concatenation is associative.

**Step 2 (a): Unit laws.** $\mu \circ T\eta = 1 = \mu \circ \eta T$.

> [!note]- Derivation
> Take a word $w = (a_1, \dots, a_n) \in A^*$.
>
> Left: $T\eta_A(w) = ((a_1), (a_2), \dots, (a_n))$, the list of singleton words; concatenating gives $(a_1, \dots, a_n) = w$.
>
> Right: $\eta_{TA}(w) = (w)$, the one-element list containing $w$; concatenating gives $w$.
>
> Both equal $w$.

**Step 3 (b): The free-monoid adjunction.**

> [!note]- Derivation
> Let $U : \mathbf{Mon} \to \mathbf{Set}$ forget the monoid structure and $F : \mathbf{Set} \to \mathbf{Mon}$ send $A$ to the free monoid $(A^*, \frown, ())$. Freeness is the natural bijection
> $$\mathbf{Mon}(A^*, M) \cong \mathbf{Set}(A, UM), \qquad \varphi \mapsto \varphi\circ\eta_A,$$
> with inverse extending a function $g : A \to UM$ to the homomorphism $(a_1,\dots,a_n) \mapsto g(a_1)\cdots g(a_n)$. So $F \dashv U$, and $UF(A) = A^* = TA$. The unit is $a \mapsto (a)$, the given $\eta$. The counit $\varepsilon_M : (UM)^* \to M$ sends a word of elements of $M$ to their product in $M$. Whiskering, $\mu = U\varepsilon F$ at $A$ is $\varepsilon_{A^*} : (A^*)^* \to A^*$, the product in the *free* monoid $A^*$ of a word of words — which is concatenation. So $\mu$ is the given multiplication, and by [[Thm - Every Adjunction Gives a Monad]] the triple is a monad.

**Step 4 (c): Algebras are monoids.**

> [!note]- Derivation
> A [[Def - Algebra for a Monad|$T$-algebra]] is $(A, a : A^* \to A)$ with $a\circ\eta_A = 1_A$ and $a\circ\mu_A = a\circ Ta$. Define $1 := a(())$ and $x \cdot y := a((x,y))$. The unit law forces $a((x)) = x$. The associativity law $a\circ\mu = a\circ Ta$, evaluated on the word $((x),(y),(z))$-style nestings, forces $a$ to respect concatenation: $a(w_1 \frown w_2) = a((a(w_1), a(w_2)))$, i.e. evaluating a concatenation equals evaluating the two pieces and combining. This makes $\cdot$ associative with unit $1$. So $(A, \cdot, 1)$ is a [[Def - Monoid in a Monoidal Category|monoid]], and conversely every monoid gives an algebra by $a(w) = $ "multiply out $w$." Hence $\mathbf{Set}^T \simeq \mathbf{Mon}$, which is why $T$ is the **free monoid** monad: its free algebras are free monoids and its algebras are monoids.

> [!note]- Complete formal solution
> **(a)** With $\eta_A(a) = (a)$ and $\mu_A$ = concatenation: associativity holds because for $W \in T^3A$ both $\mu\circ T\mu$ and $\mu\circ\mu T$ concatenate all bottom-level words in order (associativity of $\frown$); the unit laws hold because concatenating singletons of a word's letters, or concatenating the one-element list of the whole word, each returns the word. So $(T,\eta,\mu)$ is a monad.
>
> **(b)** $F : \mathbf{Set}\to\mathbf{Mon}$, $A\mapsto(A^*,\frown,())$, is left adjoint to the forgetful $U$, via $\mathbf{Mon}(A^*,M)\cong\mathbf{Set}(A,UM)$. Then $UF = T$, the unit is $a\mapsto(a)$, and the counit $\varepsilon_M$ multiplies a word in $M$; whiskering gives $\mu_A = \varepsilon_{A^*} = $ concatenation. By [[Thm - Every Adjunction Gives a Monad]], $T$ is the monad of this adjunction.
>
> **(c)** A $T$-algebra $a : A^*\to A$ defines $1 = a(())$, $x\cdot y = a((x,y))$; the unit and associativity laws make $(A,\cdot,1)$ a monoid, and this is an equivalence $\mathbf{Set}^T\simeq\mathbf{Mon}$. $\blacksquare$

---

# Key Takeaways

**Concatenation is the monoid multiplication one level up.** The single most transferable insight is that the monad's multiplication $\mu$ (concatenation of a list of lists) and the algebra structure map $a$ (multiply out a single list) are two faces of the same operation, sitting at different levels. The monad associativity $\mu\circ T\mu = \mu\circ\mu T$ is the associativity of concatenation; the algebra associativity $a\circ\mu = a\circ Ta$ is the associativity of the monoid operation. Recognizing this "associativity at two levels" pattern lets you predict, for any free-algebra monad, both that the monad axioms will hold (the free structure is associative) and what the algebras will be (the structure the free construction is free for).

**The universal property of a free object is an adjunction, full stop.** Whenever a construction is called "the free $X$ on a set," the phrase "maps out of the free object correspond to maps out of the set" is literally the adjunction isomorphism $\mathcal{D}(FA, M) \cong \mathbf{Set}(A, UM)$. This is the trigger to reach for [[Thm - Every Adjunction Gives a Monad]]: the free monoid, free group, free module, and free vector space all give monads this way, and the multiplication is always the counit "evaluate the free structure." Building this reflex means you almost never check monad axioms directly — you recognize the adjunction and let the theorem do the work.

**The name of a monad announces its algebras.** "Free monoid monad" is not just a label; it tells you that the Eilenberg–Moore category is $\mathbf{Mon}$. This is the general principle that the algebras for the "free $X$" monad are the $X$'s: free-group monad gives [[Def - Group|groups]] ([[Ex - Algebras for the free-group monad are groups]]), free-module monad gives modules, free-vector-space monad gives vector spaces ([[Ex - Algebras for the free-vector-space monad]]). When you identify a monad as the free version of some structure, you have simultaneously identified its category of algebras, which is usually the actual goal. The diagnostic for spaced practice: given a free-construction monad, immediately ask "free for *what* structure?" and that structure is $\mathcal{C}^T$.
