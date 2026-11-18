import json
import os
import datetime
import random
import string


with open ("data.json", "r") as file:
    produk = json.load(file)
with open ("riwayat.json", "r") as file:
    riwayat = json.load(file)

def buat_id(riwayat):
     while True:
          id_transaksi = "".join(random.choices(string.digits + string.ascii_letters, k = 5))
          if id_transaksi not in riwayat:
               return id_transaksi

def simpan_data(nama_dictionary, nama_file, indent = 4):
     with open (nama_file, "w") as file:
          json.dump(nama_dictionary, file, indent = indent)

def hitung_transaksi(harga_beli, harga_jual, jumlah):
     total_beli = harga_beli * jumlah
     total_jual = harga_jual * jumlah
     keuntungan = total_jual - total_beli
     return total_beli, total_jual, keuntungan

     
def semua_produk():
                                
           print(f"{"SEMUA PRODUK":^60}")
           for key, value in produk.items():
                    
                print(f"\nnama produk\t\t\t: {key} \nmodal\t\t\t\t: Rp.{value["harga_beli"]:,} /pcs\nharga jual\t\t\t: Rp.{value["harga_jual"]:,} /pcs \nstok\t\t\t\t: {value["stok"]}\nperubahan terakhir\t\t: {value["tanggal"]}")

                total_nilai_sebelum_penjualan = value["harga_beli"] * value["stok"]
                total_nilai_setelah_penjualan = value["harga_jual"] * value["stok"]
                keuntungan_per_pcs = value ["harga_jual"] - value ["harga_beli"]
                estimasi_keuntungan = total_nilai_setelah_penjualan - total_nilai_sebelum_penjualan
                print(f"total modal\t\t\t: Rp.{total_nilai_sebelum_penjualan:,} ({value["stok"]}) pcs ")
                print(f"total harga jual\t\t: Rp.{total_nilai_setelah_penjualan:,} ({value["stok"]}) pcs")
                print(f"keuntungan \t\t\t: Rp.{keuntungan_per_pcs:,} /pcs")            
                print(f"estimasi keuntungan\t\t: Rp.{estimasi_keuntungan:,} ({value["stok"]} pcs)")

    

def tambah_produk():

            print(f"{"TAMBAH PRODUK":^60}")
            while True:
           
               tambah_barang = input("tambah produk\t: ").strip().lower()
               if tambah_barang == "":
                   print("nama produk tidak boleh kosong")
               else:
                   print("nama produk valid")
                   break
               
            if tambah_barang not in produk:
              
              while True:

                try:
                    harga_beli = int(input("\nmodal\t\t: Rp."))
                    harga_jual = int(input("harga jual\t: Rp."))
                    stok = int(input("stok\t\t: "))
                except ValueError:
                    print("harga dan stok harus berupa angka")
                    continue
                    
                if harga_beli <= 0 :
                    print("modal harus lebih dari 0")
                elif harga_jual <= 0:
                    print("harga jual harus lebih dari 0")
                elif harga_jual <= harga_beli:
                     print("harga jual harus lebih tinggi dari modal")
                elif stok <= 0 :
                    print("stok harus lebih dari 0")
                       
                else:  
                    produk.update({tambah_barang: {
                        "harga_beli": harga_beli,
                        "harga_jual": harga_jual,
                        "stok": stok,
                        "tanggal": datetime.date.today().isoformat()                                                                     
                }})
                    print(f"{tambah_barang} berhasil di tambah")
                    simpan_data(produk, "data.json")
                    break
            else:
                print(f"{tambah_barang} sudah ada, tambahkan produk lain")


def ubah_harga():

            print(f"{"UBAH HARGA":^60}")
            for key,value in produk.items():
                print(f"\nproduk\t\t\t: {key}\nmodal\t\t\t: Rp.{value["harga_beli"]:,}\nharga jual\t\t: Rp.{value["harga_jual"]:,}\nperubahan terakhir\t: {value["tanggal"]}")

            perubahan_harga = input("\npilih produk\t\t: ").lower()
            if perubahan_harga in produk:

              while True:

                try:
                   update_harga_beli = int(input("\nupdate modal\t\t: Rp."))
                   update_harga_jual = int(input("update harga jual\t: Rp."))
                except ValueError:
                    print("harga harus berupa angka")
                    continue

                if update_harga_beli <= 0:
                    print("update modal harus lebih dari 0")
                elif update_harga_jual <= 0:
                    print("update harga jual harus lebih dari 0")
                elif update_harga_jual <= update_harga_beli:
                     print("harga jual harus lebih tinggi dari modal")
                else:
                    produk [perubahan_harga] ["harga_beli"] = update_harga_beli
                    produk [perubahan_harga] ["harga_jual"] = update_harga_jual
                    produk [perubahan_harga] ["tanggal"]    = datetime.date.today().isoformat()
                    print("update harga berhasil".center(30,"="))
                    print(f"\nmodal {perubahan_harga} menjadi\t: Rp.{produk [perubahan_harga]["harga_beli"]:,}")
                    print(f"harga jual {perubahan_harga} menjadi\t: Rp.{produk [perubahan_harga]["harga_jual"]:,}")
                    print(f"tanggal diubah\t\t: {datetime.date.today()}")

                    simpan_data(produk, "data.json")
                    break

            else:
                print(f"{perubahan_harga} tidak ditemukan")


