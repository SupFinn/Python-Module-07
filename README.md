> *This project has been created as part of the 42 curriculum by rhssayn.*

# 🎴 DataDeck
### *Master the Art of Abstract Card Architecture*
---

## 📌 Description
**DataDeck** is a comprehensive Python project focused on mastering **advanced object-oriented programming patterns** essential to enterprise-level systems:
**abstract base classes, multiple inheritance, design patterns, and interface composition**.

Set in the *Trading Card Game Universe*, this project transforms complex architectural concepts into concrete,
game-inspired challenges. You will design card blueprints, build factory systems,
implement strategic gameplay engines, and orchestrate tournament platforms using
professional Python patterns.

This project emphasizes **architectural thinking, design pattern mastery, and scalable system design** —
skills every professional software architect must command.

---

## 🎯 Project Objectives
By completing this project, you will learn how to:
- 🏗️ Design abstract base classes that define universal contracts
- 🎭 Implement multiple interfaces and multiple inheritance patterns
- 🏭 Use Abstract Factory Pattern for flexible object creation
- 🎯 Apply Strategy Pattern for dynamic behavior selection
- 🔗 Compose complex systems through interface layering
- 💡 Build extensible, maintainable game engines
- 🎪 Create sophisticated tournament and ranking systems
---

## 🧪 Exercises Overview

### 🏛️ Exercise 0 — Card Foundation
Master abstract base classes and create the universal card blueprint.
Design an abstract `Card` class that defines the contract all cards must follow,
then implement your first concrete card type: `CreatureCard`.

**Key Concepts:** Abstract Base Classes (ABC), inheritance, abstract methods

---

### 🎒 Exercise 1 — Deck Builder
Implement multiple concrete card types that all respect the same interface.
Build `SpellCard`, `ArtifactCard`, and a complete `Deck` management system
that works with any card type through polymorphism.

**Key Concepts:** Polymorphism, concrete implementations, class hierarchies

---

### ⚡ Exercise 2 — Ability System
Design multiple abstract interfaces using composition and multiple inheritance.
Create `Combatable` and `Magical` interfaces, then build an `EliteCard`
that simultaneously implements multiple abilities.

**Key Concepts:** Multiple interfaces, multiple inheritance, interface composition

---

### 🎮 Exercise 3 — Game Engine
Build a sophisticated game engine using Abstract Factory and Strategy Patterns.
Create `GameStrategy` and `CardFactory` interfaces with concrete implementations
like `AggressiveStrategy` and `FantasyCardFactory`.

**Key Concepts:** Abstract Factory Pattern, Strategy Pattern, composition over inheritance

---

### 🏆 Exercise 4 — Tournament Platform
Combine everything into a unified tournament management system.
Build `Rankable` interface and `TournamentCard` with tournament capabilities,
then create a `TournamentPlatform` that manages matches, rankings, and leaderboards.

**Key Concepts:** Advanced composition, ranking systems, tournament management

---

## ⚙️ Rules & Constraints
- Python **3.10+**
- Code must follow **flake8** coding standards
- **Type hints required** for all function signatures and class methods
- Authorized imports:
  - `abc` - Abstract Base Classes (essential)
  - `typing` - Advanced type hints
  - `random` - Card shuffling and game randomness
  - `enum` - Card types and rarities
  - `datetime` - Game timestamps
  - Standard library as needed
- **Forbidden:** External libraries, file I/O, `eval()`, `exec()`
- All data processing **in-memory only**
- Programs must **never crash** — handle exceptions gracefully
- Focus on **clarity and design** over code brevity
- Demonstrate **why** abstract patterns are used

---

## 📁 Project Structure
```
your-repo/
├── __init__.py (REQUIRED)
├── ex0/
│   ├── __init__.py (REQUIRED)
│   ├── Card.py
│   ├── CreatureCard.py
│   └── main.py (REQUIRED)
├── ex1/
│   ├── __init__.py (REQUIRED)
│   ├── SpellCard.py
│   ├── ArtifactCard.py
│   ├── Deck.py
│   └── main.py (REQUIRED)
├── ex2/
│   ├── __init__.py (REQUIRED)
│   ├── Combatable.py
│   ├── Magical.py
│   ├── EliteCard.py
│   └── main.py (REQUIRED)
├── ex3/
│   ├── __init__.py (REQUIRED)
│   ├── GameStrategy.py
│   ├── CardFactory.py
│   ├── AggressiveStrategy.py
│   ├── FantasyCardFactory.py
│   ├── GameEngine.py
│   └── main.py (REQUIRED)
└── ex4/
    ├── __init__.py (REQUIRED)
    ├── Rankable.py
    ├── TournamentCard.py
    ├── TournamentPlatform.py
    └── main.py (REQUIRED)
```

