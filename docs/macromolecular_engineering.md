# Macromolecular Engineering


### 15.1. Overview

Earlier chapters describe a family of technologies assuming the availability of advanced manufacturing systems to build other advanced systems: the analysis is based on present science, but not on present technology. This chapter and the next attempt to show how the gap between present technology and advanced molecular manufacturing can be bridged. Unlike the chapters of Part II, the present chapter adopts the constraint that the objects and capabilities described be within the reach of research programs that exploit only presently available laboratory capabilities.

Present technology cannot build complex structures containing billions of atoms, each occupying a predictable location. In seeking paths toward this ability, it is natural to start with technologies that can provide precise, molecular control: these include biotechnology, synthetic chemistry, and (more recently) proximal probe systems such as the scanning tunneling and atomic force microscopes (STMs and AFMs). This chapter describes how each of these fields can evolve into a more advanced technology for macromolecular engineering. The next chapter shows how these macromolecular engineering capabilities can be a starting point for a series of steps leading to advanced molecular manufacturing.

This chapter suggests objectives and approaches in several existing fields, aiming to identify lines of development that avoid insurmountable obstacles and offer large long-term rewards. This analysis, however, does not constitute a detailed proposal and cannot be compared to hard-won experimental results. It is offered as an aid in choosing experimental objectives, not as a substitute for achieving them.

### 15.2. Macromolecular objects via biotechnology

### 15.2.1. Motivation

In introducing the concept of molecular manufacturing, examples of molecular devices and processes from biology were used to make the case for physical feasibility, and an analysis of the feasibility of protein engineering was used to make the case for technological feasibility (Drexler, 1981). Although this use of examples from molecular biology (Table 15.1) has since been superseded by

Table 15.1. A comparison of macroscale and biomolecular components and functions (from Drexler, 1981).

| Device | Function | Molecular example(s) |
| :---: | :---: | :---: |
| Struts, beams, casings | Transmit force, <br/> hold positions | Microtubules, cellulose |
| Cables | Transmit tension | Collagen |
| Fasteners, glue | Connect parts | Intermolecular forces |
| Solenoids, actuators | Move things | Conformation-changing <br/> proteins, actin/myosin |
| Motors | Turn shafts | Flagellar motor |
| Drive shafts | Transmit torque | Bacterial flagella |
| Bearings | Support moving parts | Sigma bonds |
| Containers | Hold fluids | Vesicles |
| Pumps | Move fluids | Flagella, membrane proteins |
| Conveyor belts | Move components | RNA moved by fixed ribo- <br/> some (partial analogue) |
| Clamps | Hold workpieces | Enzymatic binding sites |
| Tools | Modify workpieces | Metallic complexes, <br/> functional groups |
| Production lines | Construct devices | Enzyme systems, ribosomes |
| Numerical control systems | Store and read programs | Genetic system |

more direct design and analysis, these examples still illustrate how the engineering of biomolecules could enable the construction of a first generation of molecular machines.

### 15.2.2. DNA, RNA, and protein

The macromolecules of central concern in biotechnology and molecular biology are DNA, RNA, and protein. Genetic engineering now includes powerful and general techniques for constructing DNA molecules; via RNA, these can direct the molecular machinery of bacterial cells to make protein molecules.

DNA ordinarily functions as an information molecule, but N. Seeman has demonstrated that it can also be used to build structures with both branches and loops (Seeman, 1991), including a molecule with the connectivity of a cube. The ability of complementary segments of DNA to bind to one another provides a powerful, readily controllable mechanism for guiding the ${ }^{\circ}$ Brownian assembly of molecules. Hybrid structures of DNA and other macromolecules may prove particularly attractive.

RNA in living cells has diverse functions; some are structural and chemical (e.g., in the ribosome) and some informational (e.g., in the messenger RNA that directs ribosomal synthesis of proteins). Like DNA, it can fold and bind to match up complementary segments, forming a double helix.

Molecular machines in living cells are chiefly made of protein. Unlike pure DNA and RNA structures, protein structures can be dense, compact, and relatively stiff; further, their 20 amino acids give them greater chemical and structural versatility than is found in structures consisting only of the four nucleotides
of DNA or of RNA. These characteristics suggest that proteins will play a central role if biotechnology is used to build nanomechanical systems.

Unlike DNA and RNA, however, protein chains do not bind to one another by pairwise matching of their monomers: no simple notion of complementarity can be used to predict or design the folding of a protein. Although nature demonstrates that proteins are adequate building blocks for systems of molecular machinery, and although biotechnology demonstrates that novel proteins can be constructed, the problem of protein design - of relating amino acid sequence to three-dimensional structure and function-has slowed progress toward proteinbased macromolecular systems engineering.

### 15.2.3. Protein folding: prediction vs. design

The "protein folding problem" has classically been defined as a fold-prediction problem, that is, predicting the three-dimensional folded conformation of a naturally occurring protein molecule given only its amino acid sequence (and no knowledge of the fold of a similar sequence). Despite continuing progress (Bowie et al., 1991; Jaenicke, 1987; Ponder and Richards, 1987b), no general solution to this problem has been found.

It was long assumed that solving the fold-prediction problem was a prerequisite for solving the fold-design problem; this impression lingers, discouraging efforts in de novo protein engineering. Actually, these problems are quite distinct. In solving a design problem, one is free to bias all manipulable characteristics to favor a particular result, but in predicting a natural phenomenon, one faces whatever ambiguities nature happens to present. Based on this elementary observation, together with evolutionary considerations that predict marginal stability for natural proteins, (Drexler, 1981) split the "protein folding problem" into the distinct problems of fold design and fold prediction, arguing that fold design is easier. De novo design of globular proteins has since been pursued (Eisenberg et al., 1986; Erickson et al., 1988; Hecht et al., 1989; Ho and DeGrado, 1987), yielding a recent landmark success (DeGrado et al., 1987; Regan and DeGrado, 1988) which confirmed predictions that design could yield structures of unusual stability (Drexler, 1981). Meanwhile, the ongoing failure to predict the folds of novel natural proteins confirmed the conclusion that fold design is both distinct from and easier than fold prediction. [These suggestions regarding the design of protein folds have been cited and used as a basis for attacks on the fold-prediction problem itself by Ponder and Richards (1987b); see also Lim and Sauer (1989).]

### 15.2.4. Rational design and evolutionary approaches

At present, the field of protein engineering divides into several main areas. Most protein engineering experiments modify one or more amino acid residues in a natural structure to alter protein stability or function (e.g., Bowie et al., 1990; Imanaka et al., 1986; Pantoliano et al., 1987; Pantoliano et al., 1988; Wilks et al., 1988). More ambitious experiments splice portions of known structures together to make new proteins (Blundell et al., 1988). The most ambitious experiments, termed de novo protein engineering, make protein molecules that have no close resemblance to any found in nature (e.g., DeGrado et al., 1987; Hecht et al., 1989). Experiments of the first sort have become routine; de novo protein engineering remains exceptional.

Recent years have seen the emergence of several techniques that develop new proteins not by design, but by an evolutionary process of variation, selection, and replication. The first group, monoclonal antibody technologies, exploits animal immune systems to develop protein molecules that bind a specific ligand molecule; by developing antibodies that bind a molecule resembling the transition state of a particular chemical reaction, it has proved possible to develop antibodies (abzymes) that catalyze the reaction (e.g., Janda et al., 1989; Janda et al., 1988). More recently, techniques for in vitro evolution of monoclonal antibody molecules manufactured by bacteria have been demonstrated (Huse et al., 1989). Systems that select among molecular objects by their affinity to a chromatographic column have been used to evolve specific binding affinities both in protein fragments exposed on viral surfaces (Scott and Smith, 1990) and in isolated RNA fragments (Ellington and Szostak, 1990; Tuerk and Gold, 1990).

Evolutionary techniques can be used to develop protein molecules capable of binding (and altering) other molecules, so long as the desired property permits differential selection and does not interfere with the replication mechanism. If protein molecules are to be used as self-assembling building blocks in larger structures, developing proteins that bind to the correct surface sites is a basic requirement. Evolutionary techniques may provide means for developing such molecules, if methods can be found to select for strong binding at desired sites on a target structure. Methods for masking alternative sites, or for selecting against binding to alternative sites may prove useful in evolving the desired specificity.

### 15.2.5. Material and device properties

