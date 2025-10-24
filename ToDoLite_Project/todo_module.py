# todo_module.py
tasks = []

def add_task(task):
    if not task:
        return "Error: Tugas tidak boleh kosong."
    tasks.append(task)
    return f"Tugas '{task}' berhasil ditambahkan."

def delete_task(index):
    if index < 0 or index >= len(tasks):
        return "Error: Indeks tidak valid."
    removed = tasks.pop(index)
    return f"Tugas '{removed}' berhasil dihapus."

def show_tasks():
    if not tasks:
        return "Daftar tugas kosong."
    return "\n".join([f"{i+1}. {t}" for i, t in enumerate(tasks)])