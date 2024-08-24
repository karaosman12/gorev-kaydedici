import json

# Dosya adını tanımla
FILENAME = 'tasks.json'

def load_tasks():
    """Görevleri dosyadan yükle"""
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Görevleri dosyaya kaydet"""
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Görevleri ekrana yazdır"""
    if not tasks:
        print("Görev listeniz boş.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✘"
            print(f"{index}. [{status}] {task['task']}")

def add_task(tasks):
    """Yeni görev ekle"""
    task_text = input("Yeni görev nedir? ")
    tasks.append({"task": task_text, "completed": False})
    print("Görev eklendi!")

def complete_task(tasks):
    """Görev tamamlama"""
    display_tasks(tasks)
    task_index = int(input("Tamamlanan görevin numarasını girin: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print("Görev tamamlandı!")
    else:
        print("Geçersiz görev numarası.")

def delete_task(tasks):
    """Görev silme"""
    display_tasks(tasks)
    task_index = int(input("Silmek istediğiniz görevin numarasını girin: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Görev silindi!")
    else:
        print("Geçersiz görev numarası.")

def main():
    tasks = load_tasks()

    while True:
        print("\nGörev Listesi Uygulaması")
        print("1. Görevleri Görüntüle")
        print("2. Yeni Görev Ekle")
        print("3. Görevi Tamamla")
        print("4. Görev Sil")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Değişiklikler kaydedildi. Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
