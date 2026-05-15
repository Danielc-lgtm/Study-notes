---
type: theorem
subject: group-theory
prereqs:
  - "Def - Group Action"
  - "Def - Symmetric Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Def - Normal Subgroup"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Notation

$G$ is a group with identity $e$ and operation written by juxtaposition; $X$ is a set. An [[Def - Group Action|action]] of $G$ on $X$ is a map $G \times X \to X$, written $(g, x) \mapsto g \cdot x$, satisfying $e \cdot x = x$ and $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$. For a set $X$, the [[Def - Symmetric Group|symmetric group]] $\operatorname{Sym}(X)$ is the group of all bijections $X \to X$ under composition. A [[Def - Homomorphism|homomorphism]] $\rho : G \to \operatorname{Sym}(X)$ is a map with $\rho(g_1 g_2) = \rho(g_1) \circ \rho(g_2)$; such a homomorphism is called a **permutation representation** of $G$. Its [[Def - Kernel and Image|kernel]] is $\ker\rho = \{g : \rho(g) = \operatorname{id}_X\}$ and its image is $\operatorname{im}\rho = \{\rho(g) : g \in G\} \leq \operatorname{Sym}(X)$. Following the lecture notes we write $G^X = \operatorname{im}\rho$ and $G_X = \ker\rho$. The full notation registry lives on the parent page [[Group Theory II — §1.3–1.4]].

---

# Statement

> **Theorem (Actions correspond to homomorphisms).** Let $G$ be a group and $X$ a set. An [[Def - Group Action|action]] of $G$ on $X$ is the same data as a [[Def - Homomorphism|homomorphism]] $\rho : G \to \operatorname{Sym}(X)$. Precisely:
> - Given an action $(g, x) \mapsto g \cdot x$, the map $\rho$ defined by $\rho(g) = (x \mapsto g \cdot x)$ takes values in $\operatorname{Sym}(X)$ and is a homomorphism.
> - Given a homomorphism $\rho : G \to \operatorname{Sym}(X)$, the map $g \cdot x := \rho(g)(x)$ is an action.
>
> These two constructions are mutually inverse, so the two notions carry identical information.

> **Consequence (kernel, image, first isomorphism theorem).** For the homomorphism $\rho$ of an action, write $G_X = \ker\rho$ and $G^X = \operatorname{im}\rho$. Then $G_X \trianglelefteq G$ is a [[Def - Normal Subgroup|normal subgroup]] — the set of elements acting trivially on every point — and $G^X \leq \operatorname{Sym}(X)$ is a [[Def - Permutation Group|permutation group]]. By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]],
> $$G / G_X \;\cong\; G^X.$$
> In particular, if the action is **faithful** ($G_X = \{e\}$), then $G \cong G^X \leq \operatorname{Sym}(X)$ — the group $G$ is realised concretely as permutations of $X$.

The lecture notes label this result a Lemma and add the warning that "the statement of this lemma by itself is useless" — what matters is the explicit translation in the proof, since that is what lets the entire theory of homomorphisms be imported into the study of actions.

---

# Motivation

The [[Def - Group Action|definition of a group action]] is a map $G \times X \to X$ subject to two axioms. It is the right object to *verify* — given a candidate rule for how $G$ moves the points of $X$, you check $e \cdot x = x$ and $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$ — but it is the wrong object to *think with*. The axioms look like ad hoc compatibility conditions, and from the definition alone it is not clear what an action is *for*.

This theorem supplies the answer by giving the action its true name. An action is not a strange two-variable map; it is a [[Def - Homomorphism|homomorphism]] from $G$ into the [[Def - Symmetric Group|symmetric group]] of $X$. The two action axioms are exactly the two homomorphism axioms in disguise: the associativity axiom $g_1 \cdot (g_2 \cdot x) = (g_1 g_2)\cdot x$ says $\rho(g_1) \circ \rho(g_2) = \rho(g_1 g_2)$, and the identity axiom $e \cdot x = x$ says $\rho(e) = \operatorname{id}_X$. So the definition of an action was never arbitrary — it is precisely what is needed for the rule $g \mapsto (x \mapsto g \cdot x)$ to be a homomorphism.

