# Positional Uncertainty


### 5.1. Overview

Positional uncertainty presents a fundamental challenge in nanomechanical engineering, determining many design decisions and limiting the range of workable systems. Positional uncertainty in compliant systems is a result of both thermal motion and quantum mechanical uncertainty, but thermal motion proves more important in almost all mechanical systems at room temperature. This chapter describes positional uncertainty in a set of structures characterized by a PES with a single potential well.

Section 5.2 discusses the concept of positional uncertainty and its importance in engineering. Section 5.3 presents classical and quantum mechanical analyses of displacements in thermally excited harmonic oscillators; Section 5.4 and 5.5 present similar analyses of longitudinal and transverse displacements in rods. These studies of elastic systems provide the basis for describing positional uncertainty in the structures considered in later chapters. Indeed, for analyzing mechanical systems at room temperature, Eq. (5.4) usually provides an adequate approximation. In practice, the rest of the discussion in these sections chiefly serves to quantify the errors in using Eq. (5.4), to show why its range of applicability is greater than its derivation would suggest (Section 5.8.1), and to provide more elaborate expressions that remain accurate at lower temperatures.

The following two sections discuss systems in which positional uncertainty results from fluctuations in entropic springs. The prototype of an entropic spring is a loaded piston in a gas-filled cylinder, analyzed from three perspectives in Section 5.6. A flexible, tensioned rod in a housing that subjects it to transverse elastic restoring forces is a more complex system, but provides a good description of devices useful in nanomechanical signal transmission; this is analyzed in Section 5.7. These results on entropic springs, though useful in analytical work of the sort presented in Part II, are not applied to any of the specific systems described there.

### 5.2. Positional uncertainty in engineering

In the design of nanomechanical systems, positional uncertainties stemming from thermal excitation and quantum mechanical principles are a fundamental concern. On the scale of conventional mechanical engineering, neither quantum
uncertainties nor thermal excitations are significant; the closest macroscale analogues of these effects arise in systems excited by broad-band acoustic noise, yet issues arise there (e.g., fatigue and damping) that are alien to the molecular domain. Molecules are not subject to fatigue (for a more precise discussion, see Section 6.7.1a). Damping, which degrades mechanical energy to heat, cannot degrade the vibrations of heat itself.

In an engineering context, problems involving positional uncertainty can frequently be formulated in terms of a probability density function (PDF) for a coordinate describing a part of a system. Mechanical designs typically require that each part should, under specified conditions, occupy a particular position at a particular time to within specified tolerances. Errors occur at some finite rate owing to the finite probability mass in the tail of the PDF that extends beyond the tolerance band. Good approximations to the positional PDFs of typical systems are thus of fundamental value in nanomechanical engineering.

### 5.3. Thermally excited harmonic oscillators

Many parts of nanomechanical systems are adequately approximated by linear models, in which restoring forces are proportional to displacements. The prototype of such systems is the harmonic oscillator, consisting of a single mass with a single degree of freedom subject to a linear restoring force (measured by the stiffness $k_{\mathrm{s}}$ ). Analytical results for the simple harmonic oscillator can be adapted and extended to systems with multiple degrees of freedom, as in the subsequent discussion of rods with internal vibrational modes.

### 5.3.1. Classical treatment

In classical statistical mechanics, the probability density function for the position coordinate $x$ of a particle subject to the potential energy function $\mathscr{V}(x)$ is [from Eq. (4.10)]

$$
\begin{equation*}
f_{x}(x)=\exp [-\mathscr{V}(x) / k T] / \int_{-\infty}^{\infty} \exp [-\mathscr{V}(x) / k T] d x \tag{5.1}
\end{equation*}
$$

For the harmonic potential,

$$
\begin{equation*}
\mathcal{V}(x)=\frac{1}{2} k_{\mathrm{s}} x^{2} \tag{5.2}
\end{equation*}
$$

the resulting probability density function is Gaussian:

$$
\begin{align*}
f_{x}(x) & =\frac{\exp \left(-k_{\mathrm{s}} x^{2} / 2 k T\right)}{\int_{-\infty}^{\infty} \exp \left(-k_{\mathrm{s}} x^{2} / 2 k T\right) d x}=\frac{\exp \left(-k_{\mathrm{s}} x^{2} / 2 k T\right)}{\sqrt{2 \pi}} \sqrt{\frac{k_{\mathrm{s}}}{k T}}  \tag{5.3}\\
& =\frac{1}{\sqrt{2 \pi} \sigma_{\text {class }}} \exp \left(-x^{2} / 2 \sigma_{\text {class }}^{2}\right)
\end{align*}
$$

yielding the classical value for the positional variance (= standard deviation squared = mean square displacement):

$$
\begin{equation*}
\sigma_{\text {class }}^{2}=k T / k_{\mathrm{s}} \tag{5.4}
\end{equation*}
$$

This relationship has broader applicability than its derivation may suggest.

a. The irrelevance of external bombardment. The probability density function for the position and velocity of a harmonic oscillator is independent of the nature of its coupling to the surrounding thermal bath. This may occur through vibration of its attachment point, through absorption and emission of thermal radiation, or through bombardment by molecules in a surrounding gas. None of these influences alters the potential energy function, hence none alters the Boltzmann distribution for the oscillator.

This may seem counterintuitive, given a mental image of the dynamical effects of molecular bombardment. At equilibrium, however, an impinging gas molecule is as likely to absorb energy as to deliver it, and so molecular bombardment has no net effect on the amplitude of vibration. How a system is coupled to a thermal bath can affect its detailed dynamics (e.g., the smoothness or irregularity of its trajectory, the decay time for oscillations of unusual amplitude, etc.), but not the statistical distribution of dynamical quantities. This principle holds true for systems in general, and makes the study of positional uncertainty dependent only on potential energy functions.

### 5.3.2. Quantum mechanical treatment

In quantum statistical mechanics, the classical integral over $x$ (more generally, an integral over phase space, yielding a probability density function for both position and momentum) is replaced by a sum, and the probability density function is replaced by a probability distribution over a series of states $i$ :

$$
\begin{equation*}
P(i)=\exp [-\mathscr{E}(i) / k T] / \sum_{i=0}^{\infty} \exp [-\mathscr{E}(i) / k T] \tag{5.5}
\end{equation*}
$$

From elementary quantum mechanics, the vibrational states $n=0,1,2,3, \ldots$ of a harmonic oscillator have energies that depend on the frequency

$$
\begin{equation*}
\mathscr{E}(n)=\left(n+\frac{1}{2}\right) \hbar \omega ; \quad \omega=\sqrt{k_{\mathrm{s}} / m} \tag{5.6}
\end{equation*}
$$

The probability of finding the oscillator in vibrational state $n$ is

$$
\begin{equation*}
P(n)=\exp \left[-\left(n+\frac{1}{2}\right) \hbar \omega / k T\right] / \sum_{n=0}^{\infty} \exp \left[-\left(n+\frac{1}{2}\right) \hbar \omega / k T\right] \tag{5.7}
\end{equation*}
$$

Rearranging and summing the series,

$$
\begin{gather*}
P(n)=\exp (-n \hbar \omega / k T) / \sum_{n=0}^{\infty}[\exp (-\hbar \omega / k T)]^{n}  \tag{5.8}\\
\sum_{n=0}^{\infty} y^{n}=1+\frac{y}{1-y}, \quad|y|<1  \tag{5.9}\\
P(n)=\exp (-n \hbar \omega / k T)[1-\exp (-\hbar \omega / k T)] \tag{5.10}
\end{gather*}
$$

The variance (mean square displacement) of the oscillator can be derived from its mean energy:

$$
\begin{equation*}
\overline{\mathscr{E}}=\sum_{n=0}^{\infty} P(n) \mathscr{E}_{n}=\sum_{n=0}^{\infty} \exp \left(-n \frac{\hbar \omega}{k T}\right)\left[1-\exp \left(-\frac{\hbar \omega}{k T}\right)\right]\left(n+\frac{1}{2}\right) \hbar \omega \tag{5.11}
\end{equation*}
$$

Rearranging and summing both series,

$$
\begin{gather*}
\overline{\mathscr{E}}=\hbar \omega\left[1-\exp \left(-\frac{\hbar \omega}{k T}\right)\right]\left\{\frac{1}{2} \sum_{n=0}^{\infty}\left[\exp \left(-\frac{\hbar \omega}{k T}\right)\right]^{n}+\sum_{n=0}^{\infty} n\left[\exp \left(-\frac{\hbar \omega}{k T}\right)\right]^{n}\right\}  \tag{5.12}\\
\sum_{n=0}^{\infty} n y^{n}=\frac{y}{(1-y)^{2}}, \quad y<1  \tag{5.13}\\
\overline{\mathscr{E}}=\hbar \omega\left\{\frac{1}{2}+[\exp (\hbar \omega / k T)-1]^{-1}\right\} \tag{5.14}
\end{gather*}
$$

In a harmonic oscillator, the total energy equals twice the mean potential energy, which is proportional to the mean square displacement:

$$
\begin{gather*}
\frac{1}{2} \overline{\mathscr{E}}=\overline{\mathscr{V}}=\frac{1}{2} k_{\mathrm{s}} \overline{x^{2}}=\frac{1}{2} k_{\mathrm{s}} \sigma^{2}  \tag{5.15}\\
\sigma^{2}=\frac{\hbar \omega}{k_{\mathrm{s}}}\left\{\frac{1}{2}+[\exp (\hbar \omega / k T)-1]^{-1}\right\} \tag{5.16}
\end{gather*}
$$

