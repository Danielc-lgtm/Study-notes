---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
  - "Def - Quotient Space"
  - "Def - Quotient Map of Linear Map"
  - "Thm - Fundamental Theorem of Linear Maps"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ and $W$ be vector spaces over $\mathbb{F}$ and $T \in \mathcal{L}(V, W)$ a linear map. Define $\tilde T : V / \operatorname{null} T \to W$ by
$$\tilde T(v + \operatorname{null} T) := Tv.$$

Prove that:
1. $\tilde T$ is well-defined (independent of the representative $v$);
2. $\tilde T$ is a linear map from $V/\operatorname{null} T$ to $W$;
3. $\tilde T$ is injective;
4. $\operatorname{range} \tilde T = \operatorname{range} T$.

Conclude that $\tilde T$ restricts to a linear isomorphism
$$V/\operatorname{null} T \;\xrightarrow{\;\cong\;}\; \operatorname{range} T,$$
and, when $V$ is finite-dimensional, derive the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]] $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ as a consequence.

**Recall:**

A [[Def - Linear Map|linear map]] $T : V \to W$ satisfies $T(v_1 + v_2) = Tv_1 + Tv_2$ and $T(\lambda v) = \lambda Tv$.

![[Def - Quotient Space#The Definition]]

![[Def - Null Space and Range#The Definition]]

A linear map is *injective* iff its null space is $\{0\}$, and is an *isomorphism* iff it is both injective and surjective onto its codomain.

---

# Convergent Strategy

**Problem class.** This is the linear-algebraic *first isomorphism theorem* — the structural rereading of [[Thm - Fundamental Theorem of Linear Maps|rank-nullity]]. The exercise is the template for *identifying a quotient* of a vector space as a familiar object, and it is the gateway exercise of the chapter. As stated in the [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Problem-Solving Strategy|topic page]], "identifying a quotient" routes through this isomorphism.

**Assumption pattern.** The recognisable signal is the very setup of the problem: a linear map $T$ is given, and we want to understand its quotient $V/\operatorname{null} T$. The null space is precisely the [[Def - Subspace|subspace]] that "$T$ forgets", so by quotienting by it we get the space on which $T$ becomes faithful — injective. The four properties (well-definedness, linearity, injectivity, range identification) need to be checked separately because each addresses a different requirement for $\tilde T$ to be an isomorphism.

**Theorem routing.** The route has four mechanical steps, all forced by definitions:
- *Well-definedness* uses the partition property of [[Def - Coset|cosets]] ([[Def - Affine Subset|3.101]]): $v + \operatorname{null} T = v' + \operatorname{null} T \iff v - v' \in \operatorname{null} T$.
- *Linearity* uses the definitions of operations on $V/U$ and the linearity of $T$.
- *Injectivity* uses the *same* equation as well-definedness, read in reverse.
- *Range identification* is direct: $\tilde T$ maps to the same image set as $T$ does.

Once the isomorphism is established, taking [[Def - Dimension|dimensions]] gives the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] as a corollary.

**Key decision point.** The non-obvious move is *seeing that the isomorphism is what makes rank-nullity "obvious"*. Most students learn rank-nullity as a counting identity and treat it as a separate fact. The exercise reveals that the identity *follows from a structural isomorphism* — that is, both sides count the dimension of the same vector space. Once seen, the counting becomes a consequence of the structure, not an independent theorem.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Legal Operations|the topic page]]:

1. **Partition $V$ into [[Def - Coset|cosets]] of a [[Def - Subspace|subspace]]** (operation 1). The cosets of $\operatorname{null} T$ partition $V$, and the partition is the foundation of both well-definedness and injectivity. The same identity $v + \operatorname{null} T = v' + \operatorname{null} T \iff v - v' \in \operatorname{null} T$ is used in both directions.

2. **Form the quotient to make $\operatorname{null} T$ disappear** (operation 2). Replacing $V$ by $V/\operatorname{null} T$ removes exactly the directions $T$ ignores, producing the space on which $T$ becomes injective.

3. **Identify a quotient via the first isomorphism theorem** (operation 3). This *is* the first isomorphism theorem; the exercise is its proof and template for use.

---

# Hints

