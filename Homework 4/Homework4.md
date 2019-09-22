
### Heroes Of Pymoli Data Analysis
* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.


```python
# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count

* Display the total number of players



```python
total_players = len(purchase_data['SN'].unique())
total_players_value = len(purchase_data['SN'].value_counts())
total_players = pd.DataFrame([total_players], columns = ['Total Players'])
total_players
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python
items_un = len(purchase_data['Item ID'].unique())
avg_price = round(purchase_data['Price'].mean(), 2)
avg_price_dollar = '${}'.format(avg_price)
num_purchases = len(purchase_data['Purchase ID'].value_counts())
total_revenue = purchase_data['Price'].sum()
total_revenue_dollar = '${:,}'.format(total_revenue)

df_summary = pd.DataFrame({
    "Number of Unique Items":items_un,
    "Average Price":avg_price_dollar,
    "Number of Purchases":num_purchases, 
    "Total Revenue":total_revenue_dollar
}, index=[0])
df_summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$3.05</td>
      <td>780</td>
      <td>$2,379.77</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed





```python
# LONG HAND WAY!!!! Then I realized I can do groupby :)

sn_dups = purchase_data.drop_duplicates(['SN'])
total_dups = sn_dups['Gender'].count()

male_df = sn_dups.loc[sn_dups['Gender'] == 'Male']
male_count = male_df['Gender'].count()
male_per = round(((male_count/total_dups)*100), 2)

female_df = sn_dups.loc[sn_dups['Gender'] == 'Female']
female_count = female_df['Gender'].count()
female_per = round(((female_count/total_dups)*100), 2)

other_df = sn_dups.loc[(sn_dups['Gender'] != 'Male') & (sn_dups['Gender'] != 'Female')]
other_count = other_df['Gender'].count()
other_per = round(((other_count/total_dups)*100), 2)

gender_demo = pd.DataFrame({
    "Total Count":[male_count, female_count, other_count],
    "Percentage of Players":['{}%'.format(male_per), 
                             '{}%'.format(female_per), 
                             '{}%'.format(other_per)]
})
gender_demo.index = ['Male', 'Female', 'Other / Non-Disclosed']
gender_demo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>484</td>
      <td>84.03%</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>81</td>
      <td>14.06%</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>1.91%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# More efficient method 

sn_dups = purchase_data.drop_duplicates(['SN'])
total_dups = sn_dups['Gender'].count()

gender_group = sn_dups.groupby('Gender')

sex_group_count = gender_group['Gender'].count()

new_gender_demo = pd.DataFrame({
    "Total Count":sex_group_count,
    "Percentage of Players":(sex_group_count/total_dups)*100
})
new_gender_demo.sort_values(['Total Count'], ascending = False).style.format({"Percentage of Players":'{:.2f}%'})
```




<style  type="text/css" >
</style><table id="T_3ed64ce8_dd56_11e9_8608_acde48001122" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Total Count</th>        <th class="col_heading level0 col1" >Percentage of Players</th>    </tr>    <tr>        <th class="index_name level0" >Gender</th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_3ed64ce8_dd56_11e9_8608_acde48001122level0_row0" class="row_heading level0 row0" >Male</th>
                        <td id="T_3ed64ce8_dd56_11e9_8608_acde48001122row0_col0" class="data row0 col0" >484</td>
                        <td id="T_3ed64ce8_dd56_11e9_8608_acde48001122row0_col1" class="data row0 col1" >84.03%</td>
            </tr>
            <tr>
                        <th id="T_3ed64ce8_dd56_11e9_8608_acde48001122level0_row1" class="row_heading level0 row1" >Female</th>
                        <td id="T_3ed64ce8_dd56_11e9_8608_acde48001122row1_col0" class="data row1 col0" >81</td>
                        <td id="T_3ed64ce8_dd56_11e9_8608_acde48001122row1_col1" class="data row1 col1" >14.06%</td>
            </tr>
            <tr>
                        <th id="T_3ed64ce8_dd56_11e9_8608_acde48001122level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th>
                        <td id="T_3ed64ce8_dd56_11e9_8608_acde48001122row2_col0" class="data row2 col0" >11</td>
                        <td id="T_3ed64ce8_dd56_11e9_8608_acde48001122row2_col1" class="data row2 col1" >1.91%</td>
            </tr>
    </tbody></table>




## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
# LONG HAND WAY!!!! Then I realized I can do groupby :)