Why does the reformulation matter so much? Because [[Group Theory I — §1.1–1.2]] built an entire toolkit for homomorphisms — kernels, images, the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] — and that toolkit was stranded as long as actions were thought of as bare maps. Recognizing an action as a homomorphism unstrands it. The kernel of $\rho$ becomes available, and a kernel is a [[Def - Normal Subgroup|normal subgroup]] — so every action of $G$ silently produces a normal subgroup of $G$, the elements the action "cannot see". This single observation is the source of more normal subgroups in finite group theory than any other; it is what makes the [[Thm - Coset Action and the Normal Core|coset action]] manufacture normal subgroups out of nothing but a subgroup, and it is the conceptual hinge on which [[Thm - Cayley's Theorem|Cayley's theorem]] turns. The theorem answers the question "what is an action, really?", and the answer reroutes the whole topic through machinery already built.

---

# Sources and Targets

This section is not an input/output summary. Sources record the non-obvious circumstances under which you find yourself holding the hypothesis — here, *an action of $G$ on a set*. Targets record what becomes provable once the conclusion (an action *is* a homomorphism, with kernel and image in hand) is combined with one further fact.

**Sources (Input Broadening)**

The hypothesis is "$G$ acts on a set $X$". The skill is recognizing an action where the problem advertises something else.

The first source is **$G$ is given as a subgroup of some $\operatorname{Sym}(X)$**, i.e. as a concrete [[Def - Permutation Group|permutation group]]. Property $B$ is "$G \leq \operatorname{Sym}(X)$". The bridge is that the inclusion $G \hookrightarrow \operatorname{Sym}(X)$ is itself a homomorphism, so by this theorem $G$ acts on $X$ with $g \cdot x = g(x)$ — the *tautological* action. The implication is non-obvious only because a permutation group does not announce itself as "acting"; it is just sitting inside a symmetric group. But once you read the inclusion as a homomorphism, every orbit-stabiliser argument is available. Example: the [[Group Theory I — §1.1–1.2|dihedral group]] $D_{2n}$ presented as symmetries of an $n$-gon is a subgroup of $\operatorname{Sym}(\{1, \dots, n\})$, hence acts on the $n$ vertices.

A second source is **a geometric symmetry group acting on a feature set**. Property $B$ is "$G$ is the group of symmetries of some object $\mathcal{O}$, and $X$ is a set of features of $\mathcal{O}$ — faces, edges, vertices, diagonals". The bridge is that a symmetry permutes the features, and this rule satisfies the action axioms because composing symmetries composes the induced permutations. The implication is non-obvious because the symmetry is a rigid motion of space, not a function on a finite set; the theorem says the induced finite permutation assemble into a genuine homomorphism $G \to \operatorname{Sym}(X)$. Example: the symmetry group of the cube acts on its four space diagonals, giving $\rho : G \to \operatorname{Sym}(X) \cong S_4$ — the worked example in the lecture notes, used to count $|G| = 48$.

A third source is **a homomorphism $G \to S_n$ produced by some unrelated construction**. Property $B$ is "you have, by whatever means, a homomorphism $\rho : G \to S_n$". The bridge is *this theorem read backwards*: a homomorphism into a symmetric group **is** an action, so you may immediately speak of orbits and stabilisers of $\{1, \dots, n\}$ under $G$. The implication is non-obvious because a homomorphism is usually thought of as something to take a kernel of, not something with orbits. Example: the [[Thm - Coset Action and the Normal Core|coset action]] is first met as a homomorphism $G \to S_n$; recognizing it as an action is what lets orbit-stabiliser be applied to it.

A fourth source is **$G$ acts on a structured set, and you want the structure respected**. Property $B$ is "$X$ is itself a group (or a vector space, or a topological space) and $G$ acts by structure-preserving maps". The bridge is that the homomorphism then lands not in all of $\operatorname{Sym}(X)$ but in the subgroup of structure-preserving bijections — $\operatorname{Aut}(X)$, or $\mathrm{GL}(V)$, or the homeomorphism group. The implication is non-obvious because it requires checking that each $\rho(g)$ preserves the extra structure, which the bare action axioms do not guarantee. Example: conjugation of $G$ on itself lands in $\operatorname{Aut}(G)$, not merely $\operatorname{Sym}(G)$ — this is exactly the observation that opens §1.4 and defines the [[Def - Automorphism Group|inner automorphisms]].

**Targets (Output Amplification)**

The conclusion is: an action is a homomorphism $\rho$, with a kernel $G_X = \ker\rho \trianglelefteq G$, an image $G^X = \operatorname{im}\rho \leq \operatorname{Sym}(X)$, and $G/G_X \cong G^X$.

