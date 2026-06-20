---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Cosimplicial and Simplicial Frame"
  - "Def - Simplicial Set"
  - "Def - Reedy Category and the Reedy Model Structure"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{M}$ be a **simplicial model category** — a model category tensored, cotensored, and enriched over [[Def - Simplicial Set|sSet]], with tensoring $X \otimes K$ and cotensoring $Y^K$ satisfying the pushout-product axiom (SM7): for a cofibration $i : A \to B$ in $\mathcal{M}$ and a cofibration $j : K \to L$ in $\mathbf{sSet}$, the pushout-product
$$A \otimes L \cup_{A \otimes K} B \otimes K \;\longrightarrow\; B \otimes L$$
is a cofibration, trivial if $i$ or $j$ is. Let $X$ be a cofibrant object.

(a) Show that $X^{\bullet} := X \otimes \Delta^{\bullet}$ (the cosimplicial object $[n] \mapsto X \otimes \Delta^n$, using the standard simplices) is **homotopically constant**.

(b) Show that $X \otimes \Delta^{\bullet}$ is **[[Def - Reedy Category and the Reedy Model Structure|Reedy cofibrant]]**, hence a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on $X$. (Hint: relate the latching map of $X\otimes\Delta^{\bullet}$ to a pushout-product with the boundary inclusion $\partial\Delta^n \hookrightarrow \Delta^n$.)

(c) Conclude that in a simplicial model category framings *recover* the strict structure: $\mathrm{map}(X, Y) \simeq \underline{\mathrm{Map}}(X, RY)$ for the built-in simplicial mapping object $\underline{\mathrm{Map}}$.

**Recall:**

A [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] is a Reedy-cofibrant cosimplicial object that is homotopically constant ($X^0 \simeq X$, all structure maps weak equivalences). The latching object $L_n X^{\bullet}$ is the colimit over the cofaces; for $X^{\bullet} = X\otimes\Delta^{\bullet}$ it relates to $X \otimes (\text{latching of } \Delta^{\bullet})$, and the latching object of $\Delta^{\bullet}$ in $\mathbf{sSet}$ at level $n$ is the boundary $\partial\Delta^n$.

A simplicial model category has an adjunction $\mathcal{M}(X\otimes K, Y) \cong \mathbf{sSet}(K, \underline{\mathrm{Map}}(X, Y)) \cong \mathcal{M}(X, Y^K)$.

---

# Convergent Strategy

**Problem class:** This is a "certify a frame" problem of the positive kind: a natural candidate genuinely *is* a frame, and the task is to verify both conditions cleanly using the ambient structure (here SM7). It contrasts with [[Ex - The constant cosimplicial object is rarely a frame]], where the naive candidate failed.

**Assumption pattern:** The asset is the strict simplicial enrichment with SM7. SM7 is precisely a *pushout-product* compatibility between $\mathcal{M}$-cofibrations and $\mathbf{sSet}$-cofibrations, and Reedy cofibrancy of $X\otimes\Delta^{\bullet}$ is a statement about latching maps, which *are* pushout-products with boundary inclusions. Recognizing that "Reedy cofibrancy of $X\otimes\Delta^{\bullet}$" reduces to "SM7 applied to $\partial\Delta^n \hookrightarrow \Delta^n$" is the unlock.

**Theorem routing:** The verification uses SM7 and the fact that $\Delta^{\bullet}$ is Reedy cofibrant in $\mathbf{sSet}$ (every simplicial set is, by [[Ex - Latching and matching objects for cosimplicial and simplicial objects]]); it feeds the compatibility clause of [[Thm - Framings Compute Homotopy Function Complexes]], that framings agree with the strict mapping object when $\mathcal{M}$ is simplicial.

**Key decision point:** The non-obvious move is to express the latching map of $X \otimes \Delta^{\bullet}$ as $\mathrm{id}_X \otimes (\partial\Delta^n \hookrightarrow \Delta^n)$ — more precisely as the pushout-product of $\varnothing \to X$ with $\partial\Delta^n \hookrightarrow \Delta^n$. The latching object of $X\otimes\Delta^{\bullet}$ is $X \otimes \partial\Delta^n$ because $\otimes$ is a left adjoint (preserves colimits) and the latching object of $\Delta^{\bullet}$ is $\partial\Delta^n$. Once this identification is made, SM7 finishes the proof in one line.

---

# Legal Operations Used

1. **Operation 2 from the topic page (compute a latching object).** We compute $L_n(X\otimes\Delta^{\bullet}) = X \otimes \partial\Delta^n$ using that $\otimes$ preserves colimits and the latching object of $\Delta^{\bullet}$ is the boundary.

2. **Operation 3 from the topic page (check Reedy cofibrancy).** We show each latching map is a cofibration by recognizing it as a pushout-product and applying SM7.

3. **Operation 6 from the topic page (compute the function complex as a corepresentable of a frame).** In (c), with $X\otimes\Delta^{\bullet}$ as the frame, the corepresentable $\mathcal{M}(X\otimes\Delta^{\bullet}, RY)$ is the strict mapping object by the tensor-hom adjunction.

---

# Hints

