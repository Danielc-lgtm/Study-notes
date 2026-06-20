---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Stable Module Category over a Frobenius Ring"
  - "Def - Projective Module"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a Frobenius ring. For a [[Def - Module|module]] $M$, define the **syzygy** $\Omega M = \ker(P \twoheadrightarrow M)$ for a projective cover $P \twoheadrightarrow M$, and the **cosyzygy** $\Sigma M = \operatorname{coker}(M \hookrightarrow I)$ for an injective hull $M \hookrightarrow I$.

**(a)** Show that $\Omega M$ and $\Sigma M$ are well-defined functors on the [[Def - Stable Module Category over a Frobenius Ring|stable module category]] $\underline{\mathbf{Mod}}_R$ (independent of the chosen cover/hull up to stable isomorphism).

**(b)** Using that $R$ is Frobenius (projective = injective), show that $\Omega$ and $\Sigma$ are **mutually inverse autoequivalences** of $\underline{\mathbf{Mod}}_R$, so $\Sigma = \Omega^{-1}$ is an invertible suspension. Conclude that, together with the distinguished triangles from short exact sequences, $\underline{\mathbf{Mod}}_R$ is a **triangulated category**.

**Recall:**

A **projective cover** of $M$ is a surjection $P \twoheadrightarrow M$ with $P$ projective and the kernel "small" (superfluous); over a Frobenius ring these exist. An **injective hull** is a minimal injective $M \hookrightarrow I$. Over a Frobenius ring, projective $=$ injective. **Schanuel's lemma:** if $0 \to K \to P \to M \to 0$ and $0 \to K' \to P' \to M \to 0$ are short exact with $P, P'$ projective, then $K \oplus P' \cong K' \oplus P$. A **triangulated category** is an additive category with an invertible shift $\Sigma$ and a class of distinguished triangles satisfying the octahedral and related axioms. See [[Def - Stable Module Category over a Frobenius Ring]].

---

# Convergent Strategy

**Problem class:** This is a "construct the suspension and triangulated structure" problem — establishing the higher structure on the stable category. The routine is to build the (co)syzygy functors, prove independence of choices via Schanuel's lemma, then use the Frobenius condition to make them mutually inverse.

**Assumption pattern:** The recognisable structure is "Frobenius ring", whose defining payoff is projective = injective. This is what lets the syzygy (built from projective covers) and cosyzygy (built from injective hulls) cancel: the projective $P$ in $0 \to \Omega M \to P \to M \to 0$ is *also* injective, so the same sequence reads as an injective hull witnessing $\Omega M \hookrightarrow P$ with cokernel $M$, i.e. $\Sigma\Omega M = M$.

**Theorem routing:** Part (a): Schanuel's lemma shows $\Omega M$ is independent of the projective cover up to adding a projective (= up to stable isomorphism), and dually for $\Sigma M$; functoriality follows from lifting maps across the covers modulo projectives. Part (b): the short exact sequence $0 \to \Omega M \to P \to M \to 0$ with $P$ projective = injective is simultaneously the syzygy sequence of $M$ and the cosyzygy sequence of $\Omega M$, giving $\Sigma\Omega M \cong M$ stably, and dually $\Omega\Sigma M \cong M$; the distinguished triangles are these short exact sequences.

**Key decision point:** The crucial move is reading the *single* short exact sequence $0 \to \Omega M \to P \to M \to 0$ two ways: as the defining sequence of $\Omega M$ (kernel of a projective cover of $M$) and as a defining sequence of $\Sigma(\Omega M)$ (cokernel of an injective hull of $\Omega M$, using $P$ injective). This double reading, available only because $P$ is both projective and injective, is the entire reason $\Sigma$ and $\Omega$ cancel. Missing the double reading — treating $\Omega$ and $\Sigma$ as living in separate worlds — is the natural error.

---

# Legal Operations Used

1. **Operation 8 from the topic page (take the syzygy or cosyzygy to suspend or loop).** The entire exercise constructs and analyses these functors.

2. **Operation 7 from the topic page (quotient out maps through projectives).** Used to show well-definedness: the syzygy is independent of choices *up to maps through projectives*, i.e. stably.

---

# Hints

> [!note]- Hint 1
> For (a), apply Schanuel's lemma to two projective covers $0 \to K \to P \to M \to 0$ and $0 \to K' \to P' \to M \to 0$. The conclusion $K \oplus P' \cong K' \oplus P$ says $K$ and $K'$ differ by projective summands. Why does that make $K \cong K'$ in the *stable* category?

