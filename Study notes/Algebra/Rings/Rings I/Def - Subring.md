---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
tags: [algebra, ring-theory]
---

# Notation

For a [[Def - Ring|ring]] $(R, +, \cdot, 0_R, 1_R)$ and a subset $S \subseteq R$, we write $S \leq R$ to mean "$S$ is a subring of $R$". The two distinguished elements are the additive identity $0_R$ and the multiplicative identity $1_R$; a subring must contain *both*. The additive inverse of $r$ is $-r$. The square-bracket notation $R[\alpha]$ — as in $\mathbb{Z}[i]$ or $\mathbb{Q}[\sqrt{2}]$ — denotes the smallest subring of an ambient ring containing $R$ and the element $\alpha$; it is treated informally here and made precise once [[Def - Polynomial Ring|polynomial rings]] are available. See [[Rings I — §2.1–2.2]] for the full registry.

---

# Axiom Motivation

We have a [[Def - Ring|ring]] $R$, and we want to name its **substructures** — subsets of $R$ that are themselves rings, using the *same* addition and multiplication. The motive is the same as for [[Def - Subgroup|subgroups]] of a group: a ring is a large and intricate object, and the first handle on it is the collection of smaller rings sitting inside. The chain $\mathbb{Z} \leq \mathbb{Q} \leq \mathbb{R} \leq \mathbb{C}$ is the picture to hold in mind — four genuinely different number systems, each living inside the next, each a ring in its own right under the operations of the larger one.

So the desideratum is sharp: $S \subseteq R$ should be a **subring** exactly when $(S, +|_S, \cdot|_S, 0_R, 1_R)$ — the set $S$ with the operations of $R$ restricted to it — is itself a ring. The definition is just the unpacking of "the restricted operations make $S$ a ring". Walk through the [[Def - Ring|ring axioms]] one at a time and ask what each demands of $S$.

First, the operations must not *leave* $S$. The ring's addition and multiplication are functions into $R$; restricted to $S \times S$ they must land back in $S$ for them to be operations *on* $S$. So we demand **closure under addition and under multiplication**: $a, b \in S \implies a + b \in S$ and $a \cdot b \in S$. Drop either and the restricted "operation" is not a function $S \times S \to S$, and $S$ cannot be a ring for the trivial reason that there is no operation. But closure of $+$ is not enough to make $(S, +)$ an abelian group — a subset of an abelian group is a subgroup only if it is also a [[Def - Subgroup|subgroup]], which additionally requires the additive identity and additive inverses. So we demand **closure under additive inverses**: $a \in S \implies -a \in S$. Just as for subgroups, in the *additive* group this is genuinely independent of closure under $+$: the subset $\mathbb{N}$ of $(\mathbb{Z}, +)$ is closed under addition but $-1 \notin \mathbb{N}$, so $\mathbb{N}$ is not a subring of $\mathbb{Z}$. This is the precise reason subtraction must be checked: a subring is a subset closed under $+$, $\cdot$, and *negation*.

Next, the identities. A ring has a $0_R$ and a $1_R$, and a subring must have both. We demand $0_R \in S$ and $1_R \in S$. The additive identity $0_R$ is automatic from the others by a short cancellation argument — if $S$ is non-empty and closed under $+$ and negation, then $s + (-s) = 0_R \in S$ — but it does no harm to list it, and it forbids $S = \emptyset$. The multiplicative identity $1_R$, by contrast, is **not** automatic and demanding it is a real choice. This course requires every ring to have a $1$, so a subring, being a ring, must have a multiplicative identity; and we insist it be the *same* $1_R$ as the ambient ring. This single requirement, "$1_R \in S$", is the one clause that most sharply distinguishes a subring from a related-looking notion. The set of even integers $2\mathbb{Z}$ is closed under $+$, under $\cdot$, and under negation, and it forms a perfectly good abelian group and a structure on which multiplication is associative and distributes — yet $1 \notin 2\mathbb{Z}$, so $2\mathbb{Z}$ is **not** a subring of $\mathbb{Z}$. What goes wrong if we drop the "$1_R \in S$" clause is exactly this: we would let in subsets like $2\mathbb{Z}$ that are "rings without a $1$", and the whole convention that rings are unital would silently break for subrings.

