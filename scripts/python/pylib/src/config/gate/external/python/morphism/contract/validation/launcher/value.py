from silmaril.sparky.morphism.contract.validation.application.apply import apply as APPLY
from silmaril.sparky.morphism.contract.validation.launcher.signature.value import Value as Launcher

VALUE: Launcher = lambda value: APPLY(value)
