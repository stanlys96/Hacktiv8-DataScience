'''
=================================================
Graded Challenge 1

Nama  : Stanly Sukmajaya
Batch : RMT-036

Program ini dibuat untuk melacak barang-barang apa yang sudah dibeli, lengkap dengan fitur 
penambahan barang, penampilan barang dan penghapusan barang 
=================================================
'''

class CartItem:
  '''
  Class ini dibuat untuk membuat object item, sebagai barang yang akan dimasukkan di Shopping Cart
  '''

  def __init__(self, nama, harga):
    '''
    Fungsi ini ditujukan untuk menginisialisasi class CartItem, dan memberikannya nama dan harga

    Contoh penggunaan:
    apel = CartItem("Apel", 5000)
    '''
    self.nama = nama
    self.harga = harga

class ShoppingCart:
  '''
  Class ini dibuat untuk membuat object shopping cart, sebagai keranjang yang akan digunakan untuk menampung
  data-data CartItem
  '''

  def __init__(self):
    '''
    Fungsi ini ditujukan untuk menginisialisasi class ShoppingCart

    Contoh penggunaan:
    keranjang = ShoppingCart()
    '''
    self.shopping_cart = []

  def add_cart(self, new_item):
    '''
    Fungsi ini ditujukan untuk memasukkan item ke dalam shopping_cart

    Contoh penggunaan:
    keranjang.add_cart(new_item)
    '''
    self.shopping_cart.append(new_item)

  def remove_cart(self, nama) -> bool:
    '''
    Fungsi ini ditujukan untuk memasukkan item ke dalam shopping_cart dan akan return nilai boolean

    Contoh penggunaan:
    hapus_cart = keranjang.remove_cart(item_to_remove)
    '''
    found = False
    for index, item in enumerate(self.shopping_cart):
      if item.nama.lower() == nama.lower():
        self.shopping_cart.pop(index)
        found = True
        break
    return found

  def show_cart(self):
    '''
    Fungsi ini ditujukan untuk menampilkan semua nama dan harga barang yang telah ditambahkan ke shopping_cart

    Contoh penggunaan:
    keranjang.show_cart()
    '''
    print("Barang di Keranjang:")
    for index, item in enumerate(self.shopping_cart):
      print(f"{index}. {item.nama.capitalize()} - Rp {item.harga}.00{"\n" if index == len(self.shopping_cart) - 1 else ""}")

  def calculate_total_price(self) -> int:
    '''
    Fungsi ini ditujukan untuk mengkalkulasi total harga barang yang telah ditambahkan ke shopping_cart
    dan akan return nilai int

    Contoh penggunaan:
    result = keranjang.calculate_total_price()
    '''
    result = 0
    for item in self.shopping_cart:
      int_item = 0
      try:
        int_item = int(item.harga)
      except:
        pass
      result += int_item
    return result

  def reset_cart(self):
    '''
    Fungsi ini ditujukan untuk me-reset data shopping_cart menjadi kosong seperti awal inisialisasi

    Contoh penggunaan:
    keranjang.reset_cart()
    '''
    self.shopping_cart = []

def main():
  '''
  Fungsi ini ditujukan memulai program penambahan CartItem kedalam ShoppingCart

  Contoh penggunaan: (lakukan di terminal)
  python stanly_app.py 
  '''
  
  pilihan = '''Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: '''

  input_text = f'''
Selamat Datang di Keranjang Belanja Toko Makmur!

{pilihan}'''
  keranjang = ShoppingCart()
  first_input = input(input_text)
  while first_input != "5":
    if first_input == "1":
      barang_input = input("Masukkan nama barang: ")
      harga_input = input("Masukkan harga: ")
      current_item = CartItem(barang_input, harga_input)
      keranjang.add_cart(current_item)
      print(f'\nBarang "{barang_input.capitalize()}" berhasil dimasukkan ke keranjang.\n')
    elif first_input == "2":
      if len(keranjang.shopping_cart) > 0:
        barang_input = input("Masukkan nama barang yang ingin dihapus: ")
        hapus_cart = keranjang.remove_cart(barang_input)
        if hapus_cart:
          print(f'Barang "{barang_input.capitalize()}" berhasil dihapus di keranjang belanja.\n')
        else:
          print(f"\nBarang {barang_input.capitalize()} tidak ada di keranjang.\n")
      else:
        print("Belum ada barang yang ada di keranjang.\n")
    elif first_input == "3":
      if len(keranjang.shopping_cart) == 0:
        print("\nBelum ada barang di keranjang.\n")
      else:
        keranjang.show_cart()
    elif first_input == "4":
      result = keranjang.calculate_total_price()
      print(f"Total belanja: Rp {result}.00\n")
    else:
      print("Pilihannya salah. Coba lagi ya.\n")
    first_input = input(pilihan)
  else:
    print("\nSampai Jumpa! Terima kasih sudah belanja di Toko Makmur.")

if __name__ == "__main__":
  main()