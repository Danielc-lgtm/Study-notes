---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Globular Operad"
  - "Def - The Free Strict ω-Category Monad"
  - "Def - Pullback and Pushout"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $T$ be the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] on **globular sets**, and let $\mathcal{E} = [\mathbb{G}^{op}, \mathbf{Set}]/T1$ be the category of **collections** (globular sets over $T1$).

(a) Construct the **substitution product** $\otimes$ on $\mathcal{E}$: given collections $P \xrightarrow{d} T1$ and $Q \xrightarrow{e} T1$, describe $P \otimes Q$ and its structure map to $T1$, and identify the unit object.

(b) Show that the associativity of $\otimes$ uses the cartesianness of $T$ — specifically, that the relevant identifications are pullbacks preserved by $T$.

(c) Exhibit a non-cartesian monad (the free **commutative-monoid** monad on $\mathbf{Set}$) for which the analogous substitution product *fails* to be associative, and pinpoint which pullback breaks.

**Recall:**

A **collection** is an object of the slice $\mathcal{E} = [\mathbb{G}^{op}, \mathbf{Set}]/T1$. A [[Def - Globular Operad|globular operad]] is a [[Def - Monoid in a Monoidal Category|monoid]] in $(\mathcal{E}, \otimes)$. The monad $T$ is **cartesian**: it preserves [[Def - Pullback and Pushout|pullbacks]] and the naturality squares of $\eta, \mu$ are pullbacks. The free-monoid monad $(-)^{\ast}$ on $\mathbf{Set}$ is cartesian; the free **commutative-monoid** monad $M$ (sending a set $A$ to the set of finite *multisets* over $A$) is **not** cartesian — forgetting the order of a multiset destroys the information a pullback needs.

---

# Convergent Strategy

**Problem class:** This is the hardest *cartesianness* problem of the topic page's problem-solving strategy: not merely verifying cartesianness, but exhibiting *what it buys* (an associative substitution product) and *what its absence costs* (associativity failure). The route is to build $\otimes$ via pullbacks, then track exactly where $T$ must preserve a pullback for associativity, then break that step with a non-cartesian monad.

**Assumption pattern:** The crucial assumption is that the substitution product is built by *pullback* — $P \otimes Q$ is, fibrewise, "an operation of $P$ of shape $\pi$ together with a $Q$-operation filling each cell of $\pi$", which is a pullback of $Q$-data along the cells of $\pi$. The presence of "fill each cell of an operation by another operation" is the signal that $T$ (which knows the cells of a pasting diagram) must be applied, and that its pullback-preservation is what makes the construction associative. Recognizing "substitution $=$ pullback through $T$" is the unlock.

**Theorem routing:** Route the construction of $\otimes$ through the formula $P \otimes Q = P \times_{T1} TQ$ (the pullback of $d : P \to T1$ against $T1 \xleftarrow{} TQ$ via $Te : TQ \to T(T1) \xrightarrow{\mu} T1$). Route associativity through "both bracketings $(P\otimes Q)\otimes R$ and $P\otimes(Q\otimes R)$ are computed by iterated pullbacks, equal because $T$ preserves the intermediate pullback and $\mu$ is cartesian". Route the counterexample through the explicit multiset monad, finding the pullback that $M$ fails to preserve.

**Key decision point:** The non-obvious choice is to define $\otimes$ using $T$ applied to the *second* factor, $P \otimes Q = P \times_{T1} TQ$, rather than some naive fibrewise product. The tempting alternative — defining $P \otimes Q$ fibrewise as $\coprod_\pi P(\pi) \times (\text{products of } Q \text{ over cells of } \pi)$ — is correct but obscures associativity; the $T$-based formula makes associativity a consequence of cartesianness in one clean step, and makes the counterexample transparent.

---

# Legal Operations Used

1. **Operation 2 from the topic page (use cartesianness to form the substitution product).** This exercise is the deep justification of that operation: it constructs $\otimes$ and shows associativity *requires* cartesianness.

