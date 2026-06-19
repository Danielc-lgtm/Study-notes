---
type: theorem
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Lifting Property and the Retract Argument"
  - "Thm - The Retract Argument"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a model category with weak equivalences $\mathcal{W}$, cofibrations (written $\rightarrowtail$), and fibrations (written $\twoheadrightarrow$); trivial cofibrations and trivial fibrations are the intersections with $\mathcal{W}$. A map $i$ has the **LLP** against $p$ (and $p$ the **RLP** against $i$) if every commuting square with $i$ left, $p$ right has a diagonal — see [[Def - Lifting Property and the Retract Argument]]. We write "closed under retracts/pushouts/pullbacks" in the senses of [[Def - Pullback and Pushout]]. The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

---

# Statement

> **Closure Properties of the Model Structure.** Let $\mathcal{M}$ be a model category. Then:
> 1. **(Lifting characterizations.)** A map is a cofibration if and only if it has the LLP with respect to all trivial fibrations; a map is a trivial cofibration if and only if it has the LLP with respect to all fibrations. Dually, a map is a fibration if and only if it has the RLP with respect to all trivial cofibrations, and a trivial fibration if and only if it has the RLP with respect to all cofibrations.
> 2. **(Retract closure.)** Each of the four classes (cofibrations, trivial cofibrations, fibrations, trivial fibrations) is closed under retracts.
> 3. **(Pushout/pullback closure.)** Cofibrations and trivial cofibrations are closed under pushout; fibrations and trivial fibrations are closed under pullback.
> 4. **(Two determine the third.)** Any two of the three classes $\mathcal{W}$, cofibrations, fibrations determine the third.

---

# Motivation

The axioms of a model category list three classes of maps as if they were independent data, but they are not — they are massively redundant, and this theorem is the precise statement of how. Its role is to convert the *abstract* axiomatic definition into a set of *operational* tools you can actually compute with. The axioms say "there exist factorizations" and "certain lifts exist"; this theorem says "and therefore each class is recognizable by a lifting test, stable under the obvious gluing operations, and recoverable from the other two." That conversion is what makes the subject usable.

The single most important consequence is part (1), the **lifting characterization**. Before it, "cofibration" is opaque — you would need the factorizations in hand to check membership. After it, a cofibration is *exactly* a map passing a lifting test against trivial fibrations, which you can often verify directly. This is what licenses the standard workflow: define a model structure by specifying its weak equivalences and one of the other two classes, then *derive* the third class as "the maps with the appropriate lifting property." It is also what makes the small object argument suffice to build an entire model structure from a small set of generating cofibrations — the rest of the cofibrations are forced as retracts, and the fibrations are forced as the maps lifting against them. Part (4) is the structural summary: a model structure has two degrees of freedom, not three.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypotheses are just "we are in a model category," but each *part* is invoked from a recognizable situation.

The first disguised source is **wanting to prove a specific map is a (co)fibration without the factorizations.** You recognize this whenever a problem hands you a map by a formula and asks for its class. Part (1) routes you to a lifting test: check the map lifts against every trivial fibration. The non-obvious step is that this lifting test, phrased in terms of *all other maps* of a class, is equivalent to membership. *Example problem:* show the inclusion of a subcomplex into a CW complex is a cofibration by verifying the homotopy extension property, which is the lifting test.

The second disguised source is **a gluing or base-change construction.** Whenever you form a pushout along a map or a pullback of a map, part (3) tells you the resulting map stays in its class. You recognize this from any "attach a cell," "form a quotient," or "restrict a fibration to a subspace" situation. The non-obvious step is that the lifting property survives the universal property of the (co)limit. *Example problem:* prove that attaching a cell to a CW complex yields a cofibration, since it is a pushout of the generating cofibration $S^{n-1} \hookrightarrow D^n$.

The third disguised source is **knowing two classes and wanting the third.** When a model structure is specified by its weak equivalences and its cofibrations (as on $\mathbf{Ch}(R)$), part (4) lets you recover the fibrations as "maps with RLP against trivial cofibrations." You recognize this whenever a definition gives you only two classes. The non-obviousness is that the third class is uniquely forced, not a further choice. *Example problem:* given that the cofibrations of $\mathbf{sSet}$ are the monomorphisms and the weak equivalences are the realization-equivalences, identify the fibrations (Kan fibrations) as the RLP-against-trivial-cofibrations maps.

**Targets (Output Amplification)**

The conclusions are the four parts; combined with other facts they amplify.

