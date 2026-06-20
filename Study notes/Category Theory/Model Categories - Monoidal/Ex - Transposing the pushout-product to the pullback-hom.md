---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor"
  - "Def - Closed Monoidal Category"
  - "Def - Pullback and Pushout"
  - "Def - Monoidal Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a [[Def - Closed Monoidal Category|closed monoidal category]] with internal hom $[-,-]$. For maps $i : U \to V$, $j : X \to Y$, $p : Z \to W$, prove the **lifting adjunction**: there is a natural bijection between
- commuting squares from the pushout-product $i \mathbin{\square} j$ to $p$ (together with their diagonal fillers), and
- commuting squares from $i$ to the pullback-hom $\langle j, p\rangle : [Y, Z] \to [X, Z] \times_{[X, W]} [Y, W]$ (together with their diagonal fillers).

Deduce that, in a model category, "$i \mathbin{\square} j$ is a cofibration for all cofibrations $i, j$" is equivalent to "$\langle j, p\rangle$ is a fibration whenever $j$ is a cofibration and $p$ a fibration, trivial if either is" — i.e. the two forms of the [[Def - Monoidal Model Category|pushout-product axiom]] coincide.

**Recall:**

In a [[Def - Closed Monoidal Category|closed monoidal category]], $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$ naturally.

The **pushout-product** $i \mathbin{\square} j : (V \otimes X) \cup_{U \otimes X}(U \otimes Y) \to V \otimes Y$ is the map out of a [[Def - Pullback and Pushout|pushout]]; the **pullback-hom** $\langle j, p\rangle : [Y, Z] \to [X, Z] \times_{[X, W]} [Y, W]$ is the map into a [[Def - Pullback and Pushout|pullback]].

A map $\alpha$ has the **left lifting property** against $\beta$ ($\alpha \perp \beta$) if every commuting square with $\alpha$ left, $\beta$ right has a diagonal filler. In a model category: cofibration $\iff$ LLP against all trivial fibrations; fibration $\iff$ RLP against all trivial cofibrations.

---

# Convergent Strategy

**Problem class:** This is a *prove-an-adjunction-of-lifting-problems* problem — the most structural exercise of the chapter, establishing the equivalence at the heart of [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the Quillen-bifunctor theorem]]. It is "closedness lets you check either side", proved at the level of squares.

**Assumption pattern:** The single assumption is the tensor-hom adjunction, applied not to objects but to the *four corners of a commuting square*. The pushout (a colimit, "maps out") and the pullback (a limit, "maps in") are the dual universal properties whose transposes match. Recognizing that a lifting problem is a square, and that the adjunction acts on the whole square, is the entire idea.

**Theorem routing:** The route is: decompose a square from $i \mathbin{\square} j$ to $p$ into compatible data using the pushout's universal property; transpose each piece across $- \otimes (\text{var}) \dashv [(\text{var}), -]$; reassemble into a square from $i$ to $\langle j, p\rangle$ using the pullback's universal property; check fillers correspond. Then feed this bijection into the lifting-property characterizations of the model-category classes to get the equivalence of the two axiom forms.

**Key decision point:** The crux is to transpose *the corner objects correctly*: the pushout $(V \otimes X) \cup_{U \otimes X}(U \otimes Y)$ must transpose to the pullback $[X, Z] \times_{[X, W]}[Y, W]$. This is where most attempts fail — transposing $i \otimes 1$ and $1 \otimes j$ separately loses the gluing. The decision is to use the *universal properties* of pushout and pullback (maps out of / into them are compatible tuples) and let the adjunction convert "compatible tuple out of a pushout" into "compatible tuple into a pullback".

---

# Legal Operations Used

1. **Operation 2 (transpose a pushout-product condition into a pullback-hom condition), topic page.** This exercise proves that the transposition is valid at the level of lifting problems, justifying the operation.

2. **Operation (lifting-property characterization of the classes), model-category background.** We convert the model-categorical statements ("cofibration", "trivial fibration") into pure lifting statements before applying the adjunction, then convert back.

---

# Hints

> [!note]- Hint 1
> A lifting problem is a commuting square plus the question of a diagonal. Phrase both sides — $i \mathbin{\square} j$ against $p$, and $i$ against $\langle j, p\rangle$ — as squares, and aim to biject the squares *and* their fillers.

> [!note]- Hint 2
> A map *out of* the pushout $(V \otimes X) \cup_{U \otimes X}(U \otimes Y)$ is a compatible *pair* of maps out of $V \otimes X$ and $U \otimes Y$ agreeing on $U \otimes X$. Use this to break the square from $i \mathbin{\square} j$ into two pieces.

> [!note]- Hint 3
> Transpose each piece across the tensor-hom adjunction. A map $V \otimes X \to Z$ becomes $V \to [X, Z]$; a map $U \otimes Y \to Z$ becomes $U \to [Y, Z]$; the target map $V \otimes Y \to W$ becomes $V \to [Y, W]$.

