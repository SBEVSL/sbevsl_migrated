'''
FUNC:S_2cda_1_1_1_47
PDB:2cda
EC:1.1.1.47
RESI:gly,thr
LOCI:a-40,41;
'''
IDSpec[(('gly','CA'),('rthr','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.77,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','CA'),('rthr','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.87,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','CA'),('rthr','OG1'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.99,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','N'),('rthr','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.20,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','N'),('rthr','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.99,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','N'),('rthr','OG1'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.15,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','O'),('rthr','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.75,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','O'),('rthr','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.23,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','O'),('rthr','OG1'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.62,resSelectionSubs('thr','OG1',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9')
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
IDSpec[(('thr','CA'),('sgly','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.77,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','N'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.20,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','O'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+4.75,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.87,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','N'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.99,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','O'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.23,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.99,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','N'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.15,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','O'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.62,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9')
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
IDSpec['S_2cda_1_1_1_47'] = cmd.select('S_2cda_1_1_1_47', 'gly|thr')
cmd.delete('gly')
cmd.delete('thr')
