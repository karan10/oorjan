1. reference data is of 2015
2. Api to store the data each hour - https://oorjanapp.herokuapp.com/api/solar_data/
    data = {"installation_key":"4bc157dc-bfd2-42c2-ba2e-f2d094386eb8","dc_power":250,"timestamp":"2017-02-18T23:00:00Z"}
3. File scheduled to send email report at 8pm everyday - 
    cron_jobs/daily_report.py
4. In email report entries marked with "*" are the hours where usage is less tha 80% of reference data
