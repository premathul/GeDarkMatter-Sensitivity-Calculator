# GeDarkMatter-Sensitivity-Calculator

GeDarkMatter-Sensitivity-Calculator is a research-oriented Python framework for estimating the expected sensitivity of low-background germanium dark-matter searches under explicit assumptions about signal, background, detector efficiency, resolution, threshold, exposure, and statistical treatment. The project is intended to complement low-energy recoil Monte Carlo calculations by providing the next analysis layer: once a signal model and detector response are defined, this repository evaluates how strongly an experiment could distinguish or constrain that signal.

The emphasis of the project is transparency. Sensitivity curves can appear deceptively simple, but they depend on many assumptions that are often distributed across detector, astrophysical, and statistical models. This repository keeps those ingredients separate. The user supplies expected signal and background counts, exposure scaling, and analysis choices; the code then evaluates common summary statistics without hiding the underlying definitions.

The current implementation includes expected-count scaling, Poisson log likelihoods, Asimov discovery significance, simple background-dominated signal-to-noise estimates, and a one-parameter signal-strength scan. These utilities are not intended to replace a complete experimental likelihood framework. Their purpose is to provide validated building blocks that can later be extended to nuisance parameters, profile-likelihood ratios, expected upper limits, sensitivity bands, and systematic uncertainty propagation.

For signal counts s_i and known background counts b_i, the Asimov discovery significance is

Z_A = sqrt( 2 sum_i [ (s_i+b_i) ln(1+s_i/b_i) - s_i ] ).

In the limit where signal is much smaller than background, the familiar approximate scaling approaches s/sqrt(b). The repository exposes both forms so that users can see when the Gaussian approximation begins to break down.

Installation is performed with

\`\`\`bash
git clone https://github.com/premathul/GeDarkMatter-Sensitivity-Calculator.git
cd GeDarkMatter-Sensitivity-Calculator
python -m pip install -e .
\`\`\`

The long-term goal is to support publication-quality sensitivity calculations for germanium rare-event detectors using modular likelihoods. Planned extensions include profile likelihoods with nuisance parameters, background-normalization uncertainty, energy-dependent efficiencies, detector-response matrices, expected upper limits, toy-Monte-Carlo coverage studies, and interfaces to physically validated Ge recoil spectra.

A sensitivity result should always be accompanied by the assumptions that produced it: signal model, exposure, energy range, binning, threshold, efficiency, detector resolution, background model, statistical method, and software version. The project is designed to make those assumptions explicit and reproducible.

## Contact

**Athul Prem**

For scientific discussion, collaboration, or suggestions related to this project, please contact Athul Prem through the GitHub account associated with this repository.