> [!note]- Hint 2
> For (b), take the short exact sequence $0 \to \Omega M \to P \to M \to 0$ with $P$ a projective cover. Now use that $R$ is Frobenius: $P$ is also injective. Re-read the sequence as an injective hull of $\Omega M$. What is its cokernel?

> [!note]- Hint 3
> The cokernel of $\Omega M \hookrightarrow P$ is $M$ (by exactness). So $P$ is an injective module containing $\Omega M$ with cokernel $M$ — that says $\Sigma(\Omega M) = M$ (up to the hull being minimal, which holds stably). Dually $\Omega(\Sigma M) = M$. Hence $\Sigma = \Omega^{-1}$.

---

# Solution

The syzygy and cosyzygy are well-defined modulo projectives by Schanuel's lemma. The Frobenius condition makes a single short exact sequence serve as both the syzygy sequence of $M$ and the cosyzygy sequence of $\Omega M$, so $\Sigma$ and $\Omega$ cancel; the short exact sequences become the distinguished triangles, giving the triangulated structure.

**Step 1 (a): $\Omega$ and $\Sigma$ are well-defined on $\underline{\mathbf{Mod}}_R$.**

> [!note]- Derivation
> Let $0 \to K \to P \xrightarrow{\pi} M \to 0$ and $0 \to K' \to P' \xrightarrow{\pi'} M \to 0$ be two presentations with $P, P'$ projective. By **Schanuel's lemma**, $K \oplus P' \cong K' \oplus P$. Since $P, P'$ are projective, they are zero in $\underline{\mathbf{Mod}}_R$ (by [[Ex - Projective objects become zero in the stable category|the previous exercise]]), so in the stable category $K \cong K \oplus P' \cong K' \oplus P \cong K'$. Hence $\Omega M = K$ is independent of the projective cover *up to stable isomorphism*, so $\Omega$ is well-defined on objects of $\underline{\mathbf{Mod}}_R$.
>
> Functoriality: a map $f : M \to N$ lifts to a map of chosen presentations $P_M \to P_N$ (projectivity of $P_M$), restricting to a map $\Omega M \to \Omega N$; the lift is unique up to maps through projectives, so $\Omega f$ is well-defined in $\underline{\mathbf{Mod}}_R$. Dually, $\Sigma M = \operatorname{coker}(M \hookrightarrow I)$ is well-defined and functorial, using injective hulls and the dual of Schanuel's lemma (injectives are zero in $\underline{\mathbf{Mod}}_R$ too, since projective = injective).

**Step 2 (b): $\Sigma$ and $\Omega$ are mutually inverse.**

> [!note]- Derivation
> Take a projective cover and form
> $$0 \longrightarrow \Omega M \longrightarrow P \xrightarrow{\;\pi\;} M \longrightarrow 0, \qquad P \text{ projective}.$$
> Because $R$ is **Frobenius**, $P$ is *also injective*. So the inclusion $\Omega M \hookrightarrow P$ exhibits $\Omega M$ inside an injective module $P$ with cokernel $\operatorname{coker}(\Omega M \hookrightarrow P) = M$ (by exactness of the sequence). This is exactly the data computing the cosyzygy of $\Omega M$:
> $$\Sigma(\Omega M) = \operatorname{coker}(\Omega M \hookrightarrow P) = M.$$
> (One must check $\Omega M \hookrightarrow P$ is an injective hull up to stable isomorphism; minimality holds modulo projective-injective summands, which are zero stably, so the identity holds in $\underline{\mathbf{Mod}}_R$.) Thus $\Sigma\Omega \cong \mathrm{id}$ on $\underline{\mathbf{Mod}}_R$.
>
> Dually, take an injective hull $0 \to M \to I \to \Sigma M \to 0$ with $I$ injective = projective. Then $I \twoheadrightarrow \Sigma M$ is a projective cover of $\Sigma M$ (up to stable iso) with kernel $M$, so $\Omega(\Sigma M) = \ker(I \to \Sigma M) = M$, giving $\Omega\Sigma \cong \mathrm{id}$. Therefore $\Sigma$ and $\Omega$ are mutually inverse autoequivalences of $\underline{\mathbf{Mod}}_R$, and $\Sigma = \Omega^{-1}$ is an invertible suspension.

**Step 3 (b): the triangulated structure.**

> [!note]- Derivation
> Distinguished triangles in $\underline{\mathbf{Mod}}_R$ are defined to be (the isomorphs in the stable category of) the images of short exact sequences $0 \to M \to E \to N \to 0$, completed by the connecting map $N \to \Sigma M$:
> $$M \longrightarrow E \longrightarrow N \xrightarrow{\;\partial\;} \Sigma M.$$
> The connecting map $\partial$ is constructed from the comparison of the sequence with an injective hull of $M$, exactly as $\Sigma$ was built. With the invertible shift $\Sigma$ from Step 2 and these triangles, one verifies the triangulated axioms TR1–TR4 (existence, rotation, morphisms of triangles, and the octahedral axiom) — each reduces to a diagram chase among short exact sequences, with the Frobenius condition ensuring rotation is possible (it needs $\Sigma$ invertible). Hence $\underline{\mathbf{Mod}}_R$ is a **triangulated category**. The invertibility of $\Sigma$ — which *is* the Frobenius condition — is precisely the "stable" in stable module category.

> [!note]- Complete formal solution
> **(a)** For two projective presentations of $M$, Schanuel's lemma gives $\Omega M \oplus P' \cong \Omega' M \oplus P$ with $P, P'$ projective; since projectives are zero in $\underline{\mathbf{Mod}}_R$, $\Omega M \cong \Omega' M$ stably. Functoriality follows from lifting maps across covers modulo projectives. Dually for $\Sigma$ via injective hulls.
>
> **(b)** The sequence $0 \to \Omega M \to P \to M \to 0$ with $P$ projective = injective (Frobenius) is simultaneously the syzygy sequence of $M$ and an injective-hull sequence of $\Omega M$ with cokernel $M$, so $\Sigma\Omega M \cong M$ stably; dually $\Omega\Sigma M \cong M$. Hence $\Sigma = \Omega^{-1}$ is an invertible suspension. Defining distinguished triangles as the completed short exact sequences $M \to E \to N \to \Sigma M$, the axioms TR1–TR4 hold (the Frobenius-given invertibility of $\Sigma$ supplies rotation), so $\underline{\mathbf{Mod}}_R$ is triangulated. $\blacksquare$

---

# Key Takeaways

**The Frobenius condition is exactly what makes the suspension invertible — that single short exact sequence read two ways is the whole mechanism.** The deepest insight is that projective = injective lets one short exact sequence $0 \to \Omega M \to P \to M \to 0$ serve double duty: as the syzygy sequence of $M$ (kernel of a projective cover) and as the cosyzygy sequence of $\Omega M$ (cokernel of an injective hull). Without Frobenius these are different sequences in different worlds and $\Sigma, \Omega$ do not cancel. The trigger is "is the suspension invertible here?"; the reaction is "is projective = injective?", because that is precisely the condition. This is why Frobenius categories are the standard *source* of triangulated categories (Happel's theorem): self-injectivity is the algebraic incarnation of "the suspension is an equivalence", which is the definition of stability.

**Schanuel's lemma is the statement that syzygies are well-defined modulo projectives — i.e. exactly in the stable category.** The independence-of-resolution result is not an accident; Schanuel's lemma says any two projective presentations of $M$ have kernels differing by projective summands, and projectives are exactly what the stable category kills. So the syzygy $\Omega M$ is well-defined *precisely* in $\underline{\mathbf{Mod}}_R$ and nowhere else. The transferable pattern: a construction that depends on a choice "up to projective (or injective) summands" is automatically well-defined in the stable category, and Schanuel-type lemmas are the tool that quantifies the ambiguity. Whenever you see "well-defined up to projectives", read "well-defined in the stable category".

**Distinguished triangles come from short exact sequences, and the connecting map is the suspension's shadow.** The triangulated structure is built by completing each short exact sequence $0 \to M \to E \to N \to 0$ to a triangle $M \to E \to N \to \Sigma M$, with the connecting map $N \to \Sigma M$ playing the role of the topological boundary map in a cofiber sequence. This is the same mechanism that makes the derived category $D(R)$ triangulated (there the triangles come from mapping cones) and the stable homotopy category triangulated (cofiber sequences of spectra). The unifying principle: every triangulated category arises as the homotopy category of a stable model category (or Frobenius category), the shift is the suspension, and the distinguished triangles are the (co)fiber sequences. Recognising a category as the stable category of a Frobenius ring instantly equips it with all the long exact sequences and octahedral diagrams of triangulated algebra, for free.