def tambah_stok():

            print(f"{"TAMBAH STOK":^60}")

            for key, value in produk.items():
                print(f"\nproduk\t\t\t: {key}\nstok\t\t\t: {value["stok"]}\nperubahan terakhir\t: {value["tanggal"]}")

            barang = input("\npilih produk\t\t: ").lower()
            if barang in produk:

              while True:
                
                try:
                   penambahan_stok = int(input("tambah stok\t\t: "))
                except ValueError:
                   print("stok harus berupa angka")
                   continue

                if penambahan_stok <=0:
                    print("harus lebih dari 0")
                else:
                    produk [barang] ["stok"] += penambahan_stok
                    produk [barang] ["tanggal"] = datetime.date.today().isoformat()
                    print(f"{"-- TAMBAH STOK BERHASIL --":^60}")
                    print(f"\nstok {barang} menjadi\t: {produk[barang]["stok"]}")
                    print(f"tanggal ditambah\t\t: {datetime.date.today()}")
                    simpan_data(produk, "data.json")
                    break

            else:
                print(f"{barang} tidak ditemukan")



def kurangi_stok():

            print(f"{"KURANGI STOK":^60}")

            for key, value in produk.items():
                print(f"\nproduk\t\t\t: {key}\nstok\t\t\t: {value["stok"]}\nperubahan terakhir\t: {value["tanggal"]}")

            barang = input("\npilih produk\t\t: ").lower()
            if barang in produk:

              while True:

                try:
                   pengurangan_stok = int(input("kurangi stok\t\t: "))
                except ValueError:
                    print("stok harus berupa angka")
                    continue

                if pengurangan_stok <=0:
                    print("harus lebih dari 0")
                elif pengurangan_stok > produk [barang] ["stok"]:
                    print(f"stok {barang} tidak mencukupi!")
                else:
                    produk [barang] ["stok"] -= pengurangan_stok
                    produk [barang] ["tanggal"] = datetime.date.today().isoformat()
                    print(f"{"-- KURANGI STOK BERHASIL --":^}")
                    print(f"\nstok {barang} menjadi\t\t: {produk [barang]["stok"]}")
                    print(f"tanggal dikurangi\t: {datetime.date.today()}")
                    simpan_data(produk, "data.json")
                    break

            else:
                print(f"{barang} tidak ditemukan")


    

def cari_produk():

            print(f"{"CARI PRODUK":^60}")

            pencarian_produk = input("cari produk\t\t: ").lower()
            if pencarian_produk in produk:
                data = produk[pencarian_produk]
                estimasi_keuntungan = data["harga_jual"] - data["harga_beli"]
                print(f"produk\t\t\t: {pencarian_produk}\nmodal\t\t\t: Rp.{data["harga_beli"]:,}/pcs\nharga jual\t\t: Rp.{data["harga_jual"]:,}/pcs\nestimasi keuntungan\t: Rp.{estimasi_keuntungan:,}/pcs\nstok\t\t\t: {data["stok"]} pcs\npembaruan terakhir\t: {data["tanggal"]}")
            else:
                print(f"{pencarian_produk} tidak tersedia")

        

def hapus_produk():

            print(f"{"HAPUS PRODUK":^60}")

            for key, value in produk.items():
                 print(f"\nproduk\t\t\t: {key}\nstok\t\t\t: {value["stok"]}")
        
            penghapusan_produk = input("\nhapus produk\t: ").lower()
            if penghapusan_produk in produk:            
                del produk[penghapusan_produk]
                print(f"{penghapusan_produk} berhasil dihapus")
                simpan_data(produk, "data.json")           
            else:
                print(f"{penghapusan_produk} tidak ditemukan")


