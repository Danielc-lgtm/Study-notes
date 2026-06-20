---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Monoidal Model Category"
  - "Thm - The Homotopy Category of a Monoidal Model Category is Monoidal"
  - "Def - Cofibrant and Fibrant Objects"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a [[Def - Monoidal Model Category|monoidal model category]] with unit $I$. The [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|derived tensor]] on $\mathrm{Ho}(\mathcal{C})$ has unit object $QI$, the cofibrant replacement of $I$.

(a) Show that **if $I$ is cofibrant**, then the unit axiom is automatic and $I$ itself is the unit for $\otimes^{\mathbf{L}}$, with $I \otimes^{\mathbf{L}} X \cong X$ for all $X$.

(b) Show that the **unit axiom is exactly what is needed** to make $QI$ a unit when $I$ is not cofibrant: namely that $QI \otimes^{\mathbf{L}} X \cong X$ in $\mathrm{Ho}(\mathcal{C})$ for all $X$. Identify precisely where in the argument the unit axiom (as opposed to the pushout-product axiom) is used.

(c) Explain, using **symmetric spectra** (where the sphere spectrum $\mathbb{S}$ is the non-cofibrant unit for the smash product), why the unit axiom is not vacuous and cannot be dropped.

**Recall:**

The **unit axiom** for a [[Def - Monoidal Model Category|monoidal model category]]: for a cofibrant replacement $QI \xrightarrow{\sim} I$ and every cofibrant $X$, the map $QI \otimes X \to I \otimes X \cong X$ is a weak equivalence.

The **derived tensor** is $A \otimes^{\mathbf{L}} B = QA \otimes QB$; $QI$ is already cofibrant, so $QI \otimes^{\mathbf{L}} X = QI \otimes QX$.

An object is [[Def - Cofibrant and Fibrant Objects|cofibrant]] if $\varnothing \to X$ is a cofibration; weak equivalences between cofibrant objects become isomorphisms in $\mathrm{Ho}(\mathcal{C})$.

---

# Convergent Strategy

**Problem class:** This is a *trace-the-role-of-an-axiom* problem: isolate exactly what the unit axiom buys, distinguish it from the pushout-product axiom, and locate the example that makes it non-vacuous. It targets the "unit object is the subtle corner" insight of the topic page.

**Assumption pattern:** The key structural fact is that weak equivalences between *cofibrant* objects become isomorphisms in $\mathrm{Ho}(\mathcal{C})$. The unit axiom hands us exactly such a weak equivalence ($QI \otimes QX \to QX$) between cofibrant objects. When $I$ is cofibrant, $QI = I$ and the map is the unitor, an isomorphism, so nothing is needed.

**Theorem routing:** Part (a) routes through "$I$ cofibrant $\Rightarrow QI = I$ and the comparison is the unitor". Part (b) routes through "$QI \otimes QX \xrightarrow{\sim} QX$ is the unit axiom's weak equivalence between cofibrant objects, hence an iso in $\mathrm{Ho}$" — this is Lemma 3 of [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|the derived-monoidal theorem]]. Part (c) is an example: $\mathbb{S}$ is not cofibrant, so the axiom must be verified rather than assumed.

**Key decision point:** The non-obvious recognition is that the pushout-product axiom alone gives associativity and symmetry of $\otimes^{\mathbf{L}}$ but says *nothing* about the unit — the unit object is not produced by tensoring cofibrant things, it is imposed by the monoidal structure. One must see that $QI \otimes QX \xrightarrow{\sim} QX$ is *not* a consequence of the pushout-product axiom and genuinely requires the separate unit axiom.

---

# Legal Operations Used

1. **Operation 6 (use the unit axiom to compare $QI \otimes X$ with $X$), topic page.** The entire exercise is the careful deployment of this operation and the demonstration that it is irreducible to the pushout-product axiom.

2. **Operation 4 (cofibrantly replace before tensoring), topic page.** We work with $QI \otimes^{\mathbf{L}} X = QI \otimes QX$ throughout, using cofibrant replacement to land in the homotopically meaningful range.

---

# Hints

> [!note]- Hint 1
> Part (a): if $I$ is cofibrant, what is $QI$? And what is the map $QI \otimes X \to I \otimes X \cong X$ then?

