---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Barr-Beck Monadicity Theorem"
  - "Def - Algebra for a Monad"
  - "Def - Monad and Comonad"
tags: [category-theory, foundations]
---

# Problem Statement

Fix a [[Def - Monoid in a Monoidal Category|monoid]] $M$ (in $\mathbf{Set}$). An **$M$-set** is a set $X$ with a left action $M \times X \to X$ satisfying $1\cdot x = x$ and $(mn)\cdot x = m\cdot(n\cdot x)$; morphisms are equivariant maps. Let $M\text{-}\mathbf{Set}$ be the resulting category and $U : M\text{-}\mathbf{Set} \to \mathbf{Set}$ the forgetful functor.

**(a)** Identify the [[Def - Monad and Comonad|monad]] $T$ on $\mathbf{Set}$ whose [[Def - Algebra for a Monad|algebras]] are $M$-sets.

**(b)** Use the [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck theorem]] to prove $U$ is monadic, i.e. $M\text{-}\mathbf{Set} \simeq \mathbf{Set}^T$.

**(c)** As a second example, identify the monad whose algebras are **pointed sets** (sets with a chosen basepoint).

**Recall:**

![[Thm - The Barr-Beck Monadicity Theorem#Statement]]

A $T$-algebra is a set $A$ with $a : TA \to A$ satisfying $a\circ\eta_A = 1$ and $a\circ\mu_A = a\circ Ta$ (see [[Def - Algebra for a Monad]]).

---

# Convergent Strategy

**Problem class:** A "recognize a concrete category as algebras" problem — the reverse of [[Ex - Which forgetful functors are monadic]]. Here we are told the category is algebraic and must *identify the monad* and *certify* the equivalence.

**Assumption pattern:** The action axioms $1\cdot x = x$ and $(mn)\cdot x = m(nx)$ are exactly the algebra unit and associativity laws for the monad $T(X) = M\times X$ (legal operation 3). The forgetful functor has a free object (the free $M$-set $M\times X$), so Barr–Beck applies (operation 5).

**Theorem routing:** Route through [[Def - Algebra for a Monad]] to guess the monad $T(X) = M\times X$, then through [[Thm - The Barr-Beck Monadicity Theorem]] to certify $U$ monadic by checking the three conditions.

**Key decision point:** The non-obvious step is *guessing the right monad*. The action $M\times X \to X$ already has the shape of an algebra structure map $T(X)\to X$, which forces $T(X) = M\times X$, with $\eta$ = "act by $1$" and $\mu$ = "multiply in $M$." Recognizing the action map as the structure map is the whole insight.

---

# Legal Operations Used

1. **Operation 3 from the topic page (build the structure map of an algebra).** The $M$-action *is* the algebra structure map $M\times X \to X$, which pins down $T(X) = M\times X$.

2. **Operation 5 from the topic page (apply Barr–Beck to recognize algebras).** We verify the three Barr–Beck conditions for $U : M\text{-}\mathbf{Set}\to\mathbf{Set}$.

3. **Operation 1 from the topic page (read a monad off an adjunction).** The free $M$-set adjunction gives the monad $T = M\times(-)$ directly.

---

# Hints

> [!note]- Hint 1
> An $M$-action is a map $M\times X \to X$. Compare to an algebra structure map $T(X)\to X$. This forces $T(X) = M\times X$. Now find $\eta$ and $\mu$ making the action axioms into the algebra axioms.

> [!note]- Hint 2
> $\eta_X : X \to M\times X$ should be $x\mapsto (1, x)$ (the unit law $a\circ\eta = 1$ becomes $1\cdot x = x$). $\mu_X : M\times(M\times X) \to M\times X$ should be $(m,(n,x))\mapsto (mn, x)$ (the associativity law becomes $(mn)\cdot x = m(n\cdot x)$).

> [!note]- Hint 3
> For Barr–Beck: the free $M$-set on $X$ is $M\times X$ with action $m'\cdot(m,x) = (m'm,x)$, giving a left adjoint. Conservativity: an equivariant bijection has an equivariant inverse. Split coequalizers: quotients of $M$-sets carry the induced action.

> [!note]- Hint 4
> For (c), pointed sets: a basepoint is a map $1 \to X$ from the one-point set; equivalently the monad is $T(X) = X + 1$ (the [[Def - Monad and Comonad|maybe monad]]), with $\eta$ the inclusion and the algebra structure map picking out the basepoint.

---

# Solution

The plan: (a) recognize the action as the algebra structure map, forcing $T(X) = M\times X$ with the multiplication monad structure; (b) verify the three Barr–Beck conditions; (c) repeat the recognition for pointed sets, landing on the maybe monad. The crux is reading the defining structure map as a monad algebra.

**Step 1 (a): Identify the monad.**

> [!note]- Derivation
> An $M$-action is a function $\alpha : M\times X \to X$. This has exactly the type of an algebra structure map $T(X)\to X$ with $T(X) = M\times X$. Define the monad $(T,\eta,\mu)$:
> $$T(X) = M\times X, \qquad \eta_X(x) = (1, x), \qquad \mu_X(m,(n,x)) = (mn, x).$$
> Check it is a monad: associativity $\mu\circ T\mu = \mu\circ\mu T$ becomes $(m,(n,(p,x)))\mapsto(mnp,x)$ both ways, by associativity of $M$; unit laws become $(1\cdot m, x) = (m,x)$ and $(m\cdot 1, x) = (m,x)$, by unitality of $M$. This is the **writer monad** for $M$ (action by left multiplication). The algebra axioms $a\circ\eta = 1$, $a\circ\mu = a\circ Ta$ for $a = \alpha$ read $1\cdot x = x$ and $(mn)\cdot x = m\cdot(n\cdot x)$ — exactly the $M$-action axioms. So $M$-sets are $T$-algebras.

**Step 2 (b): Barr–Beck conditions.**

> [!note]- Derivation
> *Left adjoint:* the free $M$-set on $X$ is $(M\times X, \text{act by left mult.})$, with $\mathbf{}M\text{-}\mathbf{Set}(M\times X, Y) \cong \mathbf{Set}(X, UY)$ (an equivariant map out of the free $M$-set is determined by where it sends $(1,x)$). So $U$ has a left adjoint, $UF = M\times(-) = T$ (condition 1).
>
> *Conservative:* an equivariant bijection $f : X \to Y$ has set-inverse $f^{-1}$, which is equivariant: $f^{-1}(m\cdot y) = f^{-1}(m\cdot f(f^{-1}y)) = f^{-1}(f(m\cdot f^{-1}y)) = m\cdot f^{-1}(y)$. So $Uf$ iso $\Rightarrow f$ iso (condition 2).
>
> *Creates split coequalizers:* given a $U$-split pair of equivariant maps, the coequalizer in $\mathbf{Set}$ is a quotient $Y/{\sim}$, and the $M$-action descends to the quotient (the split provides representatives compatibly), uniquely and preserved by $U$ (condition 3).
>
> By [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]], $U$ is monadic: $M\text{-}\mathbf{Set} \simeq \mathbf{Set}^T$.

