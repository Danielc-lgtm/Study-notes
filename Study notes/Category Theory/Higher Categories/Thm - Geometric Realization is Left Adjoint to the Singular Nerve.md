---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Simplicial Set"
  - "Def - Kan Complex and the Nerve"
  - "Def - Adjunction"
  - "Def - Singular Simplex"
  - "Def - Topological Space"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$ is the category of [[Def - Simplicial Set|simplicial sets]]; $\mathbf{Top}$ is a convenient category of topological spaces (compactly generated Hausdorff, so that it is cartesian closed and colimits behave). The **topological $n$-simplex** is
$$|\Delta^n| = \{(t_0, \dots, t_n) \in \mathbb{R}^{n+1} : t_i \ge 0,\ \textstyle\sum_i t_i = 1\},$$
the standard geometric simplex; an order-preserving $\theta : [m] \to [n]$ induces the affine map $|\Delta^m| \to |\Delta^n|$ summing barycentric coordinates over fibres. **Geometric realisation** is $|{-}| : \mathbf{sSet} \to \mathbf{Top}$ and the **singular nerve** (singular complex) is $\mathrm{Sing} : \mathbf{Top} \to \mathbf{sSet}$, $\mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|, Y)$ — the set of [[Def - Singular Simplex|singular $n$-simplices]] of $Y$. The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

---

# Statement

> **Theorem (Realisation $\dashv$ Singular nerve).** Geometric realisation is left [[Def - Adjunction|adjoint]] to the singular nerve,
> $$|{-}| \dashv \mathrm{Sing}, \qquad \mathbf{Top}(|X|, Y) \;\cong\; \mathbf{sSet}(X, \mathrm{Sing}(Y))$$
> naturally in $X \in \mathbf{sSet}$ and $Y \in \mathbf{Top}$, where
> $$|X| = \operatorname*{colim}_{\Delta^n \to X} |\Delta^n| \in \mathbf{Top}, \qquad \mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|, Y).$$

> **Corollary.** For every space $Y$, the simplicial set $\mathrm{Sing}(Y)$ is a [[Def - Kan Complex and the Nerve|Kan complex]] — the **fundamental ∞-groupoid** of $Y$. Hence Kan complexes are precisely the $\infty$-groupoids: the homotopy theory of spaces is the homotopy theory of Kan complexes (the combinatorial half of the **homotopy hypothesis**).

---

# Motivation

The two halves of the chapter — the combinatorial world of simplicial sets and the geometric world of spaces — would be of limited use if they could not be compared. This theorem is the comparison, and it is as tight as one could hope: a pair of [[Def - Adjunction|adjoint]] functors going back and forth. Geometric realisation glues the abstract simplices of a simplicial set into an actual topological space by replacing each formal $n$-simplex with the solid geometric simplex $|\Delta^n|$ and identifying along faces. The singular nerve goes the other way, probing a space by recording all continuous maps from geometric simplices into it. That these are adjoint says they are *optimally* matched: a continuous map out of the realisation $|X|$ is the same as a simplicial map into the probe $\mathrm{Sing}(Y)$, with no slack.

The adjunction is also the reason the construction is *forced* rather than arbitrary. There is a general principle — the theory of nerve-and-realisation, or left Kan extension along Yoneda — that says: pick any functor from $\Delta$ into a cocomplete category (here, the choice $[n] \mapsto |\Delta^n|$ of "what a geometric $n$-simplex is"), and you automatically get a colimit-preserving realisation with a right-adjoint singular functor. Geometric realisation is *the* example, but the [[Def - Kan Complex and the Nerve|nerve]] $N : \mathbf{Cat} \to \mathbf{sSet}$ is another instance of the same template (probe a category by the categorical simplices $[n]$), which is why the two constructions feel so similar. Recognising the template is the single most useful thing to carry away.

The corollary is where the abstract adjunction becomes a foundational fact. Because $\mathrm{Sing}(Y)$ is always a Kan complex — every horn fills — it is an $\infty$-groupoid, and it carries the entire homotopy type of $Y$: its [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] is the fundamental groupoid, its simplicial homotopy groups are the homotopy groups of $Y$. This is the precise sense in which "a space *is* an $\infty$-groupoid", the combinatorial form of the homotopy hypothesis, and it is what lets all of homotopy theory be done with simplicial sets.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's inputs are any simplicial set and any space, so the source question is *when a problem should be moved across the adjunction.*