> [!note]- Hint 2
> Part (b): $QI \otimes^{\mathbf{L}} X = QI \otimes QX$. The unit axiom gives a weak equivalence $QI \otimes QX \to QX$. Both objects are cofibrant — what does a weak equivalence between cofibrant objects become in $\mathrm{Ho}(\mathcal{C})$?

> [!note]- Hint 3
> Part (b), the subtle point: does the pushout-product axiom imply $QI \otimes QX \simeq QX$? It implies $- \otimes (\text{cofibrant})$ is homotopical, but $QI$ is just *some* cofibrant object — there is no reason $QI \otimes QX \simeq QX$ unless you separately know $QI$ "acts like the unit". That is the unit axiom.

> [!note]- Hint 4
> Part (c): in symmetric spectra the sphere $\mathbb{S}$ is the unit but is not cofibrant. So $Q\mathbb{S} \neq \mathbb{S}$ and the comparison $Q\mathbb{S} \wedge X \to \mathbb{S} \wedge X \cong X$ is a *real* map that must be checked to be a weak equivalence — it is, but only because the unit axiom holds, not for free.

---

# Solution

The route is: (a) when $I$ is cofibrant the unit comparison is the unitor, automatically an iso; (b) in general the unit axiom supplies a weak equivalence between cofibrant objects, which becomes the unit isomorphism in $\mathrm{Ho}$, and this is *not* derivable from the pushout-product axiom; (c) symmetric spectra show the axiom is non-vacuous.

**Step 1 (a): When $I$ is cofibrant, the unit axiom is automatic.**

> [!note]- Derivation
> If $I$ is [[Def - Cofibrant and Fibrant Objects|cofibrant]], we may take $QI = I$ (an object is its own cofibrant replacement when already cofibrant). The unit-axiom map $QI \otimes X \to I \otimes X \xrightarrow{\cong} X$ is then $I \otimes X \xrightarrow{\cong} X$, the unitor $\lambda_X$, which is an isomorphism, hence a weak equivalence. So the unit axiom holds automatically. Consequently $I \otimes^{\mathbf{L}} X = I \otimes QX \cong QX \cong X$ in $\mathrm{Ho}(\mathcal{C})$: $I$ itself is the unit for the derived tensor.

**Step 2 (b): In general $QI$ is the unit, via the unit axiom.**

> [!note]- Derivation
> Compute $QI \otimes^{\mathbf{L}} X = QI \otimes QX$ (note $QI$ is already cofibrant). The [[Def - Monoidal Model Category|unit axiom]] states that $QI \otimes QX \to I \otimes QX \xrightarrow{\cong} QX$ is a weak equivalence, for the cofibrant object $QX$. Now $QI \otimes QX$ is cofibrant (a tensor of cofibrant objects is cofibrant, since $\varnothing \to QI \otimes QX$ is a pushout-product of two cofibrations), and $QX$ is cofibrant. A weak equivalence between cofibrant objects becomes an *isomorphism* in $\mathrm{Ho}(\mathcal{C})$. Therefore
> $$QI \otimes^{\mathbf{L}} X = QI \otimes QX \;\cong\; QX \;\cong\; X \quad \text{in } \mathrm{Ho}(\mathcal{C}),$$
> so $QI$ is a left unit for $\otimes^{\mathbf{L}}$; symmetry gives the right unit. **Where the unit axiom is used:** precisely at "$QI \otimes QX \to QX$ is a weak equivalence". The pushout-product axiom only tells us $- \otimes QX$ is homotopical (preserves weak equivalences of cofibrant objects) — it does *not* tell us that the particular cofibrant object $QI$, tensored with $QX$, returns $QX$. That comparison is extra information, exactly the unit axiom.

**Step 3 (c): Symmetric spectra show the axiom is non-vacuous.**

> [!note]- Derivation
> In the category of symmetric spectra with the smash product $\wedge$, the unit is the sphere spectrum $\mathbb{S}$, and crucially $\mathbb{S}$ is **not cofibrant**. So $Q\mathbb{S} \xrightarrow{\sim} \mathbb{S}$ is a genuine cofibrant replacement with $Q\mathbb{S} \neq \mathbb{S}$, and the unit-axiom comparison $Q\mathbb{S} \wedge X \to \mathbb{S} \wedge X \cong X$ is a non-identity map whose being a weak equivalence is a real theorem about symmetric spectra, not a tautology. If one *dropped* the unit axiom, there would be no guarantee that $Q\mathbb{S} \wedge X \simeq X$, and then $Q\mathbb{S}$ would fail to be a unit for the derived smash product — the stable homotopy category would lack a unit, which is absurd. The unit axiom *holds* for symmetric spectra (this is part of establishing that they form a monoidal model category), but it is verified, not free. This is the historical and structural reason the unit axiom is a separate clause: without categories whose unit is non-cofibrant, one might never have noticed it was needed.

