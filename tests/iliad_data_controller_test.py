from data_controllers.iliad_data_controller import IliadDataController
import utils.packet_util as packet_util
import serial
import math

# TODO: Don't hardcode port values. Maybe make virtual linked ports?

def test_update():
    test = IliadDataController()
    config = {
        'port_name': 'COM2',
        'port_baud_rate': 9600,
        'port_stop_bits': serial.STOPBITS_ONE,
        'port_parity': serial.PARITY_NONE,
        'port_byte_size': serial.EIGHTBITS,
    }
    test.set_config(config)
    test.open()
    for i in range(1000):
        test.update()
    test.close()

def setup_packet_test() -> tuple[IliadDataController, serial.Serial]:
    """
    Utility function for packet tests.
    Starts and opens an IliadDataController instance.
    Opens a serial port.

    Both must be closed when finished.
    """
    # TODO: Rewrite as a context manager? The `with` syntax is perfect for opening/closing resources.
    test = IliadDataController()
    test.set_config({
        'port_name': 'COM2',
        'port_baud_rate': 9600,
        'port_stop_bits': serial.STOPBITS_ONE,
        'port_parity': serial.PARITY_NONE,
        'port_byte_size': serial.EIGHTBITS,
    })
    test.open()
    port = serial.Serial(
        port='COM1',
        baudrate=9600,
        stopbits=serial.STOPBITS_ONE,
        parity=serial.PARITY_NONE,
        bytesize=serial.EIGHTBITS,
    )
    return (test, port)

def test_arm_status_packet():
    (test, port) = setup_packet_test()
    port.write(packet_util.create_packet(packet_util.PACKET_TYPE_ARM_STATUS, 0.0, (True, True, True)))
    for i in range(100):
        test.update()
    assert test.arm_status_1_data == [(0.0, True)]
    assert test.arm_status_2_data == [(0.0, True)]
    assert test.arm_status_3_data == [(0.0, True)]
    test.close()
    port.close()
    
def test_altitude_packet():
    (test, port) = setup_packet_test()
    port.write(packet_util.create_packet(packet_util.PACKET_TYPE_ALTITUDE, 0.0, (1.234, 5.678)))
    for i in range(100):
        test.update()
    assert len(test.altitude_1_data) == 1
    assert len(test.altitude_2_data) == 1
    assert test.altitude_1_data[0][0] == 0.0
    assert test.altitude_2_data[0][0] == 0.0
    assert math.isclose(test.altitude_1_data[0][1], 1.234, rel_tol=1e-6) # TODO: Figure out specific tolerances.
    assert math.isclose(test.altitude_2_data[0][1], 5.678, rel_tol=1e-6)
    test.close()
    port.close()

def test_acceleration_packet():
    (test, port) = setup_packet_test()
    port.write(packet_util.create_packet(packet_util.PACKET_TYPE_ACCELERATION, 0.0, (1.234, 5.678, 9.012)))
    for i in range(100):
        test.update()
    assert len(test.acceleration_x_data) == 1
    assert len(test.acceleration_y_data) == 1
    assert len(test.acceleration_z_data) == 1
    assert test.acceleration_x_data[0][0] == 0.0
    assert test.acceleration_y_data[0][0] == 0.0
    assert test.acceleration_z_data[0][0] == 0.0
    assert math.isclose(test.acceleration_x_data[0][1], 1.234, rel_tol=1e-6)
    assert math.isclose(test.acceleration_y_data[0][1], 5.678, rel_tol=1e-6)
    assert math.isclose(test.acceleration_z_data[0][1], 9.012, rel_tol=1e-6)
    test.close()
    port.close()

def test_gps_coordinate_packet():
    (test, port) = setup_packet_test()
    port.write(packet_util.create_packet(packet_util.PACKET_TYPE_GPS_COORDINATES, 0.0, (1.234, 5.678)))
    for i in range(100):
        test.update()
    assert len(test.gps_latitude_data) == 1
    assert len(test.gps_longitude_data) == 1
    assert test.gps_latitude_data[0][0] == 0.0
    assert test.gps_longitude_data[0][0] == 0.0
    assert math.isclose(test.gps_latitude_data[0][1], 1.234, rel_tol=1e-6)
    assert math.isclose(test.gps_longitude_data[0][1], 5.678, rel_tol=1e-6)
    test.close()
    port.close()

def test_board_temperature_packet():
    (test, port) = setup_packet_test()
    port.write(packet_util.create_packet(packet_util.PACKET_TYPE_BOARD_TEMPERATURE, 0.0, (1.234, 5.678, 9.012, 3.456)))
    for i in range(100):
        test.update()
    assert len(test.board_1_temperature_data) == 1
    assert len(test.board_2_temperature_data) == 1
    assert len(test.board_3_temperature_data) == 1
    assert len(test.board_4_temperature_data) == 1
    assert test.board_1_temperature_data[0][0] == 0.0
    assert test.board_2_temperature_data[0][0] == 0.0
    assert test.board_3_temperature_data[0][0] == 0.0
    assert test.board_4_temperature_data[0][0] == 0.0
    assert math.isclose(test.board_1_temperature_data[0][1], 1.234, rel_tol=1e-6)
    assert math.isclose(test.board_2_temperature_data[0][1], 5.678, rel_tol=1e-6)
    assert math.isclose(test.board_3_temperature_data[0][1], 9.012, rel_tol=1e-6)
    assert math.isclose(test.board_4_temperature_data[0][1], 3.456, rel_tol=1e-6)
    test.close()
    port.close()
