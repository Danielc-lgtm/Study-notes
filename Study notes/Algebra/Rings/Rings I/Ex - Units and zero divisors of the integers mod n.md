---
type: exercise
subject: ring-theory
difficulty: "⭐"
prereqs:
  - "Def - Ring"
  - "Def - Unit and Field"
  - "Def - Characteristic of a Ring"
tags: [algebra, ring-theory]
---

# Problem Statement

Fix an integer $n \geq 2$ and work in the ring $\mathbb{Z}/n\mathbb{Z}$ of integers modulo $n$, whose elements are the residue classes $\overline{0}, \overline{1}, \dots, \overline{n-1}$ with addition and multiplication carried out modulo $n$.

1. Determine exactly which elements of $\mathbb{Z}/n\mathbb{Z}$ are **units**. Show that $\overline{a}$ is a unit if and only if $\gcd(a, n) = 1$.
2. Determine exactly which elements are **zero divisors**. Show that the zero divisors are precisely the nonzero residues $\overline{a}$ with $\gcd(a, n) > 1$ — so every nonzero element of $\mathbb{Z}/n\mathbb{Z}$ is either a unit or a zero divisor, and never both.
3. Deduce that $\mathbb{Z}/n\mathbb{Z}$ is a field if and only if $n$ is prime.

**Recall:**

The objects in play are a ring, the units inside it, the zero divisors inside it, and the notion of a field.

A [[Def - Ring|ring]] $R$ is a set with two operations $+$ and $\cdot$: it is an abelian group under $+$, the multiplication is associative with an identity $1_R$, and multiplication distributes over addition. In this course every ring is commutative. The ring $\mathbb{Z}/n\mathbb{Z}$ has underlying set the $n$ residue classes modulo $n$; the class of an integer $a$ is written $\overline{a}$, and $\overline{a} = \overline{b}$ exactly when $n \mid (a - b)$.

A [[Def - Unit and Field|unit]] of a ring $R$ is an element $u$ for which there exists $v \in R$ with $u \cdot v = 1_R$; the element $v$ is the (multiplicative) inverse of $u$. Whether an element is a unit depends on the ambient ring, not on the element alone.

A **zero divisor** of $R$ is a *nonzero* element $a$ for which there exists a *nonzero* element $b$ with $a \cdot b = 0_R$. The requirement that both factors be nonzero is what makes the notion non-trivial: it detects a genuine failure of cancellation.

A [[Def - Unit and Field|field]] is a nonzero ring in which every nonzero element is a unit. Equivalently, a field is a commutative ring with $1 \neq 0$ in which one can divide by anything except $0$.

The number-theoretic input is **Bézout's identity**: for integers $a$ and $n$, the greatest common divisor $d = \gcd(a, n)$ can be written as an integer combination $d = xa + yn$ for some $x, y \in \mathbb{Z}$. In particular $\gcd(a, n) = 1$ if and only if there exist integers $x, y$ with $xa + yn = 1$.

---

# Convergent Strategy

**Problem class.** This is a *classify the elements of a concrete ring by their multiplicative behaviour* problem. The topic's [[Rings I — §2.1–2.2#Problem-Solving Strategy|problem-solving strategy]] says that when a ring is presented concretely — here as residues modulo $n$ — the productive move is to translate every ring-theoretic question ("is $\overline{a}$ a unit?") into the arithmetic of the integers, where divisibility and the greatest common divisor are computable.

**Assumption pattern.** The only structure is the modulus $n$. Everything about $\mathbb{Z}/n\mathbb{Z}$ — which elements are units, which are zero divisors, whether it is a field — is controlled by the *divisors of $n$*. The single dial is the factorisation of $n$, and the cleanest position of that dial, "$n$ prime", is exactly the field case.

**Theorem routing.** The bridge from ring theory to arithmetic is **Bézout's identity**. A unit is an element $\overline{a}$ admitting $\overline{x}$ with $\overline{a}\,\overline{x} = \overline{1}$, which unwinds to the *integer* congruence $ax \equiv 1 \pmod n$, i.e. $ax + yn = 1$ for some integers $x, y$. Bézout says this is solvable exactly when $\gcd(a, n) = 1$. That single equivalence answers part 1 outright, and parts 2 and 3 are squeezed out of it by a counting argument and a case split.

