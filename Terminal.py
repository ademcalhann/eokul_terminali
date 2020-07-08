import requests
import pyautogui
import time
import pyperclip
from tkinter import *
from sys import version_info
from tkinter.ttk import Combobox
from tkinter import ttk
import tkinter as tk 
import os.path
from os import path
import os


stsy=int(1)
global tamx
tamx=int(0)
global durum 
global ogr_say
def uyari(sonuc,renk):
     global durum
     anaPencere.geometry("343x115+1022+0")
     return(durum.configure(text=sonuc,bg=renk))

#tc arama otomatik
def tc_ara(s_is,a_tc):
      tcem=pyautogui.locateCenterOnScreen(r'kimlik/'+s_is+'/'+a_tc+'.png')
      if tcem!=None:
           global kisix,kisiy
           kisix,kisiy=tcem
      if tcem==None:
           pyautogui.hotkey("pgdn")
           time.sleep(0.5)
           pyautogui.hotkey("enter")
           time.sleep(0.5)
           tc_ara(s_is,a_tc)
#buna gerek kalmadı
def s_yuk():
     global s_bekle
     global stsy
     global snf_say
     
     s_liste=pyautogui.locateCenterOnScreen(r'icon/bekle.png')
     if s_liste == None:
           print("Kaydetme Tamamlandı")
           uyari("Sayfa Yüklendi !","#04F358")
           s_bekle=0
           stsy+=1

           if stsy<=snf_say:
                print("Çağırılan Sınıf: "+str(stsy)) 
                snf_sec(stsy)
           if stsy==snf_say+1:
                print("Sınıflar Komple bitti")
                uyari("Sınıflar Komple Bitti !","#04F358") 

     if s_liste!=None:
           time.sleep(3)
           if s_bekle<15:
                print("Sayfa bekleniyor")
                s_bekle+=3
                s_yuk()            
           if s_bekle==15:
                s_bekle=0
                uyari("Sayfa Yüklenemedi","#F6213A")
                #otomatik 1. kişi kontol ediliyor Bu sebeble devama gerek yok 

                aktar.configure(text="Devam Et",command=lambda:snf_sec(stsy))

global kay_say
kay_say=1
def kaydet_bul():
      print("kaydet aranıyor")
      kydt=pyautogui.locateCenterOnScreen(r'icon/kaydet.png')
      if kydt==None:
            pyautogui.hotkey("pgup")
            time.sleep(1)
            kaydet_bul()
      if kydt!=None:
           global snf_say,kay_say
           if kay_say<= snf_say:
                print("Sınıf sayısı kadar kaydet "+str(kay_say))
                pyautogui.moveTo(kydt,duration=0.5)
                pyautogui.click(kydt,clicks=1) 
                kay_say+=1
           if kay_say==snf_say+1:
                print("Tekrar Kaydedilemez: "+ str(kay_say))
                
                         

#yok yazma motoru

