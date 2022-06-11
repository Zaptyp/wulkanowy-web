from pydantic import BaseModel
from typing import Optional

class StatsSubjectChartItem(BaseModel):
  grade: str
  quantity: str
  value: str

class StatsPartialChart(BaseModel):
  is_empty: bool
  average: Optional[str]
  items: Optional[list[StatsSubjectChartItem]]

class StatsPartialSubject(BaseModel):
  is_average: bool
  subject: str
  class_chart: StatsPartialChart
  student_chart: StatsPartialChart

class StatsPointsSubject(BaseModel):
  subject: str
  student_points: str
  class_points: str

class StatsFinalSubject(BaseModel):
  is_empty: bool
  subject: str
  chart: Optional[list[StatsSubjectChartItem]]
  student_grade: Optional[str]