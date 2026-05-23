---
type: theorem
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Coset"
  - "Def - Order of a Group and of an Element"
tags: [algebra, group-theory]
---

# Notation

$G$ is a finite group with identity $e$. $H \leq G$ means $H$ is a [[Def - Subgroup|subgroup]] of $G$. For $g \in G$, the **left coset** $gH = \{gh : h \in H\}$ is the translate of $H$ by $g$ (see [[Def - Coset]]). The **order** $|G|$ is the number of elements of $G$, and $|G : H|$ — the **index** — is the number of distinct left cosets of $H$. For an element $g$, $\operatorname{ord}(g)$ is the least $n > 0$ with $g^n = e$, and $\langle g \rangle = \{e, g, g^2, \dots\}$ is the cyclic subgroup it generates (see [[Def - Order of a Group and of an Element]]). The full notation registry lives on the parent page [[Group Theory I — §1.1–1.2]].

---

# Statement

> **Lagrange's Theorem.** Let $G$ be a finite group and let $H \leq G$ be a [[Def - Subgroup|subgroup]]. Then
> $$|G| = |H| \cdot |G : H|,$$
> where $|G : H|$ is the number of left [[Def - Coset|cosets]] of $H$ in $G$. In particular, $|H|$ divides $|G|$.

> **Corollary (order of an element).** If $G$ is a finite group and $g \in G$, then $\operatorname{ord}(g)$ divides $|G|$, and consequently $g^{|G|} = e$.

The corollary follows because $\operatorname{ord}(g)$ equals the order of the cyclic subgroup $\langle g \rangle \leq G$, and Lagrange's theorem applied to $H = \langle g \rangle$ forces $|\langle g \rangle|$ to divide $|G|$.

---

# Motivation

A finite group is, in the end, just a finite set with a multiplication table, and the first question one asks of any finite object is: how big are its parts compared to the whole? Before Lagrange, there is no reason to expect any relationship at all between $|G|$ and the size of a subgroup $H$. A subgroup is a subset closed under multiplication and inverses; a priori its cardinality could be anything from $1$ to $|G|$. Lagrange's theorem says no — the size of a subgroup is not free. It must divide the order of the group.

This is the first genuine theorem of finite group theory, and it earns that status because it converts a single integer, $|G|$, into a hard combinatorial constraint on the entire internal structure of $G$. Once you know $|G| = 12$, you know instantly that every subgroup has order $1$, $2$, $3$, $4$, $6$, or $12$ — orders $5$, $7$, $8$, $9$, $10$, $11$ are impossible, and you have done no work to rule them out. The same constraint, via the corollary, pins down the order of every individual element. A group of order $7$ has nothing but the identity and elements of order $7$; there is simply no room for anything else.

The theorem matters most for what it forbids. Almost every classification result in the next two topics — that [[Def - Group|groups]] of prime order are cyclic, that [[Def - Group|groups]] of order $pq$ have a normal subgroup, the entire Sylow theory — begins by writing down the divisors of $|G|$ and using Lagrange to eliminate the impossible. It is the filter through which every structural argument about finite groups is poured.

---

# Sources and Targets

This section is not an input/output summary. It records the non-obvious ways a problem can arrive at the hypothesis of Lagrange's theorem (sources), and the non-obvious results that follow once you combine its conclusion with one more fact (targets). Both are distilled from the exercises that actually use the theorem.

**Sources (Input Broadening)**

The hypothesis Lagrange needs is bare: *a subgroup of a finite group*. The skill is recognizing, in a problem that mentions no subgroup at all, that a subgroup is secretly present. Each of the following is a property $B$ of a problem from which a subgroup — and hence a divisibility fact — can be extracted.

The most common source is **a single element of known or unknown order**. Property $B$ here is just "$G$ contains an element $g$", and the bridge is that $g$ generates the cyclic subgroup $\langle g \rangle$, whose order is exactly $\operatorname{ord}(g)$. The implication "$g$ exists $\implies$ a subgroup of order $\operatorname{ord}(g)$ exists" is non-obvious only because beginners forget that *every* element silently carries a subgroup with it. This is the source behind [[Ex - Order of an element divides the group order]]: the problem hands you an element and asks for a divisibility fact, and the cyclic subgroup is the missing link. A sharper instance: in any group of order $15$, an element of order $4$ is impossible, because $4 \nmid 15$ — the element alone, through its cyclic subgroup, is already constrained.

