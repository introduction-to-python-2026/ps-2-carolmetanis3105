def find_max_number(num1, num2, num3):
   if num1 > num2 and num1 > num3 :
    return num1
   elif num2 > num3 and num2 > num3 :
    return num2
   else :
      return num3

def find_mean(num1, num2, num3):
  x = num1 + num2 + num3
 avg = float(x/3)
return avg


def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    z = (((num1 - mean)** 2 + (num2 - mean)** 2 + (num3 - mean)** 2)/3)**0.5
    return mean, z
