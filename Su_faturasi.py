toplam_abone_say = 0
toplam_su_tuketimi = 0
toplam_su_tuketim_ucreti = 0
toplam_devlete_giden_tutar = 0
toplam_ilce_belediyesine_giden_tutar = 0
toplam_buyuksehir_belediyesine_giden_tutar = 0
toplam_IZSU_tutari = 0
indirim_durumu = 'a'
kademe1_toplam_su_tuketim_mik = 0
kademe2_toplam_su_tuketim_mik = 0
kademe3_toplam_su_tuketim_mik = 0
hane_sayisi = 0
ucreti_500den_kullanimi_100den_cok_olanlar = 0
max_resmi_daire_tuketim_miktari = 0
max_aylik_su_tuketim_ucreti = 0
max1_abone_no = 0
max2_abone_no = 0
aylik_konut_ort_su_tuketim_mik = 0
aylik_isyeri_ort_su_tuketim_mik = 0
aylik_resmi_daire_ort_su_tuketim_mik = 0
aylik_organize_sanayi_ort_su_tuketim_mik = 0
aylik_ilce_tar_hay_sulama_ort_su_tuketim_mik = 0
aylik_konut_tuketim_yuzdesi = 0
aylik_isyeri_tuketim_yuzdesi = 0
aylik_resmi_daire_tuketim_yuzdesi = 0
aylik_organize_sanayi_tuketim_yuzdesi = 0
aylik_ilce_tar_hay_sulama_tuketim_yuzdesi = 0
konut_abone_yuzdesi = 0
isyeri_abone_yuzdesi = 0
resmi_daire_abone_yuzdesi = 0
organize_sanayi_abone_yuzdesi = 0
ilce_tar_hay_sulama_abone_yuzdesi = 0
aylik_konut_su_tuketim_mik = 0
aylik_isyeri_su_tuketim_mik = 0
aylik_resmi_daire_su_tuketim_mik = 0
aylik_organize_sanayi_su_tuketim_mik = 0
aylik_ilce_tar_hay_sulama_su_tuketim_mik = 0
aylik_konut_su_tuketim_yuzdesi = 0
aylik_isyeri_su_tuketim_yuzdesi = 0
aylik_resmi_daire_su_tuketim_yuzdesi = 0
aylik_organize_sanayi_su_tuketim_yuzdesi = 0
aylik_ilce_tar_hay_sulama_su_tuketim_yuzdesi = 0
kademe1_yuzdesi = 0
kademe1_aylik_ort_tuketim_mik = 0
kademe2_yuzdesi = 0
kademe2_aylik_ort_tuketim_mik = 0
kademe3_yuzdesi = 0
kademe3_aylik_ort_tuketim_mik = 0
ilce_tar_hay_50_tondan_cok_kullananlarin_yuzdesi = 0
engelli_say = 0
sehit_gazi_sporcu_say = 0
aylik_ilce_tar_hay_sulama_su_tuketim_ucreti = 0
aylik_konut_su_tuketim_ucreti = 0
aylik_isyeri_su_tuketim_ucreti = 0
aylik_resmi_daire_su_tuketim_ucreti = 0
aylik_organize_sanayi_su_tuketim_ucreti = 0
sehit_gazi_veya_sporcu_engelli_olan_konut_say = 0
sehit_gazi_veya_sporcu_engelli_olan_konut_yuzdesi = 0
toplam_konut_su_tuketimi = 0
toplam_isyeri_su_tuketimi = 0
toplam_resmi_daire_su_tuketimi = 0
toplam_organize_sanayi_su_tuketimi = 0
toplam_ilce_tar_hay_sulama_su_tuketimi = 0
kademe1_konut_say = 0
kademe2_konut_say = 0
kademe3_konut_say = 0
tuketimi_50tondan_cok_olanlar = 0
toplam_konut_aylik_su_tuketim_ucreti = 0
toplam_isyeri_aylik_su_tuketim_ucreti = 0
toplam_resmi_daire_aylik_su_tuketim_ucreti = 0
toplam_organize_sanayi_aylik_su_tuketim_ucreti = 0
toplam_ilce_tar_hay_sulama_aylik_su_tuketim_ucreti = 0
konut_say = 0
isyeri_say = 0
resmi_daire_say = 0
organize_sanayi_say = 0
ilce_tar_hay_sulama_say = 0
while True:
    indirim_durumu_olanlar = 0
    abone_no = int(input("Abone no giriniz: "))
    abone_tipi_kodu = int(input("Abone tipi kodunu giriniz (konut i??in 1, i?? yeri i??in 2 ,resmi daire i??in 3, organize \
sanayi i??in 4, il??e tar??m ve hayvan sulama i??in 5 giriniz): "))
    while abone_tipi_kodu < 0 or abone_tipi_kodu > 6:
        abone_tipi_kodu = int(input("Yanl???? giri?? yapt??n??z! Abone tipi kodunu giriniz (konut i??in 1, i?? yeri i??in 2, \
resmi daire i??in 3, organize sanayi i??in 4, il??e tar??m ve hayvan sulama i??in 5 giriniz): "))
    if abone_tipi_kodu == 1:
        hane_sayisi = int(input("Hane say??s??n?? giriniz: "))
        while hane_sayisi < 1:
            hane_sayisi = int(input("Yanl???? giri?? yapt??n??z! Hane say??s??n?? giriniz: "))
        if hane_sayisi == 1:
            konut_say += 1
            indirim_durumu = input("??ndirim durumunu giriniz (Yoksa 'y' veya 'Y', varsa ve ??ehitse '??' veya '??',\
gaziyse 'g' veya 'G', sporcuysa 's' veya 'S', engelliyse 'e' veya 'E' giriniz): ")
            while indirim_durumu not in ('y', 'Y', 'g', 'G', '??', '??', 's', 'S', 'e', 'E'):
                indirim_durumu = input("??ndirim durumunu giriniz (Yoksa 'y' veya 'Y', varsa ve ??ehitse '??' veya '??',\
gaziyse 'g' veya 'G', sporcuysa 's' veya 'S', engelliyse 'e' veya 'E' giriniz): ")
        if hane_sayisi > 1:
            konut_say += hane_sayisi
            while True:
                sehit_say = int(input("Toplam ??ehit say??s??n?? giriniz: "))
                gazi_say = int(input("Toplam gazi say??s??n?? giriniz: "))
                sporcu_say = int(input("Toplam sporcu say??s??n?? giriniz: "))
                sehit_gazi_sporcu_say = sehit_say + gazi_say + sporcu_say
                while sehit_gazi_sporcu_say < 0 or sehit_gazi_sporcu_say > hane_sayisi:
                    print("Yanl???? giri?? yapt??n??z! L??tfen de??erleri tekrar giriniz.")
                    sehit_say = int(input("Toplam ??ehit say??s??n?? giriniz: "))
                    gazi_say = int(input("Toplam gazi say??s??n?? giriniz: "))
                    sporcu_say = int(input("Toplam sporcu say??s??n?? giriniz: "))
                indirim_durumu_olanlar += sehit_gazi_sporcu_say
                engelli_say = int(input("Toplam engelli say??s??n?? giriniz: "))
                while engelli_say < 0 or engelli_say > hane_sayisi:
                    engelli_say = int(input("Yanl???? giri?? yapt??n??z! Toplam engelli say??s??n?? giriniz: "))
                indirim_durumu_olanlar += engelli_say
                if not engelli_say + sehit_gazi_sporcu_say > hane_sayisi:
                    if sehit_say > 0 and  gazi_say > 0 or sporcu_say > 0 and engelli_say > 0:
                        sehit_gazi_veya_sporcu_engelli_olan_konut_say += 1
                        sehit_gazi_veya_sporcu_engelli_olan_konut_yuzdesi = \
                            sehit_gazi_veya_sporcu_engelli_olan_konut_say * 100 / konut_say
                    break
    onceki_sayac_degeri = int(input("??nceki saya?? de??erini giriniz: "))
    while onceki_sayac_degeri < 0:
        onceki_sayac_degeri = int(input("Yanl???? giri?? yapt??n??z! ??nceki saya?? de??erini giriniz: "))
    simdiki_sayac_degeri = int(input("??imdiki saya?? de??erini giriniz: "))
    while simdiki_sayac_degeri < onceki_sayac_degeri:
        simdiki_sayac_degeri = int(input("Yanl???? giri?? yapt??n??z! ??imdiki saya?? de??erini giriniz: "))
    kullanim_suresi = int(input("Kullan??m s??resini giriniz: "))
    while kullanim_suresi <= 0:
        kullanim_suresi = int(input("Yanl???? giri?? yapt??n??z! Kullan??m s??resini giriniz: "))
    donemlik_su_tuketimi = simdiki_sayac_degeri - onceki_sayac_degeri
    toplam_su_tuketimi += donemlik_su_tuketimi
    indirim_orani = 0
    KADEME1_SINIRI = kullanim_suresi * 13 / 30
    KADEME2_SINIRI = kullanim_suresi * 20 / 30
    kullanim_suresinin_aylik_degeri = kullanim_suresi / 30
    if abone_tipi_kodu == 1:
        toplam_abone_say += hane_sayisi
        konut_say += hane_sayisi
        hane_ortalamasi = donemlik_su_tuketimi / hane_sayisi
        abone_tipi_adi = "KONUT"
        toplam_konut_su_tuketimi += donemlik_su_tuketimi
        SU_TUKETIM_BIRIM_UCRETI_KADEME1 = 2.89
        ATIK_SU_BIRIM_UCRETI_KADEME1 = 1.44
        INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME1 = 1.445
        SU_TUKETIM_BIRIM_UCRETI_KADEME2 = 3.13
        ATIK_SU_BIRIM_UCRETI_KADEME2 = 1.56
        INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME2 = 1.565
        SU_TUKETIM_BIRIM_UCRETI_KADEME3 = 6.43
        ATIK_SU_BIRIM_UCRETI_KADEME3 = 3.22
        INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME3 = 3.215
        if hane_ortalamasi <= KADEME1_SINIRI:
            kademe1_konut_say += hane_sayisi
            kademe1_toplam_su_tuketim_mik += donemlik_su_tuketimi
            kademe1_yuzdesi = kademe1_konut_say * 100 / konut_say
            kademe1_aylik_ort_tuketim_mik = kademe1_toplam_su_tuketim_mik * kullanim_suresinin_aylik_degeri / \
                                            kademe1_konut_say
            su_tuketim_bedeli1 = (INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME1 * indirim_durumu_olanlar * hane_ortalamasi) \
                                 + (SU_TUKETIM_BIRIM_UCRETI_KADEME1 * hane_ortalamasi *
                                    (hane_sayisi - indirim_durumu_olanlar))
            donemlik_su_tuketim_bedeli = su_tuketim_bedeli1
            toplam_su_tuketim_ucreti += su_tuketim_bedeli1
            donemlik_atik_su_bedeli = ATIK_SU_BIRIM_UCRETI_KADEME1 * donemlik_su_tuketimi
            donemlik_toplam_su_bedeli = donemlik_su_tuketim_bedeli + donemlik_atik_su_bedeli
            aylik_konut_su_tuketim_ucreti = su_tuketim_bedeli1 * kullanim_suresinin_aylik_degeri
        elif hane_ortalamasi <= KADEME2_SINIRI:
            kademe2_konut_say += hane_sayisi
            kademe2_toplam_su_tuketim_mik += donemlik_su_tuketimi
            kademe2_yuzdesi = kademe2_konut_say * 100 / konut_say
            kademe2_aylik_ort_tuketim_mik = kademe2_toplam_su_tuketim_mik * kullanim_suresinin_aylik_degeri / \
                                            kademe2_konut_say
            su_tuketim_bedeli2 = (KADEME1_SINIRI * INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME1 * indirim_durumu_olanlar
                                  + KADEME1_SINIRI * SU_TUKETIM_BIRIM_UCRETI_KADEME1 *
                                  (hane_sayisi - indirim_durumu_olanlar) + (hane_ortalamasi - KADEME1_SINIRI) *
                                  SU_TUKETIM_BIRIM_UCRETI_KADEME2 * (hane_sayisi - indirim_durumu_olanlar) +
                                  INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME2 * indirim_durumu_olanlar *
                                  (hane_ortalamasi - KADEME1_SINIRI))
            donemlik_su_tuketim_bedeli = su_tuketim_bedeli2
            toplam_su_tuketim_ucreti += su_tuketim_bedeli2
            donemlik_atik_su_bedeli = KADEME1_SINIRI * ATIK_SU_BIRIM_UCRETI_KADEME1 + \
                                      (hane_ortalamasi - KADEME1_SINIRI) * ATIK_SU_BIRIM_UCRETI_KADEME2
            donemlik_toplam_su_bedeli = donemlik_su_tuketim_bedeli + donemlik_atik_su_bedeli
            aylik_konut_su_tuketim_ucreti = su_tuketim_bedeli2 * kullanim_suresinin_aylik_degeri

        else:
            kademe3_konut_say += hane_sayisi
            kademe3_toplam_su_tuketim_mik += donemlik_su_tuketimi
            kademe3_yuzdesi = kademe3_konut_say * 100 / konut_say
            kademe3_aylik_ort_tuketim_mik = kademe3_toplam_su_tuketim_mik * kullanim_suresinin_aylik_degeri / \
                                            kademe3_konut_say
            su_tuketim_bedeli3 = (KADEME1_SINIRI * INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME1 * indirim_durumu_olanlar
                                  + KADEME1_SINIRI * SU_TUKETIM_BIRIM_UCRETI_KADEME1 *
                                  (hane_sayisi - indirim_durumu_olanlar) + (KADEME2_SINIRI - KADEME1_SINIRI)
                                  * SU_TUKETIM_BIRIM_UCRETI_KADEME2 * (hane_sayisi - indirim_durumu_olanlar) *
                                  (KADEME2_SINIRI - KADEME1_SINIRI) * INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME2 *
                                  indirim_durumu_olanlar + INDIRIMLI_SU_TUKETIM_BIRIM_UCRETI_KADEME3 *
                                  sehit_gazi_sporcu_say * (hane_ortalamasi - KADEME2_SINIRI) +
                                  SU_TUKETIM_BIRIM_UCRETI_KADEME3 * (hane_ortalamasi - KADEME2_SINIRI)
                                  * (hane_sayisi - indirim_durumu_olanlar))
            donemlik_su_tuketim_bedeli = su_tuketim_bedeli3
            toplam_su_tuketim_ucreti += su_tuketim_bedeli3
            donemlik_atik_su_bedeli = (KADEME1_SINIRI * ATIK_SU_BIRIM_UCRETI_KADEME1 +
                                       (KADEME2_SINIRI - KADEME1_SINIRI) * ATIK_SU_BIRIM_UCRETI_KADEME2 +
                                       ATIK_SU_BIRIM_UCRETI_KADEME3 * (hane_ortalamasi - KADEME2_SINIRI))
            donemlik_toplam_su_bedeli = donemlik_su_tuketim_bedeli + donemlik_atik_su_bedeli
            aylik_konut_su_tuketim_ucreti = su_tuketim_bedeli3 * kullanim_suresinin_aylik_degeri
        toplam_konut_aylik_su_tuketim_ucreti += aylik_konut_su_tuketim_ucreti
        if aylik_konut_su_tuketim_ucreti > 500 or donemlik_su_tuketimi > 100:
            ucreti_500den_kullanimi_100den_cok_olanlar += 1
    elif abone_tipi_kodu == 2:
        abone_tipi_adi = "???? YER??"
        hane_sayisi = 1
        toplam_abone_say += 1
        isyeri_say += 1
        toplam_isyeri_su_tuketimi += donemlik_su_tuketimi
        SU_TUKETIM_BIRIM_UCRETI = 7.38
        ATIK_SU_BIRIM_UCRETI = 3.68
        donemlik_su_tuketim_bedeli = SU_TUKETIM_BIRIM_UCRETI * donemlik_su_tuketimi
        donemlik_atik_su_bedeli = ATIK_SU_BIRIM_UCRETI * donemlik_su_tuketimi
        donemlik_toplam_su_bedeli = donemlik_su_tuketim_bedeli + donemlik_atik_su_bedeli
        aylik_isyeri_su_tuketim_ucreti = donemlik_su_tuketim_bedeli * kullanim_suresinin_aylik_degeri
        toplam_isyeri_aylik_su_tuketim_ucreti += aylik_isyeri_su_tuketim_ucreti
        toplam_su_tuketim_ucreti += donemlik_su_tuketim_bedeli
        if aylik_isyeri_su_tuketim_ucreti > 500 or donemlik_su_tuketimi > 100:
            ucreti_500den_kullanimi_100den_cok_olanlar += 1
        if max_aylik_su_tuketim_ucreti < aylik_isyeri_su_tuketim_ucreti:
            max_aylik_su_tuketim_ucreti = aylik_isyeri_su_tuketim_ucreti
            max2_abone_no = abone_no
    elif abone_tipi_kodu == 3:
        abone_tipi_adi = "RESM?? DA??RE"
        toplam_abone_say += 1
        hane_sayisi = 1
        resmi_daire_say += 1
        toplam_resmi_daire_su_tuketimi += donemlik_su_tuketimi
        SU_TUKETIM_BIRIM_UCRETI = 4.34
        ATIK_SU_BIRIM_UCRETI = 2.16
        donemlik_su_tuketim_bedeli = SU_TUKETIM_BIRIM_UCRETI * donemlik_su_tuketimi
        donemlik_atik_su_bedeli = ATIK_SU_BIRIM_UCRETI * donemlik_su_tuketimi
        donemlik_toplam_su_bedeli = donemlik_su_tuketim_bedeli + donemlik_atik_su_bedeli
        aylik_resmi_daire_su_tuketim_ucreti = donemlik_su_tuketim_bedeli * kullanim_suresinin_aylik_degeri
        toplam_resmi_daire_aylik_su_tuketim_ucreti += aylik_resmi_daire_su_tuketim_ucreti
        toplam_su_tuketim_ucreti += donemlik_su_tuketim_bedeli
        if aylik_resmi_daire_su_tuketim_ucreti > 500 or donemlik_su_tuketimi > 100:
            ucreti_500den_kullanimi_100den_cok_olanlar += 1
        if max_aylik_su_tuketim_ucreti < aylik_resmi_daire_su_tuketim_ucreti:
            max_aylik_su_tuketim_ucreti = aylik_resmi_daire_su_tuketim_ucreti
            max2_abone_no = abone_no
    elif abone_tipi_kodu == 4:
        abone_tipi_adi = "ORGAN??ZE SANAY??"
        toplam_abone_say += 1
        hane_sayisi = 1
        organize_sanayi_say += 1
        toplam_organize_sanayi_su_tuketimi += donemlik_su_tuketimi
        SU_TUKETIM_BIRIM_UCRETI = 5.00
        ATIK_SU_BIRIM_UCRETI = 2.50
        donemlik_su_tuketim_bedeli = SU_TUKETIM_BIRIM_UCRETI * donemlik_su_tuketimi
        donemlik_atik_su_bedeli = ATIK_SU_BIRIM_UCRETI * donemlik_su_tuketimi
        donemlik_toplam_su_bedeli = donemlik_su_tuketim_bedeli + donemlik_atik_su_bedeli
        aylik_organize_sanayi_su_tuketim_ucreti = donemlik_su_tuketim_bedeli * kullanim_suresinin_aylik_degeri
        toplam_resmi_daire_aylik_su_tuketim_ucreti += aylik_organize_sanayi_su_tuketim_ucreti
        toplam_su_tuketim_ucreti += donemlik_su_tuketim_bedeli
        if aylik_organize_sanayi_su_tuketim_ucreti > 500 or donemlik_su_tuketimi > 100:
            ucreti_500den_kullanimi_100den_cok_olanlar += 1
        if max_aylik_su_tuketim_ucreti < aylik_organize_sanayi_su_tuketim_ucreti:
            max_aylik_su_tuketim_ucreti = aylik_organize_sanayi_su_tuketim_ucreti
            max2_abone_no = abone_no
    else:
        abone_tipi_adi = "??L??E TARIM VE HAYVAN SULAMA"
        toplam_abone_say += 1
        hane_sayisi = 1
        ilce_tar_hay_sulama_say += 1
        toplam_ilce_tar_hay_sulama_su_tuketimi += donemlik_su_tuketimi
        SU_TUKETIM_BIRIM_UCRETI_KADEME1 = 1.45
        ATIK_SU_BIRIM_UCRETI_KADEME1 = 0.72
        SU_TUKETIM_BIRIM_UCRETI_KADEME2 = 2.89
        ATIK_SU_BIRIM_UCRETI_KADEME2 = 1.44
        SU_TUKETIM_BIRIM_UCRETI_KADEME3 = 6.43
        ATIK_SU_BIRIM_UCRETI_KADEME3 = 3.22
        if donemlik_su_tuketimi <= KADEME1_SINIRI:
            donemlik_su_tuketim_bedeli = donemlik_su_tuketimi * SU_TUKETIM_BIRIM_UCRETI_KADEME1
            donemlik_atik_su_bedeli = donemlik_su_tuketimi * ATIK_SU_BIRIM_UCRETI_KADEME1
        elif donemlik_su_tuketimi <= KADEME2_SINIRI:
            donemlik_su_tuketim_bedeli = KADEME1_SINIRI * SU_TUKETIM_BIRIM_UCRETI_KADEME1 + \
                                         SU_TUKETIM_BIRIM_UCRETI_KADEME2 * (donemlik_su_tuketimi - KADEME1_SINIRI)
            donemlik_atik_su_bedeli = ATIK_SU_BIRIM_UCRETI_KADEME1 * KADEME1_SINIRI + \
                                      (donemlik_su_tuketimi - KADEME1_SINIRI)
        else:
            donemlik_su_tuketim_bedeli = KADEME1_SINIRI * SU_TUKETIM_BIRIM_UCRETI_KADEME1 + \
                                         (KADEME2_SINIRI - KADEME1_SINIRI) * SU_TUKETIM_BIRIM_UCRETI_KADEME2 + \
                                         (donemlik_su_tuketimi - KADEME2_SINIRI) * SU_TUKETIM_BIRIM_UCRETI_KADEME3
            donemlik_atik_su_bedeli = KADEME1_SINIRI * ATIK_SU_BIRIM_UCRETI_KADEME1 + \
                                      (KADEME2_SINIRI - KADEME1_SINIRI) * ATIK_SU_BIRIM_UCRETI_KADEME2 + \
                                      (donemlik_su_tuketimi - KADEME2_SINIRI) * ATIK_SU_BIRIM_UCRETI_KADEME3
        donemlik_toplam_su_bedeli = donemlik_su_tuketim_bedeli + donemlik_atik_su_bedeli
        aylik_ilce_tar_hay_sulama_su_tuketim_ucreti = donemlik_su_tuketim_bedeli * kullanim_suresinin_aylik_degeri
        toplam_ilce_tar_hay_sulama_aylik_su_tuketim_ucreti += aylik_ilce_tar_hay_sulama_su_tuketim_ucreti
        toplam_su_tuketim_ucreti += donemlik_su_tuketim_bedeli
        if aylik_ilce_tar_hay_sulama_su_tuketim_ucreti > 500 or donemlik_su_tuketimi > 100:
            ucreti_500den_kullanimi_100den_cok_olanlar += 1
        if max_aylik_su_tuketim_ucreti < aylik_ilce_tar_hay_sulama_su_tuketim_ucreti:
            max_aylik_su_tuketim_ucreti = aylik_ilce_tar_hay_sulama_su_tuketim_ucreti
            max2_abone_no = abone_no
        if donemlik_su_tuketimi > 50:
            tuketimi_50tondan_cok_olanlar += 1
    donemlik_CTV_ucreti = 0.39 * donemlik_su_tuketimi
    donemlik_kati_atik_bertaraf_ucreti = hane_sayisi * 2.54
    donemlik_kati_atik_toplama_bedeli = hane_sayisi * 13
    devlete_giden_KDV = (donemlik_kati_atik_bertaraf_ucreti + donemlik_kati_atik_toplama_bedeli +
                         donemlik_su_tuketim_bedeli) * 8 / 100
    toplam_devlete_giden_tutar += devlete_giden_KDV
    donemlik_toplam_fatura_tutari = (donemlik_kati_atik_bertaraf_ucreti + donemlik_kati_atik_toplama_bedeli +
                                     donemlik_toplam_su_bedeli + donemlik_CTV_ucreti + devlete_giden_KDV)
    ilce_belediyesine_giden_tutar = donemlik_CTV_ucreti + donemlik_kati_atik_toplama_bedeli
    toplam_ilce_belediyesine_giden_tutar += ilce_belediyesine_giden_tutar
    buyuksehir_belediyesine_giden_tutar = donemlik_kati_atik_bertaraf_ucreti
    toplam_buyuksehir_belediyesine_giden_tutar += buyuksehir_belediyesine_giden_tutar
    IZSU_payi = donemlik_toplam_su_bedeli
    toplam_IZSU_tutari += IZSU_payi
    print("Abone no: ", abone_no)
    print("Abone tipi ad??: ", abone_tipi_adi)
    print("Abonenin d??nemlik; ")
    print("su t??ketimi: ", format(donemlik_su_tuketimi, " .2f"))
    print("su t??ketim bedeli: ", format(donemlik_su_tuketim_bedeli, " .2f"))
    print("at??k su bedeli: ", format(donemlik_atik_su_bedeli, " .2f"))
    print("toplam su bedeli: ", format(donemlik_toplam_su_bedeli, ".2f"))
    print("??TV bedeli: ", format(donemlik_CTV_ucreti, " .2f"))
    print("kat?? at??k bertaraf bedeli: ", format(donemlik_kati_atik_bertaraf_ucreti, " .2f"))
    print("kat?? at??k toplama bedeli: ", format(donemlik_kati_atik_toplama_bedeli, " .2f"))
    print("toplam fatura bedeli: ", format(donemlik_toplam_fatura_tutari, " .2f"))
    print("devletin ald?????? KDV bedeli: ", format(devlete_giden_KDV, " .2f"))
    print("il??e belediyesinin ald?????? bedel: ", format(ilce_belediyesine_giden_tutar, ".2f"))
    print("b??y??k??ehir belediyesinin ald?????? bedel: ", format(buyuksehir_belediyesine_giden_tutar, " .2f"))
    print("??ZSU'nun ald?????? bedel: ", format(IZSU_payi, " .2f"))
    aylik_su_tuketim_mik = toplam_su_tuketimi * kullanim_suresinin_aylik_degeri
    if abone_tipi_kodu == 1:
        konut_abone_yuzdesi = konut_say * 100 / toplam_abone_say
        aylik_konut_ort_su_tuketim_mik = (toplam_konut_su_tuketimi / konut_say) * kullanim_suresinin_aylik_degeri
        aylik_konut_su_tuketim_mik = toplam_konut_su_tuketimi * kullanim_suresinin_aylik_degeri
        aylik_konut_su_tuketim_yuzdesi = aylik_konut_su_tuketim_mik * 100 / aylik_su_tuketim_mik
    elif abone_tipi_kodu == 2:
        isyeri_abone_yuzdesi = isyeri_say * 100 / toplam_abone_say
        aylik_isyeri_ort_su_tuketim_mik = (toplam_isyeri_su_tuketimi / isyeri_say) * kullanim_suresinin_aylik_degeri
        aylik_isyeri_su_tuketim_mik = toplam_isyeri_su_tuketimi * kullanim_suresinin_aylik_degeri
        aylik_isyeri_su_tuketim_yuzdesi = aylik_isyeri_su_tuketim_mik * 100 / aylik_su_tuketim_mik
    elif abone_tipi_kodu == 3:
        resmi_daire_abone_yuzdesi = resmi_daire_say * 100 / toplam_abone_say
        aylik_resmi_daire_ort_su_tuketim_mik = (toplam_resmi_daire_su_tuketimi / resmi_daire_say) * \
                                               kullanim_suresinin_aylik_degeri
        aylik_resmi_daire_su_tuketim_mik = toplam_resmi_daire_su_tuketimi * kullanim_suresinin_aylik_degeri
        aylik_resmi_daire_su_tuketim_yuzdesi = aylik_resmi_daire_su_tuketim_mik * 100 / aylik_su_tuketim_mik
        if max_resmi_daire_tuketim_miktari < aylik_resmi_daire_su_tuketim_mik:
            max_resmi_daire_tuketim_miktari = aylik_resmi_daire_su_tuketim_mik
            max1_abone_no = abone_no
    elif abone_tipi_kodu == 4:
        organize_sanayi_abone_yuzdesi = organize_sanayi_say * 100 / toplam_abone_say
        aylik_organize_sanayi_ort_su_tuketim_mik = (toplam_organize_sanayi_su_tuketimi / organize_sanayi_say) * \
                                                   kullanim_suresinin_aylik_degeri
        aylik_organize_sanayi_su_tuketim_mik = toplam_organize_sanayi_su_tuketimi * kullanim_suresinin_aylik_degeri
        aylik_organize_sanayi_su_tuketim_yuzdesi = aylik_organize_sanayi_su_tuketim_mik * 100 / aylik_su_tuketim_mik
    else:
        ilce_tar_hay_sulama_abone_yuzdesi = ilce_tar_hay_sulama_say * 100 / toplam_abone_say
        aylik_ilce_tar_hay_sulama_ort_su_tuketim_mik = (
                                                               toplam_ilce_tar_hay_sulama_su_tuketimi / ilce_tar_hay_sulama_say) * \
                                                       kullanim_suresinin_aylik_degeri
        aylik_ilce_tar_hay_sulama_su_tuketim_mik = toplam_ilce_tar_hay_sulama_su_tuketimi * kullanim_suresinin_aylik_degeri
        aylik_ilce_tar_hay_sulama_su_tuketim_yuzdesi = aylik_ilce_tar_hay_sulama_su_tuketim_mik * 100 / aylik_su_tuketim_mik
        ilce_tar_hay_50_tondan_cok_kullananlarin_yuzdesi = tuketimi_50tondan_cok_olanlar * 100 / ilce_tar_hay_sulama_say
    aylik_toplam_su_tuketim_ucreti = toplam_su_tuketim_ucreti * kullanim_suresinin_aylik_degeri
    baska_abone_var_mi = input("Ba??ka abone varsa 'e' veya 'E' yoksa 'h' veya 'H' giriniz: ")
    while baska_abone_var_mi not in ('e', 'E', 'h', 'H'):
        baska_abone_var_mi = input("Hatal?? giri?? yapt??n??z! Ba??ka abone varsa 'e' veya 'E' yoksa 'h' veya 'H' giriniz: ")
    if baska_abone_var_mi == 'h' or baska_abone_var_mi == 'H':
        break

