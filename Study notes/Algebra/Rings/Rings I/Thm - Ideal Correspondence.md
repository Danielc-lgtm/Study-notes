---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Subring"
  - "Def - Ring Homomorphism"
  - "Def - Ideal"
  - "Def - Quotient Ring"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is a [[Def - Ring|ring]] and $I \trianglelefteq R$ is an [[Def - Ideal|ideal]]. The [[Def - Quotient Ring|quotient ring]] $R/I$ has elements the cosets $r + I$, and $\pi : R \to R/I$, $\pi(r) = r + I$, is the canonical quotient map. We write $\trianglelefteq$ for "is an ideal of" and $\leq$ for "is a subring of". For a subset $A \subseteq R/I$, its **preimage** is $\pi^{-1}(A) = \{r \in R : r + I \in A\}$; for a subset $B \subseteq R$, its **image** is $\pi(B) = \{b + I : b \in B\}$. The phrase "the ideals of $R$ above $I$" means the ideals $J \trianglelefteq R$ with $I \subseteq J$. The map sending a subset to a corresponding subset is called **inclusion-preserving** (or **order-preserving**) if $A_1 \subseteq A_2$ implies the corresponding sets are nested the same way. The full symbol registry is on the parent page [[Rings I — §2.1–2.2]].

---

# Statement

> **Ideal Correspondence Theorem (correspondence / lattice-isomorphism theorem for rings).** Let $R$ be a ring and $I \trianglelefteq R$ an ideal, with canonical quotient map $\pi : R \to R/I$. Then the maps
> $$J \;\longmapsto\; J/I = \pi(J) \qquad\text{and}\qquad L \;\longmapsto\; \pi^{-1}(L) = \{r \in R : r + I \in L\}$$
> are mutually inverse, inclusion-preserving bijections
> $$\{\text{ideals of } R/I\} \;\xleftrightarrow{\;\;1:1\;\;}\; \{\text{ideals } J \text{ of } R \text{ with } I \subseteq J\}.$$
> The very same pair of maps restricts to an inclusion-preserving bijection
> $$\{\text{subrings of } R/I\} \;\xleftrightarrow{\;\;1:1\;\;}\; \{\text{subrings } S \text{ of } R \text{ with } I \subseteq S\}.$$

---

# Motivation

You have just learned to form the quotient ring $R/I$. The [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]] tells you, in good cases, what $R/I$ *is* as a ring. But a ring is more than its elements and operations — it carries an internal structure: its lattice of ideals and subrings. To genuinely understand $R/I$ you must know *its* ideals and subrings, not just its multiplication table. Finding them by brute force, hunting through subsets of cosets, is unpleasant. The correspondence theorem says you never have to: the substructure of $R/I$ is already visible inside $R$.

Here is the precise statement of relief. The ideals of $R/I$ are in flawless one-to-one correspondence with the ideals of $R$ that *contain $I$* — and the correspondence preserves inclusions, so it matches not just the ideals but the entire lattice, the whole pattern of which ideal sits inside which. The same holds for subrings. So to list the ideals of $R/I$, you do not look inside $R/I$ at all. You look at $R$, you find the ideals lying above $I$, and you read them off. Passing to a quotient does not create a mysterious new substructure; it simply *truncates* the substructure of $R$, discarding everything below $I$ and keeping everything above.

Why does the cutoff land exactly at $I$? Because $I$ is the new zero. An ideal of $R/I$, like any ideal, must contain the zero element — and the zero of $R/I$ is the coset $I$. Pulling that ideal back to $R$, it must contain everything that maps to zero, namely all of $I$. So $I$ is the floor: no ideal of $R$ corresponding to an ideal of the quotient can dip below it. Everything at or above $I$ survives the quotient; everything strictly below $I$ is crushed into the new zero and becomes invisible.

