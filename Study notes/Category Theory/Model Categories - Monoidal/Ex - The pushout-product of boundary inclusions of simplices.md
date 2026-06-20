---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Monoidal Model Category"
  - "Def - Pullback and Pushout"
  - "Def - Simplicial Set"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

In the cartesian monoidal model category $(\mathbf{sSet}, \times, \Delta^0)$, the generating cofibrations are the **boundary inclusions** $\partial\Delta^m \hookrightarrow \Delta^m$. Show that the pushout-product of two boundary inclusions,
$$(\partial\Delta^m \hookrightarrow \Delta^m) \mathbin{\square} (\partial\Delta^n \hookrightarrow \Delta^n),$$
is the inclusion
$$\big(\partial\Delta^m \times \Delta^n\big) \cup_{\partial\Delta^m \times \partial\Delta^n} \big(\Delta^m \times \partial\Delta^n\big) \;\hookrightarrow\; \Delta^m \times \Delta^n,$$
and that this is a **monomorphism**, hence a cofibration in $\mathbf{sSet}$. Identify the source as the **boundary** $\partial(\Delta^m \times \Delta^n)$ of the product (the "sub-prism of faces"), and explain why this verifies the cofibration half of the [[Def - Monoidal Model Category|pushout-product axiom]] on generators.

**Recall:**

For cofibrations $f : U \to V$ and $g : X \to Y$, the **pushout-product** is the map $f \mathbin{\square} g : (V \times X) \cup_{U \times X} (U \times Y) \to V \times Y$ out of the [[Def - Pullback and Pushout|pushout]] of $V \times X \leftarrow U \times X \rightarrow U \times Y$.

In $\mathbf{sSet}$ (the [[Def - Simplicial Set|simplicial sets]]) the cofibrations are exactly the **monomorphisms** (levelwise injections). The standard simplex $\Delta^m$ has $\partial\Delta^m$ its boundary (the union of all codimension-one faces), with $\partial\Delta^m \hookrightarrow \Delta^m$ a mono.

---

# Convergent Strategy

**Problem class:** This is a *verify-the-axiom-on-generators* problem, the central computational task of §2: compute a pushout-product on the generating cofibrations and recognize the result as a cofibration. Because $\mathbf{sSet}$ is cofibrantly generated, this single computation (plus the trivial-cofibration analogue) yields the full pushout-product axiom by the reduction-to-generators lemma.

**Assumption pattern:** The crucial facts are that cofibrations in $\mathbf{sSet}$ are *exactly* the monomorphisms, and that $\mathbf{sSet}$, being a presheaf category, has colimits computed levelwise so that a pushout of monos along monos is again a mono. The combinatorial fact that the pushout corner is the boundary of the prism is what makes the result geometrically meaningful.

**Theorem routing:** The route is: compute the pushout $\partial\Delta^m \times \Delta^n \cup_{\partial\Delta^m \times \partial\Delta^n} \Delta^m \times \partial\Delta^n$ as a sub-simplicial-set of $\Delta^m \times \Delta^n$; recognize the inclusion into $\Delta^m \times \Delta^n$ as a monomorphism (levelwise, using that the union of two monos is a mono); conclude it is a cofibration since cofibrations $=$ monos in $\mathbf{sSet}$. This routes through the [[Def - Monoidal Model Category|monoidal model category]] definition's cofibration clause.

**Key decision point:** The non-obvious step is realizing the pushout corner is a *union of sub-objects inside $\Delta^m \times \Delta^n$* rather than an abstract gluing — because $\partial\Delta^m \times \Delta^n$ and $\Delta^m \times \partial\Delta^n$ are both subobjects of $\Delta^m \times \Delta^n$ meeting in $\partial\Delta^m \times \partial\Delta^n$, their pushout *is* their union. This identification is what turns "is the pushout-product a mono?" into the transparent "is a union of subobjects a subobject?".

---

# Legal Operations Used

1. **Operation 1 (form the pushout-product), topic page.** We construct $f \mathbin{\square} g$ explicitly as the map out of the pushout of the two product faces.

2. **Operation 3 (reduce an axiom to generators), topic page.** We are checking the pushout-product axiom only on the generating cofibrations $\partial\Delta^m \hookrightarrow \Delta^m$, relying on the reduction-to-generators lemma to extend it to all cofibrations.

