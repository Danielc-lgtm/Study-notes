---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Multicategory"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $k$ be a field. Define $\mathbf{Vect}_k^{\otimes}$ to have $k$-vector spaces as objects and, for a tuple $(V_1, \dots, V_n)$ and a space $W$, the set $\mathbf{Vect}_k^{\otimes}(V_1, \dots, V_n; W)$ of $k$-multilinear maps $V_1 \times \dots \times V_n \to W$. Prove that this is a symmetric [[Def - Multicategory|multicategory]]: specify the identities, the substitution composition, and the symmetric group action, and verify the associativity, unit, and equivariance axioms. Then prove that this multicategory is **representable** — there is, for each tuple, a universal object $V_1 \otimes \dots \otimes V_n$ — and explain why representability is exactly the universal property of the tensor product, so that $\mathbf{Vect}_k^{\otimes}$ "is" the [[Def - Monoidal Category|monoidal category]] $(\mathbf{Vect}_k, \otimes_k)$.

**Recall:**

A multimap in $\mathbf{Vect}_k^{\otimes}(V_1, \dots, V_n; W)$ is a function $f : V_1 \times \dots \times V_n \to W$ linear in each argument separately. A [[Def - Multicategory|multicategory]] is *representable* if for every tuple $(V_1, \dots, V_n)$ there is an object $T$ and a multimap $u \in \mathcal{M}(V_1, \dots, V_n; T)$ such that composing with $u$ gives a bijection $\mathcal{M}(T; W) \cong \mathcal{M}(V_1, \dots, V_n; W)$ for all $W$ — that is, $u$ is universal among multimaps out of the tuple. The tensor product $V_1 \otimes_k \dots \otimes_k V_n$ is, by definition, the vector space corepresenting multilinear maps: $\mathrm{Hom}_k(V_1 \otimes \dots \otimes V_n, W) \cong \{k\text{-multilinear } V_1 \times \dots \times V_n \to W\}$.

---

# Convergent Strategy

**Problem class:** This is a *structure-verification plus representability-recognition* problem. The first half checks that a concrete collection of operations satisfies the multicategory axioms; the second half recognises a universal property already in hand (the tensor product) as the statement that the multicategory is representable, hence monoidal.

**Assumption pattern:** The recognisable signal is "multilinear maps composing by substitution". Multilinear maps compose: substituting multilinear maps into the arguments of a multilinear map yields a multilinear map, because linearity in each slot is preserved under such substitution. This closure under substitution is exactly the multimap-composition the axioms govern. The second signal is the *defining universal property* of $\otimes$ stated as "multilinear maps out of a product = linear maps out of the tensor", which is verbatim the representability condition.

**Theorem routing:** The substitution composition is the composition of multilinear maps in $\mathbf{Vect}_k$; associativity and unitality are inherited from associativity and unitality of function composition. Representability routes through the universal property of the tensor product: the universal multimap is the canonical $V_1 \times \dots \times V_n \to V_1 \otimes \dots \otimes V_n$, and the bijection $\mathbf{Vect}_k^{\otimes}(V_1 \otimes \dots \otimes V_n; W) \cong \mathbf{Vect}_k^{\otimes}(V_1, \dots, V_n; W)$ is the tensor's defining adjunction.

**Key decision point:** The non-obvious step is the equivariance axiom: one must check that permuting the *arguments* of a multilinear map interacts correctly with substitution. The natural alternative — to ignore the $S_n$-action because "it's obviously fine" — hides the real content: a symmetric multilinear form is a *fixed point* of the action, and equivariance is what makes "symmetric" a meaningful operadic condition. The decision is to take the symmetric structure seriously and verify the block-permutation compatibility.

---

# Legal Operations Used

1. **Compose operations by substitution (operation 1 from the topic page).** We substitute multilinear maps into the slots of a multilinear map; the result is multilinear because each slot's linearity survives precomposition with multilinear maps that are themselves linear in their own slots.

2. **Recognise a universal property as representability (operation 6 from the topic page).** We identify the universal multimap $V_1 \times \dots \times V_n \to V_1 \otimes \dots \otimes V_n$ as the representing object, turning the tensor's universal property into the representability of the multicategory.

3. **Track the symmetric action through composition (operation 5 from the topic page).** We verify equivariance by computing the effect of permuting arguments before and after substitution.

---

# Hints

> [!note]- Hint 1
> To see substitution is well-defined, take $f : W_1 \times \dots \times W_k \to U$ multilinear and $g_i : V_{i,1} \times \dots \times V_{i,n_i} \to W_i$ multilinear; the composite $(v_{1,1}, \dots, v_{k,n_k}) \mapsto f(g_1(v_{1,\bullet}), \dots, g_k(v_{k,\bullet}))$ is linear in each $v_{i,j}$ because $g_i$ is linear in $v_{i,j}$ and $f$ is linear in its $i$th slot.

