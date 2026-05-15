---
type: theorem
subject: group-theory
prereqs:
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group and $K \leq L \leq G$ are subgroups, *both normal in $G$*: $K \trianglelefteq G$ and $L \trianglelefteq G$. We then form the [[Def - Quotient Group|quotients]] $G/K$, $G/L$, and $L/K$. Inside $G/K$, the set $L/K = \{\ell K : \ell \in L\}$ is itself a subgroup. The symbol $\cong$ denotes [[Def - Isomorphism|isomorphism]]. The full registry is on the parent page [[Group Theory I — §1.1–1.2]].

---

# Statement

> **Third Isomorphism Theorem.** Let $G$ be a group and let $K \leq L \leq G$ with $K \trianglelefteq G$ and $L \trianglelefteq G$. Then $L/K$ is a normal subgroup of $G/K$, and there is an isomorphism
> $$\frac{G/K}{\,L/K\,} \;\cong\; \frac{G}{L}.$$

---

# Motivation

Suppose you want to simplify a group $G$ by quotienting, but you intend to do it in **two stages**: first collapse a small normal subgroup $K$, obtaining $G/K$, and then collapse a further normal subgroup of $G/K$. A natural choice for the second stage is $L/K$, where $L$ is a normal subgroup of $G$ containing $K$. The third isomorphism theorem says the obvious thing — that quotienting in two stages gives the same answer as quotienting once by the bigger subgroup $L$:
$$\text{quotient by } K, \text{ then by } L/K \;=\; \text{quotient by } L.$$

This is the **cancellation law** for quotients. It is the exact group-theoretic analogue of the arithmetic identity
$$\frac{a/c}{b/c} = \frac{a}{b},$$
where dividing top and bottom by a common factor $c$ leaves the ratio unchanged. Here $G$ plays the role of $a$, $L$ of $b$, and $K$ of the common factor $c$; the theorem says the common factor $K$ "cancels". The notation $\dfrac{G/K}{L/K}$ is built so that this cancellation is visually obvious — which is precisely the point of arranging it this way.

Why would one care? Two reasons. First, it makes iterated quotients tractable: when you build a [[Thm - Composition Series|composition series]] by repeatedly passing to quotients, the third isomorphism theorem is what lets you translate between "the quotient of a quotient" and "a single quotient", so the series can be analysed coherently. Second, it is the computational half of the [[Thm - Correspondence Theorem|correspondence theorem]]: the correspondence theorem tells you the *normal subgroups* of $G/K$ are exactly the $L/K$ for $L \trianglelefteq G$ above $K$, and the third isomorphism theorem then tells you the *quotient* by each one. Together they say that the quotient $G/K$ is not a mysterious new object — its entire normal-subgroup-and-quotient structure is read directly off that of $G$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is a chain $K \leq L \leq G$ with *both* $K$ and $L$ normal in $G$. The disguised-source question is: when do you get two nested normal subgroups without the problem announcing them?

The first source is **the centre and the commutator subgroup**. The centre $Z(G)$ and the commutator subgroup $[G,G]$ are always normal in $G$, and a chain among them and their relatives — say $K = \{e\}$, $L = Z(G)$, or $K = [G,G]$ inside a larger characteristic subgroup — supplies the input automatically. The non-obvious step is recognising that characteristic subgroups are normal, so any tower of them is a legal chain. *Example problem:* relate $G/[G,G]$ to $(G/N)/([G,G]N/N)$ for a normal $N \subseteq [G,G]$.

The second source is **kernels of two homomorphisms out of $G$, one factoring through the other**. If $\psi : G \to A$ and $\chi : G \to B$ are homomorphisms with $\ker\psi \subseteq \ker\chi$, then $K = \ker\psi$ and $L = \ker\chi$ are normal subgroups of $G$ with $K \leq L$. The non-obviousness is that "$\chi$ factors through $\psi$" is exactly the containment of kernels, so a factorisation hypothesis is secretly a nested-normal-subgroups hypothesis. *Example problem:* given that a character $\chi$ is trivial on $\ker\psi$, identify the induced map on $G/\ker\psi$.

