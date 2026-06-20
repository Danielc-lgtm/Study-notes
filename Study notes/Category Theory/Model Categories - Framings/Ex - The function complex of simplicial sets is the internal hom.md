---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Homotopy Function Complex"
  - "Def - Simplicial Set"
  - "Def - Cosimplicial and Simplicial Frame"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Work in $\mathcal{M} = \mathbf{sSet}$ with the Kan–Quillen model structure (cofibrations = monomorphisms, fibrant objects = [[Def - Kan Complex and the Nerve|Kan complexes]], weak equivalences = maps with weak-homotopy-equivalent realizations). Let $X$ be any simplicial set and $Y$ a Kan complex.

(a) Show that $X \times \Delta^{\bullet}$ — the cosimplicial simplicial set $[n] \mapsto X\times\Delta^n$ — is a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on $X$. (Use that every simplicial set is Reedy cofibrant and that $\mathbf{sSet}$ is a simplicial/cartesian-closed model category.)

(b) Identify the resulting [[Def - Homotopy Function Complex|homotopy function complex]] with the **internal hom** (mapping simplicial set)
$$\mathrm{map}(X, Y) \;\cong\; Y^X, \qquad (Y^X)_n = \mathbf{sSet}(X\times\Delta^n, Y).$$

(c) Deduce that $Y^X$ is a Kan complex and that $\pi_0(Y^X) = [X, Y]$, the homotopy classes of maps of simplicial sets.

**Recall:**

$\mathbf{sSet}$ is **cartesian closed**: there is an internal hom $Y^X$ with $\mathbf{sSet}(W\times X, Y) \cong \mathbf{sSet}(W, Y^X)$ naturally, and $(Y^X)_n = \mathbf{sSet}(\Delta^n, Y^X) = \mathbf{sSet}(\Delta^n\times X, Y)$.

