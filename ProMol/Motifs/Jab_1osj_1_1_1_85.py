'''
FUNC:Jab_1osj_1_1_1_85
PDB:1osj
EC:1.1.1.85
RESI:lys,asp,tyr
LOCI:a-185,217;b-139;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. tyr'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. tyr'
jesstemp4 ='jessatom0 x. %s'%(1.541540+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
jesstemp6 ='r. lys'
jesstemp7 ='jessatom0 x. %s'%(9.909900+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,9.890110-(d*0.050000)))
jesstemp8 ='jessatom1 x. %s'%(10.050040+(d*0.050000))
jesstemp8 = '('+jesstemp8+') and not (jessatom1 x. %s)'%(max(0.05,10.029970-(d*0.050000)))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(9.909900+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,9.890110-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(10.050040+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,10.029970-(d*0.050000))))
jesstemp9 ='jessatom0 x. %s'%(8.738730+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom0 x. %s)'%(max(0.05,8.721279-(d*0.050000)))
jesstemp10 ='jessatom1 x. %s'%(8.878870+(d*0.050000))
jesstemp10 = '('+jesstemp10+') and not (jessatom1 x. %s)'%(max(0.05,8.861139-(d*0.050000)))
jesstemp11 ='jessatom2 x. %s'%(1.541540+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom2 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.738730+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,8.721279-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.878870+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,8.861139-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
jesstemp13 ='r. asp'
jesstemp14 ='r. glu'
jesstemp15 ='jessatom0 x. %s'%(13.623610+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom0 x. %s)'%(max(0.05,13.596404-(d*0.050000)))
jesstemp16 ='jessatom1 x. %s'%(12.952940+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom1 x. %s)'%(max(0.05,12.927073-(d*0.050000)))
jesstemp17 ='jessatom2 x. %s'%(8.068060+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom2 x. %s)'%(max(0.05,8.051948-(d*0.050000)))
jesstemp18 ='jessatom3 x. %s'%(7.827820+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom3 x. %s)'%(max(0.05,7.812188-(d*0.050000)))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp13+'))|(('+jesstemp0+')&('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(13.623610+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,13.596404-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(12.952940+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,12.927073-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.068060+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,8.051948-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(7.827820+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,7.812188-(d*0.050000))))
jesstemp19 ='jessatom0 x. %s'%(12.562550+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom0 x. %s)'%(max(0.05,12.537463-(d*0.050000)))
jesstemp20 ='jessatom1 x. %s'%(11.781770+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom1 x. %s)'%(max(0.05,11.758242-(d*0.050000)))
jesstemp21 ='jessatom2 x. %s'%(7.937930+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom2 x. %s)'%(max(0.05,7.922078-(d*0.050000)))
jesstemp22 ='jessatom3 x. %s'%(7.567560+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom3 x. %s)'%(max(0.05,7.552448-(d*0.050000)))
jesstemp23 ='jessatom4 x. %s'%(1.541540+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom4 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp13+'))|(('+jesstemp2+')&('+jesstemp14+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(12.562550+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,12.537463-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(11.781770+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,11.758242-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.937930+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,7.922078-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(7.567560+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,7.552448-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
cmd.select('Jab_1osj_1_1_1_85', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