Describing the frequency in terms of the fundamental mechanical parameters and then rearranging yields an equation between dimensionless quantities (see Figure 5.1):

$$
\begin{equation*}
\sigma^{2} \frac{\sqrt{k_{\mathrm{s}} m}}{\hbar}=\frac{1}{2}+[\exp (\hbar \omega / k T)-1]^{-1} \tag{5.17}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-30.jpg?height=743&width=1086&top_left_y=1394&top_left_x=188)

Figure 5.1. A dimensionless measure of variance vs. a dimensionless measure of temperature, Eq. (5.17).

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-31.jpg?height=745&width=1100&top_left_y=163&top_left_x=268)

Figure 5.2. The ratio of the actual variance to that predicted by a classical model, vs. a dimensionless measure of temperature, Eq. (5.18).

It often is desirable to determine whether the classical approximation is adequate for describing positional uncertainties in a system of engineering interest. A useful measure is the ratio of the total to the classical variance, which equals the ratio of the total to the classical energy:

$$
\begin{equation*}
\frac{\sigma^{2}}{\sigma_{\text {class }}^{2}}=\frac{\hbar \omega}{k T}\left\{\frac{1}{2}+[\exp (\hbar \omega / k T)-1]^{-1}\right\}=\frac{\overline{\mathscr{E}}}{k T} \tag{5.18}
\end{equation*}
$$

This function of the parameter $k T / \hbar \omega$ is graphed in Figure 5.2; where $k T / \hbar \omega$ substantially exceeds unity, the classical variance provides a good approximation.

With less elegance (but more immediately accessible physical significance), these dimensionless quantities can be unfolded into a set of graphs of root mean square displacement $(\sigma)$ as a function of temperature, spring constant, and mass (Figure 5.3). For perspective, note that the stiffness of nonbonded interactions between atoms at their equilibrium separation typically is about $0.1 \mathrm{~N} / \mathrm{m}$; that of covalent bond angle-bending, about $30 \mathrm{~N} / \mathrm{m}$; and that of covalent bond stretching, about $400 \mathrm{~N} / \mathrm{m}$. Many small components in nanomechanisms have masses in the hundreds to thousands of daltons.

### 5.4. Elastic extension of thermally excited rods

Various molecular structures resemble rods; these include DNA helices, microtubules, ladder polymers, and several classes of nanomechanical components. Even flexible molecular chains resemble rods (for purposes of the present analysis) when held in an extended conformation by longitudinal tension or by lateral constraints. A rod is the simplest example of an extended object and can serve as a model for various mechanical systems.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-32.jpg?height=1361&width=1112&top_left_y=178&top_left_x=185)

Figure 5.3. This set of graphs plots the logarithm of the root mean square displacement of harmonic oscillators of varying mass and spring constant as a function of temperature, from Eq. (5.16). Note that the length at the top of the graphs corresponds roughly to an atomic diameter. Above the dashed lines, the classical approximation is accurate to within $10 \%$; above the dotted lines, it is accurate to within $1 \%$. (continued)

A rod clamped at one end and free at the other undergoes both transverse and longitudinal vibrations. This section analyzes the positional variance of the free end resulting from longitudinal vibrational modes; in rods of large aspect ratio, transverse vibrations can make a significant contribution to the longitudinal positional variance of the free end (analyzed in Section 5.6). The following first considers a classical model for a continuous elastic rod, then both an approximate and an exact quantum mechanical model for a rod consisting of a series of identical masses and springs, ending with an empirical approximation to this exact model.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-33.jpg?height=1341&width=1090&top_left_y=188&top_left_x=285)

Figure 5.3. (continued) A $1 \mathrm{~nm}^{3}$ volume containing 1000 daltons has $\rho \approx 1661 \mathrm{~kg} / \mathrm{m}^{3}$.

### 5.4.1. Classical continuum treatment

A uniform rod of length $\ell$ clamped at one end and free at the other supports longitudinal vibrational modes $(n=0,1,2,3, \ldots)$ with wavelengths

$$
\begin{equation*}
\lambda_{n}=\frac{4 \ell}{2 n+1} \tag{5.19}
\end{equation*}
$$

The speed of sound $v_{\mathrm{s}}$ in the rod can be calculated from the linear modulus $E_{\ell}$ and linear density $\rho_{\ell}$ yielding the modal frequencies $\omega_{n}$.

$$
\begin{equation*}
v_{\mathrm{s}}=\sqrt{E_{\ell} / \rho_{\ell}} ; \quad \omega_{0}=\frac{\pi}{2 \ell} \sqrt{E_{\ell} / \rho_{\ell}} ; \quad \omega_{n}=\omega_{0}(2 n+1) \tag{5.20}
\end{equation*}
$$

Each longitudinal mode can be regarded as a harmonic oscillator with a certain frequency, ${ }^{\circ}$ effective stiffness, and ${ }^{\circ}$ effective mass. The effective stiffness relates the square of the amplitude (at the rod end, where the variance is to be
computed) to the potential energy at maximum displacement during a vibrational cycle, which equals the maximum kinetic energy:

$$
\begin{align*}
\frac{1}{2} k_{n} A_{n}^{2} & =\max (\mathcal{V})=\max (\mathscr{T}) \\
& =\int_{0}^{\ell} \frac{1}{2} \rho_{\ell}[v(x)]^{2} d x \\
& =\int_{0}^{\ell} \frac{1}{2} \rho_{\ell}\left(\omega_{n} A_{n}\right)^{2} \sin ^{2}\left[\frac{(2 n+1)}{2 \ell} \pi x\right] d x \\
& =\frac{1}{4} \rho_{\ell} \ell\left(\omega_{n} A_{n}\right)^{2} \tag{5.21}
\end{align*}
$$

This yields the effective stiffness $k_{n}$ of mode $n$ :

$$
\begin{equation*}
k_{n}=\frac{E_{\ell}}{\ell} \frac{\pi^{2}}{8}(2 n+1)^{2} \tag{5.22}
\end{equation*}
$$

Combining this with the classical expression for positional variance in a harmonic oscillator as a function of temperature and stiffness, Eq. (5.4), the positional variance at the free end associated with mode $n$ is:

$$
\begin{equation*}
\sigma_{n, \text { class }}^{2}=k T \frac{\ell}{E_{\ell}} \frac{8}{\pi^{2}} \frac{1}{(2 n+1)^{2}} \tag{5.23}
\end{equation*}
$$

The total variance is the sum of the modal variances:

$$
\begin{equation*}
\sigma_{\text {class }}^{2}=\sum_{n=0}^{\infty} \sigma_{n, \text { class }}^{2}=k T \frac{\ell}{E_{\ell}} \frac{8}{\pi^{2}} \sum_{n=0}^{\infty} \frac{1}{(2 n+1)^{2}} \tag{5.24}
\end{equation*}
$$

Applying the identity

$$
\begin{equation*}
\sum_{n=0}^{\infty} \frac{1}{(2 n+1)^{2}}=\frac{\pi^{2}}{8} \tag{5.25}
\end{equation*}
$$

yields the classical variance in the position of the free end for a rod of uniformly distributed mass and elasticity:

$$
\begin{equation*}
\sigma_{\text {class }}^{2}=k T \ell / E_{\ell} \tag{5.26}
\end{equation*}
$$

This is exactly $k T / k_{\mathrm{s}}$, where $k_{\mathrm{s}}$ is the stretching stiffness of the rod as a whole. This is the variance for a simple harmonic oscillator of the same stiffness, and hence of a "rod" having a single mass and a single mode-the opposite extreme from a rod of uniformly distributed mass and elasticity. The significance of this equality is discussed in Section 5.8.1.

### 5.4.2. Quantum mechanical treatments

a. Discrete rod models. For a continuous rod, a quantum mechanical treatment yields a divergent series for the positional variance, owing to the zero-point vibrations of an infinity of high-frequency modes; the continuum model is thus unacceptable even as an approximation. The following will work with a more realistic rod model (Figure 5.4) consisting of a series of $N$ identical springs and masses, supporting $N$ longitudinal vibrational modes. Introducing complexities

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-35.jpg?height=244&width=735&top_left_y=177&top_left_x=496)

Figure 5.4. Diagram of a discrete rod, showing masses, springs, and the length coordinate (measuring between atomic centers).

such as differing masses would alter the detailed dynamics of rod vibrations, but would usually have little effect on the positional variance. More drastic, however, is the approximation that entire planes of atoms perpendicular to the rod axis can be lumped together and treated as single masses, neglecting the degrees of freedom introduced by the physical extent and flexibility of each plane.

A limiting-case analysis illustrates the essential physics. In one case (Figure 5.5), the atoms in each plane are tightly coupled to one another, each plane shares a single longitudinal degree of freedom, and the approximation under consideration is correct (by construction). In the other limiting case, a "rod" consists of an uncoupled bundle of $j$ component rods, each one atom wide and $m$ atoms long; this increases the total number of modes is by a factor of $j$. If a component rod has a positional standard deviation $\sigma_{c}$, then the position of the end of the bundle (interpreted as the mean position of the component ends) has a standard deviation

