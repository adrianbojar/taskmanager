from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NotePresenter:
    """
    Klasa bazowa (rodzic) — definiuje wspólny interfejs dla prezentacji notatki.
    To jest baza do POLIMORFIZMU: template/kod używa NotePresenter,
    ale realnie dostaje jedną z klas potomnych.
    """
    category: str
    is_done: bool

    @property
    def source_label(self) -> str:
        """Tekst o źródle notatki (nadpisywany w klasach potomnych)."""
        return "Notatka"

    @property
    def badge_text(self) -> str:
        """Krótki badge/etykieta (nadpisywane)."""
        return "Własna"

    @property
    def badge_class(self) -> str:
        """Klasa CSS dla badge (nadpisywane)."""
        return "badge"


@dataclass(frozen=True)
class UserNotePresenter(NotePresenter):
    """Klasa potomna — prezentacja notatki użytkownika."""
    @property
    def source_label(self) -> str:
        return "Twoja notatka"

    @property
    def badge_text(self) -> str:
        return "Własna"

    @property
    def badge_class(self) -> str:
        return "badge badge--user"


@dataclass(frozen=True)
class AdminNotePresenter(NotePresenter):
    """Klasa potomna — prezentacja notatki wysłanej przez admina."""
    @property
    def source_label(self) -> str:
        return "Notatka od admina"

    @property
    def badge_text(self) -> str:
        return "Admin"

    @property
    def badge_class(self) -> str:
        return "badge badge--admin"