A second source is **a homomorphism out of $G$**. Property $B$ is "there is a homomorphism $\varphi : G \to K$", and the bridge is that the [[Def - Kernel and Image|kernel]] $\ker\varphi$ is a subgroup of $G$ while the image $\operatorname{im}\varphi$ is a subgroup of $K$. The implication is non-obvious because a homomorphism does not look like a subgroup, yet it produces two of them at once, on both sides. This is what lets Lagrange forbid homomorphisms: if $|G| = 10$ and $|K| = 21$, there is no injective homomorphism $G \to K$, because an injective homomorphism would embed a subgroup of order $10$ into $K$, and $10 \nmid 21$. The source converts a question about maps into a question about divisibility.

A third source is **a group action on a finite set**. Property $B$ is "$G$ acts on a set $X$", and the bridge is that the stabiliser $G_x = \{g : g \cdot x = x\}$ of any point $x$ is a subgroup of $G$. The implication is non-obvious until one checks that stabilisers are closed under multiplication and inverses. The orbit–stabiliser theorem then reads $|G| = |G_x| \cdot |G \cdot x|$, which is Lagrange applied to $H = G_x$, with the cosets of $G_x$ identified with the orbit. So every counting argument about symmetries — colourings of a cube, necklaces — routes through Lagrange via a stabiliser subgroup.

A fourth source is **an intersection of two subgroups**. Property $B$ is "$H$ and $K$ are both subgroups of $G$", and the bridge is that $H \cap K$ is a subgroup of $G$, so $|H \cap K|$ divides $|G|$ — but more usefully it divides both $|H|$ and $|K|$, since $H \cap K \leq H$ and $H \cap K \leq K$. The non-obvious payoff is the next paragraph's target: when $\gcd(|H|, |K|) = 1$ the intersection collapses to the identity. This is the source behind one half of [[Ex - The product HK and the second isomorphism theorem]].

**Targets (Output Amplification)**

The conclusion Lagrange delivers is "$|H|$ divides $|G|$" together with the exact equation $|G| = |H| \cdot |G:H|$. On its own this is a constraint; combined with one further property $D$ it becomes a positive structural result $E$.

The most powerful combination is **divisibility plus coprimality forces a trivial intersection**. Suppose $H, K \leq G$ and you have, by Lagrange, that $|H \cap K|$ divides both $|H|$ and $|K|$ (property $C$). Add the property $D$ that $\gcd(|H|, |K|) = 1$. Then $|H \cap K|$ divides $\gcd(|H|, |K|) = 1$, so $H \cap K = \{e\}$. The non-obvious result $E$ is that two subgroups of coprime order meet only in the identity — a fact you would never guess from the definitions, since nothing about coprime *sizes* obviously prevents shared elements. This is the workhorse behind direct-product decompositions: when $|H||K| = |G|$ and $\gcd(|H|,|K|)=1$ with both normal, the trivial intersection upgrades to $G \cong H \times K$.

A second combination is **divisibility plus a prime order forces cyclicity**. Take the conclusion $|H|$ divides $|G|$ in the special case $H = \langle g \rangle$, so $\operatorname{ord}(g) \mid |G|$ (property $C$). Add the property $D$ that $|G| = p$ is prime. Then $\operatorname{ord}(g)$, a divisor of $p$, is either $1$ or $p$; for $g \neq e$ it must be $p$, so $g$ generates all of $G$. The result $E$ is that every group of prime order is cyclic — see [[Ex - Groups of prime order are cyclic]]. The combination is non-obvious because "prime order" is a statement about a number while "cyclic" is a statement about structure, and Lagrange is the bridge between them.

A third combination is **divisibility plus index-counting eliminates subgroups and quotients**. The equation $|G| = |H| \cdot |G:H|$ means the index $|G:H|$ is itself a divisor of $|G|$, equal to $|G|/|H|$. Add the property $D$ that you are looking for a subgroup of a *specified* index $k$: such a subgroup can exist only if $k$ divides $|G|$, and then it would have order $|G|/k$. The result $E$ is a fast existence filter on subgroups of given index, and dually on the possible sizes of quotient groups, since $|G/N| = |G:N|$. This is non-obvious because the index feels like a derived quantity, not a constraint in its own right, until you read the equation symmetrically.