**Key decision point.** The genuine idea is the **dichotomy**: in $\mathbb{Z}/n\mathbb{Z}$ every nonzero element is *either* a unit *or* a zero divisor, with no third possibility and no overlap. The non-obvious half is that an element which *fails* to be a unit is automatically *forced* to be a zero divisor — failure of invertibility is not a passive defect but produces a concrete nonzero element that multiplies it to $0$. Spotting that "not a unit" actively manufactures a zero divisor is what makes part 2 work and what makes the field criterion of part 3 sharp.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings I — §2.1–2.2#Legal Operations|the topic page's Legal Operations]]:

1. **Translate a question about $\mathbb{Z}/n\mathbb{Z}$ into a congruence in $\mathbb{Z}$.** Every statement about residue classes — equality, the equation $\overline{a}\,\overline{x} = \overline{1}$, the equation $\overline{a}\,\overline{b} = \overline{0}$ — is rewritten as a divisibility statement about ordinary integers. This is the operation that exposes the arithmetic skeleton of the ring.

2. **Apply Bézout's identity to convert a coprimality hypothesis into an explicit linear combination.** The statement $\gcd(a, n) = 1$ is replaced by a usable equation $xa + yn = 1$; reducing that equation modulo $n$ produces the inverse of $\overline{a}$ directly.

3. **Use a counting / pigeonhole argument on a finite ring.** Because $\mathbb{Z}/n\mathbb{Z}$ is finite, the multiplication-by-$\overline{a}$ map is injective if and only if it is surjective. This lets a *non-injective* map (a witnessed zero divisor) be detected, and lets a *non-surjective* map (failure to hit $\overline{1}$) be promoted to non-injectivity, hence to a zero divisor.

4. **Build a field by verifying every nonzero element is a unit** (the definition of a field, used as a checklist). Part 3 is exactly this operation: once parts 1 and 2 pin down the units, the field criterion is read off.

---

# Hints

> [!note]- Hint 1
> Do not think about $\mathbb{Z}/n\mathbb{Z}$ as an abstract ring. The element $\overline{a}$ is a unit means there is some $\overline{x}$ with $\overline{a}\,\overline{x} = \overline{1}$. Rewrite that equation as a statement about ordinary integers: it says $ax \equiv 1 \pmod{n}$, i.e. there is an integer $y$ with $ax + yn = 1$. What classical theorem tells you exactly when an equation $ax + yn = 1$ has an integer solution?

> [!note]- Hint 2
> Bézout's identity: integers $x, y$ with $ax + yn = 1$ exist if and only if $\gcd(a, n) = 1$. That settles part 1 completely. For part 2, take a residue $\overline{a} \neq \overline{0}$ that is *not* a unit, so $d = \gcd(a, n)$ satisfies $1 < d < n$. Look at the residue of $n/d$. Compute $\overline{a} \cdot \overline{n/d}$ — what is $a \cdot (n/d)$ modulo $n$, and is $\overline{n/d}$ nonzero?

> [!note]- Hint 3
> If $d = \gcd(a, n) > 1$, write $n = d \cdot k$ with $1 \le k < n$, so $\overline{k} \neq \overline{0}$. Since $d \mid a$, write $a = d \cdot m$. Then $a k = d m k = m \cdot (d k) = m n$, which is $\equiv 0 \pmod n$. So $\overline{a}\,\overline{k} = \overline{0}$ with $\overline{k} \neq \overline{0}$: $\overline{a}$ is a zero divisor. No nonzero element can be both — a unit times anything nonzero is nonzero — so each nonzero residue is exactly one of the two.

> [!note]- Hint 4
> For part 3, a field is a nonzero ring in which *every* nonzero element is a unit. By parts 1 and 2 the nonzero non-units are exactly the $\overline{a}$ with $\gcd(a, n) > 1$. The field condition is therefore: *no* residue $\overline{a}$ with $1 \le a \le n - 1$ shares a factor with $n$. When is that true? Exactly when $n$ has no divisors strictly between $1$ and $n$ — that is, when $n$ is prime.

---

# Solution

