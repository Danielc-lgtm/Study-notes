---
type: theorem
subject: higher-categories
prereqs:
  - "Def - fc-Multicategory"
  - "Def - Weak Double Category"
  - "Def - 2-Category and Bicategory"
  - "Def - Monoidal Category"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

$\mathcal{C}$ denotes an [[Def - fc-Multicategory|fc-multicategory]], with objects, vertical $1$-cells $f : A \to A'$, horizontal $1$-cells $m : A \nrightarrow B$, and $2$-cells $\theta : (m_1, \dots, m_n) \Rightarrow p$ whose top is a string of $n$ horizontal $1$-cells. A [[Def - 2-Category and Bicategory|bicategory]] is written $\mathcal{B}$, with $1$-cells composed by $\circ$ and $2$-cells. A [[Def - Monoidal Category|monoidal category]] is written $(\mathcal{V}, \otimes, I)$. We say an fc-multicategory has **trivial vertical structure** if its only vertical $1$-cells are identities (equivalently, its vertical category is discrete). We say it is **one-object** if it has exactly one object. The full registry is on [[Higher Categories — fc-Multicategories and Weak Double Categories]].

---

# Statement

> **Theorem (fc-multicategories subsume the standard $1$- and $2$-dimensional structures).** Let $\mathcal{C}$ be an [[Def - fc-Multicategory|fc-multicategory]]. Then:
>
> 1. **Bicategories.** [[Def - 2-Category and Bicategory|Bicategories]] are precisely the fc-multicategories with trivial vertical structure in which every string of horizontal $1$-cells has a universal composite. Equivalently, the functor sending a bicategory $\mathcal{B}$ to the fc-multicategory $\widehat{\mathcal{B}}$ — objects $=$ objects of $\mathcal{B}$, no non-identity vertical $1$-cells, horizontal $1$-cells $=$ the $1$-cells of $\mathcal{B}$, and $2$-cells $(m_1, \dots, m_n) \Rightarrow p$ given by the bicategory $2$-cells $m_n \circ \cdots \circ m_1 \Rightarrow p$ — is a full and faithful embedding of bicategories into fc-multicategories, with image the representable, vertically-trivial ones.
>
> 2. **Monoidal categories.** [[Def - Monoidal Category|Monoidal categories]] are precisely the one-object bicategories, hence precisely the one-object, vertically-trivial, representable fc-multicategories: a monoidal category $(\mathcal{V}, \otimes, I)$ corresponds to the fc-multicategory with one object $\ast$, horizontal $1$-cells $\ast \nrightarrow \ast$ equal to the objects of $\mathcal{V}$, and $2$-cells $(X_1, \dots, X_n) \Rightarrow Y$ equal to morphisms $X_1 \otimes \cdots \otimes X_n \to Y$ in $\mathcal{V}$.
>
> 3. **Double categories and multicategories.** [[Def - Weak Double Category|Weak double categories]] are exactly the representable fc-multicategories (all strings have universal composites), and plain [[Def - Multicategory|multicategories]] are exactly the one-object, vertically-trivial fc-multicategories *without* the representability requirement.

In one sentence: the fc-multicategory is a single structure with four dials — *number of objects*, *vertical structure trivial or not*, *one-object or many*, *representable or not* — and turning the dials recovers monoidal categories, bicategories, double categories, and multicategories.

---

# Motivation

Higher category theory in the 1990s suffered from a proliferation of nearly-identical definitions, each with its own coherence axioms restated by hand: a [[Def - Monoidal Category|monoidal category]] has a pentagon and a triangle; a [[Def - 2-Category and Bicategory|bicategory]] has the same pentagon and triangle one level up; a double category has interchange plus the horizontal pentagon; a [[Def - Multicategory|multicategory]] has its own associativity of substitution. The suspicion — confirmed by this theorem — is that these are not four separate coherence theories but one, refracted through different choices of "how many objects" and "is composition forced". This theorem is what makes the suspicion precise: it exhibits all four as *full subcategories* of a single category of fc-multicategories, distinguished by simple structural conditions.

