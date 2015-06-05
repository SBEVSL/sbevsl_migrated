'''
FUNC:Jab_1aj0
PDB:1aj0
EC:2.5.1.15
PFAM:PF00809
RESI:asn,arg,arg
LOCI:a-22,63,255;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. asn'
jesstemp2 ='r. gln'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='r. arg'
jesstemp7 ='jessatom0 x. %s'%(12.049300+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(10.726200+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(12.049300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(10.726200+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(11.453400+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(10.039400+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.453400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(10.039400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(12.544200+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(12.402800+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(15.513600+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(15.442900+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.544200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(12.402800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(15.513600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(15.442900+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(11.887700+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(11.705900+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(14.362200+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(14.392500+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.887700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(11.705900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(14.362200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(14.392500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1aj0', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
