---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Weak and Lax Monoidal Functor"
  - "Def - Monoid in a Monoidal Category"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $(\mathcal{D}, \boxtimes, J)$ be a [[Def - Monoidal Category|monoidal category]] and let $\mathbf{1}$ denote the **terminal monoidal category**: one object $\ast$, one morphism $1_\ast$, with $\ast\boxtimes\ast = \ast$ (the trivial monoidal structure).

(a) Show that a [[Def - Weak and Lax Monoidal Functor|lax monoidal functor]] $F : \mathbf{1}\to\mathcal{D}$ is the same thing as a [[Def - Monoid in a Monoidal Category|monoid]] $(M,\mu,\eta)$ in $\mathcal{D}$: the object is $M = F(\ast)$, the multiplication is the tensor comparison $\varphi$, and the unit is the unit comparison $\varphi_0$.

(b) Identify what the lax coherence axioms (associativity, left and right unit) become under this correspondence, and confirm they are exactly the monoid axioms.

(c) Deduce the dual statement: an **oplax** monoidal functor $\mathbf{1}\to\mathcal{D}$ is a **comonoid** in $\mathcal{D}$. Why is "lax" (not "weak/strong") the correct level for this correspondence?

**Recall:**

A [[Def - Monoid in a Monoidal Category|monoid]] in $(\mathcal{D},\boxtimes,J)$ is an object $M$ with $\mu : M\boxtimes M\to M$ and $\eta : J\to M$ satisfying associativity $\mu\circ(\mu\boxtimes 1) = \mu\circ(1\boxtimes\mu)$ (up to the associator) and unit $\mu\circ(\eta\boxtimes 1) = \lambda = \mu\circ(1\boxtimes\eta)$ (up to the unitors):

