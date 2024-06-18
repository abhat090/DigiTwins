from Parser.Network import *
import pandas as pd


class DataParser:
    def __init__(self, _metadata, _options):
        self.preprocess = _options["preprocess"]
        self.units_file = _options["units_file"]
        self.connections_file = _options["connections_file"]
        self.output_file = _options["output_file"]

        self.u_net = UnitNetwork()

        if self.preprocess:
            df_unit = pd.read_csv(self.units_file)
            df_conn = pd.read_csv(self.connections_file)

            for idx, row in df_unit.iterrows():
                temp_node = self.u_net.add_node(row["Unit Name"],
                                                row["Unit Identifier"],
                                                row["Unit Type"])

                if not pd.isna(df_unit.at[idx, "Q"]):
                    temp_node.set_q(row["Q"])

            for idx, row in df_conn.iterrows():
                temp_conn = self.u_net.connect(self.u_net.get_node(row["Start Unit Name"]),
                                               self.u_net.get_node(row["End Unit Name"]),
                                               row["Start Unit Port"],
                                               row["End Unit Port"],
                                               row["Label"])

                if not pd.isna(df_conn.at[idx, "fluid"]):
                    temp_conn.update_fluid(row["fluid"])

                if not pd.isna(df_conn.at[idx, "mass flow rate"]):
                    temp_conn.update_mfr(row["mass flow rate"])

                if not pd.isna(df_conn.at[idx, "temperature"]):
                    temp_conn.update_temp(row["temperature"])

                if not pd.isna(df_conn.at[idx, "pressure"]):
                    temp_conn.update_pressure(row["pressure"])

            print("Nodes:")
            self.u_net.print_nodes()
            print("\n")
            print("Connections:")
            self.u_net.print_connections()

            return

    def gen_script(self):
        with open(self.output_file, "w") as script:
            script.write(f"# Unit Nodes: \n")

            # Generate Nodes
            for node in self.u_net.get_nodes().values():
                script.write(f"{node.name} = components.{node.typeName}('{node.id}')\n")

            script.write(f"# End Nodes \n")
            script.write(f"# Streams: \n")

            # Generate Connections
            for conn in self.u_net.get_connections().values():
                script.write(f"c{conn.label} = connections.{conn.type}({conn.output.name}, '{conn.out_port}', "
                             f"{conn.input.name}, '{conn.in_port}', label='{conn.label}')\n")

            script.write(f"# End Streams \n")
            script.write(f"# Node Boundary Conditions")

            # Generate Boundary Conditions
            # Node Boundaries
            for node in self.u_net.get_nodes().values():
                if node.Q:
                    script.write(f"{node.name}.set_attr(Q=meta['{node.name}.Q'])\n")

            script.write(f"# Connection Boundary Conditions\n")

            # Connection Boundaries
            for conn in self.u_net.get_connections().values():
                if conn.fluid:
                    script.write(f"c{conn.label}.set_attr(fluid={{meta['working_fluid']: 1}})\n")
                if conn.mfr:
                    script.write(f"c{conn.label}.set_attr(m=meta['c{conn.label}.mass_flow_rate'])\n")
                if conn.temp:
                    script.write(f"c{conn.label}.set_attr(T=meta['c{conn.label}.temperature'])\n")
                if conn.pressure:
                    script.write(f"c{conn.label}.set_attr(p=meta['c{conn.label}.pressure'])\n")

            script.write(f"# Node terms for metadata dictionary\n")
            script.write(f"# Unit Nodes\n")

            # Node terms
            for node in self.u_net.get_nodes().values():
                if node.Q:
                    script.write(f"'{node.name}.Q': {node.Q},\n")

            script.write(f"# Connections\n")

            # Connection terms
            for conn in self.u_net.get_connections().values():
                if conn.fluid:
                    script.write(f"'working_fluid': '{conn.fluid}',\n")
                if conn.mfr:
                    script.write(f"'c{conn.label}.mass_flow_rate': {conn.mfr},\n")
                if conn.temp:
                    script.write(f"'c{conn.label}.temperature': {conn.temp},\n")
                if conn.pressure:
                    script.write(f"'c{conn.label}.pressure': {conn.pressure},\n")

