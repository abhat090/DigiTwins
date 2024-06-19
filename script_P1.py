# Unit Nodes: 
source = components.Source('Source')
E3_return = components.Merge('E3 Return')
E2_return = components.Merge('E2 Return')
E1_return = components.Merge('E1 Return')
Supplemental_supply = components.Splitter('Supplemental Converter Supply')
Suppl_Cond_Cooler = components.SimpleHeatExchanger('Supplemental Condensate Cooler')
Cond_Splitter = components.Splitter('Supplemental Condensate Cooler Splitter')
Cond_Merger = components.Merge('Supplemental Condensate Return Merger')
Supplemental_Converter = components.SimpleHeatExchanger('Supplemental Steam Converter')
Supplemental_return = components.Merge('Supplemental Converter Return')
Admin_total_supply = components.Splitter('Admin Building Supply')
Admin_HEX = components.SimpleHeatExchanger('Admin Building HEX')
Admin_total_return = components.Merge('Admin Building Return')
Control_Center_supply = components.Splitter('Control Center supply')
Control_Center_HEX = components.SimpleHeatExchanger('Control Center HEX')
Control_Center_return = components.Merge('Control Center return')
Digester_5_6_supply = components.Splitter('Digester 5 6 supply')
Digester_5_6_HEX = components.SimpleHeatExchanger('Digester 5 6 HEX')
Digester_5_6_return = components.Merge('Digester 5 6 return')
Boiler_A_supply = components.Splitter('Boiler A supply')
Boiler_A_HEX = components.SimpleHeatExchanger('Boiler A HEX')
Boiler_A_return = components.Merge('Boiler A return')
Boiler_B_supply = components.Splitter('Boiler B supply')
Boiler_B_HEX = components.SimpleHeatExchanger('Boiler B HEX')
Boiler_B_return = components.Merge('Boiler B return')
Digester_7_to_10_supply = components.Splitter('Digester 7 to 10 supply')
Digester_7_to_10_HEX = components.SimpleHeatExchanger('Digester 7 to 10 HEX')
Digester_7_to_10_return = components.Merge('Digester 7 to 10 return')
Digester_15_16_supply = components.Splitter('Digester 15 16 supply')
Digester_15_16_HEX = components.SimpleHeatExchanger('Digester 15_ 16 HEX')
Digester_11_to_14_supply = components.Splitter('Digester 11 to 14 supply')
Digester_11_to_14_HEX = components.SimpleHeatExchanger('Digester 11 to 14 HEX')
Digester_11_to_14_return = components.Merge('Digester 11 to 14 return')
Digester_15_16_return = components.Merge('Digester 15 16 return')
Waste_HEX1_supply = components.Splitter('Waste HEX1 supply')
Waste_HEX1 = components.SimpleHeatExchanger('Waste HEX1')
Waste_HEX2_return = components.Merge('Waste HEX2 return')
Waste_HEX2 = components.SimpleHeatExchanger('Waste HEX2')
Waste_HEX2_supply = components.Splitter('Waste HEX2 supply')
Waste_HEX1_return = components.Merge('Waste HEX1 return')
E1_supply = components.Splitter('E1 supply')
JW_HEX_E1 = components.SimpleHeatExchanger('JW HEX E1')
E2_supply = components.Splitter('E2 supply')
JW_HEX_E2 = components.SimpleHeatExchanger('JW HEX E2')
E3_supply = components.Splitter('E3 supply')
JW_HEX_E3 = components.SimpleHeatExchanger('JW HEX E3')
sink = components.Sink('Sink')
# End Nodes 

