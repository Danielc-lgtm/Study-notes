---
type: theorem
subject: model-categories
prereqs:
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a category (in applications a model category) and $f, g, i, p$ are morphisms. We write $g \circ f$ for composition and $\mathrm{id}_A$ for the identity of $A$. A map $i$ has the **left lifting property** (LLP) against $p$, and $p$ the **right lifting property** (RLP) against $i$, if every commuting square with $i$ on the left and $p$ on the right has a diagonal filler; $f$ is a **retract** of $g$ if it sits inside $g$ via a retract diagram whose horizontal composites are identities — see [[Def - Lifting Property and the Retract Argument]]. The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

---

# Statement

> **The Retract Argument.** Let $f = p \circ i$ be a factorization of a morphism $f : A \to B$ in a category $\mathcal{C}$, so $i : A \to C$ and $p : C \to B$. If $f$ has the **left lifting property** with respect to $p$, then $f$ is a **retract of $i$**.

> **Dual form.** Dually, if $f = p \circ i$ and $f$ has the **right lifting property** with respect to $i$, then $f$ is a **retract of $p$**.

The two forms are exchanged by passing to the opposite category $\mathcal{C}^{op}$, where left and right lifting properties swap and the roles of $i$ and $p$ reverse; it therefore suffices to prove the first.

---

# Motivation

This lemma looks slight — three lines of diagram chase — but it is the hinge on which the whole logical economy of model categories turns. Its role is to make the axioms **overdetermined**: it shows that the lifting axiom MC4 and the factorization axiom MC5, which appear independent, are in fact tightly coupled, so that the three classes of a model structure are far more rigidly determined than the axioms suggest.

The concrete need it answers is this. Suppose you want to prove some specific map $f$ is a cofibration. The definition of cofibration is opaque — you would need to know the factorizations explicitly to check it directly. But suppose you can show $f$ has the LLP against every trivial fibration. Then you would *like* to conclude $f$ is a cofibration, and the retract argument is what lets you: factor $f = p \circ i$ with $i$ a cofibration and $p$ a trivial fibration (by MC5), observe that $f$ lifts against $p$ (by hypothesis), conclude $f$ is a retract of $i$ (by this lemma), and finally that $f$ is a cofibration (since cofibrations are closed under retracts, by MC3). Without the retract argument, the lifting characterization of the classes — the single most useful structural fact in the subject — would be unprovable. The lemma is small because it is doing exactly one job, but that job is load-bearing for everything in [[Thm - Closure Properties of the Model Structure]].

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is "$f$ factors as $p \circ i$ and $f$ lifts against $p$." The skill is recognizing when a problem secretly supplies both.

The first disguised source is **"$f$ lifts against all maps of a class $\mathcal{R}$, and $\mathcal{R}$ contains the second factor of some factorization of $f$."** In a model category, MC5 hands you a factorization of *every* map for free, so the moment you know $f$ lifts against all trivial fibrations, you automatically have the factorization $f = p \circ i$ with $p$ a trivial fibration, and the hypothesis is met. The non-obvious step is realizing the factorization is always available. *Example problem:* prove that a map with LLP against all trivial fibrations is a cofibration — factor it and apply the lemma.

The second disguised source is **a map already known to lie in a class defined by lifting.** If $f$ is a trivial cofibration, it lifts against all fibrations by MC4; combined with the trivial-cofibration/fibration factorization of $f$, the lemma shows $f$ is a retract of its own trivial-cofibration factor — a consistency check that recovers retract-closure. The non-obviousness is using the axiom MC4 to *supply* the lifting property rather than to consume it. *Example problem:* show every trivial cofibration is a retract of a relative cell complex built from generating trivial cofibrations.

The third disguised source is **the dual situation, recognized by turning the diagram around.** Any RLP statement about a map $p$ becomes an LLP statement in $\mathcal{C}^{op}$, so a problem about fibrations (RLP against trivial cofibrations) feeds the dual form of the lemma. The non-obvious step is the willingness to dualize rather than re-prove. *Example problem:* prove a map with RLP against all trivial cofibrations is a fibration, by the dual retract argument.

**Targets (Output Amplification)**

The bare conclusion is "$f$ is a retract of $i$ (or $p$)." Combined with closure axioms it does much more.

