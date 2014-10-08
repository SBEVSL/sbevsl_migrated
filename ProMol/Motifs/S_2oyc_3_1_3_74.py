'''
FUNC:S_2oyc_3_1_3_74
PDB:2oyc
EC:3.1.3.74
RESI:asp,arg,ser,asp
LOCI:a-25,49,134,243;
'''
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+41.48,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+41.88,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+41.07,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+40.32,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+40.73,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+39.92,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+41.87,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+42.26,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+41.47,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','CG'),('rasp_i','CG'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.60,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD1'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.70,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD2'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.16,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp_i','CG'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.06,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD1'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.00,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD2'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.77,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp_i','CG'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.38,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD1'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.58,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD2'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.73,resSelectionSubs('asp_i','OD2',subs)))
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
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','CZ'),('rser','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','CZ'),('rser','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','CZ'),('rser','OG'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','NE'),('rser','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','NE'),('rser','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','NE'),('rser','OG'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','NH1'),('rser','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','NH1'),('rser','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','NH1'),('rser','OG'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','CZ'),('rasp_i','CG'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('arg','CZ'),('rasp_i','OD1'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('arg','CZ'),('rasp_i','OD2'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('arg','NE'),('rasp_i','CG'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('arg','NE'),('rasp_i','OD1'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('arg','NE'),('rasp_i','OD2'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.73,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('arg','NH1'),('rasp_i','CG'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('arg','NH1'),('rasp_i','OD1'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('arg','NH1'),('rasp_i','OD2'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.73,resSelectionSubs('asp_i','OD2',subs)))
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
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+41.48,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+40.32,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+41.87,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+41.88,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+40.73,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+42.26,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+41.07,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+39.92,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+41.47,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','CZ'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+41.47,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','NE'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+41.47,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','NH1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+41.47,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','CZ'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+41.47,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','NE'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+41.47,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','NH1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+41.47,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','CZ'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+41.47,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','NE'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+41.47,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','NH1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+41.47,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','CA'),('rasp_i','CG'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+39.15,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('ser','CA'),('rasp_i','OD1'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+38.11,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('ser','CA'),('rasp_i','OD2'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+39.33,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('ser','CB'),('rasp_i','CG'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+39.66,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('ser','CB'),('rasp_i','OD1'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+38.65,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('ser','CB'),('rasp_i','OD2'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+39.80,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('ser','OG'),('rasp_i','CG'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+38.98,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('ser','OG'),('rasp_i','OD1'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+37.99,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('ser','OG'),('rasp_i','OD2'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+39.10,resSelectionSubs('asp_i','OD2',subs)))
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
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.60,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.06,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.38,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.70,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.58,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.16,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.77,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sarg','CZ'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.73,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sarg','NE'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.73,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sarg','NH1'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.73,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sarg','CZ'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.73,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sarg','NE'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.73,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sarg','NH1'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.73,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sarg','CZ'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.73,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sarg','NE'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.73,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sarg','NH1'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.73,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sser','CA'))] = cmd.select('asp_i19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+39.15,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sser','CB'))] = cmd.select('asp_i20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+39.66,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sser','OG'))] = cmd.select('asp_i21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+38.98,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sser','CA'))] = cmd.select('asp_i22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+38.11,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sser','CB'))] = cmd.select('asp_i23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+38.65,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sser','OG'))] = cmd.select('asp_i24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+37.99,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sser','CA'))] = cmd.select('asp_i25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+39.33,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sser','CB'))] = cmd.select('asp_i26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+39.80,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sser','OG'))] = cmd.select('asp_i27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+39.10,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec['asp_i'] = cmd.select('asp_i',' br. asp_i1&br. asp_i2&br. asp_i3&br. asp_i4&br. asp_i5&br. asp_i6&br. asp_i7&br. asp_i8&br. asp_i9&br. asp_i10&br. asp_i11&br. asp_i12&br. asp_i13&br. asp_i14&br. asp_i15&br. asp_i16&br. asp_i17&br. asp_i18&br. asp_i19&br. asp_i20&br. asp_i21&br. asp_i22&br. asp_i23&br. asp_i24&br. asp_i25&br. asp_i26&br. asp_i27')
IDSpec['r_asp_i'] = cmd.count_atoms(resSelectionSubs('asp_i', subs=subs, selection=True))
cmd.delete('asp_i1')
cmd.delete('asp_i2')
cmd.delete('asp_i3')
cmd.delete('asp_i4')
cmd.delete('asp_i5')
cmd.delete('asp_i6')
cmd.delete('asp_i7')
cmd.delete('asp_i8')
cmd.delete('asp_i9')
cmd.delete('asp_i10')
cmd.delete('asp_i11')
cmd.delete('asp_i12')
cmd.delete('asp_i13')
cmd.delete('asp_i14')
cmd.delete('asp_i15')
cmd.delete('asp_i16')
cmd.delete('asp_i17')
cmd.delete('asp_i18')
cmd.delete('asp_i19')
cmd.delete('asp_i20')
cmd.delete('asp_i21')
cmd.delete('asp_i22')
cmd.delete('asp_i23')
cmd.delete('asp_i24')
cmd.delete('asp_i25')
cmd.delete('asp_i26')
cmd.delete('asp_i27')
IDSpec['S_2oyc_3_1_3_74'] = cmd.select('S_2oyc_3_1_3_74', 'asp|arg|ser|asp_i')
cmd.delete('asp')
cmd.delete('arg')
cmd.delete('ser')
cmd.delete('asp_i')