---

# Hints

> [!note]- Hint 1
> Write down the pushout-product literally: $f = (\partial\Delta^m \hookrightarrow \Delta^m)$, $g = (\partial\Delta^n \hookrightarrow \Delta^n)$. What is the pushout of $\Delta^m \times \partial\Delta^n \leftarrow \partial\Delta^m \times \partial\Delta^n \rightarrow \partial\Delta^m \times \Delta^n$?

> [!note]- Hint 2
> All four objects are subobjects of $\Delta^m \times \Delta^n$. When two subobjects $A, B$ of $X$ meet in $A \cap B$, their pushout over $A \cap B$ is their union $A \cup B \subseteq X$. So the source of $f \mathbin{\square} g$ is $(\partial\Delta^m \times \Delta^n) \cup (\Delta^m \times \partial\Delta^n)$.

> [!note]- Hint 3
> $\mathbf{sSet}$ is a presheaf category, so monos are levelwise injections and unions of subobjects are subobjects. The inclusion of a union of two subobjects into the ambient object is a mono. Cofibrations in $\mathbf{sSet}$ are exactly monos.

> [!note]- Hint 4
> Geometrically: $\partial(\Delta^m \times \Delta^n)$, the boundary of the prism, is the union of the faces $\partial\Delta^m \times \Delta^n$ and $\Delta^m \times \partial\Delta^n$. The pushout-product is the inclusion of this boundary into the prism — exactly the "boundary-relative product".

---

# Solution

The route is: (1) write the pushout-product as the map out of the pushout of the two faces; (2) identify the pushout with the union $\partial\Delta^m \times \Delta^n \cup \Delta^m \times \partial\Delta^n$ inside the prism; (3) observe this is the boundary of the prism, and its inclusion is a mono, hence a cofibration. This is the cofibration half of the axiom on generators.

**Step 1: The pushout-product as a map out of a union.**

> [!note]- Derivation
> With $f : \partial\Delta^m \hookrightarrow \Delta^m$ and $g : \partial\Delta^n \hookrightarrow \Delta^n$, the pushout-product source is the [[Def - Pullback and Pushout|pushout]]
> $$P = (\Delta^m \times \partial\Delta^n) \cup_{\partial\Delta^m \times \partial\Delta^n} (\partial\Delta^m \times \Delta^n)$$
> of the span $\Delta^m \times \partial\Delta^n \xleftarrow{\,f \times 1\,} \partial\Delta^m \times \partial\Delta^n \xrightarrow{\,1 \times g\,} \partial\Delta^m \times \Delta^n$. All three objects include into $\Delta^m \times \Delta^n$, compatibly, so by the universal property of the pushout there is a canonical map $f \mathbin{\square} g : P \to \Delta^m \times \Delta^n$.

**Step 2: $P$ is the union of the two faces, i.e. the boundary of the prism.**

> [!note]- Derivation
> In the presheaf category $\mathbf{sSet}$, colimits are computed levelwise. The objects $\partial\Delta^m \times \Delta^n$ and $\Delta^m \times \partial\Delta^n$ are subobjects of $\Delta^m \times \Delta^n$ whose intersection (levelwise) is exactly $\partial\Delta^m \times \partial\Delta^n$. For subobjects $A, B \subseteq X$ with $A \cap B = C$, the pushout $A \cup_C B$ is the union $A \cup B$ as a subobject of $X$. Hence
> $$P = (\partial\Delta^m \times \Delta^n) \cup (\Delta^m \times \partial\Delta^n) \;\subseteq\; \Delta^m \times \Delta^n,$$
> and the canonical map $f \mathbin{\square} g : P \to \Delta^m \times \Delta^n$ is the inclusion of this union. Geometrically this union is the boundary $\partial(\Delta^m \times \Delta^n)$ of the prism — every codimension-one face of the product lies in one of the two factors' boundaries.

**Step 3: The inclusion is a mono, hence a cofibration.**

