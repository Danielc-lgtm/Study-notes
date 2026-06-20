---
type: theorem
subject: model-categories
prereqs:
  - "Def - Cofibrantly Generated Model Category"
  - "Def - Relative Cell Complex"
  - "Def - Transfinite Composition and Smallness"
  - "Thm - The Small Object Argument"
  - "Thm - The Retract Argument"
  - "Def - Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a bicomplete category (all small limits and colimits), $\mathcal{W}$ is a class of morphisms (the candidate **weak equivalences**), and $I, J$ are **sets** of morphisms (the candidate generating cofibrations and generating trivial cofibrations). We use the closure operations of [[Def - Relative Cell Complex]]: $I\text{-cell}, I\text{-cof}, I\text{-inj}$ and likewise for $J$. A class $\mathcal{W}$ satisfies **2-out-of-3** if whenever two of $f, g, gf$ are in $\mathcal{W}$, so is the third; it is **closed under retracts** if a retract of a map in $\mathcal{W}$ is in $\mathcal{W}$. "$I$ permits the small object argument" means the domains of $I$ are [[Def - Transfinite Composition and Smallness|small]] relative to $I\text{-cell}$ (and likewise for $J$). The full registry is on [[Model Categories — Cofibrantly Generated Model Categories and the Small Object Argument]].

---

# Statement

> **Theorem (Kan Recognition Theorem; Hovey 2.1.19).** Let $\mathcal{C}$ be a bicomplete category, $\mathcal{W}$ a class of morphisms, and $I, J$ sets of morphisms. Suppose:
> 1. $\mathcal{W}$ satisfies 2-out-of-3 and is closed under retracts;
> 2. the domains of $I$ are small relative to $I\text{-cell}$, and the domains of $J$ are small relative to $J\text{-cell}$ (both sets permit the small object argument);
> 3. $J\text{-cof} \subseteq \mathcal{W} \cap I\text{-cof}$;
> 4. $I\text{-inj} \subseteq \mathcal{W} \cap J\text{-inj}$;
> 5. either $\mathcal{W}\cap I\text{-cof} \subseteq J\text{-cof}$ or $\mathcal{W}\cap J\text{-inj}\subseteq I\text{-inj}$.
>
> Then there is a [[Def - Cofibrantly Generated Model Category|cofibrantly generated model structure]] on $\mathcal{C}$ with $\mathcal{W}$ as the weak equivalences, $I$ as a set of generating cofibrations, and $J$ as a set of generating trivial cofibrations. Its classes are
> $$\mathrm{cof} = I\text{-cof}, \quad \mathrm{triv\text{-}fib} = I\text{-inj}, \quad \mathrm{triv\text{-}cof} = J\text{-cof}, \quad \mathrm{fib} = J\text{-inj}.$$

> **Remark (the two conditions that carry the content).** Conditions 1 and 2 are bookkeeping ($\mathcal{W}$ is well-behaved; the small object argument runs). The substance is in 3–5, which align the two generating sets with $\mathcal{W}$: condition 3 says maps built from $J$ are genuinely trivial cofibrations; conditions 4–5 say the trivial fibrations computed via $I$ agree with "fibration $\cap$ weak equivalence" computed via $J$. The single hypothesis $J\text{-cell}\subseteq\mathcal{W}\cap I\text{-cof}$ implies condition 3, and is the form most often checked in practice.

---

# Motivation

This theorem is how new model categories are born. Verifying the five Quillen axioms directly is brutal — the lifting and factorization axioms quantify over proper classes — and almost no model structure in the literature is established that way. Instead one supplies three pieces of data: the weak equivalences $\mathcal{W}$ (the maps you have decided to invert), a set $I$ of generating cofibrations, and a set $J$ of generating trivial cofibrations. The recognition theorem then says: if these satisfy a short checklist, the entire model structure exists, and it is automatically cofibrantly generated. It converts an open-ended verification of five axioms into a bounded verification of five conditions, most of which are formal.

The role it plays is that of a *factory*. The hardest axioms — lifting (MC4) and factorization (MC5) — are discharged not by hand but by the [[Thm - The Small Object Argument|small object argument]], run twice (once for $I$, once for $J$), which is exactly why condition 2 demands smallness. The remaining axioms reduce to compatibility between the two generating sets and the chosen weak equivalences, captured by conditions 3–5. The theorem is the precise statement of *what compatibility is needed*: it tells you the minimal interface between the combinatorial data $(I, J)$ and the homotopical data $\mathcal{W}$.

