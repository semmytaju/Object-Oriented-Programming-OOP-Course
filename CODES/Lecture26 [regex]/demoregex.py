import re

input_text = "Hallo students, email berikut (semmy@gmail.com, jian@yahoo.com, budi@start.com, tommy23@unklab.co.id) adalah student yang belum tuntas class ini. Diharapkan agar dapat memasukan tugas pada 22 Juni 2024, jam 2 PM. Thank you :)"

# Regex pattern for email
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Regex pattern for date
date_pattern = r'\b(?:[0-9]|[12][0-9]|3[01])\s(?:Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)\s\d{4}\b'

# Regex pattern for time
time_pattern = r'\b(?:[1-9]|1[0-2])\s(?:AM|PM)\b'

# Extract emails
emails = re.findall(email_pattern, input_text)

# Extract date
date = re.search(date_pattern, input_text).group()

# Extract time
time = re.search(time_pattern, input_text).group()

# Print the outputs
for email in emails:
    print(email)
    
print(date)
print(time)