def yok_aktar(sira,ogr_sayisi):
    print("yok_aktar çalıştı: "+str(sira))
    global s_ici
    if sira<=ogr_sayisi:
        xa=2*int(sira)-1
        xb=2*int(sira)
        tc=s_ici[xa]
        yok_tur=s_ici[xb]
        pyperclip.copy(tc)
        pyautogui.hotkey('ctrl','f')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','v')
        pyautogui.hotkey('enter')
        global s_adi
        tc_ara(s_adi,tc)        
        global x_cord
        if sira==1:
           control=pyautogui.locateCenterOnScreen(r'icon/kontrol.png')  
           if control!= None:
                uyari("Bu Sınıfta yoklama alınmış","#04F358")
                pyautogui.moveTo(control)
                sira=ogr_sayisi+1
                #bu sınıfı atla
                yok_aktar(sira,ogr_sayisi)

           if control==None:
                uyari("Devam ediliyor !","#04F358")
                print("Devam ediliyor")
                #Türe göre x belirleme
                #1. kişiye özel yok yazma
                          
                if yok_tur=='1':
                      x_cord=tamx
            
                if yok_tur=='2':
                     x_cord=sabx
             
                if yok_tur=='3':
                      x_cord=osx 

                if yok_tur=='4':
                     x_cord=nobx

                if yok_tur=='5':
                     x_cord=gecx 

                pyautogui.click(x_cord,kisiy,clicks=1)
                #gecici kaldırma
                #time.sleep(1)
                #pyautogui.click(x_cord,kisiy,clicks=1)
                #print("Özel click"+str(x_cord))  
                #tekrar kendini çağırıyor var mı diye
                sira+=1
                print(str(sira)+". Özel çağırıcı")
                yok_aktar(sira,ogr_sayisi)

        if sira>1:  
           #Türe göre x belirleme
           #1. kişi hariç   
           if yok_tur=='1':
                x_cord=tamx
                print(x_cord)
            
           if yok_tur=='2':
                x_cord=sabx
             
           if yok_tur=='3':
                x_cord=osx 

           if yok_tur=='4':
                x_cord=nobx

           if yok_tur=='5':
                x_cord=gecx 

           pyautogui.click(x_cord,kisiy,clicks=1)
           #gecici kaldırma
           #time.sleep(1)
           #pyautogui.click(x_cord,kisiy,clicks=1)
           #print("Genel click"+str(x_cord))
           sira+=1
           print(str(sira)+". birden büyükse çağırıcı")
           yok_aktar(sira,ogr_sayisi)

    if sira==int(ogr_sayisi)+1:
        sira=ogr_sayisi+2 
        print("2 ekledim sira= "+str(sira)) 
        kaydet_bul()
        #sayfa yüklendi mi #devam et
        time.sleep(0.5) 
        yuklendi()
        print("Kaydetme Tamamlandı")
        uyari("Sayfa Yüklendi !","#04F358")
        global stsy
        global snf_say
        stsy+=1

        if stsy<=snf_say:
                print(str(stsy)+". Sınıfı seç")
                print("Çağırılan Sınıf: "+str(stsy)) 
                snf_sec(stsy)
        if stsy==int(snf_say)+1:
                print(str(stsy)+". Sınıfı seç")
                print("Sınıflar Komple bitti")
                uyari("Sınıflar Komple Bitti !","#04F358")
                #devam et te hataya neden oluyor
                raise StopIteration

                
        
global dnm
dnm=0
def sinif_ara(s_ismi):
     global dnm
     s_isx=pyautogui.locateCenterOnScreen(r'sinif/'+s_ismi+'.png')
     if s_isx==None:
          if dnm==0:
               pyautogui.moveTo(listex,listey-200,duration=1)
               dnm=1
               sinif_ara(s_ismi)

          if dnm==1:
               pyautogui.moveTo(listex,listey+200,duration=1)
               dnm=0
               pyautogui.hotkey("pgdn")
               sinif_ara(s_ismi)

     if s_isx!=None:
          global sx,sy
          dnm=0
          sx,sy=s_isx     

def cord_tur():
     tam_yok=pyautogui.locateCenterOnScreen(r'icon/tam.png')
     if tam_yok!=None:
           print("tamx buldum")
           global tamx
           tamx,tamy=tam_yok
           global sabx
           global osx
           global nobx
           global gecx 
           sabx,saby=pyautogui.locateCenterOnScreen(r'icon/sab.png')
           osx,osy=pyautogui.locateCenterOnScreen(r'icon/os.png')
           nobx,noby=pyautogui.locateCenterOnScreen(r'icon/nob.png')
           gecx,gecy=pyautogui.locateCenterOnScreen(r'icon/gec.png')
           #sayfa yüklendi ilk öğrenci ile başla

     
     if tam_yok==None:
          time.sleep(3)
          cord_tur()     

def yuklendi():
     yuk=pyautogui.locateCenterOnScreen(r'icon/yuklendi.png')
     if yuk != None:
           print("Sayfa Yüklendi")
                      
     if yuk == None:
           print("Sayfa bekleniyor")
           time.sleep(3)
           yuklendi()


