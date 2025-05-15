# Data booking awal Reservasi Lapangan
booking_data = {
    "id_booking": ["B001", "B002", "B003", "B004", "B005"],
    "nama_pemesan": ["Tim A", "Tim B", "Tim C", "Tim D", "Tim E"],
    "no_telp": ["080000000001", "080000000002", "080000000003", "080000000004", "080000000005"],
    "lapangan": ["Lapangan 1", "Lapangan 2", "Lapangan 3", "Lapangan 1", "Lapangan 4"],
    "jam_mulai": [18, 17, 22, 21, 2],
    "jam_selesai": [20, 19, 1, 23, 4]
}

lapangan_tersedia = ["Lapangan 1", "Lapangan 2", "Lapangan 3", "Lapangan 4"]
jam_operasional = list(range(16, 24)) + list(range(0, 4))

def check_overlap(lapangan, jam_mulai, jam_selesai, skip_index=None):
    if jam_selesai <= jam_mulai:
        jam_range = list(range(jam_mulai, 24)) + list(range(0, jam_selesai))
    else:
        jam_range = list(range(jam_mulai, jam_selesai))
    for i in range(len(booking_data["id_booking"])):
        if skip_index is not None and i == skip_index:
            continue
        if booking_data["lapangan"][i] != lapangan:
            continue
        start = booking_data["jam_mulai"][i]
        end = booking_data["jam_selesai"][i]
        booked_range = list(range(start, 24)) + list(range(0, end)) if end <= start else list(range(start, end))
        if any(jam in booked_range for jam in jam_range):
            return True
    return False

def generate_availability():
    tabel = {jam: {lap: "✅" for lap in lapangan_tersedia} for jam in jam_operasional}
    for i in range(len(booking_data["id_booking"])):
        lapangan = booking_data["lapangan"][i]
        jam_mulai = booking_data["jam_mulai"][i] % 24
        jam_selesai = booking_data["jam_selesai"][i] % 24
        if jam_selesai <= jam_mulai:
            jam_range = list(range(jam_mulai, 24)) + list(range(0, jam_selesai))
        else:
            jam_range = list(range(jam_mulai, jam_selesai))
        for jam in jam_range:
            if jam in tabel and lapangan in tabel[jam]:
                tabel[jam][lapangan] = f"❌{booking_data['id_booking'][i]}"
    return tabel

def show_availability():
    tabel = generate_availability()
    print("\nTABEL KETERSEDIAAN LAPANGAN")
    
    col_width = 18
    header = f"{'Jam':<11}" + "".join(f"{lap:^{col_width}}" for lap in lapangan_tersedia)
    print(header)
    print("-" * len(header))

    for jam in jam_operasional:

        jam_end = (jam + 1) % 24
        jam_str = f"{jam:02}:00-{jam_end:02}:00"
        row = f"{jam_str:<11}"

        for lap in lapangan_tersedia:
            status = tabel[jam][lap]
            row += f"{status:^{col_width}}"
        print(row)


def show_bookings():
    print("\nDATA BOOKING")
    header = f"{'ID':<6} {'Pemesan':<15} {'Lapangan':<12} {'Jam Booking':<15} {'No. Telp':<15}"
    print(header)
    print("-" * len(header))

    for i in range(len(booking_data["id_booking"])):
        jam_mulai = booking_data["jam_mulai"][i]
        jam_selesai = booking_data["jam_selesai"][i]
        jam_str = f"{jam_mulai:02}:00-{jam_selesai:02}:00"

        print(
            f"{booking_data['id_booking'][i]:<6} "
            f"{booking_data['nama_pemesan'][i]:<15} "
            f"{booking_data['lapangan'][i]:<12} "
            f"{jam_str:<15} "
            f"{booking_data['no_telp'][i]:<15}"
        )


