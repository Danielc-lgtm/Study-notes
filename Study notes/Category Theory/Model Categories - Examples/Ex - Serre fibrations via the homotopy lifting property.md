---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - The Quillen Model Structure on Topological Spaces"
  - "Def - Topological Space"
  - "Def - Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Prove that a continuous map $p : E \to B$ has the **right lifting property** against the bottom-inclusions $\{D^n \hookrightarrow D^n \times I : n \geq 0\}$ if and only if it has the **homotopy lifting property against all disks**, i.e. $p$ is a Serre fibration. Use the exponential adjunction $- \times I \dashv (-)^I$ to make the translation precise.

**Recall:**

In a [[Def - Model Category|model category]], $p$ has the **right lifting property** against $i$ when every commuting square with $i$ on the left and $p$ on the right has a diagonal filler.

The **bottom-inclusion** is $j_n : D^n \hookrightarrow D^n \times I$, $x \mapsto (x, 0)$. The **homotopy lifting property** of $p$ against $D^n$: given $H : D^n \times I \to B$ and $\tilde{h}_0 : D^n \to E$ with $p\tilde{h}_0 = H(-, 0)$, there is $\tilde{H} : D^n \times I \to E$ lifting $H$ and extending $\tilde{h}_0$. A **Serre fibration** is a map with this property for all $n$; these are the fibrations of the [[Def - The Quillen Model Structure on Topological Spaces|Quillen model structure]]. The exponential adjunction states $\mathbf{Top}(A \times I, B) \cong \mathbf{Top}(A, B^I)$ naturally, where $B^I$ is the path space with the compact-open topology (for $A$ locally compact Hausdorff, in particular for $A = D^n$).

---

# Convergent Strategy

**Problem class:** This is a "lifting against generators" problem: it identifies the fibrations of $\mathbf{Top}$ with a concrete homotopy-theoretic class, exactly the step needed to verify the lifting axiom in [[Thm - Topological Spaces Form a Model Category]]. The routine is to unwind a lifting square and recognise the resulting data as a homotopy lifting problem.

**Assumption pattern:** The recognisable structure is "RLP against the bottom-inclusions $D^n \hookrightarrow D^n \times I$". The shape of these generators — include a space as the bottom of its cylinder — is precisely what encodes "lift a homotopy starting from a given map", once one reads the cylinder direction as time.

**Theorem routing:** The route is a direct correspondence of data: a lifting square for $j_n$ against $p$ has corners (top: $\tilde{h}_0 : D^n \to E$, bottom: $H : D^n \times I \to B$, with the square commuting), and a filler is exactly a lifted homotopy $\tilde{H}$. The exponential adjunction $- \times I \dashv (-)^I$ provides the clean formal proof: it converts the lifting square against $j_n$ into an extension problem against the path-space evaluation $B^I \to B$.

**Key decision point:** The non-obvious choice is *how* to phrase the translation. Two routes work: a direct identification of the square's data with a homotopy lifting problem, and the adjunction route turning the cylinder-inclusion lift into a path-space extension. The direct route is more elementary; the adjunction route is what generalises and explains *why* the cylinder inclusion is the right generator. Presenting both is the decision that makes the exercise illuminating rather than rote.

---

# Legal Operations Used

1. **Operation 4 from the topic page (recognise a fibration of spaces by the homotopy lifting property).** This exercise *is* the justification of that operation — it shows RLP-against-cylinder-inclusions equals the homotopy lifting property.

2. **Operation 6 from the topic page (use the cylinder–path adjunction to convert lifting into extension).** The exponential adjunction route is exactly this operation.

---

# Hints

> [!note]- Hint 1
> Draw the lifting square for $j_n : D^n \hookrightarrow D^n \times I$ against $p : E \to B$. Label the top map, the bottom map, and the diagonal filler. What are they, as continuous maps?

> [!note]- Hint 2
> The top map is a map $D^n \to E$ (the lift of the bottom of a homotopy); the bottom map is a map $D^n \times I \to B$ (a homotopy); the diagonal is a map $D^n \times I \to E$. Compare with the definition of the homotopy lifting property word for word.

> [!note]- Hint 3
> For the adjunction route: by $-\times I \dashv (-)^I$, a map $D^n \times I \to B$ is a map $D^n \to B^I$, and a map $D^n \to E$ is just itself. The lifting square against $j_n$ becomes a lifting square against the path-fibration $(p^I, \text{ev}_0) : E^I \to E \times_B B^I$. Lifting against $j_n$ corresponds to lifting against this map.

---

# Solution

The two conditions are literally the same data viewed two ways. Directly, a lifting square against the bottom-inclusion is a homotopy lifting problem with its solution the diagonal. The adjunction makes the correspondence formal and explains the choice of generator.

**Step 1: a lifting square against $j_n$ is a homotopy lifting problem.**

