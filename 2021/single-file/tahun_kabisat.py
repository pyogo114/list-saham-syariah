# Check leap year

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 100 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(y, m):
    """Menghitung hari dalam sebuah bulan. Memerlukan argumen tahun dan bulan"""
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    d = month_days[m - 1]
    
    if m == 2 and is_leap(y):
        d = 29
    
    return d


year = int(input("Masukkan tahun :"))
month = int(input("Masukkan bulan :"))
days = days_in_month(year, month)

print(f"Jumlah hari pada bulan itu : {days} hari.")