The payoff is conceptual economy and a uniform coherence theory. Once you prove that the substitution of $2$-cells in an fc-multicategory is associative and unital — three lines, because it is just concatenation of strings — you have simultaneously accounted for the pentagon in a monoidal category, the pentagon in a bicategory, and the associativity of multicategory substitution, *for free*, because each is a shadow of the string-concatenation associativity. The theorem also explains *why* the same coherence diagrams keep reappearing: they are all the image of one diagram under the embeddings above. This is the organising insight of Leinster Chapter 5, and it is what justifies treating the fc-multicategory as the primitive notion and the others as derived.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypothesis is "an fc-multicategory with certain dials set", so the source question is: *which familiar structures secretly are fc-multicategories of the required kind, so that the theorem applies and tells me something?*

The first disguised source is **a monoidal category whose tensor you want to reason about coherently**. Any $(\mathcal{V}, \otimes, I)$ is a one-object, vertically-trivial, representable fc-multicategory via part (2). The bridge "$\mathcal{V}$ is such an fc-multicategory" is non-obvious because a monoidal category does not *look* like it has horizontal $1$-cells and string-topped $2$-cells — but its objects become horizontal $1$-cells and its multilinear-looking maps $X_1 \otimes \cdots \otimes X_n \to Y$ become the $2$-cells. *Example problem:* to prove a coherence statement about $n$-fold tensor products, re-read it as a statement about the length-$n$ strings in the associated fc-multicategory, where it becomes a statement about string concatenation.

The second disguised source is **a bicategory you wish to compare with a multicategory or feed into a slice construction**. By part (1), every bicategory $\mathcal{B}$ is an fc-multicategory $\widehat{\mathcal{B}}$. The bridge is non-obvious because it requires *forgetting* that horizontal composites are given and *remembering* only the universal $2$-cells representing them; once done, $\mathcal{B}$ sits inside the world where the [[Def - fc-Multicategory|fc-multicategory]] slice and opetope constructions live. *Example problem:* to define the "opetopes of a bicategory" or to compare $\mathcal{B}$ with a non-representable structure, first embed $\mathcal{B}$ via $\widehat{(-)}$.

The third disguised source is **a category-with-two-kinds-of-arrow (a double category) arising in practice** — rings/bimodules, categories/profunctors, spans. Each is a representable fc-multicategory by part (3). The bridge is that the tensor-like horizontal composition (bimodule $\otimes$, profunctor coend, span pullback) is exactly the universal composite of a string. *Example problem:* to apply a general fc-multicategory theorem (e.g. about modules, [[Thm - Monoids and Modules Form a Bicategory]]) to bimodules, recognise the bimodule double category as a representable fc-multicategory and invoke the theorem there.

**Targets (Output Amplification)**

The bare conclusion is "these four structures embed in fc-multicategories". Combined with other facts it does more.