> [!note]- Hint 4
> A map *into* the pullback $[X, Z] \times_{[X, W]}[Y, W]$ is a compatible pair of maps into $[X, Z]$ and $[Y, W]$. Check the transposed pieces assemble into exactly such a pair, producing a square from $i$ to $\langle j, p\rangle$. Then a filler $V \to [Y, Z]$ transposes back to a filler $V \otimes Y \to Z$.

> [!note]- Hint 5
> For the equivalence of axioms: "$i \mathbin{\square} j$ is a cofibration" $=$ "$i \mathbin{\square} j \perp$ every trivial fibration $p$"; transpose to "$i \perp \langle j, p\rangle$ for all trivial fibrations $p$ and all cofibrations $i$", which says $\langle j, p\rangle$ is a trivial fibration.

---

# Solution

The route is: (1) phrase both sides as squares-with-fillers; (2) use the pushout's universal property to split the left square into two compatible transposable pieces; (3) transpose via the tensor-hom adjunction; (4) use the pullback's universal property to reassemble into the right square, matching fillers; (5) feed the bijection into the lifting characterizations to equate the two axiom forms.

**Step 1: A square from $i \mathbin{\square} j$ to $p$ is a compatible pair of squares.**

> [!note]- Derivation
> A commuting square from $i \mathbin{\square} j$ to $p$ is a pair of maps $a : (V \otimes X) \cup_{U \otimes X}(U \otimes Y) \to Z$ and $b : V \otimes Y \to W$ with $p \circ a = b \circ (i \mathbin{\square} j)$. By the universal property of the [[Def - Pullback and Pushout|pushout]], $a$ is the same as a compatible pair $a_1 : V \otimes X \to Z$ and $a_2 : U \otimes Y \to Z$ agreeing after restriction to $U \otimes X$ (i.e. $a_1 \circ (1 \otimes j)|_{U \otimes X} = a_2 \circ (i \otimes 1)|_{U \otimes X}$). The relation $p \circ a = b \circ (i \mathbin{\square} j)$ becomes two relations tying $a_1, a_2$ to $b$ via $p$.

**Step 2: Transpose across the tensor-hom adjunction.**

> [!note]- Derivation
> Apply $- \otimes Y \dashv [Y, -]$ and $- \otimes X \dashv [X, -]$ to each map:
> $$a_1 : V \otimes X \to Z \ \rightsquigarrow\ \widehat{a_1} : V \to [X, Z]; \quad a_2 : U \otimes Y \to Z \ \rightsquigarrow\ \widehat{a_2} : U \to [Y, Z]; \quad b : V \otimes Y \to W \ \rightsquigarrow\ \widehat b : V \to [Y, W].$$
> The compatibility of $a_1, a_2$ on $U \otimes X$ transposes to the statement that $\widehat{a_1}$ and $\widehat{a_2}$ agree in $[X, Z]$ after composing with the structure maps to $[X, W]$ — precisely the condition for $(\widehat{a_1}, \widehat b)$ to define a map $V \to [X, Z] \times_{[X, W]} [Y, W]$ into the pullback (using naturality of the adjunction across $p$ and $j$).

**Step 3: Reassemble into a square from $i$ to $\langle j, p\rangle$.**

> [!note]- Derivation
> By the universal property of the [[Def - Pullback and Pushout|pullback]], the compatible pair $(\widehat{a_1}, \widehat b)$ is a single map $c : V \to [X, Z] \times_{[X, W]} [Y, W]$. Together with $\widehat{a_2} : U \to [Y, Z]$, and using $i : U \to V$, the data form a commuting square
> $$\begin{array}{ccc} U & \xrightarrow{\ \widehat{a_2}\ } & [Y, Z] \\ {\scriptstyle i}\big\downarrow & & \big\downarrow{\scriptstyle \langle j, p\rangle} \\ V & \xrightarrow{\ c\ } & [X, Z] \times_{[X, W]} [Y, W] \end{array}$$
> The square commutes precisely because of the transposed relations from Step 1–2. This assignment (square on the left $\leftrightarrow$ square on the right) is a bijection, since every transpose is invertible.

**Step 4: Fillers correspond.**

> [!note]- Derivation
> A diagonal filler for the right square is a map $h : V \to [Y, Z]$ with $h \circ i = \widehat{a_2}$ and $\langle j, p\rangle \circ h = c$. Transposing across $- \otimes Y \dashv [Y, -]$, $h$ corresponds to $\widetilde h : V \otimes Y \to Z$, and the two filler equations transpose exactly to the two equations a diagonal filler $V \otimes Y \to Z$ of the left square must satisfy (it restricts correctly on the pushout and composes with $p$ to $b$). The correspondence $h \leftrightarrow \widetilde h$ is a bijection. Hence: the left square has a filler iff the right square does, i.e. $i \mathbin{\square} j \perp p \iff i \perp \langle j, p\rangle$.

**Step 5: Equivalence of the two axiom forms.**