The third source is **a normal series already in hand**. If a problem hands you $\{e\} \trianglelefteq N_1 \trianglelefteq N_2 \trianglelefteq G$ with each $N_i$ normal *in $G$* (not merely in the next term), then every pair $N_i \leq N_j$ is a legal $(K, L)$. The non-obvious payoff is that the third isomorphism theorem lets you compare the successive quotients of the series, $\dfrac{G/N_1}{N_2/N_1} \cong G/N_2$. *Example problem:* show the factors of a chief series are read consistently whether viewed in $G$ or in a quotient.

**Targets (Output Amplification)**

The conclusion is the isomorphism $\dfrac{G/K}{L/K} \cong \dfrac{G}{L}$ together with $L/K \trianglelefteq G/K$.

Combine the conclusion with **a counting / Lagrange argument**. Taking orders, $\big|\frac{G/K}{L/K}\big| = |G/L|$ gives $\dfrac{|G/K|}{|L/K|} = \dfrac{|G|}{|L|}$, which is the consistent index multiplicativity $|G:L| = |G/K : L/K|$. The further result $E$ is that *index is preserved under quotienting*: the index of $L$ in $G$ equals the index of $L/K$ in $G/K$. This is non-obvious — quotienting changes the sizes of both groups — yet the *ratio* survives, which is exactly what the correspondence theorem needs to say it preserves index.

Combine the conclusion with **simplicity of the bottom quotient $G/L$**. If $G/L$ is a [[Def - Simple Group|simple group]], then $\dfrac{G/K}{L/K}$ is simple, which says $L/K$ is a *maximal* normal subgroup of $G/K$. The further result is the inductive step in the existence proof of composition series: quotienting by a maximal normal subgroup yields a simple quotient, and the third isomorphism theorem certifies this is consistent across the tower. The combination is the backbone of [[Thm - Composition Series]].

Combine the conclusion with **a known structure for $G/K$**. If $G/K$ is a group you understand — say abelian, or cyclic — then every quotient of it is too, and the theorem identifies $G/L$ as such a quotient. The further result: structural properties closed under quotients (abelian, solvable, nilpotent, having bounded exponent) pass from $G/K$ down to $G/L$ for free, because $G/L$ is literally a quotient of $G/K$.

---

# Why Is It True

The cleanest way to see why is to ask: what does it *mean* to be an element of the iterated quotient $\dfrac{G/K}{L/K}$, and how does that compare with an element of $G/L$?

Start in $G$. To form $G/K$ you declare two elements the same when they differ by an element of $K$. To then form $\dfrac{G/K}{L/K}$, you take those $K$-classes and declare two of *them* the same when they differ by an element of $L/K$ — that is, when they differ by a $K$-class coming from $L$. Unwind this. Two elements $g, g'$ of $G$ become identified in the doubly-iterated quotient exactly when the $K$-classes $gK$ and $g'K$ differ by something in $L/K$, which happens exactly when $g^{-1}g' \in L$. But "$g^{-1}g' \in L$" is *precisely* the condition for $g$ and $g'$ to be identified in $G/L$.

So the doubly-iterated quotient and the single quotient $G/L$ identify exactly the same pairs of elements of $G$. They are the same partition of $G$, and hence — once you check the multiplications agree, which they do because both are inherited from $G$ — the same group. The intuition is that **quotienting forgets information, and forgetting in two stages forgets exactly what forgetting once by the union would forget.** First you forget $K$; then you forget the rest of $L$. The order and the staging do not matter — the total information discarded is "membership in $L$", and that is $G/L$.

A second, sharper view makes the proof inevitable. There is an utterly natural map $G/K \to G/L$: send a $K$-class to the $L$-class it sits inside, $gK \mapsto gL$. This is well-defined because $K \subseteq L$ (a finer class determines a coarser one), it is surjective (every $L$-class contains some $K$-class), and an element $gK$ is killed exactly when $g \in L$, i.e. the kernel is $L/K$. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied to *this one map* says (source modulo kernel) $\cong$ image, that is $\dfrac{G/K}{L/K} \cong G/L$. The theorem is not a new fact; it is the first isomorphism theorem applied to the only sensible map between the two quotients.

