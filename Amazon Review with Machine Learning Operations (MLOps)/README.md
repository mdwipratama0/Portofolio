# Submission Machine Learning Operations (MLOps) Amazon Reviews Dataset

Nama: M. Dwi Pratama

Username Dicoding: mdpraz


| | Deskripsi |
| ----------- | ----------- |
| Dataset | Dataset yang digunakan dalam project ini dapat diakses pada laman [link](https://www.kaggle.com/datasets/thedevastator/amazon-product-reviews?select=test.csv) berikut ini|
| Masalah | Di zaman yang serba modern ini, banyak hal dapat dilakukan secara online termasuk dalam berbelanja. Online shop sudah sangat marak digunakan baik kaula muda maupun dewasa, kemudahan dalam proses transaksi membuat pengguna lebih suka untuk membeli suatu barang secara online. Dalam melakukan pembelian umumnya pengguna akan melihat review (ulasan) dari suatu barang sebelum memutuskan untuk membeli barang tersebut, tidak banyak juga ulasan manjadi suatu standar dalam membeli barang tersebut. Data tersebut kian semakin banyak dan terus tumbuh dan sulit untuk diidentifikasi karena proses yang berjalan secara real time. |
| Solusi machine learning | Oleh karena itu, diperlukannya suatu sistem yang dapat melakukan pemilahan secara otomatis dengan mengidentifikasi nilai dari suatu ulasan. Sistem ini bertujuan untuk membedakan antara ulasan yang baik dengan buruk, sehingga dapat membantu pengguna untuk dapat secara cepat mengetahui ulasan dari suatu produk yang akan dibeli. |
| Metode pengolahan | Pada data Amazon Reviews terdapat tiga feature, namun yang digunakan dalam project ini hanya feature label dan content.Fitur lainnya akan dihapus, kemudian dilakukan splitting pada data training dan evaluation dengan skema 90:10. |
| Arsitektur model | Arsitektur model yang digunakan yaitu deep neural network, yang terdiri dari dense 16 dan 8 menggunakan fungsi aktivasi ReLU dan Sigmoid karena terdiri dari dua kategori label. Loss yang digunakan untuk mengukur metriks yaitu Binary Crossentropy serta opimizer menggunakan Adam.|
| Metrik evaluasi | Metriks evaluasi yang digunakan untuk mengukur performa dari model yang dibuat yaitu Example COunt, AUC, Binary Accuracy, dan Confusion Matrix (TP,TN,FN,FP).|
| Performa model | Dari metriks evaluasi diperoleh nilai AUC sebesar 87% dengan ExampleCount sebanyak 1476 dan Binary Accuracy sebesar 80.1%. Untuk False Negative sebanyak 140, False Postive sebanyak 153, True Negative sebanyak 556, dan True Positive sebanyak 627.|
