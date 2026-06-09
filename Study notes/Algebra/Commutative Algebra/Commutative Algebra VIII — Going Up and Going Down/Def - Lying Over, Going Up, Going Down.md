---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - The Induced Map on Spectra"
  - "Def - The Prime Spectrum (Spec)"
  - "Def - Prime and Maximal Ideal"
  - "Def - Integral Element and Integral Extension"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $f : A \to B$ be a ring homomorphism with [[Def - The Induced Map on Spectra|induced map]] $f^* : \operatorname{Spec} B \to \operatorname{Spec} A$, $\mathfrak{q} \mapsto f^{-1}(\mathfrak{q})$; in the inclusion case $A \subseteq B$ this is $\mathfrak{q} \mapsto \mathfrak{q} \cap A$. Primes of $A$ are $\mathfrak{p}, \mathfrak{p}_1, \mathfrak{p}_2$; primes of $B$ are $\mathfrak{q}, \mathfrak{q}_1, \mathfrak{q}_2$. We say "$\mathfrak{q}$ **lies over** $\mathfrak{p}$" for $f^*(\mathfrak{q}) = \mathfrak{p}$. The full registry is on [[Commutative Algebra VIII — Going Up and Going Down]].

This is a compound page: it defines three interlocking notions — **lying over** (surjectivity of $f^*$), **going up** (lifting an *ascending* inclusion of primes), and **going down** (lifting a *descending* inclusion) — because they are the three lifting properties of the single map $f^*$, are always stated and compared together, and only make sense as a family (each is the failure-or-success of $f^*$ to reflect one feature of the order on primes).

---

# Axiom Motivation

These three properties are not pulled from the air: they are the complete list of *natural lifting questions* one can ask about the map $f^* : \operatorname{Spec} B \to \operatorname{Spec} A$. The spectrum is not just a set — it is a *partially ordered set*, ordered by inclusion of primes, and geometrically by *specialisation* (a smaller prime is a "more generic" point, a larger prime a "more special" point in its closure). A map of spaces should be asked not only "is it onto?" but "does it respect the order — can I lift comparisons of points?" The three definitions are the three answers.

**Why surjectivity deserves its own name (lying over).** The first and crudest question about any map is whether it is onto. For $f^*$, "$\mathfrak{p}$ is in the image" means "some prime $\mathfrak{q}$ of $B$ contracts to $\mathfrak{p}$" — some prime *lies over* $\mathfrak{p}$. So surjectivity of $f^*$ is exactly: *every* prime of $A$ has a prime of $B$ lying over it, no point of the base is missed. This earns a name because it is the property most likely to *fail* for a general ring map — the localization $\mathbb{Z} \to \mathbb{Q}$ misses every $(p)$ — and because it is the *base case* of the other two: to lift a chain you must first lay a prime over its bottom. The name "lying over" is the geometer's: a prime of $B$ "lies over" the point of $A$ beneath it, the way a sheet of a covering lies over the base.

**Why two directions of chain-lifting, and why they are genuinely different.** Once $f^*$ is onto, the next question is whether it respects the *order*. Suppose I know $\mathfrak{q}_1$ lies over $\mathfrak{p}_1$, and I am handed a *neighbouring* prime $\mathfrak{p}_2$ of $A$ comparable to $\mathfrak{p}_1$. Can I find a neighbour $\mathfrak{q}_2$ of $\mathfrak{q}_1$ lying over $\mathfrak{p}_2$, on the same side? There are exactly two cases, because $\mathfrak{p}_2$ is either larger or smaller than $\mathfrak{p}_1$. If $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ (enlarge), the lift $\mathfrak{q}_2$ should satisfy $\mathfrak{q}_1 \subseteq \mathfrak{q}_2$ — this is **going up**. If $\mathfrak{p}_1 \supseteq \mathfrak{p}_2$ (shrink), the lift should satisfy $\mathfrak{q}_1 \supseteq \mathfrak{q}_2$ — this is **going down**. The reason both deserve separate definitions, rather than one "order-respecting" property, is the central surprise of the chapter: *they are not equivalent*. For an integral extension, going up holds always, but going down requires the base $A$ to be normal and *fails* otherwise. So a finite map can lift comparisons upward but not downward — and the asymmetry is real, not a defect of the definitions. Had we lumped them together, this phenomenon — the heart of the going-down theorem — would be invisible.

**Why the lift must keep the same containment, not merely contract correctly.** A weaker definition would ask only for *some* $\mathfrak{q}_2$ over $\mathfrak{p}_2$, ignoring its relation to $\mathfrak{q}_1$. But that weaker statement is just lying over applied to $\mathfrak{p}_2$ and carries no information about chains. The whole point of going up and going down is to build *chains*: $\mathfrak{q}_1 \subseteq \mathfrak{q}_2$ (or $\supseteq$) is what lets you iterate, lifting a whole chain $\mathfrak{p}_0 \subseteq \cdots \subseteq \mathfrak{p}_n$ link by link to a chain $\mathfrak{q}_0 \subseteq \cdots \subseteq \mathfrak{q}_n$ of the same length. Drop the containment requirement and you cannot lift a chain, only its individual points — and the dimension theorem dies. The containment is not decoration; it is the entire force of the definition.

