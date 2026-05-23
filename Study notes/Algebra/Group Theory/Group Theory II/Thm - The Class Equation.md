---
type: theorem
subject: group-theory
prereqs:
  - "Def - Conjugacy Class"
  - "Def - Centraliser and Centre"
  - "Def - Group Action"
  - "Thm - Orbit-Stabiliser Theorem"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Notation

$G$ is a finite group with identity $e$ and order $|G|$. The group acts **on itself by conjugation**: $g$ sends $x$ to $gxg^{-1}$. The orbit of $x$ under this action is its [[Def - Conjugacy Class|conjugacy class]] $\operatorname{ccl}_G(x) = \{gxg^{-1} : g \in G\}$, and the conjugacy classes partition $G$. The stabiliser of $x$ is its [[Def - Centraliser and Centre|centraliser]] $C_G(x) = \{g \in G : gx = xg\}$, the set of elements commuting with $x$; it is a [[Def - Subgroup|subgroup]] of $G$. The **centre** $Z(G) = \{g \in G : gx = xg \text{ for all } x\} = \bigcap_{x} C_G(x)$ is the set of elements commuting with everything. For $H \leq G$, the **index** $|G : H| = |G|/|H|$ is the number of cosets of $H$. The full notation registry lives on the parent page [[Group Theory II — §1.3–1.4]].

---

# Statement

> **The Class Equation.** Let $G$ be a finite group. Then
> $$|G| = |Z(G)| + \sum_{i} |G : C_G(x_i)|,$$
> where $x_1, x_2, \dots$ run over a set of representatives of the **non-central** conjugacy classes — one $x_i$ from each conjugacy class of size greater than $1$. Each summand $|G : C_G(x_i)|$ is an integer greater than $1$ that divides $|G|$.

The identity rests on the following proposition, which is the orbit–stabiliser theorem specialised to conjugation and is the part actually proved in the lecture notes; the class equation is the natural way of packaging it.

> **Proposition (class size).** For any $x \in G$,
> $$|\operatorname{ccl}_G(x)| = |G : C_G(x)| = \frac{|G|}{|C_G(x)|}.$$
> In particular, the size of every conjugacy class divides $|G|$.

---

# Motivation

A finite group is, at bottom, a finite set with a multiplication table, and [[Thm - Lagrange's Theorem|Lagrange's theorem]] gives the first toehold on its structure: every [[Def - Subgroup|subgroup]] has order dividing $|G|$. But Lagrange constrains only the objects you have already found. It says nothing about what the group *contains* — whether it has a non-trivial centre, whether it is abelian, whether it has a normal [[Def - Subgroup|subgroup]]. The integer $|G|$ ought to know more about the group than just its list of divisors, and the class equation is the instrument that extracts that extra knowledge.

The idea is to count the elements of $G$ in an organised way. Conjugation is an action of $G$ on itself, so its orbits — the [[Def - Conjugacy Class|conjugacy classes]] — partition $G$ into disjoint blocks. Counting $G$ block by block gives $|G| = \sum |\operatorname{ccl}_G(x_i)|$, a true but inert statement. It becomes a lever once you make two observations. First, by [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser]], each block size $|\operatorname{ccl}_G(x)|$ equals the index $|G : C_G(x)|$, so each block size *divides $|G|$*. Second, the singleton classes — the elements whose conjugacy class is just themselves — are exactly the elements that commute with everything, that is, the [[Def - Centraliser and Centre|centre]] $Z(G)$. Separating those singletons out of the sum gives the class equation in its useful form: $|G|$, split into the size of the centre plus a collection of index terms each dividing $|G|$ and each genuinely larger than $1$.

The reason this matters is that it transmits divisibility information *from* the visible quantity $|G|$ *to* the hidden quantity $|Z(G)|$. The centre is hard to access directly — you would have to inspect every element and check it against every other. The class equation lets you reason about $|Z(G)|$ purely arithmetically. The headline application, proved in [[Group Theory III — §1.5–1.7]], is that a group of prime-power order $p^n$ has a non-trivial centre: every non-central index term is divisible by $p$, the left side $|G| = p^n$ is divisible by $p$, so $|Z(G)|$ must be divisible by $p$ as well, and therefore cannot be $\{e\}$. That single deduction, which the class equation makes a two-line argument, is the foundation of the entire theory of $p$-[[Def - Group|groups]] and the Sylow theorems.