The plan is to convert "$\overline{a}$ is a unit" into the solvability of $ax + yn = 1$, settle that with Bézout's identity, then show every non-unit nonzero residue is forced to be a zero divisor, and finally read off the field criterion.

**Step 1: $\overline{a}$ is a unit if and only if $\gcd(a, n) = 1$.**

The equation $\overline{a}\,\overline{x} = \overline{1}$ in $\mathbb{Z}/n\mathbb{Z}$ is the integer statement $ax \equiv 1 \pmod n$, equivalently $ax + yn = 1$ for some integer $y$. By Bézout's identity such $x, y$ exist precisely when $\gcd(a, n) = 1$. Hence the units of $\mathbb{Z}/n\mathbb{Z}$ are exactly the classes $\overline{a}$ with $a$ coprime to $n$.

> [!note]- Derivation
> By definition $\overline{a}$ is a unit of $\mathbb{Z}/n\mathbb{Z}$ if there exists a residue $\overline{x}$ with $\overline{a} \cdot \overline{x} = \overline{1}$. Multiplication of residue classes is defined by $\overline{a} \cdot \overline{x} = \overline{ax}$, so this equation says $\overline{ax} = \overline{1}$, which by the definition of equality of residue classes means
> $$n \mid (ax - 1), \qquad \text{i.e.} \qquad ax - 1 = -yn \ \text{ for some integer } y.$$
> Rearranged, the condition is the existence of integers $x, y$ with
> $$ax + yn = 1.$$
> Now invoke **Bézout's identity**: for any integers $a, n$, the set of integer values of the linear form $ax + yn$ (as $x, y$ range over $\mathbb{Z}$) is exactly the set of multiples of $d = \gcd(a, n)$. In particular the value $1$ is attainable if and only if $d \mid 1$, i.e. if and only if $d = 1$.
>
> Therefore: such $x$ exists $\iff \gcd(a, n) = 1$. When it exists, the very integer $x$ produced by Bézout reduces to a residue $\overline{x}$ that is the inverse of $\overline{a}$ — the inverse is not merely shown to exist, it is computed by the extended Euclidean algorithm. So the unit group is
> $$(\mathbb{Z}/n\mathbb{Z})^\times = \{\, \overline{a} : 1 \le a \le n,\ \gcd(a, n) = 1 \,\}.$$

**Step 2: every nonzero non-unit is a zero divisor; no element is both.**

If $\overline{a} \neq \overline{0}$ and $\overline{a}$ is *not* a unit, then $d = \gcd(a, n)$ satisfies $d > 1$. Writing $n = dk$ with $1 \le k < n$ gives a nonzero residue $\overline{k}$ with $\overline{a}\,\overline{k} = \overline{0}$, so $\overline{a}$ is a zero divisor. Conversely a unit can never be a zero divisor. Hence each nonzero residue is *exactly one* of unit / zero divisor.

> [!note]- Derivation
> Let $\overline{a} \neq \overline{0}$, so $n \nmid a$, and suppose $\overline{a}$ is not a unit. By Step 1, $d := \gcd(a, n) \neq 1$, so $d > 1$. Also $d \mid n$ and $d \le n$; and $d \neq n$, because $d \mid a$ would then force $n \mid a$, contradicting $\overline{a} \neq \overline{0}$. Thus $1 < d < n$.
>
> Set $k := n / d$. Since $1 < d < n$ we have $1 \le k < n$, so $\overline{k} \neq \overline{0}$. Because $d \mid a$, write $a = dm$ for an integer $m$. Then
> $$ak \;=\; (dm)\,k \;=\; m\,(dk) \;=\; m\,n,$$
> which is a multiple of $n$, so $\overline{a}\,\overline{k} = \overline{ak} = \overline{mn} = \overline{0}$. With $\overline{k} \neq \overline{0}$, this exhibits $\overline{a}$ as a **zero divisor**.
>
> For the "no element is both" claim: suppose $\overline{a}$ is a unit, with inverse $\overline{x}$, and suppose $\overline{a}\,\overline{b} = \overline{0}$. Multiply by $\overline{x}$:
> $$\overline{b} = \overline{1} \cdot \overline{b} = (\overline{x}\,\overline{a})\,\overline{b} = \overline{x}\,(\overline{a}\,\overline{b}) = \overline{x} \cdot \overline{0} = \overline{0}.$$
> So a unit annihilates only $\overline{0}$ and cannot be a zero divisor (which would require a *nonzero* $\overline{b}$). Combined with the previous paragraph, every nonzero residue is a unit or a zero divisor, and the two classes are disjoint. (The element $\overline{0}$ is excluded from both by definition.)

