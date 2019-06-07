# Sütunları Tek Bir Sütun Altında Toparlama

**Pandas ile Sütünlara Yazılmış Yılları Tek Sütunda Toplama**

Elimizde İstanbul ve Ankaraya ait yıl bazlı bir veri setimiz var. 

Veri setimiz: **Şehir Adı, Şehir Plaka, yıl ve bu yıllara ait değerlerden** meydana gelmektedir.

Yapısı itibariyle her yıl bilgileri sütunlarda verilmiş. Ve görüntüsü aşağıdaki gibi.

![Resim](https://github.com/furkantolgayuce/Data-Preparation-Notes/blob/master/Pandas/S%C3%BCtunlar%C4%B1%20Tek%20Bir%20S%C3%BCtun%20Alt%C4%B1nda%20Toparlama/img/veriseti_1.png)

Biz verisetimizi bu formata getirmek istiyoruz.

![Resim](https://github.com/furkantolgayuce/Data-Preparation-Notes/blob/master/Pandas/S%C3%BCtunlar%C4%B1%20Tek%20Bir%20S%C3%BCtun%20Alt%C4%B1nda%20Toparlama/img/veriseti_2.png)

Görüldüğü gibi **Yıl ve Değer** Adında iki sütun oluşturuyoruz ve *sütunlardaki yılları ve onlara karşılık gelen değerleri* **satır** bazlı saklıyoruz.

Bunu yaparken her yıl için şehir bilgisini de çoğaltıyoruz.