A fourth combination is **divisibility plus counting elements of each order**. By the corollary every element has order dividing $|G|$, so the elements of $G$ are sorted into bins indexed by the divisors $d$ of $|G|$ (property $C$). Add the property $D$ that elements of a given order come in predictable counts — for instance, in a cyclic group of order $n$ there are exactly $\varphi(d)$ elements of each order $d \mid n$. Summing the bin sizes recovers $|G|$, giving the identity $\sum_{d \mid n} \varphi(d) = n$. The result $E$ is that order-counting becomes an exact accounting tool, not just an inequality; this underlies the proof that a finite subgroup of the multiplicative group of a field is cyclic.

---

# Why Is It True

The intuition is a single picture, and once you have it the theorem is not surprising at all: **a subgroup tiles the group**.

Fix a subgroup $H$. Look at $H$ itself — it is a clump of $|H|$ elements sitting inside $G$, one of which is the identity. Now pick any element $g$ not in $H$ and form $gH$, the set you get by left-multiplying every element of $H$ by $g$. Two things happen, and they are the whole content of the theorem.

First, $gH$ has *exactly the same size* as $H$. Multiplying by $g$ is a reversible operation — you can undo it by multiplying by $g^{-1}$ — so the map $h \mapsto gh$ is a bijection from $H$ onto $gH$. Translation never compresses or stretches a set; it just slides it. So every coset is a perfect copy of $H$, all $|H|$ elements of it.

Second, two cosets are *either identical or completely disjoint* — they never partially overlap. The reason is that "lying in the same coset" is an equivalence relation: $x$ and $y$ are in the same coset of $H$ exactly when $x^{-1}y \in H$, and you can check this is reflexive, symmetric, and transitive directly from the subgroup axioms. Equivalence relations partition. So the cosets do not just cover $G$ — they cover it cleanly, with no double-counting.

Put the two facts together. The group $G$ is covered by cosets; the cosets do not overlap; and every coset has exactly $|H|$ elements. So $G$ is chopped into some number of identical tiles, each of size $|H|$. Call the number of tiles $|G : H|$. Counting the elements one tile at a time gives $|G| = |H| \cdot |G : H|$. There is no slack in this argument because there is no slack in the picture: a tiling of a finite region by identical tiles forces the area to be a multiple of the tile size. That is why $|H|$ *must* divide $|G|$ — not "tends to", not "usually" — it is a parity-of-the-tiling fact.

The corollary about element order is the same picture applied to the smallest interesting subgroup. Take any element $g$ and list its powers $e, g, g^2, \dots$ until they cycle back to $e$. That list is a subgroup — closed under multiplication because $g^r g^s = g^{r+s}$, closed under inverses because $g^{-1} = g^{n-1}$ where $n = \operatorname{ord}(g)$. It has exactly $\operatorname{ord}(g)$ distinct elements. So it is a tile, and the tiling argument says $\operatorname{ord}(g)$ divides $|G|$. The element's order is constrained simply because the element drags a subgroup along behind it.

---

# What Makes This Hard

The proof is short, and the one step that is not automatic is showing that two cosets which share even a single element must be the *same* coset — that there is no partial overlap. People often prove "cosets cover $G$" and "cosets all have size $|H|$" and then assume disjointness, but disjointness is exactly the part that needs the subgroup axioms (it is where closure under products and inverses is used, via the equivalence relation $x^{-1}y \in H$). The most common error is to argue with right cosets in one place and left cosets in another without noticing; the count $|G:H|$ is the same either way, but a proof that silently switches is not a proof.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Define an equivalence relation on $G$ whose classes are the left cosets of $H$. Show every class has size $|H|$ by exhibiting a bijection with $H$. Since the classes of an equivalence relation partition $G$ and all have the same size, $|G|$ is that common size times the number of classes. The corollary is this theorem applied to a cyclic subgroup.

**Subgoal decomposition:**

1. **[[Def - Coset|Cosets]] are the classes of an equivalence relation.** Show that the relation $x \sim y \iff x^{-1}y \in H$ is reflexive, symmetric, and transitive, and that the class of $x$ is precisely the coset $xH$.
   - *Hint:* Reflexivity uses $e \in H$; symmetry uses closure under inverses ($(x^{-1}y)^{-1} = y^{-1}x$); transitivity uses closure under products.
   - *Why needed:* Equivalence relations partition their underlying set, so this gives "the cosets are disjoint and cover $G$" for free, with no separate overlap argument.

