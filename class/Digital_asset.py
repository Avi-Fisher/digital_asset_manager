import datetime
from abc import ABC, abstractmethod


class Digital_asset(ABC):

    def __init__(self,name:str):

        self.__name = name
        self.__registration_date = datetime.datetime.now().isoformat()
        self.__cost = 100


    @property
    def get_info_name(self):
        print(f"Name: {self.__name}")

    @property
    def get_info_date(self):
        print(f"Creat: {self.__registration_date}")

    @property
    def get_info_cost(self):
        print(f"Cost: {self.__cost}")


    @abstractmethod
    def calculate_value(self):
        return float

    @abstractmethod
    def asset_type(self):
        return str