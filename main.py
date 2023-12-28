import streamlit as st
import pandas as pd
st.set_page_config(page_title="Rota Tavsiye", layout="wide")


df = pd.read_excel("25.12.2023.deneme.xlsx")

st.header(" :red[Tatil Rotası] Belirlerken Adım Adım Rehber")
tab_home, tab_write, tab_model = st.tabs(["Ana Sayfa", "Gezi Rehberi", "Nereye Gitsem"])


columns_1, columns_2 = tab_home.columns(2)

#TAB_HOME
columns_1.markdown("""Tatil planlamak, bazen büyük bir heyecan ve eğlence kaynağı olabilirken aynı zamanda seçenekler arasında kayboladabilirsin.
Farklı tatil tercihleri, kişisel ilgi alanları ve yaşam tarzları, herkesin kendine özgü bir tatil deneyimi arayışını beraberinde getiriyor. Tatilini 
macera dolu bir kaçamak, tarihi bir keşif, dinlendirici bir sahil molası veya farklı kültürlerin zengin mutfağını keşfetmek için tercih edebilirisin. 
Ancak bazen, bu zengin seçenekler karşısında hangi destinasyonu seçeceğin konusunda kararsız da kalabilirsin.
İşte tam bu noktada,bu sitede sunulan öneriler, sana ilgi alanların ve tercihleri doğrultusunda kişiselleştirilmiş öneriler sunarak, tatil planlama 
sürecini kolaylaştırıyor. Doğada olmak istersen sakin bir dağ kaçamağı yada paraşüt deneyimi, bir şehrin geçmişini keşfetmek istersen tarih dolu bir 
yolculuk veya sakin, dinlendirici bir tatil istersen tropikal bir cennet önerilebilir. Tatil öneri sistemi, sana tercihlerin üzerinden kişiselleştirilmiş 
öneriler sunarak, tatil kararını kolaylaştırır. Bu platform üzerinden, kendineen uygun tatil deneyimini seçerken bir yandan da yeni yerler keşfetme şansına 
sahip olursun. Bu tatil öneri sistemi, tatil planlama sürecini daha keyifli bir hale getirerek, nereye gitsem diye düşünürken kararsızlık anlarında bile en 
iyi tatil deneyimini yaşama fırsatı sunar. Hayalini kurduğun tatilin kapılarını aralamak için bu sistemi kullanarak, unutulmaz bir kaçışa adım atabilirsiniz.""")

# Dosya yolu
image_path = "media/1.jpg"
# Dosyayı göster
columns_2.image(image_path, use_column_width=True)

#TAB_WRİTE


columns_a, columns_b, columns_c, columns_d = tab_write.columns(4)

#columns_a 1. yazı
columns_a.subheader("Almanya'nın masalsı kasabası: Monschau")
image_path = "media/monschau.jpg"
columns_a.image(image_path, use_column_width=True)
columns_a.markdown("Ortaçağ'dan kalma ve çağının özelliklerini yansıtan kasaba, yarı ahşap evleri, arnavut kaldırımlı dar sokakları, yemyeşil doğasıyla, bulunduğu Eifel bölgesinin en popüler seyahat rotalarından biri. Özellikle yürüyüş ve bisiklet tutkunlarını mutlu eden kasabanın çevresindeki yürüyüş parkurları ve bisiklet yollarında, mevsiminde nergis çiçeklerinin kokusu, kayın ormanlarının heybeti ziyaretçilerine eşlik ediyor.")

#2. yazı
columns_a.subheader("İstanbul'dan kopamayanlara baharı karşılamak için ATATÜRK ARBORETUMU")
image_path = "media/Ataturk-Arboretumu.jpg"
columns_a.image(image_path, use_column_width=True)
columns_a.markdown("Kent hayatından sıkılıp baharda doğaya kaçmak istiyor ama işten, güçten dolayı şehir dışına çıkamıyorsanız doğru adres Sarıyer. 1949’dan beri bu güzelliğin farkında olan İstanbullular nefes almak için burayı tercih ediyor. Göller, bitkiler, ördekler, kazlar, sukaplumbağaları... Ağaçlar ve çiçekler arasında yürüyüş yapmak harika.")

#columns_b yazı 1
columns_b.subheader("Bu sene yeni yılda nereye gitsek ? Avrupa’nın en güzel Noel Pazarları")
image_path = "media/noel.jpg"
columns_b.image(image_path, use_column_width=True)
columns_b.markdown("Yeni yılın yaklaşmasıyla birlikte birçok Avrupa kentinde ışıl ışıl renkli ve bir o kadar da canlı Noel pazarları kurulmaya başladı. Eğlencenin, yemeğin ve alışverişin zirveye çıktığı pazarlar arasında yüzlerce yıldır aynı yerde kurulanı da var, etkileyici şovlara ev sahipliği yapanı da. Yılın ilk günlerini karşılamak için süslenmiş, coşku dolu şehirlerde yeni yıla girmek unutulmaz bir deneyime dönüşebilir.")

#columns_b yazı 2
columns_b.subheader("Parkın içinde bir bir şehir: Kiev")
image_path = "media/kiev.jpg"
columns_b.image(image_path, use_column_width=True)
columns_b.markdown("Dünyaca tanınan mimari yapıtları, keyifli bahçeleri, yemyeşil ve büyük parkları ile insanı büyüleyen bir şehir Kiev. Goethe'nin parkın içindeki şehir olarak anlattığı Kiev kimilerinin unutulmaz anılar biriktirdiği kimilerinin ise tarihi yapılarına hayran kaldığı muazzam şehir.")

