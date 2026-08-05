# The chapter boundary emitted by every projection fragment.  It is
# \silChapter and NOT \chapter: every volume in this corpus is typeset through
# one shared preamble whose document class is `article`
# (final/working/src/shared/preamble.tex line 2), and `article` defines no
# \chapter at all -- the fragments would abort with `Undefined control
# sequence` the moment they were read.  The shared preamble supplies
# \silChapter (\clearpage\section) in
# src/shared/components/layout/sectioning.tex precisely as "one consolidated
# chapter boundary for every article-class volume"; 766 authored call sites
# across 402 files already use it.  It is a SHARED command, so emitting it
# introduces no volume-local control sequence, which Volume 40's paper.tex
# forbids by invariant.
VALUE = "\\silChapter{%s}\n"
