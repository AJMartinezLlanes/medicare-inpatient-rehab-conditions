# Conditions
This repository contains all deliverables for personal project including additional files used 
in the process of producing the final deliverables.

**Repository Format**
<details>
<summary>Click to expand</summary>

- README.md: Contains a full outline of the project, information regarding the format of the repository, and instructions for reproducing the results.
- final.py: Contains all the functions used on final report notebook.
- wrangle.py: Contains convenience functions that can be used to both acquire and prepare the data in one step.
- final_report.ipynb: The final report containing an outline of all steps taken, with results, and extraneous details removed.
- wrangle.ipynb: Contains all the steps taken in the acquisition and preparation phases of the pipeline.
- explore.ipynb: Contains all the steps taken in the exploratory analysis phase of the pipeline.
- model.ipynb: Contains all the steps taken in the modeling phase of the pipeline.

</details>

___

## Table of Contents

1. [Project Summary](#project-summary)
2. [Project Goals](#project-goals)
3. [Project Description](#project-description)
4. [Initial Questions](#initial-questions)
5. [Data Dictionary](#data-dictionary)
6. [Recreate This Project](#instructions-for-recreating-this-project)
7. [Outline of Project Plan](#outline-of-project-plan)
    1. [Data Acquisition](#data-acquisition)
    2. [Data Preparation](#data-preparation)
    3. [Exploratory Analysis](#exploratory-analysis)
    4. [Modeling](#modeling)
8. [Conclusion](#conclusion)

___

## Project Summary

We conducted analysis on 2021 medicare data 

___

## Project Goals

Given 2021 rehab facility conditions data, identify what condidition has the most occurrences. This information will affect new training, safety rules and procedures.

___

## Project Description

Medicare wants to know what can we find from 2021 inpatient rehabilitation information. Simple question as to what was the leading condition, what state has the highest and lowest of it. This study will help on mandatory training decision, implementation of safety rules and procedures.

___

## Initial Questions

- What is the most occurring condition?
- What state has the highest number of it? What city?
- Which states has the lowest number of it? What city?
- What about region?
- Is there a relationship between city and condition?
- Is there a relationship between state and condition?
- Is there a relationship between region and condition?
___

## Data Dictionary

<details><summary>Click to expand</summary>

| Variable              | Meaning      |
| --------------------- | ------------ |
| ccn                   | The CCN is used to identify the facility listed.|
| facility_name         | Facility name |
| address               | Facility address |
| state                 | Facility state |
| zip_code              | Two-character postal code where the facility is located |
| county_name           | Facility county |
| phone_number          | Facility ten digit telephone number |
| cms_region            | The CMS region where the facility is located. Below is a key to the location of the regional offices and the states covered by each CMS region:<p> <p>1 = Boston: <p>Connecticut, Maine, Massachusetts, New   Hampshire, Rhode Island, Vermont <p>2 = New York: <p>New Jersey, New York, Puerto Rico, Virgin Islands <p>3 = Philadelphia: <p>Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia <p>4 = Atlanta: <p>Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee <p>5 = Chicago: <p>Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin <p>6 = Dallas: <p>Arkansas, Louisiana, New Mexico, Oklahoma, Texas <p>7 = Kansas City: <p>Iowa, Kansas, Missouri, Nebraska <p>8 = Denver: <p>Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming <p>9 = San Francisco: <p>Arizona, California, Hawaii, Nevada, Pacific Territories <p>10 = Seattle: <p>Alaska, Idaho, Oregon, Washington |
| condition            | The medical conditions treated in the facility.<p>  <p> • Stroke <p> • Nervous system disorder (excluding stroke) <p> • Brain disease or condition (non- traumatic) <p> • Brain injury (traumatic) <p> • Spinal cord disease or condition (non-traumatic) <p> • Spinal cord injury (traumatic) <p> • Hip or femur fracture <p> • Hip or knee replacement, amputation or other bone or joint conditions <p> • All other conditions |
| count           | The count of the corresponding medical condition for that facility.<p>  <p> Note: Medical conditions with counts of less than 11 are labeled as “less than 11” to protect patient confidentiality. |
| footnote             | Indicates the relevant footnote.<p> <p> 1 = Number of cases is too small to report. <p> 2 = Data not available for this reporting period. |


</details>

___

## Instructions For Recreating This Project

1. Clone this repository into your local machine using the following command:
```bash
git@github.com:AJMartinezLlanes/personal-project.git
```
2. You will need Pandas, Numpy, Matplotlib, Seaborn, SKLearn, statsmodels, and prophet installed on your machine.
3. File can be found at: https://data.cms.gov/provider-data/dataset/ka5z-ibe3
4. Now you can start a Jupyter Notebook session and execute the code blocks in the medicare_conditions.ipynb notebook.


---
### Data Acquisition

In this phase data is acquired from https://data.cms.gov/provider-data/dataset/ka5z-ibe3. The data is cached in a .csv file for faster loading and convenience.

- The wrangle.ipynb notebook in the notebooks directory contains a reproducible step by step process for acquiring and preparing data with details and explanations.

- The wrangle.py file contains all the data acquisition and preparation code used in the final report notebook.

**Steps Taken:**
1. Download .csv file from the link provided.
2. Ensure that all the data has been properly acquired.

### Data Preparation

In this phase the superstore data is prepared for exploration and modeling. Preparation includes renaming columns, removing unneeded columns, setting the date as the index, and separating the data into various groups that are to be analyzed.

- The wrangle.ipynb notebook in the notebooks directory contains a reproducible step by step process for preparing the data with details and explanations.

- The wrangle.py file contains code used in the final report for acquiring and preparing the data.

**Steps Taken:**
1. Analyze the data to determine how it should be cleaned.
2. Rename columns for ease of use.
3. Remove unnecessary columns.
4. Separate the data into various groups that will be analyzed in exploration.
5. Encapsulate all preparation code in wrangle.py.

### Exploratory Analysis

In this phase data is analyzed to determine what are the most common conditions, what states and regions are the highest and lowest. 
We start by analyzing the states with the contidions and regions. We also analyzed Texas and Vermount and conditions. Lastly we went into the cities in Texas and conditions.

- The explore.ipynb notebook in the notebooks directory contains a reproducible step by step process for exploring the data with details and explanations.

- The wrangle.py file contains all the data exploration functions used in the final report notebook.

**Steps Taken:**
1. Analyze data per region.
2. Analyze data per state.
3. Go into detail on highest and lowest month.
4. Analyze data per cities in Texas.
5. Encapsulate all preparation for final report in final.py.

### Modeling

In this phase we tried three different models that outperformed the baseline.

- The model.ipynb notebook in the notebooks directory contains a reproducible step by step process for exploring the data with details and explanations.

- The wrangle.py file contains all the modeling functions used in the final report notebook and model.ipynb notebook.


**Steps Taken:**
1. Acquire, prepare, and split the data.
2. Establish a baseline model.
3. Create various models.
4. Evaluate the performance of all models and choose the model with the best performance.

___

## Conclusion

The state of Texas had the highest number of strokes. All other conditions was the highest number of instances, but we went with stroke since was the most singular condition. Overall there was a lot of great info and I would like to go into more states and see what is the highest condition in each. 

___

[Back to top](#superstore-sales-2018-goals-and-forecast)