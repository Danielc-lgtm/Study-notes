---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Kan Complex and the Nerve"
  - "Def - Quasi-Category"
  - "Def - Category"
  - "Def - Functor"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$N : \mathbf{Cat} \to \mathbf{sSet}$ is the [[Def - Kan Complex and the Nerve|nerve]] functor, $N(\mathcal{C})_n = \mathrm{Fun}([n], \mathcal{C})$. A simplicial set $X$ has the **unique inner horn-filling property** if for every $n \ge 2$ and every $0 < i < n$, each map $\Lambda^n_i \to X$ extends to $\Delta^n \to X$ *uniquely*. A [[Def - Functor|functor]] $F$ is **fully faithful** if it induces bijections $\mathbf{Cat}(\mathcal{C}, \mathcal{D}) \xrightarrow{\sim} \mathbf{sSet}(N\mathcal{C}, N\mathcal{D})$ on hom-sets (see [[Def - Full, Faithful, and Essentially Surjective Functor]]). The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

---

# Statement

> **Theorem (Nerve characterisation).** The [[Def - Kan Complex and the Nerve|nerve]] functor $N : \mathbf{Cat} \to \mathbf{sSet}$ is **fully faithful**, and a [[Def - Simplicial Set|simplicial set]] $X$ is isomorphic to the nerve $N(\mathcal{C})$ of some [[Def - Category|category]] $\mathcal{C}$ **if and only if** every inner horn in $X$ has a *unique* filler:
> $$X \cong N(\mathcal{C}) \text{ for some } \mathcal{C} \quad\Longleftrightarrow\quad \text{for all } 0 < i < n,\ \text{every } \Lambda^n_i \to X \text{ extends uniquely to } \Delta^n \to X.$$
> Consequently $N$ embeds $\mathbf{Cat}$ as the full subcategory of $\mathbf{sSet}$ on the simplicial sets with unique inner horn fillers.

> **Corollary (the conceptual content).** Relaxing "unique inner-horn filler" to "*some* inner-horn filler" enlarges $\mathbf{Cat}$ to the [[Def - Quasi-Category|quasi-categories]]. Hence ordinary categories *are* the $\infty$-categories in which composition is single-valued, and a general $\infty$-category is exactly the relaxation in which composition exists but is determined only up to coherent homotopy.

---

# Motivation

This is the theorem that makes the whole subject hang together. Up to this point we have two parallel worlds: ordinary [[Def - Category|categories]], where you compose by applying a function, and [[Def - Simplicial Set|simplicial sets]], where you "compose" by filling horns. The nerve $N$ bridges them, turning a category into a simplicial set whose simplices are strings of composable arrows. The natural question is: *how faithfully does the simplicial world see the categorical one, and which simplicial sets come from categories at all?* The theorem answers both with surgical precision. Full faithfulness says the bridge loses nothing — $\mathbf{Cat}$ sits inside $\mathbf{sSet}$ as a full subcategory, so a functor between categories is exactly a map between their nerves. And the characterisation pins down the image: nerves are precisely the simplicial sets with *unique* inner fillers.

The payoff is the one-line definition of an $\infty$-category. The [[Def - Quasi-Category|quasi-category]] axiom was "every inner horn has *some* filler". This theorem says ordinary categories are the case "every inner horn has a *unique* filler". So the entire passage from category theory to $\infty$-category theory is a single edit — delete the word "unique". That is the most important sentence in the chapter, and this theorem is what licenses it. It tells you exactly what is being given up (single-valued composition) and exactly what is being kept (the existence of composites, encoded combinatorially). Everything else in higher category theory is the study of the consequences of that one deletion.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem has two halves with different preconditions; the source question is *when you want to recognise a simplicial set as a category, or to compare categories via their nerves.*

The first disguised source is **a simplicial set defined combinatorially that you suspect is a category**. If you can show its inner horns fill uniquely, the theorem hands you a category whose nerve it is — converting combinatorial data into categorical data. The non-obvious step is that uniqueness is checkable dimension by dimension and reduces, in the end, to the $2$- and $3$-dimensional cases (unique $2$-fillers give composition, unique $3$-fillers give associativity). *Example problem:* given the simplicial set of "commutative squares" in some structure, show inner horns fill uniquely and identify the underlying category.

