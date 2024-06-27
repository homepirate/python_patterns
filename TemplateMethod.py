from abc import ABCMeta, abstractmethod


class Transmitter(metaclass=ABCMeta):
    def voice_record(self):
        print("Record voice")

    def _simpling(self):
        pass

    def _digitization(self):
        pass

    @abstractmethod
    def _modulation(self):
        pass

    def _transmission(self):
        print("Signal transmission by channel")

    def process_start(self):
        self.voice_record()
        self._simpling()
        self._digitization()
        self._modulation()
        self._transmission()


class AnalogTransmitter(Transmitter):
    def _modulation(self):
        print("Modulation analog signal")


class DigitTransmitter(Transmitter):
    def _digitization(self):
        print("Digitization digit signal")

    def _simpling(self):
        print("Simpling digit signal")

    def _modulation(self):
        print("Modulation digit signal")


def main():
    a = AnalogTransmitter()
    a.process_start()

    print()
    d = DigitTransmitter()
    d.process_start()


if __name__ == '__main__':
    main()
