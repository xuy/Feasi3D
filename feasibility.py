from admesh import Stl
import sys
import pprint

errors = {
	'Error',
}

def get_volume(stlfile):
  stl = Stl(stlfile)
  stl.check_facets_exact()
  stl.repair()
  return stl.stats['volume']

if __name__ == '__main__':
  # Determines the feasibitily of an STL model

  if len(sys.argv) < 1:
    print "Need at least a file name"
    exit(1)
  print "=" * 80
  print "Analyzing model ", sys.argv[1]
  stl = Stl(sys.argv[1])

  # Although stl_repair provided a function that can repair errors in one shot,
  # it does not give error messages. Here we report each steps.
  tolerance = 0.0000001

  stl.check_facets_exact()

  stats = stl.stats
  if stats['facets_w_1_bad_edge'] > 0 or stats['facets_w_2_bad_edge'] >0 or stats['facets_w_3_bad_edge'] > 0:
    print "Bad edges on facets"

  shortest_edge = stats['shortest_edge']
  if shortest_edge < tolerance:
    print "Edge too short, cannot print"

  stl.repair(fill_holes_flag = True, iterations = 4)
  print sys.argv
  if len(sys.argv) == 3:
    stl.write_binary(sys.argv[2]) 
  # pprint.pprint(stl.stats)
  print
