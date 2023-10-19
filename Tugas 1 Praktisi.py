# def konversi_suhu(suhu, skala):
# if skala == 'C':
#       hasil =(suhu - 32)* 5/9
# elif skala == 'F':
#     hasil = (suhu * 9/5)+32
# else:
#     raise ValueError("Skala tidak Valis. Gunakan 'C' untuk Celsius")

def kalkulator(operator, *args):
    if operator not in ('+', '-', '*', '/'):
        print("operator tidak valid. gunakan +,-,*,atau /.")
    if len(args) <2:
        print("dibutuhkan setidaknya dua angka untuk operasi aritmatika")

    result = args[0]

    for i in range(1, len(args)):
        if operator == '+':
            result += args[i]
        elif operator == '-':
            result -= args[i]
        elif operator == '*':
            result *= args[i]
        elif operator == '/':
            if args[i] ==0:
                print ("Pembagian oleh nol tidak diizinkan") 
            result /= args[i]

        return result
