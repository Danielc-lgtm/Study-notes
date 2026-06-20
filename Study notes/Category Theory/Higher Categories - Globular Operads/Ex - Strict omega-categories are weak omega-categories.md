---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)"
  - "Def - Globular Operad"
  - "Def - Contraction on a Globular Operad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $(L, \chi)$ be the [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)|Batanin–Leinster operad]] and let $1$ be the terminal [[Def - Globular Operad|globular operad]] (whose algebras are strict $\omega$-categories).

(a) Show that $1$ admits a unique contraction, making it the **terminal** object of the category $\mathbf{OC}$ of operads-with-contraction.

(b) Deduce that the unique map $L \to 1$ induces a functor $\mathbf{Str\text{-}\omega\text{-}Cat} \to \mathbf{Wk\text{-}\omega\text{-}Cat}$, and show it is **full and faithful** using that $L$ is contractible (so every fibre $L(\pi)$ is non-empty).

(c) Conclude that strict $\omega$-categories are exactly the weak ones whose coherence cells are identities.

**Recall:**

The category $\mathbf{OC}$ has objects $(P, \chi)$ — a [[Def - Globular Operad|globular operad]] with a [[Def - Contraction on a Globular Operad|contraction]] — and contraction-preserving operad maps as morphisms; $(L, \chi)$ is its [[Thm - The Initial Contractible Globular Operad Exists|initial]] object. The terminal globular operad $1$ has $1(\pi) = \{\ast\}$ for every shape; $\mathrm{Alg}(1) \cong \mathbf{Str\text{-}\omega\text{-}Cat}$ ([[Ex - Algebras for the terminal globular operad are strict omega-categories]]). The algebra construction $P \mapsto \mathrm{Alg}(P)$ is functorial: an operad map $f : P \to Q$ induces $f^\ast : \mathrm{Alg}(Q) \to \mathrm{Alg}(P)$. A functor is **full and faithful** if it is a bijection on each hom-set. $L$ **contractible** means every parallel pair lifts, which forces every fibre $L(\pi)$ to be non-empty.

---

# Convergent Strategy

**Problem class:** This is a *doctrine-comparison* problem from the topic page's problem-solving strategy: relate two notions of higher category (strict and weak) by an explicit functor and determine how faithful the comparison is. The route is "identify the operad map, induce the functor, check full-and-faithfulness via a property of $L$".

**Assumption pattern:** Two assumptions drive it. First, $1$ is *terminal* in $\mathbf{OC}$ (it absorbs a unique contraction), so there is a canonical map $L \to 1$. Second, $L$ is *contractible*, hence every $L(\pi) \neq \emptyset$, which is precisely what makes the induced functor full and faithful. Recognizing "contractibility $\Rightarrow$ non-empty fibres $\Rightarrow$ full-and-faithful" is the unlock.

**Theorem routing:** Route through (i) uniqueness of the contraction on $1$ (singleton fibres) to make $1$ terminal in $\mathbf{OC}$; (ii) functoriality of $\mathrm{Alg}$ applied to $L \to 1$ to get $\mathbf{Str\text{-}\omega\text{-}Cat} \to \mathbf{Wk\text{-}\omega\text{-}Cat}$; (iii) the criterion (Leinster 9.2.4) that the induced functor on algebras is full and faithful when each $L(\pi) \to 1(\pi)$ is surjective — automatic here since $L(\pi) \neq \emptyset$ and $1(\pi)$ is a singleton.

**Key decision point:** The non-obvious choice is to derive full-and-faithfulness from a property of the *operad map* (surjectivity on fibres, here automatic from contractibility) rather than checking it directly on functors between algebra categories. The tempting alternative — comparing strict and weak functors element by element — is laborious and obscures *why* the embedding is full and faithful; the operad-level criterion makes it a one-line consequence of "$L(\pi)$ is non-empty".

---

# Legal Operations Used

1. **Operation 4 from the topic page (take the terminal/initial object).** Part (a) identifies $1$ as terminal in $\mathbf{OC}$; the unique map $L \to 1$ from the initial object is the comparison.

2. **Operation 9 from the topic page (pull back along an operad map).** The functor $\mathbf{Str\text{-}\omega\text{-}Cat} \to \mathbf{Wk\text{-}\omega\text{-}Cat}$ is restriction of algebras along $L \to 1$.

3. **Operation 3 from the topic page (contraction lifts), used negatively.** Contractibility of $L$ (non-empty fibres) is exactly what upgrades the functor to full and faithful.

---

# Hints

