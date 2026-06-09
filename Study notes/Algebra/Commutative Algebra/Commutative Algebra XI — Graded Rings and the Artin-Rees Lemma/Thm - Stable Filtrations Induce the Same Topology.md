---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Ideal"
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Filtration and Stable Filtration"
  - "Def - Noetherian Ring"
  - "Thm - The Artin-Rees Lemma"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring, $\mathfrak{a} \trianglelefteq R$ an [[Def - Ideal|ideal]], and $M$ an [[Def - Module|R-module]]. Two [[Def - Filtration and Stable Filtration|filtrations]] $(M_n)$, $(M_n')$ of $M$ are **equivalent**, written $(M_n) \sim (M_n')$, if there is $n_0 \geq 0$ with $M_{n + n_0} \subseteq M_n'$ and $M_{n + n_0}' \subseteq M_n$ for all $n$ — each is bounded inside a finite shift of the other. The **$\mathfrak{a}$-adic filtration** is $(\mathfrak{a}^n M)$. A filtration defines a **topology** on $M$ with the $M_n$ a basis of open neighbourhoods of $0$. The full registry is on [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma]].

---

# Statement

> **Theorem (stable filtrations are equivalent; they induce the same topology).** Let $R$ be a ring, $\mathfrak{a} \trianglelefteq R$ an ideal, and $M$ an $R$-module.
>
> 1. **(Comparison.)** Every stable $\mathfrak{a}$-filtration $(M_n)$ of $M$ is equivalent to the $\mathfrak{a}$-adic filtration $(\mathfrak{a}^n M)$.
> 2. **(Consequence.)** Any two stable $\mathfrak{a}$-filtrations of $M$ are equivalent to each other, and equivalent filtrations define the same topology on $M$. Hence all stable $\mathfrak{a}$-filtrations of $M$ induce the **same** topology — the $\mathfrak{a}$-adic topology.

The companion statement, joining this to Artin–Rees, is the one used in practice:

> **Corollary (subspace = adic, for submodules).** Let $R$ be Noetherian, $M$ finitely generated, $N \subseteq M$ a submodule. Then the topology on $N$ induced (as a subspace) from the $\mathfrak{a}$-adic topology on $M$ equals the $\mathfrak{a}$-adic topology of $N$ itself.

Statement 1 is the comparison lemma; statement 2 packages it into "stability determines the topology"; the corollary feeds in [[Thm - The Artin-Rees Lemma|Artin–Rees]] (which makes the induced filtration on $N$ stable) to identify the subspace and intrinsic topologies.

---

# Motivation

When you put a topology on a module by declaring "small means deep in the filtration", you face an immediate worry: *the topology might depend on the choice of filtration*, and that would make it a property of the bookkeeping rather than of the module. This theorem removes the worry in the case that matters. It says that as long as the filtration is *stable* — eventually $\mathfrak{a}$-driven — the topology it induces is one and the same, the $\mathfrak{a}$-adic topology. The choice of stable filtration is immaterial; only the ideal $\mathfrak{a}$ matters.

This is exactly what licenses the loose talk of "the $\mathfrak{a}$-adic topology" without specifying a filtration, and "the completion $\hat{M}$" without specifying which tower of quotients you take the inverse limit over. Two different stable filtrations give equivalent towers $M/M_n$, hence the same inverse limit, hence the same completion. The completion is an invariant of $(M, \mathfrak{a})$, not of the filtration — and this theorem is the proof.

The deeper payoff is the corollary, where it joins forces with Artin–Rees. The natural way to topologize a submodule $N \subseteq M$ is *two* ways: give $N$ its own $\mathfrak{a}$-adic topology (filtration $\mathfrak{a}^n N$), or give it the subspace topology from $M$'s $\mathfrak{a}$-adic topology (filtration $N \cap \mathfrak{a}^n M$). A priori these differ. Artin–Rees says the subspace filtration $(N \cap \mathfrak{a}^n M)$ is *stable*; this theorem says any stable $\mathfrak{a}$-filtration of $N$ induces the $\mathfrak{a}$-adic topology; so the two topologies on $N$ coincide. That is the statement "$\mathfrak{a}$-adic is a *subspace-respecting* topology", and it is what makes completion exact on submodules — without it, $\hat{N}$ computed inside $M$ and $\hat{N}$ computed intrinsically could disagree.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a stable $\mathfrak{a}$-filtration" (for statement 1) or "Noetherian + finitely generated + a submodule" (for the corollary).

