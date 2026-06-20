---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Enriched Category"
  - "Def - Penon Weak ω-Category"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Trimble's definition of weak $n$-category is by iterated enrichment: a weak $(n+1)$-category is a category **[[Def - Enriched Category|enriched]]** over the category of weak $n$-categories, where the enrichment uses a fixed **$E_\infty$-operad** $\mathcal{E}$ — a topological (or simplicial) operad whose space of $k$-ary operations $\mathcal{E}(k)$ is *contractible* for every $k$, with a free symmetric-group action.

Carry out one step of this recursion explicitly. Show that, given the data of objects, hom-objects, and an action of $\mathcal{E}$, one obtains a well-defined composition $\circ : \mathcal{C}(y,z) \otimes \mathcal{C}(x,y) \to \mathcal{C}(x,z)$ together with *all* the coherence data (associativity, unit, and higher coherences) — and explain precisely why the *contractibility* of each $\mathcal{E}(k)$ is what makes "essentially one way to compose $k$ morphisms" rigorous. Then locate Trimble's definition on the algebraic / non-algebraic axis.

**Recall:**

A category **[[Def - Enriched Category|enriched]]** over a [[Def - Monoidal Category|monoidal category]] $(\mathcal{V}, \otimes, I)$ has, for each pair of objects, a hom-*object* $\mathcal{C}(x,y) \in \mathcal{V}$, an identity map $I \to \mathcal{C}(x,x)$, and an associative, unital composition $\mathcal{C}(y,z) \otimes \mathcal{C}(x,y) \to \mathcal{C}(x,z)$ in $\mathcal{V}$.

An **operad** $\mathcal{E}$ in spaces consists of spaces $\mathcal{E}(k)$ ("$k$-ary operations") with a unit $1 \in \mathcal{E}(1)$, symmetric-group actions $\mathcal{E}(k) \times S_k \to \mathcal{E}(k)$, and composition maps $\mathcal{E}(k) \times \mathcal{E}(j_1) \times \cdots \times \mathcal{E}(j_k) \to \mathcal{E}(j_1 + \cdots + j_k)$ satisfying associativity, unit, and equivariance axioms. It is **$E_\infty$** if each $\mathcal{E}(k)$ is contractible and the $S_k$-action is free. An **algebra** for $\mathcal{E}$ on an object $A$ is a system of maps $\mathcal{E}(k) \otimes A^{\otimes k} \to A$ compatible with the operad structure.

---

# Convergent Strategy

**Problem class:** This is a *coherence-by-contractibility* problem — the recognition that a contractible space of operations gives "one operation up to coherent homotopy", with all higher coherences supplied automatically. It is the operadic counterpart of the Segal condition and of the contraction on a globular operad; the routine is to read the contractibility of $\mathcal{E}(k)$ as "the space of ways to compose $k$ things is contractible, so any two ways are connected by a contractible space of homotopies".

**Assumption pattern:** The crucial data is the $E_\infty$-operad: contractibility of every $\mathcal{E}(k)$, with a free $S_k$-action. Contractibility is what makes the *choice* of composition immaterial up to homotopy; the free symmetric action is what makes the operad "symmetric/commutative up to all higher homotopy" ($E_\infty$ rather than merely $A_\infty$), so that the composition is not only associative but also has the higher symmetric coherences. For mere associativity one would use an $A_\infty$ (non-symmetric, contractible) operad; the $E_\infty$ choice buys symmetry too.

**Theorem routing:** The route is: pick any point $\mu_2 \in \mathcal{E}(2)$ to *define* a binary composition $\mathcal{C}(y,z)\otimes\mathcal{C}(x,y) \to \mathcal{C}(x,z)$ via the algebra action; then observe that the two bracketings of a triple composite are images of two points of $\mathcal{E}(3)$, and contractibility of $\mathcal{E}(3)$ supplies a *path* between them — the associator — and contractibility of the path space supplies the pentagon, and so on up. The recursion is then closed by enriching over weak $n$-categories, which carry exactly this kind of homotopical structure.

**Key decision point:** The non-obvious choice is to *not* pick a single composition operation and treat it as canonical, but to keep the whole contractible space $\mathcal{E}(2)$ of binary operations and let contractibility generate the coherences. Picking one $\mu_2$ is fine for *defining* composition, but the coherence data comes from the *paths* in $\mathcal{E}(k)$, not from the chosen points — and forgetting the rest of $\mathcal{E}(k)$ would lose all the higher coherence.

---

# Legal Operations Used

1. **Operation 4 from the topic page (take algebras for an operad).** The composition and its coherences are the action maps $\mathcal{E}(k) \otimes \mathcal{C}(\cdots)^{\otimes k} \to \mathcal{C}(\cdots)$ of an $\mathcal{E}$-algebra structure.

2. **Operation 3 from the topic page (build a contraction).** Contractibility of $\mathcal{E}(k)$ *is* a contraction: it provides chosen paths (and higher homotopies) connecting any two operations, which are precisely the coherence cells.

