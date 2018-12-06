month = int(input("Vui lòng nhập tháng trong năm:"))

if month < 4 and month > 0:
    print("Tháng bạn vừa nhập là mùa Xuân.")
elif month > 3 and month <7:
    print("Tháng bạn vừa nhập là mùa Hạ.")
elif month < 10 and month > 0:
    print("Tháng bạn vừa nhập là mùa Thu.")
elif month > 10 and month < 13:
     print("Tháng bạn vừa nhập là mùa Đông.")     
else:
         print("Tháng bạn vừa nhập không có trong năm!")         