Combine the conclusion with **retract-closure of a class (MC3)**. If $i$ is a cofibration and the lemma shows $f$ is a retract of $i$, then $f$ is a cofibration. The amplified result $E$ is the **lifting characterization**: cofibrations are exactly the maps with LLP against trivial fibrations. This is non-obvious because it converts a property phrased entirely in terms of *other* maps (lifting) into membership in the class itself.

Combine the conclusion with **the small object argument's output.** The small object argument factors any map as (cell complex)-then-(map lifting the right way); the retract argument then shows any map with the appropriate lifting property is a retract of a cell complex. The amplified result is a *structural description* of an entire class — every cofibration is a retract of a relative cell complex — which is the starting point for recognizing cofibrations in practice.

Combine the conclusion with **two-out-of-three.** If $f$ is a retract of $i$ and $i$ is a weak equivalence, then by MC3 $f$ is a weak equivalence; combining with a factorization where the other factor is also controlled lets you deduce that a map is a *trivial* cofibration. The amplified result is the simultaneous determination of two of the three classes, feeding the "any two classes determine the third" statement.

---

# Why Is It True

Picture the factorization $f = p \circ i$ as $A \xrightarrow{i} C \xrightarrow{p} B$, and picture what you are trying to build: a retract diagram exhibiting $f$ as a "summand" of $i$. A retract of $i$ needs a map $C \to A$ (a retraction back to the domain of $f$) compatible with everything. Where could such a map come from? You have a lifting property, and a lifting property *produces maps*. So set up the one square whose lift is the retraction you need.

The square is forced. Put $i$ on the left and $p$ on the right — these are the two factors of $f$. The top map $A \to C$ is $i$ itself; the bottom map $C \to B$ is $p$ itself. This square commutes because both composites are $f = p \circ i$. Now $f$ lifts against $p$ by hypothesis, and the square is really a square with $f$ on the left after a relabelling: the lift is a map $r : C \to A$ — wait, more precisely, the lift in the square testing $f$ against $p$ gives exactly the diagonal $C \to C$ — let us be careful and let the proof below pin down the indices. The essential point is the slogan:

**the retraction is the lift, and the lift exists because $f$ has the lifting property against its own fibration-factor.**

Once you have the lift, assembling the retract diagram is bookkeeping: the lift provides the middle vertical of the retract square, the factors $i$ and $p$ provide the horizontals, and the lifting equations $h \circ i = f$, $p \circ h = g$ guarantee the horizontal composites are identities. The deep content is entirely in the one observation that a map's lifting property against its second factor manufactures a retraction onto its first factor. Everything else is drawing the diagram.

---

# What Makes This Hard

The difficulty is purely in setting up the *correct* square — choosing what goes on top, on the bottom, on the left, and on the right so that the lift is the map you want. Most people draw a square that commutes but whose lift is useless, because they put the wrong maps on the boundary. The non-obvious step is realizing that the square must use $i$ as its top edge and $p$ as its right edge (so that the lift lands in $C$ and the equations $h i = i$-side, $p h = p$-side hold), making the lift the retraction $C \to C$ that splits. The common error afterwards is mislabelling which composite in the assembled retract diagram is the identity; carefully tracking that $r \circ i = \mathrm{id}_A$ on the domain and the corresponding identity on the codomain is where the chase is won or lost.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build a single commuting square with the factorization map $i$ across the top and the fibration-factor $p$ down the right; the hypothesized lifting property of $f$ against $p$ produces a diagonal, and that diagonal is the retraction that exhibits $f$ as a retract of $i$. Then assemble the retract diagram and check the two horizontal composites are identities.

**Subgoal decomposition:**

1. **Set up the lifting square.** Form the square with $f : A \to B$ on the left, $p : C \to B$ on the right, top map $i : A \to C$, bottom map $\mathrm{id}_B : B \to B$.
   - *Hint:* Check it commutes: $p \circ i = f = \mathrm{id}_B \circ f$.
   - *Why needed:* This is the square whose lift will be the retraction.

2. **Produce the lift.** Since $f$ has the LLP against $p$, obtain $r : B \to C$ with $r \circ f = i$ and $p \circ r = \mathrm{id}_B$.
   - *Hint:* The lift exists by the lifting hypothesis; read off its two defining equations.
   - *Why needed:* $r$ is the right-hand vertical of the retract diagram.

