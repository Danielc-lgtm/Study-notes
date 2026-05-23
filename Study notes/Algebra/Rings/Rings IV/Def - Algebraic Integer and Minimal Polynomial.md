---
type: definition
subject: ring-theory
prereqs:
  - "Def - Polynomial Ring"
  - "Def - Ring Homomorphism"
  - "Def - Ideal"
  - "Def - Quotient Ring"
  - "Def - Integral Domain"
  - "Def - Irreducible and Prime Elements"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $\mathbb{C}$ is the field of complex numbers and $\mathbb{Z}[X]$ the [[Def - Polynomial Ring|polynomial ring]] over the integers — polynomials $g = c_0 + c_1 X + \cdots + c_n X^n$ with every coefficient $c_i \in \mathbb{Z}$. A polynomial is **monic** if its top coefficient $c_n$ is $1$. For a fixed $\alpha \in \mathbb{C}$, the **evaluation map** is the [[Def - Ring Homomorphism|ring homomorphism]] $\varphi : \mathbb{Z}[X] \to \mathbb{C}$, $\;g \mapsto g(\alpha)$, which substitutes $\alpha$ for $X$. Its image is written $\mathbb{Z}[\alpha]$ and its kernel $I = \ker \varphi$. We write $f_\alpha$ for the minimal polynomial of $\alpha$ and $(f_\alpha)$ for the [[Def - Ideal|ideal]] it generates. The symbol $\cong$ denotes ring isomorphism, and $\mathbb{Z}[X]/(f_\alpha)$ is the [[Def - Quotient Ring|quotient ring]]. The two compound notions defined here — *algebraic integer* and its *minimal polynomial* — are the foundation of §2.7; the full chapter symbol registry is on [[Rings IV — §2.7–2.8]].

---

# Axiom Motivation

Start from a concrete wish. The integers $\mathbb{Z}$ are the basic objects of arithmetic, but they are not closed under the operations we care about: solving polynomial equations. The number $i$ is not an integer, yet it satisfies $i^2 + 1 = 0$ — an equation as clean and integral as anything in $\mathbb{Z}$. The number $\sqrt{2}$ satisfies $X^2 - 2 = 0$. We would like a notion of "integer" wide enough to admit these — a class of complex numbers that behaves like $\mathbb{Z}$, supports a sensible factorisation theory, and forms a [[Def - Ring|ring]] — without simply admitting *all* of $\mathbb{C}$, which has no arithmetic of divisibility at all.

So the design question is: which complex numbers deserve to be called integers? The instinct "roots of polynomials with integer coefficients" is close but, as stated, far too generous. The number $\tfrac{1}{2}$ is a root of $2X - 1 \in \mathbb{Z}[X]$; the number $\tfrac{1}{3}$ is a root of $3X - 1$. If every root of an integer polynomial counted, every rational number would be an "integer", and the notion would collapse — $\mathbb{Q}$ is a field, it has no interesting divisibility, and we would have learned nothing. The defect is visible: the polynomial $2X - 1$ has a *leading coefficient* $2$ that is not $1$. That leading coefficient is exactly the denominator that $\tfrac12$ smuggles in. A root of $c_n X^n + \cdots$ is, by the formula, roughly a thing divided by $c_n$; allowing $c_n \neq 1$ allows division, and division is what we want to forbid.

The fix is to demand the polynomial be **monic** — leading coefficient $1$. This is the whole definition: an algebraic integer is a root of a *monic* polynomial in $\mathbb{Z}[X]$. Monic is precisely the condition "no denominator is being introduced by the leading term". Test it against the desiderata. It admits $i$ ($X^2 + 1$ is monic) and $\sqrt2$ ($X^2 - 2$ is monic) — good, those are the things we wanted. It excludes $\tfrac12$: a moment's thought (or [[Thm - Rational Algebraic Integers are Integers|the theorem that rational algebraic integers are integers]]) shows no monic integer polynomial has $\tfrac12$ as a root. So monic is the knob that separates "genuine integers" from "fractions in disguise".

What breaks if we weaken "monic" — say to "leading coefficient $\pm 1$"? Nothing, in fact: $\pm 1$ are units, and $-X^2 + 1$ and $X^2 - 1$ have the same roots, so allowing leading coefficient $-1$ changes no roots. But what breaks if we weaken further, to "leading coefficient any non-zero integer"? Everything: as shown, every rational becomes an algebraic integer, and the class is no longer a meaningful [[Def - Subring|subring]]. What breaks if we *strengthen*, demanding the polynomial be linear and monic, $X - n$? Then we recover exactly $\mathbb{Z}$ and gain nothing — $i$ and $\sqrt2$ are lost. The monic condition with arbitrary degree is the unique sweet spot: degree gives room to capture $i, \sqrt2, \sqrt[3]{5}, \ldots$, while monicity blocks the denominators.

