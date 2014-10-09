'''
FUNC:S_2fiv_3_4_23_16
PDB:2fiv
EC:3.4.23.16
RESI:asn,thr
LOCI:a-30,31;
'''
IDSpec[(('thr','CA'),('rasn','CG'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.40,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','CA'),('rasn','ND2'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.85,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','CA'),('rasn','OD1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.54,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','CB'),('rasn','CG'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.56,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','CB'),('rasn','ND2'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.01,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','CB'),('rasn','OD1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.61,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','OG1'),('rasn','CG'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.36,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','OG1'),('rasn','ND2'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.76,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','OG1'),('rasn','OD1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.27,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('sthr','CA'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.40,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','CB'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.56,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','OG1'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.36,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','CA'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.85,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','CB'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.01,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','OG1'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.76,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','CA'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.54,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','CB'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.61,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','OG1'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.27,resSelectionSubs('thr','OG1',subs,selection=True)))
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
IDSpec['S_2fiv_3_4_23_16'] = cmd.select('S_2fiv_3_4_23_16', 'thr|asn')
cmd.delete('thr')
cmd.delete('asn')