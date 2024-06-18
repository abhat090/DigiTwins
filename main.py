from Parser.Parser import DataParser


parser_options = {
    "preprocess": True,
    "units_file": "Data/Plant1_Heat_Loop_Units2.csv",
    "connections_file": "Data/Plant1_Heat_Loop_Streams2.csv",
    "output_file": "script_P1.py"
}


def run_parser():
    p = DataParser(None, parser_options)
    p.gen_script()
    return


if __name__ == '__main__':
    run_parser()