3. **Operation 1 from the topic page (read a contractible space of operations as "composition is essentially unique").** This is the conceptual translation that the whole exercise turns on, and it locates Trimble between the algebraic and geometric camps.

---

# Hints

> [!note]- Hint 1
> To *define* a binary composition, you only need one operation; choose any point $\mu_2 \in \mathcal{E}(2)$ and apply the $\mathcal{E}$-algebra action $\mathcal{E}(2) \otimes A \otimes A \to A$ with $A =$ the relevant hom-object. The interesting question is not the composition but its *coherence*.

> [!note]- Hint 2
> The two bracketings $(h \circ g) \circ f$ and $h \circ (g \circ f)$ of a triple composite are the images, under the operad composition, of two specific points of $\mathcal{E}(3)$ (obtained by composing $\mu_2$ with itself in the two orders). What does contractibility of $\mathcal{E}(3)$ give you between those two points?

> [!note]- Hint 3
> A path in $\mathcal{E}(3)$ between the two bracketing-operations, pushed through the algebra action, becomes the associator. The *pentagon* coherence is then a $2$-disk in $\mathcal{E}(4)$ (or in the relevant operation space) bounded by the five associator-paths; contractibility supplies it. Iterating, *every* coherence is filled because every $\mathcal{E}(k)$ is contractible — there is never an obstruction.

> [!note]- Hint 4
> For the placement on the algebraic/non-algebraic axis: composition *is* chosen (you picked $\mu_2$), which is algebraic; but it is chosen from a *contractible* space, so the choice does not matter up to homotopy, which is the geometric stance. Trimble's definition therefore straddles the two.

---

# Solution

The argument has three movements. Step 1 defines composition from a chosen operation. Step 2 produces the associator from a path in $\mathcal{E}(3)$ and explains why contractibility kills all higher coherence obstructions. Step 3 closes the recursion and places the definition on the algebraic/non-algebraic axis.

**Step 1: composition from a point of $\mathcal{E}(2)$.**

> [!note]- Derivation
> Fix objects $x, y, z$ of the to-be-constructed weak $(n+1)$-category $\mathcal{C}$, and let $A_{x,y} := \mathcal{C}(x,y)$ be the hom-object, an object of the base (weak $n$-categories). The $\mathcal{E}$-algebra structure includes an action map
> $$\gamma_2 : \mathcal{E}(2) \otimes A_{y,z} \otimes A_{x,y} \longrightarrow A_{x,z}.$$
> Choosing any point $\mu_2 \in \mathcal{E}(2)$ — equivalently, a map $I \to \mathcal{E}(2)$ from the monoidal unit — and precomposing gives
> $$\circ \;:=\; \gamma_2(\mu_2 \otimes -) : A_{y,z} \otimes A_{x,y} \longrightarrow A_{x,z},$$
> a binary composition. Different choices of $\mu_2$ give different compositions — but since $\mathcal{E}(2)$ is contractible, any two choices are connected by a path, hence the two compositions are homotopic. So composition is *defined* but *not canonical*; this non-canonicity, controlled by contractibility, is the whole point.

**Step 2: the associator and all higher coherences from contractibility.**

> [!note]- Derivation
> Consider a triple composite. The two bracketings $(h \circ g)\circ f$ and $h \circ (g \circ f)$ are obtained by applying the operad composition to $\mu_2$ twice in the two possible orders, producing two points
> $$\mu_2 \circ_1 \mu_2,\quad \mu_2 \circ_2 \mu_2 \;\in\; \mathcal{E}(3),$$
> and then acting on $A_{z,w} \otimes A_{y,z} \otimes A_{x,y}$. Because $\mathcal{E}(3)$ is *contractible*, there is a path $p : [0,1] \to \mathcal{E}(3)$ with $p(0) = \mu_2 \circ_1 \mu_2$ and $p(1) = \mu_2 \circ_2 \mu_2$. Pushing $p$ through the action map $\mathcal{E}(3) \otimes A^{\otimes 3} \to A$ yields a homotopy
> $$\alpha : (h \circ g)\circ f \;\simeq\; h \circ (g \circ f),$$
> the **associator** — a $1$-cell in the hom-object (which lives in weak $n$-categories, so it *has* such cells). Now the **pentagon**: the five ways of reassociating a quadruple composite give five associator-paths forming a pentagon in $\mathcal{E}(4)$; since $\mathcal{E}(4)$ is contractible (in particular simply connected), this pentagon bounds a disk, whose image is the pentagon coherence $2$-cell. The pattern continues without end: the $k$-th level coherence is a sphere in $\mathcal{E}(k+1)$, and contractibility of $\mathcal{E}(k+1)$ fills every sphere. **There is never an obstruction**, because a contractible space has trivial homotopy in all dimensions. This is exactly the sense in which "there is essentially one way to compose $k$ morphisms": the operations form a contractible space, so all choices and all coherences among them are canonically filled.

**Step 3: closing the recursion and placing the definition.**

