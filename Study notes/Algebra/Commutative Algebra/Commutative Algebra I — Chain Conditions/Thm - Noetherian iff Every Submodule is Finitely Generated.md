---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Finitely Generated Module"
  - "Def - Noetherian and Artinian Module"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; modules are unital. Let $R$ be a ring and $M$ an [[Def - Module|$R$-module]]. A [[Def - Submodule|submodule]] $N \subseteq M$ is **[[Def - Finitely Generated Module|finitely generated]]** if $N = R n_1 + \cdots + R n_k$ for finitely many $n_i \in N$. The module $M$ is **[[Def - Noetherian and Artinian Module|Noetherian]]** if every ascending chain of submodules $M_1 \subseteq M_2 \subseteq \cdots$ stabilises (the ascending chain condition, ACC). The full registry is on [[Commutative Algebra I — Chain Conditions]].

---

# Statement

> **Theorem (Noetherian $\iff$ every submodule finitely generated).** Let $M$ be an $R$-module. The following are equivalent:
>
> 1. **(ACC.)** Every ascending chain of submodules $M_1 \subseteq M_2 \subseteq \cdots$ of $M$ stabilises.
> 2. **(Maximal condition.)** Every non-empty set of submodules of $M$ has a maximal element.
> 3. **(Finite generation.)** Every submodule of $M$ (including $M$ itself) is finitely generated.
>
> Any one of these may be taken as the definition of *$M$ is Noetherian*.

> **Corollary.** Every Noetherian module is finitely generated. The converse is false.

The corollary follows by applying (3) to the submodule $M \subseteq M$. The converse fails — finitely generated does *not* imply Noetherian — because a submodule of a finitely generated module need not be finitely generated.

---

# Motivation

The ascending chain condition, the form in which Noetherian is usually *stated*, is awkward to *use*: it is a statement about all infinite chains at once, and you rarely want to manipulate an infinite chain directly. What you actually want in a proof is to reach into a submodule and pull out a finite generating set — to treat "Noetherian" as a license for finiteness. This theorem provides exactly that license, by showing the chain condition is equivalent to the concrete, constructive statement that every submodule is finitely generated.

The equivalence matters because it lets the two faces of Noetherian be deployed for the two kinds of task. When you want to *refute* Noetherian, you use ACC: exhibit one chain that does not stabilise. When you want to *use* Noetherian inside a proof, you use finite generation: grab generators of whatever submodule you are working with, knowing there are only finitely many. And when you want to run an *existence* argument by contradiction, you use the maximal condition: among all submodules failing some property, choose a maximal one and derive a contradiction by enlarging it. Three formulations, three jobs, one underlying condition.

The corollary draws the boundary of the concept. Noetherian is *stronger* than finitely generated — strictly stronger — and the gap is precisely that finite generation is not hereditary. This is the entire reason the chain condition exists: it is "finite generation, made to survive passage to submodules". Without this theorem, one might believe finitely generated modules already have the good behaviour needed for commutative algebra; the theorem and its (failing) converse together show that they do not, and pinpoint Noetherian as the correct, robust replacement.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition $A$ is "$M$ satisfies ACC". Several common situations imply $A$ without looking like a chain condition.

The first disguised source is **$M$ is a finitely generated module over a Noetherian ring**. The property $B$ is "$R$ is Noetherian and $M = Rm_1 + \cdots + Rm_k$". The bridge is that $M$ is then a quotient of $R^{\oplus k}$, which is Noetherian because finite direct sums of Noetherian modules are Noetherian, and quotients inherit ACC — so $A$ holds. The non-obvious part is that finiteness of the *generators* plus a chain condition on the *ring* produces a chain condition on the *module*. *Example problem:* show every submodule of $\mathbb{Z}^3$ is finitely generated — $\mathbb{Z}$ is Noetherian, so $\mathbb{Z}^3$ is a Noetherian module, so use (3).

The second disguised source is **$M$ has finite length**. The property $B$ is "$\ell(M) < \infty$". Finite length forces both chain conditions (a strictly ascending chain raises length, a strictly descending one lowers it, and length is a fixed finite integer), so in particular ACC holds. The non-obviousness: a *numerical* finiteness ($\ell < \infty$) yields the *order-theoretic* finiteness (ACC). *Example problem:* over a field, a finite-dimensional vector space has every subspace finitely generated, because $\ell = \dim < \infty$.