> [!note]- Hint 2
> The identity multimap $1_V \in \mathbf{Vect}_k^{\otimes}(V; V)$ is the identity *linear* map. The unit laws are then immediate: substituting identities changes nothing.

> [!note]- Hint 3
> Representability for the tuple $(V_1, \dots, V_n)$ means: there is a space $T$ and a multilinear $u : V_1 \times \dots \times V_n \to T$ such that every multilinear $f : V_1 \times \dots \times V_n \to W$ factors uniquely as $f = \bar f \circ u$ for a *linear* $\bar f : T \to W$. That is the universal property of $T = V_1 \otimes \dots \otimes V_n$.

> [!note]- Hint 4
> A multicategory is monoidal iff it is representable: the tensor of objects is the representing object of the pair, and the coherence isomorphisms (associator, unitors) come from uniqueness of representing objects. Cite this to conclude $\mathbf{Vect}_k^{\otimes} \cong (\mathbf{Vect}_k, \otimes_k)$.

---

# Solution

The plan: verify the multicategory axioms by inheriting them from function composition and from multilinearity (Steps 1–3), then identify the representing objects as tensor products and invoke the representable-multicategory = monoidal-category correspondence (Steps 4–5).

**Step 1: Substitution is well-defined and lands in multilinear maps.**

> [!note]- Derivation
> Given $f \in \mathbf{Vect}_k^{\otimes}(W_1, \dots, W_k; U)$ and $g_i \in \mathbf{Vect}_k^{\otimes}(V_{i,1}, \dots, V_{i,n_i}; W_i)$, define
> $$f \circ (g_1, \dots, g_k)(v_{1,1}, \dots, v_{k, n_k}) = f\big(g_1(v_{1,1}, \dots, v_{1,n_1}), \dots, g_k(v_{k,1}, \dots, v_{k,n_k})\big).$$
> Fix all variables except $v_{i,j}$. As $v_{i,j}$ varies, only $g_i$'s $j$th argument varies, so $g_i(v_{i,\bullet})$ varies $k$-linearly... more precisely linearly (the other arguments fixed), and $f$ is linear in its $i$th slot, so the composite is linear in $v_{i,j}$. As this holds for every $(i,j)$, the composite is multilinear of arity $n_1 + \dots + n_k$.

**Step 2: Identities and the unit axiom.**

> [!note]- Derivation
> Let $1_V \in \mathbf{Vect}_k^{\otimes}(V;V)$ be the identity linear map. Then $f \circ (1_{V_1}, \dots, 1_{V_n}) = f$ since each $1_{V_i}$ passes its argument through, and $1_W \circ (f) = f$ since the identity post-composed changes nothing. These are the multicategory unit laws.

**Step 3: Associativity and equivariance.**

> [!note]- Derivation
> *Associativity.* For a three-layer composite, both grafting orders evaluate to the same nested function application $f(g_1(h_{1,\bullet}), \dots)$, because composition of (multilinear) functions is associative as function composition. Hence $f \circ (g_i \circ (h_{i,\bullet})) = (f \circ (g_\bullet)) \circ (h_{\bullet})$.
>
> *Equivariance.* For $\sigma \in S_n$, define $(f \cdot \sigma)(v_1, \dots, v_n) = f(v_{\sigma(1)}, \dots, v_{\sigma(n)})$; this is again multilinear and gives a right $S_n$-action. To check compatibility with substitution: permuting the $k$ blocks of a composite by $\sigma \in S_k$ and permuting the inputs of the composite by the induced block permutation $\sigma\langle n_1, \dots, n_k\rangle$ both amount to relabelling the same arguments in the same way, so $f \cdot \sigma$ substituted equals the substitution with blocks permuted, reindexed by $\sigma\langle n_\bullet\rangle$. Likewise permuting within block $i$ by $\tau_i \in S_{n_i}$ matches permuting $g_i$'s arguments. Both are equalities of multilinear functions because they reorder the *same* evaluation. Hence equivariance holds, and $\mathbf{Vect}_k^{\otimes}$ is a symmetric multicategory.

**Step 4: The representing object is the tensor product.**

> [!note]- Derivation
> Fix $(V_1, \dots, V_n)$. Let $T = V_1 \otimes_k \dots \otimes_k V_n$ and let $u : V_1 \times \dots \times V_n \to T$ be the canonical multilinear map $(v_1, \dots, v_n) \mapsto v_1 \otimes \dots \otimes v_n$. By the defining universal property of the tensor product, every multilinear $f : V_1 \times \dots \times V_n \to W$ factors uniquely as $f = \bar f \circ u$ with $\bar f : T \to W$ linear. In multicategory language, composition with $u$ is a bijection
> $$\mathbf{Vect}_k^{\otimes}(T; W) = \mathrm{Hom}_k(T, W) \;\xrightarrow{\ \cong\ }\; \mathbf{Vect}_k^{\otimes}(V_1, \dots, V_n; W), \qquad \bar f \mapsto \bar f \circ u.$$
> So $u$ is universal, and $T$ represents the tuple. As this holds for every tuple, $\mathbf{Vect}_k^{\otimes}$ is representable.