The first disguised source is **a shifted or perturbed $\mathfrak{a}$-adic filtration**. Any filtration that agrees with $(\mathfrak{a}^n M)$ up to a finite shift — e.g. $M_n = \mathfrak{a}^{n + c}M$ for $n$ large, or a filtration coinciding with the adic one beyond some level — is stable, hence equivalent, hence topology-preserving. The bridge $B \to A$: "differs from the adic filtration by a bounded shift" $\Rightarrow$ "stable" $\Rightarrow$ "same topology". *Example problem:* show two presentations of the completion via different (stable) towers give the same $\hat{M}$.

The second disguised source is **the trace of a stable filtration on a submodule**, supplied by Artin–Rees. The induced filtration $(N \cap M_n)$ is stable by [[Thm - The Artin-Rees Lemma|Artin–Rees]], so it qualifies as input to statement 2. The bridge: "Artin–Rees output" $\Rightarrow$ "stable filtration of $N$" $\Rightarrow$ "induces the $\mathfrak{a}$-adic topology of $N$". *Example problem:* prove the subspace topology equals the adic topology on $N$ (see [[Ex - The Artin-Rees lemma and the subspace topology]]).

The third disguised source is **a filtration arising from a stable filtration on a quotient or extension**. Given a short exact sequence and stable filtrations on two of the three terms, the third inherits a stable filtration, which by this theorem induces the $\mathfrak{a}$-adic topology. The bridge: stability is preserved through the short exact sequence (via Artin–Rees on the sub, directly on the quotient). *Example problem:* show the $\mathfrak{a}$-adic topology on $M/N$ is the quotient topology.

**Targets (Output Amplification)**

The conclusion $C$ is "these (stable) filtrations induce the same topology / are equivalent".

Combine $C$ with **the inverse-limit functor**. Equivalent filtrations give cofinal towers of quotients $M/M_n$ and $M/M_n'$, and cofinal towers have isomorphic inverse limits. The further result $E$: the completion $\hat{M} = \varprojlim M/M_n$ is independent of the stable filtration chosen — an invariant of $(M, \mathfrak{a})$. Non-obvious because "same topology" is a statement about open sets, while "same completion" is a statement about a limit object, and the bridge is cofinality.

Combine $C$ (corollary form) with **left-exactness of completion**. Once the subspace and intrinsic topologies on $N$ agree, the completion $\hat{N}$ injects into $\hat{M}$ with closed image. The further result $E$: $\mathfrak{a}$-adic completion is **exact** on short exact sequences of finitely generated modules over a Noetherian ring. Non-obvious because exactness (not just left-exactness) requires the comparison of topologies that this theorem plus Artin–Rees supplies.

Combine $C$ with **Hausdorffness from Krull intersection**. The common topology is Hausdorff iff $\bigcap_n M_n = 0$, which (under $\mathfrak{a} \subseteq \operatorname{Jac}(R)$) is Krull intersection. The further result $E$: every stable filtration on a finitely generated module over a Noetherian local ring is separated, so the completion is faithful regardless of which stable filtration realizes the topology. Non-obvious because it combines a topology-independence statement with a separatedness theorem to get faithfulness "for all stable filtrations at once".

---

# Why Is It True

Equivalence is a two-sided sandwich, and each side is a one-line filtration estimate. Take a stable $\mathfrak{a}$-filtration $(M_n)$ and compare it to the $\mathfrak{a}$-adic filtration $(\mathfrak{a}^n M)$.

**One side is automatic, for free.** Every $\mathfrak{a}$-filtration *contains* the $\mathfrak{a}$-adic one: iterating $\mathfrak{a}M_k \subseteq M_{k+1}$ down from $M_0 = M$ gives $\mathfrak{a}^n M \subseteq M_n$ for all $n$. So the $\mathfrak{a}$-adic filtration is the finest, and $(M_n)$ sits above it with no shift needed: $\mathfrak{a}^n M \subseteq M_n$.

**The other side is where stability is spent.** We need $M_n$ to sit *inside* a shift of the $\mathfrak{a}$-adic filtration: $M_{n + n_0} \subseteq \mathfrak{a}^n M$ for some fixed $n_0$. Stability provides exactly this. By definition there is $n_0$ with $\mathfrak{a}M_k = M_{k+1}$ for $k \geq n_0$, so beyond level $n_0$ the filtration is generated from $M_{n_0}$ by powers of $\mathfrak{a}$:
$$M_{n + n_0} = \mathfrak{a}^n M_{n_0} \subseteq \mathfrak{a}^n M.$$
The containment $M_{n_0} \subseteq M$ does the rest. So $M_{n + n_0} \subseteq \mathfrak{a}^n M$, the second half of the sandwich.