---

# Sources and Targets

This section is not an input/output summary. It records the non-obvious circumstances under which a problem secretly calls for the class equation (sources), and the non-obvious conclusions that follow once the equation is combined with one further fact (targets).

**Sources (Input Broadening)**

The class equation needs only *a finite group*, so the question is not "does it apply" but "is it the right move". Each property $B$ below is a feature of a problem that should make you reach for the class equation.

The cleanest source is **the order $|G|$ is a prime power**, $|G| = p^n$. The bridge to the class equation is the proposition: every conjugacy class size divides $|G| = p^n$, so every class size is a power of $p$ — either $1$ or a positive power of $p$, hence divisible by $p$. This is non-obvious because the hypothesis is a statement about a single integer while the conclusion controls *every* orbit of an action at once. The moment you see "$|G| = p^n$", the class equation reads $p^n = |Z(G)| + (\text{multiples of } p)$, and you have learned $p \mid |Z(G)|$ without any further work. This is the source behind the proof that $p$-groups have non-trivial centre, and behind [[Ex - Groups of order p squared are abelian]].

A subtler source is **a problem about whether the group is abelian, or how far it is from abelian**. Property $B$ is any constraint on $Z(G)$ or on commutativity. The bridge is that $Z(G)$ appears *explicitly* and isolated in the class equation — it is the only term not of the form "non-trivial index". So any handle on the other terms is automatically a handle on $|Z(G)|$. This is non-obvious because most identities involving a group do not feature the centre at all; the class equation is the one that puts it in the open. For instance, knowing that $G/Z(G)$ is cyclic forces $G$ abelian, and the class equation is often the route to pinning down $|Z(G)|$ in the first place.

A third source is **a problem that supplies the conjugacy class sizes, or the centraliser orders, of a specific group**. Property $B$ is a table of class sizes — common for symmetric and alternating groups, where [[Thm - Conjugacy Classes of the Symmetric Group|cycle type makes every class size computable]]. The bridge is that the class equation is then a numerical *consistency check and completeness check*: the sizes must sum to $|G|$, the singletons must account for $|Z(G)|$, and any sub-collection of classes that could form a normal subgroup must include the identity's class and sum to a divisor of $|G|$. This is the source behind the brute-force proof that [[Thm - Simplicity of the Alternating Group|A₅ is simple]].

A fourth source is **a counting problem that asks how many conjugates a given element has**. Property $B$ is "an element $x$ is distinguished and its conjugates matter". The bridge is the proposition directly: the number of conjugates is $|G : C_G(x)|$, so the count reduces to "how many elements commute with $x$". This is non-obvious because conjugates are defined by an existential ("$\exists g$ with $gxg^{-1} = y$") while the centraliser is a concrete subgroup you can write down and measure.

**Targets (Output Amplification)**

The class equation delivers the identity $|G| = |Z(G)| + \sum |G : C_G(x_i)|$ together with the fact that every index term divides $|G|$ and exceeds $1$. Combined with one further property $D$, this becomes a positive structural result.

The most important combination is **the class equation plus a prime dividing every non-central term forces a non-trivial centre**. Take property $D$: every summand $|G : C_G(x_i)|$ is divisible by a fixed prime $p$, and $p \mid |G|$. Reading the equation modulo $p$, the sum on the right vanishes, so $|G| \equiv |Z(G)| \pmod p$, whence $p \mid |Z(G)|$ and $Z(G) \neq \{e\}$. The result $E$ — *the centre is non-trivial* — is non-obvious because it manufactures an element commuting with everything out of pure divisibility, with no construction. This is exactly how $p$-groups are shown to have non-trivial centre, and it cascades: $G/Z(G)$ is a smaller $p$-group, so the centre can be climbed inductively, giving the central series that defines nilpotency.

