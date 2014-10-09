'''
FUNC:S_2ohh_1_-_-_-
PDB:2ohh
EC:1.-.-.-
RESI:asp,arg,asn
LOCI:a-87,181,201;
'''
IDSpec[(('asp','CG'),('rasn','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.35,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','CG'),('rasn','ND2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.95,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','CG'),('rasn','OD1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.84,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD1'),('rasn','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.67,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD1'),('rasn','ND2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.33,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD1'),('rasn','OD1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.13,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD2'),('rasn','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.26,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD2'),('rasn','ND2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.81,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD2'),('rasn','OD1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.80,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.97,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.17,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.70,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.94,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+18.07,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+18.71,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.43,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.68,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+17.18,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('asn','CG'),('sasp','CG'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+16.35,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+16.67,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+15.26,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','CG'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+16.95,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+17.33,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+15.81,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','CG'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+16.84,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+17.13,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+15.80,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','CG'),('rarg','CZ'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+22.94,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asn','CG'),('rarg','NE'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+23.54,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asn','CG'),('rarg','NH1'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+23.68,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asn','ND2'),('rarg','CZ'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+22.51,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asn','ND2'),('rarg','NE'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+23.13,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asn','ND2'),('rarg','NH1'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+23.23,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asn','OD1'),('rarg','CZ'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+23.95,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asn','OD1'),('rarg','NE'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+24.58,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asn','OD1'),('rarg','NH1'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+24.66,resSelectionSubs('arg','NH1',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18')
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
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.97,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+17.94,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.43,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.17,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.07,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.68,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.70,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+18.71,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.18,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasn','CG'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+22.94,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasn','ND2'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+22.51,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasn','OD1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+23.95,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasn','CG'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+23.54,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasn','ND2'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+23.13,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasn','OD1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+24.58,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasn','CG'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+23.68,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasn','ND2'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+23.23,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasn','OD1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+24.66,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_2ohh_1_-_-_-'] = cmd.select('S_2ohh_1_-_-_-', 'asp|asn|arg')
cmd.delete('asp')
cmd.delete('asn')
cmd.delete('arg')