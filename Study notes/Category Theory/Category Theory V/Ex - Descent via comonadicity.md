---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Barr-Beck Monadicity Theorem"
  - "Def - Monad and Comonad"
  - "Def - Module"
  - "Def - Ring"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\varphi : R \to S$ be a **faithfully flat** homomorphism of commutative [[Def - Ring|rings]]. Consider the base-change functor
$$S \otimes_R - \;:\; \mathbf{Mod}_R \longrightarrow \mathbf{Mod}_S, \qquad N \longmapsto S\otimes_R N.$$

**(a)** Show this functor is **comonadic**, i.e. it satisfies the comonadic [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]] conditions.

**(b)** Deduce **faithfully flat descent**: an $R$-module is the same data as an $S$-module $W$ equipped with **descent data** — an $S\otimes_R S$-linear isomorphism $\theta : S\otimes_R W \cong W\otimes_R S$ satisfying a cocycle condition over $S\otimes_R S\otimes_R S$.

> [!note]- Algebraic geometry background
> A **commutative ring** $R$ is a set with $+, \times$ where multiplication is commutative, associative, distributes over $+$, and has a unit $1$ (e.g. $\mathbb{Z}$, $\mathbb{R}[x]$, $\mathbb{Z}/n$). A **module** over $R$ is "a vector space over a ring": an abelian group $N$ with an $R$-action $R\times N\to N$ that is bilinear, associative, unital. The geometric picture (the **ring–geometry dictionary**) is that a commutative ring $R$ is the ring of functions on a space, its **prime spectrum** $\mathrm{Spec}\,R$ (the set of prime ideals with the Zariski topology), and a ring map $R\to S$ is a map of spaces $\mathrm{Spec}\,S \to \mathrm{Spec}\,R$ *in the opposite direction* — pulling back functions. An $R$-module is a "vector bundle / sheaf of modules" on $\mathrm{Spec}\,R$. **Base change** $S\otimes_R -$ pulls a module back along $\mathrm{Spec}\,S\to\mathrm{Spec}\,R$. A ring map is **flat** if $S\otimes_R-$ is exact (preserves injections), and **faithfully flat** if additionally it detects nonzero modules ($S\otimes_R N = 0 \Rightarrow N = 0$); geometrically $\mathrm{Spec}\,S \to \mathrm{Spec}\,R$ is a "cover." **Descent** is the principle that a sheaf/module on the base can be reconstructed from its pullback to a cover plus gluing data — the categorical engine being comonadicity.

**Recall:**

