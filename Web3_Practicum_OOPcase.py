
# Araç sınıfına göre gişeden geçiş sırasında yapılacak ödeme miktarları (KGM sitesinden alınmıştır).

otomobil_ucret = 8.25
otobus_ucret = 23.25
minibus_ucret = 10.75


# Gişe superclassı
class Gise:
    kazanc = 0             #gişenin toplam cirosu.
    hgs_no_list = []       #HGS numaralarının tutulduğu liste.

    def bilgiler(self):    #Kullanıcı tarafından atanan objenin sahip olduğu bilgiler ve geçiş hakkındaki tüm bilgilerin yazdırıldığı fonksiyon.

        print(f"Araç sahibi: {self.isim, self.soyisim}\n")
        print(f"Aracın HGS numarası: {self.hgs_no}\n")
        print(f"Aracın geçiş yaptığı tarih ve saat: {self.tarih, self.saat}\n")
        print(f"Aracın sınıfı: {self.type}\n")

        if self.bakiye < 0:
            print("\nBAKİYENİZ EKSİDEDİR, LÜTFEN BORCUNUZU EN KISA SÜREDE ÖDEYİNİZ.\n")

        print(f"Aracın Bakiyesi: {self.bakiye}\n")
        print(f"ödenen mikar: {self.ucret}\n")

    # Geçiş ve ödeme fonksiyonu.

    def gecis_odeme(self):

        gecis_list = []
        gecis_list.append(self.tarih)
        gecis_list.append(self.saat)

        self.bakiye -= self.ucret
        Gise.kazanc += self.ucret

        print(f"Mevcut bakiye: {self.bakiye}")
        print(f"Ödenen miktar: {self.ucret}")

        self.kayit.append(gecis_list)
        self.yapilan_gecis += 1


class Otomobil(Gise):            #Otomobil Child classı

    def __init__(self):
        self.isim, self.soyisim = map(str, input("Araç sahibinin adını soyadını giriniz: \n").split())
        self.hgs_no = int(input("Aracın HGS numarasını giriniz: \n"))
        Gise.hgs_no_list.append(self.hgs_no)
        self.type = "1. Sınıf: Otomobil"
        self.bakiye = float(input("Aracın mevcut bakiyesini giriniz: \n"))
        self.ucret = otomobil_ucret
        self.tarih = input("Geçiş yapılan tarihi giriniz\n")
        self.saat = input("Geçiş yapılan saati giriniz\n")
        self.kayit = []
        self.yapilan_gecis = 0

        super(Otomobil, self).__init__()


class Minibus(Gise):             #Minibüs Child classı

    def __init__(self):
        self.isim, self.soyisim = map(str, input("Araç sahibinin adını soyadını giriniz: \n").split())
        self.hgs_no = Gise.hgs_no_list.append(int(input("Aracın HGS numarasını giriniz: \n")))
        self.type = "2. Sınıf: Minibüs"
        self.bakiye = float(input("Aracın mevcut bakiyesini giriniz: \n"))
        self.ucret = minibus_ucret
        self.tarih = input("Geçiş yapılan tarihi giriniz\n")
        self.saat = input("Geçiş yapılan saati giriniz\n")
        self.kayit = []
        self.yapilan_gecis = 0

        super(Minibus, self).__init__()


class Otobus(Gise):               #Otobüs Child classı

    def __init__(self):
        self.isim, self.soyisim = map(str, input("Araç sahibinin adını soyadını giriniz: \n").split())
        self.hgs_no = Gise.hgs_no_list.append(int(input("Aracın HGS numarasını giriniz: \n")))
        self.type = "3. Sınıf: Otobüs"
        self.bakiye = float(input("Aracın mevcut bakiyesini giriniz: \n"))
        self.ucret = otobus_ucret
        self.tarih = input("Geçiş yapılan tarihi giriniz\n")
        self.saat = input("Geçiş yapılan saati giriniz\n")
        self.kayit = []
        self.yapilan_gecis = 0

        super(Otobus, self).__init__()


"""Raporlama sistemi. Kullanıcı tarafından tuşlanan rakama göre aracın hangi sınıfa ait olduğu tespit ediliyor ve buna göre
Child class olan otomobil, otobüs veya minibüs çağırılıp obje tanımlanıyor.
Gişe Parent classında bulunan gecis_odeme fonksiyonu çağırılıyor.
gecis_sayac ile geçen araç sayısı sayılıyor ve buna göre araç listesine(arac_list) bir index olarak gelip gecis_odeme fonksiyonun argümanı oluyor.
"""
arac_list = []
gecis_sayaci = 0
tuslama = '1'

while tuslama == '1' or '2' or '3':

    tuslama = input(
        "\n *****\nHGS arayüzüne hoş geldiniz.\n******\n \n Otomobil için '1'\n Minibüs için '2'\n Otobüs için '3'\n Çıkış için ise herhangi bir şey tuşlayınız.\n")

    if tuslama == '1':
        arac_list.append(Otomobil())
        Gise.gecis_odeme(arac_list[gecis_sayaci])
        gecis_sayaci += 1

    elif tuslama == '2':
        arac_list.append(Minibus())
        Gise.gecis_odeme(arac_list[gecis_sayaci])
        gecis_sayaci += 1

    elif tuslama == '3':
        arac_list.append(Otobus())
        Gise.gecis_odeme(arac_list[gecis_sayaci])
        gecis_sayaci += 1

    else:
        print("\n*****\nSistemden çıkış yapılıyor.\n*****\n")
        break

# Sisteme kaydedilen araçların detaylı bilgisi arayüze bastırılıyor ve gişenin o sırada sisteme kaydedilen araçlara göre kazancı, günlük cirosu, bastırılıyor.

for i in range(gecis_sayaci):
    print(f"\nSİSTEMDEKİ {i + 1}. ARACIN SAHİP OLDUĞU BİLGİLER: \n")
    Gise.bilgiler(arac_list[i])

print(f"\n*****\nGişenin Kazancı: {Gise.kazanc}\n*****\n")
print("\nİyi Günler.\n")
print("\nSİSTEMDEN ÇIKIŞ YAPILIYOR...\n")