> [!note]- Derivation
> The inclusion of a subobject is a monomorphism: levelwise, $P_k \hookrightarrow (\Delta^m \times \Delta^n)_k$ is an inclusion of sets. (Concretely, a union of two levelwise-injective subobjects is levelwise-injective into the ambient object.) Since the cofibrations of $\mathbf{sSet}$ are *exactly* the monomorphisms, $f \mathbin{\square} g$ is a cofibration. This verifies the cofibration clause of the [[Def - Monoidal Model Category|pushout-product axiom]] on the generating cofibrations. By the reduction-to-generators lemma (the class of $f$ with $f \mathbin{\square} g$ a cofibration is closed under pushout, transfinite composition, and retract), the cofibration clause then holds for *all* cofibrations.

> [!note]- Complete formal solution
> Let $f : \partial\Delta^m \hookrightarrow \Delta^m$ and $g : \partial\Delta^n \hookrightarrow \Delta^n$. The pushout-product source is the [[Def - Pullback and Pushout|pushout]] $P = (\Delta^m \times \partial\Delta^n) \cup_{\partial\Delta^m \times \partial\Delta^n} (\partial\Delta^m \times \Delta^n)$. Since $\mathbf{sSet}$ is a presheaf category (colimits levelwise) and the two faces are subobjects of $\Delta^m \times \Delta^n$ meeting in $\partial\Delta^m \times \partial\Delta^n$, the pushout is their union $P = (\partial\Delta^m \times \Delta^n) \cup (\Delta^m \times \partial\Delta^n) \subseteq \Delta^m \times \Delta^n$, which is the boundary $\partial(\Delta^m \times \Delta^n)$ of the prism. The pushout-product $f \mathbin{\square} g : P \hookrightarrow \Delta^m \times \Delta^n$ is the inclusion of this subobject, a monomorphism, hence a [[Def - Simplicial Set|simplicial-set]] cofibration. This is the cofibration half of the [[Def - Monoidal Model Category|pushout-product axiom]] on generators; the reduction-to-generators lemma extends it to all cofibrations. (The trivial-cofibration half is verified separately, using that one factor being an anodyne extension makes $f \mathbin{\square} g$ anodyne.) $\qquad\blacksquare$

---

# Key Takeaways

**The pushout-product of boundary inclusions is the boundary inclusion of the product — "$\square$ of cells is the boundary-relative product cell".** This is the geometric true name of the pushout-product made concrete. The corner pushout $P$ is not an abstract gadget; it is literally the boundary $\partial(\Delta^m \times \Delta^n)$ of the prism, assembled from the two families of faces. The transferable picture: whenever you compute $f \mathbin{\square} g$ for "inclusion-of-boundary" type cofibrations, the answer is the inclusion of the product's boundary, and it is a cofibration because boundaries of products are built from boundaries of factors. This picture explains at a glance why the pushout-product axiom holds in every "cellular" model category — $\mathbf{Top}$, $\mathbf{sSet}$, $\mathbf{Ch}(R)$ — and is the reason the axiom is checkable rather than mysterious.

**In a presheaf category, "is this pushout-product a cofibration?" collapses to "is a union of subobjects a subobject?" — a triviality.** The decisive simplification was recognizing the pushout of two subobjects (along their intersection) as their union inside the ambient object, which is immediate once colimits are levelwise. The trigger-reaction pattern: in any presheaf (or more generally Grothendieck) topos, pushouts of monomorphisms along monomorphisms are monomorphisms, and intersecting subobjects pushout to their union. So in $\mathbf{sSet}$ and any presheaf category, the cofibration clause of the pushout-product axiom for the "cofibrations = monos" model structure is automatic for *any* monos, not just boundary inclusions. This is why cartesian closed presheaf categories are such reliable sources of monoidal model structures.

**Reduction to generators is what makes an "for all cofibrations" axiom a finite computation, and this exercise is its archetype.** We verified the pushout-product axiom by checking it on the *generating* cofibrations only, trusting the closure lemma to extend it. The reusable diagnostic: whenever an axiom is quantified over all cofibrations (or all trivial cofibrations) in a cofibrantly generated category, do not attempt the general case — verify it on generators and cite that the relevant class is closed under pushout, transfinite composition, and retract. This converts every monoidal-model-category verification into a bounded combinatorial check, and the same reduction underlies verifying that a functor is left Quillen, that a model structure is cofibrantly generated, and that an adjunction is Quillen. See also [[Ex - Reducing the pushout-product axiom to generating cofibrations]].
