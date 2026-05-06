"""cross_paper -- cross-paper operators for the package."""
from gaia.lang import contradiction, support

from .paper_puppin2020 import (
    gcn_1544d55444d743c8,
    gcn_4ad259a13be9454a,
    gcn_ffcf3464e99c47ed,
    gcn_5e907da32c114d34,
)
from .paper_zhao2025 import (
    gcn_3f848904ab0d4b48,
    gcn_e4a5cac31481497c,
)
from .paper_sajedi2022 import (
    gcn_762777de8c644c17,
    gcn_8c3c520295d7488c,
)

zhao_finite_temp_supports_arpes_mass = support(
    [gcn_e4a5cac31481497c],
    gcn_1544d55444d743c8,
    reason=(
        "The Zhao et al. finite-temperature HSE-SOC/AIMD claim computes a "
        "300 K CsPbBr3 hole mass of 0.265 m0 and explicitly states agreement "
        "with the ARPES measurement used as the package root; this supports the "
        "root measurement as a reproducible finite-temperature benchmark, while "
        "also motivating the thermal-disorder interpretation branch."
    ),
    prior=0.78,
)

sajedi_gw_context_supports_arpes_mass = support(
    [gcn_8c3c520295d7488c],
    gcn_1544d55444d743c8,
    reason=(
        "The Sajedi et al. G0W0 claim gives an orthorhombic CsPbBr3 hole mass "
        "near the ARPES-scale value. Because it is a theory baseline with "
        "different extraction assumptions, this is weak contextual support rather "
        "than a direct replication of the root measurement."
    ),
    prior=0.58,
)

feynman_mass_supports_polaron_model = support(
    [gcn_ffcf3464e99c47ed],
    gcn_5e907da32c114d34,
    reason=(
        "The more atomic Feynman-polaron mass calculation gives m_pol = 0.24 m_e "
        "from m0 = 0.17 m_e and alpha = 1.81, which is the numerical core of the "
        "broader claim that the polaron model reproduces the ARPES mass."
    ),
    prior=0.90,
)

thermal_mass_renorm_supports_finite_temp_model = support(
    [gcn_3f848904ab0d4b48],
    gcn_e4a5cac31481497c,
    reason=(
        "The thermal-fluctuation mass-renormalization claim quantifies the change "
        "from an ideal 0 K hole mass near 0.149 m0 to a 300 K AIMD value of 0.265 m0, "
        "directly supporting the finite-temperature explanation of the ARPES-scale mass."
    ),
    prior=0.88,
)

arpes_polaron_signature_vs_gw_no_polaron = contradiction(
    gcn_4ad259a13be9454a,
    gcn_762777de8c644c17,
    reason=(
        "The Puppin-side claim treats the ARPES effective-mass enhancement as a valid "
        "signature of polaronic mass dressing even without resolved phonon replicas, "
        "whereas the Sajedi-side claim says the ARPES-observed effective mass can be "
        "accounted for by a G0W0 quasiparticle baseline and does not require additional "
        "Fröhlich-polaron mass renormalization. open_problem: which ARPES-observable "
        "or matched theory baseline can distinguish genuine electron-phonon polaron "
        "mass dressing from quasiparticle/structural baseline effects in CsPbBr3?"
    ),
    prior=0.90,
)
arpes_polaron_signature_vs_gw_no_polaron.title = "ARPES polaron signature vs G0W0 baseline"