Putting the two together, $\mathfrak{a}^n M \subseteq M_n$ and $M_{n + n_0} \subseteq \mathfrak{a}^n M$: the two filtrations are equivalent. **The whole content is: any $\mathfrak{a}$-filtration dominates the adic one for free, and stability is exactly the bounded reverse domination $M_{n+n_0} = \mathfrak{a}^n M_{n_0} \subseteq \mathfrak{a}^n M$.**

Now the topology. A filtration's topology has the $M_n$ as a neighbourhood basis of $0$. Two filtrations give the same topology iff each one's basic neighbourhoods are eventually contained in the other's — iff every $M_n$ contains some $M_m'$ and vice versa. That is *precisely* the equivalence relation: $M_{n + n_0} \subseteq M_n'$ says the $(n+n_0)$-th neighbourhood of $(M_m)$ fits inside the $n$-th of $(M_m')$, so the two filtrations are cofinal as neighbourhood bases. Equivalence and "same topology" are the same statement, read once for sets and once for open neighbourhoods. Hence all stable filtrations, being equivalent to the adic one, are mutually equivalent and induce one topology.

---

# What Makes This Hard

There is little technical difficulty; the subtlety is conceptual. The non-obvious point is that *only one* of the two inclusions needs stability — the inclusion $\mathfrak{a}^n M \subseteq M_n$ is free (true for any $\mathfrak{a}$-filtration), and stability is spent entirely on the *reverse* bounded inclusion $M_{n+n_0} \subseteq \mathfrak{a}^n M$. People often try to prove both directions with stability and get confused. The second common error is to conflate "equivalent" (sandwiched within a finite shift) with "equal"; the filtrations are usually *not* equal — the shift $n_0$ is genuinely present, as the shifted adic filtration shows — but equivalence is all the topology sees.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove equivalence of any stable $(M_n)$ with the adic $(\mathfrak{a}^n M)$ by a two-sided sandwich. The inclusion $\mathfrak{a}^n M \subseteq M_n$ is free from the $\mathfrak{a}$-filtration property; the reverse $M_{n+n_0} \subseteq \mathfrak{a}^n M$ comes from stability via $M_{n+n_0} = \mathfrak{a}^n M_{n_0}$. Then observe that equivalence of filtrations is literally the cofinality of their neighbourhood bases, so equivalent filtrations give the same topology. For the corollary, feed in Artin–Rees to make the induced filtration on $N$ stable.

**Subgoal decomposition:**

1. **Adic is finest.** Show $\mathfrak{a}^n M \subseteq M_n$ for any $\mathfrak{a}$-filtration.
   - *Hint:* Iterate $\mathfrak{a}M_k \subseteq M_{k+1}$ from $M_0 = M$.
   - *Why needed:* It is the free half of the sandwich.

2. **Stability gives bounded reverse inclusion.** Show $M_{n + n_0} \subseteq \mathfrak{a}^n M$ for the stabilization index $n_0$.
   - *Hint:* $\mathfrak{a}M_k = M_{k+1}$ for $k \geq n_0$ gives $M_{n+n_0} = \mathfrak{a}^n M_{n_0} \subseteq \mathfrak{a}^n M$.
   - *Why needed:* It is the half that uses stability; together with step 1 it yields equivalence.

3. **Equivalence $\Rightarrow$ same topology.** Show equivalent filtrations have cofinal neighbourhood bases, hence the same topology.
   - *Hint:* $M_{n+n_0} \subseteq M_n'$ says every $M_n'$-neighbourhood contains an $M_m$-neighbourhood and vice versa.
   - *Why needed:* It upgrades the set-level equivalence to topological identity.

4. **Corollary via Artin–Rees.** Show the subspace and intrinsic topologies on $N$ agree.
   - *Hint:* [[Thm - The Artin-Rees Lemma|Artin–Rees]] makes $(N \cap \mathfrak{a}^n M)$ stable; apply steps 1–3 to $N$.
   - *Why needed:* It is the practically used statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: The adic filtration is the finest $\mathfrak{a}$-filtration
> **Statement:** For any $\mathfrak{a}$-filtration $(M_n)$ of $M$, $\mathfrak{a}^n M \subseteq M_n$ for all $n \geq 0$.
>
> **Hint:** Induct using $\mathfrak{a}M_n \subseteq M_{n+1}$ starting from $M_0 = M$.
>
> **Why needed:** It is one inclusion of the equivalence sandwich, and it holds for free — no stability required.
>
> > [!note]- Full proof
> > Induct on $n$. For $n = 0$, $\mathfrak{a}^0 M = M = M_0$. Suppose $\mathfrak{a}^n M \subseteq M_n$. Then $\mathfrak{a}^{n+1}M = \mathfrak{a}(\mathfrak{a}^n M) \subseteq \mathfrak{a}M_n \subseteq M_{n+1}$, the last by the $\mathfrak{a}$-filtration property. Hence $\mathfrak{a}^n M \subseteq M_n$ for all $n$.