The third disguised source is **$M$ is an extension of two Noetherian modules**. The property $B$ is "there is a short exact sequence $0 \to N \to M \to L \to 0$ with $N, L$ Noetherian". By [[Thm - Chain Conditions Pass Through Short Exact Sequences|the two-out-of-three lemma]], $M$ is Noetherian, so ACC holds. The non-obviousness is that the chain condition is *assembled* from sub and quotient. *Example problem:* show $M_1 \oplus M_2$ is Noetherian when each $M_i$ is, hence every submodule of it is finitely generated.

**Targets (Output Amplification)**

The conclusion $C$ is "every submodule of $M$ is finitely generated", or equivalently ACC / the maximal condition.

Combine $C$ with **a presentation of an ideal in $R[T]$ by leading coefficients**. When $M = R$ is Noetherian, $C$ says every ideal of $R$ is finitely generated; feeding this into the leading-coefficient argument gives that $R[T]$ is Noetherian. The further result $E$ is **Hilbert's basis theorem**: finite generation of ideals in $R$, run through degree-tracking, yields finite generation of ideals in $R[T]$. This is non-obvious because it bootstraps finiteness from the base ring to a strictly larger polynomial ring.

Combine the **maximal condition** with **a "choose a maximal counterexample" setup**. To prove every submodule has a property $P$, suppose not, take a submodule $N$ maximal among those failing $P$ (available by the maximal condition), and contradict maximality by exhibiting a strictly larger failing submodule or by showing $N$ actually has $P$. The further result $E$ is the entire family of **Noetherian-induction existence theorems**: that every ideal is a finite intersection of irreducible ideals, that primary decompositions exist, that associated primes are finite. The combination is non-obvious because it converts a universal statement (all submodules) into a single extremal choice.

Combine $C$ with **the corollary "Noetherian $\Rightarrow$ finitely generated"**. Once a module is known Noetherian, it and all its submodules are finitely generated *for free*, so any later argument may assume finite generating sets everywhere. The further result $E$ is that **submodules of finitely generated modules over a Noetherian ring are finitely generated** — the working hypothesis under which structure theory operates. The combination is the standard "we may assume everything in sight is finitely generated" reduction.

---

# Why Is It True

The heart of the matter is a tight correspondence between *non-stabilising chains* and *infinite generating processes*. A submodule that is not finitely generated is one you can keep adding generators to forever; an ascending chain that does not stabilise is exactly such a process made visible. The theorem says these are the same phenomenon.

**The bolded mechanism: a non-finitely-generated submodule *is* a non-stabilising chain — list its generators one at a time and the partial sums never catch up; conversely a non-stabilising chain *is* a non-finitely-generated union — its limit cannot be generated by any finite stage.**

Run the mechanism in each direction. Suppose some submodule $N$ is not finitely generated. Build a chain inside it greedily: pick any $n_1 \in N$ and set $N_1 = Rn_1$; since $N$ is not finitely generated, $N_1 \neq N$, so pick $n_2 \in N \setminus N_1$ and set $N_2 = Rn_1 + Rn_2$; again $N_2 \neq N$, so continue. This produces a strictly ascending chain $N_1 \subsetneq N_2 \subsetneq \cdots$ that never stabilises — violating ACC. So ACC forces every submodule to be finitely generated. Conversely, suppose ACC fails, witnessed by $M_1 \subsetneq M_2 \subsetneq \cdots$. Let $N = \bigcup_i M_i$, which is a submodule (a union of a chain of submodules is a submodule). If $N$ were finitely generated by $\{x_1, \dots, x_k\}$, each $x_j$ would lie in some $M_{i_j}$, and taking $i = \max_j i_j$ all the generators sit in $M_i$, forcing $N = M_i$ and collapsing the chain from stage $i$ on — contradicting strictness. So $N$ is not finitely generated, and the failure of ACC produced a non-finitely-generated submodule. The two directions are the same construction read forwards and backwards: *enumerate generators $\leftrightarrow$ ascend the chain*.

The maximal condition is ACC restated by contraposition. To say "every non-empty family has a maximal element" is to say "no non-empty family is without a maximal element", and a family without a maximal element is precisely one where every member is strictly below another — from which you can greedily extract an infinite strictly ascending chain. So the maximal condition fails exactly when ACC fails; they are logically the same, with the choice principle (axiom of choice) needed only to make the infinitely many greedy selections in the harder direction.

