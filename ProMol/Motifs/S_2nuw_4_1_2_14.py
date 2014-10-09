'''
FUNC:S_2nuw_4_1_2_14
PDB:2nuw
EC:4.1.2.14
RESI:thr,thr,lys
LOCI:a-42,43,153;
'''
IDSpec[(('thr','CA'),('rthr','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.81,resSelectionSubs('thr','CA',subs)))
IDSpec[(('thr','CA'),('rthr','CB'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.86,resSelectionSubs('thr','CB',subs)))
IDSpec[(('thr','CA'),('rthr','OG1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.83,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('thr','CB'),('rthr','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.46,resSelectionSubs('thr','CA',subs)))
IDSpec[(('thr','CB'),('rthr','CB'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.30,resSelectionSubs('thr','CB',subs)))
IDSpec[(('thr','CB'),('rthr','OG1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.86,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('thr','OG1'),('rthr','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.79,resSelectionSubs('thr','CA',subs)))
IDSpec[(('thr','OG1'),('rthr','CB'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.56,resSelectionSubs('thr','CB',subs)))
IDSpec[(('thr','OG1'),('rthr','OG1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.04,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('thr','CA'),('rlys','CD'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.51,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','CA'),('rlys','CE'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.69,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','CA'),('rlys','NZ'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.07,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','CB'),('rlys','CD'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.55,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','CB'),('rlys','CE'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.85,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','CB'),('rlys','NZ'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.16,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','OG1'),('rlys','CD'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.11,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','OG1'),('rlys','CE'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.30,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','OG1'),('rlys','NZ'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+11.46,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('thr_i','CA'),('sthr','CA'))] = cmd.select('thr_i1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.81,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','CB'))] = cmd.select('thr_i2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.46,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','OG1'))] = cmd.select('thr_i3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.79,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','CA'))] = cmd.select('thr_i4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.86,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','CB'))] = cmd.select('thr_i5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.30,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','OG1'))] = cmd.select('thr_i6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.56,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','CA'))] = cmd.select('thr_i7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.83,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','CB'))] = cmd.select('thr_i8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.86,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','OG1'))] = cmd.select('thr_i9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.04,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','CA'),('rlys','CD'))] = cmd.select('thr_i10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.55,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr_i','CA'),('rlys','CE'))] = cmd.select('thr_i11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+14.05,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr_i','CA'),('rlys','NZ'))] = cmd.select('thr_i12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr_i','CB'),('rlys','CD'))] = cmd.select('thr_i13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.95,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr_i','CB'),('rlys','CE'))] = cmd.select('thr_i14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+13.61,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr_i','CB'),('rlys','NZ'))] = cmd.select('thr_i15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+13.60,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr_i','OG1'),('rlys','CD'))] = cmd.select('thr_i16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.43,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr_i','OG1'),('rlys','CE'))] = cmd.select('thr_i17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.20,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr_i','OG1'),('rlys','NZ'))] = cmd.select('thr_i18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.15,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('sthr','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.51,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.55,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','OG1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.11,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.69,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.85,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','OG1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.30,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.07,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.16,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','OG1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.46,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr_i','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.55,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr_i','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.95,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr_i','OG1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.43,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr_i','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+14.05,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr_i','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.61,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr_i','OG1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.20,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr_i','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.87,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr_i','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.60,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr_i','OG1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.15,resSelectionSubs('thr_i','OG1',subs,selection=True)))
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
IDSpec['S_2nuw_4_1_2_14'] = cmd.select('S_2nuw_4_1_2_14', 'thr|thr_i|lys')
cmd.delete('thr')
cmd.delete('thr_i')
cmd.delete('lys')