def tarih_bul(): 
     global tarihx,tarihy
     tarihim=pyautogui.locateCenterOnScreen(r'icon/tarih.png')    
     if tarihim!=None:
          print("tarih bulundu")
          tarihx,tarihy=tarihim
     if tarihim==None:
          time.sleep(3)
          print("Tarih arnıyor")
          tarih_bul()


#eokulda sınıf seç
def sin_eok(s_adi,o_say):
    pyautogui.hotkey("home")
    tarih_bul()
    pyautogui.click(tarihx-30,tarihy,clicks=1)
    pyautogui.hotkey("ctrl","a")
    time.sleep(0.5)
    pyautogui.write(tarih)
    #tarihi bulduktan sonra listeleyi arama
    global listex,listey
    listex,listey=pyautogui.locateCenterOnScreen(r'icon/listele.png')
    pyautogui.moveTo(listex,listey-50,duration=0.5)
    pyautogui.click(listex,listey-50,clicks=1)
    time.sleep(0.5)
    s_adi=s_adi.strip()
    sinif_ara(s_adi)
    global sx,sy
    pyautogui.moveTo(sx,sy)
    pyautogui.click(sx,sy,clicks=1)
    pyautogui.click(listex,listey,clicks=1)
    if tamx==0:
         cord_tur()
    time.sleep(0.5)     
    yuklendi()  
    yok_aktar(1,o_say)    

#en temel döngü 
#posttan sınıf seç
def snf_sec(stsy):
    global s_ici
    print("Sınıf: "+str(stsy))
    s_ici=satir[stsy].split('|')
    #sınıfta kaç kişi var
    ogr_say=len(s_ici)
    ogr_say=(ogr_say-1)/2
    print("Öğrenci Sayısı: "+str(ogr_say))
    global s_adi
    #sınıf içinin [0] sınıf adıdır
    s_adi=s_ici[0]
    #değiştirdim
    uyari('Yeni Sınıf:'+s_adi,"#04F358")
    sin_eok(s_adi,ogr_say)



#EN SON AŞAĞIYA TAŞI
# ilk sınıfdana aktarmaya
#9-a sınıfı mavi alınmalı
anaPencere = tk.Tk() 
anaPencere.overrideredirect(1)
anaPencere.attributes("-alpha",0.92)
anaPencere.wm_attributes("-topmost",1)
anaPencere.geometry("343x115+1022+0")
tabControl = ttk.Notebook(anaPencere)
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tab4 = ttk.Frame(tabControl) 
tab5 = ttk.Frame(tabControl) 
  
tabControl.add(tab1, text ='Yoklama') 
tabControl.add(tab2, text ='Öğrenci Ekle') 
tabControl.add(tab3, text ='Sınıf Ekle') 
tabControl.add(tab4, text ='Terminal') 
tabControl.add(tab5, text ='Tanımla') 
tabControl.place(x=5,y=5,width=335,height=110)



def s_list(): 
    kul_kon=os.path.expanduser("~")   
    os.chdir(kul_kon+'/Documents/Terminal')         
    siniflar=os.listdir(kul_kon+'/Documents/Terminal/kimlik/')
    global s_com
    s_com=Combobox(tab2,values=siniflar)
    s_com.current(0)
    s_com.place(x=10,y=10,width=65,height=26)  
    global vs_com
    vs_com=Combobox(tab4,values=siniflar)
    vs_com.current(0)
    vs_com.place(x=10,y=10,width=65,height=26)  

s_list()