def add_booking():
    show_availability()
    show_bookings()
    print("\nTAMBAH BOOKING BARU")
    last_id = int(booking_data["id_booking"][-1][1:])
    new_id = f"B{last_id + 1:03d}"
    while True:
        nama = input("Nama Pemesan: ").strip()
        if any(nama.lower() == existing.lower() for existing in booking_data["nama_pemesan"]):
            print("Nama pemesan sudah ada. Gunakan nama yang berbeda.")
        elif not nama:
            print("Nama tidak boleh kosong.")
        else:
            break
    no_telp = input("No. Telepon: ").strip()
    print("\nPilih Lapangan:")
    for i, lap in enumerate(lapangan_tersedia, 1):
        print(f"{i}. {lap}")
    pilihan = int(input("Pilihan: ")) - 1
    lapangan = lapangan_tersedia[pilihan]
    while True:
        jam_mulai = int(input("Jam Mulai (16-23 atau 0-4): ")) % 24
        jam_selesai = int(input("Jam Selesai (16-23 atau 0-4): ")) % 24
        if not check_overlap(lapangan, jam_mulai, jam_selesai):
            break
        else:
            print("Jadwal bentrok dengan booking lain. Silakan pilih jam lain.")
    print("\nPreview Booking:")
    print(f"ID       : {new_id}")
    print(f"Nama     : {nama}")
    print(f"No. Telp : {no_telp}")
    print(f"Lapangan : {lapangan}")
    print(f"Jam      : {jam_mulai:02d}:00 - {jam_selesai:02d}:00")
    confirm = input("Konfirmasi booking ini? (Y/N): ").strip().lower()
    if confirm == 'y':
        booking_data["id_booking"].append(new_id)
        booking_data["nama_pemesan"].append(nama)
        booking_data["no_telp"].append(no_telp)
        booking_data["lapangan"].append(lapangan)
        booking_data["jam_mulai"].append(jam_mulai)
        booking_data["jam_selesai"].append(jam_selesai)
        print("Booking berhasil ditambahkan.")
    else:
        print("Booking dibatalkan.")

def update_booking():
    show_availability()
    show_bookings()
    id_edit = input("\nMasukkan ID booking yang akan diupdate: ")
    try:
        idx = booking_data["id_booking"].index(id_edit)
    except ValueError:
        print("ID tidak ditemukan!")
        return
    print("\nKosongkan input jika tidak ingin mengubah")
    while True:
        nama_baru = input(f"Nama Pemesan ({booking_data['nama_pemesan'][idx]}): ").strip()
        if nama_baru and any(nama_baru.lower() == existing.lower() and i != idx for i, existing in enumerate(booking_data["nama_pemesan"])):
            print("Nama pemesan sudah ada. Gunakan nama yang berbeda.")
        else:
            break
    if nama_baru:
        booking_data["nama_pemesan"][idx] = nama_baru
    no_telp_baru = input(f"No. Telp ({booking_data['no_telp'][idx]}): ").strip()
    if no_telp_baru:
        booking_data["no_telp"][idx] = no_telp_baru
    print("\nPilih Lapangan:")
    for i, lap in enumerate(lapangan_tersedia, 1):
        print(f"{i}. {lap}")
    pilihan = input(f"Pilihan ({booking_data['lapangan'][idx]}): ").strip()
    if pilihan:
        booking_data["lapangan"][idx] = lapangan_tersedia[int(pilihan)-1]
    jm = input(f"Jam Mulai ({booking_data['jam_mulai'][idx]}): ").strip()
    js = input(f"Jam Selesai ({booking_data['jam_selesai'][idx]}): ").strip()
    if jm:
        booking_data["jam_mulai"][idx] = int(jm) % 24
    if js:
        booking_data["jam_selesai"][idx] = int(js) % 24
    lapangan = booking_data["lapangan"][idx]
    jam_mulai = booking_data["jam_mulai"][idx]
    jam_selesai = booking_data["jam_selesai"][idx]
    if check_overlap(lapangan, jam_mulai, jam_selesai, skip_index=idx):
        print("Update ditolak! Jadwal bentrok dengan booking lain.")
        return
    confirm = input("Simpan perubahan? (Y/N): ").strip().lower()
    if confirm == 'y':
        print("Data berhasil diperbarui!")
    else:
        print("Update dibatalkan.")

def delete_booking():
    show_availability()
    show_bookings()
    id_hapus = input("\nMasukkan ID booking yang akan dihapus: ")
    try:
        idx = booking_data["id_booking"].index(id_hapus)
    except ValueError:
        print("ID tidak ditemukan!")
        return
    print(f"Anda akan menghapus booking {booking_data['id_booking'][idx]} milik {booking_data['nama_pemesan'][idx]}")
    confirm = input("Yakin ingin menghapus? (Y/N): ").strip().lower()
    if confirm == 'y':
        for key in booking_data:
            booking_data[key].pop(idx)
        print(f"Booking {id_hapus} berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

def main_menu():
    while True:
        print("\n=== SISTEM BOOKING LAPANGAN ===")
        print("1. Tampilkan Ketersediaan & Booking")
        print("2. Tambah Reservasi")
        print("3. Update Reservasi")
        print("4. Hapus Reservasi")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            show_availability()
            show_bookings()
        elif pilihan == "2":
            add_booking()
        elif pilihan == "3":
            update_booking()
        elif pilihan == "4":
            delete_booking()
        elif pilihan == "5":
            keluar = input("Yakin ingin keluar? (Y/N): ").strip().lower()
            if keluar == 'y':
                print("Terima kasih! Program selesai.")
                break
        else:
            print("Pilihan tidak valid!")

main_menu()
