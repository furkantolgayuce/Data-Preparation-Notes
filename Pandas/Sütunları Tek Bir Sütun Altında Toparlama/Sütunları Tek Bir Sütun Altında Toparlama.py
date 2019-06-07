# Kütüphanelerin Yüklenmesi
import pandas as pd

# Tablomuzu Oluşturalım.
d = {"Şehirler": ["İstanbul", "Ankara"],"Şehir Plaka": ["34", "06"],'2017': [1, 2],'2018': [3, 4], '2019': [5, 6]}

# DataFrame oluşturalım.
df = pd.DataFrame(data=d)

# Çıktı olarak alacağımız DataFrame.
df_yeni=pd.DataFrame()

# Sihirli Kodlar.
for col in df.iloc[:,2:]:
    df_baz = df.iloc[:,:2]
    df_baz["Yıl"] = col
    df_baz["Değer"] = df[col]
    df_yeni = pd.concat([df_yeni,df_baz],ignore_index=True)

print(df_yeni)

