'''
FUNC:S_1qgj_1_11_1_-
PDB:1qgj
EC:1.11.1.-
RESI:arg,his,asn,ala
LOCI:a-38,42,67,71;
'''
IDSpec[(('arg','CZ'),('rhis','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.82,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','CZ'),('rhis','ND1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.52,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','CZ'),('rhis','NE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.34,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NE'),('rhis','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.93,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NE'),('rhis','ND1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.59,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NE'),('rhis','NE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.09,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NH1'),('rhis','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.60,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NH1'),('rhis','ND1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.03,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NH1'),('rhis','NE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.34,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','CZ'),('rala','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.04,resSelectionSubs('ala','CA',subs)))
IDSpec[(('arg','CZ'),('rala','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.57,resSelectionSubs('ala','CB',subs)))
IDSpec[(('arg','CZ'),('rala','CG'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.57,resSelectionSubs('ala','CG',subs)))
IDSpec[(('arg','NE'),('rala','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.75,resSelectionSubs('ala','CA',subs)))
IDSpec[(('arg','NE'),('rala','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.20,resSelectionSubs('ala','CB',subs)))
IDSpec[(('arg','NE'),('rala','CG'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.20,resSelectionSubs('ala','CG',subs)))
IDSpec[(('arg','NH1'),('rala','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.93,resSelectionSubs('ala','CA',subs)))
IDSpec[(('arg','NH1'),('rala','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.71,resSelectionSubs('ala','CB',subs)))
IDSpec[(('arg','NH1'),('rala','CG'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.71,resSelectionSubs('ala','CG',subs)))
IDSpec[(('arg','CZ'),('rasn','CG'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.67,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','CZ'),('rasn','ND2'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.76,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','CZ'),('rasn','OD1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.63,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('arg','NE'),('rasn','CG'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.33,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','NE'),('rasn','ND2'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.32,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','NE'),('rasn','OD1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.20,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('arg','NH1'),('rasn','CG'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.58,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','NH1'),('rasn','ND2'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.79,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','NH1'),('rasn','OD1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.59,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('his','CE1'),('sarg','CZ'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.82,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.93,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NH1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.60,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','CZ'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.52,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.59,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NH1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.03,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','CZ'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.34,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.09,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NH1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.34,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','CE1'),('rala','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.29,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','CE1'),('rala','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.82,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','CE1'),('rala','CG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.82,resSelectionSubs('ala','CG',subs)))
IDSpec[(('his','ND1'),('rala','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.90,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','ND1'),('rala','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.17,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','ND1'),('rala','CG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.17,resSelectionSubs('ala','CG',subs)))
IDSpec[(('his','NE2'),('rala','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.40,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','NE2'),('rala','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.97,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','NE2'),('rala','CG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.97,resSelectionSubs('ala','CG',subs)))
IDSpec[(('his','CE1'),('rasn','CG'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.46,resSelectionSubs('asn','CG',subs)))
IDSpec[(('his','CE1'),('rasn','ND2'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.05,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('his','CE1'),('rasn','OD1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.47,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('his','ND1'),('rasn','CG'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.75,resSelectionSubs('asn','CG',subs)))
IDSpec[(('his','ND1'),('rasn','ND2'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.27,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('his','ND1'),('rasn','OD1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.68,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('his','NE2'),('rasn','CG'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.61,resSelectionSubs('asn','CG',subs)))
IDSpec[(('his','NE2'),('rasn','ND2'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.03,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('his','NE2'),('rasn','OD1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.65,resSelectionSubs('asn','OD1',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
IDSpec[(('ala','CA'),('sarg','CZ'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.04,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ala','CA'),('sarg','NE'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.75,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ala','CA'),('sarg','NH1'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+5.93,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ala','CB'),('sarg','CZ'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.57,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ala','CB'),('sarg','NE'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.20,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ala','CB'),('sarg','NH1'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.71,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ala','CG'),('sarg','CZ'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.71,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ala','CG'),('sarg','NE'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.71,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ala','CG'),('sarg','NH1'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.71,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ala','CA'),('shis','CE1'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.29,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CA'),('shis','ND1'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.90,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CA'),('shis','NE2'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.40,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','CE1'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.82,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','ND1'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.17,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','NE2'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.97,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','CE1'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.97,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','ND1'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.97,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','NE2'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.97,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CA'),('rasn','CG'))] = cmd.select('ala19', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.49,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ala','CA'),('rasn','ND2'))] = cmd.select('ala20', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.73,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ala','CA'),('rasn','OD1'))] = cmd.select('ala21', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.85,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ala','CB'),('rasn','CG'))] = cmd.select('ala22', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.29,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ala','CB'),('rasn','ND2'))] = cmd.select('ala23', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.44,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ala','CB'),('rasn','OD1'))] = cmd.select('ala24', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.73,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ala','CG'),('rasn','CG'))] = cmd.select('ala25', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.73,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ala','CG'),('rasn','ND2'))] = cmd.select('ala26', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.73,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ala','CG'),('rasn','OD1'))] = cmd.select('ala27', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.73,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('sarg','CZ'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.67,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','NE'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.33,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','NH1'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.58,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','CZ'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.76,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','NE'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.32,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','NH1'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.79,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','CZ'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.63,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','NE'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.20,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','NH1'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.59,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','CG'),('shis','CE1'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.46,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asn','CG'),('shis','ND1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.75,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asn','CG'),('shis','NE2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.61,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asn','ND2'),('shis','CE1'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.05,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('shis','ND1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.27,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asn','ND2'),('shis','NE2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.03,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asn','OD1'),('shis','CE1'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.47,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('shis','ND1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.68,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asn','OD1'),('shis','NE2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.65,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asn','CG'),('sala','CA'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.49,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sala','CB'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.29,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('sala','CG'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.29,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sala','CA'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.73,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sala','CB'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.44,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('sala','CG'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.44,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sala','CA'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.85,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sala','CB'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.73,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('sala','CG'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.73,resSelectionSubs('ala','CG',subs,selection=True)))
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
IDSpec['S_1qgj_1_11_1_-'] = cmd.select('S_1qgj_1_11_1_-', 'arg|his|ala|asn')
cmd.delete('arg')
cmd.delete('his')
cmd.delete('ala')
cmd.delete('asn')