The minimal polynomial is the second half of the definition, and it answers a different need. Once $\alpha$ is known to satisfy *some* monic integer polynomial, it satisfies infinitely many — multiply by anything. We want the *canonical* one: a single polynomial that records exactly the integer-polynomial relations $\alpha$ obeys. The set of all $g \in \mathbb{Z}[X]$ with $g(\alpha) = 0$ is the kernel $I$ of the evaluation homomorphism $\varphi$, and kernels of ring [[Def - Homomorphism|homomorphisms]] are [[Def - Ideal|ideals]]. So the relations form an [[Def - Ideal|ideal]], and the canonical polynomial should be a *generator* of that ideal. The non-trivial fact — [[Thm - The Minimal Polynomial Generates the Kernel Ideal|proved separately]], because $\mathbb{Z}[X]$ is not a principal ideal domain — is that this ideal is principal: $I = (f_\alpha)$ for a single monic $f_\alpha$. Defining $f_\alpha$ as *the* monic generator of $I$ makes it unique (a principal ideal in a domain has a generator unique up to a unit, and monicity pins the unit). And because $\mathbb{Z}[X]/(f_\alpha) \cong \mathbb{Z}[\alpha]$ sits inside the [[Def - Integral Domain|domain]] $\mathbb{C}$, the quotient is a domain, so $(f_\alpha)$ is a prime ideal and $f_\alpha$ is [[Def - Irreducible and Prime Elements|irreducible]]. Irreducibility is not an extra axiom we impose — it falls out, and it is the feature that makes $f_\alpha$ the right notion of "the equation $\alpha$ truly satisfies".

---

# The Definition

**Algebraic integer.** A complex number $\alpha \in \mathbb{C}$ is an **algebraic integer** if it is a root of some monic polynomial with integer coefficients: there exists a monic
$$f = X^n + c_{n-1}X^{n-1} + \cdots + c_1 X + c_0 \in \mathbb{Z}[X], \qquad c_0, \dots, c_{n-1} \in \mathbb{Z},$$
such that $f(\alpha) = 0$.

For an algebraic integer $\alpha$, write $\mathbb{Z}[\alpha]$ for the smallest subring of $\mathbb{C}$ containing $\alpha$. It is the image of the evaluation [[Def - Ring Homomorphism|homomorphism]] $\varphi : \mathbb{Z}[X] \to \mathbb{C}$, $g \mapsto g(\alpha)$, and by the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]],
$$\mathbb{Z}[\alpha] = \operatorname{im}\varphi \;\cong\; \mathbb{Z}[X]/I, \qquad I = \ker\varphi = \{\, g \in \mathbb{Z}[X] : g(\alpha) = 0 \,\}.$$
The hypothesis "$\alpha$ is an algebraic integer" is exactly the statement that $I \neq \{0\}$ — that $\alpha$ satisfies a *monic* integer-polynomial relation, not merely a non-zero one.

**Minimal polynomial.** Let $\alpha \in \mathbb{C}$ be an algebraic integer. The ideal $I = \ker\varphi$ is principal (a [[Thm - The Minimal Polynomial Generates the Kernel Ideal|non-trivial theorem]], since $\mathbb{Z}[X]$ is *not* a principal ideal domain), and among its generators there is a unique monic one. The **minimal polynomial of $\alpha$**, written $f_\alpha$, is this unique monic generator:
$$I = \ker\varphi = (f_\alpha), \qquad f_\alpha \text{ monic}.$$
Equivalently, $f_\alpha$ is a monic polynomial of least degree in $I$ — a monic integer polynomial of smallest degree satisfied by $\alpha$. The polynomial $f_\alpha$ is automatically [[Def - Irreducible and Prime Elements|irreducible]] in $\mathbb{Z}[X]$, and
$$\mathbb{Z}[\alpha] \;\cong\; \mathbb{Z}[X]/(f_\alpha).$$

---

# Relate to Other Fields / Compression