A second combination is **the class equation plus "$Z(G)$ is small" forces a large conjugacy class**. Property $D$ is an upper bound on $|Z(G)|$, say $Z(G) = \{e\}$. Then $|G| - 1 = \sum |G : C_G(x_i)|$ must be partitioned into index terms, each a non-trivial divisor of $|G|$. The result $E$ is a strong combinatorial restriction on the multiset of class sizes — often enough to rule out a configuration entirely. This non-obvious pigeonhole is the engine of many non-simplicity proofs in [[Group Theory III — §1.5–1.7]]: if no admissible multiset of class sizes sums correctly, the assumed group cannot exist.

A third combination is **the class equation plus normality, read as "a normal subgroup is a union of classes"**. Property $D$ is that one is hunting for a [[Def - Normal Subgroup|normal subgroup]] $N$. Because conjugation fixes $N$ setwise, $N$ is a union of whole conjugacy classes, one of which is $\{e\}$; and by Lagrange $|N|$ divides $|G|$. The result $E$ is a finite search: list the class sizes from the class equation and ask whether any sub-collection containing the $1$ sums to a proper divisor of $|G|$. If none does, $G$ is [[Def - Simple Group|simple]]; if one does, you have found a candidate normal subgroup. This is non-obvious because it converts the structural question "is $G$ simple" into arithmetic on a list of integers.

---

# Why Is It True

The class equation is not a deep theorem; it is honest bookkeeping, and the right way to see it is to watch the count assemble itself.

Start with conjugation as an action. Each $g \in G$ relabels the group by $x \mapsto gxg^{-1}$ — this is "perform $x$ in the coordinate system $g$ sets up", change of coordinates. Like any [[Def - Group Action|group action]], conjugation carves $G$ into orbits, and these orbits are the [[Def - Conjugacy Class|conjugacy classes]]. Orbits of an action are always disjoint and always cover the set, so the conjugacy classes tile $G$ perfectly. If you simply add up the sizes of the tiles you recover $|G|$. That is the entire identity in embryo: $|G| = \sum |\operatorname{ccl}_G(x_i)|$, summed over one representative per class.

Now the two refinements that turn this inert sum into a lever.

The first is that you can *measure* each tile. The [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] says the size of an orbit equals the index of the stabiliser. For the conjugation action the stabiliser of $x$ is $\{g : gxg^{-1} = x\}$, which is exactly $\{g : gx = xg\}$, the [[Def - Centraliser and Centre|centraliser]] $C_G(x)$. So each tile has size $|G : C_G(x)|$. The intuition for *why* the orbit and the centraliser are complementary: the orbit measures how many distinct disguises $x$ can wear under conjugation, and the centraliser measures the elements whose coordinate change leaves $x$ looking the same. The more elements commute with $x$, the fewer distinct conjugates it can have — and orbit–stabiliser says that trade-off is exact, with the product always equal to $|G|$. The consequence is the proposition: every class size divides $|G|$, because every index does.

The second refinement is to look at the smallest tiles. A conjugacy class has size $1$ precisely when $x$ has only itself as a conjugate, i.e. $gxg^{-1} = x$ for *every* $g$, i.e. $x$ commutes with everything — i.e. $x \in Z(G)$. So the singleton classes are not scattered specks; collected together they are exactly the centre. There are $|Z(G)|$ of them. Pulling those singletons out of the sum and counting them in one lump gives
$$|G| = \underbrace{|Z(G)|}_{\text{the singletons}} + \underbrace{\sum_i |G : C_G(x_i)|}_{\text{the genuine, larger-than-one tiles}}.$$

That is the class equation, and once you see it built this way it is unsurprising. The content is concentrated in one place: each non-central term, being an index, divides $|G|$ and is strictly bigger than $1$. So the class equation is a statement that $|G|$ decomposes as $|Z(G)|$ plus a sum of proper divisors of $|G|$. When $|G|$ has rigid arithmetic — a prime power above all — that decomposition has very little freedom, and squeezing it is what makes the equation powerful.

---

# What Makes This Hard

