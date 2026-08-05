from config.gate.external.python.stdlib.csv.library import DEPENDENCY as CSV
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS

CSV.field_size_limit(SYS.maxsize)

DEPENDENCY = CSV.reader
