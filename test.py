import sys
import pprint

admesh_lib_path = '/usr/local/lib'
if admesh_lib_path not in sys.path:
	sys.path.append(admesh_lib_path)
from admesh import Stl

errors = {
	'Error',
}

# Determines the feasibitily of an STL model
if len(sys.argv) < 1:
    print "Need at least a file name"
    exit(1)
stl = Stl(sys.argv[1])

# Although stl_repair provided a function that can repair errors in one shot,
# it does not give error messages. Here we report each steps.
tolerance = 0.0000001

pprint.pprint(stl.stats)
stl.check_facets_exact()
pprint.pprint(stl.stats)

stats = stl.stats
if stats['facets_w_1_bad_edge'] > 0 or stats['facets_w_2_bad_edge'] >0 or stats['facets_w_3_bad_edge'] > 0:
	print "Bad edges on facets"

shortest_edge = stats['shortest_edge']
if shortest_edge < tolerance:
	print "Edge too short, cannot print"

stl.repair()
pprint.pprint(stl.stats)
