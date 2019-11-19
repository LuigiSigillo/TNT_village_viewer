# TNT_village_viewer (ENGLISH)
A tribute to the TNT community.
# Disclaimer
The csv file containing the torrents is available on the TNT village website, so it is NOT present in this repository. It is the user's responsibility to download it at his own risk.
## What purpose does it serve ?
Since TNT village closed, it is no longer possible to access their site and consult an entire database of multimedia contents of any category. However, the moderators wanted to leave on their website a ZIP file containing a csv file which is basically the database of all the releases published over time. In order to have easier access to the contents and to have the convenience of a direct magnet connection, I decided to create this small and basic program.
## How does it work ?
1. Download and extract the repository into a folder.
2. Download from the [TNT site](http://www.tntvillage.scambioetico.org/) and extract the csv file contained in the archive
3. Move the csv file into the folder where you extracted the repository
4. Open the terminal and go to the repository folder
7. Execute the command to install the required packages:

    ```pip install -r requirements.txt```
6. Start the program with the command:

    ```python Main.py```

7. Perform a search, select the torrent from the list that appears, and finally click on the Download button. If everything went well and you have a Torrent client installed, it should already open with the torrent ready to be added to the download.

## If you are lazy
Follow the steps in the previous section up to and including point 4.
Execute the command to install the required package:

   ```pip install pyinstaller```

After placing yourself in the repository folder run the following command if you use Windows:

   ```pyinstaller -F --onefile --windowed -icon icon.ico --add-data dump_release_tntvillage_2019-08-30.csv;. Main.py```

if you are using MacOS or Linux use this instead:

   ```pyinstaller -F --onefile --windowed -icon icon.ico --add-data dump_release_tntvillage_2019-08-30.csv:. Main.py```

Once the process is finished, the "dist" folder will be created in which there will be a single executable file, which can be run rather than opening the command line each time.

# TNT_village_viewer (ITALIAN)
Un omaggio alla community di TNT.
# Disclaimer
Il file csv contenente i torrent è disponibile sul sito di TNT village, quindi NON è presente in questa repository. Sarà compito dell'utente scaricarlo a suo rischio e pericolo.
## A che serve ?
Da quando TNT village ha chiuso, non è più possibile accedere al loro sito e consultare un intero database di contenuti multimediali di qualsisi categoria. I moderatori hanno però voluto lasciare disponibile sul loro sito un file ZIP contenente un file csv che è sostanzialmente il database di tutte le release pubblicate nel corso del tempo. Per poter accedere in maniera più facile ai contenuti e per poter avere la comodità di un collegamento magnet diretto, ho deciso di crere questo piccolo e basilare programma.
## Come funziona ?
1. Scaricate ed estraete in una cartella la repository.
2. Scaricate dal [sito di TNT](http://www.tntvillage.scambioetico.org/) ed estraete il file csv contenuto all interno dell archivio
3. Spostate il file csv all'interno della cartella nella quale avete estratto la repository
4. Aprite il terminale e posizionatevi all interno della cartella della repository
5. Eseguite il comando per installare i prerequisiti necessari:

     ```pip install -r requirements.txt```
6. Avviate il programma con il comando:

     ```python Main.py```
7. Eseguite una ricerca, selezionate il torrent dalla lista che apparirà, e infine cliccate sul tasto Download. Se tutto è andato a buon fine e avete un client Torrent installato, dovrebbe aprirsi già con il torrent pronto da aggiungere al download.

## Se sei pigro
Segui i passi della sezione precedente fino al punto 4 compreso.
Execute the command to install the required package:

   ```pip install pyinstaller```

Dopo esserti posizionato nella cartella della repository esegui il seguente comando se usi Windows:

   ```pyinstaller -F --onefile --windowed --add-data -icon icon.ico dump_release_tntvillage_2019-08-30.csv;. Main.py```

se usi MacOS o Linux usa questo:

   ```pyinstaller -F --onefile --windowed --add-data -icon icon.ico dump_release_tntvillage_2019-08-30.csv:. Main.py```

Una volta finito il processo, si sarà creata la cartella "dist" dentro al quale sarà presente un unico file eseguibile, da poter eseguire piuttosto che aprire ogni volta la riga di comando.
