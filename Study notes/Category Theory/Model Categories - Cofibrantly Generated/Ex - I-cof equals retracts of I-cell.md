---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Small Object Argument"
  - "Thm - The Retract Argument"
  - "Def - Relative Cell Complex"
  - "Def - Lifting Property and the Retract Argument"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be cocomplete and $I$ a set of maps whose domains are small relative to $I\text{-cell}$. Prove the structural identity
$$I\text{-cof} \;=\; \{\,\text{retracts of relative } I\text{-cell complexes}\,\},$$
that is, a map is an $I$-cofibration if and only if it is a retract of a relative $I$-cell complex. Prove both inclusions, naming exactly where the [[Thm - The Small Object Argument|small object argument]] and the [[Thm - The Retract Argument|retract argument]] are used. Deduce as a corollary that a map with the LLP against all $I$-injectives, which also lies in $I\text{-cell}$ up to retract, is detected purely by lifting.

**Recall:**

![[Def - Relative Cell Complex#The Definition]]

![[Thm - The Retract Argument#Statement]]

$I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ is the class of maps with the left lifting property against every $I$-injective; $I\text{-cell}$ is the relative cell complexes. The [[Thm - The Small Object Argument|small object argument]] factors any map as $(I\text{-cell})\circ(I\text{-inj})$ when the domains of $I$ are small.

---

# Convergent Strategy

**Problem class:** This is a closure-identity problem — the second recurring target of the chapter — identifying an abstractly-defined class ($I\text{-cof}$, by lifting) with a constructively-defined one (retracts of $I\text{-cell}$). It is the structural payoff that justifies cofibrant generation.

**Assumption pattern:** The two assumptions are smallness of the domains of $I$ (so the small object argument runs and factorizations exist) and the saturation of $I\text{-cof}$ (it is an $\mathrm{LLP}$-class, hence closed under retract and the cell operations). The "$\supseteq$" direction uses only saturation; the "$\subseteq$" direction is where the factorization plus retract argument do real work.

**Theorem routing:** The route for $\supseteq$ is: cell complexes lie in $I\text{-cof}$ (saturation), and $I\text{-cof}$ is retract-closed, so retracts of cell complexes are in $I\text{-cof}$. The route for $\subseteq$ is: factor $f\in I\text{-cof}$ via the small object argument as $p\circ i$ with $i\in I\text{-cell}$, $p\in I\text{-inj}$; since $f$ lifts against $p$, the retract argument exhibits $f$ as a retract of $i$.

**Key decision point:** The non-obvious move is the self-referential lift in the $\subseteq$ direction: $f$ lifts against its *own* injective factor $p$ because $f\in I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ and $p\in I\text{-inj}$. Setting up the square with $i$ on top and $p$ on the right, with $f$ on the left and $\mathrm{id}$ on the bottom, and recognizing the diagonal lift as the retraction data, is the crux.

---

# Legal Operations Used

1. **Operation 3 from the topic page (run the small object argument to factor a map).** The $\subseteq$ direction begins by factoring $f$ as $(I\text{-cell})\circ(I\text{-inj})$.

2. **Operation 4 from the topic page (use the retract argument to upgrade a lifting property to class membership).** The factorization plus the self-lift of $f$ against $p$ exhibits $f$ as a retract of the cell-complex factor.

3. **Operation 6 from the topic page (close $I\text{-cof}$ under structural operations).** The $\supseteq$ direction uses that $I\text{-cof}$ contains $I\text{-cell}$ and is retract-closed.

---

# Hints

> [!note]- Hint 1 ($\supseteq$)
> Every relative cell complex is in $I\text{-cof}$: pushouts, coproducts, and transfinite composites of maps lifting against $I\text{-inj}$ still lift (this is the saturation of $\mathrm{LLP}(I\text{-inj})$). And $I\text{-cof}$ is closed under retract (any $\mathrm{LLP}$-class is). So retracts of cell complexes are in $I\text{-cof}$.

> [!note]- Hint 2 ($\subseteq$, setup)
> Take $f : X\to Y$ in $I\text{-cof}$. By the small object argument, factor $f = p\, i$ with $i : X\to Z$ in $I\text{-cell}$ and $p : Z\to Y$ in $I\text{-inj}$.

> [!note]- Hint 3 ($\subseteq$, the lift)
> Consider the square with $i$ across the top ($X\to Z$), $p$ down the right ($Z\to Y$), $f$ down the left ($X\to Y$), and $\mathrm{id}_Y$ across the bottom. It commutes ($p i = f = \mathrm{id}_Y\circ f$). Since $f\in I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ and $p\in I\text{-inj}$, there is a diagonal $r : Y\to Z$ with $r f = i$ and $p r = \mathrm{id}_Y$.

> [!note]- Hint 4 ($\subseteq$, conclude)
> The data $(\mathrm{id}_X, r)$ on the source-target and $(\mathrm{id}_X, p)$... — more precisely, the maps exhibit $f$ as a retract of $i$ in the arrow category: $X\xrightarrow{\mathrm{id}} X\xrightarrow{\mathrm{id}} X$ on top and $Y\xrightarrow{r} Z\xrightarrow{p} Y$ on the bottom, with the squares commuting and horizontal composites identities. By the [[Thm - The Retract Argument|retract argument]], $f$ is a retract of $i\in I\text{-cell}$.

---

# Solution

The proof is two inclusions. $\supseteq$ is pure saturation: cell complexes are in $I\text{-cof}$ and $I\text{-cof}$ is retract-closed (Step 1). $\subseteq$ factors $f$ by the small object argument, lifts $f$ against its own injective factor, and applies the retract argument (Steps 2–3). The crux is the self-lift in Step 3.

**Step 1 ($\supseteq$): Retracts of cell complexes are $I$-cofibrations.**

> [!note]- Derivation
> First, $I\text{-cell}\subseteq I\text{-cof}$. The class $I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ is *saturated*: it contains isomorphisms and is closed under pushout, coproduct, and transfinite composition, because the LLP against a fixed map (hence against the class $I\text{-inj}$) is preserved by these colimit operations. A relative cell complex is a transfinite composite of pushouts of coproducts of maps of $I$; since $I\subseteq\mathrm{LLP}(I\text{-inj}) = I\text{-cof}$ (each generator lifts against everything that lifts against it), all these building maps are in $I\text{-cof}$, and saturation gives $I\text{-cell}\subseteq I\text{-cof}$.
>
> Second, $I\text{-cof}$ is closed under retracts (any $\mathrm{LLP}$-class is: a retract of a map with a lifting property has it). Hence retracts of relative cell complexes lie in $I\text{-cof}$. This proves $\{\text{retracts of } I\text{-cell}\}\subseteq I\text{-cof}$.

**Step 2 ($\subseteq$): Factor $f$ via the small object argument.**

> [!note]- Derivation
> Let $f : X\to Y$ be in $I\text{-cof}$. Because the domains of $I$ are small relative to $I\text{-cell}$, the [[Thm - The Small Object Argument|small object argument]] produces a factorization
> $$X\xrightarrow{\ i\ } Z\xrightarrow{\ p\ } Y, \qquad i\in I\text{-cell},\quad p\in I\text{-inj},\quad p\, i = f.$$

**Step 3 ($\subseteq$): $f$ lifts against $p$, and the retract argument finishes.**

> [!note]- Derivation
> Consider the commuting square
> $$\begin{array}{ccc} X & \xrightarrow{\ i\ } & Z \\ {\scriptstyle f}\downarrow & & \downarrow{\scriptstyle p} \\ Y & \xrightarrow{\ \mathrm{id}\ } & Y \end{array} \qquad (p\, i = f = \mathrm{id}_Y\circ f).$$
> Since $f\in I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ and $p\in I\text{-inj}$, the square admits a diagonal lift $r : Y\to Z$ with
> $$r\, f = i \qquad\text{and}\qquad p\, r = \mathrm{id}_Y.$$
> Now read off a retract diagram exhibiting $f$ as a retract of $i$ in the arrow category $\mathcal{C}^{\to}$:
> $$\begin{array}{ccccc}
> X & \xrightarrow{\ \mathrm{id}\ } & X & \xrightarrow{\ \mathrm{id}\ } & X \\
> {\scriptstyle f}\downarrow & & {\scriptstyle i}\downarrow & & \downarrow{\scriptstyle f} \\
> Y & \xrightarrow{\ r\ } & Z & \xrightarrow{\ p\ } & Y
> \end{array}$$
> The left square commutes because $r f = i\circ\mathrm{id}$ (i.e. $rf = i$); the right square because $p i = f$ and $\mathrm{id}\circ f = f\circ\mathrm{id}$ — explicitly $f\circ\mathrm{id} = f = p\circ i$. The top horizontal composite is $\mathrm{id}_X$; the bottom horizontal composite is $p\, r = \mathrm{id}_Y$. So $f$ is a retract of $i$. By the [[Thm - The Retract Argument|retract argument]] (here used directly as the definition of retract), $f$ is a retract of the relative cell complex $i\in I\text{-cell}$. This proves $I\text{-cof}\subseteq\{\text{retracts of } I\text{-cell}\}$.
>
> Combining Steps 1 and 3, $I\text{-cof} = \{\text{retracts of relative } I\text{-cell complexes}\}$.

**Corollary: lifting detects $I$-cofibrations.**

> [!note]- Derivation
> The identity shows the abstract class $I\text{-cof}$ (defined by the lifting property $\mathrm{LLP}(I\text{-inj})$) coincides with the constructive class (retracts of things built from $I$). In particular, to test whether $f$ is an $I$-cofibration it suffices to check lifting against all $I$-injectives — and by the small object argument it is enough to check against the factorization's $p$, which is built from the set $I$. So membership in $I\text{-cof}$ is a lifting condition against the *set* $I$ (via its injectives), not against a proper class.

> [!note]- Complete formal solution
> Let $f\in I\text{-cof}$. ($\supseteq$) $I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ is saturated and contains $I$, so it contains $I\text{-cell}$ (transfinite composites of pushouts of coproducts of $I$); it is also retract-closed, so retracts of $I\text{-cell}$ lie in $I\text{-cof}$. ($\subseteq$) By smallness of the domains of $I$, the small object argument factors $f = p\, i$, $i\in I\text{-cell}$, $p\in I\text{-inj}$. The square $(i \text{ top}, p \text{ right}, f \text{ left}, \mathrm{id}_Y \text{ bottom})$ commutes and, as $f\in\mathrm{LLP}(I\text{-inj})$ and $p\in I\text{-inj}$, has a diagonal $r$ with $rf = i$, $pr = \mathrm{id}_Y$. The diagram with identities on top and $(r, p)$ on the bottom exhibits $f$ as a retract of $i$; the [[Thm - The Retract Argument|retract argument]] concludes $f$ is a retract of the cell complex $i$. Hence $I\text{-cof} = \{\text{retracts of } I\text{-cell}\}$, and membership is a lifting condition against the set $I$. $\blacksquare$

---

# Key Takeaways

**Generated-by means built-from-up-to-retract, and the retract is not optional.** The identity $I\text{-cof} =$ retracts of $I\text{-cell}$ is the precise content of "the cofibrations are generated by $I$": they are the retracts of the maps you can literally build from $I$ by gluing. The retract-closure is genuinely necessary — an identity map or a section of a cell complex is a cofibration that need not be a cell complex — and the small object argument is exactly what proves the closure is *exactly* retracts, no more and no less. This build-then-retract shape recurs throughout algebra (subgroup, ideal, saturation generated by a set), and recognizing the model-categorical instance lets you switch fluidly between the constructive description (induct over cells) and the lifting description (test against injectives).

**The self-lift against the injective factor is the signature move of the retract argument.** The crux of the $\subseteq$ direction is that $f$ lifts against its *own* small-object-argument factor $p$, precisely because $f$ is in the LLP-class and $p$ is in the matching RLP-class. This self-referential lift, turning a factorization into a retraction, is the universal mechanism by which "$f$ has the right lifting property" is upgraded to "$f$ belongs to the class." It appears again in the recognition theorem (to show trivial cofibrations are $J$-cofibrations) and in the closure theorem of the previous chapter. The trigger to reach for it: you have a map in an LLP-class, you factor it, and you want to conclude it is a retract of the left factor.

**An abstractly-defined class becomes computable once it is shown to be a retract-closure of a generated class.** Before this identity, "$I$-cofibration" is an opaque condition quantifying over all $I$-injectives — a proper class. After it, an $I$-cofibration is a concrete object (retract of a cell complex) and, dually, membership is testable by lifting against the *set* $I$ alone. This is the conversion that makes cofibrant generation useful: it replaces proper-class quantification with set-indexed verification and constructive description. The general lesson — that identifying a lifting class with a generated-and-retract-closed class makes it both buildable and checkable — is the structural heart of why the whole apparatus of generators exists.
