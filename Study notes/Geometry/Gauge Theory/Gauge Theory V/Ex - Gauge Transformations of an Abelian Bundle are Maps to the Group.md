---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle"
  - "Def - Gauge Transformation"
  - "Def - Principal G-Bundle"
  - "Def - Adjoint Bundles ad P and Ad P"
tags: [geometry, gauge-theory]
---

# Problem Statement

Throughout, $\pi\colon P\to M$ is a smooth principal $G$-bundle: a smooth surjective submersion with a free, fibre-preserving, fibre-transitive right action of the Lie group $G$, locally trivial in the equivariant sense. The right action is written $p\cdot g$ (or $R_g(p)$). We adopt the series convention that Lie groups act on principal bundles on the **right**. The **centre** of $G$ is $Z(G)=\{z\in G:zg=gz\text{ for all }g\in G\}$. For a smooth map $g\colon M\to G$ we write $g^{-1}$ for the smooth map $m\mapsto g(m)^{-1}$ (smooth because inversion is smooth in a Lie group), and $C^\infty(M;G)$ for the group of smooth maps $M\to G$ under pointwise multiplication $(g_1g_2)(m):=g_1(m)g_2(m)$.

Prove the following three assertions.

**(a) The abelian construction and its exhaustiveness.** Suppose $G$ is abelian. Show that for every smooth map $g\colon M\to G$ the formula
$$f(p):=p\cdot g(\pi(p))\qquad(p\in P)$$
defines a gauge transformation of $P$, and that *every* gauge transformation of $P$ arises this way; the resulting correspondence $g\mapsto f$ is an isomorphism of groups
$$C^\infty(M;G)\;\xrightarrow{\ \cong\ }\;\mathcal{G}(P).$$

**(b) The non-abelian obstruction.** For a general (possibly non-abelian) $G$, show that the recipe $f(p)=p\cdot g(\pi(p))$ with $g\colon M\to G$ produces a gauge transformation **exactly** when $g$ takes its values in the centre, $g\colon M\to Z(G)$. Exhibit, over the trivial bundle $M\times SU(2)$, a gauge transformation that is *not* of the form $p\mapsto p\cdot g(\pi p)$, to show that for non-abelian $G$ the map $C^\infty(M;G)\to\mathcal{G}(P)$ of the abelian recipe is far from surjective.

**(c) The circle bundle over the circle.** Specialise to $G=U(1)=\{z\in\mathbb{C}:|z|=1\}$ and $M=S^1$. Show that for every principal $U(1)$-bundle $P\to S^1$ the gauge group is $\mathcal{G}(P)\cong C^\infty(S^1;U(1))$, and that the group of connected components $\pi_0\mathcal{G}(P)$ is infinite cyclic, the isomorphism $\pi_0\mathcal{G}(P)\cong\mathbb{Z}$ being given by the **winding number**
$$w(g):=\frac{1}{2\pi i}\oint_{S^1}g^{-1}\,dg\in\mathbb{Z}.$$

**Recall:**

The objects in play are a principal $G$-bundle, its automorphism and gauge groups, the adjoint group bundle $\operatorname{Ad}P$, and — for the fundamental identification the whole exercise rests on — the theorem describing $\mathcal{G}(P)$ as the sections of $\operatorname{Ad}P$.

