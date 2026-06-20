---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor"
  - "Thm - The Homotopy Category of a Monoidal Model Category is Monoidal"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Monoidal Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a [[Def - Monoidal Model Category|monoidal model category]]. Prove that the [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|derived tensor product]] $A \otimes^{\mathbf{L}} B = QA \otimes QB$ is **independent of the chosen cofibrant replacements** up to canonical isomorphism in $\mathrm{Ho}(\mathcal{C})$, and is **functorial** on $\mathrm{Ho}(\mathcal{C})$. That is:

(a) if $QA, Q'A$ are two cofibrant replacements of $A$ and $QB, Q'B$ two of $B$, then $QA \otimes QB \cong Q'A \otimes Q'B$ in $\mathrm{Ho}(\mathcal{C})$;

(b) a pair of weak equivalences $A \xrightarrow{\sim} A'$, $B \xrightarrow{\sim} B'$ induces an isomorphism $A \otimes^{\mathbf{L}} B \cong A' \otimes^{\mathbf{L}} B'$ in $\mathrm{Ho}(\mathcal{C})$.

Identify precisely where the [[Def - Monoidal Model Category|pushout-product axiom]] is used.

**Recall:**

[[Def - Cofibrant and Fibrant Objects|Cofibrant replacement]]: $QA \xrightarrow{\sim} A$ with $QA$ cofibrant; any two are weakly equivalent (over $A$). A weak equivalence between *cofibrant* objects becomes an isomorphism in $\mathrm{Ho}(\mathcal{C})$.

By [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]], for cofibrant $Z$ the functor $- \otimes Z$ is a left Quillen functor and (by Ken Brown) preserves weak equivalences between cofibrant objects.

---

# Convergent Strategy

**Problem class:** This is a *well-definedness* problem of the kind that underwrites every derived construction: show that a recipe involving choices (here, cofibrant replacements) gives a canonical answer in the homotopy category. It is the foundation on which the derived monoidal structure of §3 rests.

**Assumption pattern:** Two facts carry the proof: (i) any two cofibrant replacements are connected by a weak equivalence between cofibrant objects, hence an isomorphism in $\mathrm{Ho}$; and (ii) tensoring with a cofibrant object preserves weak equivalences between cofibrant objects — this is the pushout-product axiom via Ken Brown. The combination lets a weak equivalence in one variable, with the other variable cofibrant, become an isomorphism in $\mathrm{Ho}$.

**Theorem routing:** The route is: a weak equivalence $QA \xrightarrow{\sim} Q'A$ between cofibrant objects, tensored with cofibrant $QB$, stays a weak equivalence (by [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]] + Ken Brown); both $QA \otimes QB$ and $Q'A \otimes QB$ are cofibrant, so it is an isomorphism in $\mathrm{Ho}$; repeat in the second variable; compose. Functoriality follows the same way from weak equivalences $A \xrightarrow{\sim} A'$ inducing $QA \xrightarrow{\sim} QA'$.

**Key decision point:** The non-obvious discipline is to change *one variable at a time* and to verify at each change that the *other* variable is cofibrant (so the bifunctor theorem applies). Trying to change both replacements simultaneously, or tensoring without checking cofibrancy of the fixed factor, loses the homotopy-invariance. Recognizing that the pushout-product axiom is invoked exactly to license each one-variable change is the heart of the exercise.

---

# Legal Operations Used

1. **Operation 4 (cofibrantly replace before tensoring), topic page.** The derived tensor is defined by this operation, and the exercise shows the result is canonical.

2. **Operation 5 (Ken Brown gives homotopy-invariance on cofibrant objects), topic page.** We use that $- \otimes Z$ for cofibrant $Z$ preserves weak equivalences between cofibrant objects, the precise consequence of the pushout-product axiom needed here.

---

# Hints

> [!note]- Hint 1
> Two cofibrant replacements $QA, Q'A$ of $A$ are weakly equivalent over $A$, and both are cofibrant. What does a weak equivalence between cofibrant objects become in $\mathrm{Ho}(\mathcal{C})$?

> [!note]- Hint 2
> Change one variable at a time. To compare $QA \otimes QB$ with $Q'A \otimes QB$, tensor the weak equivalence $QA \xrightarrow{\sim} Q'A$ with the *cofibrant* object $QB$. Why does it stay a weak equivalence?

