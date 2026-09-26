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

## Runnable scientific baseline

This baseline treats the analysis as one Poisson counting bin. Given an integer observed count n and an assumed exactly known background b, it finds the nonnegative signal count s for which the lower-tail probability P(N ≤ n | b+s) is 0.1. Dividing by exposure and a single efficiency yields an upper event rate in counts per kilogram-day. The computation is a classical one-sided construction with a physical zero-signal boundary; it does not model background uncertainty or guarantee every desired coverage property after additional selection rules.

Run `python src/main.py --observed 0 --background 0 --exposure-kg-day 100 --efficiency 0.8`. The zero-background, zero-count check is s = −ln(0.1) ≈ 2.302585 counts. No dark-matter cross-section appears in this output: converting a count-rate bound into a mass-dependent cross-section requires a documented halo and interaction model, germanium recoil or electron response, thresholds, resolution, acceptance as a function of energy, and the signal spectrum. Avoid interpreting this baseline as an experimental exclusion curve.

## Validation and scope

The calculations in `src/main.py` are transparent baseline models intended for reproducibility and extension. Inputs and assumptions should be reported alongside outputs; numerical agreement with a plotted trace alone does not validate a material-specific prediction. New physical terms should be accompanied by dimensional checks and independent limiting-case comparisons.

## Contact

**Athul Prem** — [GitHub profile](https://github.com/premathul). For scientific discussion or collaboration, open an issue in this repository or reach out through my GitHub profile.
