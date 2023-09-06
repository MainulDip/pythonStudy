## Python Quick Start:
It's a personalized repo aming python, machine learning, AI, etc study.

### Quick Start Python
Link: 



### Django:

Documentation Link: 
Project Link: 

Tasks:
- Creating Project and App
- urls.py in both project and app level
- adding views and calling that from app level's urls.py
- Create Models
- interactive shell by "python manage.py shell" to interact with database (sqlite3)
- template directory register inside settings.py, layout.html extending in index.html

### Type hinting:
PEP 484 introduced type hints, a.k.a. type annotations. While its main focus was function annotations, it also introduced the notion of type comments to annotate variables:
```py
# 'primes' is a list of integers
primes = []  # type: List[int]

# 'captain' is a string (Note: initial value is a problem)
captain = ...  # type: str

class Starship:
    # 'stats' is a class variable
    stats = {}  # type: Dict[str, int]

# function annotation or type hinting
def greeting(name: str) -> str:
    return 'Hello ' + name
```

This PEP aims at adding syntax to Python for annotating the types of variables (including class variables and instance variables), instead of expressing them through comments:
```py
primes: List[int] = []

captain: str  # Note: no initial value!

class Starship:
    stats: ClassVar[Dict[str, int]] = {}
```