all_constells = """
Andromeda (And) Андромеда
Antlia (Ant) Воздушный Насос
Apus (Aps) Райская Птица
Aquarius (Aqr) Водолей
Aquila (Aql) Орел
Ara (Ara) Жертвенник
Aries (Ari) Овен
Auriga (Aur) Возничий
Bootes (Boo) Волопас
Caelum (Cae) Резец
Camelopardis (Cam) Жираф
Cancer (Cnc) Рак
Canes_Venatici (CVn) Гончие Псы
Canis_Major (CMa) Большой Пес
Canis_Minor (CMi) Малый Пес
Capricornus (Cap) Козерог
Carina (Car) Киль
Cassiopea (Cas) Кассиопея
Centaurus (Cen) Центавр
Cepheus (Cep) Цефей
Cetus (Cet) Кит
Chamaeleon (Cha) Хамелеон
Circinus (Cir) Циркуль
Columba (Col) Голубь
Coma_Berenices (Com) Волосы Вероники
Corona_Australis (CrA) Южная Корона
Corona_Borealis (CrB) Северная Корона
Corvus (Crv) Ворон
Crater (Crt) Чаша
Crux (Cru) Южный Крест
Cygnus (Cyg) Лебедь
Delphinus (Del) Дельфин
Dorado (Dor) Золотая Рыба
Draco (Dra) Дракон
Equuleus (Equ) Малый Конь
Eridanus (Eri) Эридан
Fornax (For) Печь
Gemini (Gem) Близнецы
Grus (Gru) Журавль
Hercules (Her) Геркулес
Horologium (Hor) Часы
Hydra (Hya) Гидра
Hydrus (Hyi) Южный Змей
Indus (Ind) Индеец
Lacerta (Lac) Ящерица
Leo (Leo) Лев
Leo_Minor (LMi) Малый Лев
Lepus (Lep) Заяц
Libra (Lib) Весы
Lupus (Lup) Волк
Lynx (Lyn) Рысь
Lyra (Lyr) Лира
Mensa (Men) Столовая Гора
Microscopium (Mic) Микроскоп
Monoceros (Mon) Единорог
Musca (Mus) Муха
Norma (Nor) Наугольник
Octans (Oct) Октант
Ophiuchus (Oph) Змееносец
Orion (Ori) Орион
Pavo (Pav) Павлин
Pegasus (Peg) Пегас
Perseus (Per) Персей
Phoenix (Phe) Феникс
Pictor (Pic) Живописец
Pisces (Psc) Рыбы
Piscis_Austrinus (PsA) Южная Рыба
Puppis (Pup) Корма
Pyxis (Pyx) Компас
Reticulum (Ret) Сетка
Sagitta (Sge) Стрела
Sagittarius (Sgr) Стрелец
Scorpius (Sco) Скорпион
Sculptor (Scl) Скульптор
Scutum (Sct) Щит
Serpens (Ser) Змея
Sextans (Sex) Секстант
Taurus (Tau) Телец
Telescopium (Tel) Телескоп
Triangulum (Tri) Треугольник
Triangulum_Australe (TrA) Южный Треугольник
Tucana (Tuc) Тукан
Ursa_Major (UMa) Большая Медведица
Ursa_Minor (UMi) Малая Медведица
Vela (Vel) Паруса
Virgo (Vir) Дева
Volans (Vol) Летучая Рыба
Vulpecula (Vul) Лисичка
"""
# знаю, что два одинаковых стрипа в одном генераторе плохой тон, но вложенный писать лень)
constells_dict = {row.split(' ')[1][1:-1]: row.split(' ')[2]
                  for row in all_constells.strip().split('\n')}