**Step 5: Representable multicategory = monoidal category.**

> [!note]- Derivation
> A representable multicategory is the same data as a [[Def - Monoidal Category|monoidal category]]: the binary tensor $V_1 \otimes V_2$ is the representing object of the pair, the unit is the representing object of the empty tuple ($k$ itself, since multilinear maps of arity $0$ from nothing to $W$ are elements of $W$, corepresented by $k$), and the associator and unitors are the unique isomorphisms between representing objects of the same tuple regrouped (e.g. $(V_1 \otimes V_2) \otimes V_3$ and $V_1 \otimes (V_2 \otimes V_3)$ both represent $(V_1, V_2, V_3)$, hence are canonically isomorphic). The pentagon and triangle follow from uniqueness of representing objects. The resulting monoidal category is exactly $(\mathbf{Vect}_k, \otimes_k, k)$, and the symmetric structure (the $S_n$-action) becomes its symmetric braiding. Hence $\mathbf{Vect}_k^{\otimes}$ "is" the symmetric monoidal category of vector spaces.

> [!note]- Complete formal solution
> Define $\mathbf{Vect}_k^{\otimes}$ as in the statement. Substitution of multilinear maps yields a multilinear map (linearity in each slot survives because each inner map is linear in its slot and the outer is linear in the corresponding block slot); identities are identity linear maps; associativity is associativity of function composition; the $S_n$-action $(f\cdot\sigma)(v_\bullet)=f(v_{\sigma(\bullet)})$ is equivariant with substitution by inspection of which arguments are relabelled. Hence $\mathbf{Vect}_k^{\otimes}$ is a symmetric multicategory.
>
> For representability, the canonical map $u : V_1 \times \dots \times V_n \to V_1 \otimes \dots \otimes V_n$ is universal by the tensor product's defining property: $\mathrm{Hom}_k(V_1 \otimes \dots \otimes V_n, W) \cong \{$multilinear $V_1 \times \dots \times V_n \to W\}$. So every tuple has a representing object, and $\mathbf{Vect}_k^{\otimes}$ is representable. A representable symmetric multicategory is precisely a symmetric monoidal category, with tensor = representing object of pairs, unit = representing object of the empty tuple, and coherence isomorphisms = canonical isomorphisms between representing objects of regrouped tuples. The result is $(\mathbf{Vect}_k, \otimes_k, k)$. $\blacksquare$

---

# Key Takeaways

**The tensor product is the universal property that makes multilinear into linear, and that is precisely representability.** The single most useful thing to extract is the identity "representable multicategory = monoidal category". The tensor product was *invented* to convert multilinear maps into linear maps, and the multicategory viewpoint names exactly what that conversion is: the existence of a representing object for each tuple. Whenever you have a notion of "multi-input map" in some category — multilinear, bi-additive, multi-derivation, $n$-cocycle — ask whether a representing object exists; if it does, you have a monoidal structure, and if it does not, you genuinely need the multicategory to hold the multi-input maps that no single object can represent. This is the trigger: *multi-input maps present, looking for a tensor product* should make you check representability.

**Substitution closure is the multilinear chain rule.** The verification that multilinear maps compose to multilinear maps is the algebraic shadow of the fact that nesting linear-in-each-slot operations preserves linearity in each slot — a "multilinear chain rule". This pattern recurs whenever a class of maps defined by a per-argument condition (linear in each, continuous in each, polynomial in each, smooth in each) is closed under substitution; the proof is always the same fix-all-but-one argument. Recognising this lets you build a multicategory out of *any* such class without re-deriving the axioms each time — they are inherited from substitution of functions.

**The symmetric action is where "symmetric/commutative" comes from.** It is tempting to dismiss the $S_n$-action as bookkeeping, but it is the carrier of every commutativity phenomenon downstream. A symmetric bilinear form is a fixed point of the $S_2$-action; the [[Def - Operad|commutative operad]]'s defining feature is that its $S_n$-action is trivial in a way that forces the algebra's product to be commutative. Here, taking the action seriously is what licenses speaking of symmetric versus general multilinear maps, and it is the seed of the distinction between $\mathrm{Comm}$- and $\mathrm{Assoc}$-algebras in the operad chapter. The general lesson: when a structure has interchangeable inputs, the symmetric-group action is not optional decoration — it is the precise record of which symmetries the structure respects.