female_pur_df = purchase_data.loc[purchase_data['Gender'] == 'Female']
female_pur_count = female_pur_df['Gender'].count()
female_pur_avgprice = round(female_pur_df['Price'].mean(),2)
female_pur_total = female_pur_df['Price'].sum()
female_pur_avg = round(female_pur_total/female_count, 2)

male_pur_df = purchase_data.loc[purchase_data['Gender'] == 'Male']
male_pur_count = male_pur_df['Gender'].count()
male_pur_avgprice = round(male_pur_df['Price'].mean(), 2)
male_pur_total = male_pur_df['Price'].sum()
male_pur_avg = round(male_pur_total/male_count, 2)

other_pur_df = purchase_data.loc[(purchase_data['Gender'] != 'Male') & (purchase_data['Gender'] != 'Female')]
other_pur_count = other_pur_df['Gender'].count()
other_pur_avgprice = round(other_pur_df['Price'].mean(), 2)
other_pur_total = other_pur_df['Price'].sum()
other_pur_avg = round(other_pur_total/other_count, 2)

gender_purchase_df = pd.DataFrame({
    "Purchase Count":[female_pur_count, male_pur_count, other_pur_count],
    "Average Purchase Price":['${}0'.format(female_pur_avgprice), '${}'.format(male_pur_avgprice), '${}'.format(other_pur_avgprice)],
    "Total Purchase Value":['${:,}'.format(female_pur_total), '${:,}'.format(male_pur_total), '${:,}'.format(other_pur_total)],
    "Avg Total Purchase per Person":['${}'.format(female_pur_avg), '${}'.format(male_pur_avg), '${}'.format(other_pur_avg)]
})
gender_purchase_df.index = ['Female', 'Male', 'Other / Non-Disclosed']
gender_purchase_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Avg Total Purchase per Person</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>113</td>
      <td>$3.20</td>
      <td>$361.94</td>
      <td>$4.47</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>$3.02</td>
      <td>$1,967.64</td>
      <td>$4.07</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>15</td>
      <td>$3.35</td>
      <td>$50.19</td>
      <td>$4.56</td>
    </tr>
  </tbody>
</table>
</div>




```python
# More efficient method 

all_gender = purchase_data.groupby('Gender')
total_gender = all_gender.nunique()["SN"]

purchase_count = all_gender["Purchase ID"].count()

avg_purchase_price = all_gender["Price"].mean()

avg_purchase_total = all_gender["Price"].sum()

avg_purchase_per_person = avg_purchase_total/total_gender

gender_purchase_df_new = pd.DataFrame({
    "Purchase Count":purchase_count, 
    "Average Purchase Price":avg_purchase_price,
    "Average Purchase Value":avg_purchase_total,
    "Avg Purchase Total per Person":avg_purchase_per_person
})

gender_purchase_df_new.index.name = "Gender"

gender_purchase_df_new.style.format({"Average Purchase Value":"${:,.2f}",
                                  "Average Purchase Price":"${:,.2f}",
                                  "Avg Purchase Total per Person":"${:,.2f}"})
```




<style  type="text/css" >
</style><table id="T_3f1fbfd6_dd56_11e9_8608_acde48001122" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Average Purchase Value</th>        <th class="col_heading level0 col3" >Avg Purchase Total per Person</th>    </tr>    <tr>        <th class="index_name level0" >Gender</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_3f1fbfd6_dd56_11e9_8608_acde48001122level0_row0" class="row_heading level0 row0" >Female</th>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row0_col0" class="data row0 col0" >113</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row0_col1" class="data row0 col1" >$3.20</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row0_col2" class="data row0 col2" >$361.94</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row0_col3" class="data row0 col3" >$4.47</td>
            </tr>
            <tr>
                        <th id="T_3f1fbfd6_dd56_11e9_8608_acde48001122level0_row1" class="row_heading level0 row1" >Male</th>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row1_col0" class="data row1 col0" >652</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row1_col1" class="data row1 col1" >$3.02</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row1_col2" class="data row1 col2" >$1,967.64</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row1_col3" class="data row1 col3" >$4.07</td>
            </tr>
            <tr>
                        <th id="T_3f1fbfd6_dd56_11e9_8608_acde48001122level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row2_col0" class="data row2 col0" >15</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row2_col1" class="data row2 col1" >$3.35</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row2_col2" class="data row2 col2" >$50.19</td>
                        <td id="T_3f1fbfd6_dd56_11e9_8608_acde48001122row2_col3" class="data row2 col3" >$4.56</td>
            </tr>
    </tbody></table>



## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table



```python
# LONG HAND WAY!!!! Then I realized I can do groupby :)

bins = [0,9,14,19,24,29,34,39,1000000]
group_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
sn_dups['Age Group'] = pd.cut(sn_dups['Age'], bins, labels=group_names)
sn_dups_total = sn_dups['Age Group'].count()

group_one_df = sn_dups.loc[sn_dups['Age Group'] == '<10']
group_one_count = group_one_df['Age Group'].count()
group_one_avg = round((group_one_count/sn_dups_total)*100, 2)

group_two_df = sn_dups.loc[sn_dups['Age Group'] == '10-14']
group_two_count = group_two_df['Age Group'].count()
group_two_avg = round((group_two_count/sn_dups_total)*100, 2)

group_three_df = sn_dups.loc[sn_dups['Age Group'] == '15-19']
group_three_count = group_three_df['Age Group'].count()
group_three_avg = round((group_three_count/sn_dups_total)*100, 2)

group_four_df = sn_dups.loc[sn_dups['Age Group'] == '20-24']
group_four_count = group_four_df['Age Group'].count()
group_four_avg = round((group_four_count/sn_dups_total)*100, 2)

group_five_df = sn_dups.loc[sn_dups['Age Group'] == '25-29']
group_five_count = group_five_df['Age Group'].count()
group_five_avg = round((group_five_count/sn_dups_total)*100, 2)

group_six_df = sn_dups.loc[sn_dups['Age Group'] == '30-34']
group_six_count = group_six_df['Age Group'].count()
group_six_avg = round((group_six_count/sn_dups_total)*100, 2)

group_seven_df = sn_dups.loc[sn_dups['Age Group'] == '35-39']
group_seven_count = group_seven_df['Age Group'].count()
group_seven_avg = round((group_seven_count/sn_dups_total)*100, 2)

group_eight_df = sn_dups.loc[sn_dups['Age Group'] == '40+']
group_eight_count = group_eight_df['Age Group'].count()
group_eight_avg = round((group_eight_count/sn_dups_total)*100, 2)

age_purchase_df = pd.DataFrame({
    "Total Count":[group_one_count, group_two_count, group_three_count, group_four_count, group_five_count, group_six_count, group_seven_count, group_eight_count],
    "Percentage of Players":[group_one_avg, group_two_avg, group_three_avg, group_four_avg, group_five_avg, group_six_avg, group_seven_avg, group_eight_avg],
})
age_purchase_df.index = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
age_purchase_df
```

    /Users/deniscohen/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>17</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>22</td>
      <td>3.82</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>107</td>
      <td>18.58</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>258</td>
      <td>44.79</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>77</td>
      <td>13.37</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>52</td>
      <td>9.03</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>31</td>
      <td>5.38</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>12</td>
      <td>2.08</td>
    </tr>
  </tbody>
</table>
</div>




```python
# More efficient method 

bins = [0,9,14,19,24,29,34,39,1000000]
group_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
purchase_data['Age Group'] = pd.cut(purchase_data['Age'], bins, labels=group_names)

age_grouped = purchase_data.groupby("Age Group")

total_count_age = age_grouped["SN"].nunique()

percentage_by_age = (total_count_age/total_players_value) * 100

age_demographics = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})

age_demographics.index.name = None

age_demographics.style.format({"Percentage of Players":"{:,.2f}"})
```




