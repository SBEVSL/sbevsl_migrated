'''
FUNC:S_2jlc_2_2_1_9
PDB:2jlc
EC:2.2.1.9
RESI:gly,ser
LOCI:a-414,416;
'''
IDSpec[(('ser','CA'),('rgly','CA'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.45,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','CA'),('rgly','N'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.90,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','CA'),('rgly','O'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.00,resSelectionSubs('gly','O',subs)))
IDSpec[(('ser','CB'),('rgly','CA'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.99,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','CB'),('rgly','N'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.47,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','CB'),('rgly','O'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.09,resSelectionSubs('gly','O',subs)))
IDSpec[(('ser','OG'),('rgly','CA'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.28,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','OG'),('rgly','N'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.69,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','OG'),('rgly','O'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.45,resSelectionSubs('gly','O',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
IDSpec[(('gly','CA'),('sser','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.45,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('sser','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.99,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('sser','OG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.28,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gly','N'),('sser','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.90,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly','N'),('sser','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.47,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly','N'),('sser','OG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.69,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gly','O'),('sser','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.00,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly','O'),('sser','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.09,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly','O'),('sser','OG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.45,resSelectionSubs('ser','OG',subs,selection=True)))
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
IDSpec['S_2jlc_2_2_1_9'] = cmd.select('S_2jlc_2_2_1_9', 'ser|gly')
cmd.delete('ser')
cmd.delete('gly')
