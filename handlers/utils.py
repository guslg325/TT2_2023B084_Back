from datetime import datetime, timezone
from zoneinfo import ZoneInfo
def to_mx_timezone(date = ""):
  dt = datetime.fromisoformat(date)
  dt = dt.replace(tzinfo=timezone.utc)
  mx_timezone = ZoneInfo("America/Mexico_City")
  return str(dt.astimezone(mx_timezone))