Combine part (1) with **an explicit generating set.** If you have a *set* $I$ of cofibrations such that the trivial fibrations are exactly the maps with RLP against $I$, then by part (1) the cofibrations are exactly the retracts of maps built from $I$. The amplified result $E$ is **cofibrant generation**: the entire model structure is determined by two small sets, which is what makes it constructible and what the small object argument needs.

Combine part (3) with **transfinite composition.** Cofibrations are closed not only under single pushouts but under transfinite composites of pushouts of generators; the amplified result is the class of **relative cell complexes**, the building blocks of the small object argument and the concrete model for cofibrations.

Combine part (4) with **a Quillen functor.** Knowing that two classes determine the third means a left adjoint that preserves cofibrations and trivial cofibrations automatically interacts correctly with fibrations on the other side (via adjunction); the amplified result is the well-definedness of [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunctions]], where preserving the left classes is equivalent to the right adjoint preserving the right classes.

---

# Why Is It True

The whole theorem rests on one mechanism, and it is the retract argument. Start with the half of part (1) that has content: a map $f$ with the LLP against all trivial fibrations is a cofibration. You do not know $f$ is a cofibration directly — but you can *factor* it. By MC5, write $f = p \circ i$ with $i$ a cofibration and $p$ a trivial fibration. Now $f$ lifts against $p$ (since $p$ is a trivial fibration and $f$ lifts against all of those), so by [[Thm - The Retract Argument|the retract argument]] $f$ is a retract of $i$. Since $i$ is a cofibration and cofibrations are closed under retracts (MC3), $f$ is a cofibration. That is the entire proof of the hard half:

**a map that lifts against its own trivial-fibration factor is a retract of its cofibration factor, hence a cofibration.**

The easy half — every cofibration lifts against all trivial fibrations — is just the lifting axiom MC4. So part (1) is "MC4 one way, retract argument the other way," and it is the template for all four lifting characterizations.

Parts (2), (3), (4) then fall out. Retract closure (part 2) is immediate from part (1), because a class defined by a lifting property is automatically retract-closed (a retract of a map that lifts also lifts — chase the retract diagram through the square). Pushout closure (part 3) is the same: a pushout of a map with LLP against $\mathcal{R}$ still has LLP against $\mathcal{R}$, because a square testing the pushout against $p \in \mathcal{R}$ restricts to a square testing the original, whose lift extends over the pushout by its universal property. And "two determine the third" (part 4) is the observation that fibrations are forced as RLP-against-trivial-cofibrations and weak equivalences are forced as "maps factoring as trivial-cofibration-then-trivial-fibration" — so once two classes are fixed, the lifting characterizations pin down the rest.

---

# What Makes This Hard

The conceptual trap is that part (1) has a trivial half and a substantial half, and beginners prove the trivial half (cofibration $\Rightarrow$ lifts, which is just MC4) and think they are done. The substantial half — lifts $\Rightarrow$ cofibration — is where the retract argument is essential, and it requires *factoring the map first*, an idea that does not appear in the statement. The second common difficulty is the pushout-closure proof: one must see that a lifting square against the *pushout* restricts to a lifting square against the *original* map, and that the original lift then extends uniquely over the pushout by the universal property — getting the direction of this restriction-then-extension right is the crux. The third subtlety is part (4): "determine" means the third class is *uniquely characterized*, which requires checking that the lifting characterization has no ambiguity, not merely that some third class exists.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the lifting characterization (part 1) for cofibrations using factorization plus the retract argument; deduce retract and pushout closure (parts 2, 3) as formal consequences of being defined by a lifting property; obtain the other three lifting characterizations by duality and by the same argument with the other factorization; conclude "two determine the third" (part 4) by reading off the forced descriptions.

**Subgoal decomposition:**

1. **Cofibrations lift against trivial fibrations.** This direction is the axiom.
   - *Hint:* It is exactly MC4 (the cofibration/trivial-fibration lifting axiom).
   - *Why needed:* It is the easy half of the iff; without it the characterization is one-directional.

2. **A map lifting against all trivial fibrations is a cofibration.** Factor $f = p \circ i$ (cofibration, trivial fibration), lift $f$ against $p$, retract.
   - *Hint:* Apply [[Thm - The Retract Argument|the retract argument]] to the factorization; then use MC3.
   - *Why needed:* This is the substantial half and the template for all four characterizations.

3. **Retract closure.** A class defined by a lifting property is closed under retracts.
   - *Hint:* Chase a retract diagram through a lifting square; a lift for the bigger map restricts to a lift for the retract.
   - *Why needed:* It is part (2), and also re-proves MC3 for these classes from part (1).

4. **Pushout/pullback closure.** A pushout of an LLP-map is an LLP-map.
   - *Hint:* A square testing the pushout against $p$ restricts to a square testing the original; extend the lift over the pushout by its universal property.
   - *Why needed:* It is part (3) and underlies cell-attachment.