> [!note]- Hint 1
> Each $\Delta^n$ is contractible (the simplicial set $\Delta^n$ has the homotopy type of a point). Tensoring a fixed cofibrant $X$ with a weak equivalence of simplicial sets gives a weak equivalence (by SM7 / Ken Brown), so every coface and codegeneracy $X\otimes\Delta^m \to X\otimes\Delta^n$ is a weak equivalence — that is condition (2).

> [!note]- Hint 2
> Because $\otimes$ is a left adjoint, it preserves colimits; the latching object is a colimit, so $L_n(X\otimes\Delta^{\bullet}) = X \otimes L_n(\Delta^{\bullet}) = X \otimes \partial\Delta^n$ (the latching object of $\Delta^{\bullet}$ in $\mathbf{sSet}$ is the boundary $\partial\Delta^n$).

> [!note]- Hint 3
> The latching map $X \otimes \partial\Delta^n \to X \otimes \Delta^n$ is the pushout-product of the cofibration $\varnothing \to X$ (which holds since $X$ is cofibrant) with the cofibration $\partial\Delta^n \hookrightarrow \Delta^n$ — or directly, $\mathrm{id}_X \otimes (\partial\Delta^n\hookrightarrow\Delta^n)$. SM7 says this is a cofibration.

---

# Solution

The plan: Step 1 verifies homotopical constancy from contractibility of the $\Delta^n$; Step 2 identifies the latching object as $X\otimes\partial\Delta^n$ and applies SM7 to get Reedy cofibrancy; Step 3 reads off the agreement with the strict mapping object via the tensor-hom adjunction.

**Step 1: $X \otimes \Delta^{\bullet}$ is homotopically constant.**

> [!note]- Derivation
> For any map $\alpha : [m] \to [n]$ in $\Delta$, the induced map $\Delta^m \to \Delta^n$ of standard simplices is a weak equivalence in $\mathbf{sSet}$, because every $\Delta^k$ is contractible (it deformation-retracts to a vertex) and a map between contractible Kan-type objects inducing the identity on path components is a weak equivalence. Tensoring with the fixed cofibrant $X$: the functor $X \otimes (-) : \mathbf{sSet} \to \mathcal{M}$ is left Quillen (its right adjoint is $\underline{\mathrm{Map}}(X, -)$ and SM7 makes it Quillen), so by Ken Brown's lemma it preserves weak equivalences between cofibrant objects — and all simplicial sets are cofibrant. Hence $X\otimes\Delta^m \to X\otimes\Delta^n$ is a weak equivalence. In particular $(X\otimes\Delta^{\bullet})^0 = X\otimes\Delta^0 = X \simeq X$. So condition (2) holds.

**Step 2: $X \otimes \Delta^{\bullet}$ is Reedy cofibrant.**

> [!note]- Derivation
> The latching object of $X\otimes\Delta^{\bullet}$ at degree $n$ is, by definition, the colimit over the cofaces of the values $X\otimes\Delta^{n-1}$ (and lower). Since $X\otimes(-)$ is a left adjoint it commutes with this colimit:
> $$L_n(X\otimes\Delta^{\bullet}) = X \otimes L_n(\Delta^{\bullet}) = X \otimes \partial\Delta^n,$$
> where $L_n(\Delta^{\bullet}) = \partial\Delta^n$ is the latching object of the cosimplicial *simplicial set* $\Delta^{\bullet}$, namely the boundary (the union of the cofaces $\Delta^{n-1}\to\Delta^n$). The latching map is therefore
> $$X \otimes \partial\Delta^n \;\xrightarrow{\ \mathrm{id}_X \otimes \iota\ }\; X \otimes \Delta^n, \qquad \iota : \partial\Delta^n \hookrightarrow \Delta^n.$$
> This is the pushout-product of the cofibration $\varnothing \to X$ (a cofibration because $X$ is cofibrant) with the cofibration $\iota : \partial\Delta^n \hookrightarrow \Delta^n$ (a monomorphism, hence a cofibration in $\mathbf{sSet}$): indeed the pushout-product of $\varnothing\to X$ and $\iota$ is exactly $X\otimes\partial\Delta^n \to X\otimes\Delta^n$ (the term $\varnothing\otimes\Delta^n$ in the pushout-product is initial and drops out). By **SM7**, the pushout-product of two cofibrations is a cofibration. Hence each latching map is a cofibration, so $X\otimes\Delta^{\bullet}$ is Reedy cofibrant.
>
> With Steps 1 and 2, $X\otimes\Delta^{\bullet}$ satisfies both frame conditions: it is a **cosimplicial frame** on $X$. (Dually $Y^{\Delta^{\bullet}}$ is a simplicial frame on a fibrant $Y$, by the cotensor version of SM7.)

**Step 3: Framings recover the strict mapping object.**

