from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    def __init__(self):
        self._traffic_light: 'TrafficLight' = None

    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def previous_state(self):
        pass


class TrafficLight:
    def __init__(self, st: State):
        self.__state = None
        self.set_state(st)

    def set_state(self, st: State):
        self.__state = st
        self.__state._traffic_light: 'TrafficLight' = self

    def next_state(self):
        self.__state.next_state()

    def previous_state(self):
        self.__state.previous_state()


class GreenState(State):
    def next_state(self):
        print("From Green To Yellow")
        self._traffic_light.set_state(YellowState())

    def previous_state(self):
        print("Green")


class YellowState(State):
    def next_state(self):
        print("From Yellow To Red")
        self._traffic_light.set_state(RedState())

    def previous_state(self):
        print("From Yellow To Green")
        self._traffic_light.set_state(GreenState())


class RedState(State):
    def next_state(self):
        print("Red")

    def previous_state(self):
        print("From Red To Yellow")
        self._traffic_light.set_state(YellowState())


def main():
     traffic_light = TrafficLight(YellowState())

     traffic_light.next_state()
     traffic_light.next_state()

     traffic_light.previous_state()
     traffic_light.previous_state()
     traffic_light.previous_state()


if __name__ == '__main__':
    main()
