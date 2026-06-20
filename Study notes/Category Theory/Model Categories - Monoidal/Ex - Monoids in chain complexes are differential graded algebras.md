---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Module over a Monoidal Model Category"
  - "Def - Monoid in a Monoidal Category"
  - "Def - Closed Monoidal Category"
  - "Def - Chain Map and Chain Homotopy"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a commutative ring and $(\mathbf{Ch}(R), \otimes_R, R)$ the closed monoidal category of chain complexes. Show that a [[Def - Monoid in a Monoidal Category|monoid]] in $\mathbf{Ch}(R)$ is exactly a **differential graded $R$-algebra** (DGA): a graded $R$-algebra $A = \bigoplus_n A_n$ with a differential $d : A_n \to A_{n-1}$ satisfying $d^2 = 0$ and the graded Leibniz rule
$$d(ab) = (da)b + (-1)^{|a|} a\,(db).$$
Show that a [[Def - Module over a Monoidal Model Category|module]] over such a monoid is exactly a differential graded $A$-module. Identify the unit $\eta : R \to A$ and explain why the Leibniz rule is *forced* by the requirement that the multiplication $\mu : A \otimes_R A \to A$ be a chain map.

**Recall:**

A [[Def - Monoid in a Monoidal Category|monoid]] in a monoidal category $(\mathcal{C}, \otimes, I)$ is an object $A$ with $\mu : A \otimes A \to A$ and $\eta : I \to A$ satisfying associativity and the unit laws.

In $\mathbf{Ch}(R)$, the tensor product has $(A \otimes_R A)_n = \bigoplus_{p+q=n} A_p \otimes_R A_q$ with differential $d(x \otimes y) = dx \otimes y + (-1)^{|x|} x \otimes dy$ (the Koszul sign). The unit is $R$ concentrated in degree $0$.

