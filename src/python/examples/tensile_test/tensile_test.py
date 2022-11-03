from operato.starter import Starter

import numpy as np


def main():

    nodes = np.recfromcsv(
        "nodes.csv",
        delimiter=";",
        names=("node_ids", "xc", "yc", "zc"),
    )

    starter = Starter()
    starter["BEGIN"](runname="tensile_test")

    starter["NODE"](node_ids=nodes, xc_yc_zc=nodes)

    starter["END"]()
    starter.write()


if __name__ == "__main__":
    main()
