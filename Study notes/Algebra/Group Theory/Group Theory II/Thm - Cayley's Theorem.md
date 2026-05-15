---
type: theorem
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Group Action"
  - "Def - Symmetric Group"
  - "Def - Permutation Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Def - Isomorphism"
  - "Thm - Actions Correspond to Homomorphisms"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Notation

$G$ is a group with identity $e$ and operation by juxtaposition. For a set $X$, the [[Def - Symmetric Group|symmetric group]] $\operatorname{Sym}(X)$ is the group of all bijections $X \to X$ under composition; when $X = \{1, \dots, n\}$ this is $S_n$, of order $n!$. A [[Def - Permutation Group|permutation group]] is a [[Def - Subgroup|subgroup]] of some $\operatorname{Sym}(X)$. An [[Def - Group Action|action]] of $G$ on a set $X$ is a map $G\times X\to X$, $(g,x)\mapsto g\cdot x$, with $e\cdot x = x$ and $g_1\cdot(g_2\cdot x) = (g_1g_2)\cdot x$; by [[Thm - Actions Correspond to Homomorphisms]] it is the same data as a [[Def - Homomorphism|homomorphism]] $\rho : G \to \operatorname{Sym}(X)$. The **left-regular action** is the action of $G$ on the *set* $G$ given by $g\cdot x = gx$. An action is **faithful** when its [[Def - Kernel and Image|kernel]] is trivial. The full notation registry lives on the parent page [[Group Theory II — §1.3–1.4]].

---

# Statement

> **Theorem (Cayley).** Every group $G$ is [[Def - Isomorphism|isomorphic]] to a [[Def - Subgroup|subgroup]] of $\operatorname{Sym}(G)$. Concretely, the **left-regular action** of $G$ on itself, $g\cdot x = gx$, has [[Def - Permutation Group|permutation representation]] $\rho : G \to \operatorname{Sym}(G)$, $\rho(g) = (x\mapsto gx)$, and this homomorphism has trivial [[Def - Kernel and Image|kernel]]. Hence by the [[Thm - First Isomorphism Theorem|first isomorphism theorem]]
> $$G \;\cong\; \operatorname{im}\rho \;\leq\; \operatorname{Sym}(G).$$

> **Finite form.** If $|G| = n$, then $\operatorname{Sym}(G) \cong S_n$, so $G$ is isomorphic to a subgroup of $S_n$. Every group of order $n$ embeds in the symmetric group on $n$ letters.

The theorem identifies the abstract notion of "group" with the concrete notion of "[[Def - Permutation Group|permutation group]]": these are the same class of object. The cost is severity of the embedding — a group of order $n$ is realised inside a group of order $n!$ — so the theorem is decisive in principle and almost never the right tool in practice.

---

# Motivation

Group theory is built from two pictures that look unrelated. The first is abstract: a group is a set with an associative binary operation, an identity, and inverses — the axioms of [[Def - Group]], with no reference to what the elements *are*. The second is concrete and historically prior: a group is a collection of symmetries — bijections of some set that you can compose and undo — a [[Def - Permutation Group|permutation group]] sitting inside a [[Def - Symmetric Group|symmetric group]]. Felix Klein's symmetries of geometric figures, Galois's permutations of the roots of a polynomial: these were groups before anyone wrote down the axioms.

The natural worry is that the abstract definition might be *too generous*. Perhaps the axioms admit exotic groups that are not symmetries of anything — objects with the right algebraic shape but no realisation as permutations. If so, "permutation group" would be a strictly narrower notion than "group", and the concrete picture would be merely a rich source of examples rather than the whole story.

Cayley's theorem says the worry is unfounded. There is no gap. Every group whatsoever — however abstractly presented, however exotic — is isomorphic to a group of permutations. The abstract axioms generate exactly the class of objects the concrete picture already described. This is a closure statement: it certifies that nothing was lost in passing to the axioms, and nothing exotic was gained. The slogan "a group is a set of symmetries" is not propaganda; it is a theorem.

