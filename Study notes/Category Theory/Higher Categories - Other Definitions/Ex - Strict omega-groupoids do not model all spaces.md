---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Homotopy Hypothesis"
  - "Def - Higher Homotopy Group"
  - "Def - Topological Space"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Show that **strict** $\infty$-groupoids do **not** model all homotopy types: specifically, argue that no strict $\infty$-groupoid (equivalently, no **crossed complex**) has the homotopy type of the $2$-sphere $S^2$. Conclude that the **[[Thm - The Homotopy Hypothesis|homotopy hypothesis]]** is *false* for strict ω-groupoids — and explain why this failure is the sharpest possible evidence that *weakness* is mathematically forced in every definition of higher category, not a matter of convenience.

The crux is a single computation: in a strict $\infty$-groupoid the **Whitehead product** $\pi_2 \times \pi_2 \to \pi_3$ must *vanish*, whereas for $S^2$ the Whitehead product $[\iota, \iota] \in \pi_3(S^2)$ is the Hopf class, a generator of $\pi_3(S^2) \cong \mathbb{Z}$ — so $S^2$ cannot be a strict $\infty$-groupoid.

**Recall:**

A **strict $\infty$-groupoid** is a strict ω-category in which every cell (of every dimension) has a strict inverse. By the Brown–Higgins theorem these are equivalent to **crossed complexes** — a tower of groups/groupoids $\cdots \to C_3 \to C_2 \to C_1 \rightrightarrows C_0$ with an action and boundary maps, generalising chain complexes and the bottom $\pi_1$-data.

The **[[Def - Higher Homotopy Group|homotopy groups]]** $\pi_n(T, t)$ of a pointed space are the groups of based maps $S^n \to T$ up to based homotopy; $\pi_n$ is abelian for $n \ge 2$. The **Whitehead product** $[-,-] : \pi_p \times \pi_q \to \pi_{p+q-1}$ is a bilinear pairing measuring the failure of homotopy groups to assemble "freely"; for $S^2$, $[\iota,\iota] \in \pi_3(S^2)$ where $\iota \in \pi_2(S^2)$ is the identity class.

---

# Convergent Strategy

**Problem class:** This is an *obstruction / non-representability* problem — show a target object cannot arise from a restricted class of structures by exhibiting an invariant the class forces to vanish but the target has nonzero. The routine is "find the invariant the strict structures kill, compute it nonzero for $S^2$".

**Assumption pattern:** The decisive feature of *strict* $\infty$-groupoids is that all their operations are *strictly* associative and the interchange law holds *on the nose*. The Eckmann–Hilton / interchange argument then forces the higher homotopy operations — in particular the Whitehead product — to be trivial. So strictness routes directly to "Whitehead products vanish".

**Theorem routing:** The route is: (1) in a strict $\infty$-groupoid, the strict interchange law forces the Whitehead product $\pi_2 \times \pi_2 \to \pi_3$ to be zero (the same Eckmann–Hilton mechanism that makes $\pi_2$ abelian, pushed one level up); (2) for $S^2$, the Whitehead product $[\iota,\iota]$ equals (up to sign) the Hopf map $\eta$, a *generator* of $\pi_3(S^2) = \mathbb{Z}$, hence nonzero; (3) therefore $S^2$ is not (weakly equivalent to) any strict $\infty$-groupoid, and the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] fails for the strict notion.

**Key decision point:** The non-obvious choice is to test with the *Whitehead product*, not the homotopy groups themselves. A strict $\infty$-groupoid can have *any* prescribed homotopy groups — the groups alone are not the obstruction. What it cannot reproduce is the nontrivial *interaction* between them encoded by the Whitehead product (and, equivalently, by the nontrivial $k$-invariant / Postnikov data). Choosing the right invariant — a secondary operation, not a primary one — is the heart of the argument.

---

# Legal Operations Used

1. **Operation 8 from the topic page (truncate / specialise and compare with the known case).** We specialise to strict $\infty$-groupoids and compare against the homotopy type of $S^2$, the known target.

2. **Operation 7 from the topic page (the fundamental $\infty$-groupoid), used as a test).** We ask whether $\Pi_\infty(S^2)$ could be strict, and find it cannot.

3. **Illegal operation 2 from the topic page (assuming all definitions agree), examined).** This exercise is exactly a demonstration that the strict definition *fails* the homotopy hypothesis, so one may not assume strict and weak agree — the repair is weakness.

