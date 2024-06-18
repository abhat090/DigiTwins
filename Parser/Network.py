import math

def utype_custom(_in, _out):
    custom_utype = {
        "in": _in,
        "out": _out
    }
    return custom_utype

utype_Source = {"in": 0, "out": 1}
utype_Merge = {"in": 2, "out": 1}
utype_Splitter = {"in": 1, "out": 2}
utype_SimpleHeatExchanger = {"in": 1, "out": 1}
utype_Sink = {"in": 1, "out": 0}

get_utype = {
    "Source": utype_Source,
    "Splitter": utype_Splitter,
    "Merge": utype_Merge,
    "SimpleHeatExchanger": utype_SimpleHeatExchanger,
    "Sink": utype_Sink
}


class UnitNode:
    def __init__(self, _name, _id, _type, _type_name):
        self.name = _name
        self.id = _id
        self.type = _type
        self.typeName = _type_name
        self.Q = None

        self.inputs = []
        self.outputs = []

        self.connections = []
        return

    def set_q(self, _q):
        self.Q = _q

    def able_to_connect(self):
        return len(self.outputs) < self.type["out"]

    def able_to_receive(self):
        return len(self.inputs) < self.type["in"]

    def connect_to(self, _node, _conn):
        self.outputs.append(_node)
        self.connections.append(_conn)
        return

    def receive_from(self, _node, _conn):
        self.inputs.append(_node)
        self.connections.append(_conn)
        return

    def get_output(self, index):
        if type["out"] == 0:
            return None
        return self.outputs[index]

    def get_input(self, index):
        if type["in"] == 0:
            return None
        return self.inputs[index]


class UnitConnection:
    def __init__(self, _label, _out, _in):
        self.output = _out
        self.input = _in

        self.out_port = None
        self.in_port = None

        self.type = "Connection"
        self.label = _label

        self.fluid = None
        self.mfr = None
        self.temp = None
        self.pressure = None

    def update_ports(self, _pout, _pin):
        self.out_port = _pout
        self.in_port = _pin

    def update_fluid(self, _fluid):
        self.fluid = _fluid

    def update_mfr(self, _mfr):
        self.mfr = _mfr

    def update_temp(self, _temp):
        self.temp = _temp

    def update_pressure(self, _pressure):
        self.pressure = _pressure


'''
END UnitNode
'''


class UnitNetwork:
    def __init__(self):
        self._units = {}
        self._connections = {}

    def add_node(self, _name, _id, _type):
        utype = get_utype[_type]
        new_node = UnitNode(_name, _id, utype, _type)

        self._units[_name] = new_node
        return new_node

    def connect(self, _node1, _node2, _port_out, _port_in, _id):
        if not _node1.able_to_connect():
            print(_node1.name + " does not have an available output")
            return
        if not _node2.able_to_receive():
            print(_node2.name + " does not have an available input")
            return

        u_conn = UnitConnection(_id, _node1, _node2)

        u_conn.update_ports(_port_out, _port_in)
        _node1.connect_to(_node2, u_conn)
        _node2.receive_from(_node1, u_conn)

        self._connections[_id] = u_conn
        return u_conn

    def get_node(self, idx):
        return self._units[idx]

    def get_nodes(self):
        return self._units

    def get_connections(self):
        return self._connections

    def print_nodes(self):
        for node in self._units.values():
            print(node.id + " | Q: " + str(node.Q) + " | Type: " + str(node.typeName))

    def print_connections(self):
        for conn in self._connections.values():
            print("Connection: " + conn.label + " | " + conn.output.id + " --> " + conn.input.id +
                  " | Fluid: " + str(conn.fluid) +
                  " | Mfr: " + str(conn.mfr) +
                  " | Temp: " + str(conn.temp) +
                  " | Pressure: " + str(conn.pressure))

