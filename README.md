# Soal test maggang Quality Assurance engineer

Berikut adalah soal/pertanyaan yang perlu dijawab oleh peserta

## knowledge base

1. Apa yang anda ketahui tentang Rest API?
2. Apa yang anda ketahui tentang Server side and Client side processing?
3. Apa yang anda ketahui tentang Monolith dan Microservices, berikan contohnya?
4. Apa yang anda ketahui tentang Automation testing serta sebutkan contohnya?
5. Dengan menggunakan tools automation testing tersebut, biasanya menggunakan bahasa/tools apa?

## Jawaban Knowledge base

1. intinya Rest API adalah antar muka yang memudahkan client untuk berkomunikasi atau request data ke server.
2. Server side processing adalah pemrosesan data yang terjadi di sisi server seperti pemrosesan permintaan client dan memberikan respon yang sesuai. Client side processing adalah pemrosesan yang terjadi di sisi client.
3. Monolith adalah pendekatan dalam pengembangan perangkat lunak di mana seluruh aplikasi dibangun sebagai satu kesatuan yang besar dengan codebase yang sama. Semua komponen dan modul berjalan di bawah satu atap tunggal. Contohnya adalah aplikasi e-commerce besar yang memiliki semua fitur, seperti manajemen produk, pembayaran, otentikasi, dan lainnya dalam satu kode sumber.
Microservices adalah pendekatan arsitektur perangkat lunak yang mengurai aplikasi besar menjadi serangkaian layanan yang lebih kecil dan independen dengan codebase yang terpisah - pisah. Setiap layanan memiliki tanggung jawab yang terpisah dan berkomunikasi melalui antarmuka yang didefinisikan. Sebagai contoh, dalam aplikasi e-commerce berbasis mikropelayanan, ada layanan terpisah untuk manajemen produk, pembayaran, otentikasi, dan mungkin banyak layanan lainnya, masing-masing dengan kemampuan uniknya.
4. Automation testing adalah metode testing perangkat lunak yang dijalankan secara otomatis dengan menggunakan script yang dibuat oleh tester, contohnya adalah pengujian fitur login yang scriptnya sudah dibuat menggunakan framework selenium.
5. Bila Selenium biasanya menggunakan bahasa Python. Namun selenium juga mendukung bahasa lainnya seperti Java dan C#.

## Use cases

Suppose there was a transaction that had been done in tokopedia.com , the transaction
id should be available on the screen alongside with the address of shipment, date of
order, seller’s name, and delivery service (JNE/POS/REX/others). 
The transaction id (TRX_ID) should also be available on the database which again supposedly there was a simple table containing all the transaction data.

![success notif](imgs/trx-notif.png)

![tabel transaksi](imgs/table-trx.png)

Apparently, the order `01023A9AC` seems to have different Delivery Service on the UI and the
database record. How do you, as automation test developers develop such test scenario so that
this kind of error does not occur?