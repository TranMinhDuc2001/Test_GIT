import pandas as pd

#-------------Series-------------#

# a = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(a, index = ["day1", "day2", "day3"])
# print(myvar.loc["day2"])

# pd.options.display.max_rows = 999
# df = pd.read_json('data.json')
# print(df.to_string()) # in đầy đủ bảng

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)
# print(df)

#--------------Emty Cells--------------#
#df = pd.read_csv("data.csv")
# df.dropna(inplace = True) #tạo ra 1 bản sao và thay đổi dl DataFrame nếu có inplace thì data.csv sẽ bị thay đổi
# print(df.to_string())

# df["Calories"].fillna(130,inplace=True) #lấp đầy chỗ trống
# print(df.to_string())

# x = df["Calories"].mean()
# df["Calories"].fillna(x,inplace=True)
# print(df.to_string())

#--------------Wrongs Format--------------#
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date']) #những định dang sai ở cột Date sẽ đc sửa cho đúng
# print(df.to_string())

# df.dropna(subset=['Date'], inplace=True) #xóa các phần tử NULL
# print(df.to_string())

#--------------Wrongs Data--------------#
# df = pd.read_csv('data.csv')
# df.loc[7,'Duration'] = 45
# print(df.to_string())

# for x in df.index: # thay thế các hàng có duration > 120
#     if df.loc[x,'Duration'] > 120:
#         df.loc[x,'Duration']  = 120
# print(df.to_string())

# for x in df.index:
#     if df.loc[x,'Duration'] > 120:
#         df.drop(x, inplace = True)
# print(df.to_string())

#--------------Remove Duplicates--------------#
# df = pd.read_csv('data.csv')
# df.drop_duplicates(inplace=True)
# print(df.to_string())

#--------------Correlation--------------#
# df = pd.read_csv('data.csv')#sự trương quan từ -1 đến 1 nó thể hiện cái này tăng thì cái kia cũng tăng
# print(df.corr())

#--------------Plotting--------------#