The construction that proves it is the most economical imaginable. To realise $G$ as permutations you must produce a set for it to permute, and the theorem's idea is to use $G$ *itself* as that set: the element $g$ acts on the set $G$ by left multiplication, $x \mapsto gx$. A group always has itself lying around, so the construction needs no external input — which is precisely why the theorem holds with no hypotheses at all. The price of this universality is that the set $G$ is as large as the group, so the embedding lands in the vast symmetric group $S_n$; the theorem buys generality by spending efficiency.

---

# Sources and Targets

This section is not an input/output summary. Sources record the non-obvious circumstances in which the theorem's hypothesis — *being a group* — is the operative fact. Targets record what the conclusion (an embedding into a symmetric group) yields when combined with one further property. Since the hypothesis "is a group" is maximally weak, the sources here are less about *reaching* the hypothesis and more about recognizing when the *embedding into $S_n$* is the move to make.

**Sources (Input Broadening)**

The hypothesis is simply "$G$ is a group" — there is nothing to broaden. What needs recognizing is the *trigger*: the circumstances under which one should reach for Cayley's embedding.

The first trigger is **you must prove a fact about all groups by reducing to permutation groups**. Property $B$ is "the claim is a statement about an arbitrary abstract group $G$, but you have a proof technique that only works for [[Def - Permutation Group|permutation groups]]". The bridge is Cayley: replace $G$ by its isomorphic copy inside $\operatorname{Sym}(G)$, prove the claim there, and transport it back along the isomorphism. The implication is non-obvious because the original $G$ carried no permutations; Cayley *manufactures* them. Example: any theorem about cycle structure, sign, or fixed points — concepts that only make sense for permutations — can be brought to bear on an abstract group through its regular representation.

The second trigger is **you want to bound or describe a group by an ambient symmetric group**. Property $B$ is "$|G| = n$ and you wish to constrain $G$'s structure". The bridge is that $G \hookrightarrow S_n$, so $G$ inherits every constraint that subgroups of $S_n$ satisfy — for instance, $G$ embeds in a group with a sign homomorphism. The implication is non-obvious because an abstractly given group of order $n$ has no a priori relationship to $S_n$. Example: the proof that finite groups have faithful linear representations begins by embedding $G$ into $S_n$ and then $S_n$ into $\mathrm{GL}_n$ by permutation matrices.

The third trigger is **a left-multiplication action arises and you need its kernel**. Property $B$ is "the construction in front of you is $G$ (or a coset space) under left multiplication". The bridge is the regular action's defining feature: left multiplication is *free* — only $e$ fixes any point — so the kernel is trivial. The implication is non-obvious because triviality of a kernel usually takes an argument; here it is one line (evaluate at $e$). Example: this is the kernel computation that makes [[Thm - Cayley's Theorem|Cayley]] an embedding, and the same freeness underlies why the [[Thm - Coset Action and the Normal Core|coset action]]'s kernel sits *inside* $H$.

**Targets (Output Amplification)**

The conclusion is an embedding $G \hookrightarrow \operatorname{Sym}(G)$, finitely $G \hookrightarrow S_n$ for $n = |G|$.

The first combination is **embedding plus the sign homomorphism on $S_n$**. The conclusion places $G$ inside $S_n$. Add property $D$: $S_n$ carries the sign homomorphism $\operatorname{sgn} : S_n \to \{\pm 1\}$. Composing the embedding with $\operatorname{sgn}$ gives a homomorphism $G \to \{\pm 1\}$, and analysing *which* regular-representation permutations are odd produces structural information. The further result $E$: if $|G|$ is even and a Sylow $2$-subgroup of $G$ is cyclic, then $G$ has a normal subgroup of index $2$ — proved by showing an element of order $2^k$ acts in the regular representation as an odd permutation. The combination is non-obvious because the parity of a permutation has no meaning until $G$ is *inside* a symmetric group, which is exactly what Cayley arranges.

