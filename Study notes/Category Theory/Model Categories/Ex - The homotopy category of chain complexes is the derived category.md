---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Homotopy Category of a Model Category"
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a ring and $\mathbf{Ch}(R)$ the category of (non-negatively graded, say) chain complexes of left $R$-modules, equipped with the **projective model structure**: weak equivalences are quasi-isomorphisms, fibrations are the degreewise surjections (in positive degrees), and cofibrations are the degreewise-split monomorphisms with degreewise-projective cokernel.

(a) Show that the cofibrant objects are exactly the complexes of projective modules (bounded below), so that a cofibrant replacement of a module $M$ (regarded as a complex in degree $0$) is a **projective resolution** of $M$.

(b) Show that the model-categorical homotopy relation on chain maps between cofibrant objects coincides with **chain homotopy**: $f \simeq g$ if and only if $f - g = d s + s d$ for some degree-$+1$ map $s$.

(c) Conclude via [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]] that $\mathrm{Ho}(\mathbf{Ch}(R))$ is the **derived category** $D(R)$, with $\mathrm{Hom}_{D(R)}(M, N)$ computed as chain-homotopy classes of chain maps between projective resolutions.

> [!note]- Algebraic background: chain complexes, quasi-isomorphisms, and chain homotopy
> A **chain complex** $C_\bullet$ of $R$-modules is a sequence $\cdots \to C_2 \xrightarrow{d} C_1 \xrightarrow{d} C_0 \to 0$ with $d \circ d = 0$. Its **homology** is $H_n(C) = \ker(d : C_n \to C_{n-1}) / \mathrm{im}(d : C_{n+1} \to C_n)$. A **chain map** $f : C \to D$ is a family $f_n : C_n \to D_n$ commuting with $d$; it induces maps $H_n(f)$ on homology. A **quasi-isomorphism** is a chain map inducing isomorphisms on all homology. A **chain homotopy** between chain maps $f, g : C \to D$ is a family of $R$-module maps $s_n : C_n \to D_{n+1}$ with $f_n - g_n = d_{n+1} s_n + s_{n-1} d_n$; if one exists, $f$ and $g$ are **chain homotopic** and induce the same map on homology. A module $P$ is **projective** if every surjection onto $P$ splits, equivalently $P$ is a direct summand of a free module. A **projective resolution** of a module $M$ is a quasi-isomorphism $P_\bullet \xrightarrow{\sim} M$ from a complex of projectives. The **derived category** $D(R)$ is $\mathbf{Ch}(R)$ with quasi-isomorphisms formally inverted.

**Recall:**

![[Thm - The Homotopy Category of a Model Category#Statement]]

![[Def - Chain Map and Chain Homotopy#The Definition]]

---

# Convergent Strategy

**Problem class:** This is the headline identification problem of the chapter — recognizing $\mathrm{Ho}(\mathbf{Ch}(R))$ as the derived category. It is the homological-algebra instance of "identify the homotopy category" from the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Sources and Targets|topic page]], and it is the bridge that shows derived categories are a special case of homotopy categories.

**Assumption pattern:** The recognizable structure is the dictionary cofibrant = projective, weak equivalence = quasi-isomorphism, homotopy = chain homotopy. Each abstract notion has a concrete homological counterpart, and the exercise is verifying the dictionary entry by entry. Spotting that cofibrant replacement *is* projective resolution is the central recognition.

**Theorem routing:** Part (a) identifies cofibrant objects with complexes of projectives directly from the definition of cofibration. Part (b) computes the cylinder object in $\mathbf{Ch}(R)$ and shows a map out of it is precisely the data of a chain homotopy. Part (c) feeds (a) and (b) into [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]]: $\mathrm{Hom}_{\mathrm{Ho}}(M, N) = \pi(QM, QN) = \{\text{chain maps}\}/\text{chain homotopy}$ between projective resolutions, which is the standard description of the derived category.

**Key decision point:** The crux is part (b): you must compute (or recognize) the cylinder object in $\mathbf{Ch}(R)$ — the algebraic mapping cylinder, built using the chain complex $I = (\cdots \to 0 \to R \to R^2 \to 0)$ modelling the interval — and verify that a chain map out of it unpacks into the equations $f - g = ds + sd$ defining a chain homotopy. Choosing the right algebraic cylinder is what makes the identification work.

---

# Legal Operations Used

1. **Operation 4 from the topic page (replace by a cofibrant model).** Cofibrant replacement in $\mathbf{Ch}(R)$ is projective resolution; this is the operation that produces the objects on which morphisms of $D(R)$ are computed.

2. **Operation 6 from the topic page (build a homotopy as a map out of a cylinder).** The identification of model homotopy with chain homotopy is the computation of what a map out of the algebraic cylinder is.

3. **Operation 1 from the topic page (factor a map).** Cofibrant replacement is the factorization of $\varnothing \to M$ (here $0 \to M$), which in $\mathbf{Ch}(R)$ is the construction of a projective resolution.

---

# Hints

> [!note]- Hint 1
> For (a): an object $C$ is cofibrant iff $0 \to C$ is a cofibration, i.e. (by the model structure) $C$ is a complex with projective terms (degreewise-projective cokernel of $0 \to C$ is $C$ itself). So cofibrant = complex of projectives. A cofibrant replacement of a module $M$ is a quasi-isomorphism $P_\bullet \xrightarrow{\sim} M$ from a complex of projectives — a projective resolution.

> [!note]- Hint 2
> For (b): the cylinder object for $C$ is the algebraic mapping cylinder. Concretely, tensor with the "interval complex" or build $\mathrm{Cyl}(C) = C \oplus C \oplus C[1]$ with a suitable differential, factoring the fold map $C \oplus C \to C$.

> [!note]- Hint 3
> A chain map $H : \mathrm{Cyl}(C) \to D$ restricting to $f$ and $g$ on the two copies of $C$ is determined by $f$, $g$, and a map on the $C[1]$ summand — and that extra map, by compatibility with the differential, is exactly a chain homotopy $s$ with $f - g = ds + sd$.

> [!note]- Hint 4
> For (c): apply [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]]. Bifibrant objects are bounded-below complexes of projectives (every object is fibrant here, in the non-negatively-graded convention). So $\mathrm{Hom}_{\mathrm{Ho}}(M, N) = \pi(P_\bullet^M, P_\bullet^N)$ = chain-homotopy classes of chain maps between projective resolutions = $\mathrm{Hom}_{D(R)}(M, N)$.