---

# Hints

> [!note]- Hint 1
> The homotopy groups alone cannot be the obstruction: one can build a strict $\infty$-groupoid with any prescribed $\pi_n$. Look instead for a *secondary* operation — a bilinear pairing between homotopy groups — that strictness forces to vanish.

> [!note]- Hint 2
> Recall *why* $\pi_2$ is abelian: the Eckmann–Hilton argument uses two compatible compositions (horizontal and vertical) that *interchange*, forcing commutativity. In a strict $\infty$-groupoid the interchange law holds strictly in every dimension. Push the same argument one dimension up: what does strict interchange force the Whitehead product $\pi_2 \times \pi_2 \to \pi_3$ to be?

> [!note]- Hint 3
> For $S^2$: the identity class $\iota \in \pi_2(S^2) \cong \mathbb{Z}$ has a self-Whitehead-product $[\iota,\iota] \in \pi_3(S^2)$. It is a classical fact that $[\iota,\iota]$ is twice the Hopf class (or the Hopf class up to sign in the relevant normalisation), in any case a *generator* of $\pi_3(S^2) \cong \mathbb{Z}$ — nonzero.

> [!note]- Hint 4
> Put the two together: strictness $\Rightarrow$ Whitehead product zero; $S^2$ has Whitehead product nonzero; so $S^2$ is not strict. The homotopy hypothesis ("$\infty$-groupoids $=$ spaces") therefore *fails* if "$\infty$-groupoid" means "strict $\infty$-groupoid" — weakness is needed.

---

# Solution

The argument is an invariant-mismatch. Step 1 shows strict interchange kills the Whitehead product. Step 2 computes the Whitehead product of $S^2$ to be nonzero. Step 3 concludes and draws the moral.

**Step 1: in a strict $\infty$-groupoid the Whitehead product vanishes.**

> [!note]- Derivation
> Recall the Eckmann–Hilton argument at level $2$. Two unital binary operations $\cdot$ and $\ast$ on a set that satisfy the *interchange law* $(a\cdot b)\ast(c\cdot d) = (a\ast c)\cdot(b\ast d)$ and share a common unit are forced to be equal *and commutative*. In a strict $\infty$-groupoid, vertical and horizontal composition of $2$-cells satisfy strict interchange, which is exactly why $\pi_2$ (endomorphisms of an identity $1$-cell on an identity object, with the two compositions) is abelian. Now go one dimension higher: the Whitehead product $\pi_2 \times \pi_2 \to \pi_3$ is a *secondary* operation built from the failure of two ways of composing to agree — but in a strict $\infty$-groupoid the two ways agree *strictly* (interchange holds on the nose in every dimension), so there is no failure to measure, and the Whitehead product is identically zero. Equivalently, the Brown–Higgins theorem identifies strict $\infty$-groupoids with crossed complexes, and crossed complexes model exactly the homotopy types with *trivial* Whitehead products (their Postnikov $k$-invariants involving Whitehead products vanish). So: **strict $\Rightarrow$ Whitehead product $= 0$.**

**Step 2: $S^2$ has a nonzero Whitehead product.**

> [!note]- Derivation
> The homotopy groups of $S^2$ in low degree are $\pi_2(S^2) \cong \mathbb{Z}$ (generated by the identity class $\iota$, the degree-$1$ map $S^2 \to S^2$) and $\pi_3(S^2) \cong \mathbb{Z}$ (generated by the Hopf map $\eta : S^3 \to S^2$). The self-Whitehead-product $[\iota, \iota] \in \pi_3(S^2)$ is, by the classical computation (e.g. via the EHP sequence or directly from the Hopf fibration), equal to $\pm 2\eta$ in the standard normalisation — in particular *nonzero* and of infinite order. Even granting normalisation ambiguities, the essential and standard fact is that $[\iota,\iota]$ generates a finite-index (indeed infinite-order) subgroup of $\pi_3(S^2)$, so it is *not zero*. Hence $S^2$ has a *nonvanishing* Whitehead product $\pi_2 \times \pi_2 \to \pi_3$.

**Step 3: conclusion and moral.**

