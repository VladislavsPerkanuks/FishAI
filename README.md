# Ievads

## Problēmas nostādne

Attēlu atpazīšana, kas ir pamatā jebkurai programmai, kas spēj identificēt priekšmetus bildē vai attēlā, balstās uz mašinmācīšanos. Tādas lietotnes kā [Google Lens](https://lens.google/) vai [PictPicks](https://play.google.com/store/apps/details?id=jp.mydns.usagigoya.imagesearchviewer&hl=en&gl=US), spēj vispārīgi identificēt objektus attēlā, tādus, ka zivs, pudele, apavi, utt. Tādas lietotnes parasti nedod paplašinātu informāciju par identificētu objektu, kā, piemēram, mūsu gadijumā zivs sugu. Aplikācijas, kas spēj iedod lietotājam paplašinātu informāciju, parasti ir ļoti ierobežotas, ar to, kādu datu kopu izmantoja izstrādātaji, lai apmācītu modeli. Mūsu gadijumā, tas nozīmē, ka ne visas Latvijas zivis, varēs veiksmīgi būt identificētas, jo banāli modelis nebija apmācīts ar tām. Tāpēc ir vajadzīgs risinājums, kas spēs veiksmīgi identificēt populārākās Latvijas zivs sugas.

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

### Novērtēšanas kritēriji

Galvenais novērtēšanas kritērijs būs - cik Latvijas zivju sugu, algoritms būs spējīgs precīzi atpazīt.

### Izvēlētais algoritms

Risinājuma izveidei, tiks izmantots dziļās mašinmācīšanās algoritms - Convolutional Neural Network, jeb īsumā CNN. Priekšrocībās šīm algoritmam ir:

- Tas spēj efektīvi samazināt parametru skaitu, nezaudējot modeļa kvalitāti (Ātrāka/Mazāk resursus prasoša mācīšanās)
- Ir pieejami gatavi modeļi, kurus var pārmacīt uz mūsu problēmu, kā piemēri, VGG16, Xception, ResNet, u.c. (Transfer Learning)
- Tas automātiski nosaka svarīgākās klases iezīmes/īpatnības bez cilvēka uzraudzības/iejaukšanās.

## Līdzīgi tehniskie risinājumi:

### Lietotnes:

1. [FishVerify](https://www.fishverify.com/)
2. [Picture Fish - Fish Identifier](https://play.google.com/store/apps/details?id=com.glority.picturefish&hl=en&gl=US)
3. [Fishbrain](https://fishbrain.com/)
4. [Fish Identification - Fish Scanner](https://play.google.com/store/apps/details?id=e.fish.natureai&hl=en&gl=US)
5. [Fishsnap - Fish identifier](https://apps.apple.com/us/app/fishsnap-fish-identifier/id1571610312)

### Vērtēšanas kritērīji:

1. **Precizitāte** - cik no 5 Latvijas zivīm, lietotne spēja precīzi atpazīt
2. **Izmaksas** - cik izmaksā lietotne
3. **Lietotāju vērtējums** - kā lietotāji ir novērtējuši lietotni
4. **Pieejamība** - uz kādām platformām ir pieejama lietotne

### Vērtēšanas rezultāti:

| Lietotne                           | Precizitāte | Izmaksas       | Pieejamība   | Lietotāju atsauksmes                    |
| ---------------------------------- | ----------- | -------------- | ------------ | --------------------------------------- |
| FishVerify                         | 1/5         | 41.19 Eur/gadā | Android, iOS | 2.5/5 Google play <br />3.8/5 App Store |
| Picture Fish - Fish Identifier     | 4/5         | 21.99 Eur/gadā | Android, iOS | 3.8/5 Google play <br />4.0/5 App Store |
| Fishbrain                          | 3/5         | 84.99 Eur/gadā | Android, iOS | 3.9/5 Google play<br />4.7/5 App Store  |
| Fish Identification - Fish Scanner | 0/5         | Bezmaksas      | Android      | 3.1/5 Google play                       |
| Fishsnap - Fish identifier         | 2/5         | 43.20 Eur/gadā | iOS          | -                                       |


# Tehniskais Risinājums

## Prasības

**MoSCoW metode**:

| Must haves                                  | Should haves                       | Could haves                    | Would not haves     |
| :------------------------------------------ | :--------------------------------- | :----------------------------- | :------------------ |
| Identificēt zivis vismaz ar 60% precizitāti | Tiek parādīts "Confidence" līmenis | Modeļa nepārtraukta uzlabošana | Maškerēšanas padomi |
| Bibliotēka ar identificētām zivīm           | Tiek noteikta zivs noķeršanas lokācijas vieta   |  Zivs lielums tiek noteikts pēc bildes| Likumdošana|
| CRUD operācijas                             |                                    |                                | Laikapstākļi|

## Konceptu modelis

### Modelis

![Koncepta datubāze](https://i.ibb.co/dt0SgSD/Screenshot-2021-11-12-103733.png)

### Apraksts

**Lietotājs** - iekļauj sevī informāciju par lietotāju

**Loms** - iekļauj sevī informāciju par konkrētā lietotāja lomu t.i. loma bilde, datums, svars u.c

**Prognozes** - iekļauj sevī informāciju par konkrētā loma dziļās mašīnmācīšānās prognozēm. Šeit ir informācija par prognozes zivs nosaukumu un pašu prognozi (procentos). Kopumā lietotājam tiks izvadītās trīs iespējamākās prognozes. Piem, Nosaukums1 - lasis, procenti1 - 56%, Nosaukums2 - karpa, procenti2 - 33% un Nosaukums3 - līdaka, procenti3 - 11%. Lietotājam ir iespēja iedot savu nosaukumu zivij, rindā lietotaja_nosaukums, ja lietotajs to nav izdarījis, tad lietotaja_nosaukums būs vienāds ar nosaukums1. Tāda pieeja, ļauj saprast vai modelis ir pareizi prognozējis zivs nosaukumu, citos vārdos – ja lietotaja_nosaukums == nosaukums1, ir pieņemts, ka modeļa prognoze ir pareiza, un ja lietotaja_nosaukums != nosaukms1, tad ir pieņemts, ka modeļa prognoze nav pareiza. Šo informāciju varēs izmantot, lai grupētu bildes pēc nosaukuma un prognozes patiesības, un tālāk pārmācīt modeli, ar papildus jaunām bildēm.

## Tehnoloģiju steks

| Priekšgalsistēma  |                           Apraksts                           |
| :---------------: | :----------------------------------------------------------: |
| Bootstrap CSS, JS | Satvars  adaptīvu un mobilajām ierīcēm paredzētu vietņu izstrādei |

| Aizmugursistēma |            Apraksts            |
| :-------------: | :----------------------------: |
|     Python      |     Programmēšanas valoda      |
|      Flask      | Tīmekļa lapu izstrādes satvars |
|     SQlite      |   Datu bāze datu glabāšanai    |

|                        Mašīnmācīšanās                        |                         Apraksts                         |
| :----------------------------------------------------------: | :------------------------------------------------------: |
| [Google Teachable  machine](teachablemachine.withgoogle.com/) |             Modeļa izstrādei,  eksportēšanai             |
|                          TensorFlow                          | Python  bibliotēka modeļa ielādei un prognozes veikšanai |

|   Izvietošana   |              Apraksts              |
| :-------------: | :--------------------------------: |
|    Werkzeug     | Iebūvētais flask  tīmekļa serveris |
| Python anywhere |       Izvietošanas  serveris       |

Kā risinājums būs mājaslapa, kuras pamatnē būs Flask satvars un SQlite datubāze. Tiks izmantots iebūvetais flask web serveris - Werkzeug.