In designing machinery for molecular manufacturing, stiffness is a central concern. Different protein structures have widely differing moduli of elasticity (and are inhomogeneous and anisotropic as well); a Young's modulus of $\sim 10 \mathrm{GPa}$ nonetheless "seems to be common to various kinds of polymers of globular protein molecules" (Oosawa and Asakura, 1975). This falls within the range of moduli of polymeric materials such as polyethylene, $1 \mathrm{GPa}$; polystyrene, $3 \mathrm{GPa}$; polyphenylene sulfide, $8 \mathrm{GPa}$; poly(chlorotrifluoroethylene), $14 \mathrm{GPa}$; and most kinds of wood, 8 to $12 \mathrm{GPa}$ (Tapley and Poston, 1990). Although a modulus of $10 \mathrm{GPa}$ is adequate for many purposes, it is only $1 \%$ of the modulus of diamond; there is thus ample motivation to move to better materials.

Existing protein devices demonstrate forces, speeds, and frequencies that can be achieved by machinery constructed from biomolecules working in solution. The enzyme having the highest known operating frequency, catalase, decomposes hydrogen peroxide molecules at $4 \times 10^{7} \mathrm{~s}^{-1}$ (Creighton, 1984), bacterial DNA replication machinery can add nucleotides at $750 \mathrm{~s}^{-1}$, and bacterial ribosomes can add amino acids at about $40 \mathrm{~s}^{-1}$ (Watson et al., 1987). The bacterial flagellar motor can rotate at almost $300 \mathrm{~Hz}$, and can develop a torque of $\sim 2.5 \times 10^{-18} \mathrm{~N} \cdot \mathrm{m}[=2.5 \mathrm{nN} \cdot \mathrm{nm}$ (Blair, 1990)]. Several molecular linear motors (based on myosin, kinesin, and dynein) exert forces that have been estimated at 0.0005 to $0.0026 \mathrm{nN}$ (Ashkin et al., 1990).

Development paths starting with biomolecular systems can exploit existing molecular machines and components. This advantage is reduced by the complexity, fragility, and specialization of existing biomolecular systems, and by the limited knowledge of many structures (for example, no motor mechanism has yet been characterized in atomic detail). Structural knowledge will accumulate (aided by new instruments), and protein engineering techniques might be used to adapt these mechanisms to other applications and make them more robust. Developments along several other pathways, however, will be compatible with hybrid strategies in which biomolecular and wholly synthetic components are combined. Accordingly, it seems unlikely that a purely biomolecular approach will be carried through.

### 15.3. Macromolecular objects via solution synthesis[^40]

### 15.3.1. Motivation

Design becomes easier in systems that exhibit good functional modularity, and becomes more reliable when ample safety margins are possible; greater freedom of design can further both of these objectives. Alternatives to standard, genetically encoded proteins can provide a more tractable medium for the design of folded molecules with proteinlike functions, chiefly by providing better modularity and safety margins. Greater design freedom will permit novel strategies for stabilizing folds; estimates based on observed correlations between structure and free energy suggest that order-of-magnitude increases in the stability of the folded state can be achieved. Increased stability and rigidity can be expected to mitigate errors in molecular modeling and design, increasing the odds of success in a particular design. The family of approaches outlined in this section adheres closely to the protein model; attractive approaches can likely be found that are quite dissimilar from any biological model.

Constructing molecular objects poses challenges both in design and in synthesis, but one challenge can be traded off against the other. Alternatives to standard proteins typically sacrifice the convenience of biosynthesis (but see Noren et al.,1989) in exchange for greater stability and reduced design difficulty. Protein design remains challenging chiefly because the structure of a globular protein emerges from a cooperative folding process dependent on a balance of weak, noncovalent forces in a large, flexible structure. At the other extreme of molecular size and flexibility, proteinlike receptors have been constructed from relatively small, rigid, ${ }^{\circ}$ polycyclic molecules (e.g., Cram, 1988; Lehn, 1988). These molecules are comparatively easy to design: many dozens have been made, vs. the few proteins designed de novo. Their polycyclic structures, however, usually present synthetic challenges greater than those of ${ }^{\circ}$ peptides of similar molecular weight. Their molecular masses typically fall in the 200 to 1200 dalton range (Cram, 1988; Lehn, 1988), vs. $\sim 2000$ daltons for commercially available custom peptides and 5000 to 15000 daltons for experimental products (Kent, 1988).

These two approaches, growing out of protein chemistry and more general chemical synthesis, represent extremes on a spectrum. In the first, synthesis is relatively straightforward, but design is difficult; in the second, design is relatively straightforward, but synthesis is difficult. Intermediate approaches may avoid the worst problems of each, by exploiting peptide-style synthetic strategies to construct molecular objects more rigid, stable, and designable than natural proteins. In examining the potential of this approach, fundamental principles of design are relevant.

### 15.3.2. Basic design principles

Designers exploit modularity: In his classic essay, "The Architecture of Complexity," Herbert Simon notes the utility of modular structure in understanding, designing, and building complex systems (Simon, 1981). Organizing a system as an assembly of relatively distinct, independent building blocks enables the use of divide-and-conquer strategies in design and construction. Early successes in protein design have used $\alpha$ helices as modular units in design and development (DeGrado et al., 1987; Mutter et al., 1988).

Designers exploit safety margins: Evolutionary considerations suggest that evolved proteins can be expected to have minimal stability while designed proteins can have a greater margin of stability (Drexler, 1981); recent experience shows that protein designers can indeed build molecules of increased stability (Matthews et al., 1987; Pantoliano et al., 1988; Perry and Wetzel, 1984; Regan and DeGrado, 1988). Safety margins in stability will improve the odds of success in designing molecular functions.

Finally, designers exploit design freedom: In design, unlike the analytical sciences, one is free to seek components having the best available combinations of stability, predictability, manufacturability, and performance. Design freedom in protein engineering enables the successful pursuit of modularity and safety margins, as has been demonstrated (Mutter et al., 1988; Regan and DeGrado, 1988).

### 15.3.3. Alternatives to standard proteins

Structures based on sequence-specific polymers have advantages worth keeping. To assemble complex macromolecular objects from small molecules, linkages must be introduced in stages. Ease of synthesis favors starting by building linear, polymeric structures. Established synthetic techniques, the entropic advantages of rotationally rigid bonds, and the extensive knowledge resulting from protein science all favor further exploitation of peptide chemistry to build those polymers. (Note, however, that a similar case could be made for exploiting nucleic acid chemistry.)

Noncovalent linkages are well suited for the subsequent steps: they can form under conditions that preserve existing covalent structures; they can link complementary, polyatomic surfaces, enabling specific binding; and they can allow equilibration, breaking and reforming linkages, thereby enabling the system to "search" for a cooperative binding configuration planned by the designer. (Disulfide bonds also allow equilibration under mild conditions and are of similar utility.) Accordingly, proteinlike structures have engineering advantages quite apart from their biological interest.

Within this framework, design freedom can be expanded by choosing from a broader range of parts and chain topologies. It may be that linear sequences of the 20 genetically encoded amino acids of standard proteins will provide adequate design freedom, eventually making de novo protein design practical and routine. Nonetheless, it may be useful to examine the advantages and disadvantages of augmented proteins made using (1) a set of monomers augmented by inclusion of nonstandard amino acids and (2) a set of chain topologies augmented by branched (e.g., Mutter et al., 1988) and cyclic structures. Augmented structures have repeatedly proven their utility in peptide design (DeGrado, 1988), and nonstandard amino acids have appeared in proposals and experiments in protein design (Erickson et al., 1988; Mutter et al., 1988). Nature's use of nonstandard amino acids, phosphorylation, glycosylation, and so forth (via enzymatic modification of proteins) also indicates the utility of a broader set of building blocks and structures than the 20 genetically encoded amino acids.

The following sections build on current understanding of protein folding and stability to explore the utility of augmented proteins for designing stable folded structures. Many of these remarks apply equally well to nonpeptide structures, which would further expand design freedom but are not explicitly considered here. [The following discussion in this section makes free use of terms and concepts from protein chemistry; an excellent introduction is (Creighton, 1984).]

### 15.3.4. Strategies for stabilizing specific folds

Achieving a stable fold entails destabilizing (or excluding) both unfolded and misfolded states. Achieving a stable and predictable fold requires that the designed fold be clearly stable and that alternative folds be clearly improbable; this requires a margin of safety that exceeds modeling uncertainties. Both of these objectives can be pursued by (1) minimizing conformational entropy in the unfolded chain, and by (2) maximizing the strength and specificity of interactions favoring a chosen folded state.