3. **Assemble the retract diagram.** Build the two-row diagram with $f$, $i$, $f$ as the verticals and $(\mathrm{id}_A, \mathrm{id}_A)$, $(r, p)$ as the horizontals.
   - *Hint:* Top row $A \xrightarrow{\mathrm{id}} A \xrightarrow{\mathrm{id}} A$; middle column uses $i$; the maps $B \xrightarrow{r} C \xrightarrow{p} B$ form the bottom-row return.
   - *Why needed:* This diagram is the definition of "$f$ is a retract of $i$."

4. **Verify the horizontal composites are identities.** Check the top composite is $\mathrm{id}_A$ and the bottom composite $p \circ r = \mathrm{id}_B$.
   - *Hint:* The bottom identity is exactly the second lifting equation from step 2.
   - *Why needed:* It is the condition that makes the diagram a *retract* diagram rather than merely commuting.

---

# Lemma Decomposition

> [!note]- Lemma 1: The lifting square commutes
> **Statement:** With $f = p \circ i$, the square having $f$ on the left, $p$ on the right, $i$ on top, and $\mathrm{id}_B$ on the bottom commutes.
>
> **Hint:** Both composites around the square equal $f$.
>
> **Why needed:** A lift exists only for a *commuting* square; this is the precondition for invoking the lifting property.
>
> > [!note]- Full proof
> > Going across the top then down the right: $p \circ i = f$. Going down the left then across the bottom: $\mathrm{id}_B \circ f = f$. The two agree, so the square commutes.

> [!note]- Lemma 2: The lift is a section of $p$ and a "co-section" along $f$
> **Statement:** A diagonal lift $r$ of the square in Lemma 1 satisfies $r \circ f = i$ and $p \circ r = \mathrm{id}_B$.
>
> **Hint:** These are precisely the two equations a diagonal filler must satisfy: it agrees with the top map after the left edge, and with the bottom map after the right edge.
>
> **Why needed:** $p \circ r = \mathrm{id}_B$ is the identity that makes the bottom row of the retract diagram compose to $\mathrm{id}_B$; $r \circ f = i$ is the compatibility that makes the diagram commute.
>
> > [!note]- Full proof
> > By definition of a diagonal filler $r : B \to C$ for the square with left edge $f$, right edge $p$, top edge $i$, bottom edge $\mathrm{id}_B$: the upper triangle gives $r \circ f = i$, and the lower triangle gives $p \circ r = \mathrm{id}_B$.

> [!note]- Lemma 3: The assembled diagram is a retract diagram
> **Statement:** The diagram with rows $A \xrightarrow{\mathrm{id}} A \xrightarrow{\mathrm{id}} A$ and $B \xrightarrow{r} C \xrightarrow{p} B$ and verticals $f, i, f$ exhibits $f$ as a retract of $i$.
>
> **Hint:** Check all four squares commute and both horizontal composites are identities.
>
> **Why needed:** This is the conclusion — the literal definition of "retract" being satisfied.
>
> > [!note]- Full proof
> > The horizontal composites: top is $\mathrm{id}_A \circ \mathrm{id}_A = \mathrm{id}_A$; bottom is $p \circ r = \mathrm{id}_B$ (Lemma 2). The left square: going down then right, $r \circ f$; going right then down, $\mathrm{id}_A$ then $i$, i.e. $i$. By Lemma 2, $r \circ f = i$, so it commutes. The right square: going down then right, $p \circ i = f$; going right then down, $\mathrm{id} \circ f = f$ — wait, the right vertical is $f$ and the bottom-right map is $p$, top-right is $\mathrm{id}$; tracing $C \xrightarrow{p} B$ versus $C \xleftarrow{i} A \xrightarrow{f} B$ gives $p \circ i = f$. Both squares commute, and the horizontal composites are identities, so $f$ is a retract of $i$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : A \to B$ factor as $f = p \circ i$ with $i : A \to C$ and $p : C \to B$, and suppose $f$ has the left lifting property with respect to $p$.
>
> **Step 0 — the relevant square exists and commutes.** Consider the square
> $$\begin{array}{ccc} A & \xrightarrow{\ i\ } & C \\ \scriptstyle f \downarrow & & \downarrow \scriptstyle p \\ B & \xrightarrow{\ \mathrm{id}_B\ } & B \end{array}$$
> It commutes because $p \circ i = f = \mathrm{id}_B \circ f$.
>
> **Step 1 — produce the lift.** Since $f$ has the LLP with respect to $p$, there is a diagonal $r : B \to C$ with
> $$r \circ f = i \qquad \text{and} \qquad p \circ r = \mathrm{id}_B.$$
>
> **Step 2 — assemble the retract diagram.** Form
> $$\begin{array}{ccccc} A & \xrightarrow{\ \mathrm{id}_A\ } & A & \xrightarrow{\ \mathrm{id}_A\ } & A \\ \scriptstyle f \downarrow & & \downarrow \scriptstyle i & & \downarrow \scriptstyle f \\ B & \xrightarrow{\ r\ } & C & \xrightarrow{\ p\ } & B \end{array}$$
>
> **Step 3 — verify it is a retract diagram.** The top horizontal composite is $\mathrm{id}_A$. The bottom horizontal composite is $p \circ r = \mathrm{id}_B$ by Step 1. The left square commutes: $i \circ \mathrm{id}_A = i = r \circ f$ (Step 1). The right square commutes: $f \circ \mathrm{id}_A = f = p \circ i$ (the factorization). Hence the diagram displays $f$ as a retract of $i$.
>
> **Dual form.** Apply the above in $\mathcal{C}^{op}$: a factorization $f = p \circ i$ in $\mathcal{C}$ is a factorization in $\mathcal{C}^{op}$ with the roles of $i$ and $p$ swapped, the LLP becomes the RLP, and "retract of $i$" becomes "retract of $p$." Thus if $f$ has the RLP with respect to $i$, then $f$ is a retract of $p$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Idempotent splitting in any category.** In a category with split idempotents, the retract argument's bookkeeping is the same diagram chase that shows a retract of an object is the image of a split idempotent. Recognizing the retract diagram as "an idempotent $e = i \circ r$ on $C$ that splits through $A$" connects the model-categorical lemma to the elementary fact that retracts correspond to split idempotents — a useful translation when proving a class is closed under retracts.