2. **Operation 5 from the topic page (stratified/structural reasoning), in reverse.** The counterexample shows what goes wrong structurally when the monad fails cartesianness, illuminating why the well-behaved construction needs it.

---

# Hints

> [!note]- Hint 1
> The substitution product should encode "an operation of $P$, with each of its input cells filled by an operation of $Q$". Filling the cells of a $P$-operation of shape $\pi$ by $Q$-operations is the data of an element of $TQ$ lying over $\pi$. So pair a $P$-operation with a compatible $TQ$-element.

> [!note]- Hint 2
> Formalize: $P \otimes Q = P \times_{T1} TQ$, the pullback of $d : P \to T1$ against the map $TQ \xrightarrow{Te} T(T1) \xrightarrow{\mu} T1$. The structure map $P \otimes Q \to T1$ uses $\mu$ to record the substituted shape. The unit is $T1 \xrightarrow{\eta} \dots$ — the collection $\eta : 1 \to T1$? Check: the unit must be the collection whose operations are the "do-nothing" ones, i.e. $\eta_1 : 1 \to T1$? Re-examine using the monad unit.

> [!note]- Hint 3
> For associativity, expand $(P \otimes Q) \otimes R$ and $P \otimes (Q \otimes R)$ as iterated pullbacks. You will need to commute $T$ past a pullback (to compute $T(Q \otimes R)$) and to use that $\mu$'s naturality square is a pullback. Both are *exactly* the cartesianness hypotheses.

> [!note]- Hint 4
> For the counterexample, take $M =$ free commutative monoid (multisets) on $\mathbf{Set}$. Find sets and maps where $M$ fails to preserve a pullback: a multiset over a pullback $A \times_C B$ is *not* the same as a pair of multisets over $A$ and $B$ with equal image multiset over $C$, because the pairing of elements is lost when order is forgotten. That lost pairing is the broken pullback, and it breaks associativity of substitution.

---

# Solution

The solution constructs $\otimes$ as a pullback through $T$ (Step 1), proves associativity using that $T$ preserves pullbacks and $\mu$ is cartesian (Step 2), and breaks associativity with the multiset monad by exhibiting the failed pullback (Step 3). The pivot throughout is "substitution is a pullback, and only a cartesian monad preserves the pullbacks that make iterated substitution associative".

**Step 1: the substitution product.**

> [!note]- Derivation
> For collections $P \xrightarrow{d} T1$ and $Q \xrightarrow{e} T1$, define
> $$
> P \otimes Q \;=\; P \times_{T1} TQ,
> $$
> the [[Def - Pullback and Pushout|pullback]] of $d : P \to T1$ against the composite $\widetilde{e} : TQ \xrightarrow{\;Te\;} T(T1) \xrightarrow{\;\mu_1\;} T1$. An element is a pair $(\theta, \xi)$ with $\theta \in P(\pi)$ an operation of some shape $\pi$ and $\xi \in TQ$ a "$Q$-labelled pasting diagram" whose underlying shape (under $\widetilde e$) is $\pi$ — that is, a $Q$-operation filling each cell of $\pi$. The structure map $P \otimes Q \to T1$ sends $(\theta, \xi)$ to the *substituted* shape, obtained by pasting the shapes of the filling $Q$-operations into $\pi$; concretely it is $TQ \xrightarrow{Te} T(T1)\xrightarrow{\mu_1} T1$ on the second coordinate. The **unit** $I$ is the collection $1 \xrightarrow{\eta_1} T1$ (the "trivial operations", one per shape, that fill a cell by itself and do nothing) — substituting $I$ on either side returns the original collection up to canonical iso, by the monad unit laws. This is the globular analogue of the substitution product on symmetric sequences whose monoids are classical operads.

**Step 2: associativity needs cartesianness.**