The genuine step is the proposition $|\operatorname{ccl}_G(x)| = |G : C_G(x)|$: one must recognise the conjugacy class as the *orbit* of $x$ and the centraliser as the *stabiliser* of $x$, and then it is a citation of [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser]] — but the recognition is what people miss. The other subtle point is identifying the singleton classes correctly: a class has size $1$ exactly when $x \in Z(G)$, and the most common error is to forget that the equation sums over *non-central* representatives only, then double-count the centre by also including central terms (each a trivial index $|G:G| = 1$) in the sum. Stated cleanly, the singletons go into the $|Z(G)|$ lump and nowhere else.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire result.

**High-level strategy:**
Let $G$ act on itself by conjugation. Its orbits, the conjugacy classes, partition $G$, so $|G|$ is the sum of the class sizes. Use orbit–stabiliser to rewrite each class size as a centraliser index, then split off the size-$1$ classes — which are exactly the central elements — as a single block.

**Subgoal decomposition:**

1. **Conjugation is a group action of $G$ on $G$.** Verify $e \ast x = x$ and $g \ast (h \ast x) = (gh) \ast x$ for $g \ast x := gxg^{-1}$.
   - *Hint:* $e x e^{-1} = x$; and $g(hxh^{-1})g^{-1} = (gh)x(gh)^{-1}$ since $(gh)^{-1} = h^{-1}g^{-1}$.
   - *Why needed:* It licenses the language of orbits and stabilisers, so the conjugacy classes are genuine orbits and partition $G$.

2. **Class size equals centraliser index.** Show the stabiliser of $x$ under conjugation is $C_G(x)$, then apply [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser]] to get $|\operatorname{ccl}_G(x)| = |G : C_G(x)|$.
   - *Hint:* $g$ stabilises $x$ if and only if $gxg^{-1} = x$ if and only if $gx = xg$ — that is the definition of $C_G(x)$.
   - *Why needed:* This is the proposition; it makes every class size a divisor of $|G|$.

3. **Singleton classes are exactly the centre.** Show $|\operatorname{ccl}_G(x)| = 1 \iff x \in Z(G)$.
   - *Hint:* The class is a singleton if and only if $gxg^{-1} = x$ for all $g$, which says $x$ commutes with all of $G$.
   - *Why needed:* It lets the size-$1$ classes be collected into one block of size $|Z(G)|$.

4. **Assemble the class equation.** The classes partition $G$, so $|G| = \sum_{\text{all classes}} (\text{size})$. Split the sum: the singleton classes contribute $|Z(G)|$ in total, the rest contribute $\sum_i |G : C_G(x_i)|$ with each term $> 1$.
   - *Hint:* Sum the partition; group the size-$1$ terms together.
   - *Why needed:* This is the statement $|G| = |Z(G)| + \sum_i |G : C_G(x_i)|$.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: Conjugation is an action of $G$ on itself
> **Statement:** The map $G \times G \to G$, $(g, x) \mapsto gxg^{-1}$, is a [[Def - Group Action|group action]] of $G$ on the set $G$.
>
> **Hint:** Check the identity axiom and the compatibility axiom directly, being careful that $(gh)^{-1} = h^{-1}g^{-1}$.
>
> **Why needed:** It guarantees the conjugacy classes are the orbits of an action, hence that they partition $G$ — which is what makes the class equation a count.
>
> > [!note]- Full proof
> > *Identity:* $e \ast x = exe^{-1} = x$.
> >
> > *Compatibility:* for $g, h \in G$,
> > $$g \ast (h \ast x) = g(hxh^{-1})g^{-1} = (gh)\,x\,(h^{-1}g^{-1}) = (gh)\,x\,(gh)^{-1} = (gh) \ast x.$$
> >
> > Both axioms hold, so conjugation is an action. (Its [[Thm - Actions Correspond to Homomorphisms|permutation representation]] $\varphi : G \to \operatorname{Sym}(G)$ even lands in [[Def - Automorphism Group|operatornameAut(G)]], since each $\varphi(g)$ is a homomorphism: $\varphi(g)(x_1 x_2) = g x_1 x_2 g^{-1} = (g x_1 g^{-1})(g x_2 g^{-1}) = \varphi(g)(x_1)\,\varphi(g)(x_2)$.)