The reason this matters is a genuine difference in *temperament* between group quotients and ring quotients, and the source draws attention to it directly. In finite group theory, you usually take a quotient to get a *simpler* group — you mod out structure to make the object easier. In ring theory the move often runs the other way: **quotienting frequently produces a more interesting ring, not a simpler one.** The source's own example is decisive: $\mathbb{R}[X]$ is, frankly, a dull ring — an infinite, structureless polynomial ring — but $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$ is the complex numbers, one of the richest objects in mathematics. Because quotienting can manufacture interesting rings, it can also manufacture interesting *ideals*: the correspondence theorem lets you take a humdrum ideal of $R/I$ and pull it back to a possibly more illuminating ideal of $R$, or push an ideal of $R$ down to discover a new ideal of the quotient. It is the bookkeeping device that makes "build interesting rings by quotienting" into a controllable, repeatable technique.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a ring $R$ and an ideal $I$"; the quotient $R/I$ is then in play. The source question is: when should a problem make you reach for the correspondence?

The first disguised source is **any question that asks for the ideals, or the ideal lattice, of a quotient ring**. If you must enumerate the ideals of $R/I$, decide whether $R/I$ is a field or has zero divisors via its ideals, or count maximal ideals of $R/I$, the move is to translate the whole question upstairs: ideals of $R/I$ are ideals of $R$ above $I$. The non-obvious step is *recognising* that "ideals of a quotient" is a cue to leave the quotient entirely and work in $R$, where you presumably know the ideal structure. *Example problem:* find every ideal of $\mathbb{Z}/12\mathbb{Z}$ by listing the ideals of $\mathbb{Z}$ containing $12\mathbb{Z}$, namely $d\mathbb{Z}$ for $d \mid 12$.

The second disguised source is **a maximality or primality question about an ideal of a quotient, or a need to detect whether $R/I$ is a field or a domain**. Because the correspondence preserves inclusions, it sends maximal ideals to maximal ideals (relative to the floor $I$) and prime ideals to prime ideals. So "is $L$ a maximal ideal of $R/I$?" becomes "is $\pi^{-1}(L)$ a maximal ideal of $R$ containing $I$?". In particular $R/I$ is a field exactly when $I$ itself is maximal — there are no ideals strictly between $I$ and $R$. The non-obvious step is converting an internal property of $R/I$ into a position-in-the-lattice property checkable in $R$. *Example problem:* prove $\mathbb{Z}/p\mathbb{Z}$ is a field by noting $p\mathbb{Z}$ is a maximal ideal of $\mathbb{Z}$.

The third disguised source is **an iterated quotient, where you must name the outer ideal**. When a problem forms $(R/I)/L$, the correspondence is what tells you $L = J/I$ for a *unique* ideal $J$ of $R$ above $I$ — and this is exactly the input the [[Thm - Third Isomorphism Theorem for Rings|third isomorphism theorem]] needs. The non-obvious recognition is that a double quotient cannot be simplified until its outer ideal is pulled back through the correspondence to a genuine ideal of $R$. *Example problem:* simplify $(\mathbb{Z}/12\mathbb{Z})/L$ by first writing $L = J/12\mathbb{Z}$ for the appropriate $J \supseteq 12\mathbb{Z}$, then cancelling.

**Targets (Output Amplification)**

The bare conclusion is an inclusion-preserving bijection of two families of ideals. Combined with other facts it does much more.

Combine the conclusion with **the third isomorphism theorem**. The correspondence names the outer ideal of a double quotient as $J/I$; the [[Thm - Third Isomorphism Theorem for Rings|third isomorphism theorem]] then evaluates $(R/I)/(J/I) \cong R/J$. The further result $E$ is a complete catalogue of *all quotients of $R/I$*: they are exactly the rings $R/J$ for ideals $J \supseteq I$. This is non-obvious and strong — it says that passing to $R/I$ does not generate exotic quotients; the quotients of $R/I$ are precisely those quotients of $R$ that already kill $I$.

Combine the conclusion with **the order-preservation, applied to chains and maximal elements**. Because the bijection respects inclusion in both directions, it carries chains of ideals to chains, and *maximal* ideals of $R/I$ to maximal ideals of $R$ that contain $I$. The further result is a foothold on dimension and on factorisation: the length of the longest chain of prime ideals (the Krull dimension) of $R/I$ equals the length of the longest chain of primes of $R$ between $I$ and $R$. Detecting that $R/I$ has Krull dimension zero, or is a field, becomes a statement about how high $I$ sits in the prime lattice of $R$. This is non-obvious because a numerical invariant of the quotient is being computed entirely from the position of one ideal in $R$.

