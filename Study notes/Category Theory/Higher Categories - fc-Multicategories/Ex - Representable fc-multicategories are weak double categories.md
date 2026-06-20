---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - fc-Multicategory"
  - "Def - Weak Double Category"
  - "Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Call a string of horizontal $1$-cells $(m_1, \dots, m_n)$ in an [[Def - fc-Multicategory|fc-multicategory]] **representable** if there is a horizontal $1$-cell $p$ and a $2$-cell $\iota : (m_1, \dots, m_n) \Rightarrow p$ that is *universal*: every $2$-cell $\theta : (m_1, \dots, m_n) \Rightarrow q$ (with given vertical boundaries) factors as $\theta = \bar\theta \cdot \iota$ for a *unique* $2$-cell $\bar\theta : (p) \Rightarrow q$ with the same boundaries.

Prove that an fc-multicategory in which **every** string (of every length $n \geq 0$) is representable is exactly a [[Def - Weak Double Category|weak double category]]. Specifically: show the chosen universal composites define a horizontal composition $\odot$, that uniqueness of representing objects supplies coherent associativity and unit isomorphisms (associator, unitors, pentagon, triangle), and that conversely every weak double category, viewed as an fc-multicategory (its $2$-cells over a string $(m_1,\dots,m_n)$ being the $2$-cells out of $m_1\odot\cdots\odot m_n$), has every string representable.

**Recall:**

![[Def - fc-Multicategory#The Definition]]

![[Def - Weak Double Category#The Definition]]

A representing $2$-cell $\iota$ exhibits $p$ as "the composite of the string". Uniqueness of representing objects: if $(p,\iota)$ and $(p',\iota')$ both represent $(m_1,\dots,m_n)$ then there is a unique invertible $2$-cell $p\Rightarrow p'$ commuting with $\iota, \iota'$ (Lemma 2 of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]]).

---

# Convergent Strategy

**Problem class:** An *existence-of-composites / coherence-for-free* problem — the structural heart of the chapter, proving that the "representability" dial is exactly what turns an fc-multicategory into a weak double category.

**Assumption pattern:** The single hypothesis is "every string is representable". This is precisely the universal-property hypothesis that lets you *define* horizontal composition and then *derive* its coherence, rather than postulating it. The empty string's representability gives the horizontal unit.

**Theorem routing:** This is the proof of the structural equivalence asserted in the Categorical/Structural definition of [[Def - Weak Double Category|weak double category]] and used throughout [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]]. The associator and unitors come from Lemma 2 (uniqueness of representing objects); the pentagon and triangle from uniqueness over longer strings.

**Key decision point:** The non-obvious move is to obtain *all* the coherence (associator, unitors, pentagon, triangle) from a *single* principle — uniqueness of representing objects — rather than constructing each piece by hand. The temptation is to build $\odot$ and then separately verify associativity by computing with elements; instead, observe that both bracketings of a triple represent the same string, so the associator is forced and the pentagon is automatic.

---

# Legal Operations Used

1. **Operation 2 (universal $2$-cell out of a string).** Representability *is* the existence of such a universal $2$-cell; the universal composite becomes $\odot$.

2. **Operation 3 (uniqueness of representing objects gives the associator and pentagon).** The core of the coherence derivation.

3. **Operation 8 (empty string for the horizontal unit).** Representability of the length-zero string yields $\mathrm{U}_A$ and the unitors.

4. **Operation 7 (factorisation through the universal $2$-cell is unique).** Used to define the action of $\odot$ on $2$-cells.

---

# Hints

> [!note]- Hint 1
> Define $m_1\odot\cdots\odot m_n$ to be the representing object $p$ of the string $(m_1,\dots,m_n)$, with its universal $2$-cell $\iota$. For the action of $\odot$ on $2$-cells (i.e. to make $\odot$ a functor), use the universal property to factor.

> [!note]- Hint 2
> For the associator: $(m_1\odot m_2)\odot m_3$ and $m_1\odot(m_2\odot m_3)$ both represent the *string* $(m_1, m_2, m_3)$ — show each comes with a universal $2$-cell out of the triple. By uniqueness of representing objects there is a unique invertible $2$-cell between them. That is $a$.

> [!note]- Hint 3
> For the pentagon: all five vertices represent the string $(m_1, m_2, m_3, m_4)$, so all the edges (associators) are unique comparison maps; the pentagon commutes because any two parallel comparison maps between representing objects of the same string are equal (uniqueness). The unitors come from the empty string: $\mathrm{U}_A$ is its representing object, and $\mathrm{U}_A\odot m$, $m\odot\mathrm{U}_B$, $m$ all represent the string $(m)$.

---

# Solution

The proof builds $\odot$ from representing objects and derives every coherence cell from uniqueness.

**Step 1: Define horizontal composition $\odot$ and the horizontal unit.**

> [!note]- Derivation
> For each string $(m_1,\dots,m_n)$ choose a representing pair $(p, \iota)$ and set $m_1\odot\cdots\odot m_n := p$, with $\iota_{m_1,\dots,m_n} : (m_1,\dots,m_n)\Rightarrow p$ the universal $2$-cell. For $n=2$ this is the binary $\odot$; for $n=0$ at an object $A$, the representing object is the **horizontal unit** $\mathrm{U}_A$, with universal $2$-cell the empty-string unit. To make $\odot$ act on $2$-cells: given $2$-cells $\alpha_i : m_i\Rightarrow m_i'$ (length-one strings), the composite $\iota_{m_1',\dots} \cdot(\alpha_1,\dots,\alpha_n) : (m_1,\dots,m_n)\Rightarrow m_1'\odot\cdots\odot m_n'$ factors uniquely through $\iota_{m_1,\dots,m_n}$ as $(\alpha_1\odot\cdots\odot\alpha_n)\cdot\iota_{m_1,\dots,m_n}$, defining $\alpha_1\odot\cdots\odot\alpha_n$. Functoriality and unit are by uniqueness of factorisations (legal operation 7).

