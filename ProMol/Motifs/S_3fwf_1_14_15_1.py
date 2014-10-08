'''
FUNC:S_3fwf_1_14_15_1
PDB:3fwf
EC:1.14.15.1
RESI:asp,thr,phe
LOCI:a-251,252,350;
'''
IDSpec[(('asp','CG'),('rthr','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.33,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','CG'),('rthr','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.42,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','CG'),('rthr','OG1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.08,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD1'),('rthr','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.72,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD1'),('rthr','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.99,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD1'),('rthr','OG1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.57,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD2'),('rthr','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.68,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD2'),('rthr','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.68,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD2'),('rthr','OG1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.53,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','CG'),('rphe','CD1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.59,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','CG'),('rphe','CE1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.23,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','CG'),('rphe','CZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.21,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD1'),('rphe','CD1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.21,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD1'),('rphe','CE1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.75,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD1'),('rphe','CZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.64,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD2'),('rphe','CD1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.49,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD2'),('rphe','CE1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.24,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD2'),('rphe','CZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.26,resSelectionSubs('phe','CZ',subs)))
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
IDSpec[(('thr','CA'),('sasp','CG'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.33,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.72,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.68,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','CG'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.42,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.99,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.68,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','CG'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.08,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.53,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CA'),('rphe','CD1'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.69,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','CA'),('rphe','CE1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.11,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','CA'),('rphe','CZ'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.00,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('thr','CB'),('rphe','CD1'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.52,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','CB'),('rphe','CE1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.02,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','CB'),('rphe','CZ'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.04,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('thr','OG1'),('rphe','CD1'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.74,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','OG1'),('rphe','CE1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.11,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','OG1'),('rphe','CZ'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.06,resSelectionSubs('phe','CZ',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
cmd.delete('thr10')
cmd.delete('thr11')
cmd.delete('thr12')
cmd.delete('thr13')
cmd.delete('thr14')
cmd.delete('thr15')
cmd.delete('thr16')
cmd.delete('thr17')
cmd.delete('thr18')
IDSpec[(('phe','CD1'),('sasp','CG'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.59,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD1'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+16.21,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD2'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.49,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','CG'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+15.23,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD1'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+15.75,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD2'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+15.24,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','CG'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+16.21,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD1'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+16.64,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD2'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+16.26,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','CA'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.69,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','CB'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.52,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','OG1'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.74,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','CA'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.11,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','CB'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.02,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','OG1'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.11,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','CA'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.00,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','CB'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.04,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','OG1'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.06,resSelectionSubs('thr','OG1',subs,selection=True)))
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
IDSpec['S_3fwf_1_14_15_1'] = cmd.select('S_3fwf_1_14_15_1', 'asp|thr|phe')
cmd.delete('asp')
cmd.delete('thr')
cmd.delete('phe')
