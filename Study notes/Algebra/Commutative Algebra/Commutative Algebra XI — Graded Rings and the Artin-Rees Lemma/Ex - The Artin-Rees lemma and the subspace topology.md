---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Filtration and Stable Filtration"
  - "Def - Noetherian Ring"
  - "Def - Finitely Generated Module"
  - "Def - Submodule"
  - "Thm - The Artin-Rees Lemma"
  - "Thm - Stable Filtrations Induce the Same Topology"
tags: [algebra, commutative-algebra]
---

# Problem Statement

A [[Def - Filtration and Stable Filtration|filtration]] $(M_n)_{n \geq 0}$ of an $R$-module $M$ defines a topology on $M$ with topological basis $\{x + M_n : x \in M,\ n \geq 0\}$. For an [[Def - Ideal|ideal]] $\mathfrak{a} \trianglelefteq R$, the **$\mathfrak{a}$-adic topology** on $M$ is the one from the filtration $(\mathfrak{a}^n M)_{n \geq 0}$.

Let $R$ be a [[Def - Noetherian Ring|Noetherian ring]], $\mathfrak{a} \trianglelefteq R$ an ideal, $M$ a [[Def - Finitely Generated Module|finitely generated]] $R$-module, and $N \subseteq M$ a [[Def - Submodule|submodule]]. Prove that
$$\text{the topology on } N \text{ induced (as a subspace) from the } \mathfrak{a}\text{-adic topology on } M$$
$$\text{equals the } \mathfrak{a}\text{-adic topology on } N \text{ itself.}$$

(This is Example Sheet 4, Q14. The hint there: it follows easily from two claims from the lectures — namely the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]] and the fact that [[Thm - Stable Filtrations Induce the Same Topology|stable filtrations induce the same topology]].)

**Recall:**

