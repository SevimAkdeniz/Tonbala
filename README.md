# Tombala Oyunu

Bu proje, geleneksel tombala oyununu terminal üzerinde Python ile oynanabilir bir şekilde sunmaktadır. Oyun, 2-4 oyuncu arasında oynanabilir ve geleneksel tombala kurallarına sadık kalarak tasarlanmıştır.

## Projenin Amacı

Python ile çalışan bir terminal tabanlı tombala oyunu geliştirmek. Oyun, kartların rastgele oluşturulması, çinko ve tombala puanlarının hesaplanması ve sonunda kazananın belirlenmesini içerir. Bu proje, geleneksel tombala oyununu dijital ortamda deneyimlemek isteyen oyuncular için tasarlanmıştır.

---

## Özellikler

### Fonksiyonel Gereksinimler

1. **Oyuncu Ayarları**
   - Oyun, 2 ile 4 oyuncu arasında oynanabilir.
   - Oyuncu sayısı başlangıçta kullanıcıdan alınır.

2. **Tombala Kartları**
   - Kartlar, 1 ile 99 arasındaki sayılardan oluşur.
   - Her kartta rastgele seçilmiş 15 sayı bulunur.
   - Her oyuncunun kartı birbirinden farklıdır.

3. **Çinko ve Tombala Kuralları**
   - İlk çinkoyu yapan oyuncu 5 puan kazanır.
   - İkinci çinkoyu yapan oyuncu 5 puan kazanır.
   - Üçüncü çinkoyu yapan oyuncu 5 puan kazanır.
   - Tombala yapan oyuncu 15 puan kazanır.

4. **Puanlama**
   - Oyun sonunda oyuncuların toplam puanları hesaplanır.
   - Puanlar terminale sıralı olarak yazdırılır.

5. **Sayı Çekme**
   - Sayılar, 1 ile 99 arasında rastgele seçilir.
   - Çekilen sayı terminalde gösterilir.
   - Daha önce çekilmiş bir sayı tekrar seçilemez.

6. **Oyun Kuralları**
   - Çekilen sayılar oyuncuların kartlarında kontrol edilir.
   - Çinko ve tombala durumları takip edilir.
   - Oyun, bir oyuncu tombala yapana kadar devam eder.

---

### Performans Gereksinimleri
- Kartlar ve çekilen sayılar rastgele oluşturulur, bu nedenle oyun sonuçları her oynanışta değişkenlik gösterir.
- Oyun, tüm işlemleri eş zamanlı olarak terminalde gösterir.

### Kullanıcı Deneyimi Gereksinimleri
- Oyuncu sayısı başlangıçta kullanıcı tarafından terminal üzerinden seçilir.
- Çekilen her sayı şu formatta terminalde yazdırılır: `Çekilen Sayı: X`.
- Oyuncuların durumları (kart doluluk oranı ve çinkolar) terminalde düzenli olarak görüntülenir.

### Doğruluk ve Güvenilirlik
- Her oyuncunun kartları eşsizdir.
- Çekilen sayılar tekrarlanmaz.
- Çinko ve tombala puanları doğru şekilde hesaplanır.

---

## Oyun Akışı

1. Oyuncu sayısı kullanıcıdan alınır.
2. Her oyuncu için rastgele kartlar oluşturulur.
3. Sayılar rastgele çekilir ve terminalde gösterilir.
4. Çinko ve tombala durumları kontrol edilir.
5. Oyun sonunda puanlar sıralı şekilde terminale yazdırılır.
6. Oyun bitiş mesajı gösterilir.

---

## Kurulum ve Çalıştırma

1. Bu projeyi yerel makinenize klonlayın:
   ```bash
   git clone https://github.com/username/tombala-oyunu.git
