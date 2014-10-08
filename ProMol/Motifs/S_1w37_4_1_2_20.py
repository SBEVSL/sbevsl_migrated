'''
FUNC:S_1w37_4_1_2_20
PDB:1w37
EC:4.1.2.20
RESI:thr,thr,lys
LOCI:a-43,44,155;
'''
IDSpec[(('lys','CD'),('rthr','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.24,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CD'),('rthr','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.71,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CD'),('rthr','OG1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.80,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CE'),('rthr','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.04,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CE'),('rthr','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.44,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CE'),('rthr','OG1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.42,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','NZ'),('rthr','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.78,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','NZ'),('rthr','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.23,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','NZ'),('rthr','OG1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.38,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CD'),('rthr_i','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.94,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('lys','CD'),('rthr_i','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.48,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('lys','CD'),('rthr_i','OG1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.99,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('lys','CE'),('rthr_i','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.05,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('lys','CE'),('rthr_i','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.47,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('lys','CE'),('rthr_i','OG1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.17,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('lys','NZ'),('rthr_i','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.90,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('lys','NZ'),('rthr_i','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.56,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('lys','NZ'),('rthr_i','OG1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.45,resSelectionSubs('thr_i','OG1',subs)))
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
IDSpec[(('thr','CA'),('slys','CD'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.24,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.04,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','NZ'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.78,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CD'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.71,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.44,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','NZ'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.23,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CD'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.80,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.42,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','NZ'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.38,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CA'),('rthr_i','CA'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.76,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','CA'),('rthr_i','CB'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.26,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','CA'),('rthr_i','OG1'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.62,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('thr','CB'),('rthr_i','CA'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.81,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','CB'),('rthr_i','CB'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.07,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','CB'),('rthr_i','OG1'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.34,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('thr','OG1'),('rthr_i','CA'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.74,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','OG1'),('rthr_i','CB'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.58,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','OG1'),('rthr_i','OG1'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.74,resSelectionSubs('thr_i','OG1',subs)))
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
IDSpec[(('thr_i','CA'),('slys','CD'))] = cmd.select('thr_i1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.94,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr_i','CA'),('slys','CE'))] = cmd.select('thr_i2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.05,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr_i','CA'),('slys','NZ'))] = cmd.select('thr_i3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.90,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr_i','CB'),('slys','CD'))] = cmd.select('thr_i4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.48,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr_i','CB'),('slys','CE'))] = cmd.select('thr_i5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.47,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr_i','CB'),('slys','NZ'))] = cmd.select('thr_i6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.56,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('slys','CD'))] = cmd.select('thr_i7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.99,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('slys','CE'))] = cmd.select('thr_i8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.17,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('slys','NZ'))] = cmd.select('thr_i9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.45,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','CA'))] = cmd.select('thr_i10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.76,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','CB'))] = cmd.select('thr_i11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.81,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','OG1'))] = cmd.select('thr_i12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.74,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','CA'))] = cmd.select('thr_i13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.26,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','CB'))] = cmd.select('thr_i14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.07,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','OG1'))] = cmd.select('thr_i15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.58,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','CA'))] = cmd.select('thr_i16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.62,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','CB'))] = cmd.select('thr_i17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.34,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','OG1'))] = cmd.select('thr_i18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.74,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec['thr_i'] = cmd.select('thr_i',' br. thr_i1&br. thr_i2&br. thr_i3&br. thr_i4&br. thr_i5&br. thr_i6&br. thr_i7&br. thr_i8&br. thr_i9&br. thr_i10&br. thr_i11&br. thr_i12&br. thr_i13&br. thr_i14&br. thr_i15&br. thr_i16&br. thr_i17&br. thr_i18')
IDSpec['r_thr_i'] = cmd.count_atoms(resSelectionSubs('thr_i', subs=subs, selection=True))
cmd.delete('thr_i1')
cmd.delete('thr_i2')
cmd.delete('thr_i3')
cmd.delete('thr_i4')
cmd.delete('thr_i5')
cmd.delete('thr_i6')
cmd.delete('thr_i7')
cmd.delete('thr_i8')
cmd.delete('thr_i9')
cmd.delete('thr_i10')
cmd.delete('thr_i11')
cmd.delete('thr_i12')
cmd.delete('thr_i13')
cmd.delete('thr_i14')
cmd.delete('thr_i15')
cmd.delete('thr_i16')
cmd.delete('thr_i17')
cmd.delete('thr_i18')
IDSpec['S_1w37_4_1_2_20'] = cmd.select('S_1w37_4_1_2_20', 'lys|thr|thr_i')
cmd.delete('lys')
cmd.delete('thr')
cmd.delete('thr_i')
