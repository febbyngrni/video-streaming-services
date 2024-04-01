### Python Project:
# Video Streaming Services

Project ini merupakan final project dari course **Basic Python Programming** Pacmann. Pada project ini, saya diminta untuk membuat suatu program sederhana untuk platform video streaming, PacFlix. Terdapat 3 plan pada PacFlix, yaitu Basic Plan, Standard Plan dan Premium Plan. Setiap plan memiliki benefit dan harga yang berbeda-beda seperti di bawah ini:

![Screenshot 2024-04-01 075352](https://github.com/febbyngrni/video-streaming-services/assets/152588325/22945abd-0666-4ef5-bafa-84535bbb9083)

## Objective
Membuat fitur dimana user dapat melakukan:
1. Mengecek semua plan yang tersedia di PacFlix
2. Mengecek plan yang sedang digunakan oleh **existing user**
3. **Current user**: Dapat upgrade plan dari current plan, jika **duration plan > 12 bulan** akan mendapatkan diskon
4. **New user**: Dapat subscribe dan mendapatkan diskon, jika menggunakan **kode referral**

## Discount
Terdapat 2 ketentuan untuk mendapatkan diskon untuk current user maupun new user:
1. Jika user yang memiliki duration plan > 12 bulan dan ingin upgrade plan maka akan mendapatkan diskon sebesar 5%.
2. Jika user baru yang ingin berlangganan memiliki kode referral dan cocok dengan data yang ada di database, maka pembayaran akan valid dan mendapatkan diskon sebesar 4%.
