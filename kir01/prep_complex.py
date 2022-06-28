import sys

"""
Create "complex.pdb" from a complex H/L and A where all resedues in legand replaced with "LIG"
"""

inp_file = sys.argv[1]
out_file = "complex.pdb"

# out_dir  = sys.argv[2]
# out_file_rec = f"{out_dir}/rec.pdb"
# out_file_lig = f"{out_dir}/lig.pdb"

# #pdbl.retrieve_pdb_file(infile[0], pdir=infile[1], file_format="pdb")
# structure = parser.get_structure('kir', inp_file)
#
# for model in structure:
#
#     for chain in structure.get_chains():
#         io.set_structure(chain)
#         io.save(chain.get_id() + ".pdb")


def replace():
    """ Split a pdb file in different pdb files by chains: [H,L] and [A]
    """

    f = open(inp_file, "r")
    pdblines = f.readlines()
    f.close()

    # Chains selection :
    out = []

    for i, line in enumerate(pdblines):
        if line[0:4] == 'ATOM':
            if line[21] == 'H' or line[21] == 'L':
                out.append(line)
            else:
                new_line = line[:17] + 'LIG' + line[20:]
                out.append(new_line)
        if line[0:3] == 'TER':
            out.append(line)
        if line[0:3] == 'END' and i>=len(pdblines)-2:
            out.append(line)

    # fix TER if missing
    if out[-1][0:3] != 'TER' and out[-1][0:3] != 'END':
        out.append('TER')

    out.append('')

    f = open(out_file, 'w')
    f.writelines(out)
    f.close()


if __name__ == '__main__':
    replace()
    # create the file in current dir that needed for the next step
    f = open("input.dat", 'w')
    out = []
    out.append(out_file)
    f.writelines(out)
    f.close()
