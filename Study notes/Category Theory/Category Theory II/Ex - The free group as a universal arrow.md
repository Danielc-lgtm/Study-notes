---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Universal Property and Universal Arrow"
  - "Def - Free Group and Free Product"
  - "Def - Initial and Terminal Object"
  - "Def - Group"
tags: [category-theory, foundations]
---

# Problem Statement

Let $U : \mathbf{Grp} \to \mathbf{Set}$ be the forgetful functor and $S$ a set. Let $F(S)$ be the [[Def - Free Group and Free Product|free group]] on $S$, with the inclusion of generators $\eta_S : S \to U F(S)$.

1. Show that $(F(S), \eta_S)$ is a **universal arrow from $S$ to $U$**: for every group $H$ and every function $f : S \to U(H)$, there is a unique homomorphism $\bar f : F(S) \to H$ with $U(\bar f) \circ \eta_S = f$.
2. Reinterpret this as the statement that $(F(S), \eta_S)$ is an **initial object** in the comma category $(S \downarrow U)$, and use [[Thm - Uniqueness of Universal Objects]] to conclude the free group is unique up to unique isomorphism.

**Recall:**

![[Def - Universal Property and Universal Arrow#The Definition]]

The [[Def - Free Group and Free Product|free group]] $F(S)$ is the group of reduced words in the symbols $\{s, s^{-1} : s \in S\}$, with concatenation-then-reduction as multiplication; $\eta_S(s) = s$ is the length-one word. A homomorphism out of $F(S)$ is determined by its values on the generators (see [[Def - Group]]).

---

# Convergent Strategy

**Problem class:** This is the canonical "verify a universal property" exercise: given a candidate object and structure map, prove existence and uniqueness of the factorization. As the topic page's strategy notes, every such proof is the same four-beat — exhibit the structure map, take an arbitrary competitor, build the factorization, prove it is forced.

**Assumption pattern:** The decisive assumption is that elements of $F(S)$ are *words in the generators*: every element is a finite product $s_1^{\pm 1} \cdots s_n^{\pm 1}$. This is what lets a homomorphism out of $F(S)$ be *forced* by its values on $S$ — there is no freedom once the generators' images are chosen, because the homomorphism property propagates the choice to every word.

**Theorem routing:** The route is: define $\bar f$ on generators by $\bar f(s) = f(s)$, extend to words by the homomorphism law, check well-definedness (independence of word representative) and uniqueness, then translate into the language of [[Def - Universal Property and Universal Arrow|universal arrows]] and invoke [[Thm - Uniqueness of Universal Objects]] for the uniqueness corollary.

**Key decision point:** The non-obvious step is *well-definedness*: a group element has many word representatives (e.g. $ss^{-1}s = s$), so the rule "send the word $s_1 \cdots s_n$ to $f(s_1) \cdots f(s_n)$" must be checked to give the same answer on equivalent words. This is exactly where the freeness of $F(S)$ — no relations beyond the group axioms — is used: the only identifications among words are the forced ones, which any homomorphism respects.

---

# Legal Operations Used

1. **Operation 2 from the topic page (read off a morphism from generators).** We define $\bar f$ by its values on the generating set $S$ and extend by the homomorphism law; this is the standard way to specify a map out of a free object.

2. **Operation 5 from the topic page (recognize a universal property as initiality in a comma category).** Part 2 reframes the universal arrow as an initial object of $(S \downarrow U)$, enabling the uniqueness corollary.

---

# Hints

> [!note]- Hint 1
> A homomorphism out of $F(S)$ is determined by what it does to the generators. Use this to *define* the candidate factorization.

> [!note]- Hint 2
> Define $\bar f(s_1^{\epsilon_1} \cdots s_n^{\epsilon_n}) = f(s_1)^{\epsilon_1} \cdots f(s_n)^{\epsilon_n}$. The work is checking this respects the equivalence of words (reduction) so that it is well-defined.

> [!note]- Hint 3
> For uniqueness: any homomorphism $g$ with $g \circ \eta_S = f$ agrees with $\bar f$ on generators, hence on all words, hence everywhere.

> [!note]- Hint 4
> For part 2: the comma category $(S \downarrow U)$ has objects $(H, f : S \to U(H))$ and morphisms $(H, f) \to (H', f')$ given by homomorphisms $k : H \to H'$ with $U(k) \circ f = f'$. "Universal arrow" = "initial object".

---

# Solution

The proof exhibits $\bar f$ by its action on generators, extends it multiplicatively, verifies well-definedness from freeness and uniqueness from generation, and then repackages the result as initiality so that uniqueness of the free group is automatic.

**Step 1: Define the factorization on generators and extend.**

> [!note]- Derivation
> Given $f : S \to U(H)$, define $\bar f : F(S) \to H$ on a reduced word by
> $$\bar f(s_1^{\epsilon_1} s_2^{\epsilon_2} \cdots s_n^{\epsilon_n}) = f(s_1)^{\epsilon_1} f(s_2)^{\epsilon_2} \cdots f(s_n)^{\epsilon_n}, \qquad \epsilon_i \in \{+1, -1\},$$
> and $\bar f(\text{empty word}) = e_H$. By construction $\bar f(\eta_S(s)) = \bar f(s) = f(s)$, so $U(\bar f) \circ \eta_S = f$.

**Step 2: $\bar f$ is a well-defined homomorphism.**

> [!note]- Derivation
> Two words represent the same element of $F(S)$ exactly when one is obtained from the other by inserting or deleting adjacent cancelling pairs $s s^{-1}$ or $s^{-1} s$ (the only relations in a [[Def - Free Group and Free Product|free group]]). Under $\bar f$, such a pair maps to $f(s) f(s)^{-1} = e_H$ (or $f(s)^{-1} f(s) = e_H$), which can be inserted or deleted in $H$ without changing the product. So $\bar f$ assigns the same element of $H$ to all word representatives of a given group element — it is well-defined. It is a homomorphism because concatenating words multiplies their images: $\bar f(w w') = \bar f(w)\bar f(w')$, the products matching term-by-term before reduction, and reduction not changing the value by the argument just given.

**Step 3: Uniqueness of the factorization.**

> [!note]- Derivation
> Suppose $g : F(S) \to H$ is any homomorphism with $U(g) \circ \eta_S = f$, i.e. $g(s) = f(s)$ for all $s \in S$. For any reduced word, the homomorphism law forces
> $$g(s_1^{\epsilon_1} \cdots s_n^{\epsilon_n}) = g(s_1)^{\epsilon_1} \cdots g(s_n)^{\epsilon_n} = f(s_1)^{\epsilon_1} \cdots f(s_n)^{\epsilon_n} = \bar f(s_1^{\epsilon_1} \cdots s_n^{\epsilon_n}).$$
> So $g = \bar f$ on every word, hence $g = \bar f$. The factorization is unique.

**Step 4: Initiality in the comma category and uniqueness of $F(S)$.**

> [!note]- Derivation
> Form the comma category $(S \downarrow U)$: objects are pairs $(H, f)$ with $f : S \to U(H)$, and a morphism $(H, f) \to (H', f')$ is a homomorphism $k : H \to H'$ with $U(k) \circ f = f'$. Steps 1–3 say: for every object $(H, f)$ there is a *unique* morphism $(F(S), \eta_S) \to (H, f)$ in $(S \downarrow U)$, namely $\bar f$. That is exactly the statement that $(F(S), \eta_S)$ is an [[Def - Initial and Terminal Object|initial object]] of $(S \downarrow U)$ — equivalently a [[Def - Universal Property and Universal Arrow|universal arrow]] from $S$ to $U$. By [[Thm - Uniqueness of Universal Objects]], any two free groups on $S$ are connected by a unique isomorphism compatible with their insertions of generators, justifying "*the* free group on $S$".

> [!note]- Complete formal solution
> Given $f : S \to U(H)$, define $\bar f : F(S) \to H$ by $\bar f(s_1^{\epsilon_1} \cdots s_n^{\epsilon_n}) = f(s_1)^{\epsilon_1} \cdots f(s_n)^{\epsilon_n}$ and $\bar f(\text{empty}) = e_H$; then $U(\bar f)\eta_S = f$. It is well-defined because the only word identifications in $F(S)$ are cancellations $s s^{-1} \leftrightarrow \text{empty}$, which map to $f(s)f(s)^{-1} = e_H$; it is a homomorphism because concatenation multiplies images. If $g$ is another homomorphism with $g\eta_S = f$, then $g$ agrees with $\bar f$ on generators, and the homomorphism law forces agreement on all words, so $g = \bar f$. Thus $(F(S), \eta_S)$ is a universal arrow from $S$ to $U$, i.e. an initial object of $(S \downarrow U)$; by [[Thm - Uniqueness of Universal Objects]], the free group is unique up to unique compatible isomorphism. $\blacksquare$

---

# Key Takeaways

**A map out of a free object is "define on generators, extend by the law" — and the only real work is well-definedness.** This exercise is the prototype for every free-construction universal property: free monoids, [[Def - Free Module|free modules]], polynomial rings, tensor algebras. The construction of the factorization is always trivial (declare the values on generators, propagate by the structure-preserving law), and the entire mathematical content is the well-definedness check — that the propagation respects whatever identifications the free object imposes. For a free group those identifications are just cancellations, and freeness means there are no others, which is precisely why the extension exists. When you meet a new free construction, the trigger is "elements are words/combinations of generators", and the reaction is to define on generators and verify the relations map to identities.

**Uniqueness of the factorization comes from generation, not from any cleverness.** Once $g$ and $\bar f$ agree on the generators, they agree everywhere, because the generators *generate* — every element is a product of them, and a homomorphism is determined by its values on a generating set. This is a completely general principle: a homomorphism out of any object is determined by its restriction to a generating subobject. Recognizing it saves you from ever proving uniqueness by a separate argument; it is automatic the moment the structure map hits a generating set.

**Reframing a universal property as initiality turns "unique up to isomorphism" into a one-line corollary.** The payoff of part 2 is methodological: rather than prove directly that two free groups are isomorphic, recognize the free group as an [[Def - Initial and Terminal Object|initial object]] of a comma category and invoke [[Thm - Uniqueness of Universal Objects]]. This is the right habit for *every* universal construction — the moment you have verified the universal property, you have an initial or terminal object, and its uniqueness up to unique isomorphism is free. The same move justifies "the tensor product" ([[Thm - Universal Property of the Tensor Product]]), "the quotient" ([[Thm - Universal Property of the Quotient]]), and "the product".