Multiple stabilizing strategies can be applied, but quantifying their value in a design context raises questions regarding the choice of reference state. The stability of a protein can be defined as $-\Delta \mathscr{G}_{\mathrm{f}}$, the negative of the change in Gibbs free energy of folding. The change in stability resulting from a given residue substitution is then $-\Delta\left(\Delta \mathscr{G}_{\mathrm{f}}\right)_{\text {sub }}$. Employing a stabilization tactic in a design, however, will typically involve not a single substitution, but a coordinated set of changes. Consider two protein molecules, A and B, having grossly similar dimensions and properties. Assume that each has been designed for maximum stability, subject to similar functional constraints, but that use of a tactic $X$ (e.g., use of a dialkylglycine residue, a cross-link, etc.) is allowed only in the design of $B$, which may differ from $A$ in any manner needed to exploit $X$ effectively. Tactic $\mathrm{X}$ should be considered stabilizing if $\mathrm{B}$ can usually be made more stable than $\mathrm{A}$. More generally, one can define the expected stabilization resulting from the application of a tactic $\mathrm{X}$ as the average change in $-\Delta \mathscr{G}_{\mathrm{f}}$ resulting from the comprehensive redesign of typical molecules to take advantage of $X$; this can be represented as $-\Delta\left(\Delta \mathscr{G}_{\mathrm{f}}\right)_{\text {design }}$. The magnitude of $-\Delta\left(\Delta \mathscr{G}_{\mathrm{f}}\right)_{\text {design }}$ cannot be measured directly without an enormous amount of design and experimentation. Since good designs will avoid unfavorable interactions in both $A$ and $B$, however, an estimate of the value of $-\Delta\left(\Delta \mathscr{G}_{\mathrm{f}}\right)_{\text {design }}$ is the value of $-\Delta\left(\Delta \mathscr{G}_{\mathrm{f}}\right)_{\text {sub }}$ that is expected
when a single-site substitution (cyclization, etc.) introduces no adverse interactions, such as strain or steric crowding. This will be referred to as a compatible modification.

a. Backbone rigidity. Decreasing the conformational freedom of the backbone decreases the entropy of unfolding, thus stabilizing a compatible folded state. (In the configuration space picture of Section 4.3.3, folding is equivalent to compression; less-flexible molecules expand into a smaller region of configuration space when unfolded, hence the work of compression required to fold them is reduced). In accord with theoretical predictions, the compatible replacement of Gly with Ala (or, it is expected, with any amino acid having a $\beta$ carbon) or of Ala with Pro each increase stability by $\sim 7$ maJ[^41] (Matthews et al., 1987); placing Pro in an $\alpha$ helix, however, would illustrate an incompatible replacement. In augmented proteins, various cyclic amino and imino acids (Figure 15.1) could be used to constrain conformations in a similar manner, but with varied geometries.

Structures 15.1-15.4 suggest how cyclic moieties can alter and constrain backbone conformation. Cubane derivatives (suggested by J. Bottaro) are examples of rigid, saturated polycyclic structures. Structure $\mathbf{1 5 . 5}$ and derivatives can strongly constrain backbone $\phi$ and $\psi$ angles (Toniolo, 1989). Structure 15.6 is
![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-62.jpg?height=992&width=1086&top_left_y=1042&top_left_x=321)

Figure 15.1. Structures illustrating rigidity and steric diversity; BB represents the backbone of a polypeptide

that of alanine; 15.7-15.9 are those of small, nonstandard R-groups of evident use in designing core packings. Structures 15.10-15.13 illustrate known phenylalanine-like structures, formally omitting a methylene [in dialkylglycines (Cotton et al., 1986)] or adding a methyl group (Porter et al., 1987). Removing the methylene increases $\mathrm{R}$-group rigidity, but freely rotating methyl groups can, if constrained in the folded state, adversely affect stability. Structures 15.14-15.19 can be formally derived from standard amino acids by converting a methyl group into the methylene group of a cyclopropane ring, yielding a small change in steric bulk. Structures $\mathbf{1 5 . 1 4}$ and $\mathbf{1 5 . 1 5}$ correspond to valine and leucine; 15.16-15.19 correspond to isoleucine (and a side-chain diastereomer) and exhibit reduced conformational freedom. Structures $\mathbf{1 5 . 2 0}$ and $\mathbf{1 5 . 2 1}$ illustrate the use of cyclic moieties (which can bear rotationally hindered methyl groups) to provide rigid, diverse structures; the related structure of camphor, 15.22, points to the usefulness of natural products as a source of diverse, inexpensive, chirally pure precursors. Structure $\mathbf{1 5 . 2 3}$ exemplifies the use of cyclic moieties for rigidly fixing bulky R-groups to the backbone. In synthesis, difficult monomers can be sandwiched between others with more tractable properties before incorporation into chains (Cotton et al., 1986). Selection of synthetically accessible amino acids and chain sequences is a legitimate application of design freedom.

Peptide researchers have exploited nonstandard amino acids and characterized their conformational effects (DeGrado, 1988; Toniolo, 1989). In particular, dialkylglycine residues impose severe restrictions on $\phi$ and $\psi$ angles; relative to Ala, they should yield a $-\Delta\left(\Delta \mathscr{G}_{\mathrm{f}}\right)_{\text {design }}$ on the order of $\sim 7 \mathrm{maJ}$ per use.

b. R-group rigidity. Folding flexible R-groups into a tightly packed, hydrophobic protein core reduces their conformational entropy. This adverse effect can be reduced by making greater use of relatively rigid $\mathrm{R}$-group structures, such as the rings of phenylalanine, tryptophan, or nonstandard amino acids (Figure 15.1). On entropic grounds, each elimination of a rotational degree of freedom from an aliphatic chain should yield a $-\Delta\left(\Delta \mathscr{G}_{\mathrm{f}}\right)_{\text {design }}$ equaling $\sim 4 \mathrm{maJ}$.

Like other constraints compatible with a planned fold, increased R-group rigidity inhibits unplanned folds. The potential for unplanned folding is suggested by the work of Ponder and Richards on defining sets of residue sequences and R-group conformations compatible with a given backbone conformation (Ponder and Richards, 1987b). A geometric test for sequences of core residues compatible with the fold of rubredoxin yielded 44 sequences, but 236 sets of compatible conformations-that is, an average of over 5 plausible core packings per sequence. Allowing small variations in backbone conformation would presumably have enlarged this number. Both lamprey hemoglobin and crambin have internal residues with alternative conformations (Smith et al.,1986).

Greater use of rigid R-groups makes alternative packings less likely, increasing the specificity of packing and folding. However, it will also increase the difficulty of finding a sequence that has even one acceptable packing.

c. Steric diversity. More rigid R-groups provide fewer shapes per structure, but this can be countered by providing more structures. How many shapes are needed to make tight packings possible? The nonpolar amino acids Ala, Val, Leu, Ile, Pro, Phe, and Trp assume 18 common rotameric conformations in proteins (Ponder and Richards, 1987b); in a sample protein population they make
up 37\% of the residues (Creighton, 1984), and a larger fraction of the interior residues. This suggests that use of a few tens of relatively rigid $\mathbf{R}$-groups can enable the design of packings having a large fraction of rigid structure.

Natural protein interiors have a mean volumetric packing density of about .74 (Ponder and Richards, 1987b) with local variations from < 6 to >. 85 (Richards, 1977). A cavity the size of a methylene group decreases the stability of the folded state by about $8 \mathrm{maJ}$ (Kellis et al., 1988), and various unfavorable interactions in the folded state (e.g., adverse van der Waals contacts) reduce stability by an estimated 14 maJ per residue (Creighton, 1984). Expanding design freedom by including D-amino acids and nonstandard R-groups (Figure 15.1) should increase achievable packing densities while reducing adverse van der Waals contacts-a wider choice of pieces will help designers find better-fitting patterns.

d. Pairwise matching. An unworkable-yet instructive-way to think of protein folding is to regard each interior $\mathbf{R}$-group as binding to a receptor site formed by the rest of the fold. In this entirely nonmodular picture of cooperative folding, every part fits because of the way the rest fits, offering no point of departure for design and analysis. In standard proteins, regularities at the level of secondary structure provide a partial escape from this quandary.