> [!note]- Hint 1
> The rule $\tilde T(v + \operatorname{null} T) := Tv$ uses a representative $v$ of the coset. Before anything else, check that the value $Tv$ does not depend on which representative you chose — that is, well-definedness. The key identity: two cosets $v + \operatorname{null} T$ and $v' + \operatorname{null} T$ are equal precisely when $v - v' \in \operatorname{null} T$.

> [!note]- Hint 2
> Once $\tilde T$ is well-defined, linearity is automatic from the definitions: $(v + N) + (v' + N) = (v + v') + N$, $\lambda(v + N) = (\lambda v) + N$. Apply $\tilde T$ and use linearity of $T$.

> [!note]- Hint 3
> For injectivity, the null space of $\tilde T$ in $V/\operatorname{null} T$ is the set of cosets $v + \operatorname{null} T$ with $\tilde T(v + \operatorname{null} T) = 0$. By the definition of $\tilde T$, this is $Tv = 0$, i.e. $v \in \operatorname{null} T$, i.e. $v + \operatorname{null} T = 0 + \operatorname{null} T$ — the zero coset. So $\operatorname{null} \tilde T = \{0\}$.

> [!note]- Hint 4
> For range identification, the range of $\tilde T$ is the set of images $\tilde T(v + \operatorname{null} T) = Tv$ as $v$ ranges over $V$. This is exactly $\operatorname{range} T$.

> [!note]- Hint 5
> For the fundamental theorem: $V/\operatorname{null} T \cong \operatorname{range} T$ gives $\dim(V/\operatorname{null} T) = \dim \operatorname{range} T$. Combine with $\dim(V/\operatorname{null} T) = \dim V - \dim \operatorname{null} T$ from the [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread|quotient dimension formula]] to get $\dim V - \dim \operatorname{null} T = \dim \operatorname{range} T$, equivalent to the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]].

---

# Solution

The proof breaks into four steps. Step 1 establishes that $\tilde T$ is well-defined using the coset partition lemma. Step 2 shows linearity by direct computation. Step 3 establishes injectivity by computing the null space, and step 4 reads off the range. The non-obvious move is *Step 1*, the well-definedness check, where the rule "apply $T$ to a representative" must be verified independent of the choice of representative — this is where the algebra lives.

**Step 1: $\tilde T$ is well-defined.**

If $v + \operatorname{null} T = v' + \operatorname{null} T$, then $Tv = Tv'$, so $\tilde T(v + \operatorname{null} T) = Tv$ is independent of the choice of $v$.