# Streams: 
c1 = connections.Connection(source, 'out1', E3_return, 'in1', label='1')
c1a = connections.Connection(JW_HEX_E3, 'out1', E3_return, 'in2', label='1a')
c2a = connections.Connection(JW_HEX_E2, 'out1', E2_return, 'in2', label='2a')
c2 = connections.Connection(E3_return, 'out1', E2_return, 'in1', label='2')
c3 = connections.Connection(E2_return, 'out1', E1_return, 'in1', label='3')
c3a = connections.Connection(JW_HEX_E1, 'out1', E1_return, 'in2', label='3a')
c4 = connections.Connection(E1_return, 'out1', Supplemental_supply, 'in1', label='4')
c6 = connections.Connection(Supplemental_supply, 'out1', Supplemental_return, 'in1', label='6')
c6a = connections.Connection(Supplemental_supply, 'out2', Cond_Splitter, 'in1', label='6a')
c6b = connections.Connection(Cond_Splitter, 'out1', Cond_Merger, 'in1', label='6b')
c6c = connections.Connection(Cond_Splitter, 'out2', Suppl_Cond_Cooler, 'in1', label='6c')
c6d = connections.Connection(Suppl_Cond_Cooler, 'out1', Cond_Merger, 'in2', label='6d')
c6e = connections.Connection(Cond_Merger, 'out1', Supplemental_Converter, 'in1', label='6e')
c6f = connections.Connection(Supplemental_Converter, 'out1', Supplemental_return, 'in2', label='6f')
c7 = connections.Connection(Supplemental_return, 'out1', Admin_total_supply, 'in1', label='7')
c7a = connections.Connection(Admin_total_supply, 'out2', Admin_HEX, 'in1', label='7a')
c8 = connections.Connection(Admin_total_supply, 'out1', Admin_total_return, 'in1', label='8')
c8a = connections.Connection(Admin_HEX, 'out1', Admin_total_return, 'in2', label='8a')
c9 = connections.Connection(Admin_total_return, 'out1', Control_Center_supply, 'in1', label='9')
c9a = connections.Connection(Control_Center_supply, 'out2', Control_Center_HEX, 'in1', label='9a')
c10 = connections.Connection(Control_Center_supply, 'out1', Control_Center_return, 'in1', label='10')
c10a = connections.Connection(Control_Center_HEX, 'out1', Control_Center_return, 'in2', label='10a')
c11 = connections.Connection(Control_Center_return, 'out1', Digester_5_6_supply, 'in1', label='11')
c11a = connections.Connection(Digester_5_6_supply, 'out2', Digester_5_6_HEX, 'in1', label='11a')
c12 = connections.Connection(Digester_5_6_supply, 'out1', Digester_5_6_return, 'in1', label='12')
c12a = connections.Connection(Digester_5_6_HEX, 'out1', Digester_5_6_return, 'in2', label='12a')
c13 = connections.Connection(Digester_5_6_return, 'out1', Boiler_A_supply, 'in1', label='13')
c13a = connections.Connection(Boiler_A_supply, 'out2', Boiler_A_HEX, 'in1', label='13a')
c14 = connections.Connection(Boiler_A_supply, 'out1', Boiler_A_return, 'in1', label='14')
c14a = connections.Connection(Boiler_A_HEX, 'out1', Boiler_A_return, 'in2', label='14a')
c15 = connections.Connection(Boiler_A_return, 'out1', Boiler_B_supply, 'in1', label='15')
c15a = connections.Connection(Boiler_B_supply, 'out2', Boiler_B_HEX, 'in1', label='15a')
c16 = connections.Connection(Boiler_B_supply, 'out1', Boiler_B_return, 'in1', label='16')
c16a = connections.Connection(Boiler_B_HEX, 'out1', Boiler_B_return, 'in2', label='16a')
c17 = connections.Connection(Boiler_B_return, 'out1', Digester_7_to_10_supply, 'in1', label='17')
c17a = connections.Connection(Digester_7_to_10_supply, 'out2', Digester_7_to_10_HEX, 'in1', label='17a')
c18 = connections.Connection(Digester_7_to_10_supply, 'out1', Digester_7_to_10_return, 'in1', label='18')
c18a = connections.Connection(Digester_7_to_10_HEX, 'out1', Digester_7_to_10_return, 'in2', label='18a')
c19 = connections.Connection(Digester_7_to_10_return, 'out1', Digester_15_16_supply, 'in1', label='19')
c19a = connections.Connection(Digester_15_16_supply, 'out2', Digester_15_16_HEX, 'in1', label='19a')
c20 = connections.Connection(Digester_15_16_supply, 'out1', Digester_11_to_14_supply, 'in1', label='20')
c20a = connections.Connection(Digester_11_to_14_supply, 'out2', Digester_11_to_14_HEX, 'in1', label='20a')
c21 = connections.Connection(Digester_11_to_14_supply, 'out1', Digester_11_to_14_return, 'in1', label='21')
c21a = connections.Connection(Digester_11_to_14_HEX, 'out1', Digester_11_to_14_return, 'in2', label='21a')
c22 = connections.Connection(Digester_11_to_14_return, 'out1', Digester_15_16_return, 'in1', label='22')
c23 = connections.Connection(Digester_15_16_HEX, 'out1', Digester_15_16_return, 'in2', label='23')
c24 = connections.Connection(Digester_15_16_return, 'out1', Waste_HEX1_supply, 'in1', label='24')
c24a = connections.Connection(Waste_HEX1_supply, 'out2', Waste_HEX1, 'in1', label='24a')
c25 = connections.Connection(Waste_HEX1_supply, 'out1', Waste_HEX2_return, 'in1', label='25')
c26 = connections.Connection(Waste_HEX2_return, 'out1', Waste_HEX2_supply, 'in1', label='26')
c27 = connections.Connection(Waste_HEX2_supply, 'out1', Waste_HEX1_return, 'in1', label='27')
c27a = connections.Connection(Waste_HEX1, 'out1', Waste_HEX1_return, 'in2', label='27a')
c26a = connections.Connection(Waste_HEX2_supply, 'out2', Waste_HEX2, 'in1', label='26a')
c25a = connections.Connection(Waste_HEX2, 'out1', Waste_HEX2_return, 'in2', label='25a')
c28 = connections.Connection(Waste_HEX1_return, 'out1', E1_supply, 'in1', label='28')
c28a = connections.Connection(E1_supply, 'out2', JW_HEX_E1, 'in1', label='28a')
c29 = connections.Connection(E1_supply, 'out1', E2_supply, 'in1', label='29')
c29a = connections.Connection(E2_supply, 'out2', JW_HEX_E2, 'in1', label='29a')
c30 = connections.Connection(E2_supply, 'out1', E3_supply, 'in1', label='30')
c30a = connections.Connection(E3_supply, 'out2', JW_HEX_E3, 'in1', label='30a')
c31 = connections.Connection(E3_supply, 'out1', sink, 'in1', label='31')
# End Streams 