Combine the conclusion with **the subring half of the correspondence and the first isomorphism theorem**. The same bijection matches subrings of $R/I$ with subrings of $R$ above $I$. Given a subring $S$ of $R$ with $I \subseteq S$, the corresponding subring of $R/I$ is $S/I$, and applying the first isomorphism theorem to $S \to S/I$ identifies it. The further result $E$ is that the entire subring structure of $R/I$ — not just the ideal structure — is read off from $R$, which is what you need to understand, say, the prime subfield or the centre of a quotient. This is non-obvious because the subring and ideal correspondences are governed by *one* pair of maps, so a single computation in $R$ delivers both lattices of the quotient.

---

# Why Is It True

Forget cosets and picture the canonical quotient map $\pi : R \to R/I$ as a *projection* that staples together everything in each $I$-coset. The correspondence theorem is the statement that this projection sets up a perfect dictionary between substructures of $R$ that are "saturated" — that respect the stapling — and all substructures of $R/I$.

Start with the easy direction. Take any ideal $L$ of $R/I$ and pull it back: $\pi^{-1}(L) = \{r \in R : r + I \in L\}$. The preimage of an ideal under a ring homomorphism is always an ideal — this is a one-line check, because $\pi$ respects $+$ and $\times$, so a condition like "$r + I \in L$" that is closed under the operations of $R/I$ pulls back to a condition closed under the operations of $R$. And $\pi^{-1}(L)$ automatically contains $I$: every element of $I$ maps to the zero coset, the zero coset lies in the ideal $L$, so every element of $I$ lies in $\pi^{-1}(L)$. So pulling back lands you in exactly the right target — ideals of $R$ above $I$.

Now the other direction. Take an ideal $J$ of $R$ with $I \subseteq J$ and push it forward: $\pi(J) = \{j + I : j \in J\}$, which we write $J/I$. Because $\pi$ is *surjective*, the image of an ideal is again an ideal — surjectivity is what lets you absorb multiplication by an arbitrary element of $R/I$, since that element is $\pi(\text{something})$. So $J/I$ is an ideal of $R/I$.

Why are these two maps mutually inverse? Here is the whole crux, and it is a single sentence: pushing forward and then pulling back recovers $J$ *precisely because $J$ already contains $I$*. In general $\pi^{-1}(\pi(J))$ is not $J$ — it is $J$ enlarged by everything in the same $I$-coset as a point of $J$, that is, $J + I$. But if $I \subseteq J$, then $J + I = J$: enlarging $J$ by $I$ does nothing, because $I$ was inside $J$ all along. This is the *entire reason* the correspondence is restricted to ideals above $I$. Drop the containment, and pushing-then-pulling inflates an ideal to $J + I$ and the maps stop being inverse; the family of ideals above $I$ is exactly the family that is immune to this inflation. The reverse composite, pulling back then pushing forward, recovers $L$ because $\pi$ is *onto*: $\pi(\pi^{-1}(L)) = L$ holds for any subset of a surjection's codomain. So the two maps invert each other, and a pair of mutually inverse maps is a bijection.

Inclusion is preserved because both $\pi$ and $\pi^{-1}$ are monotone as set operations — a bigger set has a bigger image and a bigger preimage. And the subring version needs no new idea at all: every place the argument said "ideal" it could have said "subring", because preimages of subrings are subrings, surjective images of subrings are subrings, and the $J + I = J$ collapse used only that $I$ sits inside the structure. One pair of maps, one argument, both lattices. The deep content is small and crisp: a quotient map is a bijection between *its-own-fibres-respecting* substructures of the domain and *all* substructures of the codomain, and "contains $I$" is the precise spelling of "respects the fibres".

---

# What Makes This Hard

