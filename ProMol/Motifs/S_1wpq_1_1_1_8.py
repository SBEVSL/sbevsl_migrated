'''
FUNC:S_1wpq_1_1_1_8
PDB:1wpq
EC:1.1.1.8
RESI:gly,lys,thr
LOCI:a-201,204,264;
'''
IDSpec[(('lys','CD'),('rthr','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.59,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CD'),('rthr','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.07,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CD'),('rthr','OG1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.66,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CE'),('rthr','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.85,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CE'),('rthr','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.41,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CE'),('rthr','OG1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.63,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','NZ'),('rthr','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.88,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','NZ'),('rthr','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.55,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','NZ'),('rthr','OG1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.77,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CD'),('rgly','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.85,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CD'),('rgly','N'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.70,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CD'),('rgly','O'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.71,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CE'),('rgly','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.43,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CE'),('rgly','N'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.56,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CE'),('rgly','O'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.34,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','NZ'),('rgly','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.79,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','NZ'),('rgly','N'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.98,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','NZ'),('rgly','O'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.60,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('thr','CA'),('slys','CD'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.59,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.85,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','NZ'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.88,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CD'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.41,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','NZ'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.55,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CD'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.66,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.63,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','NZ'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+4.77,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CA'),('rgly','CA'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.06,resSelectionSubs('gly','CA',subs)))
IDSpec[(('thr','CA'),('rgly','N'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.95,resSelectionSubs('gly','N',subs)))
IDSpec[(('thr','CA'),('rgly','O'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.09,resSelectionSubs('gly','O',subs)))
IDSpec[(('thr','CB'),('rgly','CA'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.64,resSelectionSubs('gly','CA',subs)))
IDSpec[(('thr','CB'),('rgly','N'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.54,resSelectionSubs('gly','N',subs)))
IDSpec[(('thr','CB'),('rgly','O'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.58,resSelectionSubs('gly','O',subs)))
IDSpec[(('thr','OG1'),('rgly','CA'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.74,resSelectionSubs('gly','CA',subs)))
IDSpec[(('thr','OG1'),('rgly','N'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.70,resSelectionSubs('gly','N',subs)))
IDSpec[(('thr','OG1'),('rgly','O'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.95,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('gly','CA'),('slys','CD'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.85,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','CE'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.43,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','NZ'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.79,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CD'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.70,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CE'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.56,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','N'),('slys','NZ'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.98,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CD'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.71,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CE'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.34,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','O'),('slys','NZ'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.60,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','CA'),('sthr','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.06,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('sthr','CB'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.64,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('sthr','OG1'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.74,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('gly','N'),('sthr','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.95,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('gly','N'),('sthr','CB'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.54,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('gly','N'),('sthr','OG1'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.70,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('gly','O'),('sthr','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.09,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('gly','O'),('sthr','CB'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.58,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('gly','O'),('sthr','OG1'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.95,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
IDSpec['S_1wpq_1_1_1_8'] = cmd.select('S_1wpq_1_1_1_8', 'lys|thr|gly')
cmd.delete('lys')
cmd.delete('thr')
cmd.delete('gly')