In augmented proteins, a large R-group could provide a preformed, foldindependent binding site for another $\mathrm{R}$-group, yielding modularity at the level of monomer pairs. Supramolecular complexes (Cram, 1988; Lehn, 1988) and nucleic-acid base pairing in folded RNA and in DNA junctions (Robinson and Seeman, 1987) provide models for such pairwise specificity. Even weak pairwise binding could aid folding specificity, while stronger interactions could strongly direct folding by forming complexes stable enough to mimic covalent cross-links.

e. Cyclic and branched backbones. Fold-compatible cross-links decrease the entropy of unfolding, stabilizing the folded state [by about $2.8 \mathrm{maJ}$ per residue in a 10-residue loop at room temperature (Poland and Scheraga, 1965)]. Engineered disulfide cross-links have been used to stabilize natural proteins (Perry and Wetzel, 1984). Since looped structures (closed, for example, by ${ }^{\circ}$ amide bonds between $\mathrm{R}$-groups) can be made using solution chemistry and then treated as monomers during solid-phase synthesis, augmented proteins can incorporate cyclic backbone segments.

Studies of omega loops (Leszczynski and Rose, 1986) show that small looped structures (6 to 16 residues) can be globular and densely packed. Analogous cyclized structures can be regarded as small domains or large monomers, serving as modular elements in design and folding. These elements can be large enough to exhibit pairwise selectivity and binding, strongly guiding the folding process.

Branched structures decrease the entropy of unfolding through excludedvolume effects. This augmentation strategy (Mutter et al., 1988) has brought striking success in constructing stable tertiary structures, including a 73-residue molecule with enzymatic activity (Hahn et al., 1990).

f. Staged thiol pairing. Many standard proteins form cycles postsynthetically, through oxidation of pairs of cysteine ${ }^{\circ}$ thiol groups to form disulfide bonds. Cross-links exposed to a suitable mix of thiols and disulfides in solution undergo rapid thiol-disulfide exchange through $\mathrm{S}_{\mathrm{N}} 2$ displacement (Saxena and Wetlaufer, 1970); this can anneal the disulfide bond system toward a pairing pattern

Table 15.2. Model thiol compounds and their $\mathrm{p} K_{\mathrm{a}}$ values in aqueous solution.

| Thiol | $\mathrm{p} K_{\mathrm{a}}$ | ref. |
| :--- | :---: | :---: |
| Thiobenzoic acid | 2.48 | $\mathrm{a}$ |
| Thiolacetic acid | 3.5 | $\mathrm{~b}$ |
| 2-Nitro-5-mercaptobenzoic acid | 4.53 | $\mathrm{c}$ |
| 4-Mercaptobenzenesulfonic acid | 5.73 | $\mathrm{~b}$ |
| Thiophenol | 6.5 | $\mathrm{~b}$ |
| Methyl mercaptoacetate | 7.68 | $\mathrm{~b}$ |
| Cysteine | 8.30 | $\mathrm{~b}$ |
| 1-Thioglycerol | 9.51 | $\mathrm{~b}$ |
| Ethanethiol | 10.61 | $\mathrm{~b}$ |
| 2-Methyl-2-butanethiol | 11.35 | $\mathrm{~b}$ |

a Whitesides et al., 1977.

b Danehy and Parameswaran, 1968.

c Riddles et al., 1979.

of minimal free energy (Creighton, 1978; Creighton, 1984). In augmented proteins, a wider choice of thiol $\mathrm{R}$-groups can broaden the range of disulfide crosslink geometries. Further, bulky monomers (or cyclic backbone segments) can provide local steric constraints to guide cross-link formation.

Formation of disulfides under conditions of increasing oxidation and (initially) high $\mathrm{pH}$ can favor pairing of thiols in stages corresponding to their $\mathrm{p} K_{\mathrm{a}}$ values, from highest to lowest (Table 15.2), making pairing more specific. Data from studies of the kinetics and equilibria of thiol-disulfide exchange (Szajewski and Whitesides, 1980; Whitesides et al., 1977) indicate that, although equilibration among disulfides would destroy $\mathrm{p} K_{\mathrm{a}}$-specific pairing, lower $\mathrm{p} K_{\mathrm{a}}$ thiols can be paired and equilibrated among themselves rapidly enough to limit destructive equilibration with established, less-labile disulfides formed from thiols of substantially higher $\mathrm{p} K_{\mathrm{a}}$. Preliminary Monte Carlo simulations of staged thiol pairing in this approximation indicate that molecules having solely within-class pairing (for 12 to 18 thiols in three $\mathrm{p} K_{\mathrm{a}}$ classes) can be obtained with yields of tens of percent.

In this sequential annealing process, early-forming bonds can sterically constrain later bond formation [as in standard proteins (Creighton, 1978)]. This mechanism can hinder incorrect pairings within a set of thiols of a particular $\mathrm{p} K_{\mathrm{a}}$, enabling the formation of multiple specific cross-links per stage. The chief disadvantage of disulfides formed from low- $\mathrm{p} K_{\mathrm{a}}$ thiols is extreme sensitivity to alkaline degradation (Danehy, 1971).

g. Metal complexation. Suitable R-groups can form constraining cross-links when metal ions are introduced into solution. In standard proteins, these constraints can force folding of structures as small as 30-residues [e.g., zinc fingers (Párraga et al., 1988)]. Engineering of metal binding sites has increased the stability of subtilisin (Pantoliano et al., 1988). Work in supramolecular chemistry suggests that single $\mathrm{R}$-groups (e.g., based on $\alpha, \alpha^{\prime}$ bipyridine) can serve as preformed halves of metal binding sites, undergoing pairwise matching when metal
(a)

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-66.jpg?height=409&width=829&top_left_y=186&top_left_x=490)

(a2)

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-66.jpg?height=164&width=282&top_left_y=564&top_left_x=493)

(a3)

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-66.jpg?height=138&width=171&top_left_y=732&top_left_x=551)

(b2)

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-66.jpg?height=140&width=263&top_left_y=610&top_left_x=1070)

(b3)

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-66.jpg?height=113&width=116&top_left_y=749&top_left_x=1136)

Figure 15.2. Staged crosslinking and cyclic backbone segments.

ions are added to a solution (Lehn, 1988). As in staged thiol pairing, the time at which crosslinking occurs can be controlled by manipulation of solution composition. Thus, metal complexation can add a further stage to the strategy of forming cross-links in locations determined by constraints established by previous cross-links. Metal binding can also drive the quaternary assembly of separately folded structures (Frankel et al., 1988); disulfide formation can do likewise. Figure 15.2 suggests how staged crosslinking could strongly constrain a folded state.

Series (a) shows in schematic form how six crosslinking groups in three reactivity classes (based on thiol $\mathrm{p} K_{\mathrm{a}}$ values, Table 15.2, or on distinct binding specificities) might be used to constrain conformation through staged crosslinking. In stage (a1), the molecule is cyclized; in (a2) and (a3) the initial loop is further crosslinked. A theory of entropy for multiply-looped chains (Poland and Scheraga, 1965) indicates that a fold based on (a3) would be stabilized by roughly $105 \mathrm{maJ}$ relative to the uncrosslinked structure (at $30^{\circ} \mathrm{C}$ ). More speculatively, series (b) suggests an extensive application of staged crosslinking in which multiple crosslinking groups pair at each stage and selectivity of pairing within a class (if achievable) is dependent on constraints resulting from prior structure. In this sketch, a chain is synthesized with cyclic backbone segments designed to sterically and entropically favor the pattern of pairing shown in stage (b1). Selectivity in stage (b2) depends on adequate steric constraints established in (b1), and stage (b3) similarly depends on the results of (b2). This suggests the possibility of structures in which cross-links virtually preclude unfolding.

### 15.3.5. Consequences for design

Table 15.3 compares a noncrosslinked standard protein to an augmented protein of similar size, but designed to exploit the tactics described in Section 15.3.4; relative stabilizations exceeding $450 \mathrm{maJ}$ seem achievable in an augmented protein of only 50 residues. This increment is large compared to the

Table 15.3. Stability increment expected for a 50-residue augmented protein. ${ }^{a}$