<style  type="text/css" >
</style><table id="T_3f90958a_dd56_11e9_8608_acde48001122" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Percentage of Players</th>        <th class="col_heading level0 col1" >Total Count</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_3f90958a_dd56_11e9_8608_acde48001122level0_row0" class="row_heading level0 row0" ><10</th>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row0_col0" class="data row0 col0" >2.95</td>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row0_col1" class="data row0 col1" >17</td>
            </tr>
            <tr>
                        <th id="T_3f90958a_dd56_11e9_8608_acde48001122level0_row1" class="row_heading level0 row1" >10-14</th>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row1_col0" class="data row1 col0" >3.82</td>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row1_col1" class="data row1 col1" >22</td>
            </tr>
            <tr>
                        <th id="T_3f90958a_dd56_11e9_8608_acde48001122level0_row2" class="row_heading level0 row2" >15-19</th>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row2_col0" class="data row2 col0" >18.58</td>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row2_col1" class="data row2 col1" >107</td>
            </tr>
            <tr>
                        <th id="T_3f90958a_dd56_11e9_8608_acde48001122level0_row3" class="row_heading level0 row3" >20-24</th>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row3_col0" class="data row3 col0" >44.79</td>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row3_col1" class="data row3 col1" >258</td>
            </tr>
            <tr>
                        <th id="T_3f90958a_dd56_11e9_8608_acde48001122level0_row4" class="row_heading level0 row4" >25-29</th>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row4_col0" class="data row4 col0" >13.37</td>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row4_col1" class="data row4 col1" >77</td>
            </tr>
            <tr>
                        <th id="T_3f90958a_dd56_11e9_8608_acde48001122level0_row5" class="row_heading level0 row5" >30-34</th>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row5_col0" class="data row5 col0" >9.03</td>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row5_col1" class="data row5 col1" >52</td>
            </tr>
            <tr>
                        <th id="T_3f90958a_dd56_11e9_8608_acde48001122level0_row6" class="row_heading level0 row6" >35-39</th>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row6_col0" class="data row6 col0" >5.38</td>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row6_col1" class="data row6 col1" >31</td>
            </tr>
            <tr>
                        <th id="T_3f90958a_dd56_11e9_8608_acde48001122level0_row7" class="row_heading level0 row7" >40+</th>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row7_col0" class="data row7 col0" >2.08</td>
                        <td id="T_3f90958a_dd56_11e9_8608_acde48001122row7_col1" class="data row7 col1" >12</td>
            </tr>
    </tbody></table>




```python

```

## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
bins = [0,9,14,19,24,29,34,39,1000000]
group_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
purchase_data['Age Group'] = pd.cut(purchase_data['Age'], bins, labels=group_names)

age_grouped = purchase_data.groupby("Age Group")

total_count_age = age_grouped["SN"].nunique()

purchase_count_age = age_grouped["Purchase ID"].count()

avg_purchase_price_age = age_grouped["Price"].mean()

total_purchase_value = age_grouped["Price"].sum()

avg_purchase_per_person_age = total_purchase_value/total_count_age

age_demographics = pd.DataFrame({"Purchase Count": purchase_count_age,
                                 "Average Purchase Price": avg_purchase_price_age,
                                 "Total Purchase Value":total_purchase_value,
                                 "Average Purchase Total per Person": avg_purchase_per_person_age})

age_demographics.index.name = None