The first combination is **conclusion plus "$X$ is small" forces a divisibility constraint**. The conclusion gives $G/G_X \hookrightarrow \operatorname{Sym}(X)$. Add property $D$: $|X| = n$ is small, so $\operatorname{Sym}(X) \cong S_n$ has order $n!$. Then $|G/G_X|$ divides $n!$, by [[Thm - Lagrange's Theorem|Lagrange]]. The further result $E$ is a hard cap on the index of the kernel: $|G : G_X| \mid n!$. The combination is non-obvious because the action was set up to study how $G$ moves $X$, yet it silently constrains the arithmetic of $G$. This is the entire engine of [[Thm - Coset Action and the Normal Core|the coset action]] and its non-simplicity corollary.

The second combination is **conclusion plus "the action is non-trivial" forces a proper non-trivial normal subgroup, hence non-simplicity**. The conclusion gives $G_X \trianglelefteq G$. Add property $D$: the action moves some point (so $G_X \neq G$) but also fails to be faithful (so $G_X \neq \{e\}$). The result $E$ is that $G_X$ is a proper non-trivial normal subgroup, so $G$ is **not** [[Def - Simple Group|simple]]. The combination is non-obvious because "$G$ is not simple" is a deep structural statement and the only input was a set $G$ happens to act on. This is the standard non-simplicity argument and the reason actions are hunted for whenever simplicity is in question.

The third combination is **conclusion plus a faithful action embeds $G$ concretely**. The conclusion gives $G/G_X \cong G^X$. Add property $D$: the action is faithful, $G_X = \{e\}$. Then $G \cong G^X \leq \operatorname{Sym}(X)$ outright — an isomorphism, not just a quotient. The result $E$ is a concrete model of the abstract group $G$ as honest permutations. The combination is non-obvious because faithfulness is a mild-looking condition (only $e$ acts trivially) yet it upgrades a quotient statement to an embedding. This is precisely what [[Thm - Cayley's Theorem|Cayley's theorem]] exploits.

The fourth combination is **conclusion plus the image is computed gives the order of $G$**. The conclusion gives $|G| = |G_X| \cdot |G^X|$ (from $G/G_X \cong G^X$ and [[Thm - Lagrange's Theorem|Lagrange]]). Add property $D$: you can identify both the kernel $G_X$ and the image $G^X$ explicitly. The result $E$ is the order $|G|$ as a product of two computable numbers. The combination is non-obvious because $|G|$ is the unknown and the action seemed only to rearrange known points. The cube example does exactly this: $G_X \cong C_2$, $G^X \cong S_4$, hence $|G| = 2 \cdot 24 = 48$.

---

# Why Is It True

The result should feel not just true but inevitable, once you ask what the two action axioms are *for*.

Start from the action and watch what each axiom buys. Fix $g \in G$ and consider the rule $\sigma_g : x \mapsto g \cdot x$, a function $X \to X$. Is it a bijection? It has an obvious candidate inverse: the rule $\sigma_{g^{-1}} : x \mapsto g^{-1} \cdot x$. Composing them, $\sigma_{g^{-1}}(\sigma_g(x)) = g^{-1} \cdot (g \cdot x)$, and *here is where the associativity axiom is doing its job*: it rewrites this as $(g^{-1} g) \cdot x = e \cdot x$, and the identity axiom finishes it as $x$. So $\sigma_{g^{-1}} \circ \sigma_g = \operatorname{id}_X$, and symmetrically the other way, so $\sigma_g$ is a bijection with inverse $\sigma_{g^{-1}}$. The two axioms were exactly enough to guarantee that "act by $g$" is undoable. That is why $\rho(g) = \sigma_g$ lands in $\operatorname{Sym}(X)$ at all.

Now ask whether $g \mapsto \sigma_g$ respects multiplication. We want $\sigma_{g_1} \circ \sigma_{g_2} = \sigma_{g_1 g_2}$. Apply the left side to a point: $\sigma_{g_1}(\sigma_{g_2}(x)) = g_1 \cdot (g_2 \cdot x)$. And the associativity axiom is *literally the assertion* that this equals $(g_1 g_2) \cdot x = \sigma_{g_1 g_2}(x)$. There is nothing to prove beyond reading the axiom. The associativity axiom of an action and the homomorphism property of $\rho$ are the same sentence, written once with a dot and once with a circle.

So the forward direction is not a construction with a clever idea; it is a *change of notation*. "Act by $g$" is a permutation because the axioms make it reversible; "acting by $g_1$ then $g_2$ is acting by $g_1 g_2$" is the homomorphism law because the associativity axiom said so. The reverse direction is the same observation run backwards: if you are *handed* a homomorphism $\rho$, define $g \cdot x = \rho(g)(x)$ and the homomorphism laws hand you back the action axioms — $\rho(g_1 g_2) = \rho(g_1)\circ\rho(g_2)$ gives associativity, $\rho(e) = \operatorname{id}$ gives the identity axiom. And the two passages are visibly inverse: starting from an action, building $\rho$, and reading off $\rho(g)(x)$ returns $g \cdot x$ unchanged; starting from $\rho$, building the action, and bundling it back into a homomorphism returns $\rho$ unchanged. Nothing is lost or added in either direction because each axiom on one side is a single axiom on the other.

The kernel consequence is then immediate intuition rather than extra work. A homomorphism always has a kernel, and a kernel is always a [[Def - Normal Subgroup|normal subgroup]] — that is a fact from [[Group Theory I — §1.1–1.2]]. Translated through the dictionary, $\ker\rho$ is the set of $g$ with $\sigma_g = \operatorname{id}_X$, that is, the elements that move *no* point of $X$. So "the elements an action cannot detect" is automatically a normal subgroup, for the single reason that it is a kernel. And $G/\ker\rho \cong \operatorname{im}\rho$ is just the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] with the dictionary applied: the part of $G$ the action *can* see, namely $G^X$, is $G$ with its blind spot $G_X$ quotiented away. None of this is surprising once the action is a homomorphism — it is the standard behaviour of homomorphisms, inherited wholesale.

---

# What Makes This Hard

The result is not hard to prove — it is hard to *value*, which is the lecture notes' point that the statement "by itself is useless" and the proof is what matters. The genuine content is the explicit two-way dictionary: $\rho(g) = (x \mapsto g\cdot x)$ one way, $g \cdot x = \rho(g)(x)$ the other. The one step people skip is verifying that $\rho(g)$ is actually a *bijection* (not merely a function) before calling it an element of $\operatorname{Sym}(X)$; this needs the inverse $\rho(g^{-1})$ and uses *both* axioms. The most common error is sloppiness about composition order — writing $\rho(g_1 g_2) = \rho(g_2)\circ\rho(g_1)$ — which happens if one mishandles the associativity axiom; the action axiom $g_1\cdot(g_2\cdot x)$ applies $g_2$ first, so $\rho$ is a genuine (not anti-) homomorphism only because the convention is consistent.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Build the map both ways and check each is the inverse of the other. Forward: send an action to $\rho(g) = (x \mapsto g\cdot x)$; show $\rho(g)$ is a bijection (its inverse is $\rho(g^{-1})$) and that $\rho$ is a homomorphism (the action's associativity axiom *is* the homomorphism law). Backward: send a homomorphism to the rule $g \cdot x = \rho(g)(x)$ and verify the two action axioms. Then observe the two passages are literally inverse. The kernel consequence is the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied to $\rho$.

**Subgoal decomposition:**

1. **From an action, $\rho(g)$ is a permutation.** Show the function $\rho(g) : x \mapsto g \cdot x$ is a bijection of $X$.
   - *Hint:* Exhibit $\rho(g^{-1})$ as its two-sided inverse; the composite $\rho(g^{-1})\circ\rho(g)$ sends $x$ to $g^{-1}\cdot(g\cdot x) = (g^{-1}g)\cdot x = e\cdot x = x$, using both axioms.
   - *Why needed:* Only bijections live in $\operatorname{Sym}(X)$, so this is what makes $\rho$ a map *into* $\operatorname{Sym}(X)$.

2. **From an action, $\rho$ is a homomorphism.** Show $\rho(g_1 g_2) = \rho(g_1)\circ\rho(g_2)$ and $\rho(e) = \operatorname{id}_X$.
   - *Hint:* Evaluate $(\rho(g_1)\circ\rho(g_2))(x) = g_1\cdot(g_2\cdot x)$; the associativity axiom rewrites this as $(g_1 g_2)\cdot x = \rho(g_1 g_2)(x)$. The identity axiom gives $\rho(e) = \operatorname{id}_X$.
   - *Why needed:* This is the forward construction's payload — an action yields a permutation representation.

3. **From a homomorphism, recover an action.** Given $\rho : G \to \operatorname{Sym}(X)$, set $g \cdot x := \rho(g)(x)$ and verify $e\cdot x = x$ and $g_1\cdot(g_2\cdot x) = (g_1 g_2)\cdot x$.
   - *Hint:* Both follow by unwinding definitions and using $\rho(e) = \operatorname{id}_X$, $\rho(g_1 g_2) = \rho(g_1)\circ\rho(g_2)$ — the homomorphism axioms run backwards.
   - *Why needed:* This is the backward construction; together with step 2 it gives maps in both directions.

4. **The two constructions are mutually inverse.** Check that action $\to \rho \to$ action returns the original, and $\rho \to$ action $\to \rho$ returns the original.
   - *Hint:* Both are immediate from the *definitions*: the recovered action sends $(g,x)$ to $\rho(g)(x) = g\cdot x$; the recovered homomorphism sends $g$ to $x\mapsto g\cdot x$, which is $\rho(g)$.
   - *Why needed:* This upgrades "two maps exist" to "the two notions are the same data".

5. **Kernel, image, first isomorphism theorem.** Conclude $G_X = \ker\rho \trianglelefteq G$, $G^X = \operatorname{im}\rho \leq \operatorname{Sym}(X)$, and $G/G_X \cong G^X$.
   - *Hint:* Kernels of homomorphisms are normal subgroups; images are subgroups of the codomain; the isomorphism is the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] for $\rho$. Faithful means $\ker\rho = \{e\}$, whence $G \cong G^X$.
   - *Why needed:* This is the entire reason the theorem is worth stating — it imports homomorphism machinery onto actions.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

<details>
<summary><strong>Lemma 1: Acting by a fixed group element is a permutation</strong></summary>

**Statement:** Let $G$ act on $X$. For each $g \in G$, the function $\sigma_g : X \to X$, $\sigma_g(x) = g\cdot x$, is a bijection, with inverse $\sigma_{g^{-1}}$.

**Hint:** Compose $\sigma_{g^{-1}}$ with $\sigma_g$ and collapse the result using the associativity axiom and then the identity axiom.

**Why needed:** It is what makes the assignment $g \mapsto \sigma_g$ a map into $\operatorname{Sym}(X)$ rather than merely into the monoid of all functions $X \to X$.

<details>
<summary>Full proof</summary>

For any $x \in X$,
$$\sigma_{g^{-1}}(\sigma_g(x)) = g^{-1}\cdot(g\cdot x) = (g^{-1}g)\cdot x = e\cdot x = x,$$
using the associativity axiom for the middle equality and the identity axiom for the last. Hence $\sigma_{g^{-1}}\circ\sigma_g = \operatorname{id}_X$. The same computation with $g$ and $g^{-1}$ interchanged gives $\sigma_g\circ\sigma_{g^{-1}} = \operatorname{id}_X$. A function with a two-sided inverse is a bijection, so $\sigma_g \in \operatorname{Sym}(X)$ with $(\sigma_g)^{-1} = \sigma_{g^{-1}}$.

</details>

</details>

<details>
<summary><strong>Lemma 2: The assignment $g \mapsto \sigma_g$ is a homomorphism</strong></summary>

**Statement:** Let $G$ act on $X$, and define $\rho(g) = \sigma_g$ as in Lemma 1. Then $\rho : G \to \operatorname{Sym}(X)$ satisfies $\rho(g_1 g_2) = \rho(g_1)\circ\rho(g_2)$ and $\rho(e) = \operatorname{id}_X$.

**Hint:** Evaluate both sides of the multiplicativity equation at an arbitrary point $x$ and apply the associativity axiom.

**Why needed:** This is the forward direction of the correspondence: an action produces a permutation representation.

<details>
<summary>Full proof</summary>

For any $x \in X$,
$$(\rho(g_1)\circ\rho(g_2))(x) = \rho(g_1)(\rho(g_2)(x)) = g_1\cdot(g_2\cdot x) = (g_1 g_2)\cdot x = \rho(g_1 g_2)(x),$$
the third equality being the action's associativity axiom. Since this holds for every $x$, the functions agree: $\rho(g_1)\circ\rho(g_2) = \rho(g_1 g_2)$. For the identity, $\rho(e)(x) = e\cdot x = x = \operatorname{id}_X(x)$ for all $x$, so $\rho(e) = \operatorname{id}_X$. Hence $\rho$ is a homomorphism.

</details>

</details>

<details>
<summary><strong>Lemma 3: A homomorphism into $\operatorname{Sym}(X)$ defines an action</strong></summary>

**Statement:** Let $\rho : G \to \operatorname{Sym}(X)$ be a homomorphism. Then the map $G \times X \to X$ defined by $g\cdot x := \rho(g)(x)$ satisfies the two axioms of a group action.

**Hint:** Unwind both axioms into statements about $\rho$ and use that $\rho$ is a homomorphism.

**Why needed:** This is the backward direction of the correspondence.

<details>
<summary>Full proof</summary>

*Identity axiom:* $e\cdot x = \rho(e)(x) = \operatorname{id}_X(x) = x$, since a homomorphism sends $e$ to the identity of the codomain.

*Associativity axiom:* for any $g_1, g_2 \in G$ and $x \in X$,
$$g_1\cdot(g_2\cdot x) = \rho(g_1)\big(\rho(g_2)(x)\big) = \big(\rho(g_1)\circ\rho(g_2)\big)(x) = \rho(g_1 g_2)(x) = (g_1 g_2)\cdot x,$$
the third equality being the homomorphism property of $\rho$. Both axioms hold, so $g\cdot x = \rho(g)(x)$ is an action.

</details>

</details>

<details>
<summary><strong>Lemma 4: The two constructions are mutually inverse</strong></summary>

**Statement:** The passage (action $\mapsto \rho$) of Lemma 2 and the passage ($\rho \mapsto$ action) of Lemma 3 are inverse to each other.

**Hint:** Apply one construction then the other and check the result agrees with the input by definition-chasing alone.

**Why needed:** It upgrades "there are maps both ways" to "an action and a permutation representation are literally the same data".

<details>
<summary>Full proof</summary>

Start with an action $\cdot$. Lemma 2 produces $\rho$ with $\rho(g)(x) = g\cdot x$. Lemma 3 applied to this $\rho$ produces the action $g \star x := \rho(g)(x) = g\cdot x$ — identical to the original.

Start with a homomorphism $\rho$. Lemma 3 produces the action $g\cdot x = \rho(g)(x)$. Lemma 2 applied to this action produces $\rho'$ with $\rho'(g) = (x\mapsto g\cdot x) = (x\mapsto\rho(g)(x)) = \rho(g)$, so $\rho' = \rho$.

Both round-trips are the identity, so the constructions are mutually inverse bijections between actions of $G$ on $X$ and homomorphisms $G \to \operatorname{Sym}(X)$.

</details>

</details>

<details>
<summary><strong>Lemma 5: Kernel is normal, and $G/G_X \cong G^X$</strong></summary>

**Statement:** For the permutation representation $\rho$ of an action, $G_X := \ker\rho$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$, $G^X := \operatorname{im}\rho$ is a subgroup of $\operatorname{Sym}(X)$, and $G/G_X \cong G^X$. If the action is faithful then $G \cong G^X \leq \operatorname{Sym}(X)$.

**Hint:** This is the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied verbatim to the homomorphism $\rho$.

**Why needed:** It is the consequence that makes the theorem useful — it routes every action through quotients and embeddings.

<details>
<summary>Full proof</summary>

By Lemmas 1–2, $\rho : G \to \operatorname{Sym}(X)$ is a homomorphism. For any homomorphism, the kernel is a normal subgroup of the domain and the image is a subgroup of the codomain; hence $G_X = \ker\rho \trianglelefteq G$ and $G^X = \operatorname{im}\rho \leq \operatorname{Sym}(X)$. Concretely, $g \in G_X$ if and only if $\rho(g) = \operatorname{id}_X$, i.e. if and only if $g\cdot x = x$ for all $x$ — the elements acting trivially everywhere.

The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied to $\rho$ gives an isomorphism $G/\ker\rho \cong \operatorname{im}\rho$, that is, $G/G_X \cong G^X$. If the action is faithful, $G_X = \{e\}$, and $G/\{e\} \cong G$, so $G \cong G^X \leq \operatorname{Sym}(X)$.

</details>

</details>

---

# Formal Proof

<details>
<summary><strong>Complete formal proof</strong></summary>

**Theorem.** An action of $G$ on $X$ is the same data as a homomorphism $\rho : G \to \operatorname{Sym}(X)$; the two constructions are mutually inverse.

*Proof.* **From an action to a homomorphism.** Let $\ast : G \times X \to X$ be an action. Define $\rho : G \to \operatorname{Sym}(X)$ by sending $g$ to the function $\rho(g) = (g \ast - : X \to X)$.

First, $\rho(g)$ is a permutation: the function $g^{-1}\ast -$ is a two-sided inverse for it, since
$$\rho(g^{-1})\big(\rho(g)(x)\big) = g^{-1}\ast(g\ast x) = (g^{-1}\cdot g)\ast x = e\ast x = x,$$
and a symmetric computation shows $\rho(g)\circ\rho(g^{-1}) = \operatorname{id}_X$. So $\rho(g) \in \operatorname{Sym}(X)$, and $\rho$ is a well-defined function $G \to \operatorname{Sym}(X)$.

Next, $\rho$ is a homomorphism. For all $x \in X$,
$$\rho(g_1)\big(\rho(g_2)(x)\big) = g_1\ast(g_2\ast x) = (g_1\cdot g_2)\ast x = \rho(g_1\cdot g_2)(x).$$
Since this holds for every $x$, we get $\rho(g_1)\circ\rho(g_2) = \rho(g_1\cdot g_2)$. Also $\rho(e)(x) = e\ast x = x$, so $\rho(e) = \operatorname{id}_X$. Hence $\rho$ is a homomorphism.

**From a homomorphism to an action.** Conversely, given a homomorphism $\rho : G \to \operatorname{Sym}(X)$, define $\ast : G \times X \to X$ by $g\ast x = \rho(g)(x)$. Then
$$\text{(i)}\quad g_1\ast(g_2\ast x) = \rho(g_1)\big(\rho(g_2)(x)\big) = \big(\rho(g_1)\circ\rho(g_2)\big)(x) = \rho(g_1\cdot g_2)(x) = (g_1\cdot g_2)\ast x,$$
$$\text{(ii)}\quad e\ast x = \rho(e)(x) = \operatorname{id}_X(x) = x.$$
So $\ast$ is a group action.

**Mutual inverseness.** Applying the second construction to the $\rho$ built from an action $\ast$ yields the action $g\star x = \rho(g)(x) = g\ast x$, recovering $\ast$. Applying the first construction to the action built from a homomorphism $\rho$ yields $\rho'(g) = (x\mapsto g\ast x) = (x\mapsto\rho(g)(x)) = \rho(g)$, recovering $\rho$. The two constructions are therefore inverse to each other, so actions of $G$ on $X$ are the same data as homomorphisms $G \to \operatorname{Sym}(X)$. $\qquad\blacksquare$

**Consequence.** Write $G_X = \ker\rho$ and $G^X = \operatorname{im}\rho$. Since $\rho$ is a homomorphism, $G_X \trianglelefteq G$ is a normal subgroup and $G^X \leq \operatorname{Sym}(X)$ is a subgroup. The first isomorphism theorem applied to $\rho$ gives
$$G/G_X \cong G^X.$$
In particular, if $G_X = \{e\}$ (the action is faithful), then $G \cong G^X \leq \operatorname{Sym}(X)$. $\qquad\blacksquare$

This is the Lemma and Proposition of §1.3 of the source lecture notes; per the notes, the substance is the explicit translation exhibited in the proof, not the bare equivalence.

</details>

---

# Cross-Field Exercise Suggestions

The aim is to find settings where the action-as-homomorphism dictionary applies but is not advertised, battle-testing recognition of the *sources*.

**Linear algebra: a representation is an action on a vector space.** A linear representation of $G$ is by definition a homomorphism $\rho : G \to \mathrm{GL}(V)$. Since $\mathrm{GL}(V) \leq \operatorname{Sym}(V)$ (invertible linear maps are in particular bijections), this theorem says a representation *is* an action of $G$ on the set $V$ — one that happens to move points linearly. The application is non-obvious because representation theory is usually developed in the language of matrices and modules, never mentioning "action on a set"; yet orbits, stabilisers, and the kernel-as-normal-subgroup all transfer directly. The property $B$ "homomorphism into $\mathrm{GL}(V)$" maps to the precondition "homomorphism into $\operatorname{Sym}(X)$" via the inclusion $\mathrm{GL}(V) \hookrightarrow \operatorname{Sym}(V)$.

**Galois theory: the Galois group acts on the roots.** For a separable polynomial $f$ with splitting field $L/K$, the Galois group $\operatorname{Gal}(L/K)$ permutes the finite set $X$ of roots of $f$, and this gives a homomorphism $\operatorname{Gal}(L/K) \to \operatorname{Sym}(X)$. This theorem certifies it as a genuine action, so one may speak of orbits of roots (the irreducible factors of $f$) and stabilisers. The application is non-obvious because the Galois group is defined as field automorphisms fixing $K$ — objects of field theory, not set theory — and the embedding into a symmetric group is what makes the combinatorics of permutations available to study solvability.

**Topology: deck transformations act on a fibre.** For a covering space $p : \tilde X \to X$, the group of deck transformations acts on each fibre $p^{-1}(x)$, a discrete set, giving a homomorphism into its symmetric group. Recognizing this as an action via the theorem is what lets the orbit-stabiliser correspondence become the dictionary between subgroups of $\pi_1(X)$ and connected covers. The application is non-obvious because deck transformations are continuous self-maps of a space, and the relevant *set* — a single fibre — is hidden inside that space.

**Number theory: modular arithmetic as an action.** The group $(\mathbb{Z}/n\mathbb{Z})^\times$ acts on $\mathbb{Z}/n\mathbb{Z}$ by multiplication, $a \cdot x = ax \bmod n$. This is a homomorphism $(\mathbb{Z}/n\mathbb{Z})^\times \to \operatorname{Sym}(\mathbb{Z}/n\mathbb{Z})$. The orbits are the sets of residues sharing a fixed greatest common divisor with $n$, and the stabiliser of $1$ is trivial. The application is non-obvious because modular multiplication is usually treated as pure arithmetic; reading it as an action makes the partition of residues by gcd an orbit decomposition, with each orbit size dividing $|(\mathbb{Z}/n\mathbb{Z})^\times| = \varphi(n)$.

---

# Bridges

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]]** — this theorem is the *gateway* and the first isomorphism theorem is what one walks through. Once an action is recognized as a homomorphism $\rho$, the first isomorphism theorem delivers $G/G_X \cong G^X$ for free. The two together are the standard pipeline: action $\to$ homomorphism (this theorem) $\to$ quotient identified with image (first isomorphism theorem). Every structural payoff of an action factors through this pair.