$$
\begin{equation*}
\sigma_{\mathrm{b}}=\sigma_{\mathrm{c}} / \sqrt{j} \tag{5.27}
\end{equation*}
$$

and the variance of the bundle end position is thus inversely proportional to $j$. As we will see, this is exactly the variance that results from treating the bundle as a single unit with $N=m$, hence the uncoupled and the tightly coupled results are identical. $N$ may thus be taken as the number of atomic planes along the length of the rod; a conservatively generous estimate (given that real interatomic spacings are greater than $0.1 \mathrm{~nm}$ ) is

$$
\begin{equation*}
N=10^{10} \ell \quad \text { (for } \ell \text { in meters) } \tag{5.28}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-35.jpg?height=379&width=1001&top_left_y=1726&top_left_x=349)

Figure 5.5. Limiting-case rods. Part (a) diagrams a rod in the limiting case in which masses and spring constants are lumped on a plane-by-plane basis; (b) diagrams the limiting case in which the rod is treated as a bundle of decoupled simple rods.

b. Semicontinuum quantum mechanical approximation. A simple approximation to a discrete system uses the continuum results but truncates the sum of the modal variances at $n=N-1$. The continuum expressions for the modal effective stiffnesses and frequencies, together with Eq. (5.17), yield the positional variance associated with mode $n$ in the continuum approximation:

$$
\begin{equation*}
\sigma_{n}^{2} \frac{\sqrt{E_{\ell} \rho_{\ell}}}{\hbar}=\frac{4}{\pi(2 n+1)}\left\{\frac{1}{2}+\left[\exp \left(\frac{\hbar \omega_{0}}{k T}(2 n+1)\right)-1\right]^{-1}\right\} \tag{5.29}
\end{equation*}
$$

Summing over the $N$ modes in a discrete rod yields the semicontinuum approximation to the total positional variance of the free end of a clamped rod:

$$
\begin{equation*}
\sigma^{2} \frac{\sqrt{E_{\ell} \rho_{\ell}}}{\hbar}=\sum_{n=0}^{N-1} \frac{4}{\pi(2 n+1)}\left\{\frac{1}{2}+\left[\exp \left(\frac{\hbar \omega_{0}}{k T}(2 n+1)\right)-1\right]^{-1}\right\} \tag{5.30}
\end{equation*}
$$

c. Exact quantum mechanical treatment. The simple model above has serious defects when vibrational wavelengths approach the interatomic spacing of the $\operatorname{rod}\left(\lambda \approx d_{\mathrm{a}}\right)$, because the dispersive wave-propagation characteristics of the discrete structure become important. These effects are large for the single mode of a "rod" with $N=1$, and continue to be large for a substantial fraction of the modes in rods where $N \gg 1$. Defining the discrete-mass variables in terms of the continuum variables,

$$
\begin{equation*}
d_{\mathrm{a}}=\frac{\ell}{N} ; \quad m_{\mathrm{a}}=\frac{\ell \rho_{\ell}}{N} ; \quad k_{\mathrm{s}}=\frac{E_{\ell} N}{\ell} \tag{5.31}
\end{equation*}
$$

Keeping the intuitive definition of the rod length as the distance from the attachment point to the last mass,

$$
\begin{equation*}
\lambda_{n}=\frac{4 \ell}{(2 n+1)}\left(1+\frac{1}{2 N}\right) \tag{5.32}
\end{equation*}
$$

The correct, dispersive relationship of frequency to wavelength (Ashcroft and Mermin, 1976) is

$$
\begin{equation*}
\omega_{n}=2 \sqrt{\frac{k_{\mathrm{s}}}{m_{\mathrm{a}}}} \sin \left(\frac{\pi d}{\lambda_{n}}\right)=\frac{2}{\ell} \sqrt{\frac{E_{\ell}}{\rho_{\ell}}} N \sin \left(\frac{2 n+1}{2 N+1} \frac{\pi}{2}\right) \tag{5.33}
\end{equation*}
$$

The effective mass $m_{n}$ of a mode $n$ is the sum over the (equal) masses of the square of the local modal amplitude, divided by the square of the modal amplitude at the free end of the rod:

$$
\begin{equation*}
m_{n}=m_{\mathrm{a}}\left[\sin ^{2}\left(\frac{2 n+1}{2 N+1} \pi N\right)\right]^{-1} \sum_{i=1}^{N} \sin ^{2}\left(\frac{2 n+1}{2 N+1} \pi i\right) \tag{5.34}
\end{equation*}
$$

which simplifies to

$$
\begin{equation*}
m_{n}=\rho_{\ell} \ell\left[\sin ^{2}\left(\frac{2 n+1}{2 N+1} \pi N\right)\right]^{-1}\left(\frac{1}{2}+\frac{1}{4 N}\right) \tag{5.35}
\end{equation*}
$$

Given Eq. (5.16) and the above values for frequency and effective mass, the modal variance

$$
\begin{equation*}
\sigma_{n}^{2}=\frac{\hbar}{m_{n} \omega_{n}}\left\{\frac{1}{2}+\left[\exp \left(\frac{\hbar \omega_{n}}{k T}\right)-1\right]^{-1}\right\} \tag{5.36}
\end{equation*}
$$

which leads to the following dimensionless expression for the exact total variance expressed in terms of $\omega_{0}$ (the frequency of the fundamental mode given by the continuum approximation):

$$
\begin{align*}
\sigma^{2} \frac{\sqrt{E_{\ell} \rho_{\ell}}}{\hbar}=\frac{2}{2 N+1} \sum_{n=0}^{N-1} & {\left[\sin ^{2}\left(\frac{2 n+1}{2 N+1} \pi N\right) / \sin \left(\frac{2 n+1}{2 N+1} \frac{\pi}{2}\right)\right.}  \tag{5.37}\\
& \left.\times\left(\frac{1}{2}+\left\{\exp \left[\frac{4 N}{\pi}\left(\frac{\hbar \omega_{0}}{k T}\right) \sin \left(\frac{2 n+1}{2 N+1} \frac{\pi}{2}\right)\right]-1\right\}^{-1}\right)\right]
\end{align*}
$$

This equation is graphed in Figure 5.6; note that the result for $n=0$, while identical to that given for the harmonic oscillator in Figure 5.1, is shifted to the left on this graph by the expression of results in terms of $\omega_{0}$ [Eq. (5.20)] rather than in terms of the true frequency $\omega$.

Note that division of a rod into $j$ component rods with

$$
\begin{equation*}
E_{\ell}^{\prime}=E_{\ell} / j ; \quad \rho_{\ell}^{\prime}=\rho_{\ell} / j \tag{5.38}
\end{equation*}
$$

yields

$$
\begin{equation*}
\sigma^{\prime}=\sigma \sqrt{j} \tag{5.39}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-37.jpg?height=808&width=1087&top_left_y=1321&top_left_x=320)

Figure 5.6. A dimensionless measure of variance vs. a dimensionless measure of temperature, for rods supporting varying numbers of longitudinal modes, Eq. (5.37).

and the standard deviation of the bundle end position (i.e., of the mean displacement of the component ends) is

$$
\begin{equation*}
\sigma_{\mathrm{b}}=\sqrt{j \sigma^{\prime 2}} / j=\sigma \tag{5.40}
\end{equation*}
$$

d. An engineering approximation. For engineering purposes, it is advantageous to have a simple analytical expression rather than a sum over a variable number of terms. In seeking such an expression, we can begin with the relatively simple semicontinuum approximation, Eq. (5.30). This sum can be rearranged into two terms

$$
\begin{equation*}
\sigma^{2} \frac{\sqrt{E_{\ell} \rho_{\ell}}}{\hbar}=\frac{2}{\pi} \sum_{n=0}^{N-1}(2 n+1)^{-1}+\frac{4}{\pi} \sum_{n=0}^{N-1}\left((2 n+1)\left\{\exp \left[\frac{\hbar \omega_{0}}{k T}(2 n+1)\right]-1\right\}\right)^{-1} \tag{5.41}
\end{equation*}
$$

and the second term, which dominates in the classical limit, can be simplified by considering the classical limit $\left(\hbar \omega_{0} / k T \ll 1\right)$ :

$$
\begin{equation*}
\sigma^{2} \frac{\sqrt{E_{\ell} \rho_{\ell}}}{\hbar}=\frac{2}{\pi} \sum_{n=0}^{N-1}(2 n+1)^{-1}+\frac{4}{\pi} \frac{k T}{\hbar \omega_{0}} \sum_{n=0}^{N-1}(2 n+1)^{-2} \tag{5.42}
\end{equation*}
$$

The first, logarithmically divergent sum can be replaced by an integral approximation corrected by a constant. Summing the second series to $N=\infty$ yields a simple expression (also transformed to eliminate $\omega_{0}$ ) exhibiting better classical-limit behavior than the original expression:

$$
\begin{equation*}
\sigma^{2}=\frac{\hbar}{\pi \sqrt{E_{\ell} \rho_{\ell}}}[0.54+\log (2 N+1)]+k T \frac{\ell}{E_{\ell}} \tag{5.43}
\end{equation*}
$$

This expression is accurate in the classical limit $\left(\hbar \omega_{0} / k T \rightarrow 0\right)$, and provides a good approximation in the quantum limit $\left(k T / \hbar \omega_{0} \rightarrow 0\right)$. Its deviations are strictly in a conservative direction (overestimating variance), but can amount to tens of percent for values of $k T / \hbar \omega_{0} \approx 1$. A similar expression giving a more accurate result in this middle range can be obtained by multiplying the classical term by an empirically chosen function:

$$
\begin{equation*}
\sigma^{2}=\frac{\hbar[0.54+\log (2 N+1)]}{\pi \sqrt{E_{\ell} \rho_{\ell}}}+k T \frac{\ell}{E_{\ell}} \exp \left[-\left(0.7-\frac{0.39}{\sqrt{N}}\right) \frac{\pi \hbar}{2 \ell k T} \sqrt{\frac{E_{\ell}}{\rho_{\ell}}}\right] \tag{5.44}
\end{equation*}
$$

Figure 5.7 compares the results of these two approximations to the results given by Eq. (5.37). Both are shown to give conservative estimates of the variance, and the latter equation is shown to give estimates that are within a few percent of the correct values. It can serve as an adequate approximation for most engineering purposes.

Figures 5.8 and 5.9 plot quantum mechanical variances in forms that are useful for making quick estimates. Figure 5.8 plots positional standard deviations for rods with diamondlike properties at $300 \mathrm{~K}$; Figure 5.9 plots ratios of quantum to classical results for a range of properties and temperatures.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-39.jpg?height=832&width=1100&top_left_y=163&top_left_x=309)

Figure 5.7. A plot of exact variances as in Figure 5.6, with the approximations of Eqs. (5.43) and (5.44) shown for comparison.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-39.jpg?height=649&width=1105&top_left_y=1200&top_left_x=306)

Figure 5.8. Standard deviation in elastic longitudinal displacement for the end of a thermally excited rod, plotted vs. diameter and length, assuming mechanical properties like those of bulk diamond $\left(\rho=3500 \mathrm{~kg} / \mathrm{m}^{3}, E=10^{12} \mathrm{~N} / \mathrm{m}^{2}\right), N / \ell=10^{10} \mathrm{~m}^{-1}$, and $T=$ 300 K. Entropic effects, neglected here, are included in Figure 5.16. Note that quantum effects make a major contribution to the positional uncertainty only for $\ell \leq 1 \mathrm{~nm}$. At sufficiently small dimensions, neglect of atomic-scale structural detail becomes unacceptable even as an approximation (e.g., the dark gray region to the left describes nonexistent subatomic diameters); at larger dimensions, this approximation is excellent.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-40.jpg?height=1621&width=1124&top_left_y=166&top_left_x=207)

Figure 5.9. A plot of ratios of exact [Eq. (5.37)] to classical [Eq. (5.26)] variances. The final graph in the sequence assumes an unrealistically high acoustic speed $(40 \mathrm{~km} / \mathrm{s}$, vs. $\sim 17 \mathrm{~km} / \mathrm{s}$ for diamond), and thus represents an upper bound on the magnitude of quantum effects in real structures under familiar physical conditions.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-41.jpg?height=1616&width=1107&top_left_y=169&top_left_x=305)

Figure 5.9. (Continued)

### 5.5. Elastic bending of thermally excited rods

The analysis of the transverse positional variance resulting from transverse vibrational modes substantially parallels the longitudinal case. The following first considers a classical model for a continuous elastic rod, then a semicontinuum quantum mechanical model, a fit to the continuum limit of this model, and a conservative approximation to the combined effects of bending and ${ }^{\circ}$ shear deformation.

### 5.5.1. Classical treatment

a. Continuum model. Knowledge of modal frequencies and modal effective masses suffices to characterize the system. Following Timoshenko et al. (1974), the bending vibrations in a plane of symmetry of a uniform rod clamped at one end and free at the other (i.e., of a cantilever beam) have normal modes with shapes described by

$$
\begin{equation*}
\mathrm{y}_{n}(x)=C_{1} \sin \left(\kappa_{n} x\right)+C_{2} \cos \left(\kappa_{n} x\right)+C_{3} \sinh \left(\kappa_{n} x\right)+C_{4} \cosh \left(\kappa_{n} x\right) \tag{5.45}
\end{equation*}
$$

where $y(x)$ is the transverse displacement from the equilibrium position at point $x$. The constants $C_{1}, C_{2}, C_{3}$, and $C_{4}$ are determined by boundary and normalization conditions. The boundary conditions require that

$$
\begin{equation*}
\cos \mathscr{R}_{n} \cosh \mathscr{R}_{n}=-1 ; \quad \mathscr{R}_{n}=\kappa_{n} \ell \approx\left(n+\frac{1}{2}\right) \pi \tag{5.46}
\end{equation*}
$$

and the modal frequencies are given by the relationship

$$
\begin{equation*}
\omega_{n}=\left(\mathscr{R}_{n} / \ell\right)^{2} \sqrt{k_{\mathrm{b}} / \rho_{\ell}} \tag{5.47}
\end{equation*}
$$

where $k_{\mathrm{b}}$ is the bending stiffness of the $\operatorname{rod}$ in $\mathrm{J} \cdot \mathrm{m} / \mathrm{rad}^{2}$, and the elastic energy per unit length resulting from bending

$$
\begin{equation*}
\frac{\partial \mathscr{E}_{\mathrm{b}}}{\partial x}=\frac{1}{2} k_{\mathrm{b}}\left(\frac{\partial^{2} y}{\partial x^{2}}\right)^{2} \tag{5.48}
\end{equation*}
$$

The modal effective mass (taking the free-end displacement as the generalized position coordinate) can be found by integrating the square of the local normalized amplitude [requiring $y(\ell)=1$ ] with respect to the mass:

$$
\begin{align*}
A & =\left(\cos \mathscr{R}_{n}+\cosh \mathscr{R}_{n}\right)\left[\cos \left(\mathscr{R}_{n} x / \ell\right)-\cosh \left(\mathscr{R}_{n} x / \ell\right)\right] \\
B & =\left(\sin \mathscr{R}_{n}-\sinh \mathscr{R}_{n}\right)\left[\sin \left(\mathscr{R}_{n} x / \ell\right)-\sinh \left(\mathscr{R}_{n} x / \ell\right)\right] \\
m_{n} & =\int_{0}^{\ell} \frac{(A+B)^{2}}{\left(\sin \mathscr{R}_{n} \sinh \mathscr{R}_{n}\right)^{2}} \rho_{\ell} d x=\frac{\rho_{\ell} \ell}{4} \tag{5.49}
\end{align*}
$$

for all values of $n$. The modal frequency and the modal effective mass define the modal effective transverse stiffness resulting from bending

$$
\begin{equation*}
k_{\mathrm{t}, \mathrm{b}, n}=\frac{k_{\mathrm{b}}}{4 \ell^{3}} \mathscr{R}_{n}^{4} \tag{5.50}
\end{equation*}
$$

which (as in the longitudinal analysis) yields an expression for the total classical transverse variance resulting from bending ${ }^{\circ}$ compliance:

$$
\begin{equation*}
\sigma_{\mathrm{t}, \mathrm{b}, \mathrm{class}}^{2}=4 k T \frac{\ell^{3}}{k_{\mathrm{b}}} \sum_{n=0}^{\infty} \frac{1}{\mathscr{R}_{n}^{4}} \tag{5.51}
\end{equation*}
$$

Applying the identity

$$
\begin{equation*}
\sum_{n=0}^{\infty} \frac{1}{\mathscr{R}_{n}^{4}}=\frac{1}{12} \tag{5.52}
\end{equation*}
$$

yields the classical expression for the transverse variance in the position of the free end of a rod of uniformly distributed mass and bending stiffness, neglecting compliance owing to shear and the effects of discreteness (see Section 5.5.1b):

$$
\begin{equation*}
\sigma_{\mathrm{t}, \mathrm{b}, \mathrm{class}}^{2}=k T \ell^{3} / 3 k_{\mathrm{b}} \tag{5.53}
\end{equation*}
$$

But elementary theory of flexure shows that the bending stiffness of the end of a continuum cantilever rod is

$$
\begin{equation*}
k_{\mathrm{t}, \mathrm{b}}=3 k_{\mathrm{b}} / \ell^{3} \tag{5.54}
\end{equation*}
$$

hence the classical variance is simply $k T / k_{\mathrm{t}, \mathrm{b}}$. As in the longitudinal case, the vibrational modes prove irrelevant to the classical analysis (see Section 5.4.1); knowledge of the overall stiffness suffices.

For a tube, the bending stiffness is

$$
\begin{equation*}
k_{\mathrm{b}}=E \frac{\pi}{4}\left(r_{2}^{4}-r_{1}^{4}\right) \tag{5.55}
\end{equation*}
$$

and the transverse stiffness at the far end of an anchored tube is

$$
\begin{equation*}
k_{\mathrm{t}, \mathrm{b}}=E \frac{3 \pi}{4 \ell^{3}}\left(r_{2}^{4}-r_{1}^{4}\right) \tag{5.56}
\end{equation*}
$$

where $r_{1}$ and $r_{2}$ are the inner and outer tube radii, and $E$ is ${ }^{\circ}$ Young's modulus.

b. Discrete model. In bending (unlike stretching) the transition from a continuum to a lumped system changes the overall stiffness (not merely the modal stiffnesses). For a rod considered as a series of masses and angular springs, as shown in Figure 5.10, the rod-bending stiffness is related to the intermass spacings and angular stiffnesses:

$$
\begin{equation*}
k_{\mathrm{b}}=k_{\theta} d_{\mathrm{a}} \tag{5.57}
\end{equation*}
$$

For rods in which the number of segments, $N$, is finite, the compliance of the rod can be described as the sum of contributions from a series of bending joints

$$
\begin{equation*}
\frac{1}{k_{\mathrm{t}, \mathrm{b}}}=\frac{\ell^{3}}{k_{\mathrm{b}}} \sum_{n=0}^{N-1} \frac{1}{N}\left(1-\frac{n}{N}\right)^{2} \approx \frac{\ell^{3}}{k_{\mathrm{b}}}\left(\frac{3 N+4}{9 N-2}\right) \tag{5.58}
\end{equation*}
$$

where the approximation is exact for $N=1,2$, and $\infty$; for intermediate values it is always high (i.e., conservative) and in error by less than $1 \%$.

The preceding analysis takes account of transverse compliance caused by bending, but rods of multiatom width also exhibit compliance through shear.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-43.jpg?height=234&width=692&top_left_y=1909&top_left_x=522)

Figure 5.10. A discrete rod, illustrating the angles entering into calculations of bending stiffness effects.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-44.jpg?height=408&width=760&top_left_y=187&top_left_x=397)

Figure 5.11. Modal deformation in pure bending (a) vs. pure shear (b). Bending dominates in high aspect-ratio rods; shear dominates in rods of low aspect ratio. Both deformations are here shown in idealized form.

For typical materials, shear makes a substantial contribution to the total transverse compliance, $k_{\mathrm{t}}$, when rod diameter $d \approx \ell$; in vibration, it has significant effects on modal shapes and stiffnesses when $d$ is of the same order as the associated wavelength. Figure 5.11 illustrates normal modes from pure bending (zero shear compliance) and pure shear (zero bending compliance) for $n=2$, with the idealization that plane cross sections remain plane despite shear. A standard engineering approximation treats shear as an independent, additive source of compliance, with transverse stiffness effects from shear taking the same analytical form as longitudinal stiffness effects but substituting the (linear) shear modulus $G_{\ell}$ for the (linear) stretching modulus $E_{\ell}$. Combining the resulting shear compliance, $1 / k_{\mathrm{t}, \mathrm{s}}=\ell / G_{\ell}$, with Eq. (5.58) yields the engineering approximation:

$$
\begin{equation*}
\sigma_{\mathrm{t}, \text { class }}^{2}=k T\left[\frac{\ell^{3}}{k_{\mathrm{b}}}\left(\frac{3 N+4}{9 N-2}\right)+\frac{\ell}{G_{\ell}}\right] \tag{5.59}
\end{equation*}
$$

Aside from quantum corrections, this approximation breaks down when $\ell / d$ becomes small, yet bending compliance remains important. In this regime, outof-plane deformation of the free surface becomes a significant source of additional compliance. To treat objects of such low aspect-ratio as rods is, at best, a crude approximation.

### 5.5.2. Semicontinuum quantum mechanical treatment

The preceding classical treatment can serve as the basis for a quantum mechanical analysis. As in the earlier analysis of longitudinal vibrations, use of the continuum approximation neglects the dispersive properties of a discrete medium, which become significant as the characteristic wavelengths of normal modes approach interatomic distances. As will be seen, however, zero-point vibrations in the higher transverse modes (unlike those of the higher longitudinal modes) make only a modest contribution to the positional variance. Accordingly, dispersion is neglected in the following analysis; this neglect should have little effect for $N \geq 10$.

We begin with a model including only the effects of bending compliance, deferring discussion of shear compliance. (Figure 5.11 illustrates the difference between these forms of compliance.) The above values of modal effective mass

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-45.jpg?height=820&width=1087&top_left_y=164&top_left_x=320)

Figure 5.12. Dimensionless transverse variance for rods, neglecting shear compliance. The simple approximation is based on Eq. (5.64); the exponential-factor approximation on Eq. (5.65), and the exact semicontinuum sum on Eq. (5.60).

and effective stiffness yield the semicontinuum approximation to the transverse bending variance for a uniform rod. In dimensionless terms analogous to those of the longitudinal-mode analysis:

$$
\begin{equation*}
\sigma_{\mathrm{t}, \mathrm{b}}^{2} \frac{\sqrt{k_{b} \rho_{\ell}}}{\hbar \ell}=\sum_{n=0}^{N-1} \frac{4}{\mathscr{R}_{n}^{2}}\left(\frac{1}{2}+\left\{\exp \left[\frac{\hbar \omega_{0}}{k T}\left(\frac{\mathscr{R}_{n}}{\mathscr{R}_{0}}\right)^{2}\right]-1\right\}^{-1}\right) \tag{5.60}
\end{equation*}
$$

(see Figure 5.12).

### 5.5.3. Engineering approximations

Expressing the variance directly,

$$
\begin{equation*}
\sigma_{\mathrm{t}, \mathrm{b}}^{2}=\frac{\hbar \ell}{\sqrt{k_{b} \rho_{\ell}}} \sum_{n=0}^{N-1} \frac{4}{\mathscr{R}_{n}^{2}}\left\{\frac{1}{2}+\left[\exp \left(\frac{\hbar}{k T} \frac{\mathscr{R}_{n}^{2}}{\ell^{2}} \sqrt{\frac{k_{b}}{\rho_{\ell}}}\right)-1\right]^{-1}\right\} \tag{5.61}
\end{equation*}
$$

Multiplying out and taking the classical limit of the second term yields

$$
\begin{equation*}
\sigma_{\mathrm{t}, \mathrm{b}}^{2}=\frac{\hbar \ell}{\sqrt{k_{b} \rho_{\ell}}} \sum_{n=0}^{N-1} \frac{2}{\mathscr{R}_{n}^{2}}+\sum_{n=0}^{N-1} \frac{4}{\mathscr{R}_{n}^{4}} k T \frac{\ell^{3}}{k_{b}} \tag{5.62}
\end{equation*}
$$

In the limit of large $N$, the second term yields the classical continuum result, and may be replaced by the modified classical expression derived above to take account of the reduced bending stiffness of discrete rods where $N$ is small. For the first term (describing zero-point contributions to the variance) solving the
equation that defines values of $\mathscr{R}_{n}$ yields the convergent series

$$
\begin{equation*}
\sum_{n=0}^{\infty} \frac{2}{\mathscr{R}_{n}^{2}}=0.5688+0.0908+0.0324+0.0165+\cdots \approx 0.7588 \tag{5.63}
\end{equation*}
$$

Substituting the infinite series limit yields the approximation

$$
\begin{equation*}
\sigma_{\mathrm{t}, \mathrm{b}}^{2}=0.76 \frac{\hbar \ell}{\sqrt{k_{b} \rho_{\ell}}}+k T \frac{\ell^{3}}{k_{\mathrm{b}}}\left(\frac{3 N+4}{9 N-2}\right) \tag{5.64}
\end{equation*}
$$

Given the size of the first term in the above series and the shortcomings of the continuum model for rods of low $N$, it is useful to consider the case $N=1$. In a rod consisting of a single mass and a single point of bending, the continuum model overestimates the effective stiffness by a factor of three and underestimates the effective mass by a factor of four, making its estimate of the quantum mechanical positional variance conservative by a factor of $(4 / 3)^{1 / 2} \approx 1.15$.

This approximation, like that of Eq. (5.43), significantly overestimates the positional variance in the transition region between the quantum and classical limits (Figure 5.12). A more accurate result for the important case of large $N$ may be obtained by evaluating the limit of the original sum, Eq. (5.60), as $N \rightarrow \infty$ and fitting an empirical expression to the results:

$$
\begin{equation*}
\sigma_{\mathrm{t}, \mathrm{b}}^{2}=0.76 \frac{\hbar \ell}{\sqrt{k_{b} \rho_{\ell}}}+k T \frac{\ell^{3}}{3 k_{\mathrm{b}}} \exp \left(-\frac{1.97}{\ell^{2}} \sqrt{\frac{k_{\mathrm{b}}}{\rho_{\ell}}} \frac{\hbar}{k T}\right) \tag{5.65}
\end{equation*}
$$

This approximation is always high, but never by more than $1 \%$. Figure 5.12 compares these approximations to Eq. (5.60).

### 5.5.4. Shear and bending in the quantum limit

The approximations developed for longitudinal positional variance, Eq. (5.43) and Eq. (5.44), have direct analogs for the positional variance that would occur in hypothetical rods having shear but no bending compliance. The more accurate of the two takes the form

$$
\begin{equation*}
\sigma_{\mathrm{t}, \mathrm{s}}^{2}=\frac{\hbar[0.54+\log (2 N+1)]}{\pi \sqrt{G_{\ell} \rho_{\ell}}}+k T \frac{\ell}{G_{\ell}} \exp \left[-\left(0.7-\frac{0.39}{\sqrt{N}}\right) \frac{\pi \hbar}{2 \ell k T} \sqrt{\frac{G_{\ell}}{\rho_{\ell}}}\right] \tag{5.66}
\end{equation*}
$$

In the classical limit, the effects of bending and shear compliance are simply additive, yielding expressions like Eq. (5.59). In the quantum limit, effective modal masses and frequencies play a role, and a precise analysis would have to include the effects of bending and shear on a mode-by-mode basis. An upper bound on their combined effect can be had more simply. Consider the variance of a harmonic oscillator in the quantum limit