![[Def - Cosimplicial and Simplicial Frame#The Definition]]

By [[Ex - Latching and matching objects for cosimplicial and simplicial objects]], every simplicial set is Reedy cofibrant (its latching map, the inclusion of degenerate simplices, is a monomorphism).

A Kan complex is fibrant in $\mathbf{sSet}$; $[X, Y] = \mathrm{Ho}(\mathbf{sSet})(X, Y)$ for $X$ cofibrant (automatic) and $Y$ fibrant.

---

# Convergent Strategy

**Problem class:** This is a "compute the function complex via a convenient frame" problem (Legal Operation 6): in $\mathbf{sSet}$ the cartesian product with $\Delta^{\bullet}$ is the obvious frame, and the corepresentable applied to it is the internal hom. It is the simplicial-set instance of the general "framings recover the strict structure" result of [[Ex - In a simplicial model category the tensor with simplices is a frame]].

**Assumption pattern:** The assets are that $\mathbf{sSet}$ is cartesian closed (so $X\times(-)$ has a right adjoint $(-)^X$) and that every simplicial set is Reedy cofibrant (so the frame condition is nearly automatic). The product $\times$ is the tensoring of $\mathbf{sSet}$ over itself, so $X\times\Delta^{\bullet}$ is the canonical frame and the tensor-hom adjunction is the internal-hom adjunction.

**Theorem routing:** This routes through [[Ex - In a simplicial model category the tensor with simplices is a frame]] (the general statement, with $\otimes = \times$) and the compatibility clause of [[Thm - Framings Compute Homotopy Function Complexes]]; the Kan-complex conclusion is the general fact that the function complex of a cofibrant source and fibrant target is Kan.

**Key decision point:** The non-obvious recognition is that the *self*-enrichment of $\mathbf{sSet}$ — cartesian closure — *is* a simplicial model structure with tensoring $= \times$. Once you see $X\times\Delta^{\bullet}$ as "$X\otimes\Delta^{\bullet}$" for this enrichment, the entire computation is the adjunction $\mathbf{sSet}(X\times\Delta^n, Y) = (Y^X)_n$. The decision is to use cartesian closure as the enrichment rather than constructing a frame from scratch.

---

# Legal Operations Used

1. **Operation 6 from the topic page (function complex as corepresentable of a frame).** We form $\mathrm{map}(X,Y)_n = \mathbf{sSet}(X\times\Delta^n, Y)$ and recognize it as $(Y^X)_n$.

2. **Operation 3 from the topic page (Reedy cofibrancy).** We use that every simplicial set, in particular $X\times\Delta^{\bullet}$ levelwise, is Reedy cofibrant.

3. **Operation 5 ((co)fibrantly replace).** $X$ is automatically cofibrant; we need $Y$ fibrant (a Kan complex), which is the hypothesis.

---

# Hints

> [!note]- Hint 1
> The cartesian product makes $\mathbf{sSet}$ a simplicial model category enriched over itself, with tensoring $X\otimes K = X\times K$ and cotensoring $Y^K$ the internal hom. So $X\times\Delta^{\bullet}$ is the canonical frame "$X\otimes\Delta^{\bullet}$" of [[Ex - In a simplicial model category the tensor with simplices is a frame]].

> [!note]- Hint 2
> Reedy cofibrancy: the latching map of $X\times\Delta^{\bullet}$ is $X\times\partial\Delta^n \hookrightarrow X\times\Delta^n$ (product preserves the colimit defining the latching object), a monomorphism, hence a cofibration. Homotopical constancy: each $\Delta^n$ is contractible, so $X\times\Delta^n \to X$ is a weak equivalence.

> [!note]- Hint 3
> By the cartesian-closed adjunction, $\mathbf{sSet}(X\times\Delta^n, Y) \cong \mathbf{sSet}(\Delta^n, Y^X) = (Y^X)_n$. This is exactly $\mathrm{map}(X,Y)_n$, so $\mathrm{map}(X,Y) \cong Y^X$ as simplicial sets.

---

# Solution

The plan: Step 1 verifies $X\times\Delta^{\bullet}$ is a frame; Step 2 applies the cartesian-closed adjunction to identify the function complex with $Y^X$; Step 3 reads off the Kan and $\pi_0$ conclusions.

**Step 1: $X \times \Delta^{\bullet}$ is a cosimplicial frame on $X$.**

> [!note]- Derivation
> *Homotopical constancy.* For each $[n]$, the projection $X\times\Delta^n \to X\times\Delta^0 = X$ is a weak equivalence because $\Delta^n$ is contractible and $X\times(-)$ preserves weak equivalences (it is left Quillen for the cartesian monoidal model structure, and all simplicial sets are cofibrant, so Ken Brown applies). Every structure map $X\times\Delta^m \to X\times\Delta^n$ is likewise a weak equivalence. So condition (2) holds, with $(X\times\Delta^{\bullet})^0 = X$.
>
> *Reedy cofibrancy.* The functor $X\times(-)$ preserves colimits (it is a left adjoint, by cartesian closure), so the latching object is
> $$L_n(X\times\Delta^{\bullet}) = X\times L_n(\Delta^{\bullet}) = X\times\partial\Delta^n,$$
> and the latching map is $X\times\partial\Delta^n \xrightarrow{\mathrm{id}_X\times\iota} X\times\Delta^n$ for the boundary inclusion $\iota : \partial\Delta^n\hookrightarrow\Delta^n$. Since $\iota$ is a monomorphism and products of monomorphisms with anything are monomorphisms in $\mathbf{sSet}$, the latching map is a monomorphism, hence a cofibration. So condition (1) holds. (This is the cartesian instance of SM7.) Therefore $X\times\Delta^{\bullet}$ is a cosimplicial frame on $X$.

**Step 2: The function complex is the internal hom $Y^X$.**

> [!note]- Derivation
> With the frame $X\times\Delta^{\bullet}$ and the fibrant $Y$ (a Kan complex, so no fibrant replacement needed: $RY = Y$), the [[Def - Homotopy Function Complex|homotopy function complex]] is
> $$\mathrm{map}(X, Y)_n = \mathbf{sSet}\big((X\times\Delta^{\bullet})^n, Y\big) = \mathbf{sSet}(X\times\Delta^n, Y).$$
> By cartesian closure (the defining adjunction $-\times X \dashv (-)^X$),
> $$\mathbf{sSet}(X\times\Delta^n, Y) \cong \mathbf{sSet}(\Delta^n, Y^X) = (Y^X)_n,$$
> the last step by the [[Def - Simplicial Set|Yoneda]] identification $\mathbf{sSet}(\Delta^n, K) = K_n$. These bijections are natural in $[n]$ — a coface $d^i$ or codegeneracy $s^j$ of the frame corresponds to the same operation on $(Y^X)_\bullet$ — so they assemble into an isomorphism of simplicial sets
> $$\mathrm{map}(X, Y) \;\cong\; Y^X.$$
> The abstract derived mapping space *is* the internal hom.

**Step 3: $Y^X$ is a Kan complex with $\pi_0 = [X,Y]$.**

> [!note]- Derivation
> By [[Thm - Framings Compute Homotopy Function Complexes]], for cofibrant source ($X$, automatic) and fibrant target ($Y$ Kan), $\mathrm{map}(X,Y)$ is a Kan complex; via Step 2, $Y^X$ is a Kan complex. (Directly: $Y$ Kan means $Y\to *$ has the RLP against horn inclusions, and the internal-hom adjunction transposes a horn-filling problem for $Y^X$ into a lifting problem $X\times\Lambda^n_i \to Y$ against $X\times\Delta^n$, solved because $X\times\Lambda^n_i \hookrightarrow X\times\Delta^n$ is an anodyne extension — a trivial cofibration — and $Y$ is fibrant.)
>
> By [[Ex - Pi-zero of the function complex is the homotopy classes]], $\pi_0\,\mathrm{map}(X,Y) = [X,Y]$; so $\pi_0(Y^X) = [X, Y]$, the set of homotopy classes of maps $X\to Y$. Thus the internal hom $Y^X$ is the derived mapping space, refining $[X,Y]$ into a Kan complex whose higher homotopy groups are the higher homotopies of maps.

> [!note]- Complete formal solution
> **(a)** $X\times\Delta^{\bullet}$ is homotopically constant (each $\Delta^n$ contractible, $X\times(-)$ preserves weak equivalences) and Reedy cofibrant (latching map $X\times\partial\Delta^n\hookrightarrow X\times\Delta^n$ is a monomorphism, using that $X\times(-)$ preserves the latching colimit and monomorphisms). So it is a cosimplicial frame on $X$.
>
> **(b)** $\mathrm{map}(X,Y)_n = \mathbf{sSet}(X\times\Delta^n, Y) \cong \mathbf{sSet}(\Delta^n, Y^X) = (Y^X)_n$ by cartesian closure and Yoneda, naturally in $[n]$; hence $\mathrm{map}(X,Y)\cong Y^X$.
>
> **(c)** As a function complex of a cofibrant source and fibrant target, $\mathrm{map}(X,Y) = Y^X$ is a Kan complex, and $\pi_0(Y^X) = \pi_0\,\mathrm{map}(X,Y) = [X,Y]$. $\blacksquare$

---

# Key Takeaways

**In $\mathbf{sSet}$ the derived mapping space is the internal hom, and this is the model case that makes "homotopy function complex" concrete.** Simplicial sets are cartesian closed, so the internal hom $Y^X$ exists with no extra work, and the framing theory says it *is* the homotopy function complex (for $Y$ a Kan complex). This is the cleanest possible example of a derived mapping space: its $n$-simplices are literally maps $X\times\Delta^n\to Y$, its $\pi_0$ is homotopy classes, and its higher homotopy groups are the homotopy groups of the space of maps. Whenever you want intuition for $\mathrm{map}(X,Y)$ in an abstract model category, picture $Y^X$ in $\mathbf{sSet}$: the abstract construction is engineered to reproduce exactly this in the simplicial-set case.

**Cartesian closure is a simplicial model structure with tensoring $= \times$, so self-enrichment is the canonical frame.** The recognition that $\mathbf{sSet}$ is enriched *over itself* via the internal hom, with the product as tensoring, is what lets the general "tensor with $\Delta^{\bullet}$ is a frame" result apply verbatim. This is a recurring pattern: a cartesian closed category (or more generally a closed monoidal model category) is automatically self-enriched, and the product with the standard simplices is the canonical frame. The transferable move: in any cartesian closed model category, expect the internal hom to be the homotopy function complex once you fibrantly replace the target.

**Horn-filling for the internal hom transposes to anodyne lifting for the target, which is why $Y$ being Kan makes $Y^X$ Kan.** The direct proof that $Y^X$ is a Kan complex is a clean instance of the adjunction technique (Legal Operation 9): a horn $\Lambda^n_i \to Y^X$ transposes to $X\times\Lambda^n_i \to Y$, and the inclusion $X\times\Lambda^n_i \hookrightarrow X\times\Delta^n$ is an anodyne extension (trivial cofibration), so it lifts against the fibrant $Y$. This "transpose the horn-filling problem to a lifting problem against the fibrant target" is the universal reason function complexes are Kan complexes, and it works in any model category via [[Ex - In a simplicial model category the tensor with simplices is a frame|the framing version of SM7]]. The diagnostic: to show a mapping space is fibrant, transpose its lifting problems to the target and use the target's fibrancy.