> [!note]- Lemma 2: The stabiliser of $x$ under conjugation is $C_G(x)$
> **Statement:** For the conjugation action, the stabiliser of $x \in G$ is the [[Def - Centraliser and Centre|centraliser]] $C_G(x) = \{g \in G : gx = xg\}$.
>
> **Hint:** Unwind "stabiliser": $g$ stabilises $x$ if and only if $g \ast x = x$.
>
> **Why needed:** It is the identification that turns orbit–stabiliser into the proposition $|\operatorname{ccl}_G(x)| = |G : C_G(x)|$.
>
> > [!note]- Full proof
> > By definition the stabiliser of $x$ is $\{g \in G : g \ast x = x\} = \{g : gxg^{-1} = x\}$. Right-multiplying the equation $gxg^{-1} = x$ by $g$ gives the equivalent equation $gx = xg$. Hence the stabiliser is $\{g : gx = xg\} = C_G(x)$. Being a stabiliser, it is automatically a [[Def - Subgroup|subgroup]] of $G$.

> [!note]- Lemma 3: Class size equals centraliser index
> **Statement:** For any $x$ in a finite group $G$, $\ |\operatorname{ccl}_G(x)| = |G : C_G(x)| = |G|/|C_G(x)|$; in particular $|\operatorname{ccl}_G(x)|$ divides $|G|$.
>
> **Hint:** Apply the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] with the orbit $\operatorname{ccl}_G(x)$ and the stabiliser $C_G(x)$.
>
> **Why needed:** This is the proposition underlying the class equation; the divisibility of class sizes is its sharpest consequence.
>
> > [!note]- Full proof
> > By Lemma 1 conjugation is an action; the orbit of $x$ is $\operatorname{ccl}_G(x)$ and, by Lemma 2, its stabiliser is $C_G(x)$. The [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] provides a bijection $\operatorname{ccl}_G(x) \leftrightarrow G/C_G(x)$, $gxg^{-1} \leftrightarrow g\,C_G(x)$. Hence $|\operatorname{ccl}_G(x)| = |G : C_G(x)|$, and for finite $G$ this equals $|G|/|C_G(x)|$. Since $|C_G(x)|$ divides $|G|$ by [[Thm - Lagrange's Theorem|Lagrange's theorem]], the quotient $|\operatorname{ccl}_G(x)|$ is an integer dividing $|G|$.

> [!note]- Lemma 4: A conjugacy class is a singleton if and only if its element is central
> **Statement:** $|\operatorname{ccl}_G(x)| = 1$ if and only if $x \in Z(G)$.
>
> **Hint:** A class is a singleton if and only if $x$ is its own only conjugate; spell out what that says for every $g$.
>
> **Why needed:** It identifies the size-$1$ classes with the centre, so the class equation can collect them into the single block $|Z(G)|$.
>
> > [!note]- Full proof
> > The class $\operatorname{ccl}_G(x) = \{gxg^{-1} : g \in G\}$ contains $x$ (take $g = e$). It is a singleton precisely when $gxg^{-1} = x$ for every $g \in G$, equivalently $gx = xg$ for every $g$, equivalently $x$ commutes with all of $G$ — which is the definition of $x \in Z(G)$. Hence the singleton classes are exactly the elements of the centre, and there are $|Z(G)|$ of them.

---

# Formal Proof