The first disguised source is **a homotopy-theoretic question about a space**. If you want $\pi_n(Y)$, the homology of $Y$, or the homotopy type of $Y$, replace $Y$ by the Kan complex $\mathrm{Sing}(Y)$ and compute combinatorially. The non-obvious step is that $\mathrm{Sing}$ loses no homotopy-theoretic information — the unit $Y \to |\mathrm{Sing}(Y)|$ is a weak equivalence. *Example problem:* compute the [[Def - Path-Product and the Fundamental Group|fundamental group]] of $Y$ as automorphisms of a vertex in $\mathrm{ho}(\mathrm{Sing}\,Y)$.

The second disguised source is **a simplicial set you want to give a topological meaning**. If $X$ is a combinatorial model (a nerve, a classifying complex, a quotient of simplices), its realisation $|X|$ is the space it presents, and adjunction computes maps out of it. The non-obvious recognition is that $|{-}|$ preserves colimits (it is a left adjoint), so $|X|$ is built by the *same* gluing pattern as $X$. *Example problem:* show $|N(G)| = BG$, the classifying space, by realising the bar construction.

The third disguised source is **any "probe by test objects" construction**. The realisation/singular template applies to any cosimplicial object; recognising it lets you build adjunctions cheaply. The non-obviousness is that the *same* formula produces the [[Def - Kan Complex and the Nerve|nerve]] $\dashv$ fundamental-category adjunction by replacing $|\Delta^n|$ with the category $[n]$. *Example problem:* derive the nerve adjunction $\tau_1 \dashv N$ as an instance of the template.

**Targets (Output Amplification)**

Combine the adjunction with the **preservation properties of adjoints**. A left adjoint preserves colimits and a right adjoint preserves limits ([[Thm - Right Adjoints Preserve Limits|right adjoints preserve limits]]); so $|{-}|$ preserves colimits of simplicial sets (it sends a pushout of simplicial sets to a pushout of spaces) and $\mathrm{Sing}$ preserves limits. The further result is a powerful computational tool: the realisation of a cofibre sequence is a cofibre sequence, the singular complex of a product is the product of singular complexes. Non-obvious because it turns formal adjunction into concrete homotopy-theoretic identities.

Combine the corollary with the **Quillen equivalence**. $\mathrm{Sing}(Y)$ being a Kan complex, combined with the model structures on $\mathbf{sSet}$ and $\mathbf{Top}$, gives that $|{-}| \dashv \mathrm{Sing}$ is a **Quillen equivalence**: the two homotopy theories coincide. The further result is the foundational theorem that the homotopy category of spaces equals the homotopy category of simplicial sets — the formal backbone of the homotopy hypothesis. (See the Model Categories chapter for the Quillen-equivalence machinery.)

Combine $\mathrm{Sing}(Y)$ being Kan with the **homotopy category functor**. The result $\mathrm{ho}(\mathrm{Sing}\,Y)$ is the [[Def - Path-Product and the Fundamental Group|fundamental groupoid]] $\Pi_1(Y)$; combined with the higher horn-filling, the further result is the entire **fundamental ∞-groupoid** $\Pi_\infty(Y)$, recording all homotopy groups at once. Non-obvious because it packages the whole homotopy type in a single combinatorial object.

---

# Why Is It True

The adjunction is true for a structural reason that has nothing to do with topology specifically: it is **left Kan extension along the Yoneda embedding**. Here is the mechanism. The standard simplices $\Delta^n$ are the representable simplicial sets, and every simplicial set is canonically a colimit of them ($X = \mathrm{colim}_{\Delta^n \to X}\Delta^n$). A functor out of $\mathbf{sSet}$ that preserves colimits is therefore *determined* by what it does on the $\Delta^n$. We *declare* $|\Delta^n| := $ the geometric $n$-simplex, and extend by colimits: $|X| = \mathrm{colim}_{\Delta^n \to X}|\Delta^n|$. Any colimit-preserving functor between (co)complete categories has a right adjoint, given by the formula $\mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|, Y)$ — "probe $Y$ by the image of $\Delta^n$". The adjunction bijection then unwinds by writing $X$ as a colimit of representables and using that $|{-}|$ preserves it and that $\mathrm{Sing}$ is defined to make the representable case Yoneda:
$$\mathbf{Top}(|X|, Y) = \mathbf{Top}(\mathrm{colim}\,|\Delta^n|, Y) = \lim \mathbf{Top}(|\Delta^n|, Y) = \lim \mathrm{Sing}(Y)_n = \mathbf{sSet}(X, \mathrm{Sing}(Y)).$$
**The adjunction holds because realisation is the unique colimit-preserving extension of a chosen cosimplicial space, and its right adjoint is forced to be "probe by that cosimplicial space".**

