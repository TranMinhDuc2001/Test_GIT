
import numpy as np

# arr = numpy.array([1,2,3,4,5])
# print(arr)

# print(np.__version__)

# arr = np.array([1, 2, 3, 4, 5])  #this is list
# arr = np.array((1, 2, 3, 4, 5))    #this is tuple
# arr = np.array([[1, 2, 3], [4, 5, 6]]) #2D array

# nidm chỉ số chiều của mảng
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# khi khai báo có đối số ndim thì tất cả các phần tử khác đều = 0
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)

#------------Array Index------------#

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 2])

# -----------Type-----------#

# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i') #astype cho phép thay đổi kiểu dữ liệu bằng cách sao chép mảng
# print(newarr)
# print(newarr.dtype)

# arr = np.array([1, 2, 3, 4], dtype='i4')
# print(arr)
# print(arr.dtype)

# -----------Copy and View-----------#

# arr = np.array([1, 2, 3, 4, 5])
# # x = arr.copy() #ko cho phép thay đổi mảng
# x = arr.view() #cho phép thay đổi mảng
# arr[0] = 42
# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base)
# print(y.base)

# -----------Shape-----------#

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape) # in ra 1 1 1 1 4 vì các cái khác có 4 phần tử riêng phần tử trong cùng có 4 số

# -----------Reshape-----------#

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3) # 4 hàng, mỗi hàng có 3 phần tử
# newarr = arr.reshape(2, 3, 2)
# print(newarr)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arr.reshape(2, 4).base) #kiểm tra xem là dạng view hay copy = base

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2, 2, -1) # không quan tâm dimention âm, chỉ đc dùng 1 unknown demention
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12])
# newarr = arr.reshape(2,2,-1) # chỉ có 1 số âm trong reshape và nó sẽ tự tính chiều còn lại
# print(newarr)

# arr = np.array([[1, 2, 3], [4, 5, 6],[7, 8 ]])
# newarr = arr.reshape(-1) # chuyển mảng nhiều chiều thành mảng 1 chiều
# print(newarr)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x) # cái này chỉ in chiều thứ n-1 nghĩa là in dimention 1

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in np.nditer(arr):
#     print(x)

# arr = np.array([1, 2, 3])
# for idx, x in np.ndenumerate(arr): #liệt kê kèm theo index
#   print(idx,x)

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.hsplit(arr, 3)
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr%2 == 0)
# print(x)

# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7, side = 'right') # giả sử mảng đã đc sắp xếp, side chỉ nơi đc bắt đầu khi tìm
# print(x)

# arr = np.array([1, 3, 5, 7])
# x = np.searchsorted(arr, [2, 4, 6]) # 2 4 6 sẽ đc xếp vào index 1 2 3 đc chèn vào mảng ban đầu
# print(x)

# -----------Sort-----------#

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))

# -----------Filter Array-----------#

# arr = np.array([1,2,3,4,5,6,7])

# filter_arr = arr > 5
# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[::2])