> [!note]- Lemma 2: Stability gives a bounded reverse inclusion
> **Statement:** If $(M_n)$ is a stable $\mathfrak{a}$-filtration with $\mathfrak{a}M_k = M_{k+1}$ for $k \geq n_0$, then $M_{n + n_0} \subseteq \mathfrak{a}^n M$ for all $n \geq 0$.
>
> **Hint:** Stability above $n_0$ gives $M_{n + n_0} = \mathfrak{a}^n M_{n_0}$; then $M_{n_0} \subseteq M$.
>
> **Why needed:** It is the other inclusion of the sandwich, and the only place stability is used.
>
> > [!note]- Full proof
> > For $k \geq n_0$, stability gives $M_{k+1} = \mathfrak{a}M_k$. Iterating from $k = n_0$: $M_{n_0 + 1} = \mathfrak{a}M_{n_0}$, $M_{n_0 + 2} = \mathfrak{a}M_{n_0 + 1} = \mathfrak{a}^2 M_{n_0}$, and in general $M_{n + n_0} = \mathfrak{a}^n M_{n_0}$ for all $n \geq 0$. Since $M_{n_0} \subseteq M_0 = M$, we get $M_{n + n_0} = \mathfrak{a}^n M_{n_0} \subseteq \mathfrak{a}^n M$.

> [!note]- Lemma 3: Equivalent filtrations induce the same topology
> **Statement:** If $(M_n) \sim (M_n')$ (each bounded within a finite shift of the other), then the two filtration topologies on $M$ coincide.
>
> **Hint:** A filtration topology has the $M_n$ as a neighbourhood basis of $0$; equivalence says each basis refines the other.
>
> **Why needed:** It converts the set-theoretic equivalence into topological identity, which is the actual conclusion.
>
> > [!note]- Full proof
> > The topology defined by $(M_n)$ has as a basis of open neighbourhoods of $0$ the submodules $M_n$ (and their translates $x + M_n$ as a basis of opens). Suppose $M_{n + n_0} \subseteq M_n'$ and $M_{n + n_0}' \subseteq M_n$ for all $n$. A set $U$ is open in the $(M_n)$-topology iff around each point it contains some $x + M_m$. Given such a $U$ and a point $x$, $x + M_m \subseteq U$; since $M_{m + n_0}' \subseteq M_m$, also $x + M_{m + n_0}' \subseteq U$, so $U$ is open in the $(M_n')$-topology. By symmetry every $(M_n')$-open set is $(M_n)$-open. Hence the two topologies are equal.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be a ring, $\mathfrak{a} \trianglelefteq R$, $M$ an $R$-module.
>
> **Statement 1 — comparison with the adic filtration.** Let $(M_n)$ be a stable $\mathfrak{a}$-filtration, with $\mathfrak{a}M_k = M_{k+1}$ for $k \geq n_0$. By Lemma 1, $\mathfrak{a}^n M \subseteq M_n$ for all $n$. By Lemma 2, $M_{n + n_0} \subseteq \mathfrak{a}^n M$ for all $n$. The first inclusion is the case "$n_0 = 0$" of the equivalence condition with $(M_n')= (\mathfrak{a}^n M)$ ($\mathfrak{a}^{n}M \subseteq M_n$, i.e. $M'_{n} \subseteq M_n$, and trivially $M'_{n+0} \subseteq M_n$), and the second is $M_{n + n_0} \subseteq \mathfrak{a}^n M = M'_n$. Taking the larger of the two shift constants, $(M_n) \sim (\mathfrak{a}^n M)$.
>
> **Statement 2 — same topology.** Equivalence is transitive and symmetric (a routine check: if $(M_n) \sim (M_n')$ with shift $n_0$ and $(M_n') \sim (M_n'')$ with shift $n_1$, then $(M_n) \sim (M_n'')$ with shift $n_0 + n_1$). By Statement 1, every stable $\mathfrak{a}$-filtration is equivalent to $(\mathfrak{a}^n M)$, hence any two stable $\mathfrak{a}$-filtrations are equivalent to each other. By Lemma 3, equivalent filtrations induce the same topology. Therefore all stable $\mathfrak{a}$-filtrations of $M$ induce the same topology, namely the $\mathfrak{a}$-adic topology.
>
> ---
> **Corollary — subspace equals adic on a submodule.** Let $R$ be Noetherian, $M$ finitely generated, $N \subseteq M$. The subspace topology on $N$ induced from the $\mathfrak{a}$-adic topology on $M$ is, by definition, the topology of the filtration $(N \cap \mathfrak{a}^n M)$. By the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]], $(N \cap \mathfrak{a}^n M)$ is a *stable* $\mathfrak{a}$-filtration of $N$. By Statement 2 applied to $N$, it induces the $\mathfrak{a}$-adic topology of $N$ (that of $(\mathfrak{a}^n N)$). Hence the subspace topology on $N$ equals its intrinsic $\mathfrak{a}$-adic topology. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Metric comparison of equivalent norms.** The equivalence of filtrations is the algebraic analogue of equivalence of norms: two filtrations are equivalent iff the associated "valuation pseudo-metrics" $d(x,y) = 2^{-\nu(x-y)}$ (where $\nu$ is the order in the filtration) are uniformly comparable. Recognising that "stable $\Rightarrow$ equivalent to adic" is the algebraic mirror of "all norms on a finite-dimensional space are equivalent" makes the topology-independence intuitive. The application is non-obvious because it links a discrete filtration statement to the functional-analytic fact about norm equivalence.