5. **Two determine the third.** Read off fibrations as RLP-against-trivial-cofibrations and weak equivalences as the maps factoring as trivial-cof then trivial-fib.
   - *Hint:* Use the lifting characterizations from steps 1–2 and their duals.
   - *Why needed:* It is part (4), the structural summary.

---

# Lemma Decomposition

> [!note]- Lemma 1: Lifting characterization of cofibrations
> **Statement:** A map $f$ is a cofibration iff it has the LLP with respect to every trivial fibration.
>
> **Hint:** Forward is MC4; backward is factor-lift-retract.
>
> **Why needed:** It is part (1) for cofibrations and the prototype for the other three.
>
> > [!note]- Full proof
> > ($\Rightarrow$) If $f$ is a cofibration and $p$ a trivial fibration, MC4 supplies the lift in any square. ($\Leftarrow$) Suppose $f$ lifts against all trivial fibrations. Factor $f = p \circ i$ with $i$ a cofibration and $p$ a trivial fibration (MC5). Since $p$ is a trivial fibration, $f$ lifts against $p$, so by [[Thm - The Retract Argument|the retract argument]] $f$ is a retract of $i$. By MC3, cofibrations are closed under retracts, so $f$ is a cofibration.

> [!note]- Lemma 2: A lifting-defined class is closed under retracts
> **Statement:** If $\mathcal{L}$ is the class of maps with LLP against a fixed class $\mathcal{R}$, then $\mathcal{L}$ is closed under retracts.
>
> **Hint:** Given a retract diagram for $f$ over $g \in \mathcal{L}$ and a square testing $f$ against $p \in \mathcal{R}$, paste the retract into the square to get a square for $g$, lift, then push the lift back through the retraction.
>
> **Why needed:** It is part (2), and it shows the lifting characterizations are self-consistent with retract closure.
>
> > [!note]- Full proof
> > Let $f$ be a retract of $g \in \mathcal{L}$ via maps $A \xrightarrow{a} A' \xrightarrow{a'} A$ (composite $\mathrm{id}_A$) and $B \xrightarrow{b} B' \xrightarrow{b'} B$ (composite $\mathrm{id}_B$), with $g : A' \to B'$. Given a square $(u, v)$ testing $f : A \to B$ against $p \in \mathcal{R}$, precompose with the retraction maps $a', b'$ to obtain a square testing $g$ against $p$: top $u \circ a'$, bottom $v \circ b'$. Since $g \in \mathcal{L}$, there is a lift $\ell : B' \to X$. Then $\ell \circ b : B \to X$ is a lift for the original square: $\ell b \circ f = \ell \circ g \circ a$ (using $b f = g a$) $= u a' a = u$, and $p \circ \ell b = v b' b = v$. So $f \in \mathcal{L}$.

