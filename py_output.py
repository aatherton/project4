
# coding: utf-8

# In[1]:


# import modules
import pandas


# In[2]:


# declare variables
data = pandas.read_json("purchase_data.json")
data.append(pandas.read_json("purchase_data2.json"))
data.head()


# # Playercount

# In[3]:


print("Total Players: " + str(len(data["SN"].value_counts())))


# # purchasing analysis (total)

# In[4]:


result = pandas.DataFrame({"Number of Unique Items": len(data.drop_duplicates("Item ID")),
                         "Average Price": data.drop_duplicates("Item ID")["Price"].mean(),
                         "Number of Purchases": len(data),
                         "Total Revenue": data["Price"].sum()
                        }, index = [0])
result["Total Revenue"] = result["Total Revenue"].apply("${:,.2f}".format)
result["Average Price"] = result["Average Price"].apply("${:,.2f}".format)
result


# # Gender Demographics

# In[5]:


result = pandas.DataFrame(data["Gender"].value_counts())
result["Percentage of Players"] = (result["Gender"] / len(data) * 100)
result = result.rename(columns = {"Gender":"Total Count"})
result


# # Purchasing Analysis (Gender)

# In[14]:


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


# # Age Demographics

# In[13]:


result = pandas.DataFrame({"Total Count": {"<10": len(data.loc[data["Age"] < 10])}})
ball = data.drop(data.loc[data["Age"] < 10].index)
for each in range(14, 40, 5):
    result = result.append(pandas.Series(data = {"Total Count": len(ball.loc[ball["Age"] <= each])}, name = str(each-4) + "-" + str(each)))
    ball = ball.drop(ball.loc[ball["Age"] <= each].index)
result = result.append(pandas.Series(data = {"Total Count": len(ball)}, name = "40+"))
result["Percentage of Players"] = round((result["Total Count"] / len(data)) * 100, 2)
result["Percentage of Players"] = result["Percentage of Players"].apply("{:,.2f}%".format)
result


# # Purchasing Analysis (Age)

# In[8]:


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


# In[9]:


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


# In[10]:


result = pandas.DataFrame(columns = ["Item ID", "Item Name", "Purchase Count", "Item Price"])
for each in data["Item ID"].drop_duplicates():
    ball = data.loc[data["Item ID"] == each]
    result = result.append(pandas.Series(data = {"Item ID": each, "Item Name": ball["Item Name"][ball.index[0]], "Purchase Count": len(ball), "Item Price": ball["Price"][ball.index[0]]}), ignore_index = True)
result["Total Purchase Value"] = result["Purchase Count"] * result["Item Price"]
ball = result.sort_values("Total Purchase Value", ascending = False).head(5)
ball["Item Price"] = ball["Item Price"].apply("${:,.2f}".format)
ball["Total Purchase Value"] = ball["Total Purchase Value"].apply("${:,.2f}".format)
ball


# In[12]:


result = ball.sort_values("Purchase Count", ascending = False).head(5)
result

