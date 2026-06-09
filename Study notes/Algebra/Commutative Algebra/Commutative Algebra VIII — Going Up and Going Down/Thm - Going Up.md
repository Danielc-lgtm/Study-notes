---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - The Induced Map on Spectra"
  - "Def - Lying Over, Going Up, Going Down"
  - "Def - Prime and Maximal Ideal"
  - "Thm - Lying Over"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A \subseteq B$ be an [[Def - Integral Element and Integral Extension|integral extension]], $\iota : A \hookrightarrow B$ the inclusion, [[Def - The Induced Map on Spectra|ι*]] the contraction $\mathfrak{q} \mapsto \mathfrak{q} \cap A$. Primes of $A$: $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$; primes of $B$: $\mathfrak{q}_1, \mathfrak{q}_2$. For an ideal $\mathfrak{q} \trianglelefteq B$ with contraction $\mathfrak{q} \cap A$, the induced inclusion $A/(\mathfrak{q}\cap A) \hookrightarrow B/\mathfrak{q}$ is again integral. The full registry is on [[Commutative Algebra VIII — Going Up and Going Down]].

---

# Statement

> **Theorem (Going Up).** Let $A \subseteq B$ be an integral extension of rings. Let $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ be primes of $A$ and $\mathfrak{q}_1 \in \operatorname{Spec} B$ a prime lying over $\mathfrak{p}_1$ (that is, $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$). Then there exists $\mathfrak{q}_2 \in \operatorname{Spec} B$ with
> $$\mathfrak{q}_1 \subseteq \mathfrak{q}_2 \qquad \text{and} \qquad \mathfrak{q}_2 \cap A = \mathfrak{p}_2.$$

> **Corollary (chain lifting).** Any ascending chain $\mathfrak{p}_0 \subseteq \mathfrak{p}_1 \subseteq \cdots \subseteq \mathfrak{p}_n$ in $\operatorname{Spec} A$, together with a prime $\mathfrak{q}_0$ lying over $\mathfrak{p}_0$, lifts to an ascending chain $\mathfrak{q}_0 \subseteq \mathfrak{q}_1 \subseteq \cdots \subseteq \mathfrak{q}_n$ in $\operatorname{Spec} B$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$.

The corollary is the working form: it is obtained by applying the theorem to each link of the chain in turn.

---

# Motivation

[[Thm - Lying Over|Lying over]] gave you a prime over a *single* given prime; going up gives you the ability to *follow a chain*. The picture: you stand at a prime $\mathfrak{q}_1$ of $B$ sitting over $\mathfrak{p}_1$, and the base prime grows to $\mathfrak{p}_2 \supseteq \mathfrak{p}_1$ (geometrically, the image point *specialises* — moves to a more special point in its closure). Going up says you can specialise *along with it*: there is a prime $\mathfrak{q}_2 \supseteq \mathfrak{q}_1$ over $\mathfrak{p}_2$. The preimage point follows the base point as the latter specialises. Without this, an integral extension would be onto but blind to the order structure; with it, the map of spectra respects ascending chains, and that is what makes the dimension theory work.

The importance is almost entirely as a *chain-lifting* device. The single headline application is the inequality $\dim A \leq \dim B$: take a chain of primes of $A$ realising the dimension, anchor it over the bottom with lying over, and march it up with going up, getting a chain of $B$ at least as long. Together with the reverse inequality from [[Thm - Incomparability|incomparability]], this is the theorem "[[Thm - Integral Extensions Preserve Dimension|integral extensions preserve dimension]]", which in turn computes $\dim k[X_1,\dots,X_n] = n$ via Noether normalization. So going up is the upward girder of the dimension bridge.

Why expect it to be true? Because the obstruction to enlarging $\mathfrak{q}_1$ to a prime over $\mathfrak{p}_2$ is exactly a *lying-over problem one floor up*. Quotient out by $\mathfrak{q}_1$ and $\mathfrak{p}_1$: the extension $A/\mathfrak{p}_1 \hookrightarrow B/\mathfrak{q}_1$ is again integral (integrality descends to quotients), and the larger prime $\mathfrak{p}_2$ becomes a prime $\mathfrak{p}_2/\mathfrak{p}_1$ of the *new* base. Lying over for the *new* extension produces a prime $\mathfrak{q}_2/\mathfrak{q}_1$ over it, and pulling back through the quotient gives the wanted $\mathfrak{q}_2 \supseteq \mathfrak{q}_1$. So going up is not a new phenomenon — it is lying over, applied after a quotient that converts "enlarge a prime above a fixed prime" into "find a prime above a prime".

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A \subseteq B$ integral, plus a prime $\mathfrak{q}_1$ over the smaller base prime $\mathfrak{p}_1$".

