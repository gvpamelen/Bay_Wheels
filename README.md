covid19
==============================

**Objective:** Business Analysis of Bay Wheels trips (Lyft's bikes) in Jan-20. 

**General process:** 
Bay Wheels shares [monthly logs of bike anonimised bike usage](https://www.lyft.com/bikes/bay-wheels/system-data). We download the data from Jan 2020, clean it and perform an extensive EDA. We create a report (pdf), where we use extensive (automated) formatting on selected plot from this EDA to get them ready for use in high-end powerpoint reports. The latter outlines a method to automated certain powerpoint reports, in cases where (business requirements) prefer static reports over dashboards.

![](images/screenshot.png)


Recommended setup
------------
To get the best experience viewing the jupyter notebooks, we advice to use jupyterlabs, with the *table-of-contents* (toc) extension. 



Project Organization
------------

    ├── README.md          
    ├── data                 <- All data-files, raw & various stages of processing.
    │
    ├── notebooks            <- notebooks to process data, perform the EDA and generate the report
    │
    ├── requirements.txt     <- The requirements file for reproducing the analysis environment, e.g.
    │                           generated with `pip freeze > requirements.txt`
    │
    ├── src                  <- Source code for use in this project.
    │
    └── Lyft_Bay_Wheels.pdf  <- final report


--------
