print("Elliptic Curve General Form:\t y^2 mod n=(x^3  + a*x + b)mod n\nEnter 'n':")
import numpy as geek

def polynomial(LHS, RHS, n):
    for i in range(0, n):
        LHS[0].append(i)
        RHS[0].append(i)
        LHS[1].append((i * i * i + a * i + b) % n)
        RHS[1].append((i * i) % n)


def points_generate(arr_x, arr_y, n):
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            if (LHS[1][i] == RHS[1][j]):
                count += 1
                arr_x.append(LHS[0][i])
                arr_y.append(RHS[0][j])
    return count


# main
n = 193 #Bilangan Prima
LHS = [[]]
RHS = [[]]
LHS.append([])
RHS.append([])
a = 3
print("Enter value of 'a':", a)
b = 1
print("Enter value of 'b':", b)
# Polynomial
polynomial(LHS, RHS, n)

arr_x = []
arr_y = []
# Generating base points
count = points_generate(arr_x, arr_y, n)

# Print Generated Points
print("Generated points are:")
for i in range(0, count):
    print(i + 1, " (", arr_x[i], ",", arr_y[i], ")\n")

# Calculation of Base Point
bx = arr_x[5]
by = arr_y[0]
print("Titik Kurva Awal:\t(", bx, ",", by, ")\n")

print("Enter the random number 'd' i.e. Private key of Sender (d<n):")
d = int(input())
print("Private Key untuk penerima : ", d )
if (d >= n):
    print("'d' harus lebih kecil woy 'n'.")
else:
    # Q i.e. sender's public key generation
    Qx = d * bx
    Qy = d * by
    print("Public key :\t(", Qx, ",", Qy, ")\n")

    # Encrytion
    k = d
    if (k >= n):
        print("'k' harus lebih kecil 'n'")
    else:

        # Cipher text 1 generation
        C1x = k * Qx
        C1y = k * Qy
        print("Titik KKP (Titik Enkripsi) :\t(", C1x, ",", C1y, ")\n")

        # Cipher text 2 generation
        C2x = k * bx
        C2y = k * by
        print("Titik KP (Titik Dekripsi) :\t(", C2x, ",", C2y, ")\n")

        ### Enkripsi titik KP ###
        Et1 = chr(C2x)
        Et2 = chr(C2y)
        print("Enkripsi titik KP =\t(", Et1, ",", Et2, ")\n")

        ### Enkripsi Titik KKP ####
        Ek = C1x
        print("Titik Absis KKP = ", Ek)
        Eb = [bin(Ek)[2:].zfill(8)]
        Ebb= ','.join(Eb)
        print("Titik Absis KKP dalam biner = ",Eb)

        ### Masukan PlainText ###
        print("Enter the message to be sent:\n")
        B = str(input())

        ## Merubah Ke Integer ##
        In = [ord(c) for c in B]
        print(In)

        ## Merubah Ke Biner ##
        Bi = [bin(x) [2:].zfill(8) for x in In]
        Bii= ','.join(Bi)
        print(Bii)

        ## Melakukan XOR Pada Titik Absis KKP ##
        data = Bii
        key = Ebb


        #### Melakukan XOR ####4

        in_arr1 = In
        in_arr2 = [Ek]

        print("Input array1 : ", in_arr1)
        print("Input array2 : ", in_arr2)

        out_arr = geek.bitwise_xor(in_arr1, in_arr2)
        print("Output array after bitwise_xor: ", out_arr)

        Ekb = [bin(x)[2:].zfill(8) for x in out_arr]
        print("Hasil Xor Binner =",Ekb)

        ###### Chiper Text #######
        Dekripsi_xor = ''.join([chr(int(x, 2)) for x in Ekb])
        print("Hasil Xor =" ,Dekripsi_xor)


        ##### Enkripsi Plaintext + Header #####
        q= Et1
        w= Et2
        e= Dekripsi_xor
        t= '#'
        z= q+t+w+t+e
        print("Hasil ENKRIPSI =",z)

########################################################################################################################
        print("========================== PROSES DEKRIPSI PESAN TERENKRIPSI ==========================================")
        ##### Dekripsi Pemisahan Header#####
        Dz=z[4:]
        print("Chiper yang sudah di hilangkan headernya=", Dz)

        ###### DEKRIPSI ENKRIPSI #######
        bz = [ord(c) for c in Dz]
        print(bz)
        ###### INTEGER KE BINER #######
        bzi = [bin(x)[2:].zfill(8) for x in bz]
        print(bzi)

        ###### Titik kP ######
        Kt1= k*C2x
        Kt2= k*C2y
        print("Titik KP (Titik Dekripsi) :\t(", Kt1, ",", Kt2, ")\n")

        ### Enkripsi Titik KKP ####
        Edt = Kt1
        print("Titik Absis KKP = ", Edt)
        Edtb = [bin(Edt)[2:].zfill(8)]
        Edtbb = ','.join(Edtb)
        print("Titik Absis KKP dalam biner = ", Edtbb)

        #### Melakukan XOR ####4

        Dek_arr1 = bz
        Dek_arr2 = [Edt]

        print("Input array1 : ", Dek_arr1)
        print("Input array2 : ", Dek_arr2)

        Fin_arr = geek.bitwise_xor(Dek_arr1, Dek_arr2)
        print("Output array after bitwise_xor: ", Fin_arr)

        Pl = [bin(x)[2:].zfill(8) for x in Fin_arr]
        print("Hasil Xor Binner =",Pl)

        ###### Menjadikan Plaintext #######
        Plaintex_ecc = ''.join([chr(int(x, 2)) for x in Pl])
        print("text asli adalah =",Plaintex_ecc)