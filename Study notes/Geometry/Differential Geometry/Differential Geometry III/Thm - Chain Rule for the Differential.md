---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - The Differential of a Smooth Map"
  - "Def - Smooth Map between Manifolds"
  - "Def - The Tangent Space"
tags: [geometry, differential-geometry]
---

# Notation

$M$, $N$, $P$ are smooth manifolds, $F : M \to N$ and $G : N \to P$ are smooth maps, and $p \in M$. The differentials are $dF_{p} : T_{p}M \to T_{F(p)}N$ and $dG_{F(p)} : T_{F(p)}N \to T_{G(F(p))}P$, see [[Def - The Differential of a Smooth Map]]. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Statement

> **Theorem ([[Thm - The Chain Rule|Chain Rule]] for the Differential, Functoriality of $T_{p}$).** Let $M$, $N$, $P$ be smooth manifolds, $F : M \to N$ and $G : N \to P$ smooth maps, and $p \in M$. Then
> $$d(G \circ F)_{p} \;=\; dG_{F(p)} \circ dF_{p} \;\;\text{ as linear maps } T_{p}M \to T_{G(F(p))}P.$$
> Furthermore, $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$ for the identity map on $M$.

> **Corollary 1 (Diffeomorphism induces isomorphism).** If $F : M \to N$ is a [[Def - Diffeomorphism|diffeomorphism]], then $dF_{p} : T_{p}M \to T_{F(p)}N$ is a vector-space isomorphism for every $p \in M$, with inverse $(dF_{p})^{-1} = d(F^{-1})_{F(p)}$.
>
> **Corollary 2 (Functoriality).** The assignment $(M, p) \mapsto T_{p}M$ on objects, $F \mapsto dF_{p}$ on morphisms is a covariant functor from the category $\mathrm{Diff}_{*}$ of pointed smooth manifolds to the category $\mathrm{Vec}_{\mathbb{R}}$ of real vector spaces.

The chain rule and the identity rule are *the* functoriality axioms — they package the categorical content of the tangent-space construction.

---

# Motivation

The motivation is to certify that the manifold differential behaves correctly under composition — exactly the way the total derivative does in multivariate calculus, exactly the way pre-composition does in algebra. This is what makes the differential a sensible construction.

Without the chain rule, the differential would be a parochial construction — useful for one map at a time but giving no information about how maps combine. With the chain rule, complex computations can be broken into simple pieces: $d(G \circ F)_{p}$ is computed by computing $dF_{p}$ and $dG_{F(p)}$ separately and composing. This is the routine workflow of differential geometry.

The corollary about [[Def - Diffeomorphism|diffeomorphisms]] is the practical payoff: any diffeomorphism's differential is automatically an isomorphism, with no extra work. This is what licenses the use of charts as "tangent-space [[Def - Isomorphism|isomorphisms]]" and underlies the proof of [[Thm - Dimension of the Tangent Space]].

The functoriality content — that $T_{p}$ is a functor — is the categorical packaging of the chain rule and identity rule. It says the tangent-space construction is *natural*: it commutes with composition, so any computation done in one composition order matches the computation in another. This naturality is the technical heart of coordinate-independence in differential geometry.

---

# Sources and Targets

**Sources (Input Broadening).**

The precondition is "two smooth maps composable". This appears in essentially every computation.

The first source is **a composition of smooth maps appearing in a problem**. Whenever a problem involves $G \circ F$ — and these arise everywhere, from change-of-coordinates ($\psi \circ \varphi^{-1}$) to evaluation along a curve ($F \circ \gamma$) — the chain rule lets you replace the differential of the composition by the product of differentials. Example: in [[Ex - Computing the Differential in Local Coordinates]], the coordinate representative $\hat{F} = \psi \circ F \circ \varphi^{-1}$ is a composition of three maps, and its differential is the product of three Jacobians — which collapses to the Jacobian of the middle map in the right coordinates.

The second source is **the diffeomorphism property of charts**. Charts $\varphi : U \to \hat{U}$ are diffeomorphisms (a standing assumption of the definition); by the corollary, their differentials $d\varphi_{p}$ are vector-space isomorphisms. This is the input that makes "express in coordinates" a well-defined operation on tangent vectors — the chart provides an isomorphism $T_{p}M \to \mathbb{R}^{n}$. Example: the proof of [[Thm - Dimension of the Tangent Space]] uses precisely this — $d\varphi_{p}$ is an isomorphism, so $\dim T_{p}M = \dim T_{\varphi(p)}\hat{U} = n$.

The third source is **a velocity computation that needs to be transferred between manifolds**. If $\gamma : J \to M$ is a smooth curve and $F : M \to N$, the velocity of the composite $F \circ \gamma$ is computed via $(F \circ \gamma)'(t_{0}) = dF_{\gamma(t_{0})}(\gamma'(t_{0}))$ — this is Proposition 3.24 of Lee, derived directly from the chain rule applied to the composition $J \to M \to N$. The source $B$ is "a curve and a smooth map"; the bridge to the chain rule is one step. Example: see [[Def - Velocity of a Curve]] property 3.

**Targets (Output Amplification).**

The conclusion is $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$. Combined with various properties this gives:

Target 1: **combined with linear algebra invariants, the chain rule controls rank, determinant, and invertibility**. One has $\operatorname{rank}d(G\circ F)_p\leq\min(\operatorname{rank}dF_p,\operatorname{rank}dG_{F(p)})$. When all tangent spaces have the same finite dimension, $\det d(G\circ F)_p=(\det dG_{F(p)})(\det dF_p)$, so a composition is infinitesimally invertible exactly when both factors are. There is no analogous multiplicative formula for trace or characteristic polynomial; those are not functorial under composition.

Target 2: **combined with surjectivity/injectivity, the chain rule classifies submersions and immersions**. If $G \circ F$ has surjective differential at $p$, then so does $G$ at $F(p)$ — surjectivity is preserved by left-divisor in composition. If $G \circ F$ has injective differential, then so does $F$ at $p$. These input/output recognitions are the basis of submanifold theory in [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

Target 3: **combined with the diffeomorphism corollary, the chain rule implies dimension is a diffeomorphism invariant**. If $F$ is a diffeomorphism, $dF_{p}$ is an isomorphism, so $\dim T_{p}M = \dim T_{F(p)}N$, hence $\dim M = \dim N$. This is the theorem that diffeomorphic manifolds have the same dimension — see [[Ex - The Differential of a Diffeomorphism is an Isomorphism]].

Target 4: **combined with the global differential $dF : TM \to TN$, the chain rule gives functoriality at the bundle level**. The global chain rule $d(G \circ F) = dG \circ dF : TM \to TP$ promotes the chain rule for differentials at a point to a chain rule for the smooth maps between tangent bundles. This is the manifold version of the Jacobian product rule, applied globally.

---

# Why Is It True

The chain rule is true because the differential is defined by *pre-composition*: $(dF_{p}(v))(f) = v(f \circ F)$. And pre-composition is *associative*: $(f \circ G) \circ F = f \circ (G \circ F)$. The chain rule is the conversion of this associativity into a statement about linear maps.

**The bolded one-liner mechanism summary: the chain rule for the differential is the associativity of function composition, repackaged into the language of derivations and pre-composition.**

Here is the picture. A tangent vector $v$ at $p$ acts on a function $h$ on $N$ by pulling $h$ back to $M$ via $F$ and then evaluating $v$ at $p$ on the pulled-back function: $(dF_{p}(v))(h) = v(h \circ F)$. Now $G \circ F$ is a map $M \to P$, and pulling back a function $f$ on $P$ via $G \circ F$ is the same as pulling it back via $F$ after first pulling it back via $G$: $f \circ (G \circ F) = (f \circ G) \circ F$. Apply $v$:
$$(d(G \circ F)_{p}(v))(f) = v(f \circ (G \circ F)) = v((f \circ G) \circ F) = (dF_{p}(v))(f \circ G) = (dG_{F(p)} \circ dF_{p}(v))(f).$$
This is the chain rule, in one line, with each step a definition unfolding or associativity.

The identity rule is even simpler: $(d(\mathrm{id}_{M})_{p}(v))(f) = v(f \circ \mathrm{id}) = v(f)$, so $d(\mathrm{id})_{p} = \mathrm{id}_{T_{p}M}$.

The two rules combine to say that the tangent-space construction is a *functor* — a structure-preserving map from one category to another. The functor sends each pointed manifold to its tangent space, and each smooth map to its differential, with composition and identities preserved. This is the categorical statement of the chain rule.

In coordinates, the chain rule for differentials becomes the chain rule for Jacobians: if $\hat{F} = \psi \circ F \circ \varphi^{-1}$ and $\hat{G} = \chi \circ G \circ \psi^{-1}$ are the coordinate representatives, then $\widehat{G \circ F} = \chi \circ G \circ F \circ \varphi^{-1} = \hat{G} \circ \hat{F}$, and the Jacobian product rule gives the matrix identity $D(\widehat{G \circ F}) = D\hat{G} \cdot D\hat{F}$ at the appropriate points. This is the multivariate chain rule, with the manifold chain rule certifying that it is coordinate-independent.

---

# What Makes This Hard

The proof is straightforward — one line of associativity unfolding. The conceptual difficulty is recognizing that *this is the chain rule from multivariate calculus, made coordinate-free*. People who have studied multivariate calculus often expect the chain rule to involve Jacobian matrices and partial derivatives, and the manifold chain rule looks too abstract to be the same thing.

The other subtlety is the corollary about [[Def - Diffeomorphism|diffeomorphisms]]: that $dF_{p}$ has $d(F^{-1})_{F(p)}$ as inverse. This is a one-line consequence of the chain rule applied to $F \circ F^{-1} = \mathrm{id}$, but it is the corollary used most often in practice — and the proof requires recognizing that the identity map's differential is the identity (which is a separate, easy lemma but essential).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Unwind the precomposition definition of the differential. The chain rule for differentials is the chain rule for pre-composition, which is the associativity of function composition. Three lines, each a tautology.

**Subgoal decomposition:**

1. **State the precomposition definition.** $(dF_{p}(v))(f) = v(f \circ F)$ for $v \in T_{p}M$, $f \in C^{\infty}(N)$.
   - *Hint:* This is just the definition.
   - *Why needed:* Sets up the algebra.

2. **Compute $(d(G \circ F)_{p}(v))(f)$ using the definition.** $(d(G \circ F)_{p}(v))(f) = v(f \circ (G \circ F))$.
   - *Hint:* Apply the definition with $F$ replaced by $G \circ F$.
   - *Why needed:* The left-hand side of the chain rule.

3. **Compute $(dG_{F(p)} \circ dF_{p}(v))(f)$ using the definition twice.** $(dG_{F(p)} \circ dF_{p}(v))(f) = (dG_{F(p)})(dF_{p}(v))(f) = (dF_{p}(v))(f \circ G) = v((f \circ G) \circ F)$.
   - *Hint:* Apply the definition twice — once for $dG$, once for $dF$.
   - *Why needed:* The right-hand side of the chain rule.

4. **Use associativity of composition.** $f \circ (G \circ F) = (f \circ G) \circ F$ — this is the associativity of function composition.
   - *Hint:* This is a tautology.
   - *Why needed:* Connects subgoals 2 and 3.

5. **The identity rule.** $(d(\mathrm{id}_{M})_{p}(v))(f) = v(f \circ \mathrm{id}_{M}) = v(f)$.
   - *Hint:* Composing with identity does nothing.
   - *Why needed:* The second functor axiom.

6. **Derive the diffeomorphism corollary.** $F \circ F^{-1} = \mathrm{id}_{N}$, $F^{-1} \circ F = \mathrm{id}_{M}$. Apply the chain rule and identity rule.
   - *Hint:* The chain rule gives $dF_{p} \circ d(F^{-1})_{F(p)} = \mathrm{id}_{T_{F(p)}N}$ and applying the chain rule to $F^{-1}\circ F=\operatorname{id}_M$ gives the reverse composite $d(F^{-1})_{F(p)}\circ dF_p=\operatorname{id}_{T_pM}$.
   - *Why needed:* The most-used corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: The differential of the identity is the identity
> **Statement:** For any smooth manifold $M$ and any $p \in M$, $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$.
>
> **Hint:** Apply the precomposition definition; composition with the identity is the identity.
>
> **Why needed:** This is one of the two functor axioms — preservation of identities. Without it, the functorial structure of $T_{p}$ would be incomplete, and the diffeomorphism corollary would not work.
>
> > [!note]- Full proof
> > For $v \in T_{p}M$ and $f \in C^{\infty}(M)$:
> > $(d(\mathrm{id}_{M})_{p}(v))(f) = v(f \circ \mathrm{id}_{M}) = v(f)$.
> > Hence $d(\mathrm{id}_{M})_{p}(v) = v$ as derivations, i.e., $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$.

> [!note]- Lemma 2: Associativity of composition
> **Statement:** For smooth maps $F : M \to N$, $G : N \to P$, and a smooth function $f \in C^{\infty}(P)$,
> $$f \circ (G \circ F) = (f \circ G) \circ F.$$
>
> **Hint:** Apply both sides to a point $q \in M$.
>
> **Why needed:** This is the associativity of composition, the algebraic input for the chain rule.
>
> > [!note]- Full proof
> > For any $q \in M$:
> > $(f \circ (G \circ F))(q) = f((G \circ F)(q)) = f(G(F(q)))$
> > $((f \circ G) \circ F)(q) = (f \circ G)(F(q)) = f(G(F(q)))$.
> > The two equal everywhere, so the maps are equal as functions $M \to \mathbb{R}$.

> [!note]- Lemma 3: The chain rule for the differential
> **Statement:** $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$.
>
> **Hint:** Apply the precomposition definition to both sides and use Lemma 2.
>
> **Why needed:** The main theorem.
>
> > [!note]- Full proof
> > For $v \in T_{p}M$ and $f \in C^{\infty}(P)$:
> >
> > Left side: $(d(G \circ F)_{p}(v))(f) = v(f \circ (G \circ F))$ by the precomposition definition.
> >
> > Right side: $(dG_{F(p)} \circ dF_{p}(v))(f) = (dG_{F(p)}(dF_{p}(v)))(f)$
> > $= (dF_{p}(v))(f \circ G)$ by the precomposition definition for $dG_{F(p)}$
> > $= v((f \circ G) \circ F)$ by the precomposition definition for $dF_{p}$.
> >
> > By Lemma 2, $f \circ (G \circ F) = (f \circ G) \circ F$, so the two sides are equal: $v(f \circ (G \circ F)) = v((f \circ G) \circ F)$.
> >
> > This holds for every $f \in C^{\infty}(P)$, so $d(G \circ F)_{p}(v) = dG_{F(p)} \circ dF_{p}(v)$ as derivations, for every $v \in T_{p}M$. Hence $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ as linear maps.

> [!note]- Lemma 4: Diffeomorphism corollary
> **Statement:** If $F : M \to N$ is a diffeomorphism, then $dF_{p}$ is a vector-space isomorphism with $(dF_{p})^{-1} = d(F^{-1})_{F(p)}$.
>
> **Hint:** Apply the chain rule to $F \circ F^{-1} = \mathrm{id}_{N}$ and $F^{-1} \circ F = \mathrm{id}_{M}$, then use Lemma 1.
>
> **Why needed:** The most operationally useful corollary — it lets every diffeomorphism transport tangent vectors.
>
> > [!note]- Full proof
> > Since $F$ is a diffeomorphism, $F^{-1}$ is smooth and $F \circ F^{-1} = \mathrm{id}_{N}$, $F^{-1} \circ F = \mathrm{id}_{M}$.
> >
> > By Lemma 3, $d(F \circ F^{-1})_{F(p)} = dF_{p} \circ d(F^{-1})_{F(p)}$. By Lemma 1, $d(F \circ F^{-1})_{F(p)} = d(\mathrm{id}_{N})_{F(p)} = \mathrm{id}_{T_{F(p)}N}$. So $dF_{p} \circ d(F^{-1})_{F(p)} = \mathrm{id}_{T_{F(p)}N}$.
> >
> > Applying the chain rule separately to $F^{-1} \circ F = \mathrm{id}_{M}$ gives $d(F^{-1})_{F(p)} \circ dF_{p} = \mathrm{id}_{T_{p}M}$.
> >
> > These two identities certify that $dF_{p}$ has the two-sided inverse $d(F^{-1})_{F(p)}$, hence $dF_{p}$ is a vector-space isomorphism with the stated inverse.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $F : M \to N$ and $G : N \to P$ be smooth maps between smooth manifolds, and $p \in M$. Then $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$, and $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$.
>
> *Proof.* The chain rule is Lemma 3 (above). The identity rule is Lemma 1.
>
> *Proof of Corollary 1.* If $F$ is a diffeomorphism, Lemma 4 shows $dF_{p}$ is a vector-space isomorphism with the stated inverse. $\qquad\blacksquare$
>
> *Proof of Corollary 2 (Functoriality).* The assignment $(M, p) \mapsto T_{p}M$ on objects and $F \mapsto dF_{p}$ on morphisms satisfies the two functor axioms: $d(\mathrm{id})_{p} = \mathrm{id}$ (Lemma 1) and $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ (Lemma 3). Hence it is a covariant functor $T_{p} : \mathrm{Diff}_{*} \to \mathrm{Vec}_{\mathbb{R}}$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Multivariate analysis — the chain rule for Jacobians.** In multivariate calculus, the chain rule states $D(g \circ f)_{x} = Dg_{f(x)} \cdot Df_{x}$ as a product of Jacobian matrices. This is the coordinate version of the manifold chain rule applied to maps between open subsets of Euclidean spaces. The manifold chain rule certifies that this matrix identity is *coordinate-independent* — under different chart pairs, the Jacobians change but their product remains the matrix of the same linear map.

**Category theory — every covariant functor satisfies the chain rule.** The functor $T_{p}$ is one of many functors arising in differential geometry: the cotangent functor $T^{*}_{p}$ (contravariant), the Lie algebra functor on Lie [[Def - Group|groups]], the de Rham cohomology functor on smooth manifolds, the singular cohomology functor on topological spaces. Each of these satisfies a chain rule of its own type, all instances of the same category-theoretic functoriality axiom. Recognizing the chain rule as functoriality makes its appearance in many fields a single phenomenon.

**Lie theory — the chain rule and the Lie [[Def - Group|group]] homomorphism.** For a Lie group homomorphism $\phi : G \to H$, the differential $d\phi_{e} : \mathfrak{g} \to \mathfrak{h}$ at the identity is a Lie algebra homomorphism, *and* the composition rule $d(\phi \circ \psi)_{e} = d\phi_{e} \circ d\psi_{e}$ matches the corresponding rule for Lie algebra [[Def - Homomorphism|homomorphisms]]. The chain rule is what makes the Lie group $\to$ Lie algebra construction functorial. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

**Differential equations — composing flows.** If $\Phi_{t}^{X}$ and $\Phi_{s}^{Y}$ are the flows of vector fields $X$ and $Y$ respectively, the composition $\Phi_{t}^{X} \circ \Phi_{s}^{Y}$ produces a curve in $M$ whose velocity satisfies a non-trivial relation — the **Baker-Campbell-Hausdorff formula** at the infinitesimal level. The chain rule applied to flow compositions is one input. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]].

---

# Bridges

- **Functoriality is the categorical packaging of the chain rule.** The chain rule and identity rule are *exactly* the two axioms required for a covariant functor. By stating them together, we recognize the tangent-space construction as a functor from one category (pointed smooth manifolds) to another (vector spaces). This perspective is the cleanest organizing principle for differential geometry.

- **The chain rule is the basis for the rank theorem.** If $F$ has constant rank $r$ at every point of an open subset $U \subseteq M$, the rank theorem gives a local normal form $\hat{F}(x) = (x^{1}, \dots, x^{r}, 0, \dots, 0)$ in suitable charts. The proof factors $F$ as $\psi^{-1} \circ \hat{F} \circ \varphi$ where $\varphi$ and $\psi$ are diffeomorphisms (charts) and uses the chain rule to convert this factorization into a statement about $dF$. See [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

- **The chain rule for velocities (Lee 3.24) is a direct application.** For a curve $\gamma$ and a smooth map $F$, $(F \circ \gamma)'(t_{0}) = dF_{\gamma(t_{0})}(\gamma'(t_{0}))$. This is the chain rule applied to the composition $J \to M \to N$, with the velocity of $\gamma$ being $d\gamma(d/dt|_{t_{0}})$ and the velocity of $F \circ \gamma$ being $d(F \circ \gamma)(d/dt|_{t_{0}}) = dF \circ d\gamma(d/dt|_{t_{0}})$. The chain rule is the rule that "velocities transform under smooth maps via the differential". See [[Def - Velocity of a Curve]].

- **The chain rule and the global differential.** Globally, $dF : TM \to TN$ is the union of the $dF_{p}$ over $p \in M$. The chain rule $d(G \circ F) = dG \circ dF$ holds globally (Corollary 3.22(a) of Lee) — this is the fibrewise chain rule assembled over the base. The global statement is the assertion that the tangent functor $T : \mathrm{Diff} \to \mathrm{Diff}$ on smooth manifolds preserves composition.

---

# Unlocked by This

> [!tip] Functoriality of $T_{p}$ and Naturality *(from Differential Geometry)*
> The chain rule + identity rule together say $T_{p}$ is a covariant functor from $\mathrm{Diff}_{*}$ to $\mathrm{Vec}_{\mathbb{R}}$. This functorial structure is what guarantees coordinate-independence of every construction built from $T_{p}$. See [[Def - The Tangent Space]] for the functorial framing.

> [!tip] The Rank Theorem *(from Differential Geometry)*
> The rank theorem gives a local normal form for smooth maps of constant rank, using the chain rule to factor any constant-rank map through coordinate-change diffeomorphisms. The conclusions about immersions, submersions, and embeddings all follow. See [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

> [!tip] Smoothness of the Global Differential $dF : TM \to TN$ *(from Differential Geometry)*
> The chain rule (in the form of Corollary 3.22(a) of Lee) extends to a global chain rule on tangent bundles: $d(G \circ F) = dG \circ dF$ as smooth maps $TM \to TP$. This globalization makes the tangent functor $T : \mathrm{Diff} \to \mathrm{Diff}$ — sending $M$ to $TM$ and $F$ to $dF$ — a covariant functor on the category of smooth manifolds. See [[Thm - The Tangent Bundle is a Smooth Manifold]].

> [!tip] Lie Algebra Homomorphisms from Lie Group Homomorphisms *(from Lie Theory)*
> For a Lie group homomorphism $\phi : G \to H$, the differential at the identity $d\phi_{e} : \mathfrak{g} \to \mathfrak{h}$ is a Lie algebra homomorphism. The fact that compositions of Lie group homomorphisms produce compositions of Lie algebra homomorphisms is the chain rule applied at the identity, certifying that the Lie group $\to$ Lie algebra construction is functorial. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].
