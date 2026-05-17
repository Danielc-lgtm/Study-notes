---
type: theorem
subject: group-theory
prereqs:
  - "Def - p-group"
  - "Def - Centraliser and Centre"
  - "Def - Conjugacy Class"
  - "Thm - The Class Equation"
  - "Thm - Lagrange's Theorem"
  - "Def - Simple Group"
  - "Def - Normal Subgroup"
tags: [algebra, group-theory]
---

# Notation

$G$ is a finite group with identity $e$. A prime is $p$, and $G$ is a [[Def - p-group|p-group]] when $|G| = p^n$ for some $n \geq 1$. The **centre** is $Z(G) = \{x \in G : xg = gx \text{ for all } g \in G\}$, the set of elements commuting with everything; it is always a [[Def - Normal Subgroup|normal subgroup]] of $G$ (see [[Def - Centraliser and Centre]]). The **centraliser** of $x$ is $C_G(x) = \{g \in G : gx = xg\}$, the elements commuting with that one $x$. The **conjugacy class** of $x$ is $\operatorname{ccl}(x) = \{gxg^{-1} : g \in G\}$, and $|G : C_G(x)|$ is the index of the centraliser (see [[Def - Conjugacy Class]]). "Non-trivial" means "not equal to $\{e\}$". The full registry is on [[Group Theory III — §1.5–1.7]].

---

# Statement

> **Theorem (non-trivial centre of a $p$-group).** Let $G$ be a finite [[Def - p-group|p-group]] — a group of order $p^n$ with $p$ prime and $n \geq 1$. Then the [[Def - Centraliser and Centre|centre]] $Z(G)$ is non-trivial:
> $$Z(G) \neq \{e\}, \qquad \text{indeed} \qquad p \mid |Z(G)|.$$

> **Corollary (a $p$-group is not simple for $n \geq 2$).** If $|G| = p^n$ with $n \geq 2$, then $G$ is not a [[Def - Simple Group|simple group]]: it has a proper non-trivial [[Def - Normal Subgroup|normal subgroup]].

The corollary follows because $Z(G)$ is always normal in $G$. If $Z(G) = G$ then $G$ is abelian and any subgroup of order $p$ (one exists by [[Group Theory II — §1.3–1.4|Cauchy]]) is a proper non-trivial normal subgroup; if $Z(G) \neq G$ then $Z(G)$ itself is proper, and it is non-trivial by the theorem — either way $G$ has a proper non-trivial normal subgroup and is not simple.

---

# Motivation

A $p$-group is defined by one arithmetic fact — its order is $p^n$ — and the project of §1.5 is to squeeze structural consequences out of that single fact. But arithmetic on its own does not produce *elements*; it does not hand you a particular group element with a particular property. To get traction you need a theorem that converts the integer $p^n$ into the existence of a distinguished element, and that is what this theorem does. It says: the order being a prime power forces the existence of a non-identity element that commutes with everything.

