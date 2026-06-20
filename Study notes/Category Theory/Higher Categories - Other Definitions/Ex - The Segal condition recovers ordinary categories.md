---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Segal Category and Complete Segal Space"
  - "Def - Kan Complex and the Nerve"
  - "Def - Category"
  - "Def - Simplicial Set"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $X$ be a **[[Def - Simplicial Set|simplicial set]]** (regarded as a discrete simplicial space). Show that the following are equivalent:

1. $X$ is the **[[Def - Kan Complex and the Nerve|nerve]]** $N\mathcal{C}$ of some ordinary **[[Def - Category|category]]** $\mathcal{C}$;
2. for every $n \ge 2$ the **Segal map** (spine inclusion)
$$
\xi_n : X_n \longrightarrow X_1 \times_{X_0} X_1 \times_{X_0} \cdots \times_{X_0} X_1 \qquad (n \text{ factors})
$$
is a *bijection*.

Conclude that the *strict* (bijective) Segal condition is exactly the categorical condition, so that the **[[Def - Segal Category and Complete Segal Space|Segal-space]]** definition — which weakens "bijection" to "weak equivalence" — is the honest homotopical generalisation of "being a category".

**Recall:**

![[Def - Kan Complex and the Nerve#The Definition]]

The **[[Def - Kan Complex and the Nerve|nerve]]** $N\mathcal{C}$ of a category has $N\mathcal{C}_n = \{$chains $x_0 \xrightarrow{f_1} x_1 \to \cdots \xrightarrow{f_n} x_n\}$, with face maps composing/deleting and degeneracies inserting identities.

The **Segal map** $\xi_n$ takes an $n$-simplex to its *spine*: the chain of its $n$ edges $0\to1, 1\to2, \dots, (n{-}1)\to n$, an element of the iterated fibre product $X_1 \times_{X_0} \cdots \times_{X_0} X_1$ of composable edges (the [[Def - Pullback and Pushout|pullback]] glues target of one edge to source of the next).

---

# Convergent Strategy

**Problem class:** This is an *characterise-the-image-of-a-functor* problem: identify exactly which simplicial sets are nerves, by an intrinsic condition. It is the strict prototype of the Segal-space story, and the routine is to show a bijective spine map lets you *reconstruct* the category from the simplicial set and then check the reconstruction is inverse to the nerve.

**Assumption pattern:** The bijective Segal condition for $n=2$ — $X_2 \cong X_1 \times_{X_0} X_1$ — is the key assumption: it says every composable pair of edges has a *unique* $2$-simplex, hence a *unique* composite (the long edge $d_1$ of that $2$-simplex). Uniqueness is what makes composition a *function*; the $n \ge 3$ conditions then force associativity and the simplicial identities to give unitality.

**Theorem routing:** The route is: define $\mathcal{C}$ to have objects $X_0$ and morphisms $X_1$, with composition $g \circ f := d_1(\xi_2^{-1}(g,f))$ — the long edge of the unique $2$-simplex on the spine $(f,g)$. Associativity is the $n=3$ condition: the two ways of bracketing a triple are both spines of the unique $3$-simplex, so they agree. Identities are the degeneracies $s_0 : X_0 \to X_1$, and the simplicial identities give the unit laws. Then $N\mathcal{C} \cong X$ and conversely a nerve has bijective Segal maps because a chain of $n$ arrows *is* an $n$-tuple of composable arrows.

**Key decision point:** The non-obvious step is recognising that the inverse $\xi_2^{-1}$ exists precisely because the Segal map is a *bijection* (not merely a surjection), and that *uniqueness* of the filler is what makes the composite well-defined as a single value. This is the exact point where the strict and weak Segal conditions diverge: weakening bijection to equivalence replaces "the composite" by "a contractible space of composites".

---

# Legal Operations Used

1. **Operation 1 from the topic page (read a Segal condition as composition).** We read $X_2 \cong X_1 \times_{X_0} X_1$ as "composable pairs have unique composites", which manufactures the composition operation of $\mathcal{C}$.

2. **Operation 2 from the topic page (Segal condition as the avatar of the nerve/inner-horn condition).** The bijective Segal condition is exactly the [[Def - Kan Complex and the Nerve|nerve]] characterisation by *unique* inner-horn fillers, viewed through spines.

3. **Operation 8 from the topic page (recover the low-dimensional case).** The exercise *is* the strict case of the Segal machinery, recovering ordinary categories — the discrete prototype.

---

# Hints

> [!note]- Hint 1
> A composition operation needs to take a composable pair to a single morphism. Where, in a simplicial set, does a composable pair live, and where does its candidate composite live? The Segal map $\xi_2$ connects them.

> [!note]- Hint 2
> If $\xi_2 : X_2 \to X_1 \times_{X_0} X_1$ is a bijection, every composable pair $(f,g)$ has a *unique* $2$-simplex $\sigma$ with spine $(f,g)$. Define the composite to be the remaining edge $d_1\sigma$. Uniqueness is what makes this a function.

> [!note]- Hint 3
> For associativity, look at $X_3$. The spine of a $3$-simplex is a chain of three composable edges; the bijectivity of $\xi_3$ says there is a unique $3$-simplex on it. Its various $2$-dimensional faces encode $(h\circ g)\circ f$ and $h\circ(g\circ f)$ — both faces of the *same* $3$-simplex, hence equal.

> [!note]- Hint 4
> For the converse, just compute: in $N\mathcal{C}$, an element of $N\mathcal{C}_n$ is a chain of $n$ arrows, and that *is* an $n$-tuple of composable arrows — so the spine map is tautologically a bijection.

---

# Solution

The proof is a reconstruction argument. Step 1 builds a category from a simplicial set with bijective Segal maps. Step 2 checks associativity and units. Step 3 shows the reconstruction is inverse to the nerve, and that nerves have bijective Segal maps.

**Step 1: bijective Segal maps reconstruct a composition.**

> [!note]- Derivation
> Suppose all $\xi_n$ are bijections. Define a category $\mathcal{C}$: objects $\mathrm{ob}\,\mathcal{C} = X_0$, morphisms $\mathcal{C}(x,y) = \{f \in X_1 : d_1 f = x,\ d_0 f = y\}$ (using $d_1 =$ source, $d_0 =$ target for edges), identities $\mathrm{id}_x = s_0 x$. For composition, given composable $f : x \to y$, $g : y \to z$, the pair $(g, f) \in X_1 \times_{X_0} X_1$; since $\xi_2$ is a bijection there is a *unique* $2$-simplex $\sigma \in X_2$ with $d_2\sigma = f$, $d_0\sigma = g$ (its spine is $(f,g)$). Define $g \circ f := d_1\sigma$, the remaining edge. Uniqueness of $\sigma$ makes $g \circ f$ a well-defined morphism $x \to z$.

**Step 2: associativity and unitality.**

> [!note]- Derivation
> *Associativity.* Take composable $f : x\to y$, $g : y\to z$, $h : z\to w$. Since $\xi_3$ is a bijection there is a unique $3$-simplex $\tau \in X_3$ whose spine is $(f,g,h)$. Its faces are $2$-simplices: $d_3\tau$ witnesses $g\circ f$, $d_0\tau$ witnesses $h\circ g$, and the simplicial identities force the long edge to be both $(h\circ g)\circ f$ and $h\circ(g\circ f)$ — they are computed from faces of the *same* $\tau$. Concretely, $d_1\tau$ is the $2$-simplex with spine $(g\circ f,\ h)$, giving $h\circ(g\circ f)$ as its long edge, while $d_2\tau$ is the $2$-simplex with spine $(f,\ h\circ g)$, giving $(h\circ g)\circ f$; both long edges equal $d_1 d_1 \tau$, so $(h\circ g)\circ f = h\circ(g\circ f)$.
>
> *Unitality.* The degeneracy $s_0 f \in X_2$ has spine $(\mathrm{id}_x, f)$ and long edge $f$ (by the simplicial identity $d_1 s_0 = \mathrm{id}$), so $f \circ \mathrm{id}_x = f$; similarly $s_1 f$ gives $\mathrm{id}_y \circ f = f$. Hence $\mathcal{C}$ is a category.

**Step 3: the reconstruction is inverse to the nerve.**

> [!note]- Derivation
> *$X \cong N\mathcal{C}$.* An $n$-simplex of $X$ is, by iterated bijectivity of the Segal maps, the same as its spine — a chain of $n$ composable edges — which is exactly an $n$-simplex of $N\mathcal{C}$. The bijections $\xi_n$ are natural in the simplicial structure, giving an isomorphism $X \cong N\mathcal{C}$.
>
> *Nerves have bijective Segal maps.* In $N\mathcal{C}$, $N\mathcal{C}_n$ is by definition the set of chains $x_0 \to \cdots \to x_n$, and the spine map sends such a chain to the tuple of its $n$ edges — which recovers the chain bijectively (the edges, glued at shared objects, *are* the chain). So $\xi_n$ is a bijection. This closes the equivalence (1) $\Leftrightarrow$ (2).

> [!note]- Complete formal solution
> **(2) $\Rightarrow$ (1).** Assume every $\xi_n$ is a bijection. Define $\mathcal{C}$ with objects $X_0$, morphisms $X_1$ (source $d_1$, target $d_0$), identities $s_0$, and composition $g\circ f := d_1\big(\xi_2^{-1}(f,g)\big)$. Associativity: the unique $3$-simplex on spine $(f,g,h)$ has two inner faces computing $(h\circ g)\circ f$ and $h\circ(g\circ f)$ with a common long edge, so they coincide. Units: $s_0 f$ and $s_1 f$ exhibit $f\circ\mathrm{id} = f = \mathrm{id}\circ f$. Thus $\mathcal{C}$ is a category. Naturality of $\xi$ gives $X \cong N\mathcal{C}$.
>
> **(1) $\Rightarrow$ (2).** If $X = N\mathcal{C}$, then $X_n$ is the set of $n$-chains and $\xi_n$ sends a chain to its sequence of edges, which is a bijection onto composable $n$-tuples. $\blacksquare$

---

# Key Takeaways

**Bijective Segal maps mean "the composite", weak-equivalence Segal maps mean "a contractible space of composites".** This is the precise hinge between ordinary category theory and its homotopical generalisation, and the most important single fact to carry away. The nerve characterisation says a simplicial set is a category exactly when each spine map is a *bijection* — there is a unique simplex on each spine, hence a unique composite. Replacing "bijection" by "weak equivalence" does not abolish composition; it makes the simplex on each spine unique only *up to a contractible space of choices*, which is exactly the homotopy-theoretic meaning of "the composite is essentially unique". The trigger is "a Segal/spine condition", and the reaction is "ask whether it is bijective (strict, a category) or a weak equivalence (homotopical, an $(\infty,1)$-category)" — that one question places the structure on the strict/weak axis.

**Composition is reconstructed, never assumed, in the geometric definitions.** Notice that nowhere did we *postulate* a composition operation; we *recovered* it from the unique filler of a spine. This is the defining move of the non-algebraic definitions: composition is a *property* of the diagram (existence-and-uniqueness of fillers), and the operation is extracted afterward. When you meet a geometric definition and want its composition, do not look for a chosen operation — look for the filler whose existence the condition guarantees, and read the composite off it. The same move recovers composition from inner-horn fillers in a [[Def - Quasi-Category|quasi-category]] and from the Segal equivalence in a Segal space.

**Associativity is a face of a single higher simplex, not a separate axiom.** The slick part of the proof is that $(h\circ g)\circ f$ and $h\circ(g\circ f)$ are both read off the *same* $3$-simplex, so their equality is automatic once that $3$-simplex is unique. This is the simplicial mechanism by which higher-dimensional data enforces lower-dimensional laws: associativity at level $1$ is witnessed at level $2$ and pinned down at level $3$. The same architecture, with "unique" relaxed to "contractible", is how a [[Def - Segal Category and Complete Segal Space|Segal space]] makes composition *coherently* associative — the associator is a path in the (now non-discrete) space of $3$-simplices, and the pentagon is a disk one level up. Recognising that "the coherence is a face of a higher cell" lets you predict where each coherence lives without writing it down by hand.
