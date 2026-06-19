---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Adjunction"
  - "Thm - Every Adjunction Gives a Monad"
tags: [category-theory, foundations]
---

# Problem Statement

Let $P : \mathbf{Set} \to \mathbf{Set}$ be the covariant power-set functor: $P(A)$ is the set of all subsets of $A$, and for $f : A \to B$, $P(f) : P(A) \to P(B)$ takes direct images, $P(f)(S) = f(S) = \{f(s) : s \in S\}$. Define $\eta_A : A \to P(A)$ by $\eta_A(a) = \{a\}$ (the singleton) and $\mu_A : P(P(A)) \to P(A)$ by $\mu_A(\mathcal{S}) = \bigcup_{S \in \mathcal{S}} S$ (the union).

**(a)** Show that $(P, \eta, \mu)$ is a [[Def - Monad and Comonad|monad]] on $\mathbf{Set}$.

**(b)** Exhibit an [[Def - Adjunction|adjunction]] whose induced monad is $(P, \eta, \mu)$, and use [[Thm - Every Adjunction Gives a Monad|the adjunction-monad theorem]] to re-derive part (a) without checking the monad axioms by hand.

**Recall:**

A [[Def - Monad and Comonad|monad]] on $\mathcal{C}$ is a triple $(T, \eta, \mu)$ with $T : \mathcal{C} \to \mathcal{C}$ an endofunctor, $\eta : 1 \Rightarrow T$, $\mu : T^2 \Rightarrow T$, satisfying

