## The oorjan Task

1. Api to store the data each hour - 
   * Api = *https://oorjanapp.herokuapp.com/api/solar_data/*
   * Data = {"installation_key":"4bc157dc-bfd2-42c2-ba2e-f2d094386eb8","dc_power":250,"timestamp":"2017-02-18T23:00:00Z"}
2. Otherwise we can update the whole day's data by running script - *cron_jobs/solar_data_upload.py*
3. File scheduled to send email report at 8pm everyday - 
    *cron_jobs/daily_report.py*
4. In email report entries marked with "*" are the hours where usage is less tha 80% of reference data.
5. Admin Panel Link [Herou Hosted Admin](https://oorjanapp.herokuapp.com/admin).
6. Heroku redis required to run scheduler.
