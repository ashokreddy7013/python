
d1 = {"employee":
          {"stocker":
               {101:
                    {"name":"Raja","cno":9876432105},
                102:
                    {"name":"Rani","cno":9874563210}
                },
           "dispatcher":
               {1001:
                    {"name":"kumar","cno":1236547891,"type":"Regular"},
                1002:
                    {"name":"Ravi","cno":6841368444,"type":"part time"}
                }
           }
      }

print(d1)
print(d1["employee"]["stocker"])
print(d1["employee"]["stocker"][101])
print(d1["employee"]["dispatcher"][1001]["cno"])