age_demographics.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total per Person":"${:,.2f}"})
```




<style  type="text/css" >
</style><table id="T_3ffc7cd2_dd56_11e9_8608_acde48001122" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>        <th class="col_heading level0 col3" >Average Purchase Total per Person</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_3ffc7cd2_dd56_11e9_8608_acde48001122level0_row0" class="row_heading level0 row0" ><10</th>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row0_col0" class="data row0 col0" >23</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row0_col1" class="data row0 col1" >$3.35</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row0_col2" class="data row0 col2" >$77.13</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row0_col3" class="data row0 col3" >$4.54</td>
            </tr>
            <tr>
                        <th id="T_3ffc7cd2_dd56_11e9_8608_acde48001122level0_row1" class="row_heading level0 row1" >10-14</th>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row1_col0" class="data row1 col0" >28</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row1_col1" class="data row1 col1" >$2.96</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row1_col2" class="data row1 col2" >$82.78</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row1_col3" class="data row1 col3" >$3.76</td>
            </tr>
            <tr>
                        <th id="T_3ffc7cd2_dd56_11e9_8608_acde48001122level0_row2" class="row_heading level0 row2" >15-19</th>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row2_col0" class="data row2 col0" >136</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row2_col1" class="data row2 col1" >$3.04</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row2_col2" class="data row2 col2" >$412.89</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row2_col3" class="data row2 col3" >$3.86</td>
            </tr>
            <tr>
                        <th id="T_3ffc7cd2_dd56_11e9_8608_acde48001122level0_row3" class="row_heading level0 row3" >20-24</th>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row3_col0" class="data row3 col0" >365</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row3_col1" class="data row3 col1" >$3.05</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row3_col2" class="data row3 col2" >$1,114.06</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row3_col3" class="data row3 col3" >$4.32</td>
            </tr>
            <tr>
                        <th id="T_3ffc7cd2_dd56_11e9_8608_acde48001122level0_row4" class="row_heading level0 row4" >25-29</th>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row4_col0" class="data row4 col0" >101</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row4_col1" class="data row4 col1" >$2.90</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row4_col2" class="data row4 col2" >$293.00</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row4_col3" class="data row4 col3" >$3.81</td>
            </tr>
            <tr>
                        <th id="T_3ffc7cd2_dd56_11e9_8608_acde48001122level0_row5" class="row_heading level0 row5" >30-34</th>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row5_col0" class="data row5 col0" >73</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row5_col1" class="data row5 col1" >$2.93</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row5_col2" class="data row5 col2" >$214.00</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row5_col3" class="data row5 col3" >$4.12</td>
            </tr>
            <tr>
                        <th id="T_3ffc7cd2_dd56_11e9_8608_acde48001122level0_row6" class="row_heading level0 row6" >35-39</th>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row6_col0" class="data row6 col0" >41</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row6_col1" class="data row6 col1" >$3.60</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row6_col2" class="data row6 col2" >$147.67</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row6_col3" class="data row6 col3" >$4.76</td>
            </tr>
            <tr>
                        <th id="T_3ffc7cd2_dd56_11e9_8608_acde48001122level0_row7" class="row_heading level0 row7" >40+</th>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row7_col0" class="data row7 col0" >13</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row7_col1" class="data row7 col1" >$2.94</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row7_col2" class="data row7 col2" >$38.24</td>
                        <td id="T_3ffc7cd2_dd56_11e9_8608_acde48001122row7_col3" class="data row7 col3" >$3.19</td>
            </tr>
    </tbody></table>



## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
spender_df = purchase_data.groupby("SN")

count_spender = spender_df["Purchase ID"].count()
 
avg_spender = spender_df["Price"].mean()

total_spender = spender_df["Price"].sum()

top_spenders = pd.DataFrame({"Purchase Count": count_spender,
                             "Average Purchase Price": avg_spender,
                             "Total Purchase Value":total_spender})

formatted_spenders = top_spenders.sort_values(["Total Purchase Value"], ascending=False).head()

formatted_spenders.style.format({"Average Purchase Total":"${:,.2f}",
                                 "Average Purchase Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style><table id="T_404d2fd8_dd56_11e9_8608_acde48001122" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >SN</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_404d2fd8_dd56_11e9_8608_acde48001122level0_row0" class="row_heading level0 row0" >Lisosia93</th>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row0_col0" class="data row0 col0" >5</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row0_col1" class="data row0 col1" >$3.79</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row0_col2" class="data row0 col2" >$18.96</td>
            </tr>
            <tr>
                        <th id="T_404d2fd8_dd56_11e9_8608_acde48001122level0_row1" class="row_heading level0 row1" >Idastidru52</th>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row1_col0" class="data row1 col0" >4</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row1_col1" class="data row1 col1" >$3.86</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row1_col2" class="data row1 col2" >$15.45</td>
            </tr>
            <tr>
                        <th id="T_404d2fd8_dd56_11e9_8608_acde48001122level0_row2" class="row_heading level0 row2" >Chamjask73</th>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row2_col0" class="data row2 col0" >3</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row2_col1" class="data row2 col1" >$4.61</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row2_col2" class="data row2 col2" >$13.83</td>
            </tr>
            <tr>
                        <th id="T_404d2fd8_dd56_11e9_8608_acde48001122level0_row3" class="row_heading level0 row3" >Iral74</th>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row3_col0" class="data row3 col0" >4</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row3_col1" class="data row3 col1" >$3.40</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row3_col2" class="data row3 col2" >$13.62</td>
            </tr>
            <tr>
                        <th id="T_404d2fd8_dd56_11e9_8608_acde48001122level0_row4" class="row_heading level0 row4" >Iskadarya95</th>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row4_col0" class="data row4 col0" >3</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row4_col1" class="data row4 col1" >$4.37</td>
                        <td id="T_404d2fd8_dd56_11e9_8608_acde48001122row4_col2" class="data row4 col2" >$13.10</td>
            </tr>
    </tbody></table>



## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
items = purchase_data[["Item ID", "Item Name", "Price"]]

item_stats = items.groupby(["Item ID","Item Name"])

purchase_count_item = item_stats["Price"].count()

purchase_value = (item_stats["Price"].sum()) 

item_price = purchase_value/purchase_count_item

pop_items_df = pd.DataFrame({"Purchase Count": purchase_count_item, 
                                   "Item Price": item_price,
                                   "Total Purchase Value":purchase_value})

popular_df = pop_items_df.sort_values(["Purchase Count"], ascending=False).head()

popular_df.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style><table id="T_40a03bb0_dd56_11e9_8608_acde48001122" ><thead>    <tr>        <th class="blank" ></th>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Item Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >Item ID</th>        <th class="index_name level1" >Item Name</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level0_row0" class="row_heading level0 row0" >178</th>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level1_row0" class="row_heading level1 row0" >Oathbreaker, Last Hope of the Breaking Storm</th>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row0_col0" class="data row0 col0" >12</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row0_col1" class="data row0 col1" >$4.23</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row0_col2" class="data row0 col2" >$50.76</td>
            </tr>
            <tr>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level0_row1" class="row_heading level0 row1" >145</th>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level1_row1" class="row_heading level1 row1" >Fiery Glass Crusader</th>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row1_col0" class="data row1 col0" >9</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row1_col1" class="data row1 col1" >$4.58</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row1_col2" class="data row1 col2" >$41.22</td>
            </tr>
            <tr>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level0_row2" class="row_heading level0 row2" >108</th>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level1_row2" class="row_heading level1 row2" >Extraction, Quickblade Of Trembling Hands</th>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row2_col0" class="data row2 col0" >9</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row2_col1" class="data row2 col1" >$3.53</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row2_col2" class="data row2 col2" >$31.77</td>
            </tr>
            <tr>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level0_row3" class="row_heading level0 row3" >82</th>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level1_row3" class="row_heading level1 row3" >Nirvana</th>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row3_col0" class="data row3 col0" >9</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row3_col1" class="data row3 col1" >$4.90</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row3_col2" class="data row3 col2" >$44.10</td>
            </tr>
            <tr>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level0_row4" class="row_heading level0 row4" >19</th>
                        <th id="T_40a03bb0_dd56_11e9_8608_acde48001122level1_row4" class="row_heading level1 row4" >Pursuit, Cudgel of Necromancy</th>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row4_col0" class="data row4 col0" >8</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row4_col1" class="data row4 col1" >$1.02</td>
                        <td id="T_40a03bb0_dd56_11e9_8608_acde48001122row4_col2" class="data row4 col2" >$8.16</td>
            </tr>
    </tbody></table>



## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame




```python
popular_df = pop_items_df.sort_values(["Total Purchase Value"],
                                                   ascending=False).head()