The reason the corollary's converse fails is now transparent: finite generation of $M$ controls only $M$, not its submodules, and the greedy chain that witnesses non-Noetherian lives *inside* a submodule. The module $\mathbb{Z}[T_1, T_2, \dots]$ is generated by $1$ as a module over itself, yet inside it the submodule of constant-term-zero polynomials supports the never-stabilising chain $\langle T_1 \rangle \subsetneq \langle T_1, T_2 \rangle \subsetneq \cdots$ — finitely generated at the top, infinitely generated within.

---

# What Makes This Hard

The genuinely non-obvious step is the *greedy chain construction* in the direction "not finitely generated $\Rightarrow$ ACC fails": you must actively *build* an ascending chain by repeatedly choosing a new element outside the current submodule, and recognise that non-finite-generation is exactly what guarantees you never get stuck. Most people stall by trying to prove the contrapositive abstractly instead of constructing the witnessing chain. The other subtlety, easy to miss, is that the union of an ascending chain of submodules is a submodule — this is where the chain "limits" to a non-finitely-generated module, and it quietly uses that the chain is *totally ordered*. The common error is forgetting that the equivalence of the maximal condition with ACC needs the axiom of choice in one direction.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the cycle $(1) \Rightarrow (3) \Rightarrow (2) \Rightarrow (1)$, or more transparently prove $(1) \Leftrightarrow (3)$ directly by the greedy-chain/union correspondence and $(1) \Leftrightarrow (2)$ by contraposition. The single idea is that a non-stabilising ascending chain and a non-finitely-generated submodule are interconvertible by "enumerate generators".

**Subgoal decomposition:**

1. **$(1) \Rightarrow (3)$: ACC implies every submodule finitely generated.**
   - *Hint:* Given a submodule $N$, consider the family of its finitely generated sub-submodules; by the maximal condition (or directly by ACC) it has a maximal member $N_0$, and maximality forces $N_0 = N$.
   - *Why needed:* This is the "use" direction — it licenses grabbing finitely many generators.

2. **$(3) \Rightarrow (1)$: every submodule finitely generated implies ACC.**
   - *Hint:* Given a chain $M_1 \subseteq M_2 \subseteq \cdots$, take its union $N = \bigcup M_i$ (a submodule), pick finite generators, locate them all in some single $M_i$, and conclude the chain stabilises at $i$.
   - *Why needed:* This is the "refute" direction — it shows finite generation forces chains to stop.

3. **$(1) \Leftrightarrow (2)$: ACC equals the maximal condition.**
   - *Hint:* A family with no maximal element lets you greedily build an infinite strictly ascending chain; conversely a non-stabilising chain is a family with no maximal element. (Axiom of choice for the greedy selection.)
   - *Why needed:* It supplies the "choose a maximal counterexample" form used in existence proofs.

---

# Lemma Decomposition

> [!note]- Lemma 1: The union of an ascending chain of submodules is a submodule
> **Statement:** If $M_1 \subseteq M_2 \subseteq \cdots$ is an ascending chain of submodules of $M$, then $N = \bigcup_{i} M_i$ is a submodule of $M$.
>
> **Hint:** To check closure under addition, given $x \in M_i$ and $y \in M_j$, use that the chain is totally ordered to put both in the larger of $M_i, M_j$.
>
> **Why needed:** It is the object that "limits" a non-stabilising chain; finite generators of it would all lie at a finite stage, forcing stabilisation.
>
> > [!note]- Full proof
> > Let $x, y \in N$ and $r \in R$. Then $x \in M_i$ and $y \in M_j$ for some $i, j$; without loss $i \leq j$, so $M_i \subseteq M_j$ and both $x, y \in M_j$. Since $M_j$ is a submodule, $x + y \in M_j \subseteq N$ and $rx \in M_j \subseteq N$. Also $0 \in M_1 \subseteq N$. Hence $N$ is closed under addition and scalar multiplication and contains $0$, so it is a submodule.

