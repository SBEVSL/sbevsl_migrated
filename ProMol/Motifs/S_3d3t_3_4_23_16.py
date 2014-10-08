'''
FUNC:S_3d3t_3_4_23_16
PDB:3d3t
EC:3.4.23.16
RESI:asn,thr
LOCI:a-25,26;
'''
IDSpec[(('asn','CG'),('rthr','CA'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.16,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asn','CG'),('rthr','CB'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.36,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asn','CG'),('rthr','OG1'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.17,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asn','ND2'),('rthr','CA'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.37,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asn','ND2'),('rthr','CB'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.60,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asn','ND2'),('rthr','OG1'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.42,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asn','OD1'),('rthr','CA'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.67,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asn','OD1'),('rthr','CB'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.70,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asn','OD1'),('rthr','OG1'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.32,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('thr','CA'),('sasn','CG'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.16,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('sasn','ND2'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.37,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('thr','CA'),('sasn','OD1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.67,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('thr','CB'),('sasn','CG'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.36,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('sasn','ND2'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.60,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('thr','CB'),('sasn','OD1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.70,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasn','CG'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.17,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasn','ND2'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.42,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasn','OD1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.32,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_3d3t_3_4_23_16'] = cmd.select('S_3d3t_3_4_23_16', 'asn|thr')
cmd.delete('asn')
cmd.delete('thr')