> [!note]- Hint 1
> For (a): each fibre $1(\pi) = \{\ast\}$ is a singleton. A contraction component $\chi_\pi : \mathrm{Par}_1(\pi) \to 1(\pi)$ is a function into a one-element set. How many such functions are there, and do the source/target/shape conditions hold automatically?

> [!note]- Hint 2
> So $1$ has a unique contraction and is terminal in $\mathbf{OC}$. The initial object $L$ therefore has a unique map $L \to 1$. Apply the algebra functor: $\mathrm{Alg}(1) \to \mathrm{Alg}(L)$, i.e. $\mathbf{Str\text{-}\omega\text{-}Cat} \to \mathbf{Wk\text{-}\omega\text{-}Cat}$.

> [!note]- Hint 3
> For full-and-faithfulness: the induced functor on algebras is full and faithful when the operad map $L \to 1$ is *surjective on each fibre* — i.e. $L(\pi) \to 1(\pi)$ is onto. Since $1(\pi)$ is a single point, this just says $L(\pi) \neq \emptyset$.

> [!note]- Hint 4
> Why is $L(\pi)$ non-empty for every $\pi$? Because $L$ is *contractible*: every parallel pair lifts, and iterating from the bottom shows each fibre contains at least the contraction-generated operations. Hence the embedding is full and faithful.

---

# Solution

The solution shows $1$ is terminal in $\mathbf{OC}$ (Step 1), induces the embedding functor (Step 2), and proves it full and faithful via contractibility of $L$ (Step 3), concluding with the interpretation. The pivot is "contractibility makes every $L(\pi)$ non-empty, which is exactly full-and-faithfulness".

**Step 1: $1$ is terminal in $\mathbf{OC}$.**