The second disguised source is **a question about functors phrased simplicially**. Because $N$ is fully faithful, any statement about maps of nerves is a statement about functors and vice versa. The non-obvious bridge is that natural transformations also transport: $N$ extends to a $2$-functor, and $2$-cells correspond. *Example problem:* prove two functors are equal by showing their nerves agree on $2$-simplices — which by full faithfulness suffices.

The third disguised source is **a quasi-category you want to compare to an ordinary category**. If a quasi-category happens to have unique inner fillers, it *is* a nerve, so the higher structure is illusory. The non-obvious recognition is that "uniqueness of fillers" is the exact test for "this $\infty$-category is really a $1$-category". *Example problem:* show that the [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] construction is the identity on nerves, because nerves already have unique composites.

**Targets (Output Amplification)**

Combine full faithfulness with **the closure of $\mathbf{Cat}$ under the embedding**. The conclusion is a full embedding $\mathbf{Cat} \hookrightarrow \mathbf{sSet}$; combined with the limits and colimits of $\mathbf{sSet}$, the further result is that categorical (co)limits can be computed simplicially and that $\mathbf{Cat}$ inherits structure from $\mathbf{sSet}$ — for instance the Joyal model structure on $\mathbf{sSet}$ restricts to one on (nerves of) categories. Non-obvious because it lets homotopical machinery act on plain categories.

Combine the characterisation with **the quasi-category axiom**. The conclusion is "unique fillers ⟺ category"; combined with "some fillers ⟺ quasi-category", the further result is the exact location of $\mathbf{Cat}$ inside $\infty\text{-}\mathbf{Cat}$ and a clean statement of what is gained by passing to $\infty$-categories. This is the conceptual target — it is *why* the theorem is the heart of the chapter.

Combine full faithfulness with **the recovery $\mathrm{ho}(N\mathcal{C}) \cong \mathcal{C}$**. The conclusion that $N$ is a full embedding, combined with the [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] functor, gives that $\mathrm{ho}$ is a retraction of $\mathbf{sSet}$ onto $\mathbf{Cat}$: $\mathrm{ho} \circ N \cong \mathrm{id}_{\mathbf{Cat}}$. Non-obvious because it shows the categorical shadow of an $\infty$-category is computed by the *same* horn data, just remembered up to homotopy.

---

# Why Is It True

Start with full faithfulness. A map of simplicial sets $N(\mathcal{C}) \to N(\mathcal{D})$ is determined by what it does on $0$- and $1$-simplices — objects and morphisms — because higher simplices are strings of composable arrows, and a simplicial map must respect faces, so it must send a string $A_0 \to \dots \to A_n$ to the string of images. Compatibility with the face map $d_1$ (which composes) forces the assignment on morphisms to respect composition; compatibility with degeneracies forces it to preserve identities. So a simplicial map $N\mathcal{C} \to N\mathcal{D}$ is *exactly* the data of a [[Def - Functor|functor]] $\mathcal{C} \to \mathcal{D}$ — no more, no less. **A map of nerves cannot do anything a functor could not do, and must do everything a functor does, because the simplices of a nerve are commutative diagrams and a simplicial map preserves them.**

Now the characterisation. The key observation is the translation from [[Def - Kan Complex and the Nerve]]: an inner horn $\Lambda^2_1 \to X$ is a composable pair $(f, g)$, and a filler is a triangle witnessing a composite. In a nerve, the filler is *unique* because the composite of two arrows in a category is a single arrow — there is exactly one $2$-simplex with the given two edges, namely $(f, g)$ with long edge $g \circ f$. Conversely, suppose $X$ has unique inner fillers. Then: unique $\Lambda^2_1$-fillers give a *single-valued, totally defined* composition on edges (existence is the filler, uniqueness is single-valuedness); unique $\Lambda^3_1$- and $\Lambda^3_2$-fillers force this composition to be *associative* (the two ways of composing three arrows must agree, because the relevant $3$-simplex is unique); degeneracies supply identities and the unit laws. So $X$ assembles into a category $\mathcal{C}$ with $\mathrm{ob}\,\mathcal{C} = X_0$, morphisms $X_1$, and composition read off the unique $2$-fillers — and one checks $X \cong N(\mathcal{C})$ by verifying that all higher simplices are forced (uniquely determined by their $1$-skeleton). **Uniqueness in dimension two is single-valued composition; uniqueness in dimension three is associativity; together they rebuild the category.**