$$
\begin{equation*}
\sigma^{2}=\hbar /\left(2 \sqrt{k_{\mathrm{s}} m}\right) \tag{5.67}
\end{equation*}
$$

If we consider its stiffness to have two sources, $k_{\mathrm{s} 1}$ and $k_{\mathrm{s} 2}$, the variance becomes

$$
\begin{equation*}
\sigma^{2}=\frac{\hbar}{2 \sqrt{m}} \sqrt{k_{\mathrm{s} 1}^{-1}+k_{\mathrm{s} 2}^{-1}} \tag{5.68}
\end{equation*}
$$

The expression

$$
\begin{equation*}
\sigma_{\text {est }}^{2}=\sigma_{1}^{2}+\sigma_{2}^{2}=\frac{\hbar}{2 \sqrt{k_{\mathrm{s} 1} m}}+\frac{\hbar}{2 \sqrt{k_{\mathrm{s} 2} m}} \tag{5.69}
\end{equation*}
$$

overestimates the actual variance by a factor

$$
\begin{equation*}
1 \leq \frac{\sigma_{\mathrm{est}}^{2}}{\sigma^{2}}=\frac{\sqrt{k_{\mathrm{s} 1} / k_{\mathrm{s} 2}}+1}{\sqrt{\left(k_{\mathrm{s} 1} / k_{\mathrm{s} 2}\right)+1}} \leq \sqrt{2} \tag{5.70}
\end{equation*}
$$

Accordingly, it should be conservative to estimate the variance resulting from a vibrational mode subject to both bending and shear as the sum of the variances of a hypothetical mode constrained purely by bending forces and of one constrained by pure shear forces. (The differences between modal shapes in pure bending and those in pure shear would complicate a more precise analysis.) Thus, treating both classical and quantum variances as additive, expressions for the total transverse variance at the end of a rod take the form

$$
\begin{equation*}
\sigma_{t}^{2}=\sigma_{t, b}^{2}+\sigma_{t, s}^{2} \tag{5.71}
\end{equation*}
$$

with the choice of expressions for the shear and bending contributions depending on the desired accuracy, the magnitude of quantum effects, and the value of $N$. Figure 5.13 uses Eqs. (5.64) and (5.66) to graph the standard deviation of the transverse displacement at room temperature for rods with mechanical properties approximating those of bulk diamond. As can be seen, under these conditions, in the regime where shear and bending compliance are both important, quantum effects on positional uncertainty are minor for rods of nanometer or greater size; accordingly, Eq. (5.59) provides a good approximation.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-47.jpg?height=712&width=1100&top_left_y=1352&top_left_x=309)

Figure 5.13. Transverse positional standard deviation for rods at $300 \mathrm{~K}$, including shear compliance. The bending component is based on Eq. (5.64); the shear component is based on Eq. (5.66), assuming mechanical properties resembling those of bulk diamond, as in Figure 5.8; similar remarks apply.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-48.jpg?height=282&width=514&top_left_y=182&top_left_x=187)

Figure 5.14. Piston, cylinder, and gas molecules. Note that the position coordinate $x$ measures not the distance of the piston from the bottom of the cylinder, but the range of motion available to a gas molecule. A hardsphere, hard-surface model is assumed here and in the text.

### 5.6. Piston displacement in a gas-filled cylinder

Earlier sections have considered linear, elastic systems in which the motion can be divided into normal modes, treated as independent harmonic oscillators. A different approach is necessary for nonlinear systems in which the displacement of one component affects the range of motion possible to another, that is, for entropic springs. Here, the simplest example is not a mass and spring, but a loaded piston in a cylinder containing an ideal gas.

Figure 5.14 illustrates the system and the defining coordinates. The diameter of the cylinder proves irrelevant, and the displacement of the piston is chosen such that a zero displacement corresponds to zero freedom of movement for the gas molecule in the $x$ direction. The assumption of an ideal gas entails ignoring all forces between gas molecules, and accordingly ignoring the reduction in available volume that a molecule experiences as a result of the bulk of other molecules that may be present. Classical positional uncertainty in this system will be analyzed from three (ultimately equivalent) perspectives.

### 5.6.1. Weighting in terms of potential energy and available states

Let the compressing force on the piston be a constant, $F_{\mathrm{c}}$. For an empty cylinder, the potential energy of the piston is then $F_{\mathrm{c}} x$, and applying the Boltzmann weighting to this potential yields the exponential PDF

$$
\begin{equation*}
f_{x}(x)=\frac{\exp \left(-F_{\mathrm{c}} x / k T\right)}{\int_{0}^{\infty} \exp \left(-F_{\mathrm{c}} x / k T\right) d x}=\frac{F_{\mathrm{c}}}{k T} \exp \left(-\frac{F_{\mathrm{c}} x}{k T}\right) ; \quad x \geq 0 \tag{5.72}
\end{equation*}
$$

The addition of $N$ gas molecules does not change the potential energy, but does increase the number of states associated with each piston position by a factor proportional to the space available to each molecule, that is, by a factor proportional to $x^{N}$. Introducing this factor to account for the number of states yields the Erlang PDF

$$
\begin{align*}
f_{x}(x) & =\frac{x^{N} \exp \left(-F_{\mathrm{c}} x / k T\right)}{\int_{0}^{\infty} x^{N} \exp \left(-F_{\mathrm{c}} x / k T\right) d x}  \tag{5.73}\\
& =\frac{1}{N !}\left(\frac{F_{\mathrm{c}}}{k T}\right)^{N+1} x^{n} \exp \left(-\frac{F_{\mathrm{c}} x}{k T}\right) ; \quad x \geq 0
\end{align*}
$$

with mean and variance

$$
\begin{equation*}
\bar{x}=(N+1) \frac{k T}{F_{\mathrm{c}}} ; \quad \sigma_{x}^{2}=(N+1)\left(\frac{k T}{F_{\mathrm{c}}}\right)^{2} \tag{5.74}
\end{equation*}
$$

In this approach, the configurational states of the system are treated as known, and the Boltzmann-weighted probabilities are then integrated over these states.

### 5.6.2. Weighting in terms of a mean-force potential

Alternatively, one can treat the gas as a nonlinear spring described by the ideal gas equation (here in molecular rather than the more familiar molar units)

$$
\begin{equation*}
p V=N k T \tag{5.75}
\end{equation*}
$$

yielding the time-average force owing to pressure

$$
\begin{equation*}
F_{\mathrm{p}}=-N k T / x \tag{5.76}
\end{equation*}
$$

Since the gas is now treated as a spring external to the piston, its configurational states are now ignored (as discussed in Section 4.3.7). Treating $F_{\mathrm{p}}$ on the same basis as $F_{c}$, the work-energy as a function of position is

$$
\begin{equation*}
\int F_{\mathrm{c}}-(N k T / x) d x=F_{\mathrm{c}} x-N k T \log x+C \tag{5.77}
\end{equation*}
$$

hence the Boltzmann-weighted positional PDF is

$$
\begin{equation*}
f_{x}(x)=\frac{\exp \left(-\frac{F_{\mathrm{c}} x}{k T}-n \log x+\frac{C}{k T}\right)}{\int_{0}^{\infty} \exp \left(-\frac{F_{\mathrm{c}} x}{k T}-n \log x+\frac{C}{k T}\right) d x}=\frac{x^{N} \exp \left(-F_{\mathrm{c}} x / k T\right)}{\int_{0}^{\infty} x^{N} \exp \left(-F_{\mathrm{c}} x / k T\right) d x} \tag{5.78}
\end{equation*}
$$

Note that the nonlinearity of the stiffness invalidates the simple relationship

$$
\begin{equation*}
\sigma_{x}^{2}=k T / k_{\mathrm{s}} \tag{5.79}
\end{equation*}
$$

Evaluating $k_{\mathrm{s}}$ at the mean and most probable values of $x$

$$
\begin{equation*}
\frac{k T}{k_{\mathrm{s}, \text { mean }}}=\frac{(N+1)^{2}}{N}\left(\frac{k T}{F_{\mathrm{c}}}\right)^{2} ; \quad \frac{k T}{k_{\mathrm{s}, \text { max-prob }}}=N\left(\frac{k T}{F_{\mathrm{c}}}\right)^{2} \tag{5.80}
\end{equation*}
$$

yields differing results, both of which differ from the true variance, Eq. (5.74). Both expressions, however, approach the correct value in the limit of large $N$, where the standard deviation in position is small enough for a linear approximation to hold for fluctuations of ordinary magnitude.

### 5.6.3. Weighting in terms of the Helmholtz free energy

In a third approach, we begin with the Helmholtz free energy,

$$
\begin{equation*}
\mathscr{F}=\mathscr{E}-T \mathscr{S} \tag{5.81}
\end{equation*}
$$

The internal energy $\mathscr{E}$ is the sum of the potential energy $F_{\mathrm{c}} x$, the kinetic energy of the gas ( $3 / 2 N k T$, assuming a monatomic gas), and of the piston ( $3 k T$, assuming freedom to slide, rotate, and rattle). The translational entropy of an ideal gas

(Knox, 1971) is

