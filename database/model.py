from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class CountryData(base):
    __tablename__ = 'country_data'

    id = Column(Integer, primary_key=True)
    healthy_life_expectancy = Column(Float, nullable=False)
    social_support = Column(Float, nullable=False)
    country = Column(String, nullable=False)
    economy = Column(Float, nullable=False)
    generosity = Column(Float, nullable=False)
    year = Column(Integer, nullable=False)
    freedom_to_make_life_choices = Column(Float, nullable=False)
    region = Column(String, nullable=False)
    perceptions_of_corruption = Column(Float, nullable=False)
    score = Column(Float, nullable=False)
    score_predicted = Column(Float, nullable=False)

    def __str__(self):
        attributes = ", ".join(f"{key}={value}" for key, value in self.__dict__.items() if not key.startswith('_'))
        return f"CountryData({attributes})"