> [!note]- Derivation
> Recall cofibration $=$ LLP against all trivial fibrations, trivial fibration $=$ RLP against all cofibrations (dually for the trivial-cofibration/fibration pair). Fix cofibrations $i, j$ and a trivial fibration $p$. "$i \mathbin{\square} j$ is a cofibration" means $i \mathbin{\square} j \perp p$ for *every* trivial fibration $p$. By Step 4 this is $i \perp \langle j, p\rangle$ for every trivial fibration $p$ and every cofibration $i$ — which, quantifying over all cofibrations $i$, says $\langle j, p\rangle$ has the RLP against all cofibrations, i.e. $\langle j, p\rangle$ is a *trivial fibration* whenever $p$ is. This is the trivial half of the pullback-hom form. Repeating with $p$ a general fibration and tracking which of $i, j, p$ is trivial gives the remaining clauses, establishing the equivalence of the two forms of the [[Def - Monoidal Model Category|pushout-product axiom]].

> [!note]- Complete formal solution
> A commuting square from $i \mathbin{\square} j$ to $p$ consists of $a : (V \otimes X)\cup_{U \otimes X}(U \otimes Y) \to Z$ and $b : V \otimes Y \to W$ with $p a = b(i \mathbin{\square} j)$. By the [[Def - Pullback and Pushout|pushout]] universal property, $a = (a_1, a_2)$ compatible on $U \otimes X$. Transposing via $- \otimes X \dashv [X, -]$ and $- \otimes Y \dashv [Y, -]$ gives $\widehat{a_1} : V \to [X, Z]$, $\widehat{a_2} : U \to [Y, Z]$, $\widehat b : V \to [Y, W]$, with the compatibility transposing to "$(\widehat{a_1}, \widehat b)$ factors through the [[Def - Pullback and Pushout|pullback]] $[X, Z] \times_{[X, W]}[Y, W]$", yielding $c : V \to [X, Z]\times_{[X,W]}[Y,W]$. The pair $(\widehat{a_2}, c)$ with $i$ and $\langle j, p\rangle$ is a commuting square, and the correspondence is bijective. A filler $h : V \to [Y, Z]$ of the right square transposes to a filler $\widetilde h : V \otimes Y \to Z$ of the left square and back, so $i \mathbin{\square} j \perp p \iff i \perp \langle j, p\rangle$. Feeding this into the lifting-property characterizations (cofibration $=$ LLP vs trivial fibrations; trivial fibration $=$ RLP vs cofibrations) shows "$i \mathbin{\square} j$ is a (trivial) cofibration for cofibrations $i, j$" is equivalent to "$\langle j, p\rangle$ is a (trivial) fibration for $j$ a cofibration and $p$ a fibration", which is the asserted equivalence of the two forms of the pushout-product axiom. $\qquad\blacksquare$

---

# Key Takeaways

**The pushout-product and the pullback-hom are one adjunction transpose applied to a square — this is why closed monoidal model categories let you check either side.** The deep content is that a *lifting problem* (a square plus a filler) is a categorical object that the tensor-hom adjunction transforms wholesale: pushout corners become pullback corners, "maps out" become "maps in", and fillers correspond. The transferable insight is that adjunctions act not just on hom-sets of objects but on diagrams and lifting problems, and the dual universal properties of colimits and limits are exactly what make the corners match. Whenever you have an adjunction and a lifting problem phrased with one functor, transpose the whole square to phrase it with the adjoint — the answer to "does a lift exist?" is preserved.

**Always phrase model-categorical conditions as lifting problems before manipulating them.** The reason Step 5 is short is that we first stripped away the words "cofibration" and "trivial fibration" and replaced them with their lifting characterizations, leaving only $\perp$, which the adjunction can act on. The trigger-reaction pattern: when a statement mixes the model-category classes with a categorical operation ($\otimes$, $[-,-]$, a functor), translate the classes into lifting properties first, do the categorical manipulation on the bare lifting problems, then translate back. This is the universal technique for proving "$F$ is left Quillen", "the pushout-product axiom holds", "this is a Quillen adjunction" — the lifting-property layer is where the algebra happens.

**Getting the corner objects to transpose correctly is the entire difficulty, and the universal properties are the tool.** The seductive wrong move is to transpose $i \otimes 1$ and $1 \otimes j$ separately and try to relate $i \otimes j$ to $[j, p]$, which does not work because it discards the gluing. The correct move uses that a map *out of a pushout* is a compatible tuple (so it can be transposed piece by piece) and a map *into a pullback* is a compatible tuple (so the transposed pieces reassemble). The reusable diagnostic: when transposing a construction involving a colimit on one side, expect a limit on the other, and use the respective universal properties ("maps out of a colimit = compatible cocone", "maps into a limit = compatible cone") to carry the gluing across. This colimit/limit duality under adjunction is the same phenomenon behind RAPL/LAPC and behind why left adjoints preserve colimits. See also [[Ex - Reducing the pushout-product axiom to generating cofibrations]] and the bifunctor theorem [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor]].
