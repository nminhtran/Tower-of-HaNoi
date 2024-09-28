# Bai toan thap Ha Noi (de quy)
# B1 : move n-1 disks tren cung (dau -> trung gian)
# B2 : move last disks duoi cung (dau -> dich)
# B3 : move n-1 disks (trung gian -> dich)
def Matrix(column,row): # tạo ma trận chứa 3 cột (column = 3)
    matrix = []
    for _ in range(column):
        j = []
        matrix.append(j)
    for i in range(row):
        matrix[0].append(i+1)
    return matrix


def movement(matrix,numberdisks,start ,between ,finish): 
    if numberdisks == 1:
        matrix[finish-1].insert(0,matrix[start-1][numberdisks-1])
        matrix[start-1].remove(1)
    else:
        movement(matrix,numberdisks-1,start,finish,between) #B1
        #print("Loading ",matrix)
        matrix[finish-1].insert(0,matrix[start-1][0]) # B2
        matrix[start-1].remove(matrix[start-1][0]) # B2
        #print("Loading ",matrix)
        movement(matrix,numberdisks-1,between,start,finish) # B3
        #print("Loading ",matrix)

        return matrix
    

n = int(input("Number of disks: "))
matrix = Matrix(3,n)
print("Before: ",matrix)

result = movement(matrix,n,1,2,3)
print("After: ",result)
        