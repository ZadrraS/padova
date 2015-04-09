#!/usr/bin/env python
# encoding: utf-8
"""
CMD Settings reference.

This module contains settings options, defaults and validation functions.
"""
from collections import OrderedDict


INTERP = {'default': 0,
          'improved': 1}


PHOT = {
    "2mass_spitzer": " 2MASS + Spitzer (IRAC+MIPS)",
    "2mass_spitzer_wise": " 2MASS + Spitzer (IRAC+MIPS) + WISE",
    "2mass": " 2MASS JHKs",
    "ubvrijhk": "UBVRIJHK (cf. Maiz-Apellaniz 2006 + Bessell 1990)",
    "bessell": "UBVRIJHKLMN (cf. Bessell 1990 + Bessell & Brett 1988)",
    "akari": "AKARI",
    "batc": "BATC",
    "megacam": "CFHT/Megacam u*g'r'i'z'",
    "dcmc": "DCMC",
    "denis": "DENIS",
    "dmc14": "DMC 14 filters",
    "dmc15": "DMC 15 filters",
    "eis": "ESO/EIS (WFI UBVRIZ + SOFI JHK)",
    "wfi": "ESO/WFI",
    "wfi_sofi": "ESO/WFI+SOFI",
    "wfi2": "ESO/WFI2",
    "galex": "GALEX FUV+NUV (Vega) + Johnson's UBV",
    "galex_sloan": "GALEX FUV+NUV + SDSS ugriz (all AB) ",
    "UVbright": "HST+GALEX+Swift/UVOT UV filters",
    "acs_hrc": "HST/ACS HRC",
    "acs_wfc": "HST/ACS WFC",
    "nicmosab": "HST/NICMOS AB",
    "nicmosst": "HST/NICMOS ST",
    "nicmosvega": "HST/NICMOS vega",
    "stis": "HST/STIS imaging mode",
    "wfc3ir": "HST/WFC3 IR channel (final throughputs)",
    "wfc3uvis1": "HST/WFC3 UVIS channel, chip 1 (final throughputs)",
    "wfc3uvis2": "HST/WFC3 UVIS channel, chip 2 (final throughputs)",
    "wfc3_medium": "HST/WFC3 medium filters (UVIS1+IR, final throughputs)",
    "wfc3": "HST/WFC3 wide filters (UVIS1+IR, final throughputs)",
    "wfpc2": "HST/WFPC2 (Vega, cf. Holtzman et al. 1995)",
    "kepler": "Kepler + SDSS griz + DDO51 (in AB)",
    "kepler_2mass": "Kepler + SDSS griz + DDO51 (AB) + 2MASS (~Vega)",
    "ogle": "OGLE-II",
    "panstarrs1": "Pan-STARRS1",
    "sloan": "SDSS ugriz",
    "sloan_2mass": "SDSS ugriz + 2MASS JHKs",
    "sloan_ukidss": "SDSS ugriz + UKIDSS ZYJHK",
    "swift_uvot": "SWIFT/UVOT UVW2, UVM2, UVW1,u (Vega) ",
    "spitzer": "Spitzer IRAC+MIPS",
    "stroemgren": "Stroemgren-Crawford",
    "suprimecam": "Subaru/Suprime-Cam (AB)",
    "tycho2": "Tycho VTBT",
    "ukidss": "UKIDSS ZYJHK (Vega)",
    "visir": "VISIR",
    "vista": "VISTA ZYJHKs (Vega)",
    "washington": "Washington CMT1T2",
    "washington_ddo51": "Washington CMT1T2 + DDO51"}