---

# Solution

The solution matches each model-categorical notion to its homological counterpart: cofibrant to projective (a), model homotopy to chain homotopy (b), and then assembles the derived-category description via the fundamental theorem (c).

**Step 1: Cofibrant objects are complexes of projectives; cofibrant replacement is projective resolution.**

> [!note]- Derivation
> By definition of the projective model structure, $C$ is cofibrant iff $0 \to C$ is a cofibration, i.e. a degreewise-split monomorphism whose cokernel ($= C$) is degreewise projective. So $C$ is cofibrant iff each $C_n$ is a projective $R$-module (and $C$ is bounded below). A cofibrant replacement of $M$ (placed in degree $0$) is, by [[Def - Cofibrant and Fibrant Objects]], a trivial fibration $QM \xrightarrow{\sim} M$ with $QM$ cofibrant — a quasi-isomorphism from a complex of projectives to $M$, which is exactly a **projective resolution** $\cdots \to P_1 \to P_0 \xrightarrow{\sim} M$. (That projective resolutions exist is the statement that $\mathbf{Ch}(R)$ has enough projectives, the homological form of MC5.)

**Step 2: Model homotopy = chain homotopy.**

> [!note]- Derivation
> Build the cylinder object for a complex $C$. The algebraic interval is the complex $I$ with $I_0 = R \oplus R$ (the two endpoints) and $I_1 = R$ (the edge), $d : I_1 \to I_0$, $1 \mapsto (1, -1)$. The cylinder is $\mathrm{Cyl}(C) = C \otimes I$, which in each degree is $C_n \oplus C_n \oplus C_{n-1}$, with the end-inclusions $\mathrm{i}_0, \mathrm{i}_1$ the two $C \to C \otimes I$ from the endpoints and the projection $\sigma : C \otimes I \to C$ collapsing the interval (a quasi-isomorphism since $I \to R$ is). A chain map $H : C \otimes I \to D$ is determined by its restrictions to the two endpoint copies of $C$ — call them $f = H\mathrm{i}_0$, $g = H\mathrm{i}_1$ — together with its value $s$ on the "edge" summand $C[1]$ (the shifted $C_{n-1}$ in degree $n$). The condition that $H$ commutes with the differential of $C \otimes I$ unpacks exactly to
> $$f_n - g_n = d_{n+1} s_n + s_{n-1} d_n,$$
> i.e. $s$ is a **chain homotopy** from $g$ to $f$. Hence $f \simeq g$ (model homotopy, via this cylinder) iff $f$ and $g$ are chain homotopic. Since cofibrant objects are complexes of projectives and these are bifibrant, [[Ex - Left homotopy is an equivalence relation on cofibrant objects|the equivalence-relation theorem]] guarantees this relation is well-defined and independent of cylinder choice.

**Step 3: Conclude $\mathrm{Ho}(\mathbf{Ch}(R)) = D(R)$.**

