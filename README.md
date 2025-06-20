# ✨ 2nd Project of Advanced Level Dicoding DS: Student Status Analysis of JAYA JAYA INSTITUTE ✨

## Business Understanding
---
Jaya Jaya Maju is a tertiary education institution that has been operating since the year 2000, having over 4000 students across the country.

Despite its significant growth and scale, the institute continues to face challenges in managing its students. As a result, it is experiencing a high dropout rate, exceeding 10%, indicating a considerable number of students that are unable to graduate of finishing the study.

This will make the institute quality questioned if this issue still persist. Due to this matter, Jaya Jaya Institute willing to detect which student that will likely be dropout or graduate based on quality performance and other factors.

---
### Bussiness Problems
---
1. Student Dropout Rates
2. No Dependable Monitoring Tools for Performance Analysis 
3. Absence of Early Warning Systems for Predicting At-Risk Students

### Project Scope
1. Analysis of occuring dropout
2. Monitoring dashboard for students of Jaya Jaya Institute
3. Model development for student status prediction based on existing factors

### Preparation
---
Data source: [Jaya Jaya Institute Student Data] (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

---

# Accessing notebook.ipynb
---
```
open terminal
python3 -m env env
source bin env/bin/activate
```
```
pip install -r requirements.txt
```
```
jupyther notebook or code .. #forVSCode
```

# Accessing Monitoring Dashboard
---
Tools used in this project is metabase with docker as container. 

```
docker pull metabase/metabase:v0.54.3
```

```
docker run -p 3000:3000 --name metabase
```

```
username: root@mail.com
password: root123
```

This dashboard contains dropout rate, total students and breakdown types that potray students demography. Comparison also done based on the demography, possible factors affecting dropout and situation of active students. Through this initiatives, Lecturers would be able to gather insights as this could also be used for report that flexibly seen by higher level management or requested by parents if incase needed. 


## Accessing Machine Learning System
---
```
open terminal
python3 -m env env
source bin env/bin/activate
```
```
streamlit run app.py
```
```
then fill the columns based on options given, and then click predict. 
```
```
to try with link, access [this] (https://jayastudentpredict.streamlit.app/)
```
## Conclusion
---


### Action Recommendations
--
-
-