Combine the conclusion with **a single coherence proof for fc-multicategory substitution**. Because substitution of $2$-cells is associative (it is string concatenation), and because the embeddings send composition to substitution, you get *for free* the coherence (pentagon/triangle) of monoidal categories, bicategories, and double categories. The further result $E$ is: one three-line lemma about $\mathrm{fc}$ implies four classical coherence theorems. This is non-obvious because the classical proofs (Mac Lane's, the bicategory version) are long; routing them through fc-multicategories trivialises the *associativity* core, leaving only the representability bookkeeping.

Combine the conclusion with **the slice construction on generalized multicategories**. Since bicategories and monoidal categories are now fc-multicategories, the slice (which produces opetopes) applies to them. The further result is a uniform definition of the higher cells of these structures — the opetopic shapes — without separate combinatorial definitions for each. This combination powers Leinster's opetopic chapter.

Combine the conclusion with **representability as a detector**. Given any fc-multicategory, *testing* whether all strings are representable decides whether it is a weak double category; testing additionally for one object and trivial vertical structure decides whether it is a monoidal category or bicategory. The further result $E$ is a decision procedure: to classify what kind of higher structure you are holding, check the four dials. This turns a taxonomy question into a checklist.

---

# Why Is It True

The theorem feels surprising only until you notice that all four target structures are built from *the same combinatorial atom*: a way of composing a string of cells into one cell. A [[Def - Monoidal Category|monoidal category]] composes a string of objects $X_1, \dots, X_n$ into $X_1 \otimes \cdots \otimes X_n$. A [[Def - 2-Category and Bicategory|bicategory]] composes a string of $1$-cells $m_1, \dots, m_n$ into $m_n \circ \cdots \circ m_1$. A [[Def - Weak Double Category|double category]] composes a string of horizontal $1$-cells via $\odot$. A [[Def - Multicategory|multicategory]] *records* maps out of a string without composing it. The fc-multicategory's $2$-cells are, by construction, "maps out of a string", so each of these structures is captured by saying which strings have *representing* maps (universal composites) and how many objects and vertical $1$-cells there are.

**The single mechanism: the four classical structures are the fc-multicategory with its "string composer" turned on (representability) or off (multicategory), and its object/vertical dials set; the free-category monad $\mathrm{fc}$ supplies the strings, and everything else is bookkeeping.** Once you see that "the top of a $2$-cell is a path" is the defining feature, the embeddings write themselves: a bicategory $2$-cell $m_n \circ \cdots \circ m_1 \Rightarrow p$ is the same datum as an fc-multicategory $2$-cell $(m_1, \dots, m_n) \Rightarrow p$, because the bicategory has already chosen the composite $m_n \circ \cdots \circ m_1$ and the universal property of that composite says exactly that maps out of it correspond to maps out of the string. The monoidal case is the one-object specialisation, where horizontal $1$-cells degenerate to objects of $\mathcal{V}$ and the tensor is the string composer.

The reason the coherence comes for free is that string concatenation is *strictly* associative: $(S_1 S_2) S_3 = S_1 (S_2 S_3)$ as paths, no isomorphism needed. All the *weakness* of monoidal/bicategorical composition is pushed into the *representing objects*: the composite $X_1 \otimes (X_2 \otimes X_3)$ and $(X_1 \otimes X_2) \otimes X_3$ both represent the *same* string $(X_1, X_2, X_3)$, so they are canonically isomorphic by the uniqueness of representing objects — and that canonical isomorphism *is* the associator. The pentagon is then automatic because representing objects are unique up to unique iso. This is the deep reason the classical pentagon is "really" the strict associativity of concatenation seen through a representability mirror.

---

# What Makes This Hard

The non-obvious step is the *re-encoding of a chosen composite as a universal property of a string*: a bicategory's $1$-cell composite $m_n \circ \cdots \circ m_1$ must be recognised as the representing object of the string $(m_1, \dots, m_n)$, so that its $2$-cells out match the fc-multicategory $2$-cells out of the string. Most people stumble by trying to make the embedding send $2$-cells $m_i \Rightarrow m_i'$ directly, forgetting that the fc-multicategory's $2$-cells live over *whole strings*, not single horizontal $1$-cells. The second common error is mishandling the empty string ($n=0$): it must map to the unit (monoidal unit $I$, or horizontal unit $\mathrm{U}_A$), and forgetting it amputates the unit object and breaks the unitor coherence.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build the embedding functor in each case by declaring the fc-multicategory data from the classical data, with the key clause "$2$-cells over a string $=$ classical maps out of the composite of that string". Then check the embedding is full and faithful by the universal property of the classical composite, and identify the image as the fc-multicategories satisfying the stated dial conditions (vertically trivial, one-object, representable as appropriate).

**Subgoal decomposition:**

1. **Bicategory $\to$ fc-multicategory.** From a bicategory $\mathcal{B}$ define $\widehat{\mathcal{B}}$: same objects, only identity vertical $1$-cells, horizontal $1$-cells $=$ $1$-cells of $\mathcal{B}$, and $2$-cells $(m_1, \dots, m_n) \Rightarrow p$ $:=$ bicategory $2$-cells $m_n \circ \cdots \circ m_1 \Rightarrow p$ (with the empty string sent to the identity $1$-cell).
   - *Hint:* Define substitution of $\widehat{\mathcal{B}}$-$2$-cells using horizontal composition and the associator of $\mathcal{B}$; the strict associativity of string concatenation matches the coherent associativity of $\circ$.
   - *Why needed:* This is the object map of the embedding; everything else verifies it.

2. **The embedding is full and faithful.** Show that fc-multicategory morphisms $\widehat{\mathcal{B}} \to \widehat{\mathcal{B}'}$ correspond exactly to (homo)morphisms of bicategories $\mathcal{B} \to \mathcal{B}'$.
   - *Hint:* A morphism must respect strings; on length-one strings it is a map of $1$-cells, and on longer strings it is forced by the composite's universal property, so no extra data and no missing data.
   - *Why needed:* Fullness-and-faithfulness is what makes "subsume" mean "embed", not merely "relate".

3. **Characterise the image (representability).** Show $\widehat{\mathcal{B}}$ is exactly a vertically-trivial fc-multicategory in which every string has a universal composite, and conversely any such fc-multicategory is $\widehat{\mathcal{B}}$ for a unique $\mathcal{B}$.
   - *Hint:* "Every string representable" lets you *define* $m_n \circ \cdots \circ m_1$ as the representing object, recovering $\mathcal{B}$.
   - *Why needed:* It pins the image precisely, turning the embedding into an equivalence onto its image.

4. **Specialise to one object (monoidal).** Repeat with one object: horizontal $1$-cells become objects of $\mathcal{V}$, the string composer becomes $\otimes$, the representing-object iso becomes the associator.
   - *Hint:* A one-object bicategory is a monoidal category — this is the classical "delooping" — so part (1) restricts to part (2).
   - *Why needed:* It deduces the monoidal statement from the bicategory statement rather than re-proving it.

5. **Drop representability (multicategory) and keep vertical structure (double category).** Observe that omitting "all strings representable" from the one-object, vertically-trivial case gives exactly a plain multicategory, and keeping representability but allowing vertical $1$-cells gives a weak double category.
   - *Hint:* Compare directly with the definitions of [[Def - Multicategory|multicategory]] and [[Def - Weak Double Category|weak double category]].
   - *Why needed:* It completes the four-dial picture.

---

# Lemma Decomposition

> [!note]- Lemma 1: Substitution in $\widehat{\mathcal{B}}$ is associative and unital
> **Statement:** With $\widehat{\mathcal{B}}$ defined as in subgoal 1, the substitution composition of $2$-cells is associative and unital, so $\widehat{\mathcal{B}}$ is a genuine [[Def - fc-Multicategory|fc-multicategory]].
>
> **Hint:** Concatenation of strings is strictly associative; the only weakness is in re-bracketing the bicategory composites, which is handled coherently by the associator of $\mathcal{B}$ and its pentagon.
>
> **Why needed:** Without this, $\widehat{\mathcal{B}}$ is not an fc-multicategory and the embedding has no codomain.
>
> > [!note]- Full proof
> > A $2$-cell of $\widehat{\mathcal{B}}$ over $(m_1, \dots, m_n)$ with bottom $p$ is a bicategory $2$-cell $\theta : m_n \circ \cdots \circ m_1 \Rightarrow p$. Given inner $2$-cells $\theta_i : (S_i) \Rightarrow m_i$, i.e. $\theta_i : \big(\textstyle\prod S_i\big) \Rightarrow m_i$ where $\prod S_i$ is the bicategory composite of the string $S_i$, their substitute is the bicategory composite
> > $$\theta \cdot \big( (\theta_n) \circ \cdots \circ (\theta_1) \big) : \textstyle\prod(S_1 \cdots S_n) \Rightarrow p,$$
> > using horizontal composition $\ast$ of the $\theta_i$ and the canonical iso $\prod(S_1\cdots S_n) \cong (\prod S_n)\circ\cdots\circ(\prod S_1)$ from the associator. Associativity of substitution reduces to: (i) strict associativity of string concatenation $(S_1 S_2)S_3 = S_1(S_2 S_3)$, and (ii) coherence of the re-bracketing isos, which is the [[Thm - Mac Lane Coherence Theorem|pentagon]] for $\mathcal{B}$. The unit $1_m$ is the identity $2$-cell $\mathrm{id} : m \Rightarrow m$ of $\mathcal{B}$ on the length-one string; the unit laws are the unitor coherence of $\mathcal{B}$. $\square$

> [!note]- Lemma 2: A universal composite of a string is unique up to unique isomorphism
> **Statement:** In any fc-multicategory, if $(p, \iota)$ and $(p', \iota')$ both represent a string $(m_1, \dots, m_n)$ (i.e. each $\iota, \iota'$ is universal among $2$-cells out of the string), then there is a unique invertible $2$-cell $p \Rightarrow p'$ commuting with $\iota, \iota'$.
>
> **Hint:** The standard "uniqueness of representing objects" argument: factor $\iota$ through $\iota'$ and vice versa, then use uniqueness of the factorisations to see the round trips are identities.
>
> **Why needed:** This is the engine that turns representability into the associator and unitors, so that representable fc-multicategories are exactly weak double categories / bicategories with coherent composition.
>
> > [!note]- Full proof
> > By universality of $\iota'$, the $2$-cell $\iota$ factors uniquely as $\iota = u \cdot \iota'$ for a $2$-cell $u : p' \Rightarrow p$; by universality of $\iota$, $\iota' = v \cdot \iota$ for a unique $v : p \Rightarrow p'$. Then $\iota = u \cdot v \cdot \iota$, and by the uniqueness clause of $\iota$'s universal property (the only $2$-cell $w$ with $\iota = w \cdot \iota$ is $w = 1_p$), $u \cdot v = 1_p$; symmetrically $v \cdot u = 1_{p'}$. So $v$ is the required unique invertible $2$-cell. $\square$

> [!note]- Lemma 3: One object $\Leftrightarrow$ monoidal, given trivial vertical structure and representability
> **Statement:** A one-object, vertically-trivial, representable fc-multicategory is the same as a [[Def - Monoidal Category|monoidal category]], with horizontal $1$-cells as objects, the string composer as $\otimes$, and the empty-string composite as $I$.
>
> **Hint:** This is "delooping": a one-object bicategory is a monoidal category, and part (1) identifies one-object representable vertically-trivial fc-multicategories with one-object bicategories.
>
> **Why needed:** It deduces statement (2) from statement (1), avoiding a separate proof of the monoidal coherence.
>
> > [!note]- Full proof
> > With one object $\ast$, the horizontal $1$-cells $\ast \nrightarrow \ast$ form a class $\mathcal{V}_0$; representability gives, for each pair, a composite $X \otimes Y$ (the representing object of the length-two string $(X,Y)$), and for the empty string a unit $I$. A $2$-cell $(X_1, \dots, X_n) \Rightarrow Y$ is, by representability, the same as a morphism $X_1 \otimes \cdots \otimes X_n \to Y$; in particular length-one $2$-cells $(X) \Rightarrow Y$ are morphisms $X \to Y$, making $\mathcal{V}$ a [[Def - Category|category]]. Lemma 2 supplies the associator (from the two ways of bracketing a triple as representing objects) and the unitors (from $I$), and their coherence is the pentagon/triangle, which hold by Lemma 1. Conversely a monoidal category yields such an fc-multicategory by part (2). $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — what must be produced.** For each of the four classical structures we must exhibit (a) a construction turning the classical data into an fc-multicategory, (b) the verification that it *is* an fc-multicategory, (c) full-faithfulness of the resulting functor, and (d) an intrinsic characterisation of the image by the dial conditions. We treat the bicategory case in full; the others follow by specialisation.
>
> **Step 1 — the functor $\widehat{(-)}$ on bicategories.** Let $\mathcal{B}$ be a bicategory. Define $\widehat{\mathcal{B}}$: objects $=$ objects of $\mathcal{B}$; vertical $1$-cells $=$ identities only; horizontal $1$-cells $A \nrightarrow B$ $=$ $1$-cells $A \to B$ of $\mathcal{B}$; and, for a string $A_0 \xrightarrow{m_1} \cdots \xrightarrow{m_n} A_n$ and a horizontal $1$-cell $p : A_0 \nrightarrow A_n$,
> $$\widehat{\mathcal{B}}\text{-}2\text{-cells } (m_1, \dots, m_n) \Rightarrow p \;:=\; \mathcal{B}\text{-}2\text{-cells } (m_n \circ \cdots \circ m_1) \Rightarrow p,$$
> with the empty string ($n=0$) sent to the identity $1$-cell $1_{A_0}$, so that $(\,) \Rightarrow p$ means $1_{A_0} \Rightarrow p$. Substitution is defined as in Lemma 1. By Lemma 1, $\widehat{\mathcal{B}}$ is an fc-multicategory.
>
> **Step 2 — functoriality.** A homomorphism of bicategories $F : \mathcal{B} \to \mathcal{B}'$ induces $\widehat{F} : \widehat{\mathcal{B}} \to \widehat{\mathcal{B}'}$ by acting on objects and $1$-cells as $F$ does and on string-$2$-cells via the comparison $2$-cells of $F$ (which relate $F(m_n \circ \cdots \circ m_1)$ to $Fm_n \circ \cdots \circ Fm_1$). This is functorial because $F$'s comparison cells are coherent.
>
> **Step 3 — full and faithful.** Let $\Phi : \widehat{\mathcal{B}} \to \widehat{\mathcal{B}'}$ be a morphism of fc-multicategories. On objects and on horizontal $1$-cells (length-one strings) it gives an assignment of objects and $1$-cells; on $2$-cells over length-one strings it gives an action on $\mathcal{B}$-$2$-cells. Its value on a longer string $(m_1, \dots, m_n)$ is *forced*: the string-$2$-cell $1_{m_n \circ \cdots \circ m_1} : (m_1, \dots, m_n) \Rightarrow m_n \circ \cdots \circ m_1$ must be sent to a $2$-cell exhibiting $\Phi$'s value on the composite, and by the universal property of the composite in $\mathcal{B}'$ this determines a homomorphism comparison cell. Hence $\Phi = \widehat{F}$ for a unique homomorphism $F$, so $\widehat{(-)}$ is full and faithful.
>
> **Step 4 — image characterisation.** $\widehat{\mathcal{B}}$ has trivial vertical structure by construction, and *every* string is representable: the composite $m_n \circ \cdots \circ m_1$ together with the identity $2$-cell $1$ on it is universal, since by definition $2$-cells out of the string are exactly $2$-cells out of the composite. Conversely, let $\mathcal{C}$ be a vertically-trivial fc-multicategory in which every string is representable. Define a bicategory $\mathcal{B}$ with the same objects, with $1$-cells the horizontal $1$-cells of $\mathcal{C}$, and with composite $m_n \circ \cdots \circ m_1 :=$ the representing object of the string (chosen by Lemma 2 up to unique iso). The representing $2$-cells give the associator and unitors; their coherence is Lemma 2 plus Lemma 1. Then $\widehat{\mathcal{B}} \cong \mathcal{C}$. So the image is exactly the vertically-trivial representable fc-multicategories. This proves (1).
>
> **Step 5 — monoidal categories.** Restrict Step 1–4 to a single object. By Lemma 3, one-object vertically-trivial representable fc-multicategories are exactly monoidal categories, with horizontal $1$-cells as objects of $\mathcal{V}$, the string composer as $\otimes$, the empty-string composite as $I$, and $2$-cells $(X_1, \dots, X_n) \Rightarrow Y$ as morphisms $X_1 \otimes \cdots \otimes X_n \to Y$. This proves (2).
>
> **Step 6 — double categories and multicategories.** Dropping "vertically trivial" from Step 4 (keeping representability) gives, by the Categorical/Structural definition of [[Def - Weak Double Category|weak double category]] as a representable fc-multicategory, exactly the weak double categories. Keeping "one object, vertically trivial" but dropping representability gives, by definition of [[Def - Multicategory|multicategory]], exactly the plain multicategories: a $2$-cell $(X_1, \dots, X_n) \Rightarrow Y$ is precisely a multimap and substitution is precisely multicategory composition. This proves (3). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Linear algebra — multilinear maps as a multicategory becoming a monoidal category.** The vector spaces with multilinear maps $V_1 \times \cdots \times V_n \to W$ form a multicategory; representability of every string is exactly the existence of [[Def - Tensor Product of Vector Spaces|tensor products]] $V_1 \otimes \cdots \otimes V_n$, and the universal property of $\otimes$ is the representing $2$-cell. Recognising "tensor product exists" as "this multicategory is representable" is the non-obvious bridge: the theorem then says $(\mathbf{Vect}, \otimes)$ is the monoidal category obtained by turning the representability dial.

**Logic / type theory — the term multicategory of a type theory.** A multi-sorted algebraic theory or a simply-typed lambda calculus presents a multicategory whose multimaps $(A_1, \dots, A_n) \to B$ are derivable terms with $n$ free variables; representability of strings corresponds to the type theory having product/tensor types with the right universal property. The theorem frames "this type theory is (cartesian) monoidal" as a representability condition on its term multicategory — useful when comparing substructural logics (linear logic gives a non-cartesian monoidal structure).

**Algebraic topology — the bicategory of spaces and spans of spans.** Spaces, spans of spaces, and maps of spans form a bicategory (composition by homotopy pullback); embedding it via $\widehat{(-)}$ places it in the fc-multicategory world where the slice/opetope machinery applies, giving uniform higher cells. The non-obvious application is that the same embedding handles cobordism bicategories, so TQFT-style structures inherit the fc-multicategory taxonomy.

---

# Bridges

- **[[Def - Weak Double Category|Weak double categories]] as representable fc-multicategories** — this theorem's part (3) is the precise statement that "weak double category $=$ fc-multicategory with all horizontal composites". The bridge is the universal property: a string $(m_1, \dots, m_n)$ acquires a composite $m_1 \odot \cdots \odot m_n$ exactly when there is a universal $2$-cell out of the string, and that composite, with its uniqueness from Lemma 2, carries the associator and unitors of the double category. So the move from a virtual to an actual horizontal composition is precisely "impose representability".

- **[[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]** — this theorem subsumes the *associativity* half of coherence. Mac Lane proves every formal diagram of associators and unitors commutes; here that follows because all bracketings of a string represent the *same* string and so are uniquely isomorphic (Lemma 2), with the pentagon being the strict associativity of concatenation seen through representability. The two theorems are complementary: Mac Lane's lives inside one monoidal category, this one explains why the coherence pattern is identical across monoidal categories, bicategories, and double categories.

- **[[Def - Generalized Multicategory|Generalized multicategories]] and the monad $\mathrm{fc}$** — the theorem is the $\mathrm{fc}$-instance of the general principle that, for a cartesian monad $T$, the $T$-multicategories interpolate between "$T$-graphs" (no composition) and "$T$-algebras" (full composition). For $T =$ identity one gets categories from graphs; for $T =$ free-monoid one gets multicategories from sets; for $T = \mathrm{fc}$ one gets fc-multicategories from directed graphs, and the representable ones are the algebras, namely the double-category-like structures. This theorem is that pattern made explicit at the $\mathrm{fc}$ level.

---

# Unlocked by This

> [!tip] Uniform coherence and strictification *(from this chapter and HC2)*
> Because all four structures are representable fc-multicategories, **strictification** results (every bicategory is biequivalent to a strict $2$-category; every monoidal category to a strict one) become statements about replacing chosen representing objects by canonical ones — a single technique rather than four. This is the conceptual route to [[Thm - Strictification of Bicategories]] and to the strictification of monoidal categories in HC2.

> [!tip] Opetopes from any of these structures *(from later in Leinster)*
> Since bicategories and monoidal categories now live in the fc-multicategory world, the **slice construction** that produces **opetopes** applies to them directly. The $2$-dimensional opetope is exactly the shape of a string-topped $2$-cell ("many in, one out"); iterating the slice yields the opetopic cell shapes used in the Baez–Dolan definition of weak $n$-category.
