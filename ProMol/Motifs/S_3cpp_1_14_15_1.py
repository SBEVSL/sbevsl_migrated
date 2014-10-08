'''
FUNC:S_3cpp_1_14_15_1
PDB:3cpp
EC:1.14.15.1
RESI:asp,thr,phe,cys
LOCI:a-251,252,350,357;
'''
IDSpec[(('asp','CG'),('rthr','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.34,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','CG'),('rthr','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.32,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','CG'),('rthr','OG1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.90,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD1'),('rthr','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.64,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD1'),('rthr','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.49,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD1'),('rthr','OG1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.28,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD2'),('rthr','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.70,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD2'),('rthr','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.88,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD2'),('rthr','OG1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.40,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','CG'),('rphe','CD1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.40,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','CG'),('rphe','CE1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.23,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','CG'),('rphe','CZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.24,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD1'),('rphe','CD1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.28,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD1'),('rphe','CE1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.21,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD1'),('rphe','CZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.23,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD2'),('rphe','CD1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.03,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD2'),('rphe','CE1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.74,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD2'),('rphe','CZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.68,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','CG'),('rcys','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.10,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','CG'),('rcys','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.24,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','CG'),('rcys','SG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.07,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD1'),('rcys','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.92,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD1'),('rcys','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.08,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD1'),('rcys','SG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.03,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD2'),('rcys','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+18.01,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD2'),('rcys','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+17.08,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD2'),('rcys','SG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.88,resSelectionSubs('cys','SG',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27')
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
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
IDSpec[(('thr','CA'),('sasp','CG'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.34,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.64,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.70,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','CG'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.32,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.49,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.88,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','CG'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.90,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.28,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.40,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CA'),('rphe','CD1'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.51,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','CA'),('rphe','CE1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.10,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','CA'),('rphe','CZ'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.03,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('thr','CB'),('rphe','CD1'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.28,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','CB'),('rphe','CE1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.00,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','CB'),('rphe','CZ'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.07,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('thr','OG1'),('rphe','CD1'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.44,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','OG1'),('rphe','CE1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.05,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','OG1'),('rphe','CZ'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.12,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('thr','CA'),('rcys','CA'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.20,resSelectionSubs('cys','CA',subs)))
IDSpec[(('thr','CA'),('rcys','CB'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.04,resSelectionSubs('cys','CB',subs)))
IDSpec[(('thr','CA'),('rcys','SG'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.82,resSelectionSubs('cys','SG',subs)))
IDSpec[(('thr','CB'),('rcys','CA'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.66,resSelectionSubs('cys','CA',subs)))
IDSpec[(('thr','CB'),('rcys','CB'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.53,resSelectionSubs('cys','CB',subs)))
IDSpec[(('thr','CB'),('rcys','SG'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.30,resSelectionSubs('cys','SG',subs)))
IDSpec[(('thr','OG1'),('rcys','CA'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+11.53,resSelectionSubs('cys','CA',subs)))
IDSpec[(('thr','OG1'),('rcys','CB'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.46,resSelectionSubs('cys','CB',subs)))
IDSpec[(('thr','OG1'),('rcys','SG'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.01,resSelectionSubs('cys','SG',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18&br. thr19&br. thr20&br. thr21&br. thr22&br. thr23&br. thr24&br. thr25&br. thr26&br. thr27')
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
cmd.delete('thr19')
cmd.delete('thr20')
cmd.delete('thr21')
cmd.delete('thr22')
cmd.delete('thr23')
cmd.delete('thr24')
cmd.delete('thr25')
cmd.delete('thr26')
cmd.delete('thr27')
IDSpec[(('phe','CD1'),('sasp','CG'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.40,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD1'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.28,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD2'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+16.03,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','CG'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+15.23,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD1'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+15.21,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD2'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+15.74,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','CG'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+16.24,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD1'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+16.23,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD2'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+16.68,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','CA'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.51,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','CB'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.28,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','OG1'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.44,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','CA'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.10,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','CB'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.00,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','OG1'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.05,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','CA'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.03,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','CB'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.07,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','OG1'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.12,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('phe','CD1'),('rcys','CA'))] = cmd.select('phe19', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.33,resSelectionSubs('cys','CA',subs)))
IDSpec[(('phe','CD1'),('rcys','CB'))] = cmd.select('phe20', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+5.79,resSelectionSubs('cys','CB',subs)))
IDSpec[(('phe','CD1'),('rcys','SG'))] = cmd.select('phe21', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+5.99,resSelectionSubs('cys','SG',subs)))
IDSpec[(('phe','CE1'),('rcys','CA'))] = cmd.select('phe22', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+8.41,resSelectionSubs('cys','CA',subs)))
IDSpec[(('phe','CE1'),('rcys','CB'))] = cmd.select('phe23', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.87,resSelectionSubs('cys','CB',subs)))
IDSpec[(('phe','CE1'),('rcys','SG'))] = cmd.select('phe24', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.68,resSelectionSubs('cys','SG',subs)))
IDSpec[(('phe','CZ'),('rcys','CA'))] = cmd.select('phe25', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.41,resSelectionSubs('cys','CA',subs)))
IDSpec[(('phe','CZ'),('rcys','CB'))] = cmd.select('phe26', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.93,resSelectionSubs('cys','CB',subs)))
IDSpec[(('phe','CZ'),('rcys','SG'))] = cmd.select('phe27', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.90,resSelectionSubs('cys','SG',subs)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9&br. phe10&br. phe11&br. phe12&br. phe13&br. phe14&br. phe15&br. phe16&br. phe17&br. phe18&br. phe19&br. phe20&br. phe21&br. phe22&br. phe23&br. phe24&br. phe25&br. phe26&br. phe27')
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
cmd.delete('phe19')
cmd.delete('phe20')
cmd.delete('phe21')
cmd.delete('phe22')
cmd.delete('phe23')
cmd.delete('phe24')
cmd.delete('phe25')
cmd.delete('phe26')
cmd.delete('phe27')
IDSpec[(('cys','CA'),('sasp','CG'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+17.10,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+16.92,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+18.01,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','CG'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+16.24,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+16.08,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+17.08,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','CG'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+15.07,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+15.03,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+15.88,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CA'),('sthr','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.20,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sthr','CB'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.66,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('cys','CA'),('sthr','OG1'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.53,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('cys','CB'),('sthr','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.04,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sthr','CB'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.53,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('cys','CB'),('sthr','OG1'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.46,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('cys','SG'),('sthr','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.82,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sthr','CB'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.30,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('cys','SG'),('sthr','OG1'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.01,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('cys','CA'),('sphe','CD1'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.33,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sphe','CE1'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.41,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('cys','CA'),('sphe','CZ'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.41,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('cys','CB'),('sphe','CD1'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.79,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sphe','CE1'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.87,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('cys','CB'),('sphe','CZ'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.93,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('cys','SG'),('sphe','CD1'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.99,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sphe','CE1'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.68,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('cys','SG'),('sphe','CZ'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.90,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27')
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
cmd.delete('cys19')
cmd.delete('cys20')
cmd.delete('cys21')
cmd.delete('cys22')
cmd.delete('cys23')
cmd.delete('cys24')
cmd.delete('cys25')
cmd.delete('cys26')
cmd.delete('cys27')
IDSpec['S_3cpp_1_14_15_1'] = cmd.select('S_3cpp_1_14_15_1', 'asp|thr|phe|cys')
cmd.delete('asp')
cmd.delete('thr')
cmd.delete('phe')
cmd.delete('cys')
