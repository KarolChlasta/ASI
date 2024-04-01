from pydantic import BaseModel

class Bank_Client(BaseModel):
  age: int
  job: str
  marital: str
  education: str
  default: str
  balance: int
  housing: str
  loan: str
  contact: str
  day_of_week: int
  month: str
  duration: int
  campaign: int
  pdays: int
  previous: int
  