> [!note]- Lemma 2: A finitely generated submodule sits at a finite stage of any chain whose union contains it
> **Statement:** If $N = \bigcup_i M_i$ is finitely generated, say by $x_1, \dots, x_k$, then $N = M_i$ for some single index $i$.
>
> **Hint:** Each generator lies at some finite stage; take the maximum of the finitely many stages.
>
> **Why needed:** This is the mechanism by which finite generation kills a non-stabilising chain — it is the crux of $(3) \Rightarrow (1)$.
>
> > [!note]- Full proof
> > Each $x_j \in N = \bigcup_i M_i$, so $x_j \in M_{i_j}$ for some index $i_j$. Let $i = \max\{i_1, \dots, i_k\}$ (a maximum of finitely many integers). Since the chain is ascending, $M_{i_j} \subseteq M_i$ for all $j$, so all generators $x_1, \dots, x_k \in M_i$. Then $N = Rx_1 + \cdots + Rx_k \subseteq M_i \subseteq N$, forcing $N = M_i$. Consequently $M_{i'} = M_i$ for all $i' \geq i$ (each $M_{i'}$ is squeezed between $M_i$ and $N = M_i$), so the chain stabilises.

> [!note]- Lemma 3: Under ACC, every submodule has a maximal finitely-generated sub-submodule, equal to itself
> **Statement:** Assume $M$ satisfies ACC. For any submodule $N$, the family $\mathcal{F}$ of finitely generated submodules of $N$ has a maximal element $N_0$, and $N_0 = N$.
>
> **Hint:** ACC gives a maximal element of $\mathcal{F}$ (it is non-empty: $0 \in \mathcal{F}$). If $N_0 \neq N$, adjoin an element of $N \setminus N_0$ to get a strictly larger finitely generated submodule.
>
> **Why needed:** It is the engine of $(1) \Rightarrow (3)$: it converts ACC into "every submodule is finitely generated".
>
> > [!note]- Full proof
> > The family $\mathcal{F}$ of finitely generated submodules of $N$ is non-empty (it contains $\{0\}$). By ACC — equivalently the maximal condition, which ACC implies — $\mathcal{F}$ has a maximal element $N_0$. Suppose $N_0 \neq N$; pick $y \in N \setminus N_0$. Then $N_0 + Ry$ is a submodule of $N$, it is finitely generated (by the finite generators of $N_0$ together with $y$), and it strictly contains $N_0$ (since $y \notin N_0$). This contradicts the maximality of $N_0$ in $\mathcal{F}$. Hence $N_0 = N$, so $N$ is finitely generated.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove $(1) \Rightarrow (3) \Rightarrow (1)$ and $(1) \Leftrightarrow (2)$.
>
> ---
> **$(1) \Rightarrow (3)$.** Assume ACC. We first note ACC implies the maximal condition (2): if some non-empty family $\Sigma$ of submodules had no maximal element, then starting from any $N_1 \in \Sigma$ we could, at each stage, find $N_{j+1} \in \Sigma$ with $N_j \subsetneq N_{j+1}$ (no maximal element means every member is strictly contained in another), producing a non-stabilising ascending chain — contradicting ACC. (This selection uses the axiom of choice.) Now let $N$ be any submodule. By Lemma 3, applying the maximal condition to the family of finitely generated submodules of $N$ yields a maximal such submodule $N_0$, and $N_0 = N$; hence $N$ is finitely generated.
>
> ---
> **$(3) \Rightarrow (1)$.** Assume every submodule of $M$ is finitely generated. Let $M_1 \subseteq M_2 \subseteq \cdots$ be an ascending chain. By Lemma 1, $N = \bigcup_i M_i$ is a submodule, so by hypothesis it is finitely generated. By Lemma 2, $N = M_i$ for some $i$, and then $M_{i'} = M_i$ for all $i' \geq i$. So the chain stabilises, and ACC holds.
>
> ---
> **$(1) \Leftrightarrow (2)$.** That $(1) \Rightarrow (2)$ was shown in the first paragraph. For $(2) \Rightarrow (1)$: given a chain $M_1 \subseteq M_2 \subseteq \cdots$, the family $\{M_i : i \geq 1\}$ is non-empty, so by (2) it has a maximal element $M_n$; then $M_{n'} \subseteq M_n$ for all $n'$, but $M_n \subseteq M_{n'}$ for $n' \geq n$ by ascent, so $M_{n'} = M_n$ for all $n' \geq n$, i.e. the chain stabilises. Hence (1), (2), (3) are equivalent.
>
> ---
> **Corollary.** Apply (3) to the submodule $M$ itself: $M$ is finitely generated. The converse fails: $\mathbb{Z}[T_1, T_2, \dots]$ is finitely generated (by $1$) as a module over itself but its constant-term-zero submodule supports the non-stabilising chain $\langle T_1\rangle \subsetneq \langle T_1, T_2\rangle \subsetneq \cdots$, so it is not Noetherian. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Finitely generated abelian groups via $\mathbb{Z}$ Noetherian.** Since $\mathbb{Z}$ is a Noetherian ring, every subgroup of a finitely generated abelian group is finitely generated — the first step toward the structure theorem for finitely generated abelian groups. The application is non-obvious because "subgroups of finitely generated abelian groups are finitely generated" is usually proved by a direct rank argument, but it is a one-line consequence of $\mathbb{Z}$ Noetherian via this theorem applied to $M = \mathbb{Z}^n$.

**Ideals of rings of integers in number theory.** The ring of integers $\mathcal{O}_K$ of a number field is Noetherian (it is a finitely generated $\mathbb{Z}$-module, hence a Noetherian module, hence a Noetherian ring), so every ideal is finitely generated — in fact generated by two elements. The application is non-obvious because finite generation of ideals is the structural input that lets ideal factorisation in Dedekind domains even get started.

**Constraint propagation and well-founded termination in computer science.** The maximal-condition form is the abstract content of "no infinite strictly increasing sequence", which is precisely the well-foundedness used to prove *termination* of algorithms (Gröbner basis computation, term-rewriting systems). The application maps the algebraic ACC to the computational guarantee that a process adding generators must halt; the leading-monomial ideals of a Gröbner basis computation ascend, and Noetherianity is why Buchberger's algorithm terminates.

---

# Bridges

- **[[Thm - Noetherian Rings and Finitely Generated Ideals|Noetherian rings and finitely generated ideals]]** — this theorem is the module-level generalisation of the ring-level equivalence. Specialise $M = R$: submodules of $R$ are ideals, so "every submodule finitely generated" becomes "every ideal finitely generated", recovering the Rings IV result. The module version is what is needed to run inductions over modules rather than just ideals, and the proof is identical with "ideal" replaced by "submodule".

- **[[Thm - Chain Conditions Pass Through Short Exact Sequences|Two-out-of-three for chain conditions]]** — the companion structural tool. This theorem says ACC equals finite-generation-of-submodules; the two-out-of-three lemma says ACC is preserved by extensions. Together they let one certify a module Noetherian (via extensions) and then immediately extract finite generators of any submodule (via this theorem). They are used in tandem in essentially every Noetherianity argument.

- **[[Thm - Finitely Generated Modules over a Noetherian Ring are Noetherian|Finitely generated modules over a Noetherian ring]]** — the source that most often supplies the hypothesis. That theorem produces Noetherian modules; this theorem then says all their submodules are finitely generated. The combination is the standard reduction "over a Noetherian ring, every submodule of every finitely generated module is finitely generated".

- **Noetherian induction** — the proof technique unlocked by the maximal condition. To prove a property of all submodules, take a maximal counterexample and contradict; the validity of this is exactly the maximal condition. This is the engine behind primary decomposition, finiteness of associated primes, and the existence of irreducible-ideal decompositions in [[Commutative Algebra IX — Primary Decomposition]].

---

# Unlocked by This

> [!tip] Hilbert's basis theorem *(from Commutative Algebra)*
> Feeding "every ideal of $R$ is finitely generated" into the leading-coefficient argument yields that every ideal of $R[T]$ is finitely generated — **Hilbert's basis theorem**. This theorem is the indispensable input: it is exactly the finite-generation form of Noetherian (not the chain form) that the leading-coefficient proof consumes. See [[Thm - Hilbert's Basis Theorem (Algebra Form)]].

> [!tip] Noetherian induction and primary decomposition *(from Commutative Algebra)*
> The maximal-condition form licenses **Noetherian induction**: "choose a maximal counterexample". This is the proof method behind the existence of primary decompositions, the finiteness of minimal primes, and the decomposition of every ideal into finitely many irreducible ideals in a Noetherian ring — all developed in [[Commutative Algebra IX — Primary Decomposition]].