![[Def - Monad and Comonad#The Definition]]

By [[Thm - Every Adjunction Gives a Monad|the adjunction–monad theorem]], any [[Def - Adjunction|adjunction]] $F \dashv U$ ($F : \mathcal{C} \to \mathcal{D}$, $U : \mathcal{D} \to \mathcal{C}$) yields a monad on $\mathcal{C}$ with $T = UF$, unit the adjunction unit, and multiplication $\mu = U\varepsilon F$ the whiskered counit — and the monad axioms are then automatic.

---

# Convergent Strategy

**Problem class:** This is a "verify a candidate is a monad, then recognize it as the shadow of an adjunction" problem — the two standard ways of certifying a monad from the topic page's problem-solving strategy. Part (a) is the direct, axiom-checking route; part (b) is the conceptual route that makes the verification free.

**Assumption pattern:** The data given is an explicit endofunctor with explicit unit and multiplication, so the natural first move is direct verification (legal operation 2). But "power set = subsets" and "union = multiplication, singleton = unit" should immediately trigger the recognition that $P$ is the free *sup-lattice* functor composed with the forgetful functor — the assumption pattern of a free–forgetful adjunction (legal operation 1).

**Theorem routing:** Part (a) routes through the monad axioms directly. Part (b) routes through [[Thm - Every Adjunction Gives a Monad]]: identify the adjunction $\mathbf{Set} \rightleftarrows \mathbf{SupLat}$ (sets and complete sup-lattices), check that $UF = P$, $\eta$ = singleton, $U\varepsilon F$ = union, and conclude the monad axioms for free.

**Key decision point:** The non-obvious choice in (b) is *which* adjunction. The power-set functor underlies several adjunctions (it is also self-adjoint contravariantly), but the one inducing *this* monad — singleton unit and union multiplication — is the free-complete-sup-lattice adjunction, because the union of subsets is exactly the join in the sup-lattice $P(A)$, and the counit "evaluates a set of subsets to its join."

---

# Legal Operations Used

1. **Operation 2 from the topic page (check the monad axioms via whiskering).** In part (a) we verify associativity $\mu \circ P\mu = \mu \circ \mu P$ and the two unit laws by computing the effect of each side on a nested family of sets, taking care that $P\mu$ unions the *inner* families while $\mu P$ unions the *outer* family.

2. **Operation 1 from the topic page (read a monad off an adjunction).** In part (b) we recognize $P = UF$ for the free–forgetful adjunction between sets and complete sup-lattices, and invoke [[Thm - Every Adjunction Gives a Monad]] to obtain the monad without further checking.

---

# Hints

> [!note]- Hint 1
> For part (a), the associativity law $\mu \circ P\mu = \mu \circ \mu P$ acts on a set of sets of sets $\mathcal{T} \in P(P(P(A)))$. Compute both sides as a union of unions and use that unions are associative.

> [!note]- Hint 2
> Keep $P\mu$ and $\mu P$ straight: $P\mu$ applies $\mu$ inside, unioning each inner family $\mathcal{S} \in \mathcal{T}$ to $\bigcup\mathcal{S}$, giving a set of subsets; $\mu P$ first unions the outer level. Both then union once more.

> [!note]- Hint 3
> For part (b), think of $P(A)$ not as "subsets" but as "the free complete join-semilattice on $A$": every subset is the join $\bigvee_{a \in S}\{a\}$ of the generators it contains, and union is the join operation. The forgetful functor $U : \mathbf{SupLat} \to \mathbf{Set}$ has left adjoint $A \mapsto P(A)$.

> [!note]- Hint 4
> The counit $\varepsilon_L : P(UL) \to L$ at a sup-lattice $L$ is "take the join": $\varepsilon_L(S) = \bigvee S$. Whisker it: $U\varepsilon F$ at a set $A$ takes a set of subsets of $A$ — viewed inside the sup-lattice $P(A)$ — to their join, which is their union. That is $\mu$.

---

# Solution

The solution does part (a) by direct computation and part (b) by recognizing the free-sup-lattice adjunction. The plan: in (a) verify the three monad diagrams by computing unions of nested families; in (b) identify the adjunction $\mathbf{Set} \rightleftarrows \mathbf{SupLat}$, check $UF = P$ on objects and that the unit and whiskered counit match the given $\eta, \mu$, and invoke [[Thm - Every Adjunction Gives a Monad]]. The non-obvious move is reading "union" as "join in the free sup-lattice."

**Step 1 (a): Associativity.** $\mu \circ P\mu = \mu \circ \mu P$ as maps $P^3(A) \to P(A)$.

> [!note]- Derivation
> Let $\mathcal{T} \in P(P(P(A)))$ — a set whose elements $\mathcal{S}$ are sets of subsets of $A$.
>
> Compute $\mu_A \circ P(\mu_A)$. First $P(\mu_A)(\mathcal{T}) = \{\mu_A(\mathcal{S}) : \mathcal{S} \in \mathcal{T}\} = \{\bigcup\mathcal{S} : \mathcal{S} \in \mathcal{T}\}$, a set of subsets of $A$. Then $\mu_A$ of that is $\bigcup_{\mathcal{S}\in\mathcal{T}} \big(\bigcup\mathcal{S}\big) = \bigcup_{\mathcal{S}\in\mathcal{T}}\bigcup_{S \in \mathcal{S}} S$.
>
> Compute $\mu_A \circ \mu_{P(A)}$. First $\mu_{P(A)}(\mathcal{T}) = \bigcup_{\mathcal{S}\in\mathcal{T}}\mathcal{S}$, a set of subsets of $A$. Then $\mu_A$ of that is $\bigcup_{S \in \bigcup_{\mathcal{S}}\mathcal{S}} S = \bigcup_{\mathcal{S}\in\mathcal{T}}\bigcup_{S\in\mathcal{S}}S$.
>
> Both equal the union of all the bottom-level subsets, so they agree. Associativity holds because union is associative.

**Step 2 (a): Unit laws.** $\mu \circ P\eta = 1_P = \mu \circ \eta P$.

> [!note]- Derivation
> Take $S \in P(A)$, a subset of $A$.
>
> Left unit: $P(\eta_A)(S) = \{\{a\} : a \in S\}$, the set of singletons of elements of $S$. Then $\mu_A$ unions them: $\bigcup_{a\in S}\{a\} = S$. So $\mu_A \circ P(\eta_A) = 1$.
>
> Right unit: $\eta_{P(A)}(S) = \{S\}$, the one-element family containing $S$. Then $\mu_A(\{S\}) = \bigcup\{S\} = S$. So $\mu_A \circ \eta_{P(A)} = 1$.
>
> Both unit laws hold: unioning singletons recovers the set, and unioning a one-element family recovers the set.

**Step 3 (b): Identify the adjunction.** $P = UF$ for the free–forgetful adjunction $\mathbf{Set} \rightleftarrows \mathbf{SupLat}$.

> [!note]- Derivation
> Let $\mathbf{SupLat}$ be the category of complete join-semilattices (posets with all joins $\bigvee$) and join-preserving maps. The forgetful functor $U : \mathbf{SupLat} \to \mathbf{Set}$ has a left adjoint $F$ given by $F(A) = (P(A), \subseteq)$: the power set ordered by inclusion is a complete sup-lattice, with join = union, and it is the *free* one on $A$ — a join-preserving map out of $P(A)$ is determined by its values on the singletons (the generators $\{a\}$), so
> $$\mathbf{SupLat}(P(A), L) \cong \mathbf{Set}(A, UL), \qquad \varphi \mapsto (a \mapsto \varphi(\{a\})).$$
> This is the adjunction isomorphism, so $F \dashv U$. On objects $U F(A) = U(P(A),\subseteq) = P(A)$, recovering the endofunctor $P$.

**Step 4 (b): Match unit and multiplication, conclude.**

> [!note]- Derivation
> The adjunction unit $\eta_A : A \to UF(A) = P(A)$ is the transpose of the identity on $P(A)$, namely $a \mapsto \{a\}$ — the given singleton unit. The counit $\varepsilon_L : F U L \to L$, i.e. $P(UL) \to L$, is the transpose of $1_{UL}$, namely "take the join": $\varepsilon_L(S) = \bigvee_{x \in S} x$. Whiskering, $\mu = U\varepsilon F$ at $A$ is $\varepsilon_{P(A)} : P(P(A)) \to P(A)$, which takes a set $\mathcal{S}$ of subsets to their join *in the sup-lattice $P(A)$* — and the join in $(P(A),\subseteq)$ is union. So $\mu_A(\mathcal{S}) = \bigcup\mathcal{S}$, the given multiplication. By [[Thm - Every Adjunction Gives a Monad]], $(P, \eta, \mu) = (UF, \eta, U\varepsilon F)$ is a monad, with no axiom-checking required.

> [!note]- Complete formal solution
> **(a)** Define $\eta_A(a) = \{a\}$ and $\mu_A(\mathcal{S}) = \bigcup\mathcal{S}$.
>
> *Associativity:* for $\mathcal{T} \in P^3(A)$, both $\mu_A\circ P\mu_A$ and $\mu_A\circ\mu_{P(A)}$ evaluate to $\bigcup_{\mathcal{S}\in\mathcal{T}}\bigcup_{S\in\mathcal{S}}S$ (associativity of union), so $\mu\circ P\mu = \mu\circ\mu P$.
>
> *Unit laws:* for $S \in P(A)$, $\mu_A(P\eta_A(S)) = \bigcup_{a\in S}\{a\} = S$ and $\mu_A(\eta_{P(A)}(S)) = \bigcup\{S\} = S$, so $\mu\circ P\eta = 1 = \mu\circ\eta P$.
>
> Hence $(P,\eta,\mu)$ is a monad.
>
> **(b)** Let $\mathbf{SupLat}$ be complete join-semilattices with join-preserving maps and $U$ the forgetful functor. Then $F(A) = (P(A),\subseteq)$ is the free complete sup-lattice on $A$: $\mathbf{SupLat}(P(A),L) \cong \mathbf{Set}(A,UL)$ via $\varphi\mapsto(a\mapsto\varphi\{a\})$, so $F\dashv U$. Here $UF = P$, the unit is $a\mapsto\{a\}$, and the counit is $\varepsilon_L(S) = \bigvee S$; whiskering gives $\mu_A = \varepsilon_{P(A)} = \bigcup$ since the join in $(P(A),\subseteq)$ is union. By [[Thm - Every Adjunction Gives a Monad]], $(P,\eta,\mu)$ is the monad of this adjunction. $\blacksquare$

> [!tip] The algebras
> By [[Def - Algebra for a Monad]], the Eilenberg–Moore category $\mathbf{Set}^P$ is the category of $P$-algebras: a structure map $a : P(A) \to A$ assigning to each subset a "supremum," coherently. These are exactly complete sup-lattices, consistent with the free functor in part (b). This is a good check: the algebras for the free-sup-lattice monad should be sup-lattices.

---

# Key Takeaways

**Recognizing a "collect-and-combine" functor as a free-algebra monad.** The power-set monad is the prototype of a pattern: a functor that "collects elements into a structure" ($P$ collects into subsets, the list functor into words, the free-module functor into linear combinations) with a unit that "inserts a single generator" and a multiplication that "flattens nested collections." Whenever you meet such a functor, the trigger is to ask which free–forgetful adjunction it underlies — the multiplication is always the counit "evaluate the free structure," and recognizing this saves you from checking the monad axioms by hand. The diagnostic is: if the multiplication is an associative way to merge nested collections and the unit is a singleton-style inclusion, you are looking at $UF$ for a free functor $F$.

**Union is join, and that is why the algebras are lattices.** The conceptual content of part (b) is that "union of sets" is not a set-theoretic accident but the *join operation of a complete lattice*. Reading $P(A)$ as the free complete sup-lattice makes the multiplication (union) into the lattice join and the algebras (complete sup-lattices) fall out automatically. This is a recurring move: an apparently combinatorial operation (union, concatenation, formal sum) is the operation of a free algebraic structure, and identifying that structure tells you what the monad's algebras are. The same logic identifies the list monad's algebras as monoids and the free-module monad's algebras as modules.

**Direct verification and adjunction-recognition are complementary, not redundant.** Part (a) and part (b) prove the same fact two ways, and keeping both in your repertoire is the point. Direct verification (operation 2) is unavoidable when a monad is *defined* by an explicit endofunctor with no obvious adjunction — it is concrete and self-contained but teaches nothing transferable. Adjunction-recognition (operation 1) is the conceptual route: it is faster, it explains *why* the axioms hold (they are the triangle identities in disguise), and it immediately hands you the category of algebras. The skill to build is to attempt the recognition first and fall back on direct verification only when no adjunction presents itself — and the power-set monad shows that an adjunction is usually lurking even when the functor is presented combinatorially. See also [[Ex - The free monoid monad]] for the same pattern with concatenation in place of union.
