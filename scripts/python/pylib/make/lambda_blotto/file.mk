LAMBDA_BLOTTO_FILE_OUTPUT ?= $(CURDIR)/build/lambda_blotto/file
LAMBDA_BLOTTO_FILE_PRE := $(LAMBDA_BLOTTO_FILE_OUTPUT)/metadata.pre
LAMBDA_BLOTTO_FILE_PAYLOAD := $(LAMBDA_BLOTTO_FILE_OUTPUT)/payload
LAMBDA_BLOTTO_FILE_POST := $(LAMBDA_BLOTTO_FILE_OUTPUT)/metadata.post
LAMBDA_BLOTTO_FILE_STABILITY := $(LAMBDA_BLOTTO_FILE_OUTPUT)/stability
LAMBDA_BLOTTO_FILE_BOUND := $(LAMBDA_BLOTTO_FILE_OUTPUT)/bound
LAMBDA_BLOTTO_FILE_EVIDENCE := $(LAMBDA_BLOTTO_FILE_OUTPUT)/evidence
LAMBDA_BLOTTO_FILE_RECEIPT := $(LAMBDA_BLOTTO_FILE_OUTPUT)/receipt.tar
LAMBDA_BLOTTO_FILE_DIGEST := $(LAMBDA_BLOTTO_FILE_OUTPUT)/receipt.sha256
LAMBDA_BLOTTO_FILE_READBACK := $(LAMBDA_BLOTTO_FILE_OUTPUT)/readback

.PHONY: lambda-blotto-file-capture
lambda-blotto-file-capture: $(LAMBDA_BLOTTO_FILE_READBACK)

$(LAMBDA_BLOTTO_FILE_OUTPUT):
	mkdir -p "$@"

$(LAMBDA_BLOTTO_FILE_PRE): | $(LAMBDA_BLOTTO_FILE_OUTPUT)
	stat --dereference --printf='%d\n%i\n%f\n%h\n%u\n%g\n%s\n%Y\n%Z\n' "$(LAMBDA_BLOTTO_FILE_SOURCE)" >"$@"

$(LAMBDA_BLOTTO_FILE_PAYLOAD): $(LAMBDA_BLOTTO_FILE_PRE)
	head --bytes="$(LAMBDA_BLOTTO_FILE_MAXIMUM_BYTES)" "$(LAMBDA_BLOTTO_FILE_SOURCE)" >"$@"

$(LAMBDA_BLOTTO_FILE_POST): $(LAMBDA_BLOTTO_FILE_PAYLOAD)
	stat --dereference --printf='%d\n%i\n%f\n%h\n%u\n%g\n%s\n%Y\n%Z\n' "$(LAMBDA_BLOTTO_FILE_SOURCE)" >"$@"

$(LAMBDA_BLOTTO_FILE_STABILITY): $(LAMBDA_BLOTTO_FILE_PRE) $(LAMBDA_BLOTTO_FILE_POST)
	cmp --silent "$(LAMBDA_BLOTTO_FILE_PRE)" "$(LAMBDA_BLOTTO_FILE_POST)" >"$@"

$(LAMBDA_BLOTTO_FILE_BOUND): $(LAMBDA_BLOTTO_FILE_PRE)
	awk -v maximum="$(LAMBDA_BLOTTO_FILE_MAXIMUM_BYTES)" 'NR == 7 && $$1 <= maximum { accepted = 1 } END { if (!accepted) { print "file_capture_maximum_bytes_exceeded" > "/dev/stderr"; exit 65 } }' "$<" >"$@"

$(LAMBDA_BLOTTO_FILE_EVIDENCE): | $(LAMBDA_BLOTTO_FILE_OUTPUT)
	awk -v evidence="$(LAMBDA_BLOTTO_EVIDENCE_CLASS)" 'BEGIN { if (evidence != "observed") { print "non_observed_file_capture_rejected" > "/dev/stderr"; exit 65 } }' >"$@"

$(LAMBDA_BLOTTO_FILE_RECEIPT): $(LAMBDA_BLOTTO_FILE_PAYLOAD) $(LAMBDA_BLOTTO_FILE_POST) $(LAMBDA_BLOTTO_FILE_STABILITY) $(LAMBDA_BLOTTO_FILE_BOUND) $(LAMBDA_BLOTTO_FILE_EVIDENCE)
	tar --format=posix --create --file="$@" --directory="$(LAMBDA_BLOTTO_FILE_OUTPUT)" metadata.pre metadata.post payload stability bound evidence --directory="$(CURDIR)" phoenix-disintegration-routing.json federated-computing-substrate-routing.json

$(LAMBDA_BLOTTO_FILE_DIGEST): $(LAMBDA_BLOTTO_FILE_RECEIPT)
	sha256sum "$<" >"$@"

$(LAMBDA_BLOTTO_FILE_READBACK): $(LAMBDA_BLOTTO_FILE_DIGEST)
	sha256sum --check "$<" >"$@"
