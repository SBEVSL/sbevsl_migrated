'''
FUNC:S_2yyi_1_14_13_3
PDB:2yyi
EC:1.14.13.3
RESI:asn,met
LOCI:a-282,284;
'''
IDSpec[(('met','CE'),('rasn','CG'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+12.28,resSelectionSubs('asn','CG',subs)))
IDSpec[(('met','CE'),('rasn','ND2'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+11.75,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('met','CE'),('rasn','OD1'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+13.37,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('met','CG'),('rasn','CG'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+9.94,resSelectionSubs('asn','CG',subs)))
IDSpec[(('met','CG'),('rasn','ND2'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+9.65,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('met','CG'),('rasn','OD1'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+10.99,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('met','SD'),('rasn','CG'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+10.55,resSelectionSubs('asn','CG',subs)))
IDSpec[(('met','SD'),('rasn','ND2'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+9.99,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('met','SD'),('rasn','OD1'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+11.66,resSelectionSubs('asn','OD1',subs)))
IDSpec['met'] = cmd.select('met',' br. met1&br. met2&br. met3&br. met4&br. met5&br. met6&br. met7&br. met8&br. met9')
IDSpec['r_met'] = cmd.count_atoms(resSelectionSubs('met', subs=subs, selection=True))
cmd.delete('met1')
cmd.delete('met2')
cmd.delete('met3')
cmd.delete('met4')
cmd.delete('met5')
cmd.delete('met6')
cmd.delete('met7')
cmd.delete('met8')
cmd.delete('met9')
IDSpec[(('asn','CG'),('smet','CE'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.28,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asn','CG'),('smet','CG'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.94,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('smet','SD'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.55,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('asn','ND2'),('smet','CE'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.75,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asn','ND2'),('smet','CG'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.65,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('smet','SD'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.99,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('asn','OD1'),('smet','CE'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+13.37,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asn','OD1'),('smet','CG'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.99,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('smet','SD'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.66,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9')
IDSpec['r_asn'] = cmd.count_atoms(resSelectionSubs('asn', subs=subs, selection=True))
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
IDSpec['S_2yyi_1_14_13_3'] = cmd.select('S_2yyi_1_14_13_3', 'met|asn')
cmd.delete('met')
cmd.delete('asn')