**Step 3 (c): Pointed sets.**

> [!note]- Derivation
> A pointed set is a set $X$ with a chosen point $* \in X$, equivalently a map $1 \to X$. The monad is the [[Def - Monad and Comonad|maybe monad]] $T(X) = X + 1$, with $\eta_X$ the inclusion $X \hookrightarrow X+1$ and $\mu_X : (X+1)+1 \to X+1$ collapsing the two added points to one. An algebra structure map $a : X+1 \to X$ restricts to the identity on $X$ (unit law) and sends the adjoined point $*$ to a chosen element $a(*) \in X$ — the basepoint. The associativity law makes this consistent. So $\mathbf{Set}^T$ for the maybe monad is the category of pointed sets, $\mathbf{Set}_*$. (Conversely the free pointed set on $X$ is $X+1$, confirming the adjunction.)

> [!note]- Complete formal solution
> **(a)** $T(X) = M\times X$, $\eta_X(x) = (1,x)$, $\mu_X(m,(n,x)) = (mn,x)$, a monad by associativity and unitality of $M$. The algebra laws for $a : M\times X\to X$ are exactly the $M$-action axioms.
>
> **(b)** Free $M$-set $M\times X$ gives a left adjoint with $UF = T$ (1); equivariant bijections have equivariant inverses (2); $M$-actions descend to set-coequalizers of $U$-split pairs (3). By Barr–Beck, $M\text{-}\mathbf{Set}\simeq\mathbf{Set}^T$.
>
> **(c)** Pointed sets are the algebras of the maybe monad $T(X) = X+1$: the structure map fixes $X$ and sends the adjoined point to the basepoint. $\blacksquare$

> [!tip] Sanity check: free objects match
> In (a) the free $M$-set $M\times X$ equals $T(X)$, and in (c) the free pointed set $X+1$ equals $T(X)$, as required: the free algebra on $X$ is always $(TX, \mu_X)$. Verifying that the free object you expect equals $T(X)$ is a quick consistency check on the guessed monad.

---

# Key Takeaways

**The defining structure map *is* the algebra structure map — read it off directly.** The fastest route to identifying the monad behind a category of structured sets is to find the single map that defines the structure ($M\times X \to X$ for $M$-sets, $1\to X$ for pointed sets) and recognize it as an algebra structure map $T(X)\to X$ (or, for nullary operations, fold the chosen point into $T(X) = X+1$). This forces the endofunctor $T$ and usually makes $\eta$ and $\mu$ obvious. The trigger is "a category defined by one operation with axioms"; the reaction is "that operation is the structure map, so $T$ is whatever its domain is as a functor of $X$."

**Algebraic categories pass Barr–Beck by the same three one-liners.** For any category of sets-with-operations-and-equations, the three Barr–Beck conditions have a stereotyped verification: the left adjoint is the free object (operations applied formally), conservativity holds because a structure-preserving bijection has a structure-preserving inverse, and creation of split coequalizers holds because the structure descends to quotients (the split supplying compatible representatives). Recognizing this template means you rarely have to think hard about monadicity for an algebraic category — the work is identifying the monad, after which Barr–Beck is a formality. The contrast is with [[Ex - Which forgetful functors are monadic|topology and fields]], where one of these one-liners fails.

**Nullary and unary operations both fit the monad framework.** This exercise shows the monad recipe accommodates operations of any arity: a unary action ($M\times X\to X$, parametrized by $M$) gives $T(X) = M\times X$, while a nullary operation (a chosen basepoint, $1\to X$) gives $T(X) = X+1$, folding the constant into the functor. The general principle is that a monad on $\mathbf{Set}$ encodes a whole signature of operations of all arities at once, and the endofunctor $T(X)$ is "the set of formal operation-terms in variables from $X$." Whether the structure is an action, a basepoint, a binary multiplication, or all of these, the monad packages it uniformly — which is exactly the universal-algebra content of [[Def - Algebra for a Monad]].