def ogr_ekle():
      acik=pyautogui.locateCenterOnScreen(r'icon/url.png')
      if acik==None:
           uyari("Günlük Yoklama Sayfasını Açın ! ","#F80F6C")
      if acik!=None:
           o_sira=c_sira.get()
           o_sinif=s_com.get()
           ortax,ortay=pyautogui.locateCenterOnScreen(r'icon/ortax.png')
           satirim=pyautogui.locateCenterOnScreen('sayilar/'+str(o_sira)+'.png')
           if satirim==None:
                uyari("Öğrenci ekranda yok ! ","#F80F6C")
           if satirim!=None:
                katx,katy=satirim
                pyautogui.click(ortax+5,katy-8,clicks=2,duration=0.25)
                pyautogui.hotkey('ctrl','c')
                tc=str()
                tc=pyperclip.paste()
                n_tc=tc[0:7]
                pyautogui.hotkey('ctrl','f')
                pyautogui.write(n_tc)
                time.sleep(0.5)
                pyautogui.screenshot('kimlik/'+o_sinif+'/'+n_tc+'.png',region=(ortax,katy-10,81,20))
                uyari("Öğrenci Kaydedildi","#04F358")



def gundev():
     l_gun=pyautogui.locateCenterOnScreen(r'icon/l_gun.png')
     if l_gun==None:
          time.sleep(3)
          gundev()
     if l_gun!=None:
          uyari("Sayfa yüklendi !","#04F358")     

def y_getir():
    acik=pyautogui.locateCenterOnScreen(r'icon/acik.png')
    if acik==None:
         uyari("E-Okulu Açmalısınız !","#F80F6C")
         # durum.configure(text="E-Okulu Açmalısınız ! ",bg="#F80F6C")
    if acik!=None:
           okuris=pyautogui.locateCenterOnScreen(r'icon/okuris.png')
           pyautogui.click(okuris,clicks=1)
           time.sleep(0.5)
           gundev()
           url=pyautogui.locateCenterOnScreen(r'icon/url.png') 
           pyautogui.click(url,clicks=1)
           time.sleep(0.5)
           pyautogui.hotkey("ctrl","a")
           pyautogui.write("https://eokul.meb.gov.tr/OrtaOgretim/OKL/OOK08001.aspx")
           pyautogui.hotkey("enter")
           #sonra sınıf ve tarih seç döngüsü  
           v_ay=c_ay.get()
           v_gun=c_gun.get()
           g_tarih=str(v_ay)+str(v_gun)  
           y_yil=yil.get()
           d_adi="yoklama/"+str(v_ay)+str(v_gun)+y_yil+".txt"
           global tarih
           tarih=str(v_gun)+"/"+str(v_ay)+"/"+str(y_yil)

           if path.exists(d_adi)==True:
                #dosya var
                dsy=open(d_adi,"r",encoding="utf-8")
                gelen=dsy.read()
                uyari("Yoklama okunuyor...","#04F358")
           if path.exists(d_adi)==False:
                #dosya yok
                o_id=eno_id.get()
                a_ent=ara_ent.get()
                uyari("Yoklama alınıyor...","#04F358")
                gelen=requests.post("https://mesajplus.com/oku.php",data={"tarih":g_tarih,"okul_id":o_id,"ara":a_ent})
                #tüm sayfayı texte aldık
                gelen=gelen.text
                dsy=open(d_adi,"w",encoding="utf-8")
                dsy.write(gelen)
                dsy.close()
           
           aktar.configure(state="active",bg="#04F358")
           #sınıflara böldük
           global satir
           satir=gelen.split('£')
           #sınıf ve öğrenci sayısını aldık -1 sorun olabilir ???
           global snf_say
           snf_say=len(satir)-1
           print("Sınıf Sayısı: "+str(snf_say))
           global stsy
           global listex
           global listey 

