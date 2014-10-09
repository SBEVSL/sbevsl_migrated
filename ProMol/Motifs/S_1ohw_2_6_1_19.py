'''
FUNC:S_1ohw_2_6_1_19
PDB:1ohw
EC:2.6.1.19
RESI:phe,asp,lys
LOCI:a-189,298,329;
'''
IDSpec[(('asp','CG'),('rphe','CD1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.56,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','CG'),('rphe','CE1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.33,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','CG'),('rphe','CZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.64,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD1'),('rphe','CD1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.56,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD1'),('rphe','CE1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.30,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD1'),('rphe','CZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.58,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD2'),('rphe','CD1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.77,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD2'),('rphe','CE1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.43,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD2'),('rphe','CZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.78,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.06,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.88,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.13,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.14,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.75,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.92,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.03,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.98,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.30,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('phe','CD1'),('sasp','CG'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.56,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD1'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.56,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD2'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.77,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','CG'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.33,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD1'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.30,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD2'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.43,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','CG'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.64,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD1'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.58,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD2'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.78,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CD1'),('rlys','CD'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.70,resSelectionSubs('lys','CD',subs)))
IDSpec[(('phe','CD1'),('rlys','CE'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.45,resSelectionSubs('lys','CE',subs)))
IDSpec[(('phe','CD1'),('rlys','NZ'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.68,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('phe','CE1'),('rlys','CD'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.57,resSelectionSubs('lys','CD',subs)))
IDSpec[(('phe','CE1'),('rlys','CE'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.21,resSelectionSubs('lys','CE',subs)))
IDSpec[(('phe','CE1'),('rlys','NZ'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.34,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('phe','CZ'),('rlys','CD'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.56,resSelectionSubs('lys','CD',subs)))
IDSpec[(('phe','CZ'),('rlys','CE'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.13,resSelectionSubs('lys','CE',subs)))
IDSpec[(('phe','CZ'),('rlys','NZ'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.07,resSelectionSubs('lys','NZ',subs)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9&br. phe10&br. phe11&br. phe12&br. phe13&br. phe14&br. phe15&br. phe16&br. phe17&br. phe18')
IDSpec['r_phe'] = cmd.count_atoms(resSelectionSubs('phe', subs=subs, selection=True))
cmd.delete('phe1')
cmd.delete('phe2')
cmd.delete('phe3')
cmd.delete('phe4')
cmd.delete('phe5')
cmd.delete('phe6')
cmd.delete('phe7')
cmd.delete('phe8')
cmd.delete('phe9')
cmd.delete('phe10')
cmd.delete('phe11')
cmd.delete('phe12')
cmd.delete('phe13')
cmd.delete('phe14')
cmd.delete('phe15')
cmd.delete('phe16')
cmd.delete('phe17')
cmd.delete('phe18')
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.06,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.14,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.03,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.88,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.75,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.98,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.13,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.92,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.30,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('sphe','CD1'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.70,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sphe','CE1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.57,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sphe','CZ'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.56,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sphe','CD1'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.45,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sphe','CE1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.21,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sphe','CZ'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.13,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sphe','CD1'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.68,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sphe','CE1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.34,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sphe','CZ'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.07,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
IDSpec['S_1ohw_2_6_1_19'] = cmd.select('S_1ohw_2_6_1_19', 'asp|phe|lys')
cmd.delete('asp')
cmd.delete('phe')
cmd.delete('lys')