The second combination is **embedding plus a faithful permutation representation gives a faithful matrix representation**. The conclusion gives $G \hookrightarrow S_n$. Add property $D$: $S_n \hookrightarrow \mathrm{GL}_n(\mathbb{F})$ by permutation matrices (the matrix with $1$s placed by the permutation). The composite is an injective homomorphism $G \to \mathrm{GL}_n(\mathbb{F})$. The result $E$: every finite group has a faithful linear representation, hence is a group of matrices. The combination is non-obvious because it bridges two embeddings — into permutations, then into matrices — neither of which is visible from the abstract group.

The third combination is **embedding plus "the image lies in a known subgroup" pins down $G$ up to isomorphism**. The conclusion realises $G$ as a subgroup of $\operatorname{Sym}(G)$. Add property $D$: by inspecting the regular representation you locate the image inside a recognizable subgroup of $S_n$ — say, all the $\rho(g)$ are products of $n/\operatorname{ord}(g)$ disjoint cycles of equal length. The result $E$ is a concrete combinatorial model of $G$ as an explicit permutation group, from which orders, conjugacy, and generation can be read off by hand. The combination is non-obvious because the abstract $G$ gave no permutations to inspect; Cayley supplies a canonical, fully explicit list.

---

# Why Is It True

The theorem should feel almost forced, once you ask the right question: to realise $G$ as symmetries, *what is there for it to be symmetries of?*

An abstract group is handed to you with no accompanying set — no polygon, no roots, no space. So if $G$ is to permute something, the something must be built from $G$ alone. There is one obvious candidate: the underlying set of $G$ itself. The theorem's whole idea is to forget that $G$ is a group, regard it as a plain set of $n$ points, and let the group $G$ shuffle those points.

How should $g$ shuffle them? The natural rule is left multiplication: $g$ sends the point $x$ to the point $gx$. Why is this a *shuffle* — a bijection — rather than some lossy rearrangement? Because in a group, left multiplication by $g$ is undoable: multiply by $g^{-1}$ to get back. "Move every point by $g$" can be reversed by "move every point by $g^{-1}$", so it is a bijection of the set $G$. This is the cancellation law, and it is the entire reason a group's multiplication table has each element exactly once in every row — every row of the table *is* the permutation $\rho(g)$.

Now, why is this assignment $g \mapsto \rho(g)$ injective — why is the embedding faithful? Suppose $g$ acts as the identity permutation: it fixes *every* point of $G$. Then in particular it fixes the point $e$. But $g$ acting on $e$ is $ge = g$. So if $g$ fixes $e$, then $g = e$. The only element that shuffles nothing is the identity. This is the crux, and it is short because left multiplication is *free*: there is a point — indeed every point — that only the identity fixes. (Contrast conjugation, where central elements fix everything; the regular action has no such elements precisely because $gx = x$ already forces $g = e$ by cancellation, without even needing a special point.) An injective homomorphism is an isomorphism onto its image, so $G$ is isomorphic to the permutation group $\operatorname{im}\rho$.

Stand back and the theorem is the statement that *a group is its own multiplication table*. Each element $g$ contributes one row of the table, and that row, read as "where does each column-element go", is a permutation of the $n$ elements. Composing rows corresponds to composing permutations because $g$ then $h$ sends $x$ to $h(gx) = (hg)x$. The group law and the composition of these table-rows are the same operation. So every group, with no exceptions and no hypotheses, *is* the group of row-permutations of its own Cayley table — which is a group of permutations. The only reason this is a theorem and not a triviality is that one must check the rows are genuinely distinct permutations, and that is the faithfulness argument above.

The reason the theorem is impractical follows from the same picture. The set being permuted is all of $G$, so it has $n = |G|$ points, and the ambient symmetric group is $S_n$ of order $n!$. To study a group of order $12$ you are sent into $S_{12}$, a group of order nearly half a billion. The regular representation is the most *wasteful* faithful action — it uses the largest possible set. Useful actions use small sets (cosets of a large subgroup, geometric features), and finding them is the real work of the topic; Cayley's value is the existence statement, not the embedding it provides.

---

# What Makes This Hard