# Plant Add Connections 
self.plant.add_conns(c1, c1a, c2a, c2, c3, c3a, c4, c6, c6a, c6b, c6c, c6d, c6e, c6f, c7, c7a, c8, c8a, c9, c9a, c10, c10a, c11, c11a, c12, c12a, c13, c13a, c14, c14a, c15, c15a, c16, c16a, c17, c17a, c18, c18a, c19, c19a, c20, c20a, c21, c21a, c22, c23, c24, c24a, c25, c26, c27, c27a, c26a, c25a, c28, c28a, c29, c29a, c30, c30a, c31)
# End Plant Connections 

# Node Boundary ConditionsSuppl_Cond_Cooler.set_attr(Q=meta['Suppl_Cond_Cooler.Q'])
Supplemental_Converter.set_attr(Q=meta['Supplemental_Converter.Q'])
Admin_HEX.set_attr(Q=meta['Admin_HEX.Q'])
Control_Center_HEX.set_attr(Q=meta['Control_Center_HEX.Q'])
Digester_5_6_HEX.set_attr(Q=meta['Digester_5_6_HEX.Q'])
Boiler_A_HEX.set_attr(Q=meta['Boiler_A_HEX.Q'])
Boiler_B_HEX.set_attr(Q=meta['Boiler_B_HEX.Q'])
Digester_7_to_10_HEX.set_attr(Q=meta['Digester_7_to_10_HEX.Q'])
Digester_15_16_HEX.set_attr(Q=meta['Digester_15_16_HEX.Q'])
Digester_11_to_14_HEX.set_attr(Q=meta['Digester_11_to_14_HEX.Q'])
Waste_HEX1.set_attr(Q=meta['Waste_HEX1.Q'])
Waste_HEX2.set_attr(Q=meta['Waste_HEX2.Q'])
JW_HEX_E1.set_attr(Q=meta['JW_HEX_E1.Q'])
JW_HEX_E2.set_attr(Q=meta['JW_HEX_E2.Q'])
JW_HEX_E3.set_attr(Q=meta['JW_HEX_E3.Q'])

