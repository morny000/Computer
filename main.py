import sqlite3

print("Добро пожаловать")
print("Выберите процессор по id")
con = sqlite3.connect('computer')
cur = con.cursor()
query = "SELECT *" \
        "FROM cpu "
cur.execute(query)
for cpu in cur.fetchall():
   print(f"id: {cpu[0]}, name: {cpu[1]}, Сокет: {cpu[2]}, Память: {cpu[3]}, Энергопотребление: {cpu[4]}, Графическое ядро: {cpu[5]}, Максимальная температура: {cpu[6]}, Цена: {cpu[7]}")
cpu_id = input("Введите id: ")

print("Выберите материнскую плату")
query = "SELECT Socket " \
        "FROM cpu " \
        "WHERE id = ?"
cur.execute(query, (cpu_id, ))
socket_ = cur.fetchone()[0]

query = "SELECT *" \
        "FROM mother_plate " \
        "WHERE Socket=?"
cur.execute(query,(socket_ ,))
for mother_plate in cur.fetchall():
    print(f"id: {mother_plate[0]}, Название:  {mother_plate[1]}, Сокет: {mother_plate[2]}), Память: {mother_plate[3]}),Тип памяти: {mother_plate[4]}),Количество слотов памяти:{mother_plate[5]}),Разъем питнаия процесса:{mother_plate[6]})PCI-Express:{mother_plate[7]}, Цена: {mother_plate[8]}")
motherplate_id = input("Введите id: ")
for mother_plate in cur.fetchall():
        print(f"{mother_plate}")

print("Выберите видеокарту")
query = "SELECT PCI_Express " \
    "FROM mother_plate " \
    "WHERE id = ?"
cur.execute(query, (motherplate_id, ))
socket_ = cur.fetchone()[0]

query = "SELECT *" \
        "FROM video_card " \
        "WHERE PCI_Express=?"
cur.execute(query,(socket_ ,))
for video_card in cur.fetchall():
    print(f"id: {video_card[0]}, Название:  {video_card[1]}, Рекомендованный источник питания: {video_card[2]}), Размер: {video_card[3]}),PCI-Express: {video_card[4]}),Цена: {video_card[5]}")
video_card_id = input("Введите id: ")
for video_card in cur.fetchall():
        print(f"{video_card}")


print("Выберите жесткий диск ")
query = "SELECT *" \
        "From hdd" \

cur.execute(query)
for hdd in cur.fetchall():
        print(f"id: {hdd[0]}, name: {hdd[1]}), Эноргопотребленеие: {hdd[2]}),Скорость передача данных: {hdd[3]}), Стоимсоть: {hdd[4]}")
hdd_id = input("Введите id: ")
for hdd in cur.fetchall():
        print(f"{hdd}")


print("Выберите блок питания")
query = "SELECT * " \
        "From [power unit]"

cur.execute(query)
for power_unit in cur.fetchall():
   print(f"id: {power_unit[0]},name: {power_unit[1]}, Энергия {power_unit[3]},Разьемы питания видеокарты {power_unit[4]},форм-фактор {power_unit[5]}, подключение процесса {power_unit[6]},цена {power_unit[7]}")
powerunit_id = input("Введите id: ")
for power_unit in cur.fetchall():
        print(f"{power_unit}")