There is no hard step — the difficulty is conceptual, not technical. The one place to be careful is the choice of action: it must be *left* multiplication $g\cdot x = gx$, not right multiplication $g\cdot x = xg$, because $g\cdot(h\cdot x) = g(xh) = (gx)h$ does **not** equal $(gh)\cdot x = x(gh)$ — right multiplication is an anti-homomorphism, and the standard fix is $g\cdot x = xg^{-1}$. The faithfulness argument is the genuine content and the commonest place to under-explain: one must say *why* the kernel is trivial, and the reason is the specific freeness of the regular action (evaluate the fixing condition at the point $e$), not a general fact about actions.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Make $G$ act on its own underlying set by left multiplication. By [[Thm - Actions Correspond to Homomorphisms]] this is a homomorphism $\rho : G \to \operatorname{Sym}(G)$. Show its kernel is trivial — an element fixing every point in particular fixes $e$, and fixing $e$ forces the element to be $e$. Then the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives $G \cong \operatorname{im}\rho \leq \operatorname{Sym}(G)$.

**Subgoal decomposition:**

1. **Left multiplication is an action of $G$ on the set $G$.** Verify $g\cdot x := gx$ satisfies $e\cdot x = x$ and $g_1\cdot(g_2\cdot x) = (g_1g_2)\cdot x$.
   - *Hint:* $e\cdot x = ex = x$; and $g_1\cdot(g_2\cdot x) = g_1(g_2 x) = (g_1 g_2)x$ by associativity in $G$.
   - *Why needed:* It produces, via [[Thm - Actions Correspond to Homomorphisms]], the homomorphism $\rho : G \to \operatorname{Sym}(G)$ that is the whole proof.

2. **The kernel of $\rho$ is trivial.** Show that if $g\cdot x = x$ for *all* $x \in G$, then $g = e$.
   - *Hint:* The hypothesis holds in particular at $x = e$: $g\cdot e = ge = g$, and this is required to equal $e$.
   - *Why needed:* A trivial kernel is what turns the homomorphism into an *embedding* rather than a mere quotient map.

3. **Conclude the embedding.** Apply the [[Thm - First Isomorphism Theorem|first isomorphism theorem]]: $G/\ker\rho \cong \operatorname{im}\rho$, and with $\ker\rho = \{e\}$ this reads $G \cong \operatorname{im}\rho \leq \operatorname{Sym}(G)$.
   - *Hint:* $G/\{e\} \cong G$; the image is a subgroup of the codomain.
   - *Why needed:* This is the statement of the theorem.

4. **Finite form.** If $|G| = n$, note $\operatorname{Sym}(G) \cong S_n$ by any bijection $G \leftrightarrow \{1, \dots, n\}$, so $G$ embeds in $S_n$.
   - *Hint:* A bijection of sets induces an isomorphism of their symmetric groups.
   - *Why needed:* It states the theorem in the form actually used: order-$n$ groups live in $S_n$.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

<details>
<summary><strong>Lemma 1: Left multiplication is a group action of $G$ on itself</strong></summary>

**Statement:** For a group $G$, the map $G \times G \to G$ defined by $g\cdot x = gx$ (the product in $G$) is an [[Def - Group Action|action]] of $G$ on the underlying set of $G$.

**Hint:** Check the two action axioms; both reduce to associativity and the identity law of $G$.

**Why needed:** It is the action whose permutation representation *is* Cayley's embedding.

<details>
<summary>Full proof</summary>

*Identity axiom:* $e\cdot x = ex = x$ for all $x \in G$, by the identity law of $G$.

*Associativity axiom:* for all $g_1, g_2, x \in G$,
$$g_1\cdot(g_2\cdot x) = g_1\cdot(g_2 x) = g_1(g_2 x) = (g_1 g_2)x = (g_1 g_2)\cdot x,$$
the middle equality being associativity of the group operation. Both axioms hold, so $g\cdot x = gx$ is an action.

</details>

</details>

<details>
<summary><strong>Lemma 2: The regular action is faithful</strong></summary>

**Statement:** Let $\rho : G \to \operatorname{Sym}(G)$ be the permutation representation of the left-regular action. Then $\ker\rho = \{e\}$.