> [!note]- Hint 3
> That step uses the pushout-product axiom: $- \otimes QB$ is left Quillen (since $QB$ is cofibrant), so by Ken Brown it preserves weak equivalences between cofibrant objects. This is the *only* place the axiom enters.

> [!note]- Hint 4
> For functoriality, a weak equivalence $A \xrightarrow{\sim} A'$ induces $QA \xrightarrow{\sim} QA'$ between cofibrant objects (naturality of $Q$); tensor with cofibrant $QB$ and repeat the argument.

---

# Solution

The route is: (a) compare replacements one variable at a time, using that weak equivalences between cofibrant objects are $\mathrm{Ho}$-isomorphisms and that $-\otimes(\text{cofibrant})$ preserves them; (b) deduce functoriality from naturality of $Q$. The pushout-product axiom enters exactly at "tensoring with a cofibrant object preserves the relevant weak equivalences".

**Step 1 (a): Independence of the cofibrant replacement.**

> [!note]- Derivation
> Let $QA, Q'A$ be cofibrant replacements of $A$ and $QB, Q'B$ of $B$. The two replacements of $A$ are weakly equivalent over $A$: there is a weak equivalence $w : QA \xrightarrow{\sim} Q'A$ (constructed by lifting, using cofibrancy and the trivial fibrations $QA \to A \leftarrow Q'A$). Both $QA$ and $Q'A$ are [[Def - Cofibrant and Fibrant Objects|cofibrant]]. Tensor $w$ with $QB$: since $QB$ is cofibrant, $- \otimes QB$ is a left Quillen functor (by [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]], applying the pushout-product axiom with the second factor $\varnothing \to QB$), so by Ken Brown's lemma it preserves weak equivalences between cofibrant objects. Hence $w \otimes 1 : QA \otimes QB \xrightarrow{\sim} Q'A \otimes QB$ is a weak equivalence. Both source and target are cofibrant (tensors of cofibrant objects), so $w \otimes 1$ is an *isomorphism* in $\mathrm{Ho}(\mathcal{C})$.

**Step 2 (a continued): Change the second variable.**

> [!note]- Derivation
> Similarly, a weak equivalence $v : QB \xrightarrow{\sim} Q'B$ between the two cofibrant replacements of $B$, tensored with the cofibrant object $Q'A$, gives a weak equivalence $1 \otimes v : Q'A \otimes QB \xrightarrow{\sim} Q'A \otimes Q'B$ between cofibrant objects, hence an isomorphism in $\mathrm{Ho}(\mathcal{C})$. Composing,
> $$QA \otimes QB \;\xrightarrow[\cong]{\,w \otimes 1\,}\; Q'A \otimes QB \;\xrightarrow[\cong]{\,1 \otimes v\,}\; Q'A \otimes Q'B \quad \text{in } \mathrm{Ho}(\mathcal{C}),$$
> so $QA \otimes QB \cong Q'A \otimes Q'B$ in $\mathrm{Ho}(\mathcal{C})$. The isomorphism is canonical because any two choices of $w$ (resp. $v$) are homotopic, hence equal in $\mathrm{Ho}(\mathcal{C})$. Thus $\otimes^{\mathbf{L}}$ is independent of replacement.

**Step 3 (b): Functoriality.**

