---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Initial and Terminal Object"
  - "Def - Group"
  - "Def - Module"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a category with a [[Def - Initial and Terminal Object|zero object]] $0$ (an object that is both initial and terminal).

1. Show that for any two objects $X, Y$ there is a canonical morphism $0_{X,Y} : X \to Y$, the **zero morphism**, defined as the composite $X \to 0 \to Y$, and that it does not depend on any choices.
2. Show the zero morphisms are **absorbing**: for any $f : X \to Y$ and $g : Y \to Z$, $g \circ 0_{X,Y} = 0_{X,Z}$ and $0_{Y,Z} \circ f = 0_{X,Z}$.
3. Verify that $\mathbf{Grp}$, $\mathbf{Ab}$, and $R\text{-}\mathbf{Mod}$ have zero objects and that the zero morphism is the trivial/zero map; verify that $\mathbf{Set}$ and $\mathbf{Ring}$ do **not** have a zero object.

**Recall:**

![[Def - Initial and Terminal Object#The Definition]]

A **zero object** $0$ is simultaneously [[Def - Initial and Terminal Object|initial and terminal]]: the hom-sets $\mathcal{C}(0, X)$ and $\mathcal{C}(X, 0)$ are singletons for every $X$. The trivial [[Def - Group|group]] $\{e\}$ and the zero [[Def - Module|module]] are the relevant examples.

---

# Convergent Strategy

**Problem class:** This is a "manufacture canonical structure from a universal property" exercise: a zero object is a hypothesis, and the task is to extract from it a distinguished morphism between *every* pair of objects and establish its formal properties. The routine is to use the singleton-hom-set property of $0$ at both ends to force uniqueness.

**Assumption pattern:** The single assumption — $0$ is both initial and terminal — does all the work. Initiality gives a unique $0 \to Y$; terminality gives a unique $X \to 0$. Their composite is forced, and because each leg is unique, the composite is independent of any choice. The absorption laws then follow because composing with anything that factors through $0$ must again factor through $0$.

**Theorem routing:** No external theorem is required; the route is the definition of [[Def - Initial and Terminal Object|zero object]] applied twice (once at each end) plus the uniqueness clauses. The verification in concrete categories routes through the identification of the trivial object as initial-and-terminal.

**Key decision point:** The interesting decision is *why* absorption holds. The mechanism is that any morphism of the form "something $\to 0 \to$ something" composed with another morphism still has $0$ in the middle, and the uniqueness of maps into and out of $0$ collapses the result to the canonical zero morphism. Spotting that "factors through $0$" is preserved under composition is the key.

---

# Legal Operations Used

1. **Operation 1 from the topic page (translate universality into a hom-set count).** Both legs $X \to 0$ and $0 \to Y$ are the unique elements of singleton hom-sets, which is what makes the zero morphism canonical.

2. **Operation 6 from the topic page (compose universal arrows).** The zero morphism is a composite of two universal arrows, and absorption is proved by composing further and using uniqueness.

---

# Hints

> [!note]- Hint 1
> Use initiality of $0$ to get $\iota_Y : 0 \to Y$ and terminality to get $\tau_X : X \to 0$. Set $0_{X,Y} = \iota_Y \circ \tau_X$.

> [!note]- Hint 2
> Independence of choices is free: both $\iota_Y$ and $\tau_X$ are *the* unique morphisms in their hom-sets, so there is nothing to choose.

> [!note]- Hint 3
> For absorption, note $g \circ 0_{X,Y} = g \circ \iota_Y \circ \tau_X$. The morphism $g \circ \iota_Y : 0 \to Z$ lives in the singleton $\mathcal{C}(0, Z)$, so it equals $\iota_Z$.

> [!note]- Hint 4
> For the concrete categories: $\{e\}$ in $\mathbf{Grp}$ is initial and terminal; $\{*\} \neq \emptyset$ in $\mathbf{Set}$; $\mathbb{Z} \neq \{0\}$ in $\mathbf{Ring}$.

---

# Solution

The zero morphism is built by composing the two universal maps through $0$; uniqueness at each end makes it canonical, and absorption falls out by collapsing composites through $0$ to the unique map. The concrete verifications then identify it as the familiar zero/trivial map.

**Step 1: The zero morphism is canonical.**

> [!note]- Derivation
> Since $0$ is terminal, $\mathcal{C}(X, 0)$ is a singleton; call its unique element $\tau_X : X \to 0$. Since $0$ is initial, $\mathcal{C}(0, Y)$ is a singleton; call its element $\iota_Y : 0 \to Y$. Define $0_{X,Y} = \iota_Y \circ \tau_X : X \to Y$. Both $\tau_X$ and $\iota_Y$ are *the* unique morphisms in their respective hom-sets, so there is no choice involved: $0_{X,Y}$ is determined by $X, Y$ alone.

**Step 2: Absorption.**

> [!note]- Derivation
> Let $g : Y \to Z$. Then $g \circ 0_{X,Y} = g \circ \iota_Y \circ \tau_X$. Now $g \circ \iota_Y$ is a morphism $0 \to Z$, and $\mathcal{C}(0, Z)$ is a singleton, so $g \circ \iota_Y = \iota_Z$. Hence $g \circ 0_{X,Y} = \iota_Z \circ \tau_X = 0_{X,Z}$.
>
> Let $f : X \to Y$. Then $0_{Y,Z} \circ f = \iota_Z \circ \tau_Y \circ f$. Now $\tau_Y \circ f$ is a morphism $X \to 0$, and $\mathcal{C}(X, 0)$ is a singleton, so $\tau_Y \circ f = \tau_X$. Hence $0_{Y,Z} \circ f = \iota_Z \circ \tau_X = 0_{X,Z}$.

**Step 3: Zero objects in concrete categories.**

> [!note]- Derivation
> *Has a zero object.* In $\mathbf{Grp}$ the trivial group $\{e\}$ is initial (unique homomorphism $\{e\} \to G$, $e \mapsto e_G$) and terminal (unique $G \to \{e\}$), so it is a [[Def - Initial and Terminal Object|zero object]]; the zero morphism $G \to H$ sends everything to $e_H$ — the trivial homomorphism. In $\mathbf{Ab}$ the same holds. In $R\text{-}\mathbf{Mod}$ the zero [[Def - Module|module]] $\{0\}$ is initial and terminal, and the zero morphism is the map $m \mapsto 0$, recovering "the zero map" of linear algebra.
>
> *No zero object.* In $\mathbf{Set}$, the initial object is $\emptyset$ and terminal objects are singletons $\{*\}$; since $\emptyset \neq \{*\}$ they never coincide, so there is no zero object. In $\mathbf{Ring}$, the initial object is $\mathbb{Z}$ and the terminal object is the zero ring $\{0\}$; since $\mathbb{Z} \neq \{0\}$, no zero object.

> [!note]- Complete formal solution
> With $0$ both initial and terminal, let $\tau_X : X \to 0$ and $\iota_Y : 0 \to Y$ be the unique morphisms (singleton hom-sets), and define $0_{X,Y} = \iota_Y \circ \tau_X$; uniqueness at both ends makes this canonical. Absorption: for $g : Y \to Z$, $g \circ \iota_Y \in \mathcal{C}(0,Z)$ is a singleton so equals $\iota_Z$, giving $g \circ 0_{X,Y} = 0_{X,Z}$; for $f : X \to Y$, $\tau_Y \circ f \in \mathcal{C}(X,0)$ equals $\tau_X$, giving $0_{Y,Z} \circ f = 0_{X,Z}$. Concretely, $\{e\}$ is a zero object in $\mathbf{Grp}, \mathbf{Ab}$ and $\{0\}$ in $R\text{-}\mathbf{Mod}$, with zero morphism the trivial/zero map; $\mathbf{Set}$ ($\emptyset \neq \{*\}$) and $\mathbf{Ring}$ ($\mathbb{Z} \neq \{0\}$) have no zero object. $\blacksquare$

---

# Key Takeaways

**A zero object turns "the trivial map" into a structural, choice-free notion.** In linear algebra one writes "the zero map" without a second thought, but its existence as a *canonical* morphism between any two objects is exactly the statement that the category has a zero object. The construction $X \to 0 \to Y$ shows the zero morphism is not an additional piece of data but is forced by the universal properties at both ends. The trigger to look for zero morphisms is any category of "structures with a distinguished trivial element" — groups, modules, vector spaces, pointed sets — and the reaction is that such categories support kernel/cokernel calculus precisely because the zero morphism exists to measure failure of injectivity and surjectivity.

**Absorption is the formal residue of "factoring through $0$ is contagious".** The reason $g \circ 0_{X,Y}$ and $0_{Y,Z} \circ f$ both collapse to $0_{X,Z}$ is that any composite that runs through $0$ stays anchored to $0$, and the uniqueness of maps into and out of $0$ erases everything else. This is a general pattern worth internalizing: whenever a morphism factors through a universal object, composing on either side cannot escape that factorization, because the universal object's hom-sets are too small to allow alternatives. The same logic underlies why constant maps absorb composition in $\mathbf{Set}_*$ and why the zero matrix annihilates products.

**The presence or absence of a zero object diagnoses the rigidity of a category.** Comparing $\mathbf{Grp}$ (zero object) with $\mathbf{Ring}$ (none) shows that whether initial and terminal coincide is a sensitive invariant of how much structure morphisms must preserve. Categories with a zero object are the gateway to **additive** and **abelian categories**, where every hom-set is an abelian group with the zero morphism as its identity, and where homological algebra lives. When you want to know whether a category can support kernels, cokernels, and exact sequences, the first question is "does it have a zero object?" — and this exercise is the test.