> [!note]- Derivation
> By [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]], $\mathrm{Ho}(\mathbf{Ch}(R))$ is equivalent to the category of bifibrant objects and homotopy classes of maps, with $\mathrm{Hom}_{\mathrm{Ho}}(X, Y) = \pi(QRX, QRY)$. In the non-negatively-graded projective model structure every object is fibrant, so $R = \mathrm{id}$, and a bifibrant object is a complex of projectives. For modules $M, N$ regarded as complexes in degree $0$, $QM = P_\bullet^M$ and $QN = P_\bullet^N$ are projective resolutions (Step 1), and
> $$\mathrm{Hom}_{\mathrm{Ho}(\mathbf{Ch}(R))}(M, N) = \pi(P_\bullet^M, P_\bullet^N) = \{\text{chain maps } P_\bullet^M \to P_\bullet^N\}/\text{chain homotopy}$$
> by Step 2. This is precisely the standard description of $\mathrm{Hom}_{D(R)}(M, N)$ in the derived category. Since the localizations agree (both invert quasi-isomorphisms) and the hom-sets agree, $\mathrm{Ho}(\mathbf{Ch}(R)) \simeq D(R)$.

> [!note]- Complete formal solution
> **(a)** $C$ is cofibrant iff $0 \to C$ is a cofibration, i.e. $C$ is degreewise projective. A cofibrant replacement of a module $M$ is a quasi-isomorphism from a complex of projectives — a projective resolution.
>
> **(b)** The cylinder $C \otimes I$ (with $I$ the interval complex $R \xrightarrow{(1,-1)} R \oplus R$) has end-inclusions $\mathrm{i}_0, \mathrm{i}_1$ and quasi-isomorphism projection $\sigma$. A chain map $H : C \otimes I \to D$ with $H\mathrm{i}_0 = f$, $H\mathrm{i}_1 = g$ is the data of $f, g$ and a degree-$+1$ map $s$ on the edge summand; commutation with the differential gives $f - g = ds + sd$. So model homotopy is chain homotopy.
>
> **(c)** By the fundamental theorem, $\mathrm{Hom}_{\mathrm{Ho}}(M, N) = \pi(QM, QN)$ = chain-homotopy classes of chain maps between projective resolutions $= \mathrm{Hom}_{D(R)}(M, N)$. Hence $\mathrm{Ho}(\mathbf{Ch}(R)) \simeq D(R)$. $\blacksquare$

---

# Key Takeaways

**The derived category is a homotopy category, and this exercise is the dictionary that makes the identification precise.** The slogan "$\mathrm{Ho}(\mathbf{Ch}(R)) = D(R)$" rests on three dictionary entries — cofibrant = projective, weak equivalence = quasi-isomorphism, homotopy = chain homotopy — each of which is a short verification. Once the dictionary is in place, every fact about model categories becomes a fact about the derived category: cofibrant replacement is resolution, the homotopy category's morphisms are chain-homotopy classes, and derived functors are functors-after-resolution. This is the single most important bridge in the chapter for anyone with a homological-algebra background, because it reveals that the seemingly ad hoc construction of $D(R)$ (formally invert quasi-isomorphisms) is computable for exactly the reason the abstract theory says — the model structure tames the localization.

**Cofibrant replacement is projective resolution, which demystifies why resolutions are everywhere in homological algebra.** The reason you resolve a module before computing $\mathrm{Tor}$ or $\mathrm{Ext}$ is not a trick — it is cofibrant replacement, the universal move of replacing an object by a homotopically well-behaved model. The abstract theory predicts that you must replace by a cofibrant object before applying a left-derived functor, and in $\mathbf{Ch}(R)$ "cofibrant" means "projective," so the prediction is exactly "resolve by projectives." Recognizing resolution as a special case of (co)fibrant replacement unifies the homological-algebra and homotopy-theory pictures and tells you, in any new setting, what the analogue of resolution should be: whatever the cofibrant objects are.

**The model homotopy relation unpacks to chain homotopy because the algebraic cylinder encodes the equation $f - g = ds + sd$.** The abstract definition "map out of a cylinder object" becomes, in chain complexes, the concrete chain-homotopy data, because the algebraic interval complex $I$ has exactly one extra generator (the edge) whose image under a chain map, constrained by the differential, is the homotopy operator $s$. This is the mechanism by which the abstract and concrete homotopy relations coincide, and it generalizes: in any model category the cylinder object is "the source fattened by one dimension," and a map out of it is "the two maps plus a witness to their being connected." Seeing the chain-homotopy formula fall out of the cylinder's differential is the kind of computation that makes the abstract definition feel inevitable rather than arbitrary.
