# Task Manager – Dokumentacja użytkownika (User Manual)

## 1. Wprowadzenie

**Task Manager** to prosta aplikacja webowa do zarządzania notatkami/zadaniami. Umożliwia:
- rejestrację i logowanie użytkowników,
- dodawanie notatek w kategoriach **Praca** i **Studia**,
- oznaczanie notatek jako wykonane / niewykonane,
- edycję i usuwanie własnych notatek,
- (dla administratora) zarządzanie użytkownikami oraz notatkami wszystkich użytkowników,
- (dla administratora) wysyłanie notatek do wybranego użytkownika.

Aplikacja działa w przeglądarce internetowej.

---

## 2. Role w systemie

W systemie występują dwie role:
- **user** – standardowy użytkownik,
- **admin** – administrator.

Uprawnienia:
- Użytkownik (**user**) widzi i modyfikuje **tylko swoje notatki**.
- Administrator (**admin**) ma dostęp do panelu administracyjnego, gdzie może zarządzać użytkownikami oraz wszystkimi notatkami.

System blokuje:
- zmianę roli samemu sobie,
- usunięcie samego siebie,
- odebranie roli lub usunięcie ostatniego administratora.

---

## 3. Wymagania systemowe

### 3.1. Dla użytkownika
- przeglądarka internetowa (Chrome, Firefox, Edge, Safari),
- dostęp do aplikacji,
- włączona obsługa JavaScript (zegar w pasku nawigacji).

### 3.2. Dla administratora
- konto z rolą **admin**.

---

## 4. Dostęp do aplikacji

- Strona startowa: `/`
- Rejestracja: `/register`
- Logowanie: `/login`
- Dashboard: `/dashboard`
- Panel administratora: `/admin`

---

## 5. Rejestracja i logowanie

### 5.1. Rejestracja
Użytkownik podaje email oraz hasło.  
Nie można zarejestrować konta na email, który już istnieje w systemie.

Po poprawnej rejestracji:
- konto otrzymuje rolę **user**,
- użytkownik jest informowany komunikatem,
- możliwe jest zalogowanie się do systemu.

### 5.2. Logowanie
Użytkownik loguje się za pomocą emaila i hasła.  
Po poprawnym logowaniu zostaje przekierowany do dashboardu.

### 5.3. Wylogowanie
Dostępne z menu nawigacyjnego.

---

## 6. Dashboard użytkownika

Dashboard zawiera:
- informację o zalogowanym użytkowniku,
- formularz dodawania notatek,
- listę notatek użytkownika,
- przyciski edycji, usuwania i zmiany statusu notatki.

---

## 7. Zarządzanie notatkami

### 7.1. Kategorie
Dostępne kategorie:
- Praca
- Studia

### 7.2. Ograniczenia
- maksymalna długość notatki: **500 znaków**,
- treść notatki nie może być pusta.

### 7.3. Operacje na notatkach
Użytkownik może:
- dodać notatkę,
- oznaczyć notatkę jako wykonaną lub niewykonaną,
- edytować notatkę,
- usunąć notatkę.

Użytkownik nie ma dostępu do notatek innych użytkowników.

---

## 8. Notatki od administratora

Administrator może wysyłać notatki do użytkowników.  
Takie notatki są widoczne na dashboardzie użytkownika i oznaczone jako pochodzące od admina.

---

## 9. Panel administratora

Administrator może:
- przeglądać listę użytkowników,
- zmieniać role użytkowników,
- usuwać użytkowników (z ograniczeniami),
- wysyłać notatki do użytkowników,
- edytować i usuwać notatki w systemie.

---

## 10. Bezpieczeństwo

- Hasła przechowywane są w postaci haszy.
- Dostęp do panelu admina jest ograniczony dekoratorem uprawnień.
- System uniemożliwia nieautoryzowane operacje.

---

## 11. Podsumowanie

Task Manager umożliwia prostą organizację notatek i zadań z podziałem na role użytkowników i administratorów. Projekt spełnia wymagania aplikacji MVC oraz prezentuje mechanizmy autoryzacji, walidacji i zarządzania danymi.