$$
\begin{equation*}
\mathscr{S}_{\text {trans }}=N k\left(\frac{5}{2}+\frac{3}{2} \ln \frac{m k T}{2 \pi \hbar^{2}}-\ln \frac{N}{V}\right)=N k\left(C-\ln \frac{N}{x}\right) \tag{5.82}
\end{equation*}
$$

hence the free energy of the system as a function of piston position is

$$
\begin{equation*}
\mathscr{F}=\mathscr{E}-T \mathscr{S}=F_{\mathrm{c}} x+\left(3+\frac{3}{2} N\right) k T-N k T\left(C-\ln \frac{N}{x}\right) \tag{5.83}
\end{equation*}
$$

Taking the Boltzmann-weighted PDF in terms of the free energy again yields

$$
\begin{align*}
f_{x}(x) & =\frac{\exp \left(-\frac{F_{\mathrm{c}} x}{k T}+3+\frac{3}{2} N-N C+N \ln \frac{X}{N}\right)}{\int_{0}^{\infty} \exp \left(-\frac{F_{\mathrm{c}} x}{k T}+3+\frac{3}{2} N-N C+N \ln \frac{X}{N}\right) d x} \\
& =\frac{x^{N} \exp \left(-F_{\mathrm{c}} x / k T\right)}{\int_{0}^{\infty} x^{N} \exp \left(-F_{\mathrm{c}} x / k T\right) d x} \tag{5.84}
\end{align*}
$$

### 5.6.4. Comparison and quantum effects

These three perspectives on the problem are closely related: The variation in available states as a function of piston position considered in the first corresponds to the variation in entropy considered in the third. The second approach considers movement of the piston as doing work on the gas (under reversible, isothermal conditions); work done under these conditions equals the change in FF considered in the third. The choice of perspective in such problems is a matter of convenience.

Physical displacements frequently couple to changes in the range of motion available in some degree of freedom, hence altering its entropy and doing work against an entropic spring. These systems share the basic properties of the piston and cylinder system just considered, including a $(k T)^{2}$ dependence of positional uncertainty in the classical regime, as opposed to the $k T$ dependence of classical uncertainty stemming from conventional springs. In the quantum limit, systems that would exhibit entropic spring effects at higher temperatures will display a small residual compliance stemming from the compression of zero-point probability distributions. This is not an entropic effect, since (in the quantum limit) all modes are consistently in their ground state with an invariant entropy of zero; nonetheless, it is a compressive effect that is a smooth extension of the behavior in the classical regime.

### 5.7. Longitudinal variance from transverse deformation

Transverse vibrations in a rod cause longitudinal shortening by forcing it to deviate from a straight line. This longitudinal-transverse coupling causes longitudinal positional variance, and provides another example of an entropic spring. Although the following analysis is not used in this volume, sheathed flexible rods like those described have applications in a wide range of nanomechanical systems.

### 5.7.1. General approach

Rods sliding in channels can be used to couple mechanical displacements occurring at one location to displacements at a relatively distant location. Thus, it is of interest to consider the longitudinal positional variance of rods in systems where rod motion occurs in a channel that imposes transverse restoring forces (modeled as a stiffness per unit length, $k_{\ell}$ ) via overlap repulsion, and where boundary conditions may impose a mean tension $\gamma_{\ell}$ on the rod.

The effect of shear compliance on transverse vibration is usually small in systems where longitudinal-transverse coupling is significant. Further, in the approximation that the rod behaves as an isotropic, elastically linear material, shear deformation has no effect on length. Shear is accordingly neglected.

The discrete structure of the rod imposes a limit to the number of modes and modifies the coupling constants as $\lambda_{n}$ approaches $2 \Delta \ell\left(=\lambda_{\min }\right)$. The following analysis adopts a semicontinuum model that takes account of limitations on modes while neglecting changes in coupling constants. This approximation can break down in systems where modes with $\lambda \approx \lambda_{\min }$ dominate the variance. Where the restoring force for these modes is dominated by $k_{\ell}$, the approximation is conservative; where the restoring force is dominated by $\gamma_{\ell}$, the approximation is accurate; where the restoring force is dominated by $k_{\mathrm{b}}$, the approximation is too low. In this case, the maximum correction factor for the variance (for $\lambda=\lambda_{\min }$ ) is $(\pi / 2)^{4} \approx 6.09$, falling to 1.52 for $\lambda=2 \lambda_{\min }$ and to 1.02 for $\lambda=10 \lambda_{\text {min }}$.

The nonlinearity of overlap repulsions makes the use of the constant stiffness $k_{\ell}$ a rough approximation. Since stiffness increases with displacement, this approximation is conservative, underestimating the constraining forces. Discussion of quantum mechanical effects is deferred to Section 5.7.3.

### 5.7.2. Coupling and variance

The following analysis considers a weighting in terms of potential energy and available states for each of a set of normal-mode deformations, summing the resulting variances to yield the total variance. The use of normal modes here implies nothing about vibrations, but merely provides a convenient set of orthogonal functions with which to describe all possible rod configurations.

For the sinusoidal deformation characteristic of mode $n$, there exists a constant $\mathscr{C}_{n}$ (dependent on rod parameters) relating the contraction in the length of the rod to the potential energy of the deformation

$$
\begin{equation*}
\Delta \ell_{n}=\mathscr{C}_{n} \mathscr{E}_{n} \tag{5.85}
\end{equation*}
$$

The classical variance in rod length resulting from modal longitudinal-transverse coupling can be determined from the PDF for the potential energy (which in turn can be derived from the Gaussian PDF for the amplitude),

$$
\begin{equation*}
f_{\mathscr{E}_{n}}\left(\mathscr{E}_{n}\right)=\exp \left(-\mathscr{E}_{n} / k T\right) / \sqrt{\pi k T \mathscr{E}_{n}} \tag{5.86}
\end{equation*}
$$

and for the contraction in length

$$
\begin{equation*}
f_{\Delta \ell_{n}}\left(\Delta \ell_{n}\right)=\exp \left(-\Delta \ell_{n} / \mathscr{C}_{n} k T\right) / \sqrt{\pi \mathscr{C}_{n} k T \Delta \ell_{n}} \tag{5.87}
\end{equation*}
$$

From this one can derive the variance in the potential energy

$$
\begin{align*}
\sigma_{\mathscr{E}_{n}}^{2} & =\overline{\mathscr{E}_{n}^{2}}-\left(\overline{\mathscr{E}_{n}}\right)^{2} \\
& =\int_{0}^{\infty} \frac{\mathscr{E}_{n}^{2} \exp \left(-\mathscr{E}_{n} / k T\right)}{\sqrt{\pi k T \mathscr{E}_{n}}} d \mathscr{E}_{n}-\left[\int_{0}^{\infty} \frac{\mathscr{E}_{n} \exp \left(-\mathscr{E}_{n} / k T\right)}{\sqrt{\pi k T \mathscr{E}_{n}}} d \mathscr{E}_{n}\right]^{2} \\
& =\frac{1}{2}(k T)^{2} \tag{5.88}
\end{align*}
$$

and hence the variance in length resulting from longitudinal-transverse coupling in mode $n$.

$$
\begin{equation*}
\sigma_{\ell, t, n}^{2}=\frac{1}{2}\left(\mathscr{C}_{n} k T\right)^{2} \tag{5.89}
\end{equation*}
$$

The mean contraction is

$$
\begin{equation*}
\overline{\Delta \ell_{n}}=\frac{1}{2} \mathscr{C}_{n} k T \tag{5.90}
\end{equation*}
$$

### 5.7.3. Rods with tension and transverse constraints

Consider a long, continuous rod with a bending modulus $k_{\mathrm{b}}$, subject to a mean tension $\gamma_{\ell}$ and a transverse stiffness per unit length $k_{\ell}$. The energy per unit length associated with a sinusoidal deformation can be derived by integrating the contributions from each of these restoring-force terms. For a rod of length $\ell$ supporting modes with amplitudes $A_{n}$ and $\lambda=2 \ell / n(n=1,2,3, \ldots)$,

$$
\begin{equation*}
\frac{\mathscr{E}_{n}}{\ell}=\frac{A_{n}^{2}}{4}\left[k_{\mathrm{b}}\left(\frac{n \pi}{\ell}\right)^{4}+\gamma_{\ell}\left(\frac{n \pi}{\ell}\right)^{2}+k_{\ell}\right] \tag{5.91}
\end{equation*}
$$

The fractional change in length is

$$
\begin{equation*}
\frac{\Delta \ell_{n}}{\ell}=\left(\frac{n \pi A_{n}}{2 \ell}\right)^{2} \tag{5.92}
\end{equation*}
$$

hence

$$
\begin{equation*}
\mathscr{C}_{n}=\frac{\Delta \ell_{n}}{\mathscr{E}_{n}}=\left[k_{\mathrm{b}}\left(\frac{n \pi}{\ell}\right)^{2}+\gamma_{\ell}+k_{\ell}\left(\frac{n \pi}{\ell}\right)^{-2}\right]^{-1} \tag{5.93}
\end{equation*}
$$

and the total (classical) variance resulting from transverse vibrations in one of the two possible polarizations equals the sum of the modal variances

$$
\begin{align*}
\sigma_{\ell, \mathrm{t}}^{2} & =\sum_{n=1}^{N} \frac{1}{2}\left(\mathscr{C}_{n} k T\right)^{2} \\
& =\sum_{n=1}^{N} \frac{1}{2}(k T)^{2}\left[k_{\mathrm{b}}\left(\frac{n \pi}{\ell}\right)^{2}+\gamma_{\ell}+k_{\ell}\left(\frac{n \pi}{\ell}\right)^{-2}\right]^{-2} ; \quad N=\ell / \Delta \ell \tag{5.94}
\end{align*}
$$