The corollary is then immediate and is the whole point: drop uniqueness, and composition becomes multi-valued — composites still exist (existence of fillers) but are no longer determined, only determined up to the homotopy that the higher inner fillers provide. That is exactly a [[Def - Quasi-Category|quasi-category]].

---

# What Makes This Hard

The subtle direction is "unique inner fillers $\Rightarrow$ nerve", and the hard step is showing that *all* higher simplices are determined by the $1$-skeleton — not just that composition and associativity hold, but that there is no extra data in dimensions $\ge 3$. The non-obvious move is an induction: unique fillers in each dimension force the $n$-simplices to be exactly the strings of composable arrows, with nothing left over. The common error is to stop after building composition (dimension two) and associativity (dimension three) and assume the rest follows automatically; in fact one must verify that the unique-filler condition propagates all the way up, which is where the precise bookkeeping of the simplicial identities is needed. The other frequent slip is confusing *inner* with *all* horns — outer fillers are emphatically *not* required for a nerve, since a category need not be a groupoid.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
For full faithfulness, show a simplicial map of nerves is forced to be a functor by its action on $0$- and $1$-simplices together with face-compatibility. For the characterisation, translate unique $\Lambda^2_1$-fillers into single-valued composition, unique $\Lambda^3_\bullet$-fillers into associativity, and induct to show higher simplices are determined.

**Subgoal decomposition:**

1. **$N$ is faithful.** Show distinct functors have distinct nerves.
   - *Hint:* Functors differing on an object or morphism differ on the corresponding $0$- or $1$-simplex.
   - *Why needed:* Half of full faithfulness.

2. **$N$ is full.** Show every simplicial map $N\mathcal{C} \to N\mathcal{D}$ comes from a functor.
   - *Hint:* The map's values on $0$- and $1$-simplices define an object- and morphism-assignment; face-compatibility with $d_1$ forces it to preserve composition.
   - *Why needed:* The other half; together they give full faithfulness.

3. **Nerves have unique inner fillers.** Show $N(\mathcal{C})$ satisfies the unique inner horn condition.
   - *Hint:* A horn is a partial string of composable arrows; the missing simplices are forced by composing in $\mathcal{C}$, and uniqueness is single-valuedness of composition.
   - *Why needed:* The forward direction of the characterisation.

4. **Unique inner fillers rebuild a category.** From a simplicial set with unique inner fillers, construct $\mathcal{C}$ and show $X \cong N(\mathcal{C})$.
   - *Hint:* Objects $= X_0$, morphisms $= X_1$, composition from unique $\Lambda^2_1$-fillers; associativity from unique $\Lambda^3_\bullet$-fillers; induct for higher simplices.
   - *Why needed:* The converse direction; completes the characterisation.

---

# Lemma Decomposition

> [!note]- Lemma 1: A simplicial map of nerves is determined by its $1$-skeleton
> **Statement:** A map $\phi : N(\mathcal{C}) \to N(\mathcal{D})$ of simplicial sets is uniquely determined by its components $\phi_0 : X_0 \to Y_0$ and $\phi_1 : X_1 \to Y_1$, and these must define a [[Def - Functor|functor]].
>
> **Hint:** An $n$-simplex of $N(\mathcal{C})$ is a string of composable arrows, recoverable from its edges ($1$-faces); a simplicial map respects faces.
>
> **Why needed:** It is the mechanism of full faithfulness — the map cannot carry data beyond a functor.
>
> > [!note]- Full proof
> > An $n$-simplex $\sigma$ of $N(\mathcal{C})$ is a functor $[n] \to \mathcal{C}$, equivalently a string $A_0 \xrightarrow{f_1} \cdots \xrightarrow{f_n} A_n$; its edges are the $f_k$ and their composites. A simplicial map $\phi$ commutes with face maps, so $\phi(\sigma)$ has edges $\phi_1(f_k)$, hence is the string $\phi_0(A_0) \xrightarrow{\phi_1(f_1)} \cdots$. Thus $\phi(\sigma)$ is determined by $\phi_0, \phi_1$. Compatibility with $d_1 : N(\mathcal{C})_2 \to N(\mathcal{C})_1$ (composition) gives $\phi_1(g\circ f) = \phi_1(g)\circ\phi_1(f)$; compatibility with degeneracies gives $\phi_1(\mathrm{id}) = \mathrm{id}$. So $(\phi_0, \phi_1)$ is a functor, and conversely every functor yields such a $\phi$. Hence $\mathbf{Cat}(\mathcal{C},\mathcal{D}) \cong \mathbf{sSet}(N\mathcal{C}, N\mathcal{D})$.

