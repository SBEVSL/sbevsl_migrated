'''
FUNC:S_2bh2_2_1_1_-
PDB:2bh2
EC:2.1.1.-
RESI:phe,asp,pro
LOCI:a-263,363,364;
'''
IDSpec[(('pro','CA'),('rphe','CD1'))] = cmd.select('pro1', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+11.51,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('pro','CA'),('rphe','CE1'))] = cmd.select('pro2', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+11.21,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('pro','CA'),('rphe','CZ'))] = cmd.select('pro3', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+10.96,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('pro','CB'),('rphe','CD1'))] = cmd.select('pro4', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+12.90,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('pro','CB'),('rphe','CE1'))] = cmd.select('pro5', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+12.60,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('pro','CB'),('rphe','CZ'))] = cmd.select('pro6', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+12.40,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('pro','CD'),('rphe','CD1'))] = cmd.select('pro7', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+13.08,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('pro','CD'),('rphe','CE1'))] = cmd.select('pro8', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+12.55,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('pro','CD'),('rphe','CZ'))] = cmd.select('pro9', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+12.09,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('pro','CA'),('rasp','CG'))] = cmd.select('pro10', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+7.27,resSelectionSubs('asp','CG',subs)))
IDSpec[(('pro','CA'),('rasp','OD1'))] = cmd.select('pro11', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+6.90,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('pro','CA'),('rasp','OD2'))] = cmd.select('pro12', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+8.12,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('pro','CB'),('rasp','CG'))] = cmd.select('pro13', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+8.50,resSelectionSubs('asp','CG',subs)))
IDSpec[(('pro','CB'),('rasp','OD1'))] = cmd.select('pro14', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+8.04,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('pro','CB'),('rasp','OD2'))] = cmd.select('pro15', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+9.46,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('pro','CD'),('rasp','CG'))] = cmd.select('pro16', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+7.01,resSelectionSubs('asp','CG',subs)))
IDSpec[(('pro','CD'),('rasp','OD1'))] = cmd.select('pro17', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+6.48,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('pro','CD'),('rasp','OD2'))] = cmd.select('pro18', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+8.17,resSelectionSubs('asp','OD2',subs)))
IDSpec['pro'] = cmd.select('pro',' br. pro1&br. pro2&br. pro3&br. pro4&br. pro5&br. pro6&br. pro7&br. pro8&br. pro9&br. pro10&br. pro11&br. pro12&br. pro13&br. pro14&br. pro15&br. pro16&br. pro17&br. pro18')
IDSpec['r_pro'] = cmd.count_atoms(resSelectionSubs('pro', subs=subs, selection=True))
cmd.delete('pro1')
cmd.delete('pro2')
cmd.delete('pro3')
cmd.delete('pro4')
cmd.delete('pro5')
cmd.delete('pro6')
cmd.delete('pro7')
cmd.delete('pro8')
cmd.delete('pro9')
cmd.delete('pro10')
cmd.delete('pro11')
cmd.delete('pro12')
cmd.delete('pro13')
cmd.delete('pro14')
cmd.delete('pro15')
cmd.delete('pro16')
cmd.delete('pro17')
cmd.delete('pro18')
IDSpec[(('phe','CD1'),('spro','CA'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.51,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('phe','CD1'),('spro','CB'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.90,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('phe','CD1'),('spro','CD'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+13.08,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('phe','CE1'),('spro','CA'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.21,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('phe','CE1'),('spro','CB'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+12.60,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('phe','CE1'),('spro','CD'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+12.55,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('phe','CZ'),('spro','CA'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.96,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('phe','CZ'),('spro','CB'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.40,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('phe','CZ'),('spro','CD'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.09,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('phe','CD1'),('rasp','CG'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.23,resSelectionSubs('asp','CG',subs)))
IDSpec[(('phe','CD1'),('rasp','OD1'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.31,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('phe','CD1'),('rasp','OD2'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.38,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('phe','CE1'),('rasp','CG'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.49,resSelectionSubs('asp','CG',subs)))
IDSpec[(('phe','CE1'),('rasp','OD1'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.46,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('phe','CE1'),('rasp','OD2'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+8.64,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('phe','CZ'),('rasp','CG'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.52,resSelectionSubs('asp','CG',subs)))
IDSpec[(('phe','CZ'),('rasp','OD1'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.61,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('phe','CZ'),('rasp','OD2'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.55,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('spro','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.27,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('spro','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.50,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('spro','CD'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.01,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('spro','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.90,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('spro','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.04,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('spro','CD'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.48,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('spro','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.12,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('spro','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.46,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('spro','CD'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.17,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('sphe','CD1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.23,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('asp','CG'),('sphe','CE1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.49,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('sphe','CZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.52,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sphe','CD1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.31,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sphe','CE1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.46,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sphe','CZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.61,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sphe','CD1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.38,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sphe','CE1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.64,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sphe','CZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.55,resSelectionSubs('phe','CZ',subs,selection=True)))
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
IDSpec['S_2bh2_2_1_1_-'] = cmd.select('S_2bh2_2_1_1_-', 'pro|phe|asp')
cmd.delete('pro')
cmd.delete('phe')
cmd.delete('asp')
