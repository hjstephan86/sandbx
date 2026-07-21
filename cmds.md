# cmds

## pyreverse

### Linux
```bash
(venv) stephan@hp-255-17625:~/Git/umlp$ pyreverse -o dot -d doc/uml -p umlp src/
Analysed 14 modules with a total of 10 imports
(venv) stephan@hp-255-17625:~/Git/umlp$ sfdp -Tpdf doc/uml/classes_umlp.dot -o doc/uml/classes_umlp.pdf
(venv) stephan@hp-255-17625:~/Git/umlp$ sfdp -Tpdf doc/uml/packages_umlp.dot -o doc/uml/packages_umlp.pdf
```

### Windows
```bash
PS C:\Users\sepp5\Git\gen-db> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
PS C:\Users\sepp5\Git\gen-db> iwr -useb get.scoop.sh | invoke-expression
PS C:\Users\sepp5\Git\gen-db> scoop install graphviz

PS C:\Users\sepp5\Git\gen-db> C:\Users\sepp5\AppData\Roaming\Python\Python312\Scripts\pyreverse.exe -o pdf -f ALL --colorized -p gen-db src/backend/
```

## cairosvg
```bash
(venv) stephan@hp-255-17625:~/Git/iono$ for file in src/results/*.svg; do cairosvg "$file" -o "${file%.svg}.pdf"; done
```

## ocrmypdf
```bash
stephan@hp-255-17625:~/GoogleDrive/Geld/Recht/Bielefeld/moBiel/Klage/Feb$ ocrmypdf 21-T-53-25-Beschluss.pdf 21-T-53-25-Beschluss-s.pdf 
Scanning contents     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 5/5 0:00:00
Start processing 5 pages concurrently                                                         _sync.py:265
OCR                   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 5/5 0:00:00
Postprocessing...                                                                             _sync.py:314
Recompressing JPEGs   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   0% 0/0 -:--:--
Deflating JPEGs       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 5/5 0:00:00
JBIG2                 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   0% 0/0 -:--:--
Image optimization ratio: 1.04 savings: 3.7%                                             _pipeline.py:1019
Total file size ratio: 1.03 savings: 2.9%                                                _pipeline.py:1022
Output file is a PDF/A-2B (as expected)                                                       _sync.py:423
stephan@hp-255-17625:~/GoogleDrive/Geld/Recht/Bielefeld/moBiel/Klage/Feb$ pdftotext 21-T-53-25-Beschluss-s.pdf 21-T-53-25-Beschluss.txt
stephan@hp-255-17625:~/GoogleDrive/Geld/Recht/Bielefeld/moBiel/Klage/Feb$ 
```

## rclone
```bash
rclone sync GoogleDrive: ~/GoogleDrive -P
```

## wkhtmltopdf
```bash
stephan@hp-255-17625:~$ wkhtmltopdf --page-size A4 --margin-top 15mm --margin-right 15mm  --margin-bottom 15mm --margin-left 15mm Widerspruch.html Widerspruch.pdf
Loading page (1/2)
Printing pages (2/2)                                               
Done                                                           
stephan@hp-255-17625:~$ 
```

## gpg
```bash
stephan@HP-OmniBook-5:~$ gpg --list-keys
/home/stephan/.gnupg/pubring.kbx
--------------------------------
pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      23836D541CF2E6FA998E909466198EE2F77EC253
uid           [  full  ] Amtsgericht Bielefeld <poststelle@ag-bielefeld.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      614DC18B0B76A1C91423832C8CB9F2EEA14B8BC8
uid           [  full  ] Generalstaatsanwalt Hamm <poststelle@gsta-hamm.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      A95AEE37BA344BD3356FA0B423C15A70AF48C91E
uid           [  full  ] Landgericht Bielefeld <poststelle@lg-bielefeld.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      09B149570377780F05A89794DECEFD8E0251AFAE
uid           [  full  ] Landessozialgericht fuer das Land Nordrhein-Westfalen, Essen <poststelle@lsg.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      E9B1EA6135F0E3CCAFFA623EE101619D1EA165A3
uid           [  full  ] Praesident des Oberlandesgerichts Hamm <poststelle@olg-hamm.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      7AED685466E929112B65D1FE57E71B3C35F60DBB
uid           [  full  ] Oberverwaltungsgericht fuer das Land Nordrhein-Westfalen, Muenster <poststelle@ovg.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      2569AF8FA8D065292C7C0FBDB95CAB72470AB537
uid           [  full  ] Sozialgericht Detmold <poststelle@sg-detmold.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      F692667E6290190DDDC232FFCD6D5008A2A0720C
uid           [  full  ] Staatsanwaltschaft Bielefeld <poststelle@sta-bielefeld.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      316911BA25ABE2E2D4862FE69C4FD8EE0DB6AF6A
uid           [  full  ] Verwaltungsgericht Minden <poststelle@vg-minden.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2023-08-04 [SC] [expires: 2026-08-03]
      3E0CFF1731728742E7CF081C2191FA5B31352DD5
uid           [  full  ] Bezirksregierung Detmold <poststelle@brdt.sec.nrw.de>
sub   rsa4096 2023-08-04 [E] [expires: 2026-08-03]

pub   rsa4096 2025-08-20 [SC]
      F87B7ED230DBAE45FB850D8E5C3F0B67ECE1E954
uid           [ultimate] Stephan Epp <Stephan_Epp@web.de>
sub   rsa4096 2025-08-20 [E]

pub   rsa4096 2015-06-19 [SCE] [expires: 2027-06-19]
      0932579B33C18C216C9DE77D08DDBAE433775707
uid           [  full  ] HmbBfDI <mailbox@datenschutz.hamburg.de>

pub   rsa4096 2023-09-25 [SCEA] [expired: 2025-09-24]
      BDB6A1D5271A5471CF8EB7E55EDB83F8EE8610DA
uid           [ expired] Görzen, Alexander <alexander.goerzen@polizei.nrw.de>

pub   rsa4096 2021-11-22 [SC]
      081910AD8FEF62A9BD7A9C52B3DB661A2928E65A
uid           [  full  ] Bundeskriminalamt <pgp-key4k@bka.bund.de>
sub   rsa4096 2021-11-22 [E]

pub   rsa4096 2023-09-26 [SCEA] [expired: 2025-09-25]
      96BC61CA4B853E170F22ABEA0BCFDC22B5534DF2
uid           [ expired] F Bielefeld Poststelle <poststelle.bielefeld@polizei.nrw.de>

```

## grep
```bash
grep -r --include="*.tex" "Subgraph Algorithmus" . 
```

## find
```bash
find . -name "*.tex"
```

## du
```bash
du -sh */ | sort -rh | head -20
ncdu ~

# Find large files
find ~ -size +100M -type f 2>/dev/null
```

## fwupdmgr
```bash
# Show available firmware updates
fwupdmgr get-updates

# Load firmware updates
fwupdmgr update

# Firmware results
fwupdmgr clear-results
```

## upgrade
```bash
sudo apt update && sudo apt full-upgrade

sudo apt autoremove

stephan@HP-OmniBook-5:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 26.04 LTS
Release:	26.04
Codename:	resolute

stephan@HP-OmniBook-5:~$ pro status
SERVICE          ENTITLED  STATUS       DESCRIPTION
esm-apps         yes       enabled      Expanded Security Maintenance for Applications
esm-infra        yes       enabled      Expanded Security Maintenance for Infrastructure
landscape        yes       disabled     Management and administration tool for Ubuntu
livepatch        yes       enabled      Canonical Livepatch service
```