![[Thm - The Artin-Rees Lemma#Statement]]

![[Thm - Stable Filtrations Induce the Same Topology#Statement]]

The **subspace topology** on $N \subseteq M$ has as open sets the intersections $U \cap N$ for $U$ open in $M$. Concretely, the $\mathfrak{a}$-adic topology on $M$ restricts to the filtration topology on $N$ given by $(N \cap \mathfrak{a}^n M)_{n \geq 0}$: a basis of neighbourhoods of $0$ in $N$ is $\{N \cap \mathfrak{a}^n M\}$. The *intrinsic* $\mathfrak{a}$-adic topology on $N$ is given by the filtration $(\mathfrak{a}^n N)_{n \geq 0}$. The exercise asks: are these the same topology? A priori $\mathfrak{a}^n N \subseteq N \cap \mathfrak{a}^n M$ always (so the subspace topology is *coarser*), but the reverse — that the subspace neighbourhoods are not too large — is the content.

---

# Convergent Strategy

**Problem class.** This is a *two-topologies-coincide* problem, solved by showing the two defining filtrations are **equivalent** (each bounded within a finite shift of the other). As the [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Problem-Solving Strategy|topic-page strategy]] records, equality of filtration topologies is *never* proved by chasing open sets directly; it is proved by establishing filtration equivalence, because equivalence is exactly cofinality of neighbourhood bases.

**Assumption pattern.** The recognisable trigger is the pairing "Noetherian ring + finitely generated module + a submodule", which is precisely the input type of the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]]. The one inclusion $\mathfrak{a}^n N \subseteq N \cap \mathfrak{a}^n M$ is free (it holds for any submodule, no hypotheses); the *hard* inclusion — that $N \cap \mathfrak{a}^n M$ is not much bigger than $\mathfrak{a}^{n-c}N$ — is exactly what Artin–Rees supplies. So the assumptions route straight to the one theorem whose output is "the induced filtration is stable".

**Theorem routing.** The route is a two-theorem chain. First, [[Thm - The Artin-Rees Lemma|Artin–Rees]] applied to $M, N, \mathfrak{a}$ shows the *subspace filtration* $(N \cap \mathfrak{a}^n M)$ is a **stable** $\mathfrak{a}$-filtration of $N$. Second, [[Thm - Stable Filtrations Induce the Same Topology|stable filtrations induce the same topology]] shows any stable $\mathfrak{a}$-filtration of $N$ — in particular this one — induces the *intrinsic* $\mathfrak{a}$-adic topology of $N$ (that of $(\mathfrak{a}^n N)$). Composing: subspace topology = topology of $(N \cap \mathfrak{a}^n M)$ = intrinsic $\mathfrak{a}$-adic topology. Done.

**Key decision point.** The single non-obvious move is to recognise that "subspace topology" *is* "the topology of the induced filtration $(N \cap \mathfrak{a}^n M)$", and that this filtration is the literal output of Artin–Rees. The naive attempt is to prove $N \cap \mathfrak{a}^n M = \mathfrak{a}^n N$, which is *false* — the two filtrations are equal only up to a bounded shift $c$, not on the nose. The insight is that topology cannot see the shift: equivalence suffices, and Artin–Rees delivers exactly equivalence (stability), not equality. Choosing "prove stability, not equality" is what makes the problem tractable.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Legal Operations|the topic page's Legal Operations]]:

1. **Recognise the subspace topology as an induced filtration (operation 9).** Translate "subspace topology from the $\mathfrak{a}$-adic topology on $M$" into the filtration $(N \cap \mathfrak{a}^n M)$ on $N$.

2. **Invoke Artin–Rees to make an induced filtration stable (operation 4).** Apply [[Thm - The Artin-Rees Lemma|Artin–Rees]] to conclude $(N \cap \mathfrak{a}^n M)$ is a stable $\mathfrak{a}$-filtration.

3. **Replace "topologies coincide" by "filtrations equivalent" (operation 9, topology form).** Use [[Thm - Stable Filtrations Induce the Same Topology|that stable filtrations induce the same topology]] to identify the stable induced filtration's topology with the intrinsic $\mathfrak{a}$-adic one.

---

# Hints

> [!note]- Hint 1
> Translate the topological statement into filtrations. The subspace topology on $N$ has neighbourhood basis $\{N \cap \mathfrak{a}^n M\}$; the intrinsic $\mathfrak{a}$-adic topology has basis $\{\mathfrak{a}^n N\}$. Which inclusion between $\mathfrak{a}^n N$ and $N \cap \mathfrak{a}^n M$ is obvious, and which is the hard one?

> [!note]- Hint 2
> The easy inclusion is $\mathfrak{a}^n N \subseteq N \cap \mathfrak{a}^n M$ (an element of $\mathfrak{a}^n N$ is in $N$ and in $\mathfrak{a}^n M$). This shows the subspace topology is *coarser*. For the reverse, you need to bound $N \cap \mathfrak{a}^n M$ inside some $\mathfrak{a}^{n - c} N$. Which lemma produces a bounded comparison between $(N \cap \mathfrak{a}^n M)$ and the $\mathfrak{a}$-adic filtration of $N$?

> [!note]- Hint 3
> [[Thm - The Artin-Rees Lemma|Artin–Rees]] says $(N \cap \mathfrak{a}^n M)$ is a *stable* $\mathfrak{a}$-filtration of $N$. You do not need to extract the constant $c$ by hand — just use the abstract conclusion "stable". Then which theorem says all stable $\mathfrak{a}$-filtrations of $N$ give the same topology?

> [!note]- Hint 4
> [[Thm - Stable Filtrations Induce the Same Topology|The comparison theorem]]: any stable $\mathfrak{a}$-filtration of $N$ is equivalent to $(\mathfrak{a}^n N)$ and induces the $\mathfrak{a}$-adic topology of $N$. Apply it to the stable filtration $(N \cap \mathfrak{a}^n M)$ from Artin–Rees, and you are done in one line.

---

# Solution

The proof is a two-theorem chain. Step 1 translates the subspace topology into the induced filtration $(N \cap \mathfrak{a}^n M)$ and notes the free inclusion $\mathfrak{a}^n N \subseteq N \cap \mathfrak{a}^n M$. Step 2 invokes Artin–Rees to make $(N \cap \mathfrak{a}^n M)$ stable. Step 3 invokes the comparison theorem to identify its topology with the intrinsic $\mathfrak{a}$-adic topology. The non-obvious point is that one proves *equivalence*, not equality, of the two filtrations.

**Step 1: The subspace topology on $N$ is the topology of the induced filtration $(N \cap \mathfrak{a}^n M)$, and $\mathfrak{a}^n N \subseteq N \cap \mathfrak{a}^n M$.**

The subspace topology restricts the basic neighbourhoods $x + \mathfrak{a}^n M$ to $N$, giving the filtration $(N \cap \mathfrak{a}^n M)$; the intrinsic topology uses $(\mathfrak{a}^n N)$, and the free inclusion shows the subspace topology is a priori coarser.

> [!note]- Derivation
> The $\mathfrak{a}$-adic topology on $M$ has basic open neighbourhoods $x + \mathfrak{a}^n M$. The subspace topology on $N$ has basic neighbourhoods $(x + \mathfrak{a}^n M) \cap N$. For $x \in N$, $(x + \mathfrak{a}^n M) \cap N = x + (N \cap \mathfrak{a}^n M)$ (an element $x + m$ with $m \in \mathfrak{a}^n M$ lies in $N$ iff $m \in N$, i.e. $m \in N \cap \mathfrak{a}^n M$). So the subspace topology on $N$ is exactly the filtration topology of $(N \cap \mathfrak{a}^n M)_n$. This is genuinely a filtration of $N$: it is descending, starts at $N \cap M = N$, and is an $\mathfrak{a}$-filtration since $\mathfrak{a}(N \cap \mathfrak{a}^n M) \subseteq N \cap \mathfrak{a}^{n+1}M$.
>
> The intrinsic $\mathfrak{a}$-adic topology on $N$ is the filtration topology of $(\mathfrak{a}^n N)_n$.
>
> The free inclusion: $\mathfrak{a}^n N \subseteq N \cap \mathfrak{a}^n M$. Indeed $\mathfrak{a}^n N \subseteq N$ (since $N$ is a submodule) and $\mathfrak{a}^n N \subseteq \mathfrak{a}^n M$ (since $N \subseteq M$). This holds with no hypotheses and shows every intrinsic neighbourhood $\mathfrak{a}^n N$ sits inside the subspace neighbourhood $N \cap \mathfrak{a}^n M$ — so the subspace topology is *coarser than or equal to* the intrinsic one. The whole problem is the reverse comparison.

**Step 2: By Artin–Rees, $(N \cap \mathfrak{a}^n M)$ is a stable $\mathfrak{a}$-filtration of $N$.**

The hypotheses (Noetherian $R$, finitely generated $M$, the $\mathfrak{a}$-adic — hence stable — filtration of $M$) put us exactly in the Artin–Rees setting, whose conclusion is that the induced filtration on $N$ is stable.

> [!note]- Derivation
> Recall the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]]: if $R$ is Noetherian, $M$ finitely generated, $(M_n)$ a stable $\mathfrak{a}$-filtration of $M$, and $N \subseteq M$, then $(N \cap M_n)$ is a stable $\mathfrak{a}$-filtration of $N$.
>
> Apply it with $M_n = \mathfrak{a}^n M$, the $\mathfrak{a}$-adic filtration, which is stable (with stabilization index $0$: $\mathfrak{a}\cdot\mathfrak{a}^n M = \mathfrak{a}^{n+1}M$ for all $n$). All hypotheses hold: $R$ is Noetherian, $M$ is finitely generated, $N \subseteq M$. The conclusion is that
> $$(N \cap \mathfrak{a}^n M)_{n \geq 0} \text{ is a stable } \mathfrak{a}\text{-filtration of } N.$$
> Concretely, there is $c \geq 0$ with $N \cap \mathfrak{a}^n M = \mathfrak{a}^{n-c}(N \cap \mathfrak{a}^c M)$ for $n \geq c$, but we will not need the explicit $c$ — only the word "stable".