![[Def - Chain Map and Chain Homotopy#The Definition]]

---

# Convergent Strategy

**Problem class:** This is an *unwinding-a-definition* problem: take the abstract definition of a monoid in a monoidal category and compute what it says concretely when the monoidal category is $\mathbf{Ch}(R)$. It is the algebraic half of "doing algebra inside a monoidal (model) category" from the topic page, with no homotopy theory yet — just the monoid/module structure.

**Assumption pattern:** The key assumption is the form of the tensor differential on $\mathbf{Ch}(R)$, *with its Koszul sign*. The whole content of "monoid = DGA" is that the chain-map condition on $\mu$, expanded through that sign, *is* the graded Leibniz rule. The second assumption is that morphisms in $\mathbf{Ch}(R)$ are chain maps, so "$\mu$ and $\eta$ are morphisms" means "$\mu$ and $\eta$ are chain maps".

**Theorem routing:** There is no theorem to invoke beyond the [[Def - Monoid in a Monoidal Category|definition of a monoid]] and the [[Def - Chain Map and Chain Homotopy|definition of a chain map]]; the route is to substitute the explicit tensor differential into the chain-map equation $d \circ \mu = \mu \circ d$ and read off the Leibniz rule, then substitute into the action equation for modules.

**Key decision point:** The non-obvious recognition is that the *sign* in the Leibniz rule is not a separate axiom one must add to "associative graded multiplication"; it is *produced* by the Koszul sign in the tensor differential the moment you demand $\mu$ be a chain map. The decision is to expand $d(\mu(a \otimes b))$ versus $\mu(d(a \otimes b))$ rather than to posit the Leibniz rule by hand — the exercise is to *derive* it.

---

# Legal Operations Used

1. **Operation 1-analogue (do algebra in a monoidal category), topic page.** We transcribe "ring" and "module" into a monoidal category by replacing the underlying multiplication with $\mu : A \otimes A \to A$ and reading off what the monoid axioms become concretely.

2. **Operation (reduce to chain-map conditions).** "$\mu, \eta$ are morphisms of $\mathbf{Ch}(R)$" is unwound to "$\mu, \eta$ are chain maps", and the chain-map equations are expanded using the explicit tensor differential.

---

# Hints

> [!note]- Hint 1
> A monoid in $\mathbf{Ch}(R)$ is an object $A$ (a complex) with morphisms $\mu : A \otimes_R A \to A$ and $\eta : R \to A$. What does "morphism of $\mathbf{Ch}(R)$" mean? It means *chain map*.

> [!note]- Hint 2
> Write out $\mu$ being a chain map: $d_A(\mu(a \otimes b)) = \mu(d_{A \otimes A}(a \otimes b))$. Substitute the Koszul-sign tensor differential on the right.

> [!note]- Hint 3
> Writing $\mu(a \otimes b) = ab$, the equation becomes $d(ab) = (da)b + (-1)^{|a|} a (db)$ — the graded Leibniz rule, now *forced*, not assumed.

> [!note]- Hint 4
> For modules: a module is $M$ with an action $a : A \otimes_R M \to M$. Unwind the chain-map condition on the action the same way to get $d(am) = (da)m + (-1)^{|a|} a(dm)$, the DG-module compatibility.

---

# Solution

The route is: (1) unwind "monoid in $\mathbf{Ch}(R)$" to a complex with chain-map multiplication and unit; (2) expand the chain-map condition on $\mu$ using the Koszul tensor differential to *derive* the Leibniz rule; (3) note associativity and unit are degreewise the algebra axioms; (4) repeat for modules. The signs are produced, not posited.

**Step 1: A monoid is a complex with associative, unital multiplication.**

> [!note]- Derivation
> A [[Def - Monoid in a Monoidal Category|monoid]] in $\mathbf{Ch}(R)$ is a complex $A = (A_\bullet, d)$ together with chain maps $\mu : A \otimes_R A \to A$ and $\eta : R \to A$ satisfying associativity $\mu \circ (\mu \otimes 1) = \mu \circ (1 \otimes \mu)$ and the unit laws $\mu \circ (\eta \otimes 1) = \mathrm{id} = \mu \circ (1 \otimes \eta)$ (via the unitors). Writing $\mu(a \otimes b) = ab$: associativity says $(ab)c = a(bc)$, and $\eta$ picks out an element $1 = \eta(1_R) \in A_0$ with $1 \cdot a = a = a \cdot 1$. Since $\mu$ has degree $0$, $A_p \cdot A_q \subseteq A_{p+q}$: the multiplication is graded. So far this is a *graded associative unital $R$-algebra* structure on $A$.

**Step 2: The chain-map condition on $\mu$ forces the graded Leibniz rule.**

> [!note]- Derivation
> $\mu$ being a [[Def - Chain Map and Chain Homotopy|chain map]] means $d_A \circ \mu = \mu \circ d_{A \otimes_R A}$. The tensor differential is $d_{A \otimes_R A}(a \otimes b) = (da) \otimes b + (-1)^{|a|} a \otimes (db)$. Apply both sides to $a \otimes b$:
> $$d_A(\mu(a \otimes b)) = \mu\big(d_{A\otimes A}(a \otimes b)\big) = \mu\big((da)\otimes b + (-1)^{|a|} a \otimes (db)\big).$$
> Writing $\mu(x \otimes y) = xy$, the left side is $d(ab)$ and the right side is $(da)b + (-1)^{|a|} a(db)$. Hence
> $$d(ab) = (da)\,b + (-1)^{|a|}\, a\,(db),$$
> the **graded Leibniz rule**. It is not an extra axiom; it is exactly the statement that $\mu$ commutes with the differentials, with the sign inherited from the Koszul sign in the tensor differential. Together with $d^2 = 0$ (already true on $A$) and the graded associative unital structure, this is the definition of a **differential graded $R$-algebra**.

**Step 3: Modules over the monoid are DG-modules.**

> [!note]- Derivation
> A [[Def - Module over a Monoidal Model Category|module]] over the monoid $A$ is a complex $M$ with a chain map action $\alpha : A \otimes_R M \to M$, $\alpha(a \otimes m) = am$, satisfying $\alpha \circ (\mu \otimes 1) = \alpha \circ (1 \otimes \alpha)$ (associativity of the action: $(ab)m = a(bm)$) and $\alpha \circ (\eta \otimes 1) = \mathrm{id}$ ($1 \cdot m = m$). The chain-map condition on $\alpha$, expanded with the tensor differential exactly as in Step 2, gives
> $$d(am) = (da)\,m + (-1)^{|a|}\, a\,(dm),$$
> the compatibility of the action with the differentials. This is precisely a **differential graded $A$-module**. So $\mathbf{Mod}_A$ in the sense of this chapter is the category of DG $A$-modules.

> [!note]- Complete formal solution
> A [[Def - Monoid in a Monoidal Category|monoid]] in $\mathbf{Ch}(R)$ is a complex $A$ with chain maps $\mu : A \otimes_R A \to A$, $\eta : R \to A$, associative and unital. Degreewise, $\mu$ makes $A$ a graded associative unital $R$-algebra ($A_p A_q \subseteq A_{p+q}$, unit $1 = \eta(1_R) \in A_0$). The condition that $\mu$ is a [[Def - Chain Map and Chain Homotopy|chain map]], $d_A \mu = \mu\, d_{A \otimes_R A}$, expanded with the Koszul-sign tensor differential $d(a \otimes b) = da \otimes b + (-1)^{|a|} a \otimes db$, yields $d(ab) = (da)b + (-1)^{|a|} a(db)$ — the graded Leibniz rule, forced by chain-map-ness. With $d^2 = 0$, $A$ is a differential graded $R$-algebra. Identically, a module $M$ over $A$ is a complex with chain-map action satisfying $d(am) = (da)m + (-1)^{|a|} a(dm)$, i.e. a DG $A$-module. The unit $\eta : R \to A$ is the inclusion of $R$ as the scalar multiples of $1 \in A_0$. $\qquad\blacksquare$

---

# Key Takeaways

**"Monoid in a monoidal category" is a single template that specializes to ring, DGA, ring spectrum, and operad-algebra by changing the ambient category.** This exercise is the calibration case: in $\mathbf{Ab}$ a monoid is a ring; in $\mathbf{Ch}(R)$ it is a DGA; in spectra it is a ring spectrum; in $\mathbf{Cat}$ it is a strict monoidal category. The transferable diagnostic is that whenever you meet a notion of "algebra object" in a new monoidal category, you do not invent new axioms — you write down $\mu$ and $\eta$, demand they be morphisms, and unwind. The *new* content is always exactly what "being a morphism" imposes: here, the chain-map condition, which manufactures the Leibniz rule. The richness of differential graded algebra is, structurally, just ordinary algebra done in $\mathbf{Ch}(R)$ instead of $\mathbf{Ab}$.

**Compatibility conditions that look like extra axioms are often forced by demanding structure maps be morphisms — derive them, do not memorize them.** The graded Leibniz rule is the headline example: students often learn it as a separate axiom of a DGA, but it is *produced* the instant you require $\mu$ to be a chain map in a category whose tensor carries the Koszul sign. The trigger-reaction pattern is: when a definition includes a "compatibility of operation with differential/topology/structure", suspect it is the morphism condition for the operation in the right category, and try to re-derive it by expanding $\mathrm{(structure)} \circ \mu = \mu \circ \mathrm{(structure)}$. This both demystifies the axiom and tells you the *correct signs*, which are the part most easily gotten wrong.

**Reading definitions through the monoidal lens is what lets the homotopy theory of this chapter attach to algebra.** The point of identifying monoids in $\mathbf{Ch}(R)$ as DGAs is that the *next* step — putting a model structure on DG $A$-modules — is then just the general [[Def - Module over a Monoidal Model Category|module-over-a-monoidal-model-category]] construction, requiring the monoid axiom. So this purely algebraic unwinding is the bridge that lets "derived categories of DGAs", "derived Morita theory", and ultimately "module spectra over ring spectra" all be instances of one homotopical construction. The reusable principle: identify your algebraic objects as monoids/modules in a monoidal category *first*, because that identification is what makes the powerful homotopical machinery apply uniformly. See also [[Ex - The internal hom of chain complexes]] and [[Ex - The derived tensor on chain complexes computes Tor]].
