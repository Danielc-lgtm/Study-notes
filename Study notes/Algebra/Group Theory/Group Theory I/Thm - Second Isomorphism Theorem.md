---
type: theorem
subject: group-theory
prereqs:
  - "Def - Subgroup"
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group, $H \leq G$ is a [[Def - Subgroup|subgroup]], and $K \trianglelefteq G$ is a [[Def - Normal Subgroup|normal subgroup]]. The product set is $HK = \{hk : h \in H,\ k \in K\}$, and the intersection $H \cap K$ is the set of elements in both. The notation $H \hookrightarrow G$ denotes the inclusion homomorphism $h \mapsto h$, and $G \twoheadrightarrow G/K$ the quotient homomorphism $g \mapsto gK$. The symbol $\cong$ denotes [[Def - Isomorphism|isomorphism]]. The full registry is on the parent page [[Group Theory I — §1.1–1.2]].

---

# Statement

> **Second Isomorphism Theorem.** Let $G$ be a group, $H \leq G$ a subgroup, and $K \trianglelefteq G$ a normal subgroup. Then:
> 1. $HK$ is a subgroup of $G$;
> 2. $K \trianglelefteq HK$, and $H \cap K \trianglelefteq H$;
> 3. there is an isomorphism
> $$\frac{HK}{K} \;\cong\; \frac{H}{H \cap K}.$$

---

# Motivation

You have a subgroup $H$ and a normal subgroup $K$ of the same group $G$, and you would like to understand how they relate. The first thing you might do is form the [[Def - Quotient Group|quotient]] $G/K$ — collapsing $K$ to a point — and ask what becomes of $H$ inside it. The image of $H$ in $G/K$ is the set of cosets $\{hK : h \in H\}$. The second isomorphism theorem answers two questions about this image at once: *which cosets* it consists of, and *what group* it is.

The first answer is $HK/K$. The image of $H$ in $G/K$ is exactly the cosets that have a representative inside $H$, and that set of representatives is the product $HK$ — so the image is the subgroup $HK/K$ of $G/K$. The second answer comes from asking what $H$ loses when pushed into $G/K$: two elements of $H$ collapse together precisely when they differ by an element of $K$, that is, by an element of $H \cap K$. So the image is $H$ with $H \cap K$ collapsed, namely $H/(H \cap K)$. Setting the two descriptions of the same image equal gives the theorem.

This is why the theorem is sometimes drawn as a **diamond**: the four groups $HK$, $H$, $K$, $H\cap K$ sit at the corners of a square of inclusions, and the theorem says the two "opposite" quotients $HK/K$ and $H/(H\cap K)$ — the two diagonals of the diamond — are isomorphic. Concretely, it lets you compute a quotient $HK/K$ that might look complicated, by trading it for $H/(H\cap K)$, which often does not, because $H$ and $H\cap K$ are groups you chose and understand. It also produces, for free, the normality $H \cap K \trianglelefteq H$, which is useful in its own right.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$H$ a subgroup, $K$ a normal subgroup of the same $G$". The disguised sources are situations where one of the two subgroups is normal *for a structural reason you might not immediately spot*.

The first source is **$K$ of index $2$**, or more generally a subgroup that is normal because it is the kernel of a homomorphism. A subgroup of index $2$ is automatically normal, so it is a legitimate $K$. The non-obvious step is recognising that you do not need to *check* normality by conjugation — index $2$ hands it to you. *Example problem:* in a group $G$ with an index-$2$ subgroup $K$ and any subgroup $H$, apply the theorem to compute $H/(H\cap K)$, which must be trivial or $C_2$ since $HK/K \leq G/K \cong C_2$.

The second source is **$K$ the centre $Z(G)$**, or any characteristic subgroup. The centre is always normal — conjugation fixes central elements — so $K = Z(G)$ is always allowed. The non-obviousness is that "central" instantly delivers "normal", letting you relate any subgroup $H$ to the centre via $HZ(G)/Z(G) \cong H/(H \cap Z(G))$. *Example problem:* show that if $G/Z(G)$ is cyclic then $G$ is abelian, by analysing $H Z(G)/Z(G)$ for a suitable $H$.