**Step 3: $\mathbb{Z}/n\mathbb{Z}$ is a field if and only if $n$ is prime.**

A field is a nonzero ring all of whose nonzero elements are units. By Steps 1–2 the nonzero non-units are exactly the $\overline{a}$ with $1 < \gcd(a, n)$. There are none of those precisely when $n$ has no divisor strictly between $1$ and itself — that is, when $n$ is prime.

> [!note]- Derivation
> $\mathbb{Z}/n\mathbb{Z}$ is nonzero because $n \ge 2$ forces $\overline{1} \neq \overline{0}$. So it is a field exactly when every nonzero residue is a unit.
>
> *If $n$ is prime.* Take any $\overline{a} \neq \overline{0}$, so $1 \le a \le n - 1$. The divisors of $n$ are only $1$ and $n$; since $a < n$, the common divisor $\gcd(a, n)$ cannot be $n$, so $\gcd(a, n) = 1$. By Step 1, $\overline{a}$ is a unit. Every nonzero residue is a unit, so $\mathbb{Z}/n\mathbb{Z}$ is a field.
>
> *If $n$ is composite.* Then $n = d k$ with $1 < d < n$ and $1 < k < n$. The residue $\overline{d}$ is nonzero ($d < n$), and $\gcd(d, n) = d > 1$, so by Step 1 $\overline{d}$ is *not* a unit — indeed by Step 2 it is a zero divisor, with $\overline{d}\,\overline{k} = \overline{dk} = \overline{n} = \overline{0}$. A field has no zero divisors (a zero divisor is never a unit, by Step 2), so $\mathbb{Z}/n\mathbb{Z}$ is not a field.
>
> Hence $\mathbb{Z}/n\mathbb{Z}$ is a field $\iff n$ is prime. When $n = p$ is prime the field is written $\mathbb{F}_p$. $\blacksquare$

> [!note]- Complete formal solution
> Fix $n \ge 2$.
>
> **Units.** $\overline{a}$ is a unit of $\mathbb{Z}/n\mathbb{Z}$ iff there is $\overline{x}$ with $\overline{a}\,\overline{x} = \overline{1}$, i.e. $\overline{ax} = \overline{1}$, i.e. $n \mid (ax - 1)$, i.e. there are integers $x, y$ with $ax + yn = 1$. By Bézout's identity the linear form $ax + yn$ takes the value $1$ iff $\gcd(a, n) = 1$. Therefore
> $$(\mathbb{Z}/n\mathbb{Z})^\times = \{\, \overline{a} : \gcd(a, n) = 1 \,\}.$$
>
> **Zero divisors.** Let $\overline{a} \neq \overline{0}$ be a non-unit; then $d := \gcd(a, n)$ satisfies $1 < d < n$ (it is $> 1$ since $\overline{a}$ is not a unit, and $< n$ since $\overline{a} \neq \overline{0}$ forbids $n \mid a$). Put $k := n/d$, so $1 \le k < n$ and $\overline{k} \neq \overline{0}$. Writing $a = dm$, we get $ak = m(dk) = mn$, hence $\overline{a}\,\overline{k} = \overline{0}$ with $\overline{k} \neq \overline{0}$: $\overline{a}$ is a zero divisor. Conversely if $\overline{a}$ is a unit with inverse $\overline{x}$ and $\overline{a}\,\overline{b} = \overline{0}$, then $\overline{b} = \overline{x}\,\overline{a}\,\overline{b} = \overline{0}$, so a unit is never a zero divisor. Thus each nonzero residue is exactly one of: a unit ($\gcd(a,n) = 1$) or a zero divisor ($\gcd(a,n) > 1$).
>
> **Field criterion.** $\mathbb{Z}/n\mathbb{Z}$ is a nonzero ring, so it is a field iff every nonzero residue is a unit, iff no nonzero residue has $\gcd(a, n) > 1$, iff $n$ has no divisor $d$ with $1 < d < n$, iff $n$ is prime. $\blacksquare$