Why is $\mathrm{Sing}(Y)$ a Kan complex? Because the geometric horn $|\Lambda^n_i|$ is a *retract* of the solid simplex $|\Delta^n|$ — there is a continuous retraction $r : |\Delta^n| \to |\Lambda^n_i|$ fixing the horn (push the missing face and interior onto the horn). A horn $\Lambda^n_i \to \mathrm{Sing}(Y)$ is, by adjunction, a continuous map $|\Lambda^n_i| \to Y$; precomposing with the retraction $r$ extends it to $|\Delta^n| \to Y$, which is a filler. This works for *every* $i$, inner and outer, because the retraction exists for every face — which is exactly why $\mathrm{Sing}(Y)$ fills all horns and is Kan, not merely a quasi-category. **The Kan property is the retraction $|\Lambda^n_i| \hookrightarrow |\Delta^n|$ pushed through the adjunction: a map out of a retract always extends.**

---

# What Makes This Hard

Two points trip people. First, the colimit defining $|X|$ is a colimit over the *category of simplices of $X$* (the comma category $\Delta \downarrow X$), not a naive union; getting the indexing right is where errors creep in, and the clean way is to invoke "left Kan extension along Yoneda" rather than to build the quotient space by hand. Second, the corollary requires the *geometric* fact that horns retract onto solid simplices, and the subtlety is that this retraction exists for **all** horns including the outer ones — which is precisely why $\mathrm{Sing}(Y)$ is Kan (an $\infty$-groupoid) rather than only a quasi-category. The common error is to prove only inner filling and conclude "quasi-category", missing that the same retraction handles outer horns and upgrades the conclusion to Kan.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Recognise $|{-}|$ as the colimit-preserving extension of $[n]\mapsto|\Delta^n|$; its right adjoint is forced to be $\mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|,Y)$, and the adjunction bijection follows from writing $X$ as a colimit of representables. For the corollary, exhibit the retraction of the geometric horn onto the solid simplex and extend horns by precomposition.

**Subgoal decomposition:**

1. **Realisation preserves colimits.** Show $|{-}|$ is a left adjoint by exhibiting it as a colimit of $|\Delta^n|$'s.
   - *Hint:* Every simplicial set is a colimit of representables; define $|{-}|$ to preserve that colimit.
   - *Why needed:* A colimit-preserving functor out of a presheaf category automatically has a right adjoint.

2. **Identify the right adjoint.** Show the right adjoint is $\mathrm{Sing}$.
   - *Hint:* The right adjoint must satisfy $\mathbf{sSet}(\Delta^n, \mathrm{Sing}\,Y) \cong \mathbf{Top}(|\Delta^n|, Y)$; by Yoneda the left side is $\mathrm{Sing}(Y)_n$.
   - *Why needed:* Pins down the formula $\mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|, Y)$.

3. **Adjunction bijection.** Verify $\mathbf{Top}(|X|, Y) \cong \mathbf{sSet}(X, \mathrm{Sing}\,Y)$ for all $X$.
   - *Hint:* Write $X = \mathrm{colim}\,\Delta^n$, use that $|{-}|$ preserves the colimit and $\mathbf{Top}(-, Y)$ turns it into a limit, matching $\mathrm{Sing}$.
   - *Why needed:* This is the theorem.

4. **$\mathrm{Sing}(Y)$ is Kan.** Show all horns fill.
   - *Hint:* The geometric horn $|\Lambda^n_i|$ is a retract of $|\Delta^n|$; a map out of a retract extends.
   - *Why needed:* The corollary — Kan complexes are $\infty$-groupoids.

---

# Lemma Decomposition

> [!note]- Lemma 1: Every simplicial set is a colimit of standard simplices
> **Statement:** For any $X \in \mathbf{sSet}$, $X \cong \operatorname*{colim}_{(\Delta^n \to X)} \Delta^n$, the colimit over the category of simplices of $X$.
>
> **Hint:** This is the co-Yoneda / density formula for [[Def - Presheaf|presheaves]]: every presheaf is canonically a colimit of representables.
>
> **Why needed:** It is what lets us *define* $|{-}|$ by its values on the $\Delta^n$ and extend by colimits.
>
> > [!note]- Full proof
> > The category of elements (simplices) of $X$ has objects the pairs $(n, \sigma)$ with $\sigma \in X_n$, equivalently maps $\Delta^n \to X$ (Yoneda). The tautological cocone from the $\Delta^n$ to $X$ is universal: any cocone $(\Delta^n \to Z)$ compatible with the structure maps factors uniquely through $X$, because a simplicial map is exactly a compatible family of simplices. Hence $X = \mathrm{colim}\,\Delta^n$.

