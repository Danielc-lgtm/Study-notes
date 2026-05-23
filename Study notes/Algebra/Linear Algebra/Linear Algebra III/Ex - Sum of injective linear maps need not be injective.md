---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
tags: [algebra, linear-algebra]
---

# Problem Statement

Show that the set $\{T \in \mathcal{L}(V, W) : T \text{ is injective}\}$ is *not* a [[Def - Subspace|subspace]] of $\mathcal{L}(V, W)$, by exhibiting injective $S, T \in \mathcal{L}(V, W)$ whose sum $S + T$ is not injective. (Take $V$ and $W$ finite-dimensional with $\dim V \geq 2$; the result for higher [[Def - Dimension|dimensions]] follows similarly.)

**Recall:**

![[Def - Linear Map#The Definition]]

The vector space $\mathcal{L}(V, W)$ has pointwise operations $(S + T)(v) := Sv + Tv$ and $(\lambda T)(v) := \lambda Tv$ (see [[Def - Linear Map]]).

A linear map $T$ is **injective** iff $\operatorname{null} T = \{0\}$, by the [[Def - Null Space and Range|null-space-injectivity criterion]].

A subset $X \subseteq \mathcal{L}(V, W)$ is a **subspace** iff it contains the zero map *and* is closed under addition and scalar multiplication. The zero map is not injective (it kills everything), so the set of injective maps already fails to contain $0$ — but this is somewhat trivial. The more substantive failure is that the set is not closed under addition: two injective maps can sum to a non-injective map.

---

# Convergent Strategy

**Problem class.** This is a *show a candidate is not a subspace* problem — equivalently, *show a property of linear maps is not preserved under sums*. The topic-page Problem-Solving Strategy categorises this under "structural facts about $\mathcal{L}(V, W)$": exploit the vector-space structure of $\mathcal{L}(V, W)$ (where "vector space" means closed under sum and scalar multiplication) and find a property that is *not* additive.

**Assumption pattern.** $V$ and $W$ are vector spaces, $\dim V \geq 2$ (so there is room to find non-trivial injective maps whose sum kills something). The defining feature: we need to construct two specific injective $S, T$ whose sum has non-trivial kernel.

**Theorem routing.** No named theorem is needed; the proof is constructive. The natural construction is to take $S$ and $T = -S$ (the additive inverse): both are injective (since $-S$ is injective iff $S$ is, by multiplying by $-1$), but $S + T = 0$ is the zero map, which is not injective. This is the simplest valid counterexample.

**Key decision point.** The crucial recognition is that *injectivity is symmetric under negation*: $T$ injective iff $-T$ injective, since $\operatorname{null}(-T) = \operatorname{null} T$. So the pair $(S, -S)$ is a pair of two injective maps, and their sum is the zero map. The "key decision" is to choose this pair rather than something more elaborate. A more sophisticated construction would use two non-zero injective maps that happen to "cancel" on some non-zero vector, but the negation trick is cleaner.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Specify a linear map by its action on a basis** (operation 1). We use the identity map (or any injective map) as $S$, and $-S$ as $T$. Both are concretely given.

2. **Build new linear maps by sum, composition, restriction, and extension** (operation 10). We sum $S$ and $-S$ to get the zero map; the sum operation on $\mathcal{L}(V, W)$ is what makes this whole problem possible.

3. **Convert injectivity to surjectivity (or vice versa) using equal finite [[Def - Dimension|dimension]]** (operation 4), as a sanity check. In the finite-dimensional case with $V = W$, an injective map is invertible. The negative of an invertible map is invertible. Their sum is zero — not invertible. So the result also says "the invertible linear maps are not a subspace", which is more striking.

---

# Hints

> [!note]- Hint 1
> What is the simplest non-zero linear map you know? What is its negative? Are both of them injective?

> [!note]- Hint 2
> The identity operator $I : V \to V$ is injective. The map $-I$, defined by $v \mapsto -v$, is also injective. What is $I + (-I)$?

> [!note]- Hint 3
> The pair $(I, -I)$ are both injective, and $I + (-I) = 0$. The zero map has $\operatorname{null} 0 = V$, which is not $\{0\}$ unless $V = \{0\}$. So for $V \neq \{0\}$, the sum is not injective.

---

# Solution

The strategy is to take $S$ to be any injective linear map and $T$ to be its negation $-S$. Both are injective (negation preserves injectivity), and their sum is the zero map, which is not injective on a non-trivial space.

**Step 1: The identity $I : V \to V$ is injective.**

This is immediate from the definition of injectivity.

> [!note]- Derivation
> The identity operator $I_V \in \mathcal{L}(V)$ is defined by $Iv = v$ for every $v$. If $Iv = 0$, then $v = 0$. So $\operatorname{null} I = \{0\}$, and by the injectivity criterion ($T$ injective iff $\operatorname{null} T = \{0\}$), $I$ is injective.

(For the statement of the problem with $V, W$ possibly different, take $W = V$ and any injective $T : V \to W$ — e.g., the identity if $V = W$, or any specific injective map if $V \neq W$. The argument below works identically with $S = T$, $T = -T$.)

**Step 2: $-I$ is injective.**

The negation of an injective map is injective.

> [!note]- Derivation
> $(-I)(v) = -v$. If $(-I)(v) = 0$, then $-v = 0$, so $v = 0$. Hence $\operatorname{null}(-I) = \{0\}$, and $-I$ is injective.
>
> Alternatively (and more general): if $T$ is injective and $\lambda \neq 0$, then $\lambda T$ is injective. The null space is the same: $(\lambda T)(v) = 0$ iff $\lambda \cdot Tv = 0$ iff $Tv = 0$ (since $\lambda \neq 0$) iff $v = 0$ (by injectivity of $T$).

**Step 3: $I + (-I) = 0$, which is not injective (when $V \neq \{0\}$).**

> [!note]- Derivation
> By pointwise sum, $(I + (-I))(v) = Iv + (-I)(v) = v + (-v) = 0$ for every $v \in V$. So $I + (-I) = 0_\mathcal{L}$, the zero map.
>
> The zero map has $\operatorname{null} 0 = V$ (everything is in the null space, since $0(v) = 0$ for all $v$). For $V \neq \{0\}$, this is strictly larger than $\{0\}$, so $0$ is not injective.

> [!note]- Complete formal solution
> Let $V$ be a non-zero vector space over $\mathbf{F}$ and consider $\mathcal{L}(V, V)$.
>
> Let $S = I$ (the identity operator) and $T = -I$. Both are injective: $I$ has $\operatorname{null} I = \{0\}$ (since $Iv = v$, so $Iv = 0 \Leftrightarrow v = 0$), and $-I$ has $\operatorname{null}(-I) = \{0\}$ by the same argument.
>
> Their sum is $(S + T)(v) = Iv + (-I)(v) = v - v = 0$ for every $v$, so $S + T = 0$ is the zero map. The zero map has $\operatorname{null} 0 = V \neq \{0\}$, hence is not injective.
>
> Therefore the set of injective linear maps is not closed under addition, so it is not a subspace of $\mathcal{L}(V, V)$. The same construction adapted to maps $V \to W$ (using any injective map $S : V \to W$ and $T = -S$) shows that injective maps in $\mathcal{L}(V, W)$ are not a subspace for any $V, W$ with at least one injective map. $\blacksquare$

> [!warning] Illegal but tempting alternative route: the zero map argument alone
> A *quicker* but less informative argument is: "the zero map is in any subspace, but is not injective (when $V \neq \{0\}$), so the set of injective maps does not even contain $0$, hence is not a subspace". This is valid but unsatisfying — it does not exhibit the *failure of closure under addition*, which is the substantive property of [[Def - Subspace|subspaces]] being violated. The construction above is the "real" counterexample, showing that closure under addition is the failing axiom.

---

# Key Takeaways

**Properties of linear maps are not closed under sum in general.** Many natural properties — injectivity, surjectivity, invertibility, having a specific rank, having a specific eigenvalue — are *not* preserved under sums of linear maps. The sum of two rank-$r$ maps can have any rank from $0$ to $2r$; the sum of two injective maps can be the zero map. The reusable principle is to not treat "property P" as a subspace condition automatically. The trigger is any sentence of the form "the set of linear maps with property P is a subspace" — check carefully before accepting. The properties that *are* closed under sum (or scalar multiplication, or both) are special: vanishing on a fixed subspace, mapping into a fixed subspace, being in a fixed similarity class are *not* (the last one is a hard one), but "the matrix has zeros in some fixed positions" is.

**The negation trick: $T$ and $-T$ have the same null space.** Scalar multiplication by a non-zero scalar preserves both null space and range: $\operatorname{null}(\lambda T) = \operatorname{null} T$ and $\operatorname{range}(\lambda T) = \operatorname{range} T$ for $\lambda \neq 0$. This is the algebraic content of "scaling does not change the structure of a linear map". The reusable principle is that when you need *two* maps with the same property, the pair $(T, -T)$ or $(T, \lambda T)$ for any non-zero $\lambda$ is often a quick source. The trigger is "construct two maps satisfying P" — try the negation first; if it works, you're done.

**Constructive counterexamples are stronger than non-existence arguments.** This exercise asks to *exhibit* a counterexample. The lazy argument — "the zero map is not in the set, so it is not a subspace" — is technically valid but does not display the actual failure of closure. The constructive argument $(I, -I) \mapsto 0$ shows *what goes wrong*. The reusable principle is: when proving "X is not a Y", aim to *display* the failure of the defining condition, not merely point to a missing element. The richer counterexample reveals more.

---
