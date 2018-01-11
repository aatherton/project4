

```python
# import modules
import pandas
```


```python
# declare variables
data = pandas.read_json("purchase_data.json")
data.append(pandas.read_json("purchase_data2.json"))
data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>



# Playercount


```python
print("Total Players: " + str(len(data["SN"].value_counts())))
```

    Total Players: 573
    

# purchasing analysis (total)


```python
result = pandas.DataFrame({"Number of Unique Items": len(data.drop_duplicates("Item ID")),
                         "Average Price": data.drop_duplicates("Item ID")["Price"].mean(),
                         "Number of Purchases": len(data),
                         "Total Revenue": data["Price"].sum()
                        }, index = [0])
result["Total Revenue"] = result["Total Revenue"].apply("${:,.2f}".format)
result["Average Price"] = result["Average Price"].apply("${:,.2f}".format)
result
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Number of Unique Items</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.95</td>
      <td>780</td>
      <td>183</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>



# Gender Demographics


```python
result = pandas.DataFrame(data["Gender"].value_counts())
result["Percentage of Players"] = (result["Gender"] / len(data) * 100)
result = result.rename(columns = {"Gender":"Total Count"})
result
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
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
      <td>633</td>
      <td>81.153846</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>17.435897</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>1.410256</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Gender)


```python
result = pandas.DataFrame({"Male": {
    "Purchase Count": len(data.loc[data["Gender"] == "Male"]),
    "Average Purchase Price": data.loc[data["Gender"] == "Male"]["Price"].mean(),
    "Total Purchase Value": data.loc[data["Gender"] == "Male"]["Price"].sum()
}, "Female": {
    "Purchase Count": len(data.loc[data["Gender"] == "Female"]),
    "Average Purchase Price": data.loc[data["Gender"] == "Female"]["Price"].mean(),
    "Total Purchase Value": data.loc[data["Gender"] == "Female"]["Price"].sum()
}, "Other / Non-Disclosed": {
    "Purchase Count": len(data.loc[data["Gender"] == "Other / Non-Disclosed"]),
    "Average Purchase Price": data.loc[data["Gender"] == "Other / Non-Disclosed"]["Price"].mean(),
    "Total Purchase Value": data.loc[data["Gender"] == "Other / Non-Disclosed"]["Price"].sum()}})
result = result.transpose()
result["Average Purchase Price"] = result["Average Purchase Price"].apply("${:,.2f}".format)
result["Total Purchase Value"] = result["Total Purchase Value"].apply("${:,.2f}".format)
result
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>$2.82</td>
      <td>136.0</td>
      <td>$382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>$2.95</td>
      <td>633.0</td>
      <td>$1,867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$3.25</td>
      <td>11.0</td>
      <td>$35.74</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics


```python
result = pandas.DataFrame({"Total Count": {"<10": len(data.loc[data["Age"] < 10])}})
ball = data.drop(data.loc[data["Age"] < 10].index)
for each in range(14, 40, 5):
    result = result.append(pandas.Series(data = {"Total Count": len(ball.loc[ball["Age"] <= each])}, name = str(each-4) + "-" + str(each)))
    ball = ball.drop(ball.loc[ball["Age"] <= each].index)
result = result.append(pandas.Series(data = {"Total Count": len(ball)}, name = "40+"))
result["Percentage of Players"] = round((result["Total Count"] / len(data)) * 100, 2)
result["Percentage of Players"] = result["Percentage of Players"].apply("{:,.2f}%".format)
result
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
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
      <td>28</td>
      <td>3.59%</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>4.49%</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>17.05%</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>43.08%</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>16.03%</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>8.21%</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>5.38%</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>2.18%</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Age)


```python
ball = [0,0]
ball[0] = data.loc[data["Age"] < 10]["Price"]
result = pandas.DataFrame({"Purchase Count": {"<10": len(ball[0])}, "Total Purchase Value": {"<10": ball[0].sum()}})
ball[1] = data.drop(ball[0].index)
for each in range(14, 40, 5):
    ball[0] = ball[1].loc[ball[1]["Age"] <= each]["Price"]
    result = result.append(pandas.Series(data = {"Purchase Count": len(ball[0]), "Total Purchase Value": ball[0].sum()}, name = str(each-4) + "-" + str(each)))
    ball[1] = ball[1].drop(ball[0].index)
result = result.append(pandas.Series(data = {"Purchase Count": len(ball[1]), "Total Purchase Value": ball[1]["Price"].sum()}, name = "40+"))
result["Average Purchase Price"] = result["Total Purchase Value"] / result["Purchase Count"]
result["Total Purchase Value"] = result["Total Purchase Value"].apply("${:,.2f}".format)
result["Average Purchase Price"] = result["Average Purchase Price"].apply("${:,.2f}".format)
result
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28.0</td>
      <td>$83.46</td>
      <td>$2.98</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35.0</td>
      <td>$96.95</td>
      <td>$2.77</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133.0</td>
      <td>$386.42</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336.0</td>
      <td>$978.77</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125.0</td>
      <td>$370.33</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64.0</td>
      <td>$197.25</td>
      <td>$3.08</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42.0</td>
      <td>$119.40</td>
      <td>$2.84</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17.0</td>
      <td>$53.75</td>
      <td>$3.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
ball = [0,0]
ball[0] = data["SN"].drop_duplicates()
result = pandas.DataFrame(columns = ["Purchase Count", "Total Purchase Value"])
for each in ball[0]:
    ball[1] = data.loc[data["SN"] == each]["Price"]
    result = result.append(pandas.Series(data = {"Purchase Count": len(ball[1]), "Total Purchase Value": ball[1].sum()}, name = each))
result = result.sort_values("Total Purchase Value", ascending = False).head(5)
result["Average Purchase Price"] = result["Total Purchase Value"] / result["Purchase Count"]
result["Total Purchase Value"] = result["Total Purchase Value"].apply("${:,.2f}".format)
result["Average Purchase Price"] = result["Average Purchase Price"].apply("${:,.2f}".format)
result
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5.0</td>
      <td>$17.06</td>
      <td>$3.41</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4.0</td>
      <td>$13.56</td>
      <td>$3.39</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4.0</td>
      <td>$12.74</td>
      <td>$3.18</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3.0</td>
      <td>$12.73</td>
      <td>$4.24</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3.0</td>
      <td>$11.58</td>
      <td>$3.86</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = pandas.DataFrame(columns = ["Item ID", "Item Name", "Purchase Count", "Item Price"])
for each in data["Item ID"].drop_duplicates():
    ball = data.loc[data["Item ID"] == each]
    result = result.append(pandas.Series(data = {"Item ID": each, "Item Name": ball["Item Name"][ball.index[0]], "Purchase Count": len(ball), "Item Price": ball["Price"][ball.index[0]]}), ignore_index = True)
result["Total Purchase Value"] = result["Purchase Count"] * result["Item Price"]
ball = result.sort_values("Total Purchase Value", ascending = False).head(5)
ball["Item Price"] = ball["Item Price"].apply("${:,.2f}".format)
ball["Total Purchase Value"] = ball["Total Purchase Value"].apply("${:,.2f}".format)
ball
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>84</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>45</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>79</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>112</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = ball.sort_values("Purchase Count", ascending = False).head(5)
result
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>112</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
    <tr>
      <th>84</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>45</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>79</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
  </tbody>
</table>
</div>
