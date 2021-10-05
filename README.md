# Ievads

## Problēmas nostādne

Attēlu atpazīšana, kas ir pamatā jebkurai programmai, kas spēj identificēt priekšmetus bildē vai attēlā, balstās uz mašinmācīšanos. Tādas lietotnes kā [Google Lens](https://lens.google/) vai [PictPicks](https://play.google.com/store/apps/details?id=jp.mydns.usagigoya.imagesearchviewer&hl=en&gl=US), spēj vispārīgi identificēt objektus attēlā, tādus, ka zivs, pudele, apavi, utt. Tādas lietotnes parasti nedod paplašinātu informāciju par identificētu objektu, kā, piemēram, mūsu gadijumā zivs sugu. Aplikācijas, kas spēj iedod lietotājam paplašinātu informāciju, parasti ir ļoti ierobežotas, ar to, kādu datu kopu izmantoja izstrādātaji, lai apmācītu modeli. Mūsu gadijumā, tas nozīmē, ka ne visas Latvijas zivis, varēs veiksmīgi būt identificētas, jo banāli modelis nebija apmācīts ar tām. Tāpēc ir vajadzīgs risinājums, kas spēs veiksmīgi identificēt populārākās Latvijas zivs sugas.

## Mērķis

Izveidot lietotni, kas balstoties uz dziļās mašīnmācīšanās spēs atpazīst lietotāja lejuplādēto Latvijas zivs sugu un saglabāt to lietotāja identificēto zivju bibliotēkā.

# Līdzīgo risinājumu pārskats

## Tehniskais Risinājums

Attēlu atpazīšana, ir datorredzes apakškopa, kas ietver sevī vizuālu meklēšanu, semantisko segmentāciju un objektu identificēšanu no attēliem. Attēla atpazīšanas būtība ir algoritms, kas ņem attēlu kā ievadi un interpretē to, vienlaikus norādot šim attēlam klases un etiķetes. Piemēri ar dažiem attēlu klasifikācijas algoritmiem:

- [**Bag of visual words (BOVW)**](https://towardsdatascience.com/bag-of-visual-words-in-a-nutshell-9ceea97ce0fb)
- [**Support-vector machine (SVM)**](https://en.wikipedia.org/wiki/Support-vector_machine)
- [**K-nearest neighbors (KNN)**](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)
- [**Logistic regression**](https://medium.com/swlh/logistic-regression-for-image-classification-e15d0ae59ce9)
- [**Convolutional neural network (CNN)**](https://towardsdatascience.com/wtf-is-image-classification-8e78a8235acb)

## Līdzīgi risinājumi:

### 1. [FishVerify](https://www.fishverify.com/)

#### Iespējas
- Lejuplādēt vai nofotografēt zivis
- Sekot jūras laikapstākļiem
- Automātiskā nozvejas žurnāla izveide ar ģeolokāciju
- Zvejas noteikumi attiecībā pret konkrētu sugu
#### Pozitīvi
- Virtuālais maks, lai uzglabātu makšķerēšanas licences un atļaujas
- Papildus informācija par zivs izskatu, dzīvesvietu, izmēru un uzvedību
- Iespēja iesniegt savu nozveju, lai kāds no viņu ekspertiem to identificētu
#### Negatīvi
- Par brīvu var identificēt tikai 5 zivs, tālāk 6 Eur par 5 identifikācijām vai 41.19 Eur/gadā
- Viss izņemot zivs identifēšanas, nestrādā Latvijā, t.i. atļaujas, zveju licenses, laikapstākļi
- No Latvijas 5 zivīm, 1 atpazina pareizi, 1 atpazina nepareizi, pārējos 3 "Not sure what it is"

### 2. [Picture Fish - Fish Identifier](https://play.google.com/store/apps/details?id=com.glority.picturefish&hl=en&gl=US)

#### Iespējas
- Lejuplādēt vai nofotografēt zivis
- Saraksts ar identificētām zivīm

#### Pozitīvi
- Pēc identifikācijas dod 3 izvēles ar sugas izvēli, sakārtoti no labāka uz sliktāka
- Atpazīst zivis grūtos apstākļos no Latvijas 5 zivīm, 4 identificēja pareizi un vienu nepareizi
- Apraksts par zivi, zivs zinātniskais nosaukums, atbildes uz visbiežāk cilvēku jautājumiem par šo zivi, un citas bildes ar šo zivi
- Nav reklāmas

#### Negatīvi
- 7 Dienas par brīvu, tad 21.99 Eur/gadā
- Nav iespējams, pašam identificēt zivi


### 3. [Fish Identification](https://fishid.tapcurate.com/)

#### Iespējas
- Lejuplādēt vai nofotografēt zivis
- Organizēts saraksts ar identificētām zivīm

#### Pozitīvi
- Parādā "Confidence" līmeni
- Parādā citas bildes ar to pašu zivi, priekš salīdzīnāšanas

#### Negatīvi
- Pieejams tikai App Store
- No Latvijas 5 zivīm, neviena netika atpazīta



