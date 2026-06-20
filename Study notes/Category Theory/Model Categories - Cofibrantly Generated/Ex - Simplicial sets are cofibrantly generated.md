---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Cofibrantly Generated Model Category"
  - "Def - Relative Cell Complex"
  - "Def - Transfinite Composition and Smallness"
  - "Def - Simplicial Set"
  - "Def - Kan Complex and the Nerve"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that the Kan–Quillen model structure on $\mathbf{sSet}$ is [[Def - Cofibrantly Generated Model Category|cofibrantly generated]], with generating sets
$$I = \{\, \partial\Delta^n\hookrightarrow\Delta^n : n\geq 0 \,\}, \qquad J = \{\, \Lambda^n_k\hookrightarrow\Delta^n : n\geq 1,\ 0\leq k\leq n \,\},$$
the boundary inclusions and the horn inclusions. Specifically:

(a) Identify $I\text{-cof}$ and show it is the class of *all* monomorphisms of simplicial sets.

(b) Identify $J\text{-inj}$ and $J\text{-cof}$, naming them as the [[Def - Kan Complex and the Nerve|Kan fibrations]] and the anodyne maps (trivial cofibrations); explain why a Kan complex is exactly a fibrant object.

(c) Verify the smallness hypothesis, explaining why it is automatic in $\mathbf{sSet}$.

You may quote that the Kan–Quillen weak equivalences are the maps whose geometric realization is a weak homotopy equivalence.

**Recall:**

