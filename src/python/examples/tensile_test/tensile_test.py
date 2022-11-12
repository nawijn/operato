import numpy as np

from operato.keywords.starter import Begin, Bcs, End, MatPlasJohns, Node
from operato.starter import Starter

materials = {
    "MatPlasJohns": {
        "rho_i": 7.8e-6,
        "E": 210,
        "nu": 0.3,
        "i_flag": 1,
        "sigma_y": 0.3,
        "UTS": 0.686,
        "eps_uts": 0.129,
        "eps_max_p": 0.0,
    }
}

node_data = np.recfromcsv(
    "nodes.csv",
    delimiter=";",
    names=("node_ids", "xc", "yc", "zc"),
)


def main():

    starter = Starter(add_separator=True)
    # /BEGIN
    starter.add(
        Begin(
            "tensile_test",
            input_mass_unit="kg",
            input_length_unit="mm",
            input_time_unit="ms",
            work_mass_unit="kg",
            work_length_unit="mm",
            work_time_unit="ms",
        )
    )

    # /MAT/PLAS_JOHNS
    starter.add(
        MatPlasJohns(mat_id=2, mat_title="Steel_DP600", **materials["MatPlasJohns"])
    )

    # /NODE
    starter.add(Node(node_ids=node_data, xc_yc_zc=node_data))

    # /BCS
    starter.add(
        Bcs(
            bcs_id=1,
            bcs_title="Constraint 1",
            trarot=[1, 1, 1, 1, 1, 1],
            skew_id=0,
            grnd_id=2,
        )
    )

    # /BCS
    starter.add(
        Bcs(
            bcs_id=2,
            bcs_title="Constraint 2",
            trarot=[0, 1, 1, 1, 1, 1],
            skew_id=0,
            grnd_id=3,
        )
    )

    # /END
    starter.add(End())
    starter.write()


if __name__ == "__main__":
    main()
