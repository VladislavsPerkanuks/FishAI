## Projekta izstrādātāji

- Vladislavs Perkaņuks
- Jānis Droiskis
- Gundega Līcīte
- Aija Albertiņa

# Ievads

## Problēmas nostādne

Attēlu atpazīšana, kas ir pamatā jebkurai programmai, kas spēj identificēt priekšmetus bildē vai attēlā, balstās uz mašīnmācīšanos. Tādas lietotnes kā [Google Lens](https://lens.google/) vai [PictPicks](https://play.google.com/store/apps/details?id=jp.mydns.usagigoya.imagesearchviewer&hl=en&gl=US), spēj vispārīgi identificēt objektus attēlā, tādus, ka zivs, pudele, apavi, utt. Tādas lietotnes parasti nedod paplašinātu informāciju par identificētu objektu, kā, piemēram, mūsu gadījumā zivs sugu. Aplikācijas, kas spēj iedod lietotājam paplašinātu informāciju, parasti ir ļoti ierobežotas, ar to, kādu datu kopu izmantoja izstrādātāji, lai apmācītu modeli. Mūsu gadījumā, tas nozīmē, ka ne visas Latvijas zivis, varēs veiksmīgi būt identificētas, jo banāli modelis nebija apmācīts ar tām. Tāpēc ir vajadzīgs risinājums, kas spēs veiksmīgi identificēt populārākās Latvijas zivs sugas.

## Mērķis

Izveidot lietotni, kas balstoties uz dziļās mašīnmācīšanās spēs atpazīst lietotāja lejuplādēto Latvijas zivs sugu un saglabāt to lietotāja identificēto zivju bibliotēkā.

# Līdzīgo risinājumu pārskats

## Tehniskais Risinājums

### Algoritmu veidi

Attēlu atpazīšana, ir datorredzes apakškopa, kas ietver sevī vizuālu meklēšanu, semantisko segmentāciju un objektu identificēšanu no attēliem. Attēla atpazīšanas būtība ir algoritms, kas ņem attēlu kā ievadi un interpretē to, vienlaikus norādot šim attēlam klases un etiķetes. Piemēri ar dažiem attēlu klasifikācijas algoritmiem:

- [**Bag of visual words (BOVW)**](https://towardsdatascience.com/bag-of-visual-words-in-a-nutshell-9ceea97ce0fb)
- [**Support-vector machine (SVM)**](https://en.wikipedia.org/wiki/Support-vector_machine)
- [**K-nearest neighbors (KNN)**](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)
- [**Logistic regression**](https://medium.com/swlh/logistic-regression-for-image-classification-e15d0ae59ce9)
- [**Convolutional neural network (CNN)**](https://towardsdatascience.com/wtf-is-image-classification-8e78a8235acb)

### Izvēlētais algoritms

Risinājuma izveidei, tiks izmantots dziļās mašīnmācīšanās algoritms - Convolutional Neural Network, jeb īsumā CNN. Priekšrocībās šīm algoritmam ir:

- Tas spēj efektīvi samazināt parametru skaitu, nezaudējot modeļa kvalitāti (Ātrāka/Mazāk resursus prasoša mācīšanās)
- Ir pieejami gatavi modeļi, kurus var pārmācīt uz mūsu problēmu, kā piemēri, VGG16, Xception, ResNet, u.c. (Transfer Learning)
- Tas automātiski nosaka svarīgākās klases iezīmes/īpatnības bez cilvēka uzraudzības/iejaukšanās

Modeļa apmācībai tiks izmantots Google izstrādātājs no-code risinājums [**Teachable Machine**](https://teachablemachine.withgoogle.com/), kas ir domāts tieši klasifikācijas problēmai, izmantojot jau gatavo modeli un pārmācot to uz aktuālo problēmas sfēru.

### Novērtēšanas kritēriji

Galvenais novērtēšanas kritērijs būs - cik Latvijas zivju sugu, algoritms būs spējīgs precīzi atpazīt.

## Līdzīgi tehniskie risinājumi

### Lietotnes

1. [FishVerify](https://www.fishverify.com/)
2. [Picture Fish - Fish Identifier](https://play.google.com/store/apps/details?id=com.glority.picturefish&hl=en&gl=US)
3. [Fishbrain](https://fishbrain.com/)
4. [Fish Identification - Fish Scanner](https://play.google.com/store/apps/details?id=e.fish.natureai&hl=en&gl=US)
5. [Fishsnap - Fish identifier](https://apps.apple.com/us/app/fishsnap-fish-identifier/id1571610312)

### Vērtēšanas kritēriji

1. **Precizitāte** - cik no 5 Latvijas zivīm, lietotne spēja precīzi atpazīt
2. **Izmaksas** - cik izmaksā lietotne
3. **Lietotāju vērtējums** - kā lietotāji ir novērtējuši lietotni
4. **Pieejamība** - uz kādām platformām ir pieejama lietotne

### Vērtēšanas rezultāti

| Lietotne                           | Precizitāte | Izmaksas       | Pieejamība   | Lietotāju atsauksmes                    |
|------------------------------------|-------------|----------------|--------------|-----------------------------------------|
| FishVerify                         | 1/5         | 41.19 Eur/gadā | Android, iOS | 2.5/5 Google play <br />3.8/5 App Store |
| Picture Fish - Fish Identifier     | 4/5         | 21.99 Eur/gadā | Android, iOS | 3.8/5 Google play <br />4.0/5 App Store |
| Fishbrain                          | 3/5         | 84.99 Eur/gadā | Android, iOS | 3.9/5 Google play<br />4.7/5 App Store  |
| Fish Identification - Fish Scanner | 0/5         | Bezmaksas      | Android      | 3.1/5 Google play                       |
| Fishsnap - Fish identifier         | 2/5         | 43.20 Eur/gadā | iOS          | -                                       |

# Tehniskais Risinājums

## Prasības

**MoSCoW metode**:

| Must haves                                  | Should haves                                  | Could haves                           | Would not haves      |
|:--------------------------------------------|:----------------------------------------------|:--------------------------------------|:---------------------|
| Identificēt zivis vismaz ar 60% precizitāti | Tiek parādīts "Confidence" līmenis            | Modeļa nepārtraukta uzlabošana        | Makšķerēšanas padomi |
| Bibliotēka ar identificētām zivīm           | Tiek noteikta zivs noķeršanas lokācijas vieta | Zivs lielums tiek noteikts pēc bildes | Likumdošana          |
| CRUD operācijas                             |                                               |                                       | Laikapstākļi         |

## Konceptu modelis

### Modelis

![Koncepta datubāze](https://i.ibb.co/dt0SgSD/Screenshot-2021-11-12-103733.png)

### Apraksts

**Lietotājs** - iekļauj sevī informāciju par lietotāju

**Loms** - iekļauj sevī informāciju par konkrētā lietotāja lomu t.i. loma bilde, datums, svars u.c

**Prognozes** - iekļauj sevī informāciju par konkrētā loma dziļās mašīnmācīšānās prognozēm. Šeit ir informācija par prognozes zivs nosaukumu un pašu prognozi (procentos). Kopumā lietotājam tiks izvadītās trīs iespējamākās prognozes. Piem., Nosaukums1 - lasis, procenti1 - 56%, Nosaukums2 - karpa, procenti2 - 33% un Nosaukums3 - līdaka, procenti3 - 11%. Lietotājam ir iespēja iedot savu nosaukumu zivij, rindā lietotaja_nosaukums, ja lietotājs to nav izdarījis, tad lietotaja_nosaukums būs vienāds ar nosaukums1. Tāda pieeja, ļauj saprast vai modelis ir pareizi prognozējis zivs nosaukumu, citos vārdos – ja lietotaja_nosaukums == nosaukums1, ir pieņemts, ka modeļa prognoze ir pareiza, un ja lietotaja_nosaukums != nosaukms1, tad ir pieņemts, ka modeļa prognoze nav pareiza. Šo informāciju varēs izmantot, lai grupētu bildes pēc nosaukuma un prognozes patiesības, un tālāk pārmācīt modeli, ar papildus jaunām bildēm.

## Tehnoloģiju steks

| Priekšgalsistēma  |                             Apraksts                              |
|:-----------------:|:-----------------------------------------------------------------:|
| Bootstrap CSS, JS | Satvars  adaptīvu un mobilajām ierīcēm paredzētu vietņu izstrādei |

| Aizmugursistēma |            Apraksts            |
|:---------------:|:------------------------------:|
|     Python      |     Programmēšanas valoda      |
|      Flask      | Tīmekļa lapu izstrādes satvars |
|     SQlite      |   Datu bāze datu glabāšanai    |

|                        Mašīnmācīšanās                         |                         Apraksts                         |
|:-------------------------------------------------------------:|:--------------------------------------------------------:|
| [Google Teachable  machine](teachablemachine.withgoogle.com/) |             Modeļa izstrādei,  eksportēšanai             |
|                          TensorFlow                           | Python  bibliotēka modeļa ielādei un prognozes veikšanai |

|   Izvietošana   |           Apraksts           |
|:---------------:|:----------------------------:|
|    Gunicorn     |       Tīmekļa serveris       |
|      NginX      |        Reverse proxy         |
| Virtuālā mašīna | Vieta, kur mājaslapa strādās |

Kā risinājums būs mājaslapa, kuras pamatnē būs Flask satvars un SQlite datubāze. Tiks izmantots viens no pazīstamākajiem python tīmekļa serveriem Gunicorn  kopā ar NginX kā reverse proxy (apgrieztais starpniekserveris). Risinājums tiks izvietots uz virtuālās mašīnas ar Ubuntu operētājsistēmu, un būs pieejams tiešsaistē pēc adreses [www.fishai.me](https://fishai.me).

## Novērtēšanas plāns

Atkarībā no mākslīgā tīkla veidošanas no nulles, Google Teachable Machine, ļauj mainīt ļoti ierobežotu skaitu ar parametru t.i. iterāciju skaits (epochs), bilžu skaits vienā iterācijā (batch size) un apmācības ātrums (learning rate), nu un protams, katras klases bilžu skaits. Ja risinājums tiktu veikts veidojot jaunu mākslīgo tīklu, tad tie parametri varētu būt bezgalīgi daudz, sākot no neironu skaita, izvietojumam, līdz visādām attēlā modifikācijām (rotācija, translācija, kontrasta palielināšana u.c.), lai neitralizētu noslieces uz aizspriedumiem.

Kopumā tika izveidoti 15 dažādi modeļi, kur

Eksperimenta parametri:

- Trenēšanas datu kopas izmērs, katrai sugai
- Izmantotais bilžu skaits vienā iterācija
- Apmācības ciklu daudzums

Eksperimenta rezultāti:

- Pareizi prognozētas zivis
- Procentuāli pareizi prognozētas zivis
- Vidējais laiks viens zivs atpazīšanai milisekundēs

Modeļu testēšanai tika izmantots, atsevišķs Python skripts, kurš ielādēja katru modeli, un deva prognozes par katru bildi no testa kopas. Skripts fiksēja, nepieciešamo laiku prognozes veikšanai un ievietoja to sarakstā, no kura pēc tam tika aprēķināta vidējā vērtība. Prognoze tika uzskatīta par pareizu, ja prognoze ar lielāko procentuālo varbūtību sakrita ar reālo zivs nosaukumu. Visi eksperimenta rezultāti ir redzami zemāk, un tie jau ir sakārtoti pēc pareizo prognozētu zivs daudzuma dilstošā secībā. Testa datu kopa sastāvēja no 72 bildēm un 7 zivs sugām – Asaris, Karpa, Lasis, Līdaka, Nēģis, Reņģe un Zutis.

| Trenēšanas datu kopas izmērs | Izmantotais bilžu skaits vienā iterācija | Apmācības ciklu daudzums | Pareizi prognozētas zivis | Procentuāli pareizi prognozētas zivis | Vidējais laiks viens zivs atpazīšanai, ms |
|------------------------------|------------------------------------------|--------------------------|---------------------------|---------------------------------------|-------------------------------------------|
| 100                          | 32                                       | 20                       | 61                        | 84.72%                                | 50.66                                     |
| 75                           | 16                                       | 30                       | 59                        | 81.94%                                | 50.96                                     |
| 75                           | 16                                       | 50                       | 59                        | 81.94%                                | 54.72                                     |
| 100                          | 16                                       | 20                       | 59                        | 81.94%                                | 52.49                                     |
| 75                           | 16                                       | 20                       | 58                        | 80.56%                                | 51.06                                     |
| 100                          | 16                                       | 30                       | 58                        | 80.56%                                | 51.14                                     |
| 100                          | 16                                       | 50                       | 58                        | 80.56%                                | 51.20                                     |
| 100                          | 64                                       | 30                       | 58                        | 80.56%                                | 49.71                                     |
| 100                          | 64                                       | 50                       | 58                        | 80.56%                                | 49.61                                     |
| 50                           | 16                                       | 30                       | 57                        | 79.17%                                | 51.02                                     |
| 100                          | 32                                       | 30                       | 56                        | 77.78%                                | 49.35                                     |
| 100                          | 64                                       | 20                       | 56                        | 77.78%                                | 49.39                                     |
| 50                           | 16                                       | 50                       | 55                        | 76.39%                                | 50.94                                     |
| 100                          | 32                                       | 50                       | 55                        | 76.39%                                | 50.09                                     |
| 50                           | 16                                       | 20                       | 54                        | 75.00%                                | 51.46                                     |

## Novērtēšanas secinājumi

Kā redzams, labākais modelis, kas arī tiks izmantots mūsu gala risinājumā, ar rezultātu 61 pareizi prognozētām zivīm no 72, jeb ar 84.72% precizitāti ir ar sekojošiem parametriem:

- Trenēšanas datu kopas izmērs - 100 bildes katrai sugai
- Izmantotais bilžu skaits vienā iterācija – 32 bildes
- Apmācības ciklu daudzums – 20 cikli

Runājot par modeļa patērēto laiku priekš zivs atpazīšanas, ir divas lietas, ko var piebilst. Pirmā visiem 15 modeļiem, tas laiks ir ļoti mazs, kas ir ± 50ms un reālajā dzīvē nebūs nekādas atšķirības starp 49ms un 55ms, tāpēc man liekas, ka tas ir ļoti mazsvarīgs faktors šajā novērtēšanā. Otrā lieta, visi modeļi ir veidoti pēc viena principa, jeb arhitektūras, kas nozīmē to, ka visiem modeļiem būtu jābūt līdzīgiem laikiem, jo tiem parametriem, ko mēs mainījām, nevajadzētu nekādīgi ietekmēt prognozēšanas laiku. Tāpēc tiek uzskatīts, ka laika atšķirība ir kļūdas robežās, un visiem modeļiem prognozēšanas laiks ir vienāds.

## Risinājuma apskatīšana

### 1. variants (Ieteicams)

Risinājums ir pieejams, pēc adreses [www.fishai.me](https://fishai.me). Tas ir gatavs lietošanai, vienīgi ir jāizveido savs personīgais konts ar reģistrēšanas palīdzību. Diemžēl mums nav lieka datora uz kura varētu turēt serveri visu laiku, tāpēc pirms apskatīšanas būtu jāpaziņo mums, lai varētu ieslēgt serveri, vai arī pateikt kurā dienā notiks apskatīšana, lai varētu atstāt serveri strādāt.

### 2. variants

Risinājumu var nokopēt uz lokālā datora un palaist ar Flask iebūvēto serveri, lai to izdarītu ir jāveic sekojošas darbības.

1. Nokopēt risinājumu no GitLab (Clone)
2. Uztaisīt jaunu virtuālo vidi jeb virtual environment (nav obligāti, bet ieteicams)
3. Uzinstalēt visas nepieciešamas bibliotēkas no faila `requirements.txt`, to var izdarīt ar komandu

   ```python
   pip install -r requirements.txt
   ```

4. Izveidot jaunu mapi jebkurā vietā uz datora. Šajā mapē glabāsies visas lietotāju iesūtītās bildes. (Diemžēl 
   nevarējām izdomāt, kā varētu iztikt bez tā, jo modelim obligāti vajag bildi, kas atrodas uz datora)
5. Failā `functions.py` izdzēst līnijas 55-58 un tajā vietā pievienot rindiņu

   ```python
    file_path = celš/uz/jaunizveidotumapi
   ```
6. Līdzīgi kā 5. punktā tajā pašā failā izdzēst līnijas 35-38 un tajā vietā pievienot rindiņu

   ```python
    csv_path = ceļš/līdz/latvian_udenstiplnes.csv
   ```

7. No virtuālās vides palaist skriptu `app.py`, kurš izveidos serveri uz 127.0.0.1:5000

##### Ieteikumi

- Visas šīs darbības ir ieteicams darīt ar PyCharm programmatūru, tā kā tur ir iebūvēts gan jaunas virtuālās vides izveide, gan automātiskā bibliotēku instalācija no faila `requirements.txt`
- Palaižot `app.py` caur PyCharm, logā Run/Debug Configurations, ir jāuzliek Working directory, kā `ceļš/līdz/mapei/fishai`
- Ja tomēr paliek problēmas ar ceļiem līdz failiem, tad nekas nepaliek, kā nomainīt relatīvus ceļus uz absolūtiem t.i.
  - Fails `functions.py` 31 līnija
  - Fails `app.py` 12 līnija
  - Fails `predictions.py` 5 līnija

 ## Prezentācijas plakāts

  ![Prezentācijas plakāts](https://i.ibb.co/QrTrjrn/plakats-PL.jpg)
