---
type: definition
subject: group-theory
prereqs: []
tags: [algebra, group-theory]
---

# Notation

A group is written $(G, \cdot, e)$: the set $G$, the binary operation $\cdot$, and the identity element $e$. The operation is also written $\cdot$ omitted entirely, so $g_1 g_2$ means $g_1 \cdot g_2$. The identity is also denoted $1_G$, or just $1$, especially when the operation is thought of as multiplication; when the operation is written additively as $+$, the identity is $0$ and the inverse of $g$ is $-g$. The inverse of $g$ is $g^{-1}$, and $g^n$ denotes the $n$-fold product $g \cdot g \cdots g$, with the conventions $g^0 = e$ and $g^{-n} = (g^{-1})^n$. See [[Group Theory I — §1.1–1.2]] for the full notation registry.

---

# Axiom Motivation

The thing we are trying to axiomatize is **reversible composition**. Look at three situations: rotating a square, where you can rotate by $90^\circ$ and then by $90^\circ$ again, or undo a rotation; shuffling a deck, where you can apply one rearrangement after another, or shuffle back to the original order; adding integers, where you can add $3$ then add $5$, or subtract to get back. In every case there is a collection of "moves", a way to do one move after another, a move that does nothing, and for every move a move that cancels it. The group axioms are the attempt to write down exactly this much structure and not one bit more, so that any theorem proved from them applies simultaneously to rotations, shuffles, and integers.

Start with the operation. We want to be able to combine two moves into one, so we need a function $\cdot : G \times G \to G$. The codomain being $G$ is itself a real demand — it says the combination of two moves is again a move, **closure** — and it is the reason a separate closure axiom is redundant: a function called $\cdot : G \times G \to G$ already promises its outputs lie in $G$. If we dropped this and allowed $\cdot$ to be merely a partial function, or to land outside $G$, we would not have a self-contained system of moves at all; we would have to keep track of an ambient world. So closure is built into the word "function with codomain $G$".

Now, why **associativity**, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$? The honest motivation is bracketing. We want to make sense of a long composition $g_1 g_2 g_3 \cdots g_n$ — "do these $n$ moves in order" — and a binary operation only ever combines two things at a time. There are many ways to bracket $g_1 g_2 g_3 g_4$, and associativity is exactly the statement that they all agree, so the unbracketed expression is unambiguous. Without it the notion "compose these moves in order" would not even be well-defined. Concretely, function composition is associative — $(f \circ g) \circ h$ and $f \circ (g \circ h)$ both mean "apply $h$, then $g$, then $f$" — and since the motivating examples (rotations, shuffles) literally *are* functions being composed, associativity is free for them. What associativity excludes is instructive: subtraction on $\mathbb{Z}$ is *not* associative, since $(8 - 4) - 1 = 3$ but $8 - (4 - 1) = 5$, so $(\mathbb{Z}, -)$ is not a group; the failure is not a technicality, it is that "subtract these numbers in order" genuinely has no meaning.

Next, the **identity** $e$ with $e \cdot g = g \cdot e = g$. This is the "do nothing" move. We need it for two reasons. First, it is the thing every inverse must produce — without a designated identity, the inverse axiom has nothing to say "cancels to". Second, it is the analogue of $0$ for addition and $1$ for multiplication, the anchor of the whole system. Notice we demand it work on **both sides**, $e \cdot g$ and $g \cdot e$; in fact for groups a one-sided identity together with one-sided inverses already forces the two-sided versions, but stating it two-sided is cleaner and matches intuition.

