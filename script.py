from selenium import webdriver

# Inisialisasi WebDriver (menggunakan Chrome sebagai contoh)
driver = webdriver.Chrome(executable_path='path_to_chromedriver.exe')

try:
    # Buka situs Tokopedia
    driver.get("https://www.tokopedia.com/")

    # Cari elemen input pencarian dan kirimkan ID transaksi
    search_box = driver.find_element_by_id("search-box")
    search_box.send_keys("01023A9AC")
    search_box.submit()

    # Tunggu hingga halaman transaksi dimuat sepenuhnya (gantilah dengan waktu yang sesuai)
    driver.implicitly_wait(10)

    # Ekstrak informasi dari UI
    trx_id_ui = driver.find_element_by_css_selector(".trx-id").text
    seller_name_ui = driver.find_element_by_css_selector(".seller-name").text
    delivery_service_ui = driver.find_element_by_css_selector(".delivery-service").text
    date_order_ui = driver.find_element_by_css_selector(".date-order").text
    address_ship_ui = driver.find_element_by_css_selector(".address-ship").text

    # Kueri database untuk mendapatkan data yang sesuai berdasarkan TRX_ID
    import your_database_library

    # Gantilah dengan kueri sesuai dengan basis data Anda
    database_data = your_database_library.query("SELECT TRX_ID, SELLER_NAME, DELIVERY_SERVICE, DATE_ORDER, ADDRESS_SHIP FROM transactions WHERE TRX_ID = '01023A9AC'")

    # Ekstrak data dari hasil kueri database
    trx_id_db = database_data[0]
    seller_name_db = database_data[1]
    delivery_service_db = database_data[2]
    date_order_db = database_data[3]
    address_ship_db = database_data[4]

    # Bandingkan data dari UI dengan data dari database
    assert trx_id_ui == trx_id_db, "Transaction ID mismatch between UI and database."
    assert seller_name_ui == seller_name_db, "Seller name mismatch between UI and database."
    assert delivery_service_ui == delivery_service_db, "Delivery service mismatch between UI and database."
    assert date_order_ui == date_order_db, "Date of order mismatch between UI and database."
    assert address_ship_ui == address_ship_db, "Address of shipment mismatch between UI and database."

    print("Test case passed: Data matches between UI and database.")

except Exception as e:
    print("Test case failed:", str(e))

finally:
    # Tutup WebDriver
    driver.quit()
