# Tutorijal za uspostavljanje konekcije sa serverom (SSH Remote) pomoću alata Visual Studio Code

PREREQUISITES:

Neophodno je da su Vam dodeljeni username i password kako bi ste mogli da pristupite serveru. Potrebno je da se obratite administratoru na Slack kanal **#general** kako bi Vam se dodelili username i password.

Administratori su Slobodan Ilić, Milovan Medojević i Ilja Popović.

Potrebno je prvo da instalirate Visual Studio Code odlaskom na link https://code.visualstudio.com/download i da izaberete odgovarajuću verziju, u skladu sa Vašim operativnim sistemom.

![vscode download](https://user-images.githubusercontent.com/97163298/149396599-b37bb79d-1383-41ec-aa66-4772ff096491.png)

Posle, uspešne instalacije, pokrenete Visual Studio Code i odete na dugme Extension Marketplace, kako biste instalirali Remote SSH Plugin. U search polje ukucajte remote ssh, odaberete odgovarajući paket i u desnom prozoru kliknete na install.

![extension market](https://user-images.githubusercontent.com/97163298/149620164-b1d3ff1e-9233-43bb-a954-1191f530c0a8.png)

![install ssh](https://user-images.githubusercontent.com/97163298/149339244-a6ae5a0b-eada-4d8d-9925-f88ddef19f5f.png)

Zatim, idete na dugme Remote Explorer  i posle idete na dugme **+**, kako biste konfigurisali vezu, otvoriće Vam se novi prozor gde je potrebno da ukucate **ssh username@147.91.175.237 -p 52626** (username zamenite sa Vama dodeljenim username-om).

![ssh remote](https://user-images.githubusercontent.com/97163298/149327937-c341e141-8355-418d-b92a-bbe046043be0.png)

U slučaju da Vam se pojavi novi prozor Select the platform of the remote host izaberite opciju Linux.

![ssh remote](https://user-images.githubusercontent.com/97163298/149331345-bb557ade-3b60-4be3-907b-352bb92967aa.png)

Sada bi trebalo da u gornjem levom uglu ispod **SSH TARGETS** vidite da je konfigurisan remote host **147.91.175.237**.

![ssh targets](https://user-images.githubusercontent.com/97163298/149620308-a86100a1-c72b-4129-ae02-740a726e71e0.png)

Zatim kliknete na dugme Connect to host in new window koje će Vam otvoriti novi prozor gde je potrebno da ukucate **password** koji će Vam kao i username biti dodeljen od strane administratora.

![connect to host](https://user-images.githubusercontent.com/97163298/149620333-0dc97446-6d17-4f7b-be83-c9154de9ba93.png)

![pass](https://user-images.githubusercontent.com/97163298/149334966-fd8483c7-9cb8-4cef-b671-830d84ef1bcd.png)

U slučaju da ste uspešno uspostavili vezu sa serverom u donjem desnom uglu će vam biti prikazano oznaka servera **147.91.175.237** u zelenoj boji.

![connected](https://user-images.githubusercontent.com/97163298/149620364-c4d84f21-20d7-46ba-9fd0-9998178d7b36.png)










