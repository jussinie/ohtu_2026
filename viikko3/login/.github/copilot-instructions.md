# Agent Instructions

## Projekti ja komennot
- Projekti on Python uv -projekti. Kaikki komennot suoritetaan muodossa `uv run ...`.
- Työskentelyhakemisto on projektin juuri.

## Sovelluksen käynnistys
- Käynnistä sovellus komennolla: `uv run python src/index.py`
- Sovellus toimii portissa 5001 (`http://localhost:5001`).

## Testaus (Robot Framework)
- Suorita testit komennolla: `uv run robot src/tests`
- Yksittäisen testitiedoston suoritus: `uv run robot src/tests/login.robot`
- **Huomio:** Sovelluksen on oltava käynnissä testien aikana.
- Testit suoritetaan selaimella (Browser-kirjasto) ja ne nollaavat sovelluksen tilan pyynnöllä `POST /tests/reset`.

## Sovellusrakenne ja validointi
- **Validointi:** Käyttäjätunnuksen ja salasanan validointi tapahtuu tiedostossa `src/services/user_service.py` (`UserService.validate` -metodissa).
- **Autentikointi:** Kirjautumisen tarkistus tehdään samassa tiedostossa (`UserService.check_credentials`).
- **Tallennus:** `src/repositories/user_repository.py` tallentaa käyttäjätiedot keskusmuistiin (`self._users`), tietokantaa ei käytetä.
- **Reitit ja sovelluslogiikka:** `src/app.py` määrittää Flask-reitit ja näkymät.
