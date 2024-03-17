# Slicer settings

## Start/End GCODE for OrcaSlicer

#### Start Print

```ini
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count]
M204 S[machine_max_acceleration_extruding] T[machine_max_acceleration_retracting]
START_PRINT BED_TEMP=[bed_temperature_initial_layer_single] EXTRUDER_TEMP=[nozzle_temperature_initial_layer]
```

#### End Print

```ini
END_PRINT {if max_layer_z < printable_height} LIFT_NOZZLE={z_offset+min(max_layer_z+10, printable_height)}{endif}
```

## Start/End GCODE for PrusaSlicer

#### Start Print

```ini
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count]
M204 S[machine_max_acceleration_extruding] T[machine_max_acceleration_retracting]
START_PRINT BED_TEMP=[first_layer_bed_temperature] EXTRUDER_TEMP=[first_layer_temperature]
```

#### End Print

```ini
END_PRINT {if max_layer_z < max_print_height} LIFT_NOZZLE={z_offset+min(max_layer_z+10, max_print_height)}{endif}
```

## Not Slicer-specific

#### Before Layer Change

```ini
;BEFORE_LAYER_CHANGE
G92 E0.0
;[layer_z]
```

#### (After) Layer Change

```ini
;AFTER_LAYER_CHANGE
;[layer_z]
SET_PRINT_STATS_INFO CURRENT_LAYER={layer_num + 1}
```