> [!note]- Derivation
> Suppose $v + \operatorname{null} T = v' + \operatorname{null} T$ in $V/\operatorname{null} T$. By the [[Def - Affine Subset#Lemma: Two Translates of a Subspace are Equal or Disjoint|partition lemma 3.101]], two cosets are equal precisely when their basepoints differ by an element of the subspace:
> $$v + \operatorname{null} T = v' + \operatorname{null} T \iff v - v' \in \operatorname{null} T.$$
> So $v - v' \in \operatorname{null} T$, which by definition of the null space gives $T(v - v') = 0$ in $W$. By linearity of $T$, $T(v - v') = Tv - Tv'$, so $Tv = Tv'$. Hence the rule $\tilde T(v + \operatorname{null} T) := Tv$ assigns the same value $Tv$ regardless of which representative $v$ is chosen from the coset.

**Step 2: $\tilde T$ is linear.**

Write $N = \operatorname{null} T$. For all cosets $v + N, v' + N \in V/N$ and $\lambda \in \mathbb{F}$:
$$\tilde T((v + N) + (v' + N)) = \tilde T(v + N) + \tilde T(v' + N), \qquad \tilde T(\lambda(v + N)) = \lambda \tilde T(v + N).$$

> [!note]- Derivation
> Using the definitions of the operations on $V/N$:
> $$(v + N) + (v' + N) := (v + v') + N, \qquad \lambda(v + N) := (\lambda v) + N.$$
> Compute:
> $$\tilde T((v + N) + (v' + N)) = \tilde T((v + v') + N) = T(v + v') = Tv + Tv' = \tilde T(v + N) + \tilde T(v' + N),$$
> using the definition of $\tilde T$ in the second and last equalities, and linearity of $T$ in the third. Similarly:
> $$\tilde T(\lambda(v + N)) = \tilde T((\lambda v) + N) = T(\lambda v) = \lambda Tv = \lambda \tilde T(v + N).$$
> So $\tilde T$ is linear.

**Step 3: $\tilde T$ is injective.**

The null space of $\tilde T$ in $V/N$ consists only of the zero coset $0 + N = N$.

> [!note]- Derivation
> Suppose $\tilde T(v + N) = 0$ in $W$. By definition, $\tilde T(v + N) = Tv$, so $Tv = 0$, i.e. $v \in N = \operatorname{null} T$. By the [[Def - Affine Subset#Lemma: Two Translates of a Subspace are Equal or Disjoint|partition lemma]] again, $v \in N$ if and only if $v + N = 0 + N$, the zero coset of $V/N$.
>
> So $\operatorname{null} \tilde T = \{0 + N\}$, i.e. $\tilde T$ has trivial null space, hence $\tilde T$ is injective.
>
> Note the *symmetry* with Step 1: well-definedness used "$v - v' \in N \Rightarrow Tv = Tv'$", and injectivity uses "$Tv = Tv' \Rightarrow v - v' \in N$". The same equation $T(v - v') = Tv - Tv' = 0 \iff v - v' \in N$ is read in opposite directions.

**Step 4: $\operatorname{range} \tilde T = \operatorname{range} T$.**

By definition, $\operatorname{range} \tilde T = \{\tilde T(v + N) : v \in V\} = \{Tv : v \in V\} = \operatorname{range} T$.

> [!note]- Derivation
> The range of $\tilde T$ is, by definition, the set of values $\tilde T$ takes on $V/N$:
> $$\operatorname{range} \tilde T = \{\tilde T(\bar v) : \bar v \in V/N\} = \{\tilde T(v + N) : v \in V\} = \{Tv : v \in V\} = \operatorname{range} T.$$
> The second equality is the surjectivity of the quotient map $\pi : V \to V/N$ — every $\bar v \in V/N$ has the form $v + N$ for some $v$. The third equality is the definition of $\tilde T$.

**Conclude.** $\tilde T$ is a well-defined, linear, injective map with range $\operatorname{range} T$. So $\tilde T$ restricted to $\operatorname{range} T$ is a linear bijection — an isomorphism:
$$V/\operatorname{null} T \;\xrightarrow{\;\cong\;}\; \operatorname{range} T.$$

**Step 5 (corollary): The fundamental theorem of linear maps.**

When $V$ is finite-dimensional, taking [[Def - Dimension|dimensions]] of the isomorphism:
$$\dim V - \dim \operatorname{null} T \;=\; \dim(V/\operatorname{null} T) \;=\; \dim \operatorname{range} T,$$
using the [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread|quotient dimension formula]] $\dim(V/U) = \dim V - \dim U$. Rearranging:
$$\dim V \;=\; \dim \operatorname{null} T + \dim \operatorname{range} T.$$
This is the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]], reread as a counting consequence of the isomorphism. $\blacksquare$

> [!note]- Complete formal solution
> Write $N = \operatorname{null} T$ throughout.
>
> *$\tilde T$ is well-defined.* Suppose $v + N = v' + N$. By the partition lemma, $v - v' \in N$, so $T(v - v') = 0$, hence $Tv = Tv'$. Therefore $\tilde T(v + N) = Tv$ is independent of the representative.
>
> *$\tilde T$ is linear.* Using the quotient operations and linearity of $T$:
> $$\tilde T((v + N) + (v' + N)) = \tilde T((v + v') + N) = T(v + v') = Tv + Tv' = \tilde T(v + N) + \tilde T(v' + N),$$
> $$\tilde T(\lambda(v + N)) = \tilde T((\lambda v) + N) = T(\lambda v) = \lambda Tv = \lambda \tilde T(v + N).$$
>
> *$\tilde T$ is injective.* $\tilde T(v + N) = 0 \iff Tv = 0 \iff v \in N \iff v + N = 0 + N$, so $\operatorname{null} \tilde T = \{0 + N\}$.
>
> *$\operatorname{range} \tilde T = \operatorname{range} T$.* By definition, $\operatorname{range} \tilde T = \{Tv : v \in V\} = \operatorname{range} T$.
>
> Therefore $\tilde T$ restricts to a linear isomorphism $V/N \cong \operatorname{range} T$.
>
> *Fundamental theorem of linear maps.* Taking dimensions when $V$ is finite-dimensional,
> $$\dim V - \dim \operatorname{null} T = \dim(V/N) = \dim \operatorname{range} T,$$
> so $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$. $\blacksquare$

> [!warning] Illegal but tempting: defining $\tilde T$ before checking well-definedness
> A common slip is to write "define $\tilde T(v + N) := Tv$" and start using $\tilde T$ as if it were a function, before checking that the value is independent of the representative. Until well-definedness is checked, $\tilde T$ is *not a function* — the rule $v + N \mapsto Tv$ is ambiguous because the same coset has multiple representatives. The well-definedness check is the *content* of the first step, not a technicality to skip.

---

# Key Takeaways

**Quotienting by the null space is exactly the operation that makes a linear map injective, and the resulting map is an isomorphism onto the range.** This is the gateway insight of the entire chapter. The construction $\tilde T : V/\operatorname{null} T \cong \operatorname{range} T$ converts a non-injective linear map into a canonical isomorphism between two concrete vector spaces. To use this template in problems: whenever you have a linear map $T$ and an opaque quotient $V/U$, ask "is $U = \operatorname{null} T$ for some natural $T$?" — if yes, the quotient is isomorphic to $\operatorname{range} T$, and you have just identified it. The same template identifies $\mathbb{Z}/n\mathbb{Z}$ as the image of "reduction mod $n$", identifies $\mathbb{C}^\times$ as the image of $z \mapsto e^z$ from $\mathbb{C}$, and identifies $\mathcal{P}_n / x \mathcal{P}_{n-1}$ as $\mathbb{F}$ via evaluation at zero. Three checks — homomorphism, surjection onto candidate, kernel equals candidate — and the identification is done.

**The fundamental theorem of linear maps is the *counting shadow* of a structural isomorphism.** Most students learn $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ as a separate theorem with its own proof. The present exercise reveals that the identity follows from an underlying isomorphism: both sides count the dimension of *the same vector space*, namely $V/\operatorname{null} T \cong \operatorname{range} T$. This is a much more conceptual statement than the counting identity, and it generalises beyond linear algebra — the same pattern produces the first isomorphism theorem for [[Def - Group|groups]], [[Def - Ring|rings]], and [[Def - Module|modules]], in each case with the dimension shadow replaced by the appropriate notion (index, cardinality of quotient [[Def - Ring|ring]], length of [[Def - Module|module]]). When you find yourself reaching for rank-nullity, ask if the *isomorphism* is the more natural tool — often it is, and it produces a map you can use, not just a number you can quote.

**The same algebraic equation $T(v - v') = Tv - Tv'$ is used in two directions: well-definedness and injectivity.** The well-definedness check (Step 1) uses "cosets equal $\Rightarrow$ images equal": $v + N = v' + N \Rightarrow v - v' \in N \Rightarrow T(v - v') = 0 \Rightarrow Tv = Tv'$. The injectivity check (Step 3) uses the same chain in reverse: $Tv = Tv' \Rightarrow T(v - v') = 0 \Rightarrow v - v' \in N \Rightarrow v + N = v' + N$. The symmetry is no coincidence; it is the structural reason that the quotient by the null space is *exactly the right* subspace to make $T$ injective — quotienting by anything smaller leaves residual non-injectivity, quotienting by anything larger throws away information.

**A linear map factors canonically as surjection-isomorphism-inclusion.** Every linear map $T : V \to W$ has the canonical factorisation $V \xrightarrow{\pi} V/\operatorname{null} T \xrightarrow{\tilde T \cong} \operatorname{range} T \xrightarrow{j} W$, where $\pi$ is the quotient (surjective), $\tilde T$ is the induced isomorphism, and $j$ is the inclusion (injective). This is the *epi-iso-mono factorisation*, and it is one of the defining properties of an *abelian category*. The existence of this canonical factorisation is what makes linear algebra work the way it does — every linear map has a "shape" that can be cleanly decomposed, and the decomposition does not depend on any choices.

**Cross-link to companion exercises.** This exercise is the structural template for [[Ex - Annihilator of a subspace has complementary dimension]] ([[Def - Annihilator|annihilator]] dimension via inclusion-and-dualisation) and for [[Ex - Row rank equals column rank]] (row-column rank via the rank of $T'$). Both of those exercises use the first isomorphism theorem at a key step. The [[Def - Group|group]]-theoretic precursor is [[Ex - Identifying a quotient with the first isomorphism theorem]], where the same template identifies $\mathrm{GL}_n / \mathrm{SL}_n \cong \mathbb{F}^\times$.
