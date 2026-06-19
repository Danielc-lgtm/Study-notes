---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Pullback and Pushout"
  - "Def - Limit and Colimit"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Problem Statement

Let $A, B \subseteq C$ be subsets (more generally, subobjects given by [[Def - Isomorphism, Monomorphism, Epimorphism|monomorphisms]] $A \hookrightarrow C$, $B \hookrightarrow C$). Show that the intersection $A \cap B$ is the [[Def - Pullback and Pushout|pullback]] of the two inclusions,
$$A \cap B \;=\; A \times_C B,$$
and hence a [[Def - Limit and Colimit|limit]]. Deduce that intersection of subobjects is computed by a pullback in any category with pullbacks, that the pullback of a mono is a mono (so $A \cap B \hookrightarrow C$ is again a subobject), and that arbitrary intersections are wide pullbacks (limits over a discrete-plus-cospan shape).

**Recall:**

A **pullback** of $A \xrightarrow{f} C \xleftarrow{g} B$ is $A \times_C B = \{(a,b) : f(a) = g(b)\}$ in $\mathbf{Set}$, universal among objects mapping compatibly to $A$ and $B$ over $C$.

A **subobject** of $C$ is (an isomorphism class of) a monomorphism $A \hookrightarrow C$; "$A \subseteq B$ as subobjects" means the inclusion factors through $B \hookrightarrow C$.

---

# Convergent Strategy

**Problem class:** This is a "recognise a set operation as a universal construction" problem, parallel to "kernel as pullback". The routine: match the element-wise intersection to the pullback's compatible-pair description, then transport the subobject property via "pullback of a mono is a mono".

**Assumption pattern:** The key assumption is that $A$ and $B$ are *subobjects* of $C$ — given by monos. Intersection is "elements lying in both", which over the common ambient $C$ is exactly "pairs $(a,b)$ with the same image in $C$" — the pullback condition. Recognising "lies in both $\Rightarrow$ same image in the ambient object" routes to a pullback.

**Theorem routing:** The route: $A \times_C B = \{(a,b) : \iota_A(a) = \iota_B(b)\}$; since $\iota_A, \iota_B$ are inclusions, $\iota_A(a) = \iota_B(b)$ forces $a = b \in A \cap B$, giving $A \times_C B \cong A \cap B$. The pullback being a [[Def - Limit and Colimit|limit]] over the cospan shape, intersection is a limit. "[[Def - Pullback and Pushout|Pullback of a mono is a mono]]" makes the intersection a subobject; arbitrary intersections are wide pullbacks.

**Key decision point:** The subtlety is that the pullback $A \times_C B$ is a priori a set of *pairs*, while $A \cap B$ is a set of *elements*; the identification works precisely because both legs are monos, so a compatible pair $(a,b)$ has $a$ and $b$ with the same image, hence (by injectivity) "the same element" lying in both $A$ and $B$. Without the mono hypothesis the pullback is the larger "fibre product", not the intersection.

---

# Legal Operations Used

1. **Recognise intersection as a pullback of inclusions (from the topic page: pullbacks compute intersections).** $A \cap B = A \times_C B$ when $A, B \hookrightarrow C$ are monos.

2. **Transport the mono property through the pullback (operation: pullback of a mono is a mono).** Conclude $A \cap B \hookrightarrow C$ is a subobject.

3. **Assemble arbitrary intersections as a wide pullback (operation: limit over a multi-leg cospan).** $\bigcap_i A_i$ is the limit of the diagram with all $A_i \hookrightarrow C$, a wide pullback.

---

# Hints

> [!note]- Hint 1
> Intersection is "in both $A$ and $B$". Over the common ambient $C$, an element of $A$ and an element of $B$ "are the same" iff they have the same image in $C$ — which is the pullback condition $\iota_A(a) = \iota_B(b)$.

> [!note]- Hint 2
> Compute $A \times_C B = \{(a,b) : \iota_A(a) = \iota_B(b)\}$. Because the inclusions are injective, this is in bijection with $\{c \in C : c \in A \text{ and } c \in B\} = A \cap B$.

> [!note]- Hint 3
> The pullback of a [[Def - Isomorphism, Monomorphism, Epimorphism|monomorphism]] is a monomorphism, so the projection $A \cap B \to C$ is monic — i.e. $A \cap B$ is genuinely a subobject of $C$.

> [!note]- Hint 4
> For arbitrary intersections, replace the binary cospan by a family of inclusions $A_i \hookrightarrow C$ and take the limit (a "wide pullback"): $\bigcap_i A_i$.

---

# Solution

The plan: identify the pullback of two subobject-inclusions with their intersection (using injectivity to pass from pairs to elements), note it is a limit, transport the mono property to confirm it is a subobject, and generalise to wide pullbacks for arbitrary intersections.

**Step 1: The pullback of two inclusions is the intersection.**

