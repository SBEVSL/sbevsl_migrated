'''
FUNC:S_3gpx_4_2_99_18
PDB:3gpx
EC:4.2.99.18
RESI:pro,glu,lys,arg
LOCI:a-2,3,60,264;
'''
IDSpec[(('arg','CZ'),('rpro','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+17.01,resSelectionSubs('pro','CA',subs)))
IDSpec[(('arg','CZ'),('rpro','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.28,resSelectionSubs('pro','CB',subs)))
IDSpec[(('arg','CZ'),('rpro','CD'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+17.41,resSelectionSubs('pro','CD',subs)))
IDSpec[(('arg','NE'),('rpro','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.18,resSelectionSubs('pro','CA',subs)))
IDSpec[(('arg','NE'),('rpro','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.50,resSelectionSubs('pro','CB',subs)))
IDSpec[(('arg','NE'),('rpro','CD'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.72,resSelectionSubs('pro','CD',subs)))
IDSpec[(('arg','NH1'),('rpro','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.72,resSelectionSubs('pro','CA',subs)))
IDSpec[(('arg','NH1'),('rpro','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.91,resSelectionSubs('pro','CB',subs)))
IDSpec[(('arg','NH1'),('rpro','CD'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.03,resSelectionSubs('pro','CD',subs)))
IDSpec[(('arg','CZ'),('rlys','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.90,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','CZ'),('rlys','CE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.64,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','CZ'),('rlys','NZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.58,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NE'),('rlys','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.29,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NE'),('rlys','CE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.07,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NE'),('rlys','NZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.90,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NH1'),('rlys','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.30,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NH1'),('rlys','CE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.00,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NH1'),('rlys','NZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.06,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','CZ'),('rglu','CD'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.15,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','CZ'),('rglu','OE1'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.20,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','CZ'),('rglu','OE2'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.11,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NE'),('rglu','CD'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.13,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NE'),('rglu','OE1'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.15,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NE'),('rglu','OE2'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.16,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NH1'),('rglu','CD'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.05,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NH1'),('rglu','OE1'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.16,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NH1'),('rglu','OE2'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.89,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('pro','CA'),('sarg','CZ'))] = cmd.select('pro1', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+17.01,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('pro','CA'),('sarg','NE'))] = cmd.select('pro2', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+16.18,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('pro','CA'),('sarg','NH1'))] = cmd.select('pro3', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+16.72,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('pro','CB'),('sarg','CZ'))] = cmd.select('pro4', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+18.28,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('pro','CB'),('sarg','NE'))] = cmd.select('pro5', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+17.50,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('pro','CB'),('sarg','NH1'))] = cmd.select('pro6', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+17.91,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('pro','CD'),('sarg','CZ'))] = cmd.select('pro7', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+17.41,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('pro','CD'),('sarg','NE'))] = cmd.select('pro8', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+16.72,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('pro','CD'),('sarg','NH1'))] = cmd.select('pro9', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+17.03,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('pro','CA'),('rlys','CD'))] = cmd.select('pro10', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+8.04,resSelectionSubs('lys','CD',subs)))
IDSpec[(('pro','CA'),('rlys','CE'))] = cmd.select('pro11', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+9.26,resSelectionSubs('lys','CE',subs)))
IDSpec[(('pro','CA'),('rlys','NZ'))] = cmd.select('pro12', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+9.14,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('pro','CB'),('rlys','CD'))] = cmd.select('pro13', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+8.58,resSelectionSubs('lys','CD',subs)))
IDSpec[(('pro','CB'),('rlys','CE'))] = cmd.select('pro14', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+9.94,resSelectionSubs('lys','CE',subs)))
IDSpec[(('pro','CB'),('rlys','NZ'))] = cmd.select('pro15', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+10.08,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('pro','CD'),('rlys','CD'))] = cmd.select('pro16', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+9.13,resSelectionSubs('lys','CD',subs)))
IDSpec[(('pro','CD'),('rlys','CE'))] = cmd.select('pro17', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+10.27,resSelectionSubs('lys','CE',subs)))
IDSpec[(('pro','CD'),('rlys','NZ'))] = cmd.select('pro18', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+10.24,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('pro','CA'),('rglu','CD'))] = cmd.select('pro19', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+7.71,resSelectionSubs('glu','CD',subs)))
IDSpec[(('pro','CA'),('rglu','OE1'))] = cmd.select('pro20', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+8.05,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('pro','CA'),('rglu','OE2'))] = cmd.select('pro21', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+8.21,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('pro','CB'),('rglu','CD'))] = cmd.select('pro22', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+8.97,resSelectionSubs('glu','CD',subs)))
IDSpec[(('pro','CB'),('rglu','OE1'))] = cmd.select('pro23', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+9.43,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('pro','CB'),('rglu','OE2'))] = cmd.select('pro24', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+9.31,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('pro','CD'),('rglu','CD'))] = cmd.select('pro25', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+9.57,resSelectionSubs('glu','CD',subs)))
IDSpec[(('pro','CD'),('rglu','OE1'))] = cmd.select('pro26', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+9.67,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('pro','CD'),('rglu','OE2'))] = cmd.select('pro27', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+10.02,resSelectionSubs('glu','OE2',subs)))
IDSpec['pro'] = cmd.select('pro',' br. pro1&br. pro2&br. pro3&br. pro4&br. pro5&br. pro6&br. pro7&br. pro8&br. pro9&br. pro10&br. pro11&br. pro12&br. pro13&br. pro14&br. pro15&br. pro16&br. pro17&br. pro18&br. pro19&br. pro20&br. pro21&br. pro22&br. pro23&br. pro24&br. pro25&br. pro26&br. pro27')
IDSpec['r_pro'] = cmd.count_atoms(resSelectionSubs('pro', subs=subs, selection=True))
cmd.delete('pro1')
cmd.delete('pro2')
cmd.delete('pro3')
cmd.delete('pro4')
cmd.delete('pro5')
cmd.delete('pro6')
cmd.delete('pro7')
cmd.delete('pro8')
cmd.delete('pro9')
cmd.delete('pro10')
cmd.delete('pro11')
cmd.delete('pro12')
cmd.delete('pro13')
cmd.delete('pro14')
cmd.delete('pro15')
cmd.delete('pro16')
cmd.delete('pro17')
cmd.delete('pro18')
cmd.delete('pro19')
cmd.delete('pro20')
cmd.delete('pro21')
cmd.delete('pro22')
cmd.delete('pro23')
cmd.delete('pro24')
cmd.delete('pro25')
cmd.delete('pro26')
cmd.delete('pro27')
IDSpec[(('lys','CD'),('sarg','CZ'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.90,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.29,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NH1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.30,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','CZ'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.64,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.07,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NH1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.00,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','CZ'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.58,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.90,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NH1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.06,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CD'),('spro','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.04,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('spro','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.58,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('spro','CD'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.13,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('spro','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.26,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('spro','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.94,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('spro','CD'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.27,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('spro','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.14,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('spro','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.08,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('spro','CD'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.24,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('rglu','CD'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.51,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CD'),('rglu','OE1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.09,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CD'),('rglu','OE2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.65,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CE'),('rglu','CD'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.68,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CE'),('rglu','OE1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.06,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CE'),('rglu','OE2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.71,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','NZ'),('rglu','CD'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.75,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','NZ'),('rglu','OE1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.86,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','NZ'),('rglu','OE2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.94,resSelectionSubs('glu','OE2',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27')
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
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
IDSpec[(('glu','CD'),('sarg','CZ'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.15,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','NE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.13,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','NH1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.05,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','CZ'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.20,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','NE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.15,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','NH1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.16,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','CZ'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.11,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','NE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.16,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','NH1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.89,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','CD'),('spro','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.71,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('spro','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.97,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('spro','CD'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.57,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('spro','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.05,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('spro','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.43,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('spro','CD'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.67,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('spro','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.21,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('spro','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.31,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('spro','CD'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.02,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.51,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','CE'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.68,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','NZ'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.75,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.09,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CE'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.06,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','NZ'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.86,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.65,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CE'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.71,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','NZ'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.94,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
IDSpec['S_3gpx_4_2_99_18'] = cmd.select('S_3gpx_4_2_99_18', 'arg|pro|lys|glu')
cmd.delete('arg')
cmd.delete('pro')
cmd.delete('lys')
cmd.delete('glu')