The third source is **the ambient group $G$ itself being abelian**, where *every* subgroup is normal, so the roles of $H$ and $K$ are interchangeable and the theorem applies to any pair. The non-obvious payoff is that in the abelian setting the theorem becomes the symmetric, fully general statement $(H + K)/K \cong H/(H \cap K)$ for *all* subgroups, which is the additive identity behind dimension counts. *Example problem:* for subspaces $U, W$ of a vector space, derive $\dim(U+W) = \dim U + \dim W - \dim(U \cap W)$.

**Targets (Output Amplification)**

The conclusion gives an isomorphism $HK/K \cong H/(H\cap K)$ and the normality $H \cap K \trianglelefteq H$.

Combine the conclusion with **Lagrange-style counting**. The isomorphism gives $|HK/K| = |H/(H\cap K)|$, that is $|HK|/|K| = |H|/|H\cap K|$, which rearranges to the **product formula**
$$|HK| = \frac{|H|\,|K|}{|H \cap K|}.$$
The further result $E$ is a precise size for the product set $HK$ — non-obvious because $HK$ need not be a "nice" set a priori, yet its cardinality is forced by those of $H$, $K$, and their intersection. This formula is one of the most-used counting tools in finite group theory.

Combine the conclusion with **coprimality of $|H|$ and $|K|$**. If $\gcd(|H|, |K|) = 1$, then $|H \cap K|$ divides both by Lagrange, so $H \cap K = \{e\}$, and the theorem collapses to $HK/K \cong H$. The further result is that $H$ embeds *isomorphically* into the quotient $G/K$ — a coprime subgroup is undisturbed by quotienting out $K$. This is the standard mechanism for finding a copy of a known group inside a quotient.

Combine the normality conclusion $H \cap K \trianglelefteq H$ with **an inductive argument**. The theorem manufactures a normal subgroup of $H$ out of thin air whenever $H$ meets a normal subgroup $K$ of the ambient group. The further result is a supply of normal subgroups for proofs that recurse on subgroup structure — for instance, building [[Thm - Composition Series|composition series]] or proving solvability is inherited by subgroups.

---

# Why Is It True

The theorem looks like it has three separate claims, but they are all consequences of one act: **push $H$ through the quotient map $G \to G/K$ and watch what happens.**

Call that map $\pi : G \to G/K$, $g \mapsto gK$. Restrict it to $H$ — that is, only feed it elements of $H$. What is the image of this restricted map? It is $\{hK : h \in H\}$. Now, two facts. A coset $gK$ has a representative in $H$ exactly when $g \in HK$, so the *set* of cosets in the image is exactly $HK/K$ — and being the image of a homomorphism, $HK/K$ is a subgroup; pulling that back, $HK$ is a subgroup of $G$. That is claim 1, and it explains the otherwise-surprising fact that the product of two subgroups is a subgroup: $HK/K$ is a subgroup *because images of homomorphisms always are*, and normality of $K$ is what makes $\pi$ exist in the first place.

What is the *kernel* of the restricted map? An element $h \in H$ goes to the identity coset $K$ exactly when $h \in K$, i.e. exactly when $h \in H \cap K$. Kernels are always normal in the domain, and the domain here is $H$ — so $H \cap K \trianglelefteq H$. That is claim 2, and again it is not a fact you must verify by conjugation; it is automatic, because $H \cap K$ *is a kernel*.

Now the isomorphism is forced. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] says any homomorphism induces an isomorphism between (domain modulo kernel) and image. Here domain is $H$, kernel is $H \cap K$, image is $HK/K$. So $H/(H\cap K) \cong HK/K$. That is claim 3.

The deep point: the second isomorphism theorem is *not a new theorem*. It is the first isomorphism theorem applied to one specific, very natural homomorphism — the inclusion of $H$ followed by the quotient by $K$. Everything surprising about it (that $HK$ is a subgroup, that $H \cap K$ is normal in $H$) is just the generic good behaviour of kernels and images, made visible by choosing the right map. Once you see the map $h \mapsto hK$ on $H$, the theorem is not merely plausible — it is unavoidable.

---

# What Makes This Hard

