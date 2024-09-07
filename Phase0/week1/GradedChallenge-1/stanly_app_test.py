'''
=================================================
Graded Challenge 1

Nama  : Stanly Sukmajaya
Batch : RMT-036

Program ini dibuat untuk melakukan unit testing kepada program ShoppingCart yang sudah saya buat
=================================================
'''
import unittest
from stanly_app import CartItem, ShoppingCart

class ShoppingCartItemTest(unittest.TestCase):
  '''
  Class ini dibuat untuk melakukan unit testing ShoppingCart
  '''

  def test_init_cart(self):
    '''
    Fungsi ini ditujukan untuk testing bahwa shopping_cart pada saat di inisialisasi, memiliki 0 data,
    dan jika mengakses index pertama nya, akan di raise IndexError
    '''
    shopping_cart = ShoppingCart()
    self.assertEqual(len(shopping_cart.shopping_cart), 0)
    with self.assertRaises(IndexError):
      return shopping_cart.shopping_cart[0]

  def test_add_cart(self):
    '''
    Fungsi ini ditujukan untuk testing bahwa shopping_cart akan memiliki 1 data setelah ditambahkan 1 kali,
    dan nama dan harga yang di tambahkan sesuai dengan yang ada di list shopping_cart
    '''
    shopping_cart = ShoppingCart()
    current_item = CartItem("Apel", 5000)
    shopping_cart.add_cart(current_item)
    self.assertEqual(len(shopping_cart.shopping_cart), 1)
    self.assertEqual(shopping_cart.shopping_cart[0].nama, "Apel")
    self.assertEqual(shopping_cart.shopping_cart[0].harga, 5000)

  def test_remove_cart(self):
    '''
    Fungsi ini ditujukan untuk testing bahwa shopping_cart akan mengalami pengurangan data setelah di remove
    '''
    shopping_cart = ShoppingCart()
    current_item = CartItem("Apel", 5000)
    second_item = CartItem("Jeruk", 10000)
    shopping_cart.add_cart(current_item)
    shopping_cart.add_cart(second_item)
    shopping_cart.remove_cart("Apel")
    self.assertEqual(len(shopping_cart.shopping_cart), 1)
    shopping_cart.remove_cart("Jeruk")
    self.assertEqual(len(shopping_cart.shopping_cart), 0)

  def test_calculate_total_price(self):
    '''
    Fungsi ini ditujukan untuk testing bahwa total calculate price akan sesuai dengan total harga semua data
    yang telah ditambahkan ke shopping_cart
    '''
    shopping_cart = ShoppingCart()
    current_item = CartItem("Apel", 5000)
    second_item = CartItem("Jeruk", 10000)
    third_item = CartItem("Mangga", 15000)
    shopping_cart.add_cart(current_item)
    shopping_cart.add_cart(second_item)
    shopping_cart.add_cart(third_item)
    self.assertEqual(shopping_cart.calculate_total_price(), 30000)

if __name__ == "__main__":
  unittest.main()