> [!note]- Lemma 2: A colimit-preserving functor from a presheaf category has a right adjoint
> **Statement:** A functor $L : \mathbf{sSet} \to \mathbf{Top}$ that preserves all small colimits and is defined on representables by $\Delta^n \mapsto |\Delta^n|$ has a right adjoint $R$ with $R(Y)_n = \mathbf{Top}(|\Delta^n|, Y)$.
>
> **Hint:** This is the adjoint functor recognition for presheaf categories; the right adjoint's value at $Y$ is the presheaf $n \mapsto \mathbf{Top}(L\Delta^n, Y)$.
>
> **Why needed:** It produces $\mathrm{Sing}$ as the forced right adjoint of $|{-}|$.
>
> > [!note]- Full proof
> > Define $R(Y)_n := \mathbf{Top}(|\Delta^n|, Y)$, a simplicial set (functoriality in $[n]$ from precomposition with $|\theta|$). For representables, $\mathbf{sSet}(\Delta^n, R Y) \cong R(Y)_n = \mathbf{Top}(|\Delta^n|, Y) = \mathbf{Top}(L\Delta^n, Y)$ by Yoneda. For general $X = \mathrm{colim}\,\Delta^n$ (Lemma 1), since $L$ preserves colimits and $\mathbf{Top}(-, Y)$ sends colimits to limits, $\mathbf{Top}(LX, Y) = \lim \mathbf{Top}(L\Delta^n, Y) = \lim \mathbf{sSet}(\Delta^n, RY) = \mathbf{sSet}(X, RY)$. So $L \dashv R$.

> [!note]- Lemma 3: The geometric horn is a retract of the solid simplex
> **Statement:** For every $n \ge 1$ and $0 \le i \le n$, there is a continuous retraction $r : |\Delta^n| \to |\Lambda^n_i|$ with $r \circ \iota = \mathrm{id}$ for the inclusion $\iota : |\Lambda^n_i| \hookrightarrow |\Delta^n|$.
>
> **Hint:** Project radially from the barycentre of the missing $i$th face onto the union of the other faces.
>
> **Why needed:** A map out of a retract always extends, which is exactly horn-filling for $\mathrm{Sing}(Y)$.
>
> > [!note]- Full proof
> > Place the cone point at the barycentre $b_i$ of the omitted $i$th face. Radial projection away from $b_i$ pushes the interior and the omitted face onto the union $|\Lambda^n_i|$ of the remaining faces; this is a continuous retraction $r$ fixing $|\Lambda^n_i|$ pointwise. (Concretely, $|\Lambda^n_i|$ is a strong deformation retract of $|\Delta^n|$.) Hence $r \circ \iota = \mathrm{id}$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — setup.** Work in $\mathbf{Top}$ = compactly generated Hausdorff spaces, where colimits exist and $\mathbf{Top}(-, Y)$ behaves well. Define $|\Delta^n|$ as the standard geometric simplex and, for $\theta : [m] \to [n]$ in $\Delta$, $|\theta| : |\Delta^m| \to |\Delta^n|$ the affine map $|\theta|(t)_j = \sum_{\theta(k)=j} t_k$.
>
> **Step 1 — define realisation.** Set $|X| = \operatorname*{colim}_{(\Delta^n \to X)} |\Delta^n|$. By Lemma 1, $X = \mathrm{colim}\,\Delta^n$, and $|{-}|$ is by construction the colimit-preserving extension of $\Delta^n \mapsto |\Delta^n|$.
>
> **Step 2 — define the singular nerve and prove adjunction.** Set $\mathrm{Sing}(Y)_n = \mathbf{Top}(|\Delta^n|, Y)$ (the [[Def - Singular Simplex|singular simplices]]). By Lemma 2, $|{-}| \dashv \mathrm{Sing}$, i.e.
> $$\mathbf{Top}(|X|, Y) \cong \mathbf{sSet}(X, \mathrm{Sing}(Y))$$
> naturally in $X$ and $Y$.
>
> **Step 3 — $\mathrm{Sing}(Y)$ is Kan.** Let $\phi : \Lambda^n_i \to \mathrm{Sing}(Y)$ be any horn ($0 \le i \le n$). By adjunction (or directly, since $\mathrm{Sing}$ is defined by mapping in geometric simplices), $\phi$ corresponds to a continuous map $\hat\phi : |\Lambda^n_i| \to Y$. By Lemma 3 there is a retraction $r : |\Delta^n| \to |\Lambda^n_i|$; then $\hat\phi \circ r : |\Delta^n| \to Y$ is a continuous map restricting to $\hat\phi$ on the horn, i.e. a filler $\Delta^n \to \mathrm{Sing}(Y)$ extending $\phi$. This holds for every $i$, so *all* horns fill: $\mathrm{Sing}(Y)$ is a [[Def - Kan Complex and the Nerve|Kan complex]].
>
> **Conclusion.** $|{-}| \dashv \mathrm{Sing}$ and $\mathrm{Sing}(Y)$ is a Kan complex for every space $Y$ — the fundamental $\infty$-groupoid of $Y$. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Classifying spaces of groups.** Realising the [[Def - Kan Complex and the Nerve|nerve]] of a group $G$ (a one-object [[Def - Groupoid|groupoid]]) gives $|N(G)| = BG = K(G,1)$, the classifying space, whose homology is the group homology of $G$. The exercise: compute $|N(\mathbb{Z})| \simeq S^1$ and identify the cell structure. Non-obvious because a purely categorical construction (the nerve) realises to a space whose topology computes a purely algebraic invariant (group cohomology); the adjunction is the bridge.

