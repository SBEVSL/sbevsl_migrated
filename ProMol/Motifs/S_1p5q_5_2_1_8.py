'''
FUNC:S_1p5q_5_2_1_8
PDB:1p5q
EC:5.2.1.8
RESI:asp,leu,phe
LOCI:a-184,198,227;
'''
IDSpec[(('leu','CD1'),('rasp','CG'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+13.03,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CD1'),('rasp','OD1'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+12.35,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CD1'),('rasp','OD2'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+12.65,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('leu','CD2'),('rasp','CG'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+12.59,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CD2'),('rasp','OD1'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+11.88,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CD2'),('rasp','OD2'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+12.27,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('leu','CG'),('rasp','CG'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+11.93,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CG'),('rasp','OD1'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+11.27,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CG'),('rasp','OD2'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+11.55,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('leu','CD1'),('rphe','CD1'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+15.72,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('leu','CD1'),('rphe','CE1'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+14.71,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('leu','CD1'),('rphe','CZ'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+13.37,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('leu','CD2'),('rphe','CD1'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+15.72,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('leu','CD2'),('rphe','CE1'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+14.66,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('leu','CD2'),('rphe','CZ'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+13.34,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('leu','CG'),('rphe','CD1'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+15.15,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('leu','CG'),('rphe','CE1'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+14.07,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('leu','CG'),('rphe','CZ'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+12.76,resSelectionSubs('phe','CZ',subs)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9&br. leu10&br. leu11&br. leu12&br. leu13&br. leu14&br. leu15&br. leu16&br. leu17&br. leu18')
IDSpec['r_leu'] = cmd.count_atoms(resSelectionSubs('leu', subs=subs, selection=True))
cmd.delete('leu1')
cmd.delete('leu2')
cmd.delete('leu3')
cmd.delete('leu4')
cmd.delete('leu5')
cmd.delete('leu6')
cmd.delete('leu7')
cmd.delete('leu8')
cmd.delete('leu9')
cmd.delete('leu10')
cmd.delete('leu11')
cmd.delete('leu12')
cmd.delete('leu13')
cmd.delete('leu14')
cmd.delete('leu15')
cmd.delete('leu16')
cmd.delete('leu17')
cmd.delete('leu18')
IDSpec[(('asp','CG'),('sleu','CD1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.03,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','CG'),('sleu','CD2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.59,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','CG'),('sleu','CG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.93,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CD1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.35,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CD2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.88,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.27,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CD1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.65,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CD2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.27,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.55,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('asp','CG'),('rphe','CD1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.12,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','CG'),('rphe','CE1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.77,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','CG'),('rphe','CZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.54,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD1'),('rphe','CD1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.24,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD1'),('rphe','CE1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.86,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD1'),('rphe','CZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.47,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD2'),('rphe','CD1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.23,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD2'),('rphe','CE1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.86,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD2'),('rphe','CZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.54,resSelectionSubs('phe','CZ',subs)))
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
IDSpec[(('phe','CD1'),('sleu','CD1'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.72,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('phe','CD1'),('sleu','CD2'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.72,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('phe','CD1'),('sleu','CG'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.15,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sleu','CD1'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+14.71,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sleu','CD2'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+14.66,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('phe','CE1'),('sleu','CG'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+14.07,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sleu','CD1'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+13.37,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sleu','CD2'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+13.34,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('phe','CZ'),('sleu','CG'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.76,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','CG'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.12,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD1'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.24,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD2'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.23,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','CG'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+8.77,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD1'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.86,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD2'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.86,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','CG'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.54,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD1'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.47,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD2'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.54,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_1p5q_5_2_1_8'] = cmd.select('S_1p5q_5_2_1_8', 'leu|asp|phe')
cmd.delete('leu')
cmd.delete('asp')
cmd.delete('phe')