**Cofinality of inverse systems.** In the theory of inverse limits, two inverse systems with cofinal index maps have isomorphic limits. The statement "equivalent filtrations give the same completion" is exactly this cofinality principle applied to the towers $M/M_n$. The application is non-obvious because it explains *why* the completion is filtration-independent in categorical rather than computational terms — a useful reframing when constructing completions of topological groups generally.

**Adic versus subspace in lattices and codes.** For an integer lattice $N \subseteq \mathbb{Z}^k$ and a prime $p$, the corollary says the $p$-adic subspace topology on $N$ equals its intrinsic $p$-adic topology, which underlies the fact that $p$-adic approximation on a sublattice (used in lattice-based cryptography and coding) is governed by the sublattice's own $p$-adic structure up to a bounded loss. The application is non-obvious because it certifies that "reduce mod $p^n$ on the sublattice" loses only a bounded amount of precision relative to the ambient lattice.

---

# Bridges

- **[[Thm - The Artin-Rees Lemma|The Artin–Rees Lemma]]** — the supplier of stability for submodules. This theorem says "stable filtrations give the $\mathfrak{a}$-adic topology"; Artin–Rees says "the trace of the $\mathfrak{a}$-adic filtration on a submodule *is* stable". Composing them yields the corollary that the subspace topology equals the intrinsic adic topology — the union of the two is what makes the $\mathfrak{a}$-adic topology well-behaved under submodules.

- **[[Def - Filtration and Stable Filtration|Stable filtration]]** — the notion this theorem certifies as topology-determining. The entire reason to single out *stability* among $\mathfrak{a}$-filtrations is this theorem: stable filtrations are exactly the ones equivalent to the adic one, hence the ones giving the canonical topology and completion. Non-stable $\mathfrak{a}$-filtrations (which plunge faster) give strictly finer topologies and are excluded.

- **The $\mathfrak{a}$-adic completion** — the invariant this theorem protects. Because equivalent filtrations have cofinal quotient towers, they share the inverse limit $\hat{M} = \varprojlim M/M_n$. This theorem is therefore the proof that the completion is an invariant of $(M, \mathfrak{a})$ rather than of a chosen filtration — connecting forward to the chapter on **completions and limits**.

# Unlocked by This

> [!tip] Well-definedness of the completion and the formal disc *(from Commutative Algebra X)*
> This theorem is the reason "**the** $\mathfrak{a}$-adic completion" is a legitimate phrase: any stable $\mathfrak{a}$-filtration produces the same topology and hence the same completion $\hat{M} = \varprojlim M/\mathfrak{a}^n M$, an invariant of $(M, \mathfrak{a})$ alone. This independence is what lets one freely switch between presentations — between $\varprojlim R/\mathfrak{m}^n$ and $\varprojlim R/I_n$ for any stable $(I_n)$ — when computing completions like $\hat{\mathbb{Z}}_p$ or $k[[x_1, \dots, x_d]]$, the **formal disc** that is the local model for **formal schemes** and rigid-analytic geometry. The combination with Artin–Rees, giving subspace = adic on submodules, is in turn what makes completion exact, the property that lets the formal and algebraic categories talk to each other.