def ekle_sinif():
    adet=pyautogui.locateCenterOnScreen(r'icon/adet.png')
    if adet==None:
         uyari("Günlük Yoklamada Sınıfı Açın !","#FC0000")
    if adet!=None:
           adkax,adkay=adet
           pyautogui.click(adkax-35,adkay,clicks=2,duration=0.25)
           pyautogui.hotkey('ctrl','c')
           ogr_sayi=pyperclip.paste()
           ortax,ortay=pyautogui.locateCenterOnScreen(r'icon/orta.png')
           time.sleep(0.5)
           s_isim=str(s_sayi.get())+"-"+str(s_harf.get())
           os.chdir('kimlik/')
           #sınıf yoksa oluştur
           if path.exists(s_isim)==False:
                os.mkdir(s_isim) 
                s_list()
                o_id=eno_id.get()
                s_kaydet=requests.post("https://mesajplus.com/python.php",data={"ss_isim":s_isim,"ox_id":o_id})
                cevap=s_kaydet.text
                uyari(cevap,"#04F358")
  
           kul_kon=os.path.expanduser("~")   
           os.chdir(kul_kon+'/Documents/Terminal') 
           yer=1
           while yer<= int(ogr_sayi): 
           #while yer<=4: 
                if pyautogui.locateCenterOnScreen('sayilar/'+str(yer)+'.png'): 
                     katx,katy=pyautogui.locateCenterOnScreen('sayilar/'+str(yer)+'.png')
                     pyautogui.click(ortax+5,katy-8,clicks=2,duration=0.25)
                     pyautogui.hotkey('ctrl','c')
                     tc=str()
                     tc=pyperclip.paste()
                     n_tc=tc[0:7]
                     pyautogui.hotkey('ctrl','f')
                     pyautogui.write(n_tc)
                     time.sleep(0.5)
                     pyautogui.screenshot('kimlik/'+s_isim+'/'+n_tc+'.png',region=(ortax,katy-10,81,20))
                     del katx
                     del katy
                     del tc
                     yer+=1
                else:
                     pyautogui.hotkey('pgdn')
                     yer=yer

def yatay(hat_y,n_tc):
     yty=pyautogui.locateCenterOnScreen('sayilar/'+str(hat_y+1)+'.png')
     if yty==None:
          pyautogui.hotkey("pgdn")
          time.sleep(0.75)
          yatay(hat_y)
     if yty!=None:
          katx,katy=yty
          global ortamx,o_sinif
          pyautogui.moveTo(ortamx+5,katy-8,duration=0.5)
          pyautogui.screenshot('kimlik/'+o_sinif+'/'+n_tc+'.png',region=(ortamx,katy-10,81,20))
          time.sleep(0.5)
          satir_oku2(hat_y+1)

def satir_oku2(konum):
     global veri2
     global okunan
     global satir_sayisi2
     okunan=konum
     #if konum<4:
     if konum<satir_sayisi2:
           global a_tc
           tc=str()
           tc=veri2[5*konum+2]
           a_tc=tc[0:7]
           pyperclip.copy(a_tc)
           pyautogui.hotkey("ctrl","f")
           pyautogui.write(a_tc)
           yatay(konum,a_tc)
     if konum>satir_sayisi2:
          print("Tüm Öğrenciler bitti")
          uyari("Tarama Tamamlandı !","#04F358")
           

def asagi2():
    alt_kose=pyautogui.locateCenterOnScreen(r'icon/alt2.png')
    if alt_kose==None:
        pyautogui.hotkey('pgdn')
        time.sleep(0.5)
        asagi2()
    if alt_kose!=None:
        global  alt_x2, alt_y2
        alt_x2,alt_y2=alt_kose

def komple_ekle():
     yuklu=pyautogui.locateCenterOnScreen(r'icon/orta.png')
     if yuklu==None:
          uyari("Günlük yoklama sayfasında sınıf açın !","#FC0000")
     if yuklu!=None:
          global ortamx,o_sinif
          o_sinif=s_com.get()
          ortamx,ortamy=yuklu
          ust=pyautogui.locateCenterOnScreen(r'icon/ust.png')
          if ust==None:
               pyautogui.hotkey("home")
          if ust!=None:
               ustx,usty=ust 
               pyautogui.mouseDown(ustx,usty+60,button=LEFT)
               asagi2()
               pyautogui.moveTo(alt_x2-10,alt_y2-10,duration=1)
               pyautogui.mouseUp()
               pyautogui.hotkey("ctrl","c")
               pyautogui.click(clicks=1)
               time.sleep(0.5)
               ekran=pyperclip.paste()
               global veri2
               veri2=ekran.split('	')
               leni=len(veri2)
               global satir_sayisi2
               satir_sayisi2=leni/5
               uyari(str(satir_sayisi2)+" Öğrenci Bulundu !","#04F358")
               pyautogui.click(clicks=1)
               satir_oku2(0)

