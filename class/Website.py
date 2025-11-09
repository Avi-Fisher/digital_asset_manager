from Digital_asset import Digital_asset
from Reportable import Reportable

class Website(Digital_asset,Reportable):

    def __init__(self,name,monthly_traffic:int,monetization_rate:float):

        super().__init__(name)
        self.__monthly_traffic = monthly_traffic
        self.__monetization_rate = monetization_rate

    def asset_type(self):
        return "WEBSITE"


    @property
    def get_monetization(self):
        return self.__monetization_rate



    def calculate_value(self):

        value = self.__monthly_traffic * self.__monetization_rate * 12
        return value


    def to_report_line(self):

        return f"Type: {self.asset_type()}, Name: {self.get_info_name}, Creat time: {self.get_info_date}, Cost: {self.get_info_cost}, Monetization: {self.get_monetization} ,Total value: {self.calculate_value()}"
















