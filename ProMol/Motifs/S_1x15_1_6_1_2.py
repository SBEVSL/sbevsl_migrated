'''
FUNC:S_1x15_1_6_1_2
PDB:1x15
EC:1.6.1.2
RESI:arg,gln,asp,ser
LOCI:a-1120,1125,1128,1131;
'''
IDSpec[(('arg','CZ'),('rser','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.33,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','CZ'),('rser','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.11,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','CZ'),('rser','OG'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.18,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','NE'),('rser','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.59,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','NE'),('rser','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.22,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','NE'),('rser','OG'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.27,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','NH1'),('rser','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.68,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','NH1'),('rser','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.49,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','NH1'),('rser','OG'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.47,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','CZ'),('rasp','CG'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.30,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','CZ'),('rasp','OD1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.01,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','CZ'),('rasp','OD2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.65,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NE'),('rasp','CG'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.21,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NE'),('rasp','OD1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.06,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NE'),('rasp','OD2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.49,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NH1'),('rasp','CG'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.06,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NH1'),('rasp','OD1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.76,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NH1'),('rasp','OD2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.33,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','CZ'),('rgln','CD'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.70,resSelectionSubs('gln','CD',subs)))
IDSpec[(('arg','CZ'),('rgln','NE2'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.50,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('arg','CZ'),('rgln','OE1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.06,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('arg','NE'),('rgln','CD'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.43,resSelectionSubs('gln','CD',subs)))
IDSpec[(('arg','NE'),('rgln','NE2'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.21,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('arg','NE'),('rgln','OE1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.83,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('arg','NH1'),('rgln','CD'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.15,resSelectionSubs('gln','CD',subs)))
IDSpec[(('arg','NH1'),('rgln','NE2'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.97,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('arg','NH1'),('rgln','OE1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.43,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('ser','CA'),('sarg','CZ'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.33,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','NE'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.59,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','NH1'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.68,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','CZ'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.11,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','NE'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.22,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','NH1'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.49,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','CZ'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.18,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','NE'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.27,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','NH1'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.47,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','CA'),('rasp','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.34,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CA'),('rasp','OD1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.83,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CA'),('rasp','OD2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.84,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CB'),('rasp','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.52,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CB'),('rasp','OD1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.46,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CB'),('rasp','OD2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.82,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','OG'),('rasp','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.65,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','OG'),('rasp','OD1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.78,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','OG'),('rasp','OD2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.80,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CA'),('rgln','CD'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.36,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CA'),('rgln','NE2'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.69,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CA'),('rgln','OE1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.98,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','CB'),('rgln','CD'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.86,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CB'),('rgln','NE2'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.18,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CB'),('rgln','OE1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.52,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','OG'),('rgln','CD'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.35,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','OG'),('rgln','NE2'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.69,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','OG'),('rgln','OE1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.81,resSelectionSubs('gln','OE1',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27')
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
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.delete('ser23')
cmd.delete('ser24')
cmd.delete('ser25')
cmd.delete('ser26')
cmd.delete('ser27')
IDSpec[(('asp','CG'),('sarg','CZ'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.30,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.21,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NH1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.06,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','CZ'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.01,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.06,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NH1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.76,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','CZ'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.65,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.49,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NH1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.33,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.34,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.52,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.65,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.83,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.46,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.78,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.84,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.82,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.80,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','CG'),('rgln','CD'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.70,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','CG'),('rgln','NE2'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.79,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','CG'),('rgln','OE1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.93,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD1'),('rgln','CD'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.86,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD1'),('rgln','NE2'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.99,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD1'),('rgln','OE1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.00,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD2'),('rgln','CD'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.24,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD2'),('rgln','NE2'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.30,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD2'),('rgln','OE1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.50,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('sarg','CZ'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.70,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gln','CD'),('sarg','NE'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+14.43,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gln','CD'),('sarg','NH1'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.15,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sarg','CZ'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.50,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gln','NE2'),('sarg','NE'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+15.21,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gln','NE2'),('sarg','NH1'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.97,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sarg','CZ'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+16.06,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gln','OE1'),('sarg','NE'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.83,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gln','OE1'),('sarg','NH1'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+16.43,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','CA'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.36,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','CB'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.86,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','OG'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.35,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CA'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.69,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CB'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.18,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','OG'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.69,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CA'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.98,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CB'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.52,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','OG'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.81,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','CG'))] = cmd.select('gln19', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.70,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD1'))] = cmd.select('gln20', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.86,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD2'))] = cmd.select('gln21', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.24,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','CG'))] = cmd.select('gln22', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.79,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD1'))] = cmd.select('gln23', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.99,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD2'))] = cmd.select('gln24', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.30,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','CG'))] = cmd.select('gln25', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.93,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD1'))] = cmd.select('gln26', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD2'))] = cmd.select('gln27', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.50,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18&br. gln19&br. gln20&br. gln21&br. gln22&br. gln23&br. gln24&br. gln25&br. gln26&br. gln27')
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
cmd.delete('gln19')
cmd.delete('gln20')
cmd.delete('gln21')
cmd.delete('gln22')
cmd.delete('gln23')
cmd.delete('gln24')
cmd.delete('gln25')
cmd.delete('gln26')
cmd.delete('gln27')
IDSpec['S_1x15_1_6_1_2'] = cmd.select('S_1x15_1_6_1_2', 'arg|ser|asp|gln')
cmd.delete('arg')
cmd.delete('ser')
cmd.delete('asp')
cmd.delete('gln')