def tel_al():     
     telefon=pyautogui.locateCenterOnScreen(r'icon/telefon.png')
     if telefon==None:
           time.sleep(3)
           tel_al()
     if telefon!=None:
           t_x,t_y=telefon
           pyautogui.click(t_x+100,t_y,clicks=1)
           pyautogui.hotkey("ctrl","a","ctrl","c")
           t_no=pyperclip.paste()
           global islev
           if len(str(t_no))<12:
                t_no=int(t_no)-int(islev)
           if len(str(t_no))>12:
                t_no=0
           global a_tc,isim,okul_no,ss_adi
           s_bilgi=open(r"icon/"+ss_adi+".txt","a",encoding="utf-8")
           s_bilgi.write("(NULL,'"+ss_adi+"','"+isim+"','"+str(t_no)+"','"+okul_no+"','"+a_tc+"'),")
           s_bilgi.close()
           pyautogui.hotkey("browserback")
           pyautogui.hotkey("browserback")
           time.sleep(1)
           global okunan
           print("Okunan: "+str(okunan))
           yeni_satir=int(okunan)+1
           print("Yeni: "+str(yeni_satir))
           satir_oku(yeni_satir)
     

def veli_tara():
     time.sleep(0.75)
     loading=pyautogui.locateCenterOnScreen(r'icon/sms.png')
     if loading==None:
           print("sms aranıyor")
           time.sleep(3)
           veli_tara()
     if loading!=None:
           anne=None
           baba=None
           print("sms var veli anlaşılıyor")
           anne=pyautogui.locateCenterOnScreen(r'icon/anne.png')
           if anne==None:
                print("A1 yok")
                baba=pyautogui.locateCenterOnScreen(r'icon/baba.png')
                if baba==None:
                     print("B1 yok")
                     anne=pyautogui.locateCenterOnScreen(r'icon/b_anne.png')
                     if anne==None:
                          print("A2 yok")
                          anne=pyautogui.locateCenterOnScreen(r'icon/v_anne.png')
                          if anne==None:
                               print("A3 yok")
                               baba=pyautogui.locateCenterOnScreen(r'icon/v_baba.png')
                               if baba==None:
                                    print("B2 yok")
                                    anne=pyautogui.locateCenterOnScreen(r'icon/bos.png')   
                                    baba=pyautogui.locateCenterOnScreen(r'icon/istemiyor.png')
           
           global link
           if anne!=None:
                print("Anne tespit edildi")
                link="https://eokul.meb.gov.tr/OrtaOgretim/OGR/OOG02006.aspx"
           
           if baba!=None:
                print("Baba Tespit edildi")
                link="https://eokul.meb.gov.tr/OrtaOgretim/OGR/OOG02005.aspx"
           pyperclip.copy(link)      
           url=pyautogui.locateCenterOnScreen(r'icon/url.png') 
           print(url)
           pyautogui.click(url,clicks=1)
           pyautogui.hotkey("ctrl","a","ctrl","v","enter")
           tel_al()        






def ogr_dos(ara_tc,satirim):
     r_dosya=pyautogui.locateCenterOnScreen(r'icon/dosya.png')
     if r_dosya==None:
           time.sleep(3)
           print("dosya aranıyor")
           ogr_dos(ara_tc,satirim)
     if r_dosya!=None:
           print("Dosya bulundu")
           global ss_adi
           pyperclip.copy(ara_tc)
           pyautogui.hotkey("ctrl","f")
           time.sleep(0.5)
           pyautogui.hotkey("ctrl","v")
           #pyautogui.hotkey("enter")
           if satirim==1:
                pyautogui.scroll(-47)
           time.sleep(0.5)     
           tc_konum=pyautogui.locateCenterOnScreen(r'kimlik/'+ss_adi+'/'+ara_tc+'.png')
           k_x,k_y=tc_konum
           pyautogui.click(k_x-65,k_y,clicks=1)
           veli_tara()
     



