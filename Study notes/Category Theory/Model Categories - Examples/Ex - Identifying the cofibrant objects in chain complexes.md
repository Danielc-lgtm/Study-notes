---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Projective Model Structure on Chain Complexes"
  - "Def - Projective Module"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Chain Map and Chain Homotopy"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Work in the [[Def - Projective Model Structure on Chain Complexes|projective model structure]] on $\mathbf{Ch}(R)$. Show that a **bounded-below** chain complex $C$ is cofibrant if and only if it is degreewise [[Def - Projective Module|projective]] (each $C_n$ is a projective $R$-module). Deduce that the cofibrant replacement of a [[Def - Module|module]] $M$, regarded as the complex concentrated in degree $0$, is exactly a projective resolution $P_\bullet \xrightarrow{\sim} M$.

**Recall:**

In the projective model structure, **cofibrations** are the monomorphisms $f$ of chain maps with each cokernel $\operatorname{coker}(f_n)$ a [[Def - Projective Module|projective]] $R$-module, **fibrations** are the degreewise surjections, and **weak equivalences** are the quasi-isomorphisms.

![[Def - Cofibrant and Fibrant Objects#The Definition]]

A [[Def - Projective Module|projective module]] $P$ is a direct summand of a free module; equivalently every surjection onto $P$ splits, equivalently $\mathrm{Hom}(P, -)$ is exact. A **projective resolution** of $M$ is an exact complex $\cdots \to P_1 \to P_0 \to M \to 0$ with each $P_i$ projective; as a complex $P_\bullet$ (without the $M$) it maps quasi-isomorphically to $M$ in degree $0$.

---

# Convergent Strategy

**Problem class:** This is an "identify the (co)fibrant objects" problem, the second of the recurring targets named on [[Model Categories — Examples in Detail|the topic page]]. The routine is to unwind the definition of cofibrancy — "$0 \to C$ is a cofibration" — into a concrete property of the object, here using that the relevant cokernel is taken over the zero complex.

**Assumption pattern:** The recognisable assumption is "cofibrant", which by definition means the unique map from the initial object $0$ is a cofibration. The cokernel of $0 \to C$ in degree $n$ is just $C_n$ itself, so the projective-cokernel condition collapses to "$C_n$ is projective". The bounded-below hypothesis is what prevents the unbounded subtlety (K-projectivity) and makes the equivalence clean.

**Theorem routing:** The first half is a direct unwinding of [[Def - Projective Model Structure on Chain Complexes|the definition of cofibration]]. The second half routes through the observation that a projective resolution is a degreewise-projective complex (hence cofibrant by the first half) together with a quasi-isomorphism to $M$ — which is exactly the data of a cofibrant replacement in the sense of [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]].

**Key decision point:** The non-obvious choice is realising that the cokernel of $0 \to C$ is $C$ itself, so the abstract "projective cokernel" condition becomes the concrete "projective in each degree" — many readers expect cofibrancy to be a subtler global condition and miss that for the initial map it localises degreewise. The bounded-below hypothesis must be invoked explicitly, because in the unbounded case degreewise-projective is *not* sufficient.

---

# Legal Operations Used

1. **Operation 1 from the topic page (check a chain-complex condition one degree at a time).** Cofibrancy of $0 \to C$ is verified by computing the cokernel degree by degree, where it equals $C_n$, reducing the model-categorical condition to module-theoretic projectivity.

2. **Operation 3 from the topic page (replace a module by its projective resolution).** The deduction is exactly this operation: a projective resolution is the cofibrant replacement, justified by the first half of the problem.

---

# Hints

> [!note]- Hint 1
> What is the cokernel of the map $0 \to C$ in degree $n$? Write out the short exact sequence $0 \to 0 \to C_n \to \operatorname{coker} \to 0$.

> [!note]- Hint 2
> "Cofibrant" means "$0 \to C$ is a cofibration". Feed the degreewise cokernel from Hint 1 into the definition of cofibration in the projective model structure.

> [!note]- Hint 3
> For the deduction: a projective resolution $P_\bullet$ is degreewise projective (so cofibrant by the first half) and bounded below, and the augmentation $P_\bullet \to M$ is a quasi-isomorphism. Why does that make $P_\bullet$ a cofibrant replacement of $M$?

---

# Solution

The proof is two short unwindings. First, cofibrancy of $C$ means $0 \to C$ is a cofibration, and the cokernel of $0 \to C$ in degree $n$ is $C_n$, so the projective-cokernel condition reads "$C_n$ projective". Second, a projective resolution is then a cofibrant object weakly equivalent to $M$, which is what "cofibrant replacement" means.

**Step 1: $C$ cofibrant $\iff$ each $C_n$ is projective (bounded-below case).**

> [!note]- Derivation
> By definition, $C$ is cofibrant exactly when the unique chain map $0 \to C$ from the zero complex (the initial object of $\mathbf{Ch}(R)$) is a cofibration. In the [[Def - Projective Model Structure on Chain Complexes|projective model structure]], a chain map $f$ is a cofibration when it is a degreewise monomorphism with degreewise-[[Def - Projective Module|projective]] cokernel. For $f : 0 \to C$, the degree-$n$ map is $0 \to C_n$, which is automatically a monomorphism, and its cokernel is
> $$\operatorname{coker}(0 \to C_n) = C_n / 0 = C_n.$$
> So the condition "cokernel projective in each degree" is precisely "$C_n$ projective for every $n$". Hence, among bounded-below complexes, $C$ is cofibrant if and only if each $C_n$ is a projective $R$-module.
>
> (The bounded-below hypothesis is needed: for unbounded complexes one additionally requires K-projectivity, that $\mathrm{Hom}(C, -)$ preserve quasi-isomorphisms. For bounded-below complexes degreewise-projective already implies K-projective, so the two coincide and the clean equivalence holds.)

**Step 2: a projective resolution is a cofibrant replacement of $M$.**

> [!note]- Derivation
> Let $M$ be a module, viewed as the complex with $M$ in degree $0$ and zeros elsewhere. Choose a projective resolution
> $$\cdots \to P_2 \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \xrightarrow{\varepsilon} M \to 0,$$
> exact, with each $P_i$ projective. Let $P_\bullet$ be the complex $\cdots \to P_1 \to P_0$ (concentrated in degrees $\geq 0$, no $M$ term). It is bounded below and degreewise projective, hence **cofibrant** by Step 1.
>
> The augmentation defines a chain map $\varepsilon : P_\bullet \to M$ (here $M$ in degree $0$): in degree $0$ it is $\varepsilon : P_0 \to M$, in higher degrees the zero map into $0$. Exactness of the resolution says $H_0(P_\bullet) = P_0 / \operatorname{im} d_1 = M$ (via $\varepsilon$) and $H_n(P_\bullet) = 0$ for $n > 0$, while $H_*(M) = M$ in degree $0$. So $\varepsilon$ induces isomorphisms on all homology — it is a **quasi-isomorphism**, i.e. a weak equivalence.
>
> A cofibrant replacement of $M$ is, by definition, a cofibrant object $QM$ with a weak equivalence $QM \xrightarrow{\sim} M$. We have exhibited exactly this with $QM = P_\bullet$ and the augmentation. Hence the projective resolution *is* a cofibrant replacement of $M$.

> [!note]- Complete formal solution
> **($\Rightarrow$, Step 1)** Suppose the bounded-below complex $C$ is cofibrant, i.e. $0 \to C$ is a cofibration. In the projective model structure cofibrations are degreewise monos with degreewise-projective cokernel. In degree $n$ the map $0 \to C_n$ has cokernel $C_n$, so $C_n$ is projective. **($\Leftarrow$)** Conversely if each $C_n$ is projective then $0 \to C$ is a degreewise mono with cokernels $C_n$, all projective, so it is a cofibration and $C$ is cofibrant. (Bounded-below ensures degreewise-projective coincides with K-projective, so no further condition is needed.)
>
> **Deduction.** Given a module $M$, pick a projective resolution $\cdots \to P_1 \to P_0 \xrightarrow{\varepsilon} M \to 0$. The complex $P_\bullet = (\cdots \to P_1 \to P_0)$ is bounded below and degreewise projective, hence cofibrant by the equivalence just proved. Exactness of the resolution gives $H_0(P_\bullet) \cong M$ and $H_{n}(P_\bullet) = 0$ for $n \neq 0$, so the augmentation $\varepsilon : P_\bullet \to M$ (with $M$ in degree $0$) is a quasi-isomorphism. Thus $\varepsilon : P_\bullet \xrightarrow{\sim} M$ is a weak equivalence from a cofibrant object, i.e. a cofibrant replacement of $M$. $\blacksquare$

---

# Key Takeaways

**Cofibrancy localises degreewise for the initial map.** The single most transferable idea here is that "cofibrant" — a condition phrased through the initial object $0$ — collapses to a pointwise (degreewise) condition because the cokernel of $0 \to C$ is $C$ itself. Whenever you want to test cofibrancy in a model structure defined by "cofibrations = monos with cokernel in some nice class $\mathcal{P}$", the cofibrant objects are exactly the objects *in* $\mathcal{P}$ (computed against the initial object). This pattern recurs in every algebraically-presented model structure: in $\mathbf{Ch}(R)$ it gives complexes of projectives, and in the injective model structure the *fibrant* objects are dually the complexes of injectives. The trigger is "cofibrant object" plus "cofibration defined via cokernel"; the reaction is "compute the cokernel over the initial object and read off the class".

**Cofibrant replacement is resolution — this is the master dictionary entry.** The deduction is the concrete content of the slogan that runs the whole chapter: the homotopy-theoretic operation "replace $X$ by a cofibrant object" *is* the homological operation "resolve $M$ by projectives". Once you internalise this, every derived functor computation becomes mechanical: to derive a functor, cofibrant-replace the input (= resolve), apply the functor, take homology. The reason a single module is generally *not* cofibrant (it is not projective unless it happens to be) is exactly the reason it must be resolved before any derived functor is applied — and the failure of cofibrancy is the source of the higher Tor and Ext groups. Whenever you see "resolution" anywhere in mathematics, read "cofibrant or fibrant replacement".

**The bounded-below hypothesis is not cosmetic.** It is tempting to drop the boundedness and claim degreewise-projective equals cofibrant in general, but this is false: an unbounded complex of projectives can fail to be cofibrant, and the correct condition is K-projectivity (that $\mathrm{Hom}(C, -)$ preserves quasi-isomorphisms). The diagnostic to carry forward is that *finiteness or boundedness hypotheses in homological algebra are usually exactly the conditions that make "naive" and "homotopically correct" notions coincide*. When a clean statement about resolutions is offered without a boundedness hypothesis, suspect that the unbounded case hides a subtlety — here, the gap between degreewise-projective and K-projective, which is invisible until the complex stretches infinitely in both directions.