The two maps and their basic properties are routine; the entire subtlety is the round-trip identity $\pi^{-1}(\pi(J)) = J$, which holds *only* because $I \subseteq J$ — for a general ideal $J$ the composite returns the inflated $J + I$, and missing this is why the correspondence must be restricted to ideals containing $I$. The non-obvious step is therefore not constructing the bijection but *justifying its domain*: recognising that "ideals above $I$" is forced, not a stylistic choice. The most common error is to forget the floor entirely and claim a bijection with *all* ideals of $R$, or to verify only one composite ($\pi\pi^{-1} = \mathrm{id}$, which is just surjectivity) and overlook that the other composite is the one that genuinely needs the containment hypothesis.

---

# Rederivation Scaffold

**High-level strategy:**
Exhibit the two maps — push forward $J \mapsto \pi(J)$ and pull back $L \mapsto \pi^{-1}(L)$ — and prove four things: each lands in the correct family, the two composites are both the identity (this is where $I \subseteq J$ is used), and both maps preserve inclusion. Then observe the argument never used that the substructures were ideals rather than subrings, giving the subring version for free.

**Subgoal decomposition:**

1. **Pull-back is well-targeted.** For an ideal $L \trianglelefteq R/I$, show $\pi^{-1}(L)$ is an ideal of $R$ containing $I$.
   - *Hint:* Preimage of an ideal under a ring homomorphism is an ideal; and $I = \pi^{-1}(\{0_{R/I}\}) \subseteq \pi^{-1}(L)$ since $0_{R/I} \in L$.
   - *Why needed:* It shows the map $L \mapsto \pi^{-1}(L)$ actually lands in "ideals of $R$ above $I$".

2. **Push-forward is well-targeted.** For an ideal $J \trianglelefteq R$ with $I \subseteq J$, show $\pi(J) = J/I$ is an ideal of $R/I$.
   - *Hint:* Image of an ideal under a *surjective* ring homomorphism is an ideal; surjectivity is what lets $J/I$ absorb multiplication by all of $R/I$.
   - *Why needed:* It shows $J \mapsto \pi(J)$ lands in "ideals of $R/I$".

3. **Round trip from $R$ recovers $J$.** Show $\pi^{-1}(\pi(J)) = J$ for $I \subseteq J$.
   - *Hint:* In general $\pi^{-1}(\pi(J)) = J + I$; the hypothesis $I \subseteq J$ collapses $J + I$ to $J$. This is the one place the containment is essential.
   - *Why needed:* It is half of "the two maps are mutually inverse".

4. **Round trip from $R/I$ recovers $L$.** Show $\pi(\pi^{-1}(L)) = L$.
   - *Hint:* $\pi$ is surjective, and $\pi(\pi^{-1}(L)) = L$ holds for any subset of the codomain of a surjection.
   - *Why needed:* It is the other half of "mutually inverse"; together with step 3 it makes the maps a bijection.

5. **Inclusion is preserved, and repeat for subrings.** Show both maps are monotone, then note the whole argument is unchanged with "subring" for "ideal".
   - *Hint:* Images and preimages of nested sets stay nested; preimages of subrings are subrings, surjective images of subrings are subrings, and $J + I = J$ used only $I \subseteq J$.
   - *Why needed:* Monotonicity upgrades the bijection to a lattice isomorphism, and the final observation delivers the subring correspondence with no extra work.

---

# Lemma Decomposition