**Step 2: The associator and unitors from uniqueness of representing objects.**

> [!note]- Derivation
> Consider a triple $(m_1, m_2, m_3)$. The object $(m_1\odot m_2)\odot m_3$ comes with a universal $2$-cell out of the string $(m_1\odot m_2, m_3)$, which composes (via $\iota_{m_1,m_2}\odot 1_{m_3}$ then substitution) to a universal $2$-cell out of $(m_1, m_2, m_3)$; similarly $m_1\odot(m_2\odot m_3)$ gives a universal $2$-cell out of the same triple. So both objects represent $(m_1, m_2, m_3)$. By Lemma 2 of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories|the subsumption theorem]] there is a *unique* invertible $2$-cell
> $$a_{m_1,m_2,m_3} : (m_1\odot m_2)\odot m_3\xRightarrow{\ \cong\ } m_1\odot(m_2\odot m_3)$$
> commuting with the universal $2$-cells. The unitors arise the same way: $\mathrm{U}_A\odot m$, $m\odot\mathrm{U}_B$, and $m$ all represent the string $(m)$ (the empty string contributes nothing on substitution), so there are unique isos $l : \mathrm{U}_A\odot m\Rightarrow m$ and $r : m\odot\mathrm{U}_B\Rightarrow m$.

**Step 3: Pentagon, triangle, interchange, and the converse.**

