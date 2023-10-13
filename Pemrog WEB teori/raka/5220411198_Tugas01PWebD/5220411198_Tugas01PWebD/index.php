<!DOCTYPE html>
<html>

<head>
    <title>Profil</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400&display=swap');

        body {
            background-image: url('1169180.jpg');
            /* Menggunakan gambar sebagai background body */
            background-size: cover;
            /* Mengisi area dengan gambar */
            background-position: center;
            /* Menengahkan gambar */
            background-attachment: fixed;
            /* Membuat gambar latar belakang tetap */
            font-family: "Raleway", sans-serif;
            /* Menggunakan font Raleway */
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            /* Memastikan body setidaknya memiliki tinggi sebesar viewport */
        }

        header {
            background-color: rgba(0, 0, 0, 0.7);
            /* Latar belakang header hitam dengan transparansi */
            color: white;
            text-align: center;
            padding: 20px;
        }

        nav a {
            text-decoration: none;
            color: #333;
        }

        section {
            flex-grow: 1;
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.7);
            /* Latar belakang section hitam dengan transparansi */
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            color: white;
            /* Mengubah warna teks di dalam section menjadi putih */
        }

        h1,
        h2 {
            text-align: center;
        }

        h2 {
            margin-bottom: 20px;
            /* Menambah jarak bawah antara h2 "About Me" dengan elemen berikutnya */
        }

        .profile {
            display: flex;
            align-items: center;
            font-family: "Noto Sans", sans-serif;
            /* Menggunakan font Noto Sans untuk class .profile */
            margin-top: 40px;
            /* Menurunkan posisi .profile ke bawah */
        }

        .profile img {
            max-width: 200px;
            height: auto;
            margin-right: 20px;
        }

        footer {
            text-align: center;
            background-color: rgba(0, 0, 0, 0.7);
            /* Latar belakang footer hitam dengan transparansi */
            color: white;
            /* Mengubah warna teks di dalam footer menjadi putih */
            padding: 10px;
        }
    </style>
</head>

<body>
    <header>
        <h1>Welcome to My Web Profile</h1>
    </header>

    <section>
        <h2>About Me</h2>
        <div class="profile">
            <img src="foto_saya.jpeg" alt="Foto Profil">
            <p>Halo nama saya Raka Esa Rasendriya. Saya berumur 20 tahun dan kuliah di Universitas Teknologi Yogyakarta dengan NIM 5220411198. Saya mengambil program studi Sarjana Informatika pada Fakultas Sains dan Teknologi.</p>
        </div>
    </section>
    <footer>
        <p>&copy; 2023 Profil Saya</p>
    </footer>
</body>

</html>