| Mechanism | Stability improvement <br/> (maJ) |
| :---: | :---: |
| a. Increased backbone rigidity | 115 |
| b. Increased R-group rigidity | 50 |
| c. Improved packing density | 70 |
| d. Reduction in bad van der Waals contacts | ? |
| e. Cyclic backbone segments | 110 |
| f. Disulfide cross-links, metal complexation | 110 |
| Sum: | $>455$ |
| Differences between augmented and standard proteins can contribute to <br/> increased stability of the folded state. The basis of the estimates listed above is <br/> as follows: (a) 7 maJ per three residues, resulting from use of dialkylglycines and <br/> cyclic structures in one third of all residues. (b) 3 maJ per three residues, result- <br/> ing from elimination of one rotational degree of freedom in one third of all R- <br/> groups. (c) Exploitation of steric diversity is assumed to increase packing den- <br/> sity by $4 \%$, from the mean for proteins, .74, to a high value for organic crystals, <br/> .78, which still falls short of densely packed regions of proteins (>.85); see Rich- <br/> ards (1977). The associated stability increment is estimated from the 8 maJ sta- <br/> bilization resulting from filling a cavity the size of a methylene group (Kellis et <br/> al., 1988). (d) Expected to be substantial; not estimated here. (e) Based on <br/> change in conformational entropy from forming four 10 -residue loops (Poland <br/> and Scheraga, 1965). (f) Taken as equal to (e); as with (a) and (b), the effect of <br/> this tactic will vary with the extent of its application. |  |

stability of small evolved proteins (typically $\sim 35-70 \mathrm{maJ}$ ), or even of $\alpha_{4}$ [estimated at $\sim 150 \mathrm{maJ}$ (Regan and DeGrado, 1988)]. It may well be impractical (and unnecessary) to apply all these tactics to a single molecule. Margins of safety of this magnitude can expand design freedom in functionally critical parts of a molecule: if crafting a binding site or a flexible joint demands the sacrifice of several hydrogen bonds or creation of $0.1 \mathrm{~nm}^{3}$ of internal space, this need not jeopardize the stability of the folded state.

Mechanisms for imposing conformational constraints-including backbone rigidity, R-group rigidity, cyclic segments, and staged thiol- and metal-based crosslinking - will not only stabilize the desired fold, but will destabilize (or simply block) an indefinitely large set of alternative folds. The destabilization of unwanted alternatives can be quantified: since $\sim 275 \mathrm{maJ}$ of the stability increment results from decreases in conformational entropy imposed before folding begins, the number of energetically accessible alternative configurations (including both unfolded, misfolded, and misaggregated states) is reduced to $\sim 10^{-29}$ of the unconstrained value. By making results more predictable, this should increase the success rate in the trial-and-error process of designing macromolecular objects. Several groups have developed software to aid protein design (Blundell et al., 1988; Pabo and Suchanek, 1986; Ponder and Richards, 1987b); these systems appear adaptable to augmented proteins. Further, as indicated by the discussion in Section 4.4.3, stability achieved through rigidity
reduces the sensitivity of designs to the errors in molecular mechanics models; these errors pose a serious problem where natural proteins are concerned.

This discussion has focused on backbone and hydrophobic core structures, but surface properties largely determine molecular behavior. These, too, are targets for design. For example, solubility-though aided by structures that favor the folded state and thus disfavor alternative, aggregated states (Mutter et al., 1988) - can be further increased by the generous use of polar and charged Rgroups on the molecular surface; these can include groups bearing polar (Gehrhardt and Mutter, 1987) or multiply-charged polymeric chains (large, solubilizing side chains that can be cleaved and discarded after a molecular object has bound to a larger assembly may be of particular value). Broadened residue options will facilitate the design of surface geometry, electrostatics, reactivity, and so forth.

### 15.3.6. Trade-offs and applications

By expanding design freedom, the use of augmented proteins can aid the design of stable, predictable, functional molecules. Several of the tactics proposed here for augmented proteins may prove difficult to implement, but avoidance of those that prove too difficult is a proper use of design freedom. Commercial solid-phase synthesis of standard peptides now offers products with costs of $\sim \textdollar 10$ per milligram for $\textdollar 1000$ orders of crude oligopeptides in the 10 -mer to 20 mer range. Prices climb steeply with chain length and purity; they fall steeply with increased quantity. Lengths near the 50-mer range are approaching routine practice (Kent, 1988).

Feasible tactics should yield stable folds in chains of readily accessible length. Small size aids characterization (without crystallization) via solution nuclear magnetic resonance techniques (Clore and Gronenborn, 1987); these have been extended to structures several times as large as those contemplated here (Kay et al., 1990). Larger molecular systems can then be designed as quaternary structures self-assembled from these building blocks; a review of relevant principles appears in Lindsey (1991), and a more general survey appears in Whitesides et al. (1991). Various high-value molecular products might be worth making, despite the cost of chemical synthesis. Among these are systems of molecular machinery like those discussed in Section 16.4.

### 15.4. Macromolecular objects via mechanosynthesis[^42]

### 15.4.1. Motivation

The atomic force microscope [AFM (Binnig and Quate, 1986) also termed a scanning force microscope] enables surfaces to be positioned relative to one another in a solution environment with $\sim 0.01 \mathrm{~nm}$ positional precision and tip compressive loads as low as $0.01 \mathrm{nN}$ (Hansma, 1990; Weisenhorn et al., 1989). AFMs are most often used to form images of surfaces by probing mechanical interactions at many points. This section suggests how AFM mechanisms could be exploited to enable solution-phase mechanosynthesis; instruments of the sort described also have more immediate applications in improving AFM imaging.

The lack of reproducible, well-characterized, atomically sharp tips in standard AFM systems causes difficulties in image resolution, interpretation, and reproducibility. It has been proposed (Drexler and Foster, 1990) that AFMs with molecular tips could both alleviate these problems and provide an approach to achieving positional control of chemical synthesis. Single molecular tips, however, present problems of fabrication, yield, and damage during use.

Molecular tip arrays as proposed here can permit screening and interchange of tips during operation, reducing sensitivity to yield and damage. They can enable sequential use of differing tips to image a sample and to perform solution-phase mechanosynthesis. A penalty of this flexibility is limitation to small substrates. R. Merkle has proposed an analogous approach based on scanning tunneling microscope mechanisms working with adsorbed reagent molecules in vacuum.

### 15.4.2. Tip-array geometry and forces

a. Tip-array geometry. The geometry of a tip-array system is illustrated in Figures 15.3 and 15.4. On a large scale, Figure 15.3(d), a primary bead can be viewed as an AFM tip, imaging an array of flat-side beads. On a small scale, Figure 15.3(a), a single molecular tip on the flat-side secondary bead images the primary bead. The terms substrate and tip are thus ambiguous, but under the conditions of greatest interest, the primary bead acts as the substrate and a molecule on the secondary bead acts as the tip. Key geometrical parameters are defined by Figure 15.4. Reasonable dimensions for a device with this geometry
![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-69.jpg?height=792&width=1166&top_left_y=1329&top_left_x=185)

(b)

$100 \mathrm{~nm}$

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-69.jpg?height=340&width=567&top_left_y=1813&top_left_x=783)

Figure 15.3. Views of a tip-array geometry using tip support structures and multiple substrate beads on an AFM cantilever. Each view differs from the next by a factor of ten in scale.

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-70.jpg?height=567&width=1119&top_left_y=189&top_left_x=309)

Figure 15.4. Sketch illustrating the relationships among the bead, flat, and molecular tips, including basic geometric parameters.

are $r_{1} \approx 500 \mathrm{~nm}, r_{2} \approx 50 \mathrm{~nm}, h \approx 4 \mathrm{~nm}$, and $\delta \approx 6 \mathrm{~nm}$. Commercial AFMs (Prater et al., 1990) enable operation in a fluid medium with atomic resolution and scan ranges of $25 \mu$; they seem suitable as basic mechanisms. The following assumes that the fluid medium is an aqueous solution, but anhydrous solvents are feasible and sometimes desirable.

If bead-bead forces and stiffnesses are small relative to the required imaging forces and stiffnesses, they will permit imaging based on interactions between the tip and the target structure. To limit bead-bead interactions, a tip must have a height $h$ greater than some minimum imaging separation $\delta$ (discussed in Section 15.4.2b). For typical geometries with $r_{1}>r_{2} \gg(h-\delta)$, a region of diameter

$$
\begin{equation*}
d \approx \sqrt{8(2 h-\delta)\left(r_{1}+r_{2}\right) r_{1} / r_{2}} \tag{15.1}
\end{equation*}
$$

on the primary bead can be scanned to image or modify target structures, so long as other flat-side beads do not interfere. With $r_{1}=500 \mathrm{~nm}, r_{2}=50 \mathrm{~nm}$, and $(2 h-\delta)=2 \mathrm{~nm}, d \approx 300 \mathrm{~nm}$. Since the centers of the flat-side beads are expected to be separated by approximately $r_{2}$, the actual scanned diameter in this instance is