2. **Every coset has exactly $|H|$ elements.** Show the map $H \to gH$, $h \mapsto gh$, is a bijection.
   - *Hint:* It is surjective by the definition of $gH$; it is injective because $gh_1 = gh_2$ implies $h_1 = h_2$ after left-multiplying by $g^{-1}$.
   - *Why needed:* This makes every tile the same size, so the total count is a clean product.

3. **Assemble the count.** Conclude $|G| = |H| \cdot |G:H|$ where $|G:H|$ is the number of cosets, hence $|H|$ divides $|G|$.
   - *Hint:* Partition into $|G:H|$ classes, each of size $|H|$; add up.
   - *Why needed:* This is the statement.

4. **Derive the corollary.** For $g \in G$, show $\langle g \rangle = \{e, g, \dots, g^{n-1}\}$ with $n = \operatorname{ord}(g)$ is a subgroup of order $n$, then apply step 3.
   - *Hint:* Closure: $g^r g^s = g^{r+s}$, reducing the exponent mod $n$ if needed; the $n$ listed powers are distinct because $g^i = g^j$ with $i > j$ would give $g^{i-j} = e$ with $0 < i-j < n$, contradicting minimality of $n$.
   - *Why needed:* It packages the most-used consequence — $\operatorname{ord}(g) \mid |G|$ and $g^{|G|} = e$.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: Same-coset is an equivalence relation
> **Statement:** For $H \leq G$, the relation $x \sim y \iff x^{-1}y \in H$ is an equivalence relation on $G$, and the equivalence class of $x$ is the left coset $xH$.
>
> **Hint:** Check the three axioms directly. Reflexivity needs $e \in H$. Symmetry needs that $H$ is closed under inverses. Transitivity needs that $H$ is closed under products.
>
> **Why needed:** It delivers disjointness and covering simultaneously — the cosets partition $G$ because they are the classes of an equivalence relation, so no separate "cosets don't overlap" argument is required.
>
> > [!note]- Full proof
> > *Reflexive:* $x^{-1}x = e \in H$, so $x \sim x$.
> >
> > *Symmetric:* if $x \sim y$ then $x^{-1}y \in H$; since $H$ is closed under inverses, $(x^{-1}y)^{-1} = y^{-1}x \in H$, so $y \sim x$.
> >
> > *Transitive:* if $x \sim y$ and $y \sim z$ then $x^{-1}y \in H$ and $y^{-1}z \in H$; since $H$ is closed under products, $(x^{-1}y)(y^{-1}z) = x^{-1}z \in H$, so $x \sim z$.
> >
> > *The class of $x$ is $xH$:* the element $y$ satisfies $y \sim x$ if and only if $x^{-1}y \in H$, i.e. if and only if $x^{-1}y = h$ for some $h \in H$, i.e. if and only if $y = xh$ for some $h \in H$, i.e. if and only if $y \in xH$.

> [!note]- Lemma 2: Left translation is a bijection $H \to gH$
> **Statement:** For any $g \in G$, the map $\lambda_g : H \to gH$ defined by $\lambda_g(h) = gh$ is a bijection. Hence $|gH| = |H|$ for every coset.
>
> **Hint:** Surjectivity is immediate from the definition of $gH$. Injectivity is left-cancellation by $g^{-1}$.
>
> **Why needed:** It makes every coset the same size as $H$, so the partition of $G$ into cosets is a partition into equal blocks.
>
> > [!note]- Full proof
> > *Surjective:* by definition $gH = \{gh : h \in H\}$, so every element of $gH$ is $\lambda_g(h)$ for some $h \in H$.
> >
> > *Injective:* if $\lambda_g(h_1) = \lambda_g(h_2)$, then $gh_1 = gh_2$; left-multiplying both sides by $g^{-1}$ gives $h_1 = h_2$.
> >
> > A bijection between finite sets equates their cardinalities, so $|gH| = |H|$.

