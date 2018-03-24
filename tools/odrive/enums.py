
# TODO: transmit enums over protocol

AXIS_STATE_UNDEFINED = 0
AXIS_STATE_IDLE = 1
AXIS_STATE_STARTUP_SEQUENCE = 2
AXIS_STATE_FULL_CALIBRATION_SEQUENCE = 3
AXIS_STATE_MOTOR_CALIBRATION = 4
AXIS_STATE_SENSORLESS_CONTROL = 5
AXIS_STATE_ENCODER_INDEX_SEARCH = 6
AXIS_STATE_ENCODER_OFFSET_CALIBRATION = 7
AXIS_STATE_CLOSED_LOOP_CONTROL = 8

AXIS_ERROR_NO_ERROR = 0
AXIS_ERROR_INVALID_STATE = 1
AXIS_ERROR_DC_BUS_UNDER_VOLTAGE = 2
AXIS_ERROR_DC_BUS_OVER_VOLTAGE = 3
AXIS_ERROR_CURRENT_MEASUREMENT_TIMEOUT = 4
AXIS_ERROR_CONTROL_LOOP_TIMEOUT = 5
AXIS_ERROR_MOTOR_FAILED = 6
AXIS_ERROR_SENSORLESS_ESTIMATOR_FAILED = 7
AXIS_ERROR_ENCODER_FAILED = 8
AXIS_ERROR_CONTROLLER_FAILED = 9
AXIS_ERROR_POS_CTRL_DURING_SENSORLESS = 10