**IMPORTANT:** The `__init__.py` file at the repository root is **MANDATORY** for Python to recognize your exercises as packages and enable absolute imports.

---

## 🚀 Execution

All exercises are executed from the repository root:

```bash
python3 -m exN.main
```

Examples:
```bash
python3 -m ex0.main  # Card Foundation
python3 -m ex1.main  # Deck Builder
python3 -m ex2.main  # Ability System
python3 -m ex3.main  # Game Engine
python3 -m ex4.main  # Tournament Platform
```

**Imports:** Use absolute imports between exercises:
```python
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex2.Combatable import Combatable
```

Never use relative imports like `from ..ex0.Card import Card`

---

## 🧠 Architecture Layers

DataDeck is organized into five architectural layers:

| Layer | Exercise | Purpose |
|-------|----------|---------|
| **Foundation** | Ex0 | Abstract blueprints that define universal card contracts |
| **Implementation** | Ex1 | Concrete card types (creatures, spells, artifacts) |
| **Ability** | Ex2 | Multiple interfaces for flexible card abilities |
| **Engine** | Ex3 | Strategy and Factory patterns for game logic |
| **Platform** | Ex4 | Tournament management and ranking systems |

Each layer builds upon the previous, creating a cohesive, extensible system.

---

## 🧠 Learning Philosophy

This project is about **thinking like a software architect**.

You are expected to:
- Understand **when and why** to use abstract classes vs interfaces
- Master **multiple inheritance** and interface composition
- Recognize **design patterns** and apply them appropriately
- Write code that is **extensible** without modification (Open/Closed Principle)
- Build systems that **scale conceptually**, not just syntactically
- Prefer **clear intent** over clever implementations
- Justify your architectural decisions

**The goal is not short code — the goal is professional, maintainable, extensible systems.**

---

## 🧪 Testing & Validation

Test each exercise independently:

```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
```

Each `main.py` file demonstrates the functionality of that layer.

---

## 📋 Key Patterns Mastered

| Pattern | Exercise | Use Case |
|---------|----------|----------|
| **Abstract Base Classes** | Ex0 | Defining universal contracts |
| **Polymorphism** | Ex1 | Different types, same interface |
| **Multiple Inheritance** | Ex2 | Combining multiple abilities |
| **Abstract Factory** | Ex3 | Flexible object creation |
| **Strategy Pattern** | Ex3 | Dynamic behavior selection |
| **Interface Composition** | Ex4 | Advanced system integration |

---

## 🎓 Learning Outcomes

After completing DataDeck, you will be able to:

✅ Design and implement abstract base classes  
✅ Create polymorphic systems that work with any implementation  
✅ Use multiple inheritance safely and effectively  
✅ Apply Abstract Factory Pattern for extensible object creation  
✅ Implement Strategy Pattern for dynamic algorithm selection  
✅ Build complex systems through interface composition  
✅ Write professional, production-grade Python code  
✅ Understand trade-offs in software architecture  

---

## 🛠 Optional: Card Generator Tool

A card generator utility is provided (optional) in the project attachments to help during development.

To use it:
```bash
tar -xzf card_generator.tar.gz
mkdir -p tools
mv card_generator.py tools/
touch tools/__init__.py
```

Then in your code:
```python
from tools.card_generator import CardGenerator
```

**Note:** The `tools/` directory is for development only and should NOT be included in your Git submission.

---

## 📝 Notes

- **Decorators:** The `@abstractmethod` decorator is optional for this activity. You can implement abstract classes with or without it.
- **Simplicity:** Keep card game logic simple — the focus is on demonstrating abstract programming patterns.
- **Modularity:** Each exercise builds on the previous. Ensure your imports work correctly across exercises.
- **Type Hints:** Use type hints everywhere. They make your code more maintainable and catch errors early.

---

## 👤 Author

*Created as part of the 42 curriculum — Advanced Object-Oriented Programming*

If this project helps you master architectural patterns, feel free to ⭐ the repository on GitHub!

**Abstract programming patterns are the foundation of extensible, professional software design. You've learned to build systems that grow and adapt to new requirements without modification. You're thinking like an architect.**

---

*Welcome to DataDeck. Let the games begin.* 🎴✨