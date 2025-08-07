import webbrowser
import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pohjalaisten Rapujuhlat 2025/title>
    <link rel="icon" href="🦀" type="image/x-icon">
    <style>
        body {
            font-family: 'Arial Nova Cond Light', 'Arial Narrow', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
            line-height: 1.6;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .main-title {
            font-size: 48px;
            color: #333;
            text-align: center;
            margin-bottom: 40px;
            font-weight: bold;
            border-bottom: 3px solid #333;
            padding-bottom: 20px;
        }
        .contents {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 40px;
            text-align: center;
        }
        .contents h2 {
            font-size: 24px;
            color: #333;
            margin-bottom: 15px;
        }
        .contents ul {
            list-style: none;
            padding: 0;
        }
        .contents li {
            margin-bottom: 10px;
        }
        .contents a {
            color: #cc0000;
            text-decoration: none;
            font-size: 18px;
        }
        .contents a:hover {
            text-decoration: underline;
        }
        .song {
            margin-bottom: 60px;
            padding: 30px;
            background-color: #fafafa;
            border-radius: 8px;
            border-left: 4px solid #cc0000;
        }
        .song-title {
            font-size: 36px;
            color: #333;
            margin-bottom: 30px;
            font-weight: bold;
            text-align: center;
        }
        .verse {
            font-size: 20px;
            color: #333;
            margin-bottom: 25px;
            white-space: pre-line;
            text-align: center;
        }
        .back-to-top {
            text-align: center;
            margin-top: 20px;
        }
        .back-to-top a {
            color: #cc0000;
            text-decoration: none;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="main-title">🦀 Rapujuhlat 2025 </div>
       
        <div class="contents">
            <h2>📋</h2>
            <ul>
                <li><a href="#hyvat-ystävät">1. Hyvät Ystävät </a></li>
                <li><a href="#helan-gar">2. Helan går </a></li>
                <li><a href="#aqua-vera">3. Aqua vera </a></li>
                <li><a href="#vesipoikien-marssi">4. Vesipoikien marssi </a></li>
                <li><a href="#internationalen">5. Internationalen </a></li>
                <li><a href="#pikku-kakkosen-posti">6. Pikku kakkosen posti </a></li>
                <li><a href="#minne">7. Minne! </a></li>
                <li><a href="#koskenkorva">8. Koskenkorva </a></li>
                <li><a href="#eurovision">9. Eurovision </a></li>
                <li><a href="#lapinkulta-kaanon">10. Lapinkulta-kaanon </a></li>
                <li><a href="#tanaan-otetaan">11. Tänään otetaan </a></li>
                <li><a href="#taalla-jallutahden-alla">12. Täällä jallutähden alla </a></li>
            </ul>
        </div>
       
        <div class="song" id="hyvat-ystävät">
            <div class="song-title">1. Hyvät Ystävät</div>
           
            <div class="verse">Hyvät ystävät juhla voi alkaa,
sankarille me nostamme maljaa.
Tääl ei juodakaan kolmosen kaljaa.
Meille viihdyn suo shampanja vaan.</div>
           
            <div class="verse">Hauska juomia kurkkuun on suistaa,
sitten opiskeluaikoja muistaa.
Yhteinen juomalaulumme luistaa,
juhlamieli on parhaimmillaan.</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="helan-gar">
            <div class="song-title">2. Helan går</div>
           
            <div class="verse">Helan går,
Sjung hoppfalderallanlallanlej!
Helan går,
Sjung hoppfalderallanlallanlej!</div>
           
            <div class="verse">Och den som inte helan tar,
Han ej heller halvan får.
Helan går!
Sjung hoppfalderallanlallanlej!</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="aqua-vera">
            <div class="song-title">3. Aqua vera</div>
            <div style="font-size: 16px; color: #666; text-align: center; margin-bottom: 20px; font-style: italic;">
                (sävel: Terve teille lintuset)
            </div>
           
            <div class="verse">Lauletaanpas vedestä,
Jota aina riittää.
Vaikka kuinka joisit sä,
Ei se lopu siitä.
Pikku Aqun jano on,
Niin myös Paulin, Anteron.
Ah, kun sentään hyvältä,
Paljas vesi maistuu.</div>
           
            <div class="verse">Och vatten och vatten
Och vatten är så gott,
Så rysligt, fasligt, billigt
Så hälsosamt och vått
Och vatten och vatten
Och vatten är så gott,
Så rysligt, fasligt, billigt
Så hälsosamt och vått
Ett, två, tre VATTEN!</div>
           
            <div class="verse">Entäs sitten aamulla,
On olo mitä parhain.
Kannat vettä saavilla,
Sängyn viereen varhain.
Aamuyöllä vessassa
Tuumit sormet kurkussa
Ah, kun sentään hyvältä paljas vesi maistuu.</div>
           
            <div class="verse">Och vatten och vatten
Och vatten är så gott,
Så rysligt, fasligt, billigt
Så hälsosamt och vått
Och vatten och vatten
Och vatten är så gott,
Så rysligt, fasligt, billigt
Så hälsosamt och vått
Ett, två, tre VATTEN!</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="vesipoikien-marssi">
            <div class="song-title">4. Vesipoikien marssi</div>
           
            <div class="verse">Pois se meistä, että täällä maisteltais ́
Noita pahan tuomia alkoholijuomia.
Vaikka henki keltä täällä haisteltais ́,
Niin huugo raikas sois ́!</div>
           
            <div class="verse">Hurraa, me nuoret vesipojat,
Pää on selvä meillä aina,
Krapulat ei meitä paina.
Hurraa, me nuoret vesipojat,
meillä luonto raitis on!</div>
           
            <div class="verse">Säyseästi näin kun aina elelee,
Itseksensä hissuksiin,
nenä kirjassansa kiinn ́.
Tarmokkaasti lasiin aina sylkäisee,
Siitä riemu verraton!</div>
           
            <div class="verse">Hurraa, me nuoret...</div>
           
            <div class="verse">Paha perii riettauden sellaisen,
Jota toiset harjoittaa,
Kun he itsens ́ juovuttaa.
Sukukunnan turma tuopi tuollainen,
kulttuurin turmion!</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="internationalen">
            <div class="song-title">5. Internationalen</div>
           
            <div class="verse">Mera brännvin i glasen,
mera glas på vårt bord,
mera bord på kalasen,
mer kalas på vår jord.</div>
           
            <div class="verse">Mera jordar kring måne,
mera måner till Mars,
mera marscher till Skåne,
mera Skåne, bevars, bevars, bevars!</div>
           
            <div class="verse">Lisää viinaa mun lasiin,
Lisää laseja pöydälle.
Lisää pöytiä näihin juhliin,
Lisää juhlia kansalle.</div>
           
            <div class="verse">Lisää kansaa Suomeen,
Lisää Suomea päälle maan.
Lisää maata Suomeen,
Marssitaan, marssitaan, Karjalaan,
KARJALAAN!</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="pikku-kakkosen-posti">
            <div class="song-title">6. Pikku kakkosen posti</div>
           
            <div class="verse">Pikku kakkosen
Posti postilokero 347
33101 Tampere 10
Pikku kakkosen posti</div>
           
            <div class="verse">Pikku kakkosen URL
h-t-t-p kaksoispiste kautta-kautta
w-w-w piste yle piste fi
Kautta tilde ransu</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="minne">
            <div class="song-title">7. Minne!</div>
           
            <div class="verse">Jag har tappat mitt minne!
Är jag svensk eller finne?
Kommer inte ihåg.</div>
           
            <div class="verse">Inne!
Är jag ut eller inne?
Jag har luckor i minne.
Så'n där små alkohål.</div>
           
            <div class="verse">Men besinn'er,
man tätar det med brännvin man får,
fastän minnet och helan går!</div>
           
            <div class="verse">Minne?
Muisti hävis mutt' minne?
Juhlista selvisimme
Muistikatkoja on.</div>
           
            <div class="verse">Minne?
lähtisin vaikka minne,
kunhan selvittäisimme
missä olemme nyt?</div>
           
            <div class="verse">Mutta tiedän mä keinon
mikä auttaapi tuo:
Ota ryyppy, ja muistis juo!</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="koskenkorva">
            <div class="song-title">8. Koskenkorva</div>
           
            <div class="verse">Ko-ko-ko-kosken – ko-ko-ko-korvaa,
siitä aina kunnon rä-kä-kä-kännit saa.
Ko-ko-ko-kosken – ko-ko-ko-korvaa,
siitä aina kunnon rä-kä-kä-kännit,
aina kunnon rä-kä-kä-kännit,
aina kunnon rä-kä-kä-kännit saa!</div>
           
            <div class="verse">La-la-la-lappeen - ra-ra-ra-ranta,
siellä aina kunnon rä-kä-kä-kännit saa!
La-la-la-lappeen - ra-ra-ra-ranta,
siellä aina kunnon rä-kä-kä-kännit,
aina kunnon rä-kä-kä-kännit
aina kunnon rä-kä-kä-kännit saa!</div>
           
            <div class="verse">Ki-ki-ki-kivääri - ko-ko-ko-komppania,
siellä aina kunnon rä-tä-tä-tä-tä-tä saa!
Ki-ki-ki-kivääri - ko-ko-ko-komppania,
siellä aina kunnon rä-tä-tä-tä-tä-tä,
aina kunnon rä-tä-tä-tä-tä-tä,
aina kunnon rä-tä-tä-tä-tä-tä saa!</div>
           
            <div class="verse">Ty-ty-ty-tykistö - pa-pa-pa-patteri,
siellä aina kunnon TUM saa!
Ty-ty-ty-tykistö - pa-pa-pa-patteri,
siellä aina kunnon TUM,
aina kunnon TUM,
aina kunnon TUM saa!</div>
           
            <div class="verse">Ti-ti-ti-tiedustelu - ko-ko-ko-komppania,
siellä aina kunnon - saa!
Ti-ti-ti-tiedustelu - ko-ko-ko-komppania,
siellä aina kunnon -,
aina kunnon -,
aina kunnon - saa!</div>
           
            <div class="verse">Ja siellä saa! (Ja siellä saa!)
Ja siellä saa! (Ja siellä saa!)
Ja siellä saa!</div>
           
            <div class="verse">A-a-a-aura - joen ranta,
siellä aina kunnon pussikaljat saa!
A-a-a-aura - joen ranta,
siellä aina kunnon pussikaljat,
aina kunnon pussikalja,
aina kunnon pussikaljat saa!</div>
           
            <div class="verse">Ta-ta-ta-tammer - kosken ranta,
siellä aina kunnon teinipillut saa!
Ta-ta-ta-tammer - kosken ranta,
siellä aina kunnon teinipillut,
aina kunnin teinipillut,
aina kunnon teinipillut saa!</div>
           
            <div class="verse">We-we-we-westendin ranta,
siellä aina isin Bemarissa saa!
We-we-we-westendin ranta,
siellä aina isin Bemarissa,
aina isin Bemarissa,
aina isin Bemarissa saa!</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="eurovision">
            <div class="song-title">9. Eurovision</div>
            <div style="font-size: 16px; color: #666; text-align: center; margin-bottom: 20px; font-style: italic;">
                (melodia: Euroviisu-teema)
            </div>
           
            <div class="verse">Ranskassa juodaan viiniä
Saksassa olutta, Venäjällä vodkaa.
Suomessa juodaan kaikkea,
Siis malja sille nostakaa!</div>
           
            <div class="verse">Norjassa poltetaan kirkkoja
Saksassa kirjoja, Venäjällä vodkaa.
Hollannissa poltetaan kaikkea,
Siis sätkä sille käärikää!</div>
           
            <div class="verse">Norjassa syödään lunta
Ruotsissa loskaa, Venäjällä paskaa.
Suomessa syödään kaikkea,
Siis perseet sinne kääntäkää!</div>
           
            <div class="verse">Ruotsissa pannaan miehiä
Saksassa huoria, Venäjällä väkisin
Suomessa pannaan kaikkea,
Siis malja sille nostakaa!</div>
           
            <div class="verse">Kirkossa lauletaan virsiä
Tuskassa heviä, eläkkeellä humppaa
Sitseillä lauletaan kaikkea
Siis malja sille nostakaa!</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="lapinkulta-kaanon">
            <div class="song-title">10. Lapinkulta-kaanon</div>
            <div style="font-size: 16px; color: #666; text-align: center; margin-bottom: 20px; font-style: italic;">
                (melodia: Jaakko-kulta)
            </div>
           
            <div class="verse">Lapin Kulta, Lapin Kulta,
Karjala, Karjala,
Sininen ja Olvi, Sininen ja Olvi,
Koff, Koff, Koff, Koff, Koff, Koff.</div>
           
            <div class="verse">Koskenkorva, Koskenkorva,
pontikka, pontikka,
sinoli ja lasoli, sinoli ja lasoli,
tärpätti, tärpätti.</div>
           
            <div class="verse">Viru Valge, Viru Valge,
Saarenmaa, Saarenmaa,
Laua-viin, Laua-viin,
Rock A. le Coq, Rock A. le Coq.</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="tanaan-otetaan">
            <div class="song-title">11. Tänään otetaan</div>
            <div style="font-size: 16px; color: #666; text-align: center; margin-bottom: 20px; font-style: italic;">
                (melodia: Joulu on taas)
            </div>
           
            <div class="verse">:,: Tänään otetaan, tänään otetaan
helvetin paljon viinaa. :,:
:,: Huomenna on, huomenna on
helvetin kova krapula. :,:</div>
           
            <div class="verse">:,: I dag ska vi ha, i dag ska vi ha
helvetes mycket brännvin. :,:
:,: I morgon ska vi ha, i morgon ska vi ha
helvetes kova krapula. :,:</div>
           
            <div class="verse">:,: Täna võtame, täna võtame
kuradima palju viina. :,:
:,: Homme meil on, homme meil on
kuradima kõva pohmakas. :,:</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
 
        <div class="song" id="taalla-jallutahden-alla">
            <div class="song-title">12. Täällä jallutähden alla</div>
            <div style="font-size: 16px; color: #666; text-align: center; margin-bottom: 20px; font-style: italic;">
                (melodia: Täällä pohjantähden alla)
            </div>
           
            <div class="verse">Täällä jallutähden alla korkeimmalla kukkulalla.
Katson läpi lasin tyhjän, sen täytän uudestaan.
Täällä jallutähden alla, lasi täyttyy leikatulla.
Siitä suojakseni peiton, minä itselleni saan.</div>
           
            <div class="verse">Ja alla jallutähden, minä otan, yhden tähden,
ja vain jallutähden nähden, itken ilon kyyneleen.</div>
           
            <div class="verse">Täällä jallutähden alla, kova jano laulajalla.
Huolet viinaa naukkaamalla siirtyy päivään huomiseen
Täällä jallutähden alla, hiipii sieluun asti halla,
mutta korkin avaamalla, sulaa sydän uudelleen.</div>
           
            <div class="verse">Ja alla jallutähden…</div>
           
            <div class="back-to-top">
                <a href="#top">↑ Back to top</a>
            </div>
        </div>
    </div>
</body>
</html>"""
 
# Write the HTML content to a file
html_filename = "rapujuhlat2025.html"
html_filepath = os.path.join(os.getcwd(), html_filename)
with open(html_filepath, "w", encoding="utf-8") as file:
    file.write(html_content)
 
print(f"HTML file '{html_filename}' has been created successfully!")
print("Opening the HTML file...")
webbrowser.open(f"file://{html_filepath}")
 