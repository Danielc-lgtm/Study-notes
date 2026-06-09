---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Quotient Module"
  - "Def - Noetherian and Artinian Module"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Direct Sum of Modules"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; modules are unital. Let $R$ be a ring. We use a [[Def - Exact Sequence and Short Exact Sequence|short exact sequence]] $0 \to N \xrightarrow{i} M \xrightarrow{p} L \to 0$, in which $i$ is injective, $p$ is surjective, and $\operatorname{im} i = \ker p$, so $N \cong i(N)$ is a submodule and $L \cong M/i(N)$. "Noetherian" abbreviates the [[Def - Noetherian and Artinian Module|ascending chain condition on submodules]], "Artinian" the descending chain condition. For a chain of submodules we use $\subseteq$; $\bigoplus_i M_i$ is the [[Def - Direct Sum of Modules|direct sum]]. The full registry is on [[Commutative Algebra I — Chain Conditions]].

---

# Statement

> **Theorem (chain conditions are two-out-of-three).** Let $0 \to N \xrightarrow{i} M \xrightarrow{p} L \to 0$ be a short exact sequence of $R$-modules. Then
> $$M \text{ is Noetherian} \iff \text{both } N \text{ and } L \text{ are Noetherian},$$
> and likewise with "Noetherian" replaced throughout by "Artinian".

> **Corollary (finite direct sums).** If $M_1, \dots, M_n$ are Noetherian (resp. Artinian) $R$-modules, then $M_1 \oplus \cdots \oplus M_n$ is Noetherian (resp. Artinian).

The corollary follows by applying the theorem to the split short exact sequence $0 \to M_1 \to M_1 \oplus M_2 \to M_2 \to 0$ and inducting on $n$. Specialised to the case where $N$ is a submodule and $L = M/N$, the theorem says a module is Noetherian/Artinian iff a given submodule and the corresponding quotient both are.

---

# Motivation

This is the structural workhorse of the whole chapter — almost every later "$X$ is Noetherian" theorem is this lemma applied once. The reason it is so powerful is that it makes the chain condition behave like a *conservation law* along the basic exact sequence that builds $M$ out of a submodule $N$ and a quotient $L$. Conservation laws are exactly what permit induction: to prove a chain condition for a complicated module, exhibit it as the middle of a short exact sequence whose ends are simpler and already known to satisfy the condition.

Before this lemma, the chain condition is a property of a single module in isolation, and there is no obvious way to verify it for a module assembled from pieces. The lemma supplies the assembly rule. The instant you have a submodule $N \subseteq M$, the sequence $0 \to N \to M \to M/N \to 0$ is available, and the lemma says the chain condition on $M$ is *equivalent* to the chain condition on the two smaller modules $N$ and $M/N$. The forward direction ("$M$ Noetherian $\Rightarrow$ $N$ and $L$ Noetherian") is the statement that the chain condition is inherited by submodules and quotients; the reverse ("$N, L$ Noetherian $\Rightarrow$ $M$ Noetherian") is the genuinely useful direction, the one that lets you *build* Noetherian modules.

The corollary is the first dividend, and it is the bridge to the next theorem. Finite direct sums of Noetherian modules are Noetherian, so in particular $R^{\oplus \ell}$ is Noetherian whenever $R$ is a Noetherian module over itself; and since every finitely generated module is a quotient of some $R^{\oplus \ell}$, [[Thm - Finitely Generated Modules over a Noetherian Ring are Noetherian|every finitely generated module over a Noetherian ring is Noetherian]]. That entire chain of reasoning is this one lemma, applied to direct sums and then to quotients.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a short exact sequence with two of the three terms satisfying the chain condition" (for the useful direction) or "$M$ satisfying it" (for the inheritance direction). Several setups deliver this.

The first disguised source is **a submodule and its quotient**. The property $B$ is "$N \subseteq M$ is a submodule". The bridge is automatic: $0 \to N \to M \to M/N \to 0$ is exact, so the theorem applies with $L = M/N$. The non-obvious value is that *any* submodule, however it arises (as a kernel, an image, an ideal, a torsion submodule), instantly produces an exact sequence on which two-out-of-three bites. *Example problem:* to show $M$ is Noetherian it suffices to find a Noetherian submodule with Noetherian quotient.