#columns_c yazı 1
columns_c.subheader("Özgün kültür, bin yıllık tapınaklar; Siem Reap")
image_path = "media/siem_reap.jpg"
columns_c.image(image_path, use_column_width=True)
columns_c.markdown("10 yıl öncesine kadar Siem Reap, 12’nci yüzyıldan kalma Angkor Wat Tapınakları’nı görmek için gidenlerin konakladığı, yemek yediği sıradan bir yerleşimdi. Şimdi modern otelleri, iddialı restoranları, sanat galerileri, fotoğraf ve film festivalleri, özgün ürünlerin satıldığı mağazalarıyla başlı başına bir çekim merkezi.")

#columns_c yazı 2
columns_c.subheader("Doğanın ışıkla dansı, görsel şölen Kuzey Işıkları...")
image_path = "media/lotofen.jpg"
columns_c.image(image_path, use_column_width=True)
columns_c.markdown("Başta Jules Verne olmak üzere yazarlar ve ressamlara ilham olan Lofoten Adaları'nın en güzel özelliklerinden birinin Kuzey Kutup Daire’sine yakın olması nedeniyle oluşan Gece yarısı güneşi olduğu biliniyor. Gece yarısı güneşi sonucu ortaya çıkan manzarayı seyretmenin keyfi ise eşsiz! Aynı zamanda bu manzara karşısında kayaking, balık tutma, bisiklet sürme gibi aktiviteler yapabilir ya da sadece bu güzel manzarayı izleyebilirsiniz.")


#columns_d yazı 1
columns_d.subheader("Dünyanın En Renkli Festivali; Holi Festivali")
image_path = "media/holi.jpg"
columns_d.image(image_path, use_column_width=True)
columns_d.markdown("Dünyanın en renkli ve eğlenceli festivallerinden biri olan Holi Festivali (Holi Fest) yani Renklerin Festivali, baharın gelişini kutlayan, çok renkliliği ve yeniden doğuşu simgeleyen bir Hinduizm renk festivali. Havanın ısınmasının, doğanın uykusundan uyanmasının, bitkilerin tomurcuklanıp çiçeklenmesinin müjdecisi olarak kutlanıyor. Holi festivalinin en eğlenceli kısmı ise halkın rengârenk toprak boyaları önce yüzlerine sürüp sonra etrafındakilerin üzerine atıyor olması.")

#columns_d yazı 2
columns_d.subheader("Kışın bir başka karlar altında Kopenhag")
image_path = "media/kopenhag.jpg"
columns_d.image(image_path, use_column_width=True)
columns_d.markdown("Bu şehri kışın ziyaret edeceksen huzurlu ve refah dolu bu kenti kışın ziyaret etmenin keyfi bir başka. Kopenhag’ın en güzel yerlerinden biri olan Kastelette. Yıldız şeklindeki yapısı ise ve Ortaçağ Kaleleri gibi etrafını dolduran iki kat hendeği, yemyeşil çevresi ve içindeki kiremit rengi binaları ile Andersen Masalları’ndan fırlamış gibi.")
#tab_model

def tavsiye_sistemi():

    # Tatil tipi seçimi
    Tatil_tipi_options = ["Alışveriş", "Gastronomik", "Romantik", "Festival", "Kültürel", "Gece Hayatı", "Deniz Kum Güneş", "Doğa Macera"]
    Tatil_tipi = tab_model.selectbox("Hangi tatil tipini tercih edersiniz?: ", Tatil_tipi_options).strip()

    # Kıta seçimi
    kıta_options = ["Asya", "Avrupa", "Güney Amerika", "Kuzey Amerika", "Afrika"]
    kıta = tab_model.selectbox("Hangi kıtada tatil yapmak istersiniz?: ", kıta_options).strip()

    # Veri setinde filtreleme
    filtre = (df['Tatil_tipi'] == Tatil_tipi) & (df['kıta'] == kıta)
    uygun_ülkeler = df.loc[filtre, 'ülke'].unique()

    if uygun_ülkeler.size == 0:
        tab_model.warning("Üzgünüz, bu kriterlere uygun bir öneri bulunamadı.")
    else:
        tab_model.success("İşte sizin için önerilen ülkeler:")
        tab_model.success(uygun_ülkeler)

        # Ülke seçimi
        seçilen_ülke = tab_model.selectbox("Hangi ülkede tatil yapmak istersiniz? (Yukarıdaki listeden birini seçin): ", uygun_ülkeler).strip()

        if tab_model.button("Tavsiye Göster"):
         if seçilen_ülke in uygun_ülkeler:
            # Şehir ve Açıklama getirme
            bilgiler = df.loc[(df['Tatil_tipi'] == Tatil_tipi) & (df['kıta'] == kıta) & (df['ülke'] == seçilen_ülke), ['Şehir', 'Açıklama']]

            if not bilgiler.empty:
                tab_model.write(f"{seçilen_ülke} unutulmaz bir tatile ne dersiniz?")
                # Tüm şehirleri ve ilgili açıklamaları ekrana yazdır
                for index, row in bilgiler.iterrows():
                    tab_model.write(f"Şehir: {row['Şehir']}")
                    tab_model.write("Açıklama:")
                    tab_model.write(row['Açıklama'])
                    tab_model.write("-----")

            else:
                tab_model.warning(f"Üzgünüz, {seçilen_ülke} için {Tatil_tipi} tatili ile ilgili bilgi bulunamadı.")


if __name__ == '__main__':
    tab_model.subheader('Tatil Tavsiye Uygulaması')
    tavsiye_sistemi()





############# nott hepisini eski haline al satır başına  if tab_.... sil