---

# What Makes This Hard

The non-obvious step is realising you should not manipulate the iterated quotient $\dfrac{G/K}{L/K}$ directly — its elements are *cosets of cosets*, and reasoning about them by hand is error-prone — but instead build the single forgetful map $G/K \to G/L$, $gK \mapsto gL$, and invoke the first isomorphism theorem. The most common error is in checking that map is well-defined: one must use the containment $K \subseteq L$ (so that $gK = g'K \Rightarrow g^{-1}g' \in K \subseteq L \Rightarrow gL = g'L$), and beginners either skip the check or forget that it is $K \subseteq L$ that licenses it. A second subtlety is keeping straight that both $K$ and $L$ must be normal *in $G$* for all four quotients in the statement to exist — $L$ normal merely in $G/K$ would not be enough to even write $G/L$.

---

# Rederivation Scaffold

**High-level strategy:**
Define the forgetful homomorphism $\theta : G/K \to G/L$ that sends each $K$-coset to the larger $L$-coset containing it. Check it is well-defined (this uses $K \subseteq L$), a homomorphism, and surjective; compute its kernel to be $L/K$. Apply the first isomorphism theorem.

**Subgoal decomposition:**

1. **Define $\theta$.** Set $\theta : G/K \to G/L$ by $\theta(gK) = gL$.
   - *Hint:* This is the natural "coarsen the equivalence" map.
   - *Why needed:* It is the single homomorphism the whole proof runs through.

2. **Well-definedness.** Show $gK = g'K$ implies $gL = g'L$.
   - *Hint:* $gK = g'K$ gives $g^{-1}g' \in K$; since $K \subseteq L$, also $g^{-1}g' \in L$, so $gL = g'L$. This is the *only* place the hypothesis $K \subseteq L$ is used.
   - *Why needed:* Without it $\theta$ is not a function.

3. **Homomorphism.** Show $\theta$ respects multiplication.
   - *Hint:* $\theta(gK \cdot g'K) = \theta(gg'K) = gg'L = (gL)(g'L)$, using the quotient multiplication on both sides.
   - *Why needed:* An isomorphism must preserve the operation.

4. **Surjectivity.** Show every element of $G/L$ is hit.
   - *Hint:* An arbitrary element of $G/L$ is $gL = \theta(gK)$.
   - *Why needed:* So the image is all of $G/L$, the right-hand side of the claimed isomorphism.

5. **Kernel.** Show $\ker\theta = L/K$.
   - *Hint:* $\theta(gK) = L$ (the identity of $G/L$) if and only if $gL = L$ if and only if $g \in L$; the set of such $gK$ is exactly $\{ \ell K : \ell \in L\} = L/K$.
   - *Why needed:* Identifies the kernel; also, being a kernel, $L/K \trianglelefteq G/K$.

6. **Apply the first isomorphism theorem.** Conclude $\dfrac{G/K}{L/K} \cong G/L$.
   - *Hint:* First isomorphism theorem: $(G/K)/\ker\theta \cong \operatorname{im}\theta$.
   - *Why needed:* This is the statement.

---

# Lemma Decomposition

<details>
<summary><strong>Lemma 1: The forgetful map $G/K \to G/L$ is well-defined when $K \subseteq L$</strong></summary>

**Statement:** Let $K \leq L \leq G$ with $K, L \trianglelefteq G$. The rule $\theta(gK) = gL$ defines a function $G/K \to G/L$ (independent of the chosen representative $g$).

**Hint:** A finer equivalence refines a coarser one: if two elements differ by something in $K$, they differ by something in $L \supseteq K$.

**Why needed:** It is the foundational check that makes $\theta$ a legitimate map; the containment $K \subseteq L$ enters here and nowhere else.

<details>
<summary>Full proof</summary>

Suppose $gK = g'K$. Then $g^{-1}g' \in K$. Since $K \subseteq L$, we also have $g^{-1}g' \in L$, which means $gL = g'L$. Hence $\theta(gK) = gL = g'L = \theta(g'K)$: the output does not depend on the representative, so $\theta$ is well-defined.

