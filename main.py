from serial import Serial, PARITY_NONE, STOPBITS_ONE, EIGHTBITS


def main():
    port = input("serial port: ")
    serial = Serial(
        port=port,
        baudrate=115200,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        bytesize=EIGHTBITS,
        timeout=5.0,
    )

    while True:
        line = serial.readline()
        if line:
            print(line.decode("utf-8"))


if __name__ == "__main__":
    main()