> [!note]- Derivation
> Take the frame $X\otimes\Delta^{\bullet}$ and a fibrant replacement $RY$. The [[Def - Homotopy Function Complex|homotopy function complex]] is
> $$\mathrm{map}(X, Y)_n = \mathcal{M}\big((X\otimes\Delta^{\bullet})^n, RY\big) = \mathcal{M}(X\otimes\Delta^n, RY).$$
> By the tensor-hom adjunction of the simplicial enrichment,
> $$\mathcal{M}(X\otimes\Delta^n, RY) \cong \mathbf{sSet}\big(\Delta^n, \underline{\mathrm{Map}}(X, RY)\big) = \underline{\mathrm{Map}}(X, RY)_n,$$
> the last equality by the [[Def - Simplicial Set|Yoneda]] identification $\mathbf{sSet}(\Delta^n, K) = K_n$. These isomorphisms are compatible with faces and degeneracies, so
> $$\mathrm{map}(X, Y) \;\cong\; \underline{\mathrm{Map}}(X, RY).$$
> So the abstract homotopy function complex *is* the built-in simplicial mapping object (evaluated on the cofibrant $X$ and fibrant $RY$). Framings extend, rather than replace, simplicial enrichment: when the strict structure is present, the canonical frame $X\otimes\Delta^{\bullet}$ reproduces it.

> [!note]- Complete formal solution
> **(a)** Each $\Delta^k$ is contractible, so every structure map $\Delta^m\to\Delta^n$ is a weak equivalence; $X\otimes(-)$ is left Quillen, hence preserves weak equivalences between (always-cofibrant) simplicial sets by Ken Brown, so every structure map $X\otimes\Delta^m\to X\otimes\Delta^n$ is a weak equivalence and $(X\otimes\Delta^{\bullet})^0 = X$. Homotopical constancy holds.
>
> **(b)** Since $X\otimes(-)$ preserves colimits, $L_n(X\otimes\Delta^{\bullet}) = X\otimes\partial\Delta^n$ and the latching map is $\mathrm{id}_X\otimes(\partial\Delta^n\hookrightarrow\Delta^n)$, the pushout-product of $\varnothing\to X$ (cofibration, $X$ cofibrant) with $\partial\Delta^n\hookrightarrow\Delta^n$ (cofibration). By SM7 it is a cofibration. So $X\otimes\Delta^{\bullet}$ is Reedy cofibrant, hence a cosimplicial frame.
>
> **(c)** With this frame, $\mathrm{map}(X,Y)_n = \mathcal{M}(X\otimes\Delta^n, RY) \cong \mathbf{sSet}(\Delta^n, \underline{\mathrm{Map}}(X, RY)) = \underline{\mathrm{Map}}(X, RY)_n$, naturally in $[n]$, so $\mathrm{map}(X,Y) \cong \underline{\mathrm{Map}}(X, RY)$. Framings recover the strict mapping object. $\blacksquare$

---

# Key Takeaways

**SM7 is exactly the axiom that turns "tensor with simplices" into a frame, because Reedy cofibrancy is a pushout-product condition.** The pushout-product axiom looks like a technical compatibility, but it is precisely the statement needed here: the latching map of $X\otimes\Delta^{\bullet}$ *is* a pushout-product of an $\mathcal{M}$-cofibration with the boundary inclusion $\partial\Delta^n\hookrightarrow\Delta^n$, and SM7 is the assertion that such pushout-products are cofibrations. So the abstract demand "the canonical cosimplicial object is Reedy cofibrant" is the *same* statement as SM7 applied to boundary inclusions. The reusable recognition: whenever you see a latching map of an object tensored with $\Delta^{\bullet}$, rewrite it as a pushout-product with $\partial\Delta^n\hookrightarrow\Delta^n$ and the cofibrancy follows from the monoidal/SM7 axiom.

**Framings extend simplicial enrichment rather than competing with it — the canonical frame reproduces the built-in mapping object.** It would be a misunderstanding to think framings are only for non-simplicial model categories. When the strict structure exists, $X\otimes\Delta^{\bullet}$ is a frame and the abstract $\mathrm{map}(X,Y)$ equals the strict $\underline{\mathrm{Map}}(X, RY)$. This is the consistency check that makes framings trustworthy: the general theory specializes correctly to the case everyone already understands. The practical upshot is that in a simplicial model category you may compute homotopy function complexes with the built-in mapping object and know it is the right answer — frame-independence (from [[Thm - Framings Compute Homotopy Function Complexes]]) guarantees the strict computation agrees with any other frame's.

**$\otimes$ being a left adjoint is what lets latching objects be computed by tensoring with the boundary, and this is the general pattern.** The single computational fact that made Step 2 work is that $X\otimes(-)$ preserves colimits, so it carries the latching object of $\Delta^{\bullet}$ (the boundary) to the latching object of $X\otimes\Delta^{\bullet}$. This is an instance of a general principle: left adjoints commute with latching objects (which are colimits), and right adjoints commute with matching objects (which are limits). So whenever a frame or diagram is built by applying a left adjoint to a known cosimplicial object, its latching data is the image of the known latching data — no recomputation needed. This is the engine behind transporting frames along [[Def - Quillen Adjunction and Quillen Equivalence|left Quillen functors]], and it is why Quillen equivalences preserve frames and hence mapping spaces. Compare the failed naive candidate in [[Ex - The constant cosimplicial object is rarely a frame]], where no such adjoint structure rescues the constant object.
