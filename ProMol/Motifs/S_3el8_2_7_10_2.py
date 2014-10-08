'''
FUNC:S_3el8_2_7_10_2
PDB:3el8
EC:2.7.10.2
RESI:asp,arg,ala,asn
LOCI:a-386,388,390,391;
'''
IDSpec[(('asp','CG'),('rala','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.14,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','CG'),('rala','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.61,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','CG'),('rala','CG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.61,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asp','OD1'),('rala','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.93,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','OD1'),('rala','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.34,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','OD1'),('rala','CG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.34,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asp','OD2'),('rala','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.95,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','OD2'),('rala','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.31,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','OD2'),('rala','CG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.31,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.53,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.13,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.91,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.64,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.29,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.99,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.56,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.27,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.96,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','CG'),('rasn','CG'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','CG'),('rasn','ND2'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.26,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','CG'),('rasn','OD1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.25,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD1'),('rasn','CG'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.03,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD1'),('rasn','ND2'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.74,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD1'),('rasn','OD1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.74,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD2'),('rasn','CG'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.31,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD2'),('rasn','ND2'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.12,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD2'),('rasn','OD1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.71,resSelectionSubs('asn','OD1',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27')
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
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
IDSpec[(('ala','CA'),('sasp','CG'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10.14,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CA'),('sasp','OD1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.93,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CA'),('sasp','OD2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.95,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','CG'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.61,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','OD1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.34,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','OD2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.31,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','CG'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.31,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','OD1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.31,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','OD2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.31,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CA'),('rarg','CZ'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.21,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ala','CA'),('rarg','NE'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.19,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ala','CA'),('rarg','NH1'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.29,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ala','CB'),('rarg','CZ'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.06,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ala','CB'),('rarg','NE'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.24,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ala','CB'),('rarg','NH1'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.15,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ala','CG'),('rarg','CZ'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.15,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ala','CG'),('rarg','NE'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.15,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ala','CG'),('rarg','NH1'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.15,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ala','CA'),('rasn','CG'))] = cmd.select('ala19', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.77,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ala','CA'),('rasn','ND2'))] = cmd.select('ala20', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.55,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ala','CA'),('rasn','OD1'))] = cmd.select('ala21', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.54,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ala','CB'),('rasn','CG'))] = cmd.select('ala22', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.87,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ala','CB'),('rasn','ND2'))] = cmd.select('ala23', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.42,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ala','CB'),('rasn','OD1'))] = cmd.select('ala24', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.50,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ala','CG'),('rasn','CG'))] = cmd.select('ala25', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.50,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ala','CG'),('rasn','ND2'))] = cmd.select('ala26', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.50,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ala','CG'),('rasn','OD1'))] = cmd.select('ala27', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.50,resSelectionSubs('asn','OD1',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18&br. ala19&br. ala20&br. ala21&br. ala22&br. ala23&br. ala24&br. ala25&br. ala26&br. ala27')
IDSpec['r_ala'] = cmd.count_atoms(resSelectionSubs('ala', subs=subs, selection=True))
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.delete('ala6')
cmd.delete('ala7')
cmd.delete('ala8')
cmd.delete('ala9')
cmd.delete('ala10')
cmd.delete('ala11')
cmd.delete('ala12')
cmd.delete('ala13')
cmd.delete('ala14')
cmd.delete('ala15')
cmd.delete('ala16')
cmd.delete('ala17')
cmd.delete('ala18')
cmd.delete('ala19')
cmd.delete('ala20')
cmd.delete('ala21')
cmd.delete('ala22')
cmd.delete('ala23')
cmd.delete('ala24')
cmd.delete('ala25')
cmd.delete('ala26')
cmd.delete('ala27')
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.53,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.64,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.56,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.13,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.29,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.27,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.91,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.99,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.96,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sala','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.21,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sala','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.06,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sala','CG'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.06,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sala','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.19,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sala','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.24,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sala','CG'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.24,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sala','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.29,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sala','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.15,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sala','CG'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.15,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('rasn','CG'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.48,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','CZ'),('rasn','ND2'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.87,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','CZ'),('rasn','OD1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.64,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('arg','NE'),('rasn','CG'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.47,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','NE'),('rasn','ND2'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.94,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','NE'),('rasn','OD1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.75,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('arg','NH1'),('rasn','CG'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.78,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','NH1'),('rasn','ND2'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.97,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','NH1'),('rasn','OD1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.00,resSelectionSubs('asn','OD1',subs)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27')
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
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
IDSpec[(('asn','CG'),('sasp','CG'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.57,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.03,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.31,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','CG'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.26,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.74,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.12,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','CG'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.25,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.74,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.71,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','CG'),('sala','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.77,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sala','CB'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.87,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('sala','CG'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.87,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sala','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.55,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sala','CB'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.42,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('sala','CG'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.42,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sala','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.54,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sala','CB'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.50,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('sala','CG'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.50,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','CZ'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.48,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','NE'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.47,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','NH1'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.78,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','CZ'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.87,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','NE'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.94,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','NH1'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.97,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','CZ'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.64,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','NE'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.75,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','NH1'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.00,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27')
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
cmd.delete('asn19')
cmd.delete('asn20')
cmd.delete('asn21')
cmd.delete('asn22')
cmd.delete('asn23')
cmd.delete('asn24')
cmd.delete('asn25')
cmd.delete('asn26')
cmd.delete('asn27')
IDSpec['S_3el8_2_7_10_2'] = cmd.select('S_3el8_2_7_10_2', 'asp|ala|arg|asn')
cmd.delete('asp')
cmd.delete('ala')
cmd.delete('arg')
cmd.delete('asn')