The first disguised source is **a partially constructed chain lift**: you are lifting an ascending chain of $A$ and have already lifted up to $\mathfrak{p}_i$, holding $\mathfrak{q}_i$ over it. The next base prime $\mathfrak{p}_{i+1} \supseteq \mathfrak{p}_i$ together with $\mathfrak{q}_i$ is exactly the input to going up. *Example problem:* lifting a full chain to prove $\dim A \leq \dim B$ — each step is a going-up application.

The second disguised source is **a specialisation of the image point in a finite morphism**. Geometrically, $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ is a specialisation $\mathfrak{p}_1 \rightsquigarrow \mathfrak{p}_2$ in $\operatorname{Spec} A$, and a chosen point $\mathfrak{q}_1$ over $\mathfrak{p}_1$. Going up is the lifting of this specialisation. *Example problem:* showing the image of a closed subvariety under a finite map is closed (the closedness of $\iota^*$) — you must show every specialisation in the image lifts, which is going up.

The third disguised source is **a maximal ideal above which you want a prime sitting over a given prime below it**. With $\mathfrak{p}_2$ maximal and $\mathfrak{q}_1$ over $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$, going up produces $\mathfrak{q}_2 \supseteq \mathfrak{q}_1$ over $\mathfrak{p}_2$, and $\mathfrak{q}_2$ is then maximal (domain criterion). *Example problem:* extending a prime to a maximal ideal of $B$ contracting to a prescribed maximal ideal of $A$.

**Targets (Output Amplification)**

The conclusion is "$\mathfrak{q}_2 \supseteq \mathfrak{q}_1$ over $\mathfrak{p}_2$".

Combine going up with **[[Thm - Lying Over|lying over]]** (the anchor) to lift an *entire* ascending chain. The result $E$ is $\dim A \leq \dim B$, the lower bound in dimension preservation.

Combine going up with **[[Thm - Incomparability|incomparability]]** (the strictness keeper) so that a *strict* base chain lifts to a *strict* chain upstairs. Without incomparability, the lifted inclusions $\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1}$ might be equalities; incomparability rules this out because $\mathfrak{q}_i \cap A = \mathfrak{p}_i \neq \mathfrak{p}_{i+1} = \mathfrak{q}_{i+1}\cap A$ forces $\mathfrak{q}_i \neq \mathfrak{q}_{i+1}$. The result $E$: lengths are preserved exactly, not just bounded.

Combine going up with **the topological criterion** "going up $\iff$ $\iota^*$ closed". The result $E$ is that the induced map of a finite morphism is a *closed map*, the algebraic statement of properness — used to conclude that images of closed sets under finite maps are closed.

---

# Why Is It True

The whole theorem is a single reduction: **going up is lying over, seen after quotienting by $\mathfrak{q}_1$ and $\mathfrak{p}_1$.** Holding $\mathfrak{q}_1$ over $\mathfrak{p}_1$, form the quotient extension. The map $A/\mathfrak{p}_1 \to B/\mathfrak{q}_1$ is well-defined and *injective* precisely because $\mathfrak{p}_1 = \mathfrak{q}_1 \cap A$ — the kernel of $A \to B \to B/\mathfrak{q}_1$ is $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$, so $A/\mathfrak{p}_1 \hookrightarrow B/\mathfrak{q}_1$ is an inclusion. It is integral because integrality passes to quotients. Now $\mathfrak{p}_2 \supseteq \mathfrak{p}_1$ gives a prime $\mathfrak{p}_2/\mathfrak{p}_1$ of the new base $A/\mathfrak{p}_1$, and lying over for the new integral extension produces a prime $\mathfrak{q}_2/\mathfrak{q}_1$ of $B/\mathfrak{q}_1$ over it. Pull back: $\mathfrak{q}_2 \trianglelefteq B$ is a prime containing $\mathfrak{q}_1$, and a diagram chase (the quotient square commutes) shows $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$.

**The mechanism in one line: enlarging $\mathfrak{q}_1$ above a fixed $\mathfrak{p}_1$ is the same as laying a fresh prime in the quotient extension, where the fixed data has been zeroed out and lying over does the work.** The reason the quotient is the right move is that "$\mathfrak{q}_2 \supseteq \mathfrak{q}_1$" becomes "$\mathfrak{q}_2/\mathfrak{q}_1 \in \operatorname{Spec}(B/\mathfrak{q}_1)$" — the containment is automatic once you work in the quotient — so the only remaining content is the *existence* of a prime over $\mathfrak{p}_2/\mathfrak{p}_1$, which is exactly lying over.

