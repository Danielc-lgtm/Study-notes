---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Monad Monoid and Module in a Bicategory"
  - "Thm - Monoids and Modules Form a Bicategory"
  - "Def - Ring"
  - "Def - Tensor Product of Modules"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $\mathcal{K}$ be the one-object [[Def - 2-Category and Bicategory|bicategory]] $\mathbf{B}\mathbf{Ab}$ obtained by delooping the monoidal category $(\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z})$ of abelian groups: it has one object $\ast$, $1$-cells $\ast \to \ast$ the abelian groups, and $1$-cell composition the tensor over $\mathbb{Z}$. (More precisely, take $\mathcal{K}$ to be the bicategory of one-object $\mathbf{Ab}$-enriched categories so that a [[Def - Monad Monoid and Module in a Bicategory|monad]] is a ring.) Show that:

1. A monad in $\mathcal{K}$ is a [[Def - Ring|ring]] $R$;
2. A bimodule between rings $R$ and $S$ (a $1$-cell of $\mathrm{Mod}(\mathcal{K})$) is an $(R,S)$-bimodule in the ordinary sense;
3. Horizontal composition in $\mathrm{Mod}(\mathcal{K})$ is $\otimes_S$, and the associativity isomorphism is the canonical balanced-coequalizer iso $(M\otimes_S N)\otimes_T P\cong M\otimes_S(N\otimes_T P)$;
4. Two rings are **Morita-equivalent** iff they are equivalent objects of $\mathrm{Mod}(\mathcal{K})$, i.e. there exist bimodules ${}_SP_R$ and ${}_RQ_S$ with $P\otimes_R Q\cong S$ and $Q\otimes_S P\cong R$.

**Recall:**

![[Def - Monad Monoid and Module in a Bicategory#The Definition]]

A **[[Def - Ring|ring]]** $R$ is a [[Def - Monoid in a Monoidal Category|monoid]] in $(\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z})$: an abelian group with a multiplication $R\otimes R\to R$ and a unit $\mathbb{Z}\to R$ that are associative and unital. An $(R,S)$-bimodule is an abelian group with commuting left $R$- and right $S$-actions. The [[Def - Tensor Product of Modules|tensor over S]] $M\otimes_S N$ is the coequalizer balancing the right $S$-action on $M$ against the left $S$-action on $N$. Two rings are **Morita-equivalent** if their module categories are equivalent.

---

# Convergent Strategy

**Problem class:** A *dictionary-translation plus target-amplification* problem: identify $\mathrm{Mod}(\mathcal{K})$ concretely for the ring base, then combine "bicategory" with "equivalence of objects" to extract Morita theory — the target combination on the [[Thm - Monoids and Modules Form a Bicategory|theorem]] page.

**Assumption pattern:** A ring is a [[Def - Monoid in a Monoidal Category|monoid]] in $\mathbf{Ab}$, hence a [[Def - Monad Monoid and Module in a Bicategory|monad]] in the delooped bicategory; its modules and bimodules transcribe the algebraic ones, and the balancing coequalizer that powers $\mathrm{Mod}(\mathcal{K})$ is exactly $\otimes_S$. The needed local colimits (reflexive coequalizers) exist in $\mathbf{Ab}$ and are preserved by tensoring, so $\mathcal{K}$ is *suitable*.

**Theorem routing:** This is [[Thm - Monoids and Modules Form a Bicategory]] specialised to the ring base, followed by the "equivalence in a bicategory" target combination, which yields Morita equivalence. Associativity routes through Lemma 3 of that theorem (both bracketings are the same iterated balanced coequalizer).

**Key decision point:** The non-obvious move is to recognise *Morita equivalence* — usually defined as equivalence of module categories — as *equivalence of objects in $\mathrm{Mod}(\mathcal{K})$* via invertible bimodules. The temptation is to prove Morita theory from scratch with progenerators; the bicategorical viewpoint makes it the bare definition of "equivalent objects", and the progenerator condition is what an invertible $1$-cell amounts to.

---

# Legal Operations Used

1. **Operation 4 (transcribe monad/module into the ring bicategory).** A monad is a ring, a bimodule is a bimodule.

2. **Operation 5 (read $\mathrm{Mod}(\mathcal{K})$ concretely).** Composition $=$ balanced coequalizer $= \otimes_S$.

3. **Operation 6 (balanced tensor as a coequalizer).** $M\otimes_S N = \mathrm{coeq}(M\otimes S\otimes N\rightrightarrows M\otimes N)$.

4. **Operation 7 (associativity from the coequalizer universal property).** Both bracketings are the same iterated coequalizer.

---

# Hints

> [!note]- Hint 1
> A monad in $\mathcal{K}$ is an endo-$1$-cell $R$ (an abelian group) with $\mu : R\otimes R\Rightarrow R$ and $\eta : \mathbb{Z}\Rightarrow R$. What algebraic structure is "abelian group with associative unital multiplication"? A ring. A bimodule between $R$ and $S$ is then a $1$-cell carrying commuting two-sided actions — an ordinary bimodule.

> [!note]- Hint 2
> Horizontal composition in $\mathrm{Mod}(\mathcal{K})$ is the balanced tensor: $M\otimes_S N$ is the coequalizer of the two maps $M\otimes S\otimes N\rightrightarrows M\otimes N$ given by the right action of $S$ on $M$ and the left action of $S$ on $N$. This is exactly the definition of $\otimes_S$.

> [!note]- Hint 3
> For associativity: $(M\otimes_S N)\otimes_T P$ and $M\otimes_S(N\otimes_T P)$ both compute the coequalizer of the four-fold object $M\otimes S\otimes N\otimes T\otimes P\rightrightarrows M\otimes N\otimes P$, balancing simultaneously over $S$ and $T$. For Morita: an equivalence in a bicategory means invertible $1$-cells; here, invertible bimodules ${}_SP_R, {}_RQ_S$ with $P\otimes_R Q\cong S$ and $Q\otimes_S P\cong R$.

---

# Solution

We identify $\mathrm{Mod}(\mathcal{K})$ concretely and extract Morita theory.

**Step 1: Monads are rings; bimodules are bimodules.**

> [!note]- Derivation
> In the delooped bicategory $\mathcal{K}$, an endo-$1$-cell on $\ast$ is an abelian group $R$, and $1$-cell composition is $\otimes_{\mathbb{Z}}$. A [[Def - Monad Monoid and Module in a Bicategory|monad]] structure on $R$ is $\mu : R\otimes_{\mathbb{Z}}R\Rightarrow R$ (a $\mathbb{Z}$-bilinear multiplication) and $\eta : \mathbb{Z}\Rightarrow R$ (a unit element), associative and unital — i.e. a [[Def - Ring|ring]]. A $(t', t)$-bimodule for monads $t = R$, $t' = S$ is a $1$-cell carrying commuting left $S$- and right $R$-actions: an ordinary $(S, R)$-bimodule. Module maps are bimodule homomorphisms.

**Step 2: Composition is $\otimes_S$; associativity is the balanced-coequalizer iso.**

> [!note]- Derivation
> By [[Thm - Monoids and Modules Form a Bicategory]], horizontal composition of an $(S,R)$-bimodule $M$ (a $1$-cell $R\to S$) with an $(R,T)$-bimodule... — fixing orientation, the composite of $1$-cells $T\xrightarrow{N}R\xrightarrow{M}S$ is $M\otimes_R N$, the coequalizer
> $$M\otimes_{\mathbb{Z}}R\otimes_{\mathbb{Z}}N\rightrightarrows M\otimes_{\mathbb{Z}}N\to M\otimes_R N,$$
> with the two parallel maps the right $R$-action on $M$ and the left $R$-action on $N$ — exactly the ordinary [[Def - Tensor Product of Modules|tensor over R]]. The identity $1$-cell on $R$ is $R$ as an $(R,R)$-bimodule, with unitor $R\otimes_R M\cong M$. For three composable bimodules, by Lemma 3 of the theorem both $(M\otimes_S N)\otimes_T P$ and $M\otimes_S(N\otimes_T P)$ are the simultaneous balanced coequalizer of $M\otimes S\otimes N\otimes T\otimes P\rightrightarrows M\otimes N\otimes P$; the canonical comparison iso between them is the associativity isomorphism $(M\otimes_S N)\otimes_T P\cong M\otimes_S(N\otimes_T P)$. These colimits exist and are preserved because $\mathbf{Ab}$ has reflexive coequalizers preserved by $\otimes$, so $\mathcal{K}$ is suitable.

**Step 3: Morita equivalence is equivalence of objects.**

> [!note]- Derivation
> In any [[Def - 2-Category and Bicategory|bicategory]], two objects are *equivalent* when there are $1$-cells between them composing to the identity $1$-cells up to invertible $2$-cells. In $\mathrm{Mod}(\mathcal{K})$ this means: rings $R, S$ are equivalent iff there exist bimodules ${}_SP_R$ and ${}_RQ_S$ with $P\otimes_R Q\cong S$ (as $(S,S)$-bimodules) and $Q\otimes_S P\cong R$ (as $(R,R)$-bimodules). Unwinding, such a $P$ is exactly a *progenerator*: finitely generated projective and a generator on one side, with $S\cong\mathrm{End}_R(P)$. This is precisely the classical criterion for **Morita equivalence** of $R$ and $S$, which is in turn equivalent to an equivalence $\mathbf{Mod}_R\simeq\mathbf{Mod}_S$ of module categories (tensoring with $P$ and $Q$). So Morita equivalence is *definitionally* equivalence of objects in $\mathrm{Mod}(\mathcal{K})$.

> [!note]- Complete formal solution
> Delooping $(\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z})$ gives a bicategory $\mathcal{K}$ whose endo-$1$-cells are abelian groups and whose $1$-cell composition is $\otimes_{\mathbb{Z}}$. A monad in $\mathcal{K}$ is an abelian group with associative unital multiplication, i.e. a [[Def - Ring|ring]] $R$; a bimodule between rings $R, S$ is an ordinary $(S,R)$-bimodule; module maps are bimodule homomorphisms. By [[Thm - Monoids and Modules Form a Bicategory]], $\mathrm{Mod}(\mathcal{K})$ has rings as objects, bimodules as $1$-cells, composition the balanced coequalizer $M\otimes_R N=\mathrm{coeq}(M\otimes R\otimes N\rightrightarrows M\otimes N)=\otimes_R$, identity $1$-cells $R$ (with unitor $R\otimes_R M\cong M$), and associator the canonical iso $(M\otimes_S N)\otimes_T P\cong M\otimes_S(N\otimes_T P)$ from both sides being the iterated balanced coequalizer; $\mathbf{Ab}$ is suitable. Equivalence of objects $R\simeq S$ in $\mathrm{Mod}(\mathcal{K})$ means invertible bimodules ${}_SP_R, {}_RQ_S$ with $P\otimes_R Q\cong S$, $Q\otimes_S P\cong R$, i.e. a progenerator $P$ with $S\cong\mathrm{End}_R(P)$ — the classical Morita criterion, equivalent to $\mathbf{Mod}_R\simeq\mathbf{Mod}_S$. Hence Morita equivalence is equivalence of objects in $\mathrm{Mod}(\mathcal{K})$. $\blacksquare$

---

# Key Takeaways

**Morita theory is bicategory theory wearing ring-theoretic clothes.** The headline insight is that "Morita-equivalent" is not a special ring-theoretic notion but the bare bicategorical notion of "equivalent objects", instantiated in $\mathrm{Mod}(\mathcal{K})$ for the ring base. The progenerator condition, the isomorphism $S\cong\mathrm{End}_R(P)$, and the equivalence of module categories are all *consequences* of "$P$ is an invertible $1$-cell in $\mathrm{Mod}(\mathcal{K})$". The transferable diagnostic: whenever a subject has a notion of "equivalence up to invertible correspondences" (Morita for rings, derived Morita for dg-algebras, Cauchy equivalence for categories), look for the bicategory $\mathrm{Mod}(\mathcal{K})$ in which it is just equivalence of objects, and inherit the general theory of bicategorical equivalences.

**The tensor $\otimes_S$ is the balanced coequalizer, and its associativity is the universal property — never a computation.** As in [[Ex - The fc-multicategory of rings bimodules and maps]], the load-bearing recognition is that $M\otimes_S N$ is the coequalizer balancing the two adjacent $S$-actions, so that the associativity $(M\otimes_S N)\otimes_T P\cong M\otimes_S(N\otimes_T P)$ is the canonical iso between two presentations of one iterated coequalizer (legal operation 7). This is why composition in $\mathrm{Mod}(\mathcal{K})$ associates *for free* and why the existence of $\mathrm{Mod}(\mathcal{K})$ rests entirely on the local-coequalizer hypothesis. The trigger to carry: "balanced/middle-linear" $\Rightarrow$ "coequalizer", and "coequalizer associativity" $\Rightarrow$ "same iterated colimit, hence canonical iso".

**One construction, run on different bases, is the factory for correspondence calculi.** This exercise is the ring instance of the $\mathrm{Mod}(\mathcal{K})$ factory; the span instance gives categories and profunctors, the $\mathcal{V}\text{-}\mathbf{Mat}$ instance gives enriched categories and enriched profunctors, and the homotopical instance gives algebras and bimodules with derived **Tor**. Recognising that all of these are the *same* theorem with the base bicategory changed is the unifying payoff of §3: you prove the bicategory structure once and inherit Morita theory, profunctor calculus, and derived bimodule theory simultaneously. This is exactly the "name the bicategory, then interpret" trigger of [[Ex - A monad in Span Set is a small category]] applied at the level of the whole $\mathrm{Mod}$ construction rather than a single monad.
