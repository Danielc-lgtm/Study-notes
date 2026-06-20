---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Pre-Triangulated Category"
  - "Def - Cofiber and Fiber Sequence"
  - "Def - Pointed Model Category Suspension and Loop"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

A **triangulated category** is an additive category $\mathcal{T}$ with a shift autoequivalence $\Sigma = [1]$ and a class of distinguished triangles $X \to Y \to Z \to \Sigma X$ satisfying axioms TR1–TR4 (existence, rotation, morphisms, octahedral). Show that every triangulated category is a [[Def - Pre-Triangulated Category|pre-triangulated category]]:

1. Define $\Omega = \Sigma^{-1}$ and check $\Sigma \dashv \Omega$ (in fact $\Sigma \cong \Omega^{-1}$ are mutually inverse equivalences, hence adjoint).
2. Take the distinguished triangles as **both** the cofiber sequences and (rotated) the fiber sequences, and verify the pre-triangulated existence, rotation, and long-exact-sequence axioms from TR1–TR3.
3. Identify which hypothesis of "triangulated" is the *extra* one not required by pre-triangulated, and explain why the two sequence classes collapse to one.

**Recall:**

![[Def - Pre-Triangulated Category#The Definition]]

A [[Def - Pre-Triangulated Category|pre-triangulated category]] has a pointed structure, an adjunction $\Sigma \dashv \Omega$, classes of [[Def - Cofiber and Fiber Sequence|cofiber and fiber sequences]], and the long-exact-sequence axioms. A triangulated category is the special case where $\Sigma$ is an *equivalence*. TR2 (rotation): $X \to Y \to Z \to \Sigma X$ is distinguished iff $Y \to Z \to \Sigma X \xrightarrow{-\Sigma f} \Sigma Y$ is. Applying $\mathcal{T}(W, -)$ to a distinguished triangle yields a long exact sequence of abelian groups.

---

# Convergent Strategy

**Problem class:** This is a "show a stronger structure is an instance of a weaker one" exercise — a containment proof. The route is to produce the pre-triangulated data from the triangulated data and check each pre-triangulated axiom against TR1–TR3.

**Assumption pattern:** The decisive assumption is that the shift $\Sigma$ is an **autoequivalence** (TR's standing hypothesis). This is exactly the hypothesis that pre-triangulated does *not* require, and it is what lets $\Omega = \Sigma^{-1}$ exist and what merges the cofiber and fiber classes. Additivity gives the long exact sequences as sequences of abelian groups.

**Theorem routing:** Part (1) routes through "mutually inverse equivalences are adjoint." Part (2) routes through TR1 (existence) → pre-triangulated existence, TR2 (rotation) → pre-triangulated rotation, and the standard long exact sequence of a triangle → pre-triangulated long-exact-sequence axiom. Part (3) routes through comparing the definitions.

**Key decision point:** The non-obvious step is realizing that in the triangulated case a single distinguished triangle serves as *both* a cofiber sequence $X \to Y \to Z \to \Sigma X$ and, after applying $\Sigma^{-1}$ and rotating, a fiber sequence $\Omega Z \to X \to Y \to Z$. The collapse of two classes into one is *caused* by invertibility of $\Sigma$ — choosing to identify them via $\Sigma^{-1}$ is the move that makes a triangulated category fit the pre-triangulated template.

---

# Legal Operations Used

1. **Operation 6 from the topic page (use the suspension–loop adjunction).** Part (1) supplies the adjunction from the invertible shift.

2. **Operation 7 from the topic page (rotate a (co)fiber sequence).** Part (2) uses TR2 to verify the pre-triangulated rotation axiom and to convert a triangle into a fiber sequence.

3. **Operation 5 from the topic page (apply $\mathcal{T}(-, W)$ / $\mathcal{T}(W, -)$).** Part (2) uses the long exact sequence of a triangle to verify the pre-triangulated long-exact-sequence axiom.

---

# Hints

> [!note]- Hint 1
> An equivalence $\Sigma$ with quasi-inverse $\Sigma^{-1}$ is automatically both left and right adjoint to $\Sigma^{-1}$. So setting $\Omega = \Sigma^{-1}$ gives $\Sigma \dashv \Omega$ for free.

> [!note]- Hint 2
> The cofiber sequences are the distinguished triangles $X \to Y \to Z \to \Sigma X$. For the fiber sequences, apply $\Sigma^{-1} = \Omega$ to a triangle and rotate to put it in the form $\Omega Z \to X \to Y \to Z$.

> [!note]- Hint 3
> Pre-triangulated needs only $\Sigma \dashv \Omega$; triangulated needs $\Sigma$ to be an *equivalence*. The extra hypothesis is invertibility. Octahedral (TR4) is beyond pre-triangulated — it is the further structure triangulated has.

---

# Solution

The solution builds the pre-triangulated data from the triangulated data: $\Omega = \Sigma^{-1}$ gives the adjunction, distinguished triangles serve as both sequence classes, and TR1–TR3 supply the pre-triangulated axioms. Invertibility of $\Sigma$ is the extra hypothesis.

**Step 1: $\Omega = \Sigma^{-1}$ and $\Sigma \dashv \Omega$.**

> [!note]- Derivation
> In a triangulated category the shift $\Sigma = [1]$ is by hypothesis an **autoequivalence**, so it has a quasi-inverse $\Sigma^{-1} = [-1]$ with natural isomorphisms $\Sigma\Sigma^{-1} \cong \mathrm{id} \cong \Sigma^{-1}\Sigma$. Set $\Omega = \Sigma^{-1}$. A pair of mutually inverse equivalences is automatically an [[Def - Pointed Model Category Suspension and Loop|adjoint]] pair: the natural isomorphisms serve as unit $\eta : \mathrm{id} \xrightarrow{\cong} \Omega\Sigma$ and counit $\varepsilon : \Sigma\Omega \xrightarrow{\cong} \mathrm{id}$, and they satisfy the triangle identities (one can always choose the quasi-inverse so they do — an adjoint equivalence). Hence $\Sigma \dashv \Omega$, the first pre-triangulated ingredient. The pointed structure is the zero object of the additive category $\mathcal{T}$.

**Step 2: Distinguished triangles as both sequence classes; axioms from TR1–TR3.**

> [!note]- Derivation
> Declare the **cofiber sequences** to be the distinguished triangles $X \to Y \to Z \to \Sigma X$. Declare the **fiber sequences** to be the same triangles read through $\Omega = \Sigma^{-1}$: from a triangle $X \to Y \to Z \to \Sigma X$, apply $\Sigma^{-1}$ and rotate (TR2) to obtain $\Omega Z = \Sigma^{-1} Z \to X \to Y \to Z$, which is a fiber sequence in pre-triangulated form. Now verify the pre-triangulated axioms:
> - *Existence:* TR1 says every map $f : X \to Y$ extends to a distinguished triangle $X \to Y \to Z \to \Sigma X$, giving a cofiber sequence; applying $\Sigma^{-1}$ and rotating gives the fiber sequence. The identity triangle $X \xrightarrow{\mathrm{id}} X \to 0 \to \Sigma X$ (TR1) is the trivial cofiber sequence.
> - *Rotation:* TR2 is exactly the pre-triangulated rotation axiom, with the sign $-\Sigma f$ on the rotated map.
> - *Long exact sequences:* For any $W$, applying $\mathcal{T}(-, W)$ to a distinguished triangle yields a long exact sequence of abelian groups (standard consequence of TR1–TR3); this is the pre-triangulated cofiber long-exact-sequence axiom. Applying $\mathcal{T}(W, -)$ to a triangle yields the dual long exact sequence, which under the $\Sigma^{-1}$-identification is the pre-triangulated fiber long-exact-sequence axiom.
> - *Compatibility:* the cofiber and fiber classes are matched by $\Omega = \Sigma^{-1}$, so the adjunction-compatibility axiom holds trivially (the unit/counit are isomorphisms).
>
> All pre-triangulated axioms are verified, so $\mathcal{T}$ is pre-triangulated.

**Step 3: The extra hypothesis and the collapse of the classes.**

> [!note]- Derivation
> The hypothesis of "triangulated" that pre-triangulated does **not** require is that $\Sigma$ is an **equivalence**. Pre-triangulated asks only for an adjunction $\Sigma \dashv \Omega$ — with $\Sigma$ possibly non-invertible — and therefore keeps two genuinely distinct classes (cofiber and fiber sequences). When $\Sigma$ is invertible, $\Omega = \Sigma^{-1}$, and applying $\Sigma^{\pm 1}$ converts any fiber sequence into a cofiber sequence and back, so the two classes **collapse into one** class of distinguished triangles. This is exactly why a triangulated category has a single "distinguished triangle" notion rather than separate cofiber and fiber sequences: invertibility identifies them. (The octahedral axiom TR4 is a further triangulated hypothesis with no pre-triangulated counterpart; it is the coherence of *iterated* cofibers and is most naturally stated when $\Sigma$ is invertible.)

> [!note]- Complete formal solution
> **(1)** $\Sigma$ is an autoequivalence; set $\Omega = \Sigma^{-1}$. Mutually inverse equivalences are adjoint (adjoint-equivalence), giving $\Sigma \dashv \Omega$ with isomorphism unit/counit. The additive zero object makes $\mathcal{T}$ pointed.
>
> **(2)** Take distinguished triangles as cofiber sequences and their $\Sigma^{-1}$-rotations as fiber sequences. TR1 gives existence, TR2 gives rotation (with sign), the long exact sequences of $\mathcal{T}(-, W)$ and $\mathcal{T}(W, -)$ on a triangle give the long-exact-sequence axioms, and the $\Omega = \Sigma^{-1}$ identification gives compatibility. So $\mathcal{T}$ is pre-triangulated.
>
> **(3)** The extra triangulated hypothesis is invertibility of $\Sigma$; it merges the two sequence classes into one class of distinguished triangles. TR4 (octahedral) is additional structure beyond pre-triangulated. $\blacksquare$

---

# Key Takeaways

**Pre-triangulated is genuinely weaker, and the witness is the number of sequence classes.** A triangulated category has one notion of distinguished triangle; a pre-triangulated category has two, cofiber and fiber. This is not redundancy in the triangulated case — it is the *consequence* of invertibility, which lets $\Sigma^{\pm 1}$ translate between them. The transferable insight is that whenever a structure has "one shifted exact sequence" it is because a shift functor is invertible, and whenever it has "two dual sequences" the shift is merely adjoint. Counting the sequence classes is a quick read on whether you are in the stable (triangulated) or unstable (pre-triangulated) world.

**Mutually inverse equivalences are adjoint, and this is why invertibility gives the adjunction for free.** The fact that $\Sigma \dashv \Sigma^{-1}$ holds automatically for an autoequivalence is the cleanest instance of a general principle: an equivalence is both a left and a right adjoint to its quasi-inverse. The reusable diagnostic is that any time you have an invertible functor, you have an adjunction in both directions at no cost, so the suspension–loop adjunction is trivially present in the stable case. Conversely, the *content* of the suspension–loop adjunction theorem is entirely in the unstable case, where $\Sigma$ is not invertible and the adjunction must be proved by the homotopy-(co)limit argument rather than read off invertibility.

**The octahedral axiom is the one piece of triangulated structure with no pre-triangulated shadow.** TR4 governs the compatibility of *iterated* cofibers — the cofiber of a composite versus the cofibers of the factors — and it is the deepest and least intuitive triangulated axiom. That it does not appear in the pre-triangulated definition tells you it is genuinely extra, and it is the axiom that makes triangulated categories support Verdier localization and the theory of t-structures. The takeaway is that "pre-triangulated plus $\Sigma$ invertible" is not *quite* triangulated until one also imposes the octahedral coherence; the model-category chapter establishes everything up to TR4, and TR4 is verified separately in the stable setting where iterated cofibers are well-behaved.
