---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Dedekind Domain"
  - "Def - Field of Fractions"
  - "Def - Integral Domain"
  - "Def - Ideal"
  - "Def - Principal Ideal Domain"
  - "Def - Unique Factorization Domain"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A$ be an integral domain with [[Def - Field of Fractions|fraction field]] $K = \operatorname{Frac}(A)$. A **fractional ideal** is a certain $A$-submodule of $K$; we write $\mathfrak{a}, \mathfrak{b}$ for fractional ideals, $\mathfrak{a}\mathfrak{b}$ for their product, $\mathfrak{a}^{-1} = (A : \mathfrak{a}) = \{x \in K : x\mathfrak{a} \subseteq A\}$ for the inverse-candidate, and $(x) = xA$ for the principal fractional ideal of $x \in K^\times$. When $A$ is [[Def - Dedekind Domain|Dedekind]], $\mathcal{I}(A)$ is the group of nonzero fractional ideals, $\mathcal{P}(A) = \{(x) : x \in K^\times\}$ the principal ones, and $\operatorname{Cl}(A) = \mathcal{I}(A)/\mathcal{P}(A)$ the class group. The full registry is on [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

This is a compound page: it defines three interlocking notions — the **fractional ideal**, the multiplicative **group $\mathcal{I}(A)$** they form over a Dedekind domain, and the **ideal class group $\operatorname{Cl}(A)$** — because the group structure is the reason fractional ideals are introduced, and the class group is the single most important invariant it produces.

---

# Axiom Motivation

The goal is to **turn the ideals of a domain into a group**, so that the cancellation and division we take for granted with numbers become available for ideals. Ordinary ideals of $A$ form a *monoid* under multiplication — you can multiply $\mathfrak{a}\mathfrak{b}$, the identity is $A$ — but not a group, because there is no inverse: $\mathfrak{a}\mathfrak{b} = A$ forces both to be the unit ideal, so only $A$ itself is invertible among honest ideals. To get inverses we must enlarge the world, and the enlargement is forced by a single observation: the inverse of a principal ideal $(x) = xA$ *should* be $(x^{-1}) = x^{-1}A$, since $(x)(x^{-1}) = xx^{-1}A = A$. But $x^{-1}A$ is not contained in $A$ when $x$ is a non-unit — it lives in the fraction field $K$. So the moment we want inverses, we are forced out of $A$ and into $K$, and the objects we land on are $A$-submodules of $K$. That is the entire content of "fractional ideal".

**Why "submodule of $K$ with a common denominator", and not just any submodule of $K$.** We want the new objects to behave like ideals: finitely generated (so that multiplication and the module operations are well-controlled), and "comparable in size to $A$". The precise condition is that there is a single nonzero $d \in A$ with $d\mathfrak{a} \subseteq A$ — clearing denominators by one element turns $\mathfrak{a}$ into an honest ideal $d\mathfrak{a}$ of $A$. This excludes wild submodules like $K$ itself (which has no common denominator) while including everything of the form $\tfrac1d \mathfrak{b}$ for an ideal $\mathfrak{b}$. Drop the common-denominator condition and you lose finiteness over Noetherian $A$ and the products stop being fractional ideals; keep it and a fractional ideal is exactly a finitely generated $A$-submodule of $K$ when $A$ is Noetherian. The condition is the minimal one making fractional ideals a closed, well-behaved system under product, sum, and the inverse operation.

**Why the inverse is $(A : \mathfrak{a})$, and why it only works for Dedekind domains.** The natural candidate for $\mathfrak{a}^{-1}$ is the largest thing that multiplies $\mathfrak{a}$ back into $A$: the set $(A : \mathfrak{a}) = \{x \in K : x\mathfrak{a} \subseteq A\}$. One always has $\mathfrak{a}\,(A:\mathfrak{a}) \subseteq A$, so this is at worst a divisor of $A$; the question is whether equality $\mathfrak{a}\,(A:\mathfrak{a}) = A$ holds — whether $(A:\mathfrak{a})$ is a genuine inverse. For a general domain it can fail: in $k[x,y]$ the maximal ideal $\mathfrak{m} = (x,y)$ has $(A : \mathfrak{m}) = A$, so $\mathfrak{m}(A:\mathfrak{m}) = \mathfrak{m} \neq A$ — the ideal is not invertible. The deep theorem is that **invertibility of every nonzero fractional ideal is equivalent to being a Dedekind domain**. So the group structure is not free; it is the defining miracle of Dedekind domains, and the cleanest characterization of them. The mechanism that makes it work is local: at each prime, $\mathfrak{a}A_\mathfrak{p} = (\pi^n)$ is principal in the DVR $A_\mathfrak{p}$, hence invertible, and the local inverses glue because unique factorization writes $\mathfrak{a} = \prod\mathfrak{p}^{n_\mathfrak{p}}$ and lets us set $\mathfrak{a}^{-1} = \prod\mathfrak{p}^{-n_\mathfrak{p}}$.

**Why quotient by the principal ideals, and what the quotient measures.** Once $\mathcal{I}(A)$ is a group, the principal fractional ideals $\mathcal{P}(A) = \{xA : x \in K^\times\}$ form a subgroup — it is the image of the homomorphism $K^\times \to \mathcal{I}(A)$, $x \mapsto (x)$. These are the "boring" fractional ideals, the ones that come from an actual element. The interesting question is how many fractional ideals are *not* principal, and the cleanest way to package that is the quotient group $\operatorname{Cl}(A) = \mathcal{I}(A)/\mathcal{P}(A)$, the **class group**. Two ideals are identified in $\operatorname{Cl}(A)$ exactly when they differ by a principal ideal, i.e. when $\mathfrak{a} = (x)\mathfrak{b}$ for some $x$ — when they are "the same up to scaling by a field element". The class group is trivial iff every ideal is principal iff $A$ is a PID; its size is therefore a direct measure of the failure of principality, which (for a Dedekind domain) is the same as the failure of unique factorization of elements. This is *why* the construction is built: $\operatorname{Cl}(A)$ is the obstruction, made into a group so it can be computed, bounded, and used.

---

# The Definition

Let $A$ be an integral domain with fraction field $K$.

## Fractional ideal

A **fractional ideal** of $A$ is a nonzero $A$-submodule $\mathfrak{a} \subseteq K$ for which there exists a nonzero $d \in A$ with $d\mathfrak{a} \subseteq A$. (Equivalently, when $A$ is Noetherian: a nonzero finitely generated $A$-submodule of $K$.) An ordinary nonzero ideal of $A$ is a fractional ideal (take $d = 1$); a fractional ideal contained in $A$ is called **integral**. For $x \in K^\times$, the **principal fractional ideal** is $(x) = xA$.

Fractional ideals are multiplied by
$$\mathfrak{a}\mathfrak{b} = \Big\{ \textstyle\sum_{i} a_i b_i : a_i \in \mathfrak{a},\, b_i \in \mathfrak{b} \Big\},$$
which is again a fractional ideal, with identity $A$. The **inverse-candidate** of $\mathfrak{a}$ is
$$\mathfrak{a}^{-1} = (A : \mathfrak{a}) = \{x \in K : x\mathfrak{a} \subseteq A\},$$
always a fractional ideal with $\mathfrak{a}\,\mathfrak{a}^{-1} \subseteq A$.

## The group of fractional ideals

If $A$ is a **[[Def - Dedekind Domain|Dedekind domain]]**, then $\mathfrak{a}\,\mathfrak{a}^{-1} = A$ for every nonzero fractional ideal $\mathfrak{a}$, so the set $\mathcal{I}(A)$ of nonzero fractional ideals is an **abelian group** under multiplication, with identity $A$ and inverse $\mathfrak{a}^{-1}$. By unique factorization of ideals, every $\mathfrak{a} \in \mathcal{I}(A)$ is uniquely
$$\mathfrak{a} = \prod_{\mathfrak{p}} \mathfrak{p}^{\,n_\mathfrak{p}}, \qquad n_\mathfrak{p} \in \mathbb{Z},\ n_\mathfrak{p} = 0 \text{ for almost all } \mathfrak{p},$$
the product over nonzero primes; so $\mathcal{I}(A)$ is the **free abelian group on the set of nonzero prime ideals**, with $\mathfrak{a}^{-1} = \prod \mathfrak{p}^{-n_\mathfrak{p}}$.

## The ideal class group

The **principal fractional ideals** $\mathcal{P}(A) = \{(x) : x \in K^\times\}$ form a subgroup of $\mathcal{I}(A)$ — the image of the homomorphism $K^\times \to \mathcal{I}(A)$, $x \mapsto xA$, whose kernel is $A^\times$. The **ideal class group** is the quotient
$$\operatorname{Cl}(A) = \mathcal{I}(A)/\mathcal{P}(A).$$
Two fractional ideals are in the same **ideal class** iff $\mathfrak{a} = x\mathfrak{b}$ for some $x \in K^\times$. The class group is trivial iff $A$ is a [[Def - Principal Ideal Domain|PID]]. For a ring of integers $\mathcal{O}_K$, $\operatorname{Cl}(\mathcal{O}_K)$ is finite, and its order is the **class number** $h_K$.

---

# Categorical / Structural Definition

There is a clean exact sequence that *is* the structural definition of the class group:
$$1 \longrightarrow A^\times \longrightarrow K^\times \xrightarrow{\ x\,\mapsto\,(x)\ } \mathcal{I}(A) \longrightarrow \operatorname{Cl}(A) \longrightarrow 0.$$
It says: the units $A^\times$ are the field elements whose fractional ideal is trivial; $K^\times$ surjects onto the principal fractional ideals $\mathcal{P}(A)$; and $\operatorname{Cl}(A)$ is the cokernel of "take the principal fractional ideal". Since $\mathcal{I}(A) \cong \bigoplus_\mathfrak{p}\mathbb{Z}$ is free abelian on the primes (the **divisor group**), this exhibits $\operatorname{Cl}(A)$ as $\operatorname{coker}\!\big(K^\times \to \bigoplus_\mathfrak{p}\mathbb{Z}\big)$ — divisors modulo principal divisors. In the language of homological algebra this is the **degree-zero Picard functor**: $\operatorname{Cl}(A) = \operatorname{Pic}(\operatorname{Spec} A)$, the group of isomorphism classes of rank-one **projective modules** (line bundles) under tensor product, with $\mathfrak{a}$ corresponding to the module $\mathfrak{a}$ itself and the trivial class to the free module $A$. The two descriptions — cokernel of the divisor map, and $\operatorname{Pic}$ — are the same group seen arithmetically and geometrically.

---

# Relate to Other Fields / Compression

The cleanest compression: **a fractional ideal is "an ideal with denominators allowed", introduced so that ideals can be divided; the class group is "fractional ideals modulo the principal ones", the exact obstruction to being a PID.** Over a Dedekind domain, $\mathcal{I}(A) = \bigoplus_\mathfrak{p}\mathbb{Z}$ is free abelian on the primes, so ideal arithmetic becomes vector arithmetic and $\operatorname{Cl}(A)$ is a cokernel.

**True name:** the true name of the class group is "**$\operatorname{Pic}$ of the curve $\operatorname{Spec} A$ — the group of line bundles**", and equivalently "**the group of nonzero ideals modulo "differ by a principal ideal"**". The first is how to think about it; the second is how to compute with it. The class number $h$ is the order of this group, and $h = 1$ is exactly "$A$ is a PID".

A fractional ideal is, as a module, a **rank-one projective**: locally free of rank one but not globally free unless principal. This is the precise sense in which the class group is the simplest instance of the **Serre–Swan** correspondence between projective modules and vector bundles — a line bundle on $\operatorname{Spec} A$ — and the seed of the observation from [[Commutative Algebra IV — Localization|Localization]] that *freeness is not a local property*. In number theory, the finiteness of $\operatorname{Cl}(\mathcal{O}_K)$ (Minkowski's theorem) and the size of $h_K$ are central; in geometry, $\operatorname{Pic}$ of a curve carries the structure of the Jacobian variety.

---

# Examples / Corollaries

**Is an instance — principal fractional ideals.** In any domain, $(x) = xA$ for $x \in K^\times$ is a fractional ideal: take $d = $ the denominator of $x$. These are exactly the elements of $\mathcal{P}(A)$, and they form the trivial class in $\operatorname{Cl}(A)$. In $\mathbb{Z}$ with $K = \mathbb{Q}$, the fractional ideal $\tfrac{2}{3}\mathbb{Z} = \{\tfrac{2n}{3} : n \in \mathbb{Z}\}$ is principal, generated by $\tfrac23$.

**Is an instance — every Dedekind ideal, factored.** In $\mathbb{Z}[\sqrt{-5}]$, the fractional ideal $\mathfrak{p}^{-1}$ where $\mathfrak{p} = (2, 1+\sqrt{-5})$ is $\{x \in K : x\mathfrak{p} \subseteq A\}$, and $\mathfrak{p}\,\mathfrak{p}^{-1} = A$. Here $\mathfrak{p}$ is *not* principal but $\mathfrak{p}^2 = (2)$ *is*, so $[\mathfrak{p}]$ has order $2$ in $\operatorname{Cl}(\mathbb{Z}[\sqrt{-5}]) \cong \mathbb{Z}/2$. See [[Ex - The class group measures failure of unique factorization]].

**Is NOT an instance (of invertibility) — a non-Dedekind domain.** In $A = k[x,y]$, the ideal $\mathfrak{m} = (x,y)$ is a fractional ideal (it is an honest ideal) but is *not invertible*: $(A : \mathfrak{m}) = A$, so $\mathfrak{m}(A:\mathfrak{m}) = \mathfrak{m} \neq A$. Thus $\mathcal{I}(A)$ is not a group here — the group structure is exclusive to Dedekind domains. This is the example showing invertibility is the Dedekind miracle, not a general fact.

**Is NOT an instance — $K$ itself.** The whole field $K$ is an $A$-submodule of $K$ but is *not* a fractional ideal (when $A \neq K$): no single $d \in A$ has $dK \subseteq A$, since $K$ has no common denominator. This shows the common-denominator condition is doing real work.

**Corollary — trivial class group means PID.** If $\operatorname{Cl}(A)$ is trivial then every fractional ideal is principal, so in particular every integral ideal is principal, so $A$ is a PID. Conversely a PID has trivial class group. Hence for a Dedekind domain, "$A$ is a PID" $\iff$ "$A$ is a UFD" $\iff$ "$\operatorname{Cl}(A) = 0$".

**Corollary — the class of a product is the product of classes.** Since $\operatorname{Cl}(A)$ is a quotient group, $[\mathfrak{a}\mathfrak{b}] = [\mathfrak{a}][\mathfrak{b}]$ and $[\mathfrak{a}^{-1}] = [\mathfrak{a}]^{-1}$. In particular, if $\mathfrak{a}^n$ is principal then $[\mathfrak{a}]$ has order dividing $n$ — the route by which one shows $[\mathfrak{p}]$ has order $2$ in $\mathbb{Z}[\sqrt{-5}]$ from $\mathfrak{p}^2 = (2)$.

**Calibration check.** Verify $\mathfrak{a}(A:\mathfrak{a}) \subseteq A$ for any fractional ideal, directly from the definition of $(A:\mathfrak{a})$. Confirm that $x \mapsto (x)$ is a homomorphism $K^\times \to \mathcal{I}(A)$ with kernel $A^\times$. Check that in $\mathbb{Z}$ every fractional ideal is $\tfrac{m}{n}\mathbb{Z}$, hence principal, so $\operatorname{Cl}(\mathbb{Z}) = 0$. Finally, confirm that $\mathfrak{p}^2 = (2)$ principal forces $[\mathfrak{p}]^2 = 1$ in the class group, so $[\mathfrak{p}]$ has order $1$ or $2$.

---

# Unlocked by This

> [!tip] The Picard group and line bundles on a curve *(from Algebraic Geometry)*
> The class group $\operatorname{Cl}(A) = \operatorname{Pic}(\operatorname{Spec} A)$ is the **Picard group** of the affine curve: isomorphism classes of **line bundles**, with tensor product as the operation and the trivial bundle $A$ as identity. A fractional ideal *is* a line bundle (a rank-one locally free, hence **projective**, module), trivial exactly when principal. For a complete smooth curve over $\mathbb{C}$, the degree-zero part of $\operatorname{Pic}$ is a complex torus — the **Jacobian variety** — and the whole theory of divisors, linear systems, and the Riemann–Roch theorem is built on this group. The class group of a Dedekind domain is the affine, arithmetic shadow of all of it.

> [!tip] The class number and finiteness *(from Algebraic Number Theory)*
> For a number ring $\mathcal{O}_K$, the class group is **finite**, and its order $h_K$ — the **class number** — is one of the central invariants of the field, controlling how badly unique factorization fails. Its finiteness (Minkowski's geometry-of-numbers bound) and its analytic expression (the class number formula relating $h_K$ to the residue of the Dedekind zeta function) are foundational results. Kummer's proof of Fermat's Last Theorem for **regular primes** turns precisely on $p \nmid h_{\mathbb{Q}(\zeta_p)}$ — a condition on the class number.

> [!tip] The unit group and Dirichlet's theorem *(from Algebraic Number Theory)*
> The kernel of $K^\times \to \mathcal{I}(A)$ is the unit group $A^\times = \mathcal{O}_K^\times$, and the exact sequence on this page pairs the *finite* class group with the unit group, whose structure is governed by **Dirichlet's unit theorem**: $\mathcal{O}_K^\times \cong \mu_K \times \mathbb{Z}^{r_1 + r_2 - 1}$, a finite torsion part times a free part of computable rank. Together, the class group and the unit group are the two halves of the arithmetic of a number field encoded in its fractional ideals.