> [!note]- Complete formal proof
> **Proposition.** Let $G$ be a finite group. For every $x \in G$,
> $$|\operatorname{ccl}_G(x)| = |G : C_G(x)| = \frac{|G|}{|C_G(x)|},$$
> and in particular $|\operatorname{ccl}_G(x)|$ divides $|G|$.
>
> *Proof.* Let $G$ act on the set $G$ by conjugation, $g \ast x = gxg^{-1}$; this is an action because $e \ast x = x$ and $g \ast (h \ast x) = g(hxh^{-1})g^{-1} = (gh)x(gh)^{-1} = (gh)\ast x$. Under this action the orbit of $x$ is $\operatorname{ccl}_G(x)$ by definition, and the stabiliser of $x$ is
> $$\{g \in G : gxg^{-1} = x\} = \{g \in G : gx = xg\} = C_G(x).$$
> The [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] applied to this action gives a bijection $\operatorname{ccl}_G(x) \leftrightarrow G/C_G(x)$, hence $|\operatorname{ccl}_G(x)| = |G : C_G(x)|$. For finite $G$ this index equals $|G|/|C_G(x)|$, and since $|C_G(x)|$ divides $|G|$ by [[Thm - Lagrange's Theorem|Lagrange's theorem]], $|\operatorname{ccl}_G(x)|$ is an integer dividing $|G|$. $\qquad\blacksquare$
>
> **The Class Equation.** Let $G$ be a finite group. Then
> $$|G| = |Z(G)| + \sum_{i} |G : C_G(x_i)|,$$
> the sum running over one representative $x_i$ from each conjugacy class of size greater than $1$, with every summand a divisor of $|G|$ exceeding $1$.
>
> *Proof.* The conjugacy classes are the orbits of the conjugation action, so they are pairwise disjoint and their union is $G$. Counting $G$ block by block,
> $$|G| = \sum_{\text{conjugacy classes } \mathcal{C}} |\mathcal{C}|.$$
> Split the conjugacy classes into those of size $1$ and those of size greater than $1$.
>
> A class $\operatorname{ccl}_G(x)$ has size $1$ exactly when $gxg^{-1} = x$ for all $g \in G$, i.e. when $x$ commutes with every element of $G$, i.e. when $x \in Z(G)$. Thus the size-$1$ classes are precisely the singletons $\{x\}$ with $x \in Z(G)$, and there are exactly $|Z(G)|$ of them; together they contribute $|Z(G)|$ to the sum.
>
> For each class of size greater than $1$, choose a representative $x_i$. By the proposition, that class has size $|\operatorname{ccl}_G(x_i)| = |G : C_G(x_i)|$, an integer dividing $|G|$; and since the class is not a singleton, $|G : C_G(x_i)| > 1$.
>
> Substituting both pieces into the block count gives
> $$|G| = |Z(G)| + \sum_i |G : C_G(x_i)|,$$
> with the stated properties of the summands. $\qquad\blacksquare$
>
> **Remark (the lever).** If $|G| = p^n$ for a prime $p$, then by the proposition every class size divides $p^n$, so every non-central summand $|G : C_G(x_i)|$ is a positive power of $p$, hence divisible by $p$. Reducing the class equation modulo $p$ kills the sum, leaving $0 \equiv |Z(G)| \pmod p$. Therefore $p \mid |Z(G)|$, and since $e \in Z(G)$ gives $|Z(G)| \geq 1$, in fact $|Z(G)| \geq p$: a finite [[Group Theory III — §1.5–1.7|p-group has non-trivial centre]].

---

# Cross-Field Exercise Suggestions

The aim is to find settings where the class equation, or its proposition, is the decisive tool although nothing in the problem advertises conjugacy.

**Number theory: a counting proof of Cauchy's theorem for $p$-[[Def - Group|groups]], and the fixed-point principle.** The class equation is the prototype of a general move — *let a group act and count fixed points modulo $p$*. The same idea, applied to a cyclic group $C_p$ acting on a cleverly chosen set, gives McKay's one-page proof of Cauchy's theorem (a group whose order is divisible by $p$ has an element of order $p$). Recognising that the class equation is "the conjugation instance of: $|X| \equiv |X^G| \pmod p$ when a $p$-group acts" is what lets the technique transfer; the non-obvious part is seeing the class equation not as a fact about conjugacy but as a fact about fixed points.

**Linear algebra and geometry: similarity classes of matrices.** Two matrices are *similar* exactly when they are conjugate in the general linear group $\mathrm{GL}_n(\mathbb{F})$, $A \sim PAP^{-1}$. The conjugacy class of $A$ is its similarity class, and its centraliser is the group of invertible matrices commuting with $A$. Over a finite field $\mathbb{F}_q$, the proposition $|\operatorname{ccl}(A)| = |\mathrm{GL}_n : C(A)|$ counts how many matrices share a given rational canonical form — a purely combinatorial enumeration extracted from the group-theoretic identity. The application is non-obvious because "similarity" is taught as a linear-algebra equivalence, with no group action named.

