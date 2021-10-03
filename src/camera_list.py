# -*- coding: utf-8 -*-
sehir = {"0":"http://ibb-media1.ibb.gov.tr:1935/live/223.stream/chunklist_w1088399288.m3u8", #mecidiyeköy
	"1":"http://ibb-media1.ibb.gov.tr:1935/live/344.stream/chunklist_w1837373499.m3u8", #FSM Köprüsü
	"2":"http://ibb-media1.ibb.gov.tr:1935/live/338.stream/chunklist_w1878212776.m3u8", #268-s yolu asiyan
	"3":"http://ibb-media4.ibb.gov.tr:1935/live/43.stream/chunklist_w92679156.m3u8",#beşiktaş
	"4":"http://ibb-media1.ibb.gov.tr:1935/live/282.stream/chunklist_w1481500069.m3u8", #sirkeci
	"5":"http://ibb-media4.ibb.gov.tr:1935/live/66.stream/chunklist_w1412092558.m3u8", #Acıbadem Köprüsü
	"6":"hhttp://ibb-media1.ibb.gov.tr:1935/live/201.stream/chunklist_w1783199883.m3u8", #Kadıköy Rıhtım
	"7":"http://ibb-media1.ibb.gov.tr:1935/live/202.stream/chunklist_w2146144758.m3u8", #Kağıthane
	"8":"http://ibb-media2.ibb.gov.tr:1935/live/664.stream/chunklist_w814352611.m3u8",#Çavuşbaşı
	"9":"http://ibb-media2.ibb.gov.tr:1935/live/648.stream/chunklist_w109196455.m3u8", #dünya gazetesi
	"10":"http://ibb-media4.ibb.gov.tr:1935/live/13.stream/chunklist_w779799182.m3u8", #Atatürk Havalimanı
	"11":"http://ibb-media4.ibb.gov.tr:1935/live/81.stream/chunklist_w660600761.m3u8", # 15 temmuz şehitler köprüsü
	"12":"http://ibb-media1.ibb.gov.tr:1935/live/174.stream/chunklist_w1362957790.m3u8", #Bahçe Taksim
	"13":"http://ibb-media4.ibb.gov.tr:1935/live/45.stream/chunklist_w1312528785.m3u8", #Eyüp Feshane
	"14":"http://ibb-media4.ibb.gov.tr:1935/live/114.stream/chunklist_w957944218.m3u8", # harem ido
	"15":"http://ibb-media2.ibb.gov.tr:1935/live/1021.stream/chunklist_w1274393475.m3u8", #H.U Tuneli beykoz
    "16":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_eminonu.stream/chunklist_w1540259992.m3u8", # Eminönü
    "17":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_eyup.stream/chunklist_w1334162288.m3u8", # Eyüp Sultan
    "18":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_istiklal_cad_1.stream/chunklist_w1111317814.m3u8", # İstiklal Caddesi 1
    "19":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_istiklal_cad_2.stream/chunklist_w307191567.m3u8", # İstiklal Caddesi 2
    "20":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_misir_carsisi.stream/chunklist_w1494476399.m3u8", # Mısır Çarşısı
    "21":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_miniaturk.stream/chunklist_w2019234198.m3u8", # Miniatürk
    "22":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_sarachane.stream/chunklist_w1856727921.m3u8", # Saraçhane
    "23":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_sultanahmet_2.stream/chunklist_w668404393.m3u8", # Sultan Ahmet
    "24":"https://livestream.ibb.gov.tr/cam_turistik/cam_trsk_bagdat_cad_1.stream/chunklist_w2097004344.m3u8", # Bağdat caddesi
}

def selected_camera(index):
    camera_selected = sehir[f'{index-1}']
    return camera_selected