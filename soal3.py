# Soal 3 - Mengurai dan Merajut Kata

def urai(str):                       # Function dengan nama urai dan 1 parameter str
    result= ""                       # Membuat variabel result dengan string kosong
    for x in range(len(str)):        # Looping 
        result = result + str[:x+1]  # variabel result dalam looping ditambahkan dg index [:x+1]
    return result                    # me-return / mengembalikan hasil dr result


# menampilkan hasil penggunaan function
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))


def rajut(str):
    keys = str[0]                   # membuat variabel dg nama keys yg berisi string kosong
    baru = str.split(keys)          # membuat variabel dg nama baru untuk mensplit hasil dari variabel keys
    result = keys + baru[-1]
    return result                   # me-return / mengembalikan hasil dr result


# menampilkan hasil penggunaan function
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))