$$
\begin{equation*}
D \approx 2 r_{2} \tag{15.2}
\end{equation*}
$$

or approximately $100 \mathrm{~nm}$. Though small, this area should be adequate for some purposes (e.g., imaging proteins and performing mechanosynthesis).

b. Forces. Bead-bead interactions at small separations arise chiefly from electrostatic, solvation, van der Waals, and so-called steric forces. Electrostatic interactions between the bead and flat can be minimized by ensuring that the surfaces are near electrical neutrality, or by using a solution in which ions effectively screen the effects of surface charge. Moderate concentrations of salt in water ( $\geq 0.1 \mathrm{M} \mathrm{NaCl}$ ) result in a Debye screening length $<1 \mathrm{~nm}$, small compared to $\delta \approx 6 \mathrm{~nm}$. Solvation interactions can operate over multiple molecular diameters: in water, the repulsion between hydrophilic surfaces (Israelachvili, 1992)
falls off exponentially, becoming acceptably small at separations of 1 to $3 \mathrm{~nm}$ (hydrophobic forces would cause strong adhesion between surfaces and must be avoided). Oscillating solvation forces associated with molecular size effects become small at separations greater than $\sim 2 \mathrm{~nm}$ in water (Israelachvili, 1992), and are reduced by surface roughness and mixed-solvent systems. With rough bead surfaces and $\delta \approx 6 \mathrm{~nm}$, oscillating forces should not be observed.

Bead-flat van der Waals interactions can be described using continuum models based on the Hamaker constant (Section 3.5.1a). The results are thought to give a reasonably accurate picture of the forces and their dependence on geometrical parameters. One family of approaches to bead fabrication would use polystyrene-like materials; for polystyrene interacting through water, the Hamaker constant $\mathscr{A} \approx 1.3 \times 10^{-20}$ (Israelachvili, 1992). (This neglects Debye screening of zero-frequency contributions to the Hamaker constant.) With the given geometrical parameters and an intersurface separation $s=\delta=6 \mathrm{~nm}$ the force $F$ is attractive and $\approx-0.003 \mathrm{nN}$ (from the relationship stated in Figure 3.10(c), which neglects retardation effects). This is smaller than the minimum tip contact force reported in AFM work, $0.01 \mathrm{nN}$, and is associated with a stiffness of only $\sim-0.001 \mathrm{~N} / \mathrm{m}$, which is negligible in comparison to the stiffness of a typical AFM cantilever or of an interaction between two molecules in contact. Accordingly, this force should cause little difficulty.

Previous papers (Drexler, 1991b; Drexler, 1992; Drexler and Foster, 1990) have described less-symmetrical structures, with support molecules attached on a single side to avoid a requirement for two distinct attachment technologies. In those geometries, intersurface separations are smaller, requiring material and solvent choices that minimize the net Hamaker constant. The present approach has greater symmetry, enabling a single attachment technology to mount both target-supporting and tip-supporting molecules. The resulting increase in intersurface separation relaxes constraints on the Hamaker constant, and hence on the choice of materials and solvents.

Figure 15.3(a) illustrates the use of short solvophilic chains (e.g., polyoxyethlyene) on the bead surfaces to provide a short-range repulsive force caused chiefly by entropic effects. This mechanism is termed steric stabilization and is widely used to prevent the coagulation of colloids. Attachment of these chains renders the bead surfaces hydrophilic and inhibits the bead-bead adhesion that would otherwise occur though short-range hydrophobic and van der Waals attractions.

c. Multiple beads. Figures 15.3(c) and 15.3(d) illustrate larger-scale geometrical features of a system that permits primary beads to be interchanged during operation by tilting the flat relative to the cantilever. Except for molecular structures at the finest scales, Figure 15.3(a), and platelike structures at the largest scales, Figure 15.3(d), each of the shapes illustrated can be generated by the solidification either of a droplet or of a fluid forming a meniscus between two objects. With the same exceptions, all close contacts occur between spherical surfaces and are insensitive to angular misalignment. Accordingly, the most severe fabrication challenge appears to be that of attaching suitable molecules to beads, and doing so with adequate stiffness.

### 15.4.3. Molecular tips and supports in AFM

a. Protein-ligand tips. Potential tip structures include proteins or particles bearing small adsorbed molecules. A particularly versatile approach exploits the capabilities of both organic synthesis and biotechnology by using synthetic ligands as tips and protein molecules as supporting structures. Many natural proteins bind partially exposed ligands. Ligand analogs could be synthesized with protruding moieties having steric properties suiting them for use as AFM tips. Extensions of monoclonal antibody technology (e.g., Huse et al., 1989) can rapidly generate proteins able to bind almost any selected small molecule. Singlechain Fv proteins [combining antibody $V_{L}$ and $V_{H}$ sequences (Bird et al., 1988)] are compact, $\sim 3 \mathrm{~nm}$ in height, and lack hinge regions. Use of these antibodyderived proteins can allow broad freedom in ligand design, if their stability is (or can be made) adequate for use in an AFM mechanism (see Section 15.4.3c). Techniques for attaching proteins to surfaces are noted in Section 15.4.4.

b. Stiffness. To be used as AFM tip-supports and as imaging targets, proteins and protein-ligand complexes must have adequate mechanical stiffness. In protein crystals [which have been used as models for bound protein-protein complexes (Finkelstein and Janin, 1990)], individual atoms in the protein interior typically undergo a 0.03 to $0.05 \mathrm{~nm}$ root-mean-square displacement caused by thermal vibration (Creighton, 1984). The atomic-displacement stiffness, $k_{\mathrm{s}}$, can be derived from the root mean square displacement via the relationship for a thermally excited harmonic oscillator [Eq. (5.4)], which implies $k_{\mathrm{s}} \approx 1.6$ to 4.6 $\mathrm{N} / \mathrm{m}$ for typical atomic displacements in the interior ( $k_{\mathrm{s}}$ for a side chain on a surface often is far lower). Proteins in crystals typically are anchored to neighbors by a few side chain contacts; comparably stiff attachment of proteins to surfaces seems achievable.

Rigid, polycyclic structures of substantial size can be made by organic synthesis (e.g., Webb and Wilcox, 1990), and their internal stiffnesses can exceed those of proteins. Such ligands can be anchored relative to the protein by numerous van der Waals interactions of substantial stiffness (Section 3.3.2e), yielding ligand atomic-displacement stiffnesses toward or beyond the upper end of the range characteristic of proteins: the following sections will assume a value of $3 \mathrm{~N} / \mathrm{m}$. The stiffness of the interaction in imaging a protein by a protein/ligand complex can thus be $\geq 1 \mathrm{~N} / \mathrm{m} ;$ AFM cantilevers with $k_{\mathrm{s}}<1 \mathrm{~N} / \mathrm{m}$ should provide good responsiveness.

c. Stability of proteins under compressive loads. Applied forces can destabilize protein folding and ligand binding. The free energy required for unfolding or unbinding (Creighton, 1984) typically is $\sim 50$ to $100 \mathrm{maJ}$; at the larger energy, the unfolding half-life is on the order of 1000 years (assuming a $1 \mathrm{~s}$ folding time; typical values range from 0.1 to $1000 \mathrm{~s}$ ). From a kinetic perspective, the destabilizing energy increment resulting from a force equals the work it performs as the molecule moves from equilibrium to a transition state for unfolding (where the location of the transition state is affected by the force); estimating this energy requires an estimate of the atomic displacements associated with such a transition state.

In a linear elastic system, the strain energy $\mathscr{V}_{\mathrm{s}}$ is related to a displacement $\Delta x$ by

$$
\begin{equation*}
\Delta x=\left(2 \mathscr{V}_{\mathrm{s}} / k_{\mathrm{s}}\right)^{1 / 2} \tag{15.3}
\end{equation*}
$$

Large $\mathscr{V}_{\mathrm{s}}$ and low $k_{\mathrm{s}}$ yield a large (adverse) value of $\Delta x$. For $\mathscr{V}_{\mathrm{s}}=100 \mathrm{maJ}$ and $k_{\mathrm{s}}=1.6 \mathrm{~N} / \mathrm{m}, \Delta x=0.35 \mathrm{~nm}$. Localized displacements of this magnitude (an atomic diameter) might independently be expected to disrupt the tight core packing necessary for stability (Richards, 1977). Over this displacement, $0.1 \mathrm{nN}$ performs $35 \mathrm{maJ}$ of work, which is small compared to the energetic differences between more and less stable proteins. Thus, on kinetic stability grounds, this estimate suggests that $0.1 \mathrm{nN}$ forces should be compatible with imaging of proteins of moderate stability (occasionally interrupted by denaturation), and compatible with the use of tips based on proteins of good stability incorporating well-bound ligands.

