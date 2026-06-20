---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Projective Model Structure on Chain Complexes"
  - "Thm - Chain Complexes of Modules Form a Model Category"
  - "Thm - The Homotopy Category of a Model Category"
  - "Def - Chain Map and Chain Homotopy"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Prove that the [[Thm - The Homotopy Category of a Model Category|homotopy category]] of $\mathbf{Ch}(R)$ in the [[Def - Projective Model Structure on Chain Complexes|projective model structure]] is the derived category:
$$\mathrm{Ho}(\mathbf{Ch}(R)) \;\simeq\; D(R).$$
Specifically, show that (i) the abstract left-homotopy relation on cofibrant complexes coincides with [[Def - Chain Map and Chain Homotopy|chain homotopy]], and (ii) fibrant–cofibrant replacement of a [[Def - Module|module]] is its projective resolution, so that morphisms in $\mathrm{Ho}(\mathbf{Ch}(R))$ between modules $M, N$ (in degree $0$) are chain-homotopy classes of maps between projective resolutions, which is the definition of $\mathrm{Hom}_{D(R)}(M, N)$.

**Recall:**

![[Thm - The Homotopy Category of a Model Category#Statement]]

A [[Def - Chain Map and Chain Homotopy|chain homotopy]] between chain maps $f, g : C \to D$ is a degree-$+1$ family $s_n : C_n \to D_{n+1}$ with $f - g = dс + sd$ (precisely $f_n - g_n = d^D_{n+1} s_n + s_{n-1} d^C_n$); $f$ and $g$ are then **chain homotopic**. The **derived category** $D(R)$ is the localization of $\mathbf{Ch}(R)$ at the quasi-isomorphisms; on bounded-below complexes its morphisms are chain-homotopy classes of maps between complexes of projectives. Every complex is fibrant in the projective model structure, and the cofibrant complexes are the bounded-below complexes of projectives.

---

# Convergent Strategy

**Problem class:** This is an "identify the homotopy category" problem, the third recurring target of the chapter. The route, as always, runs through the [[Thm - The Homotopy Category of a Model Category|fundamental theorem]]: determine the bifibrant objects and what homotopy of maps between them means concretely, then read off $\mathrm{Ho}$.

**Assumption pattern:** The assumptions are the three classes of the projective model structure, plus the fact (from [[Thm - Chain Complexes of Modules Form a Model Category]]) that the structure exists. The decisive structural facts are "every object is fibrant" (so bifibrant = cofibrant = complex of projectives) and "the cylinder object realises chain homotopy", which together collapse the abstract description to a concrete one.

**Theorem routing:** The fundamental theorem gives $\mathrm{Ho}(\mathbf{Ch}(R))(X, Y) \cong \pi(QX, QY)$ where $\pi$ is abstract homotopy classes and $Q$ is cofibrant replacement (no fibrant replacement needed since all objects are fibrant). The route is then: (a) compute the cylinder object of a cofibrant complex and check abstract left homotopy = chain homotopy; (b) identify cofibrant replacement of a module with projective resolution (this is [[Ex - Identifying the cofibrant objects in chain complexes|the previous exercise]]); (c) conclude the Hom-sets match those of $D(R)$.

**Key decision point:** The non-obvious move is constructing the cylinder object explicitly and verifying that a left homotopy through it unwinds to the equation $f - g = ds + sd$. Many treatments assert "homotopy = chain homotopy" without exhibiting the cylinder; the content of the exercise is in that identification, and the natural alternative — trying to match the universal properties abstractly — is far harder than the direct computation with the standard cylinder $C \oplus C \oplus C[1]$.

---

# Legal Operations Used

1. **Operation 3 from the topic page (replace a module by its projective resolution).** Used to identify cofibrant replacement with projective resolution, supplying the objects of $D(R)$.

2. **Operation 6 from the topic page (build a homotopy as a map out of a cylinder).** The core of part (i): a left homotopy is a chain map out of the cylinder object, which we unwind into a chain homotopy.

3. **Operation 1 from the topic page (check a chain-complex condition one degree at a time).** Verifying the cylinder's structure maps and the homotopy equation is done degreewise.

---

# Hints

> [!note]- Hint 1
> Every complex is fibrant. So in the fundamental theorem's formula $\mathrm{Ho}(X,Y) \cong \pi(QRX, QRY)$, what does the fibrant replacement $R$ do, and what is left?

> [!note]- Hint 2
> The cylinder object of a cofibrant $C$ can be taken to be $\mathrm{Cyl}(C) = C \oplus C \oplus C[1]$ with a differential mixing the two copies of $C$ through the shifted copy $C[1]$. A left homotopy $C \to D$ out of this restricts to $f$ and $g$ on the two $C$-summands. What does the $C[1]$-component give you?

> [!note]- Hint 3
> Write a chain map $\mathrm{Cyl}(C) \to D$ as $(f, g, s)$ where $s : C[1] \to D$ has degree $+1$ as a map $C \to D$. Impose that it is a chain map (commutes with the differential). The resulting equation on $s$ is exactly $f - g = ds + sd$.

---

# Solution

The proof assembles three facts. Every object is fibrant, so bifibrant means cofibrant means complex of projectives. The standard cylinder object turns abstract left homotopy into the chain-homotopy equation $f - g = ds + sd$. Cofibrant replacement of a module is its projective resolution. Feeding these into the fundamental theorem yields $\mathrm{Ho}(\mathbf{Ch}(R)) \simeq D(R)$.

**Step 1: bifibrant = cofibrant = complex of projectives.**

> [!note]- Derivation
> In the projective model structure, every complex $C$ is fibrant because $C \to 0$ is degreewise surjective (the zero map onto the zero module). So an object is bifibrant exactly when it is cofibrant, which (by [[Ex - Identifying the cofibrant objects in chain complexes|the cofibrancy criterion]]) means it is a bounded-below complex of [[Def - Projective Module|projectives]]. The fundamental theorem's formula simplifies: since $R$ (fibrant replacement) can be taken to be the identity,
> $$\mathrm{Ho}(\mathbf{Ch}(R))(X, Y) \cong \pi(QX, QY),$$
> where $Q$ is cofibrant replacement and $\pi$ denotes abstract homotopy classes of chain maps.

**Step 2: abstract left homotopy = chain homotopy.**

> [!note]- Derivation
> Let $C$ be cofibrant. A **cylinder object** for $C$ factors the fold map $C \oplus C \xrightarrow{\nabla} C$ as a cofibration followed by a weak equivalence. The standard choice is
> $$\mathrm{Cyl}(C) = C \oplus C \oplus C[1], \qquad d(a, b, c) = (da + c,\; db - c,\; -dc),$$
> where $C[1]$ is $C$ shifted up by one degree (so an element of $C[1]_n$ is an element of $C_{n-1}$). The two end-inclusions $C \to \mathrm{Cyl}(C)$ are $a \mapsto (a, 0, 0)$ and $b \mapsto (0, b, 0)$, and the projection $\mathrm{Cyl}(C) \xrightarrow{\sim} C$, $(a,b,c) \mapsto a + b$, is a quasi-isomorphism; the inclusion $C \oplus C \hookrightarrow \mathrm{Cyl}(C)$ is a cofibration since its cokernel $C[1]$ is degreewise projective.
>
> A **left homotopy** from $f$ to $g$ is a chain map $H : \mathrm{Cyl}(C) \to D$ with $H|_{\text{first } C} = f$ and $H|_{\text{second } C} = g$. Write $H(a, b, c) = f(a) + g(b) + s(c)$ where $s : C[1] \to D$ is, as a map $C \to D$, of degree $+1$. The condition that $H$ is a chain map is $d^D H = H d^{\mathrm{Cyl}}$. Evaluating on $(0, 0, c)$:
> $$d^D(s(c)) = H(d(0,0,c)) = H(c, -c, -dc) = f(c) - g(c) + s(-dc) = f(c) - g(c) - s(dc).$$
> Rearranging, $f - g = d^D s + s\, d^C$ — exactly the [[Def - Chain Map and Chain Homotopy|chain homotopy]] equation, with $s$ the chain-homotopy operator. Conversely any chain homotopy $s$ defines such an $H$. So abstract left homotopy of maps out of a cofibrant complex is precisely chain homotopy.

**Step 3: cofibrant replacement = projective resolution, and the conclusion.**

> [!note]- Derivation
> By [[Ex - Identifying the cofibrant objects in chain complexes|the cofibrant-objects exercise]], the cofibrant replacement $QM$ of a module $M$ (in degree $0$) is a projective resolution $P_\bullet \xrightarrow{\sim} M$. Combining Steps 1–2 with the fundamental theorem:
> $$\mathrm{Ho}(\mathbf{Ch}(R))(M, N) \cong \pi(QM, QN) = \{\text{chain maps } P^M_\bullet \to P^N_\bullet\}/(\text{chain homotopy}),$$
> where $P^M_\bullet, P^N_\bullet$ are projective resolutions of $M, N$. But this set is, by definition, $\mathrm{Hom}_{D(R)}(M, N)$ — morphisms in the derived category between bounded-below complexes are chain-homotopy classes of maps between their projective resolutions. The same identification holds for arbitrary bounded-below complexes (replace $M, N$ by general $X, Y$ and their projective resolutions). Therefore $\mathrm{Ho}(\mathbf{Ch}(R)) \simeq D(R)$.

> [!note]- Complete formal solution
> Every complex is fibrant ($C \to 0$ is degreewise surjective), so bifibrant = cofibrant = bounded-below complex of projectives, and the [[Thm - The Homotopy Category of a Model Category|fundamental theorem]] gives $\mathrm{Ho}(\mathbf{Ch}(R))(X,Y) \cong \pi(QX, QY)$ with $Q$ cofibrant replacement.
>
> For a cofibrant $C$, the cylinder $\mathrm{Cyl}(C) = C \oplus C \oplus C[1]$ with $d(a,b,c) = (da + c, db - c, -dc)$ factors the fold map as a cofibration (cokernel $C[1]$ projective) followed by the quasi-isomorphism $(a,b,c)\mapsto a+b$. A left homotopy $H : \mathrm{Cyl}(C) \to D$ from $f$ to $g$, written $H(a,b,c) = f(a)+g(b)+s(c)$, is a chain map iff $f - g = ds + sd$, i.e. iff $s$ is a chain homotopy. So abstract homotopy = chain homotopy on cofibrant objects.
>
> Cofibrant replacement of a module $M$ is a projective resolution $P^M_\bullet \xrightarrow{\sim} M$. Hence $\mathrm{Ho}(\mathbf{Ch}(R))(M,N) \cong \{P^M_\bullet \to P^N_\bullet\}/(\text{chain homotopy}) = \mathrm{Hom}_{D(R)}(M, N)$, and likewise for general bounded-below complexes. Therefore $\mathrm{Ho}(\mathbf{Ch}(R)) \simeq D(R)$. $\blacksquare$

---

# Key Takeaways

**The fundamental theorem is a machine: feed it the bifibrant objects and the homotopy relation, get the homotopy category.** This exercise is the template for every "identify $\mathrm{Ho}$" problem. You never compute the localization directly — you determine which objects are bifibrant (here, complexes of projectives), what homotopy of maps between them means concretely (here, chain homotopy), and then the fundamental theorem assembles these into a description of $\mathrm{Ho}$. The trigger is "identify the homotopy category"; the reaction is the two-step "find the bifibrant objects, then unwind the cylinder/path object into a concrete homotopy relation". The same template gives the homotopy category of spaces (CW complexes and homotopy classes) and the stable module category (all modules, maps modulo projectives).

**The cylinder object is where abstract homotopy becomes computable, and the standard chain-complex cylinder encodes $f - g = ds + sd$ exactly.** The mapping-cylinder construction $C \oplus C \oplus C[1]$ is worth memorising, because the appearance of the shifted summand $C[1]$ is *forced*: it is the algebraic incarnation of the interval coordinate, and the chain-homotopy operator $s$ is the map out of it. The general lesson is that the cylinder object's "extra" summand always carries the homotopy data — in topology it is the interval direction $A \times I$, in chain complexes it is $C[1]$, in simplicial sets it is $A \times \Delta^1$. Whenever you need to make an abstract homotopy concrete, build the cylinder explicitly and read the homotopy as the map out of the extra direction.

**This identification is the founding bridge between homological algebra and homotopy theory.** The result $\mathrm{Ho}(\mathbf{Ch}(R)) = D(R)$ is not a curiosity; it is the statement that the derived category — defined classically by the inscrutable process of formally inverting quasi-isomorphisms — is computable, with concrete Hom-sets given by chain-homotopy classes between resolutions. Every time you compute a map in a derived category, an Ext group, or a morphism in a triangulated category, you are using this identification. The diagnostic to carry away: whenever a localized or "derived" category appears and you need to compute in it, look for a model structure presenting it, because the model structure's bifibrant objects and homotopy relation give the computable description. The inscrutable zig-zags of the naive localization always collapse to honest homotopy classes once the model structure is in hand.