> [!note]- Complete formal solution
> **(a)** If $I$ is [[Def - Cofibrant and Fibrant Objects|cofibrant]], take $QI = I$; the unit-axiom map is the unitor $I \otimes X \cong X$, an isomorphism, so the axiom is automatic and $I \otimes^{\mathbf{L}} X = I \otimes QX \cong X$ in $\mathrm{Ho}(\mathcal{C})$.
> **(b)** In general, $QI \otimes^{\mathbf{L}} X = QI \otimes QX$. The [[Def - Monoidal Model Category|unit axiom]] gives a weak equivalence $QI \otimes QX \xrightarrow{\sim} QX$; both objects are cofibrant (tensors of cofibrant objects are cofibrant), so this becomes an isomorphism in $\mathrm{Ho}(\mathcal{C})$, whence $QI \otimes^{\mathbf{L}} X \cong X$. The unit axiom is used exactly at the weak-equivalence $QI \otimes QX \xrightarrow{\sim} QX$, which the pushout-product axiom does not supply: the latter gives homotopy-invariance of $- \otimes QX$ but not that $QI$ acts as a unit.
> **(c)** In symmetric spectra, the unit $\mathbb{S}$ is not cofibrant, so $Q\mathbb{S} \neq \mathbb{S}$ and the comparison $Q\mathbb{S} \wedge X \to X$ is a genuine map requiring the unit axiom to be a weak equivalence; dropping the axiom would leave the derived smash product without a unit. The axiom holds for symmetric spectra but is non-vacuous. $\qquad\blacksquare$

---

# Key Takeaways

**The pushout-product axiom and the unit axiom do different jobs, and conflating them is the standard error.** The pushout-product axiom makes the *multiplication* $\otimes^{\mathbf{L}}$ homotopical, associative, and symmetric; the unit axiom makes the *unit* $QI$ act as a unit. The exercise pinpoints the irreducibility: knowing $- \otimes (\text{cofibrant})$ is homotopical does not tell you that the specific cofibrant object $QI$ returns its input when tensored, because $QI$ is "just some cofibrant object" until the unit axiom says it behaves like the unit. The transferable diagnostic: when verifying a category is a monoidal model category, treat the unit as a separate obligation — never assume the unit laws descend for free, and always ask "is the unit cofibrant?". If yes, the unit axiom is automatic; if no, it is a theorem to prove.

**"Weak equivalence between cofibrant objects = isomorphism in $\mathrm{Ho}$" is the engine that turns axioms into structure, and the unit axiom is engineered to feed it.** The reason the unit axiom is phrased as "$QI \otimes X \to X$ is a *weak equivalence*" — rather than "is an isomorphism" — is that weak equivalences between cofibrant objects automatically upgrade to isomorphisms in the homotopy category. This is the recurring mechanism throughout the chapter: every coherence isomorphism on $\mathrm{Ho}(\mathcal{C})$ comes from a weak equivalence between cofibrant objects in $\mathcal{C}$. The trigger-reaction pattern: to install an isomorphism on a homotopy category, produce a weak equivalence between cofibrant representatives; the localization does the rest. Recognizing the unit axiom as an instance of this is what makes its phrasing natural rather than arbitrary.

**Symmetric spectra are the cautionary example that justifies the entire unit axiom, illustrating that distinguished elements you do not choose must be separately checked to survive homotopy.** The sphere spectrum is the unit *by force* of the smash-product structure, not by choice, and there is no reason it should be cofibrant — and it is not. This is not a pathology but the generic situation in stable homotopy theory, and the unit axiom is the honest accounting for it. The reusable principle, beyond this chapter: whenever an algebraic structure has a distinguished element forced on you (a unit, a basepoint, a zero object, a canonical generator), do not assume it inherits the good properties of the objects you constructed by hand — verify separately that it survives whatever homotopical or limiting process you apply. The cofibrant objects you built will not vouch for the unit you were handed. See also [[Ex - The derived tensor is well-defined independent of replacement]].