Considering only stiffness and acceptable elastic deformations (taken to be $0.01 \mathrm{~nm}$ ), and calculating from a continuum model, a maximal tip force of $0.01 \mathrm{nN}$ had been suggested for protein imaging (Persson, 1987). Note, however, that with $k_{\mathrm{s}} \approx 1.6 \mathrm{~N} / \mathrm{m}$ (a low value from experimental data), a $0.1 \mathrm{nN}$ force would yield $\Delta x \approx 0.06 \mathrm{~nm}$ and $\mathscr{V}_{\mathrm{s}}<k T_{300}$. These values are compatible with imaging yielding useful structural data.

In AFM systems of standard geometry, repulsive interatomic tip forces (in the presence of net long-range attraction) have been reduced to low values. It had been suggested that forces as low as $0.01 \mathrm{nN}$ should be within reach for systems operating in solution (Weisenhorn et al., 1989), and this was subsequently achieved (Hansma, 1990). Comparably low forces should likewise be possible in multiple-tip systems, providing a substantial margin of safety when using proteins as tip supports or as imaging targets.

### 15.4.4. Attachment of supporting molecules

The immobilization of molecules (and proteins in particular) is a well-established technique in biotechnology (Scouten, 1987; Uy and Wold, 1977), often used to retain molecules in a vessel as fluid flows past. Immobilization commonly relies on the formation of cross-links between reactive moieties on a protein and on a surface. Molecular tip arrays, however, will require more than immobilization against macroscopic displacement: they will require relatively stiff attachment of molecules to a surface.

Immobilization requires only a molecular tether; stiff attachment requires three (or more) points of contact providing tripodlike stability. The stiffness of a tip can be no greater than the stiffness of the interface attaching it to a surface. A stiffness of $\sim 1.6 \mathrm{~N} / \mathrm{m}$ combined with a tip contact load of $\sim 0.01 \mathrm{nN}$ can produce an effective concentration of $\sim 145 \mathrm{~nm}^{-3}$ for a tip moiety relative to a point on a substrate, in the presence of AFM jitter and thermal noise (Section 15.4.6a). This stiffness is compatible with the mechanical properties of proteins, assuming good attachment. It also suffices for strong positional control of chemical reactions.

A previous paper (Drexler, 1992) suggests strategies for achieving stiff attachment of proteins to surfaces, several of which exploit the engineering of
protein-surface side chains to provide specific binding interactions. One family of approaches would attach proteins to surfaces directly, via the bonding of side chains (e.g., the thiols of cysteine) or chemically-modified side chains. Another family of approaches would use techniques akin to the freeze-cleave-etch methods used to prepare specimens for electron microscopy. A final family of approaches discussed there would link proteins to molecules embedded in fluid Langmuir-Blodgett films, which could then be polymerized to increase their stability; this has the advantage of forming (in effect) a binding site for the protein, thereby increasing its stability. A more recent approach, suggested by the Langmuir-Blodgett film approach combined with ideas suggested by work on imprinting small molecules in polymers (e.g., Fischer et al., 1991; Robinson and Mosbach, 1989) would link proteins to surfactant molecules embedded in a droplet that is later polymerized to form a bead. In light of these possibilities, suitable attachment techniques appear feasible.

### 15.4.5. Imaging with molecular tips

On a large scale, scanning the primary bead provides a low-resolution image of the array of flat-side beads. In regions where the primary bead and a secondary bead interact through steric repulsion forces between the polymers, the image is expected to be essentially featureless. In regions where a molecular tip on the secondary bead interacts with a target structure on the primary bead, the image is expected to show structural features at high resolution. Systematic probing in these regions (moving in and out by several nanometers at a series of points on a grid) can generate a map of force vs. distance for the interaction between tip and target. A surface in that map corresponding to a large, constant stiffness should in many instances resemble an atomic-resolution topographic map.

For a system with a $\sim 25 \mu$ scan range and $d \approx 100 \mathrm{~nm}$, the number of immediately available tips can be $\sim 10^{5}$. A tip array can advantageously include tips that have diverse structures and orientations.

On an isotropic substrate, supporting molecules (and their bound tips) will be attached at diverse azimuthal angles. Bead curvature and structural irregularities will increase the diversity of orientations in the other two rotational degrees of freedom.

Tips can be polar, nonpolar, hydrogen bonding, positively charged, or negatively charged. Information gained by imaging a single molecule with tips of multiple types may help fulfill the goal (Drake et al., 1989) of determining folded protein structures through AFM and computational modeling. It may be that features can be reproducibly mapped on the surface of a protein, yet fail to indicate which residues occupy which surface locations. If so, then imaging and comparing a series of proteins (prepared via site-directed mutagenesis) that differ only by the substitution of a distinctive residue at a known position in the sequence could reveal much about the structure of the folded state.

Tips with specific biochemical affinities (e.g., enzyme substrate analogues, candidate drug molecule analogs, etc.) can yield data of special biological interest. A tip can be moved along a trajectory aligned with the flexure direction of the AFM cantilever, carrying it from solution to (for example) a protein surface and back again. Integrating the force curve (with suitable corrections for beadbead interactions) then yields an intermolecular mean-force potential, that is, a

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-75.jpg?height=405&width=1103&top_left_y=169&top_left_x=153)

Figure 15.5. A candidate ligand framework with a sharp tip.

high-resolution spatial map of the free energy of the intermolecular interaction. For probes with tip structures of biological interest, this information can be of direct biological relevance regardless of the apparent image resolution.

To facilitate topographical imaging, organic synthesis can be used to prepare ligands with stiff tips of considerable geometric acuity. For example, molecular mechanics calculations (MM2/CSC) indicate that the $\mathrm{H}$ atom of $\mathrm{R}-\mathrm{C} \equiv \mathrm{C}-\mathrm{H}$ has a transverse bending stiffness of $\sim 2 \mathrm{~N} / \mathrm{m}$ relative to an $s p^{3}$ carbon in the $R$ group (e.g., in a polycyclic ligand structure like that in Figure 15.5); the longitudinal $k_{\mathrm{s}}$ is $\geq 100 \mathrm{~N} / \mathrm{m}$. The effective tip radius for such a probe is $\sim 0.13 \mathrm{~nm}$.

Tips made by current microfabrication techniques have irregular structures with characteristic radii estimated to be $\sim 10 \mathrm{~nm}$ (Park Scientific Instruments, 1992). The molecular tips proposed here can have well-characterized structures of diverse types, attached in diverse orientations. Imaging specimens of known structure using multiple tips should permit discrimination and mapping of the tip types and orientations in a particular tip array. To take a simple example, positive, negative, and neutral tips will have distinct, contrasting responses to a bound charge.

Chemists frequently prepare derivatives of molecules to identify the original structure. Ligands used as molecular tips can include chemically reactive moieties that can be used to map sites of differing reactivity. This mode of operation will usually require prolonged dwell times at a candidate site, as opposed to steady scanning or rapid probing.

### 15.4.6. Solution-phase mechanosynthesis

Organic synthesis today offers powerful techniques for building molecular structures. Use of maneuverable molecular tips can add a fundamental novelty: flexible, positional control of sequences of synthetic steps based on control of local effective concentration. Receptors that bind reagent ligands can serve as tool holders for mechanosynthesis.

Molecular tip array systems enable approaches substantially different from those previously proposed (Drexler and Foster, 1990): Tip arrays and antibody technologies will enable the use of distinct receptors for reagents of different types, permitting a series of reactions without cycling the composition of the solution. With rapid, spontaneous dissociation no longer necessary for interchange, reagent ligands can be bound tightly; this enables larger effective concentration ratios and hence better site specificity.

a. Effective concentrations. Reagent reaction rates are by definition proportional to reagent effective concentrations (Section 8.3.3a). All else being equal, the effective concentration of a reagent is proportional to its spatial probability density. Modeling a reagent ligand as a thermally excited object, subject to a force $F$ pressing it against a barrier, to constraint by a transverse stiffness $k_{\mathrm{s}}$, and to an additional Gaussian jitter in the AFM mechanism with a root mean square amplitude $=\sigma_{\mathrm{AFM}}$, yields a probability density having a peak local concentration $\left(\mathrm{m}^{-3}\right)$