- **[[Thm - Cayley's Theorem|Cayley's Theorem]]** — Cayley's theorem is the single most important *instance* of this correspondence: it takes the left-regular action of $G$ on itself, observes via this theorem that it is a homomorphism $G \to \operatorname{Sym}(G)$, and computes that the kernel is trivial. Without the action-homomorphism dictionary, "Cayley's theorem" would have no proof — it is exactly this theorem applied to one specific action.

- **[[Thm - Coset Action and the Normal Core|Coset Action and the Normal Core]]** — the coset action is the instance that exploits the *kernel* half. This theorem guarantees the coset action is a homomorphism $G \to S_n$; its kernel, the normal core, is then a normal subgroup automatically, again because kernels are normal. The coset action's entire force — manufacturing normal subgroups from subgroups — is borrowed from this theorem.

- **[[Thm - Orbit-Stabiliser Theorem|Orbit-Stabiliser Theorem]]** — orbit-stabiliser works on the *action* side of the dictionary, this theorem on the *homomorphism* side; fluency is the ability to switch. A homomorphism $G \to S_n$ produced abstractly becomes, via this theorem, an action with orbits and stabilisers, at which point orbit-stabiliser counting applies. The two theorems are the two faces of a single object.

- **[[Def - Automorphism Group|Automorphism Group]] and conjugation** — conjugation $g\cdot x = gxg^{-1}$ is an action of $G$ on itself, so this theorem gives a homomorphism $G \to \operatorname{Sym}(G)$; but each $\rho(g)$ is in fact a *group* automorphism, so the homomorphism refines to $G \to \operatorname{Aut}(G)$. This is the structured-codomain phenomenon from the Sources section, and it is the construction defining the inner automorphisms and, via its kernel the [[Def - Centraliser and Centre|centre]], the isomorphism $G/Z(G) \cong \operatorname{Inn}(G)$.