---

# Key Takeaways

**A concrete ring is best understood by translating every ring question into the arithmetic it is built from.** The ring $\mathbb{Z}/n\mathbb{Z}$ looks like a self-contained algebraic object, but every question one can ask of it — is this element a unit, a zero divisor, is the whole thing a field — is secretly a question about the integers and their divisibility. The reusable instinct is: *when a ring is presented as a quotient or as a concrete set of representatives, do not reason inside the ring; lift the equation back to the parent structure where you have tools.* The equation $\overline{a}\,\overline{x} = \overline{1}$ became $ax + yn = 1$, an object Bézout's identity can dispatch. The same lifting works for $R[X]/(f)$ — questions about that ring become questions about polynomial division and remainders — and for any quotient $R/I$, where ring questions become questions about membership in the ideal $I$. The skill is recognising the quotient presentation as an invitation to compute upstairs.

**Bézout's identity is the universal bridge between "coprime" and "invertible".** Coprimality, $\gcd(a, n) = 1$, is a *divisibility* statement; invertibility of $\overline{a}$ is a *ring-theoretic* statement; Bézout is the single theorem that welds them, because it converts the greatest common divisor into an explicit linear combination $xa + yn = \gcd(a, n)$. Reducing that combination modulo $n$ literally hands you the inverse — the proof is constructive, not merely existential, and the extended Euclidean algorithm is the construction. This pattern recurs throughout algebra: in any principal ideal domain the gcd is a Bézout combination, so "coprime" and "the ideal they generate is everything" and "invertible modulo the other" are all the same statement. Whenever you meet a coprimality hypothesis, your first move should be to make it concrete as a linear combination equal to $1$; that equation is almost always the engine of the proof.

**In a finite commutative ring, "not a unit" is not a passive defect — it actively manufactures a zero divisor.** The most surprising content of this exercise is the dichotomy: a nonzero element of $\mathbb{Z}/n\mathbb{Z}$ that fails to be invertible is *forced* to be a zero divisor, and the proof produces the annihilating partner explicitly ($\overline{n/d}$). The structural reason is finiteness: multiplication by $\overline{a}$ is a map of the finite set $\mathbb{Z}/n\mathbb{Z}$ to itself, and for finite sets injective and surjective coincide; if the map misses $\overline{1}$ it cannot be surjective, hence cannot be injective, hence collapses two elements, and their difference is a nonzero element sent to $\overline{0}$. So in *any* finite commutative ring every element is either a unit or a zero divisor — a clean trichotomy-collapsed-to-dichotomy that fails badly in infinite rings, where $\mathbb{Z}$ supplies elements like $2$ that are neither. The transferable lesson is that finiteness converts failure of one good property into the active presence of a bad one, and this pigeonhole-style argument is the standard route to producing zero divisors on demand.

**A field is the position where the unit/zero-divisor dichotomy degenerates — and "$n$ prime" is exactly that position.** Once you know every nonzero element is a unit or a zero divisor, "field" is the extreme case where the zero-divisor class is *empty*: nothing is left over once the units are removed. The field criterion for $\mathbb{Z}/n\mathbb{Z}$ is therefore a statement purely about the divisor lattice of $n$ — no residue may share a factor with $n$ — which is the definition of primality. This is a recurring template: an algebraic "perfection" property (being a field, being an integral domain, being simple) usually translates into the *absence* of some lattice of sub-objects (no proper divisors, no zero divisors, no proper ideals). Recognising that a maximality or perfection condition is really an emptiness condition on a poset of obstructions lets you reduce many classification problems to combinatorics. Here it tells you instantly that $\mathbb{Z}/n\mathbb{Z}$ is a field for $n = 2, 3, 5, 7, \dots$ and merely a ring with zero divisors for $n = 4, 6, 8, 9, \dots$, and it generalises: $\mathbb{Z}/n\mathbb{Z}$ is an integral domain iff it is a field iff $n$ is prime, because for finite rings "no zero divisors" already forces "field".
