---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Mass in a Homology Class"
  - "Def - First Homology, Characters, and Finite Fourier Analysis"
tags: [paper, brownian-loops, homology]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 6.2"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface.
- $H_1(X, \mathbb{Z})$ the first homology group of $X$; $\beta \in H_1(X, \mathbb{Z})$ a class; $[\gamma] \in H_1(X, \mathbb{Z})$ the homology class of $\gamma \in \Gamma$.
- $\mu^\kappa_X(\beta)$ the mass in homology class $\beta$ (Def 6.1); $L_X(s, \chi)$ the Selberg $L$-function (Def 6.3); $\chi : H_1(X, \mathbb{Z}) \to S^1$ a unitary character.
- $[$LJ11$]$ — Le Jan, *Markov paths, loops and fields*, Springer École d'Été de Probabilités de Saint-Flour, 2011.

> [!recall]- Homology class $[\gamma]$ and character $\chi([\gamma])$
> **Formally:** the Hurewicz map $\gamma \mapsto [\gamma] \in H_1(X, \mathbb{Z})$ is a group homomorphism from $\Gamma$ to its abelianisation, so it satisfies $[\gamma_1 \gamma_2] = [\gamma_1] + [\gamma_2]$ and $[\gamma^m] = m[\gamma]$. A *unitary character* $\chi : H_1(X, \mathbb{Z}) \to S^1 = \{z \in \mathbb{C} : |z| = 1\}$ is a group homomorphism; because it is a homomorphism, $\chi(m[\gamma]) = \chi([\gamma])^m$, and this value depends only on $m[\gamma]$, not on which $(\gamma, m)$ realises it.
> **In words:** the character value $\chi([\gamma])$ is a complex number of modulus $1$ attached to each topological type of loop on $X$; because $\chi$ only sees the net winding around each independent cycle (not the internal order in which handles are traversed), many different topological types with the same net winding get the same value $\chi(\beta)$. This is exactly the property the Fourier regrouping in Corollary 6.4 needs.
> **Concretely:** on the torus $T^2$ with $H_1 = \mathbb{Z}^2$, a character $\chi_{(u,v)}(a, b) = e^{2\pi i(au + bv)}$ evaluates on the class $(3, 5) \in H_1$ to $e^{2\pi i(3u + 5v)}$; the same value would be produced by any $(\gamma, m)$ whose iterate lies in $(3, 5)$. See [[Def - First Homology, Characters, and Finite Fourier Analysis]].

---

# Statement

> **Remark 6.2 (Belyaev–Huseynli).** The first definition of a Brownian loop measure on homology classes appeared, to the authors' knowledge, in Le Jan's monograph [LJ11]. Le Jan's definition was initially opaque to the present authors due to differing conventions and techniques, so the definition [[Def - Mass in a Homology Class|Definition 6.1]] was developed independently; the authors later found that the two agree, and that the Selberg $L$-function route pursued here provides a *dual* approach to Le Jan's, recovering his results in greater generality — in particular extending the construction to the non-compact case.
>
> One motivation for grading by homology (rather than the finer homotopy grading of §3) is that *geometric* intersection numbers of closed geodesics are well-defined on free homotopy classes, but *algebraic* intersection numbers are defined on homology classes. Moreover, the weight $\chi([\gamma])^m$ appearing in the logarithmic expansion of the Selberg $L$-function (Corollary 6.4) depends only on the homology class of the iterate $\gamma^m$, not on the particular geodesic representative $\gamma$: for every $(\gamma, m)$ with $m[\gamma] = \beta$,
> $$\chi([\gamma])^m = \chi(m[\gamma]) = \chi(\beta).$$
> This is exactly the property that lets the double sum over $(\gamma, m)$ regroup by homology class $\beta$.

---

# In One Line

The homology-graded Brownian loop measure was first defined by Le Jan; the paper's independent definition agrees with his and extends the setup to non-compact surfaces via the character-twisted Selberg zeta — a Fourier-analytic *dual* of Le Jan's approach.

---

# Unpacking

**Historical provenance.** Le Jan's *Markov paths, loops and fields* [LJ11] introduced a version of the Brownian loop measure decomposed by first-homology class, using techniques based on the compact-case trace formula and specific to that setting. The Belyaev–Huseynli paper arrived at Definition 6.1 independently — the authors report that Le Jan's conventions and techniques were opaque to them on first reading — and only later verified that the two definitions coincide where both are defined. The paper's contribution here is not the *definition* (which agrees with Le Jan's in the compact case) but the *route*: by twisting the Selberg zeta with a character and inverting the resulting Fourier series over the character torus, one recovers $\mu^\kappa_X(\beta)$ analytically, with no need to enumerate the infinitely many conjugacy classes above $\beta$. This analytic route extends verbatim to the non-compact geometrically finite case, which Le Jan's compact-only argument did not cover.

**The intersection-geometry motivation.** Given two oriented closed curves $\alpha, \beta$ on $X$, there are two natural intersection numbers.

- The *geometric* intersection number $i(\alpha, \beta) := \min|\alpha' \cap \beta'|$, minimising over representatives $\alpha' \in [\alpha]$, $\beta' \in [\beta]$ in their free homotopy classes: an unsigned count. Depends only on the free homotopy classes.
- The *algebraic* intersection number $\hat i([\alpha], [\beta]) := \sum_p \epsilon_p \in \mathbb{Z}$, a signed count with $\epsilon_p = \pm 1$ according to the orientation of the crossing at $p$. Two homologous curves have the same algebraic intersection with any third curve; homotopically different but homologous curves may have different geometric intersections but must have the same algebraic one. So $\hat i$ is a homology invariant.

Consequently, distributional questions about *algebraic* intersections — the expected signed self-intersection of a random loop, the variance of the algebraic-intersection pairing between two soup components, and so on — are naturally asked on the *homology-graded* measure $\mu^\kappa_X(\beta)$. Distributional questions about *geometric* intersections use the finer homotopy grading of §3. The two graded measures are two levels of a hierarchy, each right for its own class of questions.

**The character weight is what makes the regrouping work.** The key mechanical fact making Definition 6.1 tractable via Selberg $L$-functions is the identity $\chi([\gamma])^m = \chi(\beta)$ whenever $m[\gamma] = \beta$. If instead one twisted by a class function that depended on the *conjugacy* class of $\gamma$ (rather than its image in $H_1$), the sum would not regroup by homology and no Fourier inversion would exist. This is why *unitary characters* on $H_1$ — one-dimensional representations of the abelianisation — are exactly the right family to twist by.

---

# Where the paper uses this

Explanatory commentary on [[Def - Mass in a Homology Class|Definition 6.1]] in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]]; also motivates the introduction of the Selberg $L$-function ([[Def - Selberg L-Function]]) (Def 6.3), by pointing out that the character weight $\chi([\gamma])^m$ regroups the double sum by homology. Downstream: the Fourier inversion of [[Thm - Fourier Inversion by Homology Class|Theorem 6.5]] realises this regrouping analytically, and [[Prop - Total Homology of the Loop Soup|Proposition 6.7]] reads off the distribution of the total homology of the loop soup.