The standard place people get stuck is trying to prove claim 1 — that $HK$ is a subgroup — by a direct closure computation, which works but is fiddly and tempts the error of *forgetting that normality of $K$ is essential* (with neither $H$ nor $K$ normal, $HK$ generally fails to be a subgroup). The non-obvious move that dissolves the whole difficulty is to *not* prove the three claims separately: instead define the single homomorphism $\varphi : H \to G/K$, $h \mapsto hK$, and let the first isomorphism theorem deliver all three at once. The other common slip is mislabelling the diamond — pairing $HK/K$ with $H/(H\cap K)$ is correct, but it is easy to write the kernel as $K$ instead of $H \cap K$, since the map is $h \mapsto hK$ and one forgets that $h$ ranges only over $H$.

---

# Rederivation Scaffold

**High-level strategy:**
Do not attack the three claims independently. Define one homomorphism — restrict the quotient map $G \to G/K$ to the subgroup $H$ — and compute its image and kernel. Claims 1 and 2 fall out of "images and kernels are subgroups / normal", and claim 3 is the first isomorphism theorem applied to this map.

**Subgoal decomposition:**

1. **Define the map.** Set $\varphi : H \to G/K$ by $\varphi(h) = hK$. Check it is a homomorphism.
   - *Hint:* It is the composite $H \hookrightarrow G \xrightarrow{\pi} G/K$; both pieces are homomorphisms, so the composite is. Note this uses $K \trianglelefteq G$, since otherwise $G/K$ is not a group.
   - *Why needed:* This single map is the source of all three claims.

2. **Compute the image.** Show $\operatorname{im}\varphi = HK/K$, and deduce $HK \leq G$.
   - *Hint:* $\operatorname{im}\varphi = \{hK : h \in H\}$; a coset $gK$ lies here if and only if $g \in HK$. The image of a homomorphism is a subgroup of $G/K$, and its preimage under $\pi$ is the subgroup $HK$.
   - *Why needed:* Gives claim 1 and identifies the right-hand side of the isomorphism.

3. **Compute the kernel.** Show $\ker\varphi = H \cap K$, and deduce $H \cap K \trianglelefteq H$.
   - *Hint:* $h \in \ker\varphi$ if and only if $hK = K$ if and only if $h \in K$; since also $h \in H$, this is $h \in H\cap K$. Kernels are normal in the domain $H$.
   - *Why needed:* Gives the normality half of claim 2 and the left-hand side of the isomorphism.

4. **Apply the first isomorphism theorem.** Conclude $H/(H\cap K) \cong HK/K$.
   - *Hint:* The first isomorphism theorem says $H/\ker\varphi \cong \operatorname{im}\varphi$; substitute the kernel and image computed above.
   - *Why needed:* This is claim 3, the isomorphism itself.

5. **Note $K \trianglelefteq HK$.** Observe $K \subseteq HK \subseteq G$ and $K$ normal in $G$ restricts to normal in the smaller group $HK$.
   - *Hint:* Conjugation-invariance by all of $G$ in particular gives conjugation-invariance by every element of $HK$.
   - *Why needed:* Completes claim 2 and makes the quotient $HK/K$ legitimate.

---

# Lemma Decomposition

> [!note]- Lemma 1: A coset $gK$ has a representative in $H$ if and only if $g \in HK$
> **Statement:** For $H \leq G$, $K \trianglelefteq G$, and $g \in G$: there exists $h \in H$ with $hK = gK$ if and only if $g \in HK$.
>
> **Hint:** $hK = gK$ means $g^{-1}h \in K$; rearrange to express $g$ in terms of $h$ and an element of $K$.
>
> **Why needed:** It identifies $\operatorname{im}\varphi$ with $HK/K$ — the right-hand side of the theorem — and shows $HK$ is the preimage of a subgroup, hence a subgroup.
>
> > [!note]- Full proof
> > ($\Rightarrow$) Suppose $hK = gK$ for some $h \in H$. Then $g^{-1}h \in K$, say $g^{-1}h = k$, so $g = hk^{-1} \in HK$ (since $k^{-1} \in K$).
> >
> > ($\Leftarrow$) Suppose $g \in HK$, say $g = hk$ with $h \in H$, $k \in K$. Then $g^{-1}h = (hk)^{-1}h = k^{-1}h^{-1}h = k^{-1} \in K$, so $gK = hK$, and $h \in H$ is the required representative.