> [!note]- Derivation
> A commuting square with $j_n : D^n \hookrightarrow D^n \times I$ on the left and $p : E \to B$ on the right consists of:
> - a top map $\tilde{h}_0 : D^n \to E$,
> - a bottom map $H : D^n \times I \to B$,
>
> commuting: $p \circ \tilde{h}_0 = H \circ j_n = H(-, 0)$. A diagonal filler is a map $\tilde{H} : D^n \times I \to E$ with $\tilde{H} \circ j_n = \tilde{h}_0$ (extends the top, i.e. $\tilde{H}(-, 0) = \tilde{h}_0$) and $p \circ \tilde{H} = H$ (projects to the bottom). 
>
> But this is *exactly* the homotopy lifting problem for $p$ against $D^n$: a homotopy $H$ downstairs, a lift $\tilde{h}_0$ of its bottom, and a lifted homotopy $\tilde{H}$. So the RLP of $p$ against $j_n$ holds for all $n$ if and only if $p$ has the homotopy lifting property against all disks, i.e. is a Serre fibration. This is the whole equivalence.

**Step 2: the adjunction route, explaining the choice of generator.**

> [!note]- Derivation
> By the exponential adjunction $- \times I \dashv (-)^I$ (valid since $D^n$ is locally compact Hausdorff), the bottom map $H : D^n \times I \to B$ corresponds to a map $\hat{H} : D^n \to B^I$ into the path space, and the top map $\tilde{h}_0 : D^n \to E$ stays as is. Form the **path fibration** of $p$: the map
> $$\Phi : E^I \longrightarrow E \times_B B^I, \qquad \gamma \longmapsto (\gamma(0),\, p \circ \gamma),$$
> whose target is the pullback of $\mathrm{ev}_0 : E \to E$ along $p^I$. A lift in the square against $j_n$ corresponds, under the adjunction, to a lift of the map $(\tilde{h}_0, \hat{H}) : D^n \to E \times_B B^I$ through $\Phi$. So "$p$ has the RLP against $\{j_n\}$" is equivalent to "$\Phi$ has the RLP against $\{D^n \to *\}$", i.e. $\Phi$ is surjective on the relevant lifting data — which unwinds again to the homotopy lifting property. The point of this reformulation is that it exhibits *why* the cylinder inclusion is the right generator: the cylinder direction $I$ is the time variable of a homotopy, and adjoint-transposing it produces the path space, the universal recipient of homotopies. This is the structural reason the Serre fibrations are cofibrantly generated by $\{D^n \hookrightarrow D^n \times I\}$.

> [!note]- Complete formal solution
> A commuting square with $j_n : D^n \hookrightarrow D^n \times I$ (left) and $p : E \to B$ (right) has top $\tilde{h}_0 : D^n \to E$, bottom $H : D^n \times I \to B$, with $p\tilde{h}_0 = H(-,0)$; a diagonal filler is $\tilde{H} : D^n \times I \to E$ with $\tilde{H}(-,0) = \tilde{h}_0$ and $p\tilde{H} = H$. This is precisely the homotopy lifting problem of $p$ against $D^n$, so RLP against all $j_n$ $\iff$ $p$ is a Serre fibration.
>
> Equivalently, by $-\times I \dashv (-)^I$, the data transpose to a lifting of $(\tilde{h}_0, \hat{H}) : D^n \to E\times_B B^I$ through the path fibration $\Phi : E^I \to E\times_B B^I$, $\gamma \mapsto (\gamma(0), p\gamma)$; this again unwinds to the homotopy lifting property and shows the cylinder inclusion is the generator because adjoint-transposing the time direction $I$ produces the path space. $\blacksquare$

---

# Key Takeaways

**The cylinder direction is time, and lifting against a cylinder inclusion is lifting a homotopy.** The reusable insight is the dictionary entry: the interval $I$ in $A \times I$ is the time parameter of a homotopy, the bottom-inclusion $A \hookrightarrow A \times I$ is "specify the start", and lifting against it is "lift the homotopy given its start". This is why the generating *trivial* cofibrations of $\mathbf{Top}$ are exactly the cylinder inclusions, and why fibrations come out as Serre fibrations. The trigger is "RLP against a cylinder/interval inclusion"; the reaction is "this is a homotopy lifting property". The same pattern in simplicial sets makes the horn inclusions $\Lambda^n_k \hookrightarrow \Delta^n$ the generating trivial cofibrations, with Kan fibrations as the analogue of Serre fibrations.

**The exponential adjunction converts lifting into extension and reveals the path space as the universal home of homotopies.** Transposing $- \times I \dashv (-)^I$ turns a homotopy $A \times I \to B$ into a path-valued map $A \to B^I$, and a homotopy lifting problem into a problem about the path fibration $E^I \to E \times_B B^I$. This is the formal mechanism behind nearly every fibration argument in topology: to build a lifted homotopy, build a map into the path space. The diagnostic to carry forward: whenever a lifting problem involves an interval or cylinder, adjoint-transpose to a path space, where the lift becomes an extension or a section — often easier, and always structurally clarifying. The same move builds fibrant replacements via the path-space construction and underlies the loop–suspension adjunction.

**Identifying fibrations with a lifting property against a small set is what makes a model structure cofibrantly generated and tractable.** The content of this exercise — that an *infinite* condition (lifting all homotopies of all disks) is detected by a *set* of generators (the cylinder inclusions) — is the defining feature of cofibrant generation. Without it, the lifting axiom MC4 would require checking against the entire class of trivial cofibrations, which is unmanageable; with it, you test against a small generating set and the small object argument does the rest. The transferable principle: whenever you must verify a map lies in one of the four model-category classes, look for the generating set the class is defined by lifting against, and test only against those. This reduces every class-membership question to a finite-looking computation, which is the practical reason the whole subject is workable.