**Step 3: By the comparison theorem, the stable induced filtration gives the intrinsic $\mathfrak{a}$-adic topology.**

Any stable $\mathfrak{a}$-filtration of $N$ is equivalent to $(\mathfrak{a}^n N)$ and induces the same topology; applying this to $(N \cap \mathfrak{a}^n M)$ identifies the subspace topology with the intrinsic $\mathfrak{a}$-adic topology.

> [!note]- Derivation
> Recall [[Thm - Stable Filtrations Induce the Same Topology|the comparison theorem]]: every stable $\mathfrak{a}$-filtration of a module is equivalent to its $\mathfrak{a}$-adic filtration, and equivalent filtrations induce the same topology.
>
> By Step 2, $(N \cap \mathfrak{a}^n M)$ is a stable $\mathfrak{a}$-filtration of $N$. By the comparison theorem applied to $N$, this filtration is equivalent to $(\mathfrak{a}^n N)$ and induces the *same* topology — namely the $\mathfrak{a}$-adic topology of $N$. But by Step 1, the topology induced by $(N \cap \mathfrak{a}^n M)$ is exactly the subspace topology on $N$. Therefore
> $$\text{subspace topology on } N = \text{intrinsic } \mathfrak{a}\text{-adic topology on } N.$$
> Concretely, equivalence means there is $c$ with both $\mathfrak{a}^n N \subseteq N \cap \mathfrak{a}^n M$ (Step 1, free) and $N \cap \mathfrak{a}^{n + c}M \subseteq \mathfrak{a}^n N$ (from stability) — the two filtrations sandwich each other within the shift $c$, so each basic neighbourhood of one contains a basic neighbourhood of the other, which is exactly equality of topologies.

