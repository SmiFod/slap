# 📘 Dokumentasjon for Slap

Dette dokumentet er laget som del av faget **Brukerstøtte** og gir en grundig oversikt over hvordan Slap fungerer, hvordan det settes opp, og hvordan brukere og administratorer kan få hjelp.

## 1. Introduksjon

Slap er en webapplikasjon utviklet med Flask (Python) og kjører på en Raspberry Pi. Applikasjonen bruker MariaDB for datalagring og tilbyr en enkel og responsiv frontend bygget med HTML, CSS og JavaScript.

Formålet med Slap er å demonstrere en fullstack applikasjon med backend, frontend, database og drift.

---

## 2. Systemkrav

### Maskinvare
- Raspberry Pi (eller en vanlig server/PC)
- SD-kort (minst 16 GB anbefales)
- Internett-tilkobling
- Tastatur og skjerm (ved lokal installasjon)

### Programvare
- Python 3.x
- Flask
- MariaDB
- Nginx
- Git
- Nettleser (Chrome, Firefox, etc.)

---

## 3. Installasjonsveiledning

### Trinn 1: Klon prosjektet

```bash
git clone https://github.com/SmiFod/slap.git
cd slap
```

### Trinn 2: Installer avhengigheter

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Trinn 3: Konfigurer databasen

Logg inn i MariaDB og kjør følgende kommandoer:

```sql
CREATE DATABASE slap_db;
CREATE USER 'slap_user'@'localhost' IDENTIFIED BY 'dittpassord';
GRANT ALL PRIVILEGES ON slap_db.* TO 'slap_user'@'localhost';
FLUSH PRIVILEGES;
```

### Trinn 4: Start applikasjonen

```bash
python app.py
```

Gå til `http://localhost:5000` i nettleseren din for å se applikasjonen.

---

## 4. Brukermanual

- Åpne applikasjonen i en nettleser
- Naviger mellom sidene via lenker eller menyer
- Fyll inn nødvendige skjema og trykk "Send"
- Ved feil vises en feilmelding

---

## 5. Feilsøking

| Problem | Løsning |
|--------|---------|
| Klarer ikke koble til databasen | Sjekk at MariaDB kjører og at brukernavn/passord er riktig |
| Får feilmelding ved kjøring av `app.py` | Sjekk at alle avhengigheter er installert |
| Nettleseren finner ikke siden | Sørg for at Flask kjører på port 5000 og at brannmuren tillater tilkobling |

---

## 6. Vedlikehold

- **Oppdater avhengigheter**: `pip install --upgrade -r requirements.txt`
- **Backup database**: Bruk `mysqldump slap_db > backup.sql`
- **Loggfil**: Flask-logg kan sees i terminalen. Nginx-logger finnes i `/var/log/nginx/`

---

## 7. Brukerstøtte

- Åpne et Issue på GitHub: [https://github.com/SmiFod/slap/issues](https://github.com/SmiFod/slap/issues)
- Kontakt utvikler ved spørsmål

---

## 8. Vedlegg

- Eksempel på database-skjema
- Kommandoer for drift og feilsøking
- Ordliste:  
  - **Backend**: Kode som kjører på serveren (Python/Flask)  
  - **Frontend**: Det brukeren ser (HTML/CSS/JS)  
  - **Database**: Lagrer data (MariaDB)  