The second disguised source is **a finite direct sum**. The property $B$ is "$M = M_1 \oplus \cdots \oplus M_n$". The bridge is the split sequence $0 \to M_1 \to M \to M_2 \oplus \cdots \oplus M_n \to 0$ and induction. The non-obviousness is that a direct sum, which looks like a product, is handled by *peeling one summand at a time* through exact sequences. *Example problem:* $R^{\oplus \ell}$ is Noetherian because each copy of $R$ is.

The third disguised source is **a surjection or injection between modules**. The property $B$ is "there is a surjection $M \twoheadrightarrow L$" (then $L$ is Noetherian if $M$ is, via $0 \to \ker \to M \to L \to 0$) or "an injection $N \hookrightarrow M$" (then $N$ is Noetherian if $M$ is). The non-obviousness is that inheritance flows along *any* mono or epi, not just inclusions of literal submodules. *Example problem:* a quotient of a Noetherian module is Noetherian — apply inheritance to the quotient map.

**Targets (Output Amplification)**

The conclusion is "$M$ (resp. $N$, $L$) satisfies the chain condition".

Combine the conclusion with **a presentation $M \cong R^{\oplus \ell}/K$**. Knowing $R^{\oplus \ell}$ is Noetherian (corollary), the quotient $M$ is Noetherian by the inheritance direction. The further result $E$ is [[Thm - Finitely Generated Modules over a Noetherian Ring are Noetherian|finitely generated modules over a Noetherian ring are Noetherian]] — the corollary plus inheritance, no extra work. The combination is non-obvious because it routes "finitely generated" to "Noetherian" purely through exact sequences.

Combine the conclusion with **induction on a filtration**. If $M$ has a filtration $0 = M_0 \subseteq M_1 \subseteq \cdots \subseteq M_n = M$ with each quotient $M_i/M_{i-1}$ Noetherian, then $M$ is Noetherian by repeatedly applying the reverse direction up the filtration. The further result $E$ is that **a module with a composition series (simple quotients) is Noetherian and Artinian**, hence of finite length. The combination is non-obvious because it builds a global chain condition from local (graded-piece) ones.

Combine the conclusion with **the Artinian version simultaneously**. Since the theorem holds verbatim for Artinian, the same exact sequence controls both conditions, so a module is *finite length* (both conditions) iff sub and quotient are. The further result $E$ is **additivity of length** $\ell(M) = \ell(N) + \ell(L)$, since finite length is preserved and the composition factors of $M$ are those of $N$ together with those of $L$. The combination is the launching point for [[Thm - Length is Additive and Finite iff Noetherian and Artinian|length theory]].

---

# Why Is It True

The proof is a clean three-part bookkeeping, and the intuition is that a chain in $M$ *splits into a chain in $N$ and a chain in $L$*, with the chain in $M$ stabilising exactly when both pieces do.

**The bolded mechanism: a submodule of $M$ is pinned down by its intersection with $N$ and its image in $L$; a chain in $M$ therefore drags along a chain in $N$ and a chain in $L$, and stabilises precisely when both of those stabilise.**

Here is the picture. Identify $N$ with the submodule $i(N) \subseteq M$ and $L$ with $M/N$. Given any submodule $P \subseteq M$, it has a "lower part" $P \cap N$ (a submodule of $N$) and an "upper part" $p(P) = (P + N)/N$ (a submodule of $L$). The key fact is that these two pieces *almost* determine $P$: if $P \subseteq Q$ are submodules with $P \cap N = Q \cap N$ and $p(P) = p(Q)$, then $P = Q$. (Proof: take $q \in Q$; since $p(q) \in p(Q) = p(P)$, there is $x \in P$ with $p(q) = p(x)$, so $q - x \in N$; and $q - x \in Q$, so $q - x \in Q \cap N = P \cap N \subseteq P$; hence $q = x + (q-x) \in P$.) This is the entire engine.

Now run the inheritance direction. If $M$ is Noetherian, then $N \subseteq M$ inherits ACC because any ascending chain in $N$ is also an ascending chain in $M$, which stabilises. And $L = M/N$ inherits ACC because submodules of $M/N$ correspond (by the [[Thm - Isomorphism Theorems for Modules|correspondence theorem]]) to submodules of $M$ containing $N$, so an ascending chain in $L$ lifts to an ascending chain in $M$, which stabilises, dragging the original down. So $M$ Noetherian forces $N$ and $L$ Noetherian — *submodules and quotients inherit the chain condition*.

