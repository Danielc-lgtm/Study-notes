---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - fc-Multicategory"
  - "Def - Monoidal Category"
  - "Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $(\mathcal{V}, \otimes, I)$ be a [[Def - Monoidal Category|monoidal category]]. Construct an [[Def - fc-Multicategory|fc-multicategory]] $\widehat{\mathcal{V}}$ with one object, only the identity vertical $1$-cell, and horizontal $1$-cells equal to the objects of $\mathcal{V}$, whose $2$-cells are
$$\widehat{\mathcal{V}}\big((X_1, \dots, X_n) \Rightarrow Y\big) := \mathcal{V}(X_1 \otimes \cdots \otimes X_n,\, Y).$$
Show that this is a *representable* fc-multicategory in which the universal composite of the string $(X_1, \dots, X_n)$ is $X_1 \otimes \cdots \otimes X_n$, that the empty string is represented by $I$, and that the associator of $\mathcal{V}$ is recovered as the canonical isomorphism between the two representing objects of a triple, by uniqueness of representing objects. Conversely, argue that every one-object, vertically-trivial, representable fc-multicategory arises this way.

**Recall:**

![[Def - fc-Multicategory#The Definition]]

A **[[Def - Monoidal Category|monoidal category]]** $(\mathcal{V}, \otimes, I)$ is a category with a tensor functor $\otimes : \mathcal{V}\times\mathcal{V}\to\mathcal{V}$, a unit object $I$, and natural isomorphisms (associator) $a_{X,Y,Z} : (X\otimes Y)\otimes Z \xrightarrow{\cong} X\otimes(Y\otimes Z)$ and (unitors) $l_X : I\otimes X\xrightarrow{\cong} X$, $r_X : X\otimes I\xrightarrow{\cong} X$, satisfying the pentagon and triangle coherence axioms. A horizontal $1$-cell in an fc-multicategory has a universal composite when there is a $2$-cell out of the string through which all others factor uniquely.

---

# Convergent Strategy

**Problem class:** A *template-identification plus coherence-for-free* problem: build the fc-multicategory and then show its coherence is *inherited* rather than checked, following the topic page's strategy of producing associators from uniqueness of representing objects (legal operation 3).

**Assumption pattern:** Two dials are set — one object and trivial vertical structure — so $\widehat{\mathcal{V}}$ has only horizontal $1$-cells (the objects of $\mathcal{V}$) and string-topped $2$-cells. The decisive extra input is that $\mathcal{V}$ *has* a tensor, which is what makes every string *representable*: $X_1\otimes\cdots\otimes X_n$ together with the identity map is the universal $2$-cell out of $(X_1,\dots,X_n)$.

**Theorem routing:** This is the one-object case of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories|the subsumption theorem]] (its part 2), routed through Lemma 2 of that theorem (uniqueness of representing objects, which manufactures the associator) and Lemma 3 (the delooping identification). The exercise verifies the construction explicitly and shows the associator emerges from uniqueness.

**Key decision point:** The non-obvious move is to *define* the $2$-cells via the tensor — $\widehat{\mathcal{V}}((X_1,\dots,X_n)\Rightarrow Y) = \mathcal{V}(X_1\otimes\cdots\otimes X_n, Y)$ — and then *recover* the associator from the fact that $(X_1\otimes X_2)\otimes X_3$ and $X_1\otimes(X_2\otimes X_3)$ both represent the string $(X_1, X_2, X_3)$. The tempting alternative — defining the $2$-cells and then *postulating* an associator — misses the point: the associator is forced, not added.

---

# Legal Operations Used

1. **Operation 1 (set the four dials).** One object and trivial vertical structure place $\widehat{\mathcal{V}}$ in the monoidal/multicategory corner; representability lifts it to monoidal.

2. **Operation 2 (replace a chosen composite by a universal $2$-cell out of a string).** The tensor $X_1\otimes\cdots\otimes X_n$ is re-encoded as the representing object of the string.

3. **Operation 3 (uniqueness of representing objects gives the associator).** The associator $a$ is the unique iso between the two bracketings, both representing the triple.

4. **Operation 8 (empty string for the unit).** The length-zero string is represented by $I$.

---

# Hints