print("(A??a????daki de??erler ayl??k (30 g??nl??k) s??re?? i??in ge??erlidir.)")
print("Konut tipi aboneler i??in;")
print("Abone say??s??: ", konut_say)
print("Abone y??zdesi: ", format(konut_abone_yuzdesi, " .2f"))
print("Ayl??k ortalama su t??ketim miktar??: ", format(aylik_konut_ort_su_tuketim_mik, " .2f"))
print("???? yeri tipi aboneler i??in;")
print("Abone say??s??: ", isyeri_say)
print("Abone y??zdesi: ", format(isyeri_abone_yuzdesi, " .2f"))
print("Ayl??k ortalama su t??ketim miktar??: ", format(aylik_isyeri_ort_su_tuketim_mik, " .2f"))
print("Resmi daire tipi aboneler i??in;")
print("Abone say??s??: ", resmi_daire_say)
print("Abone y??zdesi: ", format(resmi_daire_abone_yuzdesi, " .2f"))
print("Ayl??k ortalama su t??ketim miktar??: ", format(aylik_resmi_daire_ort_su_tuketim_mik, " .2f"))
print("Organize sanayi tipi aboneler i??in;")
print("Abone say??s??: ", organize_sanayi_say)
print("Abone y??zdesi: ", format(organize_sanayi_abone_yuzdesi, " .2f"))
print("Ayl??k ortalama su t??ketim miktar??: ", format(aylik_organize_sanayi_ort_su_tuketim_mik, " .2f"))
print("??l??e tar??msal ve hayvan sulama tipi aboneler i??in;")
print("Abone say??s??: ", ilce_tar_hay_sulama_say)
print("Abone y??zdesi: ", format(ilce_tar_hay_sulama_abone_yuzdesi, " .2f"))
print("Ayl??k ortalama su t??ketim miktar??: ", format(aylik_ilce_tar_hay_sulama_ort_su_tuketim_mik, " .2f"))
print("T??ketimine g??re 1. kademe konut tipi abone say??s??: ", kademe1_konut_say)
print("Bu abonelerin konut tipi aboneler i??indeki y??zdesi: ", format(kademe1_yuzdesi, " .2f"))
print("Bu abonelerin ayl??k ortalama su t??ketim miktarlar??: ", format(kademe1_aylik_ort_tuketim_mik, " .2f"))
print("T??ketimine g??re 2. kademe konut tipi abone say??s??: ", kademe2_konut_say)
print("Bu abonelerin konut tipi aboneler i??indeki y??zdesi: ", format(kademe2_yuzdesi, " .2f"))
print("Bu abonelerin ayl??k ortalama su t??ketim miktarlar??: ", format(kademe2_aylik_ort_tuketim_mik, " .2f"))
print("T??ketimine g??re 2. kademe konut tipi abone say??s??: ", kademe3_konut_say)
print("Bu abonelerin konut tipi aboneler i??indeki y??zdesi: ", format(kademe3_yuzdesi, " .2f"))
print("Bu abonelerin ayl??k ortalama su t??ketim miktarlar??: ", format(kademe3_aylik_ort_tuketim_mik, " .2f"))
print("Ayl??k su t??ketim miktar?? 50 tondan ??ok olan il??e tar??msal ve hayvan sulama tipi abone say??s??: ",
      tuketimi_50tondan_cok_olanlar)
