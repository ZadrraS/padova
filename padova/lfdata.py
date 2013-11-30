#!/usr/bin/env python
# encoding: utf-8
"""
Read/represent luminosity function tables.
"""

import linecache

import numpy as np
from astropy.table import Table

from .basereader import BaseReader


class LFTable(BaseReader):
    """Read a luminosity function table (output from the Padova CMD interface).

    Attributes
    ----------
    metadata : list
        List of lines from the metadata found at the top of the ischrone
        table file.
    lfs : list
        List of :class:`LuminosityFunction` instances in the table.
    
    Parameters
    ----------

    fname : str
        Filename of LF table to read (either a .dat or a .dat.gz).
    """
    def __init__(self, fname):
        super(LFTable, self).__init__(fname)

    def _read(self):
        """Read isochrone table and create LuminosityFunction instances."""
        start_indices = self._prescan_table()
        print "start_indices",
        print start_indices
        self._lf_specs = self._read_lf_specs(start_indices)
        self.metadata = self._read_metadata(0, start_indices[0])
        self.lfs = self._read_lfs(start_indices)
        linecache.clearcache()

    def _read_lfs(self, start_indices):
        """Extract isochrones from the table, creating individual
        :class:`Isochrone` instances.
        """
        lfs = []
        for i, (start_index, meta) in enumerate(
                zip(start_indices, self._lf_specs)):
            if i < len(start_indices) - 1:
                end_index = start_indices[i + 1]
            else:
                end_index = self._linecount()
            isoc = self._read_lf(start_index, end_index, meta)
            lfs.append(isoc)
        return lfs

    def _read_lf_specs(self, start_indices):
        """Produce a list of the age and metallicity specifications for
        each isochone in the table.
        """
        specs = []
        for i in start_indices:
            line = linecache.getline(self.fname, i + 1).rstrip().split()
            z = float(line[7])
            age = float(line[10])
            specs.append({"Z": z, "age": age})
        return specs

    def _read_lf(self, start_index, end_index, meta):
        """Read a single LF, between `start_index` and `end_index`."""
        header = self._read_header(start_index)
        # build datatype for structured array
        dt = [(cname, np.float) for cname in header]
        data = np.empty(end_index - start_index - 2, dtype=np.dtype(dt))
        for j, i in enumerate(xrange(start_index + 2, end_index)):
            parts = linecache.getline(self.fname, i + 1).rstrip('\n').split()
            for val, (cname, typ) in zip(parts, dt):
                if typ == np.float:
                    data[cname][j] = float(val)
                elif typ == np.int:
                    data[cname][j] = int(val)
                else:
                    data[cname][j] = val
        tbl = Table(data,
                meta={"header": self.metadata,
                      "Z": meta['Z'],
                      'age': meta['age']})
        lf = LuminosityFunction(tbl)
        return lf


class LuminosityFunction(object):
    """Holds a single luminosity function (single age, metallicity) for
    several bandpasses.
    
    Parameters
    ----------

    table : :class:`astropy.table.Table` instance
        A table with luminosity function data. This table must also have
        metadata with age and metallicity information. This table is typically
        generated by :class:`LFTable`.
    """
    def __init__(self, table):
        super(LuminosityFunction, self).__init__()
        self.table = table

    @property
    def z(self):
        """Metallicity of this isochrone."""
        return self.table.meta['Z']

    @property
    def age(self):
        """Age of this isochrone (yr)."""
        return self.table.meta['age']

    @property
    def z_code(self):
        """Code string for the metallicity. This is a 4-digit code for the
        metallicity (with leading zeros). E.g. ``z=0.012`` will be ``0120``.
        """
        z_str = "%.4f" % self.z
        z_str = z_str[2:]
        return z_str

    @property
    def age_code(self):
        """Code string for the age. This is in format ``tt.tt`, giving the
        log age.
        """
        return "%05.2f" % np.log10(self.age)

    @property
    def info(self):
        """Info about how this isochrone was generated
        (header from CMD output).
        """
        return self.table.meta['header']

    @property
    def filter_names(self):
        """A list of (column) names of the filters included in this isochrone.
        """
        cnames = self.table.colnames
        non_mag_cnames = ['age/yr', 'bin(mag)', 'mbol']
        # Normally I'd use sets, but column ordering is important
        return [name for name in cnames if name not in non_mag_cnames]
