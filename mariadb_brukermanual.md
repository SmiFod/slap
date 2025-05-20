# 📘 Brukermanual: Opprette Bruker og Gi Rettigheter i MariaDB

Denne brukermanualen beskriver hvordan du oppretter en ny bruker i MariaDB og gir nødvendige privilegier (rettigheter).

---

## ✅ Forutsetninger

- Du må ha MariaDB installert på systemet ditt.
- Du må ha tilgang til MariaDB som `root` eller en bruker med `CREATE USER` og `GRANT` privilegier.

---

## 🔐 Logg inn i MariaDB

Åpne terminal og skriv:

```bash
mysql -u root -p
```

Skriv inn passordet når du blir spurt.

---

## 👤 Opprette en ny bruker

Slik lager du en ny bruker:

```sql
CREATE USER 'brukernavn'@'localhost' IDENTIFIED BY 'passord';
```

**Eksempel:**

```sql
CREATE USER 'emilie'@'localhost' IDENTIFIED BY 'sterkpassord123';
```

> `localhost` betyr at brukeren kun kan logge inn fra den lokale maskinen.

---

## 🛡️ Gi privilegier til brukeren

Gi alle rettigheter til en spesifikk database:

```sql
GRANT ALL PRIVILEGES ON databasenavn.* TO 'brukernavn'@'localhost';
```

**Eksempel:**

```sql
GRANT ALL PRIVILEGES ON skoleapp.* TO 'emilie'@'localhost';
```

---

## 🔄 Oppdater privilegier

Etter å ha gitt rettigheter, kjør:

```sql
FLUSH PRIVILEGES;
```

---

## 📋 Se hvilke rettigheter en bruker har

```sql
SHOW GRANTS FOR 'brukernavn'@'localhost';
```

---

## ❌ Slette en bruker (valgfritt)

```sql
DROP USER 'brukernavn'@'localhost';
```

---

## ✅ Ferdig!

Nå har du opprettet en ny bruker og gitt nødvendige rettigheter i MariaDB.