Finally, **inverses**: for every $a$ there is $a^{-1}$ with $a \cdot a^{-1} = a^{-1} \cdot a = e$. This is the axiom that makes composition *reversible*, and it is the one that distinguishes a group from its weaker cousins. If we drop it we get a **monoid**: the natural numbers $(\mathbb{N}, +, 0)$ are a monoid but not a group, because $3$ has no additive inverse — there is no natural number $n$ with $3 + n = 0$. A monoid is a perfectly good structure, but it cannot model "undo". The dihedral and matrix examples make the demand vivid: a rotation can always be rotated back, an invertible matrix can always be inverted, and these are groups; the *non*-invertible $2 \times 2$ matrices fail the inverse axiom and form only a monoid under multiplication. The inverse axiom is also why we may **cancel**: from $a \cdot b = a \cdot c$ we left-multiply by $a^{-1}$ to get $b = c$. Cancellation is not a separate axiom; it is a consequence, and it is the single most-used computational consequence of the inverse axiom.

One could ask whether to *strengthen* the axioms by also demanding commutativity, $a \cdot b = b \cdot a$. That gives a strictly smaller class, the [[Def - Abelian Group|abelian groups]], and it would exclude things we genuinely want to keep: the symmetric group $S_3$, the symmetries of a triangle, is not commutative, since reflecting then rotating differs from rotating then reflecting. Reversible composition does not in general commute — putting on socks then shoes is not the same as shoes then socks — so commutativity is left *out* of the group axioms and studied separately as an extra hypothesis.

In summary, the four demands — closure, associativity, identity, inverses — are each forced by one feature of "reversible composition": closure makes the moves self-contained, associativity makes long compositions meaningful, the identity provides the "do nothing" anchor, and inverses provide "undo". Drop any one and you lose exactly that feature.

---

# The Definition

A **group** is a triple $(G, \cdot, e)$ where $G$ is a set, $\cdot : G \times G \to G$ is a function (the **group operation** or **multiplication**), and $e \in G$ is a distinguished element (the **identity**), satisfying:

1. **Associativity.** For all $a, b, c \in G$, $\quad (a \cdot b) \cdot c = a \cdot (b \cdot c)$.
2. **Identity.** For all $a \in G$, $\quad a \cdot e = e \cdot a = a$.
3. **Inverses.** For all $a \in G$, there exists $a^{-1} \in G$ with $\quad a \cdot a^{-1} = a^{-1} \cdot a = e$.

Closure — that $a \cdot b \in G$ for all $a, b \in G$ — is not listed as a separate axiom because it is already part of the statement that $\cdot$ is a function with codomain $G$.

The **order** of the group is the cardinality $|G|$; see [[Def - Order of a Group and of an Element]].

---

# Categorical Definition

There are two ways category theory absorbs the definition of a group, and both are illuminating once the underlying categorical vocabulary is in place.

**A group is a one-object groupoid.** A *category* consists of objects and arrows between them, with an associative composition of arrows and an identity arrow on each object. A *groupoid* is a category in which every arrow is invertible — for each arrow $f$ there is an arrow $f^{-1}$ composing with it to give identities. Now take a category with exactly **one object**, call it $\star$. The arrows are all of the form $\star \to \star$; they can all be composed with one another, composition is associative by the category axioms, the identity arrow $\mathrm{id}_\star$ is a two-sided unit, and if the category is a groupoid every arrow is invertible. The arrows of a one-object groupoid are therefore precisely a set with an associative composition, a unit, and inverses — a group. The dictionary is exact: a group **is** a one-object groupoid, with the group elements being the arrows and group multiplication being arrow composition. This viewpoint is the reason group actions, conjugacy, and representations all have clean categorical descriptions: an action is a functor out of the one-object groupoid.

**A group is a group object in $\mathbf{Set}$.** A *group object* in a category $\mathcal{C}$ with finite products is an object $G$ equipped with three arrows — multiplication $m : G \times G \to G$, identity $e : 1 \to G$ (where $1$ is the terminal object), and inversion $i : G \to G$ — such that certain diagrams commute, the diagrams expressing associativity, the unit law, and the inverse law purely in terms of arrows and products. When $\mathcal{C} = \mathbf{Set}$, the category of sets, the terminal object $1$ is a one-point set, an arrow $1 \to G$ is the same as a choice of element of $G$, and the commuting diagrams unwind into exactly axioms (1)–(3) above. So an ordinary group is a group object in $\mathbf{Set}$. The payoff is that the *same* diagrams interpreted in other categories produce other species of group automatically: a group object in the category of smooth manifolds is a Lie group, a group object in topological spaces is a topological group, a group object in the category of varieties is an algebraic group. The set-theoretic definition is one instance of a template.

