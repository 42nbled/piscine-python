from datetime import datetime
import time

timestamp = time.time()

formatted_number = '{:,.4f}'.format(timestamp)
scientific_formatted_number = '{:.2e}'.format(timestamp)

print("Seconds since January 1, 1970:", formatted_number, "or", scientific_formatted_number, "in scientific notation")

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%b %d %Y")

print(formatted_date)