The total variance is the sum of contributions from both polarizations; if these are equivalent, the total is twice the above value.

Stretching the rod compresses the range of motion of the transverse modes, doing work and reducing modal entropies; from a mean-force potential perspective, transverse modes introduce a source of (nonlinear) longitudinal compli-
ance. This perspective clarifies the nature of the quantum effects: Each transverse mode can be regarded as a harmonic oscillator with a restoring force modulated by the degree of rod extension. In the quantum-mechanical limit, the transverse positional variance is proportional not to the transverse compliance (as in the classical regime)

$$
\begin{equation*}
\sigma_{\text {classical limit }}^{2}=k T / k_{\mathrm{s}} \tag{5.95}
\end{equation*}
$$

but to its square root

$$
\begin{equation*}
\sigma_{\text {quantum limit }}^{2}=\hbar /\left(2 \sqrt{k_{\mathrm{s}} m}\right) \tag{5.96}
\end{equation*}
$$

hence as quantum effects become significant, mean transverse amplitudes are less easily compressed by increases in restoring forces. Since the longitudinal compliance just described results from compression of transverse modes as a result of increasing tension, it is lower in the quantum regime than in the classical regime, for a given transverse amplitude. Quantum effects on longitudinal positional variance are neglected here.

To permit a graphical summary, the sum over the modes can be expressed in terms of two parameters, $k_{\mathrm{b}} / k_{\ell}$ and $\gamma_{\ell} / k_{\ell}$

$$
\begin{equation*}
\left(\frac{\sigma_{\ell, \mathrm{t}}^{2}}{\ell}\right) \frac{k_{\mathrm{b}} \sqrt{\gamma_{\ell} k_{\ell}}}{(k T)^{2}}=\lim _{\ell \rightarrow \infty} \sum_{n=1}^{\ell / \Delta \ell} \frac{1}{2 \ell}\left(\frac{n \pi}{\ell}\right)^{4} \frac{k_{\mathrm{b}}}{k_{\ell}} \sqrt{\frac{\gamma_{\ell}}{k_{\ell}}}\left[\frac{k_{\mathrm{b}}}{k_{\ell}}\left(\frac{n \pi}{\ell}\right)^{4}+\frac{\gamma_{\ell}}{k_{\ell}}\left(\frac{n \pi}{\ell}\right)^{2}+1\right]^{-2} \tag{5.97}
\end{equation*}
$$

Because the numerators and denominators of these parameters can both vary over many orders of magnitude, even for submicron systems, the ranges covered by Figure 5.15 are large.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-53.jpg?height=726&width=1107&top_left_y=1354&top_left_x=310)

Figure 5.15. A measure of longitudinal variance vs. ratios of restoring forces, based on Eq. (5.97).

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-54.jpg?height=656&width=1105&top_left_y=176&top_left_x=229)

Figure 5.16. Total standard deviation in longitudinal displacement for the end of a thermally excited rod, including elastic and entropic contributions. Plotted vs. diameter and length, assuming mechanical properties resembling those of bulk diamond (as in Figure 5.8); similar remarks apply.

### 5.7.4. Rods with freely sliding ends and no transverse constraint

The absence of transverse constraint forces and applied tension increases positional variance. For rods of finite length, angular freedom at the ends again increases the positional variance. Thus, these conditions are appropriate for setting upper bounds on the longitudinal positional variance resulting from longitudinal-transverse coupling in rods where the ends are constrained to the axis (or, equivalently, where the coordinate measured is the distance between the ends) but are otherwise free. Under these conditions, Eq. (5.94) simplifies to

$$
\begin{equation*}
\sigma_{\ell, \mathrm{t}}^{2}=\frac{1}{2}\left(\frac{k T}{k_{\mathrm{b}}}\right)^{2}\left(\frac{\ell}{\pi}\right)^{4} \sum_{n=1}^{N} \frac{1}{n^{4}} \approx \frac{1}{2}\left(\frac{k T}{k_{\mathrm{b}}}\right)^{2}\left(\frac{\ell}{\pi}\right)^{4} 1.082 \tag{5.98}
\end{equation*}
$$

in which the latter expression represents the rapidly approached limit as $N$ becomes large. Again, contributions from both polarizations must be included. For convenience, Figure 5.16 displays the total longitudinal positional uncertainty resulting from the combined effects of this mechanism (including both equivalent polarizations) and of longitudinal modes as analyzed in Section 5.4.2c, all at $300 \mathrm{~K}$ for rods with properties like those of bulk diamond.

It should be noted that the PDF for the value of $\Delta \ell$ resulting from longitudinal-transverse coupling involving a single mode is not Gaussian, but takes the form of Eq. (5.87). The PDF for the case just considered roughly approximates this, since it is dominated by the contribution of a single mode. Where many modes contribute, however, their sum approximates a Gaussian; the differences chiefly affect the tails of the distribution.

### 5.8. Elasticity, entropy, and vibrational modes

Elastic and entropic springs show distinct behaviors. In elastic systems in the classical regime, positional variance is proportional to compliance and to temperature. Quantum effects in elastic systems increase the variance over the classical value, and contribute a greater fraction of the variance as stiffnesses increase and as masses and temperatures fall. In entropic systems in the classical regime, positional variance is proportional to the square of the temperature. Quantum effects in entropic systems reduce the variance below the classical value; in the quantum limit of large $\hbar \omega / k T$, all vibrational modes are in their ground state, the entropy is zero, and the entropic variance is zero. (Despite the foregoing, the characteristics that yield entropic-spring behavior at elevated temperatures contribute a compliance that does not go to zero in the quantum limit.) Distinguishing these cases leads to substantial simplifications in analyzing elastic systems within the classical-mechanics approximation.

### 5.8.1. Neglect of vibrational modes in classical elastic springs

In analyzing the PDFs of elastic springs with respect to some set of coordinates in the classical limit, modal analysis can be bypassed: only the potential energy as a function of these coordinates is significant. In the quantum regime, an analysis of vibrational modes serves to capture the effects of zero-point energy. In the classical regime, an analysis of vibrational modes is merely a form of entropic bookkeeping; it provides a means of describing all possible system configurations, a step that is useful in analyzing entropic springs but irrelevant in analyzing elastic springs. The simple results Eq. (5.26) and Eq. (5.53) are direct consequences of this.

In the derivation of Eq. (5.26), rod configurations with an end displacement $A_{\text {end }}=\Sigma A_{n}$ were described as a sum of terms

$$
\begin{equation*}
\sum_{n=0}^{\infty} A_{n} \sin [(2 n+1) \pi x / 2 \ell] \tag{5.99}
\end{equation*}
$$

with many possible combinations of $A_{n}$ for a given value of $A_{\text {end }}$. One could equally well describe configurations as a sum of terms

$$
\begin{equation*}
A_{\mathrm{end}} x+\sum_{n=0}^{\infty} A_{n}^{\prime} \sin [(n+1) \pi x / \ell] \tag{5.100}
\end{equation*}
$$

This form separates the end displacement from orthogonal rod deformations; the relationship of end position to mean energy, system entropy, etc., would be the same if these deformations were embodied in an entirely separate object. Note that this recasting does not apply in the quantum regime because the deformation $A_{\text {end }} x$ does not correspond to a vibrational mode.

In general, for purely elastic systems in the classical limit, the PDF associated with a set of coordinates can be evaluated by applying a Boltzmann weighting to the potential energy as a function of those coordinates. For linear systems, the result is a Gaussian distribution (a result that holds in the quantum regime as well). Note that, in the absence of imposed accelerations, inertial mass plays no role in determining equilibrium PDFs for the position coordinates of a system, though it does affect the dynamics of fluctuations. For such systems, variance
scales linearly with temperature and compliance; accordingly, variance is inversely proportional to linear dimensions, given uniform scaling of an elastic structure.

### 5.8.2. Conservative scaling of variance with temperature

Considering quantum effects in elastic systems, it is always conservative to scale up an accurate (or conservative) variance in proportion to temperature or compliance; it is not conservative to scale down in the same manner. At room temperature, objects made of materials as stiff and light as diamond have positional uncertainties dominated by classical effects so long as dimensions exceed one nanometer (Figure 5.8).

For purely entropic systems in the classical regime, variance scales as the square of temperature. Entropic effects in the deformation of structural elements become important as aspect ratios become large (Figure 5.16). For such systems, the variance can be treated as the sum of entropic and elastic contributions.

### 5.9. Conclusions

Harmonic oscillators and elastic rods have positional uncertainties described by Gaussian PDFs. At ordinary temperatures in all but very light, stiff systems (e.g., single atomic masses and bond-stretching displacements), the classical value for the positional variance given by Eq. (5.4) is accurate enough for all but the most precise work. Elsewhere in this volume, the greater size of components and the uncertainties in their stiffness values render the use of more elaborate expressions pointless.

Entropic springs have positional uncertainties that scale differently with temperature. Displacement of an entropic spring does no work against elastic restoring forces, but instead does work against a mean-force potential, imposing position-dependent constraints on motions in other degrees of freedom. Descriptions of two systems have been presented.