def penjualan():

            print(f"{"PENJUALAN":^60}")

            for key, value in produk.items():
                print(f"\nproduk\t\t\t: {key}\nstok\t\t\t: {value["stok"]}\nmodal\t\t\t: Rp.{value["harga_beli"]:,}/pcs\nharga jual\t\t: Rp.{value["harga_jual"]:,} /pcs")

            barang = input("\npilih produk\t\t: ").lower()
            if barang in produk:

              while True:

                try:            
                   pcs = int(input("input pcs\t\t: "))
                except ValueError:
                    print("pcs harus berupa angka")
                    continue

                if pcs <=0:
                    print("pcs harus lebih dari 0")            
                elif pcs > produk [barang] ["stok"]:
                    print(f"stok {barang} tidak cukup!")
                else:
                    produk [barang] ["stok"] -= pcs
                    produk [barang] ["tanggal"] = datetime.date.today().isoformat()

                    total_harga_beli, total_harga_jual, keuntungan = hitung_transaksi(produk[barang] ["harga_beli"], produk [barang] ["harga_jual"], pcs)
                    tanggal_terjual = datetime.date.today().isoformat()
                    print(f"{"-- PENJUALAN BERHASIL --":^60}")
                    print(f"\n{barang} terjual\t\t: {pcs} pcs\ntotal modal\t\t: Rp.{total_harga_beli:,} /{pcs} pcs\ntotal harga jual\t: Rp.{total_harga_jual:,} /{pcs} pcs\nkeuntungan\t\t: Rp.{keuntungan:,} /{pcs} pcs\ntanggal terjual\t\t: {tanggal_terjual}")

                    
                         
                    id_transaksi = buat_id(riwayat)
                                                 
                    riwayat.update({id_transaksi:{
                        "barang": barang,
                        "jumlah": pcs,
                        "total_harga_jual": total_harga_jual,
                        "keuntungan": keuntungan,
                        "tanggal_terjual": tanggal_terjual
                      }})

                    if produk [barang] ["stok"] <1:
                        print(f"\nstok {barang} habis!")
                        del produk [barang]
                    simpan_data(produk, "data.json")

                    simpan_data(riwayat, "riwayat.json")
                    break
        
            else:
                print(f"{barang} tidak ditemukan")



def riwayat_penjualan():

            print(f"{"RIWAYAT PENJUALAN":^60}")                  
            for id_transaksi, value in riwayat.items():
                 print(f"\nid transaksi\t\t: {id_transaksi}\nproduk\t\t\t: {value["barang"]}\njumlah\t\t\t: {value["jumlah"]} pcs\ntotal harga\t\t: Rp.{value["total_harga_jual"]:,}\nkeuntungan\t\t: Rp.{value["keuntungan"]:,}\ntanggal terjual\t\t: {value["tanggal_terjual"]}")


def statistik():


            jumlah_jenis_produk = len(produk)
            total_unit_produk = sum(value["stok"] for value in produk.values())
            total_modal = sum(value["harga_beli"] * value["stok"] for value in produk.values())
            total_harga_jual = sum(value["harga_jual"] * value["stok"] for value in produk.values())
            keuntungan = sum(value["keuntungan"] for value in riwayat.values())
            total_penjualan = sum(value["total_harga_jual"] for value in riwayat.values())

            print(f"{"STATISTIK TOKO":^60}")
            print(f"\njumlah jenis produk\t\t: {jumlah_jenis_produk} jenis")
            print(f"Total unit produk\t\t: {total_unit_produk} unit")
            print(f"Total modal\t\t\t: Rp.{total_modal:,}")
            print(f"Estimasi total penjualan\t: Rp.{total_harga_jual:,}")

            print(f"{"STATISTIK PENJUALAN":^60}")
            print(f"\ntotal penjualan\t\t\t: Rp.{total_penjualan:,}")
            print(f"Total keuntungan\t\t: Rp.{keuntungan:,}")

            # cari produk terlaris
            total_terjual = {} # mulai dengan dictionary kosong, belum ada transaksi yang di rekap

            for transaksi in riwayat.values():
                nama_item = transaksi ["barang"]
                jumlah_item = transaksi["jumlah"]
                total_terjual[nama_item] = (total_terjual.get(nama_item, 0) + jumlah_item)
            if total_terjual:
                terlaris = max(total_terjual, key=total_terjual.get)
                print(f"terlaris\t\t\t: {terlaris}, terjual {total_terjual[terlaris]} pcs")
            else:
                print("produk terlaris\t\t\t: belum ada penjualan")
            
            print("==================================================")

        
while True:
    print("\n")
    print(f"{"MANAJEMEN":^60}")
    print(f"{"STOK TOKO":^60}")
    print("-"*60)
    print("""1. Lihat produk
2. Tambah produk
3. Ubah harga
4. Tambah stok
5. Kurangi stok
6. Cari produk
7. Hapus produk
8. Penjualan
9. Riwayat penjualan
10. Statistik
11. keluar
""")

    menu = input("\ninput menu: ")
    os.system("cls")

    if menu == "1":
        semua_produk()
    elif menu == "2":
        tambah_produk()
    elif menu == "3":
        ubah_harga()
    elif menu == "4":
        tambah_stok()
    elif menu == "5":
        kurangi_stok()
    elif menu == "6":
        cari_produk()
    elif menu == "7":
        hapus_produk()
    elif menu == "8":
        penjualan()
    elif menu == "9":
        riwayat_penjualan()
    elif menu == "10":
        statistik()
    elif menu == "11":
        print(f"{"TERIMA KASIH":^60}")
        break
    else:
        print(f"{"MENU TIDAK VALID":^60}")

    