---

# What Makes This Hard

The proof is short, so the difficulty is structural: realising that the quotient $A/\mathfrak{p}_1 \hookrightarrow B/\mathfrak{q}_1$ is the right object and that it is *injective* (this needs $\mathfrak{p}_1 = \mathfrak{q}_1 \cap A$ exactly — not just $\subseteq$). The most common error is to try to enlarge $\mathfrak{q}_1$ directly inside $B$ by hand, fighting with which elements to adjoin, instead of quotienting to reduce to lying over. The second pitfall is the diagram chase at the end: one must check that $\mathfrak{q}_2/\mathfrak{q}_1$ contracting to $\mathfrak{p}_2/\mathfrak{p}_1$ in $A/\mathfrak{p}_1$ really pulls back to $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$ in $A$, using commutativity of the quotient square.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Quotient by $\mathfrak{q}_1$ (upstairs) and $\mathfrak{p}_1$ (downstairs) to get an integral extension $A/\mathfrak{p}_1 \hookrightarrow B/\mathfrak{q}_1$; apply [[Thm - Lying Over|lying over]] to the prime $\mathfrak{p}_2/\mathfrak{p}_1$ to get $\mathfrak{q}_2/\mathfrak{q}_1$ over it; pull back to $B$ and check $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$ by the commuting quotient square.

**Subgoal decomposition:**

1. **Form $A/\mathfrak{p}_1 \hookrightarrow B/\mathfrak{q}_1$ and verify it is an injective integral extension.**
   - *Hint:* The map $A \to B \to B/\mathfrak{q}_1$ has kernel $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$; integrality descends to quotients.
   - *Why needed:* It is the extension to which lying over is applied.

2. **Apply lying over in the quotient to $\mathfrak{p}_2/\mathfrak{p}_1$.**
   - *Hint:* $\mathfrak{p}_2/\mathfrak{p}_1$ is a prime of $A/\mathfrak{p}_1$ since $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$; lying over yields $\overline{\mathfrak{q}_2} \in \operatorname{Spec}(B/\mathfrak{q}_1)$ over it.
   - *Why needed:* It produces the lifted prime in the quotient.

3. **Pull $\overline{\mathfrak{q}_2}$ back to $\mathfrak{q}_2 \trianglelefteq B$ and check $\mathfrak{q}_1 \subseteq \mathfrak{q}_2$, $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$.**
   - *Hint:* $\mathfrak{q}_2$ is the preimage of $\overline{\mathfrak{q}_2}$ under $B \to B/\mathfrak{q}_1$, so $\mathfrak{q}_2 \supseteq \mathfrak{q}_1$; the contraction equality is the commuting square $A \to A/\mathfrak{p}_1 \to B/\mathfrak{q}_1$ equals $A \to B \to B/\mathfrak{q}_1$.
   - *Why needed:* It delivers the conclusion in $A$ and $B$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The quotient extension is integral and injective
> **Statement:** If $A \subseteq B$ is integral and $\mathfrak{q}_1 \trianglelefteq B$ is a prime with $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$, then $A/\mathfrak{p}_1 \to B/\mathfrak{q}_1$ is an injective integral ring map.
>
> **Hint:** Injectivity from the kernel computation $\ker(A \to B/\mathfrak{q}_1) = \mathfrak{q}_1 \cap A = \mathfrak{p}_1$; integrality by reducing a monic equation mod $\mathfrak{q}_1$.
>
> **Why needed:** Lying over requires an integral *extension* (injective integral map); this builds it.
>
> > [!note]- Full proof
> > The composite $A \hookrightarrow B \twoheadrightarrow B/\mathfrak{q}_1$ has kernel $\{a \in A : a \in \mathfrak{q}_1\} = \mathfrak{q}_1 \cap A = \mathfrak{p}_1$, so it factors through an *injective* ring map $A/\mathfrak{p}_1 \hookrightarrow B/\mathfrak{q}_1$. For integrality, take $\bar b = b + \mathfrak{q}_1 \in B/\mathfrak{q}_1$. As $b$ is integral over $A$, $b^n + a_1 b^{n-1} + \cdots + a_n = 0$ with $a_i \in A$. Reduce modulo $\mathfrak{q}_1$: $\bar b^n + \bar a_1 \bar b^{n-1} + \cdots + \bar a_n = 0$ in $B/\mathfrak{q}_1$, with $\bar a_i = a_i + \mathfrak{p}_1 \in A/\mathfrak{p}_1$ (since $a_i \in A$ and the map sends $a_i \mapsto a_i + \mathfrak{q}_1$, identified with $\bar a_i$). This is a monic equation over $A/\mathfrak{p}_1$, so $\bar b$ is integral. Hence $A/\mathfrak{p}_1 \hookrightarrow B/\mathfrak{q}_1$ is an integral extension.