![[Def - Gauge Transformation#The Definition]]

![[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle#Statement]]

For the adjoint group bundle we use the description recalled here:

![[Def - Adjoint Bundles ad P and Ad P#The Definition]]

In one sentence, $\operatorname{Ad}P:=P\times_\alpha G$ is the associated fibre bundle for the conjugation action $\alpha_g(h)=ghg^{-1}$ of $G$ on itself; its total space is $(P\times G)/G$ under $(p,h)\cdot g=(p\cdot g,\ g^{-1}hg)$, its class notation is $[p,h]$, and its fibrewise multiplication $[p,h_1]\cdot[p,h_2]:=[p,h_1h_2]$ makes each fibre a group isomorphic to $G$; a smooth section $s\in\Gamma(\operatorname{Ad}P)$ is the same datum as a smooth map $\hat f\colon P\to G$ with $\hat f(p\cdot g)=g^{-1}\hat f(p)\,g$, via $s(m)=[p,\hat f(p)]$ for any $p\in P_m$.

---

# Convergent Strategy

**Problem class.** This is an *identify-the-gauge-group* problem: three concrete descriptions of $\mathcal{G}(P)$ are to be extracted from the abstract theorem $\mathcal{G}(P)\cong\Gamma(\operatorname{Ad}P)$ by feeding it the extra hypothesis "abelian", "central-valued", or "$U(1)$ over $S^1$". The single reusable move is to write a gauge transformation $f$ through its *fibre coordinate* $\hat f\colon P\to G$, defined by $f(p)=p\cdot\hat f(p)$, and to read off what the equivariance constraint $\hat f(pg)=g^{-1}\hat f(p)g$ becomes under the added hypothesis.

**Assumption pattern.** The hypothesis "$G$ abelian" is used in exactly one way: it makes conjugation trivial, $g^{-1}\hat f(p)g=\hat f(p)$, so the equivariance constraint degenerates from "$\hat f$ is conjugation-equivariant" to "$\hat f$ is constant on fibres". A function constant on the fibres of the surjective submersion $\pi$ descends to the base — this is the recognisable trigger that turns $\hat f\colon P\to G$ into a genuine $g\colon M\to G$. For part (b), the same degeneration is asked *pointwise*: the equivariance holds for the particular $\hat f=g\circ\pi$ precisely at the points where $g$ lands in the centre.

**Theorem routing.** The route for (a) and (b) is: invoke [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|the gauge-group identification theorem]] to pass between $f$ and its fibre coordinate $\hat f$; specialise the equivariance relation using abelianness (or centrality); descend a fibre-constant map through $\pi$ using the existence of smooth local sections (a defining property of a [[Def - Principal G-Bundle|principal bundle]]). For (c), we first note conjugation is trivial for $U(1)$ so (a) applies verbatim, then classify the path components of $C^\infty(S^1;U(1))$ directly by lifting each map through the exponential covering $\mathbb{R}\to U(1)$, $\theta\mapsto e^{i\theta}$, and reading off the winding number; the answer is consistent with [[Thm - Pi_1 of S^1 is Z|the computation that π₁(S¹) ≅ ℤ]].

**Key decision point.** The one genuinely non-obvious step is *descending a fibre-constant map to the base*. It is tempting to declare "$\hat f$ constant on fibres, so $\hat f=g\circ\pi$ for a smooth $g$" without argument; but smoothness of the descended $g$ is not automatic from smoothness of $\hat f$ and must be produced from a smooth local section $s$, via $g=\hat f\circ s$. The second decision point, in (c), is recognising that the connected components of a topological group are the cosets of the identity component, so $\pi_0\mathcal{G}(P)$ is itself a group and the winding number is a *homomorphism* whose kernel is the identity component — which is why "same winding number" and "joinable by a path" coincide.

---

# Legal Operations Used

This solution deploys the following operations from [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections#Legal Operations|the topic page's Legal Operations]].

1. **Pass to the fibre coordinate of a gauge transformation.** Write $f\in\mathcal{G}(P)$ as $f(p)=p\cdot\hat f(p)$ with $\hat f\colon P\to G$ smooth; the equivariance $f(pg)=f(p)g$ is equivalent to $\hat f(pg)=g^{-1}\hat f(p)g$. This is the content of [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|the identification theorem]], invoked in every part.

2. **Collapse conjugation using abelianness or centrality.** When $G$ is abelian, or when $\hat f(p)\in Z(G)$, the relation $g^{-1}\hat f(p)g=\hat f(p)$ holds, so the conjugation-equivariance of $\hat f$ becomes plain invariance $\hat f(pg)=\hat f(p)$.

3. **Descend a fibre-constant map to the base through a local section.** A smooth $\hat f\colon P\to G$ that is constant on each fibre of $\pi$ equals $g\circ\pi$ for the unique map $g\colon M\to G$, and $g=\hat f\circ s$ for any smooth local section $s$ of $\pi$, which is smooth; the existence of such sections is part of the [[Def - Principal G-Bundle|principal-bundle definition]].

4. **Verify the four axioms of a gauge transformation directly.** For a candidate $f(p)=p\cdot g(\pi p)$: smoothness (composition through the action map), equivariance ($f(pg')=f(p)g'$), covering the identity ($\bar f=\operatorname{id}_M$), and being a diffeomorphism (explicit smooth inverse $p\mapsto p\cdot g(\pi p)^{-1}$).

5. **Classify path components of a mapping group by a homotopy invariant.** For $C^\infty(S^1;U(1))$, use the winding number, shown to be a group homomorphism to $\mathbb{Z}$ that is constant along smooth paths and separates the components, with an explicit representative $e^{in\theta}$ of each value $n$.

---

# Hints

> [!note]- Hint 1
> Every gauge transformation $f$ can be written $f(p)=p\cdot\hat f(p)$ for a unique smooth $\hat f\colon P\to G$, because the two points $f(p)$ and $p$ lie in the same fibre and $G$ acts simply transitively on fibres. The equivariance $f(pg)=f(p)g$ then becomes a constraint on $\hat f$. Compute that constraint. What does it simplify to when $G$ is abelian?

> [!note]- Hint 2
> With $G$ abelian, the constraint $\hat f(pg)=g^{-1}\hat f(p)g$ collapses to $\hat f(pg)=\hat f(p)$: the map $\hat f$ is constant on fibres. A map $M\to G$ is hiding inside it. To get it *smoothly*, do not just "quotient"; compose $\hat f$ with a smooth local section $s$ of $\pi$. Why is $\hat f\circ s$ independent of which section you chose, and why does it recover $\hat f$?

> [!note]- Hint 3
> For the converse direction of (a) and for (b), check the four defining properties of a gauge transformation for $f(p)=p\cdot g(\pi p)$ one by one. The only property that *fails* for non-abelian $G$ is equivariance: $f(pg')=pg'g(\pi p)$ but $f(p)g'=pg(\pi p)g'$, and these agree for all $g'$ if and only if $g(\pi p)$ commutes with every $g'$, i.e. $g(\pi p)\in Z(G)$.

> [!note]- Hint 4
> For (c): $U(1)$ is abelian, so (a) gives $\mathcal{G}(P)\cong C^\infty(S^1;U(1))$ with no triviality assumption on $P$ (conjugation is already trivial, so $\operatorname{Ad}P$ is the product bundle $M\times U(1)$). To classify components, lift each $g\colon S^1\to U(1)$ to a phase: parametrise $S^1$ by $\theta\in[0,2\pi]$, and observe $g^{-1}g'=i\,u$ with $u$ real. Set $\varphi(\theta)=\varphi_0+\int_0^\theta u$; then $g=e^{i\varphi}$, and periodicity forces $\varphi(2\pi)-\varphi(0)\in 2\pi\mathbb{Z}$. That integer is the winding number.

---

# Solution

The whole exercise is the single observation that a gauge transformation is a smooth choice, over $P$, of a group element to multiply by on the right — its fibre coordinate $\hat f$ — subject only to conjugation-equivariance, and that abelianness (or, pointwise, centrality) kills the conjugation and leaves a plain map to the base. Part (a) is this statement made into a group isomorphism; part (b) reads the same computation *pointwise* to locate the obstruction; part (c) takes $G=U(1)$, where the isomorphism is automatic, and counts the connected components of the resulting mapping group by lifting phases.

## Part (a): abelian gauge transformations are maps to the group

**Step 1 (construction): $f(p)=p\cdot g(\pi p)$ is a gauge transformation.**

Given a smooth $g\colon M\to G$ (with $G$ abelian), the map $f\colon P\to P$, $f(p):=p\cdot g(\pi(p))$, is a gauge transformation of $P$.

> [!note]- Derivation
> We verify the four defining properties of a gauge transformation (an equivariant diffeomorphism covering $\operatorname{id}_M$).
>
> **Smoothness.** The map $f$ is the composition
> $$P\xrightarrow{\ p\mapsto(p,\ g(\pi(p)))\ }P\times G\xrightarrow{\ (p,h)\mapsto p\cdot h\ }P,$$
> in which the first map is smooth (as $\pi$ and $g$ are smooth) and the second is the smooth right action of a [[Def - Principal G-Bundle|principal bundle]]. Hence $f$ is smooth.
>
> **Covering the identity.** For every $p$, the point $f(p)=p\cdot g(\pi p)$ lies in the same fibre as $p$, because the right action preserves fibres: $\pi(p\cdot h)=\pi(p)$ for all $h\in G$ (a defining property of the action). Therefore $\pi\circ f=\pi$, so the induced base map is $\bar f=\operatorname{id}_M$ (by uniqueness of the base map, [[Def - Gauge Transformation|Def - Gauge Transformation]]).
>
> **Equivariance.** Let $g'\in G$ and $p\in P$. Then, writing $m=\pi(p)=\pi(p\cdot g')$,
> $$f(p\cdot g')=(p\cdot g')\cdot g(\pi(p\cdot g'))=(p\cdot g')\cdot g(m)=p\cdot\big(g'\,g(m)\big)\qquad(\text{associativity of the right action}),$$
> $$f(p)\cdot g'=\big(p\cdot g(m)\big)\cdot g'=p\cdot\big(g(m)\,g'\big)\qquad(\text{associativity of the right action}).$$
> Since $G$ is **abelian**, $g'\,g(m)=g(m)\,g'$, so the two right-hand sides coincide: $f(p\cdot g')=f(p)\cdot g'$. This is the only place abelianness is used in Step 1.
>
> **Diffeomorphism.** Let $g^{-1}\colon M\to G$, $m\mapsto g(m)^{-1}$, which is smooth (inversion is smooth in $G$). Set $f'(p):=p\cdot g^{-1}(\pi p)=p\cdot g(\pi p)^{-1}$; it is smooth, being the composition of $p\mapsto(p,\ g(\pi p)^{-1})$ with the right action exactly as for $f$, and it covers $\operatorname{id}_M$ since $\pi(p\cdot g(\pi p)^{-1})=\pi(p)$ (the action preserves fibres). Smoothness of $f'$ is all that the inverse argument below requires. For every $p$, using $\pi(f(p))=\pi(p)$,
> $$f'(f(p))=f(p)\cdot g(\pi(f(p)))^{-1}=\big(p\cdot g(\pi p)\big)\cdot g(\pi p)^{-1}=p\cdot\big(g(\pi p)g(\pi p)^{-1}\big)=p\qquad(\text{associativity; }g^{-1}\text{ is the pointwise inverse}),$$
> and symmetrically $f(f'(p))=p$. Hence $f$ is a bijection with smooth inverse $f'$, i.e. a diffeomorphism.
>
> All four properties hold, so $f\in\mathcal{G}(P)$.

**Step 2 (exhaustiveness): every gauge transformation of an abelian bundle has this form.**

Conversely, if $G$ is abelian and $f\in\mathcal{G}(P)$, then $f(p)=p\cdot g(\pi p)$ for a unique smooth $g\colon M\to G$.

> [!note]- Derivation
> By [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|the identification theorem]] — recalled: *the assignment $f\mapsto\hat f$, where $\hat f\colon P\to G$ is the unique smooth map with $f(p)=p\cdot\hat f(p)$, is a bijection from $\mathcal{G}(P)$ onto the smooth conjugation-equivariant maps $\hat f(pg)=g^{-1}\hat f(p)g$* — the gauge transformation $f$ determines a smooth $\hat f\colon P\to G$ with
> $$f(p)=p\cdot\hat f(p),\qquad \hat f(p\cdot g)=g^{-1}\,\hat f(p)\,g\quad(p\in P,\ g\in G).$$
> Because $G$ is **abelian**, $g^{-1}\hat f(p)g=\hat f(p)$, so the equivariance relation becomes
> $$\hat f(p\cdot g)=\hat f(p)\qquad(p\in P,\ g\in G):$$
> $\hat f$ is constant on each fibre of $\pi$, since the $G$-action is transitive on fibres and any two points of one fibre differ by a right translation.
>
> **Descent to the base.** We produce a smooth $g\colon M\to G$ with $\hat f=g\circ\pi$. Cover $M$ by open sets $U_\alpha$ each carrying a smooth local section $s_\alpha\colon U_\alpha\to P$ (these exist by local triviality of the [[Def - Principal G-Bundle|principal bundle]]: an equivariant trivialisation $\psi_\alpha\colon\pi^{-1}(U_\alpha)\to U_\alpha\times G$ gives $s_\alpha(m):=\psi_\alpha^{-1}(m,e)$). Define $g_\alpha:=\hat f\circ s_\alpha\colon U_\alpha\to G$, which is smooth as a composition of smooth maps. For any $p\in\pi^{-1}(U_\alpha)$, write $m=\pi(p)$; then $p$ and $s_\alpha(m)$ lie in the same fibre $P_m$, so $\hat f(p)=\hat f(s_\alpha(m))=g_\alpha(m)=g_\alpha(\pi p)$ (using that $\hat f$ is fibre-constant). In particular, on an overlap $U_\alpha\cap U_\beta$ and for $m$ there, choosing $p=s_\alpha(m)$ gives $g_\alpha(m)=\hat f(s_\alpha(m))=g_\beta(m)$ (both equal $\hat f$ evaluated anywhere on $P_m$). The local pieces therefore agree on overlaps and glue to a single smooth map $g\colon M\to G$ with $g|_{U_\alpha}=g_\alpha$, and $\hat f(p)=g(\pi p)$ for all $p$. Uniqueness of $g$ is immediate from surjectivity of $\pi$: if $g_1\circ\pi=g_2\circ\pi$ then $g_1=g_2$.
>
> Substituting, $f(p)=p\cdot\hat f(p)=p\cdot g(\pi p)$, as claimed.

**Step 3 (group isomorphism): the correspondence $g\leftrightarrow f$ is an isomorphism $C^\infty(M;G)\cong\mathcal{G}(P)$.**

The map $\Psi\colon C^\infty(M;G)\to\mathcal{G}(P)$, $\Psi(g)(p):=p\cdot g(\pi p)$, is a group isomorphism (with $C^\infty(M;G)$ under pointwise multiplication and $\mathcal{G}(P)$ under composition).

> [!note]- Derivation
> Steps 1 and 2 show $\Psi$ is well defined and *bijective* (its inverse sends $f$ to the descended $g$ of Step 2). It remains to check it is a homomorphism.
>
> Take $g_1,g_2\in C^\infty(M;G)$ and $f_i:=\Psi(g_i)$. For $p\in P$ put $m=\pi p$. Using $\pi(f_2(p))=\pi(p)=m$ (Step 1, $f_2$ covers the identity),
> $$(f_1\circ f_2)(p)=f_1(f_2(p))=f_2(p)\cdot g_1(\pi(f_2(p)))=\big(p\cdot g_2(m)\big)\cdot g_1(m)=p\cdot\big(g_2(m)\,g_1(m)\big)\qquad(\text{associativity}).$$
> Because $G$ is **abelian**, $g_2(m)g_1(m)=g_1(m)g_2(m)=(g_1g_2)(m)$, so
> $$(f_1\circ f_2)(p)=p\cdot (g_1g_2)(m)=\Psi(g_1g_2)(p).$$
> Hence $\Psi(g_1)\circ\Psi(g_2)=\Psi(g_1g_2)$: the group operation on the source is pointwise multiplication, that on the target is composition, and $\Psi$ intertwines them. The identity map $\operatorname{id}_P=\Psi(\mathbf 1)$ corresponds to the constant map $\mathbf 1\colon m\mapsto e$. Therefore $\Psi$ is a group isomorphism, so
> $$C^\infty(M;G)\cong\mathcal{G}(P).$$
> (This is the abelian case of part (b) of the identification theorem, here proved from the ground up.)

## Part (b): the non-abelian obstruction

**Step 4: for general $G$, the recipe gives a gauge transformation iff $g$ is central-valued.**

For any Lie group $G$ and smooth $g\colon M\to G$, the map $f(p)=p\cdot g(\pi p)$ is a gauge transformation of $P$ if and only if $g(m)\in Z(G)$ for every $m\in M$.

> [!note]- Derivation
> Inspecting Step 1, smoothness, covering the identity, and — provided $f$ is equivariant — the diffeomorphism property (with inverse $p\mapsto p\cdot g(\pi p)^{-1}$) hold for *any* Lie group, using no commutativity. The lone requirement that used abelianness was equivariance. We isolate it.
>
> **Equivariance $\iff$ central values.** For $p\in P$, $g'\in G$, $m=\pi p$, exactly as in Step 1,
> $$f(p\cdot g')=p\cdot\big(g'\,g(m)\big),\qquad f(p)\cdot g'=p\cdot\big(g(m)\,g'\big).$$
> Because the right action is **free** (a defining property of a [[Def - Principal G-Bundle|principal bundle]]), $p\cdot a=p\cdot b$ forces $a=b$. Hence $f(p\cdot g')=f(p)\cdot g'$ holds if and only if $g'\,g(m)=g(m)\,g'$. Requiring this for *all* $g'\in G$ and all $p$ (equivalently all $m\in M$, as $\pi$ is surjective) says precisely that $g(m)$ commutes with every element of $G$, i.e.
> $$g(m)\in Z(G)\qquad\text{for all }m\in M.$$
> Conversely, if $g$ is central-valued the displayed equality holds, and then all four properties are met, so $f$ is a gauge transformation. This proves the equivalence; and it recovers part (a), since for abelian $G$ one has $Z(G)=G$ and the condition is vacuous.

**Step 5: over $M\times SU(2)$, a gauge transformation not of the recipe form.**

Take $G=SU(2)$ (so $Z(SU(2))=\{\pm\mathbf 1\}$) and the trivial bundle $P=M\times SU(2)$. There are gauge transformations of $P$ that cannot be written as $p\mapsto p\cdot g(\pi p)$ for any $g\colon M\to SU(2)$.

> [!note]- Derivation
> On the trivial bundle $P=M\times SU(2)$ the right action is $(m,h)\cdot g'=(m,hg')$. Choose any smooth $a\colon M\to SU(2)$ and define
> $$f(m,h):=(m,\ a(m)\,h)\qquad(\text{left multiplication in the fibre by }a(m)).$$
> This is a gauge transformation: it is smooth; it covers $\operatorname{id}_M$; it is equivariant, since $f((m,h)\cdot g')=f(m,hg')=(m,a(m)hg')=(m,a(m)h)\cdot g'=f(m,h)\cdot g'$ (the multiplication by $a(m)$ is on the *left* and by $g'$ on the *right*, so they never interfere, and no commutativity is needed); and it is a diffeomorphism with inverse $(m,h)\mapsto(m,a(m)^{-1}h)$.
>
> Its fibre coordinate is found from $f(m,h)=(m,h)\cdot\hat f(m,h)$, i.e. $(m,a(m)h)=(m,h\cdot\hat f(m,h))$, giving
> $$\hat f(m,h)=h^{-1}a(m)\,h.$$
> Now $f$ is of the recipe form $p\mapsto p\cdot g(\pi p)$ if and only if $\hat f(m,h)$ is independent of the fibre coordinate $h$, i.e. $h^{-1}a(m)h=a(m)$ for all $h\in SU(2)$; by Step 4 that happens exactly when $a(m)\in Z(SU(2))=\{\pm\mathbf 1\}$. So as soon as $a$ takes any value outside $\{\pm\mathbf 1\}$ — for instance the constant $a\equiv\operatorname{diag}(e^{i},e^{-i})$ — the gauge transformation $f$ is **not** of the recipe form. Thus for non-abelian $G$ the abelian recipe $C^\infty(M;G)\to\mathcal{G}(P)$ misses most of the gauge group; the honest parametrisation is the full $\Gamma(\operatorname{Ad}P)$ of the [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|identification theorem]], which over $M\times SU(2)$ is all of $C^\infty(M;SU(2))$ acting by left multiplication.

## Part (c): the gauge group of a circle bundle over the circle

**Step 6: $\mathcal{G}(P)\cong C^\infty(S^1;U(1))$ for every principal $U(1)$-bundle over $S^1$.**

For $G=U(1)$ and any principal $U(1)$-bundle $P\to S^1$, part (a) applies and gives $\mathcal{G}(P)\cong C^\infty(S^1;U(1))$.

> [!note]- Derivation
> $U(1)$ is abelian, so Steps 1–3 apply directly with $M=S^1$: $\mathcal{G}(P)\cong C^\infty(S^1;U(1))$. No hypothesis on $P$ is needed. Indeed, the reason $\operatorname{Ad}P$ played no role is that for abelian $G$ the conjugation action $\alpha_g(h)=ghg^{-1}=h$ is trivial, so $\operatorname{Ad}P=P\times_\alpha U(1)$ is the *product* group bundle $S^1\times U(1)$ (the class $[p,h]$ depends only on $\pi(p)$ and $h$), and $\Gamma(\operatorname{Ad}P)=C^\infty(S^1;U(1))$ regardless of the topology of $P$.

**Step 7: the winding number is a well-defined homomorphism $C^\infty(S^1;U(1))\to\mathbb{Z}$.**

Parametrise $S^1=\mathbb{R}/2\pi\mathbb{Z}$ by $\theta$. For $g\in C^\infty(S^1;U(1))$ the quantity
$$w(g)=\frac{1}{2\pi i}\oint_{S^1}g^{-1}\,dg=\frac{1}{2\pi i}\int_0^{2\pi}g(\theta)^{-1}g'(\theta)\,d\theta$$
is a well-defined integer, and $w\colon C^\infty(S^1;U(1))\to\mathbb{Z}$ is a group homomorphism.

> [!note]- Derivation
> **The integrand is purely imaginary.** Since $|g|=1$, we have $\overline{g}g=1$; differentiating, $\overline{g}g'+\overline{g'}g=0$, so $\overline{g}g'=-\overline{\overline{g}g'}$, i.e. $g^{-1}g'=\overline{g}g'$ is purely imaginary. Write $g^{-1}g'=i\,u$ with $u\colon[0,2\pi]\to\mathbb{R}$ smooth and $2\pi$-periodic.
>
> **Existence of a smooth phase lift.** Fix $\varphi_0\in\mathbb{R}$ with $e^{i\varphi_0}=g(0)$ and set $\varphi(\theta):=\varphi_0+\int_0^\theta u(\tau)\,d\tau$, a smooth real function. Then
> $$\frac{d}{d\theta}\big(e^{-i\varphi}g\big)=e^{-i\varphi}\big(g'-i\varphi' g\big)=e^{-i\varphi}\big(g'-i\,u\,g\big)=e^{-i\varphi}\big(g'-g\,(g^{-1}g')\big)=0\qquad(\text{since }i\,u=g^{-1}g'\text{ and }\varphi'=u),$$
> so $e^{-i\varphi}g$ is constant, equal to its value at $\theta=0$, namely $e^{-i\varphi_0}g(0)=1$. Hence $g=e^{i\varphi}$ on $[0,2\pi]$.
>
> **Integrality.** Periodicity $g(2\pi)=g(0)$ gives $e^{i\varphi(2\pi)}=e^{i\varphi(0)}$, so $\varphi(2\pi)-\varphi(0)\in2\pi\mathbb{Z}$. Therefore
> $$w(g)=\frac{1}{2\pi i}\int_0^{2\pi}i\,u\,d\theta=\frac{1}{2\pi}\int_0^{2\pi}\varphi'(\theta)\,d\theta=\frac{\varphi(2\pi)-\varphi(0)}{2\pi}\in\mathbb{Z}.$$
> The value is independent of the choice of $\varphi_0$, since changing $\varphi_0$ shifts $\varphi$ by a constant and cancels in the difference.
>
> **Homomorphism.** For $g_1,g_2\in C^\infty(S^1;U(1))$, the product rule gives $(g_1g_2)^{-1}(g_1g_2)'=g_2^{-1}g_1^{-1}(g_1'g_2+g_1g_2')=g_2^{-1}(g_1^{-1}g_1')g_2+g_2^{-1}g_2'$. As $U(1)$ is abelian and the factors are scalars, $g_2^{-1}(g_1^{-1}g_1')g_2=g_1^{-1}g_1'$, so
> $$(g_1g_2)^{-1}(g_1g_2)'=g_1^{-1}g_1'+g_2^{-1}g_2'.$$
> Integrating, $w(g_1g_2)=w(g_1)+w(g_2)$: $w$ is a homomorphism.

**Step 8: winding number separates and exhausts the path components, so $\pi_0\mathcal{G}(P)\cong\mathbb{Z}$.**

Two maps $g_0,g_1\in C^\infty(S^1;U(1))$ lie in the same smooth path component if and only if $w(g_0)=w(g_1)$, and every integer is attained; hence $\pi_0 C^\infty(S^1;U(1))\cong\mathbb{Z}$ via $w$, and by Step 6 the same holds for $\pi_0\mathcal{G}(P)$.

> [!note]- Derivation
> **$w$ is constant on smooth paths.** Let $s\mapsto g_s$ be a smooth path in $C^\infty(S^1;U(1))$ (a smooth map $[0,1]\times S^1\to U(1)$). The function $s\mapsto w(g_s)=\frac{1}{2\pi i}\int_0^{2\pi}g_s^{-1}\partial_\theta g_s\,d\theta$ is continuous in $s$ (the integrand depends continuously on $s$, uniformly in $\theta$ on the compact circle, so the integral does) and integer-valued (Step 7); a continuous integer-valued function on the connected interval $[0,1]$ is constant. Hence $w(g_0)=w(g_1)$: *same component $\Rightarrow$ equal winding number*.
>
> **Equal winding numbers are joined by a path.** Suppose $w(g_0)=w(g_1)=n$. By Step 7 write $g_j=e^{i\varphi_j}$ with smooth $\varphi_j\colon[0,2\pi]\to\mathbb{R}$ and $\varphi_j(2\pi)-\varphi_j(0)=2\pi n$ for $j=0,1$. Define, for $s\in[0,1]$,
> $$\varphi_s:=(1-s)\varphi_0+s\varphi_1,\qquad g_s:=e^{i\varphi_s}.$$
> Each $\varphi_s$ is smooth and satisfies $\varphi_s(2\pi)-\varphi_s(0)=(1-s)\,2\pi n+s\,2\pi n=2\pi n$, so $g_s(2\pi)=g_s(0)$: $g_s$ is a well-defined smooth map $S^1\to U(1)$, and $(s,\theta)\mapsto g_s(\theta)$ is smooth. This is a smooth path from $g_0$ to $g_1$. Hence *equal winding number $\Rightarrow$ same component*.
>
> **Surjectivity.** The map $e_n\colon\theta\mapsto e^{in\theta}$ has $e_n^{-1}e_n'=in$, so $w(e_n)=\frac{1}{2\pi i}\int_0^{2\pi}in\,d\theta=n$; every integer is attained.
>
> **The set of components is a group and $w$ descends to an isomorphism.** Combining the three points, $w$ induces a bijection from the set of smooth path components of $C^\infty(S^1;U(1))$ onto $\mathbb{Z}$. The set of components carries a group structure induced by pointwise multiplication: if $g_0$ is joined to $g_0'$ by a smooth path $g_0^s$ and $g_1$ to $g_1'$ by $g_1^s$, then $s\mapsto g_0^s g_1^s$ is a smooth path (pointwise multiplication $U(1)\times U(1)\to U(1)$ is smooth) joining $g_0g_1$ to $g_0'g_1'$, so the product of components $[g_0][g_1]:=[g_0g_1]$ is well defined; associativity, the identity class $[\mathbf 1]$, and inverses $[g]^{-1}=[g^{-1}]$ are inherited from $C^\infty(S^1;U(1))$. With this structure $w([g]):=w(g)$ is well defined (constant on components, by the first point) and is a homomorphism (Step 7), and it is a bijection (the first two sentences); a bijective homomorphism is an isomorphism, so $\pi_0 C^\infty(S^1;U(1))\cong\mathbb{Z}$. By Step 6 the group isomorphism $\mathcal{G}(P)\cong C^\infty(S^1;U(1))$ carries path components to path components, so
> $$\pi_0\mathcal{G}(P)\cong\mathbb{Z}.$$
> This agrees with the topological count: free homotopy classes of maps $S^1\to U(1)=S^1$ are classified by degree, and degree equals the winding number, matching [[Thm - Pi_1 of S^1 is Z|the computation π₁(S¹) ≅ ℤ]].

> [!note]- Complete formal solution
> **Claim.** Let $\pi\colon P\to M$ be a principal $G$-bundle. (a) If $G$ is abelian then $g\mapsto\big(p\mapsto p\cdot g(\pi p)\big)$ is a group isomorphism $C^\infty(M;G)\cong\mathcal{G}(P)$. (b) For general $G$, $p\mapsto p\cdot g(\pi p)$ is a gauge transformation iff $g$ is $Z(G)$-valued. (c) For $G=U(1)$, $M=S^1$, $\mathcal{G}(P)\cong C^\infty(S^1;U(1))$ and $\pi_0\mathcal{G}(P)\cong\mathbb{Z}$ via the winding number.
>
> **(a)** *Construction.* For smooth $g\colon M\to G$ and $f(p):=p\cdot g(\pi p)$: $f$ is smooth (composition of $p\mapsto(p,g(\pi p))$ with the action); $\pi\circ f=\pi$, so $\bar f=\operatorname{id}_M$; $f(pg')=p\cdot(g'g(\pi p))=p\cdot(g(\pi p)g')=f(p)g'$ using abelianness; and $p\mapsto p\cdot g(\pi p)^{-1}$ is a smooth two-sided inverse. So $f\in\mathcal{G}(P)$. *Exhaustiveness.* Given $f\in\mathcal{G}(P)$, [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|the identification theorem]] gives a unique smooth $\hat f\colon P\to G$ with $f(p)=p\cdot\hat f(p)$ and $\hat f(pg)=g^{-1}\hat f(p)g$; abelianness makes this $\hat f(pg)=\hat f(p)$, so $\hat f$ is fibre-constant. Choosing smooth local sections $s_\alpha$ of $\pi$, the maps $g_\alpha:=\hat f\circ s_\alpha$ agree on overlaps (both equal $\hat f$ on the fibre) and glue to a smooth $g\colon M\to G$ with $\hat f=g\circ\pi$; hence $f(p)=p\cdot g(\pi p)$, and $g$ is unique because $\pi$ is surjective. *Homomorphism.* $(f_1\circ f_2)(p)=f_2(p)\cdot g_1(\pi p)=p\cdot(g_2 g_1)(\pi p)=p\cdot(g_1g_2)(\pi p)$ (abelian), so composition corresponds to pointwise product; the constant $e$ corresponds to $\operatorname{id}_P$. Thus $\Psi\colon C^\infty(M;G)\to\mathcal{G}(P)$ is a group isomorphism.
>
> **(b)** Smoothness, covering $\operatorname{id}_M$, and (given equivariance) the diffeomorphism property need no commutativity. Freeness of the action makes $f(pg')=f(p)g'$ equivalent to $g'g(\pi p)=g(\pi p)g'$; demanding this for all $g'\in G$ and all $p$ is exactly $g(m)\in Z(G)$ for all $m$. Over $M\times SU(2)$, $f(m,h)=(m,a(m)h)$ for any smooth $a$ is a gauge transformation with fibre coordinate $\hat f(m,h)=h^{-1}a(m)h$; it is of the recipe form iff $a(m)\in Z(SU(2))=\{\pm\mathbf 1\}$ for all $m$, so an $a$ with a value outside $\{\pm\mathbf 1\}$ gives a gauge transformation not of the recipe form.
>
> **(c)** $U(1)$ abelian $\Rightarrow$ (a) gives $\mathcal{G}(P)\cong C^\infty(S^1;U(1))$ (and $\operatorname{Ad}P=S^1\times U(1)$). For $g\in C^\infty(S^1;U(1))$, $g^{-1}g'$ is purely imaginary ($|g|=1$); the smooth lift $\varphi(\theta)=\varphi_0+\int_0^\theta(-i)g^{-1}g'$ satisfies $g=e^{i\varphi}$, and periodicity gives $\varphi(2\pi)-\varphi(0)=2\pi w(g)$ with $w(g)=\frac{1}{2\pi i}\oint g^{-1}dg\in\mathbb{Z}$. The identity $(g_1g_2)^{-1}(g_1g_2)'=g_1^{-1}g_1'+g_2^{-1}g_2'$ makes $w$ a homomorphism to $\mathbb{Z}$; it is continuous in $g$ (hence constant on smooth paths, being integer-valued), the linear phase homotopy $e^{i((1-s)\varphi_0+s\varphi_1)}$ joins any two maps of equal winding number, and $w(e^{in\theta})=n$. Therefore $w$ induces a group isomorphism $\pi_0 C^\infty(S^1;U(1))\cong\mathbb{Z}$, so $\pi_0\mathcal{G}(P)\cong\mathbb{Z}$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "$\hat f$ is fibre-constant, so it *is* a smooth map on $M$"
> In Step 2 it is tempting to conclude the descended $g$ is smooth for free, from "$\hat f$ constant on fibres". Set-theoretically $\hat f$ does factor as $g\circ\pi$; but the smooth structure on $M$ is the quotient structure of $\pi$, and a continuous map out of a quotient is smooth only when it pulls back to a smooth map — which is the *hypothesis*, not the *conclusion*. The correct move is to exhibit $g$ locally as $\hat f\circ s_\alpha$ for a smooth section $s_\alpha$; this manufactures the smoothness. The shortcut becomes legal precisely when one has a smooth local section to compose with, which is exactly what a principal bundle guarantees.

---

# Key Takeaways

**A gauge transformation is a smooth right-multiplication field, and its constraint is conjugation-equivariance; every structural computation about $\mathcal{G}(P)$ is a computation about that constraint.** The reusable principle is to *always* replace $f\in\mathcal{G}(P)$ by its fibre coordinate $\hat f\colon P\to G$, $f(p)=p\cdot\hat f(p)$, and to translate whatever hypothesis is in force into a statement about $\hat f(pg)=g^{-1}\hat f(p)g$. Abelianness collapses the conjugation to the identity, turning $\hat f$ into a plain map $M\to G$; centrality does the same pointwise; a representation $\rho$ turns it into $\rho\circ\hat f$ (the next exercise). The trigger to reach for this device is any question of the form "describe/parametrise/count the gauge transformations of a bundle with extra structure": pass to $\hat f$, impose the structure, and read off the answer. The diagnostic that you are using it correctly is that the equivariance relation is the *only* thing you ever manipulate.

**The abelian recipe $C^\infty(M;G)\to\mathcal{G}(P)$ is an isomorphism exactly to the extent that $G$ is abelian, and its failure is measured by the centre.** This is worth internalising as a sharp boundary: for abelian $G$ the gauge group is the mapping group $C^\infty(M;G)$, a comfortable object; for non-abelian $G$ it is $\Gamma(\operatorname{Ad}P)$, genuinely a space of *sections of a nontrivial group bundle*, and the subgroup one can name by base maps $M\to G$ (right multiplication) shrinks to $C^\infty(M;Z(G))$. The lesson for later moduli theory is that non-abelian gauge groups are "twisted" — one cannot trivialise them by a map to the group — and this twisting is the origin of the interesting topology of $\mathcal{B}=\mathcal{A}/\mathcal{G}$. When a problem quietly assumes the gauge group is $C^\infty(M;G)$, check whether $G$ is abelian; if it is not, that assumption is only correct for the central part, and using it for all gauge transformations is the error illustrated in Step 5.

**Counting the components of a gauge group is counting a homotopy invariant of a mapping space, and for $C^\infty(S^1;U(1))$ that invariant is the winding number — the same integer that is degree and that computes $\pi_1(S^1)$.** The transferable technique is: to find $\pi_0$ of a group of maps, produce a homomorphism to a discrete group that is (i) computable by an integral or a lift, (ii) locally constant / homotopy invariant, and (iii) surjective with explicit representatives, then argue that its kernel is exactly the identity component by connecting equal-invariant maps with an explicit homotopy. Here the explicit homotopy is the *linear interpolation of phases* $e^{i((1-s)\varphi_0+s\varphi_1)}$, which is legitimate only because equal winding numbers make the two phase functions share the same $2\pi n$ jump, so the interpolation stays periodic. This winding-number machine reappears throughout gauge theory: it is the degree that labels $U(1)$-bundles over surfaces, the instanton number that labels $SU(2)$-connections over $S^4$, and the reason large gauge transformations (those in a nontrivial component) act nontrivially on the Chern–Simons functional. A companion drill in the same section, [[Ex - The Gauge Group Homomorphism from a Representation and its Infinitesimal Version]], carries the same fibre-coordinate technique to the non-abelian setting of induced gauge maps.