> [!note]- Lemma 1: Preimages of ideals and subrings are ideals and subrings, and contain the kernel
> **Statement:** Let $\varphi : R \to T$ be a ring homomorphism. If $L \trianglelefteq T$ is an ideal then $\varphi^{-1}(L) \trianglelefteq R$ is an ideal; if $L \leq T$ is a subring then $\varphi^{-1}(L) \leq R$ is a subring. In both cases $\ker\varphi \subseteq \varphi^{-1}(L)$.
>
> **Hint:** A condition closed under the operations of $T$ pulls back, through a homomorphism, to a condition closed under the operations of $R$. For the kernel, note $0_T$ lies in every ideal and every subring of $T$.
>
> **Why needed:** It is the pull-back direction of the correspondence: it shows $\pi^{-1}(L)$ is an ideal (resp. subring) and that it automatically contains $I = \ker\pi$.
>
> > [!note]- Full proof
> > **Ideal case.** Let $L \trianglelefteq T$. The set $\varphi^{-1}(L)$ is an additive subgroup of $R$: if $a, b \in \varphi^{-1}(L)$ then $\varphi(a), \varphi(b) \in L$, so $\varphi(a - b) = \varphi(a) - \varphi(b) \in L$ (an ideal is closed under subtraction), giving $a - b \in \varphi^{-1}(L)$. For strong closure, let $a \in \varphi^{-1}(L)$ and $r \in R$. Then $\varphi(ar) = \varphi(a)\varphi(r)$; since $\varphi(a) \in L$ and $L$ absorbs multiplication by the arbitrary element $\varphi(r) \in T$, we get $\varphi(ar) \in L$, so $ar \in \varphi^{-1}(L)$. Likewise $ra \in \varphi^{-1}(L)$. Hence $\varphi^{-1}(L) \trianglelefteq R$.
> >
> > **Subring case.** Let $L \leq T$. Then $0_R, 1_R \in \varphi^{-1}(L)$ because $\varphi(0_R) = 0_T \in L$ and $\varphi(1_R) = 1_T \in L$ (a subring contains the ambient zero and one). Closure under $+$, $-$, $\times$ follows exactly as above, using that $L$ is closed under $+$, $-$, $\times$ by its own elements. Hence $\varphi^{-1}(L) \leq R$.
> >
> > **Kernel containment.** For any $x \in \ker\varphi$, $\varphi(x) = 0_T$. Since $0_T$ lies in every ideal of $T$ and in every subring of $T$, $\varphi(x) \in L$, so $x \in \varphi^{-1}(L)$. Hence $\ker\varphi \subseteq \varphi^{-1}(L)$.

> [!note]- Lemma 2: Surjective images of ideals and subrings are ideals and subrings
> **Statement:** Let $\varphi : R \to T$ be a *surjective* ring homomorphism. If $J \trianglelefteq R$ is an ideal then $\varphi(J) \trianglelefteq T$ is an ideal; if $S \leq R$ is a subring then $\varphi(S) \leq T$ is a subring.
>
> **Hint:** To absorb multiplication by an arbitrary $t \in T$, write $t = \varphi(r)$ using surjectivity — this is the one place surjectivity is essential.
>
> **Why needed:** It is the push-forward direction: it shows $\pi(J) = J/I$ is an ideal (resp. subring) of $R/I$.
>
> > [!note]- Full proof
> > **Ideal case.** Let $J \trianglelefteq R$. The image $\varphi(J)$ is an additive subgroup of $T$: for $\varphi(a), \varphi(b) \in \varphi(J)$ with $a, b \in J$, we have $\varphi(a) - \varphi(b) = \varphi(a - b) \in \varphi(J)$ since $a - b \in J$. For strong closure, take $\varphi(a) \in \varphi(J)$ with $a \in J$, and an *arbitrary* $t \in T$. Because $\varphi$ is surjective, $t = \varphi(r)$ for some $r \in R$. Then $t \cdot \varphi(a) = \varphi(r)\varphi(a) = \varphi(ra)$, and $ra \in J$ since $J$ is an ideal of $R$; so $t\varphi(a) \in \varphi(J)$. Similarly $\varphi(a) t \in \varphi(J)$. Hence $\varphi(J) \trianglelefteq T$. (Surjectivity was used precisely to realise the arbitrary $t$ as $\varphi(r)$ — without it, $\varphi(J)$ would only absorb multiplication by elements of $\operatorname{im}\varphi$.)
> >
> > **Subring case.** Let $S \leq R$. Then $0_T = \varphi(0_R) \in \varphi(S)$ and $1_T = \varphi(1_R) \in \varphi(S)$, and closure under $+$, $-$, $\times$ holds because the corresponding operations on preimages stay inside $S$. Hence $\varphi(S) \leq T$. (Here surjectivity is not needed: a subring need only be closed under its *own* elements.)