The remaining axioms — associativity and commutativity of $+$, associativity and commutativity of $\cdot$, distributivity — need **no separate clause at all**. They are universally quantified identities, "for all" equations, and a "for all" equation true throughout $R$ is automatically true throughout any subset $S$. This is the central economy of substructures, identical to the subgroup story: the hardest-looking axioms come along for free, and a subring is specified *purely by closure conditions* — closed under $+$, closed under $\cdot$, closed under negation, contains $0_R$ and $1_R$ — never by re-verifying any identity.

One could ask whether to *weaken* the definition by dropping the demand that $S$ contain $1_R$, or *strengthen* it by demanding $S$ be closed under division. Weakening lets in $2\mathbb{Z}$ and breaks the unital convention, as just discussed. Strengthening — closure under inverses for units — is exactly the notion of a **subfield**, a strictly stronger thing; $\mathbb{Z}$ is a subring of $\mathbb{Q}$ but not a subfield of it, since $\tfrac{1}{2} \in \mathbb{Q}$ but $\tfrac{1}{2} \notin \mathbb{Z}$. The subring definition deliberately sits at "closed under the ring operations", no more and no less, so that $\mathbb{Z} \leq \mathbb{Q}$ counts.

In summary: a subring must be closed under addition, multiplication, and additive inverses (so the operations restrict and the additive part is a [[Def - Subgroup|subgroup]]), and must contain both $0_R$ and the *same* $1_R$ (so it is a unital ring in this course's sense); all the identity-axioms — associativity, commutativity, distributivity — are inherited for free.

---

# The Definition

Let $(R, +, \cdot, 0_R, 1_R)$ be a [[Def - Ring|ring]]. A subset $S \subseteq R$ is a **subring** of $R$, written $S \leq R$, if:

1. $0_R \in S$ and $1_R \in S$;
2. for all $a, b \in S$, $\quad a + b \in S$ and $a \cdot b \in S$ (closure under both operations);
3. for all $a \in S$, $\quad -a \in S$ (closure under additive inverses).

Equivalently: $(S, +|_S, \cdot|_S, 0_R, 1_R)$ is itself a ring under the operations of $R$ restricted to $S$. Conditions 1–3 are exactly what is needed for the restricted operations to make $S$ a ring, since associativity, commutativity, and distributivity are universally quantified identities inherited from $R$ automatically.

**Subring criterion (one-step test).** A subset $S \subseteq R$ is a subring if and only if $1_R \in S$ and, for all $a, b \in S$,
$$a - b \in S \qquad \text{and} \qquad a \cdot b \in S.$$
The clause $a - b \in S$ is the [[Def - Subgroup|subgroup criterion]] for $(S, +)$ — it delivers $0_R \in S$, closure under negation, and closure under addition in one stroke — and "$1_R \in S$" then upgrades the additive subgroup to a unital subring.

> [!note]- Why the criterion is equivalent
> If $S$ is a subring then $1_R \in S$ by (1), and for $a, b \in S$ we have $-b \in S$ by (3) hence $a - b = a + (-b) \in S$ by (2), and $a \cdot b \in S$ by (2). Conversely, suppose $1_R \in S$ and $S$ is closed under $a - b$ and $a \cdot b$. Since $1_R \in S$, the set $S$ is non-empty. The condition $a - b \in S$ is exactly the subgroup criterion, so $(S, +)$ is a [[Def - Subgroup|subgroup]] of the abelian group $(R, +)$: it contains $0_R$ (take $a = b$), is closed under negation (take $a = 0_R$, giving $-b \in S$), and is closed under addition (since $a + b = a - (-b)$). Multiplication is closed by hypothesis, and associativity, commutativity, and distributivity are inherited. So $S$ is a subring.

---

# Categorical Definition

The clean categorical statement is that a subring is the data of an **injective [[Def - Ring Homomorphism|ring homomorphism]]** $\iota : S \hookrightarrow R$, considered up to relabelling of $S$. A ring homomorphism is a map preserving both operations *and* the identities — $\iota(a + b) = \iota(a) + \iota(b)$, $\iota(a b) = \iota(a)\iota(b)$, and crucially $\iota(1_S) = 1_R$. If $S \leq R$ then the inclusion $s \mapsto s$ is exactly such an injective homomorphism: the subring conditions say precisely that inclusion preserves $+$, $\cdot$, $0_R$, and $1_R$. Conversely, the image of any injective ring homomorphism $\iota : S \to R$ is a subring of $R$ isomorphic to $S$. The condition "$\iota(1_S) = 1_R$", baked into the definition of ring homomorphism, is the categorical shadow of the "$1_R \in S$" clause — and it is why structures like $2\mathbb{Z}$, which receive no unit-preserving map into $\mathbb{Z}$, are not subrings. So "subring of $R$" and "isomorphism class of injective ring homomorphisms into $R$" are the same notion; subrings are the **subobjects** of $R$ in the category $\mathbf{CRing}$ of commutative unital rings.

---

# Relate to Other Fields / Compression

A subring is the **same construction as a [[Def - Subgroup|subgroup]] or a linear subspace, transported to the category of rings**: a subset on which the ambient operations restrict to give a structure of the same kind, which forces closure under each operation and under taking inverses where the structure has them. A linear subspace is closed under vector addition and scalar multiplication and contains $0$; a subgroup is closed under the group operation and inverses and contains $e$; a subring is closed under $+$, $\cdot$, and negation and contains $0_R$ and $1_R$. The recurring economy is identical in every case: universally quantified *identities* are inherited gratis, so a substructure is always pinned down purely by *closure*.

The contrast that genuinely matters is with the [[Def - Ideal|ideal]], the *other* ring-theoretic substructure, and the two are not variants of one idea but near-opposites. A subring must contain $1_R$ and need only be closed under multiplication by *its own elements*. An ideal $I \trianglelefteq R$, by contrast, generally does **not** contain $1_R$ — indeed an ideal containing $1_R$ is the whole ring — and is closed under multiplication by *every* element of the ambient ring, the absorption property $r \in R, x \in I \implies rx \in I$. So a subring is "small but unital and self-contained", whereas an ideal is "absorbing but typically non-unital". The even integers $2\mathbb{Z}$ are the cleanest illustration: $2\mathbb{Z}$ is **not** a subring of $\mathbb{Z}$ (it misses $1$), but it **is** an ideal of $\mathbb{Z}$ (multiplying an even number by any integer keeps it even). The two notions detect different things — subrings are the sub-number-systems, ideals are the kernels of [[Def - Ring Homomorphism|homomorphisms]] and the engines of [[Def - Quotient Ring|quotient rings]] — and conflating them is the single most common beginner's error in ring theory.

---

# Examples / Corollaries

**Is an instance: $\mathbb{Z} \leq \mathbb{Q} \leq \mathbb{R} \leq \mathbb{C}$.** The standard chain of number systems. Each set is closed under the addition, multiplication, and negation of the next, and each contains $0$ and $1$, so each is a subring of the one to its right; by transitivity (see the corollary below) $\mathbb{Z}$ is a subring of $\mathbb{C}$. This is the prototype example, and it shows that "subring" is the relation that organizes the number systems into a tower. Note that although $\mathbb{Q} \leq \mathbb{R}$ as rings, $\mathbb{Q}$ is also a *subfield* of $\mathbb{R}$, a strictly stronger relation; $\mathbb{Z} \leq \mathbb{Q}$ is a subring relation that is **not** a subfield relation.

**Is an instance: the Gaussian integers $\mathbb{Z}[i] \leq \mathbb{C}$.** The set $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ is a subring of $\mathbb{C}$. Apply the criterion: $1 = 1 + 0i \in \mathbb{Z}[i]$; the difference $(a + bi) - (c + di) = (a-c) + (b-d)i$ has integer coefficients; and the product $(a+bi)(c+di) = (ac - bd) + (ad + bc)i$ also has integer coefficients. So $\mathbb{Z}[i]$ is closed under subtraction and multiplication and contains $1$ — it is a subring. It probes the criterion on a ring where the elements are not laid out on a line but on a lattice in the plane.

**Is an instance: $\mathbb{Q}[\sqrt{2}] \leq \mathbb{R}$.** The set $\mathbb{Q}[\sqrt{2}] = \{a + b\sqrt{2} : a, b \in \mathbb{Q}\}$ is a subring of $\mathbb{R}$. By the criterion: $1 = 1 + 0\sqrt 2 \in \mathbb{Q}[\sqrt 2]$; subtraction works coordinatewise; and multiplication closes because $(a + b\sqrt 2)(c + d\sqrt 2) = (ac + 2bd) + (ad + bc)\sqrt 2$, where the cross-term $\sqrt 2 \cdot \sqrt 2 = 2$ has folded back into the rational part. This last point is the instructive one: closure under multiplication is *not* automatic for a set of this shape — it works precisely because $(\sqrt 2)^2$ happens to lie back in $\mathbb{Q}$. Unlike $\mathbb{Z}[i]$, this subring is in fact a field (see [[Def - Unit and Field]]).

**Is NOT an instance: $2\mathbb{Z} \subseteq \mathbb{Z}$.** The even integers are closed under addition, under multiplication, and under negation — yet they form **no subring** of $\mathbb{Z}$, because $1 \notin 2\mathbb{Z}$: condition (1) fails. This is the canonical "closed under all the operations but missing the unit" non-example, and it is precisely the structure that a careless definition would wrongly admit. The same set $2\mathbb{Z}$ *is*, however, an [[Def - Ideal|ideal]] of $\mathbb{Z}$ — the distinction between subring and ideal is exactly the distinction this non-example draws.

**Is NOT an instance: $\mathbb{N} \subseteq \mathbb{Z}$.** The non-negative integers contain $0$ and $1$ and are closed under addition and multiplication — yet they form **no subring** of $\mathbb{Z}$, because they are not closed under additive inverses: $1 \in \mathbb{N}$ but $-1 \notin \mathbb{N}$, so condition (3) fails. Equivalently the criterion fails, since $0 - 1 = -1 \notin \mathbb{N}$. This is the "closed under the operations but not under negation" non-example; it probes condition (3) in isolation, and it is the ring-theoretic echo of the fact that $\mathbb{N}$ is not a [[Def - Subgroup|subgroup]] of $(\mathbb{Z}, +)$.

**Corollary (intersections are subrings).** If $S \leq R$ and $T \leq R$, then $S \cap T \leq R$. Apply the criterion: $1_R$ lies in both $S$ and $T$, hence in $S \cap T$; and if $a, b \in S \cap T$ then $a - b$ and $a \cdot b$ lie in $S$ and in $T$ separately, hence in $S \cap T$. More generally an *arbitrary* intersection of subrings is a subring. *Calibration check:* this is exactly what makes "$R[\alpha]$, the smallest subring containing $R$ and $\alpha$" a well-defined object — it is the intersection of all subrings containing $R$ and $\alpha$.

**Corollary (transitivity).** If $T \leq S$ and $S \leq R$, then $T \leq R$: a subring of a subring is a subring, since the subring conditions involve only the operations $+$, $\cdot$ and the elements $0_R, 1_R$, which are the same throughout the tower. This is what licenses chains like $\mathbb{Z} \leq \mathbb{Q} \leq \mathbb{R} \leq \mathbb{C}$ and lets one conclude $\mathbb{Z} \leq \mathbb{C}$ directly. *Calibration check:* contrast this with [[Def - Ideal|ideals]], for which the analogous transitivity *fails* — an ideal of an ideal need not be an ideal of the whole ring.

**Corollary (a subring inherits commutativity).** If $R$ is a commutative ring and $S \leq R$, then $S$ is automatically commutative, since $ab = ba$ is a "for all" identity inherited by every subset. Under this course's standing convention all rings are commutative, so this is reassuring rather than surprising — but it is the formal reason one never has to check commutativity when verifying a subring.