> [!note]- Complete formal solution
> The subspace topology on $N$ (from the $\mathfrak{a}$-adic topology on $M$) has basic neighbourhoods of $0$ the submodules $N \cap \mathfrak{a}^n M$; the intrinsic $\mathfrak{a}$-adic topology has basic neighbourhoods $\mathfrak{a}^n N$. Always $\mathfrak{a}^n N \subseteq N \cap \mathfrak{a}^n M$, so the subspace topology is coarser.
>
> By the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]] (with $R$ Noetherian, $M$ finitely generated, $(\mathfrak{a}^n M)$ the stable $\mathfrak{a}$-adic filtration, and $N \subseteq M$), the induced filtration $(N \cap \mathfrak{a}^n M)$ is a *stable* $\mathfrak{a}$-filtration of $N$.
>
> By [[Thm - Stable Filtrations Induce the Same Topology|the comparison theorem]], every stable $\mathfrak{a}$-filtration of $N$ is equivalent to $(\mathfrak{a}^n N)$ and induces the same topology. Hence $(N \cap \mathfrak{a}^n M)$ induces the intrinsic $\mathfrak{a}$-adic topology of $N$. Since $(N \cap \mathfrak{a}^n M)$ induces the subspace topology, the subspace topology equals the intrinsic $\mathfrak{a}$-adic topology on $N$. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One is tempted to prove the stronger-looking equality $N \cap \mathfrak{a}^n M = \mathfrak{a}^n N$ for all $n$, which would give the result immediately. **This is false.** Take $R = k[x, y]$, $\mathfrak{a} = (x)$, $M = R$, $N = (x - y) \cap \dots$ — more cleanly, the failure is generic: $N \cap \mathfrak{a}^n M$ collects elements of $N$ that happen to be $n$-fold $\mathfrak{a}$-divisible *in $M$*, using witnesses outside $N$, whereas $\mathfrak{a}^n N$ requires the divisibility to use witnesses *in $N$*. These differ; only the bounded comparison $N \cap \mathfrak{a}^{n+c}M \subseteq \mathfrak{a}^n N$ holds, which is precisely why Artin–Rees (giving stability, i.e. a bounded shift $c$) is the right tool and naive equality is not. The lesson: topological equality needs only equivalence of filtrations, and demanding equality of filtrations over-shoots into a false statement.

---

# Key Takeaways

**To show two adic topologies on the same module coincide, prove the defining filtrations are equivalent — never chase open sets, and never demand the filtrations be equal.** This is the master technique for the whole topological side of the chapter. A filtration topology is determined by its filtration *up to equivalence* (bounded mutual shift), because the basic neighbourhoods of $0$ are the filtration submodules, and "same topology" means "cofinal neighbourhood bases", which is verbatim filtration equivalence. So the reduction "topologies coincide $\iff$ filtrations equivalent" converts a topological question into an algebraic one about containments $M_{n + c} \subseteq M_n'$. The trigger: any time you must compare two adic topologies (subspace vs intrinsic, two ideals defining the same topology, a topology before and after a finite extension), set up the two filtrations and hunt for a uniform shift $c$ bounding each inside the other. The fatal error to avoid is trying to prove the filtrations *equal*; equality is usually false, and the shift $c$ is exactly the slack Artin–Rees provides.

**Artin–Rees is the engine that produces the bounded shift; its true output is "the induced filtration is stable", and stability *is* equivalence to the adic filtration.** The deep reason this exercise is a two-line consequence of the lectures is that Artin–Rees does not just give *a* comparison — it gives the strongest possible one, stability, which by the comparison theorem is the same as equivalence to the canonical $\mathfrak{a}$-adic filtration. So the chain "Artin–Rees $\Rightarrow$ stable $\Rightarrow$ equivalent to adic $\Rightarrow$ same topology" is a reusable pipeline: whenever a submodule, quotient, or extension inherits a filtration from an $\mathfrak{a}$-adic one, Artin–Rees makes the inherited filtration stable, and stability transports it back to the intrinsic adic topology. Recognising this pipeline lets you dispatch a whole family of "the topology behaves well under [submodule / quotient / completion]" statements without ever computing a constant.

**The subspace-equals-adic theorem is what makes completion exact on submodules — the payoff lives downstream.** This exercise looks like a topological curiosity, but it is the technical heart of the statement that $\mathfrak{a}$-adic completion is an *exact* functor on finitely generated modules over a Noetherian ring. The reason: completing the short exact sequence $0 \to N \to M \to M/N \to 0$ requires the completion $\hat{N}$ computed *inside* $M$ (using the subspace filtration) to agree with $N$'s *intrinsic* completion (using $\mathfrak{a}^n N$) — and these agree precisely because the two filtrations are equivalent, which is this exercise. The transferable diagnostic: whenever you need a limit or completion of a submodule to "compute the same thing" whether taken inside the ambient module or intrinsically, the hidden requirement is subspace = adic, supplied by Artin–Rees. This is the bridge to the **$\mathfrak{a}$-adic completion** chapter, where exactness of completion underwrites the comparison of a ring with its completion. See also [[Ex - Krull intersection for a Noetherian local ring]], which uses the same Artin–Rees input to a different end (separatedness rather than exactness).