$$
\begin{equation*}
c_{\text {local }}=\frac{F}{2 \pi k T}\left(\frac{k T}{k_{\mathrm{s}}}+\sigma_{\mathrm{AFM}}^{2}\right)^{-1} \tag{15.4}
\end{equation*}
$$

Neglecting energetic and orientational effects (which can, when favorable, greatly increase the effective concentration), and provided that $k_{\mathrm{s}}$ is substantially less than the transverse stiffness in the reaction transition state (as is the case here), local concentration corresponds to effective concentration. Displacements of well under $0.01 \mathrm{~nm}$ are now routinely measurable in stationary tips (Albrecht, 1990), but jitter from ambient vibration is of this order (Drake et al., 1989). Assuming $\sigma_{\mathrm{AFM}}=0.01 \mathrm{~nm}, T=300 \mathrm{~K}, F=0.01 \mathrm{nN}$, and $k_{\mathrm{s}}=1.5 \mathrm{~N} / \mathrm{m}$ (between two structures with stiffnesses of $3 \mathrm{~N} / \mathrm{m}$ ) yields $c_{\text {local }} \approx 135 \mathrm{~nm}^{-3}$ $(\sim 225 \mathrm{M})$ at $300 \mathrm{~K}$. For comparison, mobile surface-residue thiol groups in proteins can exhibit effective concentrations exceeding $60 \mathrm{~nm}^{-3}$; interior residues often exhibit much larger values (Creighton, 1984).

Rate constants for ligand binding commonly exceed $10^{8} \mathrm{~nm}^{3} \mathrm{~s}^{-1}$. Antibody technologies commonly yield proteins that bind a chosen ligand with equilibrium ${ }^{\circ}$ dissociation constants on the order of $10^{-9} \mathrm{~nm}^{-3}$ (Bird et al., 1988; Huse et al., 1989). On exposure to a solution with a $10^{-6} \mathrm{~nm}^{-3}$ ligand concentration, reagent receptors with these properties will become occupied in $\sim 10^{-2} \mathrm{~s}$, and at equilibrium will remain occupied with probability $\sim .999$ (with these parameters, the mean waiting time for dissociation to occur is $\sim 10 \mathrm{~s})$. Application of mechanical load to a tip tends to increase its equilibrium probability of dissociation while decreasing its rate of dissociation; this behavior is compatible with the tip applications described here.

Under the conditions just specified, the peak enhancement in effective concentration of a reactive moiety on a molecular tip relative to the background solution concentration is $\sim\left(100 \mathrm{~nm}^{-3}\right) /\left(10^{-6} \mathrm{~nm}^{-3}\right)=10^{8}$. This localized, positionable enhancement in effective concentration can direct site-specific reactions on molecular structures attached to the bead. The transverse probability density distribution is Gaussian; with these parameters, the enhancement falls to background levels at a radius of $\sim 0.3 \mathrm{~nm}$, or about one atomic diameter. Thus, this mechanism for positional control can produce reaction rate differentials on the order of $10^{8}$ between otherwise chemically equivalent sites separated by two to three bond lengths.

b. Anticipated synthetic capabilities. The choice of reagent ligands is constrained by requirements for chemical compatibility. Protein molecules have been suggested as reagent receptors; they have reactive functional groups and ordinarily exist in an aqueous medium. Modifications (including immobilization
itself) may help stabilize proteins, permitting their use in polar, nonaqueous media.

Reagent ligands also must not react with one another at substantial rates in solution, unless the resulting by-products are harmless to the process. Low concentrations reduce this problem, and a system that steadily flushes the AFM cell with freshly mixed reagent solution (ensuring a low residence time) can further reduce unwanted reactions. If the residence time is $\sim 100 \mathrm{~s}$, the effective-concentration ratio is $\sim 10^{8}$, and a typical mechanosynthetic reaction time is $\sim 1 \mathrm{~s} \mathrm{(at} \mathrm{an}$ effective concentration of $100 \mathrm{~nm}^{-3}$ ), then the concentration of side-reaction products will be $\sim 10^{-12} \mathrm{~nm}^{-3}$, or $\sim 10^{-6}$ that of the reagents.

A mature AFM-based mechanosynthetic technology could potentially perform syntheses involving $>10^{5}$ sequential steps in the presence of $\sim 100$ chemically equivalent sites with only a small probability of failure resulting from reactions with uncontrolled reagent molecules in solution. In an operating system, each reaction step removes a reagent ligand from a receptor that is promptly recharged by a molecule from the solution. Each reaction step can be tested for success by AFM imaging, to ensure completion. The extension of tiparray technology to encompass solution-phase mechanosynthesis will require a multidisciplinary collaboration with synthetic organic chemistry playing a prominent role. A major objective is the identification of building blocks that are (1) accessible via conventional solution-phase synthesis, and (2) adequate for use in building molecular machine systems, given positional control of the expected reliability; initial studies have been undertaken by M. Krummenacker.

### 15.4.7. Summary

Analysis suggests that AFMs with arrays of molecular tips may have substantial advantages over conventional AFM systems for the intensive study of molecular-scale specimens, including protein molecules. The chief sacrifice is a drastic reduction of the effective substrate area, which is limited to a fraction of the bead diameter. The opportunity to select among $\sim 10^{6}$ tips, guided by imaging results and without interrupting system operation, sidesteps the requirement for good tip yield and durability imposed by single-tip systems. Selection of tips with desirable mechanical and orientational properties from a population comprising well-defined molecular structures will enable more thorough and unambiguous characterization of samples. Use of reactive molecules as tips will enable nanofabrication by positional control of chemical synthesis. The estimated reliability is sufficient to enable $>10^{5}$ sequential steps, enabling the construction of molecular objects $\sim 10^{3}$ times larger than typical protein molecules and existing products of chemical synthesis.

### 15.5. Conclusions

Present technology can be extended to build macromolecular objects and systems in any of several ways:

- Biotechnology (and protein engineering in particular) can be extended to make $\sim 300$ monomer molecular objects capable of forming larger structures of indefinite size and complexity by Brownian assembly. Problems with design are the chief obstacles to this path.
- Solution-phase synthesis can be used to make $\sim 50$ monomer molecular objects with greater cost per unit mass, but with lessened design difficulty. Again, with suitable design, these objects can be made to self-assemble to form larger and more complex objects. Problems on this path seem smaller in total, but are more interdisciplinary, requiring innovations both in synthesis and design.
- Solution-phase mechanosynthesis guided by AFM mechanisms appears feasible, and could be used to build molecular objects containing $\sim 10^{5}$ highly crosslinked monomers without need for Brownian assembly. This path promises the greatest speed and flexibility of molecular construction, but its implementation requires still broader interdisciplinary collaboration.

Opportunities for hybrid approaches are evident. Biotechnology (and the stockpile of molecular components found in nature) can provide devices that can be incorporated into other structures. Solution-phase synthesis of mediumsized building blocks could provide components useful in mechanosynthesis. Molecular-tip AFM mechanisms could be used to characterize the products of biotechnological or chemical experiments, reducing the time required to detect and correct errors.

Each of the three approaches surveyed in this chapter grows out of experimental research already in progress; each can yield short-term scientific rewards while developing capabilities useful in building solution-phase molecular machine systems. Making new systems work in the laboratory is far more difficult than merely surveying possible approaches. By the same token, however, it is important to identify areas where successful experimental work can yield capabilities that open new fields of endeavor. If work is difficult, then it is best applied where the rewards seem large.

Some open problems. Much of this chapter can be taken as a description of open experimental problems. On the theoretical side, it would be useful to identify sets of compatible building-block molecules for use in solution-phase synthesis or in mechanosynthesis. This is a system design problem with numerous chemical constraints, not a problem of organic synthesis per se; it will not be solved by the traditional research strategy of synthesizing individual molecules having interesting structures or useful interactions with living organisms. Molecular CAD systems for the design of structures and syntheses based on such building blocks would be of great value.

[^40]: Save for editing and partial updating of citations, the material in this section is drawn from Drexler (1989b).
[^41]: In the following sections, values cited as $\sim 7 \mathrm{maJ}$ are to be regarded as round numbers, representing $\sim 1 \mathrm{kcal} / \mathrm{mole}$.
[^42]: Portions of the discussion in this section are based on Drexler $(1991 b, 1992)$.