'''
FUNC:S_2gcu_3_1_2_6
PDB:2gcu
EC:3.1.2.6
RESI:asp,ile,cys
LOCI:a-76,157,160;
'''
IDSpec[(('asp','CG'),('rcys','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.17,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','CG'),('rcys','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.30,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','CG'),('rcys','SG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.00,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD1'),('rcys','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.78,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD1'),('rcys','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.83,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD1'),('rcys','SG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.57,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD2'),('rcys','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.57,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD2'),('rcys','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.77,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD2'),('rcys','SG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+17.57,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','CG'),('rile','CD1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.37,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('asp','CG'),('rile','CG1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.50,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('asp','CG'),('rile','CG2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+19.06,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('asp','OD1'),('rile','CD1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.44,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('asp','OD1'),('rile','CG1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.49,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('asp','OD1'),('rile','CG2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.14,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('asp','OD2'),('rile','CD1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.86,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('asp','OD2'),('rile','CG1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+17.10,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('asp','OD2'),('rile','CG2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+18.68,resSelectionSubs('ile','CG2',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18')
IDSpec['r_asp'] = cmd.count_atoms(resSelectionSubs('asp', subs=subs, selection=True))
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
IDSpec[(('cys','CA'),('sasp','CG'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+15.17,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+14.78,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+15.57,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','CG'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+16.30,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+15.83,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+16.77,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','CG'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+17.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+16.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+17.57,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CA'),('rile','CD1'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.57,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys','CA'),('rile','CG1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.39,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys','CA'),('rile','CG2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.96,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('cys','CB'),('rile','CD1'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.69,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys','CB'),('rile','CG1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.42,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys','CB'),('rile','CG2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.94,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('cys','SG'),('rile','CD1'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+15.21,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys','SG'),('rile','CG1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.94,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys','SG'),('rile','CG2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+14.21,resSelectionSubs('ile','CG2',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18')
IDSpec['r_cys'] = cmd.count_atoms(resSelectionSubs('cys', subs=subs, selection=True))
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
IDSpec[(('ile','CD1'),('sasp','CG'))] = cmd.select('ile1', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+17.37,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ile','CD1'),('sasp','OD1'))] = cmd.select('ile2', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+17.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ile','CD1'),('sasp','OD2'))] = cmd.select('ile3', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+16.86,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ile','CG1'),('sasp','CG'))] = cmd.select('ile4', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+17.50,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ile','CG1'),('sasp','OD1'))] = cmd.select('ile5', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+17.49,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ile','CG1'),('sasp','OD2'))] = cmd.select('ile6', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+17.10,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ile','CG2'),('sasp','CG'))] = cmd.select('ile7', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+19.06,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ile','CG2'),('sasp','OD1'))] = cmd.select('ile8', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+19.14,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ile','CG2'),('sasp','OD2'))] = cmd.select('ile9', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+18.68,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys','CA'))] = cmd.select('ile10', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+12.57,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys','CB'))] = cmd.select('ile11', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+13.69,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys','SG'))] = cmd.select('ile12', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+15.21,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys','CA'))] = cmd.select('ile13', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+11.39,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys','CB'))] = cmd.select('ile14', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+12.42,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys','SG'))] = cmd.select('ile15', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+13.94,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys','CA'))] = cmd.select('ile16', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+11.96,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys','CB'))] = cmd.select('ile17', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+12.94,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys','SG'))] = cmd.select('ile18', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+14.21,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec['ile'] = cmd.select('ile',' br. ile1&br. ile2&br. ile3&br. ile4&br. ile5&br. ile6&br. ile7&br. ile8&br. ile9&br. ile10&br. ile11&br. ile12&br. ile13&br. ile14&br. ile15&br. ile16&br. ile17&br. ile18')
IDSpec['r_ile'] = cmd.count_atoms(resSelectionSubs('ile', subs=subs, selection=True))
cmd.delete('ile1')
cmd.delete('ile2')
cmd.delete('ile3')
cmd.delete('ile4')
cmd.delete('ile5')
cmd.delete('ile6')
cmd.delete('ile7')
cmd.delete('ile8')
cmd.delete('ile9')
cmd.delete('ile10')
cmd.delete('ile11')
cmd.delete('ile12')
cmd.delete('ile13')
cmd.delete('ile14')
cmd.delete('ile15')
cmd.delete('ile16')
cmd.delete('ile17')
cmd.delete('ile18')
IDSpec['S_2gcu_3_1_2_6'] = cmd.select('S_2gcu_3_1_2_6', 'asp|cys|ile')
cmd.delete('asp')
cmd.delete('cys')
cmd.delete('ile')