**Representation theory: why the number of irreducible characters is the number of classes.** A class function is a function on $G$ constant on conjugacy classes; the [[Def - Dimension|dimension]] of the space of class functions is therefore the *number of conjugacy classes* — the number of terms organised by the class equation. The deep theorem that this number also counts the irreducible representations of $G$ means the class equation's bookkeeping silently fixes the size of the character table. The non-obvious link is that a humble partition-of-$|G|$ identity controls the [[Def - Dimension|dimension]] count of representation theory.

**Combinatorics: necklaces and the orbit-counting heuristic.** When a finite group acts on a set of colourings, the orbits are the distinct necklaces, and the proposition $|\text{orbit}| = |G : \text{stabiliser}|$ is the per-necklace instance of the class equation's per-class statement. A problem asking "how many necklaces have a given symmetry group" is asking for a stabiliser, hence for an index — exactly the proposition. The application is non-obvious because the problem is phrased as enumeration with no group conjugacy in sight; the bridge is that *every* orbit-size computation is the same arithmetic as a conjugacy-class-size computation.

---

# Bridges

- **[[Thm - Orbit-Stabiliser Theorem|Orbit–Stabiliser Theorem]]** — the class equation is orbit–stabiliser specialised to one particular action, conjugation of $G$ on itself, and then summed over all orbits. The proposition $|\operatorname{ccl}_G(x)| = |G : C_G(x)|$ is literally orbit–stabiliser with the orbit renamed "conjugacy class" and the stabiliser renamed "centraliser". Everything distinctive about the class equation comes from the *choice* of this action; the theorem behind it is generic.

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]** — Lagrange supplies the divisibility that makes each class-equation summand a *proper divisor* of $|G|$: the index $|G : C_G(x_i)|$ divides $|G|$ precisely because $|C_G(x_i)|$ does. Lagrange constrains one subgroup at a time; the class equation aggregates Lagrange over the family of centralisers into a single additive identity about $|G|$.

- **[[Thm - Conjugacy Classes of the Symmetric Group|Conjugacy Classes of the Symmetric Group]]** — for $G = S_n$ the class equation becomes completely explicit, since conjugacy classes are cycle types and each class size is given by the formula $n!/\prod_k k^{a_k}a_k!$. The abstract sum $|G| = |Z(G)| + \sum |G:C_G(x_i)|$ turns into the concrete statement that the cycle-type class sizes sum to $n!$, with $Z(S_n) = \{e\}$ for $n \geq 3$.

- **[[Thm - Simplicity of the Alternating Group|Simplicity of the Alternating Group]]** — for $A_5$ the class equation reads $60 = 1 + 12 + 12 + 15 + 20$, and simplicity is the observation that no sub-collection of $\{1, 12, 12, 15, 20\}$ containing the $1$ sums to a proper divisor of $60$. The class equation provides the multiset of class sizes; checking it against the divisors of $|G|$ is the brute-force half of the simplicity story.

---

# Unlocked by This

> [!tip] $p$-groups have non-trivial centre *(from [[Group Theory III — §1.5–1.7]])*
> Applying the class equation to a group of order $p^n$: every non-central term is divisible by $p$, so $p \mid |Z(G)|$ and the centre cannot be trivial. This single deduction launches the structure theory of $p$-groups — the upper central series, nilpotency, and the existence of subgroups of every prime-power order dividing $|G|$.

> [!tip] The Sylow Theorems *(from [[Group Theory III — §1.5–1.7]])*
> The class equation is the model for the Sylow proofs, which all run by letting a group act, splitting a count into fixed and moved points, and reading off congruences modulo $p$. Sylow's theorems — existence, conjugacy, and the count $n_p \equiv 1 \pmod p$ of Sylow $p$-subgroups — are conjugation-counting arguments built on exactly this template.
