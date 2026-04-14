### Worksheet 1: Treemap – Top 3 Highest‑Paid Jobs in Major Locations

- The top 5 city locations by **employee count**.
- Within each location, the **top 3 job titles** ranked by **average annual salary**.
- Box size represents the **average salary** of that job title in that location.
- Box color distinguishes the **location**.
### Worksheet 2: Bar Chart – Salary Percentile and Composition by Age & Gender

- Total annual payroll (in millions of dollars) aggregated by **employee age range**.
- Side‑by‑side bars split by **gender (Male/Female)**.
- A **reference line** showing the average payroll per age group.
- **Table Calculation (Percent of Total)** displayed on the labels, showing each bar's share of the **entire city payroll**.
### Worksheet 3: Highlight Table – Diversity in Top‑Paying Departments

- A **heatmap** crossing **department** (rows) with **race** (columns).
- Cell color intensity reflects the selected metric, controlled by a **parameter** dropdown.
- Users can toggle between:
    - **Average Salary**
    - **Median Salary**
    - **Employee Count**
- Only departments with **≥5 employees** and ranking in the **top 5 by average salary** are shown.
### Worksheet 4: Scatter Plot – Tenure & Salary Segmentation (Clusters)
- Each point represents a **Job Tittle**.
- **X‑Axis:** `Years of Service` (calculated from `HIRE_DATE`).
- **Y‑Axis:** `Annual Salary Rate`.
- Points are **colored by cluster**.
	- Cluster 1 → **Senior / Supervisory**
	- Cluster 2 → **Entry‑Level Roles**
	- Cluster 3 → **Skilled / Mid‑Career**
	- Cluster 4 → **Executive / Leadership**
### Requirement Checklist

| Requirement                                                     | Met By                                    | Status |
| --------------------------------------------------------------- | ----------------------------------------- | ------ |
| At least one **reference line**                                 | WS2 (Average payroll)                     | ✅      |
| At least one **table calculation**                              | WS2 (percent of total payroll)            | ✅      |
| At least one **parameter**                                      | WS3 (Select Metric)                       | ✅      |
| At least one **calculated field**                               | WS3 (Metric Value), WS4 (Year of Service) | ✅      |
| At least one **analytics element** (clustering, forecast, etc.) | WS4 (Clustering)                          | ✅      |