> [!note]- Lemma 3: An element's powers form a subgroup of order $\operatorname{ord}(g)$
> **Statement:** Let $g \in G$ have finite order $n = \operatorname{ord}(g)$. Then $\langle g \rangle = \{e, g, g^2, \dots, g^{n-1}\}$ is a subgroup of $G$ with exactly $n$ elements.
>
> **Hint:** For closure, reduce exponents modulo $n$ using $g^n = e$. For the count, use the minimality of $n$ to rule out repeats.
>
> **Why needed:** It is the subgroup to which Lagrange is applied to obtain the corollary $\operatorname{ord}(g) \mid |G|$.
>
> > [!note]- Full proof
> > The set is non-empty ($e = g^0$ is in it). For closure under products and inverses it suffices, by the subgroup criterion, to check $g^r (g^s)^{-1} = g^{r-s} \in \langle g \rangle$: writing $r - s \equiv k \pmod n$ with $0 \leq k < n$ and using $g^n = e$ gives $g^{r-s} = g^k$, which is in the list.
> >
> > The $n$ listed elements are distinct: if $g^i = g^j$ with $0 \leq j \leq i \leq n-1$, then $g^{i-j} = e$ with $0 \leq i - j < n$; by minimality of $n$ as the least positive integer with $g^n = e$, the only possibility is $i - j = 0$, i.e. $i = j$. Hence $|\langle g \rangle| = n$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $G$ be a finite group and $H \leq G$. Then $|G| = |H| \cdot |G:H|$, where $|G:H|$ is the number of left cosets of $H$ in $G$; in particular $|H| \mid |G|$.
>
> *Proof.* Define a relation on $G$ by $x \sim y \iff x^{-1}y \in H$.
>
> This is an equivalence relation. It is reflexive since $x^{-1}x = e \in H$. It is symmetric since $x^{-1}y \in H$ implies $(x^{-1}y)^{-1} = y^{-1}x \in H$, $H$ being closed under inverses. It is transitive since $x^{-1}y \in H$ and $y^{-1}z \in H$ imply $(x^{-1}y)(y^{-1}z) = x^{-1}z \in H$, $H$ being closed under products.
>
> The equivalence class of $x$ is the left coset $xH$: indeed $y \sim x$ if and only if $x^{-1}y \in H$ if and only if $y = xh$ for some $h \in H$ if and only if $y \in xH$. Since the classes of an equivalence relation partition the underlying set, the distinct left cosets of $H$ partition $G$ into disjoint, exhaustive blocks.
>
> Each block has $|H|$ elements. For a fixed $g$, the map $\lambda_g : H \to gH$, $h \mapsto gh$, is surjective by the definition of $gH$ and injective because $gh_1 = gh_2$ implies $h_1 = h_2$ on left-multiplication by $g^{-1}$. Hence $|gH| = |H|$.
>
> Let $|G:H|$ denote the number of distinct cosets. Since $G$ is the disjoint union of these $|G:H|$ cosets, each of size $|H|$,
> $$|G| = \sum_{\text{cosets } gH} |gH| = |G:H| \cdot |H|.$$
> In particular $|H|$ divides $|G|$. $\qquad\blacksquare$
>
> **Corollary.** If $G$ is finite and $g \in G$, then $\operatorname{ord}(g) \mid |G|$ and $g^{|G|} = e$.
>
> *Proof.* Let $n = \operatorname{ord}(g)$ and consider $H = \{e, g, g^2, \dots, g^{n-1}\}$. This is a subgroup: it is non-empty, and for $g^r, g^s \in H$ the element $g^r (g^s)^{-1} = g^{r-s}$ lies in $H$, since reducing $r - s$ modulo $n$ and using $g^n = e$ rewrites it as one of the listed powers. The $n$ listed elements are distinct, for if $g^i = g^j$ with $i \geq j$ then $g^{i-j} = e$ with $0 \le i - j < n$, forcing $i - j = 0$ by minimality of $n$. Hence $|H| = n$.
>
> By Lagrange's theorem $n = |H|$ divides $|G|$. Write $|G| = nk$. Then
> $$g^{|G|} = g^{nk} = (g^n)^k = e^k = e. \qquad\blacksquare$$
>
> This corollary is exactly the lemma proved in §1.1 of the source lecture notes.

---

# Cross-Field Exercise Suggestions

The aim here is to find settings where Lagrange applies but is not advertised — to battle-test recognition of the *sources*.

**Number theory: Fermat's and Euler's theorems.** Take $G = (\mathbb{Z}/p\mathbb{Z})^\times$, the group of nonzero [[Def - Residue|residues]] modulo a prime $p$ under multiplication, which has order $p - 1$. The corollary says $a^{p-1} \equiv 1 \pmod p$ for every $a$ coprime to $p$ — this is Fermat's little theorem, and it is *purely* the order corollary in disguise. Replacing $p$ by a general modulus $n$ and $G$ by the units $(\mathbb{Z}/n\mathbb{Z})^\times$ of order $\varphi(n)$ gives Euler's theorem $a^{\varphi(n)} \equiv 1$. The application is non-obvious because the statements look like facts about exponents and remainders, with no group in sight; the property $B$ "the units mod $n$ form a finite group" is the bridge to the precondition. Worked in [[Ex - Order of an element divides the group order]].

