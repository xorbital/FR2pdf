# FR2pdf
FR2Pdf basiert zu 99% auf dem großartigen [SZ2Pdf](https://github.com/SiKreuz/SZ2pdf), da im Hintergrund das selbe Framework beim Verlag verwendet wird, klappt der Download der FR mit ein paar kleinen Veränderungen (siehe unten) ebenfalls.
Danke, @SiKreuz!
Dieses Tool soll dabei helfen, immer die neueste Ausgabe der [Frankfurter Rundschau](https://www.fr.de/) als PDF herunterzuladen.
Wenn man sich über die Website einloggen muss, sind es leider nervig viele Klicks, bis man zum eigentlichen Download kommt.
Das geht jetzt einfacher!

Zwingend erforderlich ist dafür natürlich ein Account und Abo bei der Süddeutschen Zeitung, sodass du den Zugriff auf das ePaper hast.

## Installation
Mit `pip` installieren:
```commandline
pip install git+https://github.com/xorbital/FR2pdf
```

Zum Updaten der Software muss die Option `-U` verwendet werden. Für eine systemweite Installation sind root-Rechte nötig.

## Konfiguration
Alle wichtigen Parameter können entweder über die Kommandozeile übergeben werden, oder in der Konfigurationsdatei festgelegt werden.

## SSL-Probleme
Es kann zu Problemen mit SSL kommen, wie:
```
urllib.error.URLError: <urlopen error [SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:997)>
```
Falls dieser Fehler auftritt, stelle sicher dass die Datei `ssl_conf` vorhanden ist.
Dann folgenden Befehl im selben Verzeichnis ausführen:
```
export OPENSSL_CONF="$(pwd)/ssl_conf"
```
Nun sollte FR2Pdf in der selben Terminalsitzung keine Probleme mehr verursachen.

Falls du diese 2 Schritte automatisieren kannst und mit in FR2Pdf.py packen kannst, würde ich mich über einen PR sehr freuen :)
Siehe: [Issue #1](https://github.com/xorbital/FR2pdf/issues/1)

### Kommandozeile
```text
Usage: FR2pdf [OPTIONS]

Options:
  -u, --username TEXT      Username for login
  -p, --password TEXT      Password for login
  -e, --edition TEXT       Specifies the edition
  -d, --download-dir PATH  Download directory
  -h, --help               Show this message and exit.
```

### Konfigurationsdatei
Die Konfigurationsdatei liegt in dem für das Betriebssystem typischen Ordner. Unter Linux wäre das `~/.config/FR2pdf/config`. Standardmäßig werden die folgenden Konfigurationen geschrieben:

```ini
[FR]
username = 
password = 
edition = Stadtausgabe
download_dir = <home-dir>/FR2pdf_Downloads
```

### Mögliche Editionen der FR
Folgende Versionen der Zeitung können angegeben werden:
- Deutschland (Standard)
- Darmstadt
- Hochtaunus
- Main-Kinzig
- Main-Taunus
- Offenbach
- Stadtausgabe

### Änderungen im Vergleich zu SZ2Pdf
- Die URLs zum Anmelden und herunterladen sind etwas anders
- Die Login-Felder sind anders benannt
- Die robots.txt verhindert ein automatisches Herunterladen, daher wurde das lesen ebendieser deaktiviert.
- Ab 3 Logins gibt es Fehlermeldungen wegen der Anzahl gleichzeitiger Sitzungen, diese beendet FR2Pdf automatisch.