> [!note]- Lemma 3: The two composites are the identity — the round-trip identities
> **Statement:** Let $\pi : R \to R/I$ be the canonical quotient map. For any ideal (or subring) $J$ of $R$ with $I \subseteq J$, $\;\pi^{-1}(\pi(J)) = J$. For any subset $L \subseteq R/I$, $\;\pi(\pi^{-1}(L)) = L$.
>
> **Hint:** In general $\pi^{-1}(\pi(J)) = J + I$; the hypothesis $I \subseteq J$ makes $J + I = J$. The second identity is pure surjectivity.
>
> **Why needed:** Together these two identities say the push-forward and pull-back maps are mutually inverse — which is exactly what makes the correspondence a bijection, and which pinpoints why "$I \subseteq J$" cannot be dropped.
>
> > [!note]- Full proof
> > **First identity, $\pi^{-1}(\pi(J)) = J$ when $I \subseteq J$.**
> >
> > ($\supseteq$) If $x \in J$ then $\pi(x) \in \pi(J)$, so $x \in \pi^{-1}(\pi(J))$. (This holds for any $J$.)
> >
> > ($\subseteq$) Let $x \in \pi^{-1}(\pi(J))$, so $\pi(x) \in \pi(J)$, meaning $x + I = j + I$ for some $j \in J$. Then $x - j \in I$, so $x = j + (x - j)$ with $j \in J$ and $x - j \in I$. Now invoke the hypothesis: since $I \subseteq J$, the element $x - j$ lies in $J$, and $J$ is closed under addition, so $x = j + (x - j) \in J$.
> >
> > Hence $\pi^{-1}(\pi(J)) = J$. The containment $I \subseteq J$ was used in the ($\subseteq$) direction and *only* there: without it, $x - j \in I$ need not lie in $J$, and one obtains only $\pi^{-1}(\pi(J)) = J + I$.
> >
> > **Second identity, $\pi(\pi^{-1}(L)) = L$.**
> >
> > ($\subseteq$) If $y \in \pi(\pi^{-1}(L))$ then $y = \pi(x)$ for some $x \in \pi^{-1}(L)$, and $x \in \pi^{-1}(L)$ means exactly $\pi(x) \in L$, so $y \in L$. (This holds for any map.)
> >
> > ($\supseteq$) Let $y \in L \subseteq R/I$. Because $\pi$ is surjective, $y = \pi(x)$ for some $x \in R$. Then $\pi(x) = y \in L$, so $x \in \pi^{-1}(L)$, whence $y = \pi(x) \in \pi(\pi^{-1}(L))$.
> >
> > Hence $\pi(\pi^{-1}(L)) = L$, using surjectivity of $\pi$ in the ($\supseteq$) direction.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be a ring, $I \trianglelefteq R$ an ideal, and $\pi : R \to R/I$ the canonical quotient map, $\pi(r) = r + I$. Recall $\pi$ is a surjective ring homomorphism with $\ker\pi = I$. Define
> $$\Theta : \{\text{ideals of } R/I\} \to \{\text{ideals of } R \text{ above } I\}, \qquad \Theta(L) = \pi^{-1}(L),$$
> $$\Xi : \{\text{ideals of } R \text{ above } I\} \to \{\text{ideals of } R/I\}, \qquad \Xi(J) = \pi(J) = J/I.$$
>
> **Step 1 — $\Theta$ is well-defined.** Let $L \trianglelefteq R/I$. By Lemma 1, $\pi^{-1}(L)$ is an ideal of $R$, and since $\ker\pi = I$, Lemma 1 also gives $I = \ker\pi \subseteq \pi^{-1}(L)$. So $\Theta(L)$ is an ideal of $R$ containing $I$, as required.
>
> **Step 2 — $\Xi$ is well-defined.** Let $J \trianglelefteq R$ with $I \subseteq J$. Since $\pi$ is surjective, Lemma 2 gives that $\pi(J) = J/I$ is an ideal of $R/I$. So $\Xi(J)$ is an ideal of $R/I$, as required.
>
> **Step 3 — $\Theta$ and $\Xi$ are mutually inverse.** Let $J$ be an ideal of $R$ with $I \subseteq J$. By Lemma 3, since $I \subseteq J$,
> $$\Theta(\Xi(J)) = \pi^{-1}(\pi(J)) = J.$$
> Let $L$ be an ideal of $R/I$. By Lemma 3, using surjectivity of $\pi$,
> $$\Xi(\Theta(L)) = \pi(\pi^{-1}(L)) = L.$$
> Hence $\Theta \circ \Xi = \mathrm{id}$ and $\Xi \circ \Theta = \mathrm{id}$, so $\Theta$ and $\Xi$ are mutually inverse bijections between $\{\text{ideals of } R/I\}$ and $\{\text{ideals of } R \text{ above } I\}$.
>
> **Step 4 — the bijection preserves inclusion.** Both $\pi(\cdot)$ and $\pi^{-1}(\cdot)$ are monotone operations on subsets: if $A_1 \subseteq A_2$ then $\pi(A_1) \subseteq \pi(A_2)$ and $\pi^{-1}(A_1) \subseteq \pi^{-1}(A_2)$, directly from the definitions of image and preimage. Hence $\Theta$ and $\Xi$ both preserve inclusion, so the bijection is an isomorphism of the two inclusion-ordered lattices: $J_1 \subseteq J_2$ if and only if $J_1/I \subseteq J_2/I$.
>
> **Step 5 — the subring version.** Inspect Steps 1–4 with "subring" in place of "ideal" throughout. Lemma 1 also asserts that preimages of subrings are subrings (and still contain $\ker\pi = I$), so Step 1 holds for subrings. Lemma 2 also asserts that surjective images of subrings are subrings, so Step 2 holds for subrings. The round-trip identity $\pi^{-1}(\pi(S)) = S$ in Lemma 3 used only that $I \subseteq S$ and that $S$ is closed under addition — both true for a subring containing $I$ — and $\pi(\pi^{-1}(L)) = L$ used only surjectivity; so Step 3 holds for subrings. Step 4 used nothing about the substructure type. Therefore $\Theta$ and $\Xi$ also restrict to mutually inverse, inclusion-preserving bijections
> $$\{\text{subrings of } R/I\} \;\xleftrightarrow{\;1:1\;}\; \{\text{subrings of } R \text{ above } I\}. \qquad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Reading off the ideals of $\mathbb{Z}/n\mathbb{Z}$.** Apply the correspondence with $R = \mathbb{Z}$ and $I = n\mathbb{Z}$. The ideals of $\mathbb{Z}$ above $n\mathbb{Z}$ are exactly the $d\mathbb{Z}$ with $n\mathbb{Z} \subseteq d\mathbb{Z}$, i.e. with $d \mid n$. So the ideals of $\mathbb{Z}/n\mathbb{Z}$ correspond one-to-one with the *divisors of $n$*, and the inclusion order matches divisibility. The application is non-obvious because the ideal lattice of the quotient ring $\mathbb{Z}/n\mathbb{Z}$ — a finite ring whose subsets one might be tempted to search by hand — is instantly identified with the divisor lattice of $n$, a purely number-theoretic object; the source property is "$R/I$ with $R = \mathbb{Z}$".

