"""Loading the topology data extracted from the thesis (topology 1, 52 nodes)."""
import json
import os
import numpy as np

_DIR = os.path.dirname(os.path.abspath(__file__))
_DATA_FILE = os.path.join(_DIR, "..", "topology_data.json")


class Topology:
    """Topology 1 of the thesis: "top_1_maia_52_65_30_CordMod".

    Attributes
    ----------
    n : int                        number of nodes (52)
    xy : ndarray (n,2)             normalized node coordinates
    A  : ndarray (n,n)             adjacency matrix (1 if link exists)
    D  : ndarray (n,n)             delay matrix (mapping) used by ACO heuristic
    AT : ndarray (n,n)             one-way delay of each link (ms)
    VA : ndarray (n,n)             link capacity / bandwidth (Mbps)
    tds : ndarray (K,5)            application demands
                                   col0=source, col1=dest, col2=flow Mbps,
                                   col3=max end-to-end delay (ms),
                                   col4=priority coefficient
    """

    def __init__(self):
        with open(_DATA_FILE, "r") as fh:
            data = json.load(fh)
        self.xy = np.array(data["xy"], dtype=float)
        self.A = np.array(data["A"], dtype=np.float64)
        self.AT = np.array(data["AT"], dtype=np.float64)
        self.VA = np.array(data["VA"], dtype=np.float64)
        self.tds = np.array(data["tds"], dtype=np.float64)
        self.n = self.A.shape[0]
        # The ACO heuristic "eta" uses the link distance ("D = A" in the code,
        # i.e. unit-cost / hop-based heuristic). We keep D as the adjacency to
        # mirror mgrafos14g exactly (eta = 1/D on existing links).
        self.D = self.A.astype(np.float64).copy()
        self.napp = self.tds.shape[0]
        self.name = "maia52"

    @classmethod
    def from_arrays(cls, name, A, AT, VA, xy, tds):
        """Build a Topology from raw arrays (used by synthetic generators)."""
        obj = cls.__new__(cls)
        obj.A = np.asarray(A, dtype=np.float64)
        obj.AT = np.asarray(AT, dtype=np.float64)
        obj.VA = np.asarray(VA, dtype=np.float64)
        obj.xy = np.asarray(xy, dtype=np.float64)
        obj.tds = np.asarray(tds, dtype=np.float64)
        obj.n = obj.A.shape[0]
        obj.D = obj.A.astype(np.float64).copy()
        obj.napp = obj.tds.shape[0]
        obj.name = name
        return obj

    def with_load(self, factor):
        """Copy of the topology with all flow demands scaled by ``factor``."""
        import copy
        obj = copy.copy(self)
        obj.tds = self.tds.copy()
        obj.tds[:, 2] = self.tds[:, 2] * factor
        return obj

    def node_degree(self):
        return int(self.A.sum(axis=1).max())

    def __repr__(self):
        return (f"Topology({self.name}: n={self.n}, "
                f"edges={int(self.A.sum()//2)}, apps={self.napp})")


def load_topology():
    return Topology()