The importance is hard to overstate. Every transferred model structure (along an adjunction), every projective or injective model structure on a diagram category, every model structure on algebras over an operad, and every left Bousfield localization is built by checking the conditions of this theorem. It is the standard entry point for putting a homotopy theory on a new category.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is the five-item checklist. The skill is recognizing when a problem hands you the data — $\mathcal{W}, I, J$ — even implicitly, and which condition will be the hard one.

The first disguised source is **an adjunction $F\dashv U$ from an existing cofibrantly generated model category $\mathcal{M}$ to a bicomplete category $\mathcal{N}$**. Here $\mathcal{N}$'s candidate weak equivalences and fibrations are "the maps $U$ sends into $\mathcal{M}$'s," and the candidate generators are $FI, FJ$. The recognition theorem becomes the **transfer theorem**: its conditions specialize to the requirement that $FJ$-cell maps are weak equivalences in $\mathcal{N}$ (the only non-formal condition). The non-obvious step is recognizing that "transfer a model structure" *is* "apply the recognition theorem to $FI, FJ$." *Example problem:* put a model structure on the category of monoids in a monoidal model category by transferring along the free-monoid$\dashv$forgetful adjunction.

The second disguised source is **a diagram category $\mathcal{M}^{\mathcal{D}}$ over a cofibrantly generated $\mathcal{M}$**. The candidate weak equivalences are the objectwise ones, and the generators are $\{i\otimes \mathcal{D}(d,-) : i\in I, d\in\mathcal{D}\}$ (and similarly from $J$). The recognition theorem produces the **projective model structure**. The non-obvious move is that the "free diagram on a generator" construction supplies the right generating set. *Example problem:* construct the projective model structure on functors $\mathcal{D}\to\mathbf{Top}$ to define homotopy colimits.