</details>

</details>

<details>
<summary><strong>Lemma 2: $\theta$ is a surjective homomorphism</strong></summary>

**Statement:** The well-defined map $\theta : G/K \to G/L$, $gK \mapsto gL$, is a homomorphism and is surjective.

**Hint:** Multiplication in both quotients is "multiply representatives"; surjectivity is immediate from the formula.

**Why needed:** These are two of the four hypotheses of the first isomorphism theorem; surjectivity pins the image as all of $G/L$.

<details>
<summary>Full proof</summary>

*Homomorphism.* For cosets $gK, g'K \in G/K$,
$$\theta\big((gK)(g'K)\big) = \theta(gg'K) = gg'L = (gL)(g'L) = \theta(gK)\,\theta(g'K),$$
using the definition of multiplication in $G/K$ and in $G/L$.

*Surjectivity.* An arbitrary element of $G/L$ has the form $gL$ for some $g \in G$. Then $gL = \theta(gK)$, so it lies in the image. Hence $\theta$ is surjective.

</details>

</details>

<details>
<summary><strong>Lemma 3: $\ker\theta = L/K$</strong></summary>

**Statement:** With $\theta$ as above, $\ker\theta = \{\ell K : \ell \in L\} = L/K$. In particular $L/K$ is a normal subgroup of $G/K$.

**Hint:** The identity of $G/L$ is the coset $L$; ask which $gK$ map to it.

**Why needed:** It identifies the kernel that the first isomorphism theorem quotients by, and it delivers the normality claim $L/K \trianglelefteq G/K$ for free.

<details>
<summary>Full proof</summary>

The identity element of $G/L$ is the coset $L = eL$. An element $gK \in G/K$ lies in $\ker\theta$ if and only if $\theta(gK) = L$, i.e. if and only if $gL = L$, i.e. if and only if $g \in L$. Therefore
$$\ker\theta = \{gK : g \in L\} = \{\ell K : \ell \in L\} = L/K.$$
(The set $\{\ell K : \ell \in L\}$ is well-defined as a subset of $G/K$ because $K \subseteq L$, so every $\ell K$ is a genuine coset of $K$.) Being the kernel of the homomorphism $\theta$, the set $L/K$ is a normal subgroup of the domain $G/K$.

</details>

</details>

---

# Formal Proof

<details>
<summary><strong>Complete formal proof</strong></summary>

Let $G$ be a group and $K \leq L \leq G$ with $K \trianglelefteq G$ and $L \trianglelefteq G$. Then $G/K$, $G/L$ are quotient groups.

**Define the map.** Set
$$\theta : G/K \longrightarrow G/L, \qquad \theta(gK) = gL.$$

**$\theta$ is well-defined.** The rule uses a representative $g$ of the coset $gK$, so we check independence of the choice. If $gK = g'K$, then $g^{-1}g' \in K$. Since $K \subseteq L$, also $g^{-1}g' \in L$, hence $gL = g'L$. Thus $\theta(gK) = \theta(g'K)$, and $\theta$ is a function. (This is the only step using $K \subseteq L$.)

**$\theta$ is a homomorphism.** For $gK, g'K \in G/K$,
$$\theta\big((gK)(g'K)\big) = \theta(gg'K) = gg'L = (gL)(g'L) = \theta(gK)\,\theta(g'K).$$

**$\theta$ is surjective.** Any element of $G/L$ is $gL$ for some $g \in G$, and $gL = \theta(gK)$. So $\operatorname{im}\theta = G/L$.

**Compute the kernel.** The identity of $G/L$ is the coset $L$. Then
$$gK \in \ker\theta \iff \theta(gK) = L \iff gL = L \iff g \in L.$$
Hence $\ker\theta = \{gK : g \in L\} = L/K$. As the kernel of a homomorphism, $L/K$ is a normal subgroup of $G/K$.

**Apply the first isomorphism theorem.** The map $\theta : G/K \to G/L$ is a homomorphism with $\ker\theta = L/K$ and $\operatorname{im}\theta = G/L$. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives
$$\frac{G/K}{\ker\theta} \;\cong\; \operatorname{im}\theta, \qquad\text{that is}\qquad \frac{G/K}{L/K} \;\cong\; \frac{G}{L}. \qquad \blacksquare$$

</details>

---

# Cross-Field Exercise Suggestions

**Iterated quotients of $\mathbb{Z}$ and divisibility.** Take $G = \mathbb{Z}$, $L = m\mathbb{Z}$, and $K = mn\mathbb{Z}$ for positive integers $m, n$, so $K \subseteq L$ (both normal, as $\mathbb{Z}$ is abelian). The third isomorphism theorem gives $\dfrac{\mathbb{Z}/mn\mathbb{Z}}{\,m\mathbb{Z}/mn\mathbb{Z}\,} \cong \mathbb{Z}/m\mathbb{Z}$. This is the statement that reducing modulo $mn$ and then modulo $m$ is the same as reducing modulo $m$ — a familiar fact of modular arithmetic, revealed as an instance of the cancellation law. The application is non-obvious because nothing about "reduce mod $m$" advertises itself as a quotient of a quotient.

**Solvability is closed under quotients.** A group $G$ is solvable if it has a normal series with abelian factors. Suppose $G$ is solvable and $N \trianglelefteq G$; one wants $G/N$ solvable. Given a normal series $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_r = G$, the images $G_i N/N$ form a series for $G/N$, and the third isomorphism theorem identifies the successive factors as quotients of the original abelian factors, hence abelian. The non-obvious recognition is that the theorem is exactly what converts "factor of the lifted series" into "quotient of an abelian group".

**Field towers in Galois theory.** For a tower of fields $F \subseteq E \subseteq L$ with $L/F$ Galois, the Galois groups satisfy $\operatorname{Gal}(L/E) \trianglelefteq \operatorname{Gal}(L/F)$ when $E/F$ is Galois, and the third isomorphism theorem underlies $\operatorname{Gal}(E/F) \cong \operatorname{Gal}(L/F)/\operatorname{Gal}(L/E)$. Quotienting a Galois group in stages mirrors building the field tower in stages. The application is non-obvious because the "common factor that cancels" is a subgroup fixing an intermediate field — a geometric object, not an algebraic one.

**Comparing two refinements of a partition.** Outside group theory entirely: if a set carries two equivalence relations, one refining the other, the third isomorphism theorem (read at the level of quotient *sets* with compatible structure) says the quotient of the fine quotient by the induced relation equals the coarse quotient. Recognising a hierarchy of equivalence relations — finest, intermediate, coarsest — as a chain $K \leq L \leq G$ is the non-obvious step that brings the theorem to bear.

---

# Bridges

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]]** — the parent result. The third isomorphism theorem is the first isomorphism theorem applied to the forgetful homomorphism $G/K \to G/L$, $gK \mapsto gL$. It introduces no new technique.

- **[[Thm - Second Isomorphism Theorem|Second Isomorphism Theorem]]** — a sibling corollary of the first isomorphism theorem. The second handles a subgroup meeting a normal subgroup; the third handles two nested normal subgroups. Both are "apply the first isomorphism theorem to the right map".

- **[[Thm - Correspondence Theorem|Correspondence Theorem]]** — its computational partner. The correspondence theorem says the normal subgroups of $G/K$ are exactly the $L/K$ for $L \trianglelefteq G$ above $K$; the third isomorphism theorem then computes the quotient by each, namely $(G/K)/(L/K) \cong G/L$. Used together they fully describe the quotient lattice and its quotients.

- **The arithmetic identity $\frac{a/c}{b/c} = \frac{a}{b}$** — the third isomorphism theorem is the group-theoretic cancellation law, with $G, L, K$ in the roles of $a, b, c$. The notational layout $\dfrac{G/K}{L/K}$ is designed so the cancellation is literally visible.

- **[[Thm - Composition Series|Composition Series]]** — the third isomorphism theorem is invoked in handling iterated quotients along a series, ensuring "quotient of a quotient" can always be rewritten as a single quotient.