**Why these are properties of $f$, and why one implies another.** Each property is a property of the *map* $f$ (equivalently of the extension $A \subseteq B$), assertable for any ring homomorphism, true or false. The logical relations among them are part of the motivation. Going up *implies* lying over: given any $\mathfrak{p}$, the localization argument produces *some* prime $\mathfrak{q}_0$ with $\mathfrak{q}_0 \cap A \subseteq \mathfrak{p}$ (a prime "below" $\mathfrak{p}$ in the image), and then going up, applied to $\mathfrak{q}_0 \cap A \subseteq \mathfrak{p}$, pushes it up to a prime over $\mathfrak{p}$ — so the image contains $\mathfrak{p}$, and $f^*$ is onto. (This is why one rarely states lying over separately for maps known to go up.) Going down does *not* imply lying over by the same token — it lifts comparisons but provides no anchor — which is one more reason to keep all three distinct. Quotient maps satisfy all three trivially (the fibres are at most points, and the order is reflected exactly on $V(I)$); integral maps satisfy lying over and going up always; and the conditional case — going down — is what the chapter exists to pin down.

---

# The Definition

Let $f : A \to B$ be a homomorphism of commutative rings, with [[Def - The Induced Map on Spectra|induced map]] $f^* : \operatorname{Spec} B \to \operatorname{Spec} A$, $f^*(\mathfrak{q}) = f^{-1}(\mathfrak{q})$.

## Lying over

$f$ **satisfies lying over** if $f^*$ is surjective: for every $\mathfrak{p} \in \operatorname{Spec} A$ there is $\mathfrak{q} \in \operatorname{Spec} B$ with $f^{-1}(\mathfrak{q}) = \mathfrak{p}$. (Equivalently, every fibre of $f^*$ is non-empty.)

## Going up

$f$ **satisfies going up** if: for all $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ in $\operatorname{Spec} A$ and every $\mathfrak{q}_1 \in \operatorname{Spec} B$ with $f^{-1}(\mathfrak{q}_1) = \mathfrak{p}_1$, there exists $\mathfrak{q}_2 \in \operatorname{Spec} B$ with
$$\mathfrak{q}_1 \subseteq \mathfrak{q}_2 \qquad \text{and} \qquad f^{-1}(\mathfrak{q}_2) = \mathfrak{p}_2.$$

## Going down

$f$ **satisfies going down** if: for all $\mathfrak{p}_1 \supseteq \mathfrak{p}_2$ in $\operatorname{Spec} A$ and every $\mathfrak{q}_1 \in \operatorname{Spec} B$ with $f^{-1}(\mathfrak{q}_1) = \mathfrak{p}_1$, there exists $\mathfrak{q}_2 \in \operatorname{Spec} B$ with
$$\mathfrak{q}_1 \supseteq \mathfrak{q}_2 \qquad \text{and} \qquad f^{-1}(\mathfrak{q}_2) = \mathfrak{p}_2.$$

In the inclusion case $A \subseteq B$, replace $f^{-1}(\mathfrak{q})$ by $\mathfrak{q} \cap A$ throughout.

**Basic implications.** Going up implies lying over. A quotient map $A \to A/I$ and a localization $A \to S^{-1}A$ each satisfy all three. An [[Def - Integral Element and Integral Extension|integral extension]] satisfies lying over and going up always (see [[Thm - Lying Over]], [[Thm - Going Up]]); it satisfies going down when $A$ is an [[Def - Integral Closure and Normal Domain|integrally closed domain]] (see [[Thm - Going Down for Integrally Closed Domains]]), and may fail going down otherwise. A *flat* ring map satisfies going down with no further hypotheses.

---

# Relate to Other Fields / Compression

The cleanest compression: **these are the three things you can ask of a map of ordered spaces — is it onto, and does it lift comparisons up and down.** Lying over is surjectivity; going up and going down are the two directions of "respects the specialisation order".

**True name:** the true name of the package is *the lifting properties of a finite map*: **lying over $=$ surjective, going up $=$ closed (lifts specialisation), going down $=$ lifts generisation (equidimensional).** In specialisation language, going up says you can follow a *specialisation* of the base point by specialising a chosen preimage; going down says you can follow a *generisation* of the base point by generising a chosen preimage. A geometer reaching for "this finite map is surjective and closed" is reaching for lying over and going up.