**Projective modules and lifting.** In [[Def - Module|module]] theory, a module $P$ is projective iff $P \to 0$ has the RLP against surjections. The retract argument shows: if $P \to 0$ lifts against a surjection $p : C \twoheadrightarrow P$ from a free module (which always exists), then $P$ is a retract of the free module $C$ — recovering "projective = direct summand of free." This is the retract argument in the category of modules, with "free" playing the role of the good factor.

**Absolute retracts in topology.** A space $Y$ is an absolute retract iff every embedding $Y \hookrightarrow Z$ as a closed subspace has the extension (LLP) property. The retract argument translates this into "$Y$ is a retract of any nice space it embeds in," the topological prototype of the model-categorical statement, and the place where the word "retract" comes from.

---

# Bridges

- **[[Thm - Closure Properties of the Model Structure]]** — the immediate consumer. Every part of the closure theorem (lifting characterizations, closure under retracts, "any two classes determine the third") is proved by factoring a map and applying the retract argument to upgrade a lifting property into class membership. The retract argument is the engine; the closure theorem is what it powers.

- **[[Def - Model Category]]** — the lemma shows the axioms are overdetermined. MC4 (lifting) and MC5 (factorization) together imply more than they state, and the retract argument is the precise mechanism: it is why Hovey can take retract-closure as nearly the only axiom and *derive* the lifting characterizations.

- **The small object argument** — the structural partner. The small object argument *constructs* factorizations; the retract argument *interprets* them, showing any map with the right lifting property is a retract of the constructed (cell-complex) factor. Together they give the structural description "cofibrations = retracts of relative cell complexes."

- **Split idempotents and Karoubi envelopes** — the categorical home of "retract." A retract is a split idempotent, and the universal way to split idempotents is the Karoubi (idempotent-completion) envelope; the retract-closure of model-category classes is the statement that they are stable under this completion.

---

# Unlocked by This

> [!tip] The Lifting Characterization of the Three Classes *(from this chapter)*
> The retract argument is exactly what makes [[Thm - Closure Properties of the Model Structure]] true: cofibrations are the maps with LLP against trivial fibrations, fibrations the maps with RLP against trivial cofibrations, and so on. Each is proved by "factor, lift, retract."

> [!tip] Cofibrant Generation and Retracts of Cell Complexes *(from Homotopical Algebra)*
> Combined with the small object argument, the retract argument yields the structural theorem that every cofibration in a **cofibrantly generated** model category is a retract of a relative cell complex built from the generating cofibrations — the practical handle on what cofibrations look like.
