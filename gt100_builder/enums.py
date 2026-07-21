"""Auto-generated numeric selectors observed in the canonical GT-100 library."""
from enum import IntEnum

class Fx1AcProcessorType(IntEnum):
    VALUE_1 = 1

class Fx1PhaserType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class Fx1RotarySpeedSelect(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx1PanType(IntEnum):
    VALUE_0 = 0

class Fx1RingModMode(IntEnum):
    VALUE_0 = 0

class Fx1HumanizerMode(IntEnum):
    VALUE_1 = 1

class Fx1SubDelayType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2FxType(IntEnum):
    VALUE_0 = 0
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_27 = 27
    VALUE_30 = 30

class OutputSelect(IntEnum):
    VALUE_0 = 0

class Fx2SubOdDsSoloSw(IntEnum):
    VALUE_0 = 0

class CompType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_7 = 7

class Fx2SubOdDsType(IntEnum):
    VALUE_6 = 6
    VALUE_11 = 11

class CompOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2TWahMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class OdDsSoloSw(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2PanType(IntEnum):
    VALUE_0 = 0

class OdDsOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2AutoWahMode(IntEnum):
    VALUE_1 = 1

class PreampAOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class OdDsCustomType(IntEnum):
    VALUE_0 = 0

class PreampType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24

# Factory-library friendly aliases used by the high-level recipe API.
PreampType.NATURAL_CLEAN = PreampType.VALUE_0
CompType.BASS_COMP = CompType.VALUE_2

class OdDsType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19

class Fx2SubWahType(IntEnum):
    VALUE_0 = 0

class Fx2RingModMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2AdvCompType(IntEnum):
    VALUE_0 = 0
    VALUE_3 = 3

class Fx2HumanizerMode(IntEnum):
    VALUE_1 = 1

class PreampAGainSw(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class PreampASoloSw(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class PreampASpType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_7 = 7

class PreampAMicType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class Fx2LimiterType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2SubDelayType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class DelayOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class PreampACustomType(IntEnum):
    VALUE_0 = 0

class DelayType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9

class PreampBOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class ChorusOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class ChorusMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class ReverbOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class ReverbType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class PreampBGainSw(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class Fx2GuitarSimType(IntEnum):
    VALUE_0 = 0
    VALUE_3 = 3

class PreampBSpType(IntEnum):
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_7 = 7
    VALUE_8 = 8

class PedalFxOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class PedalFxWahType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_5 = 5

class Fx2ToneModifyType(IntEnum):
    VALUE_0 = 0
    VALUE_5 = 5
    VALUE_7 = 7

class PreampBSoloSw(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class DividerMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class DividerChSelect(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class PreampBMicType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class PreampBCustomType(IntEnum):
    VALUE_0 = 0

class MixerMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class SendReturnOnOff(IntEnum):
    VALUE_0 = 0

class SendReturnMode(IntEnum):
    VALUE_0 = 0

class Ns1OnOff(IntEnum):
    VALUE_1 = 1

class Ns2OnOff(IntEnum):
    VALUE_1 = 1

class AccelFxType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class EqOnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class AccelFxFeedbackerMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx1OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx1FxType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_29 = 29
    VALUE_30 = 30

class Fx1SubOdDsType(IntEnum):
    VALUE_0 = 0
    VALUE_6 = 6
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_18 = 18
    VALUE_19 = 19

class Fx1TWahMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx1SubOdDsSoloSw(IntEnum):
    VALUE_0 = 0

class Fx1AutoWahMode(IntEnum):
    VALUE_1 = 1

class Fx1SubWahType(IntEnum):
    VALUE_0 = 0

class Fx1AdvCompType(IntEnum):
    VALUE_0 = 0

class Fx1LimiterType(IntEnum):
    VALUE_0 = 0

class CtlExpAccelCtlSrcMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class CtlExpExpSwSrcMode(IntEnum):
    VALUE_1 = 1

class Fx2AcProcessorType(IntEnum):
    VALUE_1 = 1

class CtlExpSubCtl1SrcMode(IntEnum):
    VALUE_1 = 1

class CtlExpSubCtl2SrcMode(IntEnum):
    VALUE_1 = 1

class Fx1ToneModifyType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_7 = 7

class Fx1GuitarSimType(IntEnum):
    VALUE_0 = 0
    VALUE_5 = 5
    VALUE_7 = 7

class Assign1OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign1SourceMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2PhaserType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class Assign2OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Fx2RotarySpeedSelect(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign2SourceMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign3OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign3SourceMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign8SourceMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign4OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class PrmFx2TeraechoMode(IntEnum):
    VALUE_1 = 1

class Assign4SourceMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign5OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign5SourceMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign6OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign6SourceMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign7OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class Assign7SourceMode(IntEnum):
    VALUE_1 = 1

class Assign8OnOff(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

PARAMETER_ENUMS = {
    "fx1_ac_processor_type": Fx1AcProcessorType,
    "fx1_phaser_type": Fx1PhaserType,
    "fx1_rotary_speed_select": Fx1RotarySpeedSelect,
    "fx1_pan_type": Fx1PanType,
    "fx1_ring_mod_mode": Fx1RingModMode,
    "fx1_humanizer_mode": Fx1HumanizerMode,
    "fx1_sub_delay_type": Fx1SubDelayType,
    "fx2_on_off": Fx2OnOff,
    "fx2_fx_type": Fx2FxType,
    "output_select": OutputSelect,
    "fx2_sub_od_ds_solo_sw": Fx2SubOdDsSoloSw,
    "comp_type": CompType,
    "fx2_sub_od_ds_type": Fx2SubOdDsType,
    "comp_on_off": CompOnOff,
    "fx2_t_wah_mode": Fx2TWahMode,
    "od_ds_solo_sw": OdDsSoloSw,
    "fx2_pan_type": Fx2PanType,
    "od_ds_on_off": OdDsOnOff,
    "fx2_auto_wah_mode": Fx2AutoWahMode,
    "preamp_a_on_off": PreampAOnOff,
    "od_ds_custom_type": OdDsCustomType,
    "preamp_a_type": PreampType,
    "od_ds_type": OdDsType,
    "fx2_sub_wah_type": Fx2SubWahType,
    "fx2_ring_mod_mode": Fx2RingModMode,
    "fx2_adv_comp_type": Fx2AdvCompType,
    "fx2_humanizer_mode": Fx2HumanizerMode,
    "preamp_a_gain_sw": PreampAGainSw,
    "preamp_a_solo_sw": PreampASoloSw,
    "preamp_a_sp_type": PreampASpType,
    "preamp_a_mic_type": PreampAMicType,
    "fx2_limiter_type": Fx2LimiterType,
    "fx2_sub_delay_type": Fx2SubDelayType,
    "delay_on_off": DelayOnOff,
    "preamp_a_custom_type": PreampACustomType,
    "delay_type": DelayType,
    "preamp_b_on_off": PreampBOnOff,
    "preamp_b_type": PreampType,
    "chorus_on_off": ChorusOnOff,
    "chorus_mode": ChorusMode,
    "reverb_on_off": ReverbOnOff,
    "reverb_type": ReverbType,
    "preamp_b_gain_sw": PreampBGainSw,
    "fx2_guitar_sim_type": Fx2GuitarSimType,
    "preamp_b_sp_type": PreampBSpType,
    "pedal_fx_on_off": PedalFxOnOff,
    "pedal_fx_wah_type": PedalFxWahType,
    "fx2_tone_modify_type": Fx2ToneModifyType,
    "preamp_b_solo_sw": PreampBSoloSw,
    "divider_mode": DividerMode,
    "divider_ch_select": DividerChSelect,
    "preamp_b_mic_type": PreampBMicType,
    "preamp_b_custom_type": PreampBCustomType,
    "mixer_mode": MixerMode,
    "send_return_on_off": SendReturnOnOff,
    "send_return_mode": SendReturnMode,
    "ns1_on_off": Ns1OnOff,
    "ns2_on_off": Ns2OnOff,
    "accel_fx_type": AccelFxType,
    "eq_on_off": EqOnOff,
    "accel_fx_feedbacker_mode": AccelFxFeedbackerMode,
    "fx1_on_off": Fx1OnOff,
    "fx1_fx_type": Fx1FxType,
    "fx1_sub_od_ds_type": Fx1SubOdDsType,
    "fx1_t_wah_mode": Fx1TWahMode,
    "fx1_sub_od_ds_solo_sw": Fx1SubOdDsSoloSw,
    "fx1_auto_wah_mode": Fx1AutoWahMode,
    "fx1_sub_wah_type": Fx1SubWahType,
    "fx1_adv_comp_type": Fx1AdvCompType,
    "fx1_limiter_type": Fx1LimiterType,
    "ctl_exp_accel_ctl_src_mode": CtlExpAccelCtlSrcMode,
    "ctl_exp_exp_sw_src_mode": CtlExpExpSwSrcMode,
    "fx2_ac_processor_type": Fx2AcProcessorType,
    "ctl_exp_sub_ctl1_src_mode": CtlExpSubCtl1SrcMode,
    "ctl_exp_sub_ctl2_src_mode": CtlExpSubCtl2SrcMode,
    "fx1_tone_modify_type": Fx1ToneModifyType,
    "fx1_guitar_sim_type": Fx1GuitarSimType,
    "assign1_on_off": Assign1OnOff,
    "assign1_source_mode": Assign1SourceMode,
    "fx2_phaser_type": Fx2PhaserType,
    "assign2_on_off": Assign2OnOff,
    "fx2_rotary_speed_select": Fx2RotarySpeedSelect,
    "assign2_source_mode": Assign2SourceMode,
    "assign3_on_off": Assign3OnOff,
    "assign3_source_mode": Assign3SourceMode,
    "assign8_source_mode": Assign8SourceMode,
    "assign4_on_off": Assign4OnOff,
    "prm_fx2_teraecho_mode": PrmFx2TeraechoMode,
    "assign4_source_mode": Assign4SourceMode,
    "assign5_on_off": Assign5OnOff,
    "assign5_source_mode": Assign5SourceMode,
    "assign6_on_off": Assign6OnOff,
    "assign6_source_mode": Assign6SourceMode,
    "assign7_on_off": Assign7OnOff,
    "assign7_source_mode": Assign7SourceMode,
    "assign8_on_off": Assign8OnOff,
}
