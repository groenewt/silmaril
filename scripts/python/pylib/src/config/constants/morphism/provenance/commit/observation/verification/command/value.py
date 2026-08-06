VALUE = (
    "git",
    "-c",
    "gpg.program=gpg",
    "log",
    "--format=%H%x1f%G?%x1f%GK%x1f%GP%x1f%GF%x1f%s",
)