> [!note]- Lemma 2: Pulling back a prime through a quotient and computing its contraction
> **Statement:** Let $\overline{\mathfrak{q}_2} \in \operatorname{Spec}(B/\mathfrak{q}_1)$ lie over $\mathfrak{p}_2/\mathfrak{p}_1 \in \operatorname{Spec}(A/\mathfrak{p}_1)$. Its preimage $\mathfrak{q}_2 \trianglelefteq B$ under $B \to B/\mathfrak{q}_1$ is a prime with $\mathfrak{q}_1 \subseteq \mathfrak{q}_2$ and $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$.
>
> **Hint:** Preimages of primes are prime and contain the kernel $\mathfrak{q}_1$; the contraction equality is the commuting square of quotient maps.
>
> **Why needed:** It transports the lifted prime back from the quotient to $B$ and certifies the conclusion.
>
> > [!note]- Full proof
> > Let $\pi_B : B \to B/\mathfrak{q}_1$ and $\pi_A : A \to A/\mathfrak{p}_1$ be the quotient maps. Set $\mathfrak{q}_2 = \pi_B^{-1}(\overline{\mathfrak{q}_2})$. As the preimage of a prime under a ring map, $\mathfrak{q}_2$ is prime, and it contains $\ker\pi_B = \mathfrak{q}_1$, so $\mathfrak{q}_1 \subseteq \mathfrak{q}_2$. For the contraction: the square
> > $$\begin{array}{ccc} A & \hookrightarrow & B \\ \downarrow\pi_A & & \downarrow\pi_B \\ A/\mathfrak{p}_1 & \hookrightarrow & B/\mathfrak{q}_1 \end{array}$$
> > commutes. Now $a \in \mathfrak{q}_2 \cap A \iff \pi_B(a) \in \overline{\mathfrak{q}_2} \iff \pi_A(a) \in \overline{\mathfrak{q}_2} \cap (A/\mathfrak{p}_1)$ (using commutativity, $\pi_B(a) = \pi_A(a)$ under the bottom inclusion) $\iff \pi_A(a) \in \mathfrak{p}_2/\mathfrak{p}_1$ (the hypothesis that $\overline{\mathfrak{q}_2}$ lies over $\mathfrak{p}_2/\mathfrak{p}_1$) $\iff a \in \mathfrak{p}_2$. Hence $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A \subseteq B$ be integral, $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ primes of $A$, and $\mathfrak{q}_1 \in \operatorname{Spec} B$ with $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$.
>
> **Step 1 — quotient.** By Lemma 1, $A/\mathfrak{p}_1 \hookrightarrow B/\mathfrak{q}_1$ is an integral extension. Since $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$, the set $\mathfrak{p}_2/\mathfrak{p}_1$ is a prime ideal of $A/\mathfrak{p}_1$.
>
> **Step 2 — lying over in the quotient.** Apply [[Thm - Lying Over|lying over]] to the integral extension $A/\mathfrak{p}_1 \subseteq B/\mathfrak{q}_1$ and the prime $\mathfrak{p}_2/\mathfrak{p}_1$: there is $\overline{\mathfrak{q}_2} \in \operatorname{Spec}(B/\mathfrak{q}_1)$ with $\overline{\mathfrak{q}_2} \cap (A/\mathfrak{p}_1) = \mathfrak{p}_2/\mathfrak{p}_1$.
>
> **Step 3 — pull back.** By Lemma 2, the preimage $\mathfrak{q}_2 = \pi_B^{-1}(\overline{\mathfrak{q}_2}) \trianglelefteq B$ is a prime with $\mathfrak{q}_1 \subseteq \mathfrak{q}_2$ and $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$. This is the required prime. $\blacksquare$
>
> ---
> **Corollary (chain lifting).** Given $\mathfrak{p}_0 \subseteq \cdots \subseteq \mathfrak{p}_n$ in $\operatorname{Spec} A$ and $\mathfrak{q}_0$ over $\mathfrak{p}_0$, apply the theorem repeatedly: having built $\mathfrak{q}_i \supseteq \cdots \supseteq \mathfrak{q}_0$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$, apply going up to $\mathfrak{p}_i \subseteq \mathfrak{p}_{i+1}$ and $\mathfrak{q}_i$ to obtain $\mathfrak{q}_{i+1} \supseteq \mathfrak{q}_i$ over $\mathfrak{p}_{i+1}$. After $n$ steps one has $\mathfrak{q}_0 \subseteq \cdots \subseteq \mathfrak{q}_n$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Lifting a flag of subvarieties under a finite map.** A chain of irreducible closed subvarieties $V_0 \supseteq V_1 \supseteq \cdots \supseteq V_n$ of $\operatorname{Spec} A$ corresponds to an ascending chain of primes; under a finite morphism $\operatorname{Spec} B \to \operatorname{Spec} A$, going up lifts it to a flag in $\operatorname{Spec} B$ over it, starting from any chosen point of $B$ over $V_0$'s generic point. The application is non-obvious because it says a finite map cannot "lose depth" — every nested family of subvarieties downstairs is realised upstairs.