The phrase "algebraic integer" is one half of a deliberate pair, and it is illuminated by its sibling. A complex number is an **algebraic number** if it is a root of *any* non-zero polynomial in $\mathbb{Q}[X]$ — equivalently, in $\mathbb{Z}[X]$, leading coefficient unrestricted. Every algebraic integer is an algebraic number; the converse fails, and $\tfrac12$ is the witness. So:
$$\text{algebraic integer} \;=\; \text{algebraic number} \;+\; \text{the defining polynomial may be taken monic}.$$
This is exactly the relationship $\mathbb{Z}$ bears to $\mathbb{Q}$, lifted one level up. Inside $\mathbb{Q}$, the integers are the rationals "with no denominator"; inside the algebraic numbers, the algebraic integers are those "with no denominator". The monic condition *is* the no-denominator condition, made precise. This analogy is not loose: [[Thm - Rational Algebraic Integers are Integers|the theorem that a rational algebraic integer is an ordinary integer]] says the new notion, restricted to $\mathbb{Q}$, gives back exactly $\mathbb{Z}$ — the lift is consistent with the original.

The construction $\mathbb{Z}[\alpha] \cong \mathbb{Z}[X]/(f_\alpha)$ is itself a compression worth naming. It says: *to adjoin an algebraic integer to $\mathbb{Z}$ is to quotient the polynomial ring by the relations that element satisfies.* This is the universal pattern of "presenting a ring by generators and relations" — $\mathbb{Z}[X]$ is the free commutative ring on one generator over $\mathbb{Z}$, and $(f_\alpha)$ is the single relation. The same pattern builds $\mathbb{C} = \mathbb{R}[X]/(X^2+1)$, builds every finitely generated algebra, and is the ring-theoretic shadow of how a field extension $F[X]/(f)$ is constructed in Galois theory. The minimal polynomial is the relation; the quotient is the ring it cuts out.

The countability remark gives one more compression. There are only countably many polynomials in $\mathbb{Z}[X]$ (each is a finite tuple of integers), each with finitely many roots, so there are only **countably many algebraic integers** — indeed only countably many algebraic *numbers*. Since $\mathbb{C}$ is uncountable, "almost every" complex number is neither. The algebraic integers are a thin, arithmetic skeleton inside the continuum, and a number like $\pi$ or $e$ — *transcendental*, satisfying no polynomial relation at all — is the generic case, not the exception.

---

# Examples / Corollaries

**Is an algebraic integer — $\alpha = i$.** Here $i$ is a root of $X^2 + 1 \in \mathbb{Z}[X]$, which is monic, so $i$ is an algebraic integer with minimal polynomial $f_i = X^2 + 1$. (It is the minimal polynomial and not merely *a* monic polynomial satisfied by $i$ because $i \notin \mathbb{Q}$, so no degree-$1$ monic integer polynomial $X - n$ vanishes at $i$; degree $2$ is least.) The quotient description reads $\mathbb{Z}[i] \cong \mathbb{Z}[X]/(X^2+1)$ — the Gaussian integers presented as polynomials modulo $X^2 = -1$.

**Is an algebraic integer — $\alpha = \sqrt{2}$.** A root of the monic $X^2 - 2 \in \mathbb{Z}[X]$, so $\sqrt2$ is an algebraic integer with $f_{\sqrt2} = X^2 - 2$, and $\mathbb{Z}[\sqrt2] \cong \mathbb{Z}[X]/(X^2-2)$. Again degree $2$ is minimal since $\sqrt2$ is irrational.

**Is an algebraic integer — $\alpha = \tfrac{1}{2}(1 + \sqrt{-3})$.** This is the surprising one, because $\alpha$ wears a denominator $2$ on its sleeve. Yet compute: $2\alpha - 1 = \sqrt{-3}$, so $(2\alpha-1)^2 = -3$, giving $4\alpha^2 - 4\alpha + 1 = -3$, i.e. $4\alpha^2 - 4\alpha + 4 = 0$, i.e.
$$\alpha^2 - \alpha + 1 = 0.$$
So $\alpha$ is a root of the **monic** polynomial $X^2 - X + 1 \in \mathbb{Z}[X]$, and $f_\alpha = X^2 - X + 1$. The visible denominator was an illusion — it cancels against the cross term. The lesson: monicity of the defining polynomial is a real, checkable condition, and it can hold even when $\alpha$ does not "look like" an integer. (This $\alpha$ is a primitive sixth root of unity; such numbers generate the ring of integers of $\mathbb{Q}(\sqrt{-3})$.)

**Is NOT an algebraic integer — $\alpha = \tfrac{1}{2}$.** The number $\tfrac12$ *is* an algebraic number: it is the root of $2X - 1 \in \mathbb{Z}[X]$. But $2X - 1$ is not monic, and the claim is that *no* monic integer polynomial vanishes at $\tfrac12$. If $f(\tfrac12) = 0$ for monic $f$, then $\tfrac12 \in \mathbb{Q}$ would be a rational algebraic integer, hence — by [[Thm - Rational Algebraic Integers are Integers|the theorem]] — an ordinary integer, which $\tfrac12$ is not. So $\tfrac12$ is the canonical *non*-example: algebraic, but not an algebraic integer. It is exactly the kind of "fraction in disguise" that the monic condition was designed to exclude.