**Hint:** An element of the kernel fixes every point; test the condition at the single point $e$.

**Why needed:** Triviality of the kernel is precisely what makes $\rho$ injective, hence an embedding.

<details>
<summary>Full proof</summary>

Let $g \in \ker\rho$. By definition $\rho(g) = \operatorname{id}_G$, i.e. $g\cdot x = x$ for every $x \in G$. Apply this at $x = e$:
$$g = ge = g\cdot e = e.$$
So the only element of the kernel is $e$, and $\ker\rho = \{e\}$.

</details>

</details>

<details>
<summary><strong>Lemma 3: An injective homomorphism is an isomorphism onto its image</strong></summary>

**Statement:** If $\varphi : G \to K$ is a [[Def - Homomorphism|homomorphism]] with $\ker\varphi = \{e\}$, then $\varphi$ restricts to an [[Def - Isomorphism|isomorphism]] $G \cong \operatorname{im}\varphi$.

**Hint:** This is the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] in the special case of a trivial kernel.

**Why needed:** It is the final step converting the faithful action into the asserted isomorphism $G \cong \operatorname{im}\rho$.

<details>
<summary>Full proof</summary>

The first isomorphism theorem gives an isomorphism $G/\ker\varphi \xrightarrow{\sim} \operatorname{im}\varphi$ induced by $\varphi$. When $\ker\varphi = \{e\}$, the quotient $G/\{e\}$ is canonically isomorphic to $G$ (the cosets $g\{e\} = \{g\}$ are the singletons). Composing, $G \cong G/\{e\} \cong \operatorname{im}\varphi$, and the composite is $\varphi$ with codomain restricted to its image. Hence $\varphi : G \to \operatorname{im}\varphi$ is an isomorphism.

</details>

</details>

---

# Formal Proof

<details>
<summary><strong>Complete formal proof</strong></summary>

**Theorem (Cayley).** Every group $G$ is isomorphic to a subgroup of $\operatorname{Sym}(G)$.

*Proof.* Define an action of $G$ on its own underlying set by
$$g \ast x = gx \qquad (g, x \in G),$$
the product taken in $G$. This is an action: $e\ast x = ex = x$, and
$$g_1\ast(g_2\ast x) = g_1(g_2 x) = (g_1 g_2)x = (g_1\cdot g_2)\ast x$$
by associativity. By [[Thm - Actions Correspond to Homomorphisms]], this action is the same data as a homomorphism
$$\rho : G \to \operatorname{Sym}(G), \qquad \rho(g) = (x \mapsto gx).$$

We compute the kernel. Suppose $g \in \ker\rho$, so $g$ acts trivially on every element of $G$. In particular it acts trivially on the identity:
$$g\ast e = e \quad\Longrightarrow\quad ge = e \quad\Longrightarrow\quad g = e.$$
Hence $\ker\rho = \{e\}$.

By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]],
$$G \;\cong\; G/\ker\rho \;\cong\; \operatorname{im}\rho \;\leq\; \operatorname{Sym}(G).$$
So $G$ is isomorphic to a subgroup of $\operatorname{Sym}(G)$. $\qquad\blacksquare$

**Finite form.** If $|G| = n$, any bijection $G \leftrightarrow \{1, \dots, n\}$ induces an isomorphism $\operatorname{Sym}(G) \cong S_n$. Composing with the embedding above realises $G$ as a subgroup of $S_n$. $\qquad\blacksquare$

This is the Cayley's theorem example of §1.3 of the source lecture notes; the proof there is exactly the kernel computation for the left-regular action.

</details>

---

# Cross-Field Exercise Suggestions

The aim is to find settings where Cayley's embedding is the productive move, even when no symmetric group is mentioned.

**Universal algebra: every monoid embeds in a transformation monoid.** Cayley's theorem is the group-theoretic case of a pattern that runs through all of algebra: every monoid $M$ embeds in the monoid of *all* functions $M \to M$ via left multiplication (the Cayley theorem for monoids), and every small category embeds in a category of sets and functions (the Yoneda embedding). The application is non-obvious because these look like separate theorems in separate subjects; the unifying property $B$ is "an associative composition", and "act on yourself by left composition" is the universal embedding trick. Recognizing Cayley as one instance of Yoneda is a genuine cross-field insight.