> [!note]- Derivation
> Compute both bracketings as iterated pullbacks. By definition,
> $$
> (P \otimes Q) \otimes R = (P \times_{T1} TQ) \times_{T1} TR, \qquad P \otimes (Q \otimes R) = P \times_{T1} T(Q \times_{T1} TR).
> $$
> To identify these we must rewrite $T(Q \times_{T1} TR)$. **Here cartesianness enters twice.** First, $T$ **preserves pullbacks**, so
> $$
> T(Q \times_{T1} TR) \;\cong\; TQ \times_{T(T1)} T(TR).
> $$
> Second, the **multiplication $\mu$ is cartesian**: its naturality square for $e : Q \to T1$ (and for $TR$) is a pullback, which lets us reduce $T(T1)$ and $T(TR)$ back down along $\mu$ to $T1$ and $TR$ compatibly. Composing these identifications, both bracketings become the *same* triple pullback
> $$
> P \times_{T1} TQ \times_{T(T1)} T(TR) \;\xrightarrow{\ \mu\ }\; (\text{coherently}) \; P \times_{T1} TQ \times_{T1} TR,
> $$
> "an operation of $P$, with each cell filled by an operation of $Q$, with each cell of those filled by an operation of $R$" — and the associativity isomorphism is the canonical comparison of the two pullback orders, which exists and is coherent *because every square involved is a pullback*. The unit laws follow similarly from $\eta$ being cartesian. So $(\mathcal{E}, \otimes, I)$ is a monoidal category, and the cartesianness of $T$ is used precisely at "$T$ preserves the pullback defining $Q \otimes R$" and "$\mu$ is cartesian".

**Step 3: the multiset monad breaks associativity.**

> [!note]- Derivation
> Replace $T$ by the free commutative-monoid monad $M$ on $\mathbf{Set}$ (multisets), and form the analogous substitution product on $\mathbf{Set}/M1 = \mathbf{Set}/\mathbb{N}$ (since $M1 \cong \mathbb{N}$, a multiset over a point is its cardinality). The associativity argument needs $M(Q \times_{M1} MR) \cong MQ \times_{M(M1)} M(MR)$ — i.e. $M$ must preserve the pullback. It does not. Concretely, take the cospan $A \to C \leftarrow B$ and consider a multiset of *pairs* over the pullback $A \times_C B$ versus a *pair of multisets* over $A$ and $B$ with equal image-multiset over $C$. A multiset of pairs records which $a$ is matched with which $b$; a pair of multisets with equal $C$-image forgets the matching. When $C$ has an element with two preimages on each side, the two descriptions differ:
> $$
> M(A \times_C B) \;\not\cong\; MA \times_{MC} MB,
> $$
> because $MA \times_{MC} MB$ admits "rematchings" that no single multiset of pairs produces. The smallest witness: $A = B = \{1, 2\}$, $C = \{c\}$ with both elements mapping to $c$; the multiset $\{(1,1),(2,2)\}$ and $\{(1,2),(2,1)\}$ over $A\times_C B = \{1,2\}\times\{1,2\}$ have the *same* projections $\{1,2\}$ on each side and the same image $\{c, c\}$ over $C$, so they are identified in $MA \times_{MC} MB$ but are distinct multisets of pairs. This is the broken pullback. Consequently iterated substitution depends on the bracketing — substituting $R$ into $Q$ first, then into $P$, can rematch elements differently than the other order — and $\otimes$ fails to be associative. So no "commutative-monoid operad" theory arises by this route, confirming that **cartesianness is the exact hypothesis that makes the substitution product associative**.

