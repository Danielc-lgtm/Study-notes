---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Group Action"
  - "Def - Coset"
  - "Def - Normal Subgroup"
  - "Def - Kernel and Image"
  - "Thm - Coset Action and the Normal Core"
  - "Thm - Orbit-Stabiliser Theorem"
  - "Thm - Lagrange's Theorem"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a finite group and let $H \leq G$ be a subgroup whose index $|G : H| = p$ is the **smallest prime** dividing $|G|$. Prove that $H$ is a normal subgroup of $G$, that is, $H \trianglelefteq G$.

**Recall:**

The objects in play are a subgroup of prime index, the action of $G$ on its cosets, and the divisibility consequences of that action.

A [[Def - Coset|left coset]] of $H$ is a set $gH = \{gh : h \in H\}$; the **index** $|G : H|$ is the number of distinct left cosets, and the set of left cosets is written $G/H$. Here $|G : H| = p$, so $G/H$ is a set of exactly $p$ elements.

![[Def - Normal Subgroup#The Definition]]

A [[Def - Normal Subgroup|normal subgroup]] $H \trianglelefteq G$ is a subgroup with $gHg^{-1} = H$ for every $g \in G$. One standard way a subgroup is certified normal is by being the **kernel of a homomorphism**: kernels are always normal.

![[Thm - Coset Action and the Normal Core#Statement]]

The [[Thm - Coset Action and the Normal Core|coset action]] is the action of $G$ on the set $G/H$ of left cosets by $g \cdot (xH) = gxH$. As an action on a $p$-element set it is a [[Def - Homomorphism|homomorphism]] $G \to S_p$, and its [[Def - Kernel and Image|kernel]] $K$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$ contained in $H$ — the **normal core** of $H$, the largest normal subgroup of $G$ inside $H$.

![[Thm - Orbit-Stabiliser Theorem#Statement]]

The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] gives $|G| = |G \cdot x|\,|G_x|$ for a finite group action; one of its consequences, [[Thm - Lagrange's Theorem|Lagrange's theorem]], is that the order of any subgroup divides the order of the group, and so does any index $|G : K| = |G|/|K|$.

---

# Convergent Strategy

**Problem class.** This is a *prove a subgroup is normal* problem in which no cheap structural reason is visible — the index is a prime $p$, but unless $p$ is the very smallest prime $2$ the index-two shortcut does not apply. It belongs to the second problem class of the [[Group Theory II — §1.3–1.4#Problem-Solving Strategy|topic page's strategy]]: a *subgroup of small index* is given, and the route is the [[Thm - Coset Action and the Normal Core|coset action]] into a small symmetric group.

**Assumption pattern.** Two hypotheses are present and both are essential. First, the index of $H$ is a prime $p$ — this bounds the size of the symmetric group the coset action lands in, since $G$ maps into $S_p$ and $|S_p| = p!$. Second, and this is the hypothesis that is easy to under-use, $p$ is the *smallest* prime dividing $|G|$ — which means every prime factor of $|G|$ is $\geq p$, so $|G|$ shares no factor with any integer built only from primes strictly below $p$. The combination of "index is prime" and "that prime is minimal" is the recognisable signature of this exercise.

**Theorem routing.** The route is: form the [[Thm - Coset Action and the Normal Core|coset action]] $G \to S_p$ with kernel $K$; by that theorem $K \trianglelefteq G$ and $K \leq H$. The goal becomes showing $K = H$, for then $H = K$ is a kernel and hence normal. To force $K = H$ we squeeze $|H : K|$ from two sides. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] embeds $G/K$ into $S_p$, so $|G : K|$ divides $p!$; writing $|G : K| = |G : H|\,|H : K| = p \cdot |H : K|$ shows $|H : K|$ divides $(p-1)!$. On the other side, $|H : K|$ divides $|G|$ by [[Thm - Lagrange's Theorem|Lagrange]]. So $|H : K|$ divides both $(p-1)!$ and $|G|$.

**Key decision point.** The crux is a number-theoretic observation that the minimality of $p$ unlocks: an integer dividing both $(p-1)!$ and $|G|$ must equal $1$. Every prime factor of $(p-1)!$ is a prime $< p$; every prime factor of $|G|$ is a prime $\geq p$, because $p$ is the *smallest* prime dividing $|G|$. A common divisor of the two can have no prime factors at all, so it is $1$. This is the step that fails without minimality — drop it and $H$ need not be normal — and recognising that "smallest prime dividing $|G|$" is precisely the hypothesis that makes $\gcd\big((p-1)!,\,|G|\big) = 1$ is the whole insight of the problem.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory II — §1.3–1.4#Legal Operations|the topic page's Legal Operations]]:

1. **Act on the cosets of a subgroup** (operation 4). Given $H \leq G$ of index $p$, we let $G$ act on the $p$-element set $G/H$ of left cosets. This is the operation that converts the bare datum "$H$ has index $p$" into a homomorphism with a usable kernel.

2. **Convert an action into a homomorphism and take its kernel** (operation 3). The coset action *is* a [[Def - Homomorphism|homomorphism]] $\rho : G \to S_p$. Its [[Def - Kernel and Image|kernel]] $K$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$, and — being the kernel of the coset action — it lies inside $H$. Producing a normal subgroup as a kernel is the move that makes the target reachable.

3. **Apply the orbit-stabiliser theorem, in the form of Lagrange's theorem** (operation 2). We use that indices multiply along a chain $K \leq H \leq G$, giving $|G : K| = |G : H| \cdot |H : K|$, and that $|H : K|$ divides $|G|$. Both are consequences of [[Thm - Lagrange's Theorem|Lagrange's theorem]], itself orbit-stabiliser for the regular action.

4. **Use the first isomorphism theorem to bound an order by a factorial** (a standing consequence of operation 3). Since $G/K$ embeds in $S_p$ via [[Thm - First Isomorphism Theorem|the first isomorphism theorem]], the order $|G : K| = |G/K|$ divides $|S_p| = p!$. This is the operation that injects the factorial $p!$ — and hence the primes below $p$ — into the argument.

---

# Hints

> [!note]- Hint 1
> The index is prime but not necessarily $2$, so the index-two argument is unavailable. The hypothesis is "small index", so reach for the standard small-index tool: let $G$ act on the set of left cosets $G/H$. What homomorphism does this produce, and into which group?

> [!note]- Hint 2
> The coset action gives $\rho : G \to S_p$ with kernel $K$. By the [[Thm - Coset Action and the Normal Core|normal core]] theorem, $K \trianglelefteq G$ and $K \leq H$. If you can show $K = H$, you are finished — why? So the target is now $|H : K| = 1$. Find two different integers that $|H : K|$ must divide.

> [!note]- Hint 3
> From $G/K \hookrightarrow S_p$, the index $|G : K|$ divides $p!$. Factor $|G : K| = |G : H| \cdot |H : K| = p \cdot |H : K|$, so $|H : K|$ divides $(p-1)!$. Separately, $|H : K|$ divides $|G|$ by Lagrange. Now use that $p$ is the *smallest* prime dividing $|G|$: what primes can divide $(p-1)!$, and what primes can divide $|G|$?

> [!note]- Hint 4
> Every prime factor of $(p-1)!$ is strictly less than $p$. Every prime factor of $|G|$ is at least $p$, because $p$ is the smallest prime dividing $|G|$. An integer dividing both can therefore have no prime factors — it is $1$. Hence $|H : K| = 1$, so $H = K$, and $K$ is a kernel, hence normal.

---

# Solution

The plan is to act on the $p$ cosets of $H$ to obtain a homomorphism $G \to S_p$ with kernel $K \leq H$, then prove $K = H$ by showing $|H : K|$ divides both $(p-1)!$ and $|G|$ — two numbers whose only common divisor is $1$ because $p$ is the smallest prime dividing $|G|$.

**Step 1: The coset action gives a homomorphism $\rho : G \to S_p$ with kernel $K$ satisfying $K \trianglelefteq G$ and $K \leq H$.**

Letting $G$ act on the $p$-element set $G/H$ of left cosets by $g \cdot (xH) = gxH$ produces a homomorphism $\rho : G \to S_p$. Its kernel $K = \ker\rho$ is a normal subgroup of $G$, and every element of $K$ lies in $H$, so $K \leq H$.

> [!note]- Derivation
> Define $g \cdot (xH) = gxH$. This is a well-defined [[Def - Group Action|action]]: if $xH = x'H$ then $x^{-1}x' \in H$, so $(gx)^{-1}(gx') = x^{-1}x' \in H$ and hence $gxH = gx'H$; the axioms $e \cdot (xH) = xH$ and $g_1 \cdot (g_2 \cdot xH) = (g_1g_2) \cdot xH$ are immediate. By [[Thm - Actions Correspond to Homomorphisms|the correspondence between actions and homomorphisms]], this action is a homomorphism $\rho : G \to \operatorname{Sym}(G/H)$, and since $|G/H| = |G : H| = p$ we identify $\operatorname{Sym}(G/H) \cong S_p$, so
> $$\rho : G \longrightarrow S_p.$$
>
> The [[Def - Kernel and Image|kernel]] $K = \ker\rho$ consists of the $g \in G$ acting trivially on every coset: $gxH = xH$ for all $x \in G$. As the [[Thm - Coset Action and the Normal Core|coset action theorem]] records, this kernel is the **normal core** $\bigcap_{x \in G} xHx^{-1}$, the largest normal subgroup of $G$ contained in $H$. Two facts from that description are all we need. First, $K \trianglelefteq G$, because the kernel of any homomorphism is a [[Def - Normal Subgroup|normal subgroup]]. Second, $K \leq H$: if $g \in K$ then in particular $g$ fixes the coset $eH = H$, so $gH = H$, which forces $g \in H$ (as $g = ge \in gH = H$). Thus
> $$K \trianglelefteq G \quad\text{and}\quad K \leq H.$$

**Step 2: $|H : K|$ divides $(p-1)!$.**

Because $G/K$ embeds in $S_p$, the index $|G : K|$ divides $p!$. Splitting that index along the chain $K \leq H \leq G$ as $|G : K| = p \cdot |H : K|$ and cancelling the factor $p$ shows $|H : K|$ divides $(p-1)!$.

> [!note]- Derivation
> By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied to $\rho$, the quotient $G/K = G/\ker\rho$ is isomorphic to $\operatorname{im}\rho$, a subgroup of $S_p$. By [[Thm - Lagrange's Theorem|Lagrange's theorem]], the order of a subgroup divides the order of the group, so
> $$|G : K| = |G/K| = |\operatorname{im}\rho| \ \big|\ |S_p| = p!.$$
>
> Indices are multiplicative along a chain of subgroups: for $K \leq H \leq G$,
> $$|G : K| = |G : H| \cdot |H : K|.$$
> (This is the tower law for indices, itself a counting consequence of [[Thm - Lagrange's Theorem|Lagrange]]: each coset of $H$ in $G$ splits into $|H : K|$ cosets of $K$.) Since $|G : H| = p$, this reads $|G : K| = p \cdot |H : K|$. Substituting into $|G : K| \mid p!$ gives
> $$p \cdot |H : K| \ \big|\ p! = p \cdot (p-1)!,$$
> and cancelling the common factor $p$ yields
> $$|H : K| \ \big|\ (p-1)!.$$

**Step 3: $|H : K|$ divides $|G|$.**

Since $K \leq H \leq G$ are finite groups, $|H : K| = |H|/|K|$ is an integer dividing $|H|$, and $|H|$ in turn divides $|G|$; hence $|H : K|$ divides $|G|$.

> [!note]- Derivation
> By [[Thm - Lagrange's Theorem|Lagrange's theorem]] applied to $K \leq H$, the index $|H : K| = |H|/|K|$ divides $|H|$. By Lagrange applied to $H \leq G$, the order $|H|$ divides $|G|$. Divisibility is transitive, so
> $$|H : K| \ \big|\ |H| \ \big|\ |G| \quad\Longrightarrow\quad |H : K| \ \big|\ |G|.$$

**Step 4: Conclude $|H : K| = 1$, hence $H = K \trianglelefteq G$.**

By Steps 2 and 3, the integer $|H : K|$ divides both $(p-1)!$ and $|G|$. Every prime factor of $(p-1)!$ is less than $p$, while every prime factor of $|G|$ is at least $p$ — because $p$ is the smallest prime dividing $|G|$. A common divisor of the two can have no prime factor, so $|H : K| = 1$. Then $H = K$, and since $K$ is a kernel it is normal: $H \trianglelefteq G$.

> [!note]- Derivation
> Let $d = |H : K|$. By Step 2, $d \mid (p-1)!$, and by Step 3, $d \mid |G|$.
>
> Consider any prime $q$ dividing $d$. Since $d \mid (p-1)!$, the prime $q$ divides $(p-1)! = 1 \cdot 2 \cdots (p-1)$, and a prime divides a product exactly when it divides one of the factors; each factor here is an integer in $\{1, \dots, p-1\}$, so $q \leq p - 1 < p$. Thus every prime factor of $d$ satisfies $q < p$.
>
> On the other hand, since $d \mid |G|$, any prime $q$ dividing $d$ also divides $|G|$. By hypothesis $p$ is the **smallest** prime dividing $|G|$, so every prime dividing $|G|$ — in particular $q$ — satisfies $q \geq p$.
>
> A prime $q$ dividing $d$ would therefore satisfy both $q < p$ and $q \geq p$, which is impossible. Hence $d$ has no prime factors at all, and the only positive integer with no prime factors is $1$:
> $$|H : K| = d = 1.$$
> Therefore $|H| = |K|$, and since $K \leq H$ this forces $H = K$. But $K = \ker\rho$ is the kernel of a homomorphism, hence a [[Def - Normal Subgroup|normal subgroup]] of $G$. Therefore
> $$H = K \trianglelefteq G. \qquad \blacksquare$$

> [!note]- Complete formal solution
> Let $G$ be finite and $H \leq G$ with $|G : H| = p$, the smallest prime dividing $|G|$.
>
> Let $G$ act on the set $G/H$ of left cosets by $g \cdot (xH) = gxH$. This action is well-defined and, since $|G/H| = p$, corresponds to a homomorphism $\rho : G \to S_p$. Let $K = \ker\rho$. As a kernel, $K \trianglelefteq G$; and $K \leq H$, since any $g \in K$ fixes the coset $H$, giving $g \in gH = H$.
>
> By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], $G/K \cong \operatorname{im}\rho \leq S_p$, so by [[Thm - Lagrange's Theorem|Lagrange's theorem]] $|G : K|$ divides $|S_p| = p!$. By the tower law for indices on $K \leq H \leq G$,
> $$|G : K| = |G : H| \cdot |H : K| = p \cdot |H : K|.$$
> Hence $p \cdot |H : K| \mid p!$, and cancelling $p$ gives $|H : K| \mid (p-1)!$.
>
> Separately, by Lagrange's theorem $|H : K| \mid |H|$ and $|H| \mid |G|$, so $|H : K| \mid |G|$.
>
> Thus $|H : K|$ divides both $(p-1)!$ and $|G|$. Any prime $q \mid |H : K|$ divides $(p-1)!$, hence equals one of $1, \dots, p-1$, so $q < p$; but $q$ also divides $|G|$, and $p$ is the smallest prime dividing $|G|$, so $q \geq p$. No prime can satisfy both, so $|H : K|$ has no prime factors and equals $1$.
>
> Therefore $H = K$, and since $K = \ker\rho$ is normal in $G$, we conclude $H \trianglelefteq G$. $\blacksquare$

> [!warning] The minimality of $p$ is indispensable
> Without "smallest prime", the result is false. In the alternating group $A_4$ of order $12$, take $H = \langle (1\,2\,3) \rangle$, a subgroup of order $3$ and index $4$. Here $4$ is the smallest *integer* exceeding $1$ that is an index, but it is not prime, and $A_4$ has the prime $2$ dividing its order with $2 < 3$. This $H$ is not normal in $A_4$ — it has four distinct conjugates. The argument above breaks at exactly Step 4: $|H : K| = |H : K|$ would need to divide $(p-1)!$ for $p$ the index, but the index is not the smallest prime, so there is no clash of prime ranges to force $|H : K| = 1$. The theorem is sharp: it is the *minimality* of the prime, not merely its primality, that does the work.

---

# Key Takeaways

**A subgroup of small index becomes a homomorphism into a small symmetric group — this is the universal first move when the index-two shortcut is unavailable.** Index two certifies normality almost for free, because two cosets leave no room for the left and right partitions to differ. For any larger index there is no such immediate argument, and the correct reflex is the [[Thm - Coset Action and the Normal Core|coset action]]: let $G$ act on the $n$ left cosets of $H$, obtaining a homomorphism $\rho : G \to S_n$ whose kernel $K$ is a normal subgroup sitting inside $H$. The trigger is any hypothesis of the form "$H$ has index $n$" with $n$ small relative to $|G|$. This single construction manufactures a normal subgroup out of an arbitrary subgroup, and it converts the qualitative datum "small index" into the quantitative constraint "$|G/K|$ divides $n!$" — a divisibility statement that can then be attacked with arithmetic. Whenever a problem gives a subgroup of small index and asks for normality, non-simplicity, or an embedding, this is where to start.

**Pin a subgroup between its normal core and itself, then collapse the gap by squeezing the index $|H : K|$ from two sides.** The structural skeleton of this proof is worth abstracting. The coset action gives $K \leq H$ with $K$ normal; if one can show $|H : K| = 1$, then $H = K$ inherits normality from $K$. To force $|H : K| = 1$ one finds *two independent divisibility constraints* on that index and shows they are jointly satisfiable only by $1$. Here one constraint comes from the symmetric group — $|H : K|$ divides $(p-1)!$ — and the other from Lagrange — $|H : K|$ divides $|G|$. The general pattern is: trap an unknown quantity between a lower object (the core $K$) and an upper object ($H$), express the gap as an index, and pile divisibility conditions on that index until only the trivial value survives. This "squeeze the index" technique recurs throughout finite group theory: it is the same shape of argument used to show groups of certain orders have normal Sylow subgroups, where the count $n_p$ of Sylow subgroups is trapped by the two constraints $n_p \equiv 1 \pmod p$ and $n_p \mid |G|$.

**"The smallest prime dividing $|G|$" is a coded instruction to make a number coprime to a factorial.** The hypothesis that $p$ is minimal looks like a mild technical condition, but it is the entire engine of the proof, and recognising what it *buys* is the transferable insight. Its content is a partition of the primes: every prime $< p$ is absent from $|G|$, and every prime dividing $|G|$ is $\geq p$. Consequently $|G|$ is coprime to $(p-1)!$, since $(p-1)!$ is built entirely from primes below $p$. Any time a hypothesis names "the smallest prime divisor", expect the proof to exploit exactly this coprimality — an integer constrained to divide both $|G|$ and something assembled from smaller primes is thereby forced to be $1$. The same idea, in the same words, proves that a group of order $2m$ with $m$ odd has a normal subgroup of order $m$, and that the smallest Sylow subgroup is often normal: in each case "smallest prime" is the lever that makes a factorial and a group order share no common factor.

**Being a kernel is the cleanest certificate of normality, so reduce "prove $H$ is normal" to "exhibit $H$ as a kernel".** The proof never conjugates a single element of $H$. Instead it identifies $H$ with $K = \ker\rho$, and kernels are normal by a one-line argument valid in every group. This illustrates a general hierarchy of ways to prove normality, from cheapest to most laborious: a subgroup is visibly normal if it is the whole group, the trivial subgroup, the centre, an intersection of normal subgroups, of index two, or — as here — the kernel of some homomorphism. Conjugating a general element is the method of last resort. The strategic lesson is that when asked to prove normality, one should hunt for a homomorphism whose kernel is the subgroup in question; constructing the *right* homomorphism (here, the coset action) is the creative work, after which normality is automatic. Recognising "prove normal" as a prompt to "find the homomorphism it is the kernel of" reorients the problem from a computation into a search for the right structural map.