**Combinatorics: the Cayley table is a Latin square.** Because each $\rho(g)$ is a permutation, every row of a group's multiplication table is a permutation of the elements; the same holds for columns (right multiplication). So the multiplication table of any finite group is a Latin square — each symbol once per row and once per column. The application is non-obvious because the Latin-square property looks like a combinatorial design fact, but it is exactly the statement that left and right multiplications are bijections, i.e. the engine of Cayley's theorem. Conversely, not every Latin square is a group table, which sharpens the question of *which* designs are groups.

**Computer science: groups as concrete data structures.** To represent an abstractly specified finite group on a computer — for algorithms computing orders, testing membership, finding subgroups — one needs a concrete model, and Cayley's theorem guarantees one always exists: store each element as a permutation of $\{1, \dots, n\}$. This is the theoretical basis of permutation-group algorithms (the Schreier–Sims algorithm and the computer algebra systems built on it). The application is non-obvious because it turns an existence theorem into an implementation strategy: "every group *is* a permutation group" becomes "every group *can be stored as* permutations".

**Representation theory: the regular representation.** Composing Cayley's embedding $G \hookrightarrow S_n$ with the permutation-matrix embedding $S_n \hookrightarrow \mathrm{GL}_n(\mathbb{C})$ produces the *regular representation* of $G$ — the linear representation on the vector space $\mathbb{C}[G]$ with basis the group elements. This representation is the cornerstone of character theory: it contains every irreducible representation of $G$, each with multiplicity equal to its dimension. The application is non-obvious because the regular representation is usually introduced abstractly as functions on $G$; its DNA is Cayley's left-regular action made linear.

---

# Bridges

- **[[Thm - Actions Correspond to Homomorphisms|Actions Correspond to Homomorphisms]]** — Cayley's theorem is *built on* this correspondence. The left-regular action is recognized as a homomorphism $G \to \operatorname{Sym}(G)$ only because that theorem licenses the translation; without it, "the regular action" would not be an embeddable map. Cayley is the headline instance of the action-homomorphism dictionary.

- **[[Thm - Coset Action and the Normal Core|Coset Action and the Normal Core]]** — the coset action is the *refinement* of Cayley that makes it practical. Cayley acts on $G/\{e\} = G$, the largest possible coset space; the coset action acts on $G/H$ for a non-trivial $H$, a smaller set, embedding $G/K$ into a smaller symmetric group $S_n$ with $n = |G:H|$. Cayley is the coset action at $H = \{e\}$; choosing a large $H$ trades the embedding's faithfulness for a much smaller target.

- **[[Thm - Orbit-Stabiliser Theorem|Orbit-Stabiliser Theorem]]** — the left-regular action is *transitive* (any $x$ reaches any $y$ via $g = yx^{-1}$) and *free* (stabilisers are trivial), so orbit-stabiliser reads $|G| = |G_x|\cdot|G\cdot x| = 1\cdot|G|$ — a tautology. Cayley extracts structure from the regular action not through orbit counting but through the *kernel*; it is the action whose orbit-stabiliser content is empty and whose homomorphism content is everything.

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]** — both theorems study a group through left multiplication, but on different sets: Lagrange restricts left multiplication by $H$ to partition $G$ into cosets, Cayley uses left multiplication by all of $G$ to permute $G$. They are two faces of the regular action — Lagrange the *orbit* face (cosets of $H$), Cayley the *kernel* face (the whole-group representation).

- **Yoneda Lemma** *(from Category Theory)* — Cayley's theorem is the one-object case of the Yoneda embedding. A group is a category with a single object whose arrows are the group elements; the Yoneda embedding sends this category faithfully into a category of set-valued functors, and unwinding the single-object case yields exactly "act on yourself by left multiplication". Cayley is Yoneda specialised from categories to groups.
