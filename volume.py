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
  print "Analyzing model ", sys.argv[1]
  print "Model volume is ", get_volume(sys.argv[1])