> [!note]- Hint 1
> First check $\widehat{\mathcal{V}}$ is an fc-multicategory at all: define substitution of $2$-cells using composition in $\mathcal{V}$ and the functoriality of $\otimes$. A $2$-cell over $(X_1,\dots,X_n)$ is a map $X_1\otimes\cdots\otimes X_n\to Y$; substituting maps $\bigotimes S_i\to X_i$ gives, after tensoring, a map $\bigotimes(S_1\cdots S_n)\to Y$.

> [!note]- Hint 2
> To show the string $(X_1,\dots,X_n)$ is *representable*, you must produce a $2$-cell $\iota$ out of it through which every other factors uniquely. Take $p = X_1\otimes\cdots\otimes X_n$ and $\iota =$ the identity map $X_1\otimes\cdots\otimes X_n\to X_1\otimes\cdots\otimes X_n$. Why does every $2$-cell factor uniquely through it?

> [!note]- Hint 3
> A $2$-cell out of $(X_1, X_2, X_3)$ is a map $X_1\otimes X_2\otimes X_3\to Y$; but "$X_1\otimes X_2\otimes X_3$" is ambiguous in a monoidal category — there is $(X_1\otimes X_2)\otimes X_3$ and $X_1\otimes(X_2\otimes X_3)$. Both represent the *same* string, so by uniqueness of representing objects they are canonically isomorphic. Identify that iso.

---

# Solution

The route has three steps: build $\widehat{\mathcal{V}}$, prove every string (including the empty one) is representable by the tensor, and extract the associator from uniqueness of representing objects.

**Step 1: $\widehat{\mathcal{V}}$ is an fc-multicategory.**

> [!note]- Derivation
> One object $\ast$; only the vertical identity $1_\ast$; horizontal $1$-cells $\ast\nrightarrow\ast$ are the objects of $\mathcal{V}$; and $\widehat{\mathcal{V}}((X_1,\dots,X_n)\Rightarrow Y) = \mathcal{V}(X_1\otimes\cdots\otimes X_n, Y)$, with the convention that the empty tensor is $I$, so $\widehat{\mathcal{V}}((\,)\Rightarrow Y) = \mathcal{V}(I, Y)$. Substitution: given $\theta : X_1\otimes\cdots\otimes X_n\to Y$ and, for each $i$, $\theta_i : \bigotimes S_i \to X_i$, form $\theta\circ(\theta_1\otimes\cdots\otimes\theta_n) : \bigotimes(S_1\cdots S_n)\to Y$ using functoriality of $\otimes$ and the canonical iso $\bigotimes(S_1\cdots S_n)\cong (\bigotimes S_1)\otimes\cdots\otimes(\bigotimes S_n)$ from the associator. The identity $2$-cell $1_X$ is $\mathrm{id}_X : X\to X$. Associativity of substitution and the unit laws hold because composition in $\mathcal{V}$ is associative/unital and $\otimes$ is coherent (the pentagon makes the re-bracketing isos agree). So $\widehat{\mathcal{V}}$ is an fc-multicategory.

**Step 2: Every string is represented by its tensor; the empty string by $I$.**

> [!note]- Derivation
> Fix a string $(X_1,\dots,X_n)$. Take $p := X_1\otimes\cdots\otimes X_n$ and $\iota := \mathrm{id}_p \in \widehat{\mathcal{V}}((X_1,\dots,X_n)\Rightarrow p)$. A general $2$-cell out of the string is a map $\theta : X_1\otimes\cdots\otimes X_n\to Y$, and it factors as $\theta = \bar\theta\circ\iota$ where $\bar\theta := \theta : p\to Y$ — uniquely, since $\iota$ is the identity and any $\bar\theta'$ with $\bar\theta'\circ\iota = \theta$ equals $\theta$. So $\iota$ is universal: $(p, \iota)$ represents the string. For $n=0$: $p = I$ and a $2$-cell out of the empty string is a map $I\to Y$, factoring uniquely through $\mathrm{id}_I$. Hence $\widehat{\mathcal{V}}$ is *representable*, with composites given by $\otimes$ and unit by $I$.

**Step 3: The associator is the unique iso between two representing objects.**