---

# Relate to Other Fields / Compression

A group is a **monoid in which every element is invertible**. A monoid is a set with an associative operation and a two-sided identity — axioms (1) and (2) alone — and adding axiom (3), invertibility, gives a group. This is the cleanest compression: groups sit one invertibility-axiom away from monoids, just as fields sit one invertibility-axiom (for nonzero elements) away from commutative rings.

From the linear-algebra side, a group is the **automorphism structure stripped of its carrier**. For any mathematical object $X$ — a set, a vector space, a graph, a topological space — the structure-preserving bijections of $X$ to itself, the *automorphisms*, always form a group under composition: composition is associative, the identity map is the identity element, and every automorphism is invertible by construction. The symmetric group $S_n$ is the automorphism group of an $n$-element set; $\mathrm{GL}_n(\mathbb{R})$ is the automorphism group of the vector space $\mathbb{R}^n$. Cayley's theorem makes the slogan precise in the other direction: every group is isomorphic to a group of permutations, so the abstract group axioms capture exactly "the symmetries of *something*", with the something abstracted away.

---

# Examples / Corollaries

**Is an instance: $(\mathbb{Z}, +, 0)$.** The integers under addition form a group. Addition is associative, $0$ is the identity, and the inverse of $n$ is $-n$. It is infinite and [[Def - Abelian Group|abelian]]. This is the prototype of a cyclic group: every element is a multiple of the generator $1$.

**Is an instance: the symmetric group $S_n$.** The set of all permutations (bijections) of $\{1, 2, \ldots, n\}$ under composition is a group. Composition of bijections is associative, the identity permutation is the identity element, and every bijection has an inverse bijection. For $n \geq 3$ it is **non-abelian**, which makes it the standard test object for any statement that might secretly assume commutativity. It has order $|S_n| = n!$.

**Is an instance: the dihedral group $D_{2n}$.** The symmetries of a regular $n$-gon — $n$ rotations and $n$ reflections — form a group of order $2n$ under composition. It is non-abelian for $n \geq 3$: rotating then reflecting is not the same as reflecting then rotating. It is the smallest interesting family of non-abelian groups and the natural place to test conjugation.

**Is an instance: $\mathrm{GL}_n(\mathbb{R})$.** The invertible $n \times n$ real matrices form a group under matrix multiplication. Matrix multiplication is associative, the identity matrix is the identity element, and the requirement of invertibility is exactly what guarantees axiom (3). Restricting to determinant $1$ gives the subgroup $\mathrm{SL}_n(\mathbb{R})$; see [[Def - Subgroup]].

**Is an instance: the cyclic group $C_n$.** The group of rotations of a regular $n$-gon, equivalently the integers $\{0, 1, \ldots, n-1\}$ under addition modulo $n$, is a group of order $n$. It is abelian and is generated by a single element. It sits inside $D_{2n}$ as the rotation subgroup.

**Is an instance: the quaternion group $Q_8$.** The eight elements $\{\pm 1, \pm i, \pm j, \pm k\}$ with $ij = k$, $ji = -k$, $i^2 = j^2 = k^2 = -1$ and $(-1)^2 = 1$ form a non-abelian group of order $8$. It is a useful counterexample-generator: it is non-abelian yet *every* subgroup of it is normal, showing that "all subgroups normal" is strictly weaker than "abelian" (contrast [[Def - Abelian Group]]).

**Is an instance: the Klein four-group $V = C_2 \times C_2$.** The group with four elements in which every non-identity element has order $2$ and the product of any two distinct non-identity elements is the third. It is abelian, of order $4$, and is the smallest non-cyclic group.