Run the reverse, harder, direction. Suppose $N$ and $L$ are Noetherian and let $P_1 \subseteq P_2 \subseteq \cdots$ be an ascending chain in $M$. Form the two derived chains: $P_1 \cap N \subseteq P_2 \cap N \subseteq \cdots$ in $N$, and $p(P_1) \subseteq p(P_2) \subseteq \cdots$ in $L$. Both stabilise — the first because $N$ is Noetherian, the second because $L$ is. Pick an index $j$ beyond which *both* are constant. For $k \geq j$, the submodules $P_j \subseteq P_k$ have equal intersections with $N$ and equal images in $L$, so by the key fact $P_j = P_k$. Hence the chain in $M$ stabilises at $j$, and $M$ is Noetherian. The Artinian case is identical with every $\subseteq$ reversed. The whole proof is "a chain upstairs stabilises iff its shadow in $N$ and its shadow in $L$ both stabilise" — two-out-of-three is literally that the middle is controlled by the two ends.

---

# What Makes This Hard

The non-obvious step is the **key fact** that a submodule $P \subseteq M$ is determined, *among submodules containing it*, by the pair $(P \cap N,\ p(P))$ — the little four-line argument that "equal intersection with $N$ and equal image in $L$ forces equality". People get stuck on the reverse direction by trying to stabilise the chain in $M$ directly, instead of stabilising the two *shadow* chains in $N$ and $L$ and then using the key fact to pull the conclusion back up. The most common error is to prove only $P_j \cap N = P_k \cap N$ *or* only $p(P_j) = p(P_k)$ and think that suffices — you need *both* to conclude $P_j = P_k$, and the example $0 \to N \to N \oplus L \to L \to 0$ shows neither alone is enough.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Identify $N$ with a submodule of $M$ and $L$ with $M/N$. The inheritance direction is immediate (subchains and quotient-chains of a stabilising chain stabilise). For the reverse direction, attach to any chain in $M$ its two shadow chains — intersections with $N$ and images in $L$ — stabilise both, and use the key squeezing lemma to conclude the original chain stabilises.

**Subgoal decomposition:**

1. **Inheritance: $M$ Noetherian $\Rightarrow$ $N$ and $L$ Noetherian.**
   - *Hint:* A chain in $N$ is a chain in $M$; a chain in $L = M/N$ lifts to a chain in $M$ through the correspondence theorem. Both stabilise because $M$ does.
   - *Why needed:* It is half the equivalence and gives "submodules and quotients of Noetherian modules are Noetherian".

2. **The squeezing lemma (key fact).** If $P \subseteq Q$ in $M$ with $P \cap N = Q \cap N$ and $p(P) = p(Q)$, then $P = Q$.
   - *Hint:* For $q \in Q$, find $x \in P$ with $p(q) = p(x)$; then $q - x \in N \cap Q = N \cap P \subseteq P$.
   - *Why needed:* It is the engine that pulls stabilisation of the two shadow chains back to the original.

3. **Reverse: $N, L$ Noetherian $\Rightarrow$ $M$ Noetherian.**
   - *Hint:* Given a chain $\{P_k\}$ in $M$, stabilise both $\{P_k \cap N\}$ (in $N$) and $\{p(P_k)\}$ (in $L$) at a common index $j$; apply the squeezing lemma for $k \geq j$.
   - *Why needed:* It is the useful direction — it lets one build Noetherian modules from Noetherian pieces.

4. **Artinian case and corollary.**
   - *Hint:* Reverse all inclusions for Artinian; for the corollary apply the reverse direction to $0 \to M_1 \to M_1 \oplus M_2 \to M_2 \to 0$ and induct.
   - *Why needed:* It delivers "finite direct sums of Noetherian/Artinian modules are Noetherian/Artinian", the input to the next theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Submodules and quotients inherit the chain condition