Why is a central element the right thing to extract, rather than, say, an element of order $p$ (which [[Group Theory II — §1.3–1.4|Cauchy's theorem]] already supplies)? Because a central element of order $p$ generates a subgroup $\langle x \rangle \cong C_p$ that is automatically [[Def - Normal Subgroup|normal]] — central elements are fixed by conjugation, so the subgroup they generate is too. A normal subgroup is exactly what you need to form a quotient $G/\langle x \rangle$, and that quotient is a strictly smaller $p$-group. So this theorem is the engine of *induction on the order of a $p$-group*: it manufactures, for free, the normal subgroup you quotient by. Cauchy's element of order $p$ need not be central, so the subgroup it generates need not be normal, and you cannot quotient by it. The word "central" is doing all the work.

The historical and structural payoff is the corollary: no $p$-group of order $p^n$ with $n \geq 2$ is [[Def - Simple Group|simple]]. Since the [[Thm - Composition Series|simple groups are the atoms]] of finite group theory, this rules out an entire infinite family of orders — $p^2, p^3, p^4, \dots$ — as candidate orders for new simple groups, with no case-checking at all. Before this theorem one might worry that some large $p$-group is simple; after it, one knows no $p$-group beyond prime order ever is. The theorem is the reason the prime powers are an "easy" region of the simple-group landscape.

---

# Sources and Targets

This section records the non-obvious ways a problem arrives at the hypothesis (a $p$-group) and the non-obvious results that follow from the conclusion (a non-trivial centre) once combined with one further fact.

**Sources (Input Broadening)**

The hypothesis is "$G$ is a finite $p$-group". The skill is recognising that hypothesis when a problem does not say the words.

The first source is **a group whose order is literally a prime power**. Property $B$ is "$|G| = p^n$", and the bridge to the precondition is immediate — that *is* the definition. The reason it is worth stating is that in practice the order arrives factored as part of a larger problem: you are told $|G| = 16$, or $|G| = 125$, and must notice that $16 = 2^4$ and $125 = 5^3$ are prime powers so the $p$-group theory switches on. Any problem handing you a group of order $p^n$ should trigger "write the class equation".

The second source is **a Sylow $p$-subgroup of an arbitrary finite group**. Property $B$ is "$P$ is a [[Def - Sylow p-Subgroup|Sylow p-subgroup]] of some group $G$ of order $p^a m$". The bridge is that $|P| = p^a$ by definition of Sylow subgroup, so $P$ is itself a $p$-group, and this theorem applies *to $P$* even though $G$ is not a $p$-group. The implication is non-obvious because the ambient group $G$ has nothing prime-power about it; you must zoom in on the subgroup. This is how the non-trivial-centre theorem feeds into Sylow-theoretic arguments: every Sylow $p$-subgroup has a non-trivial centre.

The third source is **a $p$-subgroup arising as a stabiliser or kernel**. Property $B$ is "$H$ is a subgroup of $p$-power order produced by some construction" — a stabiliser of a point under an action, the kernel of a homomorphism, an intersection of $p$-groups. Each such $H$ is a $p$-group, so it has a non-trivial centre. The implication is non-obvious because the construction (stabiliser, kernel) does not advertise the order; you compute $|H|$, see a power of $p$, and the theorem activates.

The fourth source is **a group acting on a set, where the acting group is a $p$-group**. Property $B$ is "$P$ acts on a finite set $X$ and $|P| = p^k$". The theorem itself is one instance of the deeper *fixed-point congruence* $|X^P| \equiv |X| \pmod p$ — apply it with $X = G$ and $P = G$ acting by conjugation and the fixed points are exactly $Z(G)$. Recognising that any $p$-group action carries this congruence is the broadest form of the source.

**Targets (Output Amplification)**

The conclusion is "$Z(G)$ is non-trivial, and $p \mid |Z(G)|$". On its own this is an existence statement; combined with one more property $D$ it becomes a structural result $E$.

The most-used combination is **non-trivial centre plus normality of $Z(G)$ gives non-simplicity**. The conclusion $C$ is "$Z(G) \neq \{e\}$"; add the property $D$ that $Z(G)$ is *always* a [[Def - Normal Subgroup|normal subgroup]] (this is a general fact, true for every group). If moreover $Z(G) \neq G$, then $Z(G)$ is a proper non-trivial normal subgroup, so $E$ is "$G$ is not [[Def - Simple Group|simple]]". The combination is non-obvious only in that one must remember the centre is normal — many people produce a non-trivial centre and stop, not realising it is *already* the normal subgroup the problem wanted.

A second combination is **non-trivial centre plus a central element of order $p$ gives a normal $C_p$ to quotient by**. The conclusion $C$ "$p \mid |Z(G)|$" means $Z(G)$, being a non-trivial group of $p$-power order, contains (by Cauchy applied to $Z(G)$, or by taking a suitable power of any non-identity central element) an element $x$ of order exactly $p$. Add the property $D$ that $x$ is central, so $\langle x \rangle$ is normal. The result $E$ is a normal subgroup $\langle x \rangle \cong C_p$ with $|G/\langle x \rangle| = p^{n-1}$ — the inductive step. This is the combination that powers [[Thm - Subgroups of a p-Group]].

A third combination is **divisibility $p \mid |Z(G)|$ plus a small order forces the centre to be large**. The conclusion $C$ "$p \mid |Z(G)|$" together with the property $D$ "$|G| = p^2$" forces $|Z(G)| \in \{p, p^2\}$. If $|Z(G)| = p$ then $G/Z(G)$ has order $p$, hence is cyclic, hence (by [[Thm - Quotient by the Centre and Commutativity]]) $G$ is abelian and $Z(G) = G$ — a contradiction. So $E$ is "$|Z(G)| = p^2$, i.e. $G$ is abelian": *every group of order $p^2$ is abelian*. The combination is non-obvious because the conclusion $p \mid |Z(G)|$ looks weak, yet pinned against the tiny order $p^2$ it becomes total.

---

# Why Is It True

The intuition has nothing to do with cleverness; it is a counting fact about how a prime divides a sum.

Start from the right mental image. Let $G$ act on itself by conjugation. The orbits of this action are the [[Def - Conjugacy Class|conjugacy classes]], and they partition $G$ — every element lies in exactly one class. An element $x$ lands in a class *all by itself*, a singleton class $\{x\}$, precisely when $gxg^{-1} = x$ for every $g$, that is, precisely when $x$ is central. So the singleton conjugacy classes are exactly the elements of the centre, and $|Z(G)|$ is exactly the number of singleton classes.

Now the prime steps in. By the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]], the size of the conjugacy class of $x$ equals the index $|G : C_G(x)|$, which by [[Thm - Lagrange's Theorem|Lagrange]] divides $|G| = p^n$. So every conjugacy class has size a power of $p$ — and a power of $p$ is either $1$ (if the exponent is zero) or *divisible by $p$* (if the exponent is positive). There is no middle ground. Every conjugacy class is either a singleton or has size cleanly divisible by $p$.

Here is the whole theorem in one sentence. Add up the class sizes; the total is $|G| = p^n$, which is divisible by $p$. The non-singleton classes each contribute a multiple of $p$, so they contribute a multiple of $p$ in total. Subtract: the singleton classes must *also* contribute a multiple of $p$. But the number of singleton classes is $|Z(G)|$. So $p \mid |Z(G)|$.

And $|Z(G)|$ cannot be zero — the identity $e$ is central, its class $\{e\}$ is a singleton, so $|Z(G)| \geq 1$. A positive integer divisible by $p$ is at least $p$. Hence $|Z(G)| \geq p \geq 2$: there is a central element other than the identity.

The reason to *expect* this, before any proof, is the following. Conjugation measures non-commutativity: $x$ has a big conjugacy class exactly when many elements fail to commute with it. In a $p$-group, non-commutativity is "quantised" — every conjugacy class size is a power of $p$, so non-commutativity comes only in chunks of size $p, p^2, \dots$. The identity already occupies one singleton slot. If the centre were *only* the identity, you would have exactly one singleton and all the rest of the $p^n - 1$ remaining elements distributed into classes of size divisible by $p$ — but then $p^n - 1$ would be divisible by $p$, and it is not (it is $\equiv -1 \pmod p$). The arithmetic simply does not balance unless there are more singletons. The centre is forced to grow to make the books add up. That is the honest reason the theorem is true: it is a divisibility audit, and the audit fails for a trivial centre.

---

# What Makes This Hard

The proof is short and the single step people stumble on is recognising that the count of *singleton* conjugacy classes is exactly $|Z(G)|$ — the proof never mentions the centre until that identification, and it is easy to miss that "singleton class" and "central element" are the same condition. The most common error is to claim each non-central class has size *exactly* $p$; it need only have size divisible by $p$ (it could be $p^2$, $p^3$, ...), and the argument needs only divisibility, so claiming exact size $p$ is both false and unnecessary. A secondary slip is forgetting to note $e$ is central, which is what upgrades "$p \mid |Z(G)|$" to "$|Z(G)| \geq p$".

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Let $G$ act on itself by conjugation. Write down the [[Thm - The Class Equation|class equation]] — the partition of $G$ into conjugacy classes — and read it modulo $p$. Every non-singleton class has size divisible by $p$, and $|G|$ is too, so the number of singleton classes is divisible by $p$. That number is $|Z(G)|$, and it is at least $1$ because $e$ is central, hence at least $p$.

**Subgoal decomposition:**

1. **Singleton classes are central elements.** Show that the conjugacy class of $x$ is the singleton $\{x\}$ if and only if $x \in Z(G)$.
   - *Hint:* $\operatorname{ccl}(x) = \{x\}$ means $gxg^{-1} = x$ for all $g$, which rearranges to $gx = xg$ for all $g$ — the definition of central.
   - *Why needed:* It identifies the quantity the class equation will pin down ($\#$ singleton classes) with the quantity you care about ($|Z(G)|$).

2. **Every non-singleton class has size divisible by $p$.** Show that for non-central $x$, the class size $|\operatorname{ccl}(x)|$ is divisible by $p$.
   - *Hint:* By [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser]], $|\operatorname{ccl}(x)| = |G : C_G(x)|$, which divides $|G| = p^n$ by [[Thm - Lagrange's Theorem|Lagrange]]; a divisor of $p^n$ greater than $1$ is a positive power of $p$, hence divisible by $p$.
   - *Why needed:* It makes the non-central part of the class equation a multiple of $p$.

3. **Read the class equation modulo $p$.** Conclude $p \mid |Z(G)|$.
   - *Hint:* $|G| = |Z(G)| + \sum_i |G : C_G(x_i)|$ where the sum runs over non-central class representatives; the left side and every summand are $\equiv 0 \pmod p$, so $|Z(G)| \equiv 0 \pmod p$.
   - *Why needed:* This is the divisibility statement.

4. **Conclude non-triviality.** Note $e \in Z(G)$, so $|Z(G)| \geq 1$; combined with $p \mid |Z(G)|$ this gives $|Z(G)| \geq p \geq 2$, so $Z(G) \neq \{e\}$.
   - *Hint:* The smallest positive multiple of $p$ is $p$ itself.
   - *Why needed:* It upgrades the divisibility to the existence of a non-identity central element — the usable form.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: Singleton conjugacy class if and only if central
> **Statement:** For $x \in G$, the conjugacy class $\operatorname{ccl}(x) = \{gxg^{-1} : g \in G\}$ equals the singleton $\{x\}$ if and only if $x \in Z(G)$.
>
> **Hint:** Unfold both conditions to the same equation $gx = xg$ for all $g$.
>
> **Why needed:** It is the bridge that turns "count the singleton classes" into "compute $|Z(G)|$".
>
> > [!note]- Full proof
> > The class $\operatorname{ccl}(x)$ is the singleton $\{x\}$ if and only if $gxg^{-1} = x$ for every $g \in G$ — that is, every conjugate of $x$ equals $x$. Right-multiplying $gxg^{-1} = x$ by $g$ gives $gx = xg$. So $\operatorname{ccl}(x) = \{x\}$ if and only if $gx = xg$ for all $g \in G$, which is exactly the statement $x \in Z(G)$.

> [!note]- Lemma 2: Non-central conjugacy classes have size divisible by $p$
> **Statement:** Let $G$ be a $p$-group. If $x \in G$ is not central, then $|\operatorname{ccl}(x)|$ is divisible by $p$.
>
> **Hint:** Orbit–stabiliser turns the class size into an index; Lagrange turns the index into a divisor of $p^n$.
>
> **Why needed:** It makes the entire non-central part of the class equation a multiple of $p$.
>
> > [!note]- Full proof
> > Conjugation is an action of $G$ on itself; the orbit of $x$ is $\operatorname{ccl}(x)$ and the stabiliser of $x$ is the [[Def - Centraliser and Centre|centraliser]] $C_G(x)$. By the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]], $|\operatorname{ccl}(x)| = |G : C_G(x)|$. By [[Thm - Lagrange's Theorem|Lagrange]], this index divides $|G| = p^n$, so $|\operatorname{ccl}(x)| = p^k$ for some $0 \leq k \leq n$. Since $x$ is not central, by Lemma 1 the class is not a singleton, so $|\operatorname{ccl}(x)| > 1$, forcing $k \geq 1$. Hence $p \mid p^k = |\operatorname{ccl}(x)|$.

> [!note]- Lemma 3: A non-empty $p$-power-order set has order at least $p$
> **Statement:** If $N$ is a positive integer with $p \mid N$, then $N \geq p$. In particular, if $|Z(G)| \geq 1$ and $p \mid |Z(G)|$, then $|Z(G)| \geq p \geq 2$.
>
> **Hint:** The least positive multiple of $p$ is $p$.
>
> **Why needed:** It converts the divisibility conclusion into the concrete statement that a non-identity central element exists.
>
> > [!note]- Full proof
> > If $p \mid N$ and $N \geq 1$, write $N = pk$ with $k$ a non-negative integer; since $N \geq 1 > 0$ we have $k \geq 1$, so $N = pk \geq p$. The identity $e$ satisfies $eg = ge$ for all $g$, so $e \in Z(G)$ and $|Z(G)| \geq 1$; with $p \mid |Z(G)|$ this gives $|Z(G)| \geq p$, and as $p \geq 2$, the centre contains an element other than $e$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** If $G$ is a finite $p$-group, then $Z(G) \neq \{e\}$; more precisely $p \mid |Z(G)|$.
>
> *Proof.* Let $|G| = p^n$ with $n \geq 1$. Let $G$ act on itself by conjugation, $g \cdot x = gxg^{-1}$. The orbits of this action are precisely the [[Def - Conjugacy Class|conjugacy classes]] of $G$, and they partition $G$.
>
> Each orbit has size dividing $|G| = p^n$. Indeed, the orbit of $x$ is its conjugacy class $\operatorname{ccl}(x)$ and the stabiliser is the centraliser $C_G(x)$, so by the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] $|\operatorname{ccl}(x)| = |G : C_G(x)|$, which divides $p^n$ by [[Thm - Lagrange's Theorem|Lagrange's theorem]]. Hence every conjugacy class has size $p^k$ for some $0 \leq k \leq n$, so each class is either a singleton ($k = 0$) or has size divisible by $p$ ($k \geq 1$).
>
> A conjugacy class is a singleton $\{x\}$ exactly when $gxg^{-1} = x$ for all $g \in G$, i.e. $gx = xg$ for all $g$, i.e. $x \in Z(G)$. So the singleton classes are exactly the one-element sets $\{x\}$ with $x \in Z(G)$, and there are precisely $|Z(G)|$ of them.
>
> Since the conjugacy classes partition $G$, summing their sizes gives $|G|$. Grouping the singleton classes together:
> $$|G| = |Z(G)| + \sum_{i} |G : C_G(x_i)|,$$
> where $x_1, x_2, \dots$ are representatives of the conjugacy classes of size greater than $1$ (one per non-central class). This is the [[Thm - The Class Equation|class equation]].
>
> Read this equation modulo $p$. The left side $|G| = p^n$ is divisible by $p$ since $n \geq 1$. Each summand $|G : C_G(x_i)|$ is the size of a non-singleton class, hence divisible by $p$ by the discussion above. Therefore the remaining term satisfies
> $$|Z(G)| = |G| - \sum_i |G : C_G(x_i)| \equiv 0 \pmod p,$$
> that is, $p \mid |Z(G)|$.
>
> Finally, the identity $e$ commutes with every element, so $e \in Z(G)$ and $|Z(G)| \geq 1$. A positive integer divisible by $p$ is at least $p$, so $|Z(G)| \geq p \geq 2$. Hence $Z(G)$ contains an element other than $e$, i.e. $Z(G) \neq \{e\}$. $\qquad\blacksquare$
>
> **Corollary.** If $|G| = p^n$ with $n \geq 2$, then $G$ is not simple.
>
> *Proof.* The centre $Z(G)$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$ (for any $g \in G$ and $z \in Z(G)$, $gzg^{-1} = z \in Z(G)$, so $Z(G)$ is closed under conjugation). By the theorem, $Z(G) \neq \{e\}$.
>
> If $Z(G) \neq G$, then $Z(G)$ is a proper non-trivial normal subgroup, so $G$ is not [[Def - Simple Group|simple]].
>
> If $Z(G) = G$, then $G$ is abelian. Since $|G| = p^n$ with $n \geq 2$, the order $p^n$ is divisible by the prime $p$, so by [[Group Theory II — §1.3–1.4|Cauchy's theorem]] $G$ contains an element $x$ of order $p$. Then $\langle x \rangle$ has order $p$, so it is proper ($p < p^n$ as $n \geq 2$) and non-trivial; and it is normal because $G$ is abelian (every subgroup of an abelian group is normal). So again $G$ has a proper non-trivial normal subgroup and is not simple.
>
> In both cases $G$ is not simple. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

The aim is to find settings where the theorem applies but is not advertised — testing recognition of the *sources*.

**Linear algebra: the unitriangular matrix group has a non-trivial centre.** The group $U_n(\mathbb{Z}/p)$ of upper-triangular matrices over the field $\mathbb{Z}/p$ with $1$s on the diagonal has order $p^{\binom{n}{2}}$, a prime power, so it is a $p$-group and the theorem says its centre is non-trivial. One can then *identify* the centre — it is the matrices differing from the identity only in the top-right corner — but the *existence* of a non-trivial centre is free from this theorem. The application is non-obvious because the problem looks like linear algebra (matrices, triangularity) with no mention of prime powers; property $B$ is the order count $p^{\binom{n}{2}}$.

**Number theory and combinatorics: fixed points of a $p$-group action and Cauchy's theorem.** The deeper statement underneath this theorem is the fixed-point congruence: a $p$-group $P$ acting on a finite set $X$ satisfies $|X^P| \equiv |X| \pmod p$ — the present theorem is the case $X = G$, $P = G$, conjugation. Recognising this lets you prove Cauchy's theorem itself: let $C_p$ act by cyclic rotation on the set of $p$-tuples $(g_1, \dots, g_p)$ from $G$ with product $e$; the set has size $|G|^{p-1}$, and if $p \mid |G|$ the congruence forces extra fixed points beyond the constant tuple $(e, \dots, e)$, each of which is an element of order $p$. The application is non-obvious because the acting group $C_p$ is small and artificially introduced — the source is "some $p$-group acts on some cleverly chosen set".

**Sylow theory: every Sylow $p$-subgroup of any finite group has non-trivial centre.** Take any finite group $G$ of order $p^a m$ with $p \nmid m$, however large and unstructured, and let $P$ be a [[Def - Sylow p-Subgroup|Sylow p-subgroup]]. Then $|P| = p^a$, so $P$ is a $p$-group and $Z(P) \neq \{e\}$ — even though $G$ itself need not have a non-trivial centre at all (the symmetric group $S_n$ for $n \geq 3$ has trivial centre). The application is non-obvious because $G$'s order is not a prime power; you must restrict attention to the subgroup $P$. This is the routine first step in many Sylow arguments — for instance, in showing the normaliser of a Sylow subgroup is its own normaliser.

---

# Bridges

- **[[Thm - The Class Equation|The Class Equation]]** — this theorem is essentially a single corollary of the class equation: it is the class equation $|G| = |Z(G)| + \sum |G : C_G(x_i)|$ read modulo the prime $p$. The class equation is the general tool (valid for any finite group, partitioning it into conjugacy classes); the non-trivial-centre theorem is what that tool yields the instant the order is a prime power, when divisibility by $p$ collapses all the non-central terms.

- **[[Thm - Quotient by the Centre and Commutativity|Quotient by the Centre and Commutativity]]** — these two theorems are a matched pair and are almost always used together. This one *produces* a non-trivial centre; the other says *what a large centre forces* (if $G/Z(G)$ is cyclic then $G$ is abelian). Their combination is the proof that every group of order $p^2$ is abelian, and more generally they are the two halves of every induction on the order of a $p$-group.

- **[[Thm - Subgroups of a p-Group|Subgroups of a p-Group]]** — this theorem is the base ingredient of the subgroup theorem's inductive step: the non-trivial centre supplies a central element of order $p$, hence a *normal* subgroup $C_p$ to quotient by. Without a non-trivial centre there would be no guaranteed normal subgroup to start the induction, and the subgroup theorem would have no proof.

- **Cauchy's theorem** *(from [[Group Theory II — §1.3–1.4]])* — Cauchy says a prime dividing $|G|$ yields an element of *that* order; this theorem says a $p$-group yields a *central* element. Cauchy is what you apply *to the centre* $Z(G)$ — itself a non-trivial $p$-group — to extract a central element of order exactly $p$. The two theorems compose: Cauchy gives order, this theorem gives centrality, and the conjunction gives the normal $C_p$.

- **The fixed-point congruence** — the broadest frame: a $p$-group $P$ acting on a finite set $X$ has $|X^P| \equiv |X| \pmod p$. The non-trivial-centre theorem is the conjugation action ($X = G$); [[Thm - Sylow's Theorems|Sylow's theorems]] are this same congruence deployed against other carefully chosen sets. Seeing all of §1.5 and §1.7 as instances of one congruence is the unifying insight of the chapter.

# Unlocked by This

> [!tip] Nilpotent Groups *(from Group Theory / Galois Theory)*
> Iterating this theorem builds the **upper central series** $\{e\} \trianglelefteq Z(G) \trianglelefteq Z_2(G) \trianglelefteq \cdots$, where each $Z_{k+1}(G)/Z_k(G)$ is the centre of $G/Z_k(G)$. Because every non-trivial $p$-group has a non-trivial centre, this series strictly increases until it reaches $G$ — so every finite $p$-group is **nilpotent**, hence solvable. Nilpotence is the structural reason $p$-groups are the tractable, "layered" subclass of finite groups.
