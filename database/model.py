from sqlalchemy import Column, Integer, Float, String, Boolean
from sqlalchemy.orm import declarative_base

base = declarative_base()

class CountryData(base):
    __tablename__ = 'country_data'

    id = Column(Integer, primary_key=True)
    Healthy_life_expectancy = Column(Float, nullable=False)
    Social_support = Column(Float, nullable=False)
    Economy = Column(Float, nullable=False)
    Generosity = Column(Float, nullable=False)
    Year = Column(Integer, nullable=False)
    Freedom_to_make_life_choices = Column(Float, nullable=False)
    Perceptions_of_corruption = Column(Float, nullable=False)
    Region_Central_and_Eastern_Europe = Column(Boolean, default=False)
    Region_Eastern_Asia= Column(Boolean, default=False)
    Region_Latin_America_and_Caribbean = Column(Boolean, default=False)
    Region_Middle_East_and_Northern_Africa = Column(Boolean, default=False)
    Region_North_America = Column(Boolean, default=False)
    Region_Southeastern_Asia = Column(Boolean, default=False)
    Region_Southern_Asia = Column(Boolean, default=False)
    Region_Sub_Saharan_Africa = Column(Boolean, default=False)
    Region_Western_Europe = Column(Boolean, default=False)
    score = Column(Float, nullable=False)
    score_predicted = Column(Float, nullable=False)

    def __str__(self):
        attributes = ", ".join(f"{key}={value}" for key, value in self.__dict__.items() if not key.startswith('_'))
        return f"CountryData({attributes})"