'''
FUNC:S_1bd4_2_4_2_9
PDB:1bd4
EC:2.4.2.9
RESI:arg,thr,asp
LOCI:a-137,141,235;
'''
IDSpec[(('thr','CA'),('rarg','CZ'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.61,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CA'),('rarg','NE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.43,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CA'),('rarg','NH1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.68,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','CB'),('rarg','CZ'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.06,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CB'),('rarg','NE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.93,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CB'),('rarg','NH1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.09,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','OG1'),('rarg','CZ'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.44,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','OG1'),('rarg','NE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.34,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','OG1'),('rarg','NH1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.43,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','CA'),('rasp','CG'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+21.41,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','CA'),('rasp','OD1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+22.05,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','CA'),('rasp','OD2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+20.21,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','CB'),('rasp','CG'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+22.14,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','CB'),('rasp','OD1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+22.70,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','CB'),('rasp','OD2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+20.94,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','OG1'),('rasp','CG'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+23.47,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','OG1'),('rasp','OD1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+24.04,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','OG1'),('rasp','OD2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+22.27,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('arg','CZ'),('sthr','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.61,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sthr','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.06,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sthr','OG1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.44,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.43,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.93,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','OG1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.34,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.68,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.09,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','OG1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.43,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','CZ'),('rasp','CG'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.22,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','CZ'),('rasp','OD1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.85,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','CZ'),('rasp','OD2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.01,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NE'),('rasp','CG'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.22,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NE'),('rasp','OD1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.84,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NE'),('rasp','OD2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.99,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NH1'),('rasp','CG'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.46,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NH1'),('rasp','OD1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NH1'),('rasp','OD2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.24,resSelectionSubs('asp','OD2',subs)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18')
IDSpec['r_arg'] = cmd.count_atoms(resSelectionSubs('arg', subs=subs, selection=True))
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
IDSpec[(('asp','CG'),('sthr','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+21.41,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+22.14,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','OG1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+23.47,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+22.05,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+22.70,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','OG1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+24.04,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+20.21,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+20.94,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','OG1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+22.27,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','CZ'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.22,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.22,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NH1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.46,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','CZ'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.85,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.84,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NH1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.10,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','CZ'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.01,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.99,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NH1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.24,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18')
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
IDSpec['S_1bd4_2_4_2_9'] = cmd.select('S_1bd4_2_4_2_9', 'thr|arg|asp')
cmd.delete('thr')
cmd.delete('arg')
cmd.delete('asp')