> [!note]- Lemma 2: Unique $\Lambda^2_1$-fillers $=$ single-valued total composition
> **Statement:** A simplicial set $X$ has a unique filler for every inner $2$-horn $\Lambda^2_1 \to X$ if and only if every composable pair of edges has a unique "composite" edge realised by a unique $2$-simplex.
>
> **Hint:** $\Lambda^2_1$ is exactly a composable pair; the filler's long edge is the composite.
>
> **Why needed:** It gives the composition operation of the reconstructed category and its single-valuedness.
>
> > [!note]- Full proof
> > A map $\Lambda^2_1 \to X$ is a pair of edges $f : x \to y$, $g : y \to z$ (the two faces $d_2, d_0$ of the horn). A filler is a $2$-simplex $\sigma$ with $d_2\sigma = f$, $d_0\sigma = g$; its remaining face $d_1\sigma$ is an edge $x \to z$, the composite. Existence of a filler is existence of a composite; uniqueness of the filler is uniqueness of $\sigma$, hence of the composite edge and of the witnessing triangle. So the unique-$\Lambda^2_1$-filler condition is precisely: composition is everywhere defined and single-valued.

> [!note]- Lemma 3: Unique $\Lambda^3_1$-fillers $\Rightarrow$ associativity
> **Statement:** If $X$ has unique inner fillers, the composition from Lemma 2 is associative.
>
> **Hint:** Three composable edges give a $\Lambda^3_1$ (or $\Lambda^3_2$) horn; its unique filler forces $(h\circ g)\circ f = h\circ(g\circ f)$.
>
> **Why needed:** Associativity is the remaining category axiom needed to reconstruct $\mathcal{C}$.
>
> > [!note]- Full proof
> > Given $w \xrightarrow{f} x \xrightarrow{g} y \xrightarrow{h} z$, the two bracketings of the triple composite each arise as $d_1$ of a $2$-simplex obtained by filling $2$-horns (Lemma 2). Assembling these into an inner $3$-horn $\Lambda^3_1$ and filling it uniquely produces a $3$-simplex whose faces force the two bracketings to coincide: the long edge computed via $(h\circ g)\circ f$ and via $h\circ(g\circ f)$ are both $d$-faces of the unique filler, hence equal. So composition is associative. Identities and unit laws come from degeneracies. Induction on $n$ (each higher simplex is the unique filler of an inner horn built from lower ones) shows $X_n$ is exactly the strings of composable arrows, so $X \cong N(\mathcal{C})$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Part A — full faithfulness.** By Lemma 1, for any categories $\mathcal{C}, \mathcal{D}$ the map $N : \mathbf{Cat}(\mathcal{C}, \mathcal{D}) \to \mathbf{sSet}(N\mathcal{C}, N\mathcal{D})$ is a bijection: every simplicial map of nerves is induced by a unique functor. Hence $N$ is [[Def - Full, Faithful, and Essentially Surjective Functor|fully faithful]].
>
> **Part B — nerves have unique inner fillers ($\Rightarrow$).** Let $X = N(\mathcal{C})$. An inner horn $\Lambda^n_i \to X$ ($0 < i < n$) is a partial string of composable arrows missing the data across vertex $i$; the missing arrows and simplices are uniquely determined by composing in $\mathcal{C}$ (composition is single-valued), so there is exactly one extension to $\Delta^n \to X$. Thus inner horns fill uniquely.
>
> **Part C — unique inner fillers give a nerve ($\Leftarrow$).** Suppose $X$ has unique inner fillers. By Lemma 2, define a category $\mathcal{C}$ with $\mathrm{ob}\,\mathcal{C} = X_0$, $\mathcal{C}(x,y) = \{$edges $x \to y\}$, and composition the unique $\Lambda^2_1$-filler's long edge; identities are degenerate edges $s_0 x$. By Lemma 3, composition is associative and unital, so $\mathcal{C}$ is a category. The comparison map $X \to N(\mathcal{C})$ (identity on $0$- and $1$-simplices) is an isomorphism: by induction on dimension, unique fillers force each $X_n$ to equal the set of composable strings $N(\mathcal{C})_n$. Hence $X \cong N(\mathcal{C})$.
>
> **Conclusion.** $X \cong N(\mathcal{C})$ for some $\mathcal{C}$ iff $X$ has unique inner fillers, and $N$ is fully faithful, so $\mathbf{Cat}$ is the full subcategory of $\mathbf{sSet}$ on the unique-inner-filler simplicial sets. Relaxing "unique" to "exists" yields the [[Def - Quasi-Category|quasi-categories]]. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Posets and order complexes.** The nerve of a poset $P$ (a category with at most one arrow between objects) is its **order complex**: $n$-simplices are chains $p_0 \le \dots \le p_n$. Inner horns fill uniquely because composites in a poset are forced (there is at most one arrow), so the order complex is a nerve. The exercise: identify which simplicial sets are nerves of *posets* (answer: those that are nerves *and* have at most one edge between any two vertices). Non-obvious because it geometrises order theory and connects to combinatorial topology (the order complex computes the homology of $P$).

