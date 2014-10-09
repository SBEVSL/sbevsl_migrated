'''
FUNC:S_1w96_6_4_1_2
PDB:1w96
EC:6.4.1.2
RESI:lys,gln,arg
LOCI:a-252,302,317;
'''
IDSpec[(('gln','CD'),('rarg','CZ'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.52,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gln','CD'),('rarg','NE'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.83,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gln','CD'),('rarg','NH1'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+5.81,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gln','NE2'),('rarg','CZ'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.53,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gln','NE2'),('rarg','NE'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.86,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gln','NE2'),('rarg','NH1'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.00,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gln','OE1'),('rarg','CZ'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+5.48,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gln','OE1'),('rarg','NE'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.79,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gln','OE1'),('rarg','NH1'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+4.82,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gln','CD'),('rlys','CD'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+27.23,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gln','CD'),('rlys','CE'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+26.95,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gln','CD'),('rlys','NZ'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+27.59,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gln','NE2'),('rlys','CD'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+26.96,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gln','NE2'),('rlys','CE'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+26.75,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gln','NE2'),('rlys','NZ'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+27.45,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gln','OE1'),('rlys','CD'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+26.91,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gln','OE1'),('rlys','CE'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+26.60,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gln','OE1'),('rlys','NZ'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+27.18,resSelectionSubs('lys','NZ',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18')
IDSpec['r_gln'] = cmd.count_atoms(resSelectionSubs('gln', subs=subs, selection=True))
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
IDSpec[(('arg','CZ'),('sgln','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.52,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgln','NE2'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.53,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgln','OE1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.48,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sgln','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.83,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sgln','NE2'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.86,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sgln','OE1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.79,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgln','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.81,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgln','NE2'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.00,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgln','OE1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+4.82,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('rlys','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+25.52,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','CZ'),('rlys','CE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+25.04,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','CZ'),('rlys','NZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+25.47,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NE'),('rlys','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+25.35,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NE'),('rlys','CE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+24.81,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NE'),('rlys','NZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+25.16,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NH1'),('rlys','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+26.73,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NH1'),('rlys','CE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+26.27,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NH1'),('rlys','NZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+26.73,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('sgln','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+27.23,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('sgln','NE2'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+26.96,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('lys','CD'),('sgln','OE1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+26.91,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sgln','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+26.95,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('sgln','NE2'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+26.75,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('lys','CE'),('sgln','OE1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+26.60,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgln','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+27.59,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgln','NE2'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+27.45,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgln','OE1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+27.18,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','CZ'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+25.52,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+25.35,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NH1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+26.73,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','CZ'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+25.04,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+24.81,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NH1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+26.27,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','CZ'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+25.47,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+25.16,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NH1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+26.73,resSelectionSubs('arg','NH1',subs,selection=True)))
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
IDSpec['S_1w96_6_4_1_2'] = cmd.select('S_1w96_6_4_1_2', 'gln|arg|lys')
cmd.delete('gln')
cmd.delete('arg')
cmd.delete('lys')