> **Statement:** If $M$ is Noetherian (resp. Artinian), then every submodule $N \subseteq M$ and every quotient $M/N$ is Noetherian (resp. Artinian).
>
> **Hint:** Chains in $N$ are chains in $M$; chains in $M/N$ correspond to chains in $M$ above $N$ via the correspondence theorem.
>
> **Why needed:** It is the inheritance ("forward") direction of the theorem.
>
> > [!note]- Full proof
> > *Submodule.* An ascending chain $N_1 \subseteq N_2 \subseteq \cdots$ of submodules of $N$ is also an ascending chain of submodules of $M$, hence stabilises by ACC in $M$. So $N$ is Noetherian. (Descending chains likewise for Artinian.)
> >
> > *Quotient.* By the [[Thm - Isomorphism Theorems for Modules|correspondence theorem]], submodules of $M/N$ are in inclusion-preserving bijection with submodules of $M$ containing $N$. An ascending chain $\overline{P_1} \subseteq \overline{P_2} \subseteq \cdots$ in $M/N$ corresponds to an ascending chain $P_1 \subseteq P_2 \subseteq \cdots$ in $M$ (each $P_i \supseteq N$), which stabilises in $M$; the correspondence then stabilises the chain in $M/N$. So $M/N$ is Noetherian. (Descending likewise.)

> [!note]- Lemma 2: The squeezing lemma
> **Statement:** Let $P \subseteq Q$ be submodules of $M$, where $N \subseteq M$ and $p : M \to M/N$ is the quotient map. If $P \cap N = Q \cap N$ and $p(P) = p(Q)$, then $P = Q$.
>
> **Hint:** Given $q \in Q$, subtract an element of $P$ with the same image in $M/N$; the difference lands in $N \cap Q = N \cap P$.
>
> **Why needed:** It is the device that recovers a chain in $M$ from its two shadow chains, powering the reverse direction.
>
> > [!note]- Full proof
> > Clearly $P \subseteq Q$. Conversely let $q \in Q$. Since $p(q) \in p(Q) = p(P)$, there exists $x \in P$ with $p(x) = p(q)$, i.e. $p(q - x) = 0$, so $q - x \in \ker p = N$. Also $q \in Q$ and $x \in P \subseteq Q$, so $q - x \in Q$. Hence $q - x \in Q \cap N = P \cap N \subseteq P$. Therefore $q = x + (q - x) \in P$. So $Q \subseteq P$, giving $P = Q$.

> [!note]- Lemma 3: A chain in $M$ stabilises if its two shadow chains do
> **Statement:** With $N \subseteq M$ and $p : M \to M/N$, let $P_1 \subseteq P_2 \subseteq \cdots$ be a chain in $M$. If both $\{P_k \cap N\}$ and $\{p(P_k)\}$ stabilise, so does $\{P_k\}$.
>
> **Hint:** Choose $j$ past which both shadow chains are constant, then apply the squeezing lemma to $P_j \subseteq P_k$ for $k \geq j$.
>
> **Why needed:** It is the reverse direction once the shadows are stabilised by Noetherianity of $N$ and $L$.
>
> > [!note]- Full proof
> > Suppose $\{P_k \cap N\}$ is constant for $k \geq j_1$ and $\{p(P_k)\}$ is constant for $k \geq j_2$; set $j = \max(j_1, j_2)$. For any $k \geq j$ we have $P_j \subseteq P_k$ with $P_j \cap N = P_k \cap N$ and $p(P_j) = p(P_k)$. By Lemma 2, $P_j = P_k$. Hence the chain $\{P_k\}$ is constant for $k \geq j$, i.e. it stabilises.

---

# Formal Proof

> [!note]- Complete formal proof
> Identify $N$ with the submodule $i(N) \subseteq M$ and $L$ with $M/N$ via the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]] (legitimate since $i$ is injective and $p$ is surjective with $\ker p = i(N)$). We prove the Noetherian case; the Artinian case is obtained by reversing every inclusion throughout.
>
> ---
> **($\Rightarrow$) $M$ Noetherian implies $N$ and $L$ Noetherian.** This is Lemma 1: submodules and quotients of a Noetherian module are Noetherian.
>
> ---
> **($\Leftarrow$) $N$ and $L$ Noetherian implies $M$ Noetherian.** Let $P_1 \subseteq P_2 \subseteq \cdots$ be an ascending chain of submodules of $M$. Form the two derived chains:
> $$P_1 \cap N \subseteq P_2 \cap N \subseteq \cdots \quad \text{(in } N\text{)}, \qquad p(P_1) \subseteq p(P_2) \subseteq \cdots \quad \text{(in } L = M/N\text{)}.$$
> Each $P_k \cap N$ is a submodule of $N$ and each $p(P_k)$ is a submodule of $L$, and both sequences are ascending. Since $N$ is Noetherian the first stabilises, and since $L$ is Noetherian the second stabilises. By Lemma 3 the chain $\{P_k\}$ stabilises. Hence $M$ satisfies ACC and is Noetherian.
>
> ---
> **Corollary (finite direct sums).** For $n = 2$, the sequence $0 \to M_1 \to M_1 \oplus M_2 \to M_2 \to 0$ (inclusion of the first summand, projection onto the second) is short exact, so by the theorem $M_1 \oplus M_2$ is Noetherian (resp. Artinian) when $M_1, M_2$ are. For general $n$, induct using $M_1 \oplus \cdots \oplus M_n \cong M_1 \oplus (M_2 \oplus \cdots \oplus M_n)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Finitely generated abelian groups.** Apply the corollary to $\mathbb{Z}^n = \mathbb{Z} \oplus \cdots \oplus \mathbb{Z}$: since $\mathbb{Z}$ is a Noetherian $\mathbb{Z}$-module, so is $\mathbb{Z}^n$, hence every subgroup of a finitely generated abelian group is finitely generated. The application is non-obvious because it derives a structural fact about abelian groups purely from the direct-sum corollary, with no use of the fundamental theorem.