> [!note]- Derivation
> Consider the triple $(X_1, X_2, X_3)$. Both $(X_1\otimes X_2)\otimes X_3$ and $X_1\otimes(X_2\otimes X_3)$ represent this string: each is a tensor of the three objects (the first by tensoring $(X_1\otimes X_2)$ with $X_3$, the second by tensoring $X_1$ with $(X_2\otimes X_3)$), and each comes with its canonical universal $2$-cell. By Lemma 2 of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories|the subsumption theorem]] (uniqueness of representing objects), there is a *unique* invertible $2$-cell between them commuting with the universal $2$-cells. That unique iso is exactly the associator $a_{X_1,X_2,X_3} : (X_1\otimes X_2)\otimes X_3\xrightarrow{\cong} X_1\otimes(X_2\otimes X_3)$. The pentagon is then automatic: all bracketings of a quadruple represent the same string, so all comparison isos between them are unique, forcing the pentagon to commute. Likewise the unitors come from the two ways the empty string interacts with a singleton, recovering $l, r$ and the triangle.

> [!note]- Complete formal solution
> Given a monoidal category $(\mathcal{V},\otimes,I)$, define $\widehat{\mathcal{V}}$: one object $\ast$, only vertical identity, horizontal $1$-cells $=$ objects of $\mathcal{V}$, and $\widehat{\mathcal{V}}((X_1,\dots,X_n)\Rightarrow Y)=\mathcal{V}(X_1\otimes\cdots\otimes X_n,Y)$ (empty tensor $=I$). Substitution is composition in $\mathcal{V}$ combined with $\otimes$ and the coherence isos; the pentagon/triangle of $\mathcal{V}$ give associativity/unitality of substitution, so $\widehat{\mathcal{V}}$ is an fc-multicategory. For each string, $(X_1\otimes\cdots\otimes X_n, \mathrm{id})$ is a universal $2$-cell (every $\theta$ factors uniquely as $\theta\circ\mathrm{id}$), so $\widehat{\mathcal{V}}$ is representable with composites $\otimes$ and unit $I$. By uniqueness of representing objects, the two bracketings of a triple are canonically isomorphic, and that iso is $a$; the pentagon follows from uniqueness over quadruples, the unitors from the empty string, the triangle from uniqueness. Conversely, given a one-object, vertically-trivial, representable fc-multicategory $\mathcal{C}$, set $\mathcal{V}$ to have objects the horizontal $1$-cells, morphisms $X\to Y$ the $2$-cells $(X)\Rightarrow Y$, tensor the chosen representing object of $(X,Y)$, and unit the representing object of the empty string; representability and uniqueness furnish $a,l,r$ and the coherence, so $\mathcal{V}$ is monoidal and $\widehat{\mathcal{V}}\cong\mathcal{C}$. The two constructions are mutually inverse. $\blacksquare$

---

# Key Takeaways

**Coherence is inherited from representability, never postulated.** The deep lesson of this exercise is that the associator of a monoidal category is not extra structure you bolt on — it is *forced* by the universal property of the tensor as a representing object. Once you define $2$-cells via $\otimes$ and observe that $(X_1\otimes X_2)\otimes X_3$ and $X_1\otimes(X_2\otimes X_3)$ both represent the *same* string, uniqueness of representing objects delivers the associator with no choice, and the pentagon with no computation. The transferable diagnostic: whenever you face an associativity isomorphism, look for a universal object that the two sides both represent; the iso is then unique, and its coherence is automatic. This is legal operation 3 of the topic page, and it is the single most labour-saving move in the chapter.

**The tensor is "the composite of a string", and that reframing organises monoidal coherence.** A monoidal category looks like it has a binary operation $\otimes$ with associativity glue. The fc-multicategory reframing says: $\otimes$ is the *representing object of a length-two string*, the $n$-fold tensor is the representing object of a length-$n$ string, and the unit is the representing object of the empty string. Under this reframing, [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]] becomes nearly trivial — all bracketings represent the same string and so are uniquely isomorphic. The trigger to internalise: "$n$-fold tensor" $\leftrightarrow$ "representing object of a length-$n$ string". This is exactly why one-object representable fc-multicategories *are* monoidal categories.

**The empty string carries the unit, and getting it right is what makes the correspondence exact.** As in [[Ex - A multicategory is a one-object fc-multicategory]], the length-zero layer is load-bearing: the empty string is represented by $I$, and the maps $I\to Y$ are the elements/global points of $\mathcal{V}$-objects. If you only handled positive arities you would build a *non-unital* monoidal category and lose $I$. The recurring principle across this chapter is that units live in the empty-string/empty-tensor layer; any construction that forgets $n=0$ silently amputates the unit object. Together with the previous takeaway, this shows the four-dial picture is not a slogan but a precise, verifiable correspondence at the level of data and coherence.