> [!note]- Lemma 2: The product $HK$ is a subgroup of $G$ when $K \trianglelefteq G$
> **Statement:** If $H \leq G$ and $K \trianglelefteq G$, then $HK = \{hk : h\in H, k\in K\}$ is a subgroup of $G$.
>
> **Hint:** Use the subgroup criterion: take $hk, h'k' \in HK$ and show $(h'k')(hk)^{-1} \in HK$, inserting $h^{-1}h$ to move a $K$-element past an $H$-element via normality.
>
> **Why needed:** It is claim 1 of the theorem, proved directly here as an alternative to the homomorphism route (and a self-contained drill in using normality).
>
> > [!note]- Full proof
> > The set $HK$ is non-empty since $e = ee \in HK$. Take $hk, h'k' \in HK$. Then
> > $$h'k'(hk)^{-1} = h'k'k^{-1}h^{-1} = (h'h^{-1})\,\big(h(k'k^{-1})h^{-1}\big).$$
> > The first factor $h'h^{-1}$ lies in $H$. The second factor is $k'k^{-1} \in K$ conjugated by $h \in G$, which lies in $K$ because $K$ is normal in $G$. So $h'k'(hk)^{-1}$ is a product of an element of $H$ with an element of $K$, hence lies in $HK$. By the subgroup criterion, $HK \leq G$.

> [!note]- Lemma 3: The restricted quotient map and its kernel and image
> **Statement:** Let $K \trianglelefteq G$, $H \leq G$. The map $\varphi : H \to G/K$, $\varphi(h) = hK$, is a homomorphism with $\ker\varphi = H \cap K$ and $\operatorname{im}\varphi = HK/K$.
>
> **Hint:** $\varphi$ is the inclusion $H \hookrightarrow G$ followed by the quotient map $\pi : G \to G/K$. For the kernel, $\varphi(h) = K \iff h \in K$.
>
> **Why needed:** It is the single homomorphism that the first isomorphism theorem is applied to; its kernel and image are the two sides of the final isomorphism.
>
> > [!note]- Full proof
> > The quotient map $\pi : G \to G/K$, $g \mapsto gK$, is a homomorphism (this requires $K \trianglelefteq G$). The inclusion $\iota : H \to G$, $h \mapsto h$, is a homomorphism. Hence $\varphi = \pi \circ \iota : H \to G/K$, $h \mapsto hK$, is a homomorphism.
> >
> > *Kernel.* The identity of $G/K$ is the coset $K$. So $h \in \ker\varphi \iff hK = K \iff h \in K$. Since $h$ is already in $H$, this says $h \in H \cap K$. Thus $\ker\varphi = H \cap K$.
> >
> > *Image.* By definition $\operatorname{im}\varphi = \{hK : h \in H\}$. By Lemma 1 this is exactly the set of cosets $gK$ with $g \in HK$, that is, $HK/K$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a group, $H \leq G$, and $K \trianglelefteq G$.
>
> **The homomorphism.** Define
> $$\varphi : H \longrightarrow G/K, \qquad \varphi(h) = hK.$$
> This is the composite of the inclusion $H \hookrightarrow G$ with the quotient homomorphism $G \to G/K$ (which exists because $K \trianglelefteq G$), so $\varphi$ is a homomorphism.
>
> **Claim 1: $HK$ is a subgroup.** The image $\operatorname{im}\varphi$ is a subgroup of $G/K$. By the coset-representative argument (Lemma 1), a coset $gK$ lies in $\operatorname{im}\varphi$ exactly when $g \in HK$; thus $\operatorname{im}\varphi$ consists precisely of the cosets of $K$ with a representative in $HK$. The union of these cosets is the set $HK$ itself (each such coset $hK$ with $h\in H$ is contained in $HK$, and conversely each element $hk\in HK$ lies in the coset $hK$). Since a union of cosets forming a subgroup of $G/K$ pulls back to a subgroup of $G$, $HK$ is a subgroup of $G$. (For a self-contained direct proof, see Lemma 2.)
>
> **Claim 2: normality.** Since $K \subseteq HK \subseteq G$ and $K$ is normal in $G$, conjugation by any element of the subgroup $HK$ maps $K$ into $K$; hence $K \trianglelefteq HK$, and the quotient $HK/K$ is a group. For the other half: $\ker\varphi$ is a normal subgroup of the domain $H$. We compute $\ker\varphi$: an element $h \in H$ satisfies $\varphi(h) = K$ if and only if $hK = K$ if and only if $h \in K$; combined with $h \in H$ this gives $h \in H \cap K$. So $\ker\varphi = H \cap K$, and therefore $H \cap K \trianglelefteq H$.
>
> **Claim 3: the isomorphism.** We have a homomorphism $\varphi : H \to G/K$ with
> $$\ker\varphi = H \cap K, \qquad \operatorname{im}\varphi = HK/K$$
> (the image computed via Lemma 1). The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied to $\varphi$ gives an isomorphism
> $$\frac{H}{\ker\varphi} \;\cong\; \operatorname{im}\varphi, \qquad\text{that is}\qquad \frac{H}{H \cap K} \;\cong\; \frac{HK}{K}. \qquad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**The inclusion–exclusion dimension formula in linear algebra.** For subspaces $U$ and $W$ of a vector space $V$, the second isomorphism theorem (in its additive, abelian form, with submodules replacing subgroups) gives $(U+W)/W \cong U/(U\cap W)$. Taking dimensions yields $\dim(U+W) - \dim W = \dim U - \dim(U\cap W)$, i.e. $\dim(U+W) = \dim U + \dim W - \dim(U\cap W)$. The application is non-obvious because the dimension formula is usually proved by extending a basis; recognising it as a *quotient isomorphism* shows it is the same theorem as the group product formula $|HK| = |H||K|/|H\cap K|$.