**Maximal ideals and the geometry of a quotient.** For a polynomial ring $k[X_1,\dots,X_n]$ and an ideal $I$, the maximal ideals of the quotient $k[X_1,\dots,X_n]/I$ correspond — via the order-preserving correspondence — to the maximal ideals of $k[X_1,\dots,X_n]$ that contain $I$. Geometrically, maximal ideals of the polynomial ring are points of affine space, and those containing $I$ are the points lying on the variety cut out by $I$. So the correspondence theorem says the points of the variety are the maximal ideals of its coordinate ring. This is an out-of-distribution use because a purely algebraic lattice statement is delivering the foundational dictionary of algebraic geometry; the non-obvious recognition is that "maximal ideal of a quotient" means "point of a variety".

**Pulling back to find an interesting ideal.** The source stresses that ring quotients often produce more interesting objects. Suppose $R/I$ is a familiar ring with a known interesting ideal $L$ — say $R/I \cong \mathbb{C}$, or a product ring with an obvious factor ideal. The correspondence pulls $L$ back to an ideal $\pi^{-1}(L)$ of $R$ that you might not have spotted directly. For instance, the two factor ideals of $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ pull back to $2\mathbb{Z}$ and $3\mathbb{Z}$ in $\mathbb{Z}$. The application is non-obvious because it runs the correspondence *backwards* — using a transparent quotient to discover structure in the original ring — which is precisely the "occasionally get interesting ideals from less interesting ones" move the source describes.