# Connection Boundary Conditions
c1.set_attr(fluid={meta['working_fluid']: 1})
c1.set_attr(m=meta['c1.mass_flow_rate'])
c1.set_attr(T=meta['c1.temperature'])
c1.set_attr(p=meta['c1.pressure'])
c1a.set_attr(T=meta['c1a.temperature'])
c2a.set_attr(T=meta['c2a.temperature'])
c3a.set_attr(T=meta['c3a.temperature'])
c6c.set_attr(m=meta['c6c.mass_flow_rate'])
c6f.set_attr(T=meta['c6f.temperature'])
c7a.set_attr(m=meta['c7a.mass_flow_rate'])
c9a.set_attr(m=meta['c9a.mass_flow_rate'])
c11a.set_attr(m=meta['c11a.mass_flow_rate'])
c13a.set_attr(m=meta['c13a.mass_flow_rate'])
c15a.set_attr(m=meta['c15a.mass_flow_rate'])
c17a.set_attr(m=meta['c17a.mass_flow_rate'])
c19a.set_attr(m=meta['c19a.mass_flow_rate'])
c20a.set_attr(m=meta['c20a.mass_flow_rate'])
c24a.set_attr(m=meta['c24a.mass_flow_rate'])
c26a.set_attr(m=meta['c26a.mass_flow_rate'])

# Node terms for metadata dictionary
# Unit Nodes
'Suppl_Cond_Cooler.Q': 80000.0,
'Supplemental_Converter.Q': 1020000.0,
'Admin_HEX.Q': -150000.0,
'Control_Center_HEX.Q': -130000.0,
'Digester_5_6_HEX.Q': -160000.0,
'Boiler_A_HEX.Q': -250000.0,
'Boiler_B_HEX.Q': -250000.0,
'Digester_7_to_10_HEX.Q': -140000.0,
'Digester_15_16_HEX.Q': -120000.0,
'Digester_11_to_14_HEX.Q': -150000.0,
'Waste_HEX1.Q': -175000.0,
'Waste_HEX2.Q': -175000.0,
'JW_HEX_E1.Q': 200000.0,
'JW_HEX_E2.Q': 200000.0,
'JW_HEX_E3.Q': 200000.0,

# Connections
'working_fluid': 'water',
'c1.mass_flow_rate': 50.0,
'c1.temperature': 55.0,
'c1.pressure': 101.325,
'c1a.temperature': 80.0,
'c2a.temperature': 80.0,
'c3a.temperature': 80.0,
'c6c.mass_flow_rate': 25.0,
'c6f.temperature': 92.0,
'c7a.mass_flow_rate': 20.0,
'c9a.mass_flow_rate': 25.0,
'c11a.mass_flow_rate': 22.0,
'c13a.mass_flow_rate': 25.0,
'c15a.mass_flow_rate': 20.0,
'c17a.mass_flow_rate': 25.0,
'c19a.mass_flow_rate': 10.0,
'c20a.mass_flow_rate': 20.0,
'c24a.mass_flow_rate': 25.0,
'c26a.mass_flow_rate': 25.0,