popular_df.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style><table id="T_40f2cb1e_dd56_11e9_8608_acde48001122" ><thead>    <tr>        <th class="blank" ></th>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Item Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >Item ID</th>        <th class="index_name level1" >Item Name</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level0_row0" class="row_heading level0 row0" >178</th>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level1_row0" class="row_heading level1 row0" >Oathbreaker, Last Hope of the Breaking Storm</th>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row0_col0" class="data row0 col0" >12</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row0_col1" class="data row0 col1" >$4.23</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row0_col2" class="data row0 col2" >$50.76</td>
            </tr>
            <tr>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level0_row1" class="row_heading level0 row1" >82</th>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level1_row1" class="row_heading level1 row1" >Nirvana</th>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row1_col0" class="data row1 col0" >9</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row1_col1" class="data row1 col1" >$4.90</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row1_col2" class="data row1 col2" >$44.10</td>
            </tr>
            <tr>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level0_row2" class="row_heading level0 row2" >145</th>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level1_row2" class="row_heading level1 row2" >Fiery Glass Crusader</th>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row2_col0" class="data row2 col0" >9</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row2_col1" class="data row2 col1" >$4.58</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row2_col2" class="data row2 col2" >$41.22</td>
            </tr>
            <tr>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level0_row3" class="row_heading level0 row3" >92</th>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level1_row3" class="row_heading level1 row3" >Final Critic</th>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row3_col0" class="data row3 col0" >8</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row3_col1" class="data row3 col1" >$4.88</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row3_col2" class="data row3 col2" >$39.04</td>
            </tr>
            <tr>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level0_row4" class="row_heading level0 row4" >103</th>
                        <th id="T_40f2cb1e_dd56_11e9_8608_acde48001122level1_row4" class="row_heading level1 row4" >Singed Scalpel</th>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row4_col0" class="data row4 col0" >8</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row4_col1" class="data row4 col1" >$4.35</td>
                        <td id="T_40f2cb1e_dd56_11e9_8608_acde48001122row4_col2" class="data row4 col2" >$34.80</td>
            </tr>
    </tbody></table>