These properties are the order-theoretic content of a map between posets, made into ring theory. In topology, a *closed map* sends closed sets to closed sets, and a finite morphism's induced $f^*$ is closed *exactly when $f$ satisfies going up* — the algebraic criterion for a geometric topological property. In the theory of fibrations and covering spaces, lying over is the surjectivity of a covering, and incomparability (its companion in the chapter) is the discreteness of the fibres; going up and going down are the path-lifting properties that let one transport along the base.

---

# Examples / Corollaries

**Is an instance (all three) — a quotient map $\pi : A \to A/I$.** The induced map $\pi^*$ is the inclusion of $V(I)$ into $\operatorname{Spec} A$, an order-isomorphism onto the primes containing $I$. Lying over holds among those primes; and a comparison $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ with both $\supseteq I$ lifts trivially to itself, in either direction. So quotient maps go up and down, costing nothing.

**Is an instance (lying over and going up, always) — any integral extension $\mathbb{Z} \subseteq \mathbb{Z}[i]$.** Every $(p)$ has a Gaussian prime over it (lying over), and an inclusion $(0) \subseteq (p)$ of rational primes lifts to $(0) \subseteq \mathfrak{q}$ with $\mathfrak{q}$ over $(p)$ (going up). Both hold with no further hypothesis, because $\mathbb{Z}[i]$ is integral over $\mathbb{Z}$. (Here $\mathbb{Z}$ *is* normal, so going down holds too.)

**Is NOT an instance of lying over — the localization $\mathbb{Z} \hookrightarrow \mathbb{Q}$.** $\operatorname{Spec}\mathbb{Q} = \{(0)\}$, so the image of $(\mathbb{Z} \to \mathbb{Q})^*$ is $\{(0)\}$, missing every $(p)$. Lying over fails — the map is far from onto. This is the standard reminder that surjectivity is *not* automatic; integrality (which $\mathbb{Z} \to \mathbb{Q}$ lacks) is what supplies it.

**Is NOT an instance of going down — an integral extension with non-normal base.** Take $B = k[u] \times k[v]$ and $A = \{(f,g) \in B : f(0) = g(0)\}$, the non-normal "two lines glued at a point". $A \subseteq B$ is integral, so it goes *up*, but it does *not* go down: there is a chain $\mathfrak{p}_2 \subsetneq \mathfrak{p}_1$ in $A$ and a $\mathfrak{q}_1$ over $\mathfrak{p}_1$ admitting no $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ over $\mathfrak{p}_2$ (see [[Ex - Going down can fail without normality]]). This is the separating example showing going down is strictly stronger than going up for integral maps.

**Corollary — going up lets you lift a whole ascending chain.** Iterating going up from a prime $\mathfrak{q}_0$ over $\mathfrak{p}_0$, an ascending chain $\mathfrak{p}_0 \subseteq \mathfrak{p}_1 \subseteq \cdots \subseteq \mathfrak{p}_n$ lifts to $\mathfrak{q}_0 \subseteq \mathfrak{q}_1 \subseteq \cdots \subseteq \mathfrak{q}_n$ with $\mathfrak{q}_i$ over $\mathfrak{p}_i$. (Strictness of the lift, when the base chain is strict, is supplied by [[Thm - Incomparability|incomparability]].) This is the calibration check that going up is a *chain*-lifting property, not merely a point-lifting one.

**Calibration check.** Verify that going up implies lying over by the localization-then-push-up argument. Confirm that the quotient map $\mathbb{Z} \to \mathbb{Z}/6$ satisfies all three (its $\pi^*$ identifies $\operatorname{Spec}\mathbb{Z}/6$ with $\{(2),(3)\} \subseteq \operatorname{Spec}\mathbb{Z}$). Finally, state from memory which of the three properties an integral extension satisfies unconditionally (lying over, going up) and which needs a hypothesis (going down, needs $A$ normal).

---

# Unlocked by This

> [!tip] Surjective, closed, and finite-fibred morphisms *(from Algebraic Geometry)*
> For a **finite morphism of varieties** $\pi : \operatorname{Spec} B \to \operatorname{Spec} A$, lying over is "$\pi$ is surjective", going up is "$\pi$ is closed", and (with incomparability) the fibres are finite. Going down for a normal base is "$\pi$ does not jump fibre dimension" — the equidimensionality that makes a family of varieties **flat** in good cases. These three properties are the local model for the global theory of **proper** and **finite** morphisms of **schemes**.

> [!tip] Flat maps go down — flat families *(from Commutative Algebra / Algebraic Geometry)*
> A *flat* ring homomorphism satisfies going down with **no** hypothesis on the rings — flatness is the other classical sufficient condition, orthogonal to normality. Geometrically a **flat family** of varieties has fibres that vary "continuously" without dimension jumps, and going down is the order-theoretic shadow of that continuity. This is why flatness, not just normality, recurs as the hypothesis guaranteeing well-behaved fibres in the theory of moduli and deformations.