> [!note]- Derivation
> The hom-objects $A_{x,y}$ were taken in the category of weak $n$-categories, which by the inductive hypothesis is a category with a suitable notion of homotopy (cells of every dimension). The associator, pentagon, and higher coherences produced in Step 2 are cells of the hom-objects, hence legitimate data of weak $n$-categories — so the construction is *internally consistent* and defines a weak $(n+1)$-category. The base case $n = 0$ is sets (or spaces), where $\mathcal{E}$ acts trivially and a "weak $1$-category" is an ordinary [[Def - Category|category]].
>
> *Placement.* Composition is **chosen** — we picked $\mu_2$ — which is the *algebraic* stance: a Trimble weak $n$-category carries a selected composition operation as part of its $\mathcal{E}$-algebra structure, and a morphism must respect it. But the choice is from a **contractible** space, so it is immaterial up to coherent homotopy — which is the *geometric* stance, where composition is a property up to a contractible space of choices. Trimble's definition therefore *interpolates*: structurally algebraic (operad action, like [[Def - Penon Weak ω-Category|Penon]] and Batanin–Leinster), but with the contractibility that makes it behave like the geometric definitions.

> [!note]- Complete formal solution
> Let $\mathcal{E}$ be an $E_\infty$-operad and let $\mathcal{C}$ be an $\mathcal{E}$-enriched-style structure: objects, hom-objects $A_{x,y}$ in weak $n$-categories, and action maps $\gamma_k : \mathcal{E}(k) \otimes A_{x_{k-1},x_k} \otimes \cdots \otimes A_{x_0,x_1} \to A_{x_0,x_k}$ satisfying the operad-algebra axioms.
>
> **Composition.** Choose $\mu_2 \in \mathcal{E}(2)$; define $\circ = \gamma_2(\mu_2 \otimes -)$. Any other choice is path-connected to $\mu_2$ in the contractible $\mathcal{E}(2)$, so $\circ$ is well-defined up to homotopy.
>
> **Coherence.** The two triple-bracketings are $\gamma_3$ applied to $\mu_2 \circ_1 \mu_2$ and $\mu_2 \circ_2 \mu_2 \in \mathcal{E}(3)$; a path between them in the contractible $\mathcal{E}(3)$ gives the associator $\alpha$. For each $k$, the $k$-ary coherence is a map of an $(k-2)$-sphere into $\mathcal{E}(k)$; contractibility of $\mathcal{E}(k)$ (all homotopy groups trivial) extends it over the disk, filling the coherence. Hence *all* coherences exist and are themselves coherent — there is no obstruction at any level.
>
> **Consistency and recursion.** The coherence cells are cells of the hom-objects $A_{x,y}$, which are weak $n$-categories and so admit them; thus $\mathcal{C}$ is a well-defined weak $(n+1)$-category. Base case $n=0$: sets, recovering ordinary categories at level $1$.
>
> **Placement.** Composition is selected ($\mu_2$ is chosen) — algebraic — but from a contractible space — geometric in effect. Trimble's definition straddles the algebraic/non-algebraic axis. $\blacksquare$

---

# Key Takeaways

**Contractibility of an operation space is the operadic form of "composition is a property up to a contractible space of choices".** This is the unifying translation of the whole chapter, seen here through operads. A contractible space has trivial homotopy in every dimension, so a map out of *any* sphere into it extends over the disk — which means *every* coherence one could ask for is automatically filled, with no obstruction at any level. This is why a single contractible operad generates the entire infinite tower of coherences (associativity, pentagon, and all higher) for free. The trigger is "a contractible space of operations", and the reaction is "composition exists, is unique up to homotopy, and all coherences are filled — stop looking for an obstruction, there is none". The same fact powers the recognition principle for loop spaces and the definition of $A_\infty$/$E_\infty$-algebras.

**$A_\infty$ buys associativity; $E_\infty$ buys associativity and symmetry.** The distinction between a non-symmetric contractible operad and a symmetric one ($E_\infty$) is exactly the distinction between "composable up to coherent homotopy" and "composable *and commutative* up to coherent homotopy". For building higher *categories* (where composition need not be symmetric) an $A_\infty$-operad suffices; Trimble uses an $E_\infty$-operad to get the additional symmetric coherences that make the iterated enrichment well-behaved. Recognising which flavour of operad a construction needs — $A_\infty$ for associativity alone, $E_\infty$ for symmetry too — is a reusable diagnostic whenever operads control coherence.

**Trimble's definition shows the algebraic/non-algebraic axis is a spectrum, not a dichotomy.** It is tempting to file every definition as either "composition is structure" or "composition is property", but Trimble's sits in between: composition is genuine structure (a chosen operation), yet chosen from a contractible space so that the choice is homotopically immaterial. This teaches that the real content is *how much canonicity* the composition has, and contractibility is the dial that interpolates between fully-rigid (a single chosen composite, strict) and fully-flexible (no composite chosen, pure property). When classifying a definition, do not just ask "structure or property?" but "how contractible is the space of composites?" — that question places it precisely on the spectrum and predicts how easy its equivalences and how rigid its objects will be.
