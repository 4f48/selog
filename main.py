from serial import Serial, PARITY_NONE, STOPBITS_ONE, EIGHTBITS, SerialException
from time import sleep
import logging
from logging.handlers import RotatingFileHandler


def main():
    fname = input("output file: ")
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s]%(levelname)s>%(message)s",
        handlers=[
            RotatingFileHandler(fname, maxBytes=30 * 1024 * 1024, backupCount=5),
            logging.StreamHandler(),
        ],
    )

    port = input("serial port: ")

    serial = None
    while True:
        try:
            if serial is None or not serial.is_open:
                serial = Serial(
                    port=port,
                    baudrate=115200,
                    parity=PARITY_NONE,
                    stopbits=STOPBITS_ONE,
                    bytesize=EIGHTBITS,
                    timeout=5.0,
                )
                logging.debug(f"connected to {port}")

            line = serial.readline()
            if line:
                try:
                    logging.info(line.decode("utf-8").rstrip())
                except UnicodeDecodeError as e:
                    logging.warning(f"failed to decode: {e}, raw: {line}")

        except (SerialException, OSError) as e:
            logging.error(f"connection failed: {e}")
            if serial is not None:
                try:
                    serial.close()
                except SerialException:
                    pass
                serial = None
            sleep(2.0)

        except KeyboardInterrupt:
            if serial is not None:
                try:
                    serial.close()
                except SerialException:
                    pass
            break


if __name__ == "__main__":
    main()