**Subrings of a quotient via the subring half.** Let $R = \mathbb{R}[X]$ and $I = (X^2 + 1)$, so $R/I \cong \mathbb{C}$. The subring correspondence matches subrings of $\mathbb{C}$ with subrings of $\mathbb{R}[X]$ containing $(X^2+1)$. The prime subfield $\mathbb{Q} \le \mathbb{C}$, or the subring $\mathbb{R} \le \mathbb{C}$, thus corresponds to an explicit subring of $\mathbb{R}[X]$ lying above $(X^2+1)$. This is an out-of-distribution application because one usually thinks of the correspondence only for ideals, yet the *same theorem* organises the subring lattice of the quotient; the non-obvious step is realising the subring half is not a separate result but the identical pair of maps.

---

# Bridges

- **[[Thm - Third Isomorphism Theorem for Rings|Third Isomorphism Theorem for Rings]]** — the indispensable partner. The correspondence *names* the outer ideal of a double quotient as $J/I$ for a unique ideal $J \supseteq I$; the third isomorphism theorem then *evaluates* $(R/I)/(J/I) \cong R/J$. Read together they give a complete catalogue: the quotients of $R/I$ are exactly the rings $R/J$ for ideals $J$ above $I$.

- **[[Thm - First Isomorphism Theorem for Rings|First Isomorphism Theorem for Rings]]** — the companion that identifies. Where the correspondence describes the *lattice* of ideals and subrings of $R/I$, the first isomorphism theorem identifies the quotient ring $R/I$ itself, and identifies each corresponding subring $S/I$ via the map $S \to S/I$. One gives the substructure, the other the structure.

- **[[Thm - Second Isomorphism Theorem for Rings|Second Isomorphism Theorem for Rings]]** — a sibling in the bookkeeping toolkit. All three of the second, third, and correspondence theorems are about controlling how substructures behave under quotients; the correspondence is the one that handles the *lattice*, and it is what makes chained applications of the other two coherent.

- **Correspondence theorem for groups** — the exact prototype. The group statement — subgroups of $G/N$ correspond to subgroups of $G$ above $N$, and normal subgroups to normal subgroups — becomes the ring statement by replacing "subgroup" with "subring" and "normal subgroup" with "ideal". The proof, via the canonical projection and the identity $\pi^{-1}(\pi(J)) = J$ for $J$ above the kernel, is identical; the source notes the formula is "exactly the same as for groups".

- **Lattice isomorphism / Galois connection** — the abstract frame. The pair $(\pi(\cdot), \pi^{-1}(\cdot))$ is a Galois connection between the subset lattices of $R$ and $R/I$, and the correspondence theorem is the statement that it restricts to an honest *lattice isomorphism* on the closed elements — the substructures above $I$. This is the same shape of result as the fundamental theorem of Galois theory, which pairs intermediate fields with subgroups.

---

# Unlocked by This

> [!tip] Coordinate Rings and Points of a Variety *(from Algebraic Geometry)*
> The correspondence sends maximal ideals of a quotient $k[X_1,\dots,X_n]/I$ to maximal ideals of the polynomial ring containing $I$ — geometrically, to the points of the variety defined by $I$. This is the foundational dictionary between rings and geometry.

> [!tip] Catalogue of All Quotients of a Quotient *(from Commutative Algebra)*
> Combined with the third isomorphism theorem, the correspondence shows the quotients of $R/I$ are exactly the rings $R/J$ for ideals $J \supseteq I$ — so the quotient theory of $R/I$ is fully contained in that of $R$.