> [!note]- Derivation
> Each fibre $1(\pi) = \{\ast\}$ is a singleton. A contraction component $\chi_\pi : \mathrm{Par}_1(\pi) \to 1(\pi)$ is a function into a one-element set, hence is the *unique* constant function. The source/target/shape conditions hold automatically: any parallel pair $(\alpha^-, \alpha^+) \in \mathrm{Par}_1(\pi)$ has $\alpha^- = \alpha^+ = \ast$ (the unique operation over $\partial\pi$), and $\chi_\pi(\ast,\ast) = \ast$ trivially has source $\ast = \alpha^-$, target $\ast = \alpha^+$, shape $\pi$. So $1$ admits a *unique* contraction. For terminality in $\mathbf{OC}$: given any $(P, \chi') \in \mathbf{OC}$, there is a unique operad map $P \to 1$ (since $1$ is the terminal collection), and it preserves contractions vacuously because the target fibres are singletons. Hence $(1, \chi_1)$ is the terminal object of $\mathbf{OC}$.

**Step 2: the induced embedding functor.**

> [!note]- Derivation
> Since $(L, \chi)$ is initial and $(1, \chi_1)$ is terminal in $\mathbf{OC}$, there is a unique contraction-preserving operad map
> $$
> u : L \longrightarrow 1.
> $$
> The algebra construction $P \mapsto \mathrm{Alg}(P)$ is functorial, with an operad map $f : P \to Q$ inducing $f^\ast : \mathrm{Alg}(Q) \to \mathrm{Alg}(P)$ by restricting the action along $f$. Applying this to $u : L \to 1$ gives
> $$
> u^\ast : \mathrm{Alg}(1) \longrightarrow \mathrm{Alg}(L), \qquad \text{i.e.} \qquad \mathbf{Str\text{-}\omega\text{-}Cat} \longrightarrow \mathbf{Wk\text{-}\omega\text{-}Cat}.
> $$
> Concretely: a strict $\omega$-category is an $L$-algebra by performing every $L$-operation as the *unique* strict composite of its shape (pulled back along $u$), with all coherence cells acting as identities.

**Step 3: the embedding is full and faithful.**

> [!note]- Derivation
> The induced functor $u^\ast$ on algebra categories is full and faithful provided the operad map $u : L \to 1$ is *surjective on each fibre*, i.e. $L(\pi) \to 1(\pi)$ is onto for every $\pi$ (Leinster 9.2.4). Since $1(\pi) = \{\ast\}$ is a singleton, surjectivity is equivalent to $L(\pi) \neq \emptyset$. Now $L$ is **contractible**: by the stratified construction, every fibre is non-empty (it contains at least the contraction-generated operations — e.g. unit operations and the lifts of parallel pairs), so $L(\pi) \neq \emptyset$ for all $\pi$. Therefore $u : L \to 1$ is fibrewise surjective, and $u^\ast : \mathbf{Str\text{-}\omega\text{-}Cat} \to \mathbf{Wk\text{-}\omega\text{-}Cat}$ is full and faithful.
>
> *Interpretation.* Full-and-faithfulness means: a strict $\omega$-functor between strict $\omega$-categories is the *same* as a (strict) map of their underlying weak $\omega$-categories — there are no "extra" weak maps and none are lost. So $\mathbf{Str\text{-}\omega\text{-}Cat}$ is a full subcategory of $\mathbf{Wk\text{-}\omega\text{-}Cat}$, and a strict $\omega$-category is precisely a weak $\omega$-category in which all the coherence cells (associators, unitors, interchangers, and the whole tower) happen to be *identities*. This is exactly what one expects of a notion of weak structure that genuinely generalizes the strict one.

> [!note]- Complete formal solution
> *(a)* Each $1(\pi)$ is a singleton, so the contraction component $\chi_\pi$ into it is unique and the source/target/shape conditions hold automatically (every parallel pair over $\partial\pi$ is $(\ast,\ast)$); hence $1$ has a unique contraction. The unique operad map $P\to 1$ from any $(P,\chi')$ preserves contractions vacuously, so $(1,\chi_1)$ is terminal in $\mathbf{OC}$.
>
> *(b)* Initiality of $L$ and terminality of $1$ give a unique map $u:L\to 1$; functoriality of $\mathrm{Alg}$ yields $u^\ast:\mathrm{Alg}(1)\to\mathrm{Alg}(L)$, i.e. $\mathbf{Str\text{-}\omega\text{-}Cat}\to\mathbf{Wk\text{-}\omega\text{-}Cat}$. This functor is full and faithful iff $u$ is fibrewise surjective (Leinster 9.2.4); since $1(\pi)$ is a point, this means $L(\pi)\neq\emptyset$, which holds because $L$ is contractible (every fibre is non-empty). So $u^\ast$ is full and faithful.
>
> *(c)* Thus $\mathbf{Str\text{-}\omega\text{-}Cat}$ is a full subcategory of $\mathbf{Wk\text{-}\omega\text{-}Cat}$: a strict $\omega$-category is exactly a weak $\omega$-category whose coherence cells are all identities, with strict $\omega$-functors being precisely the (strict) maps of the corresponding weak structures. $\blacksquare$

---

# Key Takeaways

**A good notion of weak structure has the strict one as a full subcategory.** The litmus test for any definition of "weak $X$" is that strict $X$ embeds *fully and faithfully* — no maps invented, none lost — so that strict objects are exactly the weak ones with trivial coherence. This exercise verifies the test for weak $\omega$-categories, and the verification is structural: $1$ is terminal in $\mathbf{OC}$, $L$ is initial, the unique map between them induces the embedding, and contractibility of $L$ (non-empty fibres) upgrades it to full and faithful. The trigger for this pattern: whenever comparing a strict and a weak doctrine, look for the operad (or monad) map between their presenting objects and check fibrewise surjectivity — that single condition controls full-and-faithfulness of the induced functor on algebras.

**Initial-to-terminal maps generate the canonical comparison functors.** The deeper structural lesson is that the category $\mathbf{OC}$ has both an initial object ($L$) and a terminal one ($1$), and the *unique* map $L \to 1$ between them is exactly the comparison "every weak $\omega$-category structure restricts from / every strict one includes into". This is a recurring device: when two doctrines are presented by the initial and terminal objects of one category of structured operads, the unique map between them *is* the comparison functor, and its properties (here fibrewise surjectivity) are read off from the operads. The same device, applied to the initial map $L \to \mathrm{End}(X)$ in [[Ex - Any contractible globular set is a weak omega-category]], produces weak $\omega$-category structures from contractibility.

**Contractibility means "every fibre is non-empty", and that is the engine of fullness.** The single property of $L$ that does the work here is that contractibility forces every $L(\pi) \neq \emptyset$ — there is always at least one operation of each shape, because the contraction generates them. This non-emptiness is exactly the surjectivity onto the singleton fibres of $1$ that makes the embedding full. The transferable diagnostic: contractibility of an operad is not only about coherence cells existing; it guarantees the operad is "everywhere inhabited", which is what lets it sit *above* the terminal operad with a fibrewise-surjective map. This same non-emptiness is what makes any contractible operad's algebras embed into weak $\omega$-categories. See [[Ex - Algebras for the terminal globular operad are strict omega-categories]] for the identification $\mathrm{Alg}(1) = \mathbf{Str\text{-}\omega\text{-}Cat}$ that this exercise builds on.
