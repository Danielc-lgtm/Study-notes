---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Complete and Cocomplete Category"
  - "Thm - Products and Equalizers Give All Limits"
  - "Thm - Limits in Set and in Functor Categories"
tags: [category-theory, foundations]
---

# Problem Statement

Prove that $\mathbf{Set}$ is [[Def - Complete and Cocomplete Category|complete and cocomplete]]. Use the reduction theorem: show $\mathbf{Set}$ has all small [[Def - Product and Coproduct|products]] and all [[Def - Equalizer and Coequalizer|equalizers]], hence (by [[Thm - Products and Equalizers Give All Limits]]) all small limits; dually all coproducts and coequalizers, hence all colimits. Identify the limit of a small diagram $D : J \to \mathbf{Set}$ as the set of compatible families $\{(x_j) \in \prod_j D_j : D(f)(x_j) = x_k\}$ and the colimit as a quotient of the disjoint union.

**Recall:**

![[Def - Complete and Cocomplete Category#The Definition]]

By [[Thm - Products and Equalizers Give All Limits|the reduction theorem]], a category with all small products and all equalizers is complete; dually for coproducts and coequalizers.

---

# Convergent Strategy

**Problem class:** This is a "verify completeness via the reduction theorem" problem — the canonical application of "products + equalizers ⇒ complete". The routine is exactly two checks (products exist; equalizers exist), then quote the theorem, then read off the explicit formula.

**Assumption pattern:** The only structure is $\mathbf{Set}$ itself. The unlocking recognition is that $\mathbf{Set}$ visibly has cartesian products (over arbitrary index sets) and agreement-set equalizers, so the hypotheses of the reduction theorem are immediately met, and one gets all limits without checking each shape.

**Theorem routing:** The route is: cartesian products give all small products; agreement-sets give all equalizers; [[Thm - Products and Equalizers Give All Limits|the reduction theorem]] then gives completeness, with the explicit limit being the equalizer of the two maps between products — which in $\mathbf{Set}$ is the set of compatible families ([[Thm - Limits in Set and in Functor Categories]]). Dually for colimits.

**Key decision point:** The decision is to *use the reduction theorem rather than construct each limit by hand*. A direct construction of an arbitrary limit in $\mathbf{Set}$ is possible but laborious; routing through products-and-equalizers is the efficient path, and it also explains why the answer is "compatible families" — they are the agreement-subset of a product.

---

# Legal Operations Used

1. **Verify the two reduction hypotheses (from the topic page: products and equalizers).** Exhibit arbitrary cartesian products and agreement-set equalizers in $\mathbf{Set}$.

2. **Invoke the reduction theorem (operation: apply [[Thm - Products and Equalizers Give All Limits]]).** Conclude completeness from the two checks, and read the explicit limit as the equalizer of two product maps.

3. **Specialise to compatible families (operation: [[Thm - Limits in Set and in Functor Categories|limits in Set]]).** Identify the equalizer-of-products with the set of compatible families and the colimit with a quotient of the coproduct.

---

# Hints

> [!note]- Hint 1
> Do not construct an arbitrary limit directly. By [[Thm - Products and Equalizers Give All Limits|the reduction theorem]], it suffices to show $\mathbf{Set}$ has all small products and all equalizers.

> [!note]- Hint 2
> The product of any family $(A_i)_{i \in I}$ of sets is $\prod_i A_i = \{(a_i)_{i} : a_i \in A_i\}$ (functions $i \mapsto a_i$ with $a_i \in A_i$). The equalizer of $f, g : A \rightrightarrows B$ is $\{a : f(a) = g(a)\}$.

> [!note]- Hint 3
> Both exist for arbitrary (small) index sets and arbitrary parallel pairs. Apply the theorem: $\mathbf{Set}$ is complete.

> [!note]- Hint 4
> For the explicit formula, run the equalizer-of-products construction in $\mathbf{Set}$: $\lim D = \{(x_j) \in \prod_j D_j : D(f)(x_j) = x_k\}$, the compatible families. Dualize for the colimit.

---

# Solution

The plan: confirm $\mathbf{Set}$ has all small products and equalizers (two short verifications), apply the reduction theorem to get completeness, read off the compatible-family formula, then dualize for cocompleteness.

**Step 1: $\mathbf{Set}$ has all small products.**

> [!note]- Derivation
> For a small family $(A_i)_{i \in I}$, the cartesian product $\prod_{i} A_i = \{(a_i)_i : a_i \in A_i \text{ for all } i\}$ (i.e. functions $a : I \to \bigsqcup A_i$ with $a(i) \in A_i$) with projections $\pi_i((a_j)_j) = a_i$ is the [[Def - Product and Coproduct|product]]: a family of maps $(f_i : X \to A_i)$ assembles into the unique $\langle f_i\rangle(x) = (f_i(x))_i$. So all small products exist.

**Step 2: $\mathbf{Set}$ has all equalizers.**

> [!note]- Derivation
> For $f, g : A \rightrightarrows B$, the agreement-set $E = \{a \in A : f(a) = g(a)\}$ with inclusion $e$ is the [[Def - Equalizer and Coequalizer|equalizer]]: any $z : Z \to A$ with $fz = gz$ has image in $E$ and corestricts uniquely. So all equalizers exist.

**Step 3: $\mathbf{Set}$ is complete, with limits the compatible families.**

> [!note]- Derivation
> By [[Thm - Products and Equalizers Give All Limits|the reduction theorem]], having all small products and all equalizers makes $\mathbf{Set}$ complete. The explicit limit of $D : J \to \mathbf{Set}$ is the equalizer of $s, t : \prod_{j} D_j \rightrightarrows \prod_{f : j \to k} D_k$ where $\pi_f s = \pi_k$ and $\pi_f t = D(f)\pi_j$; in $\mathbf{Set}$ this equalizer is
> $$\lim D = \Big\{(x_j) \in \textstyle\prod_j D_j : D(f)(x_j) = x_k \text{ for all } f : j \to k\Big\},$$
> the set of compatible families (matching [[Thm - Limits in Set and in Functor Categories]]).

**Step 4: $\mathbf{Set}$ is cocomplete, dually.**

> [!note]- Derivation
> $\mathbf{Set}$ has all small coproducts (disjoint unions $\coprod_i A_i$) and all coequalizers (quotients by generated equivalence relations). By the dual of the reduction theorem, $\mathbf{Set}$ is cocomplete; the explicit colimit of $D$ is $\big(\coprod_j D_j\big)/\!\sim$, the disjoint union modulo the equivalence relation generated by $x_j \sim D(f)(x_j)$.

> [!note]- Complete formal solution
> $\mathbf{Set}$ has all small [[Def - Product and Coproduct|products]] (cartesian products $\prod_i A_i$ with coordinate projections, the induced map $\langle f_i\rangle(x) = (f_i(x))_i$) and all [[Def - Equalizer and Coequalizer|equalizers]] (agreement-sets $\{a : f(a)=g(a)\} \hookrightarrow A$). By [[Thm - Products and Equalizers Give All Limits|the reduction theorem]], $\mathbf{Set}$ is [[Def - Complete and Cocomplete Category|complete]], and the limit of $D : J \to \mathbf{Set}$ is the equalizer of the canonical pair between $\prod_j D_j$ and $\prod_{f} D_{\mathrm{cod}\,f}$, namely the compatible families $\{(x_j) : D(f)(x_j) = x_k\}$. Dually $\mathbf{Set}$ has all coproducts (disjoint unions) and coequalizers (quotients by generated equivalence relations), so it is cocomplete, with $\operatorname{colim} D = (\coprod_j D_j)/\!\sim$. Hence $\mathbf{Set}$ is bicomplete. $\blacksquare$

---

# Key Takeaways

**Completeness is a two-line check via the reduction theorem, never a per-shape verification.** The reusable method is: to prove a category complete, exhibit all small products and all equalizers, then cite [[Thm - Products and Equalizers Give All Limits|"products + equalizers ⇒ complete"]]. This is the standard route for $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Ab}$, $\mathbf{Ring}$, $\mathbf{Mod}_R$, $\mathbf{Top}$ — you never check pullbacks, inverse limits, and large equalizers separately. The trigger: any time a problem asks "is $\mathcal{C}$ complete?", reach for the two-check reduction, and remember the dual (coproducts + coequalizers) for cocompleteness.

**The explicit limit in $\mathbf{Set}$ is the compatible families, because the equalizer-of-products construction cuts the product down by the cone equations.** Running the reduction theorem in $\mathbf{Set}$ produces, transparently, the set of tuples $(x_j)$ satisfying $D(f)(x_j) = x_k$ — the product of vertices intersected with the agreement conditions for the edges. This is the ground-truth description of *every* limit, and via [[Thm - Representable Functors Preserve Limits|representability]] it computes the hom-sets into limits in any category. The transferable insight is that "limit = compatible families" is not a separate fact but the $\mathbf{Set}$-shadow of the general construction; whenever you need to build a map into a limit, you produce a compatible family.

**Bicompleteness of $\mathbf{Set}$ is the foundation everything else stands on, via creation and pointwise computation.** Because $\mathbf{Set}$ is complete and cocomplete, algebraic categories inherit completeness through limit-[[Def - Preservation, Reflection, and Creation of Limits|creating]] forgetful functors, and [[Thm - Limits in Set and in Functor Categories|functor categories]] inherit it pointwise — so the entire web of complete categories is bootstrapped from this one result. The diagnostic to carry forward: once you know the base category is bicomplete, completeness propagates automatically to slices, functor/presheaf categories, and categories of algebras, and the *concrete* description of every limit there reduces to compatible families of underlying-set data. This is why proving $\mathbf{Set}$ bicomplete is the highest-leverage single verification in the chapter; see [[Thm - Limits in Set and in Functor Categories]] for the propagation.