**Is NOT an instance: $(\mathbb{N}, +, 0)$.** The natural numbers under addition satisfy associativity and have the identity $0$, but they **fail the inverse axiom**: $3$ has no additive inverse, since no natural number $n$ satisfies $3 + n = 0$. This is a *monoid*, not a group. It probes axiom (3) specifically — everything else holds.

**Is NOT an instance: $(\mathbb{Z}, \times, 1)$.** The integers under multiplication satisfy associativity and have the identity $1$, but again **fail the inverse axiom**: $2$ has no multiplicative inverse in $\mathbb{Z}$, since $\tfrac{1}{2} \notin \mathbb{Z}$. Only $\pm 1$ are invertible. This too is a monoid. To get a group one must restrict to the invertible elements — here just $\{\pm 1\}$ — or change the underlying set, for instance to $\mathbb{Q} \setminus \{0\}$ where every nonzero rational does have an inverse. This non-example probes axiom (3) from a different angle: the obstruction is not "negative numbers missing" but "reciprocals missing".

**Corollary (uniqueness of the identity).** A group has exactly one identity element. If $e$ and $e'$ both satisfy the identity axiom, then $e' = e \cdot e' = e$, using the identity property of $e$ on the left and of $e'$ on the right. So the article "the" in "the identity $e$" is justified. *Calibration check:* if you can reproduce this two-line argument you have understood that the identity axiom is two-sided.

**Corollary (uniqueness of inverses).** Each element of a group has exactly one inverse. Suppose $a^{-1}$ and $b$ are both inverses of $a$, so $a \cdot a^{-1} = a^{-1} \cdot a = e$ and $a \cdot b = b \cdot a = e$. Then

$$b = b \cdot e = b \cdot (a \cdot a^{-1}) = (b \cdot a) \cdot a^{-1} = e \cdot a^{-1} = a^{-1}.$$

The argument uses, in order, the identity axiom, the inverse property of $a^{-1}$, **associativity**, the inverse property of $b$, and the identity axiom again. That associativity is the load-bearing step is the lesson: without it, having two cancelling partners would not force them equal. This justifies the notation "$a^{-1}$", the inverse, and is the lemma proved in the source lecture notes.

**Corollary (cancellation).** In any group, $a \cdot b = a \cdot c$ implies $b = c$, and $b \cdot a = c \cdot a$ implies $b = c$. Left-multiply (respectively right-multiply) by $a^{-1}$ and use associativity. *Calibration check:* cancellation is why a group's multiplication table is a Latin square — every element appears exactly once in each row and column.

**Corollary (socks-and-shoes).** $(a \cdot b)^{-1} = b^{-1} \cdot a^{-1}$, with the order reversed. Indeed $(a \cdot b)(b^{-1} a^{-1}) = a (b b^{-1}) a^{-1} = a e a^{-1} = e$, and similarly on the other side, so by uniqueness of inverses $b^{-1} a^{-1}$ is *the* inverse of $a \cdot b$. The reversal is exactly the everyday fact that to undo "socks then shoes" you do "remove shoes then remove socks".

---

# Unlocked by This

> [!tip] Group Action *(from Representation Theory and Geometry)*
> Once you have the group axioms you can ask a group to *act* — a [[Def - Homomorphism|homomorphism]] $G \to \operatorname{Sym}(X)$ assigns to each group element a permutation of a set $X$, making "abstract symmetry" into "concrete symmetry of something". Group actions are the bridge from the axioms to geometry, combinatorics, and the orbit-stabiliser theorem in [[Group Theory II — §1.3–1.4]].

> [!tip] Lie Group *(from Differential Geometry)*
> Reading the group axioms in the category of smooth manifolds rather than sets — a group object whose multiplication and inversion are smooth maps — gives a Lie group, the central object linking symmetry to differential geometry and physics. The categorical definition above is exactly what makes this transfer immediate.