> [!note]- Derivation
> Let $f : A \xrightarrow{\sim} A'$ and $g : B \xrightarrow{\sim} B'$ be weak equivalences. By functoriality (or naturality up to homotopy) of cofibrant replacement, $f$ lifts to a weak equivalence $Qf : QA \xrightarrow{\sim} QA'$ between cofibrant objects, and $g$ to $Qg : QB \xrightarrow{\sim} QB'$. As in Step 1–2, $Qf \otimes 1$ and $1 \otimes Qg$ are weak equivalences between cofibrant objects (using $- \otimes QB$ and $QA' \otimes -$ left Quillen), hence isomorphisms in $\mathrm{Ho}(\mathcal{C})$. Composing gives an isomorphism
> $$A \otimes^{\mathbf{L}} B = QA \otimes QB \;\cong\; QA' \otimes QB' = A' \otimes^{\mathbf{L}} B' \quad \text{in } \mathrm{Ho}(\mathcal{C}).$$
> Therefore $\otimes^{\mathbf{L}}$ descends to a well-defined bifunctor on $\mathrm{Ho}(\mathcal{C})$, sending isomorphisms (images of weak equivalences) to isomorphisms.

> [!note]- Complete formal solution
> **(a)** Two cofibrant replacements $QA, Q'A$ of $A$ are connected by a weak equivalence $w : QA \xrightarrow{\sim} Q'A$ between [[Def - Cofibrant and Fibrant Objects|cofibrant]] objects, hence an isomorphism in $\mathrm{Ho}(\mathcal{C})$. Since $QB$ is cofibrant, $- \otimes QB$ is left Quillen (by [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]]) and preserves weak equivalences between cofibrant objects (Ken Brown), so $w \otimes 1 : QA \otimes QB \xrightarrow{\sim} Q'A \otimes QB$ is a weak equivalence of cofibrant objects, an iso in $\mathrm{Ho}(\mathcal{C})$. Likewise $1 \otimes v : Q'A \otimes QB \xrightarrow{\sim} Q'A \otimes Q'B$ for a weak equivalence $v$ of the $B$-replacements. Composing, $QA \otimes QB \cong Q'A \otimes Q'B$ in $\mathrm{Ho}(\mathcal{C})$, canonically (choices of $w, v$ are unique up to homotopy). **(b)** Weak equivalences $A \xrightarrow{\sim} A'$, $B \xrightarrow{\sim} B'$ induce $Qf : QA \xrightarrow{\sim} QA'$, $Qg : QB \xrightarrow{\sim} QB'$ between cofibrant objects; tensoring with the appropriate cofibrant factor and composing gives an isomorphism $A \otimes^{\mathbf{L}} B \cong A' \otimes^{\mathbf{L}} B'$ in $\mathrm{Ho}(\mathcal{C})$. The pushout-product axiom is used exactly to know $- \otimes (\text{cofibrant})$ preserves weak equivalences between cofibrant objects. $\qquad\blacksquare$

---

# Key Takeaways

**Well-definedness of a derived functor is always "change one variable at a time, and check the fixed variable is cofibrant".** The proof's shape is universal: to show $QA \otimes QB$ is independent of choices, one varies $A$'s replacement while $B$'s is held cofibrant, then vice versa, never both at once. The reason for the one-at-a-time discipline is that the homotopy-invariance we have (from the pushout-product axiom) is *one-variable*: $- \otimes Z$ is homotopical only for cofibrant $Z$. The transferable diagnostic: whenever proving a derived bifunctor is well-defined, factor the comparison into single-variable weak equivalences, each between cofibrant objects, and invoke one-variable homotopy-invariance at each step. This same template proves well-definedness of $\mathrm{Tor}$, $\mathrm{Ext}$, the derived smash product, and total derived functors generally.

**The pushout-product axiom enters at exactly one point — and that single point is the entire reason the derived tensor exists.** The exercise localizes the axiom's role: it is used only to know $- \otimes (\text{cofibrant})$ preserves weak equivalences between cofibrant objects. Everything else is formal (cofibrant replacements are connected by weak equivalences; weak equivalences between cofibrant objects are $\mathrm{Ho}$-isomorphisms; functoriality of $Q$). This pinpointing is valuable: it tells you precisely what a candidate monoidal model category must satisfy for its derived tensor to be well-defined, and it explains why the pushout-product axiom (not some other compatibility) is *the* axiom. The trigger-reaction pattern: when a derived construction is well-defined, ask "which single homotopy-invariance fact is doing the work?" — usually a one-variable preservation property, here supplied by the pushout-product axiom.

**"Weak equivalence between cofibrant objects becomes an isomorphism in $\mathrm{Ho}$" is used three times in three different roles — it is the workhorse lemma of the whole theory.** It is used to connect two replacements, to upgrade a tensored weak equivalence to an isomorphism, and to make functoriality land in isomorphisms. This one fact, a corollary of the construction of $\mathrm{Ho}(\mathcal{C})$, is what converts the soft data of weak equivalences into the hard data of isomorphisms in the homotopy category. The reusable principle: in any model-categorical argument, your goal is usually to manufacture a weak equivalence between cofibrant (or fibrant) objects, because that is the currency that becomes an isomorphism downstairs. Recognizing when you have such a weak equivalence — and arranging your objects to be cofibrant so that you do — is the central craft of computing in homotopy categories. See also [[Ex - The derived tensor on chain complexes computes Tor]] and [[Ex - The unit of the derived tensor and non-cofibrant units]].