# available tracks
MODELS = {
    'parsec12s': ('parsec_CAF09_v1.2S',
                  'PARSEC version 1.2S,  Tang et al. (2014), '
                  'Chen et al. (2014)'),
    'parsec11': ('parsec_CAF09_v1.1',
                 'PARSEC version 1.1, With revised diffusion+overshooting in '
                 'low-mass stars, and improvements in interpolation scheme.'),
    'parsec10': ('parsec_CAF09_v1.0', 'PARSEC version 1.0'),
    '2010': ('gi10a',
             'Marigo et al. (2008) with the Girardi et al. (2010) '
             'Case A correction for low-mass, low-metallicity AGB tracks'),
    '2010b': ('gi10b',
              'Marigo et al. (2008) with the Girardi et al. (2010) '
              'Case B correction for low-mass, low-metallicity AGB tracks'),
    '2008': ('ma08',
             'Marigo et al. (2008): Girardi et al. (2000) up to early-AGB '
             '+ detailed TP-AGB from Marigo & Girardi (2007) '
             '(for M <= 7 Msun) + Bertelli et al. (1994) (for M > 7 Msun) + '
             'additional Z=0.0001 and Z=0.001 tracks.'),
    '2002': ('gi2000',
             'Basic set of Girardi et al. (2002) : Girardi et al. (2000) '
             '+ simplified TP-AGB (for M <= 7 Msun) '
             '+ Bertelli et al. (1994) (for M > 7 Msun) '
             '+ additional Z=0.0001 and Z=0.001 tracks.')
}


CARBON_STARS = {
    'loidl': ('loidl01',
              'Loidl et al. (2001) (as in Marigo et al. (2008) and '
              'Girardi et al. (2008))'),
    'aringer': ('aringer09',
                "Aringer et al. (2009) (Note: The interpolation scheme has "
                "been slightly improved w.r.t. to the paper's Fig. 19.")
}


CIRCUM_MSTARS = {
    'nodustM': ('no dust', ''),
    'sil': ('Silicates', 'Bressan et al. (1998)'),
    'AlOx': ('100% AlOx', 'Groenewegen (2006)'),
    'dpmod60alox40': ('60% Silicate + 40% AlOx', 'Groenewegen (2006)'),
    'dpmod': ('100% Silicate', 'Groenewegen (2006)')
}


CIRCUM_CSTARS = {
    'nodustC': ('no dust', ''),
    'gra': ('Graphites', 'Bressan et al. (1998)'),
    'AMC': ('100% AMC', 'Groenewegen (2006)'),
    'AMCSIC15': ('85% AMC + 15% SiC', 'Groenewegen (2006)')
}


ISOC_VAL = {
    0: ('Single isochrone', ''),
    1: ('Sequence of isochrones at constant Z', ''),
    2: ('Sequence of isochrones at constant t (variable Z)',
        'Groenewegen (2006)')
}


def get_defaults():
    v = (('binary_frac', 0.3),
         ('binary_kind', 1),
         ('binary_mrinf', 0.7),
         ('binary_mrsup', 1),
         ('cmd_version', 2.3),
         ('dust_source', 'nodust'),
         ('dust_sourceC', 'AMCSIC15'),
         ('dust_sourceM', 'dpmod60alox40'),
         ('eta_reimers', 0.2),
         ('extinction_av', 0),
         ('icm_lim', 4),
         ('imf_file', 'tab_imf/imf_chabrier_lognormal.dat'),
         ('isoc_age', 1e7),
         ('isoc_age0', 12.7e9),
         ('isoc_dlage', 0.05),
         ('isoc_dz', 0.0001),
         ('isoc_kind', 'parsec_CAF09_v1.2S'),
         ('isoc_lage0', 6.6),
         ('isoc_lage1', 10.13),
         ('isoc_val', 0),
         ('isoc_z0', 0.0001),
         ('isoc_z1', 0.03),
         ('isoc_zeta', 0.02),
         ('isoc_zeta0', 0.008),
         ('kind_cspecmag', 'aringer09'),
         ('kind_dust', 0),
         ('kind_interp', 1),
         ('kind_mag', 2),
         ('kind_postagb', -1),
         ('kind_pulsecycle', 0),
         ('kind_tpagb', 3),
         ('lf_deltamag', 0.2),
         ('lf_maginf', 20),
         ('lf_magsup', -20),
         ('mag_lim', 26),
         ('mag_res', 0.1),
         ('output_evstage', 0),
         ('output_gzip', 0),
         ('output_kind', 0),
         ('photsys_file', 'tab_mag_odfnew/tab_mag_bessell.dat'),
         ('photsys_version', 'yang'),
         ('submit_form', 'Submit'))
    return OrderedDict(v)