**Splitting of primes in a tower of number fields.** For a tower of rings of integers $\mathbb{Z} \subseteq \mathcal{O}_K \subseteq \mathcal{O}_L$, each step integral, going up lifts the chain $(0) \subseteq \mathfrak{p}$ along $\mathcal{O}_K \subseteq \mathcal{O}_L$: starting from the zero ideal over $(0)$, the generic-to-special inclusion $(0) \subseteq \mathfrak{p}$ in $\mathcal{O}_K$ is realised by some $\mathfrak{P}$ of $\mathcal{O}_L$ over $\mathfrak{p}$, tracking how a prime of $\mathcal{O}_K$ extends upward to $\mathcal{O}_L$. The application is non-obvious because it organises the *transitivity* of prime splitting in towers as a single chain-lifting statement.

**Closedness of the image of a finite map (properness).** The criterion "going up $\iff$ $\iota^*$ closed" lets one prove that the image of a closed subvariety under a finite morphism is closed: every specialisation of an image point lifts (going up), so the image contains all its specialisations, hence is closed. The application is non-obvious because closedness of images is the algebraic-geometric form of *properness*, and it is exactly the property that generic projections lack (the hyperbola's image misses a point).

---

# Bridges

- **[[Thm - Lying Over|Lying Over]]** — going up is built *from* lying over by the quotient reduction, and *implies* lying over (localize to find a prime below $\mathfrak{p}$, then go up). The pair is the upward chain-lifting toolkit; neither alone bounds dimension, but together they give $\dim A \leq \dim B$.

- **[[Thm - Incomparability|Incomparability]]** — incomparability is the *strictness partner* of going up. Going up lifts a chain but only with $\subseteq$; incomparability upgrades each $\subseteq$ to $\subsetneq$ when the base inclusion is strict, because distinct contractions force distinct primes. Together they preserve chain *length*, not merely existence.

- **[[Thm - Integral Extensions Preserve Dimension|Integral Extensions Preserve Dimension]]** — going up supplies the lower bound $\dim A \leq \dim B$ in this theorem; incomparability supplies the upper bound. The result is the chapter's headline, and going up is one of its two girders.

- **[[Thm - Maximal and Prime Ideals via Quotients|Maximal and Prime Ideals via Quotients]]** — the proof leans on passing to quotients and recognising $\mathfrak{p}_2/\mathfrak{p}_1$ as a prime of $A/\mathfrak{p}_1$; this is the [[Thm - Ideal Correspondence|ideal correspondence]] used to convert "enlarge a prime" into "find a prime in the quotient". The quotient dictionary is the structural engine behind going up.

---

# Unlocked by This

> [!tip] Finite morphisms are closed *(from Algebraic Geometry)*
> Going up is the algebraic statement that the induced map of a **finite morphism of varieties** is a *closed map* — it carries closed subvarieties to closed subvarieties. This is the local model of *properness*: finite morphisms are proper, and the closedness of their images is exactly what going up provides. The contrast is the non-integral projection $k[T_1] \to k[T_1, T_2]/(T_1 T_2 - 1)$, whose image $\mathbb{A}^1 \setminus \{0\}$ is not closed — its algebra map is not integral, so going up fails, and the map of spectra is not closed.