def satir_oku(konum):
     global veri
     global okunan
     global satir_sayisi
     okunan=konum
     #if konum<4:
     if konum<satir_sayisi:
           global a_tc,isim,okul_no
           tc=str()
           tc=veri[7*konum]
           a_tc=tc[0:7]
           isim=veri[7*konum+1]+' '+veri[7*konum+2]
           okul_no=veri[7*konum+3]
           print("Satır okundu,ogr_dos çağırıldı")
           ogr_dos(a_tc,okunan)
           
     if konum>satir_sayisi-1:
     #if konum>3:    
           print("post gitti") 
          #dosyayı kapat yaz ve sona ; replace
           uyari("Tüm Öğrenciler tarandı !","#04F358")
           global ss_adi
           giden=open(r"icon/"+ss_adi+".txt","r",encoding="utf-8")
           o_giden=giden.read()
           #replace gerek
           o_id=eno_id.get()
           a_ent=ara_ent.get()
           po_g=requests.post("https://mesajplus.com/python.php",data={"s_adi":ss_adi,"okul_id":o_id,"ogr_ekle":o_giden})
           cevap=po_g.text
           print(cevap)
           uyari(cevap,"#04F358")
           
def mp_gonder():
           print("post gitti") 
           ss_adi=vs_com.get()
           print(ss_adi)
           #dosyayı kapat yaz ve sona ; replace
           uyari("Tüm Öğrenciler tarandı !","#04F358")
           giden=open(r"icon/"+ss_adi+".txt","r",encoding="utf-8")
           o_giden=giden.read()
           #replace gerek
           o_id=eno_id.get()
           a_ent=ara_ent.get()           
           po_g=requests.post("https://mesajplus.com/python.php",data={"s_adi":ss_adi,"okul_id":o_id,"ogr_ekle":o_giden})
           cevap=po_g.text
           print(cevap)
           uyari(cevap,"#04F358")

  

def asagi():
    alt_kose=pyautogui.locateCenterOnScreen(r'icon/alt_kose.png')
    if alt_kose==None:
        pyautogui.hotkey('pgdn')
        asagi()
    if alt_kose!=None:
        global  alt_x, alt_y
        alt_x,alt_y=alt_kose


              
def  sinif_al():
     tc_bul=pyautogui.locateCenterOnScreen(r'icon/tc_no.png')  
     
     if tc_bul==None:
           uyari("Öğrenci İşleri Modülünü açın !","#F80F6C")
     if tc_bul!=None:
           global vs_com,ss_adi,islev
           islev=e_islev.get()
           ss_adi=vs_com.get()
           tcx,tcy=tc_bul          
           pyautogui.moveTo(tcx-10,tcy+10,duration=1)
           pyautogui.mouseDown(tcx-36,tcy+20,button=LEFT)
           asagi()
           pyautogui.moveTo(alt_x-10,alt_y-10,duration=1)
           pyautogui.mouseUp()
           time.sleep(0.5)
           pyautogui.hotkey("ctrl","c")
           ekran=pyperclip.paste()
           global veri
           veri=ekran.split('	')
           leni=len(veri)
           global satir_sayisi
           satir_sayisi=leni/7
           uyari(str(satir_sayisi)+" Öğrenci Bulundu !","#04F358")
           pyautogui.click(clicks=1)
           satir_oku(0)
           
def o_bil():
      bilgi=open("icon/bilgi.txt","r",encoding="utf-8")
      v_bil=bilgi.read()
      if v_bil!="":
           tara=v_bil.split('|')
           eno_id.insert(END,tara[1])
           ara_ent.insert(END,tara[3])
           yil.insert(END,tara[5])
           e_islev.insert(END,tara[7])
           bilgi.close()
      if v_bil=="":
           eno_id.insert(END,"Okul_id")
           ara_ent.insert(END,"Ara")
           yil.insert(END,"Yıl")
           e_islev.insert(END,"islevsel")
           bilgi.close()


def guncelle():
      bilgi=open("icon/bilgi.txt","w+",encoding="utf-8")
      global eno_id,ara_ent,yil
      o_id=eno_id.get()
      a_ent=ara_ent.get()
      y_yil=yil.get()
      v_islev=e_islev.get()
      bilgi.write("okul_id|"+str(o_id)+"|ara|"+str(a_ent)+"|yıl|"+str(y_yil)+"|islevsel|"+str(v_islev))
      uyari("Tanımlama Başarılı !","#04F358")
      bilgi.close()


xima=PhotoImage(file="icon/x.png")
Button(image=xima,command=anaPencere.quit,relief=FLAT,borderwidth=0).place(x=313,y=0,width=30,height=18)
#tab1
ay=["Ay","09","10","11","12","01","02","03","04","05","06"]
gun=["Gün","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
c_ay=Combobox(tab1,values=ay)
c_gun=Combobox(tab1,values=gun)
c_ay.current(0)
c_gun.current(0)
getir=Button(tab1,text="Yoklama Getir",command=y_getir,relief=GROOVE,fg="#FFFFFF",bg="#04F358")
aktar=Button(tab1,text="E-Okula Aktar",command=lambda: snf_sec(1),relief=GROOVE,disabledforeground="#FC0000",fg="#FFFFFF",state="disable")
durum=Label(text="Terminal Başlatıldı !",bg="#04F358",relief=GROOVE,fg="#FFFFFF",font="8")
#tab2
ekle_tus=Button(tab2,text="Ekle",command=ogr_ekle,fg="#FFFFFF",bg="#04F358",relief=GROOVE)
v_sira=["Sıra No","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45"]
c_sira=Combobox(tab2,values=v_sira)
c_sira.place(x=80,y=10,width=85,height=26)
c_sira.current(0)
ekle_tus.place(x=175,y=10,width=80,height=26)

#tab3
sin_say=["1","2","3","4","5","6","7","8","9","10","11","12","Ana"]
harf=["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z"]
s_sayi=Combobox(tab3,values=sin_say)
s_harf=Combobox(tab3,values=harf)
s_sayi.current(8)
s_harf.current(0)
s_ekle=Button(tab3,text="Ekle",command=ekle_sinif,fg="#FFFFFF",bg="#04F358",relief=GROOVE)


#konumlar
c_ay.place(x=68,y=10,width=65,height=26)
c_gun.place(x=10,y=10,width=48,height=26)
getir.place(x=145,y=10,height=26)
aktar.place(x=240,y=10,height=26)
durum.place(x=5,y=70,width="334",height=47)
#tab4
Button(tab4,text="Başla",command=sinif_al,fg="#FFFFFF",bg="#04F358",relief=GROOVE).place(x=85,y=10,width="80",height="26")
#Button(tab4,text="Gönder",command=mp_gonder,fg="#FFFFFF",bg="#04F358").place(x=175,y=10,height="26",width="80")
#tab5
global eno_id,ara_ent,yil
eno_id=Entry(tab5)
ara_ent=Entry(tab5)
e_islev=Entry(tab5)
eno_id.place(x=10,y=10,width=45,height=26)
e_islev.place(x=65,y=10,width=45,height=26)
ara_ent.place(x=120,y=10,width=50,height=26)
yillar=["2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030"]
yil=Combobox(tab5,values=yillar)
yil.place(x=180,y=10,width=50,height=26)
Button(tab5,text="Güncelle",command=guncelle,fg="#FFFFFF",bg="#04F358",relief=GROOVE).place(x=245,y=10,width=80,height=26)


#tab3
s_sayi.place(x=10,y=10,width="40",height="26")
s_harf.place(x=60,y=10,width="40",height="26")
s_ekle.place(x=115,y=10,width="80",height="26")

#otomatik çalışacaklar
o_bil()
anaPencere.mainloop()