![[Def - Cofibrantly Generated Model Category#The Definition]]

The **standard $n$-simplex** $\Delta^n$ is the representable simplicial set $\mathrm{Hom}_\Delta(-, [n])$; its **boundary** $\partial\Delta^n$ is the union of the faces (all nondegenerate simplices of dimension $<n$); the **$k$-th horn** $\Lambda^n_k$ is $\partial\Delta^n$ with the $k$-th face removed. A [[Def - Kan Complex and the Nerve|Kan complex]] is a simplicial set in which every horn has a filler — i.e. $X\to *$ has the RLP against all horn inclusions.

---

# Convergent Strategy

**Problem class:** This is an exhibit-generators problem at its richest, the combinatorial counterpart to $\mathbf{Top}$. The distinctive feature is that here *every* monomorphism is a relative cell complex, so the cofibrations are exactly the monos, and smallness is automatic because $\mathbf{sSet}$ is a presheaf category.

**Assumption pattern:** The decisive inputs are (a) the skeletal filtration: every mono $A\hookrightarrow X$ is built by attaching nondegenerate simplices via boundary inclusions, so $I\text{-cell}$ already gives all monos; (b) the definition of Kan fibration as RLP against horns, making $J\text{-inj}$ immediate; (c) the fact that every object of a presheaf category is small, making the smallness check free.

**Theorem routing:** The route is: skeletal induction shows every mono is a relative $I$-cell complex, so $I\text{-cof} \supseteq$ monos, and conversely monos are closed under the operations and contain $I$, giving equality; Kan fibration $= J\text{-inj}$ by definition; the LLP-classes give the anodyne trivial cofibrations; smallness is automatic since finite simplicial sets (indeed all simplicial sets) are small in the presheaf category $\mathbf{sSet} = [\Delta^{op},\mathbf{Set}]$.

**Key decision point:** The non-obvious work is part (a): proving every monomorphism is a relative cell complex via the *skeletal filtration*. The choice is to attach the nondegenerate simplices of $X\setminus A$ dimension by dimension, each nondegenerate $n$-simplex contributing one pushout of $\partial\Delta^n\hookrightarrow\Delta^n$ (its boundary already present, its interior new). Recognizing that degenerate simplices need not be attached — they come for free from lower simplices — is the subtlety.

---

# Legal Operations Used

1. **Operation 1 from the topic page (form the closures of a set).** Both classes are read off as closures of $I$ and $J$: $I\text{-cof}$, $J\text{-inj}$, $J\text{-cof}$.

2. **Operation 9 from the topic page (reduce a lifting question to the generators).** Kan fibration is RLP against the *set* of horns $J$; fibrancy is RLP against $J$ with target the point.

3. **Operation 5 from the topic page (certify smallness — here by being a presheaf category).** Smallness is automatic: every object of $[\Delta^{op},\mathbf{Set}]$ is small, as in [[Ex - Every set is small in the category of sets]] applied levelwise.

---

# Hints

> [!note]- Hint 1 (part a, skeletal filtration)
> Given a mono $A\hookrightarrow X$, filter $X$ by skeleta: $A = X^{(-1)}\subseteq X^{(0)}\subseteq X^{(1)}\subseteq\cdots$ where $X^{(n)}$ adjoins the nondegenerate $n$-simplices of $X$ not in $A$. Each step $X^{(n-1)}\hookrightarrow X^{(n)}$ is a pushout of $\coprod\partial\Delta^n\hookrightarrow\coprod\Delta^n$, one summand per such nondegenerate simplex.

> [!note]- Hint 2 (part a, why a pushout)
> A nondegenerate $n$-simplex $\sigma$ of $X$ is a map $\Delta^n\to X$; its boundary $\partial\Delta^n\to X$ already lands in $X^{(n-1)}$ (faces have lower dimension). Attaching $\sigma$ is exactly pushing out $\partial\Delta^n\hookrightarrow\Delta^n$ along $\partial\Delta^n\to X^{(n-1)}$. Do all nondegenerate $n$-simplices at once via the coproduct.

> [!note]- Hint 3 (part a, equality)
> So every mono is in $I\text{-cell}\subseteq I\text{-cof}$. Conversely, $I\text{-cof}$ consists of monos: each generator $\partial\Delta^n\hookrightarrow\Delta^n$ is a mono, monos are closed under pushout/coproduct/transfinite composite/retract, so $I\text{-cof}\subseteq$ monos. Hence $I\text{-cof} =$ monos.

> [!note]- Hint 4 (part b)
> $J\text{-inj} =$ Kan fibrations by definition (RLP against horns). A simplicial set $X$ is fibrant iff $X\to *$ is a Kan fibration iff every horn $\Lambda^n_k\to X$ extends to $\Delta^n$ — i.e. $X$ is a Kan complex. $J\text{-cof} = \mathrm{LLP}(\text{Kan fibrations}) =$ anodyne maps $=$ trivial cofibrations.

> [!note]- Hint 5 (part c)
> $\mathbf{sSet} = [\Delta^{op},\mathbf{Set}]$ is a presheaf category. A simplicial set is a diagram of sets; its size is bounded by the cardinality of its simplices. By the levelwise version of [[Ex - Every set is small in the category of sets]], every simplicial set is small. So all generator domains ($\partial\Delta^n, \Lambda^n_k$ — finite) are small, automatically.

---

# Solution

The proof identifies the cofibrations as all monomorphisms via the skeletal filtration (Step 1–2), the fibrations as Kan fibrations and fibrant objects as Kan complexes (Step 3), and notes smallness is free in a presheaf category (Step 4), assembling to cofibrant generation (Step 5). The combinatorial heart is the skeletal filtration showing every mono is cellular.

**Step 1 (a): Every monomorphism is a relative $I$-cell complex (skeletal filtration).**

> [!note]- Derivation
> Let $f : A\hookrightarrow X$ be a monomorphism of simplicial sets. Define a filtration $A = X_{-1}\subseteq X_0\subseteq X_1\subseteq\cdots\subseteq X$ where $X_n$ is the sub-simplicial-set of $X$ generated by $A$ together with all simplices of $X$ of dimension $\leq n$. The union $\bigcup_n X_n = X$ (every simplex has some dimension), so $f$ is the transfinite (here $\omega$-indexed) composite of the inclusions $X_{n-1}\hookrightarrow X_n$.
>
> Each step attaches the *nondegenerate* $n$-simplices of $X$ not already in $X_{n-1}$ (equivalently, not in $A$ and not a face-iterate of lower simplices). Let $\Sigma_n$ be the set of these. Each $\sigma\in\Sigma_n$ is a map $\Delta^n\to X$ whose boundary $\partial\Delta^n\to X$ factors through $X_{n-1}$ (all faces of $\sigma$ have dimension $<n$, hence lie in $X_{n-1}$). Then
> $$\begin{array}{ccc} \coprod_{\sigma\in\Sigma_n}\partial\Delta^n & \to & X_{n-1} \\ \downarrow & & \downarrow \\ \coprod_{\sigma\in\Sigma_n}\Delta^n & \to & X_n \end{array}$$
> is a pushout: $X_n$ is $X_{n-1}$ with the interiors of the new nondegenerate $n$-simplices glued in along their (already-present) boundaries. Degenerate $n$-simplices need not be attached — they are images of lower-dimensional simplices under degeneracies, already present once their nondegenerate sources are.

**Step 2 (a): $I\text{-cof} =$ monomorphisms.**

> [!note]- Derivation
> By Step 1, every mono is a relative $I$-cell complex, so monos $\subseteq I\text{-cell}\subseteq I\text{-cof}$ (using [[Ex - Pushouts of coproducts of I lie in I-cof|saturation]]). Conversely, each generator $\partial\Delta^n\hookrightarrow\Delta^n$ is a monomorphism; monomorphisms of simplicial sets are closed under pushout, coproduct, transfinite composition, and retract (they are detected levelwise in $\mathbf{Set}$, where injections are so closed); hence $I\text{-cof} = \mathrm{LLP}(I\text{-inj})\subseteq$ monos. Therefore $I\text{-cof} =$ monomorphisms — every object of $\mathbf{sSet}$ is cofibrant.

**Step 3 (b): $J\text{-inj} =$ Kan fibrations, $J\text{-cof} =$ anodyne (trivial cofibrations), fibrant $=$ Kan complex.**

> [!note]- Derivation
> By definition a Kan fibration is a map with the RLP against all horn inclusions $\Lambda^n_k\hookrightarrow\Delta^n$, i.e. $J\text{-inj} =$ Kan fibrations. A simplicial set $X$ is fibrant iff $X\to *$ is a fibration iff $X\to *$ has the RLP against $J$ iff every horn $\Lambda^n_k\to X$ extends along $\Lambda^n_k\hookrightarrow\Delta^n$ to a map $\Delta^n\to X$ — which is exactly the horn-filling condition defining a [[Def - Kan Complex and the Nerve|Kan complex]]. So fibrant objects $=$ Kan complexes. The trivial cofibrations are $J\text{-cof} = \mathrm{LLP}(\text{Kan fibrations})$, classically the **anodyne** maps (Gabriel–Zisman): the saturation of the horn inclusions.

**Step 4 (c): Smallness is automatic.**

> [!note]- Derivation
> $\mathbf{sSet} = [\Delta^{op},\mathbf{Set}]$ is a presheaf category, where colimits are computed levelwise. A simplicial set $K$ has, in each degree, a set $K_n$ of $n$-simplices; its "size" is bounded by $\sup_n|K_n|$. By the levelwise application of [[Ex - Every set is small in the category of sets]] — every set is small, with threshold above its cardinality — $K$ is small relative to all maps, with threshold above $\sup_n|K_n|$. The generator domains $\partial\Delta^n$ and $\Lambda^n_k$ are *finite* simplicial sets (finitely many nondegenerate simplices), hence small with countable threshold. So both smallness hypotheses hold automatically.

**Step 5: $\mathbf{sSet}$ is cofibrantly generated.**

> [!note]- Derivation
> We have $I, J$ with small domains (Step 4), $\mathrm{cof} = I\text{-cof} =$ monos (Step 2), $\mathrm{fib} = J\text{-inj} =$ Kan fibrations and $\mathrm{triv\text{-}cof} = J\text{-cof} =$ anodyne (Step 3); the trivial fibrations are $I\text{-inj}$ (maps with RLP against all boundary inclusions, the acyclic Kan fibrations). This is the definition of a [[Def - Cofibrantly Generated Model Category|cofibrantly generated model category]]. Hence the Kan–Quillen model structure on $\mathbf{sSet}$ is cofibrantly generated.

> [!note]- Complete formal solution
> *Cofibrations.* Every mono $A\hookrightarrow X$ is a relative $I$-cell complex: filter $X$ by skeleta over $A$, and at stage $n$ attach the nondegenerate $n$-simplices of $X\setminus A$ via a pushout of $\coprod\partial\Delta^n\hookrightarrow\coprod\Delta^n$ (boundaries already present, interiors new); the transfinite composite is $f$. So monos $\subseteq I\text{-cof}$; conversely $I\text{-cof}\subseteq$ monos since generators are monos and monos are saturated. Thus $I\text{-cof} =$ monos.
>
> *Fibrations.* $J\text{-inj} =$ Kan fibrations by definition (RLP against horns); fibrant objects are Kan complexes (horn-filling against the point); $J\text{-cof} =$ anodyne $=$ trivial cofibrations.
>
> *Smallness.* $\mathbf{sSet}$ is a presheaf category, so every object is small (levelwise smallness of sets); finite simplicial sets $\partial\Delta^n, \Lambda^n_k$ are small with countable threshold.
>
> Hence $I, J$ have small domains and generate the four classes: $\mathbf{sSet}$ is cofibrantly generated. $\blacksquare$

---

# Key Takeaways

**The skeletal filtration realizes every monomorphism as a relative cell complex — this is why every simplicial set is cofibrant.** The combinatorial heart of the example is that a mono $A\hookrightarrow X$ is built by attaching the nondegenerate simplices of $X\setminus A$ one dimension at a time, each via a boundary inclusion $\partial\Delta^n\hookrightarrow\Delta^n$. This makes $I\text{-cell}$ contain all monos, so the cofibrations are *all* monomorphisms and every object is cofibrant — a feature that makes $\mathbf{sSet}$ dramatically easier to work with than $\mathbf{Top}$ (where cofibrancy is a real condition). The transferable insight is that in a presheaf category, the boundary inclusions of representables generate all monos via the canonical filtration by nondegenerate cells, a pattern that recurs for every Reedy and elegant presheaf category.

**Horn-filling is the lifting definition of fibrancy, so Kan complexes are fibrant objects by construction.** The fibrations are the Kan fibrations, *defined* as RLP against the horns $J$, and a simplicial set is fibrant exactly when it is a Kan complex — every horn fills. This is the simplicial analogue of "Serre fibration = homotopy lifting against disks," and it shows that the apparently ad hoc condition "every horn has a filler" is precisely the right-lifting condition defining fibrancy. Recognizing that the combinatorial filling conditions of simplicial homotopy theory are lifting properties against a generating set is what connects the hands-on theory of Kan complexes to the abstract model-categorical machinery.

**Presheaf categories make smallness free, which is why combinatorial models are the preferred setting.** Because $\mathbf{sSet} = [\Delta^{op},\mathbf{Set}]$ is a presheaf category, every object is small (levelwise, by the cardinality argument for sets), so the smallness hypothesis of the small object argument and the recognition theorem holds without any work — and the generator domains, being finite, are small with the smallest possible threshold. This automatic smallness is the deeper reason combinatorial (locally presentable) categories are the natural home for cofibrantly generated model structures, and it foreshadows the definition of a **combinatorial model category** and Jeff Smith's recognition theorem, where local presentability is assumed precisely to make smallness free. When choosing a category to do homotopy theory in, "is it a presheaf/locally presentable category?" is the question that decides whether the machinery runs for free.