> [!note]- Derivation
> If $S^2$ were weakly equivalent to a strict $\infty$-groupoid $\mathcal{G}$, then $\mathcal{G}$ and $S^2$ would have the same homotopy groups *and the same Whitehead products* (the Whitehead product is a homotopy invariant). But Step 1 forces $\mathcal{G}$'s Whitehead product to be zero, while Step 2 shows $S^2$'s is nonzero. Contradiction. Therefore **no strict $\infty$-groupoid has the homotopy type of $S^2$**, and the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] — "$\infty$-groupoids are spaces" — is *false* when "$\infty$-groupoid" is read strictly.
>
> The moral: the homotopy hypothesis is the acceptance test for a definition of higher category, and the *strict* definition fails it. The failure is not a technicality — it is the simplest interesting space, $S^2$, that the strict notion cannot reach. This is the sharpest evidence that the *weakness* built into every definition in this chapter (Batanin–Leinster contractions, Penon stretchings, Segal/quasi-category up-to-homotopy composition) is *forced*: weak associativity and weak interchange are precisely what allow nonzero Whitehead products, hence what allow all homotopy types. A definition that strictifies them is not merely inconvenient; it is *wrong*, missing actual spaces.

> [!note]- Complete formal solution
> Suppose, for contradiction, that a strict $\infty$-groupoid $\mathcal{G}$ is weakly equivalent to $S^2$.
>
> **(1)** In $\mathcal{G}$ the interchange law holds strictly in every dimension; by the Eckmann–Hilton mechanism, lifted one degree, the Whitehead product $\pi_2(\mathcal{G})\times\pi_2(\mathcal{G})\to\pi_3(\mathcal{G})$ is identically zero. (Equivalently: strict $\infty$-groupoids $\simeq$ crossed complexes [Brown–Higgins], which model exactly the homotopy types with vanishing Whitehead products.)
>
> **(2)** For $S^2$: $\pi_2(S^2)=\mathbb{Z}\langle\iota\rangle$, $\pi_3(S^2)=\mathbb{Z}\langle\eta\rangle$, and $[\iota,\iota]=\pm2\eta\ne0$.
>
> **(3)** A weak equivalence preserves homotopy groups and Whitehead products, so $\mathcal{G}$ and $S^2$ would have the same (zero vs nonzero) Whitehead product — contradiction. Hence no strict $\infty$-groupoid models $S^2$, and the homotopy hypothesis fails for strict $\infty$-groupoids; weakness is required. $\blacksquare$

---

# Key Takeaways

**Homotopy groups are not the obstruction; their interactions are.** The most transferable lesson is that a restricted class of structures (here, strict $\infty$-groupoids) can often realise any prescribed *primary* invariants (the homotopy groups) while failing to realise the *secondary* invariants that record how the primary ones interact (Whitehead products, Postnikov $k$-invariants, Massey products). When proving a non-representability result, do not test with the obvious primary invariant — it will usually be realisable — but hunt for the secondary operation the restriction kills. The trigger is "show class $\mathcal{X}$ cannot model object $Y$", and the reaction is "find the secondary/higher operation that $\mathcal{X}$ forces to vanish and $Y$ has nonzero".

**Strict interchange is the enemy of higher structure.** The single mechanism behind the whole failure is that strict interchange, via Eckmann–Hilton, *collapses* higher operations: at level $2$ it forces commutativity (which is fine — $\pi_2$ really is abelian), but pushed up it forces Whitehead products to vanish (which is *fatal* — real spaces have them). This is why every successful definition of weak higher category *weakens* the interchange law to hold only up to coherent higher cells. Recognising "strict interchange $\Rightarrow$ Eckmann–Hilton collapse" tells you, on sight, that any strictification will lose exactly the secondary homotopy operations — and therefore lose actual homotopy types. The same Eckmann–Hilton collapse is what makes the periodic table of $k$-tuply-monoidal $n$-categories stabilise, so the mechanism is one you will meet repeatedly.

**The homotopy hypothesis is a falsification tool, not just a slogan.** This exercise shows the hypothesis doing real work: it *rejects* a candidate definition. Because we know independently what $\infty$-groupoids should be (spaces), any definition whose groupoidal part fails to reproduce a known space is thereby refuted. The strict definition is refuted by $S^2$; this is concrete, computable evidence, not philosophy. When evaluating any proposed definition of weak ω-category, the most decisive single test is to restrict to its invertible objects and ask whether $S^2$ (or some space with nonzero Whitehead/secondary structure) is among them — if not, the definition is too rigid. This converts the homotopy hypothesis from an aspiration into an operational acceptance/rejection criterion, which is exactly its role across the chapter.