> [!note]- Lemma 3: A lifting-defined left class is closed under pushout
> **Statement:** If $\mathcal{L}$ is the class of maps with LLP against a fixed class $\mathcal{R}$ and $f \in \mathcal{L}$, then any pushout $f'$ of $f$ is in $\mathcal{L}$.
>
> **Hint:** A square testing $f'$ against $p$ restricts along the pushout maps to a square testing $f$; lift $f$, then use the pushout's universal property to assemble a lift for $f'$.
>
> **Why needed:** It is part (3), the engine of cell attachment.
>
> > [!note]- Full proof
> > Let $f : A \to B$ be in $\mathcal{L}$ and form the pushout of $f$ along a map $A \to A''$, giving $f'' : A'' \to B''$ with $B'' = A'' \sqcup_A B$. Given a square testing $f''$ against $p \in \mathcal{R}$ (top $u : A'' \to X$, bottom $v : B'' \to Y$), restrict along $A \to A''$ and $B \to B''$ to a square testing $f$. Lift it to $\ell : B \to X$. Now $u : A'' \to X$ and $\ell : B \to X$ agree on $A$ (both restrict to the lift's compatibility), so by the universal property of the pushout they assemble to $\ell'' : B'' \to X$. Check $\ell'' \circ f'' = u$ and $p \circ \ell'' = v$ on each summand; hence $f'' \in \mathcal{L}$. (Pullback closure of the right class is dual.)

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — setup.** Work in a model category $\mathcal{M}$. We freely use MC3 (retract closure of the three given classes), MC4 (lifting), MC5 (factorization), and [[Thm - The Retract Argument|the retract argument]].
>
> **Part (1), cofibrations.** By Lemma 1, $f$ is a cofibration iff $f$ has the LLP against all trivial fibrations. The trivial-cofibration case is identical with "trivial fibration" replaced by "fibration": ($\Rightarrow$) is the trivial-cofibration/fibration half of MC4; ($\Leftarrow$) factor $f = q \circ j$ with $j$ a trivial cofibration and $q$ a fibration, note $f$ lifts against $q$, retract, and use MC3. The fibration and trivial-fibration cases follow by applying the cofibration and trivial-cofibration cases in $\mathcal{M}^{op}$ (where cofibrations and fibrations swap, and LLP and RLP swap).
>
> **Part (2).** Each of the four classes is, by Part (1), the class of maps with a fixed one-sided lifting property. By Lemma 2 (and its dual for right classes), each is closed under retracts.
>
> **Part (3).** Cofibrations and trivial cofibrations are left classes (LLP against trivial fibrations, resp. fibrations); by Lemma 3 each is closed under pushout. Fibrations and trivial fibrations are right classes; by the dual of Lemma 3 each is closed under pullback.
>
> **Part (4).** Suppose the cofibrations and weak equivalences are given. Then trivial fibrations $=$ fibrations $\cap\, \mathcal{W}$ are characterized by Part (1) as the maps with RLP against all cofibrations; and fibrations are the maps with RLP against all trivial cofibrations (the cofibrations that lie in $\mathcal{W}$). Thus the fibrations are determined. The cases "cofibrations and fibrations given" (then $\mathcal{W}$ is the maps factoring as a trivial cofibration followed by a trivial fibration) and "fibrations and weak equivalences given" are symmetric. Hence any two of the three classes determine the third. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Orthogonal factorization systems in category theory.** The (epi, mono) factorization system on $\mathbf{Set}$ is a *strict* analogue: every map factors as a surjection followed by an injection, surjections are exactly the maps with the unique-LLP against injections, and each class is closed under the appropriate (co)limits. Proving these closure properties is the strict-factorization rehearsal for the model-categorical theorem, and it isolates which parts of the argument need the "weak" (non-unique lift) version.

**Projective and injective classes in homological algebra.** In an abelian category, the projective objects are exactly those with the RLP against epimorphisms, and this class is closed under retracts (direct summands) and coproducts. The closure theorem specializes to the standard facts that direct summands of projectives are projective and that the class of projectives is determined by a lifting property against surjections — the homological shadow of part (1) and part (2).

**Closed classes of maps in $\infty$-topos theory.** In the theory of factorization systems on $\infty$-categories, the modalities of homotopy type theory are exactly stable classes of maps closed under pushout and determined by an orthogonality (lifting) condition. The closure theorem is the 1-categorical seed of this; recognizing a "modality" as a pushout-closed, retract-closed, lifting-defined class is the bridge.

---

# Bridges

- **[[Thm - The Retract Argument]]** — the proof engine. Every lifting characterization in part (1) is "MC4 forward, retract argument backward," and parts (2)–(4) are formal consequences of being defined by a lifting property. The closure theorem is what the retract argument was built to deliver.

- **[[Def - Model Category]]** — the theorem is the precise statement that the axioms are overdetermined: a model structure has two degrees of freedom (part 4), and Hovey's formulation exploits this by taking retract-closure as nearly the only axiom and deriving lifting and closure as theorems.

- **The small object argument** — the constructive counterpart. The closure theorem says cofibrations are retracts of maps built from generators; the small object argument *produces* those builds (transfinite cell attachments), and pushout-closure (part 3) is exactly what guarantees each attachment stays a cofibration. Together they make cofibrantly generated model structures workable.

- **[[Def - Quillen Adjunction and Quillen Equivalence]]** — part (4) underlies the symmetry of the definition: a left adjoint preserves cofibrations and trivial cofibrations iff the right adjoint preserves fibrations and trivial fibrations, because the classes are mutually determined by lifting and adjunction transposes lifting problems.

---

# Unlocked by This

> [!tip] Cofibrantly Generated Model Categories *(from Homotopical Algebra)*
> The lifting characterization (part 1) plus a *set* of generating (trivial) cofibrations gives a **cofibrantly generated** model structure: the whole structure is built from two small sets via the small object argument. Almost every model structure in nature — on $\mathbf{Top}$, $\mathbf{sSet}$, $\mathbf{Ch}(R)$, spectra — is of this form.

> [!tip] Factorization Systems and Modalities *(from Higher Category Theory / Type Theory)*
> The closure properties are the 1-categorical seed of **orthogonal factorization systems** on ∞-categories and of the **modalities** of homotopy type theory — stable, lifting-defined, pushout-closed classes of maps. The model-categorical theorem is where the pattern first appears.
