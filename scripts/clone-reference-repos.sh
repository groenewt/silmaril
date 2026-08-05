#!/usr/bin/env bash
# Best-effort scheduler-folklore reference clones. Network-optional.
set -uo pipefail
cd "$(dirname "$0")/.."
mkdir -p references
if [ ! -d references/spark ]; then
  git clone --filter=blob:none --sparse https://github.com/apache/spark.git references/spark \
  && git -C references/spark sparse-checkout set \
       core/src/main/scala/org/apache/spark/scheduler \
       core/src/main/scala/org/apache/spark/rdd \
       core/src/main/scala/org/apache/spark/Dependency.scala \
       graphx/src/main/scala/org/apache/spark/graphx \
  || echo "warn: spark reference clone failed (offline?)" >&2
fi
if [ ! -d references/scala3 ]; then
  git clone --filter=blob:none https://github.com/scala/scala3.git references/scala3 \
  || echo "warn: scala3 reference clone failed (offline?)" >&2
fi
echo "reference clones done (best effort)"
