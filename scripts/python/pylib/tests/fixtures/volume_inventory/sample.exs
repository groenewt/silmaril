defmodule Mix.Tasks.Volume.Sample do
  use Mix.Task
  alias Telephone.Producer

  def run(_arguments), do: Producer.emit(:hook_volume_sample)
end

# mix volume.sample
# make build
# L0 L1 L2 L3 L3.5 Dunbar TrustGate ring_pool