> [!note]- Derivation
> Let $\iota_A : A \hookrightarrow C$, $\iota_B : B \hookrightarrow C$ be the inclusions. The [[Def - Pullback and Pushout|pullback]] is
> $$A \times_C B = \{(a,b) \in A \times B : \iota_A(a) = \iota_B(b)\}.$$
> Since $\iota_A, \iota_B$ are inclusions, $\iota_A(a) = \iota_B(b)$ means $a$ and $b$ are *the same element* $c$ of $C$, lying in both $A$ and $B$. The map $(a,b) \mapsto \iota_A(a) = c$ is a bijection $A \times_C B \cong \{c \in C : c \in A,\ c \in B\} = A \cap B$, compatible with the projections to $A$ and $B$. So $A \cap B = A \times_C B$ as subobjects of $C$.

**Step 2: The intersection is a limit.**

> [!note]- Derivation
> A pullback is the [[Def - Limit and Colimit|limit]] of the cospan diagram $A \to C \leftarrow B$. Hence $A \cap B$, being this pullback, is a limit; its universal property reads "a map into $A \cap B$ is a map landing in both $A$ and $B$", which is exactly what one expects of an intersection.

**Step 3: The intersection is again a subobject.**

> [!note]- Derivation
> The [[Def - Pullback and Pushout|pullback of a monomorphism is a monomorphism]]: since $\iota_B$ is monic, the projection $p_1 : A \times_C B \to A$ is monic, and composing with the mono $\iota_A : A \hookrightarrow C$ gives a monomorphism $A \cap B \to C$. So $A \cap B$ is a genuine subobject of $C$, as required for "intersection of subobjects".

**Step 4: Arbitrary intersections are wide pullbacks.**

> [!note]- Derivation
> For a family of subobjects $(A_i \hookrightarrow C)_{i \in I}$, form the diagram consisting of all the $A_i$ and $C$ with the inclusions; its [[Def - Limit and Colimit|limit]] (a **wide pullback**) is $\{(a_i)_i : \iota_{A_i}(a_i) \text{ all equal in } C\} \cong \bigcap_i A_i$. Hence in any category with such limits, arbitrary intersections of subobjects exist and are computed as wide pullbacks.

> [!note]- Complete formal solution
> Let $\iota_A : A \hookrightarrow C$, $\iota_B : B \hookrightarrow C$ be subobject inclusions (monos). Their [[Def - Pullback and Pushout|pullback]] $A \times_C B = \{(a,b) : \iota_A(a) = \iota_B(b)\}$ is, by injectivity of the inclusions, in projection-compatible bijection with $\{c \in C : c \in A \text{ and } c \in B\} = A \cap B$; so $A \cap B = A \times_C B$. This is the [[Def - Limit and Colimit|limit]] of the cospan $A \to C \leftarrow B$, hence intersection is a limit. Since the [[Def - Pullback and Pushout|pullback of a mono is a mono]], $A \cap B \to C$ is monic, so $A \cap B$ is a subobject of $C$. For a family $(A_i \hookrightarrow C)$, the wide pullback $\lim_i (A_i \to C)$ is $\bigcap_i A_i$, so arbitrary intersections are limits in any category admitting them. $\blacksquare$

---

# Key Takeaways

**Intersection is the pullback of inclusions, and "lies in both" means "same image in the ambient object".** The reusable insight is that the intersection $A \cap B$ of two subobjects is the [[Def - Pullback and Pushout|fibre product]] $A \times_C B$ over their common ambient $C$ — the pullback condition $\iota_A(a) = \iota_B(b)$ being precisely "they are the same element of $C$". This makes intersection a [[Def - Limit and Colimit|limit]], computable in any category with pullbacks, and it is the categorical reason intersections of subgroups, subspaces, ideals, and closed sets are again of the same kind: each is a pullback of monos, and the pullback of a mono is a mono. The trigger: "the part of the ambient object lying in both subobjects" is a pullback of inclusions.

**The mono hypothesis is what turns the fibre product (pairs) into the intersection (elements).** The crucial discrimination is that the pullback $A \times_C B$ is a priori a set of *compatible pairs*, and it collapses to the *intersection* of elements only because the legs are monomorphisms — injectivity identifies a compatible pair $(a,b)$ with a single shared element. Drop the mono hypothesis and the pullback is the genuine fibre product, generally larger than any "intersection" (it records *how* elements match, not just *that* they do). This distinction — fibre product in general, intersection when the legs are monic — is the same distinction as kernel pair versus kernel in [[Ex - The kernel as a pullback]], and recognising it prevents conflating the two.

**Pullbacks unify preimage, intersection, kernel, and fibre — one construction, parametrised by the cospan.** The transferable principle is that a great many "refined sub-constructions" are pullbacks of the appropriate cospan: preimage ($f$ against a subobject inclusion), intersection (two subobject inclusions), kernel ($\varphi$ against the basepoint), fibre ($f$ against a point). Once you see them all as pullbacks, their shared properties — stability under further pullback, being subobjects when the legs are monos, functoriality via [[Def - Preservation, Reflection, and Creation of Limits|base change]] — follow uniformly from the [[Def - Pullback and Pushout|pullback]] machinery rather than being proved case by case. This is the categorical economy that makes "fibre product" the single most important construction in geometry, where it specialises to the fibre product of schemes; see [[Ex - Fibre products of schemes are pullbacks]].
