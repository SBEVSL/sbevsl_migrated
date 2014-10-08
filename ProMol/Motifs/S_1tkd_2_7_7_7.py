'''
FUNC:S_1tkd_2_7_7_7
PDB:1tkd
EC:2.7.7.7
RESI:cys,gly,pro,cys
LOCI:b-32,33,34,35;
'''
IDSpec[(('pro','CA'),('rcys','CA'))] = cmd.select('pro1', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+5.83,resSelectionSubs('cys','CA',subs)))
IDSpec[(('pro','CA'),('rcys','CB'))] = cmd.select('pro2', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+6.90,resSelectionSubs('cys','CB',subs)))
IDSpec[(('pro','CA'),('rcys','SG'))] = cmd.select('pro3', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+7.51,resSelectionSubs('cys','SG',subs)))
IDSpec[(('pro','CB'),('rcys','CA'))] = cmd.select('pro4', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+6.56,resSelectionSubs('cys','CA',subs)))
IDSpec[(('pro','CB'),('rcys','CB'))] = cmd.select('pro5', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+7.44,resSelectionSubs('cys','CB',subs)))
IDSpec[(('pro','CB'),('rcys','SG'))] = cmd.select('pro6', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+7.55,resSelectionSubs('cys','SG',subs)))
IDSpec[(('pro','CD'),('rcys','CA'))] = cmd.select('pro7', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+7.32,resSelectionSubs('cys','CA',subs)))
IDSpec[(('pro','CD'),('rcys','CB'))] = cmd.select('pro8', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+7.85,resSelectionSubs('cys','CB',subs)))
IDSpec[(('pro','CD'),('rcys','SG'))] = cmd.select('pro9', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+8.15,resSelectionSubs('cys','SG',subs)))
IDSpec[(('pro','CA'),('rcys_i','CA'))] = cmd.select('pro10', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+7.66,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('pro','CA'),('rcys_i','CB'))] = cmd.select('pro11', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+7.47,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('pro','CA'),('rcys_i','SG'))] = cmd.select('pro12', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+6.18,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('pro','CB'),('rcys_i','CA'))] = cmd.select('pro13', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+8.01,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('pro','CB'),('rcys_i','CB'))] = cmd.select('pro14', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+7.57,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('pro','CB'),('rcys_i','SG'))] = cmd.select('pro15', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+5.95,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('pro','CD'),('rcys_i','CA'))] = cmd.select('pro16', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+6.65,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('pro','CD'),('rcys_i','CB'))] = cmd.select('pro17', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+6.73,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('pro','CD'),('rcys_i','SG'))] = cmd.select('pro18', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+5.50,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('pro','CA'),('rgly','CA'))] = cmd.select('pro19', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+5.84,resSelectionSubs('gly','CA',subs)))
IDSpec[(('pro','CA'),('rgly','N'))] = cmd.select('pro20', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+6.35,resSelectionSubs('gly','N',subs)))
IDSpec[(('pro','CA'),('rgly','O'))] = cmd.select('pro21', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+4.78,resSelectionSubs('gly','O',subs)))
IDSpec[(('pro','CB'),('rgly','CA'))] = cmd.select('pro22', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+6.75,resSelectionSubs('gly','CA',subs)))
IDSpec[(('pro','CB'),('rgly','N'))] = cmd.select('pro23', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+6.97,resSelectionSubs('gly','N',subs)))
IDSpec[(('pro','CB'),('rgly','O'))] = cmd.select('pro24', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+6.22,resSelectionSubs('gly','O',subs)))
IDSpec[(('pro','CD'),('rgly','CA'))] = cmd.select('pro25', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+4.94,resSelectionSubs('gly','CA',subs)))
IDSpec[(('pro','CD'),('rgly','N'))] = cmd.select('pro26', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+5.09,resSelectionSubs('gly','N',subs)))
IDSpec[(('pro','CD'),('rgly','O'))] = cmd.select('pro27', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+5.62,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('cys','CA'),('spro','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.83,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('spro','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.56,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('cys','CA'),('spro','CD'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.32,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('cys','CB'),('spro','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.90,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('spro','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.44,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('cys','CB'),('spro','CD'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.85,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('cys','SG'),('spro','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.51,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('spro','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.55,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('cys','SG'),('spro','CD'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.15,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('cys','CA'),('rcys_i','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.18,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CA'),('rcys_i','CB'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.55,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CA'),('rcys_i','SG'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.11,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CB'),('rcys_i','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.45,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CB'),('rcys_i','CB'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.65,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CB'),('rcys_i','SG'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.71,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','SG'),('rcys_i','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.79,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','SG'),('rcys_i','CB'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.50,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','SG'),('rcys_i','SG'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.31,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CA'),('rgly','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.43,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','CA'),('rgly','N'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.34,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','CA'),('rgly','O'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.07,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','CB'),('rgly','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.77,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','CB'),('rgly','N'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.30,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','CB'),('rgly','O'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.93,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','SG'),('rgly','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.73,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','SG'),('rgly','N'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.02,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','SG'),('rgly','O'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.23,resSelectionSubs('gly','O',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27')
IDSpec['r_cys'] = cmd.count_atoms(resSelectionSubs('cys', subs=subs, selection=True))
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
cmd.delete('cys19')
cmd.delete('cys20')
cmd.delete('cys21')
cmd.delete('cys22')
cmd.delete('cys23')
cmd.delete('cys24')
cmd.delete('cys25')
cmd.delete('cys26')
cmd.delete('cys27')
IDSpec[(('cys_i','CA'),('spro','CA'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.66,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('spro','CB'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.01,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('spro','CD'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.65,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('cys_i','CB'),('spro','CA'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.47,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('spro','CB'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.57,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('spro','CD'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.73,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('cys_i','SG'),('spro','CA'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.18,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('spro','CB'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.95,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('spro','CD'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.50,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.18,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.45,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.79,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.55,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.65,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.50,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.11,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.71,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.31,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('rgly','CA'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.80,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys_i','CA'),('rgly','N'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+4.43,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys_i','CA'),('rgly','O'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.07,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys_i','CB'),('rgly','CA'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.70,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys_i','CB'),('rgly','N'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.45,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys_i','CB'),('rgly','O'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.51,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys_i','SG'),('rgly','CA'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.52,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys_i','SG'),('rgly','N'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.57,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys_i','SG'),('rgly','O'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.07,resSelectionSubs('gly','O',subs)))
IDSpec['cys_i'] = cmd.select('cys_i',' br. cys_i1&br. cys_i2&br. cys_i3&br. cys_i4&br. cys_i5&br. cys_i6&br. cys_i7&br. cys_i8&br. cys_i9&br. cys_i10&br. cys_i11&br. cys_i12&br. cys_i13&br. cys_i14&br. cys_i15&br. cys_i16&br. cys_i17&br. cys_i18&br. cys_i19&br. cys_i20&br. cys_i21&br. cys_i22&br. cys_i23&br. cys_i24&br. cys_i25&br. cys_i26&br. cys_i27')
IDSpec['r_cys_i'] = cmd.count_atoms(resSelectionSubs('cys_i', subs=subs, selection=True))
cmd.delete('cys_i1')
cmd.delete('cys_i2')
cmd.delete('cys_i3')
cmd.delete('cys_i4')
cmd.delete('cys_i5')
cmd.delete('cys_i6')
cmd.delete('cys_i7')
cmd.delete('cys_i8')
cmd.delete('cys_i9')
cmd.delete('cys_i10')
cmd.delete('cys_i11')
cmd.delete('cys_i12')
cmd.delete('cys_i13')
cmd.delete('cys_i14')
cmd.delete('cys_i15')
cmd.delete('cys_i16')
cmd.delete('cys_i17')
cmd.delete('cys_i18')
cmd.delete('cys_i19')
cmd.delete('cys_i20')
cmd.delete('cys_i21')
cmd.delete('cys_i22')
cmd.delete('cys_i23')
cmd.delete('cys_i24')
cmd.delete('cys_i25')
cmd.delete('cys_i26')
cmd.delete('cys_i27')
IDSpec[(('gly','CA'),('spro','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.84,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('spro','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.75,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('spro','CD'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+4.94,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('gly','N'),('spro','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.35,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('gly','N'),('spro','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.97,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('gly','N'),('spro','CD'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.09,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('gly','O'),('spro','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.78,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('gly','O'),('spro','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.22,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('gly','O'),('spro','CD'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.62,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.43,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','CB'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.77,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','SG'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.73,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','N'),('scys','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.34,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','N'),('scys','CB'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.30,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','N'),('scys','SG'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.02,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','O'),('scys','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.07,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','O'),('scys','CB'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.93,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','O'),('scys','SG'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.23,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','CA'),('scys_i','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.80,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('scys_i','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.70,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('scys_i','SG'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.52,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('gly','N'),('scys_i','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+4.43,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('gly','N'),('scys_i','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.45,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('gly','N'),('scys_i','SG'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.57,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('gly','O'),('scys_i','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.07,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('gly','O'),('scys_i','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.51,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('gly','O'),('scys_i','SG'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.07,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
cmd.delete('gly19')
cmd.delete('gly20')
cmd.delete('gly21')
cmd.delete('gly22')
cmd.delete('gly23')
cmd.delete('gly24')
cmd.delete('gly25')
cmd.delete('gly26')
cmd.delete('gly27')
IDSpec['S_1tkd_2_7_7_7'] = cmd.select('S_1tkd_2_7_7_7', 'pro|cys|cys_i|gly')
cmd.delete('pro')
cmd.delete('cys')
cmd.delete('cys_i')
cmd.delete('gly')