The third disguised source is **an existing model category whose weak equivalences you wish to enlarge**, keeping the cofibrations. The candidate $\mathcal{W}'\supseteq\mathcal{W}$ is the new (larger) class of equivalences, $I$ stays, and $J$ is enlarged to $J'$ by adding cells that force the new equivalences. This is **left Bousfield localization**, and the recognition theorem (with the hard work in finding $J'$ and checking $J'$-cell $\subseteq\mathcal{W}'$) is what certifies the localized structure. *Example problem:* construct the stable model structure on spectra by localizing the levelwise structure at the stable equivalences.

**Targets (Output Amplification)**

The bare conclusion is a model structure. Combined with other facts it does much more.

Combine the conclusion with **the fundamental theorem of model categories** ([[Thm - The Homotopy Category of a Model Category]]). Once the recognition theorem produces a model structure, the fundamental theorem identifies its homotopy category as bifibrant objects and homotopy classes. The further result is a *computable* homotopy theory: e.g. recognizing the projective model structure on $\mathbf{Ch}(R)$ and then identifying its homotopy category as the derived category $D(R)$. The combination is non-obvious because the recognition theorem alone says nothing about $\mathrm{Ho}$; the fundamental theorem amplifies "a model structure exists" into "here is its homotopy category."

Combine the conclusion with **a Quillen adjunction criterion** ([[Def - Quillen Adjunction and Quillen Equivalence]]). When two model structures are produced by the recognition theorem with related generating sets, an adjunction between the categories is Quillen as soon as the left adjoint sends $I$ to cofibrations and $J$ to trivial cofibrations — and since $I, J$ are *sets*, this is a finite check. The further result is a Quillen adjunction (or equivalence) established by testing only the generators, the standard route to comparing two presentations of a homotopy theory.

Combine the conclusion with **smallness/presentability of the underlying category**. If $\mathcal{C}$ is locally presentable, every object is small, condition 2 is automatic, and the recognition theorem (in Jeff Smith's streamlined form) produces a **combinatorial model category**. The further result is the 1-categorical presentation of a presentable ∞-category — non-obvious because it links a finite verification to the existence of a whole higher-categorical object.

---

# Why Is It True

The theorem is true because the five conditions are *exactly* the five Quillen axioms in disguise, once you agree to define the classes by $\mathrm{cof} = I\text{-cof}$, $\mathrm{fib} = J\text{-inj}$, $\mathcal{W} = \mathcal{W}$. Let us walk the correspondence; this is the whole intuition.

Bicompleteness (MC1) is hypothesis on $\mathcal{C}$. The 2-out-of-3 and retract axioms (MC2, MC3 for $\mathcal{W}$) are condition 1. The retract axiom for the other classes is automatic, because $I\text{-cof}$ and $J\text{-inj}$ are lifting classes, hence retract-closed for free.

Factorization (MC5) is the [[Thm - The Small Object Argument|small object argument]], run twice. Condition 2 (smallness) is precisely what lets it run. Applied to $I$, it factors any map as (relative $I$-cell)$\circ$($I$-injective) $=$ (cofibration)$\circ$(trivial fibration), *provided* $I$-inj is the trivial fibrations — which is condition 4 telling us $I\text{-inj}\subseteq\mathcal{W}$. Applied to $J$, it factors any map as ($J$-cell)$\circ$($J$-injective) $=$ (trivial cofibration)$\circ$(fibration), *provided* $J$-cell is trivial cofibrations — which is condition 3 telling us $J\text{-cof}\subseteq\mathcal{W}$.

Lifting (MC4) is half-automatic and half-content. Cofibrations $=I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ lift against trivial fibrations $=I\text{-inj}$ *by definition*. Trivial cofibrations $=J\text{-cof}$ lift against fibrations $=J\text{-inj}$ *by definition*. The content is showing these are the *only* lifting relations — that a trivial cofibration is really a cofibration that is a weak equivalence, so that the two lifting systems are compatible. This is where conditions 3, 4, 5 do their work: they force
$$\mathrm{triv\text{-}cof} := J\text{-cof} = \mathcal{W}\cap I\text{-cof} = \mathcal{W}\cap\mathrm{cof}, \qquad \mathrm{triv\text{-}fib} := I\text{-inj} = \mathcal{W}\cap J\text{-inj} = \mathcal{W}\cap\mathrm{fib},$$
which is exactly the statement that "trivial" means "$\cap\,\mathcal{W}$" for both classes — the compatibility MC4 needs.

> **The recognition theorem is true because conditions 3–5 are precisely the statements that $J$-cof $=\mathcal{W}\cap I$-cof and $I$-inj $=\mathcal{W}\cap J$-inj — i.e. that "trivial cofibration" really means "cofibration and weak equivalence," and dually — which is the only compatibility the two small-object-argument factorizations need to assemble into a single model structure.**

So nothing is mysterious: the theorem is the bookkeeping that the two weak factorization systems $(I\text{-cof}, I\text{-inj})$ and $(J\text{-cof}, J\text{-inj})$, glued along $\mathcal{W}$, satisfy the model axioms, and conditions 3–5 are exactly the gluing compatibility.

---

# What Makes This Hard

The proof is mostly assembly; the genuine difficulty is the two non-formal identities $J\text{-cof} = \mathcal{W}\cap I\text{-cof}$ and $I\text{-inj} = \mathcal{W}\cap J\text{-inj}$, and in particular the *reverse* inclusions $\mathcal{W}\cap I\text{-cof}\subseteq J\text{-cof}$ (condition 5). This is where the [[Thm - The Retract Argument|retract argument]] enters: to show a trivial cofibration $f$ (a weak equivalence in $I\text{-cof}$) lies in $J\text{-cof}$, factor it via the small object argument on $J$ as $f = p\circ i$ with $i\in J\text{-cell}\subseteq J\text{-cof}$ and $p\in J\text{-inj}$; then $p$ is a weak equivalence by 2-out-of-3, so $p\in\mathcal{W}\cap J\text{-inj} = I\text{-inj}$ (condition 4), so $f$ lifts against $p$, and the retract argument puts $f\in J\text{-cof}$. Most people get stuck here, either forgetting to invoke 2-out-of-3 to upgrade $p$ to a weak equivalence, or forgetting that $f\in I\text{-cof}$ is what gives the lift against $p\in I\text{-inj}$. The other common error is treating conditions 3 and 4 as redundant; they are independent, governing the two factorizations separately.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Define $\mathrm{cof} = I\text{-cof}$, $\mathrm{fib} = J\text{-inj}$, weak equivalences $=\mathcal{W}$. Get bicompleteness, 2-out-of-3, retracts from the hypotheses. Get both factorizations from the small object argument (condition 2). The remaining work is the two identities $\mathrm{triv\text{-}cof} = J\text{-cof} = \mathcal{W}\cap I\text{-cof}$ and $\mathrm{triv\text{-}fib} = I\text{-inj} = \mathcal{W}\cap J\text{-inj}$, which give lifting (MC4); the retract argument supplies the reverse inclusions.

**Subgoal decomposition:**

1. **Cheap axioms.** MC1 (bicomplete) is hypothesis; MC2, MC3 for $\mathcal{W}$ are condition 1; retract-closure of $I\text{-cof}, J\text{-inj}$ is automatic.
   - *Hint:* $\mathrm{LLP}$- and $\mathrm{RLP}$-classes are always retract-closed.
   - *Why needed:* These are three of the five axioms, dispatched immediately.

2. **Factorizations (MC5).** Run the small object argument on $I$ and on $J$.
   - *Hint:* Condition 2 is exactly the smallness the [[Thm - The Small Object Argument|small object argument]] needs; conditions 3, 4 identify the factors as the (co)fibrations and trivial (co)fibrations.
   - *Why needed:* Produces both required factorizations.

3. **One easy lifting identity.** Show $J\text{-cof}\subseteq\mathcal{W}\cap I\text{-cof}$ and $I\text{-inj}\subseteq\mathcal{W}\cap J\text{-inj}$.
   - *Hint:* These are conditions 3 and 4 verbatim.
   - *Why needed:* The forward inclusions of the two compatibility identities.

4. **The hard reverse inclusion.** Show $\mathcal{W}\cap I\text{-cof}\subseteq J\text{-cof}$ (condition 5, or derive its dual).
   - *Hint:* Factor a trivial cofibration via the small object argument on $J$, upgrade the $J$-injective factor to a weak equivalence by 2-out-of-3, conclude it is $I$-injective by condition 4, lift, and apply the retract argument.
   - *Why needed:* Completes $J\text{-cof} = \mathcal{W}\cap I\text{-cof}$, hence MC4.

5. **Assemble.** Conclude that $(\mathcal{C}, \mathcal{W}, I\text{-cof}, J\text{-inj})$ satisfies MC1–MC5 and is cofibrantly generated by $I, J$.
   - *Hint:* MC4 is now immediate from the two identities; everything is in place.
   - *Why needed:* This is the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Lifting classes are retract-closed and the cheap axioms hold
> **Statement:** $I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ and $J\text{-inj} = \mathrm{RLP}(J)$ are closed under retracts; together with condition 1, axioms MC1–MC3 hold for $(\mathcal{C}, \mathcal{W}, I\text{-cof}, J\text{-inj})$.
>
> **Hint:** A retract of a map with a lifting property has the same lifting property, by composing the retract diagram with the lift.
>
> **Why needed:** Dispatches three of the five axioms with no further work.
>
> > [!note]- Full proof
> > MC1 (bicompleteness) is a hypothesis on $\mathcal{C}$. MC2 (2-out-of-3 for $\mathcal{W}$) and MC3 for $\mathcal{W}$ (retract-closure) are condition 1. For the cofibrations and fibrations: if $f$ is a retract of $g$ and $g\in\mathrm{LLP}(\mathcal{R})$, then given a lifting square for $f$ against $p\in\mathcal{R}$, paste the retract diagram to get a square for $g$, lift it (using $g$'s LLP), and restrict the lift back along the retraction to solve $f$'s square. So $\mathrm{LLP}$-classes are retract-closed; dually for $\mathrm{RLP}$-classes. Hence MC3 holds for all three classes. $\square$

> [!note]- Lemma 2: The small object argument supplies both factorizations
> **Statement:** Every map factors as (relative $I$-cell)$\circ$($I$-injective) and as ($J$-cell)$\circ$($J$-injective); under conditions 3, 4 these read as (cofibration)$\circ$(trivial fibration) and (trivial cofibration)$\circ$(fibration).
>
> **Hint:** Condition 2 gives smallness; apply [[Thm - The Small Object Argument]] to $I$ and to $J$. The relative cell complexes are cofibrations / trivial cofibrations by Lemma 3 below; the injectives are trivial fibrations / fibrations by conditions 4, 3.
>
> **Why needed:** This is MC5, the hard existence axiom.
>
> > [!note]- Full proof
> > By condition 2 the domains of $I$ are small relative to $I\text{-cell}$, so [[Thm - The Small Object Argument|the small object argument]] factors any $f$ as $i(f)\in I\text{-cell}$ followed by $p(f)\in I\text{-inj}$. By the corollary of that theorem $i(f)\in I\text{-cof} = \mathrm{cof}$, and $p(f)\in I\text{-inj}\subseteq\mathcal{W}$ (condition 4) and $p(f)\in J\text{-inj} = \mathrm{fib}$ (condition 4), so $p(f)$ is a trivial fibration. This is the (cofibration, trivial fibration) factorization. Identically, the small object argument on $J$ (condition 2 for $J$) gives $i'(f)\in J\text{-cell}\subseteq J\text{-cof} = \mathrm{triv\text{-}cof}$ and $p'(f)\in J\text{-inj} = \mathrm{fib}$. By condition 3, $J\text{-cof}\subseteq\mathcal{W}$, so $i'(f)$ is a trivial cofibration. This is the (trivial cofibration, fibration) factorization. $\square$

> [!note]- Lemma 3: The compatibility identities (MC4)
> **Statement:** $J\text{-cof} = \mathcal{W}\cap I\text{-cof}$ and $I\text{-inj} = \mathcal{W}\cap J\text{-inj}$.
>
> **Hint:** The forward inclusions are conditions 3, 4. For $\mathcal{W}\cap I\text{-cof}\subseteq J\text{-cof}$ (condition 5), factor a trivial cofibration through $J$, promote the $J$-injective factor to a weak equivalence by 2-out-of-3, recognize it as $I$-injective via condition 4, and retract.
>
> **Why needed:** These two identities *are* the content of MC4 — they say the cofibrations lifting against fibrations are exactly the trivial cofibrations, and dually.
>
> > [!note]- Full proof
> > Forward: condition 3 gives $J\text{-cof}\subseteq\mathcal{W}\cap I\text{-cof}$; condition 4 gives $I\text{-inj}\subseteq\mathcal{W}\cap J\text{-inj}$.
> >
> > Reverse, $\mathcal{W}\cap I\text{-cof}\subseteq J\text{-cof}$ (this is condition 5, but we show how it forces the structure). Let $f : X\to Y$ be in $\mathcal{W}\cap I\text{-cof}$. By Lemma 2 (small object argument on $J$) factor $f = p\circ i$ with $i\in J\text{-cell}\subseteq J\text{-cof}$ and $p\in J\text{-inj}$. By condition 3, $i\in\mathcal{W}$; since $f\in\mathcal{W}$ and $f = p\, i$, 2-out-of-3 gives $p\in\mathcal{W}$. Thus $p\in\mathcal{W}\cap J\text{-inj} = I\text{-inj}$ by condition 4. Now $f\in I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ and $p\in I\text{-inj}$, so $f$ lifts against $p$: the square with $i$ across the top, $p$ down the right, $f$ down the left, and $\mathrm{id}_Y$ across the bottom has a diagonal $r$ with $r f = i$, $p r = \mathrm{id}_Y$. By the [[Thm - The Retract Argument|retract argument]], $f$ is a retract of $i\in J\text{-cof}$, hence $f\in J\text{-cof}$ (Lemma 1, retract-closure). So $\mathcal{W}\cap I\text{-cof}\subseteq J\text{-cof}$.
> >
> > The other reverse inclusion $\mathcal{W}\cap J\text{-inj}\subseteq I\text{-inj}$ follows by the dual argument (or is the alternative form of condition 5), completing both identities. $\square$

> [!note]- Lemma 4: The classes assemble into a cofibrantly generated model structure
> **Statement:** With $\mathrm{cof} = I\text{-cof}$, $\mathrm{fib} = J\text{-inj}$, weak equivalences $\mathcal{W}$, the data satisfies MC1–MC5 and is cofibrantly generated by $(I, J)$.
>
> **Hint:** MC1–MC3 from Lemma 1, MC5 from Lemma 2, MC4 from Lemma 3; the definition of cofibrant generation is met by $I, J$.
>
> **Why needed:** It is the conclusion of the theorem.
>
> > [!note]- Full proof
> > MC1, MC2, MC3: Lemma 1. MC5: Lemma 2. For MC4, the trivial cofibrations are $\mathcal{W}\cap I\text{-cof} = J\text{-cof}$ (Lemma 3), which lift against $J\text{-inj} = \mathrm{fib}$ by definition; the trivial fibrations are $\mathcal{W}\cap J\text{-inj} = I\text{-inj}$ (Lemma 3), against which $I\text{-cof} = \mathrm{cof}$ lifts by definition. So both lifting axioms hold. Finally the four classes are $\mathrm{cof} = I\text{-cof}$, $\mathrm{triv\text{-}fib} = I\text{-inj}$, $\mathrm{triv\text{-}cof} = J\text{-cof}$, $\mathrm{fib} = J\text{-inj}$ with $I, J$ small-domain sets — exactly the definition of [[Def - Cofibrantly Generated Model Category|cofibrantly generated]]. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Assume the five hypotheses. Define classes on $\mathcal{C}$: weak equivalences $= \mathcal{W}$, cofibrations $= I\text{-cof}$, fibrations $= J\text{-inj}$. We verify MC1–MC5.
>
> **Step 0 — the constructions are available.** $\mathcal{C}$ is bicomplete (MC1), so all (co)limits, the small object argument's colimits, and the retract diagrams below exist; the small object argument applies to $I$ and $J$ by condition 2.
>
> **Step 1 — MC1, MC2, MC3.** Bicompleteness is MC1. By condition 1, $\mathcal{W}$ has 2-out-of-3 (MC2) and is retract-closed; by Lemma 1 the lifting classes $I\text{-cof}, J\text{-inj}$ are retract-closed, so MC3 holds for all three classes.
>
> **Step 2 — MC5.** By Lemma 2, every map factors as (cofibration)$\circ$(trivial fibration) — via the small object argument on $I$, with the injective factor a trivial fibration by condition 4 — and as (trivial cofibration)$\circ$(fibration) — via the small object argument on $J$, with the cell factor a trivial cofibration by condition 3.
>
> **Step 3 — the compatibility identities.** By Lemma 3,
> $$J\text{-cof} = \mathcal{W}\cap I\text{-cof} \quad\text{and}\quad I\text{-inj} = \mathcal{W}\cap J\text{-inj}.$$
> The forward inclusions are conditions 3, 4; the reverse inclusions use the small object argument on $J$, 2-out-of-3, condition 4, and the retract argument (full detail in Lemma 3).
>
> **Step 4 — MC4.** The trivial cofibrations are $\mathcal{W}\cap I\text{-cof} = J\text{-cof}$, which by definition lift against $J\text{-inj} = \mathrm{fib}$. The trivial fibrations are $\mathcal{W}\cap J\text{-inj} = I\text{-inj}$, against which $I\text{-cof} = \mathrm{cof}$ lifts by definition. Both lifting axioms hold.
>
> **Step 5 — conclusion.** All five axioms hold, so $(\mathcal{C}, \mathcal{W}, I\text{-cof}, J\text{-inj})$ is a model category. Its four classes are $\mathrm{cof} = I\text{-cof}$, $\mathrm{triv\text{-}fib} = I\text{-inj}$, $\mathrm{triv\text{-}cof} = J\text{-cof}$, $\mathrm{fib} = J\text{-inj}$, generated by the small-domain sets $I, J$; hence the model structure is cofibrantly generated by $(I, J)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Transferring a model structure to algebras over a monad.** Given a cofibrantly generated model category $\mathcal{M}$ and a monad $T$ with a free$\dashv$forgetful adjunction, attempt to transfer the model structure to $T$-algebras by taking $TI, TJ$ as generators and declaring weak equivalences/fibrations to be those detected by the forgetful functor. The recognition theorem's conditions reduce to a single one — $TJ$-cell maps are weak equivalences — and the exercise is to identify when this "acyclicity of transferred cells" holds (it does for nice $T$, e.g. when $\mathcal{M}$ has a fibrant-replacement-compatible path object). This grounds the user's interest in operadic and monadic structures in concrete homotopy theory: model structures on algebras over an **operad** are built exactly this way.

**The projective model structure and homotopy colimits.** Build the projective model structure on $\mathbf{Top}^{\mathcal{D}}$ for a small category $\mathcal{D}$ by applying the recognition theorem to objectwise weak equivalences and the generating set $\{(S^{n-1}\hookrightarrow D^n)\otimes\mathcal{D}(d,-)\}$. The exercise is to check the conditions and then identify the derived functor of $\mathrm{colim} : \mathbf{Top}^{\mathcal{D}}\to\mathbf{Top}$ as the homotopy colimit. The non-obvious recognition is that the "free diagram on a generator at $d$" is the correct generating cofibration, and that objectwise smallness is inherited from $\mathbf{Top}$.

**Recognizing a model structure on a category of sheaves.** On chain complexes of sheaves of $\mathcal{O}_X$-modules, supply quasi-isomorphisms as $\mathcal{W}$ and generators built from twists of the structure sheaf, and verify the recognition conditions to obtain the model structure whose homotopy category is the derived category of the scheme. The exercise highlights where local presentability of the sheaf category (a Grothendieck topos) makes condition 2 automatic, and where the substantive condition 3 (acyclicity of $J$-cells) becomes a statement about exactness of the cell attachments. This is the bridge into derived algebraic geometry.

---

# Bridges

- **[[Thm - The Small Object Argument|The Small Object Argument]]** — the existence engine inside the recognition theorem. The recognition theorem invokes it *twice*, once for $I$ to get the (cofibration, trivial fibration) factorization and once for $J$ to get the (trivial cofibration, fibration) factorization. Without the small object argument the recognition theorem would have no way to discharge MC5; condition 2 (smallness) is present solely to license these two invocations.

- **[[Thm - The Retract Argument|The Retract Argument]]** — the tool for the hard reverse inclusion. To show a trivial cofibration lies in $J\text{-cof}$, the proof factors it through $J$, upgrades the injective factor to a weak equivalence, recognizes it as $I$-injective, lifts, and retracts. The retract argument is what turns "lifts against the right class" into "belongs to the class," completing the compatibility identity that is MC4.

- **[[Def - Cofibrantly Generated Model Category|Cofibrantly Generated Model Category]]** — the output. The recognition theorem does not merely produce a model structure; it produces a cofibrantly generated one, with the given $I, J$ as generators. The two are companion statements: the definition says what cofibrant generation is, and the recognition theorem says how to verify it from scratch.

- **The transfer theorem (Crans) and Jeff Smith's theorem** — specializations. Crans' transfer theorem is the recognition theorem applied to $FI, FJ$ for an adjunction $F\dashv U$, with the conditions specialized to "$FJ$-cell maps are weak equivalences." Jeff Smith's theorem is the recognition theorem for locally presentable $\mathcal{C}$ (where condition 2 is automatic) requiring only a generating set of cofibrations and an accessible class of weak equivalences satisfying a solution-set condition. Both are the standard industrial forms of this theorem.

- **Left Bousfield localization** — an iterated application. Localizing a model category at a set of maps re-runs the recognition theorem with the same $I$ but an enlarged $J'$ and a larger $\mathcal{W}'$; the hard condition becomes the acyclicity $J'$-cell $\subseteq\mathcal{W}'$, which is the technical heart of the localization construction.

---

# Unlocked by This

> [!tip] Combinatorial Model Categories and Presentable ∞-Categories *(from Higher Category Theory)*
> Applied to a locally presentable $\mathcal{C}$ — where condition 2 is automatic — the recognition theorem (in Jeff Smith's form) produces a **combinatorial model category**. These present exactly the **presentable ∞-categories** that are the foundation of Lurie's higher algebra, and the recognition theorem is the standard tool for constructing them.

> [!tip] Model Structures on Algebras, Monoids, and Operads *(from Homotopical Algebra)*
> Transferring a cofibrantly generated model structure along a free$\dashv$forgetful adjunction, via this theorem, puts model structures on categories of **monoids in a monoidal model category**, modules, and **algebras over an operad** — the homotopy theory of structured objects, central to derived algebra and to the user's interest in operadic and compositional structures.

> [!tip] The Projective and Injective Model Structures on Diagrams *(from Homological Algebra)*
> The recognition theorem builds the **projective model structure** on diagram categories $\mathcal{M}^{\mathcal{D}}$ (generators $\{i\otimes\mathcal{D}(d,-)\}$), which is how **homotopy colimits** over a fixed shape are organized; dualizing gives the **injective model structure** underlying homotopy limits, descent, and the theory of homotopy sheaves.