> [!note]- Complete formal solution
> *(a)* Define $P \otimes Q = P \times_{T1} TQ$, the pullback of $d:P\to T1$ against $\widetilde e : TQ\xrightarrow{Te} T(T1)\xrightarrow{\mu_1} T1$; an element is an operation $\theta$ of $P$ with a $Q$-operation filling each cell, and the structure map records the substituted shape via $\mu$. The unit is $I = (1\xrightarrow{\eta_1} T1)$.
>
> *(b)* For associativity, $(P\otimes Q)\otimes R = (P\times_{T1} TQ)\times_{T1} TR$ and $P\otimes(Q\otimes R) = P\times_{T1} T(Q\times_{T1} TR)$. Since $T$ preserves pullbacks, $T(Q\times_{T1} TR)\cong TQ\times_{T(T1)} T(TR)$; since $\mu$ is cartesian, the $T(T1)$- and $T(TR)$-terms reduce along $\mu$ to $T1$ and $TR$ compatibly. Both bracketings thus become the same triple pullback, with the associator the canonical comparison of pullback orders. Unitality uses $\eta$ cartesian. So $(\mathcal E,\otimes,I)$ is monoidal, and globular operads are its monoids.
>
> *(c)* For the multiset monad $M$, associativity needs $M(Q\times_{M1} MR)\cong MQ\times_{M(M1)} M(MR)$, i.e. $M$ to preserve pullbacks. It fails: with $A=B=\{1,2\}$, $C=\{c\}$ (both elements $\mapsto c$), the multisets $\{(1,1),(2,2)\}$ and $\{(1,2),(2,1)\}$ over $A\times_C B$ have identical projections and $C$-image, so are identified in $MA\times_{MC} MB$ but are distinct elements of $M(A\times_C B)$. This broken pullback makes iterated substitution bracketing-dependent, so $\otimes$ is non-associative. Hence cartesianness is exactly what associativity of the substitution product requires. $\blacksquare$

---

# Key Takeaways

**The substitution product is a pullback, and associativity is "the monad preserves it".** The structural core of operad theory is that "substitute operations into the cells of an operation" is a *pullback* — pairing a $P$-operation with compatible $Q$-fillers — and that iterating the substitution associatively requires the monad to preserve the intermediate pullback. This is why cartesianness is not a technical convenience but the precise content of "operads exist over $T$": the entire monoidal structure $(\mathcal{E}, \otimes)$, hence the very notion of globular operad as a monoid, rests on $T$ preserving these pullbacks. The trigger for recognizing the role of cartesianness: anytime you see "compose operations by substitution" you are forming a pullback, and you should ask whether the ambient monad preserves it — if not, composition is not associative and there is no operad theory.

**Forgetting order breaks pullbacks, and broken pullbacks break associativity.** The multiset counterexample isolates the mechanism of failure with surgical precision: a multiset of pairs remembers the matching of elements, a pair of multisets forgets it, and the two differ exactly when there is genuine rematching freedom. This lost matching *is* the failed pullback $M(A\times_C B)\not\cong MA\times_{MC} MB$, and it propagates to non-associativity of substitution because the bracketing order decides when the matching is fixed. The transferable diagnostic: a monad whose construction *forgets order or identifies via a quotient* (multisets, symmetric powers, free commutative algebras) will fail cartesianness and admit no clean operad theory; a monad built from *ordered, freely-generated* data (lists, paths, trees, pasting diagrams) will succeed. This is the deep reason globular operads are *plain* (non-symmetric) — the symmetric/commutative analogue would forget order and break the pullbacks.

**"Monoid in a monoidal category" is the right altitude for operads.** Casting a globular operad as a monoid in $(\mathcal{E}, \otimes)$ is what makes the high-level results tractable: completeness of the operad category, existence of free and initial operads, the very construction of the Batanin–Leinster operad $L$ all run at the monoid-in-a-monoidal-category level, never touching the messy explicit substitution. The lesson is to identify, for any operad-like structure, the substitution monoidal product whose monoids it is — classical operads are monoids in symmetric sequences, globular operads are monoids in collections-over-$T1$ — and then import the general theory of monoids wholesale. This is exactly the viewpoint [[Thm - The Initial Contractible Globular Operad Exists]] exploits to prove $L$ exists, and it is why [[Def - Globular Operad]] states the definition in the monoid form. See [[Ex - The free strict omega-category monad is cartesian on a slice]] for the proof that $T$ supplies the cartesianness this product needs.
