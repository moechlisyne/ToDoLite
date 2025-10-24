# main.py
from todo_module import add_task, delete_task, show_tasks

def main():
    while True:
        print("\n=== ToDoLite App ===")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Lihat daftar tugas")
        print("4. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            task = input("Masukkan nama tugas: ")
            print(add_task(task))
        elif choice == "2":
            index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            print(delete_task(index))
        elif choice == "3":
            print(show_tasks())
        elif choice == "4":
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()