> [!note]- Derivation
> *Pentagon.* The five objects obtained by bracketing $(m_1, m_2, m_3, m_4)$ all represent the string $(m_1, m_2, m_3, m_4)$; each associator edge is the unique comparison iso between two representing objects of this string. Any two parallel composites of associators are comparison isos between the same two representing objects, hence equal by uniqueness — so the pentagon commutes. *Triangle.* Both routes around the triangle are comparison isos between representing objects of $(m_1, m_2)$ (with a $\mathrm{U}$ inserted), hence equal. *Interchange* is inherited from the fc-multicategory's substitution, which already satisfies the needed compatibility (it is the substitution composition). Therefore the chosen composites, with $a, l, r$ and their coherence, make the fc-multicategory a [[Def - Weak Double Category|weak double category]].
>
> *Converse.* Let $\mathbb{D}$ be a weak double category. View it as an fc-multicategory by setting the $2$-cells over $(m_1,\dots,m_n)$ to be the $2$-cells out of $m_1\odot\cdots\odot m_n$ in $\mathbb{D}$. Then $m_1\odot\cdots\odot m_n$ with the identity $2$-cell is universal — every $2$-cell out of the string is, by definition, a $2$-cell out of the composite — so every string is representable. Hence the two notions coincide.

> [!note]- Complete formal solution
> Let $\mathcal{C}$ be an fc-multicategory in which every string is representable. Choose representing pairs $(p_{m_1,\dots,m_n}, \iota_{m_1,\dots,m_n})$ for all strings; define $m_1\odot\cdots\odot m_n := p_{m_1,\dots,m_n}$ and $\mathrm{U}_A := p_{(\,)}$ at $A$. The universal property makes $\odot$ functorial on $2$-cells (unique factorisations). For a triple, both $(m_1\odot m_2)\odot m_3$ and $m_1\odot(m_2\odot m_3)$ represent $(m_1,m_2,m_3)$, so uniqueness of representing objects gives a unique invertible $a$; the empty string gives unique unitors $l, r$. The pentagon and triangle hold because all relevant objects represent a fixed string and any two parallel comparison isos coincide. Interchange is inherited from substitution. Thus $\mathcal{C}$ is a [[Def - Weak Double Category|weak double category]]. Conversely, any weak double category, with $2$-cells over a string defined as $2$-cells out of the $\odot$-composite, has every string represented by that composite. The two notions are equivalent. $\blacksquare$

---

# Key Takeaways

**Representability is the exact dial that turns "potential composites" into "actual composites".** The fc-multicategory records strings without composing them; a weak double category composes them. This exercise pinpoints that the *only* difference is whether strings have universal composites. The transferable insight is that "composition exists" is best understood as a *representability property* of an underlying virtual structure, not as primitive data — which is why the fc-multicategory (virtual double category) is the more fundamental notion and the weak double category is its representable special case. The trigger: "do composites exist?" $\Rightarrow$ "are the strings representable?", and the answer determines which structure you are in.

**All coherence flows from one principle: uniqueness of representing objects.** The single most efficient idea in the chapter is that the associator, the unitors, the pentagon, and the triangle are *not four separate things to verify* — they are all consequences of "representing objects of the same string are uniquely isomorphic". Two bracketings represent the same triple, so the associator is forced; any two parallel chains of associators are comparison maps between the same representing objects, so the pentagon commutes. This collapses the entire coherence apparatus into one universal-property argument (legal operation 3). The diagnostic to carry: whenever you must produce *and* cohere a family of isomorphisms, check whether all the objects involved represent a common universal problem — if so, the isomorphisms and their coherence are automatic.

**The construction is reversible, which is what makes it an equivalence of notions.** It is not enough to turn a representable fc-multicategory into a weak double category; the converse — every weak double category is a representable fc-multicategory — is what makes the two notions *the same*, and it is almost trivial once you define string-$2$-cells as $2$-cells out of the composite. The deeper point, recurring in [[Ex - A bicategory is a one-object weak double category]] and in [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]], is that the chapter's structures are related by *equivalences* (full, faithful, essentially surjective correspondences), not mere comparisons, so theorems genuinely transfer in both directions. This bidirectionality is why one can freely choose to work virtually (with strings) or representably (with composites), whichever is convenient for the problem at hand.
