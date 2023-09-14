"""
USE CASE

Suppose there was a transaction that had been done in tokopedia.com , the transaction id should be available 
on the screen alongside with the address of shipment, date of order, seller’s name, and delivery service 
(JNE/POS/REX/others). The transaction id (TRX_ID) should also be available on the database which 
again supposedly there was a simple table containing all the transaction data.

Apparently, the order 01023A9AC seems to have different Delivery Service on the UI and the database record. 
How do you, as automation test developers develop such test scenario so that this kind of error does not occur?
"""

"""
PENYELESAIAN

Untuk mencegah perbedaan antara tampilan UI dan catatan database untuk suatu 
transaksi seperti pesanan 01023A9AC, perlu dikembangkan skenario pengujian otomatis yang kuat.
disini saya akan membuat scenario pengujian berdasarkan dengan ilustrasi yang diberikan pada Use Case
Berikut adalah pendekatan langkah-demi-langkah untuk membuat skenario semacam itu:

"""

#Saya menggunakan Tools automatic testing Selenium Python.

""""
Scenario pengujiannya adalah
1. Mengambil data transaksi dengan TRX_ID 01023A9AC yang ditampilkan di UI
2. Mengambil data dari database dengan TRX_ID 01023A9AC
3. Kemudian bandingkan apakah data yang diambil dari tampilan UI sama dengan data
    yang ada di database.
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3

# Inisialisasi WebDriver (menggunakan Chrome sebagai contoh)
driver = webdriver.Chrome(executable_path='path_to_chromedriver.exe')

try:
    # Buka situs Tokopedia (misalkan disini langsung url langsung menuju kepada tampilan transaksinya)
    driver.get("https://www.tokopedia.com/")

    # Cari elemen input pencarian dan kirimkan ID transaksi (Misalkan ada tampilan search box-nya untuk mencari data transaksi)
    search_box = driver.find_element(By.ID,"search-box")
    search_box.send_keys("01023A9AC")
    search_box.submit()

    # Tunggu hingga halaman transaksi dimuat sepenuhnya
    driver.implicitly_wait(10)

    # Ekstrak informasi dari UI
    trx_id_ui = driver.find_element(By.CSS_SELECTOR,".trx-id").text
    seller_name_ui = driver.find_element(By.CSS_SELECTOR,".seller-name").text
    delivery_service_ui = driver.find_element(By.CSS_SELECTOR,".delivery-service").text
    date_order_ui = driver.find_element(By.CSS_SELECTOR,".date-order").text
    address_ship_ui = driver.find_element(By.CSS_SELECTOR,".address-ship").text

    # Kueri database untuk mendapatkan data yang sesuai berdasarkan TRX_ID
    # Misalkan disini nama database nya adalah tokped_trans.db

    # Mengambil data dari database berdasarkan TRX_ID
    def get_data_from_database(trx_id):
        try:
            # Membuka koneksi ke database SQLite
            conn = sqlite3.connect('tokped_trans.db')  

            # Membuat kursor
            cursor = conn.cursor()

            # Menjalankan kueri untuk mengambil data berdasarkan TRX_ID
            cursor.execute("SELECT TRX_ID, SELLER_NAME, DELIVERY_SERVICE, DATE_ORDER, ADDRESS_SHIP FROM transactions WHERE TRX_ID = ?", (trx_id,))
            
            # Mengambil hasil kueri
            data = cursor.fetchone()

            # Menutup kursor dan koneksi
            cursor.close()
            conn.close()

            return data

        except sqlite3.Error as e:
            print("Error saat mengambil data dari database:", e)
            return None

    # Mencari data dari database berdasarkan TRX_ID yang ditemukan di UI
    database_data = get_data_from_database(trx_id_ui)

    if database_data:
        trx_id_db, seller_name_db, delivery_service_db, date_order_db, address_ship_db = database_data

        # Membandingkan data dari UI dengan data dari database
        if (trx_id_ui == trx_id_db and
            seller_name_ui == seller_name_db and
            delivery_service_ui == delivery_service_db and
            date_order_ui == date_order_db and
            address_ship_ui == address_ship_db):
            print("Test case passed: Data matches between UI and database.")
        else:
            print("Test case failed: Data does not match between UI and database.")
    else:
        print("Test case failed: Data not found in the database.")

except Exception as e:
    print("Test case failed:", str(e))

finally:
    # Tutup WebDriver
    driver.quit()