![[Def - Monoid in a Monoidal Category#The Definition]]

A [[Def - Weak and Lax Monoidal Functor|lax monoidal functor]] $(F,\varphi,\varphi_0):\mathcal{C}\to\mathcal{D}$ has a tensor comparison $\varphi_{A,B}:FA\boxtimes FB\to F(A\otimes B)$ and unit comparison $\varphi_0:J\to FI$, subject to associativity and unit coherence.

---

# Convergent Strategy

**Problem class:** This is a *[[Def - Dimension|dimension]]-shift identification* problem (topic-page target four): recognising one structure (a monoid) as a degenerate instance of another (a functor out of a point). The technique is to feed the smallest possible source category into the general definition and read off what survives.

**Assumption pattern:** The source $\mathbf{1}$ has exactly one object and one morphism, so a functor $F:\mathbf{1}\to\mathcal{D}$ carries no information except the single object $M=F(\ast)$. The lax structure $\varphi, \varphi_0$ then has nowhere to vary — there is only one instance of each — so they collapse to two specific morphisms $M\boxtimes M\to M$ and $J\to M$. Recognising that "functor from a point" $=$ "an object" and "lax structure on it" $=$ "multiplication and unit" is the entire unlock.

**Theorem routing:** The proof routes straight through the [[Def - Weak and Lax Monoidal Functor|definition of a lax monoidal functor]], specialized to source $\mathbf{1}$: the tensor comparison $\varphi_{\ast,\ast}:F\ast\boxtimes F\ast\to F(\ast\boxtimes\ast)=F\ast$ becomes $\mu:M\boxtimes M\to M$, the unit comparison $\varphi_0:J\to F\ast$ becomes $\eta:J\to M$, and the three lax coherence diagrams become the three [[Def - Monoid in a Monoidal Category|monoid]] axioms.

**Key decision point:** The non-obvious point is *why lax and not weak*. If we demanded $\varphi$ be an isomorphism (the weak/strong level), then $\mu$ would have to be invertible — but a monoid's multiplication is almost never invertible (the multiplication on $k[x]$, on a [[Def - Group|group]] algebra, on the natural numbers, is not). So insisting on weak would exclude essentially every interesting monoid. The correct level is lax precisely *because* multiplication is allowed to be non-invertible, and choosing the wrong level is the natural error.

---

# Legal Operations Used

1. **Operation 7 from the topic page (restrict to one object to descend the periodic table).** Taking the source to be the one-object category $\mathbf{1}$ is the exact move that turns "a functor with monoidal structure" into "an object with a multiplication" — the bottom row of the periodic table, where a monoid is a one-object category internalized.

2. **The lax-transports-algebra principle (operation reading of [[Def - Weak and Lax Monoidal Functor|lax monoidal functors]]).** We use that the tensor comparison $\varphi$ of a lax functor is precisely a "multiplication-carrying" datum, which here *is* the monoid multiplication.

---

# Hints

> [!note]- Hint 1
> A functor $F:\mathbf{1}\to\mathcal{D}$ is determined by a single object $M:=F(\ast)$ (it must send the only morphism $1_\ast$ to $1_M$). So the only data in $F$ is $M$.

> [!note]- Hint 2
> The lax structure adds $\varphi_{\ast,\ast}:F(\ast)\boxtimes F(\ast)\to F(\ast\boxtimes\ast)$ and $\varphi_0:J\to F(\ast)$. Since $\ast\boxtimes\ast=\ast$, the first is a map $M\boxtimes M\to M$, and the second is $J\to M$. Name them $\mu$ and $\eta$.

> [!note]- Hint 3
> Write out the lax associativity coherence axiom with all objects equal to $\ast$. Every $F$ of an associator/unitor in $\mathbf{1}$ is an identity (the only morphism), so the axiom reduces to a diagram entirely in $\mathcal{D}$ relating $\mu\circ(\mu\boxtimes 1)$ and $\mu\circ(1\boxtimes\mu)$ — the monoid associativity.

> [!note]- Hint 4
> For (c), dualize: reverse the comparison arrows to get $\psi:M\to M\boxtimes M$ and $\psi_0:M\to J$, which are a comultiplication and counit. For "why lax": ask whether the multiplication of, say, the monoid $(\mathbb{N},+,0)$ in $(\mathbf{Set},\times)$ is a bijection — it is not, so a weak functor could not encode it.

---

# Solution

The plan: (a) read off the data of a lax functor out of $\mathbf{1}$ and match it to a monoid; (b) reduce the three lax axioms to the three monoid axioms, using that $\mathbf{1}$'s structural morphisms are all identities; (c) dualize for comonoids and explain the lax level by the non-invertibility of multiplication. The whole exercise is the observation that a point carries no information, so all the content of a lax functor out of it lands in its single value object.

**Step 1: The data of $F:\mathbf{1}\to\mathcal{D}$ is a monoid's data.**

A lax monoidal functor $F:\mathbf{1}\to\mathcal{D}$ gives an object $M=F(\ast)$, a map $\mu:=\varphi_{\ast,\ast}:M\boxtimes M\to M$, and a map $\eta:=\varphi_0:J\to M$.

> [!note]- Derivation
> A [[Def - Functor|functor]] $F:\mathbf{1}\to\mathcal{D}$ is determined by where it sends the unique object: $M:=F(\ast)$. It must send the unique morphism $1_\ast$ to $1_M$, so there is no further data in $F$ qua functor.
>
> A lax monoidal structure on $F$ adds:
> - the tensor comparison $\varphi_{\ast,\ast}:F(\ast)\boxtimes F(\ast)\to F(\ast\boxtimes\ast)$. Since the monoidal structure on $\mathbf{1}$ has $\ast\boxtimes\ast=\ast$, the target is $F(\ast)=M$, so $\varphi_{\ast,\ast}$ is a morphism $\mu:M\boxtimes M\to M$;
> - the unit comparison $\varphi_0:J\to F(I_{\mathbf{1}})=F(\ast)=M$, a morphism $\eta:J\to M$.
>
> Naturality of $\varphi$ is automatic (there is only one morphism in $\mathbf{1}$ to be natural in). So the data of $(F,\varphi,\varphi_0)$ is exactly $(M,\mu,\eta)$ — the data of a [[Def - Monoid in a Monoidal Category|monoid]].

**Step 2: The lax axioms are the monoid axioms.**

> [!note]- Derivation
> In $\mathbf{1}$ every structural isomorphism — associator $\alpha$, unitors $\lambda,\rho$ — is the unique morphism $1_\ast$, so $F$ of any of them is $1_M$. Substitute into the three lax coherence axioms.
>
> *Associativity coherence.* The general axiom
> $$F(\alpha)\circ\varphi_{\ast\boxtimes\ast,\ast}\circ(\varphi_{\ast,\ast}\boxtimes 1) = \varphi_{\ast,\ast\boxtimes\ast}\circ(1\boxtimes\varphi_{\ast,\ast})\circ\alpha'$$
> becomes, with $F(\alpha)=1_M$ and $\alpha'=\alpha'_{M,M,M}$ the associator of $\mathcal{D}$,
> $$\mu\circ(\mu\boxtimes 1_M) = \mu\circ(1_M\boxtimes\mu)\circ\alpha'_{M,M,M},$$
> which is exactly [[Def - Monoid in a Monoidal Category|monoid]] associativity (the associator $\alpha'$ is the usual one absorbed into the equation; in a strict $\mathcal{D}$ it disappears and we get $\mu(\mu\boxtimes 1)=\mu(1\boxtimes\mu)$).
>
> *Left unit coherence.* $F(\lambda)\circ\varphi_{I,\ast}\circ(\varphi_0\boxtimes 1)=\lambda'_{M}$ becomes $\mu\circ(\eta\boxtimes 1_M) = \lambda'_M$, the left unit law.
>
> *Right unit coherence.* Dually $\mu\circ(1_M\boxtimes\eta) = \rho'_M$, the right unit law.
>
> These are precisely the three axioms of a monoid in $\mathcal{D}$. So lax monoidal functors $\mathbf{1}\to\mathcal{D}$ are monoids in $\mathcal{D}$, and the correspondence is a bijection (it is also functorial: monoidal natural transformations between such functors are monoid [[Def - Homomorphism|homomorphisms]]).

**Step 3: Comonoids and the level of laxness.**

> [!note]- Derivation
> *Comonoids.* An [[Def - Weak and Lax Monoidal Functor|oplax monoidal functor]] $\mathbf{1}\to\mathcal{D}$ has comparison arrows *reversed*: $\psi_{\ast,\ast}:F(\ast\boxtimes\ast)\to F\ast\boxtimes F\ast$, i.e. $\Delta:M\to M\boxtimes M$, and $\psi_0:F\ast\to J$, i.e. $\varepsilon:M\to J$. The oplax coherence axioms become coassociativity and counit laws, so an oplax functor $\mathbf{1}\to\mathcal{D}$ is exactly a **comonoid** $(M,\Delta,\varepsilon)$.
>
> *Why lax, not weak.* If we required $\varphi=\mu$ to be an isomorphism (the weak/strong level), the multiplication of the monoid would have to be invertible. But multiplications are generically non-invertible: in $(\mathbf{Set},\times)$ the monoid $(\mathbb{N},+,0)$ has $+:\mathbb{N}\times\mathbb{N}\to\mathbb{N}$, which is not a bijection; a group algebra's multiplication $k[G]\otimes k[G]\to k[G]$ is not invertible; a ring's multiplication is not invertible. Demanding weak would collapse the correspondence to the trivial monoids (those whose multiplication is an iso). So lax is forced: it is the precise level that allows the comparison map to be a genuine, non-invertible multiplication, which is exactly why lax monoidal functors are the structure-transporting maps.

> [!note]- Complete formal solution
> **(a)** A functor $F:\mathbf{1}\to\mathcal{D}$ is an object $M=F(\ast)$. A lax structure adds $\mu:=\varphi_{\ast,\ast}:M\boxtimes M\to M$ (using $\ast\boxtimes\ast=\ast$) and $\eta:=\varphi_0:J\to M$. This is the data of a [[Def - Monoid in a Monoidal Category|monoid]].
>
> **(b)** Since all structural morphisms of $\mathbf{1}$ are the unique $1_\ast$, $F$ sends them to $1_M$, and the three lax axioms reduce to $\mu(\mu\boxtimes 1)=\mu(1\boxtimes\mu)\alpha'$ (associativity), $\mu(\eta\boxtimes 1)=\lambda'$ (left unit), $\mu(1\boxtimes\eta)=\rho'$ (right unit) — the monoid axioms. The correspondence is a bijection, functorial in monoid homomorphisms.
>
> **(c)** Reversing the comparison arrows gives an oplax functor $\mathbf{1}\to\mathcal{D}$, whose data $\Delta:M\to M\boxtimes M$, $\varepsilon:M\to J$ and axioms are a **comonoid**. Lax (not weak) is correct because the multiplication of a monoid is generically non-invertible (e.g. $(\mathbb{N},+)$, group algebras), so requiring the comparison to be an isomorphism would discard all interesting monoids. $\qquad\blacksquare$

---

# Key Takeaways

**A monoid is a lax functor from a point — the single most useful slogan about lax monoidal functors.** This correspondence is the operational definition of "lax monoidal functor carries algebraic structure," made into an exact statement. The terminal category $\mathbf{1}$ is the free monoidal category on nothing, so a lax functor out of it is "structure with no underlying variation," which is precisely an object equipped with a multiplication and unit — a monoid. The trigger to internalise: whenever you want to know what kind of map preserves [[Def - Monoid in a Monoidal Category|monoids]], remember that monoids *are* lax functors from a point, so the maps that preserve them are the ones that compose with lax functors — namely lax (or weak) monoidal functors. This single identification organizes a large amount of algebra: [[Def - Ring|rings]], algebras, monads, and [[Def - Operad|operad]] algebras are all monoids, hence all lax functors from a point into the right monoidal category.

**The level of laxness is dictated by the invertibility of the structure map, and choosing it wrongly silently discards your examples.** The exercise's key decision — lax, not weak — is a special case of a general diagnostic. When encoding an algebraic structure as a functor, ask whether the structure's defining operation is invertible: if not (multiplications, comultiplications, most natural transformations of interest), you must work at the lax or oplax level, never the weak one. Working at the weak level when the operation is non-invertible does not produce an error message; it silently restricts you to the degenerate sub-case where the operation happens to be an isomorphism, which is almost never what you want. This is why the four flavours of monoidal functor are kept distinct and why "monoidal functor" unqualified is ambiguous.

**Feeding the smallest possible source into a general definition isolates its essential content.** The method here — take the source to be $\mathbf{1}$ and read off what survives — is a reusable technique for understanding any structured-functor notion. A functor from a point is just an object; a lax/oplax/weak structure on it is just the corresponding structure on that object. The same move shows that a functor from the walking arrow is a morphism, a functor from the walking idempotent is an idempotent, and a monoidal functor from the free monoidal category on one object is an object-with-iterated-tensor. Whenever a definition feels abstract, evaluate it on the terminal or a free generating source: the general nonsense collapses to a concrete algebraic gadget, and that gadget is the definition's true content.