**Groups and classifying spaces.** A group $G$ is a one-object [[Def - Groupoid|groupoid]]; its nerve $N(G)$ has $N(G)_n = G^n$ (strings of $n$ group elements) with $d_1$ multiplying adjacent elements. Inner horns fill uniquely (composites are products), so $N(G)$ is a nerve; its geometric realisation is the classifying space $BG = K(G,1)$. The exercise: compute the face maps of $N(G)$ and recognise the bar construction. Non-obvious because the same unique-filler condition that defines categories produces the standard resolution computing group cohomology.

**Recognising a monoidal product simplicially.** Given a simplicial set built from "labelled composable processes", deciding whether it is a nerve (deterministic composition) or merely a quasi-category (composition up to homotopy) is exactly the unique-versus-some filler test. The exercise: for a simplicial set modelling a rewriting system, determine whether confluence (unique normal forms) corresponds to unique fillers. Non-obvious because it reframes a computer-science notion (confluence) as the nerve condition.

---

# Bridges

- **[[Def - Quasi-Category|Quasi-categories]]** — the immediate generalisation. This theorem says nerves are the unique-inner-filler simplicial sets; quasi-categories are the *some*-inner-filler ones. The single word deleted, "unique", is the entire conceptual distance from category theory to $\infty$-category theory, and this theorem is what measures it.

- **[[Thm - The Homotopy Category of a Quasi-Category|The homotopy category]]** — the partial inverse. The functor $\mathrm{ho} : \{\text{quasi-categories}\} \to \mathbf{Cat}$ satisfies $\mathrm{ho}(N\mathcal{C}) \cong \mathcal{C}$, so $\mathrm{ho} \circ N \cong \mathrm{id}$. Because $N$ is fully faithful (this theorem), $\mathbf{Cat}$ is a *reflective* (indeed coreflective in the relevant sense) full subcategory, and $\mathrm{ho}$ is the retraction that forgets the higher cells nerves never had.

- **[[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|Realisation and singular nerve]]** — the topological analogue. Both the nerve and the singular nerve are "probe by simplices" right adjoints (probe a category by the categorical simplices $[n]$, probe a space by the geometric simplices $|\Delta^n|$). The characterisation here — unique inner fillers detect categories — has a topological cousin: *all* horn fillers detect $\infty$-groupoids, i.e. spaces, which is why $\mathrm{Sing}(X)$ is a Kan complex.

---

# Unlocked by This

> [!tip] The Definition of an ∞-Category in One Edit *(from this chapter, §H.4)*
> This theorem licenses the slogan that opens $\infty$-category theory: an $\infty$-category is a category with "unique composite" relaxed to "a composite, up to coherent homotopy". Every subsequent definition — $\infty$-[[Def - Functor|functor]], $\infty$-limit, $\infty$-[[Def - Adjunction|adjunction]] — is the ordinary one with horn-filling standing in for composition.

> [!tip] Joyal Model Structure and the Equivalence of Models *(from Higher Category Theory)*
> Full faithfulness of $N$ embeds $\mathbf{Cat}$ into the **Joyal model structure** on $\mathbf{sSet}$, whose fibrant objects are the [[Def - Quasi-Category|quasi-categories]]; this is the backbone of the proof that quasi-categories, simplicial categories, complete Segal spaces, and relative categories all model the *same* homotopy theory of $\infty$-categories.
