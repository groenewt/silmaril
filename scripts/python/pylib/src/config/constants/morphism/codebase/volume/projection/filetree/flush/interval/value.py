# rationale: 1 fires UNWIND after every sibling node.  The save-stack leak is
# per-shipped-page (~1.3 entries/page) inside any open scope chain; sibling
# counts almost never reach 10000, so the prior value left the valve dead and
# scopes accumulated ~200k entries by 21% of the volume-40 file tree (LuaTeX
# hard-clamps save_size at 500000).  Cycling at every sibling bounds live
# entries to one node's page span, independent of corpus size.
VALUE = 1