**Field theory: no field of order $6$.** The nonzero elements of a finite field $\mathbb{F}$ form a group under multiplication of order $|\mathbb{F}| - 1$, and the additive group has order $|\mathbb{F}|$. One can show every element satisfies $x \cdot x \cdot \dots$ relations that, combined with Lagrange on these two groups, force $|\mathbb{F}|$ to be a prime power. So there is no field with exactly $6$ elements. The non-obvious step is seeing two different groups hiding in one field and applying Lagrange to each.

**Combinatorics: counting symmetric colourings.** Suppose you colour the faces of a cube and ask how many colourings are fixed by a given rotation group $G$ of order $24$. The colourings fixed by a subgroup, or the size of the orbit of a colouring, are governed by $|G| = |G_x| \cdot |G \cdot x|$ — the orbit–stabiliser theorem, which is Lagrange with $H$ the stabiliser subgroup. The property $B$ here is "$G$ acts on the set of colourings", and the stabiliser of a colouring is the secret subgroup. The application is non-obvious because the problem is phrased as enumeration, never mentioning [[Def - Subgroup|subgroups]] at all.

**Linear algebra: orders of invertible matrices over a finite field.** The group $\mathrm{GL}_n(\mathbb{F}_q)$ is finite, with a known order $\prod_{i=0}^{n-1}(q^n - q^i)$. The corollary then bounds the multiplicative order of any invertible matrix over $\mathbb{F}_q$: it must divide that product. Asking "can a $3 \times 3$ matrix over $\mathbb{F}_2$ have order $7$?" becomes a divisibility check. The non-obvious part is recognizing that a question about how many times you can multiply a matrix by itself is a question about element order in a finite group.

---

# Bridges

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]]** — where Lagrange counts a subgroup against the whole group, the first isomorphism theorem *identifies* the quotient $G/\ker\varphi$ with $\operatorname{im}\varphi$. They cooperate constantly: a homomorphism $\varphi$ produces a kernel subgroup that Lagrange measures, and the index $|G : \ker\varphi| = |\operatorname{im}\varphi|$ is then forced to divide $|G|$. Lagrange is the counting half, the first isomorphism theorem the structural half, of the same homomorphism.

- **Orbit–Stabiliser Theorem** *(from [[Group Theory II — §1.3–1.4]])* — this is Lagrange's theorem read through a group action: $|G| = |G_x| \cdot |G \cdot x|$, with the stabiliser $G_x$ playing the role of $H$ and the orbit $G \cdot x$ in bijection with the set of cosets. Every orbit-counting argument is therefore a coset count in disguise; Lagrange is the special case where $G$ acts on the cosets of $H$ by left multiplication.

- **[[Thm - Composition Series|Composition Series]]** — Lagrange constrains but does not construct: knowing $|H| \mid |G|$ does not tell you a subgroup of order $|H|$ exists. The converse problem — building subgroups of prescribed order — is taken up by Cauchy's theorem and the Sylow theorems in [[Group Theory III — §1.5–1.7]], which are the *partial converses* to Lagrange. The composition series then shows how the divisors of $|G|$ assemble into the group's "prime factorization".

- **The false converse, and $A_4$** — Lagrange does not assert that every divisor of $|G|$ is the order of some subgroup. The standard counterexample is the alternating group $A_4$, of order $12$, which has *no subgroup of order $6$*: if it had one, that subgroup would have index $2$, hence be normal, hence be a union of conjugacy classes containing the identity — but the conjugacy class sizes of $A_4$ ($1, 3, 4, 4$) admit no sub-collection including the class of size $1$ that sums to $6$. So the gap between "divides" and "is realized" is real, and closing it (partially) is exactly the content of Cauchy and Sylow.

- **Lagrange's theorem for cosets in topology and Galois theory** — the index formula $|G| = |H| \cdot |G:H|$ reappears as the degree formula for field extensions $[L : F] = [L : K][K : F]$ and as the multiplicativity of covering-space degrees. In each case a "whole" is partitioned into equinumerous translates of a "part", and the tower law is Lagrange with the group axioms abstracted away.
