from config.constants.morphism.codebase.volume.executable.perl.value import VALUE as PERL


VALUE = (PERL, "-MDigest::SHA=sha256_hex", "-0777", "-ne", "print sha256_hex($_)")