**Simplicial approximation and CW structure.** Geometric realisation of a simplicial set is naturally a CW complex with one cell per non-degenerate simplex. The exercise: show $|\Delta^n / \partial\Delta^n| \cong S^n$ and read off the cell structure. Non-obvious because it connects the combinatorics of non-degenerate simplices directly to CW topology, and because the left-adjoint (colimit-preserving) property is exactly what makes the quotient on the simplicial side become the quotient on the space side.

**The unit and counit as homotopy equivalences.** The adjunction has unit $X \to \mathrm{Sing}|X|$ and counit $|\mathrm{Sing}\,Y| \to Y$; both are weak homotopy equivalences. The exercise: interpret the counit $|\mathrm{Sing}\,Y| \to Y$ as "$Y$ is built from its singular simplices" and show it induces isomorphisms on all homotopy groups. Non-obvious because it is the precise statement that no homotopy-theoretic information is lost in passing to simplicial sets — the technical core of the homotopy hypothesis.

---

# Bridges

- **[[Def - Kan Complex and the Nerve|The nerve]] $\dashv$ fundamental category** — the same template, categorical instead of topological. Replace the cosimplicial *space* $[n] \mapsto |\Delta^n|$ by the cosimplicial *category* $[n] \mapsto [n]$, and the realisation/singular adjunction becomes $\tau_1 \dashv N$, where $\tau_1 : \mathbf{sSet} \to \mathbf{Cat}$ is the fundamental-category functor and $N$ the nerve. So geometric realisation and the nerve are two faces of one construction — probe by simplices, glue by colimits.

- **[[Thm - Right Adjoints Preserve Limits|Right adjoints preserve limits]]** — supplies the computational power. Because $\mathrm{Sing}$ is a right adjoint it preserves limits ($\mathrm{Sing}(Y \times Z) = \mathrm{Sing}(Y)\times\mathrm{Sing}(Z)$), and because $|{-}|$ is a left adjoint it preserves colimits (realisation of a pushout is a pushout of spaces). These preservation facts are how the adjunction is used in practice.

- **[[Thm - The Homotopy Category of a Quasi-Category|The homotopy category]] and $\pi_1$** — the corollary's payoff. Since $\mathrm{Sing}(Y)$ is a Kan complex, its homotopy category $\mathrm{ho}(\mathrm{Sing}\,Y)$ is a [[Def - Groupoid|groupoid]], the [[Def - Path-Product and the Fundamental Group|fundamental groupoid]] $\Pi_1(Y)$; the automorphisms of a vertex are $\pi_1(Y)$. The full simplicial set $\mathrm{Sing}(Y)$ is the fundamental $\infty$-groupoid, recovering all $\pi_n(Y)$ as simplicial homotopy groups.

---

# Unlocked by This

> [!tip] The Homotopy Hypothesis *(from Foundations)*
> $\mathrm{Sing}$ and $|{-}|$ form a **Quillen equivalence** between simplicial sets and spaces, so $\infty$-groupoids (Kan complexes) and spaces are the same homotopy theory — **the homotopy hypothesis** in usable form. This is the assertion that **homotopy type theory** turns into a definition: a type is a space is an $\infty$-groupoid.

> [!tip] Simplicial Model of Spaces and ∞-Categories of Sheaves *(from Higher Topos Theory)*
> Because every space is modelled by a Kan complex, sheaves *of spaces* can be modelled by simplicial presheaves, and their $\infty$-categories are the **∞-topoi** where derived and nonabelian cohomology live. The realisation–singular adjunction is the first rung of that ladder.