**Counting in finite groups via the product formula.** Suppose $G$ has order $p q$ with $p < q$ primes, and $H$, $K$ are subgroups of orders $p$ and $q$ with $K$ normal. The product formula $|HK| = |H||K|/|H\cap K|$ and $|H\cap K| = 1$ (orders coprime) give $|HK| = pq = |G|$, so $G = HK$. The theorem is the hidden engine: it is non-obvious that the size of a product *set* is pinned down so exactly, and this is the step that shows such a $G$ is a semidirect product.

**Sublattices and ideals in ring theory.** Replace "group" by "abelian group", $H$ and $K$ by subgroups of $(\mathbb{Z}, +)$, say $H = a\mathbb{Z}$ and $K = b\mathbb{Z}$. Then $H + K = \gcd(a,b)\mathbb{Z}$ and $H \cap K = \operatorname{lcm}(a,b)\mathbb{Z}$, and the second isomorphism theorem $(H+K)/K \cong H/(H\cap K)$ becomes a statement about the indices, recovering $\gcd(a,b)\cdot\operatorname{lcm}(a,b) = ab$. The non-obvious recognition is that this elementary number-theoretic identity is an instance of the diamond isomorphism.

**Pushing a subgroup through an arbitrary quotient.** Given any homomorphism $\psi : G \to G'$ and a subgroup $H \leq G$, set $K = \ker\psi$. The image $\psi(H)$ is $HK/K$, and the second isomorphism theorem identifies it as $H/(H\cap\ker\psi)$. This says the image of $H$ under *any* homomorphism is $H$ modulo the part of $H$ killed by the homomorphism — a non-obvious but constantly used principle for tracking subgroups across maps.

---

# Bridges

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]]** — the parent result. The second isomorphism theorem is precisely the first isomorphism theorem applied to the homomorphism $H \to G/K$, $h \mapsto hK$. It contributes no new proof technique; it packages a recurring application.

- **[[Thm - Third Isomorphism Theorem|Third Isomorphism Theorem]]** — a sibling. Both are corollaries of the first isomorphism theorem obtained by feeding it a specific natural homomorphism; the second uses inclusion-then-quotient, the third uses one quotient map between two quotients.

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]** — supplies the counting that turns the isomorphism into the product formula $|HK| = |H||K|/|H\cap K|$, and forces $H \cap K = \{e\}$ when $|H|$ and $|K|$ are coprime.

- **The product formula $|HK| = |H||K|/|H\cap K|$** — the most-used numerical corollary. It is valid as a statement about *set sizes* even when $HK$ is not a subgroup, but the second isomorphism theorem is the cleanest proof in the case it is.

- **The diamond / modular law** — the second isomorphism theorem is the isomorphism-theoretic shadow of the modular law in the subgroup lattice; the four groups $HK, H, K, H\cap K$ form a diamond, and the theorem equates its two diagonal quotients.