![[Thm - The Barr-Beck Monadicity Theorem#Statement]]

The **comonadic** Barr–Beck theorem: a functor $V$ is comonadic iff it has a right adjoint, is conservative, and creates equalizers of $V$-split pairs. A [[Def - Monad and Comonad|comonad]] $(G,\varepsilon,\delta)$ is the dual of a monad; its coalgebras carry $\delta$-coherent comultiplication.

---

# Convergent Strategy

**Problem class:** A "prove a descent statement via comonadicity" problem — the algebraic-geometry payoff of Barr–Beck (legal operation 6). The goal is to recognize descent as the comonadic-recognition theorem applied to base change.

**Assumption pattern:** "Faithfully flat" is the assumption to leverage: *flat* gives exactness (so base change preserves the equalizers needed), and *faithful* gives conservativity (it detects zero, hence isomorphisms). These two halves of the hypothesis map exactly onto two of the three comonadic conditions (legal operation 6).

**Theorem routing:** Route through the comonadic [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]]: check $S\otimes_R-$ has a right adjoint (restriction of scalars), is conservative (faithful flatness), and creates equalizers of split pairs (flatness preserves them). Then unwind "coalgebra for the comonad $S\otimes_R-$" into explicit descent data.

**Key decision point:** The non-obvious identification is that a **coalgebra** for the comonad $G = (S\otimes_R-)\circ(\text{restriction})$ is exactly an $S$-module with descent data. The comultiplication $\delta$ becomes the cocycle condition over $S\otimes_R S\otimes_R S$, and the counit $\varepsilon$ the normalization. Recognizing the cocycle as comonad coassociativity is the crux.

---

# Legal Operations Used

1. **Operation 6 from the topic page (dualize to a comonad for descent).** The base-change functor induces a comonad whose coalgebras are descent data.

2. **Operation 5 from the topic page (apply Barr–Beck to recognize algebras), comonadic form.** We verify the three comonadic conditions, mapping faithful flatness onto conservativity and flatness onto creation of split equalizers.

---

# Hints

> [!note]- Hint 1
> The base-change functor $S\otimes_R-$ has a right adjoint: restriction of scalars $\mathrm{Res} : \mathbf{Mod}_S \to \mathbf{Mod}_R$ (an $S$-module is an $R$-module via $\varphi$). This adjunction $(S\otimes_R-) \dashv \mathrm{Res}$ induces a comonad on $\mathbf{Mod}_S$.

> [!note]- Hint 2
> Conservativity = faithfulness in the relevant sense: if $S\otimes_R f$ is an isomorphism then $f$ is, because faithful flatness detects the zero of $\ker f$ and $\mathrm{coker}\,f$ (a map is iso iff its kernel and cokernel vanish, and $S\otimes_R-$ detects vanishing).

> [!note]- Hint 3
> Flatness makes $S\otimes_R-$ exact, so it preserves equalizers (= kernels of differences); creation of equalizers of split pairs then follows. This is the third comonadic condition.

> [!note]- Hint 4
> A coalgebra for the comonad $G = S\otimes_R\mathrm{Res}(-)$ on $\mathbf{Mod}_S$ is an $S$-module $W$ with a coaction $W \to S\otimes_R W$ — equivalently the isomorphism $\theta : S\otimes_R W \cong W\otimes_R S$; coassociativity of $\delta$ is the cocycle condition over $S\otimes_R S\otimes_R S$, and counitality is the normalization over $S$.

---

# Solution

The plan: identify the adjunction $(S\otimes_R-)\dashv\mathrm{Res}$ and its comonad (Step 1); verify the three comonadic Barr–Beck conditions, mapping flat $\to$ exactness $\to$ creation of equalizers and faithful $\to$ conservativity (Steps 2–3); unwind a coalgebra into descent data with the cocycle condition (Step 4). The crux is reading the comonad coassociativity as the cocycle.

**Step 1: The base-change comonad.**

> [!note]- Derivation
> Base change $S\otimes_R- : \mathbf{Mod}_R\to\mathbf{Mod}_S$ is left adjoint to restriction of scalars $\mathrm{Res} : \mathbf{Mod}_S\to\mathbf{Mod}_R$: a map $S\otimes_R N\to W$ of $S$-modules corresponds to a map $N\to\mathrm{Res}\,W$ of $R$-modules (tensor–restriction adjunction). By [[Thm - Every Adjunction Gives a Monad|the adjunction–comonad construction]], this induces a **comonad** $G = (S\otimes_R-)\circ\mathrm{Res}$ on $\mathbf{Mod}_S$, with counit $\varepsilon_W : S\otimes_R W \to W$ (multiplication $s\otimes w\mapsto sw$) and comultiplication $\delta_W : S\otimes_R W \to S\otimes_R S\otimes_R W$.

**Step 2: Conservativity from faithfulness.**

> [!note]- Derivation
> Suppose $f : N \to N'$ in $\mathbf{Mod}_R$ has $S\otimes_R f$ an isomorphism. A map is an isomorphism iff $\ker f = 0$ and $\mathrm{coker}\,f = 0$. Since $S\otimes_R-$ is flat (exact), $S\otimes_R\ker f = \ker(S\otimes_R f) = 0$ and $S\otimes_R\mathrm{coker}\,f = \mathrm{coker}(S\otimes_R f) = 0$. By **faithful** flatness, $S\otimes_R M = 0 \Rightarrow M = 0$, so $\ker f = 0$ and $\mathrm{coker}\,f = 0$, hence $f$ is an isomorphism. Thus base change is conservative.

**Step 3: Creation of equalizers of split pairs from flatness.**

> [!note]- Derivation
> Flatness means $S\otimes_R-$ is exact, hence preserves all finite limits, in particular equalizers (kernels of differences). For a $V$-split pair (where $V = S\otimes_R-$), the equalizer exists in $\mathbf{Mod}_R$ (modules are complete), is preserved by $V$ (flatness), and is reflected because the split makes the equalizer absolute. So $V$ creates equalizers of $V$-split pairs. Combined with Steps 1–2, the comonadic [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]] conditions hold, so $S\otimes_R-$ is **comonadic**: $\mathbf{Mod}_R \simeq \mathrm{CoAlg}_G(\mathbf{Mod}_S)$.

**Step 4: Coalgebras are descent data.**

