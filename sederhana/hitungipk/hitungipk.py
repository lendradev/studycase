def readFile(filename):
    # Mencoba membaca file
    file = open(filename, 'r')
    try:
        if file.readable():
            return file.read()
        else:
            return "File tidak dapat dibaca"
    finally:
        file.close()

def bacaFileData(filename: str):
    # Inisialisasi array kosong
    resultArray = []
    # Membaca file
    rawCSV = readFile(filename).split('\n')
    for baris in rawCSV:
        # Konversi menjadi array dari string dengan indikator ','
        resultArray.append(baris.split(','))

    # Menghapus baris pertama yang berisikan non data
    resultArray.pop(0)
    return resultArray

def extractSKS(data: list[str]):
    resultArray = []
    for baris in data[1:]:
        resultArray.append(int(baris[2]))
    return resultArray

def extractNilaiKualitas(data: list[str]):
    resultArray = []
    for baris in data:
        print(baris)
        resultArray.append(float(baris[5]))
    return resultArray

def dapatkanTotalSKS(data: list[int]):
    totalSKS = 0
    for sks in data:
        totalSKS += sks
    return totalSKS

def dapatkanTotalNilaiKualitas(data: list[float]):
    totalNilaiKualitas = 0
    for nilai in data:
        totalNilaiKualitas += nilai
    return totalNilaiKualitas


data = bacaFileData('data.csv')
hasil_akhir = dapatkanTotalNilaiKualitas(extractNilaiKualitas(data)) / dapatkanTotalSKS(extractSKS(data))
print(hasil_akhir)