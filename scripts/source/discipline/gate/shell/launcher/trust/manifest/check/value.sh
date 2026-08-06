#!/usr/bin/env bash
readonly script__input_type='silmaril.config.gates.Source.Physical.Coordinate.Text.Read.Input.Value'
readonly script__frame_type='silmaril.config.gates.Source.Discipline.Trust.Manifest.Check.Frame.Value'
readonly script__operation_type='silmaril.config.gates.Source.Discipline.Shell.Launcher.Trust.Manifest.Check.Operation.Value'
readonly script__binding_type='silmaril.config.gates.Source.Discipline.Contract.Gate.Path.Locator.Runtime.Shoe.Spelling.Schema.Binding.Admission.Provisional.Value'
make -C "$1" morphism-provenance-trust-manifest-check