**Noetherian-ness of matrix rings as modules.** The ring $M_n(R)$ of $n \times n$ matrices over a Noetherian ring $R$ is, as an $R$-module, $R^{\oplus n^2}$, hence Noetherian by the corollary; so every left ideal that is an $R$-submodule satisfies ACC. The application is non-obvious because it treats a non-commutative ring's additive structure through the commutative direct-sum result.

**Coherent sheaves and the two-out-of-three principle in geometry.** On a Noetherian scheme, the property "coherent" is two-out-of-three on short exact sequences of $\mathcal{O}_X$-modules — if two of three terms are coherent, so is the third — by exactly this lemma applied locally on each affine open. The application is non-obvious because the same bookkeeping that controls modules controls sheaves stalk-by-stalk; the local-to-global passage is what makes coherence a workable global condition.

---

# Bridges

- **[[Thm - Finitely Generated Modules over a Noetherian Ring are Noetherian|Finitely generated modules over a Noetherian ring are Noetherian]]** — the immediate downstream theorem. Its proof is *this lemma applied twice*: the corollary makes $R^{\oplus \ell}$ Noetherian, and the inheritance direction (Lemma 1) makes the quotient $M \cong R^{\oplus \ell}/K$ Noetherian. Without the two-out-of-three lemma there would be no way to pass from "$R$ is Noetherian" to "finitely generated $R$-modules are Noetherian".

- **[[Thm - Length is Additive and Finite iff Noetherian and Artinian|Additivity of length]]** — the refinement when both conditions hold. Running the theorem for Noetherian and Artinian simultaneously shows finite length is two-out-of-three, and the composition factors of $M$ are exactly those of $N$ together with those of $L$, which is additivity $\ell(M) = \ell(N) + \ell(L)$. This lemma is the qualitative statement; additivity is its quantitative sharpening.

- **[[Def - Exact Sequence and Short Exact Sequence|Short exact sequences]]** — the notation that makes the theorem expressible. The theorem is the first reason short exact sequences earn their keep: they are the device along which finiteness properties are conserved. The same "two-out-of-three along a short exact sequence" pattern recurs for flatness, projectivity, finite generation, and finite presentation throughout commutative algebra.

- **[[Thm - Isomorphism Theorems for Modules|The isomorphism/correspondence theorems]]** — the tool inside the proof. Identifying $L$ with $M/N$ and lifting chains in the quotient to chains in $M$ both rely on the correspondence theorem; the squeezing lemma uses the kernel description $\ker p = N$. These are the gears that make the shadow-chain argument run.

---

# Unlocked by This

> [!tip] Coherence and finiteness conditions on schemes *(from Algebraic Geometry)*
> The two-out-of-three principle along short exact sequences is the defining stability of **coherent sheaves**: on a Noetherian scheme, in $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$, any two coherent forces the third. This is what makes the category of coherent sheaves abelian and is the foundation of the cohomological finiteness theorems (Serre, Grothendieck). It is this module lemma, applied on affine opens.

> [!tip] Dévissage *(from Commutative Algebra and K-theory)*
> Building a module by a filtration with controlled quotients and propagating a property up the filtration via two-out-of-three is the technique called **dévissage** ("unscrewing"). It reduces statements about all finitely generated modules to statements about $R/\mathfrak{p}$ for primes $\mathfrak{p}$, and is the engine behind many computations in dimension theory and algebraic K-theory.