**Is NOT an algebraic integer (indeed not algebraic) — $\alpha = \pi$.** No non-zero polynomial in $\mathbb{Z}[X]$ has $\pi$ as a root; $\pi$ is *transcendental*. Here the evaluation map $\varphi : \mathbb{Z}[X] \to \mathbb{C}$, $g \mapsto g(\pi)$ is *injective*, so $\ker\varphi = \{0\}$ and there is no minimal polynomial at all. This is the generic situation in $\mathbb{C}$.

**Corollary — only countably many algebraic integers exist.** The set $\mathbb{Z}[X]$ is countable (a polynomial is a finite list of integers), and each non-zero polynomial has finitely many complex roots. A countable union of finite sets is countable, so the algebraic integers form a countable subset of the uncountable $\mathbb{C}$. If you can see why this argument also bounds the algebraic *numbers* — same proof, monicity never used — you have understood that the algebraic integers are a sparse skeleton in $\mathbb{C}$.

**Corollary — $\mathbb{Z}[\alpha]$ is an integral domain, and $f_\alpha$ is irreducible.** Since $\mathbb{Z}[\alpha]$ is a subring of the field $\mathbb{C}$, it inherits the absence of zero divisors: it is an [[Def - Integral Domain|integral domain]]. Through the isomorphism $\mathbb{Z}[X]/(f_\alpha) \cong \mathbb{Z}[\alpha]$, the quotient is a domain, so $(f_\alpha)$ is a prime ideal and $f_\alpha$ is a prime — hence [[Def - Irreducible and Prime Elements|irreducible]] — element of $\mathbb{Z}[X]$. This is a calibration check: if you can run it, you see that irreducibility of $f_\alpha$ is forced by the geometry ($\alpha$ lives in a field) and is not an independent stipulation.

**Calibration check.** Confirm that $\sqrt[3]{5}$ is an algebraic integer with $f = X^3 - 5$, and that the golden ratio $\tfrac12(1+\sqrt5)$ is an algebraic integer with $f = X^2 - X - 1$ (compute as in example three). Confirm that $\tfrac13$ and $\tfrac{1}{\sqrt2}$ are *not* algebraic integers — both are rational or would force a rational algebraic integer that is not in $\mathbb{Z}$. Finally, explain why "$\alpha$ is an algebraic integer" is the same statement as "$\ker(\varphi: \mathbb{Z}[X]\to\mathbb{C})$ contains a monic polynomial": if you can articulate that, the definition and its kernel reformulation have fused into one idea.

---

# Unlocked by This

> [!tip] The Minimal Polynomial Generates the Kernel Ideal *(from this topic)*
> The definition of $f_\alpha$ as *the* monic generator of $\ker\varphi$ presupposes that $\ker\varphi$ is principal. That is [[Thm - The Minimal Polynomial Generates the Kernel Ideal|a theorem]] — non-trivial because $\mathbb{Z}[X]$ is not a principal ideal domain — and it is what makes "the minimal polynomial" well defined.

> [!tip] Rational Algebraic Integers are Integers *(from this topic)*
> The non-example $\tfrac12$ is justified by [[Thm - Rational Algebraic Integers are Integers|the theorem]] that an algebraic integer lying in $\mathbb{Q}$ already lies in $\mathbb{Z}$ — the statement that $\mathbb{Z}$ is integrally closed in $\mathbb{Q}$.

> [!tip] The Algebraic Integers Form a Ring *(from Algebraic Number Theory)*
> Although it is far from obvious — given monic $f, g$ with $f(\alpha) = g(\beta) = 0$ there is no easy monic polynomial vanishing at $\alpha + \beta$ — the algebraic integers are closed under addition and multiplication, forming a subring $\overline{\mathbb{Z}} \subseteq \mathbb{C}$. The proof routes through finitely generated modules.

> [!tip] Rings of Integers and Dedekind Domains *(from Algebraic Number Theory)*
> Intersecting the algebraic integers with a number field $K$ gives its **ring of integers** $\mathcal{O}_K$ — for $K = \mathbb{Q}(i)$ this is $\mathbb{Z}[i]$, for $K = \mathbb{Q}(\sqrt{-3})$ it is $\mathbb{Z}[\tfrac12(1+\sqrt{-3})]$. These rings need not be unique factorisation domains, and repairing factorisation by passing to *ideals* is the subject of Dedekind domains.
