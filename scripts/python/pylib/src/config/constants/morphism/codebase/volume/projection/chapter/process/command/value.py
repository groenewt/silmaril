from config.constants.morphism.codebase.volume.executable.perl.value import VALUE as PERL


VALUE = (
    PERL,
    "-e",
    r'''binmode STDIN; binmode STDOUT; print "\\chapter{$ARGV[0]}\n" or die "write: $!"; while (1) { my $count = sysread(STDIN, my $chunk, 65536); die "read: $!" unless defined $count; last if $count == 0; print STDOUT $chunk or die "write: $!"; } print "\n" or die "write: $!";''',
)
