'''
FUNC:S_1n4g_1_14_-_-
PDB:1n4g
EC:1.14.-.-
RESI:ser,phe,cys
LOCI:a-237,338,345;
'''
IDSpec[(('phe','CD1'),('rcys','CA'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.38,resSelectionSubs('cys','CA',subs)))
IDSpec[(('phe','CD1'),('rcys','CB'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+5.95,resSelectionSubs('cys','CB',subs)))
IDSpec[(('phe','CD1'),('rcys','SG'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+6.23,resSelectionSubs('cys','SG',subs)))
IDSpec[(('phe','CE1'),('rcys','CA'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+8.45,resSelectionSubs('cys','CA',subs)))
IDSpec[(('phe','CE1'),('rcys','CB'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.00,resSelectionSubs('cys','CB',subs)))
IDSpec[(('phe','CE1'),('rcys','SG'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.85,resSelectionSubs('cys','SG',subs)))
IDSpec[(('phe','CZ'),('rcys','CA'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.47,resSelectionSubs('cys','CA',subs)))
IDSpec[(('phe','CZ'),('rcys','CB'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.10,resSelectionSubs('cys','CB',subs)))
IDSpec[(('phe','CZ'),('rcys','SG'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.06,resSelectionSubs('cys','SG',subs)))
IDSpec[(('phe','CD1'),('rser','CA'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.69,resSelectionSubs('ser','CA',subs)))
IDSpec[(('phe','CD1'),('rser','CB'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.53,resSelectionSubs('ser','CB',subs)))
IDSpec[(('phe','CD1'),('rser','OG'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.05,resSelectionSubs('ser','OG',subs)))
IDSpec[(('phe','CE1'),('rser','CA'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.29,resSelectionSubs('ser','CA',subs)))
IDSpec[(('phe','CE1'),('rser','CB'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.27,resSelectionSubs('ser','CB',subs)))
IDSpec[(('phe','CE1'),('rser','OG'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.01,resSelectionSubs('ser','OG',subs)))
IDSpec[(('phe','CZ'),('rser','CA'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.32,resSelectionSubs('ser','CA',subs)))
IDSpec[(('phe','CZ'),('rser','CB'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.42,resSelectionSubs('ser','CB',subs)))
IDSpec[(('phe','CZ'),('rser','OG'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.26,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('cys','CA'),('sphe','CD1'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.38,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sphe','CE1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.45,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('cys','CA'),('sphe','CZ'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.47,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('cys','CB'),('sphe','CD1'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.95,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sphe','CE1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.00,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('cys','CB'),('sphe','CZ'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.10,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('cys','SG'),('sphe','CD1'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.23,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sphe','CE1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.85,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('cys','SG'),('sphe','CZ'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.06,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('cys','CA'),('rser','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.63,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CA'),('rser','CB'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.10,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CA'),('rser','OG'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.87,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','CB'),('rser','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.45,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CB'),('rser','CB'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.95,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CB'),('rser','OG'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.87,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','SG'),('rser','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.17,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','SG'),('rser','CB'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.66,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','SG'),('rser','OG'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.68,resSelectionSubs('ser','OG',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18')
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
IDSpec[(('ser','CA'),('sphe','CD1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.69,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sphe','CE1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.29,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('ser','CA'),('sphe','CZ'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.32,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('ser','CB'),('sphe','CD1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.53,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sphe','CE1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.27,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('ser','CB'),('sphe','CZ'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.42,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('ser','OG'),('sphe','CD1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.05,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sphe','CE1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.01,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('ser','OG'),('sphe','CZ'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.26,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.63,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.45,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','SG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.17,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.10,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.95,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','SG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.66,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.87,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.87,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','SG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.68,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18')
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
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
IDSpec['S_1n4g_1_14_-_-'] = cmd.select('S_1n4g_1_14_-_-', 'phe|cys|ser')
cmd.delete('phe')
cmd.delete('cys')
cmd.delete('ser')
