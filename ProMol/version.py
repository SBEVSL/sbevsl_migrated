# CVS has support for a global revision number constant
# that will always evaluate to the revision number of the most
# recently modified file
# in each commit; however, SVN does not have such a function built in
# (it can only insert the revision number of the current file).
# I am moving away from version numbers because incrementing the x
# in 4.2.x for each commit as I had been doing through r159 (4.2.12)
# suddenly seemed like it was incrementing too far, too fast.
# I think maybe even the smallest increments of a
# three-part version number may be too big for individual commits.
# It might be better to assign version numbers when a version is
# ready for release.
# PLEASE try to keep this constant up to date with each commit!
VERSION = 'r192 (Development)'

# The following constant had been removed by Cyprian Corwin in
# revision 157.  It was restored in revision 160 at Alex's request.
# Before its removal, this line had been in promolglobals.py.
ALG_VERSION = '1.1' 