print("Ayl??k su t??ketim miktar?? 50 tondan ??ok olan il??e tar??msal ve hayvan sulama tipi abonelerin il??e tar??msal \
ve hayvan sulama tipi aboneler i??indeki y??zdesi: ", format(ilce_tar_hay_50_tondan_cok_kullananlarin_yuzdesi, " .2f"))
print("Ayl??k su t??ketimi 100 tondan y??ksek veya ayl??k su t??ketim ??creti 500 TL den y??ksek olan abone say??s??: ",
      ucreti_500den_kullanimi_100den_cok_olanlar)
print("??ehit gazi veya devlet sporcusu olan ve engelli olan konut tipi abone say??s??: ",
      sehit_gazi_veya_sporcu_engelli_olan_konut_say)
print("Bu abonelerin konut tipi aboneler i??indeki y??zdesi: ",
      format(sehit_gazi_veya_sporcu_engelli_olan_konut_yuzdesi, " .2f"))
print("Ayl??k su t??ketim miktar?? en y??ksek olan resmi daire tipi abonenin;")
print("Abone nosu: ", max1_abone_no)
print("Ayl??k su t??ketim miktar??: ", format(max_resmi_daire_tuketim_miktari, " .2f"))
print("Ayl??k su t??ketim ??creti en y??ksek olan konut tipi d??????ndaki abonenin; ")
print("Abone nosu: ", max2_abone_no)
print("Ayl??k su t??ketim ??creti = ", format(max_aylik_su_tuketim_ucreti, " .2f"))
print("Konut tipi aboneler i??in;")
print("Ayl??k toplam su t??ketim miktar??: ", format(aylik_konut_su_tuketim_mik, " .2f"))
print("Bornova i??indeki y??zdesi: ", format(aylik_konut_su_tuketim_yuzdesi, " .2f"))
print("Ayl??k toplam su t??ketim ??creti: ", format(aylik_konut_su_tuketim_ucreti, " .2f"))
print("???? yeri tipi aboneler i??in;")
print("Ayl??k toplam su t??ketim miktar??: ", format(aylik_isyeri_su_tuketim_mik, " .2f"))
print("Bornova i??indeki y??zdesi: ", format(aylik_isyeri_su_tuketim_yuzdesi, " .2f"))
print("Ayl??k toplam su t??ketim ??creti: ", format(aylik_isyeri_su_tuketim_ucreti, " .2f"))
print("Resmi daire tipi aboneler i??in;")
print("Ayl??k toplam su t??ketim miktar??: ", format(aylik_resmi_daire_su_tuketim_mik, " .2f"))
print("Bornova i??indeki y??zdesi: ", format(aylik_resmi_daire_su_tuketim_yuzdesi, " .2f"))
print("Ayl??k toplam su t??ketim ??creti: ", format(aylik_resmi_daire_su_tuketim_ucreti, " .2f"))
print("Organize sanayi tipi aboneler i??in;")
print("Ayl??k toplam su t??ketim miktar??: ", format(aylik_organize_sanayi_su_tuketim_mik, " .2f"))
print("Bornova i??indeki y??zdesi: ", format(aylik_organize_sanayi_su_tuketim_yuzdesi, " .2f"))
print("Ayl??k toplam su t??ketim ??creti: ", format(aylik_organize_sanayi_su_tuketim_ucreti, " .2f"))
print("??l??e tar??msal ve hayvan sulama tipi aboneler i??in;")
print("Ayl??k toplam su t??ketim miktar??: ", format(aylik_ilce_tar_hay_sulama_su_tuketim_mik, " .2f"))
print("Bornova i??indeki y??zdesi: ", format(aylik_ilce_tar_hay_sulama_su_tuketim_yuzdesi, " .2f"))
print("Ayl??k toplam su t??ketim ??creti: ", format(aylik_ilce_tar_hay_sulama_su_tuketim_ucreti, " .2f"))
print("Bornovan??n ayl??k toplam su t??ketim miktari: ", format(aylik_toplam_su_tuketim_ucreti, " .2f"))
print("T??m abonelerden toplanan ayl??k toplam su t??ketim ??creti: ", format(toplam_su_tuketim_ucreti, " .2f"))
print("Toplam ??ZSU'nun ald?????? pay: ", format(toplam_IZSU_tutari, " .2f"))
print("Toplam il??e belediyesinin ald?????? pay: ", format(toplam_ilce_belediyesine_giden_tutar, " .2f"))
print("Toplam b??y??k??ehir belediyesinin ald?????? pay: ", format(toplam_buyuksehir_belediyesine_giden_tutar, " .2f"))
