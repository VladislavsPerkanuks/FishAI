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

## Līdzīgi tehniskie risinājumi:

### Lietotnes:

1. [FishVerify](https://www.fishverify.com/)
2. [Picture Fish - Fish Identifier](https://play.google.com/store/apps/details?id=com.glority.picturefish&hl=en&gl=US)
3. [Fishbrain](https://fishbrain.com/)
4. [Fish Identification - Fish Scanner](https://play.google.com/store/apps/details?id=e.fish.natureai&hl=en&gl=US)
5. ...

### Vērtēšanas kritērīji:

**1. Precizitāte** - cik no 5 Latvijas zivīm, lietotne spēja precīzi atpazīt
**2. Izmaksas** - cik izmaksā lietotne
**3. Lietotāju vērtējums** - kā lietotāji ir novērtējuši lietotni
**4. Pieejamība** - uz kādām platformām ir pieejama lietotne

### Vērtēšanas rezultāti:

| Lietotne                           | Precizitāte | Izmaksas       | Pieejamība   | Lietotāju atsauksmes                    |
| ---------------------------------- | ----------- | -------------- | ------------ | --------------------------------------- |
| FishVerify                         | 1/5         | 41.19 Eur/gadā | Android, iOS | 2.5/5 Google play <br />3.8/5 App Store |
| Picture Fish - Fish Identifier     | 4/5         | 21.99 Eur/gadā | Android, iOS | 3.8/5 Google play <br />4.0/5 App Store |
| Fishbrain                          | 3/5         | 84.99 Eur/gadā | Android, iOS | 3.9/5 Google play<br />4.7/5 App Store  |
| Fish Identification - Fish Scanner | 0/5         | Bezmaksas      | Android      | 3.1/5 Google play                       |



# Tehniskais Risinājums

## Prasības

**MoSCoW metode**:

| Must haves                                  | Should haves                       | Could haves                    | Would not haves     |
| :------------------------------------------ | :--------------------------------- | :----------------------------- | :------------------ |
| Identificēt zivis vismaz ar 60% precizitāti | Tiek parādīts "Confidence" līmenis | Modeļa nepārtraukta uzlabošana | Maškerēšanas padomi |
| Bibliotēka ar identificētām zivīm           |                                    |                                |                     |
| CRUD operācijas                             |                                    |                                |                     |

## Konceptu modelis



![Koncepta datubāze](https://i.ibb.co/sFNKxBC/Untitled-1.png)