> [!note]- Derivation
> A $G$-coalgebra is an $S$-module $W$ with a coaction $\gamma : W \to G W = S\otimes_R W$ satisfying counitality ($\varepsilon_W\circ\gamma = 1$) and coassociativity ($\delta_W\circ\gamma = G\gamma\circ\gamma$). Repackage the coaction as an $S\otimes_R S$-linear isomorphism
> $$\theta : S\otimes_R W \xrightarrow{\ \sim\ } W\otimes_R S$$
> (the "transition isomorphism over the two projections $S\otimes_R S \rightrightarrows$"). Counitality says $\theta$ restricts to the identity over the diagonal $S$ (normalization). Coassociativity of $\delta$ becomes the **cocycle condition**: over $S\otimes_R S\otimes_R S$,
> $$\theta_{13} = \theta_{23}\circ\theta_{12},$$
> where $\theta_{ij}$ is $\theta$ applied in the $i,j$ tensor slots. This is exactly the classical descent datum. By comonadicity, $\mathbf{Mod}_R \simeq \{(W,\theta) : \theta \text{ descent data}\}$: an $R$-module is an $S$-module with descent data. This is **faithfully flat descent**.

> [!note]- Complete formal solution
> Base change $S\otimes_R-$ is left adjoint to restriction of scalars, inducing a comonad $G$ on $\mathbf{Mod}_S$. It is conservative: flatness makes it exact, so it preserves $\ker$ and $\mathrm{coker}$, and faithfulness detects their vanishing, so $S\otimes_R f$ iso $\Rightarrow f$ iso. It creates equalizers of split pairs: flatness preserves equalizers and the split makes them absolute. By comonadic Barr–Beck, $S\otimes_R-$ is comonadic, so $\mathbf{Mod}_R \simeq \mathrm{CoAlg}_G$. A $G$-coalgebra is an $S$-module $W$ with coaction $\gamma : W\to S\otimes_R W$, equivalently a transition isomorphism $\theta : S\otimes_R W\cong W\otimes_R S$ with $\theta$ identity over the diagonal (counitality) and $\theta_{13} = \theta_{23}\theta_{12}$ over $S^{\otimes 3}$ (coassociativity = cocycle). Hence an $R$-module = an $S$-module with descent data: faithfully flat descent. $\blacksquare$

> [!tip] The geometric reading
> Over the cover $\mathrm{Spec}\,S \to \mathrm{Spec}\,R$, an $R$-module (a sheaf on the base) is the same as an $S$-module (a sheaf on the cover) plus a gluing isomorphism $\theta$ on the double overlap $\mathrm{Spec}(S\otimes_R S)$ that is consistent on the triple overlap $\mathrm{Spec}(S\otimes_R S\otimes_R S)$. This is the Čech-style gluing of sheaves, and the cocycle condition is the consistency of the gluing — exactly comonad coassociativity.

---

# Key Takeaways

**Descent is comonadicity; the cocycle is comonad coassociativity.** The single most important identification is that "an object on the base = an object on the cover plus descent data satisfying a cocycle condition" is *literally* the statement that a coalgebra for the base-change comonad is the descent datum, with the cocycle condition being the comonad's coassociativity axiom and the normalization being its counit axiom. Once you see this, every descent theorem — for modules, for quasi-coherent sheaves, for schemes — is an instance of comonadic Barr–Beck, and you never have to re-derive the cocycle condition: it is forced by coassociativity. The trigger is "reconstruct a global object from local data on a cover"; the reaction is "this is comonadicity of the pullback functor."

**The two halves of "faithfully flat" map onto the two non-trivial Barr–Beck conditions.** Faithful flatness is not a single opaque hypothesis: *flat* gives exactness of base change, which supplies the creation of equalizers (the third comonadic condition), while *faithful* gives that base change detects vanishing, which supplies conservativity (the second condition). Recognizing this decomposition tells you exactly *why* faithful flatness is the right hypothesis for descent — it is precisely the conjunction of the two conditions Barr–Beck needs (the right adjoint, restriction of scalars, is automatic). This is the diagnostic for spotting descent situations: look for a pullback functor that is exact (flat) and detects isomorphisms (faithful).

**Comonads package observational/local structure, dual to monads' algebraic structure.** This exercise is the canonical illustration of why comonads matter despite being less famous than monads. Where a monad's algebras are objects with *operations* (group multiplication, vector addition), a comonad's coalgebras are objects with *gluing or observation* data (descent isomorphisms, contexts, streams). The base-change comonad's coalgebras are sheaves-with-gluing, and the comultiplication encodes how the gluing propagates across overlaps. The transferable lesson is that whenever a problem is about *assembling* a global object from local pieces — rather than *building* an object from generators — the right tool is a comonad and the right recognition theorem is comonadic Barr–Beck. See [[Ex - Which forgetful functors are monadic